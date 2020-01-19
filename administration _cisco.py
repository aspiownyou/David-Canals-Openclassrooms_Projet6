#!/usr/bin/python3
# Importation des librairies nécessaires
import os
import subprocess
# Le module os permet une interraction avec le système d'exploitation
# le module subprocess permet l'exécution d'autre fichier Python à partir de celui-ci

print("Configuration de matériels Cisco")

menu_principal = """  
\t1: Switch
\t2: Routeur
\t3: Fin du Programme
"""

choix = "0"
while choix != "3":
    choix = input(menu_principal)
    if choix == "1": # Menu de la catégorie switch
        switch = """
        \t1: Configuration des vlans                       
        \t2: Configuration des ports
        \t3: Exit
        """
        choix_switch = "0"
        while choix_switch != "3": # Execution des scripts 
            choix_switch = input(switch)
            if choix_switch == "1":
                subprocess.call(["/usr/bin/python3", "/home/david/Documents/Python_Scripts/vlan.py"]) 
            elif choix_switch == "2":
                subprocess.call(["/usr/bin/python3", "/home/david/Documents/Python_Scripts/port_switch.py"])
            else:
                print("Retour au menu principal")
            
            
    elif choix == "2": # Menu de la catégorie router
        router = """
        \t1: Configuration du DHCP et du routage inter-vlan
        \t2: Configuration du routage statique
        \t3: Exit
        """
        choix_router = input(router)
        while choix != "3": # execution des scripts
            if choix_router == "1":
                subprocess.call(["/usr/bin/python3", "/home/david/Documents/Python_Scripts/dhcp_routage_vlan.py"])
            elif choix_router == "2":
                subprocess.call(["/usr/bin/python3", "/home/david/Documents/Python_Scripts/"])
            else:
                print("Retour au menu principal")
            

    else:
        print("fin de programme")
