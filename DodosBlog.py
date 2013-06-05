#!/usr/bin/python
import urllib
webSeite = urllib.urlopen('http://blog.fefe.de')

webSeitenInhalt = webSeite.read()
nichts = ''
webSeitenInhaltsModulationsVerzeichnis = {'fefes':' <b> dodos </b>','Fefe':'<b> Dodo</b>','felix-bloginput (at) fefe.de':'dodo (at) chaosdorf.de','fefe':'<b> dodo </b>','"/?mon=201210">ganzer Monat':'"http://blog.fefe.de">The real fefe!','Proudly made without PHP, Java, Perl, MySQL and Postgres':'<b>Made with Python!</b>'}

for key in webSeitenInhaltsModulationsVerzeichnis:
	webSeitenInhalt = webSeitenInhalt.replace(key,webSeitenInhaltsModulationsVerzeichnis[key])
# Dateischreiber für den Momentanen Tag!
tmpTag = open('dodosBlog.html','w')
tmpTag.write(webSeitenInhalt)
tmpTag.close()
# Dateischreiber für das Archiv
archiv = open('archiv.html','a')
archiv.write('\n' + webSeitenInhalt + '\n')
archiv.close()

