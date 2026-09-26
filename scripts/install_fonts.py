"""Install the exact bundled Ocean font for the current Windows/Linux/macOS user."""
import os, platform, shutil, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
def install():
    fonts = sorted((ROOT / 'brand/fonts').glob('StackSansHeadline-*.ttf'))
    fonts = [f for f in fonts if 'variable' not in f.name]
    if len(fonts) != 5:
        raise RuntimeError('Bundled static fonts missing. Restore brand/fonts from GitHub.')
    system = platform.system()
    if system == 'Windows':
        import ctypes, winreg
        dest = Path(os.environ['LOCALAPPDATA']) / 'Microsoft/Windows/Fonts'
    elif system == 'Darwin':
        dest = Path.home() / 'Library/Fonts'
    else:
        dest = Path.home() / '.local/share/fonts/ocean'
    dest.mkdir(parents=True, exist_ok=True)
    for src in fonts:
        target = dest / src.name
        if not target.exists() or target.read_bytes() != src.read_bytes():
            shutil.copy2(src, target)
        if system == 'Windows':
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                r'Software\Microsoft\Windows NT\CurrentVersion\Fonts') as key:
                winreg.SetValueEx(key, src.stem + ' (TrueType)', 0, winreg.REG_SZ, str(target))
            ctypes.windll.gdi32.AddFontResourceW(str(target))
    if system == 'Windows':
        result = ctypes.c_size_t()
        ctypes.windll.user32.SendMessageTimeoutW(0xFFFF, 0x001D, 0, 0, 2, 1000, ctypes.byref(result))
    elif shutil.which('fc-cache'):
        subprocess.run(['fc-cache', '-f', str(dest)], check=True)
        resolved = subprocess.check_output(['fc-match', '-f', '%{family}', 'Stack Sans Headline'], text=True)
        if 'Stack Sans Headline' not in resolved:
            raise RuntimeError(f'Font substitution detected: {resolved}')
    print(f'Installed Stack Sans Headline (Light, Regular, Medium, SemiBold, Bold): {dest}')
if __name__ == '__main__': install()
