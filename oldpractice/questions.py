

a = [1,2,1,3,4,3,3,5]

# for i in enumerate(a):
#
#  print(i)



# question 1
# tel={}
# for i in a:
#  if i not in tel:
#   tel[i]=1
#  else:
#   tel[i]+=1
# print(tel)

{1:2,2:1,3:3,4:1,5:1}


a= "abccba"
leng = len(a)
print(leng)
for i in range(0,leng//2):
 if a[i]==a[leng-i-1]:
  print("yes pallindrome")
 else:
  print("not")

