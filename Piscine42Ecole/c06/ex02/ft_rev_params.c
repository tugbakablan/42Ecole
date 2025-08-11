/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_params.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tkablan <tkablan@student.42istanbul.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/02/14 04:30:26 by tkablan           #+#    #+#             */
/*   Updated: 2024/02/14 04:30:55 by tkablan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char a)
{
	write (1, &a, 1);
}

int	main(int ac, char **av)
{
	int	i;
	int	j;

	if (ac >= 1)
	{
		i = ac -1;
		while (i > 0)
		{
			j = 0;
			while (av[i][j])
			{
				ft_putchar (av[i][j]);
				j++;
			}
			i--;
			ft_putchar('\n');
		}
	}
	return (0);
}
