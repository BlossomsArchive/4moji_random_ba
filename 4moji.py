# coding: utf-8

from misskey import Misskey

import random
import os
import time

misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
misskey_token = os.environ.get("MISSKEY_TOKEN")

moji4 = Misskey(misskey_address)
moji4.token = misskey_token

# coding:utf-8
hiragana = ['ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'ゎ', 'わ', 'ゐ', 'ゑ', 'を', 'ん','ー']

a4 = random.choice(hiragana)
b4 = random.choice(hiragana)
c4 = random.choice(hiragana)
d4 = random.choice(hiragana)
while True:
    try:
        moji4.notes_create(text=a4 + b4 + c4 + d4)
    except:
        time.sleep(300)
    else:
        break
    
print(a4+b4+c4+d4+'\n')
