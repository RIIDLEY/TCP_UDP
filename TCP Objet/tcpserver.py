import socket
import sys

class tcpserver:
    def __init__(self, port):               #Constructeur du serveur
        self.TCP_PORT=int(port)             #Instancie le Port d'écoute
        self.TCP_IP = ""                    #Instancie Adresse IP de la machine (automatique) ""=adresse IpV4
        self.BUFFER_SIZE = 1024
        self.sock = socket.socket(socket.AF_INET, # Internet        Création du socket
                                    socket.SOCK_STREAM) # UDP
        self.sock.bind((self.TCP_IP, self.TCP_PORT))                #Liaison entre l'Ip, le Port et le socket
        self.sock.listen(1)                                         #Autorisation les connexions

    def recevoirMessage(self):
        while True:                                                                  #Boucle infini pour ne pas arrete la serveur au premier message
            conn, addr = self.sock.accept()                                          #Accepte une connexion
            print("client d'adresse " + addr[0] + " depuis port " + str(addr[1]))    #Print les informations du client (IP et Port)
            data = conn.recv(self.BUFFER_SIZE)                                       #Recupere les informations du client
            if not data: break                                                       #S'il n'y a pas de message, on arrete la connexions au serveur
            print("ok :", data.decode("utf-8")+'')                                   #Print le message décode en utf-8 du client
            conn.send(data)                                                          #Renvoie le message au client
        conn.close()

servertest=tcpserver(sys.argv[1])
servertest.recevoirMessage()



#port
#argv[1]=Port d'écoute
