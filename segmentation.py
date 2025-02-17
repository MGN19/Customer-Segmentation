customer_info = [
    'customer_region', 'customer_age', 'is_repeat_customer']

temporal_data = [
    'first_order', 'last_order', 'days_between',
    *['HR_' + str(i) for i in range(1, 24)], 
    *['DOW_' + str(i) for i in range(7)], 
    '0_7h', '8_14h', '15_19h', '20_23h',
    'weekend_orders', 'weekday_orders']

temporal_data_ratios = ['first_order', 'last_order', 'days_between',
                        *['DOW_' + str(i) + '_ratio' for i in range(7)],
                        *['HR_' + str(i) + '_ratio' for i in range(1, 24)],
                        'weekend_weekday_ratio', '0_7h', '8_14h', '15_19h', '20_23h',
                        'weekend_orders', 'weekday_orders']


product_vendor = [
    'vendor_count', 'product_count', 'is_chain']

spending_orders = [
    'total_orders', 'total_spend', 'avg_spend_prod',
    'promo_DELIVERY', 'promo_DISCOUNT', 'promo_FREEBIE',
    'payment_method', 'pay_CARD', 'pay_CASH', 
    'payment_method_enc', 'last_promo_enc',
    *['HR_' + str(i) for i in range(1, 24)], 
    *['DOW_' + str(i) for i in range(7)], ]

cuisine_preferences = ['CUI_American',
                    'CUI_Asian',
                    'CUI_Beverages',
                    'CUI_Cafe',
                    'CUI_Chicken Dishes',
                    'CUI_Chinese',
                    'CUI_Desserts',
                    'CUI_Healthy',
                    'CUI_Indian',
                    'CUI_Italian',
                    'CUI_Japanese',
                    'CUI_Noodle Dishes',
                    'CUI_OTHER',
                    'CUI_Street Food / Snacks',
                    'CUI_Thai']