from flask import Flask, render_template, request
from form import ContactForm
from elasticsearch import Elasticsearch

app = Flask(__name__)

app.secret_key = "nihaoma"

@app.route('/')
@app.route('/form', methods = ["GET", "POST"])
def form():
    form = ContactForm()
    
    if request.method == "POST":
        print "POST used."
        es = Elasticsearch()
        
        res = es.search(index='va', 
                        doc_type="plan",
                        body = {
                                    'query': {
                                        'match_all': {}
                                }
                }
                       )
        print "Got " + str(res['hits']['total']) + " hits"
        return render_template('resultsrefined.html', res=res['hits']['hits'])  
    elif request.method == "GET":
#         return render_template("basicform.html")
#         return "Hello world."
        print "Calling render_template"
        return render_template('form.html', form=form)
    
if __name__=="__main__":
    app.run(debug=True)