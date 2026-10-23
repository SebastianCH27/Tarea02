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

### Clases identificadas

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

Determinar el MRO de cada versión y explicar cómo se resuelve
el cálculo del costo.

Pendiente de desarrollo.

## Actividad 3 Cálculo de los cobros

Calcular los importes de las dos versiones y explicar su relación
con los cobros realizados a Luis y Rosa.

Pendiente de desarrollo.

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