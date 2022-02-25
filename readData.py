import math
import pandas as pd
import numpy as np
from collections import Counter
amtrakWords=["train","rail","amtrak","Train","Rail","Amtrak"]
delaware=["Deleware","Delware"]
noACount=0
aCount=0
trainCount=0
cities=[]
states=[]
df = pd.read_csv ('english.csv')
ansList=['7.','8.','9.']
questionTitles=['1.','2.', '3.', '3b','4._1', '4._2', '4._3', '4._4', '4._5', '4._6', '4b', '5._1','5._2','5._3','5._4','5._5','5._6','5b','6.','7.','8.','9.','10.','11.','12.','13.']
print(len(df))
for i in questionTitles:
    #for printing out the questions
    yesCount=0
    noCount=0
    totalA=0
    ansCount=[]
    for k in range(5):
        ansCount.append(0)
    print("\n\n\n"+i+" "+df[i].loc[0]+"\n\n\n")
    for j in range(2,len(df)):
        if(df[i].loc[j]==df[i].loc[j]):
            if i=="1.":
                if df[i].loc[j][len(df[i].loc[j])-1]==" ":
                    cityTemp=df[i].loc[j].capitalize()
                    cities.append(cityTemp[:-1])
                elif df[i].loc[j].capitalize()=="De - cheswold":
                    cities.append("Cheswold")
                elif df[i].loc[j].capitalize()=="Millsboro, de.":
                    cities.append("Millsboro")
                else:
                    cities.append(df[i].loc[j].capitalize())
            elif i=="2.":
                if df[i].loc[j][len(df[i].loc[j])-1]==" " and df[i].loc[j]!="Md " and df[i].loc[j].capitalize()!="Deleware ":
                    stateTemp=df[i].loc[j].capitalize()
                    states.append(stateTemp[:-1])
                elif df[i].loc[j]=="DE" or df[i].loc[j].capitalize()=="De" or ((df[i].loc[j][0]=="D" or df[i].loc[j][0]=="d")and df[i].loc[j]!="Delaware") or df[i].loc[j].capitalize()=="Deleware" or df[i].loc[j].capitalize()=="Us":
                    states.append("Delaware")
                elif df[i].loc[j]=="MD" or df[i].loc[j].capitalize()=="Md" or df[i].loc[j]=="Md ":
                    states.append("Maryland")
                else:
                    states.append(df[i].loc[j].capitalize())
            aCount+=1
            #print(df[i].loc[j]+str(j)+"\n")
            if str(df[i].loc[j])=="Yes":
                yesCount+=1
            elif str(df[i].loc[j])=="No":
                noCount+=1
            elif str(df[i].loc[j])=="Favorable":
                ansCount[0]+=1
            elif str(df[i].loc[j])=="Somewhat Favorable":
                ansCount[1]+=1
            elif str(df[i].loc[j])=="Neutral":
                ansCount[2]+=1
            elif str(df[i].loc[j])=="Somewhat Opposed":
                ansCount[3]+=1
            elif str(df[i].loc[j])=="Opposed":
                ansCount[4]+=1
        else:
            #print("No Answer\n")
            noACount+=1
        for w in amtrakWords:
            if w in str(df[i].loc[j]):
                #print(df[i].loc[j]+"\n")
                trainCount+=1
                break
    if i=="12.":
        print(str(yesCount) + " people answered yes to question " + i)
        print(str(noCount) + " people answered no to question " + i)
    elif i in ansList:
        print(str(ansCount[0])+" people answered favorable to question "+i)
        print(str(ansCount[1])+" people answered somewhat favorable to question "+i)
        print(str(ansCount[2])+" people answered neutral to question "+i)
        print(str(ansCount[3])+" people answered somewhat opposed to question "+i)
        print(str(ansCount[4])+" people answered opposed to question "+i)
    print("")
print(Counter(cities))
print(Counter(states))
print("Number of english responses: " + str(len(df)-2))
print("There were a total of " + str(noACount)+" of blank responses and " +str(aCount)+" not blank responses in the english survey")
print(str(noACount+aCount)+" responses total for the english survey")
print(str((noACount/(noACount+aCount))*100)+"% of the english answers for all questions were blank")
print("Trains were talked about " +str(trainCount) + " times")
