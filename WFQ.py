#Queue in Python
#Alex Meador
#CS 162
#Input packets as a string, S=Stard, P=Priority, E=Economy
input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen", \
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",\
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",\
                 "E Sue"]

p_queue = []
s_queue = []
e_queue = []

for packet in input_packets:
    if packet.startswith("P"):
        p_queue.append(packet)
    elif packet.startswith("S"):
        s_queue.append(packet)
    elif packet.startswith("E"):
        e_queue.append(packet)

print("Weighted Fair Queuing order:\n")
while p_queue or s_queue or e_queue:
    for _ in range(3):
        if p_queue:
            print(p_queue.pop(0))
    for _ in range(2):
        if s_queue:
            print(s_queue.pop(0))
    for _ in range(1):
        if e_queue:
            print(e_queue.pop(0))
