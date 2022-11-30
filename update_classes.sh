#!/bin/bash
mkdir -p $HOME/.texmf/tex/latex/local
sudo /usr/local/texlive/2022/bin/x86_64-linux/tlmgr conf texmf TEXMFHOME $HOME/.texmf
cp -rf common.tex exercise.cls lecture.cls $HOME/.texmf/tex/latex/local
/usr/local/texlive/2022/bin/x86_64-linux/mktexlsr $HOME/.texmf
