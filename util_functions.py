import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


def df_split(df, target, test_size=0.2, random_seed=42):
	"""
	Function used to split the dataframe into a training set and a test set.
	Arguments:
		- df: our original dataframe
		- target: our target variable
		- test_size: what size our test set should be
		- random_seed: random seed to use as random state; for replicating results
	Returns:
		- df: our new training dataframe
		- df_test: our test dataframe
	"""

	cols = df.columns.values
	y = df[target].values
	X = df.drop(target, axis=1).values


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=True, random_state=random_seed, stratify=y)

	df = pd.DataFrame(X_train, columns=cols[:-1])
	df[target] = y_train

	df_test = pd.DataFrame(X_test, columns=cols[:-1])
	df_test[target] = y_test

	return df, df_test


def df_rename(df):
    """
    Rename some predetermined variables in our dataframe.
    Arguments:
        - df: the dataframe to be renamed
    Returns:
        - df: the renamed dataframe
    """
    
    df = df.rename(index=str, columns={'Teaching_Hospital_ID': 'hospital',
                                 'Physician_Profile_ID': 'phy_ID',
                                 'Physician_First_Name': 'phy_first_name',
                                 'Physician_Last_Name': 'phy_last_name',
                                 'Recipient_Primary_Business_Street_Address_Line1': 'address',
                                 'Recipient_City': 'city',
                                 'Recipient_State': 'state',
                                 'Recipient_Zip_Code': 'zip_code',
                                 'Physician_Primary_Type': 'phy_primary_type',
                                 'Physician_Specialty': 'phy_specialty', 
                                 'Physician_License_State_code1': 'phy_state',
                                 'Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name': 'submitting_GPO_name',
                                 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name': 'paying_GPO_name',
                                 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State': 'paying_GPO_state',
                                 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country': 'paying_GPO_country',
                                 'Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID': 'paying_GPO_ID',
                                 'Total_Amount_of_Payment_USDollars': 'payment_amount',
                                 'Date_of_Payment': 'payment_date',
                                 'Form_of_Payment_or_Transfer_of_Value': 'payment_form',
                                 'Covered_or_Noncovered_Indicator_1': 'product1_covered',
                                 'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1': 'product1_type',
                                 'Product_Category_or_Therapeutic_Area_1': 'product1_category',
                                 'Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1': 'product1_name',
                                 'Associated_Drug_or_Biological_NDC_1': 'product1_associated',
                                 'Covered_or_Noncovered_Indicator_2': 'product2_covered',
                                 'Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2': 'product2_type',
                                 'Product_Category_or_Therapeutic_Area_2': 'product2_category',
                                 'Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2': 'product2_name',
                                 'Associated_Drug_or_Biological_NDC_2': 'product2_associated'})
    return df