#school management
'''this is a user friendly school managing software which is able to
enter new records read stored data ,can search record by different ways
and update records for both teacher and student it can also write marks of students moreover you can also update marks !!!
it contains 1950 lines and 47 functions that are as follows:
lines documentation:- 58 lines rest is code 1892
-------------9 functions related to security and menu---------
password()
psscheck()
query()
entry()
encode()
encoder()
decode()
decoder()
pssdeleter()
----------27 function for student--------------------
admchecker(z): -ensures uniqueness n non emptiness of adm no.
adm_maker(): -provides you a unique adm no. 
classlimit(z): -it will check that the class is in range of 1-12
wrtsr(): - it will enter new record in student\'s data 
reasr(): - it will read the whole student\'s data
sers():- it will search for a student in student\'s table with three different techniques
updatesr(): - it can update a student\'s record one at a time
rslt15(): - it shows the result of students\' of class b/w 1st to 5th inclusive both 1st and 5th
rslt610(): - it shows the result of students\' of class b/w 6th to 10th inclusive both 1st and 5th
rslt11(): - it shows the result of students\' of class 11th for whole 11th and for particular stream also'
rslt12(): - it shows the result of students\' of class 12th for whole 11th and for particular stream also'
wrtmrks15(): - it enters marks of students\' of class ranging between 1st and 5th for whole class'
wrtmrk15(a,b): -it works with wrtmrks15()
wrtmrks610(): - it enters marks of students\' of class ranging between 6th and 10th for whole class'
wrtmrk610(a,b): -it works with wrtmrks610()
wrtmrks1112()): - it enters marks of students\' of class 11th to 12th for whole class'
wrtmrk1112(a,b): -it works with wrtmrks1112()
rsltprtclr(): - it will shows the particular record of a student
classchecker1112(z): - it will check whether the class is in 11th n 12th
updatemrk1112(): - it will update marks of student of class 11th or 12th one at a time
classchecker610(z): -it will check whether the class is in 6th and 10th
updatemrk610: - it will update marks of student of class 6th or 7th or 8th or 9th or 10th one at a time
classchecker15(z): -it will check whether the class is in 1st to 5th
updatemrk15(): - it will update marks of student of class 1st or 2nd or 3rd or 4th or 5th one at a time
streamchecker(z): - it will check for a valid stream
namechecker(z): -it ensures non emptiness of name column
rec_deleters(): -it will delete !!! a particular student\'s record one at a time

---- for teachers\'s record there are 7 functions----
tchridchecker(z): -ensures uniqueness n non emptiness of teacher id
enttr(): -it enters new teacher\'s record
sert(): - it can search for a teacher in 3 different techniques
reatr(): -it will read whole teacher\'s data
updatetr(): - it can updatea teacher\'s record one at a time
tchrid_maker(): -it will auto generate teacher id on user\'s requirement
backupst():- it will make a checkpoint you can retrieve your data from nerest one for student\'s data 
backuptc():- it will make a checkpoint you can retrieve your data from nerest one for teacher\'s data
restorest():- it will restore the student\'s data by retriving data from nearest checkpoint
restoretc():- it will restore the teacher\'s data by retriving data from nearest checkpoint
rec_deletert(): - it will delete a teacher\'s record one at a time
'''
def password():
        alphapsswrd='alphapsswrd1'
        a=open('d:\\school management\\alpha.txt','w')
        a.write(alphapsswrd)
        a.close()
        passwrd=input('enter your password here remeber your password is case sensitive ')
        pobjt=open('d:\\school management\\dont delete me.dat','wb')
        dic={}
        dic['password']=passwrd
        while True:
            print('do you want to set a ques in case you forgot the password you can enter just by answering the phrase(y/n)')
            ch=input('enter your choice here').lower()
            if ch=='y':
                question=input('enter your question')
                answer=input('enter your answer').lower()
                pobjt=open('d:\\school management\\dont delete me.dat','wb')
                dic2={}
                dic2['password']=passwrd
                dic2['question']=question
                dic2['answer']=answer
                pickle.dump(dic2,pobjt)
                ans1='y'            
                a=open('d:\\school management\\yn.txt','w')
                a.write(ans1)
                a.close()
                break
            elif ch=='n':
                print('OK')
                pickle.dump(dic,pobjt)
                ans1='n'            
                a=open('d:\\school management\\yn.txt','w')
                a.write(ans1)
                a.close()
                break
            else:
                print('wrong input')
        pobjt.close()

def psscheck():
    fobjt=open('d:\\school management\\dont delete me.dat','rb')
    dic={}
    try:
        while True:
            dic=pickle.load(fobjt)
    except EOFError:
        fobjt.close()
    global c    
    a=input('How you want to login by password press p and a by a answering to question').lower()
    if a=='p':
        pss=input('enter your password')
        if dic['password']==pss:
            c=True
        else:
            sys.stderr.write('wrong password entered \n')
            print('reneter it')
            psscheck()
    elif a=='a':
        if os.path.isfile('d:\\school management\\yn.txt'):
            a=open('d:\\school management\\yn.txt')
            b=a.read()
            a.close()
            if b=='y':
                print('question is ---->',dic['question'])
                ans=input('enter answer of above question')
                if dic['answer']==ans:
                    c=True
                else:
                    sys.stderr.write('wrong answer entered \n')
                    print('reneter it')
                    psscheck()
            if b=='n':
                print('it seems you dont have any question use password option')
                psscheck()
        else:
            print('it seems you deleted question file')
            psscheck()
    else:
        print('oops you press wrong key')
        psscheck()
    return c    

           


import os,csv,sys,random,pickle


direc=os.path.isdir('d:\\school management')
if direc == False:
    os.mkdir('d:\\school management')
    sys.stderr.write('do you want to save your file with password(y/n) \n')
    choice=input('enter your choice here').lower()
    if choice=='y':
        print('Please enter your password which is impossible to crack but easy to remember')
        password()
    elif choice=='n':
        alphapsswrd='alphapsswrd0'
        a=open('d:\\school management\\alpha.txt','w')
        a.write(alphapsswrd)
        a.close()
        print('OK')
    else:
        print('wrong input')
    
    

#sturec
files=os.path.isfile('d:\\school management\\sturec.csv')
if files==False:
    a=open('d:\\school management\\sturec.csv','a',newline='')
    b=csv.writer(a)
    c=['Name','Father Name','Mother Name','Class','Section','Roll no.','Admission no.','Phone Number','Stream']
    c.extend(['English','Maths','Science','Computer','Hindi','Sst','G.K','Evst'])
    c.extend(['Physics','Chemistry','Biology','Economics','Accounts','B.St.','Pol.science','Geography','Optional'])
    b.writerow(c)
    a.close()
            
        
            
def adm_maker():
        a='S'
        b=str(random.randint(00000,99999))
        if len(b)<5:
            c='0'*(5-len(b))
            d=a+c+b
        else:
            d=a+b
        return d

    
def streamchecker(z):
    global g
    if z not in ['nm','ar','co','md']:
        sys.stderr.write('wrong stream entered \n')
        k=input('enter correct stream').lower().strip()
        streamchecker(k)
    else:
        g=z
    return(g)


def namechecker(z,x):
    global g
    if z=='':
        l='you can\'t leave'+x+ 'name column empty \n'
        sys.stderr.write(l)
        a='enter'+x+'name'
        k=input(a).title().strip()
        namechecker(k,x)
    else:
        g=z
    return g
        
              
def admchecker(z):
    a=0
    with open('d:\\school management\\sturec.csv') as fobjt2:
        admread=csv.reader(fobjt2)
        global g
        for i in admread:
            e=i
            if e[6]==z  :
                sys.stderr.write('Adm no. is already taken \n')
                k=input('enter different adm no.').upper().strip()
                a+=1
                g=k
        if z=='':
            sys.stderr.write('column of admission no. can\'t be left blank \n')
            k=input('enter adm no.').upper().strip()
            a+=1
            g=k
        if a!=0:
            admchecker(g)
        elif a==0:
            g=z
    return(g)


def classlimit(z):
    a=0
    global g
    if z not in ['1','2','3','4','5','6','7','8','9','10','11','12']:
        sys.stderr.write('wrong class entered \n')
        k=input('enter correct class in numerals only').strip()
        g=k
        a+=1
    if a!=0:
        classlimit(k)
    else:
        g=z
    return(g)


def wrtsr():
    '''it will enter new records in existing file'''
    fobj=open('d:\\school management\\sturec.csv','a',newline='')
    
    writer=csv.writer(fobj)
    a2=int(input('enter no. of records you want to enter'))
    for i in range (a2):
        a=input("student\'s Name").title().strip()
        a=namechecker(a,' student\'s ')
        b=input("student\'s Father Name").title().strip()
        b=namechecker(b,' father\'s ')
        c=input("student\'s Mother Name").title().strip()
        c=namechecker(c,' mother\'s ')
        d=str(input('enter class')).strip()
        d=classlimit(d)
        f=int(input('enter roll no.'))
        ch=input('do you need auto generated adm no.(y/n)')
        if ch=='y' or ch=='Y':
            g=adm_maker()
            
        else:
            print('OK')
            g=input('enter admission no.').upper().strip()
        g=admchecker(g)
        print('admission no. given to student is', g)
        h=int(input('enter phone no.'))
        if d=='11' or d=='12':
            print('enter nm for non medical')
            print('enter md for medical')
            print('enter co for commerce')
            print('enter ar for arts')
            i=input('enter stream').lower().strip()
            i=streamchecker(i)
            e='nil'
        else:
            i='nil'
            e=input("enter section").upper().strip()
        j=[a,b,c,d,e,f,g,h,i]
        for i in range(0,17):
            j.append('')
        writer.writerow(j)
        fobj.flush()
        print('\n')
    fobj.close()


def reasr():
    ''' it will read and show you the whole record'''
    fobj=open('d:\\school management\\sturec.csv')
    reader=csv.reader(fobj)
    for i in reader:
        print(i)
    fobj.close()


def sers():
    '''can search with three different situations'''
    a=input('press n to search by name, a to search by adm no. , nc for a student of specific class').lower().strip()
    fobjt=open('d:\\school management\\sturec.csv','r',newline='')
    c=csv.reader(fobjt)
    z=0
    if a == 'n':
        d=input('enter student\'s name ').title().strip()
        d=namechecker(d,' student\'s ')
        print(['Name', 'Father Name', 'Mother Name', 'Class', 'Section', 'Roll no.', 'admission no.',
           'phone number', 'stream', 'english', 'maths', 'science',
           'computer', 'hindi', 'Sst', 'G.K', 'Evst', 'physics', 'chemistry', 'biology', 'economics', 'accounts',
           'B.St.', 'Pol.science', 'geography', 'optional'])
        for i in c:
            e=i
            if e[0]==d:
                print(e)
                z+=1
            
    if a=='a':
        d=input('enter admission no.').upper().strip()
        print(['Name', 'Father Name', 'Mother Name', 'Class', 'Section', 'Roll no.', 'admission no.',
           'phone number', 'stream', 'english', 'maths', 'science',
           'computer', 'hindi', 'Sst', 'G.K', 'Evst', 'physics', 'chemistry', 'biology', 'economics', 'accounts',
           'B.St.', 'Pol.science', 'geography', 'optional'])
        for i in c:
            e=i
            if e[6]==d:
                print(e)
                z+=1
    if a=='nc':
        d=input('enter name').title().strip()
        d=namechecker(d,' student\'s ')
        f=input('enter class').strip()
        f=classlimit(f)
        if f in ['11','12']:
            print('enter nm for non medical')
            print('enter md for medical')
            print('enter co for commerce')
            print('enter ar for arts')
            g=input('enter stream').lower().strip()
            g=streamchecker(g)
        else:
            g=input('enter section').upper().strip()
        h=input('enter admission no.').upper().strip()
        print(['Name', 'Father Name', 'Mother Name', 'Class', 'Section', 'Roll no.', 'admission no.',
           'phone number', 'stream', 'english', 'maths', 'science',
           'computer', 'hindi', 'Sst', 'G.K', 'Evst', 'physics', 'chemistry', 'biology', 'economics', 'accounts',
           'B.St.', 'Pol.science', 'geography', 'optional'])
        for i in c:
            e=i
            if e[0]==d and e[3]==f and (e[4]==g or e[8]==g) and e[6]==h :
                print(e)
                z+=1
    if z==0:
        sys.stderr.write('no result found')
    fobjt.close()


def updatesr():
    '''it can update fields except marks\' column'''
    fobjt=open('d:\\school management\\sturec.csv','r')
    reader=csv.reader(fobjt)
    lst=[]
    cnt=0
    d=input('enter name').title().strip()
    d=namechecker(d,' student\'s ' )
    f=input('enter class').strip()
    f=classlimit(f)
    if f not in ['11','12']:
        g=input('enter section').upper().strip()
    else:
        print('enter nm for non medical')
        print('enter md for medical')
        print('enter co for commerce')
        print('enter ar for arts')
        g=input('enter stream').lower().strip()
        g=streamchecker(g)
    h=input('enter admission no.').upper().strip()
    for i in reader:
        e=i
        if i[0]==d and i[3]==f and ( i[4]==g or i[8]==g ) and i[6]==h :
            print('old record',e)
            chn=input('''to change press n,c,s,a,r,f,m,p for name,class section/stream, admno.,roll no.,
                      father name,mother name and phone no.respectively''').lower()
            if chn=='n':
                f=input('enter correct name').title().strip()
                f=namechecker(f,' student\'s ')
                e[0]=f
            elif chn=='f':
                f=input('enter correct father\'s name ').title().strip()
                f=namechecker(f,' father\'s ')
                e[1]=f
            elif chn=='m':
                f=input('enter correct mother\'s name ').title().strip()
                f=namechecker(f,' mother\'s ')
                e[2]=f
            elif chn=='c':
                f=input('enter correct class').strip()
                f=classlimit(f)
                e[3]=f
                e[9],e[10],e[11],e[12],e[13],e[14],e[15],e[16],e[17],e[18],e[19],e[20],e[21],e[22],e[23],e[24],e[25]='','','','','','','','','','','','','','','','',''
                if f in ['11','12']:
                    print('enter nm for non medical')
                    print('enter md for medical')
                    print('enter co for commerce')
                    print('enter ar for arts')
                    z=input('enter stream').lower().strip()
                    z=streamchecker(z)
                    e[8]=z
                    e[4]='nil'
                    print('as the class alteres marks also alter')
                    ch=input('do you also want to update marks now(y/n)').strip()
                    if ch=='y' or ch=='Y':
                        if z=='nm':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for physics'))
                            d=int(input('enter marks for chemistry'))
                            m=int(input('enter marks for maths'))
                            g=int(input('enter marks for optional'))
                            e[9],e[17],e[18],e[10],e[25]=b,c,d,m,g
                        elif z=='md':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for physics'))
                            d=int(input('enter marks for chemistry'))
                            bi=int(input('enter marks for biology'))
                            g=int(input('enter marks for optional'))
                            e[9],e[17],e[18],e[19],e[25]=b,c,d,bi,g
                        elif z=='ar':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for economics'))
                            d=int(input('enter marks for pol.science'))
                            ge=int(input('enter marks for geography'))
                            g=int(input('enter marks for optional'))
                            e[9],e[20],e[23],e[24],e[25]=b,c,d,ge,g
                        elif z=='co':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for economics'))
                            d=int(input('enter marks for accounts'))
                            bs=int(input('enter marks for B.St'))
                            g=int(input('enter marks for optional'))
                            e[9],e[20],e[21],e[22],e[25]=b,c,d,bs,g
                    elif ch=='n' or ch=='N':
                        print('OK')

                    
                elif f in ['6','7','8','9','10']:
                    z=input('enter section').upper().strip()
                    e[4]=z
                    e[8]='nil'
                    print('as the class alteres marks also alter')
                    ch=input('do you also want to update marks now(y/n)').strip()
                    if ch=='y' or ch=='Y':
                        b=int(input('enter marks of english'))
                        c=int(input('enter marks of maths'))
                        d=int(input('enter marks of science '))
                        fb=int(input('enter marks of computer'))
                        g=int(input('enter marks of hindi'))
                        h=int(input('enter marks of  S.St'))
                        e[9],e[10],e[11],e[12],e[13],e[14]=b,c,d,fb,g,h
                    elif ch=='n' or ch=='N':
                        print('OK')
                else:
                    z=input('enter section').upper().strip()
                    e[4]=z
                    e[8]='nil'
                    print('as the class alteres marks also alter')
                    ch=input('do you also want to update marks now(y/n)').strip()
                    if ch=='y' or ch=='Y':
                        b=int(input('enter marks of english'))
                        c=int(input('enter marks of maths'))
                        d=int(input('enter marks of computer'))
                        f=int(input('enter marks of hindi'))
                        g=int(input('enter marks of Gk'))
                        h=int(input('enter marks of  Evst'))
                        e[9],e[10],e[12],e[13],e[15],e[16]=b,c,d,f,g,h
                    elif ch=='n' or ch=='N':
                        print('OK')
            elif chn=='s':
                if e[3] in ['11','12'] :
                    print('enter nm for non medical')
                    print('enter md for medical')
                    print('enter co for commerce')
                    print('enter ar for arts')
                    f=input('enter correct stream').lower().strip()
                    f=streamchecker(f)
                    e[8]=f
                    e[9],e[10],e[17],e[18],e[19],e[20],e[21],e[22],e[23],e[24],e[25]='','','','','','','','','','',''
                    print('as the stream alters marks are also alter')
                    ch=input('do you also want to update marks now(y/n)').strip()
                    if ch=='y' or ch=='Y':
                        if f=='nm':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for physics'))
                            d=int(input('enter marks for chemistry'))
                            m=int(input('enter marks for maths'))
                            g=int(input('enter marks for optional'))
                            e[9],e[17],e[18],e[10],e[25]=b,c,d,m,g
                        elif f=='md':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for physics'))
                            d=int(input('enter marks for chemistry'))
                            bi=int(input('enter marks for biology'))
                            g=int(input('enter marks for optional'))
                            e[9],e[17],e[18],e[19],e[25]=b,c,d,bi,g
                        elif f=='ar':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for economics'))
                            d=int(input('enter marks for pol.science'))
                            ge=int(input('enter marks for geography'))
                            g=int(input('enter marks for optional'))
                            e[9],e[20],e[23],e[24],e[25]=b,c,d,ge,g
                        elif f=='co':
                            b=int(input('enter marks for english'))
                            c=int(input('enter marks for economics'))
                            d=int(input('enter marks for accounts'))
                            bs=int(input('enter marks for B.St'))
                            g=int(input('enter marks for optional'))
                            e[9],e[20],e[21],e[22],e[25]=b,c,d,bs,g
                    elif ch=='n' or ch=='N':
                        print('OK')
                else:
                    f=input('enter correct section').upper().strip()
                    e[4]=f
            elif chn=='r':
                f=int(input('enter correct roll no.')) 
                e[5]=f
            elif chn=='a':
                ch=input('do you need auto generated adm no. (y/n)')
                if ch=='y' or ch=="Y":
                    f=adm_maker()
                else:
                    print('OK')
                    f=input('enter correct admission no.').upper().strip()
                f=admchecker(f)
                e[6]=f
            elif chn=='p':
                f=int(input('enter correct phone no.'))
                e[7]=f
            print('new record',e)
            cnt=1
        lst.append(e)
    if cnt==1:
        fobjt.close()
        fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
        writer=csv.writer(fobjt2)
        for i in range(len(lst)):
            writer.writerow(lst[i])
        fobjt2.close()
    else:
        sys.stderr.write('no such record found recheck all the enteries')

    
def rslt15(kv):
    '''shows result for students of class in range of 1st to 5th'''
    fobjt=open('d:\\school management\\sturec.csv')
    a=kv
    a=classlimit(a)
    b=input('enter section').upper().strip()
    c=[]
    if a in ['1','2','3','4','5']:
        fobjt.seek(0)
        readers=csv.reader(fobjt)
        print(['Name','Father Name','Mother Name','Class','Section','Roll no.','admission no.','phone number'
               ,'english','maths','hindi','computer','evst','gk'])
        for i in readers:
            e=i
            if e[3]==a and e[4]==b:
                for j in range(0,26):
                    if e[j]=='nil' or e[j]=='':
                        pass
                    else:
                        c.append(e[j])
                print(c)
                c=[]
    fobjt.close()

            
def rslt610(kv):
    '''shows result for students of class in range of 6th to 10th'''
    fobjt=open('d:\\school management\\sturec.csv')
    a=str(kv).strip()
    a=classlimit(a)
    b=input('enter section').upper().strip()
    c=[]
    if a in ['6','7','8','9','10']:
        fobjt.seek(0)
        readers=csv.reader(fobjt)
        print(['Name','Father Name','Mother Name','Class','Section','Roll no.','admission no.','phone number','english','maths','science','computer','hindi','Sst'])
        for i in readers:
            e=i
            if e[3]==a and e[4]==b:
                for j in range(0,26):
                    if e[j]=='nil' or e[j]=='':
                        pass
                    else:
                        c.append(e[j])
                print(c)
                c=[]
    fobjt.close()

    
def rslt11():
    '''shows result for students of 11th class of any one particular stream at a time  '''
    print('1 to check whole class 11th result')
    print('2 to check for a particuar stream')
    b=int(input('enter your choice'))
    fobjt=open('d:\\school management\\sturec.csv')
    readers=csv.reader(fobjt)
    if b==1:
        print ('*' *10,'result of class 11','*' *10)
        print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
        'phone number, stream, english, maths, science, computer,'
        'hindi, Sst, G.K, Evst, physics, chemistry, biology, economics, accounts, B.St.,'
        'Pol.science, geography, optional')
        fobjt.seek(0)
        for i in readers:
            if i[3]=='11':
                print(i)

    if b==2:
        fobjt.seek(0)
        print('enter nm for non medical')
        print('enter m for medical')
        print('enter c for commerce')
        print('enter a for arts')
        a=input('enter stream').lower().strip()
        a=streamchecker(a)
        print ('*' *10,'result of class 11','*' *10)
        c=[]
        if a=='md':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,physics, chemistry, biology,optional' )
            for i in readers:
                e=i
                if e[3]=='11' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
        elif a=='nm':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,maths,physics, chemistry,optional' )
            for i in readers:
                e=i
                if e[3]=='11' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
        elif a=='co':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,economics,accounts, B.St,optional' )
            for i in readers:
                e=i
                if e[3]=='11' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
        elif a=='ar':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,economics,Pol Science, geography,optional' )
            for i in readers:
                e=i
                if e[3]=='11' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
    fobjt.close()

         
def rslt12():
    '''shows result for students of 12th class of any one particular stream at a time  '''
    print('1 to check whole class12th result')
    print('2 to check for a particuar stream')
    b=int(input('enter your choice'))
    fobjt=open('d:\\school management\\sturec.csv')
    readers=csv.reader(fobjt)
    if b==1:
        print ('*' *10,'result of class 12','*' *10)
        fobjt.seek(0)
        print(['Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
             'phone number, stream, english, maths, science, computer,'
             'hindi, Sst, G.K, Evst, physics, chemistry, biology, economics, accounts, B.St.,'
             'Pol.science, geography, optional'])
        for i in readers:
            if i[3]=='12':
                print(i)
    if b==2:
        fobjt.seek(0)
        print('enter nm for non medical')
        print('enter m for medical')
        print('enter c for commerce')
        print('enter a for arts')
        a=input('enter stream').lower().strip()
        a=streamchecker(a)
        print ('*' *10,'result of class 12','*' *10)
        c=[]
        if a=='md':
            print('Name, Father Name, Mother Name , Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,physics, chemistry, biology,optional' )
            for i in readers:
                e=i
                if e[3]=='12' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                c=[]
        elif a=='nm':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,maths,physics, chemistry,optional' )
            for i in readers:
                e=i
                if e[3]=='12' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
        elif a=='co':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,economics,accounts, B.St,optional' )
            for i in readers:
                e=i
                if e[3]=='12' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
        elif a=='ar':
            print('Name, Father Name, Mother Name, Class, Section, Roll no., admission no.,'
                   'phone number, stream, english,economics,Pol Science, geography,optional' )
            for i in readers:
                e=i
                if e[3]=='12' and e[8]==a:
                    for j in range(0,26):
                        if e[j]=='nil' or e[j]=='':
                            pass
                        else:
                            c.append(e[j])
                    print(c)
                    c=[]
    fobjt.close()

def wrtmrks15(kv):
    '''to enter marks of students of class in range of 1st to 5th. any one particular class at a time  '''
    a=kv.strip()
    a=classchecker15(a)
    b=input('enter section').upper().strip()
    cnt=0
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    print('enter marks for students of class',a,'th' ,b)
    sys.stderr.write('marks should be in three digit format for eg 6 should be written as 006 \n')
    for i in read:
        if i[3]==a and i[4]==b and i[9]=='' and i[10]=='' and i[12]=='' and i[13]=='' and i[15]=='' and i[16]=='':
            cnt+=1
    fobjt.close()
    for i in range(cnt):
        wrtmrk15(a,b)
    
 

def wrtmrk15(a,b):
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        e=i
        if i[3]==a and i[4]==b and i[9]=='' and i[10]=='' and i[12]=='' and i[13]=='' and i[15]=='' and i[16]=='':
            print('enter marks for ', 'name','->',e[0],'-','adm no. ->',e[6]) 
            b=int(input('enter marks of english'))
            c=int(input('enter marks of maths'))
            d=int(input('enter marks of computer'))
            f=int(input('enter marks of hindi'))
            g=int(input('enter marks of Gk'))
            hs=int(input('enter marks of  Evst'))
            e[9],e[10],e[12],e[13],e[15],e[16]=b,c,d,f,g,hs
        k.append(e)
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
    writers=csv.writer(fobjt2)
    for i in range(len(k)):
        writers.writerow(k[i])
    fobjt2.close()


def wrtmrks610(kv):
    '''to enter marks of students of class in range of 6th to 10th. any one particular class at a time  '''
    a=kv.strip()
    a=classchecker610(a)
    b=input('enter section').upper()
    cnt=0
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    print('enter marks for students of class',a,'th' ,b)
    sys.stderr.write('marks should be in three digit format for eg 6 should be written as 006 \n')
    for i in read:
        if i[3]==a and i[4]==b and i[9]=='' and i[10]=='' and i[11]=='' and i[12]=='' and i[13]=='' and i[14]=='':
            cnt+=1
    fobjt.close()
    for i in range(cnt):
        wrtmrk610(a,b)
 

def wrtmrk610(a,b):
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        e=i
        if i[3]==a and i[4]==b and i[9]=='' and i[10]=='' and i[11]=='' and  i[12]=='' and i[13]=='' and i[14]=='':
            print('enter marks for ', 'name','->',e[0],'-','adm no. ->',e[6]) 
            b=int(input('enter marks of english'))
            c=int(input('enter marks of maths'))
            s=int(input('enter marks of  Science'))
            d=int(input('enter marks of computer'))
            f=int(input('enter marks of hindi'))
            g=int(input('enter marks of S.St'))
            e[9],e[10],e[11],e[12],e[13],e[14]=b,c,s,d,f,g
        k.append(e)
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
    writers=csv.writer(fobjt2)
    for i in range(len(k)):
        writers.writerow(k[i])
    fobjt2.close()

def wrtmrks1112(kv):
    '''to enter marks of students of class 11th and 12th. any one particular class at a time  '''
    b=kv.strip()
    b=classchecker1112(b)
    print('enter nm for non medical')
    print('enter md for medical')
    print('enter co for commerce')
    print('enter ar for arts')
    a=input('enter stream').lower().strip()
    a=streamchecker(a)
    cnt=0
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    print('enter marks of students of class',b,'of stream',a) 
    sys.stderr.write('marks should be in three digit format for eg 6 should be written as 006 \n')
    for i in read:
        if i[3]==b and i[8]==a and i[9]=='' or i[10]=='' or i[17]=='' or i[18]=='' or i[19]=='' and i[25]=='':
            cnt+=1
    fobjt.close()
    for i in range(cnt):
        wrtmrk1112(b,a)
        
def wrtmrk1112(b,a):
    fobjt=open('d:\\school management\\sturec.csv','r')
    reader=csv.reader(fobjt)
    k=[]
    if a=='md':
        for i in reader:
            e=i
            if e[8]=='md' and i[3]==b and e[9]=='' and e[17]=='' and e[18]=='' and e[19]=='' and e[25]=='':
                print('enter marks for student---->',e[0],'admno.--->',e[6])
                b=int(input('enter marks for english'))
                c=int(input('enter marks for physics'))
                d=int(input('enter marks for chemistry'))
                f=int(input('enter marks for biology'))
                g=int(input('enter marks for optional'))
                e[9],e[17],e[18],e[19],e[25]=b,c,d,f,g
            k.append(e)
    elif a=='nm':
        for i in reader:
            e=i
            if i[8]=='nm' and i[3]==b and e[9]=='' and e[10]=='' and e[17]=='' and e[18]=='' and e[25]=='':
                print('enter marks for student---->',e[0],'admno.--->',e[6])
                b=int(input('enter marks for english'))
                c=int(input('enter marks for physics'))
                d=int(input('enter marks for chemistry'))
                f=int(input('enter marks for maths'))
                g=int(input('enter marks for optional'))
                e[9],e[17],e[18],e[10],e[25]=b,c,d,f,g
            k.append(e)
    elif a=='co':
        for i in reader:
            e=i
            if e[8]=='co' and e[3]==b and e[9]=='' and e[20] and e[21] and e[22] and e[25]=='':
                print('enter marks for student---->',e[0],'admno.--->',e[6])
                b=int(input('enter marks for english'))
                c=int(input('enter marks for economics'))
                d=int(input('enter marks for accounts'))
                f=int(input('enter marks for B.St'))
                g=int(input('enter marks for optional'))
                e[9],e[20],e[21],e[22],e[25]=b,c,d,f,g
                    
    elif a=='ar':
        for i in reader:
            e=i
            if e[8]=='ar' and e[3]==b and e[9]=='' and e[20]=='' and e[23]=='' and e[24]=='' and e[25]=='':
                    print('enter marks for student---->',e[0],'admno.--->',e[6])                   
                    b=int(input('enter marks for english'))
                    c=int(input('enter marks for economics'))
                    d=int(input('enter marks for pol.science'))
                    f=int(input('enter marks for geography'))
                    g=int(input('enter marks for optional'))
                    e[9],e[20],e[23],e[24],e[25]=b,c,d,f,g
        k.append(e)
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
    writer=csv.writer(fobjt2)
    for i in range(len(k)):
        writer.writerow(k[i])
    fobjt2.close()


def rsltprtclr():
    '''shows result of a particular student''' 
    a=input('enter student\'s name:').title().strip()
    b=input('enter student\'s class:').strip()
    b=classlimit(b)
    if b not in ['11','12']:
        c=input('enter student\'s section:').upper().strip()
    else:
        c=input('enter student\'s stream:').lower().strip()
        c=streamchecker(c)
    d=int(input('enter student\'s roll no. :'))
    e=input('enter student\'s adm no.:').upper().strip()
    
    fobjt=open('d:\\school management\\sturec.csv','r')
    reader=csv.reader(fobjt)
    print('*'*110)
    if b in ['11','12']:
        for i in reader:
            if i[0]==a and i[3]==b and i[8]=='nm' and i[6]==e:
                print('student\'s name:- ---->',i[0])
                print('student\'s Father name:- ---->',i[1],)
                print('student\'s Mother name:- ---->',i[2])
                print('student\'s class ,stream:- ---->',i[3],i[8])
                print('Student\'s roll no.:- --->',i[5])
                print('Student\'s adm no.:- --->',i[6])
                print('Student\'s phone no.:- --->',i[7])
                print('|marks in English    |',i[9],'|')
                print('|marks in physics    |',i[17],'|')
                print('|marks in chemistry |',i[18],'|')
                print('|marks in maths      |',i[10],'|')
                print('|marks in Optional  |',i[25],'|')
                print('|total marks  |',int(i[9])+int(i[17])+int(i[18])+int(i[10])+int(i[25]),'|')
                print('*'*110)
            elif i[0]==a and i[3]==b and i[8]=='md' and i[5]==d and i[6]==e:
                print('student\'s name:- ---->',i[0])
                print('student\'s Father name:- ---->',i[1],)
                print('student\'s Mother name:- ---->',i[2])
                print('student\'s class ,stream:- ---->',i[3],i[8])
                print('Student\'s roll no.:- --->',i[5])
                print('Student\'s adm no.:- --->',i[6])
                print('Student\'s phone no.:- --->',i[7])
                print('|marks in English    |',i[9],'|')
                print('|marks in physics    |',i[17],'|')
                print('|marks in chemistry |',i[18],'|')
                print('|marks in biology    |',i[19],'|')
                print('|marks in Optional   |',i[25],'|')
                print('|total marks  |',int(i[9])+int(i[17])+int(i[18])+int(i[19])+int(i[25]),'|') 
                print('*'*110)
            elif i[0]==a and i[3]==b and i[8]=='co' and i[5]==d and i[6]==e:
                print('student\'s name:- ---->',i[0])
                print('student\'s Father name:- ---->',i[1],)
                print('student\'s Mother name:- ---->',i[2])
                print('student\'s class ,stream:- ---->',i[3],i[8])
                print('Student\'s roll no.:- --->',i[5])
                print('Student\'s adm no.:- --->',i[6])
                print('Student\'s phone no.:- --->',i[7])
                print('|marks in English      |',i[9],'|')
                print('|marks in economics |',i[20],'|')
                print('|marks in Accounts   |',i[21],'|')
                print('|marks in B.st           |',i[22],'|')
                print('|marks in Optional    |',i[25],'|')
                print('|total marks  |',int(i[9])+int(i[21])+int(i[22])+int(i[20])+int(i[25]),'|') 
                print('*'*110)
            elif i[0]==a and i[3]==b and i[8]=='ar' and i[5]==d and i[6]==e:
                print('student\'s name:- ---->',i[0])
                print('student\'s Father name:- ---->',i[1],)
                print('student\'s Mother name:- ---->',i[2])
                print('student\'s class ,stream:- ---->',i[3],i[8])
                print('Student\'s roll no.:- --->',i[5])
                print('Student\'s adm no.:- --->',i[6])
                print('Student\'s phone no.:- --->',i[7])
                print('|marks in English            |',i[9],'|')
                print('|marks in economics       |',i[20],'|')
                print('|marks in Pol science      |',i[23],'|')
                print('|marks in Geography      |',i[24],'|')
                print('|marks in Optional          |',i[25],'|')
                print('|total marks  |',int(i[9])+int(i[24])+int(i[23])+int(i[20])+int(i[25]),'|')
                print('*'*110)
    elif b in ['6','7','8','9','10']:
        for i in reader:
            if i[0]==a and i[3]==b and i[4]==c and i[5]==d and i[6]==e:
                print('student\'s name:- ---->',i[0])
                print('student\'s Father name:- ---->',i[1],)
                print('student\'s Mother name:- ---->',i[2])
                print('student\'s class & section:- ---->',i[3],i[4])
                print('Student\'s roll no.:- --->',i[5])
                print('Student\'s adm no.:- --->',i[6])
                print('Student\'s phone no.:- --->',i[7])
                print('|marks in English    |',i[9],'|')
                print('|marks in Maths      |',i[10],'|')
                print('|marks in science     |',i[11],'|')
                print('|marks in hindi        |',i[13],'|')
                print('|marks in Computer |',i[12],'|')
                print('|marks in S.St          |',i[14],'|')
                print('|total marks  |',int(i[9])+int(i[11])+int(i[12])+int(i[10])+int(i[13])+int(i[14]),'|')
                print('*'*110)
    elif b in ['1','2','3','4','5']:
        for i in reader:
            if i[0]==a and i[3]==b and i[4]==c and i[5]==d and i[6]==e:
                print('student\'s name:- ---->',i[0])
                print('student\'s Father name:- ---->',i[1],)
                print('student\'s Mother name:- ---->',i[2])
                print('student\'s class & section:- ---->',i[3],i[4])
                print('Student\'s roll no.:- --->',i[5])
                print('Student\'s adm no.:- --->',i[6])
                print('Student\'s phone no.:- --->',i[7])
                print('|marks in English      |',i[9],'|')
                print('|marks in Maths        |',i[10],'|')
                print('|marks in EVST         |',i[16],'|')
                print('|marks in hindi         |',i[13],'|')
                print('|marks in Computer  |',i[12],'|')
                print('|marks in G.K           |',i[15])
                print('|total marks  |',int(i[9])+int(i[10])+int(i[12])+int(i[16])+int(i[13])+int(i[15]),'|')
                print('*'*110)
    fobjt.close()

def classchecker1112(z):
    global k
    k=z
    if z not in ['11','12']:
        sys.stderr.write('initialised class is invalid as function is for class 11th and 12 \n')
        z=input('enter class in numerals only').strip()
        k=z
        classchecker1112(z)
    else:
        return (k)
   
def updatemrk1112(kv):
    '''update marks of students of class 11th and 12th'''
    fobjt=open('d:\\school management\\sturec.csv','r')
    reader=csv.reader(fobjt)
    a=input('enter student\'s name').title().strip()
    b=input('enter student\'s adm no.').upper().strip()
    c=kv
    c=classchecker1112(c)
    k=[]
    cnt=0
    for i in reader:
        e=i
        if e[0]==a and e[3]==c and e[6]==b:
            print('old record',e)
            if e[8]=='nm':
                print('press E to update marks of English')
                print('press P to update marks of physics')
                print('press C to update marks of chemistry')
                print('press M to update marks of maths')
                print('press O to update marks of Optional')
                ch=input('enter your choice').upper().strip()
                if ch =='E':
                    f=int(input('enter correct marks for english'))
                    e[9]=f
                elif ch =='P':
                    f=int(input('enter correct marks for physics'))
                    e[17]=f
                elif ch =='C':
                    f=int(input('enter correct marks for chemistry'))
                    e[18]=f
                elif ch =='M':
                    f=int(input('enter correct marks for maths'))
                    e[10]=f
                elif ch =='O':
                    f=int(input('enter correct marks for optional'))
                    e[25]=f
            elif i[8]=='md':
                print('press E to update marks of English')
                print('press P to update marks of physics')
                print('press C to update marks of chemistry')
                print('press B to update marks of Biology')
                print('press O to update marks of Optional')
                ch=input('enter your choice').upper()
                if ch =='E':
                    f=int(input('enter correct marks for english'))
                    e[9]=f
                elif ch =='P':
                    f=int(input('enter correct marks for physics'))
                    e[17]=f
                elif ch =='C':
                    f=int(input('enter correct marks for chemistry'))
                    e[18]=f
                elif ch =='B':
                    f=int(input('enter correct marks for biology'))
                    e[10]=f
                elif ch =='O':
                    f=int(input('enter correct marks for optional'))
                    e[25]=f
            elif i[8]=='co':
                print('press E to update marks of English')
                print('press EC to update marks of economics')
                print('press A to update marks of Accounts')
                print('press B to update marks of B.st')
                print('press O to update marks of Optional')
                ch=input('enter your choice').upper()
                if ch =='E':
                    f=int(input('enter correct marks for english'))
                    e[9]=f
                elif ch =='EC':
                    f=int(input('enter correct marks for economics'))
                    e[20]=f
                elif ch =='A':
                    f=int(input('enter correct marks for accounts'))
                    e[21]=f
                elif ch =='B':
                    f=int(input('enter correct marks for B.st'))
                    e[22]=f
                elif ch =='O':
                    f=int(input('enter correct marks for optional'))
                    e[25]=f
            elif i[8]=='ar':
                print('press E to update marks of English')
                print('press EC to update marks of economics')
                print('press PO to update marks of Pol.science')
                print('press G to update marks of Geography')
                print('press O to update marks of Optional')
                ch=input('enter your choice').upper()
                if ch =='E':
                    f=int(input('enter correct marks for english'))
                    e[9]=f
                elif ch =='EC':
                    f=int(input('enter correct marks for economics'))
                    e[20]=f
                elif ch =='PO':
                    f=int(input('enter correct marks for Pol.science'))
                    e[23]=f
                elif ch =='G':
                    f=int(input('enter correct marks for Geography'))
                    e[24]=f
                elif ch =='O':
                    f=int(input('enter correct marks for optional'))
                    e[25]=f
                    
            print('updated record ',e)
            cnt=1
        k.append(e)
    if cnt==1:
        fobjt.close()
        fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
        writer=csv.writer(fobjt2)
        for i in range(len(k)):
            writer.writerow(k[i])
        fobjt2.close()
    else:
        sys.stderr.write('no such record found whosemarks to be updated \n')
        
def classchecker610(z):
    global k
    k=z
    if z not in ['6','7','8','9','10']:
        sys.stderr.write('initialised class is invalid as function is for class 6th to 10th \n')
        z=input('enter class').strip()
        k=z
        classchecker610(z)
    else:
        return (k)

                  
def updatemrk610(kv):
    '''update marks of student of class 6th to 10th. one student at a particular time'''
    fobjt=open('d:\\school management\\sturec.csv','r')
    reader=csv.reader(fobjt)
    a=input('enter student\'s name').title().strip()
    b=input('enter student\'s adm no.').upper().strip()
    c=kv
    c=classchecker610(c)
    k=[]
    cnt=0
    for i in reader:
        e=i
        if e[0]==a and e[3]==c and e[6]==b:
            print('old record',e)
            print('press E to update marks of English')
            print('press M to update marks of maths')
            print('press SC to update marks of Science')
            print('press H to update marks of Hindi')
            print('press C to update marks of Computer')
            print('press SS to update marks of S.St')
            ch=input('enter your choice').upper()
            if ch =='E':
                f=int(input('enter correct marks for english'))
                e[9]=f
            elif ch =='M':
                f=int(input('enter correct marks for maths'))
                e[10]=f
            elif ch =='SC':
                f=int(input('enter correct marks for science'))
                e[11]=f
            elif ch =='H':
                f=int(input('enter correct marks for hindi'))
                e[13]=f
            elif ch =='C':
                f=int(input('enter correct marks for computer'))
                e[12]=f
            elif ch =='SS':
                f=int(input('enter correct marks for S.St'))
                e[14]=f
            cnt=1
            print('updated record->',e)
        k.append(e)
    if cnt==1:
        fobjt.close()
        fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
        wrtr=csv.writer(fobjt2)
        for i in range(len(k)):
            wrtr.writerows(k[i])
        fobjt2.close()
    else:
        sys.stderr.write('no such record present to be updated\n')

def classchecker15(z):
    global k 
    k=z
    if z not in ['1','2','3','4','5']:
        sys.stderr.write('initialised class is invalid as function is for class 1st to 5th \n')
        z=str(input('enter class')).strip()
        k=z
        classchecker15(z)
    else:
        return k

    
def updatemrk15(kv):
    '''update marks of student of class 1st to 5th. one student at a particular time'''
    fobjt=open('d:\\school management\\sturec.csv','r')
    reader=csv.reader(fobjt)
    a=input('enter student\'s name').title().strip()
    b=input('enter student\'s adm no.').upper().strip()
    c=kv
    c=classchecker15(c)
    k=[]
    cnt=0
    for i in reader:
        e=i
        if e[0]==a and e[3]==c and e[6]==b:
            print('old record',e)
            print('press E to update marks of English')
            print('press M to update marks of Maths')
            print('press EV to update marks of EVST')
            print('press H to update marks of Hindi')
            print('press C to update marks of Computer')
            print('press G to update marks of G.K')
            ch=input('enter your choice').upper()
            if ch =='E':
                f=int(input('enter correct marks for english'))
                e[9]=f
            elif ch =='M':
                f=int(input('enter correct marks for maths'))
                e[10]=f
            elif ch =='EV':
                f=int(input('enter correct marks for EVST'))
                e[16]=f
            elif ch =='H':
                f=int(input('enter correct marks for hindi'))
                e[13]=f
            elif ch =='C':
                f=int(input('enter correct marks for computer'))
                e[12]=f
            elif ch =='G':
                f=int(input('enter correct marks for GK'))
                e[15]=f
            cnt=1
            print('updated record->',e)
        k.append(e)
    if cnt==1:
        fobjt.close()
        fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
        wrtr=csv.writer(fobjt2)
        for i in range(len(k)):
            wrtr.writerow(k[i])
        fobjt2.close()      
    else:
        sys.stderr.write('no such record present to be updated')

        
def rec_deleters():
    '''it will delete !!! record of a particular student'''
    sys.stderr.write('are you sure to delete this record !!! (y/n)')
    ch=input().strip()
    if ch=='y' or ch=='y':
        a=input('enter student\'s name').title().strip()
        a=namechecker(a,' student\'s ')
        b=input('enter admission no.').upper().strip()
        fobjt=open('d:\\school management\\sturec.csv')
        readers=csv.reader(fobjt)
        k=[]
        for i in readers:
            e=i
            if e[0]==a and e[6]==b:
                print('record found and deleted')
            else:
                k.append(e)
        fobjt.close()
        fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
        writer=csv.writer(fobjt2)
        for i in range(len(k)):
            writer.writerow(k[i])
        fobjt2.close()
    else:
        print('OK')

        
#Teacher's data
filet=os.path.isfile('d:\\school management\\tchrrec.csv')
if filet==False:
    a=open('d:\\school management\\tchrrec.csv','a',newline='')
    b=csv.writer(a)
    c=["teacher's Name","teacher's id",'salary','phone number','subject alloted','classes alloted']
    b.writerow(c)
    a.close()   

def tchridchecker(z):
    a=0
    with open('d:\\school management\\tchrrec.csv') as fobjt:
        idread=csv.reader(fobjt)
        global b
        for i in idread:
            e=i
            if e[1]==z:
                sys.stderr.write('this no. is already taken \n')
                k=input('enter different id.').upper().strip()
                a+=1
                b=k
        if z=='':
                sys.stderr.write('you can\'t leave teacher Id\'s blank \n')
                k=input('enter Teacher\'s id').upper().strip()
                a+=1
                b=k
        if a!=0:
            tchridchecker(k)
        else:
            b=z
    return(b)


def enttr():
    '''enter new record of a teacher '''
    fobjt=open('d:\\school management\\tchrrec.csv','a',newline='')
    writert=csv.writer(fobjt)
    a3=int(input('enter no. of records you want to enter'))
    for i in range(a3): 
        a=input("enter teacher's name").title().strip()
        a=namechecker(a,' Teacher\'s ')
        ch=input('do you need auto generated tchr id no.(y/n)').lower().strip()
        if ch=='y':
             b=tchrid_maker() 
        elif ch=='n':
            print('OK')
            b=input("enter teacher' id").upper().strip()
        b=tchridchecker(b)
        print('Teacher Id given is----->',b)
        c=int(input('enter salary'))
        d=int(input('enter phone no.'))
        e=eval(input("enter subject alloted within square brackets'[]' and name of sub. in quotes ").title().strip())
        f=eval(input('enter classes alloted within square brackets"[]"'))
        g=[a,b,c,d,e,f]
        writert.writerow(g)
        fobjt.flush()
    fobjt.close()


def reatr():
    '''enter whole record of teacher data '''
    fobjt=open('d:\\school management\\tchrrec.csv')
    readert=csv.reader(fobjt)
    for i in readert:
        print(i)
    fobjt.close()


def sert():
    '''this function can search for a teacher in 4 different situations '''
    fobjt=open('d:\\school management\\tchrrec.csv')
    readert=csv.reader(fobjt)
    print('press n to search by name')
    print('press ti to search by teacher id')
    print('press pct to search teacher of a particular class ')
    print('press pst to search teacher of a particular subject ')
    a=input('enter your choice')
    if a == 'n':
        b=input('enter Teacher\'s name').title().strip()
        b=namechecker(b,' Teacher\'s ')
        for i in readert:
            if i[0]==b:
                print(i)
    elif a=='ti':
        b=input('enter Teacher\'s Id').upper().strip()
        for i in readert:
            if i[1]==b:
                print(i)
    elif a == 'pct':
            b=input('enter class for which you want to search teacher ')
            for i in readert:
                if b in i[5]:
                        print(i)
    elif a=='pst':
        b=input('enter subject for which you want to search teacher in quotes').title().strip()
        for i in readert:
            if b in list(i[4]):
                print(i)
    fobjt.close()

    
def updatetr():
    '''it will update teacher record. 1 record at once'''
    fobjt=open('d:\\school management\\tchrrec.csv')
    readert=csv.reader(fobjt)
    a=input('enter Teacher\'s name').title().strip()
    a=namechecker(a,' Teacher\'s ')
    b=input('enter Teacher id').upper().strip()
    c=[]
    cnt=0
    for i in readert:
        e=i
        if e[0]==a and e[1]==b:
            print('old record',e)
            print('press  n  to update name')
            print('press  ti  to update teacher id')
            print('press  s  to update salary')
            print('press  p  to update phone no.')
            print('press  cl  to update class of a particular teacher')
            print('press  sb  to update subject of a particular teacher')
            chn=input('enter your choice').lower().strip()
            if chn=='n':
                f=input('enter correct name').title().strip()
                f=namechecker(f,' student\'s ')
                e[0]=f
            elif chn=='ti':
                ch=input('do you want auto generated(y/n)').strip()
                if ch=='y' or ch=='Y':
                     f=tchrid_maker()
                else:
                    print("OK")
                    f=input('enter correct Id no.').upper().strip()
                f=tchridchecker(f)
                e[1]=f
            elif chn=='s':
                f=int(input('enter correct salary'))
                e[2]=f
            elif chn=='p':
                f=int(input('enter correct phone no.'))
                e[3]=f
            elif chn=='sb':
                f=eval(input('enter correct subject alloted in sq bracket "[]" and name of subject in quotes ').title().strip())
                e[4]=f
            elif chn=='cl':
                f=eval(input('enter correct class alloted in sq bracket"[]"'))
                e[5]=f
            print('new record',e)
            c.append(e)
            cnt=1
    if cnt==1:
        fobjt.close()
        fobjt2=open('d:\\school management\\tchrrec.csv','w',newline='')
        writer=csv.writer(fobjt2)
        for i in range(len(c)):
            writer.writerow(c[i])
        fobjt2.close()
    else:
        sys.stderr.write('no such record found')

def rec_deletert():
    '''it will delete record of a particular teacher once at a time'''
    sys.stderr.write('are you sure to delete this record !!! (y/n)')
    ch=input().strip()
    if ch=='y' or ch=='y':
        a=input('enter teacher\'s name').title().strip()
        a=namechecker(a,' Teacher\'s ')
        b=input('enter Teacher id').upper().strip()
        fobjt=open('d:\\school management\\tchrrec.csv')
        readert=csv.reader(fobjt)
        k=[]
        for i in readert:
            e=i
            if (e[0]!=a and e[1]!=b):
                k.append(e)
        fobjt.close()
        fobjt2=open('d:\\school management\\tchrrec.csv','w',newline='')
        writer=csv.writer(fobjt2)
        for i in range(len(k)):
            writer.writerow(k[i])
        fobjt2.close()
    else:
        print('OK')

def tchrid_maker():
    a='T'
    b=str(random.randint(00000,99999))
    if len(b)<5:
        c='0'*(5-len(b))
        d=a+c+b
    else:
        d=a+b
    return d

def backupst():
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        k.append(i)
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec2.csv','w',newline='')
    write=csv.writer(fobjt2)
    for i in range(len(k)):
        write.writerow(k[i])
    fobjt2.close()
    
def backuptc():
    fobjt=open('d:\\school management\\tchrrec.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        k.append(i)
    fobjt.close()
    fobjt2=open('d:\\school management\\tchrrec2.csv','w',newline='')
    write=csv.writer(fobjt2)
    for i in range(len(k)):
        write.writerow(k[i])
    fobjt2.close()

def restorest():
    fobjt=open('d:\\school management\\sturec2.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        k.append(i)
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
    write=csv.writer(fobjt2)
    for i in range(len(k)):
        write.writerow(k[i])
    fobjt2.close()
    
def restoretc():
    fobjt=open('d:\\school management\\tchrrec2.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        k.append(i)
    fobjt.close()
    fobjt2=open('d:\\school management\\tchrrec.csv','w',newline='')
    write=csv.writer(fobjt2)
    for i in range(len(k)):
        write.writerow(k[i])
    fobjt2.close()

def encoder(a):
    e=''
    a=str(a).lower()
    for i in a:
        if ord(i) in range(97,106):
            if ord(i)!=98 and ord(i)!=103:
                c=ord(i)-64
            elif ord(i)==98:
                c=43
            elif ord(i)==103:
                c=45
        elif ord(i) in range(106,116):
            c=ord(i)-58
        elif ord(i) in range(116,123):
            c=ord(i)-56
        elif ord(i)==32:
            c=126
        elif ord(i) in range(48,58):
            c=ord(i)+19
        elif ord(i)==61:
            c=77
        elif ord(i)==46:
            c=94
        else:
            print(i,'you can\'t use this letter please correct it')
        e=e+chr(c)
    f=e
    return f

def encode():
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        k.append(i)
    for i in range(len(k)):
        for j in range(len(k[i])):
            k[i][j]=encoder(k[i][j])
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
    write=csv.writer(fobjt2)
    for i in range(len(k)):
        write.writerow(k[i])
    fobjt2.close()


def decoder(a):
    e=''
    for i in a:
        if ord(i) in range(33,42):
            if ord(i)!=34 and ord(i)!=39:
                c=ord(i)+64
        elif ord(i) in range(48,58):
            c=ord(i)+58
        elif ord(i) in range(60,67):
            c=ord(i)+56
        elif ord(i)==126:
            c=32
        elif ord(i)==43:
            c=98
        elif ord(i)==45:
            c=103
        elif ord(i) in range(67,77):
            c=ord(i)-19
        elif ord(i)==77:
            c=61
        elif ord(i)==94:
            c=46
        else:
            print('Oops!! you entered wrong letter and the letter is',i)
        e=e+chr(c)
        e=e.lower()
        if e in ['co','ar','md','nm','nil']:
            e=e.lower()
        elif e not in ['co','ar','md','nm','nil']:
            e=e.title()
    f=e
    return f

def decode():
    fobjt=open('d:\\school management\\sturec.csv')
    read=csv.reader(fobjt)
    k=[]
    for i in read:
        k.append(i)
    for i in range(len(k)):
        for j in range(len(k[i])):
            k[i][j]=decoder(k[i][j])
    fobjt.close()
    fobjt2=open('d:\\school management\\sturec.csv','w',newline='')
    write=csv.writer(fobjt2)
    for i in range(len(k)):
        write.writerow(k[i])
    fobjt2.close()

fobjt=open('d:\\school management\\sturec.csv')
rd=csv.reader(fobjt)
e=[]
for i in rd:
    e.append(i)
if e[0][0]=='Name':
    code='decoded'
elif e[0][0]=='4!3%' :
    code='encoded'

def pssdeleter():
        ch=input('Are you sure that you want to delete your password(y/n)').strip().lower()
        if ch=='y':
                if os.path.isfile('d:\\school management\\alpha.txt'):
                    a=open('d:\\school management\\alpha.txt')
                    rd=a.read()
                    a.close()
                    if 'alphapsswrd1' in rd:
                        print('but first give your old identification i.e your passowrd for verification in fields mentioned below')
                        chk=psscheck()
                        if chk==True:
                             direc='d:\\school management\\dont delete me.dat'
                             if os.path.isfile(direc):
                                    os.remove(direc)
                                    fobjt=open('d:\\school management\\alpha.txt','w')
                                    fobjt.write('alphapsswrd0')
                                    fobjt.close()
                                    fobjt2=open('d:\\school management\\yn.txt','w')
                                    fobjt2.write('n')
                                    fobjt2.close()
                                    print('your password is deleted... Next time you need not to enter any password')
                             else:
                                    print('You already deleted the password')
                    else:
                        print('You already deleted the password or you don\'t even set any password yet')
                
        elif ch=='n':
                print('Ok')
        else:
                print('OOPS!!! You entered wrong key')
                pssdeleter()  
                            
def entry():
        while True:
                direc=os.path.isfile('d:\\school management\\alpha.txt')
                if direc==True:
                    a=open('d:\\school management\\alpha.txt')
                    br=a.read()
                    a.close()
                    if 'alphapsswrd1' in br:
                            c=psscheck()
                    elif 'alphapsswrd0' in br:
                            c=True
                    break
                elif direc==False:
                    while True:
                        print('it seems you deleted password file ')
                        choice=input('do you want to save for a passowrd(y/n)').lower().strip()
                        if choice=='y':
                                password()
                                break
                        elif choice=='n':
                            alphapsswrd='alphapsswrd0'
                            a=open('d:\\school management\\alpha.txt','w')
                            a.write(alphapsswrd)
                            a.close()
                            break
                        else:
                                print('Ooops you entered wrong key')
        return c
def query():
    d=entry()
    if d==True:
        while True:
            global code
            sys.stderr.write(' enter s to work in student\'s data \n press t for working in teacher\'s data \n')
            sys.stderr.write(' press bs to save a checkpoint for students data \n bt to save a checkpoint for teacher data \n')
            sys.stderr.write(' press rs to restore the students data to nearest checkpoint\n')
            sys.stderr.write(' press rt to restore teacher\'s data to nearest checkpoint \n')
            sys.stderr.write(' press d to decode the file \n')
            sys.stderr.write(' press e to encode the file \n')
            sys.stderr.write(' press rsp to reset or to apply the password \n')
            sys.stderr.write(' press psd to delete the password \n')
            sys.stderr.write(' press q to quit \n')
            ch=input('enter your choice').lower().strip()
            if ch=='s':
                if code=='encoded':
                    decode()
                    b='y'
                else:
                    b='n'
                print('press 1 for entering records')
                print('press 2 for reading all records')
                print('press 3 for searching a particular record')
                print('press 4 for updating  records')
                print('press 5 for getting results of whole class')
                print('press 6 for entering marks')
                print('press 7 for anyone\'s particular record')
                print('press 8 for updating marks')
                print('press 9 for deleting records')
                sys.stderr.write('enter your choice')
                choice=int(input())
            
                if choice==1:
                    wrtsr()
            
                elif choice==2:
                    if b=='y':
                        encode()
                        c='y'
                    else:
                        c='n'
                    reasr()
                    if c=='y':
                        decode()
                elif choice==3:
                    sers()
            
                elif choice==4:
                     updatesr()
             
                elif choice==5:
                    a=input('enter class').strip()
                    a=classlimit(a)
                    if a in ['1','2','3','4','5']:
                        rslt15(a)
                    elif a in ['6','7','8','9','10']:
                        rslt610(a)
                    elif a=='11':
                        rslt11()
                    elif a=='12':
                        rslt12()
                
                elif choice==6:
                    a=input('enter class').strip()
                    a=classlimit(a)
                    if a in ['1','2','3','4','5']:
                        wrtmrks15(a)
                    elif a in ['6','7','8','9','10']:
                        wrtmrks610(a)
                    elif a in ['11','12']:
                        wrtmrks1112(a)
                
                elif choice==7:
                    rsltprtclr()
            
                elif choice==8:
                    a=input('enter class').strip()
                    a=classlimit(a)
                    if a in ['1','2','3','4','5']:
                        updatemrk15(a)
                    elif a in ['6','7','8','9','10']:
                        updatemrk610(a)
                    elif a in ['11','12']:
                        updatemrk1112(a)
                
                elif choice==9:
                    rec_deleters()
                else:
                    print('wrong input')
                if b=='y':
                    encode()

            elif ch=='t':
                if code=='encoded':
                    decode()
                    b='y'
                else:
                    b='n'
                print('press 1 for entering records')
                print('press 2 for reading all records')
                print('press 3 for searching a particular record')
                print('press 4 for updating  records')
                print('press 5 for deleting records')
                sys.stderr.write('enter your choice')
                choice=int(input())
                if choice==1:
                    enttr()
                elif choice==2:
                    if b=='y':
                        encode()
                        c='y'
                    else:
                        c='n'
                    reatr()
                    if c=='y':
                        decode()
                elif choice ==3:
                    sert()
                elif choice==4:
                    updatetr()
                elif choice==5:
                   rec_deletert()
                else:
                    print('wrong input')
                if b=='y':
                    encode()

            elif ch=='bs':
                backupst()
            elif ch=='bt':
                backuptc()
            
            elif ch=='rs':
                restorest()
            elif ch=='rt':
                restoretc()
                
            elif ch=='q':
                sys.stderr.write('Are you sure that you want to exit from query mode(y/n)')
                a=input().lower().strip()
            
                if a =='y':
                    print('if you want to enter again in query mode enter function name')
                    sys.stderr.write('query()')
                    direc=os.path.isfile('d:\\school management\\alpha.txt')
                    if direc==True:
                        a=open('d:\\school management\\alpha.txt')
                        b=a.read()
                        a.close()
                        if 'alphapsswrd1' in b and code=='decoded':
                                encode()
                                code='encode'
                    break
                else:
                    print('OK')
                
            elif ch=='e':
                if code=='decoded':
                    encode()
                    code='encoded'
                    print('your file is encoded')
                else:
                    print('\n file is already encoded \n')
                
            elif ch=='d':
                if code=='encoded':
                    decode()
                    print('your file is decoded')
                    code='decoded'
                else:
                    print('\n file is already decoded \n')
            elif ch=='rsp':
                if os.path.isfile('d:\\school management\\alpha.txt'):
                    a=open('d:\\school management\\alpha.txt')
                    rd=a.read()
                    a.close()
                    if len(rd)==0:
                        password()
                    else:
                        if 'alphapsswrd1' in rd:
                            print('but first give your old identification i.e your passowrd for verification in fields mentioned below')
                            chk=psscheck()
                            if chk==True:
                                print('now you are eligible to renewate your password') 
                                password()
                            else:
                                sys.stderr.write('you entered wrong identification\n\n')
                        elif 'alphapsswrd0' in rd:
                            print('Smart Choice one should save his/her file with password')
                            print('but remember not to forget it.')
                            password()
                else:
                    password()
        
            elif ch=='psd':
                    pssdeleter()
                    
            else:
                print('wrong!!! input')
                print('\n')
        backuptc()
        backupst() 
print('you are currently in the query mode')
query()