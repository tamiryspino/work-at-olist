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
from resources.pagination import paginate, search


class AuthorsApi(Resource):
    def get(self):
        search_text = request.args.get('search')
        if search_text:
            authors = paginate(search(Author, search_text))
        else:
            authors = paginate(Author.objects)
        return Response(json.dumps(authors),
                        mimetype="application/json",
                        status=200)

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
