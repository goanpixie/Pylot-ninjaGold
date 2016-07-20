"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random, datetime

class NinjaGolds(Controller):
    def __init__(self, action):
        super(NinjaGolds, self).__init__(action)
        

        self.load_model('WelcomeModel')
        self.db = self._app.db
   
    def index(self): 
        if not 'gold_pot' in session.keys():
            session['gold_pot']=0
            print session['gold_pot']
            session['is_game_in_progress'] = True

        if 'output_text' not in session:
            session['output_text'] = ''
            print session['output_text']  
        return self.load_view('index.html')

    def process_money(self):
        time=datetime.datetime.now()

        if (request.form).has_key('farmGold'):
            session['farmGold']=random.randint(10,20)
            session['gold_pot']+=session['farmGold']
            # flash('Earned',session['gold_pot'],'golds from the farm!',timestamp = datetime.now())
            session['output_text']+='<p class="green">Earned ' +str(session['farmGold'])+ ' golds from the farm!</p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))
            # print session['output']

        if (request.form).has_key('caveGold'):
            session['caveGold']=random.randrange(5,10)
            session['gold_pot']+=session['caveGold']
            session['output_text']+='<p class="green"> Earned '+str(session['caveGold'])+' golds from the cave!</p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))

        if (request.form).has_key('houseGold'):
            session['houseGold']=random.randrange(2,5)
            session['gold_pot']+=session['houseGold']
            session['output_text']+='<p class="green"> Earned '+str(session['houseGold'])+' golds from the house!</p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))

        if (request.form).has_key('casinoGold'):
            session['casinoGold']=random.randrange(-50,50)
            session['gold_pot']+=session['casinoGold']
            if session['casinoGold']<0: 
                session['output_text']+='<p class="red">Lost '+str((session['casinoGold'])*(-1))+' golds from the casino! </p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))
            elif session['casinoGold']>0:
                session['output_text']+='<p class="green">Earned '+str(session['casinoGold'])+' golds from the casino! </p>'+(time.strftime("%Y-%m-%dT%H:%M:%S"))



        return redirect('/')

    def clear(self):
        session.clear()
        return redirect('/')
  
        # session.pop('gold_pot')
        # session['is_game_in_progress'] = False





    

