import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(page_title="Data Analysis Practical", page_icon="📊", layout="wide")
st.sidebar.title("Pandas Question 🐼 ")

menu = [
    "--  select  --",
    "Q1 Remove NULL Rows",
    "Q2 Remove Fully NULL Rows",
    "Q3 Drop NULL Columns",
    "Q4 Remove Outliers",
    "Q5 Remove Duplicates",
    "Q6 Remove Columns",
    "Q7 Heights Weights Analysis",
    "Q8 IPL Analysis",
    "Q9 Spotify Dataset Analysis",
    "Q10 Car Dataset Analysis",
    "Q11 Data Result Analysis",
    "Q12. Movie Dataset Analysis",
    "Q13. IPL MATCH Analysis",
    "Q14 Sort employees by Dept (Ascending) and Salary (Descending)",
    "Q15. Create a column Average using apply() row-wise",
    "Q16 Replace 'Absent' with 0",
    "Q17. Perform outer merge using indicator=True.",
    "Q19 Group by Dept",
    "Q20 Calculate range (max - min) per team using groupby + apply",
    "Q21 Detect outliers using IQR method",
    "Q22 Find number of unique cities per department",
    "Q23  Create a new column TotalAmount = Price × Quantity using apply() row-wise",
    "Q24 Group employees by Department",
    "Q25 Find the number of employees per department using size()",
    "Q26 kc_house_data Analysis",
    "Q27 supermarket_sales data Analysis",
]

search = st.sidebar.text_input("🔍 Search Question", placeholder="Q10, IPL, Spotify...")

filtered_questions = [q for q in menu if search.lower() in q.lower()]

menu = st.sidebar.selectbox(
    "Select Question", filtered_questions if filtered_questions else menu
)

if menu == "--  select  --":
    st.title("📊 Data Analysis Practice Question")
    tab1, tab2 = st.tabs(["features", "About me"])
    with tab1:
        st.markdown(
            """
        <div style="
        padding:15px;
        border-radius:10px;
        background:linear-gradient(90deg,#2563eb,#7c3aed);
        color:white;
        text-align:center;
        margin-bottom:30px;
        ">
        <h2>🐼 Data Analysis Practice Dashboard</h2>
        <p>Interactive Data Science & Pandas Practical Solutions</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        col1, col2, col3, col4 = st.columns(4)

        col1.markdown(
            """
        <div style="background:#1e293b;padding:15px;border-radius:12px;text-align:center;">
        <h3>📚 27+</h3>
        <p>Questions</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        col2.markdown(
            """
        <div style="background:#1e293b;padding:15px;border-radius:12px;text-align:center;">
        <h3>📂 10+</h3>
        <p>Datasets</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        col3.markdown(
            """
        <div style="background:#1e293b;padding:15px;border-radius:12px;text-align:center;">
        <h3>🐼 4+</h3>
        <p>Libraries</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        col4.markdown(
            """
        <div style="background:#1e293b;padding:15px;border-radius:12px;text-align:center;">
        <h3>📈 15+</h3>
        <p>Charts</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.divider()
        st.subheader("🛠 Technologies Used")
        st.markdown("""
        ✅ Python
        ✅ Pandas
        ✅ NumPy
        ✅ Matplotlib
        ✅ Seaborn
        ✅ Streamlit
        """)
        st.divider()
        st.markdown("""
        ### 🚀 Features

        ✅ Data Cleaning  
        ✅ Outlier Detection  
        ✅ IPL Analysis  
        ✅ Spotify Analysis  
        ✅ Car Dataset Analysis  
        ✅ Interactive Dashboard  
        ✅ Dataset Upload Support
        """)
    with tab2:
        st.markdown(
            """
        <div style="text-align:left;">
            <img src="https://github.com/Deepaksingh-maker.png"
                style="
                    width:140px;
                    height:140px;
                    border-radius:50%;
                    object-fit:cover;
                    border:4px solid #60a5fa;
                    box-shadow:0 0 25px rgba(59,130,246,0.6);
                    margin-bottom:30px;
                ">
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <div style="
        background:linear-gradient(135deg,#0f172a,#1e293b);
        padding:30px;
        border-radius:15px;
        color:white;
        ">
        
        <h1>👨‍💻 Deepak Singh</h1>
        
        <h4>BSc IT Student | Data Science Enthusiast | Future Data Analyst</h4>

        <p>
        I am currently pursuing <b>BSc IT at GLS University</b> and have a strong interest
        in <b>Data Science, Artificial Intelligence, Machine Learning, and Python Development</b>.
        </p>

        <p>
        I enjoy working with real-world datasets, building interactive dashboards,
        performing data analysis, and creating projects that solve practical problems.
        </p>

        <p>
        My goal is to start my career in the field of Data Science and Analytics,
        where I can apply my technical skills and continuously learn new technologies.
        </p>

        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.subheader("🚀 Skills")

        st.markdown("""
        ✅ Python

        ✅ Pandas

        ✅ NumPy

        ✅ Matplotlib

        ✅ Seaborn

        ✅ Streamlit

        ✅ SQL / MySQL

        ✅ C & C++

        ✅ Data Analysis

        ✅ Machine Learning Basics
        """)

        st.divider()

        st.subheader("🎯 Career Objective")

        st.info("""
        Seeking opportunities in Data Science, Data Analytics,
        and Python Development where I can contribute my skills,
        gain industry experience, and grow as a technology professional.
        """)

        st.divider()

        st.subheader("🌐 Connect With Me")

        st.markdown("""
        🔗 GitHub: https://github.com/Deepaksingh-maker

        💼 LinkedIn: https://www.linkedin.com/in/baghel-deepak

        📧 Email: bagheldeepak3400@gmail.com
        """)


elif menu == "Q1 Remove NULL Rows":

    st.header("Q1 Remove Rows with NULL Values")

    data = {
        "name": ["deep", "devil", "smith", np.nan],
        "age": [25, 18, np.nan, 26],
        "sem": [2, 3, 6, 8],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    clean_df = df.dropna()
    st.subheader("After Removing NULL Rows")
    st.dataframe(clean_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            data = {
            "name" :["deep","devil","smith",np.nan],
            "age" : [25,18,np.nan,26],
            "sem" : [2,3,6,8]
                }
            df=pd.DataFrame(data)
            df.dropna()

                """)
elif menu == "Q2 Remove Fully NULL Rows":
    st.header("Q2 Remove Fully NULL Rows")
    data = {
        "name": ["deep", "devil", np.nan, "smith"],
        "age": [25, 18, np.nan, 26],
        "sem": [2, 3, np.nan, 8],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    clean_df = df.dropna(how="all")
    st.subheader("After Removing Fully NULL Rows")
    st.dataframe(clean_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            data = {
            "name" :["deep","devil",np.nan,"smith"],
            "age" : [25,18,np.nan,26],
            "sem" : [2,3,np.nan,8]
                }
            df=pd.DataFrame(data)
            df.dropna(how="all")

                """)
elif menu == "Q3 Drop NULL Columns":
    st.header("Q3 Drop Columns with NULL Values")
    data = {
        "name": ["deep", "devil", "raj", "smith"],
        "age": [25, 18, np.nan, 26],
        "sem": [2, 3, np.nan, 8],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    clean_df = df.dropna(axis=1)
    st.subheader("After Dropping NULL Columns")
    st.dataframe(clean_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            data = {
            "name" :["deep","devil","raj","smith"],
            "age" : [25,18,np.nan,26],
            "sem" : [2,3,np.nan,8]
                }
            df=pd.DataFrame(data)
            df.dropna(axis=1)

                """)
elif menu == "Q4 Remove Outliers":
    st.header("Q4 Remove Outliers using IQR Method")
    file = st.file_uploader("Upload auto-mpg.csv", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.subheader("Dataset")
        st.dataframe(df.head())
        numeric_cols = df.select_dtypes(include=np.number).columns
        column = st.selectbox("Select Column", numeric_cols)
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[column] < lower) | (df[column] > upper)]
        st.subheader("Outliers")
        st.dataframe(outliers)
        clean_df = df[(df[column] >= lower) & (df[column] <= upper)]
        st.subheader("Dataset After Removing Outliers")
        st.dataframe(clean_df)
        fig, ax = plt.subplots()
        sns.boxplot(x=clean_df[column], ax=ax)
        st.pyplot(fig)
        button = st.button("Code")
        if button:
            st.code("""
                import pandas as pd
                file = st.file_uploader(
                    "Upload auto-mpg.csv",
                    type=["csv"]
                )
                if file is not None:
                    df = pd.read_csv(file)
                    numeric_cols = df.select_dtypes(include=np.number).columns
                    column = st.selectbox(
                        "Select Column",
                        numeric_cols
                    )
                    Q1 = df[column].quantile(0.25)
                    Q3 = df[column].quantile(0.75)
                    IQR = Q3 - Q1
                    lower = Q1 - 1.5 * IQR
                    upper = Q3 + 1.5 * IQR
                    outliers = df[
                        (df[column] < lower) |
                        (df[column] > upper)
                    ]
                    clean_df = df[
                        (df[column] >= lower) &
                        (df[column] <= upper)
                    ]

                """)
elif menu == "Q5 Remove Duplicates":
    st.header("Q5 Remove Duplicate Rows")
    data = {
        "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
        "B": [50, 40, 40, 30, 50],
        "C": [True, False, False, False, True],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    st.write("Duplicate Count:", df.duplicated().sum())
    st.subheader("Duplicate Rows")
    st.dataframe(df[df.duplicated()])
    clean_df = df.drop_duplicates().reset_index(drop=True)
    st.subheader("After Removing Duplicates")
    st.dataframe(clean_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            data = {
                    "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
                    "B": [50, 40, 40, 30, 50],
                    "C": [True, False, False, False, True]
                }

                df1 = pd.DataFrame(data)
                df1
                print("Duplicated -> ",df1.duplicated().sum())
                df1[df1.duplicated()]
                df1=df1.drop_duplicates()
                df1 = df1.reset_index(drop = True)
                df1

                """)
elif menu == "Q6 Remove Columns":
    st.header("Q6 Remove mpg and cylinders Columns")
    file = st.file_uploader("Upload auto-mpg.csv", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.subheader("Original Data")
        st.dataframe(df.head())
        new_df = df.drop(columns=["mpg", "cylinders"])
        st.subheader("After Removing Columns")
        st.dataframe(new_df.head())
        button = st.button("Code")
        if button:
            st.code("""
                import pandas as pd
                df2 = pd.read_csv("auto-mpg.csv")
                df2 = df2.drop(columns=["mpg","cylinders"])
                df2
            
            """)

elif menu == "Q7 Heights Weights Analysis":
    st.header("Q7 Heights and Weights Dataset Analysis")
    file = st.file_uploader("Upload heights_weights.csv", type=["csv"])
    if file is not None and file.name == "heights_weights.csv":
        df = pd.read_csv(file)
        with st.expander("2. Dataset Info"):
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander(
            "3. Display basic statistics like mean, std, quartiles, etc. for this data frame."
        ):
            st.subheader("Statistics")
            st.dataframe(df.describe())
        with st.expander(
            "4. Create a correlation table for the data frame and comment about what kind of correlation is there between Height and Weight."
        ):
            st.subheader("Correlation Table")
            st.dataframe(df.corr(numeric_only=True))
            st.subheader("Height Boxplot")
            fig1, ax1 = plt.subplots()
            sns.boxplot(x=df["Height"], ax=ax1)
            st.pyplot(fig1)
        with st.expander("5. Do Height and Weight contain any outliers?"):
            st.subheader("Weight Boxplot")

            fig2, ax2 = plt.subplots()

            sns.boxplot(x=df["Weight"], ax=ax2)

            st.pyplot(fig2)
        button = st.button("Code")
        if button:
            st.code("""
                df3 = pd.read_csv(r"https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/heights_weights.csv")
                df3.info()
                df3.describe()
                df3.corr(numeric_only=True)

                sns.boxplot(df3["Height"])
                plt.show()
                sns.boxplot(df3["Weight"])
                plt.show()

                    """)
    elif file is not None and file.name != "heights_weights.csv":
        st.warning("Please upload the correct file: heights_weights.csv")

elif menu == "Q8 IPL Analysis":
    st.header("Q8 IPL Dataset Analysis")
    file = st.file_uploader("Upload ipl-matches.csv", type=["csv"])
    if file is not None and file.name == "ipl-matches.csv":
        df = pd.read_csv(file)
        st.subheader("Dataset")
        st.dataframe(df.head())
        with st.expander("1 Matches Gone in Super Over"):
            st.subheader("Matches Gone in Super Over")
            super_over = df[df["SuperOver"] == "Y"]
            st.dataframe(
                super_over[["ID", "Team1", "Team2", "WinningTeam", "SuperOver"]]
            )
        with st.expander("2 Chennai Super Kings Won at Kolkata"):
            st.subheader(" Chennai Super Kings Won at Kolkata")
            csk = df[
                (df["WinningTeam"] == "Chennai Super Kings") & (df["City"] == "Kolkata")
            ]
            st.write("Total Wins:", csk.shape[0])
            st.dataframe(csk)
        with st.expander("3 MS Dhoni Player of Match vs Mumbai Indians"):
            st.subheader(" MS Dhoni Player of Match vs Mumbai Indians")
            dhoni = df[
                ((df["Team1"] == "Mumbai Indians") | (df["Team2"] == "Mumbai Indians"))
                & (df["Player_of_Match"] == "MS Dhoni")
            ]
            st.write("Total Matches:", dhoni.shape[0])
            st.dataframe(dhoni)
        with st.expander("4 Gujarat Titans Won Toss + Bat + Match"):
            st.subheader(" Gujarat Titans Won Toss + Bat + Match")
            gt = df[
                (df["TossWinner"] == "Gujarat Titans")
                & (df["TossDecision"] == "bat")
                & (df["WinningTeam"] == "Gujarat Titans")
            ]
            st.dataframe(gt[["ID", "TossWinner", "TossDecision", "WinningTeam"]])
        with st.expander("5 Gujarat Titans Winning Matches"):
            st.subheader(" Gujarat Titans Winning Matches")
            gt_match = df[df["WinningTeam"] == "Gujarat Titans"]
            st.dataframe(gt_match)
        button = st.button("Code")
        if button:
            st.code(""" 

                import pandas as pd
                df4 = pd.read_csv("ipl-matches.csv")
                df4.info()
                                    
                df4["SuperOver"].value_counts()
                z = df4[df4["SuperOver"]=="Y"]
                z[["ID", "Team1", "Team2", "WinningTeam","SuperOver"]]
                
                df4["WinningTeam"].value_counts()
                x=df4[(df4["WinningTeam"]=="Chennai Super Kings") & (df4["City"]=="Kolkata")]
                print("won match -> ",x.shape[0])
                x
                
                MS_Dhoni_won = df4[(df4["Team1"]=="Mumbai Indians") | (df4["Team2"]=="Mumbai Indians") & (df4["Player_of_Match"]=="MS Dhoni")]
                print("--> ",MS_Dhoni_won.shape[0],"Matches MS Dhoni is Player of Match Vs Mumbai Indians.")
                MS_Dhoni_won
                gj_won = df4[(df4["TossWinner"]=="Gujarat Titans") & (df4["TossDecision"]=="bat") & (df4["WinningTeam"]=="Gujarat Titans")]
                gj_won[["ID","TossWinner","TossDecision","WinningTeam"]]
                df4[df4["WinningTeam"]=="Gujarat Titans"]
                """)
    elif file is not None and file.name != "ipl-matches.csv":
        st.warning("Please uplode correct csv file")

elif menu == "Q9 Spotify Dataset Analysis":

    st.header("Q9 Spotify Dataset Analysis")

    file = st.file_uploader("Upload spotify_dirty_dataset_500_rows.csv", type=["csv"])
    if file is not None and file.name == "spotify_dirty_dataset_500_rows.csv":
        df = pd.read_csv(file)
        with st.expander("9.2 Dataset Info"):
            st.subheader("Dataset")
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander("9.3 Summary Statistics"):
            st.subheader("Summary Statistics")
            st.dataframe(df.describe())
        with st.expander("9.4 Correlation Table"):
            st.subheader("Correlation Table")
            corr = df.corr(numeric_only=True)
            st.dataframe(corr)
        with st.expander("9.5 First 5 Rows"):
            st.subheader("First 5 Rows")
            st.dataframe(df.head())
        with st.expander("9.6 Last 5 Rows"):
            st.subheader("Last 5 Rows")
            st.dataframe(df.tail())
        with st.expander("9.7 Rows 15 to 39"):
            st.subheader("Rows 15 to 39")
            st.dataframe(df.iloc[15:40])
        with st.expander("9.8 Last 5 Rows and Last 5 Columns"):
            st.subheader("Last 5 Rows and Last 5 Columns")
            st.dataframe(df.iloc[-5:, -5:])
        with st.expander("9.9 Number of Rows"):
            st.subheader("Shape")
            st.write("--> Number of Rows is - ", df.shape[0])
        with st.expander("9.10 NULL Values Count"):
            st.subheader("NULL Values")
            st.dataframe(df.isnull().sum())
        with st.expander("9.11 Remove First 3 Columns"):
            st.subheader("After Removing First 3 Columns")
            remove_col = df.iloc[:, 3:]
            st.dataframe(remove_col)
        with st.expander("9.12 Remove First 10 Rows"):
            st.subheader("After Removing First 10 Rows")
            remove_row = df.iloc[10:]
            st.dataframe(remove_row)
        button = st.button("Code")
        if button:
            st.code(""" 
                import pandas as pd
                import seaborn as sns
                import matplotlib.pyplot as plt
                df5 = pd.read_csv("spotify_dirty_dataset_500_rows.csv")
                df5

                df5.info()
                df5.describe()
                df5.corr(numeric_only=True)
                df5.head(5)
                df5.tail(5)
                df5.iloc[15:40]
                df5.iloc[-5: , :-5]
                df5.shape[0]
                df5.isnull().sum()
                df5 = df5.iloc[: , 3:]
                df5
                df5=df5.iloc[10:]
                df5
                sns.boxplot(df5["popularity"])
                plt.xticks(rotation=45)
                plt.show()
                sns.boxplot(df5["energy"])
                plt.show()
                Q1 = df5["energy"].quantile(0.25)
                Q3 = df5["energy"].quantile(0.75)
                IQR = Q3 - Q1
                lower = Q1 - 1.5 * IQR
                uper = Q3 + 1.5 * IQR
                energy_out = df5[(df5["energy"] >= lower) | (df5["energy"] <= uper)]
                df5 = energy_out
                df5
                pd.crosstab(df5["mood"],df5["popularity"])
                    """)
    elif file is not None and file.name != "spotify_dirty_dataset_500_rows.csv":
        st.warning("Please upload the correct file: spotify_dirty_dataset_500_rows.csv")
elif menu == "Q10 Car Dataset Analysis":

    st.header("Q10 Car Dataset Analysis")

    file = st.file_uploader("Upload Car data.csv", type=["csv"])

    if file is not None and file.name == "car data.csv":

        df = pd.read_csv(file)

        with st.expander("Dataset Info"):
            from io import StringIO

            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander("Q10.1 Count of Ritz Cars with Kms_Driven > 30000"):
            st.subheader("Q10.1")
            x = df[(df["Car_Name"] == "ritz") & (df["Kms_Driven"] > 30000)].shape[0]
            st.write("Total Cars:", x)
            st.dataframe(df[(df["Car_Name"] == "ritz") & (df["Kms_Driven"] > 30000)])
        with st.expander(
            "Q10.2 Count of Petrol Cars from Year 2017 with Selling Price > 10 Lakh"
        ):
            st.subheader("Q10.2")
            st.dataframe(
                df[
                    (df["Fuel_Type"] == "Petrol")
                    & (df["Year"] == 2017)
                    & (df["Selling_Price"] > 10)
                ]
            )
        with st.expander("Q10.3 Count of Swift Cars with Selling Price > 4 Lakh"):
            st.subheader("Q10.3")
            st.dataframe(df[(df["Car_Name"] == "swift") & (df["Selling_Price"] > 4)])
        with st.expander(
            "4. How many Automatic Transmission Petrol Car are of the year 2015 whose selling price is > 10 Lakhs."
        ):
            st.subheader("Q10.4")
            st.dataframe(
                df[
                    (df["Transmission"] == "Automatic")
                    & (df["Fuel_Type"] == "Petrol")
                    & (df["Year"] == 2015)
                    & (df["Selling_Price"] > 10)
                ]
            )
        with st.expander(
            "10.5. List out Vehicles with Automatic Transmission and selling price < 1 Lakh."
        ):
            st.subheader("Q10.5")
            st.dataframe(
                df[(df["Transmission"] == "Automatic") & (df["Selling_Price"] < 1)]
            )
        with st.expander(
            "10.6. How Many Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included)."
        ):
            st.subheader("Q10.6")
            y = df[
                (df["Kms_Driven"] > 50000)
                & (df["Fuel_Type"] == "Petrol")
                & (df["Year"].between(2010, 2015))
            ]
            st.write(
                "--> ",
                y.shape[0],
                " Petrol Vehicles are there with kms driven more than 50000kms and Year is between 2010 to 2015(both Year included).",
            )
            st.dataframe(
                df[
                    (df["Fuel_Type"] == "Petrol")
                    & (df["Kms_Driven"] > 50000)
                    & (df["Year"] >= 2010)
                    & (df["Year"] <= 2015)
                ]
            )
        button = st.button("Code")
        if button:
            st.code("""
                import pandas as pd
                df6 = pd.read_csv("car data.csv")
                df6.info()
                df6[(df6["Car_Name"]=="ritz") & (df6["Kms_Driven"] > 30000)]
                df6[(df6["Fuel_Type"]=="Petrol") & (df6["Year"]==2017) & (df6["Selling_Price"] > 10)]
                df6[(df6["Car_Name"]=="swift") & (df6["Selling_Price"] > 4)]
                df6[
                    (df6["Transmission"] == "Automatic") &
                    (df6["Fuel_Type"] == "Petrol") &
                    (df6["Year"] == 2015) &
                    (df6["Selling_Price"] > 10)
                ]
                df6[
                    (df6["Transmission"] == "Automatic") &
                    (df6["Selling_Price"] < 1)
                ]
                df6[
                    (df6["Fuel_Type"] == "Petrol") &
                    (df6["Kms_Driven"] > 50000) &
                    (df6["Year"] >= 2010) &
                    (df6["Year"] <= 2015)
                ]

                    """)

    elif file is not None and file.name != "car data.csv":
        st.warning("Please upload the correct file: Car data.csv")

elif menu == "Q11 Data Result Analysis":

    st.header("Q11 Data Result Analysis")

    file = st.file_uploader("upload data_result.csv", type=["csv"])
    if file is not None and file.name == "data_result.csv":
        df = pd.read_csv(file)
        with st.expander("Dataset Info"):
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander("11.2. View the first few rows of the dataset."):
            st.subheader("11.2")
            st.dataframe(df.head())
        with st.expander("11.3. Check the shape of the dataset."):
            st.subheader("11.3")
            st.write("--> Shape of data_result.csv ", df.shape[0])
        with st.expander("11.4. View the first last rows of the dataset"):
            st.subheader("11.4")
            st.dataframe(df.tail())
        with st.expander("11.5. Get summary statistics of numerical columns"):
            st.subheader("11.5")
            st.dataframe(df.describe())
        with st.expander(
            "11.6. Get summary statistics of numerical columns with 0.58 and 0.87 percentiles"
        ):
            st.subheader("11.6")
            st.dataframe(df.describe(percentiles=[0.58, 0.87]))
        with st.expander("11.7. Get summary statistics of all types of columns"):
            st.subheader("11.7")
            st.dataframe(df.describe(include="all"))
        with st.expander("11.8. Information of all columns"):
            st.subheader("11.8")
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander("11.9.Check for missing values"):
            st.subheader("11.9")
            st.dataframe(df.isnull().sum())
        with st.expander("11.10. Removing duplicates if duplicates "):
            st.subheader("11.10")
            st.write("Total Duplicates:", df.duplicated().sum())
            clean_df = df.drop_duplicates().reset_index(drop=True)
            st.dataframe(clean_df)
        with st.expander(
            "11.11. List out female students who have greater than 7 spi in all semesters."
        ):
            st.subheader("11.11")
            st.dataframe(
                df[
                    (df["Gender"] == "Female")
                    & (df["Sem1_SPI"] > 7)
                    & (df["Sem2_SPI"] > 7)
                    & (df["Sem3_SPI"] > 7)
                    & (df["Sem4_SPI"] > 7)
                    & (df["Sem5_SPI"] > 7)
                ]
            )
        with st.expander(
            "11.12. Find number of students those who have greater than 8 spi in all 5 semesters."
        ):
            st.subheader("11.12")
            st.write(
                "--> ",
                df[
                    (df["Sem1_SPI"] > 8)
                    & (df["Sem2_SPI"] > 8)
                    & (df["Sem3_SPI"] > 8)
                    & (df["Sem4_SPI"] > 8)
                    & (df["Sem5_SPI"] > 8)
                ].shape[0],
                " students have greater than 8 spi in all 5 semesters.",
            )
            st.dataframe(
                df[
                    (df["Sem1_SPI"] > 8)
                    & (df["Sem2_SPI"] > 8)
                    & (df["Sem3_SPI"] > 8)
                    & (df["Sem4_SPI"] > 8)
                    & (df["Sem5_SPI"] > 8)
                ]
            )
        with st.expander(
            "11.13. Find outliers of sem 4 result. Also represent statistical analysis with visualization.(boxplot)"
        ):
            st.subheader("11.13")
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=df["Sem4_SPI"])
            plt.xticks(rotation=45)
            st.pyplot(plt)
        button = st.button("Code")
        if button:
            st.code("""
                import pandas as pd
                import seaborn as sns
                import matplotlib.pyplot as plt
                df7 = pd.read_csv("data_result.csv")
                df7.info()
                df7.head()
                df7.shape[0]
                df7.tail()
                df7.describe()
                df7.describe(percentiles=[0.58,0.87])
                df7.describe(include="all")
                df7.info()
                df7.isnull().sum()
                print("Total Duplicates -> ",df7.duplicated().sum())
                clean_df = df7.drop_duplicates().reset_index(drop=True)
                clean_df
                df7[(df7["Gender"]=="Female") & (df7["Sem1_SPI"] > 7) & (df7["Sem2_SPI"] > 7) & (df7["Sem3_SPI"] > 7) & (df7["Sem4_SPI"] > 7) & (df7["Sem5_SPI"] > 7) ]
                print("--> ",df7[(df7["Sem1_SPI"] > 8) & (df7["Sem2_SPI"] > 8) & (df7["Sem3_SPI"] > 8) & (df7["Sem4_SPI"] > 8) & (df7["Sem5_SPI"] > 8)].shape[0]," students have greater than 8 spi in all 5 semesters.")
                df7[(df7["Sem1_SPI"] > 8) & (df7["Sem2_SPI"] > 8) & (df7["Sem3_SPI"] > 8) & (df7["Sem4_SPI"] > 8) & (df7["Sem5_SPI"] > 8)]
                plt.figure(figsize=(8,6))
                sns.boxplot(x=df7["Sem4_SPI"])
                plt.xticks(rotation=45)
                plt.show()
                    """)
    elif file is not None and file.name != "data_result.csv":
        st.warning("Please upload the correct file: data_result.csv")
elif menu == "Q12. Movie Dataset Analysis":

    st.header("Q12 Movie Dataset Analysis")
    file = st.file_uploader("Upload movie_data.csv", type=["csv"])
    if file is not None and file.name == "movie_data.csv":
        df = pd.read_csv(file)
        with st.expander("Dataset Info"):
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander("12.1 List out Movies Released in Year 2019"):
            st.subheader("12.1")
            x = df[(df["year_of_release"] == 2019)]
            st.dataframe(x[["title_x", "year_of_release"]])
        with st.expander(
            "12.2. How Many Movies are having IMDB Rating > 7 (Display Number of Movies)"
        ):
            st.subheader("12.2")
            st.write(
                "--> ",
                df[df["imdb_rating"] > 7].shape[0],
                " Movies are having IMDB Rating > 7.",
            )
            st.dataframe(df[df["imdb_rating"] > 7][["title_x", "imdb_rating"]])
        with st.expander(
            "12.3. List out the Movies with ‘title’ and ‘story’ whose IMDB Votes > 20000"
        ):
            st.subheader("12.3")
            st.dataframe(df[df["imdb_votes"] > 20000][["title_x", "story"]])
        with st.expander(
            "12.4. List out Movies Released in Year 2018, Display only Movie Title with Release Date of Year 2018 Movies"
        ):
            st.subheader("12.4")
            st.dataframe(df[df["year_of_release"] == 2018][["title_x", "release_date"]])
        with st.expander("12.5. Display only Movie Title with its Wikipedia Link."):
            st.subheader("12.5")
            st.dataframe(df[["title_x", "wiki_link"]])
        button = st.button("Code")
        if button:
            st.code("""
                import pandas as pd
                df8 = pd.read_csv("movie_data.csv")
                df8.info()
                df8[df8["year_of_release"]==2019][["title_x","year_of_release"]]
                print("--> ",df8[df8["imdb_rating"] > 7].shape[0]," Movies are having IMDB Rating > 7.")
                df8[df8["imdb_rating"] > 7][["title_x","imdb_rating"]]
                df8[df8["imdb_votes"] > 20000][["title_x","story"]]
                df8[df8["year_of_release"]==2018][["title_x","release_date"]]
                df8[["title_x","wiki_link"]]

                    """)
    elif file is not None and file.name != "movie_data.csv":
        st.warning("Please upload the correct file: movie_data.csv")
elif menu == "Q13. IPL MATCH Analysis":
    st.header("IPL MATCH Analysis [2008 to 2022]")
    file = st.file_uploader("Upload ipl-matches.csv", type=["csv"])
    if file is not None and file.name == "ipl-matches.csv":
        df = pd.read_csv(file)
        with st.expander("Dataset Info"):
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander(
            "13.1 How many matches were won by Gujarat Titans in a Super Over ?"
        ):
            st.subheader("13.1")
            gt_super_over = df[
                (df["WinningTeam"] == "Gujarat Titans") & (df["SuperOver"] == "Y")
            ]
            st.write(
                "--> ",
                gt_super_over.shape[0],
                " matches were won by Gujarat Titans in a Super Over.",
            )
            st.dataframe(gt_super_over[["ID", "WinningTeam", "SuperOver"]])
        with st.expander(
            "13.2 How Many Matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders."
        ):
            st.subheader("13.2")
            rcb_kkr = df[
                (
                    (df["WinningTeam"] == "Royal Challengers Bangalore")
                    & (
                        (df["Team1"] == "Kolkata Knight Riders")
                        | (df["Team2"] == "Kolkata Knight Riders")
                    )
                )
                | (
                    (df["WinningTeam"] == "Kolkata Knight Riders")
                    & (
                        (df["Team1"] == "Royal Challengers Bangalore")
                        | (df["Team2"] == "Royal Challengers Bangalore")
                    )
                )
            ]
            st.write(
                "--> ",
                rcb_kkr.shape[0],
                " Matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders.",
            )
            st.dataframe(rcb_kkr[["ID", "WinningTeam", "Team1", "Team2"]])
        with st.expander("13.3 How many Matches won by Toss Winner of the Match."):
            st.subheader("13.3")
            toss_winner = df[df["TossWinner"] == df["WinningTeam"]]
            st.write(
                "--> ",
                toss_winner.shape[0],
                " Matches won by Toss Winner of the Match.",
            )
            st.dataframe(toss_winner[["ID", "TossWinner", "WinningTeam"]])
        with st.expander(
            "13.4 In how many matches was the result decided by the D/L method and the match was won by wickets?"
        ):
            st.subheader("13.4")
            st.write(
                "--> ",
                df[(df["method"] == "D/L") & (df["WonBy"] == "Wickets")].shape[0],
                " matches was the result decided by the D/L method and the match was won by wickets.",
            )
            st.dataframe(df[(df["method"] == "D/L") & (df["WonBy"] == "Wickets")])
        with st.expander(
            "13.5 In how many matches Toss won by Rajasthan Royals & Won the Match."
        ):
            st.subheader("13.5")
            st.write(
                "--> ",
                df[
                    (df["TossWinner"] == "Rajasthan Royals")
                    & (df["WinningTeam"] == "Rajasthan Royals")
                ].shape[0],
                " matches Toss won by Rajasthan Royals & Won the Match.",
            )
            st.dataframe(
                df[
                    (df["TossWinner"] == "Rajasthan Royals")
                    & (df["WinningTeam"] == "Rajasthan Royals")
                ]
            )
        with st.expander(
            "13.6 In how many matches V Kohli declared player of the match against Chennai Super Kings."
        ):
            st.subheader("13.6")
            st.write(
                "--> ",
                df[
                    (df["Player_of_Match"] == "V Kohli")
                    & (
                        (df["Team1"] == "Chennai Super Kings")
                        | (df["Team2"] == "Chennai Super Kings")
                    )
                ].shape[0],
                " matches V Kohli declared player of the match against Chennai Super Kings.",
            )
            st.dataframe(
                df[
                    (df["Player_of_Match"] == "V Kohli")
                    & (
                        (df["Team1"] == "Chennai Super Kings")
                        | (df["Team2"] == "Chennai Super Kings")
                    )
                ]
            )
        with st.expander(
            "Which Team is the Toss Winner of the Final match Played in Dubai?"
        ):
            st.subheader("13.7")
            final_match = df[(df["City"] == "Dubai") & (df["MatchNumber"] == "Final")][
                "TossWinner"
            ].unique()
            st.write(
                "--> Toss Winner of the Final match Played in Dubai is - ",
                final_match[0],
            )
        with st.expander(
            "13.8 List out the Finals played by Kolkata Knight Riders in which Toss Won by Kolkata Knight Riders in the Finals and choose to field."
        ):
            st.subheader("13.8")
            kkr_finals = df[
                (df["Team1"] == "Kolkata Knight Riders")
                & (df["Team2"] == "Kolkata Knight Riders")
                & (df["MatchNumber"] == "Final")
                & (df["TossWinner"] == "Kolkata Knight Riders")
                & (df["TossDecision"] == "field")
            ]
            st.dataframe(
                kkr_finals[
                    [
                        "ID",
                        "Team1",
                        "Team2",
                        "TossWinner",
                        "TossDecision",
                        "MatchNumber",
                    ]
                ]
            )
        button = st.button("Code")
        if button:
            st.code("""
                import pandas as pd
                df9 = pd.read_csv("ipl-matches.csv")
                df9.info()
                gt_super_over = df9[(df9["WinningTeam"]=="Gujarat Titans") & (df9["SuperOver"]=="Y")]
                print("--> ",gt_super_over.shape[0]," matches were won by Gujarat Titans in a Super Over.")
                gt_super_over[["ID","WinningTeam","SuperOver"]]
                rcb_kkr = df9[
                    (
                        (df9["WinningTeam"] == "Royal Challengers Bangalore") &
                        ((df9["Team1"] == "Kolkata Knight Riders") | (df9["Team2"] == "Kolkata Knight Riders"))
                    ) |
                    (
                        (df9["WinningTeam"] == "Kolkata Knight Riders") &
                        ((df9["Team1"] == "Royal Challengers Bangalore") | (df9["Team2"] == "Royal Challengers Bangalore"))
                    )
                ]
                print("--> ",rcb_kkr.shape[0]," Matches won by Royal Challengers Bangalore Vs Kolkata Knight Riders.")
                rcb_kkr[["ID","WinningTeam","Team1","Team2"]]
                toss_winner = df9[df9["TossWinner"] == df9["WinningTeam"]]
                print("--> ",toss_winner.shape[0]," Matches won by Toss Winner of the Match.")
                toss_winner[["ID","TossWinner","WinningTeam"]]
                df9[(df9["method"]=="D/L") & (df9["WonBy"]=="Wickets")].shape[0]
                df9[(df9["method"]=="D/L") & (df9["WonBy"]=="Wickets")]
                df9[(df9["TossWinner"]=="Rajasthan Royals") & (df9["WinningTeam"]=="Rajasthan Royals")].shape[0]
                df9[(df9["TossWinner"]=="Rajasthan Royals") & (df9["WinningTeam"]=="Rajasthan Royals")]
                df9[(df9["Player_of_Match"]=="V Kohli") & ((df9["Team1"]=="Chennai Super Kings") | (df9["Team2"]=="Chennai Super Kings"))].shape[0]
                df9[(df9["Player_of_Match"]=="V Kohli") & ((df9["Team1"]=="Chennai Super Kings") | (df9["Team2"]=="Chennai Super Kings"))]
                final_match = df9[(df9["City"]=="Dubai") & (df9["MatchNumber"]=="Final")]["TossWinner"].unique()
                print("--> Toss Winner of the Final match Played in Dubai is - ",final_match[0])
                kkr_finals = df9[
                    (df9["Team1"] == "Kolkata Knight Riders") &
                    (df9["Team2"] == "Kolkata Knight Riders") &
                    (df9["MatchNumber"] == "Final") &
                    (df9["TossWinner"] == "Kolkata Knight Riders") &
                    (df9["TossDecision"] == "field")
                ]
                kkr_finals[["ID","Team1","Team2","TossWinner","TossDecision","MatchNumber"]]
                    """)
    elif file is not None and file.name != "ipl-matches.csv":
        st.warning("Please upload the correct file: ipl-matches.csv")
elif menu == "Q14  Sort employees by Dept (Ascending) and Salary (Descending).":
    st.header("Q14 Sort employees by Dept (Ascending) and Salary (Descending).")
    data = {
        "EmpID": [101, 102, 103, 104, 105],
        "Dept": ["IT", "HR", "IT", "Finance", "HR"],
        "Salary": [60000, 45000, 80000, 75000, 50000],
        "Age": [25, 32, 29, 41, 28],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Sort employees by Dept (Ascending) and Salary (Descending)."):
        st.subheader("Sorted Data")
        sorted_df = df.sort_values(by=["Dept", "Salary"], ascending=[True, False])
        st.dataframe(sorted_df)
    with st.expander("After sorting, sort the index in descending order"):
        st.subheader("After Sorting Index in Descending Order")
        sorted_index_df = sorted_df.sort_index(ascending=False)
        st.dataframe(sorted_index_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            data = {
                "EmpID":[101,102,103,104,105],
                "Dept":["IT","HR","IT","Finance","HR"],
                "Salary":[60000,45000,80000,75000,50000],
                "Age":[25,32,29,41,28]
            }
            df = pd.DataFrame(data)
            sorted_df = df.sort_values(by=["Dept","Salary"], ascending=[True,False])
            sorted_index_df = sorted_df.sort_index(ascending=False)
            sorted_index_df
        """)
elif menu == "Q15. Create a column Average using apply() row-wise.":
    data = {
        "Student": ["A", "B", "C", "D"],
        "Math": [70, 45, 90, 60],
        "Science": [75, 40, 85, 55],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Create a column Average using apply() row-wise."):

        def avg_fun(x):
            return (x["Math"] + x["Science"]) / 2

        def grade(x):
            if x >= 80:
                return "Distinction"
            elif x >= 60:
                return "First"
            else:
                return "second"

        df["Average"] = df.apply(avg_fun, axis=1)
        df["Grade"] = df["Average"].apply(grade)
        st.subheader("After Adding Average and Grade Columns")
        st.dataframe(df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            data = {
                "Student":["A","B","C","D"],
                "Math":[70,45,90,60],
                "Science":[75,40,85,55]
                }
            df = pd.DataFrame(data)
            def avg_fun(x):
                return (x["Math"] + x["Science"]) / 2
            def grade(x):
                if x >=80:
                    return "Distinction"
                elif x >= 60:
                    return "First"
                else:
                    return "second"
            df["Average"] = df.apply(avg_fun, axis=1)
            df["Grade"] = df["Average"].apply(grade)
            df
        """)
elif menu == "Q16 Replace 'Absent' with 0":
    data = {
        "Student": ["A", "B", "C", "D"],
        "Math": [70, "Absent", 90, 60],
        "Science": [75, 40, "Absent", 55],
    }
    df = pd.DataFrame(data)
    st.subheader("Original Data")
    st.dataframe(df)
    st.subheader("After Replacing 'Absent' with 0")
    df.replace("Absent", 0, inplace=True)
    st.dataframe(df)
elif menu == "Q17. Perform outer merge using indicator=True.":
    students = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["A", "B", "C", "D"]})
    marks = pd.DataFrame({"ID": [2, 3, 5], "Score": [85, 90, 75]})
    # st.dataframe(students)
    with st.expander("Students and Marks Data"):
        st.subheader("Students Data")
        st.dataframe(students)
        st.divider()
        st.subheader("Marks data")
        st.dataframe(marks)
    with st.expander("Outer Merge using indicator=True"):
        merge_data = pd.merge(students, marks, how="outer", indicator=True)
        st.subheader("Outer Merge with Indicator")
        st.dataframe(merge_data)
    with st.expander("Count of both rows"):
        both_count = (merge_data["_merge"] == "both").sum()
        st.write("--> Count of rows from both: ", both_count)
    with st.expander("Count of students only"):
        student_only = (merge_data["_merge"] == "left_only").sum()
        st.write("--> Count of students only: ", student_only)
    with st.expander("Count of marks only"):
        marks_only = (merge_data["_merge"] == "right_only").sum()
        st.write("--> Count of marks only: ", marks_only)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            students = pd.DataFrame({
                "ID":[1,2,3,4],
                "Name":["A","B","C","D"]
                })
                            marks = pd.DataFrame({
                "ID":[2,3,5],
                "Score":[85,90,75]
                })
                merge_data =pd.merge(students,marks,how="outer",indicator=True)
                merge_data
                both_count = (merge_data["_merge"]=="both").sum()
                print(f"--> Students present in both tables {both_count}")
                student_only = (merge_data["_merge"]=="left_only").sum()
                print(f"--> Only in students {student_only}")
                marks_only = (merge_data["_merge"]=="right_only").sum()
                print(f"--> Only in marks {marks_only}")
                """)
elif menu == "Q19 Group by Dept":
    df = pd.DataFrame(
        {
            "Dept": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
            "Salary": [50000, 70000, 40000, 60000, 80000, 75000],
        }
    )
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Group by Dept and Calculate Mean Salary"):
        group_data = df.groupby("Dept")["Salary"].agg(["mean", "median", "max"])
        st.subheader("Mean Salary by Dept")
        st.dataframe(group_data)
elif menu == "Q20 Calculate range (max - min) per team using groupby + apply":
    df = pd.DataFrame({"Team": ["A", "A", "A", "B", "B"], "Runs": [50, 70, 80, 40, 60]})
    x = df.groupby("Team")["Runs"].apply(max) - df.groupby("Team")["Runs"].apply(min)
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Calculate range (max - min) per team using groupby + apply"):
        st.subheader("Range of Runs per Team")
        st.dataframe(x)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            df = pd.DataFrame({
                "Team":["A","A","A","B","B"],
                "Runs":[50,70,80,40,60] 
            })
            x = df.groupby("Team")["Runs"].apply(max) - df.groupby("Team")["Runs"].apply(min)
            x
        """)
elif menu == "Q21 Detect outliers using IQR method":
    df = pd.DataFrame({"Salary": [20000, 22000, 21000, 25000, 24000, 300000]})
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Detect outliers using boxplot"):
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df["Salary"])
        plt.xticks(rotation=45)
        st.pyplot(plt)
    with st.expander("Detect outliers using IQR method"):
        Q1 = df["Salary"].quantile(0.25)
        Q3 = df["Salary"].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)]
        st.subheader("Outliers Detected")
        st.dataframe(outliers)
    with st.expander("Remove Outliers and Show Cleaned Data"):
        clean_df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]
        st.subheader("Data after Removing Outliers")
        st.dataframe(clean_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            import seaborn as sns
            import matplotlib.pyplot as plt
            df = pd.DataFrame({
                "Salary":[20000,22000,21000,25000,24000,300000]
            })
            plt.figure(figsize=(8,6))
            sns.boxplot(x=df["Salary"])
            plt.xticks(rotation=45)
            plt.show()
            Q1 = df["Salary"].quantile(0.25)
            Q3 = df["Salary"].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df["Salary"] < lower_bound) | (df["Salary"] > upper_bound)]
            clean_df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]
        """)
elif menu == "Q22 Find number of unique cities per department":
    df = pd.DataFrame(
        {
            "Dept": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
            "Employee": ["A", "B", "C", "D", "E", "F"],
            "City": ["X", "X", "Y", "Z", "X", "Y"],
        }
    )
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Number of unique cities per department"):
        unique_cities = df.groupby("Dept")["City"].nunique()
        st.subheader("Number of Unique Cities per Dept")
        st.dataframe(unique_cities)
    with st.expander("One random employee per department."):
        st.subheader("One Random Employee per Dept")
        x = df.groupby("Dept").sample(1)
        st.dataframe(x)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            df = pd.DataFrame({
                "Dept":["IT","IT","HR","HR","Finance","Finance"],
                "Employee":["A","B","C","D","E","F"],
                "City":["X","X","Y","Z","X","Y"]
            })
            unique_cities = df.groupby("Dept")["City"].nunique()
            print("Number of Unique Cities per Dept")
            print(unique_cities)
            x = df.groupby("Dept").sample(1)
            print("One Random Employee per Dept")
            print(x)
        """)
elif (
    menu
    == "Q23  Create a new column TotalAmount = Price × Quantity using apply() row-wise"
):
    df = pd.DataFrame(
        {
            "Product": ["P1", "P2", "P3", "P4", "P5"],
            "Price": [100, 200, 150, 300, 250],
            "Quantity": [5, 2, 4, 1, 3],
        }
    )
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander(
        "Create a new column TotalAmount = Price × Quantity using apply() row-wise"
    ):
        df["TotalAmount"] = df["Price"] * df["Quantity"]
        st.subheader("Data after Adding TotalAmount Column")
        st.dataframe(df)
    with st.expander("Sort the DataFrame by TotalAmount in descending order."):
        sorted_df = df.sort_values(by="TotalAmount", ascending=False)
        st.subheader("Data Sorted by TotalAmount (Descending)")
        st.dataframe(sorted_df)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            df = pd.DataFrame({
                "Product":["P1","P2","P3","P4","P5"],
                "Price":[100,200,150,300,250],
                "Quantity":[5,2,4,1,3]
            })
            df["TotalAmount"] = df["Price"] * df["Quantity"]
            sorted_df = df.sort_values(by="TotalAmount", ascending=False)
            sorted_df
        """)
elif menu == "Q24 Group employees by Department":
    df = pd.DataFrame(
        {
            "Employee": ["A", "B", "C", "D", "E"],
            "Dept": ["IT", "HR", "IT", "Finance", "HR"],
            "Salary": [50000, 40000, 70000, 80000, 45000],
        }
    )
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Calculate total salary and average salary per department."):
        salary_stats = df.groupby("Dept")["Salary"].agg(["sum", "mean"])
        st.subheader("Total Salary and Average Salary per Dept")
        st.dataframe(salary_stats)
    with st.expander(
        "Display departments where average salary is greater than 50,000."
    ):
        high_avg_salary = salary_stats[salary_stats["mean"] > 50000]
        st.subheader("Departments with Average Salary > 50,000")
        st.dataframe(high_avg_salary)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            df = pd.DataFrame({
                "Employee":["A","B","C","D","E"],
                "Dept":["IT","HR","IT","Finance","HR"],
                "Salary":[50000,40000,70000,80000,45000]
            })
            salary_stats = df.groupby("Dept")["Salary"].agg(["sum","mean"])
            high_avg_salary = salary_stats[salary_stats["mean"] > 50000]
            high_avg_salary
        """)
elif menu == "Q25 Find the number of employees per department using size()":
    df = pd.DataFrame(
        {
            "Dept": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
            "Employee": ["A", "B", "C", "D", "E", "F"],
            "Experience": [2, 5, 3, 7, 4, 6],
        }
    )
    st.subheader("Original Data")
    st.dataframe(df)
    with st.expander("Find the number of employees per department using size()"):
        employee_count = df.groupby("Dept").size()
        st.subheader("Number of Employees per Dept")
        st.dataframe(employee_count)
    with st.expander(
        "Find the employee with highest experience in each department using nth() or sorting."
    ):
        highest_experience = df.loc[df.groupby("Dept")["Experience"].idxmax()]
        st.subheader("Employee with Highest Experience per Dept")
        st.dataframe(highest_experience)
    button = st.button("Code")
    if button:
        st.code("""
            import pandas as pd
            df = pd.DataFrame({
                "Dept":["IT","IT","HR","HR","Finance","Finance"],
                "Employee":["A","B","C","D","E","F"],
                "Experience":[2,5,3,7,4,6]
            })
            employee_count = df.groupby("Dept").size()
            highest_experience = df.loc[df.groupby("Dept")["Experience"].idxmax()]
            highest_experience
        """)
elif menu == "Q26 kc_house_data Analysis":
    st.header("Q26 kc_house_data Analysis")
    file = st.file_uploader("Upload kc_house_data.csv", type=["csv"])
    if file is not None and file.name == "kc_house_data.csv":
        df = pd.read_csv(file)
        with st.expander("Dataset Info"):
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        with st.expander("2) Display the first 5 rows of the dataframe."):
            st.subheader("2) First 5 rows of the dataframe")
            st.dataframe(df.head())
        with st.expander("3) Drop the columns 'id' and 'Unnamed: 0'"):
            st.subheader("3) After Dropping 'id' and 'Unnamed: 0' columns")
            df.drop(columns=["id", "Unnamed: 0"], inplace=True)
            st.dataframe(df)
        with st.expander(
            "4) Check all the null values present in all the columns of the dataframe."
        ):
            st.subheader("4) Null values in each column")
            st.dataframe(df.isnull().sum())
        with st.expander(
            "5) Fill the missing values of the column 'bedrooms' with the mean of the column."
        ):
            st.subheader("5) After Filling Missing Values in 'bedrooms' column")
            df["bedrooms"].fillna(df["bedrooms"].mean(), inplace=True)
            st.dataframe(df.isnull().sum())
        with st.expander(
            "6) Fill the missing values of the column 'bathrooms' with the mean of the column."
        ):
            st.subheader("6) After Filling Missing Values in 'bathrooms' column")
            df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True)
            st.dataframe(df.isnull().sum())
        with st.expander(
            "7) Use the Pandas method corr() to find the feature other than price that is most correlated with price and mention your answer as a comment."
        ):
            st.subheader("7) Correlation of features with price")
            correlation = df.corr()
            st.dataframe(correlation["price"].sort_values(ascending=False))
            st.write(
                "The feature most correlated with price is 'sqft_living' with a correlation coefficient of 0.702035."
            )
        with st.expander(
            "8) Fit a linear regression model to predict the 'price' using the list of features:"
        ):
            st.subheader("coming soon....")
        with st.expander("9) Consider 30% testing samples and use random state 10."):
            st.subheader("coming soon...")
        with st.expander("10) Find the Mean Squared Error"):
            st.subheader("coming soon...")
        button = st.button("code")
        if button:
            st.code("""
                import pandas as pd
                df26 = pd.read_csv("kc_house_data.csv")
                df26
                # 2) Display the first 5 rows of the dataframe.
                df26.head(5)
                # 3) Drop the columns "id" and "Unnamed: 0"
                df26.drop(columns=["id","Unnamed: 0"],inplace=True)
                # 4) Check all the null values present in all the columns of the dataframe.
                df26.isnull().sum()
                # 5) Fill the missing values of the column 'bedrooms' with the mean of the column.
                df26["bedrooms"].fillna(df26["bedrooms"].mean(),inplace=True)
                df26.isnull().sum()
                # 6) Fill the missing values of the column 'bathrooms' with the mean of the column.
                df26["bathrooms"].fillna(df26["bathrooms"].mean(),inplace=True)
                df26.isnull().sum()
                # 7) Use the Pandas method corr() to find the feature other than price that is most correlated with price and mention your answer as a comment.
                df26.corr(numeric_only=True)
                    """)
    elif file is not None and file.name != "kc_house_data.csv":
        st.warning("please uplode correct csv file")
elif menu == "Q27 supermarket_sales data Analysis":
    st.header("supermarket_sales data Analysis")
    file = st.file_uploader("uplode supermarket_sales.csv", type=["csv"])
    if file is not None and file.name == "supermarket_sales.csv":
        df = pd.read_csv(file)
        with st.expander("data frame"):
            st.subheader("orignal data frame")
            st.dataframe(df)
        with st.expander(
            "1). Load the dataset into a pandas DataFrame and read fi rst 8 rows"
        ):
            st.dataframe(df.head(8))
        with st.expander(
            "2). Check for missing values and fi ll it by mean values of that particularcolumn if any. "
        ):
            with st.expander("Before fill null value"):
                st.subheader("null value ")
                st.dataframe(df.isnull().sum())
            with st.expander("fill quantity null value"):
                st.subheader("fill quantity null value")
                st.dataframe(df["Quantity"].fillna(df["Quantity"].mean(), inplace=True))
            with st.expander("fill rating null value"):
                st.subheader("fill Rating null value")
                st.dataframe(df["Rating"].fillna(df["Rating"].mean(), inplace=True))
            with st.expander("After fill null value"):
                st.subheader("null value")
                st.dataframe(df.isnull().sum())
        with st.expander(
            " 3). Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greaterthan 600). "
        ):
            st.subheader(
                "Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greaterthan 600)."
            )
            x = df[
                (df["Quantity"] < 3) & ((df["Rating"] > 8.5) | (df["Total"] > 600))
            ].shape[0]
            st.success(x)
        with st.expander(
            " 4). Find the sum of ‘Total’ purchasing price spent by Member and Normal 'Customer type'."
        ):
            st.subheader("coming soon...")
        with st.expander(
            " 5). Find the percentage of total of ‘grossincome’ based on the different ‘Payment’ methods used by customers. (Ewallet, Cash and Credit card) "
        ):
            st.subheader("coming soon...")
        with st.expander(
            " 6). Analyze the purchasing behavior ofmale and female customers using ‘Gender’ column. Find their average purchase prices using ‘Total’ column"
        ):
            st.subheader("coming soon...")
        with st.expander(
            " 7). Create a scatter plot that showsthe relationship between total amount spent and rating. (keep ‘+’ marker, with marker size 100 and green color)"
        ):
            st.subheader("coming soon...")
        with st.expander(
            " 8). Create a box plot that showsthe distribution of ‘Rating’ and ‘Quantity’. And comment about outliers in both columns."
        ):
            st.subheader("coming soon...")
        with st.expander(
            "  9). Visualize with parallel co-ordinates for ‘Unit price’,‘Total’, ’cogs’ columns’ data with respect to ‘Product line’."
        ):
            st.subheader("coming soon...")
        button = st.button("code")
        if button:
            st.code("""
            import pandas as pd
            df27 = pd.read_csv("supermarket_sales.csv")
            df27
            # 1). Load the dataset into a pandas DataFrame and read fi rst 8 rows. 
            df27.head(8)
            # 2). Check for missing values and fi ll it by mean values of that particularcolumn if any. 
            df27.isnull().sum()
            df27["Quantity"].fillna(df27["Quantity"].mean(),inplace=True)
            df27["Rating"].fillna(df27["Rating"].mean(),inplace=True)
            df27.isnull().sum()
            # 3). Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greaterthan 600). 
            df27[(df27["Quantity"] < 3 ) & ((df27["Rating"] > 8.5 ) | (df27["Total"] > 600 )) ].shape[0]
            
            """)
    elif file is not None and file.name != "supermarket_sales.csv":
        st.warning("please uplode correct csv file")


st.markdown("---", unsafe_allow_html=True)

st.markdown(
    """
<div style="
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
">
<h3>📊 Data Analysis Practical Dashboard</h3>
<p>
    👨‍💻 <b>Deepak Singh</b><br>
    🎓 BSc IT | GLS University<br>
    🚀 Data Science | AI | Machine Learning
</p>

<p>
    <a href="https://github.com/Deepaksingh-maker" target="_blank"
    style="text-decoration:none; color:white; font-size:18px;">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg"
             width="22" style="vertical-align:middle;">
        GitHub Profile
    </a>
</p>

<p style="font-size:14px;">
    © 2026 Deepak Singh. All Rights Reserved.
</p>
</div>
""",
    unsafe_allow_html=True,
)
