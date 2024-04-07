import discord
from discord.ext import commands
import settings
from apis import *
from media_files import imagenes_durisimas, imagenes_starboard, gif_trash_out, gif_peineta_garcia, gif_regalonear
from random import randint
from datetime import timedelta

import time
import sys

#TODO Hosting (temp fix in place, just keep script running on PC)


startTime = time.time()

logger = settings.logging.getLogger("bot")
client = commands.Bot(command_prefix="_", intents=discord.Intents.all())

# -----------------CHECKS----------------

@client.event
async def is_mick(ctx):
    if ctx.author.id == mick_discord_id or ctx.author.id == hombrebicho_discord_id:
        return True
    else:
        return False

@client.event
async def is_verdi(ctx):
    if ctx.author.id == verdi_discord_id:
        return True
    else:
        return False
    
@client.event
async def channel_allowed(ctx):
    if ctx.channel.id in allowed_channels:
        return True
    else: 
        print(f'No puedes usar el bot en este canal: {ctx.channel.id}')
        return False

# ----------------BOT EVENTS------------------

@client.event
async def on_ready():
    logger.info(f"User: {client.user}; User ID: {client.user.id}")
    print("MelvinBot is LIVE ON AIR!")
    await client.get_channel(1180314714123817171).send("VIVO")

# ----------------AUDIT LOGS-------------------

@client.event
async def on_member_join(member):
    channel = client.get_channel(logia_welcome_channel_id)
    await channel.send(f"Ah, sangre fresca! Que pase **{member}**!")
    await client.get_channel(auditlog_channel_id).send(embed=discord.Embed(title=f"{member} se unió a la Logia.", color=discord.colour.Colour.from_rgb(200,200,200)))

@client.event
async def on_member_remove(member):
    await client.get_channel(auditlog_channel_id).send(embed=discord.Embed(title=f"{member} se fue de la Logia.", color=discord.colour.Colour.from_rgb(20,20,20)))
    
@client.event
async def on_message_edit(before, after):
    if before.author.name != "MelvinBot" and before.clean_content != after.clean_content and before.author.id != carl_bot_id:
        modified_embed = discord.Embed(title=f"Mensaje modificado.", description=f'Antes:\n**{before.clean_content}**\nDespués:\n**{after.clean_content}**', color=discord.colour.Colour.from_rgb(180,190,180), url=after.jump_url)
        modified_embed.set_author(name=before.author.name, icon_url=before.author.avatar.url)
        await client.get_channel(auditlog_channel_id).send(embed=modified_embed)

@client.event
async def on_message_delete(message):
    deleted_embed = discord.Embed(title=f"Mensaje eliminado.", description=f'Mensaje:\n**{message.clean_content}**', color=discord.colour.Colour.from_rgb(180,180,180), url=message.jump_url)
    deleted_embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
    lenght_attachments = len(message.attachments)
    if lenght_attachments != 0:
        if lenght_attachments == 1:
            if message.attachments[0].url[:26] == "https://cdn.discordapp.com":
                deleted_embed.set_image(url="https://media.discordapp.net"+message.attachments[0].url[26:])
            else:
                deleted_embed.set_image(url=message.attachments[0].url)
        else:
            deleted_embed.set_image(url=message.attachments[0].url)
            for i in message.attachments:
                if message.attachments[0].url[:26] == "https://cdn.discordapp.com":
                    deleted_embed.set_image(url="https://media.discordapp.net"+message.attachments[0].url[26:])
                else:
                    deleted_embed.set_image(url=message.attachments[0].url)
            
    await client.get_channel(auditlog_channel_id).send(embed=deleted_embed)
    
# -------------------DEBUG-------------------------

@client.command()
@commands.check(is_verdi)
async def die(ctx):
    await client.get_channel(1180314714123817171).send(f'Muelto :c ||MelvinBot estuvo funcionando por {int((time.time()-startTime)/60)} minutos.||')
    print("Bot stopped by DIE")
    sys.exit()
@die.error
async def die_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('https://youtu.be/y75MGw5pcyc?si=KSHRklVr_C8ljW0C&t=14')

@client.command()
@commands.check(channel_allowed)
async def report(ctx):
    await ctx.send(f'MelvinBot ready for duty!')
    # await ctx.send(f"\n{ctx.author.name} {ctx.author.nick} {ctx.author.display_name}\n{ctx.author.roles} {ctx.author.avatar} {ctx.author.display_avatar}\n{ctx.author.desktop_status}")

# -------------------USER HELP---------------------

@client.command()
@commands.check(channel_allowed)
async def melvinbot(ctx):
    await ctx.send("MelvinBot presente, ¿necesitas ayuda con algo? Usa _helpme :)")

@client.command()
async def helpme(ctx):
    helpme_text = "Comandos informativos:\n- _melvinbot\n- _helpme\n\nComandos recreacionales:\n- _callate\n- _erronea\n- _prontuario\n- _fiestaspatrias\n- _arson\n- _luismi\n- _melvin420\n- _locologo\n- _ex\n- _pirate\n- _completo\n- _roboc\n- _durisimo\n- _starboard\n- _oiemelvin [pregunta]\n- _melvinseal  [MICK EXCLUSIVE]\n_thread\n\nComandos moderación:\n- _ban [@usuario] [motivo]\n- _unban [@usuario/id]\n- _kick [@usuario] [motivo]\n- _regalonear [@usuario] [motivo]\n- _desregalonear [@usuario] [motivo]\n- _mimir [@usuario] [tiempo] ((formato: Xs / Xm / Xh / Xd | Ejemplo: 12h | Máx 28 días))\n- _despertar [@usuario] [motivo]"
    await ctx.author.send(helpme_text)

# --------------------BOT FEELINGS--------------

@client.command()
@commands.check(channel_allowed)
async def callate(ctx):
    if ctx.author.nick == None:
        await ctx.send(f"Perdón {ctx.author.name} :(")
    else:
        await ctx.send(f"Perdón {ctx.author.nick} :(")
    
# *********************EMBEDS********************

@client.command()
@commands.check(channel_allowed)
async def fiestaspatrias(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1179987125953888407/image.png?ex=657bc7a5&is=656952a5&hm=66d2407194b73c85435c3496532ae01e8fd4faeae6d3d3479b36b4c6cac7c30d&")
    await ctx.send("> ¡Melvin les desea un feliz 18 de septiembre!")

@client.command()
@commands.check(channel_allowed)
async def arson(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1179989546629345391/house.png?ex=657bc9e7&is=656954e7&hm=076b88ecac1cea730ac8663177c67a0bf5ac9d8541d82b09f230d92aa55d0772&")
    await ctx.send("> ¿Quien fuí? :smiling_imp:")

@client.command()
@commands.check(channel_allowed)
async def luismi(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1179990115414724688/luismi.png?ex=657bca6e&is=6569556e&hm=55e6329acb696e6955c38cbea437247575cbdde6e093c594dc61babb7a188b5c&")

@client.command()
@commands.check(channel_allowed)
async def melvin420(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1179990996482805780/mel.png?ex=657bcb40&is=65695640&hm=581a116d063008c40ab5917572a90e9f7e83fe41c1faa0ba7d1bccb119a6bcab&")
    await ctx.send("> Smoke weed everyday :melvinmarley::musical_note:")
    
@client.command()
@commands.check(channel_allowed)
async def locologo(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1179991723087241236/melvinhelp.png?ex=657bcbed&is=656956ed&hm=c549a681fd064271a4ad6a68ad42520b72b6a81428eacb0eec27dc3a72c00dba&")
    await ctx.send("> Amika date cuenta")

@client.command()
@commands.check(channel_allowed)
async def ex(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1180176992440684635/dapr_ex.png?ex=657c7879&is=656a0379&hm=3a7d48a25cef5613bafa83c60720c87b97b8ec688a90988c326bcbee77b9026a&")

@client.command()
@commands.check(is_mick)
async def melvinseal(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1180000612692262962/Melvinseal.png?ex=657bd435&is=65695f35&hm=97cd0bdd6a4224c90499ea2195a5ba88751f529ff2fdb1f6f0da46251b35e11c&")
    await ctx.send("> ¡Felicidades!")
@melvinseal.error
async def melvinseal_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("¡Sólo el Hombre Bicho oficial puede otorgar este galardón!")

@client.command()
@commands.check(channel_allowed)
async def completo(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1020780174310121613/1180275900839886879/l7bz4h21a7z71.jpg?ex=657cd497&is=656a5f97&hm=1dde1c331cdccbb69aa371d799fc31c4c211a89a4d4aa4d5f534f98a16948304&")

@client.command()
@commands.check(channel_allowed)
async def prontuario(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1020776041851129923/1128503634318069820/InShot_20230711_214832802.mp4?ex=6594bd69&is=65824869&hm=a2bc77674c03c5f95d7f06db8e7c536eda604edb2935ad1435ba577c42e53e4f&")

@client.command()
@commands.check(channel_allowed)
async def roboc(ctx):
    await ctx.send("https://media.discordapp.net/attachments/1020780174310121613/1180276009237495858/unknown-1444-3.png?ex=657cd4b1&is=656a5fb1&hm=be4d2667985568e5dd967b9b18a88ce8e0e4fef850afe46d5cff01c36824ecd3&=&")

@client.command()
@commands.check(channel_allowed)
async def pirate(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1180327977138000023/v51mxsd4nqub1.png?ex=657d0517&is=656a9017&hm=c83e3e920d5032c389f771f1af7b911dfa06803659de3643f7cab4b09cb07d66&")

@client.command()
@commands.check(channel_allowed)
async def erronea(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1179960160828018750/1186778931861393549/image.png?ex=65947d02&is=65820802&hm=9a09a5a46dc585163ce85013c4f8f91a0a8452cb12b7e0e466d08c2cd9f75122&")

@client.command()
@commands.check(channel_allowed)
async def durisimo(ctx):
    random_pic = imagenes_durisimas[randint(0, len(imagenes_durisimas)-1)]
    await ctx.send(random_pic)
    
@client.command()
@commands.check(channel_allowed)
async def starboard(ctx):
    starboard_tuple = imagenes_starboard[randint(0, len(imagenes_starboard)-1)]
    await ctx.send(f'> {starboard_tuple[0]}')
    await ctx.send(starboard_tuple[1])
    
@client.command()
@commands.check(channel_allowed)
async def oiemelvin(ctx):
    answers = (
        "Hay una cosa que se llama Google, demás que sabe",
        "compita no ve que estoy tratando de tomarme mi MelvinCola, vaya a webear a otro lado",
        "jaja sí, oie se me está acabando la batería, hablamos la próxima semana?",
        "loco soy un roboc, que querí que te diga ???",
        "honestamente mimportaunpico :cursedwhyme:",
        "Me gustaría atenderte pero veo que tu carnet está vencido, dirigete al edificio de la SDL https://discord.com/channels/1020776041024864350/1154128025013715085 y vuelve otro día",
        "Me parece que te falta avivarte, date una vuelta por el Centro Mundial de Avivamiento **URGENTE** https://discord.com/channels/1020776041024864350/1172551157344911481",
        "luego de considerar cuidadosa y exhaustivamente tu pregunta, he llegado a la conclusión que ya no quiero seguir trabajando en esto",
        "sigue tus pulmones o algo así, ahora dejame piola que estoy jugando DGS",
        "mmm no, y tampoco fui yo el que quemó esa casa, a mi no me engañan :smiling_imp:",
        "‎",
        "bruh",
        "Después de leer tu pregunta voy a tener que pasarme por https://discord.com/channels/1020776041024864350/1088598726790094879 un rato...",
        "se nota que teni harto tiempo libre oye",
        "Da lo miiismo weon! da lo mismo!",
        "y dale con que las gallinas mean",
        "Te respondería pero no me es interesante pregunta",
        "hazle caso a tu :heart:. digan lo que digan los demás",
        "No sé wn. sólo soy un bot, y no me pagan lo suficiente para hacer estas cosas.",
        "no entendí bien la pregunta, ¿los policias sabían que asuntos internos les tendia una trampa?",
        "Hoy no se responde, mañana sí",
        "Sí, pero no, y a la vez tampoco",
        "No te puedo decir que si, ni que no, si no que todo lo contrario",
        "Te responderé Soon ™️",
        "Como voy a saber aweonao, soy un roboc",
        "Si me dieran sinko peso por cada mensaje estúpido que leo, me harías millonario",
        "Error 404: Interés not found",
        "Sí.",
        "oie y si le vas a preguntar a otra persona mejor",
        "La comunicación es la solución para muchos problemas, practicala... pero con otra persona por favor",
        "No responderé preguntas hasta que mi abogado Oso esté presente"
    )
    random_answer = answers[randint(0, len(answers)-1)]
    await ctx.send(random_answer)

@client.command()
@commands.check(channel_allowed)
async def thread(ctx):
    await ctx.send("https://media.discordapp.net/attachments/1179960160828018750/1193317307959750717/7c8.png?ex=65ac4658&is=6599d158&hm=4dfc48264b5bb9ea10fa6d17acdb7426542ca898962a8f9e8da6160325a5d1a9&=&format=webp&quality=lossless&width=277&height=670")

# ----------------------MODERATING----------------------------

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    await member.kick(reason=reason)
    await ctx.send(f'**{member}** fue kickeado por {reason}. Chau!')
    await ctx.send(gif_peineta_garcia)
    embed = discord.Embed(title=f'{ctx.author.name} kickeó a {member} por {reason}.', color=discord.colour.Colour.from_rgb(200,0,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("https://tenor.com/view/spider-man-norman-osborn-knife-sharpening-green-goblin-willem-dafoe-gif-20955065")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para kickear.")
        
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    await member.ban(reason=reason, delete_message_days=0)
    await ctx.send(f'**{member}** fue baneado por {reason}, whoops!')
    await ctx.send(gif_trash_out)
    embed = discord.Embed(title=f'{ctx.author.name} baneó a {member} por {reason}.', color=discord.colour.Colour.from_rgb(200,0,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@ban.error 
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("https://tenor.com/view/sniper-tf2-waiting-piss-gif-27404794")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para banear.")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User, *, reason="un motivo sin especificar"):
    guild = ctx.guild
    await guild.unban(user=user)
    await ctx.send(f'El usuario {user} es bienvenido otra vez')
    await client.get_channel(auditlog_channel_id).send(embed=discord.Embed(title=f'{ctx.author.name} le quitó el ban a {user} ||por {reason}||', color=discord.colour.Colour.from_rgb(0,200,0)))
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("¿A quién quieres desbanear?")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para quitar un ban.")
        
@client.command()
@commands.has_permissions(manage_roles=True)
async def regalonear(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    role_regalon = ctx.guild.get_role(regalon_role_id)
    await member.add_roles(role_regalon, reason=reason, atomic=True)
    await ctx.send(f"**{member}** ha sido regaloneado")
    await ctx.send(gif_regalonear)
    embed = discord.Embed(title=f'{ctx.author.name} regaloneó a {member} por {reason}.', color=discord.colour.Colour.from_rgb(200,0,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@regalonear.error
async def regalonear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para regalonear :(")
    
@client.command()
@commands.has_permissions(manage_roles=True)
async def desregalonear(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    role_regalon = ctx.guild.get_role(regalon_role_id)
    await member.remove_roles(role_regalon, reason=reason, atomic=True)
    await ctx.send(f"**{member}** ya no es regalón :(")
    embed = discord.Embed(title = f'{ctx.author.name} desregaloneó a {member} ||por {reason}.||', color=discord.colour.Colour.from_rgb(0,200,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@desregalonear.error
async def desregalonear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para desregalonear :(")
        
@client.command()
@commands.has_permissions(moderate_members=True)
# MAX 28 DÍAS
async def mimir(ctx, member: discord.Member, *, time="1h", reason="un motivo sin especificar"):
    if time[-1] == "h":
        rtime_type = "horas"
        rtime_quantity = int(time[:-1])
        rtime_quantity_sec = rtime_quantity*60*60
    elif time[-1] == "d":
        rtime_type = "días"
        rtime_quantity = int(time[:-1])
        rtime_quantity_sec = rtime_quantity*60*60*24
    elif time[-1] == "m":
        rtime_type = "minutos"
        rtime_quantity = int(time[:-1])
        rtime_quantity_sec = rtime_quantity*60
    elif time[-1] == "s":
        rtime_type = "segundos"
        rtime_quantity = int(time[:-1])
        rtime_quantity_sec = rtime_quantity

    await ctx.send(f"**{member}** se va a mimir por {rtime_quantity} {rtime_type} zZzZZz")
    embed = discord.Embed(title=f'{ctx.author.name} mandó a mimir a {member}.', color=discord.colour.Colour.from_rgb(200,0,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
    await member.timeout(timedelta(seconds=rtime_quantity_sec), reason=reason)
@mimir.error
async def mimir_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para mandar a mimir :(")

@client.command()
@commands.check(channel_allowed)
@commands.has_permissions(moderate_members=True)
# MAX 28 DÍAS
async def despertar(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    await ctx.send(f"**{member}** despertó con un balde de agua fría")
    await member.timeout(timedelta(seconds=0), reason=reason)
    embed = discord.Embed(title=f'{ctx.author.name} despertó a {member} ||por {reason}.||', color=discord.colour.Colour.from_rgb(0,200,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@despertar.error
async def despertar_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para despertar a alguien :(")

   
client.run(apimelvinbot, root_logger=True)