import streamlit as st
import app_api
import app_db


st.set_page_config(page_title = 'Streamlit App')
st.title('API CALLING APP')

menu = st.sidebar.selectbox('Choose Your Option',
                            ('API CALL', 'SELECT ALL', 'INSERT RECORD','UPDATE RECORD', 'DELETE RECORD'))

if menu == 'API CALL':
    movie_id = st.number_input("Enter movie by ID: ", min_value=1)
    result = app_api.get_movie_Info_By_ID(movie_id)

    if st.button("DISPLAY API DATA"):
        if result == 'ERROR':
            st.error("YOUR MOVIE ID IS NOT FOUND")
        else:
            st.write(result)

elif menu == 'INSERT RECORD':
    movie_name = st.text_input('Enter movie name: ')
    country = st.text_input('Enter movie country: ')
    year = st.number_input('Enter year of movie: ', min_value = 1975,max_value=2026)
    imdb_rate = st.number_input('Rating of the movie: ', max_value=9.9)

    if st.button('ADD TO DB'):
        app_db.insert_record(movie_name, country, year, imdb_rate)
        st.success('record added to database succsesfully')

elif menu == 'UPDATE RECORD':
    movie_name= st.text_input("Enter OLD name of the movie: ")
    country= st.text_input("Enter the NEW country: ")
    year= st.number_input("Enter the NEW Year: ", max_value=2026)
    imdb_rate = st.number_input('Enter The NEW Rating: ',max_value=9.9)
    if st.button('Update'):
        app_db.update_record(movie_name, country, year, imdb_rate)
        st.success('Record UPDATED!')

elif menu == 'SELECT ALL':
    records = app_db.select_all_records()
    st.table(records)

elif menu == 'DELETE RECORD':
    movie_name = st.text_input("Enter movie name to delete:")
    if st.button("Delete"):
        app_db.delete_record(movie_name)
        st.success("Record deleted!")
