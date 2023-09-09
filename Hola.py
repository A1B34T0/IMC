
#se inicializan variables
cont = 0
x=0
#While que verifica que la variable nombre no este vacia
while cont == 0:

   #Se pide el nombre de la persona a travez de input
   nombre=input("Ingrese su nombre: ")

   #si la entrada se detecta vacia se ejecuta el if
   if not nombre:
       print("Ingrese un nombre valido")
   
   #sino se le suma 1 en el contador rompiendo el ciclo
   else:
       cont= cont+1    

#while para verificar que el apellido no se encuentre vacio
while cont >0:
    
    #Se pide el apellido paterno
    apellidop=input("Ingrese su apellido paterno: ")
    
    #si la entrada se detecta vacia se ejecuta el if
    if not apellidop:
       print("Ingrese un apellido valido")
    #sino se le resta 1 en el contador rompiendo el ciclo
    else:
       cont= cont-1

#while para verificar que el apellido materno no este vacio
while cont ==0:
    
    #Se pide el apellido materno
    apellidom= input("Ingrese su apellido materno: ")
    
    #si la entrada se detecta vacia se ejecuta el if
    if not apellidom:
       print("Ingrese un apellido valido")
    #sino se le suma 1 en el contador rompiendo el ciclo
    else:
       cont= cont+1

#while para verificar que el valor de peso sea el correcto
while cont >0:
   #Se solicita el peso de la persona 
   peso= input("Ingrese su peso: ")
   #Empieza el try 
   try:
      
      #Se ejecuta un if verificando si el peso es una cantidad decimal 
      if str(float(peso)) == peso:
        
        
        #se guarda el valor de peso en x
        x=float(peso)
        peso=x
        #Se le resta al contador -1
        cont= cont-1
        
      #si no es un entero tambien es aceptado
      else:
       
        #Se guarda el valor de peso en x
        x=float(peso)
        
        #se actualiza el valor de peso
        peso=x

        #Se disminuyes el contador en -1
        cont= cont-1
        
   #El mensaje se enviara en caso de provocar la exepcion al ver que la entrada no es un valor numerico
   except:
      print("Ingrese un peso valido")
      
#While para verificar que el valor de altura sea valido
while cont ==0:
   
   #Se solicita el peso de la persona 
   altura= input("Ingrese su altura: ")
   
   #Se empieza un try 
   try:
      
      #Se ejecuta un if verificando si el peso es una cantidad decimal 
      if str(float(altura)) == altura:
        
        
        #se guarda el valor de altura en x de tipo float
        x=float(altura)
        
        #Se actualiza el valor de altura
        altura=x
        
        #Se aumenta al contador en 1
        cont= cont +1
        
      #si no es un entero tambien es aceptado
      else:
       
        #Se guarda el valor de altura en x de tipo entero
        x=int(altura)
        
        #Se actualiza el valor de altura
        altura=x
        #Se aumenta el contador en 1
        cont= cont +1
        
   #El mensaje se enviara en caso de provocar la exepcion al ver que la entrada no es un valor numerico
   except:
      print("Ingrese una altura valida")

#While para verificar que el valor de edad sea valido 
while cont >0: 
   
   #Se pide la edad de la persona
   edad= input("Ingrese su edad: ")
   
   #Inicia un try
   try:
      
      #Se verifica que edad sea un valor entero
      if str(int(edad)) == edad:
          
          #Se disminuye el valor del cantador
          cont= cont-1
          
          #Se guarda el valor de edad en x de tipo int
          x= int(edad)
          
          #Se actualiza el valor de edad
          edad =x
   
   #El mensaje se enviara en caso de generar una excepcion       
   except:
      print("Ingrese una edad valida")
      

#Se calcula la primera parte del imc
temp= altura*altura

#Se calcula el indice de msasa corporal
imc=peso/temp

#Se imprime el imc de la persona
print("Nombre: ")
print(nombre +" "+ apellidop +" "+ apellidom)
print("Edad:")
print(edad)
print("Indice de masa corporal: ")
print(imc)