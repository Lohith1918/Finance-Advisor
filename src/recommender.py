def generate_recommendations(income, savings, model):
    features = [[income, savings]]
    prediction = model.predict(features)
    return f"Based on your inputs, your recommended expenditure is ₹{prediction[0]:.2f}"
