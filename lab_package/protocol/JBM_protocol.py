from lab_package.protocol import base_protocol
from visprotocol import protocol as vpprotocol
import numpy as np
import math
import flyrpc.multicall
import random_word

class BaseProtocol(base_protocol.BaseProtocol):
    def __init__(self, cfg):
        super().__init__(cfg)  # call the parent class init method


# %% # # # SIMPLE SYNTHETIC STIMS # # # # # # # # #

class WhiteNoisePixMap(BaseProtocol, vpprotocol.SharedPixMapProtocol):
    """
    Drifting square wave grating, painted on a cylinder
    """
    def __init__(self, cfg):
        super().__init__(cfg)

        self.run_parameters = self.get_run_parameter_defaults()
        self.protocol_parameters = self.get_protocol_parameter_defaults()

    def get_epoch_parameters(self):
        super().get_epoch_parameters()

        self.epoch_protocol_parameters['memname'] = random_word.RandomWords().get_random_word()
        print(self.epoch_protocol_parameters['memname'])

        frame_shape = (self.epoch_protocol_parameters['n_x'], self.epoch_protocol_parameters['n_y'], 3)

        self.epoch_shared_pixmap_stim_parameters = {'name': 'WhiteNoise',
                                                    'memname': self.epoch_protocol_parameters['memname'],
                                                    'frame_shape': frame_shape,
                                                    'nominal_frame_rate': self.epoch_protocol_parameters['frame_rate'],
                                                    'dur': self.epoch_protocol_parameters['stim_time'],
                                                    'seed': self.epoch_protocol_parameters['seed'],
                                                    'coverage': 'full'}
        self.epoch_stim_parameters = {'name': 'PixMap',
                                      'memname': self.epoch_protocol_parameters['memname'],
                                      'frame_size': frame_shape,
                                      'rgb_texture': True,
                                      'width': 180,
                                      'radius': self.epoch_protocol_parameters['render_radius'],
                                      'n_steps': self.epoch_protocol_parameters['render_n_steps'],
                                      'surface': self.epoch_protocol_parameters['render_surface']}

    def get_protocol_parameter_defaults(self):
        return {'pre_time': 1.0,
                'stim_time': 4.0,
                'tail_time': 1.0,
                
                'n_x': 20.0,
                'n_y': 20.0,
                'frame_rate': 10.0,
                'seed': 37,
                'render_n_steps': 16,
                'render_surface': 'spherical', # cylindrical, cylindrical_with_phi
                'render_radius': 1,
                }

    def get_run_parameter_defaults(self):
        return {'num_epochs': 2,
                'idle_color': 0.5,
                'all_combinations': True,
                'randomize_order': True}


class DriftingSquareGrating(BaseProtocol):
    """
    Drifting square wave grating, painted on a cylinder
    """
    def __init__(self, cfg):
        super().__init__(cfg)

        self.run_parameters = self.get_run_parameter_defaults()
        self.protocol_parameters = self.get_protocol_parameter_defaults()

    def get_epoch_parameters(self):
        super().get_epoch_parameters()
        
        center = self.adjust_center(self.epoch_protocol_parameters['center'])
        centerX = center[0]
        centerY = center[1]

        self.epoch_stim_parameters = {'name': 'RotatingGrating',
                                      'period': self.epoch_protocol_parameters['period'],
                                      'rate': self.epoch_protocol_parameters['rate'],
                                      'color': [1, 1, 1, 1],
                                      'mean': self.epoch_protocol_parameters['mean'],
                                      'contrast': self.epoch_protocol_parameters['contrast'],
                                      'angle': self.epoch_protocol_parameters['angle'],
                                      'offset': 0.0,
                                      'cylinder_radius': 1,
                                      'cylinder_height': 10,
                                      'profile': 'square',
                                      'theta': centerX,
                                      'phi': centerY}

    def get_protocol_parameter_defaults(self):
        return {'pre_time': 1.0,
                'stim_time': 4.0,
                'tail_time': 1.0,
                
                'period': 20.0,
                'rate': 20.0,
                'contrast': 1.0,
                'mean': 0.5,
                'angle': [0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0],
                'center': (0, 0),
                }

    def get_run_parameter_defaults(self):
        return {'num_epochs': 40,
                'idle_color': 0.5,
                'all_combinations': True,
                'randomize_order': True}

# %%

class MovingPatch(BaseProtocol):
    """
    Moving patch, either rectangular or elliptical. Moves along a spherical or cylindrical trajectory
    """
    def __init__(self, cfg):
        super().__init__(cfg)

        self.run_parameters = self.get_run_parameter_defaults()
        self.protocol_parameters = self.get_protocol_parameter_defaults()

    def get_epoch_parameters(self):
        super().get_epoch_parameters()

        # Create flystim epoch parameters dictionary
        self.epoch_stim_parameters = self.get_moving_patch_parameters(center=self.epoch_protocol_parameters['center'],
                                                                angle=self.epoch_protocol_parameters['angle'],
                                                                speed=self.epoch_protocol_parameters['speed'],
                                                                width=self.epoch_protocol_parameters['width_height'][0],
                                                                height=self.epoch_protocol_parameters['width_height'][1],
                                                                color=self.epoch_protocol_parameters['intensity'])

    def get_protocol_parameter_defaults(self):
        return {'pre_time': 0.5,
                'stim_time': 3.0,
                'tail_time': 1.0,
                
                'ellipse': True,
                'width_height': [(5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30)],
                'intensity': 0.0,
                'center': (0, 0),
                'speed': 80.0,
                'angle': 0.0,
                'render_on_cylinder': False,
                }

    def get_run_parameter_defaults(self):
        return {'num_epochs': 40,
                'idle_color': 0.5,
                'all_combinations': True,
                'randomize_order': True}
