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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuHov7D0WEAGWpEhUiPyoNp6zInXC03SapYCuZs_1aZlgK5WN-sasRle8bVZkXdI9XS4drR8Q-vSsSJfJJVsPjfBAWTsoSYPPfUhYMnL0Mt-q7K1iWkY8NNIoFOmuXiXFTmGLtSWGg8FYZ9IenaX2UTSVRSIvSi8WaEEGvG-DIrhrbzG866GSBLfqL7d4ZaSekp0dsmJ8H0pLaFhKX0CfZ75AJXqiFzGNV77hZIRcui_v_Q8YEq9x2wRiOacSpYVC082emngI3-xq5MaWZHjWpoSO080_1O5FwMOGl2xtPuN8vJWSUaCUVNHx1KHarySO0XSmvrR7Uw36Osv1DbWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtXdUlHgGWLPaMMav53mBaOzEh6LVMfYFMv4-UsV45MjDUaFIArMQPFU_PtKxNd23SnGNVAGAIYD1q2tOHbMqLRvJr2erR-WorI_RYY6dCDXAZB-oVpHN29GZR8LEv-JEaJPfHeVq-u2BcIb4mKbRnMCk5FHxCI4M6152FT6w7U_B_Ysp002lQ07bNKRYksjDOrCO3skheQpPUcsTUENAA2gpTYlRO3Fj5-YBCxZTRMbnxUjGyCpmab81rPRdIthAVMegX2SUC18xRIEwvF_lAa5phmA2vD4UIhIUIPm-fmGbLfjUAZCNKio4BjKge91wN0ObA6UDajfQvj-TJID_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB05TqVfC_Au7z2uzprRfIrZiGmt2MCXSOAgO9Q0Ll0y8gbttKH3bjY0qRfKTDI167O_qZbH9o55pSeNhr_Z16mrAEwO0KfAEeSZlyj7k7wTmFvPKq_E9XDl1CTYhJhExebbPzqvBTRgpAQSmFtyRBkJUO0HpVvOSUHsFPIRbk9KfJhOl_qqL5_AqfoJ3F6IE-vS6uGT5Q1H6f0ma66cU_JqpCkMlMWKLwwA_jE9A3XyGa0Hr1gJyPQ62DC8dISqD9WXnswmMB3pZAA9KE_Dr3SciBkJuvITCUgRFPBg4pvuNmH22wTAD7InRM9dIIar-lDL3Wc_H7DzXkgZdTXVdWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3px4QhoCn0NQgV0lL113tmyxG8A5PidvKfcyiRUTsPg9rfOQclGEfmRKk82S5gsNzfqv54eeEpez5IeeByRGQP6A18EeTiA9POXeXEv4MW9suqPoK4tQpi-rZceT5_qRv0AbBRelyEE5JMAl879Wh3HWKld3TVez9LWZTxhy3mGsVKIrxJpjXhEpA4yaNkBS9LTZ1KPgP-So-lRL_49omyfdac-fgROH09zKI7kPyohm66vDAzs1eYx46e3ZeDi8MpT-FmhlxI2LLIMLXQlmcNX2bRkufyHE560xuA6WKr_P4yKu7MHtho4ktGgBuP_UbDBeOT7ollGiq4SC0lGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZy_KKv8_xTw48R1cIjrXtzEuP-D4lX7UttWyPh25-FpSyLCJCOwK4d0as905NQ2_ZQNAHqOgmTuhv7cLcn_Hf5gsXtEDHPqrH_JRzTiZCeqTneWw6h0c58vJzBHo9a7tT7kJWz4zCRaqWNoWyWCYuWt6vdx0GN2_tYcmEVbNGeXxXuuQssYGTxsInyR3eBjgqtAEPM9l6bfUMPWm6_O_8-phGjVjWVHDGCz0uYlG4nuh1YcF-w6RwjvsrB5-lOPFjm94tdT-o2f44RnSjULqB2iDs0JvarXocHVQCNGWFzu7AEv2FagWt8KZq5-cts7R332pPWcyqxYcXqTbJVOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzqIoAI6tyQboPiUED7uksTaKPagHrKbkP0ky3Of4lmlNQCx1yXGE1cev9cb40Zp0fw_Nqqwe8rarPw-uUbSnrozhyZ4lm6yTyVYofveOZFvkFyvNH5VhYHUKImdP0z9C_QXYkMSZpuUJtZvHB-9fswmS8FmUFruilCWay6VQi9iuJDSGOcgjK910BsPEjzf_CbamEqIj-puHGGqQvw5J08iNzSHRGt0O2IL-DnlYhgspiO-pvQVWkaO7ohftQ8-OvhYmBggJTY3QAyrAmPoCpmpv0WV8rejI3gvO4QFd52KFZ5HsNiI7izsJ-f0xk3iARxEa-l-T1ypXIt1THAFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucd-goZn5RzXxjI0NNznZHLTTcwaHqaAkNmnlVmVLASUZ5ODX1TVB9w8HITFOgpzPnm90Sob96fnC2U1hTu413-rm8kPwuuPn4ZORMjPr6_P8Pmo2uMJGiJpyrY5kJhLgBHma-zllwgyJU0CbGEpnn-ouqQXx1fEH8rsxAJQk4XTNZT9fxX1YVflm3ykKd9tvNhlQ0CEUVcT5soxxofE-Dq2sR7JHvR0FF1jWcuAu3jr4GlDi5PjWBay8etjOskIzLWvwKMLaE8Cd-1FOeBHI7K0X4_KZh96LZHibSUDK4N3haM68GueZgORGOarx27Iwe6s_jP-Q_LmvlLngx3CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NouTR0r7ByTgxyBm-WcwnOhMC0YCwXAfSLYYckEGuJohr9W4pGdOPnM9xL3VIvbw3q6gGrozAt3c_0JlOnpDmA_4FxQsyAcaZw7wRjmzQ7zAcoqB6DVn0TmoWowANmFyIE-D97RqsADK_HiKEZz139Wsx5A6mJc5ydSrK9GQ4eBa2LO5wmh_TRvGXzOmPh33dQKi_5stvnnvj_BjBicOrXomY2hItjmMtzD5c6Cn1FiS8tL9jnyR3gQ0cpaeiSbDbko7Z0mLTRI9KOFc8EiqyVZycFuKIRosdTKCXxxOkX-Yg7vdsXB3HOeeI4NaEqA6jR4xfF-abR7CMRggJPPLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flZP_YVipT_xRU8jU1DZ2ZItE2Y-46SGmrGlPEKXkp1pnTa9CHPxOH5HJtnS9TOFBAeyYMFJwOa7qg3ODv7R4UYkXPcwnMfGALsIVwh_QtGe5ldXx7ipGdmKI0tJkdCIxP7Q0U_1oXA4VxskGIMOm2qzcMNUP_Fp22lwymHVhsIb_a4rU1v6ccmbpqadeM2XqJub7QbcRg4_IxGCd2sF4S0EmHPUGAhYlE6Nv6FeRHJ_bZbH-Ol3bWXQ5EL6FpVmgsNt-UPFZk3PpyqqQJPCKNJMiBY4W2KWYUvnxtiMIo55aP5w9ViNjlcPU6NgPbNJM3mhlEXKc72Xl75hdAlPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAKBkyGMQhZqFVkWvR824LmE53JHl1BRWnUj-D8UYt0nt4ysScykwIJCKViKUvmNxT3GCeF1LvfSGJtw1ucmdWLRYYStmeu_wYFAduHLHhTEYW2NSEOb8s9P9Z8MqujlXerrLbuFk_f1WkLABYlOgeAsidj8qpOAkwZp2GAK5CXpG90r6UsDPSkvvIcqLMPphBpCWw5p3ncWoS4dabPfbTg2ekUlXve6qFIM54m4VAhoFEQIrOkrm0Q6RYBIeqcslbE8aMiJs_kHr67xPHLdrhLxgwqEibrdLHS4VBat3v84aXoJtQVUOQoRXh42dRZvbpwN9ubZHR7HKnmBHrAJYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1MOJrhXMW88Orxw5asXvDN_CzQOx7L4qWFwR3jziJf6w8DyA4XEKt03JDhmDzADghPnUhpMdInKaKzgLN6PViVlV6N8o-kQ8P38_Kyrh-oMwJXPgpyyzkXBbumhcqCqe4shcRWNqY5IxOHHmxPEj132HCDDNTmLse6d4ZJiGpN611EhwAjKpxJCzrluepf0ZkIZ033E6rwABoIFDV-V3ALIxSE7okBINbL220VerGTCBuWfxPpC_Ze8KZ7U0HxFeOI7NfR-BliVRpX6HyTAqbgP1fb61K0-72M7TDrODAor60Y2mcKMYD3khKR-f4_5E5UI9V5CbryDcuFGxUjbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEwL5_OZhQQbpGr4gsiCVIHgUtuJSbG-AFljFlerMuWfN3JbSb5rIeFNQHDpOZfPVQzdydI1AxthCLW1qeBjxx-2GbbZ61yM6yjTLyXNgw9gMOXb8lDGaZaBJiUVY9hz_8fAOgQ6bw73IJSnQY-Q6QgqurBUm2SiKFQL0D_giPyalEFoPk98OEmmUQxkn9t7uBYYXFOez9lOpBl4XVIVsDpPc4ZOv7xT8Ro4RHVgchkrjSWAyw_alECLXr0IIale7l3UVTpr4K6NSJgWGlM81x-90c_6uBkUA-ypGyHUwQo9vVxF77wRU6e8NUkkXbTe80fSA4NVjlA9S-uFRzGkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBzZH443Fh5-dmQfHD2wn_u24skfpgIxuLYE10oHQtYT_OP-lEost3YOiYUWUK25RfeHNC1FcJMf5F7er40UP-lKcJz9GZYCwM7GmnErAHxp109i8Yf9wAQRvkUszAouMIhbpbXcVGEhL3BHihuhx6iJuMm21dqarYFdWcotOUKdWmfesNutFE7or_nk-ZXBV_YmR3FFk1TZWOtJpCXboYqx73wruHtmkonNEGH8tgY1p8j-iS76EpsWcknaZD1f1cLCYzSx4tIdj0b8j0OIB4uF-wUXy8-OfK6LrP_Yeha7-q4czZ4EQhhV-CVMlgPMECjdvmVaWaA25f6Gk6fF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGOQ_LVlCT-tmReaDAfXPAwJTkey-3XxTc1esIs7kMVvRY_f5047n1SVttLjSV72SIGu8yIQIEPZLZJt1dOkHT4-rcaCEXEzsojT5j5uBd-szCGlveWomlBckz3ni7lJhKLaRTIzeJ1lGnRC1hZpQIwFZ_olJyN-fHVuwpRS8gvYw9KgXx7uwKVhH7OkouquC2YBC9i6W451GLJCAh-vqRYpMxIJFxXPjE27wxmHv9s5gENzc-FqAieKych6gPWjSgNzkClX2SI3QoZcIWe7yo4jDlx7sjcbo8dez6rMjK76kxauJSRE86ryRsqRWwOABffAmqNW9ah4kncN0KpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfAAYoSdIp3tME2ggTDuDhBd_Zj7UZuCiBuXaATYXYZaVC3MjDAQyuqvnlcVbH-A7Z2HiLOwcYKH9XiVyv7iN7zWSJcuzpDZaBhoZMLk-ptbY3medJ1ZrducDhFVOs7HOtmlL0xMaxD0NVs-SJp_eY8gcXcqYIxYFoYnxG8u83kpN4aZl7RTnb-V32HdQgHhWlfA3F2-ZXMbkmxCj6OOKlVckp2YzrQNiMdDp8h9UzhR5C4OB0JLeEhFpC5-lZPviI8duBE6o7sfRKkztbetq1sBNf_iuapzbRkOzGimRpIJOzL2KXzshwO5D7YPUbYPkQ12tyl-iEnfrzirqxDLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDHPhcQueMPYBEc2I3MO5_j5ukORb837hEYI81CQoIcmVt0HZ74JE5FivLOLp9K8urFTcWc4E496wfUo0QUd1KeykkjD7h59Qhn1wdJpZLBcQe6biXefmbNfZ-McDarNdBk1djsE-AXDJdIA-TcMK1ppZlOH4OC7rfZKaeiVlrjbrOroOz6Txs6lqOBAHQ0IcP0KL5NDLZ185fUIIfWJZEL75edPoipChM86v6zNCQX9RO1JRxhXOQ9DSMZbE0gbs1aUT7lgouJCUeURYrvv9Dn_uyRFA6ABcoH6OhJ16HsOHm9ljC3ZcnRiOkTucx-OSGMpTBRAbumdDK7Smt8FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDB7hX2nlnFlXLk7p2N6Xl22BDXB3kUQd-Db-smW8daFEHc5DoVE3lAqlsDnzQ4nUzfJqw6WzxkzkYfBjxekr4iCjzo0zymey5KkGtrDF5GJBv4pfgVWXdXZVM50ItpMgj19RG8dg1sWbeVzKDQhynFFY-fl2btbpgQIlfvW7Q0SlQxHiyP8MMP_sryII09c2ZvL_yXlsslJpINfU7ESqJcK8vM542YxdhGOUnJX44A0nHJtnAotIeo83IfH-Th72pLpsDgwTAV_69f1tUFhDEDuqYN0vt7dogTVYWo5BuJgmXQNT40i-xoscL4PcIpFA1VDK_LiRmFs6W07NSOA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT-BMpZ4cmEZIqMzLwLUSCIpjYTJvpu9sLkB8qAulSxfbmuSIV3Rab1uUEwgVMnjhR2rjUKjfr7g1Nl-0iv4WJxBOV7R0KFLM1Jb20rSLof3nW92JhEz0ZwAStVUJzNsnw3kgEm3rDa2Aw2AQNYte8Lkr_KsE6bHco5fJ8jCHIjpLYW9uNahizVDbgREsViYhBVz079wMZn-ovl8dUptqLOvAwal8I5EcjmgumcAi_QoW97MlWwwtBB8Cw7O9QJsOGJ8muAks6Ut9YMMfz1OyYrP0A28j2iGtbnVWFfrcD1kReOMtO1-Oq1AJY4IdReM_fXz1KJkDl5gYnDZreJ8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm4BeTBYPis8zU-uNYauhHAhdRPUnpbNENkme0Lz5N3NXHpHYBdmlsFocTIAgxPI-iv-EHtcEPnu9CDWdIj6xW2JO1wiuLCs7qooavWP5JaGLKlCtNjH1ej18UHPMv7mHJ5xpkxSIZTUHXZaZDLUvjJPpR2qCxmkY_MmJGmaLhZAqPsVsQGMSzsQ7jE4mtBOMGvn2s5YLbyjXNjAwVRkgxqq15qbisKrzyOLPRuEa2dCbiDfOOclikIUYNFA2j1VVjUSMCoVcQr9oRC1EoP3K1_UPnWAwcVoEn0cNvlcsRO-agD3R0W2c5jOfOSrr0MU8Rgcclse5KMWYApcmPscLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hQO4eABIreBZUPNL6UYqLykqw9_6zOprHab7n7B3mnSw1O_oxfX6R2F75PEV56KtlESxza2MHNcxV0n4LFzZATDJNXLJFKSiTNbyMfuGC44hgO9c1cMvSXa8ZL0KVv2BgltrIIWLzJZ4pTse9axSaBJSQiyK12V97S9biUjw-h6j3Rvel5VjtsuG9aPeps1PRX0VZDwQcUXJYJeQxoNTi8-c1BEMgcc7VurWrsYqu0RHKp_1lkpxNiEvGN5UF0e9IBBc5IVY4V6lsc0kkuJtPKnVrLlVOljXUevQn-x3k0t7sKhQKd0G78ohAFEhH2yyy0-ZxFuxXZ4ke0OKI4l8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=hQO4eABIreBZUPNL6UYqLykqw9_6zOprHab7n7B3mnSw1O_oxfX6R2F75PEV56KtlESxza2MHNcxV0n4LFzZATDJNXLJFKSiTNbyMfuGC44hgO9c1cMvSXa8ZL0KVv2BgltrIIWLzJZ4pTse9axSaBJSQiyK12V97S9biUjw-h6j3Rvel5VjtsuG9aPeps1PRX0VZDwQcUXJYJeQxoNTi8-c1BEMgcc7VurWrsYqu0RHKp_1lkpxNiEvGN5UF0e9IBBc5IVY4V6lsc0kkuJtPKnVrLlVOljXUevQn-x3k0t7sKhQKd0G78ohAFEhH2yyy0-ZxFuxXZ4ke0OKI4l8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiKiD0krFPcIHUqL_OlcI84w0zGC7hXkJtKr15k3iPI9b8D0SnJmnCl_Yg9WsHaXmzJOU0j-FagB24mKp4zW7Y2UhqLxtbDYmmCgpBS-RU2yGPw6m5eRKFYdI-jfsHVuaP6pHIzg__x44MnnasIi8u_MDoGvkfzu2AeGaA6yKvjCn--euIQm-ZzPvWl0A9AWc21ZPFbbY2iNrChym-Wp_DnfqbVcM7VvWwJFGG8WY5221KgJsVuCoWznevXIvVh2TvdwieJKFufUxzxlgq0CN8s19QV64vHXR_x4o7nREZ9TzzjuFZ03D5bKLYkWqd-03eISPOLrdcozkyhNatjUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTVYDX99X501HNSVkFHPrUpU_D2kthoqRlDsT3sQZxDKpjxj10lK17HsCVFfJPn7IIvA5AasB7azk8HFfRRFnQ9t4kJomv_qNivlFIU0DIbrUQQ0ScRh52T1qUr3BhF9lauAX3yPptpJlnHzXhcnDVqDUubBJ-MBA1eTfU0ncxUsra4PXa4J1rf0DcHCdFPx-SxK3SXa2hb7wL4Iq7CZkv89Dlln-HAUJ23Cly-uvf1NcIdJy6Mrf7FlGjI3VkNU72OczqbqxVcW0nWny9E7gGnszGuDiXsGNsc_BCcA4OcBWRlm1q8VcUStsLBoO5GVoyboSVfjNKk7Y3WUvhiIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T46FztdUoL0Odatjm-DOFmvpNH2OxFs_hJ7jEy2RnwhKru0FT7k_MVZ2lQD_dlHtdVENsU2sQ75Jri6K3SBSGEKHCS4k0OgMkA5AzBIZ2B7iBlK_bcL0DVAKp7R5PXLeCBPkxoD1uQ_fFCqPCYey0L9khuz6ZgRO1ksYSAZkj8lYoUO8Q4mSCW-xa8Vhf4WHOUkBemOKdPbYEhgCaSc2VAvZ4SxgM50huoNvtk-R9TD0QyT2E7StRJmqcZXD_-fc3c6qvHSxuNY2jgHrhRhgTvT17aw3_qQmrlM1VwpLiwVIlg45Q8ZCP0aS5m3C-Xjw7LKAeYMEx7S-hrTu5uJfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPHEbU21JNmElTL8Ynw2u3kYQ08iB5AMGgBAjkBFu7ojmrYNKsASukOJaBtet9UDjPlV0RSrKBJ8DhbbtvJv8wNU6wtpbnfW31MoRcD-dKL9QnSbt3O9MkJeerbQT_KGAU6DJNsjQcIq2lP2lsYqRKM_GAy-ADuKZ7AJOJGKt3TgNwmTkh1lkreNmeAD1QC21PVgKsThfS5R8QEx1iZhjv_IcRqnovTpaFdIGZngfos4LfcyvInK0V6h717O-bI0x1ldyULriUHNKg2fSIhsBJMDg6WLlVK7Ly5GnpEfEEhzqVmhE1myyke24dUOukR9hHbolMO2Cg7tdXETGAtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai1K-_9umdJ3UvdFfRv3V-j5bw9-PJxojCdqD5OSoi_028a3WBp5xqQOT5JlD4f_zI2jJGZl9MJIzUNDMNvSXCdqf2qROZDjdE2bEczhju-9xJmehvB5D03DjzVx8auqcejCp8ungUFsjmnPMO3td2JUAMGDNJ3VYwVPBY0BqTlhmZ-MfTjGzPx2liiNvr6fAzI0mooCgtvUvmyxmBigPyUj6T_0-wipqvMMbPgjZJz2cp3dt93d1cLwkldMMkrqxmIt9zJmjKchaw7NYhsrZ43lH86QXHabsLX1fE_XFIwZ4SgZpRjCm5eqJZFzpfiQw-Kwz22CqUqWkTdvokqpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRmue3ezV0H_lt0jaCePynL0DTsmbrgczETEKvy77wOhsqPKRlgf9eNl9U_qE0KhDUj01Gucf2dsU_5nyeiIooe44Zn9oBGcFrHXO8gBIniDRLBmdtjYjX4_Gmlu9Vrnl7U0SXN8VvF2C2NAThDwFF5PozPcZKFycxgOGbb5BmrA0CQnlTrPvFjZ3rWASvnm--hKUwTfz_qnLos4PDJcKVnEDzkKYiO_6p_TYaWdcoyK7mL7Myv57NcRHycp0XJjfD4KFTRXrxQbY0kQEz24GZbt6BwZr9y8cTQSwXiUosf5DHKbSklOQT-TG_3zfXRux6VjTPwMHn7ubeluXt3LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzDNzJx-UIe2_FImhX6tPuka555-1gE2Rw3deTpwkHZkKlPCgLzEmwxLHkYpZ5FfQ5iQ7HU3O3ZrhAsWgUMG9GebYYEsyJBCM5BUBVQUUR9rnuCcDdN8R5d9H1MuQG4TkCIcMeQxrHD8LbqdaGYbvbscvJYOeTgHyrjRN2BZ00B7P1-L44zXrI7z0Vg_DgVUQ2hsCqqS749-KQBXsegyshjtqd0-wV--s7vX6YkjGbJM9EsRkNB1FLTkZrO-q-ySCtsQeH9VdAvlgFCb-iQY1voC8tvJuGrK5yf2o0DdVOCEDba3dGBWYeTko8wjTCMZ00tEn4fCEs81Qa48uq89TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDPuCQ_UeybocN1QxUgdW8HfzpNNBMYpUZwPjqtbYSrGnF4ILiV0uN0p2cJFMewvUgvnHatkePke4a4zjjoT5NPJLd64aHNjKM4w0iXHYA425oTbwff3dqNT3xt3q9o-z2RYiXVCpLG-bCZC5HpIfez59UZrfOkL73nq0tcMxuqnRLrqWrqVDGpActMzydMHpZtYSPhL8EWLAD0CWwQU1E-ed5e-_RkW7EhIJ-7JtQqcmiTSxeo9RvxCEr29FU8SZ2jAe69kQaMM-ilk4KjRf9_ddJxQeDujjj3sG6wTzSkX5kYjFDw6vqebGaeb4OVgSBmE5D2wuIK9kIOYXKO1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgE7Y76iQfwJiLGgHdB6t0S88BkWNDuldvjItK3Pag_WaDP-ux9EIiVzZ36NBY8bMRqOXnOedRgYFU57QbruitUHmoP4ZoC7D57UMsnxNehZaXBp4RTcmhw-C_z7nJLX5uRM2tnUj6fRaDMxvPKMGGhMtxKJOtfbV1xmJhKsaPazwJ5ts597owGD1gS2FNvUH3_LjGzQD1PfSIedSOIxsV14_BPNl2eYHCUtbUw576-zCBU5QQxecI8KgRHeub9CXtfremot3J3M1gsMZ7t4KCit4wsmBrCbpfUcOfGH-5_2SNMs0EUkNZiH2aFc5mkgx2tEtI702XuX6dusCt17aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNgO4fx-HlLhoWbmEgefXLHQJdi-Jb1y-lfgf5pHtVgYykrnfZnW8ptpVmyn33sNYIg4kHt1yZ11dMOAMYbpFLS5xIMj4B34hboXz3IO7VSs13R3kTQAUFPoN9z3aFRJAnDvzewmmBne8NMTyk6io9uywFq9eI-KBwn0Gs-TRpD50TMgaOZH00qmokv8t7MbD8HdzRdaX-gbIlV0zhaDaIwpoSVD_IGHfKnTnGsmgH69YNHHM71c0LXZ9SZH1KybOk3X3yt4k_-3CYIIliUvVb_J5la3bk0UDUqMr0a_ixGe-DYmdgeUp_bYvV9vRKj-cWlE5b5zp-0YCecWzvX1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyTcZ4y0wyAHsvnfwxxhanBKQDrvZn40nwgGZwQhekQBKNw13CH-vmWyQoftWQQZr_17hInxJjjFZ1-BKBbq5knJAVsSYB2hcEJy_19le_hdOBC9tRyrEe0vyYx9jQQX4eXaPrLfT-RcXu63SeutwKSOqMMSZDfvhlBkZaRyn3N-FXgnkgeYTeTBYw1hRtrtVCSpI_QjWzZst9fukkrY5A81nwYnCWbfKo3bHMw7RyEFtwDy-GGrQRtbb2SzvWPG_DvZCAyX28w9goyqaT3AzJmRoNJuSK6TrTCiJzERJbVTbfk3EAC8piixUTAeZCZo3gDLHT55bLifEpQr5ecHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK9qaiY1HnCtExKq-2vdQQORyYol4iee9EiGJyQW0AWN_3HIuWdEh57t54koGaN-2daxtMCW-F9YZKBAzJ0p5Nt2cTrJZrmPiHa_zOq3IEj5rtKyt0LduZXNX47dcRKJyqCCeo8Px3cKlMrs2ijXMcn7zsqC6ESNXOjG4f7TnbyEY5fchm7tRfuTbBbM2Y7l52YWqky5a2OJRFbdlRKG2fgPTbN8aX8TQCErKcpkoeS_ASuABJUzmTJ4kyAy0hHfnGjPwLoJVbvUQ1v5oc2ueTrXSrfc1tTV1zDoortVtip8zKzxqrjDAYQ1vbbYciJe1SDVRqABaOylLycze3XoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=aF_Rp78oQa4skaWaoXIUuvy2zC7MkiGyseYlgd34pde7yClqz-TQRisZfgu-LWIntA70hcklI8yRCtqe-48ms_xYAlRDPQFZ4gx16FQ2Zk1q7QtHg8_r-nXdjCHnI9S4vSp92wgqic7CXSsRPmIQTPNQRp0h8st2FVxkNUgIFszp728xCO_tup_MVTgTaIEzLp0fGCXFiuVt0YfAVcvqeeG1KCyA5e8pky5bsoUbPAcHRjOIxicWGZ5B07_UUBmIbI5bUVtVRhyjTsBlkjzsrHn3EywK5A0xlZAhzEnB1ruzOX5McekFPGOfl0_hB1GsZX9QLUCU8PGsBMCiQRnA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=aF_Rp78oQa4skaWaoXIUuvy2zC7MkiGyseYlgd34pde7yClqz-TQRisZfgu-LWIntA70hcklI8yRCtqe-48ms_xYAlRDPQFZ4gx16FQ2Zk1q7QtHg8_r-nXdjCHnI9S4vSp92wgqic7CXSsRPmIQTPNQRp0h8st2FVxkNUgIFszp728xCO_tup_MVTgTaIEzLp0fGCXFiuVt0YfAVcvqeeG1KCyA5e8pky5bsoUbPAcHRjOIxicWGZ5B07_UUBmIbI5bUVtVRhyjTsBlkjzsrHn3EywK5A0xlZAhzEnB1ruzOX5McekFPGOfl0_hB1GsZX9QLUCU8PGsBMCiQRnA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=fvi2xvvLtrMKDLGkFKhdvRtTEbbn4t5picTH_VH-N4r8-mTCxQuR6kDDkjTL5SrZtCB7KBfjHVtxkGc8JjgFE4T31nsVz0IU-TU-Z6AAg9ADqweamYFrlOXkXCHNav3Ux8SVFg8iy3Ee4VNInyjyDw7wWSEfz0vx0FoQFfdVCkUnhORteUFfRtPKypQkiGtRbxW8R_LdzAG0jS99mqHtntqGtO4kiS6QhtvkXw6yJ6QrVeWUb3UjDZJ-f80d1twa-hb440zO5kUjWHix1vYMCqIZB6RA8bIAGEx_ZZNoOCvZkxQPu6-9jjkYUDJHLXRwFWvFhtnuRn1Htc_xripFww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=fvi2xvvLtrMKDLGkFKhdvRtTEbbn4t5picTH_VH-N4r8-mTCxQuR6kDDkjTL5SrZtCB7KBfjHVtxkGc8JjgFE4T31nsVz0IU-TU-Z6AAg9ADqweamYFrlOXkXCHNav3Ux8SVFg8iy3Ee4VNInyjyDw7wWSEfz0vx0FoQFfdVCkUnhORteUFfRtPKypQkiGtRbxW8R_LdzAG0jS99mqHtntqGtO4kiS6QhtvkXw6yJ6QrVeWUb3UjDZJ-f80d1twa-hb440zO5kUjWHix1vYMCqIZB6RA8bIAGEx_ZZNoOCvZkxQPu6-9jjkYUDJHLXRwFWvFhtnuRn1Htc_xripFww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYuphgST61A1EmhO1zNAFmB0BDU3ZEAabwcpIxw_yzKDDlWU5MWKtgb3QbHd-f7x9SPJ2Zes5G6IgIHG1J8bB3lzi8FHi6dml6aEZNGlSytTLTrSjbrhrPYVMsOQORzmVXsBLs9ovaLrS6x2p8iQtASqucH_m46wW3ubU2_4P24d-gppAOrcKrvIzgYgeCQXm34z0jW_1eiKwF24pI1JBdZEVqKKc-7ghvQ8C3DjlC9D0eNsa-0MtCifRn6WVQd75xO_I7LCPUFdlN2kVU_M3xSB6gl9bT7Q_tr53hWo6bumP4QzTM3hstAVvC0oRo6-ReT62cyupb2xhcXgXeTT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYvX8QVUbhmRKmOCp7clFsh9qoCuNjeMsUbGvv1c5Q-BOKrCb5wagT-Tl_dm3FfG2n5MO_Hf3UARrtAgvssPyonIaW8Agd_9joDqqEYSWUhivlv3EWHL1nrFyPYN6ZHh36ZxHntkIXO7TWaOpwQWID_PTiPM8ZjzUBhQqt1W66pUqzELZ1L4ZE5SekG21RKiEXX7D587qwdO_e5nuSLUlUjfkp4yjiny6kMwASjJ6q9lRecUJpw8ToBDitur1imBv5_tgyxAf6zniiFZrPU6q0VbIMU-5Xb0IrLTt7TTeAqO2gIHylmO1XlzGAbdafI9wZ-nQ_FrdbveJyOnsDlcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=YwdVQfenceLPGZMXM4BvBa7ERMptWUb-J3mWP0xFAzNR4UsmM9pxGXtCVIGxsaQ1QvadZpiEk21ouVu3MuldnjelhJlbguX-WzoOS7SVHgXwZYu-Fc31mL4U_Ryj_r23fgWfEmpKt3pfO9x-og9JwOp2SivoevIBeOSYgTtHxaD196_1MSZ9wmd0-EHrJRCdAArq_8PIrkD3fAc5iUao8POAOt4ZEIlbL7uWxYh_Q1ykikt4HCUsSl5MOEmY3wXnVEUYdZDfrYo8GbbG7LLiZcyAX7NOP7mfhA95oK6Hg_RIPeOwOBI6FotZtcfja96mDOvPw6ciNWBeIrpBdS1XIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=YwdVQfenceLPGZMXM4BvBa7ERMptWUb-J3mWP0xFAzNR4UsmM9pxGXtCVIGxsaQ1QvadZpiEk21ouVu3MuldnjelhJlbguX-WzoOS7SVHgXwZYu-Fc31mL4U_Ryj_r23fgWfEmpKt3pfO9x-og9JwOp2SivoevIBeOSYgTtHxaD196_1MSZ9wmd0-EHrJRCdAArq_8PIrkD3fAc5iUao8POAOt4ZEIlbL7uWxYh_Q1ykikt4HCUsSl5MOEmY3wXnVEUYdZDfrYo8GbbG7LLiZcyAX7NOP7mfhA95oK6Hg_RIPeOwOBI6FotZtcfja96mDOvPw6ciNWBeIrpBdS1XIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwe-ghtXPWZ8-BxpuTj4Y5O7XffyFcJH-ZY3Zlp9iID8AKYuvrlweK6RSVFWx35yNd2f9pl7zblQZmLvSNABVUy-h8GDd22qSDAqp6zNsdWDx5xpwTvt7ThvgocAIcDaJwmsZON6oVqkU50QBs49OLHtFnpdY2u3NxfkZDJ2ZPXSSZ6Bvq4eOEz3ug79sTw0ZtgyEg-5Iy6F5XIBcutHJ3A_wdY08f3e8GnVSqP82J_52FdRC0aJ3FEU6LAVWr-IbwG0IOcRUnVUm_cymr4ybamWUCZe_3QOicMx_PGowAC6LcXwCXx3ojto95NCx4c01qmjgRCLC81OLF_eDijDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDB6yzC04Y5us1PynNPco5uJ8y2J8_C07sQgrWlhghZEbdVD0KnHDdU3aUrkRjvfMbz3GWrAvtye7saOfbjF8IM4ZGPkV6y99Bk6XzljlFv2YSWc-AYCrdOiBRZ9TpqOzlnfDA_Hr07r3shGONEKdfaBmC_Z9Es37ESj4ChHmIS1mbOm0JiSDt_3LVwa1X0qpNWVErAO5moD2DQ6p_mAJc8XtepW-YX_pTYLYNEDBIaFVrIAR4d2nZV5ejZmoBzONCOzcXBJEdLM_KhZbCm936ty429Z7zm70a5wwZgY2UmGGBHcU9DhMasbokuzHkxUGAlralv42rI-vWcXpHLX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=QgnW8nHQM7gTvUlIfjbD76cA-tjFnsID3ZfsR76wsO2LUC90mwSs0jAUhh0rD7mDPuhxaietrxY59b_aVdXPHgRL0nBeCQ43aAinvVHMFuerw7eDnmNIgZ7ptHrh6qvTrBaw23BtJIPjx5cQ_UebDPO_sC5PCsZo28ajBhy4zI75qvokrQUvscT6d7Vhm_bUNNfwfWd5yQkVFWCa1G2IKn85XwQuq2_fjuMUpYX-slev2pochH2TUqiz6rgkM8zMWcwHJvY1zXMOkA0AelMqnjgecymgHKPX3k1Uk6AOabxfyWsJjN2QIlkNO6mMcAzpAhZ7F4o_rUNzUuVweX-2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=QgnW8nHQM7gTvUlIfjbD76cA-tjFnsID3ZfsR76wsO2LUC90mwSs0jAUhh0rD7mDPuhxaietrxY59b_aVdXPHgRL0nBeCQ43aAinvVHMFuerw7eDnmNIgZ7ptHrh6qvTrBaw23BtJIPjx5cQ_UebDPO_sC5PCsZo28ajBhy4zI75qvokrQUvscT6d7Vhm_bUNNfwfWd5yQkVFWCa1G2IKn85XwQuq2_fjuMUpYX-slev2pochH2TUqiz6rgkM8zMWcwHJvY1zXMOkA0AelMqnjgecymgHKPX3k1Uk6AOabxfyWsJjN2QIlkNO6mMcAzpAhZ7F4o_rUNzUuVweX-2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTAGgSpDcYqK_rmSfFy6zmKobNohf8t6wSIkp2QDwuOreyHrw2nfPn--tR1l1bXy-q4ORD2_RpGAjTjJ7ylHKcgp1m5l6BEXKNjkW4laINVeSPtdSUFrk1ljW1cO2yx-ovg5MXooNgCZwBYxmxuX3AVdIcAW7lxU5-3Ih4ZmR8B49bVkKY8GlAOGsmOm0AzSn37fSbUd3T354woItINTNqnDPo-66DHj3AQdkyTDNmU2zDvDiM0u1LhuJ1cgILyv_Ji8_vuC2sXwE2p0xXC4Tb8YIRUsY9cEQjCPV6ENTwYszd_uwBOKgT7QDpc0EfRTfsq_VpTIzFnMH5D2wXLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=q_nc4LG_ebYYcbX75o4dJx27dw9gGF7YRKa8HMbAzAHaL5amXezcMZtRbfsuSYdw9No7OBmv-devK9peyaHNVhnwH0_OSui30hF34lMteRVpvPpuY-hD27NbTMLyEFNV9G0ZLwrQQ-bhu5ElOhPyGV196Q9FN0L-7SdI7JJYa1quDGiaXKyKYT7OyPp5aXAj_kHtI0uGc-ukAR-SMB6XdXtYXrkwFxZtf_z-zKC9GJy9gRdZTQLYAo1vsdAxWOd5P7ZNlCiDSdCKwtJGVdkmw857ozAzUkTRA3nDs6C8hQBWAndTSXSePclxmhGqjKu1X1J8DwpV91g1lwDZn9tOog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=q_nc4LG_ebYYcbX75o4dJx27dw9gGF7YRKa8HMbAzAHaL5amXezcMZtRbfsuSYdw9No7OBmv-devK9peyaHNVhnwH0_OSui30hF34lMteRVpvPpuY-hD27NbTMLyEFNV9G0ZLwrQQ-bhu5ElOhPyGV196Q9FN0L-7SdI7JJYa1quDGiaXKyKYT7OyPp5aXAj_kHtI0uGc-ukAR-SMB6XdXtYXrkwFxZtf_z-zKC9GJy9gRdZTQLYAo1vsdAxWOd5P7ZNlCiDSdCKwtJGVdkmw857ozAzUkTRA3nDs6C8hQBWAndTSXSePclxmhGqjKu1X1J8DwpV91g1lwDZn9tOog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXiaIk4GBuYLoZiHDKbQXe9iuT6JCBsy-vaChP3s7XQNJlYFqZCcX1HmcxlluhuUDe7X2mPNqOVKXo1icGIH3qzdjnCSWqr-OM3IS_cMHsoiN47i1ZGPWIwVAbkPN2T3h3dblbgQ1D6MqG8Nwbf6yFA-zd3xj9P9imIqszB7wrqONlosQlzxdbCiqEX9p0Uu6l0AYsWrC5hbsRWagLiGlD_RcQR0dxc-IYMvz9xwxUlUZzQ6USpqbFb0jTkT1p59FiUN1UPgTB6QCJTABiNhPSzkHxWHNIqQUxNbMrZn_ImyYbJ2YMOARdsY2LiT6ySxXOZuwwsXfjhCL5ZIShMUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8ar3LxZIYaKYvO06X0C3WDcY_Lb3rHjh6ehwvppvYwN3Hia6-78kSckVj89NNRQYlcmHqKATKYFuaPrv3jYqUokoRHL6YqgfEBX9VH2A3-xNVwDWa6F7U7IUwjNMTWMuMTiGpo5K_7Lt6wfnBR6hCeLeKp0I0eFgEdf7nLlPKW14sW-z_XQ6FM9NBiwxlb3VDEOgqQdIvyb2hYMQC7r3YD6M_NVSwLeTeVZUSpqHoo-qXbJOnRpcUz1Uf3heyg9Eoj6H2hkpXhj53va7zYXxt0_sLkk0wHJ_OLAIkQVYM-tojfApYWdq2D_wcmp3XkB-UJxGFfGd61SXV4TfiXIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOo53JbbzHSZZDVM44dIeCk_UIz2cMfhHO7JonDcZbakRreQExNURrnWp-rvw0fkkxHdRpo-fJCOKUVdUjqol1VyVf6TbQ0Cs7C0qwz1K9OiUnrJjaQCBxaZuNbcyq80hVULfxshpQBTOmZWIBr9YcbhzHL2DU8xAz_2uVebZpfYB2T2zQNaU3YJCeyPdvemscmCNlIypKn4jUu4c4cW2PYSZMmMai4LqZk2M_gXXMeEqEoUMx-A3yrQA6em1-yIg9677caaKhm_JcddMhnMVawNHM-r31RzNGz3O5ZxrE3EBwckpkYy7BtI-V0QSv5WamvXho9cYnnZGJVAFhezAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2-oqy-ub5UL8NAL4odnN12Ei0dkG-C0Q8M90zRrpMiLxELtuIxz8mLm-SydNBxSk8oWvXf3bGnk-505rj6G53WyRNCaWE4EUhSgxFkwC_ExHCMuixi-LppWqXBDeYZbLEZV1YUTtb-Vk8aW-co-LZ51ZFwewqEQp2y2LIaqs7hhjYB5cig7HYjrPm8I3FRV2iVie9kzdl4mfcT0e27VCSCq_B29uHZmifrjzxxtD8NhJGjM2lFuHKD-W5wMp6-S4rCmT4-ma7gRGfPlSJGacWf54s4fpL3sKP2LDVaKHouYNNUhcq5YkMMV4t06-VTqwgUefjE_Cq9PmQ5Fbkzl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWENUYl3LWYO0wxDjCtm-7wRzlSAxNhyj-e4FlSDrKxcvRYc7QoYhETELB2_4zYWXJV_uk6ZbpilDIvooJ3Vnk-8-LA49DZA63FvGM8Tipx1QUZLPxTib-2nR6XzoOgupIsc31VMsHPpIuAPuxl-_9hrnmJ9o1CgiINhaRGWUqmP-iPxUnw4m24zglu5COFv3UM1DQQ2XYelD9lPvsUFDAUqmumjQJEkowH0tlWnVHIq3rv8TyzBazFVLJW1WIjsI0sLtYOynSziWC2n6YF41Wru5QdC7sHtR2eethpmJoAM4MF_zCl5H3jQCiNbU9UhP0anX9idu3pDJzNOiW7RzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ5GlvL23QUSGPep2pT6lsszRRZu9m2hE-mJx6QAnJZxOQ5aUdzih-wYPPDbe9njKYNdsal0VDIq-DEGDECot5s9h2fDr6u1NR3XRiwSLXSru76PqoviW4lfICRKTy-pmZ9gj6MNIs7Mc18Mkh07xCYom4OWCke3DpmZK9kcAromvAQbDaOv9x1bA_2n_zESlNEu-4kC1jwbkOeLAh_8YUjlr77wtgCv1M4JWCjrVwPjU7KZTH6ckzs1aI5g40XY0pe2k8eGJ-NNxDY1-8xnN89hVAFxmcDpjRR3S7ABCB3EiPwltiaAQCJWdfJcC0pcH36eR8MTdkvppajLhJ9-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW4Z9DwCfBxrmKgoSHTCxlAQVQEUsAcgCPnpdZVUlB16RArSRDLnBbMiuXx7VUqNTiEctuQD8RKkhpfrXjm4C5QwvjGUh3vtpJhNNUMHmVlja5ogHNPE0hBYgU7l6GGt5obBGJjiD_fVOprpYnAZ5PsURrCQ_0Pcnih3y3139uiB-k8EDdoBoz6GnzVkR34mhAzMD8L_ArzY3F-dbiiiVg1U4_EXkEGHnV7YR6pw3Ye6BDfkItmCChJuh7lz7M_CEXvCxoDefReyvFq4l7QB0a7jcVTEeVYy97e2tmHuz7u-8lTfzQk0nRiRl9zTNI62g_qeCbdon7mEELxnd6oTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=vZef_I3kMAE6tkPHONzOeINQZFUH-ha_Bnu7nrX5v915j3TrpoiG16KTMMwbZWnN8v_4AQxI-fxRJlVCIMTjFq-AlEFTs1_qjM_guj_Vr7iVUpL6pCJ0fZk0A4hFz0v7-nUPALBSJBIrXhnKviWtv6es7IvtNebDtcKmDNfber5W7cXlIy17UYoiTqJho44SOfYi-ue0RXnk-LkKeXmq0oWu8LG4awqAIaGnCl6AkYMmU06GNi3FEOB2qBe2EZNWcitdR5YH4bksU26LJR39uK1ThMN659YN1FICSczyoWbGsNrqs184tmdGYkYpuwp3h23LhzVDmJ_1DRHkSvwJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=vZef_I3kMAE6tkPHONzOeINQZFUH-ha_Bnu7nrX5v915j3TrpoiG16KTMMwbZWnN8v_4AQxI-fxRJlVCIMTjFq-AlEFTs1_qjM_guj_Vr7iVUpL6pCJ0fZk0A4hFz0v7-nUPALBSJBIrXhnKviWtv6es7IvtNebDtcKmDNfber5W7cXlIy17UYoiTqJho44SOfYi-ue0RXnk-LkKeXmq0oWu8LG4awqAIaGnCl6AkYMmU06GNi3FEOB2qBe2EZNWcitdR5YH4bksU26LJR39uK1ThMN659YN1FICSczyoWbGsNrqs184tmdGYkYpuwp3h23LhzVDmJ_1DRHkSvwJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/occzobjhd4l4AHVALMq-fyik2_omrh2dx5zGE9hN6TwR4Q7UOz4RLqAlrY9PurDCx_9NBtZ3HUNZfD4RYXpwBWrhX0p-L4xEWBR-x0eln345FW2vMDdSiEhdU2x3qvS774NvaX2Z5YiFo48DqM0uf_EeN-9BFQuAzIp0yqfWwqVcjYvyMLZ8A8KMy-eGTGP0Ql_fPhCOapfdFwfuBAJn4-syxOlP0YxKQoDdM1PmPXEnA2sgwgJogbJZHkfewACM92_7kt-zpFB4QaEFfnWS2WCMSr77olGvK06Ow-uPmQzUkOQLi9V9UU2mh04r8LDPNFvkuEi0I0Xq9a7HPYUSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfEYMfHO8X-Q0AKPQCTxGVLknNHE_8wNwmjlF-4R4OiX1xSGVIp79kMq1vzTgexXJaF4HImkoAVjN3wMgKhVg74uqFUIT03otW0snJ5fV-WVxgenbCt2F6YfCkqQE8lLENXKHvbWzp4tD2Q25wwK_IIx-kpVXaStZbbSfijFQRGSwhwCvYQQqTwJzdZkhqclUiEqEPMvg2TACcQdZaalL75FgTBMWBkT_FPJPUNc2qUfx67XNSf9CT4rRfIsNCsw12Gh9mxmhqyD7mq1h6ANPNpBzEkmwKqy9NCn-Z7wZ5yFpNsnhoQAS7nVlvas4aCBimsHlhPJSu9gsSYw0272-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgcRZIpIq3ll0U9vZ_B_LmlYzJntMCmkdZXJ3NnSZ9HYmWL9OBf57MO4THBoGzwLL24wY3G8_MqvguCplPto_4IsmaEzS2i8EjRvMD3LKWWOY2JNRIxKhHQKcxVNBG2mNoF6osG1P2yAuSOegRbdyU9GAJFev06zcaAGDxaE9w66EEG6H00CW2ctbecyQyVLlbv_nfVZF5H5CaQWslhjwbDKdpmPGVbiR1_IeUie61pkbSbM5s7VO6LFDMv_l27h5uguCfTxEJNdfTfidSJStpQFMANqQCpHuVdMqhyXS5dIrV7a7DQve9cCMt-F1DAXTvwo34hEslGN8Wkx4hsxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMO8cEffe2bLQHKrVOVpnp_TiFVdDU4tKo01gdZtMPzdRWQq9bscqDNk5PaGy1I1oYLmq3nu4gJ7_NcA4600GMsJLbQrtposwaFEymwC_BB7-_DC9RZD9WQRg-JDfHIHGPWP6oTYPPQG5Ch7WGImPy9CLwDZpGlKrcAGumFd6u43A10DkvysHxKiUduPz521sy6x5K584HNXDu9QIwZl7oPHXlXlgOfRMQ9iZPNAFMVI-xnW_dUvdPtEufaZHX4-XAP_ac8e9BijSIP7O5QcqHfRFnUd31ALyRT7M1I_P-0gfizHT0g8mHjJola_UmsfZcoNcFkia9wyeWtg3jlbLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XLbJxbzrtGcfD5DIMwV-So8WVFNG2tesrwpUSbRba9m619Udbio4jfw6xCbGlNkhrqbzqZi-C3ytAa6fSfqL3NYIhueRuuTrS5YbDfM7C89srm2xgyrD4BeI-ru3N1koCqYFpMa3BBWz4XLa0TiaoshaPkgGZkPG6Jwzm-b9VCWJ4VI8U5q2Dpi2Ad-zyZPs0EsQ_acmFV6zha00UXzcWFSS8T50AhkUt6WGifzVWyp9vOmfk7_o1pamfu9ZEn0hfNjXjOGVdx-jVNbX6oqSJlRRUVJew1ZPSZfdg8zqIGdBCuvbFOHRdFuY_Hu_fcZo78AtfxwLhea518ozXzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehdv0VP50OeIvInRH9dpXku-Nmt3C-1wBBBJOuJSdZtS_Fd5DKWOGxkSp0Az-VSG8iCfKHTH44HNTusO3p2hq0iAAw5MivlzQjjaQg3LzQufrZZJm2Upk8AcTiojLvfgP_RMF-Q33FuXMpeninqrWTIOL-WNv9pq5XkZ9CwQ72Q4ubZoG2S8-t0Zj-RvfeHhnamWPnm6KGQeYD3B8zlKiReCVS4oniJclhsoll_r0q1Lyx9qIUUwWIOpPJ2iVaROSbr0XKY5eFK-euF2C3PHb7WYL49KouCuZ0iUcgD24R0V2449fjpHiVes_0Y6r1gMljo6UWYyGlZSz9F61s1gog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuS5XgKNaZlvSm-SWtKz5jeZbjkvT6oh32yKYjuzJZV_qn2v87W1S3LTZqlrGf9fUQwHMhYMmH9Wjc7wpRk-em8_t6bIdCDz8AU-R710WPYoExLTcofmhFuT_1F81cqYh92T_dZTsJL0EGMcxeX_8uU0cm8C9jfqe0hdBg3uInXx9kylaHLszKh-TPlLSZd28azD2gSEMQNKFG7vMqEaqDTumG2GktPlwjDn5cbPdv-dxpmDoZfJ9DosBFR8sI7VDhkgtf2EnggKjLSHfQ-GMWRCP_KfRuIFa0Xy7XCm085nO2prGH5JoQ1Zowp36vA9Cs4ELdlqJM-DIJf2Zl28gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-pZtjRC7YCKAq5W-S4FO6aKwn9DqcJJUnDdYMUeO9u5oHok7C5GWM6cKMNlgK0uXrbGy7tdyBHWbXumeVrprCiKe5R3cxjlc1bSwiLtEzzvyiJtZbn7fRMhQKPqci_u-jX8PBshEvaGdLWfhfhqRNI8_r28UzjNU6fMy5AMAh6Q4Llsnl1lSC-bnbfmUVzEevyx7qsXpT2R4RSuRw_wws65YZVXRPKteMmS19JB-QywTShRIdMqKOzhOiyvxY1ETZCo0kPBtGZVEdLqXaAznHxdR_lPZJOBKKZ3lPxjl4bEyOSXijxGsucfH-Fxpq3PaiP4mwzbTzObnry36Zaz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvYqB7CILZ9RTPW7nN8xxAMZnrSa7ev05EKwQVlK2znyG3V1bugCtOpHCkkN579HnltGk2Y62ACdkxqmywuWPUBuPST3VVlB-nHApc9W1iVPCsILbbJ5dlfjNTGgEYNLz-o0zP0z8qzkTAOA_g33gYIJ0mDyAP8jhupGs6sQqglINlRz6b7DySjvHAulWwLLj0Msg1ynEGEnu5bDcBoxaHn0h_KWqOfu0RhpqSRJ007-LTVJR7iaDF22vqBk3JEPG9I2iyHSUfNO268--UVViYxYCj4RSwTROhLw9pwfS7QDb7pAFzr30m0dbKe-hwHzTb_Qo0tA3AdoftUaWDSkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP1XRJxsiHwdNf9QW15-lnacm9M8vldb_LWfQStbB4LbkKFdPlTbc4f2-OreTdzuLuWnE_yqmfoXvTzYKp5GcbnYvyMkQD1oioBZgqQuR9sPaBT1sCrRTvzW4C2mS8lwvfrQVgIp4w40UqJZGImhv_XUV_6LEWHK9WapfsIGcqCldcqJ87YwyJZZ0z7fkajwbLj-Cdkehf3WUF4aKyCZSP5Pd1sMAoS4A_WXcud22TRbVp53iH5JM5sDg2le2szM1CfnVXOnSggWsw_OIDQmVTJl3E8saPKzQDSeio_-X7BxC1WXj79b-1iHBM7nq7P3A0Mmf34RVLpD5AQi-kYeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWVGnx3tA5pZDR3oAJBefdrK7qNRVRDnVp3nC5r--qLly1olZB60dzjlprl8k1cFttdcdnp5eOCgYyg1Qx7Rd4q0Ew6tGLy2pfe5H-J7SVAZzNkozRQAk2t85xPpFp5p2mmLTfYQ8J6gIrRrWhW71_kUpJahrQr4F8ZT5ZLpIkemIGElBwoy31R-qoKAP0b7UGhlKPKz9mmyIus8RYAywoSmqx4XCmNxBxQaOd9ZN5OKDrGvDjEWXVdYn57p8PsySW8DRvFyEWwPRty6Ll6zE6aGsFZm2N8z8BqZxY37aO-cn9km3yJEZ3aa1GKG4Ij6uxThqrYuqMOZ3HV8_H-Snokg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWVGnx3tA5pZDR3oAJBefdrK7qNRVRDnVp3nC5r--qLly1olZB60dzjlprl8k1cFttdcdnp5eOCgYyg1Qx7Rd4q0Ew6tGLy2pfe5H-J7SVAZzNkozRQAk2t85xPpFp5p2mmLTfYQ8J6gIrRrWhW71_kUpJahrQr4F8ZT5ZLpIkemIGElBwoy31R-qoKAP0b7UGhlKPKz9mmyIus8RYAywoSmqx4XCmNxBxQaOd9ZN5OKDrGvDjEWXVdYn57p8PsySW8DRvFyEWwPRty6Ll6zE6aGsFZm2N8z8BqZxY37aO-cn9km3yJEZ3aa1GKG4Ij6uxThqrYuqMOZ3HV8_H-Snokg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLC3SzIzObeVi-qAOdkB5rBWQDfBREnh9jTrerQsFfsl0URnxS9bCbhFBontY98wbgrsrtMU1hD-zk-YTPGSGZ4qb__nSo_nzyvTn1-xK_46a4iEQusG-RucXo0aw3xFpRebfRITowvZ6D0dXphnnEdd0pq1b5SPPOwEw8ZDPVptpbB0B5mwjPM09DSo6SjbamdMzAhjR8NMk6S8UDDGuh00qwwUCo9AmeFHWo6mm9cWmO08T7NV7suiHYA8vw8EhONfcaRh2nTw33LpSLzKF6uCpl1V7A5ZRWyQ3Hp7NM3k0rYdTNr_hU0zAhPWBjq9uMjVC4AGUqPAe7TI6ynrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4fHSgtTAPwqcjtRZxeNYbgAf_WGRItYtX-dUbUTOITXnYUr1y72CUkKSxy7J-N3sAcsxA9zRlQwxWDGLs7gCP8xD-UxEvzKNoqMqkcXpIq43H8uVx7Vpc0J8zzHHXRzcZA2JB0XfgaG1Svni-Z3xB8jhSQIyeGPlVAmxkL5QEUhf27GXr06xXAMBZt5S093XP2xnBRbtnVmKrFzQsL43LsoeaFDZJ4bAG5omLLkX533MDXjwGx8YvkILdKIwbD9r0pLO8nKJvoW5zXSuQcaKe7XiAbJt9RaJ-5_dzuTgyv4STi0tVupAaHNRvO70yPSkGFp9YJimKYbdf693TRBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8oCj9MsCPwDt_EA7q2E9RxoRX1772Jug-ncGYzJAr9sEzuWFx4-oKDkfP-zJqcGzbP1Vv4hHMtpviGjAaNLjmz1ABh0UeeXp-vPfGWt7_P_i1BVGYAFYus1FuTa3-LjdAynZcefq-IIX77mQ0ZvUSY8K9HSzva0S7dq2tFe7lHzl0s-ClhNbdYCYwDm5QMf9rkgdLszJ6DXXxs6ZbnM8vzN_Ez9EGRi-1l1pR60d1eb0eeZ5o_4phTJN7xUhpow5Dwn5UTEzdgQdPDJFK_lz4Dnvbt0P_u3BHQbNUB1YepXH16zDjY5OWExaRDYrEE5hsczz_ak3NQI1cZ8z0a2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfU0ao6ScSzJDDRpKlC7aDjeclE_STEJJ7x7-AYvITQNEZgjodV3oT0bqLcXPzwQolSumyA551GrHy9jED8r5iqc_shPbID3E9_8nWjGVVNlDvvtLvyuPQDHO2vLmXxhimuk79nDuojzCunXuJquZLBOSwhS80izmF9DTBazfSyzrCu5_Yg5c6MQopf8jw-mhGHfNyfyC3LLOAd24J5hMiqDuCXsLK-1jfU_6ip9YBbg9bwgWXq__lpDG1IXCFI7uWs-GZ3ohBVN4Hxiy3hn__Pf3ffO15u9T6Zo6NWD9DnZ8ZrTgdPZh4m_iIPr4eQoVoZ8KqksfwjIGiZ_vU_YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4r3ly5Z4ZGL3sBiFMaN1OI8Te6Ume4YrLUdlzI-NFsOPTHVT8-GcSDxqaCo-Rz3gwC9aQnP65GBARQm_Pa-NdakNbD9wuXyGmXEfu6zhbWOaX2lsE7VHGs_mzeDm-lpDYE6Ip2E-SvCOMnTs9a-2UHPaytGXelnou_ERVUQPahU2e4CrL2jDeY29-dABX-J4WZHKdP7KfGaD-wPUe8x-AxVdSsMAbCJy0WG61UoPYILSGEe78XhCiIoqxQQuGcvd2P0hZ5UHy_duMy6NDJof0fZljc0LECQ6aNSo27DPImFebbTT4FjjG_0E4ZZ_5P4pqQc77tLLhnx0r7IyKhRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX5gJlmaCo5uyXjGFkd0bTmp5rds1Pfx_mO_vLkezwwaQvBm3YeBX7qitW34kADkkM9w_za4YVE2QOknlCFe3z-DJMuJkF3vCDWVNSrBwWWUznJYKoKu4JyF1n_jo_H76-dawtMLWOeFer8uz3gasbwNeE0eIYBPIl0rrMJQV1kEDJeNsVN0TVVQC-nKnTpF2aGNbiOOtHTuK6nXTWHtDOOt2ra4O6LHUFPIsPTfSinEaDVSp21iel5xsDRQCcNJ5l8EyadzNn-MtHIrh0EzPpSVXDtYDLk7lF97dX1IvFqD9xWi-TVXhushNvT0tO5YonlcFxHrGel2tlGzfPTTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJW8aSPktXlVgmn4juiJ4MyKn3Bv26EPuSRVss_34JaLwgnldjEIYaOX1z5j7kS-Eb-Tr7vWZHUCA3uaqZfPBbebeUQOW_HgqW6JGPxTHN1wG2sxL4uI38IBOvezI5nC5u0aRdhdFkdy61flnBGfO55YkLvhVBqGcczZqOiDQvnB13o4YSobblVcyY4RJWX-uuHBK8322xuFUmcudRRxQKNZh6TrZ0UdetbgX8Gxl1U_fgHqzfUhdIQVXuv1Iy7NejYgRGEhzFILJdrkhjA1HsLHdC-6hz_Wr-O36U3AlOU-n3Np485_DeJ1RAPV56OABTg1C24xKsuBeW75MYpt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkgCx69PRoH6PCGU782IbGBElDDdIMxZiLcy_Z9WuMiEBLjz-GDXd2EIvy4ulXKd9jKfeYqA5EtM3RCFVt55ZZ2cgKFm6fHTHwYXF72iUcO_ojVYDz0oNyHn3jnEn6GI4S610eWFPJdcoAVMOtR_kwfyBNDGr3XnS4ZqjK_u5w918JnZv0t-NGF-tdNRnMOkrop6jsHaFWuYcbJT6T6N5m0uQQkiPNMHDmzWbo2uQii2AS4zAaztVduUxjXAFQpMn6slkgfttTSenBklvUdbPjWZ8YZvOYbJWz7sTenCcpvAO1R4v1bsxIJrJ0Zpcd_5KiuKEOZ77gSK3LNu0ZdoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAf8wCy2Kmgp3PNIedhXvb6oAxY1MXxjMc08QaD8HfxWd8TNj3UU_hBbayvPWuC1-JSfvIZN9oXNrrpzXbtDP6ZSGUJrKwPtCTZhybQ8w2ovbTCBHm4LIU55Elto9onnyjZgAJT6q38YJLy9SFT40X-lZzSZjlgygsSPo9imfFdjAv_T01LnIsuA6D-MR5HMY9LwMBW_VwhA4qeOv-Kuj6cYoE8-UfRU_0YQpxaJCM4M14ti5XeSH9luGjF0qlJxuttjFl-VNfce6dvXoffUq0Pd7RUX4ZM-Zn5ObqHXmgg9IVpx-y5VCyL6ye2GGBNYEKN99i8MCymiu1Ixzf0H9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c07w7eF2sGX5smZp7HGSBRBFiKZHjLqnDJnQZDpKVMSHCXyGmwL0HnoTRYlzyaDRurkwAd2UleHYZ76QrWb6sdZNJ_EPiDTyH5eCR9lHYnkptxpTBMzOmqDHl0mYzLtDYsWOYL3ybL5j2qdXlOSbjNsddEMm87BFqAg8gPfvJ1ai5j5-uDkkJSN7MYRKXYCKU0GFyIVjjN-cvrn8uc4-A6xjXOwxEk18F8lEQeqLtmHta19pXjRtqRn10RMi67kVvG9L6D5UdTEc4G-7w8chj6jHDoWLzlhtoZa0dG4tyI5mGEX5EwX2xgKQ6m8kA7e4QTpp159SFK-cHQfvxG2CgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkDN4mAHJeDzgyRvGaAB90TRPeST0sCHPczjzGFM0qRXnzRYZQNigMfJm3mQJKGXnqu5bhrCQC0QUXPUCqJDJhFkts6Ggsnwgl-B79Nsf0Dmp22z64XAH5y_os70uD5Utp111788xVJBIiT9bICuodnJJuHSbOwwgU3giyY3tlJoA8cegDU3g71v6R48LkhnUbaw-YN0U36cx55YzDeLm2r8cZh7CG3TW-ON20MFOLyHv_xruXf49vik3gzkc3lhlubNNRsa30ZIg6hGyUBjV7Kf85sHNuEbsBZ5XwXaIIBQsofBS5XVo3hGxwnR5C9FaHzyCV-GCXQec9qzjzrYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=VgxH46YaI-T1EYHlCTzKcaKg2ppUXgQsAJ476GCgrtETLNIw9pTlVwkFeedihQAPB1QopaSILjYdlED3y801BnMWoo1o4VwcBo6AXlB6V-W6dQ20eJDepKGXOBR5iCNBEUrCyG-2-oG0NrICOICcKLmC5oKY5bhl3ibpimfY4FELisB07sbaiwA5vMljyLOTR1RYBfeI2l5ONNjHBRHHjiKveMcK89E4uox4nyNLK6hcOt4FWMiFTI5viu-zVfaitxM33lTAdU2DD1xso5sEOwRLywZmHv4jFtAZq-dCi9Fh5ztg11aL5f89ZgkhtDWPOzU0eEK7xsxKaBujefAwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=VgxH46YaI-T1EYHlCTzKcaKg2ppUXgQsAJ476GCgrtETLNIw9pTlVwkFeedihQAPB1QopaSILjYdlED3y801BnMWoo1o4VwcBo6AXlB6V-W6dQ20eJDepKGXOBR5iCNBEUrCyG-2-oG0NrICOICcKLmC5oKY5bhl3ibpimfY4FELisB07sbaiwA5vMljyLOTR1RYBfeI2l5ONNjHBRHHjiKveMcK89E4uox4nyNLK6hcOt4FWMiFTI5viu-zVfaitxM33lTAdU2DD1xso5sEOwRLywZmHv4jFtAZq-dCi9Fh5ztg11aL5f89ZgkhtDWPOzU0eEK7xsxKaBujefAwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZgbjfZvKXc6oo2PQexzZGsT6MarpbQDNhcMOZaR6vftL9wXdBEgukk1dBTFR1LCum43B1LEOrHnIUD4YfEPjG5_cFz6nsXxaLTX5F7wkgEUcpKAmQrwCXGqWxlVxyM9IxHA3F5arzBXTy-Hqnu1cLDP71bo8x9SSZcnyyZC-doBOnyXFZeKJh4HctHLB3u7XFkVG0-cK5PgrMfV5TwzRd_m2Sgo5bCU7uc5vV-_NYMuaesssfz0V-_hUFpBCH5yqa04kGkHO26AZ0oKlcCc0kRXzvfho9EWCPs_UM7YxdbdysYS487xZaFT0mYVJbhxGpgtzt2fOfDYMXa772aOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qmmr9zjRZBcswOA8FzlmnsRaPTlgnLBayir8kTvDSOd3g809kvGIbEfX0eGeDfYtUbn_Z-wSNN72djeQXYHUCulXXkQMyPonO9s9rFo9lDq2iCxKJqh4YujGj-ScUog4K_BYveJA5x9v9QFFuszVGt_dpDEPOQNmPaaLPAjWL6kztkePZx5nF7JjxZW3QYqVDYkH4rWJAAbErQBLguGWKI4scRWgIuhpy7FM0_Fv1nNPGXpZ6qvK18s9oxTr8vW7CClQ0JPW5yuCXL2DGqQrRevaYHI6xrZRkcW1_jW7dmHxKH7NVOQP29-zsCx48k0i92ex15RfqivChYM-q2ulMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O02ut7c2ZZrHTtmGPhG67Rem1s_0avwAejhwl22Q5erRmn6_HB0LbY5wl4CrkRwn6n4QlzIhOV3B-fCTZNHvIcJjaFztbUZ5-f62wUMBoOYceOruNkPEmHUZekHRkmhMnA4moFDwzp7GKaThMT26vvERy1rJE2LHtkOenHZwRBlevIAvSOSBaIoqlL7DaVUlGEatwxCzjL6va2udItnMDmbi8i5KpLYdJb1xcxcs58uI8OGPOPEi56G3CHYs7s_CLhQEwDSLzs04LmUiECrHn3YVDNqvfZBNPNNg2qQprLhmcdwmVCjmvQFV3EOJit19sZ9ocAD06Lp_QALCnKdgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=Gz_VVfAbIXF3msY2Bub5BQVCAO5TKI38uXxifzkVygXI4_iW-SgYaaZWdclTLuVQuMr4DyAuvasv_IPS7M79a0YpjxXFDNmFFjcZhqewB-Yxl3o5g60OToIs8yXwXu29p4AsU9JjkmHCeSikCJwaflfXUKbyj2jWGG_SX3Ry1kb33DH9CpI4C8bJAvJRQE3tfS_uucDbrTVvYEYq6PEX1u6sf8Ihil_WEoaTB5H9VRXIVdRhV7Fig4eQ_NugZASwMdBZFccSgWL6ul-oLB62au0XX-0qiDpRRWpVzNmSpsOsxQbnOK7SzVxkptLLdCXJ36ySqXdpxH_YoxLdDp-rOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=Gz_VVfAbIXF3msY2Bub5BQVCAO5TKI38uXxifzkVygXI4_iW-SgYaaZWdclTLuVQuMr4DyAuvasv_IPS7M79a0YpjxXFDNmFFjcZhqewB-Yxl3o5g60OToIs8yXwXu29p4AsU9JjkmHCeSikCJwaflfXUKbyj2jWGG_SX3Ry1kb33DH9CpI4C8bJAvJRQE3tfS_uucDbrTVvYEYq6PEX1u6sf8Ihil_WEoaTB5H9VRXIVdRhV7Fig4eQ_NugZASwMdBZFccSgWL6ul-oLB62au0XX-0qiDpRRWpVzNmSpsOsxQbnOK7SzVxkptLLdCXJ36ySqXdpxH_YoxLdDp-rOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea6iVVh5Tr7RS29wy01lLwf56sBvkBGE4SUT71b1OIQLB84v5GcKx1zczTbKRZD0bbbkjVTwIcg8_ZIFTdHCQ13kMcHcREDCKeZPNtxNg_SBEryie3rFNkgZWcPZz-_vx1DQaIF4XGfOnFbZhijYB7vYw03yQM9iyCqOcixAw0ItKBUSk5wldnPsXkjcntB-n6ngYda_vkeIRrsAMYfRJuchuHd720WkY8l-5GUGSuTB-hKBKN0qF_1Zffw3hxiEoqpPyqzSf9aFlXEYW20s3q9bsc4_WYb2CfLr7E2DXaNT9a3DfQWe4EE4ry6P4_sZRFv3FwTPNTv9qhoSrUuvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPGCxCmi5TquHgXepTKP4j5SgmxXmwU20TZxyvIPsNJgcTro8PXuNL3GSSHO5lyxCW3hj8SIK11zqiynVWalpEi077ReQNHphI8cGAKiVyqXM_Ebm-F2AlYNpBLoSL1xqXFrCmhdVBe62djges45y1R8d-_wUp7OADjXZBZt6EDFF3TPEeYbJbCqDWC36KT_EcWstjE2tZ8GIa5pP1Lmtq0ewEZ_jepaOljvM-xULx5B60tOOzk31NhoS8rrmaHi10e2cQjQW5i077dAA202u3Tnnkcvk2qbf0L0mYYDxg6hEXBga51Ah1JNtILABI47iowk4Tq2Atq3wwrL5GR3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExVBywY4U8-ITWJ90ap5Olzg3a6jx2evMHgMGaTl-I0JRB3ByVzvRavWCh6ITsHYR_SJ48k1Jh_ABYmJElp1cI5z3yfUnPY9oaygYpNf36Yss-cXdHHfh4Xe2DY1vi3QyWZD_TkCmEP5vmaq0FVYBBPkDIXmXaV-u1v3eB-kdp4cD-PEmjiW6edOlYlQlFJjGWp6xf2eZ7cYiUzDmEu_obKfck4OCNnmoHPQMDguaI57PCYjJByiBVR5zJqOy6L4gKayLG0Imm1-vMgVHzpquBIyAdoKPrCu7hYH2biHOQCCTytWfI0vYRZzfMoUyLzb4dwkpGtaz4VrVyFYdrRCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=TaYWKahYjfdqy3RCKJnguhhNnFwr3zLbdnTcyW9zPAdVNRuqZOSf8ixkNmzrrf5GjwoA3Ec5yKxePuhR6RDJULe0DmOqIhQz7a-m67zDxSmfKb9iPawaAbu2bJ5YFQ1viJyAlnI8e9LDN2Np5EMXWBkAFRhGTNLm8uObuAnepl4msA3XbK9y1jIB4SYHZuDYRCINC6uowi7VqTF4SiUeVfKhlrHOYijDSbMk6xsqiOu6qsb2lqursQSUHo4gNgCOnp3wpREU_BLrQhMZ2gSy8wGvUix5HyNMkHfu8C1HwyD9NvioKCcOfF4US1eKZ1oKW9uTxZnmh2K1bhV_P-l2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=TaYWKahYjfdqy3RCKJnguhhNnFwr3zLbdnTcyW9zPAdVNRuqZOSf8ixkNmzrrf5GjwoA3Ec5yKxePuhR6RDJULe0DmOqIhQz7a-m67zDxSmfKb9iPawaAbu2bJ5YFQ1viJyAlnI8e9LDN2Np5EMXWBkAFRhGTNLm8uObuAnepl4msA3XbK9y1jIB4SYHZuDYRCINC6uowi7VqTF4SiUeVfKhlrHOYijDSbMk6xsqiOu6qsb2lqursQSUHo4gNgCOnp3wpREU_BLrQhMZ2gSy8wGvUix5HyNMkHfu8C1HwyD9NvioKCcOfF4US1eKZ1oKW9uTxZnmh2K1bhV_P-l2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We9fqE8btwzWW1S-1leHSWVwv4xlOrvSQonFjD8pmfIRX7w_a6-LWOgakBRVQs_6llAsg93clRhFHlsiLcNq-nMlreQIkeDNx23XrZ4VfeeP9moJ9edeCk_y0o-XX_RgFsG4IM5IMMAJHsSMWFH4ap3o18iKpDwNCsjmZChP7FriZVvQfkfW3S3jAuYURPYRR0HcHNLfD8D9H0K9tm4hMCiMYOz2b9oeI36iOexMfAVI9obv8AoSCznDp-J5dFSuViARNLlvDOe3cFGDxPzunyZP__8j0PqNgWDyTGw8QU7FB-71UVo4a4KBGoNhdwnbrG_i8bpjX0CJUaGMfxVPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=R285Th6VXM_GYY4jBV-J8PZCIqC0_-3C1HTMXxIZUFG5wC1yriCI2xXEivGAHtJXcvoxdzx8E5jdkB8CwbIxlH2G_IgsioR1_aJTBobJw85fLrAVIyuwqgau2G5xE1JstlXDt-GrwZlft8FbxfHOCNXbKDke4XH_SsW_ukqt1x-DRmUDXx8X2B-Z92msB42SaJooN9TJW3H6XPv2k-P_cvDCr6IyvRl_jV_HBDcSPDODoowjdmi4BpT1KkhSFvXPF4NWEsqug3UTVkiIBZ-YxkYi3GTT7adHfTDEfaXvkjpA7oe8LmTjk4lLn_EF_MOLSfhndu4PlB0XXNis40BeUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=R285Th6VXM_GYY4jBV-J8PZCIqC0_-3C1HTMXxIZUFG5wC1yriCI2xXEivGAHtJXcvoxdzx8E5jdkB8CwbIxlH2G_IgsioR1_aJTBobJw85fLrAVIyuwqgau2G5xE1JstlXDt-GrwZlft8FbxfHOCNXbKDke4XH_SsW_ukqt1x-DRmUDXx8X2B-Z92msB42SaJooN9TJW3H6XPv2k-P_cvDCr6IyvRl_jV_HBDcSPDODoowjdmi4BpT1KkhSFvXPF4NWEsqug3UTVkiIBZ-YxkYi3GTT7adHfTDEfaXvkjpA7oe8LmTjk4lLn_EF_MOLSfhndu4PlB0XXNis40BeUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni0Y5awO0IMNY_V9GxNlzbROVu-toMRN3Jg720g4Yse6IOZt7ixs03RWOYZvkvuWjYCvyC2mneZp9nIwiLirD3euWnbFDAmgnU3_59wkkNan0R6vJbOw2tAdXOlWT5tVNW5r8JDd569ur86xUqXU266QjgTLcNc1rZEMCvjBLhixvny-nj1U3vGA-lwURoIN5yn5yYTgscB5UlmE8Kd2B0FFx_9PAGkpLqABNLN7yGpNaK_Xb5sbMxj5ypQ0djtf0Z9rEIdFW6qTfiiG2XIHgGn7pAfL5_nmUmzeVikrOATJBrbuvcK9smytI6zhRlMZi0Co-CbhWn-8KzezGq_B1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8GKm3VaLihkul440I7y-RFFMyWCSS6oYuZlpMLUO9GUGSMg-VnC2BZ2NnoCY6DtRJMTXGttnlHixVYaPj_UqSMWs_FmC0O6WD35dM4ton4VQeOVfiZhOiOREZDqq9Q4iq_rBwHVNXiH5opMXnhIoh1kELnNtHzkRSrhs-PyY73iz4eIRc20KdzjdjV103vu0flJ5gFL8lYLdMUWWKmjDQLyDQOfFLXsgQHQssEGmPIjkJGuZE3PFn1k0xJiQz_k5V72yXDHjf7Q4WC2uYu9C70RLYMoKEfqSqTojkrZxyYc4puVbR6vKjZZO2S_MY81qgS4cMBCxCColIH2bn1_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=iSZdk7u2IQ0KWwM_cnjqFDAu9qKLXyw3ABDjd1aMNO7igyauwsh4fCzXwijHxgvOvP0jum0yUcqAvbpyyI8nHccy9lcszDb-L2O36TI4PQRK2CiQHz5QKpo_OgqgAP5viv2vlMq3D3o-QjVbKKNFQwKSinkfBVLERJRyOEGrufwb4bn4UA9zBpuIx7-msnkPeEqZD1-kAfu6m5_0sPie_04SB_KZqB6iUMrBGT528zlfkXwsiFOrBxVIu8g1HJyICssaZimf967sKEK5SJtxHbM_hJYlBgG0WkoBUc9NHaNnz5H7C-enApXRjIMQEynoLzKaPZU5mhR9rdF40cIGkBRbEoA-YIg_i2DRh0-GrKdzN0dMEkpQFdhIpTph6LjUPPsgrwxhPLui3Q8ZkYSFD5S9IZe_9vDp0lMDxl46Nt6pp64a_VEZ0ScMUDGUsWqEztcwQc-k9xHdJo0muWfwTZki7nwb4wLgY8CdX4BsumOf6Rf0l3s2tBXqzz-FlLegcqoYqh2tZ7ksKB82aSAxok2YaVMjSJwRkLwBnFEWydjXu8AJXXOl4G8OmZA1QZ1AVTfwrR6Mk555A9pBGs0aiPJXPkzobxcAKHP66q62L9LhaEu9sXtrCp3UdVLmKqIHpHo-KFGWA-l0F6V3HvvrDrK5U2FX2pWEanISUBHrPD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=iSZdk7u2IQ0KWwM_cnjqFDAu9qKLXyw3ABDjd1aMNO7igyauwsh4fCzXwijHxgvOvP0jum0yUcqAvbpyyI8nHccy9lcszDb-L2O36TI4PQRK2CiQHz5QKpo_OgqgAP5viv2vlMq3D3o-QjVbKKNFQwKSinkfBVLERJRyOEGrufwb4bn4UA9zBpuIx7-msnkPeEqZD1-kAfu6m5_0sPie_04SB_KZqB6iUMrBGT528zlfkXwsiFOrBxVIu8g1HJyICssaZimf967sKEK5SJtxHbM_hJYlBgG0WkoBUc9NHaNnz5H7C-enApXRjIMQEynoLzKaPZU5mhR9rdF40cIGkBRbEoA-YIg_i2DRh0-GrKdzN0dMEkpQFdhIpTph6LjUPPsgrwxhPLui3Q8ZkYSFD5S9IZe_9vDp0lMDxl46Nt6pp64a_VEZ0ScMUDGUsWqEztcwQc-k9xHdJo0muWfwTZki7nwb4wLgY8CdX4BsumOf6Rf0l3s2tBXqzz-FlLegcqoYqh2tZ7ksKB82aSAxok2YaVMjSJwRkLwBnFEWydjXu8AJXXOl4G8OmZA1QZ1AVTfwrR6Mk555A9pBGs0aiPJXPkzobxcAKHP66q62L9LhaEu9sXtrCp3UdVLmKqIHpHo-KFGWA-l0F6V3HvvrDrK5U2FX2pWEanISUBHrPD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
