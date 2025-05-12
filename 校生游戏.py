import random

print("欢迎来到大学校园生活模拟游戏！")

name = input("请为您的角色起名：")

print("请自由分配你的属性点(请输入整数）")
points = 100
attributes = ["学术能力", "社交能力", "体质健康", "心理健康"]
assigned_points = [0] * 4
count = 0
while True:
    for i, attr in enumerate(attributes):
        while True:
            print(f"当前剩余点数: {points}")
            assigned = int(input(f"请输入分配给 {attr} 的点数: "))
            if assigned < 0:
                print("分配的点数不能为负数，请重新输入。")
                continue
            if assigned > points:
                print(f"分配的点数不能超过剩余的 {points} 点，请重新输入。")
                continue
            assigned_points[i] = assigned
            points -= assigned
            count += 1
            break
    if count == len(attributes):
        break
print("分配结果如下：")
for attr, pts in zip(attributes, assigned_points):
    print(f"{attr}: {pts} 点")
if assigned_points[2] < 10 or assigned_points[3] < 10:
    print("你的身体状况很差，被送入了医院。")
    print("这学期你在医院里养病。")
    credits = 0
    volunteer_count = 0
    hosipitalized = 16
else:
    credits = 0
    volunteer_count = 0
    hosipitalized = 0
    choices = 16
    a = 0
    continuous_study = 0
    for i in range(choices):
        print(f"离学期结束还有{choices - i} 周。")
        print("请选择本周你要进行的活动：")
        print("1. 学习")
        print("2. 参加社交活动")
        print("3. 参加志愿者服务")
        print("4. 放松一下")
        print("5. 进行体育运动")
        choice_str = input("请输入你的选择：")
        choice = int(choice_str)
        if choice <= 0 or choice >= 6:
            print("请输入有效的选择。")
            continue
        if choice == 1:
            increase = random.randint(1, 5)
            assigned_points[0] += increase
            print(f"你认真学习，学术能力增加了 {increase} 点。")
            a += 1
            continuous_study += 1
            if a % 3 == 0:
                print("你完成了一门课，获得三学分。")
                credits += 3
            if continuous_study >= 6:
                target = random.choice([2, 3])
                decrease = random.randint(1, 5)
                assigned_points[target] -= decrease
                print(f"你的 {attributes[target]} 降低了 {decrease} 点。")
            if assigned_points[3] < 15:
                print("你的心理健康低于十五，你的状态让你很难好好学习")
                assigned_points[0] -= increase
        elif choice == 2:
            increase = random.randint(1, 5)
            assigned_points[1] += increase
            print(f"你积极参加社交活动，社交能力增加了 {increase} 点。")
            continuous_study = 0
        elif choice == 3:
            volunteer_count += 1
            target1, target2 = random.sample([1, 3], 2)
            increase1 = random.randint(1, 3)
            increase2 = random.randint(1, 3)
            assigned_points[target1] += increase1
            assigned_points[target2] += increase2
            print(f"你积极参加志愿者服务，{attributes[target1]} 增加了 {increase1} 点，{attributes[target2]} 增加了 {increase2} 点。")
            continuous_study = 0
            if increase1 == increase2:
                credits += 1
        elif choice == 4:
            increase = random.randint(1, 5)
            assigned_points[3] += increase
            print(f"你决定让自己放松一下。")
            print("你度过了比较轻松的一周，心理健康增加了 {increase} 点。")
            continuous_study = 0
        else:
            increase = random.randint(1, 5)
            assigned_points[2] += increase
            print(f"你的体质健康值增加了 {increase} 点。")
            continuous_study = 0
        if assigned_points[2] < 15:
            print("你的体质健康已经低于15，不幸生病，本周只好在医院度过。")
            choices -= 1
            assigned_points[2] = 16
            continuous_study = 0
    print("当前属性和学分情况：")
    for attr, pts in zip(attributes, assigned_points):
        print(f"{attr}: {pts} 点")
    print(f"学分: {credits}")
    
print("这学期结束了。")
if assigned_points[0] >= 50 and credits >= 9:
    print("获得成就：学术之星")
if assigned_points[1] >= 50:
    print("获得成就：社交达人")
if volunteer_count >= 4:
    print("获得成就：优秀志愿者")
if hospitalized >= 3:
    print("获得成就：脆皮大学生（请注意身体哦）")
    
print("最终属性和学分情况：")
for attr, pts in zip(attributes, assigned_points):
    print(f"{attr}: {pts} 点")
print(f"学分: {credits}")
