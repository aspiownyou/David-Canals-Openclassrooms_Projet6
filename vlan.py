import getpass
import telnetlib

host = "192.168.10.253" # Adresse Ip du Switch
user = input("Entrez votre identifiant Telnet:")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Username:")
tn.write(user.encode("ascii")+ b"\n")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode("ascii")+ b"\n")

# Commandes Cisco pour la création des Vlans
tn.write(b"enable\n")
tn.write(b"cisco\n") # Le mot de passe enable
tn.write(b"conf t\n")
tn.write(b"vlan 11\n")
tn.write(b"name Direction\n")
tn.write(b"vlan 12\n")
tn.write(b"name Ress.Hum\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii")) # Les commandes Cisco s'affichent à l'écran
print("les Vlans ont été configurés")




