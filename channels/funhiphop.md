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
<img src="https://cdn4.telesco.pe/file/gfnNtmUFhPflXExhG2u6CNxrMs1c1hQAKsEvrMvB-yrw8m9szMBzsl2wumXHBw250d6_Ii-N3NreLpFQsuMTd_4-IsgsjWH9tuZBUVivGQZaIB5XsZUf5aQ6nO7bL7DzjxzEWV4ebb9TPnDlUD5UJdhj8mK_rLyyXKNC-0TG4blWujcwbDQ7rLdGigIQtpUj7qnPQ1HyqXglhCqbb1HZahN0Jvhq_5EsYCqA3nJHNm3qv_YuTWu51sTGsGeOmAX20nYValV28x9XxigKnQWmmrKFx22jhxeFbilGeaGGdZK9v9io3nBxUGcDn4EI-kr-E2bW5C8I2VqSle8IKiIQ_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 04:16:56</div>
<hr>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7rpJqd_2VdiV1TGl7ZeqFBoCbShFSPKBygllcIncvHVqbxqEBwCfoPM9gsARY6Afa2qgI-5SdkpSEaFwFjy4oohCHkghPtY1NhJBRmF4U7c5nlvf7rWhR6Fy4a2rvFpud-DLEcZ7cM__vK9wmcq1dKyTkv6mlKTMyFnITvCBs1MPQ_0PLiwuQ2SR08FttdwlDujXxWA57aImrDWz6-opHQfASHKbH6qA5PUQxjCpzBa2Vb2lF7bx6IqwTNMeh5GRScgEWb2eWN3JFjB1a1w3bvFlaQuYqNushH5Pp4NIi1n04RKSEckmCNWIcmgFuJIYc6sWjlAud4iltbPjXu-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نیویورک بگید مسعود اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/funhiphop/83950" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آخجون ویلسون دوباره مست کرده</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/83949" target="_blank">📅 01:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر پسر عموی مهدی چیکارا میکنه سپاه یه موشک ول داد سمت یه کشتی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/83948" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044b34344.mp4?token=uLHXPNb691m8cjxivOJ_C5V5RyIwm1B6iJ-EPmRoZGnFyLi_YAx4qpJh4YFHxLlKAASbXUEV0HxqqY6kD9OB6VnNZ56apKGVGZ2aW2vmsxiOPzXV8Ud4tul5QCjoNhRV2pVFRtPh0OcKP47iVWuE6AcheP66eFMx7BJOLqs6irrvFGtCijfWPDGg7WPpuUnD-2RlPoc6CnAfdcMxBRnoKdS2mwbu-V9yrks2ilm-7VjbFoo5UBDexCvfrHsluVw-CnKuSTPNPOR0lRUF8jAo3VVir4ymhfWZ8J8Q_YmBBkn3LzHmpm5JuRWpX6fdwJhNWoRFgW6lJ-R6FOBvHO_9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044b34344.mp4?token=uLHXPNb691m8cjxivOJ_C5V5RyIwm1B6iJ-EPmRoZGnFyLi_YAx4qpJh4YFHxLlKAASbXUEV0HxqqY6kD9OB6VnNZ56apKGVGZ2aW2vmsxiOPzXV8Ud4tul5QCjoNhRV2pVFRtPh0OcKP47iVWuE6AcheP66eFMx7BJOLqs6irrvFGtCijfWPDGg7WPpuUnD-2RlPoc6CnAfdcMxBRnoKdS2mwbu-V9yrks2ilm-7VjbFoo5UBDexCvfrHsluVw-CnKuSTPNPOR0lRUF8jAo3VVir4ymhfWZ8J8Q_YmBBkn3LzHmpm5JuRWpX6fdwJhNWoRFgW6lJ-R6FOBvHO_9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یعنی کیرم تو این زندگی ای که من میکنم
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83947" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ناموسا بعد از بیف وانتونز با پوتک هروقت چنل کوروشو باز میکنم یه کصشری به پوتک انداخته، بس کن کولی خسته شدیم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83946" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvSAKb5arB9HY5L4k4uWlQxtXPUQa3GlTCkcc7PyXoLLkXKX1ybnOwHW7pZVNGOmZYkbpxI4lWYzIJclHnTbHn9IzcGmB0WgSSalkQ7Bp3qWAIeWSJGvU0ZXQBl4A2aSNzrMpNQjGwAufbRwoSdSptHxY7KLuArHBDeZFKXhU93Dq9Ygm15-IJc3P2MsklAkUqXwNI-zrmrG5kzJyHvwBHdvw_Eaxb34pBI6i_3WTgIuR1JlS5JanAC2pr5rgEsOyGADcs1KgjwtRsaTp10EQRBOZIfX9F7Qa8hw0fr0xtcKGQwa7kHtgUX5uvCxITFikTZgIvoFDmdrFe0hfeIVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKoEpqwNw0MWu1-gSoyW3pwy9-aEiZENopWnhPfxRTM-GsvbWx02tif47Pj9kFv-Cb6EGLEt2VMMVX7knBmtAGYCx1ejwFQR_JYwXe2sGZvE55QGv9hVpZPeBmreJE4WJpEaxAnaiuwlPS5sux_XHeZa-OMbqoLegRVYRpnwK_wI4lj1GDTJwqMP2LBEIR63yEp4IOFGaPgzq31zDFc7NLEB098ehFBWjXv-hHDQk0qfdlAeENj-PwzCg71Jn0ST7QKxrZnP5J0qwiqdPyyj7Po13wuIKQnyqLMSPWFExfyyQFaQBWWYS_7cDIbWmX-vv3WT8awmu1ozWiSyWNRCfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پول دونیته ها حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83944" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=Y4Onx3d-2-L8RQ13xh2JhOLKjYUgVwx1jq82pBANn5lY2Y36NdQ0H5HjOU242Nj4Jf7_8FR1bR4qjVxc9Y5GnvpKK5VfYb_VbPzmVPQ9rwTKuH8mp-0ht7Xzqyb7wIWKOI6FP-WcjIipsyhPgMkldo-9yKuE3zgPMX0XZmuVhJvZmeZ8a51ZT-xwAu5eGRN5tMcpfv2ysDSJP3tifyuaf8AgiVH0pvck11RCKoJsEgxiF5LxrU0Z929NVU-cmjaoMpg-As2UcFhVzuZfQOwmPHP_fWYAP9xhaYqorrzpUAP-2dEUBi1r4_WX6re3G-tzrfUEvVrUqdkKF2r3pUhNsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=Y4Onx3d-2-L8RQ13xh2JhOLKjYUgVwx1jq82pBANn5lY2Y36NdQ0H5HjOU242Nj4Jf7_8FR1bR4qjVxc9Y5GnvpKK5VfYb_VbPzmVPQ9rwTKuH8mp-0ht7Xzqyb7wIWKOI6FP-WcjIipsyhPgMkldo-9yKuE3zgPMX0XZmuVhJvZmeZ8a51ZT-xwAu5eGRN5tMcpfv2ysDSJP3tifyuaf8AgiVH0pvck11RCKoJsEgxiF5LxrU0Z929NVU-cmjaoMpg-As2UcFhVzuZfQOwmPHP_fWYAP9xhaYqorrzpUAP-2dEUBi1r4_WX6re3G-tzrfUEvVrUqdkKF2r3pUhNsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکارو یادشونه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83943" target="_blank">📅 23:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83941">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRapBadVpn - فیلترشکن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_9Wdf6ijNgU9m9oxWK-0OhPyyXtyXkBcIw77NFD3sf9z6hd7ZGo_AojFu7Ns_5MA53JCql3k3HKAwZ__fQIGBBZEn2H-r1CjA0mcadbUEP4uJcLvwfGycb3GIw2mrrN62YeRC2s5ezgBoOS8uU4iEjnTo-pg9zJlVcpyC6Zks7VMZai9E-0Zi60Y_BLQJPb-z25NI01lEgosM0QgDZfjhFnnE-Y_zzBSlr8_JS1WCXCM9PFdXmWL8cDPlVdXmNjRobS63I2KRafCWR6yM3mkx5jOrXxuI-Rd4sPB-WLGlVeq4sf6lwZ9krsAEL9QPesFn4z0pUKu-MZIbnegqzQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
وصل شدن آسونه؛ خوب وصل موندن مهمه!
اگه از قطعی‌های پشت‌سرهم، سرعت پایین و عوض کردن مداوم VPN خسته شدی،
RapBaad VPN
رو امتحان کن.
🌍
سرورهای متنوع جهانی
🚀
اتصال سریع و پایدار
🔒
امنیت بالا
📡
پینگ پایین
💻
پشتیبانی 24/7
🔥
بسته‌ها از
۴ تا ۱۰۰ گیگ
💵
هر گیگ فقط زیر
۴,۰۰۰ تومان
و مهم‌تر از همه؟
لازم نیست به تعریف ما اعتماد کنی
😏
اول تست رایگان بگیر، کیفیتشو ببین، بعد خرید کن.
👇
ورود و دریافت تست از لینک زیر
🔺
@RAPBAADVPN_BOT - Test
🔺
@RAPBAADVPN_BOT - Test</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83941" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83939" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83938" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83937" target="_blank">📅 21:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8382999db1.mp4?token=MQvfK4cb2f_dn2pG9fED0aygx9RqlfhofB09ZD41oK2jRqskm_qSMxLZ5JQqHx4y89EPYFsT7VFvxyuNy5Bb8XeukNFSLeXhqZ-ii72wXYlcUL7Yk9qidh7X8gw5r0v-KVAiMfvis-PKhluVjq_7zB3G7Q14oHFGuL0tVICAN7xkZ9deZAKI-gRUucdAR5g9H6ETkU3MpV8aUAfLxiR0ZLcmFHZRDxsOOK1FGcgHHIKNrG1w2GtrdMkUox0fq2awxlWKEq9PiTWaqe2ymOCg2B33r2n9lDSgrWqi-qUBvMLEhTP9a4bQaVN-GJm3h9b6-oIwaXT7SofDx1a2_P0bdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8382999db1.mp4?token=MQvfK4cb2f_dn2pG9fED0aygx9RqlfhofB09ZD41oK2jRqskm_qSMxLZ5JQqHx4y89EPYFsT7VFvxyuNy5Bb8XeukNFSLeXhqZ-ii72wXYlcUL7Yk9qidh7X8gw5r0v-KVAiMfvis-PKhluVjq_7zB3G7Q14oHFGuL0tVICAN7xkZ9deZAKI-gRUucdAR5g9H6ETkU3MpV8aUAfLxiR0ZLcmFHZRDxsOOK1FGcgHHIKNrG1w2GtrdMkUox0fq2awxlWKEq9PiTWaqe2ymOCg2B33r2n9lDSgrWqi-qUBvMLEhTP9a4bQaVN-GJm3h9b6-oIwaXT7SofDx1a2_P0bdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو سرحال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83936" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان تروخدا شوخیاتون با باز شدن مدرسه رو تموم کنید، اینا انقد تعطیل بودن الان از خداشونه مدرسه باز بشه چند روز برن مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83935" target="_blank">📅 19:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سالی یه بار یه خبر میاد که یه زندانی حکمش اعدام بوده بعد از چند سال عفو خورده و آزاد شده، بعد از آزادی از ذوقش سکته کرده مرده، نمیدونم چرا این خبر هر سال داره تکرار میشه، بس.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83934" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کی فکرشو میکرد یه روزی نتانیاهو، پزشکیان، ترامپ و رضاپهلوی همزمان تو نیویورک باشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83933" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=iTXQDlhiCOrIIo9Q2hX8cxHQSkRNcKNimA9JWzP3SZw8QmwdHmORNdktEhb0Ds4e2ZP-rAqIszZpckY8Pc8lY6n0-UAnoID3FGrj8pg593Jo6bIXgpJweU19TowZDrAUU47wF--Q4MJ4ksVNZGdN--P8GssPty7NLJJaQTf0h_zks0T6UZtROMY2eM8SGgvv-JsbDnbcgAx7H54GQXe_GYjPUbLgyg-tty3jWDGm8nw7eVQZw6-6bDackw9mNWin2i296TFrHLkLKyYLawD6Lx5dVT79vjU9sDzWibjDpTueBfgfctFzHmUV2Mx2sHNRQdbyU1bQiSNCBeYHgJc6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=iTXQDlhiCOrIIo9Q2hX8cxHQSkRNcKNimA9JWzP3SZw8QmwdHmORNdktEhb0Ds4e2ZP-rAqIszZpckY8Pc8lY6n0-UAnoID3FGrj8pg593Jo6bIXgpJweU19TowZDrAUU47wF--Q4MJ4ksVNZGdN--P8GssPty7NLJJaQTf0h_zks0T6UZtROMY2eM8SGgvv-JsbDnbcgAx7H54GQXe_GYjPUbLgyg-tty3jWDGm8nw7eVQZw6-6bDackw9mNWin2i296TFrHLkLKyYLawD6Lx5dVT79vjU9sDzWibjDpTueBfgfctFzHmUV2Mx2sHNRQdbyU1bQiSNCBeYHgJc6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برا کی ویدیو میگیری مشتی فنای تو ماماناشون گوشی‌شون رو هفته پیش گرفتن ازشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83932" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83931" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83930">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=vhS9wIs907l5sBMi3EcieeTAotwOkbo9ziNEIqWHuEqfgKZxFaqH6UIyGan701uvhc1UEYntXwbHLnRPm82kOzmojK1vLBeNJsukcgBN5wvliBA71Pvjd5v9Q0Nv99WzIdI3YddjUuto6cZIPcej_bo8Y82QP35_Dub2a3TbSSjdI_4NqYzyyH1_Ryhf3hC5N6FNs6IHzb93Kfg-ipq66OsixzNGPIH58GINWBASIi-jz0gUUHwtiQ-_G5RTgO2C347jkWt9-l4zfG7A5tUoeCYgqUaHHKqiE2FPJ9QO4sJoiCrs1n52B0zulqqPD-msz1QY-7cHzpioUa9KGm1ZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb27cdfea1.mp4?token=vhS9wIs907l5sBMi3EcieeTAotwOkbo9ziNEIqWHuEqfgKZxFaqH6UIyGan701uvhc1UEYntXwbHLnRPm82kOzmojK1vLBeNJsukcgBN5wvliBA71Pvjd5v9Q0Nv99WzIdI3YddjUuto6cZIPcej_bo8Y82QP35_Dub2a3TbSSjdI_4NqYzyyH1_Ryhf3hC5N6FNs6IHzb93Kfg-ipq66OsixzNGPIH58GINWBASIi-jz0gUUHwtiQ-_G5RTgO2C347jkWt9-l4zfG7A5tUoeCYgqUaHHKqiE2FPJ9QO4sJoiCrs1n52B0zulqqPD-msz1QY-7cHzpioUa9KGm1ZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بری‌بت
✔️
دو شرط رایگان در روز
⭐️
🇪🇺
برای پیشبینی بسکتبال، تنیس و والیبال
⭐️
🥳
بر روی بازی‌های ورزش مورد علاقه خود به صورت زنده شرط بندی کنید.
🤩
۳۰٪ از میانگین هر پنج شرط خود را در قالب شرط رایگان دریافت کنید.
💱
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
⭐
مجهز به سیستم پی اس ووچر
👑
😀
ورود به سایت:
😀
g31
🅰
📎
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106
❤️
کانال تلگرام
😀
📎
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83930" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه سوالی که هرچند وقت یبار میاد تو ذهنم اینه که کوتینیو چطوری دلش اومد هفتمی و هشتمی رو بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83929" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bA-8NcgWRtTLCfnm_zt9SVxPZGU77BEIYed-wjf9sOut0Gevhjut0okvujO3MxYKNJ4J1hccl-eRynuH6YFTbZA55evjeqgbjHxInC9dAuNl-84Bq6LIB5yi0HaaLfUQqYrsBAncVcyVVHURY2NlsosKS0WKzCpkAAH-OTgMgCgJiMzbTV7Apih0ygM2WWimQK-xp7sDgJXlNWMg8gv8To3mmlvc5u4J6GRr8-5taakfMIhw5nmnX0ZFaVGpiGFVI2joCOLrCEWWuAal0XPwvHhbT2KND8TIOn_EK2Zf_w4GuhGTLWYpe3a-LqajeG8IJyMYo7GJgrk2EWvBAnkPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین خاطره ای که از جوونیت یادمه با حسین خاک تو ماشین بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83928" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83927" target="_blank">📅 15:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q400UZmERimQtra58ryNPwSBnShCBWIXTWxnfoTbl3rTvU1Cs20PEhtRGs8rOlNDj4_5wwWSFSLRQ75BIqtPybh6fK4hterz9_Uxct7uCbaGh7P7mjNQISt2D_4SKDltl0kmdgEUYD_Ok4h5rA4LXvZSjssXo2CPRVUr39AW-vw_jEzC-LuyuQx27oYI5TxdPatUO8cyrLsNSqYVeavzKgKKzwcp9e_tOFZGEEIDjBpG5LiH0XNDf1NnQITNlvtNa_nyJh1mRlW3JRhxbFigGnDHnd55KUhgUuD07CI2bZ6U_h4MwgOXXoXZiV80hSBFJHmi0jbqxLBGB41ONm8PKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83926" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شهریور ۱۳۵۹؛ روز آغاز تجاوز عراق به ایران
ساعت ۱۳:۳۰ روز ۳۱ شهریور ۱۳۵۹، عراق با حمله گسترده هوایی و زمینی، تجاوز به خاک ایران را آغاز کرد. ایرانیان در دفاع از سرزمین خود ایستادند تا ایران به دست ارتش متجاوز عراق نیفتد؛ جنگی که پس از نزدیک به هشت سال، با برقراری آتش‌بس در ۲۰ اوت ۱۹۸۸ / ۲۹ مرداد ۱۳۶۷ متوقف شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83925" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بکیرم
ماکه پول نداریم سفر داخلیشم با هواپیما بریم
🤣</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83924" target="_blank">📅 13:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">از فردا محاصره هوایی هم شروع میشه و هیچ هواپیمایی از ایران حق خروج از کشور و هیچ هواپیمایی حق ورود به ایران رو نداره
احتمالا بعد عملی شدن این بزودی محاصره زمینی هم شروع میشه و کلا زندانی میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83923" target="_blank">📅 13:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83921" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مسعود رفت نیویورک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83920" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=kD-_CAE6VK220bVUD4c9aH8e8wBVSQaldAP89Ri4xi1LeSg8BLhAOycONpYl4Wvd2H3JtGJvClyXSFIT9TltIUxgljSOeuSvuc5sonEs7_N2mz5LLGYHvC1v9_MfUPjVHHnfWaHbugEBZtFP4PBjpqTd8b8WDBcvvrtioWZG7U0nzaD6SKb4FydKX50WItjwayBOcEUWMNoyYm2voQKK_vTYw6SfJtV2kfshiZElkQVZK2--YqHjQOe6JG8pjBce0OkBZPeymrJNfMapjBEqCCd_DGOe9CZNoZuDBsFyIS_zx4d8uQpRaiaLvlaAzfENGltNjEtUtx-Li5u4QV-rKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=kD-_CAE6VK220bVUD4c9aH8e8wBVSQaldAP89Ri4xi1LeSg8BLhAOycONpYl4Wvd2H3JtGJvClyXSFIT9TltIUxgljSOeuSvuc5sonEs7_N2mz5LLGYHvC1v9_MfUPjVHHnfWaHbugEBZtFP4PBjpqTd8b8WDBcvvrtioWZG7U0nzaD6SKb4FydKX50WItjwayBOcEUWMNoyYm2voQKK_vTYw6SfJtV2kfshiZElkQVZK2--YqHjQOe6JG8pjBce0OkBZPeymrJNfMapjBEqCCd_DGOe9CZNoZuDBsFyIS_zx4d8uQpRaiaLvlaAzfENGltNjEtUtx-Li5u4QV-rKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی تو تا الان همچین استعدادی داشتی اون کصشرارو میخوندی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83919" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83918" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83917">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDBi7My4ZEbdBvW5AZhuyfoMapIBsr5RNRrh_IyoUucgr5oYKYE9juifvMAO425opzLMMxJ3ZA9zNxAH1fhLsy9qR4RdgQvFygRWztqa23eINc0LQMLpub-HDqmPDcQnelwdkhiYnsmaNtjbndDPCYMLBUd3IUGEV9gfU8uPWysVBZ-Z1Jv--WkG4-mwPmyUDFaMbMO3GaRcySAd3iNG_Pl2RhJvk61obGKxiWxz7s8PkrqXWQQcH64HSE0caB8RcRcBEfnIfks8lX-UCxHQN0VCkcE_8kXZqKYST2knXpqFFUBqDhoZSPtLR8Cf8nHxtqUJ3MsYY300JXbhKIJdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - رومانی
⏰
ساعت ۱۶:۳۰
🌎
📲
آلمان - لهستان
😀
ساعت ۱۹:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R31
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83917" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کوروش وانتونز گفت که می‌خواد یه سایت بزنه که توش رپرای مطرح رپفارسی (مثل سروش هیچکس) به صورت ناشناس رای بدن که کی برنده بیف بود تا امثال پوریا پوتک با بات خریدن و جو سازی نتونن خودشون رو برنده بیف جا بزنن.
همچنین در ویس دیگری در ادامه اعلام کرد که زنش او را به خاطر فحاشی‌ها و توهین‌های زشتش در بیف اخیرش با پوریا پوتک سرزنش کرده و به همین دلیل او اکنون یک انسان باادب است که از توهین‌های ناموسی و زشت خود به شدت پشیمان و به طور جِدّ در صدد تکرار نکردن آنهاست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83915" target="_blank">📅 01:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب برگردید بخیر گذشت
صرفا رادارا یه تهدید نشون دادن برا همین جنگنده ها پرواز کردن، بعد فهمیدن خبری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83913" target="_blank">📅 00:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">من به شخصه اروپا رو به خویشتن داری و کاهش تنش ها دعوت میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83911" target="_blank">📅 00:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83909" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83907" target="_blank">📅 00:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نخست وزیر عراق اعلام کرد همه گروه‌های مسلح عراق سه ماه فرصت دارن که خلع سلاح بشن و اسلحه هاشون رو به دولت تحویل بدن و اگه ندن باهاشون برخورد میشه و مجرم شناخته میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83904" target="_blank">📅 00:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PClR-Lm2bSFHDz_ob_hdRdJB8LnJVi2NEr-ctS6xJ48-Ub2JNH-iJ32NqcUzGQxqykqh_gKB8Sm5JLgro5-nMcqhdcG2RL4n3Sl5ccogyqeXqpJKMWy9oIN_ZnJSvPMdVBhGJEVBkYbJfA17YNrrm29nyIAolgQdvZo_-_QIdOTPMFYZIo5oMQsxpHhYicpJVvW2PcPbN_IDSF2cW0AuhFa2CmsDF7bRMfeFfzapS7B6CEYCg_Ejy3STvCNDY7fvWyPnNopZOOO7IY5tUDubtZgmCr5y6wo9H7qPzBhKhxTe8IUw64f3K0TeCB8fUvg9nMvnvQ1aOOT0z7qJdQpFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح حرفه ای بودن نیرو ها رو میتونید از کلت توی جا خشابی تشخیص بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83903" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUAdW7rnAzQxwrsMki1ZFS7CLJj-b5f6iZnZrd1AhpYuShjBnuGyYpCnkeDSKjciVaCA5aoE0Ug_oUNLSRh2reyUHBygaUAVYcIj5L2WD2Cy7gOPvPfE1QeF0Prr1y75EOWFaRFpCnyFLwtx7z5qc5xQLa07rxeExG8Y9GmSJUOEYob186hGfUodcQclLuOJVeDP_ZB0N-AbFIwpc3GgQvB_gry3fzTPCOfXcV4yigI_L325ljhggWBn4IUVLx_6WySr0BO_29wCuf46RA8dJwQeCsCqHM__uozP_aQF5OojabBy0xB360ktQivXaZeXgouHEugGtdbIGnjUuIW-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف نمیتونم به جیک پاول فحش بدم اونوقت بسنت چنلمونو تحریم میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83902" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=tJUaKyFPVcvkDwm2Yrhm4hVY5MXaVE170Lbpd2qaT9yUFmZZ_tccnCHwAcyB1U_BXJ0nh2FYY3GFci0ia5T_u_N2tD6FgwDf6qQs6rsnTVa4HLbEIo1tlaHpPLm1-g18hsy_N97-avbli2ChlNIySOCIrai7_1jRi78ZWYE3GjyzhYVKJ86TBSagqTzL9Wf3NFVHILZ1B4VEjawkbMrRdqo97FE1STlx9rkWgu2qKNPc335E2_i1TaqbFMB_G156qOKQxm9mL4u0S5nSiFrxDho5XE-ETApl80_f_wY1QiJQONyKplumSALaFtE33aD-ZcuI_zKuDtwxgNzsL6FA0YE2uBZKOx4JAyLbfa2_7nCrWHQh2B7wQtiqiBg9KBqv0VVmggASZuXcdBTTLmo9n2jsv3hTkNPDx0QldgJRgDY7zi3sBNpE1CwtX5O1_xy2GDg6OWhAP5fJjPtoxnzGWrqSxYG8RiApwX40zwUFwj7pSU2KwVVWrGCFmH-kJDnncBiX_A5jmRNl2BMDMlAV5eZynzKYDpyStLffJFMcn7pvBSpNLw5p5lD-AlfejmJtcl9yyCNHmeEb2osnLOcAL0noDALQMBUKz02-zB7RcLLnW5oblKlfG2D-8eqMzunap6hRtABczDI0jG0vhBY0MPMKIVB5swiF1ZV8yiR9jy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=tJUaKyFPVcvkDwm2Yrhm4hVY5MXaVE170Lbpd2qaT9yUFmZZ_tccnCHwAcyB1U_BXJ0nh2FYY3GFci0ia5T_u_N2tD6FgwDf6qQs6rsnTVa4HLbEIo1tlaHpPLm1-g18hsy_N97-avbli2ChlNIySOCIrai7_1jRi78ZWYE3GjyzhYVKJ86TBSagqTzL9Wf3NFVHILZ1B4VEjawkbMrRdqo97FE1STlx9rkWgu2qKNPc335E2_i1TaqbFMB_G156qOKQxm9mL4u0S5nSiFrxDho5XE-ETApl80_f_wY1QiJQONyKplumSALaFtE33aD-ZcuI_zKuDtwxgNzsL6FA0YE2uBZKOx4JAyLbfa2_7nCrWHQh2B7wQtiqiBg9KBqv0VVmggASZuXcdBTTLmo9n2jsv3hTkNPDx0QldgJRgDY7zi3sBNpE1CwtX5O1_xy2GDg6OWhAP5fJjPtoxnzGWrqSxYG8RiApwX40zwUFwj7pSU2KwVVWrGCFmH-kJDnncBiX_A5jmRNl2BMDMlAV5eZynzKYDpyStLffJFMcn7pvBSpNLw5p5lD-AlfejmJtcl9yyCNHmeEb2osnLOcAL0noDALQMBUKz02-zB7RcLLnW5oblKlfG2D-8eqMzunap6hRtABczDI0jG0vhBY0MPMKIVB5swiF1ZV8yiR9jy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار رو به جلو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83901" target="_blank">📅 22:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1RO3UgJiRQsDkm9py3Tiu1dGGpx3TkzLFzhMZHIjzyZ-CjimRORa7DYNS9ty4t9LvCcmAU2Pz7-lZgDbD7BPPZBMmjWifIPsCBr-zpPtnh86mIieJn3vrzX-dEGmn_xu6mQ63WKfAP_kJSZOnKVhR7Fh8y2nXqcJg07mfoFEnowuuOgwUIQmhJCr2KS5wBH4PdBlGEjYt6y8V2aJanF16rCgiz5t-OswNY-UZpCADpWhemmCbrzlTABwyX9IkZO_bKSOIJvJkhRkNdK1PWdpuUdGIhxzDm7LKo_bEwBfI65jDWkYpTXsDkmg3JU5Sbq0zp7LMevmA_x1YLGOHe1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی چیه این؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83900" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: کسایی که میگفتن "۱۲ سال دیگه بخاطر گرمایش جهانی میمیریم" الان میگن "هوش قراره مارو به کشتن بده"، در کل به این کصشرا گوش نکنید، هوش مصنوعی خیلی ام چیز خوبیه و قرار نیست بشریت رو به گا بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83899" target="_blank">📅 21:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83898" target="_blank">📅 19:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=CCojtvAVM7l1SCrWj0motOITDG0Pj1xufDKLOwXv-a-nYDIp8c00IiE22x5JPyoiDcCNPDFDsgOz8Grc91lzcQ6RDdU1vRhIsundA6IEjXZaRM4qle64cLcHIjlZz2lDNnceoeMkAydiaGVGpXmyDgZv9RJ1wAdMRb4QBOk1vqYcjQTUQcyl-ZKHV0oRSXF3rDfBlIxcqp_CB5TVZ7UiFiYf3sae8OTkH1LrxU1YsK2FC990IS60ZioN97lcxzfyeDeGvJhkLBRTg4a1LRMpUDchbA42mAG6oh5WAiIX-NxmVf6dxb0k-wObKob6pvl5ID9Mx1Ut4H2jRFkB-qQSwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=CCojtvAVM7l1SCrWj0motOITDG0Pj1xufDKLOwXv-a-nYDIp8c00IiE22x5JPyoiDcCNPDFDsgOz8Grc91lzcQ6RDdU1vRhIsundA6IEjXZaRM4qle64cLcHIjlZz2lDNnceoeMkAydiaGVGpXmyDgZv9RJ1wAdMRb4QBOk1vqYcjQTUQcyl-ZKHV0oRSXF3rDfBlIxcqp_CB5TVZ7UiFiYf3sae8OTkH1LrxU1YsK2FC990IS60ZioN97lcxzfyeDeGvJhkLBRTg4a1LRMpUDchbA42mAG6oh5WAiIX-NxmVf6dxb0k-wObKob6pvl5ID9Mx1Ut4H2jRFkB-qQSwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حس میکنم بعد قطع شدن ویدیو کامران و هومن به شاهین نجفی پیشنهاد تریسام دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83897" target="_blank">📅 19:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=UUHOtgxHn8-wMIDFpr60RLrEqJu3BuhiPc9NJQipAB2Ni_m1XK6OsAfZuNrAkq6ZwuJXt7JxoLEyQ_Sp93u7y7Zr61dudeFe1cvwvE8zXBveiWCjGhWDvwl14zWI-gXUvKAv_xYNRdN61kySDMMVIlPqX9lkKJ93L-411zn1JRnj9KhC3tcJWyopsA2WduQaqkvw8LhESp_yaq_1JjL3gpmudx4RIk_801i28fNhSPFcp9onJtwFerj0IVnpDIf7dQZgeBpRGEBVCt7LTR2cKGuRjeWKrE5eJGanhdfHx3H7IDRclA3ZFYSX-eC8BGuM-WRuKxq5kmOPMB1gFJhxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=UUHOtgxHn8-wMIDFpr60RLrEqJu3BuhiPc9NJQipAB2Ni_m1XK6OsAfZuNrAkq6ZwuJXt7JxoLEyQ_Sp93u7y7Zr61dudeFe1cvwvE8zXBveiWCjGhWDvwl14zWI-gXUvKAv_xYNRdN61kySDMMVIlPqX9lkKJ93L-411zn1JRnj9KhC3tcJWyopsA2WduQaqkvw8LhESp_yaq_1JjL3gpmudx4RIk_801i28fNhSPFcp9onJtwFerj0IVnpDIf7dQZgeBpRGEBVCt7LTR2cKGuRjeWKrE5eJGanhdfHx3H7IDRclA3ZFYSX-eC8BGuM-WRuKxq5kmOPMB1gFJhxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بین دخترای دبستانی:
میدونید من اسمم رئیس جمهوره؟!
دخترا: ببببلهههه
مسعود: میدونید پدرم کارمند بوده؟!
دخترا: ببببلهههه
مسعود: آفرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83896" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یکبار امتحان کافیست
👆
👾
🙂‍↔️</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83895" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHmU83AqeR6JBlP6p2Mp1kyNPVrdWkkDuq_TUZ0xom-SVMfjYEYUcCa9tzzNCajEeunC0rLFTTWyBdzubTSDlSjyoQlH0CkmHI58KJZWcNUDdA4n0C8zY3uVZPumVveLYr3SKR_rb3vI9re4FqX74egRmV5a0X8j_h5Bm91pRwyZbTCfDSkdcUi9aTSk_hpx-jQuyO7BARtxevoFeVrfvq1iXK6Mg7Pi3cbUybU9_mONtdlEvbnWEf8tk1RxDgkCOsJlBqTSRuYSAdgRKWC4sQEHXOYFuNtVeui1VSj7rMVkw0UaPGNlPtz1O2QI0BiK-0ilbgyoNuljzyEM0Gp9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g30
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83894" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZpUq-VxgkJPA4tXqQOqpStXpzNDo0R7ZQPDWa2-PCBmCAO6hKCobVK6chuz7PohTbB6RqDSf1EOJtx8faTlpyIalXMqZ4CZQYdq1X9w4NKjRaB18bZSexdwsTPjkvTon594COOinBDZOUuTkMaq_ePmRLZK12nmPtRAVjnm8qDPWBJWcCa3Y-tkjuGhuzhQno5xmJI1n8wyl1F_YCFw6r_QtkDCwQmxppMJEPS-px9BcSpLQtCSYP5NTBkESOn0xOhfsa3GEsF7kv0W5iEhj_JV4ILW4QGYM3JGYgV6--id7csHWP7f7VRFAtv5lGNZL0EzU6k29hi60QtyxJzpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83893" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6guNfwo94UjGSg5YP-yiHktLMmw-bYHu7K2Po-EfalXZRsNywOm2V6sIKlvRsM4DjHhyT3UfsnCkjzsXyPP060g4htfU5sWDgzkVCzvBQOCbsbA_Dnm1-drHO3f1jDcjJDFhrdj4PJNHpW0TSovyRWvKEMFoOfkSFHvfxmVs8bcKA5kDyrDTykHcLTftXpn-jrkEcvPgPTyhKAF9kyvItI6til8EgFiTg5Rez_cpkrvjWIXrg5cCOUED2axysK5Qr-FSuRvZNw2rPW1W-eEBPE3laX_-umRXLPqXxz0WPUIxuZx5nx7MN0xXkzGSQgYhHIEbxvbL8spikAsDeR2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=kuB7X-3kRIyv1bx5FmNQo2A2yblCTxjqj1JYAIoQO3RHG7BHx0iGhoxDWAg_ul2KsKyEXh8OpTBxOFs_3HQTriPuQG48vyiRW4j3TyeNv305Ic4OR_V1xiksIjIPeJKL440RCvRrBLJIuOtO4ApMAYt4vndz11H6wNxs65gzhuG_zcX_6csTO-YlaYeu3nBjgdgBg37G2IQkDzuyrW_l64sYp8443tPtwSg_rjHttzUYcP0a-PVjkn5XBjei2Zw28S3lEEkmX9d0X6h4pbbQqhFKKpDdTeIzXNbwWaQB1CkjWQR47mGWFPCY71RuO7Gdwb7X7TZ2qnc_gqgJTsOEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=kuB7X-3kRIyv1bx5FmNQo2A2yblCTxjqj1JYAIoQO3RHG7BHx0iGhoxDWAg_ul2KsKyEXh8OpTBxOFs_3HQTriPuQG48vyiRW4j3TyeNv305Ic4OR_V1xiksIjIPeJKL440RCvRrBLJIuOtO4ApMAYt4vndz11H6wNxs65gzhuG_zcX_6csTO-YlaYeu3nBjgdgBg37G2IQkDzuyrW_l64sYp8443tPtwSg_rjHttzUYcP0a-PVjkn5XBjei2Zw28S3lEEkmX9d0X6h4pbbQqhFKKpDdTeIzXNbwWaQB1CkjWQR47mGWFPCY71RuO7Gdwb7X7TZ2qnc_gqgJTsOEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشکان کاگان یه ویدیو از حضور ابوطالب و رپ کردنش تو استودیوی کاگان منتشر کرده که به شدت طبیعی به نظر می‌رسه ولی خود ابوطالب اصرار داره که هوش مصنوعیه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83891" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منابع داخلی میگن مجتبی خامنه‌ای اجازه دیدار پزشکیان با دونالد ترامپ رو صادر نکرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83890" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mle4W_fKNH7SWzdc-A56AESjeMvK5W5wwFZ6jAbBWpWgNj8pzOX9LeS04Z-OElK0dkF6rTy3tCasDzW1gwGFD30HxcvOHVt7CX8fRSEDoFo3FxtPO8yrE5sy45z5cNEmLdmitHgYI5SlIX27GpoXe1lRF4tDwaP_wpeU0YSILBNwTZ3PqKsNZUyJzn4EWERUHPO9rwl6dkLGGUbZ-MfrgKWhY61XrzOGw2YAH4zisd98PU8uzfff6bxMDJgN6v1ojaogrrxnFd6_I7Z9UUDfmndnvCYE9obioV_ecL9hhCrdw6NFWScx-yyEiUCXwiSLAuTq9DHGobY7zDPN9DKBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کپشن دیگه‌ای این زیر بنویسم میان منو می‌برن پس سلام
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83889" target="_blank">📅 17:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRZkA51VyEyonNE_mGEULK8S0raZyTBc1tVYHQmdhBWQpcWCJQKKgXpWLRyWgVi97hGOo7Bdm055sNzDxlTj_X0LnnZmzCas4AjD0zKoPbIKnxlIt9jhWzf2dL3ox04rWe1yUH8bbnf-K-9HV3LJuR1o9sX5-vtgOPA4VvXKO1aunCE2tDPQ-AWvO8hGhkEvmzsFQQAATMg7dt8cpWRe4LcyaDoVq_8tVA3lHnaHGXJMKDu6IizqQOltzQHImVMNZxwDvNxX8B8OEi7Xec3iWxsvUaqHWPMhVVOfpr7Q4VL0iMoSL-ZqjFDpnj5nwgaZtbwqJ0PtojKqfFQGho6r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بازیکن فلیک بود میرفت نیمکت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83888" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lorybo1sJiMOw3s15e9dF0CvAovEF1s_wBSvuzGnUCzcJUXwrJg4NR4l7NWEOTyVSKAbptkdVuoaJYRelFIB3Kg20V16QOrwFDPc30SwK3zqJ2UQXr32APnc3Wp9Lp66KS1n3SvPe5SDwn7oMpgoxRwppD_cJs9mIz4khvOwVyJvxiZVxu9HlYuEsv0M5Lh4MfW46SqA_L4ppcehfnHFgpisf7JHmWr7iq1wn-yxp50FgWaQElv1Phz6EQvPKK8MabYbB9zT-0YjZWuP-cjOv0BFZ8IGHOrjtsHhIJrbAr2VuQRTbQPJyPHaTC75tPTwVOUTp4GhSvxJjdFLFA0d9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83887" target="_blank">📅 16:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=AtY5w6NAK-FuOKzl0VsfXQWr4vC6yafFMa0uPS0QJB7cWBiYLGG8U-Jk2F5F6cz9JpGNsyTg2Gq22U-zFAnGwXk3a8FIf8vw0OPHgsx5BRbztMEakO1oA1y4HwbU74qMzM0Eeb2T0JEHPliMNJg4WomKIfO75MYZCYaDlm91Fcy100rPVTPuprEKa3XlDTofDnRNRFtaN6nyZm7t_0IYK00zw307FiLbRsPirda_b6kWEWG5Goe1DhQiR0c-50MIwPkN5-yL4qaqNCQU7Bd8z8NvcFQdW0sL4lgsXEKgtQnvulQlZkUv6CotmCvFgHKZn5CVOPltgvIAYIXZVvHj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=AtY5w6NAK-FuOKzl0VsfXQWr4vC6yafFMa0uPS0QJB7cWBiYLGG8U-Jk2F5F6cz9JpGNsyTg2Gq22U-zFAnGwXk3a8FIf8vw0OPHgsx5BRbztMEakO1oA1y4HwbU74qMzM0Eeb2T0JEHPliMNJg4WomKIfO75MYZCYaDlm91Fcy100rPVTPuprEKa3XlDTofDnRNRFtaN6nyZm7t_0IYK00zw307FiLbRsPirda_b6kWEWG5Goe1DhQiR0c-50MIwPkN5-yL4qaqNCQU7Bd8z8NvcFQdW0sL4lgsXEKgtQnvulQlZkUv6CotmCvFgHKZn5CVOPltgvIAYIXZVvHj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی سطح طنز مرجع تقلید هامون»»»»»»»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83886" target="_blank">📅 15:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آقا کامران یک نسل چهار</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83885" target="_blank">📅 15:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آقا شما بد جلویید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83884" target="_blank">📅 15:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzX-dILP_hihfO9bazm-pekfLI_jZsl9gIRr6ZSmwYWXlYec2MlI1NhXwTsCyvhvsRYPi_45AU0qnAjAfRqXXuOnE9d1H2X6wvzb5xayDMANXFR9UdtuBlry_8O6NbFcUIsx3Z7DjtcrM_JPXoMwazUsRRuDzvHklhczk64ds14cXNscDVyfMI1akDzyDfQQs_kODnZvHYHOK_3gcCpJQ37aavBv2vysREeVXWd4STO_wQAQYNmOfmbtreCi3rKS-9O4xPzUMv0Ftdb1JboHEErA0LXptudI1_MwMVeaPU6HEYPqwPnNqKmPL7jwIez2X6bYEA2V4Yuq2RHkXecDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا شما بد جلویید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83883" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یا یه رفیق دیگش سرطان افتاده بود تو خیابونا تهران میگفت چرسی پیدات کنم زنتو میگام</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83882" target="_blank">📅 14:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83881" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83880" target="_blank">📅 14:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیرانوند گفته چون تتو دارم مشکل اعصاب روان دارم، پس معافم کنید از سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83879" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خیلی وقت پیش ی پیشگو گفته بود ی یوفو میاد و نیمار رو از زمین بازی میبره، احتمالا همونان فقط تو ترافیک گیر کرده بودن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83878" target="_blank">📅 13:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6IofiYQu7YbYXKSQ9pXZUEfCpuMC-NLX7MIqg1U7C8vS22WRhVBC7ibg4LtiFgDpqw0lQhOra-K4vNkl8o2Z7SNinjHQiQWsx25ogc_bEe__s5ZuyMtPcvQZwFLpFlPQ1ObKkfvjXJ7IPyvBiDLpwCJLeO5PnRTDD5vh1xgGDqhDZ2qbEIGPdJ_Z80EDEnkZF1xal3ALBYkZUd3VB1L9ls4MdcOXVOQIDSFW7WyCPu5B0weGuZubBmcpv_irXWxzd2LDXs8q-hKkvztyYfG0rsGJVZUrG3kobSH9MQOfKwl7AueHmRgy8jxDZcGewZxkqHHvJ1tqQJL47RFfg3vnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادرا یوفو رو هم گردن گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83877" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=dVsOixgk95OvXMPZN2s6xJmBP4zpDKdwEArbwOibT1hWMGcuN6Rf9PKffJCWA6AXTlpSqCaZRkJrBGAw1h724L5HWpAIR-lzL_FGqmANt88DFbdxkEKBAJwAjHN_3CXG5gMsdLc5ftHm39uUWjfUj13SLsc5lc16CatfmCGUeV5a3fo3fT745VCykiNlPAOCz7UY4QBHsujnve6fPGcdlX8sUHLY6Wgi4zQuGkESqv3iKPbkJAwIGzxy7j9u273E3EkoI0vO8pOPp4Ctub5DDbwaFWplLMS7EZbJxh9wIyEv97MC7rwZ_ydR_6Qa5Y34W3KE5AfJNedIbo0bA_AVig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=dVsOixgk95OvXMPZN2s6xJmBP4zpDKdwEArbwOibT1hWMGcuN6Rf9PKffJCWA6AXTlpSqCaZRkJrBGAw1h724L5HWpAIR-lzL_FGqmANt88DFbdxkEKBAJwAjHN_3CXG5gMsdLc5ftHm39uUWjfUj13SLsc5lc16CatfmCGUeV5a3fo3fT745VCykiNlPAOCz7UY4QBHsujnve6fPGcdlX8sUHLY6Wgi4zQuGkESqv3iKPbkJAwIGzxy7j9u273E3EkoI0vO8pOPp4Ctub5DDbwaFWplLMS7EZbJxh9wIyEv97MC7rwZ_ydR_6Qa5Y34W3KE5AfJNedIbo0bA_AVig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83876" target="_blank">📅 12:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4B7NqW5puGnnWxz9DTn-1rewGAemGumFR9tV9D7AgzwqT7eb7RXs_QmDnRErVdV8_u67HPbUb9LdhDoOhOl4ZoSDE8OEnmi7tXElA65uWK5v0IF3wPHsTZGcKDyMRFLMJtWVrK7WxpxurXvEJMbdFepakQwJq4LxKaLveWwA9yEAXlzuCU4TE0NipH7NflQr17RcP1ABiFSW4uLfvs7mgv6RmjttGhrdEGrzhgLXoi2v8PbscgJFmlTIgQuVCDZCF5_5yscn2yvbuFp8A_GJz-gaL910VUWBEApTC-DRYSqpj837KBCYe1Zpq86T3M2deBFpI-mXu5JqbKi66eIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجوری حساب نیست اگه میخوای علاقتو بهش نشون بدی یه کار دیگه ازش لیک کن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83875" target="_blank">📅 11:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83874">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=iRBdTCKJ1ix1gsJKIYjHZn-sRjRLgZU-ajHh_6S5D8-7Gaypqca66tCzQbgmIRPbVhZ2P5U-IwwmbmARoz9AvDBrY0P-Uh19L8xbGjFE_bDUrIXlmkXkXmq0NB99nUC2su6pBcanUTl8IOchgbAmCoLNIgOxgraR8D8f8P0mFHhajjbxJbSPCkZf1UN-8_w2jCysjFm1TGXiP8KVrrtxxgsG9oFNqDxBpDexS0iDKP2VpEVCHIytEQxsfxoijsHpxir4hfpAqX2TqmjUHIiXddk67XIDcqEM7Wp5LHJlPwwVh9ohVOYYzduwgCN074JD2kqjDb5M2wJ9bZUFwBCYAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=iRBdTCKJ1ix1gsJKIYjHZn-sRjRLgZU-ajHh_6S5D8-7Gaypqca66tCzQbgmIRPbVhZ2P5U-IwwmbmARoz9AvDBrY0P-Uh19L8xbGjFE_bDUrIXlmkXkXmq0NB99nUC2su6pBcanUTl8IOchgbAmCoLNIgOxgraR8D8f8P0mFHhajjbxJbSPCkZf1UN-8_w2jCysjFm1TGXiP8KVrrtxxgsG9oFNqDxBpDexS0iDKP2VpEVCHIytEQxsfxoijsHpxir4hfpAqX2TqmjUHIiXddk67XIDcqEM7Wp5LHJlPwwVh9ohVOYYzduwgCN074JD2kqjDb5M2wJ9bZUFwBCYAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83874" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83873" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83872">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iklAbSAQKlcMa7hYQlRds8YB2cxFeE5snmaMwPbBb95wKRfRvrn2GDBoTDhoevxNhRv8VWh_qNvy__W3qLi8cjUnmuayG0oCUa6ffnoLvXpN1itQPOhf8dJrclZXqywAROEMG5vqiB6IRA4V0A3PMSJUCmZUEwcR7mf_-eP2JQ_g4BYEHhAwun_1EVhpTPupR0UqDrPWiAwbM0gDtgU6fgYblqeSFXFgozFILQP5UN1OfPZ6RnbYw0VqSbUawzP9ECtvFnMaNrKsF10ISJOxTOdgzj3by5RXjKmABOKVB2fiKfBXPjlQ51DTzn1LxQsGYt-99pvFuelnAxTubgYjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - جمهوری چک
⏰
ساعت ۱۷:۳۰
🌎
📲
اسلوونی - صربستان
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R30
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83872" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf80PpWD_78x5R-JZ_kTfjAdYsES5NOpUhcdiWOUtFRMUSJXq2bN-RLu80H9qOzA9ZCJEIh77sKtFT-jq7yCDwoR82_JPemTEpX30uShfl0W61pRDovenqc2nghQOqv27BjelG8AtiHdNYc3q6NFQJl88B18qA529qFxhQoV8PJEPY4AcIvuJXfYghBMf1DYq914CzwvCLN5Y6QS23_jhrOAPytTequ7xQEHLYxqBnGjx2tTt4C3QgFI_6HqB6vLdo6k-67WVIx692A2AebnMF6RLQ1HQwqzrCDY0dQkQaP5sZh_yGBG-FNudfLPrtWKWMZArw19G9aqiRrYbfgnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممم عجب شب عجیبیه، دیده شده در آسمان تبریز.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/83871" target="_blank">📅 02:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTq_oUDXlXRE7NdhFJgqdzBU5xQK5i3ukbH_liOfHJJm1D9lRxPy7BBB0_dCsMLwbXGO1JTogWHnwUZRFAQZFK7h5zF8mwQAgaR0ibqjMJ-rnsu4ycSBR47YLxfIevCu8gPxBDiqariEpSTxggPn6CxLGd8jZiCfECv4fwPItfH-l1nNOvoLrgInWgvWBwlB8IPe3Ous3VbjO59rfloDjNX1xobtv9JxF8zJijXptbEzWvAfIlL6owGkEZVb1je_VYEnvDiSgFGaj_1hTZ0xYYbxbZt6PwwkVSYiTha1Gb7-TBMccnFMHnQz-A7_JMsDCcnkMrxc4KhtThUQJtARFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/83870" target="_blank">📅 02:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83869" target="_blank">📅 01:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/83867" target="_blank">📅 01:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/83866" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاید یادتون نیاد ولی خیلی سال پیش ی بنده خدایی با فوتوشاپ ی ویدیو درست کرده بود که از آسمون بادمجون میبارید و تا مدت ها مردم فکر میکردن واقعا تهران بارون بادمجون اومده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/83865" target="_blank">📅 01:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83864" target="_blank">📅 01:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=vehokxLwJh0zLw0zVzforNwTsXdI37oUEqyPjMXHTwx56Gh8HiJq3imMOhJjTKAaNlk_KwGeCv3r7qS9uKnqi7t_dETKdgIobwgprAzTxsxzdxpfkFxtY95bWN5yA0n0glPyj-orutLus863-C04QERj3z1rfWsHU1emvdXG5f0xsN7HS32z1Yqaeo5FNTzDU4C8lF4V4dcs2zV4t7espjXb6mDd8MqE07deT6Da7-zZN9VyADnqnN--vzs53nfHG-m9R4KPWcECxOzBclbXWjv_bjDnSKKVYlK5VmsOenIPHlp9qv6CwB0e47i6WIIjss-YDPUxsYl2bdNvQCEAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=vehokxLwJh0zLw0zVzforNwTsXdI37oUEqyPjMXHTwx56Gh8HiJq3imMOhJjTKAaNlk_KwGeCv3r7qS9uKnqi7t_dETKdgIobwgprAzTxsxzdxpfkFxtY95bWN5yA0n0glPyj-orutLus863-C04QERj3z1rfWsHU1emvdXG5f0xsN7HS32z1Yqaeo5FNTzDU4C8lF4V4dcs2zV4t7espjXb6mDd8MqE07deT6Da7-zZN9VyADnqnN--vzs53nfHG-m9R4KPWcECxOzBclbXWjv_bjDnSKKVYlK5VmsOenIPHlp9qv6CwB0e47i6WIIjss-YDPUxsYl2bdNvQCEAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد  @FuunHipHop | FaRib‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/funhiphop/83863" target="_blank">📅 01:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد
@FuunHipHop
| FaRib‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83862" target="_blank">📅 01:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شبیری زنجانی مرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83861" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPjOZhKZfvGBsHDGpcmNNQF2VT3E7xcK4At_joZxEOt9r3BYlriKE7u5X7U-IaixE1lQedS4RZC6du9VnmFc1p289h0rkJYU-zvODroddFVy3TTNA_L0l1mVY_K43we5s2he8wCwPvGsHE7C5FHc0wVR7iggYisvlMCOQ05Y4KRt16FkH04JMF_v32_wQ3d1R6kkgd2N5QFjxDVWmruuImGM-3eNP5e-HgVM2KeJAejX8QncHD5T74pIz9OsCptA9OlzrXeL94MbosFbOdPtQC4nYKe9YZ41RxE9bqaZKnYAOfDX2CWzzYn5Z3rYB4UWEVDByqSG6Dt5zS2E7vZWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبیری زنجانی مرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/83860" target="_blank">📅 01:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfsQ4y-yQgZJKgC0UAwfpIe0_lNyI4YPJzNN9GzNWc5E4TC-1yTxMt62yBWWvIJ3BTrE08jk5JnhoMUgGM9LYWua4tOpdTaOtUZUCpOMjPDESQceLBhrzsk1DcDaK-OTmhpJtV2RNS3ZhD4iLUURLjLXkVwsBz4VJX6C6wtVH7-YZV4OqecfRm8p6-zvu6KPe4S50a4902q7fgHyC_5JtVlDi3txX5LnxtUVxL1NQR2oSy0TLr9GE7R_hlvsPw_QOyZxU0yZSsg0kW-7NrZ5jCxp3bmKNRhz3XX1r4EkkoiUW8qY0tr3jcJVk_2XsQku-rCkeC2gOm7ozXeHWV9lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zw_AFvLS9h7pNuQSuScRXJ8SbxL-lAImmGBVBkbVzcw3Cd0LaGIv2ygqQA8nRZ92rmNMruRSGvfy-JFl3WLEr-Kof-Vb-Wgqvb_VetiebQrCRld9-XZa4tOGGS8BlkK7FZ0Txi-JukUD_82HjGG1Foem5fDx7rohU-_rIzzHQAkTON8XqY3Yn0t7cFE0DTHLnhCeJoK-Be3bVKo7VPQmi87BaPf0NkUb4siQb-tFY2IrGeVl_6MgSmwum4qtgvpM7U8mGdifvstU9R9SsEeTTqWcdpP2npGSB4J4y5Ef_-YQgB0UMP6sIQEisXX2lZQU4lpRl82w8qEvf8jtAj0reA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چقدر زود پروژه حکومت لو رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83858" target="_blank">📅 00:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw_sRscSOgc9AfhkZULPYQwA1DO1yovFLvgfGY_NpURlXX_gFWtDVRKs9hwBnJb3RZltdGcmYOVr3r9zaB8FohVju8TKcgQRn2zpD-8XAsfXnKMwk1b1XEn6CJnmxMJNfJz4r7spGSD_Hy6QXtPPk3eUcXusXcuTz77-3zVDVpAIyqjun5eOApuPVbhVK6yhZZ8o5GyuFIHaiiuFQ15tsh4ZxvYNzsl83zZfT1uwMYZwtPLBfwif0tha2CX7fXENErFdEjOvZt3XTdQL2-DbB5JizOP3Kufj2YzjsbFwbC34awEt-KOVD84jcgoEjFj0zIZKHGuX7FwQaJpYScSuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان امیر تتلو را آزاد کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83857" target="_blank">📅 00:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">همون منبع
کیری
به طرز چشمگیری موثقم گفته که صدا پدافند میاد و جنگنده های جمهوری اسلامی دارن بر فراز تهران گشت میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83856" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">طبق منبعی
کیری
به طرز چشمگیری موثق بزودی جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/83855" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4rMFEeYfCpfbiCV-1oGhulc6-jtAFmGtXp5k0LM3H2UVPN-FP8EsPdEWHdU5mQpT2vZve3l0uyoJMAjm-TnQTRAEEvLJAHwYzeYIBkmV_R5gZirFYmDyf0BWomMtIOOb6p0VlNbIVYR7gUC0ArXybv01MES8zKZZkVEyrVheZqeozjbHPOi4WrCbIyfz9ssfZQO_kknr7yYKjwLp2zkkMyGmOFxMihN_UgnXy_5IprhJAKcLmbvGzzrwtFSwIhITB2HNFOIL4BWhiheUlaUfRHVT7Yjw8aYeDsidwDpU7mby145qc4jmg2y5PuhCCT78baDpDCUi_GGb7_QYoDRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که براشون سوال شده امیرمحمد بزرگ شه چه شکلی میشه داداششو ببینن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/funhiphop/83854" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به امباپه اعتماد کنید، الان میزنه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83853" target="_blank">📅 19:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بمب خندست این مورینیو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83852" target="_blank">📅 19:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این کورتوا چرا نمیمیره</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/83850" target="_blank">📅 19:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رئال باز پیشرفت کرده پارسال همین موقعا ۵ تا خوردن از اتلتیکو، ولی امسال فقط ۲ تا خوردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/83849" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یاسر آسانی > وینیسیوس
عارف اغاسی > هویسن</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/83848" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سر رئالو بریدن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83846" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بابا دربیارید شماره 4 رئالو از تن این بچه کونی
حداقل خطا میکنی مردونه خطا کن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83845" target="_blank">📅 19:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوتا کارت قرمز مستقیم داور تا الان نداد به بازیکنا اتلتیکو</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/83844" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U94_Og-xTFMKm6semAwYUyb-x9_pCQmauOh9aB8iE0p56rqr6yEv4SPBYjGGpKQKiz1dYIskg5sp5b-l2Im0L25HQoj_adWUhoZ6CsWA361gLGyQXk-VNNzmkzXXwifbnEaANwOXQkakKxPB9sxMqLRdDr_lBC_0rNq52EAY41dLHORHC9Z69NqFdFih9y3PqZbz4AB9QocEx1sRbaYqWdH-HSgk-IN691HyflGh-CvxYf3YSJNNr4rbODaFUnbLFHUdSt0SBC5A42irKgZe76tuWR4kIZCITjyJDbzEVwC0Lb32EDQDfLh3yqaMc4u6Fp7GYzPtUvANOvok1NJIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید با دایرکت دادن دونیتش کنید میخواد پول دکیو جور کنه پس بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83843" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvZBEVxtoYaeZgNe0Bzvd_sk0ASDhja2uyfbC8lR1oJ8h8_85nF-fczwhT6SxmheaAjcYJwDsjE74UkiI3eU7bYOCBiBci6C4NtUV1KZlwH6Hl_i3GK8LdGt0XLth3Zdop-7LDB0FtE7Qu5mL_20FsG9eUGQ3W1pRgntkH-P4w16qkW6DjwAvEQmV8SPQmnOSb4mWzqa1tgb8SJOeXclRdkKavU6ftHst9r0JIXCKiW9Rh9cTZQxP0UsuOc4982wYhF80PTddASO8Pu7yd-wFLo6gg3UAH81XGreQfOncz46-0nMMZ44EIlHwK6FFiOpKCMxVKZL25wTaCutliWwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت دربی مادرید الماس مادرید رو ببینیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83842" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a15289855.mp4?token=dBWcZ1Qzo2Yzg2RVsuPDHjOdm32UPN90vyfIFIY8TEB3n2S12iJac1AAONnpFlYqdkRXo0QS_7_Ezm1Hhxqrl2vcyaEG0jPgmT2JOVkH4u5tM3z-sFIESSWnnvN9Ol23SrBLzgv5K9lJJWArXdzVqROu4eenrzCdAfZUe9xg_ftPHkzV-bBok6hGUAKhMvDyZ0xgNYQfYawdbHoksYxghAU95ucQobFUNnRBwT_YweJG38S1_0s3rXNicvkwcXm4W8-ZNY4WT56MJMtL0F0qpYLP4jzb4fbxYWlsKaQGy2-FGdpVp8zadsHWSnqvZKGqPIo6o6BsLeq-XK6NgopdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a15289855.mp4?token=dBWcZ1Qzo2Yzg2RVsuPDHjOdm32UPN90vyfIFIY8TEB3n2S12iJac1AAONnpFlYqdkRXo0QS_7_Ezm1Hhxqrl2vcyaEG0jPgmT2JOVkH4u5tM3z-sFIESSWnnvN9Ol23SrBLzgv5K9lJJWArXdzVqROu4eenrzCdAfZUe9xg_ftPHkzV-bBok6hGUAKhMvDyZ0xgNYQfYawdbHoksYxghAU95ucQobFUNnRBwT_YweJG38S1_0s3rXNicvkwcXm4W8-ZNY4WT56MJMtL0F0qpYLP4jzb4fbxYWlsKaQGy2-FGdpVp8zadsHWSnqvZKGqPIo6o6BsLeq-XK6NgopdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83837" target="_blank">📅 16:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جنگ کنسله
صداسیما اعلام کرده حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83836" target="_blank">📅 16:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83835" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=CbDJJ6AVF8agzzB6tQ3c-TjqDhzLyJgujgObjVfI7iX2eZXzQjW2a7kEjwnbV2Y-Z6eyG3hJ5aC6Ohw-rXjy-UvW_gCDciK76-ftqZzM202zN09WCYWlSsgLtvblT9I8kMikfnrFn6XK3QCVObtwkGHUFnDF5kyFe6_9XfGM5nJ1Cuh-YYFV0aiSFxghtF_aTXQap8L82wI1y4rU8qZcr4PXymkaDCNZi4fLFFDuA_6sZ_Te_zoj_DU6siBhcHECS3mLmFixddlbiN_3RIxGy3AFrPrklEiaLged1p_gP3d-KvpTqx1YyFLkyPs0JtC9lx_KKpIA3shNnMJHgKaltA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=CbDJJ6AVF8agzzB6tQ3c-TjqDhzLyJgujgObjVfI7iX2eZXzQjW2a7kEjwnbV2Y-Z6eyG3hJ5aC6Ohw-rXjy-UvW_gCDciK76-ftqZzM202zN09WCYWlSsgLtvblT9I8kMikfnrFn6XK3QCVObtwkGHUFnDF5kyFe6_9XfGM5nJ1Cuh-YYFV0aiSFxghtF_aTXQap8L82wI1y4rU8qZcr4PXymkaDCNZi4fLFFDuA_6sZ_Te_zoj_DU6siBhcHECS3mLmFixddlbiN_3RIxGy3AFrPrklEiaLged1p_gP3d-KvpTqx1YyFLkyPs0JtC9lx_KKpIA3shNnMJHgKaltA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83834" target="_blank">📅 15:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امشب یا یمن کونش پارس یا ما، همه شواهد نشون از عملیات آمریکا تو خاورمیانه میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83833" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قرارگاه خاتم: آمریکا میخواد با چراغ سبز کشورهای حاشیه خلیج فارس بهمون حمله کنه، بزنید همرو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83832" target="_blank">📅 14:39 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
