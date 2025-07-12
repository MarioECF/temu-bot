import logging
from telegram import Bot
from telegram.error import TelegramError
from datetime import datetime
import random

# Tu token de Bot
TOKEN = "7939965087:AAE01Zi0ISJzQNICMRzkwW6e7Vke1GoI-OE"

# Tu canal (con @ si es público)
CHANNEL = "@gadgetsvirales"

# Lista de productos
productos = [
    {
        "titulo": "🎧 Auriculares Inalámbricos con Mic y Pantalla LED",
        "precio": "Solo 12,44 € 🔥",
        "descripcion": (
            "✅ Cancelación de ruido ENC\n"
            "✅ Control táctil y caja con indicador LED\n"
            "✅ Batería 300mAh + carga Tipo-C\n"
            "🎮 Ideal para gaming, deporte o llamadas\n"
            "💯 Más de 100.000 ventas | Valoración 4,7 ⭐"
        ),
        "link": "https://temu.to/k/ezyhznh9xgu"
    },
    {
        "titulo": "📦 Organizador ajustable para cables",
        "precio": "2,49 €",
        "descripcion": "Despídete del caos en tu escritorio. Simple, útil y barato.",
        "link": "https://temu.com/tu-link-afiliado"
    },
    {
        "titulo": "🔥 Mini ventilador USB portátil",
        "precio": "5,99 €",
        "descripcion": "Silencioso, ideal para verano y teletrabajo. Llévalo donde quieras.",
        "link": "https://temu.com/tu-link-afiliado"
    }
]

# Genera el mensaje aleatorio
def generar_mensaje():
    producto = random.choice(productos)
    print("🟡 Producto elegido:", producto['titulo'])  # Muestra en consola el producto seleccionado
    mensaje = (
        f"{producto['titulo']}\n"
        f"💶 Precio: {producto['precio']}\n"
        f"{producto['descripcion']}\n\n"
        f"👉 [Ver en TEMU]({producto['link']})"
    )
    return mensaje

# Envia el mensaje al canal
def enviar_mensaje():
    bot = Bot(token=TOKEN)
    mensaje = generar_mensaje()
    try:
        bot.send_message(chat_id=CHANNEL, text=mensaje, parse_mode="Markdown")
        print(f"✅ Mensaje enviado: {datetime.now()}")
    except TelegramError as e:
        print(f"❌ Error al enviar mensaje: {e}")

if __name__ == "__main__":
    enviar_mensaje()
