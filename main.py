from fastapi import FastAPI, Depends
from models import CalcGetRequest, CalcPostRequest, CalcResponce
app = FastAPI()

@app.get('/calc', summary='Calc get method', response_model=CalcResponce)
async def get_calc(query: CalcGetRequest = Depends(CalcGetRequest)):
    params = query.dict()
    responce = {'result': '', 'operation': ''}
    responce['result'] = eval(params['expression'])
    responce['operation'] = params['expression']
    return responce


@app.post('/calc', summary='Calc post method', response_model=CalcResponce)
async def post_calc(body: CalcPostRequest):
    params = body.dict()
    responce = {'result': '', 'operation': ''}

    if params['operator'] == '*':
        responce['result'] = params['first'] * params['last']
        responce['operation'] = str(params['first']) + '*' + str(params['last'])

    elif params['operator'] == '/':
        responce['result'] = params['first'] / params['last']
        responce['operation'] = str(params['first']) + '/' + str(params['last'])

    elif params['operator'] == '+':
        responce['result'] = params['first'] + params['last']
        responce['operation'] = str(params['first']) + '+' + str(params['last'])

    elif params['operator'] == '-':
        responce['result'] = params['first'] - params['last']
        responce['operation'] = str(params['first']) + '-' + str(params['last'])

    return responce
