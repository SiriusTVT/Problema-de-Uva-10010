#Juan David Troncoso
from operator import index


def waldorf():
	sopa_de_letras=[]
	matriz_de_letras=[]
	matriz_de_letras_buscar=[]
	contador=0
	casos=int(input()) #Casos que el programa va ejecutar para diferentes casos
	espacio=input()
	#print(" ")
	for a in range(casos): #Casos que se va ejecutar el programa
		matriz=input() #Entrada de las dimensiones de la matriz
		sep=matriz.split() #Separa los valores ingresados
		sopa_de_letras.append(int(sep[0])) #Guarda los valores de la matriz
		sopa_de_letras.append(int(sep[1]))

		for b in range(sopa_de_letras[0]):
			letras=input() #Entrada Matriz de Letras
			if len(letras)!=sopa_de_letras[1]: #SI sobrepasa el tamaño de largo de la matriz se aborta el programa
				print("La cadena no cumple el tamaño: ", sopa_de_letras[1])
				contador=1
				break
			else:
				matriz_de_letras.append([letras]) #Caso contrario guarda la matriz en sublistas dentro de una lista 
												  #Listas(filas), SUBLista(columnas)

		if contador==1: #Se aborta si el contador es igual 1
			break

		
		letras_buscar=int(input()) #Palabras para Buscar
		for c in range(letras_buscar):
			letras=input() #Entrada para la palabras que se van a buscar en la matriz
			matriz_de_letras_buscar.append([letras]) #Se agregan las palabras en sublistas para recorrelas cuando se encuentre una.


		#print(matriz_de_letras)
		#print(matriz_de_letras_buscar)

		#Comprobar a Letras y Buscar letras en la matriz

		noencontrada=False #Si no encuentra la palabra en todo el recorrido de la matriz
		encontrada=False #Si encuentra la palabra pasa a la siguiente
		contador=0 #Si no hay mas palabras por buscar se termina el programa

		for listaMB in range(len(matriz_de_letras_buscar)): #recorre la matriz de las letras a buscar
			if contador!=len(matriz_de_letras_buscar): #Si no hay mas palabras por buscar se termina el programa
				for sublistaMB in range(len(matriz_de_letras_buscar[listaMB][0])): #recorre la matriz de las letras a buscar por cada letra de cada palabra
					if encontrada==False: #Si encuentra la palabra pasa a la siguiente
						for listaM in range(len(matriz_de_letras)): #recorre la matriz de las letras por filas
							if encontrada==False: #Si encuentra la palabra pasa a la siguiente
								for sublistaM in range(len(matriz_de_letras[listaM][0])): #recorre la matriz de las letras por columnas
									if encontrada==False: #Si encuentra la palabra pasa a la siguiente

										#print(matriz_de_letras[listaM][0][sublistaM], matriz_de_letras_buscar[listaMB][0][sublistaMB])
										
										#Comparacion de letras
										try:
											if matriz_de_letras_buscar[listaMB][0][sublistaMB].lower()==matriz_de_letras[listaM][0][sublistaM].lower():
												#Para valores de 1 letra:
												if sublistaMB+1==len(matriz_de_letras_buscar[listaMB][0]):
													tmp=listaM #guarda los valores de los indices temporalmente
													tmp1=sublistaM #guarda los valores de los indices temporalmente
													encontrada=True #Encuentra la palabra para pasar a la siguiente
													contador+=1 #Pasa a la siguiente palabra a buscar
													#print("tmp", tmp, "tmp1", tmp1)
													break
												#Para valores de 2 letras:
												elif sublistaMB+2==len(matriz_de_letras_buscar[listaMB][0]):
													if (matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM][0][sublistaM+1].lower() or
														matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM+1][0][sublistaM+1].lower() or
														matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM+1][0][sublistaM].lower() or
														matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM][0][sublistaM-1].lower()):
															tmp=listaM #guarda los valores de los indices temporalmente
															tmp1=sublistaM #guarda los valores de los indices temporalmente
															encontrada=True #Encuentra la palabra para pasar a la siguiente
															contador+=1 #Pasa a la siguiente palabra a buscar
															#print("tmp", tmp, "tmp1", tmp1)
															break
												
												#Para valores mas de 2 letras:

												#Primera letra que coincide, entra para probar si es la palabras
												SMB=sublistaMB #guarda los indices actuales
												SMBM=sublistaM #guarda los indices actuales
												LM=listaM #guarda los indices actuales
												cumple=2 #Observa que si se cumple la primera como la segunda palabra, 
												#El indice empieza analizar desde la siguiente que seria la tercera hasta el tamaño de la palabra

												#print("-Entro1- coincide palabra")
												if matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM][0][sublistaM+1].lower():
													#Segunda letra se encuentra al lado derecho ?
													SMB+=1
													SMBM+=1
													for test in range(SMB+1, len(matriz_de_letras_buscar[listaMB][0])):
														SMBM+=1
														#Encuentre las demas letras apartir de la segunda letra
														#print(matriz_de_letras_buscar[listaMB][0][test], matriz_de_letras[listaM][0][SMBM])
														if matriz_de_letras_buscar[listaMB][0][test].lower()==matriz_de_letras[listaM][0][SMBM].lower(): #Busca la siguiente letra despues de la segunda
															cumple+=1
															if cumple==len(matriz_de_letras_buscar[listaMB][0]): #Si cumple es igual al tamaño de la palabra encontro la palabra
																#print("Entro2 lado derecho")													
																tmp=listaM #guarda los valores de los indices temporalmente
																tmp1=sublistaM #guarda los valores de los indices temporalmente
																encontrada=True #Encuentra la palabra para pasar a la siguiente
																contador+=1 #Pasa a la siguiente palabra a buscar
																#print("tmp", tmp, "tmp1", tmp1)
														else:
															break #Rompe si no coincide la ubicacion de la letra
														
												elif matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM+1][0][sublistaM+1].lower():
													#Segunda letra se encuentra diagonalmente hacia el lado derecho ?
													SMB+=1
													SMBM+=1
													LM+=1
													for test in range(SMB+1, len(matriz_de_letras_buscar[listaMB][0])):
														SMBM+=1
														LM+=1
														#print(matriz_de_letras_buscar[listaMB][0][test], matriz_de_letras[LM][0][SMBM])
														if matriz_de_letras_buscar[listaMB][0][test].lower()==matriz_de_letras[LM][0][SMBM].lower():
															cumple+=1
															if cumple==len(matriz_de_letras_buscar[listaMB][0]):
																#print("Entro3 diag derh")
																tmp=listaM
																tmp1=sublistaM
																encontrada=True
																contador+=1
																#print("tmp", tmp, "tmp1", tmp1)
														else:
															break
														
												elif matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM+1][0][sublistaM].lower():
													#Segunda letra se encuentra debajo de la primera letra ?
													SMB+=1
													LM+=1
													for test in range(SMB+1, len(matriz_de_letras_buscar[listaMB][0])):
														LM+=1
														#print(matriz_de_letras_buscar[listaMB][0][test], matriz_de_letras[LM][0][sublistaM])
														if matriz_de_letras_buscar[listaMB][0][test].lower()==matriz_de_letras[LM][0][sublistaM].lower():
															cumple+=1
															if cumple==len(matriz_de_letras_buscar[listaMB][0]):
																#print("Entro4 abajo")
																tmp=listaM
																tmp1=sublistaM
																encontrada=True
																contador+=1
																#print("tmp", tmp, "tmp1", tmp1)
														else:
															break

												elif matriz_de_letras_buscar[listaMB][0][sublistaMB+1].lower()==matriz_de_letras[listaM][0][sublistaM-1].lower():
													SMB+=1
													SMBM-=1
													for test in range(SMB+1, len(matriz_de_letras_buscar[listaMB][0])):
														SMBM-=1
														#print(matriz_de_letras_buscar[listaMB][0][test], matriz_de_letras[listaM][0][SMBM])
														if matriz_de_letras_buscar[listaMB][0][test].lower()==matriz_de_letras[listaM][0][SMBM].lower():
															cumple+=1
															if cumple==len(matriz_de_letras_buscar[listaMB][0]):
																#Segunda letra se encuentra al lado izquierdo ?
																#print("Entro5 lado izq")
																tmp=listaM
																tmp1=sublistaM
																encontrada=True
																contador+=1
																#print("tmp", tmp, "tmp1", tmp1)
														else:
															break
										except IndexError: #Si se sale del indice es porque no existe una letra proxima de la palqabra que se busca
											a=None			#Se ignora para pasar a la siguiente palabra. 
																			
						if encontrada==False: #Si nunca encontro la palabra en la matriz entra por aqui
							noencontrada=True #No encontro la palabra							
							encontrada=True #Pasa hacer encontrada para seguir con la siguiente palabra de la lista
							contador+=1 #Se suma el contador para avanzar en el tamaño de la matriz de letras buscar
							break #Rompe para pasar abajo			
				if noencontrada==False: #Tanto no fue encontrada no existe idices para la palabra buscada
					print(tmp+1, tmp1+1) #Indices Finales donde se encuentran las ubicaciones de las palabras.
					encontrada=False #Pasa a la siguiente palabra
				noencontrada=False #Se resetean para la siguiente palabra existente
				encontrada=False     
		sopa_de_letras=[] #Resetea para el siguiente caso
		matriz_de_letras=[]
		matriz_de_letras_buscar=[]
		contador=0
		print(" ")		

waldorf()