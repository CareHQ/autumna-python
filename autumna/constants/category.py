from enum import Enum

__all__ = ('Category',)


class Category(Enum):

    CONTACT_FORM_MESSAGE = 1
    IN_PERSON_VISIT_REQUEST = 2
    VIRTUAL_VISIT_REQUEST = 3
    CALL_BACK_REQUEST = 4
    EMAIL_DETAILS_REQUEST = 5
    REFERRAL_WITH_CONTACT = 6
    REFERRAL_WITHOUT_CONTACT = 7
    PLACEMENT = 8
