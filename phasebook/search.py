from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    output = []
    # get all the users and stored in user variable
    for user in USERS:

        # if no requested id it will terminate and continue to the next try
        try:
            # check if the user id is the same in the requested id
            if user['id'] == args['id']:
                output.append(user)
                continue
        except:
            output = output

        # if no requested age it will terminate and continue to the next try
        try:
            # check if the user age is the same and greater than and less than 1 in the requested age
            if user['age'] == int(args['age']) or user['age'] == int(args['age']) + 1 or user['age'] == int(args['age']) - 1:
                output.append(user)
                continue
        except:
            output = output

        # if no requested age it will terminate and continue to the next try
        try:
            # check if the user name have the same word
            user['name'].index(args['name'])
            output.append(user)
            continue
        except:
            output = output

        # if no requested accupation it will terminate
        try:
            # check if the user occupation have the same word
            user['occupation'].index(args['occupation'])
            output.append(user)
            continue
        except:
            output = output
    # If no user details are found, return not found. 
    if output == []:
        return "Not Found"

    # return the output in the page
    return output
