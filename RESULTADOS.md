# 📊 Análisis de Consultas SQL

## ❌ Query 1: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
-nombre
-Disco dur SATA3 1TB
-Memoria RAM DDR4 8GB
-Disco SSD 1 TB
-GeForce GTX 1050Ti
-GeForce GTX 1080 Xtreme
-Monitor 24 LED Full HD
-Monitor 27 LED Full HD
-Porttil Yoga 520
-Porttil Ideapd 320
-Impresora HP Deskjet 3720
-Impresora HP Laserjet Pro M26nw
+codigo | nombre | precio | codigo_fabricante
+1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
+2.00 | Memoria RAM DDR4 8GB | 120.00 | 6.00
+3.00 | Disco SSD 1 TB | 150.99 | 4.00
+4.00 | GeForce GTX 1050Ti | 185.00 | 7.00
+5.00 | GeForce GTX 1080 Xtreme | 755.00 | 6.00
+6.00 | Monitor 24 LED Full HD | 202.00 | 1.00
+7.00 | Monitor 27 LED Full HD | 245.99 | 1.00
+8.00 | Portátil Yoga 520 | 559.00 | 2.00
+9.00 | Portátil Ideapd 320 | 444.00 | 2.00
+10.00 | Impresora HP Deskjet 3720 | 59.99 | 3.00
+11.00 | Impresora HP Laserjet Pro M26nw | 180.00 | 3.00
```
- ⏱ Tiempo: 0.4 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 2: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nombre | precio
-Disco dur SATA3 1TB | 86.99
+Disco duro SATA3 1TB | 86.99
 Memoria RAM DDR4 8GB | 120.00
 Disco SSD 1 TB | 150.99
 GeForce GTX 1050Ti | 185.00
 GeForce GTX 1080 Xtreme | 755.00
 Monitor 24 LED Full HD | 202.00
 Monitor 27 LED Full HD | 245.99
-Porttil Yoga 520 | 559.00
-Porttil Ideapd 320 | 444.00
+Portátil Yoga 520 | 559.00
+Portátil Ideapd 320 | 444.00
 Impresora HP Deskjet 3720 | 59.99
 Impresora HP Laserjet Pro M26nw | 180.00
```
- ⏱ Tiempo: 0.37 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 3: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 codigo | nombre | precio | codigo_fabricante
-1.00 | Disco dur SATA3 1TB | 86.99 | 5.00
+1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
 2.00 | Memoria RAM DDR4 8GB | 120.00 | 6.00
 3.00 | Disco SSD 1 TB | 150.99 | 4.00
 4.00 | GeForce GTX 1050Ti | 185.00 | 7.00
 5.00 | GeForce GTX 1080 Xtreme | 755.00 | 6.00
 6.00 | Monitor 24 LED Full HD | 202.00 | 1.00
 7.00 | Monitor 27 LED Full HD | 245.99 | 1.00
-8.00 | Porttil Yoga 520 | 559.00 | 2.00
-9.00 | Porttil Ideapd 320 | 444.00 | 2.00
+8.00 | Portátil Yoga 520 | 559.00 | 2.00
+9.00 | Portátil Ideapd 320 | 444.00 | 2.00
 10.00 | Impresora HP Deskjet 3720 | 59.99 | 3.00
 11.00 | Impresora HP Laserjet Pro M26nw | 180.00 | 3.00
```
- ⏱ Tiempo: 0.36 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 4: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nombre | precio | precio_usd
-Disco dur SATA3 1TB | 86.99 | 95.69
+Disco duro SATA3 1TB | 86.99 | 95.69
 Memoria RAM DDR4 8GB | 120.00 | 132.00
 Disco SSD 1 TB | 150.99 | 166.09
 GeForce GTX 1050Ti | 185.00 | 203.50
 GeForce GTX 1080 Xtreme | 755.00 | 830.50
 Monitor 24 LED Full HD | 202.00 | 222.20
 Monitor 27 LED Full HD | 245.99 | 270.59
-Porttil Yoga 520 | 559.00 | 614.90
-Porttil Ideapd 320 | 444.00 | 488.40
+Portátil Yoga 520 | 559.00 | 614.90
+Portátil Ideapd 320 | 444.00 | 488.40
 Impresora HP Deskjet 3720 | 59.99 | 65.99
 Impresora HP Laserjet Pro M26nw | 180.00 | 198.00
```
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 5: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 Nom de producte | Euros | Dòlars
-Disco dur SATA3 1TB | 86.99 | 95.69
+Disco duro SATA3 1TB | 86.99 | 95.69
 Memoria RAM DDR4 8GB | 120.00 | 132.00
 Disco SSD 1 TB | 150.99 | 166.09
 GeForce GTX 1050Ti | 185.00 | 203.50
 GeForce GTX 1080 Xtreme | 755.00 | 830.50
 Monitor 24 LED Full HD | 202.00 | 222.20
 Monitor 27 LED Full HD | 245.99 | 270.59
-Porttil Yoga 520 | 559.00 | 614.90
-Porttil Ideapd 320 | 444.00 | 488.40
+Portátil Yoga 520 | 559.00 | 614.90
+Portátil Ideapd 320 | 444.00 | 488.40
 Impresora HP Deskjet 3720 | 59.99 | 65.99
 Impresora HP Laserjet Pro M26nw | 180.00 | 198.00
```
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 6: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nom | precio
-DISCO DUR SATA3 1TB | 86.99
+DISCO DURO SATA3 1TB | 86.99
 MEMORIA RAM DDR4 8GB | 120.00
 DISCO SSD 1 TB | 150.99
 GEFORCE GTX 1050TI | 185.00
 GEFORCE GTX 1080 XTREME | 755.00
 MONITOR 24 LED FULL HD | 202.00
 MONITOR 27 LED FULL HD | 245.99
-PORTTIL YOGA 520 | 559.00
-PORTTIL IDEAPD 320 | 444.00
+PORTÁTIL YOGA 520 | 559.00
+PORTÁTIL IDEAPD 320 | 444.00
 IMPRESORA HP DESKJET 3720 | 59.99
 IMPRESORA HP LASERJET PRO M26NW | 180.00
```
- ⏱ Tiempo: 0.38 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 7: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nom | precio
-disco dur sata3 1tb | 86.99
+disco duro sata3 1tb | 86.99
 memoria ram ddr4 8gb | 120.00
 disco ssd 1 tb | 150.99
 geforce gtx 1050ti | 185.00
 geforce gtx 1080 xtreme | 755.00
 monitor 24 led full hd | 202.00
 monitor 27 led full hd | 245.99
-porttil yoga 520 | 559.00
-porttil ideapd 320 | 444.00
+portátil yoga 520 | 559.00
+portátil ideapd 320 | 444.00
 impresora hp deskjet 3720 | 59.99
 impresora hp laserjet pro m26nw | 180.00
```
- ⏱ Tiempo: 0.42 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 8: Correcto
- ⏱ Tiempo: 0.4 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 9: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nombre | preu
-Disco dur SATA3 1TB | 87.00
+Disco duro SATA3 1TB | 87.00
 Memoria RAM DDR4 8GB | 120.00
 Disco SSD 1 TB | 151.00
 GeForce GTX 1050Ti | 185.00
 GeForce GTX 1080 Xtreme | 755.00
 Monitor 24 LED Full HD | 202.00
 Monitor 27 LED Full HD | 246.00
-Porttil Yoga 520 | 559.00
-Porttil Ideapd 320 | 444.00
+Portátil Yoga 520 | 559.00
+Portátil Ideapd 320 | 444.00
 Impresora HP Deskjet 3720 | 60.00
 Impresora HP Laserjet Pro M26nw | 180.00
```
- ⏱ Tiempo: 0.37 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 10: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nombre | preu
-Disco dur SATA3 1TB | 86.00
+Disco duro SATA3 1TB | 86.00
 Memoria RAM DDR4 8GB | 120.00
 Disco SSD 1 TB | 150.00
 GeForce GTX 1050Ti | 185.00
 GeForce GTX 1080 Xtreme | 755.00
 Monitor 24 LED Full HD | 202.00
 Monitor 27 LED Full HD | 245.00
-Porttil Yoga 520 | 559.00
-Porttil Ideapd 320 | 444.00
+Portátil Yoga 520 | 559.00
+Portátil Ideapd 320 | 444.00
 Impresora HP Deskjet 3720 | 59.00
 Impresora HP Laserjet Pro M26nw | 180.00
```
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 11: Correcto
- ⏱ Tiempo: 0.33 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 12: Correcto
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 13: Correcto
- ⏱ Tiempo: 0.33 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 14: Incorrecto
```diff
--- 
+++ 
@@ -1,5 +1,5 @@
 nombre | precio
-Disco dur SATA3 1TB | 86.99
+Disco duro SATA3 1TB | 86.99
 Disco SSD 1 TB | 150.99
 GeForce GTX 1050Ti | 185.00
 GeForce GTX 1080 Xtreme | 755.00
@@ -8,5 +8,5 @@
 Memoria RAM DDR4 8GB | 120.00
 Monitor 24 LED Full HD | 202.00
 Monitor 27 LED Full HD | 245.99
-Porttil Ideapd 320 | 444.00
-Porttil Yoga 520 | 559.00
+Portátil Ideapd 320 | 444.00
+Portátil Yoga 520 | 559.00
```
- ⏱ Tiempo: 0.35 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 15: Correcto
- ⏱ Tiempo: 0.34 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 16: Correcto
- ⏱ Tiempo: 0.32 ms
- 🔍 No se usó ningún índice en esta consulta.

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 17: Correcto
- ⏱ Tiempo: 0.31 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ✅ Query 18: Correcto
- ⏱ Tiempo: 0.34 ms
- 🔍 No se usó ningún índice en esta consulta.

---
## ❌ Query 19: Incorrecto
```diff
--- 
+++ 
@@ -1,3 +1,3 @@
 nombre
-Porttil Yoga 520
-Porttil Ideapd 320
+Portátil Yoga 520
+Portátil Ideapd 320
```
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ❌ Query 20: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 nombre | precio | fabricant
-Disco dur SATA3 1TB | 86.99 | Seagate
+Disco duro SATA3 1TB | 86.99 | Seagate
 Memoria RAM DDR4 8GB | 120.00 | Crucial
 Disco SSD 1 TB | 150.99 | Samsung
 GeForce GTX 1050Ti | 185.00 | Gigabyte
 GeForce GTX 1080 Xtreme | 755.00 | Crucial
 Monitor 24 LED Full HD | 202.00 | Asus
 Monitor 27 LED Full HD | 245.99 | Asus
-Porttil Yoga 520 | 559.00 | Lenovo
-Porttil Ideapd 320 | 444.00 | Lenovo
+Portátil Yoga 520 | 559.00 | Lenovo
+Portátil Ideapd 320 | 444.00 | Lenovo
 Impresora HP Deskjet 3720 | 59.99 | Hewlett-Packard
 Impresora HP Laserjet Pro M26nw | 180.00 | Hewlett-Packard
```
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ❌ Query 21: Incorrecto
```diff
--- 
+++ 
@@ -6,7 +6,7 @@
 GeForce GTX 1050Ti | 185.00 | Gigabyte
 Impresora HP Deskjet 3720 | 59.99 | Hewlett-Packard
 Impresora HP Laserjet Pro M26nw | 180.00 | Hewlett-Packard
-Porttil Yoga 520 | 559.00 | Lenovo
-Porttil Ideapd 320 | 444.00 | Lenovo
+Portátil Yoga 520 | 559.00 | Lenovo
+Portátil Ideapd 320 | 444.00 | Lenovo
 Disco SSD 1 TB | 150.99 | Samsung
-Disco dur SATA3 1TB | 86.99 | Seagate
+Disco duro SATA3 1TB | 86.99 | Seagate
```
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ❌ Query 22: Incorrecto
```diff
--- 
+++ 
@@ -1,12 +1,12 @@
 codigo | nombre | Codi fabricant | Fabricant
-1.00 | Disco dur SATA3 1TB | 5.00 | Seagate
+1.00 | Disco duro SATA3 1TB | 5.00 | Seagate
 2.00 | Memoria RAM DDR4 8GB | 6.00 | Crucial
 3.00 | Disco SSD 1 TB | 4.00 | Samsung
 4.00 | GeForce GTX 1050Ti | 7.00 | Gigabyte
 5.00 | GeForce GTX 1080 Xtreme | 6.00 | Crucial
 6.00 | Monitor 24 LED Full HD | 1.00 | Asus
 7.00 | Monitor 27 LED Full HD | 1.00 | Asus
-8.00 | Porttil Yoga 520 | 2.00 | Lenovo
-9.00 | Porttil Ideapd 320 | 2.00 | Lenovo
+8.00 | Portátil Yoga 520 | 2.00 | Lenovo
+9.00 | Portátil Ideapd 320 | 2.00 | Lenovo
 10.00 | Impresora HP Deskjet 3720 | 3.00 | Hewlett-Packard
 11.00 | Impresora HP Laserjet Pro M26nw | 3.00 | Hewlett-Packard
```
- ⏱ Tiempo: 0.36 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 23: Correcto
- ⏱ Tiempo: 0.36 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 24: Correcto
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ❌ Query 25: Incorrecto
```diff
--- 
+++ 
@@ -1,3 +1,3 @@
 codigo | nombre | precio | codigo_fabricante
-8.00 | Porttil Yoga 520 | 559.00 | 2.00
-9.00 | Porttil Ideapd 320 | 444.00 | 2.00
+8.00 | Portátil Yoga 520 | 559.00 | 2.00
+9.00 | Portátil Ideapd 320 | 444.00 | 2.00
```
- ⏱ Tiempo: 0.41 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 26: Correcto
- ⏱ Tiempo: 0.41 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 27: Incorrecto
```diff
--- 
+++ 
@@ -3,4 +3,4 @@
 7.00 | Monitor 27 LED Full HD | 245.99 | 1.00
 10.00 | Impresora HP Deskjet 3720 | 59.99 | 3.00
 11.00 | Impresora HP Laserjet Pro M26nw | 180.00 | 3.00
-1.00 | Disco dur SATA3 1TB | 86.99 | 5.00
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
@@ -3,4 +3,4 @@
 7.00 | Monitor 27 LED Full HD | 245.99 | 1.00
 10.00 | Impresora HP Deskjet 3720 | 59.99 | 3.00
 11.00 | Impresora HP Laserjet Pro M26nw | 180.00 | 3.00
-1.00 | Disco dur SATA3 1TB | 86.99 | 5.00
+1.00 | Disco duro SATA3 1TB | 86.99 | 5.00
```
- ⏱ Tiempo: 0.35 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.
⚠️ Considerar `EXISTS` en lugar de `IN` para eficiencia.

---
## ❌ Query 29: Incorrecto
```diff
--- 
+++ 
@@ -1,3 +1,3 @@
 nombre | precio
-Disco dur SATA3 1TB | 86.99
+Disco duro SATA3 1TB | 86.99
 GeForce GTX 1050Ti | 185.00
```
- ⏱ Tiempo: 0.4 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 30: Correcto
- ⏱ Tiempo: 0.38 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ❌ Query 31: Incorrecto
```diff
--- 
+++ 
@@ -1,7 +1,7 @@
 nombre | precio | fabricant
 GeForce GTX 1080 Xtreme | 755.00 | Crucial
-Porttil Yoga 520 | 559.00 | Lenovo
-Porttil Ideapd 320 | 444.00 | Lenovo
+Portátil Yoga 520 | 559.00 | Lenovo
+Portátil Ideapd 320 | 444.00 | Lenovo
 Monitor 27 LED Full HD | 245.99 | Asus
 Monitor 24 LED Full HD | 202.00 | Asus
 GeForce GTX 1050Ti | 185.00 | Gigabyte
```
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ✅ Query 32: Correcto
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante, PRIMARY

---
## ❌ Query 33: Incorrecto
```diff
--- 
+++ 
@@ -1,14 +1,14 @@
 fabricant | producte
+Asus | Monitor 27 LED Full HD
 Asus | Monitor 24 LED Full HD
-Asus | Monitor 27 LED Full HD
-Lenovo | Porttil Yoga 520
-Lenovo | Porttil Ideapd 320
+Lenovo | Portátil Ideapd 320
+Lenovo | Portátil Yoga 520
+Hewlett-Packard | Impresora HP Laserjet Pro M26nw
 Hewlett-Packard | Impresora HP Deskjet 3720
-Hewlett-Packard | Impresora HP Laserjet Pro M26nw
 Samsung | Disco SSD 1 TB
-Seagate | Disco dur SATA3 1TB
+Seagate | Disco duro SATA3 1TB
+Crucial | GeForce GTX 1080 Xtreme
 Crucial | Memoria RAM DDR4 8GB
-Crucial | GeForce GTX 1080 Xtreme
 Gigabyte | GeForce GTX 1050Ti
 Huawei | NULL
 Xiaomi | NULL
```
- ⏱ Tiempo: 0.41 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 34: Correcto
- ⏱ Tiempo: 0.37 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ❌ Query 35: Incorrecto
```diff
--- 
+++ 
@@ -1,3 +1,3 @@
 codigo | nombre | precio | codigo_fabricante
-8.00 | Porttil Yoga 520 | 559.00 | 2.00
-9.00 | Porttil Ideapd 320 | 444.00 | 2.00
+8.00 | Portátil Yoga 520 | 559.00 | 2.00
+9.00 | Portátil Ideapd 320 | 444.00 | 2.00
```
- ⏱ Tiempo: 0.4 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 36: Incorrecto
```diff
--- 
+++ 
@@ -1,2 +1,2 @@
 codigo | nombre | precio | codigo_fabricante
-8.00 | Porttil Yoga 520 | 559.00 | 2.00
+8.00 | Portátil Yoga 520 | 559.00 | 2.00
```
- ⏱ Tiempo: 0.43 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ❌ Query 37: Incorrecto
```diff
--- 
+++ 
@@ -1,2 +1,2 @@
 nombre
-Porttil Yoga 520
+Portátil Yoga 520
```
- ⏱ Tiempo: 0.41 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ✅ Query 38: Correcto
- ⏱ Tiempo: 0.39 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

---
## ❌ Query 39: Incorrecto
```diff
--- 
+++ 
@@ -1,3 +1,3 @@
 codigo | nombre | precio | codigo_fabricante
 5.00 | GeForce GTX 1080 Xtreme | 755.00 | 6.00
-8.00 | Porttil Yoga 520 | 559.00 | 2.00
+8.00 | Portátil Yoga 520 | 559.00 | 2.00
```
- ⏱ Tiempo: 0.4 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
## ✅ Query 40: Correcto
- ⏱ Tiempo: 0.44 ms
- ✅ Se usó índice(s) en la consulta: codigo_fabricante

🚨 **Problemas detectados:**
⚠️ Evitar `SELECT *`. Usar solo las columnas necesarias.

---
