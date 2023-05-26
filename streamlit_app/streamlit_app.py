import streamlit as st
import speech_recognition as sr
import pyttsx3


st.title("Speech to Text Recognition")
start_recording = st.button("Start Recording")
r = sr.Recognizer()


if start_recording:
    # Record audio from the microphone
    with sr.Microphone() as source:
        st.write("Listening...")

        # Adjust microphone noise threshold for ambient noise
        r.adjust_for_ambient_noise(source)

        # Capture audio input
        audio = r.listen(source)

        # Convert speech to text
        try:
            text = r.recognize_google(audio)
            st.write(f"You Said: {text}")
        except sr.UnknownValueError:
            st.write("Unable to recognize speech")
        except sr.RequestError as e:
            st.write(f"Error: {e}")
else:
    st.write("Click the button to start recording.")


st.title("Text-to-Speech Recognition")
text = st.text_input("Enter the text to convert to speech")


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Convert text to speech on button click
if st.button("Convert to Speech"):
    if text:
        text_to_speech(text)
    else:
        st.warning("Please enter some text.")


st.title("Audio to Text")

audio_file = st.file_uploader("Upload an audio file", type=["wav"])

# Check if audio file is uploaded
if audio_file is not None:
    # Convert audio file to SpeechRecognition AudioFile
    audio = sr.AudioFile(audio_file)

    # Recognize speech from the audio file
    recognizer = sr.Recognizer()
    with audio as source:
        audio_data = recognizer.record(source)

    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio_data)
        st.write("Text:", text)
    except sr.UnknownValueError:
        st.write("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        st.write(
            "Could not request results from speech recognition service; {0}".format(e))
else:
    st.write("Upload an audio file to begin.")
