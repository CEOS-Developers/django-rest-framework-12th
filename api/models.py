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

    def __str__(self):
        return 'id:{} name:{}'.format(str(self.user.id), self.user.username)

#서비스 관련 모델 추가)
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return 'category : {}'.format(self.name)

#서비스 관련 모델1) 상품
#모든 항목 not NULL
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=3)
    customer = models.ManyToManyField(Customer, through='Choice')#through 옵션 사용
    #+적립금..?
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']#오름차순 정렬

    def __str__(self):
        return 'id:{} {}'.format(self.id, self.category)




#서비스 관련 모델 추가) 선택(유저모델과 product를 연결할 mapping table)
class Choice(models.Model):
    #FK
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='choices')
    #FK
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='choices')
    quantity = models.IntegerField()

    class Meta:
        db_table = 'choices'
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        ordering = ['id']

    def __str__(self):
        return 'customer:{} product:{}'.format(self.customer_id, self.product_id)

#서비스 관련 모델2) 주문
class Order(models.Model) :
    order_quantity = models.IntegerField()
    order_addr = models.CharField(max_length=100)
    date_of_order = models.DateTimeField(auto_now=True)#저장될 때마다 자동으로 필드에 현재 시간 설정
    #+FK :고객ID
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

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

    def __str__(self):
        return 'user:{}'.format(self.customer)

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


