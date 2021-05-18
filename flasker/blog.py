# -*- coding: utf-8 -*-
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .mysql import db
from .models import Post

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    return redirect(url_for('blog.index'))


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):

    return redirect(url_for('blog.index'))