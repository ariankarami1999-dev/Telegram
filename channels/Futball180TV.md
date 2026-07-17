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
<p>@Futball180TV • 👥 565K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 15:32:33</div>
<hr>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-cNLBk4rla9FMMzFPV1NpIPsIpqqIv7_NuDqcc3OQvesYAsjCqUR8TJJjZ5hhcPBCOWWElNFu9eE3235rAGmlNgHoTz0RNIrNAl3e3xyJbWErzgg-yzhD3rxUiEItovX-_9U59cg0BTKc5I0nqs9VPseo9WOMi_YuIAvXEUohKpWZo4Ffr0UQMAc9cuMPwBG1ubd8_PzT4BhyvFBIOxEVO0pXdWBMjtVa3Hoj155aYHgrK6JvfLyP-u_I0AzfZF2okdjyiIo9g2pRCLNHCAn1Q0Vokdqk7uWNah4GTSvEHCWuBx6Ks4Uy4ffxl4CVJprvYzY53osrVa3_pTyn4E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbCZPPPjRYbyQ00KX-9_kC1BaoyJWvcF3eKxmTXpJCFhHIPOUM5j0nKuYCF2ctJhyQUkrE6iobAUNRum6ndGC4KEjGKpRlTWUiQlCje7hNeuYxLRNmHDLWahvQoohrsJzGy_pp9gwIqUC4bgx67C4wb-DmaTwUjuc_Yx4xCA6OlgCj9wPvTIA_RMCLQr3OGlc_ciq89IJ1mYgFZjuW8GeFDxm_Mx6MSR4acGMB34pEiMQklsqvQRmJErkNuufbzOHmv_4BGOZ7o-20hSaf3IqNyLS7PJN3-9bH49CkpSxizeXjh4oo-nkGb4J_s78Hp5syrWwBeCevTBiV4epNC78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh0w6D6bBcnkWxPPop5S59BVBqv7aJJ5bJoyVcKeVOCaAYRg7feQmPUz0HFacayvQZiqKkUh4e4NAjjeqIW_BeYPn6GtNpt2L5UytQ6R0zJmDPobBGVf2cI_gEwNIhpaUwYaShYgUWZEP80aIEUsAEwOkTtPYPnMYU5QZ6TzYrOK6HwnAOGmj04UNgU__wJf9_rYppyH6-4KI-Szdsr47REGD7MadLsB7y6vMhnj5KbbRkihxLgwwU4-olp83AANfy9mSF0tm-FpQ-dp7zj3ndqj6b7hATO4OLIJPKnb-Ely0COVMAe17FmqHUO_KEby0GCVoBOrXtRDYv2Yv4MxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-hu-AgAKaqpGN6V4jOaGWnBgcEljykL7fxccrKp6VwGPO8RCmSDF9iJ6GrZAHbvUROg0J6BJnZlJQMDdmCUrNYxg_otgCyobXzyAmmBbOV2SyjW6BqsvcN6729j0lONnZNHW_HqCVE7x6LnJHkyHvEuu3cM_TVk9Gs1wbKSrnfRu-b5y9J2qEpAzOK5--0a21bcv6N2DRTDRkYImPg2G73he53gkCdyuDWHM2cmFO6of1I1QQrMpFHxLZbvBiXouaDFgGbN3Qwmxmvrc8waF89QuDyz4XfxD1P0aeZxmsNck2BLGIPuAwu27jhh-msje9Nkyw66KCUtAH8mTxt9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clev_jEt-rpOi_WsmJ6uDCZVOl2anTf7Hy_nUVigH-hW61IZX4X6sQlUujw6h9yVJplAbemACvLa481dgVN83bD17UoS0DjfxTo0j8KVhZlU-e0BEXonnWJhAIPUxROmmWAaSDy3dLTQGy7EdYhw_aAUaxweEykd2IAOItE4Qlt3pfImcAynieveIS6p_o0mMNDi4qEvN21hWwTuXDHhCbDCGFS8QFfhzQ5LxZ6kAQAE72bYOQltWeYvcAdIlgusemvScFrUskuvpp1EbqQcx0Af5aDH3G4ppUce_kzm-1whOesAz-G_FhNpVlSBKPJyghAaTehKT3DX_LdbCEm0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZuZRRrPqGJqT7GIJe7e2qy6bRhesgJkdyiteScLT1-dVo4flCk9AidamU3z1TS1F6m86vIyG6oyTHfZhz6jqCLsR2Q2yyRDlaeIMBYvz5jDzdeJ9Qf7CA9GIqm5eoS6gUhN6o1pgr8imLNY9y_XR-g6Bpq5J5C2nfg8b6BbLlYH8limEwdX0XI36o_y10EiJmMZ3nOuZmX5F7QfVmYOoXO6CP-mTsDLmB3RYr8ksAksLmgYSK5pfUTJuXeeLRJup6g2D2DZBYNBpwD4xsxuWrCXh0p0qODImbgU6-yUnBvRvKx0RqZoinEU5C9i18GqTN-tRa9tOhCpx7o80nwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7V64SVBTclIvsId_1yYdlXKGq1pBzlf7yzUOfUBIZaCGjeE7ZjFb8yzzJVBHHPQbJZHqK1gPd9GqK6INBlQP4x9l_FUrayED8jOO826PeRSNhgg-bKJsyhNC3mt_857S6UCpeSm2sb541rmMByyg3XOaeQ2_ccM6NxqFiC3jA5QVp_pcMqo434R_wyW-weAl9HM8mqUAYVppyQCgIxCvKLVBssBDxIVJQgsQbqPqH6VxicoXc-z2GaRTulvzTbvILogF8NRkRw4X95QfbkIlj-ke50KavIo7cc1ba-zZtkcykqmjeopMJHc2sM353HuoObNyLVSfZLYi7pH-xjGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA2l0LPH0MC659R2ooDQSER5ra-PTdpi6kvs0DGwsE7GFxQJ20MFg19VUYdw5ujiXS3eXtewNHe4RPhlPJdSzhgMBC08vOxuhGTQftvayFbXTJ1yEWC3Gvd5uMuk6L_oPHToJtEA6_Boc-x7wCx0tS-17GoriXZRnFW9zbCbvS8KQ-c_MhJiJMbjqTYGA0GzW9AGi_UivFkzrwxVdk9rENLEFWNgBmsILQr8DJIgiTUgUGMynLLBF426x4wlPf1_UXiMbBoktuWcbCt0MU2PERlj79s4FtkOFPNpOiR3lnzM7nTSHrBypi29KpJU-Xfl7pfUdFS2wUHbmAFk2EUzRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlyUUapLM3BCxH2QzkbBlzsSUtdIesNflqfPS9O7a71dIjiZIbFZ9YC-tLgPegJ1B9eXCRqJZJNZ0oW3AKa4SSeilncRQj2dwon40TDTo-Zc_hcJk6YKpvQBmz19lRBQuKjjYQC6JbicAfgKs2zdKHfpyOTnKK-qZi4Jnm7_HF6AGjJx_FZK8tu9nOGgeyE0qV-RSFr2Uof9ASPPRSiHkuaB3Un0Gn6CX-8CTjhU9Uyfih8zK57OGfHOa-zu8ujIeQ2VRqmtF-sPvFsICW9CFNvOCwtSz8HYpP97W_71KAwhhHT0d36sYJty8IM3PU73JPQZDidK8M3ZHge9xaYZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfeWX4p-gozdJXxAUSEmIMN19aPflw0oXgsNuD734Egr-JCMec2_yY7mSnAiM4YNXX3qmXgPBDMTSDeACm0ZfWCyizI6_mrgokK0QUiavLoNl-UccUt39WVmkkWQ8kIPrKJoRucL7J7V1_dx5Cra5Vl9uuI3719-xJ5HLQT2mgoZkBGGOFcLZNzzy2innkctZCDwkGCF9Ex_5iWfC1Pp3s0TjRZCnB6fwynvZz1pbhzHBCaQpgTtf-a8nydaIfOc0eKxf3ouq9obo_xyPJRoL3x8LcRzrOyk_RK-jbFp_cfRZt9VVGgxX_lTHoA9iKGoKuCdh2SJUs05N89z8tIGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNSIXIkBEnA_ZavuMhHkljJmz-9bsGkW54iZ7wGDh6CNQoZCnQu509gSo5Zqqpe8di0XX2bYqHn8q4S8DjntCOrvqlwnU5zB80f69TFFlYZUSNwNg575vdMXvdZMfMCAzSv0ZHBi2829VNYxfank8uPLHtxlq46dIm59HicXyhAfrGl-yxTn5JcsJJGea17HZ-0BES7m3izAfKJ2e7TKJgb5hrLlZMr0hFWKNOXwL7WZCoOzUeUXDm11tUbl2qETik1zLwEewZon5Bo7QpxoNQGeO1KXCeiaLZVyQdRfOAJZUiILBowmuMTuYZ_3RE0WWEK5UrTJdiZcTeela1jx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0fUgZUekPUBx0LpJP5GtETZ0nYnAc7dY9DPZUmmK1J2Xz8qF5Q9cdm-DM3pETTjX4JLKLcNOXkZ54Ce8WmwdcEBtwnElH-VHPzxgq50s7gWupgZ8br0hNy7cRwIro2HTUumuonlb-W0fO2hR0aa3M0eWO3SfPTG_Lw99nI2jgLoLqbI94zG6hBJPYmpiMhMdv5G3yMd7r0Zo3PYS4MgJjqRxfCGFaxcllw0wuFzei18VwVPUqa0Ge4N7FFlJuZ1xQWixuD-3t1J8-FT-w6WuQH9N9NVFbIEw_uuwHEsO3Cju0CDwh3gJBUhx7I0-j9GcK6GpCsp0sOfzuvLk8dkQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9QwjrFScVlaS27inPbVt22iuRrbj1O6DvDAQPuZN4ixgIKmlWTYEMuiKJFdooDJ2C19529e1QRN770mIhE2mQ84JlNPJZaeZBPUP684d_6ErOla6qigsXkGPvfjKT6px-6KSXZ4jouazMt6TKUDABcfFcwqDojng5-YzfDn_I_MzhPBD5ilMZUM4QLWY8bmH5cRFm0r06yYRA6Kq4-B9nmm3aVLCFHkHtI_81Qf7R052Afcytg4965BjfUSWDi9femgdil3MlCpPq2QfFS116J-tpR5mOFAg2sK9Vwz0U0sw7L1-radw-YilMbbTOFogNb_727vWjFlSdW4V8e9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTjqE9gu0RvbZhGiN47T5kVBbNfonIBd8h4jUDS1z6tgFVYNZWAggIGvUGrZ1_V-0rCx9uWRhGJb904L7fwlYlq9VT-q0DkNR_Mn_LL8s5MUZS2fnbLvZXJf9BiswwelB_T3Na-vqbXCWULyPAg4eaHAiaI8lXGNnYI-oOJzrGFgrmtPLewA6qGS83dJtE3Mwu5wFLG2_GjqwAp5i0l6PklsGtSE61banLFJbDS4_iOvYfvQvwTkOIyYEjMeVg8cmgZ8Z0SeLj4HGd6-y02iNQ62tiD6wM4l4kbJSAgaELRKBV6n_gb71COMMDELUkosvnowm9JSamHaiRCMggKUPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sReM6vs0vMVzuEXLa-BUNfDef2BfXJRXS3pl2mmlq78LoCTkXs47mLmQphLza-m3sLccJ4HdAG62DkQC0VbGSI1wQBMVCXx1tdMjfVMmo0iq1OIBxoAz4gXLI103Zlgj1Bd2K2tg2h0ahhRaUV-J5RMVtmXW6jAiyaZ5WSn-oxSfxh3cK4Axb09F6aiVXp7LcfhTel01gDMi8eSBuR4761BYf-InnW0sHhHLG38NJ_amfDjtaV0kbTRe2hUTNvu_OPoJgj2dRvizO0M0fnKkokc5pSx3GIUFc8vaFG2gkAH9pzoqge8Y_x1UETPqbziv07vr4a7Nsg-3cOlx-DLQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt9G_Mc2CNYc-f936Sh8NWx-OKXtRL25CFgtWwOqjvaMUpEO5HpAzk7HUNIJ6ZcLTJB2gX9rkp_gM2YPJ3K51FXRtjAa5n4s2VG_JE4zKJ7oYvA-Dng23uI3InkVxzbtru0bSW1PWkmhdRgBwn2OdAlFIyI3wwgxBLSz5ijoZrUer0S3ZxLH1aWFqMcn8RZGawYf-XlZFPJcb1I2KOKnARG3-hFNgPyHckC_JqtaZ1-_3NUGIDlsPmHUHgj15Kw5FJ024VuO9x1aBAxWjjHeu7Cow9voQDOSyphhwkW3We6qHCAjRrWud7LCz5jy8AFU4i0xNQvM80PWHgRnaca-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOc7-eov9vUNX3-xHzqZgPNZZrx2OtCMvAr8Tqu3xl-pTXCMmYf5DokqiH_XpTc2H5pBA65MGh6Iso-1mM374JzVDei_O1Osexr8CSVah1qhrZO_tptAa6EIkKUGluVT5I_rrTnuL7yu4tb2QGx_5-F3N6-Ah1N-1WJN7jpX23eF3CeOWyGtwLnHOpEMkBTFu6mQ8CPANsWUpb34ofB_nD_qGF7mS6Hsf2XuG-3O-56YQlgOpDzKTtAQb2E65u8VBJlZv5jd5FTR2q_iLfCtYeAoRCWhsTBNV81WipNlJOzlJtQFWFV5d5Q1jLARjseCtNrUzZzLkJ41eLORTXoItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7THh4Mt5nBHx6-NTYgmFVde_GCF2T2EzzwhWkv2TnLNFr42JtodaPNmnEI2iNB1lqF-_oUFHxelr4TEM6bLZbZkuFNd3GrHojB0mO-YHqtvdtunGlhsniS1JlrrmLkLSA7zWERxAwTsMJrONpgivMKpfwLPQPCi-meP971_KAwx4L9dPyZSGrDj_IcxsMDGR-48IoBhE86UDeSX2B09zKL6kzOG9hGhafGHxxl82t72rWXJzg85_-jJgnvkWP1nxxNCjnSLixo1y5UTdoMEogttq92ydijGOrDCXAi0fVIRD8InWNPBi0xwOJkdQotSJ-UkOPDw8z7bIc1KNhniEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100576" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJPqS3oCa7z0HYT2hKJFw6cZBslen1RLfuh1D1V3cjl-NxndDnns8oPW5TUONzhrtxcBJz_BmlbbHovoaPeMTxDM3Qs2tBdOCLA5Kag2yvAR-1lPK7LHWh-j_HmqoGEZsEuIrlp37VgOxwzHd7ObhbFio3Smpd1VmNTx37VMxLcrK5Bt8rtDStjjhMQG_CqgXsC9DzFm1sqiTGxoaCILpUiiKEwZUsb1-70eUUWjVrjmZL0qm1l9Ncf1Sg1nxdJF6Qi-HB-zasvI-6QpizwXg9FObKc8xu-h4qzi1oUTFLL4NFWEOswIp-kGgyIJoWntb3siPQI_vDR-0KhJAXGdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100575" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_6mjRkZJveE7tolEx4-iuhIMwrrIR0-WtkbrQwjCZN2RUKlbu5F1p0XB3bH8PpNdvxIpXmrYuwL4sbs1bfsMukzqfMFTBkdVtIWhgmwAwdk9NXfr7Pwjkm9KGyVbQ_KxVDTEpXLsmympi3Jnv4qI0oCU7o9kQExLkcV7pDVM6a5Aq155HL4MVadZLW13IJE1RfvQkfe7GwGH-JJLedu4bsj9yhuhZGBbQC57dCSM1PbgB3WoGMfJSqQe5Iq2hBro3W1l765Hi8cY1o37uQgQPmitmen_nbzIiBuKNT7C0bMIDgn5dzYgH0hpkxVenIbUDFJIsRgLuYBby8w5pKeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw1-ZdbH_yAb6wges4SHC4QtBcCexTiecU-Ox5M5u1qITdGki-0pz5_Oi8YXchEkvGB8TCRjeH_QCdA6MDD_peeJ354rRPl1e0SKJH-2LVnC4FR0GBwfMY9WyTF5SktrEXRjybQgh6NrduFsetN4nUFhlBBQ3kCsi2ayM1XIIhRcM-Xwrjca0ko0leKH2qdg44wfgApSFpi9ujxBOl5JSEUBMpNPV9dTZ4F6T8z8md2pkL90yj4X5mW-7ZLRth_y35iKEGvQ4O924DeKZBOWWV1vQyxP1OLYMnro2z5aM7MSVD-JZXAxVVZiRTphi4tCLSSOGrRlmx9ZeUNh9LrnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrssHWxFPMPhe2vK0kjeKDs7PA7uca3UtdJ1Pc_TVV3-YKHjaBvER1YET_-48hKkb5dEkTXnmSCMQ4uDYAcj2cz__PtV4Gq_wy65GgPC-bDjzVs4wkHTHPnW7AOQLuc_rNx2Sdwhb1UlIZtnn_pt3ThrBqoE-LA_X-cIt2TJW-BZC7o2sdpxYJgYLJjBOGRPsuU__IFWtEKu1kzKmRGPAaerbsyG44Zn2YUYSXrfAtcCMrj_Ja7XCaETBqdo3-IxC8e-P1eI9ZpYKnKes2y5BGCdm-OuYBZ4djMgwPqVoqjcnvHOUkoSANtWDIFyg7QdtqaEPTno1Jq1v9eSJr9v1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHBGfT_DzJcSsSdx5oPmw6P_zvEMsT7JJj3Hy1Xv6Pid-6x9Frb7MIkF5H8qytVu31dNa2u3hNt82YiUnFRx0x6eu5sMqaOnKkjkwyyGTcBhT5O-KqTH_MWzoVm_oOmZ9XyzzknXjuW6JkUyeTaUwrq0ughM78vBt6VbJDTvz7O9kOwAgtZ1RlAvNR3Tehmz9g_xAutLzj5aLINyy6UPhoDuvSnxjPxHKd8mKRwa7FE4KpgWl_MHWieHUZ_I1wYwC80_lXXH3gDmu404MSBPj9gmDXwyCZkPURFch5EUIGpKnVV61Kb-uXNO3aErqjgKbIZg6-D_0f8sTucPbLJSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orSRCvQqnajs81FWFIeuOVhTeVCUBABA3Dnc9AUHlbz3jBmVu-GzKXbfMgkw0e_QuCB2ndQX8B6l1MbksS_wQO0lQ9jLwJdKS-AQPwT5G1U6eqknO6Bsc95hDbgWIt5B4LLcN_RHuacvrhzimxqMCBOeVl3_6B-yBeBJtFL_imk2j1zZJwj4k2dYdCv2VAGnPTokOhH1A1ZeixOGmS8lYQwWCQl4HNkz8jrp8SaZNNJpTPE-WX9IoRTkf30K6kLE5EcB_G5hbkLJm6BBhoANkMto6DjknrDJMWg0vwEi-DZV_ypLNLxfY5b33JO5G9W-k836PDMsDHQ18IYhjH6KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afg6oO-ovq317_tQTOo0HxO0ggUX-lRgpM0yRmrc0WM13OZuX3D6hDfRDh5LG8vuEeWCzw0OR5UaWr5x5ly4XOyUxmPSMeAT5k-o9cYHiOxpX_OAB7x60yLW3jYxbDF14ogWhScxsY-Y4sk6R18pMXL656qR6e_1Be3ipOR4PLs4BDdC3sXHuNj6wgFe2B0Wr63WzB9SAGimMCbaL5V89OOW6gMk08U6I5OxsDpdVwOh9qJCe0s8ZyULqG2_H5roQfl4d7DRqXGAwOlHL4UA3XNu8VLhst_6mW4hWAdPUQ5wVzH7QQ62uqFfo5NPRUe4idQNVoxHhWHCxCgG0GiC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpSvCaWB4NINov5JGAK9TFX7tHbWAYPtqTBLoWC4oeGUXkftSHltd6dMSu60ZcqJwrw9thnSJ3PTVxGLA6qN2T3W1MynQbJwc1SZiKYhngFAFpYg4jnraYUlIQVCPfUlkn3YA3ShhXYvPxSpJsqLw18dfltMu5ctIra6O7t68hRNZcEE1yGGm55vVoR4osAM0cePq3JATGGaEKoq21TOerqamOk6BwsxuXTcDQe48xHUOvmbqG1FEK66cuImNwhYloU6tGRu9QZqXx-7WUjt7KfwBXCX62y1FZgVY-xYEiMP_2EZg-P8PsUiIzhRc3hEFOgPgJeX-reZ8fFLZEQaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=kilSZI2Jq1QHRia9Fw0Fy4WgFT0je4E2srpvzpPBAo4W-EYdcNm-gyWlBvaoEXPzqAWN30NeryzTYGJsXTf8BZEJYCaXRpP6lG62NENAsmYi3vmY8p6u-lhMn2r9NiXzD_nnrCr0R6hyuzpimvyK5l50bPk16LcVQQcx1tyiWuy57Nslonxv20v1QpjkWDwo590xX0ek4oPP7vSq6t28QQbCGD5nyw-7wPC2TR2FJWYTeR9LTWeYAS03CDy5Q-iFMCR_OUlf-8J9LzrI-dQDopr-apwrkwCHDHCwrExqK8DYOSCVOc6lnFlkrAvwjqlOPvg6PzfZWvthSf3O_7qQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=kilSZI2Jq1QHRia9Fw0Fy4WgFT0je4E2srpvzpPBAo4W-EYdcNm-gyWlBvaoEXPzqAWN30NeryzTYGJsXTf8BZEJYCaXRpP6lG62NENAsmYi3vmY8p6u-lhMn2r9NiXzD_nnrCr0R6hyuzpimvyK5l50bPk16LcVQQcx1tyiWuy57Nslonxv20v1QpjkWDwo590xX0ek4oPP7vSq6t28QQbCGD5nyw-7wPC2TR2FJWYTeR9LTWeYAS03CDy5Q-iFMCR_OUlf-8J9LzrI-dQDopr-apwrkwCHDHCwrExqK8DYOSCVOc6lnFlkrAvwjqlOPvg6PzfZWvthSf3O_7qQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=qAC3o8Usn4wqJyxH-M5uCx5bgdIqwe_z4w5iMT6lcR5N6AveEpsK_4pGLmllAdznVsFOJEn_gpLHZudbMe6Hnbveq0wNYu-ghXL0KZI0BEP-1c47fYmfDOU1hK2fHmrrYEpP4ujtC7admxnghMcbBzOYRUOzrYqeBOiyeqZEf3Vgle1oWPi1cjUzJuGwRyQ8fiZN9cJIOCzqvynUQ-F-UlPJ4t47t2UpENsti3js9fnWRy7whePWM0cEHIs9AF-fbpp0t8r_VPQiPvEcl1O-VmQ7nQGVFveeUidlaZ3POb-yglmIvxWSqoqanGBJXmCnYA8eVHPVnJZmrZr8QG9Kfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=qAC3o8Usn4wqJyxH-M5uCx5bgdIqwe_z4w5iMT6lcR5N6AveEpsK_4pGLmllAdznVsFOJEn_gpLHZudbMe6Hnbveq0wNYu-ghXL0KZI0BEP-1c47fYmfDOU1hK2fHmrrYEpP4ujtC7admxnghMcbBzOYRUOzrYqeBOiyeqZEf3Vgle1oWPi1cjUzJuGwRyQ8fiZN9cJIOCzqvynUQ-F-UlPJ4t47t2UpENsti3js9fnWRy7whePWM0cEHIs9AF-fbpp0t8r_VPQiPvEcl1O-VmQ7nQGVFveeUidlaZ3POb-yglmIvxWSqoqanGBJXmCnYA8eVHPVnJZmrZr8QG9Kfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=odlmyMl8x1Rcv38ZghUC5t6JfxzA5rZ5P7vDAUGk-uuI8rp6C24mxrm9w5SHTiffNn-W4M52wy60ybCVsHJKw_pPHrfsDsqSdt9qbmJuJDnyOxv-ABwUSxvPcloyU8GZzA759le1e5XpYoZfljxz9N-pEQ1dRzxEj_sJdc39bkpyY1BMHUTqGpmzNi_JSOS3Tn9sIL0w058SP0v5CPrDbjtWu7spOOM3g6rN1xwiHHgncPBKvKVAekooKuvK_dt3zTN44nk2AY1hXH5H7RV37Pd31trDD_7TbMWfM1uByNsq6nfMQ6VzvkMeuKLN3eTCBGlkgAgXlEWv6JZmQq09uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=odlmyMl8x1Rcv38ZghUC5t6JfxzA5rZ5P7vDAUGk-uuI8rp6C24mxrm9w5SHTiffNn-W4M52wy60ybCVsHJKw_pPHrfsDsqSdt9qbmJuJDnyOxv-ABwUSxvPcloyU8GZzA759le1e5XpYoZfljxz9N-pEQ1dRzxEj_sJdc39bkpyY1BMHUTqGpmzNi_JSOS3Tn9sIL0w058SP0v5CPrDbjtWu7spOOM3g6rN1xwiHHgncPBKvKVAekooKuvK_dt3zTN44nk2AY1hXH5H7RV37Pd31trDD_7TbMWfM1uByNsq6nfMQ6VzvkMeuKLN3eTCBGlkgAgXlEWv6JZmQq09uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqgpL15mYSNZljq5JwXK73n18zXnSQFU4VVERAOl6apxidpcQ9W6KsfrMJLxFFb0CSxko-AckeXmiH5V1aQI1zptCxynnrn0_JMH0EnCOAnKeI6rinwJEMllk_LSFaK1-cqwGqEeKM6b5PiIAu34BQZ8YkWiAg-rT39Mc7mLnNKIOgam7Lb0SEPqYw60QhpIis-gRudKxJwgaqd84iMVuPhdgMgETBhiKv4hcPrySE77_GF7IXuKbW2RKustzlLeKq0stMh_-mRfd_4Rp2_-czvV-qO-hu9CxCdsjl7mG8j6q07t0Z54FbK2rGjAJ-sR3gGS_uxv1kl6bzUPsZqRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYls0vn6ilyJXIBr1H7WrwGq4Urc50NvZGsNcX2to76iO9skxMB5Pi_lNj_j1I4fXVvxqLqWJJgTDLzwxABSvLctMSIg9wYbcCigtFvAFEmb5VUQMMb0PVBy_2WWVu_xnBVAO4CL0GI-D6eXPn8DNyUA4n6BqAeftR39iWk4D6WfTNi4HxcvUe1n1sYGGJ2vd9AtI5TfJfxWegcL7fvGzG8ImxB9HlxFZj6yW_rAnr7vuqFMmrOqytFsoTv8fvRlFkLXIUgo-jxjjM_LT_WiKw2pvuVH_rOTa9hMzPd7JupNEybw-lIwnRS4JXdfQgsgxnjMXpOBStkUBoPBZWg3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=g5ILZ1ftSziv4nsTztlGiP8A974I7Y2qrcva7XNLWC_2PeZE9xH3aV1r8Gd22ja-fJbMm1iF22jbC-HmCJnJNalfueNv3WAwfJjWRyuPcn6CLnOj8w-QkR7tz5wWFKWrwBDy3P3bJmAFcb7vzrJD_6_ZFkawaPuK0JgaWruls3osEuPxvoj9VSCIhDtfZhW3_guO8E8Xc0bnol1VaVJLN8_EliJusgpO6YWbaYh3OVqh0sbhsJy3VQpFyK-Qd9006O0Fp7e1F-O0NUgOW_daAi6h54nTkzwtmXlZsqbF1qaGMJPlnaOSrCLJ1_Vzi5_J6xvM6W7xV63zEZQD6gcdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=g5ILZ1ftSziv4nsTztlGiP8A974I7Y2qrcva7XNLWC_2PeZE9xH3aV1r8Gd22ja-fJbMm1iF22jbC-HmCJnJNalfueNv3WAwfJjWRyuPcn6CLnOj8w-QkR7tz5wWFKWrwBDy3P3bJmAFcb7vzrJD_6_ZFkawaPuK0JgaWruls3osEuPxvoj9VSCIhDtfZhW3_guO8E8Xc0bnol1VaVJLN8_EliJusgpO6YWbaYh3OVqh0sbhsJy3VQpFyK-Qd9006O0Fp7e1F-O0NUgOW_daAi6h54nTkzwtmXlZsqbF1qaGMJPlnaOSrCLJ1_Vzi5_J6xvM6W7xV63zEZQD6gcdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKGQqJh2_2guM8X5EScBjqmZ0U063XQrmg6DWhT4_NYDyiSlrLukXqvOsWsf9quhmPofe6lpvasmVm32i4ZXDmtaTcwYm3IDC8Y_Yufsvyg-EMHU4iCwqKPjmsMxfpwbBIhs11ipN15gnaQZo1LiXYCzhS_e2Gz5jw3NcEMLbCSFOne0HHbbTx3yhzJuW5ROA1MxCBl4IyEN8ZWMDwUK3xwSCsFWpJDkYFot4Dcr4aNADdTvuBV5scOmRd-GJPSTT-gzLCkb55gzhxtu7aI3iIbBi8Fhy6qWaYYSdIoOeh5h18b0VansIkn8ZNkAiFNWGFmyzgHCFA7Ha4xQ_rJjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ds4kTfKe81Ch4UUUJP9hwOL2zm-KEiiZLi4EupMmYed5FP_h3qQLpuxpNTZK-6yEo42m6glQE1AQLWdaniB3ifv4p4Lc_pAqdKYnj8h10HmSkafpIMc-HD_D6Vb98VcPU3vO_Cmx_zWWASZNK2O-F4EqyLn9GiTL73SJp4NRdgv5MH1dodXJ0SM5jM0Di9zHVW7EiZK9FN-T4yPNrbOdE6YMz4QUYs_twmXDOReF--gpFOWvpEiu_bEvcChRaqPLckIzrkgY4dImcBIpGW7IJha-XDXt3r336O_aKkRAdXybFC5_lZSuQPVFDcwWigtZXMTqaKunT2fKFc9NoaF3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmGY-DOKL8FidAOnOthORpO2I__Be6GVNhEws97i4ha6AbLl7flng3UIaOtlw-OLbiC84v-liT8dh8pPNC8Q6TOl7LN0dYMiyWHI9iatgV9uKDkfdE-MqTdBvNhtz0sy2aeUsrFsynMoUiPev4sLP86pYSRx8rHYd5rmFJtdM0xiXCW2i9_w6P3178xCI6xwVQ-xcvnMb00wPrqq-WSvnHDrbx9cYnMZJ1kbG-xwZplboPI3KAa3rn-mwt_5hxv1mk1ymspF3TMJuRTP3-iO-veQbiihzLlk3wLNsUQ_tuMkBlFYARmyl8jtYHw4CY6OBlLgr-ZRBGa2fjGH2fDLMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwv_FOb8jDRpyvo1ypaRG3FcEuhy29c_pbfg0sICz-L6asY_dey_XKmVrWqIRH5TOZDeuOUZZWeEAYI1R84Neuy9nNAA-7ew4MKXYlUozaQtA0XgmJf0yqC9a1ApGdlVj9Nio-DqFVTPqNL7hOYONgyUZ8fjjX4xPccXOX0rIx6XIoAF-giTbrlCy67ukX8kPuPpzspUUAVd0a4NtHA9wOOU3EJJk5fW3gAWK-7l8zwVzFfoLoVvI0p3jlvent_cMY4ccDEwVKDRIpYEAGvrBuY5HPRbpZ0P-iODD-5lW3iauCcw8ViEbHfEH3Sv8B7jyw6ZsUcmFeS3QlLXiI_U9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksf6XtIuY-PPC3RbzaRIXPpkD5yneib0PBY7HDr1jsXbSmZ_j7tDFs1w1nBub1jBg5H-wJwzERWUndF6vz8Mzn0g_RJdNlDCSwzoUX4YuMKrRhq2zCsJTgdkXUG_2D36wGd_cAKMdsC-yyaBd9k67DZhycBGVJXWXMHDJRmns5-hhvkrITXSyoG7qNZXU2qb538Tx8J1e0-ANdrnr7vymMKQ1ZxXKrFkPm6mbeZZRJ03M8PjEnWxgymDtLV42gHYrf5Wqd9tV-QNrrBl6afiEK2PxrSax9yeaVqVrORKKpOqSVsDCuqxTOFkdetl-WoN0Xo-uTVXR6l0-JJW5MbR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1EZC-5kvk2GBqPrteLLdsIUqokDflET-erB7NmgVIttRM68_PUtCC6bUfvk-U6ThxEMXQjTwpI6WcrkaqPk_W8eiwudto5TFh_RgJX3VaMAh-I7lDjyKIVXUXKWMFAIrFuKe0jzHcg1GItuZQNXmc1fQaEKqWB9kTaj_RccErAUKmfbu-4DZzXpDCCLgFUpbvqDwwTdbnvVIfl9nTcLQg8IJPWP5brzBr43dEBoi35GbzkgNAah6SH8NU781W8K5m5IaQOTzClVcwHvMS5asuFGsJQEK-oVLC-Az4j-1-OpzS3BDmHN2vT-kwBu_7U63TmHv4W3WLuPa1BZAKu-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYQi-4toF9c_9OnvCNMJMUXlKoZ4p2-1IaLxDGfFsuQCu35GDl2HVsvvGmKZGBBlkoRKlf3rtevSIqIMqmDYFmIG0zIEoHCT-cDYyVbIN42QGWi5PS4wS3qMMgQajNZ8S1NqF63cOnon_Bo0aatZqVUMzvidbVjh2Geds2SgaJ5bbBKMsJCGyG2kN-SVW5jXjfkmJxVVzxaJze1mUDBi7RzSetEoRp9vGXly7avKRimzTcv2fIr6Q37O7rMdjpO3rk5zKzywfBPmXLMsncasXVcG3og0uGOOpnb0QtZirmc5L73JTpPFg_x39ty2_-LTZfzXbIJvoNivOJAVcAH8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI7ZVdCb3m_aYv7BwjRIt9HFllzPilcBR9gwnf-Ovh8IzNfBuCeLMKngZH94pJBrr8JhdiLBKO6lme778PA9eR_q_Ny_PoMP7lslKV4uqlKNdpSsDdgFminuBxk11VSY2Bi3SJuQ_DZQlkQqYvtlGLzsCCY0VjOYEHOeSNNyrs26fqqknog3R399nda_sP_ePsj_juDaE7Dxx2qiCGqg_4kUl83PIdz0Z109prNlKQVJoSgIJaY8uGTPwK7CQRXZxwKonSabHvVXpiNUFMtr-MOxMf-4Zr1w5cUuHFx61hTtZxt689eXOMYQ4mH8sKvrzcKNmmKOTcv-GwJ1uuxJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3zaUBVJc5IUE14c-um8l7ep_chySomkhugKLNiwTtBiSumlzgFABSMDp6T-E4hHwdP5u2HpEP27TcfgaACHR83ONndxnGw1DdoquUELOirJn8rjmEuooBTYbJguogsR-HZOq6SMFPYTrdsEEGOeC3Ye_wc6opDN3a1HyHDvNYK1GUpmAHMP4G6jqsHj55rcTentnd9mNjw-oBuwNfAWBB_Pn58vlSAY0G7yi7bXow9WrfjJMpTbU6BXAU9lV5PNRCPcomPDcrQ67h_9mMK5_WHKKgCB_14-SVmpmwNy7kbsLopJebwnptCFVhvIuvHVJDKyO0gVQKgyrbJ5HrTLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gU_pZsw1j66bbIKLP3dcGZ3XlMeffS6AIPTyc6RHOFYP6LFkdQkL3H8Z92YawTkQ-C0MQg3upzdET8J36_mgb7WtrLMzRvFt3PkliSXRsOo8V7wLAqk-CGw1Ph_e5-aMnQTvaYJxfdIEn0lTmeqrpknh2VZQetxSa3Mxk15fEhRvsjdI0eKpUq53ziD6RVmFaRCHt-E21Wi2q0DARSA4jh7Ina94LHO9d8JOghsYOL0UYLSLe_46b6AGEsocg7OSoQfxWzXPZWFN0JAc3XXvT-zh2dkonC0Yu_9rcRUMm9HP4qp08JxGsk_ptwWvUfnt0eJkSQlCXgxJHo2a9IcxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cs-TCcFpZZELctJmc5OvTN789j90YEa1QZwbMsJEjUhzSjkgGfLT5R4QPZOxDmMm-MICFuNP8JqFTlgDp_UloHbYWqR5BxNKmQcVZiif1eAJqmsZhvHQqYEtBL73KbPvz5AIZuHT0eSWhv82vyGmPa9xsaVKTZEDXcWrDHgfcpwYIVQM_vNmWWVzmwesVVW4dsFwG5k9hOKHil6-4MpQ3Yw4HHT8RIx_vgS4Jt-Jfg7RHoqpGkwEp_97TUsPAlihL2vQmzaZDbJ-bpaPilJvGCX5RRLBsCq6IolBC3rJOePDZX7UH6yYiuqBAAXdOx-yPGGotVgfsgaI84GMyOEyPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK1NBMtzrC7xIIQk5j3fsN2bjIV4Am_ldUsEEh53cfga08UvmdDeXcSjJEhRmX0kf-BwTCGy39miFEnsnmwp78Pwipp_HKciv5S5dNrJPt2eXwHwkxfLq8oC6cH1i5t19m5wauUY-K0jnNtUfmfJ4mqnfEmwiQvUrjFBrUnLxdwrqoKn0oT5I6pbUXCtz7LtgGWhpCn7Y-bprV_wDhpbU3hFrQI_BkmaVGFdGRaBK-wvT8TJjn9K-CGKuS9BAcwFiIsdSqCT_N4WZjw5mtAYOcBULv8VjQfzoI2SVgNV435PBzQQQj1mQEOZPev-UTEcf_8ssBL2yPZjJ8fCmCJTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVL2lnURge9FO9j7GF92x3NGPeEI5GFr9HWo4gI6RZbBH_mOjfHt0B1dR9AkMt0DgTVmidYbGPacB6udinpbi_-8SIFr5gEfg00OtKgtwHAFLgzgRZjDt_Dtn64--AQra43tYdW8EUdAP__MQ0qfhGJJENXj8w8a_VkyS0vSi2xwFjGjXELLi-gg3osKgROZ_wSvnjfMfUaAyfP0Z_WDIH3oXivUV43IGpXrVENvA3CgaakZX918NaV2KPxEdcb-v-wIvVhyoXdRNEjIg8fr_yD-xygj6R-lTugISVB2XO3EvvaVccCNTgSe1z2CwqL6iQDE3aW57kmBt6mKqmLweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=eQRSs-UGQTnQmmKspaAkeAdz_g9_PWkjzbXFbZ-EWClXxiywi5cjMEzOFC4YQ3QFDqF4unb9cWyvzq6xA6HrMXTl4ceABRBUrN_6UNvCVLhapFJ-YJxpIMp-0zsZd_PQGIbZ78q367VbYWTwkYmkti2b-oeuxXg4Hv90qwbAYoEzsOLnz7gtVFoFoHOrLB0s0w08Kzb8eEb4gMlClhdrLxVXJF1PBMFBsX_qL5sOEm-1-y6q4aTgPH_Yo9PwWxj_TEY8-GJ8HhS40qcbAoqGg3YX-JQKnd0-xoNVi1nNKE5yK_JfONkYF2iODerQVHjzv263tjM5prOxmYylG7e6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=eQRSs-UGQTnQmmKspaAkeAdz_g9_PWkjzbXFbZ-EWClXxiywi5cjMEzOFC4YQ3QFDqF4unb9cWyvzq6xA6HrMXTl4ceABRBUrN_6UNvCVLhapFJ-YJxpIMp-0zsZd_PQGIbZ78q367VbYWTwkYmkti2b-oeuxXg4Hv90qwbAYoEzsOLnz7gtVFoFoHOrLB0s0w08Kzb8eEb4gMlClhdrLxVXJF1PBMFBsX_qL5sOEm-1-y6q4aTgPH_Yo9PwWxj_TEY8-GJ8HhS40qcbAoqGg3YX-JQKnd0-xoNVi1nNKE5yK_JfONkYF2iODerQVHjzv263tjM5prOxmYylG7e6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaVX8W3IsYlb9hMNJ8wEypnqwU_6YGUCWW9CHQBm9Z0d04HaczD6cj2ah3ZgxKeOuYEVEg2TQP2cn0YmkbiPLnOh47XHcSc2Yc7Wk5QpV02xCM8rb8aUZ85gaVPEciXLrQR4eXU-3hFFmGRRXfaAIWO8Rxaeu-qyNimb03sOAMPRODo92JK941ya5Xnv1uYXm1d27aInAQfLA1TP59A19yJD3xLZpwJB2uv6wQO4dGA7KNk0wqFcFEGoawoNGji4vfNzX6IN2dKJh176u5tFIUESIK_CPdqYwf8ShiLQ1wkpdslV2ahU-SdfIt1U42_JbWTmpxr1vNwA7j7I6zY97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEuhOdk_huXv2YLoQGTc6flcsbmMXyVmECvxRT-f3ZCVDQ23-SxXk0JmN5LpdCQzo0TP3TQI0jfcljKfbueqSbQA89WhntwiIh4UAahe4E8rPZnMrlcBxiDxW__lAEWCVfPU3DSPmjYZU6jWYSI7ylSzqHWs18AvbggsgqDMlcRegx9fmj7IJen_wtIn3Z16YNO3mZ9QGu8JkN19g49_y6654GTI2YNuPmMF7UkQBncyuDnGku9TiZ0bh1NXQcKEaGxVcVYxh_JbJrBXdtaw0xd8QRO4ldneIsnlmhH0HhJ6NkTjwiW7XsZRMlfiCbQOa-ZxYCshcGPq09GOyLyVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0QIbkCUoqEa7QEzwndls296ms0cqFj8-63Qw0g-t61UzwwIXmMBoUtgpEYjdkK6a83mDFv1GmUsBo0OyR5PXbFOvHhkNVEVZnMC9AZIRdS9N1yym_2dODvxp5bWop3D_yRtvz9qPgkHx5owNyJLZitPsp_yhjuae7Hcz3aP9l4UvtSfdxjjRejwdb9D1b3rLF6uI4CmEJOYIgYS2rwK1s09yAtUqwpXqzC4VfCsmC_3-XYMcUzmCtMoGHyaEPO3PW3St5W2ed3k18QocST0hbRmICOs106foZc4bJxEMOrEKe9Gw1EXEjMOcXodch7f2b-Qdkh3d90F3RV6IdBuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=QsMOUqROcd_rqqf7cmJhsKqnfKQ6XEhUJsaHIRVHvpP4G4d28rLwFWRQ9H9xqtCPtx2U8G6JomiyPwODeNcSbTsAbZGfGiFDzlCYKcQxm3DCbZGmXvJGb-zfEqNM-WxK9acgbuXTsOpMVfAcfQ_SY7a2e-KxCCIVmeU9wN9p2hlYzs6MaaUZTyxYhDEidIbFoEhuxGPyaXrINrjEoCRJslRkgreW-uxTtu9F4QJymxwgQqT5BYMTirMzmBNqHEUtIouHK1uKhImfZJawMK5Clyf4_3sRz73EnQ9jGcIrYY9Ejr_PDyDof6aJ7Ow7NiRij6kdO_vVbqbxshOk8R5fTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=QsMOUqROcd_rqqf7cmJhsKqnfKQ6XEhUJsaHIRVHvpP4G4d28rLwFWRQ9H9xqtCPtx2U8G6JomiyPwODeNcSbTsAbZGfGiFDzlCYKcQxm3DCbZGmXvJGb-zfEqNM-WxK9acgbuXTsOpMVfAcfQ_SY7a2e-KxCCIVmeU9wN9p2hlYzs6MaaUZTyxYhDEidIbFoEhuxGPyaXrINrjEoCRJslRkgreW-uxTtu9F4QJymxwgQqT5BYMTirMzmBNqHEUtIouHK1uKhImfZJawMK5Clyf4_3sRz73EnQ9jGcIrYY9Ejr_PDyDof6aJ7Ow7NiRij6kdO_vVbqbxshOk8R5fTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=hjkANUWgr2zVZLKmLZ_O1Ss6ytH8T8E9KLU8WfoN6WWx30_v3xMrEd4UfZMRovm8QN6_c8hevz7u3fNcO6JTVekJ_GDbjCM9oBWCGW6MJmvPpH1l548tBKHWlBFFTp376Bk9ej8lb2vb7kLfl6AJBWAoCSTFWCv65tQLa-SbC8Pt-YtYXB55RA-AZeMT6HIexeq3PHIH6a-stvR3OThZNy_xxZN_LAJrD0hadb7G_t6iRldjfSjpGaj7cLEqi936jUvRrHgo1tSu0ikyVDMJGSc0g1klDPKQGza6mACcKv7SX0E-Mwi_y2l8xVBqg4BDY60ehad7AWx9TQm4O5jOQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=hjkANUWgr2zVZLKmLZ_O1Ss6ytH8T8E9KLU8WfoN6WWx30_v3xMrEd4UfZMRovm8QN6_c8hevz7u3fNcO6JTVekJ_GDbjCM9oBWCGW6MJmvPpH1l548tBKHWlBFFTp376Bk9ej8lb2vb7kLfl6AJBWAoCSTFWCv65tQLa-SbC8Pt-YtYXB55RA-AZeMT6HIexeq3PHIH6a-stvR3OThZNy_xxZN_LAJrD0hadb7G_t6iRldjfSjpGaj7cLEqi936jUvRrHgo1tSu0ikyVDMJGSc0g1klDPKQGza6mACcKv7SX0E-Mwi_y2l8xVBqg4BDY60ehad7AWx9TQm4O5jOQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrE_RyWlhFmV-paKigGF83xftWZyA7aU4tOnux24arFE9Z8qjSxLRkiTcxdr8623XLdYhIPY87Okrds1UH5aSag5Bk41gtofDGAvTPnzEQHkYjrThHOzcHQW4Y5CwcvjmbITSMps1IVMbDVXmmzFXESUhulbYiV3dp8JnfCTvvCsQsfdv4-f6dF7a9A37IfCXXsHJQ9G2GSiEysbtWasFj9hTcrgsjGP1lrVZA_rf-ONX7NXnKAq4JDPYyxSYtHPQmRH8BE9-ZWfKqTOLp_XIMAO6c4_pC91Xv6m_Bl_uErIt0nMBoEDfDQktbf2tGV2AC4untMrJLFeSiuA66vkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=LJbIiAsz8y3wYbcpZEBt9pRWRZqWxymAU-5zlFPediij4kO7LH5myYnRHs868z3XnrBafMJjCD8ATBBpeK-2z1hWWXGAe7fn0Y2HTsLQH6P5U-LdIFw3_DfnGdofuobvRr8SyS3chowyQZuEuC-1qDTu89kg3r67ozpr-ylA4AVvBU7Qmo44mVrCRP7hW7Tjz0usSIAxwNbOhoSiXRCXGs6BQh2NHS1v76Ltw6iwU80rQNw22BfwYOB-7X8wBzGN-6EVS-HuHZa9sDxXZg-y_7FTvDj-_b8VTsfBIQfASVHxb4zyJOYupgCIS8S2Y7EFdZh3mKdfm11lmgAqVVJLPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=LJbIiAsz8y3wYbcpZEBt9pRWRZqWxymAU-5zlFPediij4kO7LH5myYnRHs868z3XnrBafMJjCD8ATBBpeK-2z1hWWXGAe7fn0Y2HTsLQH6P5U-LdIFw3_DfnGdofuobvRr8SyS3chowyQZuEuC-1qDTu89kg3r67ozpr-ylA4AVvBU7Qmo44mVrCRP7hW7Tjz0usSIAxwNbOhoSiXRCXGs6BQh2NHS1v76Ltw6iwU80rQNw22BfwYOB-7X8wBzGN-6EVS-HuHZa9sDxXZg-y_7FTvDj-_b8VTsfBIQfASVHxb4zyJOYupgCIS8S2Y7EFdZh3mKdfm11lmgAqVVJLPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrKnzDO0pd4leR1QFxUkm2fG8TNt677QZv0rGWn3SdJjgrgVHJDVWFHGe9po8f-qHhvZFcK92STvUnC1fn-4GIsRxLrM7SwSAcRmUvrY_G9dfsdmbdYm7meMBG7lcLIA42U_2n_XnNT9DHgMG4pZYg2hodEXyMgbR3rl0GiH9SErDoYjxTOHMXr_k_QPKziXb0NODZhaQXQiR3GuKjCHKOPWz67amy-Cp8B4CwVp8VVaXhl0RJwojynj70sdGBM5mPkSU-PfWpbEXfaOzgxOLPW9nSa8mv99Ca-4bmMhp-fIMvkZ8DZPNzwi2ef8n3WXTX3VGf5aeDvFczd8h_HtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCehaVu7RDAMI_nvmT4qLygHIJ6ofEx_BNWG66LuaSl4q7QF7PiUIQokVTM84JtSvJOrrI-Y7LGYGEe6tZKyIZ42BB20TU_-F5j_EMyhAgjhYNn1YVC3tkHMLcFg8_GxxNR8cIFhTBJ047xFVovSqCVimZWNVlBqGdd9_onREZ6uysv00JLPWP3cGmClPie5YHGyO2_PDBaEQOZCEjVsfl0p66OmEN_QvC7b7qnQ0rwK6Pz72Yo3yda6f7wxgkrT5ERRNOb9HDg9oUGlsQ9_ENfnt6mOB8FXuO9iIZb9bXr1ynWxHQ2Po99-1FfEr0EZ27UIxLmA9Soc3Xz4FXxLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=T_u7mH-KahjoF91iJk3qcHIjAFkPwuTeXaWByiJmbWgFTTfoJFzTdKl8pfcfeIRX5MKtAnqI-dpdulO-lVpLUOgu-YYb6CqrwYWGQMq5k8Z2eLoOpnyQH9uaX3Xoo8V83ehwCwu7O7xiPxYNQMr2-f3f-rk2pjJaSrg8pjqeYtKX9g3vugVD6cY6XbwIWZczOdED5DhwzfBl6hcA37NSNZviPjaTn92FoOkfpsR9ESyeIb-hbYC72Mo5AcqwUwTna_vFSCy1kpJNiAEhi0q9914yoXkweVJxg9y8I2GaUSkVKcck6utUw9gJXaPidideUgObWIxx7xsulKsZogj8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=T_u7mH-KahjoF91iJk3qcHIjAFkPwuTeXaWByiJmbWgFTTfoJFzTdKl8pfcfeIRX5MKtAnqI-dpdulO-lVpLUOgu-YYb6CqrwYWGQMq5k8Z2eLoOpnyQH9uaX3Xoo8V83ehwCwu7O7xiPxYNQMr2-f3f-rk2pjJaSrg8pjqeYtKX9g3vugVD6cY6XbwIWZczOdED5DhwzfBl6hcA37NSNZviPjaTn92FoOkfpsR9ESyeIb-hbYC72Mo5AcqwUwTna_vFSCy1kpJNiAEhi0q9914yoXkweVJxg9y8I2GaUSkVKcck6utUw9gJXaPidideUgObWIxx7xsulKsZogj8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW515nCfcp6cZ_322CJ0v-T5EHVIqdpErk7lqk2nXudsSP_oIanZ868HBTdwXk349pWlU-sFKQxqYwBJhLVR7b88jQTn1CZ-TzQU_IlTqW9aHL74TE98V_eoGT8nxBrKu1iJZJrbs-h_cuRhwKI146BZKQySQBMckkWJwc70RgxMFH3qvXloyvKyb7tUB7hEen8shqhQ-PAsUrI1gJQq_MC8nuR1cUOBXlfdNWCxmgH6Wn_SEmbufc6ZZ0errs7YDHrZ4mdsB6tBSDk_VYPv3CCkiVGmQUZP73aQ0xyxA_Q-6D-1RZUJAV8ZXjGrSfWtV9GuGRrdzNBbcCnhFpx2wrJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW515nCfcp6cZ_322CJ0v-T5EHVIqdpErk7lqk2nXudsSP_oIanZ868HBTdwXk349pWlU-sFKQxqYwBJhLVR7b88jQTn1CZ-TzQU_IlTqW9aHL74TE98V_eoGT8nxBrKu1iJZJrbs-h_cuRhwKI146BZKQySQBMckkWJwc70RgxMFH3qvXloyvKyb7tUB7hEen8shqhQ-PAsUrI1gJQq_MC8nuR1cUOBXlfdNWCxmgH6Wn_SEmbufc6ZZ0errs7YDHrZ4mdsB6tBSDk_VYPv3CCkiVGmQUZP73aQ0xyxA_Q-6D-1RZUJAV8ZXjGrSfWtV9GuGRrdzNBbcCnhFpx2wrJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLtk72w8OrM3dwa2Y2gC4cMx8goULQOXjODR6fyQ6bP4huuEcKU2wNXh5KbmR4MKK3acCPvu4WQWvKeXDEKXUMnECWbJLmmE7KYewD15kjgbjXMv-fRts1QYjkK2RUFRtkceDFVxxyGGGQFi3Nlgiosz9DKsDT0O7rFHjqKRBn2Dl77l6fs63NlcS-DUd9nWd6U6nbWqfTxzdhnUklKYE4jFulrgN1rEO75Gq8TM8jwiqvtLW20-wdPaR0paQRJC7egLRaWjDq8bfsgaUMdsMT4-fXaXN2ghYCq01w4HC1CDlP04RqJFhxS8C3pxpJLDTvuFYGL4HadLba3xnKcgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiKwY22S5MHAKMHZDWT6I6H1zeCxHVblQZYNIYl9PS_sP33L67NdBtRGj6tpiw5qaqRSq41oQPgHIO4MfnjTGllj4tGPMlGaFbtk1WSdLq27ZTlccAuwiQQs6zIQ-a5kRUZmC8oX7NDNHxJvG6yYK86Vru4pB1TYtqMV1DYC_N54-uHCb5x38Hmda_RYUFbY3-JlbdAGNK78oDxzERHRnGce-slfSWsKw-WoNq-U1IyQpGsDhhzUzofevhGSlX73n1pd_YTWxBVInP-1jK1T8__G3e_HaqSXldPH09UnH6DeZ7ucIILuZw5izwZprAiwUMji9Z0obwCoNXQ-8gWwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=t6Y91l7JwPj8j4AxAd3mBW4t0OUoTY4mEi6dMTpV1ffsTjFHPDcMe0oPHXm2INpdpkXKe6QhVm4ZNbF_YU3nZC18177dsZ_D4HSk9P3tAHSx4St_0Ab80eNN2CB9GocXUYWAHF8DkrNOTy1J1XGxh2Fcq62J1vxp24B16eOtW-dOi5J8tNFLh2F7AOER8R_ykYYzjQPG4N4Gja1XnmQtBebAYMOu2sMTPZMIxGx2Lu8nRo_emy-v-KvdPWOFAWGI0tXllzpyQdJJ_oY0Oemgms1yj0wc-RVyk7mFPovY6p_qYVP60zYBCX8kgzTo6gz0SJ_3dzOusOn57xnxsV8lRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=t6Y91l7JwPj8j4AxAd3mBW4t0OUoTY4mEi6dMTpV1ffsTjFHPDcMe0oPHXm2INpdpkXKe6QhVm4ZNbF_YU3nZC18177dsZ_D4HSk9P3tAHSx4St_0Ab80eNN2CB9GocXUYWAHF8DkrNOTy1J1XGxh2Fcq62J1vxp24B16eOtW-dOi5J8tNFLh2F7AOER8R_ykYYzjQPG4N4Gja1XnmQtBebAYMOu2sMTPZMIxGx2Lu8nRo_emy-v-KvdPWOFAWGI0tXllzpyQdJJ_oY0Oemgms1yj0wc-RVyk7mFPovY6p_qYVP60zYBCX8kgzTo6gz0SJ_3dzOusOn57xnxsV8lRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTdw8W0PXnXbk6JKzC6Mg0YLoCgbP0KnpIa0gt-rQLKOhj4c4BkfRtwSfpPEPSYKF3nwxwKnvPlxNASzMnlK_zaN872kzk4UOMyTyzDyHwN8BlH7i-_ssoG82l7Y40nrJ9m7xVgc4fpsADZnkiA2aw8Y9yMQRKHbQVF5GqOtWvudk3aLGILu6tMdCILI4wxhTzefqleKP_74AjPf_X3FotcxzVMaC0pq4iD_LNhUpVk29nlOqdO-Z9cOHH7n2intCpG1LzCG5t5PJzFIwqvBGk1V4LWLpL-nAKPg5REXWpSaq3ugdGSGbl3FY-AXPUFEO6wUrr2iynu7uRL_6ZppYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhKuHpWus6pFdfwJhxwNI9ygt4PFfg1ZUFXigzWwZNSYkOpKsamGi3HGz6_bUmr0l9d20qt_QdmQhQyddDiLCl4RlfjnhXpUgI5qqWw59r57Hl3wKuvqvBjab_hPNhhNcBRneUvfqeOeSfCLPZ0EQcbZHAXrE-UcBTEraB2QONirlLQhFet_3t8NZJdLmTiriRkhGISpc1eaVnirRMK6clSBlV035LQOjAsYapTR-Y7rA4iyUw5XrfUBKlcMb11BBDAVWdT-Jj4MePgCYXz-U5JKuSSDm9Qq0daLb-M2cg26BhWBG0233Uf_5wPUJAJRe0K8yd0-2t8sMk6NrOW4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=TnDg8YSXaF6d5tH-FS4EdQDwzHhNeb8M8JxRdoxVYYW78CAy9UMoIQLczhB-Ubrhxq28kvmKnXY_0BHarQw3xLfNMaIILzt41KNL4IF_RlDpvJecDBkH7U9nL7ATaY-4ww1LhkfamNgyniEJaorv8kh4ktr3-jA6O5ge-srhzGlLjEtD2LW2JT4eogJm3VCr27fZA_WPJpwV1zeQqN2JQEUZBOT0TWbPKAcziyYyWg6BYgmhXt4Ch2ej1sjg6LldU9nMhWtphebz0qMZusLqncheaZ76YQLyl9pmK7kSS4fqHKcC6GKxZTykNfxTBDrcqzDG-AoXoepeZCfAvNZsOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=TnDg8YSXaF6d5tH-FS4EdQDwzHhNeb8M8JxRdoxVYYW78CAy9UMoIQLczhB-Ubrhxq28kvmKnXY_0BHarQw3xLfNMaIILzt41KNL4IF_RlDpvJecDBkH7U9nL7ATaY-4ww1LhkfamNgyniEJaorv8kh4ktr3-jA6O5ge-srhzGlLjEtD2LW2JT4eogJm3VCr27fZA_WPJpwV1zeQqN2JQEUZBOT0TWbPKAcziyYyWg6BYgmhXt4Ch2ej1sjg6LldU9nMhWtphebz0qMZusLqncheaZ76YQLyl9pmK7kSS4fqHKcC6GKxZTykNfxTBDrcqzDG-AoXoepeZCfAvNZsOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRSLuHZGafBxD7gh9Bk7sPTyNRmPFmjiaUzfgcXj3T4VuHIqRL8kHxwYjbqBAyoSqhbFf5YGmKd5H6ngTLoltBrOyY-dfJlhjXeQOou_APDXcALzcHry7yDBl1bvkhkJkXluaWbOII_zRxcB8LibtawnXMwV3OPx6bHWN_G3FEXxzJHnmMH3WnDIC7FMSzI9GLnpa0xokjBO1eE8wh29h7Dwfpq4b9riToJkCbQMqFxTWRvcFLeDzAPs7xgif_3UZlm0I_vnInO3EziXumwZwRm5K6Mzj_hvmLQnDg_HRxSXPxXtmulf8CnQ9UWBQGCpsd-WVA2xMYaehH5Ub5NATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUV2i0TpscsPPRzJYYeJCvf3q_p4dUaX35-BMjqDK4B0FirMAc_sA3APdCgCLXJMe3fL0QPavqURYoilfjaAkB2KhDxciAPy-MfF5D_gZqW1ycrIZofDGWWFoxQ24II9j1OVXj-M-FtVDgRueFMTAA6BRLt4V_vWnlUE0o6F6RMH6Lw_7eJVpg8vDtUyg490JVjFGayt81B87glQ1zfSbRVDsyat0HWUGRY53Xmpf-LsxI9sIrzeUT7gUdKqM62Ur-IkPRqDMIAPe9_irnx06KfJcrqFLSSxuH7t8YlGM-aIzEjWuUjP9CGNj5UdKjPcW7ecgplcrUICsDefLGJCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxldBrOzB6Q-kLhPRV3OiZdk02F1MM4rwRZIc0xuqsrMWIylk3rpmJcy3H1pA_3_eyMrHqgWCFPE_4uiCIGAvayIbcv2ShiMLvVJqf57O0lj73UgrJS_QJUfWcQziymu3gd7v7pzO_RLNQeYeIpc_SqnJ3_5PO1rbYLyXNntskZvqMBuNrO1sbqsTTb9vjGLJ4uJQmlo0enqJDj1i4EuDD4dEoqhkSQkNahu3-u07r_YoD6H-7k0fagyQ4lC7mJdnJwYm-BlTgLhMfvZOsDDn4Nbaf3tchfCwrri-vvJiOdor9OFX1cv4ky2Q3zRy2Wxz94V3ypRYeeF1Gg_NvbQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW3Jfne-zQM8FstxnP4Hf-GNnev3XT2Tb4TT83ynA3OjQFyh0S0FGiXzPkPE6h4jDZe_bmZeQZoPCCGoL0cWKh_SEGSnCzSLDJJYfsZx3-o5L-yrZYJNjkm26InckAxUa75PBT2YRr8qF4R_eeUTbCFd2X5VNI8MzkJMZWPq8DpypoTWAl0QqH7C4NS6IWXSxhURJ-Us626272LwmhWe6JWOmY24IMkyzNm1pWJf4zYkhT9AvhUdewVdTPICE8_Qi4yqpGuPFoubsDZi8O5FSSF2UwQwJ_mdf4Fl3Qjp4L7cwLb-S18Fg8wUS7-fEefXZEa-c5AmmGOkxJ0Rs9Nzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqLbBC5pczFCEeZRYV6giXrolnh1DB1c_-2g80eS8a6baIMPcp7p-ToU9uQrgHux1fq6r6i9fu3pJhyvBl6ZyK9EfwSjwQOqPnO_Ui5o_kBPqmhq1cWOWapHjZt8Og6liLfAiFkWqqNcYWzb-EjIuXow-E8FzwRTDGghROVNAK_HSJvoqpv4uE_Te-7YJ-Z5NrbDN1ebTureC0QQZqsBt7IJKS9_QCdGTSvydue-NUU-FZ2ElSFqsu3jJdV7aeQbxfbnm1A-yKukrHVh4fRIYHTK0RArFUEvZA-kdLTD34Rg5Zh9w5E8oWCoUrwMhkOZ0WPE9WjnG02vF_uQnwwcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=FD5d0Y_VHGQOafCnu9skb8JX-ZFPI4umSfijgLQI7cd0z9-Y-T8omb_1HmLUgmKoLYxaSyCEcOzeFjgjIGUduAXl3ApDcQLrtp_uMNFQcg1J0XDo_5k5N92cxqXAE7LutCh0XQ6k9ieNnGUkSBCmHxiN3A3xzV39FkX6HE5np-Bdad8QpWH5KnkmMSBnWK8wamT4_DbAnzgH-0ryQFlj6HXFToaZWLbTyunANm-e7Z7tNHYnMjvC45TKy1620KNcfJzlOUcKpFIhPqnRAD6ddy1GcuYT6f5gPo3gWNw5vB-367vEni9wtA-evc2vfBeXeuvkaDjNeTkHwZObqhWJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=FD5d0Y_VHGQOafCnu9skb8JX-ZFPI4umSfijgLQI7cd0z9-Y-T8omb_1HmLUgmKoLYxaSyCEcOzeFjgjIGUduAXl3ApDcQLrtp_uMNFQcg1J0XDo_5k5N92cxqXAE7LutCh0XQ6k9ieNnGUkSBCmHxiN3A3xzV39FkX6HE5np-Bdad8QpWH5KnkmMSBnWK8wamT4_DbAnzgH-0ryQFlj6HXFToaZWLbTyunANm-e7Z7tNHYnMjvC45TKy1620KNcfJzlOUcKpFIhPqnRAD6ddy1GcuYT6f5gPo3gWNw5vB-367vEni9wtA-evc2vfBeXeuvkaDjNeTkHwZObqhWJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYRs-gKHSeVcZ3-nEEabzeJZX7RscBavuA1QpKq8MU4nt7GEotatdySNwIebIFPdn9RxSQaRzj1K4oMEh0pSiQMBfY_12l42kGa9GyqWIPe20vwRUxxgvKctsbMZDcUwLKQjoeicq3dbknVzr-_Lxez0EJANDlauGsdDYZjt1-oY9L4p4Jt7feTOe98nlRpLiCLkNjO_6LaPZr3Ko2FLMcvDZTNkXO-DU1jT6VHAA_DIIWTC6RioVj07fa-IWXCDGewqEDvR05UhpVQIwpRy4Dlio6f_wyHX2wXGh-2c6HdVe2WoI4E_3UkTkLR_pUU85T8qnOKif6AKW8Zj8F1O8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=PpUcNmoaG2rgnluga0p_sa7pyC15Zd1oV3trBCc97LYbLUhZRsOJrKIW5n97QVkzfIWgVGf8YTxN1bBpdp20UGJO8g1p8ge5U_oiGJ8gSNp4RA-Z6uqC1jL-waik6HHYcNHYUEf6uQvNsmpPW_fv03KFx1FiUrlT5_PgxHxqaBk3BrzpXDyJMwvs2ldgnrzkHFXlssjUOu3fKGObyL_Au3gaPN_qu5JFeWL-JOYQ1PbEqp8Oy_UytVyND5y2WmNWlvO3iq4l_JXjjLym5UznRD8cjSg3khpz5vZm_2zU8r_jsPR-lKNALNqOQbzQ-0GTfaVZG1qhE4QL--GB3zw0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=PpUcNmoaG2rgnluga0p_sa7pyC15Zd1oV3trBCc97LYbLUhZRsOJrKIW5n97QVkzfIWgVGf8YTxN1bBpdp20UGJO8g1p8ge5U_oiGJ8gSNp4RA-Z6uqC1jL-waik6HHYcNHYUEf6uQvNsmpPW_fv03KFx1FiUrlT5_PgxHxqaBk3BrzpXDyJMwvs2ldgnrzkHFXlssjUOu3fKGObyL_Au3gaPN_qu5JFeWL-JOYQ1PbEqp8Oy_UytVyND5y2WmNWlvO3iq4l_JXjjLym5UznRD8cjSg3khpz5vZm_2zU8r_jsPR-lKNALNqOQbzQ-0GTfaVZG1qhE4QL--GB3zw0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=U2Xv5Bwao6REg5pfOa9tjeIV2AIKfeMz5UYXvXWz5B3hmkHT0SZJ5Q4n2KB7F8ms5Xtni88sTaPQPF-rAEWEihlMVy87568DejDoel0srkDqsxujyOCrlE6xxXEZcHc1va68HTNfjiS6H_zWrN8vzxFwyN9ykbEqphuWXQRSyIa7stVX220XXBDt2Wx2tJXNzO_CzIiubwtj6HSGR_9zBKeZcAe8EKBAnWrTOTP4Uz0WUkkLuDoA5XVBK5r_Icq6e3WwLttkuRjVQjFgr3FDyNhydiLGbySNFWU4KBidXufX4fpjRMbIemnuSKuvNm_g9_RkBMJe70IpNtO0ToJ_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=U2Xv5Bwao6REg5pfOa9tjeIV2AIKfeMz5UYXvXWz5B3hmkHT0SZJ5Q4n2KB7F8ms5Xtni88sTaPQPF-rAEWEihlMVy87568DejDoel0srkDqsxujyOCrlE6xxXEZcHc1va68HTNfjiS6H_zWrN8vzxFwyN9ykbEqphuWXQRSyIa7stVX220XXBDt2Wx2tJXNzO_CzIiubwtj6HSGR_9zBKeZcAe8EKBAnWrTOTP4Uz0WUkkLuDoA5XVBK5r_Icq6e3WwLttkuRjVQjFgr3FDyNhydiLGbySNFWU4KBidXufX4fpjRMbIemnuSKuvNm_g9_RkBMJe70IpNtO0ToJ_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=CL7vSljf6A68sN-glBOFeSY3uyNlWag_UIvK3ZN0EcHN-3R44tU-PS_f-x4uYuIz-n5e_O9ai5Jbjc8XNWnSAp-42-ObvjBaSDKS4xCO4eU7MpySQemMGHFAAVdsJFpq9yOb2m4StCGoIAkgYi5q38IOtJ9Z3WCOSwZkjAy8L3ygd0N4PHUmURNcwQZYigFKgo8gWfEWHneSK77xBkA2gThnzpoVaPrUUKRYoQ0OvkdWxFkYcXEFr-xA_xRY4gqN9uP9VtwfUu8WqMLufbDUIKQVh7-C67KDFtBaz4vXF0fJO6aMABxrIX61Sct0oEeU88psXxkItAiJJUX75WF_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=CL7vSljf6A68sN-glBOFeSY3uyNlWag_UIvK3ZN0EcHN-3R44tU-PS_f-x4uYuIz-n5e_O9ai5Jbjc8XNWnSAp-42-ObvjBaSDKS4xCO4eU7MpySQemMGHFAAVdsJFpq9yOb2m4StCGoIAkgYi5q38IOtJ9Z3WCOSwZkjAy8L3ygd0N4PHUmURNcwQZYigFKgo8gWfEWHneSK77xBkA2gThnzpoVaPrUUKRYoQ0OvkdWxFkYcXEFr-xA_xRY4gqN9uP9VtwfUu8WqMLufbDUIKQVh7-C67KDFtBaz4vXF0fJO6aMABxrIX61Sct0oEeU88psXxkItAiJJUX75WF_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
