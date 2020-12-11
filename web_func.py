from bs4 import BeautifulSoup
from requests import get

def scrapping():
    final = []
    site = get("https://news.google.com/rss?need=pt_br&gl=BR&hl=pt-BR&ceid=BR:pt-419")
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        final.append(f"{item.title.text}\n")
    return "\n".join(final)

def previsao_do_tempo():
    site = get('http://api.openweathermap.org/data/2.5/weather?lat=-29.6842&lon=-53.8069&appid=90215b527139cc03551eff4bb45ea00f&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    fell = clima['main']['feels_like']
    descricao = clima['weather'][0]['description']
    return f"Temperatura atual: {temperatura} graus, sensação térmica de {fell} graus, situação atual do céu {descricao}"

def covid_cases():
    site = get('https://covid19-brazil-api.now.sh/api/report/v1')
    casos = site.json()
    caso = casos['data'][14]['cases']
    suspeitos = casos['data'][14]['suspects']
    mortes = casos['data'][14]['deaths']
    return f"Agora existem: {caso} casos de Covid em seu estado, com {suspeitos} casos suspeitos e {mortes} mortes"