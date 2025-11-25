import requests
from bs4 import BeautifulSoup

def scrape_job_offer(url):
    try:
        # Add headers to mimic a browser to avoid some basic blocking
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Simple extraction: get all text. 
        # In a real app, we might want to target specific tags like 'main', 'article', or specific classes.
        # But for a generic "any link" requirement, getting body text is a safe fallback.
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        
        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:10000] # Limit to 10k chars to avoid token limits
    except Exception as e:
        print(f"Error scraping URL {url}: {e}")
        return None
