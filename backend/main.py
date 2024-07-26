'''Start up script for the Backend'''
from argparse import ArgumentParser, Namespace

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


def get_arguments() -> Namespace:
    '''
    Parses arguments.

        Returns:
            args: given arguments
    '''
    parser = ArgumentParser(description='Generic API')
    parser.add_argument('-d', '--develop', action='store_true', default=False,
                        dest='develop', required=False,
                        help='Local development')
    return parser.parse_args()


def start() -> FastAPI | None:
    '''
    Starts the API. Callable by uvicorn, gunicorn etc.

        Returns:
            api (FastAPI): api containing all routes and specs
    '''
    args = get_arguments()
    docs_url = '/docs' if args.develop else None

    api = FastAPI(docs_url=docs_url, redoc_url=None)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    class Team(BaseModel):
        '''WIP'''
        key: str
        mk1: str
        mk2: str
        players: list[str]

    @api.post('/team/create', status_code=status.HTTP_201_CREATED)
    def create_team(team: Team):
        print(team)

    return api


if __name__ == '__main__':
    arguments = get_arguments()
    uvicorn.run('main:start',
                factory=True,
                host='0.0.0.0',
                port=8001,
                reload=arguments.develop)
