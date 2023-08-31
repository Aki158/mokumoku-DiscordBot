import discord

import getNextTargetDate


# 自分のBotのアクセストークンを設定する
TOKEN = ''
# 指定したいチャンネルIDを設定する(''を削除しチャンネルIDの数値を設定)
CHANNEL_ID = ''

# 接続に必要なオブジェクトを生成する
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    friday = getNextTargetDate.getNextTargetDate('金')
    saturday = getNextTargetDate.getNextTargetDate('土')
    sunday = getNextTargetDate.getNextTargetDate('日')

    strFront = '@everyone \n' + \
        '下記日程でもくもく会を開催します！\n・日程：' + \
        'よければ参加ください。\n\n'
    strBack = '・場所：Discord_もくもく①\n・応募期限：' + friday + \
        '\n・応募方法：この投稿に👍をください\n'
    strArr = ['  9:00-12:00\n','  20:00-22:00\n']

    # botが起動するまで待つ
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    # botがメッセージを送信する
    await channel.send(strFront + saturday + strArr[0] + strBack)
    await channel.send(strFront + saturday + strArr[1] + strBack)
    await channel.send(strFront + sunday + strArr[0] + strBack)
    await channel.send(strFront + sunday + strArr[1] + strBack)

# Botの起動とDiscordサーバーへの接続する
client.run(TOKEN)