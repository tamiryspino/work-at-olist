from flask import request
from flask_mongoengine import Pagination
import json
import re


def search(model, search_text):
    query = re.compile('.*'+search_text+'.*', re.IGNORECASE)
    return model.objects(name=query)


def paginate(results):
    '''Returns a dict with returned items of requested page from the model
       and necessary params of Pagination'''
    obj = {}
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    paginator = Pagination(results, page, per_page)

    # TODO Return obj['items']=[] if page does not exist
    obj['items'] = [json.loads(item.to_json()) for item in paginator.items]
    obj['has_next'] = paginator.has_next
    obj['has_prev'] = paginator.has_prev
    obj['next_num'] = paginator.next_num
    obj['page'] = paginator.page
    obj['pages'] = paginator.pages
    obj['per_page'] = paginator.per_page
    obj['prev_num'] = paginator.prev_num
    obj['total'] = paginator.total

    return obj
