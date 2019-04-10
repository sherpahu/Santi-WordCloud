#-*- coding: utf-8 -*-
from os import path
from wordcloud import WordCloud
import numpy as np
from PIL import Image

d=path.dirname(__file__)

mask=np.array(Image.open(path.join(d,'stormtrooper_mask.png')))

text=open(path.join(d,'santi.txt')).read()
text.replace('叶文洁说','叶文洁')

font_path=path.join(d,'DroidSansFallbackFull.ttf')
wordcloud=WordCloud(font_path=font_path,mask=mask).generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis('off')
plt.show()