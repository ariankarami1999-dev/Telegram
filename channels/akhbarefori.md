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
<img src="https://cdn4.telesco.pe/file/JKgikmVwZj_ooOa_vGgHKZPqgerJri3mvV_uW79Ynyxu-LQ8UCU-Fx8vc6PktmO4UWPN1L05YWGBf3jXd-LuuIIFmiiGcq30sg6PkpOjBstc5z4msYrSQNuzzNkiawTlfApv3FGTOVNy8Z4vRLfaPJtYJL7X8tb8sIzye9fEHIJoECtfM0VZ46k9IJOZMcYNZp-RWdpnOZUPq_XBq_90X142rKrjDhD-QMVF-eq5jC71OfM8zSPJKUxJ9kEP9k7CtCSd2OlP3w9Bb7G4enNi2oU6Q-Nkne2t0oa0HJFnBM5WWF71EhOQ8-6DXwRpQjspUGbgVj9A9u4VpsewakrPYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-693425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvD4BnAhmag0KdkODtistNm02G3oZqxsLEtLNykgcQcpk5jJ7mby9rX1Dmo_F2sXeR66KMsQHgoHQOg-kOjn3UeyH8EkrbaPg8n7BNkASFKo_y2Yy9yXhk1IFvjuUQwsz0-9ERczp7WEET5NoxYHSj5VZCp3lqRQLC5N6JBCxAFVFuH-5F-_koSWsfgX2Pdo-YMf0OjcIT-jG-olEVan_nsLFwnRjzngHmqIOekII9lnt61h7TtnU-bMBctDOS5hH9Kq8NObrYDc9gYY5qCmZiFMViiYTyNqb5ac0hKlK5ZQhMzTDteq9e8iRrgKrAoK6WRoMRioxWpU4sj-DnYAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بیت‌کوین به ۲۰ میلیارد تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/693425" target="_blank">📅 16:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رئیس انجمن موبایل: با توقف پروازهای عمان، گوشی وارد کشور نمی‌شود/ بالای ۹۰ درصد موبایل مورد نیاز کشور از مسیر هوایی وارد می‌شود و بخش مهمی از این مسیر از دبی به عمان و سپس به ایران بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/693424" target="_blank">📅 16:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: به‌ محض اینکه ایران تسلیم شود، قیمت نفت به‌شدت کاهش خواهد یافت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/693423" target="_blank">📅 16:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: دیشب، ما مقدار بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از میزان نفتی که قبل از جنگ از این منطقه خارج می‌کردیم
🔹
قیمت نفت الان از دوران دولت بایدن کمتر است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/693422" target="_blank">📅 16:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1zwZm47Tb8dfl7TvQ2Duk8yyYlgw09fxCSEubbONFy_wo5yFo5FHYZfqWLxR_1ZV0FHRXXTdPKhTboxNIbVbDSAkOa3CncZ8wlhosvV6zT1JE43aCaOZO1bUrwY6hTjZEQb_3-b4BR0EuK97HQfoi1vONTZhOIsywtjCzS_MH7d3t7wXpZLTRRSIQYOWgbtQo76c_7J4KY02sJvkUfR9bzHmblgSTuy8tNfe8ex1Wdsmk0DGAE2li_hLvvHNBrdK25_XcoI-45TzP-fcNd5mgq3RxED-SyRni92UCOZeM3lNhuvUA3yXaMvele9PGkR5Z5rtik0sRyqC5n3668tAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاطمه معتمدآریا پس از دو سال دوری، طی چند روز اخیر به ایران بازگشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/693421" target="_blank">📅 16:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211153c224.mp4?token=etUDN4pxXC-v8yhau1QCl4VwGubeLtiF4MAZE5pIG890H2Rb7W8ylPi_sKxlB7-6sNYv1daTzwL0L_fQ_b4OgTt4RIcE_uuGZhnS45nLGjT1WmoUKy4Rl3HNtlYqUtyuelAq3z7HHzGg01XWhk3VAY46b1gNtjq6N0G2HSd8zhyiUPET0oTE6A1ZJsdgE73iljoq35eM2RiHaYoXtpgy1zoBNxePs2MdeE4O54WcVfsNgL4GhLoQxeFW5jkDJSzpPj2hZnpFZTiFABbSvM1Hv8ls4ztdlUEKfN_c7ucPWxFbdI2prsnwHw_OxZrrXE3lFXCPXeN0yHRjbD8hut-2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211153c224.mp4?token=etUDN4pxXC-v8yhau1QCl4VwGubeLtiF4MAZE5pIG890H2Rb7W8ylPi_sKxlB7-6sNYv1daTzwL0L_fQ_b4OgTt4RIcE_uuGZhnS45nLGjT1WmoUKy4Rl3HNtlYqUtyuelAq3z7HHzGg01XWhk3VAY46b1gNtjq6N0G2HSd8zhyiUPET0oTE6A1ZJsdgE73iljoq35eM2RiHaYoXtpgy1zoBNxePs2MdeE4O54WcVfsNgL4GhLoQxeFW5jkDJSzpPj2hZnpFZTiFABbSvM1Hv8ls4ztdlUEKfN_c7ucPWxFbdI2prsnwHw_OxZrrXE3lFXCPXeN0yHRjbD8hut-2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیارشور فوری و خونگی؛ با این روش، چند ساعت بعد آماده‌ست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/693420" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بانک مرکزی ادعای میلی را تکذیب کرد
🔹
در پی انتشار نامه‌ای از سوی یکی از پلتفرم‌های آنلاین خرید و فروش طلا با محتوای «رفع موانع دسترسی به دارایی‌های خود و آزادسازی طلای موجود در خزانه‌های بانکی»، بانک مرکزی اعلام کرد:
۱. برخلاف ادعاها و جوسازی‌های صورت گرفته در برخی کانال‌های شبکه‌های اجتماعی، در نامه مورد اشاره هیچ نام، درخواست مستقیم یا ادعایی خطاب به بانک مرکزی جمهوری اسلامی ایران مطرح نشده است.
۲. مطلب منتشر شده در فضای مجازی، در راستای انحراف افکار عمومی و القای اخبار کذب و خلاف واقع به بانک مرکزی تنظیم شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/693419" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کاریال متعلق به دشمن سعودی در استان حجه سرنگون شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/693418" target="_blank">📅 16:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس از تصویب ماده پایانی طرح تنگه هرمز و تعیین این قانون به‌عنوان مبنای نظام حاکم بر این محدوده خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/693417" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نقشه دشمن برای قطع بنزین تهران و شمال کشور در ۷۲ ساعت خنثی شد
معاون وزیر نفت:
🔹
دشمن با هدف قرار دادن تلمبه‌خانه‌ها و انبارهای نفت تهران و البرز، به‌ دنبال قطع روزانه ۹۰ میلیون لیتر انتقال فرآورده و از کار انداختن شبکه توزیع سوخت در نوار شمالی کشور ظرف ۷۲ ساعت بود؛ با تغییر آرایش خطوط لوله و اعزام هزاران نفتکش، این طرح خنثی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/693416" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32ddb527e.mp4?token=eY_uY_xhmfk_ZdvPXqpBLU60StTmeI258I3xvfTWmNhRE2TJkwdKilEISs8DZYoxMZhR074r5PTR2n2VT5-72UhU_ownIb_n6-WEFXZ9z-t0Nn1ioFv5koluD-L1LfPl77jBF6ZMttonm-sdmXxsiJeaspMJbC0dtTbozCD-yIpwNDHY7OiJBVhdKh8s-16ZxWvoO-5wi-Kih3qsu9hQy3cIWNkd7Hw42Bd6QtdYlEI0KHjBE1Xs6ErX2sflXu8-jIqPymMtg81luaJOyatptes0rlSsGanU4RR9MtbZgRooeDTzlbqY-7D7_pl9vQfluH5Pibe5aWSlfmnJieK1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32ddb527e.mp4?token=eY_uY_xhmfk_ZdvPXqpBLU60StTmeI258I3xvfTWmNhRE2TJkwdKilEISs8DZYoxMZhR074r5PTR2n2VT5-72UhU_ownIb_n6-WEFXZ9z-t0Nn1ioFv5koluD-L1LfPl77jBF6ZMttonm-sdmXxsiJeaspMJbC0dtTbozCD-yIpwNDHY7OiJBVhdKh8s-16ZxWvoO-5wi-Kih3qsu9hQy3cIWNkd7Hw42Bd6QtdYlEI0KHjBE1Xs6ErX2sflXu8-jIqPymMtg81luaJOyatptes0rlSsGanU4RR9MtbZgRooeDTzlbqY-7D7_pl9vQfluH5Pibe5aWSlfmnJieK1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلب ترحم با گریه بچه؛ وقتی مادر کودک را به عمد می‌زند تا با گریه او، پول بیشتری کاسب شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693414" target="_blank">📅 16:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df514f4855.mp4?token=TtIBSrV3G4AP5M7ZFheBPo9ngBXQ6q7y4orTx7CCXfySjC0c39oLBHhCYJRNdf9OcsheTzJgCddHxYkEly2PzsMrfFP1fSAGARRPvJWNUt6m1LQrWBmzuWziZPm6MBjrMTwXXM80RzLQFlypP-eCuHaTzNm4ZxBUIwpKcEstNC5Iwm0ClhcjqEgL5zxmfwBFLin1BM5xiySc5hMTTTdb59CwWqGMwRvghEvXAeUiXy5OzP7C5QPxG5CfRQIg8Vf8a6rRnCI7VvmOr1fMZVtZ1uRY3pDUNLyCCqaP32a0zrCJKjy1O9jA9Q7D0_3prZKG8WxVH57SgwfvMNebXuLb6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df514f4855.mp4?token=TtIBSrV3G4AP5M7ZFheBPo9ngBXQ6q7y4orTx7CCXfySjC0c39oLBHhCYJRNdf9OcsheTzJgCddHxYkEly2PzsMrfFP1fSAGARRPvJWNUt6m1LQrWBmzuWziZPm6MBjrMTwXXM80RzLQFlypP-eCuHaTzNm4ZxBUIwpKcEstNC5Iwm0ClhcjqEgL5zxmfwBFLin1BM5xiySc5hMTTTdb59CwWqGMwRvghEvXAeUiXy5OzP7C5QPxG5CfRQIg8Vf8a6rRnCI7VvmOr1fMZVtZ1uRY3pDUNLyCCqaP32a0zrCJKjy1O9jA9Q7D0_3prZKG8WxVH57SgwfvMNebXuLb6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثروتمندترین خانواده‌ها چه‌طور بچه‌هاشون رو تربیت مالی می‌کنن؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/693413" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfd3010.mp4?token=a15MlH7cVSH1wHeJcVNeYHryNAlgFUNwyW1j0iWl6_e1ZbFHA3FIQ1tEDcRRTeHzRKKmfDpQfuSSpB_5EVOWBmym4xAdVT4F_ULbMI_w2sjNsDnIRUVAzsdwmB7LMNYb8gyVcP8RyV65CLybGma0yFdDsk5_0-gJ2YEL0rurZKgvKZ6CNsJP0cacHtKj228iGUNFPYAzF3on4DUT4Y3lKC6kEJIi6R-j-V5dLBhBwSvrPgdkqC70aouNpr11zkFxZ7q5Nfz0u90zVB-qs8cnaEZU0XRHHEAnxo-C3aaFVcudPPKNOZYwLoVb5FgHQk_PzVkdmYMXqGwhnwP0axgmCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfd3010.mp4?token=a15MlH7cVSH1wHeJcVNeYHryNAlgFUNwyW1j0iWl6_e1ZbFHA3FIQ1tEDcRRTeHzRKKmfDpQfuSSpB_5EVOWBmym4xAdVT4F_ULbMI_w2sjNsDnIRUVAzsdwmB7LMNYb8gyVcP8RyV65CLybGma0yFdDsk5_0-gJ2YEL0rurZKgvKZ6CNsJP0cacHtKj228iGUNFPYAzF3on4DUT4Y3lKC6kEJIi6R-j-V5dLBhBwSvrPgdkqC70aouNpr11zkFxZ7q5Nfz0u90zVB-qs8cnaEZU0XRHHEAnxo-C3aaFVcudPPKNOZYwLoVb5FgHQk_PzVkdmYMXqGwhnwP0axgmCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تابستان را با همدلی شما گذراندیم
🌨
در سرمای زمستان هم دلگرم به قرارمان هستیم....
قرارمان برقرار است.
#مدیریت_مصرف
|
#قرار_همدلی
|
#توزیع_برق_استان_تهران</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693412" target="_blank">📅 16:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ناخدا هوشنگ صمدی: تکاور اسیر ندارد، گلوله آخر سهم خودش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693411" target="_blank">📅 15:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزیر دارایی اسرائیل: ما باید در کرانه باختری وارد جنگ شویم. باید در کرانه باختری همان کاری را انجام دهیم که در غزه انجام دادیم
/
می‌خواهم همه تروریست‌ها را بکشیم و همه سلاح‌ها را جمع‌آوری کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/693409" target="_blank">📅 15:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693408">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سخنگوی هیئت‌رئیسه مجلس: مهلت ۴۵ روزه دولت برای معرفی وزرای اطلاعات و دفاع به پایان رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/693408" target="_blank">📅 15:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693407">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff1136501.mp4?token=SZemnTFtynKdgvxG0WkpdbktUH6l6AnzPg5QeIvUsST3gavuesAsUGy3G9-7XrSwZCxjxM8Vvn74qA8kqTRsxv7WsZmgWYpSeqGK0ZMBFURbshVZzU_cgXBdlpn2v-YWYN5K9pWz0enw5Hn4UPwLBUfIOQCT6WmWP_eqDkoiwWV39wW2prZ3gSv29rWt7XdNQNDG6z1oS4igjqaSJOu5kiAZx5Hw5e5icD8iR8RURL5xkksccnUWrRXy6AyxRK5cA0t4klpuWjLOIzQxHcrPrWjlLXd5Tsid1LwUstgO5ZJYSYCDxR7VtYqNP6GvSnaj3oTXLwPbBlLVQV-hAySiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff1136501.mp4?token=SZemnTFtynKdgvxG0WkpdbktUH6l6AnzPg5QeIvUsST3gavuesAsUGy3G9-7XrSwZCxjxM8Vvn74qA8kqTRsxv7WsZmgWYpSeqGK0ZMBFURbshVZzU_cgXBdlpn2v-YWYN5K9pWz0enw5Hn4UPwLBUfIOQCT6WmWP_eqDkoiwWV39wW2prZ3gSv29rWt7XdNQNDG6z1oS4igjqaSJOu5kiAZx5Hw5e5icD8iR8RURL5xkksccnUWrRXy6AyxRK5cA0t4klpuWjLOIzQxHcrPrWjlLXd5Tsid1LwUstgO5ZJYSYCDxR7VtYqNP6GvSnaj3oTXLwPbBlLVQV-hAySiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گام تازه دانشمندان ژاپنی برای حذف کروموزوم اضافی سندروم داون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/693407" target="_blank">📅 15:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693406">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
امیرعلی اکبری از MMA خداحافظی می‌کند
🔹
علیرضا استکی از قصد امیرعلی اکبری برای خداحافظی با رشته MMA در آینده نزدیک خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/693406" target="_blank">📅 15:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693405">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33bfb381a.mp4?token=s8DwPnHjfkUB5oiY5y3tdltxvvd5mynz2Hg62Z8vqV4D_ye_4mndOnk4ljJ8mneit7V0B10_hOOi2uJGMfHC-YcTqVFLnVO3hsVSJH7Y3zPALWry46enClzZY545Oopr8oJeLKWHH4GHTsP-PafQ4jy_P5cFvILddOKJ1dgeDXjF5saV47BPoN6XL7fJmm9mviywb5uCztTmjY7-rq87s-5gh6sUsF0kJIu1MKlHchlffLS_rEXj_0nAGXuWmb3oIX6zvSRYSaM2TNuAb6AtNWVPuS5atySmY_jfLQPNAFQt1ewVga-LMlcSgkukEMP-FgMbabt_67ImX71AymKUtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33bfb381a.mp4?token=s8DwPnHjfkUB5oiY5y3tdltxvvd5mynz2Hg62Z8vqV4D_ye_4mndOnk4ljJ8mneit7V0B10_hOOi2uJGMfHC-YcTqVFLnVO3hsVSJH7Y3zPALWry46enClzZY545Oopr8oJeLKWHH4GHTsP-PafQ4jy_P5cFvILddOKJ1dgeDXjF5saV47BPoN6XL7fJmm9mviywb5uCztTmjY7-rq87s-5gh6sUsF0kJIu1MKlHchlffLS_rEXj_0nAGXuWmb3oIX6zvSRYSaM2TNuAb6AtNWVPuS5atySmY_jfLQPNAFQt1ewVga-LMlcSgkukEMP-FgMbabt_67ImX71AymKUtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا از پل ورسک در میان مه و خزان پاییز
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/693405" target="_blank">📅 15:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b8447922.mp4?token=GbA-lTFQMk8Iyf5C_DambYyYhdIgSnbQvvH3PcZ3g4vTMPr4A8uNBbemK0LNWRAv3b80LRRjfACxeZ5bybB8k5TSOfiLacscwLzbMDQYeNUfVTDOfh41IL5K1i9Bq85eaRvWs00U8pFlb22I5kOs3jKH8oXBHS7y0jT384pTEGqaYAprZ1kDyjfkFEdCyY6jchNNkuyFa7M_a6ZcijCiqCSDcJNUIOtd1TTm46TtXXkEDIzh-w2oDa4L_HaVCiOG1BlGdq3udmtzOVXHDnq64h0fLdFWg8oN49L-cziiDRtIwhSkyiF6WH5-6wFVmdfjlZHSiJmzkodsP9Jb0EwGww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b8447922.mp4?token=GbA-lTFQMk8Iyf5C_DambYyYhdIgSnbQvvH3PcZ3g4vTMPr4A8uNBbemK0LNWRAv3b80LRRjfACxeZ5bybB8k5TSOfiLacscwLzbMDQYeNUfVTDOfh41IL5K1i9Bq85eaRvWs00U8pFlb22I5kOs3jKH8oXBHS7y0jT384pTEGqaYAprZ1kDyjfkFEdCyY6jchNNkuyFa7M_a6ZcijCiqCSDcJNUIOtd1TTm46TtXXkEDIzh-w2oDa4L_HaVCiOG1BlGdq3udmtzOVXHDnq64h0fLdFWg8oN49L-cziiDRtIwhSkyiF6WH5-6wFVmdfjlZHSiJmzkodsP9Jb0EwGww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یا بودجه‌ بازسازی بدهید، یا مانع‌تراشی نکنید!
🔹
درباره واحدهای تخریب‌ شده در طول جنگ؛ اگر دولت تمکن مالی دارد، باید هزینه بازسازی واحد را مستقیماً بپردازد؛ اما اگر پولی در بساط نیست، به‌ جای حواله‌ دادن سازنده به تراکم‌های بلاتکلیف در سایر مناطق، باید با اعطای تراکم در همان ملک، پای سرمایه‌گذار را به میدان باز کند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/693403" target="_blank">📅 15:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeFYyVAP9YCAbVEIuM2wI9i-oqgerXyWdCLYWu38qNAc5z2b3EHCUukSttyQMm0ye3sl-VWrBmJ2Uc6IVS1XpmmA6TAD-S23885ii3oREiMhJvMc1Cpmhoi2Btv5b5t9oSyvgggw8ylt0FtyDv-Pd4qsKOTEqzI4Sqlkt0FgchdmpBWP4AsNENYSEf31Ds1Ijebwkt0wd7J2dy4I0SvzwJ6cNWKbH_bkHQIZ7SwmHgnrA6V8V4VM5p9YsB6CcauyaJos1x8ANvPkruts8JEnLtjUOaTHcb5BHyrlIogZDB9-4iW5PuD8TX0Uj6kLMb80g409tsu4jBvHyPglyXckPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون برنامه و بودجه مجلس: مسدودسازی پلتفرم‌ها راه‌حل مشکلات اقتصادی نیست
بهروز محبی‌ نجم‌آبادی، عضو کمیسیون برنامه، بودجه و محاسبات مجلس:
🔹
بهره‌برداری از فضای مجازی و تکنولوژی، از اهمیت بنیادینی برخوردار است و امروز تمامی کشورهایی که با نگاهی دانش‌بنیان به مسائل اقتصادی می‌نگرند، بر این حوزه تمرکز دارند.
🔹
این پلتفرم‌ها مشروط بر اینکه به‌صورت دقیق تعریف شده و دارای تأییدیه‌های لازم باشند، می‌توانند کارکرد مثبتی داشته باشند.
🔹
این پلتفرم‌ها یک فرصت هستند. مشخصات و چارچوب‌هایی که این بسترهای قانونی در بحث شفافیت و شناسایی عادلانه‌ فعالان درگاه‌ها دارند، قطعاً برای کسانی که از تسلط مناسب برخوردارند و با آموزش کافی وارد فضای مجازی می‌شوند، شرایط بهتری را نسبت به کسانی که شناخت کاملی از موضوع ندارند، فراهم خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693402" target="_blank">📅 15:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25b8c231d4.mp4?token=HMmPl-OO80ZSsxFHUKTXd9xiSv9fQb9-0TgTDEEtUJIXl3bQdlW3kdkN2NmI6Ju_WIgSKs20ru4zCDMgGOSwe3xvlzaDbvI1UgpDDps0AaMI8Krm6192XaE72Xt9w8ncVbn6SQgTw51WadBMQqt-g0DdyWLEZMUGUNlP-JIRhvOK4w-yF1HO_k_o5pPfI5WcmwGRkmcCMO1WeJfPnTWre7hXVmWZm4EywAqONVf6kuL76cmRQrdbbAygllSOiUGP_GKxksljbmEMOk1pqhk7hG4SVqf-3PxxpxpMjrTYZNX8YDh4Cj5S5-cJnQYa_d601_A9qx3hj-m-LbaIfbTTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25b8c231d4.mp4?token=HMmPl-OO80ZSsxFHUKTXd9xiSv9fQb9-0TgTDEEtUJIXl3bQdlW3kdkN2NmI6Ju_WIgSKs20ru4zCDMgGOSwe3xvlzaDbvI1UgpDDps0AaMI8Krm6192XaE72Xt9w8ncVbn6SQgTw51WadBMQqt-g0DdyWLEZMUGUNlP-JIRhvOK4w-yF1HO_k_o5pPfI5WcmwGRkmcCMO1WeJfPnTWre7hXVmWZm4EywAqONVf6kuL76cmRQrdbbAygllSOiUGP_GKxksljbmEMOk1pqhk7hG4SVqf-3PxxpxpMjrTYZNX8YDh4Cj5S5-cJnQYa_d601_A9qx3hj-m-LbaIfbTTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای مسلح ایران طی ۲ شب اخیر با کشتی‌هایی که قصد عبور از مسیرهای غیرمجاز در تنگه هرمز را داشتند، برخورد کرده‌اند. شب گذشته ۷ کشتی و شب پیش از آن ۱۲ کشتی متخلف هدف قرار گرفته‌اند
/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/693401" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1027a78d5.mp4?token=Yj7ZMOgJdl6dg9iK8swoeWM4gYHO5H7IOZ9PuP_49Tyk6PBlned8M1sMV8hSq02XOnPdE76WReDQfIcGFdWjNLjFZ8pGOORNeBQQNvbteKh8aDAZnh8ITnbGwRdSAMJswdI9bRwP93-2IrEHDsCaMElJHTjlYnSly2dyJusIe-qlv4J-WTPoue0ab-GCBxWW_ovt9ms3nS0xHqrgtb_WC2hRlbV-Mw5EX5VKd5_GP8Mo8YPuwlIm_3Wqi50JEqOi94doCNi3khDD603b_2taeWMR1tQXfu8-2Ku-G9YJw6-3_g-qvN60FXDVIavQSlD6MsspwkyPmhjZlr4_RIT7vYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1027a78d5.mp4?token=Yj7ZMOgJdl6dg9iK8swoeWM4gYHO5H7IOZ9PuP_49Tyk6PBlned8M1sMV8hSq02XOnPdE76WReDQfIcGFdWjNLjFZ8pGOORNeBQQNvbteKh8aDAZnh8ITnbGwRdSAMJswdI9bRwP93-2IrEHDsCaMElJHTjlYnSly2dyJusIe-qlv4J-WTPoue0ab-GCBxWW_ovt9ms3nS0xHqrgtb_WC2hRlbV-Mw5EX5VKd5_GP8Mo8YPuwlIm_3Wqi50JEqOi94doCNi3khDD603b_2taeWMR1tQXfu8-2Ku-G9YJw6-3_g-qvN60FXDVIavQSlD6MsspwkyPmhjZlr4_RIT7vYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک‌ لیست کامل از اسم داروها و نوع کاربردشون که مطئنم نداشتید؛ یادتون باشه قبل از استفاده حتما با پزشک مشورت کنید #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/693400" target="_blank">📅 15:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: یک نقص جدید در هواپیماهای جنجالی بوئینگ ۷۳۷ وجود دارد
⠀
🔹
روزنامه وال‌استریت ژورنال براساس اسناد شرکت بوئینگ، نقص نرم‌افزاری اعلام نشده هواپیماهای سری ۷۳۷ مکس را گزارش داد که می‌تواند هنگام فرود ایجاد اختلال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693399" target="_blank">📅 15:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پزشکیان: یک میلیون اثر تاریخی داریم، آمریکا چند اثر تاریخی دارد؟/ آن‌وقت آنها می‌خواهند ما را با این سابقه تمدنی و آثار تاریخی محو کنند!
🔹
پزشکیان: اگر منِ مسئول جرات می‌کنم که با قدرت و با صلابت حرف بزنم به پشتوانه مردم بزرگوار است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693398" target="_blank">📅 14:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq1xzzRk_fRYTZBxhCZFBeVQaPC7pm_ruYvzKJLbkgf3bYJDYct6MGAuGyiIy7DxWNGbCdNW14_9ScpPkLD8X0JG5cmSvewEfL9-wevfRqlQp_VUtGsR72D8ipOHC8K3lpgYpj0-vH-r-PjGq5jcca9mdbra0peHqNCnZxU8ivjFtKUW4N1BlmYw3N4f2A6eReVpzpPT7RGFUUGxr1VpOxuaMwvWGwjQ3MaRnIl50NBTv8pxSqq5QF80shIP4tOWlCe4dyV2RGwHCEutUcjvro6wqMktVmgv3EtffZ0xCdZtMgOHS0Rr5G9yd9eX96qKpMWjIfO3oKz2161Vc7_QRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه قالیباف به پزشکیان؛ تمدید مهلت‌های اضطرار توسط دولت غیرقانونی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/693397" target="_blank">📅 14:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنیکان شهد سبلان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkVGzJJwj0IufpiUvqI_JrX-4df9Ffk9ij5GzvgaGtSSfLClk8qpXHEg0IOccyTYyw9UkUUIlB6jsOj8O0WtOWwxNdRonlFxGjFqnX4RC5t9PhoL_XDH1EXBjx3MZnKvfM8nft5OIIdk2tkuc4gD5O-YkeTq6jvH3uEQ-bCfDAmTsSJ2spBixRlEZuboffu1lERA6i6Q0D9JDvn4bkgthK_17w-GlHHqgNzWh4zBYsJN2VUUDefx1IpRiUko2K9r-atBxUTcWISuiXICg__IovrW4eZ0oUgG1nQJi1O9cKT9wnXUBlUdsmAIxMwObyaSopycUPDP_sHjc3fZqqW07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من یک  زنبوردار ایرانی‌ام  در دامنه‌های سبلان، عسل ناب و ارگانیک تهیه می‌کنیم
🐝
⛰
عسل خــــــــــود بافت زیر قیمت همه جا
اگه تابستون اومدی اردبیل، حتماً بیا گردنه‌ی
حیران از کندوهامون دیدن کن
😍
🌿
چرا عسل ما اینقدر خاصه؟
🍯
۱۰۰٪ طبیعی و خام – همون‌طور که زنبورها ساختن
🍯
ارگانیک، سالم، بدون سم و آلودگی
🍯
قابل مصرف برای دیابتی‌ها (با مشورت پزشک)
🍯
طعم و عطری کم‌نظیر از دل کوهستان
فقط یک قاشقش کافیه تا عاشقش بشی!
😍
✨
عضویت در کانال
👇
https://t.me/+ejr3jVZOO2Y2MTM0</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693396" target="_blank">📅 14:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3268989804.mp4?token=ojwQfe3TPKlzQjIcCiizCzl63R1H-JEJ2AfO_JoIC_81cWvzHRvwkNRakGAXK8fCj7ikb3uQXWXq7nTv701Jy4qMg8a9YIW8ywZRfFinHosAhKoGce8yI2v_CvqlKYufpqECIG5DHI04ObXJUj5Y6V_j6WYm-qnFrZwBtJHJEGoN_Urukd8ZUxNtGllIBQ1CS-Wu35nT2s5EO_EC_4oZyDlKMw1vYJu7RbQ-rEnpqRmEL8-cDDXONCe6RC_qXYZ6lhe1L-sfP3D__1Qwx90IGqwXweIwOskx0QtleM9M-FeL34MOYUOKq78NZPfOVy53UL-cCCU10w59PnpQtNcNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3268989804.mp4?token=ojwQfe3TPKlzQjIcCiizCzl63R1H-JEJ2AfO_JoIC_81cWvzHRvwkNRakGAXK8fCj7ikb3uQXWXq7nTv701Jy4qMg8a9YIW8ywZRfFinHosAhKoGce8yI2v_CvqlKYufpqECIG5DHI04ObXJUj5Y6V_j6WYm-qnFrZwBtJHJEGoN_Urukd8ZUxNtGllIBQ1CS-Wu35nT2s5EO_EC_4oZyDlKMw1vYJu7RbQ-rEnpqRmEL8-cDDXONCe6RC_qXYZ6lhe1L-sfP3D__1Qwx90IGqwXweIwOskx0QtleM9M-FeL34MOYUOKq78NZPfOVy53UL-cCCU10w59PnpQtNcNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای فیاض زاهد درباره ترور سردار حاجی‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693395" target="_blank">📅 14:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
حمید رسایی به ۱۰ ماه حبس محکوم شد
🔹
آوش به نقل از اداره حقوقی مجلس مدعی شد حمید رسایی، به‌دلیل پرونده‌ای مربوط به سال ۱۴۰۲، به ۱۰ ماه حبس تعزیری محکوم و برای اجرای حکم احضار شده است.
🔹
این پرونده شامل انتشار مطلبی با عنوان «دستکاری قالیباف در اسناد مجلس»…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693394" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
با گرفتن تست الکل از ۱۰۰ نفر حاضر در یک کافه در یزد، تست ۲۱ نفرشان مثبت شده و این افراد دستگیر شدند
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693393" target="_blank">📅 14:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNC30Zn5H0mSmyl-1Vvn8LZgGSgmDu0ezhdn-b9co6QitZhyrdMXPQ78svYeQs0rNggLAH5o9AGgl9GAh20dTNZT1QGbpmJiDl8t1vhYFNFXubdYOA_dU1ltn-FPvRAIIPpRPsKZ-AobykDI_SoJF2avtK1ZwXWSTU1HVRotPJF7q-tZ5EAujxiB6pSfGN4dDXYV3xnJkjE7wtTrVF5l6MTUZJr6GA450MzP_xA0_UPiV4K4ytXQjJX9BSY6-Hb358BDxTShoUjt2dZl6G34RcmDryGnPKdPqJ03dG9uRCxlHNsjjQGlnikI81BFXsoY0JsHcAuvYEJWmuhFLpTGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعاتی قبل، پرواز ۴ هواپیمای مسافربری ایرانی به مقصد ترکیه
🔹
مطابق گزارشات، با وجود توقف پروازها در مسیرهایی مثل عراق و امارات، مسافران ایرانی می‌توانند با هواپیما راهی ا
ستانبول ترکیه، اسلام‌آباد پاکستان، کابل افغانستان، پکن چین،‌ دوشنبه تاجیکستان، ایروان ارمنستان و مسکو روسیه شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693392" target="_blank">📅 14:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: اولویت جذب معلم از طریق دانشگاه فرهنگیان و کنکور سراسری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/693391" target="_blank">📅 14:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693387">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKEYTaYHgueuOcgDTzJRObEXgBr1f9nqXHikcHyGYROv-igb6h8KxmGSI0HOkZwe8eTEirlejR6G4ZCHid3idpHvLvTx37y6mTRbirSjLbxEqgmYFo7cwdun0KJsHnLBqok6YBJTLZTofwOX7akZja1Epi8P4RSR6ZFfAnApuEhKKieiNo2qyFNmtXadmcprctUqv96yEWVO1Cn2AadkZfb25P77v27oXxYKuUmLXemJ9THuU5E9VH1hhbyZThxJchuHq0xqmTkZL7PJE4gcl3cRvMQRMVPC7apEvo3l-22Oo8A8K30XvpRKDCDBhrpHO4wxB-IjzjlIBDuhWjCBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QbjgxQcRPUJilNBuQ4KgmNP0T9N5jTWJiKOphNDzPiJV0gHtW0D47L74wfSkSOAaKG5Abka-NiHO0OylapLDGPihcoyx-Zf_kh2MKzkHxnJEKCbCL7Z5Qc_TSPp1vKA6KF6ekKUnc8CDG6u-ZovyQh8mcvllqq9H_CQ4JK59bhMuSTPqEOnEk1reKpj7JVraCOj0fedyCZ8blgkFQP-ue1QjeRvBK1eTCHYrgjGEu8ce-0zoIsiXi5EPYadHXJYRzCrd42mYYuFpdKuuTboc18TvrX5DKfLPQe9GCScPr0ULBZdaq2C1PsW2TspVitV3Jlp6uRef1e1h2uWJ7jW-NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«معادله نقدینگی در جنگ تغییر کرد»
🔹
برخلاف پیش‌بینی‌ها، برآوردها نشان می دهد رشد نقدینگی در مرداد با وجود جنگ و فشارهای ارزی نزولی شد. رشد نقطه‌به‌نقطه به ۵۴.۴٪ رسید، در حالی که بهار حدود ۵۶٪ بود.
🔹
بر اساس برآوردها حجم نقدینگی از ۱۵,۵۸۰ همت پایان اسفند با رشد ۱۹٪ در پنج ماه، به حدود ۱۸,۵۴۰ همت در پایان مرداد رسید. میانگین رشد ماهانه پنج ماه نخست ۳.۵٪ و مرداد حدود ۳٪ بود.
سه دلیل اصلی این کاهش شتاب:
۱) افزایش ذخیره قانونی بانک‌ها، مجموعاً ۱.۵ واحد درصد؛ اقدامی انقباضی و ضدتورمی.
۲) اعمال سختگیرانه‌تر کنترل مقداری ترازنامه و جریمه بانک‌های متخلف.
۳) استقراض کمتر دولت از بانک مرکزی و استفاده از حساب‌های پشتیبان
🔹
با این حال، نقدینگی به دلیل شرایط جنگی همچنان بزرگ و رشد سالانه آن بالاست بنابراین سیاست‌گذار باید خط قرمز مشخصی برای رشد نقدینگی تعیین کند و از تبدیل شوک‌های جنگی به شتاب خلق پول جلوگیری کند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/693387" target="_blank">📅 14:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693386">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تصاویر دومین زهپاد [زیرسطحی] شکار شده ارتش آمریکا در تنگهٔ هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693386" target="_blank">📅 14:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693385">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71007d9ab8.mp4?token=lGBMGDU664BLvpLTZyJVV0CdaiuGKP-CtEuHRvbsGMyd3E4bow7OHjw20Q5v5giTKolO0Gjh0ioacGFakzaJ9xj3Lkf35nN-6MWWUYI4pJT8Tz9NhtwwRKw2qkYQoNWVx-3LphabsA9D9-tP3i4VAZNjfNIRwyevJEk1AeHpkFSb23oMDEDYCJXj5R0FgenO0DoKHDDTZuCx-91-bgPHYXNg3IrKIlFkZbmRW6KZo884Ye6kJUyy_wZ259kgq_a7KN4nSIzht9C8gRMPPD5vLZ7HF6EkL2JGo3NHusTSiQ-fCIVW8bQl6cxGTqmsjwfTSCG1mIQKesMh8h6LCqJFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71007d9ab8.mp4?token=lGBMGDU664BLvpLTZyJVV0CdaiuGKP-CtEuHRvbsGMyd3E4bow7OHjw20Q5v5giTKolO0Gjh0ioacGFakzaJ9xj3Lkf35nN-6MWWUYI4pJT8Tz9NhtwwRKw2qkYQoNWVx-3LphabsA9D9-tP3i4VAZNjfNIRwyevJEk1AeHpkFSb23oMDEDYCJXj5R0FgenO0DoKHDDTZuCx-91-bgPHYXNg3IrKIlFkZbmRW6KZo884Ye6kJUyy_wZ259kgq_a7KN4nSIzht9C8gRMPPD5vLZ7HF6EkL2JGo3NHusTSiQ-fCIVW8bQl6cxGTqmsjwfTSCG1mIQKesMh8h6LCqJFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی کالابرگی خانم سخنگو با خبرنگار صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/693385" target="_blank">📅 14:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693384">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85637903c3.mp4?token=JVoi4hyv08UCJWkxNKLxxT9K8W8m8CfTVHf84GmrH_7bZhc8rzIOIMHl4pCtQZDzxmW_Vyxj00563f0QViHlRI0JincMEWL5KTTilDV108J39q3h05-AwSxOl9MZvFFrOEtdoCoE402Tp8gRzx3IrMzCy73dWAUzV6VLxfbdv2M0NfQtuC5iAXTZ7CMfEu-KYtVqX_6t0VkdiLpom9MI8v7mvnvu_e6N4XD3DIhT5tMk5tfvq-ejtkZNNvEtEWeZ9dCE0thggO1tltKSEViOZ7zc8uoZlfU2y65NFgl896aomEv2L70s0M2x-pAke25gyptA1-CeU5GYrm4KcV9jh0qpSRxNzUaMTeUk7CVoE8mR4qZE43mg1Uj7LJlBV-5ayFaeS5KJaKw2JDzPxwDqCBnsZ0qKFscCW6MbfwRgVEFRzlUVydkHEWvTCO5NI05wFgZOht1JjJLt87ctpV1juWYvO-BfPLYmK5dHBZJDU7WzZ-bWFNf9HGonGtcgeXt9Zid7c3m4aT-zvJvNuSgRRKcxURdh8leVf2mnLM84PiQcQJqHMjnS4vIVwKoSvtIhs5_R6WjNBKzHvGr1PwYwRyVdaMg-KIi7inNNkJGwPwMdO5me7Uiwql3hR3lyfOMhIo8tVmzNB94BxuTOaVMSESZRsIhvvAHqn9Q2Er4W9XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85637903c3.mp4?token=JVoi4hyv08UCJWkxNKLxxT9K8W8m8CfTVHf84GmrH_7bZhc8rzIOIMHl4pCtQZDzxmW_Vyxj00563f0QViHlRI0JincMEWL5KTTilDV108J39q3h05-AwSxOl9MZvFFrOEtdoCoE402Tp8gRzx3IrMzCy73dWAUzV6VLxfbdv2M0NfQtuC5iAXTZ7CMfEu-KYtVqX_6t0VkdiLpom9MI8v7mvnvu_e6N4XD3DIhT5tMk5tfvq-ejtkZNNvEtEWeZ9dCE0thggO1tltKSEViOZ7zc8uoZlfU2y65NFgl896aomEv2L70s0M2x-pAke25gyptA1-CeU5GYrm4KcV9jh0qpSRxNzUaMTeUk7CVoE8mR4qZE43mg1Uj7LJlBV-5ayFaeS5KJaKw2JDzPxwDqCBnsZ0qKFscCW6MbfwRgVEFRzlUVydkHEWvTCO5NI05wFgZOht1JjJLt87ctpV1juWYvO-BfPLYmK5dHBZJDU7WzZ-bWFNf9HGonGtcgeXt9Zid7c3m4aT-zvJvNuSgRRKcxURdh8leVf2mnLM84PiQcQJqHMjnS4vIVwKoSvtIhs5_R6WjNBKzHvGr1PwYwRyVdaMg-KIi7inNNkJGwPwMdO5me7Uiwql3hR3lyfOMhIo8tVmzNB94BxuTOaVMSESZRsIhvvAHqn9Q2Er4W9XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارولین لیویت سخنگوی سابق کاخ سفید: گاهی فکر می‌کنم ترامپ شاید بیشتر از مردان به حرف زنان گوش می‌دهد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693384" target="_blank">📅 14:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693383">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
دست اسرائیل رو شد: دزدی از سه محور حیاتی آب اردن
🔹
اردن با ارائه اطلاعاتی مفصل به آمریکا، سرقت اسرائیل از منابع آبی این کشور را از سه محور حیاتی افشا و رسما اعلام کرده که با این «دزدی» از مهم‌ترین منابع آبی خود، توانایی همزیستی ندارد و امنیت آبی‌اش در خطر جدی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693383" target="_blank">📅 14:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a447c8960.mp4?token=DVmODiAb26ZDWfmT5aliud7LgyaFfeGBrVBvewQk-veEZZo66frY6Hx3sVclGUDi_oaV-IdEWKUvXhUWEUeGEx9zMWvd9XNGy_5yeCYzJlf5izCkUqqk_ZLeUw_nFwiRAn8fl4Upg_cQKyoYZ9rDdhgvf4JydvfNBwL2IGyfCPFwJKn7gequNjGqmH-Z96pcRREvPxIDed7FKxXBELrrw432_tiRUj-6g9SUZH357kzCrHX6tYO5hPfNrt7VyAPbYwxbqGlVne_t-ePlNNzsfk02Wso54JK3njAvLZ1TxbfvZqmSKQZwTMIzfSuARc-nNhBHES1kPud6e9J_33Baaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a447c8960.mp4?token=DVmODiAb26ZDWfmT5aliud7LgyaFfeGBrVBvewQk-veEZZo66frY6Hx3sVclGUDi_oaV-IdEWKUvXhUWEUeGEx9zMWvd9XNGy_5yeCYzJlf5izCkUqqk_ZLeUw_nFwiRAn8fl4Upg_cQKyoYZ9rDdhgvf4JydvfNBwL2IGyfCPFwJKn7gequNjGqmH-Z96pcRREvPxIDed7FKxXBELrrw432_tiRUj-6g9SUZH357kzCrHX6tYO5hPfNrt7VyAPbYwxbqGlVne_t-ePlNNzsfk02Wso54JK3njAvLZ1TxbfvZqmSKQZwTMIzfSuARc-nNhBHES1kPud6e9J_33Baaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار دومین زهپاد [زیرسطحی] ارتش تروریستی آمریکا در تنگهٔ هرمز   نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
رزمندگان نیروی دریایی سپاه، به یاری خداوند متعال، طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک، توانستند یک فروند زهپاد پیشرفتهٔ…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693382" target="_blank">📅 14:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693381">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
همزمان با برگزاری رزمایش، دوی ماراتن ۱۰ کیلومتری امروز در بوستان ولایت برگزار شد  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693381" target="_blank">📅 14:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0DjMloPhc6RNpoeEGzAZigtG83Z3nBiZbwdWbh67R6tnIXjN3KgwNS-lPokra-HLauUZjVfoitNaAfoshz0PWdR27XXpZmyzYzYag63ufHOq8qwz2j05amD5RhIuRDAb_RrwJGllvxoKNRpMlZTvdoTSuOuzCuPxIRwkAm6beq4NBLNMoLQtbVMusE64R5YhY7Pwx8NodC-gqATRQbzmQ_fZjjKEEYa9DJOjSc8Vq1qlEiprhYuE9eLbZMQt3Ww1VvldtptOHpkafV1-0gf_lKT2eNKveh7LJwaZcpa6sKwTKVl4RWhzVlJJUKw1G1Y_G2Gi3Antd69C2pTDEKuzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داستان معجزه صندوق‌های کوچک زنان
🔹
گاهی یک صندوق کوچک، برای یک زن یعنی فرصت ادامه دادن.
🔹
زنان سیستان و بلوچستان سال‌هاست ماه‌به‌ماه، حتی با پس‌اندازهای ۵۰ یا ۲۰۰ هزار تومانی، کنار هم پول روی پول گذاشته‌اند؛ صندوق ساخته‌اند، کار کرده‌اند و از دل همین سرمایه‌های کوچک، برای خودشان و خانواده‌هایشان راهی ساخته‌اند.
🔹
بعضی از این صندوق‌ها بیش از ۱۰ سال دوام آورده‌اند. اما امروز، با کوچک‌تر شدن سفره‌ها و کم شدن ارزش پول، توانشان هم کمتر شده است.
🔹
حالا کمک ما می‌تواند دوباره جان به این صندوق‌ها بدهد. حتی یک مبلغ کوچک؛ برای صندوقی که قرار نیست فقط یک‌بار خرج شود، بلکه دوباره به کار و زندگی برمی‌گردد.
لینک دریافت کمک های مردمی
لینک دریافت کمک های مردمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693380" target="_blank">📅 14:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2NKIvAWj8BV1rz7cHg2v9NOUtTjVGmbih8xn4VOlK7K21FkUNSzv75kwr9eebNEs0vC1ORzgjLmxVdk07uMyi9527-Udl81oRgRbk6H1tzfF-CB5ojKZEBWUMyypYUbrVPs90ZvcoDlxj5ecalf-Fmi_523-3kY-1-QoPwyaVzG9ZqIBlqYvheM4neScHDAMipXWBIcbIMLfE9aUGgjDJVDE_KIZPHt48afXT4tqIf69T0HzeUhi4O6fywPUfn9hRNtYWgDLFCtAt6sRiFRJ3LTcAKh3O_w82G6LeCxqo6mAhhi6EtW-BNUtO34AzhAgYZLLZeEycsYzmq0_b7gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار دومین زهپاد [زیرسطحی] ارتش تروریستی آمریکا در تنگهٔ هرمز
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
رزمندگان نیروی دریایی سپاه، به یاری خداوند متعال، طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک، توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا را که به منظور جاسوسی در تنگهٔ هرمز فعالیت داشت، به دام بیندازند.
🔹
این زهپاد از نوع یکی از زیرسطحی های هوشمند و پیشرفته با نامRemus 600 «ریموس ۶۰۰» بوده که توسط رزمندگان نیروی دریایی سپاه به غنیمت گرفته شده و اکنون در اختیار متخصصان این نیرو، به منظور بازیابی اطلاعات آن، قرار گرفته است.
🔹
نیروی دریایی سپاه با قاطعیت اعلام میکند تنگهٔ هرمز مسدود است و در برابر تحرکات خطرناک و تردد از مسیرهای غیرمجاز در تنگهٔ هرمز، با اقتدار و بی وقفه در حال برخورد هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693379" target="_blank">📅 13:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693378">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فرمانده کل ارتش: اگر ایران تجارت نکند هیچ کس نمی‌تواند تجارت کند
سرلشکر حاتمی:
🔹
اگر قرار باشد منطقه ناامن باشد، این ناامنی برای همه خواهد بود.
🔹
تنگه هرمز، تنگه عزت و شرف ماست و اجازه داده نخواهد شد از این گلوگاه بزرگ لجستیکی، دشمنان کشور استفاده کنند، اما ملت ایران محروم باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693378" target="_blank">📅 13:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
۱۷ سال پس‌انداز برای خرید خودرو با حقوق کارگری
🔹
با حقوق ماهانه ۲۴ میلیون تومان، یک کارگر در صورت پس‌انداز کامل درآمد، برای خرید کوییک RS حدود ۳۲ ماه و برای خرید فیدلیتی الیت بیش از ۱۷ سال زمان نیاز دارد.
🔹
تورم، کاهش قدرت خرید، هزینه بالای تولید و نبود ابزارهای اعتباری مؤثر از عوامل این شکاف عنوان شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693377" target="_blank">📅 13:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693376">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام برای تار کردن بخشی از استوری
🔹
اینستاگرام قابلیت Pixel را به استوری اضافه کرده که با کمک هوش مصنوعی، بخش مشخصی از تصویر را پیکسلی می‌کند؛ کاربران می‌توانند با نوشتن پرامپت، قسمت موردنظر مثل «فرد سمت راست» را انتخاب کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693376" target="_blank">📅 13:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693373">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipY_7TJ-K4u97Jgl_R-xyKTQRfcqMre_y5Q03IG8KTXgglqx1EZ7Rt_nyROleHudXO81djCibrJicwNCihIiA0HRdkuRVYAWn8DfoTeyHMKNBhwpF0TG463NUzIj6c0IFu3JmChNYctREDcahCvXRECPJdHOEvdoeGs8Ua1bg_r1wqCYn3_aCBRB23NHna6NDIwXEX-gmHuZIYESG-FiVStYbezV9WSufXKyd83AhOgUsUW_u_8Mf1q9FiEq0rePt_hftHLJMHqX8Nd8Yl_jeVRCPSwolHyACRmBGmarNj_6BU-glGdUH7uZrzSy1iMWVqjYSvFRgpb3j3lueQ775g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d27eaee4.mp4?token=QoUkVIJy6NEWwL8wXgrrho-bDgZkZl_ibWUrZVGAWpYNAaVQJWJm2AizzcJ3rxb28-NZiLINvz7rcyXlE_VDMaPh0BUqbhud_9YkBQRYkec2hjvKreSrLoFs1UVcWnf_-Ue0G20nFeY_TAZMQujfvkivPBMM1OPW0f74dPQzJ_u_SMyungbuw0U6w3gAsufovfzOWnhtqENKQooIUUNz-g5FAbmbUWvv329lcr3eR43YS7JSZIa5jeavkpGLlr49K4cMn5uZj3Id7mq9XiJU6nbGdqZqgansgkqIpH_QkqxySB-tkX8thgLjFQS28GsqpfEfj2x4PdnPstgT03uQQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d27eaee4.mp4?token=QoUkVIJy6NEWwL8wXgrrho-bDgZkZl_ibWUrZVGAWpYNAaVQJWJm2AizzcJ3rxb28-NZiLINvz7rcyXlE_VDMaPh0BUqbhud_9YkBQRYkec2hjvKreSrLoFs1UVcWnf_-Ue0G20nFeY_TAZMQujfvkivPBMM1OPW0f74dPQzJ_u_SMyungbuw0U6w3gAsufovfzOWnhtqENKQooIUUNz-g5FAbmbUWvv329lcr3eR43YS7JSZIa5jeavkpGLlr49K4cMn5uZj3Id7mq9XiJU6nbGdqZqgansgkqIpH_QkqxySB-tkX8thgLjFQS28GsqpfEfj2x4PdnPstgT03uQQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش تگرگ‌های به اندازه توپ تنیس در برزیل
🧊
🇧🇷
🔹
در شهر سانتیاگو برزیل، بارش تگرگ‌های بزرگ به اندازه توپ تنیس به سقف شماری از خانه‌ها آسیب زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693373" target="_blank">📅 13:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693371">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی نفت ایران: بر اساس اطلاعات به‌دست‌آمده، «دشمن» برای ضربه زدن به تأسیسات نفتی کشور برنامه‌ریزی کرده است؛ اقدامی که به گفته او می‌تواند به شکل بمباران تأسیسات، تحریم یا محاصره دریایی انجام شود/ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/693371" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693370">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21a593d88.mp4?token=GH002_ElmOnz_NFNjssUzuvTPmgt0-yXH6uU2GL049FdgAMGYszloRt-xWWMCqWSH4PmATBcjr-edgaezOkCURMWQ21ovyI8TC00sBhdbZwmmxHBEg_ZyBfUmKatm5OWXcfqwM0M0FKBBj45__t_3Ftb6RI9x1MK8yhVkOjbx1V3G8LZckH6Y2gGRjI3U2gPF6DAE8i0XOsocYyneQelxad9D9J_qHdTXa2p3l6CH3gF2bob7gEDx3_7PN2-bzZ6V-aiFsZqyCIsHS745uwk4pgCwcXwd3D_qw2nL7FLunoqomQF-oxlq7h3h4wjkhMIS-yj7dWwrGbjMkB_pFDeIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21a593d88.mp4?token=GH002_ElmOnz_NFNjssUzuvTPmgt0-yXH6uU2GL049FdgAMGYszloRt-xWWMCqWSH4PmATBcjr-edgaezOkCURMWQ21ovyI8TC00sBhdbZwmmxHBEg_ZyBfUmKatm5OWXcfqwM0M0FKBBj45__t_3Ftb6RI9x1MK8yhVkOjbx1V3G8LZckH6Y2gGRjI3U2gPF6DAE8i0XOsocYyneQelxad9D9J_qHdTXa2p3l6CH3gF2bob7gEDx3_7PN2-bzZ6V-aiFsZqyCIsHS745uwk4pgCwcXwd3D_qw2nL7FLunoqomQF-oxlq7h3h4wjkhMIS-yj7dWwrGbjMkB_pFDeIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده ماده یوز «تلما» با ۴ توله در یوزکنام
🔹
با تأیید این مشاهده، تعداد یوزهای شناسایی‌شده در طبیعت کشور به ۳۱ قلاده رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693370" target="_blank">📅 13:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693369">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b2f8e404.mp4?token=WEnsErRFo1Yn3LJsmADiAEviggbIc1EIdcgZS09_8NeAObD63mmjP1X3ok7TcdgO9RxPeswUY463Z2nlJ4g3AR9_Hnz7JhwOun0XnZ1f3spqYukjilUxiF9xrAfaRqJTb-ONo7Rtnv5XbPRcSTrQHQ1sMERgueSUPicEGskAY4FWPJHKjVY_V-SDS7EwWwwtUP2NCmxiCMjCEA9aZvvbLht6oHszlTGje2bRxZbEhPxdsW61RvD-VooU0OZMov5CcpA8eP9LOckOQPyalVAul7M1ldALBmDEGvZUfp_d9_dIW-Qm_PEXhnw1qN0EJzArKWN2uZ3D_rLoPEViTyRPpwZWi7h9NBXMx96iX7ijHHAEnSjBXAHMaatBW3-zKDu6EEWIYk9yByjT92r3TdfL2FDADG9opjljnytXbzMNbpBBSKq-B6rb8dz_pgnBouHcKtljn4swfQb7amXbaHNh9iGHRmSVANlDbL1MG_R5d1ZthAkIgujHvxXeIJyWVOklHdAGrMUIBZ7FWhSs_opP8YaZVy6qwZ3QshcvQfVgRbber5gz4zkBgTsNACzrHWHirFPXV7fpF4WYIEEZ2jeOY1tRoH6U017Czf2AanrHvh9ufifUKyIB6tfjKlJQmCAn-QzNsZ31cO5yqu8cA8XE2zKKZxBW7NOn_jibtpDihBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b2f8e404.mp4?token=WEnsErRFo1Yn3LJsmADiAEviggbIc1EIdcgZS09_8NeAObD63mmjP1X3ok7TcdgO9RxPeswUY463Z2nlJ4g3AR9_Hnz7JhwOun0XnZ1f3spqYukjilUxiF9xrAfaRqJTb-ONo7Rtnv5XbPRcSTrQHQ1sMERgueSUPicEGskAY4FWPJHKjVY_V-SDS7EwWwwtUP2NCmxiCMjCEA9aZvvbLht6oHszlTGje2bRxZbEhPxdsW61RvD-VooU0OZMov5CcpA8eP9LOckOQPyalVAul7M1ldALBmDEGvZUfp_d9_dIW-Qm_PEXhnw1qN0EJzArKWN2uZ3D_rLoPEViTyRPpwZWi7h9NBXMx96iX7ijHHAEnSjBXAHMaatBW3-zKDu6EEWIYk9yByjT92r3TdfL2FDADG9opjljnytXbzMNbpBBSKq-B6rb8dz_pgnBouHcKtljn4swfQb7amXbaHNh9iGHRmSVANlDbL1MG_R5d1ZthAkIgujHvxXeIJyWVOklHdAGrMUIBZ7FWhSs_opP8YaZVy6qwZ3QshcvQfVgRbber5gz4zkBgTsNACzrHWHirFPXV7fpF4WYIEEZ2jeOY1tRoH6U017Czf2AanrHvh9ufifUKyIB6tfjKlJQmCAn-QzNsZ31cO5yqu8cA8XE2zKKZxBW7NOn_jibtpDihBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواد یحیوی، مجری ممنوع الکار صداوسیما: به من می‌گفتند تو نمی‌دانی درب شمالی صداوسیما چقدر نزدیک زندان اوین است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/693369" target="_blank">📅 13:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693368">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سخنگوی ارتش: اوضاع آمریکا در منطقه اصلا خوب نیست و ممکن است دست به حمله بزند
🔹
در صورت تجاوز نظامی مجدد، ایالات متحده آسیب‌های بیشتری می‌بیند؛ ارتش همه جوره برای نبرد با دشمن آماده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/693368" target="_blank">📅 13:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693367">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
عضو مجلس خبرگان رهبری: رهبر انقلاب پس از بمباران بیمارستان سوم از زیر آوار زخمی بیرون کشیده شد
آیت الله محسن حیدری، در گفت‌و‌گو با شبکه العربی:
🔹
آیت الله مجتبی خامنه‌ای در جریان این حمله مجروح شده و پس از آنکه مشخص شد زخمی شده و به بیمارستان منتقل شده است، سه بیمارستان در تهران نیز هدف حمله قرار گرفتند.
🔹
آیت الله خامنه‌ای در بیمارستان سوم بود و ایشان را از زیر آوار بیرون کشیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/693367" target="_blank">📅 13:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeaIVI2w64zwQeNp82P0Xwse5jXlQTltM0JV0xSTtOp0hQbSmF53vAFaKZUKgc_zhyk2rA_Q6QwLoRVm3cBA9JzTp6hl4EiyhXZqH_wRP1LOnLKXRuypZVY6Kb_OXkAnjv-eyrV0SJyQwIr51ppBgjyivIN-m1gVDzGjLlreFPST4dpVg1gXQJCkyTfJ3X-OgFsmKrFJM1qGp1gHqY03UckIQbj8YLKzxwRXJgrCoS0irXfx2tDOHoIOIr5o6juHPyUZa9pZjpR1SJO5FDeBLd9puhOqCVhkWifIiJcJtu9W_5kJLBWyZFjk1DmAWzPo9PCl-eugB1xNasADg79_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۵ مهر ۱۴۰۵؛ ساعت ۱۲:۰۰
🔹
تتر آرام گرفت و طلا کاهش جزئی داشت.
🔹
در بازار طلا، هر گرم طلای ۱۸ عیار با قیمت  ۲۳ میلیون و ۹۰۳ هزار تومان معامله شد؛ در حالی که بازار در سردرگمی و انتظار برای سیگنال و خبر بعدی به سر می‌برد تا مسیر حرکت خود را مشخص کند./تیتر تجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693365" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رئیس دانشگاه تهران: در جنگ اخیر ۲ استاد و ۵ دانشجو را از دست دادیم
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/693364" target="_blank">📅 13:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
آمریکا از امارات، ترکیه و عمان به خاطر تحریم‌های ایران تشکر کرد
گلف‌نیوز:
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا، از انگلیس، ترکیه، عمان و امارات متحده عربی به خاطر حمایت از کمپین فشار اقتصادی واشنگتن علیه ایران تشکر کرده است.
🔹
او گفت ترکیه و عمان پروازهای ماهان ایر را متوقف کرده‌اند، امارات هم پروازهای خطوط هوایی ایرانی و بانک‌های تجاری بزرگ در امارات را متوقف کرده‌اند.
🔹
بسنت از ترکیه نیز به خاطر توقف معاملات با ایران تشکر کرد. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/693363" target="_blank">📅 13:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbca6bfdc5.mp4?token=bbrjoNtqqJ-KTlNhAhF44In4wQ7cSC6qllXAqyBNg47NHyt5Vh8KwLuldrY6TNoXKqDPeBTLoON-yMnaM3C4ey2agsDjS7o8MEuTArkMVpvfBuMjEnLjH3PpaE6mMKff6JGF4NvbHeolVY8nGFx-OKd6SAVuq1ngCMdlZsYUjPRCcXx4fPoagBWeOgo8sa8PnxdBU3w3qkwHF2QBiqD-ZeHrQVX7Q_0otp0_vLsRjWi9lotA6V0ZDxcItlkPoRmQOdApH8aTS1QXwUjZ_8c3IcDlCb97euQZWoDQ8v7yvllhCGDBPTaZE2bfZPuFV3RXyVVSBclPALF-uLncecHUKQpcQoabu6GNFMytJJovTKFaLmmhclnpnRr5LZLbTd4rmlNTtK5H_RWDbjoAslC391g4DnyELSX0vRrxTkUV1vSmSCWZRCZl4MzfODRtXxW0TQR-HhP1idqzkqtv6cwHZWcvQFiHp2GV0jwBO1JQYRAVKr0bBeyCLmtTIvXhEU6wQuDkc-9mWg9SwS5ofR1vANGq_QiBYAgFxR_PLxe_CwDNCQXw55n_LH_Ax2ZWYocL8-DS1incIUABO51O9pHSmRp1Q3om2F-8BkimKvhX3iuqCWgberHtTbe4hLG_9f6XkZNZkAYAX5BZaEhnfKnt1sraDMlZc50pw-1bzhf657o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbca6bfdc5.mp4?token=bbrjoNtqqJ-KTlNhAhF44In4wQ7cSC6qllXAqyBNg47NHyt5Vh8KwLuldrY6TNoXKqDPeBTLoON-yMnaM3C4ey2agsDjS7o8MEuTArkMVpvfBuMjEnLjH3PpaE6mMKff6JGF4NvbHeolVY8nGFx-OKd6SAVuq1ngCMdlZsYUjPRCcXx4fPoagBWeOgo8sa8PnxdBU3w3qkwHF2QBiqD-ZeHrQVX7Q_0otp0_vLsRjWi9lotA6V0ZDxcItlkPoRmQOdApH8aTS1QXwUjZ_8c3IcDlCb97euQZWoDQ8v7yvllhCGDBPTaZE2bfZPuFV3RXyVVSBclPALF-uLncecHUKQpcQoabu6GNFMytJJovTKFaLmmhclnpnRr5LZLbTd4rmlNTtK5H_RWDbjoAslC391g4DnyELSX0vRrxTkUV1vSmSCWZRCZl4MzfODRtXxW0TQR-HhP1idqzkqtv6cwHZWcvQFiHp2GV0jwBO1JQYRAVKr0bBeyCLmtTIvXhEU6wQuDkc-9mWg9SwS5ofR1vANGq_QiBYAgFxR_PLxe_CwDNCQXw55n_LH_Ax2ZWYocL8-DS1incIUABO51O9pHSmRp1Q3om2F-8BkimKvhX3iuqCWgberHtTbe4hLG_9f6XkZNZkAYAX5BZaEhnfKnt1sraDMlZc50pw-1bzhf657o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهم تجزیه‌طلبان برای تصرف تهران با همراهی مردم!
🔹
طرح مشترک آمریکا و اسرائیل که به تشکیل یک مرکز فرماندهی با حضور افسران عالی‌رتبه موساد و سیا و همچنین فرماندهان گروهک‌های تجزیه‌طلب کردی منجر شد، درصدد اجرای سناریوی تجزیه ایران و تغییر نظام حاکمیتی جمهوری اسلامی ایران بود.
🔹
این طرح، با حضور مردم کرد در صحنه و همچنین با اشراف اطلاعاتی و برخورد قاطعانه نیروهای جمهوری اسلامی، از جمله موشک‌باران و حملات پهپادی به مقرهای این گروهک‌ها، در همان مراحل اولیه خنثی شد و به سرانجام نرسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/693362" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG47txNFqUeTBFE7uc1dZOibBbbTu10AUX9FOCd_VFFmI8gIfsMfsQwsLmnpYV17t8Fxu5PsXiQ6w-wXUASWNn1eJgkmuhTJjWx92yjs2l7m0A83bP_XyQkc3Xz4viIa9y3HRAy6iX_Vl-KRqD3sJIsZJclhWzNqkUPhX51m63jEOF2cPCSlSWswGE3KWgd6hqN86YcbXsscxBCTBzRmnmx6pmJTLpBcrzpd9-8sk4DnF0fz1k5PX6ltIkvuRxtUMSG8od56-uMsr1LzvXgI7myw1Somzo6A80_hvY0JVn2sTmhlqshY-OTh1jOng_8IPeHKrZuK6SrZdyg_MVs1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این سازه کوه نیست؛ قلعه‌ای ۲ هزار ساله در هند است!
🏰
🇮🇳
🔹
قلعه «لوهاگاد» در ماهاراشترا هند، دژی با قدمت بیش از ۲ هزار سال و ارتفاع ۱۰۳۳ متر است که ریشه آن به دوره ساتاواهانا بازمی‌گردد.
🔹
این قلعه با دیوارهای سنگی، دروازه‌های مستحکم و مخازن آب شناخته می‌شود و شاخص‌ترین بخش آن، «وینچو کاتا» با شکلی شبیه دم عقرب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/693361" target="_blank">📅 13:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224d857ded.mp4?token=alkIZSirEG_WcPbP9DZs8WmUCGkoYdr1m3rIVXLO9kmz5cFgp6muRkSL50W0NufVVOw50wzFeKpIVYNSBx54MX-1sUcajvaMLBTFXVmS0P8pFEJoWZmhvoucGUY1UQLZ7TxbbVr_QHFJfeSHLm_yFCk9g33s683HaaOAO0Oh7R3pTCmeacqVa2HlZ1UuoBCkRMNjlMVtouXreeWGi09h8-xrOBepnA4K38GphNoWDvO942sY7Y68UVbEbLB0U0Fgqk6IRBN0b5WFVg9UZ9dXBMDrC1POGB78TNOWBAFRlfPGisJMe6LuCzfVIsxOwHOzoxTH0yZlAvqYWoLV78Cg4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224d857ded.mp4?token=alkIZSirEG_WcPbP9DZs8WmUCGkoYdr1m3rIVXLO9kmz5cFgp6muRkSL50W0NufVVOw50wzFeKpIVYNSBx54MX-1sUcajvaMLBTFXVmS0P8pFEJoWZmhvoucGUY1UQLZ7TxbbVr_QHFJfeSHLm_yFCk9g33s683HaaOAO0Oh7R3pTCmeacqVa2HlZ1UuoBCkRMNjlMVtouXreeWGi09h8-xrOBepnA4K38GphNoWDvO942sY7Y68UVbEbLB0U0Fgqk6IRBN0b5WFVg9UZ9dXBMDrC1POGB78TNOWBAFRlfPGisJMe6LuCzfVIsxOwHOzoxTH0yZlAvqYWoLV78Cg4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی چشم ۱۰۰۰ برابر بزرگ‌نمایی شود، این‌طور به نظر می‌رسد
👁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693360" target="_blank">📅 12:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
عباس عبدی و روزنامه اعتماد مجرم شناخته شدند  سخنگوی دادگاه مطبوعات:
🔹
هیئت منصفه دادگاه‌های سیاسی و مطبوعاتی با اکثریت آرا عباس عبدی و روزنامه اعتماد را مجرم شناخت و آنان را مستحق تخفیف در مجازات ندانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/693359" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9945f7392.mp4?token=cA_EWhX2cgbhkiWolhjqzY2HQtySZxatjpu-aSbTxHM8EyTiwmkc787sfoQAESmtJmlAaXA5GJ1BTwaK8_V7C5wUhZbXnxM9LET5w0LIS8dW6WCMC4wVOglfyMhPi-XvX-tkMNxFcrRb2wd43DApzDxQkN0LwcU8McIsnuxwa_chuMJDJjasNqH8gbWIZPtFcAvHSzUFpqVPEprCVDTCDtNOwjYfGs-wfSQGPGfalJ5pGGSY8xeYuw7pgpx0cqqZxyu-SOJcmBR-GLkSm9JcJih4qtKBZNzmIUoTY544kEGXAKWXmAPMazwhCg5sGcAD2ZWh65LJNKNoPKkio0j_4zp5B2grbGvz0VI3kV36kWZ08ZaORJCu7sfvaqMO29wsVqtRLH1YJqJ9ymEyiqyKG9XYqZHakMuuFAZ9KWMXiKf6j-BAWopZ_xf_Hyp188cx57Jk2vg9kMMCcjl9hyksP2oZQcKPt8J06K06EjbiObzEjxuLKrPKSO6ERWpkMSZY22EJgFgAZPLzFbS-yX9NXyDBw2_V96NS1NeVOYHL0ZvcMjebOt1ShDsczG8B6LFWteRSdt23D-PlWkpBYjbX6Ydi5GLu158yWO5S5EsjTRFXcShsIqnHuoEOEdIwxfqHOyCSc14MwhDcDqeV4HqR-WcLs7FFHF99u8YbwCyfv4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9945f7392.mp4?token=cA_EWhX2cgbhkiWolhjqzY2HQtySZxatjpu-aSbTxHM8EyTiwmkc787sfoQAESmtJmlAaXA5GJ1BTwaK8_V7C5wUhZbXnxM9LET5w0LIS8dW6WCMC4wVOglfyMhPi-XvX-tkMNxFcrRb2wd43DApzDxQkN0LwcU8McIsnuxwa_chuMJDJjasNqH8gbWIZPtFcAvHSzUFpqVPEprCVDTCDtNOwjYfGs-wfSQGPGfalJ5pGGSY8xeYuw7pgpx0cqqZxyu-SOJcmBR-GLkSm9JcJih4qtKBZNzmIUoTY544kEGXAKWXmAPMazwhCg5sGcAD2ZWh65LJNKNoPKkio0j_4zp5B2grbGvz0VI3kV36kWZ08ZaORJCu7sfvaqMO29wsVqtRLH1YJqJ9ymEyiqyKG9XYqZHakMuuFAZ9KWMXiKf6j-BAWopZ_xf_Hyp188cx57Jk2vg9kMMCcjl9hyksP2oZQcKPt8J06K06EjbiObzEjxuLKrPKSO6ERWpkMSZY22EJgFgAZPLzFbS-yX9NXyDBw2_V96NS1NeVOYHL0ZvcMjebOt1ShDsczG8B6LFWteRSdt23D-PlWkpBYjbX6Ydi5GLu158yWO5S5EsjTRFXcShsIqnHuoEOEdIwxfqHOyCSc14MwhDcDqeV4HqR-WcLs7FFHF99u8YbwCyfv4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۷ اتفاق غیر منتظره در سفر رئیس جمهور چین به آمریکا/ نقشه ترامپ جواب داد؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693358" target="_blank">📅 12:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حمید رسایی به ۱۰ ماه حبس محکوم شد
🔹
آوش به نقل از اداره حقوقی مجلس مدعی شد حمید رسایی، به‌دلیل پرونده‌ای مربوط به سال ۱۴۰۲، به ۱۰ ماه حبس تعزیری محکوم و برای اجرای حکم احضار شده است.
🔹
این پرونده شامل انتشار مطلبی با عنوان «دستکاری قالیباف در اسناد مجلس»…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693357" target="_blank">📅 12:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baF3TR9H0HTHtOY2LWYMOYgIc4R4ZQAeTcVXs3Rss_kpDJcqvgwyh6w_KMa6kMW98PH4DBQpDSiKsNLgx0VPfW1kIAldYoo_psXbWO1Sxd7mu9FzrCl8w6hr9O6PVEkn98IjTDZFJ229RnC8jNiOQmI5adBJOOm6yui9eWJ195QwkT_cZoyGY-bK6wzNqcss6XkxblIZKnp1PJRtKrAXaeNtXSvYCQo74NqdpTXbIzgpfK1KvA1i2wPRARXN4-i3GvIGOKXyk3O7C9pTXl431uh5PFeCfgq1bQUwCl5Fb1KhTOX4fWzR_XXiuOwQQqCwpRQHl6sbynK-WNFxwvhWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موهات دقیقاً چی لازم داره؟
👀
✨
ضدریزش؟ ضدشوره؟ ترمیم و مراقبت؟
هر کدوم رو بخوای، یه انتخاب مناسب توی ارکیده شاپ منتظرته
💕
🛍️
تنوع محصولات پنتن + خرید راحت + ارسال به سراسر کشور
📦
برای دیدن مدل‌ها و قیمت‌ها، سر بزن به ارکیده شاپ
🌷
https://t.me/orkide2025
https://t.me/orkide2025</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/693356" target="_blank">📅 12:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrwyvSKWZ3mi0Rt9DnFJLGkeHP_44IHQeJgmiCY2H6etFzMHChGCrUkhOJI3RBwrNPspbkrb-fC0_qA8q1lxW5Tt-vUy0hZfBVfyEO1J2BZtzIOi_dTzKe6YDuU_Uv-y_sJNa507WtS16360MatWpKKecqA9B0BZqEd0oEoKAaBoc0RCcXhkMamiBJzKmUIH1zK3cD8EvDL9Ie1CRaB8EjuazP-CGVWx9dj-Fz-GuVRv7oXb-Uwbi27CVJIfsG0KnwsdRX-t7qo3ZdImZnt-rU9bio3ETL58femcqU0j7nWkVjsXu6PMl4U4jOIPhFGdxXr3Smw7eSASJLXTE4UBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گام دیجی‌کالا برای تجهیز دانش‌آموزان به ابزار آموزشی در سال تحصیلی جدید
🔹
دیجی‌کالا مهر با همکاری روبی‌تک، مکتب‌خونه و کاریار کمپین «هرجا که تویی» را برای کاهش شکاف آموزشی کلید زد.
🔹
در این طرح، هدف تأمین حداقل ۴۰۰ تا ۱۰۰۰ دستگاه لپ‌تاپ برای دانش‌آموزان مستعد کم‌برخوردار است تا بدون دغدغه ابزار، به کلاس‌ها و مهارت‌های دیجیتال دسترسی داشته باشند.
🔹
مدل این طرح "عملکرد-محور" است؛ لپ‌تاپ‌ها به صورت امانی در اختیار دانش‌آموزان قرار می‌گیرد تا به این صورت همه بتوانند عادلانه از تجهیزات برخوردار شوند.
🔹
در کنار تأمین ابزار، برنامه منتورینگ توسط مدیران ارشد دیجی‌کالا و دوره‌های مهارتی برای ارتقای دانش‌آموزان در نظر گرفته شده است تا مسیری برای رشد آینده آن‌ها فراهم شود.
🔹
با وجود استقبال از این حرکت داوطلبانه، محمدرضا ماندنی، نویسنده و پادکستر یادآور شده که این کمپین‌ها نباید جایگزین وظایف حاکمیتی شود.
🔹
او تأکید دارد که حل پایدار معضل دسترسی به آموزش، نیازمند بودجه و سیاست‌گذاری منسجم وزارت آموزش‌وپرورش است و اقدامات بخش خصوصی تنها می‌تواند بخشی از این خلأ بزرگ را پر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/693355" target="_blank">📅 12:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
منبع نزدیک به تیم مذاکره‌کننده: ایران منافع خود را تحت فشار واگذار نمی‌کند
🔹
پیشنهاد اخیر ایران دربرگیرندهٔ مجموعه‌ای از اقدامات متقابل و مرحله‌بندی‌شده است و ایران مواضع و ملاحظات خود را به‌صورت روشن به طرف‌های مقابل منتقل کرده است.
🔹
وضعیت هیئت حاکمهٔ آمریکا در داخل این کشور با چالش‌های جدی مواجه است و نارضایتی نسبت به پیامدهای جنگ و هزینه‌های ناشی از آن افزایش یافته است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/693354" target="_blank">📅 12:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bb83d5df9.mp4?token=bRBvgWtXJGCDyxwadRS2FGfGxa2u5gZr4qSFrTlMP8uAsMFL9iR1vaAe5DWTAUIkqoThKREIvv2d2vPl6V27W2cgByD8XPUzxWpO_YSe4flIPGnNjUAVPUHC-dhgoEgNnTtjq4W7o7SzzsIZmFUKdjw5YuZe3-KLjaxvkife1U4fPPcmDZDUF_2DwALNuUCVtFCYGAGIi7gOLz3SWlC0V05Ll-opmDusnGPY0UMuEQPTI3SxQAyTWiZwhrhhyNuvRzIQQ0zerNu0Pt2DRFj8NI4bmFN1HZPpKIta-mC0ttLO-o4AyS44MpJpfkkqHtfhmyPoqG5VetgKsExWcpSI70TyIdo4h_htC1ez0lYecOzImdkLFUgR4R9Jr1lnEeRNaC7jFeUc4hIqJepaY0iCY4j-AOrMVkdjerXdHYxqN6vx6bengVcd7RQ6ZPNBZXYpU53UWCBbwnEgMzvg9nZKVczu-JPOL1Bvnh4Rf9rtmtsZSH2ksj5mkT3tvEF5owAd7eNQnIRFUHyhKdogbaDYppckrulEE62QEUFCHveJvt2OXomROjHpeHc12gSNzVtS6Jr7v3lIVlffSppShpeFUTKNzQjMZEfS4dPGqNYg67RxoJaash360zTMaewPqnJ49rccEqiJLb3PoNIbY6YJ08eicbvSQrZKSBR4mvx6jJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bb83d5df9.mp4?token=bRBvgWtXJGCDyxwadRS2FGfGxa2u5gZr4qSFrTlMP8uAsMFL9iR1vaAe5DWTAUIkqoThKREIvv2d2vPl6V27W2cgByD8XPUzxWpO_YSe4flIPGnNjUAVPUHC-dhgoEgNnTtjq4W7o7SzzsIZmFUKdjw5YuZe3-KLjaxvkife1U4fPPcmDZDUF_2DwALNuUCVtFCYGAGIi7gOLz3SWlC0V05Ll-opmDusnGPY0UMuEQPTI3SxQAyTWiZwhrhhyNuvRzIQQ0zerNu0Pt2DRFj8NI4bmFN1HZPpKIta-mC0ttLO-o4AyS44MpJpfkkqHtfhmyPoqG5VetgKsExWcpSI70TyIdo4h_htC1ez0lYecOzImdkLFUgR4R9Jr1lnEeRNaC7jFeUc4hIqJepaY0iCY4j-AOrMVkdjerXdHYxqN6vx6bengVcd7RQ6ZPNBZXYpU53UWCBbwnEgMzvg9nZKVczu-JPOL1Bvnh4Rf9rtmtsZSH2ksj5mkT3tvEF5owAd7eNQnIRFUHyhKdogbaDYppckrulEE62QEUFCHveJvt2OXomROjHpeHc12gSNzVtS6Jr7v3lIVlffSppShpeFUTKNzQjMZEfS4dPGqNYg67RxoJaash360zTMaewPqnJ49rccEqiJLb3PoNIbY6YJ08eicbvSQrZKSBR4mvx6jJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر احساس میکنید که دیگه مثل قبل خوشحال نمی‌شید، این کلیپ رو ببینید! #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/693353" target="_blank">📅 12:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حمید رسایی به ۱۰ ماه حبس محکوم شد
🔹
آوش به نقل از اداره حقوقی مجلس مدعی شد حمید رسایی، به‌دلیل پرونده‌ای مربوط به سال ۱۴۰۲، به ۱۰ ماه حبس تعزیری محکوم و برای اجرای حکم احضار شده است.
🔹
این پرونده شامل انتشار مطلبی با عنوان «دستکاری قالیباف در اسناد مجلس» در نشریه «۹ دی» و انتشار کلیپی در کانال تلگرامی او با استفاده از تعبیر «دیکتاتور پارلمانی» درباره رئیس مجلس عنوان شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/693352" target="_blank">📅 12:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31391b7814.mp4?token=X9JLUbGP4zKy3uLKh-sWIXqPXHSge_DH5Chb3rXRg0qEHr56Hg2EElI6lsXpf0VAn39cGzVi4okwthfi1iGr14j5wSPpZJ3ZrREIuzH58zBKK6BSFMBzTsdUjiQQchP9dSINLUA4XYadGbC0IIf8z7N-Dgj3Jw2Ai8TGteN4SIYNH1ffO2RTY78-IKqQjPCRdBHvOe6XzREr_JLjOuJpah7pCUnIb_SnK242B0x30J73RG0gIftMF9T3ymz0aSShMzqK-b-UP1zk_EXjT5roZFTcrZA9Cbi-0bb2-ZLNke-_U90UUkFPtyb8uHbRgE8DZXoBmOcoc9vvhq92841s0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31391b7814.mp4?token=X9JLUbGP4zKy3uLKh-sWIXqPXHSge_DH5Chb3rXRg0qEHr56Hg2EElI6lsXpf0VAn39cGzVi4okwthfi1iGr14j5wSPpZJ3ZrREIuzH58zBKK6BSFMBzTsdUjiQQchP9dSINLUA4XYadGbC0IIf8z7N-Dgj3Jw2Ai8TGteN4SIYNH1ffO2RTY78-IKqQjPCRdBHvOe6XzREr_JLjOuJpah7pCUnIb_SnK242B0x30J73RG0gIftMF9T3ymz0aSShMzqK-b-UP1zk_EXjT5roZFTcrZA9Cbi-0bb2-ZLNke-_U90UUkFPtyb8uHbRgE8DZXoBmOcoc9vvhq92841s0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات بستنی فروش در چین
🇨🇳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/693351" target="_blank">📅 11:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693349">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfecc8ef7.mp4?token=jbSen7SlHQgGQXT-eQQiC1OhXBp3aVISlbb8GTBMz4nJN8UfIYUP5k4sWe3Gvg7J1yp89W5eV8gpB4lXxfk74Yvm_FdV-1T12XHxhSloEjNo-bn7cmSlEF6QuyZiss74RcP_mViUpOuX-4RVh4wGas9-R6O0eANLj2yHlpMoENlQ1glOnddCyX23kggoVzzxTrTeoFtwnEs3XlhW5Ze2nNqzwzREIp9dSu0R4hhY53SaOfUy6v7xgpBy5nXb0nk32pzpwygZpXnCj-w_PEdTXf_pRVDA-biMYHJrAvERnU5k-XR9F_m-TC2UmJ4G3FzrucDrWEf-98Oweg0Tqwy6gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfecc8ef7.mp4?token=jbSen7SlHQgGQXT-eQQiC1OhXBp3aVISlbb8GTBMz4nJN8UfIYUP5k4sWe3Gvg7J1yp89W5eV8gpB4lXxfk74Yvm_FdV-1T12XHxhSloEjNo-bn7cmSlEF6QuyZiss74RcP_mViUpOuX-4RVh4wGas9-R6O0eANLj2yHlpMoENlQ1glOnddCyX23kggoVzzxTrTeoFtwnEs3XlhW5Ze2nNqzwzREIp9dSu0R4hhY53SaOfUy6v7xgpBy5nXb0nk32pzpwygZpXnCj-w_PEdTXf_pRVDA-biMYHJrAvERnU5k-XR9F_m-TC2UmJ4G3FzrucDrWEf-98Oweg0Tqwy6gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرخ زندگی
🔹
مسیر توسعه شغلی؛ داستانِ شروع کسب‌وکارهای کوچک خانگی که با تلاش و پشتکار رشد کردند.
🔸
روایت شما از آغاز کسب‌وکارتان می‌تواند انگیزه‌بخش دیگران باشد. در یک ویس ۳۰ ثانیه‌ای، داستان شروع کار خود را همراه با تصویر محصول یا خدماتتان برای ما ارسال کنید تا در خبرفوری منتشر شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/693349" target="_blank">📅 11:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693348">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حادثه امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس
🔹
پلیس انگلیس از وقوع یک «حادثه بزرگ» در نزدیکی پایگاه هوایی آمریکا در فیرفورد و بازداشت چند نفر به ظن نقض قوانین مواد منفجره خبر داد.
🔹
ساکنان مناطق اطراف نیز به‌دلیل این حادثه تخلیه و به یک مرکز تفریحی منتقل شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/693348" target="_blank">📅 11:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693347">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9fd9ea064.mp4?token=ZXJOaTWrWEYLhSBjXrnqqR7OsBPiS6VS85Ts8AAwioUsY8zdD3mDpXoR8HTajzbBHL0wengezaeb02jlXXWWTUhZt1gQlURYGNUrPsjHtYX5zm09yQzm9dAjWB3QPOA8gzv8luX-jaJZliiKGsHb7JfcrTue2fd_kHFWdOqL72EzztTrYzdarY46up46D0A5cqXYMR9yO3F2UZY1ifIddEFrUsqksD2gp6Mz9H1ncoQD_5e3KxRoYbExVucu1vczZsRqxgvyhnFdCJ2DZJSmJWDvhibMZNSci524Znu_2sL2Txb4NB4Li2vDEjp7Xy5SLipup0wcVYHyIxJov7YYfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9fd9ea064.mp4?token=ZXJOaTWrWEYLhSBjXrnqqR7OsBPiS6VS85Ts8AAwioUsY8zdD3mDpXoR8HTajzbBHL0wengezaeb02jlXXWWTUhZt1gQlURYGNUrPsjHtYX5zm09yQzm9dAjWB3QPOA8gzv8luX-jaJZliiKGsHb7JfcrTue2fd_kHFWdOqL72EzztTrYzdarY46up46D0A5cqXYMR9yO3F2UZY1ifIddEFrUsqksD2gp6Mz9H1ncoQD_5e3KxRoYbExVucu1vczZsRqxgvyhnFdCJ2DZJSmJWDvhibMZNSci524Znu_2sL2Txb4NB4Li2vDEjp7Xy5SLipup0wcVYHyIxJov7YYfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
جاسوس‌های ایرانی‌ و لبنانی در ترور سید حسن نصرالله نقش داشتند؟!
🔹
روایت فرزند شهید نصرالله به مناسبت دومین سالگرد شهادت دبیر کل حزب الله لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/693347" target="_blank">📅 11:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693346">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04eeaaa4d0.mp4?token=uQeHwZPp9VgmI_WaHOXxTUZ2qwZsppSWKe15gWnpGMGwQNHKJ8BMwzv8GdMeCTaPSYPfnT9Els0QVQ1eo0_PgdCUOcu6TpWwh42gFRtGs2ZXbmu1aitiwqLxu3nuMK9aJn0s9LbNryg76q0m9MD-6QEK7V_zVmXZedosCnnnImfgjn8lj6FOxDOXBDEJMwdHAWZ1iC9FZ_e7HqOVuiRTB_lplB4Mj5oPaHv73J_HbhwWFZpCEb2YLsa3TO5SdajHs5gqlSKDxWabIefxrbxn-OlV0ACB5UXmpV9JslRcr0i-XG9PC5qOxfJU1p0iSlApVLoknakk7pBcj8RRX5ldTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04eeaaa4d0.mp4?token=uQeHwZPp9VgmI_WaHOXxTUZ2qwZsppSWKe15gWnpGMGwQNHKJ8BMwzv8GdMeCTaPSYPfnT9Els0QVQ1eo0_PgdCUOcu6TpWwh42gFRtGs2ZXbmu1aitiwqLxu3nuMK9aJn0s9LbNryg76q0m9MD-6QEK7V_zVmXZedosCnnnImfgjn8lj6FOxDOXBDEJMwdHAWZ1iC9FZ_e7HqOVuiRTB_lplB4Mj5oPaHv73J_HbhwWFZpCEb2YLsa3TO5SdajHs5gqlSKDxWabIefxrbxn-OlV0ACB5UXmpV9JslRcr0i-XG9PC5qOxfJU1p0iSlApVLoknakk7pBcj8RRX5ldTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با آقا مجتبی قبل از جنگ دیدار داشتم، او عاشق سید حسن نصرالله است
🔹
گفتگوی فرزند شهید نصرالله به مناسبت دومین سالگرد شهادت دبیر کل حزب الله لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/693346" target="_blank">📅 11:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693345">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSKe64p0P1szRU47JnoI4p25kObYEYGdD0Vu1w-1Hmgc66pHfGCwb0nLpikSg487pL3uvbcF5kKEREHUIRQgIrtsADmFGe36emxhNAvRDhAQZBSf2GAZokXROD752Mc8V88u8axgn-vdrUuZBqdsPjRKwoQHz8UhX8LbDaFbITOXxBmIvMGEbFI3kGqDTaznPGyT09SHQ_qHjN7yI-1XoDiMPKskNWptjcubiHVIEGhTErhnsLMKAn_EuvZgT1XZRbuasGXGDJKlxqw5j-_fOTrRkpPvthZlxJl4rv-XXl28wQ_Hm5WRlcdxN37tQ7VnM8sk6rJHYpkTX2GmZy7ORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر غذایی، پیاز مناسب خودش را دارد
🧅
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/693345" target="_blank">📅 11:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693344">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای المانیتور: چین همچنان حامی ایران در برابر فشار آمریکا است
🔹
چین همچنان در توانایی ایران برای مقاومت در برابر فشار آمریکا نقش محوری دارد و به‌دلیل وابستگی به نفت ایران، انگیزه‌ای برای استفاده از اهرم‌های خود به نفع واشنگتن ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/693344" target="_blank">📅 11:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693343">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EICOW24brKDTT5MHtVCrJnIto_zDzYKspBugAf3TTY4wJQ9KmucvuHfF7EYFqkgCs0BEZfNkg6f31ixEFvjOIYem8_Z9WopETDFAIsa2hEMonerYNYkWaJkAYDu52AriraLgA9ukx2TdUwVcxZOWTZJQofqrIJkmAZ1Xa3iGjsptChv4434d8JVjfa67ECEtoiS7j5w-zKtRvaF9S2t6J0zPnXscE4Gyz67tTlHJvPZxzZQj7RjFKK2hjM3uTkGttIOOJLoutymDpTjc5NDx3LNqVfWr8d4BRsIWhNMsJc_WR3mmnev1WVbFHwyCpJxQdclYF7YFsqG92CM-GmYwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل تولید ویدیوهای ۱۰۸۰p با هوش مصنوعی را برای همه کاربران فعال کرد
🔹
گوگل امکان تولید ویدیو با وضوح 1080p را در Google Vids برای دارندگان حساب‌های عادی و Google Workspace فراهم کرد. این قابلیت با استفاده از مدل Gemini Omni 1.1 Flash، امکان ساخت ویدیو از روی متن، عکس، صدا یا کلیپ‌های موجود را فراهم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/693343" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvOyhSlzL15oQ085E4Ok50x660IH0q2Ig5IA6vHhPiQXz-xQjFbNE_Ebh9Kd5adTLcTHPrgenAS96H7nMyh_p3NyILa3vmXjtLFNeneS_x4rrRhWulkIlJWLsUPVVfoyzWZA1-YU1T0RNS9BLTuJlhGk3a5-y01LBNEd0ocoh6C-y13bh9cPP8-xg9Iw-T6SXDtRk8yN0z6U5IuBmYuflWs8xbtVhx7qvxQVbREzSX8Id_4-In-IbVjSUZPw74PtVgxZeWO58Ff3apBPNPFdmm3mAvHkSband7tjCj8v1H1mnwIhKB_nrBpn6k73ndIFqwhdk0DBg0pnjdnp4pNiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرهنگ دوم مجید بهرامی در زنجان به شهادت رسید
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/693341" target="_blank">📅 10:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gC2luvrUaD6UQafdJGDMm0X5NK7EZhLn99u3fVwjceOkFH8PzW0jLj13Xiwh1qKEANqT11PfqSJNi2KZpnCZWVd8ItEtFbeRNCYEfXFFL1gg3WvYi1-Epxd9faiJlzmNjxYxaS8zBD5jok_rvuZsS7ewmZ0pMlyrmJq5BmwAQLzxcfw2STuoXWBJIg-mk5b0uhf9esYhVaRjnYj6TAF4PCOvOoYK4XwpHJOwRQ2CukW1PZ5cDsIoLye9xhX-7W7AV5OdJg3IzUJkWwoaOt1wQpPDOyy-XONGNqAsg-u89gdJU8AQO8DUOwPzgfu15pLcmtUxOk12cJrzW58wiueWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل دسترسی ایرانی‌ها به ایمیل را محدود کرد؟
🔹
گزارش‌های متعدد کاربران ایرانی نشان می‌دهد روند ساخت حساب جدید گوگل و دریافت کد تأیید برای شماره‌های ایرانی با مشکل جدی روبه‌رو شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/693340" target="_blank">📅 10:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693338">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حشمت‌الله فلاحت‌پیشه، نمایندهٔ پیشین مجلس به یک سال حبس تعلیقی و ۵۰ میلیون جزای نقدی و صادق زیباکلام به یک سال حبس تعزیری و ۲ سال منع فعالیت رسانه‌ای محکوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/693338" target="_blank">📅 10:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZBdmsFad1ddFA7IVYlrMiftld8JceGq--pN8T6HFuYeuRfUXI5VnaySHSKkWUD9ZpCpcYo0XDD5-sLYonD63IypWxh_jBL7w6D1QE_4vKTqJU4DB5Yh89ZidlBwMnZZj9DTPXSbKkBF4GXUpe0HOFEVp6TqmqLFG39GMw8QexO4GTWkOqUPzB2A7gPN0pqtthWK1i5OrZzLmSUySYVvC0na160lX-swhE6kiA4eLuT2cwVvO_C-2Km0Extn-D-SvCpoGDEZdUOrL8FGo_2nqAUKUCRqI4SPOoT38OGnok_gS1hSCHG4fr1KiDhgCHgYnEsSaeh8mBfrzkkawSFdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: پنتاگون با تأیید ۳۷ مورد جدید، مجموع مجروحان نظامی آمریکا در جنگ علیه ایران را به ۸۶۱ تن رساند. در لیست جدید، نام ۲۹ ملوان و ۸ تفنگدار دریایی ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/693336" target="_blank">📅 10:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: جنگ علیه ایران باعث شده در آستانه انتخابات میان‌ دوره‌ای، جمهوری‌خواهان در محاسبات خود درباره ترامپ بازنگری کنند
🔹
نامزدها در برخی ایالت‌ها شروع به حذف نام ترامپ از وب‌سایت‌های انتخاباتی خود کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/693335" target="_blank">📅 10:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fc5bf247.mp4?token=IeGMjcHvGKxHseDQmZrwwmg1rugZdhRus8FjsjJaYiG41x5IKPFl_qSWkNOkHm5De9Fw3_07f1K30-sRKg6kSCWsipuQQfne89rOKu8YTkmp7MJG7WeG_c1entHWiUl4gzlpdRupS1BXhlUZVOJh1cFSnqOkJF0N8Dz8BLJU2cq8p2mNdxB1xN7aq6oHADc2NVaF0tgp4M2k25ZxTg1DK0wuWZm9q4PVxOUVJxYm8XCDw12-8Oraihki8Y8V8W1SZ8AV3ibPQNT7tyaAynNAgOCu-zuSuppY5hBySlLq_QeM8hqRg1-2afDqUUL_Uf1BMYh9kc00XBMcY1tOnU5o5QXVaD6J_bAVcD4TDvCFoOoPk-N8zB7v997C90EdH6SxLmLXtBCMAYOPriIqACSuOwDnQM1TiW4pt64XOoGr5Qm3QWhTphy7zLIpTHeHConI6cy-_mI5xUnn-22iYVQUun8gqTioX11REZHK67PsFkN6Nk7VDe0dcauTygkz_47T84Wust8rvaoGFok5VbKzFK481LHrNp_n2KT_9RZ45kx3qICg-Pc83sYk878wglOZQheWaLKWSH5EiGxFDSZr-uViTKvX05jqc687CjWYln9spSC5hVvDN0LyIyL8BhJOw8y_G0FMoAJ_uxJnFprfMXa17x49tcfgm9zIw4JTugE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fc5bf247.mp4?token=IeGMjcHvGKxHseDQmZrwwmg1rugZdhRus8FjsjJaYiG41x5IKPFl_qSWkNOkHm5De9Fw3_07f1K30-sRKg6kSCWsipuQQfne89rOKu8YTkmp7MJG7WeG_c1entHWiUl4gzlpdRupS1BXhlUZVOJh1cFSnqOkJF0N8Dz8BLJU2cq8p2mNdxB1xN7aq6oHADc2NVaF0tgp4M2k25ZxTg1DK0wuWZm9q4PVxOUVJxYm8XCDw12-8Oraihki8Y8V8W1SZ8AV3ibPQNT7tyaAynNAgOCu-zuSuppY5hBySlLq_QeM8hqRg1-2afDqUUL_Uf1BMYh9kc00XBMcY1tOnU5o5QXVaD6J_bAVcD4TDvCFoOoPk-N8zB7v997C90EdH6SxLmLXtBCMAYOPriIqACSuOwDnQM1TiW4pt64XOoGr5Qm3QWhTphy7zLIpTHeHConI6cy-_mI5xUnn-22iYVQUun8gqTioX11REZHK67PsFkN6Nk7VDe0dcauTygkz_47T84Wust8rvaoGFok5VbKzFK481LHrNp_n2KT_9RZ45kx3qICg-Pc83sYk878wglOZQheWaLKWSH5EiGxFDSZr-uViTKvX05jqc687CjWYln9spSC5hVvDN0LyIyL8BhJOw8y_G0FMoAJ_uxJnFprfMXa17x49tcfgm9zIw4JTugE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مایونز سالم و خونگی با چند ماده ساده؛ پرپروتئین و سرشار از چربی‌های مفید
😋
🍽
🔹
مواد لازم برای یه شیشه کوچیک مایونز سالم پروتئینی: تخم مرغ اب پز ۳ عدد آب ۸۰ میل یا یک چهارم لیوان سرکه ترجیحا سرکه سیب ۲ ق غ روغن زیتون فرابکر ۵۰ میل حدودا یک پنجم لیوان نمک نصف…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/693334" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/693333" target="_blank">📅 10:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6629a320.mp4?token=YEJlprs8o2wpkyvhtvdWLBXwdYFENaXJkNtY4YCznwMQ2FkKmRKVLPA_y0zkyuFN7CaSdtuYhQ78o_2SZ1yoARD2Px1YOIZplbmb2_k3xeKEYEdxmlCbF6lyJNL8VO6snMiRdCbmWw7i0lg9WUR6FmNZjTjcPC8wB9j0VLe3K9jrEnQ9tbILQbH_15LoUnycNouFQm-0VAEZ2Lr1m0IZne9J2DCourHUBRULX_ZFnC6rXTLG1mLskizyem448nDIVBUFwBFhBzmLs__ZsJDDzhZP41onRW0UIYlIdi6mU2wOsukJuPZfHbAiK_YnInSCqYL4b8AC9JozYZKUh6_-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6629a320.mp4?token=YEJlprs8o2wpkyvhtvdWLBXwdYFENaXJkNtY4YCznwMQ2FkKmRKVLPA_y0zkyuFN7CaSdtuYhQ78o_2SZ1yoARD2Px1YOIZplbmb2_k3xeKEYEdxmlCbF6lyJNL8VO6snMiRdCbmWw7i0lg9WUR6FmNZjTjcPC8wB9j0VLe3K9jrEnQ9tbILQbH_15LoUnycNouFQm-0VAEZ2Lr1m0IZne9J2DCourHUBRULX_ZFnC6rXTLG1mLskizyem448nDIVBUFwBFhBzmLs__ZsJDDzhZP41onRW0UIYlIdi6mU2wOsukJuPZfHbAiK_YnInSCqYL4b8AC9JozYZKUh6_-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صاحب یکی از آشناترین صداهای طبیعت را ببینید؛ جیرجیرکی کوچک با صدایی بزرگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/693332" target="_blank">📅 10:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3124a279ab.mp4?token=b8G3-e_vT6LUf7OdDJQiiMy7Tr9KXCHd4lRUnXobhR2PH5OVeKUgD6PaAqTmCbfw2tt-mgSB_2CYdsLlD-G5PSmDVDQYGPCFyvAha8Mp8xZYYW-zG83FnP8M8rAECf69D6LwTfGiy9LtRUzV19cHRAtSiaAbpBhegA9x78lCm5V2aSngerM-HV_I2nF9Y37kLUPFBRoLMQP5uSTrI0NEc0SF27pbDtRIIzLJuupTIXHJr66w-heACXn1-QDID6uZXg2jfbjSEvz8K7HlZJGK6dlUqb2kj1Q6wKXc1T8QSj32dlluARVKySvYd5My2ArzduETZ0ja5I0D4aX0Ukzvvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3124a279ab.mp4?token=b8G3-e_vT6LUf7OdDJQiiMy7Tr9KXCHd4lRUnXobhR2PH5OVeKUgD6PaAqTmCbfw2tt-mgSB_2CYdsLlD-G5PSmDVDQYGPCFyvAha8Mp8xZYYW-zG83FnP8M8rAECf69D6LwTfGiy9LtRUzV19cHRAtSiaAbpBhegA9x78lCm5V2aSngerM-HV_I2nF9Y37kLUPFBRoLMQP5uSTrI0NEc0SF27pbDtRIIzLJuupTIXHJr66w-heACXn1-QDID6uZXg2jfbjSEvz8K7HlZJGK6dlUqb2kj1Q6wKXc1T8QSj32dlluARVKySvYd5My2ArzduETZ0ja5I0D4aX0Ukzvvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار بود فرد دیگری آن روز در اتاق عملیات باشد
🔹
روایت فرزند شهید نصرالله از روز ترور، به مناسبت دومین سالگرد شهادت دبیر کل حزب الله لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/693331" target="_blank">📅 09:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91ef1e8ef.mp4?token=et12vdxA8Sh2DIQ4GiNB0gHKyhmM_xq11-RIkVgVjqQsXQTDSWlXDCNfeytOe5Xt2lsRLAhWsI5QBqXt4WLlBMx1gzPxokdPyfldjfV89KtA8sNs5oWfS0ubVk8o0mpkGnNZaZWV8cuXVmSCic5oV_tPns0yLGallYio5KtGmcz-tw5wsTTGiYZlNIrh3DmdGe15i9vbEQIA-2vyo4PuaMBrvlQxQYcNNGp7UlqzvM0xvHhIHFfAVUeVFIRWzd0X5kdlsjpD1nKvm7d7RB-Ky47sDHyZHQ8BcP4HBwIMHPYcgTh-_YNebkuNmMYnDE3-vlPqunWLYpGCcxg_HI6pfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91ef1e8ef.mp4?token=et12vdxA8Sh2DIQ4GiNB0gHKyhmM_xq11-RIkVgVjqQsXQTDSWlXDCNfeytOe5Xt2lsRLAhWsI5QBqXt4WLlBMx1gzPxokdPyfldjfV89KtA8sNs5oWfS0ubVk8o0mpkGnNZaZWV8cuXVmSCic5oV_tPns0yLGallYio5KtGmcz-tw5wsTTGiYZlNIrh3DmdGe15i9vbEQIA-2vyo4PuaMBrvlQxQYcNNGp7UlqzvM0xvHhIHFfAVUeVFIRWzd0X5kdlsjpD1nKvm7d7RB-Ky47sDHyZHQ8BcP4HBwIMHPYcgTh-_YNebkuNmMYnDE3-vlPqunWLYpGCcxg_HI6pfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران شدید خیابان‌های ایتالیا را به رودخانه تبدیل کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693328" target="_blank">📅 09:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67f1e8bc5.mp4?token=OXVnJiVC3EFLz8ub8llQXd2-RVqlqS_jEVW6o_Q3pnb9zzwEtEKS451JcYUJpbZwZdPbhk8FHZ07DBymWWE7VvtR1g6w-qsl7P0pQn_9rUVxvRmsTtobbR5ScBTsMagyE34TuJQz34s771wUcYAKVQzAqojaeXgm3fK0p-D90xT6o1H2krbLn_K4qjq6Ptxx6PLx96_mfQonaoAdfXRJ6wcpMmJX2YV7ZCSJQa_WVm_QnQb-aOTAJ5-jjv2qVg93luKcX71oRTS_748kgf2udbVWrF76Ltt0fZmC5BsqSC6Af_wE8Ch4Sex_ZCnn3457zT3H22ApivDUxBEcRUF_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67f1e8bc5.mp4?token=OXVnJiVC3EFLz8ub8llQXd2-RVqlqS_jEVW6o_Q3pnb9zzwEtEKS451JcYUJpbZwZdPbhk8FHZ07DBymWWE7VvtR1g6w-qsl7P0pQn_9rUVxvRmsTtobbR5ScBTsMagyE34TuJQz34s771wUcYAKVQzAqojaeXgm3fK0p-D90xT6o1H2krbLn_K4qjq6Ptxx6PLx96_mfQonaoAdfXRJ6wcpMmJX2YV7ZCSJQa_WVm_QnQb-aOTAJ5-jjv2qVg93luKcX71oRTS_748kgf2udbVWrF76Ltt0fZmC5BsqSC6Af_wE8Ch4Sex_ZCnn3457zT3H22ApivDUxBEcRUF_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو سال پیش؛ حمله مرگبار به ضاحیه و شهادت سیدحسن نصرالله
🔹
دو سال پیش در چنین روزی، سیدحسن نصرالله به همراه چندین فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروهوایی اسرائیل با ۸۳ بمب سنگرشکن ۲ هزار پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت، ترور و به شهادت رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/693327" target="_blank">📅 09:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا برای قطع ارتباط هوایی و بانکی کشورها با ایران، فشار می‌آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/693326" target="_blank">📅 09:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061905b87d.mp4?token=AFbwFEjJPSilrbUfY2eFiUwz30CQ6qCV8VRKzTZCxg0LMpMYMVWMttuTuR46gDei-KdmYM6j6Umx1N-er5fyMK-n7AK_6N3AK_ha6RIaOWAprEZigctjuvpPnSSTKPNyXVltaitgDAWRgtYIpSUTKjSN4cdQmaKsEs7JItvBgW8NOnrapstbxsec8qgXuZHKGRoHX2kctYm2UKWQ2u63AxDOcUpemJtIv415gdAh0Fvr8vNi0Ml72k2BTzuItk6cL6eAknHEB0LEZL00j2gMBs4oeosga1I7BwLKnn7mlWnR8ErLq65qctZwxQW4SaZvI89fMJZGkl3yWHAt6n3VbAaACyI75jzDqGl901eEmLUzdFeVbV1-jg9y9aTqtFpPVzjLrn74TDW-cWQudR98gjFQ9AvyRwWStpTroO-j3uVJDvGMKNGhPpc6EUYT19i8cgSR4r4qYEhogJMu8Ow3L1ZPOjl-cZ5xl0b8q5xOtIMfFM1s1EuGrq0cCBfqjkkWbnZjn666X144-2ToqOabCp16j2RpcfcAEGSOqprsb5orgqAuoiyxGxskinLfVGptgDmowtD3--LIPdota4ySWKaSpkAaxShbFDBUJYCeKWJSkt-lzoMqjNNgvoFyuaiP9ZfUPrfbRej8CcJZJICOtURDvMhCYhRYgTG1KNkJoVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061905b87d.mp4?token=AFbwFEjJPSilrbUfY2eFiUwz30CQ6qCV8VRKzTZCxg0LMpMYMVWMttuTuR46gDei-KdmYM6j6Umx1N-er5fyMK-n7AK_6N3AK_ha6RIaOWAprEZigctjuvpPnSSTKPNyXVltaitgDAWRgtYIpSUTKjSN4cdQmaKsEs7JItvBgW8NOnrapstbxsec8qgXuZHKGRoHX2kctYm2UKWQ2u63AxDOcUpemJtIv415gdAh0Fvr8vNi0Ml72k2BTzuItk6cL6eAknHEB0LEZL00j2gMBs4oeosga1I7BwLKnn7mlWnR8ErLq65qctZwxQW4SaZvI89fMJZGkl3yWHAt6n3VbAaACyI75jzDqGl901eEmLUzdFeVbV1-jg9y9aTqtFpPVzjLrn74TDW-cWQudR98gjFQ9AvyRwWStpTroO-j3uVJDvGMKNGhPpc6EUYT19i8cgSR4r4qYEhogJMu8Ow3L1ZPOjl-cZ5xl0b8q5xOtIMfFM1s1EuGrq0cCBfqjkkWbnZjn666X144-2ToqOabCp16j2RpcfcAEGSOqprsb5orgqAuoiyxGxskinLfVGptgDmowtD3--LIPdota4ySWKaSpkAaxShbFDBUJYCeKWJSkt-lzoMqjNNgvoFyuaiP9ZfUPrfbRej8CcJZJICOtURDvMhCYhRYgTG1KNkJoVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا ایران است
🇮🇷
🔹
این تصاویر بخشی از زیباترین مکان‌های دیدنی ایران است
😍
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/693325" target="_blank">📅 09:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4VySt6mbwT1NPlaBpFBjfkUDLuTtJlc2i_SM44kWEH3UzsaNpG2v36hQLvh4OzKWAxcWsCfZlw0r45AzCwDYjb_coWxiaoz6UkImvkNxkZEAF5eU9Tu2b42lzq_FBRirfaEt13KOZhxU_0nZvKssb5l0BtWM3Y88Or3wSntHlkr4TwIaXh5qSNTQj19HsvR26pWf9PSVCnR8lrc5-Grm7MEaEOZAa-xwSnYApImKP2puN5btDJNbEVl9t487E8bhABSqGyG06mJIaxn0tOkOTeaREolUayrBPZ_iKXD_Kku5CrFQPeinF4WKcg27FAuKTsFgliMruI4HZPPLwGJH1nY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4VySt6mbwT1NPlaBpFBjfkUDLuTtJlc2i_SM44kWEH3UzsaNpG2v36hQLvh4OzKWAxcWsCfZlw0r45AzCwDYjb_coWxiaoz6UkImvkNxkZEAF5eU9Tu2b42lzq_FBRirfaEt13KOZhxU_0nZvKssb5l0BtWM3Y88Or3wSntHlkr4TwIaXh5qSNTQj19HsvR26pWf9PSVCnR8lrc5-Grm7MEaEOZAa-xwSnYApImKP2puN5btDJNbEVl9t487E8bhABSqGyG06mJIaxn0tOkOTeaREolUayrBPZ_iKXD_Kku5CrFQPeinF4WKcg27FAuKTsFgliMruI4HZPPLwGJH1nY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه واردات کالا به کشور در شرایط جنگی سرعت گرفت؟
🔹
محمدحسین مصباح، فعال اقتصادی: سیاست‌های پیشین ارزی در کشور، تجار را برای واردات کالا زمین‌گیر کرده بود.
🔹
اما بانک مرکزی با ورود به‌موقع و اصلاح یک رویه غلط، گره کور تجارت را باز کرد و دغدغه دسترسی به کالا در شرایط جنگ و محاصره برطرف نمود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/693323" target="_blank">📅 09:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50fbe3f8e.mp4?token=rZ-WqUvwjEWZV1BCsDKz1C4mTKlxAtWejtNCDo_9SDLpfy799UpZ2tAS9oWLlRGRo99JG1hR7z8_5m0U992m_NQmuqqlkaaJfHfq8w4fBad8MQNdDgHF6RMCsSBt6IlYjUrvixcwUsG9nM2E2C-Hlx8Ky9mHJh5222wjVFBQRxvZTRdjWWNhq0y1448eh8iLl4X6ELItKUsZjCYX_T7xkgl6i4zuwHweTOF6mMO9f_PBin3jvNfXBq1df_dA6AJYvEQzg96hADgu10om8VmozdiMShVDaKURLq4sWJgCMZveQkj5ns25xOeRsBVkB3WCSH7LHAP9ug4f-JWEe1WsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50fbe3f8e.mp4?token=rZ-WqUvwjEWZV1BCsDKz1C4mTKlxAtWejtNCDo_9SDLpfy799UpZ2tAS9oWLlRGRo99JG1hR7z8_5m0U992m_NQmuqqlkaaJfHfq8w4fBad8MQNdDgHF6RMCsSBt6IlYjUrvixcwUsG9nM2E2C-Hlx8Ky9mHJh5222wjVFBQRxvZTRdjWWNhq0y1448eh8iLl4X6ELItKUsZjCYX_T7xkgl6i4zuwHweTOF6mMO9f_PBin3jvNfXBq1df_dA6AJYvEQzg96hADgu10om8VmozdiMShVDaKURLq4sWJgCMZveQkj5ns25xOeRsBVkB3WCSH7LHAP9ug4f-JWEe1WsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترمز ماشین برید؟
قبل از هر کاری این روش توقف اضطراری خودرو را یاد بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/693322" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwrjwbZw9R90wPIFwFlz7t0EaKIn3QfaXxihgKqGW5F6fRpiSxNtHF1jyhgOtwHB2p0AydkpwjGpz3xZLOYNhD1ChL3uVPCHtuH2dz0wa-2szkUOKfeY8Brpr1W9pmYos30C8VsdGxaPRPpOpu_RjvUvsqdmMIPOc9Tj3u8erpqiftYyQUvtXuT91DsoN-F4rm7iohrWcBQiazYRp4agn926ge1nAZ-wUy22WfWVcJtseQr0nDuHycct6U2Tvxw9mpGVQcVgXvIQa8NQCT1LpX0tpjKfpUz2Ll_Os4Erh_9t2VR6ePGKr_I4ogmcgx_ZR3kgGIigXgSxr-YCPjCs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه خبرگزاری روسی راشاتودی درباره میزان حضور مخاطبان در سخنرانی پزشکیان و نتانیاهو
🔹
سالن سخنرانی پزشکیان مملو از جمعیت بود؛ در حالی که سالن محل سخنرانی نتانیاهو به‌زحمت نیمی از ظرفیت خود را پر کرده بود. سوال مهم:
واقعاً چه کسی منزوی شده است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/693321" target="_blank">📅 09:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه هفتم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه هفتم؛ ولایت پروردگار
🔹
تکرار و تدبر در نام‌های پروردگار باید در عمیق‌ترین لایه‌های خیال و سلول‌های بدن تثبیت شود تا فرد حس استواری و قدرت الهی را با تمام وجود احساس کند.
🔹
اتصال به نام «الْوَلِيّ» مانند یک قطب‌نما عمل کرده و به صورت شهودی، دوستی با اهل حق و دوری از اهل باطل را در دل انسان نمایان می‌کند.
🔹
پذیرش ولایت «اللَّه»، انسان را هم‌زمان به بندگی حق و رهایی از تمام قید و بندهای باطل و تاریک می‌رساند.
🔹
تکرار و اتصال به نام «الْوَلِيّ»، حصاری نفوذناپذیر در برابر انرژی‌های تاریک، کدهای ابلیسی و افکار منفی ایجاد می‌کند.
🔹
انسان شبیه به کسی یا چیزی می‌شود که به آن دل می‌بندد؛ بنابراین، انتخاب‌های او در دوستی و الگوپذیری، تأثیر عمیقی بر زندگی او دارند.
🔹
دوستی حق، فقر، رنج و بیماری را از وجود انسان‌ها و سرزمین‌ها پاک کرده و برکت، عشق و فراوانیِ الهی را جایگزین آن‌ها می‌کند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/693320" target="_blank">📅 09:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=RAgD4lQaL_uHJB_GL9K9pFb4Ss0p9RzBeusQ5qnwfSaym0MK1P-v21qxqYKPm5c-mlHFUjCZF024iy82s5WSXXy34FtigB6F3OAsthNz3MPBcVSb1DuvBg9p3meCjGjLWlcNgHUJPU7LnR5x-SI7AL3Ttu1qtVszX4W2Qe6x94IKBbI_9_OxTDwXB_pCsgRG3okNHfGUdF3dyWG06ZbiZNwMMnoWT9EZv34GUbHCTR7G5Q4KGqBbzGaqTtoOthitQFmSiON4DNPciipGz9cj3U_GamnOin2fXyy3qhABWaycsc3QPNeVZAPY7tIEwrdRyjH4PxlenSjC1RIgyVZM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d4b39765.mp4?token=RAgD4lQaL_uHJB_GL9K9pFb4Ss0p9RzBeusQ5qnwfSaym0MK1P-v21qxqYKPm5c-mlHFUjCZF024iy82s5WSXXy34FtigB6F3OAsthNz3MPBcVSb1DuvBg9p3meCjGjLWlcNgHUJPU7LnR5x-SI7AL3Ttu1qtVszX4W2Qe6x94IKBbI_9_OxTDwXB_pCsgRG3okNHfGUdF3dyWG06ZbiZNwMMnoWT9EZv34GUbHCTR7G5Q4KGqBbzGaqTtoOthitQFmSiON4DNPciipGz9cj3U_GamnOin2fXyy3qhABWaycsc3QPNeVZAPY7tIEwrdRyjH4PxlenSjC1RIgyVZM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: از امروز برای شمال کشور بارش برف و باران و برای گلستان و شمال‌شرق سمنان هشدار نارنجی سیلاب صادر شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/693319" target="_blank">📅 08:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862b79e23.mp4?token=W4ytMm-55U4OTZRusksZ6FuHSuo6CRpFApN6xIn5_-29fEiGCGylKk0pLS0-z3LDAZxMrpJJI2yEeYKc3f_LZEDeihPmFKVBBn50PSMCxMm3CG3oYLChaea0FbEUkNFXDn3s7_hHHzXN5QZoukYibNbcdPTxjOENhaiPC6gQqRdoSf4ppkd04bRSm52e-aOKtFYWcVy9N6hGVVul46HEgNmppHz-ZJ728uBQfYIyyI3eNRtxqye4RgNVVibIwHFkhFKBBw61pwOWoZZebI9OwAmoa4c2WvwceHQ3eb3QyV4l48xYYThDFolpoLbm04MzWNxGpbrrL5yG1J3bULL5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862b79e23.mp4?token=W4ytMm-55U4OTZRusksZ6FuHSuo6CRpFApN6xIn5_-29fEiGCGylKk0pLS0-z3LDAZxMrpJJI2yEeYKc3f_LZEDeihPmFKVBBn50PSMCxMm3CG3oYLChaea0FbEUkNFXDn3s7_hHHzXN5QZoukYibNbcdPTxjOENhaiPC6gQqRdoSf4ppkd04bRSm52e-aOKtFYWcVy9N6hGVVul46HEgNmppHz-ZJ728uBQfYIyyI3eNRtxqye4RgNVVibIwHFkhFKBBw61pwOWoZZebI9OwAmoa4c2WvwceHQ3eb3QyV4l48xYYThDFolpoLbm04MzWNxGpbrrL5yG1J3bULL5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبرد انسان و حیوانات در ماراتن ۱۰۰ کیلومتری؛ این‌بار برنده یوزپلنگ نیست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/693318" target="_blank">📅 08:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
خبرنگار اسرائیلی: حملات دیشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/693317" target="_blank">📅 08:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693315">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: تیم‌هایی به نقاط مختلف جهان اعزام شده‌اند تا از کشورها بخواهند علیه ایران اقدام کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/693315" target="_blank">📅 08:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693314">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949dc40c1e.mp4?token=REfuuVLwqdNa1tbjDEQIadUpUp5vHhd39dQ5jTwaeZ85E4EJ9DSojN12j9KL6HH4h6qHvfGRmKqx7huYWzukINDt4caJjR_pbgXQHWci2K59WDsVwqKfXOLdlkeJ3vLb0yNH4hgG_-WGR0ucLVZNmJLwU2gPWc90qkTAYe28o4nWeqWD2pAnwnnScOmcMEEBpt1IqIy5w6mxII-zwcKbmUQ3oDK0b8t4SweiHiUJHEZe9iybFQjxybMx3qjIayTAjApBkSt0MHiVyj45uO8DsINdYO65i7sDPmzVVS8sNwwGU248VyrfWTsrdFfqLbdjAT-Buth9qilwrrNIv7qWviCvz_dthDNhza20v77m8QPxCIfAi7TRDjz4jAl3zFdLZoTyrJyo4o0rh0m8rSQjjBgUMbopzZ4Gv8ljNPrhMgFSo266Wx3ii-zifK33Ew48u7sFcXG14Cz0hFm9_7NaRZW2q8TcCxJijelAF9JoT122qp830ghBERabwL_8UGJDRb6RhWGEoS-rCKgMro3SeDkivdpuer7agT0E_ic-4xkptxhJq_iBr7qIVvPMGOCxSVu8T55h-MlnqNrqibo7JHenWJZ0skU7xocH6kEl2TIdbf9htrrn3giAtJbFhFXr5EMi14Fw9YOGxYvrPi_kE2CFRVNiSTBqKwvbqRFeKZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949dc40c1e.mp4?token=REfuuVLwqdNa1tbjDEQIadUpUp5vHhd39dQ5jTwaeZ85E4EJ9DSojN12j9KL6HH4h6qHvfGRmKqx7huYWzukINDt4caJjR_pbgXQHWci2K59WDsVwqKfXOLdlkeJ3vLb0yNH4hgG_-WGR0ucLVZNmJLwU2gPWc90qkTAYe28o4nWeqWD2pAnwnnScOmcMEEBpt1IqIy5w6mxII-zwcKbmUQ3oDK0b8t4SweiHiUJHEZe9iybFQjxybMx3qjIayTAjApBkSt0MHiVyj45uO8DsINdYO65i7sDPmzVVS8sNwwGU248VyrfWTsrdFfqLbdjAT-Buth9qilwrrNIv7qWviCvz_dthDNhza20v77m8QPxCIfAi7TRDjz4jAl3zFdLZoTyrJyo4o0rh0m8rSQjjBgUMbopzZ4Gv8ljNPrhMgFSo266Wx3ii-zifK33Ew48u7sFcXG14Cz0hFm9_7NaRZW2q8TcCxJijelAF9JoT122qp830ghBERabwL_8UGJDRb6RhWGEoS-rCKgMro3SeDkivdpuer7agT0E_ic-4xkptxhJq_iBr7qIVvPMGOCxSVu8T55h-MlnqNrqibo7JHenWJZ0skU7xocH6kEl2TIdbf9htrrn3giAtJbFhFXr5EMi14Fw9YOGxYvrPi_kE2CFRVNiSTBqKwvbqRFeKZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: آقای الشرع، یهودیان از زمان موسی در بلندی‌های جولان حضور داشته‌اند؛ می‌توانید در کتاب مقدس بخوانید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/693314" target="_blank">📅 08:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693313">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38043922b9.mp4?token=JaIk9I4La_MNET0l-1O9Q6Q1fnLf5t7D0oSo4wy99zOxpXwR6A-oMwhxC-M6Xs1knfFxulAF2C1QjAmAR1OgsieQAtteNRIPkcI59YnHBtCjZVyt52xYS3nm0JORdkF9_fEGnfRyT9crqX5nVN7NkrHxAOmKAgCL2Waj37O7NFdmhbECzEVaYGeMZFiWsCw5KXz_2rSMqfo3vZgc_wkSKD_i-tX2E0iePyep1yFxe2g3Boew-XZn4uxJaLGfvT7WDZ7AHc31NI-CXgNHLQSTqDFGhwJ7Rp5h6dRVBTQm3utdaPn61mQNmqe9FvipxUlKy7eEm5-jnoxnon3UW7wCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38043922b9.mp4?token=JaIk9I4La_MNET0l-1O9Q6Q1fnLf5t7D0oSo4wy99zOxpXwR6A-oMwhxC-M6Xs1knfFxulAF2C1QjAmAR1OgsieQAtteNRIPkcI59YnHBtCjZVyt52xYS3nm0JORdkF9_fEGnfRyT9crqX5nVN7NkrHxAOmKAgCL2Waj37O7NFdmhbECzEVaYGeMZFiWsCw5KXz_2rSMqfo3vZgc_wkSKD_i-tX2E0iePyep1yFxe2g3Boew-XZn4uxJaLGfvT7WDZ7AHc31NI-CXgNHLQSTqDFGhwJ7Rp5h6dRVBTQm3utdaPn61mQNmqe9FvipxUlKy7eEm5-jnoxnon3UW7wCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماهنگ جدید محمود کریمی به زبان انگلیسی منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/693313" target="_blank">📅 08:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693312">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پکن: روسای جمهور آمریکا و چین توافق کردند که «هیچ کشور یا نهادی نباید بابت تردد در آبراه‌های بین‌المللی، عوارض دریافت کند»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/693312" target="_blank">📅 08:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693310">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7JpiPZrz4EHeG5i04wL3tU2W9cqOqRzgLWCurgAv3gLA_XB-eCMBkEudai10Iyg2dUnnm3JmI4AaEt6oeSI74v1sOtVU1P6UdgqV7Y93Ct-RKer-XqdexSzaQh5x32agzMOKX17UVeR6C4tH12phulJp8qaveRdDAH6ljPbNwLT5LtASzPjRYWmIzudVbTRqCweYsE2u6iFuhAB-uglkMjm0DwHtd3e1XbOaHnyvNr7UrOjqXESrnlsvJSO1Xs8FIZj24JOg3stuv7IqTbmTuLYY-oLeqarwu6dXw1ROfIboI1UYSUNgozAoXFlpuYk1p1tP9-ajBWLRfS6CmhgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgDjD1HWwmgAKbT7iEV7Vc97PkYe_T5MT_URR4S2jDHJe25lc5Lba-iFcRo2RjiFTrdOnYWSHj36z-rF7AjRp6rf9eJMIzfP_aXly3KZo6sdNo_hUCNNZ0ooA2_Ja0se8-Y8H9qmEwiyfdc5ruO3bWQhd1kEdLLkPiGRX4sRHlteug92ohmQRmGD3GDhPicneiwv8JjzXx6g6QUDJBBBIrfwWowwk3ScX3duF0s7IMCOGmMiK34IZF3KjMAHMe4MYL5LTYfpIylAJbikCXMMfSPfTH-m_PejRHVBZHkWxGSDbvaZXo-u383V-z4-IF2bvNy8H4Vdqd0Jv7dJe2zDug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار نهاد مدیریت آبراه خلیج‌فارس به مالکان کشتی درخصوص تردد از مسیرهای نامعتبر
🔹
در راستای این هشدار ایمیل عذرخواهی مالکان کشتی‌ها بخاطر عبور غیرمجاز کشتی از تنگه هرمز دریافت شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/693310" target="_blank">📅 08:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693309">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d88a96cd.mp4?token=XLurf3QGzYwJUQuo9KMl8XG-3_L2kaM3Rmkk3koWMBrt4VdOtzrTgfLS3LDX3qUr71ieyJyx0uABIyNBaK_Mmzsk4qJDAkTv5fb8B4ka-RGQtNKLYhVK2BpsQhUoUvwvhbTvi_VqY3BlhMzfaVJC7POrLPz6TYNjCuWs23bCHxhMBFnufqYlOrpBfq76tPkQiESHOPIcocrNpyUhcsCzKfgUBYy-I2tI-iGVzrB_LeTGh95B5MJxeNMkM9NJxM58TvzOhJRfooI7MH-2zUOmgX6mUfGZEIS8luyVc95B23fyYmoEbVzzapaO6kpfli0eVWvuc0D-HdMNZy-vfJOqE7ucZwGg0MWhYFuoLAAiLLLoza_y35ghMTb3fOWvg6iqVBqCl7KM-BUPTws4CB-djlTf58suTF0mlgQhEnpoMjRCRKADJLl90Qq4-zewflmQOnM0tfwr8JNzzYw__-eLE3FfqT-zOVjf3uDSrQ5mY-ttMihNY5BRLdxZ4mB7IFHT8TTmvqI6vFO0IPjNVAhPT7IM2oQwikwCnlx46hJ8oDv9cFrZLK0OqBq9vlehQPYce3oP_Vx1hVB_lgdxSxw5YfYwy_D54ECbR-HfGl_fh6-Gq3ipbmP6NJ8-_eGt17GGxaXIb5d8-afakHjko1Y96y_tR8a_beK_Ii1MQYsM6rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d88a96cd.mp4?token=XLurf3QGzYwJUQuo9KMl8XG-3_L2kaM3Rmkk3koWMBrt4VdOtzrTgfLS3LDX3qUr71ieyJyx0uABIyNBaK_Mmzsk4qJDAkTv5fb8B4ka-RGQtNKLYhVK2BpsQhUoUvwvhbTvi_VqY3BlhMzfaVJC7POrLPz6TYNjCuWs23bCHxhMBFnufqYlOrpBfq76tPkQiESHOPIcocrNpyUhcsCzKfgUBYy-I2tI-iGVzrB_LeTGh95B5MJxeNMkM9NJxM58TvzOhJRfooI7MH-2zUOmgX6mUfGZEIS8luyVc95B23fyYmoEbVzzapaO6kpfli0eVWvuc0D-HdMNZy-vfJOqE7ucZwGg0MWhYFuoLAAiLLLoza_y35ghMTb3fOWvg6iqVBqCl7KM-BUPTws4CB-djlTf58suTF0mlgQhEnpoMjRCRKADJLl90Qq4-zewflmQOnM0tfwr8JNzzYw__-eLE3FfqT-zOVjf3uDSrQ5mY-ttMihNY5BRLdxZ4mB7IFHT8TTmvqI6vFO0IPjNVAhPT7IM2oQwikwCnlx46hJ8oDv9cFrZLK0OqBq9vlehQPYce3oP_Vx1hVB_lgdxSxw5YfYwy_D54ECbR-HfGl_fh6-Gq3ipbmP6NJ8-_eGt17GGxaXIb5d8-afakHjko1Y96y_tR8a_beK_Ii1MQYsM6rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از نخستین لحظات جست‌‌و‌جو تا رسیدن به پیکر مطهر شهید سید حسن نصرالله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/693309" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
ترامپ: من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/693306" target="_blank">📅 08:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693304">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQO1MRMBBScvyQjTGNoPpMVWFPDC_wNZM4484kxPIjG3XytF6RQ_LW5quWxenw_gJMK4Gh1kdrOVaD9YdKQyr6yR_ckGX6Kti_vAJUO3owyhKOFig577d3turkMOOz-ZhF2PC9U7WhKb2kXntKv72SX0P3zECkTsVanCnAQTsHXfbmhbWNO5JKulEm4VRU98KW-59Hd5VydUE-iO5Nq_V0k4TMXbETeAKusSTCkAWzhJbKblNYLQuGxG8hKmYepehpBcwNo3i0BQaDbsWgC-cr0P_0HuIaMRJm-heWcAqfb3iKpVTNsBM3qn83MYlFnca8-tZIoiXCi67K9m371D2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۵ مهر ماه
۱۵ ربیع‌الثانی ۱۴۴۸
۲۷ سپتامبر ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/693304" target="_blank">📅 07:53 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
