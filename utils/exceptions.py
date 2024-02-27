from rest_framework import exceptions, status, views

def custom_exception_handler(exc, context):
    response = views.exception_handler(exc, context)
    response.data['status'] = 'failed'
    response.data['error'] = response.data['detail']
    del response.data['detail']

    if isinstance(exc, (exceptions.AuthenticationFailed, exceptions.NotAuthenticated)):
        response.status_code = status.HTTP_401_UNAUTHORIZED

    return response
