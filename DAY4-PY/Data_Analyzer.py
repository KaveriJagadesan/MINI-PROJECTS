import pandas as pd
import numpy as np

class DataAnalyzer:
    """
    A class to encapsulate common data analysis functions on a Pandas DataFrame.

    Attributes:
        df (pd.DataFrame): The DataFrame to be analyzed.
    """
    def __init__(self, df):
        """
        Constructor for the DataAnalyzer class.

        Args:
            df (pd.DataFrame): The DataFrame to be analyzed.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The input must be a Pandas DataFrame.")
        self.df = df.copy()  # Use .copy() to avoid modifying the original DataFrame

    def show_summary(self):
        """
        Prints a summary of the DataFrame, including non-null counts, data types,
        and descriptive statistics for numerical and categorical columns.
        """
        print("--- DataFrame Info ---")
        self.df.info()
        print("\n--- Descriptive Statistics ---")
        print(self.df.describe(include='all'))  # include='all' covers both numeric and object types

    def get_column_stats(self, column_name):
        """
        Returns or prints descriptive statistics for a specific column.

        Args:
            column_name (str): The name of the column to analyze.

        Returns:
            pd.Series or None: A Series with descriptive statistics if the column exists,
                                otherwise None.
        """
        if column_name not in self.df.columns:
            print(f"Error: Column '{column_name}' not found.")
            return None
        return self.df[column_name].describe(include='all')

    def impute_missing_values(self, column_name, strategy):
        """
        Imputes missing values in a specified column using a given strategy.

        Args:
            column_name (str): The name of the column with missing values.
            strategy (str): The imputation strategy. Options are 'mean', 'median', or 'mode'.
        """
        if column_name not in self.df.columns:
            print(f"Error: Column '{column_name}' not found.")
            return

        if strategy in ['mean', 'median'] and not pd.api.types.is_numeric_dtype(self.df[column_name]):
            print(f"Error: Strategy '{strategy}' is not suitable for non-numeric column '{column_name}'.")
            return
            
        if strategy == 'mean':
            fill_value = self.df[column_name].mean()
            self.df[column_name].fillna(fill_value, inplace=True)
            print(f"Filled missing values in '{column_name}' with the mean: {fill_value}")
        elif strategy == 'median':
            fill_value = self.df[column_name].median()
            self.df[column_name].fillna(fill_value, inplace=True)
            print(f"Filled missing values in '{column_name}' with the median: {fill_value}")
        elif strategy == 'mode':
            # Use iloc[0] to get the first mode in case of multiple modes
            fill_value = self.df[column_name].mode().iloc[0]
            self.df[column_name].fillna(fill_value, inplace=True)
            print(f"Filled missing values in '{column_name}' with the mode: {fill_value}")
        else:
            print(f"Error: Invalid strategy '{strategy}'. Use 'mean', 'median', or 'mode'.")
### Example Usage ###
def _example_usage():
    # 1. Create a sample DataFrame with missing values
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, np.nan, 35, 25],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York', np.nan],
        'Salary': [50000, 60000, 75000, 80000, np.nan]
    }
    my_data = pd.DataFrame(data)

    # 2. Create an instance of the DataAnalyzer class
    analyzer = DataAnalyzer(my_data)

    # 3. Use the methods to perform analysis and manipulation
    print("--- Initial DataFrame ---\n", my_data, "\n")

    # Show a summary of the data
    analyzer.show_summary()

    # Get statistics for a specific column
    print("\n--- Statistics for 'Age' Column ---")
    print(analyzer.get_column_stats('Age'))

    # Impute missing values for numeric and categorical columns
    print("\n--- Imputing Missing Values ---")
    analyzer.impute_missing_values('Age', 'mean')
    analyzer.impute_missing_values('City', 'mode')
    analyzer.impute_missing_values('Salary', 'median')

    # View the updated DataFrame inside the analyzer object
    print("\n--- DataFrame After Imputation ---")
    print(analyzer.df)

    # Show summary again to see the changes
    print("\n--- Updated Summary ---")
    analyzer.show_summary()


if __name__ == "__main__":
    _example_usage()
