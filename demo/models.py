from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, TEXT, DATETIME
from sqlalchemy.orm import relationship
from demo import db
import datetime


class ArticleInfo(db.Model):
    __tablename__ = "blog_article_info"
    id = Column(Integer, primary_key=True, comment="主键字段")
    title = Column(VARCHAR(256), nullable=False, comment="文章标题")
    summary = Column(VARCHAR(1024), nullable=False, comment="文章简介")
    traffic = Column(Integer, nullable=False, comment="文章的浏览量", default=0)
    create_time = Column(DATETIME, nullable=False, comment="创建时间", default=datetime.datetime.now())
    modified_time = Column(
        DATETIME,
        nullable=False,
        comment="上次修改时间",
        onupdate=datetime.datetime.now()
    )


class ArticleDetail(db.Model):
    __tablename__ = "blog_article_detail"
    id = Column(Integer, primary_key=True, comment="主键")
    content = Column(TEXT, nullable=False, comment="文章内容")
    article_id = Column(Integer, ForeignKey("blog_article_info.id"), nullable=False)
    article = relationship("ArticleInfo", backref="detail")


class ViewCount(db.Model):
    __tablename__ = "sys_view"
    id = Column(Integer, primary_key=True, comment="主键")
    ip = Column(VARCHAR(20), nullable=False, comment="访问者IP")
    create_time = Column(DATETIME, nullable=False, comment="访问时间", default=datetime.datetime.now())


class UserInfo(db.Model):
    __tablename__ = "sys_user"
    id = Column(Integer, primary_key=True, comment="主键")
    username = Column(VARCHAR(20), unique=True, nullable=False, comment="用户名")
    password = Column(VARCHAR(32), nullable=False, comment="密码")


class UserAuth(db.Model):
    __tablename__ = "sys_auth"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("sys_user.id"), nullable=False)
    token = Column(VARCHAR(50), nullable=False, comment="用户token")
