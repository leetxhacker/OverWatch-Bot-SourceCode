# $ <--! Modules !--> $
import os
os.system("pip install -U nextcord")
import nextcord
from nextcord.ext import commands
import datetime
import psutil
from colorama import Fore

# $ <--! Intents !--> $
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# $ <--! Define !--> $
prefix = "o!"
token = "MTA2MDUwMzIwMTNjQ1MTg0MQ.GonasmMnK69XYFvq75rGlZThKNUcISysZ30XWQ0" # Enter Your Bot's Token!
client = commands.Bot(command_prefix=prefix,intents=intents,shard_count=2) # Manually Sharded!
client.launch_time = datetime.datetime.utcnow()
client.remove_command("help")
client.owner_ids = [853810604842287136, 1053255772949196820] # Owner ID's
client.load_extension("onami")

# <--! Vars !-->
footer = "OverWatch, Watching Everything!"
inv = "https://bit.ly/overwatch-invite"
supp = "https://discord.gg/vQXmhpkRzF"
# $ <--! On_Ready !--> $
@client.event
async def on_ready():
  print(f"{Fore.GREEN}- Log In Success As {client.user}\n\n[ Stats @{client.user}]\n- Guilds: {len(client.guilds)}\n- Users: {len(client.users)}")

# <--! Temporary Help Cmd !-->
@client.command()
async def idkkhelpp(ctx):
  help = nextcord.Embed(
    title=f"Temporary Help-Menu",
    description=
    f"**__All Commands__**\n```txt\nping, uptime, botinfo, roleinfo, purge, giverole, invite, mc, users, guilds, boosts, takerole, sicon, sbanner, av, ban, unban, kick, nickname, hide, unhidem lock, unlock, serverinfo```\n\n**Just Made For Storing All Cmds**\n**This Menu Will Be Changed In Final Stage After Completetion**",
    colour=0x2f3136)
  await ctx.send(embed=help)

@client.slash_command(description="Show's Bots Help Menu!")
async def help(ctx):
  help = nextcord.Embed(
    title=f"Over-Watch", description=f"• Prefix: `/` : Use `/help`\n• Total Commands: {len(client.commands)}\n• Type: `/help <command | module>` To Get Started\n• [Get OverWatch]({inv}) : [Support]({supp})",colour=0xf9b13a)
  help.add_field(name="<:flaws_next:1079342823091998860> Moderation Cmds",value="`giverole`, `takerole`, `ban`, `kick`, `unban`, `hide`, `unhide`, `lock`, `unlock`, `nickname`",inline=False)
  help.add_field(name="<:flaws_next:1079342823091998860> Public Cmds",value="`roleinfo`, `invite`, `mc`, `boosts`, `servericon`, `serverbanner`, `serverinfo`, `av`",inline=False)
  help.add_field(name="<:flaws_next:1079342823091998860> Info Cmds",value="`ping`, `botinfo`, `uptime`, `invite`, `users`, `guilds`\n\n**__Adding Up More Cmds__**",inline=False)
  help.set_thumbnail(url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
  help.set_footer(text=f"{footer}",icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
  await ctx.send(embed=help)

@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.content.startswith(f'<@{client.user.id}>'):
    embed = nextcord.Embed(color=0xf9b13a,
    description = f"Hey, My Prefix Is `/` | Use: `/help`")
    await message.reply(embed=embed)

# $ <--! Basic/Info Cmds --!>, | Slash & Without Slash Both3

# SLASH

@client.slash_command(description="Show's Server Member-Count")
async def membercount(ctx):
  await ctx.send(f"Member Count - {ctx.guild.member_count}")

@client.slash_command(description="Show's Bot Total Users")
async def users(ctx):
  await ctx.send(f"OverWatch Users - {len(client.users)}")

@client.slash_command(description="Show's Bots Round Off Latency!")
async def ping(ctx):
  await ctx.send(f"OverWatch's Latency: {round(client.latency * 1000)}ms!")

@client.slash_command(description="Show's Bot Total Guilds")
async def guilds(ctx):
  await ctx.send(f"OverWatch Servers - {len(client.guilds)}")

@client.slash_command(description="Show's Server Boost Count")
async def boosts(ctx):
  await ctx.send(f"Your Server Has `{ctx.guild.premium_subscription_count}` Boosts")

# SLASH PART 1 ENds

@client.slash_command(description="Gives You Bot Invite Link")
async def invite(ctx):
  inv = nextcord.Embed(
    title=f"OverWatch Links",
    description=
    f"[Click Here To Invite Me](https://bit.ly/overwatch-inv)\n[Click To Join Support Server](https://discord.gg/4FzqpXyGN2)",
    color=0x2f3136)
  inv.set_footer(
    text=f"{footer}",
icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024"
  )
  await ctx.send(embed=inv)

@client.slash_command(description="Show's Bot's Uptime")
async def uptime(ctx):
  delta_uptime = datetime.datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  await ctx.send(
    f"OverWatch's Uptime: {days} Day, {hours} Hours, {minutes} Mins, {seconds} Secs"
  )


def get_ram_usage():
  mem = psutil.virtual_memory()
  total_mem = mem.total / 1e9
  used_mem = mem.used / 1e9
  return f'Total RAM: {total_mem:.2f}GB\nUsed RAM: {used_mem:.2f}GB'

def get_cpu_usage():
  cpu_percent = psutil.cpu_percent(interval=1)
  return f'CPU Usage: {cpu_percent}%'

@client.slash_command(description="Show's BotInfo")
async def botinfo(ctx):
  shards = "2"
  idk = nextcord.utils.get(ctx.guild.members, id=client.user.id)
  all_c = sum(1 for channel in ctx.guild.channels
              if idk.guild_permissions.view_channel)
  delta_uptime = datetime.datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  fuck_U = nextcord.Embed(
    title=f"OverWatch's Bot-Info",
    description=
    f"**__Basic Info__**\nName: {client.user}\nMention: <@{client.user.id}>\nDeveloper: [@leet#6926](https://discord.com/users/853810604842287136)\nLanguage: [Python 3.8.10](https://www.python.org/)\nLibrary: [NextCord 2.4.0](https://docs.nextcord.dev/)",
    color=0x2f3136)
  fuck_U.add_field(
    name=f"**__Basic Stats__**",
    value=
    f"Users: {len(client.users)}\nGuilds: {len(client.guilds)}\nCmds: {len(client.commands)}\nChannels: {all_c}",
    inline=False)
  fuck_U.add_field(
    name=f"**__System Info__**",
    value=f"Shards: {shards}\nPing: {round(client.latency*1000)}ms\n{get_ram_usage()}\n{get_cpu_usage()}",
    inline=False)
  fuck_U.add_field(
    name=f"**__Uptime Info__**",
    value=f"- {days} Day, {hours} Hours, {minutes} Mins, {seconds} Secs",
    inline=False)
  fuck_U.set_footer(
    text=f"{footer}",
icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024"
  )
  await ctx.send(embed=fuck_U)


@client.slash_command(description="Show's Info Of Particular Role")
async def roleinfo(ctx, role: nextcord.Role = None):
  if role == None:
    await ctx.send(f"You Didn't Mentioned Any Role Above, Please Do Mention!")
  else:
    perms = ', '.join(
      [str(rolex[0]).replace("_", " ").title() for rolex in role.permissions if rolex[1]])
    role = nextcord.Embed(
      title=f"Role Info",
      description=
      f"ID: {role.id}\nName: {role.name}\nMention: {role.mention}\nPosition: {role.position}\nHex: {role.color}\nHoist: {role.hoist}\nMentionable?: {role.mentionable}\nIntegrations?: {role.managed}\n",
      color=0x2f3136)
    role.add_field(name=f"**__Role Permissions__**",
                   value=f"```txt\n{perms}```",
                   inline=False)
    role.set_footer(
      text=f"{footer}",
icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
    await ctx.send(embed=role)

@client.slash_command(description="Show's Banner Of Server")
async def serverbanner(ctx):
  try:
    em = nextcord.Embed(colour=0x2f3136)
    em.set_image(url=ctx.guild.banner.url)
    em.set_footer(text=f"{footer}",
                  icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
    await ctx.send(embed=em)
  except AttributeError:
    await ctx.send(f"Server Doesn't Have Any Banner! :(")

@client.slash_command(description="Show's User Avatar")
async def showavatar(ctx, member: nextcord.Member = None):
    if member is None:
        member = ctx.author
    emb = nextcord.Embed(color=0x2f3136, title=f"Avatar Of {member.name}")
    emb.set_image(url=member.avatar.url)
    emb.set_footer(text=f"{footer}",icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
    await ctx.send(embed=emb)

@client.slash_command(description="Show's Server Icon")
async def servericon(ctx):
  try:
    em = nextcord.Embed(colour=0x2f3136)
    em.set_image(url=ctx.guild.icon.url)
    em.set_footer(text=f"{footer}",
                  icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
    await ctx.send(embed=em)
  except AttributeError:
    await ctx.send(f"Server Doesn't Have Any Icon! :(")

@client.slash_command(description="Show's ServerInfo")
async def serverinfo(ctx):
  si = nextcord.Embed(
    title=f"About {ctx.guild.name}",
    description=
    f"**__Basics__**\nName: {ctx.guild.name}\nID: {ctx.guild.id}\nOwner: {ctx.guild.owner.mention}\nMembers: {ctx.guild.member_count}",
    color=0x2f3136)
  si.add_field(
    name=f"**__Channel Info__**",
    value=
    f"Text: {len(ctx.guild.text_channels)}\nVoice: {len(ctx.guild.voice_channels)}\n",
    inline=False)
  si.add_field(
    name=f"**__Boost Info__**",
    value=
    f"Boost Count: {ctx.guild.premium_subscription_count}\nBoost Tier: {ctx.guild.premium_tier}",
    inline=False)
  si.add_field(
    name=f"**__Extra Info__**",
    value=
    f"Verification Level: {str(ctx.guild.verification_level)}\nTotal Emojis: {len(ctx.guild.emojis)}\nTotal Roles: {len(ctx.guild.roles)}\nHighest Role: @{ctx.guild.roles[-1]}",
    inline=False)
  si.set_footer(
    text=f"{footer}",
    icon_url="https://cdn.discordapp.com/avatars/1060503201356451841/6040eb744fddde75a0a14b4e5ffc36c9.png?size=1024")
  await ctx.send(embed=si)


@client.slash_command(description="Del/Purges Messages!")
async def purge(ctx, limit: int):
  if limit <= 0:
    await ctx.send(
      "Error, Your Value Is Incorrect Please Provide Some Value Greater Than 0"
    )
    return
  elif limit > 200:
    await ctx.send("Sorry, Purge Limit Is 200 At Once")
    limit = 200
  deleted = await ctx.channel.purge(limit=limit + 1)
  await ctx.send(f"Deleted {len(deleted)-1} Msg!")

@client.slash_command(description="Adds Particular Role To User")
@commands.has_guild_permissions(manage_roles=True)
async def addrole(ctx, member: nextcord.Member, role: nextcord.Role):
  guild = ctx.guild
  if guild.me.top_role >= ctx.author.top_role:
    await ctx.send(f"Your Role Must Be Higher Than Me!")
    return
  elif member.top_role >= ctx.author.top_role:
    await ctx.send(f"Your Role Must Be Higher Than : {member}")
  else:
    await member.add_roles(role)
    await ctx.send(f"Changed Roles For @{member.name} : Added `@{role.name}`")

@client.slash_command(description="Removes Particular Roles From User")
@commands.has_guild_permissions(manage_roles=True)
async def rr(ctx, member: nextcord.Member, role: nextcord.Role):
  guild = ctx.guild
  if guild.me.top_role >= ctx.author.top_role:
    await ctx.send(f"Your Role Must Be Higher Than Me!")
    return
  elif member.top_role >= ctx.author.top_role:
    await ctx.send(f"Your Role Must Be Higher Than : {member}")
  else:
    await member.remove_roles(role)
    await ctx.send(f"Changed Roles For @{member.name} : Removed `@{role.name}`")

@client.slash_command(description="Hides Channel")
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: nextcord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{ctx.channel.mention} Is Now Hidden")

@client.slash_command(description="Unlocks Channel")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: nextcord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{ctx.channel.mention} Is Now Unlocked")

@client.slash_command(description="Locks Channel")
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: nextcord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{ctx.channel.mention} Is Now Locked")

@client.slash_command(description="Unhides Channel")
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel: nextcord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"{ctx.channel.mention} Is Now Visible")  
  
@client.slash_command(description="Changes Nickname Of User")
@commands.has_permissions(manage_nicknames=True)
async def nickname(ctx, member: nextcord.Member, *, nick):
    odkl = member.name
    await member.edit(nick=nick)
    await ctx.send(f"Changed Nick of `@{odkl}` To `@{nick}`") 

@client.slash_command(description="Kick's User From Server")
@commands.has_permissions(kick_members=True)
async def kick(ctx, mem: nextcord.Member = None):
  if mem == None:
    await ctx.send(f"You Haven't Mentioned Any Member To Kick!")
  elif mem.top_role >= ctx.author.top_role:
    await ctx.send(f"You Must Have Higher Role Than @{mem}")
  elif mem.top_role >= ctx.guild.me.top_role:
    await ctx.send(f"I Don't Have Permission To Perform This Action")
  else:
    try:
      await mem.kick(reason=f"{ctx.author}")
      await ctx.send(f"Kicked - @{mem}")
    except:
      await ctx.send(f"Error While Kicking @{mem}")

@client.slash_command(description="Ban's User From Server")
@commands.has_permissions(kick_members=True)
async def ban(ctx, mem: nextcord.Member = None):
  if mem == None:
    await ctx.send(f"You Haven't Mentioned Any Member To Ban!")
  elif mem.top_role >= ctx.author.top_role:
    await ctx.send(f"You Must Have Higher Role Than @{mem}")
  elif mem.top_role >= ctx.guild.me.top_role:
    await ctx.send(f"I Don't Have Permission To Perform This Action")
  else:
    try:
      await mem.ban(reason=f"{ctx.author}")
      await ctx.send(f"Banned - @{mem}")
    except:
      await ctx.send(f"Error While Banning @{mem}")

@client.slash_command(description="Unban's User From Server")
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: int):
  user = await client.fetch_user(user)
  try:
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned - @{user}")
  except:
    await ctx.send(f"Can't Unban - @{user}")


client.run(token)
