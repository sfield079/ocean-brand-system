"""Every AI tool gets the same rules: pointer files, app-builder limits and an up-to-date web kit."""
import json, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
POINTERS = ['CLAUDE.md', 'GEMINI.md', '.github/copilot-instructions.md', '.cursor/rules/ocean-brand.mdc',
            'skills/ocean-brand/SKILL.md', 'AI-TOOLS.md', 'llms.txt', 'brand/CHATGPT-PROJECT-INSTRUCTIONS.md']


class AIToolTests(unittest.TestCase):
    def test_pointer_files_point_to_agents(self):
        for f in POINTERS:
            text = (ROOT / f).read_text()
            self.assertIn('AGENTS.md', text, f)
            for rule in (['close', 'do not use', 'never stretch', 'web-kit'] if f not in ('AI-TOOLS.md', 'llms.txt') else []):
                self.assertIn(rule, text.lower().replace('never stretched', 'never stretch').replace('not stretch', 'never stretch'), f'{f} is missing the {rule!r} rule')

    def test_app_builder_instructions_fit_limit(self):
        n = len((ROOT / 'brand/AI-APP-BUILDER-INSTRUCTIONS.md').read_text())
        self.assertLess(n, 10000, 'Base44 sends only the first 10,000 characters of custom instructions')

    def test_web_kit_matches_tokens(self):
        before = {p: (ROOT / p).read_text() for p in ('web-kit/ocean.css', 'tokens/build/ocean.css', 'web-kit/ocean.tokens.json', 'web-kit/notices.json')}
        subprocess.run([sys.executable, str(ROOT / 'scripts/build_web_kit.py')], check=True, capture_output=True)
        for p, text in before.items():
            self.assertEqual(text, (ROOT / p).read_text(), f'{p} is out of date: run python3 scripts/build_web_kit.py')
        css = before['web-kit/ocean.css']
        for d in json.loads((ROOT / 'tokens/ocean.tokens.json').read_text())['pairing']['detail']:
            a, b = d['pair'].split('+')
            self.assertIn(f'[data-pair="{a}-{b}"]', css); self.assertIn(f'[data-pair="{b}-{a}"]', css)
        for w in ('Light', 'Regular', 'Medium', 'Bold'):
            self.assertTrue((ROOT / f'web-kit/fonts/StackSansHeadline-{w}.woff2').exists())

    def test_references_exist(self):
        r = subprocess.run([sys.executable, str(ROOT / 'scripts/check_references.py')], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)


if __name__ == '__main__':
    unittest.main()
