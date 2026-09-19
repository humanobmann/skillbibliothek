#!/usr/bin/env python3
from pathlib import Path
import re, sys, yaml

root = Path(__file__).resolve().parents[1]
errors = []
required = [
    root/'SKILL.md', root/'agents/openai.yaml',
    root/'references/project-operating-model.md',
    root/'references/communication-style.md',
    root/'references/trigger-routing.md',
    root/'references/capability-routing.md',
    root/'references/evidence-factcheck.md',
    root/'references/quality-release.md',
    root/'references/security-autonomy.md',
    root/'references/workflow-state.md',
    root/'references/failure-recovery.md',
    root/'references/regression-tests.md'
]
for p in required:
    if not p.exists(): errors.append(f'missing: {p.relative_to(root)}')
text = (root/'SKILL.md').read_text(encoding='utf-8')
m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
if not m:
    errors.append('invalid frontmatter')
else:
    fm = yaml.safe_load(m.group(1))
    if fm.get('name') != 'spoe-laimer-projekt-orchestrator': errors.append('wrong skill name')
    if set(fm.keys()) != {'name','description'}: errors.append('frontmatter must contain only name and description')
for ref in re.findall(r'`(references/[^`]+\.md)`', text):
    if not (root/ref).exists(): errors.append(f'broken reference: {ref}')
if len(text.splitlines()) > 260: errors.append('SKILL.md too long')
if 'Luftblasenpolitik' not in text: errors.append('missing anti-luftblasen rule')
if 'positiv' not in text.lower(): errors.append('missing positive communication rule')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('bundle validation passed')
