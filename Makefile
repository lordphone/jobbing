TEX = tectonic

.PHONY: all clean

all:
	$(TEX) resume.tex
	mv -f resume.pdf Lordphone_Wen_Resume.pdf

clean:
	rm -f *.aux *.log *.out *.synctex.gz
	rm -f applications/*/*.aux applications/*/*.log \
	      applications/*/*.out applications/*/*.synctex.gz
