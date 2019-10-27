#This is my first Python program since high school.hi
import os

gpa = sys.argv[1]
scoreType = sys.argv[2]
score = int(sys.argv[3])

collegeFile = open('colleges.txt')
collegeContent = collegeFile.readlines()
cc = {}
i = 0

for college in collegeContent:
    cc[i] = college.split('\t')
    i+=1

writeFile = open('results.html', 'w')

writeFile.write('''<!DOCTYPE html>
<html lang="en">
   <head>
      <title>College Wrecks</title>
      <meta charset="utf-8">
   </head>
   <body>
      <p>''')     #Write your table stuff after <p>

writeFile.write('<br>Safety:<br>')
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
            writeFile.write('*'+cc[element][0]+'<br>')

writeFile.write('<br><strong>Target:</strong><br>')
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
            writeFile.write('*'+cc[element][0]+'<br>')
    
writeFile.write('<br><strong>Reaches:</strong><br>')
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
            writeFile.write('*'+cc[element][0]+'<br>')

writeFile.write('''      </p>
   </body>
</html>''')

collegeFile.close()
writeFile.close()


    
