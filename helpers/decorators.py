from django.contrib.auth.decorators import user_passes_test

def check_user(user):
    """Returns true if the user is not authenticated, false otherwise"""
    return not user.is_authenticated

user_logout_required = user_passes_test(check_user, '/', None)

def auth_user_should_not_access(viewfunc):
    """Returns a decorator restricting logged in user"""
    return user_logout_required(viewfunc)
