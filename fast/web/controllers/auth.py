from fastapi import Request, Form

from fast.core import validations
from fast.infra.database import get_session
from fast.models.user import User
from fast.repositories.users import UserRepository
from fast.web import main

repository = UserRepository(get_session)


def register_view(request: Request):
    context = {}
    context['request'] = request
    context['title'] = 'Crie Sua Conta'
    context['errors'] = {}
    context['user'] = {}
    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def register_handle(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_pass: str = Form(...),
):
    global repository

    context = {}
    context['request'] = request
    context['errors'] = {}
    context['user'] = {}

    if request.method == 'POST':
        context['user'] = {
            'name': name,
            'email': email,
            'password': '',
            'confirm_pass': '',
        }
        is_valid, errors = validations.user_data(
            name, email, password, confirm_pass
        )
        context['errors'] = errors
        user = repository.find_by_email(email)

        if isinstance(user, User) and user.email == email:
            context['errors']['email'] = f'O email "{email}" já esta em uso'
        elif is_valid:
            repository.save(name, email, password)
            context['user'] = {}
            context['created'] = 'Usuário registrado com sucesso!'

    return main.templates.TemplateResponse(
        'pages/auth/register.html', context=context
    )


def login_handle(
    request: Request, email: str | None = '', password: str | None = ''
):
    context = {}
    context['request'] = request
    context['title'] = 'Entrar'
    context['user'] = {}

    if request.method == 'POST':
        print(f'login data: {email} | {password}')

    return main.templates.TemplateResponse(
        'pages/auth/login.html', context=context
    )
