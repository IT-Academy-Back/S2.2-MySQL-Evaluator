# 📊 Análisis de Consultas SQL

## ✅ Query 1: Correcto
- ⏱ Tiempo: 0.39 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 2: Correcto
- ⏱ Tiempo: 0.34 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 3: Correcto
- ⏱ Tiempo: 0.36 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 4: Correcto
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 5: Correcto
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 6: Correcto
- ⏱ Tiempo: 0.34 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 7: Correcto
- ⏱ Tiempo: 0.35 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 8: Correcto
- ⏱ Tiempo: 0.34 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 9: Correcto
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 10: Correcto
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 11: Correcto
- ⏱ Tiempo: 0.32 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 12: Correcto
- ⏱ Tiempo: 0.3 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 13: Correcto
- ⏱ Tiempo: 0.31 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 14: Correcto
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 15: Correcto
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 16: Correcto
- ⏱ Tiempo: 0.31 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 17: Correcto
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 18: Correcto
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 19: Correcto
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 20: Correcto
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 21: Correcto
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 22: Correcto
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 23: Correcto
- ⏱ Tiempo: 0.34 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 24: Correcto
- ⏱ Tiempo: 0.36 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 25: Correcto
- ⏱ Tiempo: 0.38 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 26: Correcto
- ⏱ Tiempo: 0.39 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 27: Incorrecto
```diff
--- 
+++ 
@@ -1,6 +1,6 @@
 codigo | nombre | precio | codigo_fabricante
-1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
 6.00 | Monitor 24 LED Full HD | 202.00 | 1.00
 7.00 | Monitor 27 LED Full HD | 245.99 | 1.00
 10.00 | Impresora HP Deskjet 3720 | 59.99 | 3.00
 11.00 | Impresora HP Laserjet Pro M26nw | 180.00 | 3.00
+1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
```
- ⏱ Tiempo: 0.36 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 28: Incorrecto
```diff
--- 
+++ 
@@ -1,6 +1,6 @@
 codigo | nombre | precio | codigo_fabricante
-1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
 6.00 | Monitor 24 LED Full HD | 202.00 | 1.00
 7.00 | Monitor 27 LED Full HD | 245.99 | 1.00
 10.00 | Impresora HP Deskjet 3720 | 59.99 | 3.00
 11.00 | Impresora HP Laserjet Pro M26nw | 180.00 | 3.00
+1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
```
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.
⚠️ Considerar `EXISTS` en lugar de `IN` para eficiencia.

---
## ✅ Query 29: Correcto
- ⏱ Tiempo: 0.38 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 30: Correcto
- ⏱ Tiempo: 0.41 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 31: Correcto
- ⏱ Tiempo: 0.39 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 32: Correcto
- ⏱ Tiempo: 0.38 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 33: Correcto
- ⏱ Tiempo: 0.4 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 34: Correcto
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 35: Correcto
- ⏱ Tiempo: 0.38 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 36: Correcto
- ⏱ Tiempo: 0.41 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 37: Correcto
- ⏱ Tiempo: 0.39 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 38: Correcto
- ⏱ Tiempo: 0.42 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 39: Correcto
- ⏱ Tiempo: 0.42 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 40: Correcto
- ⏱ Tiempo: 0.46 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
