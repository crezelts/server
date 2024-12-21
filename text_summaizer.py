from transformers import pipeline

# 요약을 위한 파이프라인 초기화 (BART 모델을 자동으로 사용)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(user_input):
    # 요약 생성
    summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary