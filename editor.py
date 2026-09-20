
l=[]
def write():
    print("enter your text :")
    while True:
        line=input()
        if line==":q":
            break
        
            return
        l.append(line)
def read():
    for i in l:
        print(i)
    return
def search():
    val=input("enter the text u wanna search for :")
    for i in l:
        if val in i:
            print("line :",l.index(i)+1," ",i)
    return

while True:
    choice=int(input("""Your Text Editor :\nChoose 1 to enter Text :
                     Choose 2 to see the text :
                     Choose 3 to search a word :
                     choose 4 to exit the editor :"""))
    match choice:
        case 1:
            write()
        case 2:
            read()
        case 3:
            search()
        case 4 :
            exit()