print('^^^WELCOME TO MARTIAN TOURISM^^^')
print('***SELECT YOUR PACKAGE***')
from prettytable import PrettyTable
t = PrettyTable(['ACCESS','PLATINUM','GOLD','SILVER'])
t.add_row(['Site Seeing Time','12 hr/day','6 hr/day','3 hr/day'])
t.add_row(['Space Walk Time','30 mins/day','20 mins/day','10 mins/day'])
t.add_row(['Energy/Day','6000 cal','4000 cal','3000 cal'])
t.add_row(['Room Level','5Star','6Star','7Star'])
t.add_row(['Luggage/Person','30 KG','20 KG','10 KG'])
print(t)
from prettytable import PrettyTable
t1 = PrettyTable(['PACKAGE','CODE'])
t1.add_row(['PLATINUM',0])
t1.add_row(['GOLD',1])
t1.add_row(['SILVER',2])
print(t1)
a=int(input('enter the package code : '))
b=int(input('total no of person(including childerns) : ')) 
i=0
while i<b:
    if a==0:
        p='PLANTINUM'
        c=input('enter the name : ')
        d=int(input('enter the age : '))
        e=input('if any allergies(Y/N) : ')
        f=input('food type(VEG/NONO-VEG) : ')
        g=int(input('enter the wieght : '))
        h=int(input('enter the height : '))
        i=i+1
        from prettytable import PrettyTable
        t2 = PrettyTable(['PACKAGE','NAME','AGE','ALLERGIES','FOOD_TYPE','WEIGHT','HEIGHT'])
        t2.add_row([p,c,d,e,d,g,h])
        print(t2)
        print('******TOURISM TICKET BOOKED******')
        print('******ENJOY YOUR JOURNEY ON OUR STARSHIP******')
    if a==1:
        p='GOLD'
        c=input('enter the name : ')
        d=int(input('enter the age : '))
        e=input('if any allergies(Y/N) : ')
        f=input('food type(VEG/NONO-VEG) : ')
        g=int(input('enter the wieght : '))
        h=int(input('enter the height : '))
        i=i+1
        from prettytable import PrettyTable
        t3 = PrettyTable(['PACKAGE','NAME','AGE','ALLERGIES','FOOD_TYPE','WEIGHT','HEIGHT'])
        t3.add_row([p,c,d,e,d,g,h])
        print(t3)
        print('******TOURISM TICKET BOOKED******')
        print('******ENJOY YOUR JOURNEY ON OUR STARSHIP******')
    if a==2:
        p='SILVER'
        c=input('enter the name : ')
        d=int(input('enter the age : '))
        e=input('if any allergies(Y/N) : ')
        f=input('food type(VEG/NONO-VEG) : ')
        g=int(input('enter the wieght : '))
        h=int(input('enter the height : '))
        i=i+1
        from prettytable import PrettyTable
        t4 = PrettyTable(['PACKAGE','NAME','AGE','ALLERGIES','FOOD_TYPE','WEIGHT','HEIGHT'])
        t4.add_row([p,c,d,e,d,g,h])
        print(t4)
        print('******TOURISM TICKET BOOKED******')
        print('******ENJOY YOUR JOURNEY ON OUR STARSHIP******')