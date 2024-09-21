from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = "res.users"

    # Records come from user_ids field of helpdesk.ticket.team.
    helpdesk_team_ids = fields.Many2many(
        comodel_name="helpdesk.ticket.team",
        relation="helpdesk_ticket_team_res_users_rel",
        column1="res_users_id",
        column2="helpdesk_ticket_team_id",
    )

    @api.model
    def create(self, vals):
        # Create the user using the standard method
        user = super(ResUsers, self).create(vals)
        # Check if the partner_id is created and set
        if user.partner_id:
            # Set the tech_name field to "Technician"
            user.partner_id.tech_name = 'Technician'
        return user
