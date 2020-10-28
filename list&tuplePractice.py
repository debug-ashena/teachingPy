numbers= [2,4,6,8,12,14,16,("test","pre-test"),18]
count=0
for n in numbers:
    if isinstance(n, tuple):
        break
    count +=1
    print(count)
