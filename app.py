import flask
import pickle
import numpy as np
import pandas as pd
import gensim
import sklearn
import utils

with open(f'model/finalized_model.pkl', 'rb') as f:
    model = pickle.load(f)


with open(f'model/vectorizer.pkl','rb') as v:
    vectorizer = pickle.load(v)

df_topic_keywords=pd.read_csv('templates/topic_keywords.csv')


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        
        symptom1 = flask.request.form['symptom1']
        symptom2 = flask.request.form['symptom2']
        symptom3 = flask.request.form['symptom3']
    

        input_variables=[symptom1,symptom2,symptom3]
        p = ','.join([str(elem) for elem in input_variables]) 
        listToStr=[p]




        # Define function to predict topic for a given text document

        def predict_topic(text):  
           global sent_to_words
           global lemmatization
        
           # Step 1: Clean with simple_preprocess
           mytext_2 = list(utils.sent_to_words(text))
           
           
           # Step 2: Lemmatize
           mytext_3 = utils.lemmatization(mytext_2, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
           
           
           # Step 3: Vectorize transform
           mytext_4 = vectorizer.transform(mytext_3)
           
           
           # Step 4: LDA Transform
           topic_probability_scores = model.transform(mytext_4)
        
           topic = df_topic_keywords.iloc[np.argmax(topic_probability_scores), 1:14].values.tolist()
           

           # Step 5: Infer Topic
           infer_topic = df_topic_keywords.iloc[np.argmax(topic_probability_scores), -1]
           

           #topic_guess = df_topic_keywords.iloc[np.argmax(topic_probability_scores), Topics]
           return infer_topic, topic, topic_probability_scores
       



       # Predict the topic
       

       #mytext = ["ambivalent feelings towards infant,anemia,anticipatory anxiety,avoidance of situations,compulsive behavior,difficulty bonding with infant,excitability,flashbacks,flight of ideas,grandiose thinking,irritability,jumpiness (startling easily),mood changes,nightmares,panic attacks,persistent worrying,repetitive behavior"]
        

        infer_topic, topic, prob_scores = predict_topic(text = listToStr)
        
        return flask.render_template('main.html',
                                     original_input={'Symptom1': symptom1,
                                                     'Symptom2': symptom2,
                                                     'Symptom3': symptom3},
                                     result=infer_topic,
                                     )


if __name__ == '__main__':
    app.run()
