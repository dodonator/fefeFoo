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
tmpFilename = './Sites/fefe' + monat + '.html' 
tmpPDF = './Sites/fefe' + monat + '.pdf'
os.system('touch ' + tmpFilename)
file1 = open(tmpFilename,'w')
f1 = file1.write(tmpInhalt)
file1.close()
os.system('sudo rm ' + tmpPDF)
os.system('wkhtmltopdf ' + tmpFilename + ' ' + tmpPDF)
# os.system('firefox file:///home/dodo/git/fefeFoo &')
# os.system('firefox file:///home/dodo/git/fefeFoo/start.html &')