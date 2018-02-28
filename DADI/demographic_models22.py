#!/usr/bin/home python

# This file contains the updated demographic models that we will use to test our 2DSDS
# The 1D SFS analyses suggests that the CYP&PNG pops have gone through two epochs with instantaenous size change. 
import numpy
import dadi

# Strict isolation - no migration - 2 epochs

def SI(params,ns,pts):
	nu1,nu2,T= params

	xx = dadi.Numerics.default_grid(pts)

	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	phi = dadi.Integration.two_pops(phi,xx,T,nu1,nu2)

	fs = dadi.Spectrum.from_phi(phi,ns,(xx,xx))
	return fs

# Isolation-with-migration with equal migration

def IM_sym(params,ns,pts):
	nu1,nu2,T,m = params

	xx = dadi.Numerics.default_grid(pts)

	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

	phi = dadi.Integration.two_pops(phi,xx,T,nu1,nu2,m12=m,m21=m)

	fs = dadi.Spectrum.from_phi(phi,ns,(xx,xx))
	return fs

# Secondary contact with equal migration

def SC_sym(params,ns,pts):
	nu1,nu2,Ta,Tc,m= params

	xx = dadi.Numerics.default_grid(pts)

	phi = dadi.PhiManip.phi_1D(xx)
	phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)
	phi = dadi.Integration.two_pops(phi,xx,Ta,nu1,nu2,m12=0,m21=0)

	phi = dadi.Integration.two_pops(phi,xx,Tc,nu1,nu2,m12=m,m21=m)


	fs = dadi.Spectrum.from_phi(phi,ns,(xx,xx))
	return fs

def IM_asym(params,ns,pts):
        nu1,nu2,T,m12,m21 = params

        xx = dadi.Numerics.default_grid(pts)

        phi = dadi.PhiManip.phi_1D(xx)
        phi = dadi.PhiManip.phi_1D_to_2D(xx,phi)

        phi = dadi.Integration.two_pops(phi,xx,T,nu1,nu2,m12=m12,m21=m21)

        fs = dadi.Spectrum.from_phi(phi,ns,(xx,xx))
        return fs