import pytest
from cores.authentication.serializers.login import LoginSerializer

@pytest.mark.django_db
def test_login_serializer():
    # Simulate a login attempt with valid credentials
    valid_credentials = {'username': 'admin', 'password': 'password'}
    valid_serializer = LoginSerializer(data=valid_credentials)
    assert valid_serializer.is_valid()  # Check if the serializer is valid
    validated_data = valid_serializer.validated_data
    assert 'user' in validated_data  # Check if the user key is present in the validated data

    # Simulate a login attempt with invalid credentials
    invalid_credentials = {'username': 'invalid_user', 'password': 'invalid_password'}
    invalid_serializer = LoginSerializer(data=invalid_credentials)
    assert not invalid_serializer.is_valid()  # Check if the serializer is not valid for invalid credentials
    errors = invalid_serializer.errors
    assert 'non_field_errors' in errors  # Check if there are non-field errors indicating invalid credentials
