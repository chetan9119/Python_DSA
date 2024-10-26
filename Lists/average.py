# Calulate average from the input 

def average_cal():
    value_list = []
    while True:
        value = input("Enter Number: ")
        if value == 'done':
            break
        value_list.append(int(value))
    average = sum(value_list) / len(value_list)
    print(f"The average of given numbers is : {float(average)}")
    
average_cal()