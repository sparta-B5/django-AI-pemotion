# PEMOTION

[스파르타코딩클럽 내일배움캠프 AI 3기] B5팀 두번째 머신러닝 프로젝트  



![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 프로젝트 소개
**PEMOTION**은 B5팀이 `머신러닝`을 기반으로  **반려견 감정일지** 서비스를 구현한 프로젝트입니다.


## 프로젝트 목표
1. Django 배운 내용 기반으로 **필수기능** 완벽하게 복습하기
2. **Git branch**를 이용한 협업 방식 익숙해지기
3. **머신러닝 자체 학습**시키기
4. **Django로 머신러닝 서비스** 만들기
    
## 역할 파트
- **머신러닝** : 이현지, 주세민
    - 머신러닝 학습 : 주세민
    - 머신러닝 로드 : 이현지
- **Django** : 손상훈, 유승주
    - 로그인/회원가입 : 유승주
    - 감정일지 : 손상훈
    
## 와이어프레임
### IA
![IA](https://user-images.githubusercontent.com/113073974/197100929-7cd4d177-f2ba-4cac-a430-dc6c092f679e.PNG)

## DB설계
![DB2](https://user-images.githubusercontent.com/113073974/197100356-827f3c51-de29-4a0f-86bd-78a4761ba0f9.PNG)

## API설계
| 기능 | 메소드 | URL | request | response |
| --- | --- | --- | --- | --- |
| 로그인 | POST | /user/sign-in | {‘username’ : username, ‘pw’ : pw} | redirect(“/”) |
| 회원가입 | POST | /user/sign-up | {’username’:username, ’name’:name, ‘pw’:pw} | redirect(“/user/sign-in”) |
| 로그아웃 | GET | /user/sign-out |  | redirect(“/signin”) |
| 개인 일지 목록 | GET | /diary/{id} | {’username’:usename} | DiaryModel |
| 일지 작성 | POST | /diary | {’content’:content, ‘petimage’:petimage} |  |
| 일지 삭제 | GET | /diary/delete | {'id':id} | redirect(”/diary/<usename>”)|
| 일지 수정 | POST | /diary/update | {’id’:id, 'content':content} |  |

## 사용된 기술
- Git, GitHub
- HTML, CSS, JS, jQuery, Bootstrap
- Python, Django, message_framework, tensorflow, MobileNetV2

## 머신러닝 데이터셋
[강아지 감정예측](https://www.kaggle.com/datasets/devzohaib/dog-emotions-prediction)

## 프로젝트 시연영상
[![B5팀 프로젝트 시연영상](http://img.youtube.com/vi/b66aOiNVh2A/0.jpg)](https://youtu.be/b66aOiNVh2A)

## Contributors
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LeeHyunji">
        <sub><b>이현지</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />
        <sub><b>✈Team Leader</b></sub></a><br />
        <a href="https://github.com/LeeHyunji" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/seoungjuyu">
        <sub><b>유승주</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />
	<sub><b></b></sub></a><br />
        <a href="https://github.com/seoungjuyu" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/son950610">
        <sub><b>손상훈</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />  
	<sub><b></b></sub></a><br />
        <a href="https://github.com/son950610" title="Code">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/jetaime95">
        <sub><b>주세민</b></sub></a><br />
        <sub><b>Developer</b></sub></a><br />    
	<sub><b></b></sub></a><br />
        <a href="https://github.com/jetaime95" title="Code">💻</a>
    </td>
  </tr>
</table>  
