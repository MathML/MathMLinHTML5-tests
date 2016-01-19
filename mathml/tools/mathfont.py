#!/usr/bin/python

from __future__ import print_function
import fontforge

em = 1000

def create(aName):
    print("Generating %s.woff..." % aName, end="")
    mathFont = fontforge.font()
    mathFont.fontname = aName
    mathFont.familyname = aName
    mathFont.fullname = aName
    mathFont.copyright = "Copyright (c) 2016 MathML Association"
    mathFont.encoding = "UnicodeFull"

    # Create a space character. Also force the creation of some MATH subtables
    # so that OTS will not reject the MATH table.
    g = mathFont.createChar(ord(" "), "space")
    g.width = em
    g.italicCorrection = 0
    g.topaccent = 0
    g.mathKern.bottomLeft = tuple([(0,0)])
    g.mathKern.bottomRight = tuple([(0,0)])
    g.mathKern.topLeft = tuple([(0,0)])
    g.mathKern.topRight = tuple([(0,0)])
    mathFont[ord(" ")].horizontalVariants = "space"
    mathFont[ord(" ")].verticalVariants = "space"
    return mathFont

def drawRectangleGlyph(aGlyph, aWidth, aAscent, aDescent):
    aGlyph.width = aWidth
    p = aGlyph.glyphPen()
    p.moveTo(0, -aDescent)
    p.lineTo(aWidth, -aDescent)
    p.lineTo(aWidth, aAscent)
    p.lineTo(0, aAscent)
    p.closePath();

def createSquareGlyph(aFont, aCodePoint):
    g = aFont.createChar(aCodePoint)
    drawRectangleGlyph(g, em, em, 0)
    
def save(aFont):
    aFont.em = em
    aFont.ascent = aFont.descent = em/2
    aFont.hhea_ascent = aFont.hhea_descent = em/2
    aFont.os2_typoascent = aFont.os2_typodescent = em/2
    # aFont.os2_winascent, aFont.os2_windescent should be the maximum of
    # ascent/descent for all glyphs. Does fontforge compute them automatically?
    aFont.hhea_ascent_add = aFont.hhea_descent_add = 0
    aFont.os2_typoascent_add = aFont.os2_typodescent_add = 0
    aFont.os2_winascent_add = aFont.os2_windescent_add = 0
    aFont.os2_use_typo_metrics = True
    aFont.generate("../../fonts/math/%s.woff" % aFont.fontname)
    print(" done.")
