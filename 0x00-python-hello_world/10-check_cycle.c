#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: Pointer to the head of the node
 * Return: 1 if there is a cycle 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *current;
	
	if (list == NULL || list->next == NULL)
		return (0);
	head = list;
	current = head->next;
	
	while (head != NULL && current->next != NULL
		&& current->next->next != NULL)
	{
		if (head == current)
			return (1);
		head = head->next;
		current = current->next->next;
	}
	return (0);
}
