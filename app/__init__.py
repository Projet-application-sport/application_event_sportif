from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/page_principale', methods=['GET'])
    def page_principale():
        return render_template('Page_principale.html')

    @app.route('/page_organiser_un_match', methods=['POST'])
    def page_organiser_un_match():
        return redirect('/create_event')

    @app.route('/page_global_matchs')
    def page_global_matchs():
        return render_template('Global_matchs.html')

    @app.route('/page_mes_matchs')
    def page_mes_matchs():
        return redirect('/liste_event')

    @app.route('/page_consulter')
    def page_consulter():
        return redirect('/consulter_event')

    return app


if __name__ == '__main__':
    app.run(debug=True)

