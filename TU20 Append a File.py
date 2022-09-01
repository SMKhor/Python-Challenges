with open("counter.txt", "r") as existing_file:
    for line in existing_file:
        for word in line.split():
            num = word

with open("counter.txt","a") as existing_file:
    num = int(num) + 1
    for i in range(num-1,(num+9)):
        line_to_write = str(num)+"\n"
        num = num + 1
        existing_file.write(line_to_write)
