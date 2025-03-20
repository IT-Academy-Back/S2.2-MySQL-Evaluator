import os
import mysql.connector
import re
from decimal import Decimal

# Conectar a MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="tienda"
)
cursor = db.cursor()

# Leer queries desde queries.sql
def read_queries(file_path="./queries/queries.sql"):
    with open(file_path, "r") as f:
        queries = f.read()
    return [q.strip() for q in re.split(r';\s*\n', queries) if q.strip()]

# Función para formatear valores (misma lógica que en la evaluación)
def format_value(value):
    """ Formatea valores numéricos para garantizar siempre 2 decimales. """
    if value is None:
        return "NULL"
    
    if isinstance(value, (int, float, Decimal)):
        return f"{Decimal(value):.2f}"  # 🔹 Asegura siempre 2 decimales

    return str(value)  # Para cadenas y otros valores


# Crear carpeta si no existe
os.makedirs("expected_results", exist_ok=True)

# Obtener las queries del archivo
queries = read_queries()

# Ejecutar cada query y guardar el resultado en un archivo .out
for i, query in enumerate(queries, start=1):
    try:
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        result = cursor.fetchall()

        # Formatear resultados
        result_formatted = [" | ".join(columns)]
        for row in result:
            formatted_row = " | ".join(format_value(value) for value in row)
            result_formatted.append(formatted_row)

        # Guardar en un archivo .out
        with open(f"expected_results/query_{i}.out", "w") as f:
            f.write("\n".join(result_formatted))

        print(f"✅ Resultados esperados guardados en: expected_results/query_{i}.out")

    except Exception as e:
        print(f"⚠️ Error en Query {i}: {str(e)}")

# Cerrar conexión
cursor.close()
db.close()
print("🎉 Archivos de resultados esperados generados con éxito.")
