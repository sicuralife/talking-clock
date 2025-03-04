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
    files = [f"{base_path}il_est.mp3", f"{base_path}{hour}.mp3", f"{base_path}heures.mp3"]

    if minute != 0:
        files.append(f"{base_path}{minute}.mp3")
    
    return files

def get_english_audio_files(hour, minute):
    """Returns audio files for time in English."""
    base_path = "audio/en/"
    
    # Convert 12h
    hour_12 = hour % 12 if hour % 12 != 0 else 12
    period = "am.mp3" if hour < 12 else "pm.mp3"

    hour1_12 = (hour+1) % 12 if (hour+1) % 12 != 0 else 12
    period1 = "am.mp3" if (hour+1) < 12 else "pm.mp3"
    
    if minute == 0:
        files = [f"{base_path}it_is.mp3", f"{base_path}{hour_12}.mp3", f"{base_path}oclock.mp3", f"{base_path}{period}"]
    elif minute == 15:
        files = [f"{base_path}it_is.mp3", f"{base_path}quarter_past.mp3", f"{base_path}{hour_12}.mp3", f"{base_path}{period}"]
    elif minute == 30:
        files = [f"{base_path}it_is.mp3", f"{base_path}half_past.mp3", f"{base_path}{hour_12}.mp3", f"{base_path}{period}"]
    elif minute == 45:
        files = [f"{base_path}it_is.mp3", f"{base_path}quarter_to.mp3", f"{base_path}{hour1_12}.mp3", f"{base_path}{period1}"]
    elif minute < 30:
        files = [f"{base_path}it_is.mp3", f"{base_path}{minute}.mp3", f"{base_path}past.mp3", f"{base_path}{hour_12}.mp3", f"{base_path}{period}"]
    else:
        files = [f"{base_path}it_is.mp3", f"{base_path}{60 - minute}.mp3", f"{base_path}to.mp3", f"{base_path}{hour1_12}.mp3", f"{base_path}{period1}"]

    return files

def get_german_audio_files(hour, minute):
    """Returns audio files for time in German."""
    base_path = "audio/de/"
    
    if minute == 0:
        files = [f"{base_path}es_ist.mp3", f"{base_path}{hour}.mp3", f"{base_path}uhr.mp3"]
    elif minute == 15:
        files = [f"{base_path}es_ist.mp3", f"{base_path}viertel_nach.mp3", f"{base_path}{hour}.mp3"]
    elif minute == 30:
        files = [f"{base_path}es_ist.mp3", f"{base_path}halb_nach.mp3", f"{base_path}{(hour + 1 ) % 12}.mp3"]
    elif minute < 30:
        files = [f"{base_path}es_ist.mp3", f"{base_path}{minute}.mp3", f"{base_path}nach.mp3", f"{base_path}{(hour + 1 ) % 12}.mp3"]
    else: 
        files = [f"{base_path}es_ist.mp3", f"{base_path}{60 - minute}.mp3", f"{base_path}vor.mp3", f"{base_path}{hour + 1 % 12}.mp3"]
    
    return files

def get_italian_audio_files(hour, minute):
    """Returns audio files for time in Italian."""
    base_path = "audio/it/"
    files = []

    if hour == 1:
        files.append(f"{base_path}e_la.mp3")
        files.append(f"{base_path}una.mp3")
    else:
        files.append(f"{base_path}sono_le.mp3")
        files.append(f"{base_path}{hour}.mp3")

    if minute != 0:
        files.append(f"{base_path}e.mp3")
        files.append(f"{base_path}{minute}.mp3")
    
    return files

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

def speak_time(language, time=datetime.datetime.now()):
    """Plays the current time without pauses."""
    hour, minute = time.hour, time.minute
    audio_files = get_audio_files(hour, minute, language)
    combined_audio = concatenate_audio(audio_files)
    play(combined_audio)

if __name__ == "__main__":
    language = input("Choose a language (fr, en, de, it): ").strip().lower()
    if language not in ["fr", "en", "de", "it"]:
        print("Unsupported language.")
    else:
        speak_time(language)
