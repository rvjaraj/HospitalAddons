# -*- coding: utf-8 -*-
#################################################################################
#
# Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>:wink:
# See LICENSE file for full copyright and licensing details.
#################################################################################
import logging

from odoo.http import request, route
from odoo.exceptions import UserError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.web.controllers.main import SIGN_UP_REQUEST_PARAMS

_logger = logging.getLogger(__name__)


class AuthSignupHome(Home):
    def _prepare_signup_values(self, qcontext):
        values = super(AuthSignupHome, self)._prepare_signup_values(qcontext)
        if qcontext.get('dob'):
            values.update({'dob': qcontext.get('dob')})
        return values


class AuthSighup(AuthSignupHome):

    def get_auth_signup_qcontext(self):
        SIGN_UP_REQUEST_PARAMS.update({'dob'})
        return super().get_auth_signup_qcontext()
