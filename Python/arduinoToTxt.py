import serial, serial.tools.list_ports
import keyboard
import time
import matplotlib

path = "data.csv"

delay = .2 # temps entre deux commandes clavier, trop petit = commandes pas prises en compte

heartRatesBuffer = []
timesBuffer = []


def shutdown(oTime):
    keyboard.press_and_release('windows+r')
    time.sleep(delay)
    keyboard.write('shutdown -s -t ' + oTime)
    time.sleep(delay)
    keyboard.press_and_release('enter')
    time.sleep(delay)
    keyboard.press_and_release('enter')

def cancel():
    keyboard.press_and_release('windows+r')
    time.sleep(delay)
    keyboard.write('shutdown -a')
    time.sleep(delay)
    keyboard.press_and_release('enter')

ports = list(serial.tools.list_ports.comports())   #on fait une liste des ports
for p in ports: #pour chaque port on regarde si ils correspondent à un arduino
    p = str(p).lower()
    if "arduino" in p or "ch340" in p:
        port = p[0:4] #si c'est le cas on selectionne le port.
    else:
        port = "COM" + input("Aucun arduino détecté, selectionner manuellement le port: COM") #si aucun port ne correspond (arduino non officiel donc pas forcément arduino dans le nom) on demande de le saisir manuellement.

a = input("Appuyer sur entrer pour commencer. ")
if a != "":
    if a[-4:] == ".csv":
        print("-Les données seront enregistrées dans '" + a + "' au lieux de '" + path + "'.")
        path = a

try:
    ser = serial.Serial(port, baudrate=9600)
    print("-On utilise le " + ser.name.upper())
except:
    print("Pas d'arduino branché ou port déja occupé.")
    exit()
print("-Placer le capteur.")

i = 0
while True:

    a = str(ser.read(16)) #on lis 15 bytes par 15 bytes
    #print(a[2:15])
    
    if a[2] == "I": #initialisé
        pass
    
    elif a[2] == "S": #sensor error
        print("Sensor Error!")
        break
    
    elif a[2] == "N": #no finger
        break
    
    if "hr" in a[2:17]:
        heartRatesBuffer.append(a[13:15])
        timesBuffer.append(a[2:10])
        print(timesBuffer)
        print(heartRatesBuffer)

    if i == 9:
        i = 0
        a = 0
        for j in heartRatesBuffer:
            a += int(j)
        a = int(a / len(heartRatesBuffer))
        with open(path, "a") as f: 
            f.write("{0},{1}\n".format(timesBuffer[-1], a))
        heartRatesBuffer = []
        timesBuffer = []
    else:
        i += 1

print("Appareil retiré: Fin.")
ser.close()
exit()