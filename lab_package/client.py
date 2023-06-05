#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flystim.stim_server import launch_stim_server
from flyrpc.transceiver import MySocketClient
from flystim.screen import Screen
from flystim.draw import draw_screens

from visprotocol import client


class Client(client.BaseClient):
    def __init__(self, cfg):
        super().__init__(cfg)  # call the parent class init method

     