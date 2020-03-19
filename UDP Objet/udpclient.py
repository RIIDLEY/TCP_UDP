import socket
import sys

class udpclient:
    def __init__(self, port, ip):                         #Constructeur du client
        self.UDP_PORT=int(port)                           #Instancie le port distant
        self.UDP_IP = ip                                  #Instancie le l'ip du serveur ou broadcast
        self.sock = socket.socket(socket.AF_INET, # Internet            Création du socket
                socket.SOCK_DGRAM) #UDP

    def envoyerMessage(self):   #Envoie le message au serveur
        self.sock.sendto(bytes(sys.argv[3], "utf-8"), (self.UDP_IP, self.UDP_PORT))     #Envoie le message (argv[3]) vers UDP_IP (adresse broadcast ou adresse ip du serveur) par le port UDP_PORT. Avec convertion en bytes

    def recevoirMessage(self):  #Reception des messages du serveur
        rep = True
        while rep == True:                                                      #Boucle pour attendre la réponse des serveurs
            try:
                self.sock.settimeout(5)                                         #Attend 5sec la réponse d'autre serveur
                data, addr = self.sock.recvfrom(1024)                           #Recupere la réponse du serveur
                #print("Adresse Ip du Serveur : " + addr[0] + " | Port d\'écoute du serveur : " + str(addr[1]))    #Print l'adresse et le port du serveur
                print("recu : \"ok : "+ str(data.decode("utf-8"+'')) + "\"")         #Print dans le terminal du client avec décodage en utf-8 ce que le serveur à reçue
            except Exception as e:
                print("Plus de réponse")
                rep = False                                                     #Met rep en false, pour dire qu'il n'y a plus de serveur ce qui arrete la boucle

clienttest=udpclient(sys.argv[1], sys.argv[2])                                  #Creation d'un client
clienttest.envoyerMessage()                                                     #Envoie d'un message
clienttest.recevoirMessage()                                                    #Reception de la réponse serveur

#IP serveur/broadcast port message
#argv[1]=Port Distant   argv[2]=IP  argv[3]=Message
