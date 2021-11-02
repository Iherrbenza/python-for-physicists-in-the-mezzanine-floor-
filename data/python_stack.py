import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle

dim = [10, 12]
margin = 1

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    fig, ax = plt.subplots(figsize=(10,10))
    # set spines invisible 
    ax.spines[:].set_visible(False)
    # eliminate ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.set_xlim([-dim[0]/2, dim[0]/2])
    ax.set_ylim([-dim[1]/2, dim[1]/2])
    
    dimx = dim[0] - 2*margin
    dimy = 2.5
    psx = 0
    psy = dim[1]/2 - margin - 3*dimy - 1.5
    rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
    ax.add_patch(rect)     
    ax.text(psx, psy, "Python 3.7 \ncore", ha="center", va="center", rotation=0, size=40)
    
    dimx = (dim[0] - 2*margin) / 3 - 0.1
    dimy = 2.5
    psx =  dimx + 2* 0.1
    psy = dim[1]/2 - margin - 2*dimy - 1.2
    rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
    ax.add_patch(rect)     
    ax.text(psx, psy, "Numpy\n1.20.3", ha="center", va="center", rotation=0, size=30)
    
    dimx = (dim[0] - 2 * margin) / 3 - 0.1
    dimy = 2 * 2.5 + 0.1
    psx =  - dimx  - 0.1
    psy = dim[1]/2 - margin - dimy - 1.1 + 1.28
    rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
    ax.add_patch(rect)     
    ax.text(psx, psy, "Sympy\n1.8", ha="center", va="center", rotation=0, size=30)
    
    dimx = (dim[0] - 2*margin) / 3 - 0.1
    dimy = 2 * 2.5 + 0.1
    psx =  0 
    psy = dim[1]/2 - margin - dimy - 1.1 + 1.28
    rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
    ax.add_patch(rect)     
    ax.text(psx, psy, "Matplotlib\n 3.4.2", ha="center", va="center", rotation=0, size=30)
    
    dimx = (dim[0] - 2*margin) / 3 - 0.1
    dimy = 2.5
    psx =  dimx + 2* 0.1
    psy = dim[1]/2 - margin - dimy - 1.1
    rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
    ax.add_patch(rect)     
    ax.text(psx, psy, "Scipy\n1.6.2", ha="center", va="center", rotation=0, size=30)
    
    dimx = dim[0] - 2*margin
    dimy = 2.5
    psx = 0
    psy = dim[1]/2 - margin - 1
    rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
    ax.add_patch(rect)     
    ax.text(psx, psy, "Your code\nv1.9", ha="center", va="center", rotation=0, size=40)
    
#     dimx = dim[0] - 2*margin
#     dimy = 2.5
#     psx = 0
#     psy = dim[1]/2 - margin - 1
#     rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
#     ax.add_patch(rect)     
#     ax.text(psx, psy, "Python 3.7 \ncore", ha="center", va="center", rotation=0, size=40)
    
#     dimx = (dim[0] - 2*margin) / 3 - 0.1
#     dimy = 2.5
#     psx =  dimx + 2* 0.1
#     psy = dim[1]/2 - margin - dimy - 1.1
#     rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
#     ax.add_patch(rect)     
#     ax.text(psx, psy, "Numpy\n1.20.3", ha="center", va="center", rotation=0, size=30)
    
#     dimx = (dim[0] - 2 * margin) / 3 - 0.1
#     dimy = 2 * 2.5 + 0.1
#     psx =  - dimx  - 0.1
#     psy = dim[1]/2 - margin - dimy - 1.1 + 1.28
#     rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
#     ax.add_patch(rect)     
#     ax.text(psx, psy, "Sympy\n1.8", ha="center", va="center", rotation=0, size=30)
    
#     dimx = (dim[0] - 2*margin) / 3 - 0.1
#     dimy = 2 * 2.5 + 0.1
#     psx =  0 
#     psy = dim[1]/2 - margin - dimy - 1.1 + 1.28
#     rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
#     ax.add_patch(rect)     
#     ax.text(psx, psy, "Matplotlib\n 3.4.2", ha="center", va="center", rotation=0, size=30)
    
#     dimx = (dim[0] - 2*margin) / 3 - 0.1
#     dimy = 2.5
#     psx =  dimx + 2* 0.1
#     psy = dim[1]/2 - margin - 2*dimy - 1.2
#     rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
#     ax.add_patch(rect)     
#     ax.text(psx, psy, "Scipy\n1.6.2", ha="center", va="center", rotation=0, size=30)
    
#     dimx = dim[0] - 2*margin
#     dimy = 2.5
#     psx = 0
#     psy = dim[1]/2 - margin - 3*dimy - 1.5
#     rect = Rectangle((psx - dimx / 2, psy - dimy / 2) , dimx , dimy, ec="grey", fc="#9ABCFF")
#     ax.add_patch(rect)     
#     ax.text(psx, psy, "Your code\nv1.9", ha="center", va="center", rotation=0, size=40)
    
#     ax.annotate('',
#     xy=((dim[0] - 2*margin) / 3 - 0.1 + 2* 0.1, dim[1]/2 - margin - 2.5 - 1.1), arrowprops=dict(
#     arrowstyle='simple', color='g',shrinkA=60,shrinkB=60, connectionstyle="angle3"), 
#     xytext=((0, dim[1]/2 - margin - 1)), size=30)
    
#     ax.annotate('',
#     xy=(-((dim[0] - 2 * margin) / 3 - 0.1)  - 0.1, dim[1]/2 - margin - 2.5 - 1.1), arrowprops=dict(
#     arrowstyle='simple', color='g',shrinkA=60,shrinkB=60, connectionstyle="angle3"), 
#     xytext=((0, dim[1]/2 - margin - 1)), size=30)
    
    
    plt.tight_layout()
plt.savefig("python_stack.png")