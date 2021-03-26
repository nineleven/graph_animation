import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, Animation, PillowWriter

import PIL
import io

from typing import Sequence


def figure_to_pil(fig: plt.Figure) -> PIL.Image.Image:
    '''
    Converts matplotlib figure into an array of pixels
    
    Parameters
    ----------
    fig : plt.Figure
        matplotlib figure
    
    Returns
    -------
    PIL.Image.Image
        An array of pixels
    '''
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return PIL.Image.open(buf)


def make_animation(frames: Sequence[PIL.Image.Image]) -> FuncAnimation:
    '''
    Makes an animation from a list of frames
    
    Parameters
    ----------
    frames : Sequence[PIL.Image.Image]
        Sequence of frames
    
    Returns
    -------
    matplotlib.animation.FuncAnimation
        Animation
    '''
    fig = plt.figure()
    ax = plt.axes()
    ax.axis('off')

    image = plt.imshow(frames[0])

    def animate(i: int) -> list:
        image.set_array(frames[i])
        return [image]

    anim = FuncAnimation(fig, animate, frames=len(frames))
    
    return anim


def save_animation(anim: Animation, filename: str, fps: int = 5) -> None:
    '''
    Saves an animation to a file

    Parameters
    ----------
    anim : matplotlib.animation.Animation
        Animation
    filename : str
        The output filename
    fps : int
        Frame per second
    '''
    anim.save(filename, writer=PillowWriter(fps=fps))
