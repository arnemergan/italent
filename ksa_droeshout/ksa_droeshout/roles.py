def superuser_only(request):
    if not request.user.is_superuser:
        return False
    return True