import matplotlib.pyplot as plt
import math
def createfile(tempfile):
    contents=[10,15,45,5,20,25]
    with open(tempfile,'w') as file:
        for snow in contents:
            file.write(str(snow)+'\n')
def graphSnowfall(t):
    with open(t,'r') as file:
        snowlog=[int(line.strip()) for line in file]
    temprange=[0]*5
    for snow in snowlog:
        idx=math.floor((snow-1)/10)
        temprange[idx]+=1

    x_graph=[f"{i*10+1}-{(i+1)*10}" for i in range(len(temprange))]
    plt.bar(x_graph,temprange,width=0.4,color='grey')
    plt.xlabel('Snowfall Range (x-axis)')
    plt.ylabel('Number of Occurances (y-axis)')
    plt.title('Snowfall Occurance Graph')
    plt.savefig('snowfallimage.png')
    plt.show()

tempfile='snowtext.txt'
createfile(tempfile)
graphSnowfall(tempfile)
    
