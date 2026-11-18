from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'ADMIN')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, db_index=True)
    google_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Super Admin'
        COACH = 'COACH', 'Coach'
        ATHLETE = 'ATHLETE', 'Athlete'
        
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ATHLETE)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"

class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coach_profile')
    coach_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30, blank=True)
    sport_category = models.CharField(max_length=100)
    qualification = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(default=1)
    profile_picture = models.URLField(blank=True, null=True)

class AthleteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='athlete_profile')
    athlete_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    sport = models.CharField(max_length=100, db_index=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    assigned_coach = models.ForeignKey(CoachProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_athletes')
    profile_picture = models.URLField(blank=True, null=True)
    learning_progress_pct = models.PositiveIntegerField(default=0)

class Substance(models.Model):
    class WadaCategory(models.TextChoices):
        S0 = 'S0', 'Non-approved substances'
        S1 = 'S1', 'Anabolic agents'
        S2 = 'S2', 'Peptide hormones, growth factors'
        S3 = 'S3', 'Beta-2 agonists'
        S4 = 'S4', 'Hormone and metabolic modulators'
        S5 = 'S5', 'Diuretics and masking agents'
        S6 = 'S6', 'Stimulants'
        S7 = 'S7', 'Narcotics'
        S8 = 'S8', 'Cannabinoids'
        S9 = 'S9', 'Glucocorticoids'
        P1 = 'P1', 'Beta-blockers'
        M = 'M', 'Prohibited methods'

    class Status(models.TextChoices):
        PROHIBITED = 'Prohibited', 'Prohibited'
        PERMITTED = 'Permitted', 'Permitted'
        CONDITIONAL = 'Conditional', 'Conditional'
        TUE_REQUIRED = 'TUE Required', 'TUE Required'

    substance_name = models.CharField(max_length=255, db_index=True)
    scientific_name = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=WadaCategory.choices)
    introduction = models.TextField()
    what_it_is = models.TextField()
    medical_applications = models.TextField()
    anti_doping_relevance = models.TextField()
    wada_classification = models.CharField(max_length=100)
    prohibited_status = models.CharField(max_length=50, choices=Status.choices)
    competition_status = models.CharField(max_length=100) # In-competition / Out-of-competition
    health_risks = models.TextField()
    side_effects = models.TextField()
    athlete_awareness = models.TextField()
    tue_information = models.TextField()
    official_reference_link = models.URLField(max_length=500)
    last_verified_date = models.DateField()

class StudyMaterial(models.Model):
    class MaterialType(models.TextChoices):
        PDF = 'PDF', 'PDF Document'
        AUDIO = 'AUDIO', 'Audio Guide'
        VIDEO = 'VIDEO', 'YouTube Video'

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    material_type = models.CharField(max_length=10, choices=MaterialType.choices)
    file_or_url = models.URLField(max_length=500)
    description = models.TextField()
    language = models.CharField(max_length=10, default='en')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1) # 'A', 'B', 'C', 'D'
    explanation = models.TextField()

class QuizAttempt(models.Model):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    total_questions = models.PositiveIntegerField()
    passed = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(auto_now_add=True)