#This is my first Python program since high school.hi
import os
#print('Hello world!')

gpa = sys.argv[1]
scoreType = sys.argv[3]
score = int(sys.argv[4])

collegeFile = open('colleges.txt')
collegeContent = collegeFile.readlines()
cc = {}
i = 0

for college in collegeContent:
   # print(college)
    #college.split('\t')
    cc[i] = college.split('\t')
    i+=1


#print(cc[0][0])
#c = cc[0]
#print(c[0])
print('Safety:\n')
for element in cc:
    if(scoreType.lower() == 'sat'):
        string = cc[element][4]
    else:
        string = cc[element][5]
    if(string != 'N/A'):
        dash = string.index('â€“')
        up = int(string[dash+3:])
        lo = int(string[:dash])
        mid = (lo+up)/2
        if(score >= up + (up - lo)/4):
            print('*'+cc[element][0]+'\n')

print('Target:\n')
for element in cc:
    if(scoreType.lower() == 'sat'):
        string = cc[element][4]
    else:
        string = cc[element][5]
    if(string != 'N/A'):
        dash = string.index('â€“')
        up = int(string[dash+3:])
        lo = int(string[:dash])
        mid = (lo+up)/2
        if(score >= mid + (up - lo)/4 and score < up + (up - lo)/4):
            print('*'+cc[element][0]+'\n')
    
print('Reaches')
for element in cc:
    if(scoreType.lower() == 'sat'):
        string = cc[element][4]
    else:
        string = cc[element][5]
    if(string != 'N/A'):
        dash = string.index('â€“')
        up = int(string[dash+3:])
        lo = int(string[:dash])
        mid = (lo+up)/2
        if(score < mid + (up - lo)/4):
            print('*'+cc[element][0]+'\n')


    
