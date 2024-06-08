from telethon import TelegramClient, events, Button
import random
import datetime
import requests
import openai

# Telegram API bilgilerinizi girin
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone_number = 'YOUR_PHONE_NUMBER'

# OpenAI API anahtarınızı girin
openai.api_key = 'YOUR_OPENAI_API_KEY'

# TelegramClient oluşturun
client = TelegramClient('brend_userbot', api_id, api_hash)

# Bot sahibinin bilgileri
owner_name = 'Şirvan Əliyev'
bot_birth_date = datetime.datetime(2024, 6, 8)  # Botun oluşturulduğu tarix
bot_name = 'BrendUserbot'  # Botun adı

# Giriş yapma işlemi
async def main():
    # Eğer giriş yapılmamışsa giriş yapın
    await client.start(phone=phone_number)
    print("Userbot olaraq giriş edildi.")

    @client.on(events.NewMessage)
    async def handler(event):
        message = event.message.message.lower()
        
        if message == '/start':
            await event.respond('Salam! Mən BrendUserbot. Kömək üçün /help yazın.')
        
        elif message == '/help':
            help_text = """
            Mövcud komutlar:
            /start - Botu başlat
            /help - Kömək mesajı
            /quote - Təsadüfi bir sitat
            /joke - Təsadüfi bir zarafat
            /fact - Təsadüfi bir məlumat
            /time - Cari saat
            /date - Bugünün tarixi
            /weather [şəhər] - Məlumat üçün hava durumu
            /advice - Təsadüfi bir məsləhət
            /cat - Təsadüfi bir pişik şəkli
            /dog - Təsadüfi bir it şəkli
            /number - Təsadüfi bir nömrə
            /compliment - Təsadüfi bir tərif
            /insult - Təsadüfi bir təhqir
            /motivate - Təsadüfi bir motivasiya cümləsi
            /news - Cari xəbərlər
            /fact - Təsadüfi bir həqiqət
            /trivia - Məlumat yarışması sualı
            /translate [dil] [mətn] - Mətni göstərilən dilə tərcümə et
            /reminder [zaman] [mesaj] - Göstərilən zamanda mesaj xatırlat
            /poll [sual] [seçim1, seçim2, ...] - Sorğu yarat
            /quoteoftheday - Günün sitatı
            /trivia - Günün məlumat yarışması sualı
            /wordoftheday - Günün sözü
            /activity - Təsadüfi bir fəaliyyət təklifi
            /chucknorris - Təsadüfi Chuck Norris zarafatı
            /yesorno - Bəli və ya Xeyr suallarına cavab
            /flipcoin - Yazı tura at
            /roll - Zər at
            /8ball - Sehrli 8 topuna sual sor
            /alive - Botun vəziyyətini yoxla
            /urban [söz] - Urban Dictionary tərifi
            /define [söz] - Lüğət tərifi
            /synonym [söz] - Sinonimlər
            /antonym [söz] - Antonimlər
            /rhyme [söz] - Qafiyəli sözlər
            /wiki [mövzu] - Wikipedia məlumatı
            /math [ifadə] - Riyazi ifadə həlli
            /shorten [url] - URL qısaltma
            /expand [qısa url] - URL genişləndirmə
            /recipe [tərkib] - Resept təklifi
            /movie [film adı] - Film məlumatı
            /book [kitab adı] - Kitab məlumatı
            /song [mahnı adı] - Mahnı məlumatı
            /artist [sənətçi adı] - Sənətçi məlumatı
            /lyrics [mahnı adı] - Mahnı sözləri
            /currency [miqdar] [vahid1] [vahid2] - Valyuta çevirmə
            /unit [miqdar] [vahid1] [vahid2] - Vahid çevirmə
            /eva [sual] - Süni zəka söhbəti
            """
            await event.respond(help_text)
        
        elif message == '/quote':
            quotes = [
                "Həyat velosiped sürməyə bənzəyir. Tarazlığı qorumaq üçün hərəkət etməyə davam etməlisiniz. - Albert Einstein",
                "Uğur çox iş və təxəyyülün birləşməsidir. - Colin Powell",
                "Özünə inan. Bir şey edə biləcəyini düşündüyündə, onu başarmışsan. - Henry Ford",
            ]
            await event.respond(random.choice(quotes))
        
        elif message == '/joke':
            jokes = [
                "Niyə hakerlər park cəriməsi almır? Çünki öz yol nişanlarını çəkirlər.",
                "Kompyuterlər niyə tez qaçır? Çünki çoxlu RAM var!",
                "Proqramçı niyə çaya şəkər qoymaz? Çünki koduna ilişir."
            ]
            await event.respond(random.choice(jokes))
        
        elif message == '/fact':
            facts = [
                "Balıqlar boğulmaz.",
                "Bir insanın dili barmaq izi qədər özəldir.",
                "Dünyadakı ən böyük səhrə Antarktidadır."
            ]
            await event.respond(random.choice(facts))
        
        elif message == '/time':
            now = datetime.datetime.now().strftime("%H:%M:%S")
            await event.respond(f"Cari saat: {now}")
        
        elif message == '/date':
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            await event.respond(f"Bugünün tarixi: {today}")
        
        elif message.startswith('/weather'):
            city = message.split(' ', 1)[1]
            api_key = 'YOUR_WEATHER_API_KEY'
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(weather_url).json()
            if response.get('main'):
                temperature = response['main']['temp']
                description = response['weather'][0]['description']
                await event.respond(f"{city} üçün hava durumu: {temperature}°C, {description}")
            else:
                await event.respond(f"{city} üçün hava durumu tapılmadı.")
        
        elif message == '/advice':
            advices = [
                "Öz həyatını yaşa, başqalarının sənin yer
