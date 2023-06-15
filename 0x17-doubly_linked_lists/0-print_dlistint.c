#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - prints all the elements of a list.
 * @h: pointer to the list whose elements are to be printed.
 * Return: number of nodes of the list.
 **/
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *node = h;
	size_t count = 0;

	while (node)
	{
		printf("%i\n", node->n);
		count++;
		node = node->next;
	}

	return (count);
}
