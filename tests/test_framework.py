# Copyright (c) 2013 Shotgun Software Inc.
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
        # We can't load modules from a test because load_framework can only be called
        # from within a Toolkit bundle or hook, so we'll do it from a hook.
        fw = self.engine.apps["tk-testapp"].frameworks["tk-framework-widget"]
        # we need to import a module in order to trigger
        # an import of all the framework modules.
        fw.import_module("browser_widget")

    def test_widgets(self):
        """
        Ensure we can instantiate the widgets.

        In lieu of a proper test suite that fully tests the widgets, we'll
        use the about box that uses them, which will give us some code coverage
        for really cheap.
        """
        fw = self.engine.commands["Work Area Info..."]["callback"]()
        self.engine.app.processEvents()
