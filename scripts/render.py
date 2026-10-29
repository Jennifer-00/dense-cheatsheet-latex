#!/usr/bin/env python3
"""Render PDF pages to PNG for visual checking: python render.py cheat.pdf [dpi]"""
import sys, fitz
d = fitz.open(sys.argv[1]); dpi = int(sys.argv[2]) if len(sys.argv) > 2 else 200
for i, p in enumerate(d):
    p.get_pixmap(dpi=dpi).save('page%d.png' % (i + 1)); print('page%d.png' % (i + 1))
