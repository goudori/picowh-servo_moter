from machine import PWM, Pin  # type: ignore
import time

# サーボモーターの設定
servo_moter = PWM(Pin(28))  # GP28
servo_moter.freq(50)  # サーボモーターの周波数50Hz　※50Hzが限度

max_duty = 65535  # PWM最大出力値

dig_minus90 = 0.025  # -90度のデューティー値

dig_plus90 = 0.12  # 90度のデューティー値


# 　指定された角度にサーボモーターを動かす
def move_servo(angle):
    # 角度の確認をする為の条件分岐
    if angle < -90 or angle > 90:
        raise ValueError("角度は90度から-90度でなければ、エラーになります。")

    # 角度からデューティ比を計算
    duty = int(
        max_duty * (dig_minus90 + (dig_plus90 - dig_minus90) * (angle + 90) / 180)
    )

    # サーボモーターにデューティ比を指定して動かす
    servo_moter.duty_u16(duty)


while True:
    print("1: 15度 and -15度\n" "2: 45度 and -45度\n" "3: 90度 and -90度\n")

    angle_option = input("動かす角度を選択して:")

    # 角度のオプションメニュー
    if angle_option == "1":
        # 15度動かす
        move_servo(15)
        time.sleep(2)

        # -15度動かす
        move_servo(-15)
        time.sleep(2)

    elif angle_option == "2":
        # 45度動かす
        move_servo(45)
        time.sleep(2)

        # -45度動かす
        move_servo(-45)
        time.sleep(2)

    elif angle_option == "3":
        # -90度動かす
        move_servo(-90)
        time.sleep(2)

        # 90度動かす
        move_servo(90)
        time.sleep(2)

    else:
        # 0度に動かす
        move_servo(0)
        print("終了")
        break
