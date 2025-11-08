filename = "sample.txt"
content = """This is a sample text file.
It contains multiple lines.
This text is written by the program."""

with open(filename, 'w') as file:
    file.write(content)

print(f"Content written to {filename}")
