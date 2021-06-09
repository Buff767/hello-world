import re
myfile = open('namefaa.txt', 'w')
zipcode = open('zipdist.txt', 'a')

fname = raw_input('Enter file name: ')
zipcodex = raw_input('Enter ZIPCODE 5chars: ')
breakx =  raw_input('Press enter: ')

breakx = ''
namelast = ''
namefirst = ''
lastfirst = ''
address = ''
city = ''
state = ''
zip = ''
faanames = []
zipnames = []

if ( len(fname) < 1 ) : print "Restart and chose File"
fh = open(fname)
count = 0
zipcount = 0
year = 2018

for line in fh:
     if  len(line[40:59])- line[40:59].count(' ') > 0:
         if  len(line[10:19])- line[10:19].count(' ') > 0:
            count = count + 1
            print count
            namelast = (line[40:59]) 
            namefirst = (line[10:19])
            address = (line[70:89])
            city = (line[136:145])
            state = (line[153:155])
            zip = (line[155:167])
            
            lastfirst = "{} {} {} {} {} {}  ".format(namelast, namefirst, address, city, state, zip)
            faanames.append(lastfirst)
            print namelast
            print zipcodex
            
         #zipper = re.findall('[0-9]{5}-[0-9]+|[0-9]{5}',line)    
         if zipcodex in line[155:167]:
         
         #if zipcodex in line[40:59]:
            print zipcodex
            
         #if zipcodex in line[155:167]= 
            zipnames.append(lastfirst)
            zipcount = zipcount + 1
            #zipcode.write('%20s\n' %(lastfirst))
            #raw_input('THIS IS ZIPPER')
         
         #if count == 10000:
            #break
            
                
        #"{} {} {}".format(sday, smonth, year)
        #myfile.write("%s %s %s %s %s\n" %(rotation, sday, smonth, year, weekbd ))
        #myfile.write('%20s\n' %(namex))
#faanames.sort
#print faanames 
for x in sorted(faanames):
    myfile.write('%20s\n' %(x))
    
for y in sorted(zipnames):
    zipcode.write('%20s\n' %(y)) 

zipcode.write('%s zipcount = %s' %(zipcodex, zipcount))    
    
    
    
      
print 'count = %s' %count        