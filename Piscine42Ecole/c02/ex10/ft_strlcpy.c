/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/07 22:17:25 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/07 22:18:37 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_strlen(char *str)
{
	unsigned int	counter;

	counter = 0;
	while (*str != '\0')
	{
		counter++;
		str++;
	}
	return (counter);
}

unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	unsigned int	i;

	if (size == 0)
		return (ft_strlen(src));
	i = 0;
	while (i < size - 1 && src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (ft_strlen(src));
}
