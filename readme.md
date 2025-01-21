# 🌱 JungleHub

[![Watch the video](https://github.com/user-attachments/assets/0bd7fdab-e87d-4e7b-842b-c04f2ad3f87e)](https://drive.google.com/file/d/1hirCdfClBl7u8Jx9jEuWAWmjWNXqcIAL/view?usp=sharing)

- 배포 URL: http://junglehub.net/main

## 프로젝트 소개

- JungleHub는 개발자들의 커밋 현황을 시각적으로 표현하는 플랫폼입니다.
- 사용자는 GitHub OAuth로 로그인하여 간편하게 참여할 수 있으며, 사용자의 커밋 비율에 따라 퍼즐 조각이 사라지면서 숨겨진 사진이 점차 드러납니다.
- 모든 유저가 모두 커밋을 완료하면 사진이 완전히 공개되며, 이를 통해 팀의 헌신과 협업을 시각적으로 보여줍니다.
- 사진이 완전히 공개될 때, 팀원들은 목표를 달성의 성취감을 느낄 수 있습니다.
- 이 서비스는 팀워크를 강화하고, 기여도를 명확하게 시각화하여 동기부여를 높이는 데 중점을 둡니다.
- Krafton Jungle 7기 부트캠프 과정중 Week0 3박4일 미니 프로젝트입니다.

## 팀원 구성

| 김희원                                                                     | 박자은                                                           | 정재명                                                          |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- |
| ![Profile](https://avatars.githubusercontent.com/u/65596779?v=4) | ![박자은](https://avatars.githubusercontent.com/u/105774739?v=4) | ![정재명](https://avatars.githubusercontent.com/u/44443949?v=4) |
| [@heewon1104](https://github.com/heewon1104)                               | [@ddoavoca](https://github.com/ddoavoca)                         | [@jjm159](https://github.com/jjm159)                            |

## 역할

### 김희원

- 메인페이지, 회원가입, 프로필 페이지 디자인 및 구현
- JS Animation 구현
- Issue 정리
- 코드 리펙토링
- Readme 작성

### 박자은

- 백엔드 프로필 페이지 구현
- JWT 구현

### 정재명

- 웹페이지 배포
- DB 설계
- 배치 시스템 구축
- 백엔드 메인페이지, 로그인 구현

## 개발 환경

- Frontend: HTML, CSS, JavaScript, Tailwind, JS animation
- Backend : Janja2, Flask
- API : github oauth Api, IntersectionObserver Api
- DB: MongoDB
- 버전관리: Notion, Github
- 배포환경: EC2
- 디자인: Figma

## 채택한 개발 기술과 브랜치 전략

### 기술 스택

- Html, JavaScript, CSS
  - 기본적인 Vanilla JS로 웹사이트를 구현하며 웹사이트의 근간이 되는 언어들을 익혔습니다
- Tailwind
  - Bootstrap은 미리 정의된 스타일과 클래스가 많아 CSS 파일의 양이 많아지는 단점이 있습니다
  - Styled Components는 반응형 유틸리티를 자체적으로 제공하지 않습니다
  - Tailwind는 자체적으로 반응형 유틸리티를 제공하여, HTML 태그 내에서 자유롭게 스타일을 변형할 수 있어 CSS 파일의 양을 줄일 수 있습니다.
  - 페이지와 컴포넌트가 얼마 없는 간단한 프로젝트를 구현하기에 좋다 판단하여 Tailwind를 사용 하였습니다.
- Python Flask
  - Flask를 사용하여 Model-View-controller를 분리하여 구현하였습니다
- MonGoDB
  - repository 디렉토리에 MongoDB 관련 파일들을 위치 시켰습니다.
  - 데이터를 저장, 조회, 수정, 삭제하는 기능을 하며 정보들을 데이터베이스에 저장하거나 불러옵니다.
- EC2
  - EC2를 이용하여 배포를 하였으며, 자동으로 동작하는 배치 시스템을 사용 하였습니다.
  - 배치 시스템을 통해
    - 30분 간격으로 GitHub API를 통해 모든 유저의 오늘 커밋 수를 가져오며,
    - 누적 커밋 수를 업데이트하고,
    - 모든 유저의 커밋 정보를 데이터베이스에 저장하고, 게시판 블록 리스트를 랜덤으로 열리도록 관리합니다.
- Figma
  - Figma를 통해 크래프톤 정글 홈페이지를 참고하여 디자인 하였습니다.

### 브랜치 전략

- Git-flow 전략을 기반으로 main 브랜치와 feature 보조 브랜치를 이용하여 코드를 관리 하였습니다.
- 급한 버그가 나면 Hotfix 브랜치를 생성, 고친 후 Main에 바로 PR 하였습니다.
- 기능 단위로 나눠 feature 브랜치를 생성하였고, 구현을 마치면 Main에 PR 하였습니다.
- main 브랜치에 기능 구현을 마친 feature 브랜치를 PR 하였고, 배포 단계에서 해당 브랜치를 사용 하였습니다.

## 주요 로직 - Github OAuth 로그인

<img width="726" alt="KakaoTalk_Photo_2024-09-03-00-44-02" src="https://github.com/user-attachments/assets/249f7087-7182-4ba1-86b8-ea0e9b860b4c">

1. Frontend에서 Github Login URL에 API 요청
2. Github에서 Frontend에 code 정보를 URL에 담아 전달
3. /login으로 Backend에 API 요청
4. Backend에서 Github에 client_id, client_secret, code를 body에 담아 전달
5. Github에서 Backend에 Access Token 전달
6. Backend에서 Frontend에 JWT Token 전달

## 디렉토리 구조

```
├── readme.md
├── batch
│    └── ommitCountScheduler.py
├── configuration
│    ├── config.py
│    └── config.xml
├── controller
│    ├── login.py
│    ├── main.py
│    ├── signup.py
│    └── user_profile.py
├── model
│    ├── boardBlockList.py
│    ├── dayTotalCommitCount.py
│    └── userCommitCount.py
├── module
│    ├── githubApi.py
│    ├── InMemoryCache.py
│    └── scheduler.py
├── repository
│    ├── boardBlockListRepository.py
│    ├── dayTotalCommitCountRepository.py
│    ├── repositoryConfig.py
│    ├── repositoryProfile.py
│    └── userCommitCountRepository.py
├── static
│    ├── fonts
│    │     └── Orbit-Regular.ttf
│    ├── images
│    │     ├── Logo.png
│    │     └── PuzzleImage1.png
│    └── js
│          ├── main.js
│          ├── signup.js
│          └── utils.js
├── templates
│    ├── footer.html
│    ├── header.html
│    ├── loginedHeader.html
│    ├── main.html
│    ├── profile.html
│    ├── signup.html
│    └── signupFail.html
├── .gitignore
├── app.py
└── requirements.txt
```

## 프로젝트 기능

### 1-1. 메인페이지 - 메인 배너

- 간단한 프로젝트 소개 문구를 JS 애니메이션을 통해 페이지에서 해당 컴포넌트가 보일시 재생 되도록 구현 하였습니다.
  <img width="1489" alt="스크린샷 2024-10-07 오후 7 25 07" src="https://github.com/user-attachments/assets/ed9c0485-a811-4ed9-a804-64179009763b">

### 1-2. 메인페이지 - 누적 커밋수

- 그래프톤 정글 7기 시작 날짜인 2024/09/02 부터 현재까지의 누적 커밋수입니다.
  <img width="1471" alt="스크린샷 2024-10-07 오후 7 25 17" src="https://github.com/user-attachments/assets/6c87cbde-2622-4f08-bbdb-eb85697a211c">

### 1-3. 메인페이지 - 퍼즐 보드

- 가입 인원들의 커밋수에 따라 %를 계산, 커밋수가 많을수록 퍼즐이 없어지고, 거려진 뒤의 그림이 나타납니다
  <img width="827" alt="스크린샷 2024-10-07 오후 7 26 13" src="https://github.com/user-attachments/assets/6541e1e4-06fc-4be3-b625-a4b0b906e87d">

### 1-4. 메인페이지 - 사용자 리스트

- 가입한 사용자들의 당일 커밋 개수를 내림차순으로 보여줍니다
  <img width="1457" alt="스크린샷 2024-10-07 오후 7 26 21" src="https://github.com/user-attachments/assets/2ebc14fb-15e1-4f44-a0b8-426d03d3bb85">

### 2-1. 회원가입 - 깃허브 연동

- 깃허브 정보를 입력하고 연동합니다
  <img width="631" alt="스크린샷 2024-10-07 오후 8 04 50" src="https://github.com/user-attachments/assets/a8955377-2074-4e68-8e46-8e63e2c23e9f">

### 2-2. 회원가입 - 회원 정보 입력

- 사용자의 상세 정보들을 입력합니다
  <img width="751" alt="스크린샷 2024-10-07 오후 8 02 25" src="https://github.com/user-attachments/assets/7e8f6b9f-e987-4927-8eed-b77935e2c994">

### 3. 개인 프로필

- 회원가입시 등록한 본인의 프로필을 확인 가능합니다.
  <img width="1507" alt="스크린샷 2024-10-07 오후 7 26 38" src="https://github.com/user-attachments/assets/db384278-d021-4c47-ad5e-596277e9b87f">

## 트러블 슈팅

- 개발 도중 만났던 문제 상황들을 github의 issues를 활용하여 기록하였습니다.
- https://github.com/JungleHub/JungleHub/issues

## 프로젝트를 진행하며 배운점, 느낀점

### 김희원

- React를 사용하면서, 기본기가 부족하단 느낌을 종종 받았었는데, 이번에 Vanilla JS로 간단한 웹사이트를 만들며 기본기를 다시 익힐 수 있었습니다
- 이번 SSR 방식으로 처음 구현하며 CSR, SSR 방식의 차이점을 알 수 있었습니다
- Github Oauth에 Redirect URL을 보내고, Jwt 토큰을 받아 로컬 스토리지에서 관리하는 방법을 익힐 수 있었습니다
- 간단한 JS Animation을 인터넷 예제를 보며 참고해 구현하고, IntersectionObserver Api을 이용해 화면에 포커싱이 될 때 재생이 되도록 구현 할 수 있었습니다.

### 박자은

### 정재명
- 성공적인 팀 프로젝트 였습니다. 짧은 시간 안에 이런 웹 사이트를 만들 수 있었던 건 혼자가 아니였기 때문입니다. 적절한 업무 분담, 각자의 역할에 대한 몰입, 활발한 커뮤니케이션이 가능했기 때문에 원하는 결과물을 만들 수 있었습니다.
- 많은 것들을 학습하고 성장했습니다. 웹 프로그래밍에 대해 잘 몰랐었는데, CSR과 SSR의 차이에 대해 이해할 수 있었고, 왜 CSR이 유행했다가 다시 SSR로 돌아가고 있는지 생각해보는 계기가 되었습니다. 또한 평소에 접해보지 못했던 기술 스택들을 다뤄보면서 경험의 폭을 늘릴 수 있었습니다.
- 남은 정글 기간 동안 미니 프로젝트를 했던 4일동안의 몰입했던 기억을 가지고 최선을 다해보려 합니다. 
