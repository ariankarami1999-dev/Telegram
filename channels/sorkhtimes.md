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
<img src="https://cdn4.telesco.pe/file/Wgb402k0b2AHDzmzPSzD6ni9LB8gB416e6a12LaC6GZaHFpW0C4mNuykAPzWNbjYNwqZCnajcdIRQt9qg3wOZMgnHXkr3SfXz_eqc43GM_ESiN0CWQc2i7sbmxvgzqZlL6HJ5mB0ReymBOK9_Ef_msOVMkgNOBHrC6jHwbTbPhe8DoAl-VXnSTKDqriU0_fnluf73KWpF0WhY89o0ZqmczVfiWqNttmtay-Bn5IqzG3M27FFTdZIFOD1HiaaRHeTvgKFrhICiN3CysW5Mi1fna9AWJSyyJxgFiJkM7stTbRsnlxwOYDeIEgV4FKhXCt6WOx_rnIIkHScEf_pgOCX_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/139680" target="_blank">📅 13:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fln1z6JxDW1HkpiQKgtQTkVu-20s71er6wM4tt9RaJM5eMJolv-qr6gNBYP-gZXsm9PHKa_2qzbp49_U9UojgeNfOkLsmtbKuzFhwzSNxVioe78Y3SR3b_ezjV2KHvLlheNZSzbJ-hF9lVNhClAfjt5yMUXa3RT8TnwZYX9Z4TqtZMSVI8qEdi31mj8S9wV7rPamini5inFEwXfXrkDFt2aaU93gwJ9WPd-8m0YYz8BHg5QzNdf-QBNhzavBwiFQuaLaRd51slW9DwHCZmEfrch2wwRQakOmyTHPuROdaIiUMx5Rr6VGO-m7tYgE3maA5Zhs5Dt2h1zfJpS00eEcUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/139679" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
بهاروند: طبق مصوبه هیئت رئیسه فدراسیون فوتبال لیگ نیمه کاره قهرمان ندارد.
🚨
🚨
پرونده جام حذفی فصل قبل بسته شده و درباره برگزار شدن یا نشدن جام حذفی این فصل هم هنوز تصمیم گیری نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/139678" target="_blank">📅 12:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/139677" target="_blank">📅 10:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/139676" target="_blank">📅 10:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/139675" target="_blank">📅 08:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❤️
صبح روزی که بازی داریم و شش امتیازیه بخیر
❤️
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/139674" target="_blank">📅 08:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139673" target="_blank">📅 01:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139672" target="_blank">📅 00:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139671" target="_blank">📅 00:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139670" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139669" target="_blank">📅 00:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=HuDq1lTBKDu9_Mj2Cmiukmo6EXI5cvIlQgibaZNKHw0eVdX1qXoyn4MhtLx19RE31M307H3goTtxxZEnJVPbUCBN1OKrtFMtULhMTOH1bZhN8VlERnYf_RQLMU7aZ20bUpB8HXQbRCZwdhW5jSTIRVbSpO_fCXvuFnx52ARWQ-5mRqQE71YmueN4hJydCiomNIvY043eOJXp5xnSAFsmXGH5NRUvkVE12V2lXFlogNPf4TUowTyYzA_BiiyCLZnGqIUALwseWDEHkiGkxQQzO0AREZH2CcbY2TY6cFF2J4e3GGI-rSg5VhbaD6vLOM8UrHV_l37u523WhnFFLPPokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=HuDq1lTBKDu9_Mj2Cmiukmo6EXI5cvIlQgibaZNKHw0eVdX1qXoyn4MhtLx19RE31M307H3goTtxxZEnJVPbUCBN1OKrtFMtULhMTOH1bZhN8VlERnYf_RQLMU7aZ20bUpB8HXQbRCZwdhW5jSTIRVbSpO_fCXvuFnx52ARWQ-5mRqQE71YmueN4hJydCiomNIvY043eOJXp5xnSAFsmXGH5NRUvkVE12V2lXFlogNPf4TUowTyYzA_BiiyCLZnGqIUALwseWDEHkiGkxQQzO0AREZH2CcbY2TY6cFF2J4e3GGI-rSg5VhbaD6vLOM8UrHV_l37u523WhnFFLPPokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چشمی باید اخراج می‌شد
✔️
✔️
حسین عسگری:
خطایی از این واضح‌‌تر و محکم‌‌تر نداریم مصداق خطای شدید و اخراج است
✔️
✔️
تورج حق‌وردی:
با شدت به زانوی حریف ضربه زد مصداق خطای شدید می‌باشد و باید اخراج می‌شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139668" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ1YqMi8vE22C9Qcg4_ubUOoO3nSpy_zS3273sOd7ksLHpY3e0xQ7SUOGsuRq6zQ198pZakNiAx02SpIxjdkqppH2Sbj8ZBzcREZQ8i5FxdOAoukdC4lfHu6GwbVN-q3EjKmENeSSGGPAfuuIi13Zp2x_tMOXto_3znThkXkzG_lc2PGdZaRJ3IFrYb1VHHgpyZZ56fwLz4hlB12zyTTKvngf6OFWLlYX3IIfBJEgpp9MF-YD4pBuo_q7Ig6kjtpHI9AArOM9y70_GT0TOz32nm4M-QB4AcXDwLp9fb3z1McYeVZf6UlvdeTAoP84MUL39N3j0GB3theyAnuYvgh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه فردا ببریم با ۱۳ امتیاز میریم دوم جدول
❌
❌
فوق العاده مهمه ۳ امتیاز بازی فردا</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139667" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139666" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
تارتار: باید با خداداد عزیزی برخورد شدیدی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139665" target="_blank">📅 23:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139664" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139663" target="_blank">📅 23:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139662" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139661" target="_blank">📅 22:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139660" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139659" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🗣
محمد عمری و پیام نیازمند به ترتیب کاپیتان سوم و چهارم پرسپولیس شدن/فوتبالی
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139658" target="_blank">📅 21:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت، در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139657" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139656" target="_blank">📅 21:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139655" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIcmAHdKtoCW11DEha6InXWcFVUm2-slAl08FTgKm8WfAIE4q8s_R-Jlxrfcdd2QBCai6BpVN5hOY6569Z_YijzHqCNSg-lO2toOnwIdd5E6lMrbwtQcxqNu0wKhgQb1VU3vstXV4NX-aTzaIC2ViwDAXUgOpKdkQmz2mgxbt9QDIfnkiDEE-N0L1tdarl0HWA0L9cH3cINavm9kS5iOH0Cs7djg45YBKxYB0j_Ep0NJ5zkd43UtJiYeCeED1j2nAJ62cNTEiB33TFjcUuslFC8pSmE5IZjBxg-JGq0b8VA8f9rmaqJovIFsIMNA6-GfGO84w2zIAyoElAsheNVzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139654" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU60mDzW7E-WGUTzJ4I29uggGffMRmln9k_jeOfCvqqdev3s7lCn57jtYzwHVz9Vgcp7hwIwEkYHttWBHFfQo8_rnc3jVBRnFDHVgyxlfYhgLnC6bl_CpBXnlTh1VUpb_brcdDKkOTCaS7j9d0qyPXmvG3cmCk0oJSeH_LzeMiJZchueiPjzaCkUIc4TBdAdxd07ktdG1_elSsvGx7QHHggxbnngOMr0FouHwvBxeeJkK7ZNvQyWEqsMrfg1DOUGhpvbewvEexIZeL_lVwfA8UswDOz6B--o1U3dYp0Fhm0Kdu6mQCPGU7DMiW_sQFtT_WIPY8dGqem7qWfvpgg5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول لیگ پس از پایان بازی‌های امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139653" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
بازی کیسه هم مساوی تموم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139652" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🗣
تا دقیقه 70 کیسه و آلمینیوم صفر صفر مساوی هستند ..و بهترین نتیجه برای پرسپولیس همین مساوی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139651" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139650" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
ابوالفضل جلالی در ترکیب فیکس پرسپولیس مقابل ذوب آهن قرار گرفت و تیکدری کار را از روی نیمکت اغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139649" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkAivpxo8WMKHatPIT_SjWPPhNJqNAXLaY37DqjuGCDYQUocwZEKv964J8YWl3F9gSJ2_VMkABNn5ANi4A5AoxRRdTBsQ-hCZFuEfzzMOj_ybjb-_yrBu9nglFTElXddQTcF7RXXkzlRnV7c7sB3vLB0-fZBEz8r7dVsKaNqyxf7DiyQgVX8dlMYH8JT1UKqvIjGcwUHrafDn56Z99d59tQ-yKm6hTRHn9Dk8WAqzmnDF4MuHSP0cnXGji7MzRzvjV0tq8T4z8GhO17KdoOXXbrOaHhUFFyCmeR9TZ7RSrbq-sUTzPR11dZswWPypq9AfvjA1z7SyWlS4lnDRMNxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حلقه اتحاد بازیکنا تو تمرین امروز
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139648" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139647" target="_blank">📅 20:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139646" target="_blank">📅 20:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5P-Sw2xaGz1w56NYvH3BKqUjkZ1T-5sNLasesJzGG1Db0XVk2D1XUCBP9e3q8R3j3xEj-G91lqdOgRb8rJzv9DeiUnEjRMqneZSbZpA_eXsvvnKk-AiRnfNi63XnxcTrVbTRANhya1xSOK6V5bzBsJ9YUvknoC9xJcuOK26C5zhS3Kxryar1y6kYDasuPq3gbsMmRvTQONrt6cOjSnhQ6OyNU6IigshqZL61DpqccxPerZuQuzPjgU3f3k1WiGBHdiGaKzSfTmXmiOJiRimu-SHuN5Lb245BAcKjNVVWSMbKvcy2EPEffpZ5vms9K1dpaeT7mwEOTpGZTjDJiIqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
کلاسیک ایتالیایی در راه است!
یوونتوس و میلان؛ جایی که یک اشتباه، بهای سنگینی در تورین دارد.
⚪️
Juventus -
🔴
Milan
⏰
Tonight 22:15
🏟
Allianz Stadium
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
⚽️
یووه یا میلان؟ امشب فقط یک تیم می‌تواند سربلند از زمین بیرون بیاد.
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139645" target="_blank">📅 20:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
✔️
✔️
مهدی تارتار: کاش میتونستم ۲۲ بازیکن بزارم تو زمین اما این برام چالش شیرینیه/هم بیفوما و اوستون و هم عمری و محبی رقابت شدیدی با هم دارن/بازی با ذوب‌آهن برامون از دربی مهمتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139644" target="_blank">📅 17:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: اگه همه‌ی باشگاها اجازه بدن ما هم میزاریم بازیکنامون برن تیم ملی امید/منم دوست دارم اونا پیشرفت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139643" target="_blank">📅 17:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139642" target="_blank">📅 17:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار:
✔️
بازی بسیار مهمی با تیم با تجربه و با کیفیتی داریم. ذوب آهن کادرفنی و شجاعی دارد
🗣
تیم های ویسی فوتبال جسورانه بازی می‌کنند. با توجه به اینکه هفته قبل دو امتیاز از دست دادیم محکوم به بردن هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139641" target="_blank">📅 17:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139640" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
تارتار: ما با پرس سنگینی که انجام میدهیم طبیعی است که نیمه دوم تحلیل برویم تمام شاخص ها نشان میدهد که در این چند هفته پیشرفت کردیم
✅
✅
شده سه روز به سه روز بازی کنیم باید جام حذفی برگزار شود
✔️
✔️
بیفوما و دعوت به تیم ملی؟ او خودش هم خواست که تغییر کند…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139639" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار:
✔️
بازی بسیار مهمی با تیم با تجربه و با کیفیتی داریم. ذوب آهن کادرفنی و شجاعی دارد
🗣
تیم های ویسی فوتبال جسورانه بازی می‌کنند. با توجه به اینکه هفته قبل دو امتیاز از دست دادیم محکوم به بردن هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139638" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
عبدالله ویسی سرمربی ذوب آهن: اولین نفری که زنگ زد به تارتار و برای بازی‌های خوب پرسپولیس تبریک گفت من بودم/ پرسپولیس واقعا چشم نواز بازی می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139637" target="_blank">📅 16:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
عبدالله ویسی سرمربی ذوب آهن: اولین نفری که زنگ زد به تارتار و برای بازی‌های خوب پرسپولیس تبریک گفت من بودم/ پرسپولیس واقعا چشم نواز بازی می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139636" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🗣
🗣
🗣
عبدالله ویسی سرمربی ذوب آهن: با یک بازیکن ( امید عالیشاه ) وارد مذاکره شدیم برای یک فصل از ما 130 میلیارد خواست و من جلوی این انتقال رو گرفتم. ما تیم جوان هستیم و نمی‌توانیم چنین هزینه های بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139635" target="_blank">📅 16:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtvTCicsmm-Sg6XG7aePGWGFiUMrV2uH7TiZae19IbzZSpbmgoD-KDOnnCFjq35uMRgil3rhMUO6kkzKXrKX1p5gsL5cgvBEAtWwnuJEGKjSpKaAxgmoOEZtZL2C1qxDpcpMbz_5MaCKZKlmOE8wJKeygkV44UwYZsE-S5IVUA1xLvkvuUYhV0c6W2LFB6mnm8lS9uWvEjdAJV14bPUReujeruSLsOHBmDACN7kt8CZEvgjMHcIQSV5Wa7AJsvP6et-0kXqpQqFSLF1VrDZOrzfB0hRa0VxkaPmgkZA9ikutdu8l_LmtbfJr8t8HlxnehZvv_nEVna_hERGAflKFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مرتضی کرمانی مقدم:
✔️
امیدوار بودم که کادرفنی از ابتدا از اورونوف استفاده کند ولی این بازیکن در ۱۰ دقیقه آخر وارد زمین شد. من نمی‌دانم چرا باید از دقیقه ۷۵ به بعد تعویض کرد؛ اگر قرار است بازیکن روند بازی را تغییر دهد باید حداقل بیشتر از ۲۰ دقیقه بازی کند تا بتواند کیفیت خود را به نمایش بگذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139634" target="_blank">📅 15:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4Mmuf6rbrds42oOQt02MvlgxIIiYJbbpSs-MCLTFW9Q2GjRA_-vDl6bUtwEqQm-1kk9iF5e3clkLXhBa2reYwaOgC4NvnqrikdqEPSZQ7G1w5xHya4wqYmVQlLWBCUqoDPhDBymPobOayNZQ-eNTaG2K2VNEVCNZKqTJ0KY4XSHo4u5HLPew44V779VT7ARbgatFeFVMYucsygivUsvRbYnvm_lgUj7xHxe5d3OzQ9D_D6hVxWdnytC33PIO_84uswK75nE8YJLh9rTYB3DWtNy2_YWyBHe15dZUyqoMLwxyOJAVCWBWx1DM7TH_jvs87Gdpv7xchW5DRFxQ7rNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
با اعلام کمیته انضباطی، خداداد عزیزی، سرپرست تیم فوتبال تراکتور به دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف مدت 48 ساعت دفاعیات خود را به این کمیته ارسال کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139633" target="_blank">📅 15:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
فووووووووری
🚨
امید عالیشاه قصد داره فردا با حضور در دادسرا از خداداد عزیزی شکایت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139632" target="_blank">📅 15:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY0YkJFAUTh4sVFGynnFCLBM_AznMAQUn4oZiLCqxRS91nb9ItXFiWRO3Dg8Im6Jp1rU2dfXmQxjrny4kwLt2OMxZ66eJLwN0vtqNiHJ_TIKsaYbde_leEyJ-_ytD3Wi7giAAhp0R1pr9KZtUdTUTI6R6IJWeeuGQ0_ajOUPzRyMVR6irHGYhWLmfqtr5PyQ36ysX2UMEg96XaW7ERoPxHZwpIqL3QVB3KjiyYSSq1GgSV7Uf_d22d_pNetxGXnl95N_VeTbr-I46PNcNWjKGvqNnR3x9S_NUpq3QDMKRIg0-6ONRhH8kYRaxf9xRFkaEcJ2QOiVcCqwW53vWzyr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاتالان‌ها در مستایا آماده شکار خفاش‌ها، نبردی برای صدرنشینی!
🟡
Valencia -
🔵
Barcelona
⏰
Today 17:45
🏟
Estadio de Mestalla
بارسلونا با تکیه بر مالکیت توپ و قدرت هجومی، به‌دنبال کنترل بازی از همان دقایق ابتدایی است.
والنسیا می‌تواند با دفاع فشرده و ضدحملات، برای خط دفاعی بارسا دردسرساز شود.
با توجه به برتری کیفی بارسا، کفه ترازو به سود آبی‌واناری‌ها سنگین‌تر است.
📌
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و پیش‌بینی خودتو ثبت کن:
👇
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139631" target="_blank">📅 14:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139630" target="_blank">📅 13:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
تارتار قصد داره در بازی فردا مقابل ذوب آهن از شهرآبادی در ترکیب اصلی استفاده کنه
📝
خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139629" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139628" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139627" target="_blank">📅 10:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnkkEPRvoARVukRmiO7VNLoHt7chAtOWeoLTuMqzZhwDmpJZ8085prAv5owYqoqNQcNrnSW42O2syBLZMhFncZ2Wn-TTJg-ocW6dXRkBV3BU713yQhzwv4z05gs3B3JVhQe3jxuzIy1lomtWRMAJYJfPMsLMim0MkZkj7RNVCiF_hNc3J-jI3f-AGkSKjP03pzlQ-sYUXm5dE-WyeoX1shi1KIVxX6XzA1yKlPie5FIODKDWTozGBefd-3UjXFK-9LggYzBKqJrivLSuOv-Qj9uNkQyTwCeukE4a0KjDjjeB7z6-o9iQjrsBaU7-RVMTOd5W_2Ojv6H5hafkQoP4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
ازاون اتفاقا که فقط تو ایران میفته
✔️
فرشته کریمی کاپیتان و اسطوره تاریخ
فوتسال
ایران با عقد قراردادی به تیم
فوتبال
پرسپولیس پیوست
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139626" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139625" target="_blank">📅 10:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=rIAdd2PK2kNwt_DCM0bg8fXLkHLQKW9eauNtlmGCOmRQh_lgH9lL2U1nvyGy-vvj4UPkgp0k-m9jI08FOQfKwVjAoDIhKOAEy_lZH2ULtDEFTrjuCc6pD-x8ePUMMj1UlAOumoJYLozXbYCoDI27TAC5oyD_k8zj0puqb5h--7JtKFEPULtYMiP8_bUtze_O_XH6siz-fAgvUwDmWUoUfQuwRY1Ry1tZKT2GS5Q3_3KEpGBamRzOJu2VIG3JJ0TdlBuVZmYkFAUSJGHWrYJw62iu1C63Um8bv-2kBTeK7YdjPtlXE5VQOKQbK_agEy6FnvwQWu-MLImZaSZAw_spBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=rIAdd2PK2kNwt_DCM0bg8fXLkHLQKW9eauNtlmGCOmRQh_lgH9lL2U1nvyGy-vvj4UPkgp0k-m9jI08FOQfKwVjAoDIhKOAEy_lZH2ULtDEFTrjuCc6pD-x8ePUMMj1UlAOumoJYLozXbYCoDI27TAC5oyD_k8zj0puqb5h--7JtKFEPULtYMiP8_bUtze_O_XH6siz-fAgvUwDmWUoUfQuwRY1Ry1tZKT2GS5Q3_3KEpGBamRzOJu2VIG3JJ0TdlBuVZmYkFAUSJGHWrYJw62iu1C63Um8bv-2kBTeK7YdjPtlXE5VQOKQbK_agEy6FnvwQWu-MLImZaSZAw_spBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه باشگاه گل‌گهر به بیرانوند: وقت‌کشی، کسب‌وکار من است! چه برای به‌تعویق‌انداختن سربازی، چه برای کُشتن زمان مسابقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139624" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139623" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
⭕️
🚨
🚨
🚨
🚨
خداداد بعد از اشتباهات داوری به نفع تراکتور در زمین جنجال می کند بعد از بازی هم مصاحبه  جنجالی را چاشنی کارش می کند تا حواس ها از داوری پرت شود. یک سناریوی تکراری! اما آقای عزیزی! عالیشاه رکورددار نباختن در دربی در حد شما نیست؟تفاوت شما با تماشاگران…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139622" target="_blank">📅 09:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139621">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139621" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139620" target="_blank">📅 09:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139619" target="_blank">📅 09:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139618" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=D9X5issY8roCXGHK3u1D9SA1pHwBS81XBIEt8hyy_sv0F-9HpXhuAO49WBoiG4oIuw2HxifFXUuW4JUZW4C5c7xDj4_2VNmU2IP5RXvnhvkFlZgECpWL5aq-fK9tdIGEfTbhNes3gSG4yoxP4CPRHA0KvA1RACakoHld4Ud3KSoxK7_rA_W5FvclET8h84eD5BUitaLbOXS0RQ-US4qt7XHbNTuBsunnAXq9JBFwKEIf_zl6afZL7k5Ghdvfq_4CnsFrpN8-aIxNPUij1PW9NHqRGaa4iacr8kkLqN8qGcfaezblnQbIuNqxJJQ7bev3MxLF5G-o06OCVkCJdhF_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=D9X5issY8roCXGHK3u1D9SA1pHwBS81XBIEt8hyy_sv0F-9HpXhuAO49WBoiG4oIuw2HxifFXUuW4JUZW4C5c7xDj4_2VNmU2IP5RXvnhvkFlZgECpWL5aq-fK9tdIGEfTbhNes3gSG4yoxP4CPRHA0KvA1RACakoHld4Ud3KSoxK7_rA_W5FvclET8h84eD5BUitaLbOXS0RQ-US4qt7XHbNTuBsunnAXq9JBFwKEIf_zl6afZL7k5Ghdvfq_4CnsFrpN8-aIxNPUij1PW9NHqRGaa4iacr8kkLqN8qGcfaezblnQbIuNqxJJQ7bev3MxLF5G-o06OCVkCJdhF_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139617" target="_blank">📅 09:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOXObZtzkcF8xx8gNGortb36cyeWvuYc3gv3RonwEVUZUs6iFoFSZvFLFvD8V1_g3gE-CWwvjDrHgB_PRFYQ5OfwjwYFRvC_N6JbNfpvMY3NVyyu0LPQHcmdCMLSmHsFFJWoDxjKLVsU7MC_TJUGvloF5DYO5pnB1BCRZyRsGrM6HAchrse1s3NYSaXGKbgkjFWtfGl10OIh-ZkRkU7PHRecncGSgwbldj4Yv53tXd_Nwmb7mzOG-gIo5cEEMO6CY6viFIPcT2iG3rhlHGaFaxXCTClV6FbDTAw3f63DLNU4nl2JK6wJRILn-oTMBB-H5-E7pwO6oH935Id7kNPDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139616" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s839B11QihZb39e2hw4Nfeqh0uaHcQirFg9XBtVT4-Y2qDqRTqHSliEfueFlkIz7cMEnZPYhgxr0MO6jtx0wZdvLn48nXizN4-yJkUyc7viW71-EfGYQzVRMRxxHQfguHatpMc5jE6RWkyvOsyA8ZXtS__5iEgGp-n9B4x5tZKI5fCP5GEFPmM32Yepc4Yjey34XU_IBSvPXaCqEcfkGUxQgZQ_cvCAD8kMUCWmPw1vP-OAoV0sIDIzfYvfFeQ603ilLZfN0on071TuEyvrXjuf_DExvnt0_HBY-gy5aF1dwXLgAk0CbftlRtGLt68MmeK_ULIzghZUD7xqgMY8niA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
زورف و تابیلو؛ زورف با تجربه و ثبات بیشتر شانس بالاتری دارد.
تین و منشیک هم جدالی نزدیک و جذاب خواهند داشت که سرویس‌ها می‌توانند تعیین‌کننده باشند.
🎾
Zverev -
🎾
Alejandro Tabilo
🎾
Jakub Mensik -
🎾
Learner Tien
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139615" target="_blank">📅 00:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139614" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139613" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139612" target="_blank">📅 23:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139611">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=FgV6qaNOlAf3zge36DxpoRkCrPXpWzwhpKOm6V8lBI3HkyK3BFvudA0qdxgG1Khr-hL9O07BZ9vCuAWTA7RZzfqLW1hjjlhpJEDWSBECJdkNOLyIEgCJxlz03ZWXgT9S_Sr87BzcZVTJzl5FPh8NHy0gMTQaWw4FCbA8j7doFi70hcJfcQgSRbkbat_YcG559E4I1xojQVBpZYsHrBNAoeTOMOvx0ipx6wXDuXqJyZAxGAD8GdiBX8O-Tp4RF2tJa8S3JoTzTiovR0Hj94mCknt0k_VAS9IrCE8Zbuh2Ayk7zXeaD00JYFQBEzeI4JxB71V_04ThrNnjyWVpUVk_Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=FgV6qaNOlAf3zge36DxpoRkCrPXpWzwhpKOm6V8lBI3HkyK3BFvudA0qdxgG1Khr-hL9O07BZ9vCuAWTA7RZzfqLW1hjjlhpJEDWSBECJdkNOLyIEgCJxlz03ZWXgT9S_Sr87BzcZVTJzl5FPh8NHy0gMTQaWw4FCbA8j7doFi70hcJfcQgSRbkbat_YcG559E4I1xojQVBpZYsHrBNAoeTOMOvx0ipx6wXDuXqJyZAxGAD8GdiBX8O-Tp4RF2tJa8S3JoTzTiovR0Hj94mCknt0k_VAS9IrCE8Zbuh2Ayk7zXeaD00JYFQBEzeI4JxB71V_04ThrNnjyWVpUVk_Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جواد نکونام : نمی‌دونم داوران با تراکتور چه مشکلی دارن و امروز هم یه پنالتی و یه اخراج نگرفتند هر هفته داریم ضرر میکنیم
😅
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139611" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139610">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJUQfe1nOoDdhdZFWpvACY-muGAZ-vTkv5Rp3iIjLAqnGFsgDNI2orS_LieRHlwqwmKTF7AG5J8SauBelsq8PP-rVdHYl3AZ4AiCLvEfn27xm9wHdQO9psyk3LMQLo286PBqeP_9piFXxfU3WUXMSLCdVJ6dCoZYM4ndQ_QiDyUPoTPuXID8YG93jqKxO3vYHFbSGYV7dLeFHanFE5nOpeg3qFbo6hhrOm1do6S9BIJvliteShXpOeAcbt-TkYMKAjuwv07Z_CT0FcTEpYI-3YVJa8NewOZg5rxuzavJrXJGy-eEHfXWxDZ1iUswzAR6RL8zV4m7lHWNya8lAtyGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از تمرین امروز سرخ پوشان بعد از یه روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139610" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139609">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
تارتار: ۶ تا ۷ بازیکن من تجربه بازی در دربی را نداشتند، خودم انتظار نداشتم اینقدر خوب بازی کنند
🔴
بگومگو با سرگیف؟ همه بچه های تیم مثل فرزندانم هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139609" target="_blank">📅 23:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139608">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
داوران دربست در خدمت تراکتور؛
🗣
بازی با پرسپولیس؛ اخراج نشدن مغانلو در دقایق ۳۸ و ۵۵ با کارت زرد دوم
🗣
بازی با چادرملو؛ اخراج نشدن حسین زاده
🗣
بازی با گل گهر: گلزنی با کمک، کمک داور که اعلام کرنر کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139608" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFhl2wHvDZyuNoz7a29uMS5ELLLh-Tt5CNURIFYKipKqXYwFR_hW0Z81p6QdDElMxOYTz88riYdxsj5t1ll9p7IoftWptRtEctDIbfHhYisTuzi3Cy7vYAu06W4caymomlJzPgYuJDblHavd86nW2gM-s-nZSkdeSgLZWwKnxh--lhBGdR3WyNlL83RKoatTdEa1hIrAgPDLup2LBuH4i_PkGmK5naXFZL4HnX87F4Mx5SA87neeGxlEoOoDgdxH9vXXvgs402OI4ac18tz3PYtMecjIMtX5ZOq2xw8sxJsONtzKkJqiLCbaOMbIt2H89xvwW8eQJPcNAiXsaN7idg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139607" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139606" target="_blank">📅 22:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
🚨
🚨
🚨
🚨
فووووووووووووری
🚨
محمد عمری به علت مصدومیت از ناحیه زانو دیدار برار ذوب آهن و خیبر خرم‌آباد را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139605" target="_blank">📅 22:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=WIQ0rY-cz65DhBeCrhenqB9gFsB-Q23XihkB6whpDBsT9O7LLOmlHBJbq6VlsoYySjH_7O28BV1Mv0Gu_NH1yTgf5aIGJY7ia2EblHTcgYuBM6eTKFF9JA7P0Z_v6Z9ig8uGngLQJvIxYJqyjGBqZBvJoSjwgcioMG7k_D00Gy3QWkqVuOd9UNQ1Be3c51dia2PRE0vLaOIS8hzD_9DL0lkg7wfdCsmjKlgxEryJ7AFNfGaZMTpBT-ZdrO2yIZM1C1kN1-dAlqXpjs_OzZnGM9ThSAElMrnsC6Ri9qwM6yscb_WeoEpg3__m8y2wMp7eFHKiVuRAc8nVedUKwjQWdQBCPqlZT0I3jjoM8ynD-FEHRu6zenrxdNG-QLecXonh-5i5jOM0qF3wQ6nokl__U1xwzG563WwD9Ivzj2JurmG9GDXifoF78vF47lxAP5fj4fnXcw5JHrbY1Ep9i5nFxdQ0mSm58xCU2_hneJ01s27Sb22tnNFgwUDExQsmymDd4YTVF1Qhze_H2-7ajQrVqKUxvhjJCdXjLhtMsLxHOkb_6von3fHeziIWpQL50F1vy2Q-Fm3LE95qFKUcvxix72wh1K2cDT7txVtacnWGDIhOA3IX54aSNJk323gepEKt3oUelnCZGI35guVz4cphRA6RwGurQ_Ej38JcTWuFvi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=WIQ0rY-cz65DhBeCrhenqB9gFsB-Q23XihkB6whpDBsT9O7LLOmlHBJbq6VlsoYySjH_7O28BV1Mv0Gu_NH1yTgf5aIGJY7ia2EblHTcgYuBM6eTKFF9JA7P0Z_v6Z9ig8uGngLQJvIxYJqyjGBqZBvJoSjwgcioMG7k_D00Gy3QWkqVuOd9UNQ1Be3c51dia2PRE0vLaOIS8hzD_9DL0lkg7wfdCsmjKlgxEryJ7AFNfGaZMTpBT-ZdrO2yIZM1C1kN1-dAlqXpjs_OzZnGM9ThSAElMrnsC6Ri9qwM6yscb_WeoEpg3__m8y2wMp7eFHKiVuRAc8nVedUKwjQWdQBCPqlZT0I3jjoM8ynD-FEHRu6zenrxdNG-QLecXonh-5i5jOM0qF3wQ6nokl__U1xwzG563WwD9Ivzj2JurmG9GDXifoF78vF47lxAP5fj4fnXcw5JHrbY1Ep9i5nFxdQ0mSm58xCU2_hneJ01s27Sb22tnNFgwUDExQsmymDd4YTVF1Qhze_H2-7ajQrVqKUxvhjJCdXjLhtMsLxHOkb_6von3fHeziIWpQL50F1vy2Q-Fm3LE95qFKUcvxix72wh1K2cDT7txVtacnWGDIhOA3IX54aSNJk323gepEKt3oUelnCZGI35guVz4cphRA6RwGurQ_Ej38JcTWuFvi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139604" target="_blank">📅 22:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139603">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139603" target="_blank">📅 21:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139602">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139602" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139601">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=dXBT_w-jAaKFpHDRsp5dbubT7h2YSrjVZiaBUZeXv5Lw3i1pdr8N6ha846RFGHnpYv0N5xZcmfj-c3LGH4jyEM4v3iNOflExpYs7ce5RkECISAnwRvRTvpwqIXoM3B78WNhWVzBnQheawZmYMWOv6CA-bOsAxKj48Aus-axDn74cez95oa3NFaZ5yVZp6sr4WrE0X5YvSwH4m6UoO-2WetcoFMRSMVuPGaAizcLRx06DB8bxR2IX3jUEI1fsqNtB3dOuhEsLuxC9mHLGb_Nu99BCrHtMx55d2BBKa_CtxT7HT-eZ3NUKwmvHxKeszPnIPufhroW_TrIyTviPnWFkk2qlty1YWrkilurGV34IrqOTJs1N7Knkx0ESoMSVp0fW9BQGq6ha0P5s_CmNiqlNoL7zaWcSYC2eFcWA64sWFl5GJcP1z-X54gVuNrjZMYnDoHpxMQ-n7RPTY9tPGTMO4nrn-7TK02k2OELXxt1ryTaXKO1H08DICnCBBqmWhDN093ydGz1CtHb_GSshbL-vMT-V9nR79ZPC9EC1UIWuLj7wnrxz0Sk5xU8LF2rX-LwCTJAzIKTgx1D_7hdRx0ZHSU5QmebaxAZWaz2_mOunOQMirYVt4xHIY-3P8BoqEGAYN6QnTZ5L7RfpJwPuMsPsaIIucM7ClsRB3OFnSl1zgTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=dXBT_w-jAaKFpHDRsp5dbubT7h2YSrjVZiaBUZeXv5Lw3i1pdr8N6ha846RFGHnpYv0N5xZcmfj-c3LGH4jyEM4v3iNOflExpYs7ce5RkECISAnwRvRTvpwqIXoM3B78WNhWVzBnQheawZmYMWOv6CA-bOsAxKj48Aus-axDn74cez95oa3NFaZ5yVZp6sr4WrE0X5YvSwH4m6UoO-2WetcoFMRSMVuPGaAizcLRx06DB8bxR2IX3jUEI1fsqNtB3dOuhEsLuxC9mHLGb_Nu99BCrHtMx55d2BBKa_CtxT7HT-eZ3NUKwmvHxKeszPnIPufhroW_TrIyTviPnWFkk2qlty1YWrkilurGV34IrqOTJs1N7Knkx0ESoMSVp0fW9BQGq6ha0P5s_CmNiqlNoL7zaWcSYC2eFcWA64sWFl5GJcP1z-X54gVuNrjZMYnDoHpxMQ-n7RPTY9tPGTMO4nrn-7TK02k2OELXxt1ryTaXKO1H08DICnCBBqmWhDN093ydGz1CtHb_GSshbL-vMT-V9nR79ZPC9EC1UIWuLj7wnrxz0Sk5xU8LF2rX-LwCTJAzIKTgx1D_7hdRx0ZHSU5QmebaxAZWaz2_mOunOQMirYVt4xHIY-3P8BoqEGAYN6QnTZ5L7RfpJwPuMsPsaIIucM7ClsRB3OFnSl1zgTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139601" target="_blank">📅 21:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139600">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
🚨
🚨
🚨
🚨
فووووووووووووری
🚨
محمد عمری به علت مصدومیت از ناحیه زانو دیدار برار ذوب آهن و خیبر خرم‌آباد را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139600" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139599">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139599" target="_blank">📅 21:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139597" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=Rv2kxDQ5Lt6soK3KBeulzxsMvrPMyD39kMZsHSWqS0HsQ0QF6Ntg-kYhjYMHziDRiyvR5_a7jfmculVL_MOoHDTBTKXHNvHubgdHhi3D2pHCGy4oUIyKpR_IpqcsX6PzXj1jVW91c6IQe59pGMcZw9GV7_tkrZxlQyuGvye8LCHIPU6HigpyFKDU9pG7OKfzEGUCurUpjU2n0IAq5S67XrPkCT8fU7q770oHdKm9e67jdpG1Em5PMK5iglk4eMOx2ADLLo0RsY63sQ__zGuxOH9fXZFAuYVqVBuFlIMKlUWV_jB3tZ0azRXO2lZpFjSW6pwV1j7t5QhUKz87bA99NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=Rv2kxDQ5Lt6soK3KBeulzxsMvrPMyD39kMZsHSWqS0HsQ0QF6Ntg-kYhjYMHziDRiyvR5_a7jfmculVL_MOoHDTBTKXHNvHubgdHhi3D2pHCGy4oUIyKpR_IpqcsX6PzXj1jVW91c6IQe59pGMcZw9GV7_tkrZxlQyuGvye8LCHIPU6HigpyFKDU9pG7OKfzEGUCurUpjU2n0IAq5S67XrPkCT8fU7q770oHdKm9e67jdpG1Em5PMK5iglk4eMOx2ADLLo0RsY63sQ__zGuxOH9fXZFAuYVqVBuFlIMKlUWV_jB3tZ0azRXO2lZpFjSW6pwV1j7t5QhUKz87bA99NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139596" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139595">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
با اعلام سهراب بختیاری زاده در نشست خبری پیش از بازی با آلومینیوم، صالح حردانی کاپیتان کیسه از این تیم اخراج شد و دیگر عضو این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139595" target="_blank">📅 20:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139594">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
خبرگزاری آنا: صالح حردانی بعلت درگیری با آسانی در پایان دربی و مجموعه رفتار های او در تمرینات از لیست استقلال مقابل آلومینیوم خط خورد
🤣
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139594" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139593">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
✔️
وزیر نیرو:
✔️
✔️
دیگه قطعی برق نداریم برید عشق کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139593" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139592" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
سومین باخت متوالی رحمتی ...و  بعد از شش بازی همچنان گداوند گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139591" target="_blank">📅 20:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
بلیت دیدار پرسپولیس
🆚
ذوب‌آهن از همین حالا قابل خریده
👇
🎫
footballeticket.ir
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139590" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
✔️
و همچنان ادامه داره این سبک چکش ..یک هیچ یک هیچ بردن ..دفاع اتوبوسی و گلی نخوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139589" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139588" target="_blank">📅 20:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139587">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139587" target="_blank">📅 20:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139586">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
فدراسیون فوتبال هم از احتمال برگزار نشدن جام حذفی در فصل جاری خبر داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139586" target="_blank">📅 19:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=ZR6Qonahs13fuJLaM-4LVBGHVTotlfiseQLJB84Sh8SFXRBAq2FB3RxiHH7wLcmHFa8hUddWfiVt8t-Qn9qg61C1ViFta5p4TJeH0lT2ssx7S9pVV4ZUQG0IvkxBFnHMj39fZOQcYikbZQAoiC7gh2LubxJ9POqFuVi1F8x2OZrdJctJfb_mBEeN4-LbUXFM__Xgcgf8-39byv3ItAuAopS3pcScfQn9aS8JDngXcQ8gOPAOH6-MXs1tT3eVdJaxp7oMVBwCpCTF7PBjQktGWSG7WIU7ddJlFHDBCuKQ6jpKe3gDrqrKY9tnur8d5qnJmjMCRHfQHS0AJeCLciTrGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=ZR6Qonahs13fuJLaM-4LVBGHVTotlfiseQLJB84Sh8SFXRBAq2FB3RxiHH7wLcmHFa8hUddWfiVt8t-Qn9qg61C1ViFta5p4TJeH0lT2ssx7S9pVV4ZUQG0IvkxBFnHMj39fZOQcYikbZQAoiC7gh2LubxJ9POqFuVi1F8x2OZrdJctJfb_mBEeN4-LbUXFM__Xgcgf8-39byv3ItAuAopS3pcScfQn9aS8JDngXcQ8gOPAOH6-MXs1tT3eVdJaxp7oMVBwCpCTF7PBjQktGWSG7WIU7ddJlFHDBCuKQ6jpKe3gDrqrKY9tnur8d5qnJmjMCRHfQHS0AJeCLciTrGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
داوران دربست در خدمت تراکتور؛
🗣
بازی با پرسپولیس؛
اخراج نشدن مغانلو در دقایق ۳۸ و ۵۵ با کارت زرد دوم
🗣
بازی با چادرملو؛
اخراج نشدن حسین زاده
🗣
بازی با گل گهر:
گلزنی با کمک، کمک داور که اعلام کرنر کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139585" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139584" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
🖥️
وی ای ار داره چک میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139583" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139582" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139581" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139580" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
