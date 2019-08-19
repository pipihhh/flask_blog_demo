from demo.views.index import ix
from flask import views, render_template, request, jsonify, current_app
from demo import models
from demo.utils.response import Response


class IndexView(views.MethodView):
    def get(self):
        return render_template("index.html")


class BlogView(views.MethodView):
    def get(self):
        ret_list = models.ArticleInfo.query.all()
        response = Response()
        if ret_list:
            msg = []
            for ret in ret_list:
                msg.append({
                    "id": ret.id,
                    "title": ret.title,
                    "avatar": ret.avatar,
                    "summary": ret.summary,
                    "traffic": ret.traffic,
                    "create_time": ret.create_time
                })
            response.msg = msg
            return jsonify(response.data)
        response.code = 201
        response.error = "暂无数据"
        return jsonify(response.data)


ix.add_url_rule("/index", None, IndexView.as_view("index"))
ix.add_url_rule("/blog", None, BlogView.as_view("blog"))
