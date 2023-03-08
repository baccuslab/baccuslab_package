#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flystim.stim_server import launch_stim_server
from flyrpc.transceiver import MySocketClient
from flystim.screen import Screen
from flystim.draw import draw_screens

from visprotocol import client

from lab_package.device import daq


class Client(client.BaseClient):
    def __init__(self, cfg):
        super().__init__(cfg)  # call the parent class init method [visprotocol.client.BaseClient]

        # # # Init the trigger device based on cfg # # #
        self.trigger_device_definition = cfg['rig_config'][cfg.get('rig_name')]['devices'].get('trigger', None)

        if self.trigger_device_definition is None:
            self.trigger_device = None
        else: 
            self.trigger_device = exec(self.trigger_device_definition)


        # # # Start the stim manager and set the frame tracker square to black # # #
        if self.server_options['use_server']:
            self.manager = MySocketClient(host=self.server_options['host'], port=self.server_options['port'])
            if isinstance(self.trigger_device, daq.DAQonServer):
                self.trigger_device.set_manager(self.manager)
        else:
            aux_screen = Screen(server_number=1, id=0, fullscreen=False, vsync=True, square_size=(0.25, 0.25))
            if cfg.get('draw_screens'):
              draw_screens(aux_screen)
            self.manager = launch_stim_server(aux_screen)

        self.manager.black_corner_square()
        self.manager.set_idle_background(0)
     