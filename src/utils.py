import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, Animation, PillowWriter

import PIL
import io

import sys
import logging

from typing import Sequence


def get_logger(name: str) -> logging.Logger:
    '''
    Configures and returns a logger

    Parameters
    ----------
    name : str
        Name of the logger. Usually the same as the name of module

    Returns
    -------
    logging.Logger
        Logger
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    stream_handler.setFormatter(formatter)
    
    logger.addHandler(stream_handler)

    return logger


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
