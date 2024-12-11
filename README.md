# Mini_Project_EEX5563_Buddy System 
According to the remainder obtained by dividing the registration number by 6 is 4. As the remainder is 4 required algorithm to implement is Buddy System Algorithm.

#  Concept 
Buddy system algorithm is a special algorithm which is used to allocate memory in a systematic way. 
Basically it divides the memory in to blocks which are also known as buddies. 
Each an every memory block size is a power of two value. 
According to the buddy system algorithm it is required to define the memory size to work as expected.
When a job/ request is made by the user, based on the request size the memory will be split in to buddies. 
According to the Job/request size the system check the availability of the memory block and the size of the block is sufficient. If the conditions are met, the job/request will be allocated to the identified block. 
If the block size is too larger, those blocks will be further split in to required memory block sizes. 
If the request/ job is larger than the memory size, the job/request will not be allocated. 
If a request is made to free a specific memory block and then if there are same size of free adjacence blocks, those adjacence blocks will be merge and create a larger block accordingly.  

# Features 
1. Allocates and Free the memory when required.
2. Split larger blocks in to smaller blocks as required.
3. Merge same sizes of free adjacence blocks in to larger blocks. 
4. At any satge can view the memory status.
   
# Useage 
When a job/request is made, the system will allocate the job to the smallest size and free buddy. Jobs are allocated from bottom to top of the memory. If required the larger buddied will split in to smaller size buddies.

All the buddy sizes are powers of two (512KB, 256KB,128KB,64KB,32KB,16KB,8KB,4KB,2KB).

Deallocate memory, based on the request size the memory block will be freed. If there are 2 same size adjacence free blocks , blocks will be merged. 