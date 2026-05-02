def total_pengeluaran(uang_kos, makan, bensin, kuota, laundry, lainnya):
    total = uang_kos + makan + bensin + kuota + laundry + lainnya
    return total

def cek_budget(total, budget):
    if total > budget:
        return "Pengeluaran kamu melebihi budget!"
    elif total == budget:
        return "Pengeluaran kamu pas dengan budget."
    else:
        return "Pengeluaran kamu masih aman, bagus!"
