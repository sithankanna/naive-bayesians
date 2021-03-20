import pandas as pd


class FeatureFactory:
    def __init__(self, date_col: str = None, hierarchical_col: str = None) -> None:
        """ """

        self.date_col = date_col
        self.hierarchical_col = hierarchical_col

        if date_col is None:
            self.date_col = "date"
        else:
            self.date_col = date_col

        self.features = []

    def calendar_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add calendar related features

        Parameters:
            df (pd.DataFrame): DataFrame with a date columns
        Returns:
            pd.DataFrame: Data .


        """
        date = df[self.date_col]

        calendar_features = {
            "day_of_week": self.day_of_week(date),
            "week_of_month": self.week_of_month(date),
            "week_of_year": self.week_of_year(date),
            "month": self.month(date),
        }

        df = df.assign(**calendar_features)

        self.features += list(calendar_features.keys())
        return df

    def week_of_month(self, date: pd.Series) -> pd.Series:
        """Get week number in a month.

        Parameters:
            dates (pd.Series): Series of dates.

        Returns:
            pd.Series: Week number in a month.
        """
        firstday_in_month = date - pd.to_timedelta(date.dt.day - 1, unit="d")
        return (date.dt.day - 1 + firstday_in_month.dt.weekday) // 7 + 1

    def week_of_year(self, date: pd.Series) -> pd.Series:
        """Get week number in a month.

        Parameters:
            date (pd.Series): Series of dates.

        Returns:
            pd.Series: Week number in a year.
        """

        return date.dt.week

    def month(self, date: pd.Series) -> pd.Series:
        """Get week number in a month.

        Parameters:
            date (pd.Series): Series of dates.

        Returns:
            pd.Series: Month number in a year.
        """

        return date.dt.month

    def day_of_week(self, date: pd.Series) -> pd.Series:
        """Get week number in a month.

        Parameters:
            date (pd.Series): Series of dates.

        Returns:
            pd.Series: Month number in a year.
        """

        return date.dt.dayofweek

    def hierarchical_features(
        self, df: pd.DataFrame, hierarchical_col: str
    ) -> pd.DataFrame:
        if hierarchical_col is None:
            index_col = 0
        else:
            distinct_values = set(df[hierarchical_col])
            mapping = {val: i for i, val in enumerate(distinct_values)}
            index_col = df[hierarchical_col].map(mapping)

        df = df.assign(**{"hierarchical_index": index_col})

        # self.features += ["hierarchical_index"]
        return df