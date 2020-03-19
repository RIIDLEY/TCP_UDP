import socket
import sys

class tcpclient:
    def __init__(self, port, ip):                        #Constructeur du client
        self.TCP_PORT=int(port)                          #Instancie le port distant
        self.TCP_IP = ip                                 #Instancie le l'ip du serveur (broadcast impossible en TCP)
        self.BUFFER_SIZE = 1024                          #Instantcie la taille du buffer
        self.sock = socket.socket(socket.AF_INET, # Internet            Creation du socket
                socket.SOCK_STREAM) #UDP

    def envoyerMessage(self):    #Envoie le message au serveur
        self.sock.connect((self.TCP_IP, self.TCP_PORT))              #Connection au socket avec l'Ip (TCP_IP) et le Port (TCP_PORT)
        self.sock.send(bytes(sys.argv[3], "utf-8"))                  #Envoie le message (argv[3]) vers TCP_IP (adresse ip du serveur) par le port TCP_PORT. Avec convertion en bytes


    def recevoirMessage(self):      #Recevoir la reponse du serveur
        rep=True
        while rep == True:
            try:
                self.sock.settimeout(5)                                              #Attend 5sec la réponse d'autre serveur
                data, addr =self.sock.recvfrom(self.BUFFER_SIZE)                     #Recupere la réponse du serveur
                print("recu : \"ok : "+ str(data.decode("utf-8"+'')) + "\"")         #Print dans le terminal du client avec décodage en utf-8 ce que le serveur à reçue
            except socket.timeout:
                print("Plus de réponse")
                rep = False;                                                         #Met rep en false, pour dire qu'il n'y a plus de serveur ce qui arrete la boucle
                self.sock.close()                                                    #Ferme la connexion

clienttest=tcpclient(sys.argv[1], sys.argv[2])                                       #Creation d'un client
clienttest.envoyerMessage()                                                          #Envoie d'un message
clienttest.recevoirMessage()                                                         #Reception de la réponse serveur

#IP serveur port message
#argv[1]=Port Distant   argv[2]=IP  argv[3]=Message
