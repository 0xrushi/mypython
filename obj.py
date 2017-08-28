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
lst=[1,2,3,4,5,6,7]
S21024=[]
pp=pd.read_csv('assign_3_data.csv');
#nps21024=[]
subject_index=[8]
for i in subject_index:
    print(pp.iloc[:,i])
    S21024.append(pp.iloc[:,i])
print(lst)
print(S21024)
S21024=[i.replace('FF','0') for i in S21024]
#S21024=[i.replace('NaN','0') for i in S21024]
#S21024=[].fillna(0).astype(int)
#print(S21024)
nps21024=np.array(S21024)
#print(nps21024[0])
print(nps21024)
#nparray=np.array(S21024.split(), dtype=np.float)
#a=str(cleanedList)
#print(nparray)
#b=a.replace('nan','0')

#b = np.where(np.isnan(nps21025), nps21025, 0)
#print(b)

