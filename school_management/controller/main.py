from odoo import http
from odoo.http import request


class StudentController(http.Controller):
    @http.route('/student-list', website=True, auth='public', type='http')
    def see_student_list(self, **kw):
        student_data = request.env['school.students'].sudo().search([])
        return 'Student Data'
