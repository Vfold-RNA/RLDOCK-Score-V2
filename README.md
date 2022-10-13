# RLDOCK-Score-V2 - Refined RLDOCK scoring function for RNA-ligand pose prediction and virtual screening

## Platform Requirements (Tested)
The following are tested system settings, other hardware/software could also work but has not been tested.
* GNU/Linux x86_64 (Ubuntu 20.04.1 kernel 5.15.0-48-generic)
* gcc 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)
* Python 3.8.8
* CMake 3.16.3
* GNU Make 4.2.1

## Compile and test RLDOCK-Score-V2

### 1. Clone the repository
```
git clone https://github.com/Vfold-RNA/RLDOCK-Score-V2.git /home/${USER}/RLDOCK-Score-V2
```
### 2. Compile the code
Execute the following commands:
```
cd /home/${USER}/RLDOCK-Score-V2
cmake .
make
```
The executable *rldock_score_v2* can be found in folder **/home/${USER}/RLDOCK-Score-V2/bin/**.

### 3. Running the test
Use the following commands to test the newly compiled RLDOCK-Score-V2:
```
cd /home/${USER}/RLDOCK-Score-V2/test/2CKY-A-1084-TPP
python test.py
```

## Download data sets
The training set, pose prediction set, HIV-1 TAR/PreQ1 RS ensemble and compound library can be downloaded through the following commands:
```
mkdir -p /home/${USER}/RLDOCK-Score-V2/data/
wget https://github.com/Vfold-RNA/RLDOCK-Score-V2/releases/download/dataset/checksum.txt -O /home/${USER}/RLDOCK-Score-V2/data/checksum.txt
wget https://github.com/Vfold-RNA/RLDOCK-Score-V2/releases/download/dataset/training-set.tar.gz -O /home/${USER}/RLDOCK-Score-V2/data/training-set.tar.gz
wget https://github.com/Vfold-RNA/RLDOCK-Score-V2/releases/download/dataset/pose-prediciton-set.tar.gz -O /home/${USER}/RLDOCK-Score-V2/data/pose-prediciton-set.tar.gz
wget https://github.com/Vfold-RNA/RLDOCK-Score-V2/releases/download/dataset/HIV-1-TAR.tar.gz -O /home/${USER}/RLDOCK-Score-V2/data/HIV-1-TAR.tar.gz
wget https://github.com/Vfold-RNA/RLDOCK-Score-V2/releases/download/dataset/PreQ1-RS.tar.gz -O /home/${USER}/RLDOCK-Score-V2/data/PreQ1-RS.tar.gz
```
Check the integrity of the files:
```
cd /home/${USER}/RLDOCK-Score-V2/data/
sha256sum --check checksum.txt
```

## RLDOCK-Score-V2 command line arguments
```
-r <receptor>         # path to target RNA (in mol2 format, must contain hydrogens,
                        with AMBER ff14SB partial charges)
-l <target compound>  # path to target compound (in mol2 format, must contain hydrogens,
                        with AM1BCC or AM1BCCELF10 partial charges,
                        this conformation should be the minimized before being used in
                        RLDOCK-Score-V2 with virtual_screen mode)
-p <compound poses>   # path tp poses sampled by docking software,
                        to be scored by RLDOCK-Score-V2 (in mol2 format,
                        the order of the heavy atoms should be same as the reference compound)
-i <info>             # path to the info file,
                        this file can be generated by the provided python script
                        (/bin/openeye_get_info.py),
                        but it requires a valid OpenEye Academic license (free) to run.
                        This info file should contains the following infomation,
                        user can also check the example info file in the test folder.
                        Atom index starts from 0.
                        -> lig_openeye_torsion (num of the torsions of the compound)
                        -> lig_H_donor_idx     (atom indices of the hydrogen bond donors in the compound)
                        -> lig_H_acceptor_idx  (atom indices of the hydrogen bond acceptors in the compound)
                        -> lig_aromatic_idx    (atom indices of the aromatic atoms in the compound)
                        -> nuc_H_donor_idx     (atom indices of the hydrogen bond donors in the receptor)
                        -> nuc_H_acceptor_idx  (atom indices of the hydrogen bond acceptors in the receptor)
                        -> nuc_aromatic_idx    (atom indices of the aromatic atoms in the receptor)
-s <score mode>       # should be a string, either binding_mode or virtual_screen
```
An example case for running the RLDOCK-Score-V2 can be found in the **test** folder.

## Software References

[1] RLDOCK-Score-V2: to be published.
