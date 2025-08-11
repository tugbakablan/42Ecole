/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/12 16:59:33 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/12 23:35:52 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	result;

	result = nb;
	if (nb == 0)
	{
		return (1);
	}
	if (nb < 0)
	{
		return (0);
	}
	while (nb > 1)
	{
		result *= nb - 1;
		nb--;
	}
	return (result);
}
