# ⭐ **AI News Summary & Mood Analysis Bot**

### *Automated Daily News Fetching • AI Summaries • Sentiment Analysis • HTML Newsletter*

---

## 🧠 **Project Overview**

Modern news consumption is overwhelming. Thousands of articles are published daily, and reading them all is impossible.
This project solves that problem with **AI-powered automation**.

The **AI News Summary & Mood Analysis Bot** automatically:

* Fetches the latest news from multiple sources
* Summarizes each article using an AI model
* Analyzes the overall sentiment (Positive / Neutral / Negative)
* Generates a clean HTML newsletter
* (Optional) Sends the newsletter directly to your email
* (Optional) Runs daily via Kaggle Scheduler

This is a perfect **Capstone Project** for:

✔ Artificial Intelligence
✔ Automation
✔ Data Analysis
✔ NLP
✔ Cloud Tools
✔ Python Development

---

# 🚀 **Features**

### 🔍 **1. News Fetching**

Fetches articles from:

* NewsAPI
* RSS feeds
* Custom newspapers

### 🤖 **2. AI-Powered Summarization**

Uses **Groq / Gemini / OpenAI** (your choice) to generate:

* Short summaries
* Key points
* Readable content

### 🎭 **3. Sentiment Analysis**

Classifies each summary into:

* 😊 Positive
* 😐 Neutral
* 😡 Negative

Outputs charts & statistics.

### 📰 **4. Automatic Newsletter Creation**

Generates:

* Beautiful HTML report
* Title, summary, sentiment
* Link to original article

### 📧 **5. Email Sender (Optional)**

Send the newsletter via Gmail using OAuth.

### ☁️ **6. Kaggle Automation (Optional)**

* Use Kaggle Secrets for API keys
* Run daily through Kaggle’s scheduler

---

# 🏗 **Project Architecture**

```
📦 AI-News-Summary-Bot
│
├── fetch_news.py         # News API & RSS fetcher
├── summarizer.py         # AI summarization logic (Groq/OpenAI/Gemini)
├── sentiment.py          # Sentiment analysis
├── emailer.py            # HTML generation + email sending
├── utils.py              # Helper functions + environment loader
├── main.py               # Main orchestrator
├── templates/
│   └── newsletter.html   # HTML layout for report
│
├── requirements.txt
└── README.md
```

---

# 🔧 **Tech Stack**

### **Languages & Frameworks**

* Python 3.10+
* HTML / Jinja Template

### **APIs**

* ⚡ Groq LLM (free & fast)
* 🔧 NewsAPI
* ✉ Gmail API (OAuth 2.0)

### **Tools**

* Kaggle Notebook
* Kaggle Secrets
* VS Code
* Google Cloud Console

---

# 🔑 **Environment Variables**

Create a `.env` file in the project root:

```
NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_key
SENDER_EMAIL=your@gmail.com
RECIPIENTS=receiver1@gmail.com,receiver2@gmail.com
```

---

# 🛠 **Setup Guide (LOCAL)**

## 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/ai-news-summary-bot.git
cd ai-news-summary-bot
```

## 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

## 4️⃣ Add `.env`

Create a `.env` file and paste your API keys.

## 5️⃣ Run the Project

```
python main.py
```

---

# 📡 **Gmail API Setup (If Using Email Sending)**

### 1. Go to Google Cloud Console

[https://console.cloud.google.com](https://console.cloud.google.com)

### 2. Create a new project

Name it: **AI News Bot**

### 3. Enable Gmail API

`API & Services → Library → Gmail API → Enable`

### 4. Create OAuth Consent Screen

* User Type: External
* Add yourself as "Test User"

### 5. Create OAuth Credentials

`Credentials → Create → OAuth Client ID → Desktop App`

Download `credentials.json`

Place it in your project folder.

When you run the bot, a browser will open → sign in → token.json will be created.

---

# 🤖 **Running Inside Kaggle**

### **1️⃣ Open Kaggle Notebook**

[https://www.kaggle.com/code](https://www.kaggle.com/code)

### **2️⃣ Upload Project Files**

Upload all Python files into the notebook.

### **3️⃣ Add Secrets**

Right side → Secrets → Add:

* `GROQ_API_KEY`
* `NEWS_API_KEY`

### **4️⃣ Add OAuth File**

Right side → Input → Upload → `credentials.json`

### **5️⃣ Run the notebook**

Click **Run All**

### **6️⃣ Automate (Optional)**

Kaggle → Schedule → Run daily/weekly

---

# 📈 **Example Output (Newsletter Preview)**

```
📰 AI News Summary - Nov 29, 2025

1. OpenAI releases GPT-6 preview
   Summary: ...
   Sentiment: Positive
   Link: https://...

2. Google launches Gemini 3.0
   Summary: ...
   Sentiment: Neutral
   Link: https://...
```

---

# 🧪 **Troubleshooting**

### ❌ API key not found

→ Ensure `.env` exists and environment variables load properly.

### ❌ Gmail OAuth "App blocked"

→ Add yourself as a Test User in Google Cloud.

### ❌ Summarizer not working

→ You hit model limits → switch to Groq (free).

### ❌ Kaggle error: NameError

→ Ignore console errors, only code cells matter.

---

# ❤️ **Credits**

Developed by **Nitin Mehra**
B.Tech CSE
Capstone Automation Project — 2025

---

# 📜 **License**

MIT License
Free to use, modify, and build on.

This README is **100% complete** and ready for GitHub.

