#include "lists.h"

/**
 * is_palindrome - tests if linked lists is palindrome
 * @head: address of pointer to list
 * Return: 1 is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *n, *p;
	int failed = 0;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	n = slow;
	p = NULL;
	while (n)
	{
		fast = n->next;
		n->next = p;
		p = n;
		n = fast;
	}
	fast = *head;
	n = p;
	while (p)
	{
		if (fast->m != p->m)
		{
			failed = 1;
			break;
		}
		fast = fast->next;
		p = p->next;
	}
	p = NULL;
	while (n)
	{
		fast = n->next;
		n->next = p;
		p = n;
		n = fast;
	}
	return (!failed);
}
