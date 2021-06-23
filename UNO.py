from UNO_clases_funciones import *
from partida import *


# RECREACIÓN DEL JUEGO DE CARTAS UNO EN PYTHON
# PROGRAMA REALIZADO POR ARNALDO CISNEROS
# NOVIEMBRE 2020


def run():
	while True:
		clear()
		l(5)
		esp(38);print(Fore.RED+"| |  | |"+Fore.GREEN+" | \\ | | "+Fore.YELLOW+" / __ \\ "+Fore.BLUE+" | |")
		esp(38);print(Fore.RED+"| |  | |"+Fore.GREEN+" |  \\| | "+Fore.YELLOW+"| |  | |"+Fore.BLUE+" | |")
		esp(38);print(Fore.RED+"| |  | |"+Fore.GREEN+" | . ` | "+Fore.YELLOW+"| |  | |"+Fore.BLUE+" | |")
		esp(38);print(Fore.RED+"| |__| | "+Fore.GREEN+"| |\\  | "+Fore.YELLOW+"| |__| | "+Fore.BLUE+"|_|")
		esp(38);print(Fore.RED+" \\____/ "+Fore.GREEN+" |_| \\_| "+Fore.YELLOW+" \\____/ "+Fore.BLUE+" (_)")
		l(1)
		esp(33);print("El juego de cartas para toda la familia")
		l(4)
		esp(46);print("MENU PRINCIPAL")
		l(1)
		esp(41);print("1. Iniciar una partida")
		esp(41);print("2. Sobre este programa")
		esp(41);print("3. Salir del juego")
		l(1)
		try:
			esp(41);opcion_menuPrincipal=int(input("Seleccione una opción: "))
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
			esp(43);print("UNO!")
			esp(27);print("Famoso juego de cartas escrito en Python")
			l(2)
			esp(16);print("Este código forma parte de mi librería de Proyectos personales")
			esp(17);print("De igual forma, no tiene ninguna intención de ser monetizado")
			l(2)
			esp(29);print("Realizado en Medellín, Colombia")
			esp(37);print("DICIEMBRE 2020")
			l(1)
			esp(29);print("ARNALDO JOSE CISNEROS ZAMBRANO")
			l(3)
			esp(23);print("Presione ENTER para volver al menú principal")
			standby()
		elif opcion_menuPrincipal==3:
			clear()
			l(3)
			esp(40);print("GRACIAS POR JUGAR!")
			esp(36);print("Presione ENTER para salir")
			standby()
			clear()
			break;


if __name__ == "__main__":
	run()