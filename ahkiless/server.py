
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_connections():
    """Cette boucle attend indéfiniment (infiniment) les demandes de clients potentiels"""
    while True:
        """Tout d'abord, l'objet socket doit accepter une certaine demande."""
        client, client_address = SERVER.accept()
        # La méthode accept renvoie un objet socket qui est la connexion
        # et l'adresse du client qui établit la connexion
        adresses[client] = client_address  # stocke l'adresse du client dans le dictionnaire d'adresses
        Thread(target=traiter_client, args=(client,)).start()


def traiter_client(client):  # Reçoit le socket du client en argument
    """Gère une seule connexion client."""
    """Obtenir le nom que mon client a l'intention d'utiliser pour la connexion via le socket 'client' qui a été
     retourné par accepter----- # le nom aura un maximum de 1024 octets d'informations"""
    name = client.recv(1024).decode("utf8")
    client.send(bytes(name + " est en ligne!", "utf8"))
    msg = "%s a rejoint le chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name  # stocke le nom du client dans le dictionnaire des noms (clients)

    while True:
        # boucle de communication infinie
        msg = client.recv(1024)  # rrecevoir un message du client
        """si un Message ne contient pas d'instructions de sortie, nous transmettons simplement
         le Message aux autres clients connectés"""
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + "")
        else:   # Message avec instruction de sortie
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s A quitté le tchat" % name, "utf8"))
            break
           


"""Si nous trouvons un message avec des instructions de sortie (c'est-à-dire que le client envoie un {exit}),
on répète le même Message au client (cela déclenche une action de fermeture côté client)
et fermez la prise de connexion pour cela"""


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Envoie le message à tous les clients connectés."""
    """Nous passons un préfixe à broadcast() dans notre poignée de fonction client(), 
    nous le faisons pour que les gens puissent voir exactement qui est l'expéditeur d'un message spécifique"""

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


"Définition des constantes"
clients = {}    # Dictionnaire chargé de stocker les clients
adresses = {}  # Dictionnaire responsable du stockage des adresses

"""Création du nom d'hôte (celui qui recevra les requêtes du client)"""
HOST = "127.0.0.1"
#HOST = "192.168.1.108"
"""Réglage du numéro de port"""
PORT = 50000

ADDR = (HOST, PORT)     # Constante qui stocke mon adresse et mon numéro de port

"""
Création d'un objet socket:
Où la première constante (AF_INET) représente la famille d'adresses,
la seconde constante représente un SOCKET STREAM ou un DATAGRAM (socket.SOCK_DGRAM),
une troisième valeur facultative peut être transmise en tant qu'attribut de l'objet SOCKET, le protocole, dans lequel
la valeur par défaut est 0.
L'attribut AF_INET indique qu'il s'agit d'un protocole d'adresse IP
L'attribut SOCKET_STREAM qui a été passé indique qu'il s'agit d'un protocole de transfert TCP
La combinaison des deux attributs indique qu'un serveur de type TCP/IP est en cours de création
"""
SERVER = socket(AF_INET, SOCK_STREAM)

"""Après avoir créé le serveur via un socket, l'objet doit être lié à un
adresse et numéro de port"""
SERVER.bind(ADDR)

"""Démarrage du serveur et acceptation des requêtes"""
if __name__ == "__main__":
    SERVER.listen(5)
    print("attente de la connexion...")
    ACCEPT_THREAD = Thread(target=accept_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()
