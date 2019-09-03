#!/usr/bin/env python

import json
import time
from pprint import pprint
from samplebase import SampleBase


class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

        self.fps = 2
        self.brightness = 50

    def showFrame(self, frame):

        for r in range(32):
            for c in range(32):
                if frame:
                    color = frame.pop(0)

                    rColor = (color      ) & 0xff
                    gColor = (color >> 8 ) & 0xff
                    bColor = (color >> 16) & 0xff

                    self.matrix.SetPixel(c,r,rColor, gColor, bColor);

        time.sleep((1.0 / self.fps))

    def run(self):

        self.matrix.brightness = self.brightness

        with open('art.json') as data_file:
            data = json.load(data_file)

        while True:
            frame = data.pop(0)
            newFrame = list(frame)
            self.showFrame(frame)
            data.append(newFrame)


# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()
