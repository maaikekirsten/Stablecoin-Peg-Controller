import os
from dataclasses import dataclass


@dataclass
class RuntimeConfig:
    env: str = 'production'
    timeout_sec: int = 30
    max_retries: int = 3
    debug: bool = False


def load_config() -> RuntimeConfig:
    return RuntimeConfig(
        env=os.getenv('APP_ENV', 'production'),
        timeout_sec=int(os.getenv('TIMEOUT_SEC', '30')),
        max_retries=int(os.getenv('MAX_RETRIES', '3')),
        debug=os.getenv('DEBUG', '0').lower() in {'1', 'true', 'yes'},
    )


def redact_secret(secret: str, visible: int = 4) -> str:
    s = str(secret or '')
    return ('*' * max(4, len(s) - visible)) + s[-visible:] if len(s) > visible else '****'


def parse_positive_int(raw, fallback: int = 1) -> int:
    try:
        val = int(str(raw).strip())
        return val if val > 0 else fallback
    except (TypeError, ValueError):
        return fallback


def parse_csv_env(raw: str) -> list:
    return [item.strip() for item in str(raw or '').split(',') if item.strip()]
