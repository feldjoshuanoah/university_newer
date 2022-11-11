\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{exercise}

\input{common.tex}

\titleformat{\section}{}{\Large\bfseries\ifenglish{Exercise}\else{Aufgabe}\fi \ \thesection}{1em}{}

\setlist[enumerate,1]{label=\alph*)}
\setlist[enumerate,2]{label=(\roman*)}
