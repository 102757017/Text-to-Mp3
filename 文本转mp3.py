# coding: utf-8
#!/usr/bin/python
import subprocess
status = subprocess.run("pip install --upgrade edge-tts",shell=True, capture_output=True,text=True )
print(status.stdout)
print(status.stderr)

import asyncio
import edge_tts
import os
import sys
from pathlib import Path
from edge_tts import VoicesManager
import pprint

#  所有基于模块的使用到__file__属性的代码，在源码运行时表示的是当前脚本的绝对路径，但是用pyinstaller打包后就是当前模块的模块名（即文件名xxx.py）
#  因此需要用以下代码来获取exe的绝对路径
if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    root = Path(sys._MEIPASS)
else:
    root = Path(__file__).parent
print(root)
os.chdir(root)

#要转换的文本
TEXT = '''
Link was a boy who lived in a cottage by the sea. He liked to sail his boat and look for stones on the beach. One day, he found a signpost that said "Summit of the World". He was curious and decided to join the adventure. He sailed his boat to the base of a big mountain. He saw a puzzle on the wall. It said "What if you had a flame emitter?". He thought it was a silly question. He did not bother with it and crept into a cave. Inside the cave, he saw a theatre. There were many people in costumes and masks. They were acting out a story about Tears of the Kingdom. Link liked the story. He wanted to watch it. But then, he saw something that made him gasp. It was a flame emitter! It was silver and shiny. It looked like a brilliant toy. He wanted to have it. He pulled it from the wall and ran away. He did not expect anyone to notice. But he was wrong. The flame emitter was part of the show. It was used to make fire effects. Without it, the show could not go on. The actors were angry. They chased after Link. They shouted at him to bring back the flame emitter. Link was scared. He ran out of the cave and into his boat. He sailed away as fast as he could. But he did not know how to use the flame emitter. He pressed a button and it leaked fire. The fire burned his boat and his clothes. Link jumped into the water. He swam to the shore. He felt cold and wet. He also felt shame. He wished he had not taken the flame emitter. He wished he had listened to the puzzle. He wished he had left it alone. He looked at the flame emitter in his hand. It was useless now. It did not work anymore. He threw it into the sea and watched it vanish. He walked back to his cottage. He hoped no one would complain about him. He learned his lesson. He was not an expert on flame emitters. He should not take things that did not belong to him.

'''

#设置角色
VOICE = "en-US-AriaNeural"
VOICE = "en-GB-LibbyNeural"
OUTPUT_FILE = "test.mp3"



async def amain() -> None:
    #调整语速、音量
    communicate = edge_tts.Communicate(TEXT, VOICE,rate="-15%",volume="+90%")
    await communicate.save(OUTPUT_FILE)
    print("转换已完成")


    #列出角色清单
    voices = await VoicesManager.create()
    #中文清单
    #voice = voices.find(Locale="zh-CN")   
    #美式英语清单
    #voice = voices.find(Locale="en-US")
    #英式英语清单
    voice = voices.find(Locale="en-GB")
    #pprint.pprint(voice)
    for v in voice:
        print(v["Gender"],v["ShortName"])



if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()