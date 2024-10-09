import discord


def iniciar_bot(mensagem):
    server_id = 'id do servidor' #COLOCAR EM COMO INT
    channel_id = 'id do canal'  # COLOCAR EM COMO INT
    token = 'token do seu bot'  # MANTER EM COMO STR

    class Client(discord.Client):

        def __init__(self):
            super().__init__(intents=discord.Intents.default())
            self.synced = False

        async def on_ready(self):
            print(f"Entramos como {self.user}")
            if not self.synced:
                await tree.sync(guild=discord.Object(id=server_id))
                self.synced = True
                print("Comandos sincronizados")

            target_channel = self.get_channel(channel_id)
            if target_channel:
                await target_channel.send(mensagem)
                print('Mensagem Enviada')

    aclient = Client()
    tree = discord.app_commands.CommandTree(aclient)

    @tree.command(guild=discord.Object(id=server_id),
                  name='teste',
                  description='Testando')
    async def slash2(interaction: discord.Interaction):
        await interaction.response.send_message(
            mensagem, ephemeral=False)

    aclient.run(token)

    return 'Mensagem enviada'


mensagem = 'Olá'
iniciar_bot(mensagem)
