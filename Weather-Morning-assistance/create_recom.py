from data_preparation import weather

def make_recom(w):
    msg=""
    total_txt=["Today's Weather:"]
    total_txt.append(w["W_C"])
    if w["Prob_p"]>=60:
        msg="Take umbrella, raincoat."
    elif 40<w["Prob_p"]<60 :
        msg="probably you might need an umbrella."
    total_txt.append(msg)
    t=int(w["T"])
    total_txt.append(f"Temperature_ave:{t}")
    if w["T"]<10:
        msg="wear a warm jacket."
    if 10<=w["T"]<18:
        msg="take a light jacket."
    if 18<=w["T"]<28:
        msg="comfortable clothes is recommended."
    if w["T"]>28:
        msg="wear light clothes and stay hydrated."
    total_txt.append(msg)
    return "\n".join(total_txt)

message=make_recom(weather)
