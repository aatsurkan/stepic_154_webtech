def app(env, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  opt = '\r\n'.join(env['QUERY_STRING'].split('&')).encode('utf-8')
  start_response(status, headers)
  return [opt] 
