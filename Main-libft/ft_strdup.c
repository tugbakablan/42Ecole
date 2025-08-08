/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com.tr +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/11/19 00:25:07 by tkablan           #+#    #+#             */
/*   Updated: 2024/11/19 00:25:14 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	size_t	len;
	char	*des;

	len = ft_strlen(s) + 1;
	des = malloc(sizeof(char) * len);
	if (!des)
		return (NULL);
	return (ft_memmove(des, s, len));
}
