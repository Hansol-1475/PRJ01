class Member:
    def memberInformation(self, memberNumber):
        self.memberNumber = memberNumber
        self.name = ''
        self.age = 0
        self.sex = ''
        self.address = ''
        self.email = ''
        self.phoneNumber = ''
        self.rank=''

# 멤버 객체 생성(30명)
members = []
for i in range(0, 31):
    member = Member()
    member.memberInformation(i)
    members.append(member)

# 멤버 정보 설정
members[0].name = '김민수'
members[0].age = 21
members[0].sex = '남자'
members[0].address = '대구 수성구 범어동'
members[0].email = 'minsu0101@gmail.com'
members[0].phoneNumber = '010-3332-6677'

members[1].name = '박지영'
members[1].age = 25
members[1].sex = '여자'
members[1].address = '서울 강남구 역삼동'
members[1].email = 'jiyoungpark@gmail.com'
members[1].phoneNumber = '010-5555-8812'

members[2].name = '이철수'
members[2].age = 30
members[2].sex = '남자'
members[2].address = '부산 해운대구 우동'
members[2].email = 'chulsoo@gmail.com'
members[2].phoneNumber = '010-1156-2222'

members[3].name = '김영희'
members[3].age = 28
members[3].sex = '여자'
members[3].address = '인천 연수구 송도동'
members[3].email = 'younghee@gmail.com'
members[3].phoneNumber = '010-9909-7777'

members[4].name = '정민준'
members[4].age = 24
members[4].sex = '남자'
members[4].address = '대전 유성구 장동'
members[4].email = 'superjoon@gmail.com'
members[4].phoneNumber = '010-7777-8358'

members[5].name = '홍길동'
members[5].age = 27
members[5].sex = '남자'
members[5].address = '서울 종로구 청운효자동'
members[5].email = 'honggd@gmail.com'
members[5].phoneNumber = '010-1274-5678'

members[6].name = '김지영'
members[6].age = 26
members[6].sex = '여자'
members[6].address = '서울 종로구 청운효자동'
members[6].email = 'jiyoungkim@gmail.com'
members[6].phoneNumber = '010-1116-5432'

members[7].name = '박철수'
members[7].age = 29
members[7].sex = '남자'
members[7].address = '서울 종로구 청운효자동'
members[7].email = 'parkcs@gmail.com'
members[7].phoneNumber = '010-1381-2972'

members[8].name = '이영희'
members[8].age = 29
members[8].sex = '여자'
members[8].address = '서울 종로구 청운효자동'
members[8].email = 'yeonghee@gmail.com'
members[8].phoneNumber = '010-9949-8828'

members[9].name = '최민준'
members[9].age = 30
members[9].sex = '남자'
members[9].address = '서울 종로구 청운효자동'
members[9].email = 'minjunchoi@gmail.com'
members[9].phoneNumber = '010-7727-6636'

members[10].name = '김지수'
members[10].age = 59
members[10].sex = '여자'
members[10].address = '대구 수성구 범어동'
members[10].email = 'jisoo@gmail.com'
members[10].phoneNumber = '010-1634-5678'

members[11].name = '이준호'
members[11].age = 55
members[11].sex = '남자'
members[11].address = '서울 강남구 역삼동'
members[11].email = 'junho@gmail.com'
members[11].phoneNumber = '010-9876-5432'

members[12].name = '박예은'
members[12].age = 44
members[12].sex = '여자'
members[12].address = '부산 해운대구 우동'
members[12].email = 'yeeun@gmail.com'
members[12].phoneNumber = '010-1011-2242'

members[13].name = '김동현'
members[13].age = 39
members[13].sex = '남자'
members[13].address = '인천 연수구 송도동'
members[13].email = 'donghyumn@gmail.com'
members[13].phoneNumber = '010-0979-8788'

members[14].name = '정서연'
members[14].age = 48
members[14].sex = '여자'
members[14].address = '대전 유성구 장동'
members[14].email = 'seoyeonbb22@gmail.com'
members[14].phoneNumber = '010-7007-6286'

members[15].name = '홍길순'
members[15].age = 36
members[15].sex = '여자'
members[15].address = '서울 성북구 성북동'
members[15].email = 'hongsun@gmail.com'
members[15].phoneNumber = '010-5735-1321'

members[16].name = '이동준'
members[16].age = 53
members[16].sex = '남자'
members[16].address = '서울 성북구 성북동'
members[16].email = 'dongjune2@gmail.com'
members[16].phoneNumber = '010-2832-3813'

members[17].name = '박수영'
members[17].age = 40
members[17].sex = '여자'
members[17].address = '서울 성북구 성북동'
members[17].email = 'young22@gmail.com'
members[17].phoneNumber = '010-7511-9009'

members[18].name = '김철호'
members[18].age = 47
members[18].sex = '남자'
members[18].address = '서울 성북구 성북동'
members[18].email = 'cheolhokim@gmail.com'
members[18].phoneNumber = '010-1180-2521'

members[19].name = '이예진'
members[19].age = 29
members[19].sex = '여자'
members[19].address = '서울 성북구 성북동'
members[19].email = 'yejin33@gmail.com'
members[19].phoneNumber = '010-6256-3233'

members[20].name = '김민수'
members[20].age = 39
members[20].sex = '남자'
members[20].address = '경기도 수원시 영통구'
members[20].email = 'minsusuwon@gmail.com'
members[20].phoneNumber = '010-1004-5578'

members[21].name = '박지원'
members[21].age = 38
members[21].sex = '여자'
members[21].address = '대구 달서구 상인동'
members[21].email = 'jiwon5432@gmail.com'
members[21].phoneNumber = '010-9556-5432'

members[22].name = '이성민'
members[22].age = 36
members[22].sex = '남자'
members[22].address = '서울 마포구 망원동'
members[22].email = 'seongmi2n@gmail.com'
members[22].phoneNumber = '010-1163-2102'

members[23].name = '김혜진'
members[23].age = 24
members[23].sex = '여자'
members[23].address = '부산 남구 대연동'
members[23].email = 'hyejin8238@gmail.com'
members[23].phoneNumber = '010-9039-8238'

members[24].name = '정민준'
members[24].age = 29
members[24].sex = '남자'
members[24].address = '인천 남구 주안동'
members[24].email = 'm1njoon@gmail.com'
members[24].phoneNumber = '010-1747-6616'

members[25].name = '홍수진'
members[25].age = 27
members[25].sex = '여자'
members[25].address = '대전 중구 대흥동'
members[25].email = 'suj1n@gmail.com'
members[25].phoneNumber = '010-7335-1211'

members[26].name = '이영호'
members[26].age = 43
members[26].sex = '남자'
members[26].address = '서울 강서구 화곡동'
members[26].email = 'youngh0@gmail.com'
members[26].phoneNumber = '010-6602-3312'

members[27].name = '박수현'
members[27].age = 30
members[27].sex = '여자'
members[27].address = '서울 강남구 역삼동'
members[27].email = 'suhyune@gmail.com'
members[27].phoneNumber = '010-6477-0399'

members[28].name = '김태준'
members[28].age = 27
members[28].sex = '남자'
members[28].address = '서울 송파구 잠실동'
members[28].email = 'taejun@gmail.com'
members[28].phoneNumber = '010-1816-2232'

members[29].name = '이가영'
members[29].age = 35
members[29].sex = '여자'
members[29].address = '서울 서초구 반포동'
members[29].email = 'gagayoung@gmail.com'
members[29].phoneNumber = '010-6593-3133'