# 1 Guess The Number Game:
# -we will generate a random number with the help of randint() function from 1 to 100 and ask the user to guess it.!)
# -After every guess, the user will be told if the number is above or below the randomly generated number.
# -The user will win if they guess the number maximum five attempts.
# -Ask the user to stop or continue playing again.
# ***
# Add another situations like:
# level of game (hard (guess 3 times), medium (6 times), easy (10 times)
# assume that you have 100$, each game you spent 5$. Play game until you choose stop, report the game you win/lost and amount you have.
import random
def play_round(số_lần_thử_tối_đa , số_bí_mật):
    print(f"\nTôi có thể đang nghĩ về một số nào đó trong khoảng từ 1 đến 100. Bạn có {số_lần_thử_tối_đa} lần đoán.")
    for số_đoán in range(1, số_lần_thử_tối_đa + 1):
        try:
            guess = int(input(f"Lần đoán thứ {số_đoán}: Nhập số bạn đoán: "))
        except ValueError:
            print("Dữ liệu không hợp lệ! Vui lòng nhập một số nguyên.")
            continue
        if guess < số_bí_mật:
            print("Số bạn đoán quá nhỏ!")
        elif guess > số_bí_mật:
            print("Số bạn đoán quá lớn!")
        else:
            print(f" Chính xác! Bạn đã đoán đúng số {số_bí_mật} sau {số_đoán} lần đoán!")
            return True
    print(f"\nRất tiếc, Bạn đã hết lượt đoán. Con số bí mật là {số_bí_mật}.")
    return False
def main_game():
    tiền_của_người_chơi = 100
    lần_thắng = 0
    lần_thua = 0
    chi_phí_chơi_game = 5
    print("Chào mừng bạn đến với trò chơi Đoán Số ")
    print(f"Bạn bắt đầu với ${tiền_của_người_chơi}. Mỗi lượt chơi tốn ${chi_phí_chơi_game}.")
    while True:
        if tiền_của_người_chơi < chi_phí_chơi_game:
            print("\nÔi không! Bạn không còn đủ tiền để chơi một vòng nữa.")
            break
        print("\n" + "-" * 30)
        print(f"Bạn đang có ${tiền_của_người_chơi}. Bắt đầu một vòng mới nào!")
        tiền_của_người_chơi -= chi_phí_chơi_game
        màn_chơi = 0
        while True:
            level = input("Chọn độ khó - (D)Dễ, (T)Trung bình, hoặc (K)Khó: ").lower()
            if level in ['d', 'dễ']:
                màn_chơi = 10
                break
            elif level in ['t', 'trung bình']:
                màn_chơi = 6
                break
            elif level in ['k', 'khó']:
                màn_chơi = 3
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập d, t, hoặc k.")
        số_dự_đoán = random.randint(1, 100)
        vòng_thắng = play_round(màn_chơi,số_dự_đoán)
        if vòng_thắng:
            lần_thắng += 1
            print("Bạn đã thắng vòng này!")
        else:
            lần_thua += 1
            print("Bạn đã thua vòng này.")
        print(f"Thống kê hiện tại -> Thắng: {lần_thắng} | Thua: {lần_thua} | Tiền còn lại: ${tiền_của_người_chơi}")
        print("-" * 30)
        while True:
            chơi_lại = input("\nBạn có muốn chơi lại không? (có/Không): ").lower()
            if chơi_lại in ["có", "không", "c", "k"]:
                break
            else:
                print("Dữ liệu không hợp lệ. Vui lòng nhập 'c' hoặc 'K'.")
        if chơi_lại in ["Không", "k"]:
            break
    print("\n Cảm ơn bạn đã chơi đoán số ")
    print("Đây là báo cáo cuối cùng của bạn:")
    print(f"  Tổng số lần thắng: {lần_thắng}")
    print(f"  Tổng số lần thua:  {lần_thua}")
    print(f"  Số tiền cuối cùng: ${tiền_của_người_chơi}")
if __name__ == "__main__":
    main_game()
