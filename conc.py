import os
import fnmatch
mas=[]
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print (file)
        f=open(file, 'r')
        for x in f:
            z=x.strip()
            if not(z in mas):
                mas.append(z)
        f.close()

print(len(mas))

ff=open('itogo.log', 'w')
for x in mas:
    ff.write(x+'\n')
ff.close()
print('Done')
    
    
