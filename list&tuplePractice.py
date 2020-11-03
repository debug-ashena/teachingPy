numbers= [2,4,6,8,12,14,16,("test","pre-test"),18]
count=0






#Susan:
for n in numbers:
    if type(n) is tuple:
        break
    count +=1
    print(count)
#---------------------------------
#selma
numbers= [2,4,6,8,12,14,16,("test","pre-test"),18]

count = list(map(type, numbers)).index(tuple)

print(count)
