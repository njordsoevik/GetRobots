import sys
import requests

def checkRobots(args):
    # Input of sys.argv is a list, need to check length for inputs
    if len(args)==1:
        print('Please provide URL and/or agent name')
        return 1
    elif len(args)==2:
        page='https://www.'+args[1]+'.com/robots.txt'
        agent='*'
    elif len(args)==3:
        page='https://www.'+args[1]+'.com/robots.txt'
        agent=args[2]
    else:
        print('Too many arguments provided')
        return 1
        
    # Perform get on HTTP server
    result = requests.get(page)
    if str(result) =='<Response [403]>':
        print('\nHTTP 403: Bots not allowed to read robots.txt of site {}'.format(page))
        return 1
    elif str(result) =='<Response [400]>':
        print('\nHTTP 400: Bad response by HTTP server, {} will not process request'.format(page))
        return 1
        
    
    print('\nAble to retrieve robots.txt from {}, results below: \n'.format(page))
    
    # Capture strings starting from agent index
    agent_string='user-agent: {}'.format(agent).lower()
    agent_index=result.text.lower().find(agent_string)
    capture = result.text[agent_index:]
    
    # Split capture on new lines
    full_list = capture.split('\n')
    
    # Continue if our index was correct
    if full_list[0][0:12].lower()=='user-agent: ':
        print('{}\n'.format(full_list[0]))
        rule_list = []
        output_count=0
        current_agent=True
        
        # For each in list
        for disallow in full_list[1:]:
            # If string matches a rule and we are under current agent
            if (disallow[0:8].lower() == 'disallow' or disallow[0:5].lower() == 'allow') and current_agent==True:
                print(disallow)
                rule_list.append(disallow)
                output_count+=1
            # Blank space, skip
            elif disallow=='':
                pass
            # If our string matches our agent again, set as current agent
            elif disallow.lower().rstrip()=='user-agent: {}'.format(agent).lower():
                current_agent=True
            # If not under current agent
            else:
                current_agent=False
        if output_count==0:
            print('No rules for user-agent: {}'.format(agent))
        else:
            return rule_list
    else:
        print('Could not find user-agent {} in robots.txt'.format(agent))
            
checkRobots(sys.argv)
