import pandas as pd
import requests
import json
from src.recommendation import RecommendCandidate

if __name__ == "__main__":
    # read datq
    df_projects = pd.read_csv('./data/projects.csv')

    nullornone = lambda x: x if not pd.isnull(x) else ''
    projects = []
    for _, row in df_projects.iterrows():
        projects.append({
            'id': row['id'],
            'name': row['name'],
            'title': nullornone(row['title']),
            'requirement': nullornone(row['requirement'])
        })

    url = 'http://localhost:8888/recommend'
    for project in projects:
        payload = {'project': json.dumps(project)}
        response = requests.post(url, params=payload)
        print(response.text)
