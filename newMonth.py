import urllib
import time
import datetime
import os

monat = time.localtime()[1]
if time.localtime()[1] <= 9:
	monat = str(time.localtime()[0]) + '0' + str(time.localtime()[1])
else:
	monat =  str(time.localtime()[0]) + str(time.localtime()[1])
tmpWebseite = urllib.urlopen('http://blog.fefe.de/?mon=' + monat)
tmpInhalt = tmpWebseite.read()
tmpFilename = 'fefe' + monat + '.html' 
os.system('touch ' + tmpFilename)
file1 = open(tmpFilename,'w')
f1 = file1.write(tmpInhalt)
file1.close()
tmpHyperlink = '<a href=' + tmpFilename + '>' + monat + '</a><br>' + '\n'
file2 = open('start.html','a')
f2 = file2.write(tmpHyperlink)
file2.close()
os.system('firefox file:///home/dodo/git/fefeFoo &')