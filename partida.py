from UNO_clases_funciones import *


# ***** PANTALLA DE CONFIGURACIÓN INICIAL *****


def partida():
	clear()
	while True:
		# BOOLEANOS QUE INDICAN NUMERO DE JUGADORES, Y NUMERO DE HUMANOS
		juegan_tres=False
		juegan_cuatro=False
		un_humano=False
		dos_humanos=False
		tres_humanos=False
		cuatro_humanos=False
		l(3);esp(4);print("CONFIGURACIÓN INICIAL DE LA PARTIDA")
		try:
			l(2);esp(4);numero_de_jugadores=int(input("Ingrese el número de jugadores [MÍNIMO 2 - MÁXIMO 4]: "))
		except:
			clear();continue;
		if numero_de_jugadores<2 or numero_de_jugadores>4:
			l(1);esp(4);print("Tienen que ser 2, 3 o 4 jugadores")
			standby();clear();
			continue;
		if numero_de_jugadores>=3:
			juegan_tres=True
			if numero_de_jugadores==4:
				juegan_cuatro=True
		try:
			l(1);esp(4);numero_de_personas=int(input("De los "+str(numero_de_jugadores)+" jugadores, ¿Cuántos son humanos?: "))
		except:
			clear();continue;
		if numero_de_personas<0 or numero_de_personas>numero_de_jugadores:
			l(1);esp(4);print("Número de jugadores humanos incorrecto")
			standby();clear();
			continue;
		if numero_de_personas>=1:
			un_humano=True
			if numero_de_personas>=2:
				dos_humanos=True
				if numero_de_personas>=3:
					tres_humanos=True
					if numero_de_personas==4:
						cuatro_humanos=True
		if un_humano:
			l(1);esp(10);nombre_jugador_1=input("Nombre del jugador 1: ")
		if dos_humanos:
			l(1);esp(10);nombre_jugador_2=input("Nombre del jugador 2: ")
		if tres_humanos:
			l(1);esp(10);nombre_jugador_3=input("Nombre del jugador 3: ")
		if cuatro_humanos:	
			l(1);esp(10);nombre_jugador_4=input("Nombre del jugador 4: ")
		try:
			l(1);esp(4);numero_de_cartas_iniciales=int(input("Ingrese número de cartas para cada jugador [MÍNIMO 7 - MÁXIMO 20]: "))
		except:
			clear();continue;
		if numero_de_cartas_iniciales<7 or numero_de_cartas_iniciales>20:
			l(1);esp(4);print("Tienes que elegir entre 7 y 20 cartas por jugador")
			standby();clear();
			continue;
		clear()
		l(3);esp(4);print("CONFIGURACIÓN INICIAL DE LA PARTIDA")
		l(2);esp(4);print("Hay "+str(numero_de_jugadores)+" jugadores")
		esp(4);print(str(numero_de_personas)+" humanos y "+str(numero_de_jugadores-numero_de_personas)+" computadoras")
		if un_humano:
			esp(4);print("Jugador 1: "+Fore.RED+nombre_jugador_1)
		else:
			esp(4);print("Jugador 1: CPU")
		if dos_humanos:
			esp(4);print("Jugador 2: "+Fore.BLUE+nombre_jugador_2)
		else:
			esp(4);print("Jugador 2: CPU")
		if tres_humanos:
			esp(4);print("Jugador 3: "+Fore.YELLOW+nombre_jugador_3)
		else:
			if juegan_tres:
				esp(4);print("Jugador 3: CPU")
		if cuatro_humanos:
			esp(4);print("Jugador 4: "+Fore.GREEN+nombre_jugador_4)
		else:
			if juegan_cuatro:
				esp(4);print("Jugador 4: CPU")
		esp(4);print("Cada jugador tendrá "+str(numero_de_cartas_iniciales)+" cartas")
		l(1);esp(4);r=input("¿Está bien esta configuración? si/no: ")
		if r=="si":
			clear()
			break;
		else:
			clear()

	
	# *** LAS SIGUIENTES INSTRUCCIONES TIENEN POR OBJETIVO CREAR LAS LISTAS QUE SE VAN A UTILIZAR DURANTE LA EJECUCIÓN DEL PROGRAMA
	mazo=[]
	pila_descarte=[]
	baraja1=[]
	baraja2=[]
	if juegan_tres:
		baraja3=[]
	if juegan_cuatro:
		baraja4=[]
	lista_de_jugadores=[]
	lista_de_nombres=[]
	historial_de_jugadores=["----- Mazo"]
	orientacion = "↓  "

	
	# *** LAS SIGUIENTES INSTRUCCIONES TIENEN POR OBJETIVO CREAR EL MAZO DE CARTAS, Y BARAJEARLO
	mazo=crear_mazo(mazo)
	mazo=barajearMazo(mazo)

	
	# *** LAS SIGUIENTES INSTRUCCIONES TIENEN POR OBJETIVO REPARTIR LAS CARTAS DEL MAZO EN CADA UNA DE LAS BARAJAS EN NÚMEROS IGUALES
	mazo, baraja1=crearBaraja(mazo ,numero_de_cartas_iniciales)
	mazo, baraja2=crearBaraja(mazo ,numero_de_cartas_iniciales)
	if juegan_tres:
		mazo, baraja3=crearBaraja(mazo ,numero_de_cartas_iniciales)
	if juegan_cuatro:
		mazo, baraja4=crearBaraja(mazo ,numero_de_cartas_iniciales)

	
	# *** LAS SIGUIENTES INSTRUCCIONES TIENEN POR OBJETIVO PONER DEL MAZO LA PRIMERA CARTA EN LA PILA DE DESCARTE, ASEGURANDOSE QUE ESA CARTA SEA UN NUMERO, Y NO UNA CARTA ESPECIAL
	while True:
		if isinstance(mazo[0], numero_verde) or isinstance(mazo[0], numero_azul) or isinstance(mazo[0], numero_rojo) or isinstance(mazo[0], numero_amarillo):
			mazo, pila_descarte=ponerCarta(mazo,pila_descarte,0)
			break;
		else:
			mazo=barajearMazo(mazo)

	
	# *** LAS SIGUIENTES INSTRUCCIONES TIENEN POR OBJETIVO AÑADIR LAS BARAJAS CREADAS A LA LISTA DE JUGADORES, PARA ORIENTAR EL FLUJO DEL JUEGO
	lista_de_jugadores.append(baraja1)
	lista_de_jugadores.append(baraja2)
	if juegan_tres:
		lista_de_jugadores.append(baraja3)
	if juegan_cuatro:
		lista_de_jugadores.append(baraja4)

	
	# *** LAS SIGUIENTES INSTRUCCIONES TIENEN POR OBJETIVO AGREGAR LOS NOMBRES DE LOS JUGADORES A UNA LISTA PARA PODER SER UTILZADOS DURANTE EL PROGRAMA
	if un_humano:
		lista_de_nombres.append(nombre_jugador_1)
	if dos_humanos:
		lista_de_nombres.append(nombre_jugador_2)
	if tres_humanos:	
		lista_de_nombres.append(nombre_jugador_3)
	if cuatro_humanos:	
		lista_de_nombres.append(nombre_jugador_4)

	
	# *** LAS SIGUIENTES VARIABLES TIENEN EL OBJETIVO DE CONTROLAR EL FLUJO DEL JUEGO Y TAMBIÉN CREAR LOS EFECTOS DE LAS CARTAS ESPECIALES
	control_de_flujo=1
	jugador_actual=0
	pierde_turno=False
	toma_dos=False
	toma_cuatro=False
	error=False
	carta_reverso=False
	salir=False
	ultima_opcion=False
	palabra_turno=""
	tomo_del_mazo=False
	cascada_toma_dos=0
	cascada_toma_cuatro=0
	obligar_toma_dos=False
	obligar_toma_cuatro=False
	if un_humano:
		jugador_actual_es_humano=True
	else:
		jugador_actual_es_humano=False	
	lista_de_cartas_validas=[]


	#CICLO PRINCIPAL DE LA PARTIDA
	while True:
		#CICLO DEL TURNO DEL JUGADOR ACTUAL
		while True:


			# ********************************************************************************************************
			# INICIO DE LA CONSTRUCCIÓN DEL TABLERO: Mostrar cada jugador, cuantas cartas tiene, el turno actual y la ultima carta de la pila de descartes
			clear()
			if control_de_flujo == 1:
				orientacion = "↓  "
			else:
				orientacion = "↑  "

			
			l(2)
			esp(6);print("Estado de la partida: ")
			if jugador_actual==0:
				palabra_turno="TURNO ACTUAL: "
			else:
				palabra_turno="              "
			
			
			if un_humano:
				esp(6);print(orientacion+palabra_turno, end="");print(Fore.RED+lista_de_nombres[0], end="");print(" tiene "+str(len(lista_de_jugadores[0]))+" cartas")
			else:
				esp(6);print(orientacion+palabra_turno, end="");print("El jugador 1 tiene "+str(len(lista_de_jugadores[0]))+" cartas")
			if jugador_actual==1:
				palabra_turno="TURNO ACTUAL: "
			else:
				palabra_turno="              "
			if dos_humanos:
				esp(6);print(orientacion+palabra_turno, end="");print(Fore.BLUE+lista_de_nombres[1], end="");print(" tiene "+str(len(lista_de_jugadores[1]))+" cartas")
			else:
				esp(6);print(orientacion+palabra_turno, end="");print("El jugador 2 tiene "+str(len(lista_de_jugadores[1]))+" cartas")
			if juegan_tres:
				if jugador_actual==2:
					palabra_turno="TURNO ACTUAL: "
				else:
					palabra_turno="              "
				if tres_humanos:
					esp(6);print(orientacion+palabra_turno, end="");print(Fore.YELLOW+lista_de_nombres[2], end="");print(" tiene "+str(len(lista_de_jugadores[2]))+" cartas")
				else:
					esp(6);print(orientacion+palabra_turno, end="");print("El jugador 3 tiene "+str(len(lista_de_jugadores[2]))+" cartas")
			if juegan_cuatro:
				if jugador_actual==3:
					palabra_turno="TURNO ACTUAL: "
				else:
					palabra_turno="              "
				if cuatro_humanos:
					esp(6);print(orientacion+palabra_turno, end="");print(Fore.GREEN+lista_de_nombres[3], end="");print(" tiene "+str(len(lista_de_jugadores[3]))+" cartas")
				else:
					esp(6);print(orientacion+palabra_turno, end="");print("El jugador 4 tiene "+str(len(lista_de_jugadores[3]))+" cartas")
			l(1);linea(80);
			if jugador_actual_es_humano:
				l(1);esp(6);print("Turno de "+lista_de_nombres[jugador_actual]+". Presiona ENTER para mostrar tu baraja")
			else:
				l(1);esp(6);print("Turno del jugador ",jugador_actual+1,". Presiona ENTER para que la computadora realice la jugada.")
			l(1);esp(6);print("ULTIMA CARTA --"+historial_de_jugadores[-1]+": ", end="");pila_descarte[-1].mostrar_cara();
			if len(pila_descarte) >=2:
				esp(6);print("               "+str(historial_de_jugadores[-2])+": ", end=""); pila_descarte[-2].mostrar_cara()
			if len(pila_descarte) >=3:
				esp(6);print("               "+str(historial_de_jugadores[-3])+": ", end=""); pila_descarte[-3].mostrar_cara()
			if len(pila_descarte) >=4:
				esp(6);print("               "+str(historial_de_jugadores[-4])+": ", end=""); pila_descarte[-4].mostrar_cara()
			if len(pila_descarte) >=5:
				esp(6);print("               "+str(historial_de_jugadores[-5])+": ", end=""); pila_descarte[-4].mostrar_cara()
			standby()
			linea(80);
			# FIN DE LA CONSTRUCCION DEL TABLERO
			# ********************************************************************************************************
			

			# Este es el condicional de TOMA DOS. Entra en el siempre que la carta anterior haya sido un TOMA DOS
			if toma_dos:
				hay_toma_dos=False
				# Ciclo para determinar si el jugador afectado por el TOMA DOS tiene una carta para defenderse
				for i in lista_de_jugadores[jugador_actual]:
					if isinstance(i,masDos_verde) or isinstance(i,masDos_rojo) or isinstance(i,masDos_azul) or isinstance(i,masDos_amarillo):
						hay_toma_dos=True
				if hay_toma_dos:
					if jugador_actual_es_humano:
						l(1);esp(6);jugar_toma_dos=input("Quieren hacerte agarrar "+str(cascada_toma_dos)+" cartas! Pero puedes defenderte. ¿Deseas jugar otro Toma Dos? si/no:")
						if jugar_toma_dos=="si":
							obligar_toma_dos=True
						else:
							hay_toma_dos=False
					else:
						obligar_toma_dos=True
				if not hay_toma_dos:
					l(1);esp(6); print("Tomas ",cascada_toma_dos," cartas!")
					for i in range(cascada_toma_dos):
						if len(mazo)!=0:
							mazo, lista_de_jugadores[jugador_actual]=ponerCarta(mazo,lista_de_jugadores[jugador_actual],0)
						else:
							if len(pila_descarte) >=2:
								lista_de_jugadores[jugador_actual].append(pila_descarte[0])
								pila_descarte.pop(0)
							else:
								l(1);esp(6); print("Agarraste "+str(i)+" cartas. Ya no hay más cartas en el mazo.")
								break;
					toma_dos=False
					pierde_turno=True
					cascada_toma_dos=0
					obligar_toma_dos=False
			

			# Este es el condicional de TOMA CUATRO. Entra en el siempre que la carta anterior haya sido un TOMA CUATRO
			if toma_cuatro:
				hay_toma_cuatro=False
				# Ciclo para determinar si el jugador afectado por el TOMA CUATRO tiene una carta para defenderse
				for i in lista_de_jugadores[jugador_actual]:
					if isinstance(i,masCuatro):
						hay_toma_cuatro=True
				if hay_toma_cuatro:
					if jugador_actual_es_humano:
						l(1);esp(6);jugar_toma_cuatro=input("Quieren hacerte agarrar "+str(cascada_toma_cuatro)+" cartas! Pero puedes defenderte. ¿Deseas jugar otro Toma Cuatro? si/no:")
						if jugar_toma_cuatro=="si":
							obligar_toma_cuatro=True
						else:
							hay_toma_cuatro=False
					else:
						obligar_toma_cuatro=True
				if not hay_toma_cuatro:
					l(1);esp(6); print("Tomas ",cascada_toma_cuatro," cartas!")
					for i in range(cascada_toma_cuatro):
						#VACIARMAZO
						if len(mazo)!=0:
							mazo, lista_de_jugadores[jugador_actual]=ponerCarta(mazo,lista_de_jugadores[jugador_actual],0)
						else:
							if len(pila_descarte) >=2:
								lista_de_jugadores[jugador_actual].append(pila_descarte[0])
								pila_descarte.pop(0)
							else:
								l(1);esp(6); print("Agarraste "+str(i)+" cartas. Ya no hay más cartas en el mazo.")
								break;
					toma_cuatro=False
					pierde_turno=True
					cascada_toma_cuatro=0
					obligar_toma_cuatro=False
			

			# Este es el condicional de JUGAR UNA CARTA. Entra en el siempre que el jugador actual no haya perdido el turno
			if not pierde_turno:
				
				
				#ENTRA AQUÍ SI EL JUGADOR ACTUAL ES UN HUMANO
				if jugador_actual_es_humano:
					mostrarBaraja(lista_de_jugadores[jugador_actual],6)
					l(1);esp(6);print("Otras opciones:")
					esp(6);print("0. Agarrar una carta del mazo")
					esp(6);print("-1. Salir de la partida")
					
					
					try:
						l(1);linea(80);
						l(1);esp(6);carta_jugada=int(input("¿Qué carta deseas jugar?: "))
					except:
						error=True
						break;
					
					
					if carta_jugada<-1 or carta_jugada>len(lista_de_jugadores[jugador_actual]) :
						l(1);esp(6);print("NÚMERO NO VALIDO, INTENTA DE NUEVO")
						standby()
						clear()
						break;
					
					
					if carta_jugada==-1:
						l(1);linea(80);
						l(1);esp(6);opcion_salir=input("¿Seguro que deseas abandonar la partida? si/no: ")
						if opcion_salir=="si":
							salir=True
							break;
						else:
							clear();continue;
					
					
					if carta_jugada==0:
						tomo_del_mazo=True
						if len(mazo)!=0:
							mazo, lista_de_jugadores[jugador_actual]=ponerCarta(mazo,lista_de_jugadores[jugador_actual],0)
						else:
							if len(pila_descarte) >=2:
								lista_de_jugadores[jugador_actual].append(pila_descarte[0])
								pila_descarte.pop(0)
							else:
								l(1);esp(6); print("Ya no hay más cartas en el mazo. Pierdes el turno!")
								standby()
								break;
						l(1);esp(6);print("Agarraste una carta del mazo")
						if isinstance(lista_de_jugadores[jugador_actual][-1],masCuatro) or isinstance(lista_de_jugadores[jugador_actual][-1],cambia_color):
							esp(6);print("Nueva carta: ",end="");lista_de_jugadores[jugador_actual][-1].mostrar_cara_sin_color()
						else:
							esp(6);print("Nueva carta: ",end="");lista_de_jugadores[jugador_actual][-1].mostrar_cara()
						l(1);esp(6);jugar_carta_nueva=input("¿Deseas intentar jugar esta carta? si/no: ")
						if jugar_carta_nueva=="si":
							ultima_opcion=True
							carta_jugada=len(lista_de_jugadores[jugador_actual])
						else:
							break;
					
					
					if carta_jugada!=0:
						
						
						# Este condicional determina si estamos obligando al jugador a jugar un TOMA DOS debido a que indicó que tiene uno para defenderse
						if obligar_toma_dos and not(isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_amarillo)):
							l(1);esp(6);print("Debes jugar un Toma Dos!")
							standby()
							error=True
							break;
						
						
						# Este condicional determina si estamos obligando al jugador a jugar un TOMA CUATRO debido a que indicó que tiene uno para defenderse
						if obligar_toma_cuatro and not(isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masCuatro)):
							l(1);esp(6);print("Debes jugar un Toma Cuatro!")
							standby()
							error=True
							break;
						
						
						# Este condicional es para determinar si la carta que quiere jugar la persona es válida o no
						if comprobar_validez(lista_de_jugadores[jugador_actual][carta_jugada-1],pila_descarte[-1]):
							# Entra aquí si la carta es valida
							

							#Entra aquí si el jugador quiere jugar un TOMA DOS
							if isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],masDos_amarillo): 
								toma_dos=True
								cascada_toma_dos=cascada_toma_dos+2
							

							#Entra aquí si el jugador quiere jugar un PIERDE TURNO
							if isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],bloqueo_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],bloqueo_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],bloqueo_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],bloqueo_amarillo): 
								pierde_turno=True
							

							#Entra aquí si el jugador quiere jugar un REVERSO
							if isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],reverso_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],reverso_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],reverso_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1],reverso_amarillo): 
								carta_reverso=True
								control_de_flujo=control_de_flujo*(-1)
							

							#Entra aquí si el jugador quiere jugar un CAMBIA COLOR o un TOMA CUATRO
							if isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1], cambia_color) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1], masCuatro):
								# Primero se le pide al jugador elegir el color nuevo
								l(1);linea(80);
								l(1);esp(6);print("Elige un color nuevo")
								esp(6);print("1. "+Fore.RED+"ROJO")
								esp(6);print("2. "+Fore.BLUE+"AZUL")
								esp(6);print("3. "+Fore.GREEN+"VERDE")
								esp(6);print("4. "+Fore.YELLOW+"AMARILLO")
								try:
									l(1);esp(6);color_elegido=int(input("Color elegido: "))
								except:
									if tomo_del_mazo:
										tomo_del_mazo=False
										lista_de_jugadores[jugador_actual], mazo=ponerCarta(lista_de_jugadores[jugador_actual],mazo,-1)
									clear();continue;
								if color_elegido<1 or color_elegido>4:
									clear();continue;
								if color_elegido==1:
									lista_de_jugadores[jugador_actual][carta_jugada-1].asignar_color("ROJO")
								elif color_elegido==2:
									lista_de_jugadores[jugador_actual][carta_jugada-1].asignar_color("AZUL")
								elif color_elegido==3:
									lista_de_jugadores[jugador_actual][carta_jugada-1].asignar_color("VERDE")
								elif color_elegido==4:
									lista_de_jugadores[jugador_actual][carta_jugada-1].asignar_color("AMARILLO")
								
								
								# Luego de elegir el color, si la carta es un TOMA CUATRO, entra aquí
								if isinstance(lista_de_jugadores[jugador_actual][carta_jugada-1], masCuatro):
									toma_cuatro=True
									cascada_toma_cuatro=cascada_toma_cuatro+4

							
							#Finalmente, juega la carta
							lista_de_jugadores[jugador_actual], pila_descarte=ponerCarta(lista_de_jugadores[jugador_actual],pila_descarte,carta_jugada-1)
							historial_de_jugadores.append(" Jugador " +str(jugador_actual+1))
							break;
						
						
						else:
							
							
							# Entra aquí si la carta que el jugador quiere jugar NO es valida
							if ultima_opcion:
								#Entra aquí si la carta que no es valida la acaba de tomar del mazo
								ultima_opcion=False
								l(1);esp(6);print("CARTA NO VALIDA")
								standby()
								clear()
								break;
							
							
							else:
								#Entra aquí si la carta que no es valida es una de su baraja, y puede probar otra o agarrar del mazo
								l(1);esp(6);print("CARTA NO VALIDA, PRUEBA OTRA O TOMA UNA CARTA DEL MAZO")
								standby()
								clear()
				
				
				#ENTRA AQUÍ SI EL JUGADOR ACTUAL ES UNA COMPUTADORA
				else:

					
					#Primero creamos una lista con las posiciones de las cartas que SI se pueden jugar
					for i in range(len(lista_de_jugadores[jugador_actual])):
						if comprobar_validez(lista_de_jugadores[jugador_actual][i],pila_descarte[-1]):
							lista_de_cartas_validas.append(i)
					
					
					#LUEGO ASIGNAMOS DE MANERA ALEATORIA LA CARTA QUE LA COMPUTADORA VA A JUGAR. SI NO HAY CARTAS VALIDAS, LA COMPUTADORA TOMA UNA CARTA DEL MAZO
					if len(lista_de_cartas_validas)!=0:
						posicion_aleatoria=random.randint(1,len(lista_de_cartas_validas))-1
						carta_jugada=lista_de_cartas_validas[posicion_aleatoria]
					else: 
						carta_jugada=-1

					
					# SI LA CARTA JUGADA ES "-1", LA COMPUTADORA VA A AGARRAR UNA CARTA DEL MAZO. SI LA CARTA QUE AGARRA ES VALIDA, LA JUGARÁ. SI NO, LA AGREGA A LA BARAJA Y TERMINA EL TURNO
					if carta_jugada==-1:
						tomo_del_mazo=True
						if len(mazo)!=0:
							mazo, lista_de_jugadores[jugador_actual]=ponerCarta(mazo,lista_de_jugadores[jugador_actual],0)
						else:
							if len(pila_descarte) >=2:
								lista_de_jugadores[jugador_actual].append(pila_descarte[0])
								pila_descarte.pop(0)
							else:
								l(1);esp(6); print("La computadora pierde el turno!")
								standby()
								break;
						l(1);esp(6);print("La computadora agarró una carta del mazo")
						if comprobar_validez(lista_de_jugadores[jugador_actual][-1],pila_descarte[-1]):
							carta_jugada=len(lista_de_jugadores[jugador_actual])-1
						else:
							standby()
							break;


					if carta_jugada!=-1:

						
						# Este ciclo con condicional asegura que la computadora va a jugar un TOMA DOS en caso de verse obligado a hacerlo porque esta siendo atacada
						while True:
							if obligar_toma_dos and not(isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_amarillo)):
								posicion_aleatoria=random.randint(1,len(lista_de_cartas_validas))-1
								carta_jugada=lista_de_cartas_validas[posicion_aleatoria]
							else:
								break;
						
						
						# Este ciclo con condicional asegura que la computadora va a jugar un TOMA CUATRO en caso de verse obligado a hacerlo porque esta siendo atacada
						while True:
							if obligar_toma_cuatro and not(isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masCuatro)):
								posicion_aleatoria=random.randint(1,len(lista_de_cartas_validas))-1
								carta_jugada=lista_de_cartas_validas[posicion_aleatoria]
							else:
								break;
						

						#Entra aquí si la computadora juega un TOMA DOS
						if isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],masDos_amarillo): 
							toma_dos=True
							cascada_toma_dos=cascada_toma_dos+2
							
						
						#Entra aquí si la computadora juega un PIERDE TURNO
						if isinstance(lista_de_jugadores[jugador_actual][carta_jugada],bloqueo_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],bloqueo_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],bloqueo_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],bloqueo_amarillo): 
							pierde_turno=True
							
						
						#Entra aquí si la computadora juega un REVERSO
						if isinstance(lista_de_jugadores[jugador_actual][carta_jugada],reverso_verde) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],reverso_azul) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],reverso_rojo) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada],reverso_amarillo): 
							carta_reverso=True
							control_de_flujo=control_de_flujo*(-1)
							
						
						#Entra aquí si la computadora juega un CAMBIA COLOR o un TOMA CUATRO. La computadora elige el siguiente color de manera aleatoria
						if isinstance(lista_de_jugadores[jugador_actual][carta_jugada], cambia_color) or isinstance(lista_de_jugadores[jugador_actual][carta_jugada], masCuatro):
							color_elegido=random.randint(1,4)
							if color_elegido==1:
								lista_de_jugadores[jugador_actual][carta_jugada].asignar_color("ROJO")
							elif color_elegido==2:
								lista_de_jugadores[jugador_actual][carta_jugada].asignar_color("AZUL")
							elif color_elegido==3:
								lista_de_jugadores[jugador_actual][carta_jugada].asignar_color("VERDE")
							elif color_elegido==4:
								lista_de_jugadores[jugador_actual][carta_jugada].asignar_color("AMARILLO")
							
							
							# Luego de elegir el color, si la carta es un TOMA CUATRO, entra aquí
							if isinstance(lista_de_jugadores[jugador_actual][carta_jugada], masCuatro):
								toma_cuatro=True
								cascada_toma_cuatro=cascada_toma_cuatro+4
						
						
						#Finalmente, juega la carta
						lista_de_jugadores[jugador_actual], pila_descarte=ponerCarta(lista_de_jugadores[jugador_actual],pila_descarte,carta_jugada)
						historial_de_jugadores.append(" Jugador " +str(jugador_actual+1))
						lista_de_cartas_validas = []
						l(1);esp(6);print("Carta jugada por la computdora: ", end="");pila_descarte[-1].mostrar_cara()
						standby()
						break;

			else:
				#Entra en este condicional si el jugador perdió el turno
				l(2);esp(6); print("Pierdes el Turno!")
				pierde_turno=False
				standby()
				break;

		
		#FIN DE CICLO DEL TURNO
		#INICIO DE LOS PREPARATIVOS PARA EL SIGUIENTE TURNO

		
		# El flujo entra en el condicional si el jugador elije finalizar la partida súbitamente
		if salir:
			break;
		
		
		# El flujo entra en el condicional si el jugador actual tiene CERO cartas, declarandolo ganador y finalizando la partida
		if len(lista_de_jugadores[jugador_actual])==0:
			if jugador_actual_es_humano:
				clear()
				l(2);esp(6);print("Felicitaciones "+lista_de_nombres[jugador_actual]+", ganaste la partida!")
				break;
			else:
				clear()
				l(2);esp(6);print("El jugador ",jugador_actual+1," ganó la partida!")
				break;
		
		
		# El flujo entra en el condicional si ocurrió algún error durante el turno, y se requiere inicial el turno nuevamente con el mismo jugador
		if error:
			error=False
			continue;

		
		#El flujo entra en el condicional si sólo hay 2 jugadores y alguno de ellos pone una carta reverso. Según las reglas de UNO, el que puso la carta reverso puede jugar de nuevo
		if carta_reverso and numero_de_jugadores==2:
			carta_reverso=False
			clear();continue;

		
		#Las siguientes instrucciones son para asignar un nuevo valor a la variable JUGADOR ACTUAL, para que en la siguiente iteración del ciclo, le toque al siguiente jugador en la lista
		jugador_actual=jugador_actual+control_de_flujo
		
		
		#Los condicionales siguiente funcionan para que la variable JUGADOR ACTUAL no adquiera un valor que se encuentre fuera del rango de la lista de jugadores
		if jugador_actual==numero_de_jugadores:
			jugador_actual=0
		if jugador_actual==-1:
			jugador_actual=numero_de_jugadores-1


		#Las siguientes instrucciones determinan si el proximo jugador va a ser una computadora o un humano
		if jugador_actual==0:
			if un_humano:
				jugador_actual_es_humano=True
			else:
				jugador_actual_es_humano=False
		
		if jugador_actual==1:
			if dos_humanos:
				jugador_actual_es_humano=True
			else:
				jugador_actual_es_humano=False
		
		if jugador_actual==2:
			if tres_humanos:
				jugador_actual_es_humano=True
			else:
				jugador_actual_es_humano=False
		
		if jugador_actual==3:
			if cuatro_humanos:
				jugador_actual_es_humano=True
			else:
				jugador_actual_es_humano=False


	#BORRAR VARIABLES Y LISTAS 
	del mazo
	del pila_descarte
	del baraja1
	del baraja2
	del historial_de_jugadores
	if juegan_tres:
		del baraja3
	if juegan_cuatro:
		del baraja4
	del lista_de_jugadores


	l(1);esp(6);print("Partida Finalizada. Gracias por jugar!")
	standby()
	clear()