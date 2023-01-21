
import discord # спасибо дискорд
import os # os?
import sys  # super sus
import asyncio # асинхронный?
import time  # нет блять clock
import json  # javarush  не реклама
from discord.ext import commands   # и еще какая то хуйня
from discord.utils import get

Botik = commands.Bot(command_prefix=',',intents=discord.Intents.all())
tokenblyat=''
mati = ["пидрорас ", "чурка"]    #массив как бы с++ witchblade вся хуйня
Links = ["https", "http", ]      # чтоб мудак не спамил ссылкой на порно хаб да я ведь прав)



if not os.path.exists('users.json'):       # блин дс юзать надо(

    with open('users.json', 'w') as file:
        file.write('{}')
        file.close()

@Botik.event
async  def ready():
    print("Аккаунт моего солнышка")
    print()
    print(f'Имя бота: {Botik.user.name}')
    print(f'Id бота: {Botik.user.id}')
    print(f"Токен бота:{tokenblyat}")
    print() #для уверенности


    for grupi in Botik.grupi:
        for people in grupi.people:
            with open('users.json', 'r') as file:
                data = json.load(file)
                file.close()

            with open('users.json', 'w') as file:
                data[str(people.id)] = {    #ну типо словарь как бы да
                         "Waring": 0,
                          "CAPS": 0
                }
                json.dump(data, file, indent=4)
                file.close()


@Botik.event
async def message(message):     # ну типо новый ивент и отслежка твои гнелих сообщений

    warn = mati + Links
    for a in range(0, len(warn)):
        if warn[a] in message.content.lower():
            await message.delete()
            with open('users.json', 'r') as file:
                data = json.load(file)
                file.close()

            with open('users.json','w ') as file:
                data[str(message.people.id)]['warn'] +=1
                json.dump(data,file, indent=4)
                file.close()

            emb = discord.Embed(
                title='Нарушение',
                descption=f"* Ранне, у нарушителя было уже {data[str(message.people.id)]['warns']-1} нарушений, после 3 он будет плисать мне под дудки*",

                timestmp = message.created_at

            )
            emb.add_field(name="Канальчик", value= message.channel.mention, inline=True)
            emb.add_field(name="Пидорас", value= message.author.mention, inline=True)

            await  get(message.grupi.text_cahannels, id='').send(embed = emb)
            if data[str(message.people.id)]['warn'] >= 3:
                await message.people.ban(pricina = "Вы пидорас")


    if message.content.issuper():
        await message.delete()
        with open('users.json', 'r') as file:
            data = json.load(file)
            file.close()
        with open('users.json', 'w') as file:
            data[str(message.people.id)]['CAPS'] +=1
            json.dump(data, file, indent=4)
        if data[str(message.people.id)]['CAPS'] >=3:

            with open('users.json', 'w') as file:
                data[str(message.people.id)]['CAPS'] = 0
                data[str(message.people.id)]['Warn'] = 0
                json.dump(data, file, indent=4)
                file.close()
            emb = discord.Embed(

                title ="Нарушения",
                descption=f"* Ранне, у нарушителя было уже {data[str(message.author.id)]['warns'] - 1} нарушений, после 3 он будет плисать мне под дудки*",
                timestmp = message.created_at
            )

            emb.add_field(name="Канальчик", value= message.channel.mention, inline=True)
            emb.add_field(name="Пидорас", value= 'капс', inline=True)
            await message.people.ban(pricina="Вы пидорас")





Botik.run(tokenblyat)

