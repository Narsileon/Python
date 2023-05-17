start_number = 1;
end_number = 100;
sum_number = 0;

def main():
    print("Summe:")
    get_data()
    print("- Summe beträgt: {}".format(sum_number))
    
def get_data():
    global start_number, end_number
    
    start_number = int(input("- Start number:"))
    end_number = int(input("- End number:"))
    calculate_sum()

#Anfänger Aufgabe (for loop)
def calculate_sum():
    global sum_number    
    
    for i in range(start_number, end_number + 1):
        sum_number += i
        
#Anfänger Aufgabe (math)
def calculate_sum_alternative():
    global sum_number    
    
    sum_number = (end_number * (end_number + 1) - start_number * (start_number - 1)) / 2
    
#Fortgeschrittene Aufgabe
def calculate_sum_advanced():
    global sum_number
     
    for i in range(start_number, end_number + 1):
        if (i % 2 == 0 and i % 4 != 0):
            sum_number += i
            
            if (sum_number > 50):
                print("Summe größer 50")
                exit();

main()
