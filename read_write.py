fout = open("test.txt","w")
fout.write("Hello Kiet\n")
fout.write("Hello Kiet\n")
fout.close()

fin = open("test.txt","r")
# str = fin.read() -> đọc full
str = fin.read(7) #-> đọc sô byte
print(str)
print(fin.name)
fin.close()