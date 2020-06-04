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

bot_token = 'NzE4MDIyOTk4Nzk1MjIzMDQy.Xti1oA.dDb2nKOo190xPxumRIpbbEt9Bp0'
self_bot_token = 'NzExODkxNTM2MDMxMjUyNTQy.Xtizvg.U2CzG-sZlWFdAf-7Z630-xa7fI8'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '718021754043236422')

input_hq_private  = [
    "718021754043236422",
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
input_hq_public = ['718021754043236422']
command_channel = '718021754043236422' #trivia-answers
admin_chat = '718021754043236422' # answers2

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
