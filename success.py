def success(result):
    if result.lower() == "success":
        print("Congratulations!")
    else:
        print("It's a lesson to be learned and an opportunity" \
        " to rise again and " \
        "keep fighting without giving up.")

success("success")
success("échec")
success("Success")