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
<img src="https://cdn4.telesco.pe/file/EDjlUR64-7dtKS-Oqj-V1mDVdO_ARXiQr5tJC7WCZfydz_qiYjUmtrfaN6bhScpqZ2D6Zswanz6PZFQ1eGHMXXVnRQXf2Zh0mKDt89u192-qE0o7MYI3UtZA1DDY9OhsOJ_K62ps8A06TLqZrnuE0yegN8gmvR5DQmA06R71K4Sg3Iog_8RZAhkH_K0XkGU826I_st6A6TpRfqcE3aQYnVk88bCY7c5Vr3u4kYb7B2VAdcyRBzMdi4k-yVXZuS3vvIHXbsB5kUKK526cb149NZpsaiiH1A5lVIvMjYiH_vD2aztnb11IL8fXifJnbbKVPuyuhpm58PtskigT-UjP1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIvGMYboqqLnINxSIx5V9pru-Pza1bsZxKrCdQopuQBqRBSB8y9faLc9bIkT7pGlxMhXBx9kfGboJNEVAICU9olfP9JMvBGVMAsSvz5WOk59NQoVHrWA0EMrn-JCsREoIhsHJwkNpwcmXCPPPOJfVTPDO6fnSCpMe4WC9kS0aWeCaCgZXOT0o5Y-APFzQpOd4UWc4yPQjvhuaQE-bl3MWKhqCMe1y4iirwYI5eWhBOYzO44Q0S-66xFMU0Z66sBAqCgCBQH04UWUeyotoFEGSjxQv8fM6_-jv69RFX19sXhcB6sedgOtkdd_XNcglR_xAHxYEo1lwScXcT600wCkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین خارکسه اس، ولی به تو هم نمیرسه کصشر بگی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/funhiphop/76668" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/76667" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱,۸۰۰ تومان
🚀
@suii_vpn
@suii_vpn</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/76666" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyg9iDx8d7YGb_Jb1xReG3kY4lYYUkwAbMZN2jec4MrVca4chqCc4a58gTZDDympnKE3pEMorG4dJbfV3N85nDS18zvsQMtKb041cXcaOzRGpsfn-GoyU8rfGVsvcfzGHUfRWYyAxIbtH-6E2BgM85gPONOhVKhRQyEMEaucL7WObcW9AxcoNPBlJhavQH6yjB9oiJesxLFoRItGNgJqliR8cO9vtBGt0y3DlobqkHGkLxGQ0bfZHa59xG3bTBXa1gGyhRTQbrtnWAcgmHo6_kEdsWz401B3ZQX8EsYU8zJDcZujRZWp9iJBPvNyHzzuBkx-FdOPuXDDwafM0UQggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ح   ز   :
این چیزایی که فارس و تسنیم می‌گن مذاکرات متوقف شده دورغه بابا.
این حرفا نیست که اصلا.
ما الان یه مذاکرات خیلی خفن با ایران داریم که خب البته نمی‌دونیم آخرش چی میشه ببینیم چی پیش میاد ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/76665" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روبیو: شاید ظرف چندروز آینده خبری از توافق با ایران بشنویم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/76664" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهوی جنایتکار در مراسم انتصاب رئیس جدید موساد:
رژیم ایران در نهایت از صفحه‌ی هستی پاک خواهد شد و و ما کمک خواهیم کرد تا این روند سرعت بگیرد.
در آن نقطه، این رژیم هرگز باز نخواهد گشت تا وجود ما را تهدید کند.
این دستور من است – و این مأموریت شماست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/76661" target="_blank">📅 18:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز در گزارشی افشا کرد، ارتش تروریست آمریکا برای هدایت پهپادها و کشتار مردم ایران، از شبکه استارلینک استفاده کرده‌است/ رسانه‌های خارجی مدت‌ها استارلینک را ابزاری برای دسترسی به اینترنت آزاد معرفی میکردند/ چند هزار دستگاه استارلینک توسط عوامل اسرائیل به ایران قاچاق شده بود که عمده‌ی‌ آن توسط دستگاه‌های امنیتی توقیف شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/76660" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuK2DpBQiaM1lJRM25ZD12J0QZ0zE2hDnu1W-44N78gHNyIT3peS3Zi-2NNcZktfDlApJZYfeQrjEXbmxRB_SdxS-t6f3l2jVVIkrIgNpKZPj3DC_d4h2RYXQjRgMVr6s_7TmIH--MXIgkTdNi2DWnpaZzhHh6FeoZyhVK6cTjLu3WbIhtZW7dSTeaMHHGNW37wG7OwRNDE-Td8ysKSx8cgBZ0HiZZ9BIP42WMyOx8kffvYVfpXH2fBOQU3r5C2xytQJ5FRyiYKTnVHEMsnmHal5OhF7YrUV1ODXQ85eU-Mp2L3fjDrBpqtDVwSCXd5eHvPaNdWO7kSIU-PKChDd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیشد
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/76659" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofwSAwO-MnDGPT5yrHjx1ia5dKbPHQO0wuoEmU4qLXzHfl34VLmikWardte7XiF9UOAsHv9kjIejbLQAA37ZsW36u9XJo4K76YXhWO5yyCuI0H2592VlnxJ1oKRweUUF5Yjv1JMOm73uE03g-6ErKefsDVEioPlPB2FWjq5KaImACilCuTjMycr5lSvP4DNXvOnRDpV1ZnKv3k1U1GwEwGtIxjQ03W9cg6yGmXfAh7S4msKDww6wZ_POllauRgLxuq5nzHATIUZeKTuHV5QNU51BT7PSl3NqYkZJHYueD9VpKQoj-DobEHD4gCYpcDEHwu-RShJ1qkYUrEBTxMXccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g12
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76658" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رومانو:
کوناته به رئال مادرید
هیر وی گو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/76657" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دور چهارم مذاکرات اسرائیل و لبنان توی واشنگتن در حال برگزاری هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/76656" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">معاون شهردار تهران:
برای تشییع جنازه سید علی خامنه ای ۳ روز مراسم بدرقه در قم، مشهد و تهران برگزار خواهد شد
آمادگی حضور ۱۵ تا ۲۰ میلیون نفر را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/76655" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">میگم اعتراضات امروز دانش آموزا به کجا رسید؟
انگار تاریخ امتحانات رو یه هفته انداختن جلوتر که
😂
😂
😂
😂
😂
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76654" target="_blank">📅 16:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حصین به نصف رپفارس رید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76653" target="_blank">📅 16:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76652" target="_blank">📅 16:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76651" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چقد داشت تلاش میکرد وقتی میگه کون لباش غنچه نشه</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76650" target="_blank">📅 16:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4W3vZJJqC087EreGHazOABkAiNUnmLoJu037Jijx-gU4R4PsyxuYy0xML9lh7VH50Ct8sf68iBZmDgvYYKLH1fPZmnSxV_ziS1SgrXN3JZmngH7UmmMiMLHgYoMORjiS9HEC_fKhN9snp3Ibd6zQLPv2LPYN_eEx3FtOJ5L2pWxNzC69JUelD9hYsM5_NqVdpfUHS2W35IAGPZQS0CvcAV7Wuxg1xXvJRPBcSgcYSAYW_SH4veYcvYqLUPbd_YreLLfOySxJltMQAky63jwmYFTly6rlR8jAWtAwCRqfWalOUmA4af9GlLlXBgJ2DEOutIAIkZrU4WHePHWuH95sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ی مشت کونید همتون</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76648" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76647">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حصین یجور میگه ویسایی که ازم پخش شده کار Ai عه انگار من موزیک دادم گفتم "گنگ مثل رهبری، مثل حماس پی حماسه و..." دهن سرویس محتوای ویسارو تو موزیکاتم میگفتی دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76647" target="_blank">📅 15:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کصکش دیسای پنج سالو جمع کرد تو یه ویدیو ۲ دقیقه ای جواب داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76646" target="_blank">📅 15:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حصین بنده خدا انقد فضای رپ کیرشه هنوز نمیدونه دکی مهاجرت کرده فک میکنه ساریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76645" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76644">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آنشرلی با موهای قرمز
😂
😂</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76644" target="_blank">📅 15:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76642">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76642" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76640">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به حصین دیس بک بده</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76640" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76639">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پوری پاشو پسر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76639" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گنگ مارو تروقران، به چاقو میگه نایف</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76638" target="_blank">📅 15:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حصین به نصف رپفارس رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76637" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FblDyhL-7IP6pG2R_EqQSHyW5eps8VJ9t1g935KRwdcu-jJhYSaXNrfna70O9EvIK93XBpt0RlnTelZUkRWrCj0aEUVatFBA889xHkIgXPgWGea6fMmKBS3cHgeX6GfRtEqhtp5dZXcir74kDo6Ah45pm71XRkhn2UzutvmzHsQHfKT12tav3QxhLdo9wht093qjUMGCckhzdM3PIGsgvrqykY7RSI1VGnQ6VYLTZQIZMAdQQMBYsUm58kXZ0jw3Cdh74PZnlSQBduOzbqcQKp7y04P-s1zVTq4qEFHQTO61ESuqkzzpNHqVGMZG5HwMiyzwFltfUymBB-to6p_HaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط ابر بنده خدا چرا اوبش زد بالا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76634" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده، فروش سرور های نامحدود اختصاصی باز شد  یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰  برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76633" target="_blank">📅 14:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده،
فروش سرور های نامحدود اختصاصی باز شد
یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰
برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps
🔤
@Behdad_sps</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76632" target="_blank">📅 14:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینترنت بین الملل باز نشده
درواقع فقط فیلترشکن های رایگان وصل شدن
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76631" target="_blank">📅 14:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سفارت اسپانیا هم مثل سفارت فرانسه و آلمان تو ایران باز شدن و شروع و از سرگیری فعالیتشون رو اعلام کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76629" target="_blank">📅 14:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuGEl1sfn--xmES65UySJDaFNxeL9P3PMGad3IveqkdBqzUM2-priovZ2BM4dTVwsDu4j34tw0gCgAQ5LXo4mtn2GnintPpcq7VZ_gk9Rt2JWZVT9D4gp3REEQkdg1QT2hjY_hg9JdcC9Q4FVAn91HoVLb3NRCJrn_k2K241B3jV6U4oC3XisvFvbnTNbC5BLRtJYnKramUF6VriEeqVG1FO6lpwgmMqAlpjpC9EWeBzKoIVVs5RNcbE89OwGCbUhQeTQTZuB1uasCFpNs8GHW2Ryiqr6HcHkLoXZUXEaKzw93vlY5JFx2-tKFpYtl8w-u8ADS6K8sGngEo523r3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76628" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">۰۲۱کید من هی میخوام مسخرت نکنم، بعد تو رفتی کیت آرسنال پوشیدی با پرچم ایران داری آهنگ انگلیسی میخونی برای فیفا که پرچم شیر و خورشید رو تو استدیوم های آمریکا بن کرده، حله.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76627" target="_blank">📅 14:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تنگه کص نمکی رو باز کنید تا کیر اتمی نزدم بهتون</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76626" target="_blank">📅 13:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76625">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کارت فان هیپ هاپ هنوز استفاده نشده و زیر آستین ژنرال ها و پاسدار های ارتش دو کشور قایم شده، برای همین تو گزینه ها نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76625" target="_blank">📅 13:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76624">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوبار نوشتم در نهایت، ببخشید سواد ندارم شما یه بارشو بخونید</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76624" target="_blank">📅 13:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76623">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-poll">
<h4>📊 به نظرتون در نهایت کیا باعث میشن در نهایت خار این آتش‌بس و توافق گاییده شه؟</h4>
<ul>
<li>✓ تندرو های داخلی</li>
<li>✓ نتانیاهو و ارتش اسرائیل</li>
<li>✓ جمهوری خواه های تندروی آمریکا</li>
<li>✓ هیچکی نمیتونه کیر ترامپو باقرو بخوره و در نهایت آمریکا با ایران توافق میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76623" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فایننشال تایم: رافائل گروسی اعلام کرد قزاقستان آماده است تا ذخایر اورانیوم 60% ایران را در صورت دستیابی به توافق ایران آمریکا، تو خاک خودش نگه داره.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76621" target="_blank">📅 13:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBsOiX-sUA3RZRb26VgC2Ocu0B7GIdh7WWetUBqkuKx4kvaKQeu3tWqaPBBNSnzTcKqe5pgW_Av27HsIAKClBcbYGACXZOlE8VMd_kIkhH92_eRufTO_Gsjhr7Ue-NImnV1WchMeYDTrfROfZ_YIaI30WjP_EY3gWT3e4JA66IJ9_7kvkaads7LcfTxPZDdc4P1mIaxsI8FYPoTLp1I4W0jEnONp3IxiB1uLuT_GbkOk_izGZPpHv3JnTwbQ_bEUTodJleucylLJaxVx_xj21HdQLfYNpTPdHSWieNavYr9Tb6ewnxUye45a5YWaq2QfYMNngXUQfTmeDLnS6EwGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دستور تخلیه کل نبطیه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76620" target="_blank">📅 13:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76619" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍓🦢</strong></div>
<div class="tg-text">میشه اینقدر با مزه بازی در نیاری این بچه یه سال تو اتاق درس خونده رفته برا حقش دختر بازیو جا دیگه هم می تونه با اینکه کنکوری نیستم قشنگ نبود حرفتون</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76618" target="_blank">📅 12:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76617" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=YdUCW_rMEXuTUyeb2f7UAsGoabpPh6DKOk7y6HaddH_g9I1cIRdDLuUJi0D9TgPoL8Oy9syM8l_65rLZ2zfcS8yldRfM_3uer6KS9WmlZWIqjP2nSWgzcsEFu-YLUMNUg8OeaKUz1tLvqZKP1u6dl4-yQW-o04dHxJRxcqqO0N9DnPESNwgbXYgas5XpY5TTKJ7RIQVCiMAYZRdILwuqgpq9rt_rnLil9maAhje7P7O-9KDoJWZpIRMMsD7-2m4J5BLZLEX8ReTKFTYIof3zA_8nuqxG6G6gruxc4BWqW38Ud1SDiDrr5IQ40YmvA_UhzKUPFJ_mSz66BL-dD8T3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=YdUCW_rMEXuTUyeb2f7UAsGoabpPh6DKOk7y6HaddH_g9I1cIRdDLuUJi0D9TgPoL8Oy9syM8l_65rLZ2zfcS8yldRfM_3uer6KS9WmlZWIqjP2nSWgzcsEFu-YLUMNUg8OeaKUz1tLvqZKP1u6dl4-yQW-o04dHxJRxcqqO0N9DnPESNwgbXYgas5XpY5TTKJ7RIQVCiMAYZRdILwuqgpq9rt_rnLil9maAhje7P7O-9KDoJWZpIRMMsD7-2m4J5BLZLEX8ReTKFTYIof3zA_8nuqxG6G6gruxc4BWqW38Ud1SDiDrr5IQ40YmvA_UhzKUPFJ_mSz66BL-dD8T3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76616" target="_blank">📅 12:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76615" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYoung Roque</strong></div>
<div class="tg-text">حاجی توافق شد؟؟؟
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76614" target="_blank">📅 12:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evBBdw3dQeaV-mnUsSxLKEr8B_5kX51eL6PFkKz8Mb9Ocvu52oDrJ9_8vSMOSuHolDnwpQte0ryYy1wI4WPIK7__r6aq-QVyT6oprHumMbyTUr82iWOwI10x1WtpUsIndjg37PzVLeA5bDtjjd-Gdrs3zYQkYPkoMRcCdhMf5G3ynyF1EXOisbttDvb3VhXqGfms_iMGDLeC22LC2_BLhapEf3LhD29cod188_xczbWa6W7v6KqejBDiHkZXjx64cSE4ZwWXqNzM7owz8YAtJR-7aa67h2BnDWTlXLkCnM00EwxB5rLR4aQLUALIVLFuhFRej9M4Bg4LPimoHJAZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ به نتانیاهو گفته تو یه دیوونه روانی خل و چل هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان همین الان حملات به بیروت رو متوقف کن  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76613" target="_blank">📅 12:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دانش آموزان الان در مقابل وزارت آموزش و پرورش مشغول اعتراض هستند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76612" target="_blank">📅 12:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آکسیوس:
ترامپ به نتانیاهو گفته تو یه
دیوونه روانی خل و چل
هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان
همین الان حملات به بیروت رو متوقف کن
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76611" target="_blank">📅 11:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0PDFUetTlsk-dmaD706pFCeBvBurW9rdNPrylyzFD1CUVbtCIBq_1cZtsa8_Nw1n00aGJ71hIABdd0ba75WS33V0NO9sItiFHP7TmoXqIRxL7mJnHQbEHgCJpj3YQjkXKzpDAPTxMH95mrictnJtkhZCrzE2UDz2tgZvxgok71Gck7lmLNecfB_jN480RH22ALQsmYu6-D4PyurvUp86gwUpZxdpzycluGPJBHr9hdxN7esGp1EFhWFodMHNv-gktGZq0h7Svzz5dRMILiHy6XANICGb6NhIr4ZTCkPj1XNaZrv9V3E5VFBVm_XUxtGnfZr_-K2V16zw8sFuV9fsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه مادرجنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76610" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e85LIMDq5qVa5v2_rDUX4XKhVeMRRHp-J3Sd0IJxJli1H6O5nScBdN3Ff7o7w2hgKoJhyAPUkV7vVNsTcPF8jAnj2Wh54LAW5UDo2QJhYsfXugJsKw9ndUq3ZVVbnwzD_nmgtLmrlp-inhRprxCvaKXgEyYHC3q5xTPAZdOMIBC8dehv-mcub4J_1PGv2CQE9S3zxeqrNIoEdg8ocMBntXYcrLM39aUjMuVb3Ro7lVtcKzNozkilxWJ_ivaQWzegLqo818vdHcri3lJkFKdAkrD4OKcRxWk9dtjdKPpqzFxpyb5db3l7XygoJNt22lBjJQQWhoDFugNvPMkwWUYV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون شبی که تل آویو اینجوری روشن بشه روز عید ماست !!
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76609" target="_blank">📅 10:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5CpX_pLq4-ftJpi1PIP4NZdl4_VbuDnu2SXg9bpE76pX3_BXuWQvAbCvw5XBTX5lgP8h1bTTCHLiHxk8DYgWOBGjieCxAcQqU2pLoD74RTK9sazQmGo56qdiertWZk4Iq32FH3E6JbvT5XI_LYfUKchvTYqa1F3bkTTr00rxJome3w4aX6NGE9YwqjJadSz15Z4TtEwFyVZROjXDZjbI6Njj44JaKX-hdExKQXMhtW1HuKevB2f6MHOGc1_aujK4_p9MS-_9iZWyz1Bdi2NJx6LfCAJ4TX7axJHSfwGiTvwK1JnEU4s_TebJ3iKEMmxURGSh0841D2_jFmlpixeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت رو بخونید و به پروفایلش دقت نکنید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76608" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/76607" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCqvkIcWw9VcqOkcg-cr_HuLdiecrYPXMPvPBR7pXbey1370CYh0xblBh7qIpW40-i3qtoNhX0IL6kSANPFpIsBY7pZ1x_c5yFnGh-vdhWhC652T4P02AlpRYAsGZA36fp_BnjDeyHz6Eo2TaDaNLTCD24k6FZXV5C6e_imiEOslYkiKefXWxAvK-GACzNMDM7mKHjvCJR5V4Rxlv5mYV5P0U39ZtcFzSMsPsLYBzUeUGQSeD3_a0yqHtueHiqmlO_-qcpvXKbvrxe4YgJrukzfoLBYaw8NVH19mcIj0n256yCu7Ge0Xz2E48-RmJBZKCuED8k-xYMnp6lykyrps-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r12
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/76606" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جدی جدی یه لحظه داشتم فک میکردم بیبی و ترامپ با هم دعواشون شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76605" target="_blank">📅 09:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امشب، امشب دیگه آتش بس نقض میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76604" target="_blank">📅 08:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">م   ج   :
ممکن است طی هفته‌ی آینده به توافق برسیم.
یک توافق صلح با ایران می‌تواند حتی بهتر از یک پیروزی نظامی باشد.
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر را بگیرم.
امروز یک مشکل کوچک پیش آمد — ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند.
پس من با حزب‌الله صحبت کردم و گفتم شلیک نکنید، و با بیبی صحبت کردم و گفتم شلیک نکنید، و هر دو از شلیک به یکدیگر دست کشیدند.
🥰
😊
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76601" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ3fiy5mjVPnIqA_tU2mH1rcBnNklbwQ3rzCrgJiIgi-fp0RqNKm3S46WrUvoFNMoQ54ny992A3mI6lagK9vPqpnTX7cDbw-d-MmqZWcamk_Fijd13m2MbwVrAhAvlwUBwctTSW5pRrnyJA1cr24P5r090fknIgn3sdtHWeDRWsGBWnXJNooCjVpjvH1_IFLhm9b8NzNR90RRuS7BNTFnyEhkWIOreZN88-pPs11zxZdb_4Xp8St2Mz0eIlIdccIJN6guEHLdp1p1R6z1ydD364IiHv0-UATSdMFVs1-L59C3fGa3ywF4IgxOZxLr4jD16FJIQGrG9P2acCiHGnJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76600" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76599" target="_blank">📅 00:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی ترامپ را رد کرد
نماینده حزب‌الله در پارلمان لبنان اعلام کرد که پیشنهاد آمریکا مبنی بر توقف عملیات مقاومت در مقابل عدم حمله اسرائیل به ضاحیه جنوبی بیروت غیرقابل قبول است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76598" target="_blank">📅 00:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو:
امشب با رئیس‌جمهور ترامپ صحبت کردم و به او گفتم اگر حزب‌الله دست از حمله به شهرها و شهروندان ما برندارد، اسرائیل اهداف تروریستی در بیروت را هدف قرار خواهد داد.
این موضع ما ثابت است.
همزمان، ارتش اسرائیل به عملیات برنامه‌ریزی‌شده خود در جنوب لبنان ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76596" target="_blank">📅 23:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر دفاع اسرائیل:
واشنگتن ما را از دفاع از شهرهای شمالی باز نمی‌دارد و به هر جایی که در لبنان لازم باشد می‌رسیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76595" target="_blank">📅 22:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تشکر و قدردانی حصین از بچهای سپاه قدس که امین منیجر پخش کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76592" target="_blank">📅 22:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏تحرک جت های جنگنده در تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76591" target="_blank">📅 21:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76590" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حزب الله پنج دقیقه بعد از توییت ترامپ به شمال اسرائیل حمله راکتی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76589" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دقت کردید که الگوی آتش بس لبنان هم دقیقا مثل الگوی آتش بس جنگ ۴۰ روزه بود؟
آتش بس بعد از یک تهدید بزرگ
احساس میکنم همه چیز داره طبق برنامه پیش میره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76587" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76586" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توئیت جدید ترامپ:
من یک تماس بسیار سازنده با نخست‌وزیر بیبی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده است. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردند که تمام تیراندازی‌ها متوقف شود — اسرائیل به آنها حمله نخواهد کرد و آنها نیز به اسرائیل حمله نخواهند کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76585" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یادتون باشه ترامپ داره یک شطرنج ۶۰ بعدی رو بازی میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76584" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری تسنیم:
اسرائیل از ترس ایران به بیروت حمله نکرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76583" target="_blank">📅 20:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
اگر حمله به لبنان متوقف شود امکان از سرگیری حمله به جمهوری اسلامی بیشتر میشود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76582" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کان نیوز  رسانه معتبر اسراییلی :
ارتش اسرائیل قصد داشت یه حمله شدید و سنگین به منطقه جنوبی بیروت انجام بده، اما تو آخرین لحظات بعد از دخالت آمریکا، این حمله لغو شد
گزارش ها حاکی از خایه کردن ترامپ می باشد.
@FuunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76581" target="_blank">📅 20:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تلویزیون ارتش اسرائیل:
عقب نشینی میکنیم
ای ترامپ کصکش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76580" target="_blank">📅 20:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسانه i24News :
آمریکا حمله به بیروت رو متوقف کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76579" target="_blank">📅 20:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اگه دنبال کانفیگ با سرعت و قیمت مناسب میگردید از این بات استفاده کنید داره گیگی 3 هزار با سرعت خدا میفروشه:
@vipamomamadconfig_bot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76578" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76577" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7IOxXnpeN7tTWstFJMpnzcDhpCPc7xOu9T8wfkZRY6blV-oXitDGyeqtpazvCrHqHB5qwwNGEcnhmaqTGUSA0Bw8rsjMvQSrxa_upiTjqgnwymeNCvnoUxJBOt8LSr3yMfd4z0cmjmmVlUy1N-BTd4275mDYnj3dfDC2QPtBJmvMvbI1KpOQAsteRJy9M8As906jeAGST4V7qrjaRb6vxCiI1AcuW-A7PP3DNdxVFmNlPp056z_9_ZBDg8jflwdkP5LhRO-hXEU3sc6BliClWv2nsjEPw5cGW8LqLQNXLpi2tCW67tQalRIeea8cWh3ZzBeu_-bNRGpgf8iJMq0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترویس اسکات دیشب تو ترکیه کنسرت داشته، جای خودش یه سیاه پوست دیگه رو فرستاده براشون بخونه و نصف مردم اصلا نفهمیدن خودش نیست  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76576" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76575">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ولی ناموسا الان ساعت 4:25 ظهر
با کانفیگ علی وصلم و سرعت ایده آلی داره</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76575" target="_blank">📅 19:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانفیگ گیگی 2 میلیون موجود  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76574" target="_blank">📅 19:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یکی به علی عبدالهی یادآوری کنه عاقبت کسایی که برای اسرائیل رجز میخوندن چیشد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76573" target="_blank">📅 19:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:  اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76572" target="_blank">📅 19:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:
اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76571" target="_blank">📅 19:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejuD8jbB30NxEoLsOyHKqVqoEy4gmWiHFu9LQuxXMOhJWiT9ytCvb_F_-GmpPIDRsnjf6elKHfWPQvtoM7Kure9F4jt1cAJH1rutVlvEoa3pUDBUw1nkv_4wriYGnC3sryrug0j5rDidrG4s550I6liEMp4k4UxdfzUHWX1FJWDZue-7d2s-va8NKicdSINNOSKZIvpfEkWHbxxShmX8zpdT3-0gRV9I4l7i2eIjrhD3znlkLV5wjR258LZIEq-O2l982W-dytHodP4_G98B9BsegM5sYueTfQBCtztr2ezT1PBl-zf6Dkfpe7JILPm3LHoWw-hjHyDf21ce0ih9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جهت حصول اطمینان اسرائیل از روند به شدت مثبت مذاکرات، الان ارتش اسرائیل برا جنوب پایتخت لبنان دستور تخلیه کامل داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76570" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داده است که احتمالاً یک حمله موشکی به یک کشتی تجاری در خلیج فارس شمالی، ۴۰ مایل دریایی جنوب شرقی ام قصر عراق رخ داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76569" target="_blank">📅 18:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=R6KCNH5PT-j6d2RWEyQqjSqRe1YLnJhXi3IyopMZQIKivUvCnkPqdRNLt3aykzbm1sIqDHn3FdWrtZ8xAGnkcII6nxm4xfMh1_CT-q-2joI8X_Kn3XK42vratH1uuhoDpjPZZIJkamqAOZnHCoCnCPExO1M7vf8GYJpB4X7IpQZi_0JcL-gcmBqJaUaaXmiPJdBiJgTPFdpwLTVEApjIL03ZEAtYKP6DZOjMu_bjY99OoHL3BtfVCkLun27MRG0yfTB4EPsvUHXhWajJCxUCUIyjIJmnqC4pVylTVHK1cejepC9B5luT4VP7QFMs81eKuxUSO9p5iCV8hVRPPN2sDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=R6KCNH5PT-j6d2RWEyQqjSqRe1YLnJhXi3IyopMZQIKivUvCnkPqdRNLt3aykzbm1sIqDHn3FdWrtZ8xAGnkcII6nxm4xfMh1_CT-q-2joI8X_Kn3XK42vratH1uuhoDpjPZZIJkamqAOZnHCoCnCPExO1M7vf8GYJpB4X7IpQZi_0JcL-gcmBqJaUaaXmiPJdBiJgTPFdpwLTVEApjIL03ZEAtYKP6DZOjMu_bjY99OoHL3BtfVCkLun27MRG0yfTB4EPsvUHXhWajJCxUCUIyjIJmnqC4pVylTVHK1cejepC9B5luT4VP7QFMs81eKuxUSO9p5iCV8hVRPPN2sDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.  @FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76568" target="_blank">📅 18:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فدایی تو تجمعات پاریس  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76567" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=o8GV8dGskwuJ1cqtbdx0_Y7QfrWApnF9MjaEloEww26fV3H3MPKK1AWVDRW6tUgLiJTHChDjXACsDvlDmav7ZJY1wyf8QZ5vAOUZ-5DfATw84Z1L-Azzj_9EqEanzdt-Kwe5DT8lU9yBIrgV7wnC7ueMt8JARK-p6FrniwzFet2Xef4Fgu1VnKb2202-GW1dYnvg-4-HcpS3UP5pZR3VkpbLzWWR97lfTBNY1ztCD6KkM-dFh-bzeYSASB-KJwumWRdUFXE-lw6oW_AwYBDueIjyw5OZWEMtUynjliE-fo_AJ_6rzT2hJC5u8oUBNQ-uJoR4KcbQsr2p6ZiRb7RrJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=o8GV8dGskwuJ1cqtbdx0_Y7QfrWApnF9MjaEloEww26fV3H3MPKK1AWVDRW6tUgLiJTHChDjXACsDvlDmav7ZJY1wyf8QZ5vAOUZ-5DfATw84Z1L-Azzj_9EqEanzdt-Kwe5DT8lU9yBIrgV7wnC7ueMt8JARK-p6FrniwzFet2Xef4Fgu1VnKb2202-GW1dYnvg-4-HcpS3UP5pZR3VkpbLzWWR97lfTBNY1ztCD6KkM-dFh-bzeYSASB-KJwumWRdUFXE-lw6oW_AwYBDueIjyw5OZWEMtUynjliE-fo_AJ_6rzT2hJC5u8oUBNQ-uJoR4KcbQsr2p6ZiRb7RrJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی تو تجمعات پاریس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76566" target="_blank">📅 18:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با اخباری که از سمت خبرگزاری های داخلی میاد بیرون
منتظر پرواز دلار به سوی بینهایت و فراترازآن باشید
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76565" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAhtgBPyxjWNTgy3Vy1tqFfIG_uhMpAbt6eslaoq8m2WttMCUZJfT8hkPrBk1Qm1kpupSxZGF3NKzPD-h9Ef0yUE0hIY523vrPJ0PSwjffPdNzwkKYdPoDi-FhCF6cztaYVTj7a0va8YTOl0X4eHpmZCTInPJnczn1dz51Jc425kT4dEc2-4FDy6c_L18BzoAHbyuscwh-utaf82XmKCJA4rKkm6hEmSqzABdGpGBOZCvtuH-kCfecsWgGOfMkNcLtDAlhUrkvDULZOvBsr8Ex7Sn4XvHN_8wPjhUU4nUo_IHkuVxYntQ7F8aQeD_pbP_1vMKYhTQKhCGDbHy-vycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پنالتی هرموقع یادم میاد تخم میکنم.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76564" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt422Ex2EtsonybfBDpM2dV154SxqBXC7gdsqUhK-99Le-_3_IYr7ttnenvo-lnUIzK0Zr_RMHi4NXw_Dq9zG02C0SCkwurfdRkAWqsYM_CCixptaQWzl-9wGq1_2YAsgKrNmBA1Z9750LessgxMD7M4Gb7hP_Ecb1Efbo0Cg3Ccmi197FiVS8jgh3a_wuua3b4EKgRht2sCtgY4kkMbbd8Xoa0mcunlWP58jmobGwPuZ6VlCAusE2tqzqpvzWMWXpXL2F4Dx4DzqVNDWE7oDDOZH6bh6Z074ElGzIf6-m4YRdEdPcZQ6VrWAWuDsafNEv5cpXDL6jWnUBBgEsqwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده چجوری روت شد با این وضعیت نت همچین پیامی بدی؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76563" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9teHL_kxfn2xtuyshe7J9--eBMbyTk3LMULDBPtthu2KLOw3MICo9rpVMK0o265NaUQVf7r5OVyfaUu3eGutNH6JobkN5cx_JisoinlpqUznzVKxAVSK8FIr9h8oLrEOouJ3iMuezMCqTCfTztI3iB-5qAtLHPluc2XsZlA2azs9rcoBA9MqV_ZE58YeGzLO2_Ed-WZjTvuhe3joOwughkX_VafEvOlq_ymHfNHpT12iY65f1Xi5QiRncxJLvsmX6ko9aaHiKnGT4ufiW7AhkjUMM99AvUs_pG69hxyNDxSz6c5XEpurSAXdEq2plCfiniTgDiqTs3pMemD7Bs9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76561" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبکه 15 اسرائیل:
ایران تو شروط مذاکرات علاوه بر لبنان، غزه رو هم اضافه کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76560" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبرگزاری تسنیم:
ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی در لبنان و با عنایت به اینکه لبنان جزو پیش شرطهای آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم مذاکره‌کننده ایرانی «گفتگوها و تبادل متون از طریق میانجی» را متوقف می‌کند.
▪️
توقف فوری عملیات تجاوزکارانه و وحشیانه ارتش رژیم صهیونیستی در غزه و لبنان و ضرورت عقب‌نشینی کامل رژیم از مناطق اشغال شده در لبنان، مورد تاکید مسئولان و مذاکره‌کنندگان ایرانی قرار گرفته و تا زمانی که نظر ایران و مقاومت در این زمینه تامین نشود، گفتگویی در کار نخواهد بود.
▪️
همچنین، جبهه مقاومت و ایران عزم خود را برای انسداد کامل تنگه هرمز، و فعال کردن سایر جبهه‌ها از جمله تنگه باب‌المندب، به منظور تنبیه صهیونیستها و حامیانش در دستور کار قرار داده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76559" target="_blank">📅 17:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منابع داخلی میگن مذاکره گوز شد توش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76558" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz4ZWdfGG1Qk3Lty8x0QzznFN3Jw54Vx1qWxKD2Rq1toHVTPo1P7rDMOX-atBsOYSe9X5VaYWtZf3X6XV7qaGqsZhWU1pE0U5egr9jDXzqXlnWKtcr_qTs-_rxIKJUFWWYqcrD_DW41adZR4HkJ0crrz7a9f8xVbEEOz4zDB_4awYVsQD1r9R1ce9YAnSkszFBlrfoTjhi1pD2jC-nno5ZMMNwh4Xqm_94NNIsBHqMpKSWWvqzdUuAvV7t8g2MCLVKYjKJfOy3TRVHplHi8cAYXdO0rAC9d28HYbELcuesCFv8moYcd6wHqZMxZipIWGb1Faw-LOdnk22jPRN-ls3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رخ
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76557" target="_blank">📅 17:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2Oy4timl9p3iZEC8ub_fAl4Bh7bHoff4tbpJUw1KkFfI-N5zFG-r124DqvWOTGIUu7U1T8yG9xBWHASJwk8J7X2B2XUpBcL49bV8OfUEgmNMgjUdieMvMhQMnqfSbIEm588W8iw_ePoK50yXUMvTguY0WrD5dXbJ47Vcvrcu7-PiK4kqtNEh0xaITJuihB_RTMjMJHW_QaOziWvwJWqdXkL3l_zt2P3pUpf35iuYlGb1ZCAsYUS_KIm_x6A3oJXh4MBUzspwlQ8OuSznvygO5h_YfgugnxvLrvoIRnJ0UibwP_AGE-7G2Y0rpyyd_rWm17P2zBStP6Ao6NnrqF1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزو انداختن وسط کفتارا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76556" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دعوت تتلو به جام جهانی مطالبه ملی ماست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76555" target="_blank">📅 16:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آمار رسمی تورم اردیبهشت 1405 منتشر نشده.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76554" target="_blank">📅 15:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تتلو بعد از دعوت نشدن به تیم ملی:
کس ننه قلعه نویی
👿
۷۸!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76553" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
