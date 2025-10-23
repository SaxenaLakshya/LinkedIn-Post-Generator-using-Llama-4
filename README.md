# 🚀 LinkedIn Post Generator ✨

Create engaging, AI-powered LinkedIn posts with a single click!<br>
🤖 This project helps users generate LinkedIn-ready content using preprocessed examples and customizable prompts, leveraging LLM-based text generation. The Streamlit frontend enables quick and interactive post creation for enhanced social media engagement. 🌟

---

### 🎯 Features

- 🤖 **AI-powered post generation:** Utilizes a language model to generate LinkedIn posts tailored to topic, language, and length.
- 🗂️ **Pattern-based dataset:** Includes 250+ sample posts mapped to interview-relevant DSA and tech patterns for realistic output.
- 🎛️ **Flexible options:** Choose post topic, content length (Short/Medium/Long), and language (English/Hinglish).
- 🖥️ **Rich interface:** Simple, modern Streamlit UI with instant result display.
- 💡 **Custom prompt engineering:** Incorporates example-based few-shot prompting to guide the LLM for higher-quality posts.

---

### 🛠️ Tech Stack

- 🐍 **Python** (Backend)
- 🌐 **Streamlit** (Frontend/UI)
- 🔗 **Langchain** (LLM integration)
- ⚡ **GROQ API** / Meta-Llama-4 (LLM model)
- 📊 **pandas, dotenv** (Data, config)
- 🗄️ **JSON** (Data storage: `processed_posts.json`, `raw_posts.json`)
- 🛠️ **Optional:** Data preprocessing pipelines (for new training data)

---

### 🗂️ Project Structure

| 📁 File/Folder        | 📝 Purpose                                                                |
|-----------------------|--------------------------------------------------------------------------|
| `main.py`             | Streamlit frontend: UI, input handling, connects to backend              |
| `generate_post.py`    | Prompt engineering, post generation, model calling                       |
| `few_shot.py`         | Loads and filters few-shot/example posts                                 |
| `llm_helper.py`       | Connects and calls the GROQ LLM model                                    |
| `preprocess.py`       | Parses raw post data, extracts metadata, unifies tags                    |
| `data/`               | Stores `processed_posts.json` and `raw_posts.json`                       |
| `.env`/API Key.txt    | GROQ API key management (not included in repo for security reasons)      |

---

### ⚙️ Installation & Setup

1. **Clone the repository**
    ```
    git clone https://github.com/SaxenaLakshya/LinkedIn-Post-Generator-using-Llama-4.git
    cd LinkedIn-Post-Generator-using-Llama-4
    ```
2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```
3. **Set up API keys**
    - Add your GROQ API key to a `.env` file in the root:
      ```
      GROQ_API_KEY=your_api_key_here
      ```
4. **Add datasets**
    - Place your `processed_posts.json` and `raw_posts.json` in the `data` folder.

---

### 🧑‍💻 Usage

1. **Run Streamlit app**
    ```
    streamlit run main.py
    ```
2. **Interact via UI**
    - Select post topic, language, and length. 🎚️
    - Click 'Generate Post' for instant output. ⚡
    - Copy and use the generated LinkedIn-ready post! 📋

---

### ✍️ Example Output

> "Innovation in AI is changing hiring – here’s how DSA pattern mastery can help you stand out. Solve smarter, not harder! 🚀 #AI #coding"

---

### 🤝 Contributing

- Fork the repo and create PRs for new features, improved prompts, or bug fixes. 🔧
- New post examples should be added to `raw_posts.json` and processed via `preprocess.py`.

---

### 📜 License

This repository is released under the MIT License.

---

### 👤 Author

Created and maintained by Lakshya Saxena.  
Special thanks to the open source community for LLM and Streamlit tooling. 🌍

---

For questions or issues, please open an issue in this repository. 💬
