from UNO_clases_funciones import *
from partida import *

# RECREACIÓN DEL JUEGO DE CARTAS UNO EN PYTHON
# PROGRAMA REALIZADO POR ARNALDO CISNEROS
# NOVIEMBRE 2020
while True:
	clear()
	l(5)
	print("                                      "+Fore.RED+"| |  | |"+Fore.GREEN+" | \\ | | "+Fore.YELLOW+" / __ \\ "+Fore.BLUE+" | |")
	print("                                      "+Fore.RED+"| |  | |"+Fore.GREEN+" |  \\| | "+Fore.YELLOW+"| |  | |"+Fore.BLUE+" | |")
	print("                                      "+Fore.RED+"| |  | |"+Fore.GREEN+" | . ` | "+Fore.YELLOW+"| |  | |"+Fore.BLUE+" | |")
	print("                                      "+Fore.RED+"| |__| | "+Fore.GREEN+"| |\\  | "+Fore.YELLOW+"| |__| | "+Fore.BLUE+"|_|")
	print("                                      "+Fore.RED+" \\____/ "+Fore.GREEN+" |_| \\_| "+Fore.YELLOW+" \\____/ "+Fore.BLUE+" (_)")
	l(1)
	print("                                 "+"El juego de cartas para toda la familia")
	l(4)
	print("                                              "+"MENU PRINCIPAL")
	l(1)
	print("                                         "+"1. Iniciar una partida")
	print("                                         "+"2. Sobre este programa")
	print("                                         "+"3. Salir del juego")
	l(1)
	try:
		opcion_menuPrincipal=int(input("                                         "+"Seleccione una opción: "))
	except:
		clear();continue;
	if opcion_menuPrincipal<1 or opcion_menuPrincipal>3:
		clear();continue;
	if opcion_menuPrincipal==1:
		partida()
		del opcion_menuPrincipal
	elif opcion_menuPrincipal==2:
		clear()
		l(3)
		print("                                           "+"UNO!")
		print("                           "+"Famoso juego de cartas escrito en Python")
		l(2)
		print("                "+"Este código forma parte de mi librería de Proyectos personales")
		print("                 "+"De igual forma, no tiene ninguna intención de ser monetizado")
		l(2)
		print("                             "+"Realizado en Medellín, Colombia")
		print("                                     "+"DICIEMBRE 2020")
		l(1)
		print("                             "+"ARNALDO JOSE CISNEROS ZAMBRANO")
		l(3)
		print("                       "+"Presione ENTER para volver al menú principal")
		standby()
	elif opcion_menuPrincipal==3:
		clear()
		l(3)
		print("                                        "+"GRACIAS POR JUGAR!")
		print("                                    "+"Presione ENTER para salir")
		standby()
		break;
