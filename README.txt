gosttpy
=======
###Google Speech To Text for Python

__Description:__ Python module for speech recognition using Google's speech recognition API.</br>  
__NOTES:__ Tested in ubuntu 13.10 with python_2.7</br>  
The official Python repository for this package can be found at: https://pypi.python.org/pypi/gosttpy/0.1.0

###Installation:
__If you have PIP installed in your computer just run__

    sudo pip install gosttpy
    
__OR for manuall installation:__

1. DOWNLOAD the repository by clicking this link https://github.com/fitosegrera/gosttpy/archive/master.zip __OR__ if you are a terminal user and have GIT installed then just go for:
    
        sudo git clone https://github.com/fitosegrera/gosttpy.git    

2. Unzip and cd into the folder

        cd PATH/TO/FOLDER/gosttpy-master
        
3. From within the folder, run the following command:

        sudo python setup.py install
        
###USAGE

This example recieves a voice command from the user and executes a google search...
It achieves this by recording a .flac audio file and uploading it to google's speech
recognition engine which converts it into readable text. The output from google is a 
JSON object with a list of posible interpretations/transcripts (translations from voice 
to text). The result of this operation becomes a google search engine query that outputs 
some result related to the original voice command...

The goosttPy module allows you to choose between different outputs:

1. 'RAW' --> Google's speech API JSON object (Complete / not-parsed) just raw-data
2. 'FIRST' --> Just the first transcripted version of your voice 
3. 'ALL' --> The list of all the transcripts returned by the google speech API
4. 'SEARCH' --> includes the search result returned from google


		from gosttpy import gosttpy

		speech = gosttpy.gosttpy()

		#Google API key for voice recognition (Replace the string 'YOUR-GOOGLE-SPEECH-API-KEY' with
		#your google API Key. get one from: https://console.developers.google.com/

		apiKey = 'YOUR-GOOGLE-SPEECH-API-KEY'

		#returnType --> options are: 'RAW', 'FIRST', 'ALL', 'SEARCH' 
		#(PLEASE SEE THE description at the begining of this example)

		returnType = 'FIRST'
		returnedText = speech.voiceRecognitionAndSearch(apiKey, returnType)
		print returnedText
		
###Notes:
- This python package uses your computer's microphone so verify its enabled.
- Getting a google speech API key might be a little tricky but there are many tutorials out there on how to do it. Give it a try, otherwise feel free to contact me. You can find official documentation at: http://www.chromium.org/developers/how-tos/api-keys

###Resources
https://github.com/gillesdemey/google-speech-v2</br>  
https://pypi.python.org/pypi/gosttpy/0.1.0</br>  

