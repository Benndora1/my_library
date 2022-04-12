from odoo import models, fields

class LibraryBooks(models.Model):
    _name = 'library.books'

    name = fields.Char('Title',required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner',string='Authors')
