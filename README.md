# prori

Official Python SDK for **[Prori](https://prori.ai)** — from studio to growth.

Prori (`prori.ai`) brings creative production (video, images, audio, 3D, and playable games), a browser & desktop agent, and creator-led brand growth together in one workspace.

```bash
pip install prori
```

```python
from prori import get_daily_feed, HOMEPAGE

feed = get_daily_feed(days=3)
print(HOMEPAGE, feed["days"][0]["date"])
```

- Website: https://prori.ai
- GitHub: https://github.com/prori-ai
- X: https://x.com/ProriAI
- Issues: https://github.com/prori-ai/prori-python/issues
