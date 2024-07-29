from argparse import ArgumentParser, Namespace
from datetime import datetime, timedelta
from os import getcwd, makedirs, path, remove
from uuid import uuid4

import uvicorn
from fastapi import Depends, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import EmailCreds, TeamModel
from modules import Auth, MailClient, dump_team_to_file

CSV_PATH = path.join(getcwd(), 'csv')
TEMPLATE_PATH = path.join(getcwd(), 'templates')


def get_arguments() -> Namespace:
    parser = ArgumentParser(description='Kickerliga-Bochum API')
    parser.add_argument('-d', '--develop', action='store_true', default=False,
                        dest='develop', required=False,
                        help='Local development')
    parser.add_argument('-p', '--password', dest='password', required=True,
                        help='Password for key generation.')
    parser.add_argument('-mu', '--mail-user', dest='mail_user', required=True,
                        help='Mail user, used as sender.')
    parser.add_argument('-mp', '--mail-password', dest='mail_pass', required=True,
                        help='Mail password.')
    return parser.parse_args()


def start() -> FastAPI | None:
    args = get_arguments()
    docs_url = '/docs' if args.develop else None
    auth = Auth(args.password)
    mail = MailClient(EmailCreds(email=args.mail_user,
                                 password=args.mail_pass))

    with open(path.join(TEMPLATE_PATH, 'new_team_email.html'),
              'r', encoding='utf-8') as html_file:
        new_team_email = html_file.read()

    makedirs(CSV_PATH, exist_ok=True)

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
        team.check_validity()  # this would raise
        csv_file_path = path.join(CSV_PATH, str(uuid4()) + '.csv')
        try:
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
                dump_team_to_file(team, csv_file)
            formatted_email = new_team_email % (team_name,
                                                '<br />'.join(team.get_full_team()))
            email = mail.create_email(content=formatted_email,
                                      subject=f'Neue Meldung: {team_name}')
            email.attach_file(csv_file_path, team.name + '.csv')
            mail.send_email(email,  # TODO use kickerliga after testing
                            to_address='marcel.marciland@gmail.com')
        finally:
            remove(csv_file_path)

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
