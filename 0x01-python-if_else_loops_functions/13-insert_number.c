#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: first node of the list
 * @number: node data
 * Return:  the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		prev = *head;
		current = (*head)->next;
		while (current != NULL || prev != NULL)
		{
			if (number < current->n)
			{
				prev->next = new;
				new->next = current;
				break;
			}
			prev = prev->next;
			current = current->next;
		}
	}
	return (new);

}
