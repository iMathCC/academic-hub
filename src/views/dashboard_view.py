from flask import render_template

class DashboardView:
    def dashboard(self):
        return render_template("dashboard.html")

