from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

class StudentManager(BaseUserManager):
    use_in_migrations = True

    def student_user(self, code, name, password=None):
        if not code:
            raise ValueError('must have user id')
        if not name:
            raise ValueError('must have user name')

        user = self.model(code=code, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

class ProfessorManager(BaseUserManager):
    use_in_migrations = True

    def create_professor_user(self, code, name, password=None):
        if not code:
            raise ValueError('must have user id')
        if not name:
            raise ValueError('must have user name')

        user = self.model(code=code, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Contact(models.Model):  # 소속
    email = models.EmailField(max_length=40, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    office_number = models.CharField(max_length=20, null=True, blank=True)


class Student(models.Model):  # 학생
    objects = StudentManager()
    student_code = models.CharField(max_length=20,verbose_name='학번')
    student_name = models.CharField(max_length=20,verbose_name='이름')
    student_department = models.CharField(max_length=20, null=True, blank=True,verbose_name='소속')
    contact = models.OneToOneField(Contact, on_delete=models.SET_NULL, null=True, blank=True)


class Professor(models.Model):  # 교수
    objects = ProfessorManager()
    professor_code = models.CharField(max_length=20,verbose_name='교수번호')
    professor_name = models.CharField(max_length=20,verbose_name='이름')
    professor_department = models.CharField(max_length=20, null=True, blank=True,verbose_name='소속')
    professor_major = models.CharField(max_length=40, null=True, blank=True)  # 교수 세부 전공
    contact = models.OneToOneField(Contact, on_delete=models.SET_NULL, null=True, blank=True)


class Course(models.Model):  # 강좌
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    course_name = models.CharField(max_length=40)
    course_code = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20, null=True)


class Enrollment(models.Model):  # 수강신청, 관계테이블
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
