
#include <stdlib.h>
#include <stdio.h>

/**
 * @brief Searches for a substring within a limited length of a string.
 *
 * Finds the first occurrence of `needle` in `haystack` within the first `len` characters.
 * Returns a pointer to the start of the found substring, or NULL if not found.
 *
 * @param haystack The main string to search in.
 * @param needle The substring to search for.
 * @param len The maximum number of characters to search.
 * @return A pointer to the start of `needle` in `haystack`, or NULL if not found.
 */

char	*findSubString(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	size_t	j;

	i = 0;
	if (!needle[0])
		return ((char *)haystack);
	while (haystack[i] && i < len)
	{
		if (haystack[i] == needle[0])
		{
			j = 1;
			while (needle[j] && (i + j) < len
				&& haystack[i + j] == needle[j])
				j++;
			if (needle[j] == '\0')
				return ((char *)(haystack + i));
		}
		i++;
	}
	return (NULL);
}

int main(int argc, char **argv)
{
	(void) argc;
    char *result = findSubString(argv[1], argv[2], 20);
    if (result)
        printf("Found: %s\n", result);
    else
        printf("%s Not found\n", argv[2]);

    return (0);
}