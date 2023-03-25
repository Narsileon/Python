MAX_VALUE = 350

lucky_numbers = []

def main():
    get_number()
    remove_even_numbers()
    remove_numbers_by_step()
    display_lucky_numbers()

def get_number():
    for x in range (1, MAX_VALUE):
        lucky_numbers.append(x)

def remove_even_numbers():
    delete_unlucky_numbers(1,2)

def remove_numbers_by_step():
    index = 1 
    step = int(lucky_numbers[index])
    
    while step < len(lucky_numbers):
        delete_unlucky_numbers(step - 1, step)
        
        index += 1
        step = int(lucky_numbers[index])

def display_lucky_numbers():
    print(lucky_numbers)

def delete_unlucky_numbers(start, step):
    del lucky_numbers[start::step]

main()
