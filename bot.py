import discord
import asyncio
import random
from datetime import datetime, timedelta
import os
TOKEN = os.getenv("MTQ3MzU2MzQxOTI5MzY0Njk2MQ.GidAzX.NqGTjUOVfa-jADUB0OcylObnTLjdUyPKdyhZ3c")

MY_CHANNEL_ID = 1379005104455417937 	# Pega aquí el ID de tu canal

RESPAWN_BASE = {
    "Amon Ra": 60,
    "Baphomet": 120,
    "Doppelganger": 120,
    "Drake": 120,
    "Dracula": 60,
    "Eddga": 120,
    "Golden Thief Bug": 60,
    "Maya": 120,
    "Mistress": 120,
    "Moonlight Flower": 60,
    "Orc Hero": 60,
    "Orc Hero2": 1440,
    "Orc Lord": 120,
    "Osiris": 60,
    "Pharaoh": 60,
    "Phreeoni": 120,
    "Stormy Knight": 60,
    "Turtle General": 60,
    "Atrocevefild01": 180,
    "Atrocevefild02": 360,
    "Atrocerafild04": 300,
    "Atrocerafild03": 180,
    "Atrocerafild02": 240,
    "Garm": 120,
    "Lord of Death": 133,
    "Samurai Specter": 91,
    "Evil Snake Lord": 94,
    "Tao Gunka": 300,
    "RSX": 125,
    "Vesper": 120,
    "Egnigem Cenia": 120,
    "Kiel D-01": 120,
    "Ifrit": 660,
    "Fallen Bishop Hibram": 120,
    "Beelzebub": 720,
    "Satan Morroc": 720,
    "Detale": 180,
    "Gloom Under Night": 300,
    "white lady": 117,
    "Valkyrie": 480,
    "Gopinich": 120,
    "Lady Tanee": 420,
    "Boitata": 120,
    "Dark Lord": 60
}

active_mvp = {}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Bot MVP Random activo 🔥")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != MY_CHANNEL_ID:
        return

    for mvp, base_respawn in RESPAWN_BASE.items():
        if mvp.lower() in message.content.lower():

            if mvp in active_mvp:
                return

            # Ventana random +0~10 minutos
            random_extra = random.randint(0, 10)
            total_respawn = base_respawn + random_extra

            death_time = datetime.now()
            respawn_time = death_time + timedelta(minutes=total_respawn)

            active_mvp[mvp] = respawn_time

            await message.channel.send(
                f"☠ {mvp} registrado a las {death_time.strftime('%H:%M')}.\n"
                f"🕒 Ventana estimada: {base_respawn}~{base_respawn+10} min."
            )

            # Loop inteligente
            while True:
                await asyncio.sleep(60)
                remaining = (respawn_time - datetime.now()).total_seconds()

                if 540 <= remaining <= 600:
                    await message.channel.send(f"⏳ {mvp} entra en ventana en 10 minutos")

                if 240 <= remaining <= 300:
                    await message.channel.send(f"⏳ {mvp} entra en ventana en 5 minutos")

                if remaining <= 0:
                    await message.channel.send(f"🔥 {mvp} ya está en ventana (puede estar vivo)")
                    del active_mvp[mvp]
                    break


client.run(TOKEN)