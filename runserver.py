# -*- coding: utf-8 -*-

from conure.application import app


if(__name__ == "__main__"):
    app.debug = app.config["DEBUG_MODE"]
    app.run()
