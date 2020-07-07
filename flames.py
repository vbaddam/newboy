#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time

tag = 'welcome to flames'
print(tag.center(40,' ').upper())
time.sleep(.5)
tag1 = 'enter first name:'
tag2 = 'enter second name:'

print(tag1.center(39,' ').title())
name1 = input().lower()
time.sleep(.5)
print(tag2.center(39,' ').title())
name2 = input().lower()
l1 = len(name1)
l2 = len(name2)
length = l1+l2


list1 = []
for l1 in range(0,len(name1)):
 if name1[l1] in name2:
  list1.append(name1[l1])
  
for l2 in range(0,len(name2)):
 if name2[l2] in name1:
  list1.append(name2[l2])
  
length0 = length-len(list1)

def length(num,fate):
 
 if length0 == num:
  print(fate)
 return

length(1,'s')
length(2,'e')
length(3,'f')
length(4,'e')
length(5,'f')
length(6,'m')
length(7,'e')
length(8,'a')
length(9,'e')
length(10,'l')
length(11,'m')
length(12,'a')
length(13,'a')
length(14,'f')
length(15,'m')
length(16,'f')
length(17,'a')
length(18,'f')
length(19,'l')
length(20,'e')
length(21,'f')
length(22,'e')
length(23,'f')
length(24,'f')
length(25,'m')









