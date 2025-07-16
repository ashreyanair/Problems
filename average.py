a=[23,29,45,200,45,34,27,77,88,127]
for i in a:
    if(i>100):
        a.remove(i)
print(sum(a)/len(a))

