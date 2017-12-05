#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if singly linked list has a cycle in it.
 * @list: listint_t list
 * Return: 1 if list has a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list;

	if (list == NULL)
		return (0);
	while (temp->next != NULL)
	{
		temp2 = temp->next;
		while (temp2->next != NULL)
		{
			if (temp->next == temp2->next)
				return (1);
			temp2 = temp2->next;
		}
		temp = temp->next;
	}
	return (0);
}
