import mysql.connector
import difflib
import re
from decimal import Decimal
import time

def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="tienda",
        charset="utf8mb4",
        use_unicode=True,  
        collation='utf8mb4_general_ci'
    )

def read_queries(file_path="./queries/queries.sql"):
    with open(file_path, "r") as f:
        queries = f.read()
    return [q.strip() for q in re.split(r';\s*\n', queries) if q.strip()]

def execute_query(cursor, query):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    result = cursor.fetchall()
    formatted_result = [[format_value(value) for value in row] for row in result]
    return columns, formatted_result

def format_value(value):
    if value is None:
        return "NULL"
    if isinstance(value, (int, float, Decimal)):
        return f"{Decimal(value):.2f}"
    return str(value)

def read_expected_result(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def compare_results(query_index, result_formatted, expected):
    if result_formatted == expected:
        return f"## ✅ Query {query_index}: Correcto\n"
    else:
        diff_text = "\n".join(difflib.unified_diff(expected, result_formatted, lineterm=""))
        return f"## ❌ Query {query_index}: Incorrecto\n```diff\n{diff_text}\n```\n"

def analyze_performance(cursor, query):
    start_time = time.time()
    cursor.execute(f"EXPLAIN {query}")
    explain_result = cursor.fetchall()
    execution_time = round((time.time() - start_time) * 1000, 2)

    issues = set()
    possible_keys = set()
    indices_usados = set()
    join_without_index = False

    for row in explain_result:
        scan_type = row[1] if row[1] else "N/A"
        keys_sugeridos = row[4] if row[4] else None
        indice_actual = row[5] if row[5] and row[5] != "NULL" else None

        # Guardar índices usados si existen
        if indice_actual:
            indices_usados.add(indice_actual)

        # Guardar índices posibles
        if keys_sugeridos:
            possible_keys.add(keys_sugeridos)

    # 🚨 Si hay JOIN pero ningún índice se usó
    if "JOIN" in query.upper() and not indices_usados:
        if possible_keys:
            issues.add(f"⚠️ `JOIN` podría optimizarse con los índices sugeridos: {', '.join(possible_keys)}.")
        else:
            issues.add("🚨 `JOIN` sin índice. Revisar claves foráneas e índices.")

    # ⚠️ Evitar SELECT *
    if "SELECT *" in query.upper():
        issues.add("⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.")

    # ⚠️ Considerar EXISTS en lugar de IN
    if " IN (" in query.upper() and "EXISTS" not in query.upper():
        issues.add("⚠️ Considerar `EXISTS` en lugar de `IN` para eficiencia.")

    # 📋 Construcción del informe
    report = f"- ⏱ Tiempo: {execution_time} ms\n"

    if indices_usados:
        report += f"- ✅ Se usó índice(s) en la consulta: {', '.join(indices_usados)}\n"
    else:
        report += "- 🔍 No se usó ningún índice en esta consulta.\n"

    if issues:
        report += "\n🚨 **Problemas detectados:**\n" + "\n".join(issues) + "\n"

    return report

def main():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SET NAMES utf8mb4;")

    queries = read_queries()
    report = "# 📊 Análisis de Consultas SQL\n\n"

    for i, query in enumerate(queries, start=1):
        try:
            columns, result = execute_query(cursor, query)
            result_formatted = [" | ".join(columns)] + [" | ".join(row) for row in result]

            expected_file = f"src/expected_results/query_{i}.out"
            expected = read_expected_result(expected_file)

            report += compare_results(i, result_formatted, expected)
            report += analyze_performance(cursor, query)
            report += "\n---\n"

        except Exception as e:
            report += f"## ❌ Query {i}: Error\n- **Descripción**: {str(e)}\n\n"

    with open("RESULTADOS.md", "w") as f:
        f.write(report)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
