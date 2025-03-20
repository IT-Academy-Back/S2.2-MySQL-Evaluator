import mysql.connector
import difflib
import re
from decimal import Decimal
import time

def connect_db():
    """Establece la conexión con la base de datos MySQL."""
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="tienda"
    )

def read_queries(file_path="./queries/queries.sql"):
    """Lee y separa las queries en un archivo SQL."""
    with open(file_path, "r") as f:
        queries = f.read()
    return [q.strip() for q in re.split(r';\s*\n', queries) if q.strip()]

def execute_query(cursor, query):
    """Ejecuta una query y devuelve los resultados junto con los nombres de las columnas."""
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    result = cursor.fetchall()
    formatted_result = [[format_value(value) for value in row] for row in result]
    return columns, formatted_result

def format_value(value):
    """ Formatea valores numéricos con 2 decimales y convierte `None` a "NULL". """
    if value is None:
        return "NULL"
    if isinstance(value, (int, float, Decimal)):
        return f"{Decimal(value):.2f}"  # 🔹 Asegura 2 decimales
    return str(value)

def format_results(columns, result):
    """Formatea los resultados con cabecera de columnas."""
    formatted_result = [" | ".join(columns)]
    for row in result:
        formatted_row = " | ".join(row)
        formatted_result.append(formatted_row)
    return formatted_result

def read_expected_result(file_path):
    """Lee el resultado esperado desde un archivo."""
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def compare_results(query_index, result_formatted, expected):
    """Compara los resultados obtenidos con los esperados y devuelve el reporte."""
    if result_formatted == expected:
        return f"- ✅ Query {query_index}: **Correcto**\n"
    else:
        diff_text = "\n".join(difflib.unified_diff(expected, result_formatted, lineterm=""))
        return f"- ❌ Query {query_index}: **Incorrecto** (Diferencias detectadas)\n```diff\n{diff_text}\n```\n"

def analyze_performance(cursor, query):
    """Ejecuta EXPLAIN en la consulta y analiza el rendimiento."""
    start_time = time.time()  # ⏱ Medir tiempo de ejecución
    cursor.execute(f"EXPLAIN {query}")
    explain_result = cursor.fetchall()
    execution_time = round((time.time() - start_time) * 1000, 2)  # ⏱ en ms

    report = "### 🔍 Análisis de Rendimiento (`EXPLAIN`)\n"
    inefficiency_flag = ""

    for row in explain_result:
        scan_type = row[1] if row[1] else "N/A"
        index_used = row[5] if row[5] else "❌ Ninguno"
        rows_examined = row[8] if row[8] is not None else 0
        filtered = row[9] if row[9] is not None else 100  # Si NULL, asumimos 100%
        rows_returned = 0  # Inicialización

        # Convertir valores a enteros
        rows_examined = int(rows_examined) if isinstance(rows_examined, (int, float, Decimal)) else 0

        # Ejecutar la query real para contar filas devueltas
        try:
            cursor.execute(query)
            rows_returned = len(cursor.fetchall())  # Contar filas devueltas
        except:
            rows_returned = "Error en ejecución"

        # 📌 Si `rows_examined = 0`, intentamos obtener `COUNT(*)`
        if rows_examined == 0:
            try:
                match = re.search(r'FROM\s+([a-zA-Z_][a-zA-Z0-9_]*)', query, re.IGNORECASE)
                if match:
                    table_name = match.group(1)
                    count_query = f"SELECT COUNT(*) FROM {table_name}"
                    cursor.execute(count_query)
                    rows_examined = int(cursor.fetchone()[0])  # Convertir a entero
            except:
                rows_examined = "Desconocido"

        # ⚠️ Detectar problemas
        if scan_type == "ALL":
            inefficiency_flag += "⚠️ **Escaneo completo detectado.**\n"
        if isinstance(rows_examined, int) and rows_examined > 1000 and rows_returned < rows_examined * 0.05:
            inefficiency_flag += "⚠️ **Demasiadas filas examinadas en comparación con las filas devueltas.**\n"
        if index_used == "❌ Ninguno" and rows_examined > 100:
            inefficiency_flag += "⚠️ **La consulta analiza demasiadas filas sin usar índices.**\n"

        # Agregar datos al reporte
        report += f"- **Tipo de escaneo:** `{scan_type}`\n"
        report += f"- **Índice usado:** `{index_used}`\n"
        report += f"- **Filas analizadas:** `{rows_examined}`\n"
        report += f"- **Filas devueltas:** `{rows_returned}`\n"
        report += f"- **Tiempo de ejecución:** `{execution_time} ms`\n"

    if inefficiency_flag:
        report += f"\n{inefficiency_flag}"

    report += "\n"
    return report


def optimization_checklist(scan_type, index_used, query):
    """Genera un checklist de optimización basado en la consulta y el análisis de `EXPLAIN`."""
    return (
        "### ✅ Checklist de Optimización\n"
        f"- 🔍 **Uso de Índices:** {'✅' if index_used != '❌ Ninguno' else '❌ No se usó índice'}\n"
        f"- 📉 **Reducción de Filas Analizadas:** {'✅' if scan_type != 'ALL' else '⚠️ Posible escaneo completo'}\n"
        f"- 🎯 **Evitar `SELECT *`:** {'✅' if '*' not in query else '⚠️ Revisar: Usar solo las columnas necesarias'}\n"
        f"- 🔗 **Optimización de `JOINs`:** {'✅ Revisar índices en JOINs' if 'JOIN' in query else 'N/A'}\n"
        f"- 📊 **Uso de `ORDER BY` y `GROUP BY` con Índices:** {'✅' if 'ORDER BY' in query or 'GROUP BY' in query else 'N/A'}\n"
        f"- 🚀 **Uso de `EXISTS` en lugar de `IN` (si aplica):** {'✅' if ' IN (' in query else 'N/A'}\n"
        f"- 🔒 **Evitar Locks Innecesarios:** {'✅ Revisar si se bloquean muchas filas' if 'UPDATE' in query or 'DELETE' in query else 'N/A'}\n"
        f"- 💾 **Optimización de Tipos de Datos:** ✅ Revisar tipos de datos y longitud de columnas\n"
    )

def main():
    """Función principal que ejecuta la evaluación de queries."""
    db = connect_db()
    cursor = db.cursor()
    queries = read_queries()
    report = "# 📊 Resultados de Evaluación SQL\n\n"

    for i, query in enumerate(queries, start=1):
        report += f"## Query {i}\n"

        try:
            columns, result = execute_query(cursor, query)
            result_formatted = format_results(columns, result)

            expected_file = f"expected_results/query_{i}.out"
            expected = read_expected_result(expected_file)

            report += compare_results(i, result_formatted, expected)
            report += analyze_performance(cursor, query)

            # Agregar checklist de optimización
            cursor.execute(f"EXPLAIN {query}")
            explain_result = cursor.fetchall()
            scan_type = explain_result[0][1] if explain_result else "N/A"
            index_used = explain_result[0][5] if explain_result else "❌ Ninguno"

            report += optimization_checklist(scan_type, index_used, query)

        except Exception as e:
            report += f"- ❌ **Error al ejecutar Query {i}**: {str(e)}\n"

    with open("RESULTADOS.md", "w") as f:
        f.write(report)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
