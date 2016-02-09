#!/usr/bin/python

from __future__ import print_function
from lxml import etree
from utils.misc import downloadWithProgressBar
from utils import mathfont
import json

# Retrieve the unicode.xml file if necessary.
unicodeXML = downloadWithProgressBar("http://www.w3.org/2003/entities/2007xml/unicode.xml")

# Extract the mathvariants transformation.
xsltTransform = etree.XSLT(etree.XML('''\
<xsl:stylesheet version="1.0"
                       xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:strip-space elements="*"/>
  <xsl:template match="charlist">
    <root><xsl:apply-templates select="character"/></root>
  </xsl:template>
  <xsl:template match="character">
    <xsl:if test="surrogate">
      <entry>
        <xsl:attribute name="mathvariant">
            <xsl:value-of select="surrogate/@mathvariant"/>
        </xsl:attribute>
        <xsl:attribute name="baseChar">
          <xsl:value-of select="surrogate/@ref"/>
        </xsl:attribute>
        <xsl:attribute name="transformedChar">
          <xsl:choose>
            <xsl:when test="bmp">
              <xsl:value-of select="bmp/@ref"/>
            </xsl:when>
            <xsl:otherwise>
               <xsl:value-of select="@id"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:attribute>
      </entry>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>'''))

# Put the mathvariant transforms into a Python structure.
mathvariantTransforms = {}
root = xsltTransform(etree.parse(unicodeXML)).getroot()
def parseCodePoint(aHexaString):
    return int("0x%s" % aHexaString[1:], 16)
for entry in root:
    mathvariant = entry.get("mathvariant")
    baseChar = parseCodePoint(entry.get("baseChar"))
    transformedChar = parseCodePoint(entry.get("transformedChar"))
    if mathvariant not in mathvariantTransforms:
        mathvariantTransforms[mathvariant] = {}
    mathvariantTransforms[mathvariant][baseChar] = transformedChar

# There is no "isolated" mathvariant.
del mathvariantTransforms["isolated"]

# Convert the Python structure into JSON
jsonFileName = "../relations/css-styling/mathvariant-transforms.json"
print("Generating %s..." % jsonFileName, end="")
jsonFile = open(jsonFileName, "w")
jsonFile.write(json.dumps(mathvariantTransforms,sort_keys=True, indent=4))
jsonFile.close()
print(" done.")

# Encode each transformed
font = mathfont.create("mathvariant-transforms")

transformedCharIndex = 1  # Index of the transformedChar.
numberOfBits = 11 # Number of bits to encode transformedCharIndex.
glyphWidth = 2 * mathfont.em # width of the mathvariant glyphs
rectangleWidth = glyphWidth / numberOfBits
assert rectangleWidth > 100

for mathvariant in mathvariantTransforms:
    for baseChar in mathvariantTransforms[mathvariant]:
        if baseChar not in font:
            g = font.createChar(baseChar)
            mathfont.drawRectangleGlyph(g, glyphWidth,
                                        mathfont.em/2, mathfont.em/2)
        transformedChar = mathvariantTransforms[mathvariant][baseChar]
        mathfont.createGlyphFromValue(font,
                                      transformedChar,
                                      glyphWidth,
                                      transformedCharIndex,
                                      numberOfBits)
        transformedCharIndex += 1
mathfont.save(font)
