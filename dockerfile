# 공식 FastAPI 기반 Python 이미지 사용 (최신 버전 사용 가능)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY .env . 
# 애플리케이션 코드 복사
COPY . .

# 컨테이너에서 실행될 기본 명령
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

