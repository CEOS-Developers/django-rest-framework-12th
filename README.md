# django-rest-framework-12th
## 2주차 스터디

### 서비스 설명
쇼핑몰 서비스 만들기

### 모델 설명
*유저 모델: 

Customer: 고객(회원과 관련된 정보 포함)  / PK: User 모델의 id(IntegerField)

*서비스 관련 모델:  

Product: 상품/ PK: id(CharField)

Order: 주문/ PK: order_number(IntegerField)

Cart: 장바구니/ PK: Customer의 id

Reviews: 리뷰/ PK: id(BigAutoField)

QnA: 문의/ PK: id(BigAutoField)

Answer: 답변 / PK: id(BigAutoField)

<모델 간 관계>

![modeling](./img/modeling.jpg)

### ORM 적용해보기
1.데이터베이스에 Reviews 모델 객체 3개 생성

순서: User 모델 객체 2개 생성 → Customer 모델 객체 2개 생성 → Product 모델 객체 2개 생성 → Reviews 모델 객체 3개 생성

![create_customers](./img/create_customers.jpg)

```python
from api.models import Customer
c1 = Customer(user=u1, name = "sewon", addr = "Gwangjin-gu", membership = "Gold")
c2 = Customer(user=u2, name = "Snoopy", addr = "Gwangjin-gu", membership = "Gold")

```

![create_product](./img/create_product.jpg)

```python
from api.models import Product
p1 = Product(id="a", type = "shirts", price = 5000, color = "black", size="L")
p2 = Product(id = "aa", type = "shirts" price = 5500, color = "white", size="M")
```

![create_reivews](./img/create_reviews.jpg)

```python
from api.models import Reviews
Reviews.objects.create(rating = 4.3, content = "this is good!", customer = c1, product = p1)
Reviews.objects.create(rating = 5.0, content = "this is perfect!", customer = c1, product = p2)
Reviews.objects.create(rating = 5.0, content = "I like it!", customer = c2, product = p2)
```

2.삽입한 객체들 쿼리셋으로 조회하기

![using_queryset](./img/using_queryset.jpg)

Reviews 모델의 객체들을 rating(평점)을 기준으로 내림차순으로 조회함

3.filter 함수 사용하기

![using_filterfunc](./img/using_filterfunc.jpg)



### 간단한 회고 

구상한 서비스에 필요한 모델들을 직접 구상하는 것이 낯설었고, 모델 관의 정확한 관계, PK와 FK를 정확히 지정하는 것이 중요하다는 것을 깨달았다. 



## 3주차 스터디

### 모델 선택 및 데이터 삽입

```python
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
        return self.user.username #관리자에서 객체 생성시 username으로 보임


#서비스 관련 모델1) 상품
#모든 항목 not NULL
class Product(models.Model) :
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
    customer = models.ManyToManyField(Customer, through='Choice')#through 옵션 사용
    #+적립금..?
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

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
        return str(self.id)
        
```

![choices_objects](./img/choices_objects.jpg)

![choices_objects_adminpage](./img/choices_objects_adminpage.jpg)



### 모든 list를 가져오는 API

->모든 Choice 객체 가져오는 API 요청 결과

URL: api/choices/

Method: GET

```json
[
    {
        "id": 1,
        "quantity": 1,
        "customer": 2,
        "product": 1
    },
    {
        "id": 2,
        "quantity": 1,
        "customer": 3,
        "product": 2
    },
    {
        "id": 3,
        "quantity": 2,
        "customer": 4,
        "product": 1
    },
    {
        "id": 4,
        "quantity": 2,
        "customer": 2,
        "product": 2
    }
]
```

->모든 User 객체 가져오는 API 요청 결과

URL: api/users/

Method: GET

```json
[
    {
        "id": 1,
        "username": "admin",
        "customer": null
    },
    {
        "id": 2,
        "username": "RYAN",
        "customer": {
            "addr": "서울시 광진구",
            "membership": "purple"
        }
    },
    {
        "id": 3,
        "username": "APEACH",
        "customer": {
            "addr": "서울시 서대문구",
            "membership": "purple"
        }
    },
    {
        "id": 4,
        "username": "MUZI",
        "customer": {
            "addr": "서울시 광진구",
            "membership": "purple"
        }
    }
]
```

->모든 Product 객체 가져오는 API 요청 결과

URL: api/products/

Method: GET

```json
[
    {
        "id": 1,
        "type": "TOPS",
        "price": 5000,
        "color": "black",
        "size": "M"
    },
    {
        "id": 2,
        "type": "SHIRTS",
        "price": 6000,
        "color": "blue",
        "size": "L"
    }
]
```



### 특정한 데이터를 가져오는 API

->3번째 choice를 가져오는 API 요청 결과

URL: api/choices/3/

Method: GET

```JSON
{
    "id": 3,
    "quantity": 2,
    "customer": 4,
    "product": 1
}
```



### 새로운 데이터를 create하도록 요청하는 API

->Choice 객체를 추가하는 API 요청 결과

URL: api/choices/

Method: POST

Body: {"quantity": 3, "customer":2, "product":2}

```json
{
    "id": 5,
    "quantity": 3,
    "customer": 2,
    "product": 2
}
```



### (선택) 특정 데이터를 삭제 또는 업데이트하는 API

->id 값이 5인 Choice 객체 제거하는 API 요청 결과

URL: api/choices/5/

Method: DELETE

![delete_api](./img/delete_api.jpg)



### 공부한 내용 정리

*URL과 URI의 차이점

URL: 인터넷 상의 자원 위치를 나타냄

URI: 인터넷 상의 자원을 식별하기 위한 문자열의 구성

*Serializer 

사용 이유: JSON으로 데이터를 보내야하는 RESTful API를 위해 Queryset을 Nested한 JSON으로 매핑하는 과정이 필요한데, Serializer 그 역할을 수행함

(기존 장고는 장고 ORM의 Queryset은 장고 template으로 넘겨지며 HTML로 렌더링되어 Response로 보내짐)

*APIView

CBV(클래스 기반 뷰) 중 하나여서 하나의 URL에 대해 처리 가능

ex)

/post/에 대한 CBV -> get: 목록, post: 새로운 객체 생성

/post/< int : pk >/ 에 대한 CBV -> get: pk번 객체 내용, put: pk번 객체 수정, delete: pk번 객체 삭제

*ModelAdmin

특정 모델 클래스를 admin에 등록하여 사용 가능

->방법: admin.ModelAdmin 상속, decorator 형태로 등록(@admin.register(Post))

->옵션: list_display(Admin 목록에 보여질 필드 목록)

### 간단한 회고

Serializer나 APIView을 사용하는 이유에 대해 알아가며 순차적으로 진행할 수 있었다.