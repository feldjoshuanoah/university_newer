for %%f in (common.tex,exercise.cls,lecture.cls) do xcopy /s /y %%f "C:\texlive\texmf-local\tex\latex\local\"
texhash