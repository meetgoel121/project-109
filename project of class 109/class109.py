import pandas as pd
import statistics
import csv

df=pd.read_csv("class109.csv")

meathslist=df["math score"].to_list()

mean=statistics.mean(meathslist)
mode=statistics.mode(meathslist)
median=statistics.median(meathslist)

print("mean:",mean)
print("mode:",mode)
print("median:",median)

sd=statistics.stdev(meathslist)

sd1_start,sd1_ends=mean-sd,mean+sd
sd2_start,sd2_ends=mean-(2*sd),mean+(2*sd)
sd3_start,sd3_ends=mean-(3*sd),mean+(3*sd)

sd1data=[res for res in meathslist if res >sd1_start and res <sd1_ends]
sd2data=[res for res in meathslist if res >sd2_start and res <sd2_ends]
sd3data=[res for res in meathslist if res >sd3_start and res <sd3_ends]

sd1percentage=len(sd1data)*100/len(meathslist)
sd2percentage=len(sd2data)*100/len(meathslist)
sd3percentage=len(sd3data)*100/len(meathslist)

print(sd1percentage)
print(sd2percentage)
print(sd3percentage)