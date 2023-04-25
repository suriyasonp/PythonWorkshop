# Write File

# Append file
file = open("textFile.txt", "a")

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
file.write(text)


file = open("textFile.txt", "r")
print(file.read())