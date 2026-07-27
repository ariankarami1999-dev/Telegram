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
<img src="https://cdn4.telesco.pe/file/GIS2peHtcf3msVut9FVfG1zY-UA2LjTa6JUZ1qV5tpXrEH5oqAFPEr-WMc5a7fBKGnYcwq2Y7Js2XcycUHWxmJ2pqg_qb7rwD2xjiiv3DDN-t4qMNYxcg172yxPQNYvQaAW62DtrFFuE7agDaFIkVr89Y5gXHD7I5almKt0FibHz_mB0wt0NVYt3ejNVDeHtOvKN376o9KEVmreOMjcJ_OnbZphqYtI3bfNIIEENlngi_LljvhMxhZoKMMXsEc7FMgDZilzsYt-AluJtyh0Gtsp-wqSF6DF9DsYKFNWIYG3vzqy1dXqluakcQ6yvHzqgWQwVJm9y_21S28uKfSohWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 208K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKVmcMAopjdnljZhl4s2F2zr13mEoV9HZvT_SWqi50v-biLT4om8_9jL3MmoTBm2SEPUGjwDPkYfInYBaKJglC-iXApQzlfN3GiRX_RQ1_c-0l-zKRwanASRk0WduLdKbGe4f1z4kWcrxBVDypdgjuqvJ9MZUe4T3aQl-C8ZvaFknqsjjOurOzlntyTfeNH8JdW34izHIfhkW6F2t6Ma3zUYbD3r8TxTR7joFJzwGlX4Df3ruWCtAsH84c-WbfPYyQpbKfCCbTfjSTQ2oyaeBNeIorYnHFe7Jv_0XGJ5z4rdpAZn5opD6VU0o-NOzJwQO29h90dbSntL_JP74nv8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7zRwTARC8J1ygNIdAG-bF4J5wJeMdlD2jFlxzFy7e6aYAH3DJUFCOjgWkOQSV9mdVUNikMYJZgHvtjvSTlGJF8H-iDgC9hPdqd9gmB9bYlgKsSjKCxPd0s1Fm6Aw47JltGAeeZMWAZ3lHwJj3W02yDPuE2ZdM0-aabSIXPFo2z5AYrRBSSdywa_M0kwtAt7UYjo6T9IzeQshT0WG7BTGzai8pGJl5IF0HB95keVeTNTierRH9AH-rZOYpZnRZDW4VLwpNDMU8KHxtyaI0-LYitOtBXTqdJTKEOt125Yty9oQ9hEXM3zSAOAsHMecQ0xNg29_CtFappj1QzC-dhGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dylM9x1moJakiwRpoVgQallw9R6bUIA5lFrgA4Q57pDHn3UWD8jcF6ZrbX2tMWlB1OlJi7yAfvtJRTiwQNlz5SM9tHXQP0KmqQLIqq_lmOHtABgd_CSYZolZPUec9_ZXPwsJnsGafqBg5xQqZasGZc9HTPvTUnOCJp7RxOBD3mAx-tZsxLMoS9HlOffdtPeb_VsBDr03nOiLys1C_jz1SNh50ujctVGcr04iWbtq8x6qsFO90g88VvC6rHE__Opmjoy7Ot4durQrtEcFOPcGQ6r3XGj-4uTGq1Y3-r8LT3Qq9wHtsqcoJB2x0S9P0aMxwTmfDHIr1vwwOBAluftDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okUspBLii1RcUEDHGWVQwz9VQa4TuG7UVeMvKY5NwoDw9mGwQl7IDd-ZHsei0s2mWlwtve92UbLVcysHy5I5aiH5TQkWlChMEGt4ZCJo3UAKORoOOxbrUJ3CxHuKDnct61U8cC6SCCftR67rKYrzrUnaFjaZmvnwT2t7rh4bKzkwS01GPz-CaPZy6q9xqLvzHMJGKcxfJlFWSS4TtZ26ueEIzbFXAd2XujEwL3nj0qYxPOeNIIIyCaYL0noxWXun3StlOWb56MEVd16HZIijbD1vtAY3zWZDPFpo2CqINy9_Ojw5sBbtkAUkKkL33W0FNqU-In8Dobjh4t3FhUkrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTEgOz6k7hkDaIC5UjvMowDjZl_jjH_2SqC30RnwgSkowoJ1cXy5_YW22MjqbL1X3JasZVEC_ngQK3-xvEem9ATei9l6Xb2egFIjYC-DLXnMlXNNM5KD4KnBsdboUs_v1gm6vRyUbcg97F_rnFu9paaN267L4hrBRghdEFW-CdyUhRZnwV1LxJQrcpDd2ldgzHNi73h4Rqh5oT9MZTPgtVZToBKqHnpYYHkQdamagIAqk7yqJkbfUuK7AtOwMD1fk666JfX9vKv_1gKgm3otkx_N07iFAgnDSEd8k78Ve1Kz5pbuzzrbYUHM07oC-IdMhOKabLEPqjRKn_FeY4afnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULSaJz_di_4on6BMnvE3fMfAohPqeDAKUbM6zCNVaOnQbLE6Vazl3shD74EP3vXHmm4s1NA1cXlZa4jvJZOMNb980cL3LC_FN5RcoJOKIaMQoMmTxx2xwVMiE4IkHgPvPkTPEAI7sL-cO9dx_aMERXBdFKjSehKVrd5zNabPZ0Ow9gl9KQUNKJxFPeTTYsm495yd2VZWnsbqu0Tu2Ec4eqsZ_1AgKcNTRzMNv0WYzhuAro0C2ABe1yo8vlNIuAOPjWUt3pq2Ihh3nwUZXAlMsLjjwQiRZ4f3gLmFUXrPK3y_Qal8fWADh5b-RGHMeog9SNidM7n1FRdBjSbCGb02Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=cOmy6tsbPAx8Sm2hbdPhbUr_WMUaPAH5RK_CP44Ia9f7kD-j_GyBQUBmFQpdssbMoMvOkhD6lW6YJrgziM-W-VQRmJQrC0mkSwufsBOndOhN-bM8TkmVMbGg6VtSkTVGY9_c49t-mWLsM4rhP0NW1T_9lsU5JvtocwPlJ2uRTwOHLqZIsD_1fTo7UOLzkIjyKZ5ST8g4p9-4U8E5_IFWhHOt2STfOltl7meROfhz_aYpHUB_bvQ8Cw5dhTZMwykfrjjPRaFRgw9ID6nkjKVlle4hsrtTNFQ14Hfrh3r8Jzcrt09zFOM_cdFIEmdJa3Nva9sCTRRCV-oxqJ6mJPGIew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=cOmy6tsbPAx8Sm2hbdPhbUr_WMUaPAH5RK_CP44Ia9f7kD-j_GyBQUBmFQpdssbMoMvOkhD6lW6YJrgziM-W-VQRmJQrC0mkSwufsBOndOhN-bM8TkmVMbGg6VtSkTVGY9_c49t-mWLsM4rhP0NW1T_9lsU5JvtocwPlJ2uRTwOHLqZIsD_1fTo7UOLzkIjyKZ5ST8g4p9-4U8E5_IFWhHOt2STfOltl7meROfhz_aYpHUB_bvQ8Cw5dhTZMwykfrjjPRaFRgw9ID6nkjKVlle4hsrtTNFQ14Hfrh3r8Jzcrt09zFOM_cdFIEmdJa3Nva9sCTRRCV-oxqJ6mJPGIew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUntBcC4ptxkuVkYG9AwWHDdpHV05cglzJAVa3lednL3VKfwhYgSU2ESUlFr09YWgmOMWSpfJ7_a30PmSVIHZV1mEQj6aVFi-urSiGX0JFfB33Y5RJ6nbdRk8X7of_DhTsi40egJ8DWsLEbPzUUgz0BGk1zKUV0JqApFT2n1LaQv5eUeYn5l1qM2wA0J3JSQs79_74JSmNSM1OYJVaa3WjoV8R9_Rf66bRvN4_uDhR_39zkqj6rxxXrAi1FXL0hDJnNvC9tKgwwczQ4xHwmv5W_6o8X6-XR3iKEbAzX4b0khnQtDKXOjC6femXnM9QyiiayVX4vTyJUR1ht-KcGHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUXPVenySKtuG0LqfEcgzP9cmzQ9cHEbJZo93u2SsBgkAH9NRWnOw9O8FxU1AYwFoWIsRUdfdyHqS1X-i45ZkSUEphb_7QXculQbG5_T8ZCL9PmrWrE8CIC5pJosVhBCJmn4JTlvUOaL9jPt7nrLWD7mhow6KosdcWSJQg7HGaPD2JTBzE-eALpdSAvFVo5rV68Pu95BywYuoG26B2UVsAXoVzfOTpLVDQ4LT6UdqXsxURKWi1gJz3kQR2M-Wm_EwVXln7b0FpV2FW2rCXCnEBn2ip-kRlKzt5dQ8ORVdqSPa2wLpRwYgr-7aLwip7ioP2W6uEFZ9SEe-e0BjXkeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYdGBYPq4wiQHKJ7uXofmow7zmebMMnraIUSBzLBehz542BIIw-B5vxunZCE-ku_BBnB2rNbaV0o1ZfVksaGZKq_irItcYlylqqo36DmaqzGWMx9spLKuxjNfcQTw3HpDCNbGsgukAzLG_B-4aX4AuLikc2n-bXYpOGcqmXBX1W9Q2MERPWzWt2Uh55IBG_0DXsYFzEY-cSkXq5fcWbLoVRjxiSTm4nAchr_zR04K5P9gofn6s-PU-z8ps4mHOYAjsu07KpPu9Qzd4UIuBxb9ASsDuyW-f-D3fdBGCNAxGcelK1ybJukrrEhuV5Jed5lNswd5Ylsx30NabF0i5nEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVjlfeb3N5EoHi7UBnMtq7UU_Vv-RvZqBFIQ7x9IlUas1NpfO4TWYTNPt8ZYYOPZ9ctbfVjN003mPJGJjK9mwwEqy_UMRFIhCz1qmRIeu4KI-NIneLPKP_T5TfOdetsqYdDG9IV3SyP5pYLPVH5Yax-0bYxYYu7WBIhXFrfG2Kz6xUHxH9JMnARWQj734_9pRvU15lzqil6ayoGqtDCBfBstHJ3WuCR6lKYCxPZ0AiBuZLleoU4g7iitF_17zWpNEn2PkQayaNE1ChLh4qr3U7ZF4kcIakCrZdWS1DZ5tqztdMckGOI27dgPN9H1vKupwmjIW46yyF1HTEFT6B_EeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ipx-rIWjX_9xngFFF1Cj26x4o3XGbCpZ2hrXUq8Er8zb4K_45u7ytlD6ywtLSYbAB6fUQBF5nR_0lXjIit7iI3stHLHkJUd57CLvHdk3PFJZYizulvvqaV-SJDpuQ8koqSBEBLxAJRLhaRaO7W2lpq55pLwQix5cfYH0ShFRFW4QT407tgNAGYi4DJ9yVTKyTU4hLaCEqeF80PfEuRnTFwd5Qc_c4wTcV60as49QUV7rAww6lizbuqQRYP6wnbzQ1HEERxekQg534ft8ehI8B6dkdCz9M8AKKUo4YxSZdxAemjMB6s8iAAngP1bjruKWTtMQ1f3FX0nDdK3ZfNL5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxZ1JARJmjWaMjZNGDPzspOwzDW6wicvkcqN4LNXwVeADVlVUo8IJ8LyRkB_1QE2zXY-1toOruT8dhJBH4wRZkG7gIbqt1-syTGdRAreiQDckQR1E3DkBy8vjuIHngTtvJ4M94MzgeA657Va2JXuBOKHvARv0ZhI6KzMYPWd9z7BndLnS7YRjXGSRlseRUDMpkrtD3KdrR8QxiJJgY6MwXx2c1ggYaQMMADvBk01xkwvhqmK5xFXUaeZvoMTwy0WAJfpJ-KZo19NYUOnqg3ymS6YneF044yv79fd4QxF5YAa_sLW_aWpEYrjazMrK93I5BgFfLCmNnOFS82PIM38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Xj7Q8Voji3JRs2xh0uQQPy7Q3GOL5pm7pXxiq3GAi9W70a3_hX5WJBXOb3I6Ap5zNjQGZ4drDVAG2KUPiUXTpywiHZFdk0CRmHHgj8TL2iIrSMUp_8RYIwO6Zk14p8SYvEZJOzZVqsg3OIRP1Hxi21oOhcFWi-eRs0a_1zkDCnH2fH1rLGwt_MR1MmrWUOlMIMNq6hwyy9zcI-rUyGslfBWhZL58PM43HD-UAcRYjuUw-KAJNYpHnvkqo4h20C24aAuZxWrYZoihC-zjaKP6ofyGdNGWLFfYUXvQQSGvQ_9435Ucs5L-smJbdB0IpMnJZ5she4Hl8NI2X-d4GRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuB7lbBDUdvslQ82_MJBvc5diuZ68_TD1tvmJYLgYp7V-HfNAn0Q2ajz-SrQjck-xor-RYkdfTr4orUx4SDpEfeatQmQiD0umw2OZbjtMBIqs8KwzYMi8rcrbcjtu5iT1VStXBkEf-EmAsCggwdYdP4g_L34FpHnlk5savrKyo4VjIPBmJv1jG1hb8iVY57c2FtLT7sNhw3vyviGdvrT4-3Cytayztrsj1D5f7Uggleg6DRwN_cxL6EPDw2tkVmAMrQBPkD4h_ILptcT7WUFuEAQgH6E5SkddfZ2ydxbxX7tiX4s7jISrJO80ijPgcAzJ6dZrm77By2g_zliEVq0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1QwFpiP4UuVdfOdjiePUhCFTTWY05LkNT3Q8saMiUO-eKpAhKKiYKxdyqjddpqHfMFIINOvQBcsH95I_3eJ2kDNwqK3UhssiH0DPZ2R3rlkbj3-ZX11EEucWOgObheEx-j-wQ1SOS2Xvvwg83luhGSi56o4Hl7sB4hZUGGcjNG05NELJpX6K3coLTMv_HMZSRo_0fGU9opM_sB9CJ0RoQmjIjTX2raPVRKnjXq811zEpD52i0SNFlKgpA7lWJAdO0mJ07QAHRJFLOQKRYIysHmak8SO7K2IgEcfVgEXNCFWfmb_ZaDo2fh_-auCVceZE7lcasBPDTf5OOtrRx0xBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAv5pyTEgCjhXaiz5qonsQlyKphgjz78Gswp1F_vaej0Ctqp-Ke8irFM8r5fqjh8O-01NLfNmNgCYKQr62_7NM6NYic1MSmt0gnUKzmq3J0iSCJuMh7KO3BQ08N3Glt216EZ6FijZCsaHhsuFYGo-FoeiZQAcM0txOISAmZ1DNxqlF_aMhDEUTuwUFdcI5pemR9WzwWqGBdDQzZ3sJinoppGWqMkv3t4aRae2rw9dal18a6TSguAg7h0i2jMDwiKD701cP1qXqllN2YYNRWWCVpPDMC0p3TIc8TVKFyVN9FF2IFE7AeBRoOPSPBfZr6C4yF_Sqpj0y96av4LrrE57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ggASoXfmKqNUbUp9VeH1wosNzP7NJB4N7DqaehGLb9r5vQBvP_KTfryS4pjqC9Zlh29ggwhCLAFCe0y4tUFbNBLKVvj-icu3tesJjhnMfItXGJSdllOglgrb3SJ2oEbRv4-MMsF_3yv3q3daflTwtcxgyVRPx81VZQpGtG4GGtp08-uoZfqzgxRLgr-4dMLe3agN1vvzurPjeA7-6G52q6dIYbr9UO82ox7bVuCE-C_xuCBozFF3BAv9otUq4bgrc9poTKW6L3PBZvBFZbxmywpH0I9F2P_pIP4dBGOBkSNT4CqhlJROsRuNirdO9YwhDlkaVi6IFgUMmiHKT-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUQojo29Qjyh7goRX43QFrtYe-BhWdCEMI70WeFHYS8yV0E0eo9R17zdzKsMQtP9AnonZmriybdcQIYM7qeXeL4Br57tXMHiXVAsvWY_N4WWRCl6qcLHREWosviBlt_XFJ0O53DDLFI8i14qds5Na-kKWR7btG7P90aMBwaE9fOIMVTBEhDhjE4rgQOv6xCX5k4MpTYy72e0KuCNLPTpPrmxqQSMfywCSbXRn23ZWillfNdrceNHOu-raXqVkE1Zt7mMdova2AoZzg1SdJhR2z1bzW9PCWlX_nSuWGfx9VDckdoKRZVr8T3WmcHhL0Aq-9-VKaOkn111HItnB9MqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ_G7wNHc1udry39uHR31WU65zzJmoBIAvUxzbMGX8_XaYrFEY91E3scf7AVPFAE68m3r1F_phfjq41vjWC3zoPgXqomHuQkno9n9dx7Uq5X_1RzPBqWj3NwOq2_-hoPi-J6k_gQcbKJ1C1vB_WQo1E5HDV_P0nVd7bViJmbHXughZKAnUBDnWSDoOUrGUS5TlcAQnINfNwWn2jetwYeaq6FnmWiuYfKuEQYkohXno3cdeU1T9znaw5GpHfjwVZuxbfXlbIdeElN2Qt28ghUF1H8KWZ4pJS_6xNZWZvoqPVqQA-1Ex79wZj0CJMRAqM6t87GzvcncImLwV1uBbIUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7n9IWQHVqb-fZcykEW1RLfZdaGflsUh2IpNM_12OG9IU1v-aMdzsL30XWsfdNNvq4WffiMewIsbpL9eemnAuWMEWQJdEvZMR7gAxqtMpc3KKMJ-CX_kPaFziyoqwbG626fW-4GapEOcTw3NxvcEbDssuKN0KO8q8e9oEwXX3g2ou8BrxK2r8VR3rBQ7l15Acg-aBG5vRQVHm9qHnNcS8YenEtbXbWH3lkva4scisE0nOVV6tAEzVtYTY7HqeIhT6jaYsW8adlH2VkasCQKpT8Dt8hTuJshSRMKDx5mwyq-AIj_JZHcwQSr0nAAyTgOtTWd2YPMFHSoI7r8xCOlJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ovhk9jHwVc6lVcB7PfHzBqxFmP9DqrFq8HXEFTkmnkLYVmQApaqGaIfLUmN-WEZSsmWd1uFd1wbwc9YRYL4W3X7vpa0ONt5egyv7eVt7C2rc9nr-DKWNLVCfy0oUe-oYmQZ6OBLbRrCYPsnBFqPk1IxST2pEtwwKmCPYr32tJwYitiyNLIpN79nychiFGmxvg0oNgIecL1hDKcB8OiYLciBsCZZPiwlmHIMbF76QINMupE_Nw4Oe9Altp_yl2au_2ij5KYoPaJC4BorQPICBFbvVpYxsaq_saXxlw1KpF6EPMQl1n6eKTMFpKBjvivtkvymk_hPyXx1_TdmLnoyzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luqYje3nHS5M-r601_f3vQTHVPU_b1J0alYbnoE184nfkyXriElcGcQBc3xDhwMgwfnKp_7W2ygqqsFEYSCw8IhudkCrjVoDNCOZYrhX9OcioRaVXNREGtXucIEt19brc3yYmHNEiRapsQBR2QqDCNr0yW9-TqXTMgqjHIFtSyKK908zpIjSQXrkHxQoamP00O43VzUkk_WlaJPZUT1FWf3f-OizumL_d8jsv6_uDWemKZ5dHbaXB_ApXCMRx194aNTWFm4Rot54VWBL8Cbfv9ga_Sqbfb_HGlbQ3KNRWHp8RVAIc5YCf67nfBoXK2phrUtacF_WpDF9G_2Yu7xmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXIkhCgJcl8XbKMhv29XpFWzfYSIJCTcnlpISdFx4J7EVXfAJhvxNafIqHwH9YbeyONO-mrurAOKBR_2rPAd9uX4ANoL5UOG6CY1o9TLVqRrXMfBF1Agz6rqAhLBueB54yLyiUR0x56XNKZzNhEZ8Ltmvm0pwh0l6T3k67eLvX9cb48oZ46MGky9yfrlhRh4UJ3cFn_O90aJzrCU1iWkEhDr241aUh2GMOs13j9qsbPsS4oX2E_1-82MAmyf0syMyU2k1t0WfU1FI4plZzE1YXZ_Kua5ChUrJN0jvUWIpyUSqTkXMma_p6K1xididXgOqw2wDWtUuxFWp0DjbCbMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqKG7bDMpuGzacsCL2mdGxMS1OD1UuA5UppB9OLqITwNV3PYonIb2bcI6UYTMy5u6-81SSPTBDTMf1CCbVLBzvZmeMAJhZkE96GDSJaOrylYfyKXvP8GfDocGfx4IQndRIPGFDlkJNRliIyd2XdRMMhvAjWN-7hTrljz816_IbEBsWXByX12eYvH1snTmYMuTe7tzATS8dS94t9tvgMwm7SKRB9rwsLHopxoG60idHpst41NPYy9wMgU2mcaAdDvNnyyjA67HntvGIG-HAn0NJFyP9XpLzHg_zDOUoGc-7sDHcvbxj-BBJ1jqJx3P-xoB3PEPxL7ejjEuMms9g_t7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJTygdkYJ2x_QeDVt9qarJwdCcvB_a9KjSJcG7Mf2HHp76yVtgGXag_yireMc3eKeBqhV294dQfHazsRU_GAeLXhjT35-VCCAwQJnrPN2Cd6z6n1vMQC4EWlC4ZP6E-qKi9vbqXiW0yNN6NEWxRLQt208prqasLT3oeiDS8j9dTCiXIcifaJ0Jhlu1mZTvHruFpLvOeMqI5MiNs3eFmydk-83WKMU8UmJ8zgZxezKIU62qWQHpgrUylxoh2mQXEBlrCucT7X75MDLA2lYAJJ5cuq8rxupHf1T3SPbJI-nsLIfpIUR7DjjZ7oqngbOPoZ8FS39_pNoULTQTM4-W6muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrP2M9o60aT6TxS1xrsPYQ4UyP2SP6GCiRvmytPwoGXW0wnEBS9u7ZufFEjYaZRn3q5faarohYVrvn8-ljS3WBhMuUBzw4gB2ldCFQJDqClamZJHLZGRHUkic2Vq8csxEShsZYjd-MVSmEfoXadVlZMJDeHrm8ZV-hMDzSzixmFGgKG5DE7xcD5KMG6KjWsCkohHsG_su5S8HuyGuMe2RfaoQN5FBGUf5baokJjVKMKUNkDcJspQOV_IO1tisegIc6XHuPZpaaDgpif8NYhVe4C7RkgG3yPQoyLAUMaEYs-Eylo4dlgreBpULa9igSlrMTIvCG1LBAU0_p4TNihBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vgs4n7lMNX-eBlh48Um964zy_gCJfWNU7cmPqnf_fKtkUsdexdHzNdZ3zTfKMNzFE56Sl2CcVMndsPx37gVhMqM3U_pWQQIGnZNHpYRgpRjXZHMOujReQoiOKjMP0o7Tq-kGPlX5EaAlwdec93AoSYPJAcJ1r5kWwBTWkTKApP47kR7pwYrV5I3iv54GlDsK9q11Uq-VISNiZktl8QxDF26ay4U2u1x4ptjcrnktCIOKM8bfD-XjGoBWK11pGeMcnWxCYzhLCpd8rt9_mb76_na-reo9_QgsXdQHdrPsoeoz-vFTugYn72EpA3zVL_2GY5HfjQngej3wAVSPq8GINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6gfdcW9C-0itxmsyeP3Yfn0dT9_O3lIse434yVH_IWPp9Km7B8HvLrkkzXpkScbbU7bcvec_Yf_mKucgUgy5KAXvN6pB8RxEeS2Cut1V-0eF6BqiH6jNwvml2PN9qem1bfT0z6BZG8KngO7zED8pNjAOxuiXQskzajaA14d1SjDUXAo5De1TrEq-NqjXyWtnZn83e8mhj6YtR5VFs1zeyfzjRmfx3klnZqc6C2TyFqldhZoC8szCnm2cWiGaiXeRBYXd_ERPIehUHKDOo7ZbmZXKIH7mG-TohI-pp2cwe9unzqbGiFysj7ZW-ZpnA8bTgL1lY7Kt01zhZDINGNw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGvlXJxk_poZmHbTcOt4dm7twkb18yOtM8ccop6xWkLk-V19B4GIZ5D3eJZkieeEhVtgaolWk7CFmW4A8rPw7KlnOoT1Z09s-4obxeV_2_sQyU8va1vTbrxCEeF0u-IWGUPJhKiJ0MSxn2TA_FtfgLIe_lsv7lGw3HyPF4jvimL7hJDFv0yPVlp5fW5fXZVl2m3vIViZ4AA8AA4ne9Kde1LpVgcPdzyeDcQJ5DnEAVoopQOEkB07fwR59GzqbeCvwzzTST1fOxH-4KSrzHuYixUIpMfKAkhNzPgpPI46Oc9dagDlmElcUsrSqN7ShF0e0bPg6tWOPwJnkBYkk_4DVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCR9cGCQOYyvi50DQTDBSp-M41PiBHgRNe1GkAbWhITAOK-QkNbBSWWgHLq35KTDTnny77dUGeyYUSqmjOvoF8XDEYD-Z5dxYURB0aVJ7W4sf85pxoc7qzJ_hZqeylaXcobJMamXF9U5tCvkDxkvK7N6pyMXi42nZOU8VqTYgogm584Ia5xUWWONlbmTvSQ8mfkEgIgCjHr8I1r7J_spX98dcwE3rDfR22hTExAgzK3XXYWrPoZ2O7PU_WodOlclxJ2_nJTgVD9FISQramhaHvWduZuXw0fZL5kACk0Z6sT1eJNfbo-xASPICCUpihGiF57boZ8ip9806GNkGcfptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRl4oWnDfLjNrt1TlfYbJ4N9fAEJEPrTKS4L-5cU6wG2APqnHmiVwXR0RSzxAeSkiKVNqLIJxH7nOTjQwj-P_fVyB29FUfQHohfYgi3GJCCrRtRZV6ojCLyJzSzYC3rXk2XwOqCkizLme2pVEZMJcLrTcfu2Y7BpWniNdZRvjMJlRDiCGpbSGwX5UEud38k9A7Vuy2Y3HHtJsDHC-HAaqmz8xW7s_7yDxueydfX1_ZiDuwGFpEkkUrI8f67YHNKIhFfVHOl3q8GYYOmeQNciC68qUfAw2WtY4jDiQWy0jskXLHN94qE18xr71DXWpV-rvdN4QoHKpDj8duZUh8IddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRG44134xbQFbigce6vf0Edkr2K0GEdN587KlcXfk110dSpXToKTZi7XA51H31eNerQSiXJ3eEm8IQW6uvcVBzD0azU4CiewDbbb5w1ghrfLcaog2Oxd7esY6QSVjsImcPyvu8WqGZabi3vS3zjeCQM7OZax7WA6Y40peoPKm638pskJA_KoFUoeGS4XABBIj_H6OnW4dUCgCLrOBK60McQvBb61rFWPCfTVasXcvvOsSYGF9y-7A1e7B8JJ2VhN5tXMURJERCoSnU0c7NDGMi2PaHpBYRugudY29ie_dbFBVTadimqkTE9ojQ6XXkEPEvOBi5pWRP5MJUw8mETiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfyrJHZxMzv0aPz65GzULN-6is2yXaye3wanuBjcr6RATS6GFl7NBr3B0OJMJYlK6vXOiSFdVOMVjX2iPeXoKjEkAc7S7V6f963MHdVgHEWuNKHR9tOlzuyDR4tiGjPY4-HWOd6gjZ74tb6t0NfhHYBCgfuFQqBd_KggiuFTUOTt3yiurAUxaCPQPIPB3uKZu8tUJDWpmUIsJ6wBuIliUjcmzWORLgnLdjISG58vjb_7NF4NpJ0vkfRp6aeA-jN1R1CIn-Y88_bTJiHVHKo0r7kl3ay1I3-IPZ6gy4zizhSsffSJfbI0vXlnh0QEAfN18p4fD0fn0FXbfxuPFcmf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PP6ViBTBbodh1OqRjJYa2Y2HUwF0WN2yw6OIIZp17CS2k-OEGz3PcDy89Duj2RCs_9_MZxf9gzEUssMnHPwCTgY7hUL_Dl_qD4YI7q6tvBRCzyzB1nn389L7QwzmMpp1PTvEbRKS1am-L5Wr8TCXG_OFXzKqHA9sqAvC0gtjJINIBZ33o1YJKOPt1rwax3JgP1PjjrMc_g61YO5p-xqORWXimM6gBB1lOoTcTcwcKkZ676MAdJKof4iU1GMwBQz5Ojzii39_zz0R9R3A7oXEnpEuVCokhDEVnw7-0c9ni0xguhQUXIVp9TBo2OlQmSkb-3t6ANhWqtr5ykoE9vS1Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsGPGLPvhhZ2ra07RYEDDlgBjSxxIToyeejb0-mRJFit6AO1MyoflX185DnrZ82602cy3iQSY_95wnqq0GcTjgEZd9_nrXfHGM7gA2cdVkEB38_h_EakZP9Md2zFlej1FZb15h7Le_u5zNEIusbn3-Jy7EhXwey3M3rrkkNkpswHEvB6Ge1jxiWc1WJ6ktw1pS0kc7L-E-dAlL3ktEESqzjy0RL0jcifB2uCSupPO06bCwbLCUUkK8K_K53Mr5vLYh1YglCs5w6ULnWiktY6hje96bliE_5pinN-wECPXGN86QXEq3Ll7NGBtBovLwV-Nf0S4KNz-5MlJZ5IHXmA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So6TZliW97QDYzQ1pTnOJ0A-YydEXWixxbLJ5LTrBJdXZO3O4SCSNCehrku35IsnZ2QP74TqvT16X36YJWp1U_F7Ke0Ub9OzpvmgLzq1u_8mzZQWNWc75xCi9-1Smzs9JmwtAW31xSBS3tfjKiZNnC7pT9eCj4VUWA900w63HTGruoRnhjTAUZJ0XwDdZA4AuDUtEPWh3x1_e9Ixc6GsGl8iHjtvChZQV6oAFkhcDTZTyCviGbrKWeT0gosJforWYY3dgrph7aj41UPESOv5TbB6OcBd3MPkOK6xKbgRPvNODZlliiDsWMxW8Ert4aGcyJ6RA1_YAifx9Hc6t5dXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5yR7tu2DcH87lXXYQ9s11J3XLW1UxO5iZUlP2klMOCZf4WPsqL3AFvS3sBaV0GqOXXSnrKURXZeSONfQr7cxr7sZj63J9HV2kfTTwE9ddb1kqvYvqFMHf_XIO75etslSyss2gvolzkbSD_5no_RMsVpk_6NL_saAv1Eg_S5YLrcLl-CU6zvdHoIHhymG_5xjhJd1Z0NcwxV0_YkkI95SOSVp-oGC3tyZGYcrTvzpx6QGAH_WwCCu1wzOYsx4WRN6rfHkSDWV_z-L0zw0frSzu8Y7rlDwzoUtuC7lmmZvhp5sGdJRlzFKXI5qq3eiSpXVAW2rQ1FArqVD36oRMWDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raf1YMLVHzMBMYe6yiKpPHm3Moo_a1b0M5JlFBX4f1wiJK8LKJL8IV2EIXs2OmrnZKX_kqLuEmOUu89RueAtKsZABAp_7waOJiTXOAwsgRMf3WtEK55_IcMno1VPRUS-Prxwz6kVe5QxV8SmCbAbK1JCB3HXZtjYpltMyi8zJik_cxaAnazvzgCQtbNASWmSm_DAqoLKxKPoNld3994dh1HbBoJqfHaBuJv70bKuGjan50lc3ASfuTUJwhUyavfKUcf3xK2DZRIfJ3K0YmKDh3LDuORtYFWaKnswy39v1hOanfvWGaNf1Ib-OsFwVA6GjMJGUlePja0FI0Y9YAQqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjWOBrU0WSm22nZCfhjJtpcVqZ4agK_ELPIFzMuaVbJbqLUDXRlHDtyaZjss7xNPHiAD0yqFKkq7gHN8krhkgsVeqMb4kdF5clHcKnrOqlsVIHcCIJJlYQBlbWU59rMzD_eOe5Te1oYJoELNi0dWoROwQlvfN0zxoD2N2DkUUT_b2w7tfwb09v2yiEPWYcndoD-tq8qddi01HWALTPDlLkDEJUYilcPai0_EkzY-sbN3VSeQ_OZfI2vrRXn5u7ZjfsmBB3X3zo2UkipxrYQUw79VcfFV_0RieMfosunENRQTUbmj6bsIa2nZKb71vqe-IX__r_oFbyHTGbUXEyDUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMpezWmnFLZ3iT3t9GHiyqhdX5YJ6_q07Dj6yPKax3ucgJ_EDSWvW1p5fdQBvnHpopsnw11-MBEEdmIhWF66cta-M-EqWRhtiL2anlf2622zevR7B1ng8goO2QsvTLLZZmJOBOAKE7YA6uV7pSqbTZ_9I5D7vu2-Q690C3Ql2GThQ-Jy4MQPc59bZWfVAZKIXCUFFirobvc6EiqD7tqCXunDbG-nfQkfpE39Okq79R9jvXmiVqJ1H42tWSjw7UdvI46zvezlbmglcejdpW8BsosfKy_hvRQCX64OHVV5tuxNT84IF5YFkBAkQC4LoFp2NzPmB4WkWyNWoCtvRtfntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o57QJKq_T5Vv1o6CiynheNFUTfTPCHdd_BJEuxReDQ5Mu_iHvOcYV8WWkyGiNjmlIuj_aJceVMN52TpfEEtvSraDwUjyngT7O1SdaWf3QghognfuU3sG5FRiNgK8czYixS26ETFj5LlUpROy3LxxbYUy0rMB3bSas5S1uVolQmzRumuXohCG1J0zACVCbagyLgp1GkHfN4gSunM_XThD4BVdBtBDILQBGkh6TtWOGVlh17SDjG1dNnwgwRPU0N8XSy6pteEdHrH7VdQV_zKhul_ozlCy-1MtJIsYv3SlkAPfpBNmsskoVJKFvStK6KWHUqxyF-mWDQVdK5E6JPxtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وی‌پی‌ان پرسرعت و پایدار با قیمت اقتصادی!
فقط با گیگی 4/800 با بهترین کیفیت ممکن به اینترنت بین الملل متصل شو
😍
🔹
تست رایگان 12 ساعته
🆓
🔹
ویندوز، مک، اندروید، IOS، لینوکس
👁
🔹
دانلود و آپلود نامحدود
⚡️
🔹
مناسب وب‌گردی، گیم و استریم
🎮
🔱
20%
تخفیف ویژه
برای مخاطب های عزیز کانال فان هیپ هاپ
🎁
کد تخفیف
: funhiphop
🤖
برای دریافت اکانت تست یا خرید، از طریق ربات زیر اقدام کنید:
https://t.me/ToPoLvpnbot?start=start</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W76fW_CW7lsYzW_IaIMgc1TVrMZG4SEF110YqTnugbPPRw0B6RUi9e8YcQ8Zz--8b1QH6mj3Pd_SpY0ybIIkF1CqxkisCbDPknIMqdvEIwvbdi-o7kOrdaWm6a6l2Kmsj8hTP4WJCPs4S3ef030oJUvq7ur823g0GcCgUVi3-o8x7wClrTXKGR0Sh9aHJnW34wbC_-5htJu8bUTXqCzRbNuLKYfta0gsnRA-2diHxtvz-k2L8NdDelVQ2oPvejykRvNKlf37LZZLWT0Ade0FIAUETS5uq6A99JYuc4Vke2Ks9LQDnipql-b5lsCJ443k69ReFXwB37KTsNw8SY3shA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fxWTbB1Rbw9gcSppd2ytJvEPHc4Nhq2EitRSzndQOxhY3L5-kB4iJL9IbKzPoHtq9GxCj8Y2oDaY5sdox0X2VgAMVLUCmgB9yoU-ygyVypq_IxLc6mkcLS66iSPyqrOF8-VFn9bUNY6VcVCefhk2CLZepLdkNHBp08lCu3okSdeP32mbLh1719aYHEzoBVhM1vtvXK5GtXPvLVYAgb6zu9TorBQ41Tev1c2H_txt76-cTGG069Ho2YpFhPsGqYt4EQ_GWLuvK8ZT0lXYSzgFnofROJpsJ1RCdg_VL9l2LEcHgcJRXxF1WiNzJhI3cfae0X1F0qNJWeJBb9YY4Ts1sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clXzMtkaLEdI9CvNk6PwJmzTrOInQ3MMlrfZq211dwPI5GYzVRDMf2OqiRvMtp7Y-UoemphpMhInpk-pHmRRKzmLKWjRELxTD6FQ5uHe9LTLk6IDy0oG7e5cFI4yBWc1O18u0xwGlbWKnSOI_9rkMRLX4gRK1J_M2jpOaEdqZDjo-H4r5At5WyeZChAk5Izw39pY6nF2HBYyk92j_p1DzqCsCBPC9FjOF37SLEHKN9BC-1zHvKh4tnM_MCRnhYUgOczbCDhzpkE1Ph0mU2vI7u8JVj8ck7nOqmO_d2miHirJn_NJogAVTcjuwObF8Gz2OsCgzkL2RIKWRmPZRPeBkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEzsD2MmqZdSA7HZPT4qqjnNIyLVQA-G8Vf2qi3CaBjee05nyFiOWMWZD9seXoTck_TMHIllbjSEzyiGp62io0d8Lxo3TZfd9KbAaZr4V6YgQuOwCGrJIDaVt6l5KzBCXuahO15M7IartaKuMwUMg0Q1tcsFPW5781f3Ty6gJRw_sjMY-1_uC9BqfXYNJ61_GOjgcYYsIifYe3rLc4vlYjRwirzg-mwj2CEN12RIDqnaMlWhXOm1t06-fpIAybxybi8IatxgB6_yAPdhRpY8AQ1Wt0CC05SFqcrfeCGlctPzsQxWWEtIGmBHzJGpY9br34nMp4cYjBAnA97Vo1kEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIuIFUOebEqNYAVrIYn6vFDmHFH_RkyoZ9Akg0e3fyLkRPJOcX1y3gAZNQAoXeQUNpA5Or4DnAdU6JhbpDMpA0-Z1c5P2gDFHdt1fUuj0Qvz8QetTuZ04-5xlV785YKfFy6lIJu1VJjzGzg3Qztlprvu1Ua6x0Mp6Mgs0V68QLzWYPxFpKwytclQS9nz-IERo-_enBXfHk1w0Oajrpmsl7COEW6LM13IlK08U5A2L-s0bJU2VY7Lu36vr0UWDe0ezyvMD9h75-MtRTN6-jGrt0K1iuwp7udt-O_4mXpJ8P9JFwYcXVUfyjdKLeROBLHRIze63wVzGQ7W7fOAaV2_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81297" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=HPZ06HaqmFU9vXCa_oyJNDryAy-VWqps4Q46_Y-yW_guDEKsYw8zJ7ZwtZ7_QAbopwzi0EWd-uxM6OG58s00aQ2L_U0WKfp0ccQn-Ri7bVb175_2jBEuhU4YI_joOqrM65iuVla3OHjhiJqqX8Gt4x3HEeV5r2hReyWzbrHCxGZUMDbMMxtOHh_WyR_1Karx05f4o9NMUiPP4mTt_VimEMNhkqpEF1VhDsYm4BxMOvrbY92nIzOyTR9JdSZtZTRQ8CHeuXwtEBuIW1kGJY5pXv_gOrDqmHb4RdSVVgxpaNb-VHxIoPruvTyHHr2e6pW3sT_hfPgbCQkMvEaIRSItiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=HPZ06HaqmFU9vXCa_oyJNDryAy-VWqps4Q46_Y-yW_guDEKsYw8zJ7ZwtZ7_QAbopwzi0EWd-uxM6OG58s00aQ2L_U0WKfp0ccQn-Ri7bVb175_2jBEuhU4YI_joOqrM65iuVla3OHjhiJqqX8Gt4x3HEeV5r2hReyWzbrHCxGZUMDbMMxtOHh_WyR_1Karx05f4o9NMUiPP4mTt_VimEMNhkqpEF1VhDsYm4BxMOvrbY92nIzOyTR9JdSZtZTRQ8CHeuXwtEBuIW1kGJY5pXv_gOrDqmHb4RdSVVgxpaNb-VHxIoPruvTyHHr2e6pW3sT_hfPgbCQkMvEaIRSItiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=cR0YMRNghPH2J52M68r7XpfeNjv0hF8dewQh2KV2KWMJIHtzs6LWU8yzOUdHa7JqWttorW6_95HEZKW7-djSgkVVgAd3YP6ylu8tHPNMH50aVepFq_RLsdkJVLICtKjzfuWwiYIU4HSwTIsrVuI5Z-g3hW2nu1YgWvKYSvJSlI-TV9WwJm6AneejBRdYtt6qJ4ofc7mltl0rNeTTP-9s4TM5xcuP9NGuAuzd5CkZfOEwTkt01NNCwhUxAhgDT9-TdTCyJJwDMl9O-hIYUkNmoDXdf8Zj-8Puk0vrjtQX2ulryit8mtroAvAYc-lKSScVjyoiKYoikH6tUeaGF57WRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=cR0YMRNghPH2J52M68r7XpfeNjv0hF8dewQh2KV2KWMJIHtzs6LWU8yzOUdHa7JqWttorW6_95HEZKW7-djSgkVVgAd3YP6ylu8tHPNMH50aVepFq_RLsdkJVLICtKjzfuWwiYIU4HSwTIsrVuI5Z-g3hW2nu1YgWvKYSvJSlI-TV9WwJm6AneejBRdYtt6qJ4ofc7mltl0rNeTTP-9s4TM5xcuP9NGuAuzd5CkZfOEwTkt01NNCwhUxAhgDT9-TdTCyJJwDMl9O-hIYUkNmoDXdf8Zj-8Puk0vrjtQX2ulryit8mtroAvAYc-lKSScVjyoiKYoikH6tUeaGF57WRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6-6TTqHfWrAOXoLeoneKms1xYR6_wejvP_Ma5OmcbyqNatSfwnu27OC232Z2ouiB6QDISVqvJ52eVsb-pDYIz8Ubs00VvdivfV0Df2tO4rByiKHxd-U293jHMuKZINlO9BLXK-zf5n9wKqESAUthvSAiSppKeDL87vs8QVpunOVtAEqzyqNp5AAYk9VlFDeQ4d-q0fxLqgagvAp8lwwaKxyuTCw01JvmBG_m94URxzTh7yy0uxOrooKae_WiExLwispoftmhlSSmXmA6QyKm29LQnXyV7z7szUfJ5hExDJMrXwO-6cw8x-PFY2ixraRcSNJjPMnvdu2W3ZdkDRatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=GD2SpIasGPeDxRHuxf0_LHc-ZGkBvYlevy0MteTI2tJ5Q1VQx5Dny2Zr5U7AB_9SArMKYaKvOFqVmvWHPGDP_nB9RyJtFLx8bpGLmYcuRIyhN0lJ3baPErCYJ60pnRd-4CD2q2FZMvVZr9CTAICqoyJxRrxqvPTsy8uyyxjnaxlvYWUFTnhJW366sYk21eTmxtH5d_ZLqDDd-4OTHzReGMrkn81vLhrUB9vyJ5hLK31jjzMSI9j6KTrdgXUBK5jJTY-hjsBBcOdDiWA4x2NDofDLYXMfKtW51GhYUGuQUlQ_XTGtkNSiP-kACFzUGUpu4k8L4mkXF9fBBZ77P4Ryxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=GD2SpIasGPeDxRHuxf0_LHc-ZGkBvYlevy0MteTI2tJ5Q1VQx5Dny2Zr5U7AB_9SArMKYaKvOFqVmvWHPGDP_nB9RyJtFLx8bpGLmYcuRIyhN0lJ3baPErCYJ60pnRd-4CD2q2FZMvVZr9CTAICqoyJxRrxqvPTsy8uyyxjnaxlvYWUFTnhJW366sYk21eTmxtH5d_ZLqDDd-4OTHzReGMrkn81vLhrUB9vyJ5hLK31jjzMSI9j6KTrdgXUBK5jJTY-hjsBBcOdDiWA4x2NDofDLYXMfKtW51GhYUGuQUlQ_XTGtkNSiP-kACFzUGUpu4k8L4mkXF9fBBZ77P4Ryxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKzOjcREZxU0FgW2JO2aVjRfWkaKVckLaV0TQc8Z2atlYm_sfCSp_13NipbOdLmo9_MPoqi_pQ2peHNl05bZW4P0MRb9RyiNPJaKp4ozU8wo77FuTYDd-_lD5zFf8JlgCV5CvVuYsHPh1jhbIKI4PSjH_m-fumJIDq30U4ZLHy7iGBbxIWIiNjiQm8K9S5ALJKcn8WLLJq-fIeK0p7rKxukE56-6ktKLjRS1Ut5moYOFMHs22tEN4xb9aPA-kxoHgIS9AQTHrUXTZQwWkCKiWBlRevoupuGaQUIxP7kJJnLkWTDO_1IQ1u26RdDTAeHbUhUPiSs0_TaIrDdUmf45lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWFXKhQMyyGWszZfGKaA5irGjKcT0E8fGXRh94hMHpm4JUPWLSHuxk4srH09JQkpvAZOLfXrgw8yXMkGw-IrSIEkRTE7wzs0f11hQoDkGGQ8tPLXwDRWWoFJT94Oax0lygtR3Z9YJzEos3Acphb12oPvrvq7Zyps4knTT1P6WbbhOu2Khe5T9pesP1tqvdLxsf6Su0yRMVYaZEPklz_zOCOOBdiykkYp0dE3P7uW06GRdyf42GGI8FP_EMKoQVoVmklTSEDHm4TJD_HLOgrswUlkFCO2Q7gp1XCxEKoMUwSImcLUlAili_x-C5eZQENZS4jYtbiQAxGRn2-jFzkjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-VgQcyIwlz6kD9v-twDw2HLz6BhJIWr2HMqx-9tL7JEb-LjTOhyJsMnFCuLEPpMdz3nb09KNQsoLlC1TtDkqCBuqUO7NcLtyxL6FjTQ8ELXX--dbystVlzyBQOQuyOYjXCLKZEPq-5mYBG0OssMqzkmrc8DuKnljMl01QU3qqvgWpipek9yezJppt1WpAISda7XSJ-PTY1zYNEE06DfLrekHrpEqzHhZ3d43SGpUblqcWrAikv3rwfG0bkcuNXglZxeTwPPfWkiQhoWlD0OubUXoTzhTo5Te5liDf1w4diUA2ffd3NS4PWOmk0b721HZy0aExsVRzI8hxr3udvC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید صدف زن هیپهاپولوژیست :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81285" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVo4Agbo60RjVyAqLiri4iTnV3alVAk7y3Ye6nYCQRAdFU60NiHKGXBmiiyQcfBPlVpAL-T44FOSm3ZuCSKJyekwM7_jbVL2bv1WOhlU2PAQKHGvGTdPrY-u2VQ4VI0v_Wtx2Oop1AySxxGj6CUS0f91_-SYla8WFoRk6P-VrfkUD2OGh_nMxig-iwvnBHRGuvraDS1tv2XDVzXEmJHsGKdn32ZhP52BFq5uR2U7xvfaxE15MwIVyGCps-NJvO6NsYN4kkz43hRsHrb_JPklVazJK-WPbJQZmxhtRCcMMRDafIrg0ID7AiFLMShPqaHup95OMZ74_0TNeY8Y1g0kww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81284" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFYnNtLCRappVOm_2QEkEqW3RiOu0juHIPIZ2thb3-S6PjuBp_GFx4zOIuFnfB1dhyk1JPVzB-efyZ5pibaOpcLiUqkWJMrwAnXgHnJdHve3pclaiQ-gQJiLrhxSvJXn_ixdyjIiprzoGD5-xqvOS4eIi6box6JLzX7fMpCWbijo9ZfjgSrp9JOfvT-IfwaG5oOfVSZ5YM05Qdn1Jh1S7ysNV32CYDwES58zdps-LHLH06CqCDAWkRouoWA-lhqik35A7ViVLNfeI0VQKzc4UNpbiaZ2ZMhE72Ye3Fg4AYFdiQWhwYmxbuCM6gWYDkHixJ9X_WdCDH06XhPGSGGi8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تجهیزات آمریکا که تو دو هفته‌ی اخیر زدیم نابود کردیم ۲۰۶ تا ۱۰۰ میلیون دلار قیمتشه.
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81283" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خداوندگاران هفت آسمان را سپاس که امروز من را لایق زنده ماندن و توانا در شنیدن این معجزه‌ی جدید تمدن بشری دانستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81282" target="_blank">📅 10:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یادش بخیر امتحان نهایی فیزیکو فرمولاشو نوشتم تو کاغذ بردم سر جلسه، بعد نمیدونستم کدوم فرمول برا کدوم سواله، افتادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81281" target="_blank">📅 10:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRzHXJgsw7DpV4ZHBc0Qng_ZyiQNQ8F__wjrYpHCt1qtcA5t4YQp_42sqscTgAAL2amMZFsskborRiCrNVmzURNievU8EYXaYNdd2kHmuSiWklJk1dDutX7hBHkNqquuWqRwS0tGlR4HGiDeQxVN3qKjCv2ywZYdDztwil4uEY2Lxl9gd5UFoX7_xV1Nr80_Tyye3Z9gWBJr0XPX8jy2Oioo5AkhA7W4HiKb5A76UZOcBueAkjNpQh-FFZqxCj_t21grI-ceNOXG9Wryx77a8au-pwb1LPBEyQKcXoqvM83RrWeEeVwDUfJg41uPiCtQ6shGUD-VXb4x84lgXPzxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاسی بسه، بریم دعوا جنسیتی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81280" target="_blank">📅 10:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آلوارز کلا سه تا مشتری داره پاریس، آرسنال و بارسا، آرسنال چون داره وینی رو میخره کنار کشیده، پاریسم چون فران رو داره میخره کشیده کنار، فقط بارسا مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81279" target="_blank">📅 09:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امیدوارم زودتر بمیری مهدی اونوقت حافظه تاریخی داستان پسرعمو و F35 زدن رو به همه میگه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81278" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81277" target="_blank">📅 09:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81276" target="_blank">📅 09:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یارو پیرمرد افتاده مرده ملت ریختن سر جنازش میگن ۳۰ سال پیش خایمالی میکرده، خب کیر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81275" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سلبریتی تو ایران همین که خایمالی نکنه کارشو انجام داده بیشتر از اون بکنه یا فراریش میدن یا یه بلایی سرش میارن دیگه اون آدم سابق نشه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81274" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVHMfA1V7RhY3_1ied2_v103f661JmC0RPcW4SUYmlkX9j-883Wi9j8BXxLXMJFDM24y2R87tjRRDINoeony6Rb5tsh1nxykVeJr6yyPOr3TxSv6OnDMvjSC7R97tHyMfZE-lId9uLB3BrEM9icpDLG-jtwvacUJgDHJKrB05WqNEuS-Gi0kjF3MMCUdri2TU7F3s_YrX9GB_7lBddL9qrcmqQQ4J4hFkUx_8vO1wy_guR8Rv11mvtDbRxTOS2YOfztAAhAf3SfdvoLXZ4orws0MRJ9WHjNfNCVyRpQgd7ylpZO9Wyq-ZiX97m9qBPyUB9eiEW12GheOKZujhOkfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشید مظاهری اومد مستقیم گفت، چیکار براش کردید که از بقیه هم انتظار دارید بگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81273" target="_blank">📅 09:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwrBmfD9ak6UdQxvVtaHHfM8IwVfgtxWdedV8ob-EktyEfpMqfwcapGowtu23TJSMg86rRFxJINhGBgFAv6u3nSvG-0mlZRWjv44U--YdwB3g-c7OW2CIXXe9zqjNQeAANqi9RTI_5ZYbScmJGAg53Uloe778MkgaAO0fwB02vxdwlYYPGBACtKShRMJi15C84eTIH2p1R09SJpPY8c65u2jAa9ua7ZIKCjduQXn5noM1LxBxCj1xABEA2-JDWrt3EU302SuLG0m8EGEgmr1rRNy6xBM7nRgY6IfL7kc35sfHT6YT0Xj7vhWUOaXkHa3QdGwVaAvRxvMgltVoiX7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81272" target="_blank">📅 09:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فیتای ویناک و هیپهاپولوژیست از سپاتیفای پاک شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81271" target="_blank">📅 07:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdbbinUrL21biWWuuIWdxQ_NpZkIT4oMXErHx9Jy6P7wngVyABlGdPOUf4ztMLAYcHDo0lusLz7PRZj0ukMqQ0yuxJt2IrgLY8IBRu0pTdXA_9VDm4Z3QPjb5T40EhqURSn9QdpJkENEakf0TEEob2dCqgJsp7BDihlsRdukFLP7D9YbvgKYUEzc4W_NIG4nNJXbxX_hvUNUFBpeRUCLazA4T--IHpa4MEUkFxI0zukJEkOlamyfnm6ky61thckHMy_DAqXk8uOKmi0o44gAhycDXJyZO_0uFVLa08WiAguU5YQkkKQzvHm-TqA-tlAFN-YGicZq1PWhjq7xk6kc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود هم پاخور بوده پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81270" target="_blank">📅 02:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81268">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایمان کیرم دهنت چرا کسی جز تو صدا نشنیده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81268" target="_blank">📅 01:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81267">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81267" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyBRFDkLDpCuZCExZONFn4XEOCifJKOQbMbxvwnjdkSEu1-lIUV9PgkPY_hPjXlce0FUQVTgP-xCWgUfy5v7XmRsYppPzq4as-U41fvMb2uDHq2gCq0jan1OUfIUs9sh4tWI38qtWNKOF1jIMHjhaVLbM9hDCYs1dLkQRfonmOYdnl1kY6idwiuhlaVpnzjPyovPoeO2N4v2NoaYKb1GMXB2Emp3_2-rvsKpwUpcybDlwhakV65Q5TLO0ko8V23DssTvXhIC74osepBPOWojRGm8G1BK84HRxFOffaNyIQlPEOu4nWJ7ifYRQ2mI3EgNJ5xWZ5pdScfmVo36xXjnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی رپفارسی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81266" target="_blank">📅 01:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81265" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQdBPiYjpyut8qKLx0oMrJVPEohX15kKyQfZMTnv4zs_563rypuX1dvTsoiEEJM6jFfRmS7kKgexQ_8FkqxaS5WdYHofvryuFWlEjpioDwzvH-Lkipeyg9Fy58eMG0vbVe6QS88rvrp1GwyxG2Oih8uuVs1oZuquM7USBbO_zlrob5dSANFNlU-huldq1dFHzYurwx3PxhsiXvI31I6gSXwQ_bJzjJfi3ezq3ZCKMiqDlKTNs5wraas-TRb4CInIbXxg1vQzf_MHhP59JVU2Lo75pGiMwZIB3tpo2qo31ltrFhXB4fRycVwqGR2d_shxxSuBGQKzpImtHedxuRg7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81264" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">طبق جنگ ۴۰ روزه امشب شدید میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81263" target="_blank">📅 23:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تموم شد، دیگه هیچوقت، هیچوقت نمیزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81262" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81261">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ در گفتگو با شبکه LCI فرانسه، درباره ایران:
به مامان توماج صالحی قسم این دفعه
این‌دفعه به شرافتم قسم بار آخره که به دیپلماسی فرصت می‌دم و اگه برا بار ۸۲۸۲۸۳۹۸ام، ۱۰۰ درصد از ۱۲ درصدِ نصف خواسته‌هام برآورده نشه یه جوری حمله می‌کنم که اصلا خیلی شدید و دروازه های جهنم و این داستانا قول می‌دم قول
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81261" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81260">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هوف
کانال ۱۴ اسرائیل: ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81260" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585792e34.mp4?token=TpxPS8zJimXtx4uo_dT0ssSDihjDfrNt_ApHNoqntyRL1Uzgd-2KFmhEhzCQ2KNd-Pmb-74RLXBM2lil6z1uN7tp3pIc0UJNioEXvqQI4bAgRHoJrJI4_CZsxJJ19GfByr8FC7tNsnsJaAPZ14MIELb1QggDoq71uGObuPDomxwRsl4MnzVCrCvZi88CITWAozsNDdnjkMiJuE_5tKoZzeo9UbKG9FRGZPTniVImbM9vD_vPxjQwtQ60A9svyPHm6R56SCBlKAHI_vq1FDcjjOLZmq-kkXOOpPQhKSNW8mNtKfGA_Ku00x2jTBcCSJ7nNKipaKcizR1NXgX0F7ze_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585792e34.mp4?token=TpxPS8zJimXtx4uo_dT0ssSDihjDfrNt_ApHNoqntyRL1Uzgd-2KFmhEhzCQ2KNd-Pmb-74RLXBM2lil6z1uN7tp3pIc0UJNioEXvqQI4bAgRHoJrJI4_CZsxJJ19GfByr8FC7tNsnsJaAPZ14MIELb1QggDoq71uGObuPDomxwRsl4MnzVCrCvZi88CITWAozsNDdnjkMiJuE_5tKoZzeo9UbKG9FRGZPTniVImbM9vD_vPxjQwtQ60A9svyPHm6R56SCBlKAHI_vq1FDcjjOLZmq-kkXOOpPQhKSNW8mNtKfGA_Ku00x2jTBcCSJ7nNKipaKcizR1NXgX0F7ze_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از مادر رپفارسی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81259" target="_blank">📅 22:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=tKWXdUTsWsrva_mr1bbvmL8StIfg1YhyLcruuKrBSbvew1VaBLeG3bJNjf-eSqlxWYeOHC9TQOkq2akyY-j4YZl9BFOWS839h_hvf9PcWwiLbkTcTmBjY4E1JFtYuwlRyt6EaPKIKP6Mh2WDoDhhQOejAiUnwAF-evzrurZIXEoG5sNrjX42b6T8O9GTlIshqp8fqSEgiK6r20r4cf8cvjHUFrykZwTmD41h2wgIKIoLpsZgau3seRfcBhwowITnSu6U26ST3xKWOdc0nz7UkU6lm3OBKdUEoqWasmYeFuu_CE0oSI713bWMk3SKJsEPg4wzWhyS0wCK0tcQKZSWAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=tKWXdUTsWsrva_mr1bbvmL8StIfg1YhyLcruuKrBSbvew1VaBLeG3bJNjf-eSqlxWYeOHC9TQOkq2akyY-j4YZl9BFOWS839h_hvf9PcWwiLbkTcTmBjY4E1JFtYuwlRyt6EaPKIKP6Mh2WDoDhhQOejAiUnwAF-evzrurZIXEoG5sNrjX42b6T8O9GTlIshqp8fqSEgiK6r20r4cf8cvjHUFrykZwTmD41h2wgIKIoLpsZgau3seRfcBhwowITnSu6U26ST3xKWOdc0nz7UkU6lm3OBKdUEoqWasmYeFuu_CE0oSI713bWMk3SKJsEPg4wzWhyS0wCK0tcQKZSWAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس داوینچی درحال لذت بردن از مذاکره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81258" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMzF-72jpWoxVmNCevn4YA8HDoRMg-TPP2xJ-MRlAFrZyqEVdFsO6OaefNGNYSpWMmEZR5AK8WvRxdZ5lXvGtSy_KJ64slqagIdpDc0oKwa5VYs66olTcS5tN0Q9e_5S2OqZ9oceG3nZEoa_Mx3A5UVVuUNrukko039HJ5bKB4A623jVL3_aZuSI5spU6T5XwB0fqjXQ43apUGS39-livsJUkNz5NPQ-CG83WTz7BS27NX1ZwBnVrNs6Jq88uZX0QeA3co9hxr1fk4P1E7STCB9Bnvy1Xso23ojs7zp4KBaWHAeddeGn_avPDnaisou49iArRHB_TsWJ6UpywSw5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81257" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouj45f8P2rXRrnVc-Ug5eafdQ5JNLZ-qxLMgiksffnCB70qwPQPjs2g8IDrlJrMWwX8z7sp29KhBFHjG-LNg_rswczpN6eTNSf6EMz-L9eSFZoDsUDXKGHqT0yUAcXOPukbHoct0J3BqyTI6-n-Nw-36_1TjI66At8CmDyERuTDiRUrCklC9_Uo1a2cX3Nb_1_vglLU3Yb6s39TYzoxWjV8UaF0jEcR3ewQJH2ObfnRgne63cvQGxiXcdX9MYSX1QjjcaafLCyfPYMoU93OD9UJ2RumkJXYvmXToUiDh6n4pkindryjhfqPt445Ftr9np1Rr4Hq7uZkaqg1fj5c1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81256" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید:
این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته که بگذره خواهیم دید چه خواهد شد.
#تاحدودی_بماند_به_یادگار
#تحلیل
#اکسپلور
#مراد_الله_ویسی
#خدابخشیان
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81255" target="_blank">📅 20:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81254">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICNtXO_4sFRgF7jWrbGqKHuNUkgBRBoY0upO6ryM4dEAbH0UUAIuVzgjc-HUQGZVx2scONGSAo48enjUcHc-EP_6mnWkJ5mvvy2XQknAgFIMECuYJhGtk_q1JfaU42HE5z5dU8PzwnGQUAfq6wmitqPEej5edjcTM1JJjmdgw5Ej95BEo0yM-6eAgu36uzmIqBUpLfuvbEFbxK1676OSxkPgaY9FMRcxsNW5Wkaz8YPEBE16N9EWLQkAR7IqS8quZwm-VGPwEYTjWRqQfvWrSk9s1QAbekhsWQDic8ww_nQ7RgW3pBKTmqJpgV_cX6v_3twalWDP8vYx1PXZ7F12yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید باشگاه فرهنگی ورزشی لیورپول :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81254" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قوه قضاییه اعلام کرد که ساعدی‌نیا حق باز کردن کافه نداره.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81253" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Juw--5d0afo03Dkpt-S7Z9_UyZ9riAw6AVJQ3taMFogHs7nrdR2iFCPMUczTJE-ZTDe7FriRUpXf-uK5I95DOq0KXPq6fxwnWIoyWe4FxaEn7qfOCfPZN5x5hQVzLU9ujCOPv-r-ihhkVfdjlyLr49-CUDPSVwEnkEw07dN3WEy_zn8iY8uFqU3CaGgaR0w8npqMN7TmcOTP6q1xYpWHYXmDrzKn0kQi5P1hk6mBgcyGOaqtTtDw7hPmqE5Bf8O1Q0DJzj8dVaRTjUktntNehkqFkI1XUJIf_HXBgux8eP4cVAgO0-Dy-e4oDfFYxKP93PTNB1e-a1m-eHW6SckuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستم اینو قبلا یه جایی دیدم.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81252" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری وای‌نت اسرائیل درمورد اینکه چرا دیشب نزدن و چه خواهد شد:
ترامپج می‌خواست خیلی عظیم و گسترده بزنه ها، ولی گفت یه فرصت دیگه به ایران میدم شاید دکتر عراقچی یه کاری کرد، پاکستان و قطر هم دارن تمام تلاششون رو می‌کنن.
ولی برای اسرائیل، این یک فرصت موقت برای ایران است که تغییری در ارزیابی کلی ایجاد نمی‌کند: توافق‌نامه آمریکا و ایران از بین رفته است و
احتمال دستیابی به یک توافق نهایی که در آن ایران تسلیم شود، صفر است
.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81250" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjTMZjtQcWbwQAeQERcoks74gMQZTCKiwSm_BHobxvDYSxYnqkuuoBSjSe4TOqM8HNmj1Bjuj2o8XmmVQuYLB3Wm1Imjs3t9ejBKbD8canFH4Ot3T_NM1kv7OeAxAIkeFdTJtd_PxbEmLB6FE8NcrqGUwFWeKkuyclgMSBI9ZIUrNgNL7lgYhoqVk-ou2q7nm3tUStAIIgsiaoQEPJ_L_OAW3toCI8HKubRFOokvosBUlCIU82OylnN8VObvnsAntU0sEpRmcNyjKvPQrCSoOOLsNaTaG8EmMewrQkXV10TDobgPpwrkIVkrrA8hCovxqZKcNVLSVbyIZk2d310bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
