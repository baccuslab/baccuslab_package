1
from flystim.stim_server import launch_stim_server
from flystim.screen import Screen
from flystim.experiments import init_screens
from time import sleep

#!/usr/bin/env python3
import sys
import os
import random_word
import threading

import keyboard

from flystim.trajectory import Trajectory
from math import pi, radians
import matplotlib.pyplot as plt
from flystim.draw import draw_screens

from flystim.experiments import init_screens
from time import sleep as idle
import time

def redo(manager,ax1,ax2,color):
    
    manager.stop_stim()
    manager.black_corner_square()
    manager.load_stim(name='ConstantBackground', color=[0.5,0.5,0.5,0.5])
    manager.load_stim(name='MovingPatch', width=ax1, height=ax2, color = color, hold=True)
    # manager.load_stim(name='RotatingGrating', rate=10, period=20, mean=0.5, contrast=0.5, offset=0.0, profile='square',
                      # color=[1, 1, 1, 1], cylinder_radius=1.1, cylinder_height=10, theta=0, phi=0, angle=0, hold=True)
    manager.start_stim()
    return manager


def main():


    manager = init_screens()
    manager.black_corner_square()
    idle(2)
    

    running = True
    
    color = [1,1,1,1]
    theta = 0
    speed = 2
    phi = 0
    pos = 0
    width = 10.0 
    h_speed=0.02

    ax1 = 3
    ax2 = 3

    manager = redo(manager, ax1, ax2, color)
    while running:
        if keyboard.is_pressed('left'):
            theta -= speed
        elif keyboard.is_pressed('right'):
            theta += speed
        elif keyboard.is_pressed('w'):
            color = [1,1,1,1]
            manager = redo(manager, ax1, ax2, color)
        elif keyboard.is_pressed('b'):
            color = [0,0,0,1]
            manager = redo(manager, ax1, ax2, color)
        elif keyboard.is_pressed('r'):
            theta = 0
            speed = 2
            phi = 0
            pos = 0
            width = 10.0
            ax1 = 3
            ax2 = 3

        elif keyboard.is_pressed('1'):
            speed = 0.125
        elif keyboard.is_pressed('2'):
            speed = 0.25
        elif keyboard.is_pressed('3'):
            speed = 0.5
        elif keyboard.is_pressed('4'):
            speed = 1.0
        elif keyboard.is_pressed('5'):
            speed = 2.0
        elif keyboard.is_pressed('6'):
            speed = 4.0
        elif keyboard.is_pressed('7'):
            speed = 8.0
        elif keyboard.is_pressed('q'):
            break
        elif keyboard.is_pressed('up'):
            pos -= h_speed*speed
        elif keyboard.is_pressed('down'):
            pos += h_speed*speed
        elif keyboard.is_pressed('h'):
            ax1 += 0.2
            manager = redo(manager,ax1,ax2, color)
        elif keyboard.is_pressed('l'):
            ax1 -= 0.2
            manager = redo(manager,ax1,ax2, color)
        elif keyboard.is_pressed('j'):
            ax2 += 0.2
            manager = redo(manager,ax1,ax2, color)
        elif keyboard.is_pressed('k'):
            ax2 -= 0.2
            manager = redo(manager,ax1,ax2, color)
        
        manager.set_global_theta_offset(theta)
        manager.set_global_fly_pos(0,0,pos)
        idle(0.01)




    try:
        process.terminate()
    except:
        pass

    idle(INTERVAL)

    del root_stim,process
if __name__ == '__main__':
    main()
