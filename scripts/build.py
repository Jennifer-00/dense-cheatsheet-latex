#!/usr/bin/env python3
"""Fit a multicol cheat sheet to a page budget by trying font sizes.

usage: python build.py cheat.tex [--pages 2] [--sizes 4.4,4.2,4.0,3.9,3.8,3.7]
                                 [--ratio 1.13] [--cols 4]
The tex file must read \\FS and \\LH (see assets/template.tex).
"""
import argparse, os, re, shutil, subprocess, sys

def compile_tex(tex, fs, lh, job):
    cmd = ['xelatex', '-interaction=nonstopmode', '-jobname=' + job,
           '\\def\\FS{%s}\\def\\LH{%s}\\input{%s}' % (fs, lh, tex)]
    r = subprocess.run(cmd, capture_output=True, text=True, errors='replace')
    pdf = job + '.pdf'
    if not os.path.exists(pdf):
        print(r.stdout[-1500:]); sys.exit('xelatex failed (is the PDF open in a viewer?)')
    errs = [l for l in r.stdout.splitlines() if l.startswith('!')]
    return pdf, errs

def fill(pdf, cols):
    import fitz
    d = fitz.open(pdf); out = []
    for p in d:
        W, H = p.rect.width, p.rect.height; c = [0.0] * cols
        for b in p.get_text('blocks'):
            i = min(cols - 1, int(b[0] / (W / cols))); c[i] = max(c[i], b[3])
        out.append([round(x / H, 2) for x in c])
    return len(d), out

def main():
    a = argparse.ArgumentParser()
    a.add_argument('tex'); a.add_argument('--pages', type=int, default=2)
    a.add_argument('--sizes', default='4.4,4.2,4.0,3.9,3.8,3.7')
    a.add_argument('--ratio', type=float, default=1.13); a.add_argument('--cols', type=int, default=4)
    a = a.parse_args()
    base = os.path.splitext(a.tex)[0]; best = None
    for fs in [float(s) for s in a.sizes.split(',')]:
        job = base + '_try'
        pdf, errs = compile_tex(a.tex, fs, round(fs * a.ratio, 2), job)
        n, f = fill(pdf, a.cols)
        print('FS=%s pages=%d fill=%s %s' % (fs, n, f, errs[:2]))
        if n <= a.pages: best = (fs, pdf); break
    if not best: sys.exit('Does not fit at the smallest size: cut content (references/style-guide.md).')
    fs, pdf = best
    final = base + '.pdf'
    try: shutil.copyfile(pdf, final)
    except OSError: final = base + '_fit.pdf'; shutil.copyfile(pdf, final)
    print('Chosen FS=%s -> %s' % (fs, final))

if __name__ == '__main__':
    main()
