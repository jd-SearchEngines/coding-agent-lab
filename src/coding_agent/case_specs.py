"""Small repair specifications used only by the deterministic teaching model."""

from __future__ import annotations

import base64
from dataclasses import dataclass


@dataclass(frozen=True)
class CaseSpec:
    target: str
    good: str
    wrong: str

    def write_command(self, content: str) -> str:
        encoded = base64.b64encode(content.encode()).decode()
        return (
            'python3 -c "import base64; import shutil; from pathlib import Path; '
            "shutil.rmtree('__pycache__', ignore_errors=True); "
            f"Path('{self.target}').write_bytes(base64.b64decode('{encoded}'))"
            '"'
        )


CASE_SPECS = {
    "case_001": CaseSpec(
        "name_utils.py",
        'def normalize_name(name: str) -> str:\n    """Return a canonical display name."""\n    return " ".join(name.split()).casefold()\n',
        'def normalize_name(name: str) -> str:\n    """Return a canonical display name."""\n    return name.strip()\n',
    ),
    "case_002": CaseSpec(
        "ports.py",
        'def parse_port(value: str) -> int:\n    port = int(value)\n    if port < 1 or port > 65535:\n        raise ValueError("port out of range")\n    return port\n',
        'def parse_port(value: str) -> int:\n    port = int(value)\n    if port < 0 or port > 65535:\n        raise ValueError("port out of range")\n    return port\n',
    ),
    "case_003": CaseSpec(
        "text_utils.py",
        'def truncate_text(text: str, limit: int) -> str:\n    if len(text) <= limit:\n        return text\n    words = text[: max(0, limit - 3)].rstrip()\n    return words + "..."\n',
        'def truncate_text(text: str, limit: int) -> str:\n    if len(text) <= limit:\n        return text\n    return text[:limit] + "..."\n',
    ),
    "case_004": CaseSpec(
        "time_utils.py",
        'def format_seconds(seconds: int) -> str:\n    if seconds < 0:\n        raise ValueError("seconds must be non-negative")\n    minutes, remainder = divmod(seconds, 60)\n    return f"{minutes:02d}:{remainder:02d}"\n',
        'def format_seconds(seconds: int) -> str:\n    minutes, remainder = divmod(seconds, 60)\n    return f"{minutes}:{remainder}"\n',
    ),
    "case_005": CaseSpec(
        "math_utils.py",
        'def safe_divide(numerator: float, denominator: float) -> float:\n    if denominator == 0:\n        raise ValueError("zero denominator")\n    return numerator / denominator\n',
        'def safe_divide(numerator: float, denominator: float) -> float:\n    if denominator == 0:\n        return 0.0\n    return numerator / denominator\n',
    ),
}
