from prompt_toolkit.shortcuts.prompt import prompt
import json
import requests
from extra.displaylist import Logo, Main_menu, Menu
from extra.for_inp import formaturl, is_ip, screen_clear, take
from data.data import HEADERS, Log
from datetime import datetime, time
from os import system
from extra.respond import proceed
Target=None

'''
do 
combain
search
target
val
show 
print
'''

def main():
    while True:
        try:
            x=take("Nemo ")
            Log.append("[+] "+x)
            if x.lower() in ["menu","!!"]:
                print(Menu)
            elif x.lower() in ["help","!"]:
                print(Main_menu)
            elif x.lower() in ["log","||"]:
                for i in Log:
                    print(i)
                print(" ")
                l=prompt("Would you like to print log (y/n) ")
                if l.lower() == "y":
                    log_print() 
            elif x.lower() in ["clear","cls","-="]:
                screen_clear()
            else:
                x=x.split(" ")
                organize(x)
        except KeyboardInterrupt:
            print("Exiting the instance")
            quit(0)
        except IndexError:
         print("Missing Values < May be target is not present>")
   # except:print("Error [404]")


def organize(x):
    global Target
    if x[0].lower() in ["do","run","@"]:
        proceed(str(x[1]),Target)
    elif x[0].lower() in ["combine","mix","#"]:
        k=x[1]
        k=k.split(",")
        for i in k:
            proceed(str(i),Target)
    elif x[0].lower() in ["target","set","*"]:
        Target = x[1]
    elif x[0].lower() in ["val","valuate","?"]:
        val_it()
   
    elif x[0].lower() in ["show","`"]:
        show(x[1])


def val_it():
    if is_ip(Target):
        if True if system("ping -c 1 " + Target) == 0 else False:
            print(f" {Target} is alive")
        else:
            print(f" {Target} is not accessable")

    else:
        r=requests.get(formaturl(Target),headers=HEADERS,timeout=60)
        if r.status_code == 200:
            print(f" {Target} is alive")
        else:
            print(f" {Target} is not accessable")

def search_it():
    pass

def show(x):
    if x in ["target","*"]:
        print(f" Target set to : {Target}")



def log_print():
    with open(f"log.nemo","wt") as f:
        for i in Log:
            f.write(i+"\n")


if __name__ == "__main__": 
    screen_clear()
    print(Logo,"\n")
    main()