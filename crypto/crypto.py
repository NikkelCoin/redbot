import discord
from discord.ext import commands
import urllib.request
import json
from redbot.core import commands


class Crypto(commands.Cog):
    """Crypto Price Cog (powered by coinmarketcap.com)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def btc(self, ctx):
        """What is Bitcoin's live price"""
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        await ctx.send('Bitcoin is priced $' + data['price'])
                

    @commands.command()
    async def ada(self, ctx):
        """What is Cardano's live price"""
        url = "https://api.binance.com/api/v3/ticker/price?symbol=ADAUSDT"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        await ctx.send('Cardano is priced $' + data['price'])

    @commands.command()
    async def eth(self, ctx):
        """What is Ethereum's live price"""
        url = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        await ctx.send('Ethereum is priced $' + data['price'])

    @commands.command()
    async def top5(self):
        """Get top 5 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=5"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 5:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " (" +
                               data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1

    @commands.command()
    async def top10(self):
        """Get top 10 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 10:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " ("
                               + data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1


    @commands.command()
    async def top20(self):
        """Get top 20 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=20"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 20:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " ("
                               + data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1
