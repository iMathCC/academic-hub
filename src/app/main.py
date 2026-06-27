from flask import Flask
from views.dashboard_view import DashboardView

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

dashboard_view = DashboardView()

@app.route("/")
def home():
    return dashboard_view.dashboard()


if __name__ == "__main__":
    app.run(
        debug=True
    )
