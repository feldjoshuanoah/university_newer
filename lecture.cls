\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lecture}

\input{common.tex}

\titleformat{\section}{}{\Large\bfseries\thesection.\enspace}{0pt}{\Large\bfseries}
\titleformat{\subsection}{}{\large\bfseries\thesubsection.\enspace}{0pt}{\large\bfseries}
\titleformat{\subsubsection}{}{\normalsize\bfseries\thesubsubsection.\enspace}{0pt}{\normalsize\bfseries}

\RequirePackage{amsthm}

\newtheoremstyle{custom}{}{}{}{}{}{}{ }{\bfseries#1 \thmnumber{#2}\thmnote{ (#3)}.}
\theoremstyle{custom}
\newtheorem{corollary}{\ifenglish{Corollary}\else{Korollar}\fi}
\numberwithin{corollary}{section}
\newtheorem{definition}[corollary]{Definition}
\newtheorem{example}[corollary]{\ifenglish{Example}\else{Beispiel}\fi}
\newtheorem{lemma}[corollary]{Lemma}
\newtheorem{proposition}[corollary]{\ifenglish{Proposition}\else{Satz}\fi}
\newtheorem{remark}[corollary]{\ifenglish{Remark}\else{Bemerkung}\fi}
\newtheorem{theorem}[corollary]{Theorem}

\RequirePackage{etoolbox}
\AtBeginEnvironment{corollary}{\setlist[enumerate]{label={(\roman*)}}}
\AtBeginEnvironment{definition}{\setlist[enumerate]{label={(\roman*)}}}
\AtBeginEnvironment{example}{\setlist[enumerate]{label={\arabic*)}}}
\AtBeginEnvironment{lemma}{\setlist[enumerate]{label={(\roman*)}}}
\AtBeginEnvironment{proof}{\setlist[enumerate]{label={(\roman*)}}}
\AtBeginEnvironment{proposition}{\setlist[enumerate]{label={(\roman*)}}}
\AtBeginEnvironment{remark}{\setlist[enumerate]{label={\alph*)}}}
\AtBeginEnvironment{theorem}{\setlist[enumerate]{label={(\roman*)}}}
