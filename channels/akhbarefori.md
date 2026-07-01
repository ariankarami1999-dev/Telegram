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
<img src="https://cdn4.telesco.pe/file/i58JyhUHqgRorKnq0hR06cOP1HlmhmLaf1WZgc_51rUt6ljGSwVDzKAWqDWXz3CmN_twpNIg40yDOQ3PfU_oLn1NT19fjS90MX0wixWFjXJBdTwKp3Tcj2nFW-BwMpVyjJM0U6h6ibjY_R_69D8hm8-7PLJbUrtxn-38GppcDuXDw3z80DSYHthuwmnXRsUvUFeo9X2Xsr2SrEyyntcJwbAjStyQ2owav118SMUaWHup9yOTqCcuNje-xscnlAuUHgdThPnTDMHlHdgrR26YW8w2bDo3cg3OyxOXq1tz3BgxBUkyj4fuYFhT7RtCDnzD3F8HXV1al-5_bzT0Yoo58Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 03:19:44</div>
<hr>

<div class="tg-post" id="msg-665506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os95eWi6DrYpoBZpn501bgnk2Qgl3gTnhBJX_BXWIXWNZaEHqDRn3QeFaPHUYQ2CAdlMHmzXLub-fo8MMeRCrAHJo-w8_h_xilRkAKiRG-yTpk3Y64S6EK6xjNBuJrvhaFW-Bp7mdTVKqiOxStgdmFY3j4sg03-DjqnZxRtNG0T4yl-x5AJFiiwYRf4NGv6C0To4wbMwqB0ADFEwe2dK3ay5CrkI0NRDDQZAm3j1vRKpfmYg_xNR2QW2bti3qj29EStmwngvNdUFpJqJkJzrz7U9_yy-g74R7e9NX8jf5fTbLNB-QdoX4kQCsXsiP-3NpJptWgfM9PdSd-b2TeF_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
پولت را پارک نکن!
پولی که راکد بماند، فرصت رشد را از دست می‌دهد.
با طرح درآمد ثابت کارینکس، سرمایه شما می‌تواند در کنار نقدشوندگی مناسب، بازدهی بیشتری نسبت به سپرده بانکی داشته باشد.
🔰
سودی بیشتر از بانک
🔰
نقدشوندگی مناسب
🔰
سرمایه‌گذاری با ریسک کنترل‌شده
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#درآمد_ثابت
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
اینستاگرام کارینکس
|
لینکدین
|
تلگرام
|
وبسایت
|
اینستاگرام آکادمی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/665506" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromباروبندیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbvN2nsg7Bf9fHEmLqtQ92crxboR7iVEo3dDdskI1aEtkof_0HxXY2fc2OKSEr5QQU8TODazp6-AqazGb9lZnbPNmKV8WtER-mLFDdNg4FfdYxz2wa21QQp8rQ2V7xrbR6d0tNMDfX-1P6RxaXWf2vWi0wkwllKlc7ERwUMOBEjzWFPao4rFoBT7KzPhu-XGOzCpFlrNaMuzRZ9BmMUpYegXtjZBKHB2_ngTSHv-u4UnoublZEXtVC4SYrajEJz5eI491g7iq27h_E_hh6gPNGz4rp_mbAqogbBQ7UP3TDWy17yrCVhNlKufHdt3GpSCjm7rcN8Tu_RuiVUm_t7kSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
باروبندیل‌ت رو 4 قسطه ببند
باروبندیل
بزرگترین و تخصصی‌ترین فروشگاه کیف، کوله و چمدان
🔹
برای خرید از مجموعه باروبندیل، امکان استفاده از سرویس اقساطی اسنپ‌پی وجود دارد.
🔸
امکان خرید مستقیم و حضوری از فروشگاه
🔸
ارسال سریع به سراسر کشور
🔸
تضمین کیفیت و قیمت
باروبندیل؛ همراه استایل و سفرهای شما...
@Baarobandil</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665505" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وزیر دفاع آلمان گفت که برلین خروج کشتی‌های خود از ماموریت مین روبی در تنگه هرمز را بررسی می‌کند/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/665504" target="_blank">📅 00:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665503">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRQSMLHdVZzwagHX24LElI8HNwZvcrNFiwR3w4ap2gzShtiNxhh8Zz4KqRTeH4KtCM6L0N-9wWU37kxm55ZxiGaSES38UgKy9Eh1GpnGNhtcfCCzmkQlsZ12LJFIwMu7eFPcQ5xocHWiCgFP0eoXinr8cGh-K3IYbsGfWN6FqGGqc51HGIpnbUpzoWet6NBrX2NGi4LUWEv1RJYnWsO08ihMJHZkohfncogm0nFz8NasxviHMTy8oj2SVQ3eg4hl7hJU-L4_-24U5Aj2lH6TeuKyfUg6Io24c8fv8dmeOlXEmBJG9Szi-B1f7AKRcFYgdutClmPk0Bxc1JO1e5aJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانیا سر شوخیو با باراک راوید خبرنگار آکسیوس هم باز کردن
باراک راوید:
🔹
این روزا یه نفر (که فکر کنم ایرانی باشه) داره خودشو جای من جا میزنه و از یه شماره آمریکایی تو واتساپ برا آدمای مختلف تو اسرائیل پیام می فرسته.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/665503" target="_blank">📅 00:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665502">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5a9c7c5d.mp4?token=tQq6sIkzOzEzTNa16cU5BIHOuOB9bprhvHXryNxmr0fdO16UtuuSH6GP1PIFnpVmSPh_tq3x6KcnI_2A-Nl3JHAdQs90oyIz3kUAuFqvsy3ihPvGKKyYU4w7-5YDKAzsj1Ceq6qwjphlnneAkmJsfKgtitiIbuKsbFqSLWR50m5BxcEpx2cB1nLw8jfuCdVhElzcEhLxr1UepOWWoqVNpwl9t0Ub64IJOgY4F5UvZgZlwhV6IxBBBvdsH8ZOecCTqEjNsYSMB3GyWdZ1Gc9ba3w20w0UTzyyT5xTpw9poDycmPee3XqHsxhuLSEDpgiRlFDnxzug4esb41C4GM5uRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5a9c7c5d.mp4?token=tQq6sIkzOzEzTNa16cU5BIHOuOB9bprhvHXryNxmr0fdO16UtuuSH6GP1PIFnpVmSPh_tq3x6KcnI_2A-Nl3JHAdQs90oyIz3kUAuFqvsy3ihPvGKKyYU4w7-5YDKAzsj1Ceq6qwjphlnneAkmJsfKgtitiIbuKsbFqSLWR50m5BxcEpx2cB1nLw8jfuCdVhElzcEhLxr1UepOWWoqVNpwl9t0Ub64IJOgY4F5UvZgZlwhV6IxBBBvdsH8ZOecCTqEjNsYSMB3GyWdZ1Gc9ba3w20w0UTzyyT5xTpw9poDycmPee3XqHsxhuLSEDpgiRlFDnxzug4esb41C4GM5uRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع غیررسمی: مقر احزاب تجزیه طب در منطقة «ديكلة» در اربيل هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/665502" target="_blank">📅 00:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHb6S9mVnZhitrgjk9krKYo4hcYeK8ady4CAGWeOyGoCpUOckHGlh0j3pXjkAApjxQ4YS0rCv6fOBjCz7HDGg871FJMgFbTeFbkDAtWJj8mIYLcBfWYWA_WZQC6Gj62lZ5PZO3veGsBByqvXt5f3GVFMH_nBaP8CtnRUr_v0wI90k-v6KWiPV0PWT_sXWvKksRbjLFrW2aAOdzxBHQtpXXrMRvGXq2MZprzkRZCBw9d-YUO1MCGeBU4ML9Bq8kj6YIn64coP3JNWZ4RYH7QY5_3ME5EkRgWea0mQB9D5UIvsZYK8BkFAi81yP1hlfRFMixpPHOtlmRu5OywuwM2qqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbyzXI9lA8otjORQbLNKkmcJyEgl52IW2Wk6fmJssxiqBbsINdyio1zW6q3WpOPMUaQzRjA_gdYdlHJQW8MHmqamk6pYgm7jFhbmEm2r3VVDb6rLaxmWoGTgItuVYTpAm1ER5W0WBuNhU4w64ikvlHoLHp3JfGTSm-B7bapggBpT1aSt2oePj6msz-mRErAttE_Y9xY0xDM1S7-2oryC3o7qcVoTw6Gh7kwUfZcXjtdHroEw02feMYQV3Z-2heh1jJ_KjkNfB1b8Gl_0upfSXuvTP6jef67K1IO5HMzJIg-ZmXFmmAa2mDYpGiYnWzil-bKRL27fVvAE_ScnYIgUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbsBmnL8_GQkirNRSYkyM2Nuf1s0__D6vWt6XpF8xXiVh0Y-DL9qZmEFY1otZ8fD49K74Id2LvPAW61ymiVRkj553XLcG8nXN_DTqFDPZIk1NFSuq_a7wIGWWNswMOaFe8s_Yp7cOtiB3mKIVwud5NxFFcG8pWIx4kjLAKw9sr8O8RrYDfGyaJrMVMMhCbMWiVPjYGY7QShT9aVl_PqVc43jG1OM2JS_VdgMZ0jnEJVb5ku82isJRzspjv_68RrXDKOYoMpdjADfW0gCjEEJLT7v5MiII8tWqZVr-Z9dPl5Z8n-TOOxpeeA6hnboFLWaeAOVXWnO2asN4JDGBd3yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5ez5UnAnex8VLb6zZxG7xJ8KS9lXSfAb8sy9LJtw2OY-DJV0IsuM4gG97OHBEErbstC9_jk59Oou_8POXOiaBOIAig_bK0QbsQUW9B_RsN-E7c41uB8pmFIiG-jJk6GiBNWE_fcJHl2J96fvfUFnMWmPNQIrfO_Ce5NYR-GDAL3Q12J-Fr-Jw2J55Se-aAbtVl7uPo1gtzfLZP7aVQ-k6L6awfAgOuWJre-mMiA-uMMiQlda8s6uCDGQrRdYajmop3R-VDZ8Xs6puqzv764l_GsTTRgjVQeqvpIjCYTU_W8Hc_goVqqU0IM2h0jXRSJ2XoRcenxz_MitJHRjnoyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns2SxFeZmkUZrnSiHAR-hk-XgfkIQb9eLgyYobWqQB4_gslmlSH3aydtcTWKS-N4b1A_a3zSey29eLNsidD9JFCRlFAJJg1UwLEkkSv_7fIEmZCsqIGa94Y7D6jt0yYFgdBvnx5Koldd87210IturiSk8GF0E0De5rHE0MuAuI8itbHA-upHJ_ja5pdYTvog6QEhRM8lC9wXKPS9z-CbwUg14ck8Kd35P6FtLyPcRoWXo7XniGvBpN_hcEPIxe9qpJgTtGik8NZQOwZ9jffKhqOwM8lk2sUSa8DAc9uEn6wRIQtcKhO8J7AFnpNc4SKtjvgGabPTOUh2ojy4qD_MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpRJ-TQMh8wVKWK3ZxjLeWytFkAxeE8JzDPaRAVf6xrYLy6MuV9GI8GY21qSD62Z_t-QGGWfRI8uA6a9t77c8NfksIbUkRxz7iHx35GUud_ebiP3iLkL4ZHbkyW7Tl86J6GZJGk1P-5HT4iLnlCHAoRAVGfITN57RCHqohBUtgunuE8AIKues7agDk6WO8OBA8WjzyrJB_h3O1UxG1u16wkV3n6_0jrkB9h-ylXDb_5K43dZOj77Waw1Pgww-qCABTl1XX7_QbCJtEFMYecJINbnHK-qpuazZHgAf9mDtXDOQEDeibP3qENziykt1e-DryC6-MlDsWYrhC394x2wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzXfEC3FB3aW2ZCDmYBBOYIxjzkAhtR7hN_nbJBxzv0mEpD-bMHEDwKhG5sQEFzgnLZHeyecFFNwSCmFCfUdTsQpviE6Cm_Ve9zZF2Mtw27dqoukEhSCXR5irSvZVSnROjytsJAay05vRk7T5sdx30dBBvmQ6YzKZXc0BgleDTvsyZZhKxHRdzGyfJMU2Tx_-jZoAmKjL9FIYtIXqUAQOjQa-GE4MvLfzR7bDuuZSgHHDlU9chYs6navaQk5M2jnXxcWorISclA-91qWaCElPy5OAxwbQy2hBB1hTtoBceo0Br0F5qlOpPcufOlLinhmuAq6iH11lzKdRAi3PQmMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJN4bg7pf6ctrcFqdIuYqOfSjZynVjT9qjbLh0XFH5g2FYQNufZj2LdzK_nPoNB3jvD4nsSA7idoWOoAqcukwj81ElXGHeY0SZtzmP_ALw8gcWudg9nnU8dpxVB-4IdKBAlQDf6nUgnFQBMoYNeDYKKGvMMGk_RJ-gTkTawHWXWQIHTmZHG5SCYHlKaoDkZ31URyd3iaCnn_h8-Bmd7ESfzMcIfevXH66mgyEmt2ZG7Nxj0gkNSgnngJ8zLNK0DVUP7NOnGJ8kbieR6VHIGfhitG7CE99YnMPL9nzz8_WReQFK23b_1g38wLN1T3A7P_PkrW-LEP7qAUp1-DBtVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xlh5p49ml4T9Na-sCShpaoA7LkOkdyicM7gbv8TbXXuUHiPTuiBcsj-CbShrc7-VFiPjjNwTQSEd6JuA0in-Iyu4QLX67NMtWMBGSdL5OarUTs-1pGuAwuo_1BNx3Pf7g6iWpUfqdIfKOvEK648t6H851pF6D1hNFoURsbwj3iZyfqPim5WWrQvsxpIWKY-O_kRlbIVqIwxZbxZ-Mk_cdJrlJAxK5TWtN_gaUkl0MMUG2WFRkflvlFInUNgSMAszPEYo2KqTbzJFMdBGBF2h6gVhb2dNNYfp2shHMNZLV-SMnT8Q6FOnSNzWDWSKZYPDwd17BtWSv6H7jkfzc9vXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZiLdOkQx10gscMpcUHACSfxM4Lpty1JcPG2kuJSMgPom2dh8eb3zqtQ0oJqjXO2FmWHkvyUxG8yZQIjK6bWAEfOCN6RaWJ4u3Ee09OxHYAZPo3nx0XiDzY5TYaBHWq79gnHUeHTFi2QKLYPuusHs4TlkCcTorFfIkGt0SkLnH9TjuMh3zGE1Hl9Ln7_oTozsb0-a-lBK-zEvK37uqKtVBeNAqTNFXEl15KESJqWgBjY31BGr8zu0d3-kKJKBuZoEz0zhFmsI7PbqjHXcTghulIm5UxZmD1Rje-U78C1hZtbS06kSB7SRrzpoDFJ9v5B8ZqWugpRXErme7rzcCWiaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طیف جادویی انواع رنگ ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/665492" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f12a6b4bc.mp4?token=beTc1WK69TVQcFrtdmbSX6WNLuzsIKvDYpcclFsvY7uAlYGEMo9aOOqIwz8Lp24a6a5b_tG_tSOST8bPGmIC6qNROp2da--9L0i7yBRxV6ASwOAvgAY-qry38QKzHnP-18jZFcy9eEGsXSCYqyaArgMXO1Xt-oEuIrInIucOEBtd4_p_A0axzJBtm_ZrOSIIDyBGczE85dCvfvUIpauzKwzwZqvlKLUV-Oh3RBoryuLL0PX6QxxJ1C5R464TiH6muL3f0a9Q02HH-n8bi0SBHKCDON3_0fNBRC4iuhG3u3jq2JdsMxZ-CxBVLum8L9L_W38RAT5frERiPvi4C6voCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f12a6b4bc.mp4?token=beTc1WK69TVQcFrtdmbSX6WNLuzsIKvDYpcclFsvY7uAlYGEMo9aOOqIwz8Lp24a6a5b_tG_tSOST8bPGmIC6qNROp2da--9L0i7yBRxV6ASwOAvgAY-qry38QKzHnP-18jZFcy9eEGsXSCYqyaArgMXO1Xt-oEuIrInIucOEBtd4_p_A0axzJBtm_ZrOSIIDyBGczE85dCvfvUIpauzKwzwZqvlKLUV-Oh3RBoryuLL0PX6QxxJ1C5R464TiH6muL3f0a9Q02HH-n8bi0SBHKCDON3_0fNBRC4iuhG3u3jq2JdsMxZ-CxBVLum8L9L_W38RAT5frERiPvi4C6voCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم سنگال به بلژیک توسط اسماعیل سار در دقیقه ۵۱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/665491" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141968195f.mp4?token=mlZHYLePdckZ77g7O7_ihBF33CT8fhFH-arr-ugKe1Mb3pPZiOZHQuGuPW6IzlZRnVjylWfFpHLsZlT1Hbp6ywBAtzfGsHhb8CYwW-YqQ6zXhuyqYAu7zYevzMH2qaBarCvuH6ON2djvn4mloMq-oDzVO3YL0zkUAVYbNVvspN50y5WJ7MD6d9UjMSUlsFGT1l9F9F0Ck__aXT_o4s0Ek0VkQop86CDRf-gN-ky6z8m6sc0rmeJn6WFRBDZiBXI_TdWgGzzoe4p3VvwF79c4ux0sHadQ4v8NUfcWE7PepAL8M09BB8h5-4QcGZwkFBZ5M-7tq1Q7tyPx7HKOPPXGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141968195f.mp4?token=mlZHYLePdckZ77g7O7_ihBF33CT8fhFH-arr-ugKe1Mb3pPZiOZHQuGuPW6IzlZRnVjylWfFpHLsZlT1Hbp6ywBAtzfGsHhb8CYwW-YqQ6zXhuyqYAu7zYevzMH2qaBarCvuH6ON2djvn4mloMq-oDzVO3YL0zkUAVYbNVvspN50y5WJ7MD6d9UjMSUlsFGT1l9F9F0Ck__aXT_o4s0Ek0VkQop86CDRf-gN-ky6z8m6sc0rmeJn6WFRBDZiBXI_TdWgGzzoe4p3VvwF79c4ux0sHadQ4v8NUfcWE7PepAL8M09BB8h5-4QcGZwkFBZ5M-7tq1Q7tyPx7HKOPPXGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عبور و مرور از تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/665490" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD6RbEhG3WUANFXgKDts7639e5jhR9vIg3d6r4zP3VPi1pwykI2WXcumOMWjYkXPKLSr3shb47a4X35dMtGDzrAkrH-uO8HKtMdFAsgjV0GDtTBVCbN9l8FuvFDMg4_MLBA9rTjyHjnMyAYhr8kK-ZBvRw3V2NM7kThprbg84-pYACyljmntg2DH9MhaRtW147s7m09RyJHTe8lzLzfkXBGxe9Cdl0TYJymVwcxe6WXu2a7PZ9kdXq5kM5OcnPCSOI-4oqABIfsmSeEUrvs-cwNjKWqT0EqEUj2BNLCMSJL2m6FdGH_8wSTAXCKhtukGm6nb1mLT1bbGjW2T8UKdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در اربیل در شمال عراق
🔹
منابع خبری از شنیده‌شدن صدای انفجار در اربیل واقع در شمال عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/665489" target="_blank">📅 00:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در اربیل در شمال عراق
🔹
منابع خبری از شنیده‌شدن صدای انفجار در اربیل واقع در شمال عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665488" target="_blank">📅 00:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پورجمشیدیان: در برنامه دولت عراق است که یک مراسم استقبال رسمی از پیکر رهبر شهید انقلاب در یکی از فرودگاه‌های بغداد یا نجف انجام شود #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/665487" target="_blank">📅 00:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621185e0cc.mp4?token=p8A4aD6mZFOfhSwGTR-NSU9nb2OffPYBE4CGLEWMD1tkbjFvxwhSEZx7fyqyBDArhqqtxqLAvnWwOMPELIuHpPahuiIERlMtwh-bk8ywazotlrNdTC41ZYnQsW8Oz3Ely9v4PDOvrE5sM66IwS9k_L2A7SWC6jxjQfqkqq4bUoyOGfgdRovIZCObsJhaDxvHdG3QHs0WHqx1kby28-yQRBmajOgehwVS56k9Za4qrChn0dpA2k0f-Z_4Qxqrj1z-Mmj6q_gDC-7Fdp2Kf1DGU_lN5NjXWocVM4X37do9ag4jAwkVl5-ZaR1AGe3ZQjwS2Muu6xLNQIO-f5SGFW6uWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621185e0cc.mp4?token=p8A4aD6mZFOfhSwGTR-NSU9nb2OffPYBE4CGLEWMD1tkbjFvxwhSEZx7fyqyBDArhqqtxqLAvnWwOMPELIuHpPahuiIERlMtwh-bk8ywazotlrNdTC41ZYnQsW8Oz3Ely9v4PDOvrE5sM66IwS9k_L2A7SWC6jxjQfqkqq4bUoyOGfgdRovIZCObsJhaDxvHdG3QHs0WHqx1kby28-yQRBmajOgehwVS56k9Za4qrChn0dpA2k0f-Z_4Qxqrj1z-Mmj6q_gDC-7Fdp2Kf1DGU_lN5NjXWocVM4X37do9ag4jAwkVl5-ZaR1AGe3ZQjwS2Muu6xLNQIO-f5SGFW6uWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های عبری به تشییع باشکوه و تاریخی امام شهید ایران، سیّد علی حسینی خامنه‌ای؛ ایرانِ پیروز و قوی پیام «باید برخاست» را مخابره می‌کند
کانال ۱۵ اسرائیل:
🔹
مراسم تشییع رهبر ایران، رویدادی عظیم و بزرگ‌ترین تشییع تاریخ این کشور خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/665486" target="_blank">📅 00:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8v_sNjkl1jPEV7CWVjtUXO2t4v_H3eRd-Y05O1JrkZSpWUhjcWxosbkZVI-fEULAFfYD-zDkbmqrlVaaGhCxJAWA295pDqI2OtfMDwhiQkLuJhbImQ2ExifwgdDcE5O4-Qr8PjdaSKuOfn84nXCHsQhqVDHizncfe8BfBXOkhWQP7_IC4EOXnguMNFJ2omrAUGSBsSjArXq2yaZqssc5Xzva1sS91qK8xXjB_huiRz5oWuBNuBHC987Ojj2y15ZpkqTW5wfKRSqk_7s8T0PxCwVP40jdbYtI1VqyC4WusCPkg9GOysEONi71SSwHYakdkyixM5QqvOo99dxHoAfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه راه حضور در مصلای تهران برای مراسم وداع با پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/665485" target="_blank">📅 00:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: طرفین توافق کردند که مذاکرات را در دوره آینده ادامه دهند، بر این اساس که زمان نشست بعدی در اسرع وقت پس از پایان مراسم تشییع پیکر آیت‌الله خامنه‌ای تعیین خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/665484" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a770eab7.mp4?token=adGeUAsgqUmYki1awdpH18pTGp8aOPIPzBpT3uYSGYe4XIlJmD8p_jlQLVywaa49XI31U8mjKgUNkEna-YfJjAJu-1dR6wgVqJ0ozyWZkqCQYs6Te_eiGGCUBLKJzla5K-jT4Quj7vYyeLhk7IorQNsjKl0EnDGFFoJlZSzJL07xYSpIIXnOZRT4wZ6K1XawweNfVRTTxa_th2QTTLYSxvv2dUgy3P8H3RdM4b5DXc99nguklsOZzd0RbBUr1NICMkeHEdGRZD5xBRVETu8aZZtWCoOAZ1oTXTlGxHjT6AgWb7xIaefSV3g2YyYD7AvujHsbLdpv-ghIt4lpZaK_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a770eab7.mp4?token=adGeUAsgqUmYki1awdpH18pTGp8aOPIPzBpT3uYSGYe4XIlJmD8p_jlQLVywaa49XI31U8mjKgUNkEna-YfJjAJu-1dR6wgVqJ0ozyWZkqCQYs6Te_eiGGCUBLKJzla5K-jT4Quj7vYyeLhk7IorQNsjKl0EnDGFFoJlZSzJL07xYSpIIXnOZRT4wZ6K1XawweNfVRTTxa_th2QTTLYSxvv2dUgy3P8H3RdM4b5DXc99nguklsOZzd0RbBUr1NICMkeHEdGRZD5xBRVETu8aZZtWCoOAZ1oTXTlGxHjT6AgWb7xIaefSV3g2YyYD7AvujHsbLdpv-ghIt4lpZaK_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترکیب رنگ جذاب در کابینت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/665483" target="_blank">📅 00:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ترامپ: کشتی‌ها به اعدادی از تنگه هرمز خارج می‌شوند که تا به حال کسی ندیده است و ما رکوردهایی را ثبت می‌کنیم و قیمت نفت در حال کاهش است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665482" target="_blank">📅 00:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بغض و گریه سحر امامی هنگام یاد کردن از رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/665481" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-jngHLCdbjAnq0tI_AkiCpNiq2-J_114jwROQc1KMJrjn9ZGlygYs6ANLn31WoMkWByeShGc9W0OQX53FckaoYcDm9P5Lp3GQ-MQHbut1D5WOXwfxz1STl6GPl6V3Sbuki8-KxY2DSH-0z2mzZuNv8RoY8q9dvLMF6kkzn3MBmBCs6hYQ9soA356sVlVagPkL-336lF2eqIj75O0-fAPgChYs3D9ClHx7YT40CzXC596EU5eQYJA_5EUPXxcQgS9Tve2mo9wKgksSRbgiicwRjx_Qrrlf7hw5CzOO2jpPH2eLnTiAk2oecfcJPBOeJRzONoHIgv66UmDQ3u7muECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/665480" target="_blank">📅 00:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665479">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پورجمشیدیان: ستادی در بالاترین سطح ممکن در دولت عراق تحت نظارت نخست‌وزیر این کشور به همراه عزیزانی که از ایران رفته‌اند برنامه‌ریزی می‌کنند که پیکر رهبر شهید انقلاب و خانواده عزیزشان ۱۷ تیرماه هم در کربلا و نجف طواف و هم تشییع شود #بدرقه_یار
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/665479" target="_blank">📅 00:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پورجمشیدیان، دبیر ستاد ملی تشییع وداع با قائد شهید امت اسلامی:  ۱۲۰ نماینده مجلس عراق با ارسال نامه‌ای، خواستار تشییع پیکر رهبر شهید در عراق شدند  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/665478" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6b1a1d85.mp4?token=kWuKVezmfuChMX2cazo9GKDsLE4-K9x-0oaGmiGAxe92Qw3y3E937JvOV7YtUYItgp-RWyeN8lA-GAic6o6QRNB4aBC3ivxDrXWTkWr9qFHCD6Ihm2ehAuVXuhG-gA6KIeVyXX3i-Nis3WjOvE4BW6ZBy9-L4FRsAfU5nCtqLo471ZWq_m1D_g1fYI4WZU_4r_txkMDEPJ05uIcSYGVGtTKVCwDvTdDMgEBJpTfFHyWSBHLlpnJ-2vDef7zt4yBLO39Mup67g5rOVw67S03FVSvt_c6JzEyg5BZrLrv75sb5TntshqeNSEyJPE-yTeOOMd7V3xrxeZeMMRMAq_TC-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6b1a1d85.mp4?token=kWuKVezmfuChMX2cazo9GKDsLE4-K9x-0oaGmiGAxe92Qw3y3E937JvOV7YtUYItgp-RWyeN8lA-GAic6o6QRNB4aBC3ivxDrXWTkWr9qFHCD6Ihm2ehAuVXuhG-gA6KIeVyXX3i-Nis3WjOvE4BW6ZBy9-L4FRsAfU5nCtqLo471ZWq_m1D_g1fYI4WZU_4r_txkMDEPJ05uIcSYGVGtTKVCwDvTdDMgEBJpTfFHyWSBHLlpnJ-2vDef7zt4yBLO39Mup67g5rOVw67S03FVSvt_c6JzEyg5BZrLrv75sb5TntshqeNSEyJPE-yTeOOMd7V3xrxeZeMMRMAq_TC-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیارا بلژیک را غافلگیر کرد؛گل اول سنگال
🇧🇪
0️⃣
🏆
1️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/665477" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665476">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پورجمشیدیان، دبیر ستاد ملی تشییع وداع با قائد شهید امت اسلامی:  ۱۲۰ نماینده مجلس عراق با ارسال نامه‌ای، خواستار تشییع پیکر رهبر شهید در عراق شدند  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/665476" target="_blank">📅 23:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665475">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
الجزیره: نیروهای مسلح ایران همچنان توانایی‌های نظامی قابل‌ توجهی دارند
🔹
با وجود مقیاس عظیم بمباران ایران، این کشور همچنان توانایی‌های نظامی قابل‌توجهی در اختیار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/665475" target="_blank">📅 23:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665474">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ca9e801c.mp4?token=alx-RrY962_dHLfRtO3OD2xwljpm4bPrRERNg6dyfHd86rhxdIyzsPiBXCDTg2ZWBFYXl7jbcW1nJzIQ_5AMXKj57HBL2K-oy7sx-9wTlBHix3fTY3G_zjq5pp8Qnl4QTN6dakuMhBzKaTSLH-iBS-JFcfqnAfT3B7HPU73JQpCK7QSITxtuqD36s5KdFcRFCjFIfQeHC3KJhBRaP8dI06S32KcQ_y_2VpTmsojtqbdIecxGtIcB1d-4iN1TwrEYJM4iRJWaKDZML1C7cG-xQtTohrbuFDwysdyLgNZ0_9IFG3axwd3hZT0ib2ZrhgJN4j9DJxCjv-k2UztVdKP8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ca9e801c.mp4?token=alx-RrY962_dHLfRtO3OD2xwljpm4bPrRERNg6dyfHd86rhxdIyzsPiBXCDTg2ZWBFYXl7jbcW1nJzIQ_5AMXKj57HBL2K-oy7sx-9wTlBHix3fTY3G_zjq5pp8Qnl4QTN6dakuMhBzKaTSLH-iBS-JFcfqnAfT3B7HPU73JQpCK7QSITxtuqD36s5KdFcRFCjFIfQeHC3KJhBRaP8dI06S32KcQ_y_2VpTmsojtqbdIecxGtIcB1d-4iN1TwrEYJM4iRJWaKDZML1C7cG-xQtTohrbuFDwysdyLgNZ0_9IFG3axwd3hZT0ib2ZrhgJN4j9DJxCjv-k2UztVdKP8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه دیدنی و کم نظیر از شیرجه غازهای دریایی برای صید ماهی در نیوفاندلند کانادا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/665474" target="_blank">📅 23:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665473">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec50432a5.mp4?token=DZusJWyTr6N1jOxUUi4Q8v37t0YCH0-8IAsssqv5m8fSpbUA251UNaA0TGY3mnTdtwniyZbOwQEblN0NTGRWC0zwYbkQ3HGZp-OhWzFuus_rO21jsoOh29s-kFbU1wjD7NfpO-hQX7bxdPC4evo2go_6zVB2ZRTYqBFIkWefX3H22hTk8LIMXVd5RzNEHaXzsXumnrYCLvAv9Pa4-3xZailG8RdlPm6kaOOlV0PxST_DL_G087vQiTCQ_90QNY8LdbzeyxzpvEFNClM1B0So_6yM-bPnSAhcTCodKAUQ-DOJjE1FbTJb0Yb6eultKSKwAmaI1UAFSl1W69UmqVFWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec50432a5.mp4?token=DZusJWyTr6N1jOxUUi4Q8v37t0YCH0-8IAsssqv5m8fSpbUA251UNaA0TGY3mnTdtwniyZbOwQEblN0NTGRWC0zwYbkQ3HGZp-OhWzFuus_rO21jsoOh29s-kFbU1wjD7NfpO-hQX7bxdPC4evo2go_6zVB2ZRTYqBFIkWefX3H22hTk8LIMXVd5RzNEHaXzsXumnrYCLvAv9Pa4-3xZailG8RdlPm6kaOOlV0PxST_DL_G087vQiTCQ_90QNY8LdbzeyxzpvEFNClM1B0So_6yM-bPnSAhcTCodKAUQ-DOJjE1FbTJb0Yb6eultKSKwAmaI1UAFSl1W69UmqVFWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش شبکه آی۲۴: سیا و موساد در طرح استفاده از نیروهای کرد به عنوان بخشی از تلاش گسترده‌ علیه ایران نقش داشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/665473" target="_blank">📅 23:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665472">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290dd844e9.mp4?token=RT3u-4QTjKSFXBnGk7sCFnYgZE8sHFW5XB60EUyX3jw3Jl3N4TSIMM1w8lri0Sk0dV-2Iwh2SOeT9F-w_JVqyw_4fK82bIdVX9LACpZg7h1lAhDyFhl7XSovGLLbsA5OoQGec6rcYX3m9IRJPtv-mQGxzlVN-GCD9hk5C17tYiW8az0zvfnG-QqsCYus2DIPyuVOvDY8hYfkCaMJqbm7hns8eTqeTrTV7Mcv_vViyyzSZ4h5K-taMtmFMKijoIg5m9HuW5u3x4hfpE1m8lck07sWB-OTDS2y3Ce9C5Rti5NEkBi2YvDBmPVTo_jzNvI5xwNMh7resH5zXC7ZvZzd5oLMD1JQnYgWiPXNOLbUaUh9vrIlbKJtuKWeSNoWYtmh92fEr08sUomAeXevkP4EPZ-pwEl8yzmk9tVpWYdWjvRxxTbGo9-5KibuJIf5hnObZyGsI4-vWy0bdZtkhVPYURvlUQjAr3enCR23IQG-7Xp7LSsYT2zRU_U6OP8-J9d3iHJm7EhsIuwznNs5YnJmC1QQ6PMiCBEl1Utv58KACYtkdrF-EzvAJMQDRK1rXZM9JqcMrROfW1el3XhbrYSaQzuQso0sQDTpJEF4hFOsC_aHNrtFurRuTlXAeeq9BlE-E68J1DjfDRkOBQtjUY_12NRvMLWqZmSxKt1o9nxJQzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290dd844e9.mp4?token=RT3u-4QTjKSFXBnGk7sCFnYgZE8sHFW5XB60EUyX3jw3Jl3N4TSIMM1w8lri0Sk0dV-2Iwh2SOeT9F-w_JVqyw_4fK82bIdVX9LACpZg7h1lAhDyFhl7XSovGLLbsA5OoQGec6rcYX3m9IRJPtv-mQGxzlVN-GCD9hk5C17tYiW8az0zvfnG-QqsCYus2DIPyuVOvDY8hYfkCaMJqbm7hns8eTqeTrTV7Mcv_vViyyzSZ4h5K-taMtmFMKijoIg5m9HuW5u3x4hfpE1m8lck07sWB-OTDS2y3Ce9C5Rti5NEkBi2YvDBmPVTo_jzNvI5xwNMh7resH5zXC7ZvZzd5oLMD1JQnYgWiPXNOLbUaUh9vrIlbKJtuKWeSNoWYtmh92fEr08sUomAeXevkP4EPZ-pwEl8yzmk9tVpWYdWjvRxxTbGo9-5KibuJIf5hnObZyGsI4-vWy0bdZtkhVPYURvlUQjAr3enCR23IQG-7Xp7LSsYT2zRU_U6OP8-J9d3iHJm7EhsIuwznNs5YnJmC1QQ6PMiCBEl1Utv58KACYtkdrF-EzvAJMQDRK1rXZM9JqcMrROfW1el3XhbrYSaQzuQso0sQDTpJEF4hFOsC_aHNrtFurRuTlXAeeq9BlE-E68J1DjfDRkOBQtjUY_12NRvMLWqZmSxKt1o9nxJQzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پورجمشیدیان، دبیر ستاد ملی تشییع وداع با قائد شهید امت اسلامی:  ۱۲۰ نماینده مجلس عراق با ارسال نامه‌ای، خواستار تشییع پیکر رهبر شهید در عراق شدند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/665472" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665471">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سفیر آمریکا برای اجاره زمین فلسطینی جهت احداث سفارت در قدس، تنها یک دلار پرداخت
🔹
رسانه‌های عبری گزارش دادند که مایک هاکابی، سفیر آمریکا در اراضی اشغالی، در ازای اجاره زمینی در شهر قدس به مدت ۹۹ سال جهت ساخت ساختمان سفارت آمریکا، تنها مبلغ یک دلار پرداخت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665471" target="_blank">📅 23:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665470">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اصرار دولتمردان لبنانی به تداوم مذاکرات سازشکارانه با اسرائیل
🔹
نواف سلام،  نخست‌وزیر لبنان گفته لبنان همچنان به‌دنبال  یک چارچوب توجیهی و مقدماتی برای مذاکرات است که مسیر گفت‌وگوها را مشخص می‌کند و هدف آن رسیدن به یک توافق نهایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665470" target="_blank">📅 23:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYIMc8PeYdJcKFD-SOkgTBve65asEJuWCOygh6bM512cBG9qysPvVzA_gdcq6aZ--2GeKLsacYvBWDWcx_tFllmVsd-daMmkaPHO0pRzvTH_8OpiPK7TkkxpWPL4n7ZPIk-e2u_qEKMw5jVoM-jN46hOOSPhJVDS-p2xEpcUOWvDqiYn9RLzs_ZhkVRrOXHu96AimFZQJ8GptTFRic4XRQTW0CL13E2_UaSbFqlJPOx8_QvWHPsCzKb3AHH99b5tLc8qwPoHFRIUKAAvb9XUf4vtfo0_c1narjOyI6mJmE7FJinQP_rka4rU4xL7MLM-dpi0WGGZxg3j-sdZtl6LsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ۸۰٪ تخفیف خرید حضوری با اسنپ‌پی در ۴ قسط
!
🛍️
💥
🏊‍♀️
از استخر و باشگاه‌
🛍️
تا فروشگاه‌های متنوع
💆‍♀️
کلینیک‌های زیبایی، سالن آرایشی و…
با خرید حضوری اسنپ‌پی می‌تونی برای کلی برنامه‌ی حال‌خوب‌کنِ تابستونی
"تا ۸۰٪ تخفیف"
بگیری و هزینه‌ش رو
۴قسطه
پرداخت کنی؛ هم به‌صرفه‌ست، هم پرداختش آسونه.
😎
💙
✅
انتخاب از بین
۱۰,۰۰۰ فروشگاه معتبر
📱
پرداخت راحت، تنها
با اسکن یک بارکد
📍
مسیریابی آسان
تا نزدیک‌ترین شعبه
فرصت محدوده، از تخفیف‌های داغ جا نمونی:
🔥
👇
https://l.snpy.ir/8kk7y
https://l.snpy.ir/8kk7y
https://l.snpy.ir/8kk7y</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/665469" target="_blank">📅 23:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665468">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5929c3039.mp4?token=E2pEBVd1-AssPAxCKt5KAJ3aVUHj583gtdElbZbmKvIh0l6oIBOj8kY3dzTwMiOHJhLounNQFhAipgINATtaN3bnxhTjLRXDjT-EGR-cPo8mvb6ChI_a4V3MKwIp5nIVm-Tp3x17jz9aa626G7YgJPa8Rolia1qnNhkRtsRovhh1A2bzNwceb56pkdo8ry_KorwwgEJulTYbvSzYjtYHNOsbnOvkd5bUopkOtZXwWc3z54v9ZV8RKJEfK8rZZ5ExObgLp8efHKYc9g6YAPKtxt0XDKsB5LoCCuyO9eY3noGNsUrPMiUHVlNZIgxbeoUcSLrN_s_1oRYY4oQv639h8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5929c3039.mp4?token=E2pEBVd1-AssPAxCKt5KAJ3aVUHj583gtdElbZbmKvIh0l6oIBOj8kY3dzTwMiOHJhLounNQFhAipgINATtaN3bnxhTjLRXDjT-EGR-cPo8mvb6ChI_a4V3MKwIp5nIVm-Tp3x17jz9aa626G7YgJPa8Rolia1qnNhkRtsRovhh1A2bzNwceb56pkdo8ry_KorwwgEJulTYbvSzYjtYHNOsbnOvkd5bUopkOtZXwWc3z54v9ZV8RKJEfK8rZZ5ExObgLp8efHKYc9g6YAPKtxt0XDKsB5LoCCuyO9eY3noGNsUrPMiUHVlNZIgxbeoUcSLrN_s_1oRYY4oQv639h8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
🔹
چین در تلاش برای تصاحب آبراه پاناماست.
🔹
ما اجازه نمی‌دهیم این اتفاق بیافتد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/665468" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665467">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f4e163cf.mp4?token=gPnrTGDQ8E0W_sQwNwqssiGBRQyp7T6ZKlXnP81ub5pKlM_ZZbyUQ2-voC3IFTUGuIqFtGhcOvgLmqlmjWLOUIsexjMLtsNj0G8XRH8140qvQ63lzRR2DTDelUR01_rCymwpz5A36bqHwPJIKNg8ng6YMtwPbKR9xS2RTXrGQohdGjoNEKuAHxrHl_tECPWLDj37S6sNFq5exkOGJiWTI8UlKEC70ocEWr0DBWezbjGoIp1IrcjkvFC0DqDuvw9KqsBXmMOaxIyV6qWnpsCLPaFaY5ncNPzPB1ooI4DZbJWK1TGLR-f_VN2S2yeVDDu3eeWDgMNCWmsb_K45qb9BBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f4e163cf.mp4?token=gPnrTGDQ8E0W_sQwNwqssiGBRQyp7T6ZKlXnP81ub5pKlM_ZZbyUQ2-voC3IFTUGuIqFtGhcOvgLmqlmjWLOUIsexjMLtsNj0G8XRH8140qvQ63lzRR2DTDelUR01_rCymwpz5A36bqHwPJIKNg8ng6YMtwPbKR9xS2RTXrGQohdGjoNEKuAHxrHl_tECPWLDj37S6sNFq5exkOGJiWTI8UlKEC70ocEWr0DBWezbjGoIp1IrcjkvFC0DqDuvw9KqsBXmMOaxIyV6qWnpsCLPaFaY5ncNPzPB1ooI4DZbJWK1TGLR-f_VN2S2yeVDDu3eeWDgMNCWmsb_K45qb9BBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری جالب از اسکورت رئیس‌جمهور آمریکا با اسب در داکوتای شمالی
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665467" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665466">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پیش‌بینی عجیب تحلیلگر مشهور چینی درباره زمان حمله زمینی آمریکا به ایران
اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3226986</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/665466" target="_blank">📅 23:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665462">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H78sN1BNFFAyi8Z7r3W3IWjF3znU__nhfKXXWQiOnYnEuD4ZzanpnOiDrbx9ix9dsV-RqEPuzSq5QXe57ynoQfdt47zSPjCLUb1ZSeLXVnSsu91bAlFgleYIs0Yw8uPzPpOfGWzBo65v3CQztr5LdrTWEWWdJX3z8rRgHEaXXHJSfAJo9ZuK0LHznV-oF1nLHiGcs1XXreVZLUty8PnnwrRQRLie180vsuJmtOAiFmTRyRO121g54IZVEzpxYVAk6b20BTKjqjGBpE0Bk_-Jgh1U8ggK_3RHrEkeXYyK2GWS6m6G-ZP361lVmpdl4D1sLbkop3_38hD1EyAkAMf28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLWeXFeXi_ucxSrl6GjT7i2JGYwpgpSbbmBRJhH6gE7l0PHwU35ssGd8D0JvazkEHdJPHv_ce46p9pZjRuS1ZDodosSm5LcAS22z-GBiTxDtGwfxoYtaKdjJ1BY9iWMhdaypCDxF38_4iADDKvxgn96gvLuPBrahNR7GN53j3EjXKoIbaCVj7eTM_AzSmWTC2bqCq-sqNX6j3StFbhyGVKkEgd9FJ8vB5xmoEaJn2VlcsI1cg47NYh0Btp4GcJ5-VwvJjFIMeYuANpo7YdGGfY_nfxsFgQnM11Rz_1mt0qtD63xK4rdBplXajKSOrptyTQqmnzguqHGSMEMPb6r_2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532830d055.mp4?token=ZFVIAAzgobi28CDXzGXBRWP-_X7WoJkt9SF3W1Ol1HxnZS0SUuwdasuyueB_E_tVhEJA62wcOqD0f16lOdGl-qvwtRWw7a_4aadk4_lelUhHl3D_SV-z7ZQ2tZTr7ndP1a3y2dj7G3CzuQFVkrKkKb5M3rkW9HwNjzNPgUYCtJwLoKW_y5riggcQlu9t8A_05v1wAl0BEUfz6iM1ht4sm4ZSYErMk9BV9P-_uDfQQD9uIXlMUGZgkg9st5cLiYu9X6zXqQgIq_RpRG_WeH8Wb_8ViBpwLuVu_KgfUOBdqXegLXa8SnWIDzbjNcF6dieuDtCuWWqzpWz1RQrSHNN8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532830d055.mp4?token=ZFVIAAzgobi28CDXzGXBRWP-_X7WoJkt9SF3W1Ol1HxnZS0SUuwdasuyueB_E_tVhEJA62wcOqD0f16lOdGl-qvwtRWw7a_4aadk4_lelUhHl3D_SV-z7ZQ2tZTr7ndP1a3y2dj7G3CzuQFVkrKkKb5M3rkW9HwNjzNPgUYCtJwLoKW_y5riggcQlu9t8A_05v1wAl0BEUfz6iM1ht4sm4ZSYErMk9BV9P-_uDfQQD9uIXlMUGZgkg9st5cLiYu9X6zXqQgIq_RpRG_WeH8Wb_8ViBpwLuVu_KgfUOBdqXegLXa8SnWIDzbjNcF6dieuDtCuWWqzpWz1RQrSHNN8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالا رفتن از آنتن برج امپایر استیت نیویورک برای خواستگاری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665462" target="_blank">📅 23:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
گروه کشتیرانی فرانسه: بازگشت به شرایط عادی در تنگه هرمز ماه‌ها طول می‌کشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/665461" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
این چند اتفاق سرنوشت ایران و منطقه را مشخص می کند/ شبه کودتا در عراق مقدمه «سونامی» است؟
👇
khabarfoori.com/fa/tiny/news-3227179
🔹
حجاب خاص دیپلمات ایرانی در ژنو
👇
khabarfoori.com/fa/tiny/news-3227227
🔹
تحلیلگر مشهور چینی: آمریکا در بازه زمانی آذر تا اسفند به ایران‌ حمله زمینی خواهد کرد
👇
khabarfoori.com/fa/tiny/news-3226986
🔹
۳ سناریوی دلار، طلا و سکه تا پایان امسال؛ طلای ۲۲ میلیون تومانی در دسترس است
👇
khabarfoori.com/fa/tiny/news-3227159
🔹
شوک به فوتبال ایتالیا | مدافع تیم ملی به فحشای کودکان متهم شد
👇
khabarfoori.com/fa/tiny/news-3227174
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/665460" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b4075f2b.mp4?token=qnzrAZayXNwACWhWRFyT40YHCWz0hJkPk0bX3katAsp51l030LwTHzhO10lRD5CAfVb--C81RHpsw5h0kwGIQEpucA4vBi6aVZj1YZR8zLUK8FLqolL5XW3wRfou3jwk0NHKAT9UzHd9YBLs3nSkn9AcfKBS4KD3-jfIweLWD0ybeEZS7b6N3EXI58RYylme6o3GlE-lMf6gzbNQgL_3YFQ5BM2BLOtCLZ-UGro_JHqKJ0TbS-f3rNVceAYQw3-u4I0RFqVY4_xov3n4er67DHHOMY5xU7ReVdh6HEFNWnsft02xqFGN9XTztwwAiC9D7t8sDZnKa86mWta5EGWEDBYPBQIPL57WbAYBUCpmpEhgQ6V4nW-SfgZ4MOQ1F8XRXyJgQR8xY_CqS9WFgq6Mpf8MFtfs_77aZQSNvF14RkLxISWd0Xq4_Z_VY_38g_mMHzLZevzMI9pryeBYFcHgQaUJemkyM6m0NURLnN-h-9dOA4mAz84RW_oypqQLiTMEMwgNzGnVtdFJ9KabNVpsBdkVATDDLr7XCuCEUOHTiCAkAZWzvrAGeoWFHi_INQ7vpofniTUfqABUyU6ul0Qzgc8j2dT8M33TgAl51WWv3knxTB6BGhS90kRO_MI-Mpiw11oKzuyGxoBchC-gHGa_OL4ElRsir0hKMZNBrdnLWUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b4075f2b.mp4?token=qnzrAZayXNwACWhWRFyT40YHCWz0hJkPk0bX3katAsp51l030LwTHzhO10lRD5CAfVb--C81RHpsw5h0kwGIQEpucA4vBi6aVZj1YZR8zLUK8FLqolL5XW3wRfou3jwk0NHKAT9UzHd9YBLs3nSkn9AcfKBS4KD3-jfIweLWD0ybeEZS7b6N3EXI58RYylme6o3GlE-lMf6gzbNQgL_3YFQ5BM2BLOtCLZ-UGro_JHqKJ0TbS-f3rNVceAYQw3-u4I0RFqVY4_xov3n4er67DHHOMY5xU7ReVdh6HEFNWnsft02xqFGN9XTztwwAiC9D7t8sDZnKa86mWta5EGWEDBYPBQIPL57WbAYBUCpmpEhgQ6V4nW-SfgZ4MOQ1F8XRXyJgQR8xY_CqS9WFgq6Mpf8MFtfs_77aZQSNvF14RkLxISWd0Xq4_Z_VY_38g_mMHzLZevzMI9pryeBYFcHgQaUJemkyM6m0NURLnN-h-9dOA4mAz84RW_oypqQLiTMEMwgNzGnVtdFJ9KabNVpsBdkVATDDLr7XCuCEUOHTiCAkAZWzvrAGeoWFHi_INQ7vpofniTUfqABUyU6ul0Qzgc8j2dT8M33TgAl51WWv3knxTB6BGhS90kRO_MI-Mpiw11oKzuyGxoBchC-gHGa_OL4ElRsir0hKMZNBrdnLWUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
🔹
چین در تلاش برای تصاحب آبراه پاناماست.
🔹
ما اجازه نمی‌دهیم این اتفاق بیافتد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/665459" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRiO1cfjll_6QvftZWuPNiMETgIsBjfGlyWW1x7fYGArE0B0ubyqaSrhQV_IfEzESYADagql4nA4rW6FMwoc2S9r7wUEw3XXVws1827rPXMJSunyiPXIN3yqnvigxJoU4VyL4kTGOSmajWbrAZZo_zjuYFXeBY37a6dx783G1KSeQ8iJ9dMDPSdM-GxX2OlXu6_HMSYwPoXRelps3YjzrEIPtTFKfHtEC3HkrrwSlgcI-FzIqJj9yXpUL1BPjsedDH2W5NxOPtqhxQ2m_cyFJ5xgRwck06IkHkefv1dkXRetCDODFO4Iu8oIR1hM4jxqlBUjZaCQSgs0J0SuItZVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه استرس و اضطراب شدیدی داشتین، این خوراکی‌ها رو بخورین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665458" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنان مهدی رسولی: ما از خون‌خواهی رهبر شهید انقلاب کوتاه نمی‌آییم و از ترامپ حتما انتقام می‌گیریم
🔹
باید به گونه‌ای انتقام بگیریم که دیگر کسی جرات نکند رهبر ما را ترور کند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/665457" target="_blank">📅 23:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24616fdcb5.mp4?token=qTtaCrPJAe37FOsMpxqIuDsSo1c5ze055ZKo6pIjggf0h9pYdl4nMFQzQbCOxnufzE0ycx-uocJDkiLvolH-JhKLb4q34HMG8zGsAqQBgwrEXG0RSPOr5_Rnz1a0_q6FbGfxBkPFW-ctfAb4CoUB9MdCwbO4q7auvW2B13JShHcroa_Kf3aHQpfWiJ4OAZ5otRwwwYDV7iYMc9Urk9ziJs4hpN9jmLyzErxFETl1mZnrKo2FdHSzHHERS72-ZHpKHptSdJTAF8S60jUvtgNx2R4tuwwco9qN86ccBrWtwrIFoR35Lqib7glFrlJ36KT-dB06lfea025Cs6i2WRW3Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24616fdcb5.mp4?token=qTtaCrPJAe37FOsMpxqIuDsSo1c5ze055ZKo6pIjggf0h9pYdl4nMFQzQbCOxnufzE0ycx-uocJDkiLvolH-JhKLb4q34HMG8zGsAqQBgwrEXG0RSPOr5_Rnz1a0_q6FbGfxBkPFW-ctfAb4CoUB9MdCwbO4q7auvW2B13JShHcroa_Kf3aHQpfWiJ4OAZ5otRwwwYDV7iYMc9Urk9ziJs4hpN9jmLyzErxFETl1mZnrKo2FdHSzHHERS72-ZHpKHptSdJTAF8S60jUvtgNx2R4tuwwco9qN86ccBrWtwrIFoR35Lqib7glFrlJ36KT-dB06lfea025Cs6i2WRW3Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ امتیازی بیشتر از دسترسی‌هایی که شورای عالی امنیت ملی تعیین کرده، نمی‌دهیم
🔹
طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔹
در حال حاضر، آن‌ها فقط در دو مورد حق دسترسی دارند؛ یکی نیروگاه بوشهر و دیگری…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665456" target="_blank">📅 23:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b2636460.mp4?token=Qw051YzZf1UarDsqzsyI_KISOWwxU0d1-HbQee204VFcPyy9BccZu4r5epgAOyh5frsiIRuKBFinEbpOkG_fEnKkDs_GusHGK2G_1auK0QhzWytuwQ0gmGueUhP7XXDb5Wxk1V-x8K-Nt9BGCfy_mzMOLEVAP3b26GFQKF1odHxAT37XM0lkc4YZVpR5nerDHlYSS4TRKgqPDGS99z8czLkSj1WsoxTb1LQdVFnEtwY6rnYf6ZS_jlfLkrGnilPN30-asqO3fAf-B7jvUx-Ejpe6hHLE8K7KiwMJ7sfRVjk03k5Xgxz8o-CdGBcw3xrcvMB5gZhlnHc5CG45Ap7tKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b2636460.mp4?token=Qw051YzZf1UarDsqzsyI_KISOWwxU0d1-HbQee204VFcPyy9BccZu4r5epgAOyh5frsiIRuKBFinEbpOkG_fEnKkDs_GusHGK2G_1auK0QhzWytuwQ0gmGueUhP7XXDb5Wxk1V-x8K-Nt9BGCfy_mzMOLEVAP3b26GFQKF1odHxAT37XM0lkc4YZVpR5nerDHlYSS4TRKgqPDGS99z8czLkSj1WsoxTb1LQdVFnEtwY6rnYf6ZS_jlfLkrGnilPN30-asqO3fAf-B7jvUx-Ejpe6hHLE8K7KiwMJ7sfRVjk03k5Xgxz8o-CdGBcw3xrcvMB5gZhlnHc5CG45Ap7tKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: روز بعد از امضا توافق در سوئیس، اسرائیل ۳۰۰ بمباران در لبنان انجام می‌دهد که ۲۰۰ نفر شهید می‌شوند/این در حالی است که تاکید ما آتش‌بس در تمام جبهه مقاومت بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/665455" target="_blank">📅 23:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند  رئیس هیأت مذاکره‌کننده:
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665454" target="_blank">📅 23:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCDCFxjvq6MWuBN2nwByoQtwW74bJy0BdvlkLIlw26Yh1AkdOhhKfoknErc3DIfOmi51Dmcc0GjEcDbXmv3-xUs3vzD1vMJ8xnfAOStev7PlVrxQ630_0Mu8Hij8xwU_X1PB4Ddgb94MxfZO0v79t5vukQEDBs7w-qxFAdasxgWSwaKN9785bnlTwp1BfO4gqt-yxI-DEhLAF0frhkRGc4hPPSnx1e8mXdKdUc1uoImt-xI6uyt6Y547EsCfLX7Y4inUDo9L7_2F6BYV0kCY-R60VjFJA9WwtuUIuV0kaS8R08ahnWghHJa_vSVymCMz-Gm-4gqXmcSp28T_D4WqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/665453" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=E1vPtFbUHn8mphWg2cJcuD0nb5vOBmfnxexxc8aL5OvAOmC0M1Eewv3HZn-qZPLFNgmy9FwXzx9-VZ8YMC9mitMaTdMrAPg6K6l02twW0x-i9LXFHwObL7xQhM0mNMyS4F4vTuLujoABPgZIopJgqozI9x0gvQd-ee_HM0lQvLgot-0f2LMTZFiMhzj3cmxWHxdod4RILwZNnSHV6Om45PMp3cvSZhH0d27x2ug1aC_hdU1eXBR8CKPlixYQA7ChLHyPOpZdd4hMnGK9bl6vUs0OMD2CR_MhL8Y7RhuaAabgXGSXiR4JMKOkbdBvVW0CEhQTC2wgKckdHyVD9h60FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=E1vPtFbUHn8mphWg2cJcuD0nb5vOBmfnxexxc8aL5OvAOmC0M1Eewv3HZn-qZPLFNgmy9FwXzx9-VZ8YMC9mitMaTdMrAPg6K6l02twW0x-i9LXFHwObL7xQhM0mNMyS4F4vTuLujoABPgZIopJgqozI9x0gvQd-ee_HM0lQvLgot-0f2LMTZFiMhzj3cmxWHxdod4RILwZNnSHV6Om45PMp3cvSZhH0d27x2ug1aC_hdU1eXBR8CKPlixYQA7ChLHyPOpZdd4hMnGK9bl6vUs0OMD2CR_MhL8Y7RhuaAabgXGSXiR4JMKOkbdBvVW0CEhQTC2wgKckdHyVD9h60FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد اسکان شهرداری تهران در برنامه پرچمدار: در تمام بوستان‌های تهران برای اسکان زائران مراسم تشییع رهبر شهید، امکانات مهیا می‌شود
🔹
هلال‌احمر قرار است در فضاهای باز شهر تهران مثل پارک‌ها، برای ۲ میلیون نفر چادر بزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/665452" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قالیباف: اگر به سوئیس نمی رفتم و برخی شروط محقق نمی‌شد آیا نمی‌گفتند قالیباف شروط چه شد؟ / کسانی هستند که نه در دیپلماسی به کشور کمک می‌کنند و نه در جنگ  اما من ایستاده‌ام تا هم بجنگم و هم دیپلماسی را انجام دهم/ بیشتر از این آزار ندهید و حرف‌های ترامپ را…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/665451" target="_blank">📅 23:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55053dff1a.mp4?token=A7eM8HgsqfqFEk-GDkOsgmuWhNlW_huiLE7PI1eek73NrC_OZirL3NdOlph1gwUYGzb5c8O_tKD5kl1f8r-vi18-Kvo0n5PCh-q9M66rmhFz2lsXYKCOjRyf_7_EUT1HU8UbRtfPdRaw8Sj5J6Dpj72xjZ8GuROl3G8Uac-VrjCzlta4r2TOKmTtAMBUEZDeNsl9P831GrR0gI4-MavKE_v0fxHEQzekPmVm0nEcFjG7hO3w0yxSxSXJVyZ6B4qePGRAiV5ASWDKCDuR7Pa0ZR4cp16h5T4mtEbvMzyjcVwKy8F9YJDZT9dmRHOE1aSBCEw7mRYoHfOOGKsUIB2d6jshYqeN_z9NavkvD08w127-CwuEb__I5qqfQpKgCueurpORLar-5_cwdnTDSAPG69fE5d_jiaKrCFdDNi5ZFfZugcRPiuAou4VTLvWlfcdwTPAXOwqRHOX-AQbSo5ralMRbaHEdRUPg4N-mBBkVTwUvT06SaXDn9a1Vijpj4FjXyDAsPH-OOlkpxz9GQXiJxhqF4PFyL-bErrtIpFyG5PDFPpVxnQ8IN3i5TJuASc2pwPeRjYXKqVrSIGaoJfCUIfBtIrV1btJpAsH3Dj5eqJqdPigbiuEDuEvfH9ZlR4NHM2QJCdKq5b4At5JrAT8wyY6gd41huobKdx8w2j3gF3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55053dff1a.mp4?token=A7eM8HgsqfqFEk-GDkOsgmuWhNlW_huiLE7PI1eek73NrC_OZirL3NdOlph1gwUYGzb5c8O_tKD5kl1f8r-vi18-Kvo0n5PCh-q9M66rmhFz2lsXYKCOjRyf_7_EUT1HU8UbRtfPdRaw8Sj5J6Dpj72xjZ8GuROl3G8Uac-VrjCzlta4r2TOKmTtAMBUEZDeNsl9P831GrR0gI4-MavKE_v0fxHEQzekPmVm0nEcFjG7hO3w0yxSxSXJVyZ6B4qePGRAiV5ASWDKCDuR7Pa0ZR4cp16h5T4mtEbvMzyjcVwKy8F9YJDZT9dmRHOE1aSBCEw7mRYoHfOOGKsUIB2d6jshYqeN_z9NavkvD08w127-CwuEb__I5qqfQpKgCueurpORLar-5_cwdnTDSAPG69fE5d_jiaKrCFdDNi5ZFfZugcRPiuAou4VTLvWlfcdwTPAXOwqRHOX-AQbSo5ralMRbaHEdRUPg4N-mBBkVTwUvT06SaXDn9a1Vijpj4FjXyDAsPH-OOlkpxz9GQXiJxhqF4PFyL-bErrtIpFyG5PDFPpVxnQ8IN3i5TJuASc2pwPeRjYXKqVrSIGaoJfCUIfBtIrV1btJpAsH3Dj5eqJqdPigbiuEDuEvfH9ZlR4NHM2QJCdKq5b4At5JrAT8wyY6gd41huobKdx8w2j3gF3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در خصوص دسترسی و بازرسی آژانس به چیزی که از قبل متعهد شدیم، هنوز به همان پایبندیم اتفاق جدیدی رخ نداده
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665450" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3306a1a6.mp4?token=r_tnRO9FcbvidymTA4wuPsAfFVuse8rksFddwiu74O6yz95Y-dqWCM7KcfpIAevSHI5wrF0dLik_f6Rzv2HkgQvO1XoiMGcNKThtdkOHZSlac2KyyriHSMpWE8FMDfEDqoiHtYKQZ2G-QF_LrD54Dze-pOZcoCn6raUx8vvnnrkZtXfl-gk8t98VSOf8SmL0Qkqo7g3bbmb-ytn0Bm5Wag7Ji09UE8vivgYcec2GGelpEULHwhVAFtDzks5MhJ1OuooJqA_qx42GXcmLLYq5dGfd78uMBnDVEzTyb00RUQc_AptGgXqM_IbYsnTlR3GGAQVQ3kaDpxWrisTDKnS3q1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3306a1a6.mp4?token=r_tnRO9FcbvidymTA4wuPsAfFVuse8rksFddwiu74O6yz95Y-dqWCM7KcfpIAevSHI5wrF0dLik_f6Rzv2HkgQvO1XoiMGcNKThtdkOHZSlac2KyyriHSMpWE8FMDfEDqoiHtYKQZ2G-QF_LrD54Dze-pOZcoCn6raUx8vvnnrkZtXfl-gk8t98VSOf8SmL0Qkqo7g3bbmb-ytn0Bm5Wag7Ji09UE8vivgYcec2GGelpEULHwhVAFtDzks5MhJ1OuooJqA_qx42GXcmLLYq5dGfd78uMBnDVEzTyb00RUQc_AptGgXqM_IbYsnTlR3GGAQVQ3kaDpxWrisTDKnS3q1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: ما به مذاکرات اسلام‌آباد رفتیم در حالی که اسرائیل اعلام کرد از حملاتش عقب نشینی نخواهد کرد/ از همان روز ۱۰۰۰ شهید در لبنان داشته‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/665449" target="_blank">📅 23:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
قالیباف: بحث دسترسی و بازرسی آژانس که این روزها مطرح شده کذب است
🔹
به هیچ عنوان دسترسی در سایت‌هایی که بمباران شده نمی‌دهیم، این قانون است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665448" target="_blank">📅 23:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
قالیباف: اگر ضعیف باشیم، ذلیل می‌شویم؛ این زیبنده ایران ما نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665447" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
قالیباف در گفتگوی تلویزیونی: بعضی نه در جنگ کمک می‌کنند نه در دیپلماسی؛ مردم را اذیت نکنید؛ با شعار، خونخواهی امام شهید محقق نمی‌شود این دشمن فقط زبان قدرت می‌فهمد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/665446" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665445">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
قالیباف در گفتگوی تلویزیونی: بعضی نه در جنگ کمک می‌کنند نه در دیپلماسی؛ مردم را اذیت نکنید؛ با شعار، خونخواهی امام شهید محقق نمی‌شود این دشمن فقط زبان قدرت می‌فهمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/665445" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665444">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
همه مسیرهای نفوذ و خرابکاری مسدود است/ حضور نمایندگان بیش از ۱۰۰ کشور در تشییع رهبر شهید  حجت‌الاسلام نیک‌بین، نماینده مجلس شورای اسلامی، در ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری:
🔹
تشییع رهبر شهید یک رفراندوم است. پیام اصلی هر کسی که در این تشییع…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665444" target="_blank">📅 22:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665443">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a3d1da36.mp4?token=o6HsCmgHavcKbot2tSxVTl2P88DfOgVLwbzgDSP9d2eZZvWJEuv8Vi1TkCAZ12LoFRW0O8lsA0XTvcjGY4qQWSROnmuO_XWaKqZNsT_inA9GZ8BiQIdAYfUFxknzxlPDzy1VSzE7x0325KMGqJy_BMp4VZDtM0qNlrkYTHh4E2VEOFaIMg5F5UTIRFK00PWcQgdu_3UESomw_dW8ip4s5Lz8KxsMQQl63MOXWX4FwXZQ65_17TmhWOjmIJ4zly06aT8X6CVVijTWbX4c45FCnVBHLIuv8NGjAp7M3oo_FMu2bZn8BKKkZp60iNMPZtb97Z1jZcoz0qEbGK1k49a1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a3d1da36.mp4?token=o6HsCmgHavcKbot2tSxVTl2P88DfOgVLwbzgDSP9d2eZZvWJEuv8Vi1TkCAZ12LoFRW0O8lsA0XTvcjGY4qQWSROnmuO_XWaKqZNsT_inA9GZ8BiQIdAYfUFxknzxlPDzy1VSzE7x0325KMGqJy_BMp4VZDtM0qNlrkYTHh4E2VEOFaIMg5F5UTIRFK00PWcQgdu_3UESomw_dW8ip4s5Lz8KxsMQQl63MOXWX4FwXZQ65_17TmhWOjmIJ4zly06aT8X6CVVijTWbX4c45FCnVBHLIuv8NGjAp7M3oo_FMu2bZn8BKKkZp60iNMPZtb97Z1jZcoz0qEbGK1k49a1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: حمله به دکل مخابراتی در سیریک قابل تسری در کشور است/ از حمله به دکل شروع می‌شود و به پایتخت می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/665443" target="_blank">📅 22:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665442">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0YUHxsO3f2pz_dKZ6y9ywkH2_MUeA3xCTzlBRdkZXCKqTiruL3lcxyJUdxXHqvzXxWg44zbm4dFPndztCHWzNb5YKyKk-m9Trl8DD5TD-eVPFz0-baiW2mFU5txcGjGSITK2XLlQxAtHDFkCh5OUAyNtollrxZ7kwafPgwd0GCi_4rbPbAQls8i0H-OixveC0Zys_s9Ej2xqt0ZtuvqyHiEMpzEAwdnVcTw9zZnevd8pH6M2KAh8_lzd9ZGEH9ZSQ6Vyka4yNSXF7EwMF2Vk1CStBZlOMLIhLn6En_HW0AM6we425c6yp78wimIjZd2XknLnKTzk0sLacFjKM6Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدون تخفیف
🔹
صحبت‌های محمدباقر قالیباف در صداوسیما که به صورت ناقص پخش شد، واکنش‌های زیادی را در پی داشت. نکته قابل تامل صحبت‌های وی، رفع تحریم‌های نفتی و فروش آن است که نشان می‌دهدنفت حالا مثل قبل با تخفیف فروخته نمی‌شود. قالیباف گفت که از روزی که محاصره دریایی برداشته شده، بیش از ۴۰ میلیون بشکه نفت صادر کردیم. طبق اعلام صداوسیما، ادامه صحبت‌های رییس هیئت مذاکره کننده، امشب پخش خواهد شد.
🔹
هفتصدوهشتادوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665442" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665441">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e96685e8d.mp4?token=HnHFeYEH0wMOHpQyc0vhgyuc17z_aseIuqCaqbvCCU9NBwxKylTbI2wHylG-xAP_wXIXkLdlWHyThlrdXEsbv7LhN72jmz7T6uM1dnuDMkE5-7Yqd-wT4Tg36Fa0I3STNV1CQkq-W6sYFzeRJeAodZvjHO1Eah4AzIkSn4GmAjCO_v-W2d9XvonBU3uqQ9odNsknbw3CYISagxfNE9FTsYvNgxEV7A7KGWAmrzPlhbawND_fHddYUPeVrofwqvUQL9uzyVkV9UT4wJ21PGEPh55oy4xMdBdetvfROLVun0qZI1qMcd1KfpHGhNhLmv7KsxtpKXTM7CGHeK97Ofp_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e96685e8d.mp4?token=HnHFeYEH0wMOHpQyc0vhgyuc17z_aseIuqCaqbvCCU9NBwxKylTbI2wHylG-xAP_wXIXkLdlWHyThlrdXEsbv7LhN72jmz7T6uM1dnuDMkE5-7Yqd-wT4Tg36Fa0I3STNV1CQkq-W6sYFzeRJeAodZvjHO1Eah4AzIkSn4GmAjCO_v-W2d9XvonBU3uqQ9odNsknbw3CYISagxfNE9FTsYvNgxEV7A7KGWAmrzPlhbawND_fHddYUPeVrofwqvUQL9uzyVkV9UT4wJ21PGEPh55oy4xMdBdetvfROLVun0qZI1qMcd1KfpHGhNhLmv7KsxtpKXTM7CGHeK97Ofp_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه مسیرهای نفوذ و خرابکاری مسدود است/ حضور نمایندگان بیش از ۱۰۰ کشور در تشییع رهبر شهید
حجت‌الاسلام نیک‌بین، نماینده مجلس شورای اسلامی، در ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری:
🔹
تشییع رهبر شهید یک رفراندوم است. پیام اصلی هر کسی که در این تشییع جنازه حضور پیدا می‌کند، مبارزه است. ما ایرانی‌تر از این آدم در ایران نداشتیم
🔹
خیلی‌ها می‌گفتند که مسئولان در جنگ فرار می‌کنند، اما من جایی ندیدم که کسی از مسئولان چنین کاری کند. این‌ها همه نتیجه رهبری شهید خامنه‌ای است.
🔹
پیش‌بینی می‌شود در تهران بالغ بر ۲۰ و در مشهد ۱۵ میلیون نفر در این رویداد حضور یابند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/665441" target="_blank">📅 22:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665440">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
افشای ارسال محموله مشکوک اطلاعاتی اسرائیل به سومالی
🔹
منابع راهبردی منطقه‌ای به شبکه المیادین خبر دادند که یک محموله مشکوک با اهداف جاسوسی و نظامی از مبدأ اسرائیل به سومالی ارسال شده است.
🔹
این محموله به وزن ۱۰۰۰ کیلوگرم در تاریخ ۲۱ ژوئن از تل‌آویو و از مسیر نایروبی وارد موگادیشو شده است.
🔹
اطلاعات تأیید شده حاکی از آن است که محموله مذکور، یک سامانه ارتباطی پیشرفته با اهداف اطلاعاتی-نظامی است.
🔹
این محموله به‌ظاهر تحت نام «دفتر سازمان ملل متحد» ارسال و توسط دفتر این سازمان در موگادیشو دریافت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/665440" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665439">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5abcf2028.mp4?token=iw2KmYXNy83e1xxDZAggqEwbSVg28k9BrtdWsdcVPyb0OGeB-hzAArrtOKCtMeUNw5aKqB02_8LvB5q7x4yAHpULRpDpkSSpJl7jP-q_bbHtnp7KM7hp7YfiCD7UuWaBVsMBuHk0LldmUVzm1BwGj73F7RabCStw2WOdeO1LDgztIz3gsjNC0odo5WH9hVFpTWcScymDTHQ5e3N4BATRC_A2mco4ycrgTt5Y8Ymla4KASQH0hQbMTtWSNg44iqg9nmOfBbdtQwh6kj3p6GMnD1vH9_yhAKkOG1dX__h4blnMItvhzXCg7uQcIKWXoq7D6ydUsNVZ48587hpWqxf1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5abcf2028.mp4?token=iw2KmYXNy83e1xxDZAggqEwbSVg28k9BrtdWsdcVPyb0OGeB-hzAArrtOKCtMeUNw5aKqB02_8LvB5q7x4yAHpULRpDpkSSpJl7jP-q_bbHtnp7KM7hp7YfiCD7UuWaBVsMBuHk0LldmUVzm1BwGj73F7RabCStw2WOdeO1LDgztIz3gsjNC0odo5WH9hVFpTWcScymDTHQ5e3N4BATRC_A2mco4ycrgTt5Y8Ymla4KASQH0hQbMTtWSNg44iqg9nmOfBbdtQwh6kj3p6GMnD1vH9_yhAKkOG1dX__h4blnMItvhzXCg7uQcIKWXoq7D6ydUsNVZ48587hpWqxf1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ملی پوشان فوتبال ایران به فرودگاه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665439" target="_blank">📅 22:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665438">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رویترز: پوتین آموزش محرمانه نیروهای روسی در چین را تایید کرده است
🔹
رویترز بر اساس اسناد و اظهارات دو مقام اروپایی اعلام کرد که آموزش محرمانه نیروهای نظامی روسیه در چین در سال گذشته با تایید مستقیم رئیس‌جمهور روسیه از سوی وزیر دفاع این کشور انجام شده و دست‌کم چهار ژنرال روس و چینی به طور مستقیم در آن مشارکت داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665438" target="_blank">📅 22:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665434">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU758CJ3Uv81P8PqiyAqinwxzZCkFxvp4ocIqI1dip8E0HRPHccKFboTquy9sSq_qsG8xducZkiWPMU-5C7j0cazFiez7mbiDWuVwPg4nnDY9mVy9B0xUEPoY314QM8KCR45zgQYxjRPAXgnrcWq5eeKWj-OyCwqVmRJ2YHyyfEKBlrrMgniwe-nyOxa_Am7P8PWUv14J4ynDMpOh9Y00Ig7tRL4fsBjtp384RKLsiVck-q9nSR40EtC32SXs4k1nhAcPzIQMAJlnbui7e_bzlHIpTbaNDJzoRLpNI9LPPNyRapYVRCOR2kABOMVVruek4eb2f6-fCUuZ1KpkBk0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEY96akUPEIqlpxkwm2Y7d6_NkX_2izySqlStI1calVlbQBhfR5L6SLKmmFFzg86gOjlzWdgWYoFyAftQxT24xR7guxVtyeebgB8RALGqOldLVHxbzTyScQwvJm6TOhelXYZIVJaDZ2FdrDz68MXea3CvqUhdLrheIQBoVKndAGP7WklkNgULKm_47goj41CoDfCMsDDVaseokH4Vh4NnFPTjgK3Su48tkdWweIpQVdLegYsunAbftub3gjWRA5OeO2Hp1LNi2FodGa9ozCQQOXJCJvPkTc_LhqT1mq-v_3JZrhbUm-r3VlNfu1B-Mumd9r7GI5JkLmoWzIqnjI4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGNx8pg7WoNBP2eQQc0V7A9PSwLEIYV2YVOm4JmD4bPl89xTTpkCuHVWpFd1yYvj-xKt6fCsHOmb71g_b_8JnTR1NOm_S-OYbZ1vb3Zhepxjv9KVlZBKJyXDpIIiLxSsegsgnBzXal8bjOvFpbkjr-A_MH_WmkMZT26zcs-4HvxHScn0ZsLghJ_E90782OiK8Vf69ZArJW1ju19B-dIwD1ES8UYwsmFfUqmEYM5stg4fzGAusETrYHmtNt9Gq0yhg3Iu8e-deRBpRJ7zifLhcUHiRzpSHsaDGp2IPnZu1Jr9geq5Vpi00w09PIaELwKO2TdXJ_IvTuPkncKAp0WL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9ncgq2hEjFNWmleEl0leW3J7y4guWEnn7sJaSpst0NoCy5LO5hTnQTdIatEy8cUv00q79m3qy4hBiX4S6PDynqY9XEwtW6tJojGww-gHA3QPlxJzd6mSuAX-MDrzGEOx87qpb6Mg8M5FGxGiQfOTSHXd-k_X-DbD4HoJz5hO9cchyg_3botqVxhHEEqMpBd3J4lZGjX-bQBR6mnwMz4AmQP0-d-vu0b_mbKQ-kBgSg81AhiNjuhNJTlxydsIfagKDPBEctiAlTCgh9MlbNYBX8N8GVRE-1JxzXnyRq4c3SDpamfUhiHW8TmkWXi1CdtKP7zL0Y5H1GGYKMhB1RU9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ساختمان
شمالی بهتره یا جنوبی؟
🔹
سوالی که همیشه موقع انتخاب خونه برامون پیش میاد، اما میدونی تفاوتشون چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/665434" target="_blank">📅 22:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665433">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آکسیوس: آمریکا به ایران پول نقد نمی‌دهد، طرفین در مورد اولین قسط از دارایی‌های مسدود شده ایران به تفاهم رسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665433" target="_blank">📅 22:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19424de197.mp4?token=HvaHDverBztjxJHYK7WgqHm2XuE8vwZjQAixXju1sPZk303jaDRW28M4UilbCkm_5EDZxablvKcRHxz82cSXb5dgT2EoGmQ8TddYIFgViftnWldpAdQwmD13rd9KZbWuQdxPpFArfNS274yCl1y-1gQR_q6g8_H_ylC9YsNVf0jAVAdr9KKEW0V4FrqjaIMxliJ7c49UM-O095nuldYV3RIzLx6cNeQ-cA3tuQ2PuM4VgjY3nW0CWgaa4-3NurpWThvbGe56krCqWS1OiMJjpNNJ7Q44cAvXO4672LXsV1V9PTIMPHVVCQVCPbjhNShRv-q49PFgPfVtVsc0IRfEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19424de197.mp4?token=HvaHDverBztjxJHYK7WgqHm2XuE8vwZjQAixXju1sPZk303jaDRW28M4UilbCkm_5EDZxablvKcRHxz82cSXb5dgT2EoGmQ8TddYIFgViftnWldpAdQwmD13rd9KZbWuQdxPpFArfNS274yCl1y-1gQR_q6g8_H_ylC9YsNVf0jAVAdr9KKEW0V4FrqjaIMxliJ7c49UM-O095nuldYV3RIzLx6cNeQ-cA3tuQ2PuM4VgjY3nW0CWgaa4-3NurpWThvbGe56krCqWS1OiMJjpNNJ7Q44cAvXO4672LXsV1V9PTIMPHVVCQVCPbjhNShRv-q49PFgPfVtVsc0IRfEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم‌پناه، معاون پزشکیان: اگر قرار باشد نظر رهبری هر آنچه که می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد، دیگر مجلس و شعام معنا ندارد
🔹
رهبری نظر می‌دهد و نظرش کارشناسی می‌شود دوباره برمی‌گردد یا می‌پذیرد یا نمی‌پذیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/665432" target="_blank">📅 22:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: استیضاح وزرای نیرو، کشاورزی و کار به قوت خود باقی است
مهرداد بائوج لاهوتی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دلایلی مانند جنگ دوازده روزه، حوادث دی‌ماه و جنگ رمضان باعث شد شرایط استیضاح وزرا در مجلس فراهم نشود؛ اما استیضاح وزیر نیرو، وزیر جهادکشاورزی و وزیر تعاون به قوت خود باقی است و پس از بازگشایی مجلس و در نظر گرفتن عملکرد دولت در جنگ رمضان در‌ این‌ باره تصمیم‌گیری خواهد شد.
🔹
دولت از سال گذشته وارد کردن ۶ الی ۷ هزار مگاوات انرژی خورشیدی را آغاز کرده که این اقدام تا حدودی آسیب‌های ناشی از جنگ را جبران کرده است.
🔹
تصور من این است که قطع شدن چند مرحله‌ای برق در سال گذشته، امسال اتفاق نیفتد و در بدبینانه‌ترین حالت همان یک مرحله قطعی را داشته باشیم و با استفاده درست مردم بتوانیم بهتر از سال گذشته از این گرما عبور کنیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/665431" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aafaa66f0.mp4?token=SW8-FGmVM04fUK6HBBtN3IuoDXf9TjH1CRDpXJ6Nc-AK06m0tzsr5ZHQfUxq3PK4hdVyC7vX8Xn2N4MECvLZKd9uKKGOFg1hcaIx-zbsy0kB7IZy6Ae15BO9Q7RWhbsydo598MxkmrjlhjgeTcqrWykAj-oCa7crpYz6ppCaiBOSO4w_d1hrSKKyeIx2gGGzNMcgficq_9OEa-HnzgG8dZ6pNlkbUCJYP7DMi6jJkba1s4aLCRqDHwn0BEq-pm_a3d6Chw6HbmPup5zC-ERQD44G7aNcLsEm6iz_6rYclwVxrDUHVleXJqdlorIvR6GYAv_rRLT32bM6vu8RASqTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aafaa66f0.mp4?token=SW8-FGmVM04fUK6HBBtN3IuoDXf9TjH1CRDpXJ6Nc-AK06m0tzsr5ZHQfUxq3PK4hdVyC7vX8Xn2N4MECvLZKd9uKKGOFg1hcaIx-zbsy0kB7IZy6Ae15BO9Q7RWhbsydo598MxkmrjlhjgeTcqrWykAj-oCa7crpYz6ppCaiBOSO4w_d1hrSKKyeIx2gGGzNMcgficq_9OEa-HnzgG8dZ6pNlkbUCJYP7DMi6jJkba1s4aLCRqDHwn0BEq-pm_a3d6Chw6HbmPup5zC-ERQD44G7aNcLsEm6iz_6rYclwVxrDUHVleXJqdlorIvR6GYAv_rRLT32bM6vu8RASqTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما با قطع برنامه گزارش قالیباف درباره اجرای بندهای تفاهم، به‌جای فراهم کردن بستر پاسخ‌گویی، مانع آن شد   روزنامه خراسان:
🔹
قالیباف اگر سکوت کند، متهم می‌شود به پنهان‌کاری، اگر بخواهد گزارش دهد، صداوسیما ترمز پخش را می‌کشد. صداوسیما باید روشن بگوید،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665430" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6fb81a0d.mp4?token=bATQ2C8RKp5nLG8E7vR3ngnc4gxIKh4ATJ4rt1W4oqekbz4ZjxHW8g8CuiDeX0oEggWhH60HeqFhzxl8O5pOetSCB5lHRqsmfugp4WGr5XqfdvjupLocQGbqmZC5KVfe9zxRJ7WgM-UcOpqPZwjubwc69c5LD7noXp15TOzTUjEdhzSt0yj5RPGWEFqAsRh96rS4eOuyvw3HdYQZEkOihG7S08M76lLX7GpuqidXZf39WtP7IjI2q2A8QoXKB84b5TDGGVI9alan1ZgFSEkrGzeyfK_6-mBiWDImwzmvGwvMou_BO2lpTNvRi_4FlIMed0MjfbFL-QHC0WEQFv4H_EeZV8tquXSZL9amPN2jMGP4V9H0IZ42M-Uw1RkF3dJnx2LMWiFXkuBBF3GbQAyFvy9HT6Gw_zCXWZSqjQ1pRzUS4NrEnMVDc61fl2h1IQKnBYq7pAlY4znY4D5Bj4QD2h3FRc9TX6rBLmvPyql0ymjC5NM5oJrbJfi4nEgVhivGsqplVW_OopYGivtlslQlZWMc03lvE68qH87pCd_olULjhZG15ggIsCxvyx_E0g734IXxv06ixE_53YSw2MEGGqNDpfcTBjL-EVd-toZgIFG4gCGzZjJqYvotPQY4UzgcHHWnv2yxOw9r2djpWpOBrWVDMMhG5Jtz07a252ij5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6fb81a0d.mp4?token=bATQ2C8RKp5nLG8E7vR3ngnc4gxIKh4ATJ4rt1W4oqekbz4ZjxHW8g8CuiDeX0oEggWhH60HeqFhzxl8O5pOetSCB5lHRqsmfugp4WGr5XqfdvjupLocQGbqmZC5KVfe9zxRJ7WgM-UcOpqPZwjubwc69c5LD7noXp15TOzTUjEdhzSt0yj5RPGWEFqAsRh96rS4eOuyvw3HdYQZEkOihG7S08M76lLX7GpuqidXZf39WtP7IjI2q2A8QoXKB84b5TDGGVI9alan1ZgFSEkrGzeyfK_6-mBiWDImwzmvGwvMou_BO2lpTNvRi_4FlIMed0MjfbFL-QHC0WEQFv4H_EeZV8tquXSZL9amPN2jMGP4V9H0IZ42M-Uw1RkF3dJnx2LMWiFXkuBBF3GbQAyFvy9HT6Gw_zCXWZSqjQ1pRzUS4NrEnMVDc61fl2h1IQKnBYq7pAlY4znY4D5Bj4QD2h3FRc9TX6rBLmvPyql0ymjC5NM5oJrbJfi4nEgVhivGsqplVW_OopYGivtlslQlZWMc03lvE68qH87pCd_olULjhZG15ggIsCxvyx_E0g734IXxv06ixE_53YSw2MEGGqNDpfcTBjL-EVd-toZgIFG4gCGzZjJqYvotPQY4UzgcHHWnv2yxOw9r2djpWpOBrWVDMMhG5Jtz07a252ij5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بحرانی بنزین در روسیه
🔹
تاثیرات جنگ به پشت فرمون روس‌ها رسید. قرار بود سوخت اهرم فشار روسیه علیه اوکراین و اروپا باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/665429" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=tPQx2q_rG8h7ZWTPwKvnEGJNLqDzxZkPAOfwX1AS9wTU0nlYZWEY-JVe61y8u5r_pJiwyUsKtq_ERIwpfrgb5saJ2JPrlAfV4cyFUKL7-mQdp1bE95obpxkKZmniyjOlDHZG_CsiZt2BY3dahJvH9a3_f9pQCqq5IhXL4RdSRy6Q1KiOudT3xduHr5hJxzOX2DM6ZV-LVGrOLI6LnckdsjIHeuLJA0AP2SH-YgMxaTtoR8rSH0-i9xKdDV_KJLcRLzZaUPa8eLhQkd2Y3FeKEkdKbiOJLuJsDfQE-JG1iCfSW4an5WWHIk_uq6DymObdmH46JtdHixOJWQwwWgS_pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=tPQx2q_rG8h7ZWTPwKvnEGJNLqDzxZkPAOfwX1AS9wTU0nlYZWEY-JVe61y8u5r_pJiwyUsKtq_ERIwpfrgb5saJ2JPrlAfV4cyFUKL7-mQdp1bE95obpxkKZmniyjOlDHZG_CsiZt2BY3dahJvH9a3_f9pQCqq5IhXL4RdSRy6Q1KiOudT3xduHr5hJxzOX2DM6ZV-LVGrOLI6LnckdsjIHeuLJA0AP2SH-YgMxaTtoR8rSH0-i9xKdDV_KJLcRLzZaUPa8eLhQkd2Y3FeKEkdKbiOJLuJsDfQE-JG1iCfSW4an5WWHIk_uq6DymObdmH46JtdHixOJWQwwWgS_pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: دشمن در تلاش است به دستاوردهایی برسد که هنگام جنگ نتوانسته به آن دست پیدا کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665428" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTxiuTYdKDheWUz32KRYqDNyYMjs_413UUg_ZEEAktqcgLlqdr-1Y5XbH6ZeLw8iTPwwP6LBIeWtzHXptTAW_vyDRKEtwVv8giJJJ9A3C39IF9ImLuSAB6egI_mD2UFqKMrbkBNplSqV2yWZE-_9CcunWRhjNqYRPIeTHBLZj4vkQiyXfQMZdy0QU3t0GGJ3iHxHUHMjksmml8Ae4MeM6v5se3NCfYtrfqyleqxYcP05m96TXJOY4JkWpoo_nT0gZy2fmGWSEnoEx3BgzHQmoFQrr0P5J8F_IUzR2H-gvjk4ZAc0Yhsq1k-0rMzmarNQLSodBBwxTHuZqolL9SP1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpu_i6i1eEXt4VMdstmT_osr350PWfDgiGcMyZQCeSYULxzHlO3znNt16OpJZJSLI-AwXLV5pLeQYz9G68AoJ2imgghw3i9Tc75hPH95ofnnQ6gkozbJplnIWKIMyepBOx6hSBgDxoG06cOcazD5J2vP7c1UIEHnjuLn4Qe5Vd_a_wwsVPb0JYunfQFWb-lK1t8KHDpzn88y4G4hXNojf9ElNH6lv0pcBzfnci0XxcY-b7l6ZXZ12CDNsKY4oYKu8dgI5rpOtOmGexsLSQ3ZYL7zXVk5Exig2cOcUKFKKe7bZLAq0I1uOlrMT9EaCFiFtX5xgFn5jbZaAc0YMblPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byVAzQfvcvuN4nqVaMSx8g3m0LMeN4lLuSxqL6p7D4PX59J8dCduesinu_EfbFY_fpyaeNI18UXsd4V6dEl615Iohi_z4SzqJUoy6ysjvRdWUVO-Ew4RObsqn_zFdzMIAF51ppQLl53RiAZayBeAKoss6z9eLw7HkxuG47IjnY2eK08MaDtewUf7pO3t2_diwF-isfcHiwAnTS6PMDU3xF8xH_Qs-Cs0lWdp1XPu-Fg9mCl5S5BRgW5OXEuQcxvRTYx8tSSGj_6tecIh926azkwhLbAAtAdgHcnbQLqbBkNFTGwAgOY4a-PuXpGFbWzwRtE8bxNT7QocWt35mNjlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtbVhYlYPnDKhbgTURAhkPv0kM9qE0fJRb8zzYVgpPf8z7iJXevkVD38YniWmlwXFfbWSyLTWnrrR6SXTdNawCo27g-Kv6Qj00nkVizah-dYGXnoXBWdQJ_RdJW1CHSU2Cbt-AHaQk2AOb3bbqWZKcIkQdqBgRfZovIT9bciY9X-hD6NK2kAUvDwHr9-EmaA1W0vJoRrH2ukI0y2szOC83pmrFvlFmCkB26jepXEti-sA-L6KIs_JTfITuT3ucW0e5YY0wDb9MwOt4a7fVsTA6bhNN9ShHqlosWO_jljJhXjhYJJwBDuov2MknYeHeZMjNdoXxHs8XlS8I4Xir1h9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمای زیبا و دل‌انگیز از بازار رشت
😍
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665424" target="_blank">📅 21:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پزشکیان: هیچ‌کس نباید این‌گونه سخن بگوید که گویی دولت و نیروهای مسلح دو مجموعه جدا از یکدیگر هستند. این همان روایتی است که دشمنان جمهوری اسلامی ایران دنبال می‌کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/665423" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27152751e1.mp4?token=F2zGJbGWPQ__OwZbs56huVOtlnnBqfkuWu8kOb5_JrXagZ1dkjGLGhqoNt9-EmujMrhq16xq6CWh_ghovpYlZDxzUig2Hu3Rq87aqVeErdL0vD-DKle7N0EbLx2NLM51onYDl5S7Y7JAu_C2zDknKMX3xIEE_rn5RG_M1GW1MSSlQS0SeXOgfVeXqwrqGfO_FV9EKOi5CxM2z9obiZc0XEfZdpy9kpmewn7I_t7VPFZ7V79bv0Z9zjnfIXLKhj60Uy7nKiQhQblj_OVSRP751Aryi2X4EybPoXzI05TBHWC9ERNQ7igIF5dr-eOXLdzWeICFU8ghdEN-eQUsk3NC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27152751e1.mp4?token=F2zGJbGWPQ__OwZbs56huVOtlnnBqfkuWu8kOb5_JrXagZ1dkjGLGhqoNt9-EmujMrhq16xq6CWh_ghovpYlZDxzUig2Hu3Rq87aqVeErdL0vD-DKle7N0EbLx2NLM51onYDl5S7Y7JAu_C2zDknKMX3xIEE_rn5RG_M1GW1MSSlQS0SeXOgfVeXqwrqGfO_FV9EKOi5CxM2z9obiZc0XEfZdpy9kpmewn7I_t7VPFZ7V79bv0Z9zjnfIXLKhj60Uy7nKiQhQblj_OVSRP751Aryi2X4EybPoXzI05TBHWC9ERNQ7igIF5dr-eOXLdzWeICFU8ghdEN-eQUsk3NC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ جمله ماندگار رهبر شهید انقلاب درباره نقش و جایگاه زنان
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/665422" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd755b8ce9.mp4?token=KMwPDy6QdHYY3QsKEocMSP1JtEkyGnQlP3WQ5Y80KViRNYALrlGngNG9T-wNhqA01FoDSMq_sBPbXyRSyvtzNavW0G63Y66948D-QBiIZmcJQ-ME3R25kHpaFsENmGgQjHORnqqQ3OdPXB6pXFwOQw-JsSmgAom21S_IwXp6cNFhRSR7OInevWZ2zZ9JlTmDptfeO_sp9SSo3aQ0tsImdoaSprInexHrCfrltU5FOfVYlhhO5uM9bJVQMKRXA2wnjQhT6KMK9p_mLQSZXeHRaWX3sRXyF2pd0eT6BLkvyjiiSI33cT2spWEZekoUw_6naTuxSH8_--WbhPUiNyh6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd755b8ce9.mp4?token=KMwPDy6QdHYY3QsKEocMSP1JtEkyGnQlP3WQ5Y80KViRNYALrlGngNG9T-wNhqA01FoDSMq_sBPbXyRSyvtzNavW0G63Y66948D-QBiIZmcJQ-ME3R25kHpaFsENmGgQjHORnqqQ3OdPXB6pXFwOQw-JsSmgAom21S_IwXp6cNFhRSR7OInevWZ2zZ9JlTmDptfeO_sp9SSo3aQ0tsImdoaSprInexHrCfrltU5FOfVYlhhO5uM9bJVQMKRXA2wnjQhT6KMK9p_mLQSZXeHRaWX3sRXyF2pd0eT6BLkvyjiiSI33cT2spWEZekoUw_6naTuxSH8_--WbhPUiNyh6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران در برنامه پرچمدار: قرار است از همۀ مدارس تهران برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع رهبر شهید استفاده شود
🔹
علاوه بر مدارس، مساجد، دانشگاه‌ها، ورزشگاه‌ها و سالن‌های ورزشی نیز برای این منظور پیش‌بینی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665421" target="_blank">📅 21:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: پیام آمریکا در دوحه به ایران این بود که، بزرگ‌تر فکر کنید
🔹
رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665420" target="_blank">📅 21:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voDxHt5VLzFHsWjh0hK-ZHAKEPmQdunGvD7MTOzhixUb-NDpCzRWubwUR5OlbUVhtYO7rKapyIL9XFiAbNdWGehz2gsT6j1XZ_re7alz-HfMd4F8Y2fdGJ4nw5DiTMlK-ls_PukdKds27ct_ImTnDBsVEF8toO7SbF3MkA-G3jTcYNov81OWwAcTai66klV1_95Fb7KMCCAxib-BsOObRFLl2qi61x7W37_Gfb3g7EW3YobxT-ujA3qkCSTN0vQUiiTgW_mQt8B5lYOLLhjxSMao7GlQNW018i-sI7pKIJw79nZvAZXK9mPGE8cpAE5gp-2djn4uUzJ-7RQrCDs_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
براکت جام جهانی تا این لحظه
🇲🇦
مراکش _ کانادا
🇨🇦
📆
شنبه ۱۳ تیر ساعت ۲۰:۳۰
🇧🇷
برزیل _ نروژ
🇳🇴
📆
یکشنبه ۱۴ تیر ساعت ۲۳:۳۰
🇫🇷
فرانسه _ پاراگوئه
🇵🇾
📆
یکشنبه ۱۴ تیر ساعت ۰۰:۳۰
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس _ مکزیک
🇲🇽
📆
دوشنبه ۱۵ تیر ساعت ۰۳:۳۰
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/665419" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665418">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مقام آمریکایی: پیام آمریکا در دوحه به ایران این بود که، بزرگ‌تر فکر کنید
🔹
رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/665418" target="_blank">📅 21:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665417">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61962be8c.mp4?token=GJ2dNWsqwQn5xibVhKhXmrdmqc-QzxGX8Wsoi3ncsyvHNrstJe0nJZFtq3mMLklDg0NGB3UuB3i96AaIPW33PumiLpnzZr7lwcLFHLC89ap5GYToPZC5RFS_W34OOpvCqAb9xLINjRRxrv9c-JBnkn7T0GTeQwHZ8jxTVOHgD8pQoM7_75B4pT62VdPuHiWRIRPmZf40AwT8Wp4cHfmpEss6vCXXLCwGACtIOz7oxrvh7cQdHQkzXVt25k2gtYC5A5FDFMsHN3DyVk3i__rqanMqOL80NWTLBD-VIegghiwEGdu5HMb_IFqpcw-YBQvtELnQ1mfT1S6bXCPU99cCGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61962be8c.mp4?token=GJ2dNWsqwQn5xibVhKhXmrdmqc-QzxGX8Wsoi3ncsyvHNrstJe0nJZFtq3mMLklDg0NGB3UuB3i96AaIPW33PumiLpnzZr7lwcLFHLC89ap5GYToPZC5RFS_W34OOpvCqAb9xLINjRRxrv9c-JBnkn7T0GTeQwHZ8jxTVOHgD8pQoM7_75B4pT62VdPuHiWRIRPmZf40AwT8Wp4cHfmpEss6vCXXLCwGACtIOz7oxrvh7cQdHQkzXVt25k2gtYC5A5FDFMsHN3DyVk3i__rqanMqOL80NWTLBD-VIegghiwEGdu5HMb_IFqpcw-YBQvtELnQ1mfT1S6bXCPU99cCGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به کنگو روی شوت دیدنی هری کین  در دقیقه ۸۵
🤩
2️⃣
🏆
1️⃣
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/665417" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665416">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
غریب آبادی: تصمیم گرفته شد کانال ارتباط فوری گروه نظارت نیز تا فردا تشکیل و نقص های یادداشت تفاهم به صورت رسمی و مستند، اطلاع رسانی شده و در مورد آنها بحث و بررسی و تصمیم گیری شود
🔹
در جلسات با مقامات قطری، از جمله بانک مرکزی، برخی مسائل مربوط به هزینه بخشی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/665416" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665415">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
رئیس‌جمهور با اشاره به برخی اتهامات مبنی بر عدم اطاعت دولت از نظر رهبری تأکید کرد که دولت تابع نظر رهبر انقلاب بوده و اگر ایشان دستور می‌دادند جلسه یا مذاکره‌ای برگزار نشود، نه جلسه‌ای…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/665415" target="_blank">📅 21:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665414">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
مریین ترافیک: تنگه هرمز هنوز به حالت عادی بازنگشته است
🔹
ادامه جریان عملیاتی در تنگه هرمز هنوز به بازگشت کامل به مسیریابی عادی منجر نشده است.
🔹
نگرانی‌های امنیت دریایی نیز همچنان بالا باقی مانده و سامانه ثبت حوادث اکنون ۴۹ حادثه تأیید شده منطقه‌ای را فهرست کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/665414" target="_blank">📅 21:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665413">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891dc36791.mp4?token=g-csQiXVdAhGobSwt5QEUOPuIWO4NH5rDjTzMwjdY49-pf-Z7IHyxJWCMYaVhJtXx4pxgIoyGLffJDpbig4rYDy1QCy_HFF_I5sIws3vPHbRvmecZgAC864sbAjcXxPVhfDz0bhKxmHEvOWH20C5T_fTooLq_YRvi4M1IxFLeuKI1DNHPZPChl_-5iEw567TGO3AmSlQcvaKcyjKre3FU3y5AfQYIXkW3DhRJgV0DPObsj64PzDvPbociCOQklrJ4aeCFzY9qeoReiRWyUZ2yHdjy_4LWCCai5B-ZVYwKXn1hZFwTE-MMA5pVuNuvehydCuzZNU_qMTCII5YJKQhQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891dc36791.mp4?token=g-csQiXVdAhGobSwt5QEUOPuIWO4NH5rDjTzMwjdY49-pf-Z7IHyxJWCMYaVhJtXx4pxgIoyGLffJDpbig4rYDy1QCy_HFF_I5sIws3vPHbRvmecZgAC864sbAjcXxPVhfDz0bhKxmHEvOWH20C5T_fTooLq_YRvi4M1IxFLeuKI1DNHPZPChl_-5iEw567TGO3AmSlQcvaKcyjKre3FU3y5AfQYIXkW3DhRJgV0DPObsj64PzDvPbociCOQklrJ4aeCFzY9qeoReiRWyUZ2yHdjy_4LWCCai5B-ZVYwKXn1hZFwTE-MMA5pVuNuvehydCuzZNU_qMTCII5YJKQhQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به کنگو توسط هری کین دقیقه ۷۵
🤩
1️⃣
🏆
1️⃣
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/665413" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665412">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7aZ-fLiQnQCiFTMs6SP2vnAXPT2Aft7BsGwvXObLvGmfZ7XjfwgGDNxyWgBg-kI86FQ1mKYZIRlSAnYilL17RU011y4pg95xybX_sTLaUeQnWV8lwfDbGeclvbv8eYjgbAaVEhpBKUY5PsI-Rg_io3mMYna1spaGoHmPFWm47M2_GMKqifnl1HrUBioUigSRhCOIvvwmtkJGhMczBY_8bvLipX_yZx8XXl7BIp1XskRX3JHssaiVXN2HBO4cg2dVa-S_k14abZgS9-z8qz20lGVpIxTu0-5kjhAQbsHCdpUxYfP5-aOxfAi-A1XGAp55ms-Draj_i5n0TUOpILwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: مانیفست ۲۰۲۱_۲۰۱۸| (Manifest)
🔹
ژانر: معمایی، علمی‌تخیلی، درام
🔹
امتیاز (IMDb): ۷.۰
🔹
خلاصه: یک هواپیما پس از پروازی چندساعته فرود می‌آید، اما هنگام فرود متوجه می‌شوند برای تمام دنیا پنج سال گذشته است! مسافران نه پیر شده‌اند و نه می‌دانند چه…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/665412" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665411">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ac2561aa.mp4?token=SghnuUIaL6ONf3ywb1S2QD8lZ-iSueRjBBySd30PezofoOzz93LY0Yjts2iDwKldi-W7RqdRoTdgJesvtzDmrG_gcm50YI4lOhl3fglKOtv946mxZUtHfro9EuQRMRryjwBBVtZhH6BpSg7e0Vh_imuHkZB0g5qBQFbFsqWhb2I0mxRx0vkZ1P7okH0c3hlMWe_YB2pgEwoQmlsZE1z2weZNaygqgM_18UUlG7IhCD3qZaPcfrCTOktzgVNhL4vzcYoYXciCz0_ZiZlEvq29mO_FajyT4tcfgeaqubvJrdIgfDFknmiSWH79aBoXTmTAyKK-TMxi3xHMwHW57oWHkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ac2561aa.mp4?token=SghnuUIaL6ONf3ywb1S2QD8lZ-iSueRjBBySd30PezofoOzz93LY0Yjts2iDwKldi-W7RqdRoTdgJesvtzDmrG_gcm50YI4lOhl3fglKOtv946mxZUtHfro9EuQRMRryjwBBVtZhH6BpSg7e0Vh_imuHkZB0g5qBQFbFsqWhb2I0mxRx0vkZ1P7okH0c3hlMWe_YB2pgEwoQmlsZE1z2weZNaygqgM_18UUlG7IhCD3qZaPcfrCTOktzgVNhL4vzcYoYXciCz0_ZiZlEvq29mO_FajyT4tcfgeaqubvJrdIgfDFknmiSWH79aBoXTmTAyKK-TMxi3xHMwHW57oWHkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج مرجع تقلید شهید و تأثیرگذار تاریخ شیعه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/665411" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665410">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
🔹
رئیس‌جمهور با اشاره به برخی اتهامات مبنی بر عدم اطاعت دولت از نظر رهبری تأکید کرد که دولت تابع نظر رهبر انقلاب بوده و اگر ایشان دستور می‌دادند جلسه یا مذاکره‌ای برگزار نشود، نه جلسه‌ای تشکیل می‌شد و نه مذاکره‌ای صورت می‌گرفت.
🔹
نباید به هیچ وجه زمینه اختلاف و شکاف در کشور ایجاد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/665410" target="_blank">📅 21:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665409">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ef9e931.mp4?token=aGFgucfK_HoWIY4TrEr2AAWBsgaAnJjGYv89NLzB-92BF-1C3MV0UJpL1SGvQWyKguoAKLxTqJ7svOzvBjqAw2bZ7a7q4Z6xcR9eSrYWHX4fD4kaO4gO0GhQkGA8YFTdh6TvVd2A3ZU6FR8S1HAq9Xcm-BoQy00KAxr1SoOG_qnYGOyiQl84-5pBtNDNIJCO_quCiZrHpwg0qC3WycrFJGEUuL0sxeQ7fOhey_iC6Ax-FQOontHpPkK9VUtR0juJXusHjohN4B0LovnzxYy-t337wRh3z17UKkBxfv239Y4aPMEmC8jn1RI62LNuicUQrLTBJ7ER2I9KciWqIQugng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ef9e931.mp4?token=aGFgucfK_HoWIY4TrEr2AAWBsgaAnJjGYv89NLzB-92BF-1C3MV0UJpL1SGvQWyKguoAKLxTqJ7svOzvBjqAw2bZ7a7q4Z6xcR9eSrYWHX4fD4kaO4gO0GhQkGA8YFTdh6TvVd2A3ZU6FR8S1HAq9Xcm-BoQy00KAxr1SoOG_qnYGOyiQl84-5pBtNDNIJCO_quCiZrHpwg0qC3WycrFJGEUuL0sxeQ7fOhey_iC6Ax-FQOontHpPkK9VUtR0juJXusHjohN4B0LovnzxYy-t337wRh3z17UKkBxfv239Y4aPMEmC8jn1RI62LNuicUQrLTBJ7ER2I9KciWqIQugng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی خاص از تشییع فرزاد جمشیدی
🔹
فرزاد جمشیدی با حضور مجریان تلویزیون و همکارانش در قطعه هنرمندان بهشت زهرا آرام گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/665409" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665408">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334e0e88d8.mp4?token=ryxqsdCNRjdZYWYxrNsVZ5ZwPc5UbAro-jYteoxZ7Y5H3SbwEQiFwPKU-JPiFS84pmOTwSydrMbV-j8Lv-ZvTHBrcPlHnjithDetqfPbIQlOcOgi14YrbZEZqmRNdlw9hqaGLJYSFQKkEDPRnPUY1l28TEpuwPNFIl3kpQh5HuL1LV1JbGTCr2fifodkTblsLeMFWaiKoGfaaI3SyIUc-pvwwc4-nXlVHw7fWlSbv-dB5TUkqILyY-HIste7TcDQmlpsO-rWZAmXTHXk26dlqf_pFB-HLcKyesJvoMYrLrANhxUiaLpkdxDQt64FKzcy2iYgkL8dP-vlNs0rrOR6WkKpIybnpZcTfMWoVaXAeiG9c7QFkqDQt1Fi89Wm2uQeKTlb5B2paWqR6P1UgqEV7ZuZ6fgi9dCFS5Ke9XQvzDswcH42uV9526-prRYwXK7tXeNUREuu5epHXFCEwv0A8eSd7Nb-jYGrL2xH5Nb5mfknmalT3txg4WZ23fm-5meeGz-VvDH6_0ly5IWduRczN1So7N2lwUMEXO8T_M9IZ_YInF57_m93bKgiDJpg_JS8Y-9pNNyKwgSIKK0RTcGo-VRfYFq7u7mDX38Zc0AVXuoOXrO0a4dGzN1xxQPfYcjbX-a1nnjTIoGemxVSz-iqQxDhJeXzfAH5UBApGam69XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334e0e88d8.mp4?token=ryxqsdCNRjdZYWYxrNsVZ5ZwPc5UbAro-jYteoxZ7Y5H3SbwEQiFwPKU-JPiFS84pmOTwSydrMbV-j8Lv-ZvTHBrcPlHnjithDetqfPbIQlOcOgi14YrbZEZqmRNdlw9hqaGLJYSFQKkEDPRnPUY1l28TEpuwPNFIl3kpQh5HuL1LV1JbGTCr2fifodkTblsLeMFWaiKoGfaaI3SyIUc-pvwwc4-nXlVHw7fWlSbv-dB5TUkqILyY-HIste7TcDQmlpsO-rWZAmXTHXk26dlqf_pFB-HLcKyesJvoMYrLrANhxUiaLpkdxDQt64FKzcy2iYgkL8dP-vlNs0rrOR6WkKpIybnpZcTfMWoVaXAeiG9c7QFkqDQt1Fi89Wm2uQeKTlb5B2paWqR6P1UgqEV7ZuZ6fgi9dCFS5Ke9XQvzDswcH42uV9526-prRYwXK7tXeNUREuu5epHXFCEwv0A8eSd7Nb-jYGrL2xH5Nb5mfknmalT3txg4WZ23fm-5meeGz-VvDH6_0ly5IWduRczN1So7N2lwUMEXO8T_M9IZ_YInF57_m93bKgiDJpg_JS8Y-9pNNyKwgSIKK0RTcGo-VRfYFq7u7mDX38Zc0AVXuoOXrO0a4dGzN1xxQPfYcjbX-a1nnjTIoGemxVSz-iqQxDhJeXzfAH5UBApGam69XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نان به نرخ روز خوردن شبکه تروریستی اینترنشنال
🔹
رسوایی تلویزیون موساد در پی برملاشدن تناقضات این شبکه اسرائیلی علیه تیم ملّی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665408" target="_blank">📅 20:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665407">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تصویب قانون ممنوعیت پخش اذان در فلسطین اشغالی و واکنش حماس
🔹
ادعای اکسیوس: آمریکا قصد مهار اسرائیل را دارد
🔹
ادعای الحدث: ایران بر تابعیت تنگه هرمز از حاکمیت ایران و عمان پافشاری کرد
🔹
گسترش حضور نیروهای چهارگانه ارتش در سراسر مرزهای کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/665407" target="_blank">📅 20:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jc3yt_-fqPJYQUs2EP9T4-wRjmd-GR0sgPHyhOAVvXwhylXI2KnFHeHEqoXdQWWhTHp9EP29JAhRpVl6CjoEMaueGZpnqQQuQVr5TnBHnBvm8XdAUhQBS8Vg_oOtlb8bKJRqYtMC-C7izL9XbMioq3VAYcxS7UTDh41tgDFm62VAHpilE192o3JkEDqipENk_JjmsZCxawfAi4zizaWit30J4OhvkDOXR-jbfa5mr4zhpVaoGHLGBtBA4L71u4QsvTtKuGEiE53aSrEaA7rS3HRtwQRYF9MgJWiP9LgwVNp5r5ri8SLbX3yOebBiqRUcxQztAhsXDLxvJbHMbETu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Urw1pF5Z8L98Xick_iZQhRF0HL9dTw_vrAktBHPourt52rs6pBzEzLTqi6EPBCDb9Dqy9n9ZSSIPJ4XPE0BjVdulcM2aOuK0avUyF2Yf3i0UQa0Ajw6pYuT0rMjlDHMwLenfPqzbGDQIhSl-ebcvPT2YQonVIh4A_TX-r9Z3_Yk-pP97-r_QyuyDMEsLaHYIlnGbWIzHKHgTnQogE0gce1I7lIzKap0HoFs9Z2TEo_UFLlB7HxjgkBS9g7jiDkjZ7kCrOO40Gp0fLoyqjOWXELWHtgjt99XYhFp41KHoZes1NENW9WSt6yStj0Iu3D9pyXUMxIIvaPY6Vgtakmww5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQkLwwrPZOSGdXf_oV8sK_ryMcbBXacPsxZNm_gcK9AHHX72muidHlqMO5cXEhHdbSOZpwBnOMkG4jPt8a1AeehXSiwNMT5JGXscCutRFLQNhp5rKdUHl9ywxN0OVE7sQR3EcNYBbCRLprco0tkpDBLXmgkRNRUPU8EvMydmFMUkFJ4cx5y7xiC4AL5LYtUEzHfaE3-2gAlTOU2daK7wEZgXwe7B-Zo8-h7AmmtrQzNlK4TT0McgYPgvGZWVlrS1m8TkFJmaUKxNCI70nPYk9jsDWFRJ_DlEA6dMxK0E433BGwrYaoIPdWT6_CnDGKgyhALwZzzzqi1hqZgMsXcgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqieSoWoZmKXApilKYvs2HcktefZw3L92e2u_Fm6Ck-IaR80NF15zxNTr7pasTjia6LoJyaBk4XPTiygvstn-KyRSKG1QSn_jdnimJShGxuy3oKBZRoq4x45FYxZprL587QNCkvfZNB9giw1GNwopDgoxkVnJXLrKWxnkZadwWq8Zzt1XJJc11DhvCd5rfvIPhtnv22CXwm3mo0aZW_sBznrwS-obl1fQK6ogQFOPKSGaXjbkQ0YNgP7U4poHzXLjfqXXpZXgZ4d7tDR5V7nGwrLwusJBV2yHDX8J4z-z57KJcNeSaKzaLT_Eicqgs51CyPmcaGEYhWvlj0Oob49BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خنثی‌سازی مهمات آمریکایی صهیونی در سنندج
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665403" target="_blank">📅 20:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پایان گفتگوهای هیات اعزامی ایران به دوحه   غریب‌آبادی:
🔹
گفتگوهای هیات ایرانی صبح امروز با نخست وزیر و وزیر امور خارجه آغاز شد و سپس، هیات های سه کشور ایران، قطر و پاکستان دو نشست برگزار کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/665401" target="_blank">📅 20:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پایان گفتگوهای هیات اعزامی ایران به دوحه
غریب‌آبادی:
🔹
گفتگوهای هیات ایرانی صبح امروز با نخست وزیر و وزیر امور خارجه آغاز شد و سپس، هیات های سه کشور ایران، قطر و پاکستان دو نشست برگزار کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/665400" target="_blank">📅 20:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db47fc744.mp4?token=T-jLk9P0EEQ7NGxIBmQhxRLYaE0CUBML5oSnbTenLkXcXJqok_iYjR6l14oO8utWz0eaxd7KZLZhi8NC0jWGsBt2Jc6RpknH2O_5TpcE5EeSgys5jKC-kTvrKM-VwQu9ApDBH5dubxrqtHLedolDUvMih8v4vDyGCxwt0uPGOT_BNPSdA5azVqNPR4NsN8P4sNqzhwfjtJEurJm-Ty1VsdrNyXkxlY6XVny5zfi6mgg3_LbMUWIeVNWtoXdiUYkWpNVb9I3G-oeKtypcsHtAKvIzrQNIr1ICMswYiiKgE6bwKgupuAIZymXnryZMCHssSON01d0o-snbwjf9sAUH9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db47fc744.mp4?token=T-jLk9P0EEQ7NGxIBmQhxRLYaE0CUBML5oSnbTenLkXcXJqok_iYjR6l14oO8utWz0eaxd7KZLZhi8NC0jWGsBt2Jc6RpknH2O_5TpcE5EeSgys5jKC-kTvrKM-VwQu9ApDBH5dubxrqtHLedolDUvMih8v4vDyGCxwt0uPGOT_BNPSdA5azVqNPR4NsN8P4sNqzhwfjtJEurJm-Ty1VsdrNyXkxlY6XVny5zfi6mgg3_LbMUWIeVNWtoXdiUYkWpNVb9I3G-oeKtypcsHtAKvIzrQNIr1ICMswYiiKgE6bwKgupuAIZymXnryZMCHssSON01d0o-snbwjf9sAUH9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد بی‌شرمانه و غیراخلاقی تهیه‌کننده مسن و متأهل سینما به بیتا سحرخیز در حضور همسرش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665399" target="_blank">📅 20:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=mlEDXcRU4_Fmvijo3yUT4nsQvrcfFqRMYWxnQb5C3hmHvG6_dhpvTvqiWCy2Hds1IDn43k_UPcNavnFpx9B8QsGxCNzF0fKssa-IQuAeU1-PZmgM-q4ypogITsR-4SWlC8joPEJapAx_a0Vcbw0VYo_UAXCDk2hhaWdLpMB4C8TQIbWgVRsaP_PyUB8AVMhK1gLou-NpsrsPYRtQ3kbgRzfsXzi2Y9zdWjiaJ6CUlZkox_RcOedbyecbCi16bzo8oIu5LbDc3PdbRM_FoiZWVDDfzPyLSLRsqrUOV9Ae7kpdekbctSMUObL_p2-1NdHPPJPOKgF7afn9XdWKbRqiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=mlEDXcRU4_Fmvijo3yUT4nsQvrcfFqRMYWxnQb5C3hmHvG6_dhpvTvqiWCy2Hds1IDn43k_UPcNavnFpx9B8QsGxCNzF0fKssa-IQuAeU1-PZmgM-q4ypogITsR-4SWlC8joPEJapAx_a0Vcbw0VYo_UAXCDk2hhaWdLpMB4C8TQIbWgVRsaP_PyUB8AVMhK1gLou-NpsrsPYRtQ3kbgRzfsXzi2Y9zdWjiaJ6CUlZkox_RcOedbyecbCi16bzo8oIu5LbDc3PdbRM_FoiZWVDDfzPyLSLRsqrUOV9Ae7kpdekbctSMUObL_p2-1NdHPPJPOKgF7afn9XdWKbRqiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های عجیب فیروز کریمی در پخش زنده خطاب به قلعه‌نویی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665398" target="_blank">📅 20:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا به دلیل تنش‌های عمده با ریاض بر سر جنگ علیه ایران، در حال بررسی خروج نیروهای خود از عربستان است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/665396" target="_blank">📅 20:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665395">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdvf5T8v-hiQbpkrmsNCpTTJ--HwOzwerVzG4JH6twZigPiZw6JsObIrjZvH3R2VvUL8ySHmdZ1U4-9dsBvQPHXBIJJquP6en8cSYXS5Yaac_rnT35S7nlqQclAPMVoU7lkHZFcSla21arlAt6eSTRqBX6pZsl1kCVxSuWHiH5pFSfS4KM9pVql2FLz8DMN5ob3Focu4u8YGf17MqjboaoiknLmj42oI35jVHGG-8qtTmRkYm2ofbc2GSiZSTSZ6ZH2eZI6KM8f5qYbQSWEFMmWwJRl14Cl9h8P5L2OlMXyipGTIofunIoAB2Gx0t9S65OCReNHdaWC4mHUWLL6sBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حجاب دیپلمات ایرانی در ژنو؛ روسری با نقشه ایران و حاشیه خط نستعلیق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665395" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665394">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دیدار با ملک‌الموت و سفر به برزخ؟ روایت شنیدنی یک تجربه نزدیک به مرگ
🔹
00:05:40 مچاله شدن بدن بر اثر فشار تمام اجزای اتاق
🔹
00:16:10 توقف گردش زمین و تمام امور دنیا در لحظه جان دادن
🔹
00:35:20 جدایی روح با فشار پای ملک‌الموت روی جسم
🔹
00:43:50 درک عمیق از شعور در ذرات نور
🔹
00:52:00 دلهره و نگرانی روح برای سرنوشت دنیایی فرزندان
🔹
01:03:45 زندگی دوباره در مرور زندگی
🔹
01:21:50 حضور ملک‌الموت در منزل چند روز قبل از تجربه
🔹
قسمت بیست‌وششم (آخرین بازدم)، فصل چهارم
🔹
#تجربه‌گر
: زهره ابراهیمی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/665394" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665393">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw7V_DsPMEvDltvUJLy8Xj3v_okxNH4ZoIZnKzU7CFWKwRz_yiF00xj7ugojOeRSt97VvhikGQQJE_wAcgcKMt1WlU2TVwBB0r6zQkD7IqUwZZ8NzgtYpTuPPS8SVti4g3noJ-I5UY5rkTB9QyRp2IHCVVdn0dY57vAVdS2xDSX5CebVKtFcrjT3uGMx9ghQW3E71cOANQ_1LKDMgQd-58jDOOlriHSTTvPW9e_xuYDGKv5wZELwS_StCo2AVaEhhTj1BRc00KCIhV47ILPyBX6H-nBeJFOEd9u4MBSnzui4epSE8mIv1NDSOoH5j_c_J9W_7REANspKUCkpxID83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهبرد «اول بکش» اسرائیل اکنون ترکیه را هدف گرفته است | آیا منطقه واکنش نشان خواهد داد؟
🔹
دولت آمریکا در هفته‌های اخیر دو توافق کاملا متفاوت و حتی متناقض درباره پایان دادن به درگیری با ایران امضا کرده است؛ توافق‌هایی که از نگاه بسیاری از ناظران، دو رویکرد متفاوت در قبال آینده خاورمیانه را بازتاب می‌دهند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3227170</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/665393" target="_blank">📅 20:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665392">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: مذاکرات درباره ایران در مسیری عالی پیش رفته است و ما در حال تلاش برای تضمین ادامه پیشرفتی هستیم که به دست آورده‌ایم
🔹
در نظام ایران افرادی وجود دارند که درک می‌کنند نیاز به تغییر روابط خود با ما دارند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/665392" target="_blank">📅 20:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665391">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سردار حسن‌زاده: هم‌وطنانی که به‌صورت کاروانی یا با خودروی شخصی در مراسم تشییع رهبر شهید حضور می‌یابند، حتماً خود را به محدوده تعیین‌شده برای استان خود برسانند
🔹
برای هر استان، محل مشخصی در تهران جهت اسکان و استقرار زائران در نظر گرفته شده است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665391" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما نگران مسئله هسته‌ای هستیم، درباره‌اش شروع به گفت‌وگو می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/665390" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665389">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
فرود اضطراری بالگرد ارتش آمریکا در دریای عرب، یک نظامی آمریکایی مفقود شده است
‌
🔹
بامداد امروز چهارشنبه، یک فروند بالگرد «MH-60S» متعلق به ناو هواپیمابر «جورج اچ. دبلیو بوش» آمریکا در دریای عرب دچار سانحه شد و مجبور به فرود اضطراری گردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665389" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665388">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826940ee5b.mp4?token=EuvDqrqX331BlWYteFO2RcN7w11RbFTO-C1gZGCXZ_lcG_INHOs6gSnHQh-XZqvulWKTJdgMYgeA3TmM3-VNt4uVfMAQcCwaSvycVD2zIJQVvjd5U5kAp859zlkAnhyd-8WNXgDhLy3URv2qLDeqC3MRT1tiUeASWcLB7zHgZb6qiHkXA1aI-lQ2guyuk1gR1OFWViVwIXJBUh36i4Et4YKJN3Ul68pX-xmkqwKsLIV6boY93YdSKukUv8mJHUdQtXSDwz3njK8nk-Pj4BjLYhryyZR7ELNc3dKkNgjA2kwsvMtR7NRWr0HkxV3kCi4p1wc4ybK58WO4baEqqUIWg3HB3NUmLde7_3BmgXvfyoHRSSL1NvXoRCgt_T3nFg1b2G9_jA-vkzTM3NAGbTQYXJ5L_Ptz2T32v8Z315BvFPzcOwYBzzY1dbi4y_Qb2UYljzDyYcagEG0IhGGQAPaeOvokltv5rINSEdQJrRGcrNHoaVtE7M--ojHViOlTyUnVI7yR5XCUNKSFGOShHId0TDuIzHy7VFulSiySS50xeJZdHRtw1BZ6fpDbrY8bttJRh5Ygd5eXWs2kxV_vdkQpbmj0-btu6Wmho1j78SYbMu7YM1QxC6AbdI0nn-n9Cw5J_QQDijVMIqdrlz5Oe2t9XnddLzgQ9ubexR0B3Ac1js0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826940ee5b.mp4?token=EuvDqrqX331BlWYteFO2RcN7w11RbFTO-C1gZGCXZ_lcG_INHOs6gSnHQh-XZqvulWKTJdgMYgeA3TmM3-VNt4uVfMAQcCwaSvycVD2zIJQVvjd5U5kAp859zlkAnhyd-8WNXgDhLy3URv2qLDeqC3MRT1tiUeASWcLB7zHgZb6qiHkXA1aI-lQ2guyuk1gR1OFWViVwIXJBUh36i4Et4YKJN3Ul68pX-xmkqwKsLIV6boY93YdSKukUv8mJHUdQtXSDwz3njK8nk-Pj4BjLYhryyZR7ELNc3dKkNgjA2kwsvMtR7NRWr0HkxV3kCi4p1wc4ybK58WO4baEqqUIWg3HB3NUmLde7_3BmgXvfyoHRSSL1NvXoRCgt_T3nFg1b2G9_jA-vkzTM3NAGbTQYXJ5L_Ptz2T32v8Z315BvFPzcOwYBzzY1dbi4y_Qb2UYljzDyYcagEG0IhGGQAPaeOvokltv5rINSEdQJrRGcrNHoaVtE7M--ojHViOlTyUnVI7yR5XCUNKSFGOShHId0TDuIzHy7VFulSiySS50xeJZdHRtw1BZ6fpDbrY8bttJRh5Ygd5eXWs2kxV_vdkQpbmj0-btu6Wmho1j78SYbMu7YM1QxC6AbdI0nn-n9Cw5J_QQDijVMIqdrlz5Oe2t9XnddLzgQ9ubexR0B3Ac1js0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا زمانی که قیمت‌گذاری برق واقعی و مبتنی بر الگوی مصرف نباشد، هم مصرف بی‌رویه ادامه پیدا می‌کند و هم سرمایه‌گذاری در صنعت برق آسیب می‌بیند.
🔹
تعرفه باید طوری باشد که از کم‌مصرف‌ها حمایت کند و پرمصرف‌ها هزینه واقعی‌تری بپردازند.
#مدیریت_هوشمند_مصرف
#پویش_قرار_همدلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/665388" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ba6755b.mp4?token=lyoiwJlwrkVC7mE4rW0T3Rma-qonzoWr3lsPSJhuAAoa5BdyNGeyLUcI3OuBPBgGdEZvStcltXn9zqc8YIIu9QeFvPVpD-sjRVRrLco4Y5mIVsmMSC0t-mtydGOEdtFy7BQFm1dWsravPaGSt_92yV2iPV5eqHq8mC5oi4eWRMGtr-BOjZGKSa40gPZAmmD90HB55DJnfOg8rER3indS6BMyLcbb4Q2UrZQBqB6AV7B5gKRrAvFvSQLY9eKAtj0StZPawOR540ZF20QRaSOfW5o69547V4UWaP2L0Urq_oU5N6-jLEAaWN0SDB4Izz-ln2L-fycaZdzU_XJw54bGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ba6755b.mp4?token=lyoiwJlwrkVC7mE4rW0T3Rma-qonzoWr3lsPSJhuAAoa5BdyNGeyLUcI3OuBPBgGdEZvStcltXn9zqc8YIIu9QeFvPVpD-sjRVRrLco4Y5mIVsmMSC0t-mtydGOEdtFy7BQFm1dWsravPaGSt_92yV2iPV5eqHq8mC5oi4eWRMGtr-BOjZGKSa40gPZAmmD90HB55DJnfOg8rER3indS6BMyLcbb4Q2UrZQBqB6AV7B5gKRrAvFvSQLY9eKAtj0StZPawOR540ZF20QRaSOfW5o69547V4UWaP2L0Urq_oU5N6-jLEAaWN0SDB4Izz-ln2L-fycaZdzU_XJw54bGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده خلاقانه که به راحتی میتونی تو خونه درست کنی
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665386" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
نماز بر پیکر مطهر رهبر شهید ۶ صبح یکشنبه اقامه می‌شود
رئیس ستاد آیین وداع، نماز و تشییع پیکر مطهر رهبر شهید:
🔹
اقامۀ نماز بر پیکر مطهر ساعت ۶ صبح روز یکشنبه برگزار می‌شود و از مردم می‌خواهیم برای حضور در این مراسم زودتر در محل حاضر شوند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665385" target="_blank">📅 20:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqyp7MjbrE9LPA4cKQU3lwQjBH0BhwSzeOBV4M3UrEUTGN5dqcRTjI63C4EOkR5j-w0VO6-VElLThIZjI127lbxO3TaGqQhaObeUGfzS7iIOadOwQ97qTtLGYI9ShS75pHGK_-zsicQhzYeUKDiXbojTyYkkMD8UBFflK8YsQX7ESZd8WbcnCWtrZhWPtNiKtahUcq-rB8wcL_FT6iIN_Gz6T50U6F69_cnPByISRtdweXVPuBg0qc2nQUS_5S0tTRnUGCRQ0pDNJbhY_lochLXPMwmJf3qcqHCgt0nXJacd6MS7mBFMQNJUq0QcLYB3DXhauzzbEMCLzs8pEfGXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه از بیمه‌بازار، لازم نیست این چند تا کار رو انجام بدید!
• نه لازمِه نگران پیش‌پرداخت باشید،
• نه دنبال ضامن بگردید،
• نه چک و سفته آماده کنید،
• نه دغدغه سود داشته باشید.
✅
در
بیمه‌بازار
می‌تونید بیمه‌ ماشین‌تون رو قسطی بخرید
و هزینه‌ش رو در
۱۱ ماه پرداخت کنید
‌؛
👈🏻
تمدید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/665384" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: تیم‌های مذاکره‌کننده فنی ما در حال برگزاری گفتگو با ایرانی‌ها در دوحه هستند
🔹
ما هنوز در مراحل اولیه هستیم، اما مذاکرات به خوبی پیش می‌رود.
🔹
اگر ایرانی‌ها از ورود بازرسان جلوگیری کنند یا به کشتی‌ها شلیک کنند، رئیس‌جمهور گزینه‌هایی…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/665383" target="_blank">📅 20:11 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
