# 베이스 이미지 설정 (예: Python 3.12)
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 로컬의 requirements.txt 파일을 컨테이너의 /app 디렉토리로 복사
COPY requirements.txt /app/

# 가상환경 생성
RUN python -m venv venv

# 가상환경을 활성화한 후, 패키지 설치 및 spacy 모델 다운로드
RUN . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm

# 애플리케이션 코드 복사
COPY . /app/

# 애플리케이션 실행 명령어 (Linux 환경에서 가상환경 활성화 후 애플리케이션 실행)
CMD ["sh", "-c", ". venv/bin/activate && python venv/teramo.py"]
