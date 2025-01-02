#Se realiza un programa para calcular el IMC de una persona Proyecto1
print("\n")#se imprime un salto de linea 
#Bienvenida y descripcion del programa al usuario final
print("Bienvenido a nuestro proyecto de UCAMP")
print("Deseamos que tenga excelente dia, a continuacion vamos a pedir sus datos, ")
print("Sus datos se usaran para calcular su Indice de Masa Corporal IMC")
print("\n")

val=True #se declara esta variable para poder iniciar el while

while val: #mientras la instruccion sea verdadera se cumplen las sentecias

    try:# try nos sirve para que se ingresen valores validos por el usuario final
        nombre = input("Ingrese su nombre o nombres: ").strip()#strip elimina espacios en blancos
        if not nombre:#se realiza esta sentencia para verificar que el usuario haya capturado el campo
           raise ValueError("Debe ingresar un dato")#Al estar vacio se manda a imprimir este mensaje
        
        ap=input("Ingrese su apellido paterno: ").strip()#elimina espacios en blanco
        if not ap:#se valida que la variable para verificar que el usuario haya ingresado sus datos
            raise ValueError("Debe ingresar un dato")#si esta en blanco se manda este mensaje
        
        am=input("Ingrese su apellido materno: ").strip()#strip elimina espacios en blancos
        if not am:#se valida la variable que tenga informacion
            raise ValueError("Debe ingresar un dato")#en caso de tener se manda este mensaje
        
        edad=int(input('Ingrese su edad: ').strip())#conversion de texto a entero y el .strip dentro del input
        if edad<=0:#se valida que edad sea un dato valido
            raise ValueError("Ingresa una edad valida")#mensaje al usuario

        peso=float(input('Ingrese su peso: ').strip())#conversion de texto a decimal
        if peso <= 0:#se valida que peso sea un dato valido
            raise ValueError("Ingresa un peso valido")#mensaje al usuario

        estatura=float(input('Ingrese su estatura: ').strip())#conversion de texto a entero
        if estatura <= 0:#se valida que estatura sea un dato valido
            raise ValueError("Ingresa una medida valida")#mensaje al usuario
        
        val=False#a la variable val le damos el valor de falso para que se termine el while

    except ValueError as e:#complemento de try y en la siguiente linea mandamos mensaje al usuaio final
       print(f"Error: {e}")#print del except
    
imc=peso/(estatura**2)#se calcula el IMC, con los datos proporcionados por el usuario
print("\n***** IMPRESION DE RESULTADOS*****")
print(f"Nombre(s): {nombre}\nApellido Paterno: {ap}\nApellido Materno: {am}")#se ocupa una cadena formateada
print(f"Edad: {edad} años.\nPeso: {peso} kg.\nEstatura: {estatura} metros")
print(f"Su Indice de Masa Corporal (IMC) es: {imc:.2f}")
#para imprimir varias variables y texto a la vez

if imc <= 18.9:
    print(f"{nombre} {ap} {am}, se encuentra en un PESO BAJO")
else:
    if imc >= 18.91 and imc <= 24.99:
        print(f"{nombre} {ap} {am}. se encuentra en su PESO NORMAL")
    else:
        if imc >=25.00 and imc <=29.99:
            print(f"{nombre} {ap} {am}. se encuentra en SOBREPESO")
        else:
            if imc >=30.00 and imc <=34.99:
                print(f"{nombre} {ap} {am}. se encuentra en OBESIDAD LEVE")
            else:
                if imc >=35.00 and imc <= 39.99:
                    print(f"{nombre} {ap} {am}. se encuentra en OBESIDAD MEDIA")
                else:
                    print(f"{nombre} {ap} {am}. se encuentra en OBESIDAD MORBIDA")

print("Gracias por proporcionar sus datos y hasta pronto...")