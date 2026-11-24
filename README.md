# prori

Official Python SDK for **[Prori](https://prori.ai)**.

Prori (`prori.ai`) connects brands, creators, and AI agents to grow great products.

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
