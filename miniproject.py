import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="anshika",database="gourmet")
mycursor = mydb.cursor()

def home():
    print("******WLECOME TO THE GOURMET******")
    print("1.ENTER THE CUSTOMER DATA \n2.LOGIN, \n3.EXIT")
    choice=int(input("Enter the choice"))
    if(choice==1):
        homecust()
    elif(choice==2):
        login()
    else:
        print("THANK YOU..PLEASE VISIT SOON:)")
        exit(0)
def homecust():
    L=[]
    print("******WELCOME TO THE GOURMET******")
    print("      ****sign in****      ")
    name=input("Enter the name:")
    L.append(name)
    password=input("Enter the password:")
    L.append(password)
    password1=input("Enter the pasword:")
    L.append(password1)
    phno=int(input("Enter mobile number:"))
    L.append(phno)
    email=input("Enter the email address:")
    L.append(email)
    gender=input("Enter your gender:")
    L.append(gender)
    guest_no=input("Enter the number of guest")
    L.append(guest_no)
    city=input("Enter the city name:")
    L.append(city)
    country=input("Enter the country name")
    L.append(country)
    check_in=input("Enter the checkin date")
    L.append(check_in)
    check_out=input("Enter the checkout date")
    L.append(check_out)
    cust=(L)
    print(cust)
    if(password==password1):
        sql="insert into signin(name,password,password1,phno,email,gender,guest_no,city,country,check_in,check_out)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        mycursor.execute(sql,cust)
        mydb.commit() 
        print("signin successful")
        login()
        #print("select any option to proceed")
        #print("1.accommodation 2.food items 3.payment")
        #choice=int(input("enter any option:"))
        #if(choice==1):
         #   accommodation()
        #elif(choice==2):
         #   food_items()    
        #else:    
         #   payment()
    else:
        print("Password does not match!!!\n Enter details again")
        homecust()
def login():
    mydb = mysql.connector.connect(host="localhost",user="root",password="anshika",database="gourmet")
    mycursor = mydb.cursor()
    print("  *****LOGIN*****   ")
    name1=input("Enter the name")
    password=input("Enter the password")
    #passwd=input("renter the password")
    mycursor.execute("select * from signin where name=%s AND password=%s",(name1,password))
    records=mycursor.fetchone()
    if records:
        if records[1]==password:
            print("login successful")
            print("select any option to proceed")
            print("1.accommodation 2.food items 3.travel")
            choice=int(input("enter any option"))
            if (choice==1):
                accommodation()
                
            elif (choice==2):
                food_items()
            elif (choice==3):
                travel()
            else:
                print("unsuccessful")
                home()
        else:
            print("password incorrect")
    else:
        print("record not found")
        home()
def accommodation():
    guest=int(input("Enter the number of guest:"))
    n=int(input("For How Many Nights Do You Stay:"))
    print("we have the following room for you:-")
    print("1. class A-------STANDARD NON-AC COST:1000 PER ROOM PER PERSON(MAX. 4 PEOPLE ALLOWED)")
    print("2.class B--------DOUBLE BED,TV, ESSIENTIALS COST:2000 PER ROOM PER PERSON(MAX. 4 PEOPLE ALLOWED")
    print("3. class C-------DOUBLE-DOOR CUPBOARD, FRIDGE, GARDEN VIEW,CUSHIONS COST:4000 PER ROOM PER PERSON(MAX. 4 PEOPLE ALLOWED)")
    print("4. class D-------STANDARD AC, WIFI, ROOM SERVICE,LAKE VIEW COST: 6000 PER ROOM PER PERSON(MAX. 4 PEOPLE ALLOWED)")
    room_type=int(input("enter the choice"))
    if(room_type==1):
        print("YOU HAVE CHOOSEN STANDARD NON-AC ROOM FOR YOUR STAY ")
        cost=1000*n*guest
        print("COST FOR YOUR STAY IS:"+str(cost))
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(room_type==2):
        print("YOU HAVE CHOOSEN DOUBLE BED,TV, ESSIENTIALS ROOM FOR YOUR STAY")
        cost=1000*n*guest
        print("COST FOR YOUR STAY IS:"+str(cost))
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(room_type==3):
        print("YOU HAVE CHOOSEN DOUBLE-DOOR CUPBOARD, FRIDGE, GARDEN VIEW,CUSHIONS")
        cost=1000*n*guest
        print("COST FOR YOUR STAY IS:"+str(cost))
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    else:
        print("YOU HAVE CHOOSEN STANDARD AC, WIFI, ROOM SERVICE,LAKE VIEW COST ROOM FOR YOUR STAY")
        cost=1000*n*guest
        print("COST FOR YOUR STAY IS:"+str(cost))
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    
def food_items():
    L=[]
    print("WHAT DO YOU WANT TO EAT")
    print("1.BREAKFAST \n 2.LUNCH \n3.SNACKS\n 4.DINNER\n")
    print("Select any three items:")
    choice=int(input("enter the choice"))
    if(choice==1):
        display_breakfast()
        print("enter your choice for breakfast:")
        item1=input("enter the first items:")
        L.append(item1)
        item2=input("enter the second items:")
        L.append(item2)
        item3=input("enter the third items:")
        L.append(item3)
        cust=(L)
        sql="insert into food_items(item1,item2,item3)values(%s,%s,%s);"
        mycursor.execute(sql,cust)
        mydb.commit() 
        
        print("successfully orderd")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(choice==2):
        display_lunch()
        print("enter your choice for lunch:")
        item1=input("enter the first items:")
        L.append(item1)
        item2=input("enter the second items:")
        L.append(item2)
        item3=input("enter the third items:")
        L.append(item3)
        cust=(L)
        sql="insert into food_items(item1,item2,item3)values(%s,%s,%s);"
        mycursor.execute(sql,cust)
        mydb.commit() 

        print("successfully orderd")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(choice==3):
        display_snacks()
        print("Enter your choice for snacks:")
        item1=input("Enter the first items:")
        L.append(item1)
        item2=input("Enter the second items:")
        L.append(item2)
        item3=input("Enter the third items:")
        L.append(item3)
        cust=(L)
        sql="insert into food_items(item1,item2,item3)values(%s,%s,%s);"
        mycursor.execute(sql,cust)
        mydb.commit() 
        print("successfully orderd")   
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    else:
        display_dinner()
        print("Enter your choice for dinner:")
        item1=input("Enter the first items:")
        L.append(item1)
        item2=input("Enter the second items:")
        L.append(item2)
        item3=input("Enter the third items:")
        L.append(item3)
        cust=(L)
        sql="insert into food_items(item1,item2,item3)values(%s,%s,%s);"
        mycursor.execute(sql,cust)
        mydb.commit() 
        print("successfully orderd")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
def payment():
    n=int(input("For How Many Nights Do You want Stay:"))
    print ("We have the following rooms for you:-")
    print ("1. type A	>rs 1000 PN\-")
    print ("2. type B	>rs 2000 PN\-")
    print ("3. type C	>rs 3000 PN\-")
    print ("4. type D	>rs 4000 PN\-")
    x=int(input("Enter Your Choice Please->"))
 
    if(x==1):
        print ("you have opted room type A")
        s=1000*n
        print("your amount to pay is :",s,"\n") 
    elif (x==2):
        print ("you have opted room type B")
        s=2000*n
        print("your amount to pay is :",s,"\n") 
    elif (x==3):
        print ("you have opted room type C")
        s=3000*n
        print("your amount to pay is :",s,"\n") 
    elif (x==4):
        print ("you have opted room type D")
        s=4000*n
        print("your amount to pay is :",s,"\n") 
    else:
        print("you have not entered any room type")
        print ("please choose a room")

        
def display_breakfast():
    print("coffee---->50")
    print("tea------->40")
    print("sandwich--->120")
    print("milk------->25")
    print("omelettet---->100")
    print("salad-------->200")
def display_lunch():
    print("chaapati curry----->200")
    print("chicken curry---->500")
    print("tea------->40")
    print("rice--------->150")
    print("fruits------->450")
    print("icecream------>300")
def display_snacks():
    print("coffee---->50")
    print("tea------->40")
    print("onion rings--->120")
    print("milk------->25")
def display_dinner():
    print("rice---->100")
    print("curry------->50")
    print("non-veg--->620")
    print("milk------->25")
    print("omelettet---->100")
    print("salad-------->200")
def travel():
    print("****WELCOME TO TRAVEL****")
    print("select any mode of travel")
    print("1.SIDDHIVINAYAK DARSHAN PACKAGE,\n 2. PICK UP FROM AIRPORT,\n3. DROP TO AIRPORT,\n4.HOLIDAY PACKAGE,\n5.GOA BEACH")
    n=int(input("Enter the choice"))
    if(n==1):
        print("SUCESSFULLY REGISTERED ALL SET TO GO")
        print("Pay at the counter")
        print("Pur hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(n==2):
        print(" SUCESSFULLY REGISTERD ALL SET TO GO")
        print("Pay at the counter")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(n==3):
        print("SUCESSFULLY REGISTERD ALL SET TO GO")
        print("Pay at the counter")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    elif(n==4):
        print("SUCESSFULLY REGISTERD ALL SET TO GO")
        print("Pay at the counter")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")
    else:
        print("SUCESSFULLY REGISTERD ALL SET TO GO")
        print("Pay at the counter")
        print("Our hotel gourmet has opened a new portal for extra activities. do check it before you miss it")

def laundarybill():
    global z
    print("Do yoy want to see rate for laundary : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Enter the total Your number of clothes->"))
    z=y*10
    print("your laundary bill:",z,"\n")
    return z
#def viewbill():
    #a=input("enter customer name:")
    #print("customer name :",a,"\n")
    #print("laundarey bill:")
    #print(lb)
    #print("restaurent bill:")
    #print(payment)
def extra_activity():
    print("Do yoy want to see rate for extra_activity : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from activity"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Enter Your number to choose the activity"))
    if y==1:
        print("you are opted spa")
        z=y*1000
        print("your bill for spa:",z,"\n")
    elif y==2:
        print("you are opted meditation")
        z=y*1500
        print("your bill for meditation:",z,"\n")
    elif y==3:
        print("you are opted yoga")
        z=y*2000
        print("your bill for yoga:",z)
    else:
       print("you are opted gym")
       z=y*2000
       print("your bill for gym:",z)

def staff():
    R=[]
    name=input("Enter the name:")
    R.append(name)
    password=input("Enter the password:")
    R.append(password)
    password1=input("Enter the pasword:")
    R.append(password1)
    phno=int(input("Enter mobile number:"))
    R.append(phno)
    email=input("Enter the email address:")
    R.append(email)
    gender=input("Enter your gender:")
    R.append(gender)
    city=input("Enter the city name:")
    R.append(city)
    country=input("Enter the country name")
    R.append(country)
    cust=(R)
    print(cust)
    if(password==password1):
        sql="insert into staff(name,password,password1,phno,email,gender,city,country)values(%s,%s,%s,%s,%s,%s,%s,%s);"
        mycursor.execute(sql,cust)
        mydb.commit() 
        print("signin successful")
        #print("select any option to proceed")
        #print("1.accommodation 2.food items 3.payment")
        #choice=int(input("enter any option:"))
        #if(choice==1):
         #   accommodation()
        #elif(choice==2):
         #   food_items()    
        #else:    
         #   payment()
    else:
        print("Password does not match!!!\n Enter details again")
        staff()
   
       
    
        
    


