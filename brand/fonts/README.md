# Required font

Stack Sans Headline, the exact family on page 8 of Ocean_StyleGuide_2026.pdf.
Source: https://github.com/google/fonts/tree/main/ofl/stacksansheadline
Downloaded 2026-09-25 under SIL Open Font License 1.1 (OFL.txt).
The variable source is preserved. Regular 400, Medium 500, SemiBold 600 and Bold
700 are static instances generated with fontTools.varLib.instancer and
updateFontNames=True for predictable PDF and office rendering.

Run `python scripts/install_fonts.py`. Windows installs only for the current
user, Linux uses ~/.local/share/fonts/ocean and refreshes fontconfig, macOS uses
~/Library/Fonts. PDF document generation embeds the bundled files directly.
Never use a fallback if the font fails. Stop and fix the font setup.
