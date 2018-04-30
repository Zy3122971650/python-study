import pymysql
while True:
    print("="*20)
    name=str(input("你想添加的名字").strip())
    birthday=str(input("他（她）（它）的生日像这样19990909 \n ：").strip())
    db=pymysql.connect("host","root","password","database")
    cursor=db.cursor()
    print(name,birthday)
    print("请确认信息正确，如果正确 输入 'y' 错误 输入 'n' ")
    YN=input().lower
    if YN=='n':
        cursor.close()
        db.close()
        continue
        passd
    else:

        try:
            cursor.execute("INSERT INTO Birthday (name,birthday) VALUES ('{}','{}')".format(name,birthday))
            db.commit()
            print("已完成")
            pass
        except:
            db.rollback()
            print("出错以滚回")
            pass
        cursor.close()
        db.close()

    pass

    
