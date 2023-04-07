from odoo import fields, api, models


class Chargement(models.Model):
    _name = "carburant.chargement"
    _description = "Chargement Carte"

    date = fields.Date(string="Date")
    nb_littre = fields.Float(string="Nombre de littres")
    prix = fields.Float(string="Prix littre")
    montant = fields.Float(string="Montant Total", compute="_compute_motant", store = True)
    carte_id = fields.Many2one("carburant.cartecarburant", string="Carte")

    def total_littres_consommer(self):
        consommation = self.env["carburant.chargement"].sudo().search([('carte_id', '=', 'self.carte_id.id')])
        for cons in consommation:
            nombre_littre_consommer = cons.carte_id.nb_littre
        return nombre_littre_consommer

    def name_get(self):
        charge = []
        for record in self:
            rec_name = "%s"%(record.date)
            charge.append((record.id, rec_name))
        return charge

    @api.depends("nb_littre", "prix")
    def _compute_motant(self):
        for record in self:
            if record.nb_littre and record.prix:
                record.montant = record.prix * record.nb_littre