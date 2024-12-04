import matplotlib.pyplot as plt
import seaborn as sns


class ReportingMixin():
    def save_metrics(self) -> None:
        with open(f"{self.artifact_dir}/metrics", "w") as f:
            for key, value in self.metrics.items():
                f.write("f{key}: {value}\n")
                
    def plot_confusion_matrix(
        self, annot=True, fmt=".2g", xticklabels="auto", ytickables="auto"
    )-> None:
        fig = plt.figure(figsize=(8, 8))
        sns.heatmap(
            self.metrics["cm"],
            square=True,
            annot=annot,
            fmt=fmt,
            xticklabels=xtickables, # type: ignore
            yticklabels=yticklabels, # type: ignore
        )
        plt.xlabel("Predicted Class")
        plt.ylabel("True Class")
        
        fig.savefig(f"{self.artifact_dir}/confusion_matrix.png")