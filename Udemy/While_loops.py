# Introduction to While Loops

c = 0
while c < 5:
    print(c)
    c+=1

# 3 control statements - break, continue, pass

c = 0
while c < 5:
    if c == 3:
        break
    print(c)
    c+=1

a = 0
while a < 5:
    a+=1
    if a == 3:
        continue
    print(a)  

a = 0
while a < 5:
    a+=1
    if a == 3:
        pass # do nothing command and serves as a placeholder
    print(a)  