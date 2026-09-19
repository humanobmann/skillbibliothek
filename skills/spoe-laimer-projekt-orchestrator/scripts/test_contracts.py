#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
checks = {
    'SKILL.md': ['kommunale Arbeit', 'Alltagsnutzen', 'Robert Laimer', 'Luftblasenpolitik', 'positive'],
    'references/project-operating-model.md': ['Konkretheitsgate', 'Kommunalitätsprüfung', 'Sozialdemokratischer Nutzentest'],
    'references/communication-style.md': ['Zuversicht', 'Lösung', 'Kommunaler Stil'],
    'references/evidence-factcheck.md': ['kommunale Primärquelle', 'Gegenbelegsuche'],
    'references/quality-release.md': ['Anti-Luftblasen-QA', 'Purple Team'],
}
errors=[]
for rel, needles in checks.items():
    t=(root/rel).read_text(encoding='utf-8')
    for n in needles:
        if n.lower() not in t.lower(): errors.append(f'{rel}: missing {n}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('contract tests passed')
