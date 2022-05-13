#Gamer part 2
def typeOut(message: str, speed: float = 0.000001):
    print(end="\n")
    i = 0
    u = 0
    while u < len(message):
        i += speed
        if int(i) > 1:
            i = 0
            print(message[u], end="")
            u += 1
    del i, u


typeOut("This is a test program")
typeOut("We are using pygame now")

while True:
    s = input("\nEnter something to type out. Type 'end' to end: ")
    if s.lower() == "end":
        print("Stopping program")
        break
    typeOut("[You]: "+ s)
    del s
