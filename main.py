from urllib import request
import os

fileWithIds = "urls.txt"
picturesFolder = "pictures/"

prefixLink = "https://ep1.pinkbike.org/"
uniquePrefix = "p0pb"
extensionFile = ".png"

def changeStringCharAt(text, pos, char):
	l = list(text)
	l[pos] = char
	return "".join(l)

def loadIdsFromFile():
	if not os.path.exists(picturesFolder):
		os.makedirs(picturesFolder)
	if not os.path.exists(fileWithIds):
		open(fileWithIds, 'a').close()
	return open(fileWithIds, "r").read().split('\n')
	
def createUrl(iD):
	return prefixLink+uniquePrefix+iD+'/'+uniquePrefix+iD+extensionFile
	
def downloadFile(requestUrl):
	urlSplits = requestUrl.split("/")
	fileName = picturesFolder + urlSplits[-1]
	print("Downloading file: " + requestUrl)
	f = open(fileName, 'wb')
	f.write(request.urlopen(requestUrl).read())
	f.close()
	print("Successfully downloaded file: " + requestUrl)

if __name__ == "__main__":
	iDS = loadIdsFromFile()
	for iD in iDS:
		createdLink = createUrl(iD)
		downloadFile(createdLink)
		
	print("Finished downloading " + str(len(iDS)) + " files.")