#!/usr/bin/env python
 
import rospy
from std_msgs.msg import Int32
 
procesamiento = False
nuevo_mensaje = False
mensaje = None
 
def callback(data):
    global procesamiento, nuevo_mensaje, mensaje
    rospy.loginfo("mensaje recibido: %s",data.data)
    
    if not procesamiento:
        nuevo_mensaje = True
        mensaje = data
 
def subs():
    global procesamiento, nuevo_mensaje, mensaje
    rospy.init_node('subscriber')
    rospy.Subscriber('contar_hasta_10', Int32, callback)
    frecuencia = rospy.Rate(5)
    contador = 0
    acumulador = 0
    
    while contador != 10:
        if nuevo_mensaje:
            procesamiento = True
            nuevo_mensaje = False
            rospy.loginfo(mensaje)
            frecuencia.sleep()
            procesamiento = False
            acumulador += mensaje.data
            contador += 1

    print("\n")
    print("La suma de los numeros introducidos es ---> {}".format(acumulador))

if __name__ == '__main__':
    
    try:
        subs()

    finally:
        pass
