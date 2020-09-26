# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

fh = open('mbox-short.txt')
count = 0
for line in fh:
	line=line.rstrip()
	wrd=line.split()
	if 'From' in wrd:
		count+=1
		print(wrd[1])  
print("There were", count, "lines in the file with From as the first word")
