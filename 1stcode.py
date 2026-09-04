import edge_tts
import asyncio

async def speak():
    text = "I love you"
    voice = "en-US-JennyNeural"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("love.mp3")

asyncio.run(speak())