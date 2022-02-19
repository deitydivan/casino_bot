from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# START
inline_btn_profile = InlineKeyboardButton('профиль', callback_data='profile')
inline_btn_games = InlineKeyboardButton('игры', callback_data='games')
inline_kb_start = InlineKeyboardMarkup().row(
    inline_btn_profile, inline_btn_games)


# GAMES
inline_btn_roulette = InlineKeyboardButton('рулетка', callback_data='roulette')
inline_btn_kmz = InlineKeyboardButton(
    'камень-ножницы-бумага', callback_data='kmz')
inline_btn_eagleOr = InlineKeyboardButton(
    'орел или решка', callback_data='eagleOr')
inline_btn_hl = InlineKeyboardButton('high or low', callback_data='hl')

inline_kb_games = InlineKeyboardMarkup(row_width=2)
inline_kb_games.add(inline_btn_roulette, inline_btn_kmz,
                    inline_btn_eagleOr, inline_btn_hl)

# GAMES HIGH OR LOW
inline_btn_high = InlineKeyboardButton('больше', callback_data='high')
inline_btn_low = InlineKeyboardButton('меньше', callback_data='low')
inline_kb_hl = InlineKeyboardMarkup(row_width=2)
inline_kb_hl.add(inline_btn_high,inline_btn_low)


# GAMES EAGLE
inline_btn_eagle = InlineKeyboardButton(
    'орел ', callback_data='eagle')
inline_btn_tails = InlineKeyboardButton(
    'решка', callback_data='tails')
inline_kb_egle_tails = InlineKeyboardMarkup(row_width=2)
inline_kb_egle_tails.add(inline_btn_eagle, inline_btn_tails)
# GAMES KMZ
inline_btn_rock = InlineKeyboardButton(
    'камень ', callback_data='rock')
inline_btn_scissors = InlineKeyboardButton(
    'ножницы ', callback_data='scissors')
inline_btn_paper = InlineKeyboardButton(
    'бумага ', callback_data='paper')
inline_kb_kmz = InlineKeyboardMarkup(row_width=2)
inline_kb_kmz.add(inline_btn_rock, inline_btn_scissors,
                  inline_btn_paper)

#GAMES ROULETTE
inline_btn_zero = InlineKeyboardButton('0', callback_data='zero')
inline_btn_one = InlineKeyboardButton('1', callback_data='one')
inline_btn_two = InlineKeyboardButton('2', callback_data='two')
inline_btn_three = InlineKeyboardButton('3', callback_data='three')
inline_btn_four = InlineKeyboardButton('4', callback_data='four')
inline_btn_five = InlineKeyboardButton('5', callback_data='five')
inline_btn_six = InlineKeyboardButton('6', callback_data='six')
inline_btn_seven = InlineKeyboardButton('7', callback_data='seven')
inline_btn_eight = InlineKeyboardButton('8', callback_data='eight')
inline_btn_nine = InlineKeyboardButton('9', callback_data='nine')
inline_btn_ten = InlineKeyboardButton('10', callback_data='ten')
inline_btn_eleven = InlineKeyboardButton('11', callback_data='eleven')
inline_btn_twelve = InlineKeyboardButton('12', callback_data='twelve')
inline_btn_thirteen = InlineKeyboardButton('13', callback_data='thirteen')
inline_btn_fourteen = InlineKeyboardButton('14', callback_data='fourteen')
inline_btn_fiveteen = InlineKeyboardButton('15', callback_data='fiveteen')
inline_btn_sixteen = InlineKeyboardButton('16', callback_data='sixteen')
inline_btn_seventeen = InlineKeyboardButton('17', callback_data='seventeen')
inline_btn_eightteen = InlineKeyboardButton('18', callback_data='eightteen')
inline_btn_nineteen = InlineKeyboardButton('19', callback_data='nineteen')
inline_btn_twenty = InlineKeyboardButton('20', callback_data='twenty')
inline_btn_twenty_one = InlineKeyboardButton('21', callback_data='twenty_one')
inline_btn_twenty_two = InlineKeyboardButton('22', callback_data='twenty_two')
inline_btn_twenty_three = InlineKeyboardButton('23', callback_data='twenty_three')
inline_btn_twenty_four = InlineKeyboardButton('24', callback_data='twenty_four')
inline_btn_twenty_five = InlineKeyboardButton('25', callback_data='twenty_five')
inline_btn_twenty_six = InlineKeyboardButton('26', callback_data='twenty_six')
inline_btn_twenty_seven = InlineKeyboardButton('27', callback_data='twenty_seven')
inline_btn_twenty_eight = InlineKeyboardButton('28', callback_data='twenty_eight')
inline_btn_twenty_nine = InlineKeyboardButton('29', callback_data='twenty_nine')
inline_btn_thirty = InlineKeyboardButton('30', callback_data='thirty')
inline_btn_thirty_one = InlineKeyboardButton('31', callback_data='thirty_one')
inline_btn_thirty_two = InlineKeyboardButton('32', callback_data='thirty_two')
inline_btn_thirty_three = InlineKeyboardButton('33', callback_data='thirty_three')
inline_btn_thirty_four = InlineKeyboardButton('34', callback_data='thirty_four')
inline_btn_thirty_five = InlineKeyboardButton('35', callback_data='thirty_five')
inline_btn_thirty_six = InlineKeyboardButton('36', callback_data='thirty_six')
inline_btn_red = InlineKeyboardButton('🔴', callback_data='red_btn')
inline_btn_green = InlineKeyboardButton('🟢', callback_data='green_btn')
inline_btn_even = InlineKeyboardButton('even', callback_data='even')
inline_btn_odd = InlineKeyboardButton('odd', callback_data='odd')
inline_kb_roulette_play = InlineKeyboardMarkup(row_width=5)
inline_kb_roulette_play.add(inline_btn_zero)
inline_kb_roulette_play.add(inline_btn_one,inline_btn_two,inline_btn_three,inline_btn_four,inline_btn_five,inline_btn_six,inline_btn_seven,inline_btn_eight,inline_btn_nine,inline_btn_ten,inline_btn_eleven,inline_btn_twelve,inline_btn_thirteen,inline_btn_fourteen,inline_btn_fiveteen,inline_btn_sixteen,inline_btn_seventeen,inline_btn_eightteen,inline_btn_nineteen,inline_btn_twenty,inline_btn_twenty_one,inline_btn_twenty_two,inline_btn_twenty_three,inline_btn_twenty_four,inline_btn_twenty_five,inline_btn_twenty_six,inline_btn_twenty_seven,inline_btn_twenty_eight,inline_btn_twenty_nine,inline_btn_thirty,inline_btn_thirty_one,inline_btn_thirty_two,inline_btn_thirty_three,inline_btn_thirty_four,inline_btn_thirty_five,inline_btn_even,inline_btn_red,inline_btn_thirty_six,inline_btn_odd,inline_btn_green)

# PROFILE
inline_btn_balance = InlineKeyboardButton('баланс', callback_data='balance')
inline_btn_name = InlineKeyboardButton('имя', callback_data='name')
inline_kb_profile = InlineKeyboardMarkup().row(
    inline_btn_balance, inline_btn_name)
