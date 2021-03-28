#####################################################
#                                                   #
#                                                   #
# Filename: peoxide.py                              #
# Author: Diego Becerra, 2018                       #
#                                                   #
# Characteristics: Initial configuration of         #
# atomistic polymeric peo chains                    #
#                                                   #
#                                                   #
#                                                   #
#                                                   #
#                                                   #
# Updated to August, 2018                           #
#                                                   #
#                                                   #
#####################################################
#!/usr/bin/env python

"""
# General functions
"""
import sys
import math
import numpy as np

from scipy.stats import uniform
import random
from scipy import stats
from scipy import constants
import seaborn as sns
from pyquaternion import Quaternion

# Defining classes to facilitate analysis
class Status:
    def __init__(self,type,mol,x,y,z,axis):
        self.type = type
        self.mol = mol
        self.x = x
        self.y = y
        self.z = z
        self.axis = axis

class Statusfinal:
    def __init__(self,type,mol,x,y,z,axis):
        self.type = type
        self.mol = mol
        self.x = x
        self.y = y
        self.z = z
        self.axis = axis

class LmpConf:
    def __init__(self):
        self.axis = None
        self.xlo = None
        self.xhi = None
        self.ylo = None
        self.yhi = None
        self.zlo = None
        self.yhi = None
        self.nAtoms = None
        self.nBonds = None
        self.nAngles = None
        self.nTorsions = None
        self.nAtomTypes = None
        self.nBondTypes = None
        self.nAngleTypes = None
        self.nTorsionTypes = None
        self.mass = []
        self.atoms = []
        self.velocities = []
        self.bonds = []
        self.angles = []
        self.torsions = []
        self.molecules =[]
        self.bonddata = []
        self.angledata = []
        self.torsiondata = []
        self.blen = []
        self.bhlf = []
        self.blni = []
        self.typeatom = [] #Saves atom types
        self.typeangle = [] #Saves angle types
        self.typebond = [] #Saves bond types
        self.typetorsion = [] #Saves torsion types
        self.typemass = [] #Saves mass by type
        self.nVector = None
        self.vector = []
        self.masa = []
        self.axisx = []
        self.axisy = []
        self.axisz = []
        self.axiscarbono = []
        self.vector2 = []
        self.nStatus = None
        self.nStatusTypes = None
        self.status = []
        self.statusdata = []
        self.nStatusfinal = None
        self.nStatusTypes = None
        self.statusfinal = []
        self.paso = None
        self.aleatorios = []

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Initial configuration polyethylene oxide
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def initialconfiguration(self):
     nch=37                            # number of chains
     for a in range(0,nch):
        print a
        molec=a                        # number of molecule (polymer chain)
        lcc=0.15075                    # distance between carbons [nm]
        lco=0.14115                    # distance between carbon and oxygen [nm]
        lh=0.11041                     # distance between hydrogens and carbons [nm]
        theta1=71.46*math.pi/180       # rotation angle 1 C-C-O, restriction [rad]
        theta2=71.95*math.pi/180       # rotation angle 2 C-O-C, restriction [rad]
        Nav=6.022140857e+23            # Avogadro constant [mol^-1]
        ro=1.06                        # density of polymer [g/cm^3]
        temperature=348.15             # temperature [K]
        nmpc=273                       # number of monomers per chain
        nch=37                         # number of chains
        Mwc=12028.212                  # molecular weight of each chain (2.016+44.052*nmpc [g/mol])
        TMw=Mwc*nch                    # total molecular weight (MWc*nch [g/mol])
        Tm=TMw/Nav                     # total mass of chains of polymer (TMw/Nav [g])
        V=Tm/ro*1e+21                  # box volume [nm^3]
        axis=V**(float(1)/float(3))    # cubic box axis [nm]

#####################################################################################################################
########################################### First monomer ###########################################################
#####################################################################################################################
        # First carbon (with random position in the space inside the box)
        fcx = np.random.uniform(0.8,axis-0.8)
        fcy = np.random.uniform(0.8,axis-0.8)
        fcz = np.random.uniform(0.8,axis-0.8)
        first_carbon = (fcx,fcy,fcz)

        # Random vector in the space (from the origin)
        rv0x = np.random.uniform(-axis,axis)
        rv0y = np.random.uniform(-axis,axis)
        rv0z = np.random.uniform(-axis,axis)
        rv0 = (rv0x,rv0y,rv0z)

        # Normalized Vector between the random vector 0 and the first carbon
        dx = np.subtract(rv0x,fcx)
        dy = np.subtract(rv0y,fcy)
        dz = np.subtract(rv0z,fcz)
        module=math.sqrt(dx**2+dy**2+dz**2)

        rotated_vector=(dx/module, dy/module, dz/module)

        # First oxygen (at lco nm of the first carbon)
        fox = fcx+rotated_vector[0]*lco
        foy = fcy+rotated_vector[1]*lco
        foz = fcz+rotated_vector[2]*lco
        first_oxygen = (fox,foy,foz)

        # Normalized Vector between the first oxygen and the first carbon
        dx = np.subtract(fox,fcx)
        dy = np.subtract(foy,fcy)
        dz = np.subtract(foz,fcz)
        module=math.sqrt(dx**2+dy**2+dz**2)

        rotated_vector=(dx/module, dy/module, dz/module)

        # Normalized random vector for the cross product (step 1)
        rv1x = np.random.uniform(-axis,axis)
        rv1y = np.random.uniform(-axis,axis)
        rv1z = np.random.uniform(-axis,axis)
        rv1 = (rv1x,rv1y,rv1z)
        norm = math.sqrt(rv1x**2+rv1y**2+rv1z**2)
        rv1_norm = (rv1x/norm,rv1y/norm,rv1z/norm)

        # Cross Product (step 2)
        crossx=rotated_vector[1]*rv1z/norm-rotated_vector[2]*rv1y/norm
        crossy=-(rotated_vector[0]*rv1z/norm-rotated_vector[2]*rv1x/norm)
        crossz=rotated_vector[0]*rv1y/norm-rotated_vector[1]*rv1x/norm
        crossvector=(crossx, crossy, crossz)

        # Rotated vector (step 3)
        rotated_vector=Quaternion(axis=crossvector,angle=theta2).rotate(rotated_vector)

        # Second carbon (108.05 degrees with the first oxygen and the first carbon) (step 4)
        scx = fox+rotated_vector[0]*lco
        scy = foy+rotated_vector[1]*lco
        scz = foz+rotated_vector[2]*lco

        # Normalized Vector between the second carbon and the first oxygen (step 5)
        dx = np.subtract(scx,fox)
        dy = np.subtract(scy,foy)
        dz = np.subtract(scz,foz)
        module=math.sqrt(dx**2+dy**2+dz**2)

        rotated_vector=(dx/module, dy/module, dz/module)

        # Normalized Vector for the oxygen direction from the middle of the carbons (for the third hydrogen)

        oxygenunitx = fox-((scx-fcx)/2+fcx)
        oxygenunity = foy-((scy-fcy)/2+fcy)
        oxygenunitz = foz-((scz-fcz)/2+fcz)

        moduleoxygen=math.sqrt(oxygenunitx**2+oxygenunity**2+oxygenunitz**2)

        # vectors for plane C-O-C
        fofcx=fox-fcx
        fofcy=foy-fcy
        fofcz=foz-fcz
        scfox=scx-fox
        scfoy=scy-foy
        scfoz=scz-foz

        #i     j     k
        #fofcx fofcy fofcz
        #scfox scfoy scfoz

        # Cross Product
        xhx=fofcy*scfoz-fofcz*scfoy
        xhy=-(fofcx*scfoz-fofcz*scfox)
        xhz=fofcx*scfoy-fofcy*scfox
        normx = math.sqrt(xhx**2+xhy**2+xhz**2)
        xvector=(xhx/normx,xhy/normx,xhz/normx)

        # First hydrogen (in type 2 carbon)
        fhx1=scx+xhx/normx*lh
        fhy1=scy+xhy/normx*lh
        fhz1=scz+xhz/normx*lh
        first_hydrogen = (fhx1,fhy1,fhz1)

        # Second hydrogen (in type 2 carbon)
        shx1=scx-xhx/normx*lh
        shy1=scy-xhy/normx*lh
        shz1=scz-xhz/normx*lh
        second_hydrogen = (shx1,shy1,shz1)

        # First hydrogen (in type 3 carbon)
        h1x=fcx+xhx/normx*lh
        h1y=fcy+xhy/normx*lh
        h1z=fcz+xhz/normx*lh
        first_hydrogen = (h1x,h1y,h1z)

        # Second hydrogen (in type 3 carbon)
        h2x=fcx-xhx/normx*lh
        h2y=fcy-xhy/normx*lh
        h2z=fcz-xhz/normx*lh
        second_hydrogen = (h2x,h2y,h2z)

        # Third hydrogen  (in type 3 carbon)
        h3x=fcx+oxygenunitx/moduleoxygen*lh
        h3y=fcy+oxygenunity/moduleoxygen*lh
        h3z=fcz+oxygenunitz/moduleoxygen*lh
        third_hydrogen = (h3x,h3y,h3z)

        self.status.append(Status(int(4),int(molec),float(h1x),float(h1y),float(h1z),float(axis)))
        self.status.append(Status(int(4),int(molec),float(h2x),float(h2y),float(h2z),float(axis)))
        self.status.append(Status(int(4),int(molec),float(h3x),float(h3y),float(h3z),float(axis)))
        self.status.append(Status(int(2),int(molec),float(fcx),float(fcy),float(fcz),float(axis)))
        self.status.append(Status(int(1),int(molec),float(fox),float(foy),float(foz),float(axis)))
        self.status.append(Status(int(3),int(molec),float(scx),float(scy),float(scz),float(axis)))
        self.status.append(Status(int(4),int(molec),float(fhx1),float(fhy1),float(fhz1),float(axis)))
        self.status.append(Status(int(4),int(molec),float(shx1),float(shy1),float(shz1),float(axis)))

#####################################################################################################################
########################################### monomers in polymer #####################################################
#####################################################################################################################

        while len(self.status)<(8*(a+1))+(7*(nmpc-2)*(a+1))+(8*a):  #

            # Normalized random vector for the cross product (step 1)
            rv2x = np.random.uniform(-axis,axis)
            rv2y = np.random.uniform(-axis,axis)
            rv2z = np.random.uniform(-axis,axis)
            rv2 = (rv2x,rv2y,rv2z)
            norm = math.sqrt(rv2x**2+rv2y**2+rv2z**2)
            rv2_norm = (rv2x/norm,rv2y/norm,rv2z/norm)

            # Cross Product (step 2)
            crossx=rotated_vector[1]*rv2z/norm-rotated_vector[2]*rv2y/norm
            crossy=-(rotated_vector[0]*rv2z/norm-rotated_vector[2]*rv2x/norm)
            crossz=rotated_vector[0]*rv2y/norm-rotated_vector[1]*rv2x/norm
            crossvector=(crossx, crossy, crossz)

            # Rotated vector (step 3)
            rotated_vector=Quaternion(axis=crossvector,angle=theta1).rotate(rotated_vector)

            # Third carbon (108.54 degrees with the second carbon and the first oxygen) (step 4)
            tcx = scx+rotated_vector[0]*lcc
            tcy = scy+rotated_vector[1]*lcc
            tcz = scz+rotated_vector[2]*lcc

            # Normalized Vector between the third carbon and the second carbon (step 5)
            dx = np.subtract(tcx,scx)
            dy = np.subtract(tcy,scy)
            dz = np.subtract(tcz,scz)
            module=math.sqrt(dx**2+dy**2+dz**2)

            rotated_vector=(dx/module, dy/module, dz/module)

            # Normalized random vector for the cross product (step 1)
            rv3x = np.random.uniform(-axis,axis)
            rv3y = np.random.uniform(-axis,axis)
            rv3z = np.random.uniform(-axis,axis)
            rv3 = (rv3x,rv3y,rv3z)
            norm = math.sqrt(rv3x**2+rv3y**2+rv3z**2)
            rv3_norm = (rv3x/norm,rv3y/norm,rv3z/norm)

            # Cross Product (step 2)
            crossx=rotated_vector[1]*rv3z/norm-rotated_vector[2]*rv3y/norm
            crossy=-(rotated_vector[0]*rv3z/norm-rotated_vector[2]*rv3x/norm)
            crossz=rotated_vector[0]*rv3y/norm-rotated_vector[1]*rv3x/norm
            crossvector=(crossx, crossy, crossz)

            # Rotated vector (step 3)
            rotated_vector=Quaternion(axis=crossvector,angle=theta1).rotate(rotated_vector)

            # Second oxygen (108.54 degrees with the third carbon and the second carbon) (step 4)
            sox = tcx+rotated_vector[0]*lco
            soy = tcy+rotated_vector[1]*lco
            soz = tcz+rotated_vector[2]*lco

            # Normalized Vector between the second oxygen the third carbon (step 5)
            dx = np.subtract(sox,tcx)
            dy = np.subtract(soy,tcy)
            dz = np.subtract(soz,tcz)
            module=math.sqrt(dx**2+dy**2+dz**2)

            rotated_vector=(dx/module, dy/module, dz/module)

            # Normalized random vector for the cross product (step 1)
            rv4x = np.random.uniform(-axis,axis)
            rv4y = np.random.uniform(-axis,axis)
            rv4z = np.random.uniform(-axis,axis)
            rv4 = (rv4x,rv4y,rv4z)
            norm = math.sqrt(rv4x**2+rv4y**2+rv4z**2)
            rv4_norm = (rv4x/norm,rv4y/norm,rv4z/norm)

            # Cross Product (step 2)
            crossx=rotated_vector[1]*rv4z/norm-rotated_vector[2]*rv4y/norm
            crossy=-(rotated_vector[0]*rv4z/norm-rotated_vector[2]*rv4x/norm)
            crossz=rotated_vector[0]*rv4y/norm-rotated_vector[1]*rv4x/norm
            crossvector=(crossx, crossy, crossz)

            # Rotated vector (step 3)
            rotated_vector=Quaternion(axis=crossvector,angle=theta2).rotate(rotated_vector)

            # Fourth carbon (108.05 degrees with the second oxygen and the third carbon) (step 4)
            focx = sox+rotated_vector[0]*lco
            focy = soy+rotated_vector[1]*lco
            focz = soz+rotated_vector[2]*lco

            # Normalized Vector between the third carbon and the second carbon (step 5)
            dx = np.subtract(focx,sox)
            dy = np.subtract(focy,soy)
            dz = np.subtract(focz,soz)
            module=math.sqrt(dx**2+dy**2+dz**2)

            rotated_vector=(dx/module, dy/module, dz/module)

            # vectors for plane C-O-C
            sotcx=sox-tcx
            sotcy=soy-tcy
            sotcz=soz-tcz
            focsox=focx-sox
            focsoy=focy-soy
            focsoz=focz-soz

            #i     j     k
            #sotcx sotcy sotcz
            #focsox focsoy focsoz

            # Cross Product
            xxhx=sotcy*focsoz-sotcz*focsoy
            xxhy=-(sotcx*focsoz-sotcz*focsox)
            xxhz=sotcx*focsoy-sotcy*focsox
            normxx = math.sqrt(xxhx**2+xxhy**2+xxhz**2)
            xxvector=(xxhx/normxx,xxhy/normxx,xxhz/normxx)

            # First hydrogen (in type 2 carbon)
            fhx2=tcx+xxhx/normxx*lh
            fhy2=tcy+xxhy/normxx*lh
            fhz2=tcz+xxhz/normxx*lh
            first_hydrogen = (fhx2,fhy2,fhz2)

            # Second hydrogen (in type 2 carbon)
            shx2=tcx-xxhx/normxx*lh
            shy2=tcy-xxhy/normxx*lh
            shz2=tcz-xxhz/normxx*lh
            second_hydrogen = (shx2,shy2,shz2)

            # First hydrogen (in type 2 carbon)
            fhx3=focx+xxhx/normxx*lh
            fhy3=focy+xxhy/normxx*lh
            fhz3=focz+xxhz/normxx*lh
            first_hydrogen = (fhx3,fhy3,fhz3)

            # Second hydrogen (in type 2 carbon)
            shx3=focx-xxhx/normxx*lh
            shy3=focy-xxhy/normxx*lh
            shz3=focz-xxhz/normxx*lh
            second_hydrogen = (shx3,shy3,shz3)

            if 0.2<tcx<(axis-0.2) and 0.2<tcy<(axis-0.2) and 0.2<tcz<(axis-0.2) and 0.2<focx<(axis-0.2) and 0.2<focy<(axis-0.2) and 0.2<focz<(axis-0.2) and 0.2<sox<(axis-0.2) and 0.2<soy<(axis-0.2) and 0.2<soz<(axis-0.2) and 0.2<fhx2<(axis-0.2) and 0.2<fhy2<(axis-0.2) and 0.2<fhz2<(axis-0.2) and 0.2<shx2<(axis-0.2) and 0.2<shy2<(axis-0.2) and 0.2<shz2<(axis-0.2) and 0.2<fhx3<(axis-0.2) and 0.2<fhy3<(axis-0.2) and 0.2<fhz3<(axis-0.2) and 0.2<shx3<(axis-0.2) and 0.2<shy3<(axis-0.2) and  0.2<shz3<(axis-0.2):
                scx=focx
                scy=focy
                scz=focz
                self.status.append(Status(int(3),int(molec),float(tcx),float(tcy),float(tcz),float(axis)))
                self.status.append(Status(int(4),int(molec),float(fhx2),float(fhy2),float(fhz2),float(axis)))
                self.status.append(Status(int(4),int(molec),float(shx2),float(shy2),float(shz2),float(axis)))
                self.status.append(Status(int(1),int(molec),float(sox),float(soy),float(soz),float(axis)))
                self.status.append(Status(int(3),int(molec),float(scx),float(scy),float(scz),float(axis)))
                self.status.append(Status(int(4),int(molec),float(fhx3),float(fhy3),float(fhz3),float(axis)))
                self.status.append(Status(int(4),int(molec),float(shx3),float(shy3),float(shz3),float(axis)))

#####################################################################################################################
########################################### Last monomer ############################################################
#####################################################################################################################

        while len(self.status)<(8*(a+1))+(7*(nmpc-2)*(a+1))+(8*(a+1)):

            # Normalized random vector for the cross product (step 1)
            rv5x = np.random.uniform(-axis,axis)
            rv5y = np.random.uniform(-axis,axis)
            rv5z = np.random.uniform(-axis,axis)
            rv5 = (rv5x,rv5y,rv5z)
            norm = math.sqrt(rv5x**2+rv5y**2+rv5z**2)
            rv5_norm = (rv5x/norm,rv5y/norm,rv5z/norm)

            # Cross Product (step 2)
            crossx=rotated_vector[1]*rv5z/norm-rotated_vector[2]*rv5y/norm
            crossy=-(rotated_vector[0]*rv5z/norm-rotated_vector[2]*rv5x/norm)
            crossz=rotated_vector[0]*rv5y/norm-rotated_vector[1]*rv5x/norm
            crossvector=(crossx, crossy, crossz)

            # Rotated vector (step 3)
            rotated_vector=Quaternion(axis=crossvector,angle=theta1).rotate(rotated_vector)

            # Penultimate carbon (108.54 degrees with the antepenultimate carbon and the previous oxygen) (step 4)
            pcx = scx+rotated_vector[0]*lcc
            pcy = scy+rotated_vector[1]*lcc
            pcz = scz+rotated_vector[2]*lcc

            # Normalized Vector between the penultimate carbon and the antepenultimate carbon (step 5)
            dx = np.subtract(pcx,scx)
            dy = np.subtract(pcy,scy)
            dz = np.subtract(pcz,scz)
            module=math.sqrt(dx**2+dy**2+dz**2)

            rotated_vector=(dx/module, dy/module, dz/module)

            # Normalized random vector for the cross product (step 1)
            rv6x = np.random.uniform(-axis,axis)
            rv6y = np.random.uniform(-axis,axis)
            rv6z = np.random.uniform(-axis,axis)
            rv6 = (rv6x,rv6y,rv6z)
            norm = math.sqrt(rv6x**2+rv6y**2+rv6z**2)
            rv6_norm = (rv6x/norm,rv6y/norm,rv6z/norm)

            # Cross Product (step 2)
            crossx=rotated_vector[1]*rv6z/norm-rotated_vector[2]*rv6y/norm
            crossy=-(rotated_vector[0]*rv6z/norm-rotated_vector[2]*rv6x/norm)
            crossz=rotated_vector[0]*rv6y/norm-rotated_vector[1]*rv6x/norm
            crossvector=(crossx, crossy, crossz)

            # Rotated vector (step 3)
            rotated_vector=Quaternion(axis=crossvector,angle=theta1).rotate(rotated_vector)

            # Last oxygen (108.54 degrees with the penultimate carbon and the antepenultimate carbon) (step 4)
            lox = pcx+rotated_vector[0]*lco
            loy = pcy+rotated_vector[1]*lco
            loz = pcz+rotated_vector[2]*lco

            # Normalized Vector between the last oxygen and the penultimate carbon (step 5)
            dx = np.subtract(lox,pcx)
            dy = np.subtract(loy,pcy)
            dz = np.subtract(loz,pcz)
            module=math.sqrt(dx**2+dy**2+dz**2)

            rotated_vector=(dx/module, dy/module, dz/module)

            # Normalized random vector for the cross product (step 1)
            rv7x = np.random.uniform(-axis,axis)
            rv7y = np.random.uniform(-axis,axis)
            rv7z = np.random.uniform(-axis,axis)
            rv7 = (rv7x,rv7y,rv7z)
            norm = math.sqrt(rv7x**2+rv7y**2+rv7z**2)
            rv7_norm = (rv7x/norm,rv7y/norm,rv7z/norm)

            # Cross Product (step 2)
            crossx=rotated_vector[1]*rv7z/norm-rotated_vector[2]*rv7y/norm
            crossy=-(rotated_vector[0]*rv7z/norm-rotated_vector[2]*rv7x/norm)
            crossz=rotated_vector[0]*rv7y/norm-rotated_vector[1]*rv7x/norm
            crossvector=(crossx, crossy, crossz)

            # Rotated vector (step 3)
            rotated_vector=Quaternion(axis=crossvector,angle=theta2).rotate(rotated_vector)

            # Last carbon (108.05 degrees with the last oxygen and the penultimate carbon) (step 4)
            lcx = lox+rotated_vector[0]*lco
            lcy = loy+rotated_vector[1]*lco
            lcz = loz+rotated_vector[2]*lco

            # Normalized Vector for the oxygen direction from the middle of the carbons (for the third hydrogen)

            oxygenunitx = lox-((lcx-pcx)/2+pcx)
            oxygenunity = loy-((lcy-pcy)/2+pcy)
            oxygenunitz = loz-((lcz-pcz)/2+pcz)

            moduleoxygen=math.sqrt(oxygenunitx**2+oxygenunity**2+oxygenunitz**2)

            # vectors for plane C-O-C
            lopcx=lox-pcx
            lopcy=loy-pcy
            lopcz=loz-pcz
            lclox=lcx-lox
            lcloy=lcy-loy
            lcloz=lcz-loz

            #i     j     k
            #lopcx lopcy lopcz
            #lclox lcloy lcloz

            # Cross Product
            xxxhx=lopcy*lcloz-lopcz*lcloy
            xxxhy=-(lopcx*lcloz-lopcz*lclox)
            xxxhz=lopcx*lcloy-lopcy*lclox
            normxxx = math.sqrt(xxxhx**2+xxxhy**2+xxxhz**2)
            xxxvector=(xxxhx/normxxx,xxxhy/normxxx,xxxhz/normxxx)

            # First hydrogen (in type 2 carbon)
            fhx4=pcx+xxxhx/normxxx*lh
            fhy4=pcy+xxxhy/normxxx*lh
            fhz4=pcz+xxxhz/normxxx*lh
            first_hydrogen = (fhx4,fhy4,fhz4)

            # Second hydrogen (in type 2 carbon)
            shx4=pcx-xxxhx/normxxx*lh
            shy4=pcy-xxxhy/normxxx*lh
            shz4=pcz-xxxhz/normxxx*lh
            second_hydrogen = (shx4,shy4,shz4)

            # First hydrogen (in type 3 carbon)
            h4x=lcx+xxxhx/normxxx*lh
            h4y=lcy+xxxhy/normxxx*lh
            h4z=lcz+xxxhz/normxxx*lh
            fourth_hydrogen = (h4x,h4y,h4z)

            # Second hydrogen (in type 3 carbon)
            h5x=lcx-xxxhx/normxxx*lh
            h5y=lcy-xxxhy/normxxx*lh
            h5z=lcz-xxxhz/normxxx*lh
            fifth_hydrogen = (h5x,h5y,h5z)

            # Third hydrogen (in type 3 carbon)
            h6x=lcx+oxygenunitx/moduleoxygen*lh
            h6y=lcy+oxygenunity/moduleoxygen*lh
            h6z=lcz+oxygenunitz/moduleoxygen*lh
            sixth_hydrogen = (h6x,h6y,h6z)

            if 0.2<pcx<(axis-0.2) and 0.2<pcy<(axis-0.2) and 0.2<pcz<(axis-0.2) and 0.2<lcx<(axis-0.2) and 0.2<lcy<(axis-0.2) and 0.2<lcz<(axis-0.2) and 0.2<lox<(axis-0.2) and 0.2<loy<(axis-0.2)  and 0.2<loz<(axis-0.2) and 0.2<fhx4<(axis-0.2) and 0.2<fhy4<(axis-0.2) and 0.2<fhz4<(axis-0.2) and 0.2<shx4<(axis-0.2) and 0.2<shy4<(axis-0.2) and 0.2<shz4<(axis-0.2) and 0.2<h4x<(axis-0.2) and 0.2<h4y<(axis-0.2) and 0.2<h4z<(axis-0.2) and 0.2<h5x<(axis-0.2) and 0.2<h5y<(axis-0.2) and 0.2<h5z<(axis-0.2) and 0.2<h6x<(axis-0.2) and 0.2<h6y<(axis-0.2) and 0.2<h6z<(axis-0.2):
                scx=lcx
                scy=lcy
                scz=lcz
                self.status.append(Status(int(3),int(molec),float(pcx),float(pcy),float(pcz),float(axis)))
                self.status.append(Status(int(4),int(molec),float(fhx4),float(fhy4),float(fhz4),float(axis)))
                self.status.append(Status(int(4),int(molec),float(shx4),float(shy4),float(shz4),float(axis)))
                self.status.append(Status(int(1),int(molec),float(lox),float(loy),float(loz),float(axis)))
                self.status.append(Status(int(2),int(molec),float(scx),float(scy),float(scz),float(axis)))
                self.status.append(Status(int(4),int(molec),float(h4x),float(h4y),float(h4z),float(axis)))
                self.status.append(Status(int(4),int(molec),float(h5x),float(h5y),float(h5z),float(axis)))
                self.status.append(Status(int(4),int(molec),float(h6x),float(h6y),float(h6z),float(axis)))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WRITE
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def write_configuration_file_status(self,outFile):
        file = open(outFile,"w")
        line = self.nStatus
        for i in range(0,1):
            molec=1
            c=self.status[i]
            file.write("ITEM: TIMESTEP\n")
            file.write("%s\n" % int(0))
            file.write("ITEM: NUMBER OF ATOMS\n")
            file.write("%s\n" % (len(self.status)))
            file.write("ITEM: BOX BOUNDS pp pp pp\n")
            file.write("%s\t%s\n" % (float(0),c.axis*1e+1))
            file.write("%s\t%s\n" % (float(0),c.axis*1e+1))
            file.write("%s\t%s\n" % (float(0),c.axis*1e+1))
            file.write("ITEM: ATOMS id type x y z vx vy vz\n")
        for j in range(len(self.status)):
            c=self.status[j]
            file.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (j+1,c.type,c.x*1e+1,c.y*1e+1,c.z*1e+1,float(0),float(0),float(0)))

	file.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def get_command_line_args(args):
    if len(args) != 2:
        print "Usage: %s <input files> <output files>"  % args[0]
        sys.exit(1)
    return args

def main():
    args = get_command_line_args(sys.argv)
    lmpconf = LmpConf()
    lmpconf.initialconfiguration()
    lmpconf.write_configuration_file_status(args[1])

if __name__ == "__main__":
    main()
