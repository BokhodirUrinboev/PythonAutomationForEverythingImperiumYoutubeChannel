import random

def creat_file():
    readFile = open('inputFile.txt', 'r')
    writeFile = open('creatFile.txt', 'w')

    for line in readFile:
        score = random.randint(0,100)
        if score >= 55:
            writeFile.writelines(line.rstrip() + "   " +  str(score) + "   Pass \n")
        else: 
            writeFile.writelines(line.rstrip() + "   " +  str(score) + "   Fail \n")
    readFile.close()
    writeFile.close()
# creat_file()

def read_file():
    readFile = open('creatFile.txt', 'r')
    for line in readFile:
        line_split = line.split()
        if line_split[2] == 'Fail':
            print(line)
    readFile.close()

read_file()