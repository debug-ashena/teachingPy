try:
    print(shopinglist[2])
except IndexError as e:
    print('exception :' + str(e) + 'has Occured')
else:
    print('no exception Occured ')
finally:
    print('i will always execute no matter what')