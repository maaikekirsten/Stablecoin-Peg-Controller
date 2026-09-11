# Architecture Notes

## Modules
- `src/config.py`: Environment parsing and runtime defaults.
- `src/cache.py`: Bounded in-memory TTL store.
- `src/retry.py`: Jittered exponential backoff policies.
- `src/validator.py`: Input validation and slug sanitization.
- `src/metrics.py`: Lightweight counters and latency histograms.

### Cache Eviction
Expired entries are purged lazily on reads and swept before reaching `max_items` capacity.

### Shutdown Checklist
Flush in-flight metrics snapshots and release local file locks before exiting worker loops.
