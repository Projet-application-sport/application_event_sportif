from flask import Flask, request, jsonify, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/chat', methods=['GET'])
    def get_chat():
        return render_template("Page_principale.html")

    return app
 
