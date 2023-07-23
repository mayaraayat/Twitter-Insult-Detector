import numpy as np

from PIL import Image
from wordcloud import *
import matplotlib.pyplot as plt
from collections import Counter


def frequencies(vocab_list):
    d = {}
    for i in range(len(vocab_list)):
        freq = Counter(vocab_list[i]).most_common()
        for (a, b) in freq:
            d[a] = b
    return d

def makeImage(vocab_list, path):
    alice_mask = np.array(Image.open(path))

    wc = WordCloud(background_color="white", max_words=1000,
                   mask=alice_mask, contour_color='black', contour_width=3)
    # generate word cloud
    wc.generate_from_frequencies(frequencies(vocab_list))

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

