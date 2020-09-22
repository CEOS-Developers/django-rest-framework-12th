from django.db import models


# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님) # 서비스모델?? 유저모델???

class Contact(models.Model):  # 소속
    email=models.CharField(max_length=40,null=True)
    phone_number=models.CharField(max_length=20,null=True)
    office_number=models.CharField(max_length=20,null=True)


class Student(models.Model):  # 학생
    student_name = models.CharField(max_length=20,blank=True)  # 학생이름
    student_department = models.CharField(max_length=20,null=True,blank=True)  # 소속(전공), 모든 학생 전공이 1개임을 가정
    student_id = models.CharField(max_length=20)  # 학번 != Pk
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE,null=True)


class Professor(models.Model):  # 교수
    professor_name = models.CharField(max_length=20,blank=True)  # 교수 이름
    professor_department = models.CharField(max_length=20,null=True,blank=True)  # 교수 소속
    professor_major = models.CharField(max_length=40)  # 교수 세부 전공
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True)


class Course(models.Model):  # 강좌
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)  # 교수
    course_name = models.CharField(max_length=40)  # 강좌명
    course_id = models.CharField(max_length=20)  # 학수번호!=PK
    classroom = models.CharField(max_length=20)  # 강의실


class Enrollment(models.Model):  # 수강신청, 관계테이블
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # 학생
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # 강좌