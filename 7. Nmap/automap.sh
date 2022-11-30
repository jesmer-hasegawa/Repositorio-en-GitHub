#!/bin/bash
# Definimos el menu

echo "< Practica 09 -  Homero Galindo >"
echo "1. Escaneo de red"
echo "2. Escaneo individual"
echo "3. Escaneo udp"
echo "4. Escaneo de script"
echo "5. Salir"
echo -n "Escoger opcion: "
read opcion
#Seleccion de menu
case $opcion in
1) echo "Ha seleccionado escaneo de red!"
echo -n "Ingresa tu subred: "
read subred
nmap -sn $subred -oN test_opcion1.txt
;;
2)echo "Ha seleccionado escaneo individual!"
echo -n "Ingresa la ip: "
read ip
nmap -v -A $ip -oN test_opcion2.txt
;;
3)echo "Ha seleccionado escaneo udp!"
echo -n "Ingresa la ip: "
read ip
nmap --script ssl-poodle $ip -oN test_opcion3.txt
;;
4)echo "Ha seleccionado escaneo de script!"
echo -n "Ingresa la ip: "
read ip
nmap --script ssl-ccs-injection $ip -oN test_opcion4.txt
;;
5) exit 0;;
#Alerta
*)echo "Opcion invalida..."
sleep 1
esac
