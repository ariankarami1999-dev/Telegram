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
<img src="https://cdn4.telesco.pe/file/Z17RYuk81tmqgAh_WGWk64EVsk3jINzG7njZQdsKhucRoTdO_l8zOpUZ0CABknwXxWQzKwycZ2ZKFm_C0gTGVoDm7RWeJTj4WRHbWgFmPSKfp8eAGMB5ofmkmR5TgKb-lUnPgWZWuu7_mn1-2D1Frdj1Hc3qg2Q3QdRi5SluxacRummaZzdFDYogAeiC1uEDH2TIKQ3Zm5eF8DTmFOlwMNugIFMBfSLqNzXp3TRJxhF5RHMHND9cmwde9HL8Sf1F3qSNTBgXu4ukM7fBKQhkzbXMSrpAkV3p4QonsAnp6DrvqrmDwRyKzU0QQ-AqmbDRb4Jsf84u-gxCMr-sKO0Hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/139405" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/139404" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/139403" target="_blank">📅 15:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=twaOU-oIWv5T7DyGpojaaZF7dVEuQPjFmGdcC9U4JdzzktNxuoAeIdagpTb588kxqj0Tq6gx_dV8JpOK6IGR8ueFrp3k6OpvBS0Pa-5FWJPNyhPmwcyeYc8sxEvwtGzeisLiTtVRair70ROxyhW8l81HVp8kBMSrCVcWE0naqz05ohPuhNHO446K1rbg335X-SLqK-cbsTZW6sa3qFcWkZcKxv4Cj0GdLNlzq00Q8gNRqps5DOxKXQ-CJ0IrO-n7c8X9p0LPqAWcDupdSjr4ha-ySmDSjWQavMMFxx6rJOs8uSqyndVdJ0ucReBgVId4sT4BIhycH0eEqy30qznkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55bf0f119c.mp4?token=twaOU-oIWv5T7DyGpojaaZF7dVEuQPjFmGdcC9U4JdzzktNxuoAeIdagpTb588kxqj0Tq6gx_dV8JpOK6IGR8ueFrp3k6OpvBS0Pa-5FWJPNyhPmwcyeYc8sxEvwtGzeisLiTtVRair70ROxyhW8l81HVp8kBMSrCVcWE0naqz05ohPuhNHO446K1rbg335X-SLqK-cbsTZW6sa3qFcWkZcKxv4Cj0GdLNlzq00Q8gNRqps5DOxKXQ-CJ0IrO-n7c8X9p0LPqAWcDupdSjr4ha-ySmDSjWQavMMFxx6rJOs8uSqyndVdJ0ucReBgVId4sT4BIhycH0eEqy30qznkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه نقش‌جهان ساعاتی مانده به شروع دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/139402" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/139401" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/139400" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
🔴
🔴
مروری بر بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/139399" target="_blank">📅 13:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139398">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brYoDOdCj3AYfqiHQVaDko2USELu_V-rV5jgZaIr2G7mgdKBU8qsswe2Pfs3edB6GTIR6s1FmAwkc5D12MmTYtZm614O0yVvvf_yuqWNaR8f0JG5PksBTdyDuMwSjX41kojAVSO2Z6FrxkTRC8rJYH6T1teZFH8bwbYCxpdy1bIeZ55D_17UEsqBQdSp-xO4Aqpd4J-3-8xGeoh2qDho6Q9-wrrAf6sUyHQAoH36OhiGVK33ksjPNdefG9VyFcnVnJV7IOhaFdEYFrXCJcKm271ZjrVvMzo1LBRgbr4Oij2A34_aZQxE6Mu09wRp3Stule30zoWsMHfMV_D0_lwg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اصفهان در آستانه یک نبرد بزرگ!
⚽️
پرسپولیس و استقلال؛ دربی پایتخت در حساس‌ترین جدال فصل برای شبِ فراموش نشدنی.
[
استقلال
🔵
🆚
🔴
پرسپولیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/139398" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139397">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
نتایج 19 دربی اخیر پرسپولیس و کیسه:
📊
در 19 دربی اخیر دو تیم 8 برد سهم پرسپولیس و 11 مساوی سهم دو تیم بوده، و نکته اینکه کیسه بردی نداشته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/139397" target="_blank">📅 11:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/139396" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139395">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=CX0E_y09s-80OyvQsZ-sdbc_Q6ADoeMnlssNGw0mFwOtHQ55whtcaO5JBf5Es9DU87CumznQFUSQvb_tmCQo8A2pnElwZ4CBDmFUcQ45vsCMllA8J_McTNczq6EEINNKj1fqXcwL157jSZzxh5KOJT8s2y8v5IpRjENxMZQKMkye9ZPxnTqDTwk85jtk9VZWLMRq4-dhYVV4WnAEzEj0SGWiJ52uODZyX-14VlpB9N6U5mK6Q53FBxo08629kRcDWYtBiFScUsQ6RmSKE3Sdh4J3OL0NnSlYsThIJba2Y9pwLvmNY3zgt_Ji9JKFJ1Zt_fbNQ_iVm2qmQX5yNrGOmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcd6b3f28.mp4?token=CX0E_y09s-80OyvQsZ-sdbc_Q6ADoeMnlssNGw0mFwOtHQ55whtcaO5JBf5Es9DU87CumznQFUSQvb_tmCQo8A2pnElwZ4CBDmFUcQ45vsCMllA8J_McTNczq6EEINNKj1fqXcwL157jSZzxh5KOJT8s2y8v5IpRjENxMZQKMkye9ZPxnTqDTwk85jtk9VZWLMRq4-dhYVV4WnAEzEj0SGWiJ52uODZyX-14VlpB9N6U5mK6Q53FBxo08629kRcDWYtBiFScUsQ6RmSKE3Sdh4J3OL0NnSlYsThIJba2Y9pwLvmNY3zgt_Ji9JKFJ1Zt_fbNQ_iVm2qmQX5yNrGOmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
بهمنی، سخنگوی سازمان لیگ: 6 هزار بانوی هوادار تماشاگر دربی 107 خواهند بود/ درهای استادیوم نقش جهان ساعت 12 باز می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139395" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566218d82d.mp4?token=sKHSBXxZopMWh2Qh8IIIYWOorgwo6GslmCNlIMA3U-TySZveHCgEL4U3DWu3eYHzDWsErJmn0kc-icQLzAro3j9ob18mUpA5NgRannon726j_qTh1PUKN4RNAF5u6ILj0ot1BVkTw2Cz7QUGgXhyv_ALh4s2LEmvigg7Cu7C9K2Uj7KXyB3yg52AJ8pHgIzK8ZlL3ZjkMYQgiVPjBgEDcR7CuQhDcBOA24-u2Kq-w52rJANiKM0V0af0pwIRJ495y1xXaDs4Qy7ZAqENSGGcDpmq6BTgqzCNC0JEVWinPo7NpN0hJ3EraXz_wFmX64pKbFWn_3t9b31en-K8xu31ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566218d82d.mp4?token=sKHSBXxZopMWh2Qh8IIIYWOorgwo6GslmCNlIMA3U-TySZveHCgEL4U3DWu3eYHzDWsErJmn0kc-icQLzAro3j9ob18mUpA5NgRannon726j_qTh1PUKN4RNAF5u6ILj0ot1BVkTw2Cz7QUGgXhyv_ALh4s2LEmvigg7Cu7C9K2Uj7KXyB3yg52AJ8pHgIzK8ZlL3ZjkMYQgiVPjBgEDcR7CuQhDcBOA24-u2Kq-w52rJANiKM0V0af0pwIRJ495y1xXaDs4Qy7ZAqENSGGcDpmq6BTgqzCNC0JEVWinPo7NpN0hJ3EraXz_wFmX64pKbFWn_3t9b31en-K8xu31ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فیلمی وحشتناک از حمله دیشب به سیریک
🗣
بیچاره مردمان این منطقه
🖤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139394" target="_blank">📅 10:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzcYaHG0iJTH57l4nWE1YyVB6QgeXZWwZyKyCi5jN03koF5zKUxkNf-rYbdQECIBkolmyG6pb4zscHwlc8q0CG7lEOMOlptBhLAwPm3qT84BB6RHwiDSrS4-iyvkOD8zyh4liHTZJ05QEj283Tw0_yLj9iaN7A9VFAgDEcTODLNL-SrwFgnLULE2OLXAEZHXqcka7FITWAKKMEPByjgGv8N1UzZJG_7oT_AZSqfQwcQxE4ZGQmbxTZwwaPyJo8PWKPLWYQIdcssRMRJ1Yq2MCbf_UBJEtvU-qWuj8i-pYeoIGtUghiNPDeRmX04jKdGMLebZLhGj1B3xMtOMUIOUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
⚽
پوستر جذاب باشگاه پرسپولیس برای دربی
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/139393" target="_blank">📅 10:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
برای کمک به تیم ملی امید  هفته هفتم لیگ برتر فوتبال لغو شد!
✔️
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139392" target="_blank">📅 10:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlfipSJo9aOKZwhRY7nRwiGdSpLUTYoN_Jz7StfR069IkbKQ8QPDMLUSqJ7zaApCzEBMMI4JntNox21GF4scJk2A2E-ZqpEzblZ8JFembMJTXhPVpPGd32ubJoVNItDfF-y4Dswy3wFQnyWPKuaCyAl0ORii3BKRiZ9WKA2ioQ1umH9hzGcSIB20G-GAvoGu_BpJhOmtEWdnp2CeV39SyR3xd5NLUpZuRKrnWazSkpyUPY53aqiUtxVGtSPPFjxuL-nMa3rMUTzk4rTK2h5VM9-EWp9I22pMsFG62lpme7e5a9Qu_gKLx6rUPHGuwLKeC0Z79BfBTHpyRrQAQJ89OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
تسنیم: شایعات الکی و بی مورد نسازید، دربی با حضور تماشاگران و بدون هیچ تغییری در استادیوم نقش‌جهان امروز برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139391" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkScJWT0xHJMH979ldV2mVCvIHISioHvirzW6nMWTVlR20bZXOA-oHJ-JethLGg_3pkcPoegcYph-Wx-FsboRqxx1OZo1SZbfCrLLNxh8oo8INJWQ14rROrmD0d9IitgOVw-MH6OUiJ8aZzF8F19QBeiLGgmP9NuLsFgNq2bIm5S_MaAmzDhsfYrAefq8Pjvd2J6-Rq1dCPyi9nY771kwksAZLLrNXDhdligjVKMZpvCPZsQ0jvzXd9pbeJVqOjyiGFNqxTuKkIkgCwN6amXNXqYCg1AvGasuoNf2I_8fPMa9NGLfcuG8TMrNOO7zt6v1hxOqa1CxOZ0edAdsCLA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/139389" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❤️
تکذیب شایعه برگزاری بدون تماشاگر دربی استقلال و پرسپولیس در نقش جهان
⚪️
⚪️
استاندار اصفهان شایعات مطرح‌ شده درباره برگزاری بدون تماشاگر این دیدار را تکذیب کرد و گفت: این مسابقه با حضور تماشاگران و طبق روال پیش‌بینی‌ شده برگزار می‌شود./ مهر
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139388" target="_blank">📅 09:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
خبرهای رسیده از فدراسیون فوتبال حاکی از اینه که احتمال لغو یا برگزاری بدون تماشاگر دیدارهای فردا لیگ برتر، از جمله دربی وجود دارد
❌
❌
تصمیم نهایی به‌زودی اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139387" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇮🇷
صبح روز دربی و پر از استرس بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139386" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIkPwiWhVSdK5EsziHsEd1kakYhMFyme0E92ARfo4z8crZCQwIzInwxlQIo8crVb77L3oEhHfcc-Ya2OqFFxBUykbhCBmrkwmxUjuHRNI88XP5SsnQuCb4sCG9qwmz8_h6rbmNWJ1T5duVkq8XAzEjV-gxLNAnAWHKnd_AYr5t4_XoWrcWrdKN27meFPDHYm_LY21_0CtQigzQzcv0AtIlp7j0F7h4g4MTA76op-tVO1gGXDmOK54UyPtU-klsRrMQms-hWzeuXttH9J5f9EN_k3B6ttU7Oya20xXj3hAQ8c1NQkyHqR9dLSZ18n2rVf5Ude-bJdIQY8GgInntEMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
الکساندر زورف
🆚
لورنزو سونگو
🎾
آندره‌آ گِریِری
🆚
الکس د مینور
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139385" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
فووووووووووووری
🚨
شورای تامین استان اصفهان فردا 8 صبح جلسه اضطراری داره
🗣
سه سناریو پیش رو دربی پایتخت قرار داره
⏺
1_ برگزاری دربی پایتخت بدون مشکل
⏺
2_ برگزاری دربی بدون حضور تماشاگران و عودت پول بلیط به هواداران
⏺
3_ لغو دربی پایتخت و برگزاری آن…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139384" target="_blank">📅 00:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139383" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❤️
ترکیب احتمالی پرسپولیس:           ‌‌‌‌‌   نیازمند تیکدری زارع کنعانی عیدی  ‌‌‌    پورعلی خدابنده‌لو ‌‌‌    عمری بیفوما محبی      ‌‌‌‌‌‌‌‌       علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139382" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139381" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
در صورت بالا رفتن درگیری ها، احتمال لغو پروازهای داخلی وجود دارد و از این رو تیم ها برای سفر به اصفهان باید برنامه خود را تغیبر داده و با اتوبوس راهی این شهر برای انجام دربی شوند
✔️
✔️
البته تا این لحظه خبری مبنی بر لغو پروازها مخابره نشده است///طاهرخانی…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139380" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139379">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
تموم شد
✔️
اولین توقف تراکتور تو قزوین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139379" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=HdqirY2dKq5G7SiTK-rD_0kauYtI-MejzWOlrIgCl8PTlhmjAkgTPes02AjPpBy3_dAxiWnRa50bwJr2pvUOi_pEOFMSUUTJFsHLx6qQSw9f1Cn-ssjivYp5IJo2q82XMzywOt7_jXYpAP44z3FF6F2EpB7TlfJsKSgpeiBBd0lxmdg0ATlhg93EEN7EolKL8Wo3f5ItLpQKqd1dUYysJaEMmdpnvIofe_pAYrrHhAnM3TiGFZL4FPIPfDT_82LoRyXvb1xuRyUkyIBXGMnTp1uByvpL9APbu_6eC2Ynj2D5QuGpSjBNGx5oPQHGwPxQGQcnZDlOSBnCy1X7EI9VQlXTLI4WvgN7Tsm-IiwJYrXGZWC8VKVFhVWUhrvYE-W1zIF3SkwzHxq9p0359lTK0qW0aXHzn_OiRPj3J7-Isy7dZUMp7oTxPtnpiACfIpJDqUnYrx6jD5SjmNxgmPCbp_xDT-lMtDeHhqQsX7WfQCkPNWuQ-Qzq_XQlR9o1en2HxRFuIIHL58AqaFsQ9faRIlEDdcjRg2ONDWIVaWBAhfSDlq6JemE9mtpwkzUWNMFTg4jo2v8Ye5POEykMyoouaBHS1_i_ZpwgK5rwViGpXb-dwRGI-rXpKjAve7GlzAXFzCN3Xj0mZI514OBciG73R4Oz5WD_GnMkXP9fBJrYZ6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=HdqirY2dKq5G7SiTK-rD_0kauYtI-MejzWOlrIgCl8PTlhmjAkgTPes02AjPpBy3_dAxiWnRa50bwJr2pvUOi_pEOFMSUUTJFsHLx6qQSw9f1Cn-ssjivYp5IJo2q82XMzywOt7_jXYpAP44z3FF6F2EpB7TlfJsKSgpeiBBd0lxmdg0ATlhg93EEN7EolKL8Wo3f5ItLpQKqd1dUYysJaEMmdpnvIofe_pAYrrHhAnM3TiGFZL4FPIPfDT_82LoRyXvb1xuRyUkyIBXGMnTp1uByvpL9APbu_6eC2Ynj2D5QuGpSjBNGx5oPQHGwPxQGQcnZDlOSBnCy1X7EI9VQlXTLI4WvgN7Tsm-IiwJYrXGZWC8VKVFhVWUhrvYE-W1zIF3SkwzHxq9p0359lTK0qW0aXHzn_OiRPj3J7-Isy7dZUMp7oTxPtnpiACfIpJDqUnYrx6jD5SjmNxgmPCbp_xDT-lMtDeHhqQsX7WfQCkPNWuQ-Qzq_XQlR9o1en2HxRFuIIHL58AqaFsQ9faRIlEDdcjRg2ONDWIVaWBAhfSDlq6JemE9mtpwkzUWNMFTg4jo2v8Ye5POEykMyoouaBHS1_i_ZpwgK5rwViGpXb-dwRGI-rXpKjAve7GlzAXFzCN3Xj0mZI514OBciG73R4Oz5WD_GnMkXP9fBJrYZ6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
⚽️
❤️
حمله شجاع خلیل زاده به عادل فردوسی پور: من دو سال است که فحش می‌خورم اما خم به ابرو نیوردم، فشارهای زیادی روی منه و خدا رو شاهد میگیرم که یزمانی می‌خواستم از فوتبال خداحافظی کنم اما این کار رو نجام ندادم، دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور
🔻
همه مردم تبریز می‌دونن عادل فردوسی‌پور با تراکتور مشکل داره از زمان برنامه 90 همین بود، الان هم همین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139378" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139377" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139376" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
سهراب بختیاری‌زاده: می‌خواهیم ریتم خوب شروع لیگ را ادامه دهیم و پرسپولیس حریف خوبی است که به امید خدا بتوانیم آن‌ها را شکست دهیم و با روحیه بالاتر راهی لیگ نخبگان شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139375" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
✔️
تراکتورسازی تا دقیقه ۷۷ نتونسته به شمس آذر گلی بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139374" target="_blank">📅 21:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/139373" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139372" target="_blank">📅 20:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔻
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود.
🔻
ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139371" target="_blank">📅 20:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به کنفرانس مطبوعاتی نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139370" target="_blank">📅 20:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139369">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139369" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
✔️
فوری/حملات آمریکا شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139368" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139367">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139367" target="_blank">📅 20:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139366">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaROqY7_cYhJx8ln2tOlqVoagFncu572UotVBTktG_uZbwvyW4mmuVcxE1cwWuTvSyfxhx9A5XJIEImz4QfqRqjrngBA8PguRZYjCdIgA-GA040JxTIvjIgOWenX9J-JmjRWNoJFapEcPrfglXtjoefHTkZRIjq2OVk8Tewewjh8fivGiTmQRmn66ameZWu9gFb9JeNFnBEU-4hRUDtHxxabmzP1yHc9B4Xnt6lWaO2S6ao5M5dF-ItJhm9v5TIORklkqDieML1WiNdDS8Wkw0JtBuNiXxNug5shzdI1LZHSYQYYsgPmpwE439bdTRidDseSdA4BP0MT7XCu67_1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
نبردی برای صدرنشینی!
⚽️
الهلال و الاهلی؛ جدال غول‌های عربستان
سه امتیاز، هدف مشترک دو مدعی.
[
الهلال
⚽️
🆚
⚽️
الاهلی
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139366" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139365">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes   ﻿</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139365" target="_blank">📅 18:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
با اعلام کمیته انضباطی قرارداد یاسر آسانی با استقلال قانونی است و مشکلی برای همراهی این تیم ندارد
✔️
البته خب انتظار دیگه ای هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139364" target="_blank">📅 18:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0P9aUfA0OjD4m28DEZB6dkO2poSzgRi1SFU4NAJUW512xWaPQyn7sxQSgURQrGK-Crtt1ADjp5YDO_reMOVcszi0tcFeK9NU04hCs_50J8u2DdE-RavEH9xX4UBrNVDjbQHpahgGTP69dOoimWHxv4TanS-irqFXQckVo4WVlF9Ht84S-IyHRXB4s5w4oG23MOLf9-2IVYF31Q8-nUKh8RbIk5NpF8jYmQG5-o7LtGq5ZFdiAHqXRUEPlCu8wDKqpN6evGXXxOvrwTdljb9PPRS7paTqNLfxnxf0FENdBD6_mIEpaRlVV_epVfQbj7XXK4QULAPamudIyZyfWMAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139363" target="_blank">📅 17:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQNGBIjtlpzgF3_tTtqqgzK8YaxdENegSp6j6-cg0dyUgK7aXzV1Oi4Ysrukpka4vAf7hlopqpVNMj6bK3Y_x1UTvSxTFGM2GpqhQGg3wWaan1NLhaj5yBrs4Rn0-hiGi8x2zdHj75-IHSC6tTtl03mTcDFze-vx1Mpf4LG1H_Uihh-K5zMonujEYyQ2wXkMMVVsj-B_DfA1Yq-mtSCtP0HVMX3BY5ljwHbg_Xe-623E8b8oSFFvh2o2sSMu7P19NSkJMijp0BEetJnRSW_f-g4LECj0s1NMRTp3Fj8VM2iyy0DRjaqaMFzsvH38Y4-vIzfgBBUgGKs2KQtTs_yd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کاروان پرسپولیس راهی اصفهان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139362" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
کاروان استقلال با تاخیر به اصفهان می‌رود
⏺
پیش‌تر قرار بود کاروان استقلال همزمان با پرسپولیس و ساعت ۱۶ با پروازی اختصاصی پایتخت را به مقصد اصفهان برای برگزاری دربی صد و هفتم تهران ترک کند.
⏺
با این وجود به دلیل همزمانی حضور تیم‌ها در فرودگاه و رو‌به‌رو…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139361" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
تیم داوری دربی ۱۰۷:
⚪️
داور: موعود بنیادی‌فرد
⚪️
کمک‌داوران: علیرضا ایلدروم، بهمن عبداللهی
⚪️
داور چهارم: سیدرضا مهدوی
⚪️
ناظر: اسماعیل صفیری
⚪️
داور VAR: میثم حیدری
⚪️
کمک VAR: علی احمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139360" target="_blank">📅 16:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139359" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
💢
💢
💢
گفته میشه تارتار قصد داره ترکیب پرسپولیس مقابل استقلال رو بازهم تغییر بده و عمری برای مهار آسانی بجای سرگیف وارد ترکیب بشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139358" target="_blank">📅 14:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139357" target="_blank">📅 14:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
هفته هفتم لیگ برتر فوتبال ایران به دلیل اصرار بر اعزام تیم ملی امید به بازی‌های آسیایی ناگویا و تداخل برنامه‌های اردویی این تیم با مسابقات باشگاهی، در آستانه لغو قرار گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139356" target="_blank">📅 14:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpzp_WNGZyUDGe53HsRznOG8HZA_rgP3Qbq3r1hoDPflfS-7yUfQ0zVPg1mSBX8tCBiKmZqs38x8_VY7NVt0NKy-lJdPTu7w0oakITTZcPJm4puWURnK2OXjEddIhvhaFDbxOOpACzwdkw9rPedRQYocVWnoCgPDTgdG_BUkWW1IPQh2N82DIIPVcqSL58IxFHgQicPTlqghURFJgd11LYLsjpNCO2uCX96FPDdqbYkG0S2U2LMPhIFOTyiX6sHXcxFwv-xCCwJ_Bo6uwWmJu2IMBaourdNnCA2LNW56wCQqpAW_rdurMUUmFhNBo72T8BdWRI-Yjb6uROiv7w2Llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبردی برای سه امتیاز در قزوین!
⚽️
تراکتور با انگیزه‌ی برد به مصاف شمس‌آذر می‌رود؛
یک بازی سخت، حساس و تماشایی در انتظار دو تیم!
[
شمس‌آذر
🟢
🆚
🔴
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139355" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139354">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
گویا هفته هفتم لیگ برتر بخاطر مسابقات تیم ملی امید لغو شد
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139354" target="_blank">📅 12:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139353" target="_blank">📅 12:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
تا کنون حدود 40 هزار بلیط برای بازی دربی فروخته شده و ظرفیت فروش پر شده اما احتمالش وجود داره‌ بازهم چند هزار بلیط دیگه شارژ بشه؛ ظرفیت کلی ورزشگاه نقش‌جهان 75 هزار نفر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139352" target="_blank">📅 12:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139351" target="_blank">📅 12:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139350" target="_blank">📅 12:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139349" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
☄️
تماس تلفنی پیام صادقیان با پدیده ۲۰ ساله پرسپولیس
✔️
✔️
ستاره تکنیکی و سابق پرسپولیس قبل و بعد از پیروزی شاگردان مهدی تارتار با امیرحسین محمودی جوان گفت و گو کرد.
✔️
✔️
گویا پیام صادقیان، پدیده 20 ساله پرسپولیس را دعوت به آرامش کرده و از او خواسته است…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139348" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139347" target="_blank">📅 09:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139346" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
فووووووووووووری
✅
شنیده می‌شود سازمان لیگ تنها مجوز فروش 70 هزار بلیط برای دربی داده است! ظرفیت ورزشگاه نقش جهان اصفهان 75 هزار نفری است...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139345" target="_blank">📅 08:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139344" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_19BjfwQlmq3zwlinODPWnazEOv9DEwTT_xbkQrb4FbF63inNXZ6268YIhvn5-zwkWdk427XtM2o-Aqv6uzaZGvu5jWv6fUbhRV4-P6iHko3aY7DYUpfb_pqG6jaFIzwCHI28xz8iKLFr5mb9Nv-erKU-smPBadhCQOOHyrkhidVkiPD8lhOrd_Obhx0G7yjHNSWNbzLQTdfuSEG615DvzoyEXz63QbvC9397YK6kKhG4j3kyOZAvsf5A7QlNm9qBIh7eLIE7PUu2cEf9gf9owoBAcEsAcHAgjVSGzQjDUOSgv6X78E9dXhy2zapo7poBXZ4WUOGVFn5D2WxsmZlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139343" target="_blank">📅 08:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1XaICV9gaXic5FJglkl6N9pVkxUbFN2Doke3eA8vpiCSXvuhTVOnmk6uhd9PanWMI30XIJoYRJPyHersyatmCxotKwpO281SK3YxRgIHp9CiArD45UcJuSwVUdzsQzTgTlNr42nCgR_UpCFXtkAxZSfT1Tu_pM-CykUe8FdewyWf457n1JlPGm_r5DCxUEyVKR2R0Z0Njqv8bkq-DEiYwNo9Oa99pOa6xKj9CnR9LWO8cbIpsonWK485ZJljkXhwqxX2F86ZigubR-LNp7_7INt_TJv3gS-gOohzv7gyXSitmMsN89Lwq2u5tLnTsHRd35NAf166_xDSzCHZjsrPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
بن شلتون
🆚
خریکسپور
🎾
تیافو
🆚
مارتین دام
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139342" target="_blank">📅 02:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139341">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: فوتبالیست‌های ایرانی قلیان می‌کشند
✔️
✔️
چرا باید دروغ بگویم؟ بازیکنان ایرانی قلیان می‌کشند. قطعا فوتبالیست حرفه‌ای نباید این کار را انجام بدهد اما متاسفانه این موضوعات وجود دارد. در ترکیه چیزهای بدتر از قلیان می‌کشیدند
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139341" target="_blank">📅 01:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: حضور من در ورزشگاه شهر قدس خیلی حس خوبی بود/ دوست داشتم لباس عوض کنم و به زمین بروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139340" target="_blank">📅 01:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
پیام صادقیان: حرفه‌ای ترین دوران فوتبالم ترکیه بود اما زیر تمرینات پرفشار آنها بدنم دیگر جواب نداد و فوتبال را در ۲۷ سالگی کنار گذاشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139339" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: بهم گفتن سایت شرطبندی که میزنی قانونیه مثل نیمار و فوتبالیست های بزرگ و اسپانسرش هستند و نمیدونستم قانونی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139338" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
پیام صادقیان:
❌
شرط‌بندی هر نوعش تهش باخته و فقط شما می‌بازید؛ من اشتباه کردم و همینجا میگم پشیمونم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139337" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
صادقیان : شرط بندی تهش باخته و سرابه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139336" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: با محسن مسلمان تو تیم ملی زیر 10 سال با هم بودیم بعد هم در پرسپولیس و تیم ملی با هم بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139335" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
ورزش‌سه: در تمرین امروز تارتار به سبک بازی با تراکتور بازی با ۳ هافبک و ۳ مهاجم رو تست کرده که مثلث خط حمله رو علیپور ، بیفوما و محبی تشکیل میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139334" target="_blank">📅 00:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
پیام اومده فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139333" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139332" target="_blank">📅 00:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=NHnvKeeOv3x5A4A0G3U8Zrhe58Mffe0xLq70nbUPOT_OuT5u9VVJ29XOrdQ68s1RN2QEd3q7KC7eyEYjsOItkikIQfmjhp3ftUPbR7V010tVFycwWMxxdXTVXtQwXIVLad5pyKxbUAqpKqq7DEXRyIwmeaE51GJ92jGnAY3-7HnBS9f48BreSqN0u5MHy0-4VZmKsyRBrHYLj4b5Dup_bEPpYGQn7n3Dy-2LcQIai4HuaGtZOUZjudNjT2R99QxptHZyRuzfaaQGr757oXvYuH7kxpgglkjeip-7r_ZAgmpc10QdhBN1JsL4Cnhqiexyrqm6C48qXCq-HNDUPClwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=NHnvKeeOv3x5A4A0G3U8Zrhe58Mffe0xLq70nbUPOT_OuT5u9VVJ29XOrdQ68s1RN2QEd3q7KC7eyEYjsOItkikIQfmjhp3ftUPbR7V010tVFycwWMxxdXTVXtQwXIVLad5pyKxbUAqpKqq7DEXRyIwmeaE51GJ92jGnAY3-7HnBS9f48BreSqN0u5MHy0-4VZmKsyRBrHYLj4b5Dup_bEPpYGQn7n3Dy-2LcQIai4HuaGtZOUZjudNjT2R99QxptHZyRuzfaaQGr757oXvYuH7kxpgglkjeip-7r_ZAgmpc10QdhBN1JsL4Cnhqiexyrqm6C48qXCq-HNDUPClwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139331" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139330">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139330" target="_blank">📅 23:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139329">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❤️
❤️
اورونوف در تمرین آماده بوده اما وضعیت جسمانیش همچنان بهش اجازه نمیده که ۹۰ دقیقه بازی کنه و قراره نیمه‌ی دوم به بازی بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139329" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139328">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
‏ ترامپ به شبکه فاکس نیوز: ما امشب به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139328" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139327">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
❤️
10 دربی بدون شکست برای کاپیتان
✅
حسین کنعانی در آستانه یازدهمین حضور خود در شهرآورد پایتخت قرار دارد؛ کاپیتان سرخ‌ها در 10 دربی گذشته که به میدان رفته، هرگز شکست نخورده است. او حالا به دنبال حفظ این رکورد ارزشمند در یازدهمین شهرآورد خود است.
✅
پیش از کنعانی نیز کاپیتان دیگر سرخ‌ها یعنی امید عالیشاه که امسال از جمع تیم جدا شد. با ثبت 18 دربی بدون شکست، یکی از ماندگارترین رکوردهای سرخپوشان در تاریخ این رقابت را به نام خود ثبت کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139327" target="_blank">📅 22:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139326">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139326" target="_blank">📅 22:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=W0OUAH0vqoGg1P-ng4DYknVbjDfnTOepNVBu28EOMzIuNs4StkqrQt0X7f6zFzvaOD0JqsVYyJHSQRI7AE2SjjzMBoZYN3nMJrqmek2tZLj-ZVqwzocemM7fLEHr2rsQEz4xWqAkg4GjZqa22vWZnghyrPMOmFGyoc3JN21ADDatlEE5TFXQHUTaJ3oqU2O5es-86L8BUE7TU_rYpUln5OvQl-VjWOGV6AndLX4KiMZp_-y3zZW5ZSLLMvNJJOEr2vlT4Bn25kPdN3UMJRzQ043fbrIqYsK82_aw5Ym3-tD-g7wK-KDvc0oIxAKuZuLaMzD6OUw9D6TFMtkSAgIo6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=W0OUAH0vqoGg1P-ng4DYknVbjDfnTOepNVBu28EOMzIuNs4StkqrQt0X7f6zFzvaOD0JqsVYyJHSQRI7AE2SjjzMBoZYN3nMJrqmek2tZLj-ZVqwzocemM7fLEHr2rsQEz4xWqAkg4GjZqa22vWZnghyrPMOmFGyoc3JN21ADDatlEE5TFXQHUTaJ3oqU2O5es-86L8BUE7TU_rYpUln5OvQl-VjWOGV6AndLX4KiMZp_-y3zZW5ZSLLMvNJJOEr2vlT4Bn25kPdN3UMJRzQ043fbrIqYsK82_aw5Ym3-tD-g7wK-KDvc0oIxAKuZuLaMzD6OUw9D6TFMtkSAgIo6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139325" target="_blank">📅 22:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
تأیید پارگی رباط صلیبی «مهدی ترابی» بعد از MRI اول، در انتظار نتیجه معاینه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139324" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unOVIsAp_UFz3sOimD_DcWYzPQADMqmvbLPfr4Nr0vwA2a5B0-nvg_HdAXV-YrKbRK5PnRSKNvCZYB3_lm-HARIJPFm9dSLx5o8_sIlwflBXnL7OyY9SefyI4OD5vqTiUDeRplXdJUIlXXiKkvS7TifTdG8kf39v-DRMP2skUzWK90Es5Eqdzky-jXrRlDUDOSHQcseNFZWhNQNysjtpEhsu9xa34Y3TXCFsS2mXsxm7rY4IZYy5e5saELppLWjhBT3msz-kZV-DxS8pLEEnDqo1Df1OxaIGkF2t1c8StO2JwyYVx7KE_MCk-qJKgzNEe6vVWY7_SoshOpbUPZq0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139323" target="_blank">📅 22:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139322" target="_blank">📅 21:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139321" target="_blank">📅 21:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139320" target="_blank">📅 21:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد  هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139319" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekc6O9KfeLxRaRl1avyp6htkl04t6EtujbESx7W03w98sWccxSffspFHdE0c7C2XeKT7AnCsfHFLG_iogTVEjvrSgWRCN595sUa2jU6B_W7a5TAZkC7Ed2GsXQmSIapfUnhupu65F95CoIPrfIq9JSzeHDoxhfJtOkgi5PW0xcm1Mxdr-s3EVfJwhlrI6l78bE8a40Hf3vXzdp0qRZlpZ2ktXBGahNyB_1X1mHr_ycD4HIkfPnHbF2Y9FMIvoknivOxgUP9U_OD9dLhNxBaLcIHxbomE6mcoNwLIx6G0yAwp9u_RWDeaV4mafyJBn5liplZIxdHf3PlAQiBa825HQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139318" target="_blank">📅 21:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-eM4ynpFDkXZ29b306a72wjV7A6itnpR1VF2UNViGStO6YWD6k3EFLa0ymoQ5d3J336BDbATSofmDUUPQqRnXiP1swc-aSoeRvuhiIpJMlFQ2MBMNp2XHox90rLoaiRyCgPhk8BGe6JEzQVMHHx3oP25dUBEuWiRmhNhqI9GyCqRjqWNAWTe9qnGscG2caNzOAStv1b_dCbyRy8BuvAfIx6gH61e0xd_zRlIY6fTBjYI9x8MdpM1RoLwVJ44QZgMn7aiH04VWySyNJ1U8S3KtZrlqvYXJsYdSv8z_aio9_LWOxMbBDTatTZzckoIIwO7wB0dCjxKNpon7rGyTCggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد
هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139317" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5LQihSXEEow8WZgn-cMAjMhAOeUpyyt7xDqcUMZtC37ZHvv9YF_zkh3JLZyqTz-yrhOW_CRSGplzhKRF1ITKW80OfM44ThTGasIpooiLNqsqKBUaJp_Y6eX5TQ673RfLlS_Zo0kJKNTPJEqF7F5wvzImWaix84HU3bCCNLBLJoGuZDp24Mi6OJZdTnnifzDICuyKhqNX19KeSs7tKjHAdfYGQgKpewri_L7Db2pw-sVZGQYAsay0ncYtspu5sLhPhVrH12UKXb9j-BZPlT8blYqsNJiO74XdD886Pd5iyJHitviClRO3286S7r1pmcrtsWSHTb817UXeF62t-hC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بارسا به دنبال ادامه مسیر بردها!
⚽️
رایووایکانو آمده تا کار را برای کاتالان‌ها سخت کند؛ نبردی برای صدرنشینی جایی برای لغزش نیست!
[
بارسلونا
🔵
🆚
🔴
رایووایکانو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139316" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139315" target="_blank">📅 20:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
احتمال زیاد پرسپولیس با ۲ مهاجم بازی میکنه و بیفوما هم وینگر چپ هس تا پرسپولیس تو حملات با توجه به ۳ دفاعه بودن استقلال کمبود نفرات نداشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139314" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
کامنت کریستیانو رونالدو برای مسی:«لئو، توی این روزهای سخت، یه بغل خیلی بزرگ برای تو و عزیزانت میفرستم. خیلی قوی باشین.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139313" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139312" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139311" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
تارتار نمی‌خواد ریسک کنه!
✅
به احتمال خیلی زیاد جلالی در دربی به میدان نمی‌ره و تیکدری مثل بازی‌های قبل در پست دفاع چپ پرسپولیس قرار خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139310" target="_blank">📅 15:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
فوری؛ هدایت ممبینی برکنار شد و با حکم مهدی تاج، حامد مومنی به عنوان سرپرست دبیرکلی منصوب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/139309" target="_blank">📅 15:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139308" target="_blank">📅 15:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139307" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYP44Qt2MoJ1dYUOYmrN_C5nxZeEmPuNtE9n5ZtUdyR9H2pRQqJhsAgexxddrUIFigTse3N5VUhjRA3yujsg-0JWp_ndYVAYltKYRwSVB2BTXBpo6AKLC7BL7aL9koBumHOvE83Y_ni12N3foSjC2rthvGirG8gryi_hkdGvjvGZ0i3sFJJ1SbIf58TiVe2X2Rno2LA0CqGQpvqv2hNOmDofekqTUgvtQ48m8ySHeBrGiMR0EBWS9tWXU0cITNiLzzN45qUMyUvc2uBxzu9kixNmVZi-FckLYWuyBIbgZXPYnzXcd78EPFfkOAmfqVWuxAF5j_LAx6kyx9gYMxlGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ویلا پارک آماده یک شبِ آتشین
🔥
استون‌ویلا و آرسنال؛ جدال قدرت و جاه‌طلبی
اینجا هر اشتباه می‌تونه بهای سنگینی داشته باشه!
[
استون‌ویلا
🔴
🆚
🔴
آرسنال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139306" target="_blank">📅 14:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139305">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
حدادی قول داده فردا صبح پاداش پیروزی مقابل ملوان رو بریزه به حساب بازیکنا تا قبل دربی انرژی بگیرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139305" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
