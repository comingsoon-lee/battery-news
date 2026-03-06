import requests
from bs4 import BeautifulSoup

def get_battery_news():
    # 네이버 뉴스 '이차전지' 검색 결과 (최신순)
    url = "https://search.naver.com/search.naver?where=news&query=이차전지&sm=tab_opt&sort=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_list = []
    articles = soup.select(".news_tit") # 뉴스 제목 클래스 선택
    
    for article in articles:
        title = article.get('title')
        link = article.get('href')
        news_list.append({"title": title, "link": link})
        
    return news_list

if __name__ == "__main__":
    news = get_battery_news()
    for n in news:
        print(f"제목: {n['title']}\n링크: {n['link']}\n")
