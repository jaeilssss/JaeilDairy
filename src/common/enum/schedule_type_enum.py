from enum import Enum


class ScheduleTypeEnum(str, Enum):
    ALL = "전체"
    COMPANY = "회사"
    PRIVATE = "개인"
    FRIEND = "친구"
    ETC = "기타"
