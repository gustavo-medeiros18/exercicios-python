# Crie uma f-string que formate uma data e hora em um layout específico.
from datetime import datetime

def format_date(date):
  return f"{date:%d/%m/%Y %H:%M:%S}"

print(f"Data e hora atual: {format_date(datetime.now())}")
