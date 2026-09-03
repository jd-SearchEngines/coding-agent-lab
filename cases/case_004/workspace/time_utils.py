def format_seconds(seconds: int) -> str:
    minutes, remainder = divmod(seconds, 60)
    return f"{minutes}:{remainder}"

