# SmartLang PDF2Doc



## About The Project

We created an AI-powered tool that converts PDFs from any language into Word documents in English. The tool will ensure accurate translation and preserve formatting.

### Features:
* We use [Gemini-2.0-flash](_https://deepmind.google/technologies/gemini/flash/) to extract text from image-based PDFs via OCR.
* We identified the source language using a detection tool and translated the text into English using an LLM-based translation API.
* We used python-docx and other prominent libraries to recreate the original formatting in the Word document.

## Getting Started




1. Get a free [API Key](https://ai.google.dev/gemini-api/docs?gad_source=1&gclid=CjwKCAiA7Y28BhAnEiwAAdOJUPdWwnVSMNfZ_GEBHZwQO-kaW2Biy2h-IFvZMJY2yMFdpfM_MF9d4RoC6GsQAvD_BwE)

2. Clone the repo
   ```sh
   git clone https://github.com/git-guuud/Shipathon.git
   ```

3. Make a hidden directory called ".streamlit" and create a file "secrets.toml" inside it
   ```js
   API = 'ENTER YOUR API'
   ```
  
 4. Install all packages in requirements.txt file
    ```js
    pip install -r requirements.txt
    ```

5. Run it locally
   ```js
    python -m streamlit run app.py
    ```
  






##  Deployment

 Project Link: [PDFtoDOC]()

