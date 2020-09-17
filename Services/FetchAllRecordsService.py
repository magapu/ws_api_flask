from flask import Flask, jsonify
from Constants.UrlConstants import UrlConstants
from Entities.User import UserDetails


class FetchAllRecordsService(UrlConstants):

    @classmethod
    def fetch_all_records_from_db(cls):
        res = []
        data = UserDetails.query.all()
        if data is not None:
            for row in data:
                res.append(
                    {UrlConstants.Id: row.Id, UrlConstants.firstName: row.firstName,
                     UrlConstants.lastName: row.lastName})
            return jsonify(res)
        return res
