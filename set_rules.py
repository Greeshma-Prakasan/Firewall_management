import os
from rich.console import Console
console = Console()

def rule_menu():
    console.print("\t1. Allow the host/IP\n\t2. Block the host/IP\n\t3. Allow a subnet\n\t4. Block a subnet\n\t5. Allow Port\n\t6. Block Port\n\t7. Allow Protocol\n\t8. Exit",style="bold yellow")

def allow(ip):
    res = os.popen(f"sudo ufw allow from {ip}").read()
    console.print(f"\t{res}",style="bold magenta")

def block(ip):
    res = os.popen(f"sudo ufw deny from {ip}").read()
    console.print(f"\t{res}",style="bold magenta")

def allow_port():
    port = input("\tEnter the port : ")
    res = os.popen(f"sudo ufw allow {port}").read()
    console.print(f"\t{res}",style="bold magenta")

def block_port():
    port = input("\tEnter the port : ")
    res = os.popen(f"sudo ufw deny {port}").read()
    console.print(f"\t{res}",style="bold magenta")

def allow_proto():
    prot = input("\tEnter the protocol : ")
    port = input("\tEnter the port : ")
    res = os.popen(f"sudo ufw allow in from any to any proto {prot} port {port}").read()
    console.print(f"\t{res}",style="bold magenta")

def set_rules():
    while True:
        rule_menu()
        c = int(input("\tEnter the choice : "))
        if c==1:
            ip = input("\tEnter the IP : ")
            allow(ip)
        elif c==2:
            ip = input("\tEnter the IP : ")
            block(ip)
        elif c==3:
            sub = input("\tEnter the subnet : ")
            allow(sub)
        elif c==4:
            sub = input("\tEnter the subnet : ")
            block(sub)
        elif c==5:
            allow_port()
        elif c==6:
            block_port()
        elif c==7:
            allow_proto()
        elif c==8:
            break  
        else:
            console.print("\tInvalid Choice",style="bold red") 
