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
<img src="https://cdn4.telesco.pe/file/MTLAxeaui2u_Zq6hgfHRnz6xUtsvPzTZOtnbY9LJpJ2D8XO6SNwxZaI9exg4rqLHDw9pWmFF4ehG2LrpgPWwgQejErWrAFDO5b1STT7CIwyk0uu1jdPM4QgM_DqnTSACtvA9J3gUSmaKBUK8XQACdC2szPWZawu3Bgu8D_q5usyXZt3wYLqq40h6vdB5nKpvNu8zA4wM8L5Fr5y60tjsSuCR41dMYAAke2KSdb-jVMfX8GkK7Cuizn4FAi6sp0Yer_iZJNf16Ak2UsI--KjpiVCpeAl7T9ciV8E8wqAnjqj1CkOnwkj5N8MWqF7Zk5wvurrEe-8A75_JuzELiavguw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 20:22:01</div>
<hr>

<div class="tg-post" id="msg-142285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
الجزیره: رفت‌وآمد کشتی‌ها از تنگه هرمز برای سومین روز متوالی به پایین‌ترین سطح خود کاهش یافته
🔴
روز شنبه تنها ۳ کشتی، روز یکشنبه ۲ کشتی و امروز دوشنبه ۱۷ اوت نیز ۴ کشتی از تنگه عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/142285" target="_blank">📅 20:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f4b01950.mp4?token=ScGeHhgb19vejyJn69e-irh5_9sJhkBGe2ioknp86urNbT-XSvdJg9q2uAFou3cmsv8I_65IHPJOjEM30Rzs7zzzJbYW1DD36m1gezxjKsYjTs9r3mlbyVxHUi2u2QbUSzDgeleLaxVCGpNkPxzukG-X9exIotGK9aVcRIoqLiGJYU8oRMNCuetZW9I4a4F7u3hmY7XBHEeV6ayMd-pvD5RJk9xbeOnmnR1MCCnWQ6SzbhsXJt7MXgNKtZsEPKcB79bB7FdnEwuaJxee_FxpgIr2IhbHYoJxi_Vd60kY0lKNJL46ojeC2vNdtXAXqiMLYQcys8rUlQaGayeIbIGhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f4b01950.mp4?token=ScGeHhgb19vejyJn69e-irh5_9sJhkBGe2ioknp86urNbT-XSvdJg9q2uAFou3cmsv8I_65IHPJOjEM30Rzs7zzzJbYW1DD36m1gezxjKsYjTs9r3mlbyVxHUi2u2QbUSzDgeleLaxVCGpNkPxzukG-X9exIotGK9aVcRIoqLiGJYU8oRMNCuetZW9I4a4F7u3hmY7XBHEeV6ayMd-pvD5RJk9xbeOnmnR1MCCnWQ6SzbhsXJt7MXgNKtZsEPKcB79bB7FdnEwuaJxee_FxpgIr2IhbHYoJxi_Vd60kY0lKNJL46ojeC2vNdtXAXqiMLYQcys8rUlQaGayeIbIGhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع سابق اوکراین فدرورف:
مرحله بعدی این جنگ، ربات‌ها و پهپادهایی خواهد بود که با ربات‌ها و پهپادهای خودمختار دیگر می‌جنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/142284" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روزنامه دیلی میل به نقل از منابعی نوشت بانوی اول آمریکا نگران است که ایران، رئیس‌جمهور ایالات متحده را ترور کند و این مسئله موجب ترس همسر رئیس‌جمهور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/142283" target="_blank">📅 20:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXFfku5bJTGhmzs7FVvvB_h3cMlxwhfTC6kcVDsZLU6RnAbG9iVSEI-QyPS5vzijuKAOBVWLZPUa7KXKdOCU9vXStsmYozXi0eXM3V0E3G44PlWytI_3dpQ0FxIcRFy_z4ixFyGfXXXsHPiTFnvF9kygJ5rul8ixzrZZyY0PsjbWzu-AJNBkUXoTaaerKCiRvdv5nLhjs7408Wc79ltN-in53dtW-6VgMu7nU2hX0p3GcyvUs7cyGCxmaBtM7yb9Cs67XBbBsEwuvHvly2-gan9raxLVrnsU-DrH9b8KKvyAQBY3eILhMRVO1PO7DcJU2wvZ84wL4RG6vkt6UYmcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف: روسیه دست‌کم ۱۰ پایگاه پهپادی با ۵۹ ریل پرتاب  نزدیک بخش شرقی ناتو ساخته یا گسترش داده است.
🔴
سرویس اطلاعاتی آمریکا ارزیابی کرده است که روسیه ممکن است با یک حمله محدود، این ائتلاف را آزمایش کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/142282" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از یک مقام اسرائیلی: ما در دیدار با کوشنر تأکید کردیم که هیچ چیزی را که زمینه ساز تأسیس کشور فلسطین باشد، ارائه نخواهیم داد.
🔴
نتانیاهو از دیدار کوشنر با رهبری حماس انتقاد کرد زیرا آنها معمار هفتم اکتبر بودند و کوشنر پاسخی نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/142281" target="_blank">📅 20:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c492661c3.mp4?token=vOQ9Va1Hc7ktXsI3-FD022bikj894XEM6ILsMjs08BZhJWr-3icE8x-StgveepSYcUHez4DbtJqSUS8vMdY3OV7L6YcooAncUci8LYEEb5zK6WRSWwSLpwmQmkPOUnoLME4rCSf1xxD1EhVEc3uupBd-TUbE31TKb84eQNjnY8FcTUT_zXYcsB5Dfb3dPkqHchHg8xu1G0-5GlWzn7J73F9Xwk8lBnsBIDlyto9Qb5ADnK3bUuZrPrerz3WBiOtX2rXgzlWD0MCwXmoimE1qFiXeHbqFqsTp1uRRc36yjGzt2PKUX4mtg5AC2iiffk65ep4sKnv2-r1wMrmO4SO5t4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c492661c3.mp4?token=vOQ9Va1Hc7ktXsI3-FD022bikj894XEM6ILsMjs08BZhJWr-3icE8x-StgveepSYcUHez4DbtJqSUS8vMdY3OV7L6YcooAncUci8LYEEb5zK6WRSWwSLpwmQmkPOUnoLME4rCSf1xxD1EhVEc3uupBd-TUbE31TKb84eQNjnY8FcTUT_zXYcsB5Dfb3dPkqHchHg8xu1G0-5GlWzn7J73F9Xwk8lBnsBIDlyto9Qb5ADnK3bUuZrPrerz3WBiOtX2rXgzlWD0MCwXmoimE1qFiXeHbqFqsTp1uRRc36yjGzt2PKUX4mtg5AC2iiffk65ep4sKnv2-r1wMrmO4SO5t4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو نخست وزیر اسرائیل: به رای دادن در انتخابات مقدماتی لیکود بروید و تیمی پیروز انتخاب کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142280" target="_blank">📅 19:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X882H5LGzRq5IG-SiVnxvTj0vtibRNQjqOLWwYiAK9hVV1mXyD-b9llo8g0kV31P71_oyYAklVgZSaFP6XNivraQ5ar82gnMeoxnWHnEvDXNvRxGn11b-b3vvN2A6eRzcCS2oXmaCXE41tXz7eH8Gs2xtM6ypcKIZzUjxQAoejL8EvsaN1nHOW_dA6ls0q1ooq5VgGG8CvmjaGoZj1Wb8y7EeEYEdSjeeN6iFTjPuRPQxLZpmslNiUk7aup5Ja3ZNymDJDaOIyK4IglT6pa41ELCuBUkd5G_xMobsBBdmHLsDEOsxDfyLGQ8CFDAxPidzUVoOayu4xgiJ9T9i1kjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQF7-2OlEJa-JCuOHYgV53aZ8SO9JeEA1ALO7BgcZgUzrA77r7fUcVzK8AtwPuVc2-YPWCnJa2faWjTEnVu24rl8fOPlYX3I3YP6Ol90PNuSjCaw4Ura4qHOap1vGqSSieKaE3kC7zgzOM7wAsiY2qMevyiTiwaM1GuzDY6RooHa9LAkiIrXPbBZCDJalwSODqpsybr2AnQ5a898cNembzFgEvIUyYJnjgONwXfA6Vu51xSIDMFM1fUnBqERmMbwVp3mG_6gfl5Tsiu70iGG5MFlStrRMQQ83nZGK5-DSI0b-43vLTa7HkTlG_jgdCK2YoejXr02GsrZDuPX0e0xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7piSbMCUsUc9p8Dvi7g5zzvmmPRzLG3Vcebr4492M8OyhRHpq_aGSGEipP9nvz2qiIcllrT87mSHLYIbIOD3dl9T2Chtiy-Mqv4JocNkkTSdXJcm4rkoOo9RzGbvoydcocMfTCQVUR_S0oB0Ai0CIR2P_mTewWTDAHLwLRi_icacgVv5J-RswpLz8GfTnoZhHYWvimDuAyXdgXwg9BBdqzVav57Vfwg3XyWJzaeJpmmANTvVYWbZBG3TXgcOL-6197SI4cE0EYhoKlt_vHlW2dwPzgK4d4GrZkuM0otHv-H2MsPQLu0BmAfkV1v5iAKW-9MDtWYd8ruT3I2hVKB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlXj6ECpN2x1RunH2RzmntEWgO-YNY5FygQNdDTmeq1l4klAaDX6v29nOPg4HYTQGLeqf4y9l3Y0GWL_u2kFZVY-MUAXzgoQq49gZZSLP3eFWRLIe75dq3AXCCr7UPBSfiAJj_87uipgoSZk_sTNmN6jnOJTQZ5K621pypeAY_enfI7PkjZP-qCw3CNTGgTi0WlZSn31jcnwJZIN3RUgsguhavS2XInqPGqFWyegMOR52KFBmMXjDlqI0LhT_dxr1JTCyAnqke6cZpAp8FgkrVxOb1Le9zNh4skbcDilZMLIf55zy5VvEOy8byE_OdGfFOmsoDwVDnIQYiy3no6Kcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعاتی پیش، جنگنده‌های نیروی هوایی اسرائیل به المنصوری در جنوب لبنان حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/142276" target="_blank">📅 19:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCkSVpdR_yQp0_Cys46LFrmdxPVnhY6S7M7FjrQRgDIYYfg6sNzvyanqdyYzDQPQTfsjn1URK_b8cDza62S9zTzx25ADsZTfv0To8KrcWWCySNi1q1Py3m0LqegFm5jdLk_DV1eR8GP1Pjxz4Ti5BW4fUEicMaLyzJhYnDzMpIQ4jZAxUsC4_jTVCk6Qv3N32oXQyMqmrTOEnaoeVJwNc58FEDzQ-E_mrFD1ChJEOy1znwXsJeAiWN9x-kIW22gQ8_W-qlXf0S2REreb_BOGxEyLV42vWbyr1NVxxsFGyIhwlng-qcGYeo3PpJPgJOMZ3rrMwtm4PVIVSlBMBACafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس: ترامپ باز هم حرف از تسلیم ایران زده است. ایران بزرگ تسلیم‌شدنی نیست، کسی باید تسلیم شود که با ماشین غذا و با خفت و خواری فرار می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142275" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72764905ee.mp4?token=IgVBlkWCWmEXgDN4dCALjXxyif7Mq-7d6X7xpo2Z9ly4jfpAvwuHG6IIN2lL0g7Cab0x486PAxbw6xvcjAGxyysy2QoHRcNARMmZihoscWiLVyn44miJE1v5F_wjHTVEHlHgQSDj4TERvs074DCpbe4K9uR01cSrcdKKiNY-P9GQ368zxwDGuyYpH1w2qYPvhuc341Wz_RGWRYDjSt4JrgPE4qgMI1H1vZF3sNIWM7O5O2oDyesNCnwBb8q_uT5eJ5ot5VqzqtQSpamXNEumMWwkGQ2prqUNOEdbFjXRuh_bCWauWCb6B5Hk0WZUZly7d5FjY6hwrbwTL0A1iPL-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72764905ee.mp4?token=IgVBlkWCWmEXgDN4dCALjXxyif7Mq-7d6X7xpo2Z9ly4jfpAvwuHG6IIN2lL0g7Cab0x486PAxbw6xvcjAGxyysy2QoHRcNARMmZihoscWiLVyn44miJE1v5F_wjHTVEHlHgQSDj4TERvs074DCpbe4K9uR01cSrcdKKiNY-P9GQ368zxwDGuyYpH1w2qYPvhuc341Wz_RGWRYDjSt4JrgPE4qgMI1H1vZF3sNIWM7O5O2oDyesNCnwBb8q_uT5eJ5ot5VqzqtQSpamXNEumMWwkGQ2prqUNOEdbFjXRuh_bCWauWCb6B5Hk0WZUZly7d5FjY6hwrbwTL0A1iPL-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالن جاسوسی آمریکا مجدد در آسمان استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142274" target="_blank">📅 19:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
🔴
طبق ترتیبات ایران برای عبور امن از تنگۀ هرمز، مسیر ایرانی یکی از شروط است و پرداخت‌بهای خدمات و اجازۀ ایران از دیگر شروطی است که نفتکش‌ها باید رعایت کنند.
🔴
نفتکش امارات در نزدیکی قشم متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142273" target="_blank">📅 19:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ما هر شب باید حداقل ۳۰-۴۰ تا ترور هدفمند در غزه انجام دهیم. نه فقط اونایی که برای ما خطر دارند، بلکه اونایی که ارزش زندگی کردن رو ندارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142272" target="_blank">📅 19:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foCQp7RMbgoWdlcr2JyLvyXcYN1K0ViqtChNfUmFUzhkx6i0rIeRw8q2n1fqvMFxt7unLaRPWfjctOdMFgBvyW8XdBT197gqIYqu4-ZWG8-TWjHUIr8enP6f9ILzKGUD-XP9OYHbXcmMHEQ7NX0_KHx1ct0hWn4AScbCgMQAmnoPTA6Mpk0jiK8tUrzI1gXEVvQAJCehgNGyZ-ItnJspuTkMFRxXulasDN7OPVSOjinAvd9C-RiT5pHSe3PkxXoEIABtZd_Wx_0K4In9csmEHc073Tm0X3BXgdm_bn4mifAW3-CxfyOHGUXSMhrMd7Ckc8OeoGIlzznAn9BAMNL-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ما هر شب باید حداقل ۳۰-۴۰ تا ترور هدفمند در غزه انجام دهیم. نه فقط اونایی که برای ما خطر دارند، بلکه اونایی که ارزش زندگی کردن رو ندارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142271" target="_blank">📅 19:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان: کوشنر بیش از چهار ساعت نتانیاهو را تحت فشار قرار داد تا طرح آتش‌بس ترامپ برای غزه را پیش ببرد
🔴
نتانیاهو در برابر این فشار مقاومت کرد و با اشاره به انتخابات اکتبر، تأکید کرد که پیش از هرگونه عقب‌نشینی اسرائیل، حماس باید به‌طور کامل خلع سلاح شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/142270" target="_blank">📅 19:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c96f732b1.mp4?token=tE0pcG2EhK-pyWQu1cRN7H9yjaLRfqYZPjpMyZKf8pqr2VUS8T1I5vQFq8NYSjqcQ6-cwTtYykRZc43HNUP2IJUwyvsUAyJSPpNCuHtEGE4Nz32_L58cAQ8EqqypkIOqAUpWdWUMAA3GDKyzBS0fvbrALLUy66yas0KS51cEq1AB1EJF0_Y9pMAyUv01Qr5aYTs1xed0xzca_Wcke-21fAUmrf7m9QsVnfvUFUKxMXnE2GAVIiNrNKBo4OWkSXKk_K2sFkV2Yp1mXTdt1bWyQt3c0poagpP7wjgVoi6Mk_cUun4jvzUjIAPbr9BsXx-gZSrF5ESHe9Nt4uhfCD_kVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c96f732b1.mp4?token=tE0pcG2EhK-pyWQu1cRN7H9yjaLRfqYZPjpMyZKf8pqr2VUS8T1I5vQFq8NYSjqcQ6-cwTtYykRZc43HNUP2IJUwyvsUAyJSPpNCuHtEGE4Nz32_L58cAQ8EqqypkIOqAUpWdWUMAA3GDKyzBS0fvbrALLUy66yas0KS51cEq1AB1EJF0_Y9pMAyUv01Qr5aYTs1xed0xzca_Wcke-21fAUmrf7m9QsVnfvUFUKxMXnE2GAVIiNrNKBo4OWkSXKk_K2sFkV2Yp1mXTdt1bWyQt3c0poagpP7wjgVoi6Mk_cUun4jvzUjIAPbr9BsXx-gZSrF5ESHe9Nt4uhfCD_kVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مقام‌های محلی در ایالت اوکلاهمای آمریکا پس از وقوع آتش‌سوزی گسترده در یک مخزن گاز طبیعی، دستور تخلیه ساکنان اطراف محل حادثه در شهر گلن‌پول را صادر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142269" target="_blank">📅 19:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت نیروی: 4200 مگاوات برق را در نتیجه جنگ از دست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142268" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع بلندپایه ایرانی: حادثه‌ای که امروز در اربیل، در اقلیم کردستان عراق، رخ داد، نمونه دیگری از عملیات «پرچم دروغین» است.
🔴
ایران هیچ ارتباطی با حادثه‌ای که در اربیل رخ داد ندارد و عملیات‌های ایران به‌طور رسمی و صریح اعلام می‌شوند.
🔴
هرکس به حاکمیت ایران احترام بگذارد، از احترام ایران نیز برخوردار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142267" target="_blank">📅 19:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام اسرائیلی:
نتانیاهو و کوشنر توافق کردند که یک ژنرال آمریکایی بر روند خلع سلاح حماس نظارت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/142266" target="_blank">📅 19:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
یک مقام دولتی پاکستان در اظهاراتی به «ام‌اس ناو» مدعی شد که مذاکرات برای بازگشایی تنگه هرمز و پایان مسالمت‌آمیز جنگ ایران و آمریکا همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142265" target="_blank">📅 19:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0512c8ba1b.mp4?token=g1rOb43XcgdH9XDY2fxc1hd-_rAUrINnD96GA6Iokp41SVLfbu9HpsvIhv7LIgN5bVmQfXaFxNTjKZ2u_y3oaJYHS0BB3Hgev1DY7V_vuTVxQOOCCt_r_NCb0hrMZmYJu_qAyzP0s-S3vwjK_4NXf4QsppliLYPbFo0gYQnUZFZ-7dA8uyxVz_0vsbSv0ohuDYEZr3qzoXGzIZgSxY5qbGPP3yrNu5rC3eKziiqVb_CkBpvG8njh54J1Md-NsfJ5fxnpkprlr8A-2kUOrQm8c8I_RVtwhGvBX4OSJabGZM7AazItdkkVM8pkxSc9GBDL9TjLvC-l-KuVWnE-zwsW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0512c8ba1b.mp4?token=g1rOb43XcgdH9XDY2fxc1hd-_rAUrINnD96GA6Iokp41SVLfbu9HpsvIhv7LIgN5bVmQfXaFxNTjKZ2u_y3oaJYHS0BB3Hgev1DY7V_vuTVxQOOCCt_r_NCb0hrMZmYJu_qAyzP0s-S3vwjK_4NXf4QsppliLYPbFo0gYQnUZFZ-7dA8uyxVz_0vsbSv0ohuDYEZr3qzoXGzIZgSxY5qbGPP3yrNu5rC3eKziiqVb_CkBpvG8njh54J1Md-NsfJ5fxnpkprlr8A-2kUOrQm8c8I_RVtwhGvBX4OSJabGZM7AazItdkkVM8pkxSc9GBDL9TjLvC-l-KuVWnE-zwsW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما فاش کرد: قطعا ۴ اسیر هم در کویت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142264" target="_blank">📅 18:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142263">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک حمله بمبی به یک مدرسه خصوصی در کابل انجام شد که منجر به تلفات ناشناخته‌ای در میان دانش‌آموزان شد.
🔴
مدرسه مورد هدف در منطقه‌ای واقع شده که عمدتاً توسط جامعه هزاره، که عمدتاً شیعه مسلمان هستند، مسکونی است.
🔴
هیچ گروهی مسئولیت این حمله را بر عهده نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142263" target="_blank">📅 18:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142262">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
داده‌های شرکت ردیابی نفتکش‌های «کپلر» نشان داد که عربستان سعودی در پی افزایش ناامنی‌ها، ارسال محموله‌های نفتی خود از مسیر تنگه استراتژیک باب‌المندب را موقتاً متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142262" target="_blank">📅 18:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یکی از ممبرا پیام داده گفته پارسال به بچم گفتم پول چیپس‌هات رو بریز قلک سال بعد پول زیادی جمع کنی اونم پول ۵۰تا چیپس رو ریخت تو قلک و دیشب باز کرد و الان پول ۵تا چیپس داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142261" target="_blank">📅 18:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVDepP_lsYawjZYKagTJ1dgTCJA1oxO6ufKi7xRg_OMZGvKUz79l021P08SQ_NQhjcTKTfDZTL49T4H3bOr_twsnk8LIMfrQz6EsCmUAK51RicJaX_h4z9E4M7PFSuddr_tp65TKMFVTzh0snAMgiFusQMfvFf6b0CobtEpSW9b_3arOv-kQZ8B8gMpeDxtOK4JGX2H2JYhXWP-5CyIuPJypXeEZiAWYI55I4hI2RFps_1_7ywWttl5qMfB3R73jk2Ch3YHP8kpPiD9LzBsfSlFaB2LvLKDpOLw4zCqVu-di6MEwMyrz48TnnVW_tD5mR710sZbImOFj3846HNKgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر نخست‌وزیر اسرائیل: نخست‌وزیر و هیئت صلح گفت‌وگوهای عمیق و سازنده‌ای داشتند.
🔴
توافق شد که دو گروه کاری تشکیل شود؛ یکی در زمینه خلع سلاح و غیرنظامی‌سازی غزه که هم اسرائیل و هم هیئت صلح مصمم هستند این کار سریع انجام شود و پیش از هرگونه بازسازی در غزه به پایان برسد.
🔴
گروه کاری دوم بر بهداشت، آب سالم و سایر مسائل بهداشت عمومی برای مردم غزه تمرکز خواهد کرد که این مسائل همچنین بر مردم اسرائیل نیز تأثیر می‌گذارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142260" target="_blank">📅 18:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhUa1x1FQhEYxfdeTCBI17AzEQtw9tgjs2KHxap5yjiy5s1gJX9qOrZ2V07w7nFQc3oWf_Kdpl87q9wrjtayozScTW9nuoCAmhmqkauFoAlcU_pnxAMK2DbUsgzuvUIPExMF_FZCeRONNpw7SuaUUEg5Kj87JkNX8141mgk64c0D1p6a1HaCEN6UVOyja1vj01WKzlFi7a9ZtXdQsIzFv8VVU1gJpCUHfVCU26bWW3N0yLALBk9Htt7GfaClpRObBbMVq0JxH0A4-GvAVYa1c2Q_MPbVCAOTQIitTY5obHqKspgfpJ8Z8Jwl6fkEyF5fi5QvvqDbb-Yekozgwt9YRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
د
رخواست صلح از طرف پاپ!
🔴
‌بار دیگر درخواست خود را برای پایان دادن به خشونت‌های جاری علیه غیرنظامیان فلسطینی در کرانه باختری تکرار می‌کنم و فوراً از جامعه جهانی می‌خواهم برای پیشبرد راه‌حل دو کشوری و دستیابی به صلحی عادلانه و پایدار تلاش کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142259" target="_blank">📅 18:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhFpWBcX5-gSyUhPZ9ToclqFrrL0Su7v7OC4wgpZb7joeqBYof5zW86IKCHVI28uUNve2YvSpU5Wv7i-E1FGDEvsYU2M7OToGQjFdB_hMGlWhvYhcCLfL62Vm47R89ziuxspf-qQ2OR3gioEuMmG9xcIyK0xWFzwtFc2OgyYBoKcYuuPU-ezr3a0MRLGvIuzkurnakXBgnXTmEHfpj1K-eYebz9-K1tKSkCGtzCAuvbPBeXgF0O7kowoKuN4aOD5YJoUBBM3MiF_wnY2Qv4CKT5RYZpS7mzItrtqB0YCUgk6bMC6VPvU4IjKm79lkogUXYtEPAaXFIc2clfzGWdRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ریتئون از گروه RTX قراردادی به ارزش ۲۲.۹ میلیارد دلار و به مدت هفت سال با نیروی دریایی ایالات متحده برای افزایش تولید موشک‌های کروز تامهاوک به بیش از ۱۰۰۰ موشک در سال به دست آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142258" target="_blank">📅 18:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142257">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس جمهوری لبنان: از برقراری روابط با ایران بر اساس «کشور با کشور» حمایت می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142257" target="_blank">📅 18:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb511082b.mp4?token=YIpnaAe79r8BZAbgbNwYNw6L7ms1cB78rMmr0Z6-vK-Ko0W-iNKeaLXUH0zznkHR_FmWk8H8OJV1xz3CcNXl566xpVSVFNF_KBnitwZ6F4iE93NqDIdmCdt_4sGuW2Wv8NNrsVFTuK4hA-9v3kFETb4-BdNdv2ylhnuHqLuWZ8q0p3YKsJkr1ngf2-6FvvKDs9NK2dCp0t8dL-ogP7t0CCunjiqZp7Hrj6cgSFuQb6X1Mo6rX9LGro6IR49u7LgVP0BR9nRCv3S-Uo4njVl3SajrA9MjQVg2mcTbS_fF--gAgS9AlqF6Cc1-ol_4AG-Fb9ZfiqEm-RqGEpp150BmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb511082b.mp4?token=YIpnaAe79r8BZAbgbNwYNw6L7ms1cB78rMmr0Z6-vK-Ko0W-iNKeaLXUH0zznkHR_FmWk8H8OJV1xz3CcNXl566xpVSVFNF_KBnitwZ6F4iE93NqDIdmCdt_4sGuW2Wv8NNrsVFTuK4hA-9v3kFETb4-BdNdv2ylhnuHqLuWZ8q0p3YKsJkr1ngf2-6FvvKDs9NK2dCp0t8dL-ogP7t0CCunjiqZp7Hrj6cgSFuQb6X1Mo6rX9LGro6IR49u7LgVP0BR9nRCv3S-Uo4njVl3SajrA9MjQVg2mcTbS_fF--gAgS9AlqF6Cc1-ol_4AG-Fb9ZfiqEm-RqGEpp150BmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری مشهور آمریکایی و از افراد نزدیک به ترامپ، صحبت از به کارگیری بمب اتم علیه ایران می‌کند
🔴
مارک لوین ایران را با امپراتوری ژاپن مقایسه می‌کند:
"رژیم ایران تسلیم نخواهد شد.
🔴
می‌دانید، ما قبلاً در جنگ‌هایی بوده‌ایم که با دشمنانی جنگیدیم که آنها هم تسلیم نمی‌شدند...
🔴
ژاپن را یادتان هست؟
متاسفانه، ما مجبور شدیم دو بمب اتمی بیندازیم تا آنها تسلیم شوند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142256" target="_blank">📅 18:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLtDOsQjBp-fYHYOmpVvSRNPIS1gTliWAcJ9TrBVXw_XqCHGyunbOlzOdXema3dtLytfMK2qgs5WjFLsGMti478tBt3mK-6K4ATVQMv3nk8m27Ph0ChmyRYXR2ny1_22VzypfEmM89URgXs4t3mMyZAjNUjXgbfmLy82mSK3YGsWk26P2OtZ3laD9LxsEyXITAv7W39C5IjYTscSF0gNYCYqP7oZbo-LiCoqw9UNaXROiiswolok0x5gGM3E34y-Wv4C_kwlzes3Oj7II1SetUe4QPbmp8VvJ8188z8jMh_uMugILGG76dAr_GueozQt-Vgzw7fyWcoDNcbdP0RMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
۲۰۰ میلیارد دلار زیان در بازار سهام امریکا در معاملات ابتدای هفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142255" target="_blank">📅 18:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142254" target="_blank">📅 18:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a545b29a7a.mp4?token=eO1-lwbdS6pzzbcW01NIdX9vseR6wE7RmnZp8nTJhhySD6ykzpDL0PuF4QDROh7DY1hvnOPCHL9SmwJ6yXuDVaF-ChmygRvo9awtGULkSn2Aj7qvEm3VjtkFrXgi9BP8tbQm9Sx4Roo53L1BT5uhyT4NXWctqA03nEqmav73KN0QOkKs72zVGkTzlY_mH3FkH5INqaSTJCx7A3PkY9OxqmTl7CZYEo0YtCp0qkN5LVpuowqM-3pnAW3Gr7QgOEMU8VzGemABXOvU7BjtETsAPgLqNb389lXyTZWvYV-MFtvJ6yP5yT78QlJ2r_7GIPxQcbR7rCLOJHmKH465X_JtuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a545b29a7a.mp4?token=eO1-lwbdS6pzzbcW01NIdX9vseR6wE7RmnZp8nTJhhySD6ykzpDL0PuF4QDROh7DY1hvnOPCHL9SmwJ6yXuDVaF-ChmygRvo9awtGULkSn2Aj7qvEm3VjtkFrXgi9BP8tbQm9Sx4Roo53L1BT5uhyT4NXWctqA03nEqmav73KN0QOkKs72zVGkTzlY_mH3FkH5INqaSTJCx7A3PkY9OxqmTl7CZYEo0YtCp0qkN5LVpuowqM-3pnAW3Gr7QgOEMU8VzGemABXOvU7BjtETsAPgLqNb389lXyTZWvYV-MFtvJ6yP5yT78QlJ2r_7GIPxQcbR7rCLOJHmKH465X_JtuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی
: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142253" target="_blank">📅 18:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142252">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اطلاعیه رادر کلودفلر:
ترافیک اینترنت بین الملل ایران از ۹۰ درصد به ۵۹ درصد رسیده ،وضعیت الان اینترنت ایران دقیقا مثل روزای قبل از قطعی ۸۸ روزه ی اینترنته و با اختلالات بسیار سنگین همراه شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142252" target="_blank">📅 18:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142251">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
طی اتفاقی عجیب شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142251" target="_blank">📅 17:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142250">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0T5lQWekK2BR9Ogb0VXRrqF-u5e3nt2Qt46Sm0qM2HBg707DkNXe4NPH0zEl1lTh2yLmhBeGxxh3e8uY_tlOnOng6S_9ds4QL-s6ZRDaJ9L6hEfZpIXVs5JVsmtX583aalIcqqyGkvKmlvgX6VH_O3kK_H7ULITI7Gmp68ZSvzuVdQ4vxFvY_yQW61gRLgtn5B8aAbZJKn6zIz0o9jEw_PwloZQp15TfpBxMakzBsIbYuNizezdneTvgUlejOV_OzSlb0krJ7wylBde7iyu15n0GYZOy1on5YJTFgA413LJYjIIMhZqsfGB50EYWw9gTUVHN2ehpBZ9aTUZiY531A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:به ترامپ مشکوک هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142250" target="_blank">📅 17:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142249">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مقامات پاکستانی: مذاکرات با هدف بازگشایی تنگه هرمز و پایان دادن به جنگ همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142249" target="_blank">📅 17:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142248">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME-ovMUrlvmfVSxZNrsL_1j5kyNcGaiebZShnyGVnAjM4_j7uhqViTQClFwowLDa_CpFkV7rl6xtEDEEpBGFFyA5yHZdjVcJX63njUifo1lmIcjFnjyIxAMTLKlnaKDgWBp08-ab5cExHiAdlmFKLyhCciHNxENKYTCHf1j9xDINQ7nGnF0aL6W-6j6J3NOCW3gbSCM8u7C-R8xR_KfjePaOyGy5fGblViJFiGYTDhxYt-EhfBTnQe5m6LYyUj4fZNhD6d7KRm5u568-sb7osnSF3-unFNGzqjFKZIeoPwiP9cJN1qM-_-ZxYdYk1syfJwr6-VY5cGLWv1ugcsx2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: قرار بود بعد رفتن آمریکا از افغانستان، نظام شاهنشاهی اونجا مجدد برگرده اما ما نزاشتیم و کمک کردیم طالبان قدرت بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142248" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142247">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=KgsTpyBtSnOgcxFThacvSYcic67ppwnYCACqH_1iP8I1YV8m84Q-ADmkei72BjlLOTiZFoPJ6X07iBnsxOKPDa8CGzDNnAeOyiWENLBxkPvXrL9U8fSK5GGLA_zlU6u0RL1vHlV4oCgfacJ_uZDPytKnE6jV_wgutzGg6u3w9lu08GgOi3HlANzPzxYkwbGAQu58ncUc6PtGh8WbwYtsGPrG_xuNAM4tTciATDxZGulbRC-AFAFvK1TNFnlNWeYjM54ZfG6FYpCwNODWeNGbUd0sy03Br7hURoEqllY6SXgB4brOdne57-KiFIzlMZzxYCWg9MrjCjNDJLFtfgddYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=KgsTpyBtSnOgcxFThacvSYcic67ppwnYCACqH_1iP8I1YV8m84Q-ADmkei72BjlLOTiZFoPJ6X07iBnsxOKPDa8CGzDNnAeOyiWENLBxkPvXrL9U8fSK5GGLA_zlU6u0RL1vHlV4oCgfacJ_uZDPytKnE6jV_wgutzGg6u3w9lu08GgOi3HlANzPzxYkwbGAQu58ncUc6PtGh8WbwYtsGPrG_xuNAM4tTciATDxZGulbRC-AFAFvK1TNFnlNWeYjM54ZfG6FYpCwNODWeNGbUd0sy03Br7hURoEqllY6SXgB4brOdne57-KiFIzlMZzxYCWg9MrjCjNDJLFtfgddYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خداداد عزیزی: دخترهامو زور نکردم روسری سرشون کنن. برام مهم نیست چی دربارم میگن، حکومتی بودم که بیکار نبودم
@AloSport</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142247" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142246">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrH6QXjN_NNm2w2aRq0EANfbt9YLmefeGRjQ11pih7iezNraRQYJ7if34PYMup_SvMoUb1U4Bm6KxEGILfPAGh1e_qJLcWorlhqqD0P3i-c2oQjzmK6lvKxXseQJQW7Vr7g5UxuKdg54aHjbyPNg8AtkrjdyC73ws6BHgF07g-8lXGtRNS-tnXP99Ho-zqBH9ZWfgeJiuTFzuFJ6V-9MszvrlMS15MGQfAm3z-Zpl8wjez2ElKmnXnlENA-MyKwjNKXiAnifnrgC_BpTxkYgRwRBaZ6E2DbjxIWlILCRWbSRA7I9CG16Z7kGX-Mwdn44tLVKlMHIquRETTF6F1p8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مصطفی ایزدی، جانشین فرمانده کل سپاه پاسداران:
🔴
دنیای غرب تشنه معارف انقلاب اسلامی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142246" target="_blank">📅 17:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142245">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHxMp_YqgwKhz3vna8cIRVt1g7_r7sn7G-x20WbTfxJFsow-1qNp3Byv1gdnkfY0UXd8gOZjssCe8Nd6wzFzNb8dUZ5zC-RvqbH12vkxbs_3uAe8ZXiKAJN16JgfYUHXX9mIxIlD8kcgmhRprRIGEAbANMDXpt-tMO6_fv8qW8dCx94noKR_C3sgDmWrbKLRWykQLEDMLB7RSz86Sbh1tSLA6gcjHLGm9EMVuIu-MnVBcP4sdo6LiWXjOVyEBT2KHcrhpD1TJmU8VhCrr5nBWI7BrF5hIkTvXA6mRgeRVhvJYmPp07C9iUBFC1-V7SaKkr3D_Q4ICu34olLaZQOnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
متاسفانه قطعی برق ۴ هزار ماهی آب‌بندان در بابل را تلف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142245" target="_blank">📅 17:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
حماس: از درخواست ترامپ برای توقف حملات به غزه استقبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142244" target="_blank">📅 16:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlg9MxzmrTUgypnbLtlqIzIO8M5ESIiEBqA-E7tmSC_ST8uzVreTWydwi-yepI63GmwED4GLalHkZhr-cG6xtJvVVYGhe4eISwELdu8xJnej_r60UI05zgirCmyuDNK4S6dOL71qfE77YTXJqDIBFbXR6o7Xl50l82e_pmVxCNMIzQA9zE53Rq7fEDFrd3G-HUqCZQpw6DBzCZGsD4lXxVsop0fWxbmboJ863H4brr7j6jo4zpJrwCNfJtVOi1KrVzp_qJP8iRrr46gbIxbeFKsLLnw6Be8gNL5jtNuwzXjNoixNA4U4vE02gVCqGJN4XB1elvQY4JnUJUPGUJKViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش سی‌ان‌ان،
ناوشکن نیروی دریایی ایالات متحده،
یو‌اس‌اس بنفولد،
ماه گذشته در جریان عملیات در
دریای چین جنوبی
دچار قطعی برق شدیدی شد و خدمه تقریباً ۳۰۰ نفره آن بدون سرویس بهداشتی، تهویه مطبوع، خدمات آشپزخانه یا سیستم‌های آب آشامیدنی در گرمای شدید رها شدند.
ناوشکن کلاس آرلی برک در ۲۴ ژوئیه پس از یک نقص مهندسی مرتبط با ژنراتور، برق خود را از دست داد و به مدت چهار روز قادر به مانور با نیروی خود نبود. یک کشتی جنگی دیگر قبل از اینکه یدک‌کش‌ها بنفولد را به خلیج سوبیک در فیلیپین منتقل کنند، غذای پخته شده ارائه داد، جایی که برق شش روز پس از نقص اولیه دوباره برقرار شد. هیچ آسیبی گزارش نشده است و نیروی دریایی در حال بررسی علت آن است. این حادثه دومین قطعی برق گزارش شده برای یک ناوشکن آمریکایی در هند و اقیانوسیه در سال جاری است و در حالی رخ می‌دهد که نیروی دریایی با افزایش فشار عملیاتی ناشی از جنگ ایران و سایر تعهدات جهانی مواجه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142243" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142242">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عارف: سهمیه اول بنزین کاهش نمی‌یابد، اما سهمیهٔ دوم به‌تدریج و در راستای آزادسازی قیمت‌ها کاهش می‌یابد.
🔴
خلاصه: نم نم جا میکنیم درد نگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142242" target="_blank">📅 16:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142241">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: ما یک کانال ارتباطی مخفی با سپاه پاسداران داریم
🔴
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142241" target="_blank">📅 16:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142240">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
گویا اینترنت بزودی بازهم گران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142240" target="_blank">📅 16:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142239">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مقام ایرانی به رویترز:
ایران سیاست خودشو از دفاعی به هجومی تغییر داده، واسه همین چند هفته به آمریکا ضرب‌الاجل میدیم که توافق نامه رو کامل اجرا کنه وگرنه بهش حمله میکنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/142239" target="_blank">📅 16:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142238">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نیروی دریایی ایالات متحده قراردادی ۲۲.۹ میلیارد دلاری برای تولید موشک‌های تاماهاک به RTX اعطا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142238" target="_blank">📅 16:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142237">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مدیرعامل آسیاتک: مردم بی‌رویه اینترنت مصرف می‌کنند چون قیمت هر گیگ اینترنت ناچیز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142237" target="_blank">📅 16:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142236">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6764e436a3.mp4?token=EHwK9VGTiR6_I4iofpqqVsZFd0nVkMxiCZ1KWeqQyRUpuznynQL10dmvNv7euld-IY1_1AEr7Qn0T2PavG3fDGPEHthVF_kSLx1qmM6cejjXI31xMxxng4Q2N_sXqG_P5mQwXM8ZVJlVlEVHSX4StyCXdfI6Wds2DJZBt8w55AVhN9XkO6CbPqLjYyE966MZCcaA5JYAfmEfNFAIm0cFJPCyySswJJxDLR9s6zvwkgRnbeZ9J-VCc5NU12vRmA5kNbLuCUbFwt4ahwUfgfXUyH2H_F3i452gx8b35LBWsR-dTOZBu27gzSmLBXqmdUkbyVn9l60SgE16hW_vUL1VCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6764e436a3.mp4?token=EHwK9VGTiR6_I4iofpqqVsZFd0nVkMxiCZ1KWeqQyRUpuznynQL10dmvNv7euld-IY1_1AEr7Qn0T2PavG3fDGPEHthVF_kSLx1qmM6cejjXI31xMxxng4Q2N_sXqG_P5mQwXM8ZVJlVlEVHSX4StyCXdfI6Wds2DJZBt8w55AVhN9XkO6CbPqLjYyE966MZCcaA5JYAfmEfNFAIm0cFJPCyySswJJxDLR9s6zvwkgRnbeZ9J-VCc5NU12vRmA5kNbLuCUbFwt4ahwUfgfXUyH2H_F3i452gx8b35LBWsR-dTOZBu27gzSmLBXqmdUkbyVn9l60SgE16hW_vUL1VCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با حرفاش موافقید؟
👍
👎
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142236" target="_blank">📅 15:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142235">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی آمریکا به اعمال فشارهای اقتصادی جدید بر حکومت ایران ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142235" target="_blank">📅 15:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142234">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: قیمت نفت بدون تغییر و در سطح ۸۸.۵۵ دلار در هر بشکه باقی ماند
🔴
قراردادهای آتی نفت برنت تا ساعت ۰۱:۲۸ به وقت گرینویچ بدون تغییر در سطح ۸۸.۵۵ دلار در هر بشکه باقی ماند، در حالی که قیمت نفت وست تگزاس اینترمدیت (WTI) در همان زمان با ۱۴ سنت کاهش به ۸۲.۲۶ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142234" target="_blank">📅 15:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142233">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فووری/خبر مهم درباره ابر تورم
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142233" target="_blank">📅 15:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142232">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
علی قلهکی: تغییرات مهمی در قوه قضاییه در راه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142232" target="_blank">📅 15:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142231">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: انتخابات میان دوره‌ای آمریکا کوچکترین اثری در مورد دیدگاه و نظر من در مورد ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142231" target="_blank">📅 15:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142230">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjZEnbPm7mxL_KHKc1xUpuxkgyQpFq5SPblkgjXToGnL_dOprtDLWQAj2qmmkueNnsjgbqrclAooP6qDCcbjgoj3ifAwg7g8QPgmiWPAqlQqqXU9MOO2wOBJjijw-WTi195e-4XyIIxvF6Q0IT_1ax4Sd_ERbmxdme-HywJg2QJIEyGlU_qi5vTO0mtlY8mTp8-vXu0sWDC9YaOw98f8dMqJ0yv1qKhL1iUlJ4lDJvPNsgxQSVaI1Xj0J7pkjGwAjnYZRojf8kYzaqjMGpBeICNfeSChkNWnZuZDw_al2DsCoMVXP--B5b9gubvu3yn-wH3cVWh-2OhVEq84U0VCMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از یک کشتی عربستانی که ساعاتی قبل، توسط حوثی های یمنی در تنگه باب‌المندب هدف قرار گرفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142230" target="_blank">📅 15:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کلش ریپورت: رهبران حماس در دیدار مستقیم با جرد کوشنر، فرستاده آمریکا در مصر، تعهد خود را برای خلع سلاح کامل و غیرنظامی‌سازی نوار غزه مجدداً تأیید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142229" target="_blank">📅 15:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f72ceb115.mp4?token=ufso8jh92W77f1ouv96_S2dt25sKy-1_qMf32ZYgFP0Jn_8EoyDVDno8CiwiEHoefxEyIrfEOrZt3nyhiSfsv_1IfMt1YWUveppXua-zmaJmwuy_z5dWsW0WK-bMDb24bwd00rvrxjKIIBsA_lkflRPBmecCev3h41GHO4KqmOw1WsrchpWidhds_Z2wZS64scYC8rrs7B4dIe7-XV4NTDB05FlMsFM2JGBUuUBKr4gNoim947iHmgYrvEjVjygGit9LUVHn8bmfYpvD4v_4zDYFSkUDAlEAerhVmPtxecgMDS6m-86gPZagdfn2hTe_ebkQSOPQxKcNoaHH4Mlz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f72ceb115.mp4?token=ufso8jh92W77f1ouv96_S2dt25sKy-1_qMf32ZYgFP0Jn_8EoyDVDno8CiwiEHoefxEyIrfEOrZt3nyhiSfsv_1IfMt1YWUveppXua-zmaJmwuy_z5dWsW0WK-bMDb24bwd00rvrxjKIIBsA_lkflRPBmecCev3h41GHO4KqmOw1WsrchpWidhds_Z2wZS64scYC8rrs7B4dIe7-XV4NTDB05FlMsFM2JGBUuUBKr4gNoim947iHmgYrvEjVjygGit9LUVHn8bmfYpvD4v_4zDYFSkUDAlEAerhVmPtxecgMDS6m-86gPZagdfn2hTe_ebkQSOPQxKcNoaHH4Mlz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، مناسب‌ترین کار این است که من از دخالت در انتخابات اسرائیل خودداری کنم، اما ممکن است از یکی از نامزدها حمایت کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142228" target="_blank">📅 14:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea77c36c6.mp4?token=QOVDUkr9wVUubsEwvJgKBR1EzjR6owDRUn8UbvjD1ONWOYgwG9rD8GwMJ9JxhZWt7LKZ7ZryrBvrSNEEUjfBjiPiRliUSRLCbOM3mqG0BTLdrSC4UvS2rXsIdRkPBS3Wo58ajhGB3Fwe2_5Zz8-cPNjWDl9h4eE23FFAWWYzYrF-McBuDmtmfylg0VED9FGqG38AG7xWPMljiwABX2-rv-gny90SjMWTPD5RJaXZo_54Q4edPdMkGA_UbFAG02AhZ9bdtxLrpU0kFnT-uIzr-l8UkPHuItMU9NkXnMsvgrnQ_NuMbCY--LZKowoa3X-xjJqcMFPFcikXMWE-HDcv3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea77c36c6.mp4?token=QOVDUkr9wVUubsEwvJgKBR1EzjR6owDRUn8UbvjD1ONWOYgwG9rD8GwMJ9JxhZWt7LKZ7ZryrBvrSNEEUjfBjiPiRliUSRLCbOM3mqG0BTLdrSC4UvS2rXsIdRkPBS3Wo58ajhGB3Fwe2_5Zz8-cPNjWDl9h4eE23FFAWWYzYrF-McBuDmtmfylg0VED9FGqG38AG7xWPMljiwABX2-rv-gny90SjMWTPD5RJaXZo_54Q4edPdMkGA_UbFAG02AhZ9bdtxLrpU0kFnT-uIzr-l8UkPHuItMU9NkXnMsvgrnQ_NuMbCY--LZKowoa3X-xjJqcMFPFcikXMWE-HDcv3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حماس: ما یک کانال ارتباطی متفاوت با حماس داریم و در نهایت آن‌ها سلاح‌های خود را زمین می‌گذارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142227" target="_blank">📅 14:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142226">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ : اسرائیلی‌ها نباید در غزه حمله کنند، زیرا حماس موافقت کرده است که سلاح‌های خود را زمین بگذارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142226" target="_blank">📅 14:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142225">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9189453b.mp4?token=gRWY6Z_K1ddPuR6GcxcOsbeinuWmoaWkOAzmujK1IRtlxVsooGky4kIgAQDSMHwrrhFM3JAWitHF8hwjdpjz_1SMnEJflyC7z5MpctvbjO4r35ZoBLrdHlDECnHmg30r665U4ZjdNMGxYrZva9rkYRssMJ0gYyt2r0-eY7XltVDGII8DrYiJ-wI1tBeLY7EBb6N69Q1HBcfBIvxePZU-46dTzO5ByMY-sRPpXd5vMjfBhTX8miPKQ9gYAitc4P9KdwkGbrrvCHYqrFBpWwCGw1SwBvta9tuWmI668K4V2l5Gc4JDDBr6Ouxq4x7F99QhWdtQ-aqcuqX2kZcURllJsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9189453b.mp4?token=gRWY6Z_K1ddPuR6GcxcOsbeinuWmoaWkOAzmujK1IRtlxVsooGky4kIgAQDSMHwrrhFM3JAWitHF8hwjdpjz_1SMnEJflyC7z5MpctvbjO4r35ZoBLrdHlDECnHmg30r665U4ZjdNMGxYrZva9rkYRssMJ0gYyt2r0-eY7XltVDGII8DrYiJ-wI1tBeLY7EBb6N69Q1HBcfBIvxePZU-46dTzO5ByMY-sRPpXd5vMjfBhTX8miPKQ9gYAitc4P9KdwkGbrrvCHYqrFBpWwCGw1SwBvta9tuWmI668K4V2l5Gc4JDDBr6Ouxq4x7F99QhWdtQ-aqcuqX2kZcURllJsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما یک کانال ارتباطی مخفی با سپاه پاسداران داریم
🔴
ما مستقیماً با مقامات سپاه پاسداران در ایران در ارتباط هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142225" target="_blank">📅 14:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142224">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: ایران باید پرچم سفید تسلیم را بالا ببرد
🔴
آنها در بازی پوکر خوب هستند، اما در حال نابودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142224" target="_blank">📅 14:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142223">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95373bc7de.mp4?token=MKZ1NF4prJhJESCfVzgY8mEEcVq4LFJImLqZ1vFNoPpJW86z31F8pVxcywD8EyfMVD6vlQCCxvnct4hLC9b3gAC-k5JqULOxpOvNOLo3cq1_YBjCqYL8Hok09rdo_XxYzpwB5v3_NEBPsCgoO0ZTT0qrEuUcX99fgvZdbTf8eX-bZ8gKHGEF882kmmPHUpwKYcDNy3HVBUb-ed66dSen3MbYEaBt_bikvsT0hBGgjZ8XOc7j7N9zj94CbkpcOWh_WIoFd8B-mhqVzCvb_p3R4erkqcS5dBqn-LTX_L8xRgJ8av_hwwF5KaSbHbfE-w51ZBPrNzMd5Gh6r28U2pEh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95373bc7de.mp4?token=MKZ1NF4prJhJESCfVzgY8mEEcVq4LFJImLqZ1vFNoPpJW86z31F8pVxcywD8EyfMVD6vlQCCxvnct4hLC9b3gAC-k5JqULOxpOvNOLo3cq1_YBjCqYL8Hok09rdo_XxYzpwB5v3_NEBPsCgoO0ZTT0qrEuUcX99fgvZdbTf8eX-bZ8gKHGEF882kmmPHUpwKYcDNy3HVBUb-ed66dSen3MbYEaBt_bikvsT0hBGgjZ8XOc7j7N9zj94CbkpcOWh_WIoFd8B-mhqVzCvb_p3R4erkqcS5dBqn-LTX_L8xRgJ8av_hwwF5KaSbHbfE-w51ZBPrNzMd5Gh6r28U2pEh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنچه تاکنون از آن (مهمات) استفاده کرده‌ایم، در مقایسه با کل ظرفیت، بسیار ناچیز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142223" target="_blank">📅 14:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142222">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر عمان سر راه ما قرار بگیرد، آن‌ها را حسابی بمباران خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142222" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142221">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الحدث» به نقل از منابع آگاه: گزارش‌هایی درباره موافقت با تمدید مهلت ۶۰ روزه آتش‌بس میان ایران و آمریکا وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142221" target="_blank">📅 14:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142220">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abT_h91lcY9v7c4gzY48Lxyn8ORn9iNkLT1Yi_thkcWjPPNr693LO6MoQX87uhk0bRnFQ4nRRWlshdW1NcBGIiM0MiKp44g2m0Pw1ubF6qzhhT8ThdAAH8OUW4owXaqpQv3tUBym1IkgXIcsS7UFAbvON9P06_LiKALhB929EmOBm6L_8w7JmreP39nE9c6cGo3PdZexNzbtWWe6q5upCI6SJ0wg9v5mubrHXaUW9xNK7lwN2trY8qZjzRID_AhU4M0_s-VFoyxa92GAtOTzuWrnaOAZXct2FSJtydMZD6k-7jSr68j4dn2ljsR4WZygTYZ8iET1fUe9twaYs_32lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرکل انجمن کشتیرانی و خدمات وابسته به ایران: منشا آلودگی نفتی سواحل جزیره قشم برای ما مشخص نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142220" target="_blank">📅 14:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142219">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پلیس راهور فراجا: حتی یک خودروی تولید داخل در مرکز آزمون تصادف تست نشده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142219" target="_blank">📅 14:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142218">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a5896144.mp4?token=IuVKOAmyKzLbSUBDvlH1iTUfHXBDPz-2glF1f1WjAI0JSzjWzbzOjEmIxCSdaQ-Dxv3TJBu3JUKISGd4KwKdeEUbW4bZlv_e9625ccIOhpFFo53HEkP737K_gSRlyuk9JGUQTsAjF5dB2hlbFiJsGNTP22i-o8ulEj9PsaiDg68xBxeFdKsq5N2vM2ibWR4pkE0BrWhcFbfExutBL996FaRYm1G_JBo8XZKn3hz9AVEMQCrwhjiWyjOKDKYWuM3SYF-Xz4JOL5zX6cjhAig6Gj2oDKCVq4Kj9vVV4lZ2euqYsd8V2-poYPmw0zxvHYjGZJJh8IP-UWQcRYNYTkVN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a5896144.mp4?token=IuVKOAmyKzLbSUBDvlH1iTUfHXBDPz-2glF1f1WjAI0JSzjWzbzOjEmIxCSdaQ-Dxv3TJBu3JUKISGd4KwKdeEUbW4bZlv_e9625ccIOhpFFo53HEkP737K_gSRlyuk9JGUQTsAjF5dB2hlbFiJsGNTP22i-o8ulEj9PsaiDg68xBxeFdKsq5N2vM2ibWR4pkE0BrWhcFbfExutBL996FaRYm1G_JBo8XZKn3hz9AVEMQCrwhjiWyjOKDKYWuM3SYF-Xz4JOL5zX6cjhAig6Gj2oDKCVq4Kj9vVV4lZ2euqYsd8V2-poYPmw0zxvHYjGZJJh8IP-UWQcRYNYTkVN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله هوایی اسرائیل به شهر المنصوری، در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142218" target="_blank">📅 14:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142217">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/ العربیه: گزارش‌ها حاکی از آن است که با تمدید دوره ۶۰ روزه بین ایران و آمریکا موافقت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142217" target="_blank">📅 14:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142216">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cb7364d7.mp4?token=WyeBy5XyPtNi3lTB6w3PHZHUsnHzoe74d_O7jR3rPzsPtu1avwhFng6qW8okKnFOgClN6M7YgTXn8eh_kg1spib0Mezt-htxnJIV-Czj8QsAekx4cyubjblsNUQYzLRnFzoUg0ewHGAwKQC11x38PNdabbOqQINgnD5mDvBzPmMhKYgSb1wG1K4tFRcQx7DN9yoiJuOGETtNRMUe1_P9aNJmP8XUWb5AOr-ScprjoHrXZXduDx6u8WdiR3cDLpHvKYDjdWY1d0XNM9eN7ViB0KZyWcv7-UMRcuuT95WSVabhEumVsimOHuGrSAF_emUjgxOcEQ9B9PTUs2ivvgJj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cb7364d7.mp4?token=WyeBy5XyPtNi3lTB6w3PHZHUsnHzoe74d_O7jR3rPzsPtu1avwhFng6qW8okKnFOgClN6M7YgTXn8eh_kg1spib0Mezt-htxnJIV-Czj8QsAekx4cyubjblsNUQYzLRnFzoUg0ewHGAwKQC11x38PNdabbOqQINgnD5mDvBzPmMhKYgSb1wG1K4tFRcQx7DN9yoiJuOGETtNRMUe1_P9aNJmP8XUWb5AOr-ScprjoHrXZXduDx6u8WdiR3cDLpHvKYDjdWY1d0XNM9eN7ViB0KZyWcv7-UMRcuuT95WSVabhEumVsimOHuGrSAF_emUjgxOcEQ9B9PTUs2ivvgJj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی اتوبان بابایی تهران، یه پسر جوون داشت با پشت پژو پارس سرعت میرفت، که این شکلی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142216" target="_blank">📅 14:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142215">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSL7m6J4OYmenOw135ju0xO2YRzbAeHfl0Al37LAafSQCF-4VY0tR6BgStklciSN6iCILXXqPOTXf0_9BURHAe0L1W8KXvFMHcK9eZXYFnFnqB16nXGYeOyyZHZPwmRL03jTRGIb2oMaK6YbL_euLs3L_qXFwHUFgSKuhV4WFW7pxFm2AsRw7VL_bjbptU1lNCJxG9x3Ylxogn92uA-hOVmEkdXhG_E2VdGfEJJ-2qMp2idFthX-Ty9kR3BTZikKVZuWiPMXnORVX8ZRHRBSIowHdL4Z41S-2yh0IR6fFUF82DssIfVd-dbJ5chwBq8QySAaxytSRSZ-5fLvGPRL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اکنون: هدف اول این هست و خواهد بود که ایران به هیچ راه و شکل و فرمی به سلاح هسته‌ای نداشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142215" target="_blank">📅 13:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142211">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIiyhvLpMErpSco13ZSiOw4e73RWz2LtB25qs-vBqH8iGrgtuTG9q0eICM7huvkoSxSfUuVCk0cUeBRLStXj_5_X5S8_WI6G4bHN08W-A5g_BsLrXCuBnh9YDzQdjmteLRfZdd5-toYMPc7QVTdQxEfCJ7GP_OGEfUVoX7tknAR8LU0niEb2MYIRuMpGQuVid0m60ycGGgZO_2q5r-nhywn-zXhr1NHI2mU8CPY6FYJmQ3yHtfzNc5z1VhQj4C3ze2EXx8rQ5ZtsyYRBPMrkYECidKs__M2X11ubd8x4vzI61iBF-Eas4qLvqj6RIMdI3z2XPsMqeL_ZQYF8ltn_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmpiqvSZnj1BV3OVXCi1RdNe6E82aj4BzhTJ9Xrgpk9bG-4qGhOla-FngINookNwDMrkp-4HpKCG8Ymo3RC5CxXoTQo9u5uBFDIUkvGpHpycQ4xtZtW13NNg63yoIP0SfAsEqqAysXpYM9EIoMQzeuW1haSuHG8fxeTqT3SaSDDD69LJa1oD2v88VDzW-dhQFPInKkfmenP6XFHasjTBwqmqg53z3uUZvN8ZXe7VnBoPGSQW0B4BVM5pyBrybawSk43ZgbJIITThTZ6iGW-_MDmo49H1ayRHALdciSTioyK8BvTmeGgF6q9HzvsvifuIBI8vLXZsJ_F0j-JGM3hLMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f157f1c6c4.mp4?token=SDZQJWDt3pukY6mWy7Z1x6ekTXwGeAvm1mKTtXoDSNhyBVPALPGTFIx7j8vHlYeLl9qotspsSWRgiugNNJRLJXJHkG8SzWSWTpOdxw_TJ6vCBqnTa_E9jMJP-FUzhLVCMRA7x0L00BuwPki69Tm8VCKZdalzkgt71I7FhysFMJO4bVAIv-tevWnP3IXC5lwfHN-VJnDMBCskDcYakvartWCqWZGhVCwClCKJSJUXdNE5SMpdgHtrMCfgZ7Dj6LpONeG-0Zj6s9BPgYZPmKC0fBXJVsh9SkiNVE5HE2HRsw2JqBxUDyUdq85ZZ4wECLx2Z8iHLNBRf98nUq12FlFgjU4cqeJYOXxxn24qO6hAKDc0d0O6tGU3-PBG1aFqEM5uVeuT4cpS5MSD3gBYbXuR_V0mRo8GFUwSABZ_4xr9zi5ucNbFcZp20mKZgVXe5oweBoL1Lp8QQluie3yu1d9w_nI6db5lWr4jvZ5nS1tXAatHGttE5Q4cfDnZroBSxlCaFi59HSGspa1aiW1kyZ8mgGy1WNfG7bEgdUJdevhuMZyj530RIel8CnbysDlAAAQ1m5F9szv3Hcsy0hLuoopQjWuxGdJtM9TGIQAOeEGi8wsUghRZcngAd9dEVy01h8BD4CdmlMGje6vlMxr9Cq5b-sBKIPzoWZTctD4Mtxfhrds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f157f1c6c4.mp4?token=SDZQJWDt3pukY6mWy7Z1x6ekTXwGeAvm1mKTtXoDSNhyBVPALPGTFIx7j8vHlYeLl9qotspsSWRgiugNNJRLJXJHkG8SzWSWTpOdxw_TJ6vCBqnTa_E9jMJP-FUzhLVCMRA7x0L00BuwPki69Tm8VCKZdalzkgt71I7FhysFMJO4bVAIv-tevWnP3IXC5lwfHN-VJnDMBCskDcYakvartWCqWZGhVCwClCKJSJUXdNE5SMpdgHtrMCfgZ7Dj6LpONeG-0Zj6s9BPgYZPmKC0fBXJVsh9SkiNVE5HE2HRsw2JqBxUDyUdq85ZZ4wECLx2Z8iHLNBRf98nUq12FlFgjU4cqeJYOXxxn24qO6hAKDc0d0O6tGU3-PBG1aFqEM5uVeuT4cpS5MSD3gBYbXuR_V0mRo8GFUwSABZ_4xr9zi5ucNbFcZp20mKZgVXe5oweBoL1Lp8QQluie3yu1d9w_nI6db5lWr4jvZ5nS1tXAatHGttE5Q4cfDnZroBSxlCaFi59HSGspa1aiW1kyZ8mgGy1WNfG7bEgdUJdevhuMZyj530RIel8CnbysDlAAAQ1m5F9szv3Hcsy0hLuoopQjWuxGdJtM9TGIQAOeEGi8wsUghRZcngAd9dEVy01h8BD4CdmlMGje6vlMxr9Cq5b-sBKIPzoWZTctD4Mtxfhrds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمعه خان فاتح، فرمانده شورشیان طالبان و نیروهایش پس از رسیدن نیروهای کمکی به منطقه بندخسان، تسلیم نیروهای ارتش افغانستان به رهبری طالبان شدند.
🔴
پس از تسلیم شدن، فاتح با یک هلیکوپتر دولتی در مسیر کابل اسکورت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142211" target="_blank">📅 13:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142210">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سپاه اصفهان:احتمال شنیدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142210" target="_blank">📅 13:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142209">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
بی‌بی‌سی: یک کشتی کانتینربر چینی با اجتناب از کشتیرانی در آب‌های خاورمیانه، از مسیری تازه به مقصد اروپا در حرکت است
🔴
کشتی مذکور از مسیر قطب شمال عبور به اروپا می‌رسد و بدین ترتیب خاورمیانه را دور می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142209" target="_blank">📅 13:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142208">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت خارجه : مذاکرات با عمان همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142208" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142207">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رسانه‌های یمنی همسو با عربستان سعودی:حوثی‌ها یک کشتی را در تنگه باب‌المندب هدف قرار دادند و مالک آن فردی به نام "امیر خان" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142207" target="_blank">📅 13:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142206">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر جهادکشاورزی: ۸.۲ میلیون تن گندم از کشاورزان خریداری شده و امسال وضعیت تولید خوب است
🔴
همچنین از مجموع ۴۰۰ همت طلب گندمکاران، ۲۱۸.۵ همت پرداخت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/142206" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142205">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNRmsHa_HRMExSpQdIDgVyOsnaFh9GUQl3wn8OMdaXbLswtgbqAKVy_3wAQGe7JJijZWlF36Bi-a735Aj0ltsvs32zJbw41Q2BbtsvTVPQtoP2XXkB8NfKtOzAAW1q9HavWO6MBvdiBL0oDiEMORlzKtQB27KFu6tgpM14ZFUcdxYDgDX75pYsrPZH_Trx7fVKDK3E9lXu91peyI2_xp-TKHDPaD0x_n_53l7m4L7KgKRD3HL1cHh_hzV9LVKJxu6T-f809gpmE7O1VzEF4o62393_DvOfwZOON5jvxbW9fNZw4TaPyX0kAnDNI-SzDnUwi5qWd_QyKrFnqsSCZifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار حوادث : ملیکا همت زاده دختر ۱۳ ساله اهل روستای دسک تو سیستان و بلوچستان عقرب نیشش میزنه بعد میبرنش بیمارستان تو بیمارستان ۷ ساعت منتظر پادزهر میمونن اما به دلیل نبود امکانات تشنج میکنه و جونشو از دست میده...
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142205" target="_blank">📅 12:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142204">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
باشگاه استقلال اعلام کرد که استان بصره عراق را برای میزبانی مسابقات لیگ قهرمانان آسیا انتخاب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142204" target="_blank">📅 12:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142203">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f102f9aa.mp4?token=DVCa2yalEr-6JG8EJViUsazgadk3bVDh09bIq8p1fAuvjV7CWjENUb34oXSszTHZDeZTBdvhamDh5QVexsR68BPEsTOGkg4ujXuuopJ0S5Nqs3Av5TMfYWOSpATQhHEsgD5H-P1zDjydXZHy0udJXyJ5q26PgR_iCq6Ldazu3SlciDuS08bRfz3lOMma_rIJeUH2o_KHYVA7aPcKFZY0DYpOxA63LgNGrSj80y2DZlrhFcbZvCyMAQoMBdoP6f_zDqBwDFc4s19TmToFrSzDetI-ofqgrRKc-EiKDvoxEZAKoz8QXOCh5jLHoZ8YQR2U65nGzqAljD-Q2MtMB7zJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f102f9aa.mp4?token=DVCa2yalEr-6JG8EJViUsazgadk3bVDh09bIq8p1fAuvjV7CWjENUb34oXSszTHZDeZTBdvhamDh5QVexsR68BPEsTOGkg4ujXuuopJ0S5Nqs3Av5TMfYWOSpATQhHEsgD5H-P1zDjydXZHy0udJXyJ5q26PgR_iCq6Ldazu3SlciDuS08bRfz3lOMma_rIJeUH2o_KHYVA7aPcKFZY0DYpOxA63LgNGrSj80y2DZlrhFcbZvCyMAQoMBdoP6f_zDqBwDFc4s19TmToFrSzDetI-ofqgrRKc-EiKDvoxEZAKoz8QXOCh5jLHoZ8YQR2U65nGzqAljD-Q2MtMB7zJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خودروهای نظامی اسرائیلی در حال پیشروی به شهر بنی حیان در جنوب لبنان مشاهده شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142203" target="_blank">📅 12:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142202">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت خارجه : تلاش‌های میانجی‌گران پاکستان و قطر، برای کاهش تنش ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142202" target="_blank">📅 12:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142201">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در مورد سخنان جی‌دی ونس که گفته اولویت اول آمریکا اکنون کاهش قیمت سوخت است و برنامه هسته‌ای ایران در جایگاه دوم قرار می‌گیرد گفت: این نشانه تداوم سردرگمی و اثبات این واقعیت است که از ابتدا این جنگ تحمیلی هیچ مبنا و دلیلی نداشت جز ارضای مطامع یک رژیم اشغالگر در منطقه ما.
🔴
از ابتدا، دلیل آغاز این جنگ تحمیلی را مقابله با خطر قریب‌الوقوع ایران اعلام کردند؛ خطری که بلافاصله از طرف پنتاگون رد شد و اعلام کردند که چنین چیزی اساساً وجود ندارد. در مقطعی اشاره کردند به خطر بمب هسته‌ای ایران؛ بمبی که ۳۰ سال است در مورد آن صحبت می‌کنند؛ یک دروغ بزرگ.
🔴
خود را در یک باتلاقی گیر انداختند و الان برای توجیه شکست‌ها مجبور می‌شوند که هر بار اهدافشان را تغییر بدهند یا اهداف جدیدی را تعریف کنند.
🔴
الان دغدغه‌ آنها بازگشایی تنگه‌ای است که اساساً قبل از ۹ اسفند باز بود و تجاوز نظامی آنها باعث شد که منطقه ما گرفتار این ناامنی بشود و جهان از تبعات این وضعیت آسیب ببیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142201" target="_blank">📅 12:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142199">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niJYc3iPJSNF-alcwcwmFhOWJLNSQAJWSf9UXCQfWK_oiDTDo01Cuw3oyUnUJqllG6viFqwRaK3FfMquWnOGHxYtkBbc1ZJfPTo1gOvVFMb1ZaS0Qgsv_x_EakMk4j_j4gBDkG7EWq7lCyr7qObLfzyucPSRnPBMqvwIo75khWyABnqsbudKbm1wq6vQqRYuQx81LMmb95vi9xCg4s8VZ3dwzT1OD9EG98QC1ztG57WGcXnXi-HLHChpULZPptYzw7lkt_10kyKTDP3tldx600a7bm2MmONp_k0foHkTPy0L2Wp1Es6X9cDJaTtU3JSkqCYKmo0zqJ0DQIhmmNjh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb9BPSggW_u1aqhtLeV2uwPi4Eo71ALdOPNPb_fMk6Tm2vU_eJQjf5-CG5dTsbsROccO-q0VEHJHm_3SyJ4wx8WUUnZYzDWpMTkFX1E-NIE6PGK5rrAJ43Hx_TCBS13NRMNYPKa4aIkf4fXvD9Vh3JsJwd3h9Shl2XmisKdNDdybFbZhDHM3ahD6zXt-X0RmPmC_-eTyuUhlrqK6934lWqUTetJaiUOSMBj7GpeOxgUmRo8BVcoRwe92vnIPB6H50n40GUjHIM_9R-hS_XKqo4eFWKbS-NnEtpxueyIqLmNjfk33kBE-yW520TYkpzFg3_rElta7OvPydJSC0s26Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
"قلعه" دکتر مصطفی حمزه  نیروی حزب‌الله در روستای رمان، واقع در تپه‌ای روبروی رشته‌کوه علی‌الطاهر - قبل و بعد از حمله اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142199" target="_blank">📅 12:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
5 موشک بالستیک به سمت کشتی‌هایی که در تنگه باب‌المندب شلیک شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142198" target="_blank">📅 12:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewgmp2-F6XzP13s1VYKnutts_5vR0tKXe_o4Jqyqx-ookA43c4IwEogUgzBhVw7ZIRmqDs2OKdCuk5Vi6Kq0gZ3yOMK4SxbOtMCNi5MenwTs6XYczp4zwf7cZ3ojhcC3Ope6XEJmXNrhQfCAI8EB90thxYOGOz7FVh9UbBOGX5nksgBOGenI-2maXhdtb5Tzux4wa4FN3E5fBS4HlDLHM0hftXaPyw_tXiaCXIeqUb5v9TDyQRmKc9NLgi3k6V3z2MOrkUuM4Zo0-lvS_M4agr05hDCPxql4LnPj68yOjYsIQV4L2yTALbhgD-D25Mg9FIvwjBCpuP0AuXFkgP_vWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وقوع چندین انفجار شدید در نزدیکی دفتر مسرور بارزانی در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142197" target="_blank">📅 12:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
چمران: انبار نفت شهران نباید در این محل باشد و پیگیری‌ها برای انتقال آن به خارج از شهر ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142196" target="_blank">📅 12:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درباره ادعای یک رسانه آمریکایی مبنی بر ارتباط غیررسمی واشنگتن با سپاه پاسداران از طریق اقلیم کردستان عراق جهت اطمینان از حمایت نیروهای مسلح از روند مذاکرات، و صحت‌وسقم خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل:
🔴
خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.
🔴
خبری که اشاره شد از شگردهای رسانه‌ای و عملیات روانی برای ایجاد اختلاف میان ارکان تصمیم‌گیری در جمهوری اسلامی ایران است و تردید نکنید که چنین رفتارهایی از روی استیصال انجام می‌شود.
🔴
انسجام و همدلی میان بخش‌های ذی‌صلاح در جمهوری اسلامی ایران در ارتباط با موضوع صلح و جنگ بی‌سابقه است.
🔴
هیئت مذاکره‌کننده الحمدالله مورد اعتماد کامل همه ارکان نظام، از جمله بخش‌های دفاعی کشور قرار دارد و از این بابت خدا را شاکریم.
🔴
قطعاً هر تصمیمی که اتخاذ شود، از جمله در رابطه با مذاکره و گفتگو، حتماً با لحاظ دیدگاه‌ها و ملاحظات تمامی بخش‌های نظام صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142195" target="_blank">📅 12:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / وقوع چندین انفجار شدید در نزدیکی دفتر مسرور بارزانی در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142194" target="_blank">📅 11:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffbdcb628a.mp4?token=VZdVKF1DRjNh8GG6OQQ4BGPO3U1vuKz0RE0qB3iEoBYf5vlpRy9IS-ESPTHssyFn10ygyt1mxmIn5tVXTipatWzuXYLSYRWpP66udgZFu2Hod4kmN_FwdEzUsh-8U_M_DG-8gBOvoISVlFVTIofLRZjg_qbJ1fX0-w3-hYcSIAq_G5Fj5LEYBdixMgFfQRxIz3yrQG5NxcF9RurME4Q4YyAqXAFwJivFL70yVeVHG1LuFsnCOBVYEPqHpVlGovr8KQ930r59AJh362Bb-naAK06VnyQizShMo2qygInABXETDKmUlvK6QDlG2VRqO3ShH9gx8CK149gRX2Wn6kbwQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffbdcb628a.mp4?token=VZdVKF1DRjNh8GG6OQQ4BGPO3U1vuKz0RE0qB3iEoBYf5vlpRy9IS-ESPTHssyFn10ygyt1mxmIn5tVXTipatWzuXYLSYRWpP66udgZFu2Hod4kmN_FwdEzUsh-8U_M_DG-8gBOvoISVlFVTIofLRZjg_qbJ1fX0-w3-hYcSIAq_G5Fj5LEYBdixMgFfQRxIz3yrQG5NxcF9RurME4Q4YyAqXAFwJivFL70yVeVHG1LuFsnCOBVYEPqHpVlGovr8KQ930r59AJh362Bb-naAK06VnyQizShMo2qygInABXETDKmUlvK6QDlG2VRqO3ShH9gx8CK149gRX2Wn6kbwQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: هیات مذاکره‌کننده مورد اعتماد کامل همه ارکان نظام از جمله بخش‌های دفاعی کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/142193" target="_blank">📅 11:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بقایی: میانجی‌گری اروپا میان ایران و آمریکا صحت ندارد/ مسئله آمریکا بحث میانجی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142192" target="_blank">📅 11:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ad40293d.mp4?token=J0ETBftxjhSIgKWmUAykxMADdnUkh3kNWeq0MErUH9cAlo9IClYCPz5aZhORZ1AC_BRFD1d9Gk55mAWJ28Vlmp6h1Nh3ye58s1W3kZmRfg13y6Xs9YwgqTUx87cPijskIhXRbFbaI9qIs_1S15J4QRpH4k4ISejW9RbKBF2HIlOsARbDK0GDNLkEziyQ2BAT3KrZOdktEdKAKEpJgI3YIWh_zn2DYtqHYK1y0IfBIKp7qKpB3vpx7Z8C6PMYDRKXolmDtOyTF_oZ4E8zdPYbgL27epLadZPLgb-MCKF60wlURSr9fl1hshWoGTKnzdPH41N_rsMKkkxHaclrU_SzaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ad40293d.mp4?token=J0ETBftxjhSIgKWmUAykxMADdnUkh3kNWeq0MErUH9cAlo9IClYCPz5aZhORZ1AC_BRFD1d9Gk55mAWJ28Vlmp6h1Nh3ye58s1W3kZmRfg13y6Xs9YwgqTUx87cPijskIhXRbFbaI9qIs_1S15J4QRpH4k4ISejW9RbKBF2HIlOsARbDK0GDNLkEziyQ2BAT3KrZOdktEdKAKEpJgI3YIWh_zn2DYtqHYK1y0IfBIKp7qKpB3vpx7Z8C6PMYDRKXolmDtOyTF_oZ4E8zdPYbgL27epLadZPLgb-MCKF60wlURSr9fl1hshWoGTKnzdPH41N_rsMKkkxHaclrU_SzaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: تحریم‌های آمریکا هیچ تاثیری بر موضع ایران نخواهد داشت جز انباشت کینه و دشمنی بین دو طرف
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142191" target="_blank">📅 11:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر کشاورزی: قیمت اغلب کالاهای اساسی و مواد غذایی نسبت به هفتهٔ گذشته و نسبت به ماه گذشته رو به پایین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142190" target="_blank">📅 11:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=vZbunRb4kThuaARHWGZ6jvvgWI5Fjb-_K6xL-h8RZST7zS34m6tRHIXeTRc64-a5rUkJWMa4WgXPFNWAlDUerntKHcgNflrI1vxXDuskGw1mJEyII93YZgc6p1m0fAY0get2DaeC5UnLhm_iapoCsutkSbWODTBJCEm1B5_h58pQO6olpbchK0F7Pnu1jVHgeCEjVT5vAypD1J5Fr2oofb3Wje6qfYRMpWTXaHWbeU9hB0y1WoPeon2WLpOo_UGu8faIv8gU2iN_V0JctwZKnCHOWrXiLd2wyYqsD8rAqe5LmpPIHK8emvrfSZv6zq5_3aYcEEZlmlBMmpveQK_HfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=vZbunRb4kThuaARHWGZ6jvvgWI5Fjb-_K6xL-h8RZST7zS34m6tRHIXeTRc64-a5rUkJWMa4WgXPFNWAlDUerntKHcgNflrI1vxXDuskGw1mJEyII93YZgc6p1m0fAY0get2DaeC5UnLhm_iapoCsutkSbWODTBJCEm1B5_h58pQO6olpbchK0F7Pnu1jVHgeCEjVT5vAypD1J5Fr2oofb3Wje6qfYRMpWTXaHWbeU9hB0y1WoPeon2WLpOo_UGu8faIv8gU2iN_V0JctwZKnCHOWrXiLd2wyYqsD8rAqe5LmpPIHK8emvrfSZv6zq5_3aYcEEZlmlBMmpveQK_HfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تا زمانی که وضعیت خلبان‌های ما در قطر مشخص نشود، ما آن‌ها را اسیر می‌دانیم
🔴
ما از ۱۱ اسفند پیگیر سرنوشت این خلبان‌های شجاع هستیم و از ۲۵ اسفند با صلیب‌سرخ هم مکاتبه کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142189" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه : تفاهم‌نامه‌ای که با طرف آمریکایی امضا کردیم، هیچ مهلت ۶۰ روزه‌ای را تعیین نکرده است.  آمریکا چند هفته پس از امضای تفاهم‌نامه، مفاد آن را نقض کرد.
🔴
گفتگوها با عمان به دلیل پیچیدگی موضوع، دخالت بازیگران متعدد و کشورهایی که به دنبال تضعیف این روند هستند، مدت زیادی است که به تعویق افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142188" target="_blank">📅 11:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: نامه ای با منشاء وزارت امور خارجه خطاب به مجلس برای مسکوت گذاشتن طرح اعمال مدیریت ایران بر تنگه هرمز وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142187" target="_blank">📅 11:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
👈
وال استریت ژورنال به نقل از مقامات ارشد ایرانی و عرب:
ایران در حال آماده کردن نیرو های نیابتی خود در سراسر منطقه برای گسترش قریب‌الوقوع جنگ می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142186" target="_blank">📅 11:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7902ce9fb9.mp4?token=WzQb1M2ThiBgFfqTl9Eyfo71fSUHKeLUR_qZQvL1NujVyn7_ceznsDTYc-iD0Vi7FPxO0qG9qSpvKEwR_9k4QKzUOd1G06Ukblt0yNcb2zL7jOWCJUvnuTpW_pvo8LlG_R1AgFS6v-Tswzppj13e5FyPl3VobjhtWb84GC87ZsVydH3salrKQkyab4mrzQitC0i8raUH9bSWsiGeqvW6GYTK0Cmn6RfAS-giSayijI62yRS2T-UDMBLejN4JlyRwEHM2COrCmvZ9BBQpYguBoB0S4hgW_cUQQnzuShXrLejOu78JDDG54N-mIyiWwmOH6i0vFypDZq9IhVTKEtKWKLeFVeavgAHNq1xQGBESwf9PXpCdNJ2A3Ho_o80uUcS49QP3UtX8jkWaL9jW5ERJPnBdZarQRDTYlx4qLBvNchWhBDmMIQaCe3l4zv1ytfH5uFCdWezFGTe4ZaXjW_mGeFM77RSuIvQGJGT6r0BmRSNEdJOCrFT1q_dgPCtpBPElqq6T1ieOgTLYo148WH3PiQfDrlw_ueDYPcbX5HJwcqThg4oEnLsLyYoeuYQVyqXDbvhAAiRpIhXYIsdvPJyLZzGFkooSV6DnMBtL0X5C4kKTCGdOKf5-UDvFG6XQJH8oIsDLiOw26RyO2ZNZ2SfJTqiEmpLaQV2UycfUy4mLrzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7902ce9fb9.mp4?token=WzQb1M2ThiBgFfqTl9Eyfo71fSUHKeLUR_qZQvL1NujVyn7_ceznsDTYc-iD0Vi7FPxO0qG9qSpvKEwR_9k4QKzUOd1G06Ukblt0yNcb2zL7jOWCJUvnuTpW_pvo8LlG_R1AgFS6v-Tswzppj13e5FyPl3VobjhtWb84GC87ZsVydH3salrKQkyab4mrzQitC0i8raUH9bSWsiGeqvW6GYTK0Cmn6RfAS-giSayijI62yRS2T-UDMBLejN4JlyRwEHM2COrCmvZ9BBQpYguBoB0S4hgW_cUQQnzuShXrLejOu78JDDG54N-mIyiWwmOH6i0vFypDZq9IhVTKEtKWKLeFVeavgAHNq1xQGBESwf9PXpCdNJ2A3Ho_o80uUcS49QP3UtX8jkWaL9jW5ERJPnBdZarQRDTYlx4qLBvNchWhBDmMIQaCe3l4zv1ytfH5uFCdWezFGTe4ZaXjW_mGeFM77RSuIvQGJGT6r0BmRSNEdJOCrFT1q_dgPCtpBPElqq6T1ieOgTLYo148WH3PiQfDrlw_ueDYPcbX5HJwcqThg4oEnLsLyYoeuYQVyqXDbvhAAiRpIhXYIsdvPJyLZzGFkooSV6DnMBtL0X5C4kKTCGdOKf5-UDvFG6XQJH8oIsDLiOw26RyO2ZNZ2SfJTqiEmpLaQV2UycfUy4mLrzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سخنگوی وزارت خارجه: ایران وضعیت خلبانان ارتش را از مجاری دیپلماتیک پیگیری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142185" target="_blank">📅 11:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">با پایان آتش بس، محاصره تا کجا ادامه داره
⁉️
آیا جنگ قطعیه؟
تحلیل نوستراداموس ایرانی رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142184" target="_blank">📅 11:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
👈
آیا آمریکا به دنبال تدوین چارچوب جدیدی برای مذاکرات با ایران است؟
‏
🔴
احمد الرهید، خبرنگار الجزیره در واشنگتن، گفت آمریکا در آستانه اعلام اقدامات جدید برای تشدید تحریم‌های ایران است.
‏
🔴
به گفته او، لحن تهدیدهای نظامی واشنگتن در روزهای اخیر کاهش یافته و تمرکز بر تحریم‌های اقتصادی برای بازگرداندن تهران به مذاکرات افزایش یافته است.
‏
🔴
همچنین ادامه استقرار نیروهای آمریکایی در منطقه می‌تواند اهرم فشاری علیه ایران، به‌ویژه درباره تردد دریایی در تنگه هرمز و پرونده هسته‌ای، باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142183" target="_blank">📅 11:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74072ea52.mp4?token=ZedfxaBOVR7bc27FM6NNoS_tvOLpoPmcH4JBy6aB7qPq4jyMjIXHdFwzoXNWQO1JXqLKFAmgjTm-o2P5TTDolBrIkEymL5hZdIYlyCi2jkDVCf4JwAe-kch7xE6VOUKqzMmR3NeQ1I1OZv0uV82OB27MrAorMWpAPlYem-TPnjO2C7UVeN14DQ0jiciZZZ483EL_Um8akZ_MN-6HUeC3EH1HyNhhb8jCoOavr61YJ8UskjyALPZIN5BzeYKWJmMzygufa3t-TC0TNTqkN6-RPVM88smJTz44zWjMTTH75uuFprsj1cfM8X29q2Z6fAmmMfkMDJoBBqWdhI3hhB5jww37TRiA34WQNm5lzrq11yRz-NXWe9oE7Aw7VvoBIjC2qNUVFWDdSwIypq3tpZA2sncZsSOZUEA5VIYR_5Evf8TYo9OQClV8jzu9gjxC8dkQ6Fs-CwWifUff3aJrz05VL1k6L4fQYv_4IISUwb2d1ujRZC5tikovXisMuo5NMwFIxR4A_w39xqf-pDgB-2NMKwpNxlbrBGbx-CnsEdg4ZaMQWu5bIeK8CAvm1Z3yK1TGcKHeizTOZagXa5JUAG8_rsnx1yCTfpwgTPDchEm1lQiVe6oyJzTZPUhn_5Chespz4sfVr0fYshYsr6Z0NyqLBK60ndtkTR4jVThz3QHgAAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74072ea52.mp4?token=ZedfxaBOVR7bc27FM6NNoS_tvOLpoPmcH4JBy6aB7qPq4jyMjIXHdFwzoXNWQO1JXqLKFAmgjTm-o2P5TTDolBrIkEymL5hZdIYlyCi2jkDVCf4JwAe-kch7xE6VOUKqzMmR3NeQ1I1OZv0uV82OB27MrAorMWpAPlYem-TPnjO2C7UVeN14DQ0jiciZZZ483EL_Um8akZ_MN-6HUeC3EH1HyNhhb8jCoOavr61YJ8UskjyALPZIN5BzeYKWJmMzygufa3t-TC0TNTqkN6-RPVM88smJTz44zWjMTTH75uuFprsj1cfM8X29q2Z6fAmmMfkMDJoBBqWdhI3hhB5jww37TRiA34WQNm5lzrq11yRz-NXWe9oE7Aw7VvoBIjC2qNUVFWDdSwIypq3tpZA2sncZsSOZUEA5VIYR_5Evf8TYo9OQClV8jzu9gjxC8dkQ6Fs-CwWifUff3aJrz05VL1k6L4fQYv_4IISUwb2d1ujRZC5tikovXisMuo5NMwFIxR4A_w39xqf-pDgB-2NMKwpNxlbrBGbx-CnsEdg4ZaMQWu5bIeK8CAvm1Z3yK1TGcKHeizTOZagXa5JUAG8_rsnx1yCTfpwgTPDchEm1lQiVe6oyJzTZPUhn_5Chespz4sfVr0fYshYsr6Z0NyqLBK60ndtkTR4jVThz3QHgAAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رقص و پارتی طرفداران جمهوری اسلامی اسلامی در کانادا در یک قایق بصورت نیمه عریان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142182" target="_blank">📅 11:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
آلن ایر: ترامپ حتی اگر بخواهد، نمی‌تواند از جنگ با ایران کنار بکشد
🔴
آلن ایر، دیپلمات ارشد سابق آمریکا و عضو تیم مذاکره‌کننده واشنگتن در توافق هسته‌ای ۲۰۱۵، می‌گوید ترامپ در برابر ایران در موقعیتی «غیرممکن» گرفتار شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142181" target="_blank">📅 10:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صداسیما: زمان شاه امید به زندگی ۵۰-۶۰ سال بود ولی الان شده ۸۰ سال
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142180" target="_blank">📅 10:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bkwGv1R4mze156g_77On05XjRzK4iA9h_l29l9H_-Xs6M1fOe6uzEStbDLqFJjzoIYyfdELM-9ARZuPDm1_PZOaYhjgvdYTCOpj504LhuWvxHAtj9IIQAtcMJQDV_m_GsYRg_aD7n0eJcBRq5SBb2hyvg37x9kNwVbf5aB8u9wlJxDzPvUWmYeJ0C7o4Q-6g1DDUtsTdOF5K5UVZW3zK17ayPyll6KES7AaH3SoO3EU8aEu-V4JxvBJsbvBY0qykV8xYs35DDdiY6zKEiH1-6CxvpxdCaMm-8LED8RQ7-Sy-fd7J_b_E3VaCKR9ijNmWNY7K5ng9srZM3RipP6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
مسافران رفتند، قطعی برق چالوس بیشتر شد!
🔴
‏۶ ساعت خاموشی برنامه‌ریزی شده در چالوس طی ۲۴ ساعت، با وجود کاهش قطعی برق در زمان تعطیلات آخر هفته و حضور مسافران در این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142179" target="_blank">📅 10:51 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
