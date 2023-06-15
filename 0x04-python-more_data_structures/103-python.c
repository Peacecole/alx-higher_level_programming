#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints out bytes information
 * @p: pointer to python object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int obj_size, i, size_limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	obj_size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", obj_size);
	printf("  trying string: %s\n", string);

	if (obj_size >= 10)
		limit = 10;
	else
		size_limit = obj_size + 1;

	printf("  first %ld bytes:", size_limit);

	for (i = 0; i < size_limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - prints out list information
 * @p: pointer python object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int obj_size, i;
	PyListObject *obj_list;
	PyObject *obj;

	obj_size = ((PyVarObject *)(p))->ob_size;
	obj_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", obj_size);
	printf("[*] Allocated = %ld\n", obj_list->allocated);

	for (i = 0; i < obj_size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}

