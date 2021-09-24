from UNO_clases_funciones import *
from partida import *


# RECREACIÓN DEL JUEGO DE CARTAS UNO EN PYTHON
# PROGRAMA REALIZADO POR ARNALDO CISNEROS
# NOVIEMBRE 2020


def run():
	os.system("pip install -r requirements.txt")
	if os.name=="nt":
		keyboard.press_and_release('F11')
	while True:
		clear()
		l(5)
		esp((os.get_terminal_size().columns - 29) / 2);print(Fore.RED+"| |  | |"+Fore.GREEN+" | \\ | | "+Fore.YELLOW+" / __ \\ "+Fore.BLUE+" | |")
		esp((os.get_terminal_size().columns - 29) / 2);print(Fore.RED+"| |  | |"+Fore.GREEN+" |  \\| | "+Fore.YELLOW+"| |  | |"+Fore.BLUE+" | |")
		esp((os.get_terminal_size().columns - 29) / 2);print(Fore.RED+"| |  | |"+Fore.GREEN+" | . ` | "+Fore.YELLOW+"| |  | |"+Fore.BLUE+" | |")
		esp((os.get_terminal_size().columns - 29) / 2);print(Fore.RED+"| |__| | "+Fore.GREEN+"| |\\  | "+Fore.YELLOW+"| |__| | "+Fore.BLUE+"|_|")
		esp((os.get_terminal_size().columns - 29) / 2);print(Fore.RED+" \\____/ "+Fore.GREEN+" |_| \\_| "+Fore.YELLOW+" \\____/ "+Fore.BLUE+" (_)")
		l(1)
		esp((os.get_terminal_size().columns - 39) / 2);print("El juego de cartas para toda la familia")
		l(4)
		esp((os.get_terminal_size().columns - 14) / 2);print("MENU PRINCIPAL")
		l(1)
		esp((os.get_terminal_size().columns - 22) / 2);print("1. Iniciar una partida")
		esp((os.get_terminal_size().columns - 22) / 2);print("2. Sobre este programa")
		esp((os.get_terminal_size().columns - 22) / 2);print("3. Salir del juego")
		l(1)
		try:
			esp((os.get_terminal_size().columns - 23) / 2);opcion_menuPrincipal=int(input("Seleccione una opción: "))
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
			esp((os.get_terminal_size().columns - 4) / 2);print("UNO!")
			esp((os.get_terminal_size().columns - 40) / 2);print("Famoso juego de cartas escrito en Python")
			l(2)
			esp((os.get_terminal_size().columns - 62) / 2);print("Este código forma parte de mi librería de Proyectos personales")
			esp((os.get_terminal_size().columns - 60) / 2);print("De igual forma, no tiene ninguna intención de ser monetizado")
			l(2)
			esp((os.get_terminal_size().columns - 31) / 2);print("Realizado en Medellín, Colombia")
			esp((os.get_terminal_size().columns - 14) / 2);print("DICIEMBRE 2020")
			l(1)
			esp((os.get_terminal_size().columns - 30) / 2);print("ARNALDO JOSE CISNEROS ZAMBRANO")
			l(3)
			esp((os.get_terminal_size().columns - 44) / 2);print("Presione ENTER para volver al menú principal")
			standby()
		elif opcion_menuPrincipal==3:
			clear()
			l(3)
			esp((os.get_terminal_size().columns - 18) / 2);print("GRACIAS POR JUGAR!")
			esp((os.get_terminal_size().columns - 25) / 2);print("Presione ENTER para salir")
			standby()
			clear()
			break;


if __name__ == "__main__":
	run()