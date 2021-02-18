##l=[('a',5),('b',3),('c',1),('h',10)]
####print(type(l))
####for i in l:
######   print(i)
####def sorted_touple(l):
####   print (sorted(l,key = lambda x:x[1]))
####sorted_touple(l)
##lst=len(l)
##print(lst)
##l.sort(key =lambda x:x[1])
####print(l)
##def func(x):
##    def jok(y):
####        return x*y
####    return jok()
##ob=func(10)
##print(ob(10))

##def mul(login):
##    def add(un,pw):
##        if un=='admin' and pw=='1234':
##            return login(un,pw)
##        else:
##            return 'user/password is wrong'
##    return add
##@mul
##def auth(unam,upassw):
##    return f'{unam} is logged'
##print(auth(input('enter uname:'),input('enter password:')))
##      
###print(auth(input('enter the username:')),input('enter password:'))


def auth(LOG):
    def verify(uname,passw):
        if uname=='nihal' and passw=='password':
            return LOG(uname,passw)
        else:
            return 'uname or password is wrong'
    return verify
@auth
def creds(user,passd):
    return f'{user} successfully logged in'
print(creds(input('enter username:'),input('enter password:')))
