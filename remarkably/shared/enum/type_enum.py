from enum import Enum


class EventType(Enum):
    SYSTEM = "system"
    EXTERNAL = "external"
    STAFF = "staff"
    USER = "user"
    UNKNOWN = "unknown"
