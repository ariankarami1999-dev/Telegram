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
<img src="https://cdn4.telesco.pe/file/lZuoBlfAi2vicrpRTgTukgYGZWN1UyDdqGYZ1xkX7d5h5mdmTkA_fpeCI_J01zEMk-EshWclVeeB5RK-Xmleaf_izgLoC7wEMKLEvB_FLPjvh07UpFtkMECYn0MssdmLZ23Ag7wCNc5LtHBNxlOBNK-kw9HBiQedxwiqnJaxylMsAXx0mKBjLkTu8SnbYh2nWZjpn3sIwoWFFz0MeN5iOSbpLNjpBGO9_54AkQHY6NIF3emsu0fiBgKVqpxWsDF50X3h3lJ7npEGMLem74yNco8Nu_-WC4J4YSWKrMMD80QMP-DvvbwHr7GZkHHvABNngl20FC3rWEwpp4Mtlax_iA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-684883">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
عاقبت تلخ کشتی متخلف کویتی در هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس تأیید کرد نفتکش «السلام ۲» متعلق به کویت، شامگاه پریشب در ساعت ۲۱:۵۰ به وقت جهانی مورد اصابت قرار گرفته است.
🔹
پیش از این، عصر همان روز نفتکش یونانی «مترو ونیزی» هدف حمله قرار گرفته بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/akhbarefori/684883" target="_blank">📅 04:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684882">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e148badf2.mp4?token=YSaZvLQwQ9aD2kRDeI454Z9ND7KP89WRFHxLxTf8br_Q3p11dwE3vv_Ch7xXMNbnXxYqFdkO-dELephFJD4u9zARmK3TVC0-CZfbWm03-4kJE34F8hy-ogkaJsc1kc-hhYPCTllBKh6vU_FilBVfMDjY_zd_woW7Zs6CKnJtqI7WZ7lgCzAHXmho6d8Wgg8W9WRNFeVXLGlsGlJZPGvxBuTs5-9aI7lI2XaIuc2XQNPSHTEUsoEy8Fkc_OJXCC6PYuBZLjGOMu-fC2F9r0FoIvqvp0wChwrqlXe0Nwik7c-7lOKhcrTEpdrFoP14uG6LllMWkBpkOugh4PJlXaESjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e148badf2.mp4?token=YSaZvLQwQ9aD2kRDeI454Z9ND7KP89WRFHxLxTf8br_Q3p11dwE3vv_Ch7xXMNbnXxYqFdkO-dELephFJD4u9zARmK3TVC0-CZfbWm03-4kJE34F8hy-ogkaJsc1kc-hhYPCTllBKh6vU_FilBVfMDjY_zd_woW7Zs6CKnJtqI7WZ7lgCzAHXmho6d8Wgg8W9WRNFeVXLGlsGlJZPGvxBuTs5-9aI7lI2XaIuc2XQNPSHTEUsoEy8Fkc_OJXCC6PYuBZLjGOMu-fC2F9r0FoIvqvp0wChwrqlXe0Nwik7c-7lOKhcrTEpdrFoP14uG6LllMWkBpkOugh4PJlXaESjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هولدر موبایل YB20-3 | نگهدارنده چندکاره
📱
✅
چرخش ۳۶۰ درجه و استفاده افقی و عمودی
✅
نصب روی داشبورد، آینه، آفتابگیر و میز
✅
گیره‌های محکم + پایه ضدلغزش و پد محافظ
🟢
قیمت تخفیفی: ۵۹۸ هزار تومان
🎁
ضمانت تعویض ۳ روزه
🛒
خرید تلفنی
👇
https://memarket24.ir/product/fast/31853/180124
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684882" target="_blank">📅 01:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684881">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klhhx_dreUrHpCioZvb26Dma-2tcishf4Sg4MwBUmxFO5r5rkNx4FNWO3v4MkogEVZ9mNg6CUeSYJcVZg1ioi6WI7cNbr16lmg2ckRkodRyk9LoPTEN9PqcwoAlE8yiZHcJgEviGsQ9uE4TD5-uSi-2QEc2xeO2X2aFpzqlPB9Z7V-qRB69s-BXJMakSaLOzIAFsd6VlXVbVjN9UHX_9En5Tqs4D9R4LLepLBrJuJQb561X1YH8y6Iyulgk4oAyuoIjyBhtjbiwkefi6-LmNG06cLXU9tll-cXOYeBiyunaH4sA54xu86oW9AJ2mcZvLtj2ixN1N6s1ii153OeUs4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط تا ۶ شهریور: خرید کن، طلا ببر!
🛒
✨
تو
خرید سر ماه شهریور،
از کالاهای سوپرمارکتی  گرفته تا کالاهای دیجیتال و لوازم آرایشی و لوازم خانه رو می‌تونی رو به‌صرفه‌تر بخری.
👀
🛍
تازه با هر خرید، شانس برنده شدن
طلای دیجیتال
هم داری!
🪙
✨
🏆
نفر اول: ۱۰ گرم طلا
🥇
۱۰ نفر بعدی: هر نفر ۱ گرم طلا
⏰
یادت باشه فقط تا
۶ شهریور
فرصت خرید داری.
همین حالا وارد خرید سر ماه شو و لیست خریدت رو کامل کن
!
🛍
🪄</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/684881" target="_blank">📅 01:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684880">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
عزیزی: هیچ شناوری بدون اذن نیروهای مسلح از تنگۀ هرمز عبور نمی‌کند
رئیس کمیسیون امنیت ملی مجلس:
🔹
رفت‌وآمدها در تنگۀ هرمز با نظارت و کنترل جدی نیروهای مسلح انجام می‌شود.
🔹
درحال‌حاضر هیچ شناوری از تنگۀ هرمز، چه در ورود و چه در خروج بدون اذن و اجازۀ نیروهای مسلح به‌ویژه نیروی دریایی سپاه پاسداران نمی‌تواند عبور کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/684880" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684879">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پایگاه آمریکن پراگرس گزارش داده که جنگ‌افروزی آمریکا علیه ایران تاکنون بیش از ۱۲۰۰ دلار به هر خانوار آمریکایی تحمیل کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684879" target="_blank">📅 00:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
اخبار غیررسمی از انفجار در دمشق
منابع عربی از شنیده شدن صدای چندین انفجار در پایتخت سوریه خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684878" target="_blank">📅 00:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3fK_TCBHWlKOKVclfhNkQFmdyx_BPtmnWnyBQmxFaS9BXcB2HdVZZda-Z3gspu1-vHzfCuF4kqiVyktZUSOjOsriHGvZpBDHYlcK4GHpLVJMegFKU7Ujg6oAqL4_OrvlqjAB40blp_cta0HOSjDIDj1o67T8sCwJ0E9QrRyO5Jbgh_n3fK5k_rG_kVYJX_wvXYjcbC7E8Qej7k6v_SJsAdOxnrNDySQvBOrCrxQzwaQ2Khove_X3khNTEhn5fWySOLxVg6SydRcAJOZU3VtM0mtUVqAYdtyFyKOW86F3nuNmisgXIjPvnJ7IU3-YBlPuuOk0Qs8h8na7Fn1hHWOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی اضطراب یا استرس بالا میره، معمولاً اولین چیزی که از دست می‌دیم، احساس کنترله
🔹
ممکنه ذهنتون مدام سناریوهای مختلف بسازه، ضربان قلبتون بالا بره یا احساس کنید از پس این حال برنمیاید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/684877" target="_blank">📅 00:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RASeUDpQrK2KeBtGyOEMT990m759FDryChNHvGhzSHOR3lUaTELyNd7VKLrxC2EgtYddqEtz8DoIIDnVZnscIamKt_UqB9f_nYqiA-XA99jppiraclSFiWifD2VUicI6KnyZpbKH8IrD4tX8StkegwLM_ZDLeBdMIpLQWsYX0kvu_Z-EE3BwIeHGQMxc5QBZZLhdNXgRf9y2B4FZylfJ3LT714lnpZ6q89zDW6B_BSmHoLdFVKUGMvIgHEEN2nxe1qkyI3-Xs0AfEORPw1rhYjJa7XzKkDOnjD9ro72ydeCVFAXm1Vgc7il8acvLrDzdV7ubc2GeKvUHWU2Evih9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری گاردین از پول‌پاشی رژیم صهیونیستی در هوش مصنوعی برای سفیدشویی خود در افکار عمومی دنیا
🔹
هسته این عملیات، وب‌سایت موسسه هانوفر برای سیاست عمومی است که در ۹ روز، ۱۲۴ گزارش با بیش از ۵۶۰ هزار کلمه منتشر کرده است. این محتوا که به سبک آکادمیک و با استناد به منابع معتبر ارائه می‌شود، برای بهینه‌ سازی موتورهای جستجوی هوش مصنوعی طراحی شده تا چت‌بات‌ها در پاسخ به کاربران، به‌ جای اطلاعات بی‌طرفانه، روایت رسمی اسرائیل را بازتولید کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/684876" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWR52Sa7TtTFDIL4u3G_RdiiC_yCxnbfz3rNsPzXtGuDZobLcbDePTSjH0ecnRKQPxX_ECr2bMjOImydIaZpnXMbwCN4l8rtd2aD8VGdbt6pj8u-EJeJZFdoEXvdHiVbM8O1HkLEuwTm7fsjkhywp-NjnfogGrIpDcCelJkynasvcJQ2K5VajjdVrIrl3Vit0hdUOyK86jMGed-c6b3Jj0hYR7iG8cXzfPtTk58KJCSpXEO95vQjMSV9GYQT4cPOHhjPUtF1U8cm5HdDH4GXx4Gov6LpBk4NhkMMzLvg14RELXTRTGNrNu85EsPDRDQjQpGq5Dvmom7O1QAhLBvvkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/684875" target="_blank">📅 00:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684868">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVkuJ0QTucX1CPy3Tp1jKWVKvuwkUj71gFmcc9aTlvHSSnax4aQtsLfAaIoy2lQE-n9-ZpzgoBXGIuFcskGMqi3FhdLl0SniH6_3zAsOj6CW9aveiENgjc5-YVNxoB9Z5Td6YFiI7c_mScZQu-Ul5HJ0Dr5z6os9sqXweUo95_6FJjKg5ClLEsoOq_d54v1t3fgxGAZd7pEF_OqDJPSlcmRNceZdWcO0-5KPPIbBLRe5nr36brEfAavuOXPcWwCzvU-k78tKNFPgGCJpuT4fRvm8xT2GHjZtGb--3Up41os3NKYn-p2ySan4Q-c56E0VpTYyWLSDZN4Xy6F9wIJ3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EpV-02jBIgKaJuViezHYomAVRMeJ_Ia6jaEi8tVm3XgVfBtgPCua-3xKcIgrfpsaQNkyABUAvjqhfYOARL86y59JF-kF6Sczeth3FuaagZm6m8LXJakNiRZfV7p-pUr1bylLeQj6Ax30LTKoJhR110Hq8Td06jWV9tI20Lc_KRf18SiD3Ux0RhYjRHYAmMCrnfy1KkLW7iID8HyPMLT_QfjRdIazTuCiYllR1Sobn4t02xQT4p28pzVuSVNBquJaWYnd-8eZDWA6gKC1k6O8xOJNT_nIHX90YvXdAhlOlAsO_Mg-wo1hE8SD8KnuGqB3gI8gWcPkSpiZ_Og0XC67QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrQn60Sc8wKJWs59r_aey0wBnvAD7HQrax80bmlwoDyWAlyY1weRCJgZvGas3KCfzQcWLws7e81EmYa8n8szM4jfjn1ZW5NJDPKCKJWIUslhynjMXmxWoBVBPTTBKGZOuAOl9g4YHUxs2aoQAVMTbP0UCAqTX3pY_73Yq9x7qtNOCc2R7oVscSf08oJVcijWDwXvvQbOVUsDa9hoJuZvSHFs4lIrXOGWRZkzwj1YUfJauuBVmpiGlr4du6EyoZeBmI0SHvY52nGfJZqsXq4sMy0r4AC6OWPxSvVHchKB9F9sGM-EBCYqmuuWdHbUF-QuWmdbqHLhDaovw6BCEJTlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIlKY-AZKCM22xaszPFiwZwikonNuxN2QqS07SMtwGBlYQ6ELPz2LvY4OEAt7TrRGbcLaC8cLHLsANTRazV18nTV8ncs0bDnzVNhKeKeV-gZdAxCSXNONrEtL1I5VpZomQ3IDw-8jsWnocgt0LK400NEwDU81TcN7l2rFX3xwsrDXnJvVXeB3IKTGKJUHkT2SPh5HKhaZXnp8xWurOsGvng2Jlsy7QBAhJ6ywpO5lWe5gisIdNpYDAQgI4l1Yk7_9NMaOieYlFwma58EbpSh7l6JEL-5d4OrjL3-G-JPuf71Rs1gL6ZCmNysvN_15ut58vXWeRrtWtgabF5CpsVQgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4GhGuW0q7dopy9cbfOKEXbCkT4nI6p4WnY6TQbxxalMN04vvQ2pGi5kdAuf1Q4NzXhEz84TU6HJrBpdID7QdLzb1LexEnUiaraufgJDUu0Y7IKS61EvsmTNwaIwbY1fNUQqS7r3B80attNn2rsUPqN3_ABe5tEhqrgDDTM3HcKmu7gt0tnAFAPlS9CiN1swt6ezhgLzNzzxhLETastuwz7RLrYHhkTfiXi6CMTozJNWVXTVo8ADrapEyKP-wi3g9azrmSDMgZr0RWnDaelcuOVAsqFBXgz8kB0ZiZf0lFov8_hgSCP-2FXLH9UnsBrpNmk_5WAzXuJyMy4Uyn798g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rs071684xuBZlVssedfJKITyP4sKBRsnzUmIuXAI3Hi7J_AeHGYaxEGm2qVP385HEDGLaiXp8-_vr-fqHIHwvqiJblcynAGI0hWiY5eqHfL67mFQevl55qlcQYcaMBMc15LIH9TfPvqZCDdyKke4zNxVu2QAKUSulO4T29ifhwHBE23SXjuqO3UXITruxb7lJVOM3Nt73oFvXege7C7LT5B83cTeoWsS4-dxy3jFQ3d14p_QGOP89z0LXhq1TpEBCfuh97byF1Y59Hb367X7O4cSkrBZbbY5eiAYmB0MnbU5xhLGUgrvLym4SbAADK8AXub-TIFu0oEIpilZHuVXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvOtPYYTnWiAFRGs2zUDMipLqVn44kTW45J92Ab8s_dNCEPgc4KDZtxmEE6WmRx5wI_PkfH4T1sFE1xcFC5Awm_tJD_vFDjDofUJ4lOt1FU2rlMyBUZVpurNc0kju_M9g2nywQaLtFgc5M32_7L2Yxfjpp4EzW-vXV0n_MjBuhY5HOSaaoolC7XcwWMeAgpLnjftw4CEmX4Gk1L0fKRx1vgs8TWdfb4A5P9S-XbKTEPJSV-9jD7b8XybyTp9ejaZXLRHkFmMjAZ96RfoVGcnrq2wdSztXdCRCRDAwfVEqBYuf00VYcvmAQ7etc0n5kbhbRFbmPWHt-_lx1vpCGrVSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فشار اقتصادی بر ایران فشار بر کدام کشورهاست؟
🔹
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/684868" target="_blank">📅 23:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684867">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e631616a57.mp4?token=VfZu3R5pBr1CwMYgdJIp-kJbnC7Rfr0fzv_GF0y4o4SXp38pOM3hQW4ffwgp8VJU427f2Cy_4OH-oXWlhkSzmGJ7rD8D_KWvmsXBU_Lyy6cvvgwYvYeEX_gLkgv_RHW6mOJ6ExVqIcorX4ADJCVE6F3EC3UoabWfejgb_tPzweoTHvt5rUfgHK4_JySYV4KH0-0u7Cs6r83SOhFYjVvW2vCixelKoK8OdH3RBnwm6-xgS0qInqYdoxxHy7BLeu-Zh8R4m6v4W-GXJW6pqHOlXJNXtIFr5EvblQGbB2Nuzap0Qx6a5I-N3NTEKPS1ZUq9I0k0rmqD0MSiyX1IaNcwbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e631616a57.mp4?token=VfZu3R5pBr1CwMYgdJIp-kJbnC7Rfr0fzv_GF0y4o4SXp38pOM3hQW4ffwgp8VJU427f2Cy_4OH-oXWlhkSzmGJ7rD8D_KWvmsXBU_Lyy6cvvgwYvYeEX_gLkgv_RHW6mOJ6ExVqIcorX4ADJCVE6F3EC3UoabWfejgb_tPzweoTHvt5rUfgHK4_JySYV4KH0-0u7Cs6r83SOhFYjVvW2vCixelKoK8OdH3RBnwm6-xgS0qInqYdoxxHy7BLeu-Zh8R4m6v4W-GXJW6pqHOlXJNXtIFr5EvblQGbB2Nuzap0Qx6a5I-N3NTEKPS1ZUq9I0k0rmqD0MSiyX1IaNcwbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سقوط درخت در خیابان فرشته تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684867" target="_blank">📅 23:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f09d5bca.mp4?token=mHqT2ogatGDXxetjekj6jIX9r79Oau-AWygU6-raOL9S91mN1P8FHa6sT75kPPr-jzo3MjzwZh8io88b8l4VeVU0rOzVh1jYBGjtVYNy1SHydxidh-6QNajqHuuDq7c08hfJneUiKrCxi1IFkiF6IYUsOdbI46wEC36j66hJXhj89304Ssu5Rj6vOj7e-4_o-lpRSgqarCPr_3_uHU8qtK4QWEqlFYSpcKs3wDjFPzKoouHlZ6dDVdbqi7hniUWUIDgMSYUy_MagRfE5AtZVdjgaldlY_XokEIBMBAUJA3OdsTnsGpkULMmLKAdA9DTmElwto_wIHmUt1a_5kirtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f09d5bca.mp4?token=mHqT2ogatGDXxetjekj6jIX9r79Oau-AWygU6-raOL9S91mN1P8FHa6sT75kPPr-jzo3MjzwZh8io88b8l4VeVU0rOzVh1jYBGjtVYNy1SHydxidh-6QNajqHuuDq7c08hfJneUiKrCxi1IFkiF6IYUsOdbI46wEC36j66hJXhj89304Ssu5Rj6vOj7e-4_o-lpRSgqarCPr_3_uHU8qtK4QWEqlFYSpcKs3wDjFPzKoouHlZ6dDVdbqi7hniUWUIDgMSYUy_MagRfE5AtZVdjgaldlY_XokEIBMBAUJA3OdsTnsGpkULMmLKAdA9DTmElwto_wIHmUt1a_5kirtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارعی، کارشناس مسائل منطقه: ما در شرایط جنگی هستیم اما ادارهٔ اقتصاد کشور بر مبنای غیرجنگی است
🔹
در شرایط جنگ اقتصادی، مسئولین نباید با بیان نقاط ضعف و مشکلات داخلی، زمینه فشار بیشتر دشمن علیه مردم را فراهم کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684866" target="_blank">📅 23:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684865">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
صدای انفجارهای احتمالی در چابهار مربوط به انهدام مهمات عمل‌نکرده است
🔹
المیادین از اخراج ۴۰۰ کارمند اطلاعاتی آمریکا خبر داد
🔹
پزشکیان: کشور ما قربانی ترور است
🔹
تلفات سیل ویرانگر در مرز نپال و چین به ۳۶۲ نفر رسید/ بیش از ۱۳۰۰ نفر هنوز مفقودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/684865" target="_blank">📅 23:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4308563c0e.mp4?token=J9EWW0gqSymvSkJ_BTEDgupYnFis-0GjdZ4mvNJe-Gkt8y_Hfq9izvv5-yVVucN2krGi-IoVZ8fQaopvjF2pE01EPSmZaJtDekzlyaBDq6z0-Xl5nyh9Ob7wW1XYnuK4eWVVuDWEntXbcGGVfPOkakZfm5ieS8UN4-xyeaYmjVkdRE5DqrHE5RUjYjM-WUZREufa86EbFjVg4tulR8bqZ8vEnED-zuVspvuaty2VDgivm6xzIyTSqA6D3SjLxXOz3xWPZbrfr37AUtFhDD3WRxf7f1GSWjWsu8FCT2bjMiBc7DtZFxwlhvDCnIqzH0vqLUdB58TN1LsF5-uqXhwToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4308563c0e.mp4?token=J9EWW0gqSymvSkJ_BTEDgupYnFis-0GjdZ4mvNJe-Gkt8y_Hfq9izvv5-yVVucN2krGi-IoVZ8fQaopvjF2pE01EPSmZaJtDekzlyaBDq6z0-Xl5nyh9Ob7wW1XYnuK4eWVVuDWEntXbcGGVfPOkakZfm5ieS8UN4-xyeaYmjVkdRE5DqrHE5RUjYjM-WUZREufa86EbFjVg4tulR8bqZ8vEnED-zuVspvuaty2VDgivm6xzIyTSqA6D3SjLxXOz3xWPZbrfr37AUtFhDD3WRxf7f1GSWjWsu8FCT2bjMiBc7DtZFxwlhvDCnIqzH0vqLUdB58TN1LsF5-uqXhwToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارعی، کارشناس مسائل منطقه: اگر آمریکا بر تنگهٔ هرمز مسلط است، چرا هر روز مجبور به تکرار این ادعاست؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/684864" target="_blank">📅 23:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684863">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezv0XhYtiIKzcUlAIaIChm2YcVBPsOw5OqTMM6Pl3zc9S5tEYiPcbGHpACV7_mdoGBkd73Bf3hfsnGed2oRpxX6n0L7TaB8GySF56wBiuG1aiB47QcJBX7EosidJOtIlzJbYCLgQrTKXlb0MtpI34_uaTDtvOZeLEeqhkH1AGcxyO8d-bDoVVvsWqIOu8ttc5_6O8rpCfNT_pShAZKSodRBSH0IsQnqVU6u6dtDM0mjQwm0XhX0F6ka7ish1EIzBqtqpxGvgDweV2JJbhiboLRr1CvE7iJDp3y1G-WwDUJBL4AqHiulgUM2RlZedwrL79AnWe6oiOe4X5quRIjJshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: تنها مسیر نجات آمریکا، بازگشت به تفاهم‌نامه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/684863" target="_blank">📅 23:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمبود ۱۲۰ هزار معلم برای مهرماه
احسان عظیمی‌راد، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طبق آماری که حدود یک ماه قبل وزیر آموزش و پرورش اعلام کرده کشور برای مهرماه حدود ۱۲۰ هزار معلم کمبود دارد.
🔹
جزئیات کمبود معلم در مقاطع و رشته‌های مختلف هنوز به کمیسیون آموزش ارائه نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684862" target="_blank">📅 23:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87625552ea.mp4?token=dKeujCoVaXiTcTekVvnuhHqsP_MfaxgJsJdoYRVM8Y3jUkf-HLeUM-VOVaY8kd7AoTxBsf0Y7HBm1EZV57IHI95v5LX5l4uXX5epm2EjqM5D-N_ybrm149k2cIA7pZPecnErmyjyTQQMGDKSjSyXjqDWoCH7Ll_9LAcQyNcBTzzGIekL4v-yQnypy7xIb8VXb86SibMxGy8MrAcRrZ8rko931DqlsBYnucJajvSoyEdkS8VT0B1-e2aNIBcaAfQo7UAfAWnMPDb3i2-W2Ok2LkCq5rgGm0NjXkhp1Ls9RoeAg7yLsftzgQWus2wuHpUgaO7mHRYTsYqU8LyjfM27kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87625552ea.mp4?token=dKeujCoVaXiTcTekVvnuhHqsP_MfaxgJsJdoYRVM8Y3jUkf-HLeUM-VOVaY8kd7AoTxBsf0Y7HBm1EZV57IHI95v5LX5l4uXX5epm2EjqM5D-N_ybrm149k2cIA7pZPecnErmyjyTQQMGDKSjSyXjqDWoCH7Ll_9LAcQyNcBTzzGIekL4v-yQnypy7xIb8VXb86SibMxGy8MrAcRrZ8rko931DqlsBYnucJajvSoyEdkS8VT0B1-e2aNIBcaAfQo7UAfAWnMPDb3i2-W2Ok2LkCq5rgGm0NjXkhp1Ls9RoeAg7yLsftzgQWus2wuHpUgaO7mHRYTsYqU8LyjfM27kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوباره زبان بدن توسط فیلد مارشال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684861" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شروط ایران برای توافق احتمالی با آمریکا
🔹
وی با اشاره به اینکه تهران به امنیت لبنان به عنوان بخشی از امنیت کل منطقه غرب آسیا نگاه می‌کند، خواستار پایان دادن به جنگ‌ علیه لبنان، غزه و سوریه شد.
🔹
دبیر شورای عالی امنیت ملی کشورمان با هشدار به اینکه ادامه تنش…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/684860" target="_blank">📅 23:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3YA1XiDuM7ARGgL2VMReqY2cfSjADtIZTN61d0-V07AOhpl_z7cAZB8_BWiOzZfYJB49Ncd_kzFMZmjDRArCjPCjT9T5-adDFjpjmNfSyjVGrA203P-4msoPr8w-CsUAqXc8c3zGTbmB_JTxNvg3p8OoKTf9NLFmGeE7xADsRU2ZaGAwkCAJ6-0TMwAjTt2UHFnxWt33wn5unQ-aNwrXjMzf8udq6kMNsWCbL5ETxL9kwdiiWT4qZOCUiYTMBRjTX5g4oGwR9Lyn-osWE8U9estlNGJaKXTV77cc--fLfErHWMzmouw5Tmt0lVVsH5m3TXp1g-0XDAcVpHZjnr5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جیمی بانکیویچ، فعال سیاسی آمریکایی: اینکه یک پیرمرد ۸۰ ساله، چاق و نارنجی‌پوست که در یک فاحشه‌خانه در فلوریدا زندگی می‌کند، می‌تواند به‌تنهایی اقتصاد جهان را به سقوط بکشاند، ما را وارد یک جنگ دیگر کند، کاخ سفید را نابود کند و میلیاردها دلار از هوادارانش کلاهبرداری کند، واقعاً دیوانه‌کننده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/684859" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684858">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aee742b2c.mp4?token=NufInrjdJTKr6inmDxxUR5v5kc7099XtOGRwIHPO_4yxpEceIveMBQh8TYp5wdo858fXtEKesctuvQn_omuIyNRB7d5cAAKnrcdUfbgBWxg-BtbTdID6kIanDXrP8l4QW6rTKv1b9l20nYUPOdsG9_uTz-mBjbKkUKsbMmnHtTyDM-4hrlhURnVGpC9oM5Oz67wviVzyJ9cYsKHMC9-zwOuGxfDjvIHk8F1UcZJav8V1GR6bgWXa0uCCBEq8AjOxDyRhzeSwXOg2Dr0Sqi_l4wvxOhNx6k_-3C5LV2gQorq2p9udCfqvABfFo_qUQgM6ueaTxiwIdi1lfcG8igZI_FtAi0d_270j-2nCI-sS6KAROrzslrrlQqvG50ddZC4PqhYO1GPYwaXgxF0DGGeb_6-n6sDXj37AOfukUUvBDSeKNMWJLxw0WhJK15iQkC_9SSBWBFJzkj9e-ueTctL8HPpsnMB0jsz9TIN_cuKvPEynAUN7lGMsjkztFr-lrqF1ArQ61oLXMEhaIIwXI6pESSe7UER1LIPxtrMqtJmH7vXQrXMxHab5GoVjYhH7cNTS76JS2OWl8W6RhFu6XQes40Q7vvXyvSdGi8ylQ5AvDHAo6BK24LYifjlbwSyzCqEbaui99eqFK7RNIlkQ1XK4jPva8TtHetVmelsbs7zMcVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aee742b2c.mp4?token=NufInrjdJTKr6inmDxxUR5v5kc7099XtOGRwIHPO_4yxpEceIveMBQh8TYp5wdo858fXtEKesctuvQn_omuIyNRB7d5cAAKnrcdUfbgBWxg-BtbTdID6kIanDXrP8l4QW6rTKv1b9l20nYUPOdsG9_uTz-mBjbKkUKsbMmnHtTyDM-4hrlhURnVGpC9oM5Oz67wviVzyJ9cYsKHMC9-zwOuGxfDjvIHk8F1UcZJav8V1GR6bgWXa0uCCBEq8AjOxDyRhzeSwXOg2Dr0Sqi_l4wvxOhNx6k_-3C5LV2gQorq2p9udCfqvABfFo_qUQgM6ueaTxiwIdi1lfcG8igZI_FtAi0d_270j-2nCI-sS6KAROrzslrrlQqvG50ddZC4PqhYO1GPYwaXgxF0DGGeb_6-n6sDXj37AOfukUUvBDSeKNMWJLxw0WhJK15iQkC_9SSBWBFJzkj9e-ueTctL8HPpsnMB0jsz9TIN_cuKvPEynAUN7lGMsjkztFr-lrqF1ArQ61oLXMEhaIIwXI6pESSe7UER1LIPxtrMqtJmH7vXQrXMxHab5GoVjYhH7cNTS76JS2OWl8W6RhFu6XQes40Q7vvXyvSdGi8ylQ5AvDHAo6BK24LYifjlbwSyzCqEbaui99eqFK7RNIlkQ1XK4jPva8TtHetVmelsbs7zMcVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
سرلشکر رضایی: ضاحیه و بیروت خط قرمز ماست و هیچ‌کس حق ندارد به‌سمت بیروت و ضاحیه حرکت کند
🔹
ما با جدیت کامل اوضاع را رصد می‌کنیم و زیر نظر داریم. اسرائیل مجبور خواهد شد از مناطق اشغال‌شده در لبنان عقب‌نشینی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/684858" target="_blank">📅 23:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684857">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4699eef4cb.mp4?token=Vahy7L91skn9GIv_vI73IDFtMgJ2Jl1Ey6mwN-pPlq_XYER2LB8GPTc0aEsWc_aenRH3eaUZLuoF3WvqJ5LlD9856fE9eVMcnK_WRquCgiepFQsyuyWmSETJEzrkpXMg-Z4O2lihU5d4vAas1yEuSXJiJS3RmOf3GIv2K4su--vUumr5t2n_pyKQlc2W9etvOxg8KwLwpyFQBIyD4to79rCTKFj8R1co_W2aKmL7ajpKydHUlTVYsCjS4mDWhJ_bNtnhmMGwYAQ7oLZTZw5bXoOzvsp4WnTNc-y1x2hbhUAf1fS8JCR_Kpf0q9uItscoqyQUss2UZyO3qr4lMHJU_C8nC7vUfDkM4MUugdCqOUn2QWPJA3FvVx-gGgtV3Hn3NQZrF77CPPj-XJfOOsMObO4G37q2GPZtUkzleS_3L4XCLcACFAbFvsqC2aKz-XDzSCXvFUup4NersWWZjDMnFtR5RH0G35vSud7s_1I1c6orlrGRrP5GgnOo45wKuMVWHjDuwPTZogM4SDjeVCUwDsQKdP1qDkhKF2JSHqEHptKSFvzkda9VQU5zVPBU3Ufp8QtrSACueT4Xxki6KuRNE6bSSqLlkhiBMmKBuQsQjZ0NDhedBTsC8yw0SC-etDJPOFJ1Gl4h0TSsjLCLn-rbo604hAWuiYUCyC3wUKIyJ5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4699eef4cb.mp4?token=Vahy7L91skn9GIv_vI73IDFtMgJ2Jl1Ey6mwN-pPlq_XYER2LB8GPTc0aEsWc_aenRH3eaUZLuoF3WvqJ5LlD9856fE9eVMcnK_WRquCgiepFQsyuyWmSETJEzrkpXMg-Z4O2lihU5d4vAas1yEuSXJiJS3RmOf3GIv2K4su--vUumr5t2n_pyKQlc2W9etvOxg8KwLwpyFQBIyD4to79rCTKFj8R1co_W2aKmL7ajpKydHUlTVYsCjS4mDWhJ_bNtnhmMGwYAQ7oLZTZw5bXoOzvsp4WnTNc-y1x2hbhUAf1fS8JCR_Kpf0q9uItscoqyQUss2UZyO3qr4lMHJU_C8nC7vUfDkM4MUugdCqOUn2QWPJA3FvVx-gGgtV3Hn3NQZrF77CPPj-XJfOOsMObO4G37q2GPZtUkzleS_3L4XCLcACFAbFvsqC2aKz-XDzSCXvFUup4NersWWZjDMnFtR5RH0G35vSud7s_1I1c6orlrGRrP5GgnOo45wKuMVWHjDuwPTZogM4SDjeVCUwDsQKdP1qDkhKF2JSHqEHptKSFvzkda9VQU5zVPBU3Ufp8QtrSACueT4Xxki6KuRNE6bSSqLlkhiBMmKBuQsQjZ0NDhedBTsC8yw0SC-etDJPOFJ1Gl4h0TSsjLCLn-rbo604hAWuiYUCyC3wUKIyJ5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: چیزی که در تفاهم‌نامه نوشتیم و امضا کردیم به نظر من سند افتخار جمهوری اسلامی است
🔹
بارها گفتم همه عزیزان شورای امنیت از این تفاهم‌نامه با قدرت دفاع کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/684857" target="_blank">📅 23:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684856">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سرلشکر رضایی: نتانیاهو را روانه جهنم می‌کنیم
🔹
دبیر شورای عالی امنیت ملی کشورمان شامگاه امروز پنجشنبه تأکید کرد جمهوری اسلامی ایران بنیامین نتانیاهو نخست‌وزیر رژیم صهیونیستی را به جهنم خواهد فرستاد.
🔹
ما ثابت خواهیم کرد اشتباهات بزرگ نتانیاهو باعث شده پایان…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/684856" target="_blank">📅 22:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
واکنش دبیر شورای عالی امنیت ملی به اخبار نقشه ترور فرزند ترامپ از سوی ایران
🔹
سرلشکر محسن رضایی، دبیر شورای عالی امنیت ملی، در واکنش به گزارش‌های مربوط به توطئه علیه پسر ترامپ، این ادعاها را پروپاگاندای ساختگی و ترفندهای نتانیاهو خواند.
🔹
ادعای وجود نقشه‌ای…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684855" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336d4b6b15.mp4?token=Ou3efyjld96AM4vhJQpApL7f_YAWa80JZEUHzFOGEADRkY1jYh9W3GOWgSuZaihPSjtyj2U17aXjq28gtUFwfxVuYEHfmxldw9x_UBxYXRWY7EYxEb2IF6s212hSBiLAxdUKOWieVosTVEZEx2a-7DjLULWQsQttmqCMI_NIFEW2y41P2L9Idu46-Vb23iS-p0fjkpKYf6aryBIqGefVRoDQiV9I3DBJOnEpBnihaYUL40IJfG-_nX5OqLyg3Ky7hLVVHGVi_nAI1l90AgnEmuaat_kiNO9W_0Pk5ShUUk--vb5l-UCji9VQJA7KsONy5Tgr5k1Mckc8SKVdmm0UNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336d4b6b15.mp4?token=Ou3efyjld96AM4vhJQpApL7f_YAWa80JZEUHzFOGEADRkY1jYh9W3GOWgSuZaihPSjtyj2U17aXjq28gtUFwfxVuYEHfmxldw9x_UBxYXRWY7EYxEb2IF6s212hSBiLAxdUKOWieVosTVEZEx2a-7DjLULWQsQttmqCMI_NIFEW2y41P2L9Idu46-Vb23iS-p0fjkpKYf6aryBIqGefVRoDQiV9I3DBJOnEpBnihaYUL40IJfG-_nX5OqLyg3Ky7hLVVHGVi_nAI1l90AgnEmuaat_kiNO9W_0Pk5ShUUk--vb5l-UCji9VQJA7KsONy5Tgr5k1Mckc8SKVdmm0UNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: ایران ۸۰ میلیون بشکه نفت در دوره آتش‌بس صادر کرد
🔹
دبیر شورای عالی امنیت ملی، در گفت‌وگو با شبکه المنار ضمن هشدار جدی به ایالات متحده، جزئیاتی از شکستن محاصره دریایی و وضعیت صادرات نفت ایران ارائه کرد.
🔹
اگر محاصره ادامه پیدا کند، ما منافع…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/684854" target="_blank">📅 22:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94d470f4a.mp4?token=LPaoAHO1FHiLmnB1XJ-dxF5kOYX0HrVz3XNMMlNM0JuUCpWN_ZVFFtzRPkteHwhzJ3WcllOL3uSuDkomcp12wPQS9K2kq8SIpqF0Rmi16buADD6Yyyan1FaePjeGyc67aasZYydlzru8jSD4f6ZGf7HVERKjZIaH9gz9zbgqHcI7bWCZ5Fveq1LOSO81LxP1cWDg6LTF0PU_MznSfxrfW3BlkE2AFjHqyKIy_QpMIAt-yMY719k1zuZ0G_0GYOqGRmR17opdnLAa1wHTUm2qEN8RlsfXgjI9W2a9oh9VL05WkKia73bRowOwEzJ5q_vUccWw8-hC3Zc5xmRD_ExYazN17cS6XDzTv2BfM41QR3hV7qBvsi29TYBoEr3rF-aW850Af0sYy3vEyRpUxQ6wVSeI_ukoZG7fiz-YveXdpEzLrMcBXDu9jZhH9kxfA323d1AAjTS77MVGxRAXfAflx9-FErneAvYpbyRfDMtokKS91JMTkQoHWX7dG8tULKLBPoEXQZVo5IycctDRgGs4_XbKQz2zutboPmJoAmDnKkDs2GUDPvEMsAa0p3wMRh1J-5gv9LhOYHoZNcaFYpKW5fTokUjr1c6TjUjx5bJCtRJaLbNqkZfPn7DbwhwG4glnGAtSoLAwnK4wRyz5Lvg57iqk79J0PUW6A7yCNr9ABc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94d470f4a.mp4?token=LPaoAHO1FHiLmnB1XJ-dxF5kOYX0HrVz3XNMMlNM0JuUCpWN_ZVFFtzRPkteHwhzJ3WcllOL3uSuDkomcp12wPQS9K2kq8SIpqF0Rmi16buADD6Yyyan1FaePjeGyc67aasZYydlzru8jSD4f6ZGf7HVERKjZIaH9gz9zbgqHcI7bWCZ5Fveq1LOSO81LxP1cWDg6LTF0PU_MznSfxrfW3BlkE2AFjHqyKIy_QpMIAt-yMY719k1zuZ0G_0GYOqGRmR17opdnLAa1wHTUm2qEN8RlsfXgjI9W2a9oh9VL05WkKia73bRowOwEzJ5q_vUccWw8-hC3Zc5xmRD_ExYazN17cS6XDzTv2BfM41QR3hV7qBvsi29TYBoEr3rF-aW850Af0sYy3vEyRpUxQ6wVSeI_ukoZG7fiz-YveXdpEzLrMcBXDu9jZhH9kxfA323d1AAjTS77MVGxRAXfAflx9-FErneAvYpbyRfDMtokKS91JMTkQoHWX7dG8tULKLBPoEXQZVo5IycctDRgGs4_XbKQz2zutboPmJoAmDnKkDs2GUDPvEMsAa0p3wMRh1J-5gv9LhOYHoZNcaFYpKW5fTokUjr1c6TjUjx5bJCtRJaLbNqkZfPn7DbwhwG4glnGAtSoLAwnK4wRyz5Lvg57iqk79J0PUW6A7yCNr9ABc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انجمن تولیدکنندگان فولاد ایران: بحران انرژی، تولید فولاد ایران را زمین‌گیر کرده؛ ۱۰ میلیارد دلار فرصت صادراتی در خطر است. راه حل؛ صرفه‌جویی است/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/684853" target="_blank">📅 22:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2636d3473.mp4?token=QuZevQipahT0ZUU1EHsSWNQIWraTGIKL7oJXg0nz_upgujG_0khQ9ti_2b61bOEYVr9k439zwfHnjNQdnBw5aHjnFkGfUI0A8j4Jv7Jk3vIIVyzLrwZiVJ0aRtcbeohGeETXF2A8y8GHjFWUXfrrt_2GNLD-xm5eUnotiHYfrT1--FQgrxw1hajNA50Q0ka7ZZ9Tgow8LBsPw1BVvr4_epITLnQCqmKQJAPS_vDrbppcZ453TXkdEuWAiEBP7CqvRKOHgZhBO0sJEQ7YpY9UGHCtXB1kwtARr7Nxnfbj_JZcNc8xcY3mPD0uDvXwl52L3PF6gHSjhTW4wJ_F9tywxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2636d3473.mp4?token=QuZevQipahT0ZUU1EHsSWNQIWraTGIKL7oJXg0nz_upgujG_0khQ9ti_2b61bOEYVr9k439zwfHnjNQdnBw5aHjnFkGfUI0A8j4Jv7Jk3vIIVyzLrwZiVJ0aRtcbeohGeETXF2A8y8GHjFWUXfrrt_2GNLD-xm5eUnotiHYfrT1--FQgrxw1hajNA50Q0ka7ZZ9Tgow8LBsPw1BVvr4_epITLnQCqmKQJAPS_vDrbppcZ453TXkdEuWAiEBP7CqvRKOHgZhBO0sJEQ7YpY9UGHCtXB1kwtARr7Nxnfbj_JZcNc8xcY3mPD0uDvXwl52L3PF6gHSjhTW4wJ_F9tywxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراقب باشید؛ تخفیف‌ها دارند سرتان کلاه می‌گذارند
🔹
تا حالا شده به خاطر دیدن برچسب‌های تخفیف مایل به خرید یک کالا شده باشید!
صبر کنید شما شاید از این تخفیف نه‌تنها سود نکرده باشید بلکه ضرر هم کرده باشید.
در این ویدئو به شما می‌گوییم چرا!
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684852" target="_blank">📅 22:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19455c6be.mp4?token=CGWb4Va5-FKbPZTeo1GZRxDOeGGFZ-_MdVQLKdwoM6FeMIuZCzs6m9gjhBQNvFvl5KH6dY9K6B8jIIZLxd5ibZwovmyLKCN23-UMij5b0Jrf-l2kG0MMYdbU_8wM8ASaZ6JRi3zTkAYkbIkkF-UA178nZ1DKr6ct34NPk1AwE0XbwoNhJu-D-N6u67T4raJsnF04_7Om-S4AD_8N0WRbw2NnuU_92R6XBmXcUQM-HLIBcWEm90iSCgfW-Cj7VfPWjJvUZouafn5qn3laeqlSJ4EwsPHQebJlzXHT36IvQeP_uakt2z0o9pOiy6cKGXRe3vBjl64JqehT-l4koF8g0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19455c6be.mp4?token=CGWb4Va5-FKbPZTeo1GZRxDOeGGFZ-_MdVQLKdwoM6FeMIuZCzs6m9gjhBQNvFvl5KH6dY9K6B8jIIZLxd5ibZwovmyLKCN23-UMij5b0Jrf-l2kG0MMYdbU_8wM8ASaZ6JRi3zTkAYkbIkkF-UA178nZ1DKr6ct34NPk1AwE0XbwoNhJu-D-N6u67T4raJsnF04_7Om-S4AD_8N0WRbw2NnuU_92R6XBmXcUQM-HLIBcWEm90iSCgfW-Cj7VfPWjJvUZouafn5qn3laeqlSJ4EwsPHQebJlzXHT36IvQeP_uakt2z0o9pOiy6cKGXRe3vBjl64JqehT-l4koF8g0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: ایران ۸۰ میلیون بشکه نفت در دوره آتش‌بس صادر کرد
🔹
دبیر شورای عالی امنیت ملی، در گفت‌وگو با شبکه المنار ضمن هشدار جدی به ایالات متحده، جزئیاتی از شکستن محاصره دریایی و وضعیت صادرات نفت ایران ارائه کرد.
🔹
اگر محاصره ادامه پیدا کند، ما منافع اقتصادی آمریکا را صد در صد و با شدت و قدرت هدف قرار خواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/684851" target="_blank">📅 22:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684850">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
جزئیات مهم درباره مذاکرات ایران و آمریکا به روایت وال استریت ژورنال
👇
khabarfoori.com/fa/tiny/news-3240938
🔹
اخبار تاییدنشده از حادثه دریایی در تنگه هرمز/ تصمیم بی‌شرمانه دادگستری آمریکا برای سرقت نفتکش‌های ایران
👇
khabarfoori.com/fa/tiny/news-3240776
🔹
فارن‌پالیسی: ایران در آستانه تغییر استراتژی | چرا تهران ممکن است دست به اقدام نظامی بزند؟
👇
khabarfoori.com/fa/tiny/news-3240844
🔹
پرونده خودکشی خواننده مشهور زن، قتل از آب درآمد! | تصاویر تازه از شب مرگ
👇
khabarfoori.com/fa/tiny/news-3240780
🔹
بازگشت محسن نامجو به ایران پس از حدود ۲۰ سال/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3240870
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/684850" target="_blank">📅 22:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
المیادین از اخراج ۴۰۰ کارمند اطلاعاتی آمریکا خبر داد
🔹
المیادین به نقل از منابع دیپلماتیک اعلام کرد یک گزارش محرمانه، از شتاب گرفتن روند تضعیف دفتر مدیر اطلاعات ملی آمریکا حکایت دارد.
🔹
این گزارش محرمانه به ‌دست کمیته‌های امنیت داخلی و امنیت ملی مجلس نمایندگان آمریکا تهیه شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/684849" target="_blank">📅 22:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684848">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ: دیشب ۲۴ قایق را از تنگه عبور دادیم و ما دائماً از آنجا عبور می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/684848" target="_blank">📅 22:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای منبع آمریکایی: هرگونه توافقی که بین ایران و سلطنت عمان حاصل شود، برای ما هیچ اهمیتی ندارد
یک منبع آمریکایی در گفت‌وگو با الجزیره:
🔹
تنگه هرمز باز است و تمام مین‌ها از آن جمع‌آوری شده‌اند.
🔹
هیچ مذاکره‌ای با ایران در حال انجام یا برنامه‌ریزی شده نیست و محاصره دریایی همچنان به قوت خود باقی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/684846" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrkCX6rYbKetYtuyroDt3bALsbRo5Zj5WcRMzi8yEKTo1xZuusdqxQde8ulLH1e5Av3zy76YX-3FnnTSO0DAjji5C9VH3sK4zOwxFuQP24ySXgUCW-Y9meU0RPtldTvbiXVWvl2jdK6OxlVm_oBc-UTngTrZ78WYs9wZU_OCy7WrFf5cepFD7ZYbJ5MuPlAGjTQrZsa9EagrPtZo6Ao3warhNtaMC9MIPU2FiesQH_tIyib9JtcRxcms62Bh21a-leGaFyLD9FeBzPhGELvXf_FpGF_yDCuIGUROephKr43s9HaipvoIcvPonuwxDHEVsP1EHUx0u5JZ_5piGMJE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چاپ روی لیوان؛ شروع یک کسب‌وکار خلاقانه با سرمایه قابل‌مدیریت
🔹
در کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
از آماده‌سازی طرح و انتقال…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684845" target="_blank">📅 22:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2U8AulZeRmzSSkZUxOubu0tdtX7dgwOsBRCttlDqsQcD04QvTaG9GAb2x1juyb2h_NKetDgvGTaA4LHfWdbkHyBOSj7HwkC8W82fBSwXr1dJoDUyiszF0q1ot_Hly__h6Hl1Sardemb0DiBY6kTEo-ts3g7UD810a2jYNeJbbmQ1VnRoas8LXtzXCOPG7AxW3lYnUXpsLxsaPmzOfQxq5KLtcu9npGO_7cRSQJd-O8JzhgnS1hoaVxTglvCYxNt6DQoAwhNFWt0EX1I7zLxE6_x_T5QhfHG0Hmz4IjrskYWd2t0hD63S0RcMH1TZZigxYmNkchbsvJlIivCuTaxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/npzlj
https://l.snpy.ir/npzlj
https://l.snpy.ir/npzlj</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/684844" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خبرنگار: «با کدام رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟»  ادعای ترامپ:
🔹
خیلی حرفی برای گفتن وجود ندارد. ما نمی‌خواهیم با آنها صحبت کنیم. تنگه [هرمز] باز است. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684843" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
خبرنگار: چرا بانک‌های چینی که با ایران تجارت می‌کنند را تحریم نمی‌کنید؟  ترامپ:
🔹
کی گفته که من این کار را نمی‌کنم؟ تو نمی‌دانی که آیا من دارم این کار را می‌کنم یا نه. من مجبور نیستم همه چیز را اعلام کنم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/684842" target="_blank">📅 22:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684841">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87dd2f42bc.mp4?token=VehG4C6petBo4FOKaA1EBPA7QzPnM_iKb5cU-YVusFoPWRFvso70trpmGoYIVeNbfNg-weEE2JaaEBvkTI0Ch_KaZxYENWeytthhuA5wPYmOT8ogxh5ShD5CKtN-2wYkOSo3avYYvrScUrfp475ERyJLv-9SDdyZxzY8r3WBvesq4NFk-_ucdUMM9bjWX8Yklf05i5QQqnfK0mW9KF8Im1DcsmeVlFXIU_36cvUQBDynP884nCcUzgcpfmYjCVemskytmpOWdmhoLCcNhCLrQ9SqC87HQR95-YLHHTig4_3BFgjGXBv6_3t-NiMfcoZKX-v9-7XuEPhqKDcpZhz0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87dd2f42bc.mp4?token=VehG4C6petBo4FOKaA1EBPA7QzPnM_iKb5cU-YVusFoPWRFvso70trpmGoYIVeNbfNg-weEE2JaaEBvkTI0Ch_KaZxYENWeytthhuA5wPYmOT8ogxh5ShD5CKtN-2wYkOSo3avYYvrScUrfp475ERyJLv-9SDdyZxzY8r3WBvesq4NFk-_ucdUMM9bjWX8Yklf05i5QQqnfK0mW9KF8Im1DcsmeVlFXIU_36cvUQBDynP884nCcUzgcpfmYjCVemskytmpOWdmhoLCcNhCLrQ9SqC87HQR95-YLHHTig4_3BFgjGXBv6_3t-NiMfcoZKX-v9-7XuEPhqKDcpZhz0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: چرا به‌جای اینکه با دشمنان آمریکا چنین رفتارهایی داشته باشید، این کارها را در قبال متحدان آمریکا انجام می‌دهید؟  ترامپ:
🔹
نوشتی؟مقام‌های کانادایی آدم‌های زننده‌ای هستند. آنها ادم های بدی هستند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/684841" target="_blank">📅 22:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684840">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxy2VZgM5YQXJM4LtbZ-OM7Dxh_JSxtv4Ps30M1pxPa4S0qtpQGNW0NdPgeL5IkFHY401E1eO5q0cuBoNq6sbIvjeFiHilIG420TV_rrZwsnL9hq-0ZIumfnFbFay0l8XIFoCdM7BYFOedVhf8Hkz39qxTmZtibnQbPfZCp0uapyQAg6uIDWYqRYHSTH-6jhMY6Kw2sVBHTubKh4F894vYtzwSswEUnK43yU3JYsQpzAv9E7YGIB3_HjQCfYWzhgOYE-BQUxWfpyggDnAcG8grWA1OS59irPS7XZHUmRDqChnyGE9v_kzOU0QabP_xDl0AzDCTf15rcij39qn9ulKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژدها وارد می‌شود
🔹
کاخ سفید در بیانیه‌ای اعلام کرد که «دونالد ترامپ» رئیس‌جمهور آمریکا فرمانی را امضا کرده که بر اساس آن برای حفاظت از سیستم برق این کشور در برابر تهدیدات خارجی از جمله تلاش برای خرابکاری و حملات سایبری، وضعیت اضطراری ملی اعلام می‌شود. برخی رسانه‌ها مدعی شدند هکرهای چینی به این سیستم‌ها حمله سایبری کرده‌اند.
🔹
هشتصدوچهل‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/684840" target="_blank">📅 22:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684839">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgMF9QsctC34tb0EPTH4Gxxi_24Qtt-SSJs_5lvNiz55Wmyd_XDEwuheQ3-DI_g5qVmjVD-MP3RdgglyMMX9gdf_fRShtsl18xyH_GPKHxjdpFvc3By6PRbjNQdjd07_i_EZJRhWOTzMl_Y-bW-tTZ8OvWDABNSstyFLKqTY4VgI9BkJamh9G_ShWLnvBXgJhqAuoq8QtqPYmZLDtLZ_L0OF04l0_jZNdFr4nkk2OLNCrhfiSzwYaGWuUkXIc83kOrU--W8vAuesxhK-ATrtXlIxWS7FHZAFnoqS2Iaiuw4VbdLGxFg4MINt1-W48CRDi8CZPA2EV6F9yu376Ytrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: چرا به‌جای اینکه با دشمنان آمریکا چنین رفتارهایی داشته باشید، این کارها را در قبال متحدان آمریکا انجام می‌دهید؟
ترامپ:
🔹
نوشتی؟مقام‌های کانادایی آدم‌های زننده‌ای هستند. آنها ادم های بدی هستند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/684839" target="_blank">📅 22:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684836">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6KO4AZOyviDwzLmKEzufeN4B3ynkuE_6g0d3agkMxDvToOdBO22qm9YuNX28t5orCktsZblZayMxRpDZOKEmsxiJlytmug0Ws1W9JsfSOwb2CbVo2_ZRt9sRmRoL2ksyfb_Ay0JGmgAN3c1nZOMcVjlnq2OyxnV2Lr3um0tLuUDobH48j--afYqpg7bJrYFWAweUF00SbrcH6cK9pbHF15rPaUtSAdf_sBxwy_8aLm4Qvwif03iju0MOifdYkKkL_XwPhY_j9P_bT6vWF1ZTT2-OphsGqvOur7otKWyjtjGqb2-ZUxkVQinj_kFHXYUYScPQ8LykmElUnjWtH6rKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qn4evYFKeR1wqIazFH0jonJbRrTp2CsVImNyhxSjgeuv_ej8z9A_nTQV5yap2pBxF37zvKETx1duC_IzOrVO_lhU0ZVPLnx20j6mgxk8HmK86IGaqrwDdZjI2xr97TuC0VnumBt_yf1lylzQVY6VzWsvGretgNY2JGIDmhCGZ-ZtT2QxTGvovr050oWqHEFEXxUgMdhCPyysMV1cvcLE9NW0qv53ggMquvgTCJQuVA_hzKJOe47yuNzg7McVyIOhLy439Ysk47Q7VI7D9GMEExmNRpbK8ktp-HuD3rBRRtnCiaVTAm1qiMQuHD2KBS10wj6mdecAlvAdQ89D4Kc52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3iRH4i5nMpRRxIp7ttOc9h2YDYtgKHl39ObqvrNDU9_gF_H7yMPH92kXW5P9q0dz6QfLVFdGxLTcSyjLycn32s17Stevzt9-MV2k51vTdisHucydCSEPrDYTwtxsM5T-7vkZ6sZf1Cu8Gnksk4_R_AJ36GUJXTXBwrRZvUDh8sAFGtFHaL0WKdy48qVyyi6foHPATltA4dNSDN2iCV3a1pBPuiYRBM4l9k5GmCicPcCPf2NMqWbRRNiFM8KkLiLkDTvw9SlbA6B__lbZboUUHEDLAM8TTYbzIUIpEp6ZFHLDRMGDb7GEUIqhFiX4q8M19822rtCvnundKVRf0kFRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بزرگ‌ترین پروژه زیست محیطی مهار گرد و غبار صنعت فولاد جهان در فولاد خوزستان افتتاح شد
🔹
با حضور شینا انصاری، معاون رئیس‌جمهور و رئیس سازمان حفاظت محیط‌زیست، ابرپروژه زیست‌محیطی «وین فنسینگ» (Wind Fencing) شرکت فولاد خوزستان به بهره‌برداری رسید؛ طرحی که بر…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/684836" target="_blank">📅 22:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684835">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaEZoG6mqAYswz_EKZ9m7tqtA9QFVbYSuIKx-ELdFhTTMxUujoBDOK7qvEcLzfuyIBo9IyKvjPHR4h8W2SDvF5OZtW-LLgjYEF02oePaJL46AZw7RVfVd2thcCWH1as0MNT41tCbRQ024B40bvW7blO1kCBW_5GeZCcN3lAVVgAya5Z9UKvmcSg-eoLHuw_UXLsU3Z2JE38hIdZ2aXX6JCrtP95uPD1MOLn7WjRwPzbKLBzDXz6rg0qF_e9aARJFnnDRO3oKSIuFwNzoXnwhWQezWiZkbLiXC2EvFBF9R_I1Cj78gKTi-1o81sxaljdKZpdxzqjUiErZstHWyu1S9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله تروریستی به خودروی مرزبانی در محور مواصلاتی میرجاوه - زاهدان   پلیس سیستان و بلوچستان:
🔹
در پی اقدام بزدلانه و تروریستی اشرار مسلح به خودروی گشت مرزبانی در محور مواصلاتی میرجاوه به زاهدان، یکی از مرزبانان جان‌برکف، به‌نام استواردوم «علی حیدری» به درجه…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684835" target="_blank">📅 22:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1052c3c78a.mp4?token=I2DFJ3hiJ7VfYwoamMhUxX9P2M3XuJBt7JgcriXc9RLKAB6_9yBJQAFuZaZNwQdRx9_eYRGFSKEtfVOCO96sveRT_-91ZKeXf5HaZREC1ajQNsNmMaRlbahYg_T5rbVXey5NI4CkWjArW4IvqAcE5GQrfub8IQOdQzgbspKsL3M-4igwMU2BnlDhBpcUF1T6PHNf3l-SfVnsTbbdR-A21lXi645fvtYro7liKG2DwObrJCzOKV6Cb7x--0vocP_3_3o3XyvthnuHbiLTlilg7W7bFnMoHEfrIovKUesuM2REYiOPrbBU8fxatC_8ZQEjYsxnpuRF3j6fQ10gkeijVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1052c3c78a.mp4?token=I2DFJ3hiJ7VfYwoamMhUxX9P2M3XuJBt7JgcriXc9RLKAB6_9yBJQAFuZaZNwQdRx9_eYRGFSKEtfVOCO96sveRT_-91ZKeXf5HaZREC1ajQNsNmMaRlbahYg_T5rbVXey5NI4CkWjArW4IvqAcE5GQrfub8IQOdQzgbspKsL3M-4igwMU2BnlDhBpcUF1T6PHNf3l-SfVnsTbbdR-A21lXi645fvtYro7liKG2DwObrJCzOKV6Cb7x--0vocP_3_3o3XyvthnuHbiLTlilg7W7bFnMoHEfrIovKUesuM2REYiOPrbBU8fxatC_8ZQEjYsxnpuRF3j6fQ10gkeijVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ حمله صهیونیست‌ها به وادی السلوقی در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/684834" target="_blank">📅 22:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684833">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALtYxaLlfXKgDcip1DKldaH8OmlWfQhSVlVBRQtHPAKiXk8FTCBNmvNqZAAfbQUmakHHyjapuLwvo9NgbH1cOTRJO5btSmZVkfyieKcPzBr8SlZv5DjbBSlT-TDKqJyDgHNqPZci75v9Uf9kY2hEqoCzsxj5k8DX-uTE0hqwsvRUx2FyC8IYoaogLzfauchk-Xg3Jq4LfmJjNpHDOhy-7yGATScngJuPLKdyuyXw4xMhBGOt8d5Y-YvmFGddwe3RqoxNXq-sQc026DtXKY5sjtrRHLlsMUHj_fdlIpda0R0k8HmIxINJ8vNxgoG-mlJfvagaWjci1mYxMthu4WUQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظلم، هرچقدر هم که ادامه پیدا کند، بی‌پاسخ نمی‌ماند؛ روزی عدالت فرا می‌رسد
🔹
امام علی(ع) در نهج‌البلاغه هشدار می‌دهد که ستمگر، دیر یا زود نتیجه ظلم خود را خواهد دید. شاید پاسخ ظلم در این دنیا به چشم نیاید، اما در روز قیامت، حق از باطل جدا خواهد شد. #نهج_البلاغه_بخوانیم…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/684833" target="_blank">📅 22:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684832">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmH5lDlULTvvf4iFnyH0lpD4xOUX8pBT3fw-js7EGeJ5d1YA_3JTM_kvAjYDeJmTGoLb70qYbxZ2FXvUTdJZ4rxCW4dyuxqLzIyBrVb6UvsSlj-g5DYJPSFCThX-VEew5r-MMTg2tpYLJ5YgqNTQ7L0tjGZIgB4nKuRvySRp3h4TLY1N8czWOKdSF-w8nJjl3LMhBSQFapJVvrXyq9YQhsLv2p29BeQx7QbBw2NO0oo40XNViCw5WpVDnCvDr3o19lcJ4ip0tkf_scX6lDT2vYdqXITOMf2JsHkY0uVOEfQWwDGRfyucZ4pFqquo0uZtXnS78vSXfIAO-jRzX-qN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تراز انرژی در کشورهای جهان
🔸
بررسی وضعیت تراز انرژی در کشورهای مختلف نشان می‌دهد که تفاوت چشمگیری میان صادرکنندگان بزرگ انرژی و مصرف‌کنندگان بزرگ صنعتی وجود دارد.
🔸
بر اساس این آمار، نروژ با ثبت ۶.۳۸ درصد، در صدر کشورهای دارای مازاد انرژی قرار گرفته و ایران نیز با ۰.۵۲ درصد تراز مثبت در میان صادرکنندگان جای دارد؛ در مقابل، غول‌های صنعتی مانند ژاپن، آلمان و چین با ناترازی و کسری انرژی مواجه هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/684832" target="_blank">📅 22:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684831">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عراقچی: ایران در پیگیری منافع و امنیت ملی خود مصمم و ثابت‌قدم است و از همه ظرفیت‌ها برای دفاع از حاکمیت ملی و منافع خود استفاده خواهد کرد
🔹
وزیر امور خارجه کشورمان در این دیدار با استقبال از تداوم نقش‌آفرینی کشورهای منطقه و همسایه برای کمک به کاهش تنش، خاطرنشان کرد که وضعیت کنونی منحصرا نتیجه تجاوز نظامی آمریکا و رژیم صهیونیستی و نیز استمرار اقدامات مداخله‌جویانه و غیرقانونی آمریکا به‌ویژه محاصره دریایی و تروریسم اقتصادی آن علیه ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/684831" target="_blank">📅 22:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684830">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
جنون ترامپ پس از تکرار شکست‌ها  رئیس جمهور آمریکا:
🔹
ما یک خلیج داریم. یک دریاچه داریم. حالا چیزی که نیاز داریم یک اقیانوس است
🔹
شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684830" target="_blank">📅 21:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684829">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d083252f.mp4?token=ZAgcIAjbT2YSqW_uVEhlVViG7RaNsOGMQ0j7CHKbMoYbwVQhp_iT4sRxVcMVFtE0NBQePH63r-vStgn2Q7Yjbeu8HOhXfpm6CDyFG1zsGefRuw-t2jfU5mJqSJYQ0KTZh7V7Be1mFkXGu61fqm-3ZzbAqoY09vBhA7S_enAiblTLxNy67e4ZOxTMKF1NKPpBRcvtsaKC_x0o5vBLpZjcVe6zfmUUvvxc1BZoyy1GUjNSkmh0xCqPYpki8NhqutdY1FUb2iWfVMeoEhVtCfhGis5NFoH78zkJ18wBThUZs3H7JU7RHiIHeTCLI4DalTqYY0CKY92dRJNNXdONzr0S8ojYTKjFCbOeXdulnwHG5dBMwlhuQT-bvm4yFYvSS0IK1oszG3qdtmShZSsz6rVjQ8Ky3WCk82baOztCWmbLuiHjh_Z60l1VFhjUfIW2Hfx0g7b4CvB7Zz3gpbfzvkP7mIEtCk3gUh7jpjCBPWZfj5Pi4hhNMPKFXO4GOf6y2YTYgvxs_dp5OeemaIl4RDYDXsac6MKSFnqk1LrbLtDAMyxG2hfmCDJmLQW5_Ig0u8rh4CYxuPSsNyd56kmvfIGcKRhQMNKlVdAPI2Slzkaq971kIdNfMSgpK4WTVqqoPiFM2cUBq8fQgM1JRJLEBWmLcmQSuzgjCD21qha6bHtsTnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d083252f.mp4?token=ZAgcIAjbT2YSqW_uVEhlVViG7RaNsOGMQ0j7CHKbMoYbwVQhp_iT4sRxVcMVFtE0NBQePH63r-vStgn2Q7Yjbeu8HOhXfpm6CDyFG1zsGefRuw-t2jfU5mJqSJYQ0KTZh7V7Be1mFkXGu61fqm-3ZzbAqoY09vBhA7S_enAiblTLxNy67e4ZOxTMKF1NKPpBRcvtsaKC_x0o5vBLpZjcVe6zfmUUvvxc1BZoyy1GUjNSkmh0xCqPYpki8NhqutdY1FUb2iWfVMeoEhVtCfhGis5NFoH78zkJ18wBThUZs3H7JU7RHiIHeTCLI4DalTqYY0CKY92dRJNNXdONzr0S8ojYTKjFCbOeXdulnwHG5dBMwlhuQT-bvm4yFYvSS0IK1oszG3qdtmShZSsz6rVjQ8Ky3WCk82baOztCWmbLuiHjh_Z60l1VFhjUfIW2Hfx0g7b4CvB7Zz3gpbfzvkP7mIEtCk3gUh7jpjCBPWZfj5Pi4hhNMPKFXO4GOf6y2YTYgvxs_dp5OeemaIl4RDYDXsac6MKSFnqk1LrbLtDAMyxG2hfmCDJmLQW5_Ig0u8rh4CYxuPSsNyd56kmvfIGcKRhQMNKlVdAPI2Slzkaq971kIdNfMSgpK4WTVqqoPiFM2cUBq8fQgM1JRJLEBWmLcmQSuzgjCD21qha6bHtsTnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بسته شدن اینستاگرام این‌قدر سخته؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/684829" target="_blank">📅 21:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhzI17eT2vShY7bsKQdx7Fr2amJv0sX7yfStcAGetTalOUv9FINjR8UXunZNZcmpR9SNmuJHE3w54UtoKf6gkJhPZ76jh8ZXDa8cFlIt6G_rjVR1ypd4kiQ314hiSINqIoSECeVEENSSm0ZpVS6wr0cwFt1oMWu9sOOXXzEvWJdpuOJwO9mh96Ketnls8KidFxr35KPcIZw4LmV4Uvdpc7_unFf5UOPhRxM9WbgoPe9MP0TniYnCNNloirgc9DvS-Vniqgwf4AuSzgIoS-aWBVOo--9wP2OkUZBlXh4iP7mVs5NXnk--JgJH53TgRIQmxFUR3BjN6PV-cdKyMNi5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش جدید رگولاتوری: همراه اول همچنان بیشترین سهم در شبکه موبایل را دارد
🔹
بر اساس جدیدترین گزارش فصلی سازمان تنظیم مقررات و ارتباطات رادیویی، بازار تلفن همراه ایران در بهار ۱۴۰۵، رکوردهای جدیدی را به ثبت رسانده است. تعداد کل اشتراک‌های فعال موبایل در کشور با افزایشی ۶.۲ درصدی نسبت به مدت مشابه سال قبل، به بیش از ۱۷۴ میلیون خط رسیده و برای اولین بار، ضریب نفوذ تلفن همراه از مرز ۲۰۰ درصد عبور کرده است.
🔹
همراه اول با در اختیار داشتن ۹۴ میلیون و ۷۸۸ هزار مشترک فعال، جایگاه نخست خود را حفظ کرده است. این اپراتور به تنهایی ۵۴ درصد از کل سهم بازار موبایل ایران را در اختیار دارد. پس از آن، ایرانسل با ۷۳ میلیون و ۴۰۵ هزار مشترک (سهم ۴۲ درصدی) در رتبه دوم و رایتل با ۶ میلیون و ۱۶۱ هزار مشترک (سهم ۴ درصدی) در جایگاه سوم قرار گرفته‌اند./ دیجیاتو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/684825" target="_blank">📅 21:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7DVeaxssm5RiYGPzMhsa6qRK1PANXa-J6e_ETk3FK4SjowFHUL2-PE7XAY3WutqpUo6xPBf5_HlW_OAGEY4FEaw08yGtHFwFns83XFKeMvv-nrHZIKhFXPd50J0ErGqabAIkR3jSBKMYZMLOQseTsxfkfVJvaXc1Qof0FyVY-DoGXWxwrsJ-qT459FZqeKhGmBtNcsXB3jmfqXDDkI1nzPKX8dIPqvIQpQeIGFrsacXqPYNTQQFESKhG0_4BMrPvqUs_hHB2WoSiPJAmK-9OtaoWOFDduBnaFps2_PhAXAzla1aTKpAbG4ACnHEpuwhET8vuY_ThPdE23trBkB1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گره کور ازدواج؛ وام ازدواج ۳۰۰ میلیونی و یخچال ۵۰۰ میلیونی | اقتصاد بقا؛ وقتی ازدواج به صرفه نیست | بهای سنگین تنهایی در اقتصادِ معیوب
🔹
برای بسیاری از جوانان ایرانی، «ازدواج» دیگر نه یک مرحله طبیعی از چرخه زندگی، بلکه به یک «پروژه دست‌نیافتنی» تبدیل شده است؛ پروژه‌ای که با تورم افسارگسیخته، سرپناهی که هر روز دورتر می‌شود و مخارجی که منطق اقتصادی را به چالش می‌کشند، هر روز برای بخش وسیع‌تری از جامعه به تعویق می‌افتد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3240883</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684824" target="_blank">📅 21:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe55ff39c2.mp4?token=Y-a-8IlSEubNQIe7n0fYnQ4SuhWJlS_0FVGnMvJ84stSoZ6fd8O63EUqRqf_1MrYh0uUrrk0rfCRNPzJSoIFKgRTPM5vlYKstVssKqLLGDZFfQDsmc0tc_WfRRsyIJoZJ8LvYDvVMnX_sJf3MnpQLYmdeza0pvVdBl1K2GwckalaHxHtWtt7bNMFZcrGmQaSbNcZFk73dzhTmlAEj3mfHpPZbWbwR12pcv-sidSDCzELfSwcw9i0JkhV96TGnoU-pytBUnOPSUI8fmRMEbeSXIaSilz0VRuhpoIUet7GI11ov7E0nwjAoRuLXgxZdE3GJnPxDQivTn8vQ9qGoGabow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe55ff39c2.mp4?token=Y-a-8IlSEubNQIe7n0fYnQ4SuhWJlS_0FVGnMvJ84stSoZ6fd8O63EUqRqf_1MrYh0uUrrk0rfCRNPzJSoIFKgRTPM5vlYKstVssKqLLGDZFfQDsmc0tc_WfRRsyIJoZJ8LvYDvVMnX_sJf3MnpQLYmdeza0pvVdBl1K2GwckalaHxHtWtt7bNMFZcrGmQaSbNcZFk73dzhTmlAEj3mfHpPZbWbwR12pcv-sidSDCzELfSwcw9i0JkhV96TGnoU-pytBUnOPSUI8fmRMEbeSXIaSilz0VRuhpoIUet7GI11ov7E0nwjAoRuLXgxZdE3GJnPxDQivTn8vQ9qGoGabow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684823" target="_blank">📅 21:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
کارولین لیویت، سخنگوی کاخ سفید: در حال حاضر هیچ مذاکره‌ای با ایران انجام نمی‌شود و این روند ادامه خواهد داشت تا زمانی که رئیس‌جمهوری احساس کند شاید آنها به روشی معنادار پای میز مذاکره بیایند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/684822" target="_blank">📅 21:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d0add820.mp4?token=MiajM7_NqU0fJ7mpckbx_-l5WeJuoTVc3Gf2ZN6QCiTsy0Eypj9wK9jDQUgtuCuuMBdaJmGaMObhgYl8DyBqWkvJ3w--3ujdLP6vd7oI6Q0phdCQiHMagvPfvlVavY4i3zThGfeTgKzKiWc5O51yvzTcEzRBAOsUN5YGF6ME2e3KZSInkZ4l1NgDmCivsexymfcbuXfEH7DP3GFv4rL5k30MfdTuUdqH9ShnnzsKu9WIDJuPHluAZjlfoI-I1f6w-qnybPu7Pagd95jpybnI2oJZ7CMAS9Ax4KgIHgDfoHpddVJ7wt8pAepnjdDY50YLZZRGBDgB7wBlmaLoZOtkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d0add820.mp4?token=MiajM7_NqU0fJ7mpckbx_-l5WeJuoTVc3Gf2ZN6QCiTsy0Eypj9wK9jDQUgtuCuuMBdaJmGaMObhgYl8DyBqWkvJ3w--3ujdLP6vd7oI6Q0phdCQiHMagvPfvlVavY4i3zThGfeTgKzKiWc5O51yvzTcEzRBAOsUN5YGF6ME2e3KZSInkZ4l1NgDmCivsexymfcbuXfEH7DP3GFv4rL5k30MfdTuUdqH9ShnnzsKu9WIDJuPHluAZjlfoI-I1f6w-qnybPu7Pagd95jpybnI2oJZ7CMAS9Ax4KgIHgDfoHpddVJ7wt8pAepnjdDY50YLZZRGBDgB7wBlmaLoZOtkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهید سید علی خامنه ای :
من صریحا اعلام میکنم ، کسانی که صحبت از تسلیم مقابل امریکا میکنند
خائن هستند</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/684821" target="_blank">📅 21:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعایی درباره اخراج یک مقام ایرانی از کانادا
ادعای صدای امارات:
🔹
آژانس خدمات مرزی کانادا رسماً مراحل اخراج یک مقام سابق ایرانی ساکن تورنتو را آغاز کرده است. این آژانس مدعی شده او به ایفای نقش «حیاتی» و مستقیم در کمک به تأمین مالی گروه‌های مورد حمایت تهران در خاورمیانه متهم شده است.
🔹
طبق گزارش‌های رسانه‌ای مبتنی بر اسناد رسمی، فرد مورد نظر عباس عمیدی ​​است که عنوان معاون مدیرکل وزارت صنعت، معدن و تجارت ایران داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/684819" target="_blank">📅 21:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684818">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568143ae56.mp4?token=ki4UYHfeUjRsfwHfODzfsQaq0Tj9ngUFXaW46l2qqm6Yl4hWqNQi_udX41CviglbOhSmAUsgnd_Uz6T10Q9hEyxgVBXETXvJ-mvLNcwMQtLxocOCanpU4oc51VoMridFv9_4Tnkgg4-KdoTQU9Q55qXpOkw2YeqZNVcdKZ26JDEaadXt6pY_bsnYZhXPxb4ypEWON-dPc4_0i4h-c5q46PujYnFXeKn0sJ8Fr8BYKRvw4p6irDYIFlJI2UrsMsTQZAKrBXJOCM0bc4qYr-eOb7ORUErnEo5faC1k6ZP6JdW-zqgWqYo0JIyYBkVKONkIgoIYg2ZNIeP-ncqOMmYugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568143ae56.mp4?token=ki4UYHfeUjRsfwHfODzfsQaq0Tj9ngUFXaW46l2qqm6Yl4hWqNQi_udX41CviglbOhSmAUsgnd_Uz6T10Q9hEyxgVBXETXvJ-mvLNcwMQtLxocOCanpU4oc51VoMridFv9_4Tnkgg4-KdoTQU9Q55qXpOkw2YeqZNVcdKZ26JDEaadXt6pY_bsnYZhXPxb4ypEWON-dPc4_0i4h-c5q46PujYnFXeKn0sJ8Fr8BYKRvw4p6irDYIFlJI2UrsMsTQZAKrBXJOCM0bc4qYr-eOb7ORUErnEo5faC1k6ZP6JdW-zqgWqYo0JIyYBkVKONkIgoIYg2ZNIeP-ncqOMmYugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در نپال یک پل را از جا کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/684818" target="_blank">📅 21:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
لحظاتی منتشر نشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید انقلاب
🔹
رهبر شهید انقلاب: ما فکر میکنیم که حفظ یاد شهدا، حفظ انقلاب است، حفظ کشور است. لذاست که ان‌شاءالله نمیگذاریم؛ یعنی خدای متعال نمیگذارد که فراموش بشوند. ۱۳۹۴/۱۰/۰۷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/684817" target="_blank">📅 21:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4cW7wIvBP8bnbVTtyWp1ncJ_wvf_8fgxpfl-9MpIoASxpitXDGDnmHTw0zNL3iT1FAwZbd1kx5E3tGbQwS49diSmUyv4Fzr2XSmByQfFGnvPQa9xOqWmvPcquHio6RxLrd6iRZpTzT__xF0hWeEPirrtoK5JD15LJgdJiIAbNJiJwe5Dd4EyuCmqPlj4dAlxXlXRaWs4CzLzdvfKDCN7YbUYd5xltQXklck-LE7T98hovXGRbtcrancuDR7MayYvfV_e-P60LfKJNq2MFlgAFoAUN1UcE7MiGpe0XAaa-oXC44PyHt7l7exxzofDu-aHpPf6FFOCLBW6ydT4MHf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/684815" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromطَـریقُ السُّـلُوکْ</strong></div>
<div class="tg-text">امام صادق عليه السلام : هركس در هر شب جمعه ، سوره واقعه را بخواند، خداوند ، او را دوست مى دارد و محبوب همه مردمانش مى گرداند، و هرگز در دنيا گرفتار درويشى، فقر، درماندگى و هيچ آفتى از آفات دنيا نخواهد شد و از همراهان امير مؤمنان خواهد بود. اين سوره، ويژه اميرمؤمنان است و كسى در آن ، شريكش نيست.
📚
ثواب الاعمال ، ج ۱ ، ص ۱۴۴
┄┄┅┅┅❅❁❅┅┅┅┄┄
🔺
کانال معرفتي طَریقُ السُّلُوک «کانال تخصصی یادنامه اولیاء الله و احوالات بزرگان عالم اسلام»
https://telegram.me/joinchat/BOz24TxBdq7Mz3aFRIVf7w</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/684814" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
محیط کسب‌وکار ایران سخت‌تر شد
🔹
شاخص ملی محیط کسب‌وکار در بهار ۱۴۰۵ با نمره ۶.۲۳، اندکی نامساعدتر از فصل گذشته ارزیابی شد. افزایش قیمت مواد اولیه، دشواری تأمین مالی از بانک‌ها و بی‌ثباتی سیاست‌ها و مقررات، سه چالش اصلی فعالان اقتصادی در این فصل بوده‌اند.
🔹
در این میان، قم، اصفهان و زنجان بهترین وضعیت محیط کسب‌وکار را در میان استان‌ها ثبت کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/684813" target="_blank">📅 21:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/684812" target="_blank">📅 21:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ترامپ فرمان اجرایی تغییر نام دریاچه انتاریو، دریاچه‌ای که با کانادا مشترک است، به دریاچه آمریکا را امضا کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684811" target="_blank">📅 21:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ فرمان اجرایی تغییر نام دریاچه انتاریو، دریاچه‌ای که با کانادا مشترک است، به دریاچه آمریکا را امضا کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/684810" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42020dc67.mp4?token=p4Ccm1HR_nKWzagsOx3y2_qYUDVglxZyS19jluds-3602o4BjT4MhypW732AsU_N3tUUtozmeKqxkDCO-dN5wNj8caYJ30B7OE0HvjQV7fEjs06YT90FnZ4ZQBASockdni2N1PLM8bh1PAEw68C0csNqr-XE6Ed-gFkc0aQGtMKQk0PT-zCQHFCdR5aXh0PHEiIrdjmwjy8EBbcH8uZft8l5j977NeVHxTfJIsHXz2m7ai2RPydooLuYkvUzCCvNjvH44mxiAURWl6O5H9W32v9P2PxVo9IBQR6Euuo61XCRH6ST17hg2832WgtfDw4h5k3VNJ22Uw8N_b575DCPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42020dc67.mp4?token=p4Ccm1HR_nKWzagsOx3y2_qYUDVglxZyS19jluds-3602o4BjT4MhypW732AsU_N3tUUtozmeKqxkDCO-dN5wNj8caYJ30B7OE0HvjQV7fEjs06YT90FnZ4ZQBASockdni2N1PLM8bh1PAEw68C0csNqr-XE6Ed-gFkc0aQGtMKQk0PT-zCQHFCdR5aXh0PHEiIrdjmwjy8EBbcH8uZft8l5j977NeVHxTfJIsHXz2m7ai2RPydooLuYkvUzCCvNjvH44mxiAURWl6O5H9W32v9P2PxVo9IBQR6Euuo61XCRH6ST17hg2832WgtfDw4h5k3VNJ22Uw8N_b575DCPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر دنبال هوش‌مصنوعی رایگان می‌گردی یک لیست از بهترین‌ها رو برات آماده کردیم #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684809" target="_blank">📅 21:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a61668361.mp4?token=ZGZTL73o7bHqzqitQbkAjSbadFasTMMRaVoiPvE6fX2FHlPRdrvvBkwNw4ciROPPSnlvdj3GprnpEtsUVYshVcjWT6uFbhGnwclgjt0JZ5d6m3TJitp5XhfB_09ZXsLX240jFio8lBaHzP_sUquDDxn0yplHCfD21mSt-IGyhoBeMgE2eKEjstS-HbPFWN2SEVqGFpN7S1OrDtNX-MAqshoNqXZteUDvu6GO4pCjV3VBqTjK0jWiXmk38rMlWKO3KCXXRUsCbROMu3DOUtcMwiU99OIQhhNBDgYsvefpIXXt0tIhDCa3j9g9E6L7DTA3c7LxDlZrwZJXLQrmv45dWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a61668361.mp4?token=ZGZTL73o7bHqzqitQbkAjSbadFasTMMRaVoiPvE6fX2FHlPRdrvvBkwNw4ciROPPSnlvdj3GprnpEtsUVYshVcjWT6uFbhGnwclgjt0JZ5d6m3TJitp5XhfB_09ZXsLX240jFio8lBaHzP_sUquDDxn0yplHCfD21mSt-IGyhoBeMgE2eKEjstS-HbPFWN2SEVqGFpN7S1OrDtNX-MAqshoNqXZteUDvu6GO4pCjV3VBqTjK0jWiXmk38rMlWKO3KCXXRUsCbROMu3DOUtcMwiU99OIQhhNBDgYsvefpIXXt0tIhDCa3j9g9E6L7DTA3c7LxDlZrwZJXLQrmv45dWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دنیامالی درباره شایعات فساد مالی در فدراسیون تکواندو در پاسخ به خبرفوری
🔹
وزیر ورزش و جوانان درباره اتفاقات و شایعات مطرح‌شده پیرامون فساد مالی در فدراسیون تکواندو گفت تا زمانی که احکام قطعی صادر نشده، از همکاران خود حمایت می‌کند.
🔹
دنیامالی با تأکید بر اهمیت انضباط مالی در ورزش، اظهار داشت مراجع نظارتی حق ورود و بررسی مسائل مالی را دارند و رسیدگی‌های دقیق‌تر پس از بازگشت کاروان ورزشی انجام خواهد شد.
🔹
وزیر ورزش همچنین ابراز امیدواری کرد این موضوع خللی در روند حضور تیم ملی تکواندو ایجاد نکند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684808" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sp8HcaZME0wX8af43Kl4YEKQGnO4YwFvID_gBJ9Do5JKITH_CYossIT8HqkpCTpMItGG8_IPde729d3JR-d26VdsWcWlwGwAtkdv3H9Osb8oLbJFoKnRbupladOidhs-K6w1jEKXW1-T01xbQZjfHOV3H1A3e1gqktIMYlom3ncsaWPnKF91rxG10AVPBNpBxhA1vTCleSg4f_EyfQQOzY7uhSatB6oPZgTvZrT7-veg5Ux3mp5dT4wD_HIOYtPFJ_slQyIXPWvqFhrukt8DfQZn-kMKC09J0W6a0-AYHDJyBtzjwhSml0SuP37nfCCY9fI3YcqlUyMw0HiOwcEbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرعه‌کشی لیگ قهرمانان اروپا؛ تیم‌های سید ۱
🔹
جدال پاری‌سن ژرمن با منچسترسیتی و بارسلونا، رئال مادرید و آرسنال دوباره بهم رسیدند.
🔹
قرعه سخت اتلتیکومادرید با حضور بایرن مونیخ، لیورپول و منچستریونایتد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/684806" target="_blank">📅 20:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo6rKswkdZT1EMWzYqx5X9UXq6YDdFAFs8E00NPK8QAxDxAjRK-sbs_vDU3_q5_atqOUx1-aLJ2wEql6xVl08DjYcy-wxGjDTJK72MLoQecSYcj9YiHRA4nWKObfpmyWK8oSU_QfcCM52bU60leLLsFevfjDZabWOH5L6Zprzfq6-YcBLZTvhHN67VxkC3xP-0UceBzU6pV5ddjXBv_k1zUROPZaE3M9V8Qnmu0_LmAYQtoDclRXWpjiX_78iqcQL6BCJpT7o1jBC_b4TxwMyQXKkMnoH528kguMOAdEiOf0EgaDJwS3aUUwP3t2ZvKkcRPmyqFDdKMmSvFeFAkogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین‌افرز: زمان آن رسیده که ارتش آمریکا خاورمیانه را ترک کند
فارین افرز:
🔹
دهه‌ها جنگ و درگیریِ نسنجیده، جان بسیاری را گرفته و ثروت زیادی را به خطر انداخته، در حالی که چیز زیادی به امنیت امریکا اضافه نکرده است. حضور نظامی واشنگتن به جای خدمت به منافع استراتژیک امریکا، باعث ویرانی و بی‌ثباتی شده است.
🔹
هیچ کجا این موضوع به اندازه کارزار علیه ایران آشکار نیست؛ این جنگ همان خطراتی را ایجاد کرده است که قرار بود از آنها جلوگیری کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/684805" target="_blank">📅 20:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr4kr3IXcZgE9ITFt4VDMtHoeK-ga6oh7UUt5Kg3d7dpwCJ4HP09eujclThRi2nXievCnot4jRFf4UPfrN5q29H0KdOoh7cW7gAWWfq9QwPRZDsTzHm8H3xJ4R5TswUI7ci91vMaZKyOfTVCxlp4EflnqkxA1RLAT2wu5WwDuxfJYl3Pzvbb2z1jimLcAN3dwXi9DPa0QiMB-8Op0IxB0rUMUzea85WT0fFCV5IwuGniIhSN6uKOTPn7ZxFcjMNKAKUJ31nWXFeaLI_CPxNlsVhYqT4SNoEXNMWm6Bd3rs6LKm9VgBe1S_YtenklyJsnD5Qzf8qd3ORAVr9BrYc9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قالیباف به گزافهٔ جدید وزیر خزانه‌داری آمریکا: تمام اعتبارت در معرض خطر است و امپراتوری آمریکا روبه‌زوال قرار گرفته است
قالیباف در پاسخ به گزافه‌گویی امروز اسکات بسنت با به‌اشتراک‌ گذاشتن مقاله‌ای از نیویورک‌تایمز که در آن به ناتوانی بسنت در کنترل شاخص‌های مهم اقتصادی اشاره شده، نوشت:
🔹
این امپراتوری روبه‌زوال به‌جای اینکه میلیاردها دلار را به تروریست نیابتی خود یعنی اسرائیل و ۷۵۰ پایگاه نظامی در دنیا سرازیر کند، می‌توانست آن پول را صرف مردم آمریکا کند؛ اما نه، این کار برای رژیم آمریکا زیادی منطقی است.
🔹
هی اسکات! مَرد[؟]! اعتبارت در خطر است. کاری بکن!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/684804" target="_blank">📅 20:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
یک نفتکش کویتی در تنگه هرمز هدف حمله قرار گرفت
🔹
سازمان حمل و نقل دریایی بریتانیا (UKMTO) تأیید کرد که نفتکش کویتی السلام ۲ دیروز هنگام عبور از تنگه هرمز مورد حمله قرار گرفته است.
🔹
این سازمان مدعی شد که حمله توسط نیروی دریایی سپاه انجام شده است. این کشتی متعاقباً در جزیره توکل عمان لنگر انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/684803" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99d17b82e.mp4?token=YAyDXMXjxOr3XKc3AJ0jZ_tH7hN2f5To2ooXHBjnL91UgL2HNHswwj6YRooWaN_aLi545KWP9cpjfDoPNu1QqS58A9GMAGG-rqfWkykYoPbQtPIHQyasLIulkaQhVR3SprHjnLo29DGqU9p2nfUrjxYR8-JruWb0ZTysLi4ceI3OV6l2FyTAT1AasWsYryy1ffhRKVzwYhOXRTQt_b8kxNRP_ovaqwYYvXH_dvyIS-CH2B7-AVrKtU8b94JUWYgKDcdo17vMMC5fEVWWHnwTUeHqB0kcQkWPPWu38Xy6Fw9-gnLYhViCjLxCWIkHJPLWZLL_SAFDygRvI2hZ515VJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99d17b82e.mp4?token=YAyDXMXjxOr3XKc3AJ0jZ_tH7hN2f5To2ooXHBjnL91UgL2HNHswwj6YRooWaN_aLi545KWP9cpjfDoPNu1QqS58A9GMAGG-rqfWkykYoPbQtPIHQyasLIulkaQhVR3SprHjnLo29DGqU9p2nfUrjxYR8-JruWb0ZTysLi4ceI3OV6l2FyTAT1AasWsYryy1ffhRKVzwYhOXRTQt_b8kxNRP_ovaqwYYvXH_dvyIS-CH2B7-AVrKtU8b94JUWYgKDcdo17vMMC5fEVWWHnwTUeHqB0kcQkWPPWu38Xy6Fw9-gnLYhViCjLxCWIkHJPLWZLL_SAFDygRvI2hZ515VJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح ضد پهپاد جدید اوکراین برای مقابله با کوادهای FPV
🔹
این گجت جیبی یک پرتابگر تور است که تا ۲۵ متر برد دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684802" target="_blank">📅 20:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حمله تروریستی به خودروی مرزبانی در محور مواصلاتی میرجاوه - زاهدان
پلیس سیستان و بلوچستان:
🔹
در پی اقدام بزدلانه و تروریستی اشرار مسلح به خودروی گشت مرزبانی در محور مواصلاتی میرجاوه به زاهدان، یکی از مرزبانان جان‌برکف، به‌نام استواردوم «علی حیدری» به درجه رفیع شهادت نائل آمد و یکی دیگر از همرزمان وی مجروح شد که بلافاصله توسط عوامل امدادی به مراکز درمانی منتقل و تحت مداوا قرار گرفت.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/684801" target="_blank">📅 20:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وب‌سایت عبری‌زبان «واللا» به نقل از یک منبع امنیتی گزارش داد که اسرائیل رسمیت شکست طرح خود برای ایجاد مناطق آزمایشی در جنوب لبنان را پذیرفته است
🔹
اسرائیل از طریق کانال‌های امنیتی به آمریکا اعلام کرد که طرح ایجاد «مناطق آزمایشی» در جنوب لبنان با شکست مواجه شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/684800" target="_blank">📅 20:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b193111727.mp4?token=vtT-lQ9Zbbtad2y4xADcNrOcxgDK9zDOm3Zvj8_LlwWcMfELBnFw9u0UvhzH8qKHr_HL8UY5jEVhnR74G4N4Qo58EbGPZEj3ZDb6Uu_w8EhnR5xkwvEedOUGHc4EF2LeaSjFh40SGst0mBlC7fnZPcgLgz_-J4Zh006gElAk5SrqQD4saxGxjkfkOKJsVWmhMp07y9Xc5qnjuqm2mnQh8osY7epeIdjDzGZT5Hz96OGeGUZ94iJCT4p-oMJDwJd2K1zGhT5qLAUXGgYGzzRFAWkdbqvzs4HWL8HaNrAQJWXDMcNBvhjc2801y9lpXuB-VQR7Ug8vRQ7piezjQ1WqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b193111727.mp4?token=vtT-lQ9Zbbtad2y4xADcNrOcxgDK9zDOm3Zvj8_LlwWcMfELBnFw9u0UvhzH8qKHr_HL8UY5jEVhnR74G4N4Qo58EbGPZEj3ZDb6Uu_w8EhnR5xkwvEedOUGHc4EF2LeaSjFh40SGst0mBlC7fnZPcgLgz_-J4Zh006gElAk5SrqQD4saxGxjkfkOKJsVWmhMp07y9Xc5qnjuqm2mnQh8osY7epeIdjDzGZT5Hz96OGeGUZ94iJCT4p-oMJDwJd2K1zGhT5qLAUXGgYGzzRFAWkdbqvzs4HWL8HaNrAQJWXDMcNBvhjc2801y9lpXuB-VQR7Ug8vRQ7piezjQ1WqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشنواره تخفیف‌های ۷۰ درصدی برج میلاد را از دست ندهید
🔹
از ۳ تا ۱۳ شهریور همزمان با ولادت رسول اکرم (ص) و امام صادق (ع) و آغاز هفته دولت
بلیت های بازدید از طبقات برج میلاد: ۷۰ درصد
مجموعه فرهنگی و صنایع دستی هفتا: ۱۰ درصد
زیپ لاین: ۵۰ درصد
کارواش: ۲۵ درصد
سینما گیم: ۵۰ درصد
سرزمین افسانه: ۵۰ درصد
شهربازی (چرخ و فلک، ترن و کشتی): ۵۰ درصد
کاربازیا:۲۰ درصد
رستوران ها و کافه ها: ۲۰ تا ۳۰ درصد
بازی‌های هیجانی : ۳۰ درصد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684799" target="_blank">📅 20:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684798">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
هشدار جمعیتی؛ تا دو دهه آینده ۳۰ درصد جمعیت کشور سالمند می‌شود
🔹
در ۶۰ سال گذشته، جمعیت سالمندان ایران تقریباً دو برابر سریع‌تر از رشد کل جمعیت کشور افزایش یافته است؛ روندی نگران‌کننده که زنگ خطر آینده جمعیتی ایران را به صدا درآورده است.
🔹
پیش‌بینی‌ها نشان می‌دهد تا سال ۱۴۳۰، شمار سالمندان کشور به حدود ۲۸ میلیون نفر، معادل ۳۰ درصد جمعیت ایران خواهد رسید؛ یعنی از هر سه ایرانی، یک نفر سالمند خواهد بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/684798" target="_blank">📅 20:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684797">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
صدای انفجار در اربیل عراق
🔹
منابع عراقی از حملات پهپادی به مواضع گروهک های تجزیه‌طلب در منطقه سوران در اربیل خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684797" target="_blank">📅 20:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06 Ane Manaee (1403-08-17) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684796" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه ششم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن [8:33]
🔹
در جستجوی قواعد غیب؛ تدبر در آیات قرآن چگونه ساختار هستی و انسان را آشکار می‌کند؟ [12:53]
🔹
اعتباریات و اراده؛ پرده‌برداری از بایدهای پنهان در رفتارهای ساده [24:28]
🔹
ضرورت و کنش؛ چرا هر اقدامی ریشه در ضرورتی ذهنی دارد؟ [31:23]
🔹
دینِ بی‌دینان؛ همه باوری دارند، حتی آنان که دین را نفی می‌کنند [34:10]
🔹
زیارت یا سیاحت؟ وقتی نیتِ دوگانه، خلوص عمل را مخدوش می‌کند [42:40]
🔹
خدای ناپیدا، خدای واقعی؛ آنچه به تو انگیزه حرکت می‌دهد، خدای حقیقی توست [44:03]
🔹
داستان حیرت‌انگیز کاظم؛ از شکنجه حاج آقا ابوترابی تا شهادت در حرم حضرت زینب (سلام‌الله‌علیها) [57:51]
🔹
آن‌ هنگام که کنیزان یزید ملعون در پرده بودند اما حرم رسول‌الله در میان خارهای نگاه‌ حرامیان [1:09:06]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684796" target="_blank">📅 20:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684795">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: آمریکا شرارت کند بلایی سرشان می‌آوریم که در تاریخ ثبت شود
دبیر شورای عالی امنیت ملی در دیدار با وزیر امور خارجه دولت قطر:
🔹
ایران به قطر در روزها و شرایط سخت کمک کرده است و بر دوستی و برادری بین ۲ کشور تاکید دارد.
🔹
ما به آمریکا بی‌اعتمادیم و آن‌ها بارها به دیپلماسی و مذاکره خیانت کرده‌اند.
🔹
آمریکا باید ابتدا اقدامات عملی در جهت انجام شروط ایران انجام دهد و پس از آن ایران اقدام به بازگشایی تنگه هرمز خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/684795" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684794">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9cc60ceb.mp4?token=uQBwS8DbEYcZvs74wCPK4YlEYWHmcuup2AMuFdCdi6QOydVU806jV_7gkKvlxOG9JG8AAWkCjn8qTWaqlbr7ZDoMbVgdgzOLj0riEg9xyvTFYT2iXWG8Jmb2IZ4A9YgPdICm2oc3ZGXsgWP5OfEb_kAySWWCEQAfpSd92mckI6OyjnlS6xPh5YUwLa3c7j89dJw4ZGmNDqRfu50ADNPZTfxtyxdVAnqGtybudfAUmYCtwEQ0tQJxL-GnCzupL7UNzArReur3Q7CHxh1I7wJT_Xqpz51wcSTDMVmSpnoDlU_aiXoFRhm7quaEq3rq2i09favVDd2tPWssXMxcjeuBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9cc60ceb.mp4?token=uQBwS8DbEYcZvs74wCPK4YlEYWHmcuup2AMuFdCdi6QOydVU806jV_7gkKvlxOG9JG8AAWkCjn8qTWaqlbr7ZDoMbVgdgzOLj0riEg9xyvTFYT2iXWG8Jmb2IZ4A9YgPdICm2oc3ZGXsgWP5OfEb_kAySWWCEQAfpSd92mckI6OyjnlS6xPh5YUwLa3c7j89dJw4ZGmNDqRfu50ADNPZTfxtyxdVAnqGtybudfAUmYCtwEQ0tQJxL-GnCzupL7UNzArReur3Q7CHxh1I7wJT_Xqpz51wcSTDMVmSpnoDlU_aiXoFRhm7quaEq3rq2i09favVDd2tPWssXMxcjeuBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند ترفند ساده، بوی بد کفش‌هاتو سریع از بین ببر!
👟
✨
#ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684794" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684793">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPKfVEqXkIPpmj6LT3e6tYDIJuyeYj7aBl9QLFgfYM6zCo3FzkWUknDvbJ7xOiC5TUAM9OlGyDAKcluerAYSR9GiHKZDf3C6xopuddKWylmpVee1WT9x3TOvmvtSklmur4hzqsgdioeEhuqDs9NaQ2Hp5nmFTf976-yqjumYbm6M0KHMFrTf0h-U7oNCiqAMEw_y6YMB6UxRuDacbD5xRmZQgIqQh6Fue6ahHn7WIl_7vQ9y8aStnu71sCta9SPzl0Up1CDFenE8tvBUZOWTQc5REQ1UwCVene9UlXt_jf-FLVJeBwRCXgquDOCIkKylmsVp2ahEtvx4NE_5fDwpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تازه‌ترین قسمت از کمدیِ اپوزیسیون | چهل سال جنگ قدرت در توهم | از بنی‌صدر و رجوی تا پهلوی و کریمی؛ تاریخچه دعواهای بی‌پایان اپوزیسیون
🔹
تاریخ چهار دهه‌ گذشته‌ اپوزیسیون خارج‌نشین ایران، بیش از آنکه روایتی از یک مبارزه‌ سیاسی مستمر باشد، به یک کمدی ـ تراژدی مبتذل و کشدار شبیه است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3240777</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/684793" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684792">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44675bacc.mp4?token=vtTFwUOxg7NS43nH5XbR-n_TlWvwUQgl6dnXhNgh1EHRscq0Y9n27sy-mW_jI38WuiaeLjE0f8YtyWnDwp-UFZq8-mOYB7eVMan_RP3uV0wOSoEJvJjvHwYUdkTz-FIfWXQ2SG135h32W5_KyH6IBIdIoxxj18_YDFS8-4P5zIvgNUkcNRi89atu7zmjPFZUY63g_T3bFRPBC1fGqXcqTfjeWr1lefj7QYCbJOZ90II0U0vDpffL86vzcidRLbyreF6d2QXmBDdivKjCocHjHOKUJlHDsBnvQTkss11dtotkAV9ewSg38KR1H76O7ijuRq2fT-RWNYlaBMkZ4VyEaZGV0-mVIvZR8coG-sHznEDAqIYwebFuDsMalvTI21pZ15iim4_baihLYN10Vnj41Nsyui8wnIELOLMeRqyuIX2OumxVanNLo2Cml3mCbxS3E-mVsAOqQu7BYnFNf6_9-9bFe9WAGhXZ02gkth88hAb-8PHOe8dAgbcqtFsSp45KDjfiO7Gm_QWJGJ0ynwP6jkut3GcBPuTOEKoLZywnVQ1FWspERrwXsBoKgE7bJTvexNyGaKydAXD2vKfTmQg2dtBW-6bWS0BhD_fZpCOFQmIhFgPWfiZ9WQhZhWZ_Nor4BmTUIx9czLfu0U1yMsEexITd1mapCWwXlWlMrdYzMvo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44675bacc.mp4?token=vtTFwUOxg7NS43nH5XbR-n_TlWvwUQgl6dnXhNgh1EHRscq0Y9n27sy-mW_jI38WuiaeLjE0f8YtyWnDwp-UFZq8-mOYB7eVMan_RP3uV0wOSoEJvJjvHwYUdkTz-FIfWXQ2SG135h32W5_KyH6IBIdIoxxj18_YDFS8-4P5zIvgNUkcNRi89atu7zmjPFZUY63g_T3bFRPBC1fGqXcqTfjeWr1lefj7QYCbJOZ90II0U0vDpffL86vzcidRLbyreF6d2QXmBDdivKjCocHjHOKUJlHDsBnvQTkss11dtotkAV9ewSg38KR1H76O7ijuRq2fT-RWNYlaBMkZ4VyEaZGV0-mVIvZR8coG-sHznEDAqIYwebFuDsMalvTI21pZ15iim4_baihLYN10Vnj41Nsyui8wnIELOLMeRqyuIX2OumxVanNLo2Cml3mCbxS3E-mVsAOqQu7BYnFNf6_9-9bFe9WAGhXZ02gkth88hAb-8PHOe8dAgbcqtFsSp45KDjfiO7Gm_QWJGJ0ynwP6jkut3GcBPuTOEKoLZywnVQ1FWspERrwXsBoKgE7bJTvexNyGaKydAXD2vKfTmQg2dtBW-6bWS0BhD_fZpCOFQmIhFgPWfiZ9WQhZhWZ_Nor4BmTUIx9czLfu0U1yMsEexITd1mapCWwXlWlMrdYzMvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غلتیدن غول‌های سنگی در سیلاب مرگبار نپال
🔹
سی ان ان به نقل از منابع محلی اعلام کرد که تعداد قربانیان سیل ویرانگر در مرز نپال و چین به بیش از ۱۶۰ نفر افزایش پیدا کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/684792" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684791">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سخنگوی ارتش: قطر از سرنوشت خلبانان سوخو اظهار بی‌اطلاعی کرده است  سخنگوی ارتش:
🔹
پیگیری‌ها از طریق وزارت خارجه، ریاست‌جمهوری و دولت و ارتش قطر انجام شده، اما طرف قطری تاکنون از سرنوشت خلبانان اظهار بی‌اطلاعی کرده است.
🔹
وی خواستار پیگیری جدی‌تر و ارائه پاسخ…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/684791" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSNMeXMhNtP8rMjeUs9gxIwJxyJZxTgUiiv4Yl-OHBf26i_yTXemzagl-psd25K8si4cwipSreLMyYm5Uly0wg_HVjvwfgf-JpsxNlxAcNadfz-hdvaa7-_CzMavN_8-QtfMU9wFpDdeerLKyhFWlX3gzUhiy3qVF9PFOzwpxkSE87BN3Y9GlqaGLoFBzBshNIsbnBx9OOPSN3B4yZzIjM_dgStXV05X3GI8IzXFtICGrPWkvuH4HTpX2O2LWOwooixs5uRmsvUja7s6kph4duXENeFqdlS23jtUtOTXdXXatNrITkaYPFF1xzrbiUxwcgxEVte94CkV4ncdfDMslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7J9IqWp_hgyC5oC13JOiELmq9jihEf0yzgjJfB-w8oXLStPn6k-muR8V2sLWcirPlKP4jB6_ejgflcqsaby1bQ84v8iyaPomevcmYu0aQgV7ynb4CRqyL3lx1cQxiE8BgQ9exsUWoBOJUcqxJDFdtSfQ7vvETcm1JCTt6XNrTRr3drvY4Inz5SVxjJcfIIUtYkBO5U9VdyNpUyQkfgHAvd1TLpYxOdlMaSIR2Gt6R0_gvaw4ATT2wIw678uWwGztoaykMlWzK0RBpM5BCHPpnr86pLjhLs3zzxA7gDjggMM1XHUiHSWx3jyqACJeazVJDfqVGGUERDgTp3OlOKTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWJMqV2-zNggLno46PU6GuIBfhkfr138pPvI45badTLoTCAW1-8LwRpNbI90HeS7XTgvInXBJhxfsSA30H4-dfnZ89PqfL_pYIei2hqj5dHI8s53sS8rqHme7qACOG6qjirTDM2VAZKXUqM2g17Az0L72CDc3bcJrw5phI8ZHY2xfp4HpLF42yceH6ObBGn0Sc9dznJ0O3ZnqnXBXnLQYjEiLPZAvdmsLOshW-vKj3zawkp4UxqYTEK6umQR2CFgpj4AVFqU-D1Ey3zzXc00jAHuxxL1ndJSoXgYf2euucyGardgapDWZwoNM1pZXpb0Jf8QUD6WVInEQ5TiM07_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRwK1iPZhPumN2ywARxVlOUcBjZVTgCqrvWoHzlsqFWwPmRGvgXVfUJsUT2Ol8nAcj4vziMGUfS7A2AwNymMzRhrH8r--o9FChNtFD0YJZzPt2iz5i3q39EbG4KjxSQmGYdyor9TfKqQtVXi8OOcSuR4qh7BRfT79VYmz7xySdrv5WGKPnh_F8PUBtbkKvyiUNlJbDHYnd7h_gtabs4nYvBck7EuGuCboqImT7t_BNW6FRmPpREIIQEvIQMbLBi4ogLRVYyehxRaIGIVpPH4erANTZkBgcSeXXNdtGM39kUW9677i8-xv-VvTYAnhYukUOmLdmf-b9BLoyENVcqJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlRFAf0d5wBC6iu6Y3SsMYu-MjcYCLoCCm78ORFdq9DzMKwKpcLVcnaWb_Ehfvogz8z7eUJwnBvLLuQWgN07xZiOGyQjPaVreqxbXsRjmpSR9iZpPodym-utLNwFrMm8dc6bnGBl60CAGqVd86RSUbYCClQ9Fy8dztFF4y56nmTUS_hXefPz8ois6cuSVFcpWI8kuUAPNDFAKLa4ex1VrudbMYjPe75bbmS29vYdqPq-bWkHm0XSPP8ryqa6pv632-HKDX_HF44CSsULKxW7UwGGSCmP1jJ1rtApEmNvJd1mappG3gfNEP5KBOhPOnTA2ilaKsIiUBZ4PfapwJG_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7MnyTHt8ExWJo2mbdowb0sGzZvivwQljQKls0ZvdggIo-j5eZsQ8WJcMEzJOXKm1GnnUyIpv1d0Mke0IwvOB22zIA1dZT7XvW8CU8MdpvBihqWjAkFPqk7Ql6VvVl_aCSYoBqMjbaSFUhYO4UKpayrFQQMnDCsSA5I7eSHPJ45WicWnDHnneoa4RzNaS-4VxSbztqzUXsLK4U6kPOj6PSYKuDS1iqQEBUVAgrr9DmBrAYLXdEtPt8YzYglWU-5PHF9FDvVcBxR05JvLwgPjHNxikGlZs8kGgNOGGqX_Nu5fGaFVlEURvO7akg0RHI6mGWVXKFgG3uY7_hYnqkpz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZq0jCUIZt8uvJDaYFunTNqgyNTokLuB3n0v2hIk3XWupoAHXzgwTxV1cqwf6rXdsnUuuCGfd-HG7dSdqJPXQT1lefc9epN2isS8TKmeiMKSQ4feUdh3xmsOIGnu6h5JWB6-snqlCtYssOoJMa3IJn2hD5JO7gDupnC1CX9jD-ftaBVsw4V7TYp6zij04wu8DmlAc55EHKcRfymXL8821jnBpANtu3h1FTjPCJ2qcRXsAxPHjr8M31lCHHmcvuj7Lkhl8-rt5Hpo6WLePPfWfeqm70bRrY8Dj70laPevX6uJoNgMIZMIWdXUIyd4d4eFvovGTpSuNIdUpP4WA7ZbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBcpM317nB6NmdqEW2xR-eYi8_1qTZdcTFAow8EGzoZ90E-g8t7EwyVB_zHu9FhAP81HcCVzAAAtzBLrZ_6iFeY5-tVW40cpt0xScqFa367g8lW_RCRObmd9xntaybaNkFu07JKGdecuFtOBURM1XtD-TbgXYjCjdIkMVbQ-UEI6HRMeUliyLIGJwwffBGWeDN56lPOIeNynKqB0TbgBhB2R5Wl7LSXFYPFGukrPN_BGFjI7MbV93UBoijtFagyk3TLWoB9NOglzV0of8Ll7uY9s7mu13R3KyqT4_50haOAIule831XfuzlCTHUOl9BmasBscP91yTAnUMz32In3hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ حضور
💫
✨
برکتِ هر نذر، به حضور دل‌هایی‌ست که بی‌منت کنار هم می‌ایستند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم برخوردار این همراهی را معنا می‌بخشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/684783" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
هشدار بیل‌ گیتس: هوش مصنوعی خطرناک‌تر از آن چیزی است که غول‌های فناوری اعتراف می‌کنند
🔹
از خطر بیکاری گسترده تا بیوتروریسم؛ از رهبران جهان می‌خواهم بیشتر به موضوع هوش مصنوعی فکر کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/684782" target="_blank">📅 19:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3ZiI3TGyLtML2Aft6-R98ifxrP76WLcMczqvu-Xp0bPoIOIK1269FAuTRY6at6I-Fb2M_o50lhVuefkgWALuc7XPyJpsBYbAbwEyyR6bMF0kmTRKe1-luMfG7P_MqvqanbrQR4lE2U5tWMboKiQxvFHiHNrltrnsEENeXHgIgOwqtJjubDh5WWjPDv5IbcHL5Myc8O4k3Zg08BlHAUfQGgYW-Jg2tsr2_NNFeGphuqzUx2kqFcmxudZlq3B51AbR2dikXdWmMyHofLcekn5pLjaoxjiwHcXtXPMZAPEJEazhNgWaj__aeq3BjXwMTh7KlGekCc1kMmUQwRqRpZHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار ابن‌الرضا سرپرست وزارت دفاع: معادلات قدرت منطقه را تغییر دادیم؛ با احترام با ملت ایران سخن بگویید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/684781" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف در دیدار با وزیر خارجهٔ قطر: ترامپ با محاسبات غلطش ناامنی دامنه‌دار در منطقه ایجاد کرده
🔹
ادعای سنتکام: از زمان تقویت محاصره بنادر ایران ۷۵ کشتی را به مسیرهای دیگر هدایت کردیم.
🔹
روسیه: ۱۰۰ میلیون دلار بسته حمایتی برای تقویت اقتصاد و ثبات سوریه اختصاص دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/684780" target="_blank">📅 19:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
پزشکیان در دیدار با وزیر خارجه قطر: ایران چیزی فراتر از حقوق قانونی خود مطالبه نمی‌کند و در برابر زورگویی تسلیم نخواهد شد
🔹
تمام حقوق قانونی ملت ایران باید به رسمیت شناخته شود.
🔹
جمهوری اسلامی ایران چیزی فراتر از حقوق قانونی خود مطالبه نمی‌کند و در برابر فشار و زورگویی تسلیم نخواهد شد.
🔹
ایران و قطر می‌توانند با عبور از حوادث تلخ، همکاری‌های خود را از سر بگیرند
🔹
نخست‌وزیر قطر: زبان زور و تهدید راهکار نیست؛ دیپلماسی باید به منطقه بازگردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/684779" target="_blank">📅 19:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01e91473d.mp4?token=MHdXdX_mH5tgH4BDhlQlqLSErl9J4SrZz2vDOIpZvqWU6RGA0Xs3zhTMZ7JhaYEJakOMzOagYhXg6Yt9Ms6epI8vOq8ZTlyWYjHwOF3iVDMNnId8m2xdpehAxCj0UeQyl703tZXom-0W6NpIzxabRTKz_oJDhehO9e5ZTXueU45-MElEUoJ_2wYJ3MBCxUfGPa1PS7IVCh8AumodEvBNB6_SyXDY8G1L9Hpm8vw_wHdFqgXIHOKnt5cSwB3cezgf0mlEy7olfqnrmZQZyIX0obtWLJ-D02xhrYHtsn-59czJ24WFAP42bG1LO2gotzdT6AnP2RatYefq_p4T084DFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01e91473d.mp4?token=MHdXdX_mH5tgH4BDhlQlqLSErl9J4SrZz2vDOIpZvqWU6RGA0Xs3zhTMZ7JhaYEJakOMzOagYhXg6Yt9Ms6epI8vOq8ZTlyWYjHwOF3iVDMNnId8m2xdpehAxCj0UeQyl703tZXom-0W6NpIzxabRTKz_oJDhehO9e5ZTXueU45-MElEUoJ_2wYJ3MBCxUfGPa1PS7IVCh8AumodEvBNB6_SyXDY8G1L9Hpm8vw_wHdFqgXIHOKnt5cSwB3cezgf0mlEy7olfqnrmZQZyIX0obtWLJ-D02xhrYHtsn-59czJ24WFAP42bG1LO2gotzdT6AnP2RatYefq_p4T084DFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مینی‌برگرهای جذاب؛ یک ایده خوشمزه برای شروع یک کسب‌وکار کوچک
🔹
در #چرخ_زندگی سراغ ایده‌هایی می‌رویم که با سرمایه اولیه قابل‌مدیریت می‌توانند به یک کسب‌وکار خانگی یا کوچک تبدیل شوند.
🔹
این بار نوبت به مینی‌برگرهای خوشمزه و پرطرفدار رسیده؛ محصولی که می‌توان…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684778" target="_blank">📅 19:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از جلب اعتماد تا غیب شدن ۳۰ سکه؛ شگرد کثیف متهم سابقه‌دار برای سرقت طلا و اقلام با ارزش
🔹
پلیس آگاهی موفق به بازداشت کلاهبردار سابقه‌داری شد که با پرستیژ خریدار طلا به سراغ فروشندگان می‌رفت و با جلب کامل اعتماد آن‌ها، در فرصتی مناسب طلاها و اموال باارزش‌شان را به سرقت می‌برد.
🔹
طبق گزارش‌ها پرونده برای شناسایی سایر مالباختگان احتمالی همچنان باز است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684777" target="_blank">📅 19:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🏡متراژ مسكن🏡</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH53eIgLWPLSQRrhG9MuaN1O5_Lia8ru9EmGm8ucC-8nF6Alp6uuM3AndJiKnmIqmOKIcTPp1bQoDzvvfbE9pVj8uKKsnFfrjoztms5c0NuwW7cWLcR1Eys_NNSqVIX6V__8lbWQSynTnyKunKQMaFAg9CO639GjCORafF_gQZaERS-Txp0_XLh1cjL_yPj7xcw-xvhWl2te0zqo3t3OWBnkpuzhRHHaHq67h5uJ8ijhyW6LZ9wYRjhrnFz0c2SmP_sVX7e9_KW4UgfOuhlSLkR4XQMokSmFVWJB9EcxmHEc2NIjBFKJGfmFsKgQkktiwCvpWIlt4nQHN7wSgwSsKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد ۱۶۰، آهودشت، ویلا تریبلکس زیرقیمت، ۳۷۰ متر زمین
۲۶۰ متر بنا،۳خواب مستر، استخر چهار فصل
( پروانه ساخت و..)
انشعابات ۳کنتور اختصاصی، روف گاردن، آلاچیق، شهرکی با نگهبانی ۲۴ ساعته
قیمت : قیمت کارشناسی۲۸م
قیمت الان۱۸/۵
#تهاتر
با ماشین انجام پذیر است
قیمت ویلا ها از ۴ میلیارد  با اقساط بدون بهره و زمین اقساط بلند مدت بدون بهره
https://t.me/Metrazh_maskan
خانم شایگان : 09194879515
خانم مطلق : 09199661658
https://www.instagram.com/vilamaskan_?igsh=MXM1cm1ycDU0cmNuZg%3D%3D&utm_source=qr
ادرس سایت :
http://www.metrazhvila.ir</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/684776" target="_blank">📅 19:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gyy7pZQ1Ag6Cm3c6VZDnacj7H_aSaFOHbH0potGOWEuzfQRNyAoNIdmQcrsHQc_AHIWRh_qPBgbPfQAhkKftTo9_gooUqvaetFUNqgmDmoRzVlwML0jJf7D2fmWNjRrC0Zwp9r0uQbSclRCfOH6vzeQ-FSgZA9JSV6iD1wWhH6P4M9qoHiMavIhGmO8bFUDxe1009IK-6WkjnRduW5uAXB8gD60RYlB6eT2RtXWHGZXAnHlOS8A36TfG0GY-qi9waih93F_pgCd2ms1VKbpJQKDyrt2w1VeoiNQ7mISMTwKjLkgDGaxfgiW5P4CYg6ODVkg2nP7DglhiOFirjQ2RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت تمکن مالی با خرید ETF طلای «رز ترنج»
🟢
یکی از مزایای جانبی خرید صندوق طلای «رز ترنج»، امکان دریافت گواهی تمکن‌مالی از شرکت سپرده‌گذاری مرکزی اوراق بهادار است.
🟢
با خرید صندوق طلای «رز ترنج» هم ارزش پولتان را حفظ می‌کنید و هم می‌توانید تمکن مالی با اعتبار بالا و به زبان انگلیسی دریافت کنید.
▫️
خرید رز ترنج از ساعت ۱۲:۰۰ تا ۱۸:۰۰ و با جست‌وجوی نماد «رز ترنج» در تمام کارگزاری‌ها امکان‌پذیر است.
🖥
برای آشنایی با نحوه دریافت تمکن مالی اینجا کلیک کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/684774" target="_blank">📅 19:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684773">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATlpw8Ue4MLLDx98HDSXaCY8tcm9PAf_ZVbgUig0_1rn1GVLrW9KCyt52YaOTI0pywRCVusCFlIWaMDUQZo1y-z3KAdn5RyYfD4ZqExaiLBC6k-SeoP8A6IUTMSwsPcqM9m1ND4kK91viSGE4uV8ac2zr9u8I2Dz-iklO0U__ZOB98jWazL44bELfVxpqLFqBs0VfMQT2UMBDtW97n4qEHsNwly-qG94wwBrSY2CSc6lQ-A6vc34lKtvvyAMuxPaHNqF1wHx-RnLfAE5pKuMcbujuPzVG3Q7JMFczFqI78f8_QTGgK0mjruBJYumKuYlqRSLnpEFhcvkE4slxj7jGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای دعوای علی کریمی و رضا پهلوی چیست؟ + تصاویر همه استوری‌ها
🔹
استوری‌های «علی کریمی » و درگیری او با تیم «رضا پهلوی» طی ساعات اخیر در فضای مجازی خبرساز شده است.  بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3240618</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/684773" target="_blank">📅 18:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684772">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بلومبرگ: آمریکا به‌دنبال احیای دادگاه دوران جنگ داخلی برای توقیف نفت ایران
ادعای بلومبرگ:
🔹
وزارت دادگستری آمریکا در حال احیای دادگاه‌های دریایی موسوم به «Prize Courts» است تا در صورت توقیف نفتکش‌های ایرانی، امکان مصادره محموله‌ها و انتقال درآمد حاصل از فروش آنها به خزانه آمریکا فراهم شود.
🔹
این طرح هنوز نهایی نشده و با چالش‌های حقوقی مواجه خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/684772" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684767">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM96Zmv68WElPWdeHkIFuZhP_PaCje2INCUZnoAVN8K_4cn46VOjv957_MhVhT7OV3kKVD-b1-sR2ilOX-WFbjnAk2tEhZ0-tsyiTmfEuucZN5uU3c8ctAqaA6vDheZhBiDdiWT_nwjkWmy45aZzOmQvijeo5rA9Z_rj1T96X50ZiMuNt54RjhOt055NXVPIk4Qy6Q471hLJNc4LXWy_ajebcjwTaiiV59Lxo4_wzIHIhYA8Lfe_W0qqZRYF4elL7ZMc-4zXXvmxvfztGE1oFGHgt_nQ_636-1U5V2o2cgl1BfSrnaJXculvah2c9mI_Rjngl3WeC7ME0IK2Gy3Qlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJFb3V7Km1uhpFMvO5N4oLYj8_F9nT55kruO3vGVEOBEpTuBXjKmo07ueU8psLkWFSpA68HdmWFDUMbznqmrbaTfKIP_7yOlfCD7CFt4kwIL_gAorVjHlIcTtUP8xjENMAqwPUaidvKtxE2RbnyzrosD02q_EWTatHYdWsklEnr3e2vkSDUjQr1ED6WPtI_13adtqL8BIUZ3pQWfqeJy2odEHr7yQfC2uEwHzOvt0LaQt2A7Qoid6W1pQxWwvDSqZQMH9_885Mzy482p2dKiLKYOogbV9VPj6VYxdYFPsxH5bpZxxBP58zHU9ZTLxe6kvAsuXBCkkbqZb5gVrzPnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSbLJ19l8jxt55uB3FfKRXZscAvLXuD238ZjUqqCVdSxMvBB0CAMt9VsMRDqs4OuHCM6-PKw1h9HsmBP9xaaAwy6KNM24sybEu16cxcauHn1R60NgnKQf0n8GSMmlDxpEgl_NKUhiq0q3spQFvGjk9eMhvfebOYjxOwNkQb8cVXVGziSm9MIhq17uo5cSYtcN4cHekySaLaxheQZwEdb2-5_WdpHXQVuFvet7_oMRv_uQXpf-jcW2q9sTC33a6vc_E7-DlRb27QLTUO3Jcuji6WztFBcyDIKYUW01ab0sppHCSy27BlJFE5EuFkP1RoI1uwe4zA8z3Af4gFr2Ci1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxuNb3vaIDH3l_tW8QLJn-tHY3njpIWBCV0CxsUMhdVxuqBvOmiwpPBbgP4PCmOjkSPHdsimXptym-B-UGN3StGv1aoaHQPl_levRiA0iNIghYWp4T9rDew4hgdllc6eBMDJH0DWApUYIDYkzJM0bv9zLny-__EFxjpGD4Ci2Na2icDWBBw4B92UhF7OZPVANYRJhbAxBeDa2maD-3Ca3vwR6-tsMSrpin68sjAnqwvWgyWep2vJaAO_66PViYecS1s2SmGwhTrcTyhqDxfxwM-isLyEM3WHnT728aScqK0sHfqeCSNKxoybOOIyvmp9wWCAfoKwVjZYGlTnqGSuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_BJXt3lhNnRwXGKCZblJI-b-xIFmXCcE-NKQux49lx22Kl50Wed2O4dfMu-FuoYO4zQaChyABCtrNK6tLvIEfvP4lr7rnaOjHc5dEr-z4aLx5U1PA3oFu5hnkaKmehK4UE4cZYfstC3GVNxwlYGs98x7a0HZZabh24cIKJ1djGwHGU_6wHjhxLpiAoWs4QpJDUqsn6o9dWuBBECDX0DL9DUj9bO4TA3OxE5VxLCVUXkSKS0xEARXsCZdojm7kF2bCqZ8u-3lik7zamXnjhgP5lrM8q-OmHKffADDFtUHPbwcPUup0LSNOfx6ao_hBRkwGzhH8Ro9vpwF4ZlOvBxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیانیه سازمان اطلاعات سپاه در خصوص ترسیم صحنه سرنوشت ساز مبارزه با دشمن شرور خطاب به ملت شریف ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/684767" target="_blank">📅 18:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684766">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf0ec4e373.mp4?token=hR6nLv--esW3sBSBvd4wgsk6-yJzHOcxlE0QH3ihnen--x_GZwpS8d0ZQMRa8COqpMKguNe4MsT2En9qe-fIy_HqzRSZGVEs7E9SlIzDHn7VqW3_bxTnJl0a6KLaEpqafpATeNYNJmI5LYtypejxqBADWB8UOGOo-IbEITK_wvYc88wO-Zfq8vfhqeK_Z3f280YUIIaT9bJfS-NMyq4-7dpTdMx0VjPko8YRk2HyNvv79csVVvWYwm8oL7PCqVi5jYXgPJACHyL6oygVTNtQX6CqUeGwvPn6_BM3R2OXWjQZOJcus9e5njyEQutxEsHT8hecM6l5YtghvOk3Lp9-HVRR9SvmvRQij36mo0I_neaovhG9tpflim_PgbSbRbf1IZMqR2ZyhNBR5RaIl0LM2fBRW44oCwD96B4-yYsDYUTsgIul2A-7FFoNZ-WDTNibPeG1E-c04aMKClHCVTvoIsqJoGPCM7-u95dJ7cXTktqx3zYB5Adh8R_VCD4h1yg_hQLKEjeb6FEMi6HSOgn7XgFm_tWc26N3e76zlqbI0vtKtwIz8EoPUZvH69oelz-oq6jx6mxw_0qQP4_ktUspxwJKCf70yoX0DxeGrjdC5O5fA2lit9Qso5fRW2jnt0qXcO8K37R6sumQKTAFTz2Hlxzr_HW3xewlWUHyV3PZpNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf0ec4e373.mp4?token=hR6nLv--esW3sBSBvd4wgsk6-yJzHOcxlE0QH3ihnen--x_GZwpS8d0ZQMRa8COqpMKguNe4MsT2En9qe-fIy_HqzRSZGVEs7E9SlIzDHn7VqW3_bxTnJl0a6KLaEpqafpATeNYNJmI5LYtypejxqBADWB8UOGOo-IbEITK_wvYc88wO-Zfq8vfhqeK_Z3f280YUIIaT9bJfS-NMyq4-7dpTdMx0VjPko8YRk2HyNvv79csVVvWYwm8oL7PCqVi5jYXgPJACHyL6oygVTNtQX6CqUeGwvPn6_BM3R2OXWjQZOJcus9e5njyEQutxEsHT8hecM6l5YtghvOk3Lp9-HVRR9SvmvRQij36mo0I_neaovhG9tpflim_PgbSbRbf1IZMqR2ZyhNBR5RaIl0LM2fBRW44oCwD96B4-yYsDYUTsgIul2A-7FFoNZ-WDTNibPeG1E-c04aMKClHCVTvoIsqJoGPCM7-u95dJ7cXTktqx3zYB5Adh8R_VCD4h1yg_hQLKEjeb6FEMi6HSOgn7XgFm_tWc26N3e76zlqbI0vtKtwIz8EoPUZvH69oelz-oq6jx6mxw_0qQP4_ktUspxwJKCf70yoX0DxeGrjdC5O5fA2lit9Qso5fRW2jnt0qXcO8K37R6sumQKTAFTz2Hlxzr_HW3xewlWUHyV3PZpNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن نامجو: کنسرت‌های تورنتو، نیویورک و واشنگتن‌دی‌سی لغو شده/بعد از تعیین تکلیف زندگی در ایران و خارج از ایران به روی صحنه بازمی‌گردم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/684766" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684765">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای عضو کمیسیون بهداشت: برخی اقلام دارویی تا ۲۰ برابر گران شدند
احمد آریایی‌نژاد، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
برخی اقلام دارویی به‌ویژه داروهای تک‌قلمی وارداتی، گاهی با افزایش قیمت ۳ تا ۴ برابر و حتی ۱۰ تا ۲۰ برابر مواجه شده و در مواردی سر از بازار آزاد و ناصرخسرو درمی‌آورند.
🔹
بخشی از این گرانی ناشی از تحریم‌ها و مشکلات واردات مواد اولیه است و از سمتی محاصره دریایی، هزینه حمل‌ونقل را افزایش داده و در تأمین ظروف و مواد پتروشیمی مورد نیاز تولید دارو و همچنین تخصیص ارز نیز با مشکل مواجهیم.
🔹
برای بیمارانی که توان مالی ندارند باید با تقویت پوشش بیمه‌ای و تسهیلات حمایتی، دسترسی به دارو تضمین شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/684765" target="_blank">📅 18:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
دخالت آشکار ترامپ تروریست در مسائل مربوط به فیفا و خط  و نشان برای مخالفان اینفانتینو  رئیس دولت تروریست آمریکا:
🔹
اگر فدراسیون جهانی فوتبال (فیفا) به هر دلیلی به فکر برکناری و جایگزینی جیانی اینفانتینو بیفتد، مرتکب اشتباهی بزرگ خواهد شد.
🔹
او فوق‌العاده…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684763" target="_blank">📅 18:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d83ea631.mp4?token=NLZPd-RJr_y5_xIWR8TeZpHgbFDGyAlu_m-WTPSsAEidCU4CXGvcOc6tzhSfekYZRBYpKeC2AgASt9q9zLBvGKdKXKTL_zJAR4fuQU9khUyDYLob-FJDSV4DL9PFACbyqdLwi2O-2MQnrzViWlkVW-PR0vcu2ddb1KTIjzkGQMDPG1SxsslYW0sUemGB3i53TM2YJY9Yv290b11vaDUQUqkVv1mROYrJbuSrb2TkglItkyoKvnDaVw58MWwhSdjqZ5SvV91S6FqJqK11oSMjRxpCHgB5atVss0TBehlH7kf18IvYhEpYyru8M_oKpSKfh8Z37vr7f9jElt2rqP5jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d83ea631.mp4?token=NLZPd-RJr_y5_xIWR8TeZpHgbFDGyAlu_m-WTPSsAEidCU4CXGvcOc6tzhSfekYZRBYpKeC2AgASt9q9zLBvGKdKXKTL_zJAR4fuQU9khUyDYLob-FJDSV4DL9PFACbyqdLwi2O-2MQnrzViWlkVW-PR0vcu2ddb1KTIjzkGQMDPG1SxsslYW0sUemGB3i53TM2YJY9Yv290b11vaDUQUqkVv1mROYrJbuSrb2TkglItkyoKvnDaVw58MWwhSdjqZ5SvV91S6FqJqK11oSMjRxpCHgB5atVss0TBehlH7kf18IvYhEpYyru8M_oKpSKfh8Z37vr7f9jElt2rqP5jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا به این فکر کردی که مایکروویو چگونه کار می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/684761" target="_blank">📅 18:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394056e459.mp4?token=rjupEp1pwm7CYZcd5W0dRx3ZqWFZSU1QzMoyDmfgRKWlMKqK5li8fR71-gU-DufIy60MjnduMrrUf4aKJAXcXZ7WGN9ZVmKZzlp3ha9rFQIOLiSnR9eKVbw1rqsbHguvc6Tp64WbXLETqrcJZiXFfg3mbMdjW2AHCMB2pmzy__y9xY21C4rK4a-4XgF0pZk1Dk7LWTtECLm_Jl15NdOMElxFTXdsEvzOSvvceBB7Bdf_5gdGbnl00dbsBPrQW1ryfgii-jbGFY05wpQHptcXcSNaR6-IcQS2bPwzG1mDdxLR0DRwUoiI-HWHRx3o5LTchIJO5T7fy4zyOIaNN_Smjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394056e459.mp4?token=rjupEp1pwm7CYZcd5W0dRx3ZqWFZSU1QzMoyDmfgRKWlMKqK5li8fR71-gU-DufIy60MjnduMrrUf4aKJAXcXZ7WGN9ZVmKZzlp3ha9rFQIOLiSnR9eKVbw1rqsbHguvc6Tp64WbXLETqrcJZiXFfg3mbMdjW2AHCMB2pmzy__y9xY21C4rK4a-4XgF0pZk1Dk7LWTtECLm_Jl15NdOMElxFTXdsEvzOSvvceBB7Bdf_5gdGbnl00dbsBPrQW1ryfgii-jbGFY05wpQHptcXcSNaR6-IcQS2bPwzG1mDdxLR0DRwUoiI-HWHRx3o5LTchIJO5T7fy4zyOIaNN_Smjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط در یک دقیقه تمام افعال و گرامر زبان رو یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/684760" target="_blank">📅 18:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43a9400350.mp4?token=Lhoj32rs0yGikiDjpnfzz_SubpLOReli3EmeIQb_fobea83jZ6RHqm8ntqtSaIW8qFshu26uvb_203Olstz34GNl4TTqcZzq5r5IAgVt2UZ0LEK-KI4TbHz6QhbIv4ENmHoPg1MPqUFYehbV4KWfb1GYDT-U5hR27rkfl3-RkGhVYUTkqyoavx2PI72VbUPXDsBLBx9ChtcN4s1DbwfwiB4YMLuD9oqHtmSYs6gLUHZvODAegGTfYYJ_dltaX5_8a3DVsj6UeVpBdBc-_3EKh9c4pIVrYoV5t53mJGf6_koMtGViXOTICpYtbKREW4PWU9B-kVZeaE_qV2M9pCMYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43a9400350.mp4?token=Lhoj32rs0yGikiDjpnfzz_SubpLOReli3EmeIQb_fobea83jZ6RHqm8ntqtSaIW8qFshu26uvb_203Olstz34GNl4TTqcZzq5r5IAgVt2UZ0LEK-KI4TbHz6QhbIv4ENmHoPg1MPqUFYehbV4KWfb1GYDT-U5hR27rkfl3-RkGhVYUTkqyoavx2PI72VbUPXDsBLBx9ChtcN4s1DbwfwiB4YMLuD9oqHtmSYs6gLUHZvODAegGTfYYJ_dltaX5_8a3DVsj6UeVpBdBc-_3EKh9c4pIVrYoV5t53mJGf6_koMtGViXOTICpYtbKREW4PWU9B-kVZeaE_qV2M9pCMYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با خرید از "چرم مَنطِـ" BMW ببر
❗️
از %𝟲𝟬 تا %𝟴𝟬 تخفیف «تمامی‌کالاها»
در جشنواره پایان تابستان مَنطِـ
🔥
➕
𝟮 میلیون تومان تخفیف اسنپ‌پی
حضوری و آنلاین با کد: PAYCWGZ5
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/684759" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXTNRPN_UuOWE_zKwOl0huCwWfsDU0He5z8VRwP16Thr1mtagUrok31Rloss3fJIqwGyARJ3hiiGFgjOJTiav4XnRKuPkfvj2hRfUh31Hb64OI6r379dnbNIJll3NX3YuZPMjFw0lK05M8nATr4FRcwyPE-UXBzK2MTFiue2tfrsreqKOcsuPAJXmXESZVmOSL5tImMOEvz1ZQDeTymJNlr1g9Io3kAdoDMBe5JAy0HmwJ8SmOLJYYVXKyJOF7iQcY6oC2vAX3TwjcblLNyLTIr10iME46bOeXirKmWZwojqbAv34Dh6SKeL2yeFrvWj5guONHqPRbsujv0s5P4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر پزشکیان از عملکرد وزارت راه در ایام جنگ
🔹
در اختتامیه بیست‌ویکمین جشنواره شهید رجایی با عنوان «روایت نصر»، وزارت راه و شهرسازی به‌عنوان دستگاه اجرایی برتر در بخش «یاور فتح» انتخاب شد.
🔹
این عنوان به دستگاه‌هایی اختصاص دارد که در روزهای جنگ، با وجود شرایط ویژه و محدودیت‌های ایجادشده، فرآیند خدمت‌رسانی به مردم را متوقف نکردند.
🔹
در این مراسم، فرزانه صادق، وزیر راه و شهرسازی، به نمایندگی از مدیران، متخصصان و کارکنان این وزارتخانه مورد تقدیر قرار گرفت.
🔹
وزارت راه و شهرسازی در جریان جنگ، مسئولیت تداوم فعالیت بخش‌هایی از زیرساخت‌های حیاتی کشور از جمله حمل‌ونقل جاده‌ای، ریلی، هوایی و دریایی را بر عهده داشت؛ بخش‌هایی که توقف آنها می‌توانست مستقیماً بر زندگی روزمره مردم و جریان جابه‌جایی کالا و مسافر اثر بگذارد.
🔹
حالا انتخاب این وزارتخانه به‌عنوان «یاور فتح»، یک پیام روشن دارد: در روزهای جنگ هم، زیرساخت کشور نباید از حرکت بایستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684758" target="_blank">📅 17:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434b9312db.mp4?token=q7ET_pZVQWL--ySVrhz19CRlYS8SnS8nig1wn2RezK4HcteXCleJFioOsm_1I-d7aR0BrlpaJM6zm2AiEwAJCzSq0h0YAKIzy-XiPLx-XaEs8o7yjumROlEZCPaOCij09GSUvPvaBl_LsYLfs5W31ehMWRTmJkPK3zHCvO5AYhgZDYvf3hLzoO8fp-gTTsw3hD_JuMzfeAUQeyw5CNmbHWL3vTrtwS9QiXCVUY0DVTL2cUaWd1WU5NY6RMX2xJWyYxYex37gj6Wz0sO9IP4h64M2QyWUxcxVhkPr5SeArnwZE1KU4Lxu8BuXfrzeX0uGmqiu5IMzwqW8VaiAIE_hOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434b9312db.mp4?token=q7ET_pZVQWL--ySVrhz19CRlYS8SnS8nig1wn2RezK4HcteXCleJFioOsm_1I-d7aR0BrlpaJM6zm2AiEwAJCzSq0h0YAKIzy-XiPLx-XaEs8o7yjumROlEZCPaOCij09GSUvPvaBl_LsYLfs5W31ehMWRTmJkPK3zHCvO5AYhgZDYvf3hLzoO8fp-gTTsw3hD_JuMzfeAUQeyw5CNmbHWL3vTrtwS9QiXCVUY0DVTL2cUaWd1WU5NY6RMX2xJWyYxYex37gj6Wz0sO9IP4h64M2QyWUxcxVhkPr5SeArnwZE1KU4Lxu8BuXfrzeX0uGmqiu5IMzwqW8VaiAIE_hOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه برخورد صاعقه به هلال برج ساعت در مکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/684757" target="_blank">📅 17:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ترامپ جنایتکار وضعیت وخیم در ناو آمریکا را رد کرد
🔹
خبرنگار: اعضای خانواده سربازان نگران شرایط ناو یو اس اس لینکلن هستند.
🔹
ترامپ: نه، نگران نیستند.
🔹
خبرنگار: آیا استقرار نیروها خیلی طولانی شده است؟
🔹
ترامپ: نه. نه. نه. به اندازه کافی طولانی نیست. #Devil…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/684756" target="_blank">📅 17:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684752">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUNQ6VI7Nfoi0jU26PhMy4-Qbc5-18qjE9-cUce6G1TkbZuN8s-RXeZpuq_iMvT6znghxsjq5MLMZU4QlPD-e2SZvtmfLEQtA_uEmsIX6sdgvW1bz3HakUPK9Y9070tHRB4jA2RJsLch6b8h47GCT71iuTyIzt4it5syELtW0igUjM1uOms2DfCUBxENPsQr-LSpnU6kFcCPbaWP_bt7JGg7h125NNtx8xXqsRtKSCbMknflZmtu8Qd9Ic1NVBoHaXrvzCZLfqmrn_1mXPi8zUz_e_-W3uCZaO5R9t8ESG_ObHLb5lgUD7YUg7LSefjIis9SXwYo-L67zvqnMo8QcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
اگر برای تهیه داروی مورد نیاز خود یا خانواده‌تان با کمبود، گرانی، نبود پوشش بیمه، نایاب‌شدن دارو یا سرگردانی بین داروخانه‌ها مواجه شده‌اید، تجربه‌تان را برای ما ارسال کنید.
🔸
در چند خط یا در قالب ویس حداکثر ۳۰ ثانیه‌ای، روایت خود را همراه با نام، شهر و نام دارو برای ما بفرستید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/684752" target="_blank">📅 17:26 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
