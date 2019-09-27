import os
import time
from threading import Thread

packetCounter = 0
baseDirectory = "../Database/"
cacheDirectory = "../Cache/"

def populateDictionary():
  databaseDictionary = {}
  while(1):
    for folders in os.listdir(baseDirectory):
      if folders not in databaseDictionary:
        databaseDictionary[folders] = {}
        time.sleep(3)
        for execs in os.listdir(baseDirectory + folders):
          for txtFiles in os.listdir(baseDirectory + folders + "/" + execs):
            if(txtFiles.lower().endswith(".txt")):
              for execVal in os.listdir(baseDirectory + folders + "/" +execs):
                if(not execVal.lower().endswith(".txt")):
                  (databaseDictionary[folders])[txtFiles] = [execs, 0, len(execs), execVal]

    granularity = 4
    lenOfDictionary = len(databaseDictionary)
    threadArray = []
    flag = 0
    setToRun(0, lenOfDictionary, databaseDictionary)
    """if(lenOfDictionary > granularity):
      chunk = lenOfDictionary / granularity
      for i in xrange(granularity):
        T = Thread(target=setToRun, args=(i*chunk,(i+1)*chunk, databaseDictionary,))
        threadArray.append(T)
    else:
      flag = 1
      setToRun(0, lenOfDictionary, databaseDictionary)
    if(not flag):
      for i in range(granularity):
        threadArray[i].join()"""


def setToRun(startVal, tillVal, databaseDictionary):
  global packetCounter
  j = startVal
  while(j < tillVal):
    jobDict = databaseDictionary[str(j)]
    for i in jobDict.keys():
      if((jobDict[i][1]) == 0 and jobDict[i][0] != jobDict[i][2]):
        jobDict[i][1] = 1
        tempPath = baseDirectory+str(j)+"/"
        with open(cacheDirectory+"packet"+str(packetCounter)+".txt", "w+") as myfile:
          packetCounter += 1
          execVal = str(jobDict[i][0])
          myfile.write(str(j)+"\n"+execVal+"\n"+tempPath+execVal+"/"+jobDict[i][3]+"\n"+tempPath+execVal+"/"+i+"\n"+str(1)+"\n"+str(0))
    j+=1



def main():
  populateDictionary()

main()

