import getpass
import telnetlib

host = "192.168.10.254" # Adresse Ip du Routeur
user = input("Entrez votre identifiant Telnet:")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until(b"Username:")
tn.write(user.encode("ascii")+ b"\n")
if password:
    tn.read_until(b"Password:")
    tn.write(password.encode("ascii")+ b"\n")

# Création d'une route statique entre le Router et l"extérieur pour permettre aux postes d'accéder à Internet
tn.write(b"enable\n")
tn.write(b"cisco\n") # Le mot de passe enable
tn.write(b"conf t\n")
tn.write(b"ip route 0.0.0.0 0.0.0.0 192.168.37.2\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii")) # Les commandes Cisco s'affichent à l'écran
print("routage statique configuré")
