def parse_port(value: str) -> int:
    port = int(value)
    if port < 0 or port > 65535:
        raise ValueError("port out of range")
    return port

