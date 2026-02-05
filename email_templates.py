def get_contact_confirmation_html(name: str) -> str:
    """
    Zwraca HTML email zgodny z designem strony Racis&Son
    
    Args:
        name: Imię osoby, która wysłała wiadomość
    
    Returns:
        str: Sformatowany HTML email
    """
    return f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Potwierdzenie kontaktu - Racis&Son</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #0f172a; color: #e2e8f0;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #0f172a;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%); border-radius: 16px; border: 1px solid rgba(148, 163, 184, 0.1); backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);">
                    <!-- Header z logo/nazwą -->
                    <tr>
                        <td style="padding: 40px 40px 30px; text-align: center; border-bottom: 1px solid rgba(148, 163, 184, 0.1);">
                            <h1 style="margin: 0; font-size: 32px; font-weight: 800; background: linear-gradient(135deg, #fbbf24 0%, #a3e635 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                                Racis&Son
                            </h1>
                            <p style="margin: 8px 0 0; font-size: 14px; color: #94a3b8;">Koszulki dla prawdziwych kibiców</p>
                        </td>
                    </tr>
                    
                    <!-- Ikonka wiadomości -->
                    <tr>
                        <td style="padding: 30px 40px 20px; text-align: center;">
                            <div style="width: 64px; height: 64px; margin: 0 auto; background: rgba(251, 191, 36, 0.1); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; border: 2px solid rgba(251, 191, 36, 0.3);">
                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <polyline points="22,6 12,13 2,6" stroke="#fbbf24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Treść wiadomości -->
                    <tr>
                        <td style="padding: 0 40px 30px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; font-weight: 700; color: #fbbf24; text-align: center;">
                                Dziękujemy za kontakt!
                            </h2>
                            
                            <p style="margin: 0 0 16px; font-size: 16px; line-height: 1.6; color: #e2e8f0;">
                                Cześć <strong style="color: #fbbf24;">{name}</strong>! 👋
                            </p>
                            
                            <p style="margin: 0 0 16px; font-size: 16px; line-height: 1.6; color: #cbd5e1;">
                                Dziękujemy za kontakt. Twoja wiadomość dotarła do nas i nasz zespół zajmie się nią jak najszybciej.
                            </p>
                            
                            <p style="margin: 0 0 16px; font-size: 16px; line-height: 1.6; color: #cbd5e1;">
                                Prosimy o cierpliwość – dołożymy wszelkich starań, aby odpowiedzieć Ci jak najszybciej! Zazwyczaj odpowiadamy w ciągu <strong style="color: #fbbf24;">24 godzin</strong>.
                            </p>
                            
                            <div style="margin: 30px 0; padding: 20px; background: rgba(251, 191, 36, 0.1); border-left: 4px solid #fbbf24; border-radius: 8px;">
                                <p style="margin: 0; font-size: 14px; line-height: 1.6; color: #cbd5e1;">
                                    💡 <strong style="color: #fbbf24;">Wskazówka:</strong> W międzyczasie możesz przejrzeć naszą kolekcję koszulek na stronie – może znajdziesz coś dla siebie!
                                </p>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Przycisk CTA -->
                    <tr>
                        <td style="padding: 0 40px 40px; text-align: center;">
                            <a href="https://www.racis.store/products" style="display: inline-block; padding: 14px 32px; background: linear-gradient(135deg, #fbbf24 0%, #a3e635 100%); color: #000000; text-decoration: none; font-weight: 600; font-size: 16px; border-radius: 9999px; box-shadow: 0 4px 14px rgba(251, 191, 36, 0.4);">
                                Przejdź do produktów
                            </a>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 30px 40px; border-top: 1px solid rgba(148, 163, 184, 0.1); text-align: center;">
                            <p style="margin: 0 0 12px; font-size: 14px; color: #94a3b8;">
                                Dziękujemy za zaufanie,<br>
                                <strong style="color: #fbbf24;">Zespół Racis&Son</strong>
                            </p>
                            
                            <div style="margin: 20px 0 0;">
                                <p style="margin: 0 0 8px; font-size: 13px; color: #64748b;">
                                    📧 <a href="mailto:kontakt@racis.store" style="color: #fbbf24; text-decoration: none;">kontakt@racis.store</a>
                                </p>
                                <p style="margin: 0; font-size: 13px; color: #64748b;">
                                    📞 +48 600 000 000
                                </p>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Copyright -->
                    <tr>
                        <td style="padding: 20px 40px; text-align: center; background: rgba(15, 23, 42, 0.5); border-radius: 0 0 16px 16px;">
                            <p style="margin: 0; font-size: 12px; color: #64748b;">
                                © 2026 Racis&Son. Wszelkie prawa zastrzeżone.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    """.strip()

def get_order_confirmation_html(order, products: list) -> str:
    """
    Zwraca HTML email potwierdzenia zamówienia ze wszystkimi szczegółami
    
    Args:
        order: Obiekt Order z bazy danych
        products: Lista produktów w zamówieniu
    
    Returns:
        str: Sformatowany HTML email
    """
    # Stałe promocji
    QUANTITY_THRESHOLD = 3
    QUANTITY_DISCOUNT_PERCENT = 15
    
    # Optymalizacja: Wstępne obliczenia
    order_number = order.order_number
    customer_name = order.name
    
    # 1. Oblicz cenę bazową (cena przed rabatami)
    base_price = sum(p.price for p in products)
    
    # 2. Oblicz zniżkę ze sprzedaży produktów
    product_discount = sum(p.price * ((p.sale or 0) / 100.0) for p in products)
    price_after_product_discount = base_price - product_discount
    
    current_price = price_after_product_discount
    
    # 3. Rabat ilościowy (jeśli >= 3 produkty)
    quantity_discount_amount = 0.0
    if len(products) >= QUANTITY_THRESHOLD:
        quantity_discount_amount = current_price * (QUANTITY_DISCOUNT_PERCENT / 100.0)
        current_price -= quantity_discount_amount
    
    # 4. Rabat z kodu
    code_discount_amount = 0.0
    if order.discount_code:
        code_discount_amount = current_price * (order.discount_code.sale / 100.0)
        current_price -= code_discount_amount
    
    final_price = max(0.0, current_price)
    
    # Generuj HTML dla produktów - unikaj f-stringów w pętli
    items_html_parts = []
    for product in products:
        sale_info = ""
        price_display = f'{product.price:.2f} PLN'
        
        if product.sale and product.sale > 0:
            discounted_price = product.price * (1 - (product.sale / 100.0))
            sale_info = f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 6px;"><span style="text-decoration: line-through; color: #94a3b8; font-size: 12px;">{product.price:.2f} PLN</span><span style="background: rgba(239, 68, 68, 0.2); color: #ef4444; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: 600;">-{product.sale}%</span></div>'
            price_display = f'{discounted_price:.2f} PLN'
        
        items_html_parts.append(
            f"""<tr>
                <td style="padding: 14px 0; border-bottom: 1px solid rgba(148, 163, 184, 0.1);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div style="flex: 1;">
                            <div style="font-weight: 600; color: #e2e8f0; margin-bottom: 4px; font-size: 15px;">{product.title}</div>
                            <div style="font-size: 13px; color: #94a3b8;">Rozmiar: <strong>{product.size}</strong> | Wersja: <strong style="color: #fbbf24;">{product.version}</strong></div>
                            {sale_info}
                        </div>
                        <div style="text-align: right; margin-left: 16px; white-space: nowrap;">
                            <div style="font-weight: 600; color: #fbbf24; font-size: 15px;">{price_display}</div>
                        </div>
                    </div>
                </td>
            </tr>"""
        )
    
    items_html = ''.join(items_html_parts)
    
    discount_rows = []
    
    if quantity_discount_amount > 0:
        discount_rows.append(f'''<tr>
                                        <td style="padding: 8px 0; color: #4ade80; font-weight: 600;">Zniżka {QUANTITY_DISCOUNT_PERCENT}%:</td>
                                        <td style="padding: 8px 0; text-align: right; color: #4ade80; font-weight: 600;">-{quantity_discount_amount:.2f} PLN</td>
                                    </tr>''')
    
    if code_discount_amount > 0:
        code_name = order.discount_code.code if hasattr(order.discount_code, 'code') else 'kod promocyjny'
        discount_rows.append(f'''<tr>
                                        <td style="padding: 8px 0; color: #4ade80; font-weight: 600;">Kod {code_name} (-{order.discount_code.sale}%):</td>
                                        <td style="padding: 8px 0; text-align: right; color: #4ade80; font-weight: 600;">-{code_discount_amount:.2f} PLN</td>
                                    </tr>''')
    
    discount_rows_html = ''.join(discount_rows)
    
    return f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Potwierdzenie zamówienia - Racis&Son</title>
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #0f172a; color: #e2e8f0;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #0f172a;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%); border-radius: 16px; border: 1px solid rgba(148, 163, 184, 0.1); backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);">
                    <!-- Header z logo/nazwą -->
                    <tr>
                        <td style="padding: 40px 40px 30px; text-align: center; border-bottom: 1px solid rgba(148, 163, 184, 0.1);">
                            <h1 style="margin: 0; font-size: 32px; font-weight: 800; background: linear-gradient(135deg, #fbbf24 0%, #a3e635 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                                Racis&Son
                            </h1>
                            <p style="margin: 8px 0 0; font-size: 14px; color: #94a3b8;">Koszulki dla prawdziwych kibiców</p>
                        </td>
                    </tr>
                    
                    <!-- Ikonka paczki -->
                    <tr>
                        <td style="padding: 30px 40px 20px; text-align: center;">
                            <div style="width: 64px; height: 64px; margin: 0 auto; background: rgba(74, 222, 128, 0.1); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; border: 2px solid rgba(74, 222, 128, 0.3);">
                                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    <polyline points="22 4 12 14.01 9 11.01" stroke="#4ade80" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Treść wiadomości -->
                    <tr>
                        <td style="padding: 0 40px 30px;">
                            <h2 style="margin: 0 0 8px; font-size: 24px; font-weight: 700; color: #4ade80; text-align: center;">
                                Zamówienie przyjęte!
                            </h2>
                            <p style="margin: 0 0 20px; font-size: 14px; color: #94a3b8; text-align: center;">
                                Numer zamówienia: <strong style="color: #fbbf24; font-size: 16px;">{order_number}</strong>
                            </p>
                            
                            <p style="margin: 0 0 16px; font-size: 16px; line-height: 1.6; color: #e2e8f0;">
                                Cześć <strong style="color: #fbbf24;">{customer_name}</strong>! 👋
                            </p>
                            
                            <p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #cbd5e1;">
                                Dziękujemy za zamówienie! Twoje zamówienie zostało przyjęte i oczekuje na realizację. Nasz zespół dokona ostatecznej weryfikacji i przygotuje Twoją paczkę do doręczenia.
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Sekcja produktów -->
                    <tr>
                        <td style="padding: 0 40px;">
                            <div style="background: rgba(148, 163, 184, 0.05); border: 1px solid rgba(148, 163, 184, 0.1); border-radius: 12px; padding: 20px;">
                                <h3 style="margin: 0 0 16px; font-size: 16px; font-weight: 600; color: #fbbf24;">
                                    📦 Zamówione produkty
                                </h3>
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                    {items_html}
                                </table>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Podsumowanie ceny -->
                    <tr>
                        <td style="padding: 30px 40px;">
                            <div style="background: rgba(251, 191, 36, 0.05); border: 1px solid rgba(251, 191, 36, 0.1); border-radius: 12px; padding: 20px;">
                                <h3 style="margin: 0 0 16px; font-size: 16px; font-weight: 600; color: #fbbf24;">
                                    💰 Podsumowanie
                                </h3>
                                
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="font-size: 14px;">
                                    <tr>
                                        <td style="padding: 8px 0; color: #cbd5e1;">Razem produkty:</td>
                                        <td style="padding: 8px 0; text-align: right; color: #cbd5e1; font-weight: 500;">{price_after_product_discount:.2f} PLN</td>
                                    </tr>
                                    {discount_rows_html}
                                    <tr style="border-top: 2px solid rgba(251, 191, 36, 0.2); border-bottom: 2px solid rgba(251, 191, 36, 0.2);">
                                        <td style="padding: 12px 0; font-size: 16px; font-weight: 700; color: #fbbf24;">Do zapłaty:</td>
                                        <td style="padding: 12px 0; text-align: right; font-size: 16px; font-weight: 700; color: #fbbf24;">{final_price:.2f} PLN</td>
                                    </tr>
                                </table>
                                
                                <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid rgba(148, 163, 184, 0.1);">
                                    <p style="margin: 0 0 8px; font-size: 13px; color: #94a3b8;">
                                        <strong style="color: #e2e8f0;">Metoda dostawy:</strong> {order.shipping_method}
                                    </p>
                                    <p style="margin: 0; font-size: 13px; color: #94a3b8;">
                                        <strong style="color: #e2e8f0;">Płatność:</strong> {order.payment_method}
                                    </p>
                                </div>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Informacja o statusie -->
                    <tr>
                        <td style="padding: 30px 40px;">
                            <div style="background: rgba(74, 222, 128, 0.1); border-left: 4px solid #4ade80; padding: 16px; border-radius: 8px;">
                                <p style="margin: 0; font-size: 14px; line-height: 1.6; color: #cbd5e1;">
                                    Jeśli masz pytania, nie wahaj się nam napisać!
                                </p>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 30px 40px; border-top: 1px solid rgba(148, 163, 184, 0.1); text-align: center;">
                            <p style="margin: 0 0 12px; font-size: 14px; color: #94a3b8;">
                                Dziękujemy za zaufanie,<br>
                                <strong style="color: #fbbf24;">Zespół Racis&Son</strong>
                            </p>
                            
                            <div style="margin: 20px 0 0;">
                                <p style="margin: 0 0 8px; font-size: 13px; color: #64748b;">
                                    📧 <a href="mailto:kontakt@racis.store" style="color: #fbbf24; text-decoration: none;">kontakt@racis.store</a>
                                </p>
                                <p style="margin: 0; font-size: 13px; color: #64748b;">
                                    📞 +48 600 000 000
                                </p>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Copyright -->
                    <tr>
                        <td style="padding: 20px 40px; text-align: center; background: rgba(15, 23, 42, 0.5); border-radius: 0 0 16px 16px;">
                            <p style="margin: 0; font-size: 12px; color: #64748b;">
                                © 2026 Racis&Son. Wszelkie prawa zastrzeżone.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
    """.strip()