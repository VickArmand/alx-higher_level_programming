#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list != NULL ? list->next : NULL;
	int iscycle = 0;

	while (current->next != NULL)
	{
		if (current == list)
		{
			iscycle = 1;
			break;
		}
		current = current->next;
	}
	return (iscycle);
}
