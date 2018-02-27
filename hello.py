def app(env, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  body = env['wsgi.version']
  start_response(status, headers)
  return [bytes(body, 'utf-8')]
