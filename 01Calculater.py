import re
print ("Our Magical calculator")
print("type quit to exit")

previous = 0
run = True

def performMath():
    global run
    equ = input("enter equestion:")
    if equ == "quit":
        run = False
    else:
        print("you types",equ)

while run:
    performMath()
