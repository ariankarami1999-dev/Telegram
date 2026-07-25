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
<img src="https://cdn4.telesco.pe/file/m_emIiSnpt_QHnG87jIJuXFqHwGWqReF0TRemOPxyGYbE3o3bOsuSQOtsS60UAfgSBgY3jFc73jR3sj8JzJ1dtHcOJ_OC5o3KsOp6u0YJNndYlxXkcduzMcsgfCXKJP04b3ULICt6t-hM2useMdyKNRjxguvleTLAr2rL9s3XCI4lZeiS2nd46XJITiE3UrtTdA-dWhw9sbAaxhiPG48Xw1v5xVQhnQv_y6x9CpnkQ7MvuleSWPuimTNyaKe3quTqyn0G-xMIS2WDNKzsyKty-WTYVlVX1ykGILNsxLU92nkaMS_sNPLh37r-XrQN_xIxcR4L7QfvSAgZw5Yybb_ZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 14:22:34</div>
<hr>

<div class="tg-post" id="msg-452447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=btvC-Z5-uUco74mZhoXzCim9LL-DVtMZh4CkWnHLwNw_1r-_HZGDbvS79bV0QI3gIYuVdRWGmkGvSdkje82ArVi0QN91jujTjpOyQzitx3p1xTeRuM5hwoO4EZPzS4ddfQxwdAqAQm6merZTj7ED3tgtzO3zDtMeBTehFpJI3n0LxgxNnjUCT2XD37vxTh-_zg-HDSzR0P1yKGBSU211ppo3a2dP8lL2Avm6IcW2PQUCzaSDwlKUqGcogUNFWGTDnkdOyL3QtHQI4ZbkwZkjL1O9ufy1_Pk-lUt9zVw-wiWYSF05Wqs8X7VfplPTYkH0Eea4j_rjpLsYJ164Z0Dy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=btvC-Z5-uUco74mZhoXzCim9LL-DVtMZh4CkWnHLwNw_1r-_HZGDbvS79bV0QI3gIYuVdRWGmkGvSdkje82ArVi0QN91jujTjpOyQzitx3p1xTeRuM5hwoO4EZPzS4ddfQxwdAqAQm6merZTj7ED3tgtzO3zDtMeBTehFpJI3n0LxgxNnjUCT2XD37vxTh-_zg-HDSzR0P1yKGBSU211ppo3a2dP8lL2Avm6IcW2PQUCzaSDwlKUqGcogUNFWGTDnkdOyL3QtHQI4ZbkwZkjL1O9ufy1_Pk-lUt9zVw-wiWYSF05Wqs8X7VfplPTYkH0Eea4j_rjpLsYJ164Z0Dy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بندر جاسک اسلحه‌به‌دست منتظر آمدن نیروهای آمریکایی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/452447" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmJmldPnBcwx2aqohJMoPC9Xs_CC-_jqoEGwtWoVrmKKkDPp59jP9YcNjHFCcWm0cDuLY-uCTanNRy40V9lQAbYyZzqM_jBpL-3qplqXzsz3gW3TEN-STjuWfQ79aBiL8r17v_g_0c6bI6-MQqWHcIseeh-PJERo8PWaEl_xzgnK1jg91ZDBBraUYss-wXKi7hdGgmmQ2GrP-05LSCoT_ObxtCGfuscx5h2YTN6Mlg5jg7hjbLUMUinBUzDLQ_zro9Q12SX07ZuJ7Lk2-Itj_zyyWwH7sm1X7L9uqgbMP-3CgtrG0sr8PVEd5Ep472g1_o2cLpIDKZxzup6I-QMOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: به کشتی‌های انتقال تسلیحات از ایران به روسیه حمله کردیم
🔹
رئیس‌جمهور اوکراین در گزارش عملیات‌های جدید علیه روسیه مدعی شد: در حملات دوربرد به دریای کاسپین، کشتی‌هایی که در حمل‌ونقل محموله‌های نظامی از ایران استفاده می‌شدند و یک کشتی جنگی، هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/452446" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhUweGw4_aJU3JBMTScO2RUbs_7pdDVi90q-sdId6jPmkQy1XRuYzpyDCsU51MslHQrdZgdZe0mhgOit6j2cFjcLMwcSYgZos4z9cld_MMuUKtkRGWGU7ISSnL1YRKYDMNhSEO0MclIp_LYwiFz7aqCmFKKhlIKrbP5-pOt9k1QGHwgkFt8fBIr_JvcaBFPhYwCJl3yVmgBnLm8GhkkG6nDaJI9Przx8AE563JyjgzrIYPBl9kzP7FbkM9uaQZP-qTD8kST8xeslb-5_SEwWLAZGzTFvhupMLYcczQ7L1LLIv5LIma5Gcvv9MlinqYmlXILgTWXhzckvs8zvGLYPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: جغرافیای مقاومت زبان حسابداری خودش را دارد
‏کاری که حماقت ترامپ با تجارت جهانی کرد:
🔹
افزایش مسیر ینبع–تایوان: از ۱۹ به ۴۸ روز
🔹
افزایش سوخت هر کشتی: ۱.۶۱ میلیون دلار
🔹
عوارض سوئز: یک میلیون دلار
🔹
جمع مازاد هزینهٔ هر سفر: دست‌کم ۲.۶۱ میلیون دلار (بدون حساب افزایش بیمه و کرایهٔ نفتکش و...)
@Farsna</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/452445" target="_blank">📅 14:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حملۀ هوایی عربستان سعودی به یمن
🔹
شبکۀ العربیه از حملۀ هوایی عربستان به استان‌های مأرب و الجوف یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/452444" target="_blank">📅 14:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtHdASrU1aR3mitYTaHTdeLmLeJyDZpROpIw7v6Rv9-B_ayAUb_p5eXUHVG_dewu9lYZB5fuSheT21rW7hZEXIWmQi5TthLMH3hWpbSbjnQ7ofAEkPMOcSjMo1d-GnAeii0w_pmNvLhmV48wDv6J4JQjJplAGT2yjE2GIMmySeNZiuzcmJaDzJKtDdZJ0lP5QJLTHYoOs3YH3G8a2ukaWwycGJw5m-FuVTr9xPLGE7fsXG1VPopEnARN77qgOv4Oa4WQ0Wl83v3rzZ5ai9ifwEWa2Kz8DR24gaLsqxNuMnpayq4pNT96Uvn1-nknAj5Vulinktjxo0q3uV2coSdzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در فکر دور زدن قانون اساسی آمریکا
🔹
درحالی‌که در آمریکا هر فرد فقط ۲ مرتبه می‌تواند رئیس‌جمهور شود اما دوستان ترامپ در واشنگتن نقشۀ جدیدی برای ریاست جمهوری ۳ بارۀ او در سال ۲۰۲۸ در سر دارند، طرحی که در واقع گول زدن مردم و دور زدن قانون آمریکاست.
🔹
«ان‌بی‌سی»…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/452443" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c4603615.mp4?token=A9igX2CxeXEGG1nMPjLzprBHiXOy2nYyF_mwZMYyenIpU46AclyaYYESnrvRHVqJScyIqQn2tU6UXiwSVc0DMOg1_BPyF1O_nwxHDOLuZdiRlsLgyWECuQsuLDJQPK6Hn4nF2Rvjj_yzraXiL6gpH5ySIq6ETfJF2I6tNPYOBW0MWlJy44XfBx8krQcmsFHea6gOEavW22eppeeZWxBLkHDzvBeCenryW9ui1XP1bLFEEUgXHHRZ_QD_hWP66WDJOxP8X3F_eRa7wLD7kresY8_zlWCSO0m-ezSS8qWpg9boCgNt_FPk6RGvqmsoOMiAx_TfzMtynyrw6XwEi8KZg1C8OQpI0JEq0T3KnfQeq_RljrLXZzAE65ol_DYl62ZNH3--Qy43mZqrF8yKlbMgqgN77RK0cU5vAgMS4H2YEKMenk-DgBGNeBGjSYb8Kerlz7_Q-uk5xf6n2eba3DU1Obkd79ZqVU2-D3j_ClzRHiTLnI6gFkiVKvgdPRW0_acJDT7zK-HsSWW6Dc5NmmIHvQJWjFW3pqSxTIMwoIPWnFvZuP1T4aQpqdl9qzG-NhnSjyv4cwsLTPfUs_fgqGdPL1eser59q86coF7z5WZeYvlChw3AndsXlbAZ8hQ1EZUzrts4DjQrLQNOkAzrm_fVrFz9mQgkj7VeUT_Sj5OBdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c4603615.mp4?token=A9igX2CxeXEGG1nMPjLzprBHiXOy2nYyF_mwZMYyenIpU46AclyaYYESnrvRHVqJScyIqQn2tU6UXiwSVc0DMOg1_BPyF1O_nwxHDOLuZdiRlsLgyWECuQsuLDJQPK6Hn4nF2Rvjj_yzraXiL6gpH5ySIq6ETfJF2I6tNPYOBW0MWlJy44XfBx8krQcmsFHea6gOEavW22eppeeZWxBLkHDzvBeCenryW9ui1XP1bLFEEUgXHHRZ_QD_hWP66WDJOxP8X3F_eRa7wLD7kresY8_zlWCSO0m-ezSS8qWpg9boCgNt_FPk6RGvqmsoOMiAx_TfzMtynyrw6XwEi8KZg1C8OQpI0JEq0T3KnfQeq_RljrLXZzAE65ol_DYl62ZNH3--Qy43mZqrF8yKlbMgqgN77RK0cU5vAgMS4H2YEKMenk-DgBGNeBGjSYb8Kerlz7_Q-uk5xf6n2eba3DU1Obkd79ZqVU2-D3j_ClzRHiTLnI6gFkiVKvgdPRW0_acJDT7zK-HsSWW6Dc5NmmIHvQJWjFW3pqSxTIMwoIPWnFvZuP1T4aQpqdl9qzG-NhnSjyv4cwsLTPfUs_fgqGdPL1eser59q86coF7z5WZeYvlChw3AndsXlbAZ8hQ1EZUzrts4DjQrLQNOkAzrm_fVrFz9mQgkj7VeUT_Sj5OBdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران اربعین در مرز شلمچه  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/452442" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af7pgKMVsCsmekK5vALuR65RHNnSDWcEGTQuTTgPl05_lBPlc9oTkEvl-eqzPKMVDmG-ClkHn3evpUymXPR5l0__0XWIBqJOrr4JACDcByX7SiCVAktiI1A6cIekDdt9hV2f-MbPNLF0zdbD4qfBBNl-YkgeNTQ60JueUyr94BBtoxjmkIyrz1Cvv7fK9gIwx9EOb3bl-q42vjqcHtVC_HFYIh46Ff8HZnfN6YOrfGEpinTvXOrnIxlIWYjPTnGX6w17TIwq8YJSRwa3wC9nf6ebRhh2FIr69W23YOgoQOJ3n5vNLo7ZedwLCPM_T5RzvrR9bKQ3zOKVcupyGqB1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: شلیک‌های مداوم رزمندگان ما، تا تسلیم کامل دشمن و گرفتن انتقام خون کودکان مظلوم میناب و لامرد ادامه خواهد داشت
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/452441" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjVFdGUTeP_Ogp7-zwT-De48t374XMxutzfzAlvBOFZ3HmpZT7tjvmeMB1lWqT-Wt5z4gnTUCeXfaTQ5-ZXlRDCDFGtwwWPCqfCrEuitKD7OTXICCKKFlFewrqkPo5kh_oVmdqjuw3NYWo7D6jcrRgzNj22m1paouCTQSStLK5f9X5qClsmL0tH4F_v-Jm8gepn39KrsPx-UQObNXKXkoJ5vDjyt9D0VDTs4Tsc_SLmkmz2yLdvMNQB-Gd3Wi2pedjM_Q44tf61gZWMqq4hkX97MTho44vTQnRus7XhXbYc12vdBP8UuEYw4z8bPDcjgAyqS-QhnTfXFJD_QHB7vpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انیمیشن «سفینه نجات» در راه سینماها
محصول جدید سینمای انیمیشن ایران
«سفینه نجات» تازه‌ترین انیمیشن سینمای ایران به کارگردانی هادی محمدیان و تهیه‌کنندگی محمدامین همدانی پس از ۲ونیم سال تولید در سکوت خبری به زودی توسط پخش بهمن سبز در ایران اکران عمومی می‌شود.
محمدیان پیش از این کارگردانی انیمیشن‌های «فیلشاه»، «شاهزاده روم» و «بچه زرنگ» را برعهده داشته و همچنین محمدامین همدانی با انيميشن‌ «پسر دلفینی ١و٢» شناخته شده که فروش ۵ میلیون دلاری و جذب ۳ میلیون مخاطب را در جهان رقم زده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/452440" target="_blank">📅 13:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-text">🔸
مجمع مس ایران به روایت رسانه‌ها | ۷
🔰
مس ایران، در مدار آینده
🔻
مجمع عمومی فوق‌العاده و عادی سالیانه شرکت ملی صنایع مس ایران چهارشنبه ۳۱ تیرماه در مرکز همایش‌های بین‌المللی صداوسیما برگزار شد.
گزارش گردهمایی سالیانه سهامداران «فملی» را از نگاه تلویزیون اینترنتی «معدن‌شو» ببینید.
#در_مدار_آینده
#مس_ایران
#فملی
@mespress_ir</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/452439" target="_blank">📅 13:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/452438" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUP3ndmSfyS__WaYJu8HA0s2Kwzw5-T4K_UN-vonGCOgQjKjHCV-FJEEvJGAEEmnOKny9NaSczgDDS0fukLbgxsD0pkOcCnsQV8pwC6HTZ6bEs6CsqDIT6ENU1CaUh9tqYTTnd7NgA-IrpTRwl4sOF0cVl6vq0z2E0fcX3lle431RUnidH3IMgsXw84eeD8AiQr1zbX9n_oPacZPM0TdLvc3saw-CVQ35DnUK_VtyGnU_eGkzpp77EE0OAPUv5hROqHf_M6UuRx_juSXeZoUbXFMYKpE6OLDcHa0IpaoU4yAvaitNm4NPUa74xsAgaGm_i-O7DN-UvJnIioTYPq2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ساختمان باقی‌مانده از شرکت آمازون منهدم شد
🔹
سپاه: ملت قهرمان و به پاخاسته ایران اسلامی؛ حماسه قیام بی‌نظیر شما دنیا را بیدار کرده است و دعای خیر شما، پیروزی‌های درخشان رزمندگان اسلام را تضمین کرده است.
🔹
رزمندگان اسلام در موج ۲۷ عملیات نصر۲، در تکمیل عملیات…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/452437" target="_blank">📅 13:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPh_l4VPQ6nI8LoKnHSdTfBmVVTWYWnEj_Hl3293fpvUCU2GKs73dEYCp769nYXRXIuXnWKAAcRS_J-IruQJIsojFzPl-jcYqnYSSR7a9MDtz0ScvOvBdRts1j1YkqkV6kUhGEN37E-wQwljG_nbK6ONneTARhGqtmoklmbMZdIISLXrQEctVJ9dXhaxs6jcAuu5S3IaiC6HiFe2Mkh6Kf53slOq00mGoyRLsPUxoxKzwI9qzjUDn9lQPixhHOp-kW26yhdYPHOdhgLnPf0hSV0fiEeeNRo7fYxJWdeG4OvumD_y_kPHf-b5i1MviC4f6HPMYFl2E_aVvF5VsZfYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیروز قربانی سرمربی آلومینیوم اراک شد
.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/452436" target="_blank">📅 13:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVlrTSeElUHXHvRdte9CklWY59D8kqPtrVfptx-dw9hUccVKQ4PVOaiaELk7ORe-1dCQpssaZzAtLOsJ5ZOws_VXCJzfw-QDTXZ5FSxQz1C-f20jvdZqDrJqxGQDswxNmOAVVBpR_MGgI_qMQZBasE-Ku6HOrxrvIQpVAMuvxYkCRcUCS674Gbo3gMxJ13raZooqKzi-fv5LQrktLdnB5qRAQlS23fCYHaZwqc44mcwCRF0xmHvetgqL15b1lqmgPyBHdOLgRPQHFssYScU3jEic2gytzWJCg2yncOISYIhP-06OaivcUAktq1Z1Pl8aMk-oE4cBSpHINa8zWr_5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک به پایگاه هوایی ملک فیصل در الجفر اردن  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/452435" target="_blank">📅 12:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452434">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fbcb92eb.mp4?token=ps_7gUyMYJap3hUnptiYqndRCyMjig47ERdKVMxv3tTFjmBVct43S0h5Xlp5c3dS7LwkRPocG7639PMECcyPRQnCL8xs-2Wc1K4UUwHqArAOaf3QgFjEenrtDqbjNR-FTgTKgl2fsUIxYkbHFxJofNotKnoDS1pG955zIPsp01zAGwdcgl7BEQ3xSn5mem5dGu13TZuIDmziYrLrpQ_5ZIAlB-osiDk3msWXTOjTBUEhrcPfKzT3c5r7AN0zs8Bod92k_ceTEeOLeXMDvBd3UlE8Z3cQv_GHMcCVR2yXtSQi00wfltDrJ67sY4DHIBSVsyKQL76afPr_EGDyGeLC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fbcb92eb.mp4?token=ps_7gUyMYJap3hUnptiYqndRCyMjig47ERdKVMxv3tTFjmBVct43S0h5Xlp5c3dS7LwkRPocG7639PMECcyPRQnCL8xs-2Wc1K4UUwHqArAOaf3QgFjEenrtDqbjNR-FTgTKgl2fsUIxYkbHFxJofNotKnoDS1pG955zIPsp01zAGwdcgl7BEQ3xSn5mem5dGu13TZuIDmziYrLrpQ_5ZIAlB-osiDk3msWXTOjTBUEhrcPfKzT3c5r7AN0zs8Bod92k_ceTEeOLeXMDvBd3UlE8Z3cQv_GHMcCVR2yXtSQi00wfltDrJ67sY4DHIBSVsyKQL76afPr_EGDyGeLC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرز سومار از فردا آمادۀ میزبانی از زائران اربعین است
🔹
فرماندار گیلانغرب: زائران از فردا می‌توانند از مرز سومار راهی عتبات عالیات شوند؛ مرز مندلی عراق نیز آمادگی خود را برای ارائه خدمات گذرنامه، پذیرایی در مواکب و تأمین وسایل نقلیه اعلام کرده است. @Farsna…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/452434" target="_blank">📅 12:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452433">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAVdGzLZ43MObi7pdwQoyyjNtmDc0VPivi9CeMvCQVgefaQVhZq7jkNDThoQxFgHnzijrxodHOSWPg2fXaNDylg--RjwPv49BfDlCcJIEpOsXybafqE4yiyXeg_nMfH6XKBLJEjLhb0JpSP0T6XNt4E0x4bBnEHQWObIaNG9F30KflvdrvD_ldtJEgkaqwo8nLedVaqkAm7iP4rhvW-qtPzKAjVxNFDR_MOZQIxpjz6chGCWE-qIDw2on9kicrUHW2olQ6AIss9vPrBGflM1_pH1GyBXcf6i9iLLG_eMB5Qs0f2L23htbMK7lXKf7rl5F1sZlUAs3eXaBplaC3QDaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۰ هزار واحدی به ۴ میلیون و ۸۹۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/452433" target="_blank">📅 12:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452432">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkX2V7cc1LjQKasRzY7vE76Tlg2CoFfPSe0byhqJs4W2oQ6ktsUEugfgcHpsMKxu4rINuI6Gvvxg6FF4Br2h5jQamWiwy5hMk2B_QxyTdAM-QuPu45IKavGW8xInFMa-gTGdQnusWPy9Zq4w0VaVOr5G9CzYIiOvGI_GwZOvfdGJTJnHg87IxGxEXzc-517YVA2GdVmvf7eaBbrQQpXKt-bqn3TuBW1qAbHQ1Tt6T-fAKZgmEOtBwAEkxbGYQqhCHu7x5WHEaEp4eg5jU-zSTZ-u9EVZKVqYPC_Z_WhE1pdwFtmRagxcBcypVQaCRRODmlO67p_MX-KwnhhlKfCUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثه دریایی در دریای عمان
🔹
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) امروز اعلام کرد گزارشی از وقوع یک حادثه مرتبط با یک نفتکش و نیروهای نظامی در دریای عمان دریافت کرده است.
🔹
این نهاد در اطلاعیه‌ای که در ایکس منتشر کرد، افزود مقامات از این حادثه مطلع هستند و تحقیقات مرتبط همچنان ادامه دارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/452432" target="_blank">📅 12:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452431">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادارات مازندران فردا تعطیل شد
🔹
استانداری مازندران: تمامی ادارات دولتی، نهادهای عمومی غیردولتی و مراکز آموزشی فردا به‌دلیل تداوم موج گرما و ضرورت مدیریت مصرف انرژی تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452431" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3K_pDhwajskNKyMC0L9q5K_mWj9IGJhggy1mrh5BurPbFxDb_cQc4awnF3NaDaF3kzEkbU_u97ampkyDCTVH6NlKGrSoZYaVVbG7ztKcL61GeWWzp0q5nKESo-8OfLI2Y-5_CckGEVaAq3tzfR809nEMBDiNu6p3-Mj_NzhOAUFvJ9ZaRQW5pYKF9Dbug3P-455JgqXT6h9qj6HZ0RCMLAYBNikrMvSWSTDv_omJOL7kGDUtDToa9Puf2xQijjuCaKl8J5dIk8QNSrfRBdi8ztNUxUiwByMSsXt93Y3Hvq3e3gheB27b1fsF5SpiWzn7nsxM4ZvJHfsja8aQQxR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۱۱۷ نفر در مهمانی شبانهٔ غیرمجاز در رامسر
🔹
فرمانده انتظامی رامسر: درپی دریافت گزارش‌هایی مبنی‌بر برگزاری یک مهمانی شبانهٔ غیرمجاز در جواهرده، ۱۱۷ نفر شامل ۴۹ زن و ۶۸ مرد در محل مراسم دستگیر شدند؛ مقداری مواد مخدر و تعدادی آلات و ادوات ممنوعه نیز در بازرسی از محل کشف شد.
عکس: مرضیه سلیمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452430" target="_blank">📅 12:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twVe9bJrdzhBuo_8YSaRw264qY_zhR_rK04CKefaXEYiXVUaLlV94W99ypd8y74Oynz34G0p0DcwFiDgNzCNIVj3Ljv3wC_Ou26mGUV44b5qSo7eDcBgdHUZySy7Y9WrIxvNOiv1kLrU0fByO7Z4xflRycnzewC_WdvZwHy1RdS2_fpNDX3xXJBxYFhzqg9zwm6YH_YhiA3M29kpt8WnInxZscTyLCHU75zDMQ4JKfTPLkM13XA4L7YAz5KFeH2YtD7PzAuK4b_2YFK20QkKF3GD5gN3ihZDBFV53ThaebYYwVrx26XAsxg0QI2FQt6o0AaYmgU1XOETUCPQf7PL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urB8zVgO7stk5zfw4wnXRGT_9KCWqrfZ-IsMR67cSz4uVIChdgL0e-_bNRxDPNvNuEfJngHaX9Ip0HIeqidNDoz0SkNfL6YNHBELHq3FPs_OU0CoFfJToSp2wBLyV0Ftz7HmBiShbGSkg56tScyra8c8AFHZ0V5sDcfMDUT0qgpNih_JKA9YuZfaN9WKFLUXnvmSkUPnpGNbpdmuTr6hdYB29x4VpfCDaAlUFbSS7_5nUBmcB-nfdji4VW7drOP5OdvctRXiVXRPGS4AZ72vbOhkqFTmSyFoxOL5aJa7YKzMjK-MJnYnDN-kZPubD4zcqi2FzfpYuteL-0fFzmEJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEPKq8rNL4VM1fX8uY26xQ4fv0Dfv6ThIDlSIAuvFEe12vaUj--FEUUxqYGR7P8XG5-yrIWYJUVCM6nI3NoveZw_IOTviPblizxm35kK4mLsd8xHyODDQS0eo-ez8pas7gcCdAhExVSlAPdyuThg4RU1OhsduTZ5YPX1sqkRPuIR_WbreWg0wySI4BE4akDAjr98fVkFJmruiyZNQk7UL6vE5j_SHknNFc855X3LukDR1g8-XWerjiD5gylTxZYWTpCYaXELAkopmjYlm3JaaXzS5-0KO0A9ua_0_6Tj4CprzwrPs_7mCFkcFoJu65wxGbxZVVSXEdIVYpGSHPORyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L874mccNGLNc4roI-H0o_P8saRdyo5zW8kfygx9S-rN9n2lWXzdfis-ISYkYlSLG8JyJyot4flLwY29oQflCPzTCZm2uXdER_Uob6zuOvxV5KWPBiiku18qP1MwOOSuJwqM3W7U9nQo7nnjdS3esoOGA0VAnFRw0TTPU8KKcTPcVbD6t_LiXQM8hjFJa8dM7UolhpTUB2OCF3HlWpEk0Y12HRdqlcMuZCo26-zxbPX9no5RFVaGLb9yCmFkGDOo_fqBuWN6ff70II-q6LI5Ks-EK2D8pXM1PgJ1DobKsHNjbprXK6Su-S2Xn3nnfv3lRCCz4p1gD-4s3XaT0I-SCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taU4nxrGndknEVD3VBehWm52IEzjYdtY3o3CxoI63HeRobPf0bsyLloJQkFgTny6Ob2pdxpXFuqaC9nm7rBrBTdsXj-aiVLGUwVySuw5ceQg8SxdCAHKtgoS_fn-_KFlTIYFhmtPu-l2kY7cewT-1IDrcq3XuzdTvu271Z5tLds9FR8rk2_btJwVLy8FcAOlxcLBIuuFCAncuO03Lpeemnr2fX7e51Uim8lt1hDzbCSgUqLfIv1k4WMxHDOjGLNJquE8W0rDLBshtLUSMmvw2_O7IlHQjHOxCT-8RsTp-ssGLRowXEUdCGvKatxiziNclIdT1Cub7ZBmXk0ZwNvGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vu1AjyX1j_Df9uuz8F2OGQq2_0AWRR8yQFvHUFqLX3mXn-dMdJFWICm8-IkCUJWFtJbSLkTiuaYsQyedOZDtQhc95TPbk-lbS4MeSvOJX9eC-bQRqmimOHBTRv1CilufVbXq_dRaEcNTWh_PPaGRj21dvkwTde3SCxxLsA1FZu6iWM52XldPbc5D9sdMcOLlM44b0KPFi_jaMdHwc1-8O2I5ZD0HvJxnHECKgroqDWnBNew11YQn14jnNI8IZqCCnRq3FhWf9mRv9EfO0bNLG39mDa7Pz0k3jHnyy1KQ5ac8Nf9gcsFpfXfyB1hXmEU6xBMTrL7pDRfCzSCLqXFd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2huYNtfOkEVYe7_OcIjKH4RFDYZdIXKEk2XAk91jaAoDj_-LNnSg6wbpjjv9305-KjkJdCIOpX1DLMGZhosLolZLtYZyYz_UkvVlTZ36lxk0d7q2qskEY-lNoZroFCIIpVI41YnxJgV3Zj_DzrZu08-9FQwO6hsbW1vHu5Ns-5D1qMG_2URtOs6K6u50pgAhlHScnXSQ1LEvXNAhlHPKrkWI5FWImtHE0zg-FA2-1FjrrzfxRRQZtnG0IaTFzy1cCEm-jS7UAs3Wv88soepLq5vwyI9xneq3dVs9VLJi5OTC_2eSpMOKGGTOUQUWpS-ArJjEvIGD1lAnoKmdTjB8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فوت کودک ۳ ساله بر اثر حملهٔ سگ‌های ول‌گرد
🔹
دادگستری کردستان: درپی فوت یک کودک ۳ ساله به‌دلیل حملهٔ سگ‌های ول‌گرد در امروز، ۲ نفر از مدیران شهرداری سندج دستگیر و علیه مسببان این حادثه اعلام جرم شد.
🔹
سایر عوامل دخیل در این حادثه که مرتکب قصور و ترک فعل شده‌اند،…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452423" target="_blank">📅 12:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtaSdylGZu3QLIAPyWYOKlMEJacV1t_6RezazaFFKVHIK8ajptH0gMOO6R4iT_QiTPOud95GsHGInYQe8NkUjrZX7rajmdh9y7MiRJls5omMY-AHVJ0AR4MenpYcIyZIxuRoTKo4LjrXEb_OqOQACjMrcmXTmuvL-WUYSRsb6UvYs--hFXT65lifpON4OGO8kybGzv-w_3W5nAG3JFukI087jDy86dh_oT_7LxWb4_w1sdy8NA3b9mvaiZUVrgA689JrASTpqNFpS6uplNK6S1QbuXWT21zlVrLXT8J06gOwUPKdvWJ330llGCsgHCetxK6yVdpx0Mg943NXoW3V9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: شهید خادمی چهرۀ تکرارنشدنی اطلاعاتی بود
🔹
فرمانده قرارگاه خاتم الانبیاء: رئیس شهید سازمان اطلاعات سپاه از نسل اول سپاه به‌شمار می‌رفتند که با مهارت‌های بی‌مثال، اشراف کامل به ساختارهای امنیتی، زحمات طاقت‌فرسا و ماندگاری را در حوزه اطلاعاتی رقم زدند.
🔹
به جرئت می‌توان گفت که شهید خادمی در مجموعۀ اطلاعات و امنیت کشور، یک چهره تکرارنشدنی و غیر قابل قیاس است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452422" target="_blank">📅 12:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452421">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225fcfe9b9.mp4?token=gfNEChcef_h6YLTDkYIblX0AaxX44iKFxRWVc_X3o0r26glCakr45sTRlydauq5PjMTpy0fqFyi8mMK8njtoYyx_qrDvzWY3glG_SBKkNqVV2sduOYV-p4Ux9f2QrnEFEHjUgbwtvXvcaL_hhNhpJDbh5QrpXdA61cAIwBuF-FsroB8D3_kCkuRCqrev_xXLBjPt9yPbdsNZVp9Lsvlm9obhDyL93-s4BvQQALA7OotBhSxojNr_xzOJoigpmzDRRkN3S_xdt9XcnyN54Rg39X1NWZ1cYTMGPuB3SnSM4hrq7y_acHJZP_jcQJo3C8h1Fp7BneZA60uvAjHR7Ft9sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225fcfe9b9.mp4?token=gfNEChcef_h6YLTDkYIblX0AaxX44iKFxRWVc_X3o0r26glCakr45sTRlydauq5PjMTpy0fqFyi8mMK8njtoYyx_qrDvzWY3glG_SBKkNqVV2sduOYV-p4Ux9f2QrnEFEHjUgbwtvXvcaL_hhNhpJDbh5QrpXdA61cAIwBuF-FsroB8D3_kCkuRCqrev_xXLBjPt9yPbdsNZVp9Lsvlm9obhDyL93-s4BvQQALA7OotBhSxojNr_xzOJoigpmzDRRkN3S_xdt9XcnyN54Rg39X1NWZ1cYTMGPuB3SnSM4hrq7y_acHJZP_jcQJo3C8h1Fp7BneZA60uvAjHR7Ft9sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد صاعقه با موشک چینی در حین پرتاب!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452421" target="_blank">📅 11:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
یمن از فراری دادن جنگنده‌های سعودی خبر داد
🔹
وزارت دفاع یمن اعلام کرد که پدافند هوایی این کشور با شلیک به‌سمت جنگنده‌های عربستان، آن‌ها را فراری داده و مانع از ورودشان به آسمان یمن شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452420" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5faf50be.mp4?token=Z7sTTPEXDKLPQKFzRVLMjD9uF_KmOv8kJuGHz3Raem_ND4uBUSwTes-kBkLZFa0DNMducjRTwZKK6tefy-JnhtZFS5dqZf2rWw9zPdaAyrbbC7TROrJahKLbvopVAsy0kmGgaX90H8PHnPTZ9aO4klKbL09bd298p2JE5XClgR4bQbaaWT5Df0L4veeT_JCY0YxXObqbLx7n3k6mLik88dw_c6_F31GIorvpStxyEXg3CZq5Ax7g_hqwoAxd10_WuQs3xMhe1grbypftZJF-q5BGq9wiAVAl_RacR9sLAT6IxeNSjaV7VD1Q7J0ux-AIaEaQ5xVfYWxec9ykve9nlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5faf50be.mp4?token=Z7sTTPEXDKLPQKFzRVLMjD9uF_KmOv8kJuGHz3Raem_ND4uBUSwTes-kBkLZFa0DNMducjRTwZKK6tefy-JnhtZFS5dqZf2rWw9zPdaAyrbbC7TROrJahKLbvopVAsy0kmGgaX90H8PHnPTZ9aO4klKbL09bd298p2JE5XClgR4bQbaaWT5Df0L4veeT_JCY0YxXObqbLx7n3k6mLik88dw_c6_F31GIorvpStxyEXg3CZq5Ax7g_hqwoAxd10_WuQs3xMhe1grbypftZJF-q5BGq9wiAVAl_RacR9sLAT6IxeNSjaV7VD1Q7J0ux-AIaEaQ5xVfYWxec9ykve9nlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ در مراسم شام خبرنگاران سوژه شد
🔹
دونالد ترامپ در جریان مراسم شام سالانه انجمن خبرنگاران کاخ سفید چند بار با چشمان بسته دیده شد و به نظر می‌رسید برای باز نگه داشتن چشمانش تقلا می‌کند؛ موضوعی که به سرعت به سوژه رسانه‌ها و کاربران شبکه‌های اجتماعی تبدیل شد.
🔹
بسیاری از کاربران با یادآوری کنایه‌های پیشین ترامپ به جو بایدن، او را «دانِ خواب‌آلود» (Sleepy Don) خطاب کردند و برخی هم این صحنه‌ها را مایه شرمساری توصیف کردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452419" target="_blank">📅 11:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452418">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در شهرستان ری
🔹
فرمانداری ری: به‌دلیل انجام عملیات خنثی‌سازی مهمات عمل‌نکرده در امروز، احتمال شنیدن صدای انفجار کنترل‌شده در بخش خاوران ری تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452418" target="_blank">📅 11:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452417">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbuD73KzhLG5xF039Rso0A1CSL60fhs86ruFnNBo7KmEAFds8X42G87EVt_vdqhn30u9P0mW4vae6g4TU_YvlgmxIPMwqpTYO5rNa-PuxN_uSEzdbkSdloDbkc7891zZOPJRlPrx0oCCVqDuwUADdPT5UbOKZpc2Qds1kURAVmhHtG1-Q4krvGZ1omIWPeUBnTnh6OyoIORml8RRqYHWo7bHOpHU6IIdkzWxJl34uYsfL7jcNHBqOSvpG-4AC_JfBpeG7L08AR2eLWwIBNSnNw9IQj2UE3CGfMCWG7QS4W-FWi4JsfqFsTsVOYJG275TdTt7MfZzSr8XBdmTaWOYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار آمریکا: ۱,۵۱۴,۶۷۵ ریال
🔹
یورو: ۱,۷۲۴,۳۵۴ ریال
🔹
درهم امارات: ۴۱۲,۴۳۷ ریال
🔹
یوآن چین: ۲۲۳,۶۸۳ ریال
🔹
روبل روسیه: ۱۹,۴۱۱ ریال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452417" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452416">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a8a34369.mp4?token=A3iqEow3XpgWgL2bFRDllZMolBMdnf6n3KPjPUaclDn_LejLn8v2OPOzj14Ai2jqmRzVrFfYtJfGH_PkTlfqZ97cBs6yTiPvd2Ow_OT2TAfMHkeVrhGzzhgzsyQ-JALogidCHniYBQF5Z2hTdJHEFZtE8XO4rQKSll7kTaDA1aJLPUHGv-zAwkejv9sJcX7QEH-VAgkNaauIfdUOIk-NxmjCxRrUu0LTt6yuubo1vcjPVFSLqKyEQAgDq6RQ8OnodhRiu3mQVvWqdE3LBplxiVSn6CNa0EwFhHpDPjo07fhgJbnHitCVtOf8POpOfPA__RkH_lV4tdosdeBQfFovGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a8a34369.mp4?token=A3iqEow3XpgWgL2bFRDllZMolBMdnf6n3KPjPUaclDn_LejLn8v2OPOzj14Ai2jqmRzVrFfYtJfGH_PkTlfqZ97cBs6yTiPvd2Ow_OT2TAfMHkeVrhGzzhgzsyQ-JALogidCHniYBQF5Z2hTdJHEFZtE8XO4rQKSll7kTaDA1aJLPUHGv-zAwkejv9sJcX7QEH-VAgkNaauIfdUOIk-NxmjCxRrUu0LTt6yuubo1vcjPVFSLqKyEQAgDq6RQ8OnodhRiu3mQVvWqdE3LBplxiVSn6CNa0EwFhHpDPjo07fhgJbnHitCVtOf8POpOfPA__RkH_lV4tdosdeBQfFovGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
‌کارشناس اینترنشنال پس از ۷ ماه: کشته‌های دی‌ماه ۳۲۲۲ نفر است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452416" target="_blank">📅 10:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452415">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnz0G3PX3fE_w1ufaIC4PpcTpu0os8XVKm936ccA4CJTge6Hq-x7COeUE3zVWiNgpdcHOF6-T9v7K1ZZzk4KBEZi8FJuCgNGJEQp6ZrvgSlXNqdTWg5waSDVgjejwmdypINq00RsbkpSL1PUh6Vr-6aNPeVirCj5Xr3q_sQ5DZxRNpSulXqgZt9tn6_Cy6IVSaizPb7yWaUhf3Bw2h9zKTeSAlyAfiuqP1vJMystYnn9ivamK7d8JZsRb26ABi5EIICaW0MAaUO_bRBWBVo52NPHvBPr1npjKYE6EdBHbm5Sdh27E500mFioghcsBR1vn6zYMD4cBAQEM-NsceqlWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار پیرانشهر: از آغاز تردد زائران اربعین، تاکنون ۳۳ هزار زائر از مرز تمرچین به‌سمت عتبات‌عالیات عبور کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452415" target="_blank">📅 10:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452414">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در اصفهان
🔹
استانداری اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب و غرب اصفهان، بهارستان و صفه و ابریشم تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452414" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452413">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRhtxpEjdSnLktIyZ-ArCFsTrmhpHegPPO2OK4kp_bR_uAn1-2Ut94DSLg1h_Rau9yA7VglLijFau_JcNVtrQ5Dtqj_tTsb7nc9MyoIWKfa3FDGw62MPnvgWIBFMMLrga4KHqch56p5QKnVc76BjtiUQU4iIWCfNzXNj2RLna5UyHVIIAkTIZ3JbGps0DthgYJoKWkrIWNMONJ8199uSWeDdlGqZf8l4tD3NI6sII_LcnaZKqDfGh6uqAzVHwqngQ7wfktKoLFT_v6gS1bsIngf7a2v9chw1FS7oD02x6nutiQGmSb0azFSIkpijtCiXG_tDGRNJ6A-cNpJ8lfka3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش عملکرد ۶ ماهه چادرملو؛ رشد درآمد عملیاتی و جهش سود خالص به ۱۴ هزار میلیارد تومان
شرکت معدنی و صنعتی چادرملو با نماد معاملاتی «کچاد»، در گزارش صورت‌های مالی ۶ ماهه منتهی به خرداد ۱۴۰۵، از بهبود عملکرد عملیاتی و رشد درآمدهای خود خبر داد.
مطابق با داده‌های منتشر شده، درآمد عملیاتی این شرکت در نیمه نخست سال جاری به ۵۳ هزار میلیارد تومان رسید که در مقایسه با مدت مشابه سال گذشته، رشد ۲۶ درصدی را تجربه کرده است. با وجود افزایش ۳۶ درصدی بهای تمام‌شده کالای فروش‌رفته، چادرملو موفق شد سود خالص خود را از ۱۲ هزار میلیارد تومان در دوره مشابه سال قبل، به ۱۴ هزار میلیارد تومان در این دوره افزایش دهد.
همچنین بر اساس آخرین سرمایه ۵۷ هزار میلیارد تومانی این واحد تجاری، سود محقق‌شده به ازای هر سهم (EPS) برای این دوره ۶ ماهه، ۲۳۹ ریال گزارش شده است. این ارقام، نشان‌دهنده پایداری عملیات تولید و فروش در این غول سنگ‌آهنی و توان سودسازی شرکت در آغاز سال مالی جدید است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452413" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452412">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tT1N2fCObUFyLnvs4IG4qoQaaLP5vi1zwQcRVfDSNlnHxavoc1DDJZJuWZuW6qak1J63cZP8sQbbWm7Kk1QwOkmgo3mCO8mL2aqaP5QcahQsN7WF3NCCL6e9gABFzXseC-gNzIR5-s5AVD0DTst7PdV02Rz2xts0VyC2DTFezeT5bLxH2gN8z8coO7Q1L1TkKNb24MulRvyYORr-hQk0dfNDIbx8dKKKCVzT4AL4q8PGY-bbZHHgGsjZ6pZjjYddl2cWP0wlcgTIo-FNYllbDiftK-yXD3fMHQ6Op2u-xEyEKlM3ahbSRzorWc4d-EKb0z5td_LgvYH_QiccFhs5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛️
مجمع عمومی عادی سالیانه بانک تجارت با حضور ۶۳.۱۱ درصد از سهام‌داران برگزار و صورت‌های سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ با رای قاطع به تصویب رسید.
✅
این مجمع با حضور سهامداران و نمایندگان قانونی آنان و نظارت نمایندگان وزارت اقتصاد و سازمان بورس اوراق بهادار برگزار شد.
✅
گزارش عملکرد هیأت‌مدیره توسط دکتر اخلاقی مدیرعامل بانک تجارت تشریح شد.
🤝
از همراهی سهامداران عزیز در مسیر پیشرفت خانواده بزرگ تجارت سپاسگزاریم.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452412" target="_blank">📅 10:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452411">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452411" target="_blank">📅 10:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452410">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توقف فعالیت فرودگاه‌های جازان و ینبع عربستان پس‌از حملات یمن
🔹
براساس گزارش‌ها، درپی حملات یمن به تأسیسات نفتی آرامکو، فعالیت فرودگاه‌های «امیر عبدالمحسن بن عبدالعزیز» و «عبدالله بن عبدالعزیز» در ینبع و جازان به‌طور موقت فعالیت خود را متوقف کردند.
🔹
همزمان…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452410" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd31d411a.mp4?token=he0ptv73QPp5i2QkYNeKsHYFiYx-m29PEy42srl8rtRLLWHRdxwjJTXnYuhB7zbuR9gzZHeXWy54oyurbgaB8dmjWhbTYjH0hd93Wu9xlS6Q6Hk1gRwiha5mXu9Lfg0WUvWAFV3I2QkFfkh_cSFc5luspKCVf2sh5bSj7rQdcWDFQwnWPaxczHfKoUtCogASPa_wy_w17XcyqIlJP5jYZ2OWmwUWK3RHYXWzovhQCfFWQi_bS8vzOtro1Qu7u0HwOsJugBUMdefBlsAkuKl-btEPro3lGEg97ccvLNHK5v5wdZX3NIjAfSECzbJQOVKTZkL84hV-mQ3KdtSlgV7p1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd31d411a.mp4?token=he0ptv73QPp5i2QkYNeKsHYFiYx-m29PEy42srl8rtRLLWHRdxwjJTXnYuhB7zbuR9gzZHeXWy54oyurbgaB8dmjWhbTYjH0hd93Wu9xlS6Q6Hk1gRwiha5mXu9Lfg0WUvWAFV3I2QkFfkh_cSFc5luspKCVf2sh5bSj7rQdcWDFQwnWPaxczHfKoUtCogASPa_wy_w17XcyqIlJP5jYZ2OWmwUWK3RHYXWzovhQCfFWQi_bS8vzOtro1Qu7u0HwOsJugBUMdefBlsAkuKl-btEPro3lGEg97ccvLNHK5v5wdZX3NIjAfSECzbJQOVKTZkL84hV-mQ3KdtSlgV7p1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای دق‌کردن دختر سه‌ساله در جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452406" target="_blank">📅 10:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">انصارلله: عربستان در همه چیز به اسرائیل شباهت دارد، از جمله در دروغ‌گویی و تجاوزگری
🔹
محمد عبدالسلام، رئیس هیئت مذاکره‌کننده دولت صنعاء و سخنگوی جنبش انصارلله، حمله هوایی به فرودگاه بین‌المللی صنعاء را نشانه‌ای از ادامه سیاست عربستان در جلوگیری از بازگشایی این فرودگاه دانست و تأکید کرد که ریاض همچنان اصرار دارد فرودگاه صنعاء تنها با اجازه پادشاه عربستان فعالیت کند.
🔹
عبدالسلام افزود: ریاض از یک سو بر ادامه بسته ماندن فرودگاه صنعاء اصرار می‌ورزد و از سوی دیگر با صدور بیانیه‌ای مدعی دفاع از «حاکمیت یمن» می‌شود.
🔹
سخنگوی انصارلله تأکید کرد: «عربستان در همه چیز به اسرائیل شباهت دارد؛ در دروغ‌گویی، تکبر، کینه‌توزی و تجاوزگری.»
🔹
رئیس هیئت مذاکره‌کننده دولت صنعاء همچنین هشدار داد که ادامه لجاجت عربستان و خودداری از پذیرش واقعیت، پیامدهای خطرناکی برای امنیت و اقتصاد این کشور در پی خواهد داشت.
🔹
عبدالسلام همچنین اعلام کرد که اجرای محاصره دریایی، نخستین گام در «نبرد محاصره در برابر محاصره» است و تأکید کرد: «ملت یمن از حق خود نخواهد گذشت و آن را به هر شکل ممکن بازپس خواهد گرفت.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452405" target="_blank">📅 10:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b7e22d39.mp4?token=j_fYjXbFEDXe4V7czNN_gJyejrcG33OdsGAsZVXMKTSigtnraMB9AhlDE1b9GgW4VyPLXnt8ErXOxwl9vV9YK7--3ur3eW3OyDSvm5cvasX-_PzBc3iCAElM2nanc__PjKEYabfVlNO9WBmWkBIrpqfKvS07iT4hvjWNVmwXih77A1cr89REMqP5NJTn_c05lHPgZbUXJ6cu7wa3VO6uMSEmGE0v4mzTgEjdVIJRKn0CDzGn-qMmuZsL-M84VfNLGdqQTgvAHOF8q0wv2ElE4ZbEpzN1EZ5-hXoxhzsrUOQ5lKHaTo1DVWSKQBUQPtS_roCw_91Z80CGTzT1UaJTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b7e22d39.mp4?token=j_fYjXbFEDXe4V7czNN_gJyejrcG33OdsGAsZVXMKTSigtnraMB9AhlDE1b9GgW4VyPLXnt8ErXOxwl9vV9YK7--3ur3eW3OyDSvm5cvasX-_PzBc3iCAElM2nanc__PjKEYabfVlNO9WBmWkBIrpqfKvS07iT4hvjWNVmwXih77A1cr89REMqP5NJTn_c05lHPgZbUXJ6cu7wa3VO6uMSEmGE0v4mzTgEjdVIJRKn0CDzGn-qMmuZsL-M84VfNLGdqQTgvAHOF8q0wv2ElE4ZbEpzN1EZ5-hXoxhzsrUOQ5lKHaTo1DVWSKQBUQPtS_roCw_91Z80CGTzT1UaJTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عربی از تعلیق پروازهای فرودگاه جده و ریاض، در پی حملات یمن به عربستان خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452404" target="_blank">📅 10:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxAw1Yy_nPiCdLKdlENH--V9DJWrhW5ODyHytRB7jPsF6g7iGdmDA6-Kplfl1_fgJU-_mQbbsRA-EsbinQyxsyJeiP8jYEwYgCDdoj2awuuEuepbtn21nrWlseR_5-m0MQWSBW1_e076o4GF8TUVnsqXyIxJelw3remMcYbUgylMbEOng9_vkkrF5nCcF3p5mKquQCj-j6K4PY5hf2GXi5Ky8SUxsB_PvRBs43mKStXKoAz-2vxwNj3eOtyhUkSFT3FXRykik0iOoHWeb4YSS4_ByPo-VH8sRekuWD98St0VGFMFN2f9D4UURf0hs1MiJqt44BAd_UyFG1sJAFG6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: تا به امروز یک میلیون و ۳۰۰ هزار نفر برای زیارت اربعین در سامانۀ سماح ثبت‌نام کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452403" target="_blank">📅 10:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c3d1583f.mp4?token=NrlA0-7DrWpURtYsmu5NQRbVdLLCOjMwMgjT8TKwjG8yWJIldQRBlReI1zXZIStf_2W204cIyOBg68TaI1kyjqgCMxZ35AdZn-bMx1ozB33yDun720K_0vW1KoF2tgRd5e6KJ-vfTYXLBWpjvtIE9n-tzGhBzSreSrkLqfNYSkmsoawVNAb-Z2yrMBwfOhke9RLR-_X5tSs_3yMeNZ9Rl0SrRA5KoIxiR-WVjAty9NZ_208rXgj0WNo2WhqzfV7STviApby9b1AC1TkV_Yxg7PZkpMkUmT_hvnTalXveNyqnuOeR10HybqIU0fdAI3eRuUPs1v6fBn2RwCsshc-XQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c3d1583f.mp4?token=NrlA0-7DrWpURtYsmu5NQRbVdLLCOjMwMgjT8TKwjG8yWJIldQRBlReI1zXZIStf_2W204cIyOBg68TaI1kyjqgCMxZ35AdZn-bMx1ozB33yDun720K_0vW1KoF2tgRd5e6KJ-vfTYXLBWpjvtIE9n-tzGhBzSreSrkLqfNYSkmsoawVNAb-Z2yrMBwfOhke9RLR-_X5tSs_3yMeNZ9Rl0SrRA5KoIxiR-WVjAty9NZ_208rXgj0WNo2WhqzfV7STviApby9b1AC1TkV_Yxg7PZkpMkUmT_hvnTalXveNyqnuOeR10HybqIU0fdAI3eRuUPs1v6fBn2RwCsshc-XQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمای هوای مرزهای اربعینی امروز چقدر است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452402" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnf1yO27lOSn5rIz8RrqwE15W6CmtxZI0lBuIb-QVp6PMQvy1fhw4zodWVgLuub9DZVgFm_qABHPunN6BcrqXvNRoYVE7-3RZ582bVst8HqU1NM1WVAkP0XcDkwV8GqpZtxSn3Ss49sS-60ym0gqE_CSzHbXORny5RLWhFmPpfxFiUGkI9pcrCvPlARRk4TSF0ML0V71sOBa-5egRiDhjVCUtw0RhhtgIIa5kOeh8O9WutBJAy7pPi3e3HjA_Y-D68QFI5gBI-K8dKyP9f8Qv-kkfCrh-tRdTIL8DA4ca_wmtragXMmK82qbR9VdTEgrEdnCSM4i_BK1BK1rtsEolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ستون‌های دود همچنان در آسمان شهر جیزان عربستان دیده می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452401" target="_blank">📅 09:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773cf754d.mp4?token=QULNmRt_Vb0CNW95M4EYooG9G17AtuAC1z4XnrFGQzjHwn_qKFUQANHhjGPJDcFFwuFgyW72ZX6M3HcoTfZajSB48jbkzE2QfetWcLu6SJ-FVnXcYP4BafPm_WhaVEkxUnvDDk_KZxvTVVAH61gS96dhXe4OgZhD3co567w2a8iW5OMWt6VtIg8gMQCGbDFsJ6mZpsEJRoAu546mD_mw_5qdpI64LYYYk3g-_jlXrtNBCQ5mrEa15GpEsmmYvIVB4qYFvnHfb3Epjx_vGtXbjqTbvkXRF25XYW9IV3QCrcSLkeSm2KCXnadiAzo1xLccjBXu4xumE0cmdzZFidtDdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773cf754d.mp4?token=QULNmRt_Vb0CNW95M4EYooG9G17AtuAC1z4XnrFGQzjHwn_qKFUQANHhjGPJDcFFwuFgyW72ZX6M3HcoTfZajSB48jbkzE2QfetWcLu6SJ-FVnXcYP4BafPm_WhaVEkxUnvDDk_KZxvTVVAH61gS96dhXe4OgZhD3co567w2a8iW5OMWt6VtIg8gMQCGbDFsJ6mZpsEJRoAu546mD_mw_5qdpI64LYYYk3g-_jlXrtNBCQ5mrEa15GpEsmmYvIVB4qYFvnHfb3Epjx_vGtXbjqTbvkXRF25XYW9IV3QCrcSLkeSm2KCXnadiAzo1xLccjBXu4xumE0cmdzZFidtDdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسعود ده‌نمکی: پیکر اکبر عبدی روز یکشنبه از مقابل تالار وحدت تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452400" target="_blank">📅 08:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlZndTrPSwQqTAYB5eDSqsp8OD4wsIQUDEk3YwCgxm1Bnv_O6NFtNSfXn7zzqUcl2gQE6E2gicDi_PfjsueMWciakBTmTqQi_Um-DpF45l7lqprsxYPjxjkf4ppQzG2FkaAjPezuAH-R4-hQmjmTgPiGJHZ8CnFuLutSP7p1Vjg0IHHI4MToEofuEjV3ieRSUAZ2-hfqHt86Zk4f2pFJlepsi-F-6oX_rAXNjLiPYRBuxCohXyX2idTyHjsEAdvCUcTa049KapOMG7PFbvN4rcGb6o7AhB-v01LLP14NyWz1Rqxiwoe0w564fRKebnWSE89e-IwbI53i54DcU02rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح ضربتی پلیس برای برخورد با تردد موتورسواران در خطوط ویژه
🔹
رئیس پلیس راهور پایتخت: طرح برخورد با تخلفات موتورسواران در خطوط ویژه، از امروز در خیابان‌های آزادی، انقلاب اسلامی و ولیعصر(عج) از میدان منیریه تا پل پارک وی در ۴۰ نقطه اجرایی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/452399" target="_blank">📅 07:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
منابع عربی: شهر ینبع عربستان دوباره مورد هدف موشک‌های یمنی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452398" target="_blank">📅 07:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf62abd56.mp4?token=oz2oSEKgQLbQFrvxkuuW-J4WY7Wbzi2hjwM5FMaT6xU-CdQqIX-QtR2v5ZfbIeaWWUpIZJCWrrFeqBVMCLlclR2XnCourSVaICHQXGPXCWswtgPDQqV72Z0NHHnbI02DZz4tmUa-h7wLCUzugyJAdGFTkDaXTByVpz8nF0dgBNEQw1ndZdf1vMIND2mQc5twemkj1xVnq_O36_lPcn048CkENst8fRZt1ZUgmSKRcocy8MUoaZkyHrga9sWO6Wayndal1K3ZyfrcPbu4XQzRD0T7MN5Fav9gFuHaKXZ51z5PxVXy4CWHquOIdMjoU39nmUVVvnfK8d7vhrgtUu6EIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf62abd56.mp4?token=oz2oSEKgQLbQFrvxkuuW-J4WY7Wbzi2hjwM5FMaT6xU-CdQqIX-QtR2v5ZfbIeaWWUpIZJCWrrFeqBVMCLlclR2XnCourSVaICHQXGPXCWswtgPDQqV72Z0NHHnbI02DZz4tmUa-h7wLCUzugyJAdGFTkDaXTByVpz8nF0dgBNEQw1ndZdf1vMIND2mQc5twemkj1xVnq_O36_lPcn048CkENst8fRZt1ZUgmSKRcocy8MUoaZkyHrga9sWO6Wayndal1K3ZyfrcPbu4XQzRD0T7MN5Fav9gFuHaKXZ51z5PxVXy4CWHquOIdMjoU39nmUVVvnfK8d7vhrgtUu6EIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ منابع عربی: یمن، یک تأسیسات نفتی متعلق به شرکت آرامکو در منطقۀ صنعتی جیزان را هدف قرار داد.  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452397" target="_blank">📅 07:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">منابع عربی از تعلیق پروازهای فرودگاه جده و ریاض، در پی حملات یمن به عربستان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/452396" target="_blank">📅 06:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه‌های عربی:
چندین انفجار شدید بار دیگر عربستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452395" target="_blank">📅 06:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منابع عربی: انفجارهایی پایگاه هوایی خمیس المشیط عربستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/452394" target="_blank">📅 06:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه‌های عربی: موشک‌های یمن منطقۀ «حی المطار» در نزدیکی فرودگاه عبدالله عربستان را نیز هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/452393" target="_blank">📅 06:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
رسانه‌های عربی ادعا کردند که یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/452392" target="_blank">📅 05:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv3nrgP08ISQ2TX1qb9UfW2dD-rGQt9c-vd-MBRZgD2IZ36-NbPDkwk2DDL0eVazv9pGiHh0jpq6iAyBY9Z0qFJWnYgv5H44DmAOF10mxK13oJm5-sRuECtdYGHO-ZZ5Olx4x_zay-nDDXLlAyudr3lrEzGcQTq_tPL_SCV2uaHnjJB67Og5AoukzBpGrWXwuXLfX1a7AKZ8Y_-JmEkOAY0u15-Gg2iBT1e2lKvtdgZAkYtYXkFUZsnw6hC6cU4QXt3MufaAWqgiiq2MxWM0epXSwRQR9SKeAeTfF1t1rowgqNboDlQnR-CUQ52iek22QxukMh0lR_B-z4QzFqdTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c019742750.mp4?token=XoaB2zISvPc2Dgl9Na-zM8u8KvzJQqf1Qj-eNYSkrQY-gWCl_dA0IkZ81JAZH6r70SGY9TxEggJzPV92yGqwYdhA6ZHHatT0kwGy3RumBEHEXmJP2JGtzkzOejH3Ou06DlDV1uVunRWjtR7x3aaB_v7zxMz7hcWPZ-5tOE20nbVW_0IeOG3NPEUOz2jl3SPoJ7ade2VHrt1WDYE93QOVUiGOk5V-mltEsKk8ZCvvfdMj9xVS8NfwT63hrxsdCEd9-Y4yqahulJ_89RrJp-rPO1lLjP2aBXg_x77MPIczA7YWyexmKf_Ky0W-9Db8z297DWHzQ_tld2GVgHzx-nHr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c019742750.mp4?token=XoaB2zISvPc2Dgl9Na-zM8u8KvzJQqf1Qj-eNYSkrQY-gWCl_dA0IkZ81JAZH6r70SGY9TxEggJzPV92yGqwYdhA6ZHHatT0kwGy3RumBEHEXmJP2JGtzkzOejH3Ou06DlDV1uVunRWjtR7x3aaB_v7zxMz7hcWPZ-5tOE20nbVW_0IeOG3NPEUOz2jl3SPoJ7ade2VHrt1WDYE93QOVUiGOk5V-mltEsKk8ZCvvfdMj9xVS8NfwT63hrxsdCEd9-Y4yqahulJ_89RrJp-rPO1lLjP2aBXg_x77MPIczA7YWyexmKf_Ky0W-9Db8z297DWHzQ_tld2GVgHzx-nHr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رسانه‌های عربی: در پی حملات موشکی به عربستان، برق مناطق مختلف شهر جیزان این کشور قطع شد.  @Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/452390" target="_blank">📅 05:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ رسانه‌های عربی: در پی حملات موشکی به عربستان، برق مناطق مختلف شهر جیزان این کشور قطع شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452389" target="_blank">📅 05:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
حملات موشکی یمن به عربستان
🔹
رسانه‌های بین‌المللی از شنیده‌شدن صدای انفجار در عربستان در نتیجۀ حملات موشکی و پهپادی یمن خبر می‌دهند.   @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452388" target="_blank">📅 05:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbbaa84cc.mp4?token=Ok5V6meQsi63N4zvCtXYZ8A254ITe804u-gKBIjiSnTlhqvJViwYhyjUtuc_NITXTm3i881vHvjCMgIv-F9dfGvFpcr52PnlS5tEkrQVN42w1RFTe-B64xUddlHxVOLYotJtFRqdD1dzUacG-PPTcqcSzXNgsCtrs8fntWWErh5umEyprtxc6UrV7pMLVSwr8bHIFleLVQyh9pzyJ_eShxxrqivmomtk0wn6nqF-NLNIMKYnTlmXf44QEmYp5MgzK7ths0CM99pDYQkhjjK9vwgRhAOE01cl7yllRCgq3j0uALLGCpBRY1BOakueGEM-N7c_Au4nyrXHm2tWF5CkBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbbaa84cc.mp4?token=Ok5V6meQsi63N4zvCtXYZ8A254ITe804u-gKBIjiSnTlhqvJViwYhyjUtuc_NITXTm3i881vHvjCMgIv-F9dfGvFpcr52PnlS5tEkrQVN42w1RFTe-B64xUddlHxVOLYotJtFRqdD1dzUacG-PPTcqcSzXNgsCtrs8fntWWErh5umEyprtxc6UrV7pMLVSwr8bHIFleLVQyh9pzyJ_eShxxrqivmomtk0wn6nqF-NLNIMKYnTlmXf44QEmYp5MgzK7ths0CM99pDYQkhjjK9vwgRhAOE01cl7yllRCgq3j0uALLGCpBRY1BOakueGEM-N7c_Au4nyrXHm2tWF5CkBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی: بیش از ۵ انفجار ناشی از حملات موشکی، شهر جیزان عربستان را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452387" target="_blank">📅 05:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📷
دیدار عراقچی و لاوروف در قرقیزستان
🔹
وزرای خارجهٔ ایران و روسیه در حاشیهٔ نشست شورای وزیران سازمان همکاری شانگهای در قرقیزستان با یکدیگر دیدار کردند. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452386" target="_blank">📅 05:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
رسانه‌های عربی: گزارش‌ها از شنیده‌شدن صدای چندین انفجار در جازان عربستان حکایت دارد.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/452385" target="_blank">📅 05:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عراقچی در دیدار با وزیر خارجۀ قرقیزستان در حاشیۀ نشست شانگهای: جامعۀ جهانی باید خواستار مجازات جنایتکاران آمریکایی و اسرائیلی شود
🔹
جامعۀ جهانی باید با درک پیامدهای خطرناک قانون‌شکنی و نظامی‌گری آمريکا در منطقۀ غرب آسیا، یکصدا با نقض‌های فاحش منشور ملل‌متحد و حقوق بین‌الملل مخالفت کرده و خواستار مواخذه و مجازات جنایتکاران آمریکایی و اسرائیلی شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452384" target="_blank">📅 05:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عراقچی در دیدار با وزیر خارجۀ چین در حاشیۀ نشست شانگهای:
ناامنی موجود در تنگۀ هرمز و منطقه، ناشی از پیمان‌شکنی آمریکا است.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452383" target="_blank">📅 05:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
رسانه‌های عربی:
گزارش‌ها از شنیده‌شدن صدای چندین انفجار در جازان عربستان حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/452382" target="_blank">📅 05:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452381">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1tgrWBfODJOD6lSrv03Q9yNiK_l6T7aNkjUWTuFqi0q_k_Cos2OaLbBJcqIoI0D-QU55iIjGNeTG3EFwdMlhr6XMKpWNGdvacHIa7yTrwPXsi8x-vC3D8NwJlFm3zJiZtn0zP9RUov6JUGHbXhlf5GtI2sSutJMzRfJaz-ri3HhufZAo5unCJDjIuzyTwEfZW4ZYhRSe2zN03WCLmoo55aXxt5caQCDgPoV7wpwuVIog7zaAsMHYFlqNQMsGStLiuG1OY096Vhr5WP2mH39lnFd2t-fMCZQ6nDpePga-x0SO6OFfi_S_0-6gjI9GwY_3aoprUrKuWd7znudhebdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باب‌المندب، گذرگاه حیاتی کابل‌های اینترنت اروپا و آسیا
🔹
تنگۀ باب‌المندب حلقۀاتصال دریای سرخ به خلیج عدن و اقیانوس هند است.
🔹
بیشتر کابل‌های زیردریایی که داده‌ها را میان اروپا، آسیا و بخشی از آفریقا جابه‌جا می‌کنند، پس از عبور از این تنگه به کانال سوئز و سپس دریای مدیترانه می‌رسند.
🔹
طبق گزارش‌ها حدود ۱۷ کابل زیردریایی از این تنگه عبور می‌کنند که بخش عمده ترافیک داده بین اروپا، آسیا و آفریقا را جابه‌جا می‌کنند و این رقم معادل حدود ۱۷ درصد ترافیک اینترنت جهانی و بیش از ۹۰ درصد ارتباطات اروپا-آسیاست.
🔗
اما مهمترین کابل‌های عبوری از باب‌المندب کدام‌اند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/452381" target="_blank">📅 04:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452380">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1877ec5443.mp4?token=OltqucPZaZiQPge4mHQuhgnoXj7vHKBMZQVnUDmoeqn-XWI-9n4cVRcStoA0QsB67kC28dqixCAyDrbONvkSCT39Jr8E8ksrJYHBYb63mZUYBzcb3EcyUujqfXCq4id-SKtboHa7yFG2tZD0B5l-QoydLZ18ahE3olnRWYKy1NRTCnlgLayxap3TWHSCa9Iwv5aPi3E7f2ee_BXNvOfUYX9OKH9eD96tT8aBAUr4vhXqNF9AJIDYQ1P6aHZzBl8F7BH4-roi5_JKqJpzr3i7kzuP6Jh1Y3_vLT0mkb28xo6bCdVOFKxJkzlVBeJ3xvT7uyXEhFPP7Up0L_ji3oaJYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1877ec5443.mp4?token=OltqucPZaZiQPge4mHQuhgnoXj7vHKBMZQVnUDmoeqn-XWI-9n4cVRcStoA0QsB67kC28dqixCAyDrbONvkSCT39Jr8E8ksrJYHBYb63mZUYBzcb3EcyUujqfXCq4id-SKtboHa7yFG2tZD0B5l-QoydLZ18ahE3olnRWYKy1NRTCnlgLayxap3TWHSCa9Iwv5aPi3E7f2ee_BXNvOfUYX9OKH9eD96tT8aBAUr4vhXqNF9AJIDYQ1P6aHZzBl8F7BH4-roi5_JKqJpzr3i7kzuP6Jh1Y3_vLT0mkb28xo6bCdVOFKxJkzlVBeJ3xvT7uyXEhFPP7Up0L_ji3oaJYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مومن شیرین گناه نمی‌کند!
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452380" target="_blank">📅 02:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452379">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg2QVyI6xoV-WgAC2wRlNWJsPD3NoeTEFQL3og_XA90p4apzRS3CZhYB7KD9Mj0aMs-RFq3DCPXhO3nLbT6aCxkHiTcbhCVCWZqE9hP6dYmmTq8F-k4bzcZAvOM7xRHfSIYS-M9Aa8ivNCIuggARZroglO8O0--fmB4KPhzZFvJKCIkWxQu8iV8ZLxeFdwVE62scLgj7vECjz3L7YcwbkXcZxon5YlNdwnVUyRFcCzA_Inp3LMnJgUsvPCo1aMoqoK0LwcLn9gLKUO1GPfxWN0Cvzbr8a9XFSPamBuHtSG7a0nk3uSqEQbVzwOKwfYFot_PM_Mbqroqgdaj1gjpeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومینگ ایرانی یا خرید سیم‌کارت عراقی؟
🔹
با نزدیک شدن به ایام راهپیمایی عظیم اربعین حسینی و آغاز حرکت میلیونی زائران از ایران به سمت عراق، یکی از مهم‌ترین دغدغه‌های زیرساختی و رفاهی زائران، چگونگی دسترسی به اینترنت و برقراری ارتباطات تلفنی است.
🔹
همواره یکی از سوالات پرتکرار زائرین این بوده است که آیا برای تامین نیازهای ارتباطی خود باید از داخل ایران اقدام کرده و بسته‌های رومینگ اپراتورهای داخلی را فعال کنند یا بهتر است پس از عبور از مرز، یک سیم‌کارت عراقی تهیه نمایند؟
🔗
فارس با بررسی تخصصی، مزایا و معایب هر روش را مقایسه کرده است؛
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452379" target="_blank">📅 02:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452378">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حملۀ ارتش تروریست آمریکا به یک کشتی
🔹
ارتش تروریستی ایالات متحده اعلام کرد یک کشتی تجاری دیگر را که مکرراً برای شکستن محاصرهٔ بنادر ایران تلاش می‌کرد، زمین‌گیر و از کار انداخته است.
🔹
طبق اعلام سازمان تروریستی سنتکام این دومین شناور تجاری است که از زمان برقراری مجدد این محاصره متوقف می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452378" target="_blank">📅 01:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623461967c.mp4?token=V6ent683uljUt7rVdT_BFgnXI_ENWP7bZKB4KqCOalkv0sFD3D61mpa9CQl_nvfZt8TiEvj5DsRQ-OfTdmWV5_qK1yhoIz6gpZdFzrN1qM1qZ4oVd3U1tW5zNt7BLJGphKv_9KBUXSYq4R1vC30KuBngIPn7BiNPlLHGLD6mXvIh6Hk6_lrPh2Y0cSiOCcPdh5Tt1a8GnmuPOO6cwOvjkxkt8Oa84P78N7UFdG8rLKhXItd9wb5yPOBiaLYhf3Bwyx2Oc7xxwJcuMPUxtKe0HbGZf9KVA7GywOwq5AfowuOeP_jyntIP29k0Ii3vHaox_Uf7eon22mr8HFMaE3EFPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623461967c.mp4?token=V6ent683uljUt7rVdT_BFgnXI_ENWP7bZKB4KqCOalkv0sFD3D61mpa9CQl_nvfZt8TiEvj5DsRQ-OfTdmWV5_qK1yhoIz6gpZdFzrN1qM1qZ4oVd3U1tW5zNt7BLJGphKv_9KBUXSYq4R1vC30KuBngIPn7BiNPlLHGLD6mXvIh6Hk6_lrPh2Y0cSiOCcPdh5Tt1a8GnmuPOO6cwOvjkxkt8Oa84P78N7UFdG8rLKhXItd9wb5yPOBiaLYhf3Bwyx2Oc7xxwJcuMPUxtKe0HbGZf9KVA7GywOwq5AfowuOeP_jyntIP29k0Ii3vHaox_Uf7eon22mr8HFMaE3EFPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عربی: در پی اصابت مستقیم موشک به پایگاهی در بحرین، ستون‌های دود به آسمان برخاست.  @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/452377" target="_blank">📅 01:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
منابع عربی: وقوع ۳ انفجار شدید پایگاه آمریکایی الجفیر در بحرین را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452376" target="_blank">📅 01:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc835bbbb.mp4?token=I5ei8PjxCM-sHvDyCwL_LCcvEruzvLOCKijJibPbHfIh8NA0tFbz4-8EqJQ_9wn6W9OP_UZbzQP2FI-QX9OSHppF3sf48x0H6YfSxchgDAxVp-oUtZwDC_9hasWrKRTP_ebPgzygSDVeJ6iLwqTSHWCDx-RMsZmbhrGWzvo70ZSJf5m63fVSgnY2BzTwcQKPtlNTqnigdeMmNx--w9_u1RTsTQaOk9NuwbIZca3E3DStv3U3z7IjE_4QyRqwwHQijLEjv0w_CTlS3MxpBaIDboCgyGX66HtzX_6HM7pcO0sgkhzBVtdSDfPOWPOKwDfPv_adveyN1ZpRKiGi-msijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc835bbbb.mp4?token=I5ei8PjxCM-sHvDyCwL_LCcvEruzvLOCKijJibPbHfIh8NA0tFbz4-8EqJQ_9wn6W9OP_UZbzQP2FI-QX9OSHppF3sf48x0H6YfSxchgDAxVp-oUtZwDC_9hasWrKRTP_ebPgzygSDVeJ6iLwqTSHWCDx-RMsZmbhrGWzvo70ZSJf5m63fVSgnY2BzTwcQKPtlNTqnigdeMmNx--w9_u1RTsTQaOk9NuwbIZca3E3DStv3U3z7IjE_4QyRqwwHQijLEjv0w_CTlS3MxpBaIDboCgyGX66HtzX_6HM7pcO0sgkhzBVtdSDfPOWPOKwDfPv_adveyN1ZpRKiGi-msijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انصارالله یمن ویدئویی خطاب به عربستان سعودی با عنوان «تنش در برابر تنش» منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/452375" target="_blank">📅 01:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPX6RK93oWpjq7ZCoAUxtAPqw7ehgvrso2axvY-bMSXdP_FNtVrcgmSz0PMnS6zauugbws4gxQL6RrxpLjmcM45ZvrXHZyh6hXvUbWNhxCLN3I2iZChil1wKWh4la0myc26tX-2MOl88-PPiJpFTOhuyA7pajS5wzYL8QBymIamnE-6IVgFhOQ_xf-S8Oe_-aqLgMShSRO9uqgYlHx9T8TvjPGpdHQ3o-kVCFDVe_Zey7wuU4PR-OpZE7CR2J25QM58fOs3f6-XFJyo5fZlb2bnBiLYXE-dh5YM_zIsdQHMHvsXIfQG8V9LMkeh96lKorQkhW9-PS_akuA2gWpyeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین دستورکار صحن مجلس پس از جنگ تحمیلی سوم منتشر شد
🔹
نمایندگان در روزهای یکشنبه، دوشنبه و سه‌شنبه هفتۀ جاری، به بررسی لوایح و طرح‌هایی از جمله لایحۀ مقابله با جنایات بین‌المللی خواهند پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/452374" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/452373" target="_blank">📅 00:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452369">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_jmcs43YlAeBLI6-Pg2dCKYthbovUtI0mCTMoSf42AKHDD68h44BDOvFM7zOg2dldRTW1Xzv4WLisZqfAUG1XBRLfMF1UtYUt_sWMlNaJ20pKDORSytHHhgQFZ4lucDLJfF0vgxtXahk3tFrb1-Egsmgh_Z3eSNsCogN0MV96clerqxX_tf2BxJFa1GL_Gc34bn_ifH3NnNzVTO5_yPd0kYnTcGgJF7JqUdiq8xDjmeGlXt6tNtiPcL4UH0Mu3t6fkJX2FDfaRZHvWJoAKT7ES8F4w7m35IQVplhK23nBVy6OYWJzSQESZlImWS2cIfjDJOaPqHIZGeEyHZr3ArMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9iecZov4pFtyLn6q693P2y59XtCPscX_7cirQshR2JebXmtsIXR717kugNyVFUiE7mCWawXaT12AMMc3MFbdEgJJVFlaNWB7vhk51ciWTnlYUTAOFf7rdzHwFvtsbj3jNNQj2InPI0YodqXFkRsvAlgftkGkmg-dPXf42JenYlYbQg69NaQakolaVOQL78Ehp4fFiOSy2b0yYs1gko8cuscPRtD-DNel79Txb_2xA0Q2rl5Jf1n67BqwmfXOAiqW-nkmLTBd_2d9PF00hcr9xmCfqYjnxRQ3_FxFEwq-YATwwyo0BFQygwYexnLDW5BREetqfui7kuZR7DVV_o_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2_jFInNbGp2KPBZnl5lSomJfEBv6jjC5MhZfMgH-zQS5VpLZ_gc0i6Ro-jJGC0_ZpzksAd2gp1XIn_kBnWzNnUUSDhcpc5hf5k1h-W1Y-Cph_2CmGMXLQayNqLI9pkjdF8L7nqyXV8wIikahBY2tRtMWop1wCG-6Ph6zXp1H393q96hazljZpEroCdV-yg2ahawA_s3GErE1UXhOySWbI8QWUcQzxYE_RmhvGvxvzKXvQdiRWhO5Da6YBtgP0OQPVjokaGDywKMb0Phk1-Lt41vCdxxdoWCRJaiWv38BU6P2U0TiaEPogc8VT5ILjo4ke5dGjeCpFa6djU_RYPhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GylwRkX7HOqehhgnT7BvxoQeJhRfDJFUKDYz4EDZgj0_MKcBtE3K3f6iiTXZmwHJXlnOoi6qvfI_1y6rf2put_ORhe3pO65dA_9GGUFSzy7kdKPLvMAG-GIfW0bDzz9vqRjqku5HyJCkIItj7QEb7lD2ckyr42ltE2b1tDSQaypEwSxeAKSwd6r6ujH5SWhWXqw7VEZ5yrMyyFOarfJ89n8Lko4PgShGFXDj1eBxBwfUkfkPL47eyBZpdKM4p4uuD-1TVB3gxIhmetwIHSVTedJstyXYtupB6obVsSguoKpodwx_pJMJsUKrZgMd0d0il0rCfkEIwKn1zgeNLEFNaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۳ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/452369" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452359">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyjjcEvWOSuJGtOF32CgakZFrTJzW2R7IGtAl5NcV6IBHKxeHXuOl3ZOsuCSLBSUzXl9rmcdq_c6OalyjIlWBFaer7fAFEB5x08gegUSw5YisZbE1HXe-RJxLbFqVg1U7qJvvZIRVG2H684ABPAQjo05xqvYypMaq8ZYomQHVv306J_KGKbliEYl5QavWyw74k-M3rTGg1LNMnx9MKfA9DUDO0HpQSi3z-e8iqKzTyR9UBZz0ZkMpYN1V4iRgiv6FO8kPymlLB2mj35-8qj2QYxA_cKXqC__uzh_5ibUPVfWpaeZI1ZUgF_glYdMGisVv0C1j7vBBzUQC1y53paxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyDAgvceJ1VCl36FvZYyrbs_eSFzMRTfplcRtknQOOlG7leDJNUSr7gMRclOXQgT6bPWM-hDTU6LJl0tnEahs1AGiASwPFH4eLfv4taBvXhppjGKllU2Szq9Ljxhtm2zRDVDczpz2WsaIYKkeyHp8MM5MXzcwoR7FLCKMI64bLsGPMx8Q0sawdrqLjh0Pm-ousIhRcuoZkxptA0QDpLbJbu9wAW3Jr0Ej0rhMOHRy-ePI7gn_oGCcawDQXRuSnHSN9YyK34vI_FF_6rZrJ_2k_ne6VYKmCtxxrbaOIg1fDR3fzkbiB9rxumuQ6ngw8uU77nGi934WTpCsyCaU-ZDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYF_-s5oUWfPfs8w8_0Gn_vvnYwq7-HSs1VWL8zW6OGQL1pYKzBiCdQRxJq5vePwt_Skzbd9mI_zwHt8h0jOZu5igcC_55Xv_IflMXmcPg7r5_JOs5OPFduBrz2qiZaz1IJ4nqsmCxNwipuCgr8uVa6bKIXx4xRxCMnzi8Lh6Ndlq5T_H_GWT-hquTa690rGfKIpSTXXByL-lumI69w7b7Zn3nMT87OwuE-XEFtYZAdv3TbBJfoyH5_WbYlSmPel_hHTe6-f2TlsjlRTPtwDCQ1DfSrdZxdwYtikpunJaJ8_uCpTpFArk-1rdIwH-A5kCTLPh5vdZAwMLcosH_hx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BB6T9LTl3_-9ynKQ8veylvrNjqTQr06K_y__DvUmIba8iDb7lpBufLoTAV3UlKtVLJsWAh_AczpbSpf_s3xvI3YxUWdVtzwTdmDGdNUAeNtZsHYZ8_Qi8ePHu9xRjjw7LtSjEZkjCXRSs0qMpxnXFPJoycVsefOE2aPZo7ezz2NUFWxofi7r0N6ezz0TmrJLQXlGllzE4vgicwrnrwyRiba8nwjqIUxo5OEYXrsV2-HnPxTMdCgPalWJ6qnrQ59wM3RSq_PG-F1khnCoLvsLPmFB0ZTy-AgRPSadQ6a8eQJOhqa6EtpMVw80MrHcjALlKtp9Bc7nyXcuQgmF2AKdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgNLCxkWUnevxxdWptP9GGyMeCStygPaBoVlH-0QeIrMisilkjZ1kFZBzHl1_utQN7bGx6EKGgEgzytni6ga6TqgLLYo50HAvmpNYUG9fZz6VbzKY5oUEZIGC6mAS4AB6p-tUXyDHVapnhk_NVMVQY_oi-P3hsRo0_ypF6EpwH9VW8MvjUvu72qvG7WW2PsI0THeP-qUYPjaxeTYGvvwjLYmhKQHPWMIb3BM--4ZlZIc_LGSslKr9w8-yWqkej9oDy0QG3snSn4gMqcgOcB9yLtTkaa9ExTumYpxiredt1EYqob226d9vDkr790XlPv673W4kMjyDJjiDyFBxmJNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aczMpzPGdTcEt3Psw_BNrKmyD0zH8KJYCxpu6gV_hsQTUdKFV4T3aPhyj9Nepituqk8xd9NoanPgTRarXeI9BaADmbPyg9C1190WSETNkxgVjvzply5IjGsPrBtKYDN0Yn_ZQ2SEmAPLJ3bbJn54Uyw9poHKCYn27tOx7PfHhINTfQfs4frApAHqZ0kwuuIQRuSkPQriw3q4Mj1lu1sjUomC5d7oWHxvOqcuuMFmjLZzXnf0mjXrfw5dspVW1rb7fysSpYAN5mjN02UtObTILkx9XX78jY693gNPxA0kS4FlPcxMmQCQxfuewwO5_yL-Yr3TpAHoG3Zvzaj-pmPoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYfUhBYBKcwq6fyzcd8I7Gkb8r55QOqXUIlxgOjK7uS9RsETKo-ZDMtFUNsb2fjuFILiZpLKko622eiRBWuH9ubS8xE9MCkAqg4unFkaiM_ZP-YckzX37LEc9zRI5X3aT6Qwr8-SaMgPx-epXKUHwFGNwoHfg_T0DqtY6vznUmeZCQbPCEpGjngX16ySoYcIQmPdUsAX15UOdnuu9d0svAwxznieRGb7yiuIKSUhXiHYBn8lu9BTcARy6QJq6JspS9A375CioXXAcM7gR3MJTuUYfd1sT6qbMOMSHg06vF-jR2TO8skWl4-K73XTXkojH2gpbmPdl_gm2Bj4FZlJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2zLbFED1-CadeGK-12zUoWX6UB3OkLW3IH6k3PbKd92X44QTes4SKVCakzNp3rQg8ZZ8UZXeL42Vjafq18A_mlpON1YIstKhveZ3fvVSo_vr1cYLg4ABZrYwTE1yncr5RZILGEXzIC8Ft4u8tDutN3aW7rQ0H2_tkVqtzvz6aCxx1O7XFTCw7c-FJCc7ZdkIFCH3a2HeT5dgPSYGet8OhBwX0IFgzNfzGyPbOqDotDbhQFTQ66rqv77kIcTv9ZqQn1BwdXqwL6ldKq-tRsh4RQkpFB1nLsFPnO2vu2VRymm_-UnrQtGD8mbu_gn-4fo0-ozg8PZvYkJYEoxQwtXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2ZVWecewPQf30BO4MSE4baTqG5UCMuoYpEzWqCVa4TeuNHsRmL4wTpteOFCvFNty0bUezOr0HhLdhb2YdrzBazNz0CfZ9KPuK_blrGaAYc-uTAa8j9la861bdNCZkubU6HIGor2F5f-kqCCJfZiC6JsdhkfH_c3nezdCtzQvYXp7AYGCkzBfE3zilYMFKiAFKcm6EaDxT9KheiqMIbTo4hSg28EypTzbIf-zOIs7CTkRjS2M4n-6BTaXpbOUFkLOEfLxGNL_2xPpqb-hz0LoJN_Bvzt45a77AjEbZ1SSZQLIkgx_kfYUxngs8RIImpmSN09UqC3obEB9DuFneMKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYoVdYqNYxzd3j49dXR9DQAEszA5GijVibAWCZHQRa0rMiYMZ9boMV6pMRgRdGCSspTlaj4HRn1U9S8QDW5MrOKvCYV6pjN1L1NzI-hu0mwE1cE1GvvXrd4W22o5-uKqaGGJqm8hqqx0_5MroOUwe1GbZT0_hzauwuaQpFFJDfDTBSjqNpfdYUcYEV2iTAfr_s6MCd_qN-aSA5xRHXSo-zun39EY6dCbTNDdSe0I-KAvQmM3_8V1ec__SX_Sha83CbPqn-bBIuCj9hjFH2XEIXi_Rd_3k1z54soGdflejOcP4RPIntizHcVItwyFpqRGzq6qX2QO2JScvUHqPqRVlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452359" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452358">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار و به‌صدادرآمدن آژیرهای هشدار در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452358" target="_blank">📅 00:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار و به‌صدادرآمدن آژیرهای هشدار در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452357" target="_blank">📅 00:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d0e33dbf.mp4?token=sistrlEs0l0yuMQLiLf9bvJ2KUE1ixNeH1R7GohAl6DzL3w7WKZBNkntCZerwdx-DW_agIW2F8Y-OfVAOT4Hy-NVx4__QQgcayC3UWjU6FEnVt4wYcYjcU3Zm9liz95pKWS4haCmiWGcEEXEwyq3LhuK28pccq6EIddtVSAbz8ocL3J-IWRTGy-7IymnDl8vIFOIvVq-4ardvtd0GJ-T84vTZznFIMPr9SNyInU_Blrm1vKzWRmUsSWCPlhj8XoiGifOHTw3MxHxFjHLUCiLkjCrGo0Otx2RI8lHzhjgFazRNlRi05PW_HVaqElNvlEx8-nopJHqEhfR0dDhVsyTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d0e33dbf.mp4?token=sistrlEs0l0yuMQLiLf9bvJ2KUE1ixNeH1R7GohAl6DzL3w7WKZBNkntCZerwdx-DW_agIW2F8Y-OfVAOT4Hy-NVx4__QQgcayC3UWjU6FEnVt4wYcYjcU3Zm9liz95pKWS4haCmiWGcEEXEwyq3LhuK28pccq6EIddtVSAbz8ocL3J-IWRTGy-7IymnDl8vIFOIvVq-4ardvtd0GJ-T84vTZznFIMPr9SNyInU_Blrm1vKzWRmUsSWCPlhj8XoiGifOHTw3MxHxFjHLUCiLkjCrGo0Otx2RI8lHzhjgFazRNlRi05PW_HVaqElNvlEx8-nopJHqEhfR0dDhVsyTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
«شما از بمباران کردن نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بخش زیادی از جهان متمدن، این اقدام را
جنایت جنگی
می‌داند. آیا شما هم آن را جنایت جنگی می‌دانید؟»
ترامپ:
«من به این سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟»
خبرنگار:
«نیویورک تایمز.»
ترامپ:
«حدس می‌زدم. نیویورک تایمزِ در حال ورشکستگی!»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452356" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فشار ترامپ به کردستان عراق برای جنگ با ایران
🔹
منابع رسانه‌ای خبر دادند رئیس‌جمهور تروریست آمریکا به‌شدت در حال اعمال فشار بر سران کردستان عراق است تا بتواند پای آنان را به جنگ با ایران باز کند.
🔹
به گزارش خبرنگار المیادین از سلیمانیه، دولت آمریکا به مسئولان کردستان عراق هشدار داده اگر با ایران وارد جنگ نشوند، نوع حکومت کنونی آنان (خودمختاری) را لغو کرده و تغییر خواهد داد.
🔹
درهمین رابطه، سرکردۀ گروهک تجزیه‌طلب «سازمان کردستان ایران» صراحتا اعلام کرده که آمریکایی‌ها از طریق واسطه‌هایی با این گروهک ارتباط برقرار کرده، و حالا این گروهک به دنبال حمایت تسلیحاتی، از جمله سلاح، مواد منفجره و تجهیزات پیشرفته از آمریکا است.
🔸
ایران که بارها به سران کردستان درباره آغاز چنین جنگی هشدار داده، حالا به صورت روزانه و با حملات پهپادی و موشکی، در حال کوبیدن مواضع تروریست‌های تجزیه‌طلب در منطقۀ کردستان است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452355" target="_blank">📅 00:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452354">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌ عربستان هدف گرفته‌شدن کشتی‌اش را تایید کرد
🔹
خبرگزاری دولتی واس سعودی نوشت: یک فروند کشتی متعلق به عربستان در دریای سرخ هدف حمله قرار گرفت که منجر به وقوع آتش‌سوزی در بخش جلویی آن شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/452354" target="_blank">📅 00:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452353">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مرز سومار از فردا آمادۀ میزبانی از زائران اربعین است
🔹
فرماندار گیلانغرب: زائران از فردا می‌توانند از مرز سومار راهی عتبات عالیات شوند؛ مرز مندلی عراق نیز آمادگی خود را برای ارائه خدمات گذرنامه، پذیرایی در مواکب و تأمین وسایل نقلیه اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452353" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452346">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUm1_bjhSLTTh-ONTnvMKXK7Xs_5NKv-x0nao_-1lV1tZ9B1RHxZzFQe92-ujxYZIRaLPSJHkd8Uip2qi4ww6IzkrcgQ4EZSHYa_kVnbhH1ctNKQydzdsYEh-PEjYzEP_xFZqmykb3zxqvYcY9TLhpWWvZUX0olinyrpuspwyYSr_AxxdaKyDT_jJhlRSZPWgUq4ZjQMoFp2MVWLy92pwtNdnNOaaicPCv2PXYfVqpqexuVWts0Vm7y81wBaJdbrKGLEI-e_MZ0ElkkKaiLoR4wKsO3R-3zvqResrU1AnmRRFLqrAMB7vOYxdF3KoUqC6BYYRvDVptYHJgFJWoV9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFQ3WSOyCYnIOpYmtNictDWHSaM7yEiVN3Jz5qxMfVw8VoRMLpn0tNaKZSLatQFK5YsiJOLIDusVYVTCovn5JAqb3kZHcvLB-2kE63uK-oxv4j_41hpcgYJ3MM2XtImatdRcEO_08S08KDQopiPBSGe7ZPhW_84ojI9k1IXp_TuJSqwUYOMSYMm4xpByDXc0nI9QrtdHNQplpiFhUx_2HxXFVlNV0QOsL0NmDFYLhcpraSOSA2WBYs1CLiqxC46oKRttTBgL7APxe_dSIyjoGne7uiZDzqm8Dw4nlKP8k5WIF-8H2Ve4OEX4FaD5BAcczO4X5Oejt8FEWvpG3Z1Pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_1iAkab0jh0V0_CaDC-sj-l9PknJRSYCO0bJTzCyd04pVzEYKD9_hFVjcSBL21PIHhB3lv_RW3QOltOCuMyBaqs6xOpvDr5ZG_v03fu5D4kpXbdNCIN8Jjseb7mTiBAM-QGK3M1yD2YfyUo_IoQ71VZZovAzvfMTLIRS1Za6WxTwBzTHqd02YbVFxxp9MOpUkOBkZUoHQGtJU7jUcvR7znAqmU7bu2cibYSXj1zHZE23eOMYsnfxWXoqK5nRHS-wXGTzS-eCK4K8-PJak6af6IY0_LZsNpxgtB5tm8WKgtwf_b6d4FcoNI8q9R9P9rnSA629eoCUDWp1nc9dVLnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKb4DJub7lRv5HzBp-IQlpVc1pexm1ynawgaYV3omtvmlAPKRNWAyEbJ-Vvd8mGGHI7QGtPYAEm2YExsX1u7f2sEw5C9djoXBWOSuDKdADT7Wfb5MVW4C2GHG9jRduo7vAcfXZlgGss0h2WuqzmdJri27UpU7EGlw2wdd01lrkY7obO0rC6pOGsf_axuzjueuu1BfoTJKt2gs9AxdKDFefXhKSXwI0KaMnyvnnbXN9Rp8XwX1dh7BdzXBZScTACVPG_Za8Kon9wsA5SmAQuLWBtX25vnxGmdFd2K_Rqh2RwlZaBgKSD10EOD6GX-C4r0WwabY8XH5_bQIL42POMLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWm4DaAYAPh-NeKpNrnBRif1M26ClL_f57VD81YXKruIrlhpCaZI4V2Kkr1gZCs_dAohuWrxfVb7US30_H6FXA8p4aebs7QTn0qffnE-eBsess5oXtXGUsBSgagXsJ2EXkXmuAjUI8fNCuy8_uPx307ggEgxvsjta7SqVkEXln1viMktBPXrSAe2eOI13BeVb58oNnUkWGMwHwAc5rk1H9Aevk6xOkUpyy4IeiEW_snnQ13M0jBsfZahuzuRO9GvggdQqudLd1dkEhz4dDtn6bpYMFfHA7ysl3bKOENEHyawvrYfVlAslvDh6wmoWHG9tVclPsry23Yepbr3oxHFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMIdAQ7iltbeYUdvJylDcG9DAK7yjcpAiBLS_CCrRZeQawzRbfQ0gVlHjPUoaOCmiQ7hfPms8Kn5v87pA1dVB61eF_g-5JuzOWPRfJJ6piJzUb3x4WdqQGI225AiW3uyZE6E36w6DUlFxhnt6_54ebBVTzFbBVPiYjk8cGEGAqoVpm51YirQC1Ua_SIHR3VyOXvqnbRGFfbb_PjZp0Hk_OSxVqKf9j8SCYZIRm0xE8wqpCBRvq7eLWHenHsBqTpJcSlnAdsskcA3MxTGASvYmHZS86ghUrx9EbtMLtb2loXx472qNhksmJi5xG4fKo_8lnvKma1VMnXh9B25y4CEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPS_qMy_qgE6YUdW7S6HAVYjl2Wvlu4Gg30ENJqdnuydyaLzTrdAsHnnKQ405BkoEEIgXaRTXTmAJ-64StS99iiKqT5BhG5GUFeUNegI6O5dOGe4HUjTc9EAZOjTRJM0lhCIjQe_BzaJKQZib2fa8WKDR1YWXigt-qlI4JdD4WUJPVOy09Fd1_6hCHzcQ8sNPsjGS021cm60Zu4rcxdXTUme4bHL3iDC4YCWgpOtfYM88pMVktQ3BdlzUK5Jp6_DYBCXx4dqBTXXq65lywdU1HH36-wjJGZrBlvbZZ7xXHg3UTeXoOuM732ulpTiE19OgKVXsZshkahjTOnvnxiJPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید امت در حرم عبدالعظیم الحسنی(ع)
عکس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452346" target="_blank">📅 23:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452345">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-text">چرا پرویز پرستویی از پهلوی‌چی‌ها عذرخواهی کرد؟
🔹
پرویز پرستویی که چندی پیش با یادی از جنایات علیه دانش آموزان میناب بر پهلوی و طرفدارانش لعنت فرستاده بود، حالا فضای به وجود آمده در مجازی، حمله گله‌ای پهلوی چی‌ها و ربات‌هایشان را مهم انگاشته و یا برای فرار از دست این حملات دعوت کنندگان ترامپ به حمله علیه ایران و توجیه کنندگان جنایت میناب را هم‌وطن دانسته و از استوری پیشین خود عذرخواهی کرد.
🔹
این استوری در واقع بازنشر یک فیلم بود، فیلمی که به اتفاق تلخ همان روز و پیدا شدن قطعه‌های پیکر شهدای کودک مدرسه میناب برمی‌گشت.
🔹
در همان فیلم نوشته شده بود بر پیروان پهلوی تا ابد لعنت باد، چون این جنگ از همان جایی شروع شد که این افراد از عمویشان خواستند به ایران حمله کند.
🔹
کافی‌ست کمی به عقب برگردیم و یادمان بیاید که همین حادثه میناب را همین افراد در همان زمان توجیه می‌کردند.اما اتفاقی که بعد از انتشار این استوری افتاد، خودش داستان جداگانه‌ای دارد. موج بزرگی از فحاشی در فضای مجازی راه افتاد و پرستویی هدف اصلی آن شد. این را باید گفت که فحاشی در این فضا چیز تازه‌ای نیست، همیشه بوده و سعی کرده تا دیکتاتورگونه نظرات مخالفش را خفه کنم.
🔹
همین فشار بود که باعث شد پرستویی در پستی دیگر عذرخواهی کند و بنویسد قصد توهین به هم‌وطنانش را نداشته است.
🔹
با این حال، پیش از آنکه این ماجرا همین‌جا تمام شود و با پذیرش این نکته که لشکر غیر واقعی و مجازی پهلوی ترسناک و دیکتاتور است چند نکته هست که باید با استدلال روشن شوند.
🔹
اول اینکه عامل جنایت و شهادت دانش‌آموزان میناب هرگز نمی‌تواند هم‌وطن قربانیانش به‌حساب بیاید. این حرف بی‌دلیل نیست. هم‌وطن‌بودن فقط یک رابطه جغرافیایی یا زبانی نیست، بلکه بر اشتراک در سرنوشت و منافع یک ملت شکل می‌گیرد. کسی که با دعوت عملی به حمله نظامی علیه کشورش، در کشته‌شدن کودکان همان سرزمین سهیم می‌شود، دیگر در این رابطه جایی ندارد. پس نمی‌شود صرفاً به خاطر تابعیت یا زبان مشترک، او را در همان دسته‌ای قرار داد که قربانیانش هستند.
🔹
نکته دوم به خود فضای مجازی برمی‌گردد. اینستاگرام، با همه شکل و شمایلی که دارد، بازتاب دقیقی از افکار عمومی جامعه نیست.
🔹
از اساس سلبریتی‌ها دچار این خطا شده و آن را بازتاب جامعه می‌دانند.
🔹
اما در این فضا الگوریتم انتشار محتوا، شکل‌گیری حباب‌های اجتماعی خاص و سهولت ساخت حساب‌های جعلی یا ناشناس باعث می‌شود صداهای پرسروصدا و سازمان‌یافته بیشتر از واقعیت به چشم بیایند.
🔹
اگر بخواهیم این ادعا را بسنجیم، کافی‌ست همان محتوا را در بستری داخلی مثل ایتا هم منتشر کنیم و واکنش‌ها را کنار هم بگذاریم تا به تفاوت نگاه حتی در دو فضای متفاوت در جهان مجازی نیز آگاه شویم.
🔹
اتفاقی که نشان می‌دهد آنچه در اینستاگرام دیده می‌شود، صدای همه جامعه نیست، بلکه بازتاب یک جریان خاص در همان پلتفرم است. در مقابل، همان مردمی که شب‌ها در خیابان‌های واقعی حضور دارند و از محکومیت عاملان جنایت میناب حمایت می‌کنند، تصویری دیگر و شاید صادقانه‌تر از افکار عمومی به دست می‌دهند.
🔹
پرویز پرستویی در پست آخرش نوشته است که به تمامی تفکرات احترام می‌گذارد؛ فقط سوال اینجا است که آیا تفکرات صهیونیستی در مقابله با فلسطین قابل احترام است و یا رقصنده‌های روی خون شهدای میناب هم نیازمند احترامند؟
🔹
به‌نظر جنگ اخیر باید ما را به سمتی ببرد که موضع مشخص داشته باشیم؛ افکار عمومی دیگر پذیرنده حد وسطی که سعی می‌کند هم نظرش را بگوید و هم رضایت طرفین را کسب کند، نیست.
🔹
بازتاب عمومی به این اتفاقات نیز خود گویای همین اصل است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452345" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452344">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی: مقر گروهک‌های ‌تجزیه‌طلب در اربیل عراق هدف چند حملۀ هوایی قرار گفت.  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452344" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452343">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=mc_5P6ixoejHX1YqGbInLBvWNJjix1u58qNyM4FEmcZ-X_H0TyXeYUg1Rv7BPPhtgz2aYfFagQo-Yb36p832rhf8awQJlNrVYUHKcnUC8O93Wi4e62YZC1fFo0EAOQAzcMo3Gva0wxo7D23XaFEQW8s2xh1tTCDMrjjjix29EUDok_AP1CVt8eYqBLyMWuuhsXqt6AeWb1qswKPFEnsO53KStzgidjx7Vdg1j0OBB_ZcT0HgkVpjGcfqb9jKSyZb6dZKod6fGx16ZVRfeEzyXZ4J0NfyjrgNQyMANj__VXjHYK3J0M9lcnam9LvyK5qZ9Zx0SKndevZni7RnZG8Mag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a55e0a0410.mp4?token=mc_5P6ixoejHX1YqGbInLBvWNJjix1u58qNyM4FEmcZ-X_H0TyXeYUg1Rv7BPPhtgz2aYfFagQo-Yb36p832rhf8awQJlNrVYUHKcnUC8O93Wi4e62YZC1fFo0EAOQAzcMo3Gva0wxo7D23XaFEQW8s2xh1tTCDMrjjjix29EUDok_AP1CVt8eYqBLyMWuuhsXqt6AeWb1qswKPFEnsO53KStzgidjx7Vdg1j0OBB_ZcT0HgkVpjGcfqb9jKSyZb6dZKod6fGx16ZVRfeEzyXZ4J0NfyjrgNQyMANj__VXjHYK3J0M9lcnam9LvyK5qZ9Zx0SKndevZni7RnZG8Mag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری شبکه سه: ۱۰۰ روز است که هر بار اسم بچه‌ می‌آید ناخودآگاه به میناب پرتاب می‌شوم
🔹
کسانی که دم از حقوق بشر می‌زنند، کودکان ایران را به خاک و خون کشیدند. ما از خون کودکان میناب نمی‌گذریم.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452343" target="_blank">📅 23:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452342">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5Mt9HID-llMbWglSdNts_JX8EjgpNgB3-stNPm0q8--c7louQkSxL2-_PgcPwnSbHdeQrkWSKfwbLssUgV8swtHboFN4MY4uvBhayr7QJ6lfI9mVJwaAxBBZV3zkvuRVnTIweBr_NUL6QPqR2VXYIGRNR9-KstFb_Fj8RRXf6OH3MdHDQENk4QcOEx24DCGMf_Rr8_yspMBntPqqs0WRALCrAn2i7iUrm63r0zIrx-e0DVZ9Lm0fC5N4vH7Vqicf6s54be9FboGydGBvuHF9hv6PlLcI2YJgHBCiQ8EAjYWzOMzCchnJO9nSuvnSU4OSk_MkhBrGYR98Ycd97VRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پزشکیان: تاریخ هنر، نام و یاد اکبر عبدی را در زمرۀ سرمایه‌های به‌یادماندنی ایران‌زمین ثبت خواهد کرد
🔹
رئیس جمهور در پیام تسلیت درگذشت اکبر عبدی: بازیگر توانا، صاحب‌سبک و چهره بی‌بدیل عرصه تئاتر، سینما و تلویزیون کشور، طی چند دهه نقش‌آفرینی بی‌نظیر، بخشی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452342" target="_blank">📅 23:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452341">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e798b36b5b.mp4?token=C-vmTjOUH65V9iGmzf0GSnTidf-15uI8c5dl1GZ0HOiIq5Sfh3T1zSPXWqMeXgCVSSXogIfuOu7o3W_j934x27Te2DZ-EzJGsD7fOqsttTO8SO7T1kHV-xby8EFhvjLtJr9bPAKc_TrhL8ltT3CMxEnHlJOPB4yINn7kC6hEARZFmje0hyVty3XPK3bEolE0ferF2R7kYIAK1JI6FVu2bzb0DTmJWVM8LqcH70_OKsRfn7m33CjMwjshX6tgLP1ed7L7XNh9bBbqYsnwwBzJmlg4ssyGn-niGINomjLrvY5uY5VIXhuw0azmk1PpvR6gjV5gchDEJ1rMvMSAuH9S_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e798b36b5b.mp4?token=C-vmTjOUH65V9iGmzf0GSnTidf-15uI8c5dl1GZ0HOiIq5Sfh3T1zSPXWqMeXgCVSSXogIfuOu7o3W_j934x27Te2DZ-EzJGsD7fOqsttTO8SO7T1kHV-xby8EFhvjLtJr9bPAKc_TrhL8ltT3CMxEnHlJOPB4yINn7kC6hEARZFmje0hyVty3XPK3bEolE0ferF2R7kYIAK1JI6FVu2bzb0DTmJWVM8LqcH70_OKsRfn7m33CjMwjshX6tgLP1ed7L7XNh9bBbqYsnwwBzJmlg4ssyGn-niGINomjLrvY5uY5VIXhuw0azmk1PpvR6gjV5gchDEJ1rMvMSAuH9S_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان زائران اربعین در مرز شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452341" target="_blank">📅 23:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452340">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaVuw2lkHwhKgYaE2s700Rd-wE-aFSBGDanxRO5rdgXViiZ1iV-ttkf89kFakDr1r7RAipmwzbnfhjj_0tuOgn5zsOp-ZLt6Z1u0V5l8wVQVM4qcSqUwwleVgoAfKnfhdxWyNtpSxrgjwbhGM9eWs4kWYg_gPx0avgeNH0aOBGWY7cEI1LuJmlE0HnzbsR9gI3TUFSKNNiqOUd1C_uXH-tP1dRmAvHLJpguYBDNCLZPa1iXcKbj7IDShCIAhqNNJKHfMnMQwX2GG4PAncG24I3Hj8B4oK0CH6mOTw4TkeiB8zXii5uim5xCzJrOJYaoIRycjUAYqRkWAjJFZ5zhqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از حملۀ هوایی عربستان سعودی به بندر الحدیده یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/452340" target="_blank">📅 23:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452339">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6gidxlsLnFYZSl6nj8CqNn4ApGe87EQnvC9ssan2U0qdPEOgySxqe2sIb3AeQ7ePk6ty2o9q5CrW7Ufg332eFthLIsmItGiN8-9_JTRaXKJ264y8CFhFGvwWoDN04Wl_wTfCeH6dXxWrfkEJU8S-lHKe6tQL-Sq8h0dGSSZqdld9LkanIJa-0kt_dIcSFfVDByRVVnyad_yFHf0LC2x7nGTpV1LT8SS6j3a47XVUlTvL_gGuAWjMpLyt_v5-Y7CiUfSaOZGSnPcCRbSwFuUqDgWEWXOwTRalFOsF8FTltPdPR4zKqMFK9RbaF8N9NZl1f4wPp61WD8YuNCo0gOfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسعود ده‌نمکی: پیکر اکبر عبدی روز یکشنبه از مقابل تالار وحدت تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/452339" target="_blank">📅 23:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452338">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d22d398c.mp4?token=MGrX36ySayATmHju2FXEDPo4qvU6n-QXYGaGLvLOYzJm1JOocsa42KUj0vwljK1IzLCegdxWtYgLvwsFY7ViXaE-odm0NXquNikUsfpL9cBpWnVVuvDKHD-He2CL92j1VMQx6iYFpLr96M1pNJS7pQm2Z_OiFN2ZAs29xvSJuBE013jgMOF5aAwG0dpBGgNy42xYUuaNGNAXgl9zeymBBvEF4jA2fAR2IyUMyhrAmIZdBfp4YGd-dgZFJRJPOUmwg21DVntVCi-zQ6FmN02V6o9oN2wWGXJrmZ2owo76dCL47IK8FdXT82Goq3LHQ585wy-qCRcaJws22B3JDkr3nFN8_5n19V3eWbVmsjD5XpEt805mEWeE6_IOWxu9EAdIP0x949R8rTCWNcmHLYz3rpyPnnVfChbQOXAXavi3TlRifLXfqgNThXRx0mfVHOnoe8zTJGjZZ5c5McTCxpPGLOYbyr94wr7Wh8jwrowk7lNqccyzU89gMUmGFk0sounO6y06UVWjGYK_Cy8MbtQ2atrKoK1SgQoKu_RiKpO5p4P4ZEFOxfkya0cFDakYsaJG2XC-7dnO_HqU_VEmm5-CMfa13UOB2eVvBe_94gcoMrk2EYIQ1FEi8Cb7OVRB_nWp0u6t5HJ_T88omZGt6eSFtDG7xC4A0Bk1_xPM9tQDzJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d22d398c.mp4?token=MGrX36ySayATmHju2FXEDPo4qvU6n-QXYGaGLvLOYzJm1JOocsa42KUj0vwljK1IzLCegdxWtYgLvwsFY7ViXaE-odm0NXquNikUsfpL9cBpWnVVuvDKHD-He2CL92j1VMQx6iYFpLr96M1pNJS7pQm2Z_OiFN2ZAs29xvSJuBE013jgMOF5aAwG0dpBGgNy42xYUuaNGNAXgl9zeymBBvEF4jA2fAR2IyUMyhrAmIZdBfp4YGd-dgZFJRJPOUmwg21DVntVCi-zQ6FmN02V6o9oN2wWGXJrmZ2owo76dCL47IK8FdXT82Goq3LHQ585wy-qCRcaJws22B3JDkr3nFN8_5n19V3eWbVmsjD5XpEt805mEWeE6_IOWxu9EAdIP0x949R8rTCWNcmHLYz3rpyPnnVfChbQOXAXavi3TlRifLXfqgNThXRx0mfVHOnoe8zTJGjZZ5c5McTCxpPGLOYbyr94wr7Wh8jwrowk7lNqccyzU89gMUmGFk0sounO6y06UVWjGYK_Cy8MbtQ2atrKoK1SgQoKu_RiKpO5p4P4ZEFOxfkya0cFDakYsaJG2XC-7dnO_HqU_VEmm5-CMfa13UOB2eVvBe_94gcoMrk2EYIQ1FEi8Cb7OVRB_nWp0u6t5HJ_T88omZGt6eSFtDG7xC4A0Bk1_xPM9tQDzJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذکر یا اباصالح المهدی بروجردی‌ها در شب ۱۴۶
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452338" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452337">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
سنندجی‌ها در تجمع ۱۴۶: شمال و جنوب فرقی ندارد؛ همۀ این خاک، ایران است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/452337" target="_blank">📅 22:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452336">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831aa2985d.mp4?token=oDSENnxKYiI5J7ZH0NOGGD2B07pA2vyErfXvF-q_P6yYTnM-exPfPQ0sPd3pOtf2PFGEznFkNbgcQHZ65-YmvgLRWmvHmhA-7aJspdGaFeZtT7O1KGoy30QYtpkU2yMjCo_3rMpftZrKM9cg5Lydtu7W61LFtzzuPTabwG-p6hvUpNPVpeNTj3kwGpwe8eWHWEVRvw7xQde_xVMTgsYLg2Z_GDFXGe3KlLHoPQuVwXm8Di_w9pz4RfHcZsfViEqYqUjj4StKX6hQC-a0eqZE357Igwg14GUJTidZb-yehAzjfYra0CVzRmBccYS2NYLv-E1Z79yarHsqwD0SBUjjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831aa2985d.mp4?token=oDSENnxKYiI5J7ZH0NOGGD2B07pA2vyErfXvF-q_P6yYTnM-exPfPQ0sPd3pOtf2PFGEznFkNbgcQHZ65-YmvgLRWmvHmhA-7aJspdGaFeZtT7O1KGoy30QYtpkU2yMjCo_3rMpftZrKM9cg5Lydtu7W61LFtzzuPTabwG-p6hvUpNPVpeNTj3kwGpwe8eWHWEVRvw7xQde_xVMTgsYLg2Z_GDFXGe3KlLHoPQuVwXm8Di_w9pz4RfHcZsfViEqYqUjj4StKX6hQC-a0eqZE357Igwg14GUJTidZb-yehAzjfYra0CVzRmBccYS2NYLv-E1Z79yarHsqwD0SBUjjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴۶ شب حضور دشمن‌شکن و وحدت‌آفرین گرگانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452336" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d6c3a191.mp4?token=kxj8dJk2EgwNvlHaP8VIwtj61iNgKcL9gf9wW7BNckeDmH88xSA3iv_qMJ0Sww54EEYl8luhhY8tcXky3vYXm4biOV88fR91yT8IvA5VLnJM8UsdjdVLDBHdQ8jRb0-1WWTxTkH_Orzg_eTG1M4MJ9VLBpPe-UPvoFRbkoD-PBczcU3GpZa5p7bQ1fHujTaxMP-Z0y4KcgyhtxQpr0WIlp21sI1qq3xIqAXwK2WXLviiMY_KK1WcfnaYmqQ-PtHMGS-Ssm44NDAy24RMEkhmOYHWJLnFm4Zac6NDTql1eVyxgZMfYRMitSHjqwsH5VkBF_HZAfBpDliwz-g7lttdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d6c3a191.mp4?token=kxj8dJk2EgwNvlHaP8VIwtj61iNgKcL9gf9wW7BNckeDmH88xSA3iv_qMJ0Sww54EEYl8luhhY8tcXky3vYXm4biOV88fR91yT8IvA5VLnJM8UsdjdVLDBHdQ8jRb0-1WWTxTkH_Orzg_eTG1M4MJ9VLBpPe-UPvoFRbkoD-PBczcU3GpZa5p7bQ1fHujTaxMP-Z0y4KcgyhtxQpr0WIlp21sI1qq3xIqAXwK2WXLviiMY_KK1WcfnaYmqQ-PtHMGS-Ssm44NDAy24RMEkhmOYHWJLnFm4Zac6NDTql1eVyxgZMfYRMitSHjqwsH5VkBF_HZAfBpDliwz-g7lttdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکبر عبدی درگذشت
🔹
اکبر عبدی بازیگر سینما تئاتر و تلویزیون بعد از تحمل یک دوره بیماری درگذشت و مسعود ده نمکی در گفتگو با فارس این خبر را تایید کرد.  @Farsnart</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/452335" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fd05ea96.mp4?token=bHkiqkgVmmNzz8QDp0Z-aTqXnMLNF0Y4Y8Eqquajj1yM_1qD1PuDeIA-x6Dm4BjPmnev6E2EAxE5KAJI8mBxSh1LfsOU5dRCqGA8X21U0UVO_bNCT6fqDG1Z_dVN_DRKUoHyrwulV1-hGP8d0G13YtlO-wvW8GQXm2nSINE0oiASE9DWuKDTYPabcSkep6YpYBAXb0rcs577EZHBxcHd45OVU2MCdyqzvuibKKuH--ljauFd13zZ9CqCHpv_6bTKkMzpK74VAZ005Pc6HdVwUbCdurQOcbyzIGAFPWPgHfNOZkufFRIGWhmsylafawruliP9m4Keje3KM7KcvD6dXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fd05ea96.mp4?token=bHkiqkgVmmNzz8QDp0Z-aTqXnMLNF0Y4Y8Eqquajj1yM_1qD1PuDeIA-x6Dm4BjPmnev6E2EAxE5KAJI8mBxSh1LfsOU5dRCqGA8X21U0UVO_bNCT6fqDG1Z_dVN_DRKUoHyrwulV1-hGP8d0G13YtlO-wvW8GQXm2nSINE0oiASE9DWuKDTYPabcSkep6YpYBAXb0rcs577EZHBxcHd45OVU2MCdyqzvuibKKuH--ljauFd13zZ9CqCHpv_6bTKkMzpK74VAZ005Pc6HdVwUbCdurQOcbyzIGAFPWPgHfNOZkufFRIGWhmsylafawruliP9m4Keje3KM7KcvD6dXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
ماجرای احوالپرسی امام شهید از مرحوم اکبر عبدی
@rahbari_plus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/452334" target="_blank">📅 22:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452333">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک مقام آگاه: عصر امروز ارتش آمریکا با پرتاب ۲ ‌موشک یک تانکر ال‌پی‌جی را هدف قرار داد
🔹
به گفتۀ این منبع، این کشتی از سمت دریای عمان قصد ورود به منطقه را داشت و نیروهای تروریستی آمریکا تانکر را به تصور آنکه قصد انتقال گاز ایران را داشته، مورد اصابت قرار دادند.
🔹
این منبع تشریح کرد ۲ تن از خدمه این تانکر ال‎پی‎جی در پی حمله نیروهای آمریکایی کشته شدند و کشتی بر اثر خسارت در موتورخانه آن متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/452333" target="_blank">📅 22:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksidP7iDz5Um-SB7s3_4hyIJL4QiFBJrEWL35fjJYLgGhRaeXSnuIXjl_SNvg7c5NfAsCYta6UE73mzxw41dlf1XK5MymqEb1NC2K0Wlw_CSt4Hf034Not4IJCG9DBFKsHi_WS7zfm2fTYUNChyjsGfYr25Jy0fEcdRi2gqW2lf96p1IXFqtZyzKCVIfCG0Xkbkw8wH-wP-36ggkdwJmxpUqsq_UJE1I4saRMX9tXjVdP2fW927g39bOX0gL9uhKfwZnSzwQXKLofejWmLjoFCGO7LIzg8IMW8E5Ye_nAuUfjVIBjSnTo6egzyFCl5pqXaOWKFhNfIKiCBD4qMVlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیین یادبود شهید رهبر انقلاب ویژۀ اهالی رسانه
◾️
یکشنبه؛ ساعت ۱۷:۳۰ الی ۱۹
◾️
تهران؛ مجتمع فرهنگی هنری سرچشمه
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452332" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452331">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
منابع عربی از وقوع چند انفجار در شمال کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/452331" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452330">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/220a7c89c3.mp4?token=uhavjfPrIQq_unwP-eFSvWdGfoOzpShTJkaoYyycY4DZ2yjyCN_WfwSJkJrrK-NgfqiPtIzG4nsLGEwPsAwDBmUJ4_uMX2e49y8pzOFepPvA2-WTxttzjmUY8jxZ7fKO5LuEtmkn6m67ChhnyG02NTS-kfpjKQGLVTCmJxa7L1VoJWb53Vd7fQW9M2bwSowXtSgOaTmjNeEB4L3UPqP5jEqd33_sv-qgzvXra1t9AxuYXBWLHQARceqZ2kFTC6lIhORDb4Zzy5CEH8WMTs4ke6kHw4PGac9zUwvJqvmZVf0MqWmwR6-umqVKRwsVBtszDj2zNuFfHDTuuJKUK-HQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/220a7c89c3.mp4?token=uhavjfPrIQq_unwP-eFSvWdGfoOzpShTJkaoYyycY4DZ2yjyCN_WfwSJkJrrK-NgfqiPtIzG4nsLGEwPsAwDBmUJ4_uMX2e49y8pzOFepPvA2-WTxttzjmUY8jxZ7fKO5LuEtmkn6m67ChhnyG02NTS-kfpjKQGLVTCmJxa7L1VoJWb53Vd7fQW9M2bwSowXtSgOaTmjNeEB4L3UPqP5jEqd33_sv-qgzvXra1t9AxuYXBWLHQARceqZ2kFTC6lIhORDb4Zzy5CEH8WMTs4ke6kHw4PGac9zUwvJqvmZVf0MqWmwR6-umqVKRwsVBtszDj2zNuFfHDTuuJKUK-HQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون تجمعات شبانۀ مردمی امشب نیز در رگ‌های ایران جاری است
🔹
قابی از حضور پرشور مردم در شب ۱۴۶  تجمعات  مردمی.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452330" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452329">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4f191934.mp4?token=VByzh0sysFKfvE3zVWB7aRZckJQHN7UJqQCe1z5FRvgQla7H8TPwjzjNXXKKy8l_qYWBr0oKdiy9jy00AboNitCjZd3fPj6zq6S_tDLsoYAb6HN_SsVfCxBNOLgry0R3aFWj_D5QgPpHpZNiKhl6efIga_gcs1HmE5gQ6AohbB_a0sFCZzSitqdqh-OOYKKBUurq0r2kavsHFyFhXxKqxEo5xePdN3qwL4rxLIgXduIaWAbNiKY_DZzOKY4x21MgVRdOQlq8VWWntJRzwT5Xd6CJNp2TEkJvozIbckAgmqNssurWm1MzSqUQe_ftHfW1gyyLVzlK6Kn1y1QcskDCjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4f191934.mp4?token=VByzh0sysFKfvE3zVWB7aRZckJQHN7UJqQCe1z5FRvgQla7H8TPwjzjNXXKKy8l_qYWBr0oKdiy9jy00AboNitCjZd3fPj6zq6S_tDLsoYAb6HN_SsVfCxBNOLgry0R3aFWj_D5QgPpHpZNiKhl6efIga_gcs1HmE5gQ6AohbB_a0sFCZzSitqdqh-OOYKKBUurq0r2kavsHFyFhXxKqxEo5xePdN3qwL4rxLIgXduIaWAbNiKY_DZzOKY4x21MgVRdOQlq8VWWntJRzwT5Xd6CJNp2TEkJvozIbckAgmqNssurWm1MzSqUQe_ftHfW1gyyLVzlK6Kn1y1QcskDCjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ کرایه مسیرهای اربعین از مرزهای ایران تا عراق  مرز مهران تا نجف
🔹
سواری بین ۲۰ تا ۳۰ هزار دینار، ون ۱۵ تا ۱۸ هزاردینار و اتوبوس ۱۰ تا ۱۳ هزار دینار  مرز مهران تا کربلا
🔹
سواری ۲۵ تا ۳۰ هزار دینار، ون ۱۳ تا ۱۵ هزار دینار و اتوبوس ۸ تا ۱۲ هزار دینار  مرز شلمچه…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452329" target="_blank">📅 22:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
دادگاه رسیدگی به اتهامات صادق ساعدی‌نیا برگزار شد
🔹
جلسه رسیدگی به اتهامات صادق ساعدی‌نیا مدیرعامل شرکت صنعت غذایی و کافه‌های زنجیره‌ای «ساعدی‌نیا» از متهمان کودتای آمریکایی-صهیونیستی دی‌ماه ۱۴۰۴ در دادگاه انقلاب قم با حضور رئیس و مستشاران دادگاه، نماینده…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452328" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">✨
خدمت به زائر، افتخاری که با کلام نمی‌توان توصیف کرد...
⬅️
کارکنان بانک شهر با اعزام به مرز مهران، در موکب این بانک آماده خدمت‌رسانی شبانه روزی به زائران اربعین حسینی هستند.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452327" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RcBMmmKhG4g9d4n2kLB1SB_UhSLf4WNgluqmhKEESr_Hbf3i9L9wznXGDpiF9cUJhggVS-CRv7OL6GwSnXfeh-r6C8CCtYzZUiA7iYY-AhOb2FHeRnUOSaHM_HczpYWMbfyHFE4s9nhvB_QNQZTzyuwzOXYLcgnr8gfamf6CXkuf_SZFPzysBrEayU5MhMHq480q84oCg0xaBBrtpdmDxNMQMq5BkENPDsgi6FQWDbZ4GndqknMxEcMwkqvgCl79_4fmDcDiAWPmVCxhZDbD8QY3XxTkXZo3426EHmH85v2ag8OdKC438cPcpbpc8_gmLpdQb5ChjgZxB6ipxigF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
📌
جهش سودآوری، تقویت سرمایه و تثبیت جایگاه ارزی بانک تجارت در سال ۱۴۰۴
✅
مدیرعامل بانک تجارت در مجمع عمومی عادی سالیانه این بانک، با ارائه گزارش عملکرد سال ۱۴۰۴ از رشد قابل توجه سودآوری، توسعه فروش محصولات نو، تقویت توان سرمایه‌ای، گسترش فعالیت‌های ارزی، بهبود شاخص‌های مالی و پیشرفت برنامه‌های تحول دیجیتال خبر داد؛ عملکردی که بیانگر تداوم مسیر اصلاح ساختاری و تثبیت جایگاه این بانک در شبکه بانکی کشور است.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452326" target="_blank">📅 21:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452325">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452325" target="_blank">📅 21:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452324">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc6383dad.mp4?token=bJCvUM7mwz52s5v7brj053iI2-Y6ewPMgMLDGF483hLkjQVdHhGXQZvZgqRgUj14JjEN8LiuesihUiabJbmTuzeLr2aqi6q3ccfRVZKe5jumkGYfep3fcdAlMj5FbxXQqm8G3hpFeIKEo2ra8enuDiAHT_5PkY4zYfY-oOsAr7v3fZCggyNx7sTpA8ALqt0wUdq7vhVq2qRuEXNPpu0qDJ2LSQt8v3GZlo0RxynxEUBhkEL00GiJsJWYMJ-44RoeRJ2QSx4vtSQGgR3MtqefVYBLzW8pPS-6twHctokHXt5IRx3gIe-rZUy4yjwQQzhL7d1bbBVLMhC0OlkwFowXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc6383dad.mp4?token=bJCvUM7mwz52s5v7brj053iI2-Y6ewPMgMLDGF483hLkjQVdHhGXQZvZgqRgUj14JjEN8LiuesihUiabJbmTuzeLr2aqi6q3ccfRVZKe5jumkGYfep3fcdAlMj5FbxXQqm8G3hpFeIKEo2ra8enuDiAHT_5PkY4zYfY-oOsAr7v3fZCggyNx7sTpA8ALqt0wUdq7vhVq2qRuEXNPpu0qDJ2LSQt8v3GZlo0RxynxEUBhkEL00GiJsJWYMJ-44RoeRJ2QSx4vtSQGgR3MtqefVYBLzW8pPS-6twHctokHXt5IRx3gIe-rZUy4yjwQQzhL7d1bbBVLMhC0OlkwFowXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری امشب مردم بجنورد در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452324" target="_blank">📅 21:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0aR98aLeQc2IlKwkGg7gvyQRlh-KtOC9M5thnIuYZv_pGmo2lSPIGZ8zfWHDlaUipgat0rKf-8O1DzkTvqBvPY4PbTb_kqZx09sJoKEbhscRaIjyCehhsnqX_JF1lNx_eBpwtpp0hTQlqcypCPaQyRAgtd1rvRMEIQCSzIU12TzRStwzQT3nnVlqNFtgWtHSqNp7O-48CEzKOX6lH7rNE-yrAOqhLX1eB7tFRnazIJSQPeOOgCdoldDo2EXa1caGmcm8dthlHe7Plybv9qeHlva2ijfT7_Nh1HoN-hBTHCDRCkaRZR2dJfmsEJyoQaCbveve1qpdDTMb-FtnkKkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان برای عبور از باب‌المندب دست‎به‌دامن عمان شد
🔹
روزنامه الاخبار: پس از هدف قرارگرفتن دو نفتکش سعودی در دریای سرخ، عربستان بار دیگر به دنبال میانجی‌گری عمان است و یک هیأت را برای مهار تشدید تنش با صنعا به مسقط اعزام کرده است.
🔸
منابع وابسته به ناوبری…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/452323" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452322">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922e3acbc7.mp4?token=vfqTeYns2tYLL73WNoPWx0nh1-lfOKLRv3YNEG_A4aiAMtBokXGkWUNAxHhy0yZ7ChbCzekf_YOwj1qvAaVrWYo_l2YwgqOIE8sAE6n-niBMmGrpXeEfPYPzwwxxh17Sr2dzfw-pXSq8qb4bGMDxFvGrK2lS_699Xb2jcgFHGC6h4MCFHx3c08OSvaQaI6iO3VzNiiogS2uT1Z8lTxqv3cnobHVR0j4WYi1mpQ_J5Wpu72fMiVcxhoodjaLgOtTzkI-avEJz7AoPjJiZIWzFao1bevlUPTuZPY-tr9WYv8upM4PS1ufTzf0rhbdVcv8JHzj7A6rGRg7tMCB0lVCB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922e3acbc7.mp4?token=vfqTeYns2tYLL73WNoPWx0nh1-lfOKLRv3YNEG_A4aiAMtBokXGkWUNAxHhy0yZ7ChbCzekf_YOwj1qvAaVrWYo_l2YwgqOIE8sAE6n-niBMmGrpXeEfPYPzwwxxh17Sr2dzfw-pXSq8qb4bGMDxFvGrK2lS_699Xb2jcgFHGC6h4MCFHx3c08OSvaQaI6iO3VzNiiogS2uT1Z8lTxqv3cnobHVR0j4WYi1mpQ_J5Wpu72fMiVcxhoodjaLgOtTzkI-avEJz7AoPjJiZIWzFao1bevlUPTuZPY-tr9WYv8upM4PS1ufTzf0rhbdVcv8JHzj7A6rGRg7tMCB0lVCB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارشی از کشتی‌های متوقف‌شده در تنگۀ هرمز با اعمال ارادۀ ایران در خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452322" target="_blank">📅 21:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx1_0pmUPP68vEAT4TwHooA5yngCbxmJtvY8i8UEhwNwRgtVDeoGR7DwXqOvjmuiIhCtGvFZZW-SZ4NcLXGO_HdlKO4UBYE4uhnftHICtgQBimH_3m40JZS1MJ6D1Na8IVxRtdjAz74zN69yzx2OXZCgo_ATG7jhEqrZTilAnkmD0SSruYX7-rl_ghm4GKGCK-seh1pV9RPhcftkDNm-Zb1G6RYkLE0kRVGgsME116vNgCor75RnqImOcn47OlK-sBIW0rBHIZBS0lkjhuCFw9ZP-jc7IrGQuEgmoDWIfnif3w5UyCUsX-2bIjCzSBo46vUCMeHTqU2TL3gBUdQNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به بلغارستان هشدار داد
🔹
سخنگوی وزارت خارجه در واکنش به گزارش‌ها دربارۀ بررسی درخواست آمریکا برای استقرار هواپیماهای نظامی این کشور در پایگاه هوایی «بزمر» بلغارستان گفت: «هرگونه همکاری در حملات علیه ایران، از منظر حقوق بین‌الملل به‌منزلۀ همدستی در تجاوز…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/452321" target="_blank">📅 21:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM27JgOHW1m7IyiBcSVVhNKpRlhdzHFYCUexfry6YuFbO-jHemhR6y7pByIzgwfeY26XiNwGil2Wo6eZQOMUGkdS5OT8BfRb0W_p-KYw3-HaKngThbdPnBk7GcDgyBjOUMadmsNxZ4uptNCkXXEq-GYRm9CulivhUnWpb0BQ4pzew-ei1C-kR32pnHUKgaD3r7Erw3cc4AMM-j35toYVIuS5COKToImJvO28hDaSqrqRIxwsTQYY_oc342VUADp6Dze4QNI-Rv5Ac85H_evhbgefgxovh5r2XHVatO6WzfMBmaW3BFbU8lSqp0vT1LtS6Je_nCyj7G1Jg1pY27bt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی درگذشت
🔹
اکبر عبدی بازیگر سینما تئاتر و تلویزیون بعد از تحمل یک دوره بیماری درگذشت و مسعود ده نمکی در گفتگو با فارس این خبر را تایید کرد.
@Farsnart</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452320" target="_blank">📅 20:56 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
