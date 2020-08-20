from pydub import AudioSegment
from pathlib import Path
from gtts import gTTS
MYPATH = Path().absolute()
SOUNDS_PATH = str(MYPATH) + '\\sounds\\'

##########reversing_sound#########
def reverse_sound(sound):
    sound_reverse = sound.reverse()
    sound_reverse.export(SOUNDS_PATH+'reversed.mp3',format="mp3")

##########speed_change_of_sound########
def speed_change(sound, speed=1.0):
    speed_voice = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * speed)
        })
    speed_voice.export(SOUNDS_PATH +str(speed)+"x_speed.mp3", format="mp3")


############background_effect########

def background_effect(sound, background_sound, vol_dec = 5):
    result = sound.overlay(background_sound - vol_dec)
    result.export(SOUNDS_PATH + "backgroundAdded.mp3", format="mp3")

###########text_to_speech###########
def text_to_speech(text, lang):
    myobj = gTTS(text=text, lang=lang, slow=False)
    myobj.save(SOUNDS_PATH+'gtts.mp3')


#############################################################################################################
speed = 0.5
sound = AudioSegment.from_ogg(SOUNDS_PATH + '1.ogg')
background_sound = AudioSegment.from_file(SOUNDS_PATH + 'restaurant.mp3', format="mp3")
text = "Let's speak in English somehing something something"
# reverse_sound(sound)
# speed_change(sound, speed)
# background_effect(sound, background_sound)
text_to_speech(text,'en')