import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjI4ODA0MDIzNjk2MjI4Mzky.XZdAkw.7YED188pi0MwyP-la_6F54_Hlv0'
self_bot_token = 'NTYzMDU4MzI1ODQ4MTk1MDcz.XZmHFw.VE8Xs2IZoGGXndzEczvRQAjOJTg'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '628652407689314305')

input_hq_private  = [
    "626320837120753684",
    "628291818257121298",
    "620471823787622420",
	"626992737018970112",
	"588070986554015764",
	"513818250652680213",
	"544381529829146645",
    "569843705654149130",
    "566979656083963918", # answers1
    "559442345674670082", #answers2
    '559357612068700183' #trivia-answers
]
input_hq_public = ['578824124072329226']
command_channel = '578824124072329226' #trivia-answers
admin_chat = '578824124072329226' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
