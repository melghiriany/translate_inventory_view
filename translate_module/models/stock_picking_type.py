from odoo import models, fields
from googletrans import Translator


class CustomStockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    name = fields.Char(string="Operation Type", compute="_compute_translate_name")

    def _compute_translate_name(self):
        translator = Translator()
        for rec in self:
            translated_name = ""
            if rec.code == 'outgoing':
                translated_name = translator.translate("Delivery Orders", dest=self.env.user.lang[:2], src="en").text
            elif rec.code == 'incoming':
                translated_name = translator.translate("Reception", dest=self.env.user.lang[:2], src="en").text
            else:
                translated_name = translator.translate("Internal Transfers", dest=self.env.user.lang[:2], src="en").text
            rec.name = translated_name
