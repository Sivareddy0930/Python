
with open('MyImage.jpg','rb') as f:
    print(f.read())
f.close()

print("--------------------------------------------")

with open('MyImage.jpg','rb') as f:
    for i in f:
        print(i)
f.close()

# the first approach reads the entire file content and prints it as a single byte string,
# while the second approach iterates over the file content in chunks and prints each chunk (line) separately.