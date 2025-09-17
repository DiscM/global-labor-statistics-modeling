#!/usr/bin/env python3
import argparse, subprocess, sys, os
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--dataset', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    os.makedirs(args.out, exist_ok=True)
    cmd = ['kaggle','datasets','download','-d',args.dataset,'-p',args.out,'--unzip']
    try:
        print('>>', ' '.join(cmd))
        subprocess.check_call(cmd)
    except Exception as e:
        print('Kaggle CLI failed. Install/configure kaggle to use this helper.')
        print(e); sys.exit(1)
if __name__=='__main__':
    main()
