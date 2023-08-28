# coding: utf-8

from misskey import Misskey

import random
import os
import time

misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
misskey_token = os.environ.get("MISSKEY_TOKEN")
misskey_address_2 = os.environ.get("MISSKEY_SERVER_ADDRESS_2")
misskey_token_2 = os.environ.get("MISSKEY_TOKEN_2")

moji4 = Misskey(misskey_address)
moji4.token = misskey_token
moji4_2 = Misskey(misskey_address_2)
moji4_2.token = misskey_token_2

# coding:utf-8
hiragana = ['ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'ゎ', 'わ', 'ゐ', 'ゑ', 'を', 'ん','ー']

a4 = random.choice(hiragana)
b4 = random.choice(hiragana)
c4 = random.choice(hiragana)
d4 = random.choice(hiragana)
moji4.notes_create(text=a4 + b4 + c4 + d4)
moji4_2.notes_create(text=a4 + b4 + c4 + d4)

print(a4+b4+c4+d4+'\n')
