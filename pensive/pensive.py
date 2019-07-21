import discord
from redbot.core import commands
from typing import Optional


class Pensive(commands.Cog):
    """My First Cog"""

    @commands.command()
    async def support(self, ctx):
        """Support Server"""
        await ctx.send("https://discord.gg/xGEMMmy")

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

    @commands.command(hidden=True, aliases=['hooksay'])
    @commands.bot_has_permissions(manage_webhooks=True)
    async def webhooksay(self, ctx, member: Optional[discord.Member], *, msg: str):
        """
           Beep boop boop beep i\'m a robot
        """
        # https://github.com/TrustyJAID/Trusty-cogs/blob/master/trustybot/trustybot.py#L64
        if member is None:
            member = ctx.me
        if ctx.channel.permissions_for(ctx.me).manage_messages:
            await ctx.message.delete()
        guild = ctx.guild
        webhook = None
        for hook in await ctx.channel.webhooks():
            if hook.name == guild.me.name:
                webhook = hook
        if webhook is None:
            webhook = await ctx.channel.create_webhook(name=guild.name.me)
        avatar = member.avatar_url_as(format="png")
        msg = msg.replace("@everyone", "everyone").replace("@here", "here")
        for mention in ctx.message.mentions:
            msg = msg.replace(mention.mention, mention.display_name)

        await webhook.send(msg, username=member.display_name, avatar_url=avatar)