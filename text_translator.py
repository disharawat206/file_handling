from gtts import gTTS
txt='hello mummy ,namaste ,papa namaste ,khushi didi namaste,mai roti banane ja rhi hu '
tts=gTTS(text=txt,lang='hi')
tts.save('mummy.mp3')
print('voice saved successfully')