import django_rq

# raffle scripts

from .scripts import tresbien
from .scripts import afewstore
from .scripts import jdsports
from .scripts import shinzoparis
from .scripts import chmielna20

q = django_rq.get_queue('default')

def raffle(**data):

        for key, value in data.items():
                if key == "raffle" and value == "tresbien":
                        print("Initiate tresbien.py")
                        #q1 = django_rq.get_queue('default')
                        #print(q1)
                        tresbien_job = q.enqueue(tresbien.main, tresbien=data)
                        #print(get_status(tresbien_job))
                        
                if key == "raffle" and value == "afewstore":
                        print("Initiate afewstore.py")
                        #q2 = django_rq.get_queue('default')
                        #print(q2)
                        afewstore_job = q.enqueue(afewstore.main, afewstore=data)
                        #print(get_status(afewstore_job))

                if key == "raffle" and value == "jdsports":
                        print("Initiate jdsports.py")
                        #q3 = django_rq.get_queue('default')
                        #print(q3)
                        jdsports_job = q.enqueue(jdsports.main, jdsports=data)
                        #print(get_status(jdsports_job))

                if key == "raffle" and value == "shinzoparis":
                        print("Initiate shinzoparis.py")
                        #q4 = django_rq.get_queue('default')
                        #print(q4)
                        shinzoparis_job = q.enqueue(shinzoparis.main, shinzoparis=data)
                        #print(get_status(shinzoparis_job))

                if key == "raffle" and value == "chmielna20":
                        print("Initiate chmielna20.py")
                        #q5 = django_rq.get_queue('default')
                        #print(q5)
                        chmielna20_job = q.enqueue(chmielna20.main, chmielna20=data)
                        #print(get_status(chmielna20_job))