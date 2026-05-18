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
<img src="https://cdn4.telesco.pe/file/sDsm_-keZKlNr-QSejrR9gTOXDRKiVP4oS_kEgmYxkv5yQ6DrIJxYLxyJw5RNNGVp2N113yJD_U1tQGuoI6phqBSQ8Q--AFGo-FpGzLKHpvrFVvF6eKjCwc5bfcXBOJu7wQ-9y-Jo1Bz1gLBw9NeHbfRe0ahU72475GOkFHgbVNEdN2PeW92HmCpRh3YGI0IgNb3h5IzXiHznyQ7uLQXe-I9pl1EIUmDLFGOI3LEsIhmuLqdix0xQWT2fA3xCXSs0wnQFuMhKfFTwyWXaM6bMuheuDumHYldqGp4sW0UACHKDpT-5LgTEVf0Uuo7DgwAERmSZXsKz0ZJvQNviV7txw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 949K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-120869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قائم پناه:هفتاد درصد مردم مخالف محدودیت اینترنت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/alonews/120869" target="_blank">📅 17:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مدیرعامل آبفای تهران: تابستان امسال جیره‌بندی و قطعی آب نخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/alonews/120868" target="_blank">📅 17:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔴
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/alonews/120867" target="_blank">📅 17:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر صمت: نباید اجازه دهیم کالاهای تولید قدیم را به قیمت جدید بفروشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/alonews/120866" target="_blank">📅 16:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzQlUb16ENhSGcSEok55JYh3ATaGCZ0BnAlEwTztHloYtLrq-35URsPkwvJ0zaGwif4v98EOLH0LK3vwphNYJkhNWE7B6eHN60vMD6F722uafxxCm-TB4tTX0n_Hq7CEg66kvJN_5Rxlly-DsZg_Mz8-jV6mWY3KI5bfAdm5BmFwTgPIkO_uztk6aQa5MoAi_eMmz_kEAEqQ1daqwsuP21yMaiHEtPvssbyV2dw3bOZbbKW7879vd3jgPch1Jz6bDtja8tYR6EB-eWywVdkgz7zRBUpQKIaF808rJ_S9zuLjMgK_-Eg_UvU7gzPB5VZ_aFxzhxbC3wOb7S3E5HrJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ می‌گوید که «باید بیشتر از ۱۰٪ سهم دولت آمریکا در اینتل را درخواست می‌کرد»، و به مجله Fortune گفته است که ارزش این سرمایه‌گذاری از زمان توافق سال گذشته به شدت افزایش یافته است.
🔴
ترامپ همچنین استدلال کرد که اینتل «باید بزرگ‌ترین شرکت جهان در حال حاضر باشد»، و سیاست‌های تجاری گذشته آمریکا را مقصر دانست که به رقبایی مانند شرکت تولید نیمه‌هادی تایوان اجازه داده‌اند در تولید تراشه تسلط پیدا کنند.
🔴
او افزود که اگر زودتر رئیس‌جمهور شده بود، تعرفه‌هایی برای حمایت از اینتل وضع می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/alonews/120865" target="_blank">📅 16:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120862">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqLXoWtivhjoPKbb_PQDp3sKTWvjRrRO56XXCmo88Bx8LzZ15ARmdwxURy28ctXOEDgvs0Erlh0f7RzBmm1MxIEzEULP5TH8fWrGPjJCzM0_9CRMSGw0q_WZqJUQlyngRz0XN_JQlrgk6x1Y72Y3d3rmEW4rJnBFTW26WA_rUw-jD5syusummXyE3etZNQFSwH_Cp7Mc0nRkg0pE65G-PBm3mpYKv7K5wMUkOXtketd9YFULWKvQChH0NW-4uKsZu16LFITXVwzoQ7ArjZzNBQG6d_zN069O15aEriaf3ywtBdqvSOZdWcsxQPXy3eX5umsTcJcg-CAml29a-vNnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xw4TcKeDw62Mm-gW-ed8jz9Mp8xqq6Q7MlUnB3zuS7mzPNliw_-NkPf3aSHfhKThlApCiuaV_DgbxYTubacvO9A3rXI3FvqsjJmESw3w27i7R3aEnvmbNDhJXaPHh_7SlNUsy1-r_Gjq6_khD32GBePqI8SGtFR5-MsRc7uMHDp93B099I5sM2oI5medaWP_OQxQ7w5oB_audfSc0z75cT2is_zHC-LDhsb0m3WE5PeGl-WYOUF470s4SlCVllYu8bgP3TLExvsB4l6XzBKiHV3y9mj5FrIlfezpCSi_tHjfxcdfjEsDx1s-CsL0jjbaSRjuUBgiCmpy-lcn6Z0foA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92f75a629.mp4?token=pBlyAKpezDcrv8G7LL0MrYWDSy6KfTbHTP-lidHefH3R5QXIVHSGG0iIDcEAHmgAJ4QdhwW8yvfB8WkJCialjlpkib_Q5okSmbYSXwK43AgHzCM2IWBgoq4ZO2wlX_nQZbLxg-7WykJLdzLMYuVVPgODgdzUFT-gePtyBlJLZUlCgsFBiHypSDAdBMY_MFflQYe9VcQ16Cyp5B4wOmy0cxELxkubobaLHcoQsgbgzjVMCQ8gtx_WZpC-UUy0VdWYSnq6FVeG_JdqHODhXhtaECCo5270GBt96voHriesLx2wtEa15dicgBngUTgwjkDUsAECTWdGIvcaFuyo1iGPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92f75a629.mp4?token=pBlyAKpezDcrv8G7LL0MrYWDSy6KfTbHTP-lidHefH3R5QXIVHSGG0iIDcEAHmgAJ4QdhwW8yvfB8WkJCialjlpkib_Q5okSmbYSXwK43AgHzCM2IWBgoq4ZO2wlX_nQZbLxg-7WykJLdzLMYuVVPgODgdzUFT-gePtyBlJLZUlCgsFBiHypSDAdBMY_MFflQYe9VcQ16Cyp5B4wOmy0cxELxkubobaLHcoQsgbgzjVMCQ8gtx_WZpC-UUy0VdWYSnq6FVeG_JdqHODhXhtaECCo5270GBt96voHriesLx2wtEa15dicgBngUTgwjkDUsAECTWdGIvcaFuyo1iGPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به حروف، شوکین و کفر رمان در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/alonews/120862" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120861">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای امور خارجه جمهوری اسلامی ایران و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/alonews/120861" target="_blank">📅 16:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120860">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
👈
معاون سازمان بورس: بازار بورس فردا و پس‌فردا تا ساعت ۱۳:۳۰ فعال خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/alonews/120860" target="_blank">📅 16:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120859">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: به مذاکرات ایران و آمریکا خوشبین هستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/alonews/120859" target="_blank">📅 16:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120858">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کرملین : روسیه و چین قصد دارن حدود ۴۰ سند امضا کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/alonews/120858" target="_blank">📅 16:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120857">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
غریب‌آبادی: هرگونه توافق احتمالی، باید جنگ در همه جبهه‌ها از جمله لبنان خاتمه یابد، نیروهای آمریکایی از منطقه پیرامونی ایران خارج شوند، محاصره دریایی برداشته شده و تحریم‌ها لغو و دارایی‌های ایران آزاد شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/alonews/120857" target="_blank">📅 16:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmimWGMnjiJmLZUFG4BX4pn0W3ApqHDjfnh04XWUc8rSxIoWLhaXeCYrBuUpzGsk5Hvd3zrhSKwEiqXKTFUj33k9huns3h-Y0iWPqlllzwz-hc9w2i2cH3eQg_uF7WaPKEIscbSa-eZGRVFtjjcGCKkehFKjvCCYZfbnwXo9c8RMopbnU92exbj66Rp7Li0wYkoLGQi4w2OOBOq4ENqoiEjmzsblKrXLLfbQ1wFcpsIEHA6GVibd-S-o-RyTt1jKwN7x8IHJuffOKQJ4xFjcParqAdVVr6YeEnMBIbfBs8jMVwqvdbIkCL97a0mzFPIxYEITfziLWIdWhaLZKf7fgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/alonews/120856" target="_blank">📅 16:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نایب رئیس کمیسیون انرژی مجلس: افزایش قیمت سوخت در دستور کار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/alonews/120855" target="_blank">📅 16:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نخست‌ وزیر پاکستان: به مذاکرات ایران و آمریکا خوشبین هستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/alonews/120854" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFGvsPGUyMMgJTkhVxgbazCk-LfxV5qGAxKTPxvh9WViCUNYLLyNLv1qrQqHjp5-IZLwCCAalEtGQtmTEkNiOS5eeOOsyZEbum7zYCnxgGO6saflQ4GpmPo6QGjcdKu66f1uwklZhxKpaTU_SqxqFM-Ak5ZQXZFk4lyRwY0OVgIpzur1bNB6k6myzQp-OCVeRMxNUm4cemn40IQeH1pwDEGN4huOgwy6iZm4nvAbu4xrW-3mmaT9uU03_0D6BhplTsHjPC1IxoYkrkaVBY7-lqmLFJ_RdCtRAsbzHi2ip6XbFJ6Zrli8yC_bXABQRwrwcheZDt2CC_-8L3ebnATJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی مدعی شد که پاکستان در طول جنگ ایران، ۸۰۰۰ نیرو، جت جنگنده، پهپاد و سامانه‌های پدافند هوایی را در عربستان سعودی مستقر کرده است. این نیرو شامل جت‌های JF-17، سامانه‌های HQ-9 چینی و تجهیزات تحت مدیریت پاکستان با تأمین مالی ریاض است. این ظرفیت اعزامی از پاکستان، آماده نبرد است و در صورت نیاز می‌تواند به ۸۰۰۰۰ نیرو افزایش یابد.
🔴
عربستان و پاکستان سال گذشته پیمان دفاعی مشترک امضا کردند. وزیر پاکستان بعد از آن اعلام کرد که «عربستان سعودی تحت چتر هسته‌ای پاکستان محافظت می‌شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/alonews/120853" target="_blank">📅 16:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تیم اقتصادی ترامپ از اول جنگ، 3600 معامله روی سهام انجام دادن. %80 رشد نسبت به قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/120852" target="_blank">📅 16:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120850">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8779033c.mp4?token=XBhYMGpZ9Xp-Nfwx4NJ5gCX7yikZBKUi31Sbvoza1GPumqXDTsve7AX4X1mnSwacQhdKSO05tJQFf29ZJbZKa5eLl76R3Nl46Rzg_q26cYpaW7MV5oUXuoyvMQs79HIhg90tNH2T1GRjEF7T8j_ojjhMQTcSVNKHwOBKPN2BS9f5K6KeeNM1uTAHT5iU-N9L-WN-w76LmvgicuXYPeptC2MupdSx_xNRK89Gq822mnX13p7lkJkymiuVYlOGOb-9IMgwzF05l6x1Gf-vaz9lvrjqlHZjtXF_Am7jvPrD5TM0tBZwiq4HG-gkEftL36q8GsME1CaJ65ZnAM-kAt-HtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8779033c.mp4?token=XBhYMGpZ9Xp-Nfwx4NJ5gCX7yikZBKUi31Sbvoza1GPumqXDTsve7AX4X1mnSwacQhdKSO05tJQFf29ZJbZKa5eLl76R3Nl46Rzg_q26cYpaW7MV5oUXuoyvMQs79HIhg90tNH2T1GRjEF7T8j_ojjhMQTcSVNKHwOBKPN2BS9f5K6KeeNM1uTAHT5iU-N9L-WN-w76LmvgicuXYPeptC2MupdSx_xNRK89Gq822mnX13p7lkJkymiuVYlOGOb-9IMgwzF05l6x1Gf-vaz9lvrjqlHZjtXF_Am7jvPrD5TM0tBZwiq4HG-gkEftL36q8GsME1CaJ65ZnAM-kAt-HtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل، یه منطقه از جنوب لبنان رو با خاک یکسان کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/120850" target="_blank">📅 16:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120849">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/نیویورک تایمز:
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای ازسرگیری جنگ با ایران در همین هفته هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120849" target="_blank">📅 16:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120848">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173f8825d8.mp4?token=Zj-JYJuDVP1PxtEqJKEjZF_n8oxPqrckLAXC5KZEx35V2sEmmLPysqVCUBivcg6Lk-O82syZ5e1lOwPlNCXyWQV28vJTS2d4pIikyTg0O-sSmRz8kZy90K1GbQGqdCAEUW9t4AHxmAOBXgsbl7n4_tCOVPsUd6EGmkZWjycwr0c0GqWt10f1C2r_1AMbfpqzY7fe7NVHQruYlN-702jWuWbSfTbv3BcPvrZaSn-HkHPj3h5dfz0VBVd4STTSVNX0d3IsO1p-TOCOWYzcUUUBKE5T1Wc2AqElos9Guta4riYQORdqShfpjYh8co4HaafAJ6Ira0dIP9QriNZqVJo3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173f8825d8.mp4?token=Zj-JYJuDVP1PxtEqJKEjZF_n8oxPqrckLAXC5KZEx35V2sEmmLPysqVCUBivcg6Lk-O82syZ5e1lOwPlNCXyWQV28vJTS2d4pIikyTg0O-sSmRz8kZy90K1GbQGqdCAEUW9t4AHxmAOBXgsbl7n4_tCOVPsUd6EGmkZWjycwr0c0GqWt10f1C2r_1AMbfpqzY7fe7NVHQruYlN-702jWuWbSfTbv3BcPvrZaSn-HkHPj3h5dfz0VBVd4STTSVNX0d3IsO1p-TOCOWYzcUUUBKE5T1Wc2AqElos9Guta4riYQORdqShfpjYh8co4HaafAJ6Ira0dIP9QriNZqVJo3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی آفریقای ایالات متحده، با هماهنگی دولت نیجریه، به حملات علیه تروریست‌های داعش در شمال شرقی نیجریه ادامه می‌دهد.
🔴
فیلمی از حمله هوایی به گروهی از تروریست‌ها دیروز نشان داده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120848" target="_blank">📅 16:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120847">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPVx75xj9_NeS7RcG2WYoSM4UiVbAMObb-3bB5tK-F_UQ9gKBAXhLVdQOGaHbAsLJB_6Q-wAUqj-2kFjiCXDcGMaan8rh9zOBl0T0prtBPvb4fP9qtdjH57E6AQZdlGuGEIcN1PhVbdsKi2yAVtsWZt2jXnvEaAmJ5h4R1f2BhqDJa1R5Nnp9ajKeSTWN2hqGtNYSWFemsf_wqfrvr3fpBu01HJ9crseRGXf6F9W6pM3E-VF8dk9iFMCLZYzW8OeHjYvhXZvVgD7Hj_3V7w8j0_3tNu6o_zvBKF-zG1fN-b1GtCqoodJukn9NQCtIWqNz_ZCieRli-UrhuGu2kXKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
ربات رسمی دریافت کانفیگ رایگان فلش‌نت راه‌اندازی شد!
از این پس می‌توانید با دعوت دوستان خود به ربات،
🎉
کانفیگ اختصاصی و رایگان دریافت کنید.
✅
بدون ضریب
✅
کاملاً اختصاصی
✅
فعال‌سازی سریع
🤖
آیدی ربات:
https://t.me/Flashnetgiftbot?start=5011918694
📌
همین حالا دوستان خود را دعوت کنید و جایزه بگیرید!
🙏
تیم فلش نت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/120847" target="_blank">📅 15:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120846">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvjUkaS3lMEbR3YjSM-7VrfxK1AG8g4yN75J9WyU2tY8oNoehKCsbvIqlguFb_JSlNR1nUI4eJXP8djC1cZDCsL87TgYNJbRcTrMjT-NQfHmGln0RyWnnQj5fJrZM_msAw_ghv75aMwz3Vd-G-Xq-lxV4GeMwTadsMoyA7ClsogenUq7iQ5AV18emlfubREwEWziO0-DrR18iFntL5v81dgM9gMq4ouBMvz97nxUf4FVUXvdtXF4HfMwoM4YpPTo7yZdOCE5ziUAJfX2YWivHBBIYyhINHcCsidSN_yP4Vb4cdUdKqXLFnKrM1881QOpdWY8Xf1JNKOkzKrC9ij8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در حال بررسی برنامه‌هایی برای نصب یک هلی‌پد در کاخ سفید است تا از آسیب دیدن چمن جنوبی توسط هلیکوپترهای جدید VH-92A پاتریوت که برای پروازهای مارین وان استفاده می‌شوند، جلوگیری شود، گزارش وال استریت ژورنال.
🔴
هلیکوپترهای قدرتمندتر VH-92A دود و هوایی تولید می‌کنند که به اندازه‌ای قوی است که می‌تواند بر چمن تأثیر بگذارد، که این موضوع باعث شده تا نصب یک هلی‌پد اختصاصی در نظر گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/120846" target="_blank">📅 15:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120845">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d3e3dc3.mp4?token=YueKI8dpFfNN2f-B20p4uzPQ7K7vqHlAR_n0mWN8CDYuG8n2kAcpheTemSC11DwJI6l_rPF1XWzNXvqafXV9BMvm3NCBHhIr5MXH2PejKF_5ua7AJ_XflKepDPm-quah_-HssmSt2Uu5Fnu1niA88qZ_P0FnYWLJfB9hSUgk6iv0C9Qm0Sk0tGU8PzuyraGuOj3prwXGwIg3YVhIh2YoR8LGDyFvCFfr-3bqfEqbEzfgre89rZKzQyAYcvECGBw11bljtTxZXijK2KKOstjWZbSfneGm4UuaRNqSoPmTiesDwakk-UNtC0yY9CKCsSUIwJuITmQa9jEZ9OEs0fTwJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d3e3dc3.mp4?token=YueKI8dpFfNN2f-B20p4uzPQ7K7vqHlAR_n0mWN8CDYuG8n2kAcpheTemSC11DwJI6l_rPF1XWzNXvqafXV9BMvm3NCBHhIr5MXH2PejKF_5ua7AJ_XflKepDPm-quah_-HssmSt2Uu5Fnu1niA88qZ_P0FnYWLJfB9hSUgk6iv0C9Qm0Sk0tGU8PzuyraGuOj3prwXGwIg3YVhIh2YoR8LGDyFvCFfr-3bqfEqbEzfgre89rZKzQyAYcvECGBw11bljtTxZXijK2KKOstjWZbSfneGm4UuaRNqSoPmTiesDwakk-UNtC0yY9CKCsSUIwJuITmQa9jEZ9OEs0fTwJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی نشان می‌دهد که یک کشتی از ناوگان جهانی صمود به سمت غزه توسط سربازان ارتش اسرائیل تصرف می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/120845" target="_blank">📅 15:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120844">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: تلاش‌های میانجی‌گرانه برای دستیابی به توافق بین آمریکا و ایران ادامه دارد.
🔴
تمام توان خود را برای تضمین برقراری صلحی پایدار به کار می‌بندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/120844" target="_blank">📅 15:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120843">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ادعای رویترز به نقل از منابع: پاکستان بر اساس توافقنامه دفاع مشترک، ناوگانی از جت‌های جنگنده، هشت هزار سرباز و سامانه دفاع هوایی در عربستان سعودی مستقر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120843" target="_blank">📅 15:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120842">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCK16HZ0erREkG0CcaCjtrKGj5-ZTs-hwdxil8CcdWeXaBUY56HnKD0W9f8rwoncBs53LZHVLEBANopd84V7EyHyCyYwYFHIbhilHw-9fk5QbxBj0hBRd2WUa58MYz2ZF0DdnB9wnec4mNv_F0XWRchUXaaz3o602FZmpoiurCGokZf4Tt-h0Y0oyrscM4I6_wtUPSuFS6JZk6GNI7Mv4pxzQxMgkWzBBWVZhr72a5r3hvhgO04vkQ7SqnjQ4oTWCzu_rEps2atvCEKY23AClJ2sYhMODGYSXjxUUApBjfB_moTFtFHv0PrasnDfgXhDdvmGPWt2NoPhaue2JGaVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل تأیید می‌کند که فرمانده ارشد جهاد اسلامی فلسطین، وائل محمود عبدالحلیم، در حمله هوایی اسرائیل به دره بقاع شرقی لبنان در طول شب کشته شده است.
🔴
ارتش اسرائیل می‌گوید او به عنوان فرمانده گروه در منطقه بقاع خدمت می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120842" target="_blank">📅 15:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120841">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کوثری عضو کمیسیون امنیت ملی و سیاست خارجی مجلس: قطعا و یقینا از طریق مذاکره به نتیجه نمی‌رسیم
🔴
ترامپ جنگ را باخته و می‌خواهد یک جوری خودش را برنده نشان بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120841" target="_blank">📅 15:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120840">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23f6a8852.mp4?token=G2rEd9uB_3GVsb-kU2XfuqfYEa8fr-CSVfzbGRBfqetPutw3UG85jFso5Gk9ujnYyRt4iB1WeLZO-Qld0aAo2LZRPnMfO1GyCoCCnsXpzO4gY0W3h2rR32otbCZQsc5mc573RNTmKnHt24jueGqpD5-T4I0I0AwYPnrKOPWZ1pN1aq_bxKjb10_OOIFquwiSUzyX4hvnvyczYJF-q9lXgdCC5qQWTUb2DdVjUZbWY2O9yVlHFYwBenu7RaU_tiv_RtwXrCVUQHsGuNfPzv9mdHzbJjlE_-4yKQuUe9RakhTrh4vyBYQWBO2TvyUWHILgWqLYoLgTZ1scwYNPiFyeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23f6a8852.mp4?token=G2rEd9uB_3GVsb-kU2XfuqfYEa8fr-CSVfzbGRBfqetPutw3UG85jFso5Gk9ujnYyRt4iB1WeLZO-Qld0aAo2LZRPnMfO1GyCoCCnsXpzO4gY0W3h2rR32otbCZQsc5mc573RNTmKnHt24jueGqpD5-T4I0I0AwYPnrKOPWZ1pN1aq_bxKjb10_OOIFquwiSUzyX4hvnvyczYJF-q9lXgdCC5qQWTUb2DdVjUZbWY2O9yVlHFYwBenu7RaU_tiv_RtwXrCVUQHsGuNfPzv9mdHzbJjlE_-4yKQuUe9RakhTrh4vyBYQWBO2TvyUWHILgWqLYoLgTZ1scwYNPiFyeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نمایی از تنگه هرمز از داخل یک هواپیمای مسافربری و کشتی های خاموش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/120840" target="_blank">📅 15:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120839">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آمریکا در متن جدید خود اسقاط تحریم‌های نفتی ایران را پذیرفته است
🔴
تسنیم نوشت: یک منبع نزدیک به تیم مذاکره‌کننده گفت که آمریکایی‌ها برخلاف متون پیشین خود، در متن جدید پذیرفته‌اند که در طول دوره مذاکره، تحریم‌های نفتی ایران را Wave کنند.
🔴
ویو کردن تحریم‌ها به معنای اسقاط موقت تحریم‌هاست
🔴
ایران تاکید دارد که لغو همه‌ی تحریم‌های ایران باید جزو تعهدات آمریکا باشد. آمریکا اما اسقاطی اوفک را تا زمان تفاهم نهایی مطرح کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120839" target="_blank">📅 15:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120838">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRYqMMBm9w6I3NGembvqCqLi4tWt_c_OmyR9jdJp2NouHveNS8_V03FNrEru-oaAhQMnB35_aRVQQ776DW5bWa9pTUzHZnnOALRbXD-6UIFfAae3N1sDtgocxQNEHZTcDjWLmCD9DjYu3vSxDDg0pXMUt4J5NHxwKpZ6aupz9ste1Y17ofU6bwAKSUF7u-Ttiplbq24XztDGZJK5ctA0caD2gBzlJEqe3iyaAKkv2WROZEnnJZSRgkPalC78G5_CbEvU_EakEIK3ZbGH1O9gkQTn8X-84-xqj0H0qdhv77sIfEt4pg4KiGXtyIuaXYH9ka8HWQUAzD376_EGldg0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در شبکه ایکس یک حساب کاربری جدید به اسم  « مدیریت بر تنگه خلیج فارس» ساخته شد
🔴
امروز  جمهوری اسلامی از ایجاد نهادی مسئول بر مدیریت تنگه هرمز خبر داده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/120838" target="_blank">📅 15:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نیویورک‌تایمز: امارات بیش از ۶ میلیون دلار به شرکت مدیریت شهرت «تراکیت» پرداخت کرده تا نتایج جستجوی گوگل را دستکاری کند و گزارش‌های انتقادی درباره «یوسف العتیبه»، سفیر امارات در آمریکا را سرکوب کند
🔴
این گزارش‌ها اتهاماتی درباره ارتباط «العتیبه» با قاچاق جنسی را بررسی می‌کرد
🔴
شرکت «تراکیت» اقدام به ایجاد پروفایل‌های مثبت و ویرایش ویکی پدیا با حساب‌های ناشناس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/120837" target="_blank">📅 15:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای رویترز به نقل از منابع: پاکستان بر اساس توافقنامه دفاع مشترک، ناوگانی از جت‌های جنگنده، هشت هزار سرباز و سامانه دفاع هوایی در عربستان سعودی مستقر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120836" target="_blank">📅 14:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
لاوروف: پروژه نیروگاه هسته‌ای بوشهر به هیچ‌کس جز روسیه و ایران تعلق ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120835" target="_blank">📅 14:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
معاون وزیر ارتباطات: باید دسترسی امن مردم به اینترنت پایدار را به رسمیت بشناسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/120834" target="_blank">📅 14:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
حزب الله: ما یک سکوی گنبد آهنین متعلق به ارتش اسرائیل در اردوگاه جنگل های جلیل را با یک پهپاد هدف قرار دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120833" target="_blank">📅 14:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7EgncOUDPwvwY_dwqQoAu96begZVGrvu83ch9eApgmtVa4hYEloLQujfZr8oEF40_7ffsNMT-YaNO6sD-92ZBFKORlkQNldB5akREWn7UbUq9Gm4x65vj-l6Wfuh3CWtWYXuXz6ZVYimu6ShuRg-BvMb7YMBUNFOyjCAkvmCuyHsFtRHIkDd8URgsJK9Tj9Mcmziz06xv7tw-E5sNp18wCywQwgD0pdRDLIZAHoLYYii2V_-2w_EUS-bKOtJ8a7-JGw2Xw4CkK4_NNgGzVUCUARZswSBdDUB5N0IXBxyIyKKufAzfuxMIj-G8YNIPE2YWZtcrihkLhZvv272H076g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqVWr7OjnjAg6q8uLrAZD9RcGds8uYejNiYX1jXiU5s9Ne1p4zCaZRz44s54un4mM30t1HE9Ww7ML_U2IXM7z-b5xKLJdx1Y0AxiDCCCdWpkM9ud3g_gnKsDw3_LaGZG7GvkXnB-pKTNlwT4PYnTc-kTSA4BiR2AB3TrabX3K8BOqcQq8zp7Sq_vClJNkB4njWyl9aM-hU6dR7Kf8eaPBsJW7mPh0HXaHuJqNHBGAaYVY_AzkYTzgGBCA9ANnbBjoSHx94gNXrSCncECQ9ymGyAK10FxGbpjED__nMAug6x0dldjaPsIJ9fxQOWsz4ELX2AaZuWoHiHBLQ40Q0iKkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/120831" target="_blank">📅 14:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رسانه‌های عربی از حملات هوایی اسرائیل به مناطق مختلف جنوب لبنان خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120830" target="_blank">📅 14:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اتحادیه اروپا ضمن حذف وزارت‌خانه‌های کشور و دفاع سوریه از فهرست تحریم‌های خود، تحریم‌ها علیه مقامات حکومت بشار اسد را تمدید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120829" target="_blank">📅 14:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
آلیس روفو وزیر مشاور نیروهای مسلح فرانسه با اشاره به تهدیدهای تازه دونالد ترامپ رئیس‌جمهور آمریکا علیه ایران، توقف «تنش لفظی» و «تنش نظامی» را خواستار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/120828" target="_blank">📅 14:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120827">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزارت دفاع بلاروس : تو بلاروس تمرین‌های برای استفاده رزمی از سلاح هسته‌ای شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120827" target="_blank">📅 14:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دبیر انجمن واردکنندگان خودرو:
با نبود اینترنت و قطعی دیاگ، موج خرابی خودروهای وارداتی در راه است
🔴
بسیاری از دستگاه‌های دیاگ و تجهیزات تخصصی تعمیر خودرو برای بررسی و رفع ایرادات و حتی بروز رسانی نرم‌افزار، نیازمند اتصال به اینترنت بین‌الملل هستند و اختلال یا قطعی اینترنت بین‌الملل باعث شده روند عیب‌یابی و تعمیر بسیاری از خودروهای وارداتی با مشکل مواجه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120826" target="_blank">📅 14:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر قطع ارتباطات: دسترسی مردم به اینترنت یک نیاز واقعی است، نه امتیاز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/120825" target="_blank">📅 14:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: در پیشنهاد جدید ایران هیچ اشاره‌ای به هرمز و اورانیوم غنی‌شده نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/120824" target="_blank">📅 14:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565c9a1be5.mp4?token=L3Oz2olHj9UWF_1cQzWa18_IwbymMqDSCJ8K1kZ6XfIwCpM-CK34uCg7Vr4vuZ8wJ_FDhJhsMIx7BsN8ilJnd1URHbHDw7gGjXLnLg0hsFcpxxQ1sIzgz5752Ys6S99j5ncN-3eSZ2AkwWv0-05WgUnA6k9TZHDPRc_23rxJErme2mTc15GVOJfRiNdssht2u5vOo8Z3elJDJ33qjO_uqsJSo6c6Z6IJeCnTXzVinbGWRUfoZEDUTJ6iI_1zH4fXB9AZzVuJ-sSoKuVqLdq-qjgPd6xVRzRkClNxovZE60gpD_Ps6WzRVRXaGXyU6Vo7-obGuhuUfJn6-dTe0rzdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565c9a1be5.mp4?token=L3Oz2olHj9UWF_1cQzWa18_IwbymMqDSCJ8K1kZ6XfIwCpM-CK34uCg7Vr4vuZ8wJ_FDhJhsMIx7BsN8ilJnd1URHbHDw7gGjXLnLg0hsFcpxxQ1sIzgz5752Ys6S99j5ncN-3eSZ2AkwWv0-05WgUnA6k9TZHDPRc_23rxJErme2mTc15GVOJfRiNdssht2u5vOo8Z3elJDJ33qjO_uqsJSo6c6Z6IJeCnTXzVinbGWRUfoZEDUTJ6iI_1zH4fXB9AZzVuJ-sSoKuVqLdq-qjgPd6xVRzRkClNxovZE60gpD_Ps6WzRVRXaGXyU6Vo7-obGuhuUfJn6-dTe0rzdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
افشاگری محمدحسین عظیمی دبیر کل جبهه انقلاب اسلامی در مورد مسیح علی‌نژاد و گلشیفته فراهانی
🤔
عامل دستگاه امنیتی در ایران بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120823" target="_blank">📅 14:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
خبرنگار الجزیره به نقل از منبعی در وزارت کشور پاکستان: وزیر کشور پاکستان، سفر خود به تهران را یک روز دیگر تمدید کرد
🔴
تلاش‌های پاکستان در حال حاضر بر تضمین تداوم عدم تنش متمرکز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/120822" target="_blank">📅 14:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صدراعظم آلمان: تهران باید با واشنگتن وارد مذاکره شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون محدودیت باز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120821" target="_blank">📅 13:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
تسنیم: ایران متن جدیدی را در ۱۴ بند به واسطه پاکستانی تحویل داد
🔴
یک منبع نزدیک به تیم مذاکره کننده:
ایران جدیدترین متن خود را در ۱۴ بند به واسطه پاکستانی تحویل داده است و میانجی پاکستانی آن را به آمریکایی‌ها ارائه می‌کند.
🔴
آمریکایی‌ها اخیراْ در پاسخ به متن پیشین ایران که آن هم در ۱۴ بند ارائه شده بود، متنی ارسال کرده بودند. ایران نیز مجددا بر اساس روال چند وقت اخیر در تبادل پیام، متن خود را پس از انجام اصلاحاتی مجددا در ۱۴ بند به واسطه پاکستانی ارائه کرد.
🔴
به گفته این منبع مطلع، متن جدید ایران بر موضوع مذاکرات پایان جنگ و اقدامات اعتمادساز طرف آمریکایی متمرکز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120820" target="_blank">📅 13:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قیمت نفت اوپک از ۱۱۶ دلار عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120819" target="_blank">📅 13:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بلومبرگ با استناد به تصاویر ماهواره‌ای گزارش می‌دهد که تقریباً ۲۳ نفتکش در نزدیکی جزیره خارک مشاهده شده‌اند که بزرگترین تجمع از زمان آغاز تحریم‌های آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/120818" target="_blank">📅 13:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع پاکستانی:
ما زمان زیادی برای پر کردن شکاف‌ها بین واشنگتن و تهران نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/120817" target="_blank">📅 13:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120816">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyA-woyGE-0Jvy07VpSRd2mDIB2joDdTojL5o67tTjgRYHqQj0u-v9ZqrySpmMj8b5VAp3D9TBhZdcaqm37tQj4icXrSQX_YQvnic5an5tp82GLN1o91beYOwCQKvZpBnugE--gpZ4-9yf0fYrmxDO7MA0uq2S5UkRMY_b4Lyq7VlxjhB411zixx_cIJEKUltxFlZMMU5vo2ydjhJIPvkYzhYa3kkEe0Ap1T1_aA3DQCRQ3CWLhWHhqbuzhpdXbAYvXU8LK-B1CKgjI-PBTxuRGsTCX4_16wNbMarJKLXxljCY_UHrh5HCBeAteAlC-zQxLXbypByvynZmzePI7aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پائین‌ترین پینگ‌ها رو با ما تجربه کنید
✔️
🔄
کانفیگ‌های استارلینگ با پشتیبانی 24ساعته و لینک ساب
🔄
💯
مورد تایید مجموعه الونیوز
💯
📌
تحویل زیر 1دقیقه
📌
بدون هیچ گونه قطعی
💰
خرید آسان و سریع
⬇️
💎
@FastProxyMakerBot
💎
@FastProxyMakerBot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120816" target="_blank">📅 13:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120815">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
براساس گزارشات خبری، کشورهای منطقه تمام تلاش خود را به کار گرفته اند تا جنگ میان ایران و آمریکا و اسرائیل به پایان برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/120815" target="_blank">📅 13:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120814">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت علوم: در ایران از هر ۱۰ بیکار، ۴ نفر دارای مدرک دانشگاهی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120814" target="_blank">📅 13:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120813">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ممنوعیت هرگونه تبلیغات اپراتور‌ها و دستگاه‌ها درباره فروش اینترنت پرو
🔴
اولین جلسه بهبود فرآیند اجرای طرح اینترنت پرو به میزبانی وزارت ارتباطات برگزار و در این جلسه مصوب شد که هرگونه تبلیغات توسط اپراتور‌ها و دستگاه‌ها در زمینه فروش اینترنت پرو ممنوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120813" target="_blank">📅 13:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120812">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز نقل از مقام پاکستانی: ما زمان زیادی برای پر کردن شکاف های بین ایران و آمریکا نداریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120812" target="_blank">📅 13:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120811">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرنگار کانال ۱۲ اسرائیل: به گفته منابع غربی، پیشنهاد جدید ایران شامل تعهدی با ارزش نامشخص برای عدم تولید سلاح هسته‌ای است، هیچ اشاره‌ای به اورانیوم نشده است، هیچ اشاره‌ای هم به هرمز وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120811" target="_blank">📅 12:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120810">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که نیروهای مسلح این کشور حمله‌ای گسترده را به تأسیسات صنعت دفاعی نظامی اوکراین و همچنین زیرساخت‌های حمل و نقل و انرژی مرتبط با نیروهای مسلح اوکراین انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120810" target="_blank">📅 12:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120809">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نیروی دریایی اسرائیل یک ناوگان به سمت غزه را نزدیک قبرس متوقف کرده است. ۶۰ کشتی این ناوگان قصد داشتند محاصره اسرائیل بر غزه را بشکنند و کمک‌های بشردوستانه بیاورند، طبق گزارش الجزیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120809" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120808">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4jjy--VZaLSTViqoM6hW_vAG8z13HHpaIL2TWJBY8te7wVr83L6rCkh2m6OFOECt1eQbRJKw94qypyEHnxwSuSShTi7V02q2x9BFGXmV-ONDB0xUSibROBNM6dbMuoBBL0hTGVnIR3TLzA_EHSgNnEl5kSnPtUfKyYRIs1wjSrXG5jjHhVPGpB1_FwzZa_TM2tWOc8YUrRuwRpHm5WaPd1K-tOfU-O13UnOyrd3RywIvOqUH4TJklqZwA-_GCmDubOq8znxFU_b13VkEmnP_Tp8X-OQGwvjAY2l9wYTkEHBwBXQrui_S_ANIy-g4NqqhjIAk9MEf9CY4--hoU0dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سردار آزمون به خط خوردن از تیم فوتبال ایرانی:
پاک کردن پروفایل با لباس تیم ایرانی و آنفالوی پیج های تیم ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/120808" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120807">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: نباید به دروغ ادعا کنیم که هیچ مشکلی نداریم و دشمن در حال نابودی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120807" target="_blank">📅 12:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120806">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78d5c5526f.mp4?token=VpBzACjF4sFSI_k8eZE9g36BmBieYL2HFcB0_VzpT1grx9mr72tFCon0h596WsdvcJP_b4SGiZxuRr_1Ghsa9NUojl-1cmlDSBvQXnNA_nwTs8YGxswxPEOpjVTS0f4ebAqqeTLooULwrAezpOiCT9UfzuZVH9u7g3trze73CHclchcSuADlKsHj9qmrdP318CGFV08tcW5zQErsE6OmvrTfoApJ0smOckJdVjMqetEIqKvVuFPQ6IPpDE8OBBRh4jSfAeltTooYisdSSwhsL_KhqOHVV9YPFVey10r5Tjd8TkF-CR0Z7EYt1g0SJ_z2tLGVtGkXjlnlxiqDz-jIhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78d5c5526f.mp4?token=VpBzACjF4sFSI_k8eZE9g36BmBieYL2HFcB0_VzpT1grx9mr72tFCon0h596WsdvcJP_b4SGiZxuRr_1Ghsa9NUojl-1cmlDSBvQXnNA_nwTs8YGxswxPEOpjVTS0f4ebAqqeTLooULwrAezpOiCT9UfzuZVH9u7g3trze73CHclchcSuADlKsHj9qmrdP318CGFV08tcW5zQErsE6OmvrTfoApJ0smOckJdVjMqetEIqKvVuFPQ6IPpDE8OBBRh4jSfAeltTooYisdSSwhsL_KhqOHVV9YPFVey10r5Tjd8TkF-CR0Z7EYt1g0SJ_z2tLGVtGkXjlnlxiqDz-jIhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان اگه پولتون زیادی کرده و نمیدونین باهاش چیکار کنین، کاخ گوتیک امیردشت با قیمت مفتِ 1500 میلیارد به فروش میرسه، حتما بخرین.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120806" target="_blank">📅 12:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120805">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120805" target="_blank">📅 12:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آن چیزی که با قطعیت می‌توان گفت، این است که بحث حق، چیزی نیست که بخواهیم درباره‌اش گفت‌وگو و مصالحه کنیم.
🔴
حق ایران برای غنی‌سازی بر مبنای توافقنامه NPT شناسایی شده و نیازی نیست دیگران این حق را برای ایران شناسایی کنند. این حق وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120804" target="_blank">📅 12:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120802">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfpAmMsqdAfwthyDV0IS26QixuqK6QifTU4dG5MPRHIJwThnTXRpk-_Wz6xtSxUemtX6diyy0tkr3cktpmULsVO9Y8ah8Fe7bb1_ynJ7cd32SsXFIWmW05QwfxDY--HWwUVBp255Re1E8eQ-sFDsmP88USSP5fbGEV1M4BqH5coNnm1p3w2pEnK9iZoZuRO0XcQzA5mL0rUAZvJFvpIueZv9txH5I6uU1_sYe41domSUJG3igslKIEe37sl982w1u0qzIW0Z5VQyduthZMMPfd9kE7a2fPSTNETxS9O9oCy9T7OGICP2ecIin_5p2lRqzQYcfIW6vv_kHNEAPmuHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت پزشکیان:
کسی که شعار می‌دهد باید پای شعارش بایستد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120802" target="_blank">📅 12:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120801">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ : اونا یه برگه می‌فرستن که هیچ ربطی به چیزی که توافق کرده بودیم نداره
🔴
منم می‌گم :  "شماها دیوونه‌اید یا چی؟"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120801" target="_blank">📅 12:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120800">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دونالد ترامپ به مجله Fortune: «ایران مشتاقانه در تلاش است تا قراردادی امضا کند. آنها بسیار به دنبال یک توافق هستند، ایران درباره توافق صحبت می‌کند و سپس یک کاغذ کاملاً بی‌فایده که هیچ ارتباطی با آنچه ما بحث کردیم ندارد برای من می‌فرستد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120800" target="_blank">📅 12:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120799">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
امروز هشتادمین روز قطعی اینترنت ایرانه که بیش از ۱۸۹۶ ساعت ادامه داشته...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120799" target="_blank">📅 12:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120798">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b932112c5.mp4?token=YbBdSeh7CAF3XAR_0MJB-7-EYpjHI9vKtAiVsGCRYp9EhvIx7U1QskTkglIKibKT6K8awo4afsArOy-2YWiu-upV117dzcmAUwfTgJD5SGJH2X6gsR4dNrHk2ffuIdpuDMSyqwx7lQ8C9aHsqbJohsGtyDYbYXMxyEqcKDxxhb2IqqhXDzQVSuP6zsZXSMyFwNGQcm0Nw5BMaw9uodYrS9dTnW11I6Agq9xJfzxHCOUxJMGimZZBP5XJ0eXafZy0Ml2FBz4oN823HQTV6FiLiuV8Jt555J8hCTQcLgeOAFM4kYHqS8znNuYXYLqJUkqhPtTTH5-V1WxIHuy2FXHY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b932112c5.mp4?token=YbBdSeh7CAF3XAR_0MJB-7-EYpjHI9vKtAiVsGCRYp9EhvIx7U1QskTkglIKibKT6K8awo4afsArOy-2YWiu-upV117dzcmAUwfTgJD5SGJH2X6gsR4dNrHk2ffuIdpuDMSyqwx7lQ8C9aHsqbJohsGtyDYbYXMxyEqcKDxxhb2IqqhXDzQVSuP6zsZXSMyFwNGQcm0Nw5BMaw9uodYrS9dTnW11I6Agq9xJfzxHCOUxJMGimZZBP5XJ0eXafZy0Ml2FBz4oN823HQTV6FiLiuV8Jt555J8hCTQcLgeOAFM4kYHqS8znNuYXYLqJUkqhPtTTH5-V1WxIHuy2FXHY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین: تایوان بخشی جدایی‌ناپذیر از قلمرو چین است. تایوان هرگز کشور نبوده است، نه در گذشته و نه در آینده.
🔴
استقلال تایوان و صلح در سراسر تنگه به اندازهٔ آتش و آب ناسازگارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120798" target="_blank">📅 12:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120797">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت امورخارجه به تهدیدات ترامپ: خیالتان راحت، خوب بلدیم جواب دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120797" target="_blank">📅 11:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120796">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a457e4dfad.mp4?token=SUeojIcRHQEpC71KxWBLodxApndoJPT3wG8Cf8NYQDNGH9G44GDmReRaKdPMMVlryZsVgaCsoFVgwFW_jzmVe-zaXt4_OgMP5Mv1MouPjCUVn_0_GYjMI10ep1hYlzDk5M0JhVtnegT1d-ItyI0wSOsl_C9nc6RNKBEnhQ2EDNxruZdmhVlM-ZH41hjNALnYvULgopRUr5zrG_1sNnbpg7TtwItb-zuoDrZeG1vKkNOA-nsYW38EnL6-vojmNxOIPcftt5aBPEofKtPAfO9uhXDobqdXFaLcNDqC306sllHdiWhOrfMg3QzAtdAAdaQSC9SskuS23yGbUW0cWKJoLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a457e4dfad.mp4?token=SUeojIcRHQEpC71KxWBLodxApndoJPT3wG8Cf8NYQDNGH9G44GDmReRaKdPMMVlryZsVgaCsoFVgwFW_jzmVe-zaXt4_OgMP5Mv1MouPjCUVn_0_GYjMI10ep1hYlzDk5M0JhVtnegT1d-ItyI0wSOsl_C9nc6RNKBEnhQ2EDNxruZdmhVlM-ZH41hjNALnYvULgopRUr5zrG_1sNnbpg7TtwItb-zuoDrZeG1vKkNOA-nsYW38EnL6-vojmNxOIPcftt5aBPEofKtPAfO9uhXDobqdXFaLcNDqC306sllHdiWhOrfMg3QzAtdAAdaQSC9SskuS23yGbUW0cWKJoLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: منشأ حمله به کشتی کره جنوبی را بررسی می‌کنیم، قائل به برقراری امنیت کامل برای کشتی‌ها هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120796" target="_blank">📅 11:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آخرین پیشنهاد ایران برای پایان جنگ، یکشنبه شب(دیشب) به طرف آمریکایی ارسال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120795" target="_blank">📅 11:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2HPUHJVhDXZXGdC78c9n4Jw04EYy6I88DT7S26sI5K4EFfXOs-ad8ERLVRHvHSd8bxNKd5WPdYUvuaVF4aeREZLbAqb7ggoK9VqLevHbAJdFz6IaI50GsQj7fTKAhK3xDAY5qH1DvFT2-UxRZYI-a1oxof3IgDsQtMKYI6Yx22SwDR5uMsCjblk3zSlN2zZVXerlvII4B732uDGhK4v0WGXkxDNrdwoMu26p3QF4x-zPgapjiauYsnCAywApB0oqhofKUBolWCM2EBRxOXL5BfumH5Gv5SI56ZJnclHil_g5gGnjWPYwvlRmHm0miVF-tZVxyReut9Xa8ngDJlpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/رویترز: پاکستان پیشنهاد به‌روزشده ایران رو به آمریکا منتقل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120793" target="_blank">📅 11:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUa0oHSKtUYm9bOdw6OEHiHmGHTzbE0TRBcwAsy30dqSAitwu969V2JTN3qC9EAsTR7IWePZSLV_eIvSjtV-dVbA0RcyAEHrRRxmGJmwMPotEPSTJHYF84bovcbMbGDrF5Rn0cCb8K3hlZFwSN3PxgYCwEDE7L_uv6Vylctra5FwXPd2qydU2wLnTW5epiTSm2HtRwaPgx6vy4KmRpc3SQ7QeCkbWaHgRNZ5s7gipEDo_8MfYCiwPkV8Tr6Ayisaf45Rad1aYjHlzFcl7ZKg-tnbFTjpa0YwbQV931j61k0IhBHR1gAWC_ZFS1ACMvOBZOwOOgfsSR4Doh47zm_y5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:
هرکسی که ضد جمهوری اسلامیه و باهاش مشکل داره، ضد ایرانم هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120792" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
انجام عملیات انفجار کنترل‌شده در اندیمشک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120791" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lasmEeKh2VBpNaZAEOSM-1hTCT-w_LZLY0tDuppx7uXZT6FdQy3QSgShKwfTEyCegsrxpvziOaDUgwyNIRXk1RozoJpA3ulT4mvLEpHjSprI3qVqi6IqesmLlTwp903emWqE-UqziAbUgQbmn1sqVp8x2BQIOZO4SQqgNwDkiPeFljmXWppJWGwoEk6FT02UHe2yvxrITx9EUE-OZl17X2i1-YIA7jCDHfLh0dPHyqk9izAEuitNeSkBoTJMQto2TtAsMHnrU4cxmoN7aXSrpTg64tNt3wHEtgzY3WUly3XHSYVMA_M0ekqJgpWVDg7ceD4TNdAtdlLZ0ium7bWglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
امروز فقط با گیگی
159
تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات:
@manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه مشکل:
@Niiiiiimaaaaa</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120789" target="_blank">📅 11:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120788">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در تماس مستمر با عربستان و قطر هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/120788" target="_blank">📅 11:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120787">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f97d83b5fb.mp4?token=jmJeLWksSToJrQB8Ci31IcFDDVe5AQxIrdHPpR_kxSlgDjj9Z0hGbQAdCLOwk0Dg6uQw2CxqU5NcaCJ8xFKHIvZxXOyjFCCNrWQ0aD1Mq7Xj6pcUSXpc2wk0h6A8PaeBonpGy7HuW4mXd99qRGmCOQjHiyIA45P4QfU3qZIkM1ESGZDvGgbqC3ZDVBOs64gAh71JLLChYlfjB0JXCMRtX1Ce7zRM_bTSWJx7suayS9hEaLqTTYvDHPKVRgO3HhYA2V0jXDzwPkcLBChbEtpwjJnK4EIgQuBOWiCqJEz-Y-xIKAtdabvb8ebzgtR7upaWLQeWaXO6kNUxc03sJ8bDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f97d83b5fb.mp4?token=jmJeLWksSToJrQB8Ci31IcFDDVe5AQxIrdHPpR_kxSlgDjj9Z0hGbQAdCLOwk0Dg6uQw2CxqU5NcaCJ8xFKHIvZxXOyjFCCNrWQ0aD1Mq7Xj6pcUSXpc2wk0h6A8PaeBonpGy7HuW4mXd99qRGmCOQjHiyIA45P4QfU3qZIkM1ESGZDvGgbqC3ZDVBOs64gAh71JLLChYlfjB0JXCMRtX1Ce7zRM_bTSWJx7suayS9hEaLqTTYvDHPKVRgO3HhYA2V0jXDzwPkcLBChbEtpwjJnK4EIgQuBOWiCqJEz-Y-xIKAtdabvb8ebzgtR7upaWLQeWaXO6kNUxc03sJ8bDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده‌های اسرائیل تو ارتفاع پایین، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120787" target="_blank">📅 11:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120786">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ادعای شبکه سی‌ان‌ان: پنتاگون فهرستی از اهداف برای حمله به ایران در صورت صدور دستور ترامپ آماده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120786" target="_blank">📅 11:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120785">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با هیچ یک از کشورهای منطقه دشمنی نداریم؛ همسایگان دائمی هستیم
🔴
کشورهای منطقه به شمول امارات باید از اتفاقات دو سه ماه اخیر درس بگیرند و دیدند که حضور نظامی آمریکا و اسرائیل در منطقه امنیت آور نیست و باعث ناامنی برای همه کشورهای منطقه می‌شود
🔴
رفت و آمدهای فراوانی بین رژیم و برخی کشورهای منطقه وجود داشته و دارد که از دید ما مخفی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120785" target="_blank">📅 11:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120784">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره: نتانیاهو روی جنگ با ایران برای تغییر معادله سیاسی شرط‌بندی می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120784" target="_blank">📅 11:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اوکراین: یک پهپاد روسی به یک کشتی باری چینی در دریای سیاه برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120783" target="_blank">📅 11:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120782">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با عمان برای تدوین سازوکار جدید تنگه هرمز در حال مذاکره هستیم
🔴
اقدام ایران در تنگه هرمز بر اساس حقوق بین‌الملل و حقوق داخلی ایران مجاز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/120782" target="_blank">📅 11:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120781">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
معاون وزارت نیرو: اگر مردم ۱۰ درصد در مصرف برق صرفه‌جویی کنند تا ۳۰ درصد در‌ قبض تخفیف می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/120781" target="_blank">📅 11:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120780">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/529e7b5993.mp4?token=C8O98HlTFdfSjgEONWjT3cuWayKwnBinfJkPOmZ3bvJZVAvx8Zl_q4LcTP-a11fVKlVyWQeoASgL8ZHXTDP25znsPRJ9A-2eoyi0cy_gimGx4jrXOdclhURZO4-qrSC2iUh6fxTB4jq895Dv5JvrM3vZWJz_rlIFWNutNtkWcnY4LPGoMP_Oyc89dfZvT2dzFv0_xUHmJzZTy9lRvGRILVDh10XPQqLDkW1GRzysej8UOzJQS8N8BAOf5cqgNXuISBxEleksg10sesMoV3UX0lulVfZQbSY4w4iSPwqqO3m8roxbXyQ6uQVeRL0ZjEuhFBuHQXgXZA8d2iYp5cD9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/529e7b5993.mp4?token=C8O98HlTFdfSjgEONWjT3cuWayKwnBinfJkPOmZ3bvJZVAvx8Zl_q4LcTP-a11fVKlVyWQeoASgL8ZHXTDP25znsPRJ9A-2eoyi0cy_gimGx4jrXOdclhURZO4-qrSC2iUh6fxTB4jq895Dv5JvrM3vZWJz_rlIFWNutNtkWcnY4LPGoMP_Oyc89dfZvT2dzFv0_xUHmJzZTy9lRvGRILVDh10XPQqLDkW1GRzysej8UOzJQS8N8BAOf5cqgNXuISBxEleksg10sesMoV3UX0lulVfZQbSY4w4iSPwqqO3m8roxbXyQ6uQVeRL0ZjEuhFBuHQXgXZA8d2iYp5cD9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس پلیس راه راهور فراجا:
شب گذشته، در جریان یک تعقیب‌وگریز برای متوقف کردن یک دستگاه خودروی شوتی بودیم. این متخلف برای جلوگیری از تعقیب پلیس، اقدام به ریختن میخ سه‌پر کرد تا بتواند از دست پلیس فرار کند که در نهایت این اقدام منجر به پنچر شدن تعداد زیادی خودرو شد
🔴
در نهایت خودروی متخلف توقیف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120780" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120779">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: آمادگی ما از ابتدای جنگ رمضان بیشتر است/ از سختی‌های مردم مطلعیم کاستی‌ها برطرف می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120779" target="_blank">📅 10:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0L_cUhez7v3cK05ickDvrATrx3QqMrecJigWcaoUX8L1tR3C5UzPU9wNLhM1nWKB0DQSDMHVaSQKQgiKbwR1PUw5TyxS55Ef0rr0Y-6w0L8KTxB2tHwhYYh1s-RWESUCbwO9RbLH4pEqFAwkfSqD6ytLNcqR50a2PoWiXm5pCzaQBhAi9GRsUuA6naxADnHnCBct5m86ueyC3_oP24ix0nBl9OH2GMz4CVs8Z5bxXu1VI3EYgz5vCxHwkwdfqq7kSyLnKLP9MEl3RKZid2J8ZZAPoRbXtXjloH54KOH78Ed0NR88pBzhwJIZr_1tY95LyBE5ebXGFXmdo-PkX60Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح جدید ایران برای عبور کشتی‌ها از تنگه هرمز
🔴
ایران اعلام کرده به‌زودی یک سیستم جدید مدیریت عبور کشتی‌ها از تنگه هرمز راه‌اندازی می‌کنه.
🔴
طبق این طرح، مسیر حرکت کشتی‌ها مدیریت میشه و کشتی‌هایی که بخوان عبور امن (Safe Passage) داشته باشن باید هزینه پرداخت کنن.
🔴
گفته میشه این طرح با نام Hormuz Safe معرفی میشه و در قالب آن کشتی‌ها باید بیمه مخصوص عبور از تنگه هرمز دریافت کنن.
🔴
نکته جالب اینه که طبق گزارش‌ها امکان پرداخت این هزینه با بیت‌کوین هم در نظر گرفته شده.
🔴
از طرفی موضوع دیگه ای که چند تا  خبرگزاری فارسی روش کار کردن این بود که جای هزینه پرداخت کشتی ها بیمه ایرانی بشن و ایران اونارو بیمه کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120778" target="_blank">📅 10:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120777">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
حملهٔ هوایی اسرائیل به دیر الزهرانی در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120777" target="_blank">📅 10:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: از گروه 7 می‌خواهم از رژیم تحریم‌ها پیروی کنند تا از تامین مالی ماشین جنگی ایران جلوگیری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120776" target="_blank">📅 10:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120775">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کانال ۱۲ عبری : جلسه محاکمه نتانیاهو که قرار بود امروز صبح برگزار شود به درخواست خودش «به دلایل امنیتی و سیاسی» به تعویق افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120775" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120774">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
انجمن خودرو آمریکا: قیمت بنزین در ایالات متحده افزایش یافت و میانگین قیمت هر گالن را به 4.5 دلار رساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120774" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120773">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7iLDWMqKIL0IAKgo0WaGBrA8kwVFVzv9NtGmaxKLF9jh6Hbk6CV65oGUvsPx6PAjGbUTRIlGrx046OrArFTHq83OC3YOb6wBoX20eYgd3Pkhg68h2Nq9W2lP_o-hyIJM4fLFi9BPImCg4Q29-KzhVAs4wW76whvmkR6NMU0VfsMJUF9YgH6iDA2IrgJ_2x4W4dHEAkvaftilFDMp680qgxwKgUwxEaA-HYVz_Ge2YXyoFHMMW8G4PILZk-qO2_SyCZc8Ns61hHReEDl1DUdl_wEJ-b_G6sXBCkiBjCE80HHwje7deFxpGGiOtg6Tlcdxn9zwCbPniqOi-eNG8qazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان نایب رئیس کمیسیون امنیت ملی مجلس: مجدد، تهدید رهبر انقلاب و فرماندهان نظامی از دهان نجس برخی  مقامات دشمن شنیده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/120773" target="_blank">📅 10:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120772">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
از ساعت ۱۰ صبح امروز انفجارات کنترل شده در شهرستان دزفول انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/120772" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120771">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbff622c8.mp4?token=DdoTmdd-XQYZaeTvX6sbLZHDsvFEVOqvbgiIXktsPF3W2AgS5Jn1fAnO47v4FbdeBRy8VWX0G8ylwLvwQDT2PtalaEs7jS11FCUNmLcdFO4Vs_7TiFwnklOOmWCEDbOc6cI1FlAHy_MTskK2dkvsM2_4DkxMCuKnLKAHXkomzK7c-jjeA3YVGtvG8Nx1gyjR0L54CEobY0p-XelZ80aTUsIy5bMM3qdWhi8kVwpYe0mBBxelnJR6wDA-tp7WAYTmiTGCR14H9eqhbgbHZmoaUPQTE7_9Rq8O7kLwWWorF_3oi4imsb7zoaZhlq_ifvQMEtocHzkD4XZ-7qOnTlDoVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbff622c8.mp4?token=DdoTmdd-XQYZaeTvX6sbLZHDsvFEVOqvbgiIXktsPF3W2AgS5Jn1fAnO47v4FbdeBRy8VWX0G8ylwLvwQDT2PtalaEs7jS11FCUNmLcdFO4Vs_7TiFwnklOOmWCEDbOc6cI1FlAHy_MTskK2dkvsM2_4DkxMCuKnLKAHXkomzK7c-jjeA3YVGtvG8Nx1gyjR0L54CEobY0p-XelZ80aTUsIy5bMM3qdWhi8kVwpYe0mBBxelnJR6wDA-tp7WAYTmiTGCR14H9eqhbgbHZmoaUPQTE7_9Rq8O7kLwWWorF_3oi4imsb7zoaZhlq_ifvQMEtocHzkD4XZ-7qOnTlDoVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از زلزله‌ 5.2 ریشتری در جنوب چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/120771" target="_blank">📅 09:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120770">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بلومبرگ: بی‌ملاحظگی ترامپ درباره تایوان اشتباه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/120770" target="_blank">📅 09:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120769">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بیت‌کوین به پایین‌ترین سطح دو هفته گذشته رسید
🔴
بیت‌کوین ضعیف شد و به پایین‌ترین سطح خود در بیش از دو هفته گذشته رسید، زیرا ریسک‌های کلان گسترده ناشی از جنگ آمریکا و ایران معامله‌گران را وادار کرد موقعیت‌های خود را کاهش دهند.
🔴
این ارز دیجیتال اصلی در روز دوشنبه تا ۷۶,۷۱۱ دلار سقوط کرد، که پایین‌ترین سطح از اول مه بود، قبل از آنکه بخشی از ضررهای خود را جبران کند. سایر توکن‌ها، از جمله اتریوم و سولانا، نیز کاهش یافتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/120769" target="_blank">📅 09:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120768">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b623dbe873.mp4?token=H_a99jnzf7znojxvvTbgj9kdEb0FTbuf6dyHawc1p6BU4leX6oBMRaW9MFgQfdvLaULtEsRbRm0Kr2WxJbNg3_6FhW0EyQQuj4V1PGn0m11eAWpGK6nsvi1yR22UKPUU8ECo3ELOT_3ylrHDd7jhDvkmaEAKLzL0jaI7QVwFoOCpzv60Pk1wasATddzouKDGWt52CdS9addblhMx51KF-eJ9ZXPx73J_QL5eK647zZF1oG_8xjV9hj4gLyqq9BK0g_42BoTQmmCtQk7q2ASZrEjmDjEYAeFAkeA8b4SHf-ZFKP11ZgG-dMWnK2ZvcTz18jaGLnfuB2y0Cle49B7NMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b623dbe873.mp4?token=H_a99jnzf7znojxvvTbgj9kdEb0FTbuf6dyHawc1p6BU4leX6oBMRaW9MFgQfdvLaULtEsRbRm0Kr2WxJbNg3_6FhW0EyQQuj4V1PGn0m11eAWpGK6nsvi1yR22UKPUU8ECo3ELOT_3ylrHDd7jhDvkmaEAKLzL0jaI7QVwFoOCpzv60Pk1wasATddzouKDGWt52CdS9addblhMx51KF-eJ9ZXPx73J_QL5eK647zZF1oG_8xjV9hj4gLyqq9BK0g_42BoTQmmCtQk7q2ASZrEjmDjEYAeFAkeA8b4SHf-ZFKP11ZgG-dMWnK2ZvcTz18jaGLnfuB2y0Cle49B7NMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم سابق آلمان، آنگلا مرکل:
هیچ کشوری در جهان نمی‌تواند همه مشکلاتی را که با آن‌ها روبرو هستیم به تنهایی حل کند.
🔴
حتی کشوری به بزرگی و قدرت ایالات متحده نیز، به نظر من، باید علاقه‌مند باشد که چند دوست در جهان داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/120768" target="_blank">📅 09:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120767">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a53fc05.mp4?token=g4xpO_tu7xnFj4Hy9Ic4lJHirHvdM916lsDpnP3CKr5NNeIqhkSpJVLhxHOWIFYrJA8MwAxhDrIoxBNUMAdKaRFsUz0AaXzUw3TAH253CZ1Idar5WcknsmKbbmoV1DmbRhPZfr_LSuvjwKVpuMg6lywmgaPXcdMR483HdqstP3VXySMuKko022v1fE23UWQYWPx82QYA2opRgti8c4W_nIlSgJGXtV8NA3rJP_OaATbPNHjLo6XPd0Ob18pTVbvgVVUIdMPMvXuh3UkDy8m3t2ugnypeZReImKFwyMW6KcQmuFUCDJ0Jitl1wqc70PqgAs63bdGgA16kOOfooaeH5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a53fc05.mp4?token=g4xpO_tu7xnFj4Hy9Ic4lJHirHvdM916lsDpnP3CKr5NNeIqhkSpJVLhxHOWIFYrJA8MwAxhDrIoxBNUMAdKaRFsUz0AaXzUw3TAH253CZ1Idar5WcknsmKbbmoV1DmbRhPZfr_LSuvjwKVpuMg6lywmgaPXcdMR483HdqstP3VXySMuKko022v1fE23UWQYWPx82QYA2opRgti8c4W_nIlSgJGXtV8NA3rJP_OaATbPNHjLo6XPd0Ob18pTVbvgVVUIdMPMvXuh3UkDy8m3t2ugnypeZReImKFwyMW6KcQmuFUCDJ0Jitl1wqc70PqgAs63bdGgA16kOOfooaeH5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدر اعظم سابق آلمان، آنگلا مرکل:
ترامپ فردی است که با شدت بسیار زیادی اهداف خود را دنبال می‌کند.
🔴
هرگز نباید افراد در چنین موقعیت‌هایی را دست کم گرفت. کسی که به موقعیتی مانند ریاست جمهوری ایالات متحده رسیده است، قدرت بسیار زیادی دارد. و به همین دلیل باید او را بسیار، بسیار جدی گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/120767" target="_blank">📅 09:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120766">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قیمت نفت خام برنت ۲ دلار و ۳ سنت معادل ۱.۸۶ درصد افزایش یافت و به ۱۱۱ دلار و ۲۹ سنت در هر بشکه رسید
🔴
در حالی که ابتدای معاملات تا سطح ۱۱۲ دلار پیشروی کرده بود که بالاترین قیمت در بیش از دو هفته گذشته بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/120766" target="_blank">📅 09:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120765">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پلیس راه: جاده قدیم چالوس ۳ روز مسدود است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120765" target="_blank">📅 09:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120764">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جروزالم پست گزارش داد: نتانیاهو خواستار لغو حضور خود در برابر دادگاه طی امروز بنا به دلایل امنیتی و سیاسی شد
🔴
دادستانی اسرائیل با این درخواست مخالفت کرده و جلسه را به بعد از ظهر امروز موکول کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/120764" target="_blank">📅 09:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120763">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وقوع انفجارهای کنترل شده ناشی از عملیات خنثی‌سازی در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/120763" target="_blank">📅 09:33 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
