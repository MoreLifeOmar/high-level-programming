#include "lists.h"
/**
 * check_cycle - checking if there is a cycle.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
  listint_t *slow; 
  listint_t *fast;
  slow = list;
  fast = list;

  if (list == NULL)
      return (0);
  while (slow && fast && fast->next)
    {
      fast = fast->next->next;
      slow = slow->next;
      if (fast == slow)
	return(1);
    }
  return (0);
}
