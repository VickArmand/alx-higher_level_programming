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
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		current = *head;
		while (current != NULL && number > current->n)
		{
			prev = current;
			current = current->next;
		}
		prev->next = new;
		new->next = current;
	}
	return (new);

}
