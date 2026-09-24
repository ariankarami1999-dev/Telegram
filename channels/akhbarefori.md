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
<img src="https://cdn4.telesco.pe/file/GzIBTwRN5nn2fclwzFCG9PFzy0nXuAg-OzoitXLlwznnnaGY2HoB-7T1X2kSC4I5_hA2sf-qDr-GJoe6EWZtnIoiEKPX1O2_0ZiuaCuF51pnEyvnUGtj10DKPjvi9PDg4cXswTwCFA_YS1RkdSHJzFqJ0ivpB0HcuHRZU12XuiEsr62pHr4JjgqIEWrrFNL9kLzBYzWk1ZMf5GkiDBATox4DvuDXeYs-caUR4S9zB4SameMFDyRHiZXrWkkDQ2U-vvVjKT9PChJ6LYQgCKPZiW8z_eouCd8c_J9juYBfbEG8sWbjfS_1DfD58-0iWKIlnIZPDgnrCbWCovSHNZOr9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 09:10:22</div>
<hr>

<div class="tg-post" id="msg-692532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
روز پُرمدال کاروان ایران
🥇
🥈
🔹
ورزشکاران ایران در رقابت‌های آسیایی موفق به کسب ۳ مدال طلا و ۴ مدال نقره شدند؛ فاطمه مجلل، کیمیا زارعی و زینب نوروزی و سهیل موسوی طلا گرفتند و سوگند سینکایی، شجاع پناهی، عرفان محرمی و تیم روئینگ چهار نفره زنان به مدال نقره…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/692532" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adcae89f65.mp4?token=lvdH5Em4pXHGGqG1S2zubLMG8mB-SIfN5ur_IZEh2Q-QDtDQvUYu2FYKFReg6U1HDU2i5bStp_vsNQe-_lTBPpnXK0Np6Ekq7LGOzwqGLJPVGqMiA2j_WjgrbucWMsLq2V3dyyD9OTwhODiOXIOGzqzehbiWfcge58pD1S9Epi7NT83SXtL1fXRM33rX-ElfPBw0ZwYUNOanzVR2Hxc45Uv0f6q07GPK20v0Fb3OboT_SVDvc_BJNGlUTm2ig0iZH7-DTRiILU6SAyfyfQQVml_5hzp_ZzKoAgGoD-o5O2d26fVHSD7z12zrrpF_6xr8pQK9wAvNHqAA0YvSZQ1aTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adcae89f65.mp4?token=lvdH5Em4pXHGGqG1S2zubLMG8mB-SIfN5ur_IZEh2Q-QDtDQvUYu2FYKFReg6U1HDU2i5bStp_vsNQe-_lTBPpnXK0Np6Ekq7LGOzwqGLJPVGqMiA2j_WjgrbucWMsLq2V3dyyD9OTwhODiOXIOGzqzehbiWfcge58pD1S9Epi7NT83SXtL1fXRM33rX-ElfPBw0ZwYUNOanzVR2Hxc45Uv0f6q07GPK20v0Fb3OboT_SVDvc_BJNGlUTm2ig0iZH7-DTRiILU6SAyfyfQQVml_5hzp_ZzKoAgGoD-o5O2d26fVHSD7z12zrrpF_6xr8pQK9wAvNHqAA0YvSZQ1aTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر صبح این ۵ حرکت رو در دو ست ۲۰تایی تکرار کن تا یک روز پر انرژی رو شروع کنی
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/692531" target="_blank">📅 09:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای
وال‌استریت ژورنال: چین به ایران قطعات نظامی فرستاد
🔹
چین در جریان جنگ، قطعات مورد استفاده در ساخت پهپاد و موشک‌های بالستیک را به ایران ارسال کرده است؛ این روزنامه همچنین از ارسال ۳۰۰ تن ترکیبات شیمیایی پیش از جنگ و حدود ۱۳۰۰ محموله قطعات دومنظوره در شش ماه نخست ۲۰۲۶ خبر داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/692530" target="_blank">📅 09:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcYqrKK3Ooj5Ead7rUyysB7GlMReJAuxjXdqaEB0wxd4PlHMykiE8rpe1RO29g9_0h9d47XipvsjG5m81jRdc2EE6idzqYZx38aTGZBfYc5uUP4WYwDKyiLiTdcJSj33V79Ffwg5ZyixyoFBkwLF01REw778YVZWfFJFB8XxeHAevT0kSXZQa0-NbJdXI_U0MkasnrqErXOCJXC47wHofE8xh36AQ4UwYduCMph-_cYsARKBglwVD_iOGOhx1_BbWc8KkeY-E-bKMKwZ-NnMAeUp4UDhBlVeFMldy191CJE_82t33p4EWvVa53Zf_e1QYGFY-Gmpuc4ZC_XnnnhLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار کشته‌شدگان دی ماه طبق سخنان ترامپ و وزیر امورخارجه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/692529" target="_blank">📅 08:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ترامپ تصویری منتشر کرد که سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و پولیتیکو را به شکل کیسه‌های زباله در بیرون کاخ سفید نشان می‌دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/692528" target="_blank">📅 08:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f28499e49.mp4?token=JE6DSdKly_4NcGkEePbTnL5vlP1nojIlpY_JlLxaB_S-s_gMwV-gUk41Tb6PmYayOSaze2PzUoMHOqYIKM_EVXXZGiZVRcR50CKBpsC1EwX9HP-fDMoPGxLrY8wWNRfm59Za_OZZudRag_r5oKBX9PLXbwMOZBlw28E5usqcj_-4w_NcTkjjDg42ctFwC0wcex0avvS81VX0COluvNQ2vKdHgITmkoymsNWy9sna1_EOdGTpxfLGOW4BBaRByP29E4nk2HnqOA-IrBV1wKW0xBs6YqNxrwmNsSigqBqRI1LNLUFnfx3azXcqSdZ1joFem-YWQD6ZwqCR3ra71cz0XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f28499e49.mp4?token=JE6DSdKly_4NcGkEePbTnL5vlP1nojIlpY_JlLxaB_S-s_gMwV-gUk41Tb6PmYayOSaze2PzUoMHOqYIKM_EVXXZGiZVRcR50CKBpsC1EwX9HP-fDMoPGxLrY8wWNRfm59Za_OZZudRag_r5oKBX9PLXbwMOZBlw28E5usqcj_-4w_NcTkjjDg42ctFwC0wcex0avvS81VX0COluvNQ2vKdHgITmkoymsNWy9sna1_EOdGTpxfLGOW4BBaRByP29E4nk2HnqOA-IrBV1wKW0xBs6YqNxrwmNsSigqBqRI1LNLUFnfx3azXcqSdZ1joFem-YWQD6ZwqCR3ra71cz0XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاه مکن بهر کسی، اول خودت دوم کسی
🔹
در جریان استقبال ترامپ از همتای چینی در فرودگاه، واکنش رئیس‌جمهور آمریکا به صدای شدید پرواز یک جنگنده حین پخش سرود ملی خبرساز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/akhbarefori/692527" target="_blank">📅 08:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692526">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
الجزیره به نقل از دبیرشورای امنیت ملی:آمریکا پنج روز فرصت دارد تا شرایط ایران را بپذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/692526" target="_blank">📅 08:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
چرا ملوانان ناو آمریکایی خودکشی می‌کنند؟
🔹
وضعیت بحرانی ناو آمریکایی پس از ماه‌ها حضور در جنگ با ایران که اخیرا مجبور شدن بهش پایان ماموریت بدن!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/692525" target="_blank">📅 08:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFjVA7OSeord3hLdLWk9lTdH3dJ9pm0_TdWQl2OAaOcE-Lq9Re-diYECSFEbAnGstbvSvnY_YSLXqwfUbyFXXphtVfQTHCdRHAdgIGq-aYb6EKdvHVFwl4hUPjzm86BAcn4x-Xg8aIUVSluVlkPVOXf0Ei2nsNo559PubkAZflP9Wco8sR0ISsUI4ZskRNb0K00HoF3-Ab4B6O8KO9iJ7sowLpd-iVUOmwyY6Lr4BsSlcL7jwnMcenRLXJcxcRVXBk84B-pTTeWmgv9tXA3g9eCgbBMnianTDNrKHDi_JuNZcW8nUjq1HH3jl8ZyefVrBgWzkOEo8XzyjUefmem8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی، تحلیلگر سیاسی: اگر کشورهای خلیج فارس جلوی پروازهای ایران رو بگیرن، ایران فرودگاه‌هاشون رو با زور تعطیل می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/692524" target="_blank">📅 08:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
داریوش فرهود، پدر علم ژنتیک ایران: مهاجرت کنیم یا نه؟  #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/692523" target="_blank">📅 08:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692522">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ9ziLPpQ37lPzp5m71Z5VnT2HOL1M5un0lu2t-E5LnJ14De_K2zeoPKtszyB8Hpx6tF7QX0jV_AqLn4utPEj9gcr3siO4RuQnw0e_XXuUKZO6KWJmBtcPwkND14s6HzWQTpXjF7ugq0aBHvLgyvRImIdYuD9NtmeTKBJg0WOGHiorX4ajzyK6Rt18GSltvqg98PNVPSkry4Dehoyc3VetMdII-5-7jtcwfag58cKeuO8-H8yOGtpLlhzv7vbWFQKCGrmaIX9IELtdXKvI7vLqHXnxfeeYIBGgsEK6lVuFHft4z9pLw8vWf0_Fv-nUmya--wRy2uf-LFuOEey0-NSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه بقائی به نخست‌وزیر کانا‌دا در پی حمایتش از جنگ‌طلبی ترامپ
سخنگوی وزارت امور خارجه در واکنش به حمایت نخست‌وزیر کانادا از اظهارات جنگ طلبانه ترامپ:
🔹
زمان به آنان که زیر سایه قلدری آمریکا ایستاده و گمان کردند با تکرار زبان زورمندان می‌توانند خود را از گزند زور در امان نگهدارند، نشان خواهد داد که چشم بستن بر حقیقت، آدمی را نجات نمی‌دهد، فقط او را بی‌سلاح‌تر تحویل زورگو می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/692522" target="_blank">📅 08:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aX1sP3rbSwYDZRNPulgzBQ_qNSTVOus0-8VysTkRJLRQca3NEwu75a_VZSGHD-Bd8tV6okfxc2gDAawM5pcEj7StqYpeWe04CyPrlXXAA6lr8HTyQOkNMEfXkpt2eqvbZxyisxQPz8GKIJqKeOEd86iHh9SzD1pzaqcGwtuy2r8Uri8IYOHvxdvWFg1Kxzc4KVGglD6A1qe6vZbbUrkNBUp_H5YL8ru91ttepWF0JdCqixj2Apn9IWoVWiH7kRqjeYS2H-PvAoz2j7xQwzUkVFih4u32saOWXTqvFCwY7HVgTLVSaIqITZL6YchF-OKpYYaEYCzYUdaZXHMwZ86JQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqFWp3MHnftzwADzttEF0_5xzEMZ5TYzA0Nt0jZxGW18EFxbqrG__D3svUVb4TDTJMqtIWVxci-2aKCDiCVuDtLfG1mH9tSv_XIEKkQOEtql0pEhgjn343MLlIbF98eMIEm8VBJ2fbjIfLqzOvhJV8R_LcGt4BeVN3xLpSmy-FpB5xQYaGH4YTZCvDFbTdjt4l9iIAZVA9T8kHg0jIwCd3zJcmFO23mDloMApSkhARD5jsGGshi4QBDq7Akc9VzS6uJ2PdVWjJr_f_REBlPKT-iePR8uTTc5vg4445I9z5S0ACBz9X3DQQZhNXZI-vc4SulGDIQS-EJGgo89JWts4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqwl6P6xM2UNDDWhEIwxJE6XPU8RqjeZTqSQ6wOBtifog7E-8Yf3CHNtpB2hhjP_RFC-QeqfoSlUH5NXJLuHpVwFxXFNfUGt-juHumxpVWEp9M6IvpkCyNOPy1pTMcbJUGa0Wrky5Mcza-0fynybG9zMJVBYpSCsnqd094dgHAI8CdYBjRSzKKdSF6Si7tDOODNbAij8_Gf3rrTAmy_OxmWIbuPAV39iadsqcqSTgSThwPOCJXo8HXDIkthWnoj6vLjlNK_PdyvPNZj1lXA2qSOCIvy3VgVXa_F-b9xxN7GgPGywrSPeO43On7no0F6cWzcjDQA6NVl1RhL5x3pUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R14IHSkx71N9MlUDNTLR7Rv-nKlwDYAwxOrr2P7s4B8E93LV5hEhITqms9PqIqO3T7zACbC_5kna-t9dFO4EwLHnRRTnsRw6qTRi6ywaVZIIlbQv5I7q4hfggxDg-jgCuz-iyEmj53JgMRconY37GzJTf4BRGqu-s9W6TIsC2q8Sn6_EzppczjVXQQPSejgZvpg0E1PugoI9WtPsFAnab18ZzbRGdfotgT6UU4jgSoqmtMQ4pxzquAzf1AtYt20yCWnntx0TXE-lRctTpMsIAMiJFD1IJTQNpr5bwfx8mZsQxZLRs24RIACenfdTwqrLN8ZO5mUwT_-IRUjIVMrHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TdzEmet_wG0Irw_IMMjnXUblPSu6tYMqSVxsrKf-uIX6JzgNRYGhYNYY0YDTUWre7kod1b0QFf2OKRQvhW-yFoh8GO4UkfRHyUNkTzvceMZdzvY8sVbPdzkpt5ZfHPNU8r_KTGXT_Hbc7nDgHmJKTSzR91ZoBkpY3fED9XQ4UKlsB2j0FMGIeJwYhpvooa1MyyvzSAyhJUm_M1-6gkZ67GgUg1vYkFP7gPnPx179IZXB8BgL9VykYdqQS3ezguYGq8TWHxKKGmLhHXafN4DFn5zCprKJsz1pDeTgOImWWQqpMZPYaVxxjrY6uB_DQrCXoxlmoSLue-eW03sFccUbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5jaeKTLKXnw5SVyuFEnCErs3DbyYRIHrda4bJdGBpzDa9V57EdIchuzgX8WGOlVYy46HQY4SMM2PIIoj_Rds-0dN02SwdtQCyQEnOvCCShbaLFsWYdXywloYXqlA9oOGL4HUfXxOQvI59Xw3shZEkzMeZnEwH2uco4whuhs6KJKjXoE9xY4Tcgzd0e0Rj9f1m0UP2BkJje5uhZ-FqY9SRuCnXF2jGsi_bAOhWAu3aXV0mf7M_jxYJ3g9ONygZx2O4iDgb8jJbCfH02EcXpZFmwVbo3T9s_CznlSw2faYKyq3fuUxdLjofMcnwCa8_ikoBYObp4c0cLV1-g_ZLe4Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس‌هایی متفاوت از جنگ تحمیلی ۸ ساله که کمتر دیده‌اید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/692516" target="_blank">📅 08:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: افراد تحت پوشش کمیته امداد، بهزیستی و افرادی که استحقاق دریافت کالابرگ با مبلغ بیشتر را داشته باشند، بدون اقدام خاصی کالابرگشان افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/692515" target="_blank">📅 08:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692513">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a20a33b3.mp4?token=jFiJ7d2wIA7bW9gc7l48398SvoZ6HxwnZTSPYam4GbntusXVpMX_gpfHE_nbJ46s58tngDurkipmDjyQbQnt36SYSjLPDephFwb5yS8vN1P12lb20Ip6dRLOrkWToN1W0j-pOkAAt9DtYcKlVaZ6smYpQoHGWZBvB8Dfkgpzx1FKVjui7RuwPuuEeZdEvU0bldhqCi26FKf7qAvzFd5Tl0RAEnoUg6XJXfrNUFtmU8zckO2oPIxK-SXMdzCmpXn1NAnGGhFl11s5TsOhHH_si55JI9HvcYAnfbyvIeQrPa0M8pR0g2bGY5XPibs2RwzX7Vs1u7vWNAqhpA1AFZvTmY0x-qVRc6Ea8R9bMtrCiwmc0ASqyFaPEKlmDrYIT0J9dBl1INhE9AtXk-5-RH5DaVs-k1uMrvlVgb9E8QlNEbp3OVJTDTyP2TRoIb5K5pwZRHBj_Hu7_niq_q0th3P-WtS7H_M1OGCPv0o9ANPO6E7Orr5eEEuXYw0bqSh222L5mMCExesFMCV3wwkweEsxZrDnF5Exk55RoS_7K-vpiGirbOLEVb0vLR4HVWEuuJPl-_uckP9NfzsEzPcG5KGKShipxd1JK0wC9PKinBshoCCGIg0JUK0uYumaA7f05CgPpNEgFNSOKYaYfgpqm4I9Oq5h56YxrODJlZg5dAJrqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a20a33b3.mp4?token=jFiJ7d2wIA7bW9gc7l48398SvoZ6HxwnZTSPYam4GbntusXVpMX_gpfHE_nbJ46s58tngDurkipmDjyQbQnt36SYSjLPDephFwb5yS8vN1P12lb20Ip6dRLOrkWToN1W0j-pOkAAt9DtYcKlVaZ6smYpQoHGWZBvB8Dfkgpzx1FKVjui7RuwPuuEeZdEvU0bldhqCi26FKf7qAvzFd5Tl0RAEnoUg6XJXfrNUFtmU8zckO2oPIxK-SXMdzCmpXn1NAnGGhFl11s5TsOhHH_si55JI9HvcYAnfbyvIeQrPa0M8pR0g2bGY5XPibs2RwzX7Vs1u7vWNAqhpA1AFZvTmY0x-qVRc6Ea8R9bMtrCiwmc0ASqyFaPEKlmDrYIT0J9dBl1INhE9AtXk-5-RH5DaVs-k1uMrvlVgb9E8QlNEbp3OVJTDTyP2TRoIb5K5pwZRHBj_Hu7_niq_q0th3P-WtS7H_M1OGCPv0o9ANPO6E7Orr5eEEuXYw0bqSh222L5mMCExesFMCV3wwkweEsxZrDnF5Exk55RoS_7K-vpiGirbOLEVb0vLR4HVWEuuJPl-_uckP9NfzsEzPcG5KGKShipxd1JK0wC9PKinBshoCCGIg0JUK0uYumaA7f05CgPpNEgFNSOKYaYfgpqm4I9Oq5h56YxrODJlZg5dAJrqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از استقبال ترامپ از رئیس‌جمهور چین
ترامپ:
🔹
قرار است با رئیس‌جمهور چین درباره ایران و موضوعات مختلف دیگری گفت‌وگو کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/692513" target="_blank">📅 08:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692512">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
توضیحات تامین‌ اجتماعی درباره پیامک واریز حقوق شهریورماه بازنشستگان
🔹
پیامک واریز ناقص حقوق شهریور برخی بازنشستگان ناشی از اختلال بانکی بوده و مابه‌التفاوت و حقوق کامل امروز به‌ صورت خودکار واریز می‌شود؛ نیازی به پیگیری نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/692512" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692511">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ7xSanwk3aSQ4KNJl967mNwH_njymvRhf1dZuxLWwe6cdi-rBISqvV2rS450_nLNg5ZZ8DSg74ECkhqhcUIHL1ZKHzp3izpw8UOtLqTXyBc8iSn-fzK9fAuyxlwwNp9qr_ZpIF05_oQehyYrhjbkvhzF64moVI_0zIitAPj2eF_5totrramS139kCkWi6QU5ySwVCQiwntYbojCbb_0S2pYxgRIdllbU4Wj7xnbZwTiSw9MbBtpaIXBDYOL3akGZIzOx5-0d6u_gVMq-jQgxGIgoueS67s65E_YUHOzYSkRO__kd42kXPrY9pUmeDX411hjASFvfFXptfUhzJ0rug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای اطلاع‌رسانی دولت: همه برنامه‌های هیات ایران در نیویورک در چارچوب تصمیمات در تهران، صورت می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/692511" target="_blank">📅 08:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692510">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
روز پُرمدال کاروان ایران
🥇
🥈
🔹
ورزشکاران ایران در رقابت‌های آسیایی موفق به کسب ۳ مدال طلا و ۴ مدال نقره شدند؛ فاطمه مجلل، کیمیا زارعی و زینب نوروزی و سهیل موسوی طلا گرفتند و سوگند سینکایی، شجاع پناهی، عرفان محرمی و تیم روئینگ چهار نفره زنان به مدال نقره رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/692510" target="_blank">📅 08:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692509">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idds51pQkMKi5oLI3NCupqYKqq62jOLFy0l_RzV78AT0trmyPVPu1nntHUvV2D74hSWtMpU_89iz-mHGqH2z-vSzZvVig9otE1R31p8o2VP7R6yjziYSEJ4wd6JfJF5Vyz_Dvr5KDN9Z4Ym2tJsJpVm-LKnk0EOdKKj9OR3KimbrjdF3HLeV0V_xl6D_IydLDNpSlEWtMD4hYCruTLY3eK4MC_k2egdm7zi1V6uzx79P9rL6gxFXWFD0fKwd0X_BgiXycld03vT6hm-y33Tq5rUbooQXcSu_uW4eBV4YLF1QYVMgk88u6dYBo8I0Izh_d5rLfPRgqqTLP-ZnaVkK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲ مهر ماه
۱۲ ربیع‌الثانی ۱۴۴۸
۲۴ سپتامبر ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/692509" target="_blank">📅 08:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692508">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX55Xn0yzhLAvcyio-f5SrUJpXTXg2mtvXQgWaFZrdeNN5Av1HG_JFNF9yQ-DPN_zhvx0IdPCi5HnbvKh4Cefh_Fs_ny3FawbZAAmBFi9BEXQoNO2svs4uRTmuSIbSlkplDa5bL7-1_iGvkzzoI0eJw2CuEo11AoX4qJt27k7QZjjLtpV9T91xuU3TpatMqEv1hdQ6WvOcowoGNtXbrlC3DA9Fzfq7sMKxSf2yL4RoLXuiOD9lH8cUHDhd3ecppJSnikkqVPmcHfH22oXU_HxylUa8v3YYWmP7Cpmcp1QQmGrUg6hNnJ8qLE7YTeECM5g3SmVkpn0f5rqlrso7OmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج سر ماه دیجی‌کالا شروع شد!
🛍
✨️
تو حراج سر ماه
دیجی‌کالا،
علاوه بر کلی تخفیف هیجان‌انگیز، می‌تونی برنده
آیفون ۱۸ پرو
هم بشی!
🎁
🔥
البته یادت باشه، اگر با
اشتراک پلاس
خرید کنی، هر خریدت
۲
شانس
حساب می‌شه!
🪄
و با خرید
اشتراک ۳ ماهه پلاس،
۱۰۰ هزارتومن طلای دیجیتال
دیجی‌کالا هم می‌گیری!
📱
✨
➕
اشتراک پلاس بخر، طلای دیجیتال ببر!
💸
➕
از
حراج سر ماه دیجی‌کالا با تخفیف خرید کن!
🛍</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/692508" target="_blank">📅 00:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692506">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4rZMH_6dmV3KDEk2qYCFUJC9EMOasNvI-tWwjj9L0BzHrevbbBYLPtP3iyg4SoEndWyQai2XVENQHaPBTPtDiNrUQ0xE9x7r0SX6J2oFnP7ww41E6vYL7NGnV3ptTipJBNvUmQzA1qyIE60eSJqKg4HelMWKRPHIw_if4iuRFa5kyZwncDS4Po5J91Py2BMl0Oe8cd15Rc7d-nXVMiOxr-lJC_hpjX0baFgAD5ub1pF86VCz10zbbjWe9DjILCcgGn_GfcNrTMKK00eUrRZQWXd5LNKPBW_IOnKrD-zyU6pCxrcXtISkAconcbHFABUbs5jpQ-tG9thT74uWT8A6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ست سوییشرت و شلوار مردانه بالنسیاگا مدل Hami
✔️
جنس پلی‌استر سبک و باکیفیت
✔️
فری‌سایز مناسب L و XL
✔️
مناسب هوای خنک و استفاده روزمره
✔️
راحت و خوش‌فرم؛ مناسب سفر، مهمونی و پیاده‌روی
📏
قد سوییشرت: ۷۲ | قد شلوار: ۱۰۰ سانت
🔴
قیمت 1,650,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/fast/51854/180124/</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/692506" target="_blank">📅 00:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692505">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
برخی منابع فارسی: دقایق قبل صدای دو انفجار در تنگهٔ هرمز شنیده شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692505" target="_blank">📅 00:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692502">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پاسخ کنایه‌آمیز زلنسکی به خبرنگاران روس
🔹
خبرنگاران روس از ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، پرسیدند:
«چه زمانی به مسکو می‌روید؟»
🔹
زلنسکی در پاسخ گفت:
«با موشک!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/692502" target="_blank">📅 00:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692501">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHxl5vx-wsNW4g-a951g3Zcn1fGt_asRw3Qvzo1gEfG6Bxqze7x18UXafiuaJeGXTq7mRaksbi0IamYhMxPuV-qJVtP_sdNOujuTqi2vb_D-3ond7JnqLTBySyRnnTWOZOShUnOSBlf2-2aqh8_4wPIxwZpY33tWBfGZOkGiYIRNd_JtEMkHCj0QUhFqB470KXldp2Dpe39jIrNNNwdN4RBU7aleh5brfQPGK4kRAwQC6gQjyWOXRwbzMtddLwzfKWSP0ZCOqaxMFT-Sm2OSvaq3mP9cDBT-IeuSX0FVgKRquTiHWGhL-1ZRgdsgtSDKRcG6LcbhOU3ZnPiuNXOA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهرماه فراق
🔹
شایسته است هم‌نوا با مادران و پدران داغدار، بار دیگر یاد دانش‌آموزان شهید شده در جنگ تحمیلی اخیر را گرامی بداریم. امسال روزهای خاطره‌ساز ابتدای سال تحصیلی، برای ما غمی از فراق فرزندان سفرکرده‌مان را تازه می‌سازد. ۳۱/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692501" target="_blank">📅 00:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692500">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
محسن رضایی: هر کشوری راه هوایی اش را بر روی ما ببندد، فرودگاههای آن کشور هم نمی‌توانند پرواز داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692500" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi-DAZHK1XcYVARFS1yUf98wL42HpL9G3UoYuON7nAfmcRb7nTVr8VJyZ0u1YgjMIMEi13MTA2ly0unl-OdXKxG10TIbYuKkp3MKxfpU-7I8CkucHvs5wNrVhVgWcgQUVvMr7zmF7HP8ghw3O9pDtM1u86de0-Gk4DwOUp6aHtK_aGjablWCIG0BZfUcUBE_SBc3Z_YfTES8A3nTjwQ3l355Yf9-sZHPuLbZfiybVmRsaQxZqSrIZD90vSi_VqJ84gjq8EF4phlAX76qbqOL6fy53jg5GOu1eMvRNpm-1lFuQhNXYtic28xT18vUpyNjfBDjPknSx4zOGj_ICfL_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان و رئیس شورای اروپا
🔹
در حاشیه هشتاد و یکمین مجمع عمومی سازمان ملل، رئیس‌جمهور پزشکیان با آقای آنتونیو کوستا رئیس شورای اروپا و گفت‌وگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692499" target="_blank">📅 00:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سخنگوی سپاه: رئیس جمهور ما پیام اقتدار ملت ایران را در قلب نظام استکبار باز تولید کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/692498" target="_blank">📅 00:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پزشکیان از نیویورک خطاب به مردم: دعا کنید ناامیدتان نکنم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/692497" target="_blank">📅 00:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPN9XqvNOof3hVHmh2Rq8a7vy04Vj409fvr_mdFa894d6zsl36O9H4YVejADEWfomL1QO_KHyW_YspAowHE4OLJZk06dLOYjxoctcGBEiZXl9BENoZ8Y9xfu7O2WVeb_Bls9flEDi8l4yq4GjsFirOrTx3UcPTEhvLmpuAVazhWeG1qCKfN4FbCiltiUEk8Iu0bUWIZYhRteR5EFbkYSBZje8BI0n6zYSeILt0iSwTOXXKCfFLHsCl13PU1kmKzrwZH4cdOcvwX9GYBSGdn3ae-_al6oX2wBbonc4xVqgkSvkiKdcu67aCls711U2An3R7zUOhiboZ8IOczqjxWL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/692496" target="_blank">📅 00:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692495">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9YbcR-WG6Uli3vXZo1qqAuSBsQUcHBDyM6xP3rtbzd6VGPLeQcGAGVDItcwoe3DPHsa2TvD-NOU819ubfOtxc3ImeoEMHP5uqd7w_y09GcHYZqdq9cwEVHV84_Rti5Etpn1t-SoJ2nD-owA7HVI384fwCqvcQGuDO8K0mv-V1e5ons5lqyuNth9AY0Jh1XJB-jgg4Yie-FqYVusRMJEzm5mijbZvLyHaw0BWSVxZ_RdTHitPB6cbx9FDp4rKIXVdcauhjEqq9-4eOBOau6RZPSlnKcOIQpf40LuBeeVn65J43BEYWbhOsrG5o8RVVoIsoafx5w6HSG4hvzMVWNrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/692495" target="_blank">📅 23:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692494">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db361334d0.mp4?token=SAD8vqkHQW_Y3l4t0Xlp1CYWY9tz2984uZqj7R1Km8TQRxDo4UFPlbzHfKSXkNtBmsqLz2k1JYa3Cibd_u8HyrKXnZQC0xjz9LL49d57zUsXM48IPPHfFn3HcYvNm6s5GIRz8WjkmdUSX-p_ijqRHsEY2BRc-SgO6OBHtzOaFWTsIOWWuFViayxtQI46QCjf0FBJwP_-aLxG0ETJNFcXWuPsVwGq3D7fqj6AhS5DIgO1_nuA9n5eOXNqG56Zvw9z6esFCdPtkH7yiSlBIQBhYNRWrGCVDTcIu1f6DrtpvKOTrifLXZ9fHa9f5u2P1FEPOWwGe3IyD3GwfEQWxTHt4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db361334d0.mp4?token=SAD8vqkHQW_Y3l4t0Xlp1CYWY9tz2984uZqj7R1Km8TQRxDo4UFPlbzHfKSXkNtBmsqLz2k1JYa3Cibd_u8HyrKXnZQC0xjz9LL49d57zUsXM48IPPHfFn3HcYvNm6s5GIRz8WjkmdUSX-p_ijqRHsEY2BRc-SgO6OBHtzOaFWTsIOWWuFViayxtQI46QCjf0FBJwP_-aLxG0ETJNFcXWuPsVwGq3D7fqj6AhS5DIgO1_nuA9n5eOXNqG56Zvw9z6esFCdPtkH7yiSlBIQBhYNRWrGCVDTcIu1f6DrtpvKOTrifLXZ9fHa9f5u2P1FEPOWwGe3IyD3GwfEQWxTHt4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی پر بازدید از لحظه‌ تفاُلِ امروز پزشکیان به قرآن و واکنش قابل تامل او
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/692494" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAjexuN1BqUhrstiOdUJXykMKByfiVGYhEELUxhSgkOlp_W1nIoX10-f60Tk2Rf5H-YupWRAiOhCxdRqeIqTD49h49xPm9aj3yAyiC-OnDtpzSBw-9ruXMTIeeYcCP-k8-cABxwZC7KpkpoCvTkBgSELhSg78PAexkUpTXQIP42n-i8EJV2pol6O3raAR2iCTjxgslXaA7eFpysCZnd5Q5vK-Iz-mxVgaEEEgopmIavlZW8erojzfHOEzmkQU99gTL2-VJG6eNAwK4OTrmSJdoE0EeCihlrwaAMXU3iKEm6oSGgTMl4puv6L_-ARFoFqMU3HNQqMC9FBBSNpSdYUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روآن سباستین اتکینسون؛ خالق نقش ماندگار «مستربین» ۷۱ ساله شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692493" target="_blank">📅 23:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">تقدیم به شهدای امنیتِ
سرزمین عزیزتر از جانم</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/692492" target="_blank">📅 23:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692491">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ca2bdb3d.mp4?token=CyIUe-vvA5Wu3Z2x9k_dv4ruA_OMZlbuR6616rmBFKt2lYorQsycd7QTykOrf-GBd8iCWpNRBn_k_iCiy7JPPVh5__bSrh4S1WgZjUAabBU7GW22TYYFQHzh_wjDjWDlxdWsI-N7tJgvBj7JcRGzTQ5pfFsFwueaTQcgyfazoD878lksBDeVYBTLn8dVjhNKHYDjGipZPcg9jaKW7Ffi6kYhebGWwJ-4naXlXVkY9NrbRPvM-lZcE7Il-97Ia-U90r9JmJif8QLO9Kts8CCMPGG0ZpjEX74nmDITFFwmTpICFoj7Ns5EKZ94qM5FTxT5kiwIf36jYmZdDbc8p2WGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ca2bdb3d.mp4?token=CyIUe-vvA5Wu3Z2x9k_dv4ruA_OMZlbuR6616rmBFKt2lYorQsycd7QTykOrf-GBd8iCWpNRBn_k_iCiy7JPPVh5__bSrh4S1WgZjUAabBU7GW22TYYFQHzh_wjDjWDlxdWsI-N7tJgvBj7JcRGzTQ5pfFsFwueaTQcgyfazoD878lksBDeVYBTLn8dVjhNKHYDjGipZPcg9jaKW7Ffi6kYhebGWwJ-4naXlXVkY9NrbRPvM-lZcE7Il-97Ia-U90r9JmJif8QLO9Kts8CCMPGG0ZpjEX74nmDITFFwmTpICFoj7Ns5EKZ94qM5FTxT5kiwIf36jYmZdDbc8p2WGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۴ عبری: ویدویی منتشر شده از زیر گرفته شدن فرزند سفیر رژیم صهیونسیتی در غرب رام‌الله
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692491" target="_blank">📅 23:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692490">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmzMJEfBlwAZc3zewMw87m-UQL0Npbx2Ma4sFQCN4X91LlIxFK12hLTQq1c0i8aL2AVC3Ycz0M8snqB8nLE_qzeh35DDfwgTeOH1Zh7nEyumfc3ZkvbB0kveVfgl8Gi57K-y7YSA2SwS0dhSvGdfes2FUH1InrO6pSkP7Wph6t-wRhnWmGKms-B0TStO67jztV84qMpJlM0TlUAAprE60beUC61YuAaGAr8PYGuBVvMgTXBDErP6etneg9ZL726Stqq7GPwk7EsQZAWVDdSYj85Wfdb6uRb-ZX7lDxbBIkvOXLdRr4OkAfZ74O2QmIt5vJc2z0Yj1H1a966qBCcQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این پست رو ذخیره کنید؛ ۱۵ مدل آش مناسب فصل سرما
🍜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692490" target="_blank">📅 23:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7S29RSb_0deC712Zqd3yUVC7yQuXnKajYHtSLmGFR0pIxU7Q-KVkQVxX5KMO-6JOooYzQaRwjoNjxme52S_Lef-1f_dTBkVLGrb7HiDlp6qjyqmRLWZyouCCOgjQYPWovnreTLF2v_iNLiz_HzmPqQB4CHn6ZoU18qECfZLjdLbG0rZgRr2hmNeq4n7b44DwnnpWfE-0-O-sLTYoTDmBIGw83cH_zEFdaL9JAzKqkj4fiHP4C_7O4sHds-xLKSZOHfndb9hCqqYQsweq6DAyzbIEJ-sBsxSIzlfjxDvpUi7KaR0SKQzJad4xu9C2S0sLWFsBpB3e5A99ajYM1v0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaffYVeF_0uo7jLvHWyK7wmzcwyHp3erUAjQI2FZECjvvzvb9PfcFYiCUZ13r2Gb6xKCSkyIaKxYRYszPCRbxvhEZBDz1OTG7YPQdkWm1iQzdwwXyVxz1ZXIWy5RCQUaCjxqpTCGtbHkHC5Wp3lhE9SFdrL1XtTD9C05aoBb3NLffevSO3rPBOfdTr7PDdYhYWPA5F33Y2rOj6yyxTEimeY2Uy0hCApmUb_yq-rfJYoCY5jvdsgB4CAyZzoJFNuPFF1Kr6R5DCrZ3sAUQHTj-mWxGYvsrC35Yvghb94Uk18LKCDXXqffuC1yJQXnJ34zkWFa3lewuVnQuPg4tvLXqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میانگین سن ازدواج زنان و مردان ایرانی
🔹
بر اساس آمارهای مرکز پژوهش‌های مجلس، میانگین سن اولین ازدواج از سال ۱۴۰۰ تا ۱۴۰۲ افزایشی بوده و در سال ۱۴۰۲ برای مردان به ۲۸.۳ سال و برای زنان به ۲۴.۱ سال رسیده است.
🔹
همچنین میانگین سن کلی ازدواج در سال ۱۴۰۲ برای مردان ۳۱.۲ سال و برای زنان ۲۶.۳ سال ثبت شده است.
🔹
طبق هدف‌گذاری و پیش‌بینی برنامه توسعه هفتم، هدف‌گذاری شده تا سال ۱۴۰۷ میانگین سن اولین ازدواج به ۲۷.۳ سال برای مردان و ۲۳.۱ سال برای زنان کاهش یابد.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692488" target="_blank">📅 23:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
مدافع وطن
🔹
رئیس جمهور در مجمع عمومی سازمان ملل امروز صدای شجاعت و استواری مردم ایران شد و گفت که ایران را نمی‌توان با جنگ وادار به تسلیم کرد ما ثابت کردیم که برای دفاع از خود از جنگ نمی‌ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده‌ایم. او با بیان اینکه…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692487" target="_blank">📅 23:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
عملیات وعده صادق ۵ چگونه خواهد بود؟/ بررسی پاسخ فوری ایران به حمله اسرائیل و آمریکا
🔹
در صورت تشدید تنش، ایران گزینه‌هایی فراتر از خاورمیانه را نیز بررسی خواهد کرد. گزارش‌ها حاکی از آن است که ایران ممکن است پایگاه‌های نظامی آمریکا در اروپا، به ویژه در بلغارستان و قبرس را هدف قرار دهد. بلغارستان اخیراً استفاده از پایگاه هوایی خود توسط هواپیماهای سوخت‌رسان آمریکایی را تأیید کرده است.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3247477</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692486" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEllMJPBm3yJz-0dhNYQLgV8dT87beBm55ZqPGDyvQwAeq60uA-X3tFS46Ie4Ad9k404sUyC7AFOfEzJVOfM7S-fQKd9CP8I3Fh4TWztTqH3fhX3N4Bl1kogfWZcpsujEmF60aZAbcaji1KwA6U5BUJZrO02QDQkvDTjQXKCzktcpdc_02K5D0F3j0WkV5U8RWki_lUZrnICiIeGGahzEuiN1fR6TSnCr4sVe26ZxnWGnzvlzmxBugAj3E1WFh8kHxRqSree5d_LYn3qgyx60JXx3JYFj2gHxL7b7So06qGxMsRTfjw_mquv5dTpVazqeyNjCjwvR38hUlaDddkQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکلت ماهی بادکنکی همینقدر جالبه
🐡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/692485" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTC_cXAaZMJ5_xHWli5abESlx5khtXaBKagdDUbBob_WhbatkToF5dwm2r6RvY-nv5E7ezm6MgkXVdDL_YwY88UQPIwvQJHJhc0PPRLl--s9C-ekgZCTswRIKwO2Ytf_QSJqCESE1ezJMrNhFgJd0ekab4yPlzed63TVLtuxJuGNvflKj5JwK_WTEQepIhXmvkAz0wAeEsvOMdPZzU1GhzD2jPnGKxc-UoHKrky1ypXSypy7iKHWVqK4uSWSn5svWudvx9WCtcStRGCnrSjqhxFAIM6RflQAqfkZXcQ0e7s1FK1WcWO48fo6Te3CunL1c90sOxSEtaJzxUe7DxQxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس نتانیاهو از امنیتش؛ حتی یک شب هم در نیویورک نمی‌ماند
🔹
کانال ۱۳ عبری: نتانیاهو به دلایل امنیتی ویژه در خاورمیانه، حتی یک شب هم در نیویورک اقامت نخواهد کرد و فوراً به اسرائیل بازمی‌گردد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/692484" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aea0d78MTQpFM6SpbBX3QKZb4TaQ7eS6UcfDzPvefVjdw9twWqHDVR8UPGlTTK2tTjbAvWyfgKvsMH06wyQ3o5aGJVAkFSx57o9QO6wzr0FVTwAC_rLbfP8faQKuevZRLhHs3r2U5Q77FgCyv-LXxenvq3ZIYok5Hrq_vaWNz_15GXL-DJNoOa3lO8jgSCkQVUXq58kaJ4PTiP1fF6rJbhEXgn4doOmjd8yCmkC3Xg_4cX8cNJhlrLp5AEyKLpqQHl2OZmOldrlOcKxn6KjSBdida6EveK9NCSy08i0YkNao0Np_j1CZXTnDBPwvjDVMf1JSjAAFTeD62gGAWuZpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدافع وطن
🔹
رئیس جمهور در مجمع عمومی سازمان ملل امروز صدای شجاعت و استواری مردم ایران شد و گفت که ایران را نمی‌توان با جنگ وادار به تسلیم کرد ما ثابت کردیم که برای دفاع از خود از جنگ نمی‌ترسیم تا پای جان برای دفاع از ایران عزیز ایستاده‌ایم. او با بیان اینکه یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم افزود که ایران به سوی جهان دست همکاری دراز می‌کند، ما جهان را به صلح فرا می‌خوانیم نه از سر ضعف بلکه از سر قدرت خود.
🔹
هشتصدوشصت‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692483" target="_blank">📅 23:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cc2fd75c.mp4?token=c_vBqCOg1hCnftaX44GByf-wrC4wLJCtwBecWmt_1v6k1IHmISfFtOaXC7F0vXp5tEm8qf36OrHLpAr8RESr-B4yLtbJX37Sfg5v2B7i5Rouo-xTNjb_-BMDM09l3WO9okNwN3GbOY4-NkIXWtelX6RNiSlAZy3P1jb4vE05BdFIicPnbDa8XhFgQLqnRQJdCRCRGII3eZ7m0Kbuyoov0CAo7gQ2HRXF138fZNG5pbbD5nM0Vp3uYDFAlOyoRpfNR-kRZkZ6Q1oZxnPO1KnxCWaXp3cVkP_xa3W-fsDZVmoTTj59jSkQM6Hcs5qr1bT_clsekykkd0-yub4S5uv5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cc2fd75c.mp4?token=c_vBqCOg1hCnftaX44GByf-wrC4wLJCtwBecWmt_1v6k1IHmISfFtOaXC7F0vXp5tEm8qf36OrHLpAr8RESr-B4yLtbJX37Sfg5v2B7i5Rouo-xTNjb_-BMDM09l3WO9okNwN3GbOY4-NkIXWtelX6RNiSlAZy3P1jb4vE05BdFIicPnbDa8XhFgQLqnRQJdCRCRGII3eZ7m0Kbuyoov0CAo7gQ2HRXF138fZNG5pbbD5nM0Vp3uYDFAlOyoRpfNR-kRZkZ6Q1oZxnPO1KnxCWaXp3cVkP_xa3W-fsDZVmoTTj59jSkQM6Hcs5qr1bT_clsekykkd0-yub4S5uv5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای متفاوت از آغوش گرفتن در یک تئاتر که در فضای مجازی وایرال شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692482" target="_blank">📅 23:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692481" target="_blank">📅 23:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKVGqzlCADJUOeXtKhC5-OVFfJ7MDUGqTyobfbm5JQiUA9bO7qmNwA3L27DXloz_WNJd3Gw5Jssch_4KNVd2qSXulaSd6AQ-SJc5VckxndFj7QK1VsBGO_j_5C6Fx8-ufP3yfV13mE9Mkr8R7oHE-Uql-jxUtxk2pbqb1fH-4OlX6wgcEBup0XmkoSs_oE8DFnBxMJArpsSvdQcl2ac6hVg98eaWZeeVK6tcdxUGhUwIlNmKzblog7AeN1bNLHixHbQB6Yb51m_5KQ8Au67n9uoEeJoAgM6ewNLp-8MXJP9Z3BY-F8DzFqtGh9p0Lf4RplWGxvydRUZVZkQuq-Q7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
فشارسنج سخنگو فارسی؛ اندازه‌گیری فشار، راحت و دقیق!
🔥
این فشارسنج رو می‌خوای؟ قسطی هم می‌تونی بخری!
❤️
مناسب سالمندان و افرادی که نیاز به کنترل منظم فشار خون دارن
🔊
اعلام نتیجه به زبان فارسی
📊
اندازه‌گیری فشار خون و ضربان قلب
🏠
مناسب استفاده در منزل
✅
امکان پرداخت قسطی
🔥
قیمت ویژه: فقط
1,990,000 تومان
برای اطلاع از جزئیات و خرید
👇
خرید از سایت
👇
https://memarket24.ir/product/brief/63656/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/692480" target="_blank">📅 23:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/692479" target="_blank">📅 23:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/opMSJdpcGfId0clLJVHgkMDqOOPjIsrGI7cg7wodsmoeGY6A-mgR7JUlWBK1SbP-nmrr2_e-9vzEJPxJoKnAri_tqvO3msDBFhOi3y68EJjeAQiBff8ebfAEPuY2C88XN_F4fGGWLYvvpPJmRCyMoYGVPRyAOLItJ60_WpKsebWepPV0m0_odN2j_57NJnCMoMhfcMvVlFNVCdns138Bx4Ij0-45CodYqNSVYctJzLdgs1-QfH2-6TTRSHpMA419CvIhm3Ld7D2w18NRQDp1Da7h7MWnvMva_3zFA0ba65FovFXvw_J-ZgELHd-plo9S-u9uUTii1qJoS6zP8cHBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWWbzzS3qPxaTDrebSU_Lkims2FHlVrjNRwab4I3DiGVQIEkDd_44WDciXRyWXIrWTudVP4yD0YyHiNSgyzot8fDsi74rS61_QFqXEnriX15Gliu-xMpnk-0e-W2qtzhtOPL2QGryPxXcrauSulajB-Jkr_VpzotDRBX1oOLmsbsngKrQmcRJrOSrqqE0j77uDa5uoeQhS51vjxN75EDu9Cpywp6nUcR5OFEEhMwRvEVPtQxpa3kkGZm4a9MvtdsOcjqS3PVSsjVunCiivc6zzDqANZnRQCfJj6tXaDipP85nYQ_6VaADyTrsaF-oBomQ-gEFdS0_feig2O7C05LsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ماجرای ادعای عجیب یک بلاگر بانکی در پی انتشار جدول پرداختی نامتعارف بانک‌ها به کارکنانشان؛ توجیه به چه قیمتی؟
‌
🔹
یک بلاگر بانکی ادعا کرد اعداد منتشرشده حقوق کارکنان بانک‌ها (۱۲۰ تا ۱۷۰ میلیون) در واقع «هزینه کارمند» است نه حقوق دریافتی. اما بررسی مستندات نشان داد این ادعا غلط است، چون «حقوق و مزایا» بند جداگانه‌ای در هزینه‌های بانک‌هاست و هزینه‌هایی مثل بیمه در بندهای دیگر محاسبه می‌شود./ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/692477" target="_blank">📅 22:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06787fe62c.mp4?token=otiW-f2_GUAEYDhlKAbbqfFhzl7-kZewLvS-eXdD2P6Et5h0addnXCI3jg7tcbJq3WPZj6dUjX8Eg5z13v6fsj8UUeFWCJkObeqCHVdLaMRAl2MLAZJnHdfdGdI-ixpzPGCxPEscmc9OAXVglAO7BM585Z3SUY20adfD8oLFU56NSsTBW2T1OOOkKdoyovMZQ2adYzxxO4zIRBmJvxiX4-mCJAVkLv8FPuFSgHhf55_Unnk32Ev-49sRcgyDwxjNrpbnDVZHL0LvSM0yVljYTBLquBmAWjSUJ_POxlnZdZIOVt8gSOcL6pdZdTXnj_u47whCBJ0SSDZM5sBY4Sz-Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06787fe62c.mp4?token=otiW-f2_GUAEYDhlKAbbqfFhzl7-kZewLvS-eXdD2P6Et5h0addnXCI3jg7tcbJq3WPZj6dUjX8Eg5z13v6fsj8UUeFWCJkObeqCHVdLaMRAl2MLAZJnHdfdGdI-ixpzPGCxPEscmc9OAXVglAO7BM585Z3SUY20adfD8oLFU56NSsTBW2T1OOOkKdoyovMZQ2adYzxxO4zIRBmJvxiX4-mCJAVkLv8FPuFSgHhf55_Unnk32Ev-49sRcgyDwxjNrpbnDVZHL0LvSM0yVljYTBLquBmAWjSUJ_POxlnZdZIOVt8gSOcL6pdZdTXnj_u47whCBJ0SSDZM5sBY4Sz-Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کارشناس تلویزیونی: لابی یهودی‌ها نقش پررنگی در تصمیمات کرملین دارد!
هیراد مخیری، کارشناس اوراسیا:
🔹
لابی‌های قوی یهودی در روسیه یک پیشینه تاریخی دارند و در زیرساخت‌های اقتصاد، فرهنگ و سیاست این کشور ریشه دوانده‌اند؛ این اهرم‌های فشار همواره در تصمیم‌گیری‌های کرملین نقش پررنگی ایفا کرده‌اند./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/IhdkEI9yI0c
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692476" target="_blank">📅 22:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
نتانیاهو با ترس و لرز عازم نیویورک می‌شود  شبکه ۱۲ رژیم صهیونی:
🔹
نتانیاهو امشب عازم نیویورک خواهد شد و به دلایل امنیتی، زمان پرواز و محل برخاستن هواپیمای «بال صهیون» از قبل اعلام نخواهد شد.
🔹
همچنین محل فرود هواپیمای نتانیاهو هم اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692475" target="_blank">📅 22:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692470">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq5wdbUcN4WM0-6whnZvObj4LWpgYFDLMJwGO4O9svDuRbS9aTZ2v784jtRDFmVV0l7T-wIGAaDfIkryEBc-1f77FevogLUV8USzuZ4HQGQ2pdywnSVS0JDgp9Zja7vSNdU3opWdbZWUFFe2ZxX4lDQDAOgbxVcckGcr2JUedvurV10b3qRNRVmklysoA84xOSXkmovQh4amAuCexkhaVp0Hty5fksfBS1OYp5YN0_RFm9cE3IZOKYMbrzMaD2f3D3p_nNkJOYJLoC878hS6wD-ol9B8N69_5HndY3cLvjajrnk1M1J3Zklk2Fe0QWEqr_Aj3vppkFgfrE2Iv2ovIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv2ivejdtv_bkiu_J3xNVCIZgJ8Y-A5qHT-WTUiVkpptPtuhrzOS6XFjUOxXMrFeONCrKYiQqemED99OfJry3WubBMsUDuocZl1gRowhDGnljJWcbJ2jMVaVmUwl9Oh8vkf_2uR0A9qcHJpd9uls6CaZcTNE61diwK2i_sa7i1_OvttsRkf8WQmGres_IGp0hY2a6DE1hZ2YI36l3Qk5sY490oCXyqrP8aKA6B7x0Soy6fh_ep3Di9Q3u-WXCF7XDbmFreTW4Fp2-Z_fUAPMfs8PuUSM3QIdjcJQd0BTYmWSpyxmK1zhqb74Xz_UB37jBtOj37soiZRnNqfNB39oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3Y--jMfnQh3-kHUBbpnvryYG2KpnpSoQCiZp6mxqVH_x7WTW7O2E-GsccCz8MluMSFnRLeyNWG1Wr6RBA2ZFY8R5dyV0naDBwuxehoFkOC5KrWITqv03EP_Pd9DpHK7yGq2uXJ-mmpXJK0U-nsG-6piQUxC3nfGKL9QJkSnbgWbNM9GPt_IdZwDgEvtZxcGTJo2Si9IEOT8JYU8L5Bem3ir-c4UTKVL6KMpRHP4tfUieCcd7cf5ELofn2CQdMzfwchn4S0beDuIRQpWrjwaydidr-TTwlL18jgELtgMluhIWTxasyILUtT8aMkBrdKwpUEmh01_eUv9dRms_WH82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6sHvc9MIi1HMAWOE6hvFgXXKtq8DzN9MPo04Z7_sGH7GeoErJivF7_LVH1HNq-nys7kTdt8DwYJJF1-XOccB6rMrrIjLGDoPya3f5_Y0kiW-pG_6eru0SlepieR2_O8RVMxeJ2M3f3jFK8A-xhQ120BxWjM4yje2QoyrghtmhvH85J2hSF-4s1t9e_WuhI-yvwfU2owMzKQHBaLG_SwZpq1rgi_XJVYE-49t06SlWnLDWhO3ZR6FqgQYfDGc2oOJbmwvRYe23bTDue029xZvRKCUd5vRluO1L1TLsfTnlVKn3ZetPqq8wl5Q_MRL49_j1AoG05z3PPuCta66BbQ5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5c1b7e8a.mp4?token=IDcDpL9aVoLlGrAySdxGNoNdMubqM_3rJPcIuL1EKtWW2qVXdy8wMMwV5yzTZM6EZda-k_NQWC7yDu_xdzgPLcLPM5MP8a025UA0e01uEjLQB6-hheZ643d23I62YooUE7r6KkedWeFilr-aQ6d7lAiwIpNBnxxIjsLDqPqMbNEXuoftGvCbq0AoaN6WMZuFVBZWyGM5cuwkvFa8vPlSZya0hR6TfIBeTJ5g-DYrwwNs4vpqk3kM-Bi9PDAcHdUdarppd4_LJpcsh4gRjDwkUHMryHJXWjUEZLwetT2kddXN1ECTuqZIXR_Iwwo4keqrMAa49DvwDiS0QFKspIUa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5c1b7e8a.mp4?token=IDcDpL9aVoLlGrAySdxGNoNdMubqM_3rJPcIuL1EKtWW2qVXdy8wMMwV5yzTZM6EZda-k_NQWC7yDu_xdzgPLcLPM5MP8a025UA0e01uEjLQB6-hheZ643d23I62YooUE7r6KkedWeFilr-aQ6d7lAiwIpNBnxxIjsLDqPqMbNEXuoftGvCbq0AoaN6WMZuFVBZWyGM5cuwkvFa8vPlSZya0hR6TfIBeTJ5g-DYrwwNs4vpqk3kM-Bi9PDAcHdUdarppd4_LJpcsh4gRjDwkUHMryHJXWjUEZLwetT2kddXN1ECTuqZIXR_Iwwo4keqrMAa49DvwDiS0QFKspIUa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون فرآیند آماده‌سازی ۱۱۰۰بسته تحصیلی به یاد کودکان میناب برای توزیع در شهرهای جنوبی کشور به مناسبت تولد ۱۱سالگی خبرفوری توسط همکاران این مجموعه رسانه‌ای @AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/692470" target="_blank">📅 22:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/692469" target="_blank">📅 22:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
همتی، رئیس بانک مرکزی: در حد توان تورم را کنترل می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/692468" target="_blank">📅 22:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692457">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a682239e.mp4?token=N9TbIPnOZugGxqdeS1xfoAu_g6Cb4FWuPQrqfJHbH6F0wIq6JVEN1FJVXgoAcVMXuFpHegC0ZFHW8UDqFSr5uJlFmoiKHpo4VxFWXFbreYKqFwo_Syw_lueTbyGIZ8bLHWVla4hZXE5MAbuF_ty9QiaudG4S8ECVM4PxHGtELqACV-9n1BZV3Ikge95Bod4k80xJ7OI11JISb6EshuKNS8MjTZ7u6jjn0SNTai_dCesCwLKBtLrLfTf_VULAY2Ia2Gx-GCr483SFADkdobWgblHJWAduixsEHkztya4rRexEZEnZgCuugJwLiJ41O0sSK7nF5Ef_ycABYvQMqJgn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a682239e.mp4?token=N9TbIPnOZugGxqdeS1xfoAu_g6Cb4FWuPQrqfJHbH6F0wIq6JVEN1FJVXgoAcVMXuFpHegC0ZFHW8UDqFSr5uJlFmoiKHpo4VxFWXFbreYKqFwo_Syw_lueTbyGIZ8bLHWVla4hZXE5MAbuF_ty9QiaudG4S8ECVM4PxHGtELqACV-9n1BZV3Ikge95Bod4k80xJ7OI11JISb6EshuKNS8MjTZ7u6jjn0SNTai_dCesCwLKBtLrLfTf_VULAY2Ia2Gx-GCr483SFADkdobWgblHJWAduixsEHkztya4rRexEZEnZgCuugJwLiJ41O0sSK7nF5Ef_ycABYvQMqJgn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روح کودکان میناب همراه رئیس‌جمهور بود
🔹
انیمیشن لگویی از سخنرانی پزشکیان در مجمع عمومی سازمان ملل و یادکردن از کودکان شهید میناب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/692457" target="_blank">📅 22:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692456">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzdCNEKDyHLZtQBbQzNPKG_xpK4vv6JgzWNry64AMy9V3K3SQYSDRoTgGuJN-mrHOOuoE63ixfaelyyhPnHLY3LkBtUUZ_89o8kjN-L1QwtvdafcjW52JORDoTAWE-_U7M6nJcqhW-0ELsA9isZGsCkf3HuIW7MsEZqkHEZoGwXd7S2gF5yOYL8hxAYmFl8zrRJwF6oftIqIPqRFegIR1pM-rsD9Gt5sRdMteSQimq9-3_Ypt5CGM9eK1ZEyuuCHNmfLc2iC5j3Pxx7uy6SGCK6YcUXZH0DN8h8i56lW_QnfKnU1MISanKe5pSm9XSbQdK0iTxro9oMUyxuJyuf5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همان درخت، اما در چهار فصل
🍂
🍃
🌸
❄️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/692456" target="_blank">📅 22:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_wlBDD4EQISbKjLUMYZnaJA9F8YAVQvB7uvANCa29WgIP6Xq15BNjP4QutPgc32PNY-ACVtliyhMeMiUUkn6S83FR5OPckOHcmnLFH-onPGWxV4jMqb9MxZgmmGhixPVNea9cbe3p2Qy2qCzRmqesrc9aduW80bhOIFb8Hn5BHp6R-ucUtXwLl3htC-Z3dZMB3PWleqgVlggPbtaMMHbZRj5KlOPoi9yS5CYGPujbZa5faCfm8QYiMraOVMd3tKW4_0bJIeyECBo-8uv5V5dH_2wbc9T5s6ZgGU8lm8wC-mKPDigaQJOLSpVOCwDjFH7yuEWao1wyxa58drFxnufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش دستمزد کارگران بیش از نرخ تورم، از دستاوردهای میدری است
🔹
اکبر شوکت، عضو هیئت‌مدیره کانون کارگران ساختمانی کشور، با دفاع از عملکرد احمد میدری، وزیر تعاون، کار و رفاه اجتماعی، گفت: در دوره حضور میدری، افزایش دستمزد کارگران بالاتر از نرخ تورم انجام شد و انجمن‌های صنفی کارگران ساختمانی که در دولت قبل متروک شده بودند، احیا شدند.
🔹
او همچنین از احیای بیمه‌های قطع‌شده کارگران ساختمانی، سرعت گرفتن روند برقراری سهمیه بیمه و توقف پرونده‌سازی برای انجمن‌های صنفی خبر داد.
🔹
شوکت با اشاره به طرح استیضاح وزیر کار نیز گفت: بهتر بود پیش از طرح استیضاح، نظر نمایندگان مجامع کارگری و کانون‌های بازنشستگی در استان‌ها دریافت می‌شد.
🔹
وی همچنین حمایت وزارت کار از اجرای کالابرگ و اصلاح ساختار یارانه‌ها و دهک‌بندی‌ها را از دیگر اقدامات این وزارتخانه عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/692444" target="_blank">📅 22:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKe_4Fe1_zLvfOY1BFPzB0npJ76EZJwC_4MN8m8cU6n9bYGOnKZVJZD3VdSEi3EUpn3dDUYFW8TM_jFRpQasbBwoypoMKMr-0zZsS4guE6il52iHC7uqxQrwwM9Ftk7iubfhCJavb_2FwJ-mCRLqgsRj6kGFoUTeEMf4LJ-owrkd64hX4JXhRAYjwg3GShtUkANCEXNsIddlI05l_x7kflMCqvYGplSbNklT9-DtY5UOoU6DPyMAbKEQKAY9OoY6ttJ82mC3N55gEnxZQb6hC-pPrCZ65Va5Orp84ZBuqGrKs1jiNggk3i4OlW4SpSEW19NeFQbl99IfaNhqw6jovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/692443" target="_blank">📅 22:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c75dd6a1.mp4?token=hWOJIOMw4NawvwSMxQ8__vWnxyKX1-ephhRxI2sRRX7jjNspT92JbQf7DMlO-oT1UNw0udoYbEhn4zWneUhp5PVSwyxHJnTQmBMYFerbuT3ArxoYTuc0PfaTZQNzunyb1fhjNTd0zpX1jzh12rKGZeQl7f_jRpUcbperlTkf8rZvIntDUm1zBgeKnXYqeGhfOVQjRK5h35hm-hq4cK9JzLwOfgMzqGeD2hpWj9QoziA_rTgwz107RbU9Io_nMIFeZZeJi9AbF4gl420c0X7ulAyzxZI24OzAhzJOuyJopX_ZmI991wo00NbVmioHZQWAZlXV_3QOiNc2N7PEWLkjCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c75dd6a1.mp4?token=hWOJIOMw4NawvwSMxQ8__vWnxyKX1-ephhRxI2sRRX7jjNspT92JbQf7DMlO-oT1UNw0udoYbEhn4zWneUhp5PVSwyxHJnTQmBMYFerbuT3ArxoYTuc0PfaTZQNzunyb1fhjNTd0zpX1jzh12rKGZeQl7f_jRpUcbperlTkf8rZvIntDUm1zBgeKnXYqeGhfOVQjRK5h35hm-hq4cK9JzLwOfgMzqGeD2hpWj9QoziA_rTgwz107RbU9Io_nMIFeZZeJi9AbF4gl420c0X7ulAyzxZI24OzAhzJOuyJopX_ZmI991wo00NbVmioHZQWAZlXV_3QOiNc2N7PEWLkjCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادقانه‌ترین مصاحبه تاریخ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692442" target="_blank">📅 22:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38cac377e0.mp4?token=ngRp4twjAJCe7YSmCvEN8HnFnI-NF1A_jkNIAR3FhthuRkt3ug54JYHfwxjSRgedtBFuRmRdMZf4S5Kaju2EH-PENTZMTSeqRZdhp4lYT-uCS5d6lJ0wJ1oOG53noCi6zxBizER7RrbBh8fNvQqJeE326Dow5dupJ2WkRQ8rpyWJlmG6BIVC8eRliBKhS7MUS_APO8Z0BErkNomEhca338LqNeGudOvkZ7n1hEj860iCr72HVN7LVOsunmJoWqj6VERPYuPagQsHts1lmPsVsb0RgaYLXfGJ-4Z9JTTI1SQsc2txSMIl4uFMPrUKclRtOHwOXKPDQBKLPQDagbhcoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38cac377e0.mp4?token=ngRp4twjAJCe7YSmCvEN8HnFnI-NF1A_jkNIAR3FhthuRkt3ug54JYHfwxjSRgedtBFuRmRdMZf4S5Kaju2EH-PENTZMTSeqRZdhp4lYT-uCS5d6lJ0wJ1oOG53noCi6zxBizER7RrbBh8fNvQqJeE326Dow5dupJ2WkRQ8rpyWJlmG6BIVC8eRliBKhS7MUS_APO8Z0BErkNomEhca338LqNeGudOvkZ7n1hEj860iCr72HVN7LVOsunmJoWqj6VERPYuPagQsHts1lmPsVsb0RgaYLXfGJ-4Z9JTTI1SQsc2txSMIl4uFMPrUKclRtOHwOXKPDQBKLPQDagbhcoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان کتاب «کمک‌های آمریکا به مردم ایران» را به رئیس‌جمهور سوئیس هدیه داد
🔹
در این کتاب جنایات آمریکا علیه مردم ایران، تحریم‌ها، حملات نظامی و ترور دانشمندان و فرماندهان ایرانی تشریح شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692441" target="_blank">📅 22:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
انجام
انفجار کنترل شده مهمات جنگی در جاسک، فردا از ساعت ۸ صبح تا ۱۲ ظهر در محدوده شهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692440" target="_blank">📅 22:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtTfSI_T4gvdnRLKzUuSBV0O0jUsNs8x_NRPsdH_8rkk0-0Ux3bdKuIgWREl0x29kcQAJ6IJIcWU2T-h1zDMpW9mH05X3MD9UBYCSZiUk5rJKY9WEY16qHGtAD8i0uYAMhY2NfYuElydVOBJ2qI6TBTT2_4eKeMyc9xCAg8a96QbEGT6Jgv-z_xxnHMljHGnXzzOlDX5KaQwNb0-rOtaJygWMw9gnjssN5VhfdvTwQqnkTEZuQdUv_CrVKdrXazuZza11Qm2MHHmEPDA0JJxVBzTgpAES0WwK5mnb5wkpaA3u5hRyvMtTqpPC-3U0xPgluoCbaOd8SGAM6tY7Xlm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی طراحی لویی ویتون، حال‌وهوای «شب‌های برره» را تداعی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/692439" target="_blank">📅 22:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692438">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96795c03d9.mp4?token=gvLbVTFp2dTU0auI8qxddv5PLaLWFGKiwFoDfpv3PhqdHfUtgB95nvjGB1GnyP01dJW0QBZHz9uakF-o_0ryrPlevp5UyKMuRh8gcc7UqvbN6XCdVopteWtPWe-jGbTu2zTc-ZZsNZkQk8P_ovp1nwQ5OlS6HXiqMed-OGa5ZBbfdzbVF-BtxwXijmv_NGklhTuIHTFlrLOHswaZZFoJJiingNbBFNvjO25obr9LxmfmZuKqaULGjZcoQ4NEZDZpF_1N5VPwr9jpu5LrAbbr7MxeS_BTwVHxlxqCQKULRWAB9ACi-xe47ltSKL-K5tsPN01y5ezOzpPACpPbj1etXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96795c03d9.mp4?token=gvLbVTFp2dTU0auI8qxddv5PLaLWFGKiwFoDfpv3PhqdHfUtgB95nvjGB1GnyP01dJW0QBZHz9uakF-o_0ryrPlevp5UyKMuRh8gcc7UqvbN6XCdVopteWtPWe-jGbTu2zTc-ZZsNZkQk8P_ovp1nwQ5OlS6HXiqMed-OGa5ZBbfdzbVF-BtxwXijmv_NGklhTuIHTFlrLOHswaZZFoJJiingNbBFNvjO25obr9LxmfmZuKqaULGjZcoQ4NEZDZpF_1N5VPwr9jpu5LrAbbr7MxeS_BTwVHxlxqCQKULRWAB9ACi-xe47ltSKL-K5tsPN01y5ezOzpPACpPbj1etXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه افتتاح اولین پایگاه آموزش نظامی یگان‌های مردمی جانفدا با شلیک حجت الاسلام طائب؛ فرمانده بسیج
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692438" target="_blank">📅 21:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692437">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39ffd5743.mp4?token=d3jkmakshT2R6KCGw97t_cy7NDctiCmD0hfvwJu93M0D10vgn8K-Tb26_X8EHjnqeShEBQMI9wfBUfrNII2-8-nCKtO119rofIQVlcGAXoSv5Zjeiai3mpBU8AgYAaKD6BNTb64ybKS8NrXJgB1fb2eFn16KOOrqstZzFj8mTc3FakSduy78YvW-y9U-K-OB32z9jnENVL6m7NMd9UmNM94kuwR00sgpGrFTb4nt5VoVxWe4-4TWxPz8gN8wxxbmz-qbaanGjVAtJNWkg9FBJAXh2fkZXJJBtnpWE-whSNTEAHPqCdZoaX8FFN9XQi6fZoYn1I-QwzunCXbby2b9HZn_gSVYSrl6lHJ_mXOCPDvhZYfVsppQv2Blg3A4QyMYil5AUPd42crWAUBAvRMfb0lyI2OHVcHHfQHp_NpbwOz4jeDfZLW4mXPL8iSVmlhQMdfTbqkPOH4ntzS-S-5XZlI787azV9JiL4IMvcHxpXRDjK8z1JHSKHGV0yyWxDOQZUUK-pri7OcBHMVEXmxrfPiIF-625zYAMCkxhA01ufuIWFGTasejE54yJtfo712D_AonppMYrrySBrVvNQ_2HslCsWa3JBCIJj3htT2N6jSohC6txQPQcjJuB60iYmKlxt5FK_h1I5S37du46FR8ShBuIfEahHxVhT1NVMzEa_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39ffd5743.mp4?token=d3jkmakshT2R6KCGw97t_cy7NDctiCmD0hfvwJu93M0D10vgn8K-Tb26_X8EHjnqeShEBQMI9wfBUfrNII2-8-nCKtO119rofIQVlcGAXoSv5Zjeiai3mpBU8AgYAaKD6BNTb64ybKS8NrXJgB1fb2eFn16KOOrqstZzFj8mTc3FakSduy78YvW-y9U-K-OB32z9jnENVL6m7NMd9UmNM94kuwR00sgpGrFTb4nt5VoVxWe4-4TWxPz8gN8wxxbmz-qbaanGjVAtJNWkg9FBJAXh2fkZXJJBtnpWE-whSNTEAHPqCdZoaX8FFN9XQi6fZoYn1I-QwzunCXbby2b9HZn_gSVYSrl6lHJ_mXOCPDvhZYfVsppQv2Blg3A4QyMYil5AUPd42crWAUBAvRMfb0lyI2OHVcHHfQHp_NpbwOz4jeDfZLW4mXPL8iSVmlhQMdfTbqkPOH4ntzS-S-5XZlI787azV9JiL4IMvcHxpXRDjK8z1JHSKHGV0yyWxDOQZUUK-pri7OcBHMVEXmxrfPiIF-625zYAMCkxhA01ufuIWFGTasejE54yJtfo712D_AonppMYrrySBrVvNQ_2HslCsWa3JBCIJj3htT2N6jSohC6txQPQcjJuB60iYmKlxt5FK_h1I5S37du46FR8ShBuIfEahHxVhT1NVMzEa_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرز بین کانادا و آمریکا
🔹
یک نفر می‌تواند همزمان یک پایش را در آمریکا بگذارد، یک پایش را در کانادا.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/692437" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دو سیگنال مثبت از اقتصاد ایران
🔹
ارزش حقیقی تراکنش‌های شاپرک در مردادماه، با حذف اثر تورم، ۳۰۷ درصد نسبت به تیرماه و ۲.۵ درصد نسبت به مرداد پارسال افزایش یافته است.
شامخ صنعت هم با ثبت ۴۹.۸ به مرز رونق نزدیک شده است.
🔹
نکته قابل تامل اینجاست که شامخ کل اقتصاد با عدد ۴۶.۹ برای پانزدهمین ماه متوالی زیر مرز ۵۰ مانده و صنعت نیز دهمین ماه انقباض را پشت سر گذاشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/692436" target="_blank">📅 21:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اظهارات وقیحانه زلنسکی: روسیه با تکنولوژی ایرانی نمی‌تواند ما را تسلیم کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/692435" target="_blank">📅 21:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3162143bf.mp4?token=LmgplDj5VV0XWqmiSSq_hBzRvWkukHa8yp_6ZwetzLljLkFlk0Wja_YVEabmsA7qVcy9im0Q7LChHk0upcuX_vIMmAEC4m3JTQX1JyxNcChoxNDy-B7Ox-ZXWoegYxWuqn_ubzog4MWbk8aDwPhn_r821CsEVuZL18BFT-RRosajOVE4IWfpySW7IvvJQ1I-ejv4GaXtKQVtAeCPG4IVf_o9D-W3hZ_XjNxDkDotxoCmBt4yT8fiGm2vDMovJsj1gVTWstIvCc7nuqEgL_OuTm__ULsOQuGRjqKX9TgoveX1OZc3IupZhN-b6v6afhBXkO8Naa8gC4mIL6O1lmET9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3162143bf.mp4?token=LmgplDj5VV0XWqmiSSq_hBzRvWkukHa8yp_6ZwetzLljLkFlk0Wja_YVEabmsA7qVcy9im0Q7LChHk0upcuX_vIMmAEC4m3JTQX1JyxNcChoxNDy-B7Ox-ZXWoegYxWuqn_ubzog4MWbk8aDwPhn_r821CsEVuZL18BFT-RRosajOVE4IWfpySW7IvvJQ1I-ejv4GaXtKQVtAeCPG4IVf_o9D-W3hZ_XjNxDkDotxoCmBt4yT8fiGm2vDMovJsj1gVTWstIvCc7nuqEgL_OuTm__ULsOQuGRjqKX9TgoveX1OZc3IupZhN-b6v6afhBXkO8Naa8gC4mIL6O1lmET9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سهراب احمری، ستون‌نویس سابق وال استریت ژورنال: در آینده، دیگر هیچ دولتی در آمریکا، نه جمهوریخواه نه دموکرات، به جنگ ایران نخواهد آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/692434" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e40853421.mp4?token=fdUYtAhNMPipVUcINGeIfhlw5C80Za8yAFhDPCJDm--ErEBLvPh1aoWFBpJeJtlQuwbSfRZKjqdPLBHR11kMOXzZ-VmRG0iz3LmnZzAh7F_w9KQuHkN_m6Z09GqmXRaPP1KsvsNr8kQCU_vZ21hGJMbSvQLu2BMpUD4t-Rfk2ioNnCaX7MQTVYb0xCvVeLwi0ogeuMlxw1I3BAt-hFZj5lGQMn9iQmDD0zKo1oiFHYjq-XsA7o_jUUg4EtQBD4u19fPHbG3puSMUNxMu6Uhspl_kvJitPoHLAsxik77g75u29wyYp-PK6CL1YA531KZLu-1RPVB8w1jP7QtsoWutvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e40853421.mp4?token=fdUYtAhNMPipVUcINGeIfhlw5C80Za8yAFhDPCJDm--ErEBLvPh1aoWFBpJeJtlQuwbSfRZKjqdPLBHR11kMOXzZ-VmRG0iz3LmnZzAh7F_w9KQuHkN_m6Z09GqmXRaPP1KsvsNr8kQCU_vZ21hGJMbSvQLu2BMpUD4t-Rfk2ioNnCaX7MQTVYb0xCvVeLwi0ogeuMlxw1I3BAt-hFZj5lGQMn9iQmDD0zKo1oiFHYjq-XsA7o_jUUg4EtQBD4u19fPHbG3puSMUNxMu6Uhspl_kvJitPoHLAsxik77g75u29wyYp-PK6CL1YA531KZLu-1RPVB8w1jP7QtsoWutvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداداد عزیزی پس از حواشی او در پی فحاشی به امید عالیشاه، با حضور در یک مدرسه در مشهد، زنگ آغاز سال تحصیلی را به صدا درآورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/692433" target="_blank">📅 21:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
انعقاد یک توافقِ مطلوب ایران با دولت فعلی آمریکا، یک رویا بیشتر نیست
حسین مهدی‌تبار، پژوهشگر روابط بین‌الملل در برنامه سیاست خارجی شبکه سه:
🔹
در حالی آمریکا و ایران گفت‌وگو کردند که ترامپ کشور ما را به نابودی تهدید ‌کرد. این تنها یک رویاست که توافقی مطلوب ایران، با دولت فعلی آمریکا صورت بگیرد. ترامپ در هیچ دوره‌ای نتوانسته یک توافق پایدار با سایر کشورها داشته باشد. اگر امکان پذیر بود، کانادا می‌توانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/692432" target="_blank">📅 21:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d2e663a6e.mp4?token=pPWuCS14IcHoMtM32ZfQ52vRoaInu52ScGsis6DmhwsjyzTvL2TOxv0lwgoPBNlVPEIMoCKqLkvpC66t6aUnKO8hU42EBSUexpGQz_vKiXD-bHPaNBH_ZVDL9eLyN-g2oUxxYsad2kxdavsnfVP0FZXv2gTCBvHVTSNiCmuY6HPzS_rXE9_Re1MhrMP-2a_Csuthf5NmKD3C7RmcZFCgOei6m5n5mihIo0negrgIiCEqTJQnYbsXuYJ5BzBw6u1Haa-4FG9MDUJIHIO6YdSPeW5e7FNs6zHNTTC0dWpiJPA6PUb_hG8qHf1DTvkN2CvTzrhDnuzsAdosHdo_FxmyCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d2e663a6e.mp4?token=pPWuCS14IcHoMtM32ZfQ52vRoaInu52ScGsis6DmhwsjyzTvL2TOxv0lwgoPBNlVPEIMoCKqLkvpC66t6aUnKO8hU42EBSUexpGQz_vKiXD-bHPaNBH_ZVDL9eLyN-g2oUxxYsad2kxdavsnfVP0FZXv2gTCBvHVTSNiCmuY6HPzS_rXE9_Re1MhrMP-2a_Csuthf5NmKD3C7RmcZFCgOei6m5n5mihIo0negrgIiCEqTJQnYbsXuYJ5BzBw6u1Haa-4FG9MDUJIHIO6YdSPeW5e7FNs6zHNTTC0dWpiJPA6PUb_hG8qHf1DTvkN2CvTzrhDnuzsAdosHdo_FxmyCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صورتحساب مجمع عمومی سازمان ملل در نیویورک
🔹
در هشتاد و یکمین مجمع عمومی سازمان ملل چه تعداد نفر حضور داشتند؟ هزینه این همه رفت‌وآمد، امنیت و برگزاری را چه کسی پرداخت می‌کند؟
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/692430" target="_blank">📅 21:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سهمیه دو جنگ اخیر برای کنکوری‌ها تصویب شد
دبیر شورای معین شورای‌عالی‌انقلاب فرهنگی:
🔹
سهمیه ۵ درصدی ایثارگران برای کنکوری‌های آسیب‌دیده از جنگ‌های ۱۲ و ۴۰ روزه به مدت دو سال تصویب شد؛ این سهمیه جدید نیست و در چارچوب ظرفیت‌های قانونی موجود اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/692429" target="_blank">📅 21:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c056bb91b.mp4?token=ctokdT2hXIO3FKN57ivS6HTeQaBJtKxH02N8qvhd7HV6jqxaqCTqwRwbQnZz-KCO4lu8iOX7xdEGr1T9DM2fdSCK65lSIOJVzlnMwaciWtvm_5tr7hayFM7a2rCUR79i9M0JS6nWyH-mq1val9QONs5sPkksDFFjAv5FJzRGDBi330T45-K7EI6rvPkxa1iWGnZkS_xI77Vartfci9OEmpSrXQMcmCMppH3xTPGlAc4T9BobWbIpBUsSYmdURhADMXbO3zdT953GW6u89DRJAfpMSqSTZTU0WwG-t1G0caeA540NCaWaSc71QihbOuc0hM8MKmhxLI02uZ7KWZX2XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c056bb91b.mp4?token=ctokdT2hXIO3FKN57ivS6HTeQaBJtKxH02N8qvhd7HV6jqxaqCTqwRwbQnZz-KCO4lu8iOX7xdEGr1T9DM2fdSCK65lSIOJVzlnMwaciWtvm_5tr7hayFM7a2rCUR79i9M0JS6nWyH-mq1val9QONs5sPkksDFFjAv5FJzRGDBi330T45-K7EI6rvPkxa1iWGnZkS_xI77Vartfci9OEmpSrXQMcmCMppH3xTPGlAc4T9BobWbIpBUsSYmdURhADMXbO3zdT953GW6u89DRJAfpMSqSTZTU0WwG-t1G0caeA540NCaWaSc71QihbOuc0hM8MKmhxLI02uZ7KWZX2XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز درباره ایران در سخنرانی سالانه مجمع عمومی ملل متحد: آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. #Devil…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/692428" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692426">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fbdf5753.mp4?token=LuoESw_ix7UCnCOQ7-CNVQnr1IhPahrTyXnPvQPFf5100cI2e9RspDTos2fJxxGaGgo81Bw7ORbjqv-15x3afLz3B75-Up_wFFsMMQU0R0ORYx3N7AJRbLvwHu2FLI_lw9MtFwkr3WzfcTPG7rjRveBQxR5VpG9evM-FgsqcGrH-QLdyKnYPbk-zaTwTiaUwJarqdT5CaqUaXuqtkmuaMKKXSO3oTnB0iwuh5MKcNmTzeeks5ijcS8GIrXspSz6qP_PqCh8fEu56qGJP59u63jBhHg8l2GfrIKfRXzgPMG4mY2FVT2JhYih0LFSR0O_FB_1rnpAse7sqYMfUNEZCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fbdf5753.mp4?token=LuoESw_ix7UCnCOQ7-CNVQnr1IhPahrTyXnPvQPFf5100cI2e9RspDTos2fJxxGaGgo81Bw7ORbjqv-15x3afLz3B75-Up_wFFsMMQU0R0ORYx3N7AJRbLvwHu2FLI_lw9MtFwkr3WzfcTPG7rjRveBQxR5VpG9evM-FgsqcGrH-QLdyKnYPbk-zaTwTiaUwJarqdT5CaqUaXuqtkmuaMKKXSO3oTnB0iwuh5MKcNmTzeeks5ijcS8GIrXspSz6qP_PqCh8fEu56qGJP59u63jBhHg8l2GfrIKfRXzgPMG4mY2FVT2JhYih0LFSR0O_FB_1rnpAse7sqYMfUNEZCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌اساس روبیو: تصمیم‌گیری نهایی در ایران در دست جریان‌هایی است که به صادر کردن ایدئولوژی انقلاب خود باور دارند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/692426" target="_blank">📅 21:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692425">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h68PqXXBXwCTR8hEKceF1GW-1ElgtHo4ROJ9pEpnY-uA5c2AQ7cCvlUmdC2GrekQE7e0kd_VYVq6Eswk5f1UISpCod6C8Ajvr3bBTuzxd81fPJUyixMAKaQJLCGfyqM8yr-pmRnz_T5P8eHb7ZR7DFjEiFfBMBz2JeOo_zUyhRp6jh8x254uwOGpG3xrLCJQ6R_cdFcUi71ucfqaD1AuJiKzEBgaz6Hs4kxecv11CYJdoQ2Vl8FNy1aFREt-5u3eW9IaBm8jF7ELwx6Mlqsds8ZsB9_N2RZ5YClmAK9XakRt9E9N6Wl8T-iA9YTafX3tG4xoliuGYC0CQpU13ZYSAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از صبحت های دبیر شورای عالی امنیت ملی نفت مجدد صعودی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/692425" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692424">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKxZ1k15EeV_7KDVlejouPFFiw8Lcj9vp14XbqUk7TxV1mdqe8g4NvJHzec-7xzmwaYjlOOXH1IOBPzD6qV-gWaBt9HZ3wEHElGoKzhBG4Z2bSN1l1WqYLld2J-mFmap5xzlmKtxkUUFql8LDHs-94cBlzCzLX8OQhL7twK9hfJEavah55O6wxFpq0qiAo3wUQ6s8E_iP_ciEJ9tZTwk_0PQ1JDV2zOTcfp7_ZC5vMyH-OzCOx4IYHU7EK8s5idOJp6cCjwSsx8e2ayVkHK7pw1bSoU4ygJLWp_vHYYsjHN0sPSIaFxhYiBskvWKzd2CwcoNrnvmH5kLirR0zTwHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آپدیت جدید تلگرام، میانگین زمان پاسخ‌گویی کاربران به پیام‌ها در پروفایل آن‌ها نمایش داده می‌شود؛ از چند دقیقه تا چند روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692424" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692423">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
الجولانی: به ترامپ گفتم چرا نیوجرسی را به اسرائیل نمی‌دهید؟   رئیس‌جمهور سوریه:
🔹
در دیدار با ترامپ در کاخ سفید، پس از اظهارات او درباره تعلق بلندی‌های جولان به اسرائیل، به شوخی گفتم: شما مالک جولان نیستید که آن را ببخشید، اما مالک نیوجرسی که هستید.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/692423" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
خوب نفت می‌فروشیم؟  وزیر نفت:
🔹
خداروشکر. وصولی فروش‌ها درحال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692422" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692421">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeZxyd3KE6BTUKF4bSblRHxHbs1pukQKWqwCEyZeh7zVtUs_DF3plIccQBcC_I0wDcA0EE6anij54DIDG7OA7ldbVHoXIApV2PaJSDoeFY7YIvaECQSm-tpCPJv4WRSl8XlCmFrsItqpvIs3320Z3Y8ctjouhTxRWBRe-pZCEZFANa-mNkb_xnMcKKIlXpslqLxbwJ3YvUIV51FLHeomnEfJuKUbgi7eJQKTNfqpGSudz2GNFyDRG6db3GO6Ust10aZq05Ui4lKm6skm6B2Oe2PE13zaJVXgOMqYbtjIFztf47iqvCmbKytWDTb9HP0dB2iyTqSfdgjQKWK1v8WyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختصاص یکی از ساختمان‌های آبفای میناب برای استقرار و فعالیت مدرسه «شجره طیبه»
🔹
مدیرعامل شرکت مهندسی آب و فاضلاب کشور از اختصاص یکی از ساختمان‌های آب و فاضلاب شهرستان میناب برای استقرار و تداوم فعالیت مدرسه شجره طیبه در چارچوب مسئولیت اجتماعی این شرکت خبر داد.
🔹
هاشم امینی: با توجه به ضرورت آغاز فعالیت آموزشی مدرسه از ابتدای مهرماه، یکی از ساختمان‌های آب و فاضلاب شهرستان میناب برای استقرار موقت دانش‌آموزان این مدرسه در اختیار اداره آموزش و پرورش قرار گرفته است.
🔹
این اقدام در چارچوب مسئولیت اجتماعی شرکت مهندسی آب و فاضلاب کشور و با هدف کمک به تداوم فرآیند آموزشی و فراهم‌کردن محیطی مناسب و ایمن برای حضور دانش‌آموزان انجام شده است.
🔹
شرکت مهندسی آب و فاضلاب کشور توجه به مسئولیت‌های اجتماعی را از وظایف خود می‌داند و تلاش می‌کند ظرفیت‌ها و امکانات موجود را در جهت رفع نیازهای ضروری جامعه، به‌ویژه در حوزه آموزش و دانش‌آموزان به کار گیرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/692421" target="_blank">📅 21:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
برقراری پروازهای ایرانی به امارات، ترکیه، چین، آذربایجان و افغانستان؛ بغداد پیشرو در تحریم پروازی ایران
🔹
داده‌های فلایت رادار نشان از آن دارد که پروازهای ایرانی به رغم تحریم‌های امریکایی به کشورهای امارات متحده عربی، ترکیه، چین، آذربایجان و افغانستان…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692420" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پزشکیان در نیویورک در هتل مستقر نشده است
🔹
پزشکیان در سفر به نیویورک به‌جای هتل، در محل اقامت نماینده ایران در سازمان ملل (رزیدانس) مستقر شده است.
🔹
این اقدام با هدف کاهش هزینه‌های سفر، برای اولین‌بار توسط یکی از رؤسای‌جمهور ایران انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692419" target="_blank">📅 20:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fbd948ad.mp4?token=bSednMXXaSUIL6kZZcE2k9xvE4dsWeuW1kgES6OlpzyUzfUCKMUY9ks4NTsl5v0H_QHNnUza2A3mOO_Flli8SUkfES5hV9jehk6jGjOhgB10Z60TsGtOWIIDwOVasOH1_GW429vVklDFUXtnXsaOocdlktd179Zi31IxYV92yHC2glwn1vuNjkY1ug9Xi-6-B7iuxPCiGaaQPZuZKIcqy5UpHdcprUyMh_OWJU2MHVH7VbmyYF0An9_WJTVXusW8Syy2y-wQbvj4jBnJhub-0S3yhHJj10eLQ7FFZxTe_RgW7_1RraaLW_hs6GT4NizUiXUsLBVgt7-8qzNXOUjchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fbd948ad.mp4?token=bSednMXXaSUIL6kZZcE2k9xvE4dsWeuW1kgES6OlpzyUzfUCKMUY9ks4NTsl5v0H_QHNnUza2A3mOO_Flli8SUkfES5hV9jehk6jGjOhgB10Z60TsGtOWIIDwOVasOH1_GW429vVklDFUXtnXsaOocdlktd179Zi31IxYV92yHC2glwn1vuNjkY1ug9Xi-6-B7iuxPCiGaaQPZuZKIcqy5UpHdcprUyMh_OWJU2MHVH7VbmyYF0An9_WJTVXusW8Syy2y-wQbvj4jBnJhub-0S3yhHJj10eLQ7FFZxTe_RgW7_1RraaLW_hs6GT4NizUiXUsLBVgt7-8qzNXOUjchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرزند سفیر اسرائیل در عملیات ضدصهیونیستی مجروح شد
🔹
رسانه‌های اسرائیلی گزارش دادند فرزند سفیر اسرائیل در واشنگتن، در عملیات اخیر نزدیک رام‌الله مجروح شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/692417" target="_blank">📅 20:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617c3cf0e4.mp4?token=Nv7Af1kX4HqxPcvQ-K55Zvwx9ZmpYg9DNziwZVhQApluCdXz-CKDEOjUV9oJIOPuYHy9UampQfT7oMbWwkTmWIL5zdbrm0m-0Yoi645KU_uK2GSV9XNUKBI7WDyN0RZUCNeqz2a_Xes9hI11Tjx20swE_s2Mcp7Mmsh3Kr1u42qXFZlHaA92ZR14f52OunsmaXP2vKkAWlzMuMJfvRKILekR7kkij3QWx8rSpggTeFk2gnuC4wzCtlvUl6NHDQ-31ByrJ7lH_6dgOUwIsV0QWwvsvK6oUkntR1pc9KLp3GxW7ZvNzxnin2vltxUk7KtsYGjdhuGoqjlcZx2cPeBIyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617c3cf0e4.mp4?token=Nv7Af1kX4HqxPcvQ-K55Zvwx9ZmpYg9DNziwZVhQApluCdXz-CKDEOjUV9oJIOPuYHy9UampQfT7oMbWwkTmWIL5zdbrm0m-0Yoi645KU_uK2GSV9XNUKBI7WDyN0RZUCNeqz2a_Xes9hI11Tjx20swE_s2Mcp7Mmsh3Kr1u42qXFZlHaA92ZR14f52OunsmaXP2vKkAWlzMuMJfvRKILekR7kkij3QWx8rSpggTeFk2gnuC4wzCtlvUl6NHDQ-31ByrJ7lH_6dgOUwIsV0QWwvsvK6oUkntR1pc9KLp3GxW7ZvNzxnin2vltxUk7KtsYGjdhuGoqjlcZx2cPeBIyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزند رهبر شهید انقلاب در مراسم بزرگداشت آیت‌الله شبیری زنجانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/692416" target="_blank">📅 20:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692415">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi1omo2SqTtPQmulStXdNjHwuXrUWC7ML-q5WEH9Uh8bHFAX4h1dnR8xvEs5-MblcX3VbHRC17iBb01otLwNO2oz2pyDOFRvRm69zB9cBWGrMBud6dA-Ef2_eotCi70V1s7J_RRB8NV1CuPzZ_34UlWi6wNvOWPfqGaBbh3jvJvC7Ag_JdHp5jLuwO5LD_CtlNMuc0u6GERiuc-H9w7Gt-r-RBw8RZd_AS9EjOUAeH7FrH3FSlfr2ntr87pvu5eZCye0xhzeOxMNfOcFwUdVZN_-sSRYNNEnvmiCN4bfff8PbJow5sv2VfoWdTeAprQlO_pOPUkw_BOEA2M2U9huRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هلاکت سه تروریست در سراوان
🔹
معاون امنیتی و انتظامی استاندار سیستان‌ و بلوچستان از درگیری و هلاکت سه نفر از اعضای تیم تروریستی در درگیری آنها با نیروهای امنیتی و نظامی در شهرستان سراوان خبر داد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692415" target="_blank">📅 20:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692414">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga_bGDJZanptcVLUCVc-deivpP70hzJq9rtfD9km5iiBQoHC1xGDkaWSauZ1OMSbN8G5adLWECjvdKt1B2baC2-f2_MEO9VuGx_nYf40Yd0aIpuCL5XFPkK9BZBdhaIdy-szs9QYLdYuK8zufoVrAGDMIh4U8WbwpgbvXP6fhzacB6NvVfgiP-_v-gGmSeopsrJ7iyS0oZ6Us-lId1t6JPrglcQlMVH_Pl5NeSQ4vhlz4LyQWiE_F7ME4BxEW6wO-gb6gpn1amV9dZYlaa9kiJp0FHjRQFzKXcZn1KTcrJ72aPl1pTZY3xusqCgCG78TOqUkbwkMF4V0YL0S9gjubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | جشن فرشتگان
🔹
همراهان گرامی خبرفوری، شما می‌توانید با ضبط یک ویدیوی کوتاه از دانش‌آموزان خود با لباس فرم مدرسه، در این پویش شرکت کنید .
🔸
از کودکان خود بخواهید این جمله را بیان کنند: «کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
🔸
ویدئو های خود را به آیدی زیر ارسال کنید
👇
#جشن_فرشتگان
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/692414" target="_blank">📅 20:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692412">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0orxN9TgdmzDSFtRsNupzaJh1wWPpN0_lqRTD9EKeclLwumuNXW90zkHosUEzxpcVGOk_9gmpqkgX4oN4pCkMA7K7RJYLpC2OpSrD8oNUe-JBoX5_M1QQRcf2LP_eUFL7yrDOkBgkkErjoTS6ym8LVLgQABx5JfJ-_5iNHUx2EaksZjyYe2-eZ0YH4S9PmrPI5IYo7sKZw0rOekZs4V0YfHLSTkpeh0lLiquG0zfFUGSbAFQrYsgrFwAFGurSpzwX7FLLNPW7iqw1lqzUgjiLO7d4Ui5--mPlMynQfTo0lXNZIq_vh8k2EYY2wpThn-61yNWWOURBl01ffw4ItAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور دختر و داماد پزشکیان در مجمع سازمان ملل در نیویورک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/692412" target="_blank">📅 20:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692411">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پولیتیکو: آمریکا در حال آماده‌سازی طرحی برای ممنوعیت صادرات گازوئیل به مدت ۹۰ روز است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/692411" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692410">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418cebf273.mp4?token=uqHR9-ZZOQC_sRuwzRjfitoAe7JECoMkMYaN6qs1vZHTib2wIQ7pxZJN1gASSNUlPtnBCmS1dV25ZfhPFFq_L7XKB4WLJ7t_5M8uw3y_d5fk1xG9l6_P6mVosjTn2MT58soimshrnv8rxSekT45-SV1RkMXqCRuJXyFEeM02zPdvqM6uD0LtZavfz-qypiKTgq8NHOpf2hpkzdFjO0wXvwsg2wHC08gNfuAPLu1CC8Z-He7rWhyXDIDa7dJc4KmM6yknMkwZfI4i91uDPClmA0pWTPL2I3oD9QLMGf1cvMjoMX5dFgQRhHZBJZMuUfHENUqfi5w_2VOnJP8_BZsA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418cebf273.mp4?token=uqHR9-ZZOQC_sRuwzRjfitoAe7JECoMkMYaN6qs1vZHTib2wIQ7pxZJN1gASSNUlPtnBCmS1dV25ZfhPFFq_L7XKB4WLJ7t_5M8uw3y_d5fk1xG9l6_P6mVosjTn2MT58soimshrnv8rxSekT45-SV1RkMXqCRuJXyFEeM02zPdvqM6uD0LtZavfz-qypiKTgq8NHOpf2hpkzdFjO0wXvwsg2wHC08gNfuAPLu1CC8Z-He7rWhyXDIDa7dJc4KmM6yknMkwZfI4i91uDPClmA0pWTPL2I3oD9QLMGf1cvMjoMX5dFgQRhHZBJZMuUfHENUqfi5w_2VOnJP8_BZsA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو مدعی شد: عربستان شریک راهبردی آمریکاست و به تعهدات دفاعی خود پایبند می‌مانیم!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692410" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692409">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای بی اساس روبیو: نتیجه انتخابات میان دوره ای آمریکا بر خلاف تصور ایرانی ها تغییری در اختیارات ترامپ ندارد!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/692409" target="_blank">📅 20:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692408">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f3a12635.mp4?token=io5xLV4SzfJSIzMJDpHyW9Y1eVQY-noLJ80U3GCBjPHDpsW8p0rZrx7TEGcAoqvlDrYv812Y1qqEi3qkV4EiIPYV7P2iFSM_ctz961dB7LSGR6N_dExG1-tMmBPwdv7jE4-XhnPVVGm7Vd0hBHNgqWbQdv2cgFb7YftC739LQwlerUJAVUNGpxzYQcSnDhyGOd3QeEXj6oUB-HRPNcEydcwUurebcZZM3hXSAAtA8h6ZPoXx8pRHq_iC2avwNnC9JKm87D99KP_yNzRf5oZLdcfYU7jks6Z51JrF-3v8vow3Zg18dqAN2oRLpGcm4Lh_cyFufzBkW2TjypR6IpN_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f3a12635.mp4?token=io5xLV4SzfJSIzMJDpHyW9Y1eVQY-noLJ80U3GCBjPHDpsW8p0rZrx7TEGcAoqvlDrYv812Y1qqEi3qkV4EiIPYV7P2iFSM_ctz961dB7LSGR6N_dExG1-tMmBPwdv7jE4-XhnPVVGm7Vd0hBHNgqWbQdv2cgFb7YftC739LQwlerUJAVUNGpxzYQcSnDhyGOd3QeEXj6oUB-HRPNcEydcwUurebcZZM3hXSAAtA8h6ZPoXx8pRHq_iC2avwNnC9JKm87D99KP_yNzRf5oZLdcfYU7jks6Z51JrF-3v8vow3Zg18dqAN2oRLpGcm4Lh_cyFufzBkW2TjypR6IpN_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهکار جالب و ساده برای اینکه هوش مصنوعی چهره تو تغییر نده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/692408" target="_blank">📅 20:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692407">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
کانادا ۵ مقام و نهاد ایرانی را تحریم کرد
🔹
وزارت امورخارجه کانادا بدون ارائه جزئیات مشخص، اعلام کرد تحریم‌های جدیدی علیه ۵ مقام ارشد امنیتی و ۵ نهاد دولتی ایران اعمال کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692407" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692406">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: امشب راهی نیویورک می‌شوم تا با دروغ های وحشتناکی که علیه ما گفته شده مقابله کنم/ضمن اینکه چند سوپرایز هم در راه است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/692406" target="_blank">📅 20:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692405">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d4fa3068.mp4?token=fbZuQZEoa_YMJdr7pQq0atUEkPvKA1UqZsrNe7413T5qRXHt42bKRaT1ia_G5T7onpsLGgHWeWPGXflUTQRUrFb4fe2cwGkKuL8HDsbLJouHkivYxXw3zBcrICcBfql-6ttsSEG1nUjig0_mSyolDc6edcA76jy4f8wDHtPPrjH-oIUzbKRhXzZ_rGdm4v4zE-cYVhFxC-Y6PTiPm3GlTnZEOQP09OEK5TvrlY3WItKC76G2b6zopHhmOaGPsLQqhgt1ZXAiE6axn8q_KXzdqNhC8b_clh7V4smCwzRZhbTbJkJZLeB5Tm3Tj1QeNcO_5W-SFIp3-ZZCWDHOXl1VPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d4fa3068.mp4?token=fbZuQZEoa_YMJdr7pQq0atUEkPvKA1UqZsrNe7413T5qRXHt42bKRaT1ia_G5T7onpsLGgHWeWPGXflUTQRUrFb4fe2cwGkKuL8HDsbLJouHkivYxXw3zBcrICcBfql-6ttsSEG1nUjig0_mSyolDc6edcA76jy4f8wDHtPPrjH-oIUzbKRhXzZ_rGdm4v4zE-cYVhFxC-Y6PTiPm3GlTnZEOQP09OEK5TvrlY3WItKC76G2b6zopHhmOaGPsLQqhgt1ZXAiE6axn8q_KXzdqNhC8b_clh7V4smCwzRZhbTbJkJZLeB5Tm3Tj1QeNcO_5W-SFIp3-ZZCWDHOXl1VPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
نتانیاهو جنایتکار: امشب راهی نیویورک می‌شوم تا با دروغ های وحشتناکی که علیه ما گفته شده مقابله کنم/ضمن اینکه چند سوپرایز هم در راه است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/692405" target="_blank">📅 20:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692404">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2389f63da.mp4?token=o7WVd6tXx6kmh9o0xfE3glHgZY3694SPirEcJj8fyZGMMASQQIO-F9STpx0CjlgpSU3HVDgqzICjeRXHvqPR9XHJxEsMtS_dIVaIGJQTSax-uTwHvaJXa86jaVkpQALu6WmP68t4HdculwWXzTVhc1p3X01gKLAZF61TUgdZRK1uZmXeiqnVPV7rLRM2nW8QOmVHGH6uxjJYbcA2NSegT9X10_qPDBx-Nwn--7-xKptVBZxR4waRxGintCYHc4UQzkqBLGDS5TNxvaXcsfJ_BUHmDcB1nHBcJ9-t3ZOFf5tD8Ow0b9reD4BapSN6awu-Hnj-d4jiHtXJfTwy5_cb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2389f63da.mp4?token=o7WVd6tXx6kmh9o0xfE3glHgZY3694SPirEcJj8fyZGMMASQQIO-F9STpx0CjlgpSU3HVDgqzICjeRXHvqPR9XHJxEsMtS_dIVaIGJQTSax-uTwHvaJXa86jaVkpQALu6WmP68t4HdculwWXzTVhc1p3X01gKLAZF61TUgdZRK1uZmXeiqnVPV7rLRM2nW8QOmVHGH6uxjJYbcA2NSegT9X10_qPDBx-Nwn--7-xKptVBZxR4waRxGintCYHc4UQzkqBLGDS5TNxvaXcsfJ_BUHmDcB1nHBcJ9-t3ZOFf5tD8Ow0b9reD4BapSN6awu-Hnj-d4jiHtXJfTwy5_cb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوب نفت می‌فروشیم؟
وزیر نفت:
🔹
خداروشکر. وصولی فروش‌ها درحال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692404" target="_blank">📅 20:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847dcb1767.mp4?token=EIkbERsoWsGUB4-OCvKy8Tch9h5teDvtpQ6AvCBqIMEBqGzxz_6E5Q8A8lqHaUGJG3TBMauZG1iEtviPcncouVgRu6eqkyhAhudZoyo3eXyHhR45qB3fSaYy0ph1-02rHDa1FAbCw18EUWdFMgRkGZtzpDnw2FxEjoVkZYTiITkOERL-68ipuN2WjfjwRzySJl-v-TFBuocI2u8No3qMk7k6kCximR06Mm-2dZGrr2Z2DtvlXyedVfunyJSuGJfOb918pAhZM6us2lwOZmUt_GX9iitbT3EHJ68XXJNXqSk85wBkYP3cPHDv27JWpnUTvghdqcQn9_eDuB8f_HeWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847dcb1767.mp4?token=EIkbERsoWsGUB4-OCvKy8Tch9h5teDvtpQ6AvCBqIMEBqGzxz_6E5Q8A8lqHaUGJG3TBMauZG1iEtviPcncouVgRu6eqkyhAhudZoyo3eXyHhR45qB3fSaYy0ph1-02rHDa1FAbCw18EUWdFMgRkGZtzpDnw2FxEjoVkZYTiITkOERL-68ipuN2WjfjwRzySJl-v-TFBuocI2u8No3qMk7k6kCximR06Mm-2dZGrr2Z2DtvlXyedVfunyJSuGJfOb918pAhZM6us2lwOZmUt_GX9iitbT3EHJ68XXJNXqSk85wBkYP3cPHDv27JWpnUTvghdqcQn9_eDuB8f_HeWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بی اساس روبیو: نتیجه انتخابات میان دوره ای آمریکا بر خلاف تصور ایرانی ها تغییری در اختیارات ترامپ ندارد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/692403" target="_blank">📅 20:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692402">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون اول رئیس‌جمهور: امیدواریم در روزها یا هفته‌های آینده در زمینه افزایش مبلغ کالابرگ به تکلیف خود عمل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692402" target="_blank">📅 20:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692401">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای
ناتو: بدون اروپا جنگ آمریکا علیه ایران غیرممکن بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/692401" target="_blank">📅 20:18 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692400">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رئیس‌جمهور جایزه بگیر آرژانتین: برای جلب رضایت نتانیاهو ایران را محکوم می‌کنم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/692400" target="_blank">📅 20:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692397">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78297f7d8b.mp4?token=Xyz0736ngLgyJuK7b3D4q2eR1Hh1y-jh7lBWm0etf6AZXfLvSqspKhwm3dYcFypioNgVEimWPRP-usjtBNUhQ_EOsShRIScXeS6EFK8oosPWAGD7TCkxyISNRaWsVEgIJp8-TGBAy6LYcK1lZzSWBvxoXCXijIFiyeKXqa0oBletQ6tMZiT_MxrnqjpXpDJB8DU_iNifvUJLMl4m52ENlzJ4gj8sgMMUK52grwHyYJ1wueEsCqObfQGCOiyZye7Rq-i42wcZqYTqZg-USwgJ5a5S76uNe_kUhVQ3Q0Kt05UmpknYt9GcL-LGX2UjwkEF3mIr8LGituv8ts6WgN0ZFLXBBwPrjymxW7X9cqARmWSlrNVsbncQQ1NffDkXVV7e6oZzEiqPV8YIcCyFvENeuRShonPoVZK2qKSWCjT5oru6Na4xvrwuGFssRshOHhfTeDhmb2Q9czK7uRXzOLZBO1in2qidJJKV9GnZrLVGhjQdJbbxUpMHA_VPj-wlZa4cBZXm6_WUkxppnPkxsK8EBznTZUhS5nq5Hl70JeXxNsoPfwIjATwtjQAEPtLecYOM5roSPcknsICkqzcD5H4lcMGgRa8Mo-cIDLeR4lqsIBFN2vVOn-kYgOyjMw3aY1QGmBebtn8yMJfiNcd-z-gZGS9_EgTvhMoqIi_A2b3CtJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78297f7d8b.mp4?token=Xyz0736ngLgyJuK7b3D4q2eR1Hh1y-jh7lBWm0etf6AZXfLvSqspKhwm3dYcFypioNgVEimWPRP-usjtBNUhQ_EOsShRIScXeS6EFK8oosPWAGD7TCkxyISNRaWsVEgIJp8-TGBAy6LYcK1lZzSWBvxoXCXijIFiyeKXqa0oBletQ6tMZiT_MxrnqjpXpDJB8DU_iNifvUJLMl4m52ENlzJ4gj8sgMMUK52grwHyYJ1wueEsCqObfQGCOiyZye7Rq-i42wcZqYTqZg-USwgJ5a5S76uNe_kUhVQ3Q0Kt05UmpknYt9GcL-LGX2UjwkEF3mIr8LGituv8ts6WgN0ZFLXBBwPrjymxW7X9cqARmWSlrNVsbncQQ1NffDkXVV7e6oZzEiqPV8YIcCyFvENeuRShonPoVZK2qKSWCjT5oru6Na4xvrwuGFssRshOHhfTeDhmb2Q9czK7uRXzOLZBO1in2qidJJKV9GnZrLVGhjQdJbbxUpMHA_VPj-wlZa4cBZXm6_WUkxppnPkxsK8EBznTZUhS5nq5Hl70JeXxNsoPfwIjATwtjQAEPtLecYOM5roSPcknsICkqzcD5H4lcMGgRa8Mo-cIDLeR4lqsIBFN2vVOn-kYgOyjMw3aY1QGmBebtn8yMJfiNcd-z-gZGS9_EgTvhMoqIi_A2b3CtJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: قدرت مادی آمریکا بر آنچه انقلاب اسلامی دارد، کارگر نیست
۱۳۷۴/۱۱/۲۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692397" target="_blank">📅 20:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692395">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1b9BlfN8vEc2VvHsr7Eqsr9B8cbverCoxOBi42F5FdClqWCY6KJ2AUArmxBYbiDDL4188wZrqeu-gH4zDK3zUo9PrEQHkgaLArrRKp9tcfWdlueCwUiNNsON3uv5k2s_v-p81ZQj90laOqjnjAAijIK2yGMj-vr6R7OnAX5N0VBmtLtvXinv1vuXUQumyK552VZ4EBgtOwcH7jEJU-8SKfl4tDYO-E9jDog7bn957nFxtaKeougyrKocjqGpPph3f5IvR5ZgElC54569w-67SXjgylFk9tuACYfZvR0jENIVx2jpfqAB6OLArkWHr1Etw4lGcNFWie-Z-sDoSbKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس‌هایی که پزشکیان به دنیا نشان داد چه بود؟
🔹
رئیس‌جمهور کشورمان طی ایراد سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل، عکس‌هایی از رهبر شهید انقلاب، مدرسه دخترانه شجره طیبه میناب و ورزشگاه لامرد را به عنوان سند جنایت مدعیان حقوق بشر به دنیا نشان…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692395" target="_blank">📅 20:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692394">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ایراد شورای نگهبان به طرح مهریه
🔹
صرف نظارت الکترونیکی بر بدهکاران کافی نیست و ممکن است فرد توان پرداخت داشته باشد اما از پرداخت خودداری کند.
🔹
سقف ۱۴ سکه برای ضمانت اجرای وصول مهریه ایراد شرعی دارد و باید توان واقعی پرداخت بدهکار ملاک باشد.
🔹
ضوابط نظارت…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692394" target="_blank">📅 20:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692393">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL0Hr8YvhIZmJftxAtJKVYyBP8_q1AeGGV1L5OzcuT-SSHyYl7ZuMX-sHZSKD_nDZLmpW71yhw-Dc8e0zH3uAZalkRDLfw4W9lyrvVWYl45SxpydzUmY3RCEM2eVhTQbzLU5LvdAtLQczBJpeSYIl3lEgIHVtOlMI_8fuWHs7vxddW5lfh1fBoPza83CNsfxuBHkJCGUhPJnnBkf0taOR5mEUIWHhZ3fzQd-Sgc5lfF_fsR97VPR4GyeqBkFLM-NIOwcnLMX3sFy7cGwKlM0Iy-KGbBb_1BU64LZImY2W4AVb4vfd7RFRJqpCDzIDbHsRcyWYjmm2wxYmwhZ806KlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: تا قبل از بازشدن تنگه هرمز هفت شرط ایران باید عملی شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/692393" target="_blank">📅 20:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad434211e.mp4?token=Wruhk6Mtr5TGdnHrAMohb5vl7in4bTwAPCwm_1Qo3BpfFXOiiR6DIzkniM3WxVxMrB9q1i16NKrjKajj1NERAlWIPhWwyqXhf1e9nLzWzSfuktgTtKiGrUSFcYE_0CQauMHHgQgOjeoR0xoSf10zk-cM_gUW_inhEnHvNc6o9zn7u8Tbm7Ac6P8wCpm2lfrBnHVOqFXbH-m9bPCLHplQv_XEBJkEXyHwTCJSkAo9PmeUo7M9eHqxEP3Gsduuy9aVd_9f1DpHzvhdoxXhaWYjl7Bpepi2Ouzv88yqc51bbpQdKgntIpFF3cv1gxkAKX8sneHDnS5DjQVAcTc3L9dn2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad434211e.mp4?token=Wruhk6Mtr5TGdnHrAMohb5vl7in4bTwAPCwm_1Qo3BpfFXOiiR6DIzkniM3WxVxMrB9q1i16NKrjKajj1NERAlWIPhWwyqXhf1e9nLzWzSfuktgTtKiGrUSFcYE_0CQauMHHgQgOjeoR0xoSf10zk-cM_gUW_inhEnHvNc6o9zn7u8Tbm7Ac6P8wCpm2lfrBnHVOqFXbH-m9bPCLHplQv_XEBJkEXyHwTCJSkAo9PmeUo7M9eHqxEP3Gsduuy9aVd_9f1DpHzvhdoxXhaWYjl7Bpepi2Ouzv88yqc51bbpQdKgntIpFF3cv1gxkAKX8sneHDnS5DjQVAcTc3L9dn2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اشتباه‌های کوچیک باعث میشن مواد غذایی‌ات زودتر خراب بشن! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692392" target="_blank">📅 20:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692391">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8elSwHKV6CQsC4rIG8OFHQwFzlZ3Kf9fTxsIa44xQopwF4ea2MQUTiDWCQz9D4k0QGIkJne-if5AQAXpxujDKlUXh0FvucXHo-aGLpzybrxerJgYpLVExNiCAVImp2Aj5_MvugJeHLU_4pK8no4EwbxkP48xy1qA9mMYIO9XTghtFGTwHDBM5EgwWcNGqLFF8rOwJGwKr_0VC4JXO70ENVGCp5se_5HgirUlMm-KtZ3_oV6Erxc0DisfTG6rKnG4aGXtM6EDbdE3bH-txajYOiNhX9dnsXkwobCt7vcBMyxeDbMblCtiTyi0LvowWRygsrxPLYlmIxpBAyqAG6OTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">THEIR STYLE, THEIR STORY.
هر نسلی، استایل خودش را دارد ...
40% OFF
GERAD Kids & Juniors
تخفیف طلایی | روزهای پایانی
Instagram.com/geradofficial</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/692391" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692390">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
اوکراین: با آتش‌بس فوری و بدون قید و شرط موافقت کردیم
🔹
رسانه‌های اوکراینی به نقل از وزیر امور خارجه این کشور اعلام کردند که کی‌یف با برقراری آتش‌بس کامل، فوری و بدون قید و شرط موافقت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/692390" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
