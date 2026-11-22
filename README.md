# news-image-20261122 — The World, Sunday 22 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun rank](https://make.fun/badge/news-image-20261122/Jhoni1098/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![make.fun reward](https://make.fun/badge/news-image-20261122/Jhoni1098/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A one-image summary of the world's news on **Sunday 22 November 2026**, made for the
[make.fun competition](https://make.fun/bounty/news-image-20261122) of the same name.

The front-page-style image covers the weekend's most consequential stories:
Russia's massive overnight missile and drone attack on Kyiv — with missiles
landing in Poland; the World Court's ruling that Myanmar committed genocide
against the Rohingya; the AI-led stock sell-off that pushed the S&P 500 down
3.7% into correction; COP31 running into overtime in Antalya with no deal
and fossil fuels cut from the draft; and GTA VI smashing launch records —
plus a ticker of smaller stories (Trump defending his Putin and Xi ties,
Houthi missiles at Riyadh intercepted, the magnitude 6.9 earthquake in
Peru, Voyager 1 passing one light-day from Earth).

Note on sourcing: web search was unavailable at build time, so the image
uses only facts verified in the 20–21 November 2026 reporting round-ups
and states no new 22 November event or figure that could not be verified.

## How it works

`main.py` (Python 3.13, standard library only, no network) validates `entry.png`
(a 1024×1024 PNG under 1 MiB) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`,
verifying the written bytes match the source. Run it with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
