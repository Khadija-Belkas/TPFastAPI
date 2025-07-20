import hashlib 
import random 
import string 

def generate_password(): 
    """Génère un mot de passe aléatoire""" 
    return ''.join(random.choices(string.ascii_letters + string.digits, 
k=8)) 
def hash_password(password): 
    """Hash un mot de passe""" 
    return hashlib.sha256(password.encode()).hexdigest() 
def create_user(username, email): 
    """Crée un utilisateur avec un mot de passe généré et hashé""" 
    password = generate_password() 
    hashed_password = hash_password(password)
    user = { 
            'username': username, 
            'email': email, 
            'password': hashed_password, 
            'raw_password': password  # Pour les tests uniquement 
             } 
    return user 
def validate_user(user_data): 
    """Valide qu'un utilisateur a les champs requis""" 
    required_fields = ['username', 'email', 'password'] 
    return all(field in user_data for field in required_fields) 