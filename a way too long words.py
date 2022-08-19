text = input(":")

if len(text) > 9:
    x = len(text)
    print(text[0], end="")
    print(x - 2, end="")
    print(text[-1])
    yes_or_no = input("do you want to show?")
    if yes_or_no == "yes":
        print(text)
else:
    print(text)



