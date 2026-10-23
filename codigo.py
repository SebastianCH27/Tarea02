class MatriculaGeneral:
    def __init__(self, estudiante):
        self.__estudiante = estudiante
        self.__costo_base = 60.0

    def obtener_estudiante(self):
        return self.__estudiante

    def calcular_costo(self):
        return self.__costo_base


class MatriculaExtemporanea(MatriculaGeneral):
    def __init__(self, estudiante):
        super().__init__(estudiante)
        self.__recargo = 15.0

    def calcular_costo(self):
        return super().calcular_costo() + self.__recargo


class MatriculaDesaprobado(MatriculaGeneral):
    def __init__(self, estudiante):
        super().__init__(estudiante)
        self.__recargo = 15.0

    def calcular_costo(self):
        return super().calcular_costo() + self.__recargo


class MatriculaBeca(MatriculaGeneral):
    def __init__(self, estudiante):
        super().__init__(estudiante)
        self.__descuento = 0.5

    def calcular_costo(self):
        return super().calcular_costo() * (1 - self.__descuento)


class MatriculaVersion1(
    MatriculaBeca, MatriculaDesaprobado, MatriculaExtemporanea
):
    pass


class MatriculaVersion2(
    MatriculaDesaprobado, MatriculaExtemporanea, MatriculaBeca
):
    pass


if __name__ == "__main__":
    # Para el ejemplo, Luis usa la versión 1 y Rosa la versión 2.
    luis = MatriculaVersion1("Luis Huamaní Cárdenas")
    rosa = MatriculaVersion2("Rosa Ccahuana Prado")

    for matricula in [luis, rosa]:
        print("\nEstudiante:", matricula.obtener_estudiante())
        print("Orden de resolución de métodos:")

        for clase in type(matricula).mro():
            print(clase.__name__)

        print(f"Total a pagar: S/ {matricula.calcular_costo():.2f}")

    print("\nIntento de herencia inconsistente:")

    try:
        class MatriculaIncorrecta(MatriculaGeneral, MatriculaBeca):
            pass
    except TypeError as error:
        print("TypeError:", error)