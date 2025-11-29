from contextlib import contextmanager
import time

@contextmanager
def step(name: str):
    print(f"\n➡️  STEP: {name}")
    start = time.time()
    try:
        yield
        duration = time.time() - start
        print(f"PASSED: {name} ({duration:.2f}s)")
    except Exception as e:
        print(f"FAILED: {name}: {e}")
        raise
