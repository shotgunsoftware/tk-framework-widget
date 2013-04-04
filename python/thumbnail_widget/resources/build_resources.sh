#!/usr/bin/env bash
# 
# Copyright (c) 2013 Shotgun Software, Inc
# ----------------------------------------------------

echo "building user interfaces..."
pyside-uic --from-imports thumbnail_widget.ui > ../ui/thumbnail_widget.py

echo "building resources..."
pyside-rcc resources.qrc > ../ui/resources_rc.py
