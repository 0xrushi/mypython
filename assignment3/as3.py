import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('assign_3_data.csv',usecols=['SGPA'])

list1 =df['SGPA'].tolist()
myl=[i.strip(',')for i in list1]
myl=[i.replace('--','0') for i in myl]
#print(myl)
myl=[float(i) for i in myl]
myl2=np.array(myl)

dist=np.where(myl2>8.0)
firstclass=np.where(myl2>7.0) and np.where (myl2<8.0)
hsc=np.where(myl2>6.0) and np.where (myl2<7.0)
sc=np.where(myl2>5.0) and np.where (myl2<6.0)
pc=np.where(myl2>4.0) and np.where (myl2<5.0)
fc=np.where(myl2<4.0)

ldist=len(myl2[dist])
lfirstclass=len(myl2[firstclass])
lhsc=len(myl2[hsc])
lsc=len(myl2[sc])
lpc=len(myl2[pc])
lfc=len(myl2[fc])

labels = 'Distinction', 'Firstclass', 'HigherSecondclass','Second Class','Passclass',"Fail"
sizes = [ldist,lfirstclass,lhsc,lsc,lpc,lfc]
colors = ['gold', 'yellowgreen', 'lightcoral','lightblue','orange','violet']
explode=(0, 0, 0,0,0,0.05)

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True,explode=explode)
plt.axis('equal')
plt.show()

def calculate(lst=np.array([0,0])):
	print(type(lst))
	dist=np.where(lst>80)
	firstclass=np.where(np.logical_and(lst>70,lst<80))
	hsc=np.where(np.logical_and(lst>60,lst<70))
	sc=np.where(np.logical_and(lst>50,lst<60))
	pc=np.where(np.logical_and(lst>40,lst<50))
	fc=np.where(lst<40)
	return (dist,firstclass,hsc,sc,pc,fc)

S21024=[]
nps21024=[]
subject_index=[8,16,24,32,40,47,54,61,67,81,87,95,103,111,119,126,133,140]
for i in subject_index:
    S21024.append(pd.read_csv('assign_3_data.csv').iloc[:,i])

S21024=[i.replace('FF','0') for i in S21024]
#S21025=[i==i for i in S21024]
#print(S21024)
for i in range(len(S21024)):
    for j in range(len(S21024[i])):
        if(S21024[i][j]!=S21024[i][j]):
            S21024[i][j]=0
for i in range(0,len(subject_index)):
    nps21024.append(np.array(S21024[i],dtype=np.int))

for i in range(0,len(nps21024)):
	x=calculate(nps21024[i])
	print(x)
	#print("----------------------------------------------------\n")
	myar=[len(nps21024[i][x[0]]),len(nps21024[i][x[1]]),len(nps21024[i][x[2]]),len(nps21024[i][x[3]]),len(nps21024[i][x[4]]),len(nps21024[i][x[5]])]
	plt.bar(np.arange(6), myar, align='center', alpha=0.5)
	plt.xticks(np.arange(6), labels)
	plt.ylabel('Usage')
	plt.title('Programming language usage')	 
	plt.show()
