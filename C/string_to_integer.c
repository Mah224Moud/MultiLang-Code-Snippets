/**
 * @file ft_string_to_int.c
 * @brief Converts a string to an integer.
 * 
 * This function parses a string and converts it into an integer, 
 * handling optional whitespaces, '+' or '-' signs at the beginning.
 * 
 * @param str A pointer to the string to convert.
 * 
 * @return The integer representation of the string. If no valid conversion 
 *         can be performed, the function will return 0.
 */
int	ft_string_to_int(char *str)
{
	int	i;
	int	res;
	int	sign;

	i = 0;
	sign = 1;
	res = 0;
	while (str[i] && ((str[i] >= 9 && str[i] <= 13) || str[i] == 32))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] && (str[i] >= '0' && str[i] <= '9'))
	{
		res = res * 10 + (str[i] - '0');
		i++;
	}
	return (res * sign);
}

