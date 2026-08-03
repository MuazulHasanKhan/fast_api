# This module handles JWT authentication for the FastAPI application.   
# This is he security engine of the application. It provides functions to generate and verify JWT tokens, as well as a dependency to get the current user from the token.
# This is essential for:
# Creating acess tokens after succesful user autentication
# Verifying and decoding access token