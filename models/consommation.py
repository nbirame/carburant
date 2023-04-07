from odoo import models, fields, api


class Consommation(models.Model):
    _name = "carburant.consommation"
    _description = "Consommation Carburant"

    nb_littre = fields.Float(string="Nombre de littres")
    prix = fields.Float(string="Prix")
    total = fields.Float(string="Total", compute="_compute_total", store=True)
    vehicule_id = fields.Many2one("fleet.vehicle", string="Véhicule")
    carte_id = fields.Many2one("carburant.cartecarburant", string="Carte")

    @api.depends("nb_littre", "prix")
    def _compute_total(self):
        for record in self:
            if record.nb_littre or record.prix:
                record.total = record.nb_littre * record.prix

















