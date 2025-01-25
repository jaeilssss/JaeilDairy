from enum import Enum


class ScheduleImportantEnum(str, Enum):
    NORMAL = "보통"
    IMPORTANT = "중요"
    VARY_IMPORTANT = "매우 중요"
