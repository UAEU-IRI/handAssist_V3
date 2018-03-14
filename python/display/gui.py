#!/usr/bin/env python

import os
import time
import threading
from luma.core.virtual import terminal
import sys
import logging
from luma.core import cmdline, error




def get_device(actual_args=None):
    """
    Create device from command-line arguments and return it.
    """

    actual_args = ['--interface', 'spi', '--d', 'ssd1306']
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)
    if args.config:
        # load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
    except error.Error as e:
        parser.error(e)

    return device






class Gui (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.device = get_device()
	def run(self):
		while True:
				term = terminal(self.device)
				term.println("HandAssist V3.1")
				term.println("UAEU, IRI Lab")
				time.sleep(2)
				term.puts("Connecting ...")
				while True:
					term.puts("|")
					time.sleep(0.5)
					term.backspace()
					term.puts("/")
					time.sleep(0.5)
					term.backspace()
					term.puts("-")
					time.sleep(0.5)
					term.backspace()
					term.puts("\\")
					time.sleep(0.5)
					term.backspace()