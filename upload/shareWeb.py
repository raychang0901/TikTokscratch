import shareWebAnalysis
def response(flow):
    if 'aweme/v1/user/following/list' in flow.request.url:
           shareWebAnalysis.anls(flow.response.text)