import requests
import json
import re
from bs4 import BeautifulSoup
from transformers import pipeline

# 요약 모델
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 세팅 값
GOOGLE_API_KEY = 'AIzaSyDyijAysmK6naYQGAS0IY0iVq4x-hWlEs4'
GOOGLE_CSE_ID = 'c430d6559ad374f09'

def web_search(query):
    response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q={query}")
    return response.json()

def remove_html_tags(text):
    return BeautifulSoup(text, "html.parser").get_text()

def clean_text(text):
    text = remove_html_tags(text)
    text = text.replace('\xa0', ' ')  # non-breaking space 처리
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)  # 단어와 공백만 남기기
    text = text.strip()
    return text

def crawl_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 200 OK가 아니면 예외 발생
        soup = BeautifulSoup(response.text, 'html.parser')

        # 예시로 제목과 본문을 크롤링
        title = soup.title.string if soup.title else 'No title'
        paragraphs = soup.find_all('p')  # 페이지의 모든 <p> 태그를 찾음
        content = ' '.join([para.get_text() for para in paragraphs])  # <p> 태그의 텍스트를 합침

        return clean_text(content), title
    except requests.exceptions.RequestException as e:
        return f"Error fetching the page: {e}", None
    
def summarize_text(crawled_summary):
    summary = summarizer(crawled_summary, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary

def real_time(question):
    # 검색 결과 가져오기
    search_result = web_search(question)

    # SNS 도메인 제외
    domains = ['https://www.youtube.com', 'https://www.x.com', 'https://www.instagram.com', 'https://www.facebook.com']
    ignore_sns_url = [
        item for item in search_result['items']
        if not any(domain in item['link'] for domain in domains)
    ]

    combined_content = []

    for i, item in enumerate(ignore_sns_url[:3]):  # 첫 번째 검색 결과만 사용
        url = item['link']
        title = item['title']
        # page_content = item['snippet']
    
        # 링크 크롤링하여 본문 내용 가져오기
        crawled_content, crawled_title = crawl_url(url)
        print(f'\033[32m[주소]\033[0m {url}')
        print(f'\033[32m[주제]\033[0m {title}')
        
        # 크롤링한 내용이 정상적으로 반환되었는지 확인
        if crawled_title:
            combined_content.append(f"크롤링한 내용: {crawled_content[:1000]}...")

    return f'\033[32m[내용] \033[0m{summarize_text(combined_content)}\n'
