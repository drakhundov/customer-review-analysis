# Usage: `canal *OPTIONS $CSV_FILE`
`$CSV_FILE` denotes a list of customer reviews. It can have any number of fields as long as there is a field named `text`, which denotes the review.

# Commands
## `canal search $CSV_FILE`
### Searches for inputted query in user reviews.
### Options:
### `-n $n`

## `canal best_k $CSV_FILE`
### Tells the best k for SVD for the lowest error.