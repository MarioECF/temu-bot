import logging
import random
import requests
import csv
import os
from telegram import Bot
from telegram.error import TelegramError
from datetime import datetime

# Usamos el secret existente llamado BOT_TOKEN
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@gadgetsvirales"

# Google Sheets pública en CSV
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQrJXtElnBBUZyp6bpBBQzrFkbzY7U8Q1ASDdJeZRpVOKhD6YOgUehFNrb4Fgp1aS-arQYtlJ-qifJa/pub?output=csv"

def obtener_productos_desde_hoja():
    try:
        response = requests.get(SHEET_CSV_URL)
        response.raise_for_status()
        decoded = response.content.decode("utf-8")
        reader = csv.reader(decoded.splitlines())
        next(reader)  # Saltar encabezado
        productos = []
        for row in reader:
            if len(row) >= 4:
                productos.append({
                    "titulo": row[0],
                    "precio": row[1],
                    "descripcion": row[2],
                    "link": row[3]
                })
        return productos
    except Exception as e:
        print(f"❌ Error al obtener datos de Google Sheets: {e}")
        return []

def generar_mensaje(productos):
    producto = random.choice(productos)
    mensaje = (
        f"{producto['titulo']}\n"
        f"💶 Precio: {producto['precio']}\n"
        f"{producto['descripcion']}\n\n"
        f"👉 [Ver en TEMU]({producto['link']})"
    )
    return mensaje

def enviar_mensaje():
    productos = obtener_productos_desde_hoja()
    if not productos:
        print("❌ No se encontraron productos.")
        return

    mensaje = generar_mensaje(productos)
    bot = Bot(token=TOKEN)
    try:
        bot.send_message(chat_id=CHANNEL, text=mensaje, parse_mode="Markdown")
        print(f"✅ Mensaje enviado: {datetime.now()}")
    except TelegramError as e:
        print(f"❌ Error al enviar mensaje: {e}")

if __name__ == "__main__":
    enviar_mensaje()
