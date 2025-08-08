/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com.tr +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/11/19 00:21:58 by tkablan           #+#    #+#             */
/*   Updated: 2024/11/19 00:22:01 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	count_size(long num)
{
	size_t	size;

	size = 0;
	if (!num)
		return (1);
	else if (num < 0)
	{
		num = -num;
		size++;
	}
	while (num > 0)
	{
		size++;
		num /= 10;
	}
	return (size);
}

char	*ft_itoa(int n)
{
	size_t	size;
	size_t	i;
	char	*str;
	long	num;

	i = 0;
	num = (long)n;
	size = count_size(num);
	str = malloc(sizeof(char) * (size + 1));
	if (!str)
		return (NULL);
	if (!num)
		str[0] = '0';
	if (num < 0)
	{
		num = -num;
		str[0] = '-';
	}
	while (num > 0)
	{
		str[size - 1 - i++] = num % 10 + 48;
		num /= 10;
	}
	str[size] = '\0';
	return (str);
}
