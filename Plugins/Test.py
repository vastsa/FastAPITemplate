from fastapi import APIRouter

view = APIRouter()


@view.get('/lan')
async def lan():
    return {'status': True, 'code': 200, 'message': 'hello i am lan'}
