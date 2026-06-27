from flask import render_template
from academic_hub.services.dashboard_service import DashboardService

class DashboardView:

    def __init__(self):
        self.service = DashboardService()

    def dashboard(self):
        dashboard = self.service.carregar_dashboard()

        return render_template("dashboard.html",
                               dashboard=dashboard)

