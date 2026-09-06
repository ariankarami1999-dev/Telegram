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
<img src="https://cdn4.telesco.pe/file/RG5-AgYyTVcaE5pp3Ke9zprjkK9aKEfZOnjCW0_6V5a6JYCSn5S8psgBBzjiqoz-5EFz-pMxYxyS6V77oEYmrZtArNi2IzECRWP_n1HJuBRqDCJhpOnyJu6divH_E1o6TgcHC3Xi1FG4V2uXzPDvmeSHVyV763B9P33AltEmJoZN8zn_ga7u2R-VRpAO8lrYICXAjZ5AwnA3DWEq6y-IzHcYhFyc6PhNxHOE4an21RGnWXQqqPTTtcWxVukc3mkXZsphNx9-F_46acTCU6oN4wEEfkPaNXKHSpUT5zDhykgmIQJtG9I8BfGaY0aBEDIeKWokcqzICN2hxoJ2T4rwlQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 02:04:26</div>
<hr>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 581 · <a href="https://t.me/SorkhTimes/139673" target="_blank">📅 01:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/139672" target="_blank">📅 00:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SorkhTimes/139671" target="_blank">📅 00:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/139670" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/139669" target="_blank">📅 00:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/139668" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ1YqMi8vE22C9Qcg4_ubUOoO3nSpy_zS3273sOd7ksLHpY3e0xQ7SUOGsuRq6zQ198pZakNiAx02SpIxjdkqppH2Sbj8ZBzcREZQ8i5FxdOAoukdC4lfHu6GwbVN-q3EjKmENeSSGGPAfuuIi13Zp2x_tMOXto_3znThkXkzG_lc2PGdZaRJ3IFrYb1VHHgpyZZ56fwLz4hlB12zyTTKvngf6OFWLlYX3IIfBJEgpp9MF-YD4pBuo_q7Ig6kjtpHI9AArOM9y70_GT0TOz32nm4M-QB4AcXDwLp9fb3z1McYeVZf6UlvdeTAoP84MUL39N3j0GB3theyAnuYvgh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه فردا ببریم با ۱۳ امتیاز میریم دوم جدول
❌
❌
فوق العاده مهمه ۳ امتیاز بازی فردا</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/139667" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/139666" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
تارتار: باید با خداداد عزیزی برخورد شدیدی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139665" target="_blank">📅 23:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139664" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139663" target="_blank">📅 23:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/139662" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139661">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139661" target="_blank">📅 22:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139660">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139660" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/139659" target="_blank">📅 21:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139658">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139658" target="_blank">📅 21:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت، در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139657" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139656">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139656" target="_blank">📅 21:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139655">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
نایب‌رئیس مجلس اعلام کرد: سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان حفظ می‌شود، سهمیه ۳۰۰۰ تومانی از ۷۰ به ۵۰ لیتر و سهمیه ۵۰۰۰ تومانی از ۳۰ به ۱۵ لیتر کاهش خواهد یافت؛ نرخ چهارم بنزین هنوز نهایی نشده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139655" target="_blank">📅 21:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139654">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXDSY1lLApKtil_lhmq_uW9yNj3BVIQsKNEzgkdbJE1cqeENQxoM-a7vX3eZiPMDJVsuqcfVhQlnAjh36YXh1R5gDJquq8irwqSsuCUuRjDeE6uU5C_7FbEGtKAkIy7CBbPq2cyuucmft7fXtn7Rctinp4EMVlCTQO2uNdXEhhAE9gnMwZBMhcr4PVGdbqHegffTUjezlXHpPWM-rL6levcjXtGPe5NLqcQzCAusF3cHhBMDKs41aZmIswRGZT5G2zR_AyLIPbf1Ttqt6q08zow4r_mVjFadUWf-8MyBq_tAs1tM-ye8Rk_f1Dm4XLg7ppqQCPCz1UR3THieUh622Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/139654" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139653">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxKkErEPmORNUSb_K-_V6iZ7FumSlBsiNPIkPjwXGtcQ9Y7CajshKKztqLqqvlXwmSNG01ElaB0VL2uJ_hpF0xseolo8nMYm78fSPnNP4pifcZtr80S82VP4waZxIE-hVjMplsissdS141puVYumgFdEQ_XWfZi-2evaMXp3Ql0R380L1KXeKlazcaR0Km45PRVdP9qvADxW8-zE2Vlf9D7yWi_44YJ98XDz_xXWkXPnVTfx4p9aL5_uBo7XvJYwKYiyAYNCYVq7_Y-axVTSAkclIYsxZYoA7VKZa-8HLAi9gxnlgwlN2oqPlj9SL6urCP8RzDyhjg6SDiLiWZeAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول لیگ پس از پایان بازی‌های امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139653" target="_blank">📅 21:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139652">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
بازی کیسه هم مساوی تموم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/139652" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139651">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🗣
تا دقیقه 70 کیسه و آلمینیوم صفر صفر مساوی هستند ..و بهترین نتیجه برای پرسپولیس همین مساوی هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/139651" target="_blank">📅 21:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139650">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139650" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
ابوالفضل جلالی در ترکیب فیکس پرسپولیس مقابل ذوب آهن قرار گرفت و تیکدری کار را از روی نیمکت اغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139649" target="_blank">📅 20:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLVOUkP2o9Naw8ZFELv9205fqPpYl2rvYjDdn8hklssbho7UGeiic44Q6_pKrJfqrAejpH9lvw22_whk2HEwdfvN_hMq-tYaFbHQVPxcZC6dFJB2uHtF_Is-E6lHUo4jDs7d1rQJZkuMzoGZeROMTzL8pNHXQNLU_3vwJ5ZQaO-flFfr4VEWcOQenVRATVBQAEmjbUdiFCVyZwTVPiID0SqV4eCcZAWDeffOZxIpwA85FBsYGzpQp-7q-4H8602oYLJ2L6Saa4CyLufq1KHxmUP6Wg2ruI9nhH33FPYPVSRb0A7QBGIztlg3Hg83LwtHnMFh5z2zu4peUzPUU5PuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حلقه اتحاد بازیکنا تو تمرین امروز
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139648" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139647">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139647" target="_blank">📅 20:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139646" target="_blank">📅 20:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139645">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM40KVth6IxOe3a30wp-aMWNR7SPJJb7mbq9P6IcOmbZv_uL51dO674yWiesNbM6KPcq_IgPNKENgTPaKXOLjUvjUS6gE3kfJCNMRVG0LliRObvWULpL-N67aCnTdbTSLSHIclzsxkuet3tSzwpioyfLXwvfaxlYbspW-x8IOry1q6UcwGstNBxmasiwhWF3kjkb_lngMUyqsfDKUet6yqzi9kZjKrfMP5-fH2lOVRUTzQ3T0hGK7v48s6J8jBuPBxntHLINogusbn1j7neJMDsxt1ImDtXId_O2sx6hN3fxfrZlIVw1ifOIR8aKWHx49abqndJ7l-BTZmfEUkPREw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139645" target="_blank">📅 20:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139644">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
✔️
✔️
مهدی تارتار: کاش میتونستم ۲۲ بازیکن بزارم تو زمین اما این برام چالش شیرینیه/هم بیفوما و اوستون و هم عمری و محبی رقابت شدیدی با هم دارن/بازی با ذوب‌آهن برامون از دربی مهمتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139644" target="_blank">📅 17:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139643">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: اگه همه‌ی باشگاها اجازه بدن ما هم میزاریم بازیکنامون برن تیم ملی امید/منم دوست دارم اونا پیشرفت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139643" target="_blank">📅 17:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139642">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139642" target="_blank">📅 17:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139641">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139641" target="_blank">📅 17:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139640">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139640" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139639">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
تارتار: ما با پرس سنگینی که انجام میدهیم طبیعی است که نیمه دوم تحلیل برویم تمام شاخص ها نشان میدهد که در این چند هفته پیشرفت کردیم
✅
✅
شده سه روز به سه روز بازی کنیم باید جام حذفی برگزار شود
✔️
✔️
بیفوما و دعوت به تیم ملی؟ او خودش هم خواست که تغییر کند…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139639" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139638">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139638" target="_blank">📅 16:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139637">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
عبدالله ویسی سرمربی ذوب آهن: اولین نفری که زنگ زد به تارتار و برای بازی‌های خوب پرسپولیس تبریک گفت من بودم/ پرسپولیس واقعا چشم نواز بازی می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139637" target="_blank">📅 16:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139636">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
عبدالله ویسی سرمربی ذوب آهن: اولین نفری که زنگ زد به تارتار و برای بازی‌های خوب پرسپولیس تبریک گفت من بودم/ پرسپولیس واقعا چشم نواز بازی می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139636" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139635">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🗣
🗣
🗣
عبدالله ویسی سرمربی ذوب آهن: با یک بازیکن ( امید عالیشاه ) وارد مذاکره شدیم برای یک فصل از ما 130 میلیارد خواست و من جلوی این انتقال رو گرفتم. ما تیم جوان هستیم و نمی‌توانیم چنین هزینه های بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139635" target="_blank">📅 16:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139634">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbFQVuq1y4aViOzh8KG1URthi8-ec5eB1Ntugsbv9C33fEZviNDxIyt0prm4M_hy9pL20SZAiP9fePqqy22s50hyxypb88yhGWheHOasEHgN3Mzr7CthPoJgEd_abP-ugbsxAGjUzkiLYn4JjfGT2rA6U3tF_c2VHyIOhsHZ8ebCkJg5rwbGx3Z8xgmBa2izsTlRP0PMyydFtc3vSelwwQ3nlWLDHDeRHd5MXIuBT35jzCibB2N2LCFJfYpTFm__PDjdXfV4gRFRcS8V1YKPivKQ2dgwIfFsQHxxtYtuPP40aAbCvSWwh42gvHhfNz_BbkQ9JE9MN8_NE09je4L_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مرتضی کرمانی مقدم:
✔️
امیدوار بودم که کادرفنی از ابتدا از اورونوف استفاده کند ولی این بازیکن در ۱۰ دقیقه آخر وارد زمین شد. من نمی‌دانم چرا باید از دقیقه ۷۵ به بعد تعویض کرد؛ اگر قرار است بازیکن روند بازی را تغییر دهد باید حداقل بیشتر از ۲۰ دقیقه بازی کند تا بتواند کیفیت خود را به نمایش بگذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139634" target="_blank">📅 15:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ9sDkv01L_7dNASw6Z3qa8EQXr_KLDz-pp4kVPgUvfBC9PMf3b4sq750K4uuFl6SFJ80cBTpUVWHN_BN9Ic5givWLEpgxfptaNhQZsNLrVmkIT47CNm8BTJUnRzFe42QUTpLsC7wUW8NYpV9aLWQ-_rqxapiJYz2w9jXpP5trhb0XaUAmi937TUx0OhH6YeempB666P_QjnyRoabJFZmt0k6IL_U7C0aFY3PHNkUFrGBMgjkv-mnbdxV-WRT9ZHV18b47qUGFnoKHb5CXd8x3o6GIZs_Syk2Ha3pR9AbbJddxDZJ35YaR1FwBkZ8tcrgT22Ku7fPuA0pcPAKEDYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
با اعلام کمیته انضباطی، خداداد عزیزی، سرپرست تیم فوتبال تراکتور به دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف مدت 48 ساعت دفاعیات خود را به این کمیته ارسال کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139633" target="_blank">📅 15:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139632">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
فووووووووری
🚨
امید عالیشاه قصد داره فردا با حضور در دادسرا از خداداد عزیزی شکایت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139632" target="_blank">📅 15:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139631">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-FVE_lvhD-Xw6X6ucU1EEFNr86Rz3vKe2dTU0JBnkDw8ajZJ8TceVCgPxadUz7z-kkIWLvBRn4wO2yAt_YLDK6urbsIcEhIuCjLU3df7WG63t8Uf1fJXwzndiye8ISy0sgdGMbrhejgpm0Uda6Ui2I5Nyy2FFn8hphdqb2yoBqjVrlxvxFVO3zq-ui3gGAT39Equq7NtUtX9aDHyzTHueiBLju1zMdlP-RQJRfyqdYyrYybk_Ca2gqjqSU3XsCDkbmjit0I7v58ofZX07TqetBdIoR3w58Uv_Kg0rE1mgLBYrhQqyYefqbjwtggzCnPoRNqeeHbmrUC59GvVOd3Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139631" target="_blank">📅 14:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139630" target="_blank">📅 13:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139629">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139629" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139628">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139628" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139627">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">◀️
🔴
از دیروز که باشگاه گفت پرونده ، آسانی رو به CAS می‌بریم به هـــول‌‌ُووَلا افتادن‌... دیروز تاجرنیا و امروز این هوشنگ اصرار میکنن که نکنید بی فایده‌ست‌!
⭕
اصلاً ما دلمون میخواد شکایتِ بی‌فایده کنیم چرا آنقدر میترسید فشار میارید مانعِ ما بشید‌؟
✅
اگر فایده…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139627" target="_blank">📅 10:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139626">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orYR_coHR7fmkdMUqRxYq5k-ntrwH2Ws_Cu4pyR22k8L3b9r9K6IXBdR21nwvUnAfDyUP-8aDDEjcBNYX2Wg_WAb8u2ljCyBTPNy-p7q3OGHbGcRd2DR1g0E3dEBy7HKyMZ2U6QH9fWciW9DWmeSTG1e1CHnuj2Vfru1fWA11x22m72e-qW4vz4sLOlsweI-X_qo54dQ17eacm20JHG-3gFCo3PfTosykoRbw1HXCHsd-ERa0Kfq3mBRH_JtzRsSSZ2m0LYSp0MKeVhF3we7b8loAafYpcN1c4LQ6rJlAjY7kQ8gqP_1gLn03KRpY9kOOdTGoIeyBjbDDLN19X1NJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139626" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139625" target="_blank">📅 10:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=hfm-RdrWquVziNaB80Ulze62XmdIUwXrq_Y50VLv_IuqvqnpUgt5wSNt6F2iJm5fPpGG-p3fWCvNnvIWnXfEjbXguVTcEWBwGIuip7msJW_0gwRv0mAJRDUJU4-i1gm-2jok41Nd-n2rpqVcnfGOAJ9ueW1gI4l88rxKbm7ZtybcwIFQRasSnLDzDw_wCMyFyg1gCgR8uh8z6RcjiReKeOWo-bkoIZYh2l_g6Qfnvz6SEovwcW9EAticBJ8wDwsTaXWQ4m0l5U-GsntbK6GI11xdwut-sNKsleSMPNuDxTuDaiWyPfY2qVRWltD1IdALI43Mg58QCtyqrALwxpb6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0e507217.mp4?token=hfm-RdrWquVziNaB80Ulze62XmdIUwXrq_Y50VLv_IuqvqnpUgt5wSNt6F2iJm5fPpGG-p3fWCvNnvIWnXfEjbXguVTcEWBwGIuip7msJW_0gwRv0mAJRDUJU4-i1gm-2jok41Nd-n2rpqVcnfGOAJ9ueW1gI4l88rxKbm7ZtybcwIFQRasSnLDzDw_wCMyFyg1gCgR8uh8z6RcjiReKeOWo-bkoIZYh2l_g6Qfnvz6SEovwcW9EAticBJ8wDwsTaXWQ4m0l5U-GsntbK6GI11xdwut-sNKsleSMPNuDxTuDaiWyPfY2qVRWltD1IdALI43Mg58QCtyqrALwxpb6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کنایه باشگاه گل‌گهر به بیرانوند: وقت‌کشی، کسب‌وکار من است! چه برای به‌تعویق‌انداختن سربازی، چه برای کُشتن زمان مسابقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139624" target="_blank">📅 10:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139623" target="_blank">📅 10:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭕️
⭕️
🚨
🚨
🚨
🚨
خداداد بعد از اشتباهات داوری به نفع تراکتور در زمین جنجال می کند بعد از بازی هم مصاحبه  جنجالی را چاشنی کارش می کند تا حواس ها از داوری پرت شود. یک سناریوی تکراری! اما آقای عزیزی! عالیشاه رکورددار نباختن در دربی در حد شما نیست؟تفاوت شما با تماشاگران…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139622" target="_blank">📅 09:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139621" target="_blank">📅 09:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139620" target="_blank">📅 09:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
طبق اخبار دریافتی عالیشاه هرگز به خداداد فحاشی نکرده و فقط در واکنش به توهین و هتاکی های وی گفته خفه شو بابا و بعد هم به رختکن رفته و این بخش از  فحاشی ها که فایل صوتی ان پخش شده را هم نشنیده./قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139619" target="_blank">📅 09:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139618">
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
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139618" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=g__LYiGzXxT5TFiTA-ug9YNdGH5e_3stmwqhhOjLmHB1UaM2fKS0_6wgRDjD8YLuqyZl5kHv_tjr-cAPD0cJfMKO9Bqk3etZt__OC1peVocG07bIbQLgEdE8rtCgklTx9AjA1Ggq7A7uGT6HKduMPHSjdBWT7MBohsq4HYDq_VNZKCABkxD71PYy1Jt-wPtU3QzgKNC2IoAxuHcBuU7nT5yQrahp_XgTV5oYPhyfE9jRZC6GtqufYCburf95f27GvkLXKpFI4d8H7-tULSnP7acI7fZ7Qv5ZfDEiPd44H4XmI3lTIlP0GsC69DbwVwKuaf4p0da4PdOAvWygb6h-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=g__LYiGzXxT5TFiTA-ug9YNdGH5e_3stmwqhhOjLmHB1UaM2fKS0_6wgRDjD8YLuqyZl5kHv_tjr-cAPD0cJfMKO9Bqk3etZt__OC1peVocG07bIbQLgEdE8rtCgklTx9AjA1Ggq7A7uGT6HKduMPHSjdBWT7MBohsq4HYDq_VNZKCABkxD71PYy1Jt-wPtU3QzgKNC2IoAxuHcBuU7nT5yQrahp_XgTV5oYPhyfE9jRZC6GtqufYCburf95f27GvkLXKpFI4d8H7-tULSnP7acI7fZ7Qv5ZfDEiPd44H4XmI3lTIlP0GsC69DbwVwKuaf4p0da4PdOAvWygb6h-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139617" target="_blank">📅 09:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7SnfxH37vutuIChN0OLQdzF-m33P_n-lkzvsdfx3k7UHMoyKd979SrM6KwS3EOf7sd-iciiAYV6ycvltAPoKKqXcKpHcign-p_M49RKcNThhHz4SWHftCGyHm_pNzWMGjXR_3crkpmbdTKWFKqsEyrT0bQypU-_t8v1cWGfcwcAwM3joNqDPlGsAKPS9QX5ZXadLKv0aqbMlqfTGB0yBc7X8x1j_4p_XCNSDOE6E9GkRxizBimpGmczazShnVfd1i0MDqHDOhMxiBDGofxdax6VjuhRpaF3d-XfiCvdaT6L5cx-dExou0lHbIaTmXorV-g5vKGN1p4_eyxT2b4EXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139616" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ZS4qTBP8ghyVhDe081_y9Kxglx_sEPrba9-e0R7HyNnbgc2kw5o_gpqrTDo5GpwnpeK517a02rJJg7ADpUhxmCBqV_bbkjGm1M18Rjst_yUtUPiH9vFKtASop4AmUcnGo3Zu5LZA-b7WLgxTkdgqCuDqeSjO_CamZ7BRLQIweAY7Oj829Le_SNKh-r1CZ0AN-cN_HexSc1VvR7AM5jcDyLv3VmHYdIFQsy0AX-4KB8xBhNvu70PoBlyFNxOPO4y5rY50MMaggZ4w1FfkjGM1XqBRpAYOTEGcfCRku-Cv3vGk0EQPbLGQKI-nxasK13fyPa0HYtk-x8P1L646Vvqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139615" target="_blank">📅 00:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
بازی با ذوب آهن آخرین بازی پوریا شهرآبادی و پوریا لطیفی فر و‌ دانیال ایری برای پرسپولیس خواهد بود و بعد از اون راهی اردوی تیم ملی امید خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139614" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139613" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
ورزش‌سه:
🚨
احتمالاً رقابت‌های هفته‌ی هفتم بدون ملی پوشان امید برگزار خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139612" target="_blank">📅 23:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=PXOs4_burvFhVU_1ho8Bn7dz3XgLyB4cqKvIziR1qgERO3r_xa2YKIxfH6INk2JG429v4XDICv97Uwo1DNFu6cOgbAuX_w2ST1Z5FvIcN4VwlODmVx98jr3rYL_L4JX-tyimpHhbJf-R7R3mHrfLScvQ8oYsNIOZ_cZtM85jQ-HRAQSNZ57JrBfz0gEAh94Zv0jn3j6293q0cEQp7eKqxRGPAF5RLeF7kf4owcYvBm3Yq5Ge_mHLdSe4Pdfl4v_jfARL20mY0O3UwanlBu5kvFC3IO4UV-70jq55BagG9vlrZIzwEEGpm1SZuyJyQGZsOV0ZK5KytkfrqpJSzFIOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e817b6a0.mp4?token=PXOs4_burvFhVU_1ho8Bn7dz3XgLyB4cqKvIziR1qgERO3r_xa2YKIxfH6INk2JG429v4XDICv97Uwo1DNFu6cOgbAuX_w2ST1Z5FvIcN4VwlODmVx98jr3rYL_L4JX-tyimpHhbJf-R7R3mHrfLScvQ8oYsNIOZ_cZtM85jQ-HRAQSNZ57JrBfz0gEAh94Zv0jn3j6293q0cEQp7eKqxRGPAF5RLeF7kf4owcYvBm3Yq5Ge_mHLdSe4Pdfl4v_jfARL20mY0O3UwanlBu5kvFC3IO4UV-70jq55BagG9vlrZIzwEEGpm1SZuyJyQGZsOV0ZK5KytkfrqpJSzFIOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139611" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN9nzaV2S10tnMx0odA9th_sNCTsQDtCA9cqH3qDvC4EJoSQOHy2QnITGk8H1KsirwmqDL0oHSJUsyFPKB--jRDJyHH-kZoqxZM8ObmxiQB-cE4zkzwzWn3mpw0s2NmrlnBIY8bV80gjrmObEoCgN7lM3Ua1fdzy-NiwDZB-Wf14w-C4jOCklAuV7GKxNGUtXBahLt9DTrIsn4VqEjXoXeLPOv71kk9oGq6khgxuzjazb40LdfDtL7Usrh849MxjvMRTSWUCw3zi3oUTy6pi2OODKl484PqNIxybWoGXsDChBfT7NkF2ql62xieohyyLDFgElijrkpB6g4iH31YDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از تمرین امروز سرخ پوشان بعد از یه روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139610" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
تارتار: ۶ تا ۷ بازیکن من تجربه بازی در دربی را نداشتند، خودم انتظار نداشتم اینقدر خوب بازی کنند
🔴
بگومگو با سرگیف؟ همه بچه های تیم مثل فرزندانم هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139609" target="_blank">📅 23:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139608">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139608" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isoTYrPwQ8umb-Tsmv2iatJxnczNVcbIjSO_diAmjsPMrEOATaJtDlYUMHaAgPKcrzCgP_KZ7B44Vg6GNNBdVZLySDfguyuIqiIdzT8pl2yGDFwgJn-splnh4HS_9DpbPrsrwFDe_s0I3qFRoDeW0_fjpbFnxcAmq0bPBKh4SwnuiZbNdrHzgvyM8weseefqK0AtK_YWxO-nsh71oGhVWfblHEPgJnjWIj7rVohlmYwKshN7DoId84qykqdgpErxr3yoS5Hxhcue4mo5racnKAsQvLak_ItVy31mNGra9X966FPOyglnGTOumMLVYN0P6rsJCI6_ieS58AV4yF50pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139607" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139606" target="_blank">📅 22:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139605">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139605" target="_blank">📅 22:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=SHklK9Qvw3wGK3lBrEQ9Cve_ODxSMe-TC3AOSn7tgzZEf1-atTdP4atjN9ZYXNOfwRqHXnFX1YPVVi_1p3H_FdnsGMJdPI8dUmR8BhP00kGlf0tFV6r60MLWip2aCAZtFR2iq5uwk01YVtiojhYlWKtXgJT80lXie60d7YVV18ApTusn_ezCQ4p--H8NqXZZARrKil9XRTt6ORN81KcHmFV3B7iQW4wQRFQrlKVqfMabLnlPNPg62OnUQ3WRjITTBjFwAr4cPezn5hk5D-HNL7fH5j-D2WAXm1VKqvi6kGKGIYukd3963BQ7g5lonqUwvqRghAT1hGMpjcxVWd57_ho511khhf6X0RqasWiN20dDo4lt9Wpsy04oZfFxAsT0ZLKQpTLBG74PIDQj8Uflyvan1Llh6pQakJsrXU2n68DM-hiCd8iokM0NSEUBOsuymZOYO8oDnsCi2I0koXbgE-yhxh3RJD55yetEdVDBEWF7l_vzaSHkbUzsSAKcsGQVe_sWZxpdW5WFIOyuAYdAGWklYGcjspz-3Ur_BDbAN_W1FFypd5CbCG-b0AbC8JErAl2sUFsvJKDUCPtPVARTgt3XQF0aYML_-AWzD2602MWyTTkcwemGXrq79esqmMHulDZZKjegZZmv39SMEUn7GtLdibVifUM61AmbrmT9H4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e57f0199.mp4?token=SHklK9Qvw3wGK3lBrEQ9Cve_ODxSMe-TC3AOSn7tgzZEf1-atTdP4atjN9ZYXNOfwRqHXnFX1YPVVi_1p3H_FdnsGMJdPI8dUmR8BhP00kGlf0tFV6r60MLWip2aCAZtFR2iq5uwk01YVtiojhYlWKtXgJT80lXie60d7YVV18ApTusn_ezCQ4p--H8NqXZZARrKil9XRTt6ORN81KcHmFV3B7iQW4wQRFQrlKVqfMabLnlPNPg62OnUQ3WRjITTBjFwAr4cPezn5hk5D-HNL7fH5j-D2WAXm1VKqvi6kGKGIYukd3963BQ7g5lonqUwvqRghAT1hGMpjcxVWd57_ho511khhf6X0RqasWiN20dDo4lt9Wpsy04oZfFxAsT0ZLKQpTLBG74PIDQj8Uflyvan1Llh6pQakJsrXU2n68DM-hiCd8iokM0NSEUBOsuymZOYO8oDnsCi2I0koXbgE-yhxh3RJD55yetEdVDBEWF7l_vzaSHkbUzsSAKcsGQVe_sWZxpdW5WFIOyuAYdAGWklYGcjspz-3Ur_BDbAN_W1FFypd5CbCG-b0AbC8JErAl2sUFsvJKDUCPtPVARTgt3XQF0aYML_-AWzD2602MWyTTkcwemGXrq79esqmMHulDZZKjegZZmv39SMEUn7GtLdibVifUM61AmbrmT9H4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139604" target="_blank">📅 22:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139603" target="_blank">📅 21:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🟥
حمله جنجالی و تند خداداد عزیزی به امید عالیشاه:  اسمش رو نمیارم تا گنده نشه! در حد صحبت کردن نیست. به من میگه برو بابا. مال این حرف‌ها نیستی که به من اینو بگی. کجاها بازی زدی؟ سابقه دعوت به تیم ملی نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139602" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=dXBT_w-jAaKFpHDRsp5dbubT7h2YSrjVZiaBUZeXv5Lw3i1pdr8N6ha846RFGHnpYv0N5xZcmfj-c3LGH4jyEM4v3iNOflExpYs7ce5RkECISAnwRvRTvpwqIXoM3B78WNhWVzBnQheawZmYMWOv6CA-bOsAxKj48Aus-axDn74cez95oa3NFaZ5yVZp6sr4WrE0X5YvSwH4m6UoO-2WetcoFMRSMVuPGaAizcLRx06DB8bxR2IX3jUEI1fsqNtB3dOuhEsLuxC9mHLGb_Nu99BCrHtMx55d2BBKa_CtxT7HT-eZ3NUKwmvHxKeszPnIPufhroW_TrIyTviPnWFkk427I0zyxu5Vw1u2EnA_y5z6aM_iQ5OGD2WyNLuoj89W7KkS2_6CYxdZXX57zzUgjrMACC1flO_z4wRD5mnkf9QbjLlKFs-N3mrn4XVJUUBITyjIo_EwkGtdudxguzCL_jw520xkoAT5uF_yACmqfRSeRbSm6K37vCMuyAieFLJnuLyp-2o2XAEjrg3LnHFLggygfmF_xXH7d76V3YdJDMpATwGj3dIDy1Is1wziefis9iMrL3yxUY9zAK4-mlqrTsPS2wNX0RQHiu5JmkAlAgiFQ8UNOEzKJES-wU93HXOOvFUPtm2gYVIbwMls-Cov1_Sfav6wjvVA2l5IR08Syg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ea215c33.mp4?token=dXBT_w-jAaKFpHDRsp5dbubT7h2YSrjVZiaBUZeXv5Lw3i1pdr8N6ha846RFGHnpYv0N5xZcmfj-c3LGH4jyEM4v3iNOflExpYs7ce5RkECISAnwRvRTvpwqIXoM3B78WNhWVzBnQheawZmYMWOv6CA-bOsAxKj48Aus-axDn74cez95oa3NFaZ5yVZp6sr4WrE0X5YvSwH4m6UoO-2WetcoFMRSMVuPGaAizcLRx06DB8bxR2IX3jUEI1fsqNtB3dOuhEsLuxC9mHLGb_Nu99BCrHtMx55d2BBKa_CtxT7HT-eZ3NUKwmvHxKeszPnIPufhroW_TrIyTviPnWFkk427I0zyxu5Vw1u2EnA_y5z6aM_iQ5OGD2WyNLuoj89W7KkS2_6CYxdZXX57zzUgjrMACC1flO_z4wRD5mnkf9QbjLlKFs-N3mrn4XVJUUBITyjIo_EwkGtdudxguzCL_jw520xkoAT5uF_yACmqfRSeRbSm6K37vCMuyAieFLJnuLyp-2o2XAEjrg3LnHFLggygfmF_xXH7d76V3YdJDMpATwGj3dIDy1Is1wziefis9iMrL3yxUY9zAK4-mlqrTsPS2wNX0RQHiu5JmkAlAgiFQ8UNOEzKJES-wU93HXOOvFUPtm2gYVIbwMls-Cov1_Sfav6wjvVA2l5IR08Syg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139601" target="_blank">📅 21:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139600">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139600" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139599" target="_blank">📅 21:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139597" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=DoiZ8LRVLk6_vb8u3hfDbc8kKKnoTwL9UVGNjIEAJPNmmF1XL1bhYtPTnElYwHlIk99frUPDBl-YyOQznJF_NPXYLX_K1FJrklKe-3vSGRiRPD-oQAqimcMbXR0kNwfYdEXjG1w3mj0Y3yl6W2IQw7iJv9VyOSkrV0govBiV0uXPSBlqjJ4H1zQdWNdM9-1v74-ryYUW8TeIfm2H-DSF3AodXyW03qKfq6oEP8aAd9Bu4VXfp_nPjmo9LAHJ8nuXdoXO_6tMK0CONXXPVHxuTC5PyME4Ku4Kpogv_fp-VM3LmcGWS1iadqO44GE4qoXa46WU6lEMpkqPwOK-H7Terg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=DoiZ8LRVLk6_vb8u3hfDbc8kKKnoTwL9UVGNjIEAJPNmmF1XL1bhYtPTnElYwHlIk99frUPDBl-YyOQznJF_NPXYLX_K1FJrklKe-3vSGRiRPD-oQAqimcMbXR0kNwfYdEXjG1w3mj0Y3yl6W2IQw7iJv9VyOSkrV0govBiV0uXPSBlqjJ4H1zQdWNdM9-1v74-ryYUW8TeIfm2H-DSF3AodXyW03qKfq6oEP8aAd9Bu4VXfp_nPjmo9LAHJ8nuXdoXO_6tMK0CONXXPVHxuTC5PyME4Ku4Kpogv_fp-VM3LmcGWS1iadqO44GE4qoXa46WU6lEMpkqPwOK-H7Terg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
پاره‌شدن افسار سرپرست بی‌اخلاق تراکتور تبریز و اعتراض شدید به داوری که به نفعشان در بازی امشب سوت زده بود، باعث دریافت کارت قرمز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139596" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139595">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
با اعلام سهراب بختیاری زاده در نشست خبری پیش از بازی با آلومینیوم، صالح حردانی کاپیتان کیسه از این تیم اخراج شد و دیگر عضو این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139595" target="_blank">📅 20:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139594">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139594" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139593">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139593" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139592">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139592" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
سومین باخت متوالی رحمتی ...و  بعد از شش بازی همچنان گداوند گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139591" target="_blank">📅 20:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139590">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139590" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
✔️
✔️
و همچنان ادامه داره این سبک چکش ..یک هیچ یک هیچ بردن ..دفاع اتوبوسی و گلی نخوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139589" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139588" target="_blank">📅 20:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139587">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139587" target="_blank">📅 20:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139586">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
فدراسیون فوتبال هم از احتمال برگزار نشدن جام حذفی در فصل جاری خبر داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139586" target="_blank">📅 19:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139585">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=tSgP85dWq7y7vO83-p2Ta5IfLIh72N4Tcu1YhUFQA9eIu_02EHA4UnhkwXPcHVZ23EHiyHD2kUamDjhJk1RAqDRf1HrfribHtLzr3TfoSaYhe63MiIuiOa39pWYNvUSSkLUh-mOuAbJt4eZmu8R3jcD5oLEcQl69Lmm14Fnci4RxkhYRpfxvD30cw_0ty8HX89IAc1OS3oSirjsQWgvbhFvdT7tEeJISN8AP00oN0aGSDU4HrwiG9Vbw2bW4u3tzIJjuYOFTJA_P6Rs-p3VaUO0-3NogMQ6ehm3nLR_ZqAG8zlUZmrn9dVS8qPWTp60eQmVu7z3ghMH2HcCXgRsz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5646fba40.mp4?token=tSgP85dWq7y7vO83-p2Ta5IfLIh72N4Tcu1YhUFQA9eIu_02EHA4UnhkwXPcHVZ23EHiyHD2kUamDjhJk1RAqDRf1HrfribHtLzr3TfoSaYhe63MiIuiOa39pWYNvUSSkLUh-mOuAbJt4eZmu8R3jcD5oLEcQl69Lmm14Fnci4RxkhYRpfxvD30cw_0ty8HX89IAc1OS3oSirjsQWgvbhFvdT7tEeJISN8AP00oN0aGSDU4HrwiG9Vbw2bW4u3tzIJjuYOFTJA_P6Rs-p3VaUO0-3NogMQ6ehm3nLR_ZqAG8zlUZmrn9dVS8qPWTp60eQmVu7z3ghMH2HcCXgRsz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139585" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139584">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139584" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139583">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
🖥️
وی ای ار داره چک میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139583" target="_blank">📅 19:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139582">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
ترتر گل اول رو  با حال داور به گلگهر زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139582" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139581">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139581" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139580">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139580" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139579">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
محسن مسلمان به کادرفنی تیم امید پرسپولیس پیوست  مسلمان با پیشنهاد بهادر عبدی و بعد از جلسه با ادموند بزیک مدیریت آکادمی پرسپولیس به عنوان مربی به عضویت کادرفنی این تیم درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139579" target="_blank">📅 16:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139578">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3xi9HOuO2hxNyg61YGdbFE0JFFTVV2_LM4kz9dFYFarXXFNt5FRm1z3lRN05PIFjlXIlciYK-tgbS7W-DwjucpM9pFwcHhVBJdGpdiHBaR8r0Ht4stogt2sj2-KNPT8AXd_6GMGyoWnvErMGQEgInRMhpXEOlmLOW8TmRYkdt88exxRgtqtXB_MqQ8IPwajH7DgdQXLgwjt4X-0Weuw8FL8FwophiV4fOxRwgM4bXFHwHsZvzYxFcjsmDyzvB0z1F7lt0dUuK1x5tyVhufjGUidoMC64H0-V6K4YYCKejm87BaYn_dbWOes1vP-BhBdcdwGm0FzAiVvcr-bZ1D0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
حکم سنگین فدراسیون فوتبال علیه مهدی قایدی
⚪
با رأی کمیته وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش از مهدی قایدی، این بازیکن به پرداخت مبلغ ۱۸۰ هزار دلار بابت اصل خواسته و مبلغ ۵ میلیارد و ۴۸۹ میلیون و ۵۷۰ هزار ریال بابت هزینه دادرسی در حق خواهان محکوم شد.
⚪
نیکومنش مدیربرنامه سابق قایدی است که گفته می‌شود واسطه انتقال این بازیکن به شباب الاهلی بوده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139578" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139577">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
روزگار خوشِ «مملی»!
❌
❌
محمد خدابنده‌لو بالاخره در این فصل به فرمی که هواداران پرسپولیس انتظار داشتند رسید؛ هافبک جوان تیم تارتار حالا تبدیل به یک مهره اثرگذار و مهم در ترکیب این تیم شده و روز گذشته هم در دربی ۱۰۷ فرصت داشت یا یک سوپرگل خودش را در قلب…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139577" target="_blank">📅 14:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139576">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tggmFxVAlLdvUHZ6qGGiyDRdHy2X5AdlRNwbyeO5CPe5Y6i7GNlBFL5V3yqD8U64emnXK5RPRf_ql2QSoObkszYNHS9FEdxLnztA1FbQ1fuRfIYP2zfqOSK8i0jkgOdPinoM4fw2muVjsLGO91zZtWZbaI1OIVOVTy7F3Qjq1qzJCVoSekVVGaBnOSDMo-fC9m30cV_SIH4IdktQwDqDtcKtI1gLc8TKPM6tU7s0inV8ubq7n46BlsJ7ndVVm0VAKbrEmiI8BmE0Bci-4ZMc8ElqSFNTs5gALlBHzN5Fs-qKmmQ3xA7b51R6gXClXvT6zkfx6irBxsrk2duaDCFYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کنعانی‌زادگان به ۱۱ دربی بدون شکست رسید؛ اما رکورد همچنان دست عالیشاهه با ۱۸ دربی بدون باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139576" target="_blank">📅 14:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139575">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139575" target="_blank">📅 13:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139574">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzO6OTTRJcNCgYJjPP6UO45eE0p2zDw7qIl0dp7V6qkaLdaUS7oGnOBPNS37MkJefGyO8EfA2ANCVrNoItSgtZYTwXnmquP5qLt_o5vZ29i3f3xUfDd9x7YnrcVaTzD33h_20cePMLS--8wlgNpyJmYaP4tRATlWtInzUWCgTFEuY0_ubCa4QmHhqVwk7nFgE8XLYx2yIWRz3foqaVY7loeb4IkEWamBDCIrbGazE5ZeF5VJhkxGf5QOkqc1ktaBn281oDK2Lfe2QN4Lv5zr5xXXWOwU-v-1riO5q0sh1d3D4WX8rqKkaUnUtX98vF_UUkPDdEP5ZDpdKEeI_QwlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد بزرگ در جوزپه مه‌آتزا
🔥
اینتر و ناپولی؛ جدال برای صدر
یک شب سرنوشت‌ساز در سری‌آ
[
اینتر
🔵
🆚
⚪️
ناپولی
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139574" target="_blank">📅 13:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139573">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwpDpY-ANhhHlvYq_OgfbZzNBnqOXy4f_x0Y0JWy6we-R3hxux3_3hyOYr7YO0hAPK1_B1NN-zTaFaQPcKCcwABpUvRheGo5hPpTq5bCkjpx2oilimPlI_u3xg6MxUrVwgmdkjGCeXcPh0sAyoP3of8XausMmx3FG4yNdq11GT9Po_AsD7YA5_5ozi7PlMnlMxn-fVUVAD6HImr9Uubd-9FSElcXJpHymyUdDkUrNdO8PKdEbAXlbBxc5jRsQMahwX2gcmN7vIzwpX9w7IIp6L5dPPF1Kuj9H9htVxcYGytiAEbxgQrIi0CWS7GyH8ZVDR1KeoVvdNfFaH10HBPi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیس از سوی کمیته انضباطی ۱۵۰ میلیون جریمه برای استفاده از مواد آتش‌زا و سر دادن شعار علیه بازیکنان حریف و ورود تماشاگر به زمین در بازی با ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139573" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
