#!/usr/bin/env python3

def validate_password(password):
        
        if any(char.isupper() for char in password) and len(password) >=8 and any(char.isupper() for char in password) and any(digit.isdigit() for digit in password) and not " " in password:
            
            return True
        return False