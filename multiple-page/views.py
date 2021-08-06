
import flask
import numpy as np

@blueprint.route("/", methods=["GET"])
def render_homepage():
    return flask.render_template("homepage.html")