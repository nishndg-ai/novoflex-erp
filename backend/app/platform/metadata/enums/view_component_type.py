from enum import Enum


class ViewComponentType(str, Enum):

    FIELD = "FIELD"

    LABEL = "LABEL"

    BUTTON = "BUTTON"


    TAB = "TAB"

    GROUP = "GROUP"

    SECTION = "SECTION"


    SEPARATOR = "SEPARATOR"

    SPACER = "SPACER"


    IMAGE = "IMAGE"

    HTML = "HTML"


    CUSTOM = "CUSTOM"