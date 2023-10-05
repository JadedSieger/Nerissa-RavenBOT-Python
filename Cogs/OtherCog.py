from discord.ext import commands

class OtherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send("Goodbye!")