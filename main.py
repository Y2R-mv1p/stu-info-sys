from student_management_system import StudentManagementSystem

from random_info_generator import generate_random_info

random_student_info = generate_random_info()


def main():
    system = StudentManagementSystem("student_info.xlsx")

    while True:
        print("\n学生信息管理系统")
        print("1. 添加学生信息")
        print("2. 查找学生信息")
        print("3. 删除学生信息")
        print("4. 更新学生信息")
        print("5. 退出")

        choice = input("请选择操作 (1-5): ")
        if choice == '1':
            student_info = system.generate_random_info()
            system.add_student(student_info)
            print("学生信息已添加！")

        elif choice == '2':
            student_id = input("请输入学号查找学生信息: ")
            student = system.find_student(student_id)
            if student:
                print("找到学生信息:")
                print(student)
            else:
                print("未找到学生信息。")

        elif choice == '3':
            student_id = input("请输入学号删除学生信息: ")
            if system.delete_student(student_id):
                print("学生信息已删除！")
            else:
                print("未找到学生信息。")

        elif choice == '4':
            student_id = input("请输入学号更新学生信息: ")
            new_info = system.generate_random_info()
            if system.update_student_info(student_id, new_info):
                print("学生信息已更新！")
            else:
                print("未找到学生信息。")

        elif choice == '5':
            system.update_excel()
            print("程序已退出。")
            break

        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
    # 最开始生成并添加大量数据
    system = StudentManagementSystem("student_info.xlsx")
    for _ in range(100):
        student_info = generate_random_info()
        system.add_student(student_info)
