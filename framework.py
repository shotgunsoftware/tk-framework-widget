"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------

Basic Tank Widget Framework

"""

import tank
import platform
import sys
import traceback
import os



class WidgetFramework(tank.platform.Framework):
    
    ##########################################################################################
    # init and destroy
            
    def init_framework(self):
        self.log_debug("%s: Initializing..." % self)
    
    def destroy_framework(self):
        self.log_debug("%s: Destroying..." % self)
    
    
