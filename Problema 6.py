a = input("Alegeti un numar mai mic de 10000: ")
b = 10000
print ("%d vs %d" % (int(a),int(b)))
if int(a)>int(b) :
    print("Alegeti un numar mai mic ca 10000")
    a = input("Un numar mai mic ca 10000: ")
    c = int(a)//9
    d = int(a)%9
    e = 1/int(a)
    print(c,d,e)
else :
    c = int(a)//9
    d = int(a)%9
    e = 1/int(a)
    print(c,d,e)