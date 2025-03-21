-- 1. Llista el nom de tots els productes
SELECT * FROM producto;


-- 2. Llista els noms i els preus de tots els productes
SELECT nombre, precio FROM producto;


-- 3. Llista totes les columnes de la taula producto
SELECT * FROM producto WHERE precio >= 0;


-- 4. Llista el nom dels productes, el preu en euros i el preu en dòlars estatunidencs (USD)
SELECT nombre, precio, precio AS precio_usd FROM producto;


-- 5. Llista el nom dels productes, el preu en euros i el preu en dòlars estatunidencs (USD) amb àlies
SELECT nombre AS 'Nom de producte', precio AS 'Euros', precio AS 'Dòlars' FROM producto;

-- 6. Llista els noms i els preus dels productes amb noms en majúscules
SELECT UPPER(nombre) AS nom, precio FROM producto WHERE precio >= 0;

-- 7. Llista els noms i els preus dels productes amb noms en minúscules
SELECT LOWER(nombre) AS nom, precio FROM producto WHERE precio >= 0;

-- 8. Llista el nom dels fabricants i les dues primeres lletres en majúscules
SELECT nombre, UPPER(LEFT(nombre, 2)) AS inicials FROM fabricante;

-- 9. Llista els noms i els preus dels productes, arrodonint el preu
SELECT nombre, ROUND(precio) AS preu FROM producto;

-- 10. Llista els noms i els preus dels productes, truncant el preu sense decimals
SELECT nombre, TRUNCATE(precio, 0) AS preu FROM producto;

-- 11. Llista el codi dels fabricants que tenen productes a la taula
SELECT DISTINCT codigo_fabricante FROM producto;

-- 12. Llista els noms dels fabricants ordenats de manera ascendent
SELECT nombre FROM fabricante ORDER BY nombre ASC;

-- 13. Llista els noms dels fabricants ordenats de manera descendent
SELECT nombre FROM fabricante ORDER BY nombre DESC;

-- 14. Llista els noms dels productes ordenats pel nom ascendent i pel preu descendent
SELECT nombre, precio FROM producto ORDER BY nombre ASC, precio DESC;

-- 15. Retorna les 5 primeres files de la taula fabricante
SELECT * FROM fabricante LIMIT 5;

-- 16. Retorna 2 files a partir de la quarta fila (inclosiva)
SELECT * FROM fabricante LIMIT 2 OFFSET 3;

-- 17. Llista el nom i el preu del producte més barat
SELECT nombre, precio FROM producto ORDER BY precio ASC LIMIT 1;

-- 18. Llista el nom i el preu del producte més car
SELECT nombre, precio FROM producto ORDER BY precio DESC LIMIT 1;

-- 19. Llista tots els productes del fabricant amb codi 2
SELECT nombre FROM producto WHERE codigo_fabricante = 2;

-- 20. Llista productes amb preu i fabricant
SELECT p.nombre, p.precio, f.nombre AS fabricant
FROM producto p JOIN fabricante f ON p.codigo_fabricante = f.codigo;


-- 21. Llista productes amb fabricant ordenats alfabèticament
SELECT p.nombre, p.precio, f.nombre AS fabricant
FROM producto p JOIN fabricante f ON p.codigo_fabricante = f.codigo
ORDER BY f.nombre ASC;

-- 22. Retorna el codi i nom del producte juntament amb el fabricant
SELECT p.codigo, p.nombre, f.codigo AS 'Codi fabricant', f.nombre AS 'Fabricant'
FROM producto p JOIN fabricante f ON p.codigo_fabricante = f.codigo;

-- 23. Retorna el producte més barat amb fabricant
SELECT p.nombre, p.precio, f.nombre AS fabricant
FROM producto p JOIN fabricante f ON p.codigo_fabricante = f.codigo
ORDER BY p.precio ASC LIMIT 1;

-- 24. Retorna el producte més car amb fabricant
SELECT p.nombre, p.precio, f.nombre AS fabricant
FROM producto p JOIN fabricante f ON p.codigo_fabricante = f.codigo
ORDER BY p.precio DESC LIMIT 1;

-- 25. Retorna productes del fabricant Lenovo
SELECT * FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Lenovo');


-- 26. Retorna productes del fabricant Crucial amb preu > 200€
SELECT * FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Crucial') AND precio > 200;

-- 27. Retorna productes de Asus, Hewlett-Packard i Seagate (Sense IN)
SELECT * FROM producto WHERE codigo_fabricante = 1 OR codigo_fabricante = 3 OR codigo_fabricante = 5;

-- 28. Retorna productes de Asus, Hewlett-Packard i Seagate (Amb IN)
SELECT * FROM producto WHERE codigo_fabricante IN (1, 3, 5);

-- 29. Retorna productes amb fabricants que acaben en 'e'
SELECT p.nombre, p.precio FROM producto p
JOIN fabricante f ON p.codigo_fabricante = f.codigo
WHERE f.nombre LIKE '%e';

-- 30. Retorna productes amb fabricants que contenen la lletra 'w'
SELECT p.nombre, p.precio FROM producto p
JOIN fabricante f ON p.codigo_fabricante = f.codigo
WHERE f.nombre LIKE '%w%';

-- 31. Retorna productes amb preu >= 180€, ordenats pel preu descendent i nom ascendent
SELECT p.nombre, p.precio, f.nombre AS fabricant FROM producto p
JOIN fabricante f ON p.codigo_fabricante = f.codigo
WHERE p.precio >= 180 ORDER BY p.precio DESC, p.nombre ASC;

-- 32. Retorna fabricants que tenen productes associats
SELECT DISTINCT f.codigo, f.nombre FROM fabricante f JOIN producto p ON f.codigo = p.codigo_fabricante;

-- 33. Retorna tots els fabricants i els seus productes (incloent els que no tenen productes)
SELECT f.nombre AS fabricant, p.nombre AS producte FROM fabricante f
LEFT JOIN producto p ON f.codigo = p.codigo_fabricante;

-- 34. Retorna només fabricants sense productes associats
SELECT f.nombre FROM fabricante f LEFT JOIN producto p ON f.codigo = p.codigo_fabricante WHERE p.codigo IS NULL;

-- 35. Retorna tots els productes de Lenovo (Sense JOIN)
SELECT * FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Lenovo');

-- 36. Retorna productes amb el mateix preu que el més car de Lenovo (Sense JOIN)
SELECT * FROM producto WHERE precio = (SELECT MAX(precio) FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Lenovo'));

-- 37. Llista el producte més car de Lenovo
SELECT nombre FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Lenovo') ORDER BY precio DESC LIMIT 1;

-- 38. Llista el producte més barat de Hewlett-Packard
SELECT nombre FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Hewlett-Packard') ORDER BY precio ASC LIMIT 1;

-- 39. Retorna productes amb preu >= al més car de Lenovo
SELECT * FROM producto WHERE precio >= (SELECT MAX(precio) FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Lenovo'));

-- 40. Productes d'Asus amb preu superior al preu mitjà dels seus productes
SELECT * FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Asus') AND precio > (SELECT AVG(precio) FROM producto WHERE codigo_fabricante = (SELECT codigo FROM fabricante WHERE nombre = 'Asus'));
