from datetime import datetime
name=input("enter the name:")
# list of items
list='''rice        Rs 20/kg
        sugar       Rs 40/kg
        salt        Rs 20/kg
        michipowder Rs 100/200grams
        surfexel    Rs 80/50grams
        tide        Rs 84/kg
        
        
        
        
        '''
        
# print(list)

# decleration     
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

# rate for items
items={'rice':20,
       'sugar':30,
       'salt':20,
       'michipowder':100,
       'surfexel':80,
       'tide':84,
       }

option=int(input("List of items press 1:"))
if option==1:
    print(list)
    
for i in range(len(items)):
    inp1=int(input("if want to buy press 1 or 2 for exit : "))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your items:')
        quantity=int(input("enter your quantity:"))
    if item in items.keys():
        price=quantity*(items[item])
# print(price)
        pricelist.append((item,quantity,items,price))
        totalprice+=price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)
        gst=(totalprice*5)/100
        finalamount=gst+totalprice
    else:
        print("item not available")
else:
    print("Your Enter Wrong Number")
inp2=input("Can I Bill The Items Yes or NO : ")
if inp2=="YES":
    pass
if finalamount !=0:
            # print("Your Total Price is: ",finalamount)
            # for i in range(len(pricelist)):
            #     print(i,ilist[i],qlist[i],plist[i])
            print(25*"=","D-MART",25*"=")
            print(28*" ","KAKINADA")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ","items",8*" ","Quanity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,8*" ",5*" ",ilist[i],3*" ",qlist[i],8*" ",plist[i])
                print(75*"-")
                print(50*" ","TotalAmount:","RS",totalprice)
                print("GST Amount",40*" ","Rs",gst)
                print(75*"-")
                print(50*" ","FinalAmount:","RS",finalamount)
                print(75*"-")
                print(0*" ","Thank You Visting...")
                print(75*"-")
                 