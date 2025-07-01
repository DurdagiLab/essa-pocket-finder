# essa-pocket-finder
***essa-pocket-finder*** is a Python-based computational tool developed for the identification and ranking of allosteric sites in protein structures using the Essential Site Scanning Analysis (ESSA) method. By incorporating normal mode analysis, this tool evaluates the impact of residue perturbations on global protein dynamics to detect residues and surface pockets that may serve regulatory or allosteric functions. It supports optional ligand-based contextual analysis and outputs residue Z-score profiles and ranked pocket predictions. The tool is intended for researchers working in structure-based drug design, protein dynamics, and allosteric modulation.

# Requirements & Installation
This tool was developed using Python and relies on several scientific computing libraries. Please ensure the following packages are installed in your environment:

Required Python Packages
- `ProDy == 2.4.1`  
- `NumPy == 1.23.5`  
- `Matplotlib == 3.7.1`  
- `Pandas == 1.5.3`  
- `Biopandas == 0.4.1`

**These dependencies are listed in the requirements.txt file.

-Installation Instructions
To install the required packages, we recommend using a virtual environment. Then run the following command in your terminal:

> pip install -r requirements.txt

Alternatively, individual packages can be installed using:

> pip install prody==2.4.1 numpy==1.23.5 matplotlib==3.7.1 pandas==1.5.3 biopandas==0.4.1

Note: ProDy is essential for normal mode analysis and ESSA implementation. Ensure your Python version is compatible (e.g., Python 3.8+ is recommended).

# Usage
After installation, the ESSA analysis script can be executed from the command line using the following syntax:

> python run_essa.py -p <protein.pdb> [-l <LIGAND>] [-r <RESNUM>] [-c <CHAIN>]

Command-Line Arguments:

Parameter	    Description	                            Required
-p, --pdb	    Input PDB file (e.g., protein.pdb)      Yes
-l	          Ligand residue name (e.g., ATP)	        Optional
-r            Ligand residue number (e.g., 456)       Optional
-c	          Ligand chain ID (e.g., A)	              Optional

# Output Files:
Upon successful execution, the following files will be generated:

- `ESSA_Results.txt` – Detailed analysis log and Z-score outputs  
- `ESSA_Profile.png` – Visualization of residue-based ESSA Z-scores  
- `pocket_ranks.csv` – Ranked list of predicted allosteric pockets  
- `essa_zscores.pdb` – PDB file annotated with ESSA Z-score data

**Ligand information is optional but may help guide analysis in ligand-bound states.

# Citation
If you use this tool in your academic work, please cite:

Computational Drug Design Center (HITMER), Faculty of Pharmacy, Bahçeşehir University, Istanbul, Turkey





