class lib:
    def start_instrumentation() -> None: ...
    def stop_instrumentation() -> None: ...
    def dump_stats() -> None: ...
    def dump_stats_at(trigger: str) -> None: ...
    def zero_stats() -> None: ...
    def toggle_collect() -> None: ...
