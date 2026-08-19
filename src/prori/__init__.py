from __future__ import annotations

import json
from typing import Any
from urllib.request import Request, urlopen

__version__ = "0.0.1"
HOMEPAGE = "https://prori.ai"
API_BASE = "https://api.bnbot.ai"


def get_daily_feed(
    days: int = 3,
    per_day: int = 15,
    base_url: str = API_BASE,
    timeout: float = 20,
) -> dict[str, Any]:
    """Public daily product feed used by prori.ai."""
    url = f"{base_url.rstrip('/')}/api/v1/products/daily-feed?days={days}&per_day={per_day}"
    req = Request(url, headers={"Accept": "application/json", "User-Agent": f"prori-python/{__version__}"})
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


__all__ = ["API_BASE", "HOMEPAGE", "__version__", "get_daily_feed"]
