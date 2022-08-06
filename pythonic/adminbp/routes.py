from flask import Blueprint
from pythonic import admin, db
from pythonic.models import User, Lesson, Course
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin import AdminIndexView

adminbp = Blueprint("adminbp", __name__)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.id == 1


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return False


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Lesson, db.session))
admin.add_view(MyModelView(Course, db.session))
