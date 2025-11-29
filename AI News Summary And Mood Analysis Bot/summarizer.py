import json
from groq import Groq
from utils import get_env

client = Groq(api_key=get_env("GROQ_API_KEY"))

def summarize_text_with_openai(title, description, url, max_tokens=300):
    prompt = f"""
You are a concise news summarizer. Produce JSON output with:
1. "summary_html": <ul><li>Short key points</li></ul>
2. "summary_text": A short 2-3 sentence summary

TITLE: {title}
DESCRIPTION: {description}
URL: {url}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.2
    )

    txt = response.choices[0].message.content

    try:
        return json.loads(txt)
    except:
        return {
            "summary_html": f"<ul><li>{description}</li></ul>",
            "summary_text": description[:300]
        }
