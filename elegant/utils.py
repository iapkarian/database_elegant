from django.contrib.auth.decorators import user_passes_test


def check_permission(perm, login_url='/'):
    def has_permission(u):
        if u and u.is_authenticated():
            if u.has_perm(perm):
                return True
        return False

    return user_passes_test(has_permission, login_url=login_url)
