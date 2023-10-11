# Copyright 2015 ABF OSIELL <https://osiell.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Audit Log",
    "version": "14.0.2.0.1",
    "author": "ABF OSIELL,Odoo Community Association (O"
              "CA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/server-tools",
    "category": "Tools",
    "depends": ["base",
                'openeducat_activity',
                'openeducat_admission',
                'openeducat_assignment',
                'openeducat_attendance',
                'openeducat_classroom',
                'openeducat_core',
                'openeducat_erp',
                'openeducat_exam',
                'openeducat_facility',
                'openeducat_fees',
                'openeducat_library',
                'openeducat_parent',
                'openeducat_timetable',
                'web_openeducat',
                ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron.xml",
        "views/auditlog_view.xml",
        "views/http_session_view.xml",
        "views/http_request_view.xml",
    ],
    "application": True,
    "installable": True,
}
