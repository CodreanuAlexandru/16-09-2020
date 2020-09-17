a = input("Alegeti un numar mai mic de 10000: ")
b = 10000
print ("%d vs %d" % (int(a),int(b)))
if int(a)>int(b) :
    print("Alegeti un numar mai mic ca 10000")
    a = input("Un numar mai mic ca 10000: ")
    c = int(a)%10
    d = int (a)%100//10
    e = int(a)//9
    f = int(a)%9
    h = int(a)%10000//1000+int(a)%1000//100+int(a)%100//10+int(a)%10
    print( c ,"\n",d,"\n",e,"\n",f,"\n",h,"\n",int(a)%10,int(a)%100//10,int(a)%1000//100,int(a)%10000//1000)
else :
    c = int(a)%10
    d = int (a)%100//10
    e = int(a)//9
    f = int(a)%9
    h = int(a)%10000//1000+int(a)%1000//100+int(a)%100//10+int(a)%10
    print( c ,"\n",d,"\n",e,"\n",f,"\n",h,"\n",int(a)%10,int(a)%100//10,int(a)%1000//100,int(a)%10000//1000)