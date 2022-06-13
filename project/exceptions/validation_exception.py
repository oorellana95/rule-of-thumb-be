"""Validation Exception Classes"""
from project.exceptions import ProjectException


class ValidationException(ProjectException):
    def __init__(self):
        super().__init__()
        self.code = "ERROR.VALIDATION"


class InputValidationException(ValidationException):
    def __init__(self, message):
        super().__init__()
        self.message = message
