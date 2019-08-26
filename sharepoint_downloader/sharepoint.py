# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:00:55 2019

@author: MRZEZNIC
"""

# https://pypi.org/project/Office365-REST-Python-Client/
# via ClientRequest class where you need to construct REST queries by specifying endpoint url, headers if required and payload (aka low level approach)

import json

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.runtime.client_request import ClientRequest
from office365.runtime.utilities.request_options import RequestOptions

ctx_auth = AuthenticationContext(url)
if ctx_auth.acquire_token_for_user(username, password):
  request = ClientRequest(ctx_auth)
  options = RequestOptions("{0}/_api/web/".format(url))
  options.set_header('Accept', 'application/json')
  options.set_header('Content-Type', 'application/json')
  data = request.execute_request_direct(options)
  s = json.loads(data.content)
  web_title = s['Title']
  print "Web title: " + web_title
else:
  print ctx_auth.get_last_error()

# via ClientContext class where you target client object resources such as Web, ListItem and etc.

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

ctx_auth = AuthenticationContext(url)
if ctx_auth.acquire_token_for_user(username, password):
  ctx = ClientContext(url, ctx_auth)
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print "Web title: {0}".format(web.properties['Title'])

else:
  print ctx_auth.get_last_error()
