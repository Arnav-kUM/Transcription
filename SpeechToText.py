
import streamlit as st
import speech_recognition as sr


def main():
    st.title("Real-time Voice Transcription")
    
    transcribe_button = st.button('Start Transcription' )

    if transcribe_button:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            while transcribe_button:
                
                audio = r.listen(source)
                try:
                    st.write("Please wait...")
                    text = r.recognize_google(audio)
                    st.write("Transcription:", text)
                    stop = st.button("Stop Transcription")
                    if(stop):
                        break
                except sr.UnknownValueError:
                    st.write("Could not understand audio")
                    if(stop):
                        break
if __name__ == "__main__":
    main()
