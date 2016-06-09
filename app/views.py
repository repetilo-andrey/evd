from importd import d
from .models import Requests


@d("/AddURLToQueue/")
def add_url_to_queue(request):
    try:
        batch_id = request.GET.get('batchID')
        urls = request.GET.getlist('urls')
        if len(urls) == 0:
            urls = request.GET.getlist('urls[]')
        if batch_id:
            for url in urls:
                Requests.objects.create(url=url, batch_id=batch_id)
            return {'code': 0, 'result': 'Created requests for urls: %s' % ', '.join(urls)}
        return {'code': 1, 'error': 'Error: no batchID'}
    except Exception, e:
        return {'code': 1, 'error': str(e)}


@d("/GetResult/")
def get_result(request):
    try:
        batch_id = request.GET.get('batchID')
        if batch_id:
            requests = Requests.objects.filter(batch_id=batch_id)
            resp = {'batchID': batch_id, 'results': []}
            for r in requests:
                d = {'url': r.url}
                if not r.processed:
                    d['code'] = 2
                    d['error'] = 'Error: not processed yet'
                else:
                    d['code'] = 0
                    d['result'] = r.result
                resp['results'].append(d)
            return resp
        return {'code': 1, 'error': 'Error: no batchID'}
    except Exception, e:
        return {'code': 1, 'error': str(e)}


class UrlsMiddleware(object):
    def process_request(self, request):
        if 'admin/' in request.path:
            response = d.HttpResponse()
            response.status_code = 404
            return response
        return None
