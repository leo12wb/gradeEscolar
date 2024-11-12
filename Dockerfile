# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código
COPY app .

# Exponha a porta que a aplicação usará
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]