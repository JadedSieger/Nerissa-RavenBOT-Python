from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello! This is an Example Cog!')