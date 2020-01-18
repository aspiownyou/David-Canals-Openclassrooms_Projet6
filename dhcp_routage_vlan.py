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

#Creation des sub-interfaces
tn.write(b"enable\n")
tn.write(b"cisco\n") # Le mot de passe enable
tn.write(b"conf t\n")
tn.write(b"int fa0/0.11\n")
tn.write(b"encapsulation dot1Q 11\n")
tn.write(b"ip address 192.168.11.254 255.255.255.0\n")
tn.write(b"exit\n")
tn.write(b"int fa0/0.12\n")
tn.write(b"encapsulation dot1Q 12\n")
tn.write(b"ip address 192.168.12.254 255.255.255.0\n")
tn.write(b"exit\n")

#Configuration des pools d'adresse DHCP 11 et 12 sur le routeur
tn.write(b"ip dhcp pool 11\n")
tn.write(b"network 192.168.11.0\n")
tn.write(b"default-router 192.168.11.254\n")
tn.write(b"exit\n")
tn.write(b"ip dhcp pool 12\n")
tn.write(b"network 192.168.12.0\n")
tn.write(b"default-router 192.168.12.254\n")
tn.write(b"exit\n")

#Exclusion des adresses IP réservées aux sous interfaces
tn.write(b"ip dhcp excluded-address 192.168.11.254\n")
tn.write(b"ip dhcp excluded-address 192.168.12.254\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
print(tn.read_all().decode("ascii")) # Les commandes Cisco s'affichent à l'écran
print("sub interfaces et DHCP configurés")


