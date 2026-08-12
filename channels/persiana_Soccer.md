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
<img src="https://cdn4.telesco.pe/file/WPcZrfs_eJ9rPXoSQzDSTH9J9gkSP4p5WxFxpEbqaDeobq7LlH9sanTMq_r8EGDEysZUL3r-CHwVxmlHKZxJ7FMzlsNOS5_eqnmaW3t1s99g1SFs_mLQGEFW8LarcdKuByXcZ79OIyVVfDLTGeHVbtSPpBh1ZTvhueGemk91PAyJICPL5nWMeZkSJ4wla34q-a8lrZltZVJ7VapHC1mXvla3Oz3BYvMsZ9bagef70e1bnYWufbkEdP-OYDhITvdGMc1cw1BkvVTdN6rCS3siYrUpF9iG3VBS0oE1ymhJObBnncdnhBcdV28_bVFxHm5DJ8pZvDblMk41MwLtm5yjbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 21:44:00</div>
<hr>

<div class="tg-post" id="msg-27600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip1hYLJCDnRvoIjTkQz54OfW1St9N8U_JCraFyJc9jgZP9L7WETjscmqKyrOspVV606IywM7zzmifxWjg26Xhr79dsavOmmXnL5mQObqlproZu6Z4QRb5XYwUuPxDafn5HxqI-xRpVXuShWj2tH9dPEsYrlc2FpG3_t2ucFmDKVKTplssDdX6iBZlSIJVRj5gYYeXojroQMvqLrOgpcKizrWpd7mgxok5J3TS1r2HmnXqA6uFF1S7QXooH7Y_qUlJaQn1EDQAvu1taGSN_vu8yR9V2kMCTNHEp-V6P4SGMlEudPvojGiTyJBKAFg9xBvCPAmjrVUbAHSYHiN5n5Cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا
؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/27600" target="_blank">📅 21:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzUGofjCFMbmvcPIWTPfAMdFbntX6XXYpAEKgLxBdefQkE8q_bXPjbWhu-h70qbZIwgr_Rk6I_-v17PxIxqBfpyw6sdEz7pF5y1Jc0NbntYPQFplEo2sFfS2xVXVeHaWp9Qr5_4eUhfwgJJTZCjpbvqvwRCX2fl3-2QCHnV2Wkxp3gUDbnG9mUB5iO9FoVeHbMN8BaxH8eiCgkm6IlTvWmFgiapuD1NwccVYLGLVowEwPbbmC0KikcaVfIbEgE-BZnLlhi4ut2vetDOc1RVdfJGxUdMKyFYtuX0rfy77Ow4CUl573MFAOi2HR3cJ6mZ45r9DNMIgc6riUUMhPw5new.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
حمایت‌قاطعانه‌عادل‌فردوسی‌پور از سعید کریمی کاپیتان ملوان درباره‌اتفاقات اخیر مراسم ازدواجش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/27599" target="_blank">📅 21:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27598">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeX19VRkLMbCNv1jBG6cMMss54wzfyYwDXJR0s0IUSsw0QF4XkRCf3FX0dFxTeGLhZdXjb6_HkpK31p9yoK8bIDd3Afn_rj91fpq20rcLYVJQbwyxpZv1vKFLUuOWVx7Q8eL9-nlJV_aiSi-SdNkI561U6jTJYhSvFN87nCOXbZ0mgclHr4gYAZD9Eba7KCZgMA6H3Fb0ZkhdmdtpNv2--Q8l0m8TSvfkoEjdDRt-faB83mbVoFWByXgtkSa4arg6sqMDqPK2S9K52Qdxh82Brey-bjg5RzzVPEs3FFuk1ARKO3aPoX8SC0_R82ZKt8KtpgrOeBximypbLNXWhZb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ طبق‌پیگیری‌ها؛ تا روز یکشنبه هفته آینده تکلیف‌نهایی‌باشگاه‌ جدید محمد قربانی مشخص میشود. قربانی بار ها اعلام کرده میخواد جایی باشه که‌فیکس بازی کنه. هرکدوم‌از دوتیم رضایت نامه‌اش رو پرداخت کنند میتونند با قربانی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/27598" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27597">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaZ_ly8MBRZMChzK72ILR1C7uRRiPcVxmP0geav6D-CiJMeVnK-d1BLH61TQI2kRnfWFQPF-Yh010PAZtlA5Hslf5LvQyuXdETSACUyLd9_tsiDYuvfUl2ujZmdrMJLMISHySmWrjJOHA9APsm-MHMpS6f3A2ItNG6ClLERJSWpV5K1BpiqYMRXEGoY7LV5xUodh2klQdwzGtJVo_Oo0iwCsFVaCgaOgl6-R-RMnlfpO0BBRtrW0uYyIHmiK378V4c69rCa7KJkCh92ol30-fTo-ENkqbYMxIkdP0_wq0cMGyf3GJZrL4UPTXRqu81e5ClMip_d4RM4deWqYxT352Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ تکلیف محمد جواد حسین نژاد و باشگاه‌جدیدش تا پایان این هفته مشخص میشود. طبق‌گفته ایجنت این بازیکن حسین نژاد حداقل تا پایان نیم فصل به ایران نخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/27597" target="_blank">📅 20:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27596">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDdce4CiOKGY6GayEiVSduhiPYlDW7Xdk20GYHjQkNKf3iUxuN64CVz2RxJJo0Zrgt8dc5zlsjnBYqzoQfN8Oli7Jzp7S4WuhsJnWThoQeneNi5XbKGJS9c6EZsuKt4smUPQBBxTYPxk1sET310cK8Y78CGt-5oE6FcradTogtKkUy10HITwE6XFvoZVmkcbsb_QEU4EfqSDdsyDAB8n4l4kU89ssLFazPcIQLuoBOYEKuNPMiBvrFxXzKfNbHaZJFus66NhWxf8AjV4BMFD59DrjzaIz0wmX82pZM04NZS9mGKsPg7zP1jRA5eADkk-_nkSuSj5DueQdGhTnsaa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/27596" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27595">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=ISwt3UI3nCygYwJmEVq0PsLKlNOZXPfnaEA6aJUa498x7_mrz3gWdQb-_Q8rxmAhDZPLDEEXexmNGDdFl7J4fVBsv6NvVOnx8hSS5Cq3ZfMhYBnLrzpb7xr1hFTwDBvo9b_Htm8KuvPPohDFn66AAEa-H9QKBb8IEqdDdhh8JrlTUFRVZc0URNQ3_kQ6RKT549LmBoTPPquRrfVuYYtu2fKIvT9pmbZ9cU8EJgs3wen08Wmk737tdi9R8pQeRJIPtcIZp9xGjYWfgIv2zCtIddXxnKTbvqgh3jnVqcUttdly5RLi2dNzB8opaLlJkbiduySNLLbuwrn2xiIlknG-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=ISwt3UI3nCygYwJmEVq0PsLKlNOZXPfnaEA6aJUa498x7_mrz3gWdQb-_Q8rxmAhDZPLDEEXexmNGDdFl7J4fVBsv6NvVOnx8hSS5Cq3ZfMhYBnLrzpb7xr1hFTwDBvo9b_Htm8KuvPPohDFn66AAEa-H9QKBb8IEqdDdhh8JrlTUFRVZc0URNQ3_kQ6RKT549LmBoTPPquRrfVuYYtu2fKIvT9pmbZ9cU8EJgs3wen08Wmk737tdi9R8pQeRJIPtcIZp9xGjYWfgIv2zCtIddXxnKTbvqgh3jnVqcUttdly5RLi2dNzB8opaLlJkbiduySNLLbuwrn2xiIlknG-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/27595" target="_blank">📅 19:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27594">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9yYhomOai1RFJ1EuxTonIuGCIvAKO0EW1h7Jia43r1-cJ7RP4yjpqpX7SDGHdfon7EQQsKyrxpnJiaxCsnkLAhZOWrpKIQ3zTH6tf7jZOg51XCjZvEXRb_1IveE24oRQVX-z_-htiE58x7N1ARK0IBTV_TO-HRF8lsJ9xy85x_p4k2BSzIlwZarpC3WX9ACatu_eR3xrpcH0M4M9i6pwB87NFg0XQd81NV5htVmftOppZTkVQiwLUVWX_5nr2Lvn2GmMdMQNdSTEnOZO03B5gOfbP_p-12WsDWIk8iPmv39T78taZh3mlATUMiqWis31msIUuMqfnNe0QlhLLWgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/27594" target="_blank">📅 19:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27593">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLnpFEACdUgeMW6kg42Qu-ZvKsW0n924QewKtQxu7-XwFrlE9FxwyxqWC9o8fK75hEaM0BS2aRErvyEXfvcePKOX1jgkjlClw6l0G6FnZHLsdTt_HXMluhFNnRidp2dMOXJMkx3krAsAxb5f7rDakdvlHd5nsG9y8zal1ZBfDPpkwLpybt8OMKZvz5euwB_9RMoX0NTPQeO0o5iEiOuLBa1f5HILGaiK8_IoY8i6nhCC4HQHYX41ZZg-_mpw__sSmXmA2OvrtLUaXufdsB5BMb8xwROMJL_AueglsFGZBzeZYVxURqWPMxzuJfrkFP2L3z0FbCVwg4SJUjUwXusGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛
برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/27593" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27592">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZMuYq8OiobfzVRr7VOPVZtvjghh43af3TC-SU5HdWG5tDgD6oDV9PgcWUaQOgCm2W_WlPud6pkAw2w9plzb2GMe8tO4HW7QOVOohtkvw3XAH6mIfF3ly14KPwVwYz6oppCvywjMW3UgXsBtyXLF_3FCBajoG6rm6TMNIUteQCkjfgEfAMlazmqURHrg9escxuuaLgI6JsjPNgMWjGCCRidnz43r-uIfQzW89MwM_40X8LFKEOELC34_VQT9iOtaVbnllFfltdic7hsFR6VnQsBD_kRaKSHHvX459oMsp2Ke3nL6dCFQNbgRtiXuFvHBovK3wigcESIPh6cDzS8CJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شانس‌باشگاه‌‌های‌بزرگ اروپایی برای قهرمانی در فصل جدید رقابت‌های لیگ قهرمانان اروپا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/27592" target="_blank">📅 19:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27591">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a96IasAu94ix93hcHrEMwXwIwtqIc7stk5KneI9v8roZQ1UpGYGaZRG_sZzvETzcT7YhqySbaS1kriBxchw6Ktomv1nVuYBNbHFnyQEHgeENjUITinp0ntUAPRfqMb7fJLFhistq4-5izdQKR2BtNBPXZZOYTqLmt_EQuy6RTbRF4bV8boPjaXoNk0pIRHii1Dw7LjL5TGLn_Yh70uOvnLeAeTUQUi03ow9KlPme--cLFgoTfW6fyHH0WrOrUgvR77waAgtYvJkq2f6YOGupbV_t5omfZ0yjLFNQh5trzxb6hbgDAdacdZzfTRtu3BLgRBJsGfLGFdHympRAGBfoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/27591" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27590">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzJhGTzOHzGJaXszvLeqm3PbA44P-JUjV38oyIDYc3onydilrSELC6RIUjX67AK0IsoizynSlVon9gWQVNi7ygZCQoDS6K4NWkxjtXPD7UZQRgLjc4qKy6lZmx_bihj1boRkEAkgfB5YLvTQICM-Jf1hIg42vjN8Q0mRdnRi_MhTYiX1UKWbq1nMivkvgdWtdgxxwEdN48-niQLiVkA3NpLPUIMUj6fvsO5WKZG9hX09rMbSU9unOVRScrESVGcdTcYXRzRhMbGNXTOeB4f8wmxdxSyAZIua9gMhCLF1Xox9XP-P-o-MaqqELFitZySooIvdt3b9hy_8YpPuGWVSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/27590" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27589">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUzfmblB66Q88FUL7GkevfLzrXyuaRxt74e2x79VX8-UTULYTAmO3i2ceUFLviSBBRbOFMeZT6YhKl_pqndoODSd2-0j5VliELqDSTXGM8DT6q92EKPC-g0PoEz-NDXYAKDOTtzqvhFjLGMDDpRGcHH0HvC_UN_wbN1vIrE3HMCTMFCrsATC_xTJMvJNpz8jfql0WfP8CwrO6Oba6CqkkoVHMeLijwC_VhXTxJ_byIW07HbneUW4tvVR5KJAcf73IQGWgLFk5Au6B02HeifENMZDDt1jzTEf_BEYbhTha7nHkFUyAIxCjElmFNWQzDv566ahFw59X-kramz7WOOlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سوپر کاپ اروپا
🔵
پاری سن ژرمن
🆚
استون ویلا
🔴
بیش از ۴۰۰ آپشن متنوع برای این بازی در بتگرام
⏰
چهارشنبه ۲۱ مرداد - ساعت ۲۲:۳۰
🎁
هدیه اولین واریز، ۱۰۰٪ بونوس رایگان
همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram
بهره‌مند شوید.
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/27589" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27588">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWM5B4WqQlAlNDMcYd5Bn2qmoo0JZWaO5JGkFu2g0jVl1E3JaXR4iEfYgzGpxLK4OfMqIZWMaAq3LhXSSq4ZlH7EtVEmtVs0EfdvDc_ghBka3yT0ioYSM1503G6w8udX1m_2edJCur4d3bx-h5gty2rWxtzeBlRb44THy-uiIBOYFVqKNyDCNOEdpQjdsyoKmdu9jw73LwyhGWn6D70DmSq6SF2bExWvgxTyyIfrkjlQxAEk1e7c5xeAKB-J6GvlKG31qwHObrrEa4fhw_Mq7UgxTqGosfiRUQAmuPMb7GsKx2wnrqCKlAmkPN710id2B_WplpDPxWkqdE0PNKXpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغام سعداوی برای‌خدمت‌سربازی راهی ملوان شد‌.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/27588" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27587">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpXzPA1K7kxaeRsrW66viw6ztHq0rqFo5cTAq61fV5vxx-SYtd6GxNw9xah_plgGkeR01jKZo-yyqs4S0gr-POFUqreoCcmLO1GbJ-7jpvpQuoteSn8uTjm6Gz-uVwxS3F3FwALSorICoUBHmOqwuL5YuRlz7FBPNxgKrg1aMCyz1D30eKF5RTnMCCmrZRwbn0ktAWxDVNqiFXmX1oW23Z1fjluW4KaddJ5mFEaSJCEOGfLp6JS9n9eD2Ltyds73EqpRFIan9Ge28dTYKQoI8GKYnAMwmcrNHLlxsVHfqLTTimpWeNeTNQAhyAL50ow2W0Xy0GBW8M3mClw2bv6t4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/27587" target="_blank">📅 17:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27586">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU7hxA2wnJe4ukOMPvBs_ZOF8ljwbgSK9smn1tP1zMDvHk58IdmCpkQ1hTgjFFtZtc7yTfuk8RuYO36ZcEuQicz28e3Dwb9IyNzA2V2nDAVAyM-ly2TBfwXJDBZF_Am9DMp5hCY6Tf1JBsNEHrdi_EP0dDDUBUZfVf9BHOd1q5wL5fieIgA48liwo0hP2Wa6kKou_3_1FsUxKqK3yEdzTUwDW6qw_mv56ZF7-lbW1c6bM-F9XfyU7Fz5LuE0amKDnUt5gJe5DPEcTegTdqkavizKPO3PyWmczYjGQy3KzSvJVHUw6fnKsxFsOBSHgdbFryS-hxGm2jR7lVrIUadPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/27586" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27585">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktx5itSYO7ehn_y9-0ePxTb7f_yp8ANEcbwhxaXlQ92wBNO3dkHK66wvuR1ozhc-XtiqeVYM7XRGuIjJ-1BF1HRTwrkYR8_lm552LehyNpvEB2NUe-hVpbU5HQSvaIPqKz3uKTLrbKSQLb4C32YyBcFKgHZU1u5d25eMKTScqN8dBe88Ax9SQvN7DtrNDoRedAICqA-Fjo1lZQb09TrhD0SjjpXS4kaogefyvJDU8APwtlKL-66BiL9wF24NuGPRg_cuDWo0fUZ5FWOJfqm2MhLhwy3j4L5QC_bguCBHgk_JnjVAuX5IoYL5LIlgnrKcl2jpbD3yc1nft6ud2R0CQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه اینترمیلان برای جانشینی دنزل دامفریس هلندی؛ جِد اسپنس مدافع‌راست26 ساله‌تاتنهام رو به خدمت‌گرفت. هزینه‌این انتقال 31 میلیون یورو شد. اسپنس انگلیسی فصل گذشته 44 مسابقه برای تیم تاتنهام به میدان رفت نه گلی زد نه پاس گلی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/27585" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27584">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0r34kpljLJIcHiSAgektvh_yfOwpHE-kg9Zhk-oPRTcOHvgg55cN8xRLmy9-_Id7gcj6GKJ0w7zc8j3ZhhGjxUCpIaa2_ashXYIsx9MbGmFVtp01K1oDHAIZlKq0MgKRnJOL8HqQeFrr-4D13Nt2ebTl-yEIG7UJi0oqRUG8rcqbmPS3hbJNz8TDvuaVmrPCeTDKzaa4jnNAfqU_b7q2o9KGPmwMXdgeSaOt2-6o61WjSoMgL9kehb-BjSAp7Gz10SI3YDpVgpYwM4670iAhUlBgpgFVrIovBmx7nH29VkX7S6g-df3vlbJYClAuUGKED12ua7r1UbSOkWf_MQIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27584" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27583">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odpG9R5mPgXK3TLWy7WsBLn5mbB4khGcHQ1VrHnjL4rvOoKeZvh_ULhhgbAefGrOIn-1buWlz4jM6d6r1RSCLISgjas8O-w3NSbSzHh1UXToiliyxK4_2bgkrKAJXs8JOTYhkDDEoGk81335DVMe_LZVGiPBPBYa1oQsgAzKQDzJnHFghOLJkyL7X5NcZCoS3spuNyOMkhjuUYeZt2NsSfsgkZCnFnvnIBnVjJDkEmLj-sb5zNrc9NSjG5pS_6Cg0Sy8zAF6lM1ne29E7B25VZrm8sV1EUNTZpNYNdnMRhCgYYLTgT30jdMdW2MRoKUGB39GojCqq3g0ynpkTbNCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت:
«در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27583" target="_blank">📅 17:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27582">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAdSVqpV8my8c8x-Q1LWwP9rMuEcojI_xloW6OirBie9MM2LFhhpYZ6qr3QYvRFFx0S5eH-3pRlKgOuzOcXExILSDjuW_SHV7_LbKH8o7mrmgKdjKIL6BnhaLgNh60a4BvjvZ1RhlqPFJRWKEN1tspFe1aielGGq5U8FM4JT7gHY7pD9hllsaLSEcn8PdlCdsmpWgubMj0cGndk1dlo7zy9mxv0CAiFHP7nIrmeRo4Lmrbts6To7vhxQ9jKGEyASCwOtCP545Szna21rpPrPyOGy7qeD_STnpDdKon3LbAd3IsNqdSjYULUo2fZ3RBhCqIZp4nkfkxAxGt0cKkioYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فیفا کارت‌بازی یاسر آسانی ستاره استقلال رو برای فصل جدید صادرکرد و به مدیریت باشگاه اعلام کرده هیچ مشکلی برای همراهی آسانی وجود ندارد؛ باشگاه بزودی نامه فیفا رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/27582" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27581">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvDnaL-El_SV636BkHWaQVxBndFEpp3qeVBn7wMWTKuAwlUtr0eoda9yIDr2yQidOPWb0O5sHHnVX5T5CH2G6ytD1tq18902B8CLQzzqmCCnysk_WbhGn_S2VTaVCd0s0AfQ9ncNak7nqIF_G2fUpEcgMFjXjkGGz-E0AC3oYuHUR4oBGA-WS-CKNPBRUJZfo8N6so3zR2l0lRjxoMznxjqnZy-L9ZWMhcfPUYV3JA_VJkYehnh4b05FzVmNeG1LcTWfmwCIuBpbPmaHj0RGswg6wNz_ANG6L7o88SNW75dkt2V9cBCB7IUuQP2aMaCvmARPfDIRtP5MI2YKmZXN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
درآستانه شروع فصل جدید رقابت‌ها؛ از کیت سوم دو باشگاه بارسلونا
🆚
رئال مادرید رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/27581" target="_blank">📅 16:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27580">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEXCTJpPdlBLgKhY3vZ4OGK7KmrlHU1usLyUpK6jcDl8ZhfK7TKbcroBMCFV9LzM5Rb9prXbriV1EQbnPEEgqiTIPHl8gW8UpQLX9ZVy3SN2GuafEHMSTJAP7vjymLR45MSv4sfJEgqQYIhcN1jc7uQwgxqhtfjZZ-AQAs8m_hzDMEl2_Cim4wNCoNhyw_2pdJmFU7Lz158aLPs-6HTbslCTA_uPx0cAi0FeuQFxqSSsUE0Tl0Nrki3d4xuaVCM40XipweJF39uNHbIy65NWoZG1kuTTKR1ms0HB6VPjxTyz693kM7sVvKpXfMmaePkXiIrIhQU9jL-Q7ydb5-ZZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/27580" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27579">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFICh4Ktln74Trnr7WFH_oK-mU5qGR2_oIJUEDF72wEHnyoT-BDuafXE41LPqUG1m4ioioDmX5zd9cen54KfTc3nAgN8RsumnykrPeeM3WzP3p4yGU3eVazIxAkRYMYMW43HCaUSJhV-uC7CruJnSO53ruj89J_EThvIsPEDxpQMeWp3RxzXcD283t7nVf004O2MDIpyre1qxlWzW51zoL2FG4poFzWf0pm92iHUr8GW9jENWwZoKYV_Ou6Aa880mS2lMckbDI7Vnw-69G1fYa0zbQwbkndkh_u87moSrPbB9NjPbAVfgF5lkauZT6-lWqN3bXxBUNFQihRDv_iFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
چنین‌روزی درسال2014
؛ تونی کروس اولین بازی رسمی خود را برای رئال مادرید انجام داد. او در این بازی، اولین جام خود را به دست آورد. این جام، سوپر جام اروپا بود که در برابر سویا به دست آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/27579" target="_blank">📅 15:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27578">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTLsc2LynphsAU1SDrXzIJvModL6VovRFxP_B8-83E7aP57luyDWQIyQjLVotPzDfFfFPnp7pnJ9eL9IFK1LNxS4Bv8wjnJ9bsu6hlfL5kXUkB7uQR3K5a-7_yxFudWE_uKRj6k0ppiEKhpTFb3W7Y6j9I8Eyk1wiO4LUsc6VWEm6g1TkO2nf9_tfkj70LYr8WDp37E--15K6M7ok3kQow086ks0DfobcGmZjfk1sGxYPL3RSOBC5avguendTFTupyIrxWdy3gHV_4wx3VZza8MXafOwT5JzJ9xoOYqC907qvYc9hUjcWDCpkxZu48CcV2R-Ki4BM6WVw9z97mA9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال طبق قرارداد بسته شده باید 200 هزار دلار برای فصل قبل و 400 هزار دلار برای پیش پرداختی فصل جدید به داکنز نازون پرداخت کنند. بنابر این نازون چه برای تیم استقلال بازی کند چه‌نکند باید این مبلغ به او پرداخت شود. اگر نشود‌ باکوچیک ترین شکایت داکنز…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/27578" target="_blank">📅 14:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27577">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjAqcDx0ENZ0nsn4JhHJBaDw9d4B8xvKAlEZqrKiW9aXcwMu0EXlQHUU6Fk8yeoqKntpsFSJz3s1NdhT9Zo85oOcbRgeDhGGMMlKCbIA2jN_vkWCN4VFjZFvA1S8ARRj63IdTa5iH2PbvBkGhfIeqq40vPv3U0DWK2M30eWG-ozeyMpkGfj1uP1oWDqc1bG0QXzcjtJmo0m7HTL_Fk0DiQlXaPUOWVHofa7IEf8X0U5hqbH2Yh5kXZIvSKKoBgtFthRUziVQqEozFaPiwunFX3iCutlJiN-8-SusceICBfjKlnHxhFPiudOhu6VbO62Ung7yNWZZlNRMHBih3yau_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27577" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHSf3JyT6DtUz8mD2ZO-YIzJfzEZcFcuJAXf4JHA2PH9OmwUs675Kvdv866tgnpAbFGKl4cWtTBT_M4eW1-HEkCok4ZhReXG7c-5eJHkmmcwPn19al5U0lnyBtOt8kDxB08WcAZck82ve8NqhKfaisBPgfGhKDLEkSgr_5xOgTdXCqPDP6K7khIg4--s_7Oc4MqU7yILoZZ4VuLnrMU1kRCUJO7S_BCevQEab7rR9Ts3Vq33_N0RWsic_uo_YKj--ZF8RozQnKD6TdwnXDPydgmjjjYHVlqYEvi8ssNnlQLnCWA9V_P0A4d9LKS84_2yg4Y8IUTj6SdHUYWowq_J8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq66RhJ6MlS4R_xvhDe5cZJxdfS0303K10-jZAFilfwFz5s5QmXMADlRZFuDFU8GRbOuOS0Wm9e3u2ZYED9Af46WvkY9vYr8aLoa_960teu-gmIw9kRBWkdFLnzKi0-MtpKQkkw_PEIsQviTChHGrFxsgsOwoWgAHt6g1GGWpotNtx7bfk_vEYzjwYhOIIRbgxk_b0hHePHfWl3pZPsfZ2HEVp4cJvNmS0et_AkQotIqfFkwOfBWqlrV-FR4DbGPDw7aMhiDeAAYfTMRiMIUHs92OVban7cyRFTLjKfluEuMvC7jyNaMW1ikD-XwwPyHRNrgdJgePJaG2ASpEBD1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-8ZHFLj-rgmG0aeKQeCCVNPWCcQojDPR_4-Q8BzPa1VA51yB9PEcxlpGIhWnn45LfFCjZ-fePHDsQJrxQEUM0_iIzYC-88WVNLuZ-wIe1lxaesrFwqW17ZLbqjYReO73kfu77rnmdFTV6nChAK07QN8lnZcSuYE07pPH91vU2VMLB006PCq5G05p96lBcjUJBv59Z7yweECaY1NoBQKTd0P30Ub-VQ28TnZg6msnK8O3Lp9SmKm1dC52OGIbbHzDmgeITNjFGuVruxb4w3ScPgxr9itmARyGwNGlEH8fyG6zEUBwf7bS3N28jpTX9FgfHcCBh4OfzqAoEs38hnw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27573">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOun21i5izNeYOcsPETbqO_yoR77jpMkj3OaVM40bAGc4qykw7YuLPJX9WbmbqJw-Cj-TRJaxECJafSKfNguit2zzkBVRClfJu1L-uTg33IxR8lbvAxcOe2wEESbguYjrF7zZ8-zfkMraktrqelUL_trm4Z9BCg-HHgayotFt_cpgAwAwy6hUxt7jitw4mg7LjlBNwjNf8K5Kq8jRLYRNYaiwmgFpZwNJ0m4KJkN3g6qZwB5Ck2SAxBAWiPYrjJJP7uq0mMG9f-7r0kh-FRP5Lp91dngd8z5AlR-qzci0L1MmHdoBgSgX6pNgxjzSCHkyUhXaBxApnZREAozJJu5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27573" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27572">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polUpzMrolXYH7EA75wLFNpqQbwEJWonTQ6yRTivPL3REK7vBlp2pMlzk_IX_IL2rOTCF5RjNCFeRV6oWTWHnWeFEoXSuVLb1p1Ag3v-jMCwOm9eVbIFKcSFVLcu1lkJQZmWv5gbFybPkbmF5vAHVoJcXdSl92P0SNDnH4CeFpAIlvdp-3w8a-AW78nBhicyoxpziRDWxHtHueJIZnz5ggsjxnlHD0Nea9Ez2cMViutpZ0vi1T-ZYSrx_pawcfrFUngAyFgAGUNCtucGEdioH04j1Yb-OKGLPqeEeDgaiw1guCzF4TzIBp6F_2parmUi-eeWqatOsCZiChHi9VIu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
بیمه ی
🤩
🤩
🤩
درصدی سوپرکاپ اروپا
برای اولین‌بار درایران
🎲
درصورت شارژ حساب و پیشبینی اشتباه‌بازی‌سوپرکاپ 2 برابر مبلغ شرط از وینرو فری بت هدیه بگیرید
‼️
⚽️
پاری سن ژرمن
🗼
✖️
⚽️
استون ویلا
⏰
امشب ساعت 22:30
🚨
ورزشگاه ردبول آرنا
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🤩
🤩
🤩
🤩
بونوس اولی
ن واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27572" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27571">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV2fO4KiG_KIOfrMx5H43FyZcbsg50EKaO18ttsWLsJA2SgFjcL2_jof3GYci_S6_ixwV_6C9gPW592tGVwbckwcJv7YB_ap6guS7lW8HaTdc38xg5kqVGRrxrLnz2uZ4_nSq8H-X3N3I9YjwI0WHkcw0MT0v6baLO0A-C07vozQ5fh1hlSefFrh27PtFm4EDHL6HArFS3fp0Ayy7jlkqqkv9fLnbfc9goEL2zgzYWdgFF73gE3T4BI0BJdyWvDRTYscQK6A_L5D3UBvQ1r_I6ix7OFS04iLzxfVZAVQykiUtPHtKWmEQ-fmI2mUjsQLpsGAARaBq2GCZ1C1nhUIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/27571" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiHqTncLMcVCYwxMl-j93H2FzLgHXt9HwjCEdCs_2cLvWaE7Y8WjBHUn3tp5UstsGGXLwdFNPOisB3ZohunAGN4EtAbM32ck19Mq0JXpiMlmXxJgY8NyzUpSsCEGjg3YldByJLBTkvdbrVZWCKlE3jrYBp8sNjOjBbOQtxCRnIlhPvlZ-X0TNylbWj17dIArYXrIfBvyaAHN_cJn3GdkNC6KjxoxcBmVHZljGihQm4r_tnLfxkaOJh4u_s3RxCbbPpYNILW318-usuorvMdk8KOKG9boHAbGZrZo74wtxxhm41HwZR8HfQ779usGRnzT1AEZuJcMMCI0dHsXsOkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAN6-7ViViUNG0DL8ud_FY4GhNzpshkX7mHZ-nOIiocmqBi7jn7_tj5WcTg9jr48VR-FZ3Z6L9JUghYkCZVcMMuFkfRX6EwP1rleDEckm_GMw_mwXi-MROYJeNjOOHzHZ4sEvikd8Hn163WN0o5crwYfkSG4Rmv_TIQkq_AWfqmiIyfE0_qdE6AnzfBCNHFQfuW20yxlawSMPERWT5eofHTDokmy039-Qv2nqWIeFaTlLDYr4LqQpUt-X8v9oEPJ8ITYweL6a_Fk9eyz6WSJeGFMru4bHSzTrM0-0LOV32mcwYaKi-ii50wiEtdH8eKP722x3hY6E0v84ReheEzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkL3H0Yk66PdNihoXSRfiql0xDAoaLDVS2BfXqkSfK0DMCYXgcwYo0obQUppejI6J-QEpZY0WK7R9BDCFS1MA6V4EaBFpwCBKRVV23LYaqbT-DyDaKUZwgPeNMTgp9RIlg_blbp8i77xiyItm0U8s-2XVoHmEw8FTNWzelnBPiTqsqQKwajqb7CRtCctCj-bn6zgp3dvUePpF7T6r-X1TDQHx9-S8LT6dQSbr835cuTjOxdpQJ8dGSxFfPpzk5_GMDGMMuOEQQxFn1buRwge-C6aq8iEMLzHI5PEwgkVt4sco2Ec2-8hO-QcAgXy7WHzwjdc9_fwMOxD9OTYT4lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=XUeTnItkRDPDAD5bsZgNT60vDxk1AsiYRNd6gdiF4P0c7wClHivWn0AX2M6vMY_4CBYgkyW1iVkqIRx-emHQGEtpfYgftndLAf4EHsBV5wC42zymMTvRaIigA6Fy3D6p9A3wDXLfW1OnGCuOKrds6iCxZ4LefOxY_R9yZL0OKxI-MEBgOWrySln2vtGSfe_yGs1aZ4wU3SsWXSKr9LAWXaH1bNjQLga6HWwO_36TyNLL0iyiJMf3bguPDrnV-aagG08a1Nt1TTd8ktmV7yueVsr7wreAUO-iRiv2iT22c5z4YRK4xs16TyStgfmJ3Y0IxWcUyAHU6PsWPzfPq7kt2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=XUeTnItkRDPDAD5bsZgNT60vDxk1AsiYRNd6gdiF4P0c7wClHivWn0AX2M6vMY_4CBYgkyW1iVkqIRx-emHQGEtpfYgftndLAf4EHsBV5wC42zymMTvRaIigA6Fy3D6p9A3wDXLfW1OnGCuOKrds6iCxZ4LefOxY_R9yZL0OKxI-MEBgOWrySln2vtGSfe_yGs1aZ4wU3SsWXSKr9LAWXaH1bNjQLga6HWwO_36TyNLL0iyiJMf3bguPDrnV-aagG08a1Nt1TTd8ktmV7yueVsr7wreAUO-iRiv2iT22c5z4YRK4xs16TyStgfmJ3Y0IxWcUyAHU6PsWPzfPq7kt2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=h14zzWGWcAn6P3LKItdgcKqq0T3c1lQ8uQ8BrkLckCg3oVx22Sr_otxk3Gm3f0qrbjhCvXggYWYHnEZ9T7vsYLCGeLbe_kU59AK_BWYZz9LXJ9_nnsJKmz2A6ItKEajXzRM_uas7GH86VQ2plAC5q_JIYFz6wqUpQme7NX8F-5-EydwhFvott3IToHizFXH8VgnEokzeNePLHbJOllVfulU-nUMWsoArS-gGhc_6GHuHGawZZLets51dI3wqAvVwo8jNjfJojXAHByQC9Z48oMAMrjos5P6OCsWlkd8IKvHcq-lvbk12xpyMh6QjQ8JjJivAjzeKlfCc2VuUt4Iq0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=h14zzWGWcAn6P3LKItdgcKqq0T3c1lQ8uQ8BrkLckCg3oVx22Sr_otxk3Gm3f0qrbjhCvXggYWYHnEZ9T7vsYLCGeLbe_kU59AK_BWYZz9LXJ9_nnsJKmz2A6ItKEajXzRM_uas7GH86VQ2plAC5q_JIYFz6wqUpQme7NX8F-5-EydwhFvott3IToHizFXH8VgnEokzeNePLHbJOllVfulU-nUMWsoArS-gGhc_6GHuHGawZZLets51dI3wqAvVwo8jNjfJojXAHByQC9Z48oMAMrjos5P6OCsWlkd8IKvHcq-lvbk12xpyMh6QjQ8JjJivAjzeKlfCc2VuUt4Iq0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbSHv0LNbcEhKDShkKETpX_lZch_oeeWmCymEnFkaFM8lx8wzj8zmAFh4nsBkuRMsUQLB8KIgSaYVnNRMT0PWOEBnB3kngx9TQpMYuveDvwtAQwRKCiFCEHdiMRJrioq9VbnZzrP7XJ9aBcxr_oZ6mEWD6nN88y0ijNZ6KYNo1r0ZzG1wZHPlcwUf0QfzNqbe8FangBqgfNbQUSYkG4BhJeVL3ZqlZ1fiCDKtrAcSTrNa0IS1uyz0xMzmg_rCseO6I2R4-gUwbpqOdMf99lC6E5IiBPgKKBcT2kJzXPB5jBawJsZWuhcTPBWkIF2k3SpOiLlGmgneRr-noFx-Wm_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtAJjzrTW5IHQOghLKLhZlIOJMENNQKT8KxeCCJFSyn415ic5y5VNmma07Xp4HZHy078TNjT41ZpV-6R4dIeyxO2g2H0nx8cKNl_4gXG66_71mqEFtyoT3u1q1n2LcBV9ppzdfRh75UFCZfBr9VH2tQR9E6s8EobC5SW-osGLZiSdVsl7lbc6D-BtI9bHiZ5thD0uNeKO9LRFXYuMs9d6KkmAPShCLKZGJ9XzshR4XSems5rH9K4XKP_ns0MAbF6fCFuVtumaY17Dh3czerOLXDmroW3_ewORDDfhaD0cO6MxBIF3l8nBj0c_DgNCBCZVJsQXYrX2ju67LWz6b9hBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHv6DcR2MZ9ilfMvizuUMtC7e-DD5mPa9AKYUGdWVuIJOL4g6iLe-8FI2OsRoEwzbEg1JIsKzvkgmg2dB6v048_U4P1Ds4_xfeW32U-98o2qRO15osYo8PG41Mc7UrfXA5HH2pHhrjmj3AR476f6OhSriqYTLb6Czd1W1AW5SM9955UJGzDXSiJsSab4jLEUsntA9TIkVwUKFLi4zay0oSxhiW0f2uBF7BfD1a6Dx0eNSMO0cw4R5PCP0UFRMjbLq7PVHawYxQlB09UQeh0gRGNKtUAPnPVg3P_ulXLQf5Xww--B4g75rEcOOcaWrU43naBHeTHkxJ_7rW2bwHMoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC8LGFRFLT25K4kWe9-dNO8a8HqqfJvzTsCWwCzQAgC1PnJaYhZuriyF8-0PhwYVm9_wAnEad6wmmF0kxp__RVFuEBBoxKNNC_y5pYyMf7wtKGIjIKMighjlUMuFB7lr2tP70Gm_cIThvYDVU6hWtoNXWZCjBzwjsGAW3NXEL5RrEtCUXf1UfXX08LGGKkiRNTu9O1JXBT_G8pZla1zoe7p9PshObsws5Km5C8pid_KrNdn0tndybBOcRPSjGNGWnoixs8T7HsKJ_tm_jHIXIqs11GOtBniMOxxNvRPkfyeUkWw2D4CuLRjyhdJOH98Nerpy_X3Aa9ye12L8xmcw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxORaJ3Lb6SNECcdUjt1J6kRP2PgmRbUYtrdNSTfledO2nTVBuvR26saajCPp-E0OK2iTmiy2DpD01JDRbj5EjtM7PY7SYkgrKImFe6e4bjiI0nNC4c8TcWXzMuQVzcn3k3HSpENgPNiONxzv0iQVHTVBRz5VBSm98Tag7wpE_pW75LRdbup_MlwxIhGOCNi-sq3j_-r3bGfjHnVl8B8KtfFy6EaSAx1BRLI5a55CojWpJS5e_P32u50cxqmz26zDV9B474-2WUKvMgiw_F39VCCC5GMwoFoUX_xV8WGDIUrkSt0DMA_8N8BOL8LSi9PFggQhvL3B8FzLMhbLPr3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOX9lpcVU6UwdJe0f157HaXzYlR7Q9reRXTGmmBlYd1lAeJQe8WYR6o9bIN1g5CocbFX4uSD3vOuMq1uoVHLXK1ZoDHHG0E1m7_pySxya9Iye7yhh7CILq4fnRvvljOzUN39vyPi2SRFkMZT64lY4N2BN1lazr3-GCbvVfLKwvVODLCEDr7p-pP1L8Xw5lBQ0v6PQlBU45XXFEXTUYPh2GP7WJpf4Asm0uV5FqtDr-iJ0OHJ9eNHV7YWl3cbNJI5lVMzCX_sB_s1ORzWzKls0n1RlC8_aRFUKnTorvN2GxaurgyGqIIPXZg26fTrIddqyK0HsJD8Er6_nBJOEgerGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4G3z5BHpC9Ifr3-Aeuo_S9sLzHgqVjim9DdygNh5wvOwNdzpmIMzAlJuBI10bLLwW5qv8NRSELbf5RAyp4zsHtptPCGOG4qwsoI2k41bBLxmY7240T9Nw0s3rP8YffV_dQvfcOdvkPL48Hf5HiDyKA6Q08idkFPyAZ3xcnA6j_QiszJGxQ3nlMZQjHVBoFY10kMBINUxc9XDa8fsASy2yyGThlPoftTyNCUinWIcLvnjZdY9pam8i0oOJjHawP-FRsktWppmL1rEg-jO4NTwbzYXowJFyr--zIPA3iYZD_vliyMSbwUDxXIKE7vHJrkz66d40aHIIBcMSbgGC8h8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdwLbH-HQo0nRXCnlhpVJdRBSsH1vp4LvbN7dX45PgflQf7E4-pfq-SI8D9Tf-fUsPFpyLLs-83zVU1k2yTUoDwAjHHbwU2fSM_6Ztawsxjbqou59LYmgVz-RaGcTS9TFlH6JtNgrP1TLjICFxm6gbumB-IabSZoHx-RWVyuX0W0whoU7qrTsna-mb16B38KEkbTAg3qZTjps7FJL0wiX6DZGUkNteOedcmaoDkoTf7qKIs09JvX-XtMy_IQE_s4CBJlPFkKxCVn7WJ9wKIiAOmf-3vpvXpRSnEbNiJrxP_jK10FOzuvm-1FomjELHloehGhm8RPL9515cXCCSNB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGdro5-iURRH4nBaPe7ljUCTinDaDbwByQA2M2MoTQvQT71KWChDD7J-2bhPYENQSQEHBbEm0Eqs5ytFPBJig77tXmnmUp4FRJJDyZBLUMJ1VebMA1HI6Y6WmFFg3hZFHZjRDYZf_54PDohJBhxTMiS7C53fyOZ6ZTY30hXZ2J1ucHQe2yp35m3caDzL68c7s5rlPIS8D73eqatos786vwkLZ4Xces5-VF0sXTG9Sc8c0lKs8zCLTk3sfeZ1NVVXi0srKRiGFFFkFBhcjPYQ66vyJQth4Ja5YJDTOzy55zyxiXXe5YCRLS2oMdXapOwf9OntU8rOwHh9jlqgjeOIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTWf8KggEO_32wYlFdNcxob7DSE1VfMIUcT3T-Y93d75wVaJ8MbJfxKwLqCu_Aa8F1Vx8JOgvkZv53UaSfcL1czGUn9C80C8HBlTQEszONXx6c9Jm5p1oXR0jhCmGLZfOEcLaO9SNfm5Gdyc7hvNoJ27ukOnHp-hNea__U5pUZEmbVgV0noB21U_I--XH3fKo1e7Kla75Nsa5H4zDQTSZIqRp-lfJPQSriXjKrhJGAErpQCH5hQkD7WV63qhXG6UF0RHa3IdNcXfFa1scfreGcnaBq_Joz4ttpbQn1du12F7KJtYqiZRpVxy7GvZ7Y-9Qj1NJdd_BFfAToGbHNQNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jal0JWMFcAU4KmrMOVIH8FmUNEdjq6NVpFyvRk1MjRsj3Ju51T2-f8K19fUkru77yZGRGtIt5pPS73GchVM1BFDVP6QNWk8KvGQWO-Y8LaP0uJRyMAQLht9-D6sdK-_7jA7bn9gJFuDamL_taMMMmjbEFSXY1tsi3OMHT6RYZ_WzlRmtg41BfqHBJdaXJqIKShj8zFmNG74mQT0TscHNRykVZ_fsGOHrJLZXu8sVkKD_cs7-4EyWQityu7_m-OW5eaF4tda0fteagRy3HKru9T8lTFzdvBN3_TG92J-5He0h3cuWJbORbLK62Wj97lP8jO-p_6iFE77rGgsVMTNfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEE5QOLStrfIFunPwXZVZe9tYRYSzuOuSmZW5MVDVw0uXDqg8teb3-4qyx2UlBmhiQl4zCIcD1AJJHIde0xXTGiMZdH_TOa7d76Ib0TYHIk3RgpMQWmPQR2G1D4-EW0dtPtnXJqn31KLs9y2Xo42eCgbcwd-rJujP3oniGZ1WwcReo_OQVaWep_xD3LcWeTu85GzdQQy5L1lKvzFUClrAhgm1-eCfldI6ZZW_k7p9tF-_TY9pZRteNT5E5uGyr2o8RCIXyHmezOhmMEkWl7-Sv_kdeHcL7Dcw95J32wK2VVrsWjWytCO2y-NQ35D8mgbCjSmL-v8fKKlPPYZLRTbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNohYNe4AH5E0g4fazZa8j_AcLC5A4b6UNIDhEaw0CYw6M7Sa0j2dPhsJVyo_fHo09tQYIE-1PwE78loKPD52hs8vWOVcvpQphPFo3dXX4_Xt8vjZPKNVx9u2lsdW7HPe5vdEgiaI7GI3DlRs5J_c9USh_ORZrSFI5EEmktGa6QcJLUnKWXVxGFhVLbh-eEik2exeF-x8ndDMO965YLBg6-2JApCYYCyyDnaHC8l0-lecEgbNtnfq14iNs077WevqsMyxpJxkfL0WWhA-fTn1ibyJyIDN1pDa0swXQOfMPwYyskRNoq8uRqDUk-LdL2MPm8ob-s9pixL0uyayCl4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSnr5wbnNHRoz84EoIBkkhSfz866Pj0EBjWJpYAuLev7jeHTLGoSkmK50A6pHUKVtfdZWeJd2N_ue1-dyd3lxVCebuIcpRvA7bw4uiimeZAXcybGSWYaClfhOy3ySCQx2eUZB0IUZxyzy79OURuS8kqdZg3RzpxkAkGUuCsqaQDuQwtbNaCNWHOmP7cWsuBg63T20DsvrR5m9REiVtvzKYhQCf2M9JwEpnCJUqHDBAeZot-lTHwFoB-FpH60hQnHgCo8IP2R4L4MZPEW2IiXj6jmr1plShGp5ZyduUXxsmMfAeP7EvsvkisztmptGWOaMUDPDviC_bhDSe5l3GsorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk7RQvXFZnS3Z_FJHixfLs-O9kwn50t8AT9bh9pwmGXSKn-MccwzTWGYLa5g3f0_XVx4kavjtZXEk3VHLBGt9Bf_alc9lv4neKDDBy2JBZZI3MrvqjeIxrKZfZ6CBiqsXbrYUzguhv0sUXaAUUtMnaTQYceZwKUNIsRB-6bF7hkl-yCmfRWRqQBpTiii9W3i0Ptw-vPT-CU6IW9Lc9mhoXwSobG_q-Y0ewWSt6GzL1qlJFXUR4fz3cnWe1HQsl4-cj4tp3TOWe2iQur5fvTC8SH4HA3m8e8QHvcjBNt_g1Gz5udFC9nsLKuyOISRHqDevzGM5fvfm_UmSNuzeWaOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4MWA_lUyZk8yMqH3I2Ck4t0R6t11lWHT3s0oYZvhWghEmSJLieOeK8TcFwRgwkelraDGfQ78byEkZDEfsM7CT4ji5hAHgn0YVHAUkMmuRRoAX71gDDqhtY80LZKqOKKW9_un4AhoQ5vfQ7ZvZc-RxxavY3QPS7cZWXLd_fRHqyPT8n5KJTf3PNLAZkzmG3jj6bz1omxd0E4UL7ibViWdWPbG-VrJ1v2fjJUQyeDyvcaTixjsGPhHqGcyVtlpeqlne1jxTACBaBEZiablIZzU8PTt5YlAq1KjOqsu_NF2oiu74rxKRrxBS7HX6Aqzlb-jX89dmPgnmB7gHOXcS650Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHUYkLx5x0On_f_BX_npP8L9jxZLT2nF_3G-RowF8M9Eq2VrqmLjfTlFunDagNCWdwyff_0qN3IxmeVWC2MmJaNsZN1zoDhLkoh-dE0diRxhPTRgem4KjlKrVxotyaaCqK25tDWXP2Qk8dus8M3q_OkyRQUS3mxjpAYItANnarNY0yk1IHU5t2S8wq0pMFuick5EDItKWj2i0UhXHvbUpY_e44SCcqaJWbvDQrCoir4_8ygdMi1VcnrdQEzb9F6xvaO0E1qKjmR3shpNT9CSrW0Fh4nYCggZz776N71X_1bDWUz5245Fqu7yrpyD8bsmY_MIOdHj9efaB5EHVgCi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=ShBHs4JuRkrbh3KAxXxr31rxObkoGrUtaDaUBgDHfzoIfM7dHERirkp0Atc-dJHacdgeOdh2CwMifQ1IdQD9ibB745nVaSA1dmePy5bAFxxw-8Iw2ZSyzwmtXlumY2jeLVxkaK8iKBurLin4hIHchFyqyRQvugLKohq5stpyYFJR5v5s81nczfVHwR7kGmb_Pvf-D023RHcbp1VXf0vx99CBTUK_0JVhFXx6SMSwOx0M48VX9Nl2RT_ejuF4HpRU-VtDzKsHugQn3ylo-96Jo0iz0LQ0UkMo2IIGUNHTKo3f-bz37EQd_nQFS8jiSAicIOJm4EayZnYwetpLlj5EdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=ShBHs4JuRkrbh3KAxXxr31rxObkoGrUtaDaUBgDHfzoIfM7dHERirkp0Atc-dJHacdgeOdh2CwMifQ1IdQD9ibB745nVaSA1dmePy5bAFxxw-8Iw2ZSyzwmtXlumY2jeLVxkaK8iKBurLin4hIHchFyqyRQvugLKohq5stpyYFJR5v5s81nczfVHwR7kGmb_Pvf-D023RHcbp1VXf0vx99CBTUK_0JVhFXx6SMSwOx0M48VX9Nl2RT_ejuF4HpRU-VtDzKsHugQn3ylo-96Jo0iz0LQ0UkMo2IIGUNHTKo3f-bz37EQd_nQFS8jiSAicIOJm4EayZnYwetpLlj5EdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BghJKfOzHqlFxXczLWvxAhZzb-1mqjvz56ul-GZVM5WIgrMm84V0LJdP2PzB6uyCFkx8s2zSOMVw_2KD8B6WS_QZutenC73LIVFCo6JdzMXhcyvCNOSsSN0xrfzbG_zTbxK7jLSLgszpDrdkvtbiCOpd3OG8LdIjWi4hkIbb-zRaAwXlwajV4L8gUSq5ydoA4LpCKnIqaU3_NN0O-zq1Bb9vyIEB4g1H70Np3_15IspKoV68FiIlimLxEKTLFdMDD1u2qibXuB1wl3uIfL6qQ5CU2qTOT1zTIYeLwQY72TasplY4NewrSsFSmUNG9Po0JoYNS7A2G5rWz0TlBKkt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwJU1KrG9vcnipdEiKUzl7GTs1gYyCAGUL5_loTvwOfA9oJwFw9itzP_whKQBy3ItC3TUbd9rL0nnf6a3SDxT7hIV8DLtSMvMtcfD8yymplebDw0MOGAQMu1x8mi2WpRP71f7R3DMBWhMY9z5D23WM8bA4d16GfRNJ1ZBE5JeBKNCjdPLYEJy_QK8VxFpAhQnmTJfLGHZblYdHKq3iET6xJ3Td0VQnK0PXyJpY2P3gsRZ0RRUyAeT9w2JrSlsFRoMYa0xNkE1lfOnIFkYLlObVbH0JS5SfVoCQIIW672EEv_vB5pt157yUM9EdiIFskiC4fVd8PF5MMQcJwlJPB1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUmbsImOQj4D-g9fYtiSTWufAaRYhr6Ac-5Il_1LutI-ASyU_FcHbSehmY8evcBG_a_NPBuXjFP7HEgdOfcVQM3i7Fr3-wG61ZpUNfmUi3qrVDiuPNC2C3X7fkrr60Mly1vqNkkTFq6rgR5HS_Us_qfb8hskFajaUAUfcpuus1csSGrm5EDaKFXez5sxQDK9mz9PMlB3bTbkec3DIMdTEpdjPT2PHT-36nPPx-eC1s1yy8F8YhvoamMMYwBHKLWeTTa478YKAc-hAR0sx4F5G-nRXWiFjcPn5zFW0iY2D757wATyhA5_1Fltx228Y_0MpJn56rZCrMWZnwQX5FG5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXnzNHx5zIJnXhT0mI6s4KXYmRn2R-AJDvOuIw1Tdo6QPrKxaZIHuL1r0TtFC_fkfN-yLrxzlhMiFF5df9BzBcWPY6kJXDBDMatxxXjUSOsz6PdAxPttJ5SxHivHOWpKo17Plb6sRrYrXSyGFMtqQa-sCMvIPef5WAZbHFTDgFpDuVmN1B2oHNxo3n3H_8BPo44LVEpfCfLAlW74r2ht_TKroUcsKueUBliMZDCpBx3m6CQQOnRqoH4wTtd-ANBh6VaBQmxUG8FXymvJkBHZO_H8XGq7wTnFQ-TS99QLyA2wLJlqJNcZMfBk4gioQlD4_OncHShSOlKCewSfqhluYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4NUN2btSvcAP0RmGDgWmrNPZCubOpbBX2Gv6Kg8hHC0-hTOsmCPep0YhrUZy15AR3TWjwWbp-OGEAZx45jMTK5CrwMusOAilrLhq6_aRolKeRaODgEcQe_0QwBU1g01-A1dQcDA3qcmvqg_psrJqlkzU8Kv01tpMrqjoDmbk-p3-Jbt47rVsto-WdvXYCziIuMlPWKlm_J0idd75qIwqdZeX24yweFiqfsscXYeLqSv6mg6jbl-smLEbLRn77sbrm53qY5PQu6yTBQj7NmRPiPx9T6FTowA7RZZZ0G4Ow5CLDo1sFKmn8JftAxPuJKMUW5mCyc2aL5UYapMBH-K1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_wV9cpt4B_LnRgqnlFeri3PkXIfE8k_ir-ft_SCfMCFpEZj8zMHUgIgibkvpR8USbdwQXCaVO46E_zAWcS5hwviQZeYt2RTV2JDiw0Lj-u_4P_tg0pfZbOzRwyRcxT0VVHHK1s0hGEQxwdmorxzph1G8tLOBdLfNiLTqGqWQNRdomlUZcm2oUoCSVsc8LBj1vh0odGWm0GsJA-syx3Vpg_bb5TEU33miq7YoUsUVCZvizP4sfkspHJOXOEF5DtyUHJZ6E56TrwsXBiEeVonYTBuennOBqc37rloyMKN14jSy-Nh8n7DTLuJElsrzA3vaKoZsdvTvUcWj7VsggDyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-E_0ChQCsLIZwFEv6WB3u7bWsEnjpjUKPNgY8Q6Tp0mqU61_yoL-MoUV4vs-314_ZygHpY_41M4ZUKmyxypSAiuwzUgzAa1FOlV-uxjWiEaayQhIrQSryjOQ8XTv2sl95uHiMJAiWZiwcev52IF6ZGaX2LmS1_XiU1oMwFJe77H9qXPhFySMRhbKqEly352_KAYgbeF0f7KfTeXI_eXG4gzzhqtzS5iDvqPBviPiDB7KSPF46e4KSY1FAROSsp6Z1SgUAKSFotkDzWSUMS6PaE8DZMRpxAMAoFwx2s0v11Jg_FpzZnFz3TaVyvwM4jUvtbUhhY8yYS18Z9lsnlwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE2gcl28q5QLhkgoiLQkMu_Uo22FlgHSfRv9QZU3tLHPXQVQHFOnPhHf6QG5WnhE4G6mQifxg-c8upDXQJlaHevGHq2tBidgbrc8Gs8O0blFZ5oIikIhtegl8GLbUJD0yihtNhf4MifhtRJ4UNAXwSvzn8VvFMZiclTw51VBByO91KdRizlZIPJVVUweHtYEWhvn7nldJPN2RbD9xA9jO5y4ieTHhk6z6wYtx9xrjvQCoihRGSv-kWOATx6ZigEvKm6AtUyx9nAXQxYO_GflJRTyJi8OkA_1oGGydZOOe5aTu2IvPJPfDxu7hTq3NcnqRGGyMp2QNuc1Swi6ULjPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=mtpuM9mys81afNetngv9ZRIyLr9EYOMpcAtGzhwrPFSzvLi2-Glg1yAmk6dD1Bwzf4FpmOfupx1M1fRHY9iLIE_6efAjW7EGbxeEaDFYCfIj7_xtYfOiayHBCtLQ4GU8yhAHakFGBN3DZEuQyxF296QIENp8RwOn8eh33OezSJ9ythdgGhrmtRlPIjfIEkDATsKOGs3-alAKPf9GTgd3TRs8M_YXH6Xz5q2OzPqK2tiwIo01cmyXVDnhWKAQH_tkKAMimp9Q7-7qirwP4N6BkJuGLTTCZNNLVS6fEp4cpxP6zHDXratif3mZ1CwfBdHKdf1n4lrkyUW0-MCnp6KHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=mtpuM9mys81afNetngv9ZRIyLr9EYOMpcAtGzhwrPFSzvLi2-Glg1yAmk6dD1Bwzf4FpmOfupx1M1fRHY9iLIE_6efAjW7EGbxeEaDFYCfIj7_xtYfOiayHBCtLQ4GU8yhAHakFGBN3DZEuQyxF296QIENp8RwOn8eh33OezSJ9ythdgGhrmtRlPIjfIEkDATsKOGs3-alAKPf9GTgd3TRs8M_YXH6Xz5q2OzPqK2tiwIo01cmyXVDnhWKAQH_tkKAMimp9Q7-7qirwP4N6BkJuGLTTCZNNLVS6fEp4cpxP6zHDXratif3mZ1CwfBdHKdf1n4lrkyUW0-MCnp6KHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPZG1to1B8RgLUZYjxU1ctKuVgRZJxxJ_dEsVSFFHD5WJz5xS0qlq77iKN-bXeq-h2nLGfjoreiPeR1-4WctpWpSUkav2rbKBgK9XjZlOD2smIHsP85D1ynOEzGWLUK27X2BmlEtV6DkncPN0PbUGv-NquS0Ygmtu0ePUHBNAW9v_nAJWADqFOPJHhbKNdb5ZdPyvMO18V_ZpbbOde5uZXpXF94oTh9bLDGKTDgbBiLxqB0z4R7U39umyfdN1PgGh5NJhjwhbgbiH8-3bXETwoH5rBfghdBO6CFWJvYh1y8DQLDT06ilo9EPg8DWY4vGPJYlGktb5eiuBnBDPv_0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZGgakHrZDhnTSWVe5MpsEIbph4nt0RQW6T6DDOSAiJ3nR-7zSd5v1dQcZ60G_oB5t-y6sj-Cy2U9sB2GrSC1IYI8gyXz1LaKsOP6g4kCCcFUXC0AvEUV4BXw3nQ0aoZAHlE_23Ft_oIrHIZHm_0a11h48E8KZLUIyBn2sW2u902JcTGA0A5do_31m5WV_covkNsXHsXra_VI55I_VPGyp-N_5yyljFV-QvOA7ajUF4IGsZAtVjNdJtqqECJmdAqKUdKNIEZJj2BRxbN3jzxdgFkP5RLIwvfHpxV_wwW9Y9cEv2mCwvCLOd2-kQ0UvbJ2JoXKiyK090Xf391ePq-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyy4AyREj-I44gmykHWMtjezkADd_qwZHJHMzwLByfxQ0OJiKLU8SKrf-ylGz0aevxWOA03llAplUFh2CzNCUxUlImDuW4vMap-SsApVxBFVp7cFiuM6k-abMvDPKIZ130sRYtChwVDQ275qoqzyC1NWy8H8cHlSdYqcJ3inu5cMtRTBnpbBBibCHmw_9dTFVgS1dwM1ge3ATQlE4UE4QEWX46rDiRNiybHhkdG_lF6lyxMmemt3DpVC061ZFxzGpAGO4n7JPWpwi9XIaSvxd6YSXU3uWjmsvroK66huHCgoe04pR8c_CeO5--tVNrnVsbxtyohyOQ9JOhBGvY5Qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYRCwoFimUEkX_gH7YVPUSsnqmSFuwo7bsiFn7gyW3qJiJt2pKGH4s4Flfnvit8TByUKNxIGpTVyr_VJ-IWKJYn3InLYCx5WZ4LfhNZwIMcwNf7ZTWEWxAu7M9nmXZigiVoV5oLcWZmqeNBhSywR_26zDdxxh7tyniSrW4S6rJOSFCr1DH7iPesTq5tFpdBYdzgYE_F5xOVNrkqUSGc23_dnHApdJt83KxdAdbcbKUNMe8ie-e1qLYLC1oKl8zdZO3WxHEFuOjPk3_b_nz76Om39KmV_tqKNk74JBj8JlU-YvLVIHj3sq31QMDRcdWcXBiWANhdMBrfk6BY0sxz9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=EFGX9uTNbtkvxsvtPc_34t6cz1-pkoJQAgGkSNPcJLia9CWbdUjAn15ZyxaKel8BS7zwjBVKWGLURfwq2BFJ0u4kiz98v3M2tCls6Cqa5l8MkmODNVn86njCiu1fqTIVA_3xa3EkSv7i0IidTFHzzACMieao0e_fNgwNoLybsfhFJzdIBjtUgU3ezA2bArmgIaQgTTszdNCUR7lcXeBHil_cnzYVY-zJan3DoiG6NNLdeM5BR7WLVh7GCC1fgqfH3-GkHrxVXfayrQ7E5r3uQE__n_mX8bN730cCwCLIe8cMQhEX7APlzs3imGtM0fzTgvrBom_wwqr4k3VK0pGBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=EFGX9uTNbtkvxsvtPc_34t6cz1-pkoJQAgGkSNPcJLia9CWbdUjAn15ZyxaKel8BS7zwjBVKWGLURfwq2BFJ0u4kiz98v3M2tCls6Cqa5l8MkmODNVn86njCiu1fqTIVA_3xa3EkSv7i0IidTFHzzACMieao0e_fNgwNoLybsfhFJzdIBjtUgU3ezA2bArmgIaQgTTszdNCUR7lcXeBHil_cnzYVY-zJan3DoiG6NNLdeM5BR7WLVh7GCC1fgqfH3-GkHrxVXfayrQ7E5r3uQE__n_mX8bN730cCwCLIe8cMQhEX7APlzs3imGtM0fzTgvrBom_wwqr4k3VK0pGBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkdWeZMLTKTpFliRexsaXKaM03x9Wa4JR3RvrWzXx3oS1h59AQgAyKoPI4zxurViGf-pXgqHH95vVlF0tDA_oS1GYysewwZBVZAiGLQzgSX1YRBXxBf5Jidb_REBS8tsBsN4DnJuvpXcALKChhqjfu5mHltau98nME0wV5E9SesrK11w0PQF2T9WtES-JZpBloKXMZL7ZBl5lsGva8pwICVmeim5SzeaxqCofbUs_wek6zpuu6Zs3sGDRxloKkohS46sX_iY9bWpvz8YogNaBpaXX4sFO2MVKD2jbgTMVdeqHZ62gtklvE6DmelpoJMEQz_l7jPBi4LMARHxExmytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnSG63PVk44d9XwWRoQzx8tVEK4Em2z5swdgKc7PGsyj4TNPiZB0iEh7uwR9aMH21FK5Wfn7pgAp-Icc3_tg7WJIhXjOmS0wiQavSDnvEeYZfmgr6UShPB00_iaDKnBBQFPX9nOAnW-Kcpo0oPqr7xMjiFr770HvVCiJcymbG_F1IN9QS5xjsY7jM7X07dj4LXBvNpKvey05gk_WNFIE0UJM8XHLev7C9MUDCBilZvOE6hoDDFhIPZ5aPrja34zg4ANUTT6OW_iJnUdg6EcB1JEPAnGHhn16mnnsJjasR2IikZ_ILNMieC_mSzFpVo10YNGIRZF8232x-c95wup3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag2VFeQEkrLJ1jix85fp3Ozt08XodkdmqS6E8HDiz1bczpgs6p-N1Jm8J18Kq_hNMFSE_GDx3fLK7ha8zcfcY9GinXcz5tscf0M5vaqzjIoPoQGUodQB4P2L59pHJQHH90EmlUbJCFDnw-eIPj3mQzpNeze9rOPKgNYu4aVHix22ew3uDQD0cOUt29ywLb1JRlRwDXnjUhJu3flZTX56zoiZX3L5n-OgHf7MS_HPTInf6zx2QvS_UTad1P3XgjwAfrOvR9HDFxlWdmS0WwHUVIMoKYSqYBNszUkwet5e1m3boyCedOvNsA8Fh8yF97R6G09izq0u1RFvIS9C5zl_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTVsIiOWKlGO0V6II1KIALfbH9GGzMI3jaEZWHSNnIkUiyUV2yizml3s4S0r-wDyj76F2R0jaDM7pnpHjupQb-iUAJKAc2SKUUQ9c5xb386c9Uicz36pRNCrQ1EIrWfgrwZTCpKR0eJ4Wz1hAwWmuft-ObghHE3XEY8FLdBsUPU_nhfPKUd2zPBNl3yyfI1F7g-onJusEDHGmCOwBEejRgFtKd4EBf62IOTKZmg5yfg5wmEisFacoe-3B1Vi4aB-Lep9sNNsQDi-WL9Oj0Z_1bz-VRPv9wmswLRY_cU1SuyCuFN2aX5ymt22u3ZZA0qHeY_frfpRT3_S1ZPuvzYKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM-aChxGkVq6r1k8ZNeAbYGBBgTgZ0EcHU_cXHeysU5zvsPz7rq4r0YGCis-jIO6dMUsooLkVel9XxqF9s5-a_fwB6E_Alm7WGJ1741HLFLuYjdUfUwumrJy6z8IsEgvkvLSllJMzzMb98C3jlAxkbRbhv_Op6fEB16QCTvwMkTfqdgNo0A3CqilNDexJ837U2SrQfWvr0K4dfVrPBKNVrthiv2ln8tqHncnf2dPC3Qs_PnKnfZ5Pgjpyszt10iALnKmat3O20UhIpeMJzwFLeeZZVCjNXPd1exKPm_Owef0k4hmyuWypMyDc67XFdoTDhLNncTEEGsEXcrWbnIrFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfIJEnn816o9b7d1S0hoPwpd9aXpZhNcqxD5EmCIQ_jQBiWZh7DkltBN5UFonCy6PmbqXJhCAMdZp9CGnxoG2YIbUIZYh_xXU4RlfYkduSN8FxIi7MWSRIhDHECCfifQiG7T8IkYuYPd1Ow1CNisPVdOElNH5ncSE29UCpeVQcvks5HWF_9fW0Haiu1bbBH9rWlO_PWP-GB3bB4NPpEsmvksR6NqmmdP-cNZ3FEpM6-5rul27j5OaYjnyh2hOWyW-RncVBLc9bK7l-bxr5YcAHomrKZ-M4Vb95du22dAVub8Px1581A4H7Itz1pB-JLmMjlG5DP7f3qbJ46VGMFY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E57THIimzIIx4Sbqo8ELIau5Q5wV8oNlyBr4Lp8YVmJr_k8xoWpNM0z0-9ScYjlmj1s1uE5dWG3CIH6VNfFj2MjrpdVuqwRmN2yQRWi1ie09zC-EPp08WoBiMZuFc_hktpx7QCxjntZXp5qrnDStj_g-8gJ36yKnRSEfscrmqCvgzrs8g8MRtYbXJpi5IcCnTks4tG67m-A7-ok2cLQWKut7Z7k2dCUp-ig3pfaljgHigxLhI04pB4YsAOC2Bs9n0vewydICFFVs_fdIVlvo85ot-DbqHrKb9WCs8izIsKVroioi7-bRHfZlAHUQErbDUfYrvYBgYBXjeBGFDwhiNsGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E57THIimzIIx4Sbqo8ELIau5Q5wV8oNlyBr4Lp8YVmJr_k8xoWpNM0z0-9ScYjlmj1s1uE5dWG3CIH6VNfFj2MjrpdVuqwRmN2yQRWi1ie09zC-EPp08WoBiMZuFc_hktpx7QCxjntZXp5qrnDStj_g-8gJ36yKnRSEfscrmqCvgzrs8g8MRtYbXJpi5IcCnTks4tG67m-A7-ok2cLQWKut7Z7k2dCUp-ig3pfaljgHigxLhI04pB4YsAOC2Bs9n0vewydICFFVs_fdIVlvo85ot-DbqHrKb9WCs8izIsKVroioi7-bRHfZlAHUQErbDUfYrvYBgYBXjeBGFDwhiNsGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNNTQdNyW3JE0phBMafSJ9OiJsgTjGHm3LFAqTb2jdoXK65G2Sm1uYWGPt8PatYmoYTWnyf2bcvdzl3wV2ehMaC9taTgJTAtJNXOYpCWKnMheoJFqAXZWGIyLUyExmSrRgJ0Ol5BY8uP0tRTI_IYfzeqCNy_SFEg3u557HTIkKWqwIHakBmUgmhu9GszYS-w5M_Cgt0m6Kce4U9uCcTIQbnNLLFSQd6cTvAaU6f3qVBaFEsfuHTuCyg-BIFhvfd5hmjDLPZvaklkhtrZLSXDd0-quJ1KoUUb698NWj4uRpf-rtEkf5q4vkPkrX6ua8eLfQWR0zQw-SJpOIZZQRXGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaGGgcW8ApWc77xPtMKnz4uGaJ7oVRNNfOfi2Ju5t5yaHJdhHmZ97TAeiMzqWxMeoixEoCRJK5ZiupqlWKpCCN_Hr2oDk3-uQYlZ6cYUVf1Y3172jJnO00oJAyJkqWuhvxjI1mzIwf7Ei8IvhLptmOhm04uo0oiultp3A5PylZScUs2OeljdWD3fw_LrJYh27E2SrbfY0HlT7tHUSLXEKcUf2IsQpdwZil_qinPeCt8tq8fH_mjn4PTglt9ZExeKtmTpVH5MVGznoVE8oxaHSUPAra87dNEuRkbG84NP9XAnlgi0My5Q1zOR0KN-YJMpB4VeTH0TWtIplpmZSje1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=oGRrhVyyBglKbyl7L5vL6o2tmp12D0Vp4FCrKNAAtDnr3ZHyuptC5075Se9rwn1xgRFFWB-8w-pyB_zwJQY4YPPpMbRiWcRIU8Y6JxbMF4PWGTC9mxXIu5aKurhMQ_vyGJ9hKxrU3vLJzVXR18oG0dswhlO4FZewvh9hU4xyDYq4Gm7W3fEnyjnc2uiBZCurMb0ak4Fq7Jr4uf3Vc8MFtmPK94Dkzuixuxy-WBybZLdE93j2YXRIYayzkooGrGMrfrQAA3IHYniMxBNcC-lXBSz2YP4fxdXG51xFBnAB5QvDdMiRZgYG42uiaVCnomLFbyuRBwaa1KPPG0o2x6JFjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=oGRrhVyyBglKbyl7L5vL6o2tmp12D0Vp4FCrKNAAtDnr3ZHyuptC5075Se9rwn1xgRFFWB-8w-pyB_zwJQY4YPPpMbRiWcRIU8Y6JxbMF4PWGTC9mxXIu5aKurhMQ_vyGJ9hKxrU3vLJzVXR18oG0dswhlO4FZewvh9hU4xyDYq4Gm7W3fEnyjnc2uiBZCurMb0ak4Fq7Jr4uf3Vc8MFtmPK94Dkzuixuxy-WBybZLdE93j2YXRIYayzkooGrGMrfrQAA3IHYniMxBNcC-lXBSz2YP4fxdXG51xFBnAB5QvDdMiRZgYG42uiaVCnomLFbyuRBwaa1KPPG0o2x6JFjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyBDWJw1CX3R87QaDGQXnEWYpD3X1ZEnWjsnC2H40ssEy-FDlVLI1wMkVakP3-pIU9GFCSzhJy1rnMFMJXNz74XtmCWtXqHDeSkeL9AkuDzTcB6pgl6tDELa3Kqa7RAmeRw5ug7GcSdIr2b-3oMQc6hklCDPDqvuBEalHoQEVS_W2d1VU5j5l3rGKsev7wOpgnNuCj1ye_rul_TbbnBchHc8bcrCXkDJ80xa7oLWBvzVVE1SVDYQ98MI2ckFF-ckLtZLwy2Pf1YieQNDs0XVKqc28rR0FMhfrsvcJYhnglv7ZRTK7-52YYZirmz1dLa8p4nwC48RD0qDxscOcf7gdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgSX_6TnovM6vCtDAFCfse-US74j1OIhye-m1CMRYD4xmK5auCFPLezYpgiTBDZRTCPGqkV-UNotv2AaGo17tnR2SqLYnx6OvYo121Ua1F_j6yhp1ioboy21mZXv3VKEMLMOfeKhALakKOAS4Rk_kv2ofv5EAbhOnJ0ASH6nYosg_7Es5jwDziJMusPAIIMTBvRUMQLh195YLk2PLwb2JbgNP_YERvsMSNWA5hBM0uQNbj7gOCCjI7WAVDka50uSNDtzJOAKcBYMvFWGhEXglb_YSbVShfEPmlybG678Vlus0PgNIXqKQS8CTwO09iupLI0uGxjgyuqhvOQhhgsgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=u9Ot49BNCDULrBY7Gw5Uk9Sd-glpX93jdP4XoQEAu_Z-RRgd0eFYUJZX4oz7YG6TJoPK9nptplxxybvZwf1bYZ34EhWvBdGrNwb-uHuycG-F9vyuZo9EsdKlveu9AdumQGLz3O5WJtmBI_UBTLxxL2wqnMURFNSSDuRvdEy8v7w1gq3bguDSnnGZFSdbpMEVnSUrBAoixbP4KXGBTbAunQQ07OGnXO2za9GUszjHCc0grT4JKyQnKo-7CCozk2e8EdFYSt2V_p3ADKI34PJrDUbHaJG0ieS8lYNFyn8tIHIZBS6VnCJcYq14ZtKwQxn4e93BPyJHjhYFoI6dyL968g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=u9Ot49BNCDULrBY7Gw5Uk9Sd-glpX93jdP4XoQEAu_Z-RRgd0eFYUJZX4oz7YG6TJoPK9nptplxxybvZwf1bYZ34EhWvBdGrNwb-uHuycG-F9vyuZo9EsdKlveu9AdumQGLz3O5WJtmBI_UBTLxxL2wqnMURFNSSDuRvdEy8v7w1gq3bguDSnnGZFSdbpMEVnSUrBAoixbP4KXGBTbAunQQ07OGnXO2za9GUszjHCc0grT4JKyQnKo-7CCozk2e8EdFYSt2V_p3ADKI34PJrDUbHaJG0ieS8lYNFyn8tIHIZBS6VnCJcYq14ZtKwQxn4e93BPyJHjhYFoI6dyL968g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luRBxPClHGFVu5lmprPbtIFy5M8bdhIGdjviEYI19Nx0jvJA8KnnP-evzBbt_eXDnCsp5uyRbFrJXrBRvyCQw7I4EQ_q7Yj5cvzcQtEtDBCX5yy-r1pY9Vu1da6_2m80sRF98TG0NyB5CVQOrVurC0BbminLJnI2AZYH5mhuYSA1a5cIv6zLF4TIeHyOotcHw2WwCjYFWXw_0z0_lHkqnqbt3rUKm07J4ffcYpaJ7fEE0W4AESqYqUOVEwHq4-FWbC5Ogz0zXD8UPt9efVp7shiUrjvS0OBLH-Y3AxcV_r2gfluTd_cDsv9DzEdrxO5YcKBYPwFL2_V7cWnlRhn3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=kPoO6CZ3sIf1ITa2QWKqbVBb0VYD5h7aN9pN37lpW51y_FV7xP0UYcCOXK43Rvv3V6sI0a0oUhHiUQTi0am4YNsXC4uDVhLRvLz9oD8z6Ii-BZlPno4cZTtiNY65JN0CViTsKyUutLpvIpNA4hbinl-bhkORmvjEzvGHrLJwF_sXyFnvQvga_Oaeam83-r6tCiom84ZGV5-vt0LMVxYwtZpGraMXh_hnmLwrwTMvI9OQsCNsJpT_jzdZMr9QtYWMOYYq96i3AX3C4WxdNI6iwgksEbrIKY4qm7WtE0FhzXH_l-NmY6LJQtVAU-qMsgegF8eAOvNXTEQBNBFEYqjc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=kPoO6CZ3sIf1ITa2QWKqbVBb0VYD5h7aN9pN37lpW51y_FV7xP0UYcCOXK43Rvv3V6sI0a0oUhHiUQTi0am4YNsXC4uDVhLRvLz9oD8z6Ii-BZlPno4cZTtiNY65JN0CViTsKyUutLpvIpNA4hbinl-bhkORmvjEzvGHrLJwF_sXyFnvQvga_Oaeam83-r6tCiom84ZGV5-vt0LMVxYwtZpGraMXh_hnmLwrwTMvI9OQsCNsJpT_jzdZMr9QtYWMOYYq96i3AX3C4WxdNI6iwgksEbrIKY4qm7WtE0FhzXH_l-NmY6LJQtVAU-qMsgegF8eAOvNXTEQBNBFEYqjc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvbcvgJYXFsmN1QWZkdILlQqsN6Z8wS0oeuCoLwNIi3-O3mgaeERgcadeN7AiXesjqL5w2Pe-FTCrzcZhxG0hKEl45Gk2mJBv2mYuMU_F8IvIh1wZWLJzoH60RZIc-6qlswkb9SzJf0a3KycafveQNZuYEWY7_HFFwolmxV6TEKs4wff7HAkhyYr5jR07QQreUTQyCkN1jOKqnlLkj9eARdzg1cBUZ1UKys2oI73bWWAf7KkLH3Nqgxr8EAFUbBIPtIAw-sSE_IHp-GUGlHHtRSooSNtmPTdh9GrCP8_B8KbFLyNr_UilL9QDUS_P-va4dP-g9HJ8qFBK4XsN3oeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwk4aIPqmeDd5YOsrZX4qcSXYl-byHVxonrevYuJbgciUkBc3xQo_S4R0iGVHsBnS0_R2P6XtJEXEMG7T94qczyH2GCg8N3CfBGZl4B6w-aNz4SSrI5-c5yPyp7SYQ9Avx3UfhS761bXfSSUOBT7kLUtSpbYY-jHP1cWYJraKt6Emj-m0E_J9x6tLOtIRxpz6Yh-Oj0ySFequDvvuO7gXts1SMCCfXfOXEJnXUwK7bnGlznLTUa-bcBckjKtESRga8UZSeENIwWeNrtbDbHXI2gpBILZms7gite61NRVOcsQ-ekYKGy-YAtvvm7Mn6iVsWFqp3g682ys4lt10UQctj70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwk4aIPqmeDd5YOsrZX4qcSXYl-byHVxonrevYuJbgciUkBc3xQo_S4R0iGVHsBnS0_R2P6XtJEXEMG7T94qczyH2GCg8N3CfBGZl4B6w-aNz4SSrI5-c5yPyp7SYQ9Avx3UfhS761bXfSSUOBT7kLUtSpbYY-jHP1cWYJraKt6Emj-m0E_J9x6tLOtIRxpz6Yh-Oj0ySFequDvvuO7gXts1SMCCfXfOXEJnXUwK7bnGlznLTUa-bcBckjKtESRga8UZSeENIwWeNrtbDbHXI2gpBILZms7gite61NRVOcsQ-ekYKGy-YAtvvm7Mn6iVsWFqp3g682ys4lt10UQctj70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=hANPul3UpQ-7gET5oBQdC0iHgINgqixE5hSOcgIZeOH4Vgtp4T-KBvFKxVUGhsjIQYKGHgUGaqOhoIOCVqxn94K-HIavp3nmJ3gq0TgKTlp0Md7i2wsWxOdijJCIuLmthsvh0O8iR-NU-s-i7E3_y12NLG_wZujRFnL62JmzY1PlDdm8uZDL-iaWRFqINe0_Iw25aiqKwXJMxwGIXFGqT7hUHVRq0nvl-Qq1QaOob_6r35i3HIN3Oxgtmmgfec-nIOPJa0CeyiAp5VxO8RRuVNk9bitUjg_DxXj93Y0ruFjmNJyRv7nLfejyMteWkGeN38MFLqViu1qnqxoAVQ97qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=hANPul3UpQ-7gET5oBQdC0iHgINgqixE5hSOcgIZeOH4Vgtp4T-KBvFKxVUGhsjIQYKGHgUGaqOhoIOCVqxn94K-HIavp3nmJ3gq0TgKTlp0Md7i2wsWxOdijJCIuLmthsvh0O8iR-NU-s-i7E3_y12NLG_wZujRFnL62JmzY1PlDdm8uZDL-iaWRFqINe0_Iw25aiqKwXJMxwGIXFGqT7hUHVRq0nvl-Qq1QaOob_6r35i3HIN3Oxgtmmgfec-nIOPJa0CeyiAp5VxO8RRuVNk9bitUjg_DxXj93Y0ruFjmNJyRv7nLfejyMteWkGeN38MFLqViu1qnqxoAVQ97qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRBsFQLGTo6RBULczoR1f7tJhrES1qe8kpAPDSSmAKvhDp6y5Hr46Zgt4KTXG6v7oRIkD_9hEK4TmO_OPIioFRau4ykWvYewc8IdBLXTN3TewdqSvFlImnRjnrBlYTH6x2nZo2VS0v5wbtmHzWZEaSgXFTUP4mcYzSK-kqMOdluDy4g0QCTSxBF8xGp8l4QmLuchzLolxvVHy7JeuyWuiIOF2TkdfwHGKIEWJyCVyhsvDcGPsFYDeBWrPJZySvXW2BYigscCjadTYt0iVxUTVVdegMKWfps4KX09DdFEwEe5Cj0XFedSpZ-qzF_lZFGTQZxcXvtRI7Kz_vBYyPypvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=e5xiYkBcpgoYDnXHI8xPIg0anOKhk8iGVv3uG0GTCBTl33M7OFeySC5xqngV0trLhj8jQhzaf2C7phydTYBOTkmv7HauJ64PVQNIpZPu7yYi2SORGw9Ldd1zu5yG_WZTvsWSBAGxbZrsPICje-Ma9zQca1eCSGqLK97PXICFG7i-n2g0zCo3bv_k3EipM27zGbxaOi4oYTdGpFasatrwuxq6iLvngSlWOvVIhLryJnxAnoGe3zzImGqAixDP79lpK9gg_ZdRJPygP16xG8-0M7uzG707NWc1wGVoQWtWGi5TRNdmUDAYpBbfVv0LYjB0LuC1vLjJOnne8mjBFTAOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=e5xiYkBcpgoYDnXHI8xPIg0anOKhk8iGVv3uG0GTCBTl33M7OFeySC5xqngV0trLhj8jQhzaf2C7phydTYBOTkmv7HauJ64PVQNIpZPu7yYi2SORGw9Ldd1zu5yG_WZTvsWSBAGxbZrsPICje-Ma9zQca1eCSGqLK97PXICFG7i-n2g0zCo3bv_k3EipM27zGbxaOi4oYTdGpFasatrwuxq6iLvngSlWOvVIhLryJnxAnoGe3zzImGqAixDP79lpK9gg_ZdRJPygP16xG8-0M7uzG707NWc1wGVoQWtWGi5TRNdmUDAYpBbfVv0LYjB0LuC1vLjJOnne8mjBFTAOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
