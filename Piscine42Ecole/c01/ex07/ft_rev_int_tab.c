/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/04 16:46:22 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/04 23:32:19 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_rev_int_tab(int *tab, int size)
{
	int	x;
	int	swap;

	x = 0;
	while (x < size / 2)
	{
		swap = tab[x];
		tab[x] = tab[size - 1 - x];
		tab[size - 1 - x] = swap;
		x++;
	}
}
