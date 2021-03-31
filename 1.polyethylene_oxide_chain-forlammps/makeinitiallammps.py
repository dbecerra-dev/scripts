#####################################################
#                                                   #
#                                                   #
# Filename: makeinitiallammps.py                    #
# Author: Diego Becerra, 2018                       #
#                                                   #
# Characteristics: Initial input file for atomistic #
# polymeric peo chains for simulation in Lammps     #
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
General functions
"""
import sys

# Defining classes to facilitate analysis

class Status:
    def __init__(self,id,mol,type,charge,x,y,z,zero1,zero2,zero3):
        self.id = id
        self.mol = mol
        self.type = type
        self.charge = charge
        self.x = x
        self.y = y
        self.z = z
        self.zero1 = zero1
        self.zero2 = zero2
        self.zero3 = zero3

class Bond:
    def __init__(self,type,a,b):
        self.type = type
        self.a = a
        self.b = b

class Angle:
    def __init__(self,type,a,b,c):
        self.type = type
        self.a = a
        self.b = b
        self.c = c

class Dihedral:
    def __init__(self,type,a,b,c,d):
        self.type = type
        self.a = a
        self.b = b
        self.c = c
        self.d = d

class LmpConf:
    def __init__(self):
        self.xlo = None
        self.xhi = None
        self.ylo = None
        self.yhi = None
        self.zlo = None
        self.yhi = None
        self.nAtoms = None
        self.nBonds = None
        self.nAngles = None
        self.nDihedrals = None
        self.nAtomTypes = None
        self.nBondTypes = None
        self.nAngleTypes = None
        self.nDihedralTypes = None
        self.mass = []
        self.atoms = []
        self.velocities = []
        self.bonds = []
        self.angles = []
        self.dihedrals = []
        self.bonddata = []
        self.angledata = []
        self.dihedraldata = []
        self.blen = []
        self.bhlf = []
        self.blni = []
        self.typeatom = [] #Saves atom types
        self.typeangle = [] #Saves angle types
        self.typebond = [] #Saves bond types
        self.typedihedral = [] #Saves dihedral (torsion) types
        self.typemass = [] #Saves mass by type
        self.nStatus = None
        self.nStatusTypes = None
        self.status = []
        self.statusdata = []

    def initialize_box(self):
        self.blen.append(abs(self.xhi-self.xlo))
        self.blen.append(abs(self.yhi-self.ylo))
        self.blen.append(abs(self.zhi-self.zlo))
        for i in range(3):
            self.bhlf.append(self.blen[i]/2.0)
            self.blni.append(1.0/self.blen[i])

    def apply_pbcs(self,dr,dim):
        if dr > self.bhlf[dim]:
            dr = dr - self.blen[dim] * float(int(dr * self.blni[dim] + 0.5))
        elif dr < -self.bhlf[dim]:
            dr = dr - self.blen[dim] * float(int(dr * self.blni[dim] - 0.5))
        return dr




    def write_configuration_file(self,outFile):
        numberofatoms=70781               #total number of atoms (insert a number from peoxide.in)
        numberofbonds=70744               #total bonds of one chain * number of chains ((8+7(number of monomers per chain-1))*37)
        numberofangles=131313             #total angles of one chain * number of chains ((13+13(number of monomers per chain-1))*37)
        numberofdihedrals=151182          #total dihedrals of one chain * number of chains ((6+15(number of monomers per chain-1))*37)
        atomtypes=4
        bondtypes=3
        angletypes=5
        dihedraltypes=5
        axis=88.671081977                 # len of axis of the cubic box (insert a number from peoxide.in)

        file = open(outFile,"w")
        file.write("LAMMPS configuration file modified using lmp_io\n\n")
        file.write("\t%ld atoms\n" % numberofatoms)
        file.write("\t%ld bonds\n" % numberofbonds)
        file.write("\t%ld angles\n" % numberofangles)
        file.write("\t%ld dihedrals\n\n" % numberofdihedrals)
        file.write("\t%ld atom types\n" % atomtypes)
        file.write("\t%ld bond types\n" % bondtypes)
        file.write("\t%ld angle types\n" % angletypes)
        file.write("\t%ld dihedral types\n\n" % dihedraltypes)
        file.write("\t%lf\t%lf xlo xhi\n" % (0,axis))
        file.write("\t%lf\t%lf ylo yhi\n" % (0,axis))
        file.write("\t%lf\t%lf zlo zhi\n\n" % (0,axis))


        file.write("Masses\n\n")
        massoxygen=15.999000
        masscarbon1=12.010700
        masscarbon2=12.010700
        masshydrogen=1.007940
        file.write("\t%ld\t%lf\n" % (1,massoxygen))
        file.write("\t%ld\t%lf\n" % (2,masscarbon1))
        file.write("\t%ld\t%lf\n" % (3,masscarbon2))
        file.write("\t%ld\t%lf\n" % (4,masshydrogen))
        file.write("\n")


        file.write("Atoms\n\n")
        #id,mol,type,charge,x,y,z,0,0,0
        axisx=0
        axisy=0
        axisz=0
        mol=0
        for i in range(0,37):                           # Number of chains (insert a number from properties.ods)
            mol+=1
            for j in range(0,273):                      # Number of monomers per chain (insert a number from properties.ods)
                if j==0:
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(2),float(-0.1187),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(1),float(-0.2792),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(3),float(-0.0326),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                elif j==272:    #Last number of range
                    self.status.append(Status(1,int(mol),int(3),float(-0.0326),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(1),float(-0.2792),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(2),float(-0.1187),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                else:
                    self.status.append(Status(1,int(mol),int(3),float(-0.0326),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(1),float(-0.2792),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(3),float(-0.0326),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))
                    self.status.append(Status(1,int(mol),int(4),float(0.0861),float(0),float(0),float(0),int(0),int(0),int(0)))

        contador=0
        for k in range(len(self.status)):
            c=self.status[k]
            contador+=1
            file.write("\t%ld\t%ld\t%ld\t%lf\t%lf\t%lf\t%lf\t%d\t%d\t%d\n" % (contador,c.mol,c.type,c.charge,axisx,axisy,axisz,0,0,0))
        file.write("\n")




        file.write("Velocities\n\n")
        for i in range(0,70781):                                   # Number of atoms (insert a number from properties.ods)
            file.write("\t%ld\t%lf\t%lf\t%lf\n" % (i+1,0,0,0))
        file.write("\n")

        napc=1913        # insert the number of atoms per chain: 70781/37=1913

        file.write("Bonds\n\n")
        #id,type,id1,id2

        for i in range(0,37):         # Number of chains (insert a number from properties.ods)
            contbond=-1
            for j in range(0,273):    # Number of monomers per chain (insert a number from properties.ods)
                contbond+=1
                if j==0:
                    self.bonds.append(Bond(1,int((contbond+1)+(i*napc)),int((contbond+4)+(i*napc))))
                    self.bonds.append(Bond(1,int((contbond+2)+(i*napc)),int((contbond+4)+(i*napc))))
                    self.bonds.append(Bond(1,int((contbond+3)+(i*napc)),int((contbond+4)+(i*napc))))
                    self.bonds.append(Bond(2,int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc))))
                    self.bonds.append(Bond(2,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc))))
                    self.bonds.append(Bond(1,int((contbond+6)+(i*napc)),int((contbond+7)+(i*napc))))
                    self.bonds.append(Bond(1,int((contbond+6)+(i*napc)),int((contbond+8)+(i*napc))))
                    self.bonds.append(Bond(3,int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc))))
                elif j==272:        #Last number of range minus one
                    self.bonds.append(Bond(1,int((7*contbond+2)+(i*napc)),int((7*contbond+3)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+2)+(i*napc)),int((7*contbond+4)+(i*napc))))
                    self.bonds.append(Bond(2,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.bonds.append(Bond(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+6)+(i*napc)),int((7*contbond+7)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                else:
                    self.bonds.append(Bond(1,int((7*contbond+2)+(i*napc)),int((7*contbond+3)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+2)+(i*napc)),int((7*contbond+4)+(i*napc))))
                    self.bonds.append(Bond(2,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.bonds.append(Bond(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+6)+(i*napc)),int((7*contbond+7)+(i*napc))))
                    self.bonds.append(Bond(1,int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.bonds.append(Bond(3,int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))

        contador=0
        for k in range(len(self.bonds)):
            c=self.bonds[k]
            contador+=1
            file.write("\t%ld\t%ld\t%ld\t%d\n" % (contador,c.type,c.a,c.b))
        file.write("\n")


        file.write("Angles\n\n")
        #id,type,id1,id2,id3

        for i in range(0,37):                          # Number of chains (insert a number)
            contbond=-1
            for j in range(0,273):                      # Number of monomers per chain (insert a number from properties.ods)
                contbond+=1
                if j==0:
                    self.angles.append(Angle(1,int((contbond+1)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+2)+(i*napc))))
                    self.angles.append(Angle(1,int((contbond+1)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+3)+(i*napc))))
                    self.angles.append(Angle(1,int((contbond+2)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+3)+(i*napc))))
                    self.angles.append(Angle(2,int((contbond+1)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc))))
                    self.angles.append(Angle(2,int((contbond+2)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc))))
                    self.angles.append(Angle(2,int((contbond+3)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc))))
                    self.angles.append(Angle(3,int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc))))
                    self.angles.append(Angle(2,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+7)+(i*napc))))
                    self.angles.append(Angle(2,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+8)+(i*napc))))
                    self.angles.append(Angle(4,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc))))
                    self.angles.append(Angle(1,int((contbond+7)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+8)+(i*napc))))
                    self.angles.append(Angle(5,int((contbond+7)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc))))
                    self.angles.append(Angle(5,int((contbond+8)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc))))
                elif j==272:              #Last number of range minus one
		    self.angles.append(Angle(5,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+3)+(i*napc))))
                    self.angles.append(Angle(5,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+4)+(i*napc))))
                    self.angles.append(Angle(1,int((7*contbond+3)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+4)+(i*napc))))
                    self.angles.append(Angle(4,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+3)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+4)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.angles.append(Angle(3,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+7)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                    self.angles.append(Angle(1,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.angles.append(Angle(1,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                    self.angles.append(Angle(1,int((7*contbond+8)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                else:
                    self.angles.append(Angle(5,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+3)+(i*napc))))
                    self.angles.append(Angle(5,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+4)+(i*napc))))
                    self.angles.append(Angle(1,int((7*contbond+3)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+4)+(i*napc))))
                    self.angles.append(Angle(4,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+3)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+4)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc))))
                    self.angles.append(Angle(3,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+7)+(i*napc))))
                    self.angles.append(Angle(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.angles.append(Angle(4,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                    self.angles.append(Angle(1,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.angles.append(Angle(5,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                    self.angles.append(Angle(5,int((7*contbond+8)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))

        contador=0
        for k in range(len(self.angles)):
            c=self.angles[k]
            contador+=1
            file.write("\t%ld\t%ld\t%ld\t%d\t%d\n" % (contador,c.type,c.a,c.b,c.c))
        file.write("\n")


        file.write("Dihedrals\n\n")
        #id,type,id1,id2,id3

        for i in range(0,37):                          # Number of chains (insert a number)
            contbond=-1
            for j in range(0,273):                      # Number of monomers per chain (insert a number)
                contbond+=1
                if j==0:
                    self.dihedrals.append(Dihedral(1,int((contbond+1)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((contbond+2)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((contbond+3)+(i*napc)),int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+7)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+8)+(i*napc))))
                    self.dihedrals.append(Dihedral(5,int((contbond+4)+(i*napc)),int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+10)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+11)+(i*napc))))
                    self.dihedrals.append(Dihedral(4,int((contbond+5)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+12)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((contbond+7)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+10)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((contbond+7)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+11)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((contbond+7)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+12)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((contbond+8)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+10)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((contbond+8)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+11)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((contbond+8)+(i*napc)),int((contbond+6)+(i*napc)),int((contbond+9)+(i*napc)),int((contbond+12)+(i*napc))))
                elif j==272:          #Last number of range minus one
                    self.dihedrals.append(Dihedral(5,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+3)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+4)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+7)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                else:
                    self.dihedrals.append(Dihedral(5,int((7*contbond-1)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+3)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+4)+(i*napc)),int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+7)+(i*napc))))
                    self.dihedrals.append(Dihedral(1,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+8)+(i*napc))))
                    self.dihedrals.append(Dihedral(5,int((7*contbond+2)+(i*napc)),int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+10)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+11)+(i*napc))))
                    self.dihedrals.append(Dihedral(4,int((7*contbond+5)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+12)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+10)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+11)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((7*contbond+7)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+12)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((7*contbond+8)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+10)+(i*napc))))
                    self.dihedrals.append(Dihedral(3,int((7*contbond+8)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+11)+(i*napc))))
                    self.dihedrals.append(Dihedral(2,int((7*contbond+8)+(i*napc)),int((7*contbond+6)+(i*napc)),int((7*contbond+9)+(i*napc)),int((7*contbond+12)+(i*napc))))


        contador=0
        for k in range(len(self.dihedrals)):
            c=self.dihedrals[k]
            contador+=1
            file.write("\t%ld\t%ld\t%ld\t%d\t%d\t%d\n" % (contador,c.type,c.a,c.b,c.c,c.d))
        file.close()




def get_command_line_args(args):
    if len(args) != 2:
        print "Usage: %s <LAMMPS configuation file> <output file>"  % args[0]
        sys.exit(1)
    return args

def main():
    args = get_command_line_args(sys.argv)
    lmpconf = LmpConf()

    lmpconf.write_configuration_file(args[1])


if __name__ == "__main__":
    main()
