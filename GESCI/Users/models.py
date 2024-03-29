from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import FileField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default='1900-01-01')
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Groups(models.Model):
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student"
    )
    def __str__(self):
        return self.user.username 

class Teacher(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher"
    )

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
class StudentGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student12")
    group = models.ForeignKey(Groups, on_delete=CASCADE, related_name="group12")
    class Meta:
        unique_together=[['student', 'group']]

    def __str__(self):
        return self.student.user.username + '-' + self.group.number
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student1")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course1")
    group = models.ForeignKey(Groups, on_delete=CASCADE, related_name="group1")
    class Meta:
        unique_together=[['student', 'course', 'group']]

    def __str__(self):
        return self.student.user.username + '-' + self.course.name + '-' + self.group.number

class Post(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher2")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course2")
    group = models.ForeignKey(Groups, on_delete=CASCADE, related_name="group2")
    text = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.teacher.user.username    + '-' + self.course.name + '-' + self.group.number + '-' + str(self.id)
class TeacherCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher0")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course0")
    class Meta:
        unique_together=[['teacher', 'course']]

    def __str__(self):
        return self.teacher.user.username + '-' + self.course.name 

class Teaching(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    group = models.ForeignKey(Groups, on_delete=CASCADE, related_name="group5")
    class Meta:
        unique_together=[['teacher', 'course', 'group']]

    def __str__(self):
        return self.teacher.user.username + '-' + self.course.name + '-' + str(self.group)


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.is_teacher == True :
        Teacher.objects.create(user=instance)
    elif created and instance.is_student == True :
        Student.objects.create(user=instance)
