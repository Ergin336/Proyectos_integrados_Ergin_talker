#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
 
def publicador_ros():
    publicador = rospy.Publisher('contar_hasta_10', Int32, queue_size=10)
    rospy.init_node('publisher')
    frecuencia = rospy.Rate(30)
    mensaje = Int32()
    
    while not rospy.is_shutdown():
        mensaje.data = int(input("Escribe un valor entero: "))
        publicador.publish(mensaje)
        rospy.loginfo(mensaje)
        frecuencia.sleep()
 
if __name__ == '__main__':
    
    try:
        publicador_ros()

    except:
        pass