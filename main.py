import discord
from discord.ext import commands
import settings
from apis import *
import media_files as media
from datetime import timedelta

import time
import sys

# Hosting done :) Gracias Choco!

startTime = time.time()

logger = settings.logging.getLogger("bot")
client = commands.Bot(command_prefix="_", intents=discord.Intents.all())

# -----------------CHECKS----------------

@client.event
async def is_mick(ctx):
    return (ctx.author.id == mick_discord_id or ctx.author.id == hombrebicho_discord_id)

@client.event
async def is_verdi(ctx):
    return ctx.author.id == verdi_discord_id
    
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
    await client.get_channel(logia_chat_general_id).send("VIVO")

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

def handle_attachments(message, deleted_embed) -> list:
    length_attachments = len(message.attachments)
    new_attachments = []
    match length_attachments:
        case 0:
            return (deleted_embed, new_attachments)
        case 1:
            deleted_embed.set_image(url=make_attachment_persistent(message.attachments[0].url))
            return (deleted_embed, new_attachments) 
        case _:
            for i in message.attachments:
                new_attachments.append(make_attachment_persistent(message.attachments[i].url))
            return  (deleted_embed, new_attachments)

def make_attachment_persistent(url: str) -> str:
    if url[:26] == "https://cdn.discordapp.com":
            return ("https://media.discordapp.net" + url[26:])
    return url
    
                
@client.event
async def on_message_delete(message):
    logs_embed = discord.Embed(title=f"Mensaje eliminado.", description=f'Mensaje:\n**{message.clean_content}**', color=discord.colour.Colour.from_rgb(180,180,180), url=message.jump_url)
    logs_embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)

    embed, files = handle_attachments(message, logs_embed)
    await client.get_channel(auditlog_channel_id).send(embed=embed, files=files)
    
# -------------------DEBUG-------------------------

@client.command()
@commands.check(is_verdi)
async def die(ctx):
    await client.get_channel(logia_mbot_staff_channel_id).send(f'Muelto :c ||MelvinBot estuvo funcionando por {int((time.time()-startTime)/60)} minutos.||')
    print("Bot stopped by DIE")
    sys.exit()
@die.error
async def die_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(media.vid_chacarron)

@client.command()
@commands.check(channel_allowed)
async def report(ctx):
    await ctx.send(f'MelvinBot ready for duty!')

    #
    # Debug statement for information :) ↓
    #

    # await ctx.send(f"\n{ctx.author.name} {ctx.author.nick} {ctx.author.display_name}\n{ctx.author.roles} {ctx.author.avatar} {ctx.author.display_avatar}\n{ctx.author.desktop_status}")

# -------------------USER HELP---------------------

@client.command()
@commands.check(channel_allowed)
async def melvinbot(ctx):
    await ctx.send("MelvinBot presente, ¿necesitas ayuda con algo? Usa _helpme :)")

@client.command()
async def helpme(ctx):
    await ctx.author.send(media.helpme_text)

# --------------------BOT FEELINGS--------------

@client.command()
@commands.check(channel_allowed)
async def callate(ctx):
    if ctx.author.nick != None:
        await ctx.send(f"Perdón {ctx.author.nick} :(")
        return
    await ctx.send(f"Perdón {ctx.author.name} :(")

    
# *********************EMBEDS********************

@client.command()
@commands.check(channel_allowed)
async def fiestaspatrias(ctx):
    await ctx.send(media.logiaIM_fiestaspatrias)
    await ctx.send("> ¡Melvin les desea un feliz 18 de septiembre!")

@client.command()
@commands.check(channel_allowed)
async def arson(ctx):
    await ctx.send(media.logiaIM_arson)
    await ctx.send("> ¿Quien fuí? :smiling_imp:")

@client.command()
@commands.check(channel_allowed)
async def luismi(ctx):
    await ctx.send(media.logiaIM_luismiguel)

@client.command()
@commands.check(channel_allowed)
async def melvin420(ctx):
    await ctx.send(media.logiaIM_melvin420)
    await ctx.send("> Smoke weed everyday :melvinmarley::musical_note:")
    
@client.command()
@commands.check(channel_allowed)
async def locologo(ctx):
    await ctx.send(media.logiaIM_locologo)
    await ctx.send("> Amika date cuenta")

@client.command()
@commands.check(is_mick)
async def melvinseal(ctx):
    await ctx.send(media.logiaIM_melvinseal)
    await ctx.send("> ¡Felicidades!")
@melvinseal.error
async def melvinseal_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send("¡Sólo el Hombre Bicho oficial puede otorgar este galardón!")

@client.command()
@commands.check(channel_allowed)
async def completo(ctx):
    await ctx.send(media.im_completo)

@client.command()
@commands.check(channel_allowed)
async def prontuario(ctx):
    await ctx.send(media.logiaVID_prontuario)

@client.command()
@commands.check(channel_allowed)
async def roboc(ctx):
    await ctx.send(media.logiaIM_roboc)

@client.command()
@commands.check(channel_allowed)
async def pirate(ctx):
    await ctx.send(media.im_pirate)

@client.command()
@commands.check(channel_allowed)
async def erronea(ctx):
    await ctx.send(media.logiaIM_erronea)

@client.command()
@commands.check(channel_allowed)
async def durisimo(ctx):
    random_pic = media.getRandom(media.imagenes_durisimas)
    await ctx.send(random_pic)
    
@client.command()
@commands.check(channel_allowed)
async def starboard(ctx):
    starboard_tuple = media.getRandom(media.imagenes_starboard)
    await ctx.send(f'> {starboard_tuple[0]}')
    await ctx.send(starboard_tuple[1])
    
@client.command()
@commands.check(channel_allowed)
async def oiemelvin(ctx):
    random_answer = media.getRandom(media.answers)
    await ctx.send(random_answer)

@client.command()
@commands.check(channel_allowed)
async def thread(ctx):
    await ctx.send(media.im_thread_inquiry)

@client.command()
@commands.check(channel_allowed)
async def bomdia(ctx):
    await ctx.send(media.vid_bomdia)

# ----------------------MODERATING----------------------------

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    await member.kick(reason=reason)
    await ctx.send(f'**{member}** fue kickeado por {reason}. Chau!')
    await ctx.send(media.gif_peineta_garcia)
    embed = discord.Embed(title=f'{ctx.author.name} kickeó a {member} por {reason}.', color=discord.colour.Colour.from_rgb(200,0,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(media.gif_afilar)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para kickear.")
        
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    await member.ban(reason=reason, delete_message_days=0)
    await ctx.send(f'**{member}** fue baneado por {reason}, whoops!')
    await ctx.send(media.gif_trash_out)
    embed = discord.Embed(title=f'{ctx.author.name} baneó a {member} por {reason}.', color=discord.colour.Colour.from_rgb(200,0,0))
    channel = client.get_channel(auditlog_channel_id)
    await channel.send(embed=embed)
@ban.error 
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(media.gif_sniper_wait)
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
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para quitar un ban.")
        
@client.command()
@commands.has_permissions(manage_roles=True)
async def regalonear(ctx, member: discord.Member, *, reason="un motivo sin especificar"):
    role_regalon = ctx.guild.get_role(regalon_role_id)
    await member.add_roles(role_regalon, reason=reason, atomic=True)
    await ctx.send(f"**{member}** ha sido regaloneado")
    await ctx.send(media.gif_regalonear)
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
    match time[-1]:
        case "h":
            rtime_type = "horas"
            rtime_quantity = int(time[:-1])
            rtime_quantity_sec = rtime_quantity*60*60
        case "d":
            rtime_type = "días"
            rtime_quantity = int(time[:-1])
            rtime_quantity_sec = rtime_quantity*60*60*24
        case "m":
            rtime_type = "minutos"
            rtime_quantity = int(time[:-1])
            rtime_quantity_sec = rtime_quantity*60
        case "s":
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
_ = input("Press ENTER to close.")