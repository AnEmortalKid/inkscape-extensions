#!/usr/bin/env python
# coding=utf-8
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
Exports a document into multiple PNGs of various square dimensions

The exported PNGs will be appended with an @Size name, e.g. icon@16.png
"""

import os
import inkex
from inkex.command import inkscape

class BatchPNGExport(inkex.Effect):

    def add_arguments(self, pars):
        pars.add_argument("--base_name", type=str, default="icon", help="Base name for exported files")
        pars.add_argument("--sizes", type=str, default="16,32,64", help="Comma-separated sizes")
        pars.add_argument("--output_dir", type=str, default="exports", help="Output folder")

    def effect(self):
        # get our inputs
        base_name = self.options.base_name.strip()
        sizes = [int(s.strip()) for s in self.options.sizes.split(",") if s.strip().isdigit()]
        output_dir = self.options.output_dir.strip()

        # Get the dimensions of the document to export the whole area
        width = self.svg.viewport_width
        height = self.svg.viewport_height
        export_area = f"0:0:{width}:{height}"

        # make the output dir if its given as a string
        os.makedirs(output_dir, exist_ok=True)

        # For each selected size create a png
        # The name would be something like icon@24.png
        # There should be a popup dialog with our messages of each file we exported
        for size in sizes:
            filename = os.path.join(output_dir, f"{base_name}@{size}.png")
            self.msg(f"Exporting {filename} ...")
            inkscape(self.options.input_file, export_area=export_area, export_filename=filename, export_width=size, export_height=size)
            self.msg(f"✅ Exported to {filename}")

if __name__ == "__main__":
    BatchPNGExport().run()
