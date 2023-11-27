
with open('data2','a+') as f:
    # already some data is there in data2
    f.write("\nnew data added ")
    f.seek(0)
    print(f.read())
f.close()