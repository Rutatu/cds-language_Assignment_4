#!/usr/bin/env bash

VENVNAME=networks
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME