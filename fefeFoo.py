#!/usr/bin/python
import urllib
webSeite = urllib.urlopen('http://blog.fefe.de')
# print webSeite.read()
webSeitenInhalt = webSeite.read()
webSeitenInhaltModelliert = webSeitenInhalt.replace('fefes',' <b> dodos </b>')
webSeitenInhaltModelliert = webSeitenInhaltModelliert.replace('Fefe','<b> Dodo</b>')
webSeitenInhaltModelliert = webSeitenInhaltModelliert.replace('felix-bloginput (at) fefe.de','dodo (at) chaosdorf.de')
webSeitenInhaltModelliert = webSeitenInhaltModelliert.replace('fefe','<b> dodo </b>')
webSeitenInhaltModelliert = webSeitenInhaltModelliert.replace('"/?mon=201210">ganzer Monat','"http://blog.fefe.de">The real fefe!')
webSeitenInhaltModelliert = webSeitenInhaltModelliert.replace('Proudly made without PHP, Java, Perl, MySQL and Postgres','<b>Made with Python!</b>')

text1 = open('dodosBlog.html','w')
t1 = text1.write(webSeitenInhaltModelliert)
text1.close()

