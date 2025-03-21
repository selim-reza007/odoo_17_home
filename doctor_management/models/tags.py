from odoo import api, fields, models, _

class Tags(models.Model):
    _name = "hospital.tags"

    name = fields.Char("Tag name")
    color = fields.Integer("Color")

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = _("%s (copy)", self.name)
        return super(Tags, self).copy(default)

    _sql_constraints = [
        ('unique_tag_name', "unique(name)", "Tag name must be unique!")
    ]