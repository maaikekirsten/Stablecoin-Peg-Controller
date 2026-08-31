from datetime import datetime, timezone


def format_event(level: str, message: str, **fields) -> str:
    ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    extra = ' '.join(f'{k}={v}' for k, v in sorted(fields.items()))
    return f'[{ts}] {level.upper():<5} {message}' + (f' | {extra}' if extra else '')


def fmt_duration(seconds: float) -> str:
    s = max(0.0, float(seconds))
    return f'{int(s * 1000)}ms' if s < 1.0 else f'{s:.2f}s'
