# Tests for the MathML in HTML5 implementation note

This repository contains tests for the
[MathML in HTML5 implementation note](http://www.mathml-association.org/MathMLinHTML5/).
We follow the formats and conventions of
[W3C's Test the Web Forward Project](http://testthewebforward.org/),
please read their documentation for details. The main goals are:
- helping implementers to verify conformance with the technical description
  given in the MathML in HTML5 note.
- provide a set of automatable tests to integrate into the testing framework of
  web browser developers.

## Installation

Clone the repository with

    $ git clone --recursive https://github.com/username/MathMLinHTML5-tests.git

If you cloned the repository without --recursive, you will likely have an empty
`resources` directory at the root of your cloned repo. You can clone the
submodules with these additional steps:

    $ cd test-repo-root
    $ git submodule update --init --recursive

To verify the tests in your browser, you also need a local server whose root
points to the root of the cloned repo.

Many of the tests verify OpenType features and require specific Web fonts for
that purpose. WOFF fonts are generated using the Python API of
[fontforge](https://github.com/fontforge/fontforge/). A recent enough version
of FontForge is necessary so that it includes fixes for [WOFF checkSumAdjustment](https://github.com/fontforge/fontforge/issues/926), [USE_TYPO_METRICS flag](https://github.com/fontforge/fontforge/pull/2274) and various OpenType MATH
features.
