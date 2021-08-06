
import flask
import numpy as np

blueprint = flask.Blueprint("ui", __name__)

@blueprint.route("/", methods=["GET"])
def render_homepage():
    return flask.render_template("homepage.html")