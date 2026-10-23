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

### Por qué se obtienen cobros distintos

La diferencia aparece porque la beca se aplica en momentos distintos.

En la primera versión, primero se agregan los dos recargos.
Después, la beca reduce a la mitad todo el monto acumulado:

(60 + 15 + 15) × 0.5 = S/ 45.00.

En la segunda versión, la beca reduce solamente el derecho base.
Los dos recargos se agregan después y conservan su valor completo:

(60 × 0.5) + 15 + 15 = S/ 60.00.

Por eso se obtiene una diferencia de S/ 15.00. Los recargos son
los mismos; lo que cambia es el monto sobre el que actúa la beca.

### Por qué no existe un error de sintaxis

Las dos declaraciones de herencia múltiple son válidas.
Python puede construir un MRO consistente para cada versión
y resolver sus llamadas a super().

Cambiar el orden de las clases base es válido en estas dos
versiones, pero también cambia el orden en que se aplican
las modificaciones al monto.

El problema está en el diseño del cálculo: la aplicación
de la beca depende del orden de las clases base, en lugar
de estar definida mediante una política de cobro explícita.

## Actividad 5 Herencia inconsistente

Si se combina la matrícula general con una de sus especializaciones,
colocando primero la general, se tendría esta declaración:

```python
class MatriculaIncorrecta(MatriculaGeneral, MatriculaBeca):
    pass
```

Python genera un TypeError al intentar crear esta clase,
porque no puede construir un MRO consistente.

### Causa del problema

La declaración establece dos exigencias incompatibles:

1. Por el orden de las clases base, MatriculaGeneral debería
   aparecer antes que MatriculaBeca.

2. Como MatriculaBeca hereda de MatriculaGeneral, la especialización
   debe aparecer antes que su clase padre dentro del MRO.

Python no puede cumplir ambas condiciones al mismo tiempo.
Por eso rechaza la creación de MatriculaIncorrecta.

### Tipo de error

La declaración tiene una sintaxis válida, pero su jerarquía
de herencia es inconsistente. Por eso se produce un TypeError,
no un SyntaxError.

El error aparece al crear la clase, antes de poder construir
un objeto o calcular el costo de una matrícula.

MatriculaBeca ya hereda de MatriculaGeneral, por lo que una
nueva clase que herede de MatriculaBeca también tendrá a
MatriculaGeneral como antecesora.

## Actividad 6 Propuesta de rediseño

Se propone que cada matrícula tenga una lista ordenada de ajustes.
Cada ajuste recibe el monto actual y devuelve el monto modificado.

El orden de aplicación se establece al agregar los ajustes a la lista.
Así, la política de cobro queda definida explícitamente para cada
matrícula.

### Clases del rediseño

| Clase | Responsabilidad |
|---|---|
| Matricula | Guardar los datos del estudiante, el derecho base y la lista ordenada de ajustes. Calcular el total. |
| Ajuste | Definir el comportamiento común aplicar(monto). |
| RecargoExtemporaneo | Agregar S/ 15.00 por matrícula fuera de fecha. |
| RecargoDesaprobado | Agregar S/ 15.00 por índice académico desaprobatorio. |
| Beca | Reducir a la mitad el monto recibido. |

Las clases de recargo y beca heredan de Ajuste.
Matricula utiliza estos objetos para realizar el cálculo.

Las dos versiones combinadas del diseño original se conservan
para analizar el problema. En el rediseño, las condiciones se
combinan mediante la lista de ajustes.

### Funcionamiento

1. El cálculo empieza con el derecho base de S/ 60.00.
2. Se seleccionan los ajustes que corresponden al estudiante.
3. Se agregan en el orden establecido por la política de cobro.
4. La matrícula recorre la lista y aplica cada ajuste al monto acumulado.
5. Se devuelve el total.

### Orden de aplicación

| Política | Orden de los ajustes | Total |
|---|---|---|
| Beca después de los recargos | Extemporáneo, desaprobado y beca. | S/ 45.00 |
| Beca antes de los recargos | Beca, extemporáneo y desaprobado. | S/ 60.00 |

La OTI debe establecer qué política corresponde.
Para estudiantes con las mismas condiciones y la misma política,
se utilizarán los mismos ajustes en el mismo orden.

Por ejemplo, si la beca debe reducir todo el monto, Luis y Rosa
tendrán ambos recargos primero y la beca al final. Los dos
pagarán S/ 45.00.

### Aplicación de los cuatro pilares de POO

| Pilar | Aplicación |
|---|---|
| Abstracción | Ajuste define el comportamiento común aplicar(monto). |
| Encapsulamiento | Matricula guarda sus datos y la lista de ajustes en atributos privados. |
| Herencia | Los recargos y Beca heredan de Ajuste. |
| Polimorfismo | Matricula llama a aplicar(monto) y cada ajuste ejecuta su propia operación. |