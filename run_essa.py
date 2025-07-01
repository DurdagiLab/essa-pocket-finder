"""
##########################################################################################################################
Title: ESSA Analysis and Allosteric Pocket Prediction Tool

Developed by: Mine Isaoglu, Ph.D.
Principal Investigator: Serdar Durdagi, Ph.D.
Affiliation: Computational Drug Design Center (HITMER), Faculty of Pharmacy, Bahçeşehir University, Istanbul, Turkey

Version: September 2024
##########################################################################################################################
"""

import os
import sys
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
from prody import parsePDB, ESSA

def parse_arguments():
    parser = argparse.ArgumentParser(description='ESSA Analysis for Allosteric Pocket Prediction')
    parser.add_argument('-p', '--pdb', required=True, help='Input PDB file (e.g., protein.pdb)')
    parser.add_argument('-l', '--ligand_name', help='Ligand residue name (e.g., ATP)')
    parser.add_argument('-r', '--ligand_resnum', help='Ligand residue number (e.g., 456)')
    parser.add_argument('-c', '--ligand_chain', help='Ligand chain ID (e.g., A)')
    parser.add_argument('-o', '--output', default='ESSA_Results.txt', help='Output results file')
    return parser.parse_args()

def validate_pdb_file(pdb_file):
    if not os.path.isfile(pdb_file):
        print(f"[ERROR] File '{pdb_file}' does not exist.")
        sys.exit(1)

def setup_essa_system(pdb_file, ligand_name=None, ligand_resnum=None, ligand_chain=None):
    ag = parsePDB(pdb_file, compressed=False)
    essa = ESSA()

    if ligand_name and ligand_resnum and ligand_chain:
        selection_str = f"{ligand_chain} {ligand_resnum}"
        selection = ag.select(f"resname {ligand_name} and resnum {ligand_resnum} and chain {ligand_chain}")
        if selection:
            print(f"[INFO] Ligand {ligand_name} {ligand_resnum} found. Using ligand in analysis.")
            essa.setSystem(ag, lig=selection_str)
        else:
            print(f"[WARNING] Ligand not found! Proceeding without ligand.")
            essa.setSystem(ag)
    else:
        print("[INFO] No ligand specified. Proceeding without ligand.")
        essa.setSystem(ag)

    return essa

def run_essa_analysis(essa, output_file):
    with open(output_file, "w") as f:
        sys.stdout = f  # Redirect stdout to output file

        print("[INFO] Starting ESSA residue scan...")
        essa.scanResidues()

        print("[INFO] Plotting ESSA profile...")
        with plt.style.context({'figure.dpi': 100}):
            essa.showESSAProfile()
            plt.savefig("ESSA_Profile.png")

        z_scores = essa.getESSAZscores()[:10]
        print("\n[RESULTS] Top 10 ESSA z-scores:", z_scores)
        essa.saveESSAZscores()
        essa.writeESSAZscoresToPDB()

        print("\n[INFO] Scanning for allosteric pockets...")
        essa.scanPockets()
        pocket_z_scores = essa.getPocketZscores()
        print("\n[RESULTS] Pocket Z-scores:\n", pocket_z_scores)

        essa.rankPockets()
        pocket_ranks = essa.getPocketRanks()
        print("\n[RESULTS] Ranked Pockets:\n", pocket_ranks)

        essa.savePocketZscores()
        essa.writePocketRanksToCSV()

        print("\n[INFO] ESSA analysis completed successfully.")

        sys.stdout = sys.__stdout__  # Restore stdout

    print(f"[INFO] Results saved to {output_file}")
    print(f"[INFO] ESSA Profile saved as 'ESSA_Profile.png'")
    print(f"[INFO] Pocket ranking saved as 'pocket_ranks.csv'")

def main():
    args = parse_arguments()
    validate_pdb_file(args.pdb)
    essa = setup_essa_system(
        pdb_file=args.pdb,
        ligand_name=args.ligand_name,
        ligand_resnum=args.ligand_resnum,
        ligand_chain=args.ligand_chain
    )
    run_essa_analysis(essa, args.output)

if __name__ == "__main__":
    main()
