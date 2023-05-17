VALUES = [6, 9, 4, 7, 8, 3, 5 ,1 ,2 ,0]

def main():
    global VALUES
    
    length = len(VALUES)
    
    for i in range (length):
        for j in range (length - i - 1):
            if VALUES[j] > VALUES[j + 1]:
                temp = VALUES[j]
                VALUES[j] = VALUES[j + 1]
                VALUES[j + 1] = temp
        
    print(VALUES)
            
main()