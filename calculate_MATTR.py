from lexical_diversity import lex_div as ld
import sys
import os
import csv

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 calculate_MATTR.py input.txt(or ~home/folder/*.txt) output.tsv")
        sys.exit(1)
    
    filenames = sys.argv[1:-1]
    output_filename = sys.argv[-1]
    results = []
    for filename in filenames:
        flemmatized_text = []
        with open(filename) as text:
            for line in text:
                flt = ld.flemmatize(line)
                flemmatized_text.extend(flt)
        results.append([os.path.splitext(os.path.basename(filename))[0], ld.mattr(flemmatized_text)])

    with open(output_filename, 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        writer.writerow(['Filename', 'MATTR'])
        writer.writerows(results)

    print('Results written to file', output_filename)

    

if __name__ == '__main__':
	main()




