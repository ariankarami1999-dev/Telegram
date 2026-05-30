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
<img src="https://cdn4.telesco.pe/file/mQBaxr-SSSc6rXZlBpKSeNrbyOyXdaXfeSWmdAj8wC7jTq-KWUEXmiUYyAjmKB6Vno_tl8OjKZMw2KI_ZAuQHxERZgpi2wf07g0EOyT2xgZ2D-bIuj3ukA39VbthYLahoIcMOgVzPuzX0qfu-6eUSyAbx67rnSE5nYYZrsaGIE6FSUbi66RWf2YS8WdfLPuGOt6MBnxs0NPJ3RnXu3qxPQoVxAKKy5y1zgdyfIbK6rbuT1g5jdIKN14bK8gIQSzn1zDI-s-I5pseFv7gAO6T4eanqoqPLf-0LFbz_cP4og7LiqgqmOKtubHciKfvJJo0TEsEqsEBkrO1rp0GZxbMbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 20:41:57</div>
<hr>

<div class="tg-post" id="msg-654868">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
۹۰ درصد پول پروازهای لغوشده تسویه شد
‌
معاون هوانوردی سازمان هواپیمایی:
🔹
طبق مستنداتی که شرکت‌های هواپیمایی ارائه می‌دهند بیش از ۹۰ درصد از بلیت‌ها تعیین‌تکلیف‌ شده است؛ ۱۰ درصد باقی‌مانده نیز کسانی هستند که اقدام به آغاز فرایند استرداد بلیت‌های خود نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/akhbarefori/654868" target="_blank">📅 20:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654867">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
در تجربه مرگ موقت، آینده‌ای تاریک از خود دید؛ تصویری که باعث ترک اعتیاد و تغییر شد
🔹
06:00 عذاب کسی که به نامحرم نگاه بد و دست درازی داشته
🔹
10:45 نوشیدن اشک دیگران توسط جهنمیان برای رفع تشنگی
🔹
18:50 رؤیت افرادی با چهره هایی بسیار زشت
🔹
22:50 کدامین گناهکاران مورد عنایت قرار می گیرند و بخشوده می‌شوند؟
🔹
28:30 چگونگی مورد شفاعت قرار گرفتن تجربه‌گر توسط حضرت زهرا
🔹
35:50 حس تولد دوباره بعد از  تجربه
🔹
47:50 سفارش اهمیت به مادر و همسرم در طبقه اول جهنم
🔹
01:07:40 ماجرای شنیدنی دعای هدایت شدن درحق بدهکار توسط طلبکار
🔹
قسمت دوم، (منفی هفت)، فصل چهارم
🔹
#تجربه‌گر
: دانیال قاسمعلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/akhbarefori/654867" target="_blank">📅 20:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654866">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: آمریکا یک کشتی فله‌بر را در خلیج عمان از کار انداخت
‌
خبرگزاری آسوشیتدپرس:
🔹
یک کشتی فله‌بر لیان استار که با پرچم گامبیا به سوی ایران در حرکت بود، هشدارهای مکرر نیروهای آمریکایی را در طول شب هنگام تلاش برای ورود به یک بندر ایرانی نادیده گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/akhbarefori/654866" target="_blank">📅 20:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654865">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
آزمون‌ساز شبکه شاد پولی شد
🔹
در حالی وزارت آموزش‌ و پرورش اولویت برگزاری امتحانات را در سامانه شاد اعلام کرده است که آزمون‌ساز شاد بسته‌هایی با نرخ‌های متفاوت ارائه می‌دهد.
🔹
از بسته ۵۰۰ آزمون به قیمت ۷۴۹ هزار تومان تا بسته ۳ هزار آزمون به قیمت ۳ میلیون تومان در آزمون‌ساز شاد به فروش می‌رسد. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/akhbarefori/654865" target="_blank">📅 20:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654863">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اعلام آمادگی گروسی برای کمک به حل اختلافات بین ایران و آمریکا
‌
🔹
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی اعلام کرد ذخایر هسته‌ای یک نقطه اختلاف بین ایران و آمریکا است و برای کمک به حل آن آماده‌ایم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/654863" target="_blank">📅 19:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654862">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b21f9c1c3.mp4?token=R_hP2rzsASYrP8tWotLSCnzySRp3nPijpZ66RhFaCs5jY8v4s0HcpfOaswiHamgfMBtdSiKFNJTJ6kNuazCE8KLe1-LpiUCktVa2c2-4c9TLriFTsMEP-0ndoIs5FBig-k6Ygr1QnjdrkkPNYjUaBvcjk8mm2quIAaLYoHbX5SdH8iqGdaZK2yCkG9KZwZq93X4pySfGZSifdgb0q7ITY4Dn_R4nKWsfgGzfBWGqUG4LxfdMoau6ePavuH8OwRKPCS7Jt1i0CvzA0lm9xzxpJbONY2gsu-KXyiYpD73h09dK8PuTaVp_o1mr21tvP3ntCovS4g1UxhozdFKGDi4H0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b21f9c1c3.mp4?token=R_hP2rzsASYrP8tWotLSCnzySRp3nPijpZ66RhFaCs5jY8v4s0HcpfOaswiHamgfMBtdSiKFNJTJ6kNuazCE8KLe1-LpiUCktVa2c2-4c9TLriFTsMEP-0ndoIs5FBig-k6Ygr1QnjdrkkPNYjUaBvcjk8mm2quIAaLYoHbX5SdH8iqGdaZK2yCkG9KZwZq93X4pySfGZSifdgb0q7ITY4Dn_R4nKWsfgGzfBWGqUG4LxfdMoau6ePavuH8OwRKPCS7Jt1i0CvzA0lm9xzxpJbONY2gsu-KXyiYpD73h09dK8PuTaVp_o1mr21tvP3ntCovS4g1UxhozdFKGDi4H0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرسنال به پاریسن ژرمن در دقایق ابتدایی
🔹
آرسنال ۱_ ۰ پاریسن ژرمن
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654862" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654861">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
اعتراف نخست‌وزیر لبنان به جنایات گسترده رژیم صهیونیستی در خاک این کشور
نخست‌وزیر لبنان:
🔹
اسرائیل تنها مناطق مشخصی را هدف قرار نمی‌دهد، بلکه سیاست تخریب فراگیر را اجرا می‌کند. اسرائیل با این اقدامات، به کوچ اجباری و جمعی ساکنان نیز دامن می‌زند.
🔹
تصمیم گرفتیم به‌سوی مذاکرات برویم، زیرا این گزینه را مناسب‌ترین مسیر و کم‌هزینه‌ترین راهکار می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/654861" target="_blank">📅 19:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b51d87ca.mp4?token=vRnE97Sn32u7IOVT_E9R9AfZLXjnxIBZKZxr0IJ0hoy96gNG9b_bbFfsLp1lZVfcovo3SraWivT_LBRkzu2jZSqmmO4qUdSN4s5yiR90qqpUyCWOwWPTnSRwVuXK11KnZnLV-Y5ozemoBxp3wdg6ycpIvdZBL7To_rV90f7NjL3oHKLF4VjRIwzDo-BfiG5YQN1yaPbMZukaj0zBXZPuCPqk8nvHvoB0Z43raPyC96uCnbqLwlbQQgAE9hjZVV6hI3X2WuqDnq5IlwxZ1Wj6lrfhtN1ipDMjfrOTDZCdg5ajF3wf19X60pO_sJxm443FXatwhuEDxXOopvokeqWLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b51d87ca.mp4?token=vRnE97Sn32u7IOVT_E9R9AfZLXjnxIBZKZxr0IJ0hoy96gNG9b_bbFfsLp1lZVfcovo3SraWivT_LBRkzu2jZSqmmO4qUdSN4s5yiR90qqpUyCWOwWPTnSRwVuXK11KnZnLV-Y5ozemoBxp3wdg6ycpIvdZBL7To_rV90f7NjL3oHKLF4VjRIwzDo-BfiG5YQN1yaPbMZukaj0zBXZPuCPqk8nvHvoB0Z43raPyC96uCnbqLwlbQQgAE9hjZVV6hI3X2WuqDnq5IlwxZ1Wj6lrfhtN1ipDMjfrOTDZCdg5ajF3wf19X60pO_sJxm443FXatwhuEDxXOopvokeqWLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام قهرمانی اروپا راهی ورزشگاه شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/654860" target="_blank">📅 19:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItS6Jg2qMkI-fCQqJIjvnToIU6c8gn70eflznkyCe9l8aRGahm2vg8v51okVAqAI71r4gacDClGhFpH1KjNquPTJuwt-N1eLlNnUsX9alvFvxfn-Gds3CwUuhFCWSsmfvVad9YSLZjBaNIDCvj5k3dci2E1EsP7MqIYtuChTOIbhA1S-2tXTKRd89rDZXP0oivBDtH94i_x0jST2q_xo8bchTumS4q7F6NohLjUFe9TQhutNoB5be4VHTz6ccdrPkV_gzteuborFGkY91U-yynsvHIfh7b6vJnYq9W1X9SN_2YhQ4evla1H5Gp7x7Ms2TA6y_hNwur6bdc_ZbU3QTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعایی درباره کمک نظامی چین به ایران در جنگ با آمریکا
🔹
برخی منابع به ان‌بی‌سی نیوز می‌گویند ایران ممکن است از موشک چینی برای سرنگونی جت جنگنده آمریکایی استفاده کرده باشد.
🔹
افراد آشنا به این موضوع گفته‌اند که چین ممکن است یک رادار هشدار اولیه دوربرد در اختیار ایران قرار داده باشد که هواپیماهای رادارگریز را که برای فرار از شناسایی طراحی شده‌اند، شناسایی می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/654859" target="_blank">📅 19:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQCfynls1vGMURgi_9dC8r6FMUZzfV55LCifaVpi-aAiGg7ZWeOoPEAAY5jlwBezBA07wtOHOFXQxzBNHdjTpOwADysOp6a2j58hBZ3Q_WCCghB6zdFErmri4ooR3N2S7zJcLwfiyvak2GEctsd4bn6Q4QlMn8p-KggVD-MLyFS0HAd3chkPDRqDIDiKXa5gcjhuqs4oz36iYa33IhuK2TbUvadnNgHXwCrzWE12mPPk8aKAqITTzBy8rFohhnEoXyXXDONXKOc6ycw0ENQfbM5vO7lDOOhQg-s3Bw6092X-5OYRjhJLVHvoAHPg9sPQnJndIUHykqfvgwl33nWlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری تماشایی از رنگین‌کمان در ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/654858" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بارورسازی ابرها قیمت خورد؛ هر هزار متر مکعب حدود ۲۵ دلار!
جوادیان‌زاده، کارشناس ارشد توانیر و رییس سابق سازمان توسعه و بهره‌برداری فناوری‌های نوین آب‌های جوی در
#گفتگو
با خبرفوری:
🔹
افزایش بارشی که برای باروری‌سازی ابرها می‌تواند اتفاق بیفتد بین ۱۵ تا ۲۰ درصد است اما برای کل کشور اثرگذار نیست.
🔹
حدود ۳۰ تا ۴۰ درصد این افزایش بارش تبدیل به رواناب می‌شود که به شکل منابع آبی زیرزمینی یا پشت سدها ذخیره می‌شود و داخل رودخانه‌ها جریان پیدا می‌کند.
🔹
قیمت تمام شده بارورسازی ابرها برای هر هزار متر مکعب حدود ۲۵ دلار است و روش ارزانی نسبت به سایر روش‌ها است، اما روش پایداری نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/654857" target="_blank">📅 19:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej4pXEYoyRA4gOW3ogS6tm7xFf0Yu9q4RzLQWMw3AP1BVwFKRHSdzhnJ93LueLLWmouzR0NaKelyUoSnOKqt-79KXYcFYF-ggRYTU4kviMavq-OOnDKWShbDIG-ViPE92ma9LhsU6-nyEtLSUa38vOWIqTvxhskbAhkrgUKk_Iar0_xaPO8UxokN6CZU6yragFHl_y6HjDmg1mD7Ez2BHjfkj3JjrNToc1DhLKfmJM5qWjJUxEE8kM4Et9UVqG6N5i8ExuAhEOcnr3gU8pNP7PXr1iPXA9FrgBrK4TRRZVPWpf9NDkjxN5p067ok8sI4GHkeHyiX4oZV_MwdQSbJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاندان بختیشوع؛ بنیان‌گذارهای پزشکی علمی در جهان اسلام
🔹
خاندان بختیشوع یکی از مشهورترین خانواده‌های پزشک در تاریخ ایران و جهان اسلام بود. ریشه‌های این خاندان به سنت پزشکی جندی‌شاپور در دوره ساسانی و پیش از اسلام می‌رسید؛ جایی که دانش ایرانی، یونانی و هندی در هم آمیخته بود. بختیشوعیان پس از فتح ایران این میراث علمی را حفظ کردند، به بغداد بردند و برای چند قرن پزشکان برجسته خلفای عباسی، استادان پزشکی و از پایه‌گذاران بیمارستان‌های علمی جهان اسلام شدند.
#نامداران_تاریخ
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/654856" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مدیریت تنگه هرمز توسط نیروهای مسلح جمهوری اسلامی ایران با اقتدار کامل اعمال می‌شود
قرارگاه مرکزی خاتم الانبیا:
🔹
با توجه به یکپارچگی این مسیر، تأکید می‌شود کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفاً ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران انقلاب اسلامی هستند. هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.
🔹
همچنین هشدار داده می‌شود هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی ایران قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654855" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W615WHkIQkHaSMUMbFXQWCWrXX20akHwjOfIlPTfqh6GG2mQFniuqZ-K2aYhcJXHXTF6x5ZCQ5isC90zcKmduEol5HFydEqbAcZ6FqWrCdkUmXt0VG5uzHwnti9iCnE5DZY4dVhgQ7oUZ9Gy-Z_fx67ybAKMVIFr51CQw3LRWjS0xtRJmerUIi3G0-c2C04IGnUVcOQ4UWlObsnaRaNeYyIJ0hmkznNKf0zIARQAqc9QrKnXXpHxvKl9UAOtHmAp_CWtkFYccq6ONpf6WiYxSCjxGLJiwFVRtQKUu43w3XTbs3lLD49XrKUy2HX6FGBmmdc5ljkRg2qU_mFMXYMFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ رکورددار تریدرها شد!
🔹
دفتر اخلاق دولت آمریکا فاش کرد که ترامپ در سه‌ ماهه اول ۲۰۲۶ نزدیک به ۳۹۰۰ معامله ثبت کرده است. یعنی روزی بیش از ۴۰ معامله که میانگین روزانه‌اش را از بسیاری از تریدرهای حرفه‌ای وال‌استریت هم بالاتر برده است.
🔹
در تمام سال ۲۰۲۵، او هر فصل حداکثر ۲۵۰ معامله انجام می‌داد. اما سه‌ ماهه اول ۲۰۲۶، ناگهان ۱۵ برابر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/654854" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
گمرک مهلت تردد خودروهای پلاک خارجی دارای مجوز ورود موقت را تا پایان تیرماه ۱۴۰۵ تمدید کرد
🔹
این تسهیلات شامل خودروهایی است که مجوز ورود موقت آنها تا ۲۹ اسفند ۱۴۰۴ صادر شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/654853" target="_blank">📅 18:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/633f3ac517.mp4?token=NIiq-RHaBjvZ7725AJQJkcb3zijRNCwWbn88lAjMKOO370ty6Et-in1gLkPVwx4O7Jc4y5hQFetYX3sdnMy1jjvAN1LT2nOrqsp4xGLLWibGZPfQkFz7j6HzLYSPTyR2mFXZRAwdJRsm3d8tF9TDfovGJRO6IsEU21Ts1uWKX6lJPHyBFet6tWrhZpg67epwfJhJzZeF1UAGf1KjP0vmgAErJuvLLtcY5bp3uRCcOq9qQdEWWlIiVSASxWxx_arF912y1IYnJXZz3U8tCeoda_d63voOJUsQvXVJ-Cuj-uCOnIUlWSs10MB1GzUanYRRY0WwYjsUlmXnbJ4Q7fQyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/633f3ac517.mp4?token=NIiq-RHaBjvZ7725AJQJkcb3zijRNCwWbn88lAjMKOO370ty6Et-in1gLkPVwx4O7Jc4y5hQFetYX3sdnMy1jjvAN1LT2nOrqsp4xGLLWibGZPfQkFz7j6HzLYSPTyR2mFXZRAwdJRsm3d8tF9TDfovGJRO6IsEU21Ts1uWKX6lJPHyBFet6tWrhZpg67epwfJhJzZeF1UAGf1KjP0vmgAErJuvLLtcY5bp3uRCcOq9qQdEWWlIiVSASxWxx_arF912y1IYnJXZz3U8tCeoda_d63voOJUsQvXVJ-Cuj-uCOnIUlWSs10MB1GzUanYRRY0WwYjsUlmXnbJ4Q7fQyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حزب‌الله، شهرک‌نشینان صهیونیست را وادار به فرار کرد
🔹
موج شلیک موشک‌های انتقامی حزب‌الله به مناطق شمال فلسطین  اشغالی، سبب فرار صهیونیست‌های مهاجر به پناهگاه‌ها شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/654852" target="_blank">📅 18:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654851">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjFE8-KDrVvIWUPaZIp5BOBrsT94XUZBcomSsGVPf4vqXYCvH-O5FlJc5KWutoaNJ9SRGxNeSU83yddYSsSZR-s1S2pgQkBzVOMX-EPo_H1_zxbHbCluPominIiSPLmbLV9kSk1HkANHYqRpNbvdpu0aqpPZLBzMArb2BJnQ-2u5YKkVTcSNIsueLqbTOHesy9Sb5tn7O23VEYJDVn6RFXlUkpfeE06hNjKTb4V8q1hr0sfkkFR6gR9smRgM19r-W-7HypoH8RJj6kLQagtVk2jVN40wnsIdTFvVbQ33teH09mvFmUztwSjEukQfucUPp_JEBwPnZdib5n4x_KxzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقلال و تراکتور، نماینده ایران در رقابت‌های آسیایی
🔹
تیم‌های استقلال و تراکتور به عنوان تیم‌های اول و دوم جدول لیگ تا پایان هفته بیست و دوم، به عنوان نمایندگان ایران در لیگ نخبگان آسیا معرفی خواهند شد.
🔹
همچنین تیم سپاهان به عنوان تیم سوم لیگ به عنوان نماینده ایران در لیگ قهرمانان آسیا ۲ معرفی شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/654851" target="_blank">📅 18:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654849">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaYuUHMCaeKFEVe0J33jfSZTW0XPk65P99RQrTYdtMPmiNy7SEW5eigXAqpaAoX-4BikuDQ9Baqiwv85-UIN3hSmRJQpotdwenSRqbfA_1SIfp_5Ks4OeTWfoQ7m0d6-Mmivx45KwOgZ30n7Q4oPaROSgfLY9vSCYEJAjeS25fz_eYXlbryeZwp1syiPlaQTCuPLnFJTg0XbAaW_hG4sXR_00TmZ8WFGLsIc7vmesGQnaBNd6mzEOo-tK_HOGjJJn7HpzZ3AelrtHD2LKQLISA4EWW2OzmQ5y29G_qZiyoOK-moF4wmlueRBOL-dSus2iNEAgKECUdz1GMPV6byFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7s-7_sTtybFZeRNGl0h0LqqR8hyesAdVL34zJ5SaYBJlrlOxoKlIDl4kzU9MR9JVGRpFcu7FH31nH2DVxyyELIdGXIDPhNL8h8G5Vf_pK7bGgQJZ_JszGqjTDE72oZOre1IhV1BzLzrLQ3jPdAxpEY22WVMsyS9pwyLR67n5cmWDBv30hNyMW8sMxdP0_SQU48keHZQwsjafEUvevVO1GX8mhgDXBWIoVWmXa69UDaxWna9v1ntbZqnvSPPPyOhCjOeD4dqaqA16ijm4Y5Y07YEHnqjeAhJw0F2gu4cEPKMCCAnWd_GR6Drw1a8Zed6uKKDxNVva2sfXhvnAyEPAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لونا، شیر ماده که در پارک حیات وحش در کره جنوبی زندگی می‌کند و بخاطر خوشگلی و قیافه منحصر به فردش در دنیا معروف شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/654849" target="_blank">📅 18:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654848">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل: از صبح امروز هر ۲۲ دقیقه صدای آژیر حملات موشکی در شمال اسرائیل به صدا در آمده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654848" target="_blank">📅 18:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654847">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIqHQ-AfCONHJmQxbpVTg5M1dHk7-N2Lz3e7KRFO_wNvzm5aHA0S1B3x4GbVwLiY7I543B2oHU8r5-Ub9ZVWLx4_eaM9XC_s5_kWYr3s-3cBW27z9zS8m9vzjvJkwQgs2jsvonubKhnDGWipt3dSocbK-emFlQIcVNDam-TOZwHYMrv54ydwAt8AYR6XGQSdLwBWLATnj1ST4zbtl_AnOEdaoKpQJVh1skSsR5hDGQx_uYWLQTFKkYntmotQ7jruxPICiLBdLCtUg5iPsTA8iVVglGOuOQQELaqxHDGOPwjfl4xIFQTCxcYrE9UDIAhxSzh6QUV7EHghWdTz_FyQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرواز همای، خواننده: هزینه تاریخ نخوندن و اینترنشنال دیدنتون برای ایران خیلی گرون تموم شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/654847" target="_blank">📅 18:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654846">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سی‌ان‌ان: نقشه رژیم تغییر کرد/ تهران نه، واشنگتن!
سی‌ان‌ان:
🔹
نتانیاهو پشت درهای بسته اذعان کرده اسرائیل نفوذ محدودی بر نتیجه مذاکرات پایان جنگ با ایران دارد. او خواهان حمله به تأسیسات نفتی ایران بوده و کوشنر و ویتکاف را متهم کرده ترامپ را به سمت پایان دادن به خصومت‌ها برده‌اند.
🔹
اسرائیل آن‌قدر روی «تغییر رژیم در ایران» حساب کرده بود که احتمال «تغییرات سیاسی در واشنگتن» را ندید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/654846" target="_blank">📅 18:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654845">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=AjFIuFbc1R1ltZvAt0ye0DdxujbxQaiLnkdKCJMb7QoJ_mGtzvdVSBsjlAXtZnOyPcHFlPvgXQW8COO7q8wmu2h5CLtKxC8RQeNuviz2FOcqXGYi1rXfa3OHjfrrmP5FMEiZ7o6crYEWaAoIgOmw5wiwcyOapBFzw24i8fS_WDA-SDLKUflKuXbKQD9xvD3RddOvZWGvP9hTNokyINWlG6nemZeoV-DGtt2eViiHxnTIJSdzyM6qwvXPC6ofNFKB79vlXsoG35u3FQrtPVK8OAU_1j3gd6YSzLOE7JPpjEZoousSyO8nUceFOeTbpt36Gl80sOLpk_ns8pJeWd-uVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05a6002ef.mp4?token=AjFIuFbc1R1ltZvAt0ye0DdxujbxQaiLnkdKCJMb7QoJ_mGtzvdVSBsjlAXtZnOyPcHFlPvgXQW8COO7q8wmu2h5CLtKxC8RQeNuviz2FOcqXGYi1rXfa3OHjfrrmP5FMEiZ7o6crYEWaAoIgOmw5wiwcyOapBFzw24i8fS_WDA-SDLKUflKuXbKQD9xvD3RddOvZWGvP9hTNokyINWlG6nemZeoV-DGtt2eViiHxnTIJSdzyM6qwvXPC6ofNFKB79vlXsoG35u3FQrtPVK8OAU_1j3gd6YSzLOE7JPpjEZoousSyO8nUceFOeTbpt36Gl80sOLpk_ns8pJeWd-uVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجهیز جنگنده‌های سوخو ۳۰ ارمنستان به موشک‌های هدایت‌شونده ایرانی
🔹
به گفته کارشناسان نظامی، در رژه هوایی روز ملی ارمنستان در میدان جمهوری ایروان، جنگنده‌های سوخو-۳۰SM نیروی هوایی ارمنستان با بمب‌های گلایدر (هدایت‌شونده دقیق) ایرانی یاسین پرواز کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/654845" target="_blank">📅 17:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654844">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21774a84d5.mp4?token=crm1K8SJq3UehAb43ZsdUmGUbFEWXNuoXTvZYFoUJuhzfD2RG6SW58TRcrSHTw_5CK73GvIE6I7zD2ANYrX7yFNVQRGQv-bmkuB1Wv1o802P3fZhqWQvggUgUV_p-Uwwx9XlNifKXBovBAyJoui2c2Qp3wmZ-QF1LeUsQbUCDsde6SMoZQRwTe8mBBmQuiThcxNCHjhzt6NlWaTcz_hgcs0zg4r8XB0gkHBITl-1d-iqBY-ThWg8Y0SMqRjwevts9v4Dgw8BVGXd70uuE7HtcmOTpDsrHOZoSiOUIqMRdjZQMUgzwQB0prZGG5mI-sDmN5d9fc6ik5kc3ulL6Gwr3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21774a84d5.mp4?token=crm1K8SJq3UehAb43ZsdUmGUbFEWXNuoXTvZYFoUJuhzfD2RG6SW58TRcrSHTw_5CK73GvIE6I7zD2ANYrX7yFNVQRGQv-bmkuB1Wv1o802P3fZhqWQvggUgUV_p-Uwwx9XlNifKXBovBAyJoui2c2Qp3wmZ-QF1LeUsQbUCDsde6SMoZQRwTe8mBBmQuiThcxNCHjhzt6NlWaTcz_hgcs0zg4r8XB0gkHBITl-1d-iqBY-ThWg8Y0SMqRjwevts9v4Dgw8BVGXd70uuE7HtcmOTpDsrHOZoSiOUIqMRdjZQMUgzwQB0prZGG5mI-sDmN5d9fc6ik5kc3ulL6Gwr3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان وحشتناک در شهر بیکانر در هند
🔹
طوفان گرد و غبار عظیم، شهر بیکانر در ایالت راجستان در هند را تقریباً در تاریکی فرو برد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654844" target="_blank">📅 17:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654843">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84f533728.mp4?token=bYIGy1LiwZoJ0TTbnqILA8QvkmK8sxlhbGkrN7KJXnzluDkq9g-YFCQ3E950OghaZbg1Mp2OCWFX57au-6qkFDKrgJ2vh-xe1SRKNoE7bMG6RGb6_at7DzNMS-POpOZHr5wCbNj4JiTB4VQ5kPvb6-fCIOYOScna_cgA1qTRitHuAEeoeqwmbmITvSQvevUePJVbj9PGOjxufbRoOtWRfj_DjN31DD4A8b24zkVTLCuFnwK5MWAZ4tFh0otBNgwOPkl-kEe9Btew_1t46e5md1pH-Ujd8oZ2pxu5zVGWwB7ZVwhj19oWzIK0bnsRJUFwLDjsESvmWxNfvvjRC0lNPS-hMjGqF8c3HzXfGNnqgVRh9VowM85R9PxZy3vJGujAfFRyZ5vGL37pw1KGHW9Ay40y39QmizldjLV0Cj5r_uMWMtTW3fFKE6ODb1qYbBUmyyjs9ilmuMOzvDHcZpoLKFudQmGDcZWpJL28X4zoNIWHHInqo6X57jJXuJeq2Z_PiKDPKUs9If1cjs46eCYK601oNiRBpCNigmWvpHjWFL1Vwg9t-N0cGTgFqk5dqY7GMUmw6yx78mRXQntdTi2Z3cFZ3ZF71foBoIN3zFNgL1BrcpHg62a1_TNAhkZe6ZjCRbJEWMdS5l4DIZTKXPfoeBoN9UdPvYImzi8BE99yFP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84f533728.mp4?token=bYIGy1LiwZoJ0TTbnqILA8QvkmK8sxlhbGkrN7KJXnzluDkq9g-YFCQ3E950OghaZbg1Mp2OCWFX57au-6qkFDKrgJ2vh-xe1SRKNoE7bMG6RGb6_at7DzNMS-POpOZHr5wCbNj4JiTB4VQ5kPvb6-fCIOYOScna_cgA1qTRitHuAEeoeqwmbmITvSQvevUePJVbj9PGOjxufbRoOtWRfj_DjN31DD4A8b24zkVTLCuFnwK5MWAZ4tFh0otBNgwOPkl-kEe9Btew_1t46e5md1pH-Ujd8oZ2pxu5zVGWwB7ZVwhj19oWzIK0bnsRJUFwLDjsESvmWxNfvvjRC0lNPS-hMjGqF8c3HzXfGNnqgVRh9VowM85R9PxZy3vJGujAfFRyZ5vGL37pw1KGHW9Ay40y39QmizldjLV0Cj5r_uMWMtTW3fFKE6ODb1qYbBUmyyjs9ilmuMOzvDHcZpoLKFudQmGDcZWpJL28X4zoNIWHHInqo6X57jJXuJeq2Z_PiKDPKUs9If1cjs46eCYK601oNiRBpCNigmWvpHjWFL1Vwg9t-N0cGTgFqk5dqY7GMUmw6yx78mRXQntdTi2Z3cFZ3ZF71foBoIN3zFNgL1BrcpHg62a1_TNAhkZe6ZjCRbJEWMdS5l4DIZTKXPfoeBoN9UdPvYImzi8BE99yFP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این فقط روایتِ حمله به یک کارخانه نیست...!
🔹
روایتِ حمله به قلبِ صنعت فولاد ایران است.
به جایی که هزاران کارگر شریف ، زندگی، نان و آینده‌ی خانواده‌هایشان را در دلِ آتش و فولاد ساخته‌اند.
🔹
وقتی زیرساخت‌های فولاد خوزستان هدف حملات آمریکایی‌صهیونیستی قرار می‌گیرد، فقط آهن و ماشین‌آلات آسیب نمی‌بینند...
بلکه معیشت کارگران، توسعه‌ی کشور و امیدِ یک نسل هدف گرفته می‌شود.
🔹
اما این داستان، داستانِ سقوط نیست...
داستان آنهایی‌ست که از میان دود، از دلِ آوار و از میان خاکسترِ کوره‌ها دوباره می‌ایستند.
کارگرانی که باور دارند:شاید بتوان کارخانه را ویران کرد..اما اراده‌ی ساختن را هرگز.
✅
روابط عمومی شرکت فولاد خوزستان این اثر را به ساحت کلیه کارگران شریف و خستگی ناپذیر صنعت فولاد ایران علی الخصوص همکاران خود در گروه فولاد خوزستان که به حق جانفدای جبهه اقتصادی ایران عزیز هستند، پیشکش می نماید.
🎬
We Rise From Ash
📱
@khouzestan_steel_co</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654843" target="_blank">📅 17:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654842">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: ده‌ها نظامی اسرائیلی همچنان در امارات هستند
🔹
این نیروها در اوایل ماه مارس برای اداره و حفاظت از سامانه‌های گنبد آهنین که رژیم اسرائیل به این کشور فرستاده بود، اعزام شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/654842" target="_blank">📅 17:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654841">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860b737f92.mp4?token=Y_4fWYh-qHkNUMZOnv9pKwBtKdTWGLj4o0dDPBlS2qDbVH9mhhan0rLVH775PyVfWSZdTZoeJhlczHRAXUEQA0uOlBqUZMXgdU5V3w7sY5yp9u6WdRIOFGpbXNq5ZuANlCnQ5EXh3oJUHt6hd5P08LX2FLR2h01VT1WpnLs9w0wfnKB9SUWhQJDQM9xbZHC4Xx5WK6vFoPi3x9dFcORg2TriZRB2KLxTkxjbhn48iv6XcwHmEj9szx2_IXv_FmLD8diDvXlFEtKkOi1B1IHphhDPTCSWE-EV15zUiVW6T4hgl9QRr99GL31xkkftm_wVBqT25J82REJfApHxA-ZxZlxyJnFib8JkWwcfCjH4NKmD3QfisAfJTi1xcAoNKknmL6O_2PPmoDF4yRHjmZ9Aa6lidNcQju2JnM9KJrzJPumUG7YR_NUMK4d-R9F8HyluuBzRNxJMfv3O5gjeCQImtESQxKsRxnHbcgTfcsROyu8H2TsuRZA2Y_sAAcN9odWYtuM_t3BMW4M5vLMkyQMB_YS8txuXDKZp77IO4pohh8jQ62T02NOfmH0tVVdDvBb_mzEcymNeZQRnITLIdAzWqgfD0SUEbq6yfFjjTo8N0b-munLnWCIjnDSlF3OdvhMXCtisM6XEHwCAXXu2qtrjqxMBKlycc2hhGcLakCBbLr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860b737f92.mp4?token=Y_4fWYh-qHkNUMZOnv9pKwBtKdTWGLj4o0dDPBlS2qDbVH9mhhan0rLVH775PyVfWSZdTZoeJhlczHRAXUEQA0uOlBqUZMXgdU5V3w7sY5yp9u6WdRIOFGpbXNq5ZuANlCnQ5EXh3oJUHt6hd5P08LX2FLR2h01VT1WpnLs9w0wfnKB9SUWhQJDQM9xbZHC4Xx5WK6vFoPi3x9dFcORg2TriZRB2KLxTkxjbhn48iv6XcwHmEj9szx2_IXv_FmLD8diDvXlFEtKkOi1B1IHphhDPTCSWE-EV15zUiVW6T4hgl9QRr99GL31xkkftm_wVBqT25J82REJfApHxA-ZxZlxyJnFib8JkWwcfCjH4NKmD3QfisAfJTi1xcAoNKknmL6O_2PPmoDF4yRHjmZ9Aa6lidNcQju2JnM9KJrzJPumUG7YR_NUMK4d-R9F8HyluuBzRNxJMfv3O5gjeCQImtESQxKsRxnHbcgTfcsROyu8H2TsuRZA2Y_sAAcN9odWYtuM_t3BMW4M5vLMkyQMB_YS8txuXDKZp77IO4pohh8jQ62T02NOfmH0tVVdDvBb_mzEcymNeZQRnITLIdAzWqgfD0SUEbq6yfFjjTo8N0b-munLnWCIjnDSlF3OdvhMXCtisM6XEHwCAXXu2qtrjqxMBKlycc2hhGcLakCBbLr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این لابی‌ها مانع ارتباط مطلوب ایران و آمریکا می‌شوند!
🔹
در آمریکا لابی‌های پرقدرتی وجود دارد که اساس سیاست خارجی آنها را شکل می‌دهند. دو لابی به شدت قدرتمند که جنگ با ایران از دل همین‌ها طرح‌ریزی شد.
🔹
کدام لابی‌ها؟ ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/654841" target="_blank">📅 17:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654840">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2ieizoR4qkX9ntX9EthEyh3FxRk8MjhG1V-FMM2Mr56ivoetuTt1s_TLhKUApO6IUzp0cxx-8_ctDR62HcmLga_v0FkvB_GZs_sy3AtAQHL5yMKOH8bYttalKUFbuWhVo-9Ap24zm5vbr1B_Z29AN22XXIg2ob8Psrs8LLvdSA32OqL_tjaB7Us9gabiCY-DLU9O4vflHOURxa9jvBhmSjgVmNF2kIgs47tpSaQQx32Tb-YFwCvEjMxHACoJYtKZQ9f_LkGl1xD4q-eWPTZCZvBIlJ4T7aZNenh4vV5f85eC9Q1cDtbXmvQSCAEQ2kSzpxsaKcv8s_YNH82phecQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۸ درصدی ذخایر نفت جهان
🔹
آمارهای ثبت‌شده حاکی از آن است که ذخایر نفت جهان که در هفته‌های دهم تا دوازدهم سال جاری میلادی در قله حدودی ۲ میلیارد و ۷۸۰ میلیون بشکه قرار داشت، با یک شیب تند و بی‌وقفه در مسیر نزولی قرار گرفته است.
🔹
طی تنها ۱۰ هفته این ذخایر با خروج و مصرف بالغ بر ۲۲۰ میلیون بشکه، به سطح ۲ میلیارد و ۵۶۰ میلیون بشکه سقوط کرده‌اند. دنیا همچنان تشنه نفت است و تقاضای فزاینده جهانی برای جبران کمبود عرضه، با سرعت در حال بلعیدن ذخایر روی خشکی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/654840" target="_blank">📅 17:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654839">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
با اعلام سازمان لیگ: باشگاه‌ها براساس جدول لیگ به آسیا معرفی می شوند
مدیرعامل پرسپولیس تا ریاست جمهوری هم رفت! اما پرسپولیس به آسیا نمی‌رود
دبیر سازمان لیگ:
🔹
ادامه مسابقات ممکن نبود، طبق قانون و عرف به جدول ثابت شده رجوع کردیم.
· پیمان حدادی، مدیرعامل پرسپولیس، تا نهاد ریاست جمهوری هم برای دفاع از حقوق باشگاه پیش رفت و با انتخاب پیشکسوتانی مثل محسن خلیلی، برای حفظ جایگاه باشگاه تلاش زیادی کرد.
🔹
اما پرسپولیس در رتبه ششم است، بنابراین نمی‌تواند به آسیا برود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/654839" target="_blank">📅 17:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654838">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvIJlxVSwv-XIaaZXq-hZiAiVnqSbJk-U3jbNuUQqBa-rpVtGTwKH7E0OYxTuMbKPoPRpUYoFjP90zmmMEDJ--gzhqF20cUjGgAZ7vpd0VBOdul54tyboR1L32RkeTlHJ4E9EGAeSjYTsEeabjXLakodjg5NQFfxaGRGrEgy-5lwYag8J4EnNH22pmVrIO_Vqmu5Pb35FKb50wC-vgzU0mTscUjKfsly_rTj4Npg1WGlDXipIk5Fa05ZtXSDYqUASm2RfbSiLzTa9SGw1nsJP6h1p1WQy8cXd5r_S_Kd5jNZWQkgrfyOdh67IVCEREuBiVhTCQAvQxtkr7YnRsYICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن با دلار ارزانتر از ۹ سال پیش شد
🔹
میانگین نرخ دلاری هر متر مسکن در تهران از ابتدای سال ۱۴۰۵ به حدود ۱۱۰۰ دلار رسیده است. این شاخص از ابتدای سال ۱۳۹۵ حدود ۱۱۹۰ دلار بود. یعنی مسکن امروز به دلار آزاد، از ۹ سال پیش هم ارزانتر شده است.
🔹
در شرایط تورم شدید، مسکن همیشه پناهگاه امن سرمایه بوده و این تقاضای اضافی می‌تواند قیمت دلاری را بالا ببرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/654838" target="_blank">📅 17:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIFmuRuTpcFoR0jmISQtBDmxZoo2F6jlfidcMNsta_LQENhopTsTWV7BI_rMsSW7EnqJqt4eJ-j8y2FcN8UzIXaqiH6Gd2Sz8vcnTcmgegLG3mWock96x7ZNFAFBaHIbmHgA56Af_sC5UN_HFYcYbFT9Kr9a5TwKZ11tEttXZ1OfUCCm6gD192f2StJ4slLW_U3wvmtnKBZU_VJ3fWCOB9bOCQTbjR1l93G8w2Q--szGSHZDLG0kJSg3HtN_mHvgz3RIvQ3V4iTpmI-81WeqT1Cvma1bl7dSc_7IUhJRgtY6PbCZmb7W9tIy2Y4bb2pTOdJDWf2tfkY425t0KFzX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین نقشه از وضعیت جنوب لبنان پس از تحولات نظامی اخیر
اسرائیل
🔹
زرد:
منطقه تحت کنترل ارتش اسرائیل در چارچوب خط زرد
🔹
قرمز:
منطقه‌ای که ارتش اسرائیل پس از آتش‌بس به تصرف درآورده است
🔹
نارنجی:
منطقه‌ای که تحت تهدید و حملات ارتش اسرائیل است اما نیروهای زمینی به آن نرسیده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/654837" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در کشور آنفلوآنزا شیوع پیدا کرده؟
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
شیوع علائم عفونت‌های تنفسی تا ۲ خرداد در مراجعین سرپایی ۵٪ و در بستری‌ها ۷٪ گزارش شده است.
🔹
در میان افراد دارای علائم تنفسی، حدود ۸٪ مبتلا به آنفلوانزا هستند و ویروس غالب در گردش آنفلوانزای نوع B است.
🔹
طبق داده‌های نظام مراقبت، آنفلوانزای نوع B در گردش شدت یا تابلوی بالینی غیرطبیعی نسبت به حالت مورد انتظار ندارد.
🔹
برخلاف پیک قبلی که نوع A بیشتر کودکان را درگیر کرده بود، این بار درگیری بیشتر در بزرگسالان دیده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654836" target="_blank">📅 17:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk3UWEMad2Wsx1iwhNv_x4rdpSAfjNPdskxktav8sVZB6OGMpJhUjqorkZPtTcQTYSvZjsMVhgbJ-mggh4XnhUh-Ti_Xg9TQgvHdpWfXCGXYqR5jMCxpoV1kWlzbtBlle74TJFeUaS8Zq76QU-lasLlU4R-svGjEaCtuAUVubFzhyJoCGJMcv8z1R_755MEU71wQgVwSZcoUT2q95E1mRHRB4B7KNGO52ndebHB_PmWexonUZZF63J-5_egg5ls4155K5Os_Qm2n-5I2dMU5XlmngJamKeaAL1Eb3c06dfyL3-zKp546I-gAHtf9aBzlg3tpQMgWzw06AtkrIE78jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمان از مشاهدۀ یک مین دریایی در غرب تنگۀ هرمز خبر داد
مرکز امنیت دریایی عمان:
🔹
درپی مشاهده یک شیء شناور مشکوک به مین دریایی در غرب مسیر تردد ساحلی کشتی‌ها در تنگۀ هرمز و در آب‌های سرزمینی عمان، از تمامی دریانوردان، ماهیگیران و شناورها درخواست می‌شود با نهایت احتیاط در این منطقه تردد کنند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/654835" target="_blank">📅 16:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
گندم ایرانی قاچاق شد
یک منبع آگاه:
🔹
گندم کشاورزان در بازار عراق به قیمت کیلویی ۸۰ هزار تومان فروخته می‌شود؛ یعنی ۳۲ هزار تومان بالاتر از نرخ تضمینی. این اتفاق در شرایطی رخ داده که کشاورزان از فروردین‌ماه تاکنون ۱.۸ میلیون تن گندم را به سیلوهای دولتی تحویل داده‌اند، اما به گفته آن‌ها هنوز ریالی دریافت نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/654834" target="_blank">📅 16:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
افشاگری تازه بلومبرگ از تلفات نیروهای آمریکا در حمله اخیر ایران
بلومبرگ:
🔹
در جریان حمله اخیر ایران به یک پایگاه نظامی در کویت که در واکنش به نقض آتش‌بس از سوی نیروهای آمریکا صورت گرفت، چند نظامی آمریکایی زخمی شدند و ۲ فروند پهپاد ام‌کیو ۹ ریپر نیز آسیب دید.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/654833" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654832">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAo_RITspVZg0pvwNkJoMutn1sFMUk9dkCibkYpXI1zxffQurNKQyRi4hgnlfkVH9tBu1gNoIcmyGeQnsfIo7ERPJQAbwdKW9vHRX_MuDKpp8h6ILLpmMB3uyEHVy6UR0s5Bh9vdOXpds5W51Y3Z-j5pyJQZlPwOe1EIBrVOGJ4eaDN0a41xyx5Q44Ru-UOeX8xSFQklLFzci0GPz5AEejIXjAJoosgcOsKLR8d4qnYaSFcWFgOqDYRm6RCaFOE6IfeylcgNhwAijmfxvR0SnJTFdabfElygIhKwCdBXX466pNMKW16gcxTQ-gWOeRb3mN11rp-0XVgbF1Bzht-1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس امروز همه را حیرت‌زده کرد!
🔹
بازار سهام امروز صحنه یک حمله همه جانبه تمام سبز بود. ۹۹ درصد نمادها در دامنه مثبت بسته شدند و ارزش صفوف خرید در دقایق پایانی به ۲۷ همت رسید.
🔹
شاخص کل بورس با جهشی خیره کننده ۸۰ هزار واحدی در ارتفاع ۴ میلیون و ۱۵۳ هزار واحد قرار گرفت.
🔹
حقیقی‌ها هم امروز ۲.۶ همت از صندوق‌های درآمد ثابت خارج کردند و ۴.۹ همت نقدینگی تازه به بازار تزریق کردند. ارزش کل معاملات خرد نیز از مرز ۹ همت عبور کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654832" target="_blank">📅 16:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654831">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7856964316.mp4?token=oIINE-586bILRQUIKd-BhECpWQa3MczG0mAdaGczdRmTNMxCJHp4FVpI4kas2xUlfTJ_EnHUhGQY3A0-angI65_Ev0D6rI_hc2VarK2UPhF3_Z8XtgDkvJsF5buvbKOBtFvMAIFiYhR9X3scDg7Si3RZyiQEjMpSFt3QXxLZl7c_PkfXAwizYUQqS3DrWeZoLadIAyt5P30_CrXxw6pPUX-buJ1le-URFaWG_TjAKjcbfVe5jWRSRE86lrSiqttTYzag0UZSJ4eh7MkW9mNQh-JCKLGqrta2glhp3ieyEvjTRwAeC7k65sXudQXbcEeNtfLp3NWMEGPOXeMWjJxsH7DJOm5NEyJc52gyn9h-qDPQHuuQ2VVmw5KF5orU22jr-OurfwobB3OfwIc8SGHkGeyAtThIFO3FNuhP9jv1vE7k7Kw10-y8Y8ZdPuhP4nxerWEb_bgxr-x18T25ZJ_EZTOadJoPIdiQy0JL04L5ETJfQ-sIsJzll5BIp5Qy7texfwEUwhaJ-sN9aoYVzYWWW63o1uCWEbDs3Th4RHzieOvZTZlLAiHC_aGwGe4xSVnygnOfMD1Yso-07QCEUNVyK3NF-dNUglM-Et1OppbOswgol-2gpFDXU_QIQCxkqXDiVwyWsGYixAxGlcorZmzFdSo6VGNyvX1q18NJAL9H6YU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7856964316.mp4?token=oIINE-586bILRQUIKd-BhECpWQa3MczG0mAdaGczdRmTNMxCJHp4FVpI4kas2xUlfTJ_EnHUhGQY3A0-angI65_Ev0D6rI_hc2VarK2UPhF3_Z8XtgDkvJsF5buvbKOBtFvMAIFiYhR9X3scDg7Si3RZyiQEjMpSFt3QXxLZl7c_PkfXAwizYUQqS3DrWeZoLadIAyt5P30_CrXxw6pPUX-buJ1le-URFaWG_TjAKjcbfVe5jWRSRE86lrSiqttTYzag0UZSJ4eh7MkW9mNQh-JCKLGqrta2glhp3ieyEvjTRwAeC7k65sXudQXbcEeNtfLp3NWMEGPOXeMWjJxsH7DJOm5NEyJc52gyn9h-qDPQHuuQ2VVmw5KF5orU22jr-OurfwobB3OfwIc8SGHkGeyAtThIFO3FNuhP9jv1vE7k7Kw10-y8Y8ZdPuhP4nxerWEb_bgxr-x18T25ZJ_EZTOadJoPIdiQy0JL04L5ETJfQ-sIsJzll5BIp5Qy7texfwEUwhaJ-sN9aoYVzYWWW63o1uCWEbDs3Th4RHzieOvZTZlLAiHC_aGwGe4xSVnygnOfMD1Yso-07QCEUNVyK3NF-dNUglM-Et1OppbOswgol-2gpFDXU_QIQCxkqXDiVwyWsGYixAxGlcorZmzFdSo6VGNyvX1q18NJAL9H6YU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر سابق سازمان سیا(CIA): انتقام حق ایران است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/654831" target="_blank">📅 16:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654830">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czQSmFgf_zNWF0V-ImLcXzZbmKwERAJft35pkTMVIZzF9gp9wLyt9tS-0PzbyvjZmBgj56s76yC3JjR3_Nc4b87u2e3hrriU3DamUkZae6F-hg3CQAf4rhA-TmnYxe9dW6p-f5p7HqwRgeuifwmPdMThj9XGcUX4p_sV3_sQi27t2DwFX-wWahWZ40d13hxa4aRzbiIAWVChK39Ncc4AQhzqi5KhT9VJ1jma2XWSdjriozq60urtcHoag9ikaR6jonR64Pv1H0biPdF78aY7Y-vp3CnTbkjuU7oaBk4eBCGUgDVfMxXxBI9BQ0tbPPMA2vswNmwjT7zLFHbeXsxGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند خبر کوتاه از دنیای تکنولوژی #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/654830" target="_blank">📅 16:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654829">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxFXGErHjrkagnfdXQzSvev7UPcwqzP6IolDw3YFpqML9uvRj8LrzBrXMmu-h9yvkJT_VnbVeltxuK8U8yiwRtQDOU4_U_fwFyC8rFLKNkMk_4uED2ZXLbIk06kTul2iE0TZS0mVV6bEVImbH6ByTaiO6ChSzvazmjXxfLQOsH_Hd4-hdYqVkEmki8t-Cynrt3VBWfgyWP6pejE22_FcXc-hLrtOmWzjD_MKnwdHZxMZOkZ48A9kkHVcw49u80ZOdT7Va4nTFEZxzpO-vAFJDqpwuSJ4QaFTHhsir2b-7RFN3ITLotTw-xn9T7E-adPp3CIO1vwaWMltp8I8axYyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف نام یک بازیگر از پلتفرم بدلیل وطن پرستی!
آرمان درویش نوشت:
🔹
«حذف نام از پلتفرم مهم نیست، باید در یاد مردم بمانیم …تا ابد برای ایران»
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/654829" target="_blank">📅 16:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654828">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رجبی مشهدی: مشترکان خانگی که مصرف خود را در مقایسه با دوره مشابه سال قبل حداقل ۱۰ درصد کاهش دهند مشمول تخفیف تا ۳۰ درصد در بهای قبض‌های برق‌شان می‌شوند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/654828" target="_blank">📅 16:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5hLjqHB13yhSi97CtENgr2PBfrhTgJiapI0i-IwZuGg2kKcbcTLE-h3S5-NmobJz28VLG1kYuRZWyLJWycEmpbfwNhzpY2U0DL6JoSbZfvvHvafklDU9g6rReKldiGwLew-SVEcM3TLxDF-7L2ibGTKt2Pp35F0Yz2LpCLM9JAynXqsdGVoOAyUYgh-fE6CERcLEwLeglJlbx4LxNnZQxsQRKRZIjcdSMwnnG-emVgQtVEly0mZtMYITYQewnbGCMcEVCYpLYAqJpqspmvSyzO5sLLsW83HzjewUGNO-A-gUwBeSOYSMLLH6hKlFauDRZmyksUCMljiZVM_AmmDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNlDD9DWbpBTtz6CijNE9xFJ7oRVrDgugIakC4xK8yyMye8wYyI_Q7tfQxEbOS3Qyy6-UtCprHn-UxTuqgTV6ZIg4pyUcRSAhPLPi4LkPImTW04_WVmqhTAYgRiRN77MCcmFybxoIdbSCCMAU764KKPSwY_9DsPmDfSJ2wZUwpWqvnX-J5jLIDSo37JruBnkmRWOtLpKCWl6QQwtkrmbpLqJo5hgelQup3h2MZVIDcNlCUsY_GADwSDqzipIG-LsEE3J7Fstk4taSJMSRHghHQSxlR7zlxtrdsYzGThT5jKEwl1EgtOPUnPC76e5XifIpSGP_J3SLcT1hD_JBZF-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSiVFutNONm__K6Bf-YGF1HEQjUiAS_jR7D_CdLuytr5R53NHy-zCevSZEWQzx7lJ8lmHpdth45mN19ptpojbn1ZxU9N5ZPjkP9K8uzeMWqsPr9u3jMc0F93eN5Ilqw5mB2y_4zcFNVsIPRKR1uDDVfDbRyThZT4sY7FWnqoSFII9TUMajVm5s2vxf1iSZOEL1U_qzrrfbsudH05CFg4oVwoaylO8hGUUgKMrtoSaxZz9eoi3fe8G4VqsPHmTiu6tYtKBA1VLV1AWYsnEH6EdTl7-F9fPNlXyQLP4s2pw0rN-s-nIbh5RSor-T1d6pCGke-0WDN1AqPMpkg71PnYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUZvZaH8zRxrfLEPddHILOaPHcCIIAaIGMf2y9XgkeDARw6_dR27ZRJdIfm6b3xNzM2Oglrd056aDOk7iRkQP31pMXUh2De6qqV4Qa7z5bewH5TKz_kI-NBebiC2WH0EubOUIQ4KRp_GG9JdPXBtb-5fcUIoVcCpPcKq2uCaf5R2cRkcG7ApHQU-XSXKRVBrqvxDkXEGHtSVrLl_3g4IGsVjU1VE7mMr4HxNqrgO1p_5xjV1CK92KWAGP5Opr5H4mtTwAtniCcdWXBHwzRNOe_w0WODGPYEW5_joM-_JRsqqWTlZqcoIiKeHw87ADVndlzfgUMjTh-aJmVUm39aX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PG0dB1QM7OI3YU3MDRMvY00lrJjDBSZ0kOX5WLxkPfhhjGllzo6khx-HpvuDirjlJ_CMpfkOBlCJiKYRIa-8itTNSIQv79Ih5FmiCgm7UlfZhhepSXVFqnNGu5R4gn6YUz5nhZoEa_zQD5FWfjHDoLWRa-lYluAohDM-W6um99fLsaV0rd0u7jykqOUeCX7Sc2cMBjwfskRNPXL3AEq8QD9lmfqAtpkzYj4xFVoa9Ya90YVMB3bHdzJVdNstQTKlXNhwPBtIYaMcpD8xjBpc48DilsYyxrp_8hoB0TOZ2hwe4ztaz4QrF507JRL4sGL2fA4T1Ir4LrQWJcQFiPagrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پیش‌بینی‌هایی تکان‌دهنده از آینده بازار طلا و نفت
🔹
بانک‌ها و موسسات اقتصادی مطرح آخرین برآوردها و پیش‌بینی‌های خود را از بازار طلای زرد و سیاه اعلام کردن.
🔹
این پیش‌بینی‌ها را در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654823" target="_blank">📅 16:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/637b15c089.mp4?token=I0sxb0viwJqUM-Ogl34DoMm7eS8q5IMRyWMwQIbMq1tUaAnvK_6obEtmjw_Wi91gHDgov0v0CusrsK8YaIP6nR_necQKwD_REf0nS9Iq-qcgrKV_0LqweEzzBRuMnlZAny8l6UNm55jqSiVE--Kwo-otlsdB2mmYNLAywxG52AT0LrjEQykh_f04GLQeyjZXvKIy9ZttPZGQgrd9SctBDzdvam_mnGaO9GDxEs70Tcm9CADV4_reCf4iduIju9jCfS0ZxtGHTl3XI4RLqRB4pijIjbGnfsH80rsKyK4qYZxJNlXCwUamzUJZgT42f1RPlJzE7OvtBhlyD2yTJ_SUoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/637b15c089.mp4?token=I0sxb0viwJqUM-Ogl34DoMm7eS8q5IMRyWMwQIbMq1tUaAnvK_6obEtmjw_Wi91gHDgov0v0CusrsK8YaIP6nR_necQKwD_REf0nS9Iq-qcgrKV_0LqweEzzBRuMnlZAny8l6UNm55jqSiVE--Kwo-otlsdB2mmYNLAywxG52AT0LrjEQykh_f04GLQeyjZXvKIy9ZttPZGQgrd9SctBDzdvam_mnGaO9GDxEs70Tcm9CADV4_reCf4iduIju9jCfS0ZxtGHTl3XI4RLqRB4pijIjbGnfsH80rsKyK4qYZxJNlXCwUamzUJZgT42f1RPlJzE7OvtBhlyD2yTJ_SUoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست، وزیرجنگ آمریکا مدعی شد: محاصره دریایی ایران همچنان به قوت خود باقی است
🔹
ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/654822" target="_blank">📅 16:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfeQcZx0Vtr5jNaNv_v_omyoe4C4dk8C_vU0oHLdMAn9O5Gl1w9JO5S0ElUu4dTzu9iTvTov3pXSmYKTvEDomwOKVd-_AF37Cc_3wbqrICyXu6I2xPiY2szloHgMH5yA8b_5Bn1quXN7-_5N6ThG-nVbym-wmDH6xmrz0fVcypwYES0u02vwElyaiOREruW80u3CUp_E9IN0OzVMIsn2OBm4VmD8gxXHbULHJE41R4RKooWsCjJtVsRqpeevxA8hL4I7FdoVwjS_ALq-sKAMD43scs6GwbZG0fAVT06RqODkLpdku-QsZw7nwUND7CsSdWFpkhtzhrg2LPoGYJKAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: یک چهارم نفتکش‌ها مخفیانه از خلیج‌فارس فرار کردند
بلومبرگ:
🔹
تقریباً یک چهارم نفتکش‌های بزرگ غیرایرانی که در آغاز جنگ ایران در خلیج‌ فارس گرفتار شده بودند، توانسته‌اند به آرامی و مخفیانه از خلیج فارس خارج شوند.
🔹
۲۹ کشتی از ۱۰۹ کشتی بزرگتر، که قادر به حمل ۷۰۰۰۰۰ بشکه یا بیشتر هستند و هنگام بسته شدن تنگه هرمز پس از آغاز درگیری در ۲۸ فوریه، سرگردان بودند، اکنون از این گلوگاه عبور کرده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/654821" target="_blank">📅 16:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6b4dc58f.mp4?token=HZPTx_KLrw1be8A3W-Bid_YLIONDW1D-4VQOWaF8vkA9DARZh3aATK-1B0lPFHVZ-CLq39bOkzUsFXAdhi6DuODRBtU7wwrMirl0cupPJ_XfSfP9_SfxmrKqqaIdMxLtVg8V5itAczAyXwduyh1cDin68szTlKUQTGPm3IRNvN7ohmJSPpGlTPVKkt5ojG1Qav6RPKKFyp5YhBFJ1EAiOKOxrqhOP7U9fFfY6GHRvsRQNfiWR_CCSyWGdsuBu-b0rF0-Clc-FaMhw6dxyzRu8xsXoN5YlzzVDHug-EMcZ96fRoxPHb4WO6XFOfCxPr379TMPhGpa7xhsIhIW13XTFEsw48bNfGeS6xINYvhAoMdfbiBqVPPRNjV0RAwJuQy768goMapIrBwxuaPIqlhi5naO2lWXtXiGG2U9sBXS1-_Hb7F8ObkwT9dj8e09MKq6-3vM4sJGXIVORB2BJxrFlxJF7aKx9Dx5qy3nyIzclmOjnqc5XFtbsmcoYMCGKmwsolU_FWNordPHyUwDkyR0zVZ2JJEi001qFpEDd0MjtDfh1zL9KrloycPT7BpaDhTPfcqESBFvks-A3vQ0qJ_lplDw4wcbFBaaKQ_xXAbz-cK2R18latYcBsynN5Dr-RU7wZhwutERmpdg3mKPnLjv_Axp-YbHF0LmFh4SYWpj1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6b4dc58f.mp4?token=HZPTx_KLrw1be8A3W-Bid_YLIONDW1D-4VQOWaF8vkA9DARZh3aATK-1B0lPFHVZ-CLq39bOkzUsFXAdhi6DuODRBtU7wwrMirl0cupPJ_XfSfP9_SfxmrKqqaIdMxLtVg8V5itAczAyXwduyh1cDin68szTlKUQTGPm3IRNvN7ohmJSPpGlTPVKkt5ojG1Qav6RPKKFyp5YhBFJ1EAiOKOxrqhOP7U9fFfY6GHRvsRQNfiWR_CCSyWGdsuBu-b0rF0-Clc-FaMhw6dxyzRu8xsXoN5YlzzVDHug-EMcZ96fRoxPHb4WO6XFOfCxPr379TMPhGpa7xhsIhIW13XTFEsw48bNfGeS6xINYvhAoMdfbiBqVPPRNjV0RAwJuQy768goMapIrBwxuaPIqlhi5naO2lWXtXiGG2U9sBXS1-_Hb7F8ObkwT9dj8e09MKq6-3vM4sJGXIVORB2BJxrFlxJF7aKx9Dx5qy3nyIzclmOjnqc5XFtbsmcoYMCGKmwsolU_FWNordPHyUwDkyR0zVZ2JJEi001qFpEDd0MjtDfh1zL9KrloycPT7BpaDhTPfcqESBFvks-A3vQ0qJ_lplDw4wcbFBaaKQ_xXAbz-cK2R18latYcBsynN5Dr-RU7wZhwutERmpdg3mKPnLjv_Axp-YbHF0LmFh4SYWpj1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرد مرموز رسانه‌های اسرائیل؛ باراک راوید کیست؟
🔹
چرا او از تمام خبرهای محرمانه و پشت‌پرده‌های مذاکرات ایران و آمریکا خبر دارد؟
🔹
درباره باراک راوید در این ویدئو اطلاعات شگفت‌انگیزی خواهید شنید
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/654820" target="_blank">📅 15:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4bd69983.mp4?token=ZTCjEUGehuOKoqt4M389aosU4VNhWbaP3YXhVVIfsDnTKZ7QESQDPiCDdhVZXckvWeO_tw3BKVhC5syHQ6MQFLIehd7afiI8Inr35NaLQfu5y1m5lH3yD0kzkwBrdlRMz5BOpl88wIBdlMrPDwfTGXKvvAkCbxks8XZuzWynf-nGieLxH9p3s09EUX9gJq2OK2pLB1wA3F5uEE_RHsKVZISQHnZnVF2JR4RHYicQ3V91Y07jV851BFzTHFkgWnDC0ucjL-8sOY3nuW6Ea_1XAjEEsZe8549WoCwl_ubaowYJrUR2Y_B6Pj-A3M9vcvBa-_Zmzbp5A8qi7XLGLTgHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4bd69983.mp4?token=ZTCjEUGehuOKoqt4M389aosU4VNhWbaP3YXhVVIfsDnTKZ7QESQDPiCDdhVZXckvWeO_tw3BKVhC5syHQ6MQFLIehd7afiI8Inr35NaLQfu5y1m5lH3yD0kzkwBrdlRMz5BOpl88wIBdlMrPDwfTGXKvvAkCbxks8XZuzWynf-nGieLxH9p3s09EUX9gJq2OK2pLB1wA3F5uEE_RHsKVZISQHnZnVF2JR4RHYicQ3V91Y07jV851BFzTHFkgWnDC0ucjL-8sOY3nuW6Ea_1XAjEEsZe8549WoCwl_ubaowYJrUR2Y_B6Pj-A3M9vcvBa-_Zmzbp5A8qi7XLGLTgHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش دوم تجهیزات پزشکی هم به بندر ماهشهر رسید
🔹
در فاصله یک روز پس از ورود بخش اول، دومین پارت از تجهیزات پزشکی مورد نیاز بیمارستان‌های بندر ماهشهر و بندر امام خمینی(ره) اهدایی پتروشیمی امیرکبیر وارد این شهر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/654819" target="_blank">📅 15:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2YtI-zj6sDybB6Y--4zKWQRQ_lhvsChhxJyhlYpFbMvmFjAq334FXq1MU59Pc_ir6B1x_CpcxZ4gCxNYaW4mWWWvMNuMnMYmtkqw9DQu_rXKJKslXpdx1DBz5ol1--98_6AQKSrWDG3aAPFUGJ5KBI9xa5XXIXhE6o5fNk1n-qrouJmhkvsN5IqgKlfjJ8M6qZaei32Rbp-0RBQ_D2SAWhxglcQ0T8PFzSeg0dDc5r6HrW-J1hiKDE3X5c400vwRA3c4WdJ8feYQDowFJOSZPAmfOpK_E_QSjPJb8sKu2VxEESyO54lww720iZNxQJ7jSPjXzcmUfUR0MaCRf4RwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفحه‌اول وبگاه روزنامه اسرائیلی: آمریکا تازه دارد می‌فهمد که ما در موضوع ایران سرش کلاه گذاشتیم
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/654818" target="_blank">📅 15:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654817">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رجبی مشهدی: مشترکان خانگی که مصرف خود را در مقایسه با دوره مشابه سال قبل حداقل ۱۰ درصد کاهش دهند مشمول تخفیف تا ۳۰ درصد در بهای قبض‌های برق‌شان می‌شوند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/654817" target="_blank">📅 15:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654816">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV_gqrH9ezcXA40acz-k1yqm0HIC1JLLSSQJsLRL5LCpFpacQ6jc_2bwAabPCVbaNOOV6v9AhY7OcR2gSgNCl1rUAudSkVYuxC0Dkj_9iLVDmiffBQaXux_59Pv9UkKaaJ4EfhbPMixp_Ko5SybDKhvdgVC_kC7gIL4Ad58k9uCnW302L1hs2LLKwRWib-qIRl1AjYlc-Sr8BirNCijRXZsoE3WpYlnAj9cvtQtFL3ZROZSQf0NT49yk4grQJ6Vs_nzZDK_NQi2RVBYG8vWb9jrDdx_3x0VEUdRufqG_JQvI1gvmBlcoX5SE0RGdNnJe9ujLXUCxvwIxr6gk5S5nsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ جدید ایران و آمریکا در این زمان آغاز خواهد شد
🔹
توافق موقت می تواند به ترامپ زمان لازم را برای آرام کردن اوضاع در آمریکا بدهد. او همچنین، می تواند با خیال راحت به دیگر مسائل خارجی مورد علاقه اش مانند جنگ در کوبا و مساله چین و تایوان بپردازد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3218694</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/654816" target="_blank">📅 15:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654815">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edac40a70.mp4?token=tpnb_f92SKGwW6uinCkbW56GQ4Z13ybN4nUzyBp3awv1cUMLfK7AgjhU1alUJD0qG-bj2eWnjLEjcGo75d0YPjVfGP1-5hAmEGQH4EmGm2xXGhlpXZ6rfiS6bYmpP47DpBqesANDGzeOqsXQ0JOHFdH3v8Dcp_fr3_jpazGVIdpNPtxYp2Ba_tgnHsxPWX9N3ncdiCASS1i6y-XcM_13aQAkwMwxupUgDBMiKlwPvL_z1Ri8-QtsbWgTqCamdGAanRE-LjW8R4f2clIMQK5xq1Y9IVJX8yITQjpxMUhkBS7AZr2A9st92iC-4H1pEQPpQ-Ir5ZB-Eb4i_8AnT65Fnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edac40a70.mp4?token=tpnb_f92SKGwW6uinCkbW56GQ4Z13ybN4nUzyBp3awv1cUMLfK7AgjhU1alUJD0qG-bj2eWnjLEjcGo75d0YPjVfGP1-5hAmEGQH4EmGm2xXGhlpXZ6rfiS6bYmpP47DpBqesANDGzeOqsXQ0JOHFdH3v8Dcp_fr3_jpazGVIdpNPtxYp2Ba_tgnHsxPWX9N3ncdiCASS1i6y-XcM_13aQAkwMwxupUgDBMiKlwPvL_z1Ri8-QtsbWgTqCamdGAanRE-LjW8R4f2clIMQK5xq1Y9IVJX8yITQjpxMUhkBS7AZr2A9st92iC-4H1pEQPpQ-Ir5ZB-Eb4i_8AnT65Fnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنجره نما؛ ترفند جدید دکور برای دیوار خالی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/654815" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654814">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مخالفت شهید لاریجانی با راه‌اندازی موسسه و بنیاد حفظ آثار با بودجه دولتی و بیت‌المال
محمدرضا لاریجانی، فرزند شهید لاریجانی:
🔹
شهید دکتر علی لاریجانی در زمان حیات مبارک خود مکرراً نسبت به تاسیس بنیاد و یا موسسه و از این قبیل که وابسته به بودجه‌ی بیت المال باشد نهی می‌کردند.
🔹
فلذا هرگونه اقدام در این راستا مورد تایید آن شهید سعید و خانواده‌ی ایشان نمی‌باشد.
🔹
اما در خصوص کیفیت حفظ و نشر میراث فکری و عملی بنده‌ی خدا، شهید دکتر علی لاریجانی جمعی از همراهان و دوستان شهیدان لاریجانی در سازوکاری عاری از بودجه‌ و یا حمایت دولتی در حال پیگیری امور می‌باشند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/654814" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654813">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKYi5S2R2DAbcf71xmCmh5HvvBA525HmlHQYLGz0wvnt6bgpWOczmw8sk3GIYhjT0yhkY5AET0Q02uzRvmhX_ZSqFu4ArVJbLuqcG8cXodX-5l2cUu1NcwS2g0IuZztZjooXm84Vmt70Od5fgAxb66H1nuV71VVFIgWQ61QYqFMRUIfI7CQ39O16gUmmHMVo2MV6Vyeg-7g36JOxI3pjCTJqjG_utMOm-KbujOG3dGEISkxF4W1P9CjBW1BSGA1yKIjce4Y9gWc9EnTefdnMuXVuRTRPMxPG7_U79Y3Qa3qcsuMhBhF33MnB6QR6sDf8zn88C5oGyNmobxEVrPhPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سومین نقره دختران دوومیدانی ایران در قهرمانی آسیا
🔹
در ادامه بیست‌ودومین دوره مسابقات دوومیدانی قهرمانی جوانان آسیا، هانیه شه‌پری در سومین روز از این مسابقات به مدال نقره دوی ۳۰۰۰ متر رسید.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/654813" target="_blank">📅 15:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654812">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
گروسی: ما با ایران گفتگوی حداقلی داریم
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
ما گفتگو و تبادل نظر حداقلی (با ایران) داریم، اما در حال حاضر بسیار محدود است.
🔹
دیدگاه آنها (ایران) این است در حالی که درگیری ادامه دارد، زمان برای از سرگیری همکاری کامل فرا نرسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/654812" target="_blank">📅 15:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654811">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/194d328b0d.mp4?token=pucj_2fbN_e4YfT2FXTguiv1CSrJFJc8ndmbC76UFUikzfxEt8D7IA875AQDdPL08uR5i_aLKnEfoFVsAGxdLpDxBTZeZF6AKmGmW1dJOL7RTCQbLKAOlGE0WAm48rKiEcjy8xf21VEIDWDCP3TyHR13x6Z20COIAE_2J9dq_QZwmYh1bbTC8J95JlXKxFrIkZ6UIj5HDDMJ3-h6BP5k94U88rhkbXC-b-EU7K3NSkPD8_SuCcPF-XLchm2_AyboDh6F33NFT3Ow2UHq5Jha7Br5q1wyv6aPeHxZfIHqg6TQKtS3pw8DU66457AYUFey5CT115glwfuvKxt7zQyhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/194d328b0d.mp4?token=pucj_2fbN_e4YfT2FXTguiv1CSrJFJc8ndmbC76UFUikzfxEt8D7IA875AQDdPL08uR5i_aLKnEfoFVsAGxdLpDxBTZeZF6AKmGmW1dJOL7RTCQbLKAOlGE0WAm48rKiEcjy8xf21VEIDWDCP3TyHR13x6Z20COIAE_2J9dq_QZwmYh1bbTC8J95JlXKxFrIkZ6UIj5HDDMJ3-h6BP5k94U88rhkbXC-b-EU7K3NSkPD8_SuCcPF-XLchm2_AyboDh6F33NFT3Ow2UHq5Jha7Br5q1wyv6aPeHxZfIHqg6TQKtS3pw8DU66457AYUFey5CT115glwfuvKxt7zQyhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مناظره جنجالی درباره نقش حوادث ۱۸ و ۱۹ دی در تحقق جنگ ایران و اسرائیل
🔹
سعید آجورلو، استاد دانشگاه: ۱۸ و ۱۹ دی باعث شد که ترامپ بگوید حالا وقت حمله است. گفتند در جنگ ۱۲ روزه آسمان داشتیم و زمین نداشتیم؛ این نوبت از زمین شروع کنیم و بعد از آسمان بیایم، اما معکوس شد. در آمریکا جنبش «نه به پادشاه» راه افتاد و در ایران مردم برای حمایت از دفاع ملی به خیابان آمدند. اشتباهات اقتصادی و اجتماعی بود، اما توییت ترامپ که «نجات در راه است» یا فراخوان پهلوی، زمینه‌ساز حمله بود. مشخص شد سمت دیگر سلطنت‌طلبی، تجزیه ایران است.
🔹
شهرام اتفاق، فعال اپوزیسیون: مطالبات مردم با رایزنی در بالا، یا جنبش کف خیابان، یا از جنگ میسر می‌شود! من موافق گرفتن کلانتری نیستم و نمی‌دونم چه کسی آتش زده است! جنبش اجتماعی باید عاری از خشونت باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/654811" target="_blank">📅 15:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8027339a.mp4?token=FfDCY2VcmoELROx0Tjbk3Wid7baOHJD1cwaV19AKK3dvhLKxW2xRDODhxeBtz6_hwlZUiJDG-KwPrGsQ2exm63Z-qHHnGS1jWe_SoWSA6xNdjX_dMZdye0TZgMYnOKwZLbJLDLALLEQlfOYYMJ_ai8gZQ82QlYa2ElBzu6G2iKgvZhrYPYJBrJdqUSn6u_bNDiXQwTGLvyB6rs-TeF_MAe26AOeQ3MXq-LU4kaKM1e7IA9Zy6ydoyOKBCR549_MWLsBZDhilci4bIB9t3SC7HI9DrUDexYO_zYWqCXlCl3c5RGMdtmiJlIUQeKTPXwBd19RrHbfAG7519FWAMuXGZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8027339a.mp4?token=FfDCY2VcmoELROx0Tjbk3Wid7baOHJD1cwaV19AKK3dvhLKxW2xRDODhxeBtz6_hwlZUiJDG-KwPrGsQ2exm63Z-qHHnGS1jWe_SoWSA6xNdjX_dMZdye0TZgMYnOKwZLbJLDLALLEQlfOYYMJ_ai8gZQ82QlYa2ElBzu6G2iKgvZhrYPYJBrJdqUSn6u_bNDiXQwTGLvyB6rs-TeF_MAe26AOeQ3MXq-LU4kaKM1e7IA9Zy6ydoyOKBCR549_MWLsBZDhilci4bIB9t3SC7HI9DrUDexYO_zYWqCXlCl3c5RGMdtmiJlIUQeKTPXwBd19RrHbfAG7519FWAMuXGZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست، وزیرجنگ آمریکا مدعی شد: محاصره دریایی ایران همچنان به قوت خود باقی است
🔹
ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/654810" target="_blank">📅 15:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654809">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وزیر شهرسازی: تعیین سقف افزایش اجاره‌بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/654809" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پشت‌پرده پیشنهاد صندوق ۳۰۰ میلیارد دلاری آمریکا به ایران
ادعای تایمز اسرائیل:
🔹
ویتکاف و کوشنرد پیشنهاد یک صندوق سرمایه‌گذاری در ایران را در صورت دستیابی به توافق نهایی داده‌اند. دو دیپلمات که در جریان آخرین پیش‌نویس قرار گرفتند، آن را «یک صندوق سرمایه‌گذاری بین‌المللی» نامیدند.
🔹
جزئیات این صندوق در دوره مذاکرات اولیه ۶۰ روزه بین ایران و آمریکا که این تفاهم‌نامه آغاز می‌شود، مورد بحث قرار خواهد گرفت. برخی از واسطه‌ها، پیشنهاد ترویج پروژه‌های املاک و مستغلات را نیز داده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654808" target="_blank">📅 14:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm_DFLh0NKwEpgDGsvW7f-2oVpKco6lRp3-pKmb3Nzkr9EqV3vtiDIIDoGNz0DgGAHzJrmxEXrXTh6ZIFhmTL72bnFphaGvjvz_t-IUliGF1GuC8glA6-RUJHmq2ZMKYf2qaIjdz7-3ESLYdUj62gfuMNWEbCX1rlyw0uxcWl59a_yzeR_ho5DcRcyS-dGyTz3ysiTzToXOeY_6-3OmyjSqORuFuiuweHyOJURXR-GLyvESHo7w9gzpWE0bEyV-XEFT7s0CQYp9xoN1so4sIjswYxbUOFZPXdlxHduHfHLAgG9mkisFEfdkFepThhv9q0KBecc1iqkzqJ1oRPdPcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین از جمع ۱۰ دارایی برتر جهان حذف شد
🔹
تشدید ضررهای بیت‌کوین، این رمزارز را از جمع ۱۰ دارایی برتر جهان از نظر ارزش بازار خارج کرد و آن در جایگاه سیزدهم قرار داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/654807" target="_blank">📅 14:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
توقیف
اموال ۷۴ خائن به وطن ساکن خارج از کشور در گلستان
دادگستری گلستان:
🔹
اموال ۷۴ نفر از خائنین به وطن و افراد تاثیرگذار در شبکهٔ همکاران دشمن که ساکن خارج از کشور هستند به نفع مردم توقیف شد؛ اموال توقیف‌شدهٔ این افراد شامل حساب‌های بانکی، خودرو و املاک ثبتی است.
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/654806" target="_blank">📅 14:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
در شبانه‌روز گذشته ۲۰ کشتی با هماهنگی نیروی دریایی سپاه از تنگۀ هرمز  عبور کردند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/654805" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
بهار در ارتفاعات زنجان؛ دشت گل سرخه‌سنگ
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/654804" target="_blank">📅 14:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تیزر قسمت دوم، فصل چهارم
🔹
دانیال قاسمعلی روایت کرد که پس از تجربه مرگ موقت، آینده‌ای تاریک از خود دید؛ تصویری که به گفته او باعث ترک اعتیاد و تغییر جدی در مسیر زندگی‌اش شد. او این تجربه را هشداری برای بازنگری در رفتارها و ارزش‌های زندگی دانست
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: دانیال قاسمعلی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/654803" target="_blank">📅 14:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654801">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
قطر: عوارض موقت عبور از تنگه هرمز قابل مذاکره است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654801" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf0218167.mp4?token=bqKQoFVnWVsM9cI0SzOvQuYIr3COdz1FNixsG2KFNo0Tco1e7nVaXtRQy64wQhJ_Mktb5QFz29zZfii_iQ3QtbugVVuBd5FnC8EJ3Fi3eDWe43Wj6OWTJ1xcam8NiBWGe1l9m6vzxOmthbHRUa_q90UfEtnTy03tM31Lve3Y3qPeoZowOXb653azy4xNm2WH74j7FthWms-qPueyDhqBwrxibko45mZN-s0TMKRm46vZG_AxJc6IFo3NpfYKJWO-jLw6rSb3-H7KbvKopMij2VvD7PVw1FPAvMKfuoevVG62AFMWq6B5HLkBuG7hkztvFkMGjROnd7VU6ax9tsPczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf0218167.mp4?token=bqKQoFVnWVsM9cI0SzOvQuYIr3COdz1FNixsG2KFNo0Tco1e7nVaXtRQy64wQhJ_Mktb5QFz29zZfii_iQ3QtbugVVuBd5FnC8EJ3Fi3eDWe43Wj6OWTJ1xcam8NiBWGe1l9m6vzxOmthbHRUa_q90UfEtnTy03tM31Lve3Y3qPeoZowOXb653azy4xNm2WH74j7FthWms-qPueyDhqBwrxibko45mZN-s0TMKRm46vZG_AxJc6IFo3NpfYKJWO-jLw6rSb3-H7KbvKopMij2VvD7PVw1FPAvMKfuoevVG62AFMWq6B5HLkBuG7hkztvFkMGjROnd7VU6ax9tsPczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجله فرانسوی: مکرون به زنش قول داده که فکر گلشیفته رو برای همیشه از سرش بیرون کند و دیگر خیانت نکند
!
🔹
پیش‌تر ادعا شده بود که سیلی حاشیه‌ساز همسر مکرون به او به دلیل چت‌های صمیمی مکرون با گلشیفته فراهانی بوده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654800" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e46f0cb1.mp4?token=UCvZ-nOT5R6LbApTaw0B9pD0c4J4vdmD1wy_mpp4dopxWa0EY6S6xUVCcJtSQnSXNKjx1xEYcnGLof0sdhp9F32QJg5H1hNl3JbvTcbRWUy4S75e0tpPucet1xySbG2KWkUsHn5Wgkl0X7bXXMsuPXYZ9BnYIdlyJvivq3bi8gr2N_5VsN-DfwNJcUSsdbDcyvjfxUllQCjo0OybZ0Y0sjiGaymwZihmkWE5eIKZMR2qF1zAW4jsjy7ddSfArCpt2S3iuZKUEUHRI90iK3vlLm313ygOvxppwtEYxf4w3DBt00gVbNqbXNF0nDQV_-w1QSzKFg7eroK1YB6cR7Ww6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e46f0cb1.mp4?token=UCvZ-nOT5R6LbApTaw0B9pD0c4J4vdmD1wy_mpp4dopxWa0EY6S6xUVCcJtSQnSXNKjx1xEYcnGLof0sdhp9F32QJg5H1hNl3JbvTcbRWUy4S75e0tpPucet1xySbG2KWkUsHn5Wgkl0X7bXXMsuPXYZ9BnYIdlyJvivq3bi8gr2N_5VsN-DfwNJcUSsdbDcyvjfxUllQCjo0OybZ0Y0sjiGaymwZihmkWE5eIKZMR2qF1zAW4jsjy7ddSfArCpt2S3iuZKUEUHRI90iK3vlLm313ygOvxppwtEYxf4w3DBt00gVbNqbXNF0nDQV_-w1QSzKFg7eroK1YB6cR7Ww6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری فیزیکی شب گذشته هواداران پاری‌سن‌ژرمن و آرسنال در خیابان‌های بوداپست (محل برگزاری فینال لیگ قهرمانان اروپا)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/654799" target="_blank">📅 14:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPHfiVTPEgV9h1_hdGG3-XplDWY8eitrQkJSOrLkUxVwYWLpxMHVWe9zoO0kZtlwAdzAAhu1BbJw6ATRA_Yy3ex4v0REnsYBTVw_GLL5SBm-ObOboq4nbUGgc3ZzMksgV1csA_uoQXBJHX8qVUMePFfRHT4A6Gu8ClxadoxPgOH1XUVqeJWkyU7HpF4PNU1gT2HR5CaGRdHNeWSA47WKq_zEKUreU3S1U2VZX7EuVU8T5RKZOiVrZLM2-_nNb6Xx3cs8c15BMWXQXZ75bfpWAOdOxXoO9JT0R1oCtyUVNFhQBIvpQVBJv3NA0rZwzJtzHjK7rxq-ECOxmFJ_Ov1gfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۰
💻
آموزش سواد رسانه
|
#آگاهی_رسانه‌ای
| ساعت ۱۲
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها|
#فوری_کتاب
| ساعت ۲۰
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654798" target="_blank">📅 14:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مجلس فردا میزبان‌ وزیر راه خواهد بود
سخنگوی هیئت‌رئیسۀ مجلس:
🔹
یکشنبه نشست وبیناری مجلس با حضور وزیر راه و شهرسازی با محوریت بازسازی اماکن خسارت‌دیدۀ ناشی از جنگ تحمیلی سوم برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/654797" target="_blank">📅 13:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تشدید حملات اسرائیل به لبنان؛ یک محله در صور به طور گسترده تخریب شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/654796" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbHGeeIQPblOYD_61CLAOafoRdJeW_R143fJXHurRyhYFKhtp23dLsGppqQELL-yv7G1pyIlfUFr2n0Wd8Wdq34GsUZzgSBLVdGplJ3oGxIlxpyO5kKhfzBGYAkFGt0yX_sKcrsC7fKegwA81AWRrmCEVK6J4MCKupdydF3tORj1S6kIbbwXmiixK1gcps1FlAk1zXaox7nuGLtZ8dATdNDyHER9TQN5ZopSehi9yaRUavMul1bFyn43j2QldDa6kmdhDBf18zla1f-02Y0xEVvm5C5aO4dOWSUAXgblaXmgPhMON1ctc6SAy9qsTje_o1WK-2_welvftKwcONGniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ناخودآگاه یک چشم خود را می‌بندیم؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/654795" target="_blank">📅 13:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72773a59c.mp4?token=QNxY8GeVnR5cro54blRq31d-Us72kBPsLmC4c2MKmz0AP3_AM3y0Tyo1tT7cqhOilsQrwIwVmL2ePf84l4uUtzauyVOYhnpOPI2d9Ai_tL2MF7yVttf2rZDIG4SmlIO1wPFjuL7ec739Mu5wndLg2JQfmkDCxLasBJDpEIFyJqASBCM7zoUB_pVVrQ6xuZcD2XmVltritQGpXy9QPul3RClVGXJhreXg3a6gGtqHU8dPlPRq44uYtTTdm61nJbYCLgcw5kLhl3pXr9oAhYEh6OmbrJc4iLY8fpzxMF06eg0F_1Y14TzlPOEdrYb-1FQeICCJRC21EkkL94XF_rXfaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72773a59c.mp4?token=QNxY8GeVnR5cro54blRq31d-Us72kBPsLmC4c2MKmz0AP3_AM3y0Tyo1tT7cqhOilsQrwIwVmL2ePf84l4uUtzauyVOYhnpOPI2d9Ai_tL2MF7yVttf2rZDIG4SmlIO1wPFjuL7ec739Mu5wndLg2JQfmkDCxLasBJDpEIFyJqASBCM7zoUB_pVVrQ6xuZcD2XmVltritQGpXy9QPul3RClVGXJhreXg3a6gGtqHU8dPlPRq44uYtTTdm61nJbYCLgcw5kLhl3pXr9oAhYEh6OmbrJc4iLY8fpzxMF06eg0F_1Y14TzlPOEdrYb-1FQeICCJRC21EkkL94XF_rXfaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزش باد شدید در شهر مودانجیانگ در استان هیلونگجیانگ چین، بخشی از سازه سقفی یک ساختمان بلند را کند و ورق‌های فلزی بزرگ را بر روی خودروهای پارک شده در زیر آن پرتاب کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/654794" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a875a5132.mp4?token=FT7CEqc9nCGeHH_E9sYvziWkrDay1EbhauGXKkmnotKkxp2wUZgs_sUTeWgeeEp_VDP1atuhslqCsnUtDplzpZBhQRbiybRRvaFy4VHqpAwnjjqVxhK_QBr52tT9om1NRaFKFrKdeJFGS6UjsFv4Gen59uIvj5NuieXIDSTcOEoRXLH_nsioxw6fozbe3h-GdEEdQeSDTWIcj2bmqfl1VombvOxVO8py8EztaiXHh_yDwKLTF-3yA4GozGw-0iJ96oTvQQ0yh1698xPKwPP6xZEuR3ScqA6ykpoP49yxZ2164_Iv9IzwbYOLVdQgZaZpN5Km9cAqqYJApGYc31bfuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a875a5132.mp4?token=FT7CEqc9nCGeHH_E9sYvziWkrDay1EbhauGXKkmnotKkxp2wUZgs_sUTeWgeeEp_VDP1atuhslqCsnUtDplzpZBhQRbiybRRvaFy4VHqpAwnjjqVxhK_QBr52tT9om1NRaFKFrKdeJFGS6UjsFv4Gen59uIvj5NuieXIDSTcOEoRXLH_nsioxw6fozbe3h-GdEEdQeSDTWIcj2bmqfl1VombvOxVO8py8EztaiXHh_yDwKLTF-3yA4GozGw-0iJ96oTvQQ0yh1698xPKwPP6xZEuR3ScqA6ykpoP49yxZ2164_Iv9IzwbYOLVdQgZaZpN5Km9cAqqYJApGYc31bfuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکورت هوایی پوتین در آسمان آستانه از نمای کابین جنگنده قزاقستان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/654793" target="_blank">📅 13:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654791">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
معاون سازمان سنجش: تاثیر سابقه تحصیلی در کنکور امسال برای گروه‌های ریاضی، تجربی و انسانی ۶۰ درصد (۴۳ درصد پایه دوازدهم و ۱۷ درصد پایه یازدهم) و برای گروه‌های هنر و زبان ۳۰ درصد است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/654791" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654790">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اقدام ویژۀ فیفا برای کاروان ایران در مکزیک
🔹
درحالی‌که کاروان ایران برای انتقال به شهر تیخوانا برای برگزاری کمپ خود در جام جهانی آماده می‌شود، نشریۀ اکیپ فرانسه از امنیتی‌شدن فضای شهر مرزی مکزیک به‌خاطر میزبانی از این تیم خبر داد.
🔹
طبق گزارش اکیپ، ٣٠٠ نیروی امنیتی از سوی فیفا مأمور تأمین امنیت کاروان تیم ملی ایران شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/654790" target="_blank">📅 13:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654789">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc49f4bf9.mp4?token=hentuXZdJyDUVkShAJaKBcoucBcegrMg6w8-YFS744rat5AkzJ3tbFzwEgKSsfGuVnhAR_DhSwHg6Yj2kQ4r28i20U8wbPhrv7WsXLxuHvmwpxCKU3GyqJodQC9wKSi28ZA3ujGImoH4fSdET-MCp5-sz94aQXlEm_YwmTTJRkdD4X9sGLLTSpd4UPr9o-olvGFQLec4LwRl_sqWIb8DckQUUkXP-iZD1nWihKm4c0wX9tf8RnIp0s5ffBah4PrX9a9pkVqm4iUqDp721BG7WmH1aOuzlctAx4YIhlO91OuwaHyK0gPr0eXTHjHj-peUh7qvY1n86Kd8j65CWf3VDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc49f4bf9.mp4?token=hentuXZdJyDUVkShAJaKBcoucBcegrMg6w8-YFS744rat5AkzJ3tbFzwEgKSsfGuVnhAR_DhSwHg6Yj2kQ4r28i20U8wbPhrv7WsXLxuHvmwpxCKU3GyqJodQC9wKSi28ZA3ujGImoH4fSdET-MCp5-sz94aQXlEm_YwmTTJRkdD4X9sGLLTSpd4UPr9o-olvGFQLec4LwRl_sqWIb8DckQUUkXP-iZD1nWihKm4c0wX9tf8RnIp0s5ffBah4PrX9a9pkVqm4iUqDp721BG7WmH1aOuzlctAx4YIhlO91OuwaHyK0gPr0eXTHjHj-peUh7qvY1n86Kd8j65CWf3VDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هگست از اعضای AUKUS خواست هزینه‌های دفاعی را افزایش دهند
🔹
پیت هگست، وزیر جنگ آمریکا از اعضای پیمان امنیتی AUKUS شامل آمریکا، انگلیس و استرالیا و همچنین دیگر متحدان واشنگتن در منطقه خواست سهم بیشتری از هزینه‌های دفاعی و امنیتی را بر عهده بگیرند.
🔹
دوران حمایت امنیتی گسترده آمریکا از کشورهای ثروتمند بدون مشارکت کافی آن‌ها به پایان رسیده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/654789" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654786">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsDD4lxwcyaDPQbSf4eL6fR9zx9ffqGa67ClIssXXbxSx5JE282cGkZ0gFvzm66E4jCSkYzaBzkyuoRhkFHqU4hue3MjejQaLeMlYrd-MFPBulBeK41oD_QcHfOWZsyC_E_E411WIPXmdfypbMai0EFp-hK6eJTAlgZJTe2eh6CriALuvUao6slxONtVULSN-xn9c6P-H1fzsRXuX-IMAfM6qwikjiIeK79BPuNFUyI6L2foEWgrxUgU-bQU5VDozbhwSzK5F7rsTUuvrVPqZdx7-xyprrJ-HQFcjOVLw27NWhj89VOpbP48hnrYvDVmfBMcejH7YAWuBrH7jtMTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f1a9df90.mp4?token=vYVw9MWcfuvE_7gDnvdYj-gaYo4G9JclevFrybgf-OPG2VSr2z_6Y17d0R-omWUI-kU8cpHlmY_VLCvGkR5ZJb3hNwe2eAE1vrH7bBLUm6p4xpYwo7Od_x8XLiDJO_hPRF3s2feVkD7A6egLFxUL2nj1rqQAXFWqbxIFgH4p5YZg28HpcIE6pDXM28SoZxjxm5zsZAtqUrvK92aabp9v9ytAPYRGKN54mFrnCVBj8k4mvEq0v3iYMlkEcI5OLSCSy_cU1CELOT7o8xDCWOKz_B9MnAsg8ZUX8bkD8uG0vrprIeNRaeHyQ3w9XqovcNnG1gkOTnKYyZXZu6Il4Hr2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f1a9df90.mp4?token=vYVw9MWcfuvE_7gDnvdYj-gaYo4G9JclevFrybgf-OPG2VSr2z_6Y17d0R-omWUI-kU8cpHlmY_VLCvGkR5ZJb3hNwe2eAE1vrH7bBLUm6p4xpYwo7Od_x8XLiDJO_hPRF3s2feVkD7A6egLFxUL2nj1rqQAXFWqbxIFgH4p5YZg28HpcIE6pDXM28SoZxjxm5zsZAtqUrvK92aabp9v9ytAPYRGKN54mFrnCVBj8k4mvEq0v3iYMlkEcI5OLSCSy_cU1CELOT7o8xDCWOKz_B9MnAsg8ZUX8bkD8uG0vrprIeNRaeHyQ3w9XqovcNnG1gkOTnKYyZXZu6Il4Hr2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش برف در خاباروفسک روسیه در آستانه تابستان مردم را غافلگیر کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/654786" target="_blank">📅 12:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654785">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
برگزاری کنکور سراسری فقط در داخل کشور  رئیس سازمان سنجش:
🔹
کنکور سراسری و پذیرش معلم_دانشجو برای دانشگاه فرهنگیان و تربیت دبیر شهید رجایی در داخل کشور برگزار خواهد شد و آزمونی در خارج از کشور برگزار نخواهد شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/654785" target="_blank">📅 12:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654784">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FReRDVSftVNCXnyqhXOqBq1pDWSB31y9NZZPEx-s4C7XbIgMdf5Tuhli-NWeYk6H1yELOODyaTS1X4Du0KW-WEPJX_TuYe1D-x-_WGY3xoM55tiF9ehh26AKA-OvX3iBq3NqWjnHq9601F514xYtpjOOl_wJXhyPTPfNq7RAx5survfCrrkDvP4b_Y8PC5HIYO51Qne0u9A9-FyJPVQ5OhD2y2E2NAac66UNbcu3uNel6zleUIJa0eV2eUVO8iO-XoE2JwCVb7DqTriPFjeoul5RcCKlN67pnFD72qM8172Sd50ZuCasaPAbQSOJuljRfq2c8G8rV-HhoFW7-fw2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار گرمازدگی؛ آب فراوان بنوشید و منتظر تشنه شدن نمانید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/654784" target="_blank">📅 12:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654783">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
هلاکت ۲ تروریست در درگیری با مرزبانان چالدران
🔹
فرمانده مرزبانی فراجا از ناکامی حمله عناصر گروهک‌های معاند به یکی از یگان‌های مرزی چالدران خبر داد.
🔹
در این درگیری مسلحانه، ۲ تروریست کشته شدند و تعدادی دیگر پس از زخمی شدن به آن سوی مرز متواری شدند.
🔹
از مهاجمان یک قبضه سلاح M16، ۵ خشاب، ۲ نارنجک دستی، یک گوشی تلفن همراه و تجهیزات انفرادی کشف و ضبط شد.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654783" target="_blank">📅 12:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654782">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
زمان برگزاری کنکور اعلام شد
🔹
رئیس سازمان سنجش آموزش کشور از برگزاری آزمون سراسری و کنکور دانشجو معلمان در روزهای پنجشنبه و جمعه ۲۹ و ۳۰ مردادماه خبر داد.
🔹
کنکور کارشناسی ارشد ۱۴۰۵  ۱۸ و ۱۹ تیر برگزار می‌شود.  جزییات بیشتر
👇
khabarfoori.com/fa/tiny/news-3218868</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654782" target="_blank">📅 12:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654781">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jClo-f_LTYTgXvhi-SvTiFcMuQedlCNq1buTmiOhrmV5RPUA3VbwftMuAEHsQx_Rtv-Oa7EW-K5NLuadyf32FpnIXvIl7AEfxE1cneFwb76rhvN3TKna308iyvwt95DuOGHY_ELwxkoacaxdoy05PJRVZQuDQMkCUIwF2kym6o4HR2s3xQzAlExjCniwa67Bql209NfUSqQy0dZv1_c-JoifjJtV7MUyJpXl7sz8cmCD0mS9TjVYyRkrn5HUruT8WrA6CAkedSGEutSNi9BNTLye4QLh1TAzBkOB_hxbi1q5rK1OxGwuKT-XGbsn2hq37YDD7rFpGrigU1IvAT2n-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: رئیس‌جمهور آمریکا برای بار سوم درحال خیانت به دیپلماسی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654781" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654780">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4NBbYWFlE-5KkKmzvmWgXMU-f-IQ8ewhWPWurBaAOSRG8m9WrdbSnsf0AxLyNk_RiN_thb-NCq8N2-uQ-Uu7Vx62giiu7TUTmzikA80DMyVut-JFA7TCaj7850yPUAZ9rc5jJgyFm6qM6vz28TdoZVbQFnGTu2zXiSNvoz4JvFPl_mrR9u_b1XuPiBTrFccK1Krn4CAKZUkdqoWLXH9p-4lmjSyGrtuIuGC4r-yaiC9QCa_wCkLmwQiQ21AVqsLKKYn64sGjEKGNK2IHRR7rOKgPd-bHmg8N2Agza689iBIBml_HvMDxrt9Vl5Gz86_XsifUTYDtc8z8PuNWyALnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامسونگ قابلیت «پاسپورت دیجیتال» را به گوشی‌های گلکسی اضافه کرد
🔹
کاربران آمریکایی می‌توانند اطلاعات پاسپورت خود را به‌صورت رمزگذاری‌شده در Samsung Wallet ذخیره کرده و در بسیاری از فرودگاه‌های آمریکا بدون ارائه پاسپورت فیزیکی، هویت خود را تأیید کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/654780" target="_blank">📅 12:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
فراجا: زائران اربعین گذرنامه‌های زیر ۶ ماه را تعویض کنند/امکان تمدید گذرنامه به‌صورت حضوری و غیرحضوری فراهم است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654779" target="_blank">📅 11:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654778">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کشف لاشه‌های پهپاد متخاصم آمریکایی ـ صهیونی در آب‌های خلیج فارس
🔹
لاشه‌های پهپاد متخاصم منهدم‌شده ارتش صهیونیستی آمریکایی توسط دلاورمردان پدافند هوایی ارتش جمهوری اسلامی ایران مستقر در جزیره قشم کشف شد.
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/654778" target="_blank">📅 11:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654777">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
کشتی ایرانی با عبور از محاصرهٔ آمریکا
به خانه رسید
🔹
داده‌های ماهوارهای نشان ‌می‌دهد یک کشتی فله‌بر ایرانی به‌نام کیوان با عبور از محاصرهٔ دریایی آمریکا به سواحل ایران در نزدیکی بندر امام خمینی(ره) رسیده است./فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654777" target="_blank">📅 11:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654776">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aaf6b7ee2.mp4?token=LiYvT_jrhy7VY_y6pZ8eecRi7Kwwdba1JPslI7XUY7V0IdLCqC5MaDo3VNOVLUjQevpp6SASMxTmKKPYDDUA3NEZbJ7nUvjherTQ_1hyGlN-CNUYkOjD3vrLGBV1iUTMdWAGBpdr-IPdZsNmw2M3Swhzbh8E9M3kWajcV2U7pe3Ie8dBI5kOs46648nm1EmLuiQ48k1WFSC5E4u4xZqOaC_Ys3g9YBDdeqGNPn5OO1HKsuQF0WVenRFd6ORhus4zQC1MQ-CelgSvTp64oPtWhXTOZR8lSONFtp8kTHbKbXQ0R7GM3-ZMYmDfvLlOJNDPquZrknR0fBKepb90csGftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aaf6b7ee2.mp4?token=LiYvT_jrhy7VY_y6pZ8eecRi7Kwwdba1JPslI7XUY7V0IdLCqC5MaDo3VNOVLUjQevpp6SASMxTmKKPYDDUA3NEZbJ7nUvjherTQ_1hyGlN-CNUYkOjD3vrLGBV1iUTMdWAGBpdr-IPdZsNmw2M3Swhzbh8E9M3kWajcV2U7pe3Ie8dBI5kOs46648nm1EmLuiQ48k1WFSC5E4u4xZqOaC_Ys3g9YBDdeqGNPn5OO1HKsuQF0WVenRFd6ORhus4zQC1MQ-CelgSvTp64oPtWhXTOZR8lSONFtp8kTHbKbXQ0R7GM3-ZMYmDfvLlOJNDPquZrknR0fBKepb90csGftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساندویچ سرد مرغ  #آشپزی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/654776" target="_blank">📅 11:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654775">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911d825a4c.mp4?token=UhH-uigHes_vtQwdQtNtN-J4-W-_U4z_suwe1nQiLccF1bOT5A8aLl2gI7XHqfb4IEK8OrzA_BIo6KnJBN0v0tym3V25ywUvYAdaDaDGSvRROL8ezWaaSdGAWnCpiwy7rAcu96o_WSXl3NX-VeBVayxD_FVDseHUR_O6iVZ9Twl7QGyWw-4GxCqhadapkacGvktWzcGvWeB5sMxYojQ9tbNsZ1cYG46RPZKemr1BmrDPhBj8GE_7RfodMlSQ0cCr9YSs7kNbLO9Hno1HrpZCifFSWDieSOKUKBd_Dgh4TFWl3cxRs99KQOh5euUqd1jf5WlhE44GSC3Glhze4RMCJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911d825a4c.mp4?token=UhH-uigHes_vtQwdQtNtN-J4-W-_U4z_suwe1nQiLccF1bOT5A8aLl2gI7XHqfb4IEK8OrzA_BIo6KnJBN0v0tym3V25ywUvYAdaDaDGSvRROL8ezWaaSdGAWnCpiwy7rAcu96o_WSXl3NX-VeBVayxD_FVDseHUR_O6iVZ9Twl7QGyWw-4GxCqhadapkacGvktWzcGvWeB5sMxYojQ9tbNsZ1cYG46RPZKemr1BmrDPhBj8GE_7RfodMlSQ0cCr9YSs7kNbLO9Hno1HrpZCifFSWDieSOKUKBd_Dgh4TFWl3cxRs99KQOh5euUqd1jf5WlhE44GSC3Glhze4RMCJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پلیس هلند به زن باردار
🔹
در هلند گزارش شده است که یک افسر پلیس در جریان یک حادثه، دست یک زن باردار را گرفته و او را به زمین انداخته است.
🔹
بر اساس این گزارش، همسر این زن که شاهد افتادن همسر باردارش بوده، به سمت افسر پلیس حمله‌ور شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/654775" target="_blank">📅 11:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654774">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb4y4wXffPmVAw3Fe9MjBXJb8-NYFhtWGp_GvnBDAdXjSrmp_d4fD-7BDRFs__uxefBs_VBzcEHogjTBRWSP3EQ7SSbcz5TX-RhpWmH5nyQxIxPxhXV6kjyinFnogQAREmwCd0yBDFLjDzBdOwiUBBEUoEJrEuu-VsC_GGgfuHeukDnQlwF1viFTNovY9Zk1YtmYivVZ159n0wz_xgFqoHcs82j0SUrwR2oONoZj3qqUalBeG9lf7X4NSLhwfvWRCgQDat8mDAk-9Op38aBsH7DhgL41OHT4w8FzGABO-Lg0p0vZQk5PcF-ahBtuNZS6Gm6M_DGpZY7vJsvl0B0vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا موتور سیکلت وسیله نقلیه «محبوب» تهرانی‌ها شده است؟
🔹
۹ دلیل کنارگذاشتن اجباری «خودروی شخصی» و «حمل و نقل عمومی» در سفرهای درون شهری تهران توسط طبقه متوسط جامعه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/654774" target="_blank">📅 11:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654773">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2kyECA6bFZj0bL5rSUHBX72uEpLN-FNw66TFHAPkZezd0yT7qaQ_7m9B1q9J-EseyVTfWr0zO2bx6ZUkLTrpKNBWpLjCNasUDgPAlRrxaB4QDPMm21F6E45NGRXoAQ8FX9R7QLNSAXFzVv40XpQcbtUM7CqNA53HvY9v2UEApj3-IXwMmS_jOPffJtplJJwRQtq0Fa3U4R-nSRacX-g_ON2HaQhirD3uZvli6-CPsi6OTCV294-Gd4-Tp-HcNYFMJ7y92bEUT7gjLZbQ0tBOdB8VHPDkzjBdvL72LwHpqfZtzM6I5xQQdDQT2Mbdq8ZvRIlN7L3V6mCbCesIt3BvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا زمان در کودکی کندتر می‌گذرد؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/654773" target="_blank">📅 11:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDtaY3EB7aa98yi4lngcjdylX5bDIo4mnvUL1V4Dy1TQjlfdHZtJbhpMaiq96_zqSC2tQCjkXQyOGknYYfqcnrtsY9al1ASx9xCNBYZYFHgAFz3Sl9B3U-uoAksGIeF73lFNlqIUKvZkEFsUFcaA9jNaQ2asY0r-5Z0xyZg2sADbWZQ-iA4794UOVWsbM2mC1rKhOue7IDraPAzOhZanUnKqiUtxpn-3LDIf5kG1Ed3T8rsH_t0JZEOIUPa0uvBq5Rkzly5PfBuXhMIZ2m36f8uBX0UHU7QmLxA8-j43usedwOKH_8xDuRQdGxcZFm4q05t-kpKCY-vSwmB2XUE_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیۀ عالیشاه به بازماندۀ مدرسۀ میناب رسید
‌
🔹
محمد در جریان حمله به مدرسۀ میناب، خواهر خردسال و خالۀ خود را از دست داده و خود نیز دچار جراحات شدیدی شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654772" target="_blank">📅 11:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
توت‌های خیابانی را نخورید!
علوم پزشکی البرز:
🔹
شهروندان باید از خوردن میوه درختان توت در معابر پرهیز کنند.
🔹
آلودگی‌های میکروبی روی سطح میوه توت می‌تواند باعث ایجاد عفونت‌های گوارشی شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/654771" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
کارت سفر در راه است
وزارت گردشگری:
🔹
تا هفته آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔹
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
🔹
اعتبار این کارت‌ها براساس سابقه بانکی افراد و بدون سقف تعیین خواهد شد و سودی به آن تعلق نمی‌گیرد./فارس
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/654770" target="_blank">📅 11:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654768">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITozo-PRuakOBzjH1NUwivAbSD7jqqOJnpqQHrFGNPMpSJG-_6cA-qFDHblOJHBozAw-q-7u9eEATCnDEZU-InSmXUGHXrlokGV2NqWSgPkJLfggEU4Cj-SKepOH7RlQEGUWH1zdRWvxOdFhcTJNoL1hxq40VR1cTLaaJXko2Zqrc5GkeeXq2zBEy5qgEWGx9HNxYsE-7dIwS4KeLQ7tML9Xj0x2prcOQhoXJriYeGyrUTHF-dC5PxZsCCByxRnGzRqn2bQEYlwb9FuAjI7Sz6E-i4Axff26zfrXOw2z2G5BtrMNAwf3S0lHfBDuNZHPqUI0t-A0jdsE32Jl4mUaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد تاریخی بازار سهام
/
بورس ایران برای نخستین بار بدون حتی یک سهم منفی
🔹
بازار سرمایه امروز یکی از متفاوت‌ترین روزهای معاملاتی خود را پشت سر گذاشت و در اتفاقی کم‌نظیر، برای نخستین بار در تاریخ بورس ایران، در بخشی از ساعات معاملات هیچ نمادی در محدوده منفی قرار نگرفت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654768" target="_blank">📅 11:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266a2532fd.mp4?token=FBtf0EtSKTJL2V6pQFatu51EfksCyYUVPKuK_xbQVZsWmAzpxpZ7lDGiPHIFzL74sjtxUlYdUj2PJVH4ZWSGClHVysivw3IQjinnRhZmncGfClqyI4OA2rgLToQLQBfCl4k9yce0p34GXBJpTmz9E2Rpz3GH7Ab1x8xW63eoyJLe3kU1KvwNNg8JryGJlDVFnk23y56amnXB-ghsCldRZdd5a9y7bsMwb4lyz3GHMsboJoKsmqJdGNkUrIvuShCG9AtgWCnj4Da2GG593NIItMplXw6nOuCeOUPmJtrgyg4-fwuIAHxKwxg_u_tXv_-guypIlxrdx1lSBbjFYVffOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266a2532fd.mp4?token=FBtf0EtSKTJL2V6pQFatu51EfksCyYUVPKuK_xbQVZsWmAzpxpZ7lDGiPHIFzL74sjtxUlYdUj2PJVH4ZWSGClHVysivw3IQjinnRhZmncGfClqyI4OA2rgLToQLQBfCl4k9yce0p34GXBJpTmz9E2Rpz3GH7Ab1x8xW63eoyJLe3kU1KvwNNg8JryGJlDVFnk23y56amnXB-ghsCldRZdd5a9y7bsMwb4lyz3GHMsboJoKsmqJdGNkUrIvuShCG9AtgWCnj4Da2GG593NIItMplXw6nOuCeOUPmJtrgyg4-fwuIAHxKwxg_u_tXv_-guypIlxrdx1lSBbjFYVffOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رهبر شهید انقلاب به فیلم مارمولک در اولین اکران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654767" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc91pbOlp--JKmUvxpPdtLQmqfBYMHMezTkZ5AaEl_LyHkVwa_uSIOzlQLiWkj4b45tSQp4KtOyGN2iuVNi279ijAP0mMgKi09oqgLwZ2FLku6lLjhVNtK797qyPud-NGcH2GUvhSWy37CR2g1mB0Knz203SJxcliG3V_9IiGi0bh6IXjXRYymCzoVV9vaEli9aJaRIvla4h_G0h9hqvoYvS3hl1fYdGwaCOPXL1lFqwFYXRHfBUpf-EzghyKxGut05x4w6CChY4QcjUcePjbD95hnkVIxZ-CrhcEm7u_h3qST9lU7KJXJtxGGqIG81pYMcK8Qz0Sr0TtVVs6BcJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654766" target="_blank">📅 11:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZFmK_PoqMTGLOi2oZnGlqDgL_Jmqm3i31r0bGJBjbyu8GujRU7woAv7V1dOvJbg0mgURO93zRt-N9QuiFGIfsdMGsinUH84Ahr42vr2zS48IrFc74JdSvJI5883TNssHVboXJYtP7vTC_6fO6JONldPjQq2AXAycye831qtD4DaYbdgl22EAMZnDJYTbQJlhKaW3_onGrAXHGn6bYTg6C82e9-EDB8WKXzk3OxaZ4hbX0Dao85Q2ev_2qX5vkSahpncYlUkSpxIw3YX67okVGIMRtONDQWxIZQDSWYE-TayAQQPGTIBuirudiwPmV3P3QZR8r1HwdoN8c2YptBPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی هشتمین گلزن برتر جام جهانی ۲۰۲۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654765" target="_blank">📅 11:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e8cb4359.mp4?token=b0W7FH3Vxo97l77L19vUnzJ6YJwUnorU4-ro83Q0XRy7TfAmNX33Lde_fqM0hNilgdAhGY__g5GdbIJ9mL6h0n3FdjHcV-a_FI6hX_Dg6_1uIuoM5BC2AUwQbk3Gly0ovSIHub_LhYsSYOtphLZirD0upERPelLWy1Mzi1-lwtPVzk-MtILStRxJjmT4GgDGUX5w6T3AmEFabiWqz_CUwbykYn75ZiCyDwQ6px3TElMoTxBJGFdvHscCn_Xf-uQjMkN_ZN5FAd6UtyMCiP7TBK6vIg5zrnIs4rsjnP2N7SDrcz3WlT_zY0IobmWA312u93x_wLclUaS6r3XfZxjn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e8cb4359.mp4?token=b0W7FH3Vxo97l77L19vUnzJ6YJwUnorU4-ro83Q0XRy7TfAmNX33Lde_fqM0hNilgdAhGY__g5GdbIJ9mL6h0n3FdjHcV-a_FI6hX_Dg6_1uIuoM5BC2AUwQbk3Gly0ovSIHub_LhYsSYOtphLZirD0upERPelLWy1Mzi1-lwtPVzk-MtILStRxJjmT4GgDGUX5w6T3AmEFabiWqz_CUwbykYn75ZiCyDwQ6px3TElMoTxBJGFdvHscCn_Xf-uQjMkN_ZN5FAd6UtyMCiP7TBK6vIg5zrnIs4rsjnP2N7SDrcz3WlT_zY0IobmWA312u93x_wLclUaS6r3XfZxjn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واژگونی کامیون حامل مهاجران بازگشتی از پاکستان در لغمان/۱۸ نفر کشته و ۲۹ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654764" target="_blank">📅 11:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
احکام قطعی متهمان سرقت نزدیک به ۸ هزار بشکه نفت در خوزستان صادر شد
رئیس کل دادگستری خوزستان:
بر اساس حکم صادر شده، ۴ متهم اصلی هر کدام به ۱۳ سال حبس تعزیری، شلاق و رد مال معادل نفت مسروقه محکوم شدند. سه متهم دیگر پرونده نیز به حبس و مجازات‌های تکمیلی محکوم شده‌اند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654763" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354758e503.mp4?token=TnMEOGCitio7N6ea0OsAK2P1f1Np4xMHABkV3hCTMWGWTE4wCX3aKLnKdSkVSAWqBTHn97k7XcxyhsdhE0A2g8C8e6ybFAf7KAQw_4NCl22pFAIa3PIGuR1dW07nymn7Pd3aN0gTG6-B4TJ1_-qappfAyVJMOLB1joRYM4l8RV0FqIKT2lPTi4_zfcqVhjSx9qoCi6pM8_xWR-Ln0KrGOtwk6VQt6sPWcK5P_tg8v3OjWNJl-qB0IESiTNwPbs4MPSRr2a-uYeM7WwG4jr9Qx99yGqo-HluD_LXw6sLpMN_cmlm6obEqcyMKzPpc-DkLTJxS7ID8ALP0GxcpUL8qqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354758e503.mp4?token=TnMEOGCitio7N6ea0OsAK2P1f1Np4xMHABkV3hCTMWGWTE4wCX3aKLnKdSkVSAWqBTHn97k7XcxyhsdhE0A2g8C8e6ybFAf7KAQw_4NCl22pFAIa3PIGuR1dW07nymn7Pd3aN0gTG6-B4TJ1_-qappfAyVJMOLB1joRYM4l8RV0FqIKT2lPTi4_zfcqVhjSx9qoCi6pM8_xWR-Ln0KrGOtwk6VQt6sPWcK5P_tg8v3OjWNJl-qB0IESiTNwPbs4MPSRr2a-uYeM7WwG4jr9Qx99yGqo-HluD_LXw6sLpMN_cmlm6obEqcyMKzPpc-DkLTJxS7ID8ALP0GxcpUL8qqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رونالدو در تمرینات پرتغال با جت شخصی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/654762" target="_blank">📅 10:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شوهر عصبانی، همسرش را لو داد؛ ۶ سال کار با مدرک جعلی!
🔹
مردی پس از به اجرا گذاشته شدن مهریه توسط همسرش، فاش کرد که او ۶ سال با مدرک جعلی پرستاری در چند بیمارستان مشغول به کار بوده است.
🔹
بررسی‌ها نشان داد زن ۴۰ ساله هیچ مدرک مرتبطی ندارد اما در یک بیمارستان دولتی و سه بیمارستان خصوصی فعالیت کرده است. او پس از بازداشت اعتراف کرد به دلیل علاقه به پرستاری و نداشتن امکان تحصیل، با کمک یک پرستار مدرک جعلی تهیه کرده و مشغول به کار شده است.
🔹
رئیس کل سازمان نظام پرستاری نیز تأکید کرد حضور «پرستارنماها» در برخی بیمارستان‌های خصوصی قابل انکار نیست و حتی یک مورد از این تخلف هم نباید وجود داشته باشد. / ایران
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654761" target="_blank">📅 10:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f592SOl03BKW63r-kFt_alDWx7n2hklyJsjlL0zI8wytep0Mq2FRH_mfRuR4z28AD8dDlehZdf538SmvvsoZ9GqLjxYnV9thF1C9EWKm6A9dnNrZBdxRklJwKzwaaNibil_biT2HebGoX31Yfs2aCK4f7CG_uDmBFBmRCYXt1U1Ly47Id2PHAVUjZzPQI1n70_CWbPJjmMilYBufCaAAsCVrusu7juO8cbY4lRj0l8D9Yn08Ox7y3nXX9seUMAlPQmbEOM7MjNGtFWij270OdUlff4RqSAt8h-uM5YYfvY0LzXV07NEtuQGADSopZPDT-ftzjX5Jh1kYGqiKcdf0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فردی که در تصویر زیر می‌بینید به گزارش روزنامه فایننشیال تایمز مالک شبکه ایران اینترنشنال است!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/654760" target="_blank">📅 10:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huHaevfun_51sI7sb834NFszBF1Kv_IsQ9g5Ku8luh-ImWnqZwDmlYHZUHxnrteb1VXWRGxDk1I7m-4Sc6W_fsU_P6gm9P-atskvB3dJosGr_GDTo1PHzxZxdBHnpRVztiJkeaBuzYl3YovrSMdDJgOEqdX4C80q1b8NXwhkYWjBkivtzBtzUJDhFSUtWzwnQ5wjTdk7EU_9Dy-d8wHWndkbfYQc9dr_YB-Y63Ve6Qj-mbWYetdi-ptL9hysrD5otIS7HEmlJWlb8jCCupSf6Wi46mQONKfXS_aDlBRCezfSBr8fAvxp_xiFHTUf0AVQcMfzCqOhYYEkunDzOM2YHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تام هنکس و تیم آلن، صداپیشگان وودی و باز در «داستان اسباب‌بازی» طی گذر زمان
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/654759" target="_blank">📅 10:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
از امروز محدودیت‌های چک برگشتی و لحاظ شدن بدهی‌های غیرجاری وام‌های زیر ۷۰۰ میلیون تومانی در امتیاز اعتباری، پس از پایان مهلت سه‌ماهه بازگشت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654758" target="_blank">📅 10:35 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
