from demo.views.login import lg
from flask import views


class UserView(views.MethodView):
    def get(self):
        return "login"


lg.add_url_rule("/user", None, UserView.as_view("user"))
