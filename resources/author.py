from flask import Response, request, jsonify
from database.models import Author
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_mongoengine import Pagination
from mongoengine.errors import (FieldDoesNotExist, NotUniqueError,
                                DoesNotExist, ValidationError,
                                InvalidQueryError)
import json
from resources.errors import (SchemaValidationError, AuthorAlreadyExistsError,
                              InternalServerError, UpdatingAuthorError,
                              DeletingAuthorError, AuthorNotExistsError)


class AuthorsApi(Resource):
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 3))
        paginator = Pagination(Author.objects, page, per_page)

        # TODO Return [] if page does not exist
        # TODO Return paginator properties
        authors_json = [i.to_json() for i in paginator.items]

        return Response(authors_json, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            author = Author(**body)
            author.save()
            id = author.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise AuthorAlreadyExistsError
        except Exception:
            raise InternalServerError


class AuthorApi(Resource):
    def put(self, id):
        try:
            author = Author.objects.get(id=id)
            body = request.get_json()
            author.update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingAuthorError
        except Exception:
            raise InternalServerError

    def delete(self, id):
        try:
            author = Author.objects.get(id=id)
            author.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingAuthorError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            authors = Author.objects.get(id=id).to_json()
            return Response(authors, mimetype="application/json", status=200)
        except DoesNotExist:
            raise AuthorNotExistsError
        except Exception:
            raise InternalServerError
