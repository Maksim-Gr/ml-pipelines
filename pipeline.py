def pipeline_task(task_func):
    task_func.is_task = True
    return task_func



class MLPipeline:
    def __init__(self):
        
        
        self.tasks = []
        # 'tasks' is a list of DAG vertices
        for task in tasks:
            try: 
                func = getattr(self, task)
            except AttributeError:
                raise Exception(f"'{task}' is not defined in the pipeline")
            
            if hasattr(func, "is_task"):
                self.tasks.append(func)
            else:
                raise Exception(f"'{task}' is not a pipeline task")
            
            
    @pipeline_task
    def load_data(self) -> None:
        pass
    
    @pipeline_task
    def preprocess_data(self) -> None:
        pass
    
    def not_a_task(self, a, b) -> None:
        pass
    
    def run(self) -> None:
        for task in self.tasks:
            task()