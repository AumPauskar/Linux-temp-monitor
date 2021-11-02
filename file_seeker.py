def GetRefresh():
    import json
    with open('config.json', 'r') as file:
        data = json.load(file)
        return(data['refresh-tag'])
    
def GetEntry():
    import json
    with open('config.json', 'r') as file:
        data = json.load(file)
        return(data['entry-tag'])