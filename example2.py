user=input("enter user")
password=input("enter password")
if user=="seed" or password=="it":
    ch=int(input("enter 1 to add 10 Question \n 2 Pass \n 3 fail \n 4 Topper"))
    if ch==1:
        f=open("exam.txt","w")
        for i in range(1,10):
            question=input("Enter Question ")
            option1=input("enter option1")
            option2=input("enter option2")
            option3=input("enter option3")
            option4=input("enter option4")
            answer=input("enter answer")
            f.write(question+","+str(option1)+","+str(option2)+","+str(option3)+","+str(option4)+","+str(answer)+","+"\n")

        f.close()
    if ch==2:
        f=open("result.txt","r")
        for line in f:
            z=line.split(",")
            if int(z[4])>6:
                print(line)
        f.close()


    if ch==3:
        f=open("result.txt","r")
        for line in f:
            z=line.split(",")
            if int(z[4])<3:
                print(line)
        f.close()

    if ch==4:
        m=0
        d=""
        f=open("result.txt","r")
        for line in f:
            z=line.split(",")
            if int(z[4])>m:
                m=int(z[4])
                d=line
        print(m)
        print(d)
        f.close()