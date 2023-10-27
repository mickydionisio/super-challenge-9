from django.db import models

class DocumentVerificationType(models.Model):
    document_verification_type_id = models.AutoField(primary_key=True)
    first_name = models.BooleanField()
    middle_name = models.BooleanField()
    last_name = models.BooleanField()
    street_address = models.BooleanField()
    city = models.BooleanField()
    state = models.BooleanField()
    postal_code = models.BooleanField()
    country = models.BooleanField()
    unique_document_id = models.BooleanField()
    date_issued = models.BooleanField()
    expiration_date = models.BooleanField()

class Citizen(models.Model):
    citizen_id = models.AutoField(primary_key=True)
    social_security_id = models.CharField(max_length=255)
    current_name = models.ForeignKey('NameParts', on_delete=models.SET_NULL, null=True)
    citizenship_status = models.CharField(max_length=255)
    employment_status = models.CharField(max_length=255)

class NameHistory(models.Model):
    name_id = models.AutoField(primary_key=True)
    name_parts_id = models.ForeignKey('NameParts', on_delete=models.SET_NULL, null=True)
    citizen_id = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    change_reason = models.CharField(max_length=255)

class NameParts(models.Model):
    name_parts_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255)

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    citizen_id = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    is_current = models.BooleanField()

class AddressParts(models.Model):
    address_parts_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class EmploymentHistory(models.Model):
    employment_history_id = models.AutoField(primary_key=True)
    citizen_id = models.ForeignKey('Citizen', on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_verified = models.BooleanField()
    verification_date = models.DateField()
    verification_method = models.CharField(max_length=255)

class DocumentVerification(models.Model):
    document_verification_id = models.AutoField(primary_key=True)
    document_verification_type_id = models.ForeignKey('DocumentVerificationType', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    processed_date = models.DateField()
    status = models.CharField(max_length=255)
    document_url = models.URLField()

class VerificationRequest(models.Model):
    verification_request_id = models.AutoField(primary_key=True)
    request_date = models.DateField()
    verified_date = models.DateField()
    status = models.CharField(max_length=255)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

class BiometricVerification(models.Model):
    biometric_verification_id = models.AutoField(primary_key=True)
    metadata = models.JSONField()
    processed_date = models.DateField()
    status = models.CharField(max_length=255)
    document_url = models.URLField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()

class DriversLicense(DocumentVerificationType):
    pass

class Naturalization(DocumentVerificationType):
    pass

class Passport(DocumentVerificationType):
    pass
