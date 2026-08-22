from gtts import gTTS
text='hello disha'
tts=gTTS(text=text,lang='en')
tts.save('voice.mp3')
print('audio saved successfully')