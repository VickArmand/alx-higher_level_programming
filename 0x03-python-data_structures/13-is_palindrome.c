#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to first node in linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr, *nxt;

	if (head == NULL)
	{
		return (1);
	}
	else if (size_list(head) % 2 != 0)
		return (0);
	curr = *head;
	nxt = (*head)->next;
	while (curr->next != NULL)
	{
		if (curr->n == nxt->n || curr->next->n == nxt->next->n)
			return (1);
		curr = curr->next;
		nxt = nxt->next;
	}
	return (0);
}

/**
 * size_list - finds the number of nodes in the list
 * @head: @head: double pointer to first node in linked list
 * Return: size of linked list (number of nodes)
 */

int size_list(listint_t **head)
{
	int length = 0;
	listint_t *curr;

	curr = *head;
	while (curr != NULL)
	{
		curr = curr->next;
		length++;
	}
	return (length);
}
