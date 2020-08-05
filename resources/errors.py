class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class ValidationError(Exception):
    pass


class AuthorAlreadyExistsError(Exception):
    pass


class UpdatingAuthorError(Exception):
    pass


class DeletingAuthorError(Exception):
    pass


class AuthorNotExistsError(Exception):
    pass


class EmailAlreadyExistsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class DoesNotExistError(Exception):
    pass


class EmailDoesnotExistsError(Exception):
    pass


class BadTokenError(Exception):
    pass


class ExpiredTokenError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ValidationError": {
        "message": "Invalid field",
        "status": 400
    },
    "AuthorAlreadyExistsError": {
        "message": "Author with given name already exists",
        "status": 400
    },
    "UpdatingAuthorError": {
        "message": "Updating movie added by other is forbidden",
        "status": 403
    },
    "DeletingAuthorError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403
    },
    "AuthorNotExistsError": {
        "message": "Author with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "DoesNotExistError": {
        "message": "User doesn't exist",
        "status": 401
    },
    "EmailDoesnotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400
    },
    "BadTokenError": {
        "message": "Invalid token",
        "status": 403
    },
    "ExpiredTokenError": {
        "message": "Expired token",
        "status": 403
    }
}
