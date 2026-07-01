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
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-665337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6f832d65.mp4?token=k0i2ElTOtq59mc4Rzwx8OHdm3BCBWoAaKw1xByLAEnyLOzGJtf9w53TSEVwXern_4_HIXQ0iZ2shFs7_X26-3OvPYuzm7Rq9-5gN0KSTGoPcbItd1mP0JTtIj71I99gqA23MX1ZIzsZmy_dM-JlYWXIVYNqw-v3zHSZrEpoQTGDOdjnHmkhBUMY1eN_MxUe2IFhRzzlGtn6d9vWRiNKB_OnjMTbCxJEVUAsP2ehN3w_IWVdtv6HR0crgDxcyz8rOOs5fLwRENbwzG0gzZlD4_S3QNWc4lK9p1YI-pihxZvK12YHQCiR3TI5bnHqBSCcM8b8BNGMeM_5-rXEv6QWkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6f832d65.mp4?token=k0i2ElTOtq59mc4Rzwx8OHdm3BCBWoAaKw1xByLAEnyLOzGJtf9w53TSEVwXern_4_HIXQ0iZ2shFs7_X26-3OvPYuzm7Rq9-5gN0KSTGoPcbItd1mP0JTtIj71I99gqA23MX1ZIzsZmy_dM-JlYWXIVYNqw-v3zHSZrEpoQTGDOdjnHmkhBUMY1eN_MxUe2IFhRzzlGtn6d9vWRiNKB_OnjMTbCxJEVUAsP2ehN3w_IWVdtv6HR0crgDxcyz8rOOs5fLwRENbwzG0gzZlD4_S3QNWc4lK9p1YI-pihxZvK12YHQCiR3TI5bnHqBSCcM8b8BNGMeM_5-rXEv6QWkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات الکساندریا کورتز، نماینده کنگره آمریکا به لایحه توقف ارسال تسلیحات دفاعی و تهاجمی به اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/akhbarefori/665337" target="_blank">📅 17:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-BnkgQksqVo5yTchzgXlcXu0UYu1jzh1AbGjDuC4Tsw_J1ZtDJr8RGx4Y_1oIC4xAvoEItCXfV6cieJMJ8EoWJOJ2zdTOueuAVyRJ4Zv2MNr2p-0rMFyeMDMoQUGhlvwLwsGplqLUxFFQWDz9lSspUeAoGIRqJrmwiji_QeY0jSYxtHpVnk23m067jyYD8QZxPHXBhZoVXeK5tHkmHRIuv3Yej6AE8c5B4mQzOU4N0_TSy3TYukOPIM_4l6y4YM83y_5MreDFqUjomYLwjr1yZv5bK1eUyCw-tqjAmdsPTPg7WEuzfB02RB8Ah04i-ukYzEENVBW_ol5cwl1O5s9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدامات لازم برای نجات اقتصاد ایران از نگاه رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/665336" target="_blank">📅 17:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کاخ سفید: گفت‌وگوها درباره توافق با ایران ادامه دارد.
🔹
وزیر جهاد کشاورزی: در صورت رعایت شروط ایران، از خرید کالاهای اساسی از آمریکا استقبال می‌کنیم.
🔹
طبق اعلام باشگاه پرسپولیس، همکاری با اوسمار ویرا سرمربی برزیلی به پایان رسید.
🔹
مدودف در آیین تشییع رهبر شهید انقلاب شرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/665335" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAukRGzH84hgBWN_YQ4pix28A0-grRT12Hi5TDis-MC3eunkJLRimCApidAhYXuRqNCD0ZHsk_PG-utvid562unArkAX_HY059XyE3h1-CT1lk2r2RV5Ivix-efRf1D6WTxtpUmcN6FZtdbmp7711YaJkosrPYkI9znXjEjwYiijo6kzEe0Mg-7Sg0fOgJaXyiBRp2YaWoVAVTw1MFkhWygsgUpyts_fjWoIUf4ZnEHKGo6UXmEqgZZOTfZS9DNxrXZX6BezyqUC6N-0HyB34oyzgGkPhlvZwXINZnxerRz-ELRA6aLzH0R0KiRAs_bx7aoJ6hV3Bgl_9fJMZhsPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این چند اتفاق سرنوشت ایران و منطقه را مشخص می کند/ شبه کودتا در عراق مقدمه «سونامی» است؟
🔹
اگرچه ایران در حال حاضر، درگیر مساله جنگ با آمریکا و آتش بس در لبنان است اما این تمام ماجرا نیست. اتفاقاتی به مراتب کم سر و صداتر اما مهم تر در حال رخ دادن است. شاید یکی از مهم ترین این وقایع، دستگیری برخی نمایندگان عراق باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3227179</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/akhbarefori/665334" target="_blank">📅 17:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA0VvW1ukfgBGeYULbCHbuinfrkaK5pIJC0qmk6n-qD1_BotyVuDBZqu5pNH5vmXrx-U3liNdSh9BRkwWsUoWSxyT9BGxrvuAnEErmgiNN-gQcu48cfIgQyNzcpTvRIIJY0aaFHLw2nYvvEqQZuNrnb6edyCgjjXQl9XpH5F9ameuWUh1Au7XJQS28x1pnUf0xGGXI2oM-kH81mFbyaoF3M6jTb0A83MSX4tmBpREnhh0r9roCGohaMreRB4j3DGsr4WHBujPsBoUO9b8rJKjwkmRjou9Fqa3AucfvyUdQ4hAP5MdlEkxieS-F0UJA_BNq_NkmE3NUU9oMDY7zQynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه رنگ‌ها در قلب شیراز؛ سرای مشیر چشم‌ها را خیره می‌کند
😍
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/665333" target="_blank">📅 17:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
متفکر آزاد، عضو هیأت رئیسه مجلس: حتی اگر آمریکا گندم را به ما ارزان‌تر هم بفروشد، نباید از این کشور خرید کنیم/ نباید پول به جیب قاتلان رهبر شهید انقلاب بریزیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/665332" target="_blank">📅 17:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7d97719e.mp4?token=vgHWLkQTV-9PKqVj1KMe5QnCgapSfuColUOCrBvNfndIFfZIA2fwERlJtNpbPkLA_7EUEWrVYsf7fvi2pLWMfE8NiI_OXSEvJhUk-DQbQ-XvamNIpaXfvoOdD35O2p-_kCGHMW_bjWxYgPnnPuBq2hTYxLdQJ9ZNippws1XifwS79UbrTKQm3dUh8gblAYA7kxrYF686DptIZboX1mpV4TfhP0qdpsUCyXAdQHZkUJSJqibhyWXePYeN6YKb507qx9_3dKJ97tY7ExGaBTuPSyI8QIEVPr1mfhjPpkT3r17J-XPxdN-9SDgqCKp_2focowfw1Lb9efR3QN7MCHBlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7d97719e.mp4?token=vgHWLkQTV-9PKqVj1KMe5QnCgapSfuColUOCrBvNfndIFfZIA2fwERlJtNpbPkLA_7EUEWrVYsf7fvi2pLWMfE8NiI_OXSEvJhUk-DQbQ-XvamNIpaXfvoOdD35O2p-_kCGHMW_bjWxYgPnnPuBq2hTYxLdQJ9ZNippws1XifwS79UbrTKQm3dUh8gblAYA7kxrYF686DptIZboX1mpV4TfhP0qdpsUCyXAdQHZkUJSJqibhyWXePYeN6YKb507qx9_3dKJ97tY7ExGaBTuPSyI8QIEVPr1mfhjPpkT3r17J-XPxdN-9SDgqCKp_2focowfw1Lb9efR3QN7MCHBlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر مستقیم واردات کالا یا دور زدن‌های پرهزینه؟!
مجید شاکری، کارشناس اقتصادی:
🔹
مابین وضعیتی که شما از یک مسیر پرفساد و پر اشکال و با سه مرحله دور زدن از کانال آمریکا خرید بکنید و مسیری که مستقیم از آمریکا خرید بکنید، حتماً دومی بهتره و حرف‌های همتی به لحاظ فنی درست است.
🔹
همتی قبل از رفتن به ژنو، به روسیه سفر کرد و در عمل ابتدا در روسیه ترتیبات جدیدی در حوزه تنوع مبادی واردات کالای اساسی ایجاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/665331" target="_blank">📅 17:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
روایت بابک خرمدین؛ مقاومت، خیانت و مرگ
🔹
بابک خرمدین (حدود ۷۹۸–۸۳۸ میلادی) رهبر جنبش خرمدینان در آذربایجان بود که بیش از ۲۰ سال علیه خلافت عباسی جنگید. او از دژ «بذ» مقاومت را هدایت کرد و سرانجام پس از خیانت دستگیر و در سال ۸۳۸ میلادی اعدام شد. منابع تاریخی درباره جزئیات زندگی او اختلاف‌نظر دارند، اما نقش او در تاریخ ایران بسیار شناخته‌شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/665330" target="_blank">📅 17:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت کار: تعطیلات هفته آینده شامل کارگران بخش خصوصی هم می‌شود.
🔹
موزه‌ها و اماکن تاریخی ۱۵ تیر تعطیل است.
🔹
رویترز: کویت پدافند هوایی خود را با کمک نروژ تقویت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/665329" target="_blank">📅 17:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
امیر قطر با فرستادگان آمریکا درباره ایران گفتگو کرد
🔹
شیخ تمیم بن حمد آل ثانی در دیدار با ویتکاف و کوشنر، دو فرستاده آمریکایی،  تازه‌ترین تحولات سیاسی منطقه و به‌ویژه وضعیت لبنان را مورد بحث قرار داد.
🔹
محور اصلی گفتگوها، بررسی آخرین وضعیت مسیر مذاکرات ایران و آمریکا بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/665328" target="_blank">📅 17:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
در حمله افراد مسلح به ایست بازرسی سبدلو در بانه تعداد شهدا به ۳ نفر رسید و ۵ نفر دیگر مجروح شدند  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/665327" target="_blank">📅 17:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a9e06306.mp4?token=Uu9DiaOV5yaydkP2ROa3NNpuDIHk6snULHl__JPQYvFPLKSVcdcDVBAVa_ZENRy5oNKAzICQMAIoO_I29E3KIWii4LGq7s6e56NpRmP5H94b2nxhza3zLjuCUrGTh-E1LD3HCphlOmXCBwn-EdeM2S6PDoocP3BWNU5lfwzjSRFWXcfug0E9NxdemNtzULS96eXJNQtTJe1rl_go8rrK6Jb35LmjA5s7INhP76sLOaG7sVTV6r0yehKOGVrOJfbiaV8u-_S0hLKgxuhPYb14_y3uH-jnMtHW-lLnADx4LCCyu1oRG0uKFtjJ0flYryAlp3xIZ9N_ZL-Cfem5_q4YrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a9e06306.mp4?token=Uu9DiaOV5yaydkP2ROa3NNpuDIHk6snULHl__JPQYvFPLKSVcdcDVBAVa_ZENRy5oNKAzICQMAIoO_I29E3KIWii4LGq7s6e56NpRmP5H94b2nxhza3zLjuCUrGTh-E1LD3HCphlOmXCBwn-EdeM2S6PDoocP3BWNU5lfwzjSRFWXcfug0E9NxdemNtzULS96eXJNQtTJe1rl_go8rrK6Jb35LmjA5s7INhP76sLOaG7sVTV6r0yehKOGVrOJfbiaV8u-_S0hLKgxuhPYb14_y3uH-jnMtHW-lLnADx4LCCyu1oRG0uKFtjJ0flYryAlp3xIZ9N_ZL-Cfem5_q4YrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
هشدار گوگل به میلیون‌ها شهروند ونزوئلایی قبل از وقوع زلزله
🔹
در حین وقوع دو زلزله سهمگین ۷.۲ و ۷.۵ ریشتری در ونزوئلا، سیستم هوشمند هشدار زلزله گوگل توانسته بود چند ثانیه پیش از آغاز لرزش‌های مخرب، به بیش از ۱۱.۴ میلیون شهروند هشدار بدهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/665325" target="_blank">📅 16:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای نماینده مجلس: تا زمانی که ۱۲ میلیارد دلار آزاد نشود، هیچ مذاکره‌ای در کار نخواهد بود
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات برای آزادسازی ۱۲ میلیارد دلار از منابع بلوکه‌ شده ایران به توافق اولیه رسیده و تنها موانع اداری و اختلاف بر سر بازرسی‌های سرزده باقی مانده است.
🔹
ادعای ترامپ درباره آغاز مذاکرات در دوحه شانتاژ خبری است و تا پیش از آزادسازی این منابع، مذاکره‌ای انجام نخواهد شد.
🔹
همچنین ادعا شده است که پس از توافق نهایی، زمینه سرمایه‌گذاری ۳۰۰ میلیارد دلاری در ایران طی یک دوره ۶۰ روزه فراهم خواهد شد.
@TV_Fori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/665324" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم
🔹
می‌دانید الان چقدر سهم داریم؟ هیچ. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/665323" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665321">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjpvhcknutsc5d97qJVFBV6SudsbRY5-D5mjMqzcTohQlxUcDEh15CaAc7lFIDMRqvKTQNgXwwGycQPEQhV_60HVMA_4TfyW9puqxHr9lWHcjkUn5cNzafKCjdO_3BFn2dP9q6N0YYNEqujdxS49D1fX9kzHO7mRdGdZgwbDb4OngLljMzijt-CiaiGCTI1eWa-zvTT-gxrZLFErazGPTd2LWASNa4payiPDl7ERMB-ZYOFHIK3p3ryGyr-N8h8iVFwN35aV5OyWe2Qk11O1eAkLHls1CgsxUdlziqGqAEo_kC74TZPnSh5OkB7C669G--8U1pPe92JJLjAWBy0dvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiBkdWI4Rm2J_5b9ZbY4OktZ9mO-DYEMyP7lZ7SrCPbZe1u9Nr0HSU22drFJZ8iTyuWySjMtT1Jv6yX8A81YrrMdRsyNOZeXW5bDKglr2wmRFesNK16GPp2DlN1iGfrVDbHDhbM7uVNAHPN_aT3N2j31T5AoTizCGfmFSXUKrTnlSIuG9vWFgVmL4BhDFAOcusU-8oqtHmooOgzwQ6HcpGoAC27sZU32GDtEJ61DAGT5-8ExjIyKKFwXZSG31uFi7KoeymKVx1daa_flNuc7UrhPZ68brtyLpkAW65UP2vlkXOcgOPcxUqHTsRlaS3mcvvuVvmxd_Cmoer_q95rtyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یک چراغ خیابانی در وروتسواف، لهستان که کاملاً با پیچک‌ها پوشیده شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/665321" target="_blank">📅 16:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665320">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f12816b9.mp4?token=g-k-kbtGAG72UyB1DikESJHCVajvms22QAUQPU-s36l2JiDub9S4i0Gf5gT5PSu5XphrH3piKt6ihDlTd2d6FitocNjEfZiAQn6jEZiT2oDUKY0mTJzY2F_NvR4nIGXqZK8i8oTrxiq7eUjg_tIgwLLKDkkqIyi4JJ2__04mJkk6Y-qUOAp79-TZxjefQ8pE5c-30lL8grdvZxNb7QwKJppqGq8bzMiHiDOqO4r__3SgcqMd52pgPyMttbcE3yptM7tQIGr1mgLnFbJ0rwu2SNSGE38zyRJMqU_Uchi-A0TMG0o7xXKcPTPdYCJ8xU-cyzu83G0wX-rt9KUr7xan9Q3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f12816b9.mp4?token=g-k-kbtGAG72UyB1DikESJHCVajvms22QAUQPU-s36l2JiDub9S4i0Gf5gT5PSu5XphrH3piKt6ihDlTd2d6FitocNjEfZiAQn6jEZiT2oDUKY0mTJzY2F_NvR4nIGXqZK8i8oTrxiq7eUjg_tIgwLLKDkkqIyi4JJ2__04mJkk6Y-qUOAp79-TZxjefQ8pE5c-30lL8grdvZxNb7QwKJppqGq8bzMiHiDOqO4r__3SgcqMd52pgPyMttbcE3yptM7tQIGr1mgLnFbJ0rwu2SNSGE38zyRJMqU_Uchi-A0TMG0o7xXKcPTPdYCJ8xU-cyzu83G0wX-rt9KUr7xan9Q3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم
🔹
می‌دانید الان چقدر سهم داریم؟ هیچ.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/665320" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665317">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ روز دهم</div>
  <div class="tg-doc-extra">محمد حسین حدادیان قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/665317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک ویژه مداحی هیئت قرار ویژه تشییع رهبر شهیدمان
💔
🥀
بر سنگ مزارم حك کنید؛
او غریبی بود که جز آغوش قمر، پناهی نداشت.
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/665317" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4BKyIbcgg255TWyUsZsAKzWnelgjhvae_LosvBXcUStUi9R3537fI7BcAba_8nq7W3BXoIPUCRZLZFv0UVeuYOJ5Skql2KzBX7BOe2T8CK0PDN76Aw0Xck4YaA6MzPlQ9zhoXZBx100xBxydCeEYyk-AKXMXAbx78F42DbAIo_BQ-S03ieOWFh8y1FcxRPqG0E5td9BVc1Z9iTI2RAXd475v46GxE-tKlzrXXQIwd0_foUQD--zyKkX9lryh8hmuXWkYCvhW2hsRRBjJy1AriVssZGyC1zUS208fNcgSWfHhIKUdvOoRJy8UxYutoXoM1AhBWL0aAIGgYglS3eCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtRJXojo3pL0LM9uHpndP9OpISXeyRKvJh3ReZ7Fd8mIz8NTiBTtqDOMY14G8wRpF01cvCPZfbT3lOdxuTMctfIj2J0FhDmY2p44--ooNQoAtfrZCXf-QyejXY7Ee_AoQslh8aWKR9GyV8Hr8KCc4mSdh5gitwYXMLrkhxItQC_MQKSKIsiuiXNtesVftQL0wIGO81tfpch8ua0TrwnqSXolvW4QsVFVX0qQExpg_sL-_pSu0uRM7-ljE0W8b7xr4DbUweRds6EcEoUHWuO2CiHnJkyuWyx_6zq_6o6qP02E89J9nzH1CM4oBt00Q7CuEvgWXp-3FL8juIuMieDgrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست رونالدو، سرنوشت عکاس پرتغالی را تغییر داد
🔹
یک عکاس با ثبت تصویری از رونالدو و بازیکنان پرتغال از روی سکوها و درخواست هزینه آن در کامنت، علاوه بر تگ شدن توسط رونالدو، موفق به امضای قرارداد با تیم ملی پرتغال شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/665314" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665313">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCmCY5RuzT3Be52aLFtrMSEKXrMzuLpUOpenl6iqYMtn8a6GCkjYwSgohuLkvC8IcCppwkAIrHIaScufBqhVQ1m6exs1lVGVbBCvMHa8MebrNqEKg26XISOphvoFp5pti1P3RHvza9KGj2bmbFjEWsEczJEfRZe26K1VWzZx3bJ4V6mZPN9nqe7IMRObqo9mW_JuHLi8Wlx71xNmpd6uOScm2cBBcyrg6KWJmXmLQub5G-uBxnS1i32yi4RcHjQ5nlSm13jWAf53JvLjKXtcac1OWy5Bt0bnib77i1imN6HS6FT-aDuhpegHBDJK7IVjMXlnGtzW4FVPlldgY4_fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
در حضور وزیر امور اقتصادی و دارایی و با برگزاری آیین تودیع و معارفه
✅
افشین خانی مدیرعامل بانک صادرات ایران شد
🔹
با حضور وزیر امور اقتصادی و دارایی، آیین معارفه افشین خانی، مدیرعامل جدید بانک صادرات ایران برگزار و از خدمات محسن سیفی، مدیرعامل سابق این بانک قدردانی شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/665313" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbrash Group</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40a4a2c989.mp4?token=ZWnL6EnA9Sf4n8jfb6r44jVBuUs-KJl4RsndFStUaNXf8nzIMYvyHdmCO1ATI0Iq2VGv2JyvYuRQVz46PoDsz--5FEkaR4mHin8KUd7pi28nOp7YcPMiImMS_aGENrat2Gn4y6YLmVRO7A7f1aNzGrwxBB6LcRLUDG8D9nGAF0d8Exgs5CziClQARpG6wJzFuksJjZkeJADUYIp_p7JHDTAZKEY9aLY8kEsLf9s3YPjgczG1-R223zM-o4NiGkP5gYuwgsrSHwzB7i8truwJCoDTwt1sQUCELgEtQ5IoR3iEYqQBWoVoHcqJ3v6DJQ45ShOuf0jpRttEhf6XggnwCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40a4a2c989.mp4?token=ZWnL6EnA9Sf4n8jfb6r44jVBuUs-KJl4RsndFStUaNXf8nzIMYvyHdmCO1ATI0Iq2VGv2JyvYuRQVz46PoDsz--5FEkaR4mHin8KUd7pi28nOp7YcPMiImMS_aGENrat2Gn4y6YLmVRO7A7f1aNzGrwxBB6LcRLUDG8D9nGAF0d8Exgs5CziClQARpG6wJzFuksJjZkeJADUYIp_p7JHDTAZKEY9aLY8kEsLf9s3YPjgczG1-R223zM-o4NiGkP5gYuwgsrSHwzB7i8truwJCoDTwt1sQUCELgEtQ5IoR3iEYqQBWoVoHcqJ3v6DJQ45ShOuf0jpRttEhf6XggnwCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه کارخانجات ابرش
🏭
با بیش از دو دهه تجربه، به‌عنوان
تنها تولیدکننده
هم‌زمان
شیرآلات
،
لوله‌های پنج‌لایه
و انواع اتصالات برنجی در
شمال شرق کشور
،
فرارسیدن روز صنعت و معدن
⚙️
را به تمامی صنعتگران، تولیدکنندگان و فعالان ارزشمند این عرصه تبریک عرض می‌نماید.
🤩
با آرزوی تداوم
پیشرفت
،
نوآوری
و
شکوفایی
در صنعت
ایران
.
✅
ما را در فضای آنلاین دنبال کنید
https://www.instagram.com/abrash_group
https://t.me/Abrashmedia</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665312" target="_blank">📅 16:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تفاوت حقوق ۱۸ تا ۵۰ میلیونی در بین صندوق‌های بازنشستگی!
ولی‌داداشی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بر اساس قانون برنامه هفتم، صندوق‌های بازنشستگی باید برای کاهش آشفتگی مدیریتی تجمیع شوند.
🔹
برخورد با تخلفات احتمالی در روند ادغام، تداوم نظارت مجلس و سازمان بازرسی و یکسان‌سازی حقوق بازنشستگان با کاهش اختلاف پرداختی بین صندوق‌ها لازم است.
🔹
تفاوت فاحش حقوق بین صندوق‌ها مثلاً ۵۰ میلیون تومان در برخی صندوق‌ها در مقابل ۱۸ میلیون تومان در تأمین اجتماعی با عدالت اجتماعی منافات دارد و ادغام به یکسان‌سازی حقوق کمک خواهد کرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/665311" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665310">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ترامپ متوهم: ما سه شب پیاپی ضربات شدیدی به ایران وارد کرده‌ایم، اما در حال حاضر روابط بسیار باهم داریم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/665310" target="_blank">📅 16:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665309">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnm09lz3RQUBeNQR1EzzGsDOt8ExdDqAjWvo_gArdgiKENy5_pFJlqDjembcCiOncll_RJ0dLa7nrNAByQ_gwhTFFpAWVajXk62dHg977mrQyrOronXMyKvqLfq4ClAnHwzqIGM4foVq0gKJvCc9ssJxmg4J2b_ye3-WPJY6IurGuAhY8EBXR-DuoDjjnHFyl5wvTpfnhrjtEYMKsY5BWAPV1WOUjMzC5T0Rz2eEkcLij8NDVp20CP1AIZTtWjL7UKTDg1-kkHPC8Xr1Wwc72AskgEQE_3FOKrcFirRBHW2f4znuZPORxezUqzcg-arXXuFNJxgbAxziH8kSyJE2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ تهدیدی خاموش برای طبیعت و سلامت انسان
🔹
پلاستیک فقط یک زباله نیست؛ تهدیدی است که از دریاها و جنگل‌ها تا سفره غذای انسان نفوذ کرده است.  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665309" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83c6cadb4.mp4?token=no6piV77lf3LsIq-Z3nbH7xXsKJTWrkA4056V6I9IU0Wfy0nbnU6PX6d7rUWlSpNvXFg5OK8eDyKqeUBOPpDADIMqaiMvD0KQ6itLEIMp169LpjknKl9O4UlZCh6TUcEWC5LO9GJ98DyZKXkTDoypVRkW36Zt-sztErmJyb-ogarQTyAE-a-y5rqcyxubWeQihdBgy5lww5dJnGaQ3Df_ViqcOAULCYF2ejSgwS9b9NYySeYmwtczR0ujSSIclJRaBcUfgUk1y17FPoBh41lTj5gi85NrqqllXoCH0h9oMEbq7q4InYqa7IrCg_fLUIu9GtjcLI1HiQqaqdx4rGxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83c6cadb4.mp4?token=no6piV77lf3LsIq-Z3nbH7xXsKJTWrkA4056V6I9IU0Wfy0nbnU6PX6d7rUWlSpNvXFg5OK8eDyKqeUBOPpDADIMqaiMvD0KQ6itLEIMp169LpjknKl9O4UlZCh6TUcEWC5LO9GJ98DyZKXkTDoypVRkW36Zt-sztErmJyb-ogarQTyAE-a-y5rqcyxubWeQihdBgy5lww5dJnGaQ3Df_ViqcOAULCYF2ejSgwS9b9NYySeYmwtczR0ujSSIclJRaBcUfgUk1y17FPoBh41lTj5gi85NrqqllXoCH0h9oMEbq7q4InYqa7IrCg_fLUIu9GtjcLI1HiQqaqdx4rGxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: ما سه شب پیاپی ضربات شدیدی به ایران وارد کرده‌ایم، اما در حال حاضر روابط بسیار باهم داریم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665308" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb7qOeFBnOWOVR4Z59ALaMWFARwcRqaI2aMZMD6NfNFQyK-zlOHW29sUGVE5dvirtdZOox6EEbf8JROJW9PzXi5H_eyQBN9sSrDLPbjLSyripDtEssDHKn-AblLsQCLXYJByma5KP6NR-In7AY-fYt8JQMEfKUNOrMklHYn4Kp0uaJGcXmX8fugwQ-13VGeSJihE5Wxs8RpfXLE-lxLzq-Jd02iNmIgA0P6x9PZ8usv-5K5RRfR1X5qHLDyGKCD9AxJamkBSSYVclipRYFVvzsXyr2hRjs1LLbuv6dWS6i8m1y4mMLcWQzbiXoxJYqUVXroynIjmuuaKhXt9LY8kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند پایان استعمار در جهان
🔹
در سال ۱۹۲۵، ۹۷ کشور امروزی تحت استعمار قدرت‌های اروپایی بودند.
🔹
پس از جنگ جهانی دوم، موج استقلال‌خواهی باعث فروپاشی سریع امپراتوری‌های استعماری شد.
🔹
بریتانیا و فرانسه بیشترین تعداد مستعمرات را در اختیار داشتند و بیشترین کاهش را تجربه کردند.
@amarfact</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/665307" target="_blank">📅 16:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665304">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SH-e8iw90vVKjJDdubr7eYUWws95mER1DMIHXNTibrueZBoLExjgn5rFDBr8nvGJfUlXz1mdsbBU3aauW0DjxtgsiNj06X8JrTeau2SWHH17xsNt9Fg-NC9oXLzpwAiYgcD2_Zmi23AC1wTDSZxMI590OccnCjwKz5VCAkqEHYbvFi36gZ7ASP8u_HuJFtW2wSZe5UlgNwKloFsONI8RDJtDIEn72S2AjhnFZz8NZ8p2E3i4pf8tx6CplpEz-V0EPfjiYXvaEkj51XJnvOggokDm-dGy0l8_a1q3b9FsHP9Xg6WgN8aLytaAvfVoELWUHpa0xHsPgPLO8uIO32eWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbzmWUxARPBGY9JsBzTWb9glrMjwLLInglLvydn1erw4tmBtPVHeXCyDf9bcvjrcX11SK2A5Is3JDBMwxnPEo1hv8gzZClwBU-hs1Qd5_jXU4NHp9tU7p85ubsNTGRgDxxw216W9Z-FF_qQsGizxyehrWImOWRDEcdlwLfRI4MEbgSVrgf9eMxJ8a_4VeTLtoJJ8pdi7k-52p-BIK63orX9tVR4QFLXiAagMVwJPaZIdKLwwmF75w9rNsIPy5QgEeXLDymEWxjbIW2ufBR1yI0MSWTsUibKxCnEaYz2blTdI2MxLAnENaW1LyftxsNzgXBKUqu4e7Bufv2Sip8uJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvAZ388wmSGf7f9U2j2cXtP15E2M-9XM9P8eTw9n7_barF27g73mVkFgDjdePWorMBtci0bxMpfX3nSmcGBsERNtJYXRd3jzEbPNs1MtZSLbK2k1751wGbZwpMKGWhFwSMir3yN6DhCIm5emLPRF5uwSsg3KpQJAdZKfJXIE_x-3GAMDDXdhKjFzeBjC486hkRUe00tD2pti1BZmzpvjr9llSow29jq0EvEba2Pe9hMHPrZd6z5afpra0iOFX0fOiPliaxJ9J5S1uI_mdX5lzfcc6oMgFB-Gxi7ybuTghzgbukRb2HLrh5i2ZA7MDUrcvEfhRO0ZfVs7lTfPRcjbpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۴ اشتباه والدین در آموزش سواد مالی #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665304" target="_blank">📅 16:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f119648.mp4?token=g30TXNruzT_FyqivUli5O-FNWiYPqxr46KbOA7yzdOLqmNQFa4DLTEwu2c1vcrDKA5nhYrtS9yx6pBqpzr_G5KOr2_gF-ELpf486uNkPqTyuRpXFrvN1RQjqxp33iiP5jUyyUPf18ANeT9QUvHJvMeB5JuQyk36f5ce85uYX4wEqaXPMsIUlrCr6b9fTOD5STdNRfdEvxjqEUoypiHCAEE7Obm7Eim8KTrZeT72EB3fXgOvmABRsBL3xqhrLQr0SPWpHmzYZ0gZAesZ_DkpxeADKlPk5Y1Po5LGTMDibQTpycYTK_mcWHALyCQ-ZPDmYIYn9qPqpzQsIIBXdtabRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f119648.mp4?token=g30TXNruzT_FyqivUli5O-FNWiYPqxr46KbOA7yzdOLqmNQFa4DLTEwu2c1vcrDKA5nhYrtS9yx6pBqpzr_G5KOr2_gF-ELpf486uNkPqTyuRpXFrvN1RQjqxp33iiP5jUyyUPf18ANeT9QUvHJvMeB5JuQyk36f5ce85uYX4wEqaXPMsIUlrCr6b9fTOD5STdNRfdEvxjqEUoypiHCAEE7Obm7Eim8KTrZeT72EB3fXgOvmABRsBL3xqhrLQr0SPWpHmzYZ0gZAesZ_DkpxeADKlPk5Y1Po5LGTMDibQTpycYTK_mcWHALyCQ-ZPDmYIYn9qPqpzQsIIBXdtabRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنج کودکان غزه زیر سایه جنگ
🔹
دختربچه‌ای در غزه میان صدای جنگنده‌ها و انفجارها، با پناه گرفتن در آغوش عروسکش از ترس فرار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665303" target="_blank">📅 16:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665302">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ایرانی: مذاکرات دوحه بر تنگه هرمز و پول‌های بلوکه‌شده متمرکز است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665302" target="_blank">📅 15:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665301">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گلایه نمایندگان مجلس از وزیر نیرو، پس از بازگشایی صحن به جد پیگیر استیضاح علی‌آبادی هستیم!
هاشم خنفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
نمایندگان مجلس خواستار استثنا شدن استان‌های گرمسیر مانند خوزستان از برنامه‌های قطعی برق هستند، چرا که هوای این مناطق در شب بالای ۳۰ درجه و در روز حدود ۵۰ درجه است و قطعی برق معیشت مردم را مختل کرده است.
🔹
وزیر نیرو، قبل از جنگ آماده استیضاح بود و نمایندگان امضاهای لازم را جمع کرده بودند اما به دلیل شرایط جنگی و توصیه مقام معظم رهبری مبنی بر تعامل مجلس با دولت، استیضاح به تأخیر افتاد.
🔹
نمایندگان معتقدند وزارت نیرو برنامه قابل قبولی برای رفع مشکلات کوتاه‌مدت برق ندارد و در حوزه تولید، توزیع و نگهداری شبکه دچار ضعف اساسی است. در خوزستان مشکل تولید برق وجود ندارد بلکه مشکل اصلی در توزیع و مدیریت انرژی است.
@TV_Fori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/665301" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na8ASjfjVFl5A3k7mpKVxF07uSNE6Ax80EKWIp5biS1__Ri8oxCEo6unNieEqUNFLpHixBRJ4YHCeKvxAzyXvs2uKFHBXrN_nMsiWKnQxdsDaFiCHFnrC7MmAdIB999Cr4SzA-azy1_i-i6J6UOdfuNAfbr4whDJg1851yBEDVLkcY3tN88MgQo2I-EzjrY9aIy-qnBd986yUvaYxoan4mtNvpeWoWECo4glfU_QBUnIPThdRczNM8rPucV_A01G12qhzsh8Apa_ehvYPix0rrEIW8IST9RAFb9qFmdqd3qq-NwULXoSW_UIOeCBB8wg-ywNfJOvUxkaWtwNUF2l5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/216c4f6e99.mp4?token=VJ9fR1yj9yuwcpRQVy6PL08GB-XbK1Nb1VkTbdOxFazbqYtmGmR9HcZS20DVCJjkjfHR_jqQDf7KeCVefJzKe-mOcK055ZVj2RQyp8FACC-91-vQW6LHjwLsRt05epqafNGCCSg9y3jwNAr230D6ELOhiZM7RG-JkMMd2TjEXkWdEj1BHZ3s-IGKzFrtYPQ2iIH3HMYge63LK_MAloNj12IZkfglpxOxpH7zyINytMNw1a6uJyZvZOywaCVl27YVe_GOUGywysESMz7iyIuCjUWr6kxoxZoV0tH76XVoBzVuitUDN6wPLt-F5g087238lUoai0R2vjSygXucmX450g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/216c4f6e99.mp4?token=VJ9fR1yj9yuwcpRQVy6PL08GB-XbK1Nb1VkTbdOxFazbqYtmGmR9HcZS20DVCJjkjfHR_jqQDf7KeCVefJzKe-mOcK055ZVj2RQyp8FACC-91-vQW6LHjwLsRt05epqafNGCCSg9y3jwNAr230D6ELOhiZM7RG-JkMMd2TjEXkWdEj1BHZ3s-IGKzFrtYPQ2iIH3HMYge63LK_MAloNj12IZkfglpxOxpH7zyINytMNw1a6uJyZvZOywaCVl27YVe_GOUGywysESMz7iyIuCjUWr6kxoxZoV0tH76XVoBzVuitUDN6wPLt-F5g087238lUoai0R2vjSygXucmX450g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عذرخواهی رامین رضاییان از هواداران تیم ملی
🔹
رامین رضاییان با انتشار پیامی ضمن دلجویی از مردم بابت ناکامی اخیر تیم ملی، تأکید کرد که همواره با تمام وجود برای شاد کردن مردم جنگیده و خود را همیشه در کنار آن‌ها می‌داند.
مردم عزیز ایران...
بعد از بازی هرچی تو دلم بود بهتون گفتم، بازم میگم؛ ببخشید که نتونستیم اون خوشحالی‌ای که لیاقتش رو داشتید بهتون بدیم.
من همیشه خودمو یکی از مردم دونستم و هرچی دارم از محبت شماست. هر بار پیراهن تیم ملی رو پوشیدم، با تمام وجود برای دل مردم جنگیدم و این فقط وظیفه‌ام بوده.
می‌دونم این روزها حال مردم خوب نیست؛ فقط دلم می‌خواست حتی برای چند دقیقه لبخند رو لبتون بیاد.
کنار مردم بودم، هستم و همیشه می‌مونم.
ممنونم از همه عشقی که همیشه بهم دادین
🤍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/665299" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELoyErWYZX3dWfyUvlQVeOhb_EOBYtBSZtjgvCygmA3k3VuMSDuOknbviv5rI9A-UDOh9US_sZGZpyLTrCJ7nShIED3uz5awUVcd2l_UU8sQsKSrjVhktcRaR3OK4CgvKkZweQW5knTVEHYRxnaYs58Y8ef85RF8LqV_0ffzG9hSiv_6ujQQrYp_EJEOPUQOD5DbZ48-VzZzWSxjO1aaM_ztb9iYa3XYFCc97Yr0yOnt0lCeXIEC9_q6mXChHJipSjoCwqquOS2mFPxGYRYLqstfuUSELQDWwM8v2rZMY9pYnm9vsyTzsGqqojariqV9lIEhguk8TCZJDwX9kBlkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساعات کاری سامانه پايا در ایام برگزاری مراسم تشییع و خاکسپاری رهبر شهید انقلاب اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665298" target="_blank">📅 15:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983e343a91.mp4?token=fs3PH90VOEMimq0sTnINLJRkGIkbp_OgCl2xdNnqFUn8TARSUwgj6iiuun5ENiUR63a0EYS6u3a5zFVy0zqm_kq-4ijZZUyXSie1B2-V-KCwqXhv8I_didJfnsHk0z6aUlV0HkAuyBLuENznQdPF-XHMJ8g9XZ1l1J5Ev6T1TPaBmSdaa9dL7lrT2RNaWipDS0dW7O11rbUmFZFGaYofUAnL54KcJKZZaGCgf7W2QucLrgo-IKNnhzwqG3DYIvUjd51ONeKhcmSF6uD4iMnvJ8dDMMT6ZvCONpWCLiHB09FMtmKzfDKpdljYBLwSgZC8ZUZctPHzx1CPZYgqmkSm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983e343a91.mp4?token=fs3PH90VOEMimq0sTnINLJRkGIkbp_OgCl2xdNnqFUn8TARSUwgj6iiuun5ENiUR63a0EYS6u3a5zFVy0zqm_kq-4ijZZUyXSie1B2-V-KCwqXhv8I_didJfnsHk0z6aUlV0HkAuyBLuENznQdPF-XHMJ8g9XZ1l1J5Ev6T1TPaBmSdaa9dL7lrT2RNaWipDS0dW7O11rbUmFZFGaYofUAnL54KcJKZZaGCgf7W2QucLrgo-IKNnhzwqG3DYIvUjd51ONeKhcmSF6uD4iMnvJ8dDMMT6ZvCONpWCLiHB09FMtmKzfDKpdljYBLwSgZC8ZUZctPHzx1CPZYgqmkSm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی تیرانداز، شکارچی دقیق آب‌ها
🐟
🔹
ماهی Archerfish با شلیک قطره آب، حشرات بالای سطح آب را شکار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665297" target="_blank">📅 15:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-poll">
<h4>📊 آیا شماهم در یک ماه اخیر افزایش قیمت نان را در شهرتان تجربه کرده اید؟</h4>
<ul>
<li>✓ بله،گران شده است</li>
<li>✓ خیر، تغییری نکرده</li>
<li>✓ مشاهده نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665296" target="_blank">📅 15:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1UcV4V1BhGgEOB-dN9WQIDH7b8fV46pDmVJKu2Lpxy9exPUaDgkFo1UCoAXrPC527YYlwo5JRMz0DhzLRVXgpYZ0nEzgNEohi8xoOkpo21BBKYUFEzLBeyIcS3HZCdaW2KDvnGSzIhjxFE4BshzP6AW-Ec5gde_8wJ-Lvg00CdimDSVtiD-_FO7fEwy8Yoj8VzhEtdbREKsokZ_o3SBLS5n5m3JfqiUu1hsoesDVxqDeIfQwL2LwdZEJvYrfzf_foE5rgbzBL4dOrgH1zfYsvIZdoLD7w6vNc2unRNRKiwj8jR1rMVWyJJ9HEvZ2Sf6gEAranI7FBac9Tta3iMepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دیده‌نشده از رهبر شهید انقلاب در کنار موشک سجیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665295" target="_blank">📅 15:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
فوران کوه آتنا در ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665294" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXQeWd2OFWXraGSZvgYPHb58d40DuxoC7CCNS9KD5E9g1k-2mEnTwB-z5DBr4rHma8lF0oHA0qX32MPC99q_LXFNQqkmX1BdERXMbWqcQtq7uW0eUg_o4l2D4iYLQ_d2cPPT2KquSvn4yEP332OBzJRsYvUmFthiDnaSplHyT76CDHF3xSJgVUDWiMEsaUrTw3yBsxpt0E299mvXJBj6VsNH5wKRViOHNscM4m29kMlU1aSW1gnytBsNvxKgFVjCYRVCrw4lGK70-OPQtKOG7QS5vPlaHApnEFBQHLFkuwwjfPaDoGtHlyuB71pwF-Q4drfSADiEHYmSKFJJ-6fkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله ایران به پالایشگاه حیفا کارساز بود؛ ۶۰ درصد تولید نفت اسرائیل مختل شد
شبکه ۱۲ اسرائیل:
🔹
حمله به پالایشگاه حیفا، مخزن اصلی بنزین و نیروگاه آن را نابود کرد و ۶۰ درصد از ظرفیت تولید فرآورده‌های نفتی اسرائیل از بین رفت.
🔹
بازسازی کامل تا سال ۲۰۲۸ طول می‌کشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665293" target="_blank">📅 15:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp6qju0J9xcOJ7Ny7FHo3_1P55gTbgc4VaCBhTDIUoDMvwxAUJIVyKS7h-E_nqUZi6wRXNOo34sR2URIGryazaMuHlY3HLojrdTjvO1zvSb659C99idlRkJYQ1eyDHLr2zfHkQ4hLFJR217ZhayQ7I3s6JwEEL335sb3DVLVkv8TeQsXLwksrz4DsTmgxhr0ERRhoJ83BJskNOcIybhD7Fj042_uEvELlgeft2y4TzdpJkcWVCUirAh5iwg5Rm0mJvSFqT3LPKDAw96RK6xSfPj4ebs0fHfLVGNedFVxuWCo0SjCbc5m3z7C_SiZkxncf2lVgMY3w7ur6BwFdAa-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه درباره شروط تازه ایران در مذاکرات دوحه؛ رایزنی درباره تنگه هرمز
العربیه:
🔹
مذاکرات غیرمستقیم در دوحه ادامه دارد؛ ایران خواستار آزادسازی ۳ میلیارد دلار از دارایی‌های خود در ازای هر پیشرفت در مذاکرات شده و هیئت‌ها برای بررسی پیشنهاد عمان درباره تنگه هرمز، راهی پایتخت‌های خود شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665292" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تصویری از آتش‌سوزی بزرگ در فرودگاه بین‌المللی بغداد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665291" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گزارش UKMTO از وضعیت یک قایق مشکوک در منطقه
🔹
طبق اعلام سازمان UKMTO، یک قایق کوچک مسلح با ۴ سرنشین و مجهز به آر پی جی، پس از ترک یک کشتی، همچنان در منطقه فعال بوده و خطر بالقوه‌ای برای سایر کشتی‌ها محسوب می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665289" target="_blank">📅 14:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPygsx7uCaa8gsi0VxlelEW7YDAR4Ss5XzyOugnAYc_OFY2qgNlLS7U5fcixkxEuLJwqrWzPvhH9QSPMIXYdD-nTCaW1vVdN6_FNt3zP0QS8FDwS-ADLoQ0WwAYYhiPNU6hez_f_2YbQmrHGVdfZztX1oNIsOoRraOafq0kcfM8mRQi89Sc-HxkqH1aPLQOKawxRFaXtTqFfeDtaGmjCW7NsmIY3ufC3bR7Y3TcfLX1DHUOUT9PyeVhofVwHUmAFy0FH9ZCNjgslkWx35Ft8dRww3p72t-SJr7Wr1R0TqpjVQAqAwvVI2ZMiEIiNAdR00nmDJOZ1Kd_4EU2hZ_5_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ بیت‌کوین به زیر ۵۸ هزار دلار برای هر رمز ارز سقوط کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665288" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAVTSJ9rYU-EvxVRmvx7SwdHMgv_-MwivbF8SXB72AfUQI3vY1HP5nRlAkDdaff1eJf4uuyUX1r2Ai9FI2WHMSL4D6bl2272tLG0g-T16RKowz1VmuCA-2iGRxMnAYr0KXFZxNlsEtcll5bHvXbZUosdRZoo_PamptIj9WrKDzsZWvZCumLT7YpiTUHKM5Lc2GxV1NywdsPlfE_XN2o69LpVT3FAQmKKjA0ecdA4QhINVIGQDqnoBdTYcR1OjgMRqAn79rOld0HdARtUN67yioqKPnWlJC5c_rkK5HlUh7M-AgPmrU7egDyHdcNALVQ226PVqxbIQeVLk-hbpGBtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رز ترنج؛ امنیت دارد
🟢
صندوق طلای رز ترنج پشتوانه واقعی طلا دارد. دارایی‌های صندوق در قالب گواهی سپرده شمش و سکه، با پشتوانه طلای نگهداری‌شده در انبارهای مورد تأیید بورس کالا قرار دارد.
🟢
واحدهای صندوق فقط به میزان طلای موجود قابل انتشار هستند؛ یعنی ابتدا طلا تأمین می‌شود و سپس واحدهای جدید صندوق عرضه می‌شود.
🟢
با «رز ترنج» بدون نگرانی از نگهداری، سرقت یا اصالت طلای فیزیکی، می‌توانید به‌سادگی در طلا سرمایه‌گذاری کنید.
▫️
صندوق طلای رز ترنج از تمام کارگزاری‌ها با نماد «رز ترنج» قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/665287" target="_blank">📅 14:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSypSvZ8Zr2KpqaNh04FUd-lFl1wQABJJ7_lX2ZX3Oksib79Jjs49X94H90hjc1bjjq1vJn8p81lUYN_jq6SZCtiXxWtACviGIEO7mpl6LQ19JPRDcsqDjnFUGFGfRPOK2lItGEbIdJE1Q5Wwq2LuwHkWUBAyPJXoo5NCbaA7IDZttN890DF9mxWdT-cJrLvbJjiRrNdd3hsVIhdHxqWZoRAfhV7iPfoDKgrxFzXSjlys4yVf58LYg_fsUmSq6v-C0YyKSIG99RRBhmegrqjbyho7YjoaKa236WTIWtmMo5sEJazbCnJCdLkL7lWSTuTk_KDUzDprgY5agNQ2xOQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا خبر داد:
بانک کشاورزی در آستانه ورود به باشگاه هزار همتی‌ها / تمرکز همزمان بر تقویت منابع و گسترش تأمین مالی تولید
🔻
مدیرعامل بانک کشاورزی با اشاره به عبور منابع این بانک از رقم ۹۲۶ هزار میلیارد تومان اعلام کرد: این بانک با اتکا به اعتماد سپرده‌گذاران، در آستانه ورود به باشگاه بانک‌های هزار همتی قرار دارد و این ظرفیت جدید را به‌طور هدفمند در خدمت تأمین مالی تولید و تقویت امنیت غذایی کشور به‌کار خواهد گرفت.
🔻
وهب متقی‌نیا رشد فزاینده منابع این بانک را نشان‌دهنده افزایش اعتماد عمومی، ارتقای کیفیت خدمات و تمرکز بانک بر تجهیز پایدار منابع دانست و افزود: این شرایط به ما امکان می‌دهد منابع بیشتری را به شکل هدفمند در اختیار بخش‌های مولد، به‌ویژه کشاورزی، دام، طیور، شیلات و صنایع غذایی قرار دهیم.
🔗
مشروح‌خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/665286" target="_blank">📅 14:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دستور قضایی برای ترخیص خودروهای منطقه آزاد مازندران صادر شد
رئیس پلیس راهور مازندران:
🔹
با صدور دستور قضایی، فرایند خروج و آزادسازی خودروهای دپو شده در منطقه آزاد و گمرکات استان، از ساعت ۸ صبح فردا، ۱۱ تیرماه، در بندر امیرآباد آغاز می‌شود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/665285" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6db7G-eimb4s4ljEfVmQOOpvtUDPQuFLdOiFoPmZTlFarYJBlREgwXFZWAJ4oHaB5_AZG3t_mBKuTEM7IYqQ1bfW9CTWapaXZcwoPaWYq5zefOwtWriuwRztyxgGxXmV20HJnCuS4ZkIZ3eSDOAkU-YIaSvdChFQwhVSLn66v7fK2IAEGuwaPhDuyrW9De3Zg7lL7LXSC8-yxMsttBnnYwAtH48rQNOK89lC3Kofk5TuhiFYXlgqqYKvRRpMkM46BSWLzaiZSNgTe1lYvPeNI8x0RWLtk45sVcOowHyMRopz87ifiPaidVr57JyrKGkKzIOidQeWc_3WFQbhZrEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از آتش‌سوزی بزرگ در فرودگاه بین‌المللی بغداد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665284" target="_blank">📅 14:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
گزارش UKMTO از وضعیت یک قایق مشکوک در منطقه
🔹
طبق اعلام سازمان UKMTO، یک قایق کوچک مسلح با ۴ سرنشین و مجهز به آر پی جی، پس از ترک یک کشتی، همچنان در منطقه فعال بوده و خطر بالقوه‌ای برای سایر کشتی‌ها محسوب می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/665283" target="_blank">📅 14:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
کارنامه مثبت دولت پزشکیان/ صنایع در «تابستان» بیشتر از «ماه‌های عادی» برق می‌گیرند!
🔹
بر اساس اعلام صنعت برق؛ از ابتدای خرداد سال جاری تاکنون، صنایع انرژی‌‌بر ۱۵ درصد برق بیشتری نسبت به مدت مشابه سال گذشته تحویل گرفتند.
🔹
در سال‌های ۱۴۰۰ تا ۱۴۰۳، مصرف ماهانه برق صنایع، در تابستان کمتر از ماه‌های عادی بوده. موضوعی که طبیعی به نظر می‌رسد زیرا در پیک گرما، اولویت با بخش خانگی است و برق صنایع محدود می‌شود.
🔹
حتی در سال ۱۴۰۲ صنایع در ماه‌های گرم سال ۱۷۱۰ میلیون کیلووات ساعت برق کمتری دریافت می‌کردند که یک رکورد منفی محسوب می‌شود.
🔹
اما جالب اینکه این الگو در سال ۱۴۰۴ رخ نداده و اتفاقا مصرف برق صنایع در ماه‌های گرم بیشتر از ماه‌های عادی شده؛ آن هم به میزان ۸۷۸ میلیون کیلووات ساعت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665281" target="_blank">📅 14:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9bd6a5f10.mp4?token=NhrQVURFrQyi2CQEr1kdOtZ1n9Ingaij4aEcdfEUPXWbSlUUziSyCMPjNKVvl-LKPi9V-gL0PaiAnbw-i2LneX3IXSOFsuF_PvSl8srLQFQ6dWR7WvZbsrCvg39dhEjTdy0Ha65lnYk4CzFlDqL3QsxFa-wJau_dBWVie2MDqeqFPXWiM88n5ovdYa1lkJ_7xJ1QCteO5aYkSdF-sdtjNkOYK5TDMvsDTRyWQpxxDYTG_rn0cw7BipqTVKPvwBdGLx1_uK9DDj8RDQkx5MRPaisd9FIA22PSLAavHl4Wlwprc-vahpD9aXDGxRb2Bq1W-hF2iOuoscjDKEkNOFIZZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9bd6a5f10.mp4?token=NhrQVURFrQyi2CQEr1kdOtZ1n9Ingaij4aEcdfEUPXWbSlUUziSyCMPjNKVvl-LKPi9V-gL0PaiAnbw-i2LneX3IXSOFsuF_PvSl8srLQFQ6dWR7WvZbsrCvg39dhEjTdy0Ha65lnYk4CzFlDqL3QsxFa-wJau_dBWVie2MDqeqFPXWiM88n5ovdYa1lkJ_7xJ1QCteO5aYkSdF-sdtjNkOYK5TDMvsDTRyWQpxxDYTG_rn0cw7BipqTVKPvwBdGLx1_uK9DDj8RDQkx5MRPaisd9FIA22PSLAavHl4Wlwprc-vahpD9aXDGxRb2Bq1W-hF2iOuoscjDKEkNOFIZZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کشتی به گل نشسته در مسیر غیرقانونی تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/665280" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شهردار ایلام بازداشت شد
🔹
دادستان ایلام از بازداشت شهردار این شهر به اتهام سوءمدیریت و تخلفات مالی خبر داد؛ طبق اعلام مقام قضایی، پرونده تشکیل شده و بررسی‌ها برای تکمیل مستندات ادامه دارد./ فارس
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/665279" target="_blank">📅 14:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=OdGJDWXu-0kku581W0LpFF9W2h2HB6r4ESjXKqHn0iYkA3Sq4lWZRB4aAoYaA1qj8SPJDL95L5DcdsYHN7GI0NmGq25T1KP5v2YC-19Ne0JjVL68-fwQfNRKBeNHad_36gsmFzmXIMfZDyUNiQ-c_ERasVHd6XfOMs7aq2za8bTkzsKantkhCQKAtqU-t1NYdXIDbf72aMkfOEBn-KNtyHT8mAo2Y42e1xlLpPbfWp0zhhuANqe41Ud90tmwJwwzY5mqAc_abhxoQFyb04y7_QgqwpE49Gk1GB64PCn2ARVANTIyTgZKFgxIZqEuwXs6DEIgRpmOHUbPv6r-kHmghi6Vy4-dhHyg9pGpo-xxONEkMEzOw6DLiGPaBlyxyipKgswQVQlws0K4u5nKg3TiesSX7NlGFHrU9rUKGIE3ebNiPvm7qNDfm-hv4yi88uIuMYOvmi70XSLagJHaUpdaEhSB0kTRvz0qg5HDJeA0l_6lGLlBQYXeUooH4K2y5xjrhGJe4JTSnXAZY9PbBvoAmO7-fIwoSxl6Vd8pFS73NmUZ_ZJSLOM_d9Kty9ARWQAmKivYoyL_qo1pDsy0lqBRmldFxE3z61UMbOQbmsfdZsDFdHPMxEgknMvdlJXjwdcy00BYkxlKEPwLs721Te4kVbF-JiVh1AwMd43JPLv22Zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=OdGJDWXu-0kku581W0LpFF9W2h2HB6r4ESjXKqHn0iYkA3Sq4lWZRB4aAoYaA1qj8SPJDL95L5DcdsYHN7GI0NmGq25T1KP5v2YC-19Ne0JjVL68-fwQfNRKBeNHad_36gsmFzmXIMfZDyUNiQ-c_ERasVHd6XfOMs7aq2za8bTkzsKantkhCQKAtqU-t1NYdXIDbf72aMkfOEBn-KNtyHT8mAo2Y42e1xlLpPbfWp0zhhuANqe41Ud90tmwJwwzY5mqAc_abhxoQFyb04y7_QgqwpE49Gk1GB64PCn2ARVANTIyTgZKFgxIZqEuwXs6DEIgRpmOHUbPv6r-kHmghi6Vy4-dhHyg9pGpo-xxONEkMEzOw6DLiGPaBlyxyipKgswQVQlws0K4u5nKg3TiesSX7NlGFHrU9rUKGIE3ebNiPvm7qNDfm-hv4yi88uIuMYOvmi70XSLagJHaUpdaEhSB0kTRvz0qg5HDJeA0l_6lGLlBQYXeUooH4K2y5xjrhGJe4JTSnXAZY9PbBvoAmO7-fIwoSxl6Vd8pFS73NmUZ_ZJSLOM_d9Kty9ARWQAmKivYoyL_qo1pDsy0lqBRmldFxE3z61UMbOQbmsfdZsDFdHPMxEgknMvdlJXjwdcy00BYkxlKEPwLs721Te4kVbF-JiVh1AwMd43JPLv22Zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی چهل‌سرا در جنوب مصلا برای خدمت‌رسانی مراسم وداع "آقای شهید ایران"
🔹
فعالسازی تلفن ۴۰۳۰ برای اطلاع‌رسانی مراسم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/665278" target="_blank">📅 14:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d2420819.mp4?token=jUMXl_t-OPM--5xHGT-H7YWTijnRras2fEyN3EUCfXeuS6GIi3pw_ZqD88q-QgfQP0QyRrfXO-bwHgzFHB7E7SUIoKwsZmQNyy7dQr77ypr9y1BUgAk8GGxP-bCl10xrpX3yWtL25djuTwbXurSap_jDjh4xJD9ldDQWZORmBQPib-f03PC4zGuSviZgeV7FGLqqdUvgqexGL1RVgdbpDXacxMfaTnXaEsUOuWm6iN-yzrn6cfsq3qAEBM1R1rd_fA5php_ybw1DvwSQgHzwQzRP5VB906b6D9EyIIr35Hlz9tCcurDGWPyJBcCTO9Eg51_WduUh4P9rvM59rjc4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d2420819.mp4?token=jUMXl_t-OPM--5xHGT-H7YWTijnRras2fEyN3EUCfXeuS6GIi3pw_ZqD88q-QgfQP0QyRrfXO-bwHgzFHB7E7SUIoKwsZmQNyy7dQr77ypr9y1BUgAk8GGxP-bCl10xrpX3yWtL25djuTwbXurSap_jDjh4xJD9ldDQWZORmBQPib-f03PC4zGuSviZgeV7FGLqqdUvgqexGL1RVgdbpDXacxMfaTnXaEsUOuWm6iN-yzrn6cfsq3qAEBM1R1rd_fA5php_ybw1DvwSQgHzwQzRP5VB906b6D9EyIIr35Hlz9tCcurDGWPyJBcCTO9Eg51_WduUh4P9rvM59rjc4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسواسِ والدین، قاتلِ نشاطِ فرزندشان است! پدر و مادرهای وسواسی حتما باید خود را درمان کنند
/ مدار
این گفت‌وگو را به طور کامل اینجا ببینید
👇
https://aparat.com/v/jjy2nnk
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/665277" target="_blank">📅 14:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665276">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رایزنی غریب‌آبادی در قطر برای اجرای تفاهم‌نامه آتش‌بس
🔹
کاظم غریب‌آبادی، مذاکره‌کننده ایران، در دیدار با نخست‌وزیر قطر، ضمن بررسی چالش‌های اجرای یادداشت تفاهم «خاتمه جنگ» و تحولات لبنان، از تشکیل کارگروه‌های ویژه برای توافق نهایی خبر داد.
🔹
به گفته وی، زمان و مکان آغاز مذاکراتِ این کارگروه‌ها در حال رایزنی است./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665276" target="_blank">📅 14:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv5o0bRb8lYuDJ9Liviovv9Wpm2pI2GJ9zESWoHCWRRVWf4xA86AA2mFLvEarhrXUN9AC9hAJNsNk1VZWcInMkoA2va8SeZ2T443cx5mB0-8z30mshizRwLTpy-H9QsvszsxHINZ7RwA6EdRJdAhF1AvDvtGVsfnvuVvDqtZr28hdLpGw132x6nvlSXuod8XjsgEs8npW5y3CVWwcgAqX7Fahe_zmH9p9KT_OjHXER0_1ZPaCRje3hBSTYkSIR0rNNGvQLc7vx9EKfgWrhqXz1UgLajbuMsb6o3ZNDfIzoXiNaEPXrnWQh8V0RhG8V3hetLWw8QRpEdfb8p4HYs8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز یک واژه، برای فهم بهتر خبرها امروز نوبت اصطلاح «کیفرخواست» است؛ می‌دونستی یعنی چی؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/665275" target="_blank">📅 14:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXeZ0rfaLxuh1yfuWMiIkBoeqMf_Pu3l5ILaADZirt5yrJKEfmSLLDMX2TMrROfrNL7YJTQ2fOla1OojW4SnZCtDegV9HeXKLsPVt8UBHrtGTymFTK7Mztb_p2RBWfenRlWWA9CX-pRc1czRTBEOHIy-4zXL_DR_5f5GkRyhhlEP_m4sMoMtK1VAzpSYVQIxr8ltzVAE4xGQHCSzPDg0J3QDuA0MP3VmSWqdoOq_TQcRR6XroatPrzPWQsNvr_SxnlB-xoRJHDPigz_38xd7PQIOmFWOcnHTo05gdRG1fNEjLDjq7K_TfpoUUKvtXVABUFOud4FwX5nQChE5PaAKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: مراسم تشییع رهبر شهید انقلاب باید نماد وحدت و انسجام ملی باشد
🔹
رئیس‌جمهور خواستار تبدیل مراسم تشییع «رهبر شهید» به نماد وحدت ملی شد و از مردم خواست با حضور گسترده، پیام همبستگی را به جهان مخابره کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/665274" target="_blank">📅 14:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_o3bmvNhrd5mVIRt6m2okJT6Z70tsxHMYIZUNsCpkuABkHMrzGGU_2VBv6TPfE487S1jGprgpOPRbcbm_AfuKWBed01Hz-QKEl6LEYE1ahSxfsBDqsHUoH1xJjG0coggSj9x0F7T9gsRkJvjmXmIFic2eszlvs4_YY7uZNFft25fBLwyctZpkOMldgACDAGwtllkTTxiD3uUus46CGWoOjuIubSaxLFw9ljWuRfkmqsbqam847IAM2TwdXxJKTN4UAfg1zJ00AVHzPEwXo7LHZ_dRYP0iu3e0HSvP1kImS8O74KU-2TuOz5doGrJ8zvyil0BN_z4WDLlxxCqTvY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ قاطع وزیرخارجه به تهدیدات گالانت: اسرائیل را سر جای خود می‌نشانیم
سیدعباس عراقچی در واکنش به اظهارات خصمانه «یوآو گالانت» علیه رهبری ایران، با تأکید بر شفافیت مفاد تفاهم‌نامه اسلام‌آباد، هشدار داد:
🔹
رئیس‌جمهور آمریکا متعهد به مهار این «جانور دست‌آموز» در تل‌آویو شده است؛ اگر آن‌ها از دستور ارباب خود سرپیچی کنند، ایران درس لازم را به آن‌ها خواهد داد و هرگونه تهدیدی با پاسخ فوری و قدرتمند مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665273" target="_blank">📅 14:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نماز آیت‌ الله العظمی سید محمدرضا موسوی گلپایگانی بر پیکر مطهر امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/665272" target="_blank">📅 14:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665271">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
پیکر داماد رهبر شهید انقلاب روز جمعه تشییع می‌شود
🔹
مراسم وداع با پیکر مطهر شهید مصباح الهدی باقری کنی، داماد رهبر مجاهد شهید آیت‌الله سیدعلی خامنه‌ای، روز جمعه ۱۲ تیر از ساعت ۱۷ با حرکت از میدان دوم شهران به سمت پل شهید احمد کاشانی برگزار می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665271" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZBC5LfyOj-UV5FYcOYC1JWXNcnVj3AUAbNdm6iR_rTsWUyvBlXkThU7BmlAgduDcK9ePcuwG0Zjpy7WfnJZSxD0R1-TRZOGIQIizardS6Hv3c75HuN4ZrjOjYgfQVIY61o8MhuRWRTEveQ08HjySygbYPEJLMBU4D4SNp4DHm_d30cTmTDnYUc5CrpMpkq3Wm2pyaF8CbJzD43toqD6P2AsJtvXatCZTkzZhkB-u3VXQSPuP70PT2u0bm19IrYXQLW-RBPFKZ7nxcI_MNv9fckx32AewScVzdyWvjiF_pZdx3sWmwQEin7gzs1noTdSYymEJH5SSGewDsdJdZbpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی جهانگیری، رئیس گروه مالی گردشگری، به مناسبت فرارسیدن روز صنعت و معدن پیامی صادر کرد. در این پیام آمده است:
«صنعت و معدن، ستون‌های استوار توسعه اقتصادی، خوداتکایی و پیشرفت هر کشور هستند و شکوفایی این دو حوزه، مرهون همت، دانش و تلاش خستگی‌ناپذیر انسان‌هایی است که با نوآوری، مسئولیت‌پذیری و روحیه جهادی، مسیر آبادانی و آینده‌سازی را هموار می‌کنند.
فرارسیدن روز صنعت و معدن را به تمامی صنعتگران، معدنکاران، مهندسان، کارآفرینان، مدیران، متخصصان و کارگران پرتلاش این عرصه تبریک و تهنیت عرض می‌کنم و از نقش ارزشمند آنان در خلق ثروت، توسعه پایدار، اشتغال‌آفرینی و تقویت بنیان‌های اقتصادی کشور صمیمانه قدردانی می‌نمایم.
امید است با اتکا به سرمایه انسانی، دانش، فناوری و نوآوری، شاهد شکوفایی روزافزون صنعت و معدن، افزایش توان رقابتی و دستیابی به افق‌های روشن‌تر برای ایران عزیز باشیم.انشالله»
گفتنی است گروه مالی گردشگری با حضور در ۱۱ حوزه اقتصادی و ایجاد بیش از ۴۵ هزار فرصت شغلی، در مسیر سرمایه‌گذاری، تولید، توسعه زیرساخت‌ها و خلق ارزش برای اقتصاد کشور گام برداشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/665269" target="_blank">📅 14:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665267">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5969f713.mp4?token=RtHPzx6cIkQv-3gcvfxIYw51YwIZpBXE_zVx1qlkAv-Yr3qv37esrg81XqdhvXFmG9p6EIxXD8acuKmyq-HTon8NECWkX10X0Pqdm8QM3hzSqNI3_8Un8zwKIsnvLPjrAZ2yy5DIxDJFvZnLWaW5le_8E63RyK3TFbUKnyJVrs2Mjpn240jah9jd8KGcd4BZvL7lw_jv19aF-aFrsNUCy4LraB4XQN6PykAH27xAWAjB8QM5bLC6f6zeJcFqIylFkDQU1--V46qz6UyrSs9qayOHNSNbz79FW97Ew8H41l5JRSb26RZAiO5p0LbANDanY_y3IOlyv1FxHdEemrYmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5969f713.mp4?token=RtHPzx6cIkQv-3gcvfxIYw51YwIZpBXE_zVx1qlkAv-Yr3qv37esrg81XqdhvXFmG9p6EIxXD8acuKmyq-HTon8NECWkX10X0Pqdm8QM3hzSqNI3_8Un8zwKIsnvLPjrAZ2yy5DIxDJFvZnLWaW5le_8E63RyK3TFbUKnyJVrs2Mjpn240jah9jd8KGcd4BZvL7lw_jv19aF-aFrsNUCy4LraB4XQN6PykAH27xAWAjB8QM5bLC6f6zeJcFqIylFkDQU1--V46qz6UyrSs9qayOHNSNbz79FW97Ew8H41l5JRSb26RZAiO5p0LbANDanY_y3IOlyv1FxHdEemrYmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان عجیب ازدواج و جدایی محسن مسلمان؛ ۲تا خونه و ۱۱۴سکه در سال ۹۶ دادم رفت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665267" target="_blank">📅 13:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665266">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f147454758.mp4?token=SKatDpfC9UwpcPlN2GYtbgNoB9h6eTJ-yVmM6ER6rbTe2Q83V1MAGE-9JnuTuV9hvet7NMjyOUT7woAkljGYYO103KP14oyfZb-g28Ce9uwJBmZWj3TyVwL5HU2iWUUBEqCa2KBfryM4IDkmYK4Gev4e8bXVE4ccx104CTz21Uv0FeppTdHEFGe5vBQT9Uu6hnu__UFN-CjpyymQ9kZBJ5ZaSdHuF_LXhCFhcEw-rIkdiZ8LTEDdX2cAOEDezn8qOEbljuZ8h5SE-_CZYtp2IlFnpfN0unsv4Mt33sP_1Jwu-n_Ebt1uPwAhhtjdC_Ue-en6GrgV-PpkKz0Uv212Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f147454758.mp4?token=SKatDpfC9UwpcPlN2GYtbgNoB9h6eTJ-yVmM6ER6rbTe2Q83V1MAGE-9JnuTuV9hvet7NMjyOUT7woAkljGYYO103KP14oyfZb-g28Ce9uwJBmZWj3TyVwL5HU2iWUUBEqCa2KBfryM4IDkmYK4Gev4e8bXVE4ccx104CTz21Uv0FeppTdHEFGe5vBQT9Uu6hnu__UFN-CjpyymQ9kZBJ5ZaSdHuF_LXhCFhcEw-rIkdiZ8LTEDdX2cAOEDezn8qOEbljuZ8h5SE-_CZYtp2IlFnpfN0unsv4Mt33sP_1Jwu-n_Ebt1uPwAhhtjdC_Ue-en6GrgV-PpkKz0Uv212Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر آمریکا در فلسطین اشغالی: خداوند ۳۸۰۰ سال پیش تصمیم گرفت که اورشلیم پایتخت اسرائیل باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665266" target="_blank">📅 13:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665265">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe9a027b9.mp4?token=kk9PwjwaeVWn5p_NijlfXvnBefd_s6veL9jvcg3HhPNJAQ1uI2RVtlQyvnF2hu65E1NKY-VdJORlASFmR28Xp47R9ADcKVS857zSoFI43iXNCNcHYpldEaCBawHRnlzCnwwl0icTrCPh-nje7VbjsTJybZuCUJG7F4Gl3dtWsQmUOKKY0M2z1hN3ksAgs5e86Ro5qMIReeNQAlnvcgwqjMrDA6YhpsL-1tzDwbIb2HpMrxPylaFuP1RLs1eDiqZ640aP8NxSpdXrHLuAMV0cuNR_LnvlHa8jGLngTUKZnyw6RZAm2RUbDKPfr8OIx_kQrNJ39by6ws8MiUlMDVSyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe9a027b9.mp4?token=kk9PwjwaeVWn5p_NijlfXvnBefd_s6veL9jvcg3HhPNJAQ1uI2RVtlQyvnF2hu65E1NKY-VdJORlASFmR28Xp47R9ADcKVS857zSoFI43iXNCNcHYpldEaCBawHRnlzCnwwl0icTrCPh-nje7VbjsTJybZuCUJG7F4Gl3dtWsQmUOKKY0M2z1hN3ksAgs5e86Ro5qMIReeNQAlnvcgwqjMrDA6YhpsL-1tzDwbIb2HpMrxPylaFuP1RLs1eDiqZ640aP8NxSpdXrHLuAMV0cuNR_LnvlHa8jGLngTUKZnyw6RZAm2RUbDKPfr8OIx_kQrNJ39by6ws8MiUlMDVSyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قتل نوجوان ۱۴ ساله فلسطینی توسط ارتش تروریستی رژیم صهیونسیتی در کرانه باختری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665265" target="_blank">📅 13:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665264">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTxvKgQHRyxklfZZz3jacNhv8BviG_8bLobZdPmUi7y23cM2aCoJLoPBU4igH1pyHRhDulmCtc6JprFrGNGtPa23gPVnJkD360UThLie_uUx86LgT1wCFNQortH46PhzGio8pW_xdWe64hptTesPRkHMKate-XgI9A1no8XH9vQ6EcHWJNVjG3Y1mSJxubp3ZNKN5r3baq3Gz_DgPb635nlrrWtLS06CTYHHLIzkMQ5HvESEBcO-UqKtDoNmu-QyNMnjr0N9cf7A1Z_u1QcC3U3if-i6_aX0WPv8_abmuXynq3bqwd5gY1-VQcENW2s__S1FbT7Q9I1BsSoPo7ou-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین بازی‌های جهان/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/665264" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665263">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8NK5vTCJRbEv9HjLkXQfXC8cmhZSnuYei7slFllD6YtYV5-RUzyHLmr4Qb7blAQDXsHI5QVB-paLHw6YW_hBidreSRwuCq_ChMe9wyRPyKnj3ogR97sQksyNwnGoSCS732ebX0q2elyvkMGIGeELwgKDEU21gAeDr197e9ry6Uur-IyMoiF1uMwrH0LqFxmptfnfAJ2W6rX9c2PQj3czLv1hrCvQllG06rSaTNZ7XTLI5VEcYQKOsA-wWpwO38XMKxB-q_Y7aInXRrg-0JhbnaToxQXvITrT5Xcmg4DMjMll4yMvcYMTywSYnS99nzgToGrM3Vy0lFArBDDAL06bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت نفت اسیر جنگ روانی نخواهد شد/ وزیر نفت مجدانه در حال انجام وظیفه است
📍
سامان قدوسی، مدیرکل روابط‌عمومی و سخنگوی وزارت نفت در اکس نوشت:
🔹
جای بسی تأسف است در روزهایی که ⁧وزیر نفت⁩ مجدانه در حال انجام وظایف و تعهدات خطیر تعریف‌شده ⁧وزارت نفت⁩ برای خدمت به مردم شریف ایران است، عده‌ای معلوم‌الحال با شایعه‌سازی به‌دنبال اجرای نقشه‌های نخ‌نمای خود هستند؛ وزارت نفت اسیر جنگ روانی نخواهد شد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/665263" target="_blank">📅 13:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665262">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d177a891d9.mp4?token=dhr93xo6SxF_HRzEs8KJxxqfq87w7nym1bWrr8M63rAiUDfjddt8LlEvmMoniCp0_YUBdA-IUUt5iY4QZhpxHTPx2tiZIelFQB9hjRMwsrqg4LVnJ6eZNZ-c-cn1C_8It4S_9Ui3P2R0-9fHG-NEQ4jJTPu2q5R5-9Raz-sp-d-5XMo0mbDGQVo68ls9mzhs5NsgCgRDEKFTP516K9xFb4J34Ah8sUUJyqooapKQYMcwCHl14glafCYZXT9GqvtorMIzE96FYO9dSP-rhwmFMn3Jl1lyX-7513tae4P2b2PbVprDMP9KQPDY1CMwaePibgEbB1xz9iOaV5xb99cZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d177a891d9.mp4?token=dhr93xo6SxF_HRzEs8KJxxqfq87w7nym1bWrr8M63rAiUDfjddt8LlEvmMoniCp0_YUBdA-IUUt5iY4QZhpxHTPx2tiZIelFQB9hjRMwsrqg4LVnJ6eZNZ-c-cn1C_8It4S_9Ui3P2R0-9fHG-NEQ4jJTPu2q5R5-9Raz-sp-d-5XMo0mbDGQVo68ls9mzhs5NsgCgRDEKFTP516K9xFb4J34Ah8sUUJyqooapKQYMcwCHl14glafCYZXT9GqvtorMIzE96FYO9dSP-rhwmFMn3Jl1lyX-7513tae4P2b2PbVprDMP9KQPDY1CMwaePibgEbB1xz9iOaV5xb99cZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲٠۲۶ #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/665262" target="_blank">📅 13:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YInJEe_PILdJpwrkRIWby8P0FaxNzcEtmeZiQgMkztsqlsSp5AsgBMebgFQLtCEo8Ld0dT8WjBrN6jkoykUQPVwKBVeGdzRaCvHTFRmrHuCVhQo8se7U2580rzVvpQitYbZIJ0NOD4YSAt3PEWyPgYhE5Z2-tdATyyN1bO6uW1ZBSgzhO-eCHKXm-BH6hg_ChDaomaEXBtY1mfGv4UYEEykXodwERT8PfPG40xmRSTxvadWwPDqJxQBSxtfi18veT44H1EksHSfsHyF0lP2ylUrOllQPjxDhuDe7ASjfl2pW8EqHYpzCSYqZ4E3NMIVqtGSxZIluteBXWKAE5VFKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
علاقه‌مندان به بخش
گزارش ویدئویی
سوگواره «بدرقه یار» می‌توانند پس از مطالعه آیین‌نامه، آثار خود را از طریق لینک زیر ثبت و ارسال کنند. در صورت عدم امکان ثبت از طریق سامانه، ارسال آثار به شناسه رسمی دبیرخانه نیز امکان‌پذیر است.
#بدرقه_یار
▪️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
▪️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/665261" target="_blank">📅 13:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbdhRGrXb7PJG4bjmmP83YZTNJ2HJxColOwlw3urXdcN5ejH76WOvzRTW4Lk_rGGEUk4pEVZ13lnxjI9vvCvAddcBcYAN0rSLu_MBFdxBlAlCq3KJuuLxzGwNGs3jbYFKPjxlvpzwicRrh8Ga6VNfxHpJWRNgCJSJIHha7mjkXANcBj8Fhi5oqBax0d8praZQJrLTx1HaypYvihNwmk-FL9fxP-R3V4-0JXxbhC9-byC2Uf6AL59VFmRZRqgnfoMDwFfVbDpBLrhjtwfLMuahNlC41RNkFxYriD9MBSxZEKM4QYbVOvo0ckU_Pjfg4inAM8MRgt4u1-s_po9xcMAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تعطیلی استان‌ها برای مراسم تشییع «رهبر شهید انقلاب»
🔹
بر اساس بخشنامه سازمان اداری و استخدامی، استان‌های تهران (۱۳، ۱۴ و ۱۶ تیر)، قم (۱۶ تیر) و خراسان رضوی (۱۸ تیر) و همچنین سراسر کشور (۱۵ تیر) به منظور تسهیل حضور عزاداران در مراسم تشییع پیکر مطهر رهبر شهید، تعطیل اعلام شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/665260" target="_blank">📅 13:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
معافیت تحریم نفتی فقط برای فروش‌های جدید است؛ مبالغ قبلی را آزاد نمی‌کند
علی مسعودیان، پژوهشگر دکترای حقوق بین‌الملل:
🔹
با توجه به موقتی بودن مجوز ایران، باید در قراردادها، سازوکار‌هایی برای دریافت قطعی پول و جلوگیری از اختلافات بعدی پیش‌بینی کند.
🔹
اگر قرارداد در دوره اعتبار مجوز امضا شود، اما موعد تحویل نفت یا پرداخت، بعد از پایان آن باشد، ممکن است دوباره با محدودیت تحریمی روبه‌رو شود./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/665258" target="_blank">📅 13:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از یک مقام ایرانی: مذاکرات دوحه بر تنگه هرمز و پول‌های بلوکه‌شده متمرکز است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/665257" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fx6oboJ_Ko7B_rGAwVRM3VYA_IFrAW749_YIaK--D_g4-O3qhsJSyabqegoWuIJIqyEBgT3y1K-9o3xr-7yG81fCa6jn9hnAKcdGwZ8OwIu5uf_QeA472mloMpwAKcJCIPFG5ojs91u4odBz--mBdsIybqXeF3pKkZXmVt_w6gnUmeoNrXjjG1u5EPeLqqQccaItJkSi_NweaOE6Di_8BB3izmgD8-YGNRKqegH0g5_vk70fPwmx2bl7d68EMjijxO0Olci28ZAsDHkoLA7njFHvj3CxABwe1yrl8gAtcEseEsSytzmQiYn02cXPDera9-tGnb6wi_IDfVDRTsPncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwbdMOvcEMe35BiKF1xnj67Un0rD3qs1NYshyiHwjQ6n6110TD22nHAZw4rlk34vIhli9y3M9BncvWUOId90KK8CV_nGKV_eqSUHqA8LADiSNgS255GxPhm0gsXP67oYNXG6cQiiDZPLsFJcSeiAU6NWlftLGi8M7RYVGNf0a9h3dolRZW6cPgvRIklCb5fxUyec7T_t20y3VLPHq5sNVZHedv9Jt14bQ5Ui8ka77ighIO10pDLmYqzEKhsshyUeS-SxZJNpiL2cQKG4yirTam0DDbN-aKHYDKpnQ76lKKeXBCKKZbRjtgdVhC2l5rLStTwd84sGToormKnagf3Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TETeS2w5ByIyMI-srkwbbRRnZstAQSatSAFpiMoYr_4qD4OnROAC5_F588Iz51EFEnpGreEEcWGWCIrCKtL3N2KQPzHlB8xMIDphWme0IeKMkf7-EIMC1EA_6ycxBxEjERjj68mrvAzAZl2PYv_7RAYKcWGwprFPtPUYStWou-oqRDpnf_uVuxGKB4tYvzutifOJ3pF3aBooufOB_E_DisBdXGVIg_9gf_bG8FIRww9dbuEfTsjLTe8Z2j-8oRot5PnPWQEIo9rkzP78bpy8KxAbN462Txpg1piuKJQ0Y63fAfUHLJxxo-eRKr3ZzhGUThVp0jE6CODJPcgmOxPqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSrsM3h1TYicFwX2rvRRHWyHOcuLLs7S2FDsJB7zKzY3UIGdB6KEfwyiZLSoNwFG5z7WQaDjaidvkJeQYKfT8wvPZRRUfU2CehmT7qgGDaWQ9Vz5DLQymAlM643H2flkDlO1K4I-HCmXXoRkMPXkz-1Zs17duDGA77akDViDViuVVY6oFNXBR6tyOXhHZZM69ym1qNewOlG8v-DRDoGDSMG5mlN-A__1W1Oa05gGS94qtqv3fjTx5tDdqUVzjCSWsJFywcyNkwOBoUWjyOn3IoNCY1jaOhNllOMorfpyUA0J7VS_vE0Bw6MH69twM40k5spdkCzzXWwpWVv8WFfbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlxJ9T9R8Qpdywdl6GicZWYO6prMErSH1xMkYwB7mSThG3OYME6nilTW_q_HIAcmlphKqvbP-ELjCODW4f2Xv2RcGrT1gghoibdD0UWR23hCmt12gQLYvXahSKDvk4KOtTkh40F5T5n2mUMvfc0HIB9eBW-t__uDLOZF-04-Mcyc2tWQQBkFNIM6h1AsJpNFGU7Pm7IgbElw0aJPiTv5gwwVLr_VKkf2-t9pD3El0IuCWkYm3z3zuNVUr0iDzg7foebDOtC8bijJGUGdW607nA9WY_zWnXxlaUYTaVe8xBwJpGtWaAdS_UMJlb4QP8kJv7bo5O8Hv2XTLt2-ga0exA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نکات لازم و ضروری برای حضور در مراسم وداع با رهبر شهید انقلاب اسلامی
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/665252" target="_blank">📅 12:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4741c4b552.mp4?token=r2HYhC6KWR7hlGfw4OhER-fB_ZPxXs2kcK7Hj035tqFPTcupun1qDYfGJ7rvRWvkf94JcgOruex_dfV1WpUQZMjpXknu45N-FRPy-pVLqI1XwPOWBnctKi0o89DiytREP9-mgp81_SeacgPTc-gVmpHcHkE3j-deEbawmxiwg1RJt13zUE4kVDsa99DwP_tkZmSgC3KV58uYiD93ydc93ur3E6z1mubkyg7X2h6smWkhnUzxc726iuk23pvPER665PH38Wc1qOGJb_HQHhkL7_ceOEpqKQyQqLCrDlJtC9AhgrOKBA4jaoRrBUSJwI7LTt2xYgdWaWMY-erOMdm2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4741c4b552.mp4?token=r2HYhC6KWR7hlGfw4OhER-fB_ZPxXs2kcK7Hj035tqFPTcupun1qDYfGJ7rvRWvkf94JcgOruex_dfV1WpUQZMjpXknu45N-FRPy-pVLqI1XwPOWBnctKi0o89DiytREP9-mgp81_SeacgPTc-gVmpHcHkE3j-deEbawmxiwg1RJt13zUE4kVDsa99DwP_tkZmSgC3KV58uYiD93ydc93ur3E6z1mubkyg7X2h6smWkhnUzxc726iuk23pvPER665PH38Wc1qOGJb_HQHhkL7_ceOEpqKQyQqLCrDlJtC9AhgrOKBA4jaoRrBUSJwI7LTt2xYgdWaWMY-erOMdm2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دونات فوق‌العاده خوشمزه و سالم چون نیاز به سرخ شدن تو روغن نداره
🍩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/665249" target="_blank">📅 12:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNq0vhrIbMDyc9sMagWPpklNZJLsWucmUbZo6Q8xthK0lXKbABADTtoVF5xVsNmd_dy7yn7Hjds2OW4MbXnCEayD2pUJGteFf4fkrsiHsaxfLcUE3nnlvwLz76qWThUq7Q5e_qsPn2-LrMobMqwCpzOYXt97lTSd7EsCnoZfNHPgjRvWnYcxKlrK24O4FIn5D_ZVH_shuD69AhbwgKSgN3pCts3s615FE3oX7qm9s9lUBZrOhKV7YISh_Ex6VUF_bEFJOFiAHVLL771gMOixpvBm9eBu9Cp1FWd0CpJUDWtI0I1j76_fd783gGAxThV1twFdXyyfNgQn89GbfQHhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
میزبانی از زائران مراسم تشییع رهبر شهید
🖤
#تهران
#مشهد
#قم
🔹
اگر در تهران،مشهد و قم امکان اسکان دارید، با میزبانی از عزاداران و زائرانی که از نقاط مختلف کشور برای حضور در این مراسم در حال سفر هستند، در این حرکت مردمی سهیم شوید.
🔸
از خانه و آپارتمان گرفته تا حسینیه، مسجد، سالن یا هر فضای مناسب دیگر، می‌تواند چند روز مأمن آرامش مهمانان این مسیر باشد.
🖤
برای ثبت محل اسکان:
👇
🔗
https://mahame.ir/s/gsA5HY
✅
یا عدد 40 را به سرشماره 3000143030 ارسال نمایید.
ماهمه، برای ساخت ایران
🌱
🌐
www.mahame.ir</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/665248" target="_blank">📅 12:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBAmp_p-sV9AhPKmGZhdqVkJm_SrqGRgQZSOGOsTUXJbYCptvcxJK-jCGdhzSmQon7UYnOCMuAmAYXzBJ6JqbrgbxV3r6iN2E-t5PfU_Q8F_r5LbMdwx9hmYT1wt-4Ti9lVcDIpZwWau7qTMqMwwhElHuhAuM1owQ-lA8RTDO4OPL31XFAh89bbeBlKneMvSLJDBbCd77_jJiSeVuBafCgAsvUz6raLqsoaRSXzn9XGkLTUGTcSmhFfS1ddBTgKzecT9-hptRqpxgX-EKcLSvOzDCjtu3Qoa6QsH20EopI7ryJ0PPzDucyKZEHE0QctU1IUNjNAtMZBIMmFPdYTxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با جهش ۶۰ هزار واحدی به ۵ میلیون و ۱۸۷ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/665247" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3b6141bd.mp4?token=nLWco570VMbzoFGkgir0d1DX5tEs170x9agfBWgqA1NLmUk7txzZRMhbkv6bZSG1nunPcHDyt8l0txbWvXq7i43NVuTeBrHlI6C-IA1exKy0OURvdBuazahw4TfbfGIFboZ8jMnM1aovfJO1S2UiTKn0r7tTcb06z49WlgDr4OiU35NJL551oN_LBGuZSoC8TaZRr07Xq90pcvR8n-TTFu_qeaPWbOmMNmCugyg4FUjKhhOD6O_10CSZHg-hdSNhwk25aWgpIzJz7Pn4DM2AXPLCrdvDQgzvXFehmKQsMzhzZnkdkLFiKZljWeJrcL5oUPK6NzwlfuxTDbfh8gGtSzFOOxBEG_9LVSFTcYxBgwbx6cyfLPBkQFS4ThJy20hBV5vP1g1Gik8cAbgA3_6ZU3bwnXyaJKkclhyIN9PFlRo8PwkVOR1_fPRtvugjNpS3Mg8wlLFv-6JyTTj8E95PLcRqbR5QZixhCs3bqhgrkf_3bPcOeYckKt-9ZtkyAnLayhxxJF8T0zf_WqpxBcOI95zOdKb8ltSY9DAEPZIq5Z_zp-F7GptjDDCOe1ZgHXE6xAvo3K8UtG336SZyv8Wmm7Mz13cVhnWwFS1nrWico0dAg2yaL0CJCQFDQzFx9XndGqLI488f7aoqA2A5EZk-oWfrQTKS2BtTbFZVmBtZVlo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3b6141bd.mp4?token=nLWco570VMbzoFGkgir0d1DX5tEs170x9agfBWgqA1NLmUk7txzZRMhbkv6bZSG1nunPcHDyt8l0txbWvXq7i43NVuTeBrHlI6C-IA1exKy0OURvdBuazahw4TfbfGIFboZ8jMnM1aovfJO1S2UiTKn0r7tTcb06z49WlgDr4OiU35NJL551oN_LBGuZSoC8TaZRr07Xq90pcvR8n-TTFu_qeaPWbOmMNmCugyg4FUjKhhOD6O_10CSZHg-hdSNhwk25aWgpIzJz7Pn4DM2AXPLCrdvDQgzvXFehmKQsMzhzZnkdkLFiKZljWeJrcL5oUPK6NzwlfuxTDbfh8gGtSzFOOxBEG_9LVSFTcYxBgwbx6cyfLPBkQFS4ThJy20hBV5vP1g1Gik8cAbgA3_6ZU3bwnXyaJKkclhyIN9PFlRo8PwkVOR1_fPRtvugjNpS3Mg8wlLFv-6JyTTj8E95PLcRqbR5QZixhCs3bqhgrkf_3bPcOeYckKt-9ZtkyAnLayhxxJF8T0zf_WqpxBcOI95zOdKb8ltSY9DAEPZIq5Z_zp-F7GptjDDCOe1ZgHXE6xAvo3K8UtG336SZyv8Wmm7Mz13cVhnWwFS1nrWico0dAg2yaL0CJCQFDQzFx9XndGqLI488f7aoqA2A5EZk-oWfrQTKS2BtTbFZVmBtZVlo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاوه‌گویی‌های سوشا مکانی، دروازه‌بان سابق تیم ملی، صدای مجری و تحلیلگر صدای آمریکا را هم درآورد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/665245" target="_blank">📅 12:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61525dee8.mp4?token=gDstB7C4IMtQo-MzWRgWVCHYNmL3_oylTma8LVqOG_sKDPEZBBfFjBp9-0Ce4D4JIRWAbRgrWqh8QwT5-vhxEfQtfCzPa04JXrtEWtvosJHjjRIBlChwneQ-5mWMp_OlBzh3caoX9gNrRcmxkIaaDuvUv801Wg2YHMDsL3cxeQGB_1tcZAujKNi6m1dNVVvRnJtNGKmbP_75prbXBFbTm6k8nZ4QdwiygAoCAzmvu7EwDNfBAPmdAHY8mItb0pJx3AemD6dii8J5yQs5T1yua7i6qn3z2aleGpQRgtIwCmbh8NxiL1-c5DLLzSUKpVm5houMeED-K2-ADelpmEKXOhGlEvV-CqTXH2op-4vhpGkUjN93iD3l31qqM1LqxK_C6i7wTnIAN8BNE_OXJYTnOz9T4dUuokC72jFO3_BIQCrhpQK3tG_HolS5hidl2LRiral8P9IcW8oOiTMchzGLITXy26O1GIo_-9rdcu8EoUPIXlEK_TUm-7qkpxAj3iu-HqvH2Zzjoj4Vwz7cpF0tm0lZozkj_H8mrSncDvN148Xci-uVFHMh_f2y3TEOHFyPUEWnaNbxmvf1GcLBb1g2bnpTi9QKTjZO563_RsIAlCeSz-g8KN3lHkpVx_A2yRtaG0unAIPc_bH_CEhLcRRI_kO5TeczW_p-onrZTGumFsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61525dee8.mp4?token=gDstB7C4IMtQo-MzWRgWVCHYNmL3_oylTma8LVqOG_sKDPEZBBfFjBp9-0Ce4D4JIRWAbRgrWqh8QwT5-vhxEfQtfCzPa04JXrtEWtvosJHjjRIBlChwneQ-5mWMp_OlBzh3caoX9gNrRcmxkIaaDuvUv801Wg2YHMDsL3cxeQGB_1tcZAujKNi6m1dNVVvRnJtNGKmbP_75prbXBFbTm6k8nZ4QdwiygAoCAzmvu7EwDNfBAPmdAHY8mItb0pJx3AemD6dii8J5yQs5T1yua7i6qn3z2aleGpQRgtIwCmbh8NxiL1-c5DLLzSUKpVm5houMeED-K2-ADelpmEKXOhGlEvV-CqTXH2op-4vhpGkUjN93iD3l31qqM1LqxK_C6i7wTnIAN8BNE_OXJYTnOz9T4dUuokC72jFO3_BIQCrhpQK3tG_HolS5hidl2LRiral8P9IcW8oOiTMchzGLITXy26O1GIo_-9rdcu8EoUPIXlEK_TUm-7qkpxAj3iu-HqvH2Zzjoj4Vwz7cpF0tm0lZozkj_H8mrSncDvN148Xci-uVFHMh_f2y3TEOHFyPUEWnaNbxmvf1GcLBb1g2bnpTi9QKTjZO563_RsIAlCeSz-g8KN3lHkpVx_A2yRtaG0unAIPc_bH_CEhLcRRI_kO5TeczW_p-onrZTGumFsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش خیره‌کننده ۲۰۰۰ پهپاد در آسمان هنگ‌کنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/665244" target="_blank">📅 12:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac3fe55de.mp4?token=rIDLskD-edinw_bkjcokIVXIWhuql3WrSNzgyKzgtRHuEtk-R9cT8TuGMGvLB3UcidpTfdQcBQK2bERRLmG-TW-VDFkc6ME1ETusR2PMjrtb22IrbuuZJjLlmVo4AIgpM1dS7VyADYsxmLk4rg55oizC9bIchSj0_3s05vw9NypADW4mK1OcB8yWB8oUafGNp3xfz0lrglyuB8PO1O7JF-4jWE_KrBau0YDszTW1UjD76oHjwjcPSaYZ6btCt4TI-0aiF7zGKIUdWTAMj6RewnuOQOdRBt_MfvRdTBEJUkehLJCsO8S5jF1xDAX0yfSAO7fpgjacDUaM3DypBOJ5whgl0sKiU6tIIsUQ0Z5zCUTyaI4j-l-EhphEVbFXu6mecOzKLzD8Tpm7dIZiCqSj0jX2dDicDhahpbvjCu1lQ6F1Z5cxlpLgZLF4TLyfI4GsSBXNmkKXCQG88k6vOJ07Wx08_e4pkbRkFZIv2hEZ55_9SHujrWhsGcQmUJ41gh6locvp3KQeF9P1YcRH6Li56aH2nqBMYVheqTWL-uKM7umoldtddGQrYxzJgaRTws8UlHXvJhtOws2Xsy88gvgaMtamD1D6dkSRiJgATAjRFqpBDfVM0CevtMqNbksQKEVyyIF13Ge5xVD7rkdu6YvDQC5lXB72GG0WwavR2qu9PBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac3fe55de.mp4?token=rIDLskD-edinw_bkjcokIVXIWhuql3WrSNzgyKzgtRHuEtk-R9cT8TuGMGvLB3UcidpTfdQcBQK2bERRLmG-TW-VDFkc6ME1ETusR2PMjrtb22IrbuuZJjLlmVo4AIgpM1dS7VyADYsxmLk4rg55oizC9bIchSj0_3s05vw9NypADW4mK1OcB8yWB8oUafGNp3xfz0lrglyuB8PO1O7JF-4jWE_KrBau0YDszTW1UjD76oHjwjcPSaYZ6btCt4TI-0aiF7zGKIUdWTAMj6RewnuOQOdRBt_MfvRdTBEJUkehLJCsO8S5jF1xDAX0yfSAO7fpgjacDUaM3DypBOJ5whgl0sKiU6tIIsUQ0Z5zCUTyaI4j-l-EhphEVbFXu6mecOzKLzD8Tpm7dIZiCqSj0jX2dDicDhahpbvjCu1lQ6F1Z5cxlpLgZLF4TLyfI4GsSBXNmkKXCQG88k6vOJ07Wx08_e4pkbRkFZIv2hEZ55_9SHujrWhsGcQmUJ41gh6locvp3KQeF9P1YcRH6Li56aH2nqBMYVheqTWL-uKM7umoldtddGQrYxzJgaRTws8UlHXvJhtOws2Xsy88gvgaMtamD1D6dkSRiJgATAjRFqpBDfVM0CevtMqNbksQKEVyyIF13Ge5xVD7rkdu6YvDQC5lXB72GG0WwavR2qu9PBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام کاشانی: اسلام دنبال چشم‌و‌گوش بسته قبول‌کردن افراد نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/665243" target="_blank">📅 12:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9UldgaY8suXF12Y9WT-KQtfl3IjxIJNrhr-jK3qewuuapjwly5CUXsAgo-SzyuogzjKHtCIsoCBHV_lPKSKpq0zZLu3JeG0dAeQhwsQLVR2vYzny1-TfIdxXuGEE25DHl5oe_Ce52ZyJk4KwfZP0AFdYaGgtH6EWoQRwmkbcegY4aC1w8WsPUR-3qAGijuD6KhdaDNCqE-tPCQ5Oh5EZufn6rxDK_JRtas8Buis5uoQpXfLYuRBcykRqaHxvul4dZFgWeLwqi6znIPNKiU-zzW_vS_kBUKvMiaPUsIX8p_5fD3zWkwbV1OigRQZdQ7N4TbxPMipFueJ7cU27jyXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹۰٪ آدم‌ها سؤال اشتباه می‌پرسند؛ برای همین به جواب درست نمی‌رسند! می‌خواهید موفق‌تر باشید؟ از یادگیری این مهارت شروع کنید. #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/665242" target="_blank">📅 12:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5bd20ec96.mp4?token=JC24NPPiT6-wu_8SVxHgodEt-MXbAwTuhh-XsCOODa6EddOYJKc4L8YondxouOTFbK2RSF4sE7IJ2wRyqbJuy27KaBgV84QozxcQgEyRgSGg84hAiYGEn72rMlt_zCkKxeBqzhhZjYR7_6QmXstcgGR4TN0EWSS6f45LAKeiryojI4vuz1eYN5hfgIULSUENuoEPIh8SzpZGTakFu50tTvJ9exJU2CiEmVwK_37824fkyA8fz7SXirxFTfbD5yD_Zq9SL-IRlmvwcwYRfgxUZAVaoADzXJ_8pk2RCKv-dvjgQf_bqHY2wgoLP8BocerW84M06e1ywNTmBg0mmxM0znNiRiaWHnT-hmygB4Y3MZPxgvzx7ygsZ3CcUC_sG1AApY_SguyjXKeSwMntlNL0tyjyMbvsTS4gB_LuOsPE3-l_7V2g016vOwl4BW5VLqCkaeqj9HGixPnX478SFKQwWIywZrLYxGTGnxwowuhPsQKooOmVuERndkGluBxRnOrskuLmoKSLB3x9zfujKP6CCQg4JE4HxQSPFF51Tkj3MGkjY7rL26sDmaNHbfanMiNbwK-h412QfoeO3ZNhv-uW_uYoeTNHzkZu6OdFuPIl3TKpewDZxKB1OXVxjDM4ZUFoK-_RSALGW3FU6eivqlDfqQHKtL4thsFQWylAg4NPSQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5bd20ec96.mp4?token=JC24NPPiT6-wu_8SVxHgodEt-MXbAwTuhh-XsCOODa6EddOYJKc4L8YondxouOTFbK2RSF4sE7IJ2wRyqbJuy27KaBgV84QozxcQgEyRgSGg84hAiYGEn72rMlt_zCkKxeBqzhhZjYR7_6QmXstcgGR4TN0EWSS6f45LAKeiryojI4vuz1eYN5hfgIULSUENuoEPIh8SzpZGTakFu50tTvJ9exJU2CiEmVwK_37824fkyA8fz7SXirxFTfbD5yD_Zq9SL-IRlmvwcwYRfgxUZAVaoADzXJ_8pk2RCKv-dvjgQf_bqHY2wgoLP8BocerW84M06e1ywNTmBg0mmxM0znNiRiaWHnT-hmygB4Y3MZPxgvzx7ygsZ3CcUC_sG1AApY_SguyjXKeSwMntlNL0tyjyMbvsTS4gB_LuOsPE3-l_7V2g016vOwl4BW5VLqCkaeqj9HGixPnX478SFKQwWIywZrLYxGTGnxwowuhPsQKooOmVuERndkGluBxRnOrskuLmoKSLB3x9zfujKP6CCQg4JE4HxQSPFF51Tkj3MGkjY7rL26sDmaNHbfanMiNbwK-h412QfoeO3ZNhv-uW_uYoeTNHzkZu6OdFuPIl3TKpewDZxKB1OXVxjDM4ZUFoK-_RSALGW3FU6eivqlDfqQHKtL4thsFQWylAg4NPSQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامپیوتر در سال ۱۹۹۴؛ فرکانس پردازنده: ۶۶ مگاهرتز
🖥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/665241" target="_blank">📅 12:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4ZtS8KkO1huLCSVTmoCN0FBnCGYs8DZV2PmtCZY-ngQuQRF1EbImvKte2R607_1WWTPf9Sp0UymrNMbtfFF6p93GcEnzCcByuYE-oHFvgXcjVZzVspQrj1QOX38gwTjEN-6Nx05tsdxfUPiRqh7Aoy370rjW_QGEXc-JkFGiZv0Lg2-Lm7qGDS163ap8VNrIE_JclFHQ_swq15jWWbwMFDsvF634vzt6rtjgBBWmCNI6sSNQWNKky1xdLYWCTIc-2hQuFiAJI5VkyKbydVsvQzVrgD5xp7qp1F6M-ovcV6Eo4WuXn96n4h9if17BgHoRzwcipT4dvkNxQQs32Vy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازخوانی بندهای کلیدی بیانیه الجزایر (۱۹۸۱)
🔹
در توافق‌نامه الجزایر، ایران متعهد به آزادی فوری گروگان‌ها شد و در مقابل، ایالات متحده لغو تحریم‌ها، آزادسازی دارایی‌های مسدودشده و عدم دخالت در امور داخلی ایران را پذیرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/665240" target="_blank">📅 12:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665239">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpQZsmksF3_an5OWKsZHU3zLzkEnlAHNhMFK8Am2mnKmkkwrY_wSpQqJ59HT6hgbVhkOOfVel2ktRiR_uWm_1pPe7LK8S1c2xc1lpJlZIqQswk5VPF_YAG0m1a9PXQd8baXILBbqzz62X6aVBfbeNFtxljPguoRDNO7gm4OyrAInhmyXLamNjTphGqjqQ3IYtORJDl-mg8OAIEBDHrCVs7BU9BEMQxtuZpWzkhZ9M7fgFYVnkit4s5YLPyasxCG8PhwNf_9ksxW_cX4p0m1cH7o2eFKARMsJxKqSi3qKZ6DEnpWnaIv_tyo-0_tH1BP171Pph5rMFaSX7PMBLD3KhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی عضو تیم مذاکره کننده: ایران به سرعت درحال بازسازی زیر ساخت‌های غیر نظامی خود است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665239" target="_blank">📅 12:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665237">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36c3ef379.mp4?token=t3rxc1q9-uBNjCozcmYFiDWZVDVNav_7qFKaHWSsthHsPBKVsbkn2zQeFms0qWH6USxFWCtebXXmuXu0ZfluBmfugdtv-HmvTsjEXIUvrE8jL0y9PYj58rySpU_fcaEaaBrP8fA9Fz3NTcmfBUh6rUzkruhehpAB0ozAoRgyOd5YwpoUHbdBLBVw7eI8LzESCOjZV4uSMvlDxK2zOcSi-Pw_atSGC87BYpSvhOAFBmPLjo4AhE0vaJBlbpb5WcdD7ZcGpVkZXNLGYNwaVmKQhseCYGdCPQGYOdAJl-o3FV1QBetEoBgJ5r8bqRyKmH-wX0wzLl4xDA9E5KMlTzGJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36c3ef379.mp4?token=t3rxc1q9-uBNjCozcmYFiDWZVDVNav_7qFKaHWSsthHsPBKVsbkn2zQeFms0qWH6USxFWCtebXXmuXu0ZfluBmfugdtv-HmvTsjEXIUvrE8jL0y9PYj58rySpU_fcaEaaBrP8fA9Fz3NTcmfBUh6rUzkruhehpAB0ozAoRgyOd5YwpoUHbdBLBVw7eI8LzESCOjZV4uSMvlDxK2zOcSi-Pw_atSGC87BYpSvhOAFBmPLjo4AhE0vaJBlbpb5WcdD7ZcGpVkZXNLGYNwaVmKQhseCYGdCPQGYOdAJl-o3FV1QBetEoBgJ5r8bqRyKmH-wX0wzLl4xDA9E5KMlTzGJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداها رفتند، خاطره‌ها ماندند؛ بیشتر صداهای خاطره‌ساز دیگر میان ما نیستند
🥺
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665237" target="_blank">📅 12:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f151079d27.mp4?token=Z47rbIiRxvn4dhtPx3yUq_iYrBmX0Kk5Tmdrd7rqBexNZevITmj772WgdI9MzjYZsYaGuIFVP--oPYSbR3_oCUaVtJBNWZf5HTcOb3ZH1A9t9i3bVx8ifrjqUGdJLdi_ruuIjI7EQb_rZhFCDekrBTn6vphsF83Lni0rWTuPxh9ByvNHamSSCZZqmO5XI2YMGyK6OFttOLjzp7NQenr5i_B1s7ipoWAZHN4aWGhchuyjEykZjsT6jYZ7kBpzyScGcRPL5_vN5GDvPkCbBHmo0O2NUPhZrCj1diaC2YWiyWYM-E_xO5Kh_UX4K-99g5ayyvidG2GHu57IN2CZSBCauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f151079d27.mp4?token=Z47rbIiRxvn4dhtPx3yUq_iYrBmX0Kk5Tmdrd7rqBexNZevITmj772WgdI9MzjYZsYaGuIFVP--oPYSbR3_oCUaVtJBNWZf5HTcOb3ZH1A9t9i3bVx8ifrjqUGdJLdi_ruuIjI7EQb_rZhFCDekrBTn6vphsF83Lni0rWTuPxh9ByvNHamSSCZZqmO5XI2YMGyK6OFttOLjzp7NQenr5i_B1s7ipoWAZHN4aWGhchuyjEykZjsT6jYZ7kBpzyScGcRPL5_vN5GDvPkCbBHmo0O2NUPhZrCj1diaC2YWiyWYM-E_xO5Kh_UX4K-99g5ayyvidG2GHu57IN2CZSBCauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی حرم حضرت معصومه (س) برای آخرین حضور رهبر شهید انقلاب در شهر قم
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/665235" target="_blank">📅 12:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d45a19551.mp4?token=soGIj4xZh1dVYVhqsazTbGkvRG8kCuXfIJ7dJMcya0JLAsPyCWY_ETZDG-n4PTI39StOvnBk7QuHrucXQ7DJf2l2r87wzJPkpsSfBZxdomOB6ovSIDKQBIdSl4Krlv2C8d_Kh2TnGxSaFtXTOwmWmOI2fbylJ9-fDKECgA6Kep1YU3jPUQ_UCsl3HbuYM3wxsxndPM_QVPL2HCgmAcIeHUKfV_sJONSRFN_n6SxpMmWQAeUy5kcKhmUfEQZ4qSh6hB7xAFnftjA1Z0xCzDI-G2nEhggPPsuz0xz_RzHbLimOsbqVBtC3GbpkL4oMySQ20lN2-JfGMnf9ZKtqQxQcJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d45a19551.mp4?token=soGIj4xZh1dVYVhqsazTbGkvRG8kCuXfIJ7dJMcya0JLAsPyCWY_ETZDG-n4PTI39StOvnBk7QuHrucXQ7DJf2l2r87wzJPkpsSfBZxdomOB6ovSIDKQBIdSl4Krlv2C8d_Kh2TnGxSaFtXTOwmWmOI2fbylJ9-fDKECgA6Kep1YU3jPUQ_UCsl3HbuYM3wxsxndPM_QVPL2HCgmAcIeHUKfV_sJONSRFN_n6SxpMmWQAeUy5kcKhmUfEQZ4qSh6hB7xAFnftjA1Z0xCzDI-G2nEhggPPsuz0xz_RzHbLimOsbqVBtC3GbpkL4oMySQ20lN2-JfGMnf9ZKtqQxQcJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
نسل جدید رنگ‌های دیواری در راه است، تحول صنعت ساختمان‌سازی با رنگ‌های فانتا کروم
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/665234" target="_blank">📅 11:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pApYr7vitQWiEg3-bfA38a2NwIBB90br_FhXkAPe8eRgWZ6O4OdVpv8_ryWjqzkSU8BIA6Z3N_FtgppgZYgt-Rnn4157wyC4EWcHIddhirSycX7EIKmJCOX0rxJrjmHgMHXVer5N5uIBoon6C5qdf3ZiPeu8OeRA2Lfu52UqeEp_qLw6YlIH7shwBverbBYmjMFauOyC7SnEqvL-qsrn4AMAGpCaJ4xk1DTBfVdif2r5HlCMaNtYWR1zROcPXeNFXhnyt7WMoqQUI03BVt326mSSwD0RjvYqd6RmzPBZ-nDBtg4U1ZyP6W5UvkQEpboNUqNSEGnsryaKSuxt-pn55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: پرونده انتقام خون‌پاک خامنه‌ای کبیر و شهدای مظلوم ایران باز است وآمرین و عاملین این جنایت به سزایشان خواهند رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/665233" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoZ-7_ZinXu72irNtReeRRRvSJvCmOnWIgJNMA9LAR3V--lVs_rOliHkXEuEUlP-iXWNPSJSpxZPAURtEdf8MYEitsTg5jhbHnd4FxdsHjI82aFJWyaFDxhoyMQBBBVipiPHb4j1YV6-r3nTWzGhwdq5ZZKzBBQksi_5agD_UMrXuBeJqVoyASzPld0RorwlRQ_9ugxRFy1o9HocF2IwAyrbKxcOKCAkW8RbfrDDmZIOVAiV7nZs6_K-Sh5NCDBqjhSxS4LNOZyAFdX9k8X2nHirdtXGiIL-EvbJBSRRGw3esCM-c7CaFsbOhCuJaOMOzZSkAJo7p96PdD6Z1GLWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران در دو هفته ۴۰ میلیون بشکه نفت فروخت
سی‌ان‌بی‌سی:
🔹
ایران از زمان لغو محاصره دریایی توسط آمریکا در دو هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است. تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد.
🔹
ایران موافقت کرده که به کشتی‌ها اجازه دهد به مدت ۶۰ روز بدون عوارض از تنگه هرمز عبور کنند، اما اعلام کرد که کنترل اداره این آبراه را حفظ خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/665232" target="_blank">📅 11:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
واکنش قاسمیان به مقایسه مذاکره با صلح حدیبیه: اول واشنگتن را بگیرید، بعد از بخشش ابوسفیان حرف بزنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/665231" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665230">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv3xldZlyXJluv0aC7m9xk3Qu4GykcN_Wen_Torer2uLg8pOSumI5RTHiMllL2sgtq2vy5d4VPEh4uRpG9-3WCk84FYde8vg05btrJNoVFTX1yOl1TTjbc8wW21cicUjIK2htlGGR9nxrXHdFzM28PmXw6yE1m06SnK7KW_exd5zxdI8xOnX9ZTPm0IRAF5Nhkrs2GRgMGcJMHEClxUAYDUrm7rfUz-iXQNykS35u6FAGEei7Ys1267fKn89r2s66uXRqUXHI0ri2kBzxnTOIeM69pobNykVuwEHHP8rp_CPAnSIOl3jS1U023SzvynCvGLiPhQtEhfEr7lh92_Xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت بهشتی کوهستان گرین نهاوند در تابستان
#ایران_زیبا
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665230" target="_blank">📅 11:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665229">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اختصاص قطارهای شهری و حومه‌ای برای مراسم تشییع رهبر شهید
مدیرعامل راه‌آهن:
🔹
قطارهای عادی و فوق‌العاده در مسیرهای تهران، قم و مشهد برای مراسم تشییع و عزاداری رهبر شهید ایران اختصاص یافته‌اند.
🔹
قطارهای فوق‌العاده به مقصد تهران، در روزهای دوشنبه و سه‌شنبه قطارهای فوق‌العاده به مقصد قم و در روزهای سه‌شنبه و چهارشنبه قطارهای فوق‌العاده به مقصد مشهد اعزام خواهند شد.
🔹
همچنین برای بازگشت مسافران نیز از روزهای پنجشنبه، جمعه، شنبه و یکشنبه قطارهای فوق‌العاده در نظر گرفته شده است.
🔹
فروش اینترنتی ظرفیت باقی‌مانده قطارها از ساعت ۱۴ امروز آغاز می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/665229" target="_blank">📅 11:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665228">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF_9pw5OBEazomwlAbNdNsK9BmwBXYqJ04-skh_RJnppabA1iDn0-s8L1Gsdm6NvESfR6v3K3NEFRMlAb1BfYIpFsl98jkogydYn9qgMtWHwqrYQGE28Wl7mc4NT7yaPhl7gK3xG0rwQ2h6cdVFVtBKK5Kwako7QTVIYcCv6OPfyx2KXVBLhUJFPGTUgjAvzJbLQe1VYBjLfs6C_1D4fwKbDRTqAcSLQNoP0ZSrSTUaoehKFnvQ6tjGCVePrez0Kvv4GD5FYXYt-1-mWl7-bREyZ7IFiirnmTlJ2XfK9UZLpsrWAGOqnWL1rfCjU2aVeBVHYvxdf7RooPYIUVgkKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا پایان سال خودرو چقدر گران‌تر می‌شود؟ پیش‌بینی بازار خودرو تا پایان سال
بر اساس یک سناریوی تحلیلی مبتنی بر شرایط فعلی اقتصاد ایران، روند تورم، وضعیت نقدینگی، کسری بودجه، رشد هزینه‌های تولید و چشم‌انداز بازار خودرو، احتمال وقوع سناریوهای زیر تا پایان سال ۱۴۰۵ برآورد می‌شود:
🔹
افزایش ۱۵ تا ۲۵ درصدی قیمت خودرو: ۱۰٪ احتمال
🔹
افزایش ۴۰ تا ۶۰ درصدی: ۵۵٪ احتمال
🔹
افزایش ۶۰ تا ۹۰ درصدی: ۲۵٪ احتمال
🔹
افزایش بیش از ۹۰ درصدی: ۱۰٪ احتمال
این اعداد چه می‌گویند؟
🔹
حدود ۹۰ درصد احتمال وجود دارد که قیمت خودرو تا پایان سال بیش از ۴۰ درصد نسبت به امروز افزایش پیدا کند.
🔹
محتمل‌ترین سناریو، رشد حدود ۴۰ تا ۶۰ درصدی قیمت‌هاست؛ یعنی اگر این سناریو محقق شود، قیمت خودروهای بازار در اسفندماه می‌تواند به طور متوسط حدود ۵۰ درصد بالاتر از امروز باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/665228" target="_blank">📅 11:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
🔹
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌‌کشی و با پارچه پوشیده شده است.
🔹
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ از این‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد. احتمال دارد پیکر مطهر رهبر شهید در رواق دارالمرحمه یا یکی از رواق‌‌های حرم مطهر رضوی آرام گیرد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/665227" target="_blank">📅 11:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6483a8f64e.mp4?token=vt9kITRHg3GfnqV8X0pA06qrs8n8D6wV9uzxKhONGg5y0qfoGvQ52fUbtArImsctaX1uHdsGPZw6ZkFYOPrZQB2-Auc_OCQwwbKTU579WQEWKXjCB_MBvhAVtqp9i0X2_kW2Egr-iPXKmZHWI2QjBoAm2niJCoZWbGaWIYKWj7gLleOnFtj5GPUaaFbHQczS7Y8jM8OIhUsc8Hf1gpiFZ7L0yJmOX1rB3owFZnNXG3q8avs5UIbQWHIi4Avt-W7JHefa_74klVjA_FrJtEM-z5DqlZ8mtN1Ea9P9yfP2nNzFk3ya6E6r56mo6DR7fx_WYH3PvK4KSD0MgSCKRXWpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6483a8f64e.mp4?token=vt9kITRHg3GfnqV8X0pA06qrs8n8D6wV9uzxKhONGg5y0qfoGvQ52fUbtArImsctaX1uHdsGPZw6ZkFYOPrZQB2-Auc_OCQwwbKTU579WQEWKXjCB_MBvhAVtqp9i0X2_kW2Egr-iPXKmZHWI2QjBoAm2niJCoZWbGaWIYKWj7gLleOnFtj5GPUaaFbHQczS7Y8jM8OIhUsc8Hf1gpiFZ7L0yJmOX1rB3owFZnNXG3q8avs5UIbQWHIi4Avt-W7JHefa_74klVjA_FrJtEM-z5DqlZ8mtN1Ea9P9yfP2nNzFk3ya6E6r56mo6DR7fx_WYH3PvK4KSD0MgSCKRXWpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی سفیر آمریکا در اسرائیل: بدون یهودیان، آمریکا هرگز شکل نمی‌گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665226" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🏆
پیروزی کوبنده فرانسه برابر سوئد با درخشش زوج طلایی کیلیان - اولیسه
🇫🇷
3️⃣
🏆
0️⃣
🇸🇪
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/665225" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید   رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/665224" target="_blank">📅 11:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8b453312.mp4?token=J3o7tOJMAwPW_CQhT79DmrYKmSRJjnNwtx7uHS_7c0M9qGETcnzpaiPVFPnDWDXEFnYQJhrtymjSbAZJgC5gzY8yPi5_7Rds7CpU6enbyJ8mE3Uqz13H9NkyD2Bhlkk364-BL7ePbNFRGI-5I4wIuZDxBOxqsqMMVWxaECOlpy0PoClp3nuhovvEtM4NoaVTKsjObPQYFl42BmT16dpmXFxU-TQ6AshoG2MPAxbnF_FNySCoBYQiY4ELs32zj5IrV78SeeV2htVBw_lDd60Bx722RKgal94V5B4FOqxQrU96rOmsPkBIeCQwr8iXSqxWeuph-jgpsBBulzFATLOqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8b453312.mp4?token=J3o7tOJMAwPW_CQhT79DmrYKmSRJjnNwtx7uHS_7c0M9qGETcnzpaiPVFPnDWDXEFnYQJhrtymjSbAZJgC5gzY8yPi5_7Rds7CpU6enbyJ8mE3Uqz13H9NkyD2Bhlkk364-BL7ePbNFRGI-5I4wIuZDxBOxqsqMMVWxaECOlpy0PoClp3nuhovvEtM4NoaVTKsjObPQYFl42BmT16dpmXFxU-TQ6AshoG2MPAxbnF_FNySCoBYQiY4ELs32zj5IrV78SeeV2htVBw_lDd60Bx722RKgal94V5B4FOqxQrU96rOmsPkBIeCQwr8iXSqxWeuph-jgpsBBulzFATLOqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شدیدترین سیل در پایتخت سه میلیونی غنا، آکرا
🔹
گزارش‌هایی از کشته‌شدگان و تعداد زیادی مفقودالاثر منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665221" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYsuwpNGZE0HPSHbfe48OPEi_ApVG471fPJqu5jzGrL4y-2OEdrY803OfrTTSDtzPN7tGtkMWUT_uFXbf9L5IlMyOEF75OKa7DP18h_zw8KPyqSbz7m1QLV4TAcP7ALSR613hZ0BuTSj_Y1qoO9r-WK3RVP86wEdx3xuSsbaTXz4Ca12c9kMigHincgJiYhiYdE8ptriDadsZxhN0XyRBXGlkWNFHA5IACSVmZ3NmG86wgPHXMpY8lZ5FJ0nsdTWMK69MCv6mbcy3mrX-7MXWBPffpstvqCzLSKiBa42vKE49qexibTMa6TmF-rgCqreSjBQbIn4tGCg10KrxMZ4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوهی عظیم از دوچرخه‌های رها شده و شکسته در چین!
‌‌‎‌‎‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665220" target="_blank">📅 10:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
حضور مقامات و سران ۴۰ کشور در مراسم وداع و تشییع رهبر شهید انقلاب
سخنگوی مراسم وداع و تشییع رهبر شهید انقلاب:
🔹
در مراسم وداع و تشییع، علاوه بر حضور گسترده مردم، شخصیت‌های سیاسی، فرهنگی، علمی، دینی، دانشگاهی و نخبگان از اقصی نقاط جهان نیز برای ادای احترام به پیکر مطهر رهبر شهید انقلاب در تهران حضور خواهند داشت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/665219" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzF3oqXrvhvupdlgOYL-DuOCljJVcn3JLlDJD7zTGmJf4Tmy-pETQvOBcQwsfaz54OcZCiSwZC6FMdrxhyGxenUa0Fd9X_dUbrjyD-IKzEAC0lKZ3lMq-2Cns3h_LR7LX42lw9DqO-RbokFl8fD70Cd9vQgrrvygKx054o0IHRMCtXJcyWLlVMb_jVmJMaWtWiYYF4vBwm75tk0qg73t0uFau8JijLgUhEQ4EaRi3NpHcI1iZF_oOWK1d8uzRKfNa9BgRf0dS7r-sE-GU4iFVs132EM8Inb6nJSEMOUtU18jmsjiaFqcnfGyMoAggoeTSww7lpLGvho2_AHqpE6vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرجمعیت‌ترین تشییع جنازه تاریخ کدوم بوده؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/665218" target="_blank">📅 10:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665217">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
جزئیات تعطیلی فرودگاه‌های کشور در ایام مراسم تشییع رهبر شهید انقلاب
رئیس سازمان هواپیمایی کشوری:
🔹
فرودگاه مهرآباد روز جمعه تعطیل است و تنها پروازهای دیپلماتیک و سیاسی انجام می‌شود. فرودگاه امام خمینی در این روز طبق روال عادی فعالیت خواهد کرد.
🔹
دوشنبه آینده آسمان تهران و فضای هوایی فرودگاه‌های مهرآباد و امام خمینی‌ به طور کامل بسته می‌شود و هیچ پروازی انجام نخواهد شد.
🔹
سه‌شنبه فرودگاه مهرآباد به فعالیت عادی بازمی‌گردد، اما فرودگاه امام خمینی به دلیل انتقال پیکر رهبر شهید به عراق همچنان تعطیل خواهد بود.
🔹
هجدهم تیرماه نیز همزمان با مراسم تشییع در مشهد، فضای هوایی این شهر و فرودگاه‌های اقماری آن به طور کامل بسته خواهد شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/665217" target="_blank">📅 10:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید   رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/665214" target="_blank">📅 10:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اعلام محدودیت‌های ترافیکی جاده‌ای برای مراسم تشییع رهبر شهید
رئیس پلیس راه راهور فراجا:
🔹
با توجه به پیش‌بینی افزایش سفرهای برون‌شهری و افزایش حجم تردد وسایل نقلیه همزمان با مراسم تشییع رهبر شهید، محدودیت‌ها و ممنوعیت‌های ترافیکی در محورهای مختلف کشور اجرا می‌شود.
🔹
تردد انواع موتورسیکلت از ساعت ۱۲:۰۰ ظهر روز چهارشنبه ۱۰ تیر ۱۴۰۵ تا ساعت ۰۶:۰۰ روز شنبه ۲۰ تیر ۱۴۰۵ در محورهای کرج-چالوس، هراز، فیروزکوه، تهران-سمنان-مشهد و بالعکس ممنوع است.
🔹
تردد کلیه وسایل نقلیه از ساعت ۱۲:۰۰ روز جمعه ۱۲ تیرماه تا ساعت ۰۷:۰۰ روز دوشنبه ۱۵ تیر ۱۴۰۵ در مسیر (جنوب به شمال) محور کرج-چالوس ممنوع خواهد بود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/665213" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01586d97c0.mp4?token=g2tNQjD2qEhVqH0OYPdJveezdbfAFgMrbOOLE_UD1pT0BxHaSmWhrvyj2kywouXL_PLVSHN9HMM8qZgIkvfDte1sYANYiTfx4JmQ7FmbVDCW8fAhHSdab0lIM14uKLj0r5t-UjACM3xCkbuzcm7BjHM7b5DUibr-0zee2tvPyUz9KJJogBvH_CRGhBafQKJKFOGNVE1mC-8GKlVHi2ywnNaszlPnAO2oaqrkWf3ydSnYd_MUOsHq6E6fD9U_9AWpf-s30CVkjqYe3ziSEXwmrM8tzzs0WHanMA9o1ef_z1vW5192RRwDun00_ea-b1dt28UwjwxJnpI6aCwRebEMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01586d97c0.mp4?token=g2tNQjD2qEhVqH0OYPdJveezdbfAFgMrbOOLE_UD1pT0BxHaSmWhrvyj2kywouXL_PLVSHN9HMM8qZgIkvfDte1sYANYiTfx4JmQ7FmbVDCW8fAhHSdab0lIM14uKLj0r5t-UjACM3xCkbuzcm7BjHM7b5DUibr-0zee2tvPyUz9KJJogBvH_CRGhBafQKJKFOGNVE1mC-8GKlVHi2ywnNaszlPnAO2oaqrkWf3ydSnYd_MUOsHq6E6fD9U_9AWpf-s30CVkjqYe3ziSEXwmrM8tzzs0WHanMA9o1ef_z1vW5192RRwDun00_ea-b1dt28UwjwxJnpI6aCwRebEMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضهٔ شب تاسوعا| قاجار | ۱۲۵ سال پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/665212" target="_blank">📅 10:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665209">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b360968015.mp4?token=dJAz49ggbvXioEFl9c9EVnrHj0W5WWz1Zb3RBRGlsE-XMA4AbUnlMDNL-oQ4tot4FKh61jzmwoD1IY2SZj8jTq9a5Ps5SMN4ZncnZfmN0xqKnBilh-h69MEv06CqTACVP41Ob0EZr8Dv69uZpUlx063a38YBm8SvLS523PfsK_YIuzMVtRMJpjyXBJFOEXQjAYzAVGMWbIpS6f9PLYC1oR6FmfcYSc2sL6UD-GUC_8bIejm7BnK2BAE2BR_BeLSTpHJc0gGDWT-ZhPmaiGzcKNyTs5_1OSx9ykTmN2BWKoc1UMJLbF08ipNStelhyU-pZoBwmuQY55NFxEwSzcUoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b360968015.mp4?token=dJAz49ggbvXioEFl9c9EVnrHj0W5WWz1Zb3RBRGlsE-XMA4AbUnlMDNL-oQ4tot4FKh61jzmwoD1IY2SZj8jTq9a5Ps5SMN4ZncnZfmN0xqKnBilh-h69MEv06CqTACVP41Ob0EZr8Dv69uZpUlx063a38YBm8SvLS523PfsK_YIuzMVtRMJpjyXBJFOEXQjAYzAVGMWbIpS6f9PLYC1oR6FmfcYSc2sL6UD-GUC_8bIejm7BnK2BAE2BR_BeLSTpHJc0gGDWT-ZhPmaiGzcKNyTs5_1OSx9ykTmN2BWKoc1UMJLbF08ipNStelhyU-pZoBwmuQY55NFxEwSzcUoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ ثانیه از قاب‌های که دیگر تکرار نمی‌شوند
فقط چند روز مانده تا وداع...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/665209" target="_blank">📅 09:51 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
