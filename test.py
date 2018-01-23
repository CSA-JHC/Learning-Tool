file=open('studyterms.txt','r')
for line in file:
    line=line.replace('\n','').split(',')
    print(line[0])
file.close()
