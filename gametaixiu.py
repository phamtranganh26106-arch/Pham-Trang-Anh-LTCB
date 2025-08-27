# 2.Write a game that simulate rolling a pair of dice.
# -If the sum of two faces is greater than 5 à “Tài”
# -Otherwise  à “Xỉu”
# -User ask for guessing “Tài” or “Xỉu”
# -Match the results
# -After one turn, ask user for continue playing game.
# -**** Extend the game by asking the user to enter an amount of money, then continue playing until the user runs out of money or the user stops playing. Statistics of results.results
import random
import time
def nhận_tiền_của_người_chơi():
    while True:
        try:
            tiền = int(input("Bạn muốn bắt đầu với bao nhiêu tiền? $"))
            if tiền > 0:
                return tiền
            else:
                print("Vui lòng nhập một số tiền lớn hơn 0.")
        except ValueError:
            print("Số tiền không hợp lệ. Vui lòng nhập một con số.")
def nhận_tiền_cược_của_người_chơi(lượt_cược_cao_nhất):
    while True:
        try:
            cược = int(input(f"Bạn muốn cược bao nhiêu cho vòng này? (Tối đa ${lượt_cược_cao_nhất}): $"))
            if 0 < cược <= lượt_cược_cao_nhất:
                return cược
            else:
                print(f"Vui lòng cược một số tiền trong khoảng từ $1 đến ${lượt_cược_cao_nhất}.")
        except ValueError:
            print("Số tiền không hợp lệ. Vui lòng nhập một con số.")
def nhận_đự_đoán_của_người_chơi():
    while True:
        đoán = input("Bạn đoán là (T)ài hay (X)ỉu? ").lower()
        if đoán in ['t', 'tai', 'x', 'xiu']:
            if đoán.startswith('t'):
                return "tài"
            else:
                return "xỉu"
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập 'T' cho Tài hoặc 'X' cho Xỉu.")
def play_game():
    tiền_của_người_chơi = nhận_tiền_của_người_chơi()
    người_chơi = 0
    thắng = 0
    print("\n BẮT ĐẦU TRÒ CHƠI TÀI XỈU ")
    while tiền_của_người_chơi > 0:
        print("\n" + "=" * 30)
        print(f"Vòng {người_chơi + 1}. Bạn đang có: ${tiền_của_người_chơi}")
        cá_cược = nhận_tiền_cược_của_người_chơi(tiền_của_người_chơi)
        dự_đoán = nhận_đự_đoán_của_người_chơi()
        print("Đang tung xúc xắc...")
        time.sleep(1.5)
        xúc_sắc1 = random.randint(1, 6)
        xúc_sắc2 = random.randint(1, 6)
        total = xúc_sắc1 + xúc_sắc2
        if total > 5:
            result = "tài"
        else:
            result = "xỉu"
        print(f"Kết quả: Xúc xắc 1 ra [{xúc_sắc1}], Xúc xắc 2 ra [{xúc_sắc2}]")
        print(f"Tổng là {total} => {result.upper()}!")
        if dự_đoán == result:
            print(f" Chúc mừng! Bạn đã đoán đúng và thắng ${cá_cược}.")
            tiền_của_người_chơi += cá_cược
            thắng += 1
        else:
            print(f"Rất tiếc! Bạn đã đoán sai và mất ${cá_cược}.")
            tiền_của_người_chơi -= cá_cược
        người_chơi += 1
        if tiền_của_người_chơi == 0:
            print("\nBạn đã hết tiền!")
            break
        while True:
            tiếp_tục_chơi = input("Bạn có muốn chơi tiếp không? (c/k): ").lower()
            if tiếp_tục_chơi in ['c', 'co', 'k', 'khong']:
                break
            else:
                print("Lựa chọn không hợp lệ.")
        if tiếp_tục_chơi.startswith('k'):
            break
    print("\n KẾT THÚC TRÒ CHƠI ")
    print("Cảm ơn bạn đã tham gia!")
    print("Thống kê cuối cùng của bạn:")
    print(f"  - Tổng số vòng đã chơi: {người_chơi}")
    print(f"  - Số vòng thắng: {thắng}")
    print(f"  - Số vòng thua: {người_chơi - thắng}")
    print(f"  - Số tiền cuối cùng: ${tiền_của_người_chơi}")
    print("=" * 28)
if __name__ == "__main__":
    play_game()
