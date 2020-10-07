print("(1). f(xy)= ax^ny^m")
print("(2). f(x)= at^n(x) ; t=(sin,cos,tan,cosec,sec,cot)")
print("(3). f(x)= aln(bx)")
print("(4). f(x)= aln(bx)t^n(cx) ; t=(sin,cos,tan,cosec,sec,cot)")
print("(5). f(x)= ax^(nx^m)")
print("(6). f(xy)= {(ax^n y^n1 + bx^n2 y^n3)/(cx^n4 y^n5 + dx^n6 y^n7)}^n8")
print("(7). f(x) = e^(x^n)t^m(cx) ; t=(sin,cos,tan,cosec,sec,cot)")
print("(8). f(x)= at^-1(cx) ; t=(sin,cos,tan,cosec,sec,cot)")
print("Got a different question, try below.")
print("(9).Enter your question: ")
_a=int(input("Enter the no:"))
if(_a==1):
   a=int(input("Enter the a:"))
   n=int(input("Enter the n:"))
   m=int(input("Enter the m:"))
   if(n !=0 and m !=0):
       i=0
       z=[1,2,3,4,5,6,7,8,9,10]
       while(i<len(z)):
           if(a==z[i]):
               n1= a*n
               n2= a*m
               if((m-1)==0):
                   print("f'(xy)=",n1,"x^",(n-1),"y","+",n2,"x^",n,"dy/dx")
               elif((m-1)==1):
                   print("f'(xy)=",n1,"x^",(n-1),"y^",m,"+",n2,"x^",n,"y","dy/dx")
               elif((n-1)==0):
                   print("f'(xy)=",n1,"y^",m,"+",n2,"x","y^",(m-1),"dy/dx")
               elif((n-1)==1):
                   print("f'(xy)=",n1,"x","y^",m,"+",n2,"x^",n,"y^",(m-1),"dy/dx")
               elif((n-1)==0 and (m-1)==0):
                   print("f'(xy)=",n1,"y","+",n2,"x","dy/dx")
               elif((n-1)==1 and (m-1)==1):
                   print("f'(xy)=",n1,"x","y^",m,"+",n2,"x^",n,"y","dy/dx")
               else:
                   print("f'(xy)=",n1,"x^",(n-1),"y^",m,"+",n2,"x^",n,"y^",(m-1),"dy/dx")
           i+=1
   elif(m==0):
       j=0
       g=[1,2,3,4,5,6,7,8,9,10]
       while(j<len(g)):
           if(a==g[j]):
              n1= a*n
              if((n-1)==0):
                  print("f'(x)=",n1)
              else:
                  print("f'(x)=",n1,"x^",(n-1))
       j+=1
elif(_a==2):    
   print("(1).f(x)=asin^n(bx)")
   print("(2).f(x)=acos^n(bx)")
   print("(3).f(x)=atan^n(bx)")
   print("(4).f(x)=acosec^n(bx)")
   print("(5).f(x)=asec^n(bx)")
   print("(6).f(x)=acot^n(bx)")
   l=int(input("Enter the no."))
   if(l== 1):
       a2=int(input("Enter the a:"))
       n2=int(input("Enter the n:"))
       b=int(input("Enter the b:"))
       c=a2*n2*b
       if(n2>2 and b!=1):
          print("f'(x)=",c,'sin^',(n2-1),'(',b,'x)','cos(',b,'x)')
       elif(n2<=2 and b!=1):
           print("f'(x)=",c,'sin(',b,'x)','cos(',b,'x)')
       elif(n2==1 and b!=1):
          print("f'(x)=",c,'cos(',b,'x)')
       elif(n2>1 and b==1):
          print("f'(x)=",c,'sin^',(n2-1),'(x)','cos(x)')
       elif(n2==1 and a2==1 and b==1):
          print("f'(x)= cos(x)")
       elif(n2==1 and a2==1 and b!=1):
           print("f'(x)=",c,'cos(',b,'x)')
       elif(n2==1 and b==1 and a2!=1):
           print("f'(x)=",c,'cos(x)')
   elif(l==2):
       a2=int(input("Enter the a:"))
       n2=int(input("Enter the n:"))
       b=int(input("Enter the b:"))
       c=a2*n2*b
       if(n2>2 and b!=1):
          print("f'(x)=",-c,'cos^',(n2-1),'(',b,'x)','sin(',b,'x)')
       elif(n2<=2 and b!=1):
           print("f'(x)=",-c,'cos(',b,'x)','sin(',b,'x)')
       elif(n2==1 and b!=1):
          print("f'(x)=",-c,'sin','(',b,'x)')
       elif(n2>1 and b==1):
          print("f'(x)=",-c,'cos^',(n2-1),'(x)','sin(x)')
       elif(n2==1 and a2==1 and b==1):
          print("f'(x)= -sin(x)")
       elif(n2==1 and a2==1 and b!=1):
          print("f'(x)=",-c,'sin','(',b,'x)')
       elif(n2==1 and b==1 and a2!=1):
          print("f'(x)=",-c,'sin(x)')
   elif(l==3):
       a2=int(input("Enter the a:"))
       n2=int(input("Enter the n:"))
       b=int(input("Enter the b:"))
       c=a2*n2*b
       if(n2>2 and b!=1):
          print("f'(x)=",c,'tan^',(n2-1),'(',b,'x)','sec^2(',b,'x)')
       elif(n2<=2 and b!=1):
          print("f'(x)=",c,'tan(',b,'x)','sec^2(',b,'x)')
       elif(n2==1 and b!=1):
          print("f'(x)=",c,'sec^2(',b,'x)')
       elif(n2>1 and b==1):
          print("f'(x)=",c,'tan^',(n2-1),'(x)','sec^2(x)')
       elif(n2==1 and a2==1 and b==1):
          print("f'(x)= sec^2(x)")
       elif(n2==1 and a2==1 and b!=1):
          print("f'(x)=",c,'sec^2(',b,'x)')
       elif(n2==1 and b==1 and a2!=1):
           print("f'(x)=",c,'sec^2(',b,'x)')
   elif(l==4):
       a2=int(input("Enter the a:"))
       n2=int(input("Enter the n:"))
       b=int(input("Enter the b:"))
       c=a2*n2*b
       if(n2>2 and b!=1):
          print("f'(x)=",-c,'cosec^',(n2-1),'(',b,'x)','cot(',b,'x)','cosec(',b,'x)')
       elif(n2<=2 and b!=1):
          print("f'(x)=",-c,'cosec(',b,'x)','cot(',b,'x)','cosec(',b,'x)')
       elif(n2==1 and b!=1):
          print("f'(x)=",-c,'cot(',b,'x)','cosec(',b,'x)')
       elif(n2>1 and b==1):
          print("f'(x)=",-c,'cosec^',(n2-1),'(x)','cot(x)','cosec(x)')
       elif(n2==1 and a2==1 and b==1):
          print("f'(x)= -cot(x)cosec(x)")
       elif(n2==1 and a2==1 and b!=1):
          print("f'(x)=",-c,'cot(',b,'x)','cosec(',b,'x)')
       elif(n2==1 and b==1 and a2!=1):
          print("f'(x)=",-c,'cot(x)cosec(x)')
   elif(l==5):
       a2=int(input("Enter the a:"))
       n2=int(input("Enter the n:"))
       b=int(input("Enter the b:"))
       c=a2*n2*b
       if(n2>2 and b!=1):
          print("f'(x)=",c,'sec^',(n2-1),'(',b,'x)','sec(',b,'x)','tan(',b,'x)')
       elif(n2<=2 and b!=1):
          print("f'(x)=",c,'sec^2','(',b,'x)','tan(',b,'x)')
       elif(n2==1 and b!=1):
          print("f'(x)=",c,'sec(',b,'x)','tan(',b,'x)')
       elif(n2>1 and b==1):
          print("f'(x)=",c,'sec^',(n2-1),'(x)','sec(x)','tan(x)')
       elif(n2==1 and a2==1 and b==1):
          print("f'(x)= sec(x)tan(x)")
       elif(n2==1 and a2==1 and b!=1):
          print("f'(x)=",c,'sec(',b,'x)','tan(',b,'x)')
       elif(n2==1 and b==1 and a2!=1):
          print("f'(x)=",c,'sec(x)tan(x)')
   elif(l==6):
       a2=int(input("Enter the a:"))
       n2=int(input("Enter the n:"))
       b=int(input("Enter the b:"))
       c=a2*n2*b
       if(n2>1 and b!=1):
          print("f'(x)=",-c,'cot^',(n2-1),'(',b,'x)','cosec^2(',b,'x)')
       elif(n2<=2 and b!=1):
          print("f'(x)=",-c,'cot(',b,'x)','cosec^2(',b,'x)')
       elif(n2==1 and b!=1):
          print("f'(x)=",-c,'cosec^2','(',b,'x)')
       elif(n2>1 and b==1):
          print("f'(x)=",-c,'cot^',(n2-1),'(x)','cosec^2','(x)')
       elif(n2==1 and a2==1 and b==1):
          print("f'(x)= -cosec^2(x)")
       elif(n2==1 and a2==1 and b!=1):
          print("f'(x)=",-c,'cosec^2(',b,'x)')
       elif(n2==1 and b==1 and a2!=1):
          print("f'(x)=",-c,'cosec^2','(x)')
elif(_a==3):
   a3=int(input("Enter the a:"))
   b3=int(input("Enter the b:"))
   c= a3*b3
   if(a3>=2 and b3>=2):
      print("f'(x)=",c,'/(',b3,'x)')
   elif(a3>=2 and b3==1):
      print("f'(x)=",c,'/x')
   elif(a3==1 and b3==1):
      print("f'(x)= 1/x")
elif(_a==4):
    a4=int(input("Enter the a:"))
    b4=int(input("Enter the b:"))
    t =input("Enter the t:")
    n4=int(input("Enter the n:"))
    b=int(input("Enter the c:"))
    c = a4 * n4 * b
    if(t=='sin'):
      if (n4 > 2 and b != 1 and a4 > 2 and b4>2):
        print("f'(x)=",'(',a4,'sin(',b,'x))/(',b4,'x)','+', c,'ln(',b4,'x)', 'sin^', (n4 - 1), '(', b, 'x)', 'cos(', b,'x)')
      elif (n4 > 2 and b != 1 and a4 > 2 and b4 == 1):
        print("f'(x)=", '(', a4, 'sin(', b, 'x))/x)', '+', c, 'ln(x)', 'sin^', (n4 - 1),'(x)','cos(x)')
      elif (n4 <= 2 and b != 1 and a4>2 and b4>2):
        print("f'(x)=",'(',a4,'sin',b,'x)', c, 'sin(', b, 'x)', 'cos(', b, 'x)')
      elif (n4 == 1 and b != 1):
        print("f'(x)=", c, 'cos(', b, 'x)')
      elif (n4 > 1 and b == 1):
        print("f'(x)=", c, 'sin^', (n4 - 1), '(x)', 'cos(x)')
      elif (n4== 1 and a4 == 1 and b == 1):
        print("f'(x)= cos(x)")
      elif (n4 == 1 and a4 == 1 and b != 1):
        print("f'(x)=", c, 'cos(', b, 'x)')
      elif (n4 == 1 and b == 1 and a4 != 1):
        print("f'(x)=", c, 'cos(x)')
elif(_a==5):
    a = int(input("Enter the a:"))
    n = int(input("Enter the n:"))
    m = int(input("Enter the m:"))
    if(a>1 and n!=1 and m>2):
        print("f'(x)= f(x).{",n*m,'xln(',a,'x)','+(',n,'/',a,')x^',m-1,'}')
elif(_a==6):
    a = int(input("Enter the a:"))
    b = int(input("Enter the b:"))
    c = int(input("Enter the c:"))
    d = int(input("Enter the d:"))
    n = int(input("Enter the n:"))
    _n1 = int(input("Enter the n1:"))
    _n2 = int(input("Enter the n2:"))
    _n3 = int(input("Enter the n3:"))
    _n4 = int(input("Enter the n4:"))
    _n5 = int(input("Enter the n5:"))
    _n6 = int(input("Enter the n6:"))
    _n7 = int(input("Enter the n7:"))
    _n8 = int(input("Enter the n8:"))
    if (n >=2 and _n1 >= 2 and _n2 >= 2 and _n3>=2 and _n4>=2 and _n5>=2 and _n6>=2 and _n7>=2 and _n8>=2 ):
        print("f'(xy)=",_n8,'{(',a,'x^',n,'y^',_n1,'+',b,'x^',_n2,'y^',_n3,')/(',c,'x^',_n4,'y^',_n5,'+',d,'x^',_n6,'y^',_n7,')}^',_n8-1,'{(',a*n,'x^',n-1,'y^',_n1,'+',a*_n1,'x^',n,'y^',_n1-1,'dy/dx','+',b*_n2,'x^',_n2-1,'y^',_n3,'+',a*_n3,'x^',_n2,'y^',_n3-1,'dy/dx)/(',c*_n4,'x^',_n4-1,'y^',_n5,'+',c*_n5,'x^',_n4,'y^',_n5-1,'dy/dx','+',d*_n6,'x^',_n6-1,'y^',_n7,'+',d*_n7,'x^',_n6,'y^',_n7-1,'dy/dx)}')
elif(_a==7):
    a= int(input("Enter the a:"))
    n = int(input("Enter the n:"))
    t = int(input("Enter the t:"))
    m = int(input("Enter the m:"))
    c = int(input("Enter the c:"))
    if(n>=2 and t == 'cos' and m>=2 and c>=2):
        print("f'(x)=" -m*a,'e^(x',n,')')
elif(_a==9):
    _a = input("Enter the question: f(x)=")
    i, j, l, k, f, m = 0, 0, 0, 0, 0, 1
    _x = ['+', '-', '/']
    x = [1, '1', '2', 2, '3', 3, '4', 4, '5', 5, '6', 6, '7', 7, '8', 8, '9', 9]
    while (i < len(_a)):
        if (_a[i] == 's' and _a[i + 1] == 'i' and _a[i + 2] == 'n'):
            b = _a[i - 1]
            c = _a[i + 4]
            d = _a[i + 5]
            while (j < len(x)):
                if (b == x[j]):
                    e = x[j + 1]
                    while (l < len(x)):
                        if (d == x[l]):
                            f = x[l + 1]
                            while (k < len(x)):
                                if (c == x[k]):
                                    t = x[k + 1]
                                k += 1
                            print(f * e * t, 'sin^', t - 1, '(', t, 'x)', 'cos(', t, 'x)')
                        l += 1
                j += 1
        i += 1
        if (_a[i] == 's' and _a[i + 1] == 'i' and _a[i + 2] == 'n' and _a[i+6]=='x' and _a[i + 7] == 'l' and _a[i + 8] == 'n' and _a[i+10=='x']):
            t, e, z = 0, 0, 0
            b = _a[i - 1]
            c = _a[i + 4]
            d = _a[i + 5]
            p = _a[i + 9]
            while (j < len(x)):
                if (b == x[j]):
                    e = x[j + 1]
                    while (l < len(x)):
                        if (d == x[l]):
                            f = x[l + 1]
                            while (k < len(x)):
                                if (c == x[k]):
                                    t = x[k + 1]
                                k += 1
                                while (z < len(x)):
                                    if (p == x[z]):
                                        g = x[z + 1]
                                    z += 1
                        l += 1
                j += 1
        i += 1
    print(f * e * t, 'sin^', t - 1, '(', t, 'x)', 'cos(', t, 'x)', 'ln(', g, 'x)', '+(', e, '/', g, 'sin^', c, '(', d,
          'x))/x')







   
   
   









       











    
