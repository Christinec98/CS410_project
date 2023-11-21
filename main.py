import argparse
from search import get_knn
from scrape import do_scrape

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Test')
	parser.add_argument('query', type=str, help='query')
	parser.add_argument('--k', type=str, help='k nearest neighbors', default=5)
	args = parser.parse_args()

	scrape_output = do_scrape(args.query)
	search_output = get_knn(args.query, scrape_output, args.k)
	for o in search_output:
		print(o)

