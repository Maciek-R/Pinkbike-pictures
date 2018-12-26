from urllib import request
import os

fileWithUrls = "urls.txt"
picturesFolder = "pictures/"

def changeStringCharAt(text, pos, char):
	l = list(text)
	l[pos] = char
	return "".join(l)

def loadLinksFromFile():
	if not os.path.exists(picturesFolder):
		os.makedirs(picturesFolder)
	if not os.path.exists(fileWithUrls):
		open(fileWithUrls, 'a').close()
	return open(fileWithUrls, "r").read().split('\n')
	
def modifyUrl(requestUrl):
	urlSplits = requestUrl.split("/")
	urlSplits[-1] = changeStringCharAt(urlSplits[-1], 1, '0')
	urlSplits[-2] = changeStringCharAt(urlSplits[-2], 1, '0')
	return "/".join(urlSplits)
	
def downloadFile(requestUrl):
	urlSplits = requestUrl.split("/")
	fileName = picturesFolder + urlSplits[-1]
	print("Downloading file: " + requestUrl)
	f = open(fileName, 'wb')
	f.write(request.urlopen(requestUrl).read())
	f.close()
	print("Successfully downloaded file: " + requestUrl)

if __name__ == "__main__":
	links = loadLinksFromFile()
	for link in links:
		modifiedLink = modifyUrl(link)
		downloadFile(modifiedLink)
		
	print("Finished downloading " + str(len(links)) + " files.")