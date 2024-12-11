import tkinter as tk
import math

class BuddySystem:

    def __init__(self):

        self.memory_pool_list = []
        self.memory_status = []
        self.job_queue = []
        self.data = []
        self.powers_of_2 = set()
        self.sub_divided_memory = []

    # popup message UI
    def message(self,title_message,message,output_message,ico_path,image_path,btn_colour,message_colour):

        popup = tk.Toplevel()
        popup.title(title_message)
        popup.iconbitmap(ico_path)
        popup.geometry("200x190+130+200")
  
        popup.configure(bg='white')
    
        image2 = tk.PhotoImage(file=image_path) 
        image2 = image2.subsample(max(1,image2.width()//50, max(1,image2.height()//50)))
        error_label = tk.Label(popup, image=image2)
        error_label.config(width=50,height=50)
        error_label.image2 = image2
        error_label.pack(pady=5)
    
        label = tk.Label(popup,text=message, bg="white",fg=message_colour)
        label.pack(pady=20)

        button = tk.Button(popup,text=output_message, command=popup.destroy, bg=btn_colour,fg="white",width=17, font=('Times new roman',10,'bold'))
        button.pack(pady=5)
    
    # GUI implementation
    def GUI(self):
      
      window = tk.Tk()
      window.title("Buddy System")
      window.iconbitmap("Assets/Buddy_system.ico")
      window.geometry("380x610+50+50")
      window.config(bg="white")
    
      # GUI Elements 
      # variables 
      memory_pool_size_var = tk.IntVar()
      job_size_var = tk.IntVar()
       
      # header image
      header_Image = tk.PhotoImage(file="Assets/Buddy_system.png")
      header_Image = header_Image.subsample(max(1,header_Image.width()//50, max(1,header_Image.height()//40)))

      # header label
      header_label = tk.Label(window, text="Buddy System", image=header_Image,foreground="white",padx=12,background="#42d40d",width=600,font=('Times new roman',16,'bold'),compound="left")
      header_label.config(height=50)
      header_label.pack(pady=1)

      # frame to add job details
      buddy_system_data_frame = tk.Frame(window, width=260, height=200, relief=tk.GROOVE,background="white")
      buddy_system_data_frame.pack_propagate(False)
      buddy_system_data_frame.pack(pady=20)
    
      # frame to add the Allocate Memory button 
      allocate_memory_button_frame = tk.Frame(window, relief=tk.GROOVE,background="white")
      allocate_memory_button_frame.pack_propagate(False) 
      allocate_memory_button_frame.pack(pady=10)

      # frame to get the memory status details
      status_frame = tk.Frame(window,width=260, height=200, relief=tk.GROOVE,background="white",bd=2)
      status_frame.pack_propagate(False)
      status_frame.pack(pady=8)
      
      # frame to add the Fee Memory Button 
      button_frame = tk.Frame(window, relief=tk.GROOVE,background="white")
      button_frame.pack_propagate(False)
      button_frame.pack(pady=10)

      # define the buddy system user input data 
      buddy_system_info_frame = tk.LabelFrame(buddy_system_data_frame,text="Job Details",relief=tk.GROOVE,background="white",font=('Times new roman',15,'bold'))
      buddy_system_info_frame.grid(row=0,column=0,padx=10, pady=15)
      
      # define the memory pool size input
      memory_pool_label = tk.Label(buddy_system_info_frame, text = "Memory Pool Size (KB) :",background="white")
      memory_pool_label.grid(row=1,column=0,padx= 15,pady=10,sticky='w')

      memory_pool_entry = tk.Entry(buddy_system_info_frame,highlightbackground="#E4E4E8",highlightthickness=1,textvariable=memory_pool_size_var)
      memory_pool_entry.config(width=20)
      memory_pool_entry.grid(row=1, column=1,pady=10,padx=25)
      
      # define the memory pool size 
      memory_pool_button = tk.Button(buddy_system_info_frame, text="Initialize",background="#3dd90d", padx=4,pady=2,
                                 font=('Times new roman',10,'roman'),foreground='white',command=lambda:self.define_memory_size(int(memory_pool_entry.get())))
      memory_pool_entry.delete(0,tk.END)
      memory_pool_button.config(width=14)
      memory_pool_button.grid(row=2,column=1,padx=6,pady=12)

      # define the number of jobs
      job_size_label = tk.Label(buddy_system_info_frame, text = "Job Size (KB) :",background="white")
      job_size_label.grid(row=3,column=0,padx= 15,pady=10,sticky='w')

      job_size_entry = tk.Entry(buddy_system_info_frame,highlightbackground="#E4E4E8",highlightthickness=1,textvariable= job_size_var)
      job_size_entry.config(width=20)
      job_size_entry.grid(row=3, column=1,pady=10,padx=25)
      
      # view the jobs in job queue
      view_job_button = tk.Button(buddy_system_info_frame, text="View Jobs",background="#3dd90d", padx=4,pady=2,
                                 font=('Times new roman',10,'roman'),foreground='white',command=self.view_jobs)
      view_job_button.config(width=14)
      view_job_button.grid(row=4,column=0,padx=6,pady=12)

      # button to add a job in to the job queue 
      add_job_button = tk.Button(buddy_system_info_frame, text="Add Job",background="#3dd90d", padx=4,pady=2,
                                 font=('Times new roman',10,'roman'),foreground='white',command=lambda:self.add_Job(int(job_size_entry.get()),job_size_entry))
      job_size_entry.delete(0,tk.END)
      add_job_button.config(width=14)
      add_job_button.grid(row=4,column=1,padx=6,pady=12)

      # allocate memory 
      allocate_memory_button = tk.Button(allocate_memory_button_frame, text="Allocate Memory",background="#056e03", padx=8,pady=4,
                                 font=('Times new roman',10,'roman'),foreground='white',command=self.create_buddies)
      allocate_memory_button.config(width=45)
      allocate_memory_button.grid(row=5,column=1,padx=6,pady=12)

      # get memory status
      memory_status = tk.Label(status_frame, text = "View Current Memory Status ",background="white",font=('Times new roman',12,'bold'))
      memory_status.grid(row=7,column=0,padx= 15,pady=10,sticky='w')

      memory_status_label = tk.Label(status_frame, text = "View Memory Status :",background="white",font=('Times new roman',11))
      memory_status_label.grid(row=8,column=0,padx= 12,pady=10,sticky='w')

      memory_status_button = tk.Button(status_frame, text="Memory Status",background="#3dd90d", padx=4,pady=2,
                                 font=('Times new roman',10,'roman'),foreground='white',command=lambda:self.memory_pool_details())
      memory_status_button.config(width=12)
      memory_status_button.grid(row=8,column=1,padx=6,pady=12)

      # free memory 
      free_memory_button = tk.Button(button_frame, text="Free Memory",background="#056e03", padx=8,pady=4,
                                 font=('Times new roman',10,'roman'),foreground='white',command=self.free_memory)
      free_memory_button.config(width=45)
      free_memory_button.grid(row=8,column=1,padx=6,pady=12)

      window.mainloop()

    # define the memory sizes based on the memory pool size 
    def define_memory_size(self,memory_entry):

       if memory_entry >0:
          self.memory_pool_list.append(memory_entry)
          self.memory_status.append("Free")

          x = math.log(memory_entry,2)
          i = 1
          while i<=x:
            power = 2**i
            self.powers_of_2.add(power)
            i +=1
          
          self.powers_of_2_list = list(self.powers_of_2)
          self.powers_of_2_list.sort()

          self.message("Memory size defined Success","Memory size defined Succesfully",
                    "Done","Assets/success.ico","Assets/success.png","green","dark green")

          return self.memory_pool_list

       else:
          self.message("Invalid Size","Invalid memory Size",
                       "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")

    # define the memory pool 
    def memory_pool_details(self):

        memory = tk.Toplevel()
        memory.title("Job Queue")
        memory.iconbitmap("Assets/Buddy_system.ico")
        height = 140 + 30* len(self.memory_pool_list)
        memory.geometry(f"240x{height}+130+200")
  
        memory.configure(bg='white')
        
        label = tk.Label(memory,text="Memory Status", bg="white",fg="dark green",font=('Times new roman',14,'bold'))
        label.pack(pady=6)
        
        if len(self.memory_pool_list) ==0:
           label = tk.Label(memory,text="Memory size is not defined.", bg="white",fg="black",font=('Times new roman',10))
           label.pack(pady=6)

        elif len(self.memory_pool_list) >0:
            for x in range(len(self.memory_pool_list)):
                label = tk.Label(memory,text=f"{self.memory_pool_list[x]} KB Block : {self.memory_status[x]} ", bg="white",fg="black",font=('Times new roman',10))
                label.pack(pady=6)
        
        button = tk.Button(memory,text="Done", command=memory.destroy, bg="dark green",fg="white",width=12, font=('Times new roman',11,'bold'))
        button.pack(pady=12)

    # add jobs to the job queue
    def add_Job(self,job,job_size_entry):
        
        if job>0:
           self.job_queue.append(job)
           self.message("Job Added Success","Job Added Succesfully",
                    "Done","Assets/success.ico","Assets/success.png","green","dark green")
             
        elif job<=0:
           self.message("Invalid Size","Invalid Job Size",
                    "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")
           
        job_size_entry.delete(0,tk.END)
    
    # method to view the jobs in job queue
    def view_jobs(self):

        jobs = tk.Toplevel()
        jobs.title("Job Queue")
        jobs.iconbitmap("Assets/Buddy_system.ico")
        height = 140 + 30* len(self.job_queue)
        jobs.geometry(f"220x{height}+130+200")
  
        jobs.configure(bg='white')
        
        label = tk.Label(jobs,text="Jobs in Job Queue", bg="white",fg="dark green",font=('Times new roman',14,'bold'))
        label.pack(pady=6)

        if len(self.job_queue) <= 0:
            label = tk.Label(jobs,text="No Jobs in Job queue", bg="white",fg="black",font=('Times new roman',10))
            label.pack(pady=6)
                
        for x in range(len(self.job_queue)):
            label = tk.Label(jobs,text=f"Job {x+1} : {self.job_queue[x]} KB", bg="white",fg="black",font=('Times new roman',11))
            label.pack(pady=6)

        button = tk.Button(jobs,text="Done", command=jobs.destroy, bg="dark green",fg="white",width=12, font=('Times new roman',11,'bold'))
        button.pack(pady=12)
    
    # creating the buddies of the memory
    def partitioning_memory(self,job):
        
        count = 0
        if job > max(self.memory_pool_list) or job <=0:
           self.message("Error","cannot allocate the job",
                    "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")

        else:
          
          for x in range(len(self.powers_of_2_list)):
         
            minimum = min(self.memory_pool_list)

            nearest_value = minimum//2

            if job<= nearest_value and nearest_value !=1:
              
              self.memory_pool_list.remove(minimum)
              self.memory_status.remove(self.memory_status[count])

              for x in range(2):
                self.memory_pool_list.append(nearest_value)
                self.memory_status.append("Free")

    # find the nearest power of 2 value based on the job size
    def nearest_value(self,job):
      for value in self.powers_of_2_list:
          if job <= value:
            self.data.append(value)
            
      nearest_value = min(self.data)
      self.data.clear()

      return nearest_value
    
    # creating buddies in the memory to allocate jobs
    def create_buddies(self):
        # defining the counter value
        k = 0

        if len(self.job_queue) == 0:
           self.message("Error","No Jobs To Allocate",
                    "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")
           
        if len(self.memory_pool_list) == 0:
           self.message("Error","Memory Size is Not Defined",
                    "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")

        if all(status.startswith('Allocated') for status in self.memory_status):
                      
            self.message("Error","Memory is full",
                        "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")
            
        else:                 
          for j in range(len(self.job_queue)):
            if j >= 0:
              job = self.job_queue.pop(0)
              self.partitioning_memory(job)

              nearest_power = self.nearest_value(job)
              
              # iterate from the last element from the list to allocate memory from the bottom to top             
              for x in range(len(self.memory_pool_list)-1,-1,-1):
                
                if nearest_power == self.memory_pool_list[x] and self.memory_status[x] == "Free":
                   self.memory_status[x] = f"Allocated ({job} KB)"

                   self.message("Memory Allocated Success","Memory Allocated Succesfully",
                    "Done","Assets/success.ico","Assets/success.png","green","dark green")
                   
                   break

                else:  
                  
                   if nearest_power == self.memory_pool_list[x-1] and "Allocated" in self.memory_status[x-1]:
                     
                      next_nearest_power = nearest_power * 2
                      index = self.memory_pool_list.index(next_nearest_power)
                         
                      for x in range(2):
                        
                        new_index = index + x +1
                        self.memory_pool_list.insert(new_index,next_nearest_power//2)
                        self.memory_status.insert(new_index,"Free")

                        if nearest_power == self.memory_pool_list[x] and self.memory_status[x] == "Free":
                            self.memory_status[x] = f"Allocated ({job} KB)"

                            self.message("Memory Allocated Success","Memory Allocated Succesfully",
                                         "Done","Assets/success.ico","Assets/success.png","green","dark green")
                            
                            break
                
                      self.memory_pool_list.remove(next_nearest_power)
                      self.memory_status.remove(self.memory_status[index])

                   elif nearest_power not in self.memory_pool_list:
                      next_nearest_power = nearest_power * 2

                      index_value = self.memory_pool_list.index(next_nearest_power)

                      if "Allocated" in self.memory_status[index_value]:
                         self.message("Error","Cannot allocate memory",
                                      "Done","Assets/Error.ico","Assets/Error.png","dark red","dark red")
                         break
                      
                      elif self.memory_status[index_value] == "Free":

                        for y in range(2):

                          new_index_value = index_value + y +1
                          self.memory_pool_list.insert(new_index_value,next_nearest_power//2)
                          self.memory_status.insert(new_index_value,"Free")

                        if nearest_power == self.memory_pool_list[x] and self.memory_status[x] == "Free":
                            self.memory_status[x] = f"Allocated ({job} KB)"

                            self.message("Memory Allocated Success","Memory Allocated Succesfully",
                                         "Done","Assets/success.ico","Assets/success.png","green","dark green")
                            break
                        
                        self.memory_pool_list.remove(next_nearest_power)
                        self.memory_status.remove(self.memory_status[index_value])
                
                           
    # free memory
    def free_memory(self):
       
       for j in range(len(self.job_queue)):

          job = self.job_queue.pop(0)
          
          for x in range(len(self.memory_pool_list)-1,-1,-1):

             if job == self.memory_pool_list[x] and "Allocated" in self.memory_status[x]:
                self.memory_status[x] = "Free"

                self.message("Memory Freed Success","Memory Freed Succesfully",
                    "Done","Assets/success.ico","Assets/success.png","green","dark green")
                
                self.merge()

                break
             
    # merging the free adjasance blocks 
    def merge(self):
      for x in range(len(self.memory_pool_list)): 
       
         for i in range(len(self.memory_pool_list)-1,-1,-1):

            if i >= 0 and  i-1>=0: 
      
               if self.memory_pool_list[i] == self.memory_pool_list[i-1] and self.memory_status[i] ==  self.memory_status[i-1] == "Free":
        
                  self.memory_pool_list[i] = self.memory_pool_list[i] + self.memory_pool_list[i-1]  
                  self.memory_status[i] = "Free"
        
                  self.memory_pool_list.pop(i-1)
                  self.memory_status.pop(i-1)
                  
            else:
               i -= 1
             
             
                          
Buddy_System = BuddySystem()
Graphical_User_Interface = Buddy_System.GUI()



