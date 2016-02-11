from flask import Blueprint, request, Response
import json
import hmac
import hashlib
import request as r

subApp = Blueprint('intra', __name__)