from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    def __init__(self, nombre, ambulancias, tiempo_de_asistencia):
        self.nombre = nombre
        self.ambulancias = ambulancias
        self.tiempo_de_asistencia = tiempo_de_asistencia


    def get_nombre(self):
        return self.nombre


    def get_cantidad_de_ambulancias(self):
        return self.ambulancias


    def get_tiempo_de_asistencia(self):
        return self.tiempo_de_asistencia


class BaseCompuesta(Base):
    def __init__(self, nombre):
        self.nombre = nombre
        self.ambulancias = 0
        self.tiempo_de_asistencia = 0
        self.bases = []

    def añadir_base(self, bases):
        if type(bases) == list:
            for bas in bases:
                self.bases.append(bas)
                self.ambulancias += bas.get_cantidad_de_ambulancias()
                self.tiempo_de_asistencia += bas.get_tiempo_de_asistencia()


        else:
            self.bases.append(bases)
            self.ambulancias += bases.get_cantidad_de_ambulancias()
            self.tiempo_de_asistencia += bases.get_tiempo_de_asistencia()




    def get_cantidad_de_ambulancias(self):
        return self.ambulancias

    def get_tiempo_de_asistencia(self):
        return self.tiempo_de_asistencia

    def get_tiempo_de_asistencia_medio(self):
        return self.get_tiempo_de_asistencia() / self.get_numero_de_bases(self.bases)

    def get_bases(self):
        return self.bases

    def get_numero_de_bases(self, lista_de_bases):
        numero_de_bases = 0
        for base in lista_de_bases:
            if isinstance(base, BaseCompuesta):
                numero_de_bases += self.get_numero_de_bases(base.get_bases())

            else:
                numero_de_bases += 1

        return numero_de_bases


if __name__ == '__main__':
    Medicina_del_Campo = Base('Medicina del campo', 10, 15)
    Hospital_universitario = Base('Hospital universitario', 6, 7)

    Valladolid = BaseCompuesta('Valladolid')
    Valladolid.añadir_base([Medicina_del_Campo, Hospital_universitario])

    Hospital_de_Zamora = Base('Hospital de Zamora', 3, 5)

    Zamora = BaseCompuesta('Zamora')
    Zamora.añadir_base(Hospital_de_Zamora)

    Castilla_y_Leon = BaseCompuesta('Castilla y Leon')
    Castilla_y_Leon.añadir_base([Valladolid, Zamora])

    print(Valladolid.get_cantidad_de_ambulancias())
    print(Castilla_y_Leon.get_tiempo_de_asistencia_medio())





