/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com.tr +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/11/19 00:20:23 by tkablan           #+#    #+#             */
/*   Updated: 2024/11/19 00:21:11 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nbyte, size_t size)
{
	void	*dst;

	dst = malloc(size * nbyte);
	if (!dst)
		return (0);
	ft_bzero(dst, size * nbyte);
	return (dst);
}
