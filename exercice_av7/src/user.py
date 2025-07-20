def get_user_from_db(username):
    """Fetch user data from DB"""
    raise NotImplementedError()

def check_password(password, hashed_password):
    """Compare password to hash"""
    raise NotImplementedError()

def log_login_attempt(username, success):
    """Log login result"""
    print(f"[LOG] Login attempt: {username} - {'SUCCESS' if success else 'FAILURE'}")

def login_user(username, password):
    """Handles user login logic"""
    try:
        user = get_user_from_db(username)
    except Exception:
        return {"status": "error", "reason": "db_error"}

    if not user:
        log_login_attempt(username, False)
        return {"status": "fail", "reason": "user_not_found"}

    if not user.get("active", False):
        log_login_attempt(username, False)
        return {"status": "fail", "reason": "user_inactive"}

    if not check_password(password, user["password_hash"]):
        log_login_attempt(username, False)
        return {"status": "fail", "reason": "wrong_password"}

    log_login_attempt(username, True)
    return {"status": "success", "user_id": user["id"]}
def get_user_data(username, password):
    result = login_user(username, password)
    return result