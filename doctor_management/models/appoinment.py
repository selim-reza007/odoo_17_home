from odoo.exceptions import ValidationError
from odoo import api, models, fields, _

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Hospital patient appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "ref"
    _order = "id desc"

    ref = fields.Char("Reference")
    patient_id = fields.Many2one('hospital.patient', string="Patient", tracking=2)
    room = fields.Char("Bed no.", tracking=1)
    duration = fields.Float('Average duration')
    appointment_date = fields.Date(string="Appointment date", tracking=True)
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    state = fields.Selection([
        ('bed', 'Bed'),
        ('visited', 'Visited'),
        ('prescribe', 'Prescribe'),
        ('released', 'Released'),
        ('cancelled', 'Cancelled'),
    ], string='Appointment Status', tracking=True)
    operation = fields.Many2one("hospital.operation", string="Operation")
    progress = fields.Integer(string="Progress", compute="_compute_progress")
    medicine_ids = fields.One2many("hospital.appointment.medicine.line","appointment_id",string="Medicine")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    total_amount = fields.Monetary(string="Total Amount", compute="_compute_total_amount", currency_field="currency_id")

    def action_notification(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'info',
                'title': _('Sending invoices'),
                'message': _('Some dummy message.'),
                'next': {'type': 'ir.actions.act_window_close'},
            },
        }

    def sent_in_whatsapp(self):
        if not self.patient_id.phone:
            raise ValidationError(_("Missing phone number!"))
        msg = "Hi!, %s" % self.patient_id.name
        whatsapp_api = "https://api.whatsapp.com/send?phone=%s&text=%s" % (self.patient_id.phone, msg)
        return {
            'type': 'ir.actions.act_url',
            'target' : 'new',
            'url' : whatsapp_api,
        }

    @api.depends('medicine_ids.sub_total')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = sum(rec.medicine_ids.mapped('sub_total'))

    @api.depends('progress')
    def _compute_progress(self):
        for rec in self:
            if rec.state == 'bed':
                rec.progress = 25
            elif rec.state == 'visited':
                rec.progress = 50
            elif rec.state == 'prescribe':
                rec.progress = 75
            elif rec.state == 'released':
                rec.progress = 100
            else:
                rec.progress = 0

    def state_bed(self):
        self.write({'state' : 'bed'})

    def state_visited(self):
        self.write({'state': 'visited'})

    def state_prescribe(self):
        self.write({'state': 'prescribe'})

    def state_released(self):
        self.write({'state': 'released'})

    def state_cancelled(self):
        self.write({'state': 'cancelled'})

    def unlink(self):
        for rec in self:
            if rec.state == "bed":
                raise ValidationError(_("Appointment can't be deleted when state is in bed state!"))
        return super(Appointment, self).unlink()

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('appointment.sequence.data')
        return super(Appointment, self).create(vals)

    def cancel_appointment(self):
        return self.env.ref('doctor_management.action_cancel_appointment_wizard').read()[0]

    def redirect_button(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'https://www.youtube.com',
        }


class AppointmentMedicineLine(models.Model):
    _name = 'hospital.appointment.medicine.line'
    _description = 'hospital appointment medicine line'
    _rec_name = 'product'

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    product = fields.Many2one("product.product", string="Product")
    unit_price = fields.Float("Unit Price", related="product.list_price", digits='Product Price')
    qty = fields.Integer("Quantity")
    company_currency_id = fields.Many2one('res.currency', related="appointment_id.currency_id")
    sub_total = fields.Monetary("Sub-total", compute="_compute_sub_total", currency_field="company_currency_id")

    @api.depends('qty', 'unit_price')
    def _compute_sub_total(self):
        for rec in self:
            rec.sub_total = rec.qty * rec.unit_price