import pandas as pd
from flask import Flask, jsonify, request
import json
from src.recommendation import RecommendCandidate

app = Flask(__name__)

@app.route("/recommend", methods=['GET', 'POST'])
def recommend():
    project = json.loads(request.args.get('project'))
    scores = recommender.find_candidates(project)
    return jsonify(candidates[scores.index(max(scores))])


if __name__ == "__main__":
    # read data
    df_candidates = pd.read_csv('./data/candidates.csv')
    nullornone = lambda x: x if not pd.isnull(x) else None
    # convert dataframe to a list of dict
    candidates = []
    for _, row in df_candidates.iterrows():
        candidates.append({
            'id': row['id'],
            'name': row['name'],
            'description': row['description']
        })
    recommender = RecommendCandidate(candidates)
    app.run(port='8888', debug=True)
