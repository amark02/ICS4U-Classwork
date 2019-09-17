"""
Create a text file with word on a number of lines.
1. Open the text file and print out 'f.read()'. What does it look like?
2. Use a for loop to print out each line individually, 'for line in f:'
3. Print out only the words that start with 'm', or some other specific letter
"""
# 1
with open("random_text.txt", "r") as f:
    print(f.read())

# 2
with open("random_text.txt", "r") as f:
    for line in f:
        print(line.strip())

# 3
with open("random_text.txt", "r") as f:
    for line in f:
        if line.lower().startswith("m"):
            print(line.strip())
        