import discord
from redbot.core import commands
from typing import Optional


class Pensive(commands.Cog):
    """My First Cog"""

    @commands.command()
    async def support(self, ctx):
        """
           Support Server

           enable your dms to get the server invite lol
        """
        try:
            await ctx.author.send("https://discord.gg/xGEMMmy")
        except discord.HTTPException:
            pass

    @commands.command()
    async def say(self, ctx, *, msg: str):
        """Make the bot repeat things"""
        await ctx.send(msg)

    @commands.command(hidden=True)
    async def silentsay(self, ctx, *, msg: str):
        """
           Makes the Bot repeat things silently
        """
        # https://github.com/TrustyJAID/Trusty-cogs/blob/master/trustybot/trustybot.py#L56
        if ctx.channel.permissions_for(ctx.guild).manage_messages:
            await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def pensivespam(self, ctx):
        msg =  '<:pensivecowboy:592510037793177619>' * 100
        await ctx.send(msg)