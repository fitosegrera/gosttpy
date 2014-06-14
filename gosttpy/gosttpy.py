#!/usr/bin/python
# -*- coding: utf-8 -*-

# gosttpy.py
# Created by: fito_segrera 
# www.fii.to
# 05-07-14



import urllib  # For http request / google search
import urllib2  # For doing https POST
import simplejson as json # for handling JSON objects - in this case the return from google's API
import os


class gosttpy:

    def voiceRecognitionAndSearch(self, apiKey, returnType):
        #Use sox to record the input voice and generate a .flac audio file...
        os.system("sox -r 16000 -t alsa default voice.flac silence 1 0.1 5% 1 1.0 5%")
        print '================================'
        f = open('voice.flac')
        audioFile = f.read()
        f.close()
        lang_code = 'en-US'
        googl_speech_url = 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=' + apiKey
        hrs = {'Content-type': 'audio/x-flac; rate=16000'}
        req = urllib2.Request(googl_speech_url, data=audioFile, headers=hrs)
        p = urllib2.urlopen(req)

        # -----------------------
        # For some reason the google speech API returns 2 json objects (the first one is empty)
        # and parsing with the json library was breaking the code...
        # I solved the issue writing a .txt file with the json data and deleting the first json object in the stream...
        # As follows:

        rawData = p.read()
    
        # remove the empty "{"result":[]}" object that comes in the json
        # string:
        textFileClean = rawData.replace("""{"result":[]}""", '')
        
        # -----------------------
        # Parsing the CLEAN JSON data:

        # Loads the converted and cleaned data as a JSON object
        data = json.loads(textFileClean)
        parsedData = data['result'][0]['alternative'][0]['transcript']

        # Read through all the json object and store all the 'transcript' items in an array called 'allData'
        allData = []
        itemsCounter = 0

        # Return the list of all transcriptions from the JSON
        if returnType == 'ALL':
            for items in data['result'][0]['alternative']:
                allData.append(items['transcript'])
            return allData    

        # This line deletes the audio file once the operation is done
        os.remove('voice.flac')

        # ------------------------
        # Searching the returned text in google using urllib http request with the following link
        # http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=TEXT_TO_SEARCH_GOES_HERE

        # encode the clean data for searching with google... eg. 'hello world' --> 'hello%20world'
        # Spaces are replaced with %20

        # Return the SEARCH results from google search engine
        if returnType == 'SEARCH':
            encodedData = urllib.quote(parsedData)
            rawSearch = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + encodedData).read()
            jsonSearch = json.loads(rawSearch)  # load json to variable
            # Parse the jason object and get the specific item
            cleanSearch = jsonSearch['responseData']['results'][0]['content']
            return cleanSearch

        # Return the entire JSON object
        if returnType == 'RAW':
            return textFileClean

        # Return the FIRST transcription from the JSON
        if returnType == 'FIRST':
            return parsedData
