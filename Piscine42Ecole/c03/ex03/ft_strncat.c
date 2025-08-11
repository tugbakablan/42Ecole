/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/11 20:18:46 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/11 21:31:50 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	unsigned int	a;
	unsigned int	b;

	a = 0;
	b = 0;
	while (dest[a] != '\0')
		a++;
	while (src[b] != 0 && b < nb)
	{
		dest[a] = src[b];
		a++;
		b++;
	}
	dest[a] = '\0';
	return (dest);
}
