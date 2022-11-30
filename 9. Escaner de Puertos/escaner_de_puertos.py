import nmap
# Jesus Homero Galindo Gaytan

scaner = nmap.PortScanner()
print("1 Escaneo UDP")
print("2 Escaneo completo")
print("3 Deteccion de sistema operativo")
print("4 Escaneo de red con ping")
opcion = input("Ingresa un numero: ")

if opcion == 1:
	print(scaner.scan('192.168.1.65', arguments='-n -Pn -sU -p- -v'))
elif opcion == 2:
	print(scaner.scan('192.168.1.65', arguments='-p 1-65535 -T4 -A -v'))
elif opcion == 3:
	print(scaner.scan('192.168.1.65', arguments='-sV -O -v'))
elif opcion == 4:
	scaner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
 	


