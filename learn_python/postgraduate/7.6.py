w=80
print('-'*w)
print('1\t2\t3\t4\t5\t6\t7\t8\t9\t10')
print('-'*w)
for x in range(1, 11):
    for y in range(1, 11):
        print (x*y, end = "\t")
print('*'*w)
