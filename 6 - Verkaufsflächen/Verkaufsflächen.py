Etages = [1]

def main():
    display_data()

def display_data():
    for i in Etages:
        print ("Verkaufsflächen Etage {}".format(i))
        print ("-----------------------")
        for x in range(12,42):
            print("Verkaufsfläche 1.{}".format(x))
    
main()
