import datetime
import os
from pydub import AudioSegment
from pydub.playback import play

def concatenate_audio(files):
    """Concatenates multiple MP3 files into one without pauses."""
    combined = AudioSegment.empty()
    for file in files:
        if os.path.exists(file):
            audio = AudioSegment.from_mp3(file)
            combined += audio
    return combined

def get_french_audio_files(hour, minute):
    """Returns audio files for time in French."""
    base_path = "audio/fr/"

    files = [f"{base_path}il_est.mp3"]
    if hour == 0:
        files.append(f"{base_path}minuit.mp3")
    else: 
        files.append(f"{base_path}{hour}.mp3")
        files.append(f"{base_path}heures.mp3")

    if minute != 0:
        files.append(f"{base_path}{minute}.mp3")
    
    return files

def get_english_audio_files(hour, minute):
    """Returns audio files for time in English."""
    base_path = "audio/en/"

    # Convert 12h
    hour_12 = hour % 12 if hour % 12 != 0 else 12
    period = "am.mp3" if hour < 12 else "pm.mp3"
    
    files = [f"{base_path}it_is.mp3"]

    if hour == 0:
        files.append(f"{base_path}midnight.mp3")
        if minute != 0:
            files.append(f"{base_path}{minute}.mp3")
        return files
    elif hour == 12:
        files.append(f"{base_path}noon.mp3")
        if minute != 0:
            files.append(f"{base_path}{minute}.mp3")
        return files
    else:
        if minute == 0:
            files.append(f"{base_path}{hour_12}.mp3")
            files.append(f"{base_path}oclock.mp3")
            files.append(f"{base_path}{period}")
            return files
        else:
            files.append(f"{base_path}{hour_12}.mp3")
    
    files.append(f"{base_path}{minute}.mp3")
    files.append(f"{base_path}{period}")
    return files

def get_german_audio_files(hour, minute):
    """Returns audio files for time in German."""
    base_path = "audio/de/"
    
    files = [f"{base_path}es_ist.mp3"]

    if hour == 0:
        files.append(f"{base_path}mitternacht.mp3")
    elif hour == 1:
        files.append(f"{base_path}1s.mp3")
    else:
        files.append(f"{base_path}{hour}.mp3")
        files.append(f"{base_path}uhr.mp3")
    
    if minute != 0:
        files.append(f"{base_path}{minute}.mp3")
    
    return files

def get_italian_audio_files(hour, minute):
    """Returns audio files for time in Italian."""
    base_path = "audio/it/"
    files = []

    if hour == 0:
        files.append(f"{base_path}e_mezzanotte.mp3")    
    elif hour == 1:
        files.append(f"{base_path}e_la.mp3")
        files.append(f"{base_path}una.mp3")
    else:
        files.append(f"{base_path}sono_le.mp3")
        files.append(f"{base_path}{hour}.mp3")

    if minute != 0:
        files.append(f"{base_path}e.mp3")
        files.append(f"{base_path}{minute}.mp3")
    
    return files

def vibrate_time(hour, minute):

    hour_12 = hour % 12 if hour % 12 != 0 else 12

    hour_long = hour_12 // 5
    hour_short = hour_12 % 5

    minute_10 = minute // 10
    minute_1 = minute % 10

    minute_10_long = minute_10 // 5
    minute_10_short = minute_10 % 5
    minute_1_long = minute_1 // 5
    minute_1_short = minute_1 % 5

    for _ in range(hour_long):
        print("💥 long")
        print("pause 0.5")
    for _ in range(hour_short):
        print("💢 short")
        print("pause 0.5")
    print("pause 1 second")
    for _ in range(minute_10_long):
        print("💥 long")
        print("pause 0.5")
    for _ in range(minute_10_short):
        print("💢 short")
        print("pause 0.5")
    print("pause 1 second")
    for _ in range(minute_1_long):
        print("💥 long")
        print("pause 0.5")
    for _ in range(minute_1_short):
        print("💢 short")
        print("pause 0.5")
    return True

def get_audio_files(hour, minute, language):
    """Returns audio files based on the chosen language."""
    if language == "fr":
        return get_french_audio_files(hour, minute)
    elif language == "en":
        return get_english_audio_files(hour, minute)
    elif language == "de":
        return get_german_audio_files(hour, minute)
    elif language == "it":
        return get_italian_audio_files(hour, minute)
    return []

def speak_time(language, hour, minute):
    """Plays the current time without pauses."""
    audio_files = get_audio_files(hour, minute, language)
    combined_audio = concatenate_audio(audio_files)
    play(combined_audio)

if __name__ == "__main__":
    language = input("Choose a language (fr, en, de, it, vibration): ").strip().lower()
    hour = int(input("hour: ").strip().lower())
    minute = int(input("minute: ").strip().lower())
    if language not in ["fr", "en", "de", "it", "vibration"]:
        print("Unsupported language.")
    elif language == "vibration":
        vibrate_time(hour,minute)
    else:
        if(hour > 24 or minute > 59):
            print("Wrong time.")
        else:
            speak_time(language, hour, minute)
        
