import socket
import sys

class udpserver:
    def __init__(self, port):       #Constructeur du serveur
        self.UDP_PORT=int(port)     #Instancie le Port d'écoute
        self.UDP_IP = ""            #Instancie Adresse IP de la machine (automatique) ""=adresse IpV4
        self.sock = socket.socket(socket.AF_INET, # Internet        Création du socket
                                    socket.SOCK_DGRAM) # UDP
        self.sock.bind((self.UDP_IP, self.UDP_PORT))            #Liaison entre l'Ip, le Port et le socket

    def recevoirMessage(self):
        while True:                                                                    #Boucle infini pour ne pas arrete la serveur au premier message
            data, addr = self.sock.recvfrom(1024)                                      #Recupere les informations du client
            print("client d'adresse " + addr[0] + " depuis port " + str(addr[1]))      #Print les informations du client (IP et Port)
            print("ok :", data.decode("utf-8")+'')                                     #Print le message décode en utf-8 du client
            self.sock.sendto(data,addr)                                                #Renvoie le message au client

servertest=udpserver(sys.argv[1])                 #Creation du serveur
servertest.recevoirMessage()                      #Utilisation de la méthode recevoirMessage



#port
#argv[1]=Port d'écoute
