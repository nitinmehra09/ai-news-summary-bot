import requests
from utils import get_env
from bs4 import BeautifulSoup

NEWSAPI_KEY = get_env("NEWSAPI_KEY")

def fetch_from_newsapi(query=None, category=None, page_size=10):
    url = "https://newsapi.org/v2/top-headlines"
    params = {"apiKey": NEWSAPI_KEY, "pageSize": page_size, "language": "en"}
    if category: params["category"] = category
    if query: params["q"] = query

    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()

    articles = []
    for a in data.get("articles", []):
        articles.append({
            "title": a.get("title"),
            "description": a.get("description") or "",
            "content": a.get("content") or "",
            "url": a.get("url"),
            "source": a.get("source", {}).get("name"),
            "published": a.get("publishedAt"),
        })
    return articles

def fetch_from_rss(topic="technology", limit=10):
    rss_url = f"https://news.google.com/rss/search?q={topic}"
    r = requests.get(rss_url)
    soup = BeautifulSoup(r.content, "xml")
    items = soup.find_all("item")[:limit]
    out = []
    for it in items:
        out.append({
            "title": it.title.text,
            "description": "",
            "content": "",
            "url": it.link.text,
            "source": it.source.text if it.source else "",
            "published": it.pubDate.text if it.pubDate else "",
        })
    return out
