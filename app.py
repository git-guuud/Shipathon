import streamlit as st
import time
import os
import aspose.words as aw

def sleep_st():
    time.sleep(5)

st.title("PDF To DOCX Translator")

pdf_file = st.file_uploader("Please upload a PDF file to translate.", type=["pdf"])
if pdf_file is not None:
    with open(os.path.join("uploads",pdf_file.name),"wb") as f: 
      f.write(pdf_file.getbuffer())  

    with st.spinner('Uploading and Translating'):
        sleep_st()
        doc = aw.Document("uploads/Shipathon.docx")
        save_options = aw.saving.ImageSaveOptions(aw.SaveFormat.JPEG)
        save_options.page_set = aw.saving.PageSet(0)
        image_file = pdf_file.name.rsplit(".",1)[0] +  ".jpg"
        doc.save(f"uploads/{image_file}", save_options)
        st.subheader("Preview")
        st.image(f"uploads/{image_file}")
        docx_file = pdf_file.name.rsplit(".",1)[0] + ".docx"
        with open(f"uploads/{docx_file}", 'rb') as f:
            document = f.read()
        st.download_button('Download Translated Docx', data = document, file_name=docx_file)
    
    st.success("Done!")




