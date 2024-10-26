numdays = int(input("How many days temperature ? \n"))
total = 0
temp = []
for day in range(numdays):
    nextDay = int(input(f"Days {day+1}'s high temp: "))
    temp.append(nextDay)
    total += temp[day]
average = round(total/numdays)
print(f"Average = {float(average)}")

above = 0
for i,value in enumerate(temp):
    if value > average:
        print(f"Day.{i} is above average")
        above += 1
print(f"Total : {above} days has extreme hot temperature out of {numdays} days ")