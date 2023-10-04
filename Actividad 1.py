
kilometros = 800 

dias = 8

preciodelkilometro = 0.63

descuento = 30


kilometros = int(input("ingrese los kilometros que recorrera: "))
dias = int(input("ingrese los dias que se quedara: "))

#precio sin el descuento
if kilometros > 800 and dias > 7:
    preciosindescuento = kilometros * preciodelkilometro

    preciodeldescuento = preciosindescuento - descuento

else : 
    preciosindescuento = kilometros * preciodelkilometro
    print("el precio final seria: ${:,.2f}".format(preciosindescuento))
    
  




