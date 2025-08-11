/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/12 17:52:27 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/12 23:38:03 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_factorial(int nb)
{
	if (nb == 0)
	{
		return (1);
	}
	if (nb < 0)
	{
		return (0);
	}
	return (nb * ft_recursive_factorial(nb -1));
}
