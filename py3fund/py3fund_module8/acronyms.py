look_up = input("What software acronyms do you want to look up?")

found = False

try:
    with open("acronyms.txt", "r") as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
except FileNotFoundError as ex:
    pass

if not found:
    print("Acronym not found. Please share the definition with us.")
    definition = input("Enter the definition: ")
    with open("acronyms.txt", "a") as file:
        file.write(f"{look_up} - {definition}\n")
        print("Acronym added to the file.")


