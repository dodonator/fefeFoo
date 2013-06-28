# coding: utf-8

import urllib
import time
import datetime
import os

monate = ['01','02','03','04','05','06','07','08','09','10','11','12']
jahre = []
startJ = '2006'
for i in range(int(startJ),time.localtime()[0]):
	jahre.append(str(i))
# print jahre

resultMonate = []

for jahr in jahre:
	for monat in monate:
		resultMonat = jahr + monat
		resultMonate.append(resultMonat)
for mon in range(1,time.localtime()[1]):
	if mon <= 9:
		mon = str(0) + str(mon)

	resultMonate.append(str(str(time.localtime()[0]) + str(mon)))


print resultMonate

jahr = ''
monat = ''
inhaltsverzeichnis = []
os.system('touch start.html')
files = ['start.html']
counter = 0
for monat in resultMonate:
	tmpFilename = 'fefe' + monat + '.html'
	files.append(tmpFilename)
	tmpCommand = 'touch ' + tmpFilename
	tmpPath = 'file:///home/dodo/git/fefeFoo/' + tmpFilename
	tmpHyperlink = '<a href=' + tmpFilename + '>' + monat + '</a><br>' + '\n'
	# print tmpFilename
	# print tmpCommand
	# print tmpPath
	# print tmpHyperlink
	# time.sleep(2)
	# os.system('clear')
	os.system(tmpCommand)
	site = urllib.urlopen('http://blog.fefe.de/?mon=' + monat)
	result = site.read()
	file1 = open(tmpFilename,'a')
	f1 = file1.write(result)
	file1.close()
	inhaltsverzeichnis.append(tmpHyperlink)
dateiInhalt = ''	
for link in inhaltsverzeichnis:
	dateiInhalt += link + '<br>'

file2 = open('start.html','w')
f2 = file2.write(dateiInhalt)
file2.close()
def removeMonthFiles(files):
	for datei in files:
		os.system('sudo rm ' + datei)
#removeMonthFiles(files)