import numpy
import theano
from RNADE import *
from RNN_RNADE import RNN_RNADE
import mocap_data
import pdb
from numpy_implementations import *
import pickle

#model params
n_hidden = 50
n_recurrent = 100
n_visible = 49
n_components = 10
hidden_act = 'sigmoid'

#initialize model
model = RNN_RNADE(n_visible,n_hidden,n_recurrent,n_components,hidden_act='sigmoid',
                  load=False,rec_mu=True,rec_mix=False,rec_sigma=False)

load_dir = '/scratch/Sid/RNN_RNADE_2/100-300-10-0.1-0.001/mu'
model.load_model(None,filename='best_params_train.pickle')
model.build_RNN_RNADE()


#make functions for theano RNN-RNADE
theano_outputs = theano.function([model.v],[model.log_probs,model.u_t,model.b_alpha_t,model.b_mu_t,model.b_sigma_t])
new_seq = pickle.load(open('seq.pkl','r'))

#get sequence 

#fprop through numpy RNN-RNADE
np_ll,np_u_t,np_b_alpha_t,np_b_mu_t,np_b_sigma_t = RNN_RNADE_fprop(new_seq,model)
print np_ll