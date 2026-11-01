from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def test_tavily():
    tool = TavilySearchResults(max_results=2)
    results = tool.invoke({"query": "Latest breakthroughs in AI agent frameworks"})
    
    print("--- Tavily Search Test Output ---")
    for r in results:
        print(f"Title: {r.get('title')}")
        print(f"URL: {r.get('url')}\n")

if __name__ == "__main__":
    test_tavily()