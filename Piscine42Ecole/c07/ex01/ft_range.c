/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/14 13:19:55 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/14 13:36:37 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	range;
	int	i;
	int	*a;

	if (min >= max)
	{
		return (a = NULL);
	}
	range = max - min;
	a = (int *)malloc(range * sizeof(int) + 1);
	if (!a)
		return (0);
	i = 0;
	while (min < max)
	{
		a[i] = min ;
		min++;
		i++;
	}
	return (a);
}
