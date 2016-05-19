import json
from importd import d
from .models import Requests


@d("/AddURLToQueue/")
def add_url_to_queue(request):
    try:
        url = request.GET.get('url')
        if url:
            r = Requests.objects.create(url=url)
            return int(r.id)
        return
    except:
        return


@d("/GetResult/")
def get_result(request):
    try:
        id = request.GET.get('id')
        if id:
            r = Requests.objects.filter(id=id).first()
            if r:
                if not r.processed:
                    return json_resp({'code': 2, 'error': 'Error: not processed yet'})
                return json_resp({'code': 0, 'result': r.result})
            return json_resp({'code': 1, 'error': 'Error: ID not Found'})
        return
    except:
        return


def json_resp(resp):
    return json.dumps(resp)
