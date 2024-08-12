import aiohttp

# Obter a mensagem a ser enviada pelo bot


async def messagebot():
    url_bot = 'URL DO BOT'

    async with aiohttp.ClientSession() as session:
        async with session.get(url_bot) as response:
            status_bot = response.status
            return status_bot
