import flet as ft

def main(page: ft.Page):
    page.title = "Tuition Fee Calculator"
    page.window.width = 400
    page.window.height = 700
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT

    # Inputs
    units = ft.TextField(label="No. of Units", value="21", keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.MENU_BOOK)
    rate = ft.TextField(label="Rate per Unit (₱)", value="650", keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.PAYMENTS)
    misc = ft.TextField(label="Miscellaneous Fees (₱)", value="2500", keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.RECEIPT_LONG)
    discount = ft.TextField(label="Discount / Scholarship (%)", value="0", keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.LOCAL_OFFER)

    result_text = ft.Text("", size=16)
    total_card = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Total Tuition", size=14, color=ft.Colors.GREY_600),
                ft.Text("₱0.00", size=32, weight=ft.FontWeight.BOLD, key="total"),
            ], spacing=4),
            padding=20,
        ),
        visible=False
    )

    def calculate(e):
        try:
            u = float(units.value or 0)
            r = float(rate.value or 0)
            m = float(misc.value or 0)
            d = float(discount.value or 0)

            subtotal = (u * r) + m
            discount_amount = subtotal * (d / 100)
            total = subtotal - discount_amount

            total_card.content.content.controls[1].value = f"₱{total:,.2f}"
            result_text.value = f"Tuition: ₱{u*r:,.2f}\nMisc: ₱{m:,.2f}\nDiscount: -₱{discount_amount:,.2f}\nSubtotal: ₱{subtotal:,.2f}"
            total_card.visible = True
            page.update()
        except:
            result_text.value = "Please enter valid numbers."
            page.update()

    def clear_all(e):
        units.value = ""
        rate.value = ""
        misc.value = ""
        discount.value = "0"
        total_card.visible = False
        result_text.value = ""
        page.update()

    page.add(
        ft.Text("Tuition Fee Calculator", size=26, weight=ft.FontWeight.BOLD),
        ft.Text("Enter your fees to compute total", size=13, color=ft.Colors.GREY_600),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        units,
        rate,
        misc,
        discount,
        ft.Row([
            ft.ElevatedButton("Calculate", icon=ft.Icons.CALCULATE, on_click=calculate, expand=True, height=45),
            ft.OutlinedButton("Clear", on_click=clear_all, height=45),
        ], spacing=10),
        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        total_card,
        result_text,
    )
ft.app(target=main)