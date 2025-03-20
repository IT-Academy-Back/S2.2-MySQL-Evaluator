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
        database="test_db"
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

    # 🔍 Depuración: Imprimir resultados en bruto antes de aplicar formato
    print(f"\n🔍 QUERY EJECUTADA: {query}")
    print(f"📌 COLUMNAS: {columns}")
    print(f"📌 RESULTADOS CRUDOS: {result}")

    formatted_result = [[format_value(value) for value in row] for row in result]

    # 🔍 Depuración: Imprimir resultados después del formateo
    print(f"📌 RESULTADOS FORMATEADOS: {formatted_result}")

    return columns, formatted_result



def format_value(value):
    """
    Formatea valores numéricos para evitar diferencias en la comparación.
    - Si el valor es None, devuelve "NULL".
    - Si es un número decimal con parte decimal 0, lo convierte a entero.
    - Si tiene decimales, lo redondea a 2 decimales.
    - En otro caso, lo convierte a string.
    """
    if value is None:
        return "NULL"
    if isinstance(value, Decimal):  # Si es un Decimal de MySQL, lo convertimos correctamente
        value = float(value)  # Convertimos Decimal a float
    if isinstance(value, float):
        if value.is_integer():  # Si es un número entero (ej. 2900.0)
            return str(int(value))  # Convertir a string sin decimales
        else:
            return f"{value:.2f}"  # Si tiene decimales, mantener 2 decimales
    return str(value)



def format_results(columns, result):
    """Formatea los resultados con cabecera de columnas."""
    formatted_result = [" | ".join(columns)]
    for row in result:
        formatted_row = " | ".join(row)  # Los valores ya vienen formateados
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

        # Depuración: Mostrar las diferencias entre ambos formatos
        debug_info = (
            f"\n### 🔎 Depuración de Query {query_index}:\n"
            f"📌 **Resultado Obtenido:**\n{result_formatted}\n"
            f"📌 **Resultado Esperado:**\n{expected}\n"
        )

        return f"- ❌ Query {query_index}: **Incorrecto** (Diferencias detectadas)\n```diff\n{diff_text}\n```\n{debug_info}"



def analyze_performance(cursor, query):
    """Ejecuta EXPLAIN en la consulta y analiza el rendimiento."""
    start_time = time.time()  # ⏱ Medir tiempo de ejecución
    cursor.execute(f"EXPLAIN {query}")
    explain_result = cursor.fetchall()
    execution_time = round((time.time() - start_time) * 1000, 2)  # ⏱ en ms

    report = "### 🔍 Análisis de Rendimiento (`EXPLAIN`)\n"

    for row in explain_result:
        scan_type = row[1] if row[1] else "N/A"
        index_used = row[5] if row[5] else "❌ Ninguno"

        # Extraer métricas de rendimiento
        rows_examined = row[8] if row[8] is not None else 0
        filtered = row[9] if row[9] is not None else 100  # Si NULL, asumimos 100%
        rows_returned = 1  # Estimación, ajustar según el resultado real

        # Si la query realmente se ejecutó, medimos `rows_returned`
        try:
            cursor.execute(query)
            rows_returned = len(cursor.fetchall())
        except:
            pass  # Si la query no se puede ejecutar directamente, omitimos esto

        # 📌 Si `rows_examined = 0`, intentamos obtener `COUNT(*)`
        if rows_examined == 0:
            try:
                match = re.search(r'FROM\s+([a-zA-Z_][a-zA-Z0-9_]*)', query, re.IGNORECASE)
                if match:
                    table_name = match.group(1)
                    count_query = f"SELECT COUNT(*) FROM {table_name}"
                    cursor.execute(count_query)
                    rows_examined = cursor.fetchone()[0]  # Reemplazamos `0` con el número de filas reales
            except:
                rows_examined = "Desconocido"

        # Detectar consultas ineficientes
        inefficiency_flag = ""
        if scan_type == "ALL":
            inefficiency_flag = "⚠️ **Escaneo completo detectado.**"
        elif rows_examined > 1000 and rows_returned < rows_examined * 0.05:
            inefficiency_flag = "⚠️ **Demasiadas filas examinadas en comparación con las filas devueltas.**"

        report += f"- **Tipo de escaneo:** `{scan_type}`\n"
        report += f"- **Índice usado:** `{index_used}`\n"
        report += f"- **Filas analizadas:** `{rows_examined}`\n"
        report += f"- **Filas devueltas:** `{rows_returned}`\n"
        report += f"- **Tiempo de ejecución:** `{execution_time} ms`\n"
        
        if inefficiency_flag:
            report += f"- {inefficiency_flag}\n"

    cursor.fetchall()  # 🔹 Consumir cualquier posible resultado pendiente
    report += "\n"
    return report


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

        except Exception as e:
            report += f"- ❌ **Error al ejecutar Query {i}**: {str(e)}\n"

    with open("RESULTADOS.md", "w") as f:
        f.write(report)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
