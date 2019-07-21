import discord
from redbot.core import commands
from typing import Optional


class Pensive(commands.Cog):
    """My First Cog"""

    @commands.command()
    async def support(self, ctx):
        """Support Server"""
        await ctx.send("https://discord.gg/xGEMMmy")

    @commands.command(hidden=True)
    async def say(self, ctx, *, msg: str):
        """Make the bot repeat things"""
        await ctx.send(msg)