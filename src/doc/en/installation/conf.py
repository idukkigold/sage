# -*- coding: utf-8 -*-
#
# Sage Installation Guide documentation build configuration file, created by
# sphinx-quickstart on Fri Aug 22 15:04:04 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
from sage.env import SAGE_DOC_SRC
sys.path.append(SAGE_DOC_SRC)
from common.conf import *

# General information about the project.
project = u"Sage Installation Guide"
name = 'installation'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + " v"+release
html_short_title = u"Install Guide v" + release

# Output file base name for HTML help builder.
htmlhelp_basename = name

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', name+'.tex', u'Sage Installation Guide',
   u'The Sage Development Team', 'manual'),
]

