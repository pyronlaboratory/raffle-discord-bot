import sys
sys.path.insert(0, r"C:\Users\AYUSH\Desktop\Ronnie\python\discord-raffle-bot\raffle_server\raffle_form\scripts") # update address on production server

import tresbien
#import afewstore
#import jdsports


def raffle(**data):
        for key, value in data.items():
                if key == "raffle" and value == "tresbien":
                        print("Initiate tresbien.py")
                        tresbien.main(tresbien=data)
                if key == "raffe" and value == "afewstore":
                        print("Initiate afewstore.py")
                        afewstore.main(afewstore=data)
                if key == "raffe" and value == "jdsports":
                        print("Initiate jdsports.py")
                        jdsports.main(jdsports=data)


