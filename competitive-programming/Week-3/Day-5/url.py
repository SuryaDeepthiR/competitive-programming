def Base(string):
	dict1={}
	for i in range(len(string)):
		dict1[i]=string[i]
	return dict1


short = 7
shorturl={}
Long={}
count=0
base=Base("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")


def shortmethod(url):
	if (url in Long):
		print("ShortURL Exists"+Long[url])
		return
	global count
	s=""
	k=count
	count+=1

	if (k==0):
		s="0000000"
		if (s not in shorturl):
			shorturl[s]=url
			Long[url]=s
			print("short URL for "+url+" is https://ca.ke/"+s)
			return

	while(k!=0):
		s=base[k%62]+s
		k=k//62
	l=len(s)

	if (l<short):
		for i in range(short-l):
			s="0"+s

	if (s not in shorturl):
		shorturl[s]=url
		Long[url]=s

	print("https://ca.ke/"+s)

while (True):
	print("\n\t1)Generate ShortURL\n\t2)Redirect ShortURL\n\t3)Stop\n\tYour option:",end="")
	i=int(input())
	if (i==1):
		url=input("Enter URL: ")
		shortmethod(url)
	elif (i==2):
		correct=input("Enter a short URL: ")
		if shorturl.get(correct,None) is not None:
			print("Redirect to "+shorturl[correct])
		else:
			print("URL does not exist")
	elif(i==3):
		break
	else:
		print("Please enter valid Input")
