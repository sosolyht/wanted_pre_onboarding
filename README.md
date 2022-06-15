# 원티드 프리온보딩 사전과제
---

### 구현 과제

1. 채용공고 등록
2. 채용공고 수정
3. 채용공고 삭제
4. 채용공고 목록을 가져옵니다.
5. 채용 상세 페이지를 가져옵니다.
6. 사용자는 채용공고에 지원합니다

---


## 데이터베이스 ERD

![image](https://user-images.githubusercontent.com/2377807/173739275-439b861f-1798-4c6a-97c4-570b3c10458c.png)

[ERD 참고 링크](https://dbdiagram.io/d/6295b5f1f040f104c1c8b780)

## 채용공고 등록

### Request

`POST /recruit/`
```
{
    "company_id" : 1,
    "position_id" : 1,
    "compensation" : 900000,
    "content" : "원티드입니다. 우리는 채용중입니다.",
    "stack_id" : 1
}
```

### Response

```
HTTP/1.1 201 Created

{'message' : 'SUCCESS'}
```

## 채용공고 수정

### Request

`PUT /recruit/{공고id}`

ex)</br>
`PUT /recruit/1`
```

{
    "position_id" : 1,
    "compensation" : 520000,
    "content" : "안녕하세요. 원티드입니다. 우리는 채용중입니다.",
    "stack_id" : 1
}
```

### Response

```
HTTP/1.1 200 OK

{'message' : 'SUCCESS'}
```

## 채용공고 삭제

### Request

`DELETE /recruit/{공고id}`

ex)</br>
`DELETE /recruit/1`


### Response

```
HTTP/1.1 200 OK

{"message" : "DELETE_SUCCESS"}
```

## 채용공고 목록을 가져옵니다.

### Request

`GET /recruit/`

### Response

```
HTTP/1.1 200 OK
[
    {
        'id'           : 1
        'company'      : "원티드",
        'country'      : "대한민국",
        'state'        : "서울",
        'position'     : "백엔드 개발자",
        'compensation' : 500000,
        'stack'        : "Spring"
    },
    {
        'id'           : 2
        'company'      : "토스",
        'country'      : "대한민국",
        'state'        : "서울",
        'position'     : "백엔드 개발자",
        'compensation' : 500000,
        'stack'        : "Django"
    },
    {
        'id'           : 3
        'company'      : "네이버",
        'country'      : "대한민국",
        'state'        : "경기",
        'position'     : "백엔드 개발자",
        'compensation' : 500000,
        'stack'        : "Rails"
    },
]
```

## 채용공고 목록을 검색 (4-2)

### Request

`GET /recruit/search?query={stack}`

`GET /recruit/search?query={position}`

ex)

`GET /recruit/search?query=spring`

`GET /recruit/search?query=백엔드`

### Response

```
HTTP/1.1 200 OK
[
    {
        'id'           : 1
        'company'      : "원티드",
        'country'      : "대한민국",
        'state'        : "서울",
        'position'     : "백엔드 개발자",
        'compensation' : 500000,
        'stack'        : "Spring" #spring 검색 결과
    },
    {
        'id'           : 4
        'company'      : "삼성",
        'country'      : "대한민국",
        'state'        : "서울",
        'position'     : "백엔드 개발자",
        'compensation' : 500000,
        'stack'        : "Spring" #spring 검색 결과
    },
    {
        'id'           : 5
        'company'      : "카카오",
        'country'      : "대한민국",
        'state'        : "경기",
        'position'     : "백엔드 개발자",
        'compensation' : 500000,
        'stack'        : "Spring" #spring 검색 결과
    },
]
```

## 채용 상세 페이지를 가져옵니다.

### Request

`GET /recruit/find/{공고id}`

ex)

`GET /recruit/find/1`


### Response

```
HTTP/1.1 200 OK

{
    'id'           : 1,
    'company'      : "원티드",
    'country'      : "대한민국",
    'state'        : "서울",
    'position'     : "백엔드",
    'compensation' : "500000",
    'stack'        : "Django",
    'content'      : "안녕하세요 원티드입니다. 우리는 사람을 뽑고있습니다.",
    'similar'      : [
        2,
        3,
        5
    ]
}
```


## 사용자는 채용공고에 지원합니다

### Request

`POST /mypage/`

```
{
    "user_id" : 1,
    "recruit_id" : 1
}
```

### Response

성공 시
```
HTTP/1.1 201 Created

{
    {'message' : 'SUCCESS'}
}
```

이미 지원을 했을 시
```
HTTP/1.1 400 Bad Request

{
    {'message' : 'ALREADY_APPLIED'}
}
```