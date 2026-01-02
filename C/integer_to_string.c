#include <stdlib.h>

/**
 * @brief Calculate the length of the resulting string for an integer.
 * 
 * This helper function determines the number of characters needed 
 * to represent an integer as a string, including space for the sign if negative.
 * 
 * @param n The integer to analyze.
 * @return The length of the string required to store the integer representation.
 */
static int	get_integer_length(int n)
{
	int	len;

	len = 1;
	if (n < 0)
		len++;
	while (n / 10 != 0)
	{
		n /= 10;
		len++;
	}
	return (len);
}

/**
 * @brief Recursively convert an integer to a string representation.
 * 
 * This helper function uses recursion to build the string representation 
 * of the integer, storing each digit in the result string.
 * 
 * @param nb The number to convert (as a long to handle edge cases).
 * @param res Pointer to the result string being constructed.
 * @param i Pointer to the current index in the result string.
 */
static void	convert_integer_to_string_recursive(long nb, char *res, int *i)
{
	if (nb >= 10)
	{
		convert_integer_to_string_recursive(nb / 10, res, i);
		convert_integer_to_string_recursive(nb % 10, res, i);
	}
	else
	{
		res[*i] = nb + '0';
		(*i)++;
	}
}

/**
 * @brief Convert an integer to its string representation.
 * 
 * This function converts an integer to a dynamically allocated string, 
 * including handling of negative numbers. The resulting string should be freed 
 * by the caller to avoid memory leaks.
 * 
 * @param n The integer to convert.
 * @return A pointer to the resulting string, or NULL if memory allocation fails.
 */
char	*integer_to_string(int n)
{
	char	*res;
	int		i;
	long	nb;

	nb = n;
	i = 0;
	res = (char *)malloc((get_integer_length(nb) + 1) * sizeof(char));
	if (res == NULL)
		return (NULL);
	if (n < 0)
	{
		res[i++] = '-';
		nb = -nb;
	}
	convert_integer_to_string_recursive(nb, res, &i);
	res[i] = '\0';
	return (res);
}

int     main(void)
{
     __builtin_printf("The result is a string value : %s\n", integer_to_string(-2024));
	// Output The result is a string value : -2024
	return (0);
}
