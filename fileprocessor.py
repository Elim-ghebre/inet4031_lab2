file = open("fileprocessor.input", 'r')
lines = file.readlines()
file.close()

print("Printing out User Data:\n")

for line in lines:
    line = line.strip()

    if line[0] == "#":
        print(line[1:], "is skipped because it starts with a hashtag (is commented out)")
    else:
        parts = line.split(":")
        print("The user", parts[0], "has a password of", parts[1], "and has userid", parts[2], "and groupid", parts[3])

print("\nEnd of User Data")
