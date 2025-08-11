/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/12 18:05:00 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/12 23:41:43 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_power(int nb, int power)
{
	int	i;
	int	result;

	i = 1;
	result = nb;
	if (power == 0)
		return (1);
	if (power < 0)
		return (0);
	while (i < power)
	{
		result *= nb;
		i++;
	}
	return (result);
}
