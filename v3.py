import pandas as pd
import matplotlib.pyplot as plt

# Data Validation
def validate_data(data):
    # Check for required columns
    required_columns = ["date", "value"]
    missing_columns = set(required_columns) - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    # Check data types
    if data["date"].dtype != "datetime64[ns]":
        raise TypeError("Invalid data type for 'date' column. Expected datetime64[ns].")

    if not pd.api.types.is_numeric_dtype(data["value"]):
        raise TypeError("Invalid data type for 'value' column. Expected numeric.")

    # Additional data constraints or validations can be performed here


# Interactive Visualization Selection
def select_visualizations():
    available_visualizations = ["line", "bar", "scatter"]
    selected_visualizations = []

    print("Available visualizations:")
    for i, vis in enumerate(available_visualizations):
        print(f"{i+1}. {vis}")

    while True:
        choice = input("Select a visualization (or 'done' to finish): ")
        if choice.lower() == "done":
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(available_visualizations):
                selected_visualizations.append(available_visualizations[index])
                print(f"Visualization '{available_visualizations[index]}' selected.")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    return selected_visualizations


# Export Dashboard
def export_dashboard(figure, file_format="pdf"):
    if file_format.lower() == "pdf":
        figure.savefig("dashboard.pdf", format="pdf")
        print("Dashboard exported as PDF.")
    elif file_format.lower() == "html":
        figure.savefig("dashboard.html", format="html")
        print("Dashboard exported as HTML.")
    else:
        print("Unsupported file format.")


# Dashboard Customization
def customize_dashboard(figure):
    title = input("Enter dashboard title: ")
    figure.suptitle(title)

    # Additional customization options can be added here


# Data Filtering
def filter_data(data):
    while True:
        filter_value = input("Enter a filter value (or 'done' to finish): ")
        if filter_value.lower() == "done":
            break

        try:
            filter_condition = data["value"] > float(filter_value)
            data = data[filter_condition]
            print(f"{len(data)} records remaining after filtering.")
        except ValueError:
            print("Invalid filter value. Please try again.")

    return data


def main():
    # Load data
    data = pd.read_csv("data.csv")

    # Data Validation
    validate_data(data)

    # Interactive Visualization Selection
    selected_visualizations = select_visualizations()

    # Generate Visualizations
    for vis in selected_visualizations:
        if vis == "line":
            plt.plot(data["date"], data["value"], label="Value")
        elif vis == "bar":
            plt.bar(data["date"], data["value"], label="Value")
        elif vis == "scatter":
            plt.scatter(data["date"], data["value"], label="Value")

    plt.legend()

    # Dashboard Customization
    customize_dashboard(plt.gcf())

    # Data Filtering
    filtered_data = filter_data(data)

    # Export Dashboard
    export_dashboard(plt.gcf(), file_format="pdf")

    plt.show()


if __name__ == "__main__":
    main()
