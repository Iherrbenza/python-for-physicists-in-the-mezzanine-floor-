import os
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


dim = [10, 10]
margin = 2

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    fig, ax = plt.subplots(figsize=(10,10))
    # set spines invisible 
    ax.spines[:].set_visible(False)
    # eliminate ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Change all the fonts to humor-sans.
    prop = fm.FontProperties(fname="Humor-Sans.ttf", size=16)
    
    ax.set_xlim([-dim[0]/2, dim[0]/2])
    ax.set_ylim([-dim[1]/2, dim[1]/2])
        
    n_l1 = 3
    for i in range(n_l1):
            
            step = (dim[1] - 2 * margin ) / n_l1 
            y_pos = (dim[1] / 2 - margin - step/2) - step * i
            ax.text(
                0, y_pos, f"n{i}", ha="center", va="center", rotation=0, size=20, fontproperties=prop,
            bbox=dict(boxstyle="circle,pad=0.5", fc="cyan", ec="b", lw=2))
            
            ax.annotate('s',
                xy=(0, y_pos), arrowprops=dict(
                arrowstyle='simple', color='g',shrinkA=10,shrinkB=25, connectionstyle="angle3"), 
                xytext=(-dim[0]/2 + margin, 0), size=30)
            
    # input
    ax.text(
        -dim[0]/2 + margin, 0, "Input\nY", ha="center", va="center", rotation=0, size=20, fontproperties=prop,
        bbox=dict(boxstyle="round4, pad=0.5", fc="cyan", ec="b", lw=2))
    
plt.savefig("netw0_graph.png")