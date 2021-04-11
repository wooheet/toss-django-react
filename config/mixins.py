import logging
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList

logger = logging.getLogger(__name__)


class CustomResponseMixin(object):

    def _validation_error(self, error):
        if isinstance(error, dict) and 'code' in error and 'message' in error:
            return True
        return False

    def success(self, status_code=200, detail='Success', results=None,
                next=None, previous=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, next=next, previous=previous)

    def bad_request(self, status_code=400, detail="Bad Request", results=None,
                    error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def forbidden(self, status_code=403, detail="Forbidden", results=None,
                  error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def not_acceptable(self, status_code=406, detail="Not Acceptable",
                       results=None, error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def not_found(self, status_code=404, detail="Not Found", results=None,
                  error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def timeout(self, status_code=408, detail="Request Time Out",
                results=None, error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def server_maintenance(self, status_code=503, detail="Server Maintenance",
                           results=None, error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def server_exception(self, status_code=500,
                         detail="Iternal Server Exception", results=None,
                         error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def un_authorized(self, status_code=401, detail="UnAuthorized Request",
                      results=None, error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def conflict(self, status_code=409, detail="Conflict", results=None,
                 error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def unprocessable_entity(self, status_code=422,
                             detail="Unprocessable Entity", results=None,
                             error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def too_many_request(self, status_code=429, detail="Too Many Requests",
                         results=None, error=None):
        return self.get_response(status_code=status_code, detail=detail,
                                 results=results, error=error)

    def get_response(self, status_code, detail, results, next=None,
                     previous=None, error=None):
        if results is None:
            results = []

        if type(results) != ReturnList and type(results) != list:
            results = [results]

        data = {'status_code': status_code, 'detail': u'{}'.format(detail),
                'results': results}

        if error and isinstance(error, dict) and 'code' in error \
                and 'message' in error:
            data['error'] = error

        if next is not None or previous is not None:
            data["next"] = next or ""
            data["previous"] = previous or ""

        return Response(status=status_code, data=data)