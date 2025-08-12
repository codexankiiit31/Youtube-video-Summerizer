# 🦜 LangChain: AI-Powered Content Summarizer

Quickly summarize any English-language YouTube video or website just by pasting its URL. This tool leverages the power of **LangChain** to orchestrate the workflow, **Groq's** ultra-fast API to run the Gemma2 model for summarization, and **Streamlit** to provide a clean, interactive user interface.

## ✨ Features

* **YouTube & Website Support**: Summarize content from both YouTube videos (by extracting transcripts) and any public website.
* **High-Speed Summarization**: Powered by the **Groq API** and Google's **Gemma2-9b-it** model for near-instantaneous results.
* **Intelligent Content Loading**: Automatically detects the URL type and uses the appropriate content loader.
* **Secure API Key Handling**: Keeps your Groq API key safe using a password input field.
* **User-Friendly Interface**: A simple and clean UI built with Streamlit makes it easy for anyone to use.

---

## ⚙️ How It Works

The application follows a streamlined process orchestrated by LangChain:

`URL Input (YouTube or Website)` ➔ `🤖 Step 1: Content Loading` ➔ `Raw Text (Transcript or HTML Content)`➔ `🧠 Step 2: Groq & LangChain Summarization Chain` ➔ `✅ Final 300-Word Summary`

1.  **URL Input**: The user provides a URL and their Groq API key.
2.  **Content Loading**: The app checks the URL.
    * If it's a **YouTube link**, it uses the `youtube-transcript-api` to fetch the video's full transcript.
    * If it's a **website link**, it uses LangChain's `UnstructuredURLLoader` to scrape and extract the text content from the page.
3.  **Summarization**: The extracted text is passed to a LangChain `load_summarize_chain` (using the `stuff` method). This chain uses a specific prompt to instruct the **Gemma2-9b-it model** (via Groq) to generate a high-quality, 300-word summary.
4.  **Display**: The final summary is presented to the user on the Streamlit interface.

---

## 🛠️ Tech Stack

* **Backend & AI Orchestration**: Python
* **Web Framework**: Streamlit
* **LLM Serving**: Groq API (running Gemma2-9b-it)
* **AI Framework**: LangChain
* **Content Loaders**: `UnstructuredURLLoader`, `youtube-transcript-api`
* **Environment Management**: `conda`, `dotenv`

---

## 🚧 Limitations & Future Roadmap

This project is currently in its initial version. While fully functional for its core purpose, there are known limitations and exciting updates planned for the future.

### Known Limitations

* 📄 **Long Content**: The current summarization method (`stuff` chain) processes the entire text at once. It may fail on very long articles or video transcripts that exceed the AI model's context window.
* 🌐 **Language Support**: Summarization is currently optimized for **English-language content only**.

### Planned Updates

* 🧠 **Advanced Summarization**: Implement a more robust chain type like `Map-Reduce` or a **RAG (Retrieval-Augmented Generation)** pipeline to handle documents and videos of any length.
* 🌍 **Multi-Language Support**: Add capabilities to process and summarize content in multiple languages.
* 💾 **Session History**: Integrate a feature to save and view a history of your past summaries.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.10
* Conda for environment management
* A Git client

### 1. Clone the Repository

First, clone the project repository to your local machine.
``bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_DIRECTORY>
``bash
### 2.Create and Activate the Conda Environment
 Create the Conda environment with Python 3.10
conda create -p urlenv python==3.10 -y

 Activate the newly created environment
conda activate urlenv/

###3. Install Dependencies
pip install -r requirements.txt

###4. Setup Enviroment
 .env file
 Get your API key from the Groq console ([https://console.groq.com/keys](https://console.groq.com/keys))
 GROQ_API_KEY="YOUR_GROQ_API_KEY"

### 5.Run The Application
Streamlit run app.py
