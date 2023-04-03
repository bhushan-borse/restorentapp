from enum import Enum


class ErrorMessages(Enum):
    REQUIRE = "{}!. Field is required."
    AL_NULL = "{}!. Field is not null."
    AL_BLANK = "{}!. Field should not be blank."
    INT_FAIL = "{}!. Value should be Integer ({})."
    FLOAT_FAIL = "{}!. Value should be Float ({})."
    DICT_FAIL = "{}!. Value should be Dict ({})."
    LIST_FAIL = "{}!. Value should be List ({})."
