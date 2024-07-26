from argparse import ArgumentParser, Namespace

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import TeamModel


def get_arguments() -> Namespace:
    parser = ArgumentParser(description='Generic API')
    parser.add_argument('-d', '--develop', action='store_true', default=False,
                        dest='develop', required=False,
                        help='Local development')
    return parser.parse_args()


def start() -> FastAPI | None:
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

    @api.post('/team/create', status_code=status.HTTP_201_CREATED)
    def create_team(team: TeamModel):
        print(team)

    return api


if __name__ == '__main__':
    arguments = get_arguments()
    uvicorn.run('main:start',
                factory=True,
                host='0.0.0.0',
                port=8001,
                reload=arguments.develop)
