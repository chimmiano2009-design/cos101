number=int(input("Enter a number:"))
print(f"MULTIPLICATION TABLE FOR {number}")
for multiplier in range (1,14):
    result= number* multiplier
    print(f"{number}*{multiplier}={result}")
