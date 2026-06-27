from pathlib import Path

from flask import Flask

from academic_hub.views.dashboard_view import DashboardView

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

dashboard_view = DashboardView()


@app.route("/")
def home():
    return dashboard_view.dashboard()


if __name__ == "__main__":
    app.run(debug=True)
