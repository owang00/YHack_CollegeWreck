#This is my first Python program since high school.hi
import os
import sys
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
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
   </head>
   <body>
      <div class="row form-group">
         <div class="col-md-4">
            <p>''')

writeFile.write('''<strong>Safety</strong><br> ''')
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
            writeFile.write('- '+cc[element][0]+'<br> ')

writeFile.write('''
            </p>
         </div>       
         <div class="col md-4">
            <p><strong>Target:</strong><br> ''')

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
            writeFile.write('- '+cc[element][0]+'<br> ')
    
writeFile.write('''
            </p>
         </div>
         <div class="col md-4">
            <p><strong>Reaches:</strong><br> ''')
for element in cc:
    if(scoreType.lower() == 'sat'):
        string = cc[element][4]
    else:
        string = cc[element][5]
    if(string != 'N/A'):
        dash = string.index('â€“')
        up = int(string[dash+3:])
        lo = int(string[:dash])
        mid = (lo+up)//2
        if(score < mid + (up - lo)/4):
            writeFile.write('- '+cc[element][0]+'<br> ')

writeFile.write('''
            </p>
         </div>
      </div>
   </body>
</html>''')

collegeFile.close()
writeFile.close()


    
