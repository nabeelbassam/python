# Compute minimum of a list using threads
import random
import threading

mylist = [random.randint(1, 100000000) for i in range(1000000)]
mins = []

def calc_min(li):
    minimum = li[0]
    for x in li:
        if x < minimum:
            minimum = x

    mins.append(minimum)

# Dividing list in halves
l1 = mylist[:len(mylist)//2]
l2 = mylist[len(mylist)//2:]

# Dividing list in quaters
q1 = l1[:len(l1)//2]
q2 = l1[len(l1)//2:]
q3 = l2[:len(l2)//2]
q4 = l2[len(l2)//2:]

workers = []

workers.append( threading.Thread(target=calc_min(q1)) )
workers.append( threading.Thread(target=calc_min(q2)) )
workers.append( threading.Thread(target=calc_min(q3)) )
workers.append( threading.Thread(target=calc_min(q4)) )

for worker in workers:
    worker.start()
for worker in workers:
    worker.join()

print("global minimum: ", min(mins))
