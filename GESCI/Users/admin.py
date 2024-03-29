from django.contrib import admin
from .models import Student, User, Teacher, Course, Attendance, Teaching, Groups, StudentGroup, Post, TeacherCourse
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','username', 'email', 'date_of_birth', 'first_name', 'last_name',  'is_admin', 'is_student', 'is_teacher')
    list_filter = ('is_admin', 'is_student', 'is_teacher')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser','is_active' ,'is_admin', 'is_student', 'is_teacher')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2','is_admin','is_student', 'is_teacher')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
class TeacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attendance, AttendanceAdmin)

class TeachingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teaching, TeachingAdmin)


class GroupsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Groups, GroupsAdmin)

class StudentGroupsAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentGroup, StudentGroupsAdmin)

class PostsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostsAdmin)

class TeacherCoursesAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherCourse, TeacherCoursesAdmin)



