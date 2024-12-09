from ml_pipeline.datasets import iris


class DatasetFactory:
    def __init__(self, dataset_config):
        self.datasets = {"iris": {"class": iris.IrisDataSet}}

        for dataset, config in dataset_config.items():
            if dataset in self.datasets:
                self.datasets[dataset]["path"] = config.path
