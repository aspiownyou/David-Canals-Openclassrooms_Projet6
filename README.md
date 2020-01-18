# Python: automatisation de configurations Cisco

<a href="https://www.casimages.com/i/20011805252325065016607769.png.html" target="_blank" title="Mon image"><img src="https://nsm09.casimages.com/img/2020/01/18//20011805252325065016607769.png" border="0" alt="Mon image" /></a>

Le but ce ce projet est d'automatiser des configurations sur du matériel Cisco avec Python et le protocole Telnet: 
* La créations automatique de Vlans et d'assignations de ports pour le Switch.
* La mise en place d'un rôle DHCP et du routage statique pour le Routeur. 

Pour ce faire on dispose de plusieurs scripts: 
* Le script principal administration_cisco.py demande dans un premier temps à l'utilisateur de choisir entre le Switch et le Routeur. Puis dans un deuxième temps une liste de tâches automatique lui sera proposé.
* Le script vlan.py va automatiquement créer 2 vlans: un vlan 11 pour le directeur et un vlan 12 pour une employés des Ressources Humaines.
* Le script port_switch.py va affecter deux ports aux vlans créer précédemment et configurer deux autres ports en mode trunk.
* Le script dhcp_routage_vlan.py va créer deux subinterfaces qui feront office de gateway pour chaque vlan ainsi que l'ajout d'un rôle DHCCP pour le Routeur.
* Le script routage_statique.py va créer un routage statique simple entre notre LAN et Internet


## Prérequis

* Un poste ou une machine virtuelle sous Linux disposant d'une version récente de Python version 3. Pour la rédaction des scripts Python on a utilisé le logiciel Visual Studio Code.
* Configurer une connexion Telnet pour permettre l'administration du Switch et du Routeur à distance.
* Une connaissance des commandes CLI Cisco.
* Les modules nécessaires pour le fonctionnement de l'ensemble des scripts sont les modules OS, Telnelib, Getpass et Subprocess. 



## Quelques remarques et précisions pour les scripts

* Pour notre exemple on a pris comme nom d'utilisateur et mot de passe "cisco" (sans les guillemets)
* Chaque commande cisco est précédé par la lettre b et se finit par \n . Le b permet de simuler une commande entrer manuellement, le \n simule la validation de la commande avec la touche entrée.
* Ne pas oublier de faire un chmod 700 sur chaque scripts pour qu'ils puissent être executer sur le terminal.



