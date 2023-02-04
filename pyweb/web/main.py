from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pyweb.api.v1 import index as index_apiv1
from pyweb.api.v1 import users as users_apiv1

from pyweb.api.v2 import dashboard as dashboard_apiv2
from pyweb.api.v2 import users as users_apiv2

from pyweb.web.controllers.auth import routes as auth_routes
from pyweb.web.controllers.root import routes as home_routes


webapp = FastAPI(help="WebAPP com FastApi101")
webapp.mount('/pyweb/web/statics', StaticFiles(directory='pyweb/web/statics'), name='statics')
templates = Jinja2Templates(directory='pyweb/web/templates')


webapp.include_router(index_apiv1.routes)
webapp.include_router(users_apiv1.routes)

webapp.include_router(dashboard_apiv2.routes)
webapp.include_router(users_apiv2.routes)

webapp.include_router(auth_routes)
webapp.include_router(home_routes)
