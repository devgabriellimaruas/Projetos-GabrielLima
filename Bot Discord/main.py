import discord
import aiohttp

def iniciar_bot():
  server_id = "ID DO SERVER DESEJADO"
  channel_id = "ID DO CANAL DESEJADO"
  token = "TOKEN DO BOT DO DISCORD"

  class Client(discord.Client):

    def __init__(self):
      super().__init__(intents=discord.Intents.default())
      self.synced = False

    async def on_ready(self):
      await self.wait_until_ready()
      if not self.synced:
        await tree.sync(guild=discord.Object(id=server_id))
      self.synced = True
      print(f"Entramos como {self.user}")

      # Envia msg automaticamente
      target_channel = self.get_channel(int(channel_id))
      if target_channel:
        await target_channel.send(f"Mensagem de erro: {await 'Mensagem aqui!'}")

      print('Mensagem Enviada')

  aclient = Client()
  tree = discord.app_commands.CommandTree(aclient)

  @tree.command(guild=discord.Object(id=server_id),
                name='teste',
                description='Testando')
  async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Mensagem de erro: {await message_bot()}", ephemeral=False)

  aclient.run(token)

  return 'Mensagem enviada'


iniciar_bot()