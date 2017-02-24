# To Transform dataset into required form - list
import csv

f1=open("data.csv","r")

reader=csv.reader(f1,delimiter=',')

labels=[]
data_x=[]
data_y=[]

i=1
for row in reader:
	# Place all labels in a list
	if i==1:
		labels=row
		i+=1
		continue
	# Place all x values in data_x list 
	data_x.append(float(row[0]))

	# Place all y values in data_y list
	data_y.append(float(row[1]))