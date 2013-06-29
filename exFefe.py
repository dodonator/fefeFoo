# coding: utf-8

import urllib
import time
import datetime
import os

# 200701 Beispiel

monate = ['01','02','03','04','05','06','07','08','09','10','11','12']
jahre = []
startJ = '2006'
for i in range(int(startJ),time.localtime()[0]):
	jahre.append(str(i))

resultMonate = []

for jahr in jahre:
	for monat in monate:
		resultMonat = jahr + monat
		resultMonate.append(resultMonat)
for mon in range(1,time.localtime()[1]):
	if mon <= 9:
		mon = str(0) + str(mon)

	resultMonate.append(str(str(time.localtime()[0]) + str(mon)))
jahr = ''
monat = ''
inhaltsverzeichnis = []
os.system('touch start.html')
files = ['start.html']
counter = 0
# os.system('mkdir Sites')
currentDir = os.getcwd()
ordnerInhalt = os.listdir('./Sites')
for monat in resultMonate:
	tmpFilename = 'fefe' + monat + '.html'
	tmpUnterVerzeichnis = './Sites/' + tmpFilename
	files.append(tmpFilename)
	if tmpFilename not in ordnerInhalt:
		tmpCommand = 'touch ' + tmpFilename
		os.system(tmpCommand)
		site = urllib.urlopen('http://blog.fefe.de/?mon=' + monat)
		result = site.read()
		file1 = open(tmpUnterVerzeichnis,'w')
		f1 = file1.write(result)
		file1.close()
	tmpPath = 'file://' + currentDir + '/Sites/' + tmpFilename
	tmpHyperlink = '<a href=' + tmpPath + '>' + monat + '</a>' + '\n'
	inhaltsverzeichnis.append(tmpHyperlink)
# print inhaltsverzeichnis
dateiInhalt = ''
dateiInhalt += '<html><head><title>Fefe Archiv</title></head><body>'
dateiInhalt += "<h3> Inhaltsverzeichnis von Fefe's Blog! </h3><br>"
dateiInhalt += '<br>'
dateiInhalt += '<table border="1">'
dateCounter = 0
yearCounter = 0
dateiInhalt += '<tr>'
for i in range(1,13):
	dateiInhalt += '<th>' + str(i) + '</th>'
dateiInhalt += '</tr><tr>'
for link in inhaltsverzeichnis:
	dateCounter += 1
	if dateCounter == 12:
		dateiInhalt += '<th>' + link + ' ' + '</th><th>' + str(int(startJ)+yearCounter) + '</th></tr>'
		dateCounter = 0
		yearCounter += 1
	else:
		dateiInhalt += '<th>' + link + '</th>'
dateiInhalt += '</body></html>'
file2 = open('start.html','w')
f2 = file2.write(dateiInhalt)
file2.close()
def removeMonthFiles(files):
	for datei in files:
		os.system('sudo rm ' + datei)
#removeMonthFiles(files)