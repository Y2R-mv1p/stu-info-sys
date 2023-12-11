import random
import string

def generate_realistic_name():
    surnames = ["吴", "王", "李", "张", "刘", "陈", "洪", "汪", "胡", "苏", "阮", "侯", "吕"]
    chinese_characters = "巧月巧云今夜巧非宁静无以致远超然离俗尘采菊东篱下低头思故乡岂同凡鸟群"
    given_name = random.choice(chinese_characters) + random.choice(chinese_characters)
    surname = random.choice(surnames)
    return f"{surname}{given_name}".capitalize()

def generate_realistic_address():
    cities = ["合肥"]
    roads = ["安庆路", "黄山路", "潜山路", "长江路", "延乔路", "繁华大道", "望江路", "合作化南路", "金寨路", "宁国路", "马鞍山路"]
    number = ''.join(random.choices(string.digits, k=2))
    return f"{random.choice(cities)}{random.choice(roads)}{number} 号"

def generate_random_info():
    student_id = ''.join(random.choices(string.digits, k=8))
    # 姓名生成
    student_name = generate_realistic_name()
    student_class = random.choice(["1班", "2班", "3班"])
    student_email = f"{student_id}@qq.com"
    # 地址生成
    student_address = generate_realistic_address()
    subject_grades = [random.randint(60, 100) for _ in range(5)]
    student_info = {
        "学号": student_id,
        "姓名": student_name,
        "班级": student_class,
        "邮箱": student_email,
        "家庭住址": student_address,
        "科目1": subject_grades[0],
        "科目2": subject_grades[1],
        "科目3": subject_grades[2],
        "科目4": subject_grades[3],
        "科目5": subject_grades[4],
    }

    return student_info

