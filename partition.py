'''
list-------------------
append
extend
clear
pop
insert
sort
reverse
index
count

touple-----------------
index
count

set---------------------
 add
 update
 insertion
 insertion update
 diffrence
 diffrence upate
 sym diff
 sym diff update
 clear
 pop
 remove
 replace
 isdiscard
 issubset
 issuperset
 union

 string---------------------
 upper
 lower
 reversre
 format
 partition
 clear
 pop
 stratswith
 endwith
 count
 find
 strip
  l strip
  r strip
 title
 capitalize
 isspace
 isupper
 islower
 istitle
 isalpha
 isalnum
 isdigit

 dictinory------------------------------------
 add
 update
 clear
 keys
 values
 insert
 pop
 pop.items
 GET
 SETDEFAULT



 '''

f= open('employee.txt','a+')
'''
for i in range (int(input('enter the no. of entries'))):
    id=int(input('enter id'))
    age=int(input('enter age'))
    sal=int(input('enter salary'))
    nam=input('enter the name')
    s=f'{id} | {nam} | {age} | {sal} | \n'
    f.write(s)
f.close()
'''
print(f.readlines())
f.seek(0)
l=[]
for i in f.readlines()[1:]:
    i1=i.split('|')
    p=i1[1]
    l.append(p)
p=''
d={}
s=''
for j in l:
    p+=j
print(p)
for k in p:
    if not k.isspace():
        d[k]=p.count(k)
print(d)
