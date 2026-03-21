weather=(1,0,0,0,1,1,0)
suuny=0
rainy=0
for i in range(0,7):
    if(weather[i]==0):
        rainy+=1
    else:
        suuny+=1
if suuny > rainy:
    print("good weather")
else:
     print("bad weather")