#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to first node in linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr, *nxt, *prev;

	if (*head == NULL)
	{
		return (1);
	}
	prev = *head;
	curr = prev->next;
	nxt = curr->next;
	while (curr != NULL)
	{
		if (curr->n == nxt->n || curr->next->n == nxt->next->n)
			return (1);
		prev = prev->next;
		curr = curr->next;
		nxt = nxt->next;
	}
	return (0);
}
