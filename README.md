# prori

Official Python SDK for [Prori](https://prori.ai).

```bash
pip install prori
```

```python
from prori import get_daily_feed, HOMEPAGE

feed = get_daily_feed(days=3)
print(HOMEPAGE, feed["days"][0]["date"])
```

This package reserves the `prori` name on PyPI. The client surface will grow as the public API ships.

- Site: https://prori.ai
- Org: https://github.com/prori-ai
- Issues: https://github.com/prori-ai/prori-python/issues
