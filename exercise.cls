\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{exercise}

\input{common.tex}

\titleformat{\section}{}{\ifenglish{\ul{Task}}\else{\ul{Aufgabe}}\fi\ul{\ \thesection}}{1em}{}

\setlist[enumerate,1]{label=\alph*)}
\setlist[enumerate,2]{label=(\roman*)}
