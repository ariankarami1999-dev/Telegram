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
<img src="https://cdn4.telesco.pe/file/FBMilpdKStYOPJKEZBob9hArFyw4wKXQ-hk_zLhS4vGwPieZVJmwQQI7TNdazBFd3_0qIFKAAQdRCY1ztiazVFYKANscflFJvdLAMs8UD4wOt-NnLUdHCcl8Ib81SpKAzCuqK_A5aRoxDuoA0Lh647Lb_ZaYN9-Fo1JpBI29tA3hBWa0GQbOgVSzZHybV5UjoYjAE29Mdrv1-YasyamaZ6cUO_WgkQVvnQye-rk3vGdoOYmc7jDBigIjMJuecpK9Rkz4jeGepOe7oYsC-IFiaUiTAJBIfvP4iVECLng5Wf3APp5L2Pl4GO6AGWd3UYr2g5OY1JDAvOBj52e0EVvfzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiLxFEFQsDM6vmqXJJtlppXLcu7WpG0XnJQIRowRzWBg_zhdhf2ewYwZF1EBDd7narzuxwbPLFXDaF06aY1bco15JnkROh7k08_VU24M2OjLo2QPR0NE0rgsGx27ZbyvzqI1VSgBVA4kbxCpnU6oWxtNVGesU9ndjm8J6u7-uyGIBgw0X4DhllIv0lySzTdZQJ0u--1ecicI1OTH7QT7x2W-tovtsHzm6jLss8hcbjRL5ZNJYiyJm7hDzOjSYh7xscsJWD92YsZi4guIrnzEpZFNHRl-USku_QecEEDu6Tdu7Jxma23GzHs8HNEQFKm39egB00sf63cQQ1aYTlL-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جدال نزدیک و نفس‌گیر؛ برست و پاریس برای یک برد ارزشمند امشب به میدان می‌روند!
[
برست
🔴
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
بازی برای هر دو تیم از نظر امتیازی مهم است و انتظار می‌رود محتاطانه شروع شود. پاریس روی مالکیت و کیفیت هجومی حساب می‌کند، اما برست در انتقال‌ها می‌تواند خطرناک باشد. با توجه به سبک دو تیم، تقابل نزدیک و کم‌فاصله‌ای می‌تواند شکل بگیرد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/140002" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/140001" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7Ay1EFRy3zPFIbg0Kae2WnwuVUkMYZRAUkXMtoOe_DsuuoBnrZKRhtJkitj3EGopDJlKgC4i2eEeATqrcgCgbwwNsjVBVsVNxzKFjmcwIzv46bGJlA7x8XvTMskwA8B7fGRpy8n3DXOtP96pu47O4IbSU4aNYJslwwQOSiScfpLh3xfH17iHIZX2_J7DPpb3Um7qzG45_BTqWxZ4e58hPXmjSqJYr0BiCtlerJ3jdmUKxuOcHbfRC5_Lm9y9_5qH4cwxztMs_1QtGgmB8FdT9-9whBkPNXnqvmC8xg2yslQUa0-db6tRvjA3evHI4MqCEYnCFFWOkP8ye5vAiQ8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
بیرانوند سرباز شد
😂
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/140000" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/139999" target="_blank">📅 18:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=rzS611M0to6f0_bzUzNZr8KNSKoWqUvCVmEBx1yrKagDMKL09xGSetgEIayg27XbUusgzAS2MN2bIYiURK_yrc3foGli-8qrt4hY4OrQkt1eww3FVD63J1Z_-ySoL-1ZHG-whviQT4Ym09LY2lf0EyEf0Ktj2m-Kknyd5-9W99oQy9L5six4HkHeBtZ35S7sHOAO4eJtoWjah5Hkjkqh4qEbatnAWuva4B0TBlwO6Vwcv6E8P3G7HrCvgAS256KX7WuyT7I7viRC2j0KKLN-eHk-SlMAeWu4933hgakzsYRmgk4R2Q2pbbUHdTNEFtdvA3Pjbf5ajiLeEK7TNT9OM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=rzS611M0to6f0_bzUzNZr8KNSKoWqUvCVmEBx1yrKagDMKL09xGSetgEIayg27XbUusgzAS2MN2bIYiURK_yrc3foGli-8qrt4hY4OrQkt1eww3FVD63J1Z_-ySoL-1ZHG-whviQT4Ym09LY2lf0EyEf0Ktj2m-Kknyd5-9W99oQy9L5six4HkHeBtZ35S7sHOAO4eJtoWjah5Hkjkqh4qEbatnAWuva4B0TBlwO6Vwcv6E8P3G7HrCvgAS256KX7WuyT7I7viRC2j0KKLN-eHk-SlMAeWu4933hgakzsYRmgk4R2Q2pbbUHdTNEFtdvA3Pjbf5ajiLeEK7TNT9OM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/139998" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139997">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/139997" target="_blank">📅 18:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/139996" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/139995" target="_blank">📅 18:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEuNiuf0hmzUHTEioq2phNcG1n_etIeux5RcihFGwLMJTiJM1ZCNaui8c4J7ZlsfgCOvmAo5eYE_guAe906rVlCK3iMlT1SyKsGUCYyt_9_qYHa6FESwQLMRxXCpRMmRvrwuIP-l5TDIZjLEcrAd00amMKYPWMn97nbSvunJk3spzXWY88MEjZDhNvquD5YjVeAQiyGMaX6AzgNmzLFyWGDUYrjcz-pRvZvD6kHqXiMOb5pxNumQYjHP_5FIURfQbxS-ON1uiT7IUhLhmO0NDeZLnfrFNi01Fl9vwqao1fHRHRkaKFrzUr6E4gaZ9UPJyHHCkjP1qSkb_WekPl2xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/139994" target="_blank">📅 18:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/139993" target="_blank">📅 16:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
حضور هانی نوروزی پسر زنده یاد هادی نوروزی، کاپیتان فقید پرسپولیس در تمرین تیم دهه شصت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/139992" target="_blank">📅 16:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فارس: محسن نامجو با هماهنگی به ایران برگشت، احتمالا شادمهر عقیلی هم به کشور برمیگرده و حتی کنسرت هم میذاره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/139991" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/139990" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
دو ست و فعلا باختیم و واقعا زورمون به ژاپن نمی‌رسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/139989" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
میثاقی:
✔️
مهرداد محمدی یه چیزی گفت شش ماه محروم شد اما خداداد چهار ماه؛ ساکت الهامی هم شش ماه محروم شد!
✔️
یکی از دوستان حقوقی گفت شکایت قضایی این موضوع چهار ماه زندان دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139988" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbQtEELfoHwhHj3EzMlnhxcGTp3xgnNj-CGIRLhWseRXK6Nuxe_Ak9BiWqytTeLqfCjA-ao9k8ca56WTX8dcda4Yz-ILLKaD92DQJEiO-zpkNtCNdzhDpQFbvAT8EyCM5I3fDZ8kSuJa73Jdh0XBJ84smqVSYM_UUTuNRh9WHHTAYSTvnwNJBC2RegckRQzty1uMcmI40sJAEU-6TdclyrN1fGKca9TLYmMMYTVlIdWv909kzfVC0B9H1_X0jWlLuZ6to5VcX8bOO8-ghXX9VAvZ-N-eDlJDSPOWWcZ7jV3rswEsdnnxdLABN0u6omT-2eYMCkmSRiyo1sHD758AhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پس از آنکه محسن خلیلی در ابتدا اعلام کرد: «جام حذفی برگزار نشود بهتر است»، حالا پیمان حدادی برای چندمین بار خواهان برگزاری این مسابقات شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/139987" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/139986" target="_blank">📅 15:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/139985" target="_blank">📅 14:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139984" target="_blank">📅 14:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEqt8DRkWyF9YQTOpXcRVmwb2Cz_fnUzvw1N-Z8zMmUHnWn0qhLtO5rwM-iC0819iquCRLGeYPxi9nNx_F7P4lrp_YCOE2TyKMBawAfOHbSyj4E7sKMLh0KAmchBfqcJISFVU28fbj7QhHEMNjpPjOBoNkMPj7o7-ug8n2RhlRB-DzLnI3slYCRHOknIz1RMr03Fqf6s8X_nvomTfDdi1KKfDWfdcgqtiRSn3-Ipe_aLC1UGiyrestjeecIYbmKwFVnz1HlmgbSnjn1MBmT28aI8W0wcGV_FHPj_cY6tQVUziO8K-RWOAg8uiWRXhAechq67150bgkNR-23iu7JL-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Man United -
🔵
Man City
⏰
Tonight 19:00
🏟
Old Trafford
🟣
منچستریونایتد در اولدترافورد با تکیه بر انرژی هواداران و ضدحملات می‌تواند سیتی را به دردسر بیندازد، اما ضعف دفاعی‌اش نگرانی اصلی است.
سیتی با شروع قدرتمند فصل و خط حمله آماده، کنترل میانه میدان و فشار روی دفاع یونایتد را هدف می‌گیرد؛ دیداری که پتانسیل گل‌دار شدن دارد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/139983" target="_blank">📅 12:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139982">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139982" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">💢
💢
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139981" target="_blank">📅 11:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139980" target="_blank">📅 11:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=F1kNAYwwSjZbeVOe8hB69cnxqcRPQ75B0-7a_akMqH8MV_4SkI-i0qd_SOuLWroLz2TKfPOdRT7h-f6NmRiSHwVe3-OAME9X1ckt95afBe25OolKCCYRyYrsOgNIeI-T93xIdr2v7uQcbylCHr3mJ619ajWU3vO-yk-6-_cCQKX2Wq0xevyI5iBHytEwfrfDVikHfDM71uvueglpFw-vIlcmBG2IP-8Hug2kqDqePDly2phbqISm66HuPnf4wReTlXGu3XS2VorDQAQWjlcv6Vep8nYoJIw2jM0iI9lpbDbbx0354LiZzKKKF60y03uPtFlCmOXY1Q5dDv2kiPjZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=F1kNAYwwSjZbeVOe8hB69cnxqcRPQ75B0-7a_akMqH8MV_4SkI-i0qd_SOuLWroLz2TKfPOdRT7h-f6NmRiSHwVe3-OAME9X1ckt95afBe25OolKCCYRyYrsOgNIeI-T93xIdr2v7uQcbylCHr3mJ619ajWU3vO-yk-6-_cCQKX2Wq0xevyI5iBHytEwfrfDVikHfDM71uvueglpFw-vIlcmBG2IP-8Hug2kqDqePDly2phbqISm66HuPnf4wReTlXGu3XS2VorDQAQWjlcv6Vep8nYoJIw2jM0iI9lpbDbbx0354LiZzKKKF60y03uPtFlCmOXY1Q5dDv2kiPjZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139979" target="_blank">📅 10:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA-RQEBXYU4ZdiyQEufujIxwLIkupph08DAR8lyrMt9AwUwa2OYiadZ3Pq1EWtSYizprLo4IRAdB5jMQ0dP_1PmopJDFf6AL9MxTfMVWr3aCHP1OkVdC1gbq41tL3MdsxwVFWDzyGP1WmFF-PsOtyfcWlLX1DJzV5X6I5wr8ioEIWx1td5J0Li61YJvq2ABsIh6yLNhSywsEX7xKyGvXQ2e6rgz3juIjy2UDlBI8W1tzQT9ah9qHnmljM1dqBeboAN_t901I1O46eQox5T6zHXD1bNuUBAmDdOzxud9eFfH0uypNXmaupi5ByGIEbcynAZW1bJzTWgiUuvahNk-X4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کاروان تیم فوتبال گل گهر امروز برای اولین بازی خود در لیگ قهرمانان آسیا مقابل الجزیره امارات راهی تاجیکستان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/139978" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHlH2VOE-kS65K0Rfo12I1vKlVFkNevy4MJbD1c70FPoub0_jveGKEIujHfyc1pKUZadzv3bZK-TSCjBbq7zPcn5kz7cz7II1MUvcQRqMwSKSE_qBgyiTSVgXz4XyXOrOq5cPhPGvG4EFm-FnJ7B3TtQ4CvrepAprYEfjIXUKGS7tUwunKTlmzk4F48t0S__cipcMun8EDEn6TWC68PuxM59SUfYH23YFFF-hmBQDYtEDoUA_N_ENfMnB3Fpxt3Hs4yDsioj4mci8TGqNLn5lIb60Qr7iNM1Kr-xYRHSAnN-GhN4_9Wio3_eYp_DOVdCZja5M3RminWe_tiko8txEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پرسپولیس امروز عصر در دیداری تدارکاتی به مصاف تیم شهید قندی یزد می‌رود. این دیدار در زمین شماره ۳ آزادی و پشت درهای بسته برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/139977" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🗣
🗣
🗣
🗣
🗣
🗣
حمید درخشان: هیچ‌کس در باشگاه پرسپولیس دوست نداشت موفقیت من را ببیند. همین‌جا در خبرورزشی با صراحت می‌گویم چند بازیکن آن زمان پرسپولیس کم‌فروشی کردند تا تیم نتیجه نگیرد و با حمید درخشان موفق نشود.
✔️
✔️
امیدوارم این بازیکنان حالا پس از گذشت ۱۲ سال جواب…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/139976" target="_blank">📅 10:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/139975" target="_blank">📅 10:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqNm6EFykEIbGW2hdsLWoGTwWOME41G-Rh5qQkiN4BGFL-HNIKs1b9rscIOlHpRv1_pp8SZzI1qPFHfGDqclpjxe_iuM3NQmSbZBjAQMk1eI6R9s82Wv8NAor3KRz0Mr9rOxYzPwhiLYSoqDlIidQ03qvvXK8CWTDTgaa2b9-6mydEPc633pe-WkJlVU6maTLmRc6OpXVqFSGyofVkymUM--4SRa5yuLEB8CFH8dfMHzdZV6T0U254N18d5vYKMxbI9LdI0ly-peamjspBisf9t1u1q-upxJ_d_7ce7lJIzB0kYfzoeQNgDyYp2zjadaCiJXovtjgJE2bqDxi_8zHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗣
🔴
❤️
پیمان حدادی:
🔻
بازی با خیبر را لغو کردند تا یک‌ماه دیگر به صدر نرسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139974" target="_blank">📅 08:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPdWmKyaS16cECOmnPxJWddBsFp8RgYal0Ol0poIIIIb2u_SJ3kApNV67RWwyHRur4Str4xgrv8eUTme-7hkdzEAYV6hipLA1pgkGzwyi8ND1pULcXWjLWgu1GRTW-P5AumWkgweIe-ltW0mIdiZCQtbzo_Nmb961ok1LF14kqG4cXor4IVz6ygSOl4jx1AftIvR0WaiIR_uxIMuhb_5oUrg44Ttjuy3TNusvdFb7ApY2TRn6GGMgJTyjmTrELHCd0gdL9i47Dy-WujsbV12Wl7tUsmAemy1peuecSr5rDMH_Mgk-KSSMmgLYPUJqw4SJXP0cpCHo-NtGgmxXqFlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/139973" target="_blank">📅 08:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139972" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=gKLdiI-rI0cbzB4iPjiVgBjFKie35sftFjSNiCWFe_A57XydkA8qCuQXiJNSpNpatOhDrE1dG96t5TEYZPnF5xZ_AI-Xg49TF1b9ZvRqy73gobyuGOUcbC2DSUWjdosQrqAAdyGJXxyKuY19udtjGVmGCOyL4n44h6bl7fVx1rFRJpYuum8XNgxlRehgg56WJeEe22YgwKlcgZWxe8c1CZTdRF21y71KQuGbvCufTt0Ewl4Kk2jAdTNeMmKHyED5YKsBZcbf4Sxoc74sSaBvfTkBJdw9FIZE4JVSVEXGT5MIggCZeyiA3eWc9lnt77e4dLtgPMNz3yN_789xmv9mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=gKLdiI-rI0cbzB4iPjiVgBjFKie35sftFjSNiCWFe_A57XydkA8qCuQXiJNSpNpatOhDrE1dG96t5TEYZPnF5xZ_AI-Xg49TF1b9ZvRqy73gobyuGOUcbC2DSUWjdosQrqAAdyGJXxyKuY19udtjGVmGCOyL4n44h6bl7fVx1rFRJpYuum8XNgxlRehgg56WJeEe22YgwKlcgZWxe8c1CZTdRF21y71KQuGbvCufTt0Ewl4Kk2jAdTNeMmKHyED5YKsBZcbf4Sxoc74sSaBvfTkBJdw9FIZE4JVSVEXGT5MIggCZeyiA3eWc9lnt77e4dLtgPMNz3yN_789xmv9mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139971" target="_blank">📅 00:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
‌ ۵-۶ بازیکن از پرسپولیس در فیفادی جاری به تیم ملی دعوت میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139970" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139969" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139968" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
✔️
درخشش بشار رسن در ازبکستان ادامه دارد؛ هتریک پاس گل این بازیکن در دیدار روز گذشته تیمش که با برتری 3 بر صفر پاختاکور همراه شد
✅
✅
آمار او در این فصل : 25 بازی، 4 گل، 9 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139967" target="_blank">📅 23:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139966" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❤️
پیمان حدادی: وقتی لیگ تموم شد و به همه جا اعلام کردن نیمه تمام هست، هیچ جای دنیا پس به تیمی جام نمیدن و خیلی غیر منطقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139965" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
ریکاردو ساپینتو؛سرمربی سابق استقلال:
🔻
من با مدیران زیادی کار کرده‌ام اما تابه‌حال مدیری به شهرت‌طلبی و دروغ‌گویی علی تاجرنیا ندیده‌ام.
✔️
✔️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد و انتظار داشت من مسائل تیم را با او…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139964" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139963" target="_blank">📅 23:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
ساپینتو: پیشنهاد عجیب تاجرنیا برای استقلال!
✔️
✔️
ساپینتو مدعی شد تاجرنیا به او گفته قرار است سعید فتاحی به استقلال اضافه شود تا با توجه به ارتباطاتش با داوران، مدیران سازمان لیگ و فدراسیون، مشکلات داوری و برنامه‌ریزی مسابقات را به نفع استقلال حل کند و…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139962" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❤️
پیمان حدادی: خیلی ها آرزوی قهرمانی دارن اما پرسپولیس در ۸-۹ سال اخیر ۶-۷ جام گرفته. بازی ما رو لغو کردن تا صدرنشینی ما یک ماه عقب بیفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139961" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❤️
حدادی: هاشمیان قبل و بعد از پرسپولیس کجا مربیگری کرده است؟ دوستان در یک سال، سه بار او را دعوت کرده‌اند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139960" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: محمد عمری تا ۳ هفته‌ی دیگر به تمرینات برمی‌گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139959" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139958" target="_blank">📅 22:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139956" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdUzXsMP31T78tV_LshB6drQWU_XBCUvWePhJBdWgszGtfDV0zMltl_8MaCYFEAd9qnoSkbRd2Fs9GTLIc2h0hl6u-Hqn9K7ba_uZuWCoFg12fWo5CW_pOkYyl1pzDS34lW6Zvy8GPE4cBqvKMAOIjSRhmqHfQwS7_LhME3SnRZA25w1imfmUReM4wckMCVP5ksBkgGnuDFhxj0pSCy2nyMYqa5lXWcylGpdfvDaxbe-2rTD4Z9EHesX5D1B7yvWjMP_lX18YjEZd65riTEH1CCGb3FSqhbRX7yR8cbWQXW5LdsiTMZMvG2R75WIygqTUsgwFDWlNUW2EEZg_6ucdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139955" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6060af132f.mp4?token=TAJElFCFHZ-rIGrksFIWJsQagINrQ8PjhtibSyeF_YptgXjt-aXx1SHoIYCgtFts0yysxGz3ISmL64sd30CkvceE9EdfnbJp7a0gO8NhwJqkRmWKzcLmHFeNHy4TToHzEae_ebR1xy1ufluEtvkJDwJ0SumpFMOCOtDvH6ioTQBfX1yFfXWe9bRBKR89TmHN19ocdxLSKuNA22MX9ghbxBu9LpbBJS_ppPuVvznHVqWs6-R3eMLoS7OOYlSvkW2_I5olsKlFjSbPGmHE9s41LVElSn_ehR2ETDtK2zFSRdM4tuBlEWsExT0499ZwdtCdTNEXxN7x9x06HIzE5tBeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6060af132f.mp4?token=TAJElFCFHZ-rIGrksFIWJsQagINrQ8PjhtibSyeF_YptgXjt-aXx1SHoIYCgtFts0yysxGz3ISmL64sd30CkvceE9EdfnbJp7a0gO8NhwJqkRmWKzcLmHFeNHy4TToHzEae_ebR1xy1ufluEtvkJDwJ0SumpFMOCOtDvH6ioTQBfX1yFfXWe9bRBKR89TmHN19ocdxLSKuNA22MX9ghbxBu9LpbBJS_ppPuVvznHVqWs6-R3eMLoS7OOYlSvkW2_I5olsKlFjSbPGmHE9s41LVElSn_ehR2ETDtK2zFSRdM4tuBlEWsExT0499ZwdtCdTNEXxN7x9x06HIzE5tBeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:  حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139954" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
السد در 4 بازی اخیرش 19 گل زده
🔥
پ.ن یعنی دوباره قراره عروس بشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139953" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=iPPtnSAYiUQ55SeoUq5LQCCm9okrVwmMP0gk7RnhyhI5bwwIR6j4Yxox_wFcUj9iITWbRQDvFbiTNKTPKERhK8cGw62A5YP7ksk4qmDogArCwyvoncR8BQ-7Y3WsdOJt2Ml3RmxKdzH2v8fk7OC0giW4ckIEwzR-giFY1r8SZFphq65Yn_lPteFkXjdn2T72Sk7qt_ykrSHc7s08M-ojDKMvVQl8kIExlHqNfi2Q1TAVcQF-Qf1dTE4KQZ8T8PPFEY0QZmt64BjL2z3k0FBb6xznVVKQ3Ww-q9op45n4LPPrr-2NCC20jL-rxvkiCVojMU0vBHFuFMFH1nsSviPbw7Z9MqcOs7Ei9Oaqnm7SKF9cVPqn7-MTQzZaxmtSjq54ZAug8BGd9lHaslHVu6cgjKRRrgRrDMpEyB27F2CXmjOD_JpSGPg0paGaNs22no_pWJ7fubR5iKxPSKeBbNOjCmaobnfFS12LZ4HAIkbammi2L0oWYFh785hGrNKqb3awRWcrcTHueqv9fTEz1XLjHXpfT66_SRkyscFaPGL7xJYdZILS6k1Av6_a7Js2iAfG5IgHZYGeQ7FddXDb2medK-dj1IPEGTSbttFu-mbvTzpxKuQIjoQJUXEVFy-N5NvKNh1LHPURmPEuQiHLHBL_W7H7vYmBBhsXFlKBWl4k30s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=iPPtnSAYiUQ55SeoUq5LQCCm9okrVwmMP0gk7RnhyhI5bwwIR6j4Yxox_wFcUj9iITWbRQDvFbiTNKTPKERhK8cGw62A5YP7ksk4qmDogArCwyvoncR8BQ-7Y3WsdOJt2Ml3RmxKdzH2v8fk7OC0giW4ckIEwzR-giFY1r8SZFphq65Yn_lPteFkXjdn2T72Sk7qt_ykrSHc7s08M-ojDKMvVQl8kIExlHqNfi2Q1TAVcQF-Qf1dTE4KQZ8T8PPFEY0QZmt64BjL2z3k0FBb6xznVVKQ3Ww-q9op45n4LPPrr-2NCC20jL-rxvkiCVojMU0vBHFuFMFH1nsSviPbw7Z9MqcOs7Ei9Oaqnm7SKF9cVPqn7-MTQzZaxmtSjq54ZAug8BGd9lHaslHVu6cgjKRRrgRrDMpEyB27F2CXmjOD_JpSGPg0paGaNs22no_pWJ7fubR5iKxPSKeBbNOjCmaobnfFS12LZ4HAIkbammi2L0oWYFh785hGrNKqb3awRWcrcTHueqv9fTEz1XLjHXpfT66_SRkyscFaPGL7xJYdZILS6k1Av6_a7Js2iAfG5IgHZYGeQ7FddXDb2medK-dj1IPEGTSbttFu-mbvTzpxKuQIjoQJUXEVFy-N5NvKNh1LHPURmPEuQiHLHBL_W7H7vYmBBhsXFlKBWl4k30s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: بازی خیبر را عمدا به تعویق انداختند تا روند پرسپولیس را متوقف کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139952" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139951" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139950" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139949" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUf37k0b6ZqCCElCPUfXd-g1ymbdDd5fU-20cc9RU0ZR6N0QWOG-dRWSGt8w2BicQ_80pBdHrYLPskBS4uiTNBfNFGjTKS97U1tRkCspcq1JLq2HXgQ2XuiF8syj0DR7Olc8QknybUeZcYhSp8fME-UMzSt_ww1JWVi7FsK2UGUAil00c-fT9NEFSWZNPlXVWgPQjCZ30qq3WsckdQUDzX5R4Gw2dTF8yXNcEtewNOA9zQAB3BjiPPUsu5VD92WhZxnUtk9xv_at1Zswl6By35AbXHBblE-5QbBjL-8E7RmZ8uCx3RPnJCOORgB0rVfvWCueNOj-xyR5FyBoXQtL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139948" target="_blank">📅 20:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udIS0mBiTx06-F83PSzofMUk0bhZiWlkX_iecfPxTBw00lcve0DtLL2meizZqXGbCd99W6LQREhu9mRQymJIs4kN1YIBqjLvdy8PX0LGiIPFpa8EnOZ2ku3KmyLxbTElOVDt7IPIllt3jahZg6aQjoiQ5MfqU-D6GSo2wt3us6LEPVmr1-oe_twiq2PIUt0Ao_61q9Y-e5XprmFdQ1aRwyn0xDO8OODmZ8SC_ilqXZkyXihmpC4lgi7Zta0sJ7XI-7cm2PJDyqm0s_Sot-Js-Ub1Vj2x1aJ9K0HPD6hBZ5H5u4bXCVPZ42MuU70BYEqjlHEABB3qm3jjJm4j3xiDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid -
⚪️
Rayo Vallecano
⏰
Tonight 22:30
🏟
Estadio Bernabèu
🟠
رئال با برتری کیفیت فردی و مالکیت توپ، از همان ابتدا برای کنترل بازی جلو می‌آید.
رایو وایکانو احتمالاً با دفاع فشرده و ضدحملات سریع، سعی می‌کند ریتم رئال را برهم بزند.
کلید بازی برای رئال، باز کردن لایه‌های دفاعی رایو و استفاده از فضاهای کناری خواهد بود.
با توجه به اختلاف کیفیت دو تیم، کفه ترازو به سود رئال مادرید است و شانس بردش بالاتر به نظر می‌رسد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139947" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139946" target="_blank">📅 18:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZTCXCBkB0DP7fOetyd0zKK-Ffa4hMP9G7sGOfGGVu7j6tiVvj-MEilRzCXCybydnCf5MulR1KQJKSkNw97dgTOnQdhwIS4guTk9DgLGm9bxCZtIXX-SrdquHCRxVzbPUcWoQcHlNxu3FziDF01oDXuBiDG2JoGeEqYrioCem3yLDRJdhfcwwd3Nc2hDb-6Sx3dJcq7lk-RftfB6dXwYn-8U-u2AD0iHQPLug7rm4_7Lpoi4qd8fmGL3DJbVjIiWges2Ws06NfX_SknC89os7vJ01YWorvxF2PAFFLM73pcZtNF46MXsjnWwmC0Muifm4QX5LyEnWMj_Zji2SNTAjkLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a080739df.mp4?token=jEGZNBVhpQXP3SRiNDv8MnYXR_keloPt4ZlN6gmFF0VzJsk4Xb8wUMlGmEu3B6t4xGDfcggvCakHZ5p21-FJLENHFeCMT3pJzzuOhdHfiwRnq5UMok-ZfigOtihR9-9Tlxwa6MOTfmJCyVIsHmt2hjof8NfgatheONAYTcduDMhFyQHLfQbP29D2RPuznocKE6g6jK8An6vMN3qNAiot7Uss-jjT9di33EP4-MH5TAdULUPstczHxsusUOlSRenD5pnS52WvvEaLlV55rKtZS89EIO7tq3N3nAocnBaX_pO45hSI4tO3j3bjfT1xiCHP4cgDGu5n-eIZt1RoPigZZTCXCBkB0DP7fOetyd0zKK-Ffa4hMP9G7sGOfGGVu7j6tiVvj-MEilRzCXCybydnCf5MulR1KQJKSkNw97dgTOnQdhwIS4guTk9DgLGm9bxCZtIXX-SrdquHCRxVzbPUcWoQcHlNxu3FziDF01oDXuBiDG2JoGeEqYrioCem3yLDRJdhfcwwd3Nc2hDb-6Sx3dJcq7lk-RftfB6dXwYn-8U-u2AD0iHQPLug7rm4_7Lpoi4qd8fmGL3DJbVjIiWges2Ws06NfX_SknC89os7vJ01YWorvxF2PAFFLM73pcZtNF46MXsjnWwmC0Muifm4QX5LyEnWMj_Zji2SNTAjkLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139945" target="_blank">📅 18:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
با توجه به لغو بازی با خیبر، پرسپولیس فردا در دیداری دوستانه به مصاف تیم شهید قندی یزد خواهد رفت.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139944" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139943" target="_blank">📅 17:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139942" target="_blank">📅 17:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139941" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUIFPxpvZyuuEApIEg3bbztfSPjw0rRh7ZprsPethQ4QlTTVnYLUxCoD8_aY0KOrvboQ7AUztpah6m3kNUD0DKoTolq73XWVQWDKBMT4-6-npe_QvOONni4m4q8UUf5HOF2_dviQFerLycq-DxMJkSSwzVLgEAzQAzH6ar4z-Rvpft-DjprMFm5so0weGDVtaLBWpPpiLY3z84DOQI6UZBC6Y5e2Hi4ldsKcrtztjYhXLrRQnuh7PCpKxTXoMXCahttz5vN_J7-a6sUvt76N9YKp5aMp294JGR73LyBZf38RC-qS2Yralzm04z9sDO8-1WcjWTuYLOg0crmC6Xi9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میلان در آزمون لاتزیو؛ جدالی نزدیک و تماشایی
⚽️
میلان با تکیه بر کیفیت هجومی و امتیاز میزبانی، دست بالاتری روی کاغذ دارد. لاتزیو اما با ساختار دفاعی و ضدحملاتش می‌تواند بازی را برای روسونری سخت کند. انتظار دیداری نزدیک می‌رود؛ جایی که جزئیات می‌تواند سرنوشت بازی را تعیین کند.
[
آث‌میلان
🔴
🆚
⚪️
لاتزیو
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139940" target="_blank">📅 16:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139939" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139938" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPa9HiFUqqNOX83eCfoHtXPBOPBuG6oJ7vc8YVj8fp4mHbqCP4zTeWxEg2CGJSXorhqYcs5iWb5EBKhNqw9q5wG2ZSVNF07zCyuvowmIsZ-LxtLYSt-KYxxrUTESysTjRP62Z5v_CNkeUS-0_VkhfySCekehXwA04Kq-CLtaRfDyKlDz9konvBp3QFLcHTUqztXQII02pw5LjRKU2F-OzlTTZKb9gjObYrusy5Ay0T6nX0r570LjE9EZ3nQub0knIWOl9I9cf-4M0tllYofJXGMT2YF0gZZHRTDUPTagNtZ4IryftBzBindiHJndW9KuWWoV8dYR4DhjkOpp82ij7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده است.
📊
۶ بازی | ۱۳۰ دقیقه
⚽️
۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139937" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
باشگاه آلومینیوم اراک هم از بازی کردن آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139936" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139935" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139934" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoT6JailPbA2Xt2HT8yW1Ya-kNw6irOOf2t_9D2pxJJgg6o-qq-tMerpfHlFW9VxwiAB53zzcK5xX3dCSuvugnrcZmM4aR9kwTyP0nsMMBiCQu36KqBj6h25nP_j4rMbrLYwVYSZriZ4i1nwJSm0YjbM4H_elmCWgalFJYh1PPovleyYYD86I6uwoae1IuKm9m_Eu1zXAhGUQ67HEibTe_ItbSROqo2S-fD8RTMUCjh2AKvGJT34PUDztsAWyG5OHf1TUCmpcZAMDzT5_-rjUihDR-NWRp_jNlUlHhxH5cnXD9xXPYPAkJg-sT5OPe8-mtX0aRuIRLtYgiTDTaZSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139933" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_FVZy5PmV8cwP5kUkJevkktv6-4dFStbcXMzKXKcEMWbddQZqch2Uo2618FykWfTvfV1Gp-PcQOSK8QWLDQJ_reCnDuwhsUpHfM7sgKgc78o-YVceTNuhrWqp0RPq972yTnSGBKmKoctHkTf1RBawRspMaD_z2WkHHndyJZETyyZc67nMLa38ASVAM19Yzdi5tWdURsfF2vZEioSndOnAj1Pz4D3GjpkXXakOgXjfezM8tOZWnGTMwVlKxuu41pP6k2u-bYnVn9ZLfssXMMaZc1CXbgUj4nKeOaD6iZL8PX6NIm8uapws36jRBa9vBHFqQxs016UC8UsN2V9RLUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسپانسر دو باشگاه لیگ برتری نساجی (وارش) و تراکتور (آتا) توسط وزارت خزانه داری آمریکا تحریم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139932" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139931" target="_blank">📅 11:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
حمایت از خداداد عزیزی به رغم فحاشی های زشت و حمله بی اساس به فدراسیون فوتبال درباره var
✔️
✔️
سخنگوی فدراسیون فوتبال: قطعا و حتما امید عالیشاه هم زمانی که خداداد به استرالیا گل زد از آن گل خوشحال شده. هم عالیشاه و هم خداداد عزیزی برای این فوتبال عزیز هستند!…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139930" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
پروازهای ایران–بصره تعلیق شد؛ سفر استقلال در هاله‌ای از ابهام
❌
❌
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139929" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
پزشک‌باشگاه استقلال: یاسر آسانی هیچ مشکلی برای همراهی استقلال در بازی برابر السد قطر نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139928" target="_blank">📅 09:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt4zn20DMgKe6zzJaMCahRotOzYsnzH2BUdc6eL1er15HG6EUoLXCq9p_U1uoAQ6L0B5U6Vhp9gIsH1YSs9egI2b2JhtBBi140wraa9hL6pXzOSIS-Ce4UzgYcJijdJ6ffiJHx_jsIG_gbBvzgATsl52arfSwF_5j635k9eYfvfItQpghec5QKpA_rjAM2P2YGncnMm5F4dCIjLKpfT-F0kww_cO3-OOucFgDO0_NU58hM0cg6wHP_PSOZIycedgnIH2oai4Tpi8hHMWn4I4afRx531v5fBvcMDhu6HUEI5OWbcvd9yvqHRDlGms_HvgsVgBYOubLh9iJZGs98vp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139927" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuM6W2SvVrqs7aOJog6EfOqI_h-6u3AtQJ5pwytnLnfKDz_L98eU2Gbt63KAhvhj8ycxAN-r9QECCmOkWnRWQJINuMnr3AXZchqIKD-d7ksRr2GzGNa4brmdYEkt4jTJAM8nk_wzn6cOzQ4IaZNXosoyuHZaGzo2jx4a6cwUDz0I6nuyctIsaSqeasP4_GzMY45UKa-3r5iWs4iszfdg9vWOC3rPEaRhF4hZWNoSfYEUoLxmrC-lvhZhN2MlVWDxbkTF3MMNPEg4OQqDj2LEXm4yfnczy2nRtxhLDMYn-LICeKeyZa-VfMrhwEs9W-y03sEvqL3c0g8Sy_aEXvwSyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139926" target="_blank">📅 09:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYyLDBMdQnXeQ3s6XPfvqXRN8Wwph1pwEKtlhEVQzO6OwfP-aLqIjIkUfKCkgiSJlcV_qHRT4ej97PruNRcAymkwcDLrNjrdEeQ-I3DY-TBI0BpZf2TRrEw_QkhjFzEvHFZ2GcUiA5RMS1XN1yBa5ZG4lp0VqQzG5gc5tNxHmoho5cwsElmD2vBZcWgfD3-aJJj9MflxvR90IWWtAt_TmzdHll5ibgH0HkEEW1kO5LYcRjK3KMJ7plRqiZRTojXQd4u12f5W98Z94_XL1kpzy19xVRFEIGGVKSv5dL1lmWVEAAy5kGN5EhXHnSo2EKcB_dvLjCqMHZdddifcYyScNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
شلتون و تیافو؛ نبرد قدرت و جسارت برای صعود در نیویورک
[
فرانسیس تیافو
🆚
بن شلتون
]
⏰
بامداد شنبه ساعت ۰۲:۳۰
🎾
شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند ریتم مسابقه را در دست بگیرد. تیافو اما در رالی‌ها و تغییر سرعت، توانایی بالایی برای به‌هم‌زدن برنامه حریف دارد. اگر شلتون روی سرویس اول و ضربات فورهندش مسلط باشد، شانس برتری‌اش بیشتر می‌شود. با این حال، تجربه و تنوع تیافو می‌تواند این نبرد را به یک بازی نزدیک و جذاب تبدیل کند.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139925" target="_blank">📅 01:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139924" target="_blank">📅 00:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
تارتار قصد داره که به اورونوف تایم بیشتری بازی بده تا اعتماد به نفس رفته این بازیکن برگرده و این بازیکن رو دوباره احیا کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139923" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎦
تحلیل مدعیان اصلی قهرمانی در لیگ از نگاه وحید هاشمیان؛ شانس اول قهرمانی به نظرم پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139922" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
براساس گزارش منابع خبری، مسعود پزشکیان با درخواست زنوزی بدنبال حل مشکل سربازی علیرضا بیرانوند تا پایان جام ملت‌های آسیا است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139921" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=q8MuN8AmEje01N6SQgC_GKGt49qs6FQyYwWY9GmDnqegVOxKINgT7QdmtoX_DYOlt9UpCPTdDHk2pLr2Jvr-h1y5TVBaX59-Cwg8ZnIi73ADTSLcWlytFAEEtuolamObho3ZMUYsWvz2Z5hi8MFP1KWQg8lQA67B_mJvbTzXfEni2D_aCglda5CcqF4x8PM3ISRFqzhAmWQchCGftcJTjXmGiikjfALwpPMAw24KuAJgADsBwmAS3kCxgtdCV-XRMQhZQO5JqdvEgElKhsuHIQsD8kXstwTLKY4OiIT7t5CmKVsS-7DKyIf8Z8Y58gk6NVhXUhw581dQiXBDNvS6L4Uwj8QtYEtG2mdJQY28gIk4AOX2_wCSpGKAySIRMoEwFHouDUsi_Q4SPuSnvJdvHawrIVehy7Oxqe1MRrcXc5cdCb1DVWCq2-7X1zqx-g8ZQnUh012PvSV2_3XbN2_KTHSNKX3FtBDgZt2aGxlE0jgm4d2wPHc-dHPDE_xGAN7LoQ8IQ8919h1xJt6S1LhslN88Ndh1AZLipuPl8Ki4HjMKCWGzNhrBGyZ0usH0we4VGuC2FbfMjNatsGzSS0RLdpc2tEB9peFf4VNtGJLwLiUIvHZQLnPDVGAl4ZFCd7eSvVzHBKIOdZXsd0wXM2-489M85Ro3AdXHeTaOs6xt4Ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=q8MuN8AmEje01N6SQgC_GKGt49qs6FQyYwWY9GmDnqegVOxKINgT7QdmtoX_DYOlt9UpCPTdDHk2pLr2Jvr-h1y5TVBaX59-Cwg8ZnIi73ADTSLcWlytFAEEtuolamObho3ZMUYsWvz2Z5hi8MFP1KWQg8lQA67B_mJvbTzXfEni2D_aCglda5CcqF4x8PM3ISRFqzhAmWQchCGftcJTjXmGiikjfALwpPMAw24KuAJgADsBwmAS3kCxgtdCV-XRMQhZQO5JqdvEgElKhsuHIQsD8kXstwTLKY4OiIT7t5CmKVsS-7DKyIf8Z8Y58gk6NVhXUhw581dQiXBDNvS6L4Uwj8QtYEtG2mdJQY28gIk4AOX2_wCSpGKAySIRMoEwFHouDUsi_Q4SPuSnvJdvHawrIVehy7Oxqe1MRrcXc5cdCb1DVWCq2-7X1zqx-g8ZQnUh012PvSV2_3XbN2_KTHSNKX3FtBDgZt2aGxlE0jgm4d2wPHc-dHPDE_xGAN7LoQ8IQ8919h1xJt6S1LhslN88Ndh1AZLipuPl8Ki4HjMKCWGzNhrBGyZ0usH0we4VGuC2FbfMjNatsGzSS0RLdpc2tEB9peFf4VNtGJLwLiUIvHZQLnPDVGAl4ZFCd7eSvVzHBKIOdZXsd0wXM2-489M85Ro3AdXHeTaOs6xt4Ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139920" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=GHAIAGIGqJwQ2BJWW1CgZJSwPJfMXTkKyeab9v9kHWrlVDyDq0w7HFjUzNTSibEuV7IMo_iRJ4yd4_fmI6L2lkG0V352lMZzSt-PS7FXx2NwI50e8PXYtywURPUJO9UZIq1QzS37B5oFOG54zHO3a5VzV80VDuJkDJ5a2F8KIVN74ajYWGESrK0N1gDQlbAUvUwJRRoMJaEAbBB0IUXVbnKfBol6gDnVzLfucCXjKbjIfLpiwfcjdADleVq5Pc-fJbEr_k6dUm4ULoNbZw0BAORDG4zNnygv9LfPa-FmDQF_TfGLQuKAGhTeGiZk2--o0o4LPtnbOClyZMtN1g3GX3sJXdXmAbsbFSNKX0GsiQRgVe2nua-TEwF9-6vg2tWvafHDUwEl-eEYEwt6ZhtmM_9IH5hF0VIFuvSiU6UJTO_z0oa-JcR3q-ICurb0KGIS8zhYY3FDVufG53aWPVhQFuYv3j9UrJZZwhmI_fHcihCQfzwCqAWNpUTVRPs2QAzGnjKAOYfMSAWXoA6Qsgxdsy75sdsaIC2tWT4oDh8pkv0UjTBuz59x1NdszFPPJNW5SgkZXRMDFeOZY0wHRcVHStWk2C1sh0dwpwIXYwg9neDOCvQhSw6TY7jFhms6MgH8HQXCNf96OwU9_dms-0IjzSs2sqUYuqn2JnuYAoqWncY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=GHAIAGIGqJwQ2BJWW1CgZJSwPJfMXTkKyeab9v9kHWrlVDyDq0w7HFjUzNTSibEuV7IMo_iRJ4yd4_fmI6L2lkG0V352lMZzSt-PS7FXx2NwI50e8PXYtywURPUJO9UZIq1QzS37B5oFOG54zHO3a5VzV80VDuJkDJ5a2F8KIVN74ajYWGESrK0N1gDQlbAUvUwJRRoMJaEAbBB0IUXVbnKfBol6gDnVzLfucCXjKbjIfLpiwfcjdADleVq5Pc-fJbEr_k6dUm4ULoNbZw0BAORDG4zNnygv9LfPa-FmDQF_TfGLQuKAGhTeGiZk2--o0o4LPtnbOClyZMtN1g3GX3sJXdXmAbsbFSNKX0GsiQRgVe2nua-TEwF9-6vg2tWvafHDUwEl-eEYEwt6ZhtmM_9IH5hF0VIFuvSiU6UJTO_z0oa-JcR3q-ICurb0KGIS8zhYY3FDVufG53aWPVhQFuYv3j9UrJZZwhmI_fHcihCQfzwCqAWNpUTVRPs2QAzGnjKAOYfMSAWXoA6Qsgxdsy75sdsaIC2tWT4oDh8pkv0UjTBuz59x1NdszFPPJNW5SgkZXRMDFeOZY0wHRcVHStWk2C1sh0dwpwIXYwg9neDOCvQhSw6TY7jFhms6MgH8HQXCNf96OwU9_dms-0IjzSs2sqUYuqn2JnuYAoqWncY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
❤️
🎙
انتقادهای تند وحید هاشمیان از مدیریت پرسپولیس: وقتی سرمربی دارید چرا به او احترام نمی‌گذارید و رسما اعلام می کنید که دنبال سرمربی دیگری هستید؟ همین می شود که بازیکن هم به سرمربی احترام نمی‌گذارد
🔴
همین جریان و اتفاق را هم برای اوسمار ایجاد کردند و این رفتار اصلا حرفه ای نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139918" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=XCH-6BU-lEwy-Zjr6TnEK3ccAs1uunDiczd8GnAM5YYV80eW-fT2KqHT78cfb7eZ62bZnFHRUaLs-mW2K8MQpD7f4T-KPrjq_HcqdWovjSjPLZ8VxpLo8UpEWrQ_NBKc30R8mFV3AESarIXzUzlPTjTEi1y6DrxiTTXhacNiA1xqi0bf8oJXm5kkAnWSB_EpZrJHaiUhv026JVKBI_ShRH-e2LDrYb080R7zurCqSAo-ZU7rp6J8Xb6JoYpE9uKS1KW8ouUu0t8G4WLuZuyPnpI_ovlIj64mujOYcaAfF9WfMTg1PN_BMLAmznOhmOfLfMOuM0dppfB73f2RnC6uhDhgxlBtM6sf_2D5j9d73TqkrDokZpnB_8uJqU3-180MBEO8sM_80KGt0ZVlPiz0fMI55T7GGdBQzpncQOvg4rbGMHrcsWSDtNSOrkm2zCbLU_QwmcHYTh8PX_nMGyweepEuxTwjov1xp7s3izGcoB4DtF5aKMqE2v4C-zDgUz50rAWn0Zx9OFCgIipWbf961DvsejUzjYUnIRAHsnlSrmlKKYdwMHsrD8coTzT92oGdetSBZP0Ujn5C8bPfJnZtLQ7-X-pFLoCC7qCpL6QyNQIH2xNmqjEu2vwpDrCvNXERuz15TpyUtHL-4q1iXvwvnyhT9i-kbB9khnIlySkqMlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=XCH-6BU-lEwy-Zjr6TnEK3ccAs1uunDiczd8GnAM5YYV80eW-fT2KqHT78cfb7eZ62bZnFHRUaLs-mW2K8MQpD7f4T-KPrjq_HcqdWovjSjPLZ8VxpLo8UpEWrQ_NBKc30R8mFV3AESarIXzUzlPTjTEi1y6DrxiTTXhacNiA1xqi0bf8oJXm5kkAnWSB_EpZrJHaiUhv026JVKBI_ShRH-e2LDrYb080R7zurCqSAo-ZU7rp6J8Xb6JoYpE9uKS1KW8ouUu0t8G4WLuZuyPnpI_ovlIj64mujOYcaAfF9WfMTg1PN_BMLAmznOhmOfLfMOuM0dppfB73f2RnC6uhDhgxlBtM6sf_2D5j9d73TqkrDokZpnB_8uJqU3-180MBEO8sM_80KGt0ZVlPiz0fMI55T7GGdBQzpncQOvg4rbGMHrcsWSDtNSOrkm2zCbLU_QwmcHYTh8PX_nMGyweepEuxTwjov1xp7s3izGcoB4DtF5aKMqE2v4C-zDgUz50rAWn0Zx9OFCgIipWbf961DvsejUzjYUnIRAHsnlSrmlKKYdwMHsrD8coTzT92oGdetSBZP0Ujn5C8bPfJnZtLQ7-X-pFLoCC7qCpL6QyNQIH2xNmqjEu2vwpDrCvNXERuz15TpyUtHL-4q1iXvwvnyhT9i-kbB9khnIlySkqMlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
❌
گلایه وحید هاشمیان از احمدی و مدیریت اسپانسر اصلی پرسپولیس؛ صحبتهای او حرفه ای نبود
🔻
احمدی گفت که هاشمیان نبود دورسون و امیری را رد می کرد و این حرف در رسانه حرفه ای نبود و میتوانست شخصا با خودم صحبت کند/ صحبتهای او فرار از مسئولیت بود و در شان یک مدیر نبود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139917" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139916" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
روشنک :
✔️
✔️
باشگاه‌هایی مثل سپاهان، آلومینیوم و.. به ما اعلام کردند که اگر هفته هفتم را برگزار کنیم نمی‌توانند بازیکن در اختیار تیم امید قرار دهند.
✔️
✔️
فقط پرسپولیس درخواستی برای لغو بازی‌اش در هفته هشتم نداشت.
✔️
✔️
نمی دانم سازمان لیگ چه گناهی مرتکب…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139915" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trE14ZJc9-VWhwiVQQC-hBuepVED505VG4Ff54qqjhJ-lK9iHC0BildjvBGSODErIUhv9_GodQEMQp5nJ1MQ9ZxWILQ5hKForYuiO-pT1r8QzCctNLt9CVCLRGsMLsuarOH75WVrI37xT3MmvJr7pFACgyf--bLgjsLnKQ8bImAXdix9-7VsW_y2riiSI7t3OzESybSkiSRleDXTWA5uTVmw8YydwdD56_888S45eCLQNAwhIo0s3iAVYUIYu3FZAl4cgX2AQAU1EmhfRA2ctPwOAcLAUwAw_NtP74iPx4B93VoIRsF0bQFWLqe4CULoYs95z_ZmtG1cjuMRZwrLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با وجود لغو دیدار برابر خیبر خرم‌آباد، پرسپولیس امروز هم طبق برنامه تمرین کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139914" target="_blank">📅 22:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=Yp7Avy7yqdr_TvBDxAdhRECVU5_3x25MNb-lGsRGFyHVT3cDDDaCAQA_cG9TIeyLKpNYYKopRzQH4ROW2858Rcra947OLKJQyxcC8v73j0-DP1hGgsGunfx5qSyYb8t4RGksD0vtlroxCBKgM62RAgCDw-cWUloYMJFA9dvReTBXfDALEOGDNAWp3MowQnUgK2gvYDmeyd_D-isR1GdB9ceYhAKkvwt-BQTf-urAALLp-qb_BV3bTgZmBvKwOM-LL-eQ2CUNPGr9UTUdXzqONIYBQXVUqtWjfE4oifBhLs9XIj0kUt4YJQuZIp_gW397fKefEkUX5P0v9Sbz0Jw6-QuTqD9eWyBxeG6Z1X4WJxInoBix9UKSTDzRIOIHzPz-RmcdLL6WRUT-cbmKK1FlIdVdPxP39fI0DmKdWbOdV4oJtTpuuo0jKRsrMQA5Bf268MYfCaTqzdszwtSWQ-Bk0dq_lPlC99ljWHzXxXQQ64cd7WpuO1GgTgsK1f-Nd_dBzapqkayrFnAD6drvZl8to7D1fEH4_HNIgu-AUa8otlqJI6fxPaKLmfWH7HuU1-bd9HPCgJJEbiyxw27y2yDB0rKaumgmRJ6OD2DEZNoPpTAHsRKDu1aG90ksGUXsWwt8ysFTPjCT8suWWeGlxHxa1Fpj_3tgX6xo5i_d1Ok9crE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=Yp7Avy7yqdr_TvBDxAdhRECVU5_3x25MNb-lGsRGFyHVT3cDDDaCAQA_cG9TIeyLKpNYYKopRzQH4ROW2858Rcra947OLKJQyxcC8v73j0-DP1hGgsGunfx5qSyYb8t4RGksD0vtlroxCBKgM62RAgCDw-cWUloYMJFA9dvReTBXfDALEOGDNAWp3MowQnUgK2gvYDmeyd_D-isR1GdB9ceYhAKkvwt-BQTf-urAALLp-qb_BV3bTgZmBvKwOM-LL-eQ2CUNPGr9UTUdXzqONIYBQXVUqtWjfE4oifBhLs9XIj0kUt4YJQuZIp_gW397fKefEkUX5P0v9Sbz0Jw6-QuTqD9eWyBxeG6Z1X4WJxInoBix9UKSTDzRIOIHzPz-RmcdLL6WRUT-cbmKK1FlIdVdPxP39fI0DmKdWbOdV4oJtTpuuo0jKRsrMQA5Bf268MYfCaTqzdszwtSWQ-Bk0dq_lPlC99ljWHzXxXQQ64cd7WpuO1GgTgsK1f-Nd_dBzapqkayrFnAD6drvZl8to7D1fEH4_HNIgu-AUa8otlqJI6fxPaKLmfWH7HuU1-bd9HPCgJJEbiyxw27y2yDB0rKaumgmRJ6OD2DEZNoPpTAHsRKDu1aG90ksGUXsWwt8ysFTPjCT8suWWeGlxHxa1Fpj_3tgX6xo5i_d1Ok9crE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
به مناسبت خداحافظی گولسیانی، یادی کنیم از گلش به مس تو دقایق پایانی که باعث قهرمانی پرسپولیس شد و باسن خیلی از کیسه کشارو سوزوند
❤️
🔥
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139913" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139912" target="_blank">📅 20:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤩
🤩
🤩
🤩
🤩
🤩
💬
گولسیانی:
⭐️
من تو تیمهای زیادی بازی کردم ولی یه تیم هست که وقتی یه بار داخلش بازی کنی و بدرخشی، دیگه از قلبت بیرون نمیره. نمیدونم چرا ولی وقتی یه بار تو پرسپولیس بدرخشی دیگه پرسپولیس میشه عضوی از خونوادت. من رو نخواستن ولی من تا ابد عاشق پرسپولیس…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139911" target="_blank">📅 20:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLoqP_KiEWNwLtJpoJb3IpHo-4fZr5V4fn0FE4887xDgOpOvsKM9vSa69bYXAeqPJu4DtnSGSee82kE4_W3EIqK10wicj2X-jChkJ1HgghAR4Q6TKASwId8kfsQOLwZMhEUpdCBvp1sQUiKXcgV5QTIkYLrRLHpxK0A63FA-ajfISir41k2E2SLxRcSpQV3B1h_iKdGDkmlu3ZQX7qNiKNCDfum1l2mV5iZEGytNBjCDZqu-7BNC0CyLwWDrjJWXIzOZ2gFaDRtyllEofdNSRDNxnIkKPnNs3BiQ-rS1hyZ3G9g2-nmKTW1Cw_6KN2_xF-npxOEXNyiwfSlwK4HiJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽
سالاری از پست مشاوره مدیرعامل پرسپولیس استعفا داد.
🔻
محمد رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال که چندی قبل به عنوان مشاور پیمان حدادی مدیرعامل پرسپولیس انتخاب شده بود از این سمت استعفا کرده است.
🔻
سالاری به توصیه مهدی تاج رئیس فدراسیون فوتبال برای توسعه رده های پایه و کمک به فوتبال از تاریخ اول شهریور در پیامی به حدادی اعلام کرده که دیگر به عنوان مشاور او فعالیت نخواهد کرد و از این سمت استعفا داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139910" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
✔️
فراز کمالوند سرمربی خیبر: سازمان لیگ تصمیم بسیار درستی گرفته است که بازی‌ ما با پرسپولیس را لغو کرده است/ من نمی دانم سر و صدای دوستان برای چیست؟
☹️
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139909" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
فراز کمالوند سرمربی خیبر در گفتگو با ورزش سه:
🗣
باشگاه پرسپولیس ابوذر صفرزاده را از ما خواسته و ما گفتیم در شرایطی این بازیکن را می‌دهیم که حسین ابرقویی را بگیریم. همچنان هم در حال مذاکره هستیم و به نتیجه نرسیده‌ایم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139908" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPhrp7fw6sm4fMBDyvnxzty-whEnjv3670cagqVSvH13bvAhAbXXwRd9Sr-8M8Qlil-kiPgCIIt8BbVIQdMsGjGE7A_zO5p5431jeuQ5QMDWTL4H73k5XQl0Kcj7tqkjHLp8ULI8fg0tLYmdcZqMrpZ4Z0928yoXTiPGgxELCLaax_TZhNjF2mdyYIl5bsgSlmHJj_-dD3KUe91Rb8Y4BL0eTOLVPNQ3p3rLSOe1Y0lDqkLnUPfSWmZaugwg6RU2w_p5SQJ5p6v6l5dXSfMivOzRw58Ij6GsOyaozHa5aDDwFVHD6O7LZsf_tluPkHYkyy_0gh06-BPa0dkr7OYquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبردی نزدیک و تاکتیکی؛ والنسیا با تکیه بر امتیاز میزبانی به‌دنبال فشار بیشتر است و سویا امیدوار به استفاده از فضاهای دفاعی حریف و ضربه در ضدحملات؛ دیداری که می‌تواند تا دقایق پایانی کاملاً پایاپای دنبال شود.
[
سویا
🔴
🆚
⚪️
والنسیا
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139907" target="_blank">📅 19:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139906" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND45JsTPzAGpWbbnUAvPRkYh49WP5EceDqnZyB0VXsT7xGUcnq08arRMFjFSwqr9atvbknP_tx9ysW6NZj8NCuUKC2io5Yls48_JryFuiFaFwjX57Zt7CG1MyEXV1kvVGwmGW2zNfoVmS5hqNYDwxRla53Zg9EBBuAqkxNvXLfoIzQ5H7t-7r9W8Ai0o-4rCXmmLqWcztgW-X2O1fAFW-4-YYkxhaawWK9j7_YhSXB0TfOeyGZdma8rr6IaoNy23FgJMmO-gDwq3PW4f9kX6_C67llBcCqGXVURbMsyuF2a7hHmuKGMd52dTKPL9ngQDP4ifmAkktPm7gerXeoNgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139905" target="_blank">📅 18:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139904" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
مهدی تارتار بزودی و بعد از بازگشت دنیل گرا به تمرینات درباره‌ی ادامه‌ی همکاری با او نظر میده/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139903" target="_blank">📅 17:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139902" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC4_cyiDDmNHUTmWNG7UlJOr-s4Oh6UuWHvTZKJBUDc7Ngs9YQeOwQXpsn2yi1ziNJvcvjBusqwCZ49qncG0tuWufSLLZ395VaGQGk64NTJr2aUCo_MMFC6-xNK2KMtOhfTqBwnwUsqn88DKT2yAtvKZkvhthyV6hPcTtgVAwLRHmfK5kTe1CcTLlj3MtBHNp52r142emEuwUh3_ZS8lH5xFnVSOpLou3InNCA7A3ud0aTGRjj48e_8rmngiYULiiRHAwNYPr8gWKuuUEhVwRXpYFVqw0BHktRuwFermyoadKbdqPURQ3GL9lI9p7toP6eXD3pciBGwRJaZLOKP_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
پوریا شهرآبادی ۱۵۵ دقیقه ۲ گل
✔️
شهریار مغانلو ۶ بازی فیکس ۴۶۰ دقیقه ؛ ۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139901" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
