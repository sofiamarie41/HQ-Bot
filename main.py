
'''
using discord.py version 1.0.0a
'''
import discord
import asyncio
import re
import multiprocessing
import threading
import concurrent

#BOT_OWNER_ROLE = '' # change to what you need
#BOT_OWNER_ROLE_ID = "583573353978265610" 
  
 

 
oot_channel_id_list = [
'708939235259973652','709419284975059014'
]


answer_pattern = re.compile(r'(not|n)?([1-3]{1})(\?)?(cnf)?(\?)?$', re.IGNORECASE)

apgscore = 60
nomarkscore = 30
markscore = 15

async def update_scores(content, answer_scores):
    global answer_pattern

    m = answer_pattern.match(content)
    if m is None:
        return False

    ind = int(m[2])-1

    if m[1] is None:
        if m[3] is None:
            if m[4] is None:
                answer_scores[ind] += nomarkscore
            else: # apg
                if m[5] is None:
                    answer_scores[ind] += apgscore
                else:
                    answer_scores[ind] += markscore

        else: # 1? ...
            answer_scores[ind] += markscore

    else: # contains not or n
        if m[3] is None:
            answer_scores[ind] -= nomarkscore
        else:
            answer_scores[ind] -= markscore

    return True

class SelfBot(discord.Client):

    def __init__(self, update_event, answer_scores):
        super().__init__()
        global oot_channel_id_list
        #global wrong
        self.oot_channel_id_list = oot_channel_id_list
        self.update_event = update_event
        self.answer_scores = answer_scores

    async def on_ready(self):
        print("======================")
        print("Nelson Trivia Self Bot")
        print("Connected to discord.")
        print("User: " + self.user.name)
        print("ID: " + str(self.user.id))

    # @bot.event
    # async def on_message(message):
    #    if message.content.startswith('-debug'):
    #         await message.channel.send('d')

        def is_scores_updated(message):
            if message.guild == None or \
                str(message.channel.id) not in self.oot_channel_id_list:
                return False

            content = message.content.replace(' ', '').replace("'", "")
            m = answer_pattern.match(content)
            if m is None:
                return False

            ind = int(m[2])-1

            if m[1] is None:
                if m[3] is None:
                    if m[4] is None:
                        self.answer_scores[ind] += nomarkscore
                    else: # apg
                        if m[5] is None:
                            self.answer_scores[ind] += apgscore
                        else:
                            self.answer_scores[ind] += markscore

                else: # 1? ...
                    self.answer_scores[ind] += markscore

            else: # contains not or n
                if m[3] is None:
                    self.answer_scores[ind] -= nomarkscore
                else:
                    self.answer_scores[ind] -= markscore

            return True

        while True:
            await self.wait_for('message', check=is_scores_updated)
            self.update_event.set()

class Bot(discord.Client):

    def __init__(self, answer_scores):
        super().__init__()
        self.bot_channel_id_list = []
        self.embed_msg = None
        self.embed_channel_id = None
        #global wrong
        self.answer_scores = answer_scores

        # embed creation
        self.embed=discord.Embed(title="**__LOCO TRIVIA__**",color=0x0ff14)
        self.embed.add_field(name=f"**Aɴsᴡᴇʀ 1**", value="0.0 ", inline=True)
        self.embed.add_field(name=f"**Aɴsᴡᴇʀ 2**", value="0.0 ", inline=True)
        self.embed.add_field(name=f"**Aɴsᴡᴇʀ 3**", value="0.0 ", inline=True)
        self.embed.add_field(name=f"**__BEST ANSWER..!__**", value="0.0", inline=True)
        self.embed.add_field(name=f"**___SUGGEST ANSWER___**", value="0.0", inline=True)
        self.embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/583675981466828801/685776310525755392/unnamed.png")
        self.embed.set_footer(text="Loco Answer | HACK么7676™ ||")
   
        

        #await self.bot.add_reaction(embed,':spy:')


    async def clear_results(self):
        for i in range(len(self.answer_scores)):
            self.answer_scores[i]=0

    async def update_embeds(self):
      #  global wrong

         

        one_check = ""
        two_check = ""
        three_check = ""
        wrong_answer = ""
        

        lst_scores = list(self.answer_scores)
        

        highest = max(lst_scores)
        wrong_answer = ""
        lowest = min(lst_scores)
        answer = lst_scores.index(highest)+1
        

        #global wrong             

        if highest > 0:
            if answer == 1:
                one_check = " :one: :white_check_mark: "
            else:
                one_check = ""
                wrong_answer = " :one: :x:"
       

            if answer == 2:
                two_check = " :two: :white_check_mark: "
            else:
                two_check
                wrong_answer = " :two: :x:"
       

            if answer == 3:
                three_check = " :three: :white_check_mark: "
            else:
                three_check = ""
                wrong_answer = " :three: :x:"
          

            

        if lowest < 0:
            if answer == 1:
                one_cross = ":x:"
            if answer == 2:
                two_cross = ":x:"
            if answer == 3:
                three_cross = ":x:"
            
        self.embed=discord.Embed(title=f"**__LOCO TRIVIA__**\n\n**__Counter Answer__**\n**Answer :one: :- {lst_scores[0]}{one_check}\nAnswer :two: :- {lst_scores[1]}{two_check}\nAnswer :three: :- {lst_scores[2]}{three_check}**\n\n**__Crowd Result__** \n**Answer :- {one_check}{two_check}{three_check}\n__Crowd Wrong__** \n**Answer :- {wrong_answer}**",color=0x0ff14)
        self.embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/583675981466828801/685776310525755392/unnamed.png")
        self.embed.set_image(url="https://cdn.discordapp.com/attachments/625229957135597578/625246299947794432/SAVE_20190922_135432.gif")
        self.embed.set_footer(text="LOCO ANSWER | BOT")


        if self.embed_msg is not None:
            await self.embed_msg.edit(embed=self.embed)

    async def on_ready(self):
        print("==============")
        print("Nelson Trivia")
        print("Connected to discord.")
        print("User: " + self.user.name)
        print("ID: " + str(self.user.id))

        await self.clear_results()
        await self.update_embeds()
        #await self.change_presence(activity=discord.Game(name='with '+str(len(set(self.get_all_members())))+' users'))
        await self.change_presence(activity=discord.Activity(type=1,name="Loco Trivia | Auto"))

    async def on_message(self, message):

        # if message is private
        if message.author == self.user or message.guild == None:
            return

        if message.content.lower() == "lo":
            #await message.delete()
           # if BOT_OWNER_ROLE in []:
            self.embed_msg = None
            await self.clear_results()
            await self.update_embeds()
            self.embed_msg = \
                await message.channel.send('',embed=self.embed)
                #await self.embed_msg.add_reaction("✔️")
                #await self.embed_msg.add_reaction("✖️")
            self.embed_channel_id = message.channel.id
            #else:
                #await message.channel.send("**Lol** You Not Have permission To Use This **cmd!** :stuck_out_tongue_winking_eye:")
            #return

          

        # process votes
        if message.channel.id == self.embed_channel_id:
            content = message.content.replace(' ', '').replace("'", "")
            updated = await update_scores(content, self.answer_scores)
            if updated:
                await self.update_embeds()

def bot_with_cyclic_update_process(update_event, answer_scores):

    def cyclic_update(bot, update_event):
        f = asyncio.run_coroutine_threadsafe(bot.update_embeds(), bot.loop)
        while True:
            update_event.wait()
            update_event.clear()
            f.cancel()
            f = asyncio.run_coroutine_threadsafe(bot.update_embeds(), bot.loop)
            #res = f.result()

    bot = Bot(answer_scores)

    upd_thread = threading.Thread(target=cyclic_update, args=(bot, update_event))
    upd_thread.start()

    loop = asyncio.get_event_loop()
    loop.create_task(bot.start('NzA5Nzg3MjA1MTg2NDg2MzEy.Xrq_Bg.52OLHukHd4-MFHYWLdavvDC_jHw'))
    loop.run_forever()


def selfbot_process(update_event, answer_scores):

    selfbot = SelfBot(update_event, answer_scores)

    loop = asyncio.get_event_loop()
    loop.create_task(selfbot.start('NzAyNDk4MTc1OTM1ODQwMzE2.XqQvjw.VY9cwAvxn-9dgy8MtEM8PfebLwU',
                                   bot=False))
    loop.run_forever()

if __name__ == '__main__':

    # running bot and selfbot in separate OS processes

    # shared event for embed update
    update_event = multiprocessing.Event()

    # shared array with answer results
    answer_scores = multiprocessing.Array(typecode_or_type='i', size_or_initializer=7)

    p_bot = multiprocessing.Process(target=bot_with_cyclic_update_process, args=(update_event, answer_scores))
    p_selfbot = multiprocessing.Process(target=selfbot_process, args=(update_event, answer_scores))

    p_bot.start()
    p_selfbot.start()

    p_bot.join()
    p_selfbot.join()




 
 
