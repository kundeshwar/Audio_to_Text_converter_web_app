import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr

reco = sr.Recognizer()
final_result = ""
#--------------------------------------------
st.markdown("<h1 style='text-align: center;'>Audio to Text Converter</h1>", unsafe_allow_html=True)
st.markdown("--------",unsafe_allow_html=True)
#------------------------------------------------------
audio = st.file_uploader("Upload Your File", type=["mp3","wav"])
if audio:
    st.audio(audio)
    audio_segment = AudioSegment.from_file(audio)#convert into audio segment 
    chunks=silence.split_on_silence(audio_segment, min_silence_len=500, silence_thresh=audio_segment.dBFS-20, keep_silence=100)
    for index,chu in enumerate(chunks):
        chu.export(str(index)+".wav", format="wav")
        with sr.AudioFile(str(index)+".wav") as source:
            recorded = reco.record(source)
            try:
               text = reco.recognize_google(recorded)
               st.write(text)
               final = final_result+" " +text
            except:
                a= "we not able to convert your audio"
                final = final_result+" "+ a
    st.text_area("", value=final)
#-----------------------------------------------------























