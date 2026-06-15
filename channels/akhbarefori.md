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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.54M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 06:22:01</div>
<hr>

<div class="tg-post" id="msg-659612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔶
فراخوان کمک برای یک بانوی مبتلا به سرطان
🔸
خانمی جوان مبتلا به سرطان سینه از یک خانواده نیازمند دارای همسری کارگر و مستاجر می باشد که تاکنون۹۰ میلیون بابت درمان  هزینه کرده است.
🔸
برای ادامه درمان و انجام شش جلسه شیمی درمانی نیازمند ۳۶ میلیون تومان است
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/akhbarefori/659612" target="_blank">📅 04:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJeEpwXyTC8m6BffvWxx3P9LbgGF22bTO7VSrV7ddGQ2H0j93tmfL8dbFbkaeC7KzKFUdqNgwhU7NJBS-9gcNOsaFLM9ys6bk8z_UbPNWamv7Aii23l9ii1FRn7MPBYaaAjRitSoaa-Y4C_IhsIOZ9UithC5_KAUKNkSUr0RAFrDYSHucPdz8psL2q4nit644_lwD7X56JpRz6YwQrLdZphQFkBJ6CTv4-zhj06XZnE1Lh5ddS83yY2YzWqdUPOwjLjnb70sXNmqere1uw9odIw6DQhX0hwjYZ32v0YY66e0XfzjjzcN9ZbnP7Cfsitm_XC0rmWyOQlBmSeBf3HMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: فاذا فرغت فانصب. هیچ وقت هم نباید خسته بشویم. شنیدید آیه‌ی قرآن را «فاذا فرغت فانصب»؛ وقتی از کار فراغت پیدا کردی، یعنی کارت تمام شد، تازه قامت راست کن، یعنی شروع کن به کار بعدی؛ توقف وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659611" target="_blank">📅 04:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f03eff7c.mp4?token=eI-hAKMivYpoNuD7SFhPdwDUGd_lLouA0l_sM2BRbxlLNXPF69a0o92OHLpBxYauXuJuN9nYGPJactI4SShATOb2D8QIvpk07FnMPhHfg-AxjrB1xYccQdvA1g53ItwS4dM_u18Qt-q8DuCmxYTlEWsrgKDrE5ObpHtyIqwAqUTqtaL-pqCjlN33EuFZRKFgw0jUhKgi45f-iL9oztRPV-rr667-887kh4Lnk3Xxlq-Bmoz7foNgVNX3kPLuW_KHLuqCdgU1BtPmrws-lS68LzDshgtbImS94jMxYwe5IQNiEprTJ3h-LnhufXr9WURpcG4VCxRw1kumb8OmWsvxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f03eff7c.mp4?token=eI-hAKMivYpoNuD7SFhPdwDUGd_lLouA0l_sM2BRbxlLNXPF69a0o92OHLpBxYauXuJuN9nYGPJactI4SShATOb2D8QIvpk07FnMPhHfg-AxjrB1xYccQdvA1g53ItwS4dM_u18Qt-q8DuCmxYTlEWsrgKDrE5ObpHtyIqwAqUTqtaL-pqCjlN33EuFZRKFgw0jUhKgi45f-iL9oztRPV-rr667-887kh4Lnk3Xxlq-Bmoz7foNgVNX3kPLuW_KHLuqCdgU1BtPmrws-lS68LzDshgtbImS94jMxYwe5IQNiEprTJ3h-LnhufXr9WURpcG4VCxRw1kumb8OmWsvxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب توافق ایران و آمریکا در رسانه‌های جهانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659605" target="_blank">📅 03:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pIlQVsTsiJFy5-31Lqhz58fT-QpSgWahdmTzKBZ8Z-OEOFREoL5o4FXCWraOolYQJJz6affxC1QZRyKw-NPuK6mPpGUUi-9jvaKOJWC_cTEsEcre_ULnu6_AjDjpgwKH1w_8O0WSWAsYrj16YNOPT_VryQZiNWyz95udCcx-s2NedIRWoRAkvhhRzc1__8RONdB6dzJpzm_ugwNSUJX1lO5PO0JUeUxPB3uG4UTwO8s9r5F5mWdi9BFFlOAdNVVKA3-Ksg_dm2CWaQK0it9dpVRKGcTuhQrZdGZUXxxW1b7UovUP2cHr2oNy_DgI6Bc8DHbc1m2jNfXFHkJk7iplyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فیدان به یادداشت تفاهم ایران و آمریکا
وزیر امور خارجه ترکیه:
🔹
از توافق میان ایالات متحده و ایران استقبال می‌کنیم و آن را گامی به سوی صلحی پایدار در منطقه می‌دانیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/659603" target="_blank">📅 03:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
هیات قطری پس از ۱۷ ساعت مذاکرات فشرده، ساعاتی پیش تهران را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659602" target="_blank">📅 03:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خبرنگار المیادین: رژیم صهیونسیتی با حمله توپخانه‌ای، شهر النبطیه و شهرک کفرمان در جنوب لبنان را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659601" target="_blank">📅 03:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a44d4e47d.mp4?token=YVjjx6PTxXPxd3xmObooYgc4ruPppMH4p1DK317FPTYJ0fBekktnWKYUQg0vv7JgggPUkbB2VffYrgEnXRatmV-bofQYtBbGM8aHJYn-18oQSblDUn2j7bKjtJb9Itu__F8YHtL8b6g--vhXtN4fO8ZpFEKLkfYtybCV2It1QHPyYHhyfPs5Tnx-LS0LBerqmXu8EVZZ6soub2rlBhwiV0i5gMEJTjh9m2Y1XSVQtX4ejiDbi7normTHZxHSVcQjpCYN8nmuq9thtiYxTR-4Blw2-NiysVDw4Ak6dXZTHnoZFij4zV0EGX_QYiBlpwFL7U_6t09NAdKl8lAjpLN-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a44d4e47d.mp4?token=YVjjx6PTxXPxd3xmObooYgc4ruPppMH4p1DK317FPTYJ0fBekktnWKYUQg0vv7JgggPUkbB2VffYrgEnXRatmV-bofQYtBbGM8aHJYn-18oQSblDUn2j7bKjtJb9Itu__F8YHtL8b6g--vhXtN4fO8ZpFEKLkfYtybCV2It1QHPyYHhyfPs5Tnx-LS0LBerqmXu8EVZZ6soub2rlBhwiV0i5gMEJTjh9m2Y1XSVQtX4ejiDbi7normTHZxHSVcQjpCYN8nmuq9thtiYxTR-4Blw2-NiysVDw4Ak6dXZTHnoZFij4zV0EGX_QYiBlpwFL7U_6t09NAdKl8lAjpLN-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود اتوبوس تیم ملی فوتبال ایران به هتل محل اقامت در لس‌آنجلس با تدابیر امنیتی ویژه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/659600" target="_blank">📅 03:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659598">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سعید آجورلو عضو تیم رسانه‌ای هیئت مذاکراتی ایران: به دلیل بدعهدی طرف مقابل، با یک تفاهم چندمرحله‌ای روبه‌رو هستیم تا گام به گام پیش برویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/659598" target="_blank">📅 03:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659597">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با نیویورک‌تایمز: اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به عنوان نگهبان منطقه قرار خواهم داد
🔹
حملات اسرائیل تقریباً توافق نهایی با تهران را از مسیر خود خارج کرد.…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/659597" target="_blank">📅 03:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نیش ترامپ به نتانیاهو: او باید از ما سپاسگزار باشد!  ادعای ترامپ در گفتگو با نیویورک‌تایمز:
🔹
تصمیم برای حمله به ایران در اواخر فوریه و اعمال محاصره دریایی، بعداً خاورمیانه را به نفع منافع آمریکا تغییر شکل داد.
🔹
کنار آمدن با نتانیاهو فوق‌العاده دشوار است…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/659596" target="_blank">📅 03:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با نیویورک‌تایمز: توافق با ایران در نهایت تضمین می‌کند که تنگه هرمز برای همیشه بدون عوارض باقی بماند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/659595" target="_blank">📅 03:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw0sRVnpkT-ZvRqBguhUrDAsQsbA9aqDEUeQpytgqlRG2AueIlOBODcQsoz1OgFXGnqAVq344zsjFlzetsDfMQ_SGXF4Vf2PqWQLcaA0eAqiT5ugGVc6am3yyiEmR0KTgLJJotSzVGwFI_W8GhiTPGBV7nIi0s1PSZKC-LqNTd8dUCs0Ac9zdNnnPd-zcUWnU_5FsmO8XlbUN1sc68yScOGpJ601tT-pW702g-D9lNfye8COnM4fyu4yUu_OGCZ49NWiqlUrfnuviq1rtrQ5DVxerdASEo8RtMLxuKIQ8q2UnvAU54mLl7vOBP2b3zWVQGK4FOxOPN29o0mhdq_4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس: تفاهم احتمالاً منطقه را به وضعیت پیش از جنگ بازمی‌گرداند؛ اما با این تفاوت که ایران اکنون با توانایی خود در تأثیرگذاری بر کشتیرانی تنگهٔ هرمز، به اهرم فشار جدیدی دست یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/659594" target="_blank">📅 03:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTGbWxjCgrT7VyVYbZ0psArBieCOZZF6cATkCdaClLW0fOfth6fpQyOlkZm1p208CZ8BLRmUlRC3-3KJ7I6dedWFiT_nqdMtG9A9WqVoJxqkrPUF-_4YQWYIuT0wDmTW6HYhQbFtP2ouuARGRPNacNs3cYB8MaNleHbXK_Exw7ryyeFs0rlwcAfz8T2AUfYTuilmUkYCYDAbr4zplawlEmy8ttPh-pnhxIsfuvfXrdKmtP4VuFYyH-Y_H5IzuIOGPiWxTmtH6-J_38BEEYFAuM2EmO3-9CzyEIURlul2FbndUBPRw81NSuz3C_87ECtvH8inuzyb0a62OUz-rAoRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندسی گراهام: از شنیدن توافق با ایران برای باز شدن تنگه هرمز خوشحالم
🔹
طبق قانون ما، هرگونه توافق هسته‌ای با ایران برای بررسی و رأی‌گیری به کنگره ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/659593" target="_blank">📅 02:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659592">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با نیویورک‌تایمز: توافق با ایران در نهایت تضمین می‌کند که تنگه هرمز برای همیشه بدون عوارض باقی بماند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/659592" target="_blank">📅 02:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659591">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
غریب‌آبادی: دو اقدام فوری از همین لحظه
معاون وزیر خارجه:
🔹
دو اتفاق فوری از بامداد امروز رخ می‌دهد؛ اول پایان جنگ در تمام جبهه‌ها از جمله لبنان و دوم، رفع محاصره دریایی./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/659591" target="_blank">📅 02:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659590">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ماجرای تغییرات لحظه آخری یادداشت تفاهم ایران و آمریکا چه بود؟
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
پس از آنکه روز شنبه کلیات  یادداشت تفاهم در شورای عالی امنیت ملی تصویب شد، از صبح یکشنبه با ورود تیم قطری، برخی مسائل باقی‌مانده مورد بحث قرار گرفت. به نظر می‌رسید که این مسائل لاینحل بمانند تا اینکه حوالی ظهر امروز، اسرائیل به منطقه «ضاحیه» حمله کرد و عملاً از خطوط قرمزی که ایران تعیین کرده بود عبور نمود.
🔹
در این لحظه، ایران آماده می‌شد که از چند جبهه، حملات گسترده‌ای را به سمت رژیم صهیونیستی آغاز کند و مذاکره به سمت تعطیلی پیش می رفت. اما با ورود مجدد ترامپ و امتیازهایی که در ازای عدم حمله ایران به اسرائیل ارائه شد، تیم مذاکره کننده قانع شد که این توافق در راستای منافع کشور و منافع مردم لبنان است.
مهم‌ترین تغییرات لحظه آخر عبارت بودند از:
🔹
برداشته شدن فوری محاصره دریایی (به جای بازه ۳۰ روزه که قبلاً توافق شده بود)
🔹
پایان جنگ و عملیات نظامی در همه جبهه ها و همه مناطق لبنان و ضرورت احترام به تمامیت ارضی این کشور
🔹
نهایتاً این رایزنی‌ها تا ساعات پایانی شب یکشنبه ادامه داشت. در حالی که همه چیز برای حمله به اسرائیل آماده بود، با تمکین آمریکا در برابر خواسته‌های ایران، عملاً موانع امضای یادداشت تفاهم برداشته شد و قرار شد روز جمعه این یادداشت تفاهم امضا شود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/659590" target="_blank">📅 02:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659589">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نشست خبری سرمربی تیم ملی فوتبال ایران و مهدی طارمی
امیر قلعه‌نویی ایران:
🔹
خیلی خوشحالم از کشور بزرگ و قدرتمند ایران اینجا حضور دارم و امیدوارم فوتبال وسیله‌ای شود که کشورها و فرهنگ‌ها به هم نزدیک شود و خوشحالم که از طرف کشور و قدرتمند ایران اینجا حضور دارم.
🔹
ما اینجا هستیم که به نمایندگی ملت بزرگ ایران بازی کنیم. فقط به فوتبال فکر می‌کنیم. ما سیاستمدار نیستیم و فوتبال از سیاست جداست ولی همه ملت بزرگ ایران برای ما قابل احترام هستند.
🔹
بخاطر مشکلات کمپ ما دو بار جا به جا شد اما جا دارد از مردم و دولت مکزیک تشکر کنیم. ما ایرانیان از سختی‌ها فرصت درست می‌کنیم. به غیر از شادی مردم کشورمان به چیز دیگری فکر نمی‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/659589" target="_blank">📅 02:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659588">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مذاکرات نهایی با اجرای کدام بندهای تفاهم‌نامه شروع می‌شود؟
منبع مطلع:
🔹
بر اساس بند سیزدهم تفاهمنامه، مذاکرات برای توافق نهایی پس از امضای تفاهم‌نامه و راستی آزمایی اجرای بندهای مربوط به رفع محاصره دریایی، شروع روند بازگشایی تنگه هرمز، آزادسازی بخشی از اموال ایران و اسقاط تحریم‌های ایران در حوزه فروش نفت، پتروشیمی و مشتقات، آغاز می‌شود./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659588" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بیانیه مشترک رهبران بریتانیا، فرانسه، آلمان و ایتالیا: ما از یادداشت تفاهم بین واشنگتن و تهران استقبال می‌کنیم و به همه میانجیگران، از جمله قطر و پاکستان، تبریک می‌گوییم
🔹
ما آمادگی داریم در پاسخ به گام‌های واضح و قابل‌راستی‌آزمایی ایران در مورد برنامه هسته‌ای‌اش، تحریم‌های مرتبط را لغو کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/659586" target="_blank">📅 02:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
یک نکته مهم از اصلاحیه ترامپ با فشار ایران؛ بازگشایی محاصره دریایی آغاز شد؛ بازگشایی تنگه بعد از جمعه
🔹
ترامپ، ابتدا در پیام خود در شبکه‌های اجتماعی نوشته بود که از این لحظه هم محاصره دریایی ایران پایان می‌یابد و هم تنگه هرمز بازگشایی خواهد شد.
🔹
با این حال او دقایقی بعد با تاکید و فشار ایران، سخن قبلی خود را اصلاح و تاکید کرد که بازگشایی تنگه هرمز بعد از روز جمعه (روز امضا) انجام خواهد شد. او در پیام خود چیزی درباره تعلیق بازگشایی محاصره دریایی نکرده است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/659585" target="_blank">📅 02:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
برخی محورهای مهم بیانیه شورای عالی امنیت ملی درباره تفاهمنامه ایران و آمریکا
🔹
شورایعالی امنیت ملی، یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه ۲۴ خرداد ماه، نهایی کرد.
🔹
جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان می‌یابد
🔹
محاصره دریایی ایران بلافاصله به طور کامل خاتمه می‌یابد
🔹
امضای این یادداشت تفاهم در روز جمعه ۲۹ خرداد به طور رسمی انجام خواهد شد.
🔹
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/659584" target="_blank">📅 02:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فوری/ بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
🔹
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه ۲۴ خرداد ماه، نهایی کرد.
🔹
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
🔹
امضای این یادداشت تفاهم در روز جمعه ۲۹ خرداد به طور رسمی انجام خواهد شد.
🔹
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/659583" target="_blank">📅 02:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf836a8c5.mp4?token=VMtP_b_P_gt70GDDoIt-44wEIj2TTAecDQIry_wamfT21LZeKoo5Vg1k2G7D0VTJOi6Nm2zJUBtXTGCIbxAWRgWZMvykQCDLZiXQXjLf5UscbsuGMtGgK1OTx1E0FRrlj12iG6g_h7Yxi_vh_ph531Xh3StVe6KO-rYPr2yMH-fgBnIyGrOGB-U0zjaHyg1kXG7I1mGU7xYfQHHDHEbYjWklYFraqu5lb0IdeRJTJKDKWaQcfGeYEpPXOiax1PUA-AC3N4o_yG1FsLmzdRFXyq5t6-GfawZgiJBlI6qw_OSN7A_s1O6-xOegC407pQqZbsQ_jRNdjJiLxAk5zTjgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf836a8c5.mp4?token=VMtP_b_P_gt70GDDoIt-44wEIj2TTAecDQIry_wamfT21LZeKoo5Vg1k2G7D0VTJOi6Nm2zJUBtXTGCIbxAWRgWZMvykQCDLZiXQXjLf5UscbsuGMtGgK1OTx1E0FRrlj12iG6g_h7Yxi_vh_ph531Xh3StVe6KO-rYPr2yMH-fgBnIyGrOGB-U0zjaHyg1kXG7I1mGU7xYfQHHDHEbYjWklYFraqu5lb0IdeRJTJKDKWaQcfGeYEpPXOiax1PUA-AC3N4o_yG1FsLmzdRFXyq5t6-GfawZgiJBlI6qw_OSN7A_s1O6-xOegC407pQqZbsQ_jRNdjJiLxAk5zTjgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن و پایکوبی در خیابان‌های لبنان پس از اعلام توافق ایران و آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/659582" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس، معاون ترامپ: تا زمانی که ایران به تعهدات خود پایبند باشد، از مزایای واقعی بهره‌مند خواهد شد. اگر ایرانی‌ها به این توافق پایبند بمانند، این توافق خاورمیانه را طی ۵۰ سال آینده اساساً متحول خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/659581" target="_blank">📅 02:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCq_3gUk1052F5-lxBdHvXY65aWzW1R3otE1FkbMx38nDumRz4MsbSSv_TGyPr2mYypXjvA1iX6I4Gf3R5lwqSbnrn5myvGO0xE-ZAGjkUAn8PeLTd9wgnPilZm9xHGAruzVbgPIvo1y8Kx2802QSkOBRQ7hBp8Xhgzp0Qt4MgdxYTWHdNqlMr065j7l3vXf3dMqSpFX-Ix-nl7SfGJPSLxlxvJD79cuP2I-o39WSVxjC0k3i6tsrFbkrTd9SWssZVvl9i9VEXa98CcJbiDZbhMyhp3jIh13VQD7JE1mLYqazypkTOAF9q-G-3OCS__NhhwsXQZ9KACi7BYDd0gcZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باوجود تکذیب‌های پیاپی رسمی آمریکایی‌ها؛ نخستین محموله ۳ میلیارد دلاری وارد تهران شده است
🔹
براساس اخبار دریافتی، یک فروند هواپیمای اختصاصی اماراتی در روزهای اخیر با عبور از محدودیت‌های پروازی منطقه، در فرودگاه مهرآباد تهران به زمین نشست. این پرواز حامل نخستین محموله ۳ میلیارد دلاری از دارایی‌های ارزی ایران بوده است.
🔹
تصاویر راداری تایید می‌کند یک فروند بوئینگ ۷۳۷-۷JZ BBJ اماراتی (با رجیستر A۶-RJF) روز دوشنبه ۸ ژوئن (۱۸خرداد) پرواز مستقیمی را از ابوظبی به مقصد تهران انجام داده است.
🔹
طبق گزارش منابع موثق منطقه‌ای و بین‌المللی، این اقدام در راستای اجرای توافق مالی جدید میان تهران و ابوظبی برای حفظ ثبات اقتصادی منطقه صورت می‌گیرد.
🔹
با وجود تکذیب‌های پیاپی رسمی آمریکایی‌ها بر اساس بخشی از این مذاکرات، امارات متعهد به آزادسازی ۱۰ تا ۲۰ میلیارد دلار از منابع مالی ایران شده است که محموله ۳ میلیارد دلاری اخیر، بخش اول این تفاهم به شمار می‌رود. این اقدام نشان‌دهنده دست برتر ایران در اجرای گام‌های اولیه توافق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/659580" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خشم رسانه‌های عبری از اعلام یادداشت تفاهم بین ایران و آمریکا
🔹
کانال ۱۴ عبری: کاری که دونالد ترامپ با ما کرد آنقدر بد است که حتی توضیحش هم سخت است.
🔹
شبکه عبری آی ۲۴ نیوز: ترامپ به ایرانی‌ها خیلی چیزها می‌دهد و در عوض هیچ چیزی دریافت نمی‌کند.
🔹
دیگر پلتفرم‌های عبری: به نظر می‌رسد این توافق شامل خروج از لبنان باشد.
🔹
خبرنگار رؤی کایس: چه کسی باور می‌کرد که یک حمله واحد در ضاحیه جنوبی بیروت، صلح جهانی را تسریع کند؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/659579" target="_blank">📅 02:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659576">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUrD1T8aKGE40ZugGdcHpj_UMDGPdUYJCA_gPOAaTFB6Jpukf4y_0_p65g_3jac5NBuBxwr_GKjS5tIe9y85n3dbPPDkEBJ-6GRNJX5xF5dGDQb4USg32O3GwjWbb6yD8Ps8H8wSlwh-dvh34vFM2WnVEmpaA9RmZsZhde1ixyls5RWSXXY3aI-Kbb845AMeLgizRuMETCu2_2-rSr67iGSzmpdGQm6ZyqJty25-r9eNgqFJ8nVK6LsK_b4-MUx_vFNq3XKWtRRoJ-diq9jMpKsWuRaWI66kUZk7Zp2hcA7CjEi7hFpj6PqJqn0-10fgpZ_tR52djBWL_E9M_NmxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ei2-ivQJ95DBbcOfIG54vaIqpNg1uzjiN6FONbZakLqf1PVgrMV2g2W-DmTKJ6zL9HwZmcWlStj2cYGVpTGF5wuYcwFILeHTep4Tg-nxDCw2cm0TZhGrelSxCIRvds6fDwJ82W1NB6TTdivlVwXh4hWDjj5Gw5_D7b2pes78Q9j519XI4phESx_YtXB3qIg3eD9FCGT_C36veTwVlvRUmyLOBRukSFbNJwmoFrto9Q5HXuJ7DQGTGOBUjWXMvg9V-Zr7DD3Q6J5MY73eDM0Qhi54JBvjugRiLN4KXoMm4-w9fZzQknWk8ucq5bgaUXL-tQhFvy9fHg9qQXKLwlFmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMylVMOumttWYj8Zg48hp5Ql0XBdzhYv0yi4bT9Du3YZfIKWVElDVEgtID2zsK7Rx-o8m4TA8TYrEbniPdhsE8tVpsQ1abJxqtfFjEb_Q-_58jUjNBxIRlrh0778giCoVpD91o_SnKpHiWCORfuh-jVOn6Ij6A3KHWW7A5GF6MXPUPbGMsf3aIgewAZjKB0MwBfnSDaukon002VJdG_Ks5BVTTEBNgmWKK6-gIxZCgEZBq52CHproVd7mB5x8Nj9wEtiWF6mkg99kyXDD2M819BvJSDfFJO206mI7diRfXu36hvDBoOMy0pZwJ4IzF-v6HKmUeZTOjdghijaaE1ArQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش بورس‌های آمریکا، اروپا و آسیا به اخبار توافق/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/659576" target="_blank">📅 02:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659575">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای
جی‌دی ونس، معاون ترامپ: پس از حمله اسرائیلی‌ها به بیروت، ما شواهد زیادی دیدیم که ایرانی‌ها قصد دارند تعداد زیادی موشک به سمت اسرائیلی‌ها پرتاب کنند
🔹
واشنگتن پس از حمله اسرائیل به بیروت نگران پاسخ گسترده ایران بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/659575" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659574">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جزئیاتی از یادداشت تفاهم ایران و آمریکا
🔹
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
🔹
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
🔹
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
🔹
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
🔹
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
🔹
براساس جزئیات این تفاهم‌نامه، ایران تنگه هرمز را مدیریت خواهد کرد و عوارض را در تاریخ بعدی دریافت خواهد کرد./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/659574" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659573">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
یک منبع آگاه: بازگشایی تنگه هرمز، پس از روز جمعه و امضای تفاهم آغاز خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/659573" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659572">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
یک منبع آگاه: بازگشایی تنگه هرمز، پس از روز جمعه و امضای تفاهم آغاز خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/659572" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659571">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPxAWUJnPY6fy8_RaE3BcbaNqRiMdvJWpHxHN18UO01JxyRCmwvQmG-_gbMWk0nYoreAJa6H486eWYordAHEGhfOHUuhx4uZUOn6rUz8NvB6pje9DUR0KhmhA9WuEN1naIKnsXGAZaKWaWqqdC3SYaRHyAzWkPlI3b3QRVOrmTgkhFEBIASaBd5JCD5uSrF7oWDTy3cnoc1Nt0t9fxfF9RVLo5_aMk2urJ86Hon2xOtM9RFadVUA-pyRUVQ7hZyGWA0y_lVFQ-OPx-hZB-Iqhzit89DyIAN21tuhN36TBP9XO1Cz7EVyULpZb2JNoYOFoCSlZSHN74UL4B42T8Q2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والله که از خون رهبرمان نمی‌گذریم
🚩
‏⁦
#WillPayThePrice
⁩
‏⁧
#تقاص_خواهید_داد
⁩
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/659571" target="_blank">📅 02:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659570">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2jA8OmYO3Mwl3foFylbCiYNgo-rV5yp9PONilunfiLKdMUK2e56a9AeFKAbS8pkLJgdu2-LAzhnp04ZUG_2ZBfZC8y4oWXocND7RSPqk2JzMfhMlH2qp2ieUfXQlB5ihykLMiI4Hf0dhrrowlvC8C7QDjFPB8qWb0SMQqZNkNrqc4p1GWT--43QDOo6cR0dvD6KO35UbIiCgA4OXvgVgV1qGK4l2eC6Svp75wkWYr4_IC8psEUvFBSfndAYRYrnz8ZnDs5Vcty0D4_GGRcrXHnoRtm0ftZPC5u7fXDpmyYWMSpemWFC8zzODo59G0VyQa_hfmyxiPB6LdTn9Nz-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
🔹
رؤسای جمهور بسیاری تلاش کردند با ایران به صلح دست یابند، اما همگی پیش از من شکست خوردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/659570" target="_blank">📅 02:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659569">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای معاریو: نتانیاهو به ترامپ گفت که اسرائیل خود را ملزم به رعایت بخش مربوط به لبنان در توافق پیشنهادی آمریکا و ایران نمی‌داند
🔹
بر اساس منابع اسرائیلی، اسرائیل قصد دارد نیروهای خود را در لبنان نگه دارد، عملیات علیه حزب‌الله را ادامه دهد و در صورت نیاز به حملات پاسخ دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659569" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659568">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGpF4RZACujGsEHeSyJZVFG0YjlNIRpzlIgT3aA4gfLekE6uCNzcM-Jo9OzUEpGAQ1J8KLm0qSpumpSmid2HCqPWxRRJvj1KF3Oeajz5yStHRu_pZIJCmKEmb2VlvmtUwJBPKHGxTQopciLAfEdljHATLHm1cSirJ3yAdyd7dfjl0LUjzog6EjXzqrcw6KMbnRhHmLdNK7GRBeuYMSPlLhXtu67aCfqqNkRmWdnuHkUqL66SGZ1BiumsZucwcVz4qNGTaMtpD-JFubqrsWxAeijkMA_pZ10MDr2wNVbgKkLd9_OWYYZAaO0SSLev4KbxsFw7xDAwFBAfqxpW_A-p3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر مرندی:
۱) حماقت نتانیاهو بن‌بستِ مذاکرات را شکست. برخلاف برخی گمانه‌زنی‌ها، تا پیش از حمله جنایتکارانه او هیچ متن نهایی‌ای وجود نداشت. این حمله بود که ترامپ را وادار کرد خواسته‌های ایران، به‌ویژه در مورد لبنان، را بپذیرد.
۲) حماقت نتانیاهو نتیجه معکوس داد. این یک عقب‌نشینی تاریخی از سوی «امپراتوری شر» است. هرگونه نقض توافق با پاسخی سخت و قاطع از سوی ایران و محور مقاومت مواجه خواهد شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/659568" target="_blank">📅 01:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659567">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-h5n6Y5tMyv657DOW2lf92nfjmsCZbmvCsep6sKyprCaJj1T27GRoYDmZPiGhrWNUN6FSLevHclTx5AmJp9WjbbYoFS3mIm_nWPZDJwDTnbeKwzEaFytXkbILHt4OIvvQsHxUjLsvPlgbxWmgfwrWhZzSWjIuelIw2DMoBNL_lUxcbEaZZ_6ji35OntMVj76lWHG690TT_1h2A1cV7Ge0Zi_3mkDoeZOuBRAHnFKn5GInbs6tH_OZ2iAFdHaF7cExIPMKvXWkFmF6yP5MilCC55tMR1tva6Hd19ZyTq4AzqWso7oY97mAJb2QWhGt1Nn0Aa671wmnbyeSmJc91V2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صعود ۱.۱۳٪ ارزش بازار کریپتو و رسیدن به عدد ۲.۲تریلیون دلار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/659567" target="_blank">📅 01:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659566">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
طبق یک بند از یادداشت تفاهم بین ایران و آمریکا، پول های بلوک شده ایران طی ۶۰ روز باید آزاد شود
/صبح نو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/659566" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
قرارگاه خاتم: مردم و نیروهای مسلح ایران ثابت کردند که دشمن راهی جز پذیرش شکست و تسلیم ندارد
🔹
مردم مقاوم و سربلند ایران و فرزندان دلاور و شجاع ملت در نیروهای مسلح مقتدر کشور و جبهه مقاومت با عنایت پروردگار متعال و تحت تابعیت فرمانده معظم کل قوا مدظله العالی با تحمیل اراده الهی و پولادین خود به دشمنان زبون آمریکایی و صهیونیستی با قدرت ثابت کردند که راهی جز پذیرش شکست و تسلیم در برابر مردم مبعوث شده و جنود پروردگار متعال ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/659565" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMLBX1nL-YZ47SxvkNnRZw_TL_HXURC3sxHzeH_HyScxsLc-qjDXKKnzsh2UmBBCD2jITl2qnbtPkX2gz6i5C-82MAkmNAFF7NMh0wXJmfjKRM3cAT_E2F0JCltn6ZtMNLmMAAi8NFQnnUYz14iKHuNL5vOwSe5bEkp74_sEJV3tCgiss04vTD5MxJT8ileIqR8Fy4xfpRs6rGfdVfQtCRecU7pIDcGkQqc_JmQodZUN_eT_5vSbTUUlMg0K9nTPCSWSk8oapX_1WiYCklAvm09xDzwfJolfs4-zirphGoQWUGHMdwIKnDkKAhnE5KV6V25gI07iRJiVVz2yWOiXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۱.۹۴٪ اونس جهانی طلا پس از خبرهای توافق ایران و آمریکا و رسیدن به عدد ۴٬۳۰۱٫۲۶ دلار/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/659564" target="_blank">📅 01:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
یک منبع آگاه: طبق یکی از بندهای یادداشت تفاهم بین ایران و آمریکا، یک برنامه ۳۰۰ میلیارد دلاری بازسازی و توسعه در ایران، تعهد آمریکا و متحدانش است
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/659563" target="_blank">📅 01:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
نخست وزیر قطر: از توافق حاصل شده بین ایران و آمریکا استقبال می‌کنیم
محمد بن عبدالرحمن:
🔹
«ما از توافق حاصل‌شده درباره یادداشت تفاهم میان ایالات متحده آمریکا و جمهوری اسلامی ایران استقبال می‌کنیم.
🔹
مراتب قدردانی خود را از برادرانمان در جمهوری اسلامی پاکستان، و نیز از تمامی طرف‌های منطقه‌ای و بین‌المللی که در فراهم‌سازی شرایط مساعد برای دستیابی به این تفاهم نقش داشتند، ابراز می‌داریم.
🔹
امیدواریم همه طرف‌ها در مذاکرات آتی با روحیه‌ای مثبت و سازنده مشارکت کنند؛ روحیه‌ای که به تحکیم این پیشرفت و بنا نهادن گام‌های بعدی بر پایه آن کمک خواهد کرد.
🔹
بار دیگر تأکید می‌کنیم که دولت قطر همچنان حامی ثابت‌قدم این تلاش‌ها و همه ابتکارهایی خواهد بود که با هدف تقویت امنیت و ثبات در سطوح منطقه‌ای و بین‌المللی، از طریق گفت‌وگو و راهکارهای مسالمت‌آمیز، دنبال می‌شوند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/659562" target="_blank">📅 01:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659561">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
شبکه خبر به نقل از منابع آگاه: ایران امتیازات بسیار مهمی برای حزب الله لبنان در آخرین ساعات تلاش‌های دیپلماتیک به دست آورد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/659561" target="_blank">📅 01:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659560">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
قیمت نفت خام برنت با ۴ درصد کاهش به ۸۳.۹۶ دلار در هر بشکه رسید
خبرگزاری رویترز:
🔹
قیمت نفت خام برنت پس از اعلام توافق بین تهران و واشنگتن با ۴ درصد کاهش به ۸۳.۹۶ دلار در هر بشکه رسید
🔹
بر اساس این گزارش قیمت نفت خام آمریکا پس از اعلام توافق بین تهران و واشنگتن به پایین‌ترین حد خود یعنی ۸۰.۲۵ دلار در هر بشکه رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/659560" target="_blank">📅 01:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659559">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
احتمال حضور همزمان ترامپ و ونس در اروپا برای امضای توافق با ایران
ادعای خبرنگار فاکس‌نیوز در کاخ سفید:
🔹
معاون رئیس‌جمهور، ونس می‌گوید که قصد دارد برای مراسم امضا در ژنو باشد، اما می‌گوید ممکن است رئیس جمهور نیز آنجا باشد. هنوز در حال بررسی تدارکات است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659559" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e8d57794.mp4?token=FkxuOnsx_yLH7dJuJaiQCWECUg_037TaC5xYQiqQG4_OI2Q4u6Wg84I56aw38zXZ_-4Pf8nK1oocmInsaLuZ-dES6LJ8TXKZJn-g8s9aoxjGML7BL6eLMeBg5W7O7INA2H723H6faroqPkfrYBoe4hHqsPlebGmeug0D1hPxcj5BMKucEwLX4PpgLa5d9xBTPl1rNBd8rubvo6SGC1T5v2MKxMeRqZ8frJLBViCD_tcpeLH1OaQ5LQeH71PjzPTanSPW7CzvZT72y6z8uz13cLPPuTDZ5YmZx4A0m-7WfksHIxeD__z--Ea9-0MGBmObmjo8G63tlQK0RMdcvXSifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e8d57794.mp4?token=FkxuOnsx_yLH7dJuJaiQCWECUg_037TaC5xYQiqQG4_OI2Q4u6Wg84I56aw38zXZ_-4Pf8nK1oocmInsaLuZ-dES6LJ8TXKZJn-g8s9aoxjGML7BL6eLMeBg5W7O7INA2H723H6faroqPkfrYBoe4hHqsPlebGmeug0D1hPxcj5BMKucEwLX4PpgLa5d9xBTPl1rNBd8rubvo6SGC1T5v2MKxMeRqZ8frJLBViCD_tcpeLH1OaQ5LQeH71PjzPTanSPW7CzvZT72y6z8uz13cLPPuTDZ5YmZx4A0m-7WfksHIxeD__z--Ea9-0MGBmObmjo8G63tlQK0RMdcvXSifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه ونس با فاکس‌نیوز پس از اعلام رسمی توافق صلح ایران و آمریکا
🔹
حالا امیدواریم دوران جدیدی با ایرانی‌ها آغاز شود! این برای مردم آمریکا اتفاق بزرگی است.
🔹
می‌دانم که آنها از قیمت بالای بنزین رنج برده‌اند. رئیس جمهور قطعاً نگران این واقعیت بوده است. اما کاری که ما می‌توانیم انجام دهیم این است که هزینه انرژی را نه فقط اکنون، بلکه برای درازمدت کاهش دهیم و یک موتور واقعی رفاه در خاورمیانه ایجاد کنیم که در آن آمریکایی‌ها از قیمت‌های پایین‌تر انرژی و قیمت‌های پایین‌تر بنزین بهره‌مند شوند و ما همان خطر هرج و مرجی را که در نسل گذشته داشته‌ایم، نداشته باشیم."
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/659558" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659556">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
جزئیات تازه از امتیاز لحظه آخری قالیباف از ترامپ درمورد لبنان
یک منبع آگاه:
🔹
اضافه شدن احترام به حاکمیت و به رسمیت شناختن تمامیت ارضی لبنان، یکی از تغییرات مهم در متن است که براساس آن مناطقی که رژیم تصرف کرده به عنوان مناطق اشغالی شناسایی می شود و باید عقب نشینی کند./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/659556" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اقای ما امام وعده های صادق بود....
ترامپ امشب اعلام کرد قصد تغییر نظام را ندارد.. که البته قصدش را داشت... حمله نظامی کرد.. ناتو با او بود .. اعراب با او بودند.. اسراییل با او بود... تجهیزات و پول با او بود... اما به هدفش نرسید.. او که میگفت کمک برای براندازی در راه است امروز منکر قصد براندازی شده....
او به هدفش نرسید همانطور که ریگان.. همانطور که صدام و همانطور که تمام دشمنان جمهوری اسلامی ایران...
اقای شهید ما قبل شهادت این وعده را به ما داده بود آنجا که فرمود:
آنها و ده‌ها متوهم دیگر به درک واصل شدند و رژیم اسلامی روزبه‌روز رشد پیدا کرد. من به شما عرض می‌کنم این تجربه این بار هم به فضل الهی تکرار خواهد شد....
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/659555" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: آمریکا را در جنگ نظامی مغلوب کردیم و آنها در این تفاهم‌نامه تعهد به پایان جنگ دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/659553" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مذاکرات ۶۰ روزه پس از راستی آزمایی اجرای تعهدات آمریکایی آغاز می‌شود  غریب‌آبادی، معاون وزیر خارجه:
🔹
روز جمعه یک امضای رسمی خواهیم داشت و گفتگوهایی روسای دو هیئت برای تعیین ترتیبات آتی مذاکرات خواهند داشت.
🔹
تا آن موقع موضوع تعهدات طرف آمریکایی درباره خاتمه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/659552" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ونس معاون ترامپ: من برای شرکت در امضای توافق با ایران به ژنو خواهم رفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/659551" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
مذاکرات ۶۰ روزه پس از راستی آزمایی اجرای تعهدات آمریکایی آغاز می‌شود
غریب‌آبادی، معاون وزیر خارجه:
🔹
روز جمعه یک امضای رسمی خواهیم داشت و گفتگوهایی روسای دو هیئت برای تعیین ترتیبات آتی مذاکرات خواهند داشت.
🔹
تا آن موقع موضوع تعهدات طرف آمریکایی درباره خاتمه جنگ و رفع محاصره و آزادسازی اموال، راستی آزمایی خواهد شد.
🔹
ورود به مذاکرات ۶۰ روزه منوط به اجرای این تعهدات آمریکاست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/659550" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: میانجی‌ها در مذاکرات آتی همچنان حضور خواهند یافت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/659549" target="_blank">📅 01:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نیروهای مسلح ایران دستشان همواره روی ماشه خواهد بود
غریب‌آبادی، معاون وزیر خارجه:
🔹
نیروهای مسلح ایران همواره دستشان روی ماشه خواهد بود برای مقابله با توطئه‌های دشمنان. همواره برای مقابله با هر توطئه‌ای آماده خواهیم بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/659548" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
مذاکرات تا یک ساعت قبل ادامه داشت
غریب‌آبادی، معاون وزیر خارجه:
🔹
تا زمانی که آخرین نکات و مطالبات خود را وارد متن تفاهم نکردیم، با تفاهم نامه موافقت نکردیم. مذاکرات تا یک ساعت قبل ادامه داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/659547" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
غریب‌آبادی: تعهدات ایران نسبت به دستاوردهایمان قابل قیاس نیست
غریب‌آبادی، معاون وزیر خارجه:
🔹
به زودی متن تفاهم نامه منتشر می‌شود و مردم می‌توانند دستاوردها و تعهدات ایران را ببینید. تعهدات ما نسبت به دستاوردهایمان قابل قیاس نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/659546" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تهدیدات امشب ایران در پیشبرد برخی موضوعات در متن مذاکره موثر بود
غریب‌آبادی، معاون وزیر خارجه:
🔹
برخی اصلاحات مدنظر در تفاهم را با اتفاقاتی که در لبنان افتاد و با بیانیه‌های نیروهای مسلح، پیشبرد کار مذاکراتی را تسهیل کرد. نیروهای مسلح آماده پاسخ قاطع بودند.
🔹
ترامپ هم مواضعی اتخاذ کرد و نسبت به رژیم صهیونیستی انتقاد کرد. و حزب‌الله نیز پاسخهای محکم و قاطعی به اقدام تروریستی رژیم صهیونیستی داد.
🔹
اقتدار نظامی و تهدیداتی که صورت گرفت کمک کرد به فرآیند نهایی کردن متن و پیشبرد برخی موضوعات که برای نهایی کردن متن داشتیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/659545" target="_blank">📅 01:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659543">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه:  دشمنی که حمله کرده بود تا اهداف شومش را عملیاتی کند، در تمامی اهدافش متحمل شکست شد و جمهوری اسلامی ایران پیروزی‌های بزرگی در جنگ کسب کرد
🔹
در پیش نویس تفاهم، تمامی مواضع مهم خود را گنجانده‌ایم.
🔹
پس از امضای رسمی، متن تفاهم‌نامه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659543" target="_blank">📅 01:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659542">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه:  دشمنی که حمله کرده بود تا اهداف شومش را عملیاتی کند، در تمامی اهدافش متحمل شکست شد و جمهوری اسلامی ایران پیروزی‌های بزرگی در جنگ کسب کرد
🔹
در پیش نویس تفاهم، تمامی مواضع مهم خود را گنجانده‌ایم.
🔹
پس از امضای رسمی، متن تفاهم‌نامه منتشر خواهد شد. قبل از امضا نیز از طریق رسانه‌های عمومی، ابعاد مختلف یادداشت تفاهم را تشریح خواهیم کرد و دستاوردها را خواهیم گفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659542" target="_blank">📅 01:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659541">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: پایان فوری و دائمی جنگ و عملیات‌های نظامی در جبهه‌های مختلف و از جمله لبنان، از همین امشب اعلام می‌شود
🔹
از امشب خاتمه محاصره دریایی آمریکا علیه ایران آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659541" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxewwoL5pNzMv5fQETzWe5Pv63asYcxRs5c14xSyChrt1eoSOm-xrJQuYnMdg6AMbwmL_WzM4xG7Rx7JtGLzQlFhmjyFyBXOMuJBp-5nZBWbFMrm8MWfV_2T9p4KF4uEDy_JMEZVvucoBCzCvLa69IN_cPucxpKmiV46UBja0zNu_iKi6wz57ZVEtE7-Cb1jiuGX3G_UVuUwh5qnhcWFCLBmC7bVp0MPz1zKPK0biizpZ-9JHJvdGs_Af7vbFjG5GzH4DmfAWhOiEopBVXHqDThdHLrKSTVD1t-WpxGMF7TsxwqJCNh49FdD7P2PrkXGffAjN4Fm1oA1sVPbGOh9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط نفت به ۸۷ دلار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659539" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: پایان فوری و دائمی جنگ و عملیات‌های نظامی در جبهه‌های مختلف و از جمله لبنان، از همین امشب اعلام می‌شود
🔹
از امشب خاتمه محاصره دریایی آمریکا علیه ایران آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/659538" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: متن یادداشت تفاهم نهایی شده و امضای رسمی یادداشت تفاهم اسلام آباد روز جمعه در سوئیس انجام خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/659537" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb2c4f204e.mp4?token=nmweDIVKk01Q80UWqXUWVbAUUTUZk2Kj_EQ9EjPqK_rqH2y6bqEnSbW-O3USTO63IVR8BvdmP9z89I-M0zAjmt0imDjfRjsDjSB67XQDsqZjNWTf6eEr3k35-GNQ1iAsWgb2TkMjxJ1DgQ3kx_Z0pHKvjPqXY_Bw7AL1ZIs4vnZyag8ckCXu1vt2Bb7kQL_6cWDTagmCL1c7GN_LpvYbOsMxXXicplFXENV0kqylYcfJaob6M92i56GTstop84jimmvzT6EBL9NloC_2yKcYqZXNWaw6PKFN9lRptEsiX-DFnloQEfkQ6VTOZmlz7yS3L8IJ2nHVWNRLLMQSrz5ksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb2c4f204e.mp4?token=nmweDIVKk01Q80UWqXUWVbAUUTUZk2Kj_EQ9EjPqK_rqH2y6bqEnSbW-O3USTO63IVR8BvdmP9z89I-M0zAjmt0imDjfRjsDjSB67XQDsqZjNWTf6eEr3k35-GNQ1iAsWgb2TkMjxJ1DgQ3kx_Z0pHKvjPqXY_Bw7AL1ZIs4vnZyag8ckCXu1vt2Bb7kQL_6cWDTagmCL1c7GN_LpvYbOsMxXXicplFXENV0kqylYcfJaob6M92i56GTstop84jimmvzT6EBL9NloC_2yKcYqZXNWaw6PKFN9lRptEsiX-DFnloQEfkQ6VTOZmlz7yS3L8IJ2nHVWNRLLMQSrz5ksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم ژاپن به هلند توسط کامادا ۸۹
⬛️
🇯🇵
2️⃣
🏆
2️⃣
🇳🇱
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/659536" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دقایقی دیگر بیانیه رسمی دبیرخانه شورای عالی امنیت ملی درباره توافق آتش بس منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/659535" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b85cc77a.mp4?token=WzXPYdHsTLvjfZZlBS5EHn_Y4du0_OljJXDqrYTxzXPV5VkUZYgDBohxqoZSsXRzqxIjgWIf2TezRpOvB0BQCk7PC1VRy5Ag0djYxyqBBwSOgPakuzTU1G8spa9EtcqfWE0aAknqMUeaTwtEuDZmw3N2rxvR6utgim9fZv7hI4mALoghI6VaVX-gEqhlAYzcEWqmhb5qaNvIpsFoZ7gSHP57tuH4SFfykJC_GBIgC3elRABZ0vi5p5MHtuCE33otzWBv5kfb1DtBpnBJPrsUBsG71Q9lRRFX3o75v0sIlK8SOoR_DIED5Nc2Q57VU7WYASY4sEGZ58QD_9pHZF6cAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b85cc77a.mp4?token=WzXPYdHsTLvjfZZlBS5EHn_Y4du0_OljJXDqrYTxzXPV5VkUZYgDBohxqoZSsXRzqxIjgWIf2TezRpOvB0BQCk7PC1VRy5Ag0djYxyqBBwSOgPakuzTU1G8spa9EtcqfWE0aAknqMUeaTwtEuDZmw3N2rxvR6utgim9fZv7hI4mALoghI6VaVX-gEqhlAYzcEWqmhb5qaNvIpsFoZ7gSHP57tuH4SFfykJC_GBIgC3elRABZ0vi5p5MHtuCE33otzWBv5kfb1DtBpnBJPrsUBsG71Q9lRRFX3o75v0sIlK8SOoR_DIED5Nc2Q57VU7WYASY4sEGZ58QD_9pHZF6cAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید به شیوه سنتی امضای توافق صلح با ایران را اعلام کرد
🔹
خبرنگاران تصاویری از دود سفید در کاخ سفید را منتشر کردند، طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659534" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
نیویورک تایمز: ایران یک حمله برنامه‌ریزی‌شده به اسرائیل را لغو کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/659533" target="_blank">📅 01:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659531">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
خواسته ایران در موضوع اداره تنگه هرمز محقق شد
🔹
با تغییرات لحظه آخری در متن تفاهنامه ایران و آمریکا، تنگه هرمز با ترتیباتی که ایران اتخاد خواهد کرد بازگشایی می شود و نحوه اداره تردد در تنگه هرمزو شیوه ارائه خدمات دریایی و دریافت هزینه های مربوط به آن به جمهوری اسلامی ایران و عمان به عنوان کشورهای ساحلی  تنگه محول شد./ صبح نو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659531" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLGH53XiMhunr3WwnLDw88A9hWOsTFNg3MXRdZT9ppMKt7PkVhvbEMx64WzE1iCt67lKWaYpIfa1QwKBNHNE3v6eR5GHOjb2_8glSCNQF10JooO0Pwb_PzNbqcnPrkxrWHIFRQH14j_040N2XPM3d_Mvn-nq9VAE-25r5dins-ZxOFoM9yNMn18_TGF1ZavZ8xmXo51unPEP7naBjsjwScDAiPULGhw_V8OTmj8_J0bJnI99MPYS6zW2oL603AD3NXgNUAnziDv-GFKzvKU8AgKO7Lv3R3iYO9nww3IZr6DScXGBTItVNpbjQA2IuTDwoqsMRDP7EFsLtRQk7iybAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستاورد فوق العاده با ارزش ترامپ:
بازگشایی تنگه ای که قبل از جنگ هرگز بسته نبود!
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659529" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/659528" target="_blank">📅 01:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ترامپ: کشتی‌های جهان می‌توانند تردد در تنگه هرمز را از سر بگیرند
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659527" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659526">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تسنیم: برخی منابع حاکیست که تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/659526" target="_blank">📅 01:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترامپ: توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
🔹
بدین‌وسیله من بازگشایی بدون عوارض تنگه هرمز را به طور کامل مجاز می‌دانم، و همزمان با این، لغو فوری محاصره دریایی ایالات متحده را دستور می‌دهم.
🔹
ای کشتی‌های جهان، موتورهایتان…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/659525" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70bce1a9.mp4?token=MBlDzQ7VnFQp7mD_E8f6emxHX15XWHePa2m87iuI6RhJm6-IEYGZ1a6g0MH0x8WYVxrFHZB6Sc3J6Ua1jzXmsPNlzuPs3ZDzXf1vXKbZbTuyZ_lcny7FcI9DbPkUKiwpYEnqe37qeSLGfCeyzOTA-_t0Ohj9fePDqU2yaSwF2VeZ_Wg3sLbZZcQuF6EJgfq4RaxaCeA9O0IjJz0OkLElG326zilMlQEmoALl5jcu6kEsYZIcQLcSZHcPPdaqY9ll0wMTgvVhb4-M_uVlMI1Rb0MdikjAQ5wcQh2uBAS7jKJ6DhIIN1a_MXfj1wraX1wHeGtRDr6Hvq5o97nA39AFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70bce1a9.mp4?token=MBlDzQ7VnFQp7mD_E8f6emxHX15XWHePa2m87iuI6RhJm6-IEYGZ1a6g0MH0x8WYVxrFHZB6Sc3J6Ua1jzXmsPNlzuPs3ZDzXf1vXKbZbTuyZ_lcny7FcI9DbPkUKiwpYEnqe37qeSLGfCeyzOTA-_t0Ohj9fePDqU2yaSwF2VeZ_Wg3sLbZZcQuF6EJgfq4RaxaCeA9O0IjJz0OkLElG326zilMlQEmoALl5jcu6kEsYZIcQLcSZHcPPdaqY9ll0wMTgvVhb4-M_uVlMI1Rb0MdikjAQ5wcQh2uBAS7jKJ6DhIIN1a_MXfj1wraX1wHeGtRDr6Hvq5o97nA39AFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام رسمی خبر توافق و توقف جنگ در شبکه خبر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/659524" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwxIB6DiBI80bFll5PI_tfxmzqOKn7GayTygjYgHoSMQQsKvsPyE0J7ZMRfkrWmiRjJsBcevRzS6-4itRY1Yc1jTW4xj4tXeMFsr5cEzKUkbHU3kXBQWzVo43b22IRD-3JUqbrrxGS7BCvXO11nFNFRt4DZUzZxx4Yi1yi4DJ5mm-c0OU4OfD2wbNg7fKMMsHg6K1PaiiTFJ662A67oK8fcyh9dfsra_Ssi7oznYlIeRZUB_Rybi9GyQRjaH5ipBQU4mlAWM_5vjBDT0Mhnx_3B2v9rtGkm68nCZx3SBNuune7HmCbtazVdIRKOccJUg2mqXaeh768LogXI71g1KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلاکارد هم می‌خوای بگیری دستت، اینجوری باشه
🫠
‎
#WillPayThePrice
‎
#تقاص_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/659523" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ترامپ: توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
🔹
بدین‌وسیله من بازگشایی بدون عوارض تنگه هرمز را به طور کامل مجاز می‌دانم، و همزمان با این، لغو فوری محاصره دریایی ایالات متحده را دستور می‌دهم.
🔹
ای کشتی‌های جهان، موتورهایتان را روشن کنید. بگذارید نفت جاری شود! رئیس‌جمهور، دونالد جی. ترامپ
📲
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659522" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxOMNisEdlxcm30Ells0_BqZXokiF1Bim46bM_GNSwuhWC5YHTCZbYlzpwtVBmd1Q99M0Q19_qBGPFVdSQF1fU8ONfCahG-hOmsUFnqyvvZ0oo14L5YbN-HwYLNJKFuzzbFWmezITxpCtPvSDas7GxNDTjuRqx7EUG7EC5KUz9djwG7wJ29xWSncyuTC6IGy8yoiB8gZTDqCy4bvakxN77rSZzTRu7FJmSYdxs2N8yl-t01Qk8XZvsv-Au92qHw3Mid7f72qsX81-u0eOJCTh1Dgha_4j1l_x6vd2sU1lOTQ26matAagZeiktHaxPYCkhtF5dq1jpFig2Z6rQj6YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: توافق با جمهوری اسلامی ایران به طور کامل نهایی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/659521" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0372d04149.mp4?token=px9rCPVd-nqDIMNlqlzSB1vU9lQ3K4sCiOil_xpEiHoKOozzd1uGOX9Guufer5wuZ7bdQNztO1XjC25kJ3CpwBQFsitjQe2sdkzX944X56KJ4SSeRHURuQt53FAwAQYV63ccxapxuLdojya5SxufiIUzo0rrObI8Ijbbewg5aAHxofq6I8mqyuxQRMT3MvJn39-XAtyhJjZFUlWn_ybPb4Qhpq_LoUXBI0DiDw25lty4HcJsBrxyM6UgNkwViw2lJBv2oBBex-3ZhYn-xPXF6v__waIuaI6w4ePbctMFMVNaVR21ep9oUJf4dI5O9WfnCx_t0Tp4fQQMYcbo9cIadA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0372d04149.mp4?token=px9rCPVd-nqDIMNlqlzSB1vU9lQ3K4sCiOil_xpEiHoKOozzd1uGOX9Guufer5wuZ7bdQNztO1XjC25kJ3CpwBQFsitjQe2sdkzX944X56KJ4SSeRHURuQt53FAwAQYV63ccxapxuLdojya5SxufiIUzo0rrObI8Ijbbewg5aAHxofq6I8mqyuxQRMT3MvJn39-XAtyhJjZFUlWn_ybPb4Qhpq_LoUXBI0DiDw25lty4HcJsBrxyM6UgNkwViw2lJBv2oBBex-3ZhYn-xPXF6v__waIuaI6w4ePbctMFMVNaVR21ep9oUJf4dI5O9WfnCx_t0Tp4fQQMYcbo9cIadA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم هلند به ژاپن توسط سامرویل ۶۴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659520" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2fecc6be.mp4?token=csPY9NGgvGhMIC8gu5hXcboKmmQsjP6ODo16wtVcQjDIOzSCH0gJYATdmc3bn9dtWaeP6sId4eX34NueRNzQHMt9JzN7oRAJPJJaysNX2prKmz0ZlKgPjWIIMYJxwp5LI6lBXcxG1_AL6zVBsNXUs_hZwY8srvvF8zpX_LarqAw1lJkRV8v7N-CEOp8ZWJn674WDa2i3uQ_YOVU9uo-3e4FKwgU9Kt0F_Pm_MdrpeY_n2fXYGftcXDLs1H41ZX3jr2It1WtD5E8NJerA7L0JVgC5AiJGJCXrB2KQcbT21qeR0X64h6siFchJO6X_709kSdAVA5yuk0gkcDNddrZENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2fecc6be.mp4?token=csPY9NGgvGhMIC8gu5hXcboKmmQsjP6ODo16wtVcQjDIOzSCH0gJYATdmc3bn9dtWaeP6sId4eX34NueRNzQHMt9JzN7oRAJPJJaysNX2prKmz0ZlKgPjWIIMYJxwp5LI6lBXcxG1_AL6zVBsNXUs_hZwY8srvvF8zpX_LarqAw1lJkRV8v7N-CEOp8ZWJn674WDa2i3uQ_YOVU9uo-3e4FKwgU9Kt0F_Pm_MdrpeY_n2fXYGftcXDLs1H41ZX3jr2It1WtD5E8NJerA7L0JVgC5AiJGJCXrB2KQcbT21qeR0X64h6siFchJO6X_709kSdAVA5yuk0gkcDNddrZENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین واکنش مجری شبکه خبر به امضای توافق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659519" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659518">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#خبرفوری
عقب نشینی دقیقه آخری ترامپ
🔹
در پی ایستادگی هیئت مذاکره کننده ایرانی بر خطوط قرمز، آمریکا در لحظات پایانی عقب نشینی کرد و قرار است رئیس جمهور آمریکا اعلام کند که محاصره دریایی علیه ایران که براساس متن در طول ۳۰ روز برداشته می شود، به یکباره و به طور کامل رفع خواهد شد/خبرفوری
📲
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/659518" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
صداوسیما: آمریکا بند پایان دادن به جنگ در تمام جبهه‌ها حتی در لبنان را قبول کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659517" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
قیمت تتر به ۱۶۵هزار تومان رسید
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/659516" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozljToNtnMgT31Pyxl59zbp9MVssEaStkBHmm9ivPWw6Q5Ete4yknLkyD_-tMg5oJhOe-4fd0j6DrxsaiP7dMR7H69n5dYRjDGMDElCx7ELQr7hvRVIUX0SV896yCsKVIq-f-hM5QiMWTV8zAN9ChMsBothIBeFwO-WLnQiGz3IpGAcypgFuGLNyHlTICKhsCyaIXgiy9a8EWcTQN9Spz0iHmumoEH5_Brp6a3hLEP4OisdYIkGAd59vJ1MNZhZS2eb030Ma659C9Cw_yDOSJ_Bj4j6RSMiRF91hfSVbiP0mF39ll0wTBJsNRM9Zmpd7KwcdJdtoenfwexTvuhkEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیرنویس شبکه خبر: نخست وزیر پاکستان از دستیابی به توافق پایان جنگ آمریکا علیه ایران خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/659515" target="_blank">📅 00:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659513">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad78c1119.mp4?token=RPlJw11xJT2VNgRiQ8dxn33JVirnRsvp3Hi98hN3pgnENkJ3EqFIXhMlirrAjqVfjfU3Wwex0Jeh9MXPrxuW-ZpZCTQUTBsA0QWnAi4V2Y6twG5cdrk01H_ww3B6Jvc9KNgLKOMPt7fweL185QgyduouSIjjZsftwTmuihbaQtKBIOIjh3YxwPd_Pn73Zp4DFbNv_dDpZJHkgSrcZ0erzNt6k8hrepBfXpaRZIuC5emhhu12ZKFPvISTEMi2C9FOGg9UriJgiwe0vXYAi5nq-pxCFI2KwvJYuzEqibTvgMOSjq_PRHfA6sQtFmoZL7UMgFw46h3vqPn_4ENHPH4M1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad78c1119.mp4?token=RPlJw11xJT2VNgRiQ8dxn33JVirnRsvp3Hi98hN3pgnENkJ3EqFIXhMlirrAjqVfjfU3Wwex0Jeh9MXPrxuW-ZpZCTQUTBsA0QWnAi4V2Y6twG5cdrk01H_ww3B6Jvc9KNgLKOMPt7fweL185QgyduouSIjjZsftwTmuihbaQtKBIOIjh3YxwPd_Pn73Zp4DFbNv_dDpZJHkgSrcZ0erzNt6k8hrepBfXpaRZIuC5emhhu12ZKFPvISTEMi2C9FOGg9UriJgiwe0vXYAi5nq-pxCFI2KwvJYuzEqibTvgMOSjq_PRHfA6sQtFmoZL7UMgFw46h3vqPn_4ENHPH4M1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل مساوی ژاپن در دقیقه ۵۷
هلند ۱ ــ ۱ ژاپن
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659513" target="_blank">📅 00:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659511">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نخست وزیر پاکستان از دستیابی به توافق با واشنگتن و تهران خبر داد
🔹
پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/659511" target="_blank">📅 00:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659510">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZfK2Y5qGzmkZX3AcononxShaITCdf6bCGxdm_2VzRGQ8dnp3oYE-5GL6JTvz_-u09iEplX7eZelpKUkQ3hQT7LCK56EoJs4KWtDsIswJCDtY6zyGMDdgaohL19re3gWfGUrB4tee9rCje40wC3SvmJGtaJRjOlLt1F7V1uiT4OAwptbnLsofUUWghaTKj2azlzblLuU01mLHrjDPNsFaqez6l0aTQOnpeLve-fObuzSPl5_iWJu-gEhFmwLBgfQmBxJLZVdfsj9ivE9abLsJHA2zmKXrN73XbTCh-0XlCrvjd57Wiwj8nVlFn8GuP5e05_EhMzBvGKnWyYKpQX_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر پاکستان از دستیابی به توافق با واشنگتن و تهران خبر داد
🔹
پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
🔹
ما مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حل دیپلماتیک برای این درگیری تشکر کنیم. همچنین مایلیم از برادرانمان در این تلاش میانجیگری، رهبری بزرگ کشور قطر، به خاطر حمایتشان در دستیابی به این توافق‌نامه، صمیمانه قدردانی کنیم. همچنین به ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه به خاطر کمک‌های عظیمشان در این زمینه تشکر می‌کنم.
🔹
با حصول توافق‌نامه، میانجی‌ها این هفته مجموعه‌ای از جلسات را تسهیل خواهند کرد. این بحث‌های پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم رسمی امضای توافق‌نامه را بنا خواهد نهاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659510" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: این توافق به صورت الکترونیکی، یا توسط من یا معاون رئیس جمهور ونس، امضا خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/659509" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ در گفتگو با وال استریت ژورنال: ایران هنوز تأیید نکرده است که با این توافق موافقت کرده باشد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/659508" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659507">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#خبرفوری
🔹
یک منبع آگاه به خبرفوری گفت: پس از حمله رژیم صهیونی به ضاحیه با تصمیم رئیس هئیت مذاکره کننده ایران، اعضای تیم مذاکراتی مذاکره با طرف قطری را متوقف کردند.
🔹
همزمان نیروهای مسلح آماده برای حمله به رژیم شدند. با توئیت قالیباف در واکنش به حمله رژیم به ضاحیه، ترامپ مجبور به ارائه امتیازات جدید و جدی به ایران در موضوع لبنان شد.
طرف آمریکایی و رژیم، تهدید ایران را همچنان معتبر می دانند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659507" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با وال استریت ژورنال: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/659506" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659505">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844b0be1f8.mp4?token=JNnxoWiN0DtD45B3VvGyhJEk6B8cKLgsQrtjIcr4tK3xy8UXQYgaUMbs1_zoKvyRAny8MLgyySa9sdEf_rj5FDTet-ZhjHcqUWhezPRF_q413hV4jRC8rLKM5lBDlQrx2l9mvz3zHPLGb1BbmQ8LWRiGY6tl3-G7ePjKcovJtuZK13LZl_mSCJWxrCeknjLu1qu48yYLOrj6nrTRgK6a69TUqkAdapQ5P9aX2_Ej2t3PnYH61Y7ciOwr4GzSAxWMxgbNnQQR6MpG_o6jqj-Q10q2Qip88xsox-ZV2L_JKkgK4FtQJ47pivJ31inegS4WTe80cwl-RFFk0CWypu4cZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844b0be1f8.mp4?token=JNnxoWiN0DtD45B3VvGyhJEk6B8cKLgsQrtjIcr4tK3xy8UXQYgaUMbs1_zoKvyRAny8MLgyySa9sdEf_rj5FDTet-ZhjHcqUWhezPRF_q413hV4jRC8rLKM5lBDlQrx2l9mvz3zHPLGb1BbmQ8LWRiGY6tl3-G7ePjKcovJtuZK13LZl_mSCJWxrCeknjLu1qu48yYLOrj6nrTRgK6a69TUqkAdapQ5P9aX2_Ej2t3PnYH61Y7ciOwr4GzSAxWMxgbNnQQR6MpG_o6jqj-Q10q2Qip88xsox-ZV2L_JKkgK4FtQJ47pivJ31inegS4WTe80cwl-RFFk0CWypu4cZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به ژاپن توسط فن دایک
۵
۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659505" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659504">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
فوری/ ترامپ به وال استریت ژورنال: به زودی بیانیه‌ای صادر خواهم کرد که تایید توافق با ایران توسط ایالات متحده را تایید می‌کند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659504" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659503">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
فوری/ ترامپ به وال استریت ژورنال: به زودی بیانیه‌ای صادر خواهم کرد که تایید توافق با ایران توسط ایالات متحده را تایید می‌کند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659503" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659502">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdr2Sdp_-qSj6NifE776baQLHCj9tic0jd4OJNVFQb0wJzrDdRX3XAKwPtuvzKy3xLYE5g0WfPD8gsUUM-vaPdleY7kUFS-mmkFFRRzmk2UttodzezbInsa5MXfaLuCCKt2pszxQQSxM7pC196BCvcO_6Nd-XzvAdCF66A-99G7WPpRurUKltxL8bl_wnvAFaM6j_j8hCpYrQ8s1NLC9MxmmK69yPkdg6etj8kZtIcXs5KxcUloWHi-MQgSeGpaiZmi7frkh2lzv5V8dq7qXiP8Q_GmcPwak1dNdyXkILQ_xoCCte1xGsvMInHQGd5Jvz3XN_BCDEC4OI8beLDns3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت وزیر کشور پاکستان: الله اکبر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/659502" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659501">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
فارس:
تفاهم در «یکشنبهٔ موعود ترامپ» امضا نشد!
🔹
ادعای رئیس‌جمهور آمریکا مبنی بر نهایی‌شدن یادداشت تفاهم در روز یکشنبه، با گذشت این روز و عدم تحقق هرگونه توافق، عملاً خنثی شد.
🔹
ترامپ طی روزهای اخیر بارها بر تاریخ یکشنبه به‌عنوان روز امضای تفاهم تأکید کرده بود.
🔹
با این حال، مقامات جمهوری اسلامی ایران پیش‌تر به‌صراحت اعلام کرده بودند که تفاهم نهایی حاصل نشده است. حتی در فرض نهایی‌شدن، تأکید داشتند که الزامی برای تطابق با تاریخ اعلامی از سوی ترامپ وجود ندارد و این تاریخ نمی‌تواند به‌صورت‌ دیکته‌شده از سوی طرف مقابل تعیین شود.
🔹
اکنون و با پایان‌یافتن روز یکشنبه بدون وقوع رویداد خاصی، مشخص شد که این ادعا نیز مانند بسیاری از اظهارات پیشین ترامپ، فاقد وجاهت واقعی و در چارچوب عملیات روانی و جعل خبر طراحی شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/659501" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ebc4a08.mp4?token=LFInO3xk5p5B4Si3tHpCcBejRXcOxaNdE597icCeDOktZnnjPGXATtP0pUHPraHWTQmUFFEq3ug2sKv3TOwcqgidnKB2qt-hS3PBAjjwYnmH57Uz8JlaWituP25TOOsMcBtypDmKo2_Rk_UmxHOOffcNZvAEfwdQINDNgEPS_ey4pkiq0gEUBHRHPpfftE5RG5KpuXdU84q70rjivIR6WJU11q8xELzIamLBPiShNqHPCx3j0QQ50r0AvEWXbBRMEte-mN141q2_oPniY8x1s_Bw6R0ZhO9lxUnoI9qsDPqystJ1Z9NscCB7ahH9MHC4ZoISl1G3_oiCEpDqTjygmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ebc4a08.mp4?token=LFInO3xk5p5B4Si3tHpCcBejRXcOxaNdE597icCeDOktZnnjPGXATtP0pUHPraHWTQmUFFEq3ug2sKv3TOwcqgidnKB2qt-hS3PBAjjwYnmH57Uz8JlaWituP25TOOsMcBtypDmKo2_Rk_UmxHOOffcNZvAEfwdQINDNgEPS_ey4pkiq0gEUBHRHPpfftE5RG5KpuXdU84q70rjivIR6WJU11q8xELzIamLBPiShNqHPCx3j0QQ50r0AvEWXbBRMEte-mN141q2_oPniY8x1s_Bw6R0ZhO9lxUnoI9qsDPqystJ1Z9NscCB7ahH9MHC4ZoISl1G3_oiCEpDqTjygmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت : امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659499" target="_blank">📅 00:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اراجیف تکراری ترامپ علیه ایران
🔹
ترامپ، در حالی که برنامه هسته‌ای ایران دارای ماهیت صلح‌آمیز است، ادعا کرد: «ایران هرگز صاحب سلاح هسته‌ای نخواهد شد.»
🔹
با تکرار ادعاهای خود درباره تنگه هرمز، وعده داد که این آبراه حیاتی به‌زودی به روی تجارت جهانی باز خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/659498" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
منابع عبری: تماس تلفنی وزیر جنگ آمریکا و همتای اسرائیلی
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659497" target="_blank">📅 00:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: اگر ضاحیه را امروز رها کنیم، مقصد موشک‌های بعدی اسرائیل تهران خواهد بود/ به زودی اسرائیل را با یک حمله بزرگ تنبیه می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/659496" target="_blank">📅 00:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شبکه ۱۲ عبری به نقل از یک مقام مسئول: نتانیاهو و ترامپ لحظاتی پیش با یکدیگر گفتگو کردند و ترامپ نتانیاهو را در جریان پیشرفت‌های حاصل‌شده برای امضای یک توافق قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/659495" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_4AjcYGz4GTQe45U30G-L6V_V22yNLsaBlrXsYNq3TQVmF3TQ4QRiQ9TRqjtmYRD1UlsZIIRxjCUvHz84Iglf6rRCSbHI6Haz2fazz35IGunjmUToqTnsCtizCk0CsQIa-pX0FRsNR4MnzBTkwSbWG5nayDvcq48m7zzx5ksSTv1Sy7lhgMjPfxbB6e-vmS9y-wpgx_KfDI5TPqUbK-gYfxGJV7SCHjMOwEx2gln2EFc6SevWKQoZpfq5HwAzT-eL51OWWvDNZNZwgYG8ECqn653TN1-frsuEY1pWb8YXK9youRY1veM-ysuqD9vRD8-iJdc7E2au0oTQ2IS0DyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دولت خود را موظف می‌داند از نیروهایی که برای دفاع از کشور و امنیت مردم در میدان حضور دارند، حمایت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/659494" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
