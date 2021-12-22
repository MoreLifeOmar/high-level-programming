#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new;
  listint_t *current;

  current = *head;
  if (*head == NULL)
    {
     new = malloc(sizeof(listint_t));
     if (new == NULL)
       return (NULL);
     new->n = number;
     new->next = NULL;
    *head = new;
    return(new);
    }
  while (current && current->next)
    {
      if (number <= (*head)->n)
	{
	 new = malloc(sizeof(listint_t));
	 if (new == NULL)
	    return (NULL);                                                                                                                                                                                                  new->n = number;
	  new->next = *head;
	  *head = new;
	  return (*head);
	}
      else if (number <= current->next->n)
	{
	  new = malloc(sizeof(listint_t));
	  if (new == NULL)
	    return (NULL);                                                                                                                                                                                                  new->n = number; 
	  new->next = current->next;
	  current->next = new;
	  return (new);
	}
      current = current->next;
    }
  if ((number >= current->n) && (current->next == NULL))
    {
      new = malloc(sizeof(listint_t));
      if (new == NULL)
	return (NULL);                                                                                                                                                                                                  new->n = number;
      new->next = NULL;
      if (current != NULL)
	current->next = new;
      else
	*head = new;
      return (new);
    }
  return (NULL);
}
