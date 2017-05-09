import random
def main():

    num1 = roll()
    print num1

    choice = raw_input("Would you like another number? (y/n): ")

    while (choice == 'y'):
        num2 = roll()
        print num2
        choice = raw_input("Would you like another number? (y/n): ")
    else:
        print "goodbye"
        

def roll():
    num = random.randint(1,6)
    return num

main()
