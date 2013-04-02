#!/usr/bin/env bash
# 
# Copyright (c) 2013 Shotgun Software, Inc
# ----------------------------------------------------

echo "building user interfaces..."
pyside-uic --from-imports thumbnail_ui.ui > ../ui/thumbnail_ui.py

echo "building resources..."
pyside-rcc resources.qrc > ../ui/resources_rc.py
