FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]  # ¡Cambia esto! Que ejecute directamente tu script
