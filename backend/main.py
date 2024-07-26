from argparse import ArgumentParser, Namespace

import uvicorn
from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from auth import Auth
from models import TeamModel


def get_arguments() -> Namespace:
    parser = ArgumentParser(description='Kickerliga-Bochum API')
    parser.add_argument('-d', '--develop', action='store_true', default=False,
                        dest='develop', required=False,
                        help='Local development')
    parser.add_argument('-p', '--password', dest='password', required=True,
                        help='Password')
    return parser.parse_args()


def start() -> FastAPI | None:
    args = get_arguments()
    docs_url = '/docs' if args.develop else None
    secret: str = args.password

    api = FastAPI(root_path='/kickerliga-bochum/api',
                  docs_url=docs_url, redoc_url=None)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    @api.post('/team/create', status_code=status.HTTP_201_CREATED,
              dependencies=[Depends(Auth(secret))])
    def create_team(team: TeamModel):
        print(team)

    @api.get('/key', status_code=status.HTTP_200_OK,
             dependencies=[Depends(Auth(secret).login)])
    def get_key(team: str) -> str:
        payload = {
            'team': team
            # add exp if wanted
        }
        return Auth(secret).create_key(payload)

    return api


if __name__ == '__main__':
    arguments = get_arguments()
    uvicorn.run('main:start',
                factory=True,
                host='0.0.0.0',
                port=8001,
                reload=arguments.develop)
