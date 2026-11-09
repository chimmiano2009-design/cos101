number_1=int(input("Enter a number greater than 1 or click 5 to exit:"))
print(f"THIS IS A MULTIPLICATION TABLE FOR {number_1}")
for number_2 in range (1,13):
    result= number_1 * number_2
    print(f"{number_1}*{number_2}={result}")
    if number_1 >= 1:
        print("Success")
        else:
        print("Input another number")
        
