# Ahmed Rouiha — GitHub profile

This repository displays the profile README for [Rouiha-ahmed](https://github.com/Rouiha-ahmed). The layout is adapted from the supplied `emmi-lili-main.zip` reference and uses Ahmed's own portrait, text, stack, and links.

The README swaps local SVG assets for light and dark GitHub themes. The animated banner is generated from `assets/ahmed-rouiha.jpeg`; the focus cards are static SVGs. The statistics card and language chart use public GitHub data. A scheduled workflow refreshes those two assets daily with GitHub's built-in token.

To regenerate the banner after changing the portrait or text:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/banner/requirements.txt
.venv/bin/python scripts/banner/generate.py
```

To regenerate the focus cards:

```bash
python3 scripts/generate_assets.py
```

To refresh public statistics and the language chart locally:

```bash
python3 scripts/cards.py --user Rouiha-ahmed
python3 scripts/radar.py --github Rouiha-ahmed -o assets/radar-langs --title "GitHub language mix"
```

The Python metrics scripts require network access. No personal access token is required for public data. On GitHub, the workflow uses the repository's built-in `GITHUB_TOKEN`.
