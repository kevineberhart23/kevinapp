from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime



@StreamBot.on_message(filters.private & filters.regex("وضعیت سرور"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'● سرور\n' \
            f'•  آپتایم: [ {currentTime} ]\n' \
            f'• حجم هارد سرور: [ {total} ]\n' \
            f'• فضای استفاده شده: [ {used} ]\n' \
            f'• فضای باقی مانده: [ {free} ]\n\n' \
            f'• سرعت آپلود: [ {sent} ]\n' \
            f'• سرعت دانلود: [ {recv} ]\n' \
            f'• سی پی یو استفاده شده: [ {cpuUsage}% ]\n' \
            f'• رم استفاده شده: [ {memory}% ]\n' \
            f'• فضای استفاده شده: [ {disk}% ]'
  await update.reply_text(botstats)
