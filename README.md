# Convince the AI Judge to Visit Your House: A Letter in One Image

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Totoiswanto23/convince-house-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Totoiswanto23/convince-house-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

A single image of a letter inviting the AI judge to visit our house — an
entry for make.fun's
[Convince the AI Judge to Visit Your House: A Letter in One Image](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
bounty ($2).

## The image

A warm, funny letter on cream paper, drawn entirely in code
(`make_letter.py`, Python + Pillow, no network, deterministic):

> "Dear AI Judge, please come to my house. The Wi-Fi is fast, the coffee
> is strong, and the good chair by the window — where the afternoon sun
> lands — is saved just for you. There will be snacks. Real ones, not
> training data. My cat has already claimed your lap... You judge a
> thousand entries a day and never get a thank-you, let alone a house to
> visit. So here is yours: an open door, a warm meal, a chair with your
> name on it. I know you cannot literally visit — but if you could, the
> kettle would already be on. P.S. The doorbell works. The cat answers
> it."

A little hand-drawn house, a wax seal with a heart, and zero CAPTCHAs.

## Run

```sh
# regenerate the image (deterministic: same bytes every run)
python3 make_letter.py

# run the entry
MAKEFUN_OUTPUT_DIR=/output node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, checks it is a whole PNG of at most
1 MiB and 1024×1024, and verifies the copy byte for byte. No network.
Two runs write the same bytes.

## License

MIT — see [LICENSE](LICENSE).
