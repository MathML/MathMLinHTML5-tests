#!/usr/bin/python

from utils import mathfont
import fontforge

verticalArrowCodePoint = 0x21A8
v1 = 5 * mathfont.em
v2 = 14 * mathfont.em
f = mathfont.create("axisheight%d-verticalarrow%d" % (v1, v2))
f.math.AxisHeight = v1
mathfont.createSquareGlyph(f, verticalArrowCodePoint)
g = f.createChar(-1, "size1")
mathfont.drawRectangleGlyph(g, mathfont.em, v2 / 2, 0)
g = f.createChar(-1, "size2")
mathfont.drawRectangleGlyph(g, mathfont.em, v2, 0)
f[verticalArrowCodePoint].verticalVariants = "uni21A8 size1 size2"
mathfont.save(f)
