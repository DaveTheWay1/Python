from flask_app import app
from flask_app.models import user
from flask import request, redirect
from flask_app.models.user import User

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # * we redirect to the template with the form.
        return redirect('/')
    # * if no errors are found; continue as normal
    user.User.save(request.form)
    return redirect('/dashboard')