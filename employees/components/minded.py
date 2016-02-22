def get_minded_request(request):
    r = request.GET
    if bool(r) and 'page' not in r:
        request.session['filter'] = r
    else:
        r = request.session.get('filter', request.GET)
    return r
