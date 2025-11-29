from fetch_news import fetch_from_newsapi, fetch_from_rss
from summarizer import summarize_text_with_openai
from sentiment import classify_mood, mood_icon
from emailer import render_newsletter_html, send_email
from utils import now_date_str

CATEGORIES=["technology","business","science","health"]
MAX_PER_CAT=3

def build_article(raw):
    title=raw.get("title","")
    desc=raw.get("description","") or raw.get("content","")
    url=raw.get("url")
    summary=summarize_text_with_openai(title,desc,url)
    mood,score=classify_mood(summary["summary_text"])
    return {
        "title":title,"description":desc,"url":url,
        "source":raw.get("source"),"published":raw.get("published"),
        "summary_html":summary["summary_html"],"summary_text":summary["summary_text"],
        "mood":mood,"mood_icon":mood_icon(mood),"category":raw.get("category","")
    }

def main():
    email=input("Enter recipient email: ")
    all_articles=[]; seen=set()
    for cat in CATEGORIES:
        try: arts=fetch_from_newsapi(category=cat,page_size=MAX_PER_CAT)
        except: arts=fetch_from_rss(topic=cat,limit=MAX_PER_CAT)
        for a in arts:
            if a["url"] in seen: continue
            seen.add(a["url"]); a["category"]=cat
            all_articles.append(build_article(a))
    html=render_newsletter_html(all_articles,now_date_str())
    send_email("Your AI Daily News Digest",html,email)

    print("Sent newsletter.")



if __name__=="__main__": main()
