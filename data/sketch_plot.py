import os
import requests
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm


# download a the humor font
fname = "Humor-Sans.ttf"
if not os.path.exists(fname): 
    url_font = 'http://antiyawn.com/uploads/Humor-Sans-1.0.ttf'
    r = requests.get(url_font)
    with open(fname,'wb') as f:   
        f.write(r.content)


dataXHL = np.arange(0.1, 10, 0.1)
dataYHL = np.exp(-(0.7*dataXHL)) + 0.3
dataXLL = np.arange(3, 10, 0.1)
dataYLL = np.exp(-(1*(dataXLL - 2))) + 0.15
dataXLLL = np.arange(5, 10, 0.1)
dataYLLL = np.exp(-(0.8*(dataXLLL - 3))) + 0.1

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    
    fig, ax = plt.subplots(figsize=(10,5))
    # set spines invisible 
    ax.spines[:].set_visible(False)
    # eliminate ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Change all the fonts to humor-sans.
    prop = fm.FontProperties(fname="Humor-Sans.ttf", size=16)
    
    ax.set_xlim([-0.5, 10])
    ax.set_ylim([-.05, 1])
   
    ax.plot(dataXHL, dataYHL, color="r", label="HIGH-LEVEL LENGUAGE")
    ax.plot(dataXLL, dataYLL, color="b", label="LOW-LEVEL LENGUAGE")
    ax.plot(dataXLLL, dataYLLL, color="g", label="LOWLOW-LEVEL LENGUAGE")
    
    ax.annotate('',
        xy=(0, 1), arrowprops=dict(arrowstyle='->'), xytext=(0, -0.1))
    ax.annotate('',
        xy=(10, 0), arrowprops=dict(arrowstyle='->'), xytext=(-0.5, 0))

    ax.set_xlabel('DEVELOPMENT\nTIME', position=(1,0), rotation=2,  fontproperties=prop)
    ax.set_ylabel('CPU\nTIME', position=(0, 0.8), rotation=12, fontproperties=prop)
    plt.legend(prop=prop, loc='upper right')

    
plt.savefig("sketchy_graph.png")