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
<img src="https://cdn4.telesco.pe/file/CZcUB40GwJYFR1MGPcot8LKCw7mXZ3TnJ62ezOezREOjE92vJfbInejwSbzI_iKHN6P02W-KLz0UGvMqjoBpnHdA6GgvZU2yVCAVPXIs8uzB1I1ObVpmKUOiWWVmRpk3Ie8T_P9I_ABysLIb7b30mviY-O-U7chTN34JzpeI2NNpvxSeovkHnmskBJRNgIuK3IN27OZowaOLSo33LxrkNd7pP0K0cxI5cjBECbwMMaRVNh9Q2TRv06Ucf3wpUyqZCoyt5n7hZBKNjZWCbfBPVDsmR5yRuRE80zvdTPeq5wCFYgg4V5B8Nx7TsKIlxVEtkccS-r7lAPLC62d_IwgK2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 17:46:37</div>
<hr>

<div class="tg-post" id="msg-137965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKBMNTaeVn5suJkajwAmtHL07LtyWzYL94QiQclrBp3cWN0rzKUHPvyFQrDRRgpMq4g7Sz7bRCCOaXS1zTwQ6XHn_546x5rFhxJvqJVl5r2kdYtXdn2MxAUv9txyAiFlBuwZF9JXyUS3nW2jFZUcHL_AWiOwlniCMH2HL75iS7S4oPI0nG61_EqTuznTEvntkW3e_YspoEUSldsBbksOga5U7Vtv__oDyCFLLlCVXl4kLNnBvdl5cRtQWOzLZBgSirryT6e1JYTMUwHJA0iMd9-yYjpbm7sgf7_-JW7YnM_XRQRbuBJe5iqLBvGpv2-T9mjHeIe9nV1KRQAKVY1rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
محسن خلیلی مهدی تارتار رو راضی کرد و دنیل گرا در پرسپولیس موندنی شد / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/137965" target="_blank">📅 17:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137964">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
مذاکرات با قربانی ادامه داره؛ ولی الوحده فعلاً راضی به فروشش نیست. با این حال پرسپولیس امیدوارِ یکی دو روز آینده کار انتقالش رو جور کنه.
✍️
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/137964" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmeUYOBZFYqqAoDoRCIHLxvXsMYniS1d-4ZeEchUTXqflNzGPx9TxaU_rjAnBhKG4BfoUf6ZfIalufN5c79EVQ--uSU8wcsSnZd1AqOtZ1_M12dtI_7VfUHJsNc7VNd9BVl1o2ijzrU8o5G0EOrhWKZky4ypEwQ18MJqaHbHA0h8LHsmprjCzScZ73G-e1hLDMDTWTlpShEmU-crskf89d0Vs0EtfAUKRNsl0pKnTVgbmX_c4QsVeGHLx2Y5AH9l6tq5eHqiBxfN_8yw4pNFtF5GPo1AfHOllzIByE-qa07ZuDq_l361HMPNyQkCtM3A-sB8zwhyoOEpIIotvi2ISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
بلیت فروشی بازی پرسپولیس و شمس‌آذر آغاز شد:
https://footballeticket.ir/buy-ticket.zul
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/137963" target="_blank">📅 17:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
فووووووووری
⏺
گفته میشه با نظر جواد نکونام تراکتور قید جذب قربانی رو زده و به دنبال جذب اندونگ هافبک گابنی سابق استقلال رفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/137962" target="_blank">📅 17:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqqUcTt9GD7ceOc49ZdOEWHI0QojaoXHSQ3nf39wL9E-JC0O2smpuzkU_687D3ePfHYv2VkG6LWzYTSRnEnOlSseY6XP4UtGwD8M0mNDZqQoBIqxsRvWNMRAtiOHWndxmO6v5ETGE4VMMl7u_kI1tXdMX8cFurbpX0faxsBXM8f0xWU4NeBx8k4nu9tyNO5oheUpj9CQ8v4SQ3WfEPtyCrEXZeEDrUhDHLuxp28ZfuBvyLVe-uI1ZsFeHZZBDinhAtFOBdk7JNn0wXFX7IT86TIAROGz60PVtjCkMNHdB_DSXnErUue0SO5GiZ7hHscI4CMdfDg6IUcKzXs10Gb1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برانکو ایوانکوویچ سرمربی سابق تیم پرسپولیس بعنوان‌مشاورفنی زلاتکو دالیچ به کادر فنی‌اش در تیم ملی امارات اضافه شد و قراردادش رو امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SorkhTimes/137961" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuXdUw7HqpOt_JpSGnuvaJL6G6sq4e6-5DyOEL2Z4CdKHtQK0DgiTgSdT7hw6JL2YCbmHjpccq9QupCYm00EVr_AnED8xzKK5bfzv2p-WW3yc3COTNrrMzsrHPrZyV6l3QuziFSjDdO-gaV14Pg2W4wpadUc33Df1gocxf_DozaquJiO8OPqSMJaQqYyrdzexW1lSR6yAAGa1IClx81fTq_u9SL7XMgQAWxQ7xuuDWj_4Fr6yNW-HhyePmN1BvObFKJc65MKAJH-J-4yQfYjXqLG-DMoG_rNExTPK5OdtkMNMaHFipsxM4MiiYq0yeXHbCqjzjCAEEe_GZf0mlCE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب ۴ تا تیم مدعی این فصل لیگ ایران
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/137960" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LalPT8zDrHpGQxw5LO_dw7ic9zUwCZbycOFxpwHgOB8L2vOyP-1whwYbhzLQQTfS1Ti6IjNLq0zoVvC9MB8m7e3l-PdipFjzV4v-vNfafq5HnO14zX80j1Ky-DKASDLIVg3fO2T6mr21P-LTQzKs6FtWmZ9gnzTgmXMIMZMEgChPCmAEtqbKNGIFtlZN1j1U-xUsbidsShJm9nAB6092fvaANzyOnfwnoY__UhFJGOrGfRkklZXxq_dZqABy0NtbfzHQ68CdrRBQjS_4PWIx9D_RKSIOGPkBlvq9JhS_Usu_6mSJGNFv5u8LluycwNPKIxa5vHZEwMBVHwkBZuo9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
تراکتور هم از کیتش رونمایی کرد
🚜
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/137959" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
✔️
کوروش اژدهاکش با قراردادی قرضی و یک‌ساله به نساجی پیوست؛
🔴
این بازیکن از عصر امروز در تمرینات نساجی حاضر میشه. / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/137958" target="_blank">📅 14:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137957">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب احتمالی پرسپولیس مقابل شمس آذر:
🔴
پیام نیازمند
🔴
مجید عیدی
🔴
حسین کنعانی
🔴
محمدمهدی زارع
🔴
ابوالفضل جلالی
🔴
پوریا لطیفی فر
🔴
مارکو باکیچ
🔴
اوستون ارونوف
🔴
مهدی تیکدری
🔴
علی علیپور
🔴
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/137957" target="_blank">📅 14:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
✅
دیس بک سهراب به تارتار
❌
❌
سهراب بختیاری‌زاده مربی استقلال : یک مربی خارجی که می‌شناسید و پرسپولیسی است تا دوشنبه به ما اضافه می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/137956" target="_blank">📅 14:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137955">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
❌
فووووووووری
🔴
🔴
🔴
پیشنهاد جدید پرسپولیس به فولاد باعث شده که گرشاسبی رضایت خودشو از انتقال رزاق پور به پرسپولیس اعلام کنه و جلسه نهایی برای راضی کردن مطهری امروز برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/137955" target="_blank">📅 14:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137954">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
مذاکرات با قربانی ادامه داره؛ ولی الوحده فعلاً راضی به فروشش نیست. با این حال پرسپولیس امیدوارِ یکی دو روز آینده کار انتقالش رو جور کنه.
✍️
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/137954" target="_blank">📅 13:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137953">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووری
❌
مدیران باشگاه پرسپولیس مدعی شده انتقال محمد قربانی به پرسپولیس ظرف یکی دو روز دیگر نهایی خواهد شد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/137953" target="_blank">📅 13:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137952">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
علی شیخ الاسلامی آنالیزور ساپینتو در استقلال بعنوان آنالیزور جدید مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/137952" target="_blank">📅 13:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8HLRMG7ylpA6JBJLh59tcAPyYU7K3hjHirUDhpUhQNZ39MahiMzzoN3JWcOgld6xHJWVk8-UdMRQ5bOx_7i6hT3g5Rf2_oB0mWmERfRNcp-9CHH4bJ9vK2ofUcSWdgOqto103jKrJwFDYjSI-SboHm8Vk7cEkypSQgpZIgszMcwhQ2uF-wcWZoEqVK9C1jEf4TcAuEs3ksTAqxC_xWZgfYwiKYNlwr2VhTV_IIAcq4I5pm3ep1b3R4gDiKcuHHuym58kdxw6qKUv_Su2OmRqVsrwXfTL3jXEoy4xxl5l9fLNOzxaM4X49cRg91dvO6N3XWw2M4tSqNvwaRSlzhKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
⚡️
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/137951" target="_blank">📅 13:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/137950" target="_blank">📅 12:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137949">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
✅
🎙
جلسه فشرده با الوحده برگزار شد
👀
واقعا یک قدم مونده تا امضای قرارداد با محمد قربانی چون باشگاه الوحده بسیار خوش‌بینه تا بتونه قربانی رو بفروشه. امروز مکاتبات و جلسه فشرده‌ای برای این انتقال بین ۲ باشگاه برگزار شد.
❌
❌
خود محمد قربانی هم بسیار مشتاقه تا…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/137949" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137948">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
هفتمین خرید از گل‌گهر...
😳
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/137948" target="_blank">📅 12:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137947">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
یکی از خبرنگاران فرهیختگان مدعی شده؛ که پرسپولیس به جذب امیر جعفری خیلی نزدیکه و احتمالا با ایری همزمان رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137947" target="_blank">📅 12:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137946">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/137946" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137945">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
سید بندی لیگ نخبگان آسیا منطقه غرب
❌
استقلال در سید اول در کنار: الاهلی، العین، السد و ترتر تو سید سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/137945" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137944">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
🚀
🚀
فووووووووووووری
⏺
مهدی تارتار امروز برای چهارمین بار از زمان حضورش در نام دنیل گرا را در لیست مازاد خودش قرار داد
🗣
باید دید اینبار مانند سه بار گذشته خلیلی و حدادی مانع خواهند شد یا خیر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/137944" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137943">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
علی بازگشا، سخنگو پرسپولیس: تا سه شهریور فرصت داریم و تا اون زمان فکر کنم بتوانیم ۳ بازیکن بگیریم و اسکواد تیم رو تکمیل کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137943" target="_blank">📅 11:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137942">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
امیر جعفری، مدافع چپ گل‌گهر مدنظر پرسپولیس قرار داشت، اما چون سرخ‌ها تاکنون خریدهای زیادی از باشگاه سیرجانی داشته‌اند برای اینکه فشار و حاشیه ایجاد نشود برای جذب این بازیکن اقدام نکردند
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/137942" target="_blank">📅 10:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137941">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
بهمنی سخنگوی سازمان لیگ: در طول فصل رتبه تیم‌های هم‌امتیاز با تفاضل گل مشخص می‌شود اما در انتهای فصل بازی رو در رو محاسبه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137941" target="_blank">📅 10:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137940">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPI8UpzvWxk8LhEHA-53nFYUjPJviqnhHMUZ8PA_ubvBMO7K1mmoH_tcQIv0J5_1UVj2lCtaZQW7ngfppZ-1C3ux2ckbVGdB4Hy4km8bpFrmxP0izMkWo6jEhxDH-taL2d3EgWsreqaPcahZVyNdE82id3Ex5mtNWpTufBYnQs6qIxJqISMfzxgVPZags22No8-2KeDTltwc60gY9QvK4hUzLkh1KL7YHbh_l4l5EzN6nzvl3oGnXELBTG7XxTQlRfYwhO_kZpVyQBodIzfwiKao5_S6TxJJ1JX3bN5KI6dkYheaWgQyW4GVoC3ThDZ9B7_Il4k-mPvRYy04z69ICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دژ مستحکم خط دفاعی پرسپولیس برای فصل پیش رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/137940" target="_blank">📅 10:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137939">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4GlllvJy0SAnSDZ0D6Ooy-Pc7nDwTNztkfVSqypAcdMb8oses0OyWOf9GzAysxcuoDVsTFBanhLwZT12WPChWrCigln4ndEH074RizfvAINoBkHMI7J0G88Bg3B3tMGKDLV5ZYIB7VGNcCDldDvjuFDqAuvdlkVB8slLr9aDCH0qIj8YPcLIkHw9_A3JhO3f0C3xFnt-vc-vzqJh-Lb3Qf9WQpwlin3Zat9o8PQA9sBNgqZ0S8QyWz3DotzNtmQHBr85yaO2i3EnRgVCWsu1DsDf2U-yE6lCCpIL59ElrWH6VDA9ZWjGp0hbLGHCoKYkR7KgTnlCFaSXNOwRqKmPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
2️⃣
روز تا اولین بازی پرسپولیس..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137939" target="_blank">📅 10:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137938">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی: تمام قلب و توانم برای پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137938" target="_blank">📅 10:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137937">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/leLwA6GjjNTWEWGM8UfDPpEJdhIfLi1TZssmVsc55YzF6q3d9t_EVaKymhd9Kf0bhwnhLHXWVpuzP_VD8kvKRdAEFH8iFthf656HbFHsJGB-hHnoco5keXBw1HjuCmW69stU3EUckS46UP0ZYv9VGVgfCRibBkc3CWbAlkXcZptqigEYKQI1hQBJmkgaCAom2IEmI3WGbBOx93JTsAEeG1FodqRZEdmbf4ATZlz7JmOI8l_WFpfpma0GY65tKjpszCAM9HzQfJBQdHW1YmwuDmn7M_6tMerY7_vG5hIgFhEW65yWARCMdCby--hfMNBn80JItH60Aov3DBnRiPAz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
هیچ بازیکنی به اندازه امید عالیشاه برای پرسپولیس در رقابت‌های لیگ بازی نکرده است. او با انجام ۲۲۹ مسابقه رکورددار است و علی علیپور با ۲۳ بازی دیگر رکورد او را خواهد شکست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/137937" target="_blank">📅 09:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137936">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
✅
🎙
جلسه فشرده با الوحده برگزار شد
👀
واقعا یک قدم مونده تا امضای قرارداد با محمد قربانی چون باشگاه الوحده بسیار خوش‌بینه تا بتونه قربانی رو بفروشه. امروز مکاتبات و جلسه فشرده‌ای برای این انتقال بین ۲ باشگاه برگزار شد.
❌
❌
خود محمد قربانی هم بسیار مشتاقه تا…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137936" target="_blank">📅 09:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137934">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
رسمی: با اعلام باشگاه مرتضی پورعلی گنجی و سروش رفیعی از پرسپولیس جدا شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137934" target="_blank">📅 09:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137933">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlbGMsp567yX37kQRwEQg3HxAPMicBTT1VkkAXnPiY0DUFg-zkIIhC0g1DKJzeiPNKeIMd5a8rzr8OGq8DUOPHMp8w9s9QaDwi7JuWFMo8MU1NdcYmr5zAJT4QNGRJ-_qQSlyOHNhNAao-eai_WR7oq9dvc_SoW1gk5rjurVAJW_AIjdpNH_8XutRoQdm3YCQOW35d8y2By6lo3B23gnrlnxZFYGy2MX4iBt4Fka8yJfqr_gDTM8maw3kJSC-4tejE3O-ZmCafm3NRO5GC9fxcKaRNc3ryGRRIBOr2qQBhYQf_Z899lVws0AdsNjpW37BGcWFFUd0DCEE8WmmdUhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137933" target="_blank">📅 09:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137932">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwclEFFOpl42XMYMD9YJVaw4m5-6scKUz0JzGHLisrhdb8OsLEMvPSvXtwQa7vX0qamFkEv89vZMm2CcN3f9qGFlDCAu0aVgEK1jr_knuWMv91Weija8xrJfjOWeeWbrIE-6UzMkosA_aYXEwPO6NFsF6wLXSuXVo77-FkHWy7njGJJ4wHD7EvRt7azrhmPkzL9lxiYgByohXOW6pT0RmFGxGILOAkMlVrJniEqIKENQ-YS_RKDWAjeDhGXeSF6oQyuk5cwHNeXMkce4Dbi4782zXVU5PNWsWIN2B3Akn9XD5aLqzhSduOudz5YTYTF2-MBUEDTdGPLwymttdszv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
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
-
مزیت روش ورود از طریق ربات:
👇
• ورود مستقیم به سایت
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137932" target="_blank">📅 02:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137931">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#افشاگری
👀
🫦
دیروز بهروز سلطانی خوابونده تو گوش یکی از مدیران بدنام باشگاه،قضیه از این قراره اون بنده خدا به بهروز سلطانی گفته چی شده آقا بهروز مصاحبه میکنی علیه من بهروز سلطانی هم زارت زده تو گوشش
🚫
البته قبلترش این مدیر بدنام فنونی زاده و سلطانی رو به دفترش راه نداده و بهشون گفته چیکار دارید اینجا… القصه سلطانی هم نامردیه نکرده تلافی همه این داستان هارو یه جا خالی کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137931" target="_blank">📅 02:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137930">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuNRnJiSpSxKKQmYlB-2hhEREINxVPghAkhtohCTrA0FyZPApxUlNmE5deCTUB6Jjn3-Jq5RgqzKzt5fP508d3r2BB8JbOmrUBdVRFrtUE7tIxXv_WtCGnC1R8a-hYgjdAPlpkLsAVZkuiAKFSs65dRLu0UI3fFmcLal5cCtARtZRsQz-B3nxVMdbDhJ3zOrnZ-nuBXGJhokaw6LmqFVoFBuXoHCXuQvOa2KX22coZz1tP4lqOyZUROUK4jaAg-g6EDhgQMRNIwO9KXL-DZlYYXVV8iabISr-iW0oXeOvQkUjOAyJuTibLqNGrcO_WFFlyVoLaLQnPlyG-FcwdwA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبتون بخیر ارتش سرخ
🚩
🤍
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137930" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137929">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137929" target="_blank">📅 01:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137928">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🤝
🤝
🤝
🤝
🤝
🤝
🤝
🤝</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137928" target="_blank">📅 01:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137927">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137927" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137926">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
فارس: عرضه بنزین با نرخ آزاد پالایشگاهی توی کرمان فعلاً متوقف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/137926" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
✅
🎙
جلسه فشرده با الوحده برگزار شد
👀
واقعا یک قدم مونده تا امضای قرارداد با محمد قربانی چون باشگاه الوحده بسیار خوش‌بینه تا بتونه قربانی رو بفروشه. امروز مکاتبات و جلسه فشرده‌ای برای این انتقال بین ۲ باشگاه برگزار شد.
❌
❌
خود محمد قربانی هم بسیار مشتاقه تا…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137925" target="_blank">📅 00:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
منهای ورزش
🚨
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماً آغاز می‌شود؛
🗣
طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87…</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/SorkhTimes/137924" target="_blank">📅 00:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137923">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
منهای ورزش
🚨
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماً آغاز می‌شود؛
🗣
طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137923" target="_blank">📅 00:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137922">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین سید جلال حسینی به عنوان سرمربی پرسپولیس ب انتخاب خواهد شد و کمال کامیابی نیا به عنوان دستیار اول در کنار او خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SorkhTimes/137922" target="_blank">📅 00:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137921">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
خواکین گیل دستیار سابق کالدرون در پرسپولیس قرار است به عضویت کادرفنی استقلال و به عنوان دستیار سهراب بختیاری‌زاده انتخاب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137921" target="_blank">📅 00:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137920">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
امروز جلسات بسیار مثبتی با الوحده برگزار شده و قربانی به پرسپولیس خیلی نزدیکه/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137920" target="_blank">📅 00:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137919">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
#فووووووووووووری
🚨
خرید بعدی پرسپولیس مشخص شد
💣
💥
⏺
طبق اعلام منابع خبری نزدیک به باشگاه پرسپولیس، مدیران باشگاه پرسپولیس که پس از نهایی کردن قرارداد دانیال ایری به سراغ جذب محمد قربانی رفته اند با باشگاه الوحده به توافق رسیدند
⏺
حالا باشگاه پرسپولیس در…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137919" target="_blank">📅 00:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZs7_7MnliU8Rs55ODcd3JXlaap1-uTwJHt_pT5pCz_rhypmHCaxPCfxLShhYHapJVoeUXTvYmD1A3OXhnAN4sMirvw7CkDSd7ASNAnE-6HTeXtfjZbbztPJ4EDjIXllAv7UKM9I1CJw8XZMsCSTWBmwkLP45e0B53TpM6Q2jEkhH8-eW7utHnPE7b9PyunFzqKxJEje3mqlSkQU4q8zpZDrQmpYSi3oeuKDQTJPQ9kPJhWWHXa8ydushkH27YfHjMWGkqpCnJppAbI4C7pZwh3hNgl_8I3Og4iG7aINlElq1LFlzg9qLsfCw9msWhCn8LLx2XJYUnMtr4i_PR9U3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی شیخ الاسلامی آنالیزور ساپینتو در استقلال بعنوان آنالیزور جدید مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/SorkhTimes/137918" target="_blank">📅 23:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚡️
⚡️
ایری همچنان در تمرینات نساجی شرکت می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137917" target="_blank">📅 23:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137916">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137916" target="_blank">📅 23:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137915">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137915" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137914">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تسنیم: قرارداد دانیال ایری با پرسپولیس پنج ساله بسته شد و مبلغ رضایت‌نامه این بازیکن 2,5 میلیون دلار ثبت شد که پرسپولیس بتونه بعدا ازش درآمدزایی بکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137914" target="_blank">📅 22:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
منهای ورزش
🚨
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماً آغاز می‌شود؛
🗣
طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137912" target="_blank">📅 22:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
حمید رسایی: دولت میخواد قیمت بنزین رو تا ۲۰ هزار تومان افزایش بده.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137911" target="_blank">📅 22:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137910" target="_blank">📅 22:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
ادعای رسانه مصری؛ ژاوی گزینه هدایت تیم ملی ایران!
🔴
رسانه‌‌ Smashi Sports مصر، در گزارشی مدعی شد که "ژاوی هرناندز" سرمـربی سابق بارسلونا، در فهرست گزینه‌ های فدراسیون‌فوتبال ایران برای سرمربیگری تیم‌ملی قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137909" target="_blank">📅 22:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
خبرنگار: چرا کسری و دانیال رو خریدی!؟
🔴
شهاب زندی: من وظیفمه برای این هوادارا بجنگم. باید بهترین بازیکنا رو بخرم و باشگاه رو به سمت درامد زایی ببرم. شما نساجی را در سه سال آینده ببینید. قول میدهم بیشترین لژیونر و جوان را تحویل فوتبال ایران بدهیم
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137908" target="_blank">📅 22:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
پرسپولیس هنوز به دنبال جذب دفاع چپ است و شاید سعید کریم‌آذر مدافع چپ تراکتور که به چادرملو رفته به فهرست سرخ‌ها و میز مذاکره برگردد./ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137907" target="_blank">📅 22:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
شطرنج پاریس و استون؛ فقط یک برنده! یکی برای تحمیل قدرت می‌آید، دیگری برای شکار لحظه‌ها؛ ۹۰ دقیقه کافی‌ست تا یکی رویایش را به واقعیت تبدیل کند.
🏆
فینال سوپرکاپ اروپا  [ پاری‌سن‌ژرمن
⚽️
🆚
⚽️
استون‌ویلا ]
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137906" target="_blank">📅 22:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137905">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🟣
با اعلام مدیر ورزشی باشگاه الوحده جدایی محمد قربانی از این تیم قطعی شده و مقصد بعدی این بازیکن یکی از دو تیم تراکتور یا پرسپولیسه‌.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137905" target="_blank">📅 22:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137903">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
بازیکنان پرسپولیس امروز زیر نظر کادر فنی، برنامه‌های فشرده خود را دنبال کردند.
🔴
در این تمرین، سرخ‌پوشان پایتخت پس از گرم کردن، به اجرای دستورات تاکتیکی و فوتبال درون‌تیمی پرداختند.
⚡️
نشاط و آمادگی بالایی در میان بازیکنان مشهود بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137903" target="_blank">📅 21:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137902">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEI0GZb8wPIrADoRsimpPWixPqolkLdmJ4MJxEf5JTwalk3_DUf3oEXABkps7JDFERYjbRD0LBdjIw2EV3Ue1cwTSAjQX3tELv8wwpOP2Bj9haBYahfyGZKCLh-TdbmMJ0T7B2mQTV9jWySLPTPw5gax54U-Qvm_NcYlcSaKEC8yyNizBWy5LxO9beM_r6oGjfW_Fy8Q5Zlna56jslj11c3FER9qqeWsnhJDBa4JYqjI8P8OJEsWKTZUyO0zUjCwoyqMKjp6bFzjBm0VOXA6l92UvjgqtzAZ66LF0D4FqzGFa8Ee7r06eLJdnl8TYi6C8ZeJ01846s0fXVzHrLVQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازیکنان پرسپولیس امروز زیر نظر کادر فنی، برنامه‌های فشرده خود را دنبال کردند.
🔴
در این تمرین، سرخ‌پوشان پایتخت پس از گرم کردن، به اجرای دستورات تاکتیکی و فوتبال درون‌تیمی پرداختند.
⚡️
نشاط و آمادگی بالایی در میان بازیکنان مشهود بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137902" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137901">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
باشگاه‌ الوحده ‌امارات: دوباشگاه ایرانی برای جذب محمد قربانی مکاتباتی با ما داشته‌اند و بزودی تکلیف نهایی این بازیکن نیز مشخص خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137901" target="_blank">📅 21:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
ممد قربانی برای دهمین روز پیاپی در تمرینات الوحده حضور نداشت تا خروجش از تیم اماراتی قطعی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137900" target="_blank">📅 21:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137899">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx6IrQbIXQUwzquUa33l6pM12_1wtJgbQzMHGujHZnI6SVFPx2-RTokLbaLNShr_GMXrupA0w9y8dXvatEjvx8bBqUtS5NhaiRutaRJVvDJnaLJx69ijtqpk0FoX7Lzr74bEJprpBP1Ic2vCf0y25JgbMTR99y49vG-__HOVPJOR8Aqtcd-r0UvciaZbUQGkEt3bSBCQk2_D6tI_kWWpyq0YCTKzv4L7vOO7qjigFAmVvtZFhMytdWATuvGxW-mhpyyYixcpW6NBequS7GQEfWJ8DpcrB-J82MxbvPpGN3dsSyFWnInjcIofaOQQlhViYcuf-Pd5W0WnMvr2-jPvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
شطرنج پاریس و استون؛ فقط یک برنده!
یکی برای تحمیل قدرت می‌آید، دیگری برای شکار لحظه‌ها؛ ۹۰ دقیقه کافی‌ست تا یکی رویایش را به واقعیت تبدیل کند.
🏆
فینال سوپرکاپ اروپا
[
پاری‌سن‌ژرمن
⚽️
🆚
⚽️
استون‌ویلا
]
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
استادیوم ردبول آرنا
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137899" target="_blank">📅 21:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137898">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
❌
محمد قربانی سورپرایز مدیران باشگاه پرسپولیس بعنوان آخرین خرید در بازار نقل و انتقالات خواهد بود
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137898" target="_blank">📅 20:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137897">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
❌
محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137897" target="_blank">📅 20:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137896">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137896" target="_blank">📅 19:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137895">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
ادعای آناتولی به نقل از منابع پاکستانی:
❌
آمریکا و ایران با تمدید ۶۰ روزه آتش‌بس بر اساس یادداشت تفاهم، موافقت کرده‌اند؛ طرفین در حال تبادل پیام هستند تا درباره مدت زمان تمدید، تصمیم‌گیری کنند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137895" target="_blank">📅 19:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137894">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137894" target="_blank">📅 19:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137893">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔄
🔄
😳
😳
😳
😳
محمد قربانی به پرسپولیس پیوست/ پنبه کار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137893" target="_blank">📅 19:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137892">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137892" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137891">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137891" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137890">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/137890" target="_blank">📅 18:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137888">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
گفته میشه که کوروش اژدهاکش بازیکن جدیدمون قرضی 1 ساله میره نساجی..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SorkhTimes/137888" target="_blank">📅 18:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
سازمان لیگ به استقلال گفته کارت بازی آسانی رو صادر می‌کنیم ولی اگه بعدا بازی‌هاتون سه هیچ شد پای خودتونه
🔹
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/SorkhTimes/137887" target="_blank">📅 17:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
واکنش مسی به درگذشت پدرش
❌
❌
«بابا، هنوز نمی‌توانم باور کنم که دیگر نیستی، یا بهتر بگویم، نمی‌خواهم باور کنم. تصور اینکه دیگر تو را نمی‌بینم و حرف نمی‌زنیم، خیلی سخت است.»
❌
❌
«همیشه از من می‌خواستی که آخرین جام جهانی‌ام را بازی کنم. چند روز مانده به شروع…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/SorkhTimes/137886" target="_blank">📅 17:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
‏ مسی در مراسم ختم پدرش
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‎</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/137885" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
📰
باراک راوید، خبرنگار آکسیوس: توافق ایران با عمان و امریکا نهایی شده و فقط شورای عالی امنیت ملی ایران باید اون رو تصویب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137884" target="_blank">📅 16:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3O901Kw_sZ-Ygy091voYfNkZ2X9ejkdOcNnKAElUnsyPY0RtZq27aXgXc9RKYIq5wyijxD9sgQnFz47Nkf6ZdmvaVb8CBMib922y4_80DoRfytPhrGO7K1PIN9iAIUtIDZUq0FOrkuPBGauhJYJUKSJlKSJaRjpRJ9ECemeDzf5qw1Ru7gs8C_wcwwmcEvlHiHsXQGOAcaYmVhbEL3bLEeGn421PUmt_H63YNAFo3EtrgbxRUd5WGrB1T0wmqpEb87PdtCfcRCg2J_t8O7N-9rbP0v5sH3ZNXVFpAVIp5mcKuocqI-pj_bv_DgY7vSuOwR948um2ExaoBwTqhCjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
صدای ماندگار موسیقی ایران خاموش شد
✔️
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، ساعتی قبل در سن ۹۴ سالگی درگذشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137883" target="_blank">📅 16:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
تارتار رسما اعلام کرده به هر چهار مدافع تیمش نیاز داره و اجازه جدا شدن به حسین رو نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137882" target="_blank">📅 15:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137881">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137881" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های ورزشی آذربایجان هم در حال پوشش خبری پیوستن قربانی به پرسپولیس هستند‌.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137880" target="_blank">📅 15:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
تلاش باشگاه پرسپولیس برای جذب قربانی ادامه دارد و به نتایج مثبتی هم رسیده و اگر اتفاق خاصی رخ ندهد، او به زودی به پرسپولیس ملحق خواهد شد / ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137879" target="_blank">📅 15:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
تسنیم: قرارداد دانیال ایری با پرسپولیس پنج ساله بسته شد و مبلغ رضایت‌نامه این بازیکن 2,5 میلیون دلار ثبت شد که پرسپولیس بتونه بعدا ازش درآمدزایی بکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137878" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
#فووووووووووووری
🚨
خرید بعدی پرسپولیس مشخص شد
💣
💥
⏺
طبق اعلام منابع خبری نزدیک به باشگاه پرسپولیس، مدیران باشگاه پرسپولیس که پس از نهایی کردن قرارداد دانیال ایری به سراغ جذب محمد قربانی رفته اند با باشگاه الوحده به توافق رسیدند
⏺
حالا باشگاه پرسپولیس در…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137877" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137876">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
tik tak...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137876" target="_blank">📅 15:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4g_ewrXnSSpZd6QH38cgvD64dCQ4W022olzJVm2RI6o7PH61bNbFfCoQvlKy_QOxReFPfcrG8ZKL57WeFVdZR-ihwEhYaGzt8aKqQgCkMnIgnsF8Xg9MohtdmkTaT6ZnYS9Phs8GOfXuza2VDB__akLwFQQoUdygJFmzLwyzqFqCOcGw65SQqtWyYAokGr-SheNfMD-GHsuykIEymr-XMF_o9BctAPO8m9vN1VFPc6tDgb_rByPw20u1hhjHil7wU87gwxXIdjWCXkveAUIvAS3XoEIBa36zFjeZahwTSHcBytNHHzQKVHA408-kE8kkhYdAPCJipBIntlfVeAyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی تو بازی‌های پیش‌فصل 8 تا گل زده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137874" target="_blank">📅 15:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBGSIYorzQuMp0C52ksJ62MyEgdflrR24XnaM-sfbvhqVt0YFINyR0fkr2k3vXtbCWjpn9plu4TC6cYTP2rDDI0iJtetNklZAA_PRKc4ZUamc3_Cy_csE55D-lj6qrihOa8fVNUMRA7yxLhZa0FwLau-Z4yAppzdmeUUvq0kHRNoenQbJjdTE1qgYUw_C1nH39E3hXEgOk5e74AYuPUuVOSD6vFlYzMsOJD1NvV6--ALChojo0VHBH_NfNy7FkUgb6E3PUnbDYBoG1XPXvVJQX2XyGCkB53JTBmKYUdgx9i4cp-UbzfHO2KYvoivlyzZaEPqRAPFNPOPb1DiUCxkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاریس در مسیر فتح یک جام دیگر!
🔵
PSG -
🔵
AstonVilla
⏰
ToNight 22:30
🏟
Red Bull Arena
پی‌اس‌جی با موج حملاتش می‌آید تا از همان ابتدا نبض بازی را در دست بگیرد، اما استون‌ویلا تیمی نیست که عقب بنشیند، ضدحملاتش می‌تواند هر لحظه معادله را برهم بزند. یک طرف قدرت پاریس، یک طرف جاه‌طلبی ویلا؛ نبردی که می‌تواند تا سوت آخر نفس‌گیر بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ بونوس خوش‌آمدگویی رو به موجودی اصلی حسابت اضافه کنی.
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
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137873" target="_blank">📅 14:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137872">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
شهاب زاهدی: بجز سردار آزمون و مهدی طارمی اونم با اختلاف خیلی کم هیچ مهاجمی رو بالاتر از خودم تو ایران نمیبینم
😀
😀
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137872" target="_blank">📅 13:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137871">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
فوری : رامین رضاییان با قراردادی ۱+۱ ساله به فولاد خوزستان پیوست.
✍️
خبرگزاری فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137871" target="_blank">📅 13:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137870">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
بند فسخی که پرسپولیس برای ستاره‌های جوونش گذاشته:
🔹
🔹
پوریا لطیفی‌فر: 1.6 میلیون دلار
🔹
🔹
پوریا شهرآبادی: 1.7 میلیون دلار
🔹
🔹
محمد مهدی زارع: 1.8 میلیون دلار
🔹
🔹
دانیال ایری: 2.5 میلیون دلار
😀
مدت قرارداد همه شون 4 و 5 سال هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137870" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137869">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
قدوسی: مدیران باشگاه پرسپولیس به ما گفتن با وجود عنایت زاده، باکیچ، خدابنده لو ، پورعلی و لطیفی فر امکان جذب توأمان هر دو بازیکن (محمد قربانی و محمدجواد حسین نژاد) وجود ندارد و یکیشون جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137869" target="_blank">📅 12:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137868">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137868" target="_blank">📅 12:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137867">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbdv8ssHvLg9Ls7U-3xm-EeTaoN6V0aIQ9ioy6zMZqM-A9LI-DTPaRRs0o64e__bZIkvz4XP4-0KA5c5uY0Z9K6n1EdhMQy6hG--1ICPoNOXhtls8bB8Zp0BBvvRkpktJ1HuQHlPJWvpF3IYAMg_5Q3RHsoW6-4w_t_tcEIzYosQw4HIIu3Vy1pMxpooCMbOdnh9QddsAn8H8ogyAwxVwo6zhdqQuAdrB-cRvsAt8PUWkYHITz273xmeDTBDHgtnVndFuq94L9fa8Nm-lA7TtQTwVnsT-xxtf9JWn_yxlBp881w4NUQ7AlGbM_hBNo0BvZMqbj5VjhB3OeShPz7uoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137867" target="_blank">📅 12:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137866">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137866" target="_blank">📅 12:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137865">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔄
🔄
توافق نهایی پرسپولیس با دانیال ایری و نساجی انجام شد و صبح شنبه از ایری رونمایی میشه
⚪️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137865" target="_blank">📅 12:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137864">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137864" target="_blank">📅 10:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
شهاب زاهدی: بجز سردار آزمون و مهدی طارمی اونم با اختلاف خیلی کم هیچ مهاجمی رو بالاتر از خودم تو ایران نمیبینم
😀
😀
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137863" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137861">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
خرید بعدی پرسپولیس محمد قربانی خواهد بود / ورزش 3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137861" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
قربانی آخرین خرید پرسپولیسه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137860" target="_blank">📅 10:20 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
