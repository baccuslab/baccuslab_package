#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: mhturner
"""

from lab_protocol import base_protocol


class BaseProtocol(base_protocol.BaseProtocol):
    def __init__(self, cfg):
        super().__init__(cfg)  # call the parent class init method

# %%

class DriftingSquareGrating(BaseProtocol):
    def __init__(self, cfg):
        super().__init__(cfg)

        self.get_run_parameter_defaults()
        self.get_parameter_defaults()

    def get_epoch_parameters(self):
        current_angle = self.select_parameters_from_lists(self.protocol_parameters['angle'], randomize_order = self.protocol_parameters['randomize_order'])

        self.epoch_parameters = {'name': 'RotatingGrating',
                                 'period': self.protocol_parameters['period'],
                                 'rate': self.protocol_parameters['rate'],
                                 'color': [1, 1, 1, 1],
                                 'mean': self.protocol_parameters['mean'],
                                 'contrast': self.protocol_parameters['contrast'],
                                 'angle': current_angle,
                                 'offset': 0.0,
                                 'cylinder_radius': 1,
                                 'cylinder_height': 10,
                                 'profile': 'square',
                                 'theta': self.screen_center[0]}

        self.convenience_parameters = {'current_angle': current_angle}

    def get_parameter_defaults(self):
        self.protocol_parameters = {'period': 20.0,
                                    'rate': 20.0,
                                    'contrast': 1.0,
                                    'mean': 0.5,
                                    'angle': [0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0],
                                    'center': [0, 0],
                                    'center_size': 180.0,
                                    'randomize_order': True}

    def get_run_parameter_defaults(self):
        self.run_parameters = {'protocol_ID': 'DriftingSquareGrating',
                               'num_epochs': 40,
                               'pre_time': 1.0,
                               'stim_time': 4.0,
                               'tail_time': 1.0,
                               'idle_color': 0.5}

# %%

class MovingSpot(BaseProtocol):
    def __init__(self, cfg):
        super().__init__(cfg)

        self.get_run_parameter_defaults()
        self.get_parameter_defaults()

    def get_epoch_parameters(self):
        current_diameter, current_intensity, current_speed = self.select_parameters_from_lists((self.protocol_parameters['diameter'], self.protocol_parameters['intensity'], self.protocol_parameters['speed']), randomize_order=self.protocol_parameters['randomize_order'])

        self.epoch_parameters = self.get_moving_spot_parameters(radius=current_diameter/2,
                                                             color=current_intensity,
                                                             speed=current_speed)

        self.convenience_parameters = {'current_diameter': current_diameter,
                                       'current_intensity': current_intensity,
                                       'current_speed': current_speed}

    def get_parameter_defaults(self):
        self.protocol_parameters = {'diameter': [5, 10, 15, 20, 25, 30],
                                    'intensity': [0.0, 1.0],
                                    'center': [0, 0],
                                    'speed': [80.0],
                                    'angle': 0.0,
                                    'randomize_order': True}

    def get_run_parameter_defaults(self):
        self.run_parameters = {'protocol_ID': 'MovingSpot',
                               'num_epochs': 70,
                               'pre_time': 0.5,
                               'stim_time': 3.0,
                               'tail_time': 1.0,
                               'idle_color': 0.5}

# %%