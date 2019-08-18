from demo.views.index import ix
from flask import views, render_template, request, jsonify, current_app


class IndexView(views.MethodView):
    def get(self):
        return render_template("index.html")


ix.add_url_rule("/index", None, IndexView.as_view("index"))
