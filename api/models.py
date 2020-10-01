from django.db import models
from django.contrib.auth.models import User

#유저 모델
#새로운 모델 생성해서 기존의 User Model과 OneToOne 으로 연결하는 방식
class Customer(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)#User모델의 user_id 필드를 PK로 지정
    addr = models.CharField(max_length=100)#추후에 확실히 찾아볼 것!
    membership = models.CharField(max_length=10)
    #적립금..?
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


#서비스 관련 모델1) 상품
#모든 항목 not NULL
class Product(models.Model) :
    #자동 증가하는 ID일 경우 별도 생성X
    #choices 생성 for type
    TYPE_CHOICES = [
        ('OUTERWEAR', 'OUTERWEAR'),
        ('TOPS', 'TOPS'),
        ('SHIRTS', 'SHIRTS'),
        ('BOTTOMS', 'BOTTOMS'),
        ('SKIRTS', 'SKIRTS'),
        ('DRESSES', 'DRESSES'),
        ('BAGS', 'BAGS'),
    ]
    type = models.CharField(max_length=9, choices=TYPE_CHOICES, default='TOPS')
    price = models.IntegerField()
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=3)
    customer = models.ManyToManyField(Customer, through='Order')#through 옵션 사용
    #+적립금..?
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


#서비스 관련 모델2) 주문 (유저모델과 1을 연결할 mapping table), N:M 관계 아직 못함..
class Order(models.Model) :
    order_quantity = models.IntegerField()
    order_addr = models.CharField(max_length=100)
    date_of_order = models.DateTimeField(auto_now=True)#저장될 때마다 자동으로 필드에 현재 시간 설정
    #+FK :고객ID
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    #+FK :상품ID
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

#서비스 관련 모델3) 장바구니 (유저 모델과 1:1 관계)
class Cart(models.Model) :
    total_quantity = models.IntegerField()
    total_payment = models.IntegerField()
    #+고객ID: PK 이자 FK
    customer = models.OneToOneField(Customer, primary_key=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

#서비스 관련 모델4) 상품 리뷰
class Reviews(models.Model) :
    rating = models.DecimalField(max_digits=2, decimal_places=1)#숫자 최대 자릿수 2, 소수점 1자리 수까지 저장
    content = models.TextField()
    #+고객ID : FK
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='reviews')
    #+상품ID : FK
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


#서비스 관련 모델5) 상품 문의
class Question(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_of_question = models.DateTimeField(auto_now=True)
    #+고객ID: FK
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='questions')
    #+상품ID: FK
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='questions')

    class Meta:
        db_table = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


#서비스 관련 모델6) 문의 답변
class Answer(models.Model) :
    writer = models.CharField(max_length=5, default="Admin")#default 값 = 관리자로 지정
    date_of_ans = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    #+QuestionID : FK
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    class Meta:
        db_table = 'answers'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'