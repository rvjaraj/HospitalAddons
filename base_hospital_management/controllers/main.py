# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
import werkzeug
from werkzeug.urls import url_encode

from odoo import http, tools, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.home import ensure_db, Home, SIGN_UP_REQUEST_PARAMS, LOGIN_SUCCESSFUL_PARAMS
from odoo.addons.base_setup.controllers.main import BaseSetup
from odoo.exceptions import UserError
from odoo.http import request

_logger = logging.getLogger(__name__)


class AuthSignupHome(Home):
    def _prepare_signup_values(self, qcontext):
        values = super(AuthSignupHome, self)._prepare_signup_values(qcontext)
        if qcontext.get('dob'):
            values.update({'dob': qcontext.get('dob')})
        return values


class OAuthLogin(Home):
    def get_auth_signup_qcontext(self):
        SIGN_UP_REQUEST_PARAMS.update({'dob'})
        return super().get_auth_signup_qcontext()
