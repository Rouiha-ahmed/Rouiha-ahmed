#!/usr/bin/env python3
"""Regenerate the two light/dark focus cards. Python standard library only."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

THEMES = {
    "dark": {
        "bg": "#0D1117", "panel": "#161B22", "line": "#30363D",
        "text": "#F0F3FA", "muted": "#A4AFBF", "accent": "#B7A7F3",
        "teal": "#5EEAD4", "pill": "#212436", "dim": "#8996AB",
    },
    "light": {
        "bg": "#FAFBFF", "panel": "#F0F2F8", "line": "#D8DEE9",
        "text": "#202A3B", "muted": "#556278", "accent": "#7251B5",
        "teal": "#0D766C", "pill": "#EDE7F9", "dim": "#66748A",
    },
}


def text(x, y, value, fill, size=18, weight=400, extra=""):
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" {extra}>{escape(value)}</text>'
    )


def svg(width, height, title, description, content):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-labelledby="title desc">\n'
        f'<title id="title">{escape(title)}</title>\n'
        f'<desc id="desc">{escape(description)}</desc>\n'
        '<style>\n'
        'text { font-family: "DejaVu Sans Mono", "SFMono-Regular", Consolas, monospace; }\n'
        '.cursor { animation: blink 1.1s steps(1,end) infinite; }\n'
        '.intro { animation: arrive .75s ease-out both; }\n'
        '@keyframes blink { 0%,49% { opacity:1; } 50%,100% { opacity:0; } }\n'
        '@keyframes arrive { from { opacity:0; } to { opacity:1; } }\n'
        '@media (prefers-reduced-motion: reduce) { .cursor, .intro { animation:none; } }\n'
        '</style>\n' + "\n".join(content) + '\n</svg>\n'
    )


def focus(p, kind):
    build = kind == "build"
    color = p["teal"] if build else p["accent"]
    title = "Currently building" if build else "Currently learning"
    tag = "01 / WORKBENCH" if build else "02 / NEXT UP"
    rows = (
        [("INTERFACES", "Next.js + React"), ("APPLICATION LOGIC", "TypeScript"), ("DATA LAYER", "Prisma + PostgreSQL")]
        if build else
        [("BACKEND", "Java + Spring Boot"), ("DELIVERY", "DevOps + Docker"), ("INFRASTRUCTURE", "Cloud + deployment")]
    )
    parts = [
        f'<rect x="1" y="1" width="478" height="300" rx="14" fill="{p["bg"]}" stroke="{p["line"]}" stroke-width="2"/>',
        text(26, 33, tag, color, 12, 600, 'letter-spacing="1.4"'),
        text(26, 68, title, p["text"], 23, 600),
        f'<path d="M26 88H454" stroke="{p["line"]}"/>',
    ]
    for index, (label, value) in enumerate(rows):
        y = 117 + 62 * index
        parts += [
            f'<rect x="26" y="{y-8}" width="3" height="38" rx="1.5" fill="{color}"/>',
            text(42, y, label, p["muted"], 11, 500, 'letter-spacing="1"'),
            text(42, y + 24, value, p["text"], 18, 500),
        ]
    return svg(480, 302, title, "; ".join(value for _, value in rows), parts)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    for name, palette in THEMES.items():
        for kind in ("build", "learn"):
            (ASSETS / f"focus-{kind}-{name}.svg").write_text(focus(palette, kind), encoding="utf-8")
    print("Generated 4 focus-card SVG assets.")


if __name__ == "__main__":
    main()
