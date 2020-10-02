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

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8c157250-f1b4-4c2b-a418-879cc497e262/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083622Z&X-Amz-Expires=86400&X-Amz-Signature=9e8d41c5665da24c32c40fa17a9a4a50dff754935b21fb82e3532fe13e68ae0f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### ORM 적용해보기
1.데이터베이스에 Reviews 모델 객체 3개 생성

순서: User 모델 객체 2개 생성 → Customer 모델 객체 2개 생성 → Product 모델 객체 2개 생성 → Reviews 모델 객체 3개 생성

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/13a9858d-c729-4bda-8bea-cb9021ac2d7c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083306Z&X-Amz-Expires=86400&X-Amz-Signature=f4e78f6d9fd8e485864de8781e520f202b6ee0d2e82ee6c005326b785ff37f08&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

```python
from api.models import Customer
c1 = Customer(user=u1, name = "sewon", addr = "Gwangjin-gu", membership = "Gold")
c2 = Customer(user=u2, name = "Snoopy", addr = "Gwangjin-gu", membership = "Gold")

```

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6c83a6e2-803a-4ada-9ec3-33bde7fbb991/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083416Z&X-Amz-Expires=86400&X-Amz-Signature=0a1c44610433ec7e1b2106704784ce0bea5d0c1aacae1f6642245f0fb046ae5c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)



```python
from api.models import Product
p1 = Product(id="a", type = "shirts", price = 5000, color = "black", size="L")
p2 = Product(id = "aa", type = "shirts" price = 5500, color = "white", size="M")
```

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cb7a5f45-5084-4d95-9b67-c2ac2b7b0198/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083521Z&X-Amz-Expires=86400&X-Amz-Signature=a6f345eb3840d5c80c61c0aeba1fb1c0ce247b69cdc87b094568543fe0e3428d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

```python
from api.models import Reviews
Reviews.objects.create(rating = 4.3, content = "this is good!", customer = c1, product = p1)
Reviews.objects.create(rating = 5.0, content = "this is perfect!", customer = c1, product = p2)
Reviews.objects.create(rating = 5.0, content = "I like it!", customer = c2, product = p2)
```

2.삽입한 객체들 쿼리셋으로 조회하기

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/314a3417-f8fd-4152-9e8e-9b0f1e09fc8f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T084835Z&X-Amz-Expires=86400&X-Amz-Signature=83ae95d0b55210c5ba95fbf3dc0fa411ebae43f8b08c553f017b5413a81c0de0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)



3.filter 함수 사용하기

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c59b7327-18b2-463f-85cb-6414c42e5043/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T085157Z&X-Amz-Expires=86400&X-Amz-Signature=f2976280a6258d91b18dee16f1ba996da8fcec4235a1cc865532ad7822708ce0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22) 



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

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/02ee76ce-4150-45f7-aef8-d430b0b1e13d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201002T113240Z&X-Amz-Expires=86400&X-Amz-Signature=0aa95c75464cb9314fd2df206b8de0f9bdb76dbf666bdd1779842895728040ab&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22) 





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

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e07b9411-eb56-4353-9cd0-5d17ea55e21e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201002T113110Z&X-Amz-Expires=86400&X-Amz-Signature=586b9c064b5899da4f6162539d327ad9c9e511c8a632f8ccc6f81b06db722ecf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22) 

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