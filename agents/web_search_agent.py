# agents/web_search_agent.py

from duckduckgo_search import DDGS

class WebSearchAgent:
    def __init__(self):
        pass

    def search(self, query, max_results=3):
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            return [{
                "title": r.get("title", ""),
                "href": r.get("href", ""),
                "body": r.get("body", "")
            } for r in results]
