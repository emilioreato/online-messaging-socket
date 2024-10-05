from firewall import FirewallRules
import online_tools
from portforwarding import Portforwarding
import time
import os
import threading

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # sets the current directory to the file's directory

port = 8050


with open('rules.txt', 'r') as archivo:  # Small code that creates a firewall rule if it has not been created yet. the state of the creation is saved on rules.txt
    if not "yes" in archivo.read():
        print("creating")
        FirewallRules.get_admin_permitions()
        rule_name = "GambitGameRule"
        if not FirewallRules.rule_exists(rule_name):
            FirewallRules.add_firewall_rule(port, rule_name + "Inbound", "Inbound")
            FirewallRules.add_firewall_rule(port, rule_name + "Outbound", "Outbound")
        with open('rules.txt', 'w') as archivo:
            archivo.write('yes')
    else:
        print("already")


time.sleep(2)
local_ip = online_tools.Online.get_local_ip()
print(local_ip)

Portforwarding.initialize()
if not Portforwarding.check_ports(port):
    Portforwarding.open_port(local_ip, port, port, "TCP")


choice = input("Unirse a partida(1) o crear una partida(2):").strip()
if (choice == "1"):
    sckt = online_tools.Client()
    ip = input("Ingrese la clave de la partida:").strip()
    sckt.set_up_client(ip, port)
else:
    sckt = online_tools.Server()
    print("La clave de tu partida es:", online_tools.Online.get_public_ip())
    sckt.set_up_server(port)
    # while (True):
    #    print("inloop")
    #    if sckt.recieve():
    #        break
    #    time.sleep(0.1)
run = True
msg = ""
msg_ant = " "


def get_input():
    global msg
    while True:
        msg = input("Escribe un mensaje para enviar:").strip()
        if msg == "exit":
            global run
            run = False


def receive_messages():
    while True:
        guest_msg = sckt.recieve()  # Recibir mensajes
        if guest_msg:
            print("Guest:", guest_msg)


# Hilos para entrada y recepción
threading.Thread(target=get_input, daemon=True).start()
threading.Thread(target=receive_messages, daemon=True).start()


sckt.send("Conexion establecida")

while run:
    if msg != msg_ant:
        msg_ant = msg
        sckt.send(msg)
    if msg == "exit":
        break


if (choice == "2"):
    sckt.close()
Portforwarding.close_port(port)
