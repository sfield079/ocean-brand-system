from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
from lib.publication import build
for name in ('proposal','report'):
    build(ROOT/f'documents/_starter/{name}.json',ROOT/f'output/pdf/ocean-{name}-reference.pdf')
