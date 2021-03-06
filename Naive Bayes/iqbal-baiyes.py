import xlrd
import numpy as np
from collections import defaultdict

def getData(filename, index_sheet):
	data = xlrd.open_workbook(filename)
	sheet = data.sheet_by_index(index_sheet)
	return sheet
	
# print getData("dummy.xls",0)
data = getData("dummy.xls",0)
sheet_row = data.nrow
sheet_cols = data.ncols

def getDataInput(atribut):
	datainput = []
	for i in range(1, sheet_row):
		datainput.append(data.row(i)[atribut].value)
	return len(datainput)

# print getDataInput(1)

def tabellikeli(sheet, atribut, kelas, hasil):
	listdata = [getDatainput(atribut)][3]
	totalprob=0
	totalyes=0
	totalno=0
	for i in range(1, sheet.nrows):
		listdata[i][1]=0
		listdata[i][2]=0
		for j in range(1, sheet.nrows):
			if listdata[j][0] != atribut:
				listdata[j][0] = atribut
				if data.row(i)[kelas].value =="Yes":
					listdata[i][1]+=1
				else:
					listdata[i][2]+=1
			else:
				if data.row(i)[kelas].value =="Yes":
					listdata[i][1]+=1
				else:
					listdata[i][2]+=1

	for i in getDatainput(atribut):
		for j in range(3):
			totalyes = listdata[i][1]+totalyes
			totalno =listdata[i][2]+totalno
			totalprob = listdata[i][1] + listdata[i][2]
			# print listdata[i][j]," : [", listdata[i][j],",",listdata[i][j],"]"
			# print "yes : ", totalyes/totalprob
			# print "no :" ,totalno/totalprob
	if (hasil =="Yes"):
		return totalyes
	else:
		return totalno

def prob(hasil,atr1,atr2,atr3,atr4):
	sheet = getData("dummy.xls",0)
	lh1 = tabellikeli(sheet,0,atr1,hasil)
	lh1 = tabellikeli(sheet,1,atr2,hasil)
	lh1 = tabellikeli(sheet,2,atr3,hasil)
	lh1 = tabellikeli(sheet,3,atr4,hasil)

	probb = 
