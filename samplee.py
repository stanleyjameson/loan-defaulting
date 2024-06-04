if predict_button:
  
    user_credit_score = calculate_credit_score(annual_income, work_exp, years_in_current_employment, 
                                               marital_status, house_ownership, vehicle_ownership)
    
    with col2:
        st.write(f"Calculated Credit Score: {user_credit_score}")
        
