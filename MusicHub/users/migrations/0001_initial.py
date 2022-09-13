from django.conf import settings
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z][a-zA-Z\\-\\s]*",
                                message="Name not valid: name must start and ends with letter and can contain only ' ' or '-' special characters ",
                            )
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z][a-zA-Z\\-\\s]*",
                                message="Name not valid: name must start and ends with letter and can contain only ' ' or '-' special characters ",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=256,
                        unique=True,
                        validators=[
                            django.core.validators.EmailValidator(
                                code="Invalid email",
                                message="Please provide valid email address",
                            )
                        ],
                        verbose_name="email address",
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Password must be beetween 8-64 characters and can include Upper/lower cases, digits and special characters",
                                regex="^.{8,64}$",
                            )
                        ],
                    ),
                ),
                (
                    "profile_avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="users/avatar",
                        validators=[
                            django.core.validators.validate_image_file_extension
                        ],
                        verbose_name="Avatar",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "followers",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
