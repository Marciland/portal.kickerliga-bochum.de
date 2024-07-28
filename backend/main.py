from argparse import ArgumentParser, Namespace
from datetime import datetime, timedelta
from os import getcwd, makedirs, path
from uuid import uuid4

import uvicorn
from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import TeamModel
from modules import Auth, dump_team_to_file


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
    auth = Auth(args.password)
    csv_path = path.join(getcwd(), 'csv')
    makedirs(csv_path, exist_ok=True)

    api = FastAPI(root_path='/kickerliga-bochum/api',
                  docs_url=docs_url, redoc_url=None)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    @api.post('/team/create', status_code=status.HTTP_201_CREATED)
    def create_team(team: TeamModel, team_name: str = Depends(auth)):
        team.name = team_name
        file_path = path.join(csv_path, str(uuid4()) + '.csv')
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            dump_team_to_file(team, file)
        # construct E-Mail
        # send email + csv as attachement
        # cleanup

    @api.get('/key', status_code=status.HTTP_200_OK,
             dependencies=[Depends(auth.login)])
    def get_key(team: str) -> str:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=100),
            'team': team
        }
        return auth.create_key(payload)

    return api


if __name__ == '__main__':
    arguments = get_arguments()
    uvicorn.run('main:start',
                factory=True,
                host='0.0.0.0',
                port=8001,
                reload=arguments.develop)
