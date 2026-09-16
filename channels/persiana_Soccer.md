<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/l0oCevYuAzu8-6evub6TXK_nCnwt-wU05fsP3PBBF6K5Qx4mntzGR6pQlHpTd-Ghb6AixaLqtLNchxwmp0NFA8y3wt7j_1p4sFU6CNbZhs6TKo7G0JHYzV4-rQe5--X2S-tsu8_ISxZwGG6pL-ts6HfnNZCxHMS2iqkz5ZdZUuHnrb96YX4mdj4BEJZGMlOvzQ75uVF17s6QIqIL4HSmXLt4esf14-j1ZlKjoYyRQRmnF41KOjiqnHjlNYRwfvTDXzpTI1pZRp7IhToU9CvLXTKGrvegZkEPJIFxnZW_IWGDSY1UXlpsJwbDUJ6QykCez0604nZy3Fx6_9-hI12Jzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 502K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-29900">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzkkfGmG_oRI1PH97QiRFSc2K-MsTNmzQgfz5x7KDQVAFhCskDVJ69KvcsoLg3C2y2S0NER0JLUmtDnI4p-kNGMW4r3HqPKb-jgvd7J4EpauggJ2IYHVGDdAEsr_xzOWxiYCMFYFrTOk-8FXTPq3IJrZ2YVDjgY4bDwquXJ471GNBISi-LAgX2EGRtxNRYrXgvWz-FlLutiyDp0x40l1x5SQbeUlJPXn7infj7JWcAuoBmZcvWe1Wp5gyxKEntpWt6-8gpmwUblk_HuiUcjV1q1sgtx1ttk6NASoDT2jZNwvzkezOq-_-xR62eZpj9kreLgDFt1rXpoSO4c_5gQO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش یان دیومانده خرید جدید رئال مادرید به شعار هواداران الچه که دیشب شعار سر میدادند که رئال کثیف ترین تیمه. اینم از حرکت دیومانده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/29900" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29899">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX4Z-5TuBvTvp0Ng9LdFtnZ6Gi-3kDhug_aeTV11BJM_nDvjnazFULm5LZfvnOxXwSnLJSuBOeImgoYgMJ4kAJ4sL7UZNhpHRMNNowXmz2TxXdVwJfiWEMQQG5qbIOynm74KyYy7UDQK0aPdANnkbZMQvhh2AHZtj7ZtaTOVOpM_nL3xxG1RPBocQ5Z0wk4hujSVtqxEKiExN7m_L6ZSyQtiIeiS0g6OFE3eujI9ISlWgdb4g4x-WY5yySN9PzAzJum7-tPltC5uCdCjetQ9CA-bHrVE0Ttc3eBmD64z96XyFuFityDch54dMjJM1eP-n0mzTrv2s5MRc4nS65velg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لالیگا
|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/29899" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29898">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvJI7VD6VHcIjAJp-h693styN4lvEaDwYNtSkFF8OheA4Lio8TG6wkvEY6ugIaRaUeL2Mn0Qn4SYOrdUD9PH6qsIDQaa95jKJbd-a4DYQlxX8WVw3AgpkyICBkpSBTrrcywRjVS-jWzM0sL2zgm0W5eoytuLcjz-43G3lYQEZ02pCUS-8bxnJnswiMdSkyFll87u-FuxU1kn2XXqWp5vjEaiWkSPoHfzGnsgakvaa2CfGIyhK-nXpwt-dApA1caUR24RbWWXspHrLyReOlVsj2dKl_bizs7BsiI4BvDX5KPCYnz9Mmin31nR3X1TbDGpHpUrF98jymykvZ7IqyZgVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/29898" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29897">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcsV9vPaVIUgQ7rQ2v9YNahWbNg-VwByWVmp39bHSoyd2-V59jzOHwLwriqcymbRpgOVFUk5XAtzm2Uh-XBCH5wEnM9F7-oVR5_Nbx6G52KNoIMZS7SEHxzO-YKjzxauxpJY564_eF-uz42xRikgVnoyOky6ZdZd6irHfkeUIl66xJVhhy0HfGXPuBeOqKx9R7GV2T-UcbzHLgFwNW6lIGrw_4hUbNt3qk1F1ivo-vF2HUFUoeIMP5VyYRR-bEezwWcd8px4FkQekA5nvX_V_TShijo0UIwcs70fHZthaZXMjE40kT_rtKdxKmkb78GyQuiA_MlY-Kp8YA97UlYj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رونمایی باشگاه پرسپولیس از فرشته کریمی خرید جدید خود؛ کریمی از 18 سالگی تاکنون درتیم‌ملی فوتسال حضور داشت و بعد از خدافظی از این رشته به تیم بانوان فوتبال پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/29897" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29896">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM0ZxNxQfOPHARf_R-guO7Ps4jLW3xDhV1eqfmjVDMARB_Xm9ar33T0iO7zS2H6jslFws1KzBW3ke_R16QTsbKWdMfyBwddXhJ46S-6b-xwn2Sl8-b2c2j9WX9CfgyZCOxu63NdfvKQPZRKdNtOcTN_ZNmkvDVEwPkXsKtrYNPzU4JNjWwQ4QDvdohy27b56Xomjm1tv50UuMrYp4orZWVaJpdKl1oLVWVJ4BpKeTATynpnW8Z4M0JADh1-fHGwsVR1XbG64Y3TcVX4nzSplPky3yz0S9nOy4NY-3XhQottmHh05KJXagLVgXa6fhNy52NeH8Hix0Q3q4XUwEmBd-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو ساعت مونده تا شروع بازی میلان و بنفیکا؛
میلان تو پنج بازی آخرش باختی نداشته و سه بازی آخرش روبرده. تو این بازی میزبان هم هست. اگه یک میلیون روی برد تیم آث میلان شرط ببندی ۲/۳۰۰/۰۰۰ برنده می‌شی. احتمال بردش بالاست. توی سایت زیر درعرض ۳۰ ثانیه ثبتنام‌کن و در صورت برنده شدن به صورت آنی برداشت بزن: "
لینک ورود به سایت
"
⚪️
@persiana_soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/29896" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29895">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmoO8WaoJJTrb-lMvod_t6rErKjgWIYX1aBLvDIx1DxvxknnHvvdawNEag-XEGTU0M4kW0jkQ1yvsgOYHTQg6NkBpRRfhZuAt__sylK8yMz2ID5u846CZoaatfzYBMTH0AqVp4qQdo1LTl4iRbKcL8CplJH4NxsrMHXAW9PZ_OzdgujK7hWGProE7CNtedp1NrQsV_1H888Ph9c_UsWwygbblLLgs__Q1f1InhxViqEJVZvTyZEut7yPmEnE1zambLBP1e1RXAZ6tAWsxjSsgpAj2CvWv8UWWr57WCjHEPuJ1gNxghBc67vgKkpNRkXt8elqlkJmZwz6Rek1Loo3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ یکی‌از مسئولان سازمان لیگ امروز صبح به‌مدیریت‌تراکتور اخطارداده درصورت استفاده ازعلیرضا بیرانوند در بازی با استقلال در هفته هشتم لیگ برتر که روز پنجشنبه 16 مهر ماه برگزار میشود بازی سه‌برصفر به سود آبی‌پوشان میشود. اتفاقی که سال قبل برای سینا خادمپور…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/29895" target="_blank">📅 20:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29894">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA2qVOnvnP-nKxgVlG160pifUFPm5uMX6tdjjGI7LIoET_tUdjeksLV2_hfu1rjC_W6hMHG6yT9RXdLoJuTtuQ9bYUXU4CmPcvcagbrT6qpu8gOBeYvS959HNt6UzC15l5MFJJ7gajUC0wqFe7vGYp1DhgEarP0lLimAsbYR7XyA-wPpZenJv0ELxvJjeKTsIzwa-S4gsW_a9jE2bRF1Dxec5wlWLjAO5dbzJROTdYI4y8UmBCnXjH7y7-RB5MpBbm6MHgbIVxP_3CS5ng9jU6PLxWiKJaAH2yb6YqrhfVUUhX4ldiezucc5VH-ciUQHZ1cRokpBAgmUPcGYD5Lhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه: پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه.…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29894" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29893">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HILbmyK5hihWRQPE_K6tTYs2GUgAQXwUq8wjLnKlb6bS5QjlxBy3QUwvJtKyFRKb5esCjPkbXs9GuUCB6dkBwBYCYaEfZVHLBtTrZ0U5C-GVoJWf5kpTqqxhR-tnPyaF2EmTeKRWarFCAgZCE91ecauEVeFkzN47FUYnJIZwAayG6vWM8vjG9pRwaQjui9Yz6Ez4ZbNOcGNj3OLHyJ-B6vqLZ07VUtkQAzs131wBnGZ4kkpyNa5pUSC2tA-AA8m2G9XIcF96my4Eagvd1RpBHq_xXXB4cq0smTzeYXa0qLEE1Cta73P-WEZ8TTLKfQoZ0d-JR0pzj2WH9UvsUx1Qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
رئیس‌سابق‌اینترمیلان:
سال2012 خواستم به هرشکلی‌که‌شده لیونل‌مسی رو به این تیم بیارم. به او پیشنهادسالانه 500 میلیون یورو دادم و حتی معاون باشگاه رو هم به اسپانیافرستادم‌که او رو راضی کنه که از بارسا به اینتر بیاد اما لئو حتی نامه‌ای که من براش فرستاده بودم رو باز نکرد و آفر رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/29893" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29892">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paz2wId1lXrBecRDpItTt26HXoem70yN_0DXKEjjJBFfcPU5OEnxhjGD3ZVInfq8rMnr6w8l4a9ylvt5MuECItkXyiA7PP6H_kzwlSdQ0kfpQLDqw9FZO8bdS6YIHqqpDbIBiqS3OmsA09xlEwhlxwcGm_LVoXdCTxoL7OcfULTi_7lzN0QBnRC1u5XWd8TuUIdN7Iwk0TtEtVYKjxgKaCyiANXQOvJwLDUlwPVosps4Z--UTVzdAkpSo3tmlvixsi7VgC6GFWJUUJKzArsnt4jWraMgFJ93hOg_93etVqtu_9b1wAozqqMXJRq7taeXCAF7ctRYztKCf50CXz9m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/29892" target="_blank">📅 20:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29891">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRRr2Aci6lZ-mvbVfMkLcYjhZicvsG-xG1Rbo0IxS-CTMbwUGxJR3YrfXuMvHMsEON6lSZi0M8WEhWDUIwUjWkMT9DtTlbBm5CPX9mq7hUWKy1SnRzudD3foJN2khRDc-80yeDBqlyIyYhMVfd9yk0Y78c6BapN1noO_UlZa33LKcQfClzQkGhsjDxizRIXQJdKmdTlmltCJ0dpmtFTDxeZZhQXJtw_rxDE1OypmM0sClpyds3QIOs0HDS32XYflTlwfs-kbMf_Rr0xpfjNE2je3nZqf-aU04uhroieuH2H2JHCQ2xPl4I2QupUEDa93LBMo1A8DNudByYo1Qcazqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان: یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/29891" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W58zsQq6ya1gMm-NeyNgPqY6iFZs4cpUufzWejXEm6CnwOTBaIBrE6LbiLiPpZkQao3tX77sdMRLad3EscTr06camy5oElYK69gJpF1cljSWIQKAvqjpRWS3JpV-Kk9jKpYcT2ULYwv68aeFQFc46v6yeDNv7lUNMdhRYbKLyCk0yxdDI6b9Q_tQMg4VQl8RiS_-RGxmPnq7c8gLGPF_-N7T3YnFiNrpd2X4TBHSztjETOvnAHOGYFVTWNQ6tmm-dOlRatnNN9MRTDnPNN-Jt7V8JMZ9dgqgVQ2sWeG7mJ5fSp-l18bxlawi424On4VduTCGT-TjrYPJQJ-KpcRgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
یوونتوس در نقل‌ و انتقالات پیش فصل؛
سه‌مهاجم‌فصل‌گذشته خود را فروخت و سه مهاجم جدید گرفت. مهاجمان سابق‌یووه این فصل روی هم هفت‌گل‌زده‌اند درحالی مهاجمان جدید بیانکونری در این فصل هنوز موفق به گلزنی در سری‌آ نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/29890" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29889">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDP6sKlv7sDxJdjLPPc4vQ8ymBzQjjqWdPxQAmFu6nQ_l-A_xCzVl2vNsTgZobE_m0IEqQUiMqhfGLUlmxx3YyD6RxDy3tjHcOl0L421r2cEb_KolvCyzlrLT5cO_tomytrQogdRCz7DPSpbcdHkJ9BqTmTi1RjyBEqmKFE18UoPTKCyn6Pmf7ZSNUu18mAhGwaYmmWaEbjvYVExuCsN0w_3qq718xaGu3sAwDrCgbOirJ80KxQJ9Fpvc9UsN3K4NVFRX--r56bSp8KfwqFdZ8H5nLJf7PFvtAJWksYAcX7VWM2_IvRGt4ucKNb9hWJvSYZP6e270Ca60FniuyWyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
اگه تو این اوضاع اقتصادی بد دنبال یه راه مطمئن واسه کسب درامد میگردی دارک بت بهترین گزینس
💵
💵
💵
🤩
۱۰٪ هدیه ی نقدی برای تمامی‌واریزها
✔️
🤩
تحلیل آمار و شرایط بازی
✔️
🤩
بررسی آپشن‌های مهم
✔️
🤩
چالشهای متنوع همراه با جوایز نقدی
✔️
🤩
جبران خسارت برای کاربران فعال
✔️
💎
کانال دارکبت محیطی امن برای کسانی که به فوتبال با چشم تماشاگر نگاه نمیکنند بلکه دنبال یه درآمد مطمئن از این راه هستند
🔥
💵
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/29889" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29887">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1ChuR3yx_Y8oJtW86yYrviKsfjQyhvHTvQyHrTuaDmSsiyAs6AHBLoXeXJXmoIUjuLJaray7hNPFMWeBjwkX3w3HGfAANEoyJPSZI3vaxf16jM4RFLGPXFpGCp4dY9kcDIrISSAQrNDLNJda9nBekx_20uCUZIiNK0sZ8g041sBAEX_90vswTa5LtwRhWy49HkiI6Nlktn8vw48xAR5VYGAmBVdo8QBQ4ed_8u8A9zTBLxlUvUGlbaON8GKIV9HzvoZSCeMBMcmwciEUTfxCmqFiDpTjc6L784xCgqRwvg43mXQNDtCw3zRjIqwk3h3B1X00yLqCf0VNQBK2fqcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/29887" target="_blank">📅 19:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29886">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDti5yAQV-m6fhpR8LXcuf9GkwZ-GUXEbheiWqjH848L48nP1DAZGaU5KRjDlFi47cFgrgOPFo7b29pzL0fZ1tPLIl0W84XC9Q4EtTFGbK5ipDJ5dIIurnk8PQgfWo0piSNdpBJ9DZJIDmlbUUBAJ5Tnyfk3m1S34t45ef_CkB3r_n2XpEyZ3APNLUyuVJIFOLSWIzqG9KfQv6tmuv-BU0x0D9UbSVgWbY5VX5jkkYpx2cAemM46G-O6bhPRMyuB-YfdMUCtNKWYF2ekxrQVKoLBDJVQKODQ5HiBZbJYhy4GXi0nMjUrIy3GLWEmmGk7M-sjyFObLRePu-JLNNz_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/29886" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29885">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R52eR578eXpklm1FBIV1GRWuBM4aIO-6e0nfOOgLJY7Djt-lnr2aaMd3UOAjbSycLY4Cmx9ykppCNjhCJn_KPCtgnOzWropd2a3igS-h2s_I5ZFb3x-Z5owrydKOGbXe8om8svqCnBQA6QyT6ZzbEFOrW-wfyoD9WFFAKAbNqLw1Zk-zI56rk5hGkmY4eCG4JewKaIO2179qu8N6QXpQnUqgUHfoJOX1SHLXa-coksuOTdDILptnljc4ZQcDL6btUJFk7NvRKq1nF9O4pkWp5uqJWDwf_qw_vsJK98LKIRC8poIIMnaAkwjlUigI9RHu6Z7BQSL_Q6wOgAFJqmKo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو: این زمستون رو نبین ما هم بهاری داشتیم. افسوس که نامه جوانی‌ام طی شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29885" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29884">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1SZcH2z6WMjk9oPYn-QQ-H6VY6KAb8-t54_3lAbsbv6qIrW0scf4JKYmI-hSQEN__-nejYfkb6EfSQv3eWfK9QDbZ5fjbD3Tw1zBjnnaFtAWK6HRdf8pmHmE-0uVnXWZSCO5m1AkRc3X4CSFg9kH6kVPBS68haBB6JmNbQEGsy0TlCiKQrXzlRz9ux7DRhiUb0k3mfLlTnHfsEthevUQqs2n4ptKm5j_oOFBDB_ZHyfkhPc-qZUSlcdMU-pITpJk_kiM_gP90rKBiz3-BH5_EUGAxVrUhb_IHkyqFvv56nIcmiVEwSbpVEl06OKh5sPDkaaY64IpOM0L2M3CJJcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ازابتدای‌این‌فصل تا کنون 17 موقعیت‌گل‌صدرصدی رو در بازی‌های رئال مادرید از دست داده‌که باعث‌شاکی‌شدن هواداران رئال شده. پرز هفتگی داره 600 هزار دلار به وینی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29884" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29883">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29883" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29882">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/29882" target="_blank">📅 17:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29881">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت
؛ علیرضا بیرانوند، داوود نوشی صوفیانی و فرزین گروسیان سه دروازه‌بانی هستند که تا پایان هفته هفتم لیگ برتر موفق به ثبت پاس گل شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29881" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utuex_a_ANeu6HGDsuJ7IfnyNHMCgCtyNWRNSmZkm5FdbQsScxww8kCUrVLglsUmCqGAKDxqO6gemXdm0ivj_Azq9JIzrUuwUggUeHEURh9WLNEenvkbLjzuokMbHixfb6Im9cotzOnMWDOYNIf-WdO-DO2QMZoryB5lEjppK_YTngyS0e-MADzoIvciMrIzyes5jG0p9BSzBGM1ukOnLaa_rkUvrYt47FAZVZXmua_bBCZE-ILfHSzaB3ktZ4wMDz4HglaU9NlQfw5C-46ymQl7Mv2R4wcJCJk5zhm8X_VpOCAYkwoK1vkmRS__fqFSK0p8wroiW2Yo2IOgFSSHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان:
یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم روزی کاری میکنم هرجا رفتی با افتخار بگی زلاتان شاگرد من بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/29879" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29878">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltBCX1xXLJYktdvEGNgkp40J2FTulOnXHRVQ0D-wSzxXrcpdul8UbinTVXCV5B6pYDwIRscTCZPueQyI7ywBalWnyLVR1meRzkpy4rz6vN6yb7Tw9jvfoprWDcHF4RrfsJxrtzpLcYCXRnadUGiGBnptGEKcPKnKk4Q1skkBbEGd-ut0CEVmI4IOiTia1nICO0k0jdCNu8n8y103z-p05KlbSPMXzQfIa7HIpiYDUrGEOepI6eo3gKKSeAd5aYml6qtNCFZeMVQcNfa4pIl1oqhs8I-BmBONomOsYTI_JbLBrvLDXOs_6If7zHV5n1KJEe0QJlRI9nAo70C8gQTVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌معاون‌سازمان‌نظام‌وظیفه؛ از بین قایدی، حسینی، قلی زاده و جهانبخش تنها کاپیتان تیم ملی علیرضت جهانبخش معافیت تحصیلی اش به پایان رسیده و باید تکلیف سربازی‌اش رو روشن کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29878" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29877">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf87MZ2OL1TQR4cSkxAKjb0ymmoMDOMf_YHe-PyrSGhjSx-Lne-hF5CigwSchuzkAIYN_ZU_5oU1o6ShTRXn_y3V5TqrFXZuy8wFdMBTa4h51xTqxAQ0wYsJ6o6GbY1V1R9x3Hh0EP9BoY7-_FHEfJJ9cew03qu1EReF62vsOcsgVlpRwNp7TcEVay42-5XyJJpoJeXxJjYqMdGVnM4Vb_lsNCxTWjfkZm4UBNWSQiNuLsYodabtadNqcvil3_VCn_qammMC1gqerXyuNrWpbG6eKZjeFxqYC8JUKytFVrwvMypFO9TF-1YzjRvJTJIn8BlyozHUw_ysCslbACEHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29877" target="_blank">📅 16:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29876">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owgrbg0cFAmSdBuYttNyhlKVVWd0I-u9dwLuNij0GsISiUmaH8jQOK6OlHMU7Rrb-t_nNPEmiPUYPxXwZn7OlnQZ10DRGgS0iEJa7Wy7JqLyiBzWsnpU2Bg8FVs09TNDw6YnAguN8VC81DuPK9FA-U-8d16aKclfpAp8ccMqFoKVC324j7qTsbKb65Dl3TZlB3yW8lFY73DReytlgxj4WBoR9rqtNjDssd27Vrv64YewomZ-f001lw3GCm9MVvYRwvI0fN91tmwCxE8m7dn4obJ5eKk0kEWy43xH7zpj2CVXxQ06ozm7sYfLVe6O4kTFLYFF0PCsSKsOerDGtLfydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دوتیم‌آرژانتین و پرتغال به مناسبت خدافطی فوق ستاره آرژانتینی تاریخ از دنیای مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29876" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29875">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky0wlvvfXxy1pEfYdvB10kTWR2QN0EZLZQXrZXa3UDUXxnYviJfh4P76BXcmFNxE1NVtJFA6XIkcxE-8-VkwpUX4ujnE-EZQg8-Pq1lIgj3LvFQ4p9TJZAoFnxc1thUuD4Xt9-pGXOGLPJj4y0uDDCiMVgKyjrwCJaPZvRHjc06XX17gXGqhqqtFalfRO04t1bnIILqO8t56DA-BLo6vtZ-n6tdMd5I0ETigjNxZfmxQqp-4wcPK9-rFDLJxh0UVk7UW-bnBcPNkvKybADY2cfrqLprNZ-WzCLt0HLaoN6e_iFrh5w4AaYL_YDB1wa7IwMMAsLfa0MiU3_XYW5qb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29875" target="_blank">📅 15:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29874">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO4jGbua6eV8GP7MxEGIEKIp8ZCmvJKyuwepzTX8R4BekZm-Xjk81bggqcGap2WIqqmSqIPaoJXYOtNqmk4cKczPsib6oJn9dZZ1R1DIs5bn75Q4Bc1h9IomPlXks47jIlkZ9o4C6qjv5zyf4nT2xmGvhbIHxHlEmfiofiQSOKFCyl4bvYoqhL4AaXqYvJKQQc0HhJlHtxsiSvneGlU1jxJWEa2VAbXKAUOcMAlyMhclv7ulKTmKHrrSmBGGDyDpwO7P9p5ZpRbqRKVvRbI8TFTha2NrU1A2Z1vErdOjZ6D0oWdrJtTLNfmyq90sGQPVqdsHOoIKCPBFKMgq7L1H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29874" target="_blank">📅 15:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29873">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHsgxYSBianWCEP_M-prFpkDetpBPvJUs2BBNDsDdEjkHSeHqAlzgoDJfhOfWWPRUsso0tI4IWZfGhdp8OGWIgfv6KyfLBumR3j6It_jbpHQiwECPsuMfDmlC8mRietZPSBrv6DnFgKwyH5Wzh6shaE-Cwxgegt5W-9HczGdiojVukv1ThccuJRZ1hVIHFJ07TaZpf8FsXxI-itBI8C-ihAnzShvTGXQTXKNLxMYPJc9-iPxXw51zIyUgv33GULHr6S9x0kmC2kCRdZPpXTZgQeCR8SxqSPfPZUV32GXA0soJDv0Q8hW1GxPPt__BX-ZDZcaT6-Jz43QJsq-cU0qMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29873" target="_blank">📅 15:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29872">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flRs-VKEfqmH40Nyhte9LZ7WrSMSeupT3HXS9I7q_1bdjF_pFGDDKDEYrNm-rR9T4pDxFoyOnIIYxnUsx30guDnvZxAru3CCkXpoUWcnEU9cWKkPonHWZqj-dGJgWUQ819fIHvLB5ojLyVqWHe-ye_WmDn6j6JziPBYyY-gtjLxGA-2gRejUcki3gKJSZEp5vX-oGrlEedqkvXMX8snaJRZInR9x-vEBafxGPy5TGLa0k3SBP81tzXJGiN13O8-dUSW78mpE_d9R-Ac3FQsCTHBejko2q08TeegBHPF7m5vln10jubijnoMy1Dq5mpCU88VphqXYDP57l-T8iqac7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته ششم لالیگا؛ شاگردان خوزه مورینیو دردیداری فوق‌العاده سخت و نفسگیر مقابل تیم قعر نشین الچه با نتیجه سه بر دو پیروز شد و سه امتیاز ارزشمند این دیدار خارج از خونه رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29872" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29871">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq1kWI_vjB0p3YRv8SJV8HJs1ad4_cyyNWTjERETplrWczGstwB5a_J8QKhIGnt_GAE4BjMECWDc4L8l40GMKLaQXi_6uFp1Lppp9JwE0zv2ZOEwHccKW9A8unQo4Rqkx0qb2MtkxrYsAFobiCr6V6nNc4JKR3-2zjVr45TaDgSy3Qyi_6rTN_I47ON4BZJ6jf-Rr1jTsaUeqWxVVzi2hS00DoQDHC2vg9S7ej2lcM6Qxh3Sd8VxqXMl5TosoZPMYlB1czKKZ6J_JBDMw1jMRbrY6Gz3hVOh51iU6q8CQt7g6ah2iVqmv-tZSYAcgv0DA9U2eQrn89SCiK-C0tgCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29871" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29870">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29870" target="_blank">📅 13:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29869">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoXLaFD3jGyLd5m1D0WJe988ZQ3-XzpSzuGZfwJBh3rNbiOHY_rRaxycl-Q9gMjXOUR37HY0u2MOQcWhTUr6E7mScuIE1JG-nbF_s7K-kgD5jzcFhXe_wIumjYwV5SrbJxOM_2YSX_5eG-HfIEsByKLYw7SVP3VZSEzhTfOFFLzVNf_Poa6ZqaDWfEx1aBzAxg8yAeiNphksQh3xWwYUudB_fAxTir-y8UVsBs5ILGYIfYuWLQZo9ziUcIB5Gkc0rJk1FJUCZJcP2Czm9wNkw7PGH8JmgoVvY7mUi51p2F5JNgjtw3feafCIMzprrY1I104uJGuBRjahd5Ewcx_sIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
سهراب بختیاری زاده نام دو مربی جدید ایتالیایی و پرتغالی رو به مدیریت تیم استقلال داده تا با یکی از این دو گزینه برای دستیاری او در استقلال به توافق برسند. بختیاری زاده اصرار ویژه‌ای برای جذب دستیار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29869" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29868">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRm8Dl42dBusc6xs7yVj8SkK21Gv_QhBRjBVUt6XyZUTqOmmq-yKkrzs_cbQDUglENNkn8n-ME0qkSQGlTFmEN7eHN37rpPtQzF5hGfdtBlv3yyeZRfo9VjCNyhmhJ1N8XwwoWLbAI_cq-oLA9b654QWEgge0E6i1_Kx9HpPuASq9_INV22uDG8th6fg3XtPEgwO_MaFzPapFwuf7Dma8mhJN-O4kP4atfthRtRrO6HNlttJCSl3LSI6nYh6RkkDkSXEzmr0L6SgvO2O6ufP103pw88eyXSzjLglIhmHyg9YWGQLbLQvdgZK44x5pR_VYD9T6a_dPTdzRnXQ95QBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد حبیب فرعباسی دروازه‌بان استقلال درفصل جدید در تمام مسابقات: 8 مسابقه، 7 کلین شیت، 19 سیو، میانگین نمره 7.9 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29868" target="_blank">📅 13:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29867">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX8mfiNUjrBY46_ln8ITK3l5y4CiR6V1vYsOhLFt8F8_BQIzzenIH5-8XHXQ8iPaDm3dtFKT5lclAwv7tbtvc3OIITLdv2ACMHQ8RWButLmAoWqhcWJE27-MTe2sAU_hCyRdUNY9Q6UhujHE2dWK0GKUqJeqW-WjbvciOGHYjXQTJRezCZ7iHoshh9JZSWkJezXIcHGEkkHGQpS3GjFZWx4cCxqJQ7_BXCVEwfkkxUgZ0lVQsvtpgvdAzEGG2m1pn14rmFTXShteBbnoGalZ6Z4F3-i53D-0TO5nOhKo7pE-Ft2Z4AkXui4C7cjTruPOEBYDu_wqeAGNbPuFXGrSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29867" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29866">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29866" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29863">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THiQ7essGBwDRbFHjTFrXBRQ6WyM4EyMX62c4IyihdANdWiLrV2Cd0hWlSARsivE3quT1909SpmPKppTYs1cevr2mWDi2BDCB-dljEn-yyo022ujXymdt6FA0EqSvagjKxeOnXS-ypyYHbWHTKeglldnftLHCZ32RpWPH5avd1UpxVj_UpcB5vV44-Z8iRQ9XcY49ywEVzNgltOPZiUTHP27fAZHe2jrD2-I_86Qp6qI2EbIThiXIfuPDiUei5THkut0MazvpL5pTPdy_B1_Lip6MGUxKKgwNWpwhdoZPCZVwTUqAm_kJ-mykx5KWvuEhTLLyaBdjqKmB-OlWaNYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراکتوری‌هایی که در پایان فصل قرار دادشون به پایان میرسه:
علیرضا بیرانوند، شجاع خلیل زاده، محمد نادری، کریم آذر، دانیال اسماعیلی فر، صادق محرمی، مهدی شیری، اودیل خامربکوف، تیبور هالیلویچ، مهدی حسینی، مهدی ترابی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29863" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5t6oAzywEFCDsE5-OBMu7CtJ7VXyS-FRjxFPe1Ic3FcmRZidnotItHGfBiMCsZis-r2trLlr0OLrwQipoobFRYG3vpfN3Js8FAYVswzYyuqsHZfmajKnEnx8Hky4G-SKMLitIj_LSq8DuIKp3tybxGEi5Qwhxp_4hTKDCr4y5izu_-C_mq2CbUFu2xiSb4RdwACkWAUziISP5awluDvSkYfikV6CpoFlkw9Gx3vxRXkWlKjFU5CLPwhUJaJak1PpCg-YdBWt0Ye1Kwu39H-e8s8hxNWfIjyrJw6F4INrMsqi4P1rWBVKZiV6f95_oRer_M0_jufJwFoeAHVY4Yk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه:
محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29861" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJPjGIjKOAxmiC9WlLWXtJEKOpjzsb1u2rG-ZSAiJCogwagtPvCnMubSHYwMMC9iQiLjphJtNrs8JmdnwJ_0MGIyd7pkbLDXpDF6PEqKxwlB3vdUf9o1p4_aSd5yaxz1gVNxzRZokZWhaRuiyHaKIeJEqqCnjXS6n5VgLNGxCNuq7gk1qM-JsL5MnFLVgHwXlAVtRlzQmrCsXld-KxzZ_NQkd7yDMHFTiAhQ-0SY6ImpWOLaOSs2zuoJJ9injZDxvJxFDc6DPbxvlwsTNA44nr7xKANbwrVKg5R1fImG9s7ieHVq_xf2pM8iUtBbfABZLUFWyWuW42ixMJq4GiSC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29860" target="_blank">📅 12:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWldIdBKC-c4_cbgqqIVnBkZFVh8gPViMZL7jbxDZhtK1mySdo8tj_97lapDnWzMLG7KCuJjOE4bxVTLEjKAkydcbaTFpZUKUwRto24pAyklWdd8-4er7MblxOF2o0WS_ogapRgaugDjCmpP-9df-qdQLTOxVl3WbPv6AfWJnGDyA7tUlp1F6Q9CU9C4SBmXoReZrt7Ny-VeXtTstT1pHYpY9xUeqMaZTA-oMbCYd4wanUE-QqPL1D9nbiEDhNAd29SQtxlLP15sxlR7sjiSZ76bJij2A2cCsB0F2Z49joCR0tPRciTzyIocjKs-SHl5cL0Xb2qw9SOtcckzv2QzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه:
پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه. بقیه‌فعلاحرفی نزدن باهاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29858" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ula_GVsUMOda3StiP63AJS4rLLPjz-SvkHem9F9mckdgQWhW8JnMnQKuyo61vHUkBPlac-HedmzpUcxmq84BhZMUghXEO9Uf2qPH43rWzh-HqOHjZGhWIitdZxQ2JVP0putgit8FWCX3XzLq2MSjHbm_AlU3Feiyh0LpEAsAHXR1dRWCdpkGAwbWTrN8WCsLPJJ4-eZB8MA4yhYbtjKEJbnvimkJUs_U2hjvQFpchEOLVIZbtQQASf4rObTBRKKjioft-9FoI8b-8f8PL53P4xJUdeniCR_apgYmGiZElQReFXYv3Osh7dOixhDpNQ-MGQBlp3IxwjkTmQQpK5lLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
فابیان روییز ستاره PSG
: اگه توپ طلا رو براساس‌تعدادجام‌درسال و بازی جوانمردانه میدهند خب‌قطعاهیشکی شایسته‌تر از من پیدا نمیشه. تموم جام‌های‌سال2026 روبردم. تو زمین‌هم‌همیشه سعی کردم آدم‌آرومی‌باشم و بابازیکنان‌حریف درگیر نشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29857" target="_blank">📅 11:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
⚫️
آنالیزدقیق‌بازی‌استقلالِ‌سهراب بختیاری زاده مقابل تیم السد قطر در هفته اول لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29856" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDP5-7CCPW07vFXZJ_tET7IuOPVGmTW65LrZUJ0A5vd3XWsxAXlcpJHPZ4HGaXXLfzcq2DB1EaQlsKukYhMnuYdO8rfPs2ea_Fil4wGP5NIDRd3b6njUjua1B7cyI78X0Y_Wpd3jAFi1PKWAwxPoxqtLfms4zQkgpGE2vwtVoDkKXiU8dOrA9BxOzU9WCn_WDkinltZNJYrWvM03iqKsBExeF_gIV6NX9ls9S7hMEGsohOpr0R4hD-Njq93OP1HKspyW-7MDZhQe3jwEap0pu9DRf1p_kuqNLZ_wPgjZtwcKs5yUOyEwM9gm1DFwZdMtUHI9oqmkGurr6vOkugPByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه اتلتیک: به احتمال زیاد جیجی گابریل ستاره 15 ساله منچستریونایتد طی روزهای آینده با عقدقراردادی10ساله به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29855" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4KmUHs5y7fkMz53oiCRHISQyWbhi4jAJTTG2N_oblwqCrGLuQ6pxnfvbrqXvEQ1QqfZVCpneH5-3PaeF1kZATXFVZcgSfgMAbToRDlfW4hxFrBREf2o80-AyBq6iTEsW0XSUEhWTtPtEbvIuVuSNsI3eVw6wdXda1iJTwEj6yK4Q6tjDCgVOzec0IX8g9O91GdMut_P2Z6V1kT8iv8yf85jlLbasGz2GRhrR03EkBzBvn8_Vr1FyGQbYui_ca6tMCF-NPpepDdk9rqHrh9bslfrkCZjyMPS3gy56mhX9bqdjEYWMhGMNNbjdYK20HrbFrS5m2Yv31F-2ZpqxnMdqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4KmUHs5y7fkMz53oiCRHISQyWbhi4jAJTTG2N_oblwqCrGLuQ6pxnfvbrqXvEQ1QqfZVCpneH5-3PaeF1kZATXFVZcgSfgMAbToRDlfW4hxFrBREf2o80-AyBq6iTEsW0XSUEhWTtPtEbvIuVuSNsI3eVw6wdXda1iJTwEj6yK4Q6tjDCgVOzec0IX8g9O91GdMut_P2Z6V1kT8iv8yf85jlLbasGz2GRhrR03EkBzBvn8_Vr1FyGQbYui_ca6tMCF-NPpepDdk9rqHrh9bslfrkCZjyMPS3gy56mhX9bqdjEYWMhGMNNbjdYK20HrbFrS5m2Yv31F-2ZpqxnMdqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌دیدارجذاب امروز صبح دو تیم امید ایران و امید امارات در مسابقات آسیا که با برتری سه بر یک ملی پوشان ایرانی به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29854" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29850">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBdJGP1Wfq1vmsMHEZIYOaDeJmZD2sLOsgUXKLbGGMHEw0RGHG4BWtf3AVDw3K4tTBJQZE4FRx46DWFsdRAsYfdj1AIE6SgawgbMxsdYpytO_lw4LnMgDdQ4oOmZz-W5zg0M4POHp3-VUkH9N8d3wxMHfwWQ9POvWPohWMnSUEFDVmQ8N-yRImIHM4oAUAK8iCTkNy-8i9cAABFnYoV6iifagN7z1GO7yQ9HCv5z1-T0wazRPinUJLMkoWAgFoEsU73ZT3wcLVzAaOkUha7d5Wx-RdbG3e8Fo8QldTaGWCLav1sHWXkaohfeD-JzzOf26zpOcDysJZE3-fbO-pQ1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ از دوئل یونایتدی‌ها با تیم آماده برایتون تا جدال بارساییا با تیم تازه وارد لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29850" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29849">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeoIi57ehT8BpiOSLCOXU3wGISM52GrXYlyCbzFax3WzZ3nEs1lglW6fEm1HA0wJzFNpPIo5oXUt7EyzZqSIcm-qLAXvCeCrru4bzaauxec8Lpq9mKdlw0zDLB6tYkD1zKV3-GOPggmG8lwVibvQ3oEn07VVVKmq1I8UXutyEyx81ryfvqi_J3iRAq3-QM9dvG_c49lq7GPfEEcx72hl3afMJsEJta5kSO1FezQt2sqzeIj-oZY4RyA8twPFkSPtMnqfSn2RSHMnqCjx7KkLm4sUpa_cZP57v7HfTipXp51MIeHPsFpeGXMz_KTbThFZ5x441RWrnJeLl9B57rb3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
رستگاری‌رئالی‌هاباگل اسپی و پیروزی غیرمنتظره العین در جدال با یاران رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29849" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCimgnv-UdOjxeBCN1JCFGQPM7mcMtng3yzhwqGaeTg8RbbrnOqyq4WG1dZPuvtmoVUu1mbF0NovfOETSA5apfLXgbDEnG_BfwB52MK60B91Dql36ebKPcl8PI2RZs7eCK9nuA76rSkWdWYMGEvg9k2XJrFMZ3Eyn7tNIV6kwWbKEfiYdk-WHTmsrNhdJ6CV4uXqc06ZEXctvCUA9HwhGa8R9EK_0SdY7s_bflgKli_Nmz_5Z01RBHM9Rx2QETwnqw5o3qqt-g-12HfFNaes278P2RsJHycIU65gngai9DHhc4OEjTuWjyHJSbhmCQIACd5ZDLLr2aM9vgIkvnVXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ مهدی تارتار سرمربی پرسپولیس امشب موافقت خود را باجذب بشار رسن هافبک عراقی 29 ساله پاختاکور ازبکستان به‌مدیرعامل‌سرخ‌ها اعلام‌کرده. بدین ترتیب پیمان حدادی بزودی مذاکرات رسمی خود را با ستاره سابق پرسپولیس برای بازگشت…</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/29846" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw57bTXuAjElbw1gDPF-xO8GSiS_2_jZ2qgGon4aiRO87oDahMxVp8iOh6UXxxrEsPYlM-tJKAuTajpPPA34B9inkjG-4PK8rRUREMWwzlO2Z1C76F-mGYG-U_uzrz9N9R69A9qqXa3N5_TXwOzJo53ahBFtDQGyPLyiqSVPdTUw0BzgMBLqWBm9PDyMWfOrlmVbivIws-RTGbM-8M9nK28xEjq73EzHjL0aFrBws-P8MnMnkmfZO0F0pSeo6eZ563IhuTlWYW9Da07QI3csCwc88lEYY5IiIIN0wcbwyqmoc241LE6naoNXLFqTyOHmMwpsjz8QDZECjoAQkBhu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس تا اواسط هفته‌آینده پاسخ نهایی خود درخصوص جذب احتمالی بشار رسن هافبک‌ عراقی در نیم‌فصل خواهد داد. پاسخ تارتار مثبت باشد بشار رسن به پرسپولیس بازخواهدگشت و مارکوباکیچ و دنیل‌گرا جدامیشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/29845" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_02RzcWOdTTAeDb1Cx_t-DaeLb1GiuUcP72CyfiyH1a6yPbjK_d3lQW5wY4-LGQyPXe4hS0psZJbNH_16EdcJw9H8CNtnM-TlOOpzdsL4F0ZMQ3SJ0eNUgb8V2CHLolKiGfhsWEtMPrszLZNSP6kgvOJagpUlBCmROMmBttB5mY6HV_sUtYlIAbn_wklHLVbx733VbbZnG2mtQzBfPOVjGQXAilOqPcn0aRyA1z_TcQy8YlkBJoegd54dvfRQjHIUtlQvaBL_iPAbheGEgX0ILmeT5wKMzFclYDG1ffbf8PWA1JCngdOHWS-cVl6G1jtwRy6932MAaf8rc5-wWpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/29844" target="_blank">📅 00:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29842">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0bzNFb4hHk_Ne2VHoUWDqnIuFfxwSmQanyGUWIfEdjd4O8N5Dz-Iwsz5qi2sN-4Lp1zcJusY4jH3uZ9oKwmJKuwsRR5gXV1rNsbP5_L0jSs5KDAhgnoD9QPF5_mLqjlSM1Jo1x7Jw1FPe3NpTFuu6YplgXcvoGne9B0CFI83i-STaBmBV9lK7xT5_Ns2MN0fsH175Iz5ZIVPjvb9lg7-FxBGCcF_T7JNX8sS9F6X0PTA5PR7SGpPRdj-MHnXeWodi88gjTpQXEqxqx5BxXq9oQX7hpmKeIk97rd7rndXMW9JzQftsph-LmMVdFa8EKK0YpGALvrWQCPUorUXDPo_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29842" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtiPtwiiYHXHXyR3dQwhS0MFge7Y5Mpkdxj5IEabvutuB1AGO-JdNt094jSPmKGW1R1DvTWYKrnA2kWPUbuSL0Du8GKOPdeH6vTcHVDFxE-zgZHy9aLJgHSz2a6dm_cRk5ouAK2oVd7w1pAudY3h8o8OgVbv4b-U_NIFm8LVp-eUqPsxwL4S6CybL3hUyKuMRkxIHVw0PShK_ueJWS6aUI9T6EiEzR_pPGk508UF6tJw7hGWucPBNDe8IMBqGhxqrllKq7s1pVrXQ0rlYsO5w_weoBNMcAQ7xAFEeqHEsilCFS_K-iOoxwc_tGMazF5A8RiE7mqmMWjtnd-eX2XAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFugzN09R8OxjO6KhBzejxPm23li2xZE7gmF01SQXe5QlEh4dMm5Od3MbyIhbJQ42p45H152A-kz5H4WvlBtVW7BJVRMbt4uHT32iq2QIKydRQKEwkWBDC_gJH6HY2diZ2sphdlS8lTFjY6-vzOxsYKEQRfCwFVLfStOBhlO008xNwFf7co1Z0OUq_s9QS7S579YHe_I2RP-IlB2hf3To83DZl0WqVbaqCJEyKP9z4xk5-tuieAalzL83helCVYB5NzKCcaCPk1x2eyAUv1iY9_kG035OJshRmHosnUwbV_ftIlqQyinpQhRtHPoRTWYsxnbVdIQpPD1zCF_m8i7dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛
صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29840" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AynDysX-4jWDM03546tzta7liOGkzl8s98-_Pwe6ZZWId00Eznq1la3WSyOYo13-Sv2sJShYhX6xUwhJXbksvesMoPJXvkuM4eXEGMDsMp7TWFgvZcUux_cwYYqaPX-AUQvMxsB4naBomxlyHLuNxOrrcwtJu5VCc_-gJIjOuxhlAVRyOlT3aMWv6bimHg4TPp2sQ9t4t3O3MqZ_7cb0RMTCXTtkp4CvSEomMzq3xN385hBxL4kosgiK7yPGn24QTAf59UjwNgfD7rb3sWIGetguszNdW1HrhlrNropVkTJfQQUUukpnAX_C6xt8ErUdVnv9rUNSlv6gBxtPuCMECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29839" target="_blank">📅 00:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T4mPUBGfyLwOKKRqH8Lp4kjESS-ZvDx5QN-i8K6fYX_pEFajEHswwpOxKDehqqfk8ayEXgCcQ0kaD3W01uN_1xthILrsasRyY8dqlTfQlMYMsyl8I6bcx_6dDf9wsYHTt1USUVr69KSLY-SKU6H_xGqc-dOJf0Sa205D2F6Ix6yAjW0yOgtcoHbdWMM9HZj6OpKp6p3J7EzST0IXiHl538lgjkKqCUOFvIa6InZUWGap1P2DfHe5WOS1T7HQrQq5S7LF4dIg3aKqvV4f96rHnTpM4KezF66QlgUMwYk-3qwh5Z6X4TLA-aWZutodI2hfXMVzmKlgM3nqPG4HTw6Vql4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T4mPUBGfyLwOKKRqH8Lp4kjESS-ZvDx5QN-i8K6fYX_pEFajEHswwpOxKDehqqfk8ayEXgCcQ0kaD3W01uN_1xthILrsasRyY8dqlTfQlMYMsyl8I6bcx_6dDf9wsYHTt1USUVr69KSLY-SKU6H_xGqc-dOJf0Sa205D2F6Ix6yAjW0yOgtcoHbdWMM9HZj6OpKp6p3J7EzST0IXiHl538lgjkKqCUOFvIa6InZUWGap1P2DfHe5WOS1T7HQrQq5S7LF4dIg3aKqvV4f96rHnTpM4KezF66QlgUMwYk-3qwh5Z6X4TLA-aWZutodI2hfXMVzmKlgM3nqPG4HTw6Vql4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه‌برنامه‌اینترنتی شب گذشته لیگ نخبگان؛
محمود فکری کارشناس‌بازی بود. مجریان برنامه 500 بار "حاج محمود" او رو صدا زدند اونم کیف میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29838" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PERwLh1WUi44XNwHExXgkBPpDle_CNFBpqaTRR5cwCgBLegcAosVFdJx4Mgw6iWRCQgeCmMsgFQ5jTyW1lrWe3hJj55TAGsyXw27pymG6VyQwTGjD6eXoY6NQ6OnMwzimONPxzf_g6z5DWiPTugDcOXkd9HIPShyfKTIfy-MjDrIawx4w_gVc39BaM6_F3k2CEOBTSpIgM8yp_JPOFG_p9aOzY07D2DqqeOuTYUMgfg7Jwfr3TucvuKQD6oTPjC5RKnIQ79T985VjboqKwXX4g-An8KD0qPq6ROAW6XNtrtZ5BSLzlFwOYxjd-rHWrhTTU_OXatLU9tl4Pl2HBn_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رونالدو امشب‌توبازی با‌العین اعصاب نداشت، مدافع العین هم خودش رو چسپوند بهش اونم این حرکت رو روش پیاده کرد. 4 تا زدین ولکن دیگه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29837" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h1Ga8w-jZ7IgIXf_nOTwO6GzNjsbYplaTFthX534y3d8hzW8ba416nxOguRmGWjic2c-daVksJlHKiKarpp8YsM8Aad1Y9JGRPRFqSeWyTF884k_dWVvIKfAmxr0SYksMuVvmGMzXjkpmIDZvrMyTu2D0B9sK3-O3Ie_YLaHz1UvVpzdQeXBZMNJxnr5Ctls4YlpuiRNdgaK9rPE1aNcxg6jZBGgqWRpz4zTRrkYCOJ3kWpYXBjTAezbCF9RmI67mn8YwyeqNJoTIATTt8eFwY1aE2eQybGH3xAu53LrODSxMUXIjGZTkT_JAGOu1TWoLxdI7lssa9Z9DeFu-BN8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h1Ga8w-jZ7IgIXf_nOTwO6GzNjsbYplaTFthX534y3d8hzW8ba416nxOguRmGWjic2c-daVksJlHKiKarpp8YsM8Aad1Y9JGRPRFqSeWyTF884k_dWVvIKfAmxr0SYksMuVvmGMzXjkpmIDZvrMyTu2D0B9sK3-O3Ie_YLaHz1UvVpzdQeXBZMNJxnr5Ctls4YlpuiRNdgaK9rPE1aNcxg6jZBGgqWRpz4zTRrkYCOJ3kWpYXBjTAezbCF9RmI67mn8YwyeqNJoTIATTt8eFwY1aE2eQybGH3xAu53LrODSxMUXIjGZTkT_JAGOu1TWoLxdI7lssa9Z9DeFu-BN8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29836" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=v0jVXSZig8iurmL9XOBlcScbaMvrHhQdV2u9oZl-z9YmGhPhQIGyKNthivr62jGLvZ2dNFhwJWHKLagRbANyHRPeff79Qj7QdgfmWBuWx93UXeWRZXGpGc-ogYylkENGF3x4NixIEQaPgmKCtPlVjFU53Z6ONBqhDz4o9DgXaQ52QvwVmMp7x0gyaho34sNtpRZD_fogTN2Kzi03xDOCF4Y2ygLuZQLI2I5pdjJXvYjIgxWhiDI5IRY-zvhD5nHVpbIBHZqydnekGYNMaXajJsmrUjWc3vY5lloe0YX8BXpHF88l5hoHHbQCa6KpYo3IKIDtCCn2iJQpwWyAYJAtNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=v0jVXSZig8iurmL9XOBlcScbaMvrHhQdV2u9oZl-z9YmGhPhQIGyKNthivr62jGLvZ2dNFhwJWHKLagRbANyHRPeff79Qj7QdgfmWBuWx93UXeWRZXGpGc-ogYylkENGF3x4NixIEQaPgmKCtPlVjFU53Z6ONBqhDz4o9DgXaQ52QvwVmMp7x0gyaho34sNtpRZD_fogTN2Kzi03xDOCF4Y2ygLuZQLI2I5pdjJXvYjIgxWhiDI5IRY-zvhD5nHVpbIBHZqydnekGYNMaXajJsmrUjWc3vY5lloe0YX8BXpHF88l5hoHHbQCa6KpYo3IKIDtCCn2iJQpwWyAYJAtNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=oumokif9iBwG5xHVARiR-BqyjHo04YLCDwoeulGQUlYU7mYx8ARbArtOmhuADd4HJxqf9IfzxCtTpexBXWFK7Zukrll750yrzjdkV57q6DDLqSdAUvIqeawec8YPkt4w8v_FjTdXfAh1vB0Smi1D9iD-uyVwUCkYIJSVBIUKN9LpyyQCPgNyVnp1AxY0551xVML9Fy_k3iJ-3X3Dl8RM1yXDHptgk469TGIzQaAOc68yLGuCSD1HjeeewJcHREZxQwTzERYLKB-KxCeNq3e_vhHn2-EW_yWJTNpiTJCZGm4wJLQnRJjkqc7EOzRma6DLHQCDFPH1qS0VGEitFe8zGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=oumokif9iBwG5xHVARiR-BqyjHo04YLCDwoeulGQUlYU7mYx8ARbArtOmhuADd4HJxqf9IfzxCtTpexBXWFK7Zukrll750yrzjdkV57q6DDLqSdAUvIqeawec8YPkt4w8v_FjTdXfAh1vB0Smi1D9iD-uyVwUCkYIJSVBIUKN9LpyyQCPgNyVnp1AxY0551xVML9Fy_k3iJ-3X3Dl8RM1yXDHptgk469TGIzQaAOc68yLGuCSD1HjeeewJcHREZxQwTzERYLKB-KxCeNq3e_vhHn2-EW_yWJTNpiTJCZGm4wJLQnRJjkqc7EOzRma6DLHQCDFPH1qS0VGEitFe8zGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=nKKf4xoBZccUF4AtMqQHgKEacg2JWszt3OOdXliNFM20L01n4XxySMTHpvrlCytVeF7R5VQax9jX5fILNV1r3y-o_R6U30ekeCD3DqdyO8h_DlIwWTjLBQ5CJjHBYNoDCI1RBewfDSebnXt5KAJzGL0UeuoBb2lPfVCgEAnUjNeWpPfH_ScyB568ZlResVIlSaiZBVVGiIwSdbjuzEWUJz6whgBJAPqN-l-udwoHkj95cMk7KGc_D8V4CGhw3AN0X4kqG0ejsSjAiP5kfK3j5d2YwgPGXInfD43bT5WG_zcjiViAMi7G_UGycOfy0rdbKrSxixKXqeP1KZMXxXL64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=nKKf4xoBZccUF4AtMqQHgKEacg2JWszt3OOdXliNFM20L01n4XxySMTHpvrlCytVeF7R5VQax9jX5fILNV1r3y-o_R6U30ekeCD3DqdyO8h_DlIwWTjLBQ5CJjHBYNoDCI1RBewfDSebnXt5KAJzGL0UeuoBb2lPfVCgEAnUjNeWpPfH_ScyB568ZlResVIlSaiZBVVGiIwSdbjuzEWUJz6whgBJAPqN-l-udwoHkj95cMk7KGc_D8V4CGhw3AN0X4kqG0ejsSjAiP5kfK3j5d2YwgPGXInfD43bT5WG_zcjiViAMi7G_UGycOfy0rdbKrSxixKXqeP1KZMXxXL64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccmPyXyT9GUdMm8_BdlCEwtvpHJX7SvceUTZEZL9Vq-8ikg9D-WxYdCev1L4G6Rpd3ifgDVn1n3YaYsQOc1sYT9JkAmVeaP2QnU-Ha2SPQfsu527BZYiPU-xU-PnHqN4Vs7P6gW6Pmp10GBG_bmVuNMJ4bMFa-84Hi9aPJbS9OqO2QrJZNw2aNtV8ztWN3KvvSByd5hS0K67fNPVzeNxe7rZv6eFUelCbQngYGlHYO38Fr0dAqf5Z3KuhPrhuZWPN-V5KTyhUaPHXSpUM7gBGN5tWCfQbkTEHrzWj-2LgtmMQFqiHebC_T3cMA11aUUnRTADM0PYjzlBE5J8Lhu8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAudALPJ_GJ0AnYDd5gjPoIzaWF-LdV8kQ96g5tJYVtZtL8AHJ1lYDONtN6TN8-7izGXv1u20BNVZVSZSDaS7jQIIg3nZmhH55Mu7e2C7eZHVtffx5AKAgxuFoWnITPAR9GaYDiQ7Vc5Q9M6EH6zfX1JjVwPKjvQNg3Fh0Ee1pMG4JCxJxPkbhrlWCizbJmt4RT09a3atXiG8OvtW2Ll9389xImRnFyDJxuI0Qp0lAU9-BXMFlrKe_RprFjVqP7zZyQEELa_nIAsWFeiw5bclkBp6OoxADP_orzBsFBE5J1BOS7vLcuKlyRRIFVyoFyF1bt8CILRLTGB5iTYavAdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKFkkvC56EqRYRGYiVp9GDdahrR6BjoZkH_6QRce1nl6HKUrxnN7sY0te0wkxMW4wobZflRlnFybUkKRbqc--sQrWbmT7pvdjSBq9m634d_Cba9-pLj1yz-_ujjJBKBtWWvffskczMsupPTYV7CKIur_TkBRqWBUp9tylOLWVCH2h08tGp10u3Pq3XVw1qhx-5S7VBUM9rpKHN1zcOZVIoT3GZaWyIChj4w8K2067VqfWSF0QeiJuHWQQvmg9-CRE_X1pOr95uipgkhm943qdORyIxDgmoe3aJYLFxOxxnQbmc7v3A3ieNy-ixLqiEx1X-mjDao9LXtYBl2pdAQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3jsMQ0QdJe5_uR3dB9czoomzvtXxMRTe9Rb5r6NCtia8x1x4yE_NRdf8buUzCc1v_VLjzJyE3LBF9LdSrMWAQ_-B8TeQrdTy037Fe9wbGDk_sqbg0ER2aUImdDQS11fryDt3XoMw9SxaC4RoKY1iUf8KBQTRNMRQmb_ZgWxJQUem0pMytHX2Jvnfk_ou7bWW6EhS_FuoMILJdWVpvNry_bE9CMG2Jgbr6ZrwNFOegwRS9wCR-13xRaCe8e9bAmuS3OFzrugZ8YuJ8iMOfDSPqE7qFy5oWn0ezkLBIN0AaONCY-dwREJ-f-ZDwQudKHPpuS0ienONDlIhtkTOWJ4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=lYG1h8SiFLfm-_NywbhNCU7DR_QXjthyOAA2HB6r05eUHdoUatn-y9IoWtNrrDcWFiG9qbZc8-kOqjwkEis9VJnEn2gjTBPDqFAmkHKc_qvktw_HDU9yTKWiUALjfAPPbGGLYUOzv9CptjlcNB1jJFwIUPeWA0b_xUthkGhe7Tmrjxs6MjQFOS7N2Jm2gpMs98f0pT6Y_GbK77ASd0jU4f8mVPaWQY9lvcoDnAHSGjQAIo4jAaFVuJMJG5ykKjZrfFmKRX-9t-whuHatvPee_GM1cFo7EG5bc99X6JLtKSPjfrESoA0VPOoaiZ_a9ca6eubNrVPpdU94GZG2aw7eUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=lYG1h8SiFLfm-_NywbhNCU7DR_QXjthyOAA2HB6r05eUHdoUatn-y9IoWtNrrDcWFiG9qbZc8-kOqjwkEis9VJnEn2gjTBPDqFAmkHKc_qvktw_HDU9yTKWiUALjfAPPbGGLYUOzv9CptjlcNB1jJFwIUPeWA0b_xUthkGhe7Tmrjxs6MjQFOS7N2Jm2gpMs98f0pT6Y_GbK77ASd0jU4f8mVPaWQY9lvcoDnAHSGjQAIo4jAaFVuJMJG5ykKjZrfFmKRX-9t-whuHatvPee_GM1cFo7EG5bc99X6JLtKSPjfrESoA0VPOoaiZ_a9ca6eubNrVPpdU94GZG2aw7eUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_-0oGmzViLi3gbUQxSkX7AV1HYj9pq9vBF7tz79eZG1QKyZS8jl-sl34mMHs1jHfhqojICoc5TeYYZE_rbpQppy9dH6reCv9qHGQXQoW6C_brZ3GMvH6rUXGzQeOEXH4nZCulYfxQM-QURU3pVZbADjgmgL0QeO13geFDgCrlOdFgacn2169Q7bh1kdZUxiMMd6eZTLcJHQ_cUkWj_PtHrjEl3tWMdhovFQeUdhLoR-TGUrVoumaniEqkWaGzmq6efU0OCJ5GqxTj2u_KpgJOoZgx41f94ovyJjz3rUWA_ia5EZ6Q_OasQSH7XnZZTU3P11xb7uvD3nMSwh4gUlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljyns3vEPc5rm9z52vxWCS99OHgGbXVROFJGRQYtIziDS3Yq7fxl4e0BvFIkWYTpFC0uuAhv34VAElWI_JAxYZxn6kmZvlAAIj4PaUUnGhuhggsyb4ObeVopBaEqDWWAK22BZ88GLJUjfbC9BpmEtYhpL469q5a3WXbwms34Ops-40dm2ab10uztGEMiPdTuc4ie3bEiI2DyX3noIXSVts21GRDnvlyHItyqNLbN1y2jzIFCNem4tEEbSWU7AREb7mEvu5z3mjAbACEjV0H5QKc5tdGjyns7fRJzrzDUqa3-Bp4dPt1HG0yz_oc7VnYMtw1aRKOEv5CPNKPwjTm6wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=LY_InklHcvXjD6cy8-28QETNDSLFsAvsLVDxt7XrFKAq-fkXOm_Y5QXdlNrX44Tv90PMIIHnIhm1oRLaKcvAhG82gy-3nXfFctrWsc4x-hkvxmTUqpN4NIvTfPiXnecOpXWbO1SlZIEhNX2SMmntpbw9cRt_b8FizELj0KvXl9ZB-rzUFRh-erS6rHHvlhqjSS5jRN9XZFSsngPSozjopizmAvjAaq_3tpkUJBUKlQkllLlQXjTvVfdpAWtUlUv0f6ZS1ryhfPeJrn2ApISDJXeHwgcpPdnofUpfE4eUszrJDLEHdyronh1Fo43rNAAFxj176IjYg1KbtCgDVMye2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=LY_InklHcvXjD6cy8-28QETNDSLFsAvsLVDxt7XrFKAq-fkXOm_Y5QXdlNrX44Tv90PMIIHnIhm1oRLaKcvAhG82gy-3nXfFctrWsc4x-hkvxmTUqpN4NIvTfPiXnecOpXWbO1SlZIEhNX2SMmntpbw9cRt_b8FizELj0KvXl9ZB-rzUFRh-erS6rHHvlhqjSS5jRN9XZFSsngPSozjopizmAvjAaq_3tpkUJBUKlQkllLlQXjTvVfdpAWtUlUv0f6ZS1ryhfPeJrn2ApISDJXeHwgcpPdnofUpfE4eUszrJDLEHdyronh1Fo43rNAAFxj176IjYg1KbtCgDVMye2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOrVZN7msRN7X6MB_DzDsq9E4LHC_qJTxet0SJ6fyz5DIyMeNvM8DSPacrl7qs7pK0UVS2il10SJviMZWUIFr7drfeOBhtPEK2KeiOomPgvKwq9uG376swzuMcDyWRA9-T_knY_Op7VCc_50MNT4iLlkIMHKIK-gYNKFCEd5P7snyiB2Syso9vck0xzw7LaNGOXYb1Pk6nERZcqTrk1U557g3H1V3C84kqaQu6qUwircVi7MMGFdhl1-W3OeeJqeQGTgsPxvmR3NjLq9ISgHM2gomgY2vfBFvK-UNIswSRu9nqqgZ-QVU9Sx7v9W_wiwTwVGaZ5eKFyrivDTHIdkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWCkYCZUxtnlQDrKfe6VuktgmykdP1adEbqBz4QxI85JaDoIgjUqst-6wX6I9UwJqSTWN6bO6cLRS_afkfb26XVS33gaxUUuxXKRpRSDNnuacoJNmt06T1lA-xEGF9ZGowyRwscq434HxuWW89XzKkjPh5M-5jyNIT_DOg_gd67-QE74QJ0pGXKOBWPNvw_D7CmFzeXUTvz3YMio3fuppSl41sXBV9-OzQ7qLr4Ma7GDlqA2SirM9uIL3UF5rBtzrz_M8lSP2azJIoZnKtML_r7W6Dyh8l6RJebhnOqE9m8O4g7OpAURi_GrbZm7DxtkYAJQ-cYy3Bx9lME2gUysDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYjqm0VECCFv-wJfAQq61URf18fV1U86qMmF28Rb17H0nrQmGjgYRUho0C7-IaHcyjeMupMqapyWKOYcrSw_wCn_4tpBgiHahIbVX82yvgbn0wgWpjarYKAhAKqq8p-2hHihTnZ02_dI7fUSuM9x2jWU8oFSzIbyHDI1cULfEVjQBX8-Jbik_RLN1as0vkflbt56w5IJqS_GYprlaL5UPylwH167uz7QRxekXPDkGsmw302qEaUgRj3uypW9TldDOmI70nQ5OwBeQt3bO1rLMblOypZUHRWx3LuHuYm9oeGdNxMz9E7yhlnpcDv02Dbu9Pwytz_wEcQ38CtPktF6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDFqTfPxVc42J73htnJgniyDK0Dr3Vysi-C1spGiv2unfNqXPunAyKhw-OiCe8fOW6z0L5J7NWEqEtAovcj3Fz6IbpTD6XS9-25b6l0WVG_bF4fUub9XYmDaW1POM9Tx1gsIonnGQwsfBsDYExTyJf9HyMGjiaNs1zgDclJMshS4iSFhBKeb45BXSenTH0UaFIzilbg-eKpNX2KQnHSDSTyiOqnxQErxhDTprOqArRuel9vbsDQoOquzCrcQecJRC-XPXHamkmttBuim6SCj-Z2My8NZONOm-3PpRv-pepyl-eYwRKGGebuGD9W1txZQ111ZmnbhSprfjuHpKaG92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYNZ39EKiVrj7XkG_b521VhrOG_TqNKrHise_1veXNdOYO9y3QnOmnjZFsBJenSWWhbYaiEZdmrUznyIotYS35IwgWWrN5r1cfgAcB4gT-m_83uUZnjfa5a9gbQcHa5QSRkYlCQBFXBHDbaK5gIBvkA03VnAnBjtrScqTOn9yLSkkiqeE5fpRjWa7hZH6PyyCCtbGXksA8JH4j_QVUJ0q_uYIVuQGAPZFMdPksBNc-Jt9HnMyxLCegDHhp5QMePeWwJ-pUJIQZCRfMZoKLhirp_inl33Bwh46fNY6DmLRCaJYwWRUP7KB7fEja6ihiC8X8szXUbE0ieu1pWmOEfZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiDS4k2hgPOSBdQ8YrlsICmpCwjgV4IoIG9fWxa4NQCXKe_bsSuJs6XfvoqDzB_KGvZ6zzm5Ro_jTPUshNRGYDSIeiUBn3KBEgkQg4dxTyi4n8chgUj8u-L1FrBGVIDErnEf6OzNO0wu9QA9dh1z240CnkgHSQ9KEgQ9d9HXmd5sF1BkQvHjbLx_JDry27bqRN7_mP8TxhkyVFKqudyJQckWsJ-Ha-IwjYwenXyQSETADqAgo0HvjCqaPoXrPkkQnrssCMVZ9y6NHr8lYVIvKjYmpzAtDtqW4ORpha-Eofa9V1wvGvOxwH-LkVi9gf2IP2pqtmfOrKVXgzvwT_GZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_4YzYujBLhE7kN_b-4HvDz3xRpfaGGhqCZG1cNnFJfV4flotsPtV0V92qzxFoTh9ViI9TuKn_ikSAU__aFPRpWNvPjTl2_ot7hbdMbvAUeVbcnkUHIdIpJNgPgSNsUxr-dlkQWOiqcUT1_JrNC6iJ6B4rtypWw27M05Ao37JMcmzNNAvKrdBlQmiT5jc1kt28KiegZzlH0Hbk9cf7afjSyFScILen2R6zBAeUY66lt36QVE9gG_kbGEolFu1vr3Z32avyK31QnqT_D_7zwZtQweKSRhJ5VvDnAf1mTL5aIf9W1qosdULnXkB6TVjc60Vq0oupjzrXG5bhoOTkWFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v60lL-sl-7LTYNWKZ6dMlt5WD-zIJXmqezqNX0X_HNDIDtFFWZl_dW6WaIYhmIYY2b14-89AwRdPaZzRx8bO6n5uIDDyuN8LrQvTrNEN7rL87Mxye7sQi7iDO0dW6hlYlmbVaL8mDsu9lZEDQ7Xz80DX7tsIR-pzwn7Er2mPWmJD0MEQwBAc9-uVm7ReoNqT8jvaw6XDoOpC3LSkTL-xTZGI72Bhjbewx_Ca59oJVskqwEHNL4mH7H817Lj8NWvcsevLw5kED-Uz20hCUV5r_Olr7ilYvVW-qwftG6ej3GnXgj8sQ3XXKOoN_mvQDS7CQwWVm7ACe26dML3R2cKxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVpFfJY_b3owcnJOg8UWXGb1zYTHMWzqD4qSFg26u2rkjjcJoVnDodsgmx9KL2Zfx9tPmotN2WGnOuCHCuY3zZhLDhmx-E1nqZRIDfhBfyASbzW-n1bpZFHyWnoHJy7hjt1QePBt3vKbfvhe6Da143dQx6AC0RBWLaISJisxfDcMV-B2jiU3gh0eaadd0GsjJKRAmdJQzm9iicStKnqWpCg9NSQli-5hvZUGZhssHJi5BndFQFZcpdGndAV4aJVRYVivwXYXLdLeDhgub92u4QcQ5EjNMI5AWZwJaSaqxeBNV_s73wb16_ZlIYHtHmIzaRRLIy-KKzQfmuSyvaInpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzECsdVAZQmko50Pox0kjWfrcZo9lzKh3I94SabHtcowDa7u11pVdUKjX3e9caRhP1mS7SFyYYnpvdyyHXbV57z3K0UpLlhlu5fscfvrnhYiVhDzraJG3tkl6OtZ7VWJ-aeWBXEWtpU1KEU91-Hy5-L1P07WXAOqu0qZuZO25jnrvF2AfiMxy37_ZNVWmJ-TLgt2VIVrnRx8EWoYmRAMGPjBABY-EfVPsTEHaGHrkzthIVB-IwIYC3CElYfiJMOIfU9DrDa6JQNMSN0oK0-43LFW1nPah5EXhhWjTv7Pu2Qd5LoVl-3VrgQJBVWw8swTxhWn9Ge-nHfG12BjA8nLOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci5whgGnOT58cnWzM6VXDjAzSI54S9ghh14kKSxz9AdvBjMK5gExHKpOTVDJ0ZAXeyfOlvHTBY_yjs-_g_CFyzVV5bfQSuhiu-eLq1ZAzQHNc3FBrwa2ElWu8Upfk4EceoQxpUT89p8mrS0Gh7TtSB2tU5VLpDroKmFla3hUd_XhPk_IW5npzRuXcSxec0nvsO9B1v0yrVJph8Y_gSw6nQBbLbAg6ALFR9jTUVnP0aBTzlfHQtV8DmG_kBQ_JgqUf97OlX1rT2UzfMki5YeNN3gQoOCLjS_PPtVkf6SgkAQBlL5A2FN_ISjRPV0pUjzCsFf7gYNCNqhHsqX_XjKLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVk5qvYdoJDHgoBDumSPEPoDuXaKutgIybLlxLNDP4qTtSCo2-Yv5Bfb5JQr7a5903aRBUmeu2aHuHVDJqyml6uap_JPMareX6R8ZBydE6o1T3Yzpt8M8wWmUJzjTGSfcp41_D9INEwlVjR0A94VqwhFHxCyH2vayDb6hcbL9_5D0DoQGj4MyGcLQpgGYPhkIBGdJXFhYPk3LohtQjFDsBv111A7C5s_XGauKqpzYrRdyfh0gQ6nNSy-3EGoCLWmZhuFdbgVg5BNCXIB4kt7W8iS8pk5aI6Oy44LVWnyXZj2DG6zmAOwFp3q-Ey4cxTIorZDNfXZotLKxL3XmL0Dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ3OKRoNN4XPFv3vUyjMLh-pzMVUMeEEw532v3WH6PDOMty_J_Ko6rhhA4qs0wyPDPVR-BS0UXqaRbz_KXT6_ef-d5iIHkm8bPV-RAH6xf8DWJVSKdBrHqGgyebH8wJfu0UPJ04WNMSkHrEM2mnCtoANcr3gDET67ObHLFp5gzNAkAvWwtL95BBb_OK1n5v8eyYOa357Pu64n5xyIqmR5jgWNEmCzEWMHSDlruSxHotSjftTGWdKQHPr6H_5_TbWhQnvcBCN3pspP2w1CZFX0JEx_NqWKOxuzb_I3Cyxfn7qA-OeQ5W8twrZ6h3nyMTYzwmiooHoSsyPFlS2be9KhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKwirteeKg1050L4rUAqDwBx1EN87LB8ly1LgXiuEo_h7uS9NyMh6hQWu0o4NoBJNz8zFkzHeXLdilfA4998XvSVIzPb7N1i7KhxafBfRdlcdHXjKr5sNUrIlqFmRwXB5lKE-GdrZVDsbGF0YlmQdYJW7M5UOUUM2OImBseWQq41N4_jFv0CH2c4hn2HCOY5HJTwiKu3rIo32z58uQaXCq6vrOdqPcWmtY9Lw3-i95gxQbbdIRMocepWsCKGEX-XqYQ3_WcuilvRUbLQEDcOd6VqxE3qS2zhV_XhBLaPgwTAb3STOiNI4Xn0niolBYt09u3OMo1YmQH1FaxOA4Obxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEpcu6FwSxlR4qMMaXN6w-sz3fxUm-UwYfrCgCJrRjuZfqK9Vqr7Uxx1bfHjl8MzE5ietgaC3rCLAzlCHU7xelbVtgg23D6nDp6ukc1QC7IHCAciYkIj-zqmEp4wJ5Zd_NPoQppWqAVMgAnwr4JolwmBemLjUquXlt2e-Sptcno4uYexg5MN8qDhTrUi-SyT0t9KDSgpnaKQ92-N8cfeMIixKOAEaSWegy7LWYHGbHhQlBmQS-gmiQnfRQtBsGXOWgEKsyYiWeUdpRmN7Ek6IFBGvQBua3wVfPJ9JsTAwN9_x5bYxamaHdJFhQauS-5D586KTh_S66WxSnltqpZ2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0-r0yx_9l9b9VNNTTXPSRTMO-Oje7Lp3jJfT5kPmDScSj0rO41in7iaPfRhqruhEWuAKfRCl3rYWlORlX5RLhDY6M5j9b9necYSdjSoHnogTxXXSYDkbnjTSqUq70C4aC1Os7_T4HBGKFO_K7Xc4lpgNzYoHbCGvcPYIOFy77aQdCA8zjDavzsNm8sHsYM4490gvnEYMqxkDUkfEx9wxMSCY_NjYH6yhqFZ-zGBEz-MyDXgjpeYUALK_L0tP-prh3FYQ-sc0FBguC9jRBV_whlGiqsFsIoFZ54PmAjspty8jRRWHnh1obD28fkPESvTSXKanCz8pSxun_n6o8pFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubnAgjho5NeKS5G7Klcc6NUHmT9jPTk8HOpbhsYgXiKzipFTIMzTjAiAZFjjbkuNcjP2f3AwMMYyMJ8sfFKsFy9hvD7fgxUkvQsZNHQApRsr3hXMXwckb2py8z0jMNuaeLdIKU203dn0Jy352U8x-WIQn5c7EveDZ0Ha2H2W_fBqQZxwaRE2v2N-wQWXtFMFBMjW7VPY-NiC5wKmz15perIxAYuk7Ige__yOgf1x-j-BGd2WxUu6WZGR7fZohu6078qZRoGahOmLZ93nBJxvQP4pAuCBNWzaUyIUSMsERHpr9M4QNA1X3T4_814N4_U3F89jbhOznj21Li_clZMERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q54EZseCrEfR06YhTb2sPESj4usaYlUt4im6BBsYSKLiEPnbLZkLXnfQrpMNtjor1HnO2bwO4dEzpuoSi_8FB4bL-OpeJgqIBRfWfFrtRR8d2MzbHZB1XTOg9tBjuL6uLCyarOCrc4bNgFdaDUggncqYDvSxYk7K3PIf-C1j-54bdwLt8AMNyPxCCi84NUeFBrpUvj5chVZufzYbIhBotCUcC1Q_2hX7GALc6qR-Athi8RQSsNpkJ9UEPH50sAF5Qb9pBJPqzn2a1YaSiHk5KZcVn2LbquEsF_-pBa6GMXWL40e7DmqokPQMnQdgkVI8NXU7zsfGutDwcGEVXF3w5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkDmOPa40ujZgjyRFfrV033Z8p0gH5exdmOV4x5TQ8VjN04aMvaI__dA_TxV1kXw3lXqIuOXQr7WYw9rXUCrshMeExXzTtHoF6wRnmQiNv6tNv886qMq4KEMiAlD1owZd-FczPh3pHXBFPNpp4PgONtiJcmTTvPJiBNPcuLfLCmOObIDnJ-6pakDXON_zQSh-KkmKsWTMlY2V0zvWN4AehM8QdR2gJtWv93VBR_-jZtZZKLp4iURHrwKp-1qPfihM53uz6CiLZIUzUvwzd3KXGM9gsEZ7dE215iiVy1rhTGkB67yeMolz2z1hn6co9yAMD-SGw3Po_WouiXqMAPZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywk5RkX-9QH7PFsFi3xVoo2ySP_MFGqozvlXihBCuZP0llE67bRYKZJlgeyds8c-yv_gA0biAbtnmaLXCHE0BrymfG7ADrroduNnQwfNqpFE2h0nEuuCwdvFQbDQe8Qcdi6NKDF5PjRrCpPvWovQkXSKb31C31olLhvRBk7soUG03co08wT5Mvcxyi278OrTJ2_9vTYbVKw4Y_GW9skW8UmUPWu7uBiaDLclhKZ2JkQHsn3KUe08XrP0DGJenVM_GXhi3oMOSQUJzZxRGDbzV8TJA7GSSt45ibCt6f4zIS0DVR2t1sriKTnnoIy-74vGzCZnHuCxnNWpMYE9qcVfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNTZaCYrJcqseGYOTss8N1LcrnvZ9R0C5523cFk7EmS7X271gw7IJ56-IIoUT7V06h3p8oj_1eueye_ITkbYQNaFpDzMpHowqJwNkLQBbuNdQ2DMHyyTuJTbFXY1gfaXttTYoLGac73-w_Dv05q6vY4urzMyjcsm_HojyYgdBmTI0sUV9lQ48H4_7XFPSLPMuJUsG_UfRTDJlqj4lbKBnRX-8Jv0WBI8xntB-T4Y_oeRkDyg9mnf_ifwknc3omiVdhmjAGmBeCVUDVUai8fMesJm_2Ax7zEK0Nh17zdaBgva1WrfMI4rx2zELV8Pi082IzweXxJwkLJanQ1_MlEQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kep1I9SpYYF2qjT0x4Znw41uwcNvs60W9e3aCp6E_LrjdKGsMwqWGsvcxgcrHVTlqlCTIgVhes6I9pxPk3vtDZefeqqVfFUbuClZFD77pWR2NzdXGHDHdXr0zWDTjecSvAcmCbJLuRVtUhuUdDM1HyOu3WMEUJjuJyogpuH5uempg7o3_rThR0bjQ-j4bNvBSxBSPpaZFXIE1WS9o28hDTtb5pBiPVc_6V15MTU4OeNx4Q3m2tm7h1QGB68HSb_Oc9Rn2RiNvHhH63B8v7Yy_w09YKxPrUTihRhuUpkSGseObVzTVkkrvIfdbmoRCbQ2248TfTqQl3R1HLfN73L6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMpPMvR2ggceazemeXAQClkvzCGvetvQhzuGgBJrrIGBt5Vgo2Zn5hsxNqd0Wgxe0P6iFYNrnsSyZ6o7vDhpAaujoLFcqn6XEaIlS9vbejE7qXZImvWnfVE5qQpg_9lWvzc3kAwP8w4mY5O_nq-3Dzo7a_hLxDDVmucrBpepoIX4XDUZ64_DV4ISJQQGQrfOG20HYLVB4N3qyRNDNo08UlVrk4Bd0XQ5CHX6VAgSAPQb51CK8SGAliwA64H_P7KbQAz5iVTD95WLrtdkxhKtsTXwVwI8VZWvpcv5RKHmVggPF0Uw97T27mbZmYyoRlUNDMso9IqTq7N3ETa7NJfcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdUQkXA-gyLkMFm8Lvzs6uKkldOgrW1uBl6EwnnUOIk3kNXzPCG6RRMqJ1BvTjf2w9N1FTNSjk5JyDMOtNczfNGjY2ynobiZsCF3M6ZhwNym4Na8UCvXI2BcpmoB9i4UtPOGd8MqicLMJIzTlWPgFfCuIaZugNj033nu5eqAxphNIiVf_F7lG39-egTMq58ijbmPoT8BKtTUDQmdtP0MkyLHp80M5imY1nxezytYmBgPhRRYFOmDW2js75Px3UIwFpLqGq-ir0cLvm4QMzw_vuBZ1e612sB7aFhZScrNCwfAkzvz99FhUpZSUlsfbT1n-Af5IRiwvv357hm5H6dJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW7XLEH58j5Kr40kyDslwSI1jkbrNaGETE0LU8YKWxIBqwVb0cpvOr7zPOb0p2rfSuK1V2stkWDbzgvx0aS_3RMEBi7KI8tqeAhdXioDBRdG3pj3_8kKyv61nStdeVE0YRQnWjVJvod0Ftbpx_m5JV4JSFTr98pJK8DQyReRFhJZyl3IwfKyVi-BHUz-zTf1m3nzbM5pfIwY02ud8c64UzNE2UZXo6UAAHyYJx_suDuFBSkZ_oa8oyeurXeafjQA968k52DvNMKF1IY7ju2BfC32FIZlwGuFmDCF0R7PmEq_HaN1qeps-P1vnznIB-7IlYBCObYYxTT6gOpzYWxa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLdUmx9VmPSJtRJeh4az2TB8CVRKfhLWlFvAW5fPBkO4rWynBknxqiz2ae1v2zHEXBphCDCs2Q4hN1-pBLGQOSNqGbPOp41NWoziEGA6o9ZWRkb-6v2fK97qIekgf_Qmz7A4FLoYRbMmPw4sZjVm7KKnx-XG27M6-K9hL4gSKE9lD2bG3-v0v1xjjWoC_NzAbAqpL7fa_CT6GgAOoSrCzDhSCU8iCumzNNDIH9jJVpsuISzc3jIYf9aS8XVErdM_ETx0yOv6P2KgqoL1biZWDRPnSO6QGw3wNQKGZ60b9shX2XH9dgpfuSUZpU6B1hsRZNNkG19Q2H22HZXb3CK5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-O8QoKDYb-T51ShU8kUpdMXDcnxWnoJkAZICkjWh2xev5CVDEHZpaEYCEo8ID5sXif-xzV5AfNmgD7YtRIGZn4G9l1rkm_E3gv4RZQhehudsVXzlbTzzzw01DMFCUCetJF0IaPV0AXoRJxT3x2W4o4HFH1zRoNi2KiptbU2QoEJbVn0cGTJZouATi6fs835-mXtZGL0ZuI6qs19FKpGmbbdeIQUb9lYyZzmKu2TfiLcVL9PYLS9jNsO7Prhe8TQsCqQacZOsuuRMCzYwjAYbmpVXCZf_c4XpyVOLzjplIHGeAt6coRRvZy-_J0CU5_9PnYbhGhS1yqpZYbQxMC-fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9wonpOfa6t1Crb4n9S4_i2jxmVebZBEe41o8NF-w6S3nNH8Uti1bv7QOmrxuSIAfh1kxWD7ZztsyAlFJIjAEtHJkMSebLiUfcfvHbAZYLt6NywF5ZMWm2pYWDK8GAnN3qhbrFxgi7KProWyqJqnQi5odIyoQ-CpCwBtietStyDSzFJakXJhp1sDV-bsgEspKSR2vraB2H-aGyjX3WKvbuRwq8zB_Jpbjt0naKp04HKxlGW3NbnKw7jnVwXru6pTKnDNu47ukPKtmRkY7iA6fbkmRnYhPV2I3GIBmB9v-O-hrOc4s147cqNfrRm-_qXNcUSw4SxFZFfryOUDLJYUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISieIb7J9T1pCIyG-66sDB5piCx6h-nJ1I5SREW_OGqOVQlrcTn0PPhpwgfB1dESeWw9HJQx-yefYFZudPiNWU9jWBVu5IydV-zHmDhrwpsndr5F8NnLGqaj66BKfqJbWHA-zMZvVXQUYHCf4x7julpb98S5j1H_KhfBpGn3NRX_vZsfYOEwGPBDUzWHfpxbGfTWzo2VN10EyGwCpmfotMuiWbt-i5V3w9yYvOUd_9PmJ9RmXqqWWVyO09yDj1TRSTOSiENctoOxADWQqy0QEtlAmUhiyRa7IhXD29vxSesvS2IBZo_RjYuiPLURyeHZRaY2FBW6aDwQstSjmvdFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMIjojzJDkHbcP3zreL0HSq2tA_8QEeFKMshtXNss4w3fHFeCDorXGbwb8YzyVry_PZB3yAkjW9NeRoTrtfOmNAxdH8VRlchjwh3uGTAxfYBDEb-7BqRsPvUf_ylYsrBOXHhW9PFuSBM2d3_YbsKOnIKDQwRlfEQxYXtZoLtn7fvPYW1KqYnZo8FHPjeij3vE6hrnfQ1PEYAc9oiVXyagBYFHVW84JOrQm9meUYLPBDiZgrM7_AX6LYXNLXPg5oqiiua8Snrp4e-tcgbY6ouEGF8uILotG-BHt14oH9Di6AR2yQM_Kk_LIYbtf_exn_hHZA9TeugMD0BiBCBewJdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDzXj44WBleuz_sXQPDRZ0i6ju8zZEtjLuwBEdXgfc3zXO_N2PJyOpcrjYUTj-xC6yM-N9uq1eGWjLxmWFcTvltjJJLMd2mNgNw_j3pa9QdV6iagYGaMKr518qjKN5EshztsfYDc0wMNkGn7tohCgFVYJOSanKQsEDwF7xmrAaGraDMMX9v-1noo_wis7ABR--XEbd64fj3DeSYKn7ojERIglLsTlYloP3zARi8V_AaxuPiw1sc_9EEOzHFcGaRiQzGXuHtAcFyDNadJRU-Blf45kPxhL-w0O56dBwUfZl2FCEMSbG6yzo32f7fXd4nouDEv559oE0LzujiWVX-brQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9eMhRjA9Ezjgrolsf9az__gKgrTWX30IF5AXlEWktr558bVc6OtyfImtjA3k97haiO2pUk4GC7J-qf6JjSEc5eu3GQaGT-TEWfWv82gjX8C-35M0OhoV7RF1dWeOcKrvfXiUBZCOgaiEpA7sZgphRIZqxLnLetlXFfdq7itX5J5Ouni363VUeDbI42mMGBgmgqb04bqXLMbBIGFoPpZR2FlkICQxKig7v4icks1WUbrCqB_L8I_PmCpcAsH6FEaOXYRDPNrvIT4YzolorOlkDyWkdpM-HkeurhH3_KxbkXn_cZNA9IIdilSmi0s6IVllXZZOwX0kxC6pq_P8EgV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Mim6cQejOkRWbOtoXBHXFK9cmqW55xZW0oHDroOX01G12yw-XKH17IQHFZiyujE0kbQK0nz0rqGRD4ROowN0RlZO0flT6_abMASNAYndE6zO8jcf0UAWaPYJ6MDvPHjBKOewJ4Xe7avuJBY7Pm8DHU9rSJxMIblxgEiGMmsjfHCykx23LU2rgG0nVFZzUNPh__NzGSfuwRE0v-4oJJOmOEBsSO25jajy72OhW26U0NYWkHC-ySx5Aw-zTVJrTg7roE9_o5Qvr6pcUjGL3v5LVxxkMpXCeKbR_o6cQWXw8d0LnvArwqCWnlHD2dP1BI0zNmhvmBH-lFHZbtQg1z-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
