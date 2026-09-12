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
<img src="https://cdn4.telesco.pe/file/hJBRH9lDJyOGbC8Is5ZAGJ_QGXwnkWVkOleCh9R574s3MBNs1gNTq85WNP5SqWFMuhVzkzuCP283ERNJtgwgU_zixbaq66ifZSaXY8mD9vFMiDERmB2Rzfbsxk9gc5mUIUU9mKW8NLLENO0dZACWcDiQpfA5E28gakk86J96Y2Hh1abZM2rtVH1Nja35BtJ2-GiADNTHluZiVqFxZNh1lS8_RFcp0lvFWdlWY0vf1rvIrv_VT2KgljvbIyrxQEoXKfr1VWJ4c45KAR42PyQtuyBL_hxhO4nmk7ds7pnwn5HfSxB3gQGiuhfEo1-PXZXsE83ahS6V5DsD4mpJUqOwHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 20:48:51</div>
<hr>

<div class="tg-post" id="msg-461619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0befecda34.mp4?token=YEgihGBrxRXYnz6eWgBPvORQafX1eIL_3QYK692O1tiVRsqFrkMUGTwQpGdw-eBJ8vnicQQX_Llfpc9OpTQ1uCepRNDwWoyL7r50jkhbQHCH7Tgwm2hE2o4T_3A9nr8f5Egr3nv4GxAIkZnfAPN0gAs4QfUFKRerDO5LueJUiCOCl5U-sPhfGpnxvjO6hYQ6ut4Pb5bk7aeYtlYpTjWMp6HiEDgDFbEWxvfnuPVruzYgoaVxKZwDVJTeI7CFsIm0YKxZtnVvOdqPf2xRPeRZu_brNLi7n8CsiL0OK48Syn3YEsart81lzVkpb7Y7NCbMVBqlnnbo91n83E369y1IHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0befecda34.mp4?token=YEgihGBrxRXYnz6eWgBPvORQafX1eIL_3QYK692O1tiVRsqFrkMUGTwQpGdw-eBJ8vnicQQX_Llfpc9OpTQ1uCepRNDwWoyL7r50jkhbQHCH7Tgwm2hE2o4T_3A9nr8f5Egr3nv4GxAIkZnfAPN0gAs4QfUFKRerDO5LueJUiCOCl5U-sPhfGpnxvjO6hYQ6ut4Pb5bk7aeYtlYpTjWMp6HiEDgDFbEWxvfnuPVruzYgoaVxKZwDVJTeI7CFsIm0YKxZtnVvOdqPf2xRPeRZu_brNLi7n8CsiL0OK48Syn3YEsart81lzVkpb7Y7NCbMVBqlnnbo91n83E369y1IHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: پیام‌هایی که سعودی‌ها برای مذاکره می‌فرستند ارزشی ندارد
🔹
رژیم سعودی چون بردۀ آمریکاست خوی پیمان‌شکنی پیدا کرده وهیچ توافقی با او ارزش ندارد.
🔹
ما تجربۀ زیادی دربارۀ مذاکره و وقت‌کشی در مذاکرات داریم.
🔹
تنها چیزی که می‌تواند…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/461619" target="_blank">📅 20:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b7792acb.mp4?token=DDUGGbbq2iPOk6wOlOthHC0i6gLKjBIyrIdUqL9EHKTCITqdB8c3zjfoPQ4bYnRuZY7UZg3DViZIpJCw6AEV1DLuxSIcWB2YpHDJYz5Wmlz_18H-hJCA0yEYlcv_OgTqeA0AK3ZQ_439B3jgifJaJtpCGs-CT8rwn7be3d3B4TVQNxYaZZJRV6N7ylGVHNtOa4Wd0LcJUFlymzxvKB1HGkGkD-1ibFUBoiNbhRJmz45TvrpiCOPkZuutJCLtRWQGi4gHzWd7cZvJOlw9mJXodPm5GrF3Tm6uSZGgNGfyimZj4SVCiyVBZ26lGU_l1RSF-DNObh29eFxidRk7ZSL_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b7792acb.mp4?token=DDUGGbbq2iPOk6wOlOthHC0i6gLKjBIyrIdUqL9EHKTCITqdB8c3zjfoPQ4bYnRuZY7UZg3DViZIpJCw6AEV1DLuxSIcWB2YpHDJYz5Wmlz_18H-hJCA0yEYlcv_OgTqeA0AK3ZQ_439B3jgifJaJtpCGs-CT8rwn7be3d3B4TVQNxYaZZJRV6N7ylGVHNtOa4Wd0LcJUFlymzxvKB1HGkGkD-1ibFUBoiNbhRJmz45TvrpiCOPkZuutJCLtRWQGi4gHzWd7cZvJOlw9mJXodPm5GrF3Tm6uSZGgNGfyimZj4SVCiyVBZ26lGU_l1RSF-DNObh29eFxidRk7ZSL_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ابراهیم حاتمی‌کیا از جلسه سینماگران با حاج قاسم
🔹
حاتمی‌کیا: فیلم موسی(ع) را بعد از دیدن حاج‌قاسم قبول کردم؛ حاج قاسم سلیمانی نفس من را باز کرد.
@Farsna</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/461618" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYlDJd6vwoAgG36-udSuFfw1zyS3szdbHYo4Udwe8mmTKqEFkYPjUAL_S_pCmjqMiq3mkl58tP4G5bwPglpp0eeORkNF1gzN4uVxTy6GsQExF0the4mAQazMqWSgDDNyw2bes6XuOdaCu6Xpipd10Im8IfzQKnfKcz2-zU-AJQJfSpbLHHLby0bBNwABlUPSWk6emepfxmm2hTVo-eIzMTxvcG78A1JOl_jg2Q4EdoM8xC41_lqO6Kz5svn4AF1tFLNfqANY66hOg6iqYei64Lt5iJnxj76XLJWR_RWCMJnCKoHnDSdRcbow9GNFVPo4yl1nD338JXSduEWMYagd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ۲ تن از شهدای عملیات پاکسازی یک خانه تیمی در سراوان
🔹
میثاق ثانی و مهدی سرحدی در درگیری امروز با یک تیم تروریستی در سراوان به شهادت رسیدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/461617" target="_blank">📅 20:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5458242bfc.mp4?token=lxF4rzzz3EInT8riTNox8VnhNSh7H54DhZmY2Fv-5uDrbNvElE08Igg8v0FcbgbwZmoyaoAkUDWFZq1NXFnP5DO3Ayt_VrHpwei-y_AAzZJVNhUws_3fMo5b26o8rySbEA8CN-ey6al4Uhh8N5aYueYLYXU-_26PftRPwY5CpYRqsVBspr5k-W0v8Rp_QV54fK7MCKm5Iuy0U9mhbFj8IxtAOQSyC892Y1dXqbiGkUJ97zQoEtPjaJwlsr4Jl-NoQPQM4YGwxWr2FAaNuZEoYtdCVpfKQKoznO7GVhQJfRsbYiYmt4yIDL0tkoD6E4xV7YVYAQ0iDOcKfWpTI-GaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5458242bfc.mp4?token=lxF4rzzz3EInT8riTNox8VnhNSh7H54DhZmY2Fv-5uDrbNvElE08Igg8v0FcbgbwZmoyaoAkUDWFZq1NXFnP5DO3Ayt_VrHpwei-y_AAzZJVNhUws_3fMo5b26o8rySbEA8CN-ey6al4Uhh8N5aYueYLYXU-_26PftRPwY5CpYRqsVBspr5k-W0v8Rp_QV54fK7MCKm5Iuy0U9mhbFj8IxtAOQSyC892Y1dXqbiGkUJ97zQoEtPjaJwlsr4Jl-NoQPQM4YGwxWr2FAaNuZEoYtdCVpfKQKoznO7GVhQJfRsbYiYmt4yIDL0tkoD6E4xV7YVYAQ0iDOcKfWpTI-GaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای خسارات وارده به پالایشگاه جیزان شرکت آرامکوی عربستان در اثر حملات یمن را نشان می‌دهد  @Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/461616" target="_blank">📅 20:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drd4gD5K6L3ybcfeO5u3SgBPBuaBt2JVP2EWaZlwJBdtihZxSVQgBEx-WPL8MHKi7C7Axe2toUHzYGPIkINdNX5csDPT6Zf3urCbDCeMlmzKVHG7POzvT4EL115GBwI3lSsAuPWi2Qndy_-AcMUZjAn4P0WPZZ8MDpwWjYHekkjFc5XLCK3dsEXzqEBUme6-GBqXdm9bjgTG4sJsWRhaWRKCmN7YTjUc8tdtAlWD-TPbP6ZUnc0Htti4ML9eXRFO3TiS1ba9uq1Fszd3cFoH3GLLkYlwSvnXxw5zP3CSe9L_CnF6wJ0t8bai2JJa0m_mZCAmvMgwNsO-nnm8ZpbAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما با هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/461615" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f8403a0bc.mp4?token=l4PSsT1lscKNFWTQSsYqnOJ6wUV9QwQHKc6vrAXzR4H0y5GoHdZr29XxIE7wjc0fqCKQ9uD6KdYA95_Rl46e7LMkcDe_aEHFHFzfDt-Ipk_hJNK2bQ0dvAe6cBPzbQ_O5NCTh87JF-Tzqw_WuMMr8EWXrGYlpFjfe4u3r7JsK4R4IfJuoc8WNx7R2YyNoihT0V2eTZ3UyQriUM_HGS8TU16L4kGDbGjHGMPmkuEKGMqe9jcTezH6dD_HCRXx68qOfH6JiqjkEsynyBYN_NzzKBOiCPioC9yuxI7-ibBNyrICcOSo5SpAGxuBXqvkKH3qiW1adcXP5nwaQyeQ3Nq-xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f8403a0bc.mp4?token=l4PSsT1lscKNFWTQSsYqnOJ6wUV9QwQHKc6vrAXzR4H0y5GoHdZr29XxIE7wjc0fqCKQ9uD6KdYA95_Rl46e7LMkcDe_aEHFHFzfDt-Ipk_hJNK2bQ0dvAe6cBPzbQ_O5NCTh87JF-Tzqw_WuMMr8EWXrGYlpFjfe4u3r7JsK4R4IfJuoc8WNx7R2YyNoihT0V2eTZ3UyQriUM_HGS8TU16L4kGDbGjHGMPmkuEKGMqe9jcTezH6dD_HCRXx68qOfH6JiqjkEsynyBYN_NzzKBOiCPioC9yuxI7-ibBNyrICcOSo5SpAGxuBXqvkKH3qiW1adcXP5nwaQyeQ3Nq-xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: برای همۀ جبهه‌ها در یمن برنامه داریم
🔹
هر شیطنت دوبارۀ عربستان در یمن باعث تصرف جبهه‌های دیگر در یمن به دست ما می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/461614" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce34d6f66.mp4?token=ILYX7yplM7pvwq_H_ESMA7UhQ3g-ctEsWXv3OU2h5uhfvAw-cGps-83QzcsQdfgZM0hIgfhuCmsDG_kU62wbsKhZp-6bI78s7W7zgKy8IAIwRecmDqW-oRy93SF4rwbWgIpm5bI0kDrL3Po64fTMfPjCzmqnBl7OjrFPXZ35NOWHckiU1nexmlLdGZ3KohSnayEKij4w5HgH1ZPhznDHhdUef1JIiMo4ZdAkUn7LVGvV_6dNXeeY_6YtYYu-fqiCsjn-Wmugy8cCdVlM5axMmF89IVRrjTL3zNMBTBwtZlQ3tflV1_XSo-Mza4QXgieco5QMGmx-3veY-A3znC_jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce34d6f66.mp4?token=ILYX7yplM7pvwq_H_ESMA7UhQ3g-ctEsWXv3OU2h5uhfvAw-cGps-83QzcsQdfgZM0hIgfhuCmsDG_kU62wbsKhZp-6bI78s7W7zgKy8IAIwRecmDqW-oRy93SF4rwbWgIpm5bI0kDrL3Po64fTMfPjCzmqnBl7OjrFPXZ35NOWHckiU1nexmlLdGZ3KohSnayEKij4w5HgH1ZPhznDHhdUef1JIiMo4ZdAkUn7LVGvV_6dNXeeY_6YtYYu-fqiCsjn-Wmugy8cCdVlM5axMmF89IVRrjTL3zNMBTBwtZlQ3tflV1_XSo-Mza4QXgieco5QMGmx-3veY-A3znC_jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما با هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/461613" target="_blank">📅 20:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bbpq0uPmrHUpUVgAn4LfhnNRDnmNX-0BbSyGhzkIybZvA1KXqT25PJe8bQkne1Am0isBgctJKByyEzZkbV_DtBD_R3NYmNR9skjTRtwipTl1I121QYZK_awjLARssbQ2VY7RaTwq6SpO-JOlUPziKgAd53cH6Xegb5FWZo00XXkc-gyXBaqdtub8dwsGnGdJSQoXuOvHIl3OkhmBHlyiEYkexAXRDOFj1yF9qDR2b-9StXob4p-Sfh75r93sD4pppwrzDkvyju0mQYGI93btVN4aAC_DYfLgkAA1BKKhoTFrF8rmzrpO9k5mm_-H5Fk7ei8zMR5wGhgeNt45KmTqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: ترامپ تنها ۵۳ روز فرصت دارد؛ نباید با صحبت در مورد گفت‌وگو و مذاکره به او پاس گل بدهیم
🔹
منوچهر متکی در صفحۀ خود در فارس تعاملی نوشت: هم‌اکنون در حساس‌ترین بازۀ زمانی جنگ ترکیبی آمریکا و رژیم صهیونیستی علیه کشورمان قرار داریم.
🔹
ترامپ در شرایطی که با…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/461612" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5474caacf.mp4?token=plqjH4cphHNc2T6902pfmYzTwCi4PWABhJV9aGbx4uKe7BaYDYPrEtmwTZ5Ypy39Cg4H5t3YseS-MaGw5wc-LsLCSRsywRvl_kW2sqED4UdBvY_4S3dKt4VQHBLABYMzPYtruNnQfPl9HTY4mCn-FJNHcwB6b6aBR51sgQ9UeZFuNvSNibdxJZuYy8avu8XXWrTO4sZ3PyuvIJvOJFrjei_3SB66kUXLOC-U6VR4tzIH0DxtLCnxsdMOnDBExq1BSZJ5P1pmcgT4nh-PKMFBJbgi28HPI1-LL0IvvIaqDx2jMisBLlKpKjoCjYHLyWSqmSow5cA7UVvmDCDhquKgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5474caacf.mp4?token=plqjH4cphHNc2T6902pfmYzTwCi4PWABhJV9aGbx4uKe7BaYDYPrEtmwTZ5Ypy39Cg4H5t3YseS-MaGw5wc-LsLCSRsywRvl_kW2sqED4UdBvY_4S3dKt4VQHBLABYMzPYtruNnQfPl9HTY4mCn-FJNHcwB6b6aBR51sgQ9UeZFuNvSNibdxJZuYy8avu8XXWrTO4sZ3PyuvIJvOJFrjei_3SB66kUXLOC-U6VR4tzIH0DxtLCnxsdMOnDBExq1BSZJ5P1pmcgT4nh-PKMFBJbgi28HPI1-LL0IvvIaqDx2jMisBLlKpKjoCjYHLyWSqmSow5cA7UVvmDCDhquKgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رسانه‌ای انصارالله یمن: فکر نمی‌کنم سران پاکستان یا ترکیه آن‌قدر نادان باشند که وارد جنگ با یمن شوند
🔹
البته آن‌ها پیام‌هایی به ما داده‌اند که نمی‌خواهند در این موضوع دخالت کنند.
🔹
به هرحال ما با هرکسی در تجاوز به ما مشارکت کند پاسخ می‌دهیم و هرکس علیه ما اقدامی کند به سمت باخت می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/461611" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIJCWd40pAmvmprhTABsALsCTNfMXjisSB3dWmq8fEkFaWoOynffgTzFE28kVN0Ob6a3jhHktBdKHG9NhCVynR33Sr3Djb0paCBU-pxvGkDmIk56AJ7hL1EpujDjQMW0fMqdrqfV_pAJFQwuxncbe20nysttCdl0Am-28DY_coZQPhq6bzXj-7_Slu0llFfq4_QYztGmOm3tdZDhuqyN_44dAVh84hW05QHXUZOw7sDkS_V2T0Ix43nAA7jlR_PCbxB7m94sxYWh26btJFksClLEAIWa8_19p_YhWlCzNGidlpm_NGp7VRMy91SqKlWeewnYYaq-wjRPb8-BQSpGXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6BM4C_WKJT8iALR51ZIydxcicwBonjdjEqsFBKrhS_sDD5NMYWjHPIXBRk8luWzrf6-i0lCvWSkuLGc3CJJH-KQGMLP-Mv8oLhjWeAaStuGor_woXY-RrGDR_2LXBJRdSsa53c1l0jU3vfzR1WrqEinhuYKWicGudIXkG8qbwHybsGyV10HkIj7HiqNQKA2Yh93Rr7yiJ2xHiycntG_TRHdZ_UbtpDZU4Z94TP-5aSPgCSzt7RlOPtcyl_VQS6A329cQ7rLx7piYuZUp58YPO-j-7uD2AtSDjgluxC_r7QULdLMmXP2GfBtIRVBnpyVtZN_VUAoUKcbLJmT6Wdpkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تنها یک کشتی چینی از تنگۀ هرمز عبور کرد
🔹
اکانت رهیابی‌های دریایی، منچ اوسینت می‌گوید امروز فقط نفتکش چینی لیسا با سامانۀ ردیابی روشن در حال عبور از تنگۀ هرمز دیده شده است.
🔹
ساعاتی پیش ترامپ باز هم تکرار کرده بود که «ما تنگه را کنترل می‌کنیم و مین‌های دریایی را از آن خارج کردیم».
🔸
اوایل شهریورماه یک هفته بود که ترامپ و سنتکام از مین‌روبی کامل تنگه هرمز می‌گفتند و هشتم شهریور ماه آمریکا با حمله به لارک مدعی منهدم کردن راکت‌های پرتاب مین ایران شد اما فردای همان روز سپاه پاسداران از برخورد یک نفتکش با مین در کریدور جنوبی خبر داد.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/461609" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTwnX0HgfPd2YvW2Nmz8R_RMTVMPWZ2E7O-gdU9-m_d4-shgRZANew3M04RZ55nUqbotqQWANLoia0LIqEjO6euxPo4zPyvjmn_i6pJgZ1eOwRHJB8X0pXqrdCZaZvLMQSbM9nfkCoSrI9c3gpTWWpJExfi-rabr-OAXw9q_pwoSpLUPicAQlkJMBePM3J5S1e8PjNwDRtprgVxqYgtMeTBpdcoyRDZcTcdaku1Dg-FIX1-gjj67_GF0dcfdmZr-az5AaM-6Zb0_Zwrc9fhHwgs3aeKFczkbCuquI6w6Vna1l8WbE1tkzUiGnBP8ZKLBP2nEA6Xyy90mQbAn4NYtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذعان صهیونیست‌ها به کمبود موشک‌های رهگیر دربرابر ایران
🔹
رئیس هیئت مدیره صنایع هوایی رژیم صهیونیستی اذعان کرد که در جنگ نامتقارن با ایران و شلیک انبوه موشک‌های بالستیک، این رژیم همواره با کمبود موشک‌های رهگیر مواجه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/461606" target="_blank">📅 19:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516f875777.mp4?token=ARQFc1oW62WjQofAig3U3iB2weygCn7Qy4TJfDn9zyFgE6Q7S_ucMapgT6Y95o7L2MnmFKh6eXXUs91xfEDd8K0qiLnMhmeozCcY9hOd02WndIma0sne16Hc8Fidg4PmZMH0IJ7g0Ma7Pm2w5JGky9w04E7m949PEUWW6brNNmkuTGoPAtM6Xe7NNH5AoKqZEZrcyG5qI5zpwdTQV_injxQ0Ufk5rlTSUXCKfhnNzC8SWq46nHbG5bSizqzUXr5SWTVqWYOm2z_Dz1e3BchHbqh98L-rWS_KcYSm1CO7fnghF-qz8DgcX5r44NRUx09rVOjR_TAgMAjkiDT40S84AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516f875777.mp4?token=ARQFc1oW62WjQofAig3U3iB2weygCn7Qy4TJfDn9zyFgE6Q7S_ucMapgT6Y95o7L2MnmFKh6eXXUs91xfEDd8K0qiLnMhmeozCcY9hOd02WndIma0sne16Hc8Fidg4PmZMH0IJ7g0Ma7Pm2w5JGky9w04E7m949PEUWW6brNNmkuTGoPAtM6Xe7NNH5AoKqZEZrcyG5qI5zpwdTQV_injxQ0Ufk5rlTSUXCKfhnNzC8SWq46nHbG5bSizqzUXr5SWTVqWYOm2z_Dz1e3BchHbqh98L-rWS_KcYSm1CO7fnghF-qz8DgcX5r44NRUx09rVOjR_TAgMAjkiDT40S84AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا خانۀ ۸ گونه گربه‌سان وحشی ایران است
🔹
از دل کویر تا دامنه‌های جنگلی شاهرود زیستگاه‌هایی گسترده شکل گرفته که یوزپلنگ ایرانی، پلنگ ایرانی،گربه پالاس، کاراکال یا سیاه‌گوش، لینکس یا همان گربه دم کوتاه، گربه وحشی، گربه جنگلی و گربه شنی را در خود جای داده‌اند.
🔹
این تنوع کم‌نظیر، شاهرود را به یکی از مهم‌ترین پناهگاه‌های گربه‌سانان کشور تبدیل کرده است اما در این میان یوزپلنگ آسیایی به دلیل وضعیت بحرانی جمعیت، جایگاه ویژه‌ای در برنامه‌های حفاظتی دارد.
🔹
این گربه‌سان چابک بیشتر در دشت‌ها و مناطق باز زندگی می‌کند و کاهش زیستگاه، کمبود طعمه و تهدیدهای انسانی، بقای آن را با چالش روبه‌رو کرده است.
🔗
برای حفاظت پایدار از این گنجینۀ زیست‌محیطی چه باید کرد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/461605" target="_blank">📅 19:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc4823cdb.mp4?token=oV9F7_NJQS3SV6sO5tKWlKeta3jq5JVyX-_2m_HrwxKCenDX22iNah6Y_vJt4SXZvoex5rjilTFHucybpxdmGAl-XPVwvCARh84_a2xPh22Fifyd2HLVoMOoZmnpGaF51BeIbF0RHNZbFrPDp7XTtpJ3O8xBZhklW1N5Z1ISdlLoIl-7ahsQMERPJk5xufz9eG3uAaqK2ysMDp_VKElRzp_2gxqWEQpo3ghkjp2GZPLSh_aDwp1pxUcd29a4eGKAp39oATZ1bqliqIslFm79p6dfmXu63cb4v4X9ns6e_cvc2M_B5CZRUhPUHjH1J68UISKcUme5AHRZh0sEmIs8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc4823cdb.mp4?token=oV9F7_NJQS3SV6sO5tKWlKeta3jq5JVyX-_2m_HrwxKCenDX22iNah6Y_vJt4SXZvoex5rjilTFHucybpxdmGAl-XPVwvCARh84_a2xPh22Fifyd2HLVoMOoZmnpGaF51BeIbF0RHNZbFrPDp7XTtpJ3O8xBZhklW1N5Z1ISdlLoIl-7ahsQMERPJk5xufz9eG3uAaqK2ysMDp_VKElRzp_2gxqWEQpo3ghkjp2GZPLSh_aDwp1pxUcd29a4eGKAp39oATZ1bqliqIslFm79p6dfmXu63cb4v4X9ns6e_cvc2M_B5CZRUhPUHjH1J68UISKcUme5AHRZh0sEmIs8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/461604" target="_blank">📅 19:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZQANRrhIW32sp-lO_V9FyKxabnPS3XH4wrBiWCrSDLWADchiXMxF5W9NwULW5XqMpiKGguvMpOEvyJ9WAwPAb5qKUglqyDirb2Wzcx33GHySHhioz353ZyoLNuA3E_N1A2S7kInr7nF7uvHagnn0Pz5wfyQHXJ5WCv8BImxgpFRpKjhfPwi2qIFlZaH0UezWUu4jE5opzZ0Mk226-j--ivNzkBYa5uEGej0lKzjal2Ll_Sn82r3Yo-xnPXZs2K9L_v6pnJfbwTGYotIOCc6WNEmSX81N6-zCrXti2fT_tRYJFWAbs01TVPdgoNG3pQi79kAYjcMcxfHzvlqooeaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cThdJJ-eFFP5TlyCkupznOaXe6UVPLJZaInIPJAU70uJCe0Scja22gZAqB78kpEKCsLpmAF94LdYpeKoAn5i94eNvqr0znCaIm7X3PNh6-hP1tiGBc6zIxOQKNDm8oo1MAXhhlYNOrA9ALySp71pvzdqDOhTd1qUDgNUmUAMYiY2G7akeu7y2X0J2IVsT1MMOIwnB1fUZb1ae1J5OIFNPxdVRR5zgn_rGmX4x4uc2yJEen1iV7sw4BOKTdLHZL5WXN23HcTiBJD6n3xT_6Pb3johKa1MRJ5mfn2FdeksIJdgihL35PQ_9wvJqnEsrGg2Ke8pEL-KwiLmshdx5JeNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwHnpIzPW-f80sG4B6rEODrAgge9vuf4eILYR7QfxYuc--mC9HV7foEBEnr9W3QcIVGwXOAb9UZmka0ZXAXpvABht1Xf2-O_r5oZJVee4N02JMCeY7OsOV2nf9nFv9wo1oX2UiBsvZ61UPjH3u6EpzGh5Y7xLKYmytoNkQRxuWCX_p_tYJgp2ilcjxpp-b3-Y3vV8bIPTI8a29cq8Yy5U72jYCvgeY-n-hKFC-AQwDfW6WJu5BwlAf_6Dg5DCrGMmqlkQWkqjDh1e-mxsbviPkBcd6oAv1h1OqAL8LK6C_0db2lQMfeKgaaRwk6cJ0W8rO8fCOuYKsJbJWEJZ2nysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG16jrYNxrpZ4KAK1YWb08bI52x1_fmDjBjQy13F1QauJgcYPCjHZpqMSeb3myOS39wU_rIJS9dKYpXhGeeioi5jaYbtWKXohI7pfolC5KrrOJRCSbq69dEyfryA6wXK0DnnRAl73E6MnZjGJH_bMsTMs_M0nT7pRw6v68DgdGGZRU-Mvserx8nP-QOMv2M7GNBjn4CB5sb7-NmR_v011AUlZNWA99jI8uu-SWClbArYYHH8Zd15vQXMdh6HsUOWn4S94T2gDBk18dDKq9h4k0mJvnS9fdCWneMKbok5cptrl9iDtNXNdq9A25RnZJbjYf7cM7yf67b3ZhRB-XBuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-Q98jYbKu1Qb1KxY0G9Ej-SdmsV_YKeGCPQ00ioS56sd88S8WsFDKFdalJ56TULJH92uFbeSVnoeXn1gfVamOX_ENLCVSOxOsjG3pPROo5WpshQoS6L6qUJKhbF3KDtaPG1E6YqJ7Lz4C93dp2U8ZEzv_Xk0yp5VOIDdzMPCY-DoJ_p1KPUkQVvOW6F1sBZztuEEqHEVye31syTAmCLOyeVM6ZcHrCItJwOPnhzGabpQa8bITO4fek1yvxY5cd6EcAl0M_dOzsdEeElnqcsVCgrls2OrjXylPiW8Ln0AOpfv3WafYe5OhyLi1JX1ZQobDWdv6tGCbez9B56meT5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDYNON_-iZmK0lk-QnbLW4teMA5TFtDTqrck9eBVuIwy6N1dv0WnIDlozPmYAw8ch7hQW43yPe43nsUqklnthe9D-dfIXJA50lX16XwOFprCyRTpyouau_k9y7V8RnT6Dig-6BbZcIux955A5JpW1jt7h4lphIO0JAhKWbV00RADOFXpYHlWH8vgxu9Gpa9iiopbafK4AsF9aeM4QRhCA89PqnIB66-usymVwvP6eaS-fLkO8ZUh0Eqck0UyA8uT7QRgUS8GTDnOV7Od1dkOpkPhG_vypLlN7eSaRKjbb92jqZp_RS8lAzl-eN1XYBSl4RnXvBONxweTDzsPoqCCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eu4UfaVTf_GYmzyzGFjOICje8SxHEE_2EZ2Lwjye6CM3fgayULtL6eAY7I2328NtmyIuPmABpTbF5m--sx_J3MG-RfKrOfup-uP9TPmsPkN-ys42L7cADX6vF7dc8nS1UlTAQYNqe4ar328DDbqOjVNk9Cq0HfojjYPK_HpBgJ5zGF00oqZ0XsiDPM8reUJndFWBQAKA74pahaJWZ0iGgmuOM0silCQZ81Fp3p13c7vOnSuM61lNenfhGMFKC4QbxUFTiTnrX85vFoPSPIIZz4ge_1G6SuoP9YMaTrkWBRbMTraailCeH6q9JrzahbmhsOBVyDUzrF7nTH_cQywfdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جنایت آمریکا در بندرعباس، از میناب تا کوهستک
عکس:
محمدمهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/461597" target="_blank">📅 19:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وحشت موسسۀ امنیتی اسرائیل از تغییر احتمالی دکترین هسته‌ای ایران
🔹
راز زمیت، موسسۀ مطالعات امنیت ملی اسرائیل معتقد است ایران برای دهه‌ها تلاش کرده تا به توانایی آستانه هسته‌ای دست یابد و درعین‌حال، از توسعه واقعی سلاح‌های هسته‌ای خودداری می‌کند. اما دو حمله آمریکا و اسرائیل، درخواست‌ها برای ارزیابی مجدد دکترین هسته‌ای را تقویت کرده است.
🔹
زمیت می‌گوید طرفداران تغییر سیاست، استدلال می‌کنند که فرسایش محور مقاومت، محدودیت‌های بازدارندگی موشکی و آسیب‌های وارده به برنامه هسته‌ای ثابت کرده است که تنها سلاح‌های هسته‌ای می‌توانند بقای رژیم را تضمین کرده و از حملات آینده جلوگیری کنند.
🔹
به گزارش این موسسه، این تصور در تهران ایجاد شده که دارایی استراتژیک اصلی این کشور لزوماً گزینه هسته‌ای نیست، بلکه کنترل آن بر تنگه هرمز است. این امر ایران را قادر می‌سازد تا در کنار قابلیت‌های نظامی متعارف خود در حوزه‌های موشکی و پهپادی، بر بازار جهانی انرژی تأثیر بگذارد و بازدارندگی ژئوپلیتیکی با اهمیت استراتژیک ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/461596" target="_blank">📅 19:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461595">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173f09546c.mp4?token=kqWUDATXqqnDYh1iqAtdWucWmNlCiR_jwAY3_xqRDyIGvPqHAmsLatdD54SgYP-V4Yk9XP8PwhGEerHlyUn3H3J2dQqeAMywcWbYFBfARYkv8DBZLtkNjWPGd2sKUsMB2urpqqNi0FWlinoJAoww8mQjYQ01L5OQPTU2IVzrIcAZZ_P71fHe-Z2cLdSM_4PqpAcRjGuRUVzuMLOz0FYP34V6cpt4cKzJTuiodnym2kAYsbDWqiKq9bauD86VSfH0tgfthrDU-t5kaYIR2rwu_SrruAfcAO5lfQkLI31XRZUwPRjAd0HLus0qJFRaQmGE9MK_glR9hZ8UQNWkb1l5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173f09546c.mp4?token=kqWUDATXqqnDYh1iqAtdWucWmNlCiR_jwAY3_xqRDyIGvPqHAmsLatdD54SgYP-V4Yk9XP8PwhGEerHlyUn3H3J2dQqeAMywcWbYFBfARYkv8DBZLtkNjWPGd2sKUsMB2urpqqNi0FWlinoJAoww8mQjYQ01L5OQPTU2IVzrIcAZZ_P71fHe-Z2cLdSM_4PqpAcRjGuRUVzuMLOz0FYP34V6cpt4cKzJTuiodnym2kAYsbDWqiKq9bauD86VSfH0tgfthrDU-t5kaYIR2rwu_SrruAfcAO5lfQkLI31XRZUwPRjAd0HLus0qJFRaQmGE9MK_glR9hZ8UQNWkb1l5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/461595" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461594">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKHpnfgCghFVG6z-d9RYVYfTwAU9oPta9xNNs6sMMAwQq8_UBmXD6yL3E5j2f1nLbeGLawap0REChFL08wG852fsUFF_0zj8igCWF0poLUyOXowWHYiiIm8rQI0Zxv-vfMv2WjHG0ZpgV2i4javQQUkxXs2AGYLQ1irX0z00f_5MHoBhgA3nNcL-3X4ElqooH94tiqEQl4mG9K28AWh7C_XPziiE60YPQApj77NAHF3Dz1EBpqmk2tsgt0GuPo30Cn09HMyvMLwcjdruzFFQ3zOJ9LKDLmFaH_3EgWp59yh3wl8kp4QOJj6G0RNdnLSDI0kGGBzQMRSA-McW3kf-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جبهۀ مقاومت در کنار ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/461594" target="_blank">📅 19:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461593">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFMPrHvrROkty872bnpDyP6gHMOesApUWqR9X3OMmqNv_tTuV6ejz1IQssC_NXIZWr0F2E4PggJegM1QS3AcyZT0o6Cv-kf6-IlwJPeXxc-dsxq8718GID_tWafghGqWQMAuWT05vtmlj7udCjaNI7la9t7NiiiBUeQ-lynKwPUILRwULu73f3By4vVSMMBzp3qB0aFwSCLfCsdgdMe5-kvb3TcBsxwJrwXdsTykO7unGXyoX0gZIEWqL_ZxV9hDoKh1oBQIJCZFzowV16JI2WfPLe6GBtBOlBsP_Ctpi7x3wyoAg3YxecLEz9S8aOgIwHLgm5mMSr-SfHo7xfIOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه: سران بریکس از درخواست الحاق ایران به سازمان تجارت جهانی حمایت قاطع کرده‌اند
🔹
غریب‎‌آبادی: این حمایت صریح در چارچوب کلی‌تر اصلاح و تقویت نظام تجارت چندجانبه و افزایش سهم جنوب جهانی در آن مطرح شده است.
🔹
محکومیت حمله به تأسیسات هسته‌ای صلح‌آمیز تحت پادمان، مخالفت با تحریم‌های یکجانبه، حمایت از عضویت ایران در سازمان تجارت جهانی و تأکید بر حاکمیت ملی کشورها و حمایت از فلسطین، از مهم‌ترین محورهای بیانیه پایانی هجدهمین اجلاس سران بریکس است که با مواضع جمهوری اسلامی ایران هم‌راستایی دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/461593" target="_blank">📅 19:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461588">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1VjSDCTuI5MYSN6RV9gPgu5nTuxlgeBS2YgcGfrRH-wUX-JHDoITFkT2SpIif7kQTdmYTDV7PRFoohKMRg9aVEypmZuKviyOYk__4nT6zRrFpd951jvNEhm6CbRJa_tBZE-3oMy3h7YW2jD3AYbysKMzSQopLZjzWUm9HMrK55m4DS0i1QowJBcBRqwHSj8pLdKGtQ7U-O3Bc0oQDtCQbNXwN3ksBKIRm8civgLAhm-BR-o5UXoBdTua9EwPPouSGxskS8wB5b8keGZiI4eY5GOTjI-QVwJA5n4vw3VFyHqXDK8v0aPRlZ7hhBinl8l2G1JS66gAuAS60rQFTs1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5fOVXbgwc0OVR6BZhJ2McVxC4qnnRrGrvPTNXB5yfV1_C5GkWs-xeiEucdYNpjrb8IAUpM-F8wOs4Mw-9JJOqlm4_rS8QNopCAdCj8qEMOQhDHni1InknFBD64WnHmZVredXaDsAUY8Jh1qL49yRFUGzIfEctRiQHNH6euF9RRh8hnBxIcmu29w2TAc2YDxqeOCTbC5zasQjmPMj-eGO2DXtZPt7QjbJqFhVKzAXKeAmJHSLrzL3Etvu5PReR4s-nNv1dCJ0I3KJExEeZZeRU4TZX6EMP6Q7nMJaznrGzf3GemKJ5IQR3OsicCl6Im2HxalknMP4aLiglj2Qadbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6fICJT2qPwDaU8Fmf1Q1IIQknO5AWKXbyRQdeBkBa3tlTulBZKWd-wbqLP7XcZfjf6e5G45Q01iRVGqVUc-ngpEZqUjhczvqulJ9eO3MAkhjCpp3Z2UwZR38qOiIzKvkyUPTU_ac2RmN75DlbDs6zmbaNIGvSMkbzqc45aVhRTuGAaRCD2WEIwV0RCd2Weqm7wxHMALIuhLDeAg9uKOi3bk3vFmSrX97qXgXHvDvtQHJhB24zF6oSydSDzPSiupmhQE2-kf5LUgQWFcKbGSLiqTTd-EOAaEaf4KmH_hoHr86inDYK9MH2HQzkJJmTy61ahtNkK3Y07PGvWyf0glng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYGMrkyqGhtq78GxEAScLXKY2-4ZR1aDu-M66ClQaoiuj7TKiIRhC1YlOc_EfrETiUysoQiJ6VWWSuTxGzlgwtu_B8zEgD_oCzmqm72Zv0P2TATrUNgxbQAkriyDspkOWKCTu699vAeVoKMbo74T9JehRa6kUqA_TrDUHWzR7AOOvhL9h8qxGNLyojgvgXFbj5XCQeU1QkiN_Aaucg9z2c_rs_UWvF9vHoKbWWk6Rv_Ln570orpqheOSsy3cqcdzwVKtbaXoh3eHX0XH6Ao8rtlEtNCJ80NlfskvVHNeDLwxpgFMfVhxelX1eBpxwjAxXc1k65MGjMShgENqNdFFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SurIrjYN1VcSlALSXn_5MxF6oejzFSQRA-_oBYsonnEM8lK1Y6Pyw_GAZ18RXOOfYcDSUdb0L72Taw6bq1upHM5a7i_d8DHKDFDXj6hKGbOewZfEym-Nj0v5HGgE7oiPnJxatf-NqSyLqOuwFi3HeocsLkCV9V8mUIDlI5vmUrDvf-2N7RlHNvjIg_-FTOTgxx9c7oB_1JnkVonV6Kmcj05kRplPwjT0OWkug2diXr1OPpU6nmUrEDYLlAt2H4WNvH2rv-h1CyPx_ioUrVhqDTQLf-s7laslJrGhBAeUpL_u3D3URRh_NYf_yHgrm7fyxJM3_b5soCYuOwietCDmXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران برگزار شد
✅
تاکید بر ارتقای کیفی شاخص‌ها در بانک صادرات ایران/ افشین خانی: اعتماد پایدار مشتریان، پشتوانه اصلی توسعه است
💠
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران با پیروی از شعار محوری «پیشرانی شعب، هوشمندی بانک؛ ارزش‌آفرینی پایدار» برگزار شد و راهکارهای عملیاتی برای توسعه محصولات مشتری‌مدار مورد تاکید قرار گرفت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/461588" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461587">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اجرای ویدئو مپینگ بر دیوار ساختمان بانک ملی ایران، شعبه بازار تهران
به مناسبت نود و هشتمین سال تأسیس بانک ملی ایران</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/461587" target="_blank">📅 19:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461586">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/461586" target="_blank">📅 19:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461585">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb1af6713.mp4?token=H-YJCQhVPUSvuN7-Xw8eEmCt8jZ2QRa1CLbCm3So7CsrcQLZlynjMtiTkqfI8Z1n7JjP9NOyFfXuzvH-e2YnRJ92MFl7I3uno25CtokUPtk2w5UFeTDv6N3HF2TYG1oCeQ3GAJrmxVPAc_xMURWPI6isi7Bwl_bPEqu7MzaSv0OwW1BKRgiw1p8eEYCZzc5kZUlDmaLh0G7sBav7l4AJSEij5iXeEwekB12C-7o_VtDslnQLSXPlSVsM22l6nmD6Ger7u58mrJQV7nqJrmpyTfMLrp8oD5RtbS0vhmQ_08ywgqB3QQfpb4oLmOPLekupLh1cxSwWDj96CQna5QxB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb1af6713.mp4?token=H-YJCQhVPUSvuN7-Xw8eEmCt8jZ2QRa1CLbCm3So7CsrcQLZlynjMtiTkqfI8Z1n7JjP9NOyFfXuzvH-e2YnRJ92MFl7I3uno25CtokUPtk2w5UFeTDv6N3HF2TYG1oCeQ3GAJrmxVPAc_xMURWPI6isi7Bwl_bPEqu7MzaSv0OwW1BKRgiw1p8eEYCZzc5kZUlDmaLh0G7sBav7l4AJSEij5iXeEwekB12C-7o_VtDslnQLSXPlSVsM22l6nmD6Ger7u58mrJQV7nqJrmpyTfMLrp8oD5RtbS0vhmQ_08ywgqB3QQfpb4oLmOPLekupLh1cxSwWDj96CQna5QxB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین عملیات پرچم دروغین اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/461585" target="_blank">📅 19:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461584">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELDP1dXPLDa0Lc0hvmIlIVReFnkZsINwRW4Xoqq9flDym7aJQXfbzmNn7zXNsuQZ_P8tgh4Qo-ebaJedao5vZ5Gl8rxWow19rCd8SFEvVcyXif-24E5-edD-qeaJfEs-6bDHqX1oN9Zpd7anlXOHDB9OWUuc_yGBcvFHsZWj181ow9zEtLr7bX8ziExOsOabWelajX5w21TXTNMRpu1e-6fRdXyiohWauNrbbHKjP_qgGTOAIfILNUr1Im_nEwIOSspXFdjajqKhYnx30zCRKHQfGuz6wEK8sgtoI9RpvvlgRHAUERawcugorCNt79KfPYGZ7_S8LhRi-R1Ejyriew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندیشکده آمریکایی: جنگ با ایران معیشت مردم آمریکا را سخت کرد
🔹
کارشناس مسائل خاورمیانه در اندیشکده آمریکایی توضیح می‌دهد که جنگ علیه ایران، تقریباً تمام مناسبات داخلی و خارجی را در آمریکا تحت الشعاع قرار داده و با توجه به برتری میدانی ایران، بنابر دلایلی که برمی‌شمارد، نظم جهانی جدیدی که در حال شکل گرفتن است، خارج از دایره منافع و اراده واشنگتن، تعیین خواهد شد.
🔹
جان آلترمن معتقد است که جنگ علیه ایران، صرفاً یک منازعه نظامی یا ژئوپلیتیکی نیست، بلکه پیامدهای آن به شکل مستقیم به زندگی مردم و محاسبات اقتصادی و امنیتی کشورهای دیگر سرایت کرده است.
🔹
از نگاه او، تجربه کشورهایی مانند هند و امارات نشان می‌دهد که تغییرات ناشی از جنگ، از اختلال در اقتصاد و زنجیره تأمین گرفته تا افزایش هزینه‌های انرژی و تأثیر بر مناسبات امنیتی، باعث شده مردم و دولت‌ها نسبت به نحوه تأمین امنیت و رفاه خود تجدیدنظر کنند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/461584" target="_blank">📅 18:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461582">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌  بقایی: هر کشوری که ناقضان حقوق بشردوستانه را در قلمرو خود شناسایی می‌کند، مطابق تعهدات بین‌المللی موظف است زمینۀ پاسخگویی و اجرای عدالت دربارۀ آنان را فراهم کند. @Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/461582" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461581">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بقایی: پیگیر اجرای عدالت برای شهدای لامرد خواهیم بود
🔹
سخنگوی وزارت خارجه در نشست خبری در محل قتلگاه شهدای لامرد: در این که جنایت آمریکا یک جنایت جنگی است شکی نیست؛ تحقیقات نشان داده سلاح استفاده‌شده سلاح ممنوعه بوده و موشک خوشه‌ای که هر کدام حاوی ۱۸۰ هزار…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/461581" target="_blank">📅 18:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461580">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۲.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/461580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۱.pdf</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/461580" target="_blank">📅 18:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461579">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puafVb14JyZ5yY3Rd6gpPlT2f6ioJvnOcz3ll_05AiHbYQZIGZTZF6oqyi-DRHQa4BOhAb38rOiwCQndaDS-zVrQMId2gr7Jq7jyLUBYRrLr1oca4vM3WE4QB-nmqUdSFbshL9xBbDXITyydBzoccGUaW475k4B53bM0DIi4J75jFbMk6fQCq9e00jvA3k1xhVd_UWaAyyTg4g8r5yLRMbyu-tlwMoYK4Cl3L8uDSt2waOYVrjlpNuEyUXFhih-Hv1ls_uNvd6AlwovaNAFJtajfXNuZOEW6hpb89LQClq7__Ckk7a6K3A3TwxGSvv4hB34xt9SXfDr6aAlJVU2Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ هلاکت ۴ نفر از تروریست‌های وطن‌فروش در سراوان
🔹
قرارگاه قدس نیروی زمینی سپاه: درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به‌هلاکت رسیدند.
🔹
همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از…</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/461579" target="_blank">📅 18:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461578">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pngbso5VdP5KP_61DFOFe22rfOKhFZK4-PWNzE6BkYIMcbANucSMftxhFWGDkaZf78qBAeahCj9n3iy4Q_6gPQ4GHtzZS_6ZRI4fga2XWyXsVn2DhYWMxSpmG0hpDU827naovktnkIBeT06C5Sog1_t--rGN_DZrGptt0zj_Tamxuj-oPsa6rUP-syeesIVcW2MG0lBpxTgdGlp7LOf02EHB5hD0lOpNSP9WYw1nJVqF8AiZ1d5Pz-g3kU0Ht7sZ5rz6fGJxyH8fu3TjQOwzRmg0jgd_ejDOYkLbX0i6hrZlc3eoxBH1HYTPe2iIREWsoWOSEw9C2dVZYMDIwqlwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی ۲۵ روزۀ لیگ برتر
🔹
پس از پایان مسابقات این هفته، لیگ برتر حدود ۲۵ روز تعطیل می‌شود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.
🔸
تیم ملی در دو هفته روزهای فیفا قرار است ۳ بازی دوستانه با تیم‌های ازبکستان، روسیه و یک تیم غیر آسیایی انجام بدهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/461578" target="_blank">📅 18:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461571">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qxs7qGFA1kVEdIk5icQQ4OG-wtfI42S_u50y2IZ6bwDGQYPHf06esvYBMke10KuebYbOVzfB9N4st4FJ-eGRkuLTQiCPGTNLOuUSYpaWsv3pOpUHWH2ZR3mXMClFmOmJhgPA2G00leUW3EnsQ2mNY52kIIsnKQRZnzadjS1lk2SUTUmFhrJPmF1WyIFdS_q-mZZK9J6Exjlpk17vB4rp_lUCsRL9qjn673SlFYyzAs1LBbN1Pm9frCC5i2t29olQQ1zgw-tNQGh4NY437vR9-mypF--tHcjOD_-FO9S5FLRM0JwoBEjmOQATWPnFU6MGU5LON_i2khzFwpK8b9n0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwhl07bnNvIPS5YZ3miFCYLUJxRLndyxIbBUu_-qWYyuysBBSYyIRyYsjimiL-QEo56ETqsCBC1VZcAPuREaKilNew6zmpE2mV3-FmOYp7_XdoYIP2nH7twmcrl1yy20H2FB-ep7VBZ_VCPNI_l06FxaapimAdfe_XIc7wrXC9x2eebqiWGetRRzuXO0g5UR8-7FpYQ4EtCoM0x-dgndH_vS2bMU6UzbtXQpl5O4rtyF1yVUaXBc1zK3I_8o9ZGgLIxokj_91Zs-DnvqaRT7VIVKQtYyCqL_2yxOmyRAMSEpJ_lKkCWx7Abyiq4jZPVrSNfZoca_dFafcmiNactJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGujuCSQ6Ud7j3EAxE_my8n5Eszs_HzVODJmfs2aAflCKrU1BxCpOPS0E6jCmlUxHXIVZ9vp-YMbSb4QrRc1ql6XXvAFIBwS5mtHjbg3RrrUumQ4wxe2F_kAq99vGofsjlF2wGh5OtRt_vtep-DsAESNwTrtUKIli2PAnQFLjqy0o8Emfwf_NneXk7NPrAG7gzFrj724wGVJWblAqhwBIUmOlFmao5fyzuzbPjsvYm2-SHF-Q-n6GFk4a21SGeVhTB45ENmTDRPAntsXE5lCsoej05Z2vUU00R17KxuciKsEAVC0JXDJs0XXvAQjdOyqOLENKYvZcoGf06AXkxuttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i37G55d6PLw_Wci-GXmj80YMXr3s5GylCSwP5Ua8LjoGqtpRV5nsINynIMkWteXC368y3ORtapriJB4Oj3lp-a0JllT7wgI3xdFrPSKbiUj-Vt_HFbgHv-5H1IpdmXFQv_ETK2g4TN4QrMdIL4zMj6cZmfzoUa7qxjVYV7z9J3BD7x3zPdNJZAQvJ11pUOmT30qqP9cZzq8t3sg-NzVWGAD8NauqaLCFlx98UwD1syTegn-IetCa3Mmer7ChHsoWTZmbAon2x48SQRa_CLC3Q5z9YznH8gj9danBaOhl_mIdszQVcf8lR0_BB4rO28kNX4CISRPtzCzTar3uYT9g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfZjLA0GnBpOymCyUvxZ-eNlN9ydvHxzWRRhFVhH3N3ZtqHsGsqG7uPkNgcJ1xYqB8IfjAS-LYMcoYNAbO9OVVjkdNJtnTOkIAg4chxpolLI015V9u35BKWIOkfT9VLT6Z9cg1A674j8oS96dQ1hjSjGZaw6aU4eH4NTlXNLfIV6G-Wp_GKvt68zmG3qsnuWP_cL19kPbj7mcBcCzb6iFSVJI0PAliMpTALgss8lN2vTd43cZ8MIuSUoqTqvhjoR3dKbtK42f-SN-j6zUP_xE33k_NkiniAaTYGJAycmM3ftAqpnV6fmP8_tDgVuzPq93MSkNd5WVmjtrInltR0e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cc_-QW_4CwSky743miSlCuu81Qc1hLLb749IBeNNyZZ4g17bavHt-BjJZKsIbw6Bjs38VomcvveeYvbAaLgLuZtah1104BI8s33QENd8UL3i80aAY8_JsEsrvJbuYwo3RSm-ndy463CW-7Z9LoZN1peAeMf0KwUDl2k4mPLNAi1_222fd4urjpITkys5Id77hUPCEWdzRZCdyZa35p0lYxvavS-NiSR9mRuq10XdqtUXKtr7Bay5mkn_Rbyo5dfXkXwO3XXMxTPwtca5QDAzNNw9pSwIV-QbJRuJKoOkoAYLwEjzTbXb1jyyAP3cLz-1F8GlM3CbQZuY1YaZvGPU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACd6Atkv--g9L5owcZwdGcBx5XEBgF13Ke40uVODSe2TPV_2PGPkeKLvMQfdjO3CVy9kfWHC1j4aBkHHnkRBlJ23RYIOlyl7-hU9p3-cImBBVA66M2GQ1bzY4vfd57lvoQkSJvtXP0hk1cCkrCiuPqYtvXzx_-0EFzBCaMb_wo4Fjj6PPPYc0BxR3g4BpJw8ANFN7VZMQM_1LCgnD_lCOVaNHs0-Uhke2lZjdhaSKwKjX-bnbvX2WkTUjOYd08gKo7Em3MyEl6x8Lbe_Bm2yiqL3HTt0tCom4fZyIN9TbYP8Gite_t3PDNuO5vGk9ve5hoVKapu15zH2mqj_VyAPWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بقایی: پیگیر اجرای عدالت برای شهدای لامرد خواهیم بود
🔹
سخنگوی وزارت خارجه در نشست خبری در محل قتلگاه شهدای لامرد: در این که جنایت آمریکا یک جنایت جنگی است شکی نیست؛ تحقیقات نشان داده سلاح استفاده‌شده سلاح ممنوعه بوده و موشک خوشه‌ای که هر کدام حاوی ۱۸۰ هزار…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/461571" target="_blank">📅 18:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461570">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqjVkrTjoEjPSQRzb6SZXozHonARmbjqo5wMBEtT7Z2Sm0vTH7ok384F6fAks54WnFQbZ3O1idT7yPsysLDfu2ki12irbCYHELZhxQCmMlRYoLajplrnfEOjQnvjDrXHNWa593SZUHgWvi7ZAK6iEGA1hLOVEMLPVyAbphC82-s3Z-Ho5HvE6YMv0LSNl5hWaizAbfl2V1RyOgsjKr1nlc_0uAA6xZiT2rgWr3lxpdUFDSE7ZAtcEqp35rWjVhh17KifOXRM6fkdWK1jxHug8p37axWutx6saBpkR6AWkQh2B7l4o2m-hCFeVFNLopfA_3CO1Z_xQf8bdppGsoY0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاوروف: زلنسکی برای مذاکره با پوتین می‌تواند به مسکو بیاید
🔹
وزیر خارجه روسیه: آماده مذاکره با اوکراین هستیم اما روسیه در زمان مذاکره عملیات ویژه را متوقف نخواهد کرد.
🔹
رئیس‌جمهور اوکراین می‌تواند برای گفت‌وگو با پوتین به مسکو بیاید؛ این خودش یک حرکت بزرگ به نشانه حسن نیت از سوی ماست. چون زلنسکی فرمان ممنوعیت مذاکره با روسیه را لغو نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/461570" target="_blank">📅 18:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgL1bvv5mYxSKw6EPB0Dlp6L3bvzE4gBRBLaJJGiAn3Mt8mowXxJ3CfPLQLiWfiAdvz0DnN7LAVbary19SBXqxYovVC_3OScuhNmNtnz44NoSxXi6s33YsGX6RVQ6ZG55vWB_v1sVkzzjuhcRd8KM2Ac-NhRpu5dj6r3FZqTnFKm90N3lAdtwxXhmFXc1zqKOIxj0rWrYNk8MZJw89716KLbRCIdZzk1VMD836kx2DkivLxuIVyYwcNhsHn7BUtjSfGFAb8APVqA0rMEpq8vG4XQkpSEZ2AWr12uPkIti9pn42eDg3q1twtLABXeAiN_qAyK9Vkoa6RQ_CZWyFmyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: پیگیر اجرای عدالت برای شهدای لامرد خواهیم بود
🔹
سخنگوی وزارت خارجه در نشست خبری در محل قتلگاه شهدای لامرد: در این که جنایت آمریکا یک جنایت جنگی است شکی نیست؛ تحقیقات نشان داده سلاح استفاده‌شده سلاح ممنوعه بوده و موشک خوشه‌ای که هر کدام حاوی ۱۸۰ هزار ساچمه بوده و محل‌های مورد اصابت همه مسکونی و غیرنظامی بوده است.
🔹
چهار موشک در فاصله ۳۵ ثانیه شهر ۳۰ هزار نفری لامرد را داغدار کرد؛ ما به جد پیگیر عدالت خواهیم بود و از هر فرصتی برای تبیین این جنایت تلاش خواهیم کرد تا جامعه جهانی برای مطالبه عدالت برای شهدای لامرد با ما همراه شوند.
🔹
آوینا، شهید ۲  ساله این جنایت، نماد مظلومیت مردم ایران در جریان تجاوز آمریکا و رژیم صهیونیستی بود، ساچمه‌هایی که به بدن او اصابت کرده بود چنان عمیق بود که بدن او را پاره‌پاره کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/461568" target="_blank">📅 18:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18190f11ba.mp4?token=RM_8KpjN7YSzaCF2PgKdo8I-JG8dqf4H9FRd7Ss7pN1wmpgC6ciI8kOTCmPUwdKsI9gWgCP7EtrdWGW7zyxu7w1kWeegNuX8LMQBNhowXhGOOzUvlBS52H3OgbBW1SgH0nuN2mEqQMsMGxFLq8ZG83AQYwW0cEmC4_7Xf2fZoyjMXg0JclZevoAKdSg1dj_ckBHsd93S5PaRIHIjE4l65jjaAliMVNTts16u5YKQ3FNtj-aggE5ID23wCE2qCEeuMDX9fQ5EN-b93RpucViecEq8wPjebGJrSJfF3cbadGFmcffQncJv6Z0oeaybVf8dJKl4aafe5Ki4smvUGn8Pvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18190f11ba.mp4?token=RM_8KpjN7YSzaCF2PgKdo8I-JG8dqf4H9FRd7Ss7pN1wmpgC6ciI8kOTCmPUwdKsI9gWgCP7EtrdWGW7zyxu7w1kWeegNuX8LMQBNhowXhGOOzUvlBS52H3OgbBW1SgH0nuN2mEqQMsMGxFLq8ZG83AQYwW0cEmC4_7Xf2fZoyjMXg0JclZevoAKdSg1dj_ckBHsd93S5PaRIHIjE4l65jjaAliMVNTts16u5YKQ3FNtj-aggE5ID23wCE2qCEeuMDX9fQ5EN-b93RpucViecEq8wPjebGJrSJfF3cbadGFmcffQncJv6Z0oeaybVf8dJKl4aafe5Ki4smvUGn8Pvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کابوس نفتی عربستان به حقیقت پیوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/461567" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ هلاکت ۴ نفر از تروریست‌های وطن‌فروش در سراوان
🔹
قرارگاه قدس نیروی زمینی سپاه: درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به‌هلاکت رسیدند.
🔹
همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/461566" target="_blank">📅 17:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCfrvmdZgku0nerZd5jVEicEhrWB1H7Yjgb9RyLZdgjHwtPbpzJeQlmEOi7slwWE0qstDWXepeSLqDzFXJ-gFKQtK6NwGMZy0h11ZprAggOp1dRaVdTWXcXWkmtvgRxC07q2uHXlh8DGBrzWW6Xv3FhLKgoJNZeEmcdNxoU8usZe9av8vam79xdY8mhm23iHAjm3HnvCDqVlyVIMgoweWFHZbE6rQLuPZH62ZUz0mRRFt2wKcDTkNZwxV75VUaQZME5CgHvjBhSy6DJvJgXq8JXkyJ4x07QjTqwbsAt1R_1uCqVKXqSXJlxPbYkjbeyNg1vQf9Tx6O6M2c-VCvUFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر دیر آمادۀ ورود نخستین محموله خودرو از قطر
🔹
رئیس اداره بندر و دریانوردی دیر: بسترهای لازم برای ورود نخستین محموله خودرو از قطر فراهم شده و خودروها پس از ورود، تشریفات ترخیص قطعی یا ترانزیت را طی خواهند کرد.
🔹
همزمان، صادرات بندر دیر به بندر الرویس قطر پس از وقفه‌ای چندماهه دوباره به‌صورت منظم و روزانه از سر گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461565" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🖼
سخنگوی سپاه: پیروزی‌های انصارالله در ساحل غربی، روایتی از یک پیروزی الهی و ثمرهٔ سال‌ها ایستادگی در سخت‌ترین میدان‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461564" target="_blank">📅 16:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شایعه توقف پروازها به عراق رد شد
🔹
سازمان هواپیمایی:  تمامی پروازهای کشور به مقاصد نجف و بغداد مطابق برنامه در حال انجام است.
🔸
پیشتر شایعاتی مبنی بر توقف پروازهای ایران به فرودگاه‌های عراق منتشر شده بود که سازمان هواپیمایی می‌گوید فرودگاه بصره، یک فرودگاه نظامی است و به دلایل مسائل داخلی عراق بسته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461563" target="_blank">📅 16:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpdXG2Egyy1W2YTWpw5bI_h_fAvdqqvvLkefjcz84j6OHJAbjxk_0mj8BEbBSZIRYPM3q3hPLCCYjzmUmBv9DWemSiG6v9I5FpqfZxO1Yx7l_4Qi73cyi_wWRUWaHXprb81P6qc3FFO9102ysIvxP74q0fIrpd6la_uj5XlxUP_83ScXdEb2ysmhuaGlMn_ES9NjunnrY6aAJyLLcXeYma4-0ItLVdkLemeiYyA75yKOvJfuyFsujAsDcAvt3hiie2LlsID3VlLgJ4OFJz-BbTERzrGWWDNUkui2ASKNrr7HLn37MbTOTZgB4lL1QB2u5snHcruegQxrdn5dDYIAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: ترامپ تنها ۵۳ روز فرصت دارد؛ نباید با صحبت در مورد گفت‌وگو و مذاکره به او پاس گل بدهیم
🔹
منوچهر متکی در صفحۀ خود در فارس تعاملی نوشت: هم‌اکنون در حساس‌ترین بازۀ زمانی جنگ ترکیبی آمریکا و رژیم صهیونیستی علیه کشورمان قرار داریم.
🔹
ترامپ در شرایطی که با استیصال در جنگ نظامی، نگرانی از شکسته‌شدن محاصرۀ دریایی و ناامیدی از کارآمدی تحریم‌های اقتصادی روبه‌روست، تنها ۵۳ روز فرصت دارد تا فضای سیاسی آمریکا و نظرسنجی‌های مربوط به انتخابات کنگره را به نفع جمهوری‌خواهان تغییر دهد.
🔹
ترامپ با تلاش برای پایین‌نگه‌داشتن قیمت نفت و القای درجریان‌بودن مذاکره با ایران، درحال مدیریت افکار عمومی و نخبگان آمریکایی برای پیروزی در انتخابات کنگره در ۱۲ آبان است.
🔹
پیروزی متجاوزان در انتخابات آمریکا می‌تواند به معنای ورود به جنگی تمام‌عیار دیگر علیه کشورمان باشد، اگرچه نتیجه‌ای بهتر از دو جنگ قبلی نصیبشان نخواهد شد.
از آقایان قالیباف و عراقچی درخواست می‌کنم:
🔸
در ۵۳ روز پیشِ‌رو، به‌هیچ‌وجه از تعبیر «مذاکره» در سخنرانی‌ها و مصاحبه‌های خود استفاده نکنند.
🔸
هیچ گفت‌وگو و ملاقاتی با واسطه‌های رسمی (پاکستان ، قطر ،عمان) یا واسطه‌های غیررسمی دربارۀ جنگ و انتقال پیام به دولت آمریکا انجام نشود.
🔸
برگزاری نشست با کشورهای جنوبی خلیج‌فارس، به‌ویژه دربارۀ نظم منطقه‌ای، به پس از این بازۀ زمانی موکول شود؛ چراکه نتیجۀ جنگ، نظم آیندۀ منطقه را مشخص خواهد کرد.
🔹
ترامپ با اعلام منتفی‌شدن تفاهم‌نامه‌ای که خود امضا کرده بود، بهانۀ لازم را برای چنین تصمیمی فراهم کرده است. مراقب باشیم برخی به ترامپ پاس گل ندهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461562" target="_blank">📅 16:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hupfm0BEykoAPyOLHWv_Wa1_2M-0TBnawA6aHqHfkmYibY-zTw6ypiIybzGg33WfWURUylOSZVuSMBgm759mXm1mCQuvL5xUN7SuBSoAsZPXMGDgpw-SBgbpWlUF0kswGLH3g4xPLOAMYXzTZpnCLG2kBgxaUQOYOAHsKD69PLXN-4uytV-Zj102Xy8vOqWegYlW-4MJkEwUUNSIW56X2jU7hxV6lMmljK8izyGlqNPB8cE1OZN1yFNa6vza2mAF_l9OxmPmD56Y6sjju8nJu34Dfx6KUs8un-GLbqsZ8SHRLi6BCU5y9eVFqZ7x4Zh5NMXXhw8KJuUecBnKLtcYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh4OOZJoBqBvq4RdRdtPPyhVS1dx1p5Yn-eqvrusNFV94G3OU3Qxhgt7pM-69zGAZqP6ZBPXiFsOLu9YPkFvoX5ugDdgKrYL7zsOBAFcw4q432MhDsn-oRVr6p5c96bcjcgin-oXhkLTXtYkIstlzPqTMfAWqM7udaKvoxR-glw5_zogOi-bMb7GobWeq1pqQePDy9XUNdv-giSnIJoGHqgbcybB_2AGKeN6TaV5tiHP6NNpk1iJnJyZ3K3Qb7voglI4GsK9HhhGhCSnRkjW6nerytdU7JwUlpviny9V_zVh5HQw6PvIYvHVmjypiywrxawREFn3bvvaJPpYKvUeaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گفت‌وگوی سرپایی عراقچی با همتای چینی در حاشیهٔ نشست بریکس در هند  @Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/461560" target="_blank">📅 16:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj8DpQKMAf55PjJXZMBSBu3dlW2eizbzGO6eKesZPEicINHFGnDvlECDWwQ6BNPViJ0LilROH-K9ykwC0WOKuf8bcRYp1IwEMktkXHXSMTpXN2twaxzVERG8FJn0aYEGZonszvfDmanHeJRQue5TUTgswlUxRQDidvK9xn31QxXoFqQn9JNbY0C2MZaceNIKBFTcx8crogMkVr2KcZ3GyZDw0oqnno9eC960j4rGeZ_-t83AodQhFxa_fqjkxXJc89p7Zjj1Go30a2susevVXpuioH7paVn6MmfNBLzf4VWeNlBYC6gaF8A0ecighOPpbBk0cFJ4fYJoOwKI_jMQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترافیک سنگین ایستایی در جاده‌های شمال
🔹
پلیس راه استان مازندران: درحال حاضر ترافیک در محورهای هراز، کندوان، سوادکوه و بزرگراه‌های استان در مسیر رفت و برگشت به‌صورت پرحجم گزارش شده است.
🔹
در خروجی شهر مرزن‌آباد محور کندوان ترافیک ۷ کیلومتری ایستایی رخ داده و از حوالی ساعت ۲۰ تا ۲۱ مسیر شمال به جنوب محور کندوان محدودیت یک‌طرفه اجرا خواهد شد.
🔹
ساعت ۱۶ مسیر جنوب به شمال در آزادراه منطقه یک البرز به مازندران و پل‌زنگوله انسداد انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/461559" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461558">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El53ks8LEPcw4MhOpkQvHy6d8W2EjM37lA48eSzRLl82CCb-b2lNQgVFQ3G8RnVS8onqojIqx_3yKPs2ZbDZOMXkr0iHK1WCf3BAF8BAMQ4ugT2AzA2Q7EPGuTigLFYY1GyfihS3ugi_iPMYKn4s23Ur_liPfnWtaX2Jc1m_CDFCZdiJhONKTBRhD74JMSSKBqibKyClfoEMuaYe4FNdVJyd64llasw2cgHWEkMhFtKru978o0XctKVVD9CmsjOiocjviLRmdp39IjGp4Lw0p33MFl-NXoCOe0ovDFpckKdzWaelxtWghMPWpHYik8lOU9FGBseMdHuLa5Zdavnm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم هزار پروژه‌ای همراه اول از بزرگ‌ترین افتتاح ارتباطی کشور
🔹
۷ هزار و ۹۴۷ پروژه ارتباطی در سراسر کشور با حضور رئیس‌جمهوری افتتاح شد که یک‌هزار و ۵۰ پروژه آن به همراه اول اختصاص داشت. این پروژه‌ها با هدف گسترش پوشش، افزایش سرعت و ظرفیت و تقویت پایداری شبکه اجرا شده‌اند.
🔹
راه‌اندازی ۸۳ سایت جدید ارتباطی و توسعه شبکه 5G و ظرفیت LTE در ۲۲ استان، به معنای تماس‌های پایدارتر، اینترنت سریع‌تر و دسترسی مطمئن‌تر مردم به آموزش مجازی، خدمات بانکی، سلامت دیجیتال، کسب‌وکارهای اینترنتی و دیگر خدمات آنلاین است.
🔹
افزایش ظرفیت شبکه، توسعه زیرساخت‌های انتقال و توزیع محتوا و ایجاد شبکه مدیریت بحران تهران نیز تاب‌آوری ارتباطات را در زمان افزایش مصرف یا وقوع بحران تقویت می‌کند.
🔹
همراه اول با اجرای این پروژه‌ها، توسعه ارتباطات پایدار را در نقاط مختلف کشور دنبال می‌کند، ارتباطی که امروز نقشی اساسی در زندگی روزمره، اشتغال، آموزش، اقتصاد و امنیت مردم دارد.
@mcinews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/461558" target="_blank">📅 16:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461556">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcAM2vBJ-l--xq7opzkSrOs9bRs2RC9ocoLFYPtNwW_11mYqFxsAvAmBPPGfpiHYSg5wNuI3c7ulKb0mu8I2L7dNP95W3RrBEP8_GbeCwWtU0lyjxG9lrNfp-Ucd5ON3aEKasUWlcK7kajNZpmXnifzD92JCWoqYhjJShlJupxPBzu09bDS83VwOxWTgLd4HNtlk1TdIwmK671hTXbvShmWJQDBJmsqtiwTQ-qJJVAbS2RDOv5VkJ_TIF3TzjGKGq99AaZqHHxxc-uniZ9IPwofxO8D0EFDe_fnmzibK0mm8JrcI2RYdfMDRX-SuyFD3_vWUIVj2CFfT1AaPvHL9Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iG_Plgbm53MJzfb1Xh2m4MNLWRYISQu6bUJQD4CoVYn-LscUwSLocsvV_C7DDTcCq1yCql_0OXOpK_37wGGjXcIgXykViDZelgNYR5WuWH52mQ4bbG51M3Uu0oqhAcPNkeGdd6rQ3FGQ2asuwBE3n_AFGKGcnhx-7uwHhQq3EZx_dJLVKsMfNriMjO4HszhSzz6EomK8VHbPwcDAK0xJGMA_DHJig436FklHEdYvcFHuaTQmLk5ON_UJitcS9j7SgIp3ZrQPQKjn1Ji5t9u6j0Lnt8FdHGANz353gIx5RTpCz7838zeTsLbXTa_0_xrtLCBFGr1AZ97bx246cAEdag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
نصب تجهیزات فرآیندی و سازه ۱۱۰تنی در ارتفاع ۷۰متری؛
🔰
پیشرفت فاز۳ تغلیظ مس سونگون به ۷۰درصد رسید
🔻
پروژه فاز۳ تغلیظ مجتمع مس سونگون با پیشرفت ۷۰درصدی، وارد مرحله مهمی از عملیات نصب تجهیزات و سازه‌های فرآیندی شده است؛ در این مرحله، مکانیزم‌های فلوتاسیون نصب شده و سازه ۱۱۰تنی پل گالری و بریج شماره۴ نیز در ارتفاع ۷۰متری با موفقیت جانمایی شده است.
🔹
عملیات نصب تجهیزات فرآیندی پروژه فاز۳ تغلیظ مس سونگون در حال پیشرفت است و تاکنون مکانیزم‌های مربوط به ۹ دستگاه تانک ۱۶۰ مترمکعبی Cleaner & Scavenger نصب شده است. براساس برنامه تأمین تجهیزات، ۲۰ دستگاه مکانیزم مربوط به تانک‌های رافر با ظرفیت ۳۰۰ مترمکعب و پنج دستگاه مکانیزم تانک‌های Recleaner با ظرفیت ۵۰ مترمکعب نیز در ادامه وارد مرحله نصب خواهند شد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Tn
@mespress_ir</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/461556" target="_blank">📅 16:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461555">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/461555" target="_blank">📅 16:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461552">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnOQ023jacLmquLBTDsObC6PgTrwqocIsApuKMNwG-nsMGi6iDUSEVUavm-Byc260177WT28DZnSwuuaChSY0k-IJQE9wXZcK4-IqjEcsibRrX5KNtzCCryZgGwi99etFgo-CZL6sKEP9OXubXWFLH79rlo3RYE5_h5etmcvFegq48cap0Ru8X2oshxobcoOawD2K0qvwDmf_iJ9UCO0eNd7Le_jUo91HecHX2tZ8MATApHYwZdxvfP3Di8Fxv4aVE9wTwGk5oWW_CyQSq72Cmi71fY5xldJzqZKgukK0dsgOhKejUHEbuwDfFUmvVtXnTpzR-7e0HzjNMX59gUzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj9LrGibFq0Mk1K8cKQm9WYNpoHEgTUg9nsZEDnvAqLg9-bWvv8K18Uze6yGs8euVHYoPav32ifdXDG-1fxXjOoRgFG-7yTl21h__KlJypYUj6NPQtc-OPNVHFroLl2MJDCBjaY0sb3jhymjdAodWsVOZylHyln2TeAtx0MgiL3_NAYKdITffOnDoEX61uD2KjtVcvEA2oSO3VEpnB3mG9ZQD7Dd8P4ooop4ThQ0wrteiwBVB51Ll-yxI2BUWpKmN2OQcYzU2gbNpO8fffZ9yXU6KLtFZPknFvMjr_-y0P4LuqqJrmeqQjrtbWWijHZ2dN5h_8oCNWYyLmIB3T2Cvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyP1tFMt9w67ZSyrtHNQmHUP_87ddIjzhz80zezMU8Y_9PQHofLEdQxuq9yyuX6wyQZ7Jqbu8u4HkPMv6MgD_jrP0yZihEgeadUuw-V3QH2s_SZNBhRIEKbabTsHfQUzTnpLv-DcBCg0RbD9PNToy1XHBXqdlGGdlc25EmL5wK4wUfYjHBsVVfF50VuDe-ryPpOefp3O61d8CcoWWU_tGTsXj-BvYDfvBIOj2raXLjZmpB7AmYAVkuZRHbEBggnYfImCSxdwJnt7EwPxuc7uehaIvDgdYvnaEHRwKMuegyEIfbBJGJ0LQz6DGe6vENOJ0jAQ-kbUMvD4ueeSH4hkuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان با خالد بن محمد بن زاید آل نهیان، ولیعهد امارات دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/461552" target="_blank">📅 16:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461551">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpqE-7akiv5V4Vt7lT6mXAVdl1KaSQilY5mdOoRmmTsadutz409nIKI23idfe5CTP9JjerCJhnsiXlKIYcq3bCQp1pVVnQzSThvTkmR2lhhizOw3ZmkRd1B-zfWz2WM84Wpg9f3wpiE9aI_R2J9U98aSKaB1KRsf4IvukLW7lfpLgoG_GL3xKzhVC_e9m3Kv0uEKYmOcfy6cW8LsXuPtFOBc1Vafb36MSBEM0bvtVVFyGvTbPrUD79GmZCxH3azPClo1LM7fIO5CJfkrnmXGDk37Adn3o3Iyd2KoqQCM0cIGyiDmNQUjtpU-b8K3007hgD2_W8Nq70cGjiZSloJREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت اطلاعاتی آمریکا از عربستان در یمن
🔹
شبکۀ ای‌بی‌سی نیوز گزارش داد، دولت ترامپ در حال ارائۀ حمایت‌های قابل‌توجه اطلاعاتی و کمک در زمینۀ شناسایی و تعیین اهداف نظامی به عربستان سعودی است؛ اما فعلاً برنامه‌ای برای انجام حملات مستقیم علیه نیروهای انصارالله…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461551" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38b2b245b.mp4?token=UocOr_GonLcZ4L7rWe-Kr_BvPTaF3KAyzHHrw-IAgZbi7nR_UEa7ZlfP_qb5lywRHH_cQD_K4dg0LbfN1G2KmhMvZ4JAtoXqv_gVS9MnK4t6aY9wtRPDKPMLgDCPLnsFYTnhOliHLDnj5ww_pKkUrCQPvJtIFDpH2T15BqW33S6ESUr11uExLcJlVpZ_L-dwSYxP1K5Spw_gEfOp60kQucmceLPZT8H5Z3xqrcLbm8GUPW1S-fC7F58BgpDto9lw3q-T1e56HK89YMuji5X1Zq7PtjUpcV07OQ-k4CZDIM-l5O4HbmLFQ6xAaSBDuj2xuy3ZEUAZT7KZCZqnEIn9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38b2b245b.mp4?token=UocOr_GonLcZ4L7rWe-Kr_BvPTaF3KAyzHHrw-IAgZbi7nR_UEa7ZlfP_qb5lywRHH_cQD_K4dg0LbfN1G2KmhMvZ4JAtoXqv_gVS9MnK4t6aY9wtRPDKPMLgDCPLnsFYTnhOliHLDnj5ww_pKkUrCQPvJtIFDpH2T15BqW33S6ESUr11uExLcJlVpZ_L-dwSYxP1K5Spw_gEfOp60kQucmceLPZT8H5Z3xqrcLbm8GUPW1S-fC7F58BgpDto9lw3q-T1e56HK89YMuji5X1Zq7PtjUpcV07OQ-k4CZDIM-l5O4HbmLFQ6xAaSBDuj2xuy3ZEUAZT7KZCZqnEIn9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی و بازیکن خارجی که به استقلال نیامدند اما پول را می‌گیرند تاجرنیا: با کاریله و استراندبرگ تفاهم می‌کنیم  سرپرست مدیرعاملی استقلال:
🎙
کاریله از ما شکایت کرده. درخواست مالی او از ما زیاد نیست. می‌خواهیم با نصف مبلغی که می‌خواهد توافق کنیم. با استراندبرگ،…</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/461550" target="_blank">📅 15:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461549">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db67df5f5.mp4?token=CrApSV1xgjgx5W0ZJesbRvdY_uubARUe0X28AxXkOiUGDVglifDibNi4WwxfyiV2BWfSfveDYCPFlYREYfBodisCYCopNOTOQD6hRdJ6PVHJwAKXnanMcpuxJhY-rsfk2SPzWX2maXt4azF4EgiDnMLn4cR6cFmXnEBe29Ln2xWLnlNVSO3yEJgVS0KpfiPQ_47LsV13KpDXGk2UOWnGKA2kQlQpYx4-cmbos2z6c6hcgIHPbFXrBJ3SlC6oJSGOaoY1K9Gn3viVcmc5_mCkg846tPnNj-KVv0ogIjvgqAZDrpFVIv-mi2dM4ufCGYZB5RPXPigetQWNAU3QYWpK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db67df5f5.mp4?token=CrApSV1xgjgx5W0ZJesbRvdY_uubARUe0X28AxXkOiUGDVglifDibNi4WwxfyiV2BWfSfveDYCPFlYREYfBodisCYCopNOTOQD6hRdJ6PVHJwAKXnanMcpuxJhY-rsfk2SPzWX2maXt4azF4EgiDnMLn4cR6cFmXnEBe29Ln2xWLnlNVSO3yEJgVS0KpfiPQ_47LsV13KpDXGk2UOWnGKA2kQlQpYx4-cmbos2z6c6hcgIHPbFXrBJ3SlC6oJSGOaoY1K9Gn3viVcmc5_mCkg846tPnNj-KVv0ogIjvgqAZDrpFVIv-mi2dM4ufCGYZB5RPXPigetQWNAU3QYWpK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در قضیهٔ تراستی‌ها و رفع تعهدات ارزیِ آن‌ها، پیگیری‌ها باید منظم و مستمر باشد
🔹
به‌هیچ‌وجه قابل‌قبول نیست که یک تراستی در ماه نخست ۱۰۰ میلیون یورو عدم رفع تعهد ارزی داشته باشد و عدم رفع تعهدات همین تراستی در ماه بعد ۱۵۰ میلیون یورو شود. از سوی دیگر،…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/461549" target="_blank">📅 15:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-d-uEZOnL1FTz95kLlzhJauRVcf24b8RrLWEDyIO-4DPmq5MuLDzbftV9k6WGeFpEYq5eaWoATX1XvAOPNKySsS5a2L5TpOK6TDJKU6OB69iTkzKYxhB4pxGWt_MrLrBlnOwnwTGuw8US-3EkG3oSkSvjR5Bv395uUu95axBtNqtUYB9uXbni17VMEIhg0Z4hfm-SE2rSPBQ7sHnt0sHzoFBAEc93mVzs0Nc0auYyG7V-9z-c0bMBwC-yTVPgkK0zQsF289o_1yBW6yIU_Vos1XbyNJdvpzkyyDgrMLMQz1rRXk6-AGUkHtUZHuSlUkFHCFbB3cnBsGgOQ-dnYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بنیاد آیت‌الله رئیسی از ادعاهای کذب یک بلاگر اقتصادی
🔹
بنیاد شهید آیت‌الله رئیسی از یک بلاگر اقتصادی به‌دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد.
🔹
این بلاگر مدعی شده بود در دولت شهید رئیسی از او خواسته شده مباحث اقتصادی را به رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/461548" target="_blank">📅 15:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic2N0EY1lTLk3XmORRCFfYvzEFNTU7dKLU0sSpuxFunUilKQHyt1itQVdA7TExURlOfHY5boKYQEDqU8kP9zbkTejXkM2axu77vPRCw4XgbxflIFhkiOZw6G_Bxzd1ojBuTk-GxjRsqPP6-1ADuYMCDEPZyQsAMnx2yE-5hKXaRZ-Efxtl2v1pDDdHuwVZiqUYVt7xZBQHOG5LElUp_gcq7z8fPQ2v6bYaClAJGWRvcQbBnzAPTaHVNmca78QgM0PNmY2QBQyXc_aT7qUwSdWVQFOC_7HZUwSpGySFksxv8sUArs-ma255RY3FZn4Fj0f6UFcATC33Tz19anDKStSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qdde5ZSa-KKkTqtjU5Fnufdr0rUYTHodv-veE6vHNZlZbwkjLGfQq6taw5IGKyky3im3wnaBcnKWrggp9boa2vyThGkVN0hILJb-QPNZ8rlZOGjAQadSQZrKYtIFujSEJuUHHoE0fyoAbuuIYKKLV6qO5sD5QtH9ND1PvmNNT2L5utms-jiaIiGhJkUn2jnALSxkQalYZY5q8p0x1jvDngEM_T7EoIG5-KokJIkfE-tHqNhwvSicN51V-sD6z_eKy3ELV_E7JyOjh88DIqVHHdYAqAqNT5Y8Si6pLMiWZ61UJkskU7B5Y3gWlVX-m42_XD6CTzPQc-uCle4NFn46jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h57LwVLFaEn0uMFOKUv9nAAycnWWdGtzGlvo0jAQLP3MI0ac1zOvwv_ZpNJVN7xlP2W748c6LkJK4CwGPNUJ-qq4f2_xVDQpVjgSxw-Azj4W861-n8-0g3tFLVOrQUb6WYydyBnYpfBzuQ0nSNBDkwuDzggfDgslitBrevn8we_Ewq6U_s_SUcvNXPI4I5rbF-RRL8HoleMgZwMY5GVKw3qCBYrqN_NUfJS3mHPVnrm_ZDpwAOfqeDmA3b0cmcxP2rEuct5eDTa9h5GA_DIr3O9_g0sTVDYXBSz7rr94HOibpQGndOi2m5uYiSABaiBig2aqKmBvm-qi8UE8kYIpUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گفت‌وگوی سرپایی عراقچی با همتای چینی در حاشیهٔ نشست بریکس در هند
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/461545" target="_blank">📅 15:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461544">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اجتماعی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-DPjZFGQTSpy6ddeyYr7yo621UXw3nFZ5VYxxrcI2dR15PKZUTPOM0UafORb7_zxPo0lcjyCQdOt26nMUdOM97VqtUbzCosZIerkDNFiCl1TCfOhix212U5AUvlv1VlfZXMA1BmnzggWFnLKeijcTjVJA4-FiehDn6qSF9abhuqDco2g1dDmEtGj-iL1a4pKaMIgsUSv-LbN9rqAM-k3C79VsNjJ_9wpqfaEAvrpna84HokHN42OEMlykicQg2KODYYVcKlCJVcU_rMkBl1D80hKWVgRfRuJLGCg2j255HMLlUx9JvH__0qjCmZDoWVGEQ4DY5EItCp7yg2NPVe4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال سیلاب، صاعقه و وزش باد شدید در ۸ استان کشور
🔹
سازمان مدیریت بحران از احتمال رگبار شدید، صاعقه، سیلاب و وزش باد شدید در آذربایجان‌شرقی، زنجان، قزوین، تهران، البرز، مازندران، گیلان و اردبیل در روزهای شنبه و یکشنبه خبر داد.
🔹
از تردد و توقف در حاشیهٔ رودخانه‌ها و مسیل‌ها خودداری کنید.
@Farssocial
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/461544" target="_blank">📅 15:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461543">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fad3da36c.mp4?token=eAg8QFomTHlEapFr1wPJG152uH3cyYR6_yvCmkg2Fjt9fxFTEei6EMjxWb9gBnr0vfyRJe4pn-wPR31TL79nJRH1nzS4_KNb_WZ9fliiXozuIMKWIs0NpkNPUCUy6hnacOUJqZkZgNpwiceEeB2RlerxVPPRmVu-SGGmKOlpNvVFGU0eu4oSLzslX6DPXgTf9kuAXyGwv_ypYxUyTFoqtrDdJpD1i_ejEwOvOers-JSeptXm3OR_mqCXV9nGnyaHdbA2niTmF0Lt8iQL0vfDS6yWo_P2MUChvV1j_3aVA8BGiXYgBCTwxTwr4hSUrCj9oBRBZKhv-T2rBqvwalVukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fad3da36c.mp4?token=eAg8QFomTHlEapFr1wPJG152uH3cyYR6_yvCmkg2Fjt9fxFTEei6EMjxWb9gBnr0vfyRJe4pn-wPR31TL79nJRH1nzS4_KNb_WZ9fliiXozuIMKWIs0NpkNPUCUy6hnacOUJqZkZgNpwiceEeB2RlerxVPPRmVu-SGGmKOlpNvVFGU0eu4oSLzslX6DPXgTf9kuAXyGwv_ypYxUyTFoqtrDdJpD1i_ejEwOvOers-JSeptXm3OR_mqCXV9nGnyaHdbA2niTmF0Lt8iQL0vfDS6yWo_P2MUChvV1j_3aVA8BGiXYgBCTwxTwr4hSUrCj9oBRBZKhv-T2rBqvwalVukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارت‌های بازرگانی همچنان دست‌به‌دست می‌شوند
🔹
مشاهدات نشان می‌دهد یکی‌از فضاهایی که کارت‌های بازرگانی برای اجاره عرضه می‌شوند، آگهی‌های سکوهای رسمی فضای مجازی است.
🔸
این درحالی‌ست که به‌گفتهٔ دادستان تهران اجاره و خریدوفروش کارت‌های بازرگانی جرم است.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/461543" target="_blank">📅 15:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461542">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf92b2ceaf.mp4?token=Reup1-tBUo3A5Mz2K4IgHD_0DyKplMZ1RKfFl3Mg91P85cYQPUj1OKPEsLx41x3ZQa8RRFGsRsYXA8414xuAbhc8dU5cUbAO1PrDA2bExpRaE3dR61IDjuBXRTbbD93x5i7fPEUQSIIQVinffIUcCpm7TTHT1YWJ026bHB-0UlEanVRQnAPf5ZBcmamV7Dq4zZLAxifXHH1hSxC4rGf3s1V-BrnuB29pPx174jzhXHqVPrKySXu1ui3UfirnkPJMr6ZO209UEkuGfnzU1DuasvH7dJK2r_N_HxZmv48aCJlZI2vEpMGg32oxEqrPxk60f6MYhw4OCkngfiZ4lbsXxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf92b2ceaf.mp4?token=Reup1-tBUo3A5Mz2K4IgHD_0DyKplMZ1RKfFl3Mg91P85cYQPUj1OKPEsLx41x3ZQa8RRFGsRsYXA8414xuAbhc8dU5cUbAO1PrDA2bExpRaE3dR61IDjuBXRTbbD93x5i7fPEUQSIIQVinffIUcCpm7TTHT1YWJ026bHB-0UlEanVRQnAPf5ZBcmamV7Dq4zZLAxifXHH1hSxC4rGf3s1V-BrnuB29pPx174jzhXHqVPrKySXu1ui3UfirnkPJMr6ZO209UEkuGfnzU1DuasvH7dJK2r_N_HxZmv48aCJlZI2vEpMGg32oxEqrPxk60f6MYhw4OCkngfiZ4lbsXxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جای نفت در جهان هرروز خالی‌تر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/461542" target="_blank">📅 15:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461541">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d6e9ca6f.mp4?token=kZdry_XkfgljI5PlbE1NlK6UL2Fp7K0B4Lbga3nTwio2a0-uV9Sy6aveU8xcb0U5q6lXaUzh9cC8ls3OxPPdxjrWsxjefKrY9QYVADcQYUPu-ht1zswqdYMNIy-j54VHZmMNTeUletbjDKSsV0Es_9gtWi8wXsmufLvfAogb0zYiPKra25lyo56BLO7RiMDpcEx8yp_nFM06xxoLKiXKDSZcbZaYZEiX488MmFeETBVxls6vg-Ur0hG5MR1HYVvnR3S3lF-R5-y6cwv2hNTd-fXCvZr0vC3M1FNUHAtcKeLMTgS8GhFjIDYThTeulDBBgA7R990Nmqdyws2ywrMYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d6e9ca6f.mp4?token=kZdry_XkfgljI5PlbE1NlK6UL2Fp7K0B4Lbga3nTwio2a0-uV9Sy6aveU8xcb0U5q6lXaUzh9cC8ls3OxPPdxjrWsxjefKrY9QYVADcQYUPu-ht1zswqdYMNIy-j54VHZmMNTeUletbjDKSsV0Es_9gtWi8wXsmufLvfAogb0zYiPKra25lyo56BLO7RiMDpcEx8yp_nFM06xxoLKiXKDSZcbZaYZEiX488MmFeETBVxls6vg-Ur0hG5MR1HYVvnR3S3lF-R5-y6cwv2hNTd-fXCvZr0vC3M1FNUHAtcKeLMTgS8GhFjIDYThTeulDBBgA7R990Nmqdyws2ywrMYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه از صحنهٔ جنایات دشمن در لامرد بازدید کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/461541" target="_blank">📅 14:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzdq1X6x834RR4JfqdinnWoVVy_fRhKlhwnR9yxpsqD-ymCpydi2LpduD1ebWqQ28ehigGoKsko61IjYjHbMXxeGy4vcLiGE8u6yXTQhGlh-tHOpJgQlO3Mm_r5KnNhubzlXnxn5jk70VlQva0tMXmi4vIpE2Ku_v9ddnaMFL_VTo1pHni5k_wJ_jAx3Oh1SlzlD6qOeO2gnHqx-GuE9LusqF_g4EuMEwJlhj-wAY-bZV-3vOfa8D6gEQiaXLpnUCsPB5QcDl59bmJgX_uDtYgXrUll_3oSFS3uTamJ_VeAeMpXgxz2K8ntHr8bk1TOlPWCaU_CNSo3HUiogyvnhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGwmLdcSrzzdsz8TikT6ZnL36ms3yG4EDKtK6e9wjamKpf_-tNAa3AaT88alhECoAX1r03kvA5mrx70FsFnycvSWzekzQBDGbCaj_h5xEIsE8aXYpH-jRuky9zSN4I5qVvwBOLPHkEIRTnOC99bp7Lc1CrfJDAF6teUx9-SIQvqwWg2JnO8DwSLu57ZXk1MdF1ITverLcDO9RPRjxrzu6mCJwao645xv4iWGfPnQe_Dr8_g1Q5uljHHAwbupPpm7kogIa_CGGdbpnF3QZdmwInL2KA8BHGYAdeCW-wSwZiqYY4Wlv7yutoaCE_mjeeFOQF-QuG1SnkhKUiku6AipVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNjLyHdpSn27Z-1ytav_t88xMIxKFTF3qW-Z7ZSACvZj9_ku3f7vF9y2-JXRd2QaF48-5YnKW0ETXBkPrT6dDaAIaUGmLst8TvZT_NyS5dNfOlz0UCpDNK9ZBNcW_mVqvv43kryZ4n5jmBpoLq3K1m-dPDdMoDgcgTWZa1yhIiZpLJrJ8G49TQolU111e8J76eI-LH-6BVgOhdUU2Mx_1YSzN0Km22ytQlSm5yqIZCUv9T7FuLRD97Mu_shG7Emy-I7pQvdFukKLT_bTkEJijVVFRDmuTeSQkfxdTrwLtihyvXXPLoeh_Cj0h7bSk1ME62djo_nRyVIJTA0Zg3fiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJnhjzZrFvi-VqvF_fvRdhoERb3StJ35KEqYNHG40gSzWAADfNuHZGUONgcFBYuJ6WAXmjNVpytwwMIw1l8DV_L_QZ5_rU1y4aFWeAc2IeUx151nHqmoBW_Zg05-_kun-Zv-7dJTLDPuHtMr6qDLB2Dw61u5VOnJk8LYLJvwAWx7_CvyYtxJrPGrFxy3VMdtnwRuFFq2_SticzydMRGQhntlcckeSlV8JIPngYa1c9Xync3UjWj-BuO_VZyspBvmDN0WRRIWCIdPyIGTbI9-fEDdqOEDAY3xdrK1WIBsZHHq4-tDS0LYqxaQhmfX95TrYu8pRnFBekdJapFmnqAf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKBBgjuxQx6qMmGkC0ZwEEm-fwwPwithvXAwNPCIg0bj7b_Lj-hthR8fMS71EMnLmfkGC9-NkZnI9ibhN7o4bcjUVV8oOv_4_jB_ZHx9tB_aHqbjmuQ7l0MsgsWxjf5ScphGJ3eUQ4z0prWdz8vweS-7dEfw_Y1ptaNMOf2TIK-A-yEi-I3AMdpMiLAondGfFvdsUcwp-l-0ZdsJHskbCxHnVdg909seGgTktxSNuGjjZFvk63HSzuOB0TZtLJFT3Xv3nRd1SaNmcomsmOhs1yEk5SmXIaAL2IRaaz5-89bLoegLhQgoYZQ9Hd0qW0l_R81YhAwii2GRIUDAaYa76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ithonNdV5B4atU8iyoaYQKVgn5PI9OsQ0b2dCeQawDeDWz4YsMe__13mIpO-NYylf6Q6Ef3fQbZ0hVDKoMStRuGqeV-XxpWWxWTQzaoNZ2LAzBkqBUWMXrBJK0eu4a5VJqLdxjdcXLy3Ht9agHOzdOS9uwP36dNA5mxDPLNe1b_IYImqU1Z3r4ouOY754gIQo1_Dcfaa2jnqFJxfDXuWAVYy6lKG-DuO6S0S4GnVyL1L6rU2vCNOSMwQYMSSaTU4FZmQ7qCxEsDacGa3EGq6pIaeELIaHbfglTHIWtBFSOHXbwhZmyyp8j9SEDktUqSwlaPqr_faBuGdDfZqjkpUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5yojMtn_huFUAIUqESMzsvUrsPFQVYfnu18pF4Nn5JUn4DYLWMY8btTq_4KrJP72xhVITYOVjCux2tc_xdhxhw68OU6berPZmY0TkTnLwJRkaKHk_kooRj0muKhL63i2t_sKZTvcpvvVqoaZr7uslg_PDwZiOgm7HivggVEi9BsZ67f94wJOJeKdhcc8pR_0ZSffBWRoEEX38Gbxfm3TeKBFdNbnL-59cP0NbjBnexNsI6ExBITRKi0hIboZhYMFpzlQVzVkwZBtgD94ru24ivwsGLKG6ms2NtWzP0c-qj7J8rmZbytdF_ZwiBmQ8136rBDZ9XJanXeEfnwlYTNrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نهمین جشنوارۀ انگور ارومیه
عکاس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/461534" target="_blank">📅 14:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=fuiRDikLcgh0EzJ7J30xhGjVDccLXcAdhlCnVB82BVM-8o-2DYU533tVfuyrkdW2QwJ1OeFkSoRNfTjRoWb5veoGCSVLXB5H08j9x7xto_M56MrKXR37ZE0MgpZW7Yd4LnunfhE4Wd19-Vs-rtP_WpzU2rYEr9KDi_p2JjUGBvlfzR67MYQQ8Yx5_X1eEy5O_L5IS3npqScSNoLmPydkkTJvaW_9Ijju60Kla3Z80IU3aIxFTErbpfgH2kyq37F_TDTt1piFBjj99ikoVMBi5ZYmjagzQ3r8ia7MJEhImUs8cjONZkqKoPKu1BdaB2WJg-wGg4_WxATNnt0BgLODhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=fuiRDikLcgh0EzJ7J30xhGjVDccLXcAdhlCnVB82BVM-8o-2DYU533tVfuyrkdW2QwJ1OeFkSoRNfTjRoWb5veoGCSVLXB5H08j9x7xto_M56MrKXR37ZE0MgpZW7Yd4LnunfhE4Wd19-Vs-rtP_WpzU2rYEr9KDi_p2JjUGBvlfzR67MYQQ8Yx5_X1eEy5O_L5IS3npqScSNoLmPydkkTJvaW_9Ijju60Kla3Z80IU3aIxFTErbpfgH2kyq37F_TDTt1piFBjj99ikoVMBi5ZYmjagzQ3r8ia7MJEhImUs8cjONZkqKoPKu1BdaB2WJg-wGg4_WxATNnt0BgLODhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/461533" target="_blank">📅 14:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461532">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttucBcaIb6ULuEmmQlCcb5D3PCQBsDLsj08Bu99RyQlaLx9ma4f-INPOZYD1Gv9ExHNrNbh_C_OmrW0oFowXwMuBRJjCpcjgkYF3WDSCwtP8nq-WqJK7PmOweqwaVT1gDa8AKmgTCWITJSxe-NQ2fVrWt1dOrUJngwFZhRfOGPEoR-fAVfLjGtDq-92i0hRxJjUZlT7SEhqVqKeqJryKNU8GEo79vzx2Pu39nPnRslBkmOB4plJm_qEgOE-ZNAYJEbF5pcJMyypoe80BqZEA7rPAWHInK4ATdHIre1Nb4S-UUcah5ucRZXc9ZIwzHETEO0EQAaGZhK8nFLxqsorlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان با رئیس‌جمهور هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461532" target="_blank">📅 14:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461531">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6858133e.mp4?token=RAOrO_ouLuR8Ni5mE5FsDIqa1VR-JYiQfnKNxrrj_MiCCpxbQIge2bFleuoMEoTOgo6UrrvOpD2RgMAqt_IeVcrhDnrJDVsnMdoaVPJGIGt76s3Hm9a5_8OE8qmASTdsMtzMeakFPVudG75c1J_jKAh1AvqP42l1mWyvVpAiXhak0g6CT3Pke3HzHU8n_vP-XySj0Q9GFLVh3Nua3End-pvsQp7KUsNIe4elS8dho6-eC4R5v8WbT2LF9azN_H_3LbDKVdCPeP-GqvVguFO10srTr3JfHiZmiRA68Q0Og-eum6Pfc5iiBq0dQ3gD9SKx3K_vGJTPNli8OM0B1VmaLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۰ مگاوات انرژی تجدید‌پذیر برق‌آبی به شبکهٔ برق تزریق شد
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/461531" target="_blank">📅 14:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461530">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff42263766.mp4?token=f97cSSyDhAq2QQwVG6ZAFV15risQZyhL_lvufLG91p91GTbtu6ImydmCJZKBrksdRJV4Tjnixgt9rur8FcIO0iB_rpvb0qi4fvl2aXVjHuXrITcjjycKsPzAXVzsUEABxehFz5KA_Wk99Itv8SMHmMoZ_QzmP70NzzWjFjyTP7UMLfDAQFvDkitrIjW20PFJiY6tcK7ifxK1O0dZfo897pj-oT576VlYG0MWdP0WmZ-zNQikqVaScOxnH-75J2xTOP8-FQrxep0U4TU4XISbOH8TKJw9_kurz495X8EP459UkM75tIjiyhX3fr_bGxEmRqxg75-L-hDyTv_6hyMkbxNlF63FoJYhhOC5zhVpqsdCSJqgsM4y-q7z4IwRx3JEa6Wy6JregrVS3qcDA1yFcGJcDt72WTZkwGNzpz_4LIEDRr_rqOoh3RnAsf91BmluCo2nt6Xu6Wie7PGkkuFYqx5hoiHyBWBLXTVO5qAL-OHwu9Y13CHbNPdfHbGJ7tMp_lLtER_MCirzEQ22AN6YMI5PUkr_GGYcq_Y6ESVY_XVicPBmVBubgek4zZqO55rhiBRCStdPL7cOa24t8OihH4s3zXHskINryKIaTu7pngexbG3T8ydtNnq1aoDeX8RYR8v8zYrchHBqOl-eMXnzUPG6QclHkSTLfpjZiVM7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/461530" target="_blank">📅 14:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461527">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae4DXayOGAePEDRhfOCXd4GbS-vhH6eiXYdx_Rg_xV49PSY_NeLuMWVbrD0DiUTi_o69zkptCFeGbHnRnz4wsud-5vhTUKAsTBvuHb60tIFEdB-3NpfLGvdIgvKwF5E7Qn1yBXtWBxVdlLVk2liyOHpo647wumFip6fBRbbuqvQ_A_TVOGId6r6idYH9zh0OFnp239AK6K4fSEcQ41wh6qQj43S2vLZnPf9eI062Cw3xZ6ygZ2dTWN34lsUd8ysEcrb3VSZWjfMyU0GwAksrkZCJBiyhHUdLXZjL_qLheLRG7sXYLrrU7iezMrAQNnAJfy5DZECYX5f2m9-EbEiaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brlQfW-nsGg9lm1Q5EPRnhlxfGaejMM9d9v0QMNv7arfkUwES_4S2fSL4M7oYFEMaiJNDdb--E4G2RBMEhANiU_nuWWn-YJGmBT79gFr0YnDN6f66Po3eA13I7NXBfdbV9p031z2V_BEg75ChG7CQMmvyJ18Tenc756882zlDMfO4xtFXy_3OdXSCh2iWjg_8aLmHTL3uE3K6DzJO3VRyTJMlVekdq9Uy6Jrn5NSh89q6Fgs4P3om1k-a0etz6g4bzkW-iIMC3WQvaLmc98uZudI5an3G2sJL7hJYuQY5jjyP1wPE2HV69UB8PxcnQM2OlSNWNJMGFTnMEdDt-qeZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">25 سال بعد از یازده سپتامبر؛ مردم دنیا درباره آن چه می‌گویند؟
🔹
در پی انتشار پستی از سوی پیت هگزث، وزیر جنگ آمریکا، که در آن مسلمانان و گروه‌های اسلام‌گرا مسئول حملات ۱۱ سپتامبر معرفی شده‌اند، شماری از کاربران با انتقاد از این روایت، تاکید کردند که این حادثه در چارچوب یک عملیات «پرچم دروغین» برای تحریک افکار عمومی آمریکا و جهان علیه کشورهای اسلامی و فراهم کردن زمینه جنگ‌های بعدی صورت گرفته است.
🔹
بخش دیگری از واکنش‌ها نیز به سابقه سیاست‌های آمریکا در قبال گروه‌های تروریستی اختصاص داشت. کاربران با اشاره به تاریخچه شکل‌گیری و گسترش القاعده و داعش، واشنگتن را به حمایت یا بهره‌برداری از گروه‌های مسلح برای پیشبرد اهداف خود در منطقه متهم کردند و مدعی شدند که آمریکا از تهدید گروه‌های تروریستی برای توجیه مداخلات نظامی خود در کشورهای اسلامی استفاده کرده است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/461527" target="_blank">📅 14:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461526">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7108374e6a.mp4?token=aEZYNxAhBYE4w9Ul6Y3Z9NEy2uS9NtwQNxibQ-NliXOFhG5vk_2faw2YWLXP39_X2sWSMUVEaWSb0OU-t58o-PYyKs68q95B4Jsn5X_qKOY25Ib0BGUK77vc_0F9GJE9CdaZLHURyHmNa8U5NVRa79uS0b4jY_qjk3hp6Am0DugAkumZA-Mo52EzW1Crbcz3HpbrLBF7sX9jIZCSzeJH9apoDMvn27WgOdlzn7P-dz6vjRzYNpUGTFqX4uV1s1bQJZSzLIAn7Qscfrne2uW_N4NxqFAC0J4RT6leGRn5GoqZNSWNBhOGVUnTpvSTsssVMx0KxPgwIPZvg8JEJ8T8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
🔹
مقابلۀ عملیاتی با تحریم‌های یک‌جانبه و ضدبشری اولویت اعضای بریکس است. بریکس باید صدای عدالت باشد.
🔹
اعضای بریکس موظف به ایستادگی در برابر عادی‌سازی حمله به زیرساخت‌های غیرنظامی و تأسیسات…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461526" target="_blank">📅 14:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461525">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bleGXamophasIwzTeCoxp4IXDHZSdGv_pHjUafrSWxqV_q2Qq8o39Fosatoph3VwokrPBMXBhUxtFGDhQ4oM8X5Ae95c_jw7uCwC04-1WJijHLe2RNzfNzXep1QICcZcMUiT4k1P8EZ6YzXOWVHEXmVvVlYlyRDrneR6NBrZQWaRfLA5CQZ27ALnfu1vynLvuTTQBzN_GBrSgCzjKN4WndfATl3IXiCDQGxdOjc0pb51vH_sT5bNh45ySIBE9eIfIiWqSGt6onLP8zYY-TuO26n3D-g8MipK91T-akd0JMerIL6OTkXkK7EVDHMRYg0FV6Dc61gmRz8kGIc9BSY2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه‌ها می‌توانند تا ۲۵ درصد آموزش مجازی داشته باشند
🔹
معاون آموزشی وزیر علوم: برنامهٔ وزارت علوم برای نیمسال اول سال تحصیلی ۱۴۰۵-۱۴۰۶، برگزاری حضوری کلاس‌های دانشگاه‌هاست.
🔹
دانشگاه‌ها براساس آیین‌نامهٔ جدید می‌توانند تا ۲۵ درصد آموزش خود را به‌صورت مجازی برگزار کنند و آموزش ترکیبی نیز در دستور کار قرار گرفته است.
🔹
وزارت علوم برای اجرای تدریجی این شیوه، کلاس‌های نمونه‌ای را در برخی دانشگاه‌ها آماده کرده است.
عکس: اصغر خمسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/461525" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=E_NIJO93lG9yimD_HwtHCT4R-J2XBGg71ESLFHk-1jkatyjrbbGgsqY3eDerkNYuLvweEEv4Uw8cp7_GOn8y065IpaDAu3u7sHYJMhrs6r49rHWz2DQf4NZ1kL5WoqnPlYdaBtrouHstiiuuTUeBUUb5LF1DxEK08MQUpWxxj4GROp7W-zMXfZ8nhEcHjfgdGeqsenFiU6haOC0kLU5pYG0Kea3q4tWTLRtK550JWpsNGd1VTmV7EEn0219dP_Fi91IlJw4IDY9dZbb_rL3Fsfx2OYeXdXXpDsfJwAg6TeQrK0JpT74hqp0sijQV1nTHzC1PD41KDQD4-sO_dge64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/461524" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szMxxNuTxrjWhBjTEhbm84SiHPF-_-aKKYyqn4mu_fUvCnhp7wFnpnjXlJU6JgtIMJmARZdKnhT0HZ4pFXyHlr3DnYDpiBAqiOJAGG8FfGaKpmuz1mce57pPEPYEGW906IEsC0jnU3EqbfhRhdnqIJpI5K8vc2-qDRKjw-ULYLTSyK7Mzfy48kkItf7CW7-TSeWHtS46HxLI3jnMc72TVkt6IMTvCWQjm0PoA1UmuZiK3XMNTN5WdhszYaxHHhBjRwGLfOD8v7t24mIqGvDUStn2aBrQT4gukRoUw4lVG8XHKk7-ow2XNoiIG0mVXp97KMCWQaM9IGJ5F_ZOot_yjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: پوتین مایل به دستیابی به یک توافق است و اگر زلنسکی هم خواهان توافق باشد، خیلی عالی خواهد شد؛ مانع اصلی ۲ نفر هستند که از یکدیگر متنفرند.  @Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/461523" target="_blank">📅 13:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c7826bdb.mp4?token=EA6i7BRrnyTJcHzZnBGpgVwp2tB1Obo8kckr2HwytXmXJjaOvaq8O5lhbv7ectiG7sHKj-aXprJZyfu6LbfJZPU6etUjCtSfuQRTqFEyBTBPdOVnYLy8pEmpdXkCyF-W7AcambScbgyfJul-AEUyzbjjZc1tM2Me0-O5id6GwTBAEuRLbM5gBIAwuJv9P0F20ADzhBLdzkTBy2-CryQP0TKdAugqAMTfypxbEmyBzrRbhdWvbrZrxTx2cI0VxMkYkocd2QVNS5Ig6GrLPP_Cd9t6qtERQtcxTMO3o76nXGOFRe7cJeEEVDV4-kQ47INe2qfdxOXcpE628o38kLbZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c7826bdb.mp4?token=EA6i7BRrnyTJcHzZnBGpgVwp2tB1Obo8kckr2HwytXmXJjaOvaq8O5lhbv7ectiG7sHKj-aXprJZyfu6LbfJZPU6etUjCtSfuQRTqFEyBTBPdOVnYLy8pEmpdXkCyF-W7AcambScbgyfJul-AEUyzbjjZc1tM2Me0-O5id6GwTBAEuRLbM5gBIAwuJv9P0F20ADzhBLdzkTBy2-CryQP0TKdAugqAMTfypxbEmyBzrRbhdWvbrZrxTx2cI0VxMkYkocd2QVNS5Ig6GrLPP_Cd9t6qtERQtcxTMO3o76nXGOFRe7cJeEEVDV4-kQ47INe2qfdxOXcpE628o38kLbZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از به‌غنیمت‌گرفتن تجهیزات نظامی مزدوران سعودی پس‌از فرار در یمن
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/461522" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عملیات پاکسازی یک خانه تیمی در سراوان
🔹
بامداد امروز عملیات حافظان امنیت در شهرستان سراوان برای پاکسازی یک مقر عوامل ضدامنیتی آغاز شده و همچنان ادامه دارد.
🔹
یک منبع به فارس گفت: از حوالی ساعت ۴ بامداد امروز یک عملیات منسجم علیه یک خانهٔ تیمی در شهرستان سراوان…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/461521" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86aa112bb8.mp4?token=FlXgT3fe5o5ROp7YbhaeV6H4AQsM1m69CL7k1ZesZu7Kj7uOgd9NqU5ebZjRL1DKK--GsAy6LBwRQJpzRJ4v34pRL5bs8JvH2f9FYShc3APSq7B3cKo4z5ShsOFDjbStpsA1t2uv1XEgg6ZcGxpYJdrhx0psiyEsiT55-4lfSUk73QxC2A5uWWI5dAgpVHhIF96aUgVDrvUPDZBuF1h0c3M0uNO1bBXPAG_ykTUQvSjtvtSfzJcn38reyByp3SE6EKtXBRFFZhudkpypDIDdqG9JEE9Sg1KihXQXj2zAY4ChGczeOaMdIQWVePZ-AM3He648oUXfbKIwRc7eE3T0gy0kCGO1k5ZvOi_4-eZIWTQxkSHjgIxZsG9Nha64rOUFgLerMj-SdT3r5n8KRrnNVcdCyuNQgUXXogaOvGC4Ww-rDL13XvSVqhlGU3livAmmEcqkg3nNR2aVxm25f2tNnbEvs4ocZKiznOBgISnWMk-l3gEfxeEhQAGDTnxA6eBnVVIYosIaB06TzoKQM1Rq5OJUg6PKWnlFxBEqqx02ECWtH0Av3IGz8Vjnsen5JeestdRI9OWdWKotR0sOhh2Tk2_sxefKD_gPkcmf_ScNc93XWKzf_Haj0tKldH7386YVqy52fgWKF7hPcZ-xiLJIsj_Fv9qqg-_Sn5ZzNjtlKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86aa112bb8.mp4?token=FlXgT3fe5o5ROp7YbhaeV6H4AQsM1m69CL7k1ZesZu7Kj7uOgd9NqU5ebZjRL1DKK--GsAy6LBwRQJpzRJ4v34pRL5bs8JvH2f9FYShc3APSq7B3cKo4z5ShsOFDjbStpsA1t2uv1XEgg6ZcGxpYJdrhx0psiyEsiT55-4lfSUk73QxC2A5uWWI5dAgpVHhIF96aUgVDrvUPDZBuF1h0c3M0uNO1bBXPAG_ykTUQvSjtvtSfzJcn38reyByp3SE6EKtXBRFFZhudkpypDIDdqG9JEE9Sg1KihXQXj2zAY4ChGczeOaMdIQWVePZ-AM3He648oUXfbKIwRc7eE3T0gy0kCGO1k5ZvOi_4-eZIWTQxkSHjgIxZsG9Nha64rOUFgLerMj-SdT3r5n8KRrnNVcdCyuNQgUXXogaOvGC4Ww-rDL13XvSVqhlGU3livAmmEcqkg3nNR2aVxm25f2tNnbEvs4ocZKiznOBgISnWMk-l3gEfxeEhQAGDTnxA6eBnVVIYosIaB06TzoKQM1Rq5OJUg6PKWnlFxBEqqx02ECWtH0Av3IGz8Vjnsen5JeestdRI9OWdWKotR0sOhh2Tk2_sxefKD_gPkcmf_ScNc93XWKzf_Haj0tKldH7386YVqy52fgWKF7hPcZ-xiLJIsj_Fv9qqg-_Sn5ZzNjtlKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده‌کل ارتش: وحدت و هماهنگی موجود میان ارتش و سپاه کلید فتح قله‌های امنیت و اقتدار است
🔹
سپاه پاسداران در طول بیش از ۴ دهه همواره یکی از ستون‌های اصلی قدرت ملی، امنیت و بازدارندگی جمهوری اسلامی ایران بوده و امروز نیز با اتکا به ایمان، تجربه و توانمندی‌های…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461518" target="_blank">📅 13:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQz8meuBfZeFn1mAjUkdrxh8DPCDMFPoNaRvxRQgikrEAnDBaJ3qcxACGiGgbDcJ4PIRyajJRT3_8fNE0R-yR7xcBZEJnKuMzsE6ldYUhZMRYKWwL6Q34_gS1MEmSp034NMqb_Zt77Yn6Vzf-MMA57TQVVTC0qnGQk08VjIaTRWM01naPVbUF_0qgrdnmam5T4jIvzZVV69JKNxMchLxkba94SOFd7sNm42XOdbristoCgO_aj7TLkEPX0L1lBtltwf9LGAWZMyM8Veqh_sWIYiuX7MJ-HRKRX6rj8zdXFmT-2zlEvrV615roaWvWG9zD1oonimsEGNT0zH6zc-ojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه: ترامپ برای دستاوردسازی به دروغ و فریب‌کاری متوسل شده
🔹
آمریکایی ها به سد مستحکم ایمان و غیرت ایرانیان برخورد کرده اند و استیصال و درماندگی در رفتار و تصمیمات کاخ سفید موج می‌زند.
🔹
ترامپ برای دستاوردسازی به دروغ و فریب‌کاری متوسل شده است.…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/461517" target="_blank">📅 13:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWm-XzhE-YhyU6hjpDM3wmqyiDStUOFy0wbL3zJKMklbY0CoS_6-VX1VRuVIpMu5pip9ClCWf6wPGH-lscdYaz5Kdyn_sBzlK31VGkZGOczLhhODZLPRE5RoQcfw1klQveFUrVmWg-GAErdC5UczbkOaszr161YHj334k8Y0NzwyrDkFarpCrySltRTVLBiHYPNuZDXMKFipPaA6K9OUgc_-yfvssFjm6q_jYu2-aqiKO7AGHcPA2qBGA9Tb7VJT8vllPeIs_YgMJvL4id6k0uR2nkDSIAGMg7MmaYFmwlwTKZvhUn41pCugepTfLTz_a_laAQiknGy2HZaPyxLN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مشترک فرماندهان ارتش و سپاه
🔹
سرلشکر وحیدی، فرمانده کل سپاه در نشست مشترک با سرلشکر حاتمی، فرمانده کل ارتش برای بررسی آخرین وضعیت میادین نبرد بیان کرد: توان نظامی ارتش فراتر از تصور دشمن است، در این جنگ آنها برآوردهای غلط خود از توان ارتش ما را به عینه…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/461516" target="_blank">📅 13:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsplmAlroy7VxlwDq0dQryF5ev-IEpls-zGEN1tFbbclfVCZLU-d_pLEg1sVopTENMB39v2l44-vbuqyh2PskNrwEj16ynfU9K2-2UdQKOpWQZIUtFk7ZmdtLeOi1E-3R25sL8MAsctiAQuZUuKiKg_xI2VHtWkNyuKILPNEnI-EWNRa2VEtjRmFJlTWyIgXj8s76ALTimC6ZDIKL-S1384UPpq8rWtH-GeZ1Zh4YUMaPbJA_1rt1xcPiHHsucKcJY3xmBsZmO_yrqKwEoKIT4mu_UPb-6PCj2F73gcugH1kxFPa8YfKP03HfpfaWzKXfkO4qlrLJzsjaDq82f64wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست مشترک فرماندهان ارتش و سپاه
🔹
سرلشکر وحیدی، فرمانده کل سپاه در نشست مشترک با سرلشکر حاتمی، فرمانده کل ارتش برای بررسی آخرین وضعیت میادین نبرد بیان کرد: توان نظامی ارتش فراتر از تصور دشمن است، در این جنگ آنها برآوردهای غلط خود از توان ارتش ما را به عینه مشاهده کردند و واقعیت‌های نظامی ایران در میدان رونمایی می‌شوند. ارتش صهیونیستی بدون پشتیبانی آمریکایی ها در زمانی بسیار کوتاه فرو می پاشد.
🔹
فرمانده کل ارتش: وحدت و هماهنگی موجود میان ارتش و سپاه، ستون استوار امنیت ملی و کلید فتح قله‌های امنیت و اقتدار است.
🔹
وحدت ناگسستنی ارتش و سپاه همان گونه که رهبران انقلاب اسلامی انتظار داشته و دارند، سپر آهنینی است که از کشورمان در برابر فتنه‌ها، ترفندها و توطئه‌های دشمنان، محافظت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/461515" target="_blank">📅 13:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmsyAErB97ReMsnwMiCeijGjXTVQBponeVxz7ceMWmmrdR3R3xdgBg54_otInb5N25A0zr_DvOVla1xNIuEX7008MGFR_Z7V5nmPamO744MftKUyTK0gdgl3kqMlyiBf5B9IRc1T_1u4KTk3boinD3toqZMFLbg4Gcl9BEW-hd4WZdSK8PD2myQRbYegpFiNczOFSPztoSazhICCWrzBzqnt4FF_Se62NXjZqG_XROwJqshpXXrXNmDHuIQP2KtQbs3E0tgHhDot0SPrseuO6xt9sr3PGrHOqEenvalRfFt-PCdVtSvcbs5bYsKri1E2wYRUfTYJPtJyhI1SoU2-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردزنی بورس در آغاز هفتهٔ جدید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۵۵ هزار واحدی به ۷ میلیون و ۲۷۸ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461514" target="_blank">📅 12:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مرز خسروی باز است
🔹
گمرک خسروی: مرز خسروی باز است و فعالیت‌های تجاری و صادراتی در این مرز بدون مشکل ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461513" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGSr_Uwz5wS5x9t9l4RLycR31_lDfvRGkoMltb9MRX2NvxVEq0JWQxT3nv1Q5nmNFzGTKn_EYcmCGr165BPtfLqN8o5AlvXsbRkpWKf9UOXTtJOVV04UnrbJJzRkogKyxL0x3-l0kmczSbrGA-Wm_vIAFv1I4q350dR3ReYw88k_DXfxOJ8WwREmLgKLS1ixr786NlYabhRX0f6pffqEx4tg3FV5jN4kgcv3bOIXXPaoP6_-oFqIts_ERcCBlCm2sCuVBr3q76kHL1nuoDCYSFKztsE4LJ_HMZiHy6rxiidb16E2InVzjMx14gTvAdRynwb7Bj-qxCaQ7Aono62WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461512" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOiKTbJhYK7pmCOOPSoYml4W-EGTY5wAZllReotuabMjOA5PT5ejPUUKCeCu0B5l8IThlVTwk9C0_je1mhOZk94APVrqTkYowI3H5l_axr_yOt5fG3Svp_ctY-fRdWdFuJsKVpnaolPdNborBRTiNy2OG1_I_WaC0acEWZ45bJA_DCwbhsBOthQJTjumD1rT1ujM-Nh5gjeV71axjf58JZLTj-y4IaPWU46qpsouCdOIap0JvsrlWxrXvEDKB2GK6awcFHy45JtsmmNMIs8flOnj4zhUxgvIuuinGwKwVdkbsLLegtep0NZLcdPvIOTQPnjAT-jnA0RRNy_iwR7NkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد پتروشیمی خراسان ۳ برابر شد؛ ثبت رکورد ۱۲۷ هزار میلیارد ریالی در ۵ ماه نخست سال جاری
به گزارش روابط عمومی پتروشیمی خراسان، مهندس عیسی نوروزی‌پور، مدیرعامل شرکت پتروشیمی خراسان، با اعلام این خبر اظهار کرد: درآمدهای عملیاتی شرکت در پنج ماه نخست سال جاری با رشد ۲۰۹ درصدی نسبت به مدت مشابه سال گذشته، به بیش از ۱۲۷ هزار میلیارد ریال رسید.
وی افزود: از مجموع درآمدهای کسب‌شده، ۵۳ درصد مربوط به فروش صادراتی محصولات می باشد
همچنین نوروزی‌پور ادامه داد: پتروشیمی خراسان در همین مدت با *ثبت ۵ درصد افزایش تولید و تحقق ۹۸ درصدی بودجه تولید،* موفق به تولید  بیش از ۴۰۵ هزار  تن انواع محصولات اوره، آمونیاک و ملامین شده است.
مدیرعامل پتروشیمی خراسان خاطرنشان کرد: رشد قابل توجه درآمدهای عملیاتی در کنار افزایش تولید و تحقق بخش عمده برنامه بودجه‌ای، بیانگر تداوم روند رو به رشد عملکرد تولیدی و اقتصادی شرکت در سال جاری است که مرهون زحمات همکاران و متخصصین مجتمع میباشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/461511" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7FmQLYMGRP08Gothc_FbnPGSI35enqVQ3iB-GHxvHDUGbNJ5oXMj9laoIADx81d21UQQ9MBD834v_MpRamZLmFWOLXYA76txX6fuatekVp_yqiXENBt5jolmUVsTMwkoAvY1zOWl6Kud4dzgD6zpEFqmSy0h4dFsvxUUOEKur0VGvERp8Ph8JE0d_t5Lh3msxv446ka23M_GwEz-_i6IuVysVmmC8FfNjla6G3JcMFp7DZmXrnhbmx7XSz_-BwafQdUKTKOp6NKSXz5dEMRPRd_ggsmMHIT4Cv00UlP7I3-Pae2IMRXpqu53NnTjQinOXZPm2auqcgJ8_qJEd0UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بانک رفاه کارگران پل ارتباطی مستحکمی میان جامعه کارگری و کارفرمایی است
🔹️
سرپرست سازمان تأمین اجتماعی گفت: بانک رفاه کارگران، بازویی توانمند و پل ارتباطی مستحکمی میان جامعه کارفرمایی و کارگری است.
🔹️
دکتر محمدی با بیان این مطلب در نشست سراسری مدیران صف و ستاد بانک رفاه کارگران، بر ضرورت بهره‌گیری حداکثری از ابزارهای نوین بانکی تاکید کرد و گفت: استفاده از این ابزارها برای مدیریت تعهدات مالی و تسهیل در پرداخت به‌موقع مستمری‌ها، با جدیت تمام در سازمان تأمین اجتماعی دنبال می‌شود.
🔹️
وی خاطرنشان کرد: سال پرکاری پیش رو داریم و باید با تلاش دوچندان و مدیریت جهادی پای کار باشیم.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/461510" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/461509" target="_blank">📅 12:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aea342e2.mp4?token=lG92-mk-_dZ-6TBUyn8T-h0EKaolNFi3vVNi6W4FgPdwNQN-2vPW4E-jNrIDsnih-wBzWYUy_M3IJcx2QabQAzQKtHqAzaf_izZgPh1l-WCQzsOJbvbGANz_KsQkgyj9pCmlTqx5MqRS380unEXXNFupa-lnA1A5uq-40dPgbIw-k96_kc2DcNMReSmCs7cTe4ZQm0YpBqrsv_grcOpB3m_i6k-j0lajLKmX-iXEMD81256_3DTGzQPAT9mlYk5pZDGDii2ELgx6OCOslBrJKRrYHn1TefgejUU0WYD7RC6CkYxzSzYODiYlYUMSsQNhfA1j0wO-Wo6lNBlsWS00SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aea342e2.mp4?token=lG92-mk-_dZ-6TBUyn8T-h0EKaolNFi3vVNi6W4FgPdwNQN-2vPW4E-jNrIDsnih-wBzWYUy_M3IJcx2QabQAzQKtHqAzaf_izZgPh1l-WCQzsOJbvbGANz_KsQkgyj9pCmlTqx5MqRS380unEXXNFupa-lnA1A5uq-40dPgbIw-k96_kc2DcNMReSmCs7cTe4ZQm0YpBqrsv_grcOpB3m_i6k-j0lajLKmX-iXEMD81256_3DTGzQPAT9mlYk5pZDGDii2ELgx6OCOslBrJKRrYHn1TefgejUU0WYD7RC6CkYxzSzYODiYlYUMSsQNhfA1j0wO-Wo6lNBlsWS00SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ موشکی کره‌شمالی به رزمایش ترامپ و شرکا
🔹
ستاد مشترک ارتش کره‌جنوبی اعلام کرد که پرتاب چندین موشک بالستیک از منطقهٔ «وونسان» کره‌شمالی را ساعت ۵:۲۰ صبح رصد کرده و در حال تحلیل مشخصات دقیق آن‌ها با طرف آمریکایی است.
🔹
این پرتاب‌ها یک روز پس‌از پایان رزمایش‌های نظامی مشترک کره‌جنوبی، ژاپن و آمریکا صورت گرفت. کره‌شمالی بارها در جریان یا پس‌از رزمایش‌های واشنگتن و متحدانش، دست به آزمایش‌های موشکی زده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/461508" target="_blank">📅 12:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMArBAq7LQfmsgZrt9YE9SDmoBzeCOfgpWSQFZ9mQy_rvCEJLFKH243BhQM44BmTaWierpeNzUisWNrtKuajfzzkzpSIMr1akxglLluIbtv32rXm61RmwYqRjv7Mb-gH6R1_RxgpHLZXyjQSz0o84eLtKLz2mrjUs0RToRl0gfNLHzJW4HTx39KSnLvlSUKuoQ8WhTvSEW3UvPDzZ8iz7NUcHcMsTTvs5fzwTSKrRglPbpQLPeWn97Fe7w48l2D5XzpfwwSks4xXz-WM28uGNVNS2Y1bdbya-gJQPvZDfuUl-YwXpSjIltpPImsRsdrMTyC0vXr_bOtkzaz_q6byXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلندقامتان ایران راهی فینال آسیا شدند
🏐
تیم ملی والیبال کشورمان در مرحلهٔ نیمه‌نهایی مسابقات قهرمانی آسیا با نتیجهٔ ۳ بر یک مقابل استرالیا به پیروزی رسید و راهی فینال این مسابقات شد.
🏐
ایران برای کسب عنوانی قهرمانی با برندهٔ دیدار ژاپن و کرهٔ جنوبی روبه‌رو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/461507" target="_blank">📅 12:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfb2ceb1b.mp4?token=e_MPyM53YjZO2dxo1nI_SPVbaIOyIfXt3h6IwhqCNE9UWISsqLieAYzeKvCgLZRPk9reJcLL3vdHJjISgHqRTdtUFN0T9f8OAg-cdJchPi-EL7Cai7uIdyVwyU9zEL3-7m3WtBVKJckO0OHKlTxJDeE161rb44GrVwX0gobA4odw1eYQi13aZMVyn9JUojZ0UzwPYZ8QgSGHbKKJOlfylH5mjbJSKPNRwKXI3xd6cx86jP7d4roCY_mFt_EqrCcG_0ElNpKNYI9J1HCBoBMQ6vyU_TFU1jg9OSR-M0Jz5od8lHXZPPIJt2QVakp3v4c8ZOkkfiNXy1tzKPW04BtbWgMLKjXYdnBLYA_d_pzR9WPtXxe5Gu5VYcl7tZ71sCu22bH_YNBy0llcp4yLTXuKCugCUfnPxeMTJ-UyfEUCUdkUhpj9fjVb3AhMBVx-TLs4FM7muRybW4eSGYEbxVfab4YMMj_WFqyxAKMiZ7sYUtP7R-m7ilwp6RFWuDMI8zXDOhfiHVA_9a_RKmPbYqFFTpbopbPHyy71kOnzEe2N9YpPTAbNvhZljsYlW99a5WIAVH9IWPAGLTLDtIFrFWwHvWpPX9Z3zQn_olvq93WahkdgeZ6EznYOssXSaulidZpqAgp392iQoC_UmULClgP9QAqUOU9BMV3_8ZpsEE3jxSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfb2ceb1b.mp4?token=e_MPyM53YjZO2dxo1nI_SPVbaIOyIfXt3h6IwhqCNE9UWISsqLieAYzeKvCgLZRPk9reJcLL3vdHJjISgHqRTdtUFN0T9f8OAg-cdJchPi-EL7Cai7uIdyVwyU9zEL3-7m3WtBVKJckO0OHKlTxJDeE161rb44GrVwX0gobA4odw1eYQi13aZMVyn9JUojZ0UzwPYZ8QgSGHbKKJOlfylH5mjbJSKPNRwKXI3xd6cx86jP7d4roCY_mFt_EqrCcG_0ElNpKNYI9J1HCBoBMQ6vyU_TFU1jg9OSR-M0Jz5od8lHXZPPIJt2QVakp3v4c8ZOkkfiNXy1tzKPW04BtbWgMLKjXYdnBLYA_d_pzR9WPtXxe5Gu5VYcl7tZ71sCu22bH_YNBy0llcp4yLTXuKCugCUfnPxeMTJ-UyfEUCUdkUhpj9fjVb3AhMBVx-TLs4FM7muRybW4eSGYEbxVfab4YMMj_WFqyxAKMiZ7sYUtP7R-m7ilwp6RFWuDMI8zXDOhfiHVA_9a_RKmPbYqFFTpbopbPHyy71kOnzEe2N9YpPTAbNvhZljsYlW99a5WIAVH9IWPAGLTLDtIFrFWwHvWpPX9Z3zQn_olvq93WahkdgeZ6EznYOssXSaulidZpqAgp392iQoC_UmULClgP9QAqUOU9BMV3_8ZpsEE3jxSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان با رئیس‌جمهور هند دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/461506" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmy7DEYil9SFClMd7WIDwK3-Wg5W0wRFADQBhXnbZmNqMBdJFgegogzuQF6AU6o_xbvh7rHUvdGuqC0tLuDinR9BRYnNOaXGnbpx6ljxEp81l_XrncJXmQ_02PC4uUYTT2d0qSBGhtEyKunikvy05rkwa1eWUzBtjamwer3J4-G8OW-AJ_1HV9bR_bfdORBgGJ20znUHIASD2u0s0vQrbh_Yh1jD0HBvP9zL220_e1PwDDCg2KnIDcKENd4Hm9kPCVnpPIQD5colak1wRs-11AjMnWCeVYce-LrXm6wQh1VS2jR11e6crq3OGUHU4Ts4nWh3KmkhcxH_s1pLXLWwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد ۱۲۳ مگاواتی آسیب‌دیده از جنگ به مدار بازگشت
مدیرعامل شرکت تعمیرات نیروگاهی ایران: واحد گازی ۱۲۳ مگاواتی G15 نیروگاه مبین انرژی در منطقهٔ پارس جنوبی که در جنگ تحمیلی دوم دچار آسیب‌های شدید شده بود، به‌چرخهٔ تولید بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461505" target="_blank">📅 11:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO3Swn83cFir_t9u6CmJZmqveWEZ38t3IhpYO2OCFMI0h-RK8pchO4tdH9FSt50mNdFhPyyUGoJytXSiSvgxe5N14VFBj10NRUNMDPsZbaxuEPJjfcq8awguJORKwSuM3e8bVBD1NONxmc7mbAqvTkR5Yb5j3eu-FwYZy_y7vkV7NpbJk4C-Axc_zPFIpAIM_1PO80Lnhood9QreITjkEJgPs8ape_J1GYJcqPw-YR9SqF7vF1F4yvMb-E3epr8MIyZPRML2ctjvlpCT3ASxWcZkxBpBWTJxXrdkG3bbvqs2yl655H7eVuMUQ1TEYX7Js9Im2SHfi6J1OPR2qGFoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان در حاشیهٔ نشست بریکس در هند با نخست‌وزیر مالزی و رئیس‌جمهور اتیوپی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461504" target="_blank">📅 11:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghAilx2lO4QsmrHHcypiMCj0gEBNjpetD_0LVbMDuDPXik3kmoR5R2qUlUKhnSyqcZrhXQPEO4vri3MJ8NsHv4gi5Q_sT48JTixW2StAg--pEvlZhcXTY83LOrXGeCmvOAr_tl_SgXszRe9Uv9xL_opneDSHZ9P-UTUHxi7iDSAv_yOhYounyhL6em1LsX_EJ91DiQHbFEXuYWI8GxN0GIQg411Igqp9BkRD2LI6M4Mj-FXOLU3y_wvRMFRGHb_2Msqjp8W_IVbHJfvG4T_KWH-niqCgkNHZcIm9gMTfyrCJ408WZMIEH6SKr-kFTAzuWqJzYkCfso4xrBW2lkrMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رگبار و رعدوبرق در راه شمال و جنوب کشور
🔹
هواشناسی: درپی فعالیت سامانهٔ بارشی در بخش‌هایی از شمال‌غرب، سواحل دریای خزر و دامنه‌های البرز، امروز و فردا در این مناطق رگبار باران، رعدوبرق و وزش باد شدید موقت پیش‌بینی می‌شود.
🔹
همچنین در ۵ روز آینده، جنوب کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان با رگبار، رعدوبرق و وزش باد شدید موقت مواجه خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461503" target="_blank">📅 11:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فدراسیون فوتبال ۲۰۰۰ دلار جریمه شد
🔹
کنفدراسیون فوتبال آسیا، فدراسیون فوتبال ایران را به‌دلیل تأخیر در درخواست مجوز دیدار دوستانهٔ پرسپولیس مقابل آلانیا اسپور ترکیه، ۱۰۰۰ دلار جریمه کرد.
🔹
فدراسیون همچنین به‌دلیل ارسال دیرهنگام درخواست مجوز بازی دوستانهٔ تیم امید ایران مقابل کایسری‌اسپور ترکیه، ۱۰۰۰ دلار دیگر جریمه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/461502" target="_blank">📅 11:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTsZosIjsA5xmuYTBgi4VINChbKd46GEtk7K6rEtu9ZuWy2BQdvsk7L5rsGfnaBeLklbRIP6CL0vmIGVkVOWLyZg3zLQZxvEBxO7uRNYJB62BeX9Pmk2ItwvVeH5_ezuc5uxnRi95zjp0245uyIResHajPAbueQg28_GG4ildUIIRzSWfFRrnFXj9O7q6LJJ18f5SzH1X6n1MxcvQYWexx-i6F7zQhUMtFO_9Ncs-LIjTjfbi4Eej_eFCHy2CUdHNTPIrjNV0_X9nsii-ZfIb0uFHP_0tMhROtvyp5B9DB7vWDSpJYYs3YpQEBfuOOgEtJntXc9c2B7MO17Bg9FMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ سردار سیدمجید موسوی به زوج جوانی که حلقهٔ ازدواجشان را به رزمندگان هوافضای سپاه هدیه کردند
🔹
فرمانده نیروی هوافضای سپاه در پاسخ به زوج جوانی که حلقهٔ ازدواجشان را به رزمندگان این نیرو هدیه کردند، نوشت: برای بنده و هم‌رزمانم در نیروی هوافضا جای بسی افتخار است که جان‌فدای ملت بزرگ و عزت‌مندی هستیم که همچون شما گرامیان را در دل خود جا داده است.
🔹
هدیهٔ شما برکت و مایهٔ ریزش لطف الهی در بدنهٔ سازمان ما و ان‌شاءالله موجب خیر در زندگی مؤمنانه و انقلابی شما شود. ممنون لطف شما هستم.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461500" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkc5nXjOakdzRzM3Q9PCJvncoQffu88WxGYg1Bn2X1JUIi8tEyhIHpxUAKQIjIPQJUBoxwwUfWiaKkxTU93Q7sY52tNLzTfrfP95Rl7c7ZTAASxNkdTChcFnC64v8oEXhitT69tMsK-tMsVJyTe9ynSBRKZ1JSAN9QcCCLq6jrq031hyFjX_oor49r7FVa9KA7eRCu1iiUV_zfX_ztX6umj_iSoTF85kwvWC7ebQEhxxEXNsenV_d_mXY9LCxDWhftssb2eGOxEMsgSdYo_igAPnuM-GhdUiPj0S4FTGZyEGPjceYjRPShBG7TvtskEj_orFtS2dcLa7Xq_h08LHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت بنیاد آیت‌الله رئیسی از ادعاهای کذب یک بلاگر اقتصادی
🔹
بنیاد شهید آیت‌الله رئیسی از یک بلاگر اقتصادی به‌دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد.
🔹
این بلاگر مدعی شده بود در دولت شهید رئیسی از او خواسته شده مباحث اقتصادی را به رئیس‌جمهور آموزش دهد و این مطالب نیز در قالب انیمیشن‌های کوتاه، کمتر از ۳ دقیقه، تولید شود؛ چراکه به‎گفتهٔ او «ذهن شهید رئیسی فرّار است».
🔸
گفتنی‌ است میانگین رشد اقتصادی ایران در ۳ سال پایانی دولت دوازدهم منفی ۲.۰۵ درصد بود، اما رشد اقتصادی کشور در سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ به‌ترتیب به ۵.۶، ۵ و نزدیک به ۶ درصد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/461499" target="_blank">📅 10:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdf7fbf08.mp4?token=i5-k6Gbdow4aP7wSbOLnsvjv2-y52oIdXsHXmY2FIO_A8YLzXhQ9CNS_2GZVcWMV6h-ez_fx0GrkpfAB8bC5Zw4vRgti111pSQrk8lt5sZA61UHXawMkp9BqOUFtkK3MFdXWtj0NiPLDLi0HIjhx5v8dj6tLpsAF30w82TwVCk1GVSyICUm19POuA2ArQbe953LgsHxA0NVxdShnZ6m12keThj6dY-PerIeDAUXieVOIFL8Hl1C58qGmZt7EF-upRzRjeuq9917UXBGSJq4iK1UPfykowImo3DM2pqtjLm7zLCP5UgsPoU8vuHyzHMFe-cn73x1TV0DmVAnNdgWgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdf7fbf08.mp4?token=i5-k6Gbdow4aP7wSbOLnsvjv2-y52oIdXsHXmY2FIO_A8YLzXhQ9CNS_2GZVcWMV6h-ez_fx0GrkpfAB8bC5Zw4vRgti111pSQrk8lt5sZA61UHXawMkp9BqOUFtkK3MFdXWtj0NiPLDLi0HIjhx5v8dj6tLpsAF30w82TwVCk1GVSyICUm19POuA2ArQbe953LgsHxA0NVxdShnZ6m12keThj6dY-PerIeDAUXieVOIFL8Hl1C58qGmZt7EF-upRzRjeuq9917UXBGSJq4iK1UPfykowImo3DM2pqtjLm7zLCP5UgsPoU8vuHyzHMFe-cn73x1TV0DmVAnNdgWgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دانِ خوابالو» روی «جویِ خواب‌آلود» را سفید کرد
🔹
پس‌از انتشار تصاویر جدید از ترامپ در حال چرت‌زدن در یک دیدار رسمی، منتقدان با اشاره به لقب «جویِ خواب‌آلود» که او در اشاره به بایدن به‌کار می‌برد، خودش را «دانِ خوابالو» نامیدند.
🔹
انصاری، عضو دموکرات مجلس…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461498" target="_blank">📅 10:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461496">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cute8aj7UHyEIIeOJ5sZ6h19iKek7wMDw-7TIaRF3oof8uS7hTKV_ZmQp4dfsJNJi6cUDwB6Hl1UOb5UIw-I14lUATKCWcDJh3u_Lc-FIK3Z0pnq3DMzSbz5NsNfMKFVF8Y4AEWjJ0J33O_ADbPxoyf7kSXNo1jh2805QL9gNSPTnKXwikXMtJnrha4pa42JkiJDS6JM-odTn4hHeb3cwDyPYMjpYPLj13ivSg6qpphy5WJBGchsH1T12FhRWmxd66R5JIxScBm-D2HxsBpkxB6kltf6FIuuSihT5BfNF_zkvUBRp2GRbYd2BupHpwcyJbvCReqxNS0URp2lvjbejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2xO-cnBxWSriglBh9W0XQp65SC9NoVDL5euDbSIlWtHuJyG-SxcEv6iGjfTaFvfxozibZv-g309E-70BheCiU-bE_WgkK95h9LfzZoJfBUo0e7V6HpWpqUagLDh4r9LfpCI4ekY228_cMaAuwqbqiTiK44nO0NdAIZ1X2SFmPvJxaZxSTCWXMhhLq6Ks_QyOCDM4CfFjyZ74Fn55WpfI8lWC7DUtBEAWqasQ0fRzkKjfXPhshIp2MpuNxC4iamKdq-uMqUG8CiTZ92EGOITzhjgKDmOtyNdO2o6DoGbwr7kSfV9_ZJf7jfVOuW3OXUfN_4LBA8pRDj17yD4hwDc3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا چون نمی‌تواند با قُلدری مردم ایران را وادار به تسلیم کند می‌خواهد کاری کند که مردم به‌خاطر نبود معیشت و امکانات تسلیم شوند اما مردم ایران تسلیم نخواهند شد
🔹
اگر این‌ها مرد جنگ هستند با نظامیان بجنگند؛ با نان و معیشت و زیرساخت مردم چکار دارند؟…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461496" target="_blank">📅 09:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461495">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461495" target="_blank">📅 09:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461494">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Htw4lvDkTDPunljnz8-zXNqi9MYnDtQNrhHjpz3L9glbNCWvmdXPiXvqrPu4AE6ZcBROCEJ1SbxBaH0bkY0LA2Z10-OwtpNZ0h-dxUbT_9s5YJnj24QHWVmrGkxCRCyisESWR8jdwtJjyTjSRPmqzLGqj3SpdX4iYJkwxxqHCs0ZPWAPN65R8yGEn5GkIaJM7GPtFlCFSTd3_pIhkOVTnxMsV--ed5FbOkf4cUaoXIoXuvFWWz8xt0sv7e_OXBER5nQzhnSbBVRAF9IRmSMyuox2P_zvCFW6QMqGHG047PPivq51oiWAkKO-Rfpl7B79rxsNE1UOn-hsfVjQb7S-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/461494" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461493">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdrp4gK-RYb1r-s1QNVvNFaw56X24OW3gVhhAKnj9FBozrhm3bCxBJYYInJPVYZlphC7NHOHde8cSgboPBvdazzRbR19PJX88EH_nNWspuYw6Qe26LPS7O--IF0AMbsR_PUgeDh0_dz6FQiF25Z024WySKoD8U4bZRxumQoT0WuHbWXj5nAUrAMj6YQDdgaCpK_FW3PsSFD6Ku_AugYUYACeCRDv8933TTty1KggVi-QGcXraN8Z4A3-8s3eJ4G20TYtiSJNFJDTKvEbq5QQOIWEr0N8lOzv-CH9Rt9fdGPFWCSEKpn5mPEyvjVafmNU0NQDQ7OzoR5YOUsMazs-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های جدید حوالهٔ ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۶۳،۴۱۳ تومان
🔹
یورو: ۱۸۹،۶۰۱ تومان
🔹
درهم: ۴۴،۴۹۶ تومان
🔹
یوآن: ۲۴،۳۶۴ تومان
🔹
روبل: ۱،۹۳۹ تومان
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461493" target="_blank">📅 09:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461492">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرماندار مهران: مرز مهران باز است و تردد در بخش‌های مسافری و تجاری در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/461492" target="_blank">📅 09:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461491">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461491" target="_blank">📅 09:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461490">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvcugz3jTnSiiAnENvx9DlQqr5nCH4fkQo6cOWsFcy20tyyDYc65f89nThBQxQDGKeNYFf6Xov9gKuH_-Sfsp1hJSzlBVWbLj5gLqj4mv4AcVD39BV1aUlV6TH8MaeOqH3kX0CHL07UyT-o4X_bEUBaDUQJ4FAbB4Q-mdcu1DUH7eLxOfu5HOzFeewsr9_1xj3_oPHEfk7jAglD_jHXdZ2dt6I7h2DdUAMmzZYMG0C6CW18IxQQ55VLQnpVAbpTsEoFY4MdcPV82KNlM-MtQOxZEf__Gki08QNKyxfGRPt6zMON68m23q_Isg0BpRbXefgWfrbop-QrHByUVPQTBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ هواگرد سعودی را سرنگون کردیم
🔹
ستاد نیروهای مسلح یمن در بیانیه‌ای دستاوردهای خود را نبردهای روزهای گذشته با مزدوران سعودی را اعلام کرد.
🔹
۱. بیرون راندن نیروهای سعودی از ۶ منطقه در استان‌های تعز و الحدیده، با مساحتی کلی معادل…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/461490" target="_blank">📅 08:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461489">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عملیات پاکسازی یک خانه تیمی در سراوان
🔹
بامداد امروز عملیات حافظان امنیت در شهرستان سراوان برای پاکسازی یک مقر عوامل ضدامنیتی آغاز شده و همچنان ادامه دارد.
🔹
یک منبع به فارس گفت: از حوالی ساعت ۴ بامداد امروز یک عملیات منسجم علیه یک خانهٔ تیمی در شهرستان سراوان آغاز شده است.
🔹
گزارش‌های اولیه از زخمی‌شدن و هلاکت تعدادی از اعضای این مقر در جریان این درگیری حکایت دارد. در حال حاضر تلاش برای دستگیری عوامل و پاکسازی نهایی این مقر در سراوان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461489" target="_blank">📅 08:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق
🔹
معاون استاندار خوزستان: بر اساس اعلام مقامات کشور عراق، از بامداد امروز مرزهای شلمچه و چذابه تا اطلاع ثانوی بسته شده‌اند و هیچ‌گونه تردد کالا و مسافر از این مرزها انجام نمی‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/461488" target="_blank">📅 07:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ضربۀ ایران به زنجیرۀ پشتیبانی هوایی آمریکا
🔹
ضربات اولیۀ ایران به پایگاه‌های نزدیک به خاک خود طی جنگ تحمیلی ۴۰ روزه مثل قطر، کویت و شرق عربستان که فاصله کمتر از ۶۰۰ تا ۷۰۰ کیلومتر از مرزهای ایران داشتند، این پایگاه‌ها را به‌شدت آسیب‌پذیر کرده بود.
🔹
اما کاهش چشمگیر توان رزمی این پایگاه‌ها، فرماندهی آمریکا را به چاره‌ای اساسی کشاند: عقب‌نشینی تاکتیکی به عمق بیابان. بدین‌ترتیب، مهم‌ترین تجهیزات هوایی و پدافندی به دو پایگاه دوردست الخرج در عربستان و الازرق در اردن منتقل شدند.
🔹
با انتقال دارایی‌ها به این دو پایگاه، یک واقعیت تازه شکل گرفت: تراکم بی‌سابقۀ سامانه‌های پدافندی و لایه‌های متعدد دفاع هوایی در اطراف الخرج و الازرق، آسمان منطقه را به یکی از امن‌ترین حریم‌های هوایی تبدیل کرد.
🔹
شبکۀ هوایی جدید، ترکیبی از پرنده‌های بدون سرنشین مانند MQ-9 و MQ-4 و همچنین پرنده‌های شناسایی رژیم صهیونیستی و از سوی دیگر، هواپیماهای سرنشین‌دار از انواع E-11، E-3 و E-2D بود.
🔹
اما در میانۀ این بن‌بست تاکتیکی، یک تغییر رویکرد همه‌چیز را دگرگون کرد. به‌جای تمرکز بر انهدام مستقیم سکوهای پرتاب، تیم‌های اطلاعاتی و عملیات ایران تصمیم گرفتند شبکۀ پشتیبانی و زنجیرۀ سوخت‌رسانی پایگاه‌های دوردست را هدف قرار دهند.
🔹
منطق این تصمیم ساده اما هوشمندانه بود: با وجود مسافت طولانی، جنگنده‌ها و آواکس‌های مستقر در الخرج و الازرق برای ادامۀ مأموریت‌های خود به سوخت‌رسانی هوایی وابسته بودند.
🔹
عملیات ترکیبی آغاز شد. در این بازۀ زمانی محدود، چندین پهپاد و موشک، هم‌زمان با یکدیگر، نقاط مختلف این زنجیره را هدف گرفتند.
🔹
نتیجه فراتر از پیش‌بینی‌های اولیه بود. هفت فروند سوخت‌رسان نظامی آسیب جدی دیدند که از میان آن‌ها، دو فروند به‌طور کامل منهدم شدند و لاشۀ آن‌ها در بیابان به‌جای ماند.
🔹
دست‌کم یک سامانۀ پدافندی تاد که از گران‌قیمت‌ترین و حساس‌ترین تجهیزات ضدموشکی به شمار می‌رود، به‌کلی از کار افتاد و منهدم شد. یک فروند آواکس دیگر نیز در جریان همان موج هدف قرار گرفت و سقوط کرد.
🔹
مرکز تعمیر و کنترل سوخت‌رسان‌ها که نقش حیاتی در تداوم عملیات هوایی ایفا می‌کرد، به‌شدت آسیب دید و عملاً از مدار خارج شد. حتی ساختمان‌های اسکان نیروهای آمریکایی نیز در این حملات تخریب شدند یا دچار خسارت قابل توجهی شدند که نشان از دقت بالا و شناخت کامل از موقعیت‌های حساس داشت.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/461487" target="_blank">📅 07:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461486">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هوای پایتخت «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۷۷، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/461486" target="_blank">📅 07:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8cc0bb73.mp4?token=T-1_oXp2gJ2n4MtmGftr3FXCO6Viws1oev7G_Xnw9mP5wkmALr0xRXYXoeAAxQRkobRQF7fwpEUK4xadr1j0GjnPNYxjSN07fg9X2p6wPQE5Cf6KNH-OaG3nOFFLHzISXUeAQ1_FLsFMZNRI7aQwKEQ9hTJ_7FoDtiEXeF6MFFgutHREDFehrj9vpr3iB_sqzJociI2wrhU4l7CdrLGlnG0nSQGzBuCIgPzIcr4Vk1EUn1jFvnZw5J1d2t83ux2ohReThNL5tiKqWOA31EHubnraweHDVH-l-x5bcc3xqu8bxA5YxrWR5dmAE2DCMI7OU_gb7Vkt3ORWdDdU9ZJ_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8cc0bb73.mp4?token=T-1_oXp2gJ2n4MtmGftr3FXCO6Viws1oev7G_Xnw9mP5wkmALr0xRXYXoeAAxQRkobRQF7fwpEUK4xadr1j0GjnPNYxjSN07fg9X2p6wPQE5Cf6KNH-OaG3nOFFLHzISXUeAQ1_FLsFMZNRI7aQwKEQ9hTJ_7FoDtiEXeF6MFFgutHREDFehrj9vpr3iB_sqzJociI2wrhU4l7CdrLGlnG0nSQGzBuCIgPzIcr4Vk1EUn1jFvnZw5J1d2t83ux2ohReThNL5tiKqWOA31EHubnraweHDVH-l-x5bcc3xqu8bxA5YxrWR5dmAE2DCMI7OU_gb7Vkt3ORWdDdU9ZJ_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض رباتی!
🔹
حدود ۳۰ ربات در مقابل ساختمان وزارت امور دیجیتال لهستان در ورشو تجمع کردند و خواستار نظارت و قانون‌گذاری بیشتر در حوزۀ هوش مصنوعی شدند.
🔹
این تجمع با شعارهایی در حمایت از تدوین قوانین برای هوش مصنوعی برگزار شد و نگرانی دربارۀ پیامدهای گسترش فناوری‌های خودکار و تأثیر آنها بر بازار کار را برجسته کرد.
🔸
حضور ربات‌ها در این اعتراض، اقدامی نمادین برای جلب توجه افکار عمومی به بحث تنظیم‌گری هوش مصنوعی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/461485" target="_blank">📅 06:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwvvQXl6TRZH07-ExXUMEwJyba-PAKhJRJ1sgRtw-ST8U6DH4ZRHlQ3Ka-1QHPd0ojiPpCohO2uolIpAJW_xCewX5IOcqyEtkHAQujGmAzb5ULWHaa_bU9_48YK6-r3gpsSCn-b6uM67KWuE1U_bsLGNRfi1kS3CZ4v2FedBBiFCnecptgAk8mZNmRoeAFvRz5XhTgyEY4TcwCvfzP3Bf6KvPHVbh479O7c_KlDmFgQE_9oIPC7JYhuxunQOh_UcIfgUsH-oa0Xa4qYGRGITBKeSxYp-FFdj108CIgwa-1fifF3It_FRXl5RWAoNkPGURytGaoMArMK3vIvWWa6JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس انرژی اتمی: کرۀشمالی یک مجتمع غنی‌سازی جدید راه‌اندازی کرده است
🔹
آژانس بین‌المللی انرژی اتمی اعلام کرد، کرۀشمالی یک تأسیسات جدید غنی‌سازی اورانیوم در مجتمع هسته‌ای یونگ‌بیون ساخته است که می‌تواند ظرفیت استقرار حداکثر ۲۸ آبشار سانتریفیوژ را داشته باشد.
🔹
آژانس تأکید کرد که برای رصد فعالیت‌های هسته‌ای کرۀشمالی از تصاویر ماهواره‌ای و اطلاعات منابع باز استفاده کرده است، چرا که این نهاد از سال ۲۰۰۹ هیچ بازرس مستقیمی در کرۀشمالی نداشته است.
🔹
کرۀشمالی بارها اعلام کرده که جایگاه این کشور به‌عنوان یک دولت دارندۀ سلاح هسته‌ای «برگشت‌ناپذیر» است و آژانس حق دخالت در امور داخلی یک کشور هسته‌ای خارج از پیمان NPT را ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/461484" target="_blank">📅 05:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBINGIHpCtsbPRoM0vdhY6Hqu6X-TpVSYjD_c6oqHzMR9faWnof90D98nOy8b4EJNtTgOONRdJ0Aa1SWGJQ15WercaO5-hQioRWkqVoB7m-bl3bEMMg5RkW-kKVg45FGN8PShysZw_3RuOcDzIwhAB6ROtNArkN6s6AqqnqpcCtozzPP_TxCZoJ_pQcvx-R0b1J5Bu4v-y0vtk2n3i1V-BZvK5wouR1-aCTAZ8TCaMro9-JR0LIcR2GezcI7dR-AwmsnKR2o4Z5ceNT6Yc_fB26XvmCrwc_abXIb2540RM90myN6K3vhkokSw3TU0RmbAuaWmyqK7-Mp-qNTxyolXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی برای یک پروندۀ قتل شاهد ساخت
🔹
یک وکیل مدافع در نیومکزیکو برای تهیۀ لایحۀ تجدیدنظر از چت‌جی‌پی‌تی استفاده کرد، اما بخشی از اطلاعات تولیدشده شامل شهادت پلیس و شاهدانی بود که هرگز وجود نداشتند.
🔹
دادگاه عالی نیومکزیکو این وکیل را به‌دلیل ارائۀ اطلاعات جعلی، ۵ هزار دلار جریمه و به بی‌احترامی به دادگاه محکوم کرد.
🔹
وکیل گفته بود تصور می‌کرد چت‌جی‌پی‌تی یک خلاصۀ «ضدخطا» از پرونده ارائه می‌کند و از توانایی هوش مصنوعی برای ساختن اطلاعات نادرست اطلاع کافی نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/461483" target="_blank">📅 04:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=qkBOjduJO6kvlHYOWXwkSOIa1OU5fqL6hIWfIrrECnzgBGknDNSHyy3vkzkD56FGUKgtpMIrsYi6aeFx8O9LxEJeFrpBS1oo7OUGiAbEazXF8hgdRWEKaBdHnsY7Zblcc8p-_LlSp4FExn6_Oz34FIin9uxhimqAbAluXDvz1kpXmBCJbUmOcBtNLlBuRkqjmBOLASE-V6GsBazMPhXWgwzX3bQipK03JDWhX2DzUcYuc8qpwPHWwx6pdFJa_3b8JJ1NuE46E25QckDac1TNtupfhyLLm7VTUjIbvLPk9BHNncwYSIlF0NAT726VOpowJn4fudWCN1Ya8UTYWQFnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24f8e1f79.mp4?token=qkBOjduJO6kvlHYOWXwkSOIa1OU5fqL6hIWfIrrECnzgBGknDNSHyy3vkzkD56FGUKgtpMIrsYi6aeFx8O9LxEJeFrpBS1oo7OUGiAbEazXF8hgdRWEKaBdHnsY7Zblcc8p-_LlSp4FExn6_Oz34FIin9uxhimqAbAluXDvz1kpXmBCJbUmOcBtNLlBuRkqjmBOLASE-V6GsBazMPhXWgwzX3bQipK03JDWhX2DzUcYuc8qpwPHWwx6pdFJa_3b8JJ1NuE46E25QckDac1TNtupfhyLLm7VTUjIbvLPk9BHNncwYSIlF0NAT726VOpowJn4fudWCN1Ya8UTYWQFnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات پهپادی دقیق روسیه به نیروها و تجهیزات اوکراینی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/461482" target="_blank">📅 03:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97bf68b8d3.mp4?token=ZwWDJHrBQj53pHDsez8vTeuJ4tyszSvkuTsSf8zwChMUQLptCbEuKR_OBoxaEHLOUsBcckMcX0OFLsAdW6lFnv6DYt3_g3WH_Ah8E5le8ePzV5It0cXaOtVY-GYHat7gwMpzKUa6nfK30B07xUYagS9kLXMSbZ3K7IaWLdn3BReK3UfkEkyrMEdTygDgl_OUe28yH6ZPCdXpSO5vaB4V9ns-O6PNYtoxeUMzosLZysurxbLvDE4-aMD-TGiAm22k_-UXxccxf0uO1WEoZuXhV8P2Z1TXkEaN1KCrTyjvvLYcMEpXucxHcOn5gkIHUkz_8YO9r88DsO90k8wYRM9tFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97bf68b8d3.mp4?token=ZwWDJHrBQj53pHDsez8vTeuJ4tyszSvkuTsSf8zwChMUQLptCbEuKR_OBoxaEHLOUsBcckMcX0OFLsAdW6lFnv6DYt3_g3WH_Ah8E5le8ePzV5It0cXaOtVY-GYHat7gwMpzKUa6nfK30B07xUYagS9kLXMSbZ3K7IaWLdn3BReK3UfkEkyrMEdTygDgl_OUe28yH6ZPCdXpSO5vaB4V9ns-O6PNYtoxeUMzosLZysurxbLvDE4-aMD-TGiAm22k_-UXxccxf0uO1WEoZuXhV8P2Z1TXkEaN1KCrTyjvvLYcMEpXucxHcOn5gkIHUkz_8YO9r88DsO90k8wYRM9tFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌خواهی کارهایت درست شود؟
🎙
آیت‌الله مجتهدی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/461481" target="_blank">📅 03:26 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
