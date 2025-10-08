numbers = range(45, 211)
for number in numbers:  
    if number == 100:
        continue  # Skip the number 100
    if number == 205:
        break  # break the loop at 205
    print(number)


while True:
    answer:str = input("what is the product of 7 * 24 ? ")

    if answer.isdigit():
        answer = int(answer)

        if answer == 7 * 24:
            print("You answered this Question correctly")
            break # the answer is right exit the loop

        else:
            print("Your Answer is wrong try again..")