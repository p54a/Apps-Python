# Mark counter app
#input (Do you want me to count your total mark? )
#list []
#If yes 



while True:
    ask = input("Do you want me to count your total mark? ")
    ask = ask.lower()
    
    if ask == "yes":
        marks = []
        break
    elif ask == "no":
        print("Thanks, for visiting my app.")
        exit()
    else:
        print("Pleasee type either yes or no.")
        continue
    

while True:
    mark = input("Please type your mark (one by one): ")
    
    isnumber = mark.isnumeric()
    isalpha = mark.isalpha()
    
    if isnumber:
        mark = int(mark)
        marks.append(mark)
    elif isalpha:
        break
    elif not isnumber and not isalpha:
        try:
            mark = float(mark)
        except ValueError:
            break
        marks.append(mark)

numberOfMarks = len(marks)
markTotal = 0
x = 1

for mark in marks:
    print("Mark numeber", x, "is " + str(mark))
    markTotal += mark
    x += 1

markTotal = markTotal / numberOfMarks

if markTotal >= 90 and markTotal <=100:
    heIs = "Very Good"
elif markTotal >= 80:
    heIs = "Good"
elif markTotal >=60:
    heIs = "Passed"
elif markTotal < 60 and markTotal > 0:
    heIs = "Failed"
else:
    raise ValueError("Please enter your marks correctly.")

while True:
    check = input("Is that correct: ")
    check = check.lower()

    if check == "yes":
        print("Your Total marks is " + str(round(markTotal, 2)) + ", and you are " + heIs)
        break
    elif check == "no":
        print("Please type it again correctly.")
        break
    else:
        print("Please type either yes or no.")
        continue