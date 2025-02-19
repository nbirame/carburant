from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Carte(models.Model):
    _name = "carburant.cartecarburant"
    _description = "Carte de Carburant"
    _inherit = ['mail.thread.cc',
                'mail.thread.blacklist',
                'mail.thread.phone',
                'mail.activity.mixin',
                'utm.mixin',
                'format.address.mixin',
                ]

    libelle = fields.Char(string="Libellé")
    detenteur = fields.Many2one("hr.employee", string="Détenteur carte", store=True)
    numero = fields.Integer(string="Numéro")
    type_carte = fields.Selection([('Personnelle', 'Personnelle'), ('Mission', 'Mission'), ], 'Type de Carte',
                                  default="Personnelle")
    fourniseur = fields.Many2one("res.partner", string="Fournisseur", store=True, check_company=True, index=True, tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    quantite = fields.Float(string="Quantité Totale", compute='_compute_carburant_quantite', store = True)
    nb_littre = fields.Float(string="Nombre de littre consommées", compute="_compute_carburant_nb_littre", store=True)
    restant_littre = fields.Float(string="Quantité actuelle", compute='_compute_carburant_restant_littre', store = True)
    montant = fields.Float(string="Montant" , compute="_compute_carburant_montant", store = True)
    montant_cons = fields.Float(string="Montant consommé", compute="_compute_carburant_montant_consommer", store = True)
    chargement_ids = fields.One2many("carburant.chargement", "carte_id", string="Chargement")
    consommation_ids = fields.One2many("carburant.consommation", "carte_id", string="Consommation")
    _rec_name = 'libelle'

    @api.depends("chargement_ids")
    def _compute_carburant_quantite(self):
        quantity = []
        for record in self:
            #  quantité pour 100km c'est 15 littre de carburant
            for chage in record.chargement_ids:
                nombre_littre = chage.nb_littre
                quantity.append(nombre_littre)
                record.quantite = sum(quantity)

    # methode qui permet de calculer le nombre de littre consommer
    @api.depends("consommation_ids")
    def _compute_carburant_nb_littre(self):
        somme = []
        for record in self:
            for consma in record.consommation_ids:
                somme.append(consma.nb_littre)
                record.nb_littre = sum(somme)
        # carte = self.env["carburant.cartecarburant"].sudo().search([])
        # for carburant in carte:
        #     carburant_consommer = carburant.nb_littre
        # for record in self:
        #     if record.consommation_ids:
        #         for cons in record.consommation_ids[-1]:
        #             record.nb_littre = cons.delegation_id.carburant + carburant_consommer

    # méthode qui permet de calculer le nombre de littre restant dans la carte de carburant en fonction du nombre
    # total de littre et du nombre de littre consommer
    @api.depends("quantite", "nb_littre")
    def _compute_carburant_restant_littre(self):
        for record in self:
            record.restant_littre = record.quantite - record.nb_littre

    # @api.constrains("restant_littre")
    # def _check_restant_littre(self):
    #     for record in self:
    #         if record.restant_littre <= 0:
    #             raise ValidationError(_('Veillez charger la carte'))

    # méthode qui permet de calculer la cout du chargement
    @api.depends("chargement_ids")
    def _compute_carburant_montant(self):
        for record in self:
            for charge in record.chargement_ids:
                record.montant = charge.montant

    @api.depends("consommation_ids")
    def _compute_carburant_montant_consommer(self):
        somme = []
        for record in self:
            for consma in record.consommation_ids:
                somme.append(consma.total)
                record.montant_cons = sum(somme)

    def return_action_to_open(self):
        """ This opens the xml view specified in xml_id for the current vehicle """
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')
        if xml_id:

            res = self.env['ir.actions.act_window']._for_xml_id('carburant.%s' % xml_id)
            res.update(
                context=dict(self.env.context, default_employee_id=self.id, group_by=False),
                domain=[('employee_id', '=', self.id)]
            )
            return res
        return False
