from odoo import http
from odoo.http import request


class DoctorController(http.Controller):

    @http.route('/web/doctors', type='http', auth="user", website=True)
    def doctor_kanban(self, **kw):
        employees = request.env['hr.employee'].search([('is_doctor', '=', 'doctor')])
        return http.request.render('base_hospital_management.doctor_kanban_template', {
            'employees': employees,
        })
