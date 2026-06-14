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
<img src="https://cdn4.telesco.pe/file/bsefD64zyA_telpyIfSw1n9i2_-5OwxYgsMAAAKWErA-umviJEOkebZILHe6RU5gOW2jx2GOOwRRD6SQg6nheD6wqsxu9E7Co-NVCgea7Suk-oFjFiPYgmb0vi1MW0oH1P_x7NfMtTTpfY-Bqzi3XoekBw-S51qFrs2ehtnTct5TtOVQ1yF5RJitI252DYc2ib8aJR3rxPdAfnnBc9PVBuPe5pnJudlsL9pIX10WXNNaHZf_JKaMBk-miAU2K33I9NhI_W-KnP2F4XlsqMNsWM0Di7t7He3VbceEk9T-LMOjnjwhLBvfuGbEjSzHC5M03Z5c_cN8MEPSryIx4RcDMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-442131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqEfkZQnpXkMDFKeaGQijW4IXzFH9Aw4fhcLbxi5k6cAqs5vIPwp8A6B16VY_Ldep-4hFLPswkZhm-P0ZuuYKDhk2Rw5vXJ6EUfDnak0zZVUHZI1de-vj_tbbq-ppok8Pbsu_5-vASoIA3GIcY5GqIbMokwNKJPgBQZLuNvZKtiXmOUnMx3Pq7cc_ltkU1MzQ-luoiUk2WQ0k_pN1DDnDKoyN-UtnTEqOT7sdojkumrR8b77VJh_Kl2-idhgX2XLg1cT5e35_RwnSoy77REIhcs7ZsIirbJr2oy288r3cygxkbbH41aBmK6z7rtCU96YqcEiWs-YaLFpD--Vcapm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۵۸ کیلوگرم موادمخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: ۱۲۸ کیلوگرم تریاک و ۱۳۰ کیلوگرم کشف و ۱۲ نفر از سوداگران دستگیر شدند.
🔹
۲ اسلحه کلاشینکف به همراه ۹ خشاب، ۲۹۶ فشنگ جنگی، یک دستگاه استارلینگ و ۹ خودرو نیز از متهمان توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/farsna/442131" target="_blank">📅 21:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442130">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4302e6bf30.mp4?token=ktnhByTaGY34T5t6q513Y8jTr6MdPXI2dvGkiY7QbvDFR2RWctDX9zCGakLzwFhX1MAWmtzvx1txSelxW5i7Uo5TOj3jyYFUgtTgKnYIuOYUo-h2wq0ldL-E15wVFNVgkIwwbe6Jz4YIcQHujLTeMcpkARGOpQOZbrYe9l7ahq4G7XJPukesDwEvaXgAbEwBXy7VoVT0MNJPjkx8wvgoJDjST95E6xLnqbI2LpfTl-c6klxLJOaefeWVblJpXc8dWrhaOA-i0qP-PBSbxQHPT6k2qUXixUUDpfvvv0tUgSnXUHkXfLsmf2p0yU91p5cUmN5edXtOMjRnGjOR9lILBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4302e6bf30.mp4?token=ktnhByTaGY34T5t6q513Y8jTr6MdPXI2dvGkiY7QbvDFR2RWctDX9zCGakLzwFhX1MAWmtzvx1txSelxW5i7Uo5TOj3jyYFUgtTgKnYIuOYUo-h2wq0ldL-E15wVFNVgkIwwbe6Jz4YIcQHujLTeMcpkARGOpQOZbrYe9l7ahq4G7XJPukesDwEvaXgAbEwBXy7VoVT0MNJPjkx8wvgoJDjST95E6xLnqbI2LpfTl-c6klxLJOaefeWVblJpXc8dWrhaOA-i0qP-PBSbxQHPT6k2qUXixUUDpfvvv0tUgSnXUHkXfLsmf2p0yU91p5cUmN5edXtOMjRnGjOR9lILBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازی‌ای که برای ترور کردن ساخته شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/farsna/442130" target="_blank">📅 21:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzArSgkzJ946fsC9_EDloYmlBSiTwNmv6rxBZO6im9ejEqU7l7rbVumuUZq7aB0SnxsncPwt8P7pW_RtO1JVPE5NfkSc0PWYE7N2Yg8Tj1y1W41EuT-WfzNEBNZK1fgYhRjKhABmI35pmmPeGMv21PLD6uGV6a5tklPkxVgD7KnYSw9msr7_axYutRm6enjYAunmDS5QWzbMwsvtEW67x_tmZCPvckpMJbtFaz0S5LSGw8T8t-e1k4_fwjKCEnZabHTH2f3fTrYEfmA9GLuB0Yn8OtWeNLsi47piMI8jz9P70-AdkzewUWZ5AW4eNl2Z4Db9dJKRWeLEWE1qYPYN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: پاسخ رزمندگان اسلام در پیش است
🔹
ذوالقدر: وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
🔹
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/442127" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS6wced02vbh2m77pGrIyCvGIwru9FLnLNhudFDNyuKZ-BYA0ObQbB9_juiwHNAM1-9pS4Xah2NLPGH48g5rnWCkomuVEYdGFWyvei1BniIkng3dCIoz6JPdGqaDj7ZeF35fRGCJhRcan4uN0u2asO3UgxDQExXXwzdSlwfWG_giTahyHP91X9UOwnSr0g_vdcF6v1B1O_r_Pb_ZhfFdvWl9TteEiyEl75FoPTV2phwZYRAZ3xVuG8hF8auvxFOZX4kwgjHlHkyheeW8f_TSiHhk_FCU7yYH6CUv-pOYx7yXthnQPQrkOQ2TgGf0LskOiUVqPHfrRiQgXbObbFn6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیر روابط عمومی شرکت خدمات انفورماتیک: سیستم کارت‌خوان بانک ملی تا ساعات آینده فعال می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/442126" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8574d680a3.mp4?token=KBJvVUb24o5pFCqjyiPMw2Ax1vVQ4-Z5y08dA94uzzkvVHGfLIEZLXR4yby94XKLDaJ-Z1So0BGZdZyzPDXQHznT-4K-ltpn0zygi3mC335Qf1rKhmIXBAMOE3clHFxzr8qunMAq6Fgxm3hM4TpgLoNPuo9fvJkcSuWQRanGF1GwK60I6vBin3rMQNW3A-RnOm_jgDxYtrxI-gpIO6b8Ya6OxapOaajt5ss1mvaCfm8gTrgdT5Z0QWntIp3jSZbeL2UA4yBNMJ42UHKCU4_bS52W3dAYnij-P31OLUXybitvFr9zY37qETMceziSukLpM1KmtbMUtuS_jRP0b7cQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8574d680a3.mp4?token=KBJvVUb24o5pFCqjyiPMw2Ax1vVQ4-Z5y08dA94uzzkvVHGfLIEZLXR4yby94XKLDaJ-Z1So0BGZdZyzPDXQHznT-4K-ltpn0zygi3mC335Qf1rKhmIXBAMOE3clHFxzr8qunMAq6Fgxm3hM4TpgLoNPuo9fvJkcSuWQRanGF1GwK60I6vBin3rMQNW3A-RnOm_jgDxYtrxI-gpIO6b8Ya6OxapOaajt5ss1mvaCfm8gTrgdT5Z0QWntIp3jSZbeL2UA4yBNMJ42UHKCU4_bS52W3dAYnij-P31OLUXybitvFr9zY37qETMceziSukLpM1KmtbMUtuS_jRP0b7cQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ شکار امروز پهپادهای حزب‌الله
🔹
حزب‌الله: یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/442125" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7d56e42c.mp4?token=lBPYTHmyffO9C3rNf8am9tVdrwI3XwQAXcRDpNi1Xz_z_tmqcFO_lwLqIja6tUpOjcpqnESwcpiZNC8-rOsZqfWSWKxx2o4Q3fmvVef5GLlCX9clGoRgrqYWCjlIni3gpIf-5xDnVRYZwYzvcjHz-L4HLktTvf32OaH2OTDgzIGIVsbVL6QK9Xik4UKzYFxQZ15i6x7NCZTKFJjaleXSI8XrZla9toPQY7S680n0q5wh-3nrN37oOyamoNpT60Y8-9QxsnNnarJBa0OEfIeZSWaZU9lpEODOlrTh8DGfvANu8Rv_PNMFh8tsgohK9mjHmp-eoL-7eWtxzigxnshyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7d56e42c.mp4?token=lBPYTHmyffO9C3rNf8am9tVdrwI3XwQAXcRDpNi1Xz_z_tmqcFO_lwLqIja6tUpOjcpqnESwcpiZNC8-rOsZqfWSWKxx2o4Q3fmvVef5GLlCX9clGoRgrqYWCjlIni3gpIf-5xDnVRYZwYzvcjHz-L4HLktTvf32OaH2OTDgzIGIVsbVL6QK9Xik4UKzYFxQZ15i6x7NCZTKFJjaleXSI8XrZla9toPQY7S680n0q5wh-3nrN37oOyamoNpT60Y8-9QxsnNnarJBa0OEfIeZSWaZU9lpEODOlrTh8DGfvANu8Rv_PNMFh8tsgohK9mjHmp-eoL-7eWtxzigxnshyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
امروز به‌صورت همزمان گروه‌های سرود جان‌فدای ایران، به‌طور نمادین سپر انسانی در اطراف زیرساخت‌ها تشکیل دادند.  @Farsna</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/442124" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9637adae92.mp4?token=Tb2uhkKaiCNgPPdkoCC9cghAqlQqfOZeUt8802N7IJhE-rQGgeB8De7V33-sGzRpoFkg-_tliAObT7FWIh-wc3_eggSKspL6uZMwOnLx6wC7L3bS5j99DREQkIh3sGVQgfpLgGrkx66V3UkYRRXhWCI1cUjF7dHYlSES6lb3DcqQZmPKUoV6SVNXsvzJ2EHSaCdIIHnoGtCZLnTZzAlUvQyeojsIwwuCCtG7vQvpbRUjxWL2McbqwzB3M6HXI15hBdCrIuFoS0OzJZ_ceHQhr53VTGsO2wxIwOp_jUyGQDR-70UTD-hHs8Ad-AhuB2GgyBWIXunighlBnJJlN2Ziiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9637adae92.mp4?token=Tb2uhkKaiCNgPPdkoCC9cghAqlQqfOZeUt8802N7IJhE-rQGgeB8De7V33-sGzRpoFkg-_tliAObT7FWIh-wc3_eggSKspL6uZMwOnLx6wC7L3bS5j99DREQkIh3sGVQgfpLgGrkx66V3UkYRRXhWCI1cUjF7dHYlSES6lb3DcqQZmPKUoV6SVNXsvzJ2EHSaCdIIHnoGtCZLnTZzAlUvQyeojsIwwuCCtG7vQvpbRUjxWL2McbqwzB3M6HXI15hBdCrIuFoS0OzJZ_ceHQhr53VTGsO2wxIwOp_jUyGQDR-70UTD-hHs8Ad-AhuB2GgyBWIXunighlBnJJlN2Ziiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست.  @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/442123" target="_blank">📅 20:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8b423b02.mp4?token=p-qFu6T0YOO7V7WKGcKPOKABY7mf0cJGa6AoLj1W8vi-5-syRXtF9jp860SG_QEbQCCPwxT2oNEyc0B3RdtjrpSvhqRcrUb6dLMmOXdRDFvkMdKNdrsO-20QVb1rHPdUysrw6tGtUeAHwbZQ6F9eBJqAQkruPLTEZjNEBhqHpkDy5cqxQVK8jdHzOfhgBru1iS99wKbaeoP4ThSaBaW4HDs8ZDnuHbGhK-dY01aPrPtRK3Zu5YLDk5usOaccpG7LHZCCG_q8Ic6sJrppXaSsmn7a9iX9kyhiguf_vogDWNFM6EpbrCZ3Ptf9Teiec7i8zvKtrnykwGCQmDCWIY3SKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8b423b02.mp4?token=p-qFu6T0YOO7V7WKGcKPOKABY7mf0cJGa6AoLj1W8vi-5-syRXtF9jp860SG_QEbQCCPwxT2oNEyc0B3RdtjrpSvhqRcrUb6dLMmOXdRDFvkMdKNdrsO-20QVb1rHPdUysrw6tGtUeAHwbZQ6F9eBJqAQkruPLTEZjNEBhqHpkDy5cqxQVK8jdHzOfhgBru1iS99wKbaeoP4ThSaBaW4HDs8ZDnuHbGhK-dY01aPrPtRK3Zu5YLDk5usOaccpG7LHZCCG_q8Ic6sJrppXaSsmn7a9iX9kyhiguf_vogDWNFM6EpbrCZ3Ptf9Teiec7i8zvKtrnykwGCQmDCWIY3SKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/442122" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442118">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3o6BuduX72mYvYnYEnO44a5dU4axRfJ2m_en5jt8Gzhn0c_oC2vrdloQ18rToY7j5nwFmBBTfCoeJNspevRajQtGWOpn7s-lBkeZCG1F9CYPYqKnbv1-V-JSvXdWA69gTfHlNZ4D7is9dyZWTL29crjRIFH6SAVg3Wh0eBlBbpO-cYkEjoedaiJr_elz5iqAGdWjEaVtCCudZ5M4DQnZphFJvr6Xxxz9Ecah5ihlh8rdzb097-PgKBVZpgJ8YFb9e9GZD9jFEnbrape747-1_zhttd1o5keXDNJm8QHVDWvyv97QYQUCwwexzVADg80YqI5677UFCjM1-FJAY9UpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ9aVNk_-5wefvNglk3tZZPCDtqewLS_8-CI3JFDAhwaMQFtfqo_eDXS1H4CbSTHGoPsk64MUV-XHS9sc0nTm2xbwy2BQ8C0INeeJNhTV-73jricVrdtatIrECZ8meXEfpoVQT1q120jyWAhtJhq8jHSvb6lly5Z98fk38m7ILU-d5dlv1jf_oWmM9_BS6EsGP8168jSgBv_ihLBlUFjc3tefbiP6KH7JDXHcoiA_1_-nxQC1rUQdNlSMM504lMY84jqeUpvFiTXxMEwgNcCtYIShzgy6QMvqqsL71qdVVJYyCLthrR7XvfAew1roTJ1KNIgjuflCFhrtfx7Kgs6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofbSOlNqDrb0I5nUmy1X8sR5pSVXzZrMPMwT-4r_WFSuYIjpPml7mjFTFizIVCKEisLYpArVRFBbMDLTfkqEr39Q7DqgdHXRsQTEDsMUhuWks9PgpvZbUuI7OxYbkm71g-7BPeLnq99MO-HuqShJtpXTetmS0v4QonGzL-Gx4Nxz0tRYVJnu7qPxsnSsE3FDUMzw1Hv5iDfE6a9SAUQHNcE_2_-jLlb_1RG2Ip0bt33ByPMCfcP7fW-a0BHgjpItK9ooeIp3DjSerHnrGr2zSUbxZomhAL9NHgS2ctpxJRgQ-QFDFUkSYgTN2jayZnSdlkXg-dLlmZNCAZjWAymVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDn7PusdF1D6pVGCQgKGfpqPMOaeI9X4LoE0HKBM4BJQ5XnXCMlO2RWlO8O7cQJIlRS3LnTS6kTuNymo6PdSNDbYTyNZcCwlRpdmnUni7uyeGGJGyYZk-YwYd6eC3l0sU_T5ZU6ugTBK4zF3h4yq8MeWQdWdoyJemwywMwp5YdfDBgKvqezXEvB0S0CXRMc8qRpRjZjAWFr6oUwHG4QzPQRduccpKJLpLVwJ_j8sl38-2ZUm3e83T8trzzGpwcorNqftdoqUlAInLixzkjqq99fgi0e2-FkSruNJQ31nTh0pRJ4jYt5Sw_oQV37lxaLZKbpwKMrFPNGgoiQJwXbGeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیاء: فرزندان ملت دست به ماشه آماده شلیک به قلب دشمن هستند
ملت قهرمان ایران
🔹
مقاومت و بعثت دوباره شما، فصل نوینی را در تحولات بین‌الملل رقم زد و جمهوری اسلامی ایران را در قامت یک «قدرت جهانی اثرگذار» تثبیت کرد. فرزندان شما در نیروهای مسلح، به‌ویژه فرماندهان شهید که تربیت‌یافتگان اصیل مکتب امام خمینی (ره) و امام خامنه‌ای شهید بودند، از روز اول نهضت، بغض و عدوات با استکبار و صهیونیسم را جزئی جدانشدنی از ماهیت انقلاب اسلامی می‌دانستند و می‌دانند.
🔹
اتفاقات یک سال اخیر، از جنگ ۱۲ روزه تا «جنگ رمضان»، علیرغم خسارت‌های سنگین و داغِ جانسوزِ شهادت امام شهید، فرماندهان و مردم بی‌گناه، یک فرصت بزرگ برای «تسویه حساب تاريخی» با جنایتکاران فراهم کرد؛ نیرو‌های مسلح به پشتوانه‌ی مردم و با عنایت الهی بر سر آن‌ها آوردند آنچه لایقشان بود.
🔹
توان رزمی، دفاعی و قدرت موشکی، دریایی، پهپادی و پدافند هوایی ما پرقدرت‌تر از گذشته و تحت اوامر فرماندهی معظم کل قوا حضرت آیت‌الله ‌سید مجتبی حسینی خامنه‌ای مدظله‌العالی، ارتقا یافته و فرزندان ملت در نیروهای مسلح «دست به ماشه»، آماده شلیک به قلب دشمن هستند.
🔹
آرمان مقدس فتح قدس و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزشی از سوی دشمن متجاوز هستیم تا درسی فراموش‌نشدنی و پایان‌بخش به آن‌ها بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/442118" target="_blank">📅 20:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442117">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81dda67827.mp4?token=GZdwWQIQVVNfMVSc2_T-4EaZ9QOoPTSszF4jvNIHg0ynB3nh8c02F4KbbbzJnhkTTwWNdPS2KJte9lMGn9G5V9QLjeKZTTXpINkqE9ph4nKcckPeBPdoI2LY2M3FZiH7j1ZKSXwyYK4RRxpDrBjnUha30oK2ydCVIt6xH4xK3sRo9Nd0aakhZpEl25B1jhZRNF0MkXtPEU_ey1l413GMx4G0-4zfKbDopfVA0992BR4CGGlLcZWlo443LuViLU88QOotsbHjXoz2Luw5LVgPQHpabNS3aZPv4GAeZtVLquM5o8yz1HkSaD4qig4E90xQe28zIPhjAvSXj1tncSdavUzldlsFAbDy3z_LHQSJaPvQLJnlCTWsWx5L-o5pVfH1jkpeG90ugZayHluWnafKycOkDAW2flrURYEYvIXEE4bSrek7h-bHeNA8zo_gxFF4CaZblueW0y3PLWFKzt1MllqOqNKJgwg-HcpxB6O30fDRinpFxGscf46Iv9O5P0Xea6wQIfP7LBxpad9wEDp9EBBmlc58Vo03AtOIQzisLR0u0buAR2-TgyI5vGSUDoCFNCEr1ckJI0hnGFTqhWDS23NCZC2Vcc9RVFzYOWycmHfOsgR-1E08pigTcKXB0uXdIGGE7Oiu7k8xrjHML4pnDHQHjE9DAsejzx2F37pwsUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81dda67827.mp4?token=GZdwWQIQVVNfMVSc2_T-4EaZ9QOoPTSszF4jvNIHg0ynB3nh8c02F4KbbbzJnhkTTwWNdPS2KJte9lMGn9G5V9QLjeKZTTXpINkqE9ph4nKcckPeBPdoI2LY2M3FZiH7j1ZKSXwyYK4RRxpDrBjnUha30oK2ydCVIt6xH4xK3sRo9Nd0aakhZpEl25B1jhZRNF0MkXtPEU_ey1l413GMx4G0-4zfKbDopfVA0992BR4CGGlLcZWlo443LuViLU88QOotsbHjXoz2Luw5LVgPQHpabNS3aZPv4GAeZtVLquM5o8yz1HkSaD4qig4E90xQe28zIPhjAvSXj1tncSdavUzldlsFAbDy3z_LHQSJaPvQLJnlCTWsWx5L-o5pVfH1jkpeG90ugZayHluWnafKycOkDAW2flrURYEYvIXEE4bSrek7h-bHeNA8zo_gxFF4CaZblueW0y3PLWFKzt1MllqOqNKJgwg-HcpxB6O30fDRinpFxGscf46Iv9O5P0Xea6wQIfP7LBxpad9wEDp9EBBmlc58Vo03AtOIQzisLR0u0buAR2-TgyI5vGSUDoCFNCEr1ckJI0hnGFTqhWDS23NCZC2Vcc9RVFzYOWycmHfOsgR-1E08pigTcKXB0uXdIGGE7Oiu7k8xrjHML4pnDHQHjE9DAsejzx2F37pwsUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای ترامپ کیک تولد گرفتیم!
واکنش مردم را ببینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442117" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442116">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex9LI-gOF9VVxkNY39vVF13B1CT17dsdTNP_X0fTHwvwbSE1mlh7k87HUZcyvlm7I4PCYHezc7aDMnDqxL4wNgl78EMpbBLrxTQeZ7T-SBqSLdW098DQOkivd7UgJD4ZtVaKUhTdJjkIg-2Pl4bhSNjDhgHMc5f8dnFhjy5DReK5efwn-smeACO9gUrILpzfgXgB83kCLUEQFs8zbJx6rK_0NupKsNO5Ptb5zaP2ACuOYbffTCtn6cTSbR8Tanmlhq_VivleLAlOi91lElHVsb_RcPHK4SnYnzSsQeUIeDQ_8UCfXqR4aebfJJysEvuYdfOKFgqlYohKEUpgRXHRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبک شاگردان پیاتزا تکمیل نشد
خطاهای فردی کار دست ملی‌پوشان والیبال داد
🏐
لیگ ملت‌های والیبال
ایران ۲ - ۳ بلژیک
🇮🇷
ایران: ۲۳ | ۲۲ |۲۵ |۲۵ |۱۲
🇧🇪
بلژیک: ۲۵ | ۲۵ |۲۳ |۱۷ |۱۵
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442116" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442115">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۳ شکار امروز پهپادهای حزب‌الله
🔹
حزب‌الله: یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/442115" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442114">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd60451a9.mp4?token=YZ1MqffZMdA8-tYkQRjU6Yq_SlFXDH6thWqVO-6v29vv43gCB5bWlL4wfD7fLHVygttVDLlFfjLPsb5w7_yBY1Y8wk1zrwBcjNmR-VEPeDOm9oxtUsZbx3UmKzDQ-qNvEKe2BUOabz9EpMh2pmgl7Zp-YmYJGrkymrdNsevjKaJnUVIOUiSTnz3V_8afTVWMhWOLR7uQHr7BZ544lYXRnSrSwFWYYhOSD04klKeeXBZxGeQKaOxoDjVfz8zkT29L48VsB3SVpRUfbIO4zgPhOb3CMfp3bz_fG61OyNDhqAAeCiwUvfHTZHMBZ1ojheBRNv8VgP467zv4d7Twv7oOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd60451a9.mp4?token=YZ1MqffZMdA8-tYkQRjU6Yq_SlFXDH6thWqVO-6v29vv43gCB5bWlL4wfD7fLHVygttVDLlFfjLPsb5w7_yBY1Y8wk1zrwBcjNmR-VEPeDOm9oxtUsZbx3UmKzDQ-qNvEKe2BUOabz9EpMh2pmgl7Zp-YmYJGrkymrdNsevjKaJnUVIOUiSTnz3V_8afTVWMhWOLR7uQHr7BZ544lYXRnSrSwFWYYhOSD04klKeeXBZxGeQKaOxoDjVfz8zkT29L48VsB3SVpRUfbIO4zgPhOb3CMfp3bz_fG61OyNDhqAAeCiwUvfHTZHMBZ1ojheBRNv8VgP467zv4d7Twv7oOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ دندان‌شکن سفارت ایران در کنیا به سنتکام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/442114" target="_blank">📅 20:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442113">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
🔴
پزشکیان: هیچ فرد یا جریانی نباید خود را فراتر از سازوکارهای رسمی تصمیم‌گیری بداند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442113" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
پزشکیان: برای من پذیرفتنی نیست که در جایگاه مسئولیت قرار داشته باشم اما بخشی از مردم با مشکلات معیشتی جدی مواجه باشند و شب را با شکم گرسنه به صبح برسانند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442112" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442111">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
پزشکیان: رسانۀ ملی درحالی بیانات رهبری شهید در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی «نه جنگ، نه صلح» گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442111" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442110">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
پزشکیان:  تصمیم‌گیری درباره جنگ و مذاکره برعهده شورای‌عالی امنیت ملی است
🔹
در این شورا نمایندگان تمامی ارکان حاکمیت از جمله رهبری عالی‌قدر حضور دارند و سیاست‌های کلان باید از آن مسیر ابلاغ شود.
🔹
نمی‌توان خواسته‌ها و برداشت‌های شخصی را به عنوان مطالبه…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442110" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442109">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
پزشکیان: کسانی که خود را مدافع ولایت و رهبری می‌دانند، بیش از دیگران باید به سیاست‌ها، چارچوب‌ها و تصمیمات رسمی کشور پایبند باشند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442109" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442108">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
پزشکیان: در بسیاری از موارد، ملاحظات بنده معطوف به آن است که مبادا موضعی برخلاف نگاه و سیاست‌های رهبر معظم انقلاب تلقی شود و به وحدت کشور لطمه وارد کند. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/442108" target="_blank">📅 19:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442107">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
پزشکیان: انتظار می‌رود رسانۀ ملی منعکس‌کننده سیاست‌ها و رویکردهای مراجع رسمی تصمیم‌گیری کشور باشد
🔹
آنچه گاها در رسانه ملی درباره جنگ و مذاکره مطرح می‌شود، لزوماً بازتاب‌دهنده دیدگاه شورای عالی امنیت ملی، شورای عالی دفاع یا حتی رهنمودهای رهبر معظم انقلاب…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/442107" target="_blank">📅 19:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442106">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
پزشکیان: عبور موفق از این شرایط نیازمند همراهی مردم و مشارکت عمومی در اصلاح الگوی مصرف است
🔹
در ماه‌های گذشته، وزارتخانه‌های نیرو، نفت، کشور و صنعت با همکاری و تلاش مستمر توانسته‌اند با وجود ناترازی‌های قابل توجه و همچنین آسیب‌های ناشی از جنگ به بخشی از…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/442106" target="_blank">📅 19:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442104">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
پزشکیان: مردمی که در در بیش از ۱۰۰ روز گذشته و در سخت‌ترین شرایط از کشور و نظام حمایت کردند، اگر با تورم و مشکلات اقتصادی پی‌درپی مواجه باشند ممکن است دلسرد و ناراضی شوند
🔹
دولت خود را موظف می‌داند تمام توان خود را برای بهبود شرایط زندگی آنان به کار گیرد.…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/442104" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442103">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
پزشکیان: اگر امروز کشور توانسته است از یکی از پیچیده‌ترین مقاطع خود عبور کند، این موفقیت حاصل تلاش مجاهدانه مدیران، مسئولان دولت و همه کسانی است که در سخت‌ترین شرایط، اداره کشور را برعهده داشتند. @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/442103" target="_blank">📅 19:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442102">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
پزشکیان: مذاکره به معنای چشم‌پوشی از اصول نیست و جمهوری اسلامی ایران در برابر هیچ‌گونه زورگویی و فشار غیرقانونی سر تسلیم فرود نخواهد آورد.
🔹
مذاکرات تنها یکی از ابزارهای تأمین منافع ملی است. دولت همزمان مسیرهای مختلفی را برای تقویت اقتصاد و ارتقای جایگاه…</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/442102" target="_blank">📅 19:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442101">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
پزشکیان:  دفاع از منافع ملی و حفظ اقتدار کشور در چارچوب مذاکره نیز رویکردی محدود به دولت نیست، بلکه تمامی ارکان حاکمیت در این زمینه دارای نگاه و هدف مشترک هستند. @Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/442101" target="_blank">📅 19:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
پزشکیان: بخش مهمی از تلاش‌های دیپلماتیک کشور در هفته‌های اخیر نتایج مثبتی به همراه داشته و بسیاری از مسائل و سوءتفاهم‌ها با کشورهای حوزۀ خلیج فارس در مسیر حل‌وفصل قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/442100" target="_blank">📅 19:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🔴
پزشکیان: پیش از این نیز گفته‌ام و امروز نیز بر همان موضع تأکید دارم که از بابت قرار گرفتن کشورهای همسایه در معرض تبعات اقدامات نظامی ابراز تأسف می‌کنم
🔹
البته هدف عملیات ما پایگاه‌های آمریکا در خاک این کشورها بوده است. @Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/442099" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌
🔴
پزشکیان: تصمیمات راهبردی باید بر مبنای عقلانیت، محاسبۀ دقیق و در نظر گرفتن توان ملی گرفته شود
🔹
در کنار حمایت از نیروهای مسلح، باید نسبت میان مأموریت‌ها، امکانات و ظرفیت‌های کشور نیز مورد توجه قرار گیرد. @Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/442098" target="_blank">📅 19:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت خود را موظف می‌داند از نیروهایی که برای دفاع از کشور و امنیت مردم در میدان حضور دارند، حمایت کند
🔹
نمی‌توان از رزمندگانی که جان خود را برای دفاع از میهن در طبق اخلاص گذاشته‌اند انتظار ایستادگی داشت اما در حوزه پشتیبانی، امکانات و نیازهای…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/442097" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت هرگز معتقد به شوک‌درمانی و تحمیل هزینه‌های ناگهانی به مردم نیست
🔹
در عین حال دولت بر این باور است که تداوم برخی رویه‌های ناعادلانه نیز قابل دفاع نیست. رویکرد ما واقعی‌سازی تدریجی و عادلانه قیمت‌ها با هدف برقراری عدالت در نظام توزیع منابع…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/442096" target="_blank">📅 19:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
پزشکیان: تحقق انسجام اجتماعی بدون توجه به معیشت مردم امکان‌پذیر نیست
🔹
پیش‌نیاز حفظ وحدت و انسجام ملی آن است که جمهوری اسلامی بتواند در حوزه‌هایی همچون معیشت، مسکن، اشتغال و رفاه عمومی پاسخگوی نیازهای مردم باشد.
🔹
بخش قابل توجهی از آسیب‌های اجتماعی نیز…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/442095" target="_blank">📅 19:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌
🔴
پزشکیان: مهم‌ترین اولویت دولت، بهبود شرایط زندگی مردم و کاهش فشارهای اقتصادی جنگ اخیر بر خانوارهاست
🔹
امروز بخش‌هایی از جامعه با مشکلات معیشتی جدی روبه‌رو هستند؛ درحالی‌که برخی افراد بدون آنکه آثار تورم و دشواری‌های اقتصادی را در زندگی خود لمس کنند، صرفاً…</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/442094" target="_blank">📅 19:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
پاسخ پزشکیان به دروغ‌پردازی‌ها در مورد استعفایش
🔹
بنده شخصاً برای کار و تلاش و خدمتگزاری به مردم کشور هیچ تردیدی به خود راه نداده‌ام و اگر به پیش از انتخابات هم بازگردیم و این باور را داشته باشم که با آمدنم می‌توانم گره‌ای از مشکلات کشور و مردم باز کنم…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/442093" target="_blank">📅 19:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌‌
🔴
پزشکیان: دولت برای حفظ منافع کشور و مردم تلخ زبانی‌ها را به جان می‌خرد
🔹
ما با تمام وجود برای خدمت به کشور و مردم عزیزمان و همچنین آرمان‌ها و ارزش‌های واقعی خود آمده‌ایم نه ارزش‌های کاذب و غیرواقعی. @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/442091" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ ‌
🔴
پزشکیان: [در مورد مذاکرات] حتی اگر نظر شخصی بنده متفاوت باشد، خود را موظف به تبعیت از تصمیم نهایی نظام می‌دانم؛ چراکه معتقدم ایشان براساس دور اندیشی و همفکری با عقلای کشور و در نظر گرفتن مصالح و منافع ملت تصمیم خواهند گرفت نه تحت فشار جریان‌های سیاسی…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/442090" target="_blank">📅 19:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
پزشکیان: دربارۀ مذاکرات، مصوبۀ شورای‌عالی امنیت ملی ملاک عمل است و هر آنچه مورد تأیید و صلاحدید رهبر معظم انقلاب قرار گیرد، برای همه ما لازم‌الاتباع خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/442089" target="_blank">📅 19:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
پزشکیان: ما به دنبال آن هستیم که از مسیر حفظ اقتدار ملی، برای کشور گشایش ایجاد و منافع مردم را تأمین کنیم. @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/442088" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
پزشکیان: نقد و مطالبه‌گری حق طبیعی جامعه است، اما تخریب کسانی که مأموریت مبتنی بر قانون به‌عهده دارند به دور از انصاف و مردانگی است
🔹
مایه تأسف است که افرادی که در چارچوب مأموریت‌های رسمی و با هدف صیانت از منافع ملی و عزت کشور در حال انجام وظیفه هستند،…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/442087" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
پزشکیان: در برابر هیچ قدرتی سر تعظیم فرود نخواهیم آورد، اما در برابر ملت ایران و مطالبات مشروع آنان خود را مسئول و پاسخگو می‌دانیم. البته منظور از مردم، همه مردم ایران هستند، نه یک جریان یا گروه خاص. @Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/442086" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
پزشکیان: تحولات اخیر نشان داد که هیچ کشوری بیش از خود ما دغدغه منافع ایران را ندارد و به جز خدای متعال به هیچ کس نباید متکی باشیم. @Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/442085" target="_blank">📅 19:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442084" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
پزشکیان: اگر به وحدت و انسجام ملی باور داریم و اگر مدعی تبعیت از ولایت هستیم، باید تصمیمات شورای‌عالی امنیت ملی را که برآیند نظر تمامی ارکان نظام است، مبنای عمل قرار دهیم
🔹
شورای‌عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442083" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f5decafd.mp4?token=DHwpueEYJIl_Fm5vokZJcf5vRc7O3ZyDg-oqoA8tGGhkj1GbFHV6nIkWEaZmCtbpsmWQd6BEk7AzIiBI9RS8vyDIKcG5eGjmrxSoMnEydJIDvu1NHKIkaXaaC_HhtT55TWXwhHfjreMq6lrm7_LMWEe99_FaPxjPKHCJEa0Z_agqTghRuMkr9jj3FVdEUUVFrp-fJKuk7OSXsQk5YOPTHRZ5rVPYDjebvBS1YNCZR_RsF7hoLChtbYB35IzYeJcw0844JacMTlhSZ0vuh3FAvDmt6GWXXopDgfZXSBLe2cm0uZVFv8SVtGy-R3krGCRd8WEEqf2oAR8Gn-kj0P0j5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f5decafd.mp4?token=DHwpueEYJIl_Fm5vokZJcf5vRc7O3ZyDg-oqoA8tGGhkj1GbFHV6nIkWEaZmCtbpsmWQd6BEk7AzIiBI9RS8vyDIKcG5eGjmrxSoMnEydJIDvu1NHKIkaXaaC_HhtT55TWXwhHfjreMq6lrm7_LMWEe99_FaPxjPKHCJEa0Z_agqTghRuMkr9jj3FVdEUUVFrp-fJKuk7OSXsQk5YOPTHRZ5rVPYDjebvBS1YNCZR_RsF7hoLChtbYB35IzYeJcw0844JacMTlhSZ0vuh3FAvDmt6GWXXopDgfZXSBLe2cm0uZVFv8SVtGy-R3krGCRd8WEEqf2oAR8Gn-kj0P0j5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگزث وزیر جنگ آمریکا به CBS : «ما در مسیر امضای توافق با ایران هستیم و سوال این نیست که آیا آن را امضا خواهیم کرد یا نه، بلکه کی امضا خواهیم کرد.»
🔹
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران شود.
🔹
اگر ایران می‌خواهد این موضوع…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/442082" target="_blank">📅 18:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An_2lF_k7sX97HDxvJMY8kjXBXCEAeeC9cv4-yMC7IEzt-W4wAx5DFKXJvOdfgXJygxGkPpihtpgUSmU2kChZAZ_4Irf1U5_gz6PUvVBjcrnc5z8DNHnR4b9gxY5c7_GzwFZ5Nb8HMS-64DzH-6CrJm05DSe_LgF4NGgZ9sKlB9IRTr7ld1owFH1CM8T14TARFHoFxyfnv34O34G2XDHJzet7MlbgF-uJp6btg7_Ae0H2wb_TgHKcTjjqwx4Bm_mSwfyj8FqH2fFkQGrc8x8nI5KdOtkwz5meIStQPyYlkPyqzCaJiUaPWzq725YiAiLQgdpg4Wr1jLSJw4IUZOwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده هوافضا: گوش به فرمان ولایت باشید و از هر کلامی که اتحاد مقدس شما را به خطر می‌اندازد دوری نمایید
🔹
سردار سید مجید موسوی: ملت بصیر و غیور که در خونخواهی امام شهید مبعوث گشتید و در راه تحقق ارمانهای بلند انقلاب اسلامی و اقتدار و سرافرازی ایران عزیز، با امام حاضر عهدی تازه بستید، هوشیار باشید که از شئون متعهد بودن تبعیت کردن است. پس نه یک گام جلوتر و نه یک گام عقب‌تر، بلکه همراه با ولی خویش باشید.
🔹
درست در مسیری که امام خمینی کبیر رحمه الله علیه فرمودند: پشتیبان ولایت فقیه باشید تا به مملکت شما اسیب نرسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442081" target="_blank">📅 18:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به صدا درآمدن آژیرها در شمال اراضی اشغالی
🔹
رسانه‌های عبری اعلام کردند درپی نفوذ پهپاد از جنوب لبنان، آژیرهای هشدار در شهرک صهیونیست‌نشین «عرب العرامشه» در منطقه الجلیل غربی به صدا درآمده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/442080" target="_blank">📅 18:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgW63P2Yy_4iWb-SUKVQ6zCreEcyF62EglBlCfMDwR7MdtfGwj0Ec_Bq8tlxVT3dZ0I4ynY5TOOSP47o9QV7cgBXQ7_GcptVKPX9SDc6zPDtz0Sf2xsjEOVMA8_hXa61kfkSuCpgA589ZhvqlUdQ2Td98sXC4Rt18fFw5-VUgnObzX__wlr-6sVVwyQQaM1928pfvhUYpdTKVI5pVXjWHm1nm4xFaPkQwrP9wjbtX0Obx3AHjACpNHc4cYmnsAidWW7hDEVuyBe90yy_cCZRHQSkfVVNPIC2OocqyA9eAVjTAza-uRWqVBXiv9nRW9UVwzyeqSgN7pcon65jxN510g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
خبرنگار آکسیوس و شبکهٔ ۱۲ رژیم صهیونیستی: اسرائیل پیش‌از حمله به بیروت، به آمریکا اطلاع داد. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442079" target="_blank">📅 18:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I33mgbvW2Vh0RvipUqKzjo0U-8u35UanSVKeciJBSNAgqQSP8b3PfSBfRZecNlbLKCqvd7yTw2T1rX993wmK5cPNWPjfnD_yDqDc9ayysC_UfY1dlSMP2HP8lJOCE7nEIV-4nhQekrWLhpZ1y2zy57MhQGvfAbhAr3gVM_ZKIvtIyG4VaKLF-C_k9oTR5nH1lXElN7bhkUOVp47gzZGO7zsq6SoE-Jog-hEDRdi4pZ8XeFhrf4W3w6ZGvx8TtEJ8HKZgmQCNKlBXGsVjdFLOVojvWcCAKD_7Y_Wr2-nlRb2zFN6tDFGiotER4flS7JHnpSrB0PpYkXRkw0nGofHbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگزث وزیر جنگ آمریکا به CBS :
«ما در مسیر امضای توافق با ایران هستیم و سوال این نیست که آیا آن را امضا خواهیم کرد یا نه، بلکه کی امضا خواهیم کرد.»
🔹
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران شود.
🔹
اگر ایران می‌خواهد این موضوع پابرجا بماند، باید حزب‌الله را مهار کند.
🔹
انتظار دارم مذاکرات پیشرفته‌تری انجام شود و معتقدم این مذاکرات ادامه خواهد داشت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442078" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5fdb39a7.mp4?token=RvPgQpbMFgsjOAzy1XJSW3ZNWSb6YgDWMukjNavG7yIn_WH-0RS0k8lQAAjJlCPBrycGX6iMmHjIoM5zvim2Lm6NMKFu3NcV5FdJJRw9uqTBMD1-MrGls2l-m6BsPKmoYQ0AT33_5wtGw0kbmGU4rh5_8SNEla56cTd5msNtkecGAoiyZLswqc6okMGTlnIw26eC7SBP-LYm9AauIjvmDddwSs16Qvdgz5zYS1pprGaoVrkngyKMtT-xEojdTgrapOMwMGfYwL9t4JXor0jGZB4DxvacPzQY6dRevpqgsjCNqW8Yapb8MvrU1YagijyPrCgjJFC7hGzFY-dE8vnf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5fdb39a7.mp4?token=RvPgQpbMFgsjOAzy1XJSW3ZNWSb6YgDWMukjNavG7yIn_WH-0RS0k8lQAAjJlCPBrycGX6iMmHjIoM5zvim2Lm6NMKFu3NcV5FdJJRw9uqTBMD1-MrGls2l-m6BsPKmoYQ0AT33_5wtGw0kbmGU4rh5_8SNEla56cTd5msNtkecGAoiyZLswqc6okMGTlnIw26eC7SBP-LYm9AauIjvmDddwSs16Qvdgz5zYS1pprGaoVrkngyKMtT-xEojdTgrapOMwMGfYwL9t4JXor0jGZB4DxvacPzQY6dRevpqgsjCNqW8Yapb8MvrU1YagijyPrCgjJFC7hGzFY-dE8vnf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک تانک مرکاوا توسط حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442077" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442076">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjI7621oE3eUvWM4bC89NIVgFzQjyFugtEWgOKgyZWPk3y_17oiuqcoB2Uk80iIVOvXqWXUOHaxy7tFENKPkyV9wkcDPMSRYJKVjJrvWgiMnzen5FAoRtnWiaOuMpSJzz8-8EN-txvzn8XiG2uXEJmoxv9rlZ0mM9nLA_DUdsons_KDbKyXWOy3uE81hjPNwTWjsHyFuh5K8Zl9oobWeuAFrOOuVzhzcfoeoZqMZ30kr9DAlDVOYnQC6cwu42aOe_YiDnNpoSj9bbLPkNbYAkmQ445RipzXgitwJCwDbgNAY1TgSBP1NmxEWMtgXgTUnUyDsTa9Ww8Ux5fobWR5tqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش جدید سایپا از سه‌شنبه
🔹
سایپا اعلام کرد از ساعت ۱۰ صبح سه‌شنبه ۲۶ خرداد، طرح فروش مشارکت در تولید دو محصول «پارس نوآ» و «کوییک GX-L» را ویژه متقاضیان طرح عادی آغاز می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442076" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442075">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آماده‌باش صهیونیست‌ها برای حملات موشکی ایران
🔹
ارتش رژیم صهیونیستی اعلام کرد در پی حملهٔ ساعتی پیش به ضاحیه بیروت، خود را برای حملات موشکی ایران آماده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442075" target="_blank">📅 17:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442073">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVpStclVXoJmNALLvWRgagBpPAvL9p3yodJnecrPdIiZbjIexTR1qntQlbNSqqPF7_PR1OC63bh1tMjXbBFVOw5tP_HCGLsrcPsZ2hVHt8zWceKOIZAt6WIknwWFmS3_QqI1qZaKjIZvdWjvVfTVP-o-D8jnbeE-D8evRrL1Wz__KYM42kOa7QmZi_G4nAaArJlg038wxToAJWslYY7sPkXrABfz3yU1RgvOHpfK3AkgdPl16oLd8JtU2MSAI2wXbJZQeOGizsY1FkwY4VP4I0UKMggRNe0Droz5dZS0Sb0lci8mZ9GVES0ni2lV1A2scBiqaKZ60UOI-a_3zzfz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو شهر ایران در فهرست گرم‌ترین شهرهای جهان
🔹
امیدیه در خوزستان با ثبت دمای ۴۶.۴ درجه و ایرانشهر در سیستان‌وبلوچستان، با ثبت دمای ۴۶.۳ درجه در جایگاه ششم و هشتم فهرست گرم‌ترین شهرهای جهان قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442073" target="_blank">📅 17:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آخرین جزئیات مذاکرات غیرمستقیم قبل از حملهٔ رژیم صهیونیستی به ضاحیه/ حضور تیم قطری در تهران
🔹
یک منبع نزدیک به تیم مذاکره‌کننده ایران، ساعاتی پیش از حملهٔ رژیم صهیونیستی به ضاحیه بیروت، آخرین جزئیات از روند مذاکرات غیرمستقیم با آمریکا را تشریح کرد.
🔹
براساس این گزارش، تیم قطری هم‌اکنون در تهران حضور دارد و ایران بندهای موردنظر خود را همراه با جزئیات دقیق مدنظرش، از طریق همین تیم قطری به طرف مقابل منتقل می‌کند.
🔹
او با تأکید بر اینکه هنوز هیچ چیزی نهایی نشده، در خصوص فراز و فرودهای مسیر مذاکره گفت: «حتی اگر در روند مذاکره پیش و پس برویم و به عقب برگردیم، شرط اساسی ایران این است که در پایان، تمام موارد مدنظرش به طور کامل لحاظ شود.»
🔹
او افزود: حتی در صورت اعمال همه نظرات ایران قطعاً در زمان اعلامی ترامپ هیچ توافقی امضا نخواهد شد.
🔸
گفتنی است این اظهارات پیش از حملات اخیر رژیم صهیونیستی به منطقهٔ ضاحیه بیان شده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/442062" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58da26d3a4.mp4?token=XQUfOS_sATGsMs9TsPlymvRvc5robx-J7cB34XXdUx9cW_KLyNE6_lHwKcfcQUjGZnDgbO5A5HOVvQNYRggj08E3VdzmY9VKUP8V282Phm3oju21QPPS2C0eiA6N5nr894O4k7Q48XpRxmfgCAMNlkLHL1cJUF172lOGobq-hpz7Uu2vOVG0wft9ri8JFbMOvepxLAuyOXEjYOrpmhPQ-lgB-mAZbzb-34gFkf4KJ1XHv947oYY6xqrVFVIKQoSHX1FqNzz-gfDceGqXdUVRlemcxL0FNa4W9mb36Q9pCcv4MrFqEp-RRWEfIoDKQlE7y8wGbB9puapv9bn1_I090g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58da26d3a4.mp4?token=XQUfOS_sATGsMs9TsPlymvRvc5robx-J7cB34XXdUx9cW_KLyNE6_lHwKcfcQUjGZnDgbO5A5HOVvQNYRggj08E3VdzmY9VKUP8V282Phm3oju21QPPS2C0eiA6N5nr894O4k7Q48XpRxmfgCAMNlkLHL1cJUF172lOGobq-hpz7Uu2vOVG0wft9ri8JFbMOvepxLAuyOXEjYOrpmhPQ-lgB-mAZbzb-34gFkf4KJ1XHv947oYY6xqrVFVIKQoSHX1FqNzz-gfDceGqXdUVRlemcxL0FNa4W9mb36Q9pCcv4MrFqEp-RRWEfIoDKQlE7y8wGbB9puapv9bn1_I090g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در میدان تایمز نیویورک
🔹
آشوب‌های خیابانی در نیویورک پس از پیروزی تیم بسکتبال نیکس همچنان ادامه دارد.
🔹
پلیس تایید کرد که یک جوان ۱۷ ساله در این تیراندازی‌ها زخمی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442061" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1c7b7a76.mp4?token=QKcNukff4ff0387WWTOTmyZTL1dFQnbhWH7fYnCNPxGW7nbTfmSg4iiB2XUJgdw7ndvh_6pKV1PrcTz9-nd1QLSY-YrpJCo1e7vblfsXZkTW3lV6OVXCWBd9YmSaur9NEfa8t5vQq1utPOojc5aBsLdkgIk8xdEPxe-OeXwmqu3eExRndUXRtBCijEmCd8Z7plYNss1Bj7us7V-ECsgD9lmDcM9zhtyul_G5WqAP1kjYiHHyYq9TzQef_tWJjsZPrGQBNiWQeuYNqS4D-Rtu-2wcswsz8bKUtG-gFVY0-bwVYLsU3Rmeably-PVanq9Q2RvzViUUG0RqWbftPx4ANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1c7b7a76.mp4?token=QKcNukff4ff0387WWTOTmyZTL1dFQnbhWH7fYnCNPxGW7nbTfmSg4iiB2XUJgdw7ndvh_6pKV1PrcTz9-nd1QLSY-YrpJCo1e7vblfsXZkTW3lV6OVXCWBd9YmSaur9NEfa8t5vQq1utPOojc5aBsLdkgIk8xdEPxe-OeXwmqu3eExRndUXRtBCijEmCd8Z7plYNss1Bj7us7V-ECsgD9lmDcM9zhtyul_G5WqAP1kjYiHHyYq9TzQef_tWJjsZPrGQBNiWQeuYNqS4D-Rtu-2wcswsz8bKUtG-gFVY0-bwVYLsU3Rmeably-PVanq9Q2RvzViUUG0RqWbftPx4ANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم حضرت عباس(ع) در
آستانه حلول ماه محرم
@Fars_plus</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442060" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
بستنی فروشی که مدافع اصلی تیم ملی فوتبال شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442059" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh2mgjbDhwWOA55WEJPq_zzJQ0GrzC9EvTi1HDXDt8qbqQZYCC3g2l26B9aaqJB5uEE6p2O2hHacpGPe9o0NiKMuv5nMKEFvi1tZu7kSoWBq_6Nl_GRTI7ciDFkdfVDmnKLl6nRiu_BCc75GGDLjtNNb2PUxRujfGUgXNhrUbqIVRDtUYrnUYZjpTCfGqu1m83dweT8hHLfSsS-N3CEIetXYzo0jlSXXNhsmOil2noZbm2MIzT2zgzmJ37MM78stxlQseAiicw2QqijuZh7JNydtXiyoPDEC1UsUFXKU9X7Cc6vMKpB4BfHx6Z3UjE2I6xq7znozZcqjo928X2XUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
ادعای شبکهٔ ۱۲ رژیم صهیونیستی: هدف حمله به ضاحیه فرمانده واحد ارتباطات حزب‌الله بود.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442058" target="_blank">📅 17:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndf-As8iAg5WKVtgy7OKDNNSByE8CJPn9_JBePrd4Rq_qS_GbhcwpFSW01MuuyXbeeNiNya3jW-QkBYfb4X4lFBqtTj522y9puOxboJUcR7qFlFKcYrGblnfCmj35Ex4OXyS9dXNtoPb6kPg8jRrERr5y0fxPp0NlNYInD8t9nHIWQEFjK3ECtc3iqyON4JvD-ZfrpBzv5biG9awwHkdfmUGcPiVKPpRmzArCfJ2Ip3D8mW5EMUNWdRfDeP_tT_cGAnjodhIV2roXd2vbKa5oXiCLMk8RtNHRpv4D1Pb0yhU_6ZngJezDFh9-HBV-QY9ifDBRDFI26Jms8fQ3EaJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج شمش طلا سه‌شنبه برگزار می‌شود
🔹
مرکز مبادلۀ ایران اعلام کرد صدوپنجاهمین حراج شمش طلا سه‌شنبه ۲۶ خرداد از ساعت ۱۴ تا ۱۷ برگزار خواهد شد.
🔹
قیمت پایه شمش‌ها در روز حراج اعلام می‌شود و معاملات به‌صورت حضوری و نقدی انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442057" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df5L25xlKwm5vNazPUDjMW04NanvbYMGuSKDitwoUnQokI9xGtk_QYs_fDse3zoiP5uS8BMhfPuHgFSn3v0yuzxsC6lIN5LWIaaSIUox4IVC_l5sC6LX2MIpj9_d3DdR_tVYT4PQnACH0F3qbVDuk6P1rpG4uUZ-g4TygIHqAsMofgI9Df5PBXamfKEJoRvqQskQvrMvIecnuqDyHJTukzXxou8pwSMkumwbezntAJSOguuqbRXDO1nuQEdHhNGNJT5wjj2CJRmwHG0IywXZThutbTSrRtGhB7qFfWozTMT-qZ08Ctq8PnzL9OfItqPfvIaUa0jsqJ6W2Z-wGMmF2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در بندرعباس
🔹
سپاه هرمزگان: روز دوشنبه ۲۵ خرداد، عملیات انهدام مهمات عمل‌نکرده در بندرعباس از ساعت ۸ صبح تا حوالی عصر انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442055" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌‌ آمار اولیهٔ دفاع مدنی لبنان از حمله به ضاحیه: ۳ نفر شهید و ۶ نفر دیگر زخمی شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/442054" target="_blank">📅 16:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پلیس: فریب فروشندگان سؤالات سمپاد را نخورید
🔹
رئیس پلیس فتا با هشدار به دانش‌آموزان و خانواده‌ها اعلام کرد هرگونه ادعا دربارۀ فروش سؤالات یا کلید آزمون سمپاد، کلاهبرداری و فریبکاری است.
🔹
کلاهبرداران مبالغی دریافت می‌کنند اما در نهایت یا هیچ سؤالی ارسال نمی‌کنند یا سؤالات سال‌های گذشته را در اختیار خریداران قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/442053" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwh6gz3WBXUEC9wHRu7yf_URU2X9yJDXp5GGSydgyOttaBdOFxL0nS0ZkNSlIctDuwVm_L-XBSPDES4Fc0K3ZldzRwyBzTIlJWbg9k7Jrt4vLy2h5p5HpnQiBH-FRQ6Acsxw65oM0u1hK2I2b_cVNyqw4X3cgmRmjYeVBRHa_ja7_PcxlN9CcZjWCEWuXX23_rMuASt8vUW1uD93MFGmX-fFKlDsP2oqoMCFNKE3vOWbKgEbXtxkjLpD9oQoqiqfsRi-Dtr4Ny8Oom6blloWkNm76tJjIYLccdnL7x-oTEUNYn-sxRnYyvZ_b7-FVnj70psPpOpVy1SbB2Npswil_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات وام جدید بازنشستگان تأمین‌اجتماعی
🔹
مدیرعامل تأمین‌اجتماعی از آغاز ثبت‌نام وام قرض‌الحسنۀ ۶۰ میلیون تومانی بازنشستگان و مستمری‌بگیران از تیرماه خبر داد.
🔹
حدود ۳۴۰ هزار نفر مشمول دریافت این تسهیلات خواهند شد و بازپرداخت آن با کارمزد ۴ درصد و اقساط ۲۴ ماهه از محل حقوق بازنشستگان انجام می‌شود.
🔹
ثبت‌نام متقاضیان از طریق کانون‌های بازنشستگی استان‌ها و شهرها انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442052" target="_blank">📅 16:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
خبرنگار آکسیوس و شبکهٔ ۱۲ رژیم صهیونیستی: اسرائیل پیش‌از حمله به بیروت، به آمریکا اطلاع داد. @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/442051" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌ ‌
🔴
قالیباف خطاب به آمریکا: با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/442050" target="_blank">📅 16:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
قالیباف: تجاوز صهیونیست‌ها به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را.  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/442049" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
قالیباف: تجاوز صهیونیست‌ها به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/442048" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca63c77fc3.mp4?token=I7bYIjSDZSjYbgs7ypvD68cpHsXmnWY5dGBT5cBT8bHK4LxoTT35_GMMassBz0H26LKcR1egWcFJLkW3G7mJVHDa7QacM1NXoVGmfTXtP3Q55fO3W8V_narywf3Y1ejXJwxE07GghBsqZh6IiJMIMihgWFTXxsy9NEMkLp5zw98YhgB1V4UIHsdgwkwsrXGGWMpX3m7Zx5PnW5GpIb2-IwH1GT0-tRPSROSkeZIXZl2ZrWrXkJC7OcpgPZqjPupbipVkEiYmezj8DCXMmQGhffFqqyvODGmt31NjfZYi3BnrhzGV54t3LRo8w0YXxf9ETw-WpWh1LKgUsisyj5RdHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca63c77fc3.mp4?token=I7bYIjSDZSjYbgs7ypvD68cpHsXmnWY5dGBT5cBT8bHK4LxoTT35_GMMassBz0H26LKcR1egWcFJLkW3G7mJVHDa7QacM1NXoVGmfTXtP3Q55fO3W8V_narywf3Y1ejXJwxE07GghBsqZh6IiJMIMihgWFTXxsy9NEMkLp5zw98YhgB1V4UIHsdgwkwsrXGGWMpX3m7Zx5PnW5GpIb2-IwH1GT0-tRPSROSkeZIXZl2ZrWrXkJC7OcpgPZqjPupbipVkEiYmezj8DCXMmQGhffFqqyvODGmt31NjfZYi3BnrhzGV54t3LRo8w0YXxf9ETw-WpWh1LKgUsisyj5RdHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه سقوط هواپیمای نظامی هند
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442047" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX8v4vPAvZVT0pOpX-QvMTwGOk4a_cRnIw0ZITzzE6SDR52zysuntL3xezI-NXHezpUh3emBOeJYU7BlRl63e-jk3GM7iXRBonWz973_hSqX_y8gGqFtft9eFqf5ca69shU-RpnSrCdMWOn8N2rZMkIAY8G3uhHUCU1Drlyt9rxaROR6evc_4kBl0c_yuBQ4nCgljZsvUFXxzlQZOcke8wcrNUBJcgdnjUWxzZ3Y8wL_2_VfAvB9Ga4ygSfi-RA8oU4O7eN3GEcjZCw-B4Rl1y1FfKgh3JxGawz9JLv2GIrzNUNQHBP0zLO7LTsqMzzh81idV4q4_MVj5diIpJJw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروی تهران به بیمارستان‌ها متصل می‌شود
🔹
مدیرعامل متروی تهران از اجرای طرح اتصال خطوط مترو به مراکز درمانی خبر داد و گفت نخستین پروژه، اتصال خط ۷ مترو به مجتمع بیمارستانی امام خمینی(ره) است و احتمالا این مسیر تا پایان سال به بهره‌برداری برسد.
🔹
این اقدام می‌تواند در شرایط بحرانی مانند زلزله، حوادث گسترده یا ترافیک سنگین، امدادرسانی را تسریع کند.
عکس: شایان محرابی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/442046" target="_blank">📅 15:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
تصاویر منتشرشده توسط ارتش رژیم صهیونیستی از لحظهٔ حمله به ضاحیهٔ بیروت  @Farsna - Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/442045" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81128e890.mp4?token=Cp7Pzn20cryETvf_JvwWf8ivMzWVFgx6Y3nLleJ52QMK7Phm6hiVuAXQuoaWpotyevgT5tqHNnMgp7sx7FrOUzQL1R2X23XOCoEqwFj4KSIP9ouA1hRC2jdNQaMOli8ZiuG-q6t6-sFB4AWGgJcHr79ovDH_-6iOoc-Omg-DjjExFpWpt8RBPB6t2vBP_yMAq7NpcnH_8ltdThsIFAl0qutCOHHUaWi0jfFz5TnDn0SGOuzlCGkntGzGdbgpAxo3l5vCjq6jCmxAZ66RV6vRkohL2ut7U8Yq5D92J_PBGnjfp2WHSgtijqBK3peTHq07Mhb41Y86WbAhVVEYuOBd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81128e890.mp4?token=Cp7Pzn20cryETvf_JvwWf8ivMzWVFgx6Y3nLleJ52QMK7Phm6hiVuAXQuoaWpotyevgT5tqHNnMgp7sx7FrOUzQL1R2X23XOCoEqwFj4KSIP9ouA1hRC2jdNQaMOli8ZiuG-q6t6-sFB4AWGgJcHr79ovDH_-6iOoc-Omg-DjjExFpWpt8RBPB6t2vBP_yMAq7NpcnH_8ltdThsIFAl0qutCOHHUaWi0jfFz5TnDn0SGOuzlCGkntGzGdbgpAxo3l5vCjq6jCmxAZ66RV6vRkohL2ut7U8Yq5D92J_PBGnjfp2WHSgtijqBK3peTHq07Mhb41Y86WbAhVVEYuOBd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«در همسایگی مرگ» زندگی کردند…
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/442044" target="_blank">📅 15:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44a4baefb.mp4?token=W5w2ihAoO0XhmIsi9km5kpsWSXQiYNz-vcvLPQKvXruCHkAh5gjvo_rOQiqIQnd0RdG3otSfGb7VXMnhJGiZ7gkMJQrRzUABWjsJCWYWgaXsMWXeNT_wlDkuF7yhbgCcl5lyDZni-4tY7kmRaTWlVietuu4KTB16DdAwXSbPgK23ZVloBfO8QWx1UpidyuacT-ffbMstpvBjxFsHUYWB87152IUPhmR3BBwD4nmQJZSkbl3OarfB9ZpVxa1pjgU_Pjcm0uuKmOpUdr37fEEIDi4XN6UCG5ipIjE_OG73IAgd7Pfdjhgkj6pqgqzat3oBxjVB2wdpVPr1QKULs6FTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44a4baefb.mp4?token=W5w2ihAoO0XhmIsi9km5kpsWSXQiYNz-vcvLPQKvXruCHkAh5gjvo_rOQiqIQnd0RdG3otSfGb7VXMnhJGiZ7gkMJQrRzUABWjsJCWYWgaXsMWXeNT_wlDkuF7yhbgCcl5lyDZni-4tY7kmRaTWlVietuu4KTB16DdAwXSbPgK23ZVloBfO8QWx1UpidyuacT-ffbMstpvBjxFsHUYWB87152IUPhmR3BBwD4nmQJZSkbl3OarfB9ZpVxa1pjgU_Pjcm0uuKmOpUdr37fEEIDi4XN6UCG5ipIjE_OG73IAgd7Pfdjhgkj6pqgqzat3oBxjVB2wdpVPr1QKULs6FTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
🔹
وزارت اطلاعات: یک هستهٔ ۴ نفرهٔ گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکهٔ اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442043" target="_blank">📅 15:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442036">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BupEmaAK0jbLjuhjmQEkgNlfrN8kAQJfCL8HCYJciLRFcaqUMrUXh4pmWPkF4C3fObPf3Oc4b7UfuQY6X01E6cZwF26B1gltRm4DTbtxENJtmnlIhy-SmLYolyjzlj3hE7upMLXU0de3Vg6dOafalyOw5hYftQiauv8mtP31pHyFHAjDV2_SvoKpuLxuGnxmMSWLlQQJ7bvRWq1-BCWZlpsG6Hn6SsielcbtIFxFsrnw4BfbNGVwPBiYJOefGun0ZZu15Jy_1Zmiy5DhnsbsrJfgaG2n2WIC7cLsGsFFiyvh3wZkIcgR64-EBuQge0RVAkBxURFxlSTraAyX7MVBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZci0aLMVDxWRbReQp7A9O2tYJHfd6PCcU2ALIsLNoNPwL8i6hW0zurlxfgOCMuQSmIrV690vnHG1YeyCcjbThY_YrEXNCnN4Amy20svsg08swbn3HVh1CyuPtFvVJmNC9WmsA-pNkA9oWZD4iacDMseUzTIAW2VyKxpX7B7V8-bIVvwVMw8D-9ogHytUDGv5J7b-Yleec2MYwB-NWEeCVHtYhmVP7bdl-2BYdbqYzzxh26yEn_06S4WdmzhyU-xjU7ZCGEO1_KnlFDpIwV_1RR_S9Iho-Bi_oWDnQm-d9kLkNY4ozUmFYZ0QMBhT-9tNrqejZTOIt84luRrcHda0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1ZrFOELo_k91nAi0JFVywAtO8TCGtTuSxqY8YvYA6adVntPzkHPdeSjsgSKJLfExcfyadZ06o-ytyYdWlI3C2zHnojQuM3QU-HwvHhzUik9uABZ3L_Bq1KfYMQI0sfeZK4qMqe4160RahxbCTibHgjxGApTH64U8jBms9vGHdvtUc0lM6O5QL-4WU7naOcIcPC2e8_196FOU-FxB2pIVLMja4XnjzsN47QbN7h_cAcsS9lN9DvF0B-dPJv3oHtqFpcObhPX7Oyd-VkqcUrnqus207EbEuHmoAYxO3fhF2AKBmxBILkhvX5_478gZ7ygOcRed_Z5T7Ovd4_CxUy1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YblrHCceByMEGMT3iFQJYlBPCU7d1SML-uhy5OQ1H-DzDQXulihbNiuGDeG-bi1wZbFou1dCLtxhf_FTMJ5bkY_FpdPGMdtY6AV70DQzSKIWp2V3tkFZh7RfZqOZY0oNK-xruP6l6z7LdbvnSCPbJ2OeYp4YdhMMe9VlkQKIYlP7AN-GzvDmjy7mePovfHR0n6YVeIIOt5jLVnpiMpL3VPF9Lhb3a-X80FcEkP34npcLIZQ9dOMqpf1euOd7RgypCL1ugSRtozoLRGZl0b9I49ZkRrKZHj1P3XFu2Db02Qrwg9X4h1iMe5u0ZGTuOu_y3wWJ_cJIHIldJDDZ0p1WAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agQD-KMHFZ2Xt45WKBuSeFvIZnVhZRPJWGwg_NMnevH9IGRkgC02_9_EcLMaEbLU8cAsxJbhsuTfjs4uEGK3wBeaBgcwDLHP6b0dWHlNdpwOkS056kMGklzIBpZI6LOp4gxDrZT-GbkNULGUDc4seZT6FR4cljKRMWRSeelMZyAFpjW617QR1b8p2GLhW4tR0dYZez1hxiu4LYZkFqOmTS6DsFn5heYpf802dmP_JZ3W_vYZbRQmSR5-Yrx1DN8uGtUdAjZy8pl8Yi6IHOvSs37DsSlHTKrN8KVA7HEetdnnZncZXYGXZ18H6kCWANo271isuCgQcxtNf223NipILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keLa-vg8V1MdQrwba6-lxgWZr2JeEm-gmJ0eipBhgTOL8CqGA1MzMODkZwt5MsE3zUoniXrzzBnmKIaNP-5aoJxGNMF0wMzGPqow3dDGdrKUu6BYI89lMhHolMhS-RuHg-ExO1SeTIhITol1tdARnYvf958WQ2BD7_ycrUffgaVkxOcmTvlbU3FeZiSsHlexMKzPJBO8JYdFJv_v7mCnTmvLHcdvKDWXZGAnArF0MTvaT1ElnSJ7FJdD9SIu1eu2HSsZ6PtDIeVFcaXxmEQrBv9zOysc93kEFcMWfzj5CSBcpw2W-VqmtfEt-zvhFAJ5JVzLWCvGRwsJWf0_Si4MVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gOUGXcirkxpmOQO82U85FKF2y-1INe7koNq_cI5K9Ora2J1JxAoLyb81oyZ_1rEj6dNweC7VXU0xNtmc-J1U8DLP-75m-C6yiPUa66qOcFfiruJAdb_L54zXA-GVXpPRmMluppgw0t6mvHBWQzC1PXLcm2gsCae76TdAzwapaFL_eB1nF_Eo3RCnOesH6hYq4spa15peHNkBlgXJY8C7cBeENW1a3ZK5EfieFNI3QsF6if4N2d9vCHhxhiYq1JouApzmR1j8OQ9o67HEu0_-pbHjxlXQuS8w4_ACNTzlPyuIUb8NBwa9qFAUEsEJzn_WCq7rJfHbO_qCEFKCLjhREQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز جهانی انتقال خون
عکس‌:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/442036" target="_blank">📅 15:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442035">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ-R092lUkTXvQ0UpbKIYlpib895Rbtkh9wkMtkYYGSWSfd5JPj5pvcQhIQbLs6TtyhJxnmONkkFdRsjvyuFhxPJGwuUichw8j1ygFmUiRSKb0REiAZFxtoI_xwPLtnIIcmki7_iJBEQu9KX_MA426SFkP6Jr2N1kVEURE1mCKKyPu6P3QPUdQFUxeEqx7Enpx13yPlxIHarTgdlZGrF9XRVDWMv53U-yWjhzgtKrEHMYKb5YA8M_3jHIEZ5JeCjIDkpR0zyeDF2Qy1jvbenR3WQ0ZpJ9_aHgSXzY0KF-IKaTpca9ryNphCWnvT6xLD_eAXE7LvCp63ZQgkhj0ppAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۶۵ سلاح جنگی و شکاری در مرزهای غرب و شمال‌غرب کشور
🔹
فرمانده مرزبانی فراجا: درپی عملیات‌های هدفمند، ۵۵ سلاح جنگی و ۱۰ سلاح شکاری به‌همراه مقادیر قابل‌توجهی مهمات از قاچاقچیان در مرزهای غرب و شمال‌غرب کشور کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442035" target="_blank">📅 15:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442034">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
المیادین به نقل از رسانه‌های اسرائیلی از فعال شدن سامانه‌های پدافند هوایی در کریات شمونه بدون به صدا درآمدن آژیرهای خطر خبر داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442034" target="_blank">📅 15:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442033">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxgL21GIEe4faXVX6bOkt8aFOXuaTaqWrcKgbXt1f7HJ0ZECr2WrAA1Qrhws-cx-E7qb5lkfIX1lwSdMgSJv6dmNJSMbh94e7ZjAaA_SE5r9wLTQOWxvrDLs9AphSzjyeB8QTLO88E9Ax2wxNJyWCSzm64E_Z1PVqSdzAt7DyAaXqT6Bo7xM0VXdUPXb2kje50hwEizB-20puWZLzraFDyzjOyd-n6_TeSheJVEFfq7VX69tqDtKtkTBiYkOYYbPEl7Eonqwpk2clC6Er9uQu0thj6d2EmlY9D9lDB3_tSRE6-V6tb693EyrK9OazHLWcPk1pAU3Qo9fmXzN_iBolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷۰۰ تن سیمان احتکار شده در یزد
🔹
فرمانده انتظامی استان یزد: ۷۰۰ تن سیمان احتکار شده در یزد کشف و دراین‌خصوص پرونده تشکیل و به همراه یک متهم تحویل اداره تعزیرات حکومتی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442033" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442032">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2Z-wbh7Ssu0DU4AFjPsErOOmanYWvBFc_M4c5NNIlhi_AFhLHSotO4OLzYW4NgLY0KvmDdA6LT4uNytGcYLvnL8YG5WWT80F2qEXuO443NnBHoplLh2d85_DfRYmMsVlBg_MGWMzDV4waw2j01mDJRkOxctN_PmR4aMATvzG0vNDZFUiuxqaRZq0ItbEfzJmF1wZibAVUzJod-sItee-PhabwuF6ZIh98MDiO9vjGDx5a295efFWpdWrCFaHf83tKhIBY_mmFSWUgdGyMG5dI-WtkDg-1zAJaaac1WrmXTZ8-F2p9HlwOGA1vs7DMUWcpjlDaAPOsBARQMv9tJvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت تولید گاز فاز ۱۱ پارس جنوبی از ۲۶ میلیون مترمکعب گذشت
🔹
شرکت نفت و گاز پارس: با ورود یازدهمین حلقه چاه موقعیت SPD11B فاز ۱۱ پارس جنوبی به مدار، ظرفیت تولید گاز غنی این فاز به بیش از ۲۶ میلیون مترمکعب در روز افزایش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442032" target="_blank">📅 15:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442031">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29b8cc220a.mp4?token=P8HvZ0a5q79nYd2CR4cGywXaOAZM1-st3u2uvM-xDhQBOAP3X4Tgmm9-tvqLUoENgJX2IPI-8LQMuk1tvJ9DEO5EokX6dfsBrC3uYr-KWF3vguljimljYlwXfX38u4sRnnoiNjudKrQnrjun1ZZonkX0yaC_qaovhL5dsG6ARbxrh1_Rg8pwNg5oC7qJ2vc91wS62NMak4GfDFwGcUCnZ1GkRRGsrey44lNYUjL0SQ0YAdFoYSZOK85LAtuCrg5TAtNk2LYHnz2V7s4qFBSNidTIcNZwKwLSFSDfXcOEfCexAdHARFsEyiLTZoiTxPub7LluLMMscD8MlT23XK-ieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29b8cc220a.mp4?token=P8HvZ0a5q79nYd2CR4cGywXaOAZM1-st3u2uvM-xDhQBOAP3X4Tgmm9-tvqLUoENgJX2IPI-8LQMuk1tvJ9DEO5EokX6dfsBrC3uYr-KWF3vguljimljYlwXfX38u4sRnnoiNjudKrQnrjun1ZZonkX0yaC_qaovhL5dsG6ARbxrh1_Rg8pwNg5oC7qJ2vc91wS62NMak4GfDFwGcUCnZ1GkRRGsrey44lNYUjL0SQ0YAdFoYSZOK85LAtuCrg5TAtNk2LYHnz2V7s4qFBSNidTIcNZwKwLSFSDfXcOEfCexAdHARFsEyiLTZoiTxPub7LluLMMscD8MlT23XK-ieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شهدای هوافضا که برای اولین‌بار می‌بینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/442031" target="_blank">📅 15:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442030">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMmzgMjRFm6ONh75dAEWSodZUYNh8dVA2YaMEYXj-yrJk7AK04nq0pCIje9ZTY-2_ChYuf6AMfWRd4FutIwlS3K7KxAVg6-213KWi-EHhiObQAEc-VXkr3hUd83uyxrEgtVEjARcHAQT0Rzy1Sss_SOGPkcgSJT1ViFBrCQEtZFNvZ9WTP2oEh1IQLNiWyCjCzIfAoANoA6WkuH6kskbjLv5L-3QADf9vFIDLDgfDQ0EYKHBi3iQb_bcgB-D1ALFiHHcAhC_Hj6eb5hZ8SJi_pnFvicwg74syefLGFLSHGUvHS5Wf7HVSnwwB1Twb4NWKw5xsem-37toBBYieilpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای قوه‌قضاییه به ماجرای وام ازدواج باز شد
🔹
رئیس کمیسیون حمایت از خانواده مجلس: برخی از بانک‌ها سال گذشته کمتر از ۵۰ درصد سهمیۀ وام ازدواج و فرزندآوری خود را پرداخت کرده‌اند و سازمان بازرسی تعدادی از این بانک‌ها را به قوه‌قضاییه معرفی کرده‌است.
🔗
شرح کامل…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/442030" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442029">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e288b78.mp4?token=n1VQp-pt_0IB5Y8ALskZGnMXNb04yIhB35hLusvVimtLCSYsOHvQd1fxA4j6MDWffn3BoXA2tbbT7AH6prtcAqy-SG1H6yQMn221DrrrojapAaR6oJboqqd-BMazR2mJ59d73WG4DYfKZUoYEJiYNshhuR4688X4UBv1Sbk_2NTwFFKCZ-PnhQuBoM8xJhWXH3qIDWHSL-fMmgZni2Z9YQxzRS6tf-DqRbjanXD028GuNoIBQ_2Kv7lD1nqUEMEE8oAHdQzkpb2kyp8D0TNR-NvPMQy7o1PlnpXhVxlK5JhkrXxmNOQW9jl8ZR6dlQEfRNy7Y3iofGm0FlkAMNhiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e288b78.mp4?token=n1VQp-pt_0IB5Y8ALskZGnMXNb04yIhB35hLusvVimtLCSYsOHvQd1fxA4j6MDWffn3BoXA2tbbT7AH6prtcAqy-SG1H6yQMn221DrrrojapAaR6oJboqqd-BMazR2mJ59d73WG4DYfKZUoYEJiYNshhuR4688X4UBv1Sbk_2NTwFFKCZ-PnhQuBoM8xJhWXH3qIDWHSL-fMmgZni2Z9YQxzRS6tf-DqRbjanXD028GuNoIBQ_2Kv7lD1nqUEMEE8oAHdQzkpb2kyp8D0TNR-NvPMQy7o1PlnpXhVxlK5JhkrXxmNOQW9jl8ZR6dlQEfRNy7Y3iofGm0FlkAMNhiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگۀ هرمز تا اطلاع بعدی بسته است
🔹
نهاد مدیریت آبراه خلیج فارس: تنگهٔ هرمز تا اطلاع ثانوی بسته خواهد بود. از متقاضیانی که مجوز عبور دریافت کرده‌اند تقاضا می‌شود صبور باشند و منتظر راهنمایی‌های آتی بمانند. @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/442029" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442028">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClRVKm1W0L_LSfuHGeYqI1eSz1KcsMZe8Vv4_wd86kdkhZz3tLy3k6d1-j7kFTUJpNnaLWIrqkiFfybHn_BM4mxdUxr8qRchnL1O6Fulq50CIgN9v8v6-k1kaMgStpjeIKiWXxMkSsfwGRKaIJZhneecPU51-48Sou6BNn2-u6i07Xls82l2uRpz2nwsBsV87ccdMn_svyjoaVeqI9iKjkSND14RDD5ba-KKrTU8KsUWtaQXRGm1jCDpHhykCi9HpxU43mekz25SfidpJTOBvRj0kxECPv1zZWlMHbypvIGdcOLMGxXNty4z-OjkHW6urrLpCHBe40tzlIPS3Rm2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مشتری گرامی
🔵
با سلام و احترام
🔹
حفظ کیفیت خدمات و امنیت تراکنش‌های شما اولویت اصلی ماست.
🔹
در پی بروز اختلال در برخی از زیرساخت‌های یکپارچه مشترک شبکه بانکی، به استحضار می‌رساند؛
هم‌اکنون سپهرکارت شما به طور کامل در تمامی درگاه‌های پرداخت شامل خودپردازها, دستگاه‌های کارتخوان(POS)، شبکه شتاب و سایر مجاری پرداخت قابل استفاده است.
🔵
با تشکر از صبوری و اعتماد شما
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442028" target="_blank">📅 14:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442027">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUTOF0Qj43vdswdbzIDCLoKlKUAt3Gd8HVIZq_Hvt0PXDvfGew9nDZ8sePzTgQDcpeLPq4uGwdnp8puAXsTf8umMVUwt2R1WmMuZbiV8oOlkcrNBx2kMdezlviJX6YVmRmDME-ybY5Zy3M-cQhZuB56D_rE7w6zkd4a8k0GTamj9QhD15if8XeuYynuksPxho2JaMXPKx-9VudaaWKO3uqWg-o50tvglzlzoFgIKf5D9UJEY749271OoWvZgTOt9gqMYaW3YrUw8HT8IiByqwPPTlQoGCDw5kWZzDtCJDcbjzO7sAIrw3wkm-iVsiXe7qrV6BQXBq74NBMvkzjnb4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی داغ‌تر از همیشه در پارک آبی اُپارک!
🌊
⚽
گردونه شانس ویژه جام جهانی فعال شد
جایزه بزرگ: PS5
🎮
کارت اشتراک سالیانه اُپارک
🏆
کدهای تخفیف ویژه
🎁
فقط کافیه وارد سایت بشی و گردونه رو بچرخونی.
شاید جایزه بزرگ همین الان منتظر تو باشه...
شانس خودتو امتحان کن
👇
ورود به گردانه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442027" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442026">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442026" target="_blank">📅 14:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155131f3a6.mp4?token=rfAk5kEx0s6v7YSuRhEvfF6_b8aach_ekSEVgdDmBMNz_3MQSp8zlK8WdfPNKacvoSwXNgr8N0Rq02zk-YYlY2XtpWqGyhJ2d5YUcW_2EsFqx4Cfti4DkRbNR5m5XLyfPHlUAeA8Me4vgCW63URbKV4RMLl5_IFJaWd4tYsP9SRjlRwRlt7mPF2Csaz5o66w96Z3md_4y3fKb5hpVmrqyxJtl-dTZLQRgU7mA3OeVz9jnuYwKazVgy0XsrWldIHZ-EidApdWqLkb_KqL7aU9Hs3BdH2zTStpXeNT7S_66AWTrQ2_S1idQQizSyo4wGAAUWlzCORM46IV2jDrXyIoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155131f3a6.mp4?token=rfAk5kEx0s6v7YSuRhEvfF6_b8aach_ekSEVgdDmBMNz_3MQSp8zlK8WdfPNKacvoSwXNgr8N0Rq02zk-YYlY2XtpWqGyhJ2d5YUcW_2EsFqx4Cfti4DkRbNR5m5XLyfPHlUAeA8Me4vgCW63URbKV4RMLl5_IFJaWd4tYsP9SRjlRwRlt7mPF2Csaz5o66w96Z3md_4y3fKb5hpVmrqyxJtl-dTZLQRgU7mA3OeVz9jnuYwKazVgy0XsrWldIHZ-EidApdWqLkb_KqL7aU9Hs3BdH2zTStpXeNT7S_66AWTrQ2_S1idQQizSyo4wGAAUWlzCORM46IV2jDrXyIoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
المیادین: هدف حمله در ضاحیه یک ساختمان ۵ طبقه بوده و تلفاتی هم داشته است.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442025" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facf30ec9a.mp4?token=v27IjljHV_47wN5z3YJH2FZ1F8rTzKk-AK1N0-EI2BvR7QXTB06ynCXCD0hHrrvl0Bd9uvokewuF4ccHB1hg8KNmZkBIPuehaRLxVjoUBkzebiGzBbKoeYagk72-SMtlECblDXdxjbp5bwY2nyxPGg6HI41V1Z82vdbSJGJYteOXY7Nr4VDv7ql7mup2RQBzIAxvr7KOEA7mOtgp6oV5JTJrczHVLWdUnVgJtnzKGNJOlg1GdR0kclPCbSICheHLUH4nt02XdTLx2kMWYLgxG8A6boNszyuxs2FFLmBtpCon9eoDh3IVL-I-JDJsuONjB8-060Jy4w93ZFUik__QSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facf30ec9a.mp4?token=v27IjljHV_47wN5z3YJH2FZ1F8rTzKk-AK1N0-EI2BvR7QXTB06ynCXCD0hHrrvl0Bd9uvokewuF4ccHB1hg8KNmZkBIPuehaRLxVjoUBkzebiGzBbKoeYagk72-SMtlECblDXdxjbp5bwY2nyxPGg6HI41V1Z82vdbSJGJYteOXY7Nr4VDv7ql7mup2RQBzIAxvr7KOEA7mOtgp6oV5JTJrczHVLWdUnVgJtnzKGNJOlg1GdR0kclPCbSICheHLUH4nt02XdTLx2kMWYLgxG8A6boNszyuxs2FFLmBtpCon9eoDh3IVL-I-JDJsuONjB8-060Jy4w93ZFUik__QSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/442024" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ab3c92192.mp4?token=H3mYGRPOAgq2oEWh_gydtVSoWvhCRiBx3LSYkHrs-_ejivz0uFrOyLqhWQTGKvBsi7V50pCOq-QCaKehtCNJ4RH5tLbxCCHy3ytWytljXG9Fv1hwoOThatiYrDU4mGKrAU1wDZMOdm3CyEZHFXiNkj3tPTAVHFDzCQGFoPvBoO9QdbE8utT9AHmEfVBYYrB-WLLHDrP_zrqWEsMCSnF4a8D59_A-XxaXp-cc1nS70oZAhyuTOs9HSa1Fe6WdS-jdnVC46mpIUXo_WKeFIYq5SfT1h2hFg7ABcJGQW9nv_vvZpMHevHSfMHGRa84clownmvADUO8DmGhVy60GoA84wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ab3c92192.mp4?token=H3mYGRPOAgq2oEWh_gydtVSoWvhCRiBx3LSYkHrs-_ejivz0uFrOyLqhWQTGKvBsi7V50pCOq-QCaKehtCNJ4RH5tLbxCCHy3ytWytljXG9Fv1hwoOThatiYrDU4mGKrAU1wDZMOdm3CyEZHFXiNkj3tPTAVHFDzCQGFoPvBoO9QdbE8utT9AHmEfVBYYrB-WLLHDrP_zrqWEsMCSnF4a8D59_A-XxaXp-cc1nS70oZAhyuTOs9HSa1Fe6WdS-jdnVC46mpIUXo_WKeFIYq5SfT1h2hFg7ABcJGQW9nv_vvZpMHevHSfMHGRa84clownmvADUO8DmGhVy60GoA84wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مشکل خدمات بانک‌های تجارت و صادرات رفع شد
🔹
شرکت ملی انفورماتیک: طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت‌های بانکی بانک‌های تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است. …</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442023" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442022">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_C98kbQL1I_3DPK5LK1trUaxMTltAH-aa5S6nGJ2WldK40P8TftIGMruf7QgbkVkt4TsM8nySJMO45bzAtvDRXFW38vQQ1VX2MaJHG25Bj8PEgvp1EplevHXDX2q7l3Gw3_98aH1BxnIl6ZMbfUOHW996xDlVVa5yp6v7EZlrBJNzndqVa-_QTb_BTQmK37JkkHSxxygw8H5kVdxV63z4xMuDvlW_aTEF664fjR-Fmf16qSIMnIRuH2KBO_6f65Ug8wA2yhVZ0cIZ73R0CG0YnMYv9oKvykRq15qmvqte92d3mqOsGbMxK-30lj46pfOQtq_l_9onktGOwb_K_4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دستخط منتشر نشدهٔ رهبر شهید انقلاب در ابتدای قرآنی که ثواب تلاوت آن را به شهدای جنگ ۱۲ روزه هدیه کردند
🔹
بسم الله الرّحمن الرّحیم
شروع در تلاوت هدیه به ارواح طیبۀ سرداران و دانشمندان شهید در جنگ اخیر و دیگر شهیدان عزیز این واقعه در سحر.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442022" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZWGz0dNdNGX8TNXu6uzfS71WNrXP_lvultvFJg9rQz6PH408lYG8E6cQ9RFx_KNEiUlLyk8qwM5oM2OwcL2kyZFnB7NQZ3WjsCk5bSW3quAFHGwlqda2tlogz8u_MvIlCsI8wwOHxjRKdatWWsh7NjuD5rTVVb6xLy0JXe4vzLAJT_i3psvx-BDOhv4X8W4YSAybp4FuYJ5H2tCqDSDDbc4MoZNTv6V-kJfblEDHiA71esOi2prEoDNeEIYlRPZD-Gu3CgfQ3Ft3tA_AfL-WIC50PyOWTSt9BmWi1OYGlnaPihJvWUgC9SwbNO81puOP0Mbs1S1kiucR-GmDwV4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYCU0GOYoH5XsRVZ9NSyRQV2tzAWUECfvcnrX31w7NszfIkJHtHo5QgZKfhkldIGEOp0joK3YNSHMfN52o8UOX6inRCLTkW29rCmWxx6QGPsrAR910wfPnaO-0c37BbNhPgPhiv2viRD2soEWDMgr3eGgY9Z64TCUVeZF_nEVk7yqWGf4s42cOtLOVOw_VA8c5YE-Qw-9AxAI74LfVDI5mSePZpG15mBB8WXgbFlRCSuQ1sflo0PxWovANTwSOffxkIFkjTOQmo-gj4EljwjjH4s0o6ajIZHdC78xmGy2ihinOzS6cpnbf6DRA9WybbGAiD7tp7DDH2mEh5fASuM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVlR6_VFyUYIQBBKPJi3-1Jf2nZR8GeHhBWT78g-1vNsKcA6oy0LKjnSgWQCLAHjS4fUwuKNz1p3ds-KXT8txkTJd43ki6tK3sLMmaaqAdH_U6RpqACBoq9sT-PUUk1OS7vDNcF3uGWJZ_26aagQULaFTgJHHrUGqAHe1fslexMLt_vXvA9NN68buJIWHNrMWZNwI0EIodDxcvH1IQiATOQqsshxkKpElB6qWHapM6GNBMf3FW3KEhmCs3fzpEAAKuvjPS_GHix2TBXWxJUurwt02dtsEwVS9QWXUZfIKuzGDjd7hu1K3BELMTxfkF8qdOZ00oTYQC9XVEsYkN37hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pt8FNVGWjTVw91ndmbHAYx4-q8QwpBV6qoHpSKaRA6eOaNVCi3uUnk3EaW7mN5fiw-1CR6vA8T0ujdo98zGNTm1cXJqoOZGOhGX8qX4WhoARpR2vdPTr_X-GOeTlp030wNWRi5vk4OnELxVSZsm8xrEDv7w7BptHIkpzCNS28SGBaO_T6K3j88uT2ZVkmgU3QrNEfLYqSZSckCD00h2KwStzuEEAND2DSzY2BF-T3CbnsNbhjFt04fLyESSSSm-tEkVyJG40T7fxAW5T4r7z7nXe8bd_MkaCKBdgRiwY5djn1242VW0EhXG02EgbX-zQXHNT8dnvf_PbIxPAeiEpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKUe4AoPgSIswwBI-FvSmqH7osPyIZdZFKJndU62xQu9lWOAxM9UgXWTN0Hnvx_4D0UrtEkoUWmN4-Gla_Xbe1MppA3jOZr66lECb6sIlehGATLdpodt0vY2iieHGcYVMEbe_hRbEBZKYUzDOLsIjT9rjOVNdFm2MkeHXaoVlR5Q--UlkovR7ZYgAZZDVypCLGKJx1DtFh6_0zthLJQS2I1lcrm9KVNPs61hcOND5_beRm4z2TvfO-ZpNfgAVGgybOfmY8kINvUl5jRhCqXYANnUncXDhVyAK4CMATcnelo61JqqpkFsHZPHMqhvFJyRHVQf5KqZue_R8LaJQ3oUnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حملهٔ رژیم صهیونیستی به ضاحیهٔ بیروت از نمایی دیگر  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/442017" target="_blank">📅 14:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1774b9fe8.mp4?token=QeE5NT6dA-OYmJaWvxbFW9QYa7jcfLuPHaHrqdDy9zwxr_r_fpE0rr2bvEcrUJoxfb597tzfmT6QPVO94Pq9VO7lvr6xoPBAvZSlkTqPCcTXBznbSmoNbfTv04zI4Lq_2ZnYpj8VUXZoOdKkHr2qp-JUz5HwQgd_vqROPVTBs381jzMcj5mKOVRU6ZOh6YdHMKZRBAahlYVWd27kqYwJKL1-5OG3TuFx9wa-FFi8XGYXeuBDrPObanO3yI8JpOMJj3sC9qZGiqJmHAxAxwk6eeXHsQ8PeLR3ti95BvvJtJ1pZNiEIAjJAk9lcovWYXiZ3mNAvDfJCMbvpObsi-T2iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1774b9fe8.mp4?token=QeE5NT6dA-OYmJaWvxbFW9QYa7jcfLuPHaHrqdDy9zwxr_r_fpE0rr2bvEcrUJoxfb597tzfmT6QPVO94Pq9VO7lvr6xoPBAvZSlkTqPCcTXBznbSmoNbfTv04zI4Lq_2ZnYpj8VUXZoOdKkHr2qp-JUz5HwQgd_vqROPVTBs381jzMcj5mKOVRU6ZOh6YdHMKZRBAahlYVWd27kqYwJKL1-5OG3TuFx9wa-FFi8XGYXeuBDrPObanO3yI8JpOMJj3sC9qZGiqJmHAxAxwk6eeXHsQ8PeLR3ti95BvvJtJ1pZNiEIAjJAk9lcovWYXiZ3mNAvDfJCMbvpObsi-T2iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از ضاحیهٔ جنوبی بیروت پس‌از حملهٔ رژیم صهیونیستی  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442016" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e3d13594.mp4?token=Nq2egtaPGeNBuXzjTyIikCyTimGrga48cJQiHBiRdp-9zVB5OywsRoSxYtY4hmntre6uFgqyc0vuss4-nHKAyKzavjnihM5x0940jtdSMfU8c7FgFt24Joqf0V66MTKP1Ev_prNTZmd0NZDd0qgRtutFFuIlwVK9gugPN-Vv_Y7nOjW3rr70fm-b8gyhI1Xtf1rJX0zokwnLeJBRwmHmL6zt4D1txNa3-8lWgVrZN2Yu_di1TKXDP5eSV_3VvEyTdCGfBHQ9rkcJ5HpLLDNFj97V4Xrfvx0l1ZWOceWRAMIqoY5n76qjet3ua6O4KFZEOoR5HdZURe284uArPkP6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e3d13594.mp4?token=Nq2egtaPGeNBuXzjTyIikCyTimGrga48cJQiHBiRdp-9zVB5OywsRoSxYtY4hmntre6uFgqyc0vuss4-nHKAyKzavjnihM5x0940jtdSMfU8c7FgFt24Joqf0V66MTKP1Ev_prNTZmd0NZDd0qgRtutFFuIlwVK9gugPN-Vv_Y7nOjW3rr70fm-b8gyhI1Xtf1rJX0zokwnLeJBRwmHmL6zt4D1txNa3-8lWgVrZN2Yu_di1TKXDP5eSV_3VvEyTdCGfBHQ9rkcJ5HpLLDNFj97V4Xrfvx0l1ZWOceWRAMIqoY5n76qjet3ua6O4KFZEOoR5HdZURe284uArPkP6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیانیهٔ مشترک نتانیاهو و وزیر جنگ رژیم صهیونیستی: ارتش اسرائیل هم‌اکنون در ضاحیهٔ بیروت مناطقی را هدف حمله قرار داده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442015" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUkm1pZoDbCNaZBPpOgW87UOP8avQVvQDPda72Ipj0E13lRHAsh9VVExmlJ6dItdpQO64jAL0X5pxCfWj1vZPS9iTgYRTrp6p6A7sqhWZe-FJnKGVPkYvNrpH_F188i7vNxk6TpLFUY3ImnVmut2NlSmwHeM08NmX3LHPT6WRz4DngFcoivnof36nYfdD6GX-5DfyE52Fn1za5ja7E0hJxiE7wCBTzOMqteEdHmaOAv4BV5qqgPbs2kylEUOTjJs42IVTZr5HHd65bQ5M_e9Swd2Wfp6djzm7sN43TOm2lvgkPmjdk1tWoXqeBCpyHtgxFJynJ3tf9A7cw28r6Tk2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عبری از حملهٔ ارتش رژیم صهیونیستی به ضاحیهٔ جنوبی بیروت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442014" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW_CJK_jYk277CKzbDkszL_Dba7lF1fb3SaIywyf9y9hDO7C2QXsmcprkX-aaF_d-RjB15-gnErXsAWmqNJ9Pq6b-6W5PXkf8Ae6hfsprdR5o6y-y6PgYZ0i9y0FAjsPVBtbUsjP-m_lQBrdtYFqU3IVPuR-3t-n6u4i63Ze4g4WxmPejHUtufkIRdcCEW0IdzOi7cueloZpBrL3YcxLVS0yWxdjl5Hwafu-OGY0-VBa51zgTJZ8jvQGDi4uSztq9inkQN96Axnfui-wcJUgZ7ey1_BRbItdAYxqcsR3Nfze4a57CUZq2P2gzHhWhQ469T_yide8UBWD1MMAJnz4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عبری از حملهٔ ارتش رژیم صهیونیستی به ضاحیهٔ جنوبی بیروت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442013" target="_blank">📅 14:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
🔹
وزارت اطلاعات: یک هستهٔ ۴ نفرهٔ گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکهٔ اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442012" target="_blank">📅 14:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV73Q5aLY-R2uWmOczf943BY92LipZipxiTdYoK4uhM-4D0DCnMfGsr2twxD-pieencA1Po-RYhFT19jHOM7vIOr4rUfu6eZpC82AGS8oPYlXvDHDdQZLyVB83qyNI3WN1BZJeFpWxupynuSFdmCmt8dCNnGc3Lds60DZvWYiD8iW4_avM8xuKzVgV17LBEKdHFR-DS3Ff6voqFnjw6w5pwcu1qc3mZGABQUKTp9cMSmRXL2AKm0QBsEXDZhQqVYoQ_9XwajdtWr-VB0j9P_sIot5QWw52ewCFmwDdBdvx6A7qEn_m_KPdmO4b72COVxLNeGf8JufYHJo0awuq2Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اژه‌ای: دشمن به مخدوش‌کردن وحدت و انسجام ملی چشم دوخته است
🔹
صهیونیست‌های خبیث علناً می‌گویند که منتظر خالی‌شدن خیابان‌ها از ملت مبعوث‌شدهٔ ایران هستند؛ آن‌ها این آرزو را به گور می‌برند.
🔹
وحدت ساحات در ایران اسلامی استمرار خواهد داشت؛ میدان، خیابان، دیپلماسی و رسانه؛ همه و همه در راستای ارتقای همبستگی ملی ما هستند.
🔹
همهٔ‌ مسئولان کشور متفق‌القول‌اند که در برابر دشمن نباید کوتاه آمد؛ در این رابطه هیچ اختلاف‌نظری وجود ندارد.
🔹
در اینکه ما نباید تسلیم تهیدات و فشار‌های دشمن در بخش‌های نظامی، اقتصادی و رسانه‌ای شویم همه یکصدا هستند؛ البته ممکن است در روش‌ها، اختلاف‌نظر باشد، اما در اصل مقاومت تردیدی وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/442011" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLhsQ1oDC73Obi4OoyxGNO7kzsc2eUe745FjLE-LbthlUkbqCmCxnIskP-8rEgGDG_z4YRF5FBW_sQUpl5c0FYH5hIqKID3WYobvo1ef-JewolQCEWNoYv2ZrC7n8zPZoXphNKqnwZgqGS1BgqXD-7hcgdCEOB_Mky_5zKX027huTVUlHPcgX4dJV8qBllorwOxlG2fzPwwKvrm9AH1wDlorsdGscezjeosWrcvbrqgg4Tf444TOq6nfqxG5vr29l0vcGAu5c-72b7Fph-59lLbfPjIhCGk4xlW4THM3iezlErxNHg_N1q31gRhznGsaCAQpNhy1v-OjPjgsCG_7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای ۲ مدیر دولتی غیرقانونی اعلام شد
🔹
طبق نامهٔ حسابرس دیوان محاسبات به صندوق بازنشستگی کشور، تعهد و امضای مدیرعامل‌های «شرکت آتیه صبا» و «صنایع شیر ایران» واجد اشکال قانونی است.
🔸
پیشتر دیوان محاسبات در قالب ۲ نامه به وزیر کار، نسبت به رویهٔ ناصواب انتصاب مدیرعامل‌های این ۲ شرکت اعتراض کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442010" target="_blank">📅 13:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buRbKm85KJiHOhwVwOtfgON-WOkmRkvzXWnKNQHGW4jzY4Vxr4ru3SzwX7-gy8T7hbbjmclpVL5T661jQfUJbb5RKE7RZ2KgIkRxMp2MvaRpXlxJHgO1qMHJrK_2YppRiJm4JOc9DkxLQwCtUdd7XxeKM-6L1eaL_FxrNVU24_QDMT4PKdfx_E8gAlbfsfT56RGIV8IL4Qq4zDzNHlUlRLTiimjkrXZjUgNY_f1UsucayUvdyn7VZ1_t2rY26YXEuv1wU9MikF1q3DlJai5UdAM2S0Urm__CY0nr8FYQ49OVfIId2iHcB7kMOUOPnk8U-1faCBOFxzbrbj3U2TSLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاریخ قطعی برگزاری کنکور مشخص شد
🔹
رئیس سازمان سنجش: کنکور سراسری به‌همراه آزمون پذیرش دانشجومعلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد برگزار خواهد شد
🔹
بیش از یک میلیون و ۸۰ هزار نفر در کنکور سراسری و آزمون پذیرش دانشجومعلم ثبت‌نام کرده‌اند.
🔹
آزمون پذیرش دانش‌آموزان…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442009" target="_blank">📅 13:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442002">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGE9jacaJoLtQMG_jhPStlvWaAHFii61R7S4sgYlbPfwPzDUyukCbbmRqWQ_pC8FMDjssDuXC9CR8MNjH4-xX-YMiLysF0JqMR06oczrVSQDsFHOysY52gKdG3PRA1KuY45qPraZh3pIB3wFOz0i8marlg-3LnQaXH509cgwGpgNXSlFGaw-InwpVDh5c5lNivxd-fnX7st2AdOOMzbSzHVwEEjpTmofwqYJX_VL4oDSxO34SHXirtVwHhQghcVrOitHEMRHIIU1HPBTAWhLdS-c4hclGu-nVDLxUDSTKeOcvNdOhsa3VR1JDfo4JEMIdrUgE2LDswibYBDe-A2zGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEZxvHHceiqvLf_Kg8zzNiCcbfiyWypNMzMpXcXRjrjvCyJxNHb-XUPUOnGyHRsCQjQpQHo6uiYoWMxxK845PIzXA9PjL0BQ-dQvxhgg88YDOAKgBpnn_QiOzZAK8Z3Ro4pVj1N3GUtMNCHmCcRQZTcHlug8j5Am17I6D9KBJUBaYMA5w8DQ3pAcQq2d2USEPKqM-U_wyauk8E3q8Crg6Vw2ESdOEJtb3XHZKAQXB8R47K5tGAG6l189Rvel6KDCFFe-mILOJVq5eCzkK96e58D3oSuFk8ky1fil1bfMS4ilGDnqfy8-zSzdlZroe_ajxk4oBRHx20CBtZ5byFuqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFfdPHTPfJz_x0ATBlYPLEiEiCSuycHcK505f3y8yfFXsQHbgrCFCRpUNF9vOCFgVaZOiBkIqm3_F_JEbePPkJIE7bztO7IpBrK7vveeeGl6F5-HJtq2hcsB6Ksw5-HXAuNiJ7-wtujZCeAPvacH_YEPLgCROgJ_Qa7lDSSjX_dP6mbnRitw1vH6tK9r771GI8uf_8Ux2avPy_VWXlIzc5FnBvJq3OtzbAE6oYY2c7KyPZBT-Yb3wnSb_otvY1fRID2ESSGIDZRVfOL07zO4oTmKXpFTu3xrmXhntbaNQ-Irs0AZ5F6yefINJzfEeFTFHEQsVuRURZt0YVgqvv5nIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-FAB0Jrbg64GURoHXHkTsitJC5nDEaIWFj_Kmi44jNy-cwr7gC6v3J9W-Q-v6aDjrJ58pPYdTk9k-0OqnE5YuqYmomJO8rEKoy_R-IpZtu24AalupLxf3SnG8W6a6zB3QPbsBjUztRwZuBooq4xRYPB9zQh2UxplovXFaYr5-qOU_giHrn_l7sLN8B8pZ4NOGkTgNZ3j8VjzyzyuXxxoE3zwWAfL6kvh8RzBgbFqMCYFikE8sA7IpdSt_mKBY14CtY2m3f-l9FM59lAhVNTZ6v2BfFpliwik2f4oaek2mFghZspjG4r31zzJDN_MGjqVkH-tTvwUjmQ9qA7rs8M5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLE5bSgDYJE3ZlrViJ34g8fmuLrUmQXfWtP6U1w8ZyqonII4DPxJOWIqYGPclsXCshf4-XlM69mMRau1ZC1gL7YAESKXDlW6a-7i5kutCaCGCE2CoXnvI6uWsIargt8GV9luIuC1u9OnUbUp1-weTOEFmjad7XEsLsOpheYSoIe7L1axIUboClnL_uKMt2sAOfGE_rQhz75tILn7DtjNxyPGorrmUnolgpD8BKjl5D-w6qt2wfR1ljh7WOkYqgv-j4KHj5nFsfJ6jeOyZuDSfVgra_qFGBwCotEDU9zxlFc70f5BEGrH-p9m2iV0eHsg1Tm-P_ghnmm3VaukGBPfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8EiJ-t4l6NvqSgZLr7LR8__stg2mYaEBWwr5fKU3069HdRKYeqU6ZJaet9S3FNqxxxiqVJxqebSpejyH13KxQbVH-6q3i7nSWfCva-jzUr_ccIX0qzZVPmDh4tEOblwm1LT_GkuntwwPaxVIgABqdCydiNO3gQxZbI5o78ocDLLNBf2j2Ss0tbE-UpMse1r2napg_5rnKxH0fl_xKIMAuKOm6c6EC8SKe2CEM72Go86NdDqkFQEN9msYL3hBBeDd5KbsOdDNS7nMVpjEZFZBlJULCHhFxHhlqdBIZudzt8b8LlI_GFK6gKKpNlhkHVlA-oERo9SToekcOOp4KRDZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست مجازی مجلس با حضور وزرای آموزش‌وپرورش و علوم برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442002" target="_blank">📅 12:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd-8MAdOPCGu8TN4oe3EOfLqBdtdlkkx6aYnavAh-3mejwLFD5c2NHvRfsRXKl9Ybp8_NabDKEkYdhDvLX53pal2Qygf43vdQO2aE7Woxzq1LvcDrxfdoL1u7DYl01Ox3Z1Va_S_HKmw-4ELMFseBXrZIBEDLz2YJgs2cYD2VExIX4UsSsAunx0ZQuDSMe595geICr89ns1T4jN2hkpBNnExbd5bKmEFEccmyIFW_7huaXHRDNWZYwTSZJVn4cWUZ6KQ95CuUDxE_2MPmwxSYkRs_W5MrmDvD6FlcqMlEBUSXZ58Wulx8WZLF3q1oYRx-oVJQfPYu7mAbvFD9dQk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدیدش از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و مثل روزهای گذشته رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442001" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌ زمان‌بندی امتحانات دانشگاه‌ها تغییر می‌کند
🔹
وزارت علوم: تمامی امتحانات دانشگاه‌ها و مؤسسات آموزش عالی کشور که زمان برگزاری آن‌ها با مراسم وداع و تشییع رهبر شهید انقلاب تداخل داشته باشد، به زمان دیگری موکول خواهد شد.
🔹
برنامۀ زمان‌بندی جدید متعاقباً اعلام…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/442000" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txvOt0poIkEsDXlVzPf-8_LlJgQk_Ly8lOHDkk-BlAawIN_whIAqwRlbEfce6ZMAH4SqE-U4S58xFc7RQ0Eg9AfE6_bjDyhwSsp4dHNYz16_DagI2W_mUZOiUcVkKbvJspSpDDGkCR7ggBADnJiC8EKHnRbPy7hRQHNkqIzm12c1RIOg4GhJ7VOLSFTe8RBUsH4oWd69Bhi6gdHUajddnKhhPzNRHAvWM6Wa7IOq9psAeXozmAdscl7kqFVApP3HCT67MitGBbFh3id3VDZBEShL5KJYfA73QgchrLoe2Mdare_xLsQZWvc1ugNz4f33_GLANIc4qcMrSarYKFmauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGUjekvw0p77mgmIkkdodGNhhaapzaPAdY-sU-H9Mov5N_NcgDLkb3jxbt6f-BT_-mPChKKqdm3JfwuNb0DPzrPX3ySnWEKjq9En7tvu2XfcZZWjx_xT11mxvBqnlZdBiEB8pDMJjF8YLVOZBIdFs6GuhOYW_qREBHZdtx6v_2TY-xj2c6gIfYvMTo-VOcmc9W7bmZjmI4dHgBGrLLt4XJmFasDjceAomMoAz41RsW_e51wOcnvpvT6VmAoWdKg4f_Iw7XjRw7FQqYVD801CCd-3sLa0KmDVvoUO9dea3ZqxRPmtDk8Jn-OhsoNNk0fPR5aZNU5RWuA36xUyc6y48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssNjoOqrxABI_Bv66gxuMNLz1uCNBqkaxLnJ3oMnxOZFJFazTQzbUBe7_h2f3AQZJ4ETGU2dk4oLl9Bu9CMgqhi5wVtZ_gGJRic39XsSYnvykyrqJmZZx-aAA3EvXNKpec1pYMPzWVLXCklQ4HWZ-GpiyhloR5oVlcoH6IGkft6WbzP0x6ZoavKMnLV6ygh-7YzK_Kk5EEGbwHePj4EpDbPAwClGTCmEdwzHakSOOMF5rt5vt_cXQvORIaTpWmtmR5IWusXA94zJhnqBUWuBNTnMlzMkDwmvoV7K9I7MVcYMQJHe2TSYcnLrz4hdhNw8oC_NfBdE46CWITxEie9K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H113zx7EVIU1LS5JL691VeahYHf48e4n9oCQbnkJfc7fhEzaAR253DayKUZU8W-H9Reo_7xEggRilpV664WYs7rBISkhDuSLqzFjq6PZV8DMgF7XeCxWF1EqHCpe7woYurOXCsZuyptiG4OZnRHA9wpkDQOvgo5qqjTsGHpvloG60vI9MTdUEPAgR7NRYWBJfjGdIpeBDseWmkdPPwpHijJBFvqpwUXh3igKdTbHioJJZaq-9oQ-m6L4u03i2yFW0vQwfpe5Aok1I0q66OyDNIj6mnTRZ_6FavNhWle5Zwv28tvC8G9Zpvj1rMPixLWs0wF6hodIl_Jg6ssbSP7NsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7-thi36Y3MBVW0f3lL2926ukyfL8SSKAA9IN9N08xSpVuiXKgPt9_Guo5UK8p4NZqdNTl-kB9FpFWjz5SMwZKFBALJKEaAqy0D0hq6NVYIC3seICmFcRxQ11YYkfyBl3twZSHdZiHFPcl_RVDVadQ7mr1EicmtTDfWkd-7kQJ7XDb_aTtqXkRrnohLy_B3FbW1lA3iWoEePDOzbBh7Uko8jFn9HGKyZrhZD8YEuNtpKdlMtgqcmQejqst660xDkeDK824pO6QmmqjyTYDrhbdeK0tqkHyG6wfzvwozIEpuo7t0wsMuOVsbkRlfuhklRbmDpDF-CCZ-a4LNV16x_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgTJ0ACqfbqw5I5k66xHxmaIo0De9Mai9fD-7iOJcFfxDIagxWksSXTq5B0vHM4Piwjx3NbFrL0f0EVLEB_jsO3AugtBns3dSWDXEyN9_XIKXv6CD3j2yZVNB3D0G5_aRzRuZp3rA4BAbOum04ozs8Nh2z0Wgv6t8qe3VJb7zlTBKfREXvqIw5krBxScfBlqmB-wrnMTEe6cxXv2LW-QrvkeEPOTkzlStTHHInj7HFOC1LOopploDq2f_o38sHusiztqBD0v5nhcSmEAG7K7Ou7C1j0cuMri-yQiJUlqV4UsZjRXxBqqmOB8HD77pt45XtNIb0KyY1Tt419WvIvkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDxJCcV-toH7viiIGhpXcDAWy55VNs74bWiOMn5_yQkMGjxTuJEgZF8656Hhy9dwyQLVoibwO2X_-ku8h7DYJHXzbXO7eF9l637ePnn4mkRyWT5AwG5-gkccWcxueS6v6WXJBfzDtPSgTiK5MpWq9_YaYsGGasHBVXLm2dHCdWo5xfQB-MchhLjvo0hoPlA5Ocb7ntwhkxTSW4q16IFvqS77hUgShF7R2H3apK89ryi5R9a_A4_WWeTmxDKuU3sknfPQFpN9gAqAXy9GhdlCSBKmG1A95xskm-NT9Oa0AOJ78-EczgE_nj6umVZUcBHMdlZSoQt78y_4lKwTpIIZ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ننه میلاد در تکاپوی استقبال از محرم
🔹
بانویی که سال‌هاست در مرز شلمچه با برپایی موکب و مراسم عزاداری، خدمت به زائران و دلدادگان اهل‌بیت(ع) را به‌رسم هر سالهٔ زندگی خود تبدیل کرده است.
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/441993" target="_blank">📅 11:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa4129ee2.mp4?token=WJfAYQf8ct2KJQzYPpQ7m-b50XksDPD9cRR8g0UaR2C8c7ROX-xki6Qz-1KNiEX-rbtZg1AWp-7eyAsS2qiFrBAE9qqUzcGm-VuyzshsnSnL-LRB0hIppJZcZtDZ2WKVy2YntCx3YUdgRJ0m7uih8C1Jt4tA0UdXVqacMg4y3ybeMSu-_nLtFMQvm98g7S6N2ipu5oOHCBcCb46aEvtPr5NVFTMvv0Zrchd84jFgIGrOPNmjW0hnKJIcjOt_uKZ5iAdZg-oHGXNbs3di8VW4pQWfTMThFUahNX9UIDdsjFIEtHoSXTJW5OEKNOb7nGnIksRVOhSEvK0HRbBvm3jGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa4129ee2.mp4?token=WJfAYQf8ct2KJQzYPpQ7m-b50XksDPD9cRR8g0UaR2C8c7ROX-xki6Qz-1KNiEX-rbtZg1AWp-7eyAsS2qiFrBAE9qqUzcGm-VuyzshsnSnL-LRB0hIppJZcZtDZ2WKVy2YntCx3YUdgRJ0m7uih8C1Jt4tA0UdXVqacMg4y3ybeMSu-_nLtFMQvm98g7S6N2ipu5oOHCBcCb46aEvtPr5NVFTMvv0Zrchd84jFgIGrOPNmjW0hnKJIcjOt_uKZ5iAdZg-oHGXNbs3di8VW4pQWfTMThFUahNX9UIDdsjFIEtHoSXTJW5OEKNOb7nGnIksRVOhSEvK0HRbBvm3jGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون خرید و عضو کمیته راهبری پروژه بازسازی و نوسازی نواحی آسیب‌دیده  فولاد مبارکه:
📽
بیش از ۹۲ درصد تجهیزات بازسازی فولاد مبارکه از طریق ساخت داخل تأمین شد
▫️
آرمان امیری، از تأمین بیش از ۹۲ درصد تجهیزات موردنیاز از طریق ساخت داخل خبر داد و گفت: راهبرد بومی‌سازی و همکاری گسترده سازندگان داخلی، نقش تعیین‌کننده‌ای در تسریع بازسازی، حفظ کیفیت تجهیزات و بازگشت سریع واحدهای تولیدی به مدار بهره‌برداری ایفا کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441992" target="_blank">📅 11:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHrjAf_edo8fB_hirN72zUqEB5IXCzKrx8Uh0wM83xLdvjWjc-JurrF2BuBRNQn1Eu-d_83poIq6u_lPXqJXrn_PjUm9y_yRlAivwfYYAhgas40Y0px982GNmuML2bhs8heQB-I-TfQ_WA06ENdGPk5tE5fNXQyBpWyNPnEQnrFTY3GUbDjVu01AJ62jxD7F2y8cL2tPtmdfrAqmQtZ7d5uKHSOcjUGZBg6zeuRdtk0Lhwmwcd28HFU2Pz1czysdee9VpkKEqf33uKTEWukrFrBOh5-N55ublzOmqiv2PhfxYTKW3Z9WLfPCmO6j7oXew214_tfIV4Eo-mviU58pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت بیمه مرکزی با تمدید یک‌ساله مجوز قبولی اتکایی
#بیمه_البرز
بیمه مرکزی جمهوری اسلامی ایران با تمدید یک‌ساله مجوز قبولی اتکایی از داخل شرکت بیمه البرز موافقت کرد. این تمدید بر اساس ضوابط و آیین‌نامه‌های مصوب نهاد ناظر صنعت بیمه صورت گرفته است.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5046</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/441991" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
