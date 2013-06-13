#!/usr/bin/python
# coding: utf-8
# License: GPLv3
# Developer/Owner: Dodo (dodo@chaosdorf.de)
import urllib
import time
class fefe(object):
	def lese(self):
		self.webSeite = urllib.urlopen('http://blog.fefe.de')
		self.webSeitenInhalt = self.webSeite.read()
		self.webSeitenInhalt = self.webSeitenInhalt.replace("""<h2><a href="/" style="text-decoration:none;color:black">Fefes Blog</a></h2>
<b>Wer schöne Verschwörungslinks für mich hat: ab an felix-bloginput (at) fefe.de!</b>
<p align=right>Fragen?  <a href="/faq.html">Antworten!</a>  Siehe auch: <a href="http://alternativlos.org/">Alternativlos</a><p>""",'\n')
		self.webSeitenInhalt = self.webSeitenInhalt.split('/<ul>')
	def markiere(self,toMark):
		for inhalt in self.webSeitenInhalt:
			inhalt = inhalt.replace(toMark,'<b>' + toMark + '</b>')
	def archivPutzen(self):
		self.archiv = open('archiv.html','w')
		self.archiv.write('\n')
		self.archiv.close()
	def publish(self):
		self.lese()
		archiv = open('archiv.html','r')
		self.archiv = archiv.read()
		archiv.close()
		# Dateischreiber für das Archiv
		for inhalt in self.webSeitenInhalt:
			if inhalt not in self.archiv:
				self.sappend('archiv.html',inhalt, 3)
			else:
				pass
	def main(self):
		self.lese()
		eingabe = raw_input('')
		marks = []
		if eingabe == 'c' or eingabe == 'C':
			self.archivPutzen()
		elif eingabe == 'p' or eingabe == 'P':
			self.publish()
		elif eingabe == 'm' or eingabe == 'M':
			mark = ''
			while mark != '#q':
				mark = raw_input('')
				marks.append(mark)
			mark = ''
			for mark in marks:
				self.markiere(mark)
			self.publish()
		self.publish()
	def sappend(self,file, string, line = 0):
		f = open('archiv.html', 'r').read().split('\n')
		a = f[:line]
		b = f[line:]
		a.append(string)
		open('archiv.html', 'w').write('\n'.join(a + b))
		
	
f = fefe()
f.main()