from redbot.core import commands


class PensiveCowBoy(commands.Cog):
    """My First Cog"""

    @commands.command()
    async def support(self, ctx):
        """Support Server"""
        await ctx.send("https://discord.gg/xGEMMmy")
