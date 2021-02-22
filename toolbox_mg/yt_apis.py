import requests

def fetch_vid_id(results, id, key=None):
    """
    Fetch vid IDs according to category.
    """
    url = "https://youtube.googleapis.com/youtube/v3/search/?"
    ids = []
    
    for i in np.linspace(0,50000,1001, dtype="int"):
        params= {
                 "part":"snippet",     
                 'resultsPerPage': results, 
                 "maxResults": results, 
                 "relevanceLanguage":"en",
                 "videoCategoryId":id,
                 "order":"viewCount",
                 "type":"video",
    #              "forMine":True,
                 "start-index":i+1
                }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return 'Error'
        data = response.json()
        for video in data["items"]:
            ids.append(video["id"]['videoId'])
    return ids