#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list->next;
	int iscycle = 0;

	while (current->next)
	{
		if (current->n == list->n)
		{
			iscycle = 1;
			break;
		}
		current = current->next;
	}
	return (iscycle);
}
