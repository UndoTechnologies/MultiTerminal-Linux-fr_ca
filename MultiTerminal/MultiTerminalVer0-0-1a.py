#MultiTerminal par UndoTechnologies/Brennan LeBlanc
#Copyright 2019 par Brennan LeBlanc et Undo Technologies
#Sur license de GNU General Public License 3.0

import sys
import os
import time
import getpass

print("MultiTerminal - Crée par Undo Technologies")
time.sleep(1)
print('MultiTerminal: Bienvenue à MultiTerminal! Faire sur que cette programme est ouvert avec les permission de "SuperUser (su)" ou de "sudo".')
time.sleep(3)

helplist = 'aide', 'Aide', 'AIDE', '?'
verify = 'verifier', 'verifie', 'vérifier', 'verifié', 'vérifié', 'vérifie'
danger_list = "sudo format disk0", "format disk0", "del C:\Windows\System32\*.*"
continue_y = 'oui', 'Oui', 'OUI', 'o', 'O', 'y', 'Y'
end = "fermer", "Fermer", "FERMER"
version = "Version", "version", "VERSION", "ver", "Ver", "VER"

message = input("MultiTerminal: Qu'est-ce que tu veux faire aujourd'hui? > ")

if message in helplist:
    print('MultiTerminal: Vos options sont:')
    print('MultiTerminal: Vérifier - Faire sur que ton programme est sauf pour ton ordinateur')
    print('MultiTerminal: Analyser - Analyser des fichiers *Pas fonctionelle encore*')
    print("MultiTerminal: Fermer - Fermer MultiTerminal")
    print("MultiTerminal: Version - Donner la version du MultiTerminal")
    print('MultiTerminal: Et plus à venir...')
    print("MultiTerminal: La programme va redémmarer pour continuer.")
    input("MultiTerminal: Tapper le boutton d'entrée pour continuer...")
    os.system("sudo python3 MultiTerminalVer0-0-1a.py")
else:
    if message in verify:
        command = input("MultiTerminal: C'est quoi ton commande? > ")
        if command in danger_list:
            print("MultiTerminal: Cette commande est malveillent et peut causer des problèmes dessus ton ordinateur. Nous vous conseillons de ne pas utiliser cette commande pour la sécurité de ton ordinateur!")
            time.sleep(2)
            continue1 = input("MultiTerminal: Veux-tu faire d'autre choses aujourd'hui? > ")
            if continue1 in continue_y:
                print("MultiTerminal: OK, la programme va redémmarer maintenant!")
                time.sleep(3)
                os.system("sudo python3 MultiTerminalVer0-0-1a.py")
            else:
                print("MultiTerminal: OK, bonne journée!")
        else:
            print("MultiTerminal: Cette programme est saufe pour ton ordinateur! Si vous encore n'êtes pas sûr si cette commande est 100% sauf, tu n'as pas besoin d'exécuter.")
            run = input("MultiTerminal: Veux-tu qu'on exécute cette commande? > ")
            if run in continue_y:
                print("MultiTerminal: OK, on va faire ça maintenant!")
                time.sleep(3)
                os.system(command)
                continue3 = input("MultiTerminal: Veux-tu faire d'autre choses aujourd'hui? > ")
                if continue3 in continue_y:
                    print("MultiTerminal: OK, la programme va redémmarer maintenant!")
                    time.sleep(3)
                    os.system("sudo python3 MultiTerminalVer0-0-1a.py")
                else:
                    print("MultiTerminal: OK, bonne journée!")
            else:
                print("MultiTerminal: OK, on ne va pas exécuter cette commande.")
                continue2 = input("MultiTerminal: Veux-tu faire d'autre choses aujours'hui? > ")
                if continue2 in continue_y:
                    print("MultiTerminal: OK, la programme va redémmarer maintenant!")
                    time.sleep(3)
                    os.system("sudo python3 MultiTerminalVer0-0-1a.py")
                else:
                    print("MultiTerminal: OK, bonne journée!")
    else:
        if message in end:
            print("MultiTerminal: OK, bonne journée!")
        else:
            if message in version:
                print("MultiTerminal: Version 0.0.1a par Undo Technologies/Brennan LeBlanc")
                time.sleep(3)
                print("MultiTerminal: La programme va redémmarer maintenant pour continuer.")
                time.sleep(3)
                os.system("sudo python3 MultiTerminalVer0-0-1a.py")
            else:
                print("MultiTerminal: Je m'excuse, je n'ai pas compris ça. La programme va maintenant redémmarer pour continuer.")
                os.system("sudo python3 MultiTerminalVer0-0-1a.py")
            
