import uuid
from demo.views.login import lg
from demo import models
from demo import db
from flask import views, render_template, request, jsonify, current_app
import hashlib


class UserView(views.MethodView):
    def get(self):
        return render_template("login.html")

    def post(self):
        username = request.form.get("username")
        pwd = request.form.get("pwd")
        md5 = hashlib.md5(bytes(current_app.config["SALT"], encoding=current_app.config["CHARSET"]))
        md5.update(bytes(pwd, encoding=current_app.config["CHARSET"]))
        ret = models.UserInfo.query.filter_by(username=username, password=md5.hexdigest()).first()
        if ret:
            token = str(uuid.uuid4())
            auth = models.UserAuth.query.filter_by(user_id=ret.id).first()
            auth = models.UserAuth(user_id=ret.id, token=token) if auth is None else auth
            db.session.add(auth)
            db.session.commit()
            return jsonify({
                "code": 200,
                "msg": {
                    "href": "/index",
                    "token": str(uuid.uuid4())
                }
            })
        return jsonify({
            "code": 201,
            "error": "用户名或密码错误"
        })


lg.add_url_rule("/user", None, UserView.as_view("user"))
