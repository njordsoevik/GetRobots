def checkRobots(page,agent='*'):
    result = requests.get(page)
    if str(result) =='<Response [403]>':
        return 'HTTP 403: Bots not allowed to read robots.txt'
    elif str(result) =='<Response [400]>':
        return 'HTTP 400: Bad response by server, will not process request'
    
    print('Able to retrieve robots.txt, results below: \n')
    
    agent_index='User-agent: {}'.format(agent)
    capture = result.text[result.text.find(agent_index):]
    full_list = capture.split('\n')
    print('{}\n'.format(full_list[0]))
    disallow_list = []
    
    for disallow in full_list[1:]:
    
        if disallow != '' and disallow[0:8]=='Disallow':
            print(disallow)
        else: 
            break

