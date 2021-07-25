import csv
 
from collections import Counter



def getmean(totalweight,totalentries):
    mean=totalweight/totalentries
    print(f"mean is-{mean}")
def getmedian(totalentries,sorteddata):
    if totalentries%2==0:
        median1=float(sorteddata[totalentries//2])
        median2=float(sorteddata[totalentries//2-1])
        median=(median1+median2)/2
    else :
        median=float(sorteddata[totalentries//2])
    print(f"median is-{median}")
def mode(sorteddata):
  


    data=Counter(sorteddata)
    modedataforrange={
                    "75-85":0,
                    "85-95":0,
                    "95-105":0,
                    "105-115":0,
                    "115-125":0,
                    "125-135":0,
                    "135-145":0,
                    "145-155":0,
                    "155-165":0,
                    "165-175":0,

                     }
    for weight,occurence in data.items():
        if 75<float(weight)<85:
            modedataforrange["75-85"]+=occurence
        elif 85<float(weight)<95:
            modedataforrange["85-95"]+=occurence
        elif 95<float(weight)<105:
            modedataforrange["95-105"]+=occurence
        elif 105<float(weight)<115:
            modedataforrange["105-115"]+=occurence
        elif 115<float(weight)<125:
            modedataforrange["115-125"]+=occurence
        elif 125<float(weight)<135:
            modedataforrange["125-135"]+=occurence
        elif 135<float(weight)<145:
            modedataforrange["135-145"]+=occurence
        elif 145<float(weight)<155:
            modedataforrange["145-155"]+=occurence
        elif 155<float(weight)<165:
            modedataforrange["155-165"]+=occurence
        elif 165<float(weight)<175:
            modedataforrange["165-175"]+=occurence
    moderange,modeoccerence=0,0
    for range,occurence in modedataforrange.items():
        if occurence>modeoccerence:
            moderange,modeoccerence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
    mode=float((moderange[0]+moderange[1])/2)
    print(f"mode is...{mode:2f}")

with open("D:/Daksh/WhiteHatJr/C98/c104/sw.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
totalweight=0
totalentries=len(filedata)
sorteddata=[]
for persondata in filedata:
    totalweight=totalweight+float(persondata[2])
    sorteddata.append(float(persondata[2]))
sorteddata.sort()
getmean(totalweight,totalentries)
getmedian(totalentries,sorteddata)
mode(sorteddata)



