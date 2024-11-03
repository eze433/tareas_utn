# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def mostrar(self):
#         print(f'Su nombre es {self.nombre} y tiene {self.edad} años')
        
# persona1 = Persona('Ezequiel Do Campo', 20)

# persona1.mostrar()

# class Libro:
#     def __init__(self, titulo, autor, año_publi):
#         self.titulo = titulo
#         self.autor = autor
#         self.año_publi = año_publi

#     def mostrar(self):
#         print(f'El titulo del libro es {self.titulo}, de {self.autor}, publicado en el año {self.año_publi}')

# libro_1 = Libro('El corazon delator', 'Edgar Allan Poe', 1974)

# libro_1.mostrar()

# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura

#     def area_calc(self):
#         area = self.base * self.altura
#         return area

# rect_1 = Rectangulo(10, 20) 

# print(rect_1.area_calc())

# class Calculadora:
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2

#     def suma(self):
#         return self.n1 + self.n2

#     def resta(self):
#         return self.n1 - self.n2

#     def multiplicacion(self):
#         return self.n1 * self.n2

#     def division(self):
#         return self.n1 / self.n2

#     def potencia(self):
#         return self.n1 ** self.n2

# calc_1 = Calculadora(10, 5)

# print(calc_1.suma())
# print(calc_1.resta())
# print(calc_1.multiplicacion())
# print(calc_1.division())
# print(calc_1.potencia())


# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def dar_nombre(self):
#         print(self.nombre)

# class Perro(Animal):
#     def __init__(self, nombre):
#         super().__init__(nombre)

#     def sonido(self):
#         print('Guau')

#     def dar_nombre(self):
#         super().dar_nombre()

# class Gato(Animal):
#     def __init__(self, nombre):
#         super().__init__(nombre)

#     def sonido(self):
#         print('Miau')

#     def dar_nombre(self):
#         super().dar_nombre()

# gato_1 = Gato('Pepo')
# gato_1.dar_nombre()
# gato_1.sonido()

# perro_1 = Perro('Firulais')
# perro_1.dar_nombre()
# perro_1.sonido()

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):
        print(f'${self.__saldo}')

    def depositar(self, deposito):
        while deposito < 0:
            print('Ingrese un número mayor a 0')
            deposito = int(input('Ingrese una cantidad a depositar: '))
        
        self.__saldo += deposito
        print(f'Se han depositado ${deposito}')

    def retirar(self, retiro):
        while retiro > self.__saldo or retiro < 0:
            if retiro > self.__saldo:
                print('Saldo insuficiente')
            elif retiro < 0:
                print('Ingrese una cantidad mayor a 0')

            retiro = int(input('Ingrese una cantidad a retirar: '))

        self.__saldo -= retiro
        print(f'Se han retirado ${retiro}')

caja_1 = CuentaBancaria('Ezequiel', 100)
caja_1.obtener_saldo()

caja_1.depositar(int(input('Ingrese una cantidad a depositar: ')))
caja_1.obtener_saldo()

caja_1.retirar(int(input('Ingrese una cantidad a retirar: ')))
caja_1.obtener_saldo()

