import logging
from itertools import combinations
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

from .models import Funds
from . import mutual_fund as mf


logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Mutual funds index page")

def detail(request, funds_id):
    details = model_to_dict(get_object_or_404(Funds, pk=funds_id))
    response = {"status": "success", "data": details}
    return JsonResponse(response)

def overlap(request):
    funds = request.GET.get('funds', '').split(",")
    objects = []
    
    for fund in funds:
        fund_obj = get_object_or_404(Funds, pk=int(fund))
        objects.append(fund_obj)
    
    overlap, total, common, most_common = mf.get_overlap(objects)
    
    pairwise_overlap_dict = {}
    for comb in combinations(objects, 2):
        pairwise_overlap, pairwise_total, pairwise_common, pairwise_most_common = mf.get_overlap(comb)
        pairwise_overlap_dict[f"{comb[0]} and {comb[1]}"] = pairwise_overlap
    
    partial_overlap = mf.partial_overlap(objects) if len(objects) > 2 else []

    response = {
        "status": "success",
        "data": {
            "overlap": overlap,
            "pairwise_overlap": pairwise_overlap_dict,
            "partial_overlap" : partial_overlap
        }
    }
    
    return JsonResponse(response)

