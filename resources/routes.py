from resources.author import AuthorsApi, AuthorApi


def initialize_routes(api):
    api.add_resource(AuthorsApi, '/api/authors')
    api.add_resource(AuthorApi, '/api/authors/<id>')
