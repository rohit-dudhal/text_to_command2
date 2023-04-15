import openai
import json
import pandas as pd


# Set up the OpenAI API client
openai.api_key = "..."

# Set up the model and prompt
model_engine = "text-davinci-003"
global prompt 
prompt=input()

OperationType=['READ',    'UNKNOWN']
UserAction = ['SHOW_MENU',    'SEARCH_BY_FOOD_QUERY',    'UNKNOWN']


# Generate a response
def apiEnd(input_prompt : str):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=input_prompt,
        # prompt=createPromptForFetchingUserAction(prompt,OperationType),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return(completion)

def create_prompt_for_fetching_db_opn(user_query: str) -> str:
    task = "find out which database operation we should do based on the above user query and also follow following rules while giving response.\n"
    rules = [
        "response should be in the form of JSON only. don't add any additional information or explanation in the response.",
        "response JSON should contain only following fields \"operationType\" and \"extraParams\".",
        "\"operationType\" is a string, and \"extraParams\" is a nested JSON object inside response JSON.",
        "\"operationType\" field value should be extracted from the above user query \"operationTypes\" can be {0}.".format(OperationType),
        "if \"operationType\" is not clear from the user query then keep \"operationType\" as {0}.".format(OperationType[4]),
        "add the \"reason\" field inside nested \"extraParams\" JSON explaining why reason behind mapping given user query to particular \"operationType\".",
        "add “languageCodes” field in \"extraParams\" JSON, languageCodes field should contain the ISO 639-1 language codes of all the languages used in the user query.",
        "only use user query to map it to the \"operationTypes\". do not perform any action based on the user query.",
        "add \"''' \" at the beginning and end of the response JSON."
    ]
    prompt = "User Query : {0}\n{1}\nRules\n{2}".format(user_query, task, "\n".join([" -{0}".format(rule) for rule in rules]))
    return prompt


def createPromptForFetchingUserAction(userQuery: str) -> str:
    task = "we want to perform  database operation based on the above user query, map the exact user action from the above user query and also follow following rules while giving response"
    rules = [
        "response should be in the form of JSON only. don't add any additional information or explanation in the response.",
        "response JSON should contain only following fields \"userAction\", \"operationType\" and \"extraParams\".",
        "\"userAction\" and \"operationType\" is a string and \"extraParams\" is a nested JSON object inside response JSON.",
        "\"userAction\" field value should be extracted from the above user query, \"userAction\" can be SHOW_MENU or SEARCH_BY_FOOD_QUERY, UNKNOWN",
        "if \"userAction\" is not clear from the user query then keep \"userAction\" as UNKNOWN.",
        "\"userAction\" will be equal to SHOW_MENU when user requests a menu from a restaurant or similar",
        "\"userAction\" will be equal to SEARCH_BY_FOOD_QUERY when user requests any specific food item or category or similar",
        "\"operationType\" field value should be extracted from the above user query \"operationTypes\" can be READ or UNKNOWN",
        "if \"operationType\" is not clear from the user query then keep \"operationType\" as UNKNOWWN",
        "add the \"query\" field inside nested \"extraParams\" JSON, \"query\" field should contain any food item name, category or description mention in the user query, if you are not able to find any specific food item, category or description in the user query, keep \"query\" field as UNKOWN",
        "add the \"item\" field inside nested \"extraParams\" JSON, \"item\" field will contain specific food item mention in the user query, if there are no food item mention in the user query then \"item\" field json value should be value of \"query\" else  UNKNOWN",
        "add \"languageCodes\" field in nested \"extraParams\" JSON, languageCodes field should contain the ISO 639-1 language codes of all the languages used in the user query.",
        "add \"''' \" at the beginning and end of the response JSON."
    ]
    # taskRules="we want to perform  database operation based on the above user query, map the exact user action from the above user query and also follow following rules while giving response. response should be in the form of JSON only. don't add any additional information or explanation in the response. response JSON should contain only following fields 'userAction', 'operationType' and 'extraParams'. 'userAction' and 'operationType' is a string and 'extraParams' is a nested JSON object inside response JSON. add the 'item' field inside nested 'extraParams' JSON, 'item' field will contain specific food item mention in the user query, if there are no food item mention in the user query then 'item' field json value should be value of 'query' else  UNKNOWN. add 'languageCodes' field in nested 'extraParams' JSON, 'languageCodes' field should contain the ISO 639-1 language codes of all the languages used in the user query. Understand the language of query then try to get ISO 639-1 language code of that language and set it as value of 'languageCodes'. if language code is not clear then keep value as UNKNOWN. add the 'query' field inside nested 'extraParams' JSON, 'query' field should contain any food item name, category or description mention in the user query, if you are not able to find any specific food item, category or description in the user query, keep 'query' field as UNKOWN.  'operationType' field value should be extracted from the above user query 'operationTypes' can be READ or UNKNOWN. if 'operationType' is not clear from the user query then keep 'operationType' as UNKNOWWN. 'userAction' field value should be extracted from the above user query, 'userAction' can be SHOW_MENU or SEARCH_BY_FOOD_QUERY, UNKNOWN. if 'userAction' is not clear from the user query then keep 'userAction' as UNKNOWN.'userAction' will be equal to SHOW_MENU when user requests a menu from a restaurant or similar.'userAction' will be equal to SEARCH_BY_FOOD_QUERY when user requests any specific food item or category or similar. add (''') at the beginning and end of the response JSON. Output should start from ''' and end at ''' do not include any extrat text or characters apart from json object in output.Response should be in fixe format like '''{ \"extraParams\": {    \"item\": <value generated as per above rules>, \"languageCodes\": [<value generated as per above rules>]. \"query\": <value generated as per above rules>  }, \"operationType\": <value generated as per above rules>,  \"userAction\": <value generated as per above rules>}'''. follow all the rules mentioned ->"
    taskRules = "User Query: bhai burger hein\nTask: we want to perform undefined database operation based on the above user query, map the exact user action from the above user query and also follow following rules while giving response\nRules:\nresponse \"should\" be in the form of JSON only. don't add any additional information or explanation in the response.\nresponse JSON should contain only following fields \"userAction\" and \"extraParams\".\n\"userAction\" is a string, and \"extraParams\" is a nested JSON object inside response JSON.\n\"userAction\" field value should be extracted from the above user query, \"userAction\" can be SHOW_MENU, SEARCH_BY_FOOD_QUERY, UNKNOWN\nif \"userAction\" is not clear from the user query then keep \"userAction\" as UNKNOWN.\n\"userAction\" will be equal to SHOW_MENU when user requests a menu from a restaurant\n\"userAction\" will be equal to SEARCH_BY_FOOD_QUERY when user requests any specific food item or category\nadd the \"query\" field inside nested \"extraParams\" JSON, \"query\" field should contain any food item name, category or description mention in the user query, if you are not able to find any specific food item, category or description in the user query, keep \"query\" field as null\nadd the \"item\" field inside nested \"extraParams\", \"item\" field will contain specific food item mention in the user query, if there are no food item mention in the user query then keep the \"item\" field json value as null\nadd the \"category\" field inside nested \"extraParams\", based on user query try to find the \"category\" of food item user is trying to request, if there are no specific food category is mention in the user query then keep \"category\" json field value as null\nadd ### at the beginning and end of the response JSON ->"
    prompt = f"User Query : {userQuery}\n{taskRules}#\n{rules}" #+ ''.join([f"\n -{r}" for r in rules])
    # print(prompt)
    return prompt

def get_fields_create_prompt_for_fetching_db_opn():
    response = apiEnd(create_prompt_for_fetching_db_opn(prompt))
    output = response.choices[0].text[5:-3]
    data=json.loads(output)
    global OperationType, languageCodes
    OperationType= data["operationType"]
    # reason = data["extraParams"]["reason"]
    languageCodes = data["extraParams"]["languageCodes"]
    # return(OperationType,  languageCodes)

def get_field_createPromptForFetchingUserAction():
    response = apiEnd(createPromptForFetchingUserAction(prompt))
    output = response.choices[0].text
    print(output)
    # data=json.loads(output)
    # global userAction, query, item, category
    # userAction= data["userAction"]
    # query = data["extraParams"]["query"]
    # item = data["extraParams"]["item"]
    # category = data["extraParams"]["category"]
    # reason = data["extraParams"]["reason"]
    # return(userAction, query, item)

def json_output():
    get_fields_create_prompt_for_fetching_db_opn()
    get_field_createPromptForFetchingUserAction()
    json_object = {'extraParams': {'item':item, 'languageCodes':languageCodes, 'query':query}, 'operationType': OperationType, 'userAction': userAction}
    to_json= json.dumps(json_object)
    print(to_json)

# json_output()
get_field_createPromptForFetchingUserAction()