# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import time
import os
import inspect

from tank_test.tank_test_base import TankTestBase
from tank_test.tank_test_base import setUpModule  # noqa

import sgtk


class TestFramework(TankTestBase):
    """
    Very basic tests for the framework.
    """

    def setUp(self):
        """
        Prepare a configuration with a config that uses the framework.
        """
        super(TestFramework, self).setUp()
        self.setup_fixtures()
        context = sgtk.Context(self.tk, project=self.project)
        self.engine = sgtk.platform.start_engine("tk-testengine", self.tk, context)

    def tearDown(self):
        """
        Terminate the engine and the rest of the test suite.
        """
        self.engine.destroy()
        super(TestFramework, self).tearDown()

    def test_import_framework(self):
        """
        Ensure we can import the framework.
        """
        fw = self.engine.apps["tk-testapp"].frameworks["tk-framework-widget"]
        # we need to import a module in order to trigger
        # an import of all the framework modules.
        fw.import_module("browser_widget")
