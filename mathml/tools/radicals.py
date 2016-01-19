#!/usr/bin/python

import mathfont
import fontforge

RadicalCodePoint = 0x221a

v1 = 25
v2 = 1 * mathfont.em
f = mathfont.create("radical-degreebottomraisepercent%d-rulethickness%d" % (v1, v2))
mathfont.createSquareGlyph(f, RadicalCodePoint)
f.math.RadicalDegreeBottomRaisePercent = v1
f.math.RadicalDisplayStyleVerticalGap = 0
f.math.RadicalExtraAscender = 0
f.math.RadicalKernAfterDegree = 0
f.math.RadicalKernBeforeDegree = 0
f.math.RadicalRuleThickness = v2
f.math.RadicalVerticalGap = 0
mathfont.save(f)

v1 = 7 * mathfont.em
v2 = 1 * mathfont.em
f = mathfont.create("radical-displaystyleverticalgap%d-rulethickness%d" % (v1, v2))
mathfont.createSquareGlyph(f, RadicalCodePoint)
f.math.RadicalDegreeBottomRaisePercent = 0
f.math.RadicalDisplayStyleVerticalGap = v1
f.math.RadicalExtraAscender = 0
f.math.RadicalKernAfterDegree = 0
f.math.RadicalKernBeforeDegree = 0
f.math.RadicalRuleThickness = v2
f.math.RadicalVerticalGap = 0
mathfont.save(f)

v1 = 3 * mathfont.em
v2 = 1 * mathfont.em
f = mathfont.create("radical-extraascender%d-rulethickness%d" % (v1, v2))
mathfont.createSquareGlyph(f, RadicalCodePoint)
f.math.RadicalDegreeBottomRaisePercent = 0
f.math.RadicalDisplayStyleVerticalGap = 0
f.math.RadicalExtraAscender = v1
f.math.RadicalKernAfterDegree = 0
f.math.RadicalKernBeforeDegree = 0
f.math.RadicalRuleThickness = v2
f.math.RadicalVerticalGap = 0
mathfont.save(f)

v1 = 5 * mathfont.em
v2 = 1 * mathfont.em
f = mathfont.create("radical-kernafterdegreeminus%d-rulethickness%d" % (v1, v2))
mathfont.createSquareGlyph(f, RadicalCodePoint)
g = f.createChar(-1, "size1")
mathfont.drawRectangleGlyph(g, mathfont.em, 2 * mathfont.em, 0)
g = f.createChar(-1, "size2")
mathfont.drawRectangleGlyph(g, mathfont.em, 3 * mathfont.em, 0)
g = f.createChar(-1, "size3")
mathfont.drawRectangleGlyph(g, mathfont.em, 4 * mathfont.em, 0)
f[RadicalCodePoint].verticalVariants = "radical size1 size2 size3"
f.math.RadicalDegreeBottomRaisePercent = 0
f.math.RadicalDisplayStyleVerticalGap = 0
f.math.RadicalExtraAscender = 0
f.math.RadicalKernAfterDegree = -v1
f.math.RadicalKernBeforeDegree = 0
f.math.RadicalRuleThickness = v2
f.math.RadicalVerticalGap = 0
mathfont.save(f)

v1 = 4 * mathfont.em
v2 = 1 * mathfont.em
f = mathfont.create("radical-kernbeforedegree%d-rulethickness%d" % (v1, v2))
mathfont.createSquareGlyph(f, RadicalCodePoint)
f.math.RadicalDegreeBottomRaisePercent = 0
f.math.RadicalDisplayStyleVerticalGap = 0
f.math.RadicalExtraAscender = 0
f.math.RadicalKernAfterDegree = 0
f.math.RadicalKernBeforeDegree = v1
f.math.RadicalRuleThickness = v2
f.math.RadicalVerticalGap = 0
mathfont.save(f)

v = 8 * mathfont.em
f = mathfont.create("radical-rulethickness%d" % v)
mathfont.createSquareGlyph(f, RadicalCodePoint)
f.math.RadicalDegreeBottomRaisePercent = 0
f.math.RadicalDisplayStyleVerticalGap = 0
f.math.RadicalExtraAscender = 0
f.math.RadicalKernAfterDegree = 0
f.math.RadicalKernBeforeDegree = 0
f.math.RadicalRuleThickness = v
f.math.RadicalVerticalGap = 0
mathfont.save(f)

v1 = 6 * mathfont.em
v2 = 1 * mathfont.em
f = mathfont.create("radical-verticalgap%d-rulethickness%d" % (v1, v2))
mathfont.createSquareGlyph(f, RadicalCodePoint)
f.math.RadicalDegreeBottomRaisePercent = 0
f.math.RadicalDisplayStyleVerticalGap = 0
f.math.RadicalExtraAscender = 0
f.math.RadicalKernAfterDegree = 0
f.math.RadicalKernBeforeDegree = 0
f.math.RadicalRuleThickness = v2
f.math.RadicalVerticalGap = v1
mathfont.save(f)
