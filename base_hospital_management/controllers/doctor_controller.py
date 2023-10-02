from odoo import http
from odoo.http import request


class DoctorController(http.Controller):

    @http.route('/web/doctors', type='http', auth="user", website=True)
    def doctor_kanban(self, **kw):
        employees = request.env['hr.employee'].search([('is_doctor', '=', 'doctor'),
                                                       ('published', '=', True)])
        return request.render('base_hospital_management.doctor_kanban_template', {
            'employees': employees,
        })

    @http.route(['/doctors'], type='http', auth="public", website=True)
    def service_request(self):
        return request.render("base_hospital_management.controller_doctor_form")

    @http.route('/create/doctors', methods=['POST', 'GET'], type='http',
                auth="public", website=True, csrf=False)
    def submit_form(self, **kw):
        """Taking appointment to doctor"""
        if kw:
            # Crear un nuevo doctor con los datos del formulario
            doctor_vals = {
                'name': kw.get('doctor_name'),
                'job_title': kw.get('title'),
                'identification_id': kw.get('identification_id'),
                'gender': kw.get('gender'),
                'mobile_phone': kw.get('phone'),
                'work_email': kw.get('email'),
                'birthday': kw.get('birthday'),
                'title_registration': kw.get('title_registration'),
                'registration_number': kw.get('registration_number'),
                'is_doctor': 'doctor',
            }

            doctor = request.env['hr.employee'].sudo().create(doctor_vals)
            vals = {'doctor': doctor}
            return request.render(
                'base_hospital_management.doctor_thanks', vals)
        else:
            return request.redirect('/')

    @http.route('/create/comment', type='http', auth="user", website=True, csrf=False, methods=['POST'])
    def create_comment(self, **kw):
        if kw:
            user = request.env.user
            doctor_id = int(kw.get(
                'doctor_id'))
            rating = int(kw.get('rating'))
            comment = kw.get('comment')
            DoctorRating = request.env['doctor.rating']
            DoctorRating.create({
                'user_id': user.id,
                'doctor_id': doctor_id,
                'rating': str(rating),
                'review': comment,
            })
            return request.redirect('/web/doctors')
        else:
            return request.redirect('/')
