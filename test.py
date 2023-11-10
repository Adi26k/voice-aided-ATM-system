import os
import pickle
from random import random
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time
import random
from stscreen import gui
from recaudio import rec
from spttex import SpeakText
"""
#path to training data
source   = "development_set/"   
modelpath = "speaker_models/"
test_file = "development_set_test.txt"        
file_paths = open(test_file,'r')

"""
#path to training data
source   = "SampleData/"   
accountdb=[{}]
#path where training speakers will be saved
modelpath = "Speakers_models/"
models=[]
gmm_files = [os.path.join(modelpath,fname) for fname in 
			os.listdir(modelpath) if fname.endswith('.gmm')]
"""for fname in gmm_files:
	with open(fname,'rb') as fl:
		response = pickle.load(fl,encoding='bytes')
		print(response)"""

#Load the Gaussian gender Models
models    = [pickle.load(open(fname,'rb')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
			in gmm_files]
for i in range(len(speakers)):
	accountdb.append({"name":speakers[i],"balance":random.randint(1000,5000)})
accountdb.pop(0)
print(accountdb)

error = 0
total_sample = 0.0


print ("Do you want to Test a Single Audio: Press 'any number'")
take = int(input().strip())
if take %2 == 0:
	SpeakText("Starting recording")
	rec()
	time.sleep(1.0)
	path = "recorded.wav" 
	print ("Testing Audio : ", path)
	sr,audio = read(source + path)
	vector   = extract_features(audio,sr)
	
	log_likelihood = np.zeros(len(models)) 
	
	for i in range(len(models)):
		gmm = models[i]
		
		scores = np.array(gmm.score(vector))
		
        
		 
		log_likelihood[i] = scores.sum()
		print(abs(int(log_likelihood[i])))
	vld=abs(int(np.max(log_likelihood)))
	print(vld)
	if vld<=29:
		winner = np.argmax(log_likelihood)
		print(winner)
		SpeakText("Detected as - "+speakers[winner])
		print ("\tdetected as - ", speakers[winner])
		for i in accountdb:
			print(i)
			if i["name"] == speakers[winner]:
				gui({"name":speakers[winner],"balance":i["balance"]})
	else:
		print("Speaker not found")
		SpeakText("Speaker not found")
	time.sleep(1.0)
else:
	SpeakText("Starting recording")
	rec()
	time.sleep(1.0)
	path = "testom.wav" 
	print ("Testing Audio : ", path)
	sr,audio = read(source + path)
	vector   = extract_features(audio,sr)
	
	log_likelihood = np.zeros(len(models)) 
	
	for i in range(len(models)):
		gmm = models[i]
		
		scores = np.array(gmm.score(vector))
		
        
		 
		log_likelihood[i] = scores.sum()
		print(abs(int(log_likelihood[i])))
	vld=abs(int(np.max(log_likelihood)))
	print(vld)
	if vld<=27:
		winner = np.argmax(log_likelihood)
		print(winner)
		SpeakText("Detected as - "+speakers[winner])
		print ("\tdetected as - ", speakers[winner])
		for i in accountdb:
			print(i)
			if i["name"] == speakers[winner]:
				gui({"name":speakers[winner],"balance":i["balance"]})
	else:
		print("Speaker not found")
		SpeakText("Speaker not found")
	time.sleep(1.0)

print (error, total_sample)
# Read the test directory and get the list of test audio files 
for path in file_paths:   

		total_sample += 1.0
		path = path.strip()   
		print ("Testing Audio : ", path)
		sr,audio = read(source + path)
		vector   = extract_features(audio,sr)

		log_likelihood = np.zeros(len(models)) 

		for i in range(len(models)):
			gmm    = models[i] #checking with each model one by one
			scores = np.array(gmm.score(vector))
			log_likelihood[i] = scores.sum()
		
		checker_name = path.split("_")[0]
		if speakers[winner] != checker_name:
			error += 1
			time.sleep(1.0)

print (error, total_sample)
accuracy = ((total_sample - error) / total_sample) * 100

print ("The Accuracy Percentage for the current testing Performance with MFCC + GMM is : ", accuracy, "%")


print ("Hurrey ! Speaker identified. Mission Accomplished Successfully. ")
