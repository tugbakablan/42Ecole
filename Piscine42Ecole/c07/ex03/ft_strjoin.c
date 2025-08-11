/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/15 02:40:48 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/15 12:36:36 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*new_str;
	int		index;
	int		index2;
	int		index3;

	new_str = (char *)malloc(sizeof(strs));
	index = 0;
	index3 = 0;
	while (index < size)
	{
		index2 = 0;
		while (strs[index][index2] != '\0')
		{
			new_str[index3++] = strs[index][index2++];
		}
		index2 = 0;
		while (sep[index2] != '\0' && index != size - 1)
		{
			new_str[index3++] = sep[index2++];
		}
		index++;
	}
	new_str[index3] = '\0';
	return (new_str);
}
