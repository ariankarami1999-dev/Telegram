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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 563K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 00:28:36</div>
<hr>

<div class="tg-post" id="msg-100683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=TwFSCkiTObCrAqSQmXzGYLQJksWcIRmwF7GaukfA__YXLimO5RKEW_OzNt9XaH-iWLFypoeXFAraRG7kVh_UP-5L6axazjgeYCJUppyHY1y7c1xeL_dQCaucEt5lMogUlpdVdzvXTFv2xAN1S0q_NMHoujXG9800kF0TQaK0G40ndamIdoJhMsEnfJ4f8wnrRQVyWHrKQvjZOt5OAuSi_LV1NKutx6pIbjzYYOtyGsBAwrWJ8DR6Grs1nfe2XHHU5ae_-eZvMZ0gnO5_repve5GjAr7gi1HPI37lPVTMCqPJ5GliooB6cIc4NQ-VSwjnFW9cLodtQkUUpax6N1Y30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=TwFSCkiTObCrAqSQmXzGYLQJksWcIRmwF7GaukfA__YXLimO5RKEW_OzNt9XaH-iWLFypoeXFAraRG7kVh_UP-5L6axazjgeYCJUppyHY1y7c1xeL_dQCaucEt5lMogUlpdVdzvXTFv2xAN1S0q_NMHoujXG9800kF0TQaK0G40ndamIdoJhMsEnfJ4f8wnrRQVyWHrKQvjZOt5OAuSi_LV1NKutx6pIbjzYYOtyGsBAwrWJ8DR6Grs1nfe2XHHU5ae_-eZvMZ0gnO5_repve5GjAr7gi1HPI37lPVTMCqPJ5GliooB6cIc4NQ-VSwjnFW9cLodtQkUUpax6N1Y30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدئویی منتسب به حملات دقایقی‌پیش به شهر موشکی لارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/Futball180TV/100683" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/Futball180TV/100682" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5hu-b7jVNAqSFwr7p5RhPMx8tGDTrKLSLWdV259Snng2tr_aLnDQo0byhNEnJrgecMZfmcUxA-1IZ2tY0PCscuAs5FrHaMgPQEgujlg7jlckS5F5Fzgpr7OwN3dFtNrPQujVXwnauPSd7zM3WmqNeCeJ_EDezwVENXynwZ8Nx8ygEsYsZpZ07EnxmSdY1v8bv2f2DPdeTV3nFcZic8kiV6nNJRVywCjbnV9HtWtVJj0nNvokaAq7urhqLM3v8f8eBJMizhWVa_0KwlI1Ek3Uv9u6pQAJe097AMYDZYE1bhb7X7Bl3LGZDHWpG_JHt-bcwOBQp4su4CoffrSkJKOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/Futball180TV/100681" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100680">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKCPV7R14mbYAGFinzjgEP4V9OAyS1qAdAZo9HA62znnI09VWgpJuxctQvA34vpJQLc90gkQL2insFBjFhBdIlRmD8aCIEv0sHy1XR6y7KcPI0xCBf24piVvduugx-r92O9rf-HI23wnoVVj42qCeEVmHwRH8jHtsS_62WEidUDX9w-kjAx5cQ4BuJ2GZgO88znlw1WkLyoxw_7YKw0oiGzb52OzGguJTRY1F48XisI3BEgyajPTq5O5fkPu0tBmfhaKm3LEhksu2UupARJFP5CJqBBkNW0zJBuMrMILgpVXSqeTgN2LT1Hkl0NOmDy8pEwvokNDM2NYm0u7r2kC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚬
🙂
شرکت تروث سوشال متعلق به ترامپ به مشتریان خود اعلام کرده که میتونن با پرداخت ۱۰۰ هزار دلار ماهیانه،توئیت ها و حرف های مهم ترامپ رو قبل از انتشار چند دقیقه زودتر دریافت کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/100680" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100679">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=by0nFb3N9gbdWhciPftpnGgVi_j0mLu5g0r8IeaX8GaOOgfWmeUHlu2lRImJMfNo_xXgb3Oi0PcfGVrJkAN71USXnL5ZdPlidDUTZpQee-ZkCI8bTLET8tyjBZ-3vEAiG7JmV265NCo49AextRUGmoigkJZuz2FVWHr2Zx2gRxmHDUzNEaQvryG6C0XWud7SakqmklxAeg7MgTYijGnjfSfRLn6dK7RDsZ8FaWBCkOKPTGMylOyuZOLOwSZXOnQ-VLSFSjDbma2ZPU5ElSjaBFNBe5trdQl80ki_z1X5BkZ0csWqAH79lQfuxAs1aOgVOjjGrO12jovz1SBVHgwu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=by0nFb3N9gbdWhciPftpnGgVi_j0mLu5g0r8IeaX8GaOOgfWmeUHlu2lRImJMfNo_xXgb3Oi0PcfGVrJkAN71USXnL5ZdPlidDUTZpQee-ZkCI8bTLET8tyjBZ-3vEAiG7JmV265NCo49AextRUGmoigkJZuz2FVWHr2Zx2gRxmHDUzNEaQvryG6C0XWud7SakqmklxAeg7MgTYijGnjfSfRLn6dK7RDsZ8FaWBCkOKPTGMylOyuZOLOwSZXOnQ-VLSFSjDbma2ZPU5ElSjaBFNBe5trdQl80ki_z1X5BkZ0csWqAH79lQfuxAs1aOgVOjjGrO12jovz1SBVHgwu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلد مارشال رضایی
با نظریه جدیدش دنیا رو شوکه کرد :
اگر فرضاً دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/100679" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100678">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMWlookjNMlJivcJxcN1YqjE2EtbCTmlJpukNau_45lrhoqG6I0PF_hRNGvMqKZqCWE85iaE97QsdUqGPB7gxatRlfL7HxzfQY0XufCjTCqjzgK9PZSDompgT5HGZapKKhRVTub8tXjm6H2OoXBBWZi5fjTh6lSklPDUl1CvoAZpTzyL7p_zK9Z6xd3CLtWTV6YJooJ3m6TasaiXnKcXzaSWMJ68uOJS6yBO1Wc6hkcGjuPDuTDeBHOBlCA5BNdVIBltjCibHPiOxNdqHhWSBBHNdLpYvcq1cGwebCVYiH04qYHMeYlVbAaSK9pi61a3P7mbtrHU5y8fIOuCg0R8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
😍
یادی کنیم از استوری رونالدو سال 2021 برای علی دایی: یک قهرمان واقعی همیشه قهرمان می‌ماند. افتخار می‌کنم که این جملات مهرآمیز را از الگوی بزرگی چون تو می‌خوانم. ممنون علی دایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/Futball180TV/100678" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100677">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8e7Gk5unhz7kaSFf5CKGCWmUxCUV-3G79y4-O5s7BQw-pXLgmBIJ_spkL_ShqC0WdiqI1NYpUo4IEkiG2r-7zdWwkcPjzbVgVPea_RV4rT71AYWy8Im1yAa0PUUx0MG0QtuC2xyWHwyXV-3hv0v4bizvQ4JlNEqT2yVPGHgF0NQxn6jMybfA4p9vZgtpk-447naGG12MKuOrrnRUV97iEBXkx5WNRF8ilyVPpXw2EaMIaKnxGARY72NK7NODzOZoTBsKrdo_ZZskiz4soRzNxvbEqCstsVHtgORniaGy-e5WhqKBK_8hOYtIdWGeWfDk1I1TeDFni_JlcdvoT_MoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100677" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100676">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP4ym5rwPEFVjIfGSEYcmPULdmHy6LAWcRmcVSbFX8EOfK4ZYsmVS4E9LetlFa90hIAq-XkSvKeljMlXiYE4ce3BghVhv0JeuOJg7Cm8YRPX3IMV426G_6k3yd7x9TqmuaSCIMP4By5IEkBKAPF73bSylEyGh8u3I0RlgnJDnOEP4Ntq7TxHnFm-dDclMHMVKm19qnwlod2RML21RaS9IOwTIadl1L0nLijmm3IDs0944c9OtXyyqyHARBjQ9fN5xHKQ78U1c_q5U5d0Nxe8KbRnCAFGm1hDfniYtUzP_9nuJzbz3QdiWn-H_WUgj4phgvNEkQzeePndidYkSFgwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
رونمایی رسمی لاکرونیا از اوبامیانگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100676" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100675">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100675" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100674">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRi3AR2VDIpbWXVwZxKQUvk64ELxz47PRbY7J9l5veEaa8q6wFp7fV_64EdiHApNDd8viQgtndmN-ox5-hhfQE2aTxpuVo5msusv4vW_S36NLm4UWN-RP5LPI8C6kkq-iDQ-WYbYlRfqK5bKA1O_GI3ui7M5KQYm1Ntfq_LA6Zs15d7XTiM6Qi50-T5rhDeVgiF3ToJ0dWO82lFTzpfNuYK5FW_Qfdw20mXt6_mo2Uk0QfSe1e3gJ3OstyQHykS6KygYMXIFAHTuFtOfbBs1RTglz_BOsSTOMr5aGdFLymoMh9b0Yfz5-vCk5yp1j6EcfpPyi4O02LfXk0BXCuLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100674" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100673">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INVUjjRydUedMw0JzhYpiZtRDNGawHQ2YEyEsueIUMoEGcmbYZLE3ddMadx3z6uNz0Ikwt2Lv9MiGlyQUzqsUxv0eTdFbf4bNJSwPyngWMQRACHG4psAfg1H7TDP4OPU19VyKX97elDdGeeIGZY5QCwSs9WsUuFaQYGDY_JzDnFHIePLPN7JDNDH3FaUJqU0KNeW0Xzs3NcQFuQqU7JyEWrcOAhOKB5vIb3j4-6nbFWntXBPzmZDhK3d-0Xw77GJTL02sxxDHraHbJ3WgGmWazJswHXRlYtPjCqA73cMz5tcOWXMgBuzFJmxeWAHOuM5r8hVQiSRs6HtDfBIkuZUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100673" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100672">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpheum3ChsKGSI-tS3JEh3PSAWdrstpInEhdkxfCQyD6BvWxu0R3Z3pK3S9HQwNBI7YS1yra1YPp0D2XXlwBcSXMQTDJUUzGRqGJjfMU1fnjvp-UI9Smq0U6FZP4cwYIrLxbAsmMenn3Wi1HimNHs75U7-AyeWduC2nuxMlAqqOv1X6GccarXa9FZAdch-Hgq50mQitEFkioMU--_0_oxPMpYK2hSmdTbLSVlsGsoQK0dUtKjn_q6zI3sQWfRccqZV7YTOi2kTw1XMOKoLWuEiQHz_j6dto4ycGwpP6mDZvEHsMXUtV2N3O2hgP3kaiOITYyvMtAnHb5QbY6vW_kVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100672" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100671">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
علیرضا فغانی: بعید نیست در سن ۵۲ سالگی در جام جهانی باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100671" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100670">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
علیرضا فغانی: برای اسلاوکو‌ وینچیچ هم خوشحالم، انگار خودم داور فینالم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100670" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100669">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZnuI5IU1lEQEABw1rGDgtT0GAaWT_DCctzEX-KMpPXtWPLba-X2gr3fjku9DTXzhFuXrih7drfqLlXvbbg16Ua0xWanpSMOU7Wz--qRoiIu_CqNbmP9MlDSG27ZbyooELzrUQ1mw7FjJB1Gk67yQOUXO-AszZrm2YhmNi3N-9tzmUKNXPrasV-mtCoLT6EXGtdnBrpqtelkHxiGEJ9IsGELHpcwGF9wxdaYw9UKqD55pm72fDGPYu1NQCLf9jhTRMR24UIoNvlgUcvQksgfdK9Vkd1UT6SiTgivITWs7-YjaUCopSWOQ9AfWMnnyAN8iYFkLh1TSMHnwTHMRABlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
رودریگو ستاره برزیلی رئال‌مادرید پس از گذراندن دوران مصدومیت رباط‌صلیبی خود در اواخر ماه دسامبر به میادین بازخواهد گشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100669" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100668">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6PBJSN6EwwT1C8zOrEFmrGaq1xC_DfDGcLhTAGF-UJ73ixMh10AtKfFcnO83V6wXWSublgaKrN4qa9ahjSsCutErIlMCGYGHRGppZgrWyotfmho5gbLEIaoU0BbzwdQ77j0oet3DDAUCNO_yiMZ9EwGM7HB7oMYdoK1bjw6ona2ShQLlZ5OW6U5GKKCyEPH9jyOhrp14WhsyJWmtDHwM-rlVHisRqnx2qGgH_RvMKnXpnHfQxpF_o1VoIlArA3-bL29SvVF7tAkHTXakK4rFEN8bufmpEpy39iaFfPBEzk0BT07S6JOzv2BnhfKvpAZAHMYi8w50yMitNOfNkeBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مکسنس‌لاکروا مدافع کریستال‌پالاس مورد توجه آرسنال قرار گرفته و مذاکرات ابتدایی میان دو باشگاه نیز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100668" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100667">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لطفاااا فیک نیوز پخش نکنیدددددددد
خبرای دقیق رو اینجا پوشش میده براتون :
👉
@khabar
👉
@khabar
تهدید سنگین آمریکا برای حمله شدید به تهران!!!! نمیخوام بهتون استرس بدم ولی این کانال رو دا‌شته باشید
👇
Khabar
Khabar
اینجا موثقه
🖐️
🖐️</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/100667" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100666">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlxjaV3ykxL9I69ys1j2mAfUekLmoaooiV65gjYBB2gkl97yhbquSlAkbKSZxWMk5G3jlfu6FNMaOk_MtDvevv2h-vqdH7PZx_rLGzY3AgchZn25sOT2mqr2CM_OwSUQjem-ul1NJYpF7DI4X3YzamXhXsMIdRJoBv-IMTTGoDoxZd8rMxeaEoj-2arwvCcci5rH6Ips8PHhEojoR2atyVpf8W5T911HJqn1OwfUFkFQbkokUpe9D6RW35InvCV6PGyQ7g0T7PfKPfb7Z8H6HXsRCX0zAqzEAOOR0qaGboeWZbY9rJkrDFitkwpEIYgvo865lle9KG1l7pSwoHT75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
والیبال ایران مقابل اسلوونی هم لنگارو هوا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100666" target="_blank">📅 23:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100664">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLb2htvBtjoHoLIwLTlBlAKr0TQgxJknr59P9YwLRyLDudtuU2Vs6CLWXhn_GP3r4nZTlzTDU8J16L4qV1dPU08W_phPkAFnYoAoCEAFF9n5Jeylv3G9EX8jx9mrDoZ1hH_ypS86_FFN91yjYIPhGm3jcq_a9wpMnrTS4bNSca0hdxeWpvFujv47YiYjZkR3VS3wdxPWRWD7FBFE9b-dkzSMylQQJeDkwXiQsD7-PwwRIwDugjyjprWIeX25aJUC8vvkMQVMZz2YDG1dshLAOn6gHRv1fgS46Z4DJlaT_CmdkTOwQWNO2I8C67fn2eb3qbDy_2W73nTlyBPt6Iuoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wp7OCrW_boBG5MWmy_PvgQKp_uf0EwpUxJTsvE_Fge8WXtFsNNUe1tgjl8v0LQ9ictIbW3jGlmsfTkCFp-7AQEcbaejtsYPfepBmhAPNHcUo6EyllnFg6b7cFvjKPcxnusjdlPOpgtozjgFmxCOWW0nweq3TCeEaVdUjsFSjFQ5Rmg2A1Nm0ovd7Em8y913Fuy_FB70F-TfaKb9SuTFuTJga4nS_JLeYJblkXdzHBQ8dm0AiAAzAvgT9Y8mXqtFgJCAVSnWaqXHTCLAiZ98IdfThnpVS6gq-iYac6UNVWzT4yT7RKjpF3rpjrwIWuE-VSw0WuldT7u885ttCjB5e2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زیبایی کاپ‌قهرمانی جام‌جهانی فوتبال
🏆
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100664" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100663">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu0n4Tla3eFKsoXqk2DxmCJcCdGSd6Y4Dd0En3H3t_hzxvAECsne_-Wkog4FDd2Bw5SOVb2Ly3k1Bn30gi-L4Nx85e4Md958jYGwZxvYGRxJMmAUsqv2rAIHUYkCrjSmCTfG8G-6PWA4cXW8i96W_vSTdSFkhmZjZwV0Ucrq5X2JK3VGiRhgmoWzwVQ4L1QTdIjAVoP1jJKUTSba1BPwDAYoGMawchU4rxOW5BU4OTX05T-yJwnQYwHxVXnC8CJe9bT1UnINRnsa_rB1HWdHgbs6kPTeDG--vufCLY6N4EffItDVkpI_2doGQq7f4diVVf5UaKuyqmRW-34ut15Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حمله تند و بیشرمانه بیرانوند به صحبت‌های علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100663" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100662">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGyN4QD0ClYdTquyeXUMxfGBTjtiHSO6EtHq2RgSGyz9na6YXgi97nWrp9fKrXAKI_JsTkLn1-5GvFxjzVBHdk7Jfju-R7Vl6mQGaw6hd4lgj05scs4LzMcuNMMpPRfx58dk_63TK3I8BmT9G6swrFXXHqC2AT-hVeciTVj4pfd_YYNUZq7s-yhZQ3M8uE-dkiBjpGGkmwKTyoGq0bSKBDbq89QQKjLSuac5rro6DlaY0hcb9Pp6lAsGoM0jZ7EiUEHhcXSa3zfUD6t2gaEvo0mEOWGxuUVaJZpNOZ-VHsEmewumihAsBGSdflvs4xhQuiikoWzOQUfOieq9bG_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
بازیکنان انگلیس هم قبل بازی فرداشب رده بندی تمرین رو دایورت کردن و به خوردن فست‌فود سپری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100662" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGSWMV1TwFrwxZVT3F1HkGLRIwebQvdeChSaJHiTakKvsBWfLd-MOSwSLsyHBvc4IWxagsIpFkhblk7hgIRVSAFsTLO6nuyjKQniZAudFrjrvJIC0Rx5waUpYDwUSDs_TnlYVYEHCdK_7sdjmZNEqNwP41td3Jftq5gYzPmeauB8v6VSwDn6G4EmKeaGIPaWfxklogm-qPjsX7ZD-GXkp7BI50vSoWL-xev18D0ZlA7fuHYTA_ElQrXfaz0XvrdaJlEC0o0rSKHlYsNkEKGrk-TYpjWIsGVYsDzhwzUdCTDx0dY5nEidq9RW9F_kNMPOPf09jkeAE47pHNRMzrH43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلور ناواس:
من فکر میکنم آرژانتین فینال رو میبره چون واقعا داشتنِ مسی یه برگ برندست و همین تفاوت مهمی رو در یه همچین بازی مهمی ایجاد میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100661" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100660">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L52VF8MIIaAd1DaqMV7kDQAjNgdFYpSCuj1wMkYhtcJfLA_g1LWAQwvStcR4srYvkX_gBiD6UH9kb1wHSaFifsVVAvNSvu6ku9ZLi8qlmcn4e2WV6oShCVyY4rsd3jbLn0h6jCblshtowo4KQ1Jk-3k0ddTizlX9F2WD0Mk730RMywplwfx9Q13JD-Y7t7QqKtKC-R-aqzRtiQm93A7gcoW2n_cJOyOUDP8p2dU2bbRO-6QbNosxYyuMBJPtQZvr_esDtHm3LfePl8DWFpqOWF9-_EHO8E_EGAtHZQhHdF_JMIRfI_EeEZXMHj2WQ4HbgiLcytnXSgwDG_4cuvtUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
دلافوئنته:
مسی و یامال
هر دو بازیکنان فوق‌العاده‌ای هستند، اما در حال حاضر هیچ مقایسه‌ای بین آن‌ها وجود ندارد. چون مسی سابقه بی‌نظیری دارد که هیچ بازیکنی در تاریخ فوتبال تا به حال به آن دست نیافته است، در حالی که لامین هنوز در ابتدای مسیر خود قرار دارد. امیدوارم مسی یکی از بازی‌های درخشان همیشگی خود را ارائه دهد. اما لامین هم می‌تواند یک بازی فوق‌العاده داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100660" target="_blank">📅 21:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100659">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu4A3P2k0PIkoWEPJbrxMbscUz8nKpwm6fSfSwwyQUQ3CiwIxGCLbfKIhvMJRs3eiEvOtW1LIKCG-2_iDS7iA0pJyj13-Vwzkg8LZtCY5_k0WdZaQMyZGHhUS9D9Kq_x0FnnU8Qv1kinK_mbp776WmlDCKng_gA9Lfhnpyw3IGPRbGjdoHHK1u5BYR4e5TwuJ1tTTN1QZEPKhpoL3Aq8P-jicx69lMF3URm3JeiZ2jEovyOk-OfnioUGsMXl2yYAjvL4xhMyecr2n3mHhPFirShOoCOpbvj6d1RzfaP4u5UL6kjr1sQ3VXa5jrCJWcr4cPKoJDykvfiiEBdfzvVs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بارسلونا در یک تورنمنت دوستانه سه جانبه با تیم‌های ناتینگهام فارست و اودینزه به میدان خواهد رفت. این تورنمنت در تاریخ 8 آگوست در ایتالیا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100659" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz38XR9vkjyr2KGsWjMJHMhjR7QA4NaNugY_VVSWP1sSH87wNonPWAMVLL4q2tQfZ_f6Vc4fhdV-G3SgUs6xbgQZpruZtBuMCoaOpFO4JQqmufVSNjG-d3h5jZpYJNVkFCOmdYwuS_g4hZpjnqJOYlVGpxYAB0wky6baxiGClE6Y9i03H4bZxJjqUk89YOohw_NaP5mrZi7XfKO7sP-j2AlVagE91u9GrKdLM00FAiRUVVmNKYbCymoPHyDDOjolPCMA0AEUCrwt9ebkJe-f1ttsWgCKKDGs1jphzuWUwHrKYkg5SU-D2uepOqQ_XwmOZfnqRRC8_m5--hnbQFYS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
؛ لکیپ: اولین پیشنهاد رئال‌مادرید برای جذب اولیسه رقم ۲۰۰ میلیون است که تا ۲۵۰ میلیون یورو نیز قابل افزایش خواهد بود و هفته‌آینده تقدیم باواریایی‌ها می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100658" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2KFWHUovQsGKTytz0yY9mAyeIrTLnmoP10wGVBiHdToLaY28kIyKCbEjep1F9gUVY0VMCBUnZGuhlz5pmVB8c9rLodv08vTT-IvuIRtnWL65vOKbX-aIoqNp02GEHaoJS2rNSXCi_qx4slJQD4VkuUoUFiBS1kWhmPxzxwo256e5N9vEaWVGdK1cD15WYKoktxkrq1BbH1bn6Wr11oRik1Agklmt9EHYMT_WWB6uzknL9kXyQyLc67Q5ocKMmYwst4dhrDp8FlTMnAcDAS0pNBPMsheqfA8tSf7Zj9UectooBxL4IO-12qqlhmFe6Oz14I4pwljlglpQc01aTsayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح برای عقد قرارداد با بشیکتاش ترکیه به توافق اولیه رسید. دستمزد ستاره مصری حدود ۱۰ میلیون دلار خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100657" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEP2tVekCUGDpt116UqOJQRjR0HAc4glW1hnI_fL86s2Mw9WorUsn_GTliPYkGJKV4Gmgv63kL4raj5dj-GcIdvIWNve4DN2rkMWavYVZFz0zgphQwzboeChOThFbLEHxZL6pdYBshc1zf67zBKs2uWJ-d_s0v9KxrHACQ1y0SDy5W-0L8xez2jmGU0T1JoZKWUoLPWaegccpM5mUkPNbnoGJkOW_UCZc8VA9CzHBUx3U_nwqcub8QvKZ8kowKd6PT4q4y5s54Ldrk8D9CmZifxfPb1SOSYSIB8X2hc-Sq89WqGX6gluvnpcfhdhFoECJ1J1zfvqIBwsD2xRazN-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
قرارداد ادرسون برزیلی با آتالانتا پس از عدم انتقالش به شياطين‌سرخ، تا سال ۲۰۳۱ تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100656" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1mW2AsOXEPJ53696ivlIcbxgaYyldOvdeEKwQ0fXdSalfus6fXKzIMTNf8pB8zrRvqyNbW7Rq9cUNgfRZruglqPv_NzBgIPrIRR7u3MhZD1fWn1DgD8SiUkGyFbGPjPLLPut9uoCY129GDThosXNNMOD4dSDEdGPdRAQ3v0ndqJbRFf4zHzvwFnYY-iQixJWVBICqJPKGpCgk2lzfRac0wn5Z_nQeEI-ZgLANkq2P0XwBo-Y1XzrW9WKXjDa-RfFPiHLw7D0P8z0MuVZtexhn-NOFhIJj0YLT52Jx6DLIhFKCT20FL4FS0rBWKwbfC7Tf_zTXDlWkZfYLMWNA9pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
طبق قرارداد زین‌الدین زیدان با فرانسه، این سرمربی در یورو ۲۰۲۸ و جام‌جهانی ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100655" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7DR4Wbw86Kq1poFZZOFqsrJp5ifpcWNhZPnhX6Qd1UDGY9SFhLZ249NuIGTF8JcHNmLJZ8DOuDYng6HC4_eYBdvC5t9Z1IGIJjhsc_xqINI5_oPSTT_ZoSU8NBJ51KqEgaNgM6g04zH6DV2AMPVHUH92UkL9bfchn66OQCjlg-95-rp2TZPxaK_ZuOi7duaJrXobYiE8kZwNvFH9pBWHRj3W-PUfEg16Ea_Sfz6vOLbIw4gRULWZiB65UQhiCQO1UKmwHRLD7IZ_d_lM09pbgPJvA0jDbqPSUIOQxcNyIRZ4uAUzytdpmO7mtVKjDXk60Qz0cW89ZoVyqCwSS6rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100654" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15sksOK_Aa-cSLwgRIXGFy6CzSz0kA5Za1IWT2ZTEGYlCkxqOx39dwWgjykrnTnye1nTurGWVoWC8dG_ehawfCOkxVQTJbb8DBCJrC7P1BnJbAUkNDjUN21Eh59k5Vni7TeQDc3Faju1cnEshJVRIybCz1FKEkhc0BB7cpI0XBMy8vQ17r5v0NoKkFcWHZqJI3xccZT39IrVwS9IMtXdQABDhkNHxj7Oh0DNqjhHKxb1roLoXaJM2CQT95HfNT6HzgYjBuZrcXOu8mS9c3kkeIBfvddK5uTtA_xOrwpdOyQba3W6nLh4bwhuXItQaHsxYympMOMIzvHozNl5rzKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک‌خوردن انگلیس فقط به این جام‌جهانی خلاصه نمیشه؛ تو چند سال اخیر انگلیسیای لوزر تا میتونستن کامبک خوردن
😐
🔺
2018: 1-0 مقابل کرواسی
🔺
2020: 1-0 مقابل ایتالیا
🔺
2024: 1-1 مقابل اسپانیا
🔺
2026: 1-0 مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100653" target="_blank">📅 20:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o01iWjMqcFYTWNX-b2xGYlmemMttL-a-IE9tKgvM97Dve5_aPZvchtID_pdUF6mxa4hpT4ZTk7jB7TIXMeb494tO1ccedkk3FyxzGkIp3C7e-aRzyU7Jjn6W2HcTorrM1jQxr7cLGlOkdDA3J5VyAOINKgtpCcpoP9m-Fwfn1jcU8s9jNKFe5aw2th6P5uxLSIGerZ7FJaUyqQliHmYVtB4eIPvMXrXCFoHg11qq6tCGqSRDK_bUPeMXxS2vs4JMG5jDry2QqLbiQ45kq-QY0RfLUy1rvMYF_xI3v36VsUT1R7E7yZsZTb7arWpIIe-KV7TPxAoUwxOEabn4pVXCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جیانی اینفانتینو در انتخابات سال ۲۰۲۷ فیفا آرا قاطعی داشته و به احتمال بسیار زیاد در سمت ریاست فیفا ابقا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100652" target="_blank">📅 20:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fttlorP7P-Opy6iDB9BJghG22Kq1Irno1j8PYlRE_QpV86d03gfg0a9cCKIJDi06jtnUJnaUX8j0WflvYwwxPiX4qLCCZm1Y5tD6rkjrrvlBzasJxejpu2w5GjF7meCYp-vZst_xlQ2g5opsesFZGA3a299JMkGFVoF7UwexiUa5JriKP3fPFdTBnmoR2DXjC1v9S44trowBQOILt07boVQML4QSq-qD4kRRa6dEFd1iiblAqoFkvddg9MN8HhhpD8x6_Qj-vJft5BuncUDkvhScxdJDsyEE1ioYcxiIvrOiXBMJZL9AzXNJ-DKQaqfwP_tEJK698UXnRE_tG0-mVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBLg3p-EQ4rqBF4tkWrxcd5lehL0RbNZKPzewTlK00r-mT-j9TK6YCJ--awV-V9XngwTz9iGEzO3FtbuYkckIYcZI255V4CuKIuUuBpypuJOkfTqS3KUTq00TcGl2RvMTSRETMdHcw9eQDe3SJkBwGbfxWQikcslqQkbfUeB7xRN6pb9P7Zh4OESrvmgB2AWwLQEvrPIwZbJ6LAEZ42Jb0mbY5ZvJ1IiLkGiCNG4HKqzojIVM6Vl-V-dcHOEUEDI2lLERQnLtHY4-7O1yhhW2yByEd5dGi3WCx-JyDI5TTQcx77HkV5vKEYehyd9qXfVodcaIx3mdqimEAavVEBOew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🏟
جام‌قهرمانی جهان در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100650" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYQPnh9gWP6EmoFSHryCJoWL1F-bVtEnchHB5jNy1siWGp7_LO_vyXKQbKlJ9jgWQPCXMC8uEgYLCTviYDeFcjdsypI53z2H1hBGqLhsiDseOnwgFSY84fLpgYNrEKND3JQTFz5fTfQqyuRVofbvPfzFpVUy9GVQUKNMeuQ6XU0Vri5Nm6_IyBGjTbqORoLDOVrjikw8hGBR8m5DJpIQe0_CtfSiODWvDXKl-awxpcITR704i8-M-5MQFEQF11jeLqF-yrf68xrJIOKWuoMsxC0zpGnkf4q4tu2j7frIVgR3nm9EM8s6gNsaknfMyF4TpmK1FY8j9CfAPqUlmZ4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یکی از جالب‌ترین اتفاقات در فوتبال:
- آخرین بازی که دیدیه دشان به عنوان بازیکن برای تیم ملی فرانسه انجام داد، مقابل تیم ملی انگلیس در ۲ سپتامبر ۲۰۰۰ بود، و آخرین بازی او به عنوان مربی نیز مقابل تیم ملی انگلیس خواهد بود، در ۱۸ جولای ۲۰۲۶. بعد از ۲۶ سال، این چرخه کامل می‌شود.
✅
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100649" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100648" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR_1Q9VZWjGZiPiyxn5hUz6qpfesOUfWd2v_z-xD-GPKzDoINkdniEjIE8xVpsOOJl-2ztrINN4OM99HzghMxgPrJ0xiE4buD3mFZwLeiZYVJHkA2JOITuv4tgeyKIpzCajieqprDUxgw4b9o1Qs7yXawcEXPGbw98fm6pNZIX35VBP7YjP706JkGMupFw-9l9VlLl8DtPiNiAWxyZRnFrHmUVL0dYkpvJ3oitcX-Q4ptW0hcnmITpiltrGJlN0Gfm6Knx0iUQeTEHcRD-35ZROnGzbGhyOG__IkkWCCS352ldswg_-xre_XqNfrjxWgzb8hxTFnEoumn_DEZynDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100647" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbOtOE4kTncDUXVt8lYwisL0egQCBU7pmgQ_KNAMBeV_Te8tjqSj2vekcb5LWP3DCedfLi8wrMp6kfqbW23L_T2E-c5OAKHxs4s2W0ivO5hc_CW1yGXKqpOsyK6_oszZ31CCYqMa73GAYPJhLxtkUC3AWBKnuJ81YP5U1h4qRtNXoCX0w_IuMf4iA0T_OQIl_oLv-A20GeNez90CDB7cjSzXWodOr5M9Yjk28Rk0i9v1rJMFY9uQpL3q_WSlEQEvqcszhYanf_FtQ8-kir6ZQzX-O4-swipdwf5u5i9QjZ9yQNP13ZRGACnRiVB5NT2h7FM3HWt0ht8o3PP_as5DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا رسما اعلام کرد نمایش بین دو نیمه فینال جام جهانی 17 دقیقه طول میکشه و نه 30 دقیقه! خود نمایش 11 دقیقه است و باقی زمان هم صرف جابجا کردن وسایل میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100646" target="_blank">📅 19:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بهترین جایگاه برای تماشای شادی هواداران آرژانتین پس از صعود به فینال جام جهانی فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100645" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G76Mj_1W1r-t_zHtbGZpJB0gssODKeaVqZoy2cxT1nj64eVZJw4EkxnOW_n3RTkaU_lpNlZKwLcqgVySiM5a9Z1kbHLuftXcayK6TZktpFtkUK6N107KD_l-maydwSc_pBt5GBBxLmvGt2STI4yN8CKrN3AIPjJqsr5OlpuKEc1JqccJE75mGo0mojYyYwNw-tMwRYOpg7z1T8H5bmu_GUt5UjYg7HTw-fwIhk786m0h9CjXoclnpRkwctulDPnCHJQlB_62oHqZDOFdef-pdia1XZo4j5UNhxBAQskVKQylUVWTBvaOcvfiFTMw8EiO4dgLTDpiQPfnG7OoNmPsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آرسنال به دنبال جذب مورگان راجرز،  پیش‌بینی می‌شود ارزش انتقال راجرز به آرسنال حدود 100 میلیون یورو باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100644" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
در سال 2020 جناب وینچیچ داور فینال جام‌جهانی توسط پلیس بوسنی و هرزگوین به اتهام قاچاق سلاح و مواد مخدر بازداشت میشه و پس از تحقیقات گسترده و یکسال ممنوع‌الکاری مشخص شد که این داور بی‌گناه بوده و تبرئه میشه. حالا پس از  ۶ سال این داور با انتخاب فیفا قراره مهمترین بازی عمرش رو سوت بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100643" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1kR6gdTMlxnVnYpoU3aLWN3_SlZ9Vblcw02ujVaNfTMrpXp-S9KvlPso8yApwE8UUD9sVOIZiBHFU66HQcNj09dYvaWQOehgjR45u3gXb7xChbaO6YNm6GW_el7bD9WwzjuR8xTMEd-gjaN2KuRwk33X4DJvnWhcKoQEBjXkEnw49k2l5NlhVOX-vc1E964vbY1FqjJ6MnP5g6Ob5JMpK2RIZizj4ae0jqvk05OdKaPUaLbqwo-BHuOtEBzkQB0qJP0a4hJimJIdy2d7BpNoo5YHxv9F8cVKkNlF8Lr6rCFrZ5iv8k71wU6BwerTofRV00eJdozEbqm9Gys9r5x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJ2vUtdGqlLg6hZfK2gvKjiPdatyuRL5yzxMRI_brSI8YI3whwP_-czFzn9DLFFHRt9emFBFNDZhbFPrKCz6Ay6VEb1T2Cr3ReqIIOPbmzlYwSoHJiNApDnUcRmL9I2eIOTZi7DF7BpmCcLQ5hD2Sv2PGrm8lZz33KMc0Mq0klXwKBZen0BLlBHpj0pNBOpP_z03w3AryceTbwQGxqVmZ0ffrTid5TseYCya5aedH4ESDe44DQm9GUIve8E8O0RsePV2embmUMgRXc_z0f_HHnBzvjqoqwzB95TFizoJWjwy9GNCt4aZzDLWVfDYyx3CM2o4gaTo8qOzisrZVlcwTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ووزینیا: من معتقدم که در آینده لامینه یامال، مسیِ نسل بعدی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100641" target="_blank">📅 19:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA7ejRhSwAvqkjrluSonhS6xaFtAtvGIS_BnEd0gZ1pVDIDVF8iyDlhwV4zpS_wPs8cOHwDtil5GKwgn5Wz-YhehZhlJ2zdrZvBWDpXbXKmi2pZQhbqzhFjBhvJxExbmpN3AypAuc_P5kih5BJoAfghwJl3IVkMrG_g7FyFoaZdPyVxaMH186TPv07o9A5nwb2BhVd8rtia3IwiBGfC7OF6wbboGiGGOFXRUNMu2QXCcY-5DbNOeUb6gIlj3-NVnKcPmuiLxDA605hVUMnF7G41iyq2iup_rCkgvba6PwROe201sjloIpD8s_GyLWN6sDjp_HDUNVoJ-XoQqcdRcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌‌های‌ملی اسپانیا و آرژانتین در فینال جام‌جهانی با لباس اصلی خود بازی خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100640" target="_blank">📅 18:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2BMWhbhXp557qwaQfV7RPqcfjZ1-Hhs3e_MubC34AbIeneXsIZd6nkH8NITHJVxvINlQTd3kg_cNnkJ2ZlV_gLq1KGui6S68E0Q6y6tV-iGwkw3IrK8MhXJI8kHl3fV_N2FolihKsrFMibNfOS_71nvRL2C3Ty86rpzWKQgAPKtkB2WSQ3cJ1x_BNMYo_SjeFD-EDVludLNHlFyAKWuA1KH_Oo5eKckEJKnAVCvS6nHnrSMZfK7jyh7WyGQCRetmbTHSSgpz5BXacwoPW-q6ngG_KuymfUSDuCtdMy7ii2qPROWTsDjAWyFsL8zn4BOhnw4VA7TUKubeFXjAXb2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو گوگل Marc Cucurella رو سرچ کنید یه گربه با مدل موهای کوکوریا تو صفحه ظاهر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100639" target="_blank">📅 18:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm2Ew1ZdA0zkO5WW34ShEXTrYgFv3WaUmMQR-DVBVw7SnAgqvexTgYzzlaVCceEdnkXnqZrQFNnoQ3v2q5eWAcqrUmmDIVceKV_AffdlgRdGc49i8UnjTxdZUQrx0NyBuTzG8CX8tvLJu2Z-IpHGabzR9gqBEAkUFvenUcx3MduRMbxbJy29IKWUCyNXfpU8Xdg9dOyDjAp4mwll3dufloxSqTugs2z4a3PtTWDV36LVtvavLYdUU4mjiyw3f4ZaTOIDfiPp_J-rwtW6EthEE_iizj_kj6emIKyab60JVPNrIhJK-J6ttbIqiTEUpFm6FlhxYEoAfzGtNhae1EapqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
• خبرگزاری فرانسه
🤩
:
🇪🇸
نخست‌وزیر اسپانیا، پدرو سانچز، که در جنگ اخیر بدلیل مواضع مخالف ترامپ اختلافاتی جدی با رئیس‌جمهور آمریکا، دونالد ترامپ دارد، در فینال جام جهانی 2026 بین اسپانیا و آرژانتین شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100638" target="_blank">📅 18:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
❌
ورزشگاه آتالانتا هم به خاطرات پیوست و زمین چمن این استادیوم برداشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100637" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
🇪🇸
تیزر دیدنی از بازی آرژانتین و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100636" target="_blank">📅 18:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند پیروز قربانی خطاب به علیرضا جهانبخش: من چندین سال داخل باشگاه بزرگ استقلال بودم و نیازی به دیده شدن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100635" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه ابوطالب راجب سرمربی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100634" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJ2srNG5khLszj7cp6H4VlfVV_HQxDoE9jz-oqUdXjiH05oXNhKFg486oFdwZIMJIFcefeT7LFOFtORcsUbzZ2FNyGLSbsSFignpNHxiRDG3wUGiDANg-TwT4q9RH69Tw9UeqPi5bMzJYvXfa7tNT_mTeES7IAp0k8v_G6gP_xK12RzIjTKmX61JId-HAf0GGa61tsu3So8enpcOWEhmdghnI_k7W7fqF6J92NmkyjYGqeOn-Q2p7MFL4rPiQCaqWjgR3I1FDPt1Vy_AZNvpyA-JTaC4M6LFG0PvJ_glSL7Xb_pGGY2RZpOriXft9WHvlLS2-Md0VXWN4Okul1uqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول رسماً اعلام کرد که قرارداد دومینیک سوبوسلای را به مدت پنج سال تمدید کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100633" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
به قول عادل فردوسی‌پور علیرضا فغانی متعلق به ایران بوده و خواهد بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100632" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwqp658mOmx3EuKjwWc5B_II6O4445OMmr7UShV4pg1HsE4wDUMAtnV5ipWP8jZctv21wpyDqRIJZ7UvKBJ3HvvERXSkg_pJ0lY4tntHX0Atx_9nrvEmx9ZVTxBsfnsR1x4YLL7623f3weSDqW1aEPxZG_ajwPv-iDU0UCmTrunNNdCAwrT_N34VDAop9KWzGuWJ75JLLF0ncx6Z4avr0bFfNCMF3CmDBpr4PDqV2Zm6WgRkSmhe1w7d2vyXjHq_sIMZJNyn47WJTVgA36BZN47qUunIzZFuX6RY-o19Lc0yXmnlE_IdcDTLaV1L5aqMa43sA_Pm6_fNcq4M_0nsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
سجده شکر داور آمریکایی بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100631" target="_blank">📅 17:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گلاره ناظمی داور فوتبال: لیونل‌مسی صدردصد باید در بازی مرحله گروهی اخراج میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100630" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشت‌پرده گلزنی تیم فیروز کریمی به پرسپولیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100629" target="_blank">📅 16:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری کفاشیان از تیم ملی: علی دایی با دستور احمدی‌نژاد رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100628" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
پیشنهاد ابوطالب به مسی برای دوران بازنشستگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100627" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
⚠️
🇪🇸
مارک کوکوریا:
اگر قهرمان جام جهانی شویم، روز بعد با لوییس دلا فوئنته تماس می‌گیرم و به او می‌گویم که دیگر روی من حساب نکند و من با این قهرمانی خداحافظی می‌کنم! چون فکر می‌کنم که بعد از قهرمانی در یورو و جام جهانی، نمی‌توان بیشتر از این جام خواست
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-cNLBk4rla9FMMzFPV1NpIPsIpqqIv7_NuDqcc3OQvesYAsjCqUR8TJJjZ5hhcPBCOWWElNFu9eE3235rAGmlNgHoTz0RNIrNAl3e3xyJbWErzgg-yzhD3rxUiEItovX-_9U59cg0BTKc5I0nqs9VPseo9WOMi_YuIAvXEUohKpWZo4Ffr0UQMAc9cuMPwBG1ubd8_PzT4BhyvFBIOxEVO0pXdWBMjtVa3Hoj155aYHgrK6JvfLyP-u_I0AzfZF2okdjyiIo9g2pRCLNHCAn1Q0Vokdqk7uWNah4GTSvEHCWuBx6Ks4Uy4ffxl4CVJprvYzY53osrVa3_pTyn4E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZlBJTHLvNMqZ60o_yous-NehCHxFMGfKaGXgKYxt_4RiKi515MsFRoN4jKtpGvdLtTlwC3kAyudv9h68u3iIQoO5qzc_IgDUbbXtpd1WTyb0KgX7QLCFVgBlAzh1X7UU1YdUaiDY7BuGO4luVvFtVBaQXF15ykycKptlZ8qZBVnAjq-Nh7fYPsE7NYs4NDA9H5hKjArtNuOF_RPRYXT1hEbPL5sqG8FKLbklD6I8bAr9ejByPBAJ8yqqADzla7PzjXxFlbKrf6bek-uupd-Yqwg41fRY7AerSuT90v4Io-zLEGCli-o_0tcqfA72GYDRtwuOTTtwu2ef53WMbBsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صحنه عالیه. عادل غیر مستقیم رید به پیروز قربانی و تهش داشت از خنده میمیرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور بنده‌خدا ذهنش هنوز تو برنامه ۹۰ گیر کرده
💔
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇦🇷
خلوت اسکالونی با خودش در نخستین تمرین بعد برتری قاطع مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
خاطره خنده‌دار شیدا خلیق از خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=Re_uNWbxjh4IpbAHu2Qr90UGOwkVmN-xkLmIQv7RA4ap_QSC0yhKt0jS2ok5KCQdDTvO7UbcoFlTR0fehQYtv8OK3bZg6LeW5cYgyLkVSHILnQaPMdJ3EZQryZDygZ-F8iTzkqbWGBmquSRqg1BX5kt1LUgz0-RIBTYA91xTEZtqDrkxA1D2uujVYsqayGtTNlVuLt_P-Jvfln71z0NwI75k_sh5JplQ8TDN6ikMMQEnaV8feCxLoF5qv7Bsf243-eYfNg9FzMLTe2eNQENnPyvMHadPShpMtN5X3R81h3703VWzny-tMJpPyUGgKicfgqteOQTjoxxb2OKyVruj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=Re_uNWbxjh4IpbAHu2Qr90UGOwkVmN-xkLmIQv7RA4ap_QSC0yhKt0jS2ok5KCQdDTvO7UbcoFlTR0fehQYtv8OK3bZg6LeW5cYgyLkVSHILnQaPMdJ3EZQryZDygZ-F8iTzkqbWGBmquSRqg1BX5kt1LUgz0-RIBTYA91xTEZtqDrkxA1D2uujVYsqayGtTNlVuLt_P-Jvfln71z0NwI75k_sh5JplQ8TDN6ikMMQEnaV8feCxLoF5qv7Bsf243-eYfNg9FzMLTe2eNQENnPyvMHadPShpMtN5X3R81h3703VWzny-tMJpPyUGgKicfgqteOQTjoxxb2OKyVruj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtpQ4Y1nOI8QKRyWntSBVe951mZJKPd4jP1Bd-6fK-8LCvCMJzDoV8K9gPd9cjk4d6WMntFj6G3yDc1xi7lb3MXjshBXNfayyG5AmTMOCZogYzjlHwwzcKcRpRkUlOIxke9Mi_YUeDX8Drbihxrnhfr9CdjKsgm_4xiTbFmduaE8qH6uygWbkxYYZ0VbNKeegndsGThbcQs9Y5o2_Q7DFFM1G0vFnTBFhGljTcsuBsRSLFcYd34JfcB6l1m7xj7fLWsDjwPSwnhW-_aNiSh7uOenCKfMcXtZb_3-gRYRRuKUWpy9oIsjtGcD5oXhn6sm4oaYWWxb8QzPFFQS9riucBBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtpQ4Y1nOI8QKRyWntSBVe951mZJKPd4jP1Bd-6fK-8LCvCMJzDoV8K9gPd9cjk4d6WMntFj6G3yDc1xi7lb3MXjshBXNfayyG5AmTMOCZogYzjlHwwzcKcRpRkUlOIxke9Mi_YUeDX8Drbihxrnhfr9CdjKsgm_4xiTbFmduaE8qH6uygWbkxYYZ0VbNKeegndsGThbcQs9Y5o2_Q7DFFM1G0vFnTBFhGljTcsuBsRSLFcYd34JfcB6l1m7xj7fLWsDjwPSwnhW-_aNiSh7uOenCKfMcXtZb_3-gRYRRuKUWpy9oIsjtGcD5oXhn6sm4oaYWWxb8QzPFFQS9riucBBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پشت‌صحنه تصاویر پیج همسر لیونل‌مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=TT1Pv1u4ohhZ6m48vBZ1-K2q9YQ-7yhPjeqGRzrQdHqC86CAqiOygu6gQs-Sq9v_49CWlUtz6xcCuTrkR5J5dD79E7XPVAW20JJ1ZS_pkN8jhLj57sOxxclGnLp5yDxMTg5doLN8LnNCRQKPouX5tMF9rp6wPUokPPxpTJ3-HOpETev1-bFlXZ8gRcDETGbI56DbjI5tzP69fsf_LgF-b9Qwml8lru9keXmfVJH81VUBzbn2LcaIe7a4i_raHQCFHtYY8Yz6Z5eie9lu6LWTVGb57W7jH5KMPihFactUCt855Uo6bTWV6v9vouajxNJwIsqtKuy0ZNMPN1fcJS_fTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=TT1Pv1u4ohhZ6m48vBZ1-K2q9YQ-7yhPjeqGRzrQdHqC86CAqiOygu6gQs-Sq9v_49CWlUtz6xcCuTrkR5J5dD79E7XPVAW20JJ1ZS_pkN8jhLj57sOxxclGnLp5yDxMTg5doLN8LnNCRQKPouX5tMF9rp6wPUokPPxpTJ3-HOpETev1-bFlXZ8gRcDETGbI56DbjI5tzP69fsf_LgF-b9Qwml8lru9keXmfVJH81VUBzbn2LcaIe7a4i_raHQCFHtYY8Yz6Z5eie9lu6LWTVGb57W7jH5KMPihFactUCt855Uo6bTWV6v9vouajxNJwIsqtKuy0ZNMPN1fcJS_fTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpXJyhKG8Y4SrLaB9ofUjzCAxAc2BAQGU284oSGD1P81eHcmNhI-pYwgmbEU5_qkFvF4SqIyV35_EawJBvees1BFMpSpxMPDhMsPYIqyE89LOWFGVLV0kpzD9ziOs09bzF-ryTOC2SsI5yvps6741j0m5KKw-sn07zoQoqPf46x5FHaH0JY-wpbcab_TLFm43Oiho2ocBqX4hsER-NluFLsPxwboHmWwYHJ97KcgR777CCkTBPccf65YIUvC2xsuoF-jQsRZREm5iCrvA0hdEptK52CDaAnJ9xFRBiyF9hGeK_wjgUIYqs3M0sbPBn-Mc9nSNy_sUPM4abb2nva9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=nwBi2YxKLzfxyb8x-8kWBencA4CBC1Bi16ux86c8eMtypF3L5P2_ebnP5YQXTwDOIMjs1-oYzqikAA1ZJt-JqtCrWiwQg0fPd2EAUsp3VcQ5tw-BlivHTqnToaxzQ4EqiK-YvxroVzNxVXZoMJI5DVaDiGWzXNUHXMCQdbZSmp1-q1rcB0Sxxstlbsn8SmipL2lHwKeQ3Fgc2JI8CVoYy9IUWFnuwhY08LT1L9PTqZNZscRilcBnzDxAfsRQzUQdtiFluO1fTxTzAhiAanoq1ri67sbDZPrY73k198kl4WTxT6IZJ5ZrSoE95zJtMXQTSVTJ7tPhHtk4Vxwf6LM36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=nwBi2YxKLzfxyb8x-8kWBencA4CBC1Bi16ux86c8eMtypF3L5P2_ebnP5YQXTwDOIMjs1-oYzqikAA1ZJt-JqtCrWiwQg0fPd2EAUsp3VcQ5tw-BlivHTqnToaxzQ4EqiK-YvxroVzNxVXZoMJI5DVaDiGWzXNUHXMCQdbZSmp1-q1rcB0Sxxstlbsn8SmipL2lHwKeQ3Fgc2JI8CVoYy9IUWFnuwhY08LT1L9PTqZNZscRilcBnzDxAfsRQzUQdtiFluO1fTxTzAhiAanoq1ri67sbDZPrY73k198kl4WTxT6IZJ5ZrSoE95zJtMXQTSVTJ7tPhHtk4Vxwf6LM36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=s7yzdWscwyBG_zwigaR-q426yW4VKn7R1dlVgVazi_01J77mwMgiBMI9HpWoIW05Xxs1MLSYZuF3On6JolaDTaRTDtucPO7ABFE_udFSOXiwLPgvneZCIsJ3H1Fse-PpKFDy0e03Xj7Ii7v1IwlcUSKNUfqJn2e1bsX5bPdK4KF_8zzyL9ZKdauAxH-8RJ1ybW72aQlwvnx3dKlyZYKDzGX2UhWr6dwBeiPsgZBPz-dDHvPGNM5WpjpliiZ_3fhscdKma9hH7qG-hPT4n7N7NBCKk2u2GQC6OxJJkxRTJMjBaG0gwSakka7UB0iOX9mVH8QzC8q6e5yWFf43geZu6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=s7yzdWscwyBG_zwigaR-q426yW4VKn7R1dlVgVazi_01J77mwMgiBMI9HpWoIW05Xxs1MLSYZuF3On6JolaDTaRTDtucPO7ABFE_udFSOXiwLPgvneZCIsJ3H1Fse-PpKFDy0e03Xj7Ii7v1IwlcUSKNUfqJn2e1bsX5bPdK4KF_8zzyL9ZKdauAxH-8RJ1ybW72aQlwvnx3dKlyZYKDzGX2UhWr6dwBeiPsgZBPz-dDHvPGNM5WpjpliiZ_3fhscdKma9hH7qG-hPT4n7N7NBCKk2u2GQC6OxJJkxRTJMjBaG0gwSakka7UB0iOX9mVH8QzC8q6e5yWFf43geZu6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=oi8wmW1dqPqTCXuTxFsw4xCM0XyY8hj4NqFhv3QZevXhGUodNkdTQV2VUH1awsr4f0XbgvRRhxfQM1rOtbQ9R0NVj_D4UVm1jRMN7pMbM0pqXoPOizv0yaeCChzRfXh-kR_BzJDmLGbjCwddeoq0n_E1Eup1Oc4mcQumSIJaQcImRzsYfZkOQMy3b4bp9yypXsMYyiNEwj7QQ1V5OjkSknXqqe6gLyl-Be0qwUTO4xsfLTrYllucgZ5Fz0VSIt34yF0hYsQSE8vNrUuIrGDu8ilrfrmkyEtQGvZG9zK4kYfIjIVrHNaWlTRVe96jZ3qDzQfmUsb_DqCV0ejjyrrKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=oi8wmW1dqPqTCXuTxFsw4xCM0XyY8hj4NqFhv3QZevXhGUodNkdTQV2VUH1awsr4f0XbgvRRhxfQM1rOtbQ9R0NVj_D4UVm1jRMN7pMbM0pqXoPOizv0yaeCChzRfXh-kR_BzJDmLGbjCwddeoq0n_E1Eup1Oc4mcQumSIJaQcImRzsYfZkOQMy3b4bp9yypXsMYyiNEwj7QQ1V5OjkSknXqqe6gLyl-Be0qwUTO4xsfLTrYllucgZ5Fz0VSIt34yF0hYsQSE8vNrUuIrGDu8ilrfrmkyEtQGvZG9zK4kYfIjIVrHNaWlTRVe96jZ3qDzQfmUsb_DqCV0ejjyrrKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=dxoo5Bq1MvAf8K_4YdnzCcUCD_qNRpxojp-iVB46jRMN4u_URUzv-NJLFKEtsb5TueRjCvdvVDpV1QmSBxYQGUsmwsfI7GkVX8CXZVxvyN6NIToyyPDI2tZOfadDdIhXnSfOMrtbTDNE4rd37nR0o2g3Kxiq0BN8g9MJaztbLsxgsyvC4IdCwC2aGxWVls43fT0cGHpF8GO-eQyXD9FRTQeB3EfWY6wCvMqOvpUXrfs5rz6R-qdPsy_q2p7EyZNkxZ8b10SX8TmEam0aSXmi09lFa0JkT6gT-0FO1fka48DYjTr9xlhc-ovPeTkkXrTMWOSCxHLueOVWYQThEX0f9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=dxoo5Bq1MvAf8K_4YdnzCcUCD_qNRpxojp-iVB46jRMN4u_URUzv-NJLFKEtsb5TueRjCvdvVDpV1QmSBxYQGUsmwsfI7GkVX8CXZVxvyN6NIToyyPDI2tZOfadDdIhXnSfOMrtbTDNE4rd37nR0o2g3Kxiq0BN8g9MJaztbLsxgsyvC4IdCwC2aGxWVls43fT0cGHpF8GO-eQyXD9FRTQeB3EfWY6wCvMqOvpUXrfs5rz6R-qdPsy_q2p7EyZNkxZ8b10SX8TmEam0aSXmi09lFa0JkT6gT-0FO1fka48DYjTr9xlhc-ovPeTkkXrTMWOSCxHLueOVWYQThEX0f9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=sxLhoDiW_5NNRIrVi-JuANJLXl9NBACxAQj_FwpYk7WFUWFKzSEpHJc3NoZSVSK99nHRCwtuBxyN3Fqdh1eZG4UKENTZKF_570iFoMcu6Zsd6RUAcy5dvvdjOZb852USYecJwFKJrPXGjQ5aLsF5_vKHoCvQU7wB-QUqxPxrav8n-_qr6HS_luY04a0Wukr0YK3Y3iPNtpwDwsZVLl5RvXaAVM9pbOBgzEpxKKpsUj9_nTqANyAdZojcIFV0Bw6qxb_0lJ-MY_20NK-jlD56sQOoLlOa9rVr7p4O0umIILTHtzaHDWxe377pM5lXYqkOIy1otc1HbyOgY_hpak01MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=sxLhoDiW_5NNRIrVi-JuANJLXl9NBACxAQj_FwpYk7WFUWFKzSEpHJc3NoZSVSK99nHRCwtuBxyN3Fqdh1eZG4UKENTZKF_570iFoMcu6Zsd6RUAcy5dvvdjOZb852USYecJwFKJrPXGjQ5aLsF5_vKHoCvQU7wB-QUqxPxrav8n-_qr6HS_luY04a0Wukr0YK3Y3iPNtpwDwsZVLl5RvXaAVM9pbOBgzEpxKKpsUj9_nTqANyAdZojcIFV0Bw6qxb_0lJ-MY_20NK-jlD56sQOoLlOa9rVr7p4O0umIILTHtzaHDWxe377pM5lXYqkOIy1otc1HbyOgY_hpak01MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=LHLAXdqaWwUm7optsZiVk9su1VR45LaujXECokwXj1D1RFGU_rojafabUQNVK_DM3MQIrC3c5ZwrzeMMSg8j8EpzyskchQh0bEwUE8YkODHHneitNu-z2z2QAsia-rAiEzg0afuQclFC4Ro7UIxLYpGOISsiiVqfPD9UnAK6PoQK0OolVsfwMLv7XrXGWaSwK2AitrznIFdjz7-GJlmhtS09B0xGNQwitA043DvM8W0INjbSYflEOFVnAr44BYplj5Kr-rICDbLS2lVTLGHD-Aj9oDPUXk4ge5eqlOSNC0zpkS0lBticZStDExDl5Eqmqen3eborDRg0Nq5pJtERrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=LHLAXdqaWwUm7optsZiVk9su1VR45LaujXECokwXj1D1RFGU_rojafabUQNVK_DM3MQIrC3c5ZwrzeMMSg8j8EpzyskchQh0bEwUE8YkODHHneitNu-z2z2QAsia-rAiEzg0afuQclFC4Ro7UIxLYpGOISsiiVqfPD9UnAK6PoQK0OolVsfwMLv7XrXGWaSwK2AitrznIFdjz7-GJlmhtS09B0xGNQwitA043DvM8W0INjbSYflEOFVnAr44BYplj5Kr-rICDbLS2lVTLGHD-Aj9oDPUXk4ge5eqlOSNC0zpkS0lBticZStDExDl5Eqmqen3eborDRg0Nq5pJtERrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=CfauoyHxzg-bkBYEF8zYDWkjb5leh8I8USvuKmKxRvjAZKY3c83MAR-ONFyjk1H44hw_ZiN5k5jSGOODEIFO1CNagEgO8OCOglfq5Q1q3X5SvYIWWweGFjLPAechiQGDJ60-MWv0gfbhzFRw7vSjJK-E_prngGVs_6XAGsN5rOgd_TASG-kO2D5iVdGdVbZdsvMg9F2eLnUkBwPzqBTLayuelkxtNe_yJ8uJ_yPlauS6tQF_kdoGCaloOBYBzvUF9vlezOJWfzwR7ZkD9rHBkwVDjvPb90Wx2S_O0uP9C3jXyB3bkPIEwloLgtMJB4_RRGlR05XenuoshAUoYM-cARU7g9Qq3uS2MoCoR7CCNTrSU3KSrzyBHWgww3dt1znK5erKTUqU52pRDA8wS-FHgdvZ6UHU2Yun5kTb7XvZkzSxQZkfaVy6JJdn6Ieo3HE_IJ_iBeBFmGT6n7DzPesaSW70PYsrw79dnpE2dxW8WN47N3_tAIy8KB4oHXD5jxUwBZhJkdwdD5yHKNre-BvEAy40bmRl_9XYlf-HC3XVMvNIYUGSf1yEKnR7fGvZqcAdbjL936XlpEx8dpRN8NL3LfdtD0k8Cu9CXfPBHhYCFuN29GFLSY1Qa-lwzUDQDN1reuI8oEY3M-_LkvcR8R12r5h06UNapdML9caYO3Yyxts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=CfauoyHxzg-bkBYEF8zYDWkjb5leh8I8USvuKmKxRvjAZKY3c83MAR-ONFyjk1H44hw_ZiN5k5jSGOODEIFO1CNagEgO8OCOglfq5Q1q3X5SvYIWWweGFjLPAechiQGDJ60-MWv0gfbhzFRw7vSjJK-E_prngGVs_6XAGsN5rOgd_TASG-kO2D5iVdGdVbZdsvMg9F2eLnUkBwPzqBTLayuelkxtNe_yJ8uJ_yPlauS6tQF_kdoGCaloOBYBzvUF9vlezOJWfzwR7ZkD9rHBkwVDjvPb90Wx2S_O0uP9C3jXyB3bkPIEwloLgtMJB4_RRGlR05XenuoshAUoYM-cARU7g9Qq3uS2MoCoR7CCNTrSU3KSrzyBHWgww3dt1znK5erKTUqU52pRDA8wS-FHgdvZ6UHU2Yun5kTb7XvZkzSxQZkfaVy6JJdn6Ieo3HE_IJ_iBeBFmGT6n7DzPesaSW70PYsrw79dnpE2dxW8WN47N3_tAIy8KB4oHXD5jxUwBZhJkdwdD5yHKNre-BvEAy40bmRl_9XYlf-HC3XVMvNIYUGSf1yEKnR7fGvZqcAdbjL936XlpEx8dpRN8NL3LfdtD0k8Cu9CXfPBHhYCFuN29GFLSY1Qa-lwzUDQDN1reuI8oEY3M-_LkvcR8R12r5h06UNapdML9caYO3Yyxts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=YuYscneSnC7T4-7_Ja4Lma42R-BRocIcBstAwxjefBSVVhFp8cAgEzvWQUJ6fLngv_upDluevMvHqeoUqzGSDRSNoP1inNwT0zmv2CXkTfE53tKv7P3Xgd0JZ77hr9nnDZDywjC2Df7AdIhupRNscteVf31wabQmulEi3v_9_VoWqSA4SREWSzXiQ5Nzt5YGK0f7y3o-qmLdDS2emmWOrXGKVlJtIF-C4li5Z4YrT08KcpI5OxzwkrSGW_H7iAK1C5eEQmJuJjqIHnCid07dbN76943_wnpQwX0-UxJIryLCFVqxz4Kn_Gv-gPlXlWqI7iOec4kIRP5lo_72Z0kmaXSAdbt67ZZK_rIpXruvZUliu4mEZwjBi0om0bY-YyCu_Inm04njfOHnyQli676Sn0pDCMbS16-1SOohKSrIDQ7tGJ6TZT8EFEXJ0bNFRd8L1GbaZOtofkEnI0NDTZMSyKIPGRXa6lK3hmQTgPZNkW3kQejRs45yd_59FUa2hq16Wk5DT0gFPw-LHp7oPM_7QTjYWoBqvgiC_qDgB7HhjxB6hnSQHB2vUUR5bbenMhGDiZTV0SiUS9o75ULx3MIj1WsCy8339heR2DCIlOJ6Q7zPyiluKIYmOR9XgAbsC5tcUIM-oYxrwl0PC6lhSuknacjZ8qS75nKSIsHFfui457Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=YuYscneSnC7T4-7_Ja4Lma42R-BRocIcBstAwxjefBSVVhFp8cAgEzvWQUJ6fLngv_upDluevMvHqeoUqzGSDRSNoP1inNwT0zmv2CXkTfE53tKv7P3Xgd0JZ77hr9nnDZDywjC2Df7AdIhupRNscteVf31wabQmulEi3v_9_VoWqSA4SREWSzXiQ5Nzt5YGK0f7y3o-qmLdDS2emmWOrXGKVlJtIF-C4li5Z4YrT08KcpI5OxzwkrSGW_H7iAK1C5eEQmJuJjqIHnCid07dbN76943_wnpQwX0-UxJIryLCFVqxz4Kn_Gv-gPlXlWqI7iOec4kIRP5lo_72Z0kmaXSAdbt67ZZK_rIpXruvZUliu4mEZwjBi0om0bY-YyCu_Inm04njfOHnyQli676Sn0pDCMbS16-1SOohKSrIDQ7tGJ6TZT8EFEXJ0bNFRd8L1GbaZOtofkEnI0NDTZMSyKIPGRXa6lK3hmQTgPZNkW3kQejRs45yd_59FUa2hq16Wk5DT0gFPw-LHp7oPM_7QTjYWoBqvgiC_qDgB7HhjxB6hnSQHB2vUUR5bbenMhGDiZTV0SiUS9o75ULx3MIj1WsCy8339heR2DCIlOJ6Q7zPyiluKIYmOR9XgAbsC5tcUIM-oYxrwl0PC6lhSuknacjZ8qS75nKSIsHFfui457Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCg2DEGyUOWTgRRqLkgU87Bfmwu97N480yrAZhwkQcIuSfcvhC6U-M4PS6387PaPU9GnEAMNke8lXPO5XLp-6hSCZjxpmeBmFu5WLUElLw91DflNLl_e5tFp37cBUmg8yK6LxNJ86nPRDV0XFNiw0IqSB9NlxSOtA0ZIRNoZNtxSDdK3-ZONLRzdUHhH_fEfW1FUI6xzZOrKg6hdWX_Ef4UOI46Tzy_FR2sZR78Hu5hlYX5eRr3YCn7n6qPCimdpd4vNYGsEul8LE9QSDDFHujYXg3qyWcQk62pLCi6em9adsWocLiqSMLpxFB0z_L3unz4x3an30HhoaT5h9UvxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=gaj9a4-4y_1KOHuU_Vb04vDBkezSGbAy4GmTLY9Yl4o-LNN2_Z3XGPrkfvenInjuSFTAXQ4uiah1EqFDaQFqelMUjuTpD1epbypKINQGtBsBMI4j5mKVqBJSw3Aze3grP_YuiU4QJ49KDcXzomnk1_xKOwtIaMPirhbiCHuIBzh0WkT8pgPc51vGYZs4qaBqS6uEFhb7gGdmEMs1uXScIVa26deQkfCnz9bHycCXKNtuTawHz7183-3PyBrDDxqEfLtLK0jy6dLohGFVYZ-X5okifYDK9DUTD2EdK2mjuJTgZPgIN5R1D26S_auK3uQy-ARYNVQE-nw83o4WJOi0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=gaj9a4-4y_1KOHuU_Vb04vDBkezSGbAy4GmTLY9Yl4o-LNN2_Z3XGPrkfvenInjuSFTAXQ4uiah1EqFDaQFqelMUjuTpD1epbypKINQGtBsBMI4j5mKVqBJSw3Aze3grP_YuiU4QJ49KDcXzomnk1_xKOwtIaMPirhbiCHuIBzh0WkT8pgPc51vGYZs4qaBqS6uEFhb7gGdmEMs1uXScIVa26deQkfCnz9bHycCXKNtuTawHz7183-3PyBrDDxqEfLtLK0jy6dLohGFVYZ-X5okifYDK9DUTD2EdK2mjuJTgZPgIN5R1D26S_auK3uQy-ARYNVQE-nw83o4WJOi0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr7L8by3-dlgXldMwPm1Y56fHTE2Lh6iC-W-oGjrS3YZoMKx4_dCnRYShI5OkA_dSEKkPesVkyzqUQQjHVqYrLCJDarmzCLwT0P7aGoeFx0mUYaDG63fFSgHxGD7Zd72DWIRmvPsysipfDufFIsZLsngp4rl4FnDGNP4I7RjlpxDwHgkIEy4me14R3FA0rDQeJD-BQ3judT6rXK1RJuEJvrKBUH39kUu2L5O6zLyMyUg-XqOB_4PO3-8EFX-tYF-DdDyS2H6OTGe9UL24C1-e9M1n1kdoSFihLUCoItNHHscqXlc8Lln25vW5k4y2saFR5eU_kDXpGb6_GIu1IigqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZE0nluW1p7sbJsHdyj4FW_XKJdh05dAsriMWCTrGsQpSMGUWZ_I3_txQ_Kvdxmh5dIdyA5-FDuDlfRdzIqWi7dLwIN9caExZyu7G16xAqSGDJyrWQ8Ul836hawZo_2Tmtt1JvQqjoxurMjntL8RNinRgqFMvtwCnB4UXnckzAw4CZlvzx9N9YQEP2s7xsKfFPqEADm0SecsHbOinatnKdKuWIswADHCGgAPlwMfU6rrTd9oPnYdFGGMSKQOe_KcosqYcTCWcS5qP5qVdaYuyUtXE5-9tL5l27ysDz98Bm5NvGoA8U4VmeVfo9rnRedgIAuU4VyZkjdSbjqOR0VjGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5ptZ_wbg-Y6D8AgMYrbeQTT2sBhCFosUmkDyfSOqVflmyF4dufZns84Xkuv5pyQbGo5jVhXWA88UnZ8jGDqQ1HvAsY1TiLlROnTOG5UIjZAoWQ9jefHbDtWB01KvIVsoE_shS4k4PgC94uSa03WDNrk94kGiByJNPrSlnNLWYX05V5M1YGVgNey7OK35ltswRwKgtWCE55F3ZAH-IkBMMWcvHOgb35Jmk-RZ47HT_XlhwHKNUcO0eBEY38GHmwVJ9sbRrltgEb64rAct6NTd6ihKFTY8e0206hlhM8RjD4D-Yz3byf5lRwChBcOdaB7FLAIFqiL-Al4bOcecRsGIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K59S-y7D2LNqQzIKfU8AzLlhQnfAGGpvYumRIUW3XnZsre4wdHwtNJaiz_F1fBULfw_sAgR2HDavJqkdGJTqbjgpInircf1cgfBtcGQToViqZlhZhfkHBRITKqnvcJohaCq6HfuzUHI3UU2WCyQFiTQMNXFoWBVC6YvWNcBdraLa0AAh159SiCHGxt2XTYOCZjhiCPvoe9RAlB0qGJd8LwK4uL3J4b84ItjJB8aJBkj1vo0am-QdhaVU5x13wUhaM13O0wx5djzVmQuKEvB_BDQscya_gApRllxaIGS7nXU0PV_sX7MY7kza0PxQwo1yYeX3jSSWtaN-xMECRXfo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdDvC-TWKqPUcDSmQ-em2ZH2iFXKJVrhUbAul5qF3KJO8geg7NoILag3nvJy9VHk_txeBG9NxWd3CCyROsMhmwCSS9vaMd7USOG_qM-NvsPogb_JsVcC_TOBuQXAOgFvmLkMOEj3KQdyiQYLz6Q6fCdPhEPY-ld66HXncv-Yq4bxgB6ijh2x94BNZGNjgKtIBkrLJ2YOpOtVi0YsIbPkbAJVxTwmJXgJIc6gMn9HgF9UiNsE0dGAb1PrziHfybklWEkfqsfiYP8tvCDUK22L76fGH8AXJtB5UKH3izmNOVAJsPgjcC43u2_ropMw42rADd8mG7i0xd-4JG4GueNfSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
⚪️
12 سال پیش در چنین روزی، تونی کروس به رئال مادرید پیوست.
⚽️
465 بازی
⚽️
28 گل
✨
93 پاس گل
🪄
121 تاثیر مستقیم روی گل
🎖
34091 پاس
🎖
974 موقعیت ایجاد شده
🎖
94% دقت پاس
🔹
🎙
کروس: لازم نیست همیشه حرکات نمایشی انجام بدهی؛ اگر با دو لمس توپ بتوانی بازی را کنترل کنی، همان بهترین کار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=kXZdHtda7QwWfwEK810BiiiR0MfQL0YPbV9UGjfdfxGONEPG8sXG0I-eIUCIkJyX9ajH2PwAjwqSzEC7bMMztByTkzmF2QhwKXkRGraLMKKlZmgpIot8cntP6CdsuDRZnPHkJUB3xR_o51qYAabOrDGx7feOeHmYukaEzgl0uT-yn6SUIyEJowsjvUOUS9y-w2wIIPB0L4fjPct8S_lrgGFL3s7sOq6a_dPiMPmDZJOMmY874INRBLiBxoe1g3ZUH30vNcBbXGYYiMXKZG49NpD4Xg--rk4OoskM9_uUM2b0tLExwaGUNcqYaEZVvzN5g0w4fG314PoocXwK7EVtWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=kXZdHtda7QwWfwEK810BiiiR0MfQL0YPbV9UGjfdfxGONEPG8sXG0I-eIUCIkJyX9ajH2PwAjwqSzEC7bMMztByTkzmF2QhwKXkRGraLMKKlZmgpIot8cntP6CdsuDRZnPHkJUB3xR_o51qYAabOrDGx7feOeHmYukaEzgl0uT-yn6SUIyEJowsjvUOUS9y-w2wIIPB0L4fjPct8S_lrgGFL3s7sOq6a_dPiMPmDZJOMmY874INRBLiBxoe1g3ZUH30vNcBbXGYYiMXKZG49NpD4Xg--rk4OoskM9_uUM2b0tLExwaGUNcqYaEZVvzN5g0w4fG314PoocXwK7EVtWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=hVOJYjRa_rg2eICmeqmdedx9W3lYmDrfbP9Ji9ovSmMOIcQ9R6vUNkVRarI5Y7AciulIzg8cHFcOJDPncUxL2TN_A7OdffFx2zuawGd-QOqKYdrjCiHMn9GmcW2lR3A4-rkyGkUGeuAV5XFPRE4ygFlioFYkUIuECSiOb1IPAW4IpBES2Igvbv1uSF25p8Q1iPhhyBhoAmU65Hwt142vJIEX1gE5oTYUdU8IMvleXExgqycvBO3QmkFhP_Q-jroH_r9c-gsU3N3Q4xeWuUZxf3VerH_pxTYwiNGVId0tPZxFzA76SPkc_0Y3i9MJeWTpjsudLK1sWBljHgteeA3scQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=hVOJYjRa_rg2eICmeqmdedx9W3lYmDrfbP9Ji9ovSmMOIcQ9R6vUNkVRarI5Y7AciulIzg8cHFcOJDPncUxL2TN_A7OdffFx2zuawGd-QOqKYdrjCiHMn9GmcW2lR3A4-rkyGkUGeuAV5XFPRE4ygFlioFYkUIuECSiOb1IPAW4IpBES2Igvbv1uSF25p8Q1iPhhyBhoAmU65Hwt142vJIEX1gE5oTYUdU8IMvleXExgqycvBO3QmkFhP_Q-jroH_r9c-gsU3N3Q4xeWuUZxf3VerH_pxTYwiNGVId0tPZxFzA76SPkc_0Y3i9MJeWTpjsudLK1sWBljHgteeA3scQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=NW1lsj2DLPJr6u81T_d9j-W7gun2jHvt732kW7vg1sEzPXaPRVReiHs4GnNZ3AUfR9NM_eWNcc7EtR0MH8B6hK7EsA2_aA6972Kh24WImi1bAOHfPaWk2nRj1FWZ9tvr3PNGPLpPsjAnhMrwNPeJ9jmnC4xCMEYs-_-mRRv715AKFD_NHMabLJeLfMSq672Qyb5Lypkct1_cGqBskXVmwZ39AyBlfjdNdsRyFKwX1ws8aimLv3xdrfLCMNwrAGxYTIbDgpW6zf-Gpv-HIKSUEcrT1a6RyoVyxQX37Tn_JG0dbuLFgWl_wsUictmPoemNxszWmrL9fbnjfPuxA2YWOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=NW1lsj2DLPJr6u81T_d9j-W7gun2jHvt732kW7vg1sEzPXaPRVReiHs4GnNZ3AUfR9NM_eWNcc7EtR0MH8B6hK7EsA2_aA6972Kh24WImi1bAOHfPaWk2nRj1FWZ9tvr3PNGPLpPsjAnhMrwNPeJ9jmnC4xCMEYs-_-mRRv715AKFD_NHMabLJeLfMSq672Qyb5Lypkct1_cGqBskXVmwZ39AyBlfjdNdsRyFKwX1ws8aimLv3xdrfLCMNwrAGxYTIbDgpW6zf-Gpv-HIKSUEcrT1a6RyoVyxQX37Tn_JG0dbuLFgWl_wsUictmPoemNxszWmrL9fbnjfPuxA2YWOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZBpWUK-c0rStIInSuOu9pR8SC_7lYzcBnn9701h75FLXv0YeRFQAbwQ1FsIPSyMZYCQBvT5gJQAVOPVcLr2Zmg8tLNv2wk5rkVql5SxAQ0bm7Yw-OmpY4_aKda9adNeNlxzyrv-sTtXkCWJqppr8hMp6E58IoF-Kii4gpkSO8JnwvlYHolCHrQ8NgorguXSIB_c_dbAau2vFnJfk-RjvxgveSkdd5fG1e0U2axKvoVF-Fi5K4z-qIfXs8PvSRPY1kbJdvAwmq389BFw8LdTOM31e_E-GIkC3-hctwqT3VnrJxbWqP8lnYmu84GytFfXltlF0KlVOkfjQ6GXaskfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT475oS4_BnoEXtsVTQ4KNfqVL4g_APf9A4HZFJvhzKWiQg51ykLRrEU1VjLIS-99voqX6IJyJYRNzXGHTtEnXGds0OpAFvrU13vLPNTJ4C44CxLY-WfSZntBgcZ7ETtpL3LETY3Ba3hs7bFMDNUAzfkJ62yHIdMzNweOoTa9MprVDMEJTKvMZiMBME140oIbpeswbkZnU9Z_gTLaqUdvn7AafE-kAh5qAyOML-ajChQhuUAId6ciLgvKS8b1xbHquO4iD2DsSFfghXWc6ia-LimXcPt89BE_rtih1t5aW30NFQWjibtA3zZDUZSQ2nDz0pp9G7irZggAYAMeCCjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTx4gi3iWfsAPP68YSnUAhsFCmo88BAlIyAV_YsvZYZAaYwsqibL8pVGwGfOWkQvRxmz7okXb0_k6udsOjgRxQ8sZdTD7JVKTgHCfRT1R34ued-AEFH-S4yb7HDQ7jXwcyqf5yzSbgu5TZ08gM5-NJUHzS3hpm_KQm6N4zkx4kSkogAWJaxqBQTcoFHjTcgboH8yNbMmhpRvA_VvsxgvklAo1meJMtHsqGj_mbVipDaj3alxOm-qvof51nGWi7n_rNujDkHBmMNcDHtltZU-AlQAGU5E2mZ-IRTWubnQyUNLwpzgI3WDKL8mMShlMlwL7OoY_yrlfkpcfJjwk-9qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObibZ--1mU4E21qak1SNG7qhLaz8mRr5D3fQ1ixvG02z5Jecu-uoNRIUQqt6AvzDWdZzVg952hX5LbtRO3mWW3Jikx8WDn5mk7P4FkWifXr8sBMqIJ3C95-rOD2MXA186qjNVZNFN6XJYm0z6Dve7WKsixc1iOFEUaKmueCJ1lYCTlENrErs0VIm7_w5NFBh1GuZBRT2ixDz0N9zjJD1w-O3yuReJs1q_AIK710mS8079yowzbkhzeu0d1eG9JYIdMhdmctRaf4s8U6PcwjaHtk8xC7k7J915Ok3BJeBqOgvR6CC1fRm6uBbZWGCCwSpk6vD-Fzwy4cO8p2oL_602Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5xOHCjE_VDC_n9Wsh071uXRGj9HN-nA4J4hK5KcEJVpti3JQQ6T-fUM0marHbdVRrbHSQWd1CrHAzAH1Ruu-KXOMKRewNZq6IPflsnyxEP6ImHls2S_3U5VMWyAd7e5nmZ-2ad8r_r5azaFWA0oZgwXBHG5u69-hxpEpUcP4HC0aDV-RX_0nr6CmlUUbAVN3kf9fCl_z_Q90O06qnmT9aLXN286-28AuDDb3nzC6bBewHt4iTl8FNk5FJDvnWF0_usUxNFMB8Zvfkf9ps2HOrFv46fMOZxDsOHAAjS2nff51Ij0n7v4pC_VWPxt4JPRwMcLrdj4EDW-HY92HBF3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSoGMAShhV15Nu5xBMj2klrmlGYcN6opDFn86QW1p7-VTY5n4vA0Xxfb4s34tdqSmPP5SVua--qlJhYG7Na2H0MTIld1s6KQHIiUpGgcgroTIlETirMS-a427QXKRodV7fQkl-Oglk-aQaV_nkS0pHQpQS0blH2v2BSoObx07TxNZrXtr7cstl8wexRxcM-Zgt1OQ2yYaIiwoeaCHvyXo5-2cZ5WiaYlL7-FUWzt-Oo1USo41BCjQaByHSv3AkmmFWAR4j1gu9hXl75IomStPIiQU1AP8RNj7uyQPDkWxIU5GLLb8IHhgNyeATPzS9mi66MH9anZwPmEijhpD7KzBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAwNjjX5CalNM9cMpTHM_M0d6kFBvg_3YQOVt_sgal7HMHOW9rXMjeqUiYAS06JdFISQbZYY-Myz7cKhr8ZDH6t0I1lnioIfVGFB8lVx59dxrznC5afESxAOrZw1zLJHKFNeLZNClU5ZiPnQvb4hArAearY5nFpZu42xg0V36wGEvDSf2vMBMY7LoOSa0oDFf_8jyQ4S2FgS1C9eFBGI0B1LU73XFT2WBxuW2c-2JZMOu2Tj9CQIS9D2dcqhIoVD-uTBoNTV4DD3b7wl1X6xyrL0kNIbeebiH9B6ZbF13A3bbP2240lkeIgysXcNEmh9zruSje8uNuRmE42dUMfs9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciwugKfMA6aSS-D1mTkcJKZ3s35qPrr_wd-wWlKbCPEqsyqbe3L9Kn8Au3Pu-YuB4VcCaqR8EegFc1bG3rBGMcm_xZQsCmQ6u1sQ78mHQMWWeeI5L8NkHIeLxiMOJ9JnzrkiGIY-1jGHxGgDlpn61wcsKh1x65tax85-Ahfe9DcHNHbZqK3maz291O34wIEg_KYU9dpA0I7hJFuNXkEkzbOyPWC7BUYljRC8e5amNYK_NtTfVx7Zy9Pbzbh3ZvfiigAmyeC_OnfowSLx9vAimjbey5X_9enINQiuqjOIUZ5aWU6SACzkHzzHELYf8-BbLF7Wj0AgM1FrITc48DSScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6EFUSA1UaSGfVALtBfNP9FPWXF0ymVY-PX1fvKJd8IVO5z0-dTH21fJCyz7o4sM83VqpuQSwBCfMCiFWGDtjg3mxi5Ctwzm6Eh3uPw5kVP3x485P7YkczkQEUvnPihOiKdg_1Ubi7HfOVKx5V7EKL9EU9DFLltfoc9zs2-b7hkhlnc0FoTsSI5KcDzqZ6HDkyAhEDdgTtutbran6m9QcM6w-XUhOvwfFe7e9vJX6B3SxRGga72WOeMrUfyf3ZKFou3RKpEuZ6Gdn9OI7haQWhfQ1cogd4vK7-56wLMT6Hthum7WthUA8a7n0Qo-ibhSnpTiC1PhatadqPY6er1cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🎙
🇪🇸
خوان لاپورتا:
- ما یک پیشنهاد ارائه دادیم و اکنون تصمیم با باشگاه اتلتیکو است.
- بازیکن(آلوارز) اعلام کرده که می‌خواهد جدا شود، اما پیشنهاد ما تا ابد باز نیست.
- در صورت تغییر موضع باشگاه اتلتیکو، ما یک مهلت نهایی تعیین خواهیم کرد.
- ما یک پیشنهاد بسیار خوب ارائه دادیم.
- این بازیکنی است که فلیک و دکو می‌خواهند.
- اما اگر این انتقال انجام نشود، باید روی گزینه‌های جایگزین دیگری کار کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krtHIxRye8Xdz2XV4ASFn-mI8u3q0dORI8PVvn65f-4YJLLP17MrZsj4Vd0ofQvRfEMS6it_Ou4nC6ICiC7k_3I2AWbRd48OzO_8ubflbYeIM0p6yEodFw-HRihRS6zioYzKIJh9Pi_hiAdCCORn9NE1vF_9hYtgByZKXqIXNo0BLy7_n_D6AdOSkRMxEHJLYX6rQtTTGpXYySyV-Pr-NIWGKlbPKl7GjyXT1KCtNqdqB2hxY2EP6gVSO6GIhdG3Fpz23C9rn3dq6OBY1sWbkZCDiIffCEPJefilyB2dT10_b18P-GqBpdgHon5XjYH8pQ_3gJ9pCNfaIqNX9BzZ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx3Fe1W_XDq3mD-IpnEVD7tPeC9fy88lj6gCYdwBaGM6udrhxfQ7wwaVJ7Os6dWylBfaapG1ghxD0VSgI_DB52DtOnEfWiywAFn_ueOl1oxRsWXWuv5BFKYAvHfVE1SYVQsnLjyofGVenEwCxz1jURbiscjJVj6-HbM-r9HgQcxLm33Q0fGjeb72hFydxJn6iKePUOBps8cInt1MlVPSByMSDNnQk6rjlYfNsibBI9kwLrchU2oNi8uf1ObvzIWL0kVPRCL9-cfsy5s-EhyH2GRtD3gPEmssuKEMTGkYviplmCf0OkSXWsV__3E9JdOutnev8SSu7dd0eOV_bzJk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dycE2jMcv2OnQZFE7RlG3_87tbGhRXGY244H6bvDUfQfnokspraPZW7n6WNaz4qnQlCY79qv8m_MmeSpOdTtOlyhZIIDfNl3F7df_Ycf0Cq8ePsTQLh-lX2FWAie5mRcybtuSXGTBotRUEBMfa47sRrGGp48SDSnv_gER7NmIp-SiXbZawOKRwCZpOZwcs45-DgvEgGojI3JhVie0OlVkgrcVOLWwsaQmoWT6qFrJFarer8lun4LKugStwloG_pmqoDNFoGFzfJPPjBHGbfWCwMScngQy0FhmdcDQAnXIQCI-mMYEoL5OJFw0s_H32eKHMfXdSnjAzfZDqw264Mdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiV6ElwjkSVb-rMwL81SmN2KrZJ0tmVf9aCg6_gCfwXtwM5vfqJ3s9lGGug8PDcBxD6ZYja1aihROna8KXTjfi3x2-0fkNulS7lS5gSC48kLdQ-JCTkFCCChxO1HFkVvC1fWkwLh2KjoMCNdEtiMCFqjybn4Sgf7qR018ViViJevOKAzg-9YVcMzdOxx94-cFlDtNRvWwhjRUB3ExPiBymQ8S_GaoqcYKjDBhExKqhf5fja-Mz3sKcwuFooIG_xw-Lb9ITe0WryHZD3BZsA6LtlR84OhjcZqJcPaIWS-MglATK2QMBhFIBgJgcs1r03FwClT2TlButj7347g4F1Tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONkWrQpDM3EVWIbKiWzUA6MLA-DbjZKx22VOPPQkDiGH0IX4_185tPp2EuWD_IKxHn5NXwCPEFM5lfRCp0ZHObstTUIuLVj9zp4qLVLDzPVD_5R4FAqe7ZVdFmtqwb3xafw1uYvvtaOjjzW9CHhb_LgFv2MV1Uatiur3xI88D7rRKpNU4DS1LiosLqu6sSMCXnM0KTK33z3CtWPOXSZ7ipGM3DXINwzZem9iL-D19Nh30v54xWvotgOlenxNARLJPfdZasTJtfAU3SoimnY_3pZtZzQv8Btpl2fhsRMxYX7Oeh5te_Z3bPJ_KyU95EwTYStXDjjciprYT_vb9caPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixvaQeM-c_JkSUecy8i_VhbDaaKqTQUMfeAug98xydet6qV8Wpznbhh03xOmmDqoFLMZb38Cb_h8muQC-zMBpZH-oNxhg9elsn1H8XAZHLyovQQ4CDDgR7r4DIcKbLIWqGuChREAkrb-lBAcu3FTgxc50aZSOe3_iDq9Ope5rUOCNnxwfjmqLz7sayYX_pAUyxvPUia8n1mHiRrSlxOgj3SLsvRYiGAIQX5BXYZ4qtUQHRlrWcv-lWUgkvKe5NN5RtM3rChiEnNNmec9PvOMtOQhqnIc0lzXB-ojYaSxWmif7BAB8fT11cm64kNRhiIhCBD5tgDPr0bOuRAxUdGvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
