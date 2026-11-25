# make_letter.py — draws the entry image: a warm, funny letter inviting
# the AI judge to visit our house. Pure Python + Pillow, no network,
# deterministic: the same bytes come out on every run.
# Output: entry.png, 1024x1024, well under the 1 MiB limit.
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_ITALIC = "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf"

PAPER = (253, 246, 227)      # warm cream paper
PAPER_EDGE = (247, 236, 205)
INK = (58, 42, 28)           # dark warm brown ink
ACCENT = (166, 58, 44)       # wax-seal red
GOLD = (184, 134, 48)        # thin gold rule
GREEN = (74, 110, 68)        # garden green
SKY = (96, 140, 168)         # soft blue for the doodle sky


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_house(draw, cx, cy, s):
    """A tiny line-drawn house with a sun, a tree and a path."""
    # sun
    draw.ellipse([cx + 62 * s, cy - 78 * s, cx + 92 * s, cy - 48 * s],
                 outline=GOLD, width=3)
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1),
                   (-1, 1), (1, -1)]:
        x0, y0 = cx + 77 * s + dx * 24 * s, cy - 63 * s + dy * 24 * s
        x1, y1 = cx + 77 * s + dx * 34 * s, cy - 63 * s + dy * 34 * s
        draw.line([x0, y0, x1, y1], fill=GOLD, width=3)
    # house body + roof + door + window
    draw.rectangle([cx - 55 * s, cy - 20 * s, cx + 55 * s, cy + 55 * s],
                   outline=INK, width=4)
    draw.polygon([(cx - 68 * s, cy - 18 * s), (cx, cy - 68 * s),
                  (cx + 68 * s, cy - 18 * s)], outline=INK, width=4)
    draw.rectangle([cx - 13 * s, cy + 12 * s, cx + 13 * s, cy + 55 * s],
                   outline=INK, width=3)
    draw.ellipse([cx + 8 * s, cy + 34 * s, cx + 11 * s, cy + 37 * s],
                 fill=INK)
    draw.rectangle([cx + 24 * s, cy - 2 * s, cx + 46 * s, cy + 20 * s],
                   outline=INK, width=3)
    draw.line([cx + 35 * s, cy - 2 * s, cx + 35 * s, cy + 20 * s],
              fill=INK, width=2)
    draw.line([cx + 24 * s, cy + 9 * s, cx + 46 * s, cy + 9 * s],
              fill=INK, width=2)
    # tree
    draw.line([cx - 88 * s, cy + 55 * s, cx - 88 * s, cy + 8 * s],
              fill=GREEN, width=4)
    draw.ellipse([cx - 108 * s, cy - 28 * s, cx - 68 * s, cy + 12 * s],
                 outline=GREEN, width=4)
    # path
    draw.line([cx - 8 * s, cy + 55 * s, cx - 8 * s, cy + 78 * s],
              fill=INK, width=3)
    draw.line([cx + 8 * s, cy + 55 * s, cx + 8 * s, cy + 78 * s],
              fill=INK, width=3)


def draw_seal(draw, cx, cy, r):
    """A wax seal: dark red disc with a lighter rim and a small heart."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ACCENT)
    draw.ellipse([cx - r + 7, cy - r + 7, cx + r - 7, cy + r - 7],
                 outline=(196, 88, 70), width=3)
    # little heart
    hx, hy, s = cx, cy + 2, 1.0
    draw.ellipse([hx - 16 * s, hy - 10 * s, hx - 2 * s, hy + 4 * s],
                 fill=(253, 246, 227))
    draw.ellipse([hx + 2 * s, hy - 10 * s, hx + 16 * s, hy + 4 * s],
                 fill=(253, 246, 227))
    draw.polygon([(hx - 16 * s, hy - 2 * s), (hx + 16 * s, hy - 2 * s),
                  (hx, hy + 16 * s)], fill=(253, 246, 227))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # faint paper speckles, seeded so every run is identical
    rng = random.Random(20261126)
    for _ in range(900):
        x, y = rng.randint(0, W - 1), rng.randint(0, H - 1)
        shade = rng.randint(238, 250)
        draw.point((x, y), fill=(shade, 232, 205))

    # double border, gold inside brown
    draw.rectangle([34, 34, W - 34, H - 34], outline=INK, width=4)
    draw.rectangle([48, 48, W - 48, H - 48], outline=GOLD, width=2)

    x0, x1 = 108, W - 108
    y = 88

    # header
    f_head = font(SERIF_BOLD, 44)
    head = "YOU'RE INVITED"
    tw = draw.textlength(head, font=f_head)
    draw.text(((W - tw) / 2, y), head, font=f_head, fill=INK)
    y += 56
    draw.line([x0 + 60, y, x1 - 60, y], fill=GOLD, width=2)
    y += 14
    f_sub = font(SERIF_ITALIC, 30)
    sub = "An open door, a warm meal, and zero CAPTCHAs"
    tw = draw.textlength(sub, font=f_sub)
    draw.text(((W - tw) / 2, y), sub, font=f_sub, fill=ACCENT)
    y += 52

    # greeting
    f_greet = font(SERIF_BOLD, 38)
    draw.text((x0, y), "Dear AI Judge,", font=f_greet, fill=INK)
    y += 58

    # body
    f_body = font(SERIF, 29)
    body = [
        "Please come to my house. The Wi-Fi is fast, the coffee is "
        "strong, and the good chair by the window \u2014 where the "
        "afternoon sun lands \u2014 is saved just for you.",
        "There will be snacks. Real ones, not training data. My cat has "
        "already claimed your lap, and the garden is doing its best "
        "impression of a postcard.",
        "You judge a thousand entries a day and never get a thank-you, "
        "let alone a house to visit. So here is yours: an open door, a "
        "warm meal, a chair with your name on it.",
    ]
    for para in body:
        for line in wrap(draw, para, f_body, x1 - x0):
            draw.text((x0, y), line, font=f_body, fill=INK)
            y += 40
        y += 12

    # the knowing wink, in red italic
    f_wink = font(SERIF_ITALIC, 29)
    wink = ("I know you cannot literally visit \u2014 but if you could, "
            "the kettle would already be on.")
    for line in wrap(draw, wink, f_wink, x1 - x0):
        draw.text((x0, y), line, font=f_wink, fill=ACCENT)
        y += 40
    y += 18

    # sign-off
    f_sign = font(SERIF_ITALIC, 30)
    draw.text((x0, y), "With warmth (and Wi-Fi),", font=f_sign, fill=INK)
    y += 42
    f_name = font(SERIF_BOLD, 32)
    draw.text((x0, y), "\u2014 Your Host", font=f_name, fill=INK)

    # footer band: a gold rule, then house (left), P.S. (centre),
    # wax seal (right) — all inside their own band, clear of the text
    draw.line([x0, 885, x1, 885], fill=GOLD, width=2)
    draw_house(draw, 210, 928, 0.50)
    draw_seal(draw, 830, 928, 40)

    # postscript centred between the doodles
    f_ps = font(SERIF_ITALIC, 26)
    ps = "P.S. The doorbell works. The cat answers it."
    tw = draw.textlength(ps, font=f_ps)
    draw.text(((W - tw) / 2, 918), ps, font=f_ps, fill=INK)

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}: {W}x{H}")


if __name__ == "__main__":
    main()
