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
    async def luna(self, ctx):
        """What is LUNA's live price"""
        url = "https://api.binance.com/api/v3/ticker/price?symbol=LUNAUSDT"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        await ctx.send('LUNA is priced $' + data['price'])
        
    @commands.command()
    async def sol(self, ctx):
        """What is SOL's live price"""
        url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        await ctx.send('SOL is priced $' + data['price'])
