from __future__ import print_function
import requests
import json
import logging
import os

slack_token = os.environ.get('slack_token')

def add_reaction(react_type, group, ts):
    ts_asc = str(ts)
    reaction_endpoint = ("https://slack.com/api/reactions.add?token=%s&name=%s&timestamp=%s&channel=%s&pretty=1" % (slack_token, react_type, ts_asc, group)).encode('utf-8')
    print(reaction_endpoint)
    resp = requests.post(reaction_endpoint)
    print("Reaction Post OK: " + str(resp.json()))
    logging.info("Resp status: " + str(resp.status_code))
    logging.info("REACTION POST URL: " + str(reaction_endpoint))
    
def react_all(group, ts, count):
    all_reacts = ['neckbeard', 'rotatingparrot', 'tacoparrot', 'bananaparrot','ryangoslingparrot','trollface','upvotepartyparrot','parrot','finnadie','shuffleparrot','slowparrot','goberserk','ultrafastparrot','christmasparrot','shipit','parrotcop','thumbsupparrot','thumbsup_all','beryl',
    'dreidelparrot',
    'moonwalkingparrot',
    'blondesassyparrot',
    'parrotwave5',
    'parrotdad',
    'slack_call',
    'shipitparrot',
    'bluescluesparrot',
    'parrotbeer',
    'rage2',
    'pride',
    'parrotwave4',
    'middleparrot',
    'evilparrot',
    'boredparrot',
    'rage4',
    'fastparrot',
    'twinsparrot',
    'aussiecongaparrot',
    'shufflepartyparrot',
    'cubimal_chick',
    'slomoparrot',
    'invisibleparrot',
    'sassyparrot',
    'loveparrot',
    'skiparrot',
    'metal',
    'octocat',
    'dusty_stick',
    'sadparrot',
    'aussieparrot',
    'rightparrot',
    'matrixparrot',
    'parrotmustache',
    'troll',
    'congaparrot',
    'rage1',
    'parrotsleep',
    'prideparrot',
    'black_square',
    'scienceparrot',
    'fiestaparrot',
    'angelparrot',
    'hamburgerparrot',
    'bowtie',
    'parrotwave1',
    'papalparrot',
    'fidgetparrot',
    'suspect',
    'shufflefurtherparrot',
    'tripletsparrot',
    'stableparrot',
    'halalparrot',
    'beretparrot',
    'harrypotterparrot',
    'stalkerparrot',
    'pizzaparrot',
    'simple_smile',
    'reversecongaparrot',
    'parrotwave2',
    'gentlemanparrot',
    'feelsgood',
    'congapartyparrot',
    'angryparrot',
    'glitch_crab',
    'godmode',
    'hurtrealbad',
    'explodyparrot',
    'piggy',
    'oldtimeyparrot',
    'parrotwave6',
    'margaritaparrot',
    'rage3',
    'fu',
    'aussiereversecongaparrot',
    'squirrel',
    'rube',
    'parrotwave7',
    'confusedparrot',
    'abhi',
    'slack',
    'parrotwave3',
    'dealwithitparrot',
    'gothparrot',
    'ice-cream-parrot',
    'partyparrot',
    'darkbeerparrot',
    'coffeeparrot',
    'white_square',
    'luckyparrot',
    'chillparrot']
    for i in range(0,count):
        add_reaction(all_reacts[i], group, ts)

def get_ts(group_id):
    message_endpoint = "https://slack.com/api/conversations.history?token={0}&channel={1}&count=2&pretty=1".format(slack_token, group_id)
    resp = requests.get(message_endpoint)
    resp_json = resp.json()
    ts = resp_json['messages'][0]['ts']
    text = resp_json['messages'][0]['text']
    return ts
        
def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    count = event["count"]
    group = event["group"]
    ts = get_ts(group)
    react_all(group, ts, count)
    return "Done"
