# thesis
This is the code that I used to compute all measures for my thesis "Human vs Machine Translation: a Comparative Analysis on Linguistic and Syntactic Structures"

Note that if you want to run udstyle, you have to download the file udstyle.py from https://github.com/andreasvc/udstyle

This are the commands that I used:
```bash
python3 udstyle.py --parse=en content/Original_story.txt --output=ST_syn.tsv
python3 udstyle.py --parse=nl content/HumanTranslations/*.txt --output=HT_syn.tsv
python3 udstyle.py --parse=nl content/MachineTranslations/*.txt --output=MT_syn.tsv
python3 calculate_MATTR.py content/Original_story.txt ST_MATTR.tsv
python3 calculate_MATTR.py content/HumanTranslations/*.txt HT_MATTR.tsv
python3 calculate_MATTR.py content/MachineTranslations/*.txt MT_MATTR.tsv
```
If you want to run everything in one go, run ``` python3 run_all.py ```

For running the file that computed the COMET scores (calculate_comet.ipynb) using Jupyter Notebook is recommended.
