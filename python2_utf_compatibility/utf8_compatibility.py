# -*- coding: utf-8 -*-
#!/usr/bin/python

######################################################
# UTF-8 COMPATIBILITY CODE ###########################
######################################################

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

######################################################
