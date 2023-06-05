#include "lists.h"


/**
 * check_cycle - check speed
 * @list: list
 * Return: 1 if detected, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *quick = list;

	while (low != NULL && quick != NULL && quick->next != NULL)
	{
		low = low->next;
		quick = quick->next->next;
		if (low == quick)
		{
			return (1);
		}
	}
	return (0);
}
