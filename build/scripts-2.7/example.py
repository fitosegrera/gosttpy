#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------
# gosttpy Example
# Created by: fito_segrera 
# www.fii.to
# 05-07-14

'''
//////////////////////////////
/// PLEASE READ CAREFULLY! ///
//////////////////////////////

This example recieves a voice command from the user and executes a google search...
It achieves this by recording a .flac audio file and uploading it to google's speech
recognition engine which converts it into readable text. The output from google is a 
JSON object with a list of posible interpretations/transcripts (translations from voice 
to text). The result of this operation becomes a google search engine query that outputs 
some result related to the original voice command...

The goosttPy module allows you to choose between different outputs:

	1. 'RAW' --> Google's speech API JSON object (Complete / not-parsed) just raw-data

	2. 'FIRST' --> Just the first transcripted version of your voice 

	2. 'ALL' --> The list of all the transcripts returned by the google speech API

	3. 'SEARCH' --> includes the search result returned from google
'''

from gosttpy import gosttpy # From the file goosttPy.py import the class goosttPy 

speech = gosttpy.gosttpy()

# Google API key for voice recognition (Replace the string 'YOUR-GOOGLE-SPEECH-API-KEY' with
#your google API Key. get one from: https://console.developers.google.com/

apiKey = 'YOUR-GOOGLE-SPEECH-API-KEY'

#returnType --> options are: 'RAW', 'FIRST', 'ALL', 'SEARCH' 
#(PLEASE SEE THE description at the begining of this example)

returnType = 'FIRST'
returnedText = speech.voiceRecognitionAndSearch(apiKey, returnType)
print returnedText