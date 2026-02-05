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
                                Prosimy o cierpliwość – dołożymy wszelkich starań, aby odpowiedzieć Ci jak najszybciej! Zazwyczaj odpowiadamy w ciągu <strong style="color: #fbbf24;">24-48 godzin</strong>.
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
                            <a href="https://twoja-domena.pl/products" style="display: inline-block; padding: 14px 32px; background: linear-gradient(135deg, #fbbf24 0%, #a3e635 100%); color: #000000; text-decoration: none; font-weight: 600; font-size: 16px; border-radius: 9999px; box-shadow: 0 4px 14px rgba(251, 191, 36, 0.4);">
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
                                    📧 <a href="mailto:RacisAndSon@gmail.com" style="color: #fbbf24; text-decoration: none;">RacisAndSon@gmail.com</a>
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