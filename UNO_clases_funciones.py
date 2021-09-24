# Librerías
import os
import random #DOCU: https://www.youtube.com/watch?v=PoUcplbntYo&ab_channel=LeonardoKuffo
try:
	import keyboard
	from colorama import *
except:
	if os.name=="nt":
		os.system("cls");
	else:
		os.system("clear");
	print('')
	print('')
	print('    	 / / / / | / / __ \/ /')
	print('     / / / /  |/ / / / / /') 
	print('    / /_/ / /|  / /_/ /_/')  
	print('    \____/_/ |_/\____(_)')
	print('')
	print('    INSTALANDO DEPENDENCIAS:')
	print('        keyboard v0.13.5')
	print('        colorama v0.4.3')
	print('')
	print('    Por favor espere, el juego se iniciará pronto...') 
	os.system("pip install -r requirements.txt")
	import keyboard
	from colorama import *
init(autoreset=True) # VER https://pypi.org/project/colorama/


# Métodos Estéticos y de Espera de respuesta


def clear(): 
	if os.name=="nt":
		os.system("cls");
	else:
		os.system("clear");


def l(n): 
	for i in range(n): print("");


def standby(): a=input()


def esp(n):
	if n <= 0:
		n = 0
	if type(n) == float:
		n = round(n)
	for i in range(n):
		print(" ", end="")


def linea(n):
	for i in range(n): print("-", end="");
	print("")


# CLASES


class carta():
	def __init__(self, color):
		self.color=color

	def devolver_color(self):
		return self.color

	def imprimir_color(self):
		print(self.color)

	def informacion_general(self):
		print("Esta carta tiene el color "+self.color)


class carta_verde(carta):
	def __init__(self, color):
		super().__init__(color)

	def informacion_general(self):
		super().informacion_general()
		print(Fore.GREEN+"SE IMPRIME EN ESTE COLOR")

	def devolver_color(self):
		return "VERDE"


class carta_azul(carta):
	def __init__(self, color):
		super().__init__(color)

	def informacion_general(self):
		super().informacion_general()
		print(Fore.BLUE+"SE IMPRIME EN ESTE COLOR")

	def devolver_color(self):
		return "AZUL"


class carta_roja(carta):
	def __init__(self, color):
		super().__init__(color)

	def informacion_general(self):
		super().informacion_general()
		print(Fore.RED+"SE IMPRIME EN ESTE COLOR")

	def devolver_color(self):
		return "ROJO"


class carta_amarilla(carta):
	def __init__(self, color):
		super().__init__(color)

	def informacion_general(self):
		super().informacion_general()
		print(Fore.YELLOW+"SE IMPRIME EN ESTE COLOR")

	def devolver_color(self):
		return "AMARILLO"


class carta_negra(carta):
	def __init__(self, color):
		super().__init__(color)

	def informacion_general(self):
		super().informacion_general()
		print("SE IMPRIME EN ESTE COLOR")

	def asignar_color(self, color_asignado):
		self.color=color_asignado

	def devolver_color(self):
		return self.color


class numero_verde(carta_verde):
	def __init__(self, numero):
		super().__init__("VERDE")
		self.numero=numero

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Numero "+str(self.numero))

	def mostrar_cara(self):
		print(Fore.GREEN+str(self.numero))

	def devolver_numero(self):
		return self.numero


class numero_azul(carta_azul):
	def __init__(self, numero):
		super().__init__("AZUL")
		self.numero=numero

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Numero "+str(self.numero))

	def mostrar_cara(self):
		print(Fore.BLUE+str(self.numero))

	def devolver_numero(self):
		return self.numero


class numero_rojo(carta_roja):
	def __init__(self, numero):
		super().__init__("ROJO")
		self.numero=numero

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Numero "+str(self.numero))

	def mostrar_cara(self):
		print(Fore.RED+str(self.numero))

	def devolver_numero(self):
		return self.numero


class numero_amarillo(carta_amarilla):
	def __init__(self, numero):
		super().__init__("AMARILLO")
		self.numero=numero

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Numero "+str(self.numero))

	def mostrar_cara(self):
		print(Fore.YELLOW+str(self.numero))

	def devolver_numero(self):
		return self.numero


class masDos_verde(carta_verde):
	def __init__(self):
		super().__init__("VERDE")
		self.tipo="MAS DOS"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de TOMA DOS")

	def mostrar_cara(self):
		print(Fore.GREEN+"TOMA DOS")

	def devolver_tipo(self):
		return self.tipo


class masDos_azul(carta_azul):
	def __init__(self):
		super().__init__("AZUL")
		self.tipo="MAS DOS"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de TOMA DOS")

	def mostrar_cara(self):
		print(Fore.BLUE+"TOMA DOS")

	def devolver_tipo(self):
		return self.tipo


class masDos_amarillo(carta_amarilla):
	def __init__(self):
		super().__init__("AMARILLO")
		self.tipo="MAS DOS"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de TOMA DOS")

	def mostrar_cara(self):
		print(Fore.YELLOW+"TOMA DOS")

	def devolver_tipo(self):
		return self.tipo


class masDos_rojo(carta_roja):
	def __init__(self):
		super().__init__("ROJO")
		self.tipo="MAS DOS"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de TOMA DOS")

	def mostrar_cara(self):
		print(Fore.RED+"TOMA DOS")

	def devolver_tipo(self):
		return self.tipo


class bloqueo_verde(carta_verde):
	def __init__(self):
		super().__init__("VERDE")
		self.tipo="BLOQUEO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de PIERDE TURNO")

	def mostrar_cara(self):
		print(Fore.GREEN+"PIERDE TURNO")

	def devolver_tipo(self):
		return self.tipo


class bloqueo_azul(carta_azul):
	def __init__(self):
		super().__init__("AZUL")
		self.tipo="BLOQUEO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de PIERDE TURNO")

	def mostrar_cara(self):
		print(Fore.BLUE+"PIERDE TURNO")

	def devolver_tipo(self):
		return self.tipo


class bloqueo_amarillo(carta_amarilla):
	def __init__(self):
		super().__init__("AMARILLO")
		self.tipo="BLOQUEO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de PIERDE TURNO")

	def mostrar_cara(self):
		print(Fore.YELLOW+"PIERDE TURNO")

	def devolver_tipo(self):
		return self.tipo


class bloqueo_rojo(carta_roja):
	def __init__(self):
		super().__init__("ROJO")
		self.tipo="BLOQUEO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de PIERDE TURNO")

	def mostrar_cara(self):
		print(Fore.RED+"PIERDE TURNO")

	def devolver_tipo(self):
		return self.tipo


class reverso_verde(carta_verde):
	def __init__(self):
		super().__init__("VERDE")
		self.tipo="REVERSO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de INVERTIR SENTIDO")

	def mostrar_cara(self):
		print(Fore.GREEN+"CAMBIAR SENTIDO")

	def devolver_tipo(self):
		return self.tipo


class reverso_azul(carta_azul):
	def __init__(self):
		super().__init__("AZUL")
		self.tipo="REVERSO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de INVERTIR SENTIDO")

	def mostrar_cara(self):
		print(Fore.BLUE+"CAMBIAR SENTIDO")

	def devolver_tipo(self):
		return self.tipo


class reverso_amarillo(carta_amarilla):
	def __init__(self):
		super().__init__("AMARILLO")
		self.tipo="REVERSO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de INVERTIR SENTIDO")

	def mostrar_cara(self):
		print(Fore.YELLOW+"CAMBIAR SENTIDO")

	def devolver_tipo(self):
		return self.tipo


class reverso_rojo(carta_roja):
	def __init__(self):
		super().__init__("ROJO")
		self.tipo="REVERSO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de INVERTIR SENTIDO")

	def mostrar_cara(self):
		print(Fore.RED+"CAMBIAR SENTIDO")

	def devolver_tipo(self):
		return self.tipo


class masCuatro(carta_negra):
	def __init__(self):
		super().__init__("NEGRO")
		self.tipo="MAS CUATRO"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de TOMA CUATRO Y CAMBIA COLOR")

	def mostrar_cara(self):
		if self.color=="NEGRO":
			print("TOMA CUATRO")
		elif self.color=="VERDE":
			print(Fore.GREEN+"TOMA CUATRO")
		elif self.color=="AZUL":
			print(Fore.BLUE+"TOMA CUATRO")
		elif self.color=="AMARILLO":
			print(Fore.YELLOW+"TOMA CUATRO")
		elif self.color=="ROJO":
			print(Fore.RED+"TOMA CUATRO")

	def mostrar_cara_sin_color(self):
		print("TOMA CUATRO")


	def devolver_tipo(self):
		return self.tipo


class cambia_color(carta_negra):
	def __init__(self):
		super().__init__("NEGRO")
		self.tipo="CAMBIA COLOR"

	def informacion_general(self):
		super().informacion_general()
		print("Su valor es: Carta de CAMBIA COLOR")

	def mostrar_cara(self):
		if self.color=="NEGRO":
			print("CAMBIA COLOR")
		elif self.color=="VERDE":
			print(Fore.GREEN+"CAMBIA COLOR")
		elif self.color=="AZUL":
			print(Fore.BLUE+"CAMBIA COLOR")
		elif self.color=="AMARILLO":
			print(Fore.YELLOW+"CAMBIA COLOR")
		elif self.color=="ROJO":
			print(Fore.RED+"CAMBIA COLOR")

	def mostrar_cara_sin_color(self):
		print("CAMBIA COLOR")

	def devolver_tipo(self):
		return self.tipo


# METODOS DE CREACION Y MANIPULACION DE BARAJAS Y MAZOS


def crear_mazo(mazo_creado):
	cartas_especiales=["+2","reverso","bloqueo"]
	cartas_negras=["+4","color"]
	numero=0
	for i in range(2):
		while numero<=9:
			carta_creada=numero_verde(numero)
			mazo_creado.append(carta_creada)
			del carta_creada
			carta_creada=numero_azul(numero)
			mazo_creado.append(carta_creada)
			del carta_creada
			carta_creada=numero_rojo(numero)
			mazo_creado.append(carta_creada)
			del carta_creada
			carta_creada=numero_amarillo(numero)
			mazo_creado.append(carta_creada)
			del carta_creada
			numero+=1
		numero=1
	for i in cartas_negras:
		if i=="+4":
			carta_creada=masCuatro()
			for i in range(4):
				mazo_creado.append(carta_creada)
			del carta_creada
		if i=="color":
			carta_creada=cambia_color()
			for i in range(4):
				mazo_creado.append(carta_creada)
			del carta_creada
	for i in cartas_especiales:
		if i=="+2":
			carta_creada=masDos_rojo()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=masDos_verde()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=masDos_azul()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=masDos_amarillo()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
		if i=="reverso":
			carta_creada=reverso_rojo()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=reverso_verde()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=reverso_azul()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=reverso_amarillo()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
		if i=="bloqueo":
			carta_creada=bloqueo_rojo()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=bloqueo_verde()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=bloqueo_azul()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
			carta_creada=bloqueo_amarillo()
			mazo_creado.extend([carta_creada,carta_creada])
			del carta_creada
	return mazo_creado


def crearBaraja(mazo_origen, numero_de_cartas):
	baraja=[]
	for i in range(numero_de_cartas):
		posicion=random.randint(1,len(mazo_origen))-1
		carta_elegida=mazo_origen[posicion]
		baraja.append(carta_elegida)
		mazo_origen.remove(mazo_origen[posicion])
	return mazo_origen, baraja


def barajearMazo(mazoParametro):
	auxiliar=[]
	for i in range(len(mazoParametro)):
		posicion=random.randint(1,len(mazoParametro))-1
		carta_elegida=mazoParametro[posicion]
		auxiliar.append(carta_elegida)
		mazoParametro.remove(mazoParametro[posicion])
	mazoParametro=auxiliar
	return mazoParametro


def mostrarBaraja(baraja,sangria):
	l(1)
	esp(sangria);print("Elige una carta para jugar: ")
	for i in range(len(baraja)):
		esp(sangria);print(str(i+1)+". ", end="")
		if isinstance(baraja[i],cambia_color) or isinstance(baraja[i],masCuatro):
			baraja[i].mostrar_cara_sin_color()
		else:
			baraja[i].mostrar_cara()


def comprobar_validez(carta_elegida,carta_descarte):
	try:
		valido=False
		if carta_elegida.devolver_color()==carta_descarte.devolver_color():
			valido=True
		if (isinstance(carta_elegida, numero_verde) or isinstance(carta_elegida, numero_azul) or isinstance(carta_elegida, numero_rojo) or isinstance(carta_elegida, numero_amarillo)) and (isinstance(carta_descarte, numero_verde) or isinstance(carta_descarte, numero_azul) or isinstance(carta_descarte, numero_rojo) or isinstance(carta_descarte, numero_amarillo)):
			if carta_elegida.devolver_numero()==carta_descarte.devolver_numero():
				valido=True
		if isinstance(carta_elegida, masCuatro) or isinstance(carta_elegida, cambia_color):
			valido=True
		if (isinstance(carta_elegida,masDos_azul) or isinstance(carta_elegida,masDos_amarillo) or isinstance(carta_elegida,masDos_rojo) or isinstance(carta_elegida,masDos_verde) or isinstance(carta_elegida,reverso_amarillo) or isinstance(carta_elegida,reverso_azul) or isinstance(carta_elegida,reverso_rojo) or isinstance(carta_elegida,reverso_verde) or isinstance(carta_elegida,bloqueo_amarillo) or isinstance(carta_elegida,bloqueo_azul) or isinstance(carta_elegida,bloqueo_rojo) or isinstance(carta_elegida,bloqueo_verde)) and (isinstance(carta_descarte,masDos_azul) or isinstance(carta_descarte,masDos_amarillo) or isinstance(carta_descarte,masDos_rojo) or isinstance(carta_descarte,masDos_verde) or isinstance(carta_descarte,reverso_amarillo) or isinstance(carta_descarte,reverso_azul) or isinstance(carta_descarte,reverso_rojo) or isinstance(carta_descarte,reverso_verde) or isinstance(carta_descarte,bloqueo_amarillo) or isinstance(carta_descarte,bloqueo_azul) or isinstance(carta_descarte,bloqueo_rojo) or isinstance(carta_descarte,bloqueo_verde)):
			if carta_elegida.devolver_tipo()==carta_descarte.devolver_tipo():
				valido=True

		return valido
	except:
		print("Hubo un error dentro de la funcion comprobar_validez()")
		standby()


def ponerCarta(baraja_origen,mazo_destino,posicion):
	mazo_destino.append(baraja_origen[posicion])
	baraja_origen.remove(baraja_origen[posicion])
	return baraja_origen, mazo_destino

