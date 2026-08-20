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
<img src="https://cdn4.telesco.pe/file/nGVx4LkmBo_UM-gDYgiwuhgkItDgdngJbDaswq5LlYo2490oL5q32vi-JzSq622pBhaw59McSQaeXd9EYDRBMl0YmEl04_iZ1cq0xP-qblB-FKAcAfDaP_wj60pTvjagjkbWzmQ7lItVJZqiOdbx5lU3uUVsRGadGwm3UU0-NlReK-zKDg0_tiVgN83VanoglODNt9exlbXt8R0kufsekDN_EAgrAQy7SA03qpROyKOdSxrdAMux83sX-btySnXQHWrcWnsQPQTqLZl0nG_AypEqPjdReYc5becSlj-kcVz9n2JkRMAxUDDdrrWx8hRn3bITCbmblQWBCxUR0ALT1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 00:49:05</div>
<hr>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/SorkhTimes/138695" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/138694" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/138693" target="_blank">📅 00:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🔴
🔴
پیگیری کردم؛ ابوالفضل جلالی احتمالا به دلیل مصدومیت بازی‌های حساس پرسپولیس مقابل تراکتور ، ملوان و استقلال را از دست بدهد. در واقع یک ماه دور از میادین.
🟫
🟫
🟫
البته خبر پارگی رباط صلیبی صحت نداره چون زانوی جلالی نچرخیده که رباط بده و خودش هم با پای خودش بدون…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/138692" target="_blank">📅 00:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✖️
✖️
احتمال معاوضه بیفوما با رزاق‌پور وجود داره.
🔴
تارتار تاکید ویژه داره رزاق‌پور جذب بشه. البته تارتار فعلا در قبال رد کردن بیفوما پاسخی نداده.
🔴
ولی درخواست فولاد همینه. بیفوما رو بدید رزاق‌پور رو ببرید.
🎤
سپهر خرمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/138691" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/138690" target="_blank">📅 00:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138689">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/138689" target="_blank">📅 00:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚜
علیرضا بیرانوند در تلاش برای حضور در تیم ملی امید ایران برای ۳ سهمیه بزرگسالان میباشد تا با کسب مقام احتمالی در مسابقات آسیایی از خدمت سربازی معاف شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/138688" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/138687" target="_blank">📅 23:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138686">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/138686" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138685">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/138685" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxI7Nn_EvwKByt1c90AXysGWEfUn25BSieJml0MM33UlAe2RwP7tzLSM3lpJC6eVNeLEkJh7ToSaknucmsWILOiExV3QohTvXSFqFHqwelIU4Zq5yxnBmxtiVJJK3D_9-NU3gmu_pgRgAduRkNSlEZvbcT1mtmZCWcrEN7XuxBWw6ffujDLl8Vdh54qZSmi50q7X6eRhyI8ag28HPBFUxCE2S4n1rks9HQvap2oq6-y72iDjFFxG0BzB5-JM80T0aK6jdcC7VYvC5n2A9DNBTiOgin2vYJyuw5DjcZ7ZZ1hxHHzBQENJikkb0nHwbpwdFb2IW_IbU7gZstPPv67Fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/138684" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8400611245.mp4?token=mvfT9evUxA4DaD0lbz68ANW4zqjc_E11FAV-yqRuZuzyWGGx1JEwqat6sOxILaT0n7fp3k3wWB7vjcVayuCEo3fstanYUx0wpGcIOsOX5op8X6GIyT1t0QISVxxs4Bjmz53fdyg53hjLEtrENVFby4C-IKNtFWLRGUR_k-qT6kzxoRTbv7KM_XYMo2XTadUIXDQ2OKFtiaWJnwf6YuMyzjb9GYmvOlKFyap4mK3_kxIVgF2OLoglawgG0QYrlyY6pnbDhzDHoST3o-RMVWgPa9ZdikI_W_rGKbDKxQIN-86Z7bpTamcEzQPjWg85wYr07ooAFRGo0xyXiBKpz2mSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8400611245.mp4?token=mvfT9evUxA4DaD0lbz68ANW4zqjc_E11FAV-yqRuZuzyWGGx1JEwqat6sOxILaT0n7fp3k3wWB7vjcVayuCEo3fstanYUx0wpGcIOsOX5op8X6GIyT1t0QISVxxs4Bjmz53fdyg53hjLEtrENVFby4C-IKNtFWLRGUR_k-qT6kzxoRTbv7KM_XYMo2XTadUIXDQ2OKFtiaWJnwf6YuMyzjb9GYmvOlKFyap4mK3_kxIVgF2OLoglawgG0QYrlyY6pnbDhzDHoST3o-RMVWgPa9ZdikI_W_rGKbDKxQIN-86Z7bpTamcEzQPjWg85wYr07ooAFRGo0xyXiBKpz2mSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازگشا سخنگوی باشگاه پرسپولیس: فکر نمی کنم محمد قربانی را باشگاهش بفروشد/ پرونده هیچ بازیکنی را برای جذبش نمی بندیم ولی در خصوص این بازیکن با توجه به مبلغ قراردادش اصلا وارد جزئیات برای این انتقال نشده ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/138683" target="_blank">📅 22:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/138681" target="_blank">📅 22:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🚀
آف ویژه سرویس نامحدود
🚀
1‌کاربره فقط و فقط 600T
2 کاربره فقط و فقط 700T
3 کاربره فقط و فقط 800T
ثبت سفارش و پشتیبانی:
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/138680" target="_blank">📅 21:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
🔻
🔻
طبق شنیده ها فولاد در آخرین جواب به پیشنهاد پرسپولیس خواستار معاوضه بیفوما با رزاق پور شده.
❌
همه چیز به نظر تارتار بستگی داره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/138679" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">💢
💢
💢
باشگاه میخواد یکی دو بازیکن جوون رو وارد معامله با فولاد کنه تا با قرض دادن این بازیکن ها و مبلغی پول رزاق پور رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/138678" target="_blank">📅 20:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/138677" target="_blank">📅 20:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5FoAAg8PW4O6PGkGyHM8oTLGahzIFoFWG5N9oXBzY1uD70TeFMkMjRUv9EER06u9gnodwjgd67v_YyIeAEAI9FM_3VhpsNUnbVxkXFeSGZ3E9NVE2yC5SbtQ-EZ3N19gp5HYoJBBYBRaW3O2PHEvwPUgfm6QtHQ-lB8ILZPg8N7407uyvsvmm7FBTe6whuNz8nq_I2eWY9eCR9FsUJUq5EiZo6ALUA7I8DFGTPenFNBFlsF8UMRl5aIwRr2vk8WKmyhzPjeTh0yc7pYd_wv0vntSuAUN-xgVW82-j1CZbB4lUCzYEgHUtYVI-NvoEGq8ynSuMHX0SCyrol_vUfhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
فوری ؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ دو تیم بزرگ ایرانی و خارجی رقم 1.1 میلیون دلار است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/138676" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3BbX7QGgcivW5YUReW8CknSzBElUrylIkllbNnLYgGRAfwVip-sVl1EsK8oQQ5sld9H1LliYT8jB65oSdd98e1b3Ssg7XSrnhGyhxvuDx5k3Dp7u7K7cJruwT8NUfAbzPG8JIeD7H29fhkCRruSPa-cVT2wEtHIzMUZ5FBaMgaXgWa8K3QEvtlmMP_hsNKpbw7yp-X4F1eawRkxDLSmO14HsIradwZa6CT3L2IIcgd0fF4CROtGoN8BJxbzKojkuQ19vnK-UKl2BC5FdSr0CVDWve3fpiH0vgtr-EwAG_JWXkqMkmCf9Z8crjXKoLi4mD__g6cR_3v-gCZiwTo-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138675" target="_blank">📅 20:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=qN4nOFzxJ3RjxTtwaf5ZN6oQFyM4HfQFmGo4VKJeEam36cGCrBAE1suFJr1-XDjEXTkR2uNW6ue7D8ldTZaFSBLTiBRURMEF2xSO_0kREUjn98zG3FzIILahmO8idAccNpo0yEDhZtCkJLTEPP7XwjNXAuUDM8kZiMBQcqfUpjrDb3Kr5nsm9RdREbmOr2_vPrOmo-BC0bJKUivZ2pMjqf3sozYdIg9JIGXru6Z41MQ1TfGuVv0o68A0cezz3taz123o8sNFZwbfsn4JdkWSV7lY7adJMHnkFUapXJzuZaxtdyZJx7XQNJ9bC10HWNVmndMXfs5LZarhALQrKZPNMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=qN4nOFzxJ3RjxTtwaf5ZN6oQFyM4HfQFmGo4VKJeEam36cGCrBAE1suFJr1-XDjEXTkR2uNW6ue7D8ldTZaFSBLTiBRURMEF2xSO_0kREUjn98zG3FzIILahmO8idAccNpo0yEDhZtCkJLTEPP7XwjNXAuUDM8kZiMBQcqfUpjrDb3Kr5nsm9RdREbmOr2_vPrOmo-BC0bJKUivZ2pMjqf3sozYdIg9JIGXru6Z41MQ1TfGuVv0o68A0cezz3taz123o8sNFZwbfsn4JdkWSV7lY7adJMHnkFUapXJzuZaxtdyZJx7XQNJ9bC10HWNVmndMXfs5LZarhALQrKZPNMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
🏅
این شاهکارو از دوربین باشگاه هم ببینید
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
❤️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/138674" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTghdpDzTQT2py5AU9gXZlXPLOxhHBiEeaKK1qNSqx23N1CSA5_0yYkvvL_P7sLfFOGBmWGNsdasST3CahbwIOkrhHhbrNEyd81_6rciZ4pkbIzs5ZNMa-mDOw2fRCKZnjgCA6AaI7LtQ3LxEHiDl7K2wuBpOJCwNWxfQBwwPGSnhiCS0KBJ0oQrlxhFc0TJCcNJJudTSc2Vx-JuoAvB2fdHJJNTD6Le4hqHImGbnBVK3WhfPe6D_Hd0muW5Pk7xdMG_CoQzspIShKm0iS8VPSssbala8aaruaR70tsJSiAu7fU8JCu1JNuFNzrjh3RzLLO7VKouD5kVUPK53HYfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه بازی Scarab Temple
7️⃣
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنید.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/138673" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔔
⭕️
احمد العتابیه، رئیس نقل و انتقالات باشگاه الوحده، در مصاحبه اختصاصی با رادیو ورزشی دبی تأیید کرد که محمد قربانی، هافبک ایرانی، در آستانه جدایی از این تیم است و خاطرنشان کرد که دو باشگاه ایرانی علاقه جدی خود را برای جذب این بازیکن در پنجره نقل و انتقالات جاری نشان داده‌اند.
❌
العتابیه اعلام کرد: ما مکاتبات رسمی از دو باشگاه بزرگ ایران برای امضای قرارداد با محمد قربانی دریافت کردیم و این بازیکن در صورت توافق نهایی این باشگاه‌ها با مدیریت الوحده، پذیرای یک تجربه جدید است.
❌
العتابیه فاش کرد که ارزش غرامت مورد نیاز برای جدایی این بازیکن ۱.۱ میلیون دلار (معادل ۴.۰۴ میلیون درهم امارات) است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138672" target="_blank">📅 19:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/138671" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🚨
مهدی طارمی برای عقد قرارداد با الوصل امارات راهی دبی شد
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138670" target="_blank">📅 17:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔄
🔄
🔄
فدریکو پاستورلو؛مدیر برنامه طارمی:
🔻
جدایی‌ مهدی‌ طارمی‌ از باشگاه المپیاکوس قطعی شده است.
🔻
درحال برسی پیشنهادات هستیم و به‌زودی تیم جدید طارمی رو معرفی خواهیم کرد.
🔻
مهدی یک آفر از لیگ ایران نیز دریافت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138669" target="_blank">📅 17:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6RhVWu-k4OGTPHGjsoiskxarsuC4v6AUQZTypP1hr4PaqWZ1HtbLvdVlSJE--6QEpL6VhkJC3yPOYni1zPQH0GzypENpfFp8xvF26Y_-47mmSq3ta0C7T6jDxgesbbvygyUKpd4XAWa0EbEJ44PELS7qpkqB11AaraxgOdE1eD-VqeRfzoqoBmZeUC6gQcd0r4eeVG3VYouKVcC2qRC7spVO_ijjjJEaMjZrHdLVpBfpZRwBJiOHZJM1bjT3R5GJ-6CagEBVyBlG14MEgOEAB5u42p6XhGUW9i70_JNPWDuI9lzEg_PIwD8XkSJYpyZm1weFgtUxvrjE4M9dXmeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
شایعات: الوحده امارات با فروش محمد قربانی موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/138668" target="_blank">📅 17:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
ایشون بازم نخ داد
👀
🚨
کامنت محمد قربانی برای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138667" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138666">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
یکی‌ از خبرنگاران نزدیک به باشگاه الوحده مدعی شده که محمد قربانی با عقد قراردادی سه ساله به یک تیم ایرانی پیوسته.
⏺
اما اسمی از تیم مقصد نبرده و گفته این قرارداد به زودی رسمی میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138666" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138665">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💢
💢
💢
💢
مدیریت بانک شهر صبح امروز به وعده‌اش عمل‌کرد و 800 هزار دلار بودجه برای جذب محمد قربانی دراختیار مدیریت پرسپولیس قرار داد.
❗
❗
مدیربرنامه‌های‌محمدقربانی  به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138665" target="_blank">📅 17:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138664">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138664" target="_blank">📅 16:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0QqQswPKtGdCy1fJ_SEDDQW8qDzhAsdN0rgVGqj0Oa8nPMksdmYI_2MZ1S81CamAha9D0i_jek0hZ54tzeUwesBkZeFhnefAHhRTPleFE53ZH_DA-4rHLeX-Z5lTaHe7vKrlrl9IcTH0bCNKsmjxfxA-tsKYrAhZIi3S2Aw2BTgwJcpkPjmwIthZELTmtFgd6tLYVmpaMdXLrGJTUle-NlMVcb1V7oZYnv8YHYl00cEfOPTxMkHRHE5tdOoTowdTss-6gpWU2tBcTfP-Fz0UyvZ4vtS6d4hezHg3UpbUzr8_Hm0TrTnDjPJXQWnxI9LghGdUjvbyI1V0anO96Q0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138663" target="_blank">📅 16:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138662">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
تارتار: چون جلالی از قبل هم مصدومیت داشت، وقتی نتیجه ۲ بر صفر بود ترجیح دادیم ریسک نکنیم و او را تعویض کنیم.‌ما در پست او همایی‌فر را هم داریم که از جوانان خوب است اما نیاز داریم در این پست تقویت بشویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138662" target="_blank">📅 15:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138661">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
✅
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138661" target="_blank">📅 15:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138660">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQDZAYpm_omVrMXHNN0w5xY1OufN71TEgEkEYhho4yJ7nCJX8dQKHTOquCQhTawAjBo4Pyb5MzqvhMPuQR3xr5U2egukAkS1N5juBZ8e29RWDSvP3AjdWrRjY-mwSlJWvlNRfet6y27GsXLkQWakiBy9kQNfAEH99QgsiiID7iGEYc-aZdgLrVXZSOke27VOHlkt3NhmOX1GrhYM12GeZNROrtalIOPjwC6UIbumjVCq6tQ7HpIZq7z_qZeUYwJasu8vuqylFuxIBx2GzExWsGzPQNQhu4R64OZNrKBK9OqSjvAF74O8Be5rMijICo7uuDn_rOws33NsCKrKrWBCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138660" target="_blank">📅 15:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138659">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKZk4iohsj7i8yVPZq-DD0AG6ivfAG52GbaoZe2b93LJkOL0bcd_UUtwV6sFse-Ro9OGWSMkiVlXA5mV-tPQNwBjz1qEhiF2amVn_ML5i0L0oqOf9ExMQCK99Vr2Dy15o9UKQw1VCNIeCHfKU8qMyQp3yp7ADu-2y4sIRIOqn1gL4U3SY0syvzLT3-SEReVFYb1WFFFDddFWfAXxnhSGbbnmTBDbG7DlHXWRdg_5JITx5_lqiSRFMaGPJW6m6EB2JINCKnD7yYEBWv1mnx0wQtQmyGgjXwOLa4UslhcH6N9IXEah5jxmMvQNuAQPphwFf35pD88Lt4ZfqNuWzpvxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید عیدی با خلق 4 موقعیت مسلم گلزنی خلاق ترین بازیکن پرسپولیس در این بازی بود
🟧
یک پاس گل به علیپور
🟧
یک ارسال دقیق برای جلالی
🟧
یک ارسال دقیق قبل از گل مملی
🟧
یک پاس پشت دفاع تک به تک برای علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138659" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138658">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
یکی‌ از خبرنگاران نزدیک به باشگاه الوحده مدعی شده که محمد قربانی با عقد قراردادی سه ساله به یک تیم ایرانی پیوسته.
⏺
اما اسمی از تیم مقصد نبرده و گفته این قرارداد به زودی رسمی میشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138658" target="_blank">📅 13:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138657">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
پنج بازیکن برتر پرسپولیس در بازی دیشب :
⏺
علی علیپور 8.45
⏺
ایگور سرگیف 7.83
⏺
محمد خدابنده لو 7.72
⏺
پویا پورعلی 7.68
⏺
محمد مهدی محبی 7.41
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138657" target="_blank">📅 13:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138656">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
فووووووووری
🔄
🔄
شنیده میشه حسین ابرقویی مجددا درخواست جدایی داده و گفته میخواد جایی باشه شانس ملی پوش شدن داشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138656" target="_blank">📅 13:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138655">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
✔️
پنج بازیکن برتر پرسپولیس در بازی دیشب :
⏺
علی علیپور 8.45
⏺
ایگور سرگیف 7.83
⏺
محمد خدابنده لو 7.72
⏺
پویا پورعلی 7.68
⏺
محمد مهدی محبی 7.41
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138655" target="_blank">📅 13:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138654">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyZ4A_77joQAZD41UJELiEFDnlOTgSD1WUaI9TEsN2nsbqjrNVVCiGxrTATxPXcQOsjdzirhBLXUz8Vv6H4ccIFPMGkyh8UHx7lAaYGdEgzNNXiThD8J7Y6otna7xX9jRlJgk3aeRSWuc0qAPR1FmFFs2HU1cOCebGtp5_D5jt37ayq4GynYkpG8sFtqFtaAn--HBoWDxLPsphxqE6QAoL6M0v5JXnr3KS7QefupUcfJamwCk4-bPmTW6HS5OiQYrcf0-d__kJbS44A3m_5zveuEx8KlRX_Lblt9RxYqYb2uzyJ0u6gnpuyz9Xmt0Mo8WFNUZsI6x9zzzlEq5oLGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
️ بونوس اختصاصی چرخش رایگان بازی Scarap Temple
💰
کاربران اسپورت نود می‌توانند از همین حالا، با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138654" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138653">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
⭕️
⭕️
😰
😰
شانس
🚨
🇮🇷
🇸🇦
رسمی؛ استقلال و تراکتور با خوش شانسی تمام به تیم‌های عربستانی نخوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/138653" target="_blank">📅 12:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138652">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
✔️
عبدی: بیفوما اگرچه فصل گذشته فصل خوبی را پشت سر نگذاشت، اما در فصل جاری از نظر کیفیت فوتبال و میزان ازخودگذشتگی، من را شگفت‌زده کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138652" target="_blank">📅 12:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
تیکدری
✔️
شه‍رآبادی
✔️
بیفوما
✔️
محمودی
✔️
اورونوف
✔️
همایی فر
✔️
سلمانی
✔️
باکیچ
✔️
لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138651" target="_blank">📅 12:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138650">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5M-g4IZ1yD5qfNFEJYIKT0AkoCLrhg8P2HT2o3PVy67jMNQ6YddEh4us1lQBcVIh3raDoa54x24AZAIJmNTdtlBNqkRFA4hNl02iNE-YWtRdP9U_1WcQRAXZJmvF9VQXK3G1aSNQbIEpGAIih6x4a0n2j5zHMso57AjoG7fWiDXwNT7Fs-teRVxPVwnMRrZxgL3NjRNjtKYTmnoYutLNHDoN0OaebIKXi7xOVRuXCvfbt_YnpyZ-UogE43z8Zoah_zS02t_5ESIkinvlyxVukTu8xrSL0GKOKOVsFqxeYwB-XX0ZXjeQ2Z2YNjZhMiFrc-4b4iKu2ioLZ_qui8TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
❤️
برخلاف برخی شایعات مطرح‌شده، اوستون اورونوف در جشن پیروزی کنار هواداران حضور داشت و در شادی آن‌ها سهیم شد؛ او پس از پایان جشن، راهی رختکن شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138650" target="_blank">📅 10:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138649">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWDOB0-OaVjIEf-8_4jV5bDCyJRCjRvrKUYaNJ_Y7roDOsVkIahczVJ7mrL8auLSBjq2sWVOQ1lnrww-uTepJi6_b6ey87zrReS6yoqs-kRnrRy4BVV97k23uLsDcfXstWqQ5IBEIaK5qM37IPqWt3msKfKC94swrLRpXNNyVq-OFIpfZPknywRmsYtve8UjRudy_fdEAD_WFV2TGJFy5W9xRytBj7fhiApuAVn0o31fDKlJX_Xz1CiCK7EI9z5ull5QENYMmRx7XKcE-iA0cQM8wcD40GIAZUclxnAWOD8d2RX20bCzm2inZl-M_3sVE2D4JsPCYSAFlpQdsUJ9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
هفته‌سوم لیگ‌برتر فوتبال
✔️
پرسپولیس
🆚
تراکتور
✔️
🗓
تاریخ دوشنبه ۲ شهریور
⏰
ساعت ۱۸:۳۰
🏟
میزبان ورزشگاه تبریز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138649" target="_blank">📅 10:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138648" target="_blank">📅 10:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138647">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
علی علیپور با دو پاس گل و یک گل بهترین بازیکن بازی امشب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138647" target="_blank">📅 09:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhsiyEEBKstvgTJytQNBFxtekcUgh4jXEiAZwiLPKNf9BVhQ8J3PpSTdDQjLeA1nT9GkLsYJ7iDKFXmepgyp3ZM3o08Ns4yCz6Cnik3K2A1XfF01-jAKk1ZGf0vQgZ3w66HGHCa8D1If3YQONGKDxw0i9FXf3eH_tkd15k4tTMuqTqsWO2Dir0rk8bqhYwF90GsevsbBLrueIJJHFk56aS0tBjIuHISsYLj3rMc5OnE-exBksd3QQU4oQJAEJHe3BLIvPcGMNxpivhxCp08issgM1HjVnBwmGIlC0rHO0OVOFbgdtrRXzPSv8CQgJZAve_t77y1gEu-KFP3eesn2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارک کلاتنبرگ: گل استقلال خوزستان به پرسپولیس صددرصد آفساید بود چون مهاجم جلوی دفع توپ مدافع از روی خط رو گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138646" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
حسن اکرمی داور بازی پرسپولیس و استقلال خوزستان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138645" target="_blank">📅 09:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3h5WN7vmQP6qVZVN34bvp1msjW6oy6qAQf1dQ2ZcZrtw3o9-yNcDbjqS52Gxu2eangPLaCpH_eNVuMkZ_Jm-nQMPo1ceF_rCg4j7ohXBejumvkyS10bvfFd82ZNbsOn20Uq3nrKetda2kz_U_vFTv7p1kay5CFbLRxERPLTQ3B36p17xrJ0aVhO2Cdnlcug5_B1KociF2WovUdJjQbLhahXjP7kAr4wvSScW4LO6iEdtRLW8ts080cQxoCJNS3yWa1I7u2teBjK8fJHl1DM_bHMB-3Wu2XfYAMq-M6uNT1h0e9SrS5_hfKr_taN8rE8nSN_ybgJqiuKpy-ZJFPLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر خط رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138644" target="_blank">📅 08:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138643" target="_blank">📅 08:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">➕
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
➕
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138642" target="_blank">📅 03:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8ef11ffd0a.mp4?token=khP_q4r4HvnbsrB-rXUkptGerqR741kcbD85IBUkaAWCgzf56wONjQW8XBkfuua--rRIXsSeFhi3XUQHOcGj69CjcT14JjHXkXNQr6j_zQbXyWsOq4x0mWQBaK-8d0UPhKhxTWSki6QhZo6V9Gj1lBe8YQbOLf3L0jFEsicsAvwGJMbuRrmXfMzGa19-mS-8y8ws3DH4__KYC76C5DmVA9xx5SE5gj_URjgFeyuCyyeXuztQ9MrU83UMOzPe0eOHtUjASGAES48adHVMyRdiC3PITnVoEXmFnkVVKGvi7UYDPV6EoGPtzVKkeD6uieoTGQmD79FHhgvyP0LRF-t36g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8ef11ffd0a.mp4?token=khP_q4r4HvnbsrB-rXUkptGerqR741kcbD85IBUkaAWCgzf56wONjQW8XBkfuua--rRIXsSeFhi3XUQHOcGj69CjcT14JjHXkXNQr6j_zQbXyWsOq4x0mWQBaK-8d0UPhKhxTWSki6QhZo6V9Gj1lBe8YQbOLf3L0jFEsicsAvwGJMbuRrmXfMzGa19-mS-8y8ws3DH4__KYC76C5DmVA9xx5SE5gj_URjgFeyuCyyeXuztQ9MrU83UMOzPe0eOHtUjASGAES48adHVMyRdiC3PITnVoEXmFnkVVKGvi7UYDPV6EoGPtzVKkeD6uieoTGQmD79FHhgvyP0LRF-t36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس در پایان بازی با نظافت سکوهای ورزشگاه، کار قابل تحسینی انجام دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138641" target="_blank">📅 00:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138640">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8nSaQ1Ym2Sp5k6XRINhj-y9Gu1tCDfwuyDwJiQrYFLx1Xomfa0662YMisiM7Nf-4MmuOPQBapKN0z2iDDQGDXTdJGZKB8VodCU3PARlMg26A9CApDC5tCTSv9yzm3vcFltg96GYO59l9zKUdZd7r7wRz-QzzFyq2njAQYg4nL94OcmQNIiTj__g05NhqE3xImGc8yt11K1rDmgx_YFslqI0ZmIRKUpLQgj6clPbvlLlelzyscwHc2NyHCS_tt1g7d84PjkMjsj4p7EDRAJXn9YoD46fbCwBBfISpZIDjh0lBFbz7sliTUBSnaCDrzDT_jS-s16QPtFxXMDTCgmquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💯
میانگین سنی بازیکنان تیم(ترکیب اصلی و تعویضی) در بازی امشب 27٫81 بوده!
✅
تیوی بیفوما با 34 سال مسن ترین و پوریا شهرآبادی با 20 سال سن جوان ترین بازیکن امشب پرسپولیس بودند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138640" target="_blank">📅 00:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
دردسر شیرین تارتار؛ ۴ مدافع برای ۲ جایگاه
‼️
⬇
⬇
⬇
با اضافه شدن دانیال ایری، تارتار حالا کنعانی، زارع، ابرقویی و ایری را برای قلب دفاع در اختیار دارد. زوج کنعانی و زارع در هفته اول خوب ظاهر شدند، اما حالا رقابت برای ترکیب اصلی جدی‌تر می‌شود؛ مخصوصاً با توجه…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138639" target="_blank">📅 00:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
#فووری
❌
طبق شنیده ها, حمیدرضا گرشاسبی برای صدور رضایت نامه ابوالفضل رزاق پور با مبلغ 120 میلیارد تومن رضایت داده و تنها موافقت حمید مطهری مانده تا این بازیکن پرسپولیسی شود
❌
❌
البته بعید است مطهری راضی شود مگر آنکه....
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138638" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obaJObN6O9l4siGSPfGcBBelJJwPxK5bKPQYIETVp16MVSr_dHPsd4n0ET1SadkCiUv3R2q87oYIiqRQNfgcNooFKOVp38G3v95FeIhIQkXE7-9ShQG0NvVnR-ecC_LZQdqj8q_BOkJ3PI4K6AZkxWmuz64D_Hxi9zTOveYOyAyDBPsMcWalwixDiFGwnETNKXDs9smsV8iInNf_vd5YMrL2-79oCkWQvz9i0HI1om6djBsrrmAqHmzhGNPak8yV5L4o4M85JxH7Dz57f-E0-hGyjJUx3gU_198Qyo5oLImV3f4suVNr-qoHTxQ8lQrw-_JO3wuHPB3YXnYTFkRrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صحنه‌ای که کرک و پر ابوالفضل جلالی از پرش محمدمهدی زارع بعداز گل محمد خدا بنده‌لو ریخت
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138637" target="_blank">📅 00:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
📱
استوری محمودی کنار بیفوما  بیفوما: عشق منی محموش ؛ فدا بازی
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138636" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384e0a5eb3.mp4?token=iKTUEE92VLdKZ6nRVECQDYVrWoie6gVMQmZa50Y3shhUp7j4epSxL3bxF95FBnMUHkY-QqR07YHg_EdhChyrgx2HbZYU2kmW6NDDFgaCSpU1nD7VNsoSmF65Kt6sb8SW43BCfkpGRbugC4elfFdjYLtq2yzCOF2l25dolwYcRRQoDauAuKIjRPi4dqQcyzQRIAggTAlEuemZ_ghB1F8JT3a0eABJPADlhY77-b7MljEyFZPxWmC9SxWqF5xK57-MCS2J95_i4WJNOFgiEmo3Ejgt0V8yOM76Q2TSPJAf6xqmy_N7FoEONOrFDPUb3y5w6UMfwzhbHsfaN_9-BmOnCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384e0a5eb3.mp4?token=iKTUEE92VLdKZ6nRVECQDYVrWoie6gVMQmZa50Y3shhUp7j4epSxL3bxF95FBnMUHkY-QqR07YHg_EdhChyrgx2HbZYU2kmW6NDDFgaCSpU1nD7VNsoSmF65Kt6sb8SW43BCfkpGRbugC4elfFdjYLtq2yzCOF2l25dolwYcRRQoDauAuKIjRPi4dqQcyzQRIAggTAlEuemZ_ghB1F8JT3a0eABJPADlhY77-b7MljEyFZPxWmC9SxWqF5xK57-MCS2J95_i4WJNOFgiEmo3Ejgt0V8yOM76Q2TSPJAf6xqmy_N7FoEONOrFDPUb3y5w6UMfwzhbHsfaN_9-BmOnCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📱
استوری محمودی کنار بیفوما
بیفوما: عشق منی محموش ؛ فدا بازی
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138635" target="_blank">📅 00:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
در یک پست باید تقویت شویم
❌
از مدیریت باشگاه تشکر می کنم و از آنها می خواهم در پستی که مشکل داریم بازیکن جذب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138634" target="_blank">📅 00:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2_larp7NVrw9lUiUCwce6CAOVi5eDQYNZwz6d_QEBVhloGuNbZjmycTr4GZIvHC1SegqXdwCHA_j12dFFgtUxEDv4vmUe8YGCzffcdFqrDVWS-PcXMbi4hWyv3TBuVU1rt-NURtaTIhU3DvJWuDXthiE1F_dUh1PecG0Hy6h44jL9_lxrqzSbUZSC2e4pHNbizui77WL_P_wxV4COV15rGgmjYVnpBUaWQ2BNzHo7dw8eddJ9uoPFVWOVBVrNL9ZzMBSEDKlGyQH2Vx69AomK1DRAV_yveKOB21soaJtkcxx5DQouWLIH9kGSyQdyM2hZKaEIQh4CJT2zyMzTaPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور با دو پاس گل و یک گل بهترین بازیکن بازی امشب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138633" target="_blank">📅 23:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGUudjYerSBuYbcvFsa1uu97ma3EcoTNsdLFqWWaMa16u1H18n26sfhbXvQuOPYEPyxOKkAjSA6OBNqBbQqGfoIF8JFGzc-PZFdQGfGTVq-joK-v5zq3YVmotqhZ0EkvbqEW0L0xyx5tFYcLBfka97GLUcuIrQQTkKsDaguFHTntygfsPeJzJLwJlv1aHjBK6Ptw6jyrFgAa3tpNb-yDsPL3uHScLRjlkr3HApqysrGuBr03TdMw1f7S20nN-9sknpQMb8SGqQTP7Vdy092oTa1snGPjgzK1S3ubI-bQ1TIds_qV9xYFfE-xzbdOOPuI8Ou_nPRKq3Q2lbXsVn-4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
علی علیپور، مجید عیدی و ایگور سرگیف با نمرات 8.8، 8.4 و 8.0 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس
🆚
استقلال خوزستان بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138632" target="_blank">📅 23:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
بهترین بیفومای دو فصل اخیر بوده .عالی بودی پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138631" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
♦️
ممنوع المصاحبه ای بازیکنان؟ در این مورد من مطلع نیستم و باید بدانم ماجرا چیست. چنین چیزی با من هماهنگ نشده و این بحث مربوط به مدیر رسانه است.‌باید به هواداران تبریک بگویم و امروز سنگ تمام گذاشتند
♦️
اینکه نیمه اول در تایم زود…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138630" target="_blank">📅 23:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
تارتار: چون جلالی از قبل هم مصدومیت داشت، وقتی نتیجه ۲ بر صفر بود ترجیح دادیم ریسک نکنیم و او را تعویض کنیم.‌ما در پست او همایی‌فر را هم داریم که از جوانان خوب است اما نیاز داریم در این پست تقویت بشویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138629" target="_blank">📅 23:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b3360c20.mp4?token=vFmiERF2ZuRzJVrm33Fi3cUyXjyNxg_bs4flg5ZNWer1Mmqg2NpTsUBJVHbkvQQ0hXGj7qLzj4_0HQdj70uomtXu501y07METoecbT-Sed6IYsARCxWRk2EBltZ0skCeOlX6Q_8zt0oOP47ntmyDq6kzmNHUk3lJTa6edOqoFBSZJlw_nkGzxXsy_T1mUPkEFtYg2VObbhvueWGBzljx7peD4C_XvuJjgQv0ed4rXFnDBpAQB7Jo5aS1xcCaP-OyLeoSd7JjfBlFVqwmMHhe9w7_fPYWnd7ZUUQqDdLF-V89v2G8hEA2yvhhODZi4X048PeWmSoAYyna35geLy2lHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b3360c20.mp4?token=vFmiERF2ZuRzJVrm33Fi3cUyXjyNxg_bs4flg5ZNWer1Mmqg2NpTsUBJVHbkvQQ0hXGj7qLzj4_0HQdj70uomtXu501y07METoecbT-Sed6IYsARCxWRk2EBltZ0skCeOlX6Q_8zt0oOP47ntmyDq6kzmNHUk3lJTa6edOqoFBSZJlw_nkGzxXsy_T1mUPkEFtYg2VObbhvueWGBzljx7peD4C_XvuJjgQv0ed4rXFnDBpAQB7Jo5aS1xcCaP-OyLeoSd7JjfBlFVqwmMHhe9w7_fPYWnd7ZUUQqDdLF-V89v2G8hEA2yvhhODZi4X048PeWmSoAYyna35geLy2lHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
پوریاشهرآبادی؛مهاجم پرسپولیس:
🔻
امسال تیم یکدل است.
🔻
همه بچه‌ها جان خود را برای این لباس می گذارند.
🔻
تیم ما لیاقت قهرمانی دارد.
🔻
پوشیدن پیراهن پرسپولیس آرزوی هر بازیکنی است.
🔻
مهم نیست چه کسی گل می‌زند و مهم بردن تیم است.
🔻
بوسیدن لوگو؟!این عشق بچگی است.
🔻
رقابت در خط حمله نیست و رفاقت داریم.
🔻
تارتار پرسپولیس را متحول کرده است.
🔻
در مورد وضعیت تیم امید و باشگاه نمی دانم و آنها باید حل و فصل کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138628" target="_blank">📅 22:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb8538e6b.mp4?token=oghOdsYHDp9yQgYhTVg8JCaobYZ9uk1I-DcKtwvHTU35_qVIoNB7KPs4CVlf29vxlelO_B_AQNvyVAWRVDJKQB4oq8L5NXDomXJizPjpzWLjCHcX9Nu3jiCe41AZ7nWSfCVcXzJZNEKPYBUeLAdwKCDHoXZpFmgD0vtrFi5SQ0XTT8e6YOqO8qWmAomkC89vhiFN_VlSJH8Zu-I_F2X6nzuyhz90GGUriowOxSbTz-IfjR4BweUBDn9FiX6FLeL-mRsVRynEhdOIjOuQ7jSQqNUxidRrv14BT9fqPI2V51Tcuq1CiqN2rJ74AoIu4E7N1Qjq-qZ6SSFEgqbBpgE-Njfr7aXBDuguzX-oM3uCrhoaV0Ez9UjuwM8K5X2XFrZcfqwOx9qBq745H4ZxOimiidTu9TiUhipZAacueNvshKLBDYORx6gmDC-56xEJaISeJL6H6cAKyJL9imd9axYgDQPvP-tuqMZAmIq9GDkA2qxmjt8n8ngApDAY_yMhGiUdU8W5p4fi7E5BtVmqXmqDPIYRGVAlWiRN9BfYZ8OD1P3XEx_wdE73PASsGPem5lp71BZpOCz49ehsd-ncalH81FkXPzDMSqNdXwBhzYFfhDPmq-xD67WRtbyn1CyTeMNxIT73gMUUgaxD1YRyfels2mA8ZtYfYzP4Y4xpiLRoOyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb8538e6b.mp4?token=oghOdsYHDp9yQgYhTVg8JCaobYZ9uk1I-DcKtwvHTU35_qVIoNB7KPs4CVlf29vxlelO_B_AQNvyVAWRVDJKQB4oq8L5NXDomXJizPjpzWLjCHcX9Nu3jiCe41AZ7nWSfCVcXzJZNEKPYBUeLAdwKCDHoXZpFmgD0vtrFi5SQ0XTT8e6YOqO8qWmAomkC89vhiFN_VlSJH8Zu-I_F2X6nzuyhz90GGUriowOxSbTz-IfjR4BweUBDn9FiX6FLeL-mRsVRynEhdOIjOuQ7jSQqNUxidRrv14BT9fqPI2V51Tcuq1CiqN2rJ74AoIu4E7N1Qjq-qZ6SSFEgqbBpgE-Njfr7aXBDuguzX-oM3uCrhoaV0Ez9UjuwM8K5X2XFrZcfqwOx9qBq745H4ZxOimiidTu9TiUhipZAacueNvshKLBDYORx6gmDC-56xEJaISeJL6H6cAKyJL9imd9axYgDQPvP-tuqMZAmIq9GDkA2qxmjt8n8ngApDAY_yMhGiUdU8W5p4fi7E5BtVmqXmqDPIYRGVAlWiRN9BfYZ8OD1P3XEx_wdE73PASsGPem5lp71BZpOCz49ehsd-ncalH81FkXPzDMSqNdXwBhzYFfhDPmq-xD67WRtbyn1CyTeMNxIT73gMUUgaxD1YRyfels2mA8ZtYfYzP4Y4xpiLRoOyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
♦️
ممنوع المصاحبه ای بازیکنان؟ در این مورد من مطلع نیستم و باید بدانم ماجرا چیست. چنین چیزی با من هماهنگ نشده و این بحث مربوط به مدیر رسانه است.‌باید به هواداران تبریک بگویم و امروز سنگ تمام گذاشتند
♦️
اینکه نیمه اول در تایم زود به گل می رسند جای خوشحالی دارد. یک گلایه ای هم از داوری داریم که امروز تمرکز داور در 20 دقیقه آخر از بین رفته بود. خطای روی عیدی و توپی که به دست مدافع استقلال خوزستان خورد نیازمند دقت بیشتری بود. همه بازی های پرسپولیس سنگین است و داور باید دقت بیشتری داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138627" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0042859545.mp4?token=pP0jU2AtX0SSckKKh2a-C6PYMYzUr0DJVOqcvj6P6gGgrXKAr5vUB6snC_QCOAfuJbWV_G-lYliHqXRR6R4CkFo9BXANhwW3WdNQEY8QvS3Zq65zZ5cqqZTy1POg8KFU4aQXyppmRR7010FxM9AtFgYLyVsM6begnyl2CZ5MCVPXBo8-hQSR_xKdHi00MLR6jlFqPOXe6X2ffHy027sKURn6EMzr5NTFHMEOVEFZbN4yp3ZkrE-8I9ejQ0MI93PfwpY259SoYnx0-gFt80DnJAyx-DJ96bM7eZbAlToA494e-jkHNj49KEbtO4-QpVLRIydnid-n4xzLmbCGUxwnTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0042859545.mp4?token=pP0jU2AtX0SSckKKh2a-C6PYMYzUr0DJVOqcvj6P6gGgrXKAr5vUB6snC_QCOAfuJbWV_G-lYliHqXRR6R4CkFo9BXANhwW3WdNQEY8QvS3Zq65zZ5cqqZTy1POg8KFU4aQXyppmRR7010FxM9AtFgYLyVsM6begnyl2CZ5MCVPXBo8-hQSR_xKdHi00MLR6jlFqPOXe6X2ffHy027sKURn6EMzr5NTFHMEOVEFZbN4yp3ZkrE-8I9ejQ0MI93PfwpY259SoYnx0-gFt80DnJAyx-DJ96bM7eZbAlToA494e-jkHNj49KEbtO4-QpVLRIydnid-n4xzLmbCGUxwnTIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
محمد حسین کنعانی زادگان، کاپیتان پرسپولیس:
❌
❌
من به تک تک استقلال خوزستانی ها افتخار می کنم و بعد از بازی به رختکن آنها رفتم.‌بازی تراکتور و درخواست برای حضور تماشاگر؟ فعلا بگذارید این بازی را بگذرانیم و بعد کارهای لازم را انجام می دهیم
❌
❌
ناراحتی اورونوف؟ اصلا چنین چیزی نبود، در تیمی مثل پرسپولیس بازیکنی بازی نکند طبیعی است که ناراحت شود.‌هر چه آقای تارتار تصمیم بگیرد همان می شود و تابع هستیم. گلزن تیم فرق نمی کند، من دوست دارم تا آخر فصل گل نزنم اما پرسپولیس قهرمان شود.‌خوشحالی من حرکت موزون نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138626" target="_blank">📅 22:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpgfm97_eCa_rzl_ns-bADAXDiI5uwIhu7aSo1pmCSbuyU87M3BLXONYtkQx4igmJ7oeZWEYqEKvXpAlh5gVWhNgcRAyfQ9mtLEBASKva3DN_VULAz9xZ3FxU1gflDl0MPNaKJIXdj_1yK7Ggo0EZsEtyXVStFK-YTczWGbxXFi1h0rVZy0r4qHBLCEgSHuycTOiB278A1mwNu6Y5ELI-uiha4Am3RE20VB9PGO_UuNGuyCuHF9l_AzMx-q_vcxAncmV6ijYKZvI9G2dVJueHHOhEXq0oWhz1dwxAfO-Q3DCFqWfqoQEMlcDY4mHpukkDS0hqhJNu7OOFuexhmpp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول لیگ برتر پس از پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138625" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
مهدی تارتار، سرمربی پرسپولیس:
❌
گلی که خوردیم از شیرینی برد ما کم کرد
✔️
✔️
دوست دارم هم خط دفاع و هم گلرمان جزو بهترین ها باشند
✔️
✔️
از جلو خوب فشار به تیم ها وارد می کنیم
✔️
✔️
به جز نیازمند درون دروازه رفیعی را داریم که خوب کار می کند
✔️
✔️
دلم سوخت که…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138624" target="_blank">📅 22:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✖️
✖️
مهدی تارتار، سرمربی پرسپولیس: بازی با تراکتور و درخواست برای تماشاگر؟ فعلا می‌خواهیم امشب از برد خود لذت ببریم
❌
از داوری امروز توقع بیشتری داشتیم! در صحنه‌ای که علیپور به سرگیف پاس می‌دهد مدافع حریف توپ را با دست می‌گیرد!
❌
داور می‌توانست برای ما پنالتی…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138623" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یکی از نکات مهم اینه که فصلهای پیش جلوی تیمهای ته جدولی امتیاز از دست میدادیم</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/138622" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">یکی از نکات مهم اینه که فصلهای پیش جلوی تیمهای ته جدولی امتیاز از دست میدادیم</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138621" target="_blank">📅 22:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
✔️
✔️
هدف ما از اول این بوده همه بازی ها را ببریم. هواداران پرسپولیس این شکل بازی را دوست دارند. بر اساس فلسفه هوادار خواسته های خود را جلو می بریم.‌در یک پست باید تقویت شویم .از مدیریت باشگاه تشکر می کنم و از آنها می خواهم…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138620" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138618" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138617" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138616">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
تشویق بی امانه تارتار در استادیوم ..همگی دارن از این تیم هجومی و جذاب لذت میبرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138616" target="_blank">📅 22:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138615">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📌
به عقیده من تیم با خرید یکی دو بازیکن دیگه ۱۰۰٪ تکمیل میشه
❌
یه دفاع چپ و هافبک دفاعی… بنظرم میشه به همایی فرد اعتماد کرد چون دفاع چپ ایرانی تو مارکت نیست و اگرم بخایم خارجی بگیریم باید با دو تا از خارجی ها فسخ کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138615" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138614">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔖
⚽
به باد این دوتا برد نباید بخوابیم،عیار تیم تو بازی های بزرگ مشخص میشه، با دو تیم نسبتا ضعیف بازی داشتیم اما عالی بودیم اما هنوز برخی ضعف های تاکتیکی هست که باید رفته رفته برطرف بشه ولی از همه جهات این دو بازی عالی بودیم تمام بازیکنان مون عملکرد خوبی به نمایش…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138614" target="_blank">📅 22:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138613">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔖
⚽
به باد این دوتا برد نباید بخوابیم،عیار تیم تو بازی های بزرگ مشخص میشه، با دو تیم نسبتا ضعیف بازی داشتیم اما عالی بودیم اما هنوز برخی ضعف های تاکتیکی هست که باید رفته رفته برطرف بشه ولی از همه جهات این دو بازی عالی بودیم تمام بازیکنان مون عملکرد خوبی به نمایش گذاشتن
◀️
و به لطف باشگاه تیم خوب و سرحالی بسته شده، همه باید از تارتار و حدادی حمایت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138613" target="_blank">📅 22:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138612">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138612" target="_blank">📅 22:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138611">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138611" target="_blank">📅 22:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138610">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bca5c905.mp4?token=r10MzbI7DyMalJRXNuq2HshnHjFt3AZUwsSkL-ypqOHNkRUpb8HgrNcEfsiKP9wn6tGbEwu7Q0bI_zasXOLFCffR3VHpY3jU9z6CKME-ZsKKxc1sHmLKMqEUWaudaXdeR83K9lfVIZFbCps0Hog4dkEdGhlNOMYPtN_qXZyiTnNRwAaqAFoZvKQOqlkkN-LCsNhSXkaFSo7SeEOgYT5pYKNiL9_9WiZOAMH3fYe7jQjlvn_vYdevbPZdp-WfRVQgy4LaXi5XdOie4e93x6adC4Mi5pgY__ocuUPQU69sxYLu3FxJ0oMFfCh09CQrvn65gG0wQBBNL3fIIFK02n4--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bca5c905.mp4?token=r10MzbI7DyMalJRXNuq2HshnHjFt3AZUwsSkL-ypqOHNkRUpb8HgrNcEfsiKP9wn6tGbEwu7Q0bI_zasXOLFCffR3VHpY3jU9z6CKME-ZsKKxc1sHmLKMqEUWaudaXdeR83K9lfVIZFbCps0Hog4dkEdGhlNOMYPtN_qXZyiTnNRwAaqAFoZvKQOqlkkN-LCsNhSXkaFSo7SeEOgYT5pYKNiL9_9WiZOAMH3fYe7jQjlvn_vYdevbPZdp-WfRVQgy4LaXi5XdOie4e93x6adC4Mi5pgY__ocuUPQU69sxYLu3FxJ0oMFfCh09CQrvn65gG0wQBBNL3fIIFK02n4--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🎙
بهنام ابوالقاسمپور؛مدیرعامل استقلال خوزستان:‌
🔻
با حدادی در مورد بیفوما حرف زدم.
🔻
ما باید مبلغی به کمیته وضعیت می دادیم اما چون ندادیم نورشرق به نفع پرسپولیس رای داد.
🔻
الان پول رسیده و باشگاه پرسپولیس هم گفته مشکل را حل کنیم و دیگر کار به دادگاه عالی ورزش نرسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138610" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154eade970.mp4?token=sNI6Yw9RjAdeNZ8X-4mRKQRJUN98CBMMaK7g6jzmaiLlWobwuCcCEe68sZB9-s1SvL75y2dUVTUPtyxBFAaV2BUIBqO_hST75BDsDKgZLHYXs1n2pePwJoANerfWuG_OOUAhuHNKXsePkyr4odlFB9xKeXA_2jkhFO8XjdwOG8JnPyiMf8cM2E-23d0uBsMUA7KQbqFuR0-kFcjxzmD0TwwNxC9NjkWtM4j0J6LvfsJoVucZ2QJSxDxKVj4kMumpYyEcZTIE23W6qUtwt6eTyOGODOV8ueGYb4cCKo_TS0UpzuqqkffcTONdtxaCrjRJVon01vMksbNysVlCCl0TfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154eade970.mp4?token=sNI6Yw9RjAdeNZ8X-4mRKQRJUN98CBMMaK7g6jzmaiLlWobwuCcCEe68sZB9-s1SvL75y2dUVTUPtyxBFAaV2BUIBqO_hST75BDsDKgZLHYXs1n2pePwJoANerfWuG_OOUAhuHNKXsePkyr4odlFB9xKeXA_2jkhFO8XjdwOG8JnPyiMf8cM2E-23d0uBsMUA7KQbqFuR0-kFcjxzmD0TwwNxC9NjkWtM4j0J6LvfsJoVucZ2QJSxDxKVj4kMumpYyEcZTIE23W6qUtwt6eTyOGODOV8ueGYb4cCKo_TS0UpzuqqkffcTONdtxaCrjRJVon01vMksbNysVlCCl0TfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
شادی هواداران پرسپولیس و اعضای این تیم پس از سوت پایان بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138609" target="_blank">📅 22:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c286dc680.mp4?token=tB2EdexXILO99QrpyMh_9b4RdedkM7S6HloRALuXPEKUnPVp0sKb7vLOttzBtZxeoDotVg8Kl7R21l2hCC0jXAaQpq9vNcLptDSJm9KiQoPK9wBwL2i0gVjbtb2Fiw3XGXmaKlFZ22qrLH4xLViLMWzezfsqGg_wmVxFks8pUzLqnQUklnYi90X9Zl6qermW24KSB4CyDwlf8ENhaXohqZ_5NBa4ApRu5sNmAM-VMqPLwVLzynpwiQVZgaot2emQpChykXs2zRqSWzOBHniVQwCA8PgOV1-lmvN76NwtcSeiVjNGgwUxOCukcpNmr0r3gLZXxs2Q_FvnArPL43NaRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c286dc680.mp4?token=tB2EdexXILO99QrpyMh_9b4RdedkM7S6HloRALuXPEKUnPVp0sKb7vLOttzBtZxeoDotVg8Kl7R21l2hCC0jXAaQpq9vNcLptDSJm9KiQoPK9wBwL2i0gVjbtb2Fiw3XGXmaKlFZ22qrLH4xLViLMWzezfsqGg_wmVxFks8pUzLqnQUklnYi90X9Zl6qermW24KSB4CyDwlf8ENhaXohqZ_5NBa4ApRu5sNmAM-VMqPLwVLzynpwiQVZgaot2emQpChykXs2zRqSWzOBHniVQwCA8PgOV1-lmvN76NwtcSeiVjNGgwUxOCukcpNmr0r3gLZXxs2Q_FvnArPL43NaRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
گل چهارم پرسپولیس به استقلال خوزستان توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138608" target="_blank">📅 22:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f62d7868.mp4?token=Auh1WYukH77OYaaetZDIOYEQsBO4ZgZGsWl9_1zPp597Z6hsKex2iBqPjk8ZuIgXE4xX85pbMZK7z82ide1U7AwCC_TRN6jMBAGe9op1r2CVpUYOmcsobMWneFkX_6vlA3jgLjOtZNO3HhYSYygPzj-BJXfYSXNb7fhKtYiE6r6cN8ApBjFV-tlOd2dJGQSkMAx4imFP-nCk3yv6GZHYvKJkQ6VFlmCMHH0Qdbd9m922QgGtWIFqlZ5H3GTzoLobi66L278kdZnxFX-oU62ZOSZzkiqm0ExgH22BTBgUfJrmttoRcZTAs2K_9YtYAAqZ9D4_oreQ7wDpsAN2XjIKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f62d7868.mp4?token=Auh1WYukH77OYaaetZDIOYEQsBO4ZgZGsWl9_1zPp597Z6hsKex2iBqPjk8ZuIgXE4xX85pbMZK7z82ide1U7AwCC_TRN6jMBAGe9op1r2CVpUYOmcsobMWneFkX_6vlA3jgLjOtZNO3HhYSYygPzj-BJXfYSXNb7fhKtYiE6r6cN8ApBjFV-tlOd2dJGQSkMAx4imFP-nCk3yv6GZHYvKJkQ6VFlmCMHH0Qdbd9m922QgGtWIFqlZ5H3GTzoLobi66L278kdZnxFX-oU62ZOSZzkiqm0ExgH22BTBgUfJrmttoRcZTAs2K_9YtYAAqZ9D4_oreQ7wDpsAN2XjIKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
❤️
گل سوم پرسپولیس به استقلال خوزستان توسط ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138607" target="_blank">📅 22:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6f4fb205d.mp4?token=ZT5yHmMY_ISOIUMx15OHGxHloNQMkriQL0iCGnyQIJdNopofh40s0VvewEUa9TWRJL2763nkNFG-EBNBXpdQF2rCMt3svrGT5p71KqltA4lfh6EV1DiLscd4IG96Ao--ehqsyJxCkcT32A7anjuHOdygQAURFa4U2tk5l8hMUuC_3nbzcq7arMsR9RBYtLbj9F1bJLgTt4NcnXxO3QOtAazH0RFx_IOsvksBhMfamniaJv3kAtbSpjLJpVunO6qL_xeZ9b00ZLiAz-PTv9TTLko4sSiQr1VsnrflR_KJr-3HpFXoLfk67DkMil4ufVYEv0mu4PnanXPPwut0Bdhzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6f4fb205d.mp4?token=ZT5yHmMY_ISOIUMx15OHGxHloNQMkriQL0iCGnyQIJdNopofh40s0VvewEUa9TWRJL2763nkNFG-EBNBXpdQF2rCMt3svrGT5p71KqltA4lfh6EV1DiLscd4IG96Ao--ehqsyJxCkcT32A7anjuHOdygQAURFa4U2tk5l8hMUuC_3nbzcq7arMsR9RBYtLbj9F1bJLgTt4NcnXxO3QOtAazH0RFx_IOsvksBhMfamniaJv3kAtbSpjLJpVunO6qL_xeZ9b00ZLiAz-PTv9TTLko4sSiQr1VsnrflR_KJr-3HpFXoLfk67DkMil4ufVYEv0mu4PnanXPPwut0Bdhzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل دوم پرسپولیس به استقلال خوزستان توسط علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138606" target="_blank">📅 21:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fbb512d19.mp4?token=ayDW272Oy7o5U2deFcFeYFgAADu7Mg6cp9zg3EakThE0dVB-Z1kj2dGh2SN1kbfRqqDEmbfQhj-0Q0OLFpQLPnj7OAr4V9Q2C1xPgOlJfk9SJo-AGtnE2sSY_w49vZTcqjILp7VstPk0dPS62YzcptH-hp5AOXm3JkWiFqjS4k3rpO_jTZvXU7gsW5sa069hhbdBq7XDldzeo1sB1rzacEmJ4ThFt0V6ponFQYgmsvmq7jCxMC2BAswMOpAnvU8ody4T7kZ08JZKvf9IE-pI2BPCgToMOY4uP6EiaYOdPP2HC1eva5eYHhtGHjeuf4F4uO5u9bL9gB77iUg7_KcOwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fbb512d19.mp4?token=ayDW272Oy7o5U2deFcFeYFgAADu7Mg6cp9zg3EakThE0dVB-Z1kj2dGh2SN1kbfRqqDEmbfQhj-0Q0OLFpQLPnj7OAr4V9Q2C1xPgOlJfk9SJo-AGtnE2sSY_w49vZTcqjILp7VstPk0dPS62YzcptH-hp5AOXm3JkWiFqjS4k3rpO_jTZvXU7gsW5sa069hhbdBq7XDldzeo1sB1rzacEmJ4ThFt0V6ponFQYgmsvmq7jCxMC2BAswMOpAnvU8ody4T7kZ08JZKvf9IE-pI2BPCgToMOY4uP6EiaYOdPP2HC1eva5eYHhtGHjeuf4F4uO5u9bL9gB77iUg7_KcOwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل اول پرسپولیس به استقلال خوزستان توسط محمد خدابنده‌لو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138605" target="_blank">📅 21:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚫
خطا روی باکیچ و بیفوما نگرفت به هردو کارت زرد داد مادر به خطا
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138604" target="_blank">📅 21:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
👤
تعویض ها مهدی تارتار مقابل استقلال خوزستان
🔴
۱- همایی فرد: عملکرد قابل قبول
🔴
۲- بیفوما: یک پاس گل و عملکرد خوب در جریان بازی
🔴
۳- ارونوف: عملکرد خوب در جریان بازی
🔴
۴- شهرآبادی: یک گل و عملکرد در طول بازی قابل قبول
🔴
۵- باکیچ: اثر گذاری روی گل چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138603" target="_blank">📅 21:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_jUFQ0NV08XUebDmH7DzLF0akMR805Pnoe3qS1xQcO9naueuD_eBdgSWoowTKjtqR_wCzvHS2GoBGr5V5-lKIXN265tkLT-T79S3RzeRBEKpLZQME4M6Cior4Q2GrmJMb5-o8QCxYpMBAkEZoi__Yovhimheo_XhsmZth8OQ5-P3R2AXYd-_sCFw07CIDTBys0s6A1s_o5cFal0ACCfCumAT4A-sj1Lye1dO_JZHhC1sq9fqP8DJOkqpdJW2EqDFhOd65FaSCXwnsL8IdmQDTB1Uhrp_-VvSqQoec9ey8BhU0cPq2dufucK5g3KAZ5_l7WGmy5GvVt9vVLKDIb-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
علی علیپور، مجید عیدی و ایگور سرگیف با نمرات 8.8، 8.4 و 8.0 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس
🆚
استقلال خوزستان بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138602" target="_blank">📅 21:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138601" target="_blank">📅 21:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkSZ-GhhEecwuwzNi4c5CVylEFp2cipg2sVK0cINRfBQ4iuBzOQxIMZsl2kRxjeyxuFkLwUZJNqww6LFlrERMi8vjOVIRBbbNBiS0tXrCvGyvQr2KIbmgoANu-pSOmcdvocQhfQIO0d2Dc4uwbpkfSX0HQkMpZEOsVPmryM-Pxh62LWuyoAUW_G7IZAYOapqd2-RrgC4h_JM2ybTdOCYfEeS3Kuz8YAP74iVKtt91bDO352xsueo2b05yj5INHjZ2roKVdz2Dd5Yc6pPj4gTao2emlmRhk7VIk3ox1UJ20CkP9wtqSB33PF-ANkJ5rsGnLDlP97Tla-xxf2Z7rif6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
صعود به صدر جدول با چاشنی گلزنی تمام مهاجمان/پای علیپور، سرگیف و شهرآبادی هم به گلزنی باز شد
❌
پرسپولیس 4
❌
استقلال خوزستان 1
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138600" target="_blank">📅 21:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
مبارکه با چهار گل بردیم ..دو بازی شش گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138599" target="_blank">📅 21:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138598">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚫
داور حروم زاده ریدم پس کله پدر جاکشت اکرم حروم زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138598" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
گل چهارم هم زدیم توسط شهر آبادی 19 ساله و با زدن گل بالا رفتیم صدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138597" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚫
داور حروم زاده ریدم پس کله پدر جاکشت اکرم حروم زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138596" target="_blank">📅 21:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
پای جلالی خوب نشده بود و دوباره گرفت و تعویض شد و جاش همایی فرد جوون اومد داخل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138595" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
گل چهارم هم زدیم توسط شهر آبادی 19 ساله و با زدن گل بالا رفتیم صدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138594" target="_blank">📅 21:29 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
