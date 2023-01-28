iteration_var = 0
code = ""
count = 0
while iteration_var < 1:
    code_inp = input("Enter a single digit: ")  # change to mouse click
    code += code_inp
    print(f"Code: {code}")
    count += 1
    if count >= 4 and code != "1234":
        print("Wrong")
        count = 0
        code = ""
    elif code == "1234":
        print("Correct")
        iteration_var += 1
    else:
        continue