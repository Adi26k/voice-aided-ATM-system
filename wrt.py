f=open("trainingDataPath.txt", "a+")
f.seek(0)
for i in range(1,24):
     f.write("Speaker-Nish/Audio_ "+str(i)+".wav\n")
f.close()