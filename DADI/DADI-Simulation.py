#####################################################################################################################################
### This is the script we used to run DADI for simulations. This script needs dependency on DADI_Simulation_demographic_models.py
### We used project size [100,100] and pts_l = [100,200,300].
#####################################################################################################################################

#!/urs/bin/python
import numpy
import scipy
from numpy import array
import os
import sys
import dadi
import  demographic_models22
import  Models_2D
import  Demographics2D


def dadi_estimation(inputfile, demographic, polarized, migration):
  dd = dadi.Misc.make_data_dict(inputfile)
  print "Done: read data from input file!"
  data = dadi.Spectrum.from_data_dict(dd, pop_ids=['ABC','DE'], projections=[24,15], polarized=False)
  ns = data.sample_sizes
  print "The projections = [24,15]"
  pts_l = [50,60,70]
  print "pts_l = [50,60,70]"

  # two pop bottleneck model
# if demographic == 'Twopop-Bottleneck-Model': 
#    pts_l = [50,60,70]
#    func = demographic_models.prior_twopop_bottleneck_mig
#    params = array([0.05, 0.5598, 0.088, 0.93, 0.535, 1.576, 0.235, 0.1845])
#   upper_bound = [100, 100, 100, 100, 100, 500,10,10]
#    lower_bound = [1e-2,1e-2,1e-2,1e-2, 1e-2, 0, 0,0]
#    fixed_params = [None, None, None, None, 1.0, 0.0, None, None]
#    print "The model is two pop bottleneck model"
#    print "The parameters are: (nu1B, nu1F,nu2B,nu2F,nuA, m,Tp,T)"
#    print "The initial parameters are: ", params 
#  
  #1 no migration model, same with strict isolation model
  if demographic == 'no_mig': 
    pts_l = [50,60,70]
    func =  Models_2D.no_mig
    params = array([8.47017,4.3902,0.0526854])
    upper_bound = [100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None]
    print "The model is strict isolation model model"
    print "The parameters are: (nu1, nu2, T)"
    print "The initial parameters are: ", params

  #2 split with symmatric migration model
  if demographic == 'split_mig': 
    pts_l = [50,60,70]
    func =  Demographics2D.split_mig
    params = array([1.0, 1.0, 1.0, 1.0])
    upper_bound = [100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None]
    print "The model is Split into two populations of specifed size, with migration model"
    print "The parameters are: (nu1, nu2, T, m)"
    print "The initial parameters are: ", params


  #3 Split into two populations, with different migration rates
  if demographic == 'asym_mig': 
    pts_l = [50,60,70]
    func =  Models_2D.asym_mig
    params = array([0.085861,0.139045,0.0628436,1.17523,0.0100003])
    upper_bound = [100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None]
    print "The model is Split into two populations, with different migration rates"
    print "The parameters are: (nu1, nu2, m12, m21, T)"
    print "The initial parameters are: ", params

  #4 Model with split and no gene flow, followed by period of symmetrical gene flow
  if demographic == 'sec_contact_sym_mig': 
    pts_l = [50,60,70]
    func =  Models_2D.sec_contact_sym_mig
    params = array([1.04239, 1.22869, 2.58872, 0.425956, 0.283847])
    upper_bound = [20, 20, 40, 10, 10]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None]
    print "The model is sec_contact_sym_mig"
    print "The parameters are: (nu1, nu2, m, T1, T2)"
    print "The initial parameters are: ", params

  #5 Model with split and no gene flow, followed by period of symmetrical gene flow
  if demographic == 'sec_contact_asym_mig': 
    pts_l = [50,60,70]
    func =  Models_2D.sec_contact_asym_mig
    params = array([0.926479, 1.3363, 3.31188, 2.07183, 0.414847, 0.26607])
    upper_bound = [10, 10, 16, 15, 8, 5]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None]
    print "The model is sec_contact_asym_mig"
    print "The parameters are: (nu1, nu2, m12, m21, T1, T2)"
    print "The initial parameters are: ", params

  #6 Split into two populations with no migration, then size change
  if demographic == 'no_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.no_mig_size
    params = array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    upper_bound = [100, 100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None]
    print "The model is Split into two populations with no migration, then size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, T1, T2)"
    print "The initial parameters are: ", params

  #7 Split into two populations with symmetric migration, size change
  if demographic == 'sym_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.sym_mig_size
    params = array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    upper_bound = [100, 100, 100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None]
    print "The model is Split into two populations with symmetric migration, size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, m, T1, T2)"
    print "The initial parameters are: ", params

  #8 Split into two populations with asymmetric migration, size change
  if demographic == 'asym_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.asym_mig_size
    params = array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    upper_bound = [100, 100, 100, 100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None, None]
    print "The model is Split into two populations with asymmetric migration, size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, m12, m21, T1, T2)"
    print "The initial parameters are: ", params

  #9 Model with split and no gene flow, followed by symmetrical gene flow, size change
  if demographic == 'anc_sym_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.anc_sym_mig_size
    params = array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    upper_bound = [100, 100, 100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None]
    print "The model is Split into two populations with symmetric migration, size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, m, T1, T2)"
    print "The initial parameters are: ", params

  #10 Model with split and no gene flow, followed by asymmetrical gene flow, size change
  if demographic == 'anc_asym_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.anc_asym_mig_size
    params = array([1.0, 1.0, 1.0, 1.0, 3.31188, 2.07183, 0.414847, 0.26607])
    upper_bound = [100, 100, 100, 100, 10, 10, 10, 10]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None, None]
    print "The model is split and no gene flow, followed by asymmetrical gene flow, size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, m12, m21, T1, T2)"
    print "The initial parameters are: ", params

  #11 Model with split in isolation, followed by secondary contact with symmetrical gene flow, size change
  if demographic == 'sec_contact_sym_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.sec_contact_sym_mig_size
    params = array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    upper_bound = [100, 100, 100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None]
    print "The model is split in isolation, followed by secondary contact with symmetrical gene flow, size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, m, T1, T2)"
    print "The initial parameters are: ", params

  #12 Model with split in isolation, followed by secondary contact with asymmetrical gene flow, size change
  if demographic == 'sec_contact_asym_mig_size': 
    pts_l = [50,60,70]
    func =  Models_2D.sec_contact_asym_mig_size
    params = array([1.21192, 2.18235, 0.690729, 1.00252, 5.18979, 2.68898, 0.32193, 0.114907])
    upper_bound = [15, 20, 8, 10, 30, 10, 10, 10]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None, None]
    print "The model is split in isolation, followed by secondary contact with asymmetrical gene flow, size change"
    print "The parameters are: (nu1a, nu2a, nu1b, nu2b, m12, m21, T1, T2)"
    print "The initial parameters are: ", params

  #13 IMpre  allows for population size changes before and after species split
  if demographic == 'IM_pre': 
    pts_l = [50,60,70]
    func =  Demographics2D.IM_pre
    params = array([0.0969677, 0.548046, 0.147397, 1.04744, 1.50377, 5.82946, 2.86678, 1.63852])
    upper_bound = [2, 3, 1, 10, 10, 15, 10, 5]
    lower_bound = [1e-3, 1e-2, 0, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None, None, None]
    print "The IMpre  allows for population size changes before and after species split"
    print "The parameters are: (nuPre,TPre,s,nu1,nu2,T,m12,m21)"
    print "The initial parameters are: ", params

  #14 anc_asym_mig, asym mig during the early stage of divergence, then strict isolation
  if demographic == 'anc_asym_mig': 
    pts_l = [50,60,70]
    func =  Demographics2D.IM_pre
    params = array([1, 1, 1, 1, 1, 1])
    upper_bound = [100, 100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None, None]
    print "The anc_asym_mig allows asym mig during the early stage of divergence, then strict isolation"
    print "The parameters are: (nu1, nu2, m12, m21, T1, T2)"
    print "The initial parameters are: ", params

  #15 anc_sym_mig, sym mig during the early stage of divergence, then strict isolation
  if demographic == 'anc_sym_mig': 
    pts_l = [50,60,70]
    func =  Demographics2D.IM_pre
    params = array([1, 1, 1, 1, 1])
    upper_bound = [100, 100, 100, 100, 100]
    lower_bound = [1e-2, 1e-2, 1e-2, 1e-2, 1e-2]
    fixed_params = [None, None, None, None, None]
    print "The anc_sym_mig allows sym mig during the early stage of divergence, then strict isolation"
    print "The parameters are: (nu1, nu2, m, T1, T2)"
    print "The initial parameters are: ", params



  # Makde the extrapolating version of our demographic model function.
  func_ex = dadi.Numerics.make_extrap_log_func(func)
  model = func_ex(params, ns, pts_l)
  ll_model = dadi.Inference.ll_multinom(model, data)
  print 'Model log-likelihood:', ll_model
  theta = dadi.Inference.optimal_sfs_scaling(model, data)
  print 'Model estimated theta = ', theta
  f = open("./IM_pre", 'a')
  p0 = dadi.Misc.perturb_params(params, fold=1, upper_bound=upper_bound)
  if migration == 'True':
    popt = dadi.Inference.optimize_log(p0, data, func_ex, pts_l, lower_bound=lower_bound, upper_bound=upper_bound, verbose=len(params),maxiter=5000)
  else:
    popt = dadi.Inference.optimize_log(p0, data, func_ex, pts_l, fixed_params = fixed_params,  lower_bound=lower_bound, upper_bound=upper_bound, verbose=len(params),maxiter=5000)
  print >>f,  'Model log-likelihood:', ll_model , 'Model estimated theta = ', theta ,"The optimized parameters are: ", popt ,'\n',
  
# Plot a comparison of the resulting fs with the data.
# import pylab
# pylab.figure(1)
# dadi.Plotting.plot_2d_comp_multinom(model, data, vmin=0.05, resid_range=300, pop_ids =('high','low'))
# pylab.savefig('tree_sparrow.png', dpi=300)
  #import matplotlib
  import matplotlib.pyplot as pyplot
  #pyplot.switch_backend('agg')
  pyplot.figure(1)
  dadi.Plotting.plot_2d_comp_multinom(model, data, vmin=0.05)
  pyplot.show()

def main(argv):
  if len(argv)<5:
    print "Model to run with DADI_Simulation_demographic_models.py" 
    print "Usage: DADI-Simulation.py <input file><demographic(Isolation-Migration/Bottleneck-NonBottleneck/Twopop-Bottleneck-Model)><polarized(True/False)><migration(True/False)>"
    exit(2)
  inputfile = argv[1]
  demographic = argv[2]
  polarized = argv[3]
  migration = argv[4]
  dadi_estimation(inputfile, demographic, polarized, migration)
  
if __name__=='__main__':
  main(sys.argv)



# Plot a comparison of the resulting fs with the data.
# import matplotlib.pyplot as pyplot
# pyplot.figure()
# dadi.Plotting.plot_2d_comp_multinom(model, data, vmin=0.05)
# pyplot.savefig('tree_sparrow.png', dpi=300)





# Plot a comparison of the resulting fs with the data.
# import pylab
# pylab.figure(1)
# dadi.Plotting.plot_2d_comp_multinom(SI, data, vmin=0.05, resid_range=300,pop_ids =('high','low'))
# pylab.savefig('fig.png', dpi=300)
