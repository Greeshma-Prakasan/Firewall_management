import os
from rich.console import Console
import set_rules as rules


console = Console()

def get_status():
    stat = os.popen("sudo ufw status").read()
    console.print(stat,style="bold magenta")


def delete_rules():
    res = os.popen("sudo ufw status numbered").read()
    console.print(res,style="bold magenta")
    ind = input("Enter the index to delete : ")
    res = os.popen(f"sudo ufw delete {ind}").read()
    console.print(res,style="bold magenta")


def reload_rules():
    res = os.popen("sudo ufw reload").read()
    console.print(res,style="bold magenta")

def menu():
    console.print("1. Status of Firewall\n2. Set Rules\n3. Delete Rules\n4. Reload the rules\n5. Exit",style="bold blue")

while True:
    menu()
    c = int(input("Enter the choice : "))
    if c==1:
        get_status()
    elif c==2:
        rules.set_rules()
    elif c==3:
        delete_rules()
    elif c==4:
        reload_rules()
    elif c==5:
        break
    else:
        console.print("Invalid Choice",style="bold red")