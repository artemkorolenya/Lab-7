import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API2_KEY')
url = "https://newsapi.org/v2/everything"

def get_news():
    topic = input("Введите тему новостей (например: технологии, спорт): ")
    
    params = {
        'q': topic,
        'apiKey': API_KEY,
        'language': 'ru',
        'pageSize': 3,  
        'sortBy': 'popularity'  #relevancy ,popularity ,publishedAt
    }
    
    try:
        print("\n Ищу новости...")
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f" Ошибка {response.status_code}")
            return
            
        data = response.json()
        
        if data['totalResults'] == 0:
            print(" Новостей не найдено")
            return
            
        print(f"НОВОСТИ ПО ТЕМЕ: {topic.upper()}")
        print(f"Найдено: {data['totalResults']} новостей")
        
        for i, article in enumerate(data['articles'], 1):
            print(f"\n НОВОСТЬ #{i}")
            
            print(f"Заголовок: {article.get('title', 'Н/Д')}")
            
            source = article.get('source', {})
            print(f"Источник: {source.get('name', 'Н/Д')}")
            
            date = article.get('publishedAt', 'Н/Д')[:10] 
            print(f"Дата: {date}")
            
            desc = article.get('description', 'Н/Д')
            if desc and len(desc) > 50:
                desc = desc[:50] + "..."
            print(f"Описание: {desc}")
            
            print(f"Ссылка: {article.get('url', 'Н/Д')}")
            
    except Exception as e:
        print(f" Ошибка: {e}")

if __name__ == "__main__":
    print("Новости")

    while True:
        get_news()
        again = input("\nХотите найти еще новости? (да/нет): ").lower()
        if again not in ['да', 'yes']:
            print("До свидания!")
            break