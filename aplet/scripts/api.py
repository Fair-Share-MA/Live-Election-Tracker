import json

api_key = 'oq5o5bimci19os5zh3yiacswjy'
office_ids = ','.join(['G', 'I', 'A', 'L', 'R', 'T'])
election_date = '2022-09-06'
request = f'https://api.ap.org/v3/elections/{election_date}?apikey={api_key}&statePostal=MA&format=json&resultstype=l&level=RU&officeID={office_ids}'

def get_races(session):
    response = session.get(request)
    return json.loads(response.text)["races"]
