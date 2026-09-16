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
<img src="https://cdn4.telesco.pe/file/hejHqzUpMzzX9DxeFZL0MfxDD0g86OSyNx5bvdbsZnjmU0RhnERMh9wkGfThcuplrm1pwJPscV-f4dZsc-qlsHLAH5WPw0R6v9dz4VIKYStW4aZKhb2gXPRB8CRSPQ_Y1Yim_ILwW-8nQzmeJQMR3_Y7zWyfqVumHNnva8RMgLzzJE3RsF2XNVbISMxSby9bvK_J9Ic-frPQp88XPOpvy3crmWJrzeGHSgo8BWLsGSREj9yP3xAAoVQ-x0DX67zBISIIMbJqUgv6s2XjMzEVPQfJr4qbINQHH0_jFlrdr7GBpRMA-EhRvo_XWxeK-pE9k3Pob-vk3utejqwmeSv7Lg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 929K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-147692">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان به خبرگزاری فرانسه: ما به دنبال توافق امنیتی با اسرائیل هستیم که می‌تواند مقدمه‌ای برای توافق صلح باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/147692" target="_blank">📅 13:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147691">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
به زودی اروپا باید منتظر پاسخ ما به ارسال پرونده هسته ای ایران به شواری امنیت باشد و عواقب آن را بپذیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147691" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147690">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر رفاه: برای مردم عزیزمون کالابرگ رو حداقل ۳۰۰ هزارتومن زیاد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/147690" target="_blank">📅 13:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/147689" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دبیر کمیسیون فرهنگی: شادمهر عقیلی اگر برگردد و در چارچوب اخلاقی نباشد، با او برخورد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/147688" target="_blank">📅 13:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پیش‌بینی بارش‌های پاییزی فراتر از نرمال در کشور
🔴
رئیس سازمان هواشناسی: نقشه‌های پیش‌بینی نشان می‌دهد بارش‌های کشور در پاییز فراتر از نرمال خواهد بود و این وضعیت تا حدودی در اوایل زمستان نیز ادامه دارد.
🔴
هرچه به فصل زمستان نزدیک‌تر شویم، سیگنال بارش‌های فراتر از نرمال در نقشه‌های پیش‌بینی کمرنگ‌تر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147687" target="_blank">📅 13:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: بزرگ ترین حمله را نتانیاهو تدارک دیده است
🔴
۴۰ هزار بمب و ۲۰ هزار کلاهک جنگی: تسلیحاتی که دولت ترامپ در قالب یک قرارداد عظیم در اختیار اسرائیل قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/147686" target="_blank">📅 13:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
زلنسکی: روسیه دو بار تلاش کرد هواپیمای من را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/147685" target="_blank">📅 12:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmIwMaU-eknVkXrCTSrKVCgQaqx6qVtfDLpf-WbWAkxV-XVlrUIlrdkdxVBdVxq0QfNLriPH49g2k8uE6MP2Lj6h5gAjg6Z-1rzGN38Eh_kEvGQyVCTFOmoXlS2K4C1-ktJnjlVdDHFpqOAi2qvRrPZX1LeU0OJ5acQr_t9bhsbSE6ZkABLTitQ8gTl-DiZzhok0cdvKwUKUIkFCtf2RheCEQyEgkihWahTCmcLX5eJKYqQOkd0SPU0c2NWNdWe7W3Hl8f8kxlOVPVx8FpwLiCnGXb6P5DsTdoWX0ORckI41bLczpFK6ZPFtuK2nWK4HxKMsHBRscg9BwkKJ1FgQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سازمان ملل متحد قرار بود در فرودگاه صنعا فرود بیاید، اما قبل از فرود، مسیر خود را تغییر داد و به فرودگاه بازگشت. این اتفاق همزمان با حضور یک هواپیمای سوخت‌رسانی سعودی در نزدیکی یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147684" target="_blank">📅 12:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c0324d63.mp4?token=gIENMVFfun1_N_aRftt-BzRiYsMHlu5d-wyXfGNaD-ViMhFrdDjU33lanGeMuWs3_U39e-bPus_LoJyTAWjjTOdXNOJE-KQqRJNbzNNSNIyhaAd4_rZAAgkJzmLn9o9s8ApG7Z7eYEs9uUKSwTKldUJyQRPQlHds5rRRX6ngzLAZgr5kB6oFdnFLRf9C8py1TU8WMiC9o282r4DaFDa91--_fAIxsBkGTfbIm29WLx9bXybx9Xk4sAGOv93fPg4Z-oEiMJwQgYQcZxd_-M0zPePAwR0ZfibAIQ2pnjQ09UxU9o1yev2b5KbmPe1ecKIxAHa0vYxT7Xin0CGitIf16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c0324d63.mp4?token=gIENMVFfun1_N_aRftt-BzRiYsMHlu5d-wyXfGNaD-ViMhFrdDjU33lanGeMuWs3_U39e-bPus_LoJyTAWjjTOdXNOJE-KQqRJNbzNNSNIyhaAd4_rZAAgkJzmLn9o9s8ApG7Z7eYEs9uUKSwTKldUJyQRPQlHds5rRRX6ngzLAZgr5kB6oFdnFLRf9C8py1TU8WMiC9o282r4DaFDa91--_fAIxsBkGTfbIm29WLx9bXybx9Xk4sAGOv93fPg4Z-oEiMJwQgYQcZxd_-M0zPePAwR0ZfibAIQ2pnjQ09UxU9o1yev2b5KbmPe1ecKIxAHa0vYxT7Xin0CGitIf16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج تازه‌ی بازداشت بانوان توسط پایداریا در کابل
🔴
دست کم ۲۰ زن و دختر در کابل بازداشت شدند و  گروه خودخوانده طالبان از تشدید نظارت بر حجاب و موسیقی خبر می دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147683" target="_blank">📅 12:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzzeogplRETTSSQVJBT_w-EIPbSS0zgi30_ydY2vPcVWyFizN0xwv3QVzFt753AMNjKQ8LbDr76_SJXJivemcClKezdaevhR8ZUYta8y7QBeW_PdJJN9-maxSzgchGnIicGEwQ4LUsB8ocJQZwn9O8NI0wVSazcygnM4EP99iTGvtoGi17l2g_3LeKAkUaHYrOIcxg-h9uCqDAWmz1rkAQJiLAWOxLgyTRns5OOnt44xQZCUpFkipvSR4nu8jNPNK3Cr24FhlvlRNcJZrIVfdzEeePxoyGYYFz8BN4DRR9QfTf9Ixw0jWeQ4w8fyJZhmY7Px4cGgm69KDcz4TIna6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
تخفیف فضایی تپسی‌فود
🔥
تا 50⁒ تخفیف ویژه رستوران‌ها
همین حالا غذات رو از تپسی‌فود بگیر
🔥
از اینجا سفارش بده
👇
https://tapsi.food/?utm_source=telegram&utm_medium=social&utm_campaign=fz0625
⚠️
مخصوص تهران و مشهد، کلیک کن
☝️</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147682" target="_blank">📅 12:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02cc6cfc9.mp4?token=jZ5SUTfw1Rjvx2GuGG9bns5wNQEpYi6IWFHCslftHR1UzhFX5VjHutNEozntCdFliq8MiSjO9TX3dcA3U1YW4EpeWByOVKw9Qw_53WtALNoln6WWmjEvkV3tfzIXBtigSwCxf0m_2RhzrjJvAcTpxifZXLiRpRinR8mY_nbcr-7fOzLlpTOFT-1biUUL10Z1wTxo17C1ap6nxBL-fEBd8exaFiBoheR0Olu8v8Otc07xcrU9JkQV9XpsMt3EplOJXQ7NJF0JDBUdtsJ2gt3DyJcDsLVA91x2FHRL4ZDGYPZQ10tG8grssk72ZDZweCacCAbxdZfFdQjcb5RaokBlBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02cc6cfc9.mp4?token=jZ5SUTfw1Rjvx2GuGG9bns5wNQEpYi6IWFHCslftHR1UzhFX5VjHutNEozntCdFliq8MiSjO9TX3dcA3U1YW4EpeWByOVKw9Qw_53WtALNoln6WWmjEvkV3tfzIXBtigSwCxf0m_2RhzrjJvAcTpxifZXLiRpRinR8mY_nbcr-7fOzLlpTOFT-1biUUL10Z1wTxo17C1ap6nxBL-fEBd8exaFiBoheR0Olu8v8Otc07xcrU9JkQV9XpsMt3EplOJXQ7NJF0JDBUdtsJ2gt3DyJcDsLVA91x2FHRL4ZDGYPZQ10tG8grssk72ZDZweCacCAbxdZfFdQjcb5RaokBlBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هلی برن نیروهای ویژه اسرائیل روی سقف یک خانه در اطراف کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147681" target="_blank">📅 12:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ: پاکستان در حال بررسی گزینه‌های خود در مورد یک نفتکش سرگردان در دریای سرخ در نزدیکی خط لوله شرق به غرب عربستان سعودی است و هشدار می‌دهد که هرگونه حمله به این کشتی به عنوان "عمل جنگی" تلقی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147680" target="_blank">📅 12:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سی‌ان‌ان : گزارش‌ها، چهارده ماهواره جاسوسی روسی چند روز قبل از حمله ایران، بر فراز یک پایگاه نظامی آمریکایی در عربستان سعودی پرواز کردند.
🔴
مقامات آمریکایی گفتند که اطلاعات جمع‌آوری‌شده ممکن است با ایران به اشتراک گذاشته شده باشد و این امر به انجام حمله دقیق، که شامل موشک‌ها و پهپادها بود و باعث زخمی شدن ۱۲ سرباز آمریکایی شد، کمک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/147679" target="_blank">📅 12:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
تو سایت های شرط بندی احتمال حمله نظامی یا اتمی ترامپ به ایران تا قبل مهر ماه به 84% رسیده!
🔴
بالاترین عدد تو دو ماه اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/147678" target="_blank">📅 11:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: توافق مکه روابط با ایران را تحت تأثیر قرار نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/147677" target="_blank">📅 11:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=dPDxRbvO6RFzj-g4MuNl-AcfqGR0iJeHxQMO5MZPILPdaKAJsSvv4f3kYLS63ySp5MhxvoRM8Pv7jxVZ9b7qZ-WlaBox720THDdP-dRmdSAY20FNG_eA-ZW0mCTPeLpc0RNBhqyZGfwRD9rxs3r0JbVioIlVQhK_3qGPawnBxdKSCZkwLzcC7R5qwBnFhDvbXWt_ncqt3ZW-I5-3ZqKuT8jtVF_YPWBKC_INoMjs10mrugo7OqUhmYi1zIDhXnwbOW09NBxt78uIOPX4XhcsAiTcas6EWILpcSithMcREWwDHkKievFHt8ms_jMSA1rhKRf1QX6dl4ogpZFcZ2W8_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5da33205e.mp4?token=dPDxRbvO6RFzj-g4MuNl-AcfqGR0iJeHxQMO5MZPILPdaKAJsSvv4f3kYLS63ySp5MhxvoRM8Pv7jxVZ9b7qZ-WlaBox720THDdP-dRmdSAY20FNG_eA-ZW0mCTPeLpc0RNBhqyZGfwRD9rxs3r0JbVioIlVQhK_3qGPawnBxdKSCZkwLzcC7R5qwBnFhDvbXWt_ncqt3ZW-I5-3ZqKuT8jtVF_YPWBKC_INoMjs10mrugo7OqUhmYi1zIDhXnwbOW09NBxt78uIOPX4XhcsAiTcas6EWILpcSithMcREWwDHkKievFHt8ms_jMSA1rhKRf1QX6dl4ogpZFcZ2W8_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏اعتصاب عمومی در سنندج و شماری دیگر از شهرهای استان کردستان بخاطر سالگرد جاویدنام مهسا امینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147676" target="_blank">📅 11:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رو کدوم سرمایه گذاری میکنید؟</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/147675" target="_blank">📅 11:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
لحظه رهگیری موشک بالستیک حوثی‌ها توسط سامانه پاتریوت بر فراز مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/147674" target="_blank">📅 11:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یدیعوت آحارونوت: هواپیمای نتانیاهو از ترس اقدامات شهردار نیویورک، در فرودگاه جان اف کندی به زمین نخواهد نشست
🔴
مقامات امنیتی اسرائیل نگرانند که زهران ممدانی، در طول سفر نتانیاهو به سازمان ملل مشکلاتی برای او [اجرای حکم بازداشت] به وجود آورد؛ نیوآرک یا یک فرودگاه نظامی در نزدیکی نیویورک در حال بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147673" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر خارجه چین: از ایران و آمریکا می‌خواهیم به تفاهم اسلام‌آباد بازگردند و درباره مسائل باقی مانده، وارد رایزنی‌های جدی و اساسی شوند
🔴
طرف‌ها اقدامات مؤثری برای بازگشایی تنگه هرمز اتخاذ کنند
🔴
نمی‌خواهیم شاهد کشیده شدن تنش‌های منطقه‌ای به یمن و دریای سرخ باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147672" target="_blank">📅 11:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بلومبرگ: شرکت کشتیرانی ژاپنی: بازار LNG با اختلال طولانی مدت در تنگه هرمز روبرو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147671" target="_blank">📅 10:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۳.۷ ریشتر در عمق ۱۰ کیلومتری، کنارتختهٔ فارس را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147670" target="_blank">📅 10:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eccbab7fa2.mp4?token=oXna3LQUb6Ha6kuOa0cHUhaTtwJ6V3R_PKwvEwOUMZVC524bLQoVf8ACXFc6doPS-r-5-cPoP5XLff0QQotijEgnOkwhcXT1qU5jfixk9wuvDKayOVkm6X51S6iYhuV0oCC5qiGtsECIfo_bw4eDWeHV4wlJd7Cl8JzpRhMRgpETSvMXJX_l7S2N6kzL9vXl5fVFzn5x7gu6FwmKIaf0sJcrbF0sUcoMxYxzVlveyTBOhci16PQQHfJBMHu5qtZeCjm_9oPNEGzsBVycvLbBx5fIM13M1MpRwQdUGJ8GJ4ZnpzjB5DQk6nzEHqlvMWyUYudu1l_vGYFlg2ED87RGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eccbab7fa2.mp4?token=oXna3LQUb6Ha6kuOa0cHUhaTtwJ6V3R_PKwvEwOUMZVC524bLQoVf8ACXFc6doPS-r-5-cPoP5XLff0QQotijEgnOkwhcXT1qU5jfixk9wuvDKayOVkm6X51S6iYhuV0oCC5qiGtsECIfo_bw4eDWeHV4wlJd7Cl8JzpRhMRgpETSvMXJX_l7S2N6kzL9vXl5fVFzn5x7gu6FwmKIaf0sJcrbF0sUcoMxYxzVlveyTBOhci16PQQHfJBMHu5qtZeCjm_9oPNEGzsBVycvLbBx5fIM13M1MpRwQdUGJ8GJ4ZnpzjB5DQk6nzEHqlvMWyUYudu1l_vGYFlg2ED87RGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: ترامپ تنها رئیس‌جمهور ۴۰ سال گذشته ست که حاضر بوده بگوید: «بله، نتانیاهو شریک خوبیه، اما من و نتانیاهو در این موضوع نظر متفاوتی داریم»
🔴
یا «نتانیاهو در این مورد اشتباه می‌کند» یا حتی«از دیدگاه اسرائیل، نتانیاهو در این مورد حق داشته ، اما مردم آمریکا چیز دیگری میخواهند.»...
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147669" target="_blank">📅 10:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XSwNclDdWFgUJ6uHGP11UZAjQ9ogfWZF1BdEPzNcEyJt2wbUAd7P3UKDFfZzMLOYvi3UJuqim1RWlPIW2EBXn97Wu03nzKVAcXLu1ZhbcT5ua-dH7dd16FohwobNA2QEaY5cmrWCBbG2lYq7Pk-PJ5gP_UbCuXt9R41otrp6-mIye5bg5D2pqFswbQUMHpJELATm5YTRascz54MVvLu0nfXPLhraCHr8CbSMHTee6iHmBcCuqu6rKWfeZWGQScUxLZdW1Vhs_lCznCtFqTkfj6eY5C_BNmkceb2WgESkFtPZIfyAfyquyuE6XOSf53vCU1mcvr0AZxmAOyKPUkY1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان: حمله پهپادی منتسب به حوثی‌ها علیه مکه را محکوم کرد و گفت مردم پاکستان از «این اقدام توهین‌آمیز» نگران و ناراحت هستند.
🔴
حوثی‌ها این حمله به مکه را رد کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147668" target="_blank">📅 10:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ca794428.mp4?token=lEYMjGkJysTA8P77mHmVeFEUBozVxOE4Nt0-0JIY4qmg8BeR_WepG_agj_Wdj5l_1yduAbPqMAMDOmJx03ry4VYKBRjqMaWp9XkDPjXWpc5HE232VmxHpaj1slrV1QV0b24eDaldBwKUVZ6QgmNtuFXXTctDcFS6OHNqUC91CXig4aZRSBbjRl_RR6-c0VCWQXMGYZVvo0RJ5OWq1HsbQz8q34hLrNJurCC3jspcp9fJjh6qOAPBQa7DpM8ASaie6pAgG_GK0h_BLOG6NUnmcuFFgDmV8W9Fpl1Y_d1rHcho4Ft1gJG1clsN9qJzy3okdhx8kFCdA0e1omyKm4kUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ca794428.mp4?token=lEYMjGkJysTA8P77mHmVeFEUBozVxOE4Nt0-0JIY4qmg8BeR_WepG_agj_Wdj5l_1yduAbPqMAMDOmJx03ry4VYKBRjqMaWp9XkDPjXWpc5HE232VmxHpaj1slrV1QV0b24eDaldBwKUVZ6QgmNtuFXXTctDcFS6OHNqUC91CXig4aZRSBbjRl_RR6-c0VCWQXMGYZVvo0RJ5OWq1HsbQz8q34hLrNJurCC3jspcp9fJjh6qOAPBQa7DpM8ASaie6pAgG_GK0h_BLOG6NUnmcuFFgDmV8W9Fpl1Y_d1rHcho4Ft1gJG1clsN9qJzy3okdhx8kFCdA0e1omyKm4kUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه رهگیری موشک بالستیک حوثی‌ها توسط سامانه پاتریوت بر فراز مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147667" target="_blank">📅 10:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
جی دی ونس: اسرائیل در زمینه فناوری نظامی و تبادل اطلاعات، شریک مهمی برای آمریکا بوده است؛ اما در عین حال، ایالات متحده همیشه و در همه مسائل با اسرائیل هم‌نظر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147666" target="_blank">📅 10:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
افزایش ۶۰ درصدی ثروت ترامپ بعد از بازگشت به کاخ سفید.
🔴
نشریه "فوربس" گزارش داد که ثروت دونالد ترامپ از ابتدای دوره دوم ریاست جمهوری در آمریکا، به میزان ۲.۷ میلیارد دلار افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147665" target="_blank">📅 10:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a47484293.mp4?token=rlN5ja8HMIPkADImueFEIwx2CTzJkx491lKuhh-wz5EBTE4k2DJJp1MCUFh1I8SPCfIUuWT5EOQE0D9F8f9PDSptokI8ORtnMt9GhbJzRsgBtf-fAoa7l7c1EhN_osOM2ERIZhRyO3TSwgTTK8lA10Uynf8p0eaQ1KgPj4HgL3wmw2Eq9Arcz_01Xl073Lzu9kx5jTF9lZWqKackG09In66fwwEgI_BWdU4xRYuK-AB1rMn5Wt833NAOz5Ey-ZY6jUQWtFET4Xp66JoNGUxIZeqfF5LJSOYhd7D9IKsv69dOQ-1tkefHxIxLPNvMjIt1XGmoBLhNPcJik-OZo_p_LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a47484293.mp4?token=rlN5ja8HMIPkADImueFEIwx2CTzJkx491lKuhh-wz5EBTE4k2DJJp1MCUFh1I8SPCfIUuWT5EOQE0D9F8f9PDSptokI8ORtnMt9GhbJzRsgBtf-fAoa7l7c1EhN_osOM2ERIZhRyO3TSwgTTK8lA10Uynf8p0eaQ1KgPj4HgL3wmw2Eq9Arcz_01Xl073Lzu9kx5jTF9lZWqKackG09In66fwwEgI_BWdU4xRYuK-AB1rMn5Wt833NAOz5Ey-ZY6jUQWtFET4Xp66JoNGUxIZeqfF5LJSOYhd7D9IKsv69dOQ-1tkefHxIxLPNvMjIt1XGmoBLhNPcJik-OZo_p_LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: «حتی اگر در همه مسائل با ما موافق نباشید، طرف مقابل درگیر دیوانگی شده است.
🔴
آنها تحت تأثیر افرادی هستند که می‌خواهند همه‌چیز را از دیگران بگیرند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147664" target="_blank">📅 10:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220ab7f29d.mp4?token=Rpu6EkD8an3dYpJWjnXaZjN4vXI8izvzfuRg1hvOoFc8_Im_n2dCiRUxl-WrG6Vb9oQKmCmWqMVEdg40cT7iA0DdvC9mKtD_9e6WdnMIC3VuWYSadNajtcGqDfz3iJErwTI1RSrfKtbFk99HsY02hHlZQqvF-M-RJvoBg11HoTKGi_sOy7dewWvbEMBxZWrqlpl3SIgwAIxJvIpoR-VDnBVm85zcLvnkbXdsJ4dOYwDJ8q0IjrWrgJ9O1Df3koJf4seSdc8T1qaUkdZma4XarzV3DRsqVnkdHCSXpaq8BGE-apKXl7i1fClaN1uy5bnag9dBhRK7Tynuta462gmthQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220ab7f29d.mp4?token=Rpu6EkD8an3dYpJWjnXaZjN4vXI8izvzfuRg1hvOoFc8_Im_n2dCiRUxl-WrG6Vb9oQKmCmWqMVEdg40cT7iA0DdvC9mKtD_9e6WdnMIC3VuWYSadNajtcGqDfz3iJErwTI1RSrfKtbFk99HsY02hHlZQqvF-M-RJvoBg11HoTKGi_sOy7dewWvbEMBxZWrqlpl3SIgwAIxJvIpoR-VDnBVm85zcLvnkbXdsJ4dOYwDJ8q0IjrWrgJ9O1Df3koJf4seSdc8T1qaUkdZma4XarzV3DRsqVnkdHCSXpaq8BGE-apKXl7i1fClaN1uy5bnag9dBhRK7Tynuta462gmthQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: خروج آمریکا از معادلات خاورمیانه می‌تواند به بحران جهانی انرژی منجر شود
🔴
جی‌دی ونس درباره ایران گفت: «اگر آمریکا عملاً به خاورمیانه بگوید که از این پس خودتان باید از پس مسائل برآیید، تا زمانی که ایران به حمله به کشتی‌ها ادامه دهد، نتیجه آن ناگزیر یک بحران جهانی انرژی خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147663" target="_blank">📅 10:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدراعظم آلمان: ایران فورا تنگه هرمز و حوثی ها فورا باب المندب را باز کند؛ ایران باید برنامه هسته‌ای خود را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147662" target="_blank">📅 09:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147661">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoOHbuUHPGDyZMG9zVpBZkotl0fqO3bWKDih8RAt88uoPTNJUORu7GICWieymi2zHEyjB8gIC634fidwqdCpFUjp87XX0FkTLiMiDTCK7dWheZVxJNd_-lt-O9mHI40inLkhnp6KtiVmFVA5SPmpkfwF6FTDkZE7Q1mF186_J99H1f0IolLgC23S_7zLGR5zrjoKS6XI4ejghiyeT-suvLWJcUgQsbdiRhMA9vZxYeKUq3Y7NASixG6XSm8PJP06SRZH3zvPbo_gRoSXpDNS0X3rFFXApQJ8R7n_4nT2HkbV31K_FNXOKCCijKijPl31ssTG7JRJw68XhtIRKRtEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان
:
در واکنش به حملات جاری روسیه به اوکراین، جنگنده‌های خود را در حریم هوایی نزدیک به مرز اوکراین به پرواز درآورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147661" target="_blank">📅 09:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147660">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e663b6aabb.mp4?token=hQL7bNR9hERoF2_G4-3awjny8GPAKXTASk4gFO0aMyFxOWM9xZp3KsXa-lhSfZHqtuFn5X-c4gDtyvzpNw0z-4J8fVWJGnFU0MsQUlxMO-jj113kmp1DGcK3ZQ_NvJqVb_ANFufTCAewir8PfEPQ8Tr8Nd68nWY6HeUyNAmH9FnrgcjnzNW1kMEpfEt0ogWz4oyPzmm6GUQr9fJb_nllJNFU188PAlw7jm1ADDZ3N5MTrAQ4pM6018RE0Y1_NJ856ymbb1jec_HSvoY085GckS2X2DjBEoo9ZWaBz883_lZ_IQ459FDoeDyHVxmcy6cZB2u99bbKZLZYsRtPmn81SYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e663b6aabb.mp4?token=hQL7bNR9hERoF2_G4-3awjny8GPAKXTASk4gFO0aMyFxOWM9xZp3KsXa-lhSfZHqtuFn5X-c4gDtyvzpNw0z-4J8fVWJGnFU0MsQUlxMO-jj113kmp1DGcK3ZQ_NvJqVb_ANFufTCAewir8PfEPQ8Tr8Nd68nWY6HeUyNAmH9FnrgcjnzNW1kMEpfEt0ogWz4oyPzmm6GUQr9fJb_nllJNFU188PAlw7jm1ADDZ3N5MTrAQ4pM6018RE0Y1_NJ856ymbb1jec_HSvoY085GckS2X2DjBEoo9ZWaBz883_lZ_IQ459FDoeDyHVxmcy6cZB2u99bbKZLZYsRtPmn81SYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: «ما نمی‌توانیم اجازه دهیم سیاست خارجی آمریکا در خاورمیانه تابع دولت اسرائیل باشد.
🔴
ما زمانی که با دیگران توافق داشته باشیم، با آنها همکاری خواهیم کرد و زمانی که اختلاف داشته باشیم، با آنها مخالفت خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147660" target="_blank">📅 09:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147659">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
یحیی فست: اف-۱۵ سعودی را در آسمان مأرب سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147659" target="_blank">📅 09:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147658">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: روابط برادرانه ما با ایران، عاملی تعیین کننده در موفقیت روند میانجی‌گری بین تهران و واشنگتن محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147658" target="_blank">📅 09:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147657">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یحیی فست: اف-۱۵ سعودی را در آسمان مأرب سرنگون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147657" target="_blank">📅 09:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147656">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fd5bb0a95.mp4?token=fjK07gvLb-zE9wMp_iceLvep1AsQZIe9yZTCySeyyCf89xHrhmsahK0tUE67Z4maESECAdKorCGeI_9JVKpBJYRyqIhrlpAhuuEJ5CqP40AxR7HirVkW16JAcEwgzHhjiXw3n_OqbWd_NlS6L14ZvV4Vdo2DBDbCLClEg-X-t_8_5WRUfADr2lxmca30JPPGS_al2JFiAusmQsaKuCuswku3L8KCym6nnynzin9pC75KulJnI2WLN7BUN83VMiI4U2TlZjTHocgo3Mri5DEHg8WeY0XeVhkVfLR0EaTXlY7Q2M2mq3gCYgA-8GkZQkuFMQTWRSPoNWVSpcDKy8FvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fd5bb0a95.mp4?token=fjK07gvLb-zE9wMp_iceLvep1AsQZIe9yZTCySeyyCf89xHrhmsahK0tUE67Z4maESECAdKorCGeI_9JVKpBJYRyqIhrlpAhuuEJ5CqP40AxR7HirVkW16JAcEwgzHhjiXw3n_OqbWd_NlS6L14ZvV4Vdo2DBDbCLClEg-X-t_8_5WRUfADr2lxmca30JPPGS_al2JFiAusmQsaKuCuswku3L8KCym6nnynzin9pC75KulJnI2WLN7BUN83VMiI4U2TlZjTHocgo3Mri5DEHg8WeY0XeVhkVfLR0EaTXlY7Q2M2mq3gCYgA-8GkZQkuFMQTWRSPoNWVSpcDKy8FvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی سندرز درباره هوش مصنوعی: احتمال خطر هوش مصنوعی احتمالاً بیشتر از سلاح‌های هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147656" target="_blank">📅 09:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147655">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K09FTr4ZOhE-N7u0E6hbqGYe-FucvjdTjqIge29CqdACyaSTXKqWWzMVrFPypaMM9pRVu-TAjZ2qUJXgILRAkuQ1GTv65oG_qRBo9lYPjtmIEkeOU8iV4u9GZ5b9oVkV9t9AQrgxkIwWK_cOwY94lxE1-Pds9JRjssCgck59m8dduNvN1TIH7_d5JrYvwgU4nNkVQuNuHU4dkzn0SkzbUQ1n3vlGOaP3xi2Sp1ekgWC9ox529Mwowje5RMN1ZGUfBIuXwMaTjtd6jiuw_231FHuMa3uD5FTIdcDpU6bewF92P-VUbeQZYapsCEQWnMAUr_YNnqLbMIYJdGOFrJLN9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا:توصیه می‌شود که سفر به عربستان سعودی مورد بازنگری قرار گیرد، زیرا خطر هدف قرار گرفتن منافع آمریکایی توسط پهپادها و موشک‌های ایرانی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147655" target="_blank">📅 09:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147654">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e6dfc0ba.mp4?token=qRV7dCUlaaOA0nOdYbF6TSt0WbqJru3gfpr_QoxLKE6cs31bxoZ3fC7nc_mYB1OaFC9h13L9fXR_q8Jo2I54Fezemw2LJj6oZ_uAgGJaRc-Gjtyo2r0Kh2WIQynjJLzeiHnzc1NEu0a1h4CaqXU10phS3uL-rrSfWTTQX7gh9zy0yaingoznjR7_NiC4XYXCTtjPlAKfo-YtYGtqPjmC1enXPvkSCXr_6-9ig0x65tlK8ShhGjHQDstIMmYdIBysSFoHFiEjNF0uwlXgZ8E-ndzb2O-4xIU9vMk5C2lZtR_keKb_XIMzuljOSKWX9A8YjzDAFCPMbmV8RI16KPF0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e6dfc0ba.mp4?token=qRV7dCUlaaOA0nOdYbF6TSt0WbqJru3gfpr_QoxLKE6cs31bxoZ3fC7nc_mYB1OaFC9h13L9fXR_q8Jo2I54Fezemw2LJj6oZ_uAgGJaRc-Gjtyo2r0Kh2WIQynjJLzeiHnzc1NEu0a1h4CaqXU10phS3uL-rrSfWTTQX7gh9zy0yaingoznjR7_NiC4XYXCTtjPlAKfo-YtYGtqPjmC1enXPvkSCXr_6-9ig0x65tlK8ShhGjHQDstIMmYdIBysSFoHFiEjNF0uwlXgZ8E-ndzb2O-4xIU9vMk5C2lZtR_keKb_XIMzuljOSKWX9A8YjzDAFCPMbmV8RI16KPF0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی در سفر به پکن با وانگ یی، همتای چینی خود دیدار و رایزنی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147654" target="_blank">📅 09:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7b36ce4e.mp4?token=P9O5KF3Q861Gx_hUcCZIyHmtIBLe2QL_i0JOItcWB7geesjtto0s68_xJZCJ4yHIopsaanP9wuJK9VWGgZ88rZKXwPl2G7CQJ8X5ThRz5bKIpF_N0zbqF9iVKd3eLd7wM5vJxc2HGOeNWlYQDUBqL7ja-l1gzzLbFRN-LHe9Waq694VSRzegjr6dFw8WqMjI4ar8LR-cq9l8CqjiCrT6-J4gPN9ZWlT83Vj6GdnXVNNT60_VANWRHqE3gGlfmnK1ZP7f8HToIhtzgPOIjfszU8CW5bpWvYlIZPELGeDJa3yw5jJq45uehNUo_B7BmnCwSuVcSeDkqFP23fnx9vMg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7b36ce4e.mp4?token=P9O5KF3Q861Gx_hUcCZIyHmtIBLe2QL_i0JOItcWB7geesjtto0s68_xJZCJ4yHIopsaanP9wuJK9VWGgZ88rZKXwPl2G7CQJ8X5ThRz5bKIpF_N0zbqF9iVKd3eLd7wM5vJxc2HGOeNWlYQDUBqL7ja-l1gzzLbFRN-LHe9Waq694VSRzegjr6dFw8WqMjI4ar8LR-cq9l8CqjiCrT6-J4gPN9ZWlT83Vj6GdnXVNNT60_VANWRHqE3gGlfmnK1ZP7f8HToIhtzgPOIjfszU8CW5bpWvYlIZPELGeDJa3yw5jJq45uehNUo_B7BmnCwSuVcSeDkqFP23fnx9vMg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط مرگبار بالگرد خبری آمریکا هنگام پوشش تصادف
🔴
در پی سقوط یک بالگرد خبری شبکه «ان‌بی‌سی لس‌آنجلس» هنگام پوشش صحنه یک تصادف مرگبار میان یک خودروی شاسی‌بلند و اتوبوس، ۳ نفر جان خود را از دست دادند و یک نفر دیگر زخمی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147653" target="_blank">📅 08:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گرجستان پرواز شرکت‌های هواپیمایی ایرانی را متوقف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147652" target="_blank">📅 08:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سپاه: بامداد امروز پنجاه و دومین پهپاد MQ-9 ارتش آمریکا را در جزیره قشم زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147651" target="_blank">📅 08:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر خارجه چین: ادامه درگیری بین واشنگتن و تهران به نفع هیچ‌کس نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147650" target="_blank">📅 08:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147648">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
در حرکتی بسیار عجیب دادگستری هرمزگان پلاک ۱۶۳ خودرویی که بیش از یک بار در یک روز سوختگیری کردن رو به عنوان خودروی متخلف منتشر کرد و اعلام کرد از این به بعد هر خودرویی بیش از یک بار در طول روز سوختگیری کنه متخلف به حساب میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/147648" target="_blank">📅 08:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147647">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
۵ فروند هواپیمای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند و فعالیت هواپیماهای ترابری بین پایگاه‌های آمریکا در اروپا و خاورمیانه نیز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/147647" target="_blank">📅 02:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147646">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbd3251f05.mp4?token=I-D_aXYFV4kvu7zJ0t6lEnuoLZUAP7BYx8qhygElL3rx3fkkKw5fMuZPZIfyC9WmgALfBE19VgKaZ8nd4r0jr2yK4sZVGGgwXVn4BabC-UvElCSmKvfdMS3FRrxvA2XMKEhiK4_6oIF8p35adqIiZad-09HKHNHHljEC7HCNG1bzlW_CBisD66cHrdJjU4-Uc6M3SuRZ2vf3S9VdbVRKOfQOVYY5aH5o3RmtHUdJRH13XYTxTI-zLzk4o88vnQ2rWs8Ev-8MBpEQuq9jzi68-ga0FNUHq67xYjYwqSKqEosI8wghfFxqduZVQZUaefORtScsBRUpk3xq0XYNPyvhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbd3251f05.mp4?token=I-D_aXYFV4kvu7zJ0t6lEnuoLZUAP7BYx8qhygElL3rx3fkkKw5fMuZPZIfyC9WmgALfBE19VgKaZ8nd4r0jr2yK4sZVGGgwXVn4BabC-UvElCSmKvfdMS3FRrxvA2XMKEhiK4_6oIF8p35adqIiZad-09HKHNHHljEC7HCNG1bzlW_CBisD66cHrdJjU4-Uc6M3SuRZ2vf3S9VdbVRKOfQOVYY5aH5o3RmtHUdJRH13XYTxTI-zLzk4o88vnQ2rWs8Ev-8MBpEQuq9jzi68-ga0FNUHq67xYjYwqSKqEosI8wghfFxqduZVQZUaefORtScsBRUpk3xq0XYNPyvhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب عادل فردوسی پور از پوریا پورعلی بازیکن پرسپولیس سوال کرد که میدونی چطوری مهدی زارع تو حموم پاشو بُرید؟
پورعلی برگشت گفت آره بابا، من با مهدی زارع، دوتایی باهم رفته بودیم زیر دوش
🏳‍🌈
عادلم هر کاری کرد نتونست جلو خودشو بگیره و ۳۰ ثانیه فقط خندید
🤣
@AloSport</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/147646" target="_blank">📅 02:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147645">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/درگیری‌ موشکی در نزدیکی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/147645" target="_blank">📅 01:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147644">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در عجبم عرزشی‌ها طلاهاشون میدن تا خونه‌های لبنانی‌ها ساخته بشه اما وقتی میگیم همون پولو بدید تو سیستان و بلوچستان خونه بسازیم میگن وظیفه دولته!  [@AloTweet]</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/147644" target="_blank">📅 01:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ4REF5-tDLL38OQwR0MGRhe8kBYFQdlDr5lcYQ449wYL7LkNFr0Jas1vOLc5rK4_ET3Dt4Ti003DM0PtyjUKwG3TgjbHrV0mXI8yrBozKOOfsV9f4flWBe2RjLplTTkdLhIdmsNpaH3c9dr_fN_FV_Q2VfmuGvp6jy1xPBZ2srUdSn_1dReAHbUyR5rTvx6hUOyCSgkkUQwVuRZ9P3Wk_sphKiCOaM93HO0_OROav2bWB5ZnGppRSiM_anRGucN0s6dTtr5jZw-Oh8K33tDNB-gehe8sWbaE_8mb139XhRAiBHnEytJpsl0xYYfvEUzn6RF6gZEpbG3ZGCK8wlfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا با رأی ۲۳۲ به ۱۴۷ و ۴۷ رأی «حاضر»، طرحی برای آغاز روند استیضاح دونالد ترامپ را کنار گذاشت؛ بنابراین این طرح پیش از رسیدن به رأی‌گیری درباره خودِ استیضاح، عملاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/147643" target="_blank">📅 01:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147641">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏
👈
جی دی ونس: ایران تا زمان انتخابات میان‌دوره‌ای آمریکا، به‌تدریج کنترل خود بر تنگه هرمز را از دست خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/147641" target="_blank">📅 00:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147640">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
👈
جی دی ونس:
ایران تا زمان انتخابات میان‌دوره‌ای آمریکا، به‌تدریج کنترل خود بر تنگه هرمز را از دست خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/147640" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147639">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گویا صبح سه شنبه جنگنده‌های آمریکایی وارد حریم هوایی ایران شدن و برگشتن و برای همین بود تمام اماکن نظامی تخلیه شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/147639" target="_blank">📅 00:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147638">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a028d46d.mp4?token=Gj5iCXhmf4fb2BtIoqdHNocmAXses0xLZ-sOU74-WO5Bp2xRX85JKFCyqedIkdZWo1l48-4HNSlKA2d3bFYRh56uyCvKBox-QuGx-f3VMk2etgqiuR4fAuOo2HakCYKd3-zFWT-ZilXbHchZnCoy04RJvoICRbx3zdtSurES0hqRCJGnhh94j7PesvjD0WYVJ0AHJND0dOeFOyc773gvJ8HpR7N3OKN64hqOZJ_ESQ3snXVUd4yK80XDXcyvKSCW3wZTgCBBqWBCVvLJXb5o-cT9izA5Hd3V2rSIeHtCudPHn5nXAF45p07nZvpo0jZ42ZKr7rZfWO3oNMo1YHE1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a028d46d.mp4?token=Gj5iCXhmf4fb2BtIoqdHNocmAXses0xLZ-sOU74-WO5Bp2xRX85JKFCyqedIkdZWo1l48-4HNSlKA2d3bFYRh56uyCvKBox-QuGx-f3VMk2etgqiuR4fAuOo2HakCYKd3-zFWT-ZilXbHchZnCoy04RJvoICRbx3zdtSurES0hqRCJGnhh94j7PesvjD0WYVJ0AHJND0dOeFOyc773gvJ8HpR7N3OKN64hqOZJ_ESQ3snXVUd4yK80XDXcyvKSCW3wZTgCBBqWBCVvLJXb5o-cT9izA5Hd3V2rSIeHtCudPHn5nXAF45p07nZvpo0jZ42ZKr7rZfWO3oNMo1YHE1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند:
گرونی شده؟بدبخت شدی؟ به ما چه؟ یاعلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/147638" target="_blank">📅 00:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147637">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در قشم
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/147637" target="_blank">📅 00:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147636">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترور آلارم : لیست ترور بروز شد
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/147636" target="_blank">📅 00:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147635">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌بی‌اس گزارش داده مصر پیشنهاد حوثی‌ها برای مذاکره مستقیم درباره ترتیبات جدید کشتیرانی در دریای سرخ را نپذیرفته است
🔴
قاهره نمی‌خواهد وارد چارچوبی شود که بتواند به حوثی‌ها یا هر طرف دیگری امکان ادعای حاکمیت یا اختیار بر تنگه باب‌المندب را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/147635" target="_blank">📅 00:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147634">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ونس: جنگ چند ماه دیگر وارد مرحله‌ای کاملاً متفاوت خواهد شد
🔴
ما نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم ترامپ درست می‌گوید که این درگیری چند ماه دیگر وارد مرحله‌ای کاملاً متفاوت خواهد شد.
🔴
من قطعاً درک می‌کنم که مردم آمریکا تا حدی بی‌تاب شده‌اند، اما اساساً آنچه اکنون در جریان است اینکه ایالات متحده در عملیات تهاجمی درگیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/147634" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147633">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: واشنگتن گفت‌وگوهایی با پکن در مورد ارتباطات مالی با تهران داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/147633" target="_blank">📅 23:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us5W_wIk-J9f9_HP2xNvU_-nDK-OgWOCDfz-SKIpTMFTrxh3oCso9oeJ7E8FC92n1SbaDQvUCoCd7fPdfWffkTlJK2edRZrT_AyzJsiL4KSDZUu5MfTLlN5Ob__y0lXsM8QzcwiC0RE9dy5okhp2ej755a7Kmw70Xu31JOe1btxkmFr89fpCptvKkLTxtrfd_zblA2i9KCL7rSqUuliH6tgvMIAKGuKiUoAtw5c3CW0fRedBLBrvYv9SdkOgRHbiBKRxkrT5i8VAHLPwFyICrVfWP2cyAxEFuy8ZZ_dWk8HVFydUTYGT4rJPrpxKtDnHbMKm6g859pwg79Xs7sYOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین تأکید کرد که اوکراین به بمباران پالایشگاه‌های روسی ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/147632" target="_blank">📅 23:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو و کاتس در بیانیه مشترک: ارتش لحظاتی پیش فرمانده تیپ رفح در جنبش حماس را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/147631" target="_blank">📅 23:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره خود علیه بنادر ایران، مسیر 103 فروند کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد، نسبت به گزارش روز یکشنبه، ۲ فروند کشتی بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/147630" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / حمله یمن به تاسیسات آرامکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/147629" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=dW4oZOsYO7xfvsdclPdf13bAlx9BkXeNFQpS6MWiRbAQUp5Ug6OO8xPXlQCKtl8qj9uA0w_tDJ2F9FmShYCFtnyZCPYXPQZEgk-qR3rAk8593NZADwgu1MjY99xFKGr-kfFI4BggxYtSo9_Dbcdu-Fd1j4Zv8yWko1d-SjXeWOvfGj7Z4fzpEIWKb_hR5OCaempyo9eXss2wDAbrczty1PE4xEJRmX7ixQgBgQTAL9Ff1J8t_NExpiAYkyUXz2-7RLpxnN4rSnXoYXr78KzMngUaNLdYW-l7ZQ3330ST34n7tAsIiqOwrAdij2KGIUBmpZ98lE9DWGIofCYGv6zQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=dW4oZOsYO7xfvsdclPdf13bAlx9BkXeNFQpS6MWiRbAQUp5Ug6OO8xPXlQCKtl8qj9uA0w_tDJ2F9FmShYCFtnyZCPYXPQZEgk-qR3rAk8593NZADwgu1MjY99xFKGr-kfFI4BggxYtSo9_Dbcdu-Fd1j4Zv8yWko1d-SjXeWOvfGj7Z4fzpEIWKb_hR5OCaempyo9eXss2wDAbrczty1PE4xEJRmX7ixQgBgQTAL9Ff1J8t_NExpiAYkyUXz2-7RLpxnN4rSnXoYXr78KzMngUaNLdYW-l7ZQ3330ST34n7tAsIiqOwrAdij2KGIUBmpZ98lE9DWGIofCYGv6zQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/147628" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رویترز: بارگیری نفت عربستان از بندر ینبع در دریای سرخ متوقف شده است
🔴
این امر باعث شد امروز قیمت هر بشکه نفت حدود سه دلار افزایش یابد.
🔴
ریاض به خریداران اروپایی اطلاع داده که تحویل نفت خام در پایان سپتامبر را لغو کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/147627" target="_blank">📅 23:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / گزارش ها از ترور یکی از اعضای ارشد دفتر رهبر حوثی های یمن خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/147626" target="_blank">📅 22:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147625">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f471b636.mp4?token=E46OHsuyLjv3CrJn2XqEK_v_B6XVMg7Tyvzsmc0Un1o76HZh0EyCiKh2TyTlFGGJ6nj32C8sWFA5Rw1u-oa2Isbcp8H12mcmbIJqx5h0a02ioxjoWgInzSPIsKb-BYGlttw8MYZ34YYB9mZRcNUaFmNInFucBZ7dEW2g3JK2oaNhIt1bRjP14b_ccgnzRdEp-n-KofeG797l9KxmMq65Ojyz-BBWL_VAhvuTdlyWqPtFPYWfGxcE6xxhwL5t56WreWQksABqBwTDJz0xM1p9KKjtlk000YqI2W2BPZlDbv-6Rx8GgsipxMcxI5IuAdD-mn0N6wusoyZIkGUU1Mx0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f471b636.mp4?token=E46OHsuyLjv3CrJn2XqEK_v_B6XVMg7Tyvzsmc0Un1o76HZh0EyCiKh2TyTlFGGJ6nj32C8sWFA5Rw1u-oa2Isbcp8H12mcmbIJqx5h0a02ioxjoWgInzSPIsKb-BYGlttw8MYZ34YYB9mZRcNUaFmNInFucBZ7dEW2g3JK2oaNhIt1bRjP14b_ccgnzRdEp-n-KofeG797l9KxmMq65Ojyz-BBWL_VAhvuTdlyWqPtFPYWfGxcE6xxhwL5t56WreWQksABqBwTDJz0xM1p9KKjtlk000YqI2W2BPZlDbv-6Rx8GgsipxMcxI5IuAdD-mn0N6wusoyZIkGUU1Mx0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو این خانوم فضول حسود که در مترو داره به بی حجاب ها تذکر میده در فضای مجازی وایرال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/147625" target="_blank">📅 22:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147624">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صداوسیما: خلبان نجات یافته ای که آمریکا باهاش مصاحبه کرد هوش مصنوعی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/147624" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
تخلیه فرودگاه ورشو به‌دلیل تهدید بمب‌گذاری
🔴
فرودگاه بین‌المللی ورشو، پایتخت لهستان پس از گزارش بمب‌گذاری تخلیه شد.
🔴
نیروهای امنیتی و پلیس لهستان در حال جست‌وجوی پایانه‌ها هستند و جست‌وجوها ادامه دارد.
🔴
هنوز مشخص نیست چه کسی این تهدید ادعایی بمب را گزارش کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/147623" target="_blank">📅 22:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
در اقدامی بی سابقه عربستان سعودی اعلام کرد به دنبال حملات حوثی‌ها و ادامه دار بودن جنگ با یمن، ارسال نفت به اروپا را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/147622" target="_blank">📅 22:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/147621" target="_blank">📅 22:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/147620" target="_blank">📅 22:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWfhmgzOwjM5z5GJJohF_4-op2T3hRrR6KZk3OJmPGTnS8wxsiC-kgFesKd0f6D1cyt-xtgJfApni8Ei0Oi9s2w3bgwP0h_qMTToVTnA5txvqppXAyC6E8LaoYbeYiBg4CkRxiVPlfZ7ApLr8YBpReBxs_qAAToEYynPkjd2ozh2b-uTNzEAHrGNh8jgQRC9XJgYDb6L0MJRERw15RETACgDT8c9cqRmnj-_TyZZWf4NybOpXnF8HZD2r4U33qEMmXZ4jb5UeXrijhSDJsP_4ZEZ4shAijYWvSzAe26vQ3HUrxC0l7MIscC9n6sCKOlrQEl1R8oOvHlAozuGuGikAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی پیش، ۱۲ فروند جنگنده F-16 خاک آمریکا را ترک کرده و احتمالا عازم خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/147619" target="_blank">📅 22:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147618">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/147618" target="_blank">📅 22:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147617">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
دفتر بودجه کنگره آمریکا: پنج ماه اول جنگ با ایران ۳۸ میلیارد دلار برای وزارت دفاع هزینه داشته است
🔴
هزینه این درگیری ماهانه بین ۲ تا ۳ میلیارد دلار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/147617" target="_blank">📅 22:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147616">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تعلیق پروازهای لوفت‌هانزا تا ۸ فروردین ۱۴۰۶ و ترکیش ایرلاینز تا ۱۰ اسفند ۱۴۰۵
🔴
آخرین وضعیت تعلیق پروازهای ایرلاین‌های خارجی به ایران، بر اساس اعلام این شرکت‌ها
🔴
با توجه به تحولات منطقه، احتمال بازنگری در این تاریخ‌ها و ازسرگیری زودتر پروازها وجود دارد؛ با این حال، هرگونه تغییر در برنامه پروازها منوط به اعلام رسمی شرکت‌های هواپیمایی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/147616" target="_blank">📅 22:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147615">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reApzHZMk-A1Aj0jOFhaLpII-WPfDwUbOTnr5FU-JQvoEJIn6a1qVK3_apqwbBD2upCR7p95zSH5fiI5AFk6D0Q6zWzHFjgFeJacXh-cdwG4OpBtPiKbJ4Gg1s-o1uQtcM2JDEvDbdW58XK7F85Aa02yk--DPuekmurYFzvLvtekphl7xk9Tdey72Whi2B6FWLH7HF_HMdkFtE1cLrl_GKROrQ9iiKeMTbtJhxhujAxZGnmH2NdX8TqddjdtQ_xG3Qbyl-D20RaDE91ERzUqLySn4uzox6fETWf_RYwlOlUbAYECriQpuVjoytdeBpwu_Nabh-HCu31AvFClYM7RTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : همه می‌دانند که اداره فدرال پلیس (FBI) تحت رهبری "جو بایدنِ متقلب" کاری را که باید انجام می‌داد، در مورد فرد دیوانه‌ای که به من در شهر باتلر، ایالت پنسیلوانیا، شلیک کرد، انجام نداد. تا زمانی که من در تاریخ ۲۰ ژانویه، به قدرت رسیدم، بیشتر اطلاعات مربوط به این حادثه، یا مفقود شده بودند، یا تغییر یافته بودند، یا تحریف شده بودند، یا به طور کامل از بین رفته بودند.
🔴
اطلاعات جدیدی به تازگی کشف شده است! چرا این اطلاعات قبلاً دیده نشدند؟ این تماماً یک توطئه از سوی دموکرات‌ها بود، برای اینکه مرا از انتخابات کنار بگذارند، که این توطئه شکست خورد.
🔴
"کریستوفر وری"، افسر پلیس فاسد، باید بهای عملکرد خود در این تلاش برای ترور و همچنین اظهاراتش را بپردازد. خداوند آمریکا را حفظ کند — آمریکا را دوباره شکوه بخشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/147615" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147614">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTpA7sCDuL9gNvudfrjWoWa71cwW3tAsiqMTAiK6CRTxfKejDh_6VZwOqui-ZU0BG8fpz9BDXVwGwh5v91mW2pCLdPw_GKvmj_8h30PHEMtky_hefTbo81f_4S5xbxajeW8edSxjSUxXeUO77AmyG4rw3LRzbzAXh-yn88VbbVtNLWgJ-mgaGD5KGZx72Tx1TPg5LB1syuhd23ixM1E_SzhMTcpiXtKPd5lzMIcMMftFX9nTSCrqhrRm8AZ2dlWXMtDIl6LV0poh06vklu1zx1Z0rSPXYPyNorQTNlIo-loYjKRnGE6AMZR5YIS7F4u9CEx_nXRI6GnYhWp9B0W-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تقوی نیا:
امروز تا آستانه جنگ رفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/147614" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147613">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/payK015RhPq6qInvQYyOI5hCRAfI-yoABhU8NM4Rx4vSl0uLRhGE5bwzbx65uBDpwqpn_bkIGkFu7v_JJCEWqbEjWL06SgPYh-aLZN430v-houDkN6U9CZMlhWS3R2Zz0WEAmaNMbaULKeRE0Ps-zDRvu3Lzs6sicCkH1E5HKYayyXdkfSjnqFheVh6sQkHKZSzufwmibAHI87effLOXGtsJ5LAG9CNZpkKBw0W_1oMRZ_Ewy2RgkZSUYn8PZBfPQNX2JDvIZzmBKZcUOybMcyXIFbz54gTp1mp2CiWsH8kp3IcZjIGtrt4FuxhtFtKtBg1QQc-lhDArYtyYi59rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا به اسرائیل چهل هزار بمب ۲۰۰۰ پوندی می‌دهد!
🔴
واشنگتن‌پست: دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از نوع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است.
🔴
این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود. این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/147613" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قیمت دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/+jkJGKa0y56liZGZk
https://t.me/+jkJGKa0y56liZGZk</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/147612" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQnEFdIQfYhnL45TOJAsZulfKsBr5BmiLJgtJ9g06i5AE8Wq0LICBAE-aoB9Ts72H6BAIe2btFcFCpqibxOdSOolejvpxQ4gDEwR_onjuJXmRAfX9pwk6UzFwpwfTngZNuz5PbS4ulgeTpSdaQ6jSXjSeke5_NnezCW-nVk_wfxfCVy990ALsqT8S9uspw8wMcg-54F78nIlgvFevM_zn9AZyt5VfnjKIV5V8MgP6IQpwxvYYLBdsoxzQ_5K_0cRq4EQkDUAUYJd7FkjysBbTr7YrJAerEsvSpTQB6kwflrFajjmd85VGi4KY3z5SPP-IGoTzMA7LOGIaVn1gsb5Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/147611" target="_blank">📅 21:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیروی هوایی ارتش: سه خلبان ایرانی عملیات العدید اسیر هستند و قطر باید پاسخگو باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/147610" target="_blank">📅 21:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری / گزارش سه انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/147609" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روزنامه کان اسرائیل: موساد و ارتش اسرائیل از طریق ارتش آمریکا، اطلاعات بسیار گسترده حساسی از حوثی های یمن را در اختیار عربستان سعودی قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/147608" target="_blank">📅 21:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل به شهر نباتیه الفوقا، در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/147607" target="_blank">📅 21:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147606">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده:
روبیو در تماس تلفنی با همتای عمانی خود، حملات اخیر ایران به کشتی‌های تجاری و کشورهای منطقه را محکوم کرد
🔴
روبیو، وزیر امور خارجه، در تماس تلفنی با همتای عمانی خود، از نقش مسقط در کاهش تنش‌ها در منطقه تقدیر کرد.
🔴
روبیو بر تعهد واشنگتن به تضمین عدم دستیابی ایران به سلاح هسته‌ای و آزادی دریانوردی در تنگه هرمز تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/147606" target="_blank">📅 21:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147605">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqPEy6q3K5rPm-gbfhCXu_JFmJKvG_Vr0aX2nFWMjR67Vrp37jXBbbkHvmLi05ibd1nWE63MyIN5LWwdEH4HiT_rWVVMzjHOqjD3yQGkaYDFiircXp60ELo-0JJYhdwh0msqI_34BSMz7PQNCtCJCalwGSIB7MurgdN0-5AuzRH0N_fBuPils06HgwakhQUZIu394xnXmlQ0c63wi_jxhjQwmbaLl727Pf2NLffhaXawIjyDfJbExll655rM5Qwx3FZKnOl6jDF0_znT3Y07MoDWb4und7dMf-Vl_pQn05H71-1BIaRxMKcWfZ5tmnYL65yMC2aHYHtL4Z6nt_8Khg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سفیر اسرائیل در امارات:
کویت ممکن است طی ۴ تا ۶ ماه آینده به توافق ابراهیم بپیوندد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/147605" target="_blank">📅 20:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147604">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1474c81cb6.mp4?token=dA2fzpR7z5NYkx9pWSVIpN1nCdX8rcRpN6guaphwbq3D98EopJ_985ae3ztJdf5seid8ifevZGI1ktUb1JEzg-B_aOJXo2owiZdAJoJ_QNLx5JLSp-Jru2gXCDDPPtOVcZs6adzqCdI1re2dLsh7p4e4vfQwPArigNIClGVvhf_oBHhhS3bLQse_r4TQZRHq83rfwRSqTK4cQ9UwjVccXwB30z7Dksclo90KfAkIlYNfnOUtYlgKTecONhrZBAG3qIsKMjznJp8L4XG5i6h1O1FWca8BCBrXfWP6dWAc1hBth15GO7wNU8vVkwxemYNnSWiJp7CiM6WgV7ZqM1ch2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1474c81cb6.mp4?token=dA2fzpR7z5NYkx9pWSVIpN1nCdX8rcRpN6guaphwbq3D98EopJ_985ae3ztJdf5seid8ifevZGI1ktUb1JEzg-B_aOJXo2owiZdAJoJ_QNLx5JLSp-Jru2gXCDDPPtOVcZs6adzqCdI1re2dLsh7p4e4vfQwPArigNIClGVvhf_oBHhhS3bLQse_r4TQZRHq83rfwRSqTK4cQ9UwjVccXwB30z7Dksclo90KfAkIlYNfnOUtYlgKTecONhrZBAG3qIsKMjznJp8L4XG5i6h1O1FWca8BCBrXfWP6dWAc1hBth15GO7wNU8vVkwxemYNnSWiJp7CiM6WgV7ZqM1ch2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات و فناوری اطلاعات:
فیلترینگ و نظام محدودسازی به کیفیت اینترنت آسیب می‌زند/ فناوری رویکرد منفعلانه را رد می‌کند، باید از ظرفیت آن استفاده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/147604" target="_blank">📅 20:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147603">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H99A8qGgUz7Floi3Gak_befk-rbkxADxXDHpgMZD4I_t0Cp_aALnFz3vaLQbZyJWA_DLcycMf5veACE57vWkTONv6vSnYdN9llj8aL5ObFeBIPHAgiwe16iDjDHCnVvqT5zUliYvYqWL1TC9_n5c_7LlHCP1Ep8c5fZhK7tY-GLmwn81LbSR1e9E-RMVISrvest1F4Znl4Reo6bRkT4dADtRPqZijPTd5SaYv9OqRSyfVyjzoWsZFYH2gH0n4T_Fs4_GQhK1d_cGikM5d7F52q_mV2g2ktFGKqsJAZI4yNigvhtWyFOfSYhwY-A6uWKWLsOU-UTaW6KX6Kyai1Wj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ارتش آمریکا اسکورت نفتکش‌ها در طول روز را آغاز کرده است
🔴
پیش از این روال این بود که نفتکش‌ها شبانه از تنگه هرمز عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/147603" target="_blank">📅 20:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147602">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=vHrWLDhb5maWhiMQdeQCONvt0vUC8uhCFCjwdyu0HkFkeivWngIYG5kmjBRShibLG2VRuWS-f27dKNBy7oP_XlJIGFsr5nQN0sKu3upttXExZrJP1HdQCy32aQjbv1mZIFGMmyFaaNMVQUzioGsdJXa38PMVm-OxcmZQlrNnJBTxmslp6Pvn1bVv5B3ah5g4W4pyKtyWlzknvz_kzzRyoaghe4rWar7eEu71B8l60IhgvAkoKOg7NUwoZ6_HjCwkvBBKDJBaRKhi09ZIVd6Gm-y4k-IfP7g4kIFyNFuAYQOq34o7Hx5hzpN4F0M5wKo9uZ21keTKodTO3b7KCj65YIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=vHrWLDhb5maWhiMQdeQCONvt0vUC8uhCFCjwdyu0HkFkeivWngIYG5kmjBRShibLG2VRuWS-f27dKNBy7oP_XlJIGFsr5nQN0sKu3upttXExZrJP1HdQCy32aQjbv1mZIFGMmyFaaNMVQUzioGsdJXa38PMVm-OxcmZQlrNnJBTxmslp6Pvn1bVv5B3ah5g4W4pyKtyWlzknvz_kzzRyoaghe4rWar7eEu71B8l60IhgvAkoKOg7NUwoZ6_HjCwkvBBKDJBaRKhi09ZIVd6Gm-y4k-IfP7g4kIFyNFuAYQOq34o7Hx5hzpN4F0M5wKo9uZ21keTKodTO3b7KCj65YIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از سوپرنفتکش الگایا که در اثر برخورد با مین‌های ایرانی منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/147602" target="_blank">📅 20:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeNobeZqvnD_RutYKTx8MSSkGg8gX6KcuHDNmeocQFUKOE_PlcTho1zMRtEMTfTRJO80G7Lv0iTjsREMfH2A6N8SnhCmZuEbDKoH43Gw8C_6cKEB00h1lhP9Vx1dA8foAHN4qta3SEVYUndijvr_YutLmJqIZauTfDqnTNZl2m1FPI2fbfuQfEP-BC1PWx2t1XM--TNyAPHTcE2Wmssl41kOnS1vNleARnJk0ODjMkLvJNbUJFo4X2WGbYS5HepAjGv3_vjIUBdGMRv02kf0pJdQZXOcDAvaPb4FUgPQm5gNzhFY1Nya96toqxrUypcUtHM8GJR5PoC3EyoJ6s0nGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : در زمان مناسب میزان واقعی تلفات نیروهای آمریکایی را افشا می‌کنیم
🔴
ادعا: ایران بی‌دفاع است
🔴
واقعیت: صدها پایگاه و تأسیسات نظامی آمریکا در هم کوبیده شده و ده‌ها فروند هواپیمای آمریکایی به آتش کشیده شده‌اند. (منبع: پنتاگون)
🔴
این فقط مشتی از خروار است!
🔴
در زمان مناسب میزان واقعی تلفات نیروهای آمریکایی را افشا خواهیم کرد.
🔴
و روسیاهی برای آنها که به دروغ ادعا می کنند ایران بی‌دفاع است خواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/147601" target="_blank">📅 20:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آمیت سیگال خبرنگار کانال ۱۲ اسرائیل: تماس‌ها و رایزنی‌هایی میان اسرائیل و عربستان سعودی، از طریق فرماندهی مرکزی ایالات متحده (سنتکام)، در جریان است و هدف از آن، ارائه کمک‌های اطلاعاتی به عربستان برای مقابله با حوثی‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147600" target="_blank">📅 20:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXeKYk-pzO8e2FfkE0Mcv5ex0cyA_MGKaFEe-jK5_4dQggWOwuhwZwD4l2R7U6wK-pSaQvNctaz30f5ZzmVviTg9YjCoAMrXBzMXLr0dDosJTVY1GZxtzk5stM-lCQmjJONR8bA8qY13O9S-roGKAZtHrfXb4GFcmE5zkIwh4vzDEAZ-RRQ7xS43ota21AcbSUBKUjVjx54N9JsqdvcwLuC_TquGb7XFGnqr9SFJlhKy1W9d1o4rbYYuAJUQxH6HRxdCPXgF5UJB81DyDYXQHfO3mzJfkXxBWw5XjU3JAPvIE2jFh22dFg7XW4sROHq6yiwPa1bb_Q1saXNQDB-GAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: فرماندهان نظامی آمریکا، اسرائیل و کشورهای عربی در حال برگزاری نشستی محرمانه در رابطه با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/147599" target="_blank">📅 20:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147598">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658a596829.mp4?token=BUs5zHVH6aTuRwx4Fmf9-dZlIJ_6vQIeSUQo7lq-v_UqdX8EuQLk2hoHPwFOAKSiPEDkPoV5wVXJbnHsVZqm2ss-LmHIK_gkjm9yp8qq6XVlqJ0Se_jZLFSOjXj73Xz4ylwaYSytFSd5yCiLFwvVcykluudI9Ie_IOTMuLvb-diJhWW5S9bKV70hEPaPDVe7d3W8ojk7L4uSJidCqxhL1x0PISelSKw5pFnekjqlZfBIQGhza9OgYjGtwhRCDWUFRwbDB3Iv0jQYBd756HOZ00F__AAlzQQOX64Q1k4PeuZ6nzYsae-ecdUkc3yB9ZRWsLGONoJirAMh_ZeurLJipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658a596829.mp4?token=BUs5zHVH6aTuRwx4Fmf9-dZlIJ_6vQIeSUQo7lq-v_UqdX8EuQLk2hoHPwFOAKSiPEDkPoV5wVXJbnHsVZqm2ss-LmHIK_gkjm9yp8qq6XVlqJ0Se_jZLFSOjXj73Xz4ylwaYSytFSd5yCiLFwvVcykluudI9Ie_IOTMuLvb-diJhWW5S9bKV70hEPaPDVe7d3W8ojk7L4uSJidCqxhL1x0PISelSKw5pFnekjqlZfBIQGhza9OgYjGtwhRCDWUFRwbDB3Iv0jQYBd756HOZ00F__AAlzQQOX64Q1k4PeuZ6nzYsae-ecdUkc3yB9ZRWsLGONoJirAMh_ZeurLJipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند درباره لاله مرزبان، بازیگر برنده جایزه جشنواره ونیز: بازیگری شیطانی است؛ خاک بر سر مسئول بی‌غیرتی که به او مجوز بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/147598" target="_blank">📅 20:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147597">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
قیمت نفت: ۱۰۸.۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/147597" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147596">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: «اظهارات صریح و بسیار رو به جلویی» از سوی امارات درباره قطع منابع مالی ایران مشاهده کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/147596" target="_blank">📅 19:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147595">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d6f89f5b.mp4?token=UdYyOKxyGdqViUJ-VPifFPfGq54KvpeWy4Bz8e1M-pyZVvanavpfmLWgxJUE17stA6X4ZmIzLgi-J9dDc6tdFL_bk-cb5M4eu5_9NsfusHzpT_9HvNyFOzxYmRRUjP3OxFW-FYqe95tbjaKNZxYXQXWMIRV7iLZ4C7YT_Yxd0IHkprfpu7NkYirW73zf5EBVqX2Xi1q06dCc9YwA6PJ0oXqQjfASWZY-cJ7mqg9WwUHfHJ5sLDRlqaEKFWSzvZ1xUO1u3U9XFNuMovS6urTX8fu8vOzsAQVQ9T56MwX6qd7uVYhveoPuT7rAsutzYCpQBQ5Zka9U7fNQ6_lBXldh1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d6f89f5b.mp4?token=UdYyOKxyGdqViUJ-VPifFPfGq54KvpeWy4Bz8e1M-pyZVvanavpfmLWgxJUE17stA6X4ZmIzLgi-J9dDc6tdFL_bk-cb5M4eu5_9NsfusHzpT_9HvNyFOzxYmRRUjP3OxFW-FYqe95tbjaKNZxYXQXWMIRV7iLZ4C7YT_Yxd0IHkprfpu7NkYirW73zf5EBVqX2Xi1q06dCc9YwA6PJ0oXqQjfASWZY-cJ7mqg9WwUHfHJ5sLDRlqaEKFWSzvZ1xUO1u3U9XFNuMovS6urTX8fu8vOzsAQVQ9T56MwX6qd7uVYhveoPuT7rAsutzYCpQBQ5Zka9U7fNQ6_lBXldh1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به نظر میاد تجمعات شبانه بیشتر جای مسخره بازی و لودگی شده.
🔴
پای آیفون 18 هم به شعارها باز کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/147595" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147594">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG0v-nezNLsXDIZ50DmPTAOzRiXxR1WqIGRLPfXkbzaY4rFKMygn3JkH6x8a4t7bXEdzkHeCIKs-5M_zIrDPjJScBZG8YESEUT7xlqz4GHWmKkXse34hBjHPF4ydXhks-5cJ0yr3hxSFTF_NBQhHoEl5m6VTw9Z_BTcTbLbVPdcDG7YjH2p5zHrXXqPUUy_ybBvM1f_XeggUssrHUXUfUabTtnHLC3V7Hb52cfzpq3OKGG98Vupt5rKO2VY-wYOFJgte7lOgSymJkUzEbeyn119c1-_dqyYmHL9LYgO96f_x8flJC24ZtwgA_A2m3pIn7hVlFG916DUcGoOJT_Y49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
مرکز کندی در وضعیت فروپاشی تقریبی قرار دارد و این وضعیت سال‌هاست ادامه دارد. تکه‌ای بزرگ از بتن و فولاد با صدای مهیبی از سقف یکی از راهروهای اصلی و پرتردد سقوط کرد.
🔴
اگر ساختمان باز بود، افراد بی‌گناه کشته می‌شدند. یک نگهبان امنیتی دقیقاً یک دقیقه قبل از این فروپاشی سقف از آن منطقه عبور کرده بود. بنابراین، او ۶۰ ثانیه با مرگ قطعی فاصله داشت.
🔴
قاضی مجبورمان کرده است که آن را باز نگه داریم، حتی اگر هیچ اجرای هنری وجود نداشته باشد و هیچ‌کس شجاعت ورود به آنجا را نداشته باشد.
🔴
هیئت مدیره مرکز کندی به‌شدت رأی به نجات آن داده‌اند و می‌دانند که من تنها کسی هستم که می‌توانم این کار را انجام دهم، زیرا من توانایی جمع‌آوری پول و توانایی ساخت‌وساز را دارم؛ توانایی‌هایی که افراد کمی دارند.
🔴
من همچنین قدرت و اقتدار ریاست‌جمهوری را دارم که برای انجام کارهای ضروری و دادن شانس قوی به بازگشت به عظمت مورد نیاز خواهد بود!
🔴
به یاد داشته باشید، مرکز کندی زمانی که من مسئولیت آن را بر عهده گرفتم، صدها میلیون دلار ضرر می‌کرد. آن‌ها به‌شدت در حال شکست بودند! این موضوع هیچ ربطی به من نداشت، من فقط آنجا هستم تا کمک کنم.
🔴
من فقط آنجا رفتم تا حقایق را آشکار کنم، به‌ویژه آن‌هایی که مربوط به ایمنی ساختمان هستند. یک قاضی بسیار خصمانه و متعارض (چه خبر جدیدی است؟) به نظر می‌رسد اجازه نمی‌دهد این اتفاق بیفتد و در این صورت، متأسفانه، سرنوشت ساختمان به سوی نابودی است.
🔴
آیا این خیلی بد نیست؟ ما بیش از ۶ ماه را در دادگاه «با بازی‌های بی‌فایده» هدر داده‌ایم. زمان دشمن ماست!
🔴
هیئت مدیره، که متشکل از برخی از برجسته‌ترین و محترم‌ترین افراد کشور ماست، امروز دوباره جلسه برگزار می‌کند. جالب خواهد بود ببینیم چه اتفاقی می‌افتد!
🔴
از توجه شما به این موضوع سپاسگزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147594" target="_blank">📅 19:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147593">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/147593" target="_blank">📅 19:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147592">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ZoefmAYFen650bfnPRGXBOPrCIpbPzS9jO-inXbzaSS1jYkTpSz0BsQWuYlJYUbPA30XT1T2O-cMxk-fqnmhS9FvqLrByYjEsCwFajV77FR4rv6ajobCc_7NErcenRpjD4HFoh8--qXyogHkpysITGCfxy3Zk2QO4OkYg8zJciEx18IRzueTZ92ZROL_4vBWF4ONfLrMdatQ0Mz9N6ATorv_X9zhcwWupG2j4jXSD7T2Mx1_DS-fTR0zrc8npT8UkcDCMRGPAO4L7bnhozEV0jGXcBsSoL6hk9uAhtr-yUmPgYjz0Hd8hTELHJu6DFIodo8I48HPPov0BCy_oZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همه پروازهای خروجی فرودگاه جده متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147592" target="_blank">📅 19:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147591">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789860f816.mp4?token=ZA6vZ74EhJG5_gBL_G5_UnxMpYVC8s_a5ro_7Xm9gEJ5XKqn9pjyK110PC_BAwjptOT2DzrhJmLic5qTWlEQPfy7TdLtDYtA0GHrL3XgTLABkXFhpMcwhc_5ZmT3HA5G8VVAirbbsWDyTmDyYd0NNGsr0uaaGrwKcJ9EENNuEYp1R0EOlsBz-BPeJj_f_qWMaFXCi-mGk4wzavh4xT5YpcqGWhdkrUvB-Pa8PfhpRdtwqQmhSuBwCJyBCKC1UC3C_E2luNOJ97HOLFBABscoPxPyfHfwQsMU84fdLLI3w8PV2eV_7q03o50-HoVh5OHlxPunrQOpNltOmVlJZB2VlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789860f816.mp4?token=ZA6vZ74EhJG5_gBL_G5_UnxMpYVC8s_a5ro_7Xm9gEJ5XKqn9pjyK110PC_BAwjptOT2DzrhJmLic5qTWlEQPfy7TdLtDYtA0GHrL3XgTLABkXFhpMcwhc_5ZmT3HA5G8VVAirbbsWDyTmDyYd0NNGsr0uaaGrwKcJ9EENNuEYp1R0EOlsBz-BPeJj_f_qWMaFXCi-mGk4wzavh4xT5YpcqGWhdkrUvB-Pa8PfhpRdtwqQmhSuBwCJyBCKC1UC3C_E2luNOJ97HOLFBABscoPxPyfHfwQsMU84fdLLI3w8PV2eV_7q03o50-HoVh5OHlxPunrQOpNltOmVlJZB2VlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قائم‌پناه معاون پزشکیان:
حساب کردم اگر بنزین ۸۰هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷میلیون یارانه به هر نفر داد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/147591" target="_blank">📅 19:18 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
