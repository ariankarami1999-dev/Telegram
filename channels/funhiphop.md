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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dylM9x1moJakiwRpoVgQallw9R6bUIA5lFrgA4Q57pDHn3UWD8jcF6ZrbX2tMWlB1OlJi7yAfvtJRTiwQNlz5SM9tHXQP0KmqQLIqq_lmOHtABgd_CSYZolZPUec9_ZXPwsJnsGafqBg5xQqZasGZc9HTPvTUnOCJp7RxOBD3mAx-tZsxLMoS9HlOffdtPeb_VsBDr03nOiLys1C_jz1SNh50ujctVGcr04iWbtq8x6qsFO90g88VvC6rHE__Opmjoy7Ot4durQrtEcFOPcGQ6r3XGj-4uTGq1Y3-r8LT3Qq9wHtsqcoJB2x0S9P0aMxwTmfDHIr1vwwOBAluftDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okUspBLii1RcUEDHGWVQwz9VQa4TuG7UVeMvKY5NwoDw9mGwQl7IDd-ZHsei0s2mWlwtve92UbLVcysHy5I5aiH5TQkWlChMEGt4ZCJo3UAKORoOOxbrUJ3CxHuKDnct61U8cC6SCCftR67rKYrzrUnaFjaZmvnwT2t7rh4bKzkwS01GPz-CaPZy6q9xqLvzHMJGKcxfJlFWSS4TtZ26ueEIzbFXAd2XujEwL3nj0qYxPOeNIIIyCaYL0noxWXun3StlOWb56MEVd16HZIijbD1vtAY3zWZDPFpo2CqINy9_Ojw5sBbtkAUkKkL33W0FNqU-In8Dobjh4t3FhUkrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTEgOz6k7hkDaIC5UjvMowDjZl_jjH_2SqC30RnwgSkowoJ1cXy5_YW22MjqbL1X3JasZVEC_ngQK3-xvEem9ATei9l6Xb2egFIjYC-DLXnMlXNNM5KD4KnBsdboUs_v1gm6vRyUbcg97F_rnFu9paaN267L4hrBRghdEFW-CdyUhRZnwV1LxJQrcpDd2ldgzHNi73h4Rqh5oT9MZTPgtVZToBKqHnpYYHkQdamagIAqk7yqJkbfUuK7AtOwMD1fk666JfX9vKv_1gKgm3otkx_N07iFAgnDSEd8k78Ve1Kz5pbuzzrbYUHM07oC-IdMhOKabLEPqjRKn_FeY4afnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUntBcC4ptxkuVkYG9AwWHDdpHV05cglzJAVa3lednL3VKfwhYgSU2ESUlFr09YWgmOMWSpfJ7_a30PmSVIHZV1mEQj6aVFi-urSiGX0JFfB33Y5RJ6nbdRk8X7of_DhTsi40egJ8DWsLEbPzUUgz0BGk1zKUV0JqApFT2n1LaQv5eUeYn5l1qM2wA0J3JSQs79_74JSmNSM1OYJVaa3WjoV8R9_Rf66bRvN4_uDhR_39zkqj6rxxXrAi1FXL0hDJnNvC9tKgwwczQ4xHwmv5W_6o8X6-XR3iKEbAzX4b0khnQtDKXOjC6femXnM9QyiiayVX4vTyJUR1ht-KcGHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUXPVenySKtuG0LqfEcgzP9cmzQ9cHEbJZo93u2SsBgkAH9NRWnOw9O8FxU1AYwFoWIsRUdfdyHqS1X-i45ZkSUEphb_7QXculQbG5_T8ZCL9PmrWrE8CIC5pJosVhBCJmn4JTlvUOaL9jPt7nrLWD7mhow6KosdcWSJQg7HGaPD2JTBzE-eALpdSAvFVo5rV68Pu95BywYuoG26B2UVsAXoVzfOTpLVDQ4LT6UdqXsxURKWi1gJz3kQR2M-Wm_EwVXln7b0FpV2FW2rCXCnEBn2ip-kRlKzt5dQ8ORVdqSPa2wLpRwYgr-7aLwip7ioP2W6uEFZ9SEe-e0BjXkeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYdGBYPq4wiQHKJ7uXofmow7zmebMMnraIUSBzLBehz542BIIw-B5vxunZCE-ku_BBnB2rNbaV0o1ZfVksaGZKq_irItcYlylqqo36DmaqzGWMx9spLKuxjNfcQTw3HpDCNbGsgukAzLG_B-4aX4AuLikc2n-bXYpOGcqmXBX1W9Q2MERPWzWt2Uh55IBG_0DXsYFzEY-cSkXq5fcWbLoVRjxiSTm4nAchr_zR04K5P9gofn6s-PU-z8ps4mHOYAjsu07KpPu9Qzd4UIuBxb9ASsDuyW-f-D3fdBGCNAxGcelK1ybJukrrEhuV5Jed5lNswd5Ylsx30NabF0i5nEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ipx-rIWjX_9xngFFF1Cj26x4o3XGbCpZ2hrXUq8Er8zb4K_45u7ytlD6ywtLSYbAB6fUQBF5nR_0lXjIit7iI3stHLHkJUd57CLvHdk3PFJZYizulvvqaV-SJDpuQ8koqSBEBLxAJRLhaRaO7W2lpq55pLwQix5cfYH0ShFRFW4QT407tgNAGYi4DJ9yVTKyTU4hLaCEqeF80PfEuRnTFwd5Qc_c4wTcV60as49QUV7rAww6lizbuqQRYP6wnbzQ1HEERxekQg534ft8ehI8B6dkdCz9M8AKKUo4YxSZdxAemjMB6s8iAAngP1bjruKWTtMQ1f3FX0nDdK3ZfNL5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxZ1JARJmjWaMjZNGDPzspOwzDW6wicvkcqN4LNXwVeADVlVUo8IJ8LyRkB_1QE2zXY-1toOruT8dhJBH4wRZkG7gIbqt1-syTGdRAreiQDckQR1E3DkBy8vjuIHngTtvJ4M94MzgeA657Va2JXuBOKHvARv0ZhI6KzMYPWd9z7BndLnS7YRjXGSRlseRUDMpkrtD3KdrR8QxiJJgY6MwXx2c1ggYaQMMADvBk01xkwvhqmK5xFXUaeZvoMTwy0WAJfpJ-KZo19NYUOnqg3ymS6YneF044yv79fd4QxF5YAa_sLW_aWpEYrjazMrK93I5BgFfLCmNnOFS82PIM38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Xj7Q8Voji3JRs2xh0uQQPy7Q3GOL5pm7pXxiq3GAi9W70a3_hX5WJBXOb3I6Ap5zNjQGZ4drDVAG2KUPiUXTpywiHZFdk0CRmHHgj8TL2iIrSMUp_8RYIwO6Zk14p8SYvEZJOzZVqsg3OIRP1Hxi21oOhcFWi-eRs0a_1zkDCnH2fH1rLGwt_MR1MmrWUOlMIMNq6hwyy9zcI-rUyGslfBWhZL58PM43HD-UAcRYjuUw-KAJNYpHnvkqo4h20C24aAuZxWrYZoihC-zjaKP6ofyGdNGWLFfYUXvQQSGvQ_9435Ucs5L-smJbdB0IpMnJZ5she4Hl8NI2X-d4GRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph4YvjhKrVuL18ZHTUKknl_Xz5isDt1vGJCt6nCuKY2YQufbozV1T-1YXRtel0ThOcHMc2_AvbB5tMTRu4JSBTKCUpHfMu3BUM72sQp8RDrw8Pmxny-M-GjgEJ70l99gau5flzo9C5A8CDsFg3alb_lBcjhUp4MtQ3dKIgZb72JSJ0NsekGxLNJZRADGPh66Cloh0ZQtCVpsKv8O_AEQXGwfi-LULVxo5P9uIkQQQ_1f6PVG87fao6zQ8gbsFZ42pQODcAKYm6MunY9-5d90pR-kVKIXfRI1Q4_r23Uyp3Yjtm6_HhdfuSFyY9XjhDI2ey1zS7ar3NdFv58NvAFFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1QwFpiP4UuVdfOdjiePUhCFTTWY05LkNT3Q8saMiUO-eKpAhKKiYKxdyqjddpqHfMFIINOvQBcsH95I_3eJ2kDNwqK3UhssiH0DPZ2R3rlkbj3-ZX11EEucWOgObheEx-j-wQ1SOS2Xvvwg83luhGSi56o4Hl7sB4hZUGGcjNG05NELJpX6K3coLTMv_HMZSRo_0fGU9opM_sB9CJ0RoQmjIjTX2raPVRKnjXq811zEpD52i0SNFlKgpA7lWJAdO0mJ07QAHRJFLOQKRYIysHmak8SO7K2IgEcfVgEXNCFWfmb_ZaDo2fh_-auCVceZE7lcasBPDTf5OOtrRx0xBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAv5pyTEgCjhXaiz5qonsQlyKphgjz78Gswp1F_vaej0Ctqp-Ke8irFM8r5fqjh8O-01NLfNmNgCYKQr62_7NM6NYic1MSmt0gnUKzmq3J0iSCJuMh7KO3BQ08N3Glt216EZ6FijZCsaHhsuFYGo-FoeiZQAcM0txOISAmZ1DNxqlF_aMhDEUTuwUFdcI5pemR9WzwWqGBdDQzZ3sJinoppGWqMkv3t4aRae2rw9dal18a6TSguAg7h0i2jMDwiKD701cP1qXqllN2YYNRWWCVpPDMC0p3TIc8TVKFyVN9FF2IFE7AeBRoOPSPBfZr6C4yF_Sqpj0y96av4LrrE57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUQojo29Qjyh7goRX43QFrtYe-BhWdCEMI70WeFHYS8yV0E0eo9R17zdzKsMQtP9AnonZmriybdcQIYM7qeXeL4Br57tXMHiXVAsvWY_N4WWRCl6qcLHREWosviBlt_XFJ0O53DDLFI8i14qds5Na-kKWR7btG7P90aMBwaE9fOIMVTBEhDhjE4rgQOv6xCX5k4MpTYy72e0KuCNLPTpPrmxqQSMfywCSbXRn23ZWillfNdrceNHOu-raXqVkE1Zt7mMdova2AoZzg1SdJhR2z1bzW9PCWlX_nSuWGfx9VDckdoKRZVr8T3WmcHhL0Aq-9-VKaOkn111HItnB9MqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlXcgAPYG3zsf827bfla2IHCEAbMyKmAH0Z5ctavJ5jxamb9IjyPltddVH8w_QfsPwiGX4rNmtghTL9NTgOBQwogFUmPeKxRMZpUAWdLVj7TWrWweB_HTYHXpEH5_KY16kZRkPbWsQjMHMo3GPDtL_FqtI-rYJlDT-0escjhf7XTh7AhAtnL75j8I1UUNFMOYLFsrBwx_tMlUCTakhm1_TPStL5xoKXP_glFxCQMGT1WLJQRX0sxVHuGC4NqMB71xrCvKivWImxCJtvfx1DpFXV_a8zDV7AzUMJm2CFw4Cf6nqtXbxr67rZk57miI7YHOasc02DcmmV7dE9LjSYoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7n9IWQHVqb-fZcykEW1RLfZdaGflsUh2IpNM_12OG9IU1v-aMdzsL30XWsfdNNvq4WffiMewIsbpL9eemnAuWMEWQJdEvZMR7gAxqtMpc3KKMJ-CX_kPaFziyoqwbG626fW-4GapEOcTw3NxvcEbDssuKN0KO8q8e9oEwXX3g2ou8BrxK2r8VR3rBQ7l15Acg-aBG5vRQVHm9qHnNcS8YenEtbXbWH3lkva4scisE0nOVV6tAEzVtYTY7HqeIhT6jaYsW8adlH2VkasCQKpT8Dt8hTuJshSRMKDx5mwyq-AIj_JZHcwQSr0nAAyTgOtTWd2YPMFHSoI7r8xCOlJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ovhk9jHwVc6lVcB7PfHzBqxFmP9DqrFq8HXEFTkmnkLYVmQApaqGaIfLUmN-WEZSsmWd1uFd1wbwc9YRYL4W3X7vpa0ONt5egyv7eVt7C2rc9nr-DKWNLVCfy0oUe-oYmQZ6OBLbRrCYPsnBFqPk1IxST2pEtwwKmCPYr32tJwYitiyNLIpN79nychiFGmxvg0oNgIecL1hDKcB8OiYLciBsCZZPiwlmHIMbF76QINMupE_Nw4Oe9Altp_yl2au_2ij5KYoPaJC4BorQPICBFbvVpYxsaq_saXxlw1KpF6EPMQl1n6eKTMFpKBjvivtkvymk_hPyXx1_TdmLnoyzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkp-iJXALcKIRv2nxkkuejqjSg571D-O8trPaUMFVqke4PN3dWEOZpzJNmwe1EOOvduGqZjsoRe5XG0lsTnbmGgAUC59vlJ7v9x4Bc-xlE_nZFzvs-9f9ELJ9dc97rOceoWETwwtIFNqp0spjY1BR4iD6LOe01qmZLKy5EKu_D-6ebGNCz33nVgWhvnmonupEP00Ze-2iJQAmHlxhYkpGqd5VarZZgJSo2U4JrKPsOvBpLIjiapJYFAdjKPtKQFhyQd5D0HcV4i9ME_lVCEqbKDKqZFioRyV2W_7pypyDrEqaeRNNziIDN1aqbqWdpnnUozX6FFAU0Gb3UVIjB-E7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXIkhCgJcl8XbKMhv29XpFWzfYSIJCTcnlpISdFx4J7EVXfAJhvxNafIqHwH9YbeyONO-mrurAOKBR_2rPAd9uX4ANoL5UOG6CY1o9TLVqRrXMfBF1Agz6rqAhLBueB54yLyiUR0x56XNKZzNhEZ8Ltmvm0pwh0l6T3k67eLvX9cb48oZ46MGky9yfrlhRh4UJ3cFn_O90aJzrCU1iWkEhDr241aUh2GMOs13j9qsbPsS4oX2E_1-82MAmyf0syMyU2k1t0WfU1FI4plZzE1YXZ_Kua5ChUrJN0jvUWIpyUSqTkXMma_p6K1xididXgOqw2wDWtUuxFWp0DjbCbMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asw8iaKj3BKfiZGFyC-Zejxf58a6ZprAFD5sUh4_srPNnzc1jvVv-Qifo-vxkg37olq414qqkFd4kHbU69CLHM3vQDKA7wtHdH7VeX-1HpwTHrDuVh62kn2NPjHNdAxhKWTslFpyvWHimf-avIZRa55dGyPdRIDyunig-4F_6oFdiVppsFoasUOpn7TBRESFG-X8MLQ5QOc-XAtp5-lXHalBhaJkMghTR3ovfm-3xHcdJMvZy7mtWm24uziLRt735s7rh2dxmCOa8qAFkOV9QR_xz24b2W9kTCu1jp-oNwthgM69AJ-NEBQaVRpXk2Fi0kOAE-XN4a190zcadVX3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJTygdkYJ2x_QeDVt9qarJwdCcvB_a9KjSJcG7Mf2HHp76yVtgGXag_yireMc3eKeBqhV294dQfHazsRU_GAeLXhjT35-VCCAwQJnrPN2Cd6z6n1vMQC4EWlC4ZP6E-qKi9vbqXiW0yNN6NEWxRLQt208prqasLT3oeiDS8j9dTCiXIcifaJ0Jhlu1mZTvHruFpLvOeMqI5MiNs3eFmydk-83WKMU8UmJ8zgZxezKIU62qWQHpgrUylxoh2mQXEBlrCucT7X75MDLA2lYAJJ5cuq8rxupHf1T3SPbJI-nsLIfpIUR7DjjZ7oqngbOPoZ8FS39_pNoULTQTM4-W6muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrP2M9o60aT6TxS1xrsPYQ4UyP2SP6GCiRvmytPwoGXW0wnEBS9u7ZufFEjYaZRn3q5faarohYVrvn8-ljS3WBhMuUBzw4gB2ldCFQJDqClamZJHLZGRHUkic2Vq8csxEShsZYjd-MVSmEfoXadVlZMJDeHrm8ZV-hMDzSzixmFGgKG5DE7xcD5KMG6KjWsCkohHsG_su5S8HuyGuMe2RfaoQN5FBGUf5baokJjVKMKUNkDcJspQOV_IO1tisegIc6XHuPZpaaDgpif8NYhVe4C7RkgG3yPQoyLAUMaEYs-Eylo4dlgreBpULa9igSlrMTIvCG1LBAU0_p4TNihBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vgs4n7lMNX-eBlh48Um964zy_gCJfWNU7cmPqnf_fKtkUsdexdHzNdZ3zTfKMNzFE56Sl2CcVMndsPx37gVhMqM3U_pWQQIGnZNHpYRgpRjXZHMOujReQoiOKjMP0o7Tq-kGPlX5EaAlwdec93AoSYPJAcJ1r5kWwBTWkTKApP47kR7pwYrV5I3iv54GlDsK9q11Uq-VISNiZktl8QxDF26ay4U2u1x4ptjcrnktCIOKM8bfD-XjGoBWK11pGeMcnWxCYzhLCpd8rt9_mb76_na-reo9_QgsXdQHdrPsoeoz-vFTugYn72EpA3zVL_2GY5HfjQngej3wAVSPq8GINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8dqe6nuYQ5juvAGUDberguGsRau1FB0Yw2yh0XOHBYFuVY4mOkLSPAPbMfeWSudhAnnUKmP6nBEECcrx6-wwor8YkLFXi-G7KuYR20QIU80hv7MCC1H85kbxraUtxCPXEQZA305uOnOcCKqpNBeq_MfmoNUno85I8w-fz-xuuTKQf2UX3jNpQd5XSrrmpPXRkp__ERP2GHM9GFwiv07u9HZOKDSxzCsXycoUbsJjOhl0Ho2cde_8HEI5siX21M9JBdZfoRgcJaPw1MMbS_OAtZ18btWmkAqYHODBU7ZrZUhk_pE3hpkUC4Z3kNl-71isuwUZsbRwHwVL6nDDNOxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecenNTJczm5WFj-Mc3zNUIi0ORYTILgYF8GEJkmLSs0SN-cxtrp9f_s5IcDDzTP4xncH6rkLY7redCkHq_zjLflddE3xaB8S6MvMMeZr38AVU9E1eiKOm3WY_SamXDAelSdukhuu_ZQh6_7AvLvcYodUc0B0ThHn7uHRlXdU6EvIrurHvwmqMgERzMcOHADCyFqFQNyPXCjuUMqxevTIJGQlG1z24lnMegxlZZeU6HC75dfIM0AI0xuRauTW-3IkGzvwt8XOn4fEbMCpuwz3_GlUDnLQAoy49lxRIbgm1gOW7wrGa5uC_DHj4bqMRqlCFn7xaoDiWe3iG-V1XMKCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKBGduOGu8EMjCNAHvHgH8FfhBmh5NrLlTtwcQ4FoAa3pR3LXOZCBvy56gnr8v5weo4Aq5bAs_dgPF1jC3fiGza-c7PGvoIDCHetowdpE2oGYV_URta76MassN8Fu3TIcOVZ8w48Ao6KGFQ3Zq2YGZ4kbvDdpf5pOsm9usV7MyJAoIbcd2V15E4igK5f3pd14dJRGJMxtLnyCEqhRR_QaZoOlBJV-KPrlWEq5K45pIgQXpj6zm7q1EGr6FFD4SyTEjz8M63y37JIT9AdQ1KFNrXswO0bu0YYCAdWX7sGHD46YOd9sXgEkrKWkXKjCELvd-vNJi1PG1EROqusirjvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjfO4Iz2KqcUVruERAjTQoXDmn9_Yj5LvpooYze6ZqYMWh-Y11Lwh-ogV2zihtTjxUaeVG07065gyj0WotcHAduh29duK6zGf-A4FtN5dP16yfn0ILh5npetDN-H78KBycARW0Sq3gt8sOUoHcgZPhJ410JUYV8wVQ3trCPiG2mHNVyaVCHEVCIsxkauNsLZTUGnnhPck1rGPJW3uZX-geB6gYv23pOMPVTAGvDgpIMGKLws2skJ4hFTErWTs14twgdJVfTmIA2fY8tuE4AP7NDOjCTqvHnbbSo1x9WGWkTElaGW9Tp0LQwr7sIcYlwarjs6YXcHhmL4qm_oPPP8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRG44134xbQFbigce6vf0Edkr2K0GEdN587KlcXfk110dSpXToKTZi7XA51H31eNerQSiXJ3eEm8IQW6uvcVBzD0azU4CiewDbbb5w1ghrfLcaog2Oxd7esY6QSVjsImcPyvu8WqGZabi3vS3zjeCQM7OZax7WA6Y40peoPKm638pskJA_KoFUoeGS4XABBIj_H6OnW4dUCgCLrOBK60McQvBb61rFWPCfTVasXcvvOsSYGF9y-7A1e7B8JJ2VhN5tXMURJERCoSnU0c7NDGMi2PaHpBYRugudY29ie_dbFBVTadimqkTE9ojQ6XXkEPEvOBi5pWRP5MJUw8mETiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O80EEJpr9VDftn-SqrT2ww06S6DWRkn_G7WqHzba_jA46LahQW7uUSWCHfe5DGF_mrA5Uab7up0zbYqfUQzMBE-TKxTfhSyw2hVIEW-S3XT1V5p8Uphr1B3xLZOFBRj0vav1RohuXEldByS8f7xpnuADud0W4MgQ09f4haw75E-Aq0iHp4hxvLAeKVzD7Rbfr8j3UiMLQH5-PLQ3YAb-eA6zhPivV4VjGZ2KoKjny-jHFy3DCC9s18LrCo3iYcUk5c2i3u6DMpk4nlmeaZgHv1jL5v7qNps4UNCZ0reJF4SirQ3dqk1jgO8763pMlMT8xp8gfCgDjqE4-ThL5EoEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PP6ViBTBbodh1OqRjJYa2Y2HUwF0WN2yw6OIIZp17CS2k-OEGz3PcDy89Duj2RCs_9_MZxf9gzEUssMnHPwCTgY7hUL_Dl_qD4YI7q6tvBRCzyzB1nn389L7QwzmMpp1PTvEbRKS1am-L5Wr8TCXG_OFXzKqHA9sqAvC0gtjJINIBZ33o1YJKOPt1rwax3JgP1PjjrMc_g61YO5p-xqORWXimM6gBB1lOoTcTcwcKkZ676MAdJKof4iU1GMwBQz5Ojzii39_zz0R9R3A7oXEnpEuVCokhDEVnw7-0c9ni0xguhQUXIVp9TBo2OlQmSkb-3t6ANhWqtr5ykoE9vS1Xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsGPGLPvhhZ2ra07RYEDDlgBjSxxIToyeejb0-mRJFit6AO1MyoflX185DnrZ82602cy3iQSY_95wnqq0GcTjgEZd9_nrXfHGM7gA2cdVkEB38_h_EakZP9Md2zFlej1FZb15h7Le_u5zNEIusbn3-Jy7EhXwey3M3rrkkNkpswHEvB6Ge1jxiWc1WJ6ktw1pS0kc7L-E-dAlL3ktEESqzjy0RL0jcifB2uCSupPO06bCwbLCUUkK8K_K53Mr5vLYh1YglCs5w6ULnWiktY6hje96bliE_5pinN-wECPXGN86QXEq3Ll7NGBtBovLwV-Nf0S4KNz-5MlJZ5IHXmA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So6TZliW97QDYzQ1pTnOJ0A-YydEXWixxbLJ5LTrBJdXZO3O4SCSNCehrku35IsnZ2QP74TqvT16X36YJWp1U_F7Ke0Ub9OzpvmgLzq1u_8mzZQWNWc75xCi9-1Smzs9JmwtAW31xSBS3tfjKiZNnC7pT9eCj4VUWA900w63HTGruoRnhjTAUZJ0XwDdZA4AuDUtEPWh3x1_e9Ixc6GsGl8iHjtvChZQV6oAFkhcDTZTyCviGbrKWeT0gosJforWYY3dgrph7aj41UPESOv5TbB6OcBd3MPkOK6xKbgRPvNODZlliiDsWMxW8Ert4aGcyJ6RA1_YAifx9Hc6t5dXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5yR7tu2DcH87lXXYQ9s11J3XLW1UxO5iZUlP2klMOCZf4WPsqL3AFvS3sBaV0GqOXXSnrKURXZeSONfQr7cxr7sZj63J9HV2kfTTwE9ddb1kqvYvqFMHf_XIO75etslSyss2gvolzkbSD_5no_RMsVpk_6NL_saAv1Eg_S5YLrcLl-CU6zvdHoIHhymG_5xjhJd1Z0NcwxV0_YkkI95SOSVp-oGC3tyZGYcrTvzpx6QGAH_WwCCu1wzOYsx4WRN6rfHkSDWV_z-L0zw0frSzu8Y7rlDwzoUtuC7lmmZvhp5sGdJRlzFKXI5qq3eiSpXVAW2rQ1FArqVD36oRMWDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raf1YMLVHzMBMYe6yiKpPHm3Moo_a1b0M5JlFBX4f1wiJK8LKJL8IV2EIXs2OmrnZKX_kqLuEmOUu89RueAtKsZABAp_7waOJiTXOAwsgRMf3WtEK55_IcMno1VPRUS-Prxwz6kVe5QxV8SmCbAbK1JCB3HXZtjYpltMyi8zJik_cxaAnazvzgCQtbNASWmSm_DAqoLKxKPoNld3994dh1HbBoJqfHaBuJv70bKuGjan50lc3ASfuTUJwhUyavfKUcf3xK2DZRIfJ3K0YmKDh3LDuORtYFWaKnswy39v1hOanfvWGaNf1Ib-OsFwVA6GjMJGUlePja0FI0Y9YAQqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjWOBrU0WSm22nZCfhjJtpcVqZ4agK_ELPIFzMuaVbJbqLUDXRlHDtyaZjss7xNPHiAD0yqFKkq7gHN8krhkgsVeqMb4kdF5clHcKnrOqlsVIHcCIJJlYQBlbWU59rMzD_eOe5Te1oYJoELNi0dWoROwQlvfN0zxoD2N2DkUUT_b2w7tfwb09v2yiEPWYcndoD-tq8qddi01HWALTPDlLkDEJUYilcPai0_EkzY-sbN3VSeQ_OZfI2vrRXn5u7ZjfsmBB3X3zo2UkipxrYQUw79VcfFV_0RieMfosunENRQTUbmj6bsIa2nZKb71vqe-IX__r_oFbyHTGbUXEyDUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOsumiu2seVD9mXNJh4rE51gG4AHeqkbEsR8G04hbqRdZkCLak_M8e3_4FvcddHM4PtgQKmASKFCmSIfraFryXTjY4KeyECLI8kSLD6F9qGXBw2DP8p8b5CHhQ350K8Kgwcc4HnJrwOfGrCHKNoLmJonW24fsUiba4_EQ6J_SJj-K976k7IuAmLD10mAMSK2XYu4gNZwWcsB_r4PyqFyz0kWFiV9Q6eXdi5gDXspmmIAk-ENhkTfjtZyiuyObiJC0nK4do95zFtfwELxarNf_rtTEYtCM8UrCLryH7oRPNpz9VHhydK1yRy6DnbY0EK0LXj2IaU31sx5d1PPA8cYmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWnw4ll5w5MTa3jhAZsTE8LeNPt-k90r8leBOzgEWSYVXZ2NdEUnex2NrF_ySRPtUAeop1XBNK_QcX4Sg-eC2fBvXFFZ7XoZQ3Dv7r-zqZ5b6qWH6ufdTFniAtM_JZb_u_W0K3ltPaYUt8fkF1-HUOmlsfe8gbitE72T8AzcY2Q8T0b7zFNihak7fHFht9fsz24xD-dRxI6RoLj9aK-NZuuXwg99syxjEM71LLQdtjKwrGCTC9zmy4rwON-aFCsCLnreXxaIrXd0HrznUcAW0fnl7DrYRSXwYpesMW6g-NpiJjVAOnLIM7p4MQeSJSbAazwyhy-kxkYyNBgr0H0W1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjawAg8Yo5IIMAJL7t8NcKRgEt8dPyqMlCTu6mYKEBkhX7W3SRSA2M7znI0tz4j3fv_annUOxcrJfY7BqundTYjKtqIbq3pzEUDVUFrdz94aV1Qcm_2j-n2fQtiaCur5HGl8Cazkf_9K1CiTMVAlfMWLsm_5VsU-_cDw14vANXXRyQWcPb3ccaoBMeAUFDnn8Eyn5GqLz3GJG-iGRnIH7vBIrOMsqcE707oA6IvFCtRajI2n8apEs_YKO64foemqZgxrFhei5k3LSr_SGgaf1jD9CPGhM5fJ9wKWMnzej2mYOICLrmbQuZKWsgEh4XCHPLBjzi_UrAhlZwO9ym6rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkvQX3zPdf7d6w98m5dtvxQp5lZ7Lb9ivCKah1pbLFpNPrGOG7uPvZX9LSN2bhvT5pAQ2MdKiBVx0tzrZVsCBxZd9JlJkvPQmBOVF0SdaEowbc4xrRVQS4-t7IsFkNO7v2RUFo2e2B904qmoxv9ZIekEAP7QzGIWl3I6UFYk3usFNO7u0Jo64LJoc_maw5TOKLoKF-ld3H8WP2XLWYB3jo6Jd_U5TmEg6j6QR_Gi3bTOgRK-H75Tu_ZgQKfUjjcO7KiaIyzwlr9JLWf9S_EqEXRBQ2Eh8p7Wt4I4MoLUqC3qwzJ8Q3PbYP8weuFu68hJNdRpBtszq5D_liDHFoa3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0WDLPzOc3OHwyh3jRvxajKVx4pTxCI8gR5NNTND9HxR2Kbi5vo0eD6Dmkwdwn5a2aP_dwuGMSLxwOA_JD8m5I9gftiprpnsqfJg5x_cYtVU9AJoWYnkWW_qlX4Ogj-voIAbjVPvKuD4yCb69WcV5kkx5QNci2HY7JJhs_66Hq0vYMwHs7LHVMPZjXND89wjkbIYu5i5Sk1YMSaYrSepq-ar84AGOBRuIHzvGEXflTrq0m6dhJ_M19vouWqN39BOe-a8mNAeewlEtuTlhZgHpgsZGr5PLTVg07ZunHq6N_56yfKMYtaE0DAD3pfYB0br7Pgc8kb1DVytsPLhhnv-cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEzsD2MmqZdSA7HZPT4qqjnNIyLVQA-G8Vf2qi3CaBjee05nyFiOWMWZD9seXoTck_TMHIllbjSEzyiGp62io0d8Lxo3TZfd9KbAaZr4V6YgQuOwCGrJIDaVt6l5KzBCXuahO15M7IartaKuMwUMg0Q1tcsFPW5781f3Ty6gJRw_sjMY-1_uC9BqfXYNJ61_GOjgcYYsIifYe3rLc4vlYjRwirzg-mwj2CEN12RIDqnaMlWhXOm1t06-fpIAybxybi8IatxgB6_yAPdhRpY8AQ1Wt0CC05SFqcrfeCGlctPzsQxWWEtIGmBHzJGpY9br34nMp4cYjBAnA97Vo1kEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa83M92MG7oTJUSQOFuSJmxtY8WfpPcuWHU2BICmdCzNN0jrBlNv_HOKtJcZNM3xOpSe70FxWQCdVYb6jhyQGNv5j0N3HPwgPJXIoaesVcWzlUNb_iZ6HfL6Ra0Ca00KXO43DW7kkJ59BMATnYACBIz8lqj7YCjkCEbx16ZVHj81Ta1R5h1lgGzFVLuV2iTzCtlWR47LmwpkP6X-KvL3gAYITTmHe_UWs-wEoSXZQpaW-d36NqRvz3zjrClv8INQU6wVV2vogEC4A0YGIwgnQtHS7uDDtutr6bo-X4mjwMwQwpi7p4PHRC3yxgcHfNE1qXos9ZuPbOFeMlFGVl9VJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81297" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=DgaGIupKHUV1L0B96y9fhw6kMxnRQ16atc2NjzzBfErxGa1TA-Zt7F68Iv_Od_UyUsojU7EWnwh718Mn-W8z7DzAYdAiG1Zw_IlgGFQghcVPdz9y-U-Cca57asy0NNrwrAmMR6KdUgvPKXqef2ReMwNSkvEwGN6K4Cj-G3IDwvl1PXm2pSid8SI394fjj8jj2oH0cyX9jt9J0HccIz9GR_WduBZ5O1XV5e6gIbAXUL73OP28Evyf1_mUyU2Dp546_iEdDuC3N6pzpvuMpdZKaMO8dW2FTI4GgvShUDh-qAY_AEw3GiYRJXWjqz5Y1nkMzQ9KF-KIZja49gJtJzX2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=DgaGIupKHUV1L0B96y9fhw6kMxnRQ16atc2NjzzBfErxGa1TA-Zt7F68Iv_Od_UyUsojU7EWnwh718Mn-W8z7DzAYdAiG1Zw_IlgGFQghcVPdz9y-U-Cca57asy0NNrwrAmMR6KdUgvPKXqef2ReMwNSkvEwGN6K4Cj-G3IDwvl1PXm2pSid8SI394fjj8jj2oH0cyX9jt9J0HccIz9GR_WduBZ5O1XV5e6gIbAXUL73OP28Evyf1_mUyU2Dp546_iEdDuC3N6pzpvuMpdZKaMO8dW2FTI4GgvShUDh-qAY_AEw3GiYRJXWjqz5Y1nkMzQ9KF-KIZja49gJtJzX2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=KhHMdCVjAkhprs--SKK4RTyvVOqYeFYU_FksSGxYBp_Vjn-NOXk_-IGwCXg8bfeGuUC7lRfY0Hz-na3W0__-sfm05JERyTluxLNtk00M1qNRf39rFvT0aY4pcBjoNXq7CKwg2uija0SQwQCS_2fprdAMrlZycLEeEXTDKINnOgYRU6JNZMK4Xf6u0_sI-qvxwc9klcnJl_0XKGN7A8RFhCgxUP0HegulWDbWI9_zBf6ieVe9QZcMjd4_wvWPVRNJzPk4yF59BqLzHGO2ayvYUey500uNClHrAlYTKKeaD_Lqh2IK3KctGAa1_HYyalO5tBsK1phqk5a3YL__eXeIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=KhHMdCVjAkhprs--SKK4RTyvVOqYeFYU_FksSGxYBp_Vjn-NOXk_-IGwCXg8bfeGuUC7lRfY0Hz-na3W0__-sfm05JERyTluxLNtk00M1qNRf39rFvT0aY4pcBjoNXq7CKwg2uija0SQwQCS_2fprdAMrlZycLEeEXTDKINnOgYRU6JNZMK4Xf6u0_sI-qvxwc9klcnJl_0XKGN7A8RFhCgxUP0HegulWDbWI9_zBf6ieVe9QZcMjd4_wvWPVRNJzPk4yF59BqLzHGO2ayvYUey500uNClHrAlYTKKeaD_Lqh2IK3KctGAa1_HYyalO5tBsK1phqk5a3YL__eXeIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMxyo0pkZSL9mezsaQm0qgPv8jbfkHxDgbglLua1rzh0vEFwZOY6oZzzEtqljRLWo58konpbQ2RvA06mccZXuss2kmRm0bjL8oyzmmqjDCQ0PYVfJzdaDIbB4JGAb9Nfms0_ddIDVlHz3pOLCAv8nEd-rx4xjsKbtlb63jLvwLJ5IDhuncMmMaO30ry1o196eoj9RcwvJYJsulYinBdMJzwLramza4-yMcCbGvFmpWZu86PTLGaMlW5F0MnzA7hEdwPAFZVesjp0EahqRGC4nlUeuCF9FaSg-X4MSP_I5rJi4SLEJDHgd4KKVunHbq9x3-Ef9cLatak9NgRZGP3uAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW3ivOHbMjLEIZMt6z6wx4jNY1GiL0HY2vfibArnhCsvar829tm4Zmd90vh3wHKGODz212G5hdjQn6t7wN_lrzD5BZ6dagkNGjYgK_j0gZiQ2dUVZh3GybEfn5uzy2nagC4V1dHDSrQd0gqk-spi0fbAEYgCm1bSircitBe9xFMq5KScmWY8Twq-Mc-EdG4VT-v0NShEhMgxUzyY4nJGlDDH8JKiTlMIInP_NZO-jruzNkFzzXn6BCmTId7D_myogEud59roYsI9MdXk7_axBCqlVApvA8kZXu715xQPvjwwnw2mzg5O11qeWAAfgSfcjtLIjG5Yb72Yc2lp_u_qAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al4gckWM23SOXid2sjUNW94Et396PKicrSSPjgUiKyVU7lPcFSvTA3iEzxkKc9_9wQosm-Us0jfbTRXrY6VoZyRcFIFMWYJ3zZQMLTCBfO9QsVQXcdlK7i9B7Q89HmWpsEd_VPObu-WPJz9qVooJWdlRoxsNLjZBY0IRW3Jq2liUdsg-3bSJfTrnNZGAD7UfJCqo2Rk2bDMSPUdRIHet3nvMeCYS9-hQomnu51w6sGQyZJXNkNm9-OO7bX4yZdSHQwsxBhc3VcArdlqYcab87Ed_v6wRCClKI0MTuHkY-31DTgjRtBtNBLh0j6-VuvGsAf161uhUREz3-hRA0Q9TJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVVNud4jtYv_i83jQmXIMCwfVOB9BonVvRF_veYyyX7rHkrKLS2pHZw36ldDXWRJUL4zOMzzCmJTMoKb3zXfANh-v1W3_3eIRjoMja-28fJ3EvXeHieipriNQ654D-pjiebTe5n2qDOPYR923rvCzNXWb_nnMiInvRSZUgAGRCOkpO4jUrsXtcYANK9-YO9XtZy2nqHC9TyrwrRMFDJYSwwP01k56IdYniSl6_B17oVDym61s_Dah-zHB5F1a6zfNeLIldbu_K826zkNMy2YAofHOxGTOxaUeXF5T-URWDdXRtJI3i6400o21ru1Dtk3YiwEFsPyWW52AGGbxVTewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید صدف زن هیپهاپولوژیست :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81285" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81284" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFYnNtLCRappVOm_2QEkEqW3RiOu0juHIPIZ2thb3-S6PjuBp_GFx4zOIuFnfB1dhyk1JPVzB-efyZ5pibaOpcLiUqkWJMrwAnXgHnJdHve3pclaiQ-gQJiLrhxSvJXn_ixdyjIiprzoGD5-xqvOS4eIi6box6JLzX7fMpCWbijo9ZfjgSrp9JOfvT-IfwaG5oOfVSZ5YM05Qdn1Jh1S7ysNV32CYDwES58zdps-LHLH06CqCDAWkRouoWA-lhqik35A7ViVLNfeI0VQKzc4UNpbiaZ2ZMhE72Ye3Fg4AYFdiQWhwYmxbuCM6gWYDkHixJ9X_WdCDH06XhPGSGGi8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تجهیزات آمریکا که تو دو هفته‌ی اخیر زدیم نابود کردیم ۲۰۶ تا ۱۰۰ میلیون دلار قیمتشه.
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81283" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خداوندگاران هفت آسمان را سپاس که امروز من را لایق زنده ماندن و توانا در شنیدن این معجزه‌ی جدید تمدن بشری دانستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81282" target="_blank">📅 10:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یادش بخیر امتحان نهایی فیزیکو فرمولاشو نوشتم تو کاغذ بردم سر جلسه، بعد نمیدونستم کدوم فرمول برا کدوم سواله، افتادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81281" target="_blank">📅 10:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkaYnRxR7QOb4oUIZmk6bDlW1njLUWm6mss1CKY3svSLAghfuCQDGYnka8ZiLhrHpT-7giQxiykEZAtZHdMuVMQsYcDC-7rx5q_3ZTnue7A1DVON8_KYUjS4cT8b4UwwVLhuYT3gTR4h5ypp6WGwYHoaoT35eJ5_5ccdS9uNcnzx9r7og9J0jNhiE3HVmIsjsb5w1l9H6c5ieYUCgsBiTCQPVeJnTltRu2M6eDyTPKv6kJdUfF2ygwFQNwz3mQShOQzNxypqma2R6z5eVUlm7PiGu2O7-jtu04Gs07LNny5gn1WigupL8xJfm9DGSH2vHpXm4c2-ikCjslE6ptsblQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاسی بسه، بریم دعوا جنسیتی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81280" target="_blank">📅 10:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آلوارز کلا سه تا مشتری داره پاریس، آرسنال و بارسا، آرسنال چون داره وینی رو میخره کنار کشیده، پاریسم چون فران رو داره میخره کشیده کنار، فقط بارسا مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81279" target="_blank">📅 09:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امیدوارم زودتر بمیری مهدی اونوقت حافظه تاریخی داستان پسرعمو و F35 زدن رو به همه میگه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81278" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81277" target="_blank">📅 09:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81276" target="_blank">📅 09:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یارو پیرمرد افتاده مرده ملت ریختن سر جنازش میگن ۳۰ سال پیش خایمالی میکرده، خب کیر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81275" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلبریتی تو ایران همین که خایمالی نکنه کارشو انجام داده بیشتر از اون بکنه یا فراریش میدن یا یه بلایی سرش میارن دیگه اون آدم سابق نشه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81274" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrOjKXncrIdk1NfsXlV1nsq53sGVr4T-Ia1Zq01Re_GiJedpe5ZmCmJ_4UnLlL_68izDq2rZxhdYYuMkbEuv14alzSAtKV5I1agXpWLR8HTFlKx7K4QiAb4QgrgpvmJ8Ywdiyru0QeaZ-4-LypU3d41-g9veenApp0G8EeTIkM90asLKxbMkI7CuupvYlEfHR2vksVhj7yy9svlWOrXpNjsgd3zeu30M1O7gvEzHgTKScCt5AIs9iGYp1qadaxAZ8n4-S15DGT5-WzjVuqP8uMWUzbrUXSZUYVnYwmbizVsSH44J_iEzljMeLmuP5A1uvYmFeAtVecaChYyYcXEyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشید مظاهری اومد مستقیم گفت، چیکار براش کردید که از بقیه هم انتظار دارید بگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81273" target="_blank">📅 09:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwrBmfD9ak6UdQxvVtaHHfM8IwVfgtxWdedV8ob-EktyEfpMqfwcapGowtu23TJSMg86rRFxJINhGBgFAv6u3nSvG-0mlZRWjv44U--YdwB3g-c7OW2CIXXe9zqjNQeAANqi9RTI_5ZYbScmJGAg53Uloe778MkgaAO0fwB02vxdwlYYPGBACtKShRMJi15C84eTIH2p1R09SJpPY8c65u2jAa9ua7ZIKCjduQXn5noM1LxBxCj1xABEA2-JDWrt3EU302SuLG0m8EGEgmr1rRNy6xBM7nRgY6IfL7kc35sfHT6YT0Xj7vhWUOaXkHa3QdGwVaAvRxvMgltVoiX7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81272" target="_blank">📅 09:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فیتای ویناک و هیپهاپولوژیست از سپاتیفای پاک شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81271" target="_blank">📅 07:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdbbinUrL21biWWuuIWdxQ_NpZkIT4oMXErHx9Jy6P7wngVyABlGdPOUf4ztMLAYcHDo0lusLz7PRZj0ukMqQ0yuxJt2IrgLY8IBRu0pTdXA_9VDm4Z3QPjb5T40EhqURSn9QdpJkENEakf0TEEob2dCqgJsp7BDihlsRdukFLP7D9YbvgKYUEzc4W_NIG4nNJXbxX_hvUNUFBpeRUCLazA4T--IHpa4MEUkFxI0zukJEkOlamyfnm6ky61thckHMy_DAqXk8uOKmi0o44gAhycDXJyZO_0uFVLa08WiAguU5YQkkKQzvHm-TqA-tlAFN-YGicZq1PWhjq7xk6kc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود هم پاخور بوده پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81270" target="_blank">📅 02:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ایمان کیرم دهنت چرا کسی جز تو صدا نشنیده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81268" target="_blank">📅 01:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81267" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyBRFDkLDpCuZCExZONFn4XEOCifJKOQbMbxvwnjdkSEu1-lIUV9PgkPY_hPjXlce0FUQVTgP-xCWgUfy5v7XmRsYppPzq4as-U41fvMb2uDHq2gCq0jan1OUfIUs9sh4tWI38qtWNKOF1jIMHjhaVLbM9hDCYs1dLkQRfonmOYdnl1kY6idwiuhlaVpnzjPyovPoeO2N4v2NoaYKb1GMXB2Emp3_2-rvsKpwUpcybDlwhakV65Q5TLO0ko8V23DssTvXhIC74osepBPOWojRGm8G1BK84HRxFOffaNyIQlPEOu4nWJ7ifYRQ2mI3EgNJ5xWZ5pdScfmVo36xXjnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی رپفارسی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81266" target="_blank">📅 01:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81265" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVESGyxZ01OpaUgMo1HbqJfrplEznL2ftfomt07vzDVCXLmPFI3nxqEU75x9_kZiiuN3J8PKa3R0517XmzMu4dXxHstaRop7fYuTwBRnhWc2J1mvicAwh7JB5mxj48Zwd00z6nbakaD8OKiECTdlMGN_DL03JbuEvjwB-6fUq9SUscg7rRLDgA7CRx_k3n2RRVZaH4m5QAjCkaq853TBYlap1_zEiZqjlGWab0sHh_KjoCKredkJnwA5wVgdjuZV5HHI8nqLu6g5IaVV_Depul1cQ6KUTwrGvhGG6pznuxL2ORQI4Wyi2jUeSBCPUZTBh44y3aNTnaHVaXjAwYonaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81264" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">طبق جنگ ۴۰ روزه امشب شدید میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81263" target="_blank">📅 23:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تموم شد، دیگه هیچوقت، هیچوقت نمیزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81262" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ در گفتگو با شبکه LCI فرانسه، درباره ایران:
به مامان توماج صالحی قسم این دفعه
این‌دفعه به شرافتم قسم بار آخره که به دیپلماسی فرصت می‌دم و اگه برا بار ۸۲۸۲۸۳۹۸ام، ۱۰۰ درصد از ۱۲ درصدِ نصف خواسته‌هام برآورده نشه یه جوری حمله می‌کنم که اصلا خیلی شدید و دروازه های جهنم و این داستانا قول می‌دم قول
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81261" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هوف
کانال ۱۴ اسرائیل: ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81260" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585792e34.mp4?token=LC9n8KfM0K4eVjN4N-5qPrkMQ3c0QIUFOOmiqdZxuZjgm26Y3cCDq_v7WcnwnSZMGX-KtKPL075aa3G0z--uAwIKLx5o6vt4JlGeH8dN4jbB3Qd6FmJznzsR9bdX86kjR09wmYg3v4d_qJrXh8ah8G2X2lNXnER3eu5JoFjHmXMzZGMSGZebBQ_K-Uf2oabIHRmJDpcJjYhlRADLYzZnH6R8rWpUJcmVifrESG7X8KVEWacKTFulv7f4k6_LeKNSNmI04FkhzHugE0eUR7iHpHR7Rupk0FV7LN5bQX_R6kyc9UKr_KnqsPrbLey32u0zgBnlNIew3Z9VmpjWD8b3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585792e34.mp4?token=LC9n8KfM0K4eVjN4N-5qPrkMQ3c0QIUFOOmiqdZxuZjgm26Y3cCDq_v7WcnwnSZMGX-KtKPL075aa3G0z--uAwIKLx5o6vt4JlGeH8dN4jbB3Qd6FmJznzsR9bdX86kjR09wmYg3v4d_qJrXh8ah8G2X2lNXnER3eu5JoFjHmXMzZGMSGZebBQ_K-Uf2oabIHRmJDpcJjYhlRADLYzZnH6R8rWpUJcmVifrESG7X8KVEWacKTFulv7f4k6_LeKNSNmI04FkhzHugE0eUR7iHpHR7Rupk0FV7LN5bQX_R6kyc9UKr_KnqsPrbLey32u0zgBnlNIew3Z9VmpjWD8b3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از مادر رپفارسی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81259" target="_blank">📅 22:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=CeAMVTKGoV7plRShrEZ8AeO7-GP8D1W7gpG1KIMKmr9hABhCsBf6hmOZYF2mZLCOaG6hnGgtHmSOyhpGlyYEMnsD8AS7_TlQhZ4IucvSNZhrLar3KITyYlLSp3tg_5S37P0i0w6yr1rSy9Q5OTtHgfyDE1y4UoqJd62aCKf0MdMiHJasvcv8s4RwVynpE9tqNB8nm7gF7gPcWdF2niS9T71c5fwEEUX0y-YajkNP4h7r1QuR1va5bZjqETTOar7akEK3Xu9aU1zkZc0fS3XyIXT_5tmmdclDb3E8Ji2FDb1P-9oiIRB-10Jr9Q6pripmsaZU3o9CeUnOk1T6DKSc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=CeAMVTKGoV7plRShrEZ8AeO7-GP8D1W7gpG1KIMKmr9hABhCsBf6hmOZYF2mZLCOaG6hnGgtHmSOyhpGlyYEMnsD8AS7_TlQhZ4IucvSNZhrLar3KITyYlLSp3tg_5S37P0i0w6yr1rSy9Q5OTtHgfyDE1y4UoqJd62aCKf0MdMiHJasvcv8s4RwVynpE9tqNB8nm7gF7gPcWdF2niS9T71c5fwEEUX0y-YajkNP4h7r1QuR1va5bZjqETTOar7akEK3Xu9aU1zkZc0fS3XyIXT_5tmmdclDb3E8Ji2FDb1P-9oiIRB-10Jr9Q6pripmsaZU3o9CeUnOk1T6DKSc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس داوینچی درحال لذت بردن از مذاکره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81258" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMzF-72jpWoxVmNCevn4YA8HDoRMg-TPP2xJ-MRlAFrZyqEVdFsO6OaefNGNYSpWMmEZR5AK8WvRxdZ5lXvGtSy_KJ64slqagIdpDc0oKwa5VYs66olTcS5tN0Q9e_5S2OqZ9oceG3nZEoa_Mx3A5UVVuUNrukko039HJ5bKB4A623jVL3_aZuSI5spU6T5XwB0fqjXQ43apUGS39-livsJUkNz5NPQ-CG83WTz7BS27NX1ZwBnVrNs6Jq88uZX0QeA3co9hxr1fk4P1E7STCB9Bnvy1Xso23ojs7zp4KBaWHAeddeGn_avPDnaisou49iArRHB_TsWJ6UpywSw5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81257" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5CXG38lmk1GCpWqBrqVL0XMVkwJlZORdYFVl3zdSbGMf4JsZZIb2ysCiceeeJ6OHNY1hGujhH4TQbW6tJqNesPSpAb4wYLoT2ATVFXhriBjOrz2FhfyMfXMxkcXoE82SOCGnGglpMmorcJA18fP45nSVCGVX6l2aEdSH7eo_QBVUNbBIh2rKG2DgTrsog64UdoZQrRZpq-drkMPyIQ87sh3RvrJzOFa_qtHssDKaq7i5LK7htGPjMl_Y-PBvjET4LTe1EqXx9yYhtfQMWBzYhglU6Qy2W-46KyJZFvWJ85Jp9jkfh0L8OKiynAITxTRSs-wRJgCzdAypk7FdUC3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81256" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICNtXO_4sFRgF7jWrbGqKHuNUkgBRBoY0upO6ryM4dEAbH0UUAIuVzgjc-HUQGZVx2scONGSAo48enjUcHc-EP_6mnWkJ5mvvy2XQknAgFIMECuYJhGtk_q1JfaU42HE5z5dU8PzwnGQUAfq6wmitqPEej5edjcTM1JJjmdgw5Ej95BEo0yM-6eAgu36uzmIqBUpLfuvbEFbxK1676OSxkPgaY9FMRcxsNW5Wkaz8YPEBE16N9EWLQkAR7IqS8quZwm-VGPwEYTjWRqQfvWrSk9s1QAbekhsWQDic8ww_nQ7RgW3pBKTmqJpgV_cX6v_3twalWDP8vYx1PXZ7F12yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید باشگاه فرهنگی ورزشی لیورپول :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81254" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قوه قضاییه اعلام کرد که ساعدی‌نیا حق باز کردن کافه نداره.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81253" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Juw--5d0afo03Dkpt-S7Z9_UyZ9riAw6AVJQ3taMFogHs7nrdR2iFCPMUczTJE-ZTDe7FriRUpXf-uK5I95DOq0KXPq6fxwnWIoyWe4FxaEn7qfOCfPZN5x5hQVzLU9ujCOPv-r-ihhkVfdjlyLr49-CUDPSVwEnkEw07dN3WEy_zn8iY8uFqU3CaGgaR0w8npqMN7TmcOTP6q1xYpWHYXmDrzKn0kQi5P1hk6mBgcyGOaqtTtDw7hPmqE5Bf8O1Q0DJzj8dVaRTjUktntNehkqFkI1XUJIf_HXBgux8eP4cVAgO0-Dy-e4oDfFYxKP93PTNB1e-a1m-eHW6SckuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستم اینو قبلا یه جایی دیدم.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81252" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV2BCUeNwOIKoFBHbUBPqZn0Q17yv5YiXGyPsPq-6f6nGyq70NdyHkLUKJM_lbTVbnpOdBNUC-s9piH0PgaxYm9mCK-j4AVPF_76-7iodvI4B7Yt50DGyc4Tk-Sjt_HXQW923pMn9yLCicJWc6j5hWFNW4tA_suWPslL5CGQqitySfyOwjdIzK7qQ185ym0X2rHR98OH7VUps8D6ZSLQiXAE-5_qDoQ_y-hde1O_HFLq6DoWKNiFxoriQgfnMl8HE1OEHXtyawXOT1qbwLiq89Z-ueY2H8PXfRNIuRKHk6A2XVSvqbZT7UitXaeSjH7bsgfaeng5ZaRQLNnF-JKOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عباسدرمن: اگه وزیر نبودم میرفتم پشت لانچر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81243" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFwC5FgDgu93DMpRu_QUFYoJuI_5FQOpO_lrcWHIfJip7qFmL-PtmH8rcLZyNyJk27CGcyGZpsLK74-zWh4T2Vc5fUOVgrOlP0FNvTyYkegIkMrfKzcnk545aTKG5lyr6Jtkh8YgeyaEQZABETJuvNiPabnAXd_dQL5AJN5O5FT4NOX_Q7SSzMwJloYIJju9yjfbozqmmPzho9fnlz3Z-dkiECfShrCfsN3ObKXwgTKYT90ykZGosVGofzRVXh2HzMXsc44Y0zpVIfin8Ar_7rreEQ3OZwQDGY7rebi-ff2GWu-HnAww0foYztRyijwclz-IruGeEvsaZlX0oeXp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ما بزرگ شدیم علاقه به کودک ترند شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81241" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
