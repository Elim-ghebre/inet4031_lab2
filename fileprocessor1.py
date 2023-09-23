with open("fileprocessor.input", 'r') as file:
    lines = file.readlines()

print("Printing out User Data:\n")

for line in lines:
    line = line.strip()  # Removing leading and trailing whitespaces

    if line.startswith("#"):
        user = line.split(":")[0][1:]  # Remove the '#' and get the username
        print(user, "is skipped because it starts with a hashtag (is commented out)")
    else:
        parts = line.split(":")

        if len(parts) == 4:
            print("The user", parts[0], "has a password of", parts[1], "and has userid", parts[2], "and groupid", parts[3])

print("\nEnd of User Data")
