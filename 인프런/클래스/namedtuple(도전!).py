# #from collections import namedtuple

# # 1. Student 구조 정의
# Student = namedtuple("Student", "name sid score")

# # 2. 학생 목록 만들기
# students = [
#     Student("은서", 1001, 85),
#     Student("보람", 1002, 92),
#     Student("민수", 1003, 74),
#     Student("지연", 1004, 58),
#     Student("하늘", 1005, 99),
# ]

# # 3. 출력
# print("🎓 학생 목록")
# for s in students:
#     print(f"{s.sid}번 {s.name} - {s.score}점")

# # 4. 평균 점수
# avg = sum(s.score for s in students) / len(students)
# print(f"\n📊 전체 평균 점수: {avg:.2f}점")

# # 5. 최고점 학생
# top = max(students, key=lambda s: s.score)
# print(f"🏅 최고 점수 학생: {top.name} ({top.score}점)")

# # 6. 60점 미만 낙제자
# print("\n❗ 낙제 학생 목록 (60점 미만)")
# for s in students:
#     if s.score < 60:
#         print(f"{s.name} ({s.score}점)")

from collections import namedtuple
Student=namedtuple("Student","name id score")
names=["은서","하늘","보람","성연","종기"]
ids=[1004,1005,1006,1007,2000]
scores=[97,50,95,70,100]
students=[Student(a,b,c) for a,b,c in zip(names,ids,scores)]
for i in students:
    print(f"이름: {i.name} | 학번 : {i.id} => [{i.score}점]")
#평균 점수
total=sum(s.score for s in students)/len(students)
#최고점
s=max(students,key=lambda x:x.score)
print(f"최고점 학생: {s.name} ({s.score})")
#낙제 판별
for i in students:
    if i.score<60:
        print("낙제생: "+i.name,i.id)

