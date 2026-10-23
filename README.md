# Caso 02 Sistema de matrícula de la UNSCH

**Estudiante:** Sebastián Adán Cahuín Huamán  
**Lenguaje:** Python  
**Semestre del caso:** 2026-II

## Descripción del caso

La OTI de la UNSCH necesita analizar un problema en el cálculo del
costo de matrícula. Dos programadores combinaron las mismas
especializaciones en diferente orden y obtuvieron cobros distintos.

El derecho base de matrícula es de S/ 60.00. Se consideran estas
situaciones especiales:

- Matrícula extemporánea: recargo de S/ 15.00.
- Índice académico desaprobatorio: recargo de S/ 15.00.
- Beca por afectación de la violencia sociopolítica: reducción del 50 %.


## Actividad 1 Identificación de clases y relaciones

### Clases involucradas

El caso describe una matrícula general, tres especializaciones y
dos versiones de una modalidad combinada. Para representarlas
utilizaremos estas clases:

| Clase | Responsabilidad |
|---|---|
| MatriculaGeneral | Representar la matrícula común y establecer el derecho base de S/ 60.00. |
| MatriculaExtemporanea | Agregar un recargo de S/ 15.00 por matricularse fuera de fecha. |
| MatriculaDesaprobado | Agregar S/ 15.00 por tener un índice académico desaprobatorio en el semestre anterior. |
| MatriculaBeca | Reducir a la mitad el monto calculado por las reglas anteriores. |
| MatriculaVersion1 | Representar la modalidad combinada del primer programador. |
| MatriculaVersion2 | Representar la modalidad combinada del segundo programador. |

Los nombres de las clases son una propuesta para representar el caso.
Las dos clases de versión permiten comparar las soluciones de ambos
programadores dentro de un mismo programa.

### Relaciones entre las clases

**Herencia simple**

MatriculaExtemporanea, MatriculaDesaprobado y MatriculaBeca heredan
directamente de MatriculaGeneral. Cada una representa una
especialización de la matrícula común y modifica su costo.

**Herencia múltiple**

MatriculaVersion1 hereda de MatriculaBeca, MatriculaDesaprobado
y MatriculaExtemporanea, en ese orden.

MatriculaVersion2 hereda de MatriculaDesaprobado,
MatriculaExtemporanea y MatriculaBeca, en ese orden.

**Estructura de herencia en diamante**

Las tres especializaciones tienen como antecesora a
MatriculaGeneral y vuelven a reunirse en cada modalidad combinada.
Por eso existen varios caminos de herencia hacia la misma clase base.

## Actividad 2 Orden de resolución de métodos

El MRO es el orden que sigue Python para buscar los métodos
en una jerarquía de herencia.

En este caso, cada especialización primero obtiene el resultado
de super().calcular_costo() y después aplica su recargo o descuento.

### MRO de cada versión

| Posición | MatriculaVersion1 | MatriculaVersion2 |
|---|---|---|
| 1 | MatriculaVersion1 | MatriculaVersion2 |
| 2 | MatriculaBeca | MatriculaDesaprobado |
| 3 | MatriculaDesaprobado | MatriculaExtemporanea |
| 4 | MatriculaExtemporanea | MatriculaBeca |
| 5 | MatriculaGeneral | MatriculaGeneral |
| 6 | object | object |

Las clases combinadas no tienen un método calcular_costo() propio.
Por eso Python continúa buscando en sus especializaciones,
siguiendo el orden de la tabla.

### Primera versión

Python encuentra calcular_costo() en MatriculaBeca.
Ese método espera el resultado de MatriculaDesaprobado,
que a su vez espera el de MatriculaExtemporanea.
Finalmente, MatriculaGeneral devuelve el derecho base de S/ 60.00.

Cuando las llamadas regresan, se realizan estas operaciones:

1. MatriculaExtemporanea agrega su recargo.
2. MatriculaDesaprobado agrega su recargo.
3. MatriculaBeca aplica el descuento al monto acumulado.

### Segunda versión

Python encuentra calcular_costo() en MatriculaDesaprobado.
Ese método espera el resultado de MatriculaExtemporanea,
que a su vez espera el de MatriculaBeca.
Finalmente, MatriculaGeneral devuelve el derecho base de S/ 60.00.

Cuando las llamadas regresan, se realizan estas operaciones:

1. MatriculaBeca aplica el descuento al derecho base.
2. MatriculaExtemporanea agrega su recargo.
3. MatriculaDesaprobado agrega su recargo.

### Funcionamiento de super()

En herencia múltiple, super() continúa con la siguiente clase
del MRO del objeto. No necesariamente llama directamente
a la clase padre declarada en la especialización.

El orden de búsqueda sigue el MRO, pero los ajustes se aplican
cuando regresan las llamadas, porque cada método necesita
primero el resultado de super().calcular_costo().

La clase object forma parte del MRO, pero no interviene en
el cálculo, porque MatriculaGeneral devuelve el monto base
sin continuar la cadena.

## Actividad 3 Cálculo de los cobros

### Primera versión

Las modificaciones se aplican en este orden:

1. Derecho base: S/ 60.00.
2. Recargo por matrícula extemporánea: 60 + 15 = S/ 75.00.
3. Recargo por índice desaprobatorio: 75 + 15 = S/ 90.00.
4. Beca del 50 %: 90 × 0.5 = S/ 45.00.

El total de la primera versión es S/ 45.00.

### Segunda versión

Las modificaciones se aplican en este orden:

1. Derecho base: S/ 60.00.
2. Beca del 50 %: 60 × 0.5 = S/ 30.00.
3. Recargo por matrícula extemporánea: 30 + 15 = S/ 45.00.
4. Recargo por índice desaprobatorio: 45 + 15 = S/ 60.00.

El total de la segunda versión es S/ 60.00.

### Cobro por estudiante

El documento no especifica qué versión utilizó cada estudiante.
Para presentar los resultados, suponemos que Luis utilizó la
primera versión y Rosa la segunda.

| Estudiante | Versión utilizada | Total |
|---|---|---|
| Luis Huamaní Cárdenas | Primera versión | S/ 45.00 |
| Rosa Ccahuana Prado | Segunda versión | S/ 60.00 |

Bajo esta suposición, Rosa pagó S/ 15.00 más que Luis.
Si se intercambian las versiones utilizadas, también se
intercambian los importes de ambos estudiantes.

## Actividad 4 Explicación de la diferencia

Explicar por qué cambian los importes y por qué ninguna de las
dos versiones presenta un error de sintaxis.

Pendiente de desarrollo.

## Actividad 5 Herencia inconsistente

Analizar qué ocurre al combinar la matrícula general con una
especialización, colocando primero la clase general.

Pendiente de desarrollo.

## Actividad 6 Propuesta de rediseño

Proponer una solución que permita establecer explícitamente
el orden de los ajustes y decidir si la beca se aplica antes
o después de los recargos.

Pendiente de desarrollo.