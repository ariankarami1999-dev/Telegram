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
<img src="https://cdn4.telesco.pe/file/vz7bcqj_oJXVCfvEPmgQELfxh4t-5QdLg4VcQ4emrlDbWIfuZX4Guzy3wnoZ2_qBKCdoJ_XkaEaiElq4d-lSZxiitRSNIJEZ1tNz9CCCyQy_MNbii1XfO9q4UbABREeYT0TbIijW_iEU8MZx75RiSFutgPju_glLE-2p-tFaDrdYg6q2eDk4bcCpsqcDdi63u_jnEabHngR_SWm3zLbgTJKoXHxT1WPSdglSu3O8Xt9cJRgcN78bGLCSfwKdrFc8ZSFHHs1tDviZB3M0EZ9gwbx3sGACeHw3SNJZ8WWic8CG1hX89q_7lKZO4oNihxEASCFf33Qq9koXB4y1C8xjpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 474K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSeMs_Mawl9Mr5gey_IG4wivpFVvfuRu6MN26PaQsCP6R13gF9SBuD9CuVUH8wvp0ExbXxcEGE_OOK0D_uJgFL5Kfossadc9lcEEfMpcm4UBtqWUpdaFFVwuaCMGPRQRVoWIAns4tV6OOFuEeWJXWROlNKqVuA3Bn4cQeK4hU2KkQDoGqX0RKkhCfK0ALFsp1FXxnwLKKgWVf6CzYT76i5JDUaWkF4eaItUaW0Yede5dv5-3k2jz3LBGPuE5ZPMOkIhudFvPINn5mk1AP3C99kohn2dsLGTPYZufvFTshLmwdFtPHnAJhOVgIZiIk7AMYS-dtkBkpNvD1sTEQTCd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP-00K8cnB2psuOSFbw_DRfGn6Ka69sCesmRVIKskyoFzVyC2V2Xs63AyJsG8BEc4KFBxxX7Ke-fcI-ox-GDR0ggHl9lHWzxW8GdoKQUCIsnZ2lOL8hIIYcSBgUOV54DA-cK5t2q5X2In6yJtr7lIcCnHL2QHBPhYcaM5kGH7svWwwwtJaMqJciHSa7xeiXVhheaycDDJC_F8zTBQ9bU1cAI-Fh-vj2VIdwgyEk9jFd0__0nMdKFlsPADfcU2QbyuSnCIv87w1iqJHESyG1nabt8rdiM-D8VhjO47b_zyAP9weoRJSszZLAv4q2GoQhB6jumUKnlwwl-e5iq1U2GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRTiEJ35JEBcsj8MUqMrB7vQ3SThqZC9R7qPloEbZn3zcWVhXrXaIC1Y8-RLLWf8dYQ8_5QDq7M-X_gQiwbpEQiYl7e7hnPcwwc9ECvuyVeuFvo0LsDI0t9Ns94ICXR8sSKWAfcOr32e6_vqhfph9Qwb_yWlnkzfyTWLwL-SpiojzBLftX31b8sKr8BCDN7gnNbximKQMNTymlLPl9-FK3iAVO2Bh_js6PvCoQ_Tk5ufTV5YRmDSsCN1yBZboNg4Sw0KFCaAiDDfXE9BzapZ7QKoZWDfpc3SV1YxFPTr508U6uy9aec0penKyhvotW8JfgjOUVx41nGRAxl-tFeKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8XailJz17Kn1tcIoeZ1Lkgel1CXWodhdM7n_VJCxaVDt2nHpDc0NcfODwhCC_eWPQQVUSNi1bA7rIuJFEtp6HfrDEkLRuToQu_SZqkbhKq2pfcyHX7NZ_NOvrLr_7YeCXwxzqGK_VHs04jncDmB_6TOjopnB52JCbYCPgAX2JjVMCuUvne6HWxjUQ3ZQktU0Lg4TUY_hwa0ejI6PgAay64Nv-7SCepHUgjCmRG0evDPpHvPJtiyERfBJMZVFk87zRcIQWCscSCswmWOYM_EnJma7UqlMbCl_bH7BLi0qHGGjK6mffn_Vw8n1PzMIUuq57t1IW3wzUCP7AYV8uRvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmDA6G0DiNYIj7ODdPeeKwmOZs-pU1kPF1S5J-qyKYHmm72QaD3NNtZdYfzvKKroQR7ch4QzdZwo1DKFL4QKCaEYKty-h35m3Noi4IIFEcnZn7pursDG58l7puQADK8QUqGEHsJkwTkjONkGgF_wH4CwvakMEUOZESwMUB84s2N562_uxTZ1iZv2bjpMjsKE3Q1m8t1y5cJulr3VwBvK7TC_cnByeCSzZe72Cb8tMby15GyJGNHjOg1BkyZbAFRBBxR0nB9oTRaDA3MJIoVYbRFjPl3xoegtsij_eAQYtf73W8tSflJo6j_hPMPTp5PyBPeYLWuxWahdbGM0pQJDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo3NW1zAU6SIAIrbJ3ZdQk7L0iNcy8rVV-5EkedDEOlptihPeGK_PwLSRPv0e9JJvn1FV4e4LxwyCWlKUMQLeVtZWVa1VwWW7I18YUkYoIz4uUrv1yAv1zd0rG60PNn5jmhaWeFYbcQg9SHX-KxOfoNsQH6uK884UuY8gcVta7XQmA9l1rd7MAI4ptyoydGhzQfUjDYlM_bjUcjfxDeWAnLSKKOJzmhImnwW4Rc_St7TSbZIhDeMEbwUCeWdaNS-6-Hg9b7hA_Fn1MIXdzJbIcnS6UVJqPhSLBCDXa5pV7KnzXQvmI2s4w9cqodL24p2PRq03uYx6NsAZDf84vD5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYkp8wy57oA_ON3oOEyTCExLKC4Un7teB-ZNrUv1Yph2QSmtaVJRTSjPft9veFD0pNbAtEdl3azNXmyv2G0JPC-Qui-moBFof4xIYFTkCv7cHtqC3PHvKM2L2qHWBUQYV4h9Oi1Hb2HAinF1rDMA2yDdqC0tKaXzYlTllhR6wLWsFa7dZ0MAsw7vdtDGRxtcdCKJ3AfhFYcdEn6xPUXjtxpF1gFgnlNMVBTM2Cs5Uu9TA-T3y_gZNimVQczAfnkZCj8WvlbceLbDS5P4OV5cYi6QUZEzTFzLTmlDWQ7dOxQcWIRssPXe1m_2kulwYuimql6wl3WJkTVL4Aw3ktNt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNdfOjKYituLo6ClcVYJMY0n782my03A7lO3Cby8KPcizTp-B6dN90iuG_omJ4jjjonn0qhcjVF_5MhFhrdPiEOh_4O4zRKmmBhBzCAIacZ4n7UNwaXOZYQYwWpl7Hr5yk4hfImpf-ZZLzjT5iiZ6-RZDP9wY2dIe3sje6l3_hk6U4aELtRxDxzwg94iYdWZQvGwyXpxbL5kj6ov4oocXLn9o_u4H9uT_wxiFGPIirekdccFeFrTHuGTjditcZvVOduhjji6QJKnpLvICKkkP9Z9ldlJwcnm5bYddO8_eTSQU_0KYBSLeATLI-lV_nKZSl1Q8uwGWuV9mvMiRrwyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnIJ7CMQYG5fWsk8wb1e8R3KIsvRsxW-GNbQBDRrd6rxLlN9jXfjtFeDEDNs8KsCjtBGf8bwrgarLZZQWFvLo0g0jwZg4df1YLxT6e1Sp5cKwLTznFUdslVZ1DyaXnVBOzaYMUJkhni8YaMf-tQUAp1XhxJ0XH0LF-yr7Y9ELxjPxJgASVL42qQH2xGmFf5HS9fE7OcRB2quCzxzMkV4vA--AxktxPzkiF4Uk-HHH-KVR3qDzUqLqknv_1feIgOY_LYBqQFGOhsOA7f7Tfh_AxV2M_sNr3EUNPaAYHz8CmeCYyfD5qwNR0EZPKTdFTmPPcwoyGrvzc9edAlsYGj9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7lUxaOXpMtT_Un95Io9xncQ4Rk_C5FAoZ0Xlm7P2SFcn3RdpkaAIzyVau-xFXDJC1iiGFAeqBv2iIAvlGNYNfy7gfYSlx8ZFTA-bMYOcdxrU9Kfp0khAVPE2rnQp5ZqJddfk2w-sdIyUAVDJjT9G72iMCRBdo9UMTz_LSwfRd7_lX5BzTNtOF_TOGn7iHfOCTGNFDw_u-1IFYEw5VPsrXXq0CCtZGKBI_12oKg9hWCR1qt3DyYSF4JxX25UkPIv5GZ9M1e9gYskny5cQPWSYwz2As0BhETOIQDY3QvHGpJjjWVN0KB-UVTBTN7AYiVgvLyJd6tCAiRSeBwZlSZRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo3jHxrA8jMiQjLzxzTyxL13He7kmRLuMd4Kcg8tyT61UWRwm2eCEu63igj0q7-3s-CtvLLL9siuNjkjMbXbbJYS6NjmPsqo-N8RxqLHNf59lPLy7lg3V5bSQdN4sbGuzex1fuX3FHqpsOip9Zda7wQHALGYYd_mGm3BmgZczPzQPuNCwX-08qbj4UT6SW5Q8LcP9hTnEI77Q4ntIcGFVO3u0ws-JNnhP1PEY9J9ARCoI9cozsf5ZMWjpEZDahAxOyU9ouAaMdqdQJZi-EO0ztiVpgh0lSTu91A9-SsMJIsNVNIrfMjCpDLNNLx9Spx2cLFLuj_zzVDXmqI--s2NcPsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo3jHxrA8jMiQjLzxzTyxL13He7kmRLuMd4Kcg8tyT61UWRwm2eCEu63igj0q7-3s-CtvLLL9siuNjkjMbXbbJYS6NjmPsqo-N8RxqLHNf59lPLy7lg3V5bSQdN4sbGuzex1fuX3FHqpsOip9Zda7wQHALGYYd_mGm3BmgZczPzQPuNCwX-08qbj4UT6SW5Q8LcP9hTnEI77Q4ntIcGFVO3u0ws-JNnhP1PEY9J9ARCoI9cozsf5ZMWjpEZDahAxOyU9ouAaMdqdQJZi-EO0ztiVpgh0lSTu91A9-SsMJIsNVNIrfMjCpDLNNLx9Spx2cLFLuj_zzVDXmqI--s2NcPsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3JuXZ6NgH_CK4f1-0Ja4q6uaHPlbKQt5BJO93comMqkvflDHUfTp5-s9XvyXBi7ERhdZpWwsPBWjQdwth8_IuknJsHX3ViZxDw92_ihhxzaNhHfiudnrTtnwSXAz4k3WCLlsTyk3vTKEBY16GV1FzJoWn9sNrPM1-987u-mBzNTU7EyGvgvqm4HZ4XKQdZs1oFSDa5z4QZq5rXVe753BnPueJVuv4zmWC1fQ6J9LwOO2cTDBIqOpkbPrI0y50h5R9qneIKYQFbgpMdcTbPjxgYU54z9VEVUGttEJKXR9EEhMX8audXQD6aiYfyoMucT_9l47iLq__hkKSWqFT2-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RksepAnSDg5I64l1LT3m6OR-6PZl49mAjNQwQP75PrXUZ-NDk2Cy3U_Es9xexEqtaWj-GQUzkuhTTF1hEwtHpivtxcg-P2vNYnxF0Oqz1z7Z3B6m0ajU9X4KUZkS6D66UeovZsV_ArwsNAw9ZQkqRyUU2VBRvXP6PpU4q5MRKZCRNy_uOuk29NeLCnKwcxzmfkDN9oVkg_7E1RjfLy8EH66GdiSlHBpRbgLhKKcVPARBW8CIZJSf_lYKFv9zfSoX1YPIsO33rV0IbcHYc_P_LdaQzs2MMkwyklCBDrvYmS8ra9M20usFYekokuQqmBL3Lk4Haz6We-xhbVGJrx66zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCsImGHvmJvaXvh3mrNAyq7z7ou9vfrZztFWTRzVrjSboKdwABh04P7V1pS6sBxai0CDdEF0zxM1XEJ614sJYPWHGfqKIswEQcq0tgtEh3aC-hiHtPM7cs7iIzhIdkx5J7COlLGIaHDb3BnaScrv8PJKEE3GseIMQMo9LBvID_tTLF1xkMP5lq_Gxpyt3JYBBRAHprIQdaZz-k100JwIN8Ne52tpzoRdQi4ngyUTQ2nd3h3yTjBcPJ0_yvGHEDXjuVwJgovhCiOIJBL-lkEj08iw2yYJ4q-K8a3NdzoMfVV8i3YCde5wudOcMTl3kN1SYQ78io_q_fTitFmmCK9c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boR49ptuGpLStuJgLQxrV3-T4YkLdLnOEtm1OiCG9sjooMnfENY_H_mPplMsaQ1QI4Y36fP-BUB6HDgX9vkAkkvB04IZ5vfLUMTxoQuvvVFG3sn4uONbPm-ejbvM9TMEDQDbdaIqksZf8QlZvowc1bFbRZ6PCg9Ytu2gwXNn6ZESeMWgFKwwCIOMmpv-g9kOet1z54LAbZeL8tzyy_s-X4us3L3l-KIJojc3Otv4AYDhu_xlkWuGoFjIVuAMFJnhzxnPTdm-2dH7CW7otNsNeMs92b4PNc5KMhdOpvS6y8irDefX-L0kx3OrE3hLviTyerGEFAwV4KlmF-AssL1meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
برنامه‌مسابقات‌این هفته رقابت‌های لیگ قهرمانان اروپا که قراره فرداشب و پس فرداشب برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/31481" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlM7dDgsV5C9C_O706z3Nz6zv2ATI9d5uZDWw91sIjta_6RLMRUT1NitRAWqhDHYYKz1xDricD-Lo9SoY-ezNQjAaWnw277Ach2iBjPaAdKCddJU7dpgdh1BMn1lCIakoQrUdZxydbghC5xaaIkrr-iIIxBxfooZr65TFonKDUiwLXuV_eDCW20kphOJy23I4So7NSvjl5WCGWNPxAHL8SEgBeWYqmUNk5IEa-d3KCCM4tzwSQLTtwdhfQZ-cRXNJmgXHI-TeVAYpF827z4jvmzSRqZZSxQBP-5TYO2kG3ZlopUcFvkd6QyEE6jZNnu8i3SbBQooHqRXlEyih-xHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
👤
سعید الهویی دستیار و همه‌کاره کادر فنی امیرقلعه‌نویی رسما گفت که مهدی قایدی بخاطر اون مصاحبه‌اش باامیرحسین قیاسی خط‌خورده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/31480" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScpGn8kr-_3kP6vkiQRPgnu82mKi-eTNCI33dA8gkfa9u60Vsz0yzQm9xoqmFiAMVVf-wc99-P23HHBsDrV-hXTAblUM1DCNXoz-HG2JhB00w0BwquIkk2Fqula4gkSkItu_-HrXb79ijQAJWTcCWgdLrSNPGtSrOsU94tcFRo5n6CgokqsheomptdnqQKSgsBUTgNLLnSTT5QChC3WWbqNIPeioG2xm0IfVyFRyfpKnrVu7qHazRVAybNP8hmTWPhqjbunoTDNNjCmdspE3uQrLbCQOf_DxlIKU_OU4vlYL5qrzbrDWn4cQROB-E80_eNzjpuKW-2shqMYBCJ7jgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته نهم و دهم رقابت های لیگ برتر که قراره از شنبه 25 مهرماه استارت بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31479" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjIDnhSZvRSguR4gVmiG_hJDfDW7sTVB3Iu15LlaCFnKIO_f7yct5GPC8rRh6KApK_YBD-WtuQl7b34y9DOAjxcH13867S40a8pP1LcCtnDoF1Ehhoo49tRiHXrcuxsqN8C4fsRPZWZiSZl7WsLwisQeH2UJar5Z0goWr6Fa7LZ79XIiICbHdoq1wW4h5Rw22wvpfe9G4bGNC-fZWsaXR7tnftrMBCIJ_onz_t0Mx_F9i6zoRcI8jd3EoSLNnmV2rdacSJ-wH_86QcYVlHuCVwFmVgksEmzjZTZfOyAttBIGUAwyOqfw-MZUZBSbLJkoTEp-NasV9cnBO_NRURvU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/31478" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=pV46ESmTftQtUGPzofPeFOz6oFCD1iqhpNomKU9R1jXs4SuWvZKtlFYRdfWrJxO4E_q3J24Dpq0QtTdVvxFBFLQh1M7gDozokkAcR6w8yYNaxFy1WRQs4X8Yt1oXM0Thgl5Mna5UqT299Hx5jSpWVLSxoIKFRHmYqUGAZx0kFPrwbINUTbRYTjysDRoyU_CHM_xgaDKxh6t8VXi6veeSifdgs4EEXq0SHg1KX_mK76f09mEcaqkfPM3VigCICpAvCA5NSLE5vtVKEb4o6ir9Mdfo2BTEpPKlfPcOKlic60U827WfO3S0nt9Xe6SBUOwAJ2aIzwoL14VCdy4nIiUFow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=pV46ESmTftQtUGPzofPeFOz6oFCD1iqhpNomKU9R1jXs4SuWvZKtlFYRdfWrJxO4E_q3J24Dpq0QtTdVvxFBFLQh1M7gDozokkAcR6w8yYNaxFy1WRQs4X8Yt1oXM0Thgl5Mna5UqT299Hx5jSpWVLSxoIKFRHmYqUGAZx0kFPrwbINUTbRYTjysDRoyU_CHM_xgaDKxh6t8VXi6veeSifdgs4EEXq0SHg1KX_mK76f09mEcaqkfPM3VigCICpAvCA5NSLE5vtVKEb4o6ir9Mdfo2BTEpPKlfPcOKlic60U827WfO3S0nt9Xe6SBUOwAJ2aIzwoL14VCdy4nIiUFow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دستور محمدرضا زنوزی مالک تراکتور به حجت کریمی: قرارداد علیرضا بیرانوند روفسخ کن. او دیگر به هیچ عنوان جایگاهی در تراکتور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/31477" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=m8LJr5Jrto3hTc-lHMc6btKP8ZA4Io7e3Co-Ze3Mc0-IPqRYLXE8u6eY4jlu-2HgQ7wKISESD6DFI4hAI736l1IrxBoaJcjlTd0o1b4YjYGD95U0Hilw1P3mgSrffouvBcsXbQxvO4MRFIqpO4Vtjt4md4_l73BVtcwF4BgAjTxBBF2Shub5Noy3HJq8jhNfIhjvkXcAC5Dfmsf6ATDzHOJDxeBsgMd-XOOw8D0lLu2QUL0aokQBL1_IxGL3hLhjZjEh4V_IF94gVf9kmOHBlh15mQcbDyWww9mxSDp1I_DOq5RHgombnBYHmWOmthiee0WTj8ZisnugA2lXvB0AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=m8LJr5Jrto3hTc-lHMc6btKP8ZA4Io7e3Co-Ze3Mc0-IPqRYLXE8u6eY4jlu-2HgQ7wKISESD6DFI4hAI736l1IrxBoaJcjlTd0o1b4YjYGD95U0Hilw1P3mgSrffouvBcsXbQxvO4MRFIqpO4Vtjt4md4_l73BVtcwF4BgAjTxBBF2Shub5Noy3HJq8jhNfIhjvkXcAC5Dfmsf6ATDzHOJDxeBsgMd-XOOw8D0lLu2QUL0aokQBL1_IxGL3hLhjZjEh4V_IF94gVf9kmOHBlh15mQcbDyWww9mxSDp1I_DOq5RHgombnBYHmWOmthiee0WTj8ZisnugA2lXvB0AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش حامد لک به صحبت‌های بیرانوند علیه علی دایی: طوری می‌گوید در نوجوانی کارگری کرده که انگارهمه‌فوتبالیست‌های‌ایران در خانواده میلیاردر متولد شده‌اند. ببند دهنت رو بابا. حرف نزن تو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/31476" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=Yd6SY4suJ3CuACI_oGhXKR_mCCagBxZN9ORiwYVJ7-3v6WMLJ_d8fyZTZanOxrj0UMhdWwZ2hUVxiPRLG5npjrefIhkzCQ3tXQzsnhQiQuIA73wwwBSAc5kb-ojzN8y71IFuqV6V-gCttiMw4zSUfOInNu678j-Akdisx2Ib0W3tacjfz9HDgMnK3PX0slOI7Ik7jTN4hvLricE8t5Tr3Tjf1ROUnJdsclkUCrid5Er796uyDTl1gwtlUnKheuDcMLB_HyBuylOcGvbYFuqSXtK80aePI1xNPx2dtgVliU12M2Ie2T6THikBs6YGCxB6hINX8OMy4U9a4GTds6yzLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=Yd6SY4suJ3CuACI_oGhXKR_mCCagBxZN9ORiwYVJ7-3v6WMLJ_d8fyZTZanOxrj0UMhdWwZ2hUVxiPRLG5npjrefIhkzCQ3tXQzsnhQiQuIA73wwwBSAc5kb-ojzN8y71IFuqV6V-gCttiMw4zSUfOInNu678j-Akdisx2Ib0W3tacjfz9HDgMnK3PX0slOI7Ik7jTN4hvLricE8t5Tr3Tjf1ROUnJdsclkUCrid5Er796uyDTl1gwtlUnKheuDcMLB_HyBuylOcGvbYFuqSXtK80aePI1xNPx2dtgVliU12M2Ie2T6THikBs6YGCxB6hINX8OMy4U9a4GTds6yzLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دیدنی‌کریس‌رونالدو در بازی شب گذشته النصر مقابل نفتچی از زاویه‌ای متفاوت؛ CR7 بدون نگاه به دروازه حریف توپ رو وارد دروازه کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31475" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFknW5kySECJz4URdwXUNB3DLQQ5TJplnPL7PVMocNbx652HIPgOTksOyzc82pt0t8K6tzfiVmnG0i6TpJ3PswafAAeJx5WW-E4FgxDnD0evakOizmNfwUUoAyhP8VPeGX5P2zdPEjCaSVcVAkGyRt3JVf5bJfuS6dE2kipmS2QIDa2dZP2-kG7U8z28L1_GsLvWDAdSrUm1YoC6e1WAsvnQXjT0LefWg0C4m6gNW77eiWsFGiPhDz8iUe0Jcnr74tAWwNE7bJOEVuoKDEf0vyb3OkhmcJ2UhmKqExtoyOy2m76NhmTlK_GnOL181K8-CpsdLJwU1TDU8SE9n3AQHcBxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFknW5kySECJz4URdwXUNB3DLQQ5TJplnPL7PVMocNbx652HIPgOTksOyzc82pt0t8K6tzfiVmnG0i6TpJ3PswafAAeJx5WW-E4FgxDnD0evakOizmNfwUUoAyhP8VPeGX5P2zdPEjCaSVcVAkGyRt3JVf5bJfuS6dE2kipmS2QIDa2dZP2-kG7U8z28L1_GsLvWDAdSrUm1YoC6e1WAsvnQXjT0LefWg0C4m6gNW77eiWsFGiPhDz8iUe0Jcnr74tAWwNE7bJOEVuoKDEf0vyb3OkhmcJ2UhmKqExtoyOy2m76NhmTlK_GnOL181K8-CpsdLJwU1TDU8SE9n3AQHcBxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDeT6wwEc4tDtOa5oMqXasnAVg8rItE7MazqKF_qMBxl1diA33wQzM0_J2Kr8OuRxc686E2oLlxLiyuA5bBC4wPR2I_HfF4br9rSzijBNZkTvwaus4SKsQEDB5ua2OavLGyg10TXt05HlnCj_WgPL1RbZH9D7z3naDhq46R5PDb6YGSlb_V0m9o9_kn4NyH4-17pnCAEpI6zwJJVZdc_pxb86Rt_B39qU8uTF1DsP8LqSTmLwKdMOn4vqBVjtssFNA7s-xUn4oL7FG3qbvS7zGznzdN-zMyJZ4HVfywPbS9zUE0sn4mcYgNK3kUqMOOq-GF55X54JT6dytKeNk1pnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5UEuy2wCLtSXzguO6T9o_C9IAs-LzuBdy2OaWT9b5KcOAZ4a-89OdKk1XwzMNCBqdzU_f3LOkQWdU5KFt7uS7pWY-Zl8eAhbYIt6bLgVVUTx4lHlzqO_1A48MNAjhJjBSlZd8goHGipuL3NfaDRB5X2ZheWO5hbiHTTGxBDUuP6y42Q08HEwJPKoKALuh3-GhFq7IViYCuH7qJqEaQ0WnlHX5Jm8fTu7-BOfgGeD8vPT5-RaT0ffc30tLLU2db6t7pZq9F716wT50Mb1_sx2IJLUzdgg1gK-r1cJPBHmubVxMMT3SeWVUMxycLQWhYk5CU2wrTOgX4w622TAl0Wlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_5-EmrlnwQPFai0qH7MLt0ywoO8rWCgAQjOmQ2xxtzVF49gX9KyE9Bwe0fabvi-ggh1bx-k1FvHmM5WTaCCJ8mX9Po9imNhOa_RCtsclvYyUA3oLNq0OwEtHx11KYimTX6hX_DcARwlSwNs0bvPb-nNtma2LbtK05CzhBsqjZMNUSRCTlxayIoY0gKw68ScyxTVHriXex_R_exgLsxeOAv27vi3MK2j_qVuy3RVHKcWRbKUJNfd-CgmpchYtNJzAFgcQ4tZp2vBHol-nPAoXBFdPJuAvIby8T5pWw8B8MIEhQDgj7ifUe1hraZHhzqeTlWKSbcM1F0HuZJpotN5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fncymc6f0AMP8LavY84Dbxauup_dSwqWJcRzOqBU6XrURoXvEqU2L_qNWHh8gpzMInRBk8edU3J7hOC3AzZZrIBqhpFhxPg7LRwhcZqfcYn9fHlX9gX6n734cguuMFisAleGXKfr96DvazP2ynen5nvGRkVZxemZWuRLPItEGfWUG-F66l7gQL-V9i6-WmDuRd-b9b8TZKEpCRrqtlowbT3FAiC3b8b_jBcX8UF7KqZd6YOfbpiRa2EWE0zGHdU3untTlkfCz-XFXxwompq8FhN7ixJUnwdAnpjTr5kj3M8gZ3lPkHYd4R08OnaMGvrkqw_SI7OkzNbRI0W4Vz0P8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqJ8Ni3dqLXMhgDAjdbdn0MoWjzWFikAmGRxE4rQG9x8j4NQK3YceNWfqdLVzkkjM06i5UCIgRja2GeR8X42KulU0VghFMryX2DTEmOo-8dCVuOHxPmnhxhB7mP8eaEH-mk7Rx2VOeBOV9ew3rnZOLvnDehih5iiGZ0G7heqn0gibotXLVZBs3Jd7f8HwKZwI9jg9W9PospK27ETLF-0QBAe1IPitIM3cprC3uJl_R-Hh6VV3qcInbyS8RRDs-ETdn1iNdZ5KVGKIKWIT6og97DvGUILmbBlhrOXYuIZ9ld6dqJyc1KN7FuiYsk_7IkFeguW6BvMeCdCuwp2AQFgbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_rqqIBEmPB1qS2G4V1UPYihvLRfv4FyGYXFbpAPiQ7TAsticDVeOnxfoc-FDs1i-tuj1UCsYfF2VIpxgL2lVZ-MmU88Qf6hnda2hz2Cx-RckxnGWWuFLX2fOh5LKXSC_J9OXRkObSfFpfym9wMNk6qOd-bU4oXamr8LdmwYWmLq-oZ8tuEaNObAcskElckATUFHT9x_U2tZGnb1nSUCEKCQ3m5P0tK_9xHMXfYQtwCGHcAHdtLaNFbmfxoyFyYGsTf4uJkFfFlkfWp3mzLp-uuJw_gqABBeFUIf_lyQe0tiNpEHnwrutWbD9umQEJ9mFft_W2HM1T0Qsx6MFhVK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkyMAMadrwbPvHj5HsMs7LPszzwGwX0ZrJvRCBf6n3oPFXLep4Op1-jwW5cq__pEB9h_DsrfbX9v0HXlAsPW0I_HffUvsLSkc6SMo6RPC4udH5XizGdMQDU_FggTbqJVamqC4xItwnwLZJYS_SPE30uwlaORmZtosDFKfZpiGSxRc5LVLI8dtrjDMLrbx_jh5Zf1NgNGlcdUlEHpmBXHwObEd1bt7LYqZtyavqKP2MaofWlueho7r7QkCmsI1yyKb-ZgRvxJmc1YeZgBdGqmTEWxleWWQ11sFZozQUoBI2VDxNrZfpn8Ns4RvvEXMMdZ6KNcemEii0TVVImMUq7QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP0XGk4V0yM4_QOVLMYme3ZuK9LbGVrfu3_qCuYa9shifppHPGR8RVzRt6mKplszlH5YhQTTbw77Wi9p6finfUiTRyRFr_2CtdTuGCgqVoQqgjO2CWaoU6W8F1xvf6gbh_6aY3oRnel9Io3AoBFmuIMw2jirUfwPNEUpl1ZxCPr4fmc2VQph7xHQCZUdf4Ta0zJis8S4cGA0ilCwYJLL-GMcsRIgFPwlWidllkq_7YlD8lE64jHLwZ1Y38bxIwekGsCQ9LORYffOf00lgWAMwjFKsKDFYZg8p01B816CI8QuPk_awzBbWD9x6QD6zTq3OmjvrfWCS1dp0cuT5mAuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=UAxV_P1-6yBosh7XxrPW8Zsse0cx5E268W7N578Px39MsEDrWEiVscJdYCJOLrQe6VV4K-9ULtWF8L-ympj4nz4AjMo2JyLhq1OOUIs8LS4tuK2jMdQc7OKOTjJxAWqM1ca65dksau0-qsD6BhwcrDo6hCx8qEYzZ2Bv0UcjNAzS4AnCHRf_Q76eP-UjgKHN84D2uv_im6Wb4cGEByn-nwJ9V-NI0mksjjagn08IAzmzwwVfibMyyEsifCaQz5zU7u3EC8Wy9imGJUdRQ07WdKPnBAb1ZgAVFejGL0jJgrRjGQmbBxdT00v-rIkxZZCdnuBn7v2UI4B41nFUDR1Atw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=UAxV_P1-6yBosh7XxrPW8Zsse0cx5E268W7N578Px39MsEDrWEiVscJdYCJOLrQe6VV4K-9ULtWF8L-ympj4nz4AjMo2JyLhq1OOUIs8LS4tuK2jMdQc7OKOTjJxAWqM1ca65dksau0-qsD6BhwcrDo6hCx8qEYzZ2Bv0UcjNAzS4AnCHRf_Q76eP-UjgKHN84D2uv_im6Wb4cGEByn-nwJ9V-NI0mksjjagn08IAzmzwwVfibMyyEsifCaQz5zU7u3EC8Wy9imGJUdRQ07WdKPnBAb1ZgAVFejGL0jJgrRjGQmbBxdT00v-rIkxZZCdnuBn7v2UI4B41nFUDR1Atw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش از بازی با گالاسرای در UCL
؛ یکی از خبرنگاران درباره‌وضعیت‌فعلی رئال از هانسی فلیک سوال پرسید که اون‌هم‌عصبی‌شد و گفت امیدوارم بالاخره یه روزی یاد بگیری از این سوالات نپرسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31461" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3vWpnrGNizeXAzdaskFKbo2H4T1SRnJnBpS0ZmErS4N1FErppUqEU7KGwFdU3y8OnvQgBmWgtEhl-smpb9LzWZdf6mSQOC2OFkNdZRil3tEWG5qCsQhfZU5qrS_WEn40X3ndJ8pPHDtS9X3VqugGHSXB6YmUephOv100H0jZQON5DmGaILQxGz3InoQ5SiZo6l1feaEs8HSgvp7AzYdNxdOkpsGFkIXPEdILPmsqiMMjc5MWaxJ-kkxZy0KnHkkHrL2b32LMiSd-RqjfEhEhFUYGrBrw-JcMW8e0T_lVB1XveVF1H4x49BDqq92J6ySXR7FVi74zs3s3noY6lOaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31460" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9B40QN9-mAkXlXIG1vW9dk8oit68-LAkiGatp3vaZOk_xEX2M6FGYmTCTpoCIRAKI82QvqQmfqnhXrOyNPr2Do_BrlzUTP9HbLzSlXW51GdRAPKV_zHyBeN5YJgzo49sGxIwJrdkVtbIq86lukj1wZG2mHO9tLGl3AX-M03SU7BTnrY6vC14uZWq-LTFWMYCHa5QBcAjQa4b_mAq3AtZHQllZyV2Y9YLXQVe-vMblX-0p01WAFvUom_vnrV3M-IgBkmeR18e4VKbNWWwWE9h04UhCSONz6VqXkJ_S8pW7O7qYLqyRJNLBoDZhHb4D9308zvNoftDgGtw1xdF7nL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31459" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBMiN4Foz4_9t2JdYJpvPirV_j46aUh41YyFowr6EUibva7Cgb4RKh-PZVtDPyBUTTm71fOTEA5dNlAoW_kJQnPyyXICZSg_TlqyV2_4zvPXG5z_7j5Tl5FR79NGCXKpQUUX9qR-kUL8hH7-YWtmLKWJp-ObrHV036bS8i4gq4OCeL-f7pHfxxDTwKxzldCpiGpHNQ4AylfCSD4mN6mJYQmqNbyZq0_Egogk2Kl4tWHtfeDNHOo2vXHfFdk-Z5EtUK8hNka1-phwJkNczF66wx46sm1OZzCO82MZTANo8b1StpJ1rhQbAnJAXPiGGu0P6OVFxeFtB2gEALkICUEQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31458" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57855f950d.mp4?token=ErvQHzH-L4K0erIcJvfqkORsHb1lykd4S2e5qiWfdTPKHivPyPL2zaL6DBJFo7vzmGqZRgjIihnYnHGkbbR7HmqarJ_kPTbLpXVVg0ZylWb-YqK4DluVDYDBFUUD250i4UR_2zoxDYqirDXCosp5Yz6uTITBJSPL0Dw-RPFfGhJfIr106K2FFdOA7XKU27_gx3NhKnhSkWIhnItytKyaolbSjzhf4_nUK8q0hdw_fLYSVlcv1hghhnZ8P8KpRkSU0D_5WbNAQYV8hCJyqDKl7LEXzN4rfy9D4NLEETzdzmdYXKEmZ6mUEM3NRYOzcNRv9NypDM0rx_EieIK0nLoB4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57855f950d.mp4?token=ErvQHzH-L4K0erIcJvfqkORsHb1lykd4S2e5qiWfdTPKHivPyPL2zaL6DBJFo7vzmGqZRgjIihnYnHGkbbR7HmqarJ_kPTbLpXVVg0ZylWb-YqK4DluVDYDBFUUD250i4UR_2zoxDYqirDXCosp5Yz6uTITBJSPL0Dw-RPFfGhJfIr106K2FFdOA7XKU27_gx3NhKnhSkWIhnItytKyaolbSjzhf4_nUK8q0hdw_fLYSVlcv1hghhnZ8P8KpRkSU0D_5WbNAQYV8hCJyqDKl7LEXzN4rfy9D4NLEETzdzmdYXKEmZ6mUEM3NRYOzcNRv9NypDM0rx_EieIK0nLoB4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/31457" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di_QXqgEhmTEK7-TOf9-b0FVDHzxFRzDlNsGFws5yUXMC8mW7Wg1NK6KD-0Icq-T2WpTsKfq4bl2HR_Gh9RWjY1VoQ-So5qvYdtfnVu1zym3C8K_ViStjpnetlILrhVe-zbyH8XZvf7fmRLbt3HvhS0l3-27LZ2oK1zBLk3cYFa2zBikZ5GqJ43L1obwNm_vSbuo1JtFIp6dBg1x2MU7lZEW-atdBbUeNAISIZInMVqS25UBEsS5AN5HYwCjeprvRzFFqXyMdtl5RJvjZuNOfeL5Hvo8g-6AY16bIGVBYXcwzWymyt5hpIRHSjZIZwU2wSoYyRVFd1wvsv-9VjSEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حوثی های یمن: بزودی تمومه ستاره های فوتبال از عربستان خارج میشن. کار میکنیم که عربستان نتونه هیچ‌فوتبالی‌رو درخاکش برگزار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31456" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=cgkpmXf1FcIufJnwzBwGdk-w0B2Q3L8yZBxm9lOTxWUcgJGpa-ZpOEqukMKE5BL63GEJhbLfujPBV8RbqtM0js1oLL8YalkXLCskNqNq8ED21iek8DIDI-L9sbrlvreChGeo16raoMU4SJ3MC7zbKJaSqZlGSRfyK5u5qWLoagioRmb-H0Ic1I4NZ1bCiaL1vtLNvZ6nICsAIfRchtAz2LGIGKc-TRhC5r4I2XZ1PJP09UW9QJYUQA1K8h0ua89VQ_pkaq8tZvw_081_D4OKT3FG15JJQpk72hLnNzOg9yYYSYlz8ZsJ8bZrz6EWkAVpZdgziO3zOQfA4fXhI3GZXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=cgkpmXf1FcIufJnwzBwGdk-w0B2Q3L8yZBxm9lOTxWUcgJGpa-ZpOEqukMKE5BL63GEJhbLfujPBV8RbqtM0js1oLL8YalkXLCskNqNq8ED21iek8DIDI-L9sbrlvreChGeo16raoMU4SJ3MC7zbKJaSqZlGSRfyK5u5qWLoagioRmb-H0Ic1I4NZ1bCiaL1vtLNvZ6nICsAIfRchtAz2LGIGKc-TRhC5r4I2XZ1PJP09UW9QJYUQA1K8h0ua89VQ_pkaq8tZvw_081_D4OKT3FG15JJQpk72hLnNzOg9yYYSYlz8ZsJ8bZrz6EWkAVpZdgziO3zOQfA4fXhI3GZXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
قطری‌ها خیلی زود دومیم خوردند؛ گل دوم استقلال به الغرافه توسط گودرزی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31455" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=p7PprvVaKKqiKjNCznIXbjtlkpOPZHIKzMfSX2VupcAyQknoE_osWZ2yRg3FtFgN7v1Ov2xeiln7RYR8xeJz6ta2zWrk7N1_l0cfYXXFPmfP6izwiW1tN0bHjU7ouK4xPLwj3k9KgUS8rEL-V7owLmo6HuLh-UwzHXOoE3b6Ejud3EaZvfYexh6lEPEMCZtG8NU8lAH_S2pP1uren6Dxg8Fusj5K9Sz7XJqxQw5mUD8FmtrfSa-4pJoNrs4jF_0dNO8ZJc5Dhi65f_MkxkiB_tzggGPdy5kBNrxgSXu9lZmalEt3TTPRpfpGdjoVCe5UubJ33kNO55LRqiJXGngLhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=p7PprvVaKKqiKjNCznIXbjtlkpOPZHIKzMfSX2VupcAyQknoE_osWZ2yRg3FtFgN7v1Ov2xeiln7RYR8xeJz6ta2zWrk7N1_l0cfYXXFPmfP6izwiW1tN0bHjU7ouK4xPLwj3k9KgUS8rEL-V7owLmo6HuLh-UwzHXOoE3b6Ejud3EaZvfYexh6lEPEMCZtG8NU8lAH_S2pP1uren6Dxg8Fusj5K9Sz7XJqxQw5mUD8FmtrfSa-4pJoNrs4jF_0dNO8ZJc5Dhi65f_MkxkiB_tzggGPdy5kBNrxgSXu9lZmalEt3TTPRpfpGdjoVCe5UubJ33kNO55LRqiJXGngLhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آبی‌ها گل مساوی رو از قطری‌ها دریافت کردند؛ گل اول‌الغرافه به استقلال توسط فرجانی ساسی 48
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31454" target="_blank">📅 23:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=qsIb2hVhZGliXog80zx9yyq4n3Ogxs2OR2URjSiTKx-gONEF_Qcn-jOyn4m31E3q0_Ov1_jb9wBJFUve_Whaodnrdq7DL2EKKLfPiAZLvGWwgLOZotYZOXbp3F6Hvph2UU6K436OWsy1SI4E6T3Kwt_2KoXaKlBQaVXLjef29qfSi4mumgojiwh3ze-Io8SjmoTx0PKhTEDMzYBbP5cgp90vqjNZ3krJt6eZihx-hGmUWEaEHuiPAIcbO_9VWE64LonFAUMTiByw-VSzMMrP4fJiWgDDXpl-5GxxV_LJw_-oW21mTNiDdciOj8SpjeBFrZ1O9Jah10VAAmdsKA5Q6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=qsIb2hVhZGliXog80zx9yyq4n3Ogxs2OR2URjSiTKx-gONEF_Qcn-jOyn4m31E3q0_Ov1_jb9wBJFUve_Whaodnrdq7DL2EKKLfPiAZLvGWwgLOZotYZOXbp3F6Hvph2UU6K436OWsy1SI4E6T3Kwt_2KoXaKlBQaVXLjef29qfSi4mumgojiwh3ze-Io8SjmoTx0PKhTEDMzYBbP5cgp90vqjNZ3krJt6eZihx-hGmUWEaEHuiPAIcbO_9VWE64LonFAUMTiByw-VSzMMrP4fJiWgDDXpl-5GxxV_LJw_-oW21mTNiDdciOj8SpjeBFrZ1O9Jah10VAAmdsKA5Q6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31453" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDFD7HXMgARRAnfVPjC0OUNWpYTc7XCVXHhBN9lg0OQzsLd9fnU7sq6ReWcDpoqFOOUi7ZWLVIxaToeJwJANNU_AP930MB-DBTpB5NvTzYR73H_FetqgLYnqMKDwvWAPO7Ap_7MttHv4DTidUVIYq7-7MS2RojgIQrQ5re4oLiA0QxB7VE3-WXEqzJQriM0LYUMFTbhEB9kuzqAd4qZEhXIrd45uukqSAcRF1gEw-jY4Uebc9ZT2cMX6hj_mNSASuW0m2Ey5L9jzs2PYJnOrp5FY9vKq9-yY9SSaN8TvBgPz-KBTQEClnSC8TRs3ukY_4Ld4uBVL9eau2yTEGjzU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31452" target="_blank">📅 22:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qizhE29UI-bhwxlFLXbGh3NtGvg0yJEj95ZDUfCDXOKbL1g-JDTGSJGUjo84k7JDWF0o4rvlFkL0bNC3sd31wHxSPXVIBj2NM-XfJwephd02PRtvmUssfF5dmolLtL6NLl5w4vO2EKia4HBLs6mohcC96N4xc5i7Aa6BEng3E9UM4uwaKUviMplsbYM2g7VR7HCpqaktsVTtdNXhsYN7Ca8m9C-Oe4A0TVW1a7Ro8aeCoLnL5xwPx6UXoYczMPTAyqRI4NRjga-h_bsuuyWcgEmJcRA9eo1m_5e4azFwoA7xGic1yS1YY0apBC5wcR1iBbxBl4gI1rQZOophKZSbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌امشب النصر درلیگ‌نخبگان‌بخاطر هشدار امنیتی و احتمال حمله‌حوثی‌های‌یمن‌تاخیر خورد. عربستان با این‌وضع 3 ماه‌دیگه‌میخواد جام ملتها رومیزبانی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31451" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔵
👤
سوپرگل پشم ریزون فوق ستاره آلبانیایی تیم استقلال بلافاصله بعد از اومدن به زمین بازی؛ گل اول استقلال به الغرافه توسط یاسر آسانی در دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31450" target="_blank">📅 22:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31449">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=dGQSyMI6pRS_oPaKQhksul90z8RB1-zhzM4lm6NtySqs3LpfAduHXbruSlrWLxfKXc-uEXxBzZAxS4HdIwVQ5liiQefsmCdBg3PsZhFvEprRJCdn62D5nKRUIIa5s9TmSLPTYhTzPN6jJAemtcR7gQ9TftcSkhhr8Kr21ZVqiLNUjlggXmXtoIC-IWLCHBhW-rhhov0Y_mdnRb76boycOUqyXBiQK6W6LU82mf4DthafbZ_4hBhLmirj9tA7-KVS_xsVJM3Qg4rtrS3l_zcqdhAlPKnJt799HJ6y_qjT2ntzqTVde4-WDcAJmtjmE2WtKHbUsUp4uoxWdft6K6h5tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=dGQSyMI6pRS_oPaKQhksul90z8RB1-zhzM4lm6NtySqs3LpfAduHXbruSlrWLxfKXc-uEXxBzZAxS4HdIwVQ5liiQefsmCdBg3PsZhFvEprRJCdn62D5nKRUIIa5s9TmSLPTYhTzPN6jJAemtcR7gQ9TftcSkhhr8Kr21ZVqiLNUjlggXmXtoIC-IWLCHBhW-rhhov0Y_mdnRb76boycOUqyXBiQK6W6LU82mf4DthafbZ_4hBhLmirj9tA7-KVS_xsVJM3Qg4rtrS3l_zcqdhAlPKnJt799HJ6y_qjT2ntzqTVde4-WDcAJmtjmE2WtKHbUsUp4uoxWdft6K6h5tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک ترکیب استقلال برای دیدار حساس امشب مقابل الغرافه قطر در هفته دوم لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=OYxx_JFqVLDJLqnCZyn1GcH8tj65tuQsoBaTT3WaqrDaJmBhe41cT1qY1j2ylMitar4WqDmQReKItLuuRLq2pwIDHkpQFllb3NvkNDm0quzPr8vBn6ozcGP5IX64ZCCeD7q7_vPiORbs6PI58cKLqu0THWHoU_5j3JxGkiV-F1bQu2Ar229VIgqoLAwhQipuyFePy_X0WLc97x_DRTOGwRKtQbYoGkx3eEhicyGVEJyvAWYppo9jH9YUFPXQ6JCvM02aHw_nCEVP_okJXYTn2b6Y2JeHWcGHdDv_lRAJwv8jfD3Umo2PVg04DCxEr6g0Fce--IQIqVSRAMmyicuwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=OYxx_JFqVLDJLqnCZyn1GcH8tj65tuQsoBaTT3WaqrDaJmBhe41cT1qY1j2ylMitar4WqDmQReKItLuuRLq2pwIDHkpQFllb3NvkNDm0quzPr8vBn6ozcGP5IX64ZCCeD7q7_vPiORbs6PI58cKLqu0THWHoU_5j3JxGkiV-F1bQu2Ar229VIgqoLAwhQipuyFePy_X0WLc97x_DRTOGwRKtQbYoGkx3eEhicyGVEJyvAWYppo9jH9YUFPXQ6JCvM02aHw_nCEVP_okJXYTn2b6Y2JeHWcGHdDv_lRAJwv8jfD3Umo2PVg04DCxEr6g0Fce--IQIqVSRAMmyicuwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31448" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=LJZvQWMC10kIt4NOTv9yFvMT2ZFwLTQpHMR1ewJUYc_BFQ-t6zIy9a6gqfgh8_7nmb80bdU9TQI9B2888P3nQucibMNDfo_9n-hrNQiDo3vEGsIhK-uK9LJ0OZtZLvHRaM1Cp6dgzhNMCVNGlj2gQ9LVKoZoBT13GWwTnL_CohN3pxwDIbmmYfivYWfSlEyXHwiYKtRL4cvypPN0j2swYehWrx-F5aNthMl5egV42Vqcyp2cVyDYn2V4IJpnUt6TsZqd4D5AV3PrlhUKEp-W4MghiGGJxgPw0SoML-nPEOyRBaGE-WQRYRoaK5lQHSR4pUB9XNxrRj9Rs_ZVxb7ckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=LJZvQWMC10kIt4NOTv9yFvMT2ZFwLTQpHMR1ewJUYc_BFQ-t6zIy9a6gqfgh8_7nmb80bdU9TQI9B2888P3nQucibMNDfo_9n-hrNQiDo3vEGsIhK-uK9LJ0OZtZLvHRaM1Cp6dgzhNMCVNGlj2gQ9LVKoZoBT13GWwTnL_CohN3pxwDIbmmYfivYWfSlEyXHwiYKtRL4cvypPN0j2swYehWrx-F5aNthMl5egV42Vqcyp2cVyDYn2V4IJpnUt6TsZqd4D5AV3PrlhUKEp-W4MghiGGJxgPw0SoML-nPEOyRBaGE-WQRYRoaK5lQHSR4pUB9XNxrRj9Rs_ZVxb7ckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی جالب از فوق ستاره‌های حال حاضر فوتبال اگه خانوم میبودند؛ نیمار خیلی بهش میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31447" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4HGIzQ--lEcqXho76h5rh-QCQxvG2pOSWtsLnbfFdDVGGqYPJ0IjttsCu3u71440c1_DaTIya2XMFQPYXrTVyzdd6Jcdwh6rLMfgpgR2SyiTEii4S7I3czhpgXx8PIJDSTEnK67F-NvJlA7Z8H6daLJgh3gZiDiBJlvyT7aJLw31jl6iMqDDskYHA51E69uA5wLRx64AkFXaOqm-Ix5AwHPO-OEH0fJ6GXMSWqGHkpDFRFcglZ2BGdbl2WGDAE1-kq5yzaD63HMzX0YwepO1h7EobNO7dw8k3RdQJKVxlCcQgg4_nv78BI_zZC9eOoHi0reOd2xse7gIdbP9XrlUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باگذشت‌‌بیش‌از 15 دقیقه از مسابقه بازی تراکتور و الشمال؛ شبکه‌ورزش موفق به دزدیدن تصاویر شد و بازی تراکتور الان داره پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31446" target="_blank">📅 21:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDGJpCp4ulcGiI10hLRZjS2JiyKsYmukPZSU6OM_zRqtNxorg-UQWuY3XFjbmQJt9wt-rNSjhPMC11K0N3P9Lctu4F4GaNdwUphrL4y5NXfwNH5xKy9NRloQA7HeRcFFROsGL8FcVxHJkcTKes9ING7h2uiWE_mb8OMFVPxCBHJvbiL3LjYkUI9D9klowfv0udBnLRjEQTNo6iGHhbHyWjbZlyFyeTzH7W_tUt441KUzmJJ0N01ZYq7DxMgp04gD2YWK9ua7kpCTEzAD7Peh6Tug6jiaMa_oFZdv_7ZpAl9IU6OBxT9erond5hDZ-40fG1RP94Y6IYoZvyupoy2zOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31445" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEbGiD4iJffLO2dfYcyWwELV-WgXUg9KZZxz0Si2lqRCfTndIp-qYYIClHPajtnrn_jj1koCtbMIlYrL164tU96Q32nUgqIjCNGERgFMCo4Hebz70BgupmVYjTQMNu4du5csoDknUgZD5BLp0omnpI4bwroAaymwoOUKwQ3dpYxvDoyrb9nA6MKM8HR3OoWyZW_uhqK54qUNrAwa5vfJALvyr_LsNHcJ35ZT0ihBDFsjRlLC75X3UAg1-e5AJuMZJms4U9xvckokcd7B_aqbGSBR1-hLc2beVgrHfTh0c7th2s_BFGElmt6D96-aXFFr32w3ndhCuv77fubWf9akRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار باشگاه فنرباغچه و فن کریس رونالدو که در ورزشگاه بازی شب‌گذشته تیم ملی کشورش مقابل فرانسه درهفته‌اول لیگ ملت‌های اروپا حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31444" target="_blank">📅 20:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS3LVry-UiKwlqArLu5iX1LDFfjbNZeFnEOynfgagzmnoAdTZhHnxpEHhHHJZmuaTf8Mdzj40-F995LIiG7dymjgmF-u73vALGVomelxk0iBT72KA_5UxprQOp8ZHTFzCCzMaKpeDhJxCQlwsxof4eNGixBdYmTG8tQX7NfbScx-h8eAOb7LW7UQQvDmtxKg3RCz8q-0Tlbm5SSMwQBXg32Cnkq1895kiZ-JEpZwnGHLTs98hk-ZlvIkktfQ8hv6nir6Bh7r2bURWdxgi0ZbI8WcxKdsPLWwcvmbtoglN8c4EI9zrtMkSOBMsE3RWNwUnXZrwpZZfoAuzjz_MO9QaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌نخبگان‌آسیا؛ ترکیب استقلال برای دیدار مقابل الغرافه قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31443" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_rbYfBj4UCcPMegx9TgTY_6wZrg0O95KStBdR4WrXxlKRG4XcRRBH3hVG1DiOjK15DOKOqmXheTgtsqDAbWxHRa_-VLLosa5j46uPQxylVNLzr1s8bK80uS7sF1qcMTUTgf5MILRMbDkL4Q3VElO_J4lgPyY-oKgNPMiWjU3rOW0pfE0awtDpo39o19kKG-Aohbj-SmcBXZP698NnecB9h2qBpYxOAaREwA0jQRJoqSkauDopVs666dUJArkLQ4u9SyJHf_NDXiCyk_99K2xzVlmOP8tKeCUAECNs0LduNlff0e-yDY5b6spsxFEA2PU_1KCNj_RQ6kxAtFinIXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31442" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=SZjbLd3NNLuLKCfd8H7DT3SQLUeokjVyrrszTOjWzSfUbfuLqgJB-kUm0dgk7NQzsgArDshbf3LUqnyHlvJTxQEFvRuVy4aO3vD0UepQ-KMGsqIuzH7Xb3MMQ0V3C2K98V8FPEFAyuiFaCyXvBnmzgy8WNweZOmkasVbrMJLBFzH-Uj7TgUfjExd4bHe8h1o3rX7IMLn1f2E_nLhuBEvmqV-3zRLVyxFXMj9fPjHRAn6WR_dvOg6UhGtSo--gO5tY4w0OtJ4NzcPVsbapce6uyMUC5Nb1Pj0ejkCo4TxB_SoLpoLhjZI6skd8Lm5ssdR1VoO36Iv-i7PzYF6wVriRwP6tU-RiSsFjuEQXfPq4tz61aG7TS5ZgBoVuaT17jxN_HHbnJzqzIcx-yXjsQmJn0AZVBivXddFEXamqo3GvGtf7bBwEZDcZIx6p2atm1opxIJ3ukylSUhJP9mnhw-aMUtNPxAQXZEWMcmztT16aano1TbdYpitw7OOQuJpDXTo_wKzBLUtQOzOGyUAo1u4Kl6r7paOTVsK1ShZybyR1MkJZjXP0BukHX2JmxCQUJSVUYNWhheJLz0aCgBc_Ig6Vo6xyw6ccnJCHp4Ya5imlp9fSwRubCTX0YNqP5QY9CteFUCx5-dnyZS_XtMok9hxOJv5oy_L32GQImw8NP8fzuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=SZjbLd3NNLuLKCfd8H7DT3SQLUeokjVyrrszTOjWzSfUbfuLqgJB-kUm0dgk7NQzsgArDshbf3LUqnyHlvJTxQEFvRuVy4aO3vD0UepQ-KMGsqIuzH7Xb3MMQ0V3C2K98V8FPEFAyuiFaCyXvBnmzgy8WNweZOmkasVbrMJLBFzH-Uj7TgUfjExd4bHe8h1o3rX7IMLn1f2E_nLhuBEvmqV-3zRLVyxFXMj9fPjHRAn6WR_dvOg6UhGtSo--gO5tY4w0OtJ4NzcPVsbapce6uyMUC5Nb1Pj0ejkCo4TxB_SoLpoLhjZI6skd8Lm5ssdR1VoO36Iv-i7PzYF6wVriRwP6tU-RiSsFjuEQXfPq4tz61aG7TS5ZgBoVuaT17jxN_HHbnJzqzIcx-yXjsQmJn0AZVBivXddFEXamqo3GvGtf7bBwEZDcZIx6p2atm1opxIJ3ukylSUhJP9mnhw-aMUtNPxAQXZEWMcmztT16aano1TbdYpitw7OOQuJpDXTo_wKzBLUtQOzOGyUAo1u4Kl6r7paOTVsK1ShZybyR1MkJZjXP0BukHX2JmxCQUJSVUYNWhheJLz0aCgBc_Ig6Vo6xyw6ccnJCHp4Ya5imlp9fSwRubCTX0YNqP5QY9CteFUCx5-dnyZS_XtMok9hxOJv5oy_L32GQImw8NP8fzuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریا بوز، استعداد ۱۹ ساله انگلیسی، پس از حضور درآکادمی‌ های چلسی و برایتون و تجربه اسپورتینگ، حالا بازیکن وستهمه و بصورت قرضی برای ساندرلند بازی میکنه. به‌ایشون‌لقب آلیشا لمن جدید داده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31441" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pttpnrl1lNbhg0pvixC117hlV2f9uKNt9UOeGsGL-qSMOsn5AnyyV_NPoDZSaEmSo-_5-V1eoFZEXzhhu8VRWhgzkkXBVisL15tXUR8w_AFZscFRKR7lwn0eug17iV3-Bkr3MOmLzHGs5CDRzeUd8RBkoVp_QgXwXJcLoadXss0eHQfqpay3bCK6pwY2_jDfN38oCkL8YGoiSJ6Vm76eeWIDfKM6y-h8GBu5TcYUBIuMyKLG9uTuZXmDMuxcJ8xA3adKvBbaZ7qeqw2KFe4FQ9VSyt2RXoNH7iTZUtE5Fzau7qD7vliLj83nrcbdHEan-PoqdYlFamGTISfKofQ_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31439" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31438">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpts6Iz48TEtuGW4INLveZzxeJ5K2d1Cl7h6h9jCaRHoqzNAlbIoAR_6YSv0igV11CiCCUERooUQxo_xzO_R174VRxt0YIFqGvo0yIjzM6wOquYbrwZUDjgqSQoMwu9RKVO83bcNhGtw_CjsAuMfImUY7fQy7XXxKfbkgK6PXFREVgJStz6IHDqORX_iqLkPMwEQW9IeRSp-K1cx58NLElejnKYGEq3mZG-05MRANr1kLb5wIB4-le8Wt4sDn4_ScauvojjY4VPhWhh8CSITwgYkYNoT15yZ2m5_xWe7nMNOqNrl-N_HvkafQIAuMucAWm4J1WaIRx_XKOdvplHm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31438" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31437">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWEFcMeTeeQ_mrNsRiyjAvXnUE-iyixUnwfmSqNFlOH9PvACpvqy5SSF9bOILnIGuE3i8rRxEKsQRGSFZpt_l7QzAh_D1TBj1TZ8y4hAV5d5qcntqIZegc0q_kqbEUu9TgeuxojcXbQitBgccRp68QZt8j_SPMqpxfAP7XCk5QttnC-Tl_HR7WZzwQmiwHlyYg2C9Ff9QeO8eydLOUyHcmxPE7zqmSPntzuoujeysLCtd_uHKzjYMgsJqCeZM1_zbp3xAwKoVwpdjv5y914LKI1QYb2QZFhWv25D55TZHMFn7FHU680NrJ0qC23aHTiiFLPfD2Bdmsc8jTG2sejhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فدراسیون فوتبال اسپانیا؛ وینیسسوس جونیور ستاره برزیلی تیم رئال مادرید مسابقه سوم آبان‌ماه با بارسا رو بدلیل محرومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31437" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31436">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWIhlth7X7sSboa9OjEHjHCFBYIeKljnUkB1vXxPRVVOxhNqx94yuk2paod1xN98PT_jgamR2hGXXWgrHBLcSY9FY5yeCNn2qi9NQZ0ljjS-hq0kOqSvjVM2vdkCe4KH9RQOspRf5gWFfp5s49SmLYU2z1goXMYaKpSoYHuqI_2hBh9fGPM5awKaq5l02_TtlAb9OJk5b8NGQN4nStz3YuxM52EE0T8I0EuGb6SKLkvF4KMl1Pkl8zk2aphUzOEiMb-nSt5Emw3iDrkheBulEk7dfPDpwEr-vdco-vhLCKCZ1FNVlFHWBJoCBHhRCUMjtSnJRVDSZNqF5D-QpcNrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه از هزینه‌ای که باشگاه بارسلونا برای جذب پدری کرد بابقیه‌باشگاه‌هاکه برای جذب بازیکن هم پستی پدری هزینه‌کرده. پدری درحال‌حاضر یکی از بهترین و آماده ترین هافبک فوتبال جهانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31436" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf0B0mruxRdoSjrbEzHD_VBRTDlm5CShG2druLDu94UY1iNC-41SG9Z7zZ2qrsTpMiqmeR9Snx3iwK6tz7Mq7NpyBYf4JruhgrOTm9IHwSrYAXmrQDAt9ekHa4oZFcNtAaDWa-ZSdSUrTR6Wm_EOf-RTzfwceSJB_0HnCK_a-W9hp-sPAcogC97khECHCqLcBkYc0ixN3nhHszEuceYNeeOFkMljEhHtAtWLTlugsDoZTlu7LqAuluVoYsMkJpc1xl0LupdqGcYO0abGk3a-ug79hnXsdS1sYM5tBAGxQlEA_9aGronmHR2_6r0q8ZCf5b9t-4_UTpFdE57phix8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31434" target="_blank">📅 18:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=V6YhSejXZRxr1j1eJ6CHFTii3Td1VR_VC4XXhobitnZyvQfcuRh_5hUxwmNQgRSv9NzljQRrk8LwtyjgpkvKU1tkkbRynmwkA0T5h7c6KmKZ_nbn8a3uO34u_LuUnKZKmH4mabXMVvFKFW_LVgpMOvfBS_w5msYxEOou8bYWrF2PxFCwbtd45Nb2YsLvGCW-fEmIeBo-OmtIEW9awOtYqHX8T4yvM3gcFotCQcmcWdVY1CYrlvB-EPBm6ei6PqkMxykR3FPnVJ4C0DgmQC3QXDxupkIgMto3AfvJFfp5Zqy_Er_H8E5caKaYLI1ilcEFaOOjIU_k2-cWdKkDod1ngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=V6YhSejXZRxr1j1eJ6CHFTii3Td1VR_VC4XXhobitnZyvQfcuRh_5hUxwmNQgRSv9NzljQRrk8LwtyjgpkvKU1tkkbRynmwkA0T5h7c6KmKZ_nbn8a3uO34u_LuUnKZKmH4mabXMVvFKFW_LVgpMOvfBS_w5msYxEOou8bYWrF2PxFCwbtd45Nb2YsLvGCW-fEmIeBo-OmtIEW9awOtYqHX8T4yvM3gcFotCQcmcWdVY1CYrlvB-EPBm6ei6PqkMxykR3FPnVJ4C0DgmQC3QXDxupkIgMto3AfvJFfp5Zqy_Er_H8E5caKaYLI1ilcEFaOOjIU_k2-cWdKkDod1ngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد!
جواد نکونام سرمربی تراکتور:
شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31433" target="_blank">📅 18:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbeBsveenfIXt9n8_lTj-aTO2f-S9J9EdD73fBNJZ25GNtlh5RKEd59hjZzKAoR6LcMjYoUoe9zRHV1N569lZi6ybms7ihMWB1x3Ckj7lanv0CCvoauHCjtFlUwf_6TZxXs4grozxexiW0BF_x8Mcqf5eaoWMxkNdfIEYPU4z0hWTbGhiYmn5-S2bnYUF-4p8GBHsIgWsgqVNb6NETTopK2fxPW_I_SjGiZnIGqmp66n1pIQM58UxMKqSJV8eVmhOjzaJ87f73B1jqKhKBg9xU5i7ZEO1T-cWWb7PE1rk7LU9_nrCRjYSwU7Kd5QiwY7poGIQTbUlZGwUurgFWNZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31432" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Frq0-y8wMHTPPZh6fTtplww9agy0JvZQz0t6M-W6mwKfFw8IVefeiJ30DjsONUIymdPoMzySx9Zd-sYuoxnyacoBfEoIrRZC1y_EKRk9wpGNp7FGyzW-vZFtwJJuT08eAd4mtuD8Av5ZphaaKxuapb3ek5eWeGwRgvAotPUJlMOKLGdLdYAE833CE8wma6uzk5t3Z58bBbqbxwvn4LhuXvH6ze4cNl4Tkcll1mIBnCGVpPJ7ljxie0s7bzdfFQKNBoPW6IIKGQbW_yLAUETerLHg0OEbBiQ4TKc-9FVZC9JuUHhLMEyCI1maYAWo63GIflB6G63EF7_IyWWNeYkVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قد عجیب پسر رونالدو!
کریس جونیور درحالی‌که فقط ۱۶ سالشه، قدش به حدود ۱۹۰ سانتی‌ متر رسیده و حالا ازپدرش کریس‌رونالدو باقد حدود ۱۸۷ سانتی‌مترم بلندتره! جالب اینجاست که با توجه به‌سنش، هنوز صفحه رشد قدیش بسته نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31431" target="_blank">📅 18:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQvZ82xVMZl5aNCKMnOf4d7GCqY6B1X4ofvPesLSkMdwcV0B8WKEjdxtao5wh5cV4OfILnuXZsahLV_pfc6GDfnG233V_0em6GwhhnNs1tzva9gn0krvWSe5DyR4_GaBnuSqpHg4-gBuGNnbP7MGrtbRud6ojOClpbkP8m4W2Js0iTUTVu5CrpzdjjjeGen3ENoozj2Y2X1JJdd0JI27hTD4hGK-FB-wnZLo8rlMms2P7qo5r1XIYHoLbiKa4M0KHChpbyO_XSffGRt0XZjVunxPoMyRASpulV96dRyVnxCwOGlcM4e1XSLJ7P0bvN9oeD7oxZ3k1locMEASXJUrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31430" target="_blank">📅 17:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFLZzC0H_95TWurnz8RH-sgVBFrgdP5AS8S6I9Q1yGVD9YAEkyZ6oqUcjDY2WNqSUfWk3C7wo5yZrxNsLuRO1ZB04ea2drI2x7AZ3s1cJBp9oYEq7j5RlhPPT5D0V2KgwX2j_lyP1yACf8DA4uNwb9Ur6VX0ODOWvu-tLAKZWJQ6iPtI2gd7EGVVsxEIOBq7ileqd721oMWFfuLwELEgMLdDRBXMwFDA7veby7wf9HmPw6PV6qzVdgcGn5yJllwK-xCpIqk4glFL4bqLGoT9Tu6-UkQ-7lHt8v2M4QcQqb0u7NRhujVRheHaoxwgV3a7IYojL0IRnW3Tor4ZwjeYhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخواست‌پزشکی‌علیرضابیرانونددروازه‌بان سابق پرسپولیس و تراکتور ازسوی‌سازمان نظام وظیفه رد شد و از اول آبان ماه اعزام پادگان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31429" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZO_00SXhy6yljbQF-_7xGGiShI0VsFGZLhfimFOYIbFi7N3kbjBuPnmwymYHpJUHWayRKB_prz8R8h2fA44l0rwDgZiAJiNjjvxCMVaOP4p_Dwi1SDLNmb_UE_s80MJpeLREGeMdh-DzEIccqrMW_89XKlZ1YQI6LG8PQfu-8I9RAD8zS1fnWuSoXhqM1hs-DEA75bpDGNJXteq3ksi72BZJzfwYrlWrkQt4zCF5TxmSD-xg-z9X9pRIumqX-yRDMgwZSHBP-nvZiVnXpMRPd97v33rcbFeJN5PSh4YjB_nl54IIattxsbID_3_4bxgYelCGfBjsbwsN_631McTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ سهراب بختیاری زاده سرمربی تیم استقلال در تماس بامدیریت باشگاه درخواست جذب همزمان یوسف مزرعه و یادگار رستمی دو ستاره 21 ساله فولاد خوزستان و فجرسپاسی رو داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31428" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh2-tKTozL63Xed-D1p89aGjYE1QCuxea9NqG1XmlilFZoeBUh014aVibrwI9ie9Ai9C1RrLQNsdDzsPJzQ-AVD2Eohp62ocLWZsQERR_l1Qy-p83Ksd9Gi2nEwYji0BOpK8fI4jxVpVfEQS8hk53WnMjDosPXUyWw-_rXO0SewIvoGo7uWqZj03955nvE_zkqdWHz1myvIVPNCNwmOOYsmDtpnaG9BYN-po-9SgoDY5YFdEUGl5B2gI_b1j0pRNBOzExNHmsY0WNAjIyQY1ReM7HUSXVGZBr6r43_x2B_UOD_y91u2OTpuxQVpiqH1xHJZ6Nrowrz2tPqSBNkgqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
#تکمیلی؛ کازویوشی میورا ۵۹ ساله قراردادش را با باشگاه فوکوشیما تمدید کرد‌. میورا فوتبال حرفه ای خودش را ۴۱ سال قبل و از سال ۱۹۸۶ شروع کرده و در فوریه ۲۰۲۷ میورا ۶۰ ساله خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31427" target="_blank">📅 15:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
ویدیو کامل قسمت سوم فان 360 با امیر مهدی ژوله با بالاترین کیفیت؛ عالی بود حتما ببینید تا آخر.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31426" target="_blank">📅 14:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMpAuVxDzvmxOulDk9mfhhzayag0hfLc7Ln9dL4RJoVcmQ1uos67trq6P0F89C0RF0xW2MRIUPBYVQnfVF3oc-vfCsbug5DlxzB7TcVK5qQ27eT29MlCwoA5PbLyumlXULCTdSzFDjB0-op9bWgxTJdMCbHbhmRYVke7ZmAUepmNDak4cjSNdz-XS3M2r8SrfvpkAPlOj59Xi4UY3rlcFLHAVV7Y3jl9hB__ThaDLoUTSw4Q8FrxOucVxET6uEiLHkQ4yeiKFcPxQclx4WIAsMdgRudkIEIhx9kVquUsGVE7aVREOnyXSkCHlwdcpO_k_18AZYt6a1m57USf2Q_9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31425" target="_blank">📅 14:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoZ3Z39atlhEePSkmjXlslpZWM6ljmvl9AmOViZHxTNx4ImSX0z-4rM7zhUeJMm13X8qVIJmuIlxMY74KZkGi2SZd576yya0M3gQszEpjWbtxjSQDx6yQWrasTCVyeT4PbLCugkDX-x37D2YzmpQvzVTtDvco0Ee-HHmqEJOOyWNaAmkstF2fVMzGDIfZ24YK-qqqfI3E_aohuOMVM_r3TzfbiE8ZnqN0CYlqaaZW5n5fpvMcaRU7Jip69sR8k8C3xeS2z3uQmNafIkuE1aTCldkMoLfoe8m5KGPyVqFwedqIcs0iWceBSemlB9dJxKd57bHGHn3PfNoIJiv9SEEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31424" target="_blank">📅 13:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=LuzpKk8UrUB5p_Xun4IRL1rCOmQaYwcSifssFW-j9gnVVurvo2SgtFkS35Kfady9TjdIZnmepF2n81M6dHXX163I7-vSdX3cJ4lU6AGJaVTBMJsypSi0d_UDkUlvaKZf7YoJythFSfM_gcgQz-DOHNm6gL4zTjkEoQnyRfxOBGLEAz2CEJV4XT7ABNopNZWGcEMi4x4C1VRc3oTqPweqHmRiIiYiveFq2-THqOOvlGBUK2lQX5847c4ZpvuEV-Md-GJGgn2NZ7-oXvxPgTarCuJ3MB8R3wH-nyxhIbk0GJ_mtYlA0UlmtvQscnNSkF4a5kBujPSpZbCzp8iYxEZTt4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=LuzpKk8UrUB5p_Xun4IRL1rCOmQaYwcSifssFW-j9gnVVurvo2SgtFkS35Kfady9TjdIZnmepF2n81M6dHXX163I7-vSdX3cJ4lU6AGJaVTBMJsypSi0d_UDkUlvaKZf7YoJythFSfM_gcgQz-DOHNm6gL4zTjkEoQnyRfxOBGLEAz2CEJV4XT7ABNopNZWGcEMi4x4C1VRc3oTqPweqHmRiIiYiveFq2-THqOOvlGBUK2lQX5847c4ZpvuEV-Md-GJGgn2NZ7-oXvxPgTarCuJ3MB8R3wH-nyxhIbk0GJ_mtYlA0UlmtvQscnNSkF4a5kBujPSpZbCzp8iYxEZTt4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل بخودی‌های تاریخ لیگ برتر؛ از گل بخودی‌های عجیب و غریب محسن ایران نژاد تا گل بخودی مدافع ذوبی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31423" target="_blank">📅 13:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-9pN9-BivenAs2uecbvBNSQWYz6xQGzPhl4AG6x9W731N-v_VTsNVV6101HrzhLkezXT1CD9Nwa4Vh9rR3VoPb3TRxGFOzepAvpFEJe9G-V-xhH_vVWjNZWLxTffBjl4nCCFqorA5PWGf9W7g8zcSSwlygZVbT7o7yG0KEPfmuR2MbSd8K8KZL57VugKyJopZIMtBsmZnIVhHxB4pzhqeedE8TmhcVsIgSDezqPfs1rggVocM1qsr_qXc_YJiRhUyQGNlvwBXLE3pJ4dSxOnAGLSQAcSJPKTY_oD_vzSwkckC_dxQgpaLPBzm11gIQi9s1b_HcecVfkfWOx-hvNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31422" target="_blank">📅 13:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-p0oqDpRHbbeCDlsIctKr6_fbeHlXDx4amPEqcl-2iTFTvrHEM0pF7yqsTj4gqccYXkEP9vW12ppQIVMDcyQAJUeU2Dp50W8boyk1L21Mx5HafEe1HaONMtY7ILrs8w73fhtHZiYascQVCIKCKTExBqNikSiu03DpD9lNiwg4hxQ7ViubyKcbZu2X_SPRmH_4GXZ98J3Fk6dB2-HQkATcbE6InbOxl3D8mpPyp8To_pvt29Sdc4xn5T2RLtI5lFfBHs8ytc72FjV6jAJagBZ0fUxUMKncUv-DsxMwsxHPuuU4PCCCVSoxNzZp5xudKIEj71LjKMGNXXELQwIZ3o-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31421" target="_blank">📅 13:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj9sIXYYp2f8J1Xe1UKZYXUnPtmsm7B8LzbLYf69eqpi9UwVqTE-92Uj08oggvC4pT8SE3okMPicS7FvNatejFi6ZZGPEzfzqskUQOAQ5_h5_0TfXsyUSzrLbZY-Zw6Ivelvvxj9NzyAyIhqNoJBVYr_BrT6Gi9MEPWXzUcYl2LcL-6FNXeAAVpDJQ2sPK6reOafHctkKlzpsWMaIHRModML7jp5EVAtXxi7fZWcnGBpfOS8IAtRxa6hNmBG8_KH4mcybXXJBEeLO9GG2S93OAeT4RLSrI-9f5c0IC2MFwbs899P-2ALzNapLohNWk1woKW6B1qAp_onwISKFZPH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهار افتخار بزرگ لیونل‌مسی که از سال 2021 استارت خورد. مسی حتی‌قبل‌ترشم از بازی‌های ملی خدافظی کرده بود اما به یک باره ورق برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31420" target="_blank">📅 12:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbojz1cLEHipO9V6XykNKuTMnU_NrXop81tZ32AqfSDcQrybEOQ7nBWDjsZ1hod75IcPti3kRUT8KqTrpSp_XW2T6OBQ5yEg8jbZLd6j-H1L0vCMHFmV_c2J-Ao2B5CUFNvXQlhw2curUJlPVEzrOD8yGwZSNjk_18PMxGQiMZ8KL96eXaLbLdLC6JFL_FzCoK-8nea_QPgl4Q_vQB5UtkEtMMls3T3Sq70WPPsAbUKLnE7DMd2zJxErJ3BZMej_3ilRasayx3D0U2aJuXxwftX2zOF2H4u_uXeuzq-hQNBnNjcUy6h8O5q2luOrLqLS6cdcKV7SYJ8H1uoIfZidIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31419" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31418">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0LIksGepa9-L7dFMSypXfSLQqGQ3cAa6RZPzqP2Qep8qFa6XrFRazqrvWr3toSA_-JYnIISf0CMoPmhj1KvXhH1tFw3O_Rbis7lPubbK-DMoco21xXsRb_HY7YXW_lVcMJ7kd1FLCmQTqUgiqAhYL2F1-hYxsbklNzCeJt5GpYjlGmNCs30Y-Zsp9L48yh583s73v0zRxAPVpv1q1NY3VktLYwjAE8DQqGuy0miTT1Uywcylsmzm_XZzr4UIVK6LNVjZXY6GQjcvIbYQmGJWGic-PgqwlJEj2Gxa4c5BeB0TjvHkwHC4koOoNIdKc0GpAuSIsMt-es7RGGJOmHYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31418" target="_blank">📅 11:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31417">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic6gXSnkc4VWmor8mUYm1FJ5UO-YILYC1g_IwWzgJp0ToCJnb94H50qfrKLZcoG3Jjb00XsqjzI_Z8uzdEMZY0SyMFHWU8UjOD3ywEyj2S1kFFJ9EIxJAcAEtMhLVetQ-XW0Kq4y11sfMoVHpnWeu5PDzCkkgfU3QemlQyfYnMbFD31zpBb9kJsiT2OG9TTbMGgTTRExT5c8lAZn70j1Jt_ZyznKpHfQcrU47CLrFodtIqQ3l3QL0_cCa1M7fyW_6GJgvAP9a4cUoQ0hagQPdF3nUj6mGfz_kCHcuGgGF5vai00FIR9bYskaCRFRst829S8VGYf7jjBQBAsLF4ul3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضابیرانوند خطاب به‌شجاع خلیل زاده: هیچ نیازی به فالوکردن بازیکنان‌تراکتور ندارم. من به تراکتور نمیومدم این‌تیم‌عمرا قهرمان لیگ برتر میشد. بعداز خدمت‌سربازی به تیمی خواهم‌رفت که قهرمان خواهد شد. ثابت میکنم هرجاباشم جام خواهم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31417" target="_blank">📅 10:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31416">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMGOzIJm2n_S4uMGOQNCJxCQb2R9w_kb3WuiYESR0ztOwocblUwaIJu5o9fjvK-b3f36qmk7QD2BybgxjcpHESej8Rvlk2RXFgMG3VpRrQpdqn98e0lDXuDzAmDz8PjrvVCJZ_AoQpKTfBuSMgMhJbdk6vktXiXw7SwXfs16SL8o0qvYsojbwIEOZ36K_oKTcsbA9Du9EJ8mCaTabuhRC0UTYiZRSODkOnR7Yms2wLzbUKZb7h7dQMubPcsZyutSrMscrxmACV89Yp1kDbt2yT8rMas9gsiTE8tTXTwOxasfwD45N6vDV4irij_Nq6PgYMWt5DVKY5nijgX-T5A_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31416" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31415">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Unq4AOWVH_FIt0aSdjFrTY0AWFkaGS5CgshkzKQoSOFvuc1u6Xyzb6BSTQtyIQUDEsL_90HXkfk8YcvAsTEQ48TMY5fHBVUJdg1FDROK5GVbMtb-sLf4thwjlTnAYfmXhexazdkhvUeaBBTOIJ-DL_09Gk98yZ8L5wgaYo_drjznNALh5-4nqaZodSeIW4GbWsfELbMMfGXK4nrUwnPj-8I7JcOyi5pE-eQYfEEcbun7EsDgbOCxIxu8XbOhwTBn3fW2ceW-yNGlgeFkoX6yuirtr-0QdFj1Csvr8ZHMRmIZM5U9R6Iq-o_VQaX0C582sZ4496_OClMWcmojpTCpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده جی‌جی گابریل ستاره 15 منچستریونایتد درفصل‌گذشته:23 مسابقه، 23 گل زده، 5 پاس گل، میانگین نمره 8.6 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31415" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=nsTo693NzQc4aLIzTWMPZTAnZNEYVUXk7aAJ8GEW-blbntPpHK0hUOersW0-d5lT88lJSTEDmDphNkC5bAsoPmwM9IOH5aIH_eNCxzU_fOiIOaE4TBszQgtL9LLNKqy2kZBtvq1gYbfWdmIAs2P_fwt-08UC3x2vZ0yL0jyWE0-ykh9rRgogJf-8rxqmitTFThVzPHM3FeBNVUUYR8L6nH29pSo-HrEW47uRIWATt5zLPYqr9yKo8gIj3Nnp7XCrN136ATkhQ7enmdyZU0OcHdNxg2e-5vls8MpB51RLT0tAIrSv6MC2VHPpo7N271IUTWZzHhHl8sj4p4sZn0Rp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=nsTo693NzQc4aLIzTWMPZTAnZNEYVUXk7aAJ8GEW-blbntPpHK0hUOersW0-d5lT88lJSTEDmDphNkC5bAsoPmwM9IOH5aIH_eNCxzU_fOiIOaE4TBszQgtL9LLNKqy2kZBtvq1gYbfWdmIAs2P_fwt-08UC3x2vZ0yL0jyWE0-ykh9rRgogJf-8rxqmitTFThVzPHM3FeBNVUUYR8L6nH29pSo-HrEW47uRIWATt5zLPYqr9yKo8gIj3Nnp7XCrN136ATkhQ7enmdyZU0OcHdNxg2e-5vls8MpB51RLT0tAIrSv6MC2VHPpo7N271IUTWZzHhHl8sj4p4sZn0Rp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت! زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31413" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=fP0ITRWncJyu8N0L4ePzTYU1T4fQe4NEhNZpD1DWX22QL38NL-B_t2IxHZ3UucRjgfzRRuv8CwI0FWyQTs2Lxzz84itpsrrsrYDTR-ZUBzz5TiyvMV_QwfwnAX9ZFtH_tY_qJkPv0Xo2s9cSXhKBquM3uXBz7wiIeQxUGVvQVL9qamudGsX9yzEcb1I5uQN8ExPND0ZH55LZcLLwU-7Bq9z2019Wga2LOUyTQMR5PqALEMEN_k6u8Lf9uaKystcqpAcfi2U9BWTQqfh3vt8874BUQgGbklpAnXwWcNn9pKF03kXfmBC3fPd0s_pJFTeTanDQi3ojbluKzhhvu1KI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=fP0ITRWncJyu8N0L4ePzTYU1T4fQe4NEhNZpD1DWX22QL38NL-B_t2IxHZ3UucRjgfzRRuv8CwI0FWyQTs2Lxzz84itpsrrsrYDTR-ZUBzz5TiyvMV_QwfwnAX9ZFtH_tY_qJkPv0Xo2s9cSXhKBquM3uXBz7wiIeQxUGVvQVL9qamudGsX9yzEcb1I5uQN8ExPND0ZH55LZcLLwU-7Bq9z2019Wga2LOUyTQMR5PqALEMEN_k6u8Lf9uaKystcqpAcfi2U9BWTQqfh3vt8874BUQgGbklpAnXwWcNn9pKF03kXfmBC3fPd0s_pJFTeTanDQi3ojbluKzhhvu1KI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر قاضی‌پور نماینده سابق مجلس:
تراکتور پر طرفدارترین‌تیم‌جهانه.بالاتراز رئال مادرید و بارسلونا. درترکیه، ترکمنستان و آلمان همه طرفدار تراکتورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31412" target="_blank">📅 09:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7024843df.mp4?token=XtMq7kdrWFZLqLKgCLSt3WSQxvcm6vqTiUTaq76fdcTiUFrutYGNqIuWtMIvvZTgED_bmUi8iM6OUDdrjUl9Neb48Ix11I8dI5Twf_yY01OFtOYIOknFqPhEn8MvDjXEuuXus004lCe_0WKE9KNP8hdJaMidIOkOJKN7pz-I32Tp1jQrmBug2sk4585Dbt5OUQ6A7ag8K7Cd0fl2jPb-RZsGUWKAxD4RctBjpZ5ChLsMoeXO0vbLEgT6gibbJZdVg3RTyf-v7vMawzaQXfnuONKy6VDeBei46_B39Rgryco3cobtChCseWeCdgvLobsp92HPwQ3N22ZwxRa_T8G-Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7024843df.mp4?token=XtMq7kdrWFZLqLKgCLSt3WSQxvcm6vqTiUTaq76fdcTiUFrutYGNqIuWtMIvvZTgED_bmUi8iM6OUDdrjUl9Neb48Ix11I8dI5Twf_yY01OFtOYIOknFqPhEn8MvDjXEuuXus004lCe_0WKE9KNP8hdJaMidIOkOJKN7pz-I32Tp1jQrmBug2sk4585Dbt5OUQ6A7ag8K7Cd0fl2jPb-RZsGUWKAxD4RctBjpZ5ChLsMoeXO0vbLEgT6gibbJZdVg3RTyf-v7vMawzaQXfnuONKy6VDeBei46_B39Rgryco3cobtChCseWeCdgvLobsp92HPwQ3N22ZwxRa_T8G-Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ذوق‌زدگی امیرحسین‌قیاسی از حضور رضا گلزار در «دور امیر»؛ پز دادن به دوستانش با حضور گلزار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31410" target="_blank">📅 08:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVEw9fZrH8C0tSBhi6DsVwYGD_GO2tR7X5wiStCkufWW7aAUHh1WzJy9rQ6porrqf8b7hJ1kyVHRTuxMM_3snaBguK8syT59lKp5-_bquHxdydTRUY7SMkIkfeBigIlTfZgYSHoCUQlRgENfDkE-TNj-188NBM1nSrJSRhAJrIkU-J46nyWbvlkki8YbwZwHFn_FrKLDC7R_eXBm1Iakyl-y-3MXXSz5mGWQrpFGcEBRLNvElLu2iGV4XjrncEpVtO5bFOQ7nA1tU_h54rYH5qBSqHbOM43Z1RMvDugfAqaLkPJAVtG3fl8WJEybiKps3Twv0i2yYRRSxNXwIph0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31409" target="_blank">📅 08:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31407">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCcitviaudM8URUI8-LvM1q2Sx7eo8P5GpEshGeR-8zq5VzRfgEJHBoh6xOHI6y4TgveozK-BG47XA-EK4Le881npOnObINyUXfcXwz5dyPdNpTWwBQKuVC3km8t5mP6duOOFnmdo7BbZH7KTYeEOt-BpvkArXlL6_sXyDV4_Ffzuk92VvafxddIXL-kH-Jo6-BeNU5ps9JkPAwczACu9CgzjAAZ1TbMFjAuumVyb8oaDiOB8FdREU9Z4T86IVGYSWH-90oX7mkPUlbmb_UKORUtJWjxD0yQuVF4O6IsZH8Tpt2-nTKGTxeiK37Tjbo74ICEvps9NSb_hy1oZwLd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31407" target="_blank">📅 08:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rspxNw0AFkGegc-nfoHN4x_mn_arArTiCmKdnGlFQKDW1r-SucMoJAr4r3SWG5lMeULeoou5n1cPJgX67JwuwFxjWpj8SptyrxL4pEXWvjLPcIGjZklKCNa7xjXIme0PwCPHND98Ktj2wut3kMPLPynIq7-uSOb3Ejv1hVZHq7q9r7aIdeLciuFzo4KSG0WF-G2H0fe8TP3k-2Tj3O4zXefmlfiWYOTqHKE1TUUl1O6GIIlX84VGFo2DWctwRUC3Q5SbJND8jYQtTsj3FqbOGQzgDf9CBmwArDXXJ3Vkk_ey8z0h8LWZQ3XzKRHAD0zDZJ52aLbnVv4l0j-kn4p3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از پیروزی بزرگ شاگردان مارسکا در آنفیلد تا توقف روسونری برابر ساسولو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31406" target="_blank">📅 08:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📹
هایلایتی از عملکرد درخشان محمد خدا بنده لو هافبک پرسپولیس در بازی این هفته با صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31405" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران تحصیلات | irantahsilat</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkoA0xxXLSEIqtNscXsGhG9DojIwzNMSq5CvPdH0ZV6HaMcY1ImX6vD7LWBzv2oYf5eC7EsF-NqMFRmpjR8gbNrN4SDGggIXnoR7rCGPp0xMCzLKkCs3tGk1ZVQ5jiG2c4on0LEl0PPhEUqb-QoaOhLaa9k7A5E2djY1rMarccJzGUmgrUucHYpZ_58EBX9BTW-jocJRdLthqJ637mgAHz2lUG3Pgmojy1TTA_7-bnVSrZ32YOurjkU0s_ZNdYa-UWN6YlibKjcS3LYNTscsvXxHQROHyCXvfKw_1y3qVu11k0PUvNNbD441waA4O0hHHKn002qxLersN9nM23cxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
مدارک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_support
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/31404" target="_blank">📅 01:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGZxBB0GCDMfKSebGCObBvzy03GaOqpSF8ZDM8GIipfirJoOyZtk7zoNjfZ0GbF92Qqt-zyCjOZFIHNCQqCUI5C8F5m0F904vqD4rb9mwWpTu_xsObwEyAvD4vVW0NU0MzZyqUAjcZQh61dXwRX7SRJlqwc2lcys-JWvho1nvxDuSLJL4zq-oHdrKPXBRwAQMz8VmnUBS9IqGV1k-iwNXaiN_J7JGPZ3fUJaNYW0irAzA2qaQAlfK4NhTmYzfUqy6imfY_dAw6m-nlDM1iDR97U0b2eI5zMEz_BKWvvUhrPxLb7pZchJMKGBUzo5_YCJSyxtOyI4wRVtYwcvDJF4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادار دوست داشتنی و ناناز باشگاه روبین کازان روسیه‌هستن‌که‌اخیرا گفته از بین بازیکنان ایرانی به سبک بازی سردار آزمون علاقمنده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31403" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVmAi-UINXfxqrJsFXCBVX04diAv6Ns026BmUZMHZ383nh7fOQsYpR-h8sf2ZO44o2L79LmFYGg-ql-YKc69BVHRpiDZ8M2pLszaiTBBTE3ELdHpkvAybpfqbdo9tGM5GzuIYLwYFfamhMJx8FMuzC6C6oUGvVBxWo92y2t7fp6c0Ta0_JwODPx7GKjBZgx7tB48GPXOxPSon_Z_BUR6sewk3kGVFvTZ247SZp7VOtvHIyP8T9eVk9vuYpBPpwZNwC126ul_fSAJg1R8xFon7VwBb6KVeYDIIKULdoU7zkI4aAh5b3grJoQRPg_8_bJvRUUfhWvp-sjwJ4DdxaWQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار جدید دریافتی رسانه پرشیانا؛ یاسر آسانی تنها دیدار با الغرافه رو از دست خواهد کرد و به دیدار هفته آینده مقابل گل گهر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31402" target="_blank">📅 00:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ0MAZOTGeTlSI6fdsTh0x1mlbAe_0TaayTxuR2YZ0Wd1MEbZUUTYGvyUMg20MRCLmnk55AMpcM96ujRng8ZCbwN2IJqMLzrpMuyTDpWrbG5NgPgdfpkDhmQ-o5MxcWUT2rU5rfrYtxH834dG8ipBtOAMTwbtvGRNVbe-XACKnKOv7Y2J4hdrplD3doWZwJyi1BY2u0trX6H1w26zg2AP4cK5wrzpd3ZYO35FkIb7vS392MMPPhPkEucavEYDIG0r6u4hn5x0ksJUyuyH6F8G0RQvGXxfoZU3yStyuJm5RXxdBa6r7dqK6Yr0Wo_EJWFHjKtMz6iA6hMK2FX5Hf8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛ دوئل حساس لیورپول vs من‌سیتی در استادیوم آنفیلد بدون حضور پپ   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31401" target="_blank">📅 00:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4azPX25wTr6hW5Lp8PV2_P__1bOsoAqgGNcD2_5gp9avHX1UiOzSBXIaPvoS93Iypq8xm0_5sb89icvbGuE0EWa99h7T1v5Y_QNmR80nNp3ZZ6RVyh_BwhLf3HbMz-V7qBgiZ2KRJTRKK5-Q0BacfV_cje7-p3yNrlqTwkLAyzWkt7BszJbOXb1LfTWwXQjE_BYnCnJiGrgaOziZA1xOL9Aj-HJz6FjUzpJVqzgdy7XcX9CfwHEZmWmiZghiqnn2mQq8DuA3aqwvCx8py5MnBCCNXg9116RZEf-LnLkC8nEQ6HaoNBt1qTumB2YYVId7Y7ooXa9YR2Jzq91TkVoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد جام‌ های لواندوفسکی
🆚
زلاتان ابراهیموویچ درکل دوران حرفه‌ایشون؛ زلاتان فوق ستاره‌ای‌که‌هیچوقت‌نتونست قهرمانی UCL بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31400" target="_blank">📅 00:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pW8hVdkvoCXzeQaK5w3sah8ivLn-8enqneTyMxtllKQuJSZ6rmWWv8u0RtgCVnE284NEVwOPox9IyY8JxzZZpXua_I4b8w3oow2tAkA36NeKfdQaFhUkdDyT0oNWXrFt-w146Hq7sCsPlNjN0yiydytpqPwlbHPPftJx2SHDFj_oM874k8FISIEuKwU-F4H54om7VxxGSmGbpvYZ5vLPxIi9A_CvlT8jLFH1EyiiTnb2H2xtIfMoJ1W80lTH0ctbvYLZ9u_nyB1ep3MIWM5fQxQpYDzh-aqllvJxdvNEwcjffHW2bxRhQ164g6ht1JC2ovmtqdA1rWZc4W2POGac9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31399" target="_blank">📅 23:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJOxYr0is7bnnC95lG48AOemVF4Wk_s_Ocs8_VAcZljohpS2NpxLdmtxY5X4Fq0b0ZFb7JPbmAM5JLSIpvuPivwWJKzlsZn8gtIpDBQmZZmprMLLkC5qh616okYeFLOxEEDeFbfYEcDkzJgWNIUEcbiRG14_Uco1brtu0jwX4UEdQyeSRsaufVUkd2YueAeqZ--6pezJzDGop4y38zG5_nOud4OjJHkTYNfgdeYoDF2_ZqHhYOMrRLdiLvzYFbFYvWKz6yGRlmpFJ8SGCRUhwqzHlT4OHeQBuHJgTnkzGtcJIc0MIpaP7iy-WSpLjKZws9o_loSBZf3mbPPRgoPkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شباهت‌پشم‌ریزون گل دیدنی ارلینگ هالند در بازی امشب به لیورپول به گل تماشایی او به آرسنال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31398" target="_blank">📅 23:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbg8FEhye5PNJqjTTfLqGwPJv6lGm1M81Di_vDFbs8nUQ_7F3DLZITBrD3qzC82x-sLoE_5TyJz_t36UqJkEsdBDaGotZv63CimNvKrt-cyCQNPbpQxXc1_f0kR2AHgA0UuujOGlJ1oRavD7RZsKET-ukjIzZmPMGxlqhSZoYryF9YSJBh-crH-ltdIZSFCkNlEEPYPVzw24rENJnwcUuzf1hKS5t-2szJv1G21lu48O8qmIvaZk74lNEonlMK7B3R1Gx8jefrU0jS7TBWfX_Mf_r8tnDbOqCUxysSmYWiTXuGo3nBbEBWJ9SYJbL6iUE9GY7kgaJHilWXqEYcQahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
افت‌شدید ستاره‌فصل‌گذشته تیم استقلال؛ علیرضا کوشکی وینگر 26 ساله آبی‌ها آخرین بار در تاریخ 9 آبان 1404 مقابل آلومینیوم اراک موفق به گلزنی شد. حالا درصورتیکه که علیرضا کوشکی تا 9 آبان ماه موفق به گلزنی نشود دیگه‌یک‌سال کامل از آخرین گل او با پیراهن استقلال…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31397" target="_blank">📅 23:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_DAFaJlLOJvulpZXb7UqXsfEaPegR6fE1--Ie-xXJ2LR9bxVEsRqfzgxy_kEqmj4OsWL9pXPueJXOw4XLv9s9wzMfxgk1c8O9CeDwIlRALr-l361gzmZ16yTN8b-KscSwkyNWAacKP5PAbb7HkeZflJaFOvncwm8HWegI8RzOvhTP5iog9McHmC0vRSrRCjl8nYaWrYQ836KL83OGGI8t7GBp1epzcC19JrJOuTU1-6MDv5V0Y6orrv36cGzwFcRxKqbl08EapyYjUjguGPjFS7RNFUpyN-F2OoIHz5KWK6Szo5qUmr76rZ_qM2nGA7I1a-jjiqvOGUr_9SmiJ1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد رونالدو
🆚
مسی با پیراهن دو تیم النصر عربستان
🆚
اینترمیامی در رقابت‌های باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31396" target="_blank">📅 22:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=OD2AkAnkGu0Hg-DBjIWJ7jlHN06dzP8wf1jDsfu14cMDnJ89UiHWPRYaa_UVjdWR_NmPErYGa2DNusW5MWrr6z6O6PutshPBBgjCK8xi5x0LcysOk7T3UjhHak0Ca5-GOGkoPyGA7kqU88AkeZfxDMTMOJ5e-5_qGbKSReDm-lVcP7Zc2JICayycuswN0lUy0dXKS2Myi24GYkUOMsrCPDezzlkvZMEU2vr89gPySImRLQupxLdmuRmMMKqQCCNkRP4_KHsmvb3vTWpYPVj8-zzSkPiz50iFTPJu2x3r9TtzQUcA6324JAAbw5FINJz-wEkkGeFl9K9nKFMZE8JOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/095e7b9659.mp4?token=OD2AkAnkGu0Hg-DBjIWJ7jlHN06dzP8wf1jDsfu14cMDnJ89UiHWPRYaa_UVjdWR_NmPErYGa2DNusW5MWrr6z6O6PutshPBBgjCK8xi5x0LcysOk7T3UjhHak0Ca5-GOGkoPyGA7kqU88AkeZfxDMTMOJ5e-5_qGbKSReDm-lVcP7Zc2JICayycuswN0lUy0dXKS2Myi24GYkUOMsrCPDezzlkvZMEU2vr89gPySImRLQupxLdmuRmMMKqQCCNkRP4_KHsmvb3vTWpYPVj8-zzSkPiz50iFTPJu2x3r9TtzQUcA6324JAAbw5FINJz-wEkkGeFl9K9nKFMZE8JOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگاتون‌بریزه
؛ دانا جین وایلد ورزشکار ۶۱ ساله کانادایی، با ثبت یک رکورد جهانی در حرکت پلانک، نشان داد که سن مانعی برای دست یابی به قدرت و استقامت بالا نیست. او توانست حرکت پلانک را به مدت باورنکردنی ۵ ساعت حفظ‌کند و رکورد جهانی طولانی‌ترین پلانک زنان را به نام خود ثبت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31395" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVwX27KAegzq5D-FJvXY5OrQhKW_x9F6irIIRG_c6pdTValwg29-SQ2E3k5qsAsVuyYCCsR6n7MLGhS-uKtaNr6qxeXslEGS-Z9Ndltv6pWyaAxjceJV96ULsfyE0-LVSpGBhKBtgH6Uk1Dtgr4-kTgmPpnCQpszEnLtImJW1p-lQ6b-CStoz2-mzQ8uHrVuzqiGix9-_zBQx5fFzPZF5s6CQwo8pIyporuL41a332ZT5smzzULyU2aj631aG-SqWsZQaHqd_SpsCbRqfslwxe4U0ksbITFSEAUF4-iw_cg8XU4k6YEhdS-6Nnvy7wlD4iAg1iisdD7CLFpXLIbpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام رسانه‌های معتبر خارجی؛ وینیسیوس جونیور ستاره رئال مادرید بعداز چند ماه از دوست دخترش ویرجینیا جدا شد. بچسپ به فوتبالت مرد حسابی. پیر کردی رئالیارو از بس حرصشون دادی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31394" target="_blank">📅 22:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31393">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5mRM5xV7W_jKQ_l1xFJowBke8seUt9fXkVSy0z3Ax32qVgBuym3Xbm220wBcSyQwXYGe4laSd4w2o6km4igaHc86v46HtKrMynJMxyHKL2MWHtDba_U9tr-offxXldN5Q9Tgckr5LnKuuh62lV63bdG539bBsWU5Qo9vP8Uz5ZCF0Gs6tKy21vFNFqdNBu-_tluLMI1mPf299m109evj2uJXIbGExCXttfyp9vpyveFZsoYMYnJcUyzOJ0Fyk06wwWymkBxHBKttiehpcG4oNSNqMi2fqXG5P_NC7X8b63Vi-pR1QGbL6af2TADbghj-g7NWSR_X4BIttwaBFZ77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت!
زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31393" target="_blank">📅 21:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31392">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=hprWIrrFZ5-pG-4OWbQPp9RNLnNqw2w1xlCX_CRbSF0sc_oRUnUuONZIvLTXNYCT04aHBQ8xHB6XvbB3WSpBnm6E80eJGcaN8Zdc6mFec4ImVkFnXCtSni6v46dnYnej4MGrLobPJcmxOgPOV5hCgorG4HQbSXXIdjima5QFtl03uLMM_i-hTW7eRJKm27czmSz0UgJeMiQltjg35D-SD7QTQF2vI9kkwCJiJsb9yQLQ015tWwOFMxrn7AV4idkmyC1od19tLLsgTprSUkHNcWoObkNv9ItojiPUSTykDDGKlnOwh3PToC4dJmHLjiS_MzEt24GTNFOUZoBOVRRGtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6abb5815e.mp4?token=hprWIrrFZ5-pG-4OWbQPp9RNLnNqw2w1xlCX_CRbSF0sc_oRUnUuONZIvLTXNYCT04aHBQ8xHB6XvbB3WSpBnm6E80eJGcaN8Zdc6mFec4ImVkFnXCtSni6v46dnYnej4MGrLobPJcmxOgPOV5hCgorG4HQbSXXIdjima5QFtl03uLMM_i-hTW7eRJKm27czmSz0UgJeMiQltjg35D-SD7QTQF2vI9kkwCJiJsb9yQLQ015tWwOFMxrn7AV4idkmyC1od19tLLsgTprSUkHNcWoObkNv9ItojiPUSTykDDGKlnOwh3PToC4dJmHLjiS_MzEt24GTNFOUZoBOVRRGtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31392" target="_blank">📅 21:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31391">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6RIrazrBP7qj-jJMXJXyc3oV3fXOk9A3JKkR4lj3q2qVCC0Kj5KMouD1PyBKrPM2SpgXnBLXXd0HvvNqEy5piiWzKgTe7hYkJ16yAOCARMjFo7mb_WCCiGNFIXacBLJq6Zo6E3_0onGkzo_j_AJ2VRWWA4dJ1_JxKreFi__zXJj8lQegi2JJkAsazJHHHwccD1xqochyB-CCfNv3JU-WzOS2emW2QZ9ygdHLSMCUTnwzr1oo_IS1D4E5H6pXaUgsG5Lg_lJ5KXmOTJUNEXS3WYg2VIpT1XOxjKzlkCz12cwfcZ4zvqCIVRUyTQyzxgUVCXK1mURDq4UUQJ5TZ_i9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31391" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIKvHnEx7T_UZ7ooWYXceYIpriScRby9YCJ8aqEeKzVLaZ6AKF_-r-D9Ut2apOQTrNGyozJd-rA_icKkqXzcRVT1u7T2m8tlhcbMKEhpHIqYKn6xW5D4RjzYDZD9ieob8wLGMyPUYy852xMMS4wNyd4RIimhAlyg2Aln34ovyVn05eO00-RO0DpZLdu0NYvE57KV-mSWUJypmvjMgIpsPC_q3BYbIqX3bMvHHUpt8tVb6jgICRXk-KO0QtVwTZr9b7TI4o_8BqgpGs8EDQdB7I9zRmXlMG7QBAKsYeJNj5QvoN9elZTuPVs_mg8n-MkuJQjFn32kA5_kXCAAXCVnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه‌دوست‌داشتنی‌ترین‌زوج تاریخ فوتبالم از هم جدا شدن و خانوم ویرجینیا باید فعلا تنهایی سه تا بچه قد و نیم‌قدشو بزرگ کنه تو ۲۷ سالگی.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31390" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqo9I_6A2VlECPQKqzdGAdklfyStVL1yL1o2WdpyqUrC9Q_HKNpXmCEisz_jv32adZDXVuS5Yw__2PrL4RrgAU886rS1-VIBYERoE-FyXqYfSqgl5q-XEbFDgGU1Y8aAFyWqK_oqoVQgo_aKH-Lfid3MEADznof8CaJVGLeiTxu3CjnhP9HdaMUyeH42hUl1BSX5moZHHg_ZjEOBkVYsbIU-eWbgxOX6LY12xnR__NKmgPeqB1PGzkdli-_SIhs-ILlfxoW--zPv2ZIt1t3WBO44T4WABb-JSK0UXGddLPk84VNs4-_HjVLrLhUOTiXoqB_ehAwnCYpt5EJ1i_Qqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
در هفته ششم لیگ جزیره؛ شاگردان مارسکا در منچسترسیتی درشب‌درخشش رایان چرکی و گلزنی ارلینگ هالند سه بر صفر از سد لیورپول گذشت و با شش پیروزی پیاپی در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31389" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🟣
گل‌های دیدار امشب دو تیم منچستر یونایتد و تاتنهام در هفته ششم رقابت‌های لیگ‌جزیره انگلیس؛ مایکل‌کریک سرالکس‌جوان‌نشد و در آستانه اخراجه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31388" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygbxio1Lni7n_NrdD3xk032VmuC-cX6w19r0Tuq3msQpmm15LorL1IAjcyZor0LKFg2VpLrIGoSxG20CEQZqRLPrzaIEP3PJVv5YnWP7All09KFZDPK4C0WTQIuDjScZ9mYTilH5Br5-qPPbz51DcCw9bSgHufO_j9kk4jtJxjj14PahY3dh2aRPyOI4qnUXD6tvT8NWnVnK2TFd1tGRUUHsLipyIIvV8zwwTrQ3h-lNaz2f0SLelGAFLpLPWSyj8SNZ-rj85KruNJK4ToLYPcWKoCUabBwkgVAzKKkZ0xKkQRm-DcS9OwdMP7W-gQVAIE8U0pBH5uCC8QBbS5WoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31387" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ee700462.mp4?token=Fp-PE-eMbwGHFf57XOGsF3Pi6832YXddWtIPFPFPmPItJmuDWrAZ-pihwsc1sC7ZW0mqzXyNae06L2j_y3HmtCgxiJa9UQjGscYiz33cEEIVEbozr7SkXhHh3o4udjiSJDYnSjpzIZO1yqYZCI6PGPjGlcQqwiuYZnTdzEyTjHYYywz2fz1YA4BmOUqHL2DkrQI6lc99_23KcukeqSZd1MF-JusMPB3bra2wvogVqd6sWNPI4GjCH2scFOvJp2fH4HcyCgHQA_FYcpXILQHFX4rqmPk-bnYiGmAGAnKMqkBGB_793mRaSuGOfk_8PfTQYk44kj-I2l8Wxznmck7C0xKct2i6gdD37fWgDyTQKhx1q7JVO4v7ME2UYHu1bXChRMpKpnvfzssZJTH2-En9oPEftW2lahzDhuE0Kyiz7LmnDrJFEm6fCRm3aCKmLJx_mqrS436NpAUUiw8GYLpPtaxqsEz-3WHrdDbGE9RYSo3vdCluNzt-kRBzhQvUmRQbdLKyu5kW5MvdGUyWuiu4bq5DnikN0OujhrfBc7t8EylFH1UXgIAEKX8hg6s7WTzQYrb6ji8MyEHdyCQ1YvujObAbZteUmQvR_l-ImEtl6Z-61OaCnOTIOEyuZBNDmiaIdH6eoZSBIEzLrhV4Ps_HB8BfYQcF9LxwpVLltU3oO3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ee700462.mp4?token=Fp-PE-eMbwGHFf57XOGsF3Pi6832YXddWtIPFPFPmPItJmuDWrAZ-pihwsc1sC7ZW0mqzXyNae06L2j_y3HmtCgxiJa9UQjGscYiz33cEEIVEbozr7SkXhHh3o4udjiSJDYnSjpzIZO1yqYZCI6PGPjGlcQqwiuYZnTdzEyTjHYYywz2fz1YA4BmOUqHL2DkrQI6lc99_23KcukeqSZd1MF-JusMPB3bra2wvogVqd6sWNPI4GjCH2scFOvJp2fH4HcyCgHQA_FYcpXILQHFX4rqmPk-bnYiGmAGAnKMqkBGB_793mRaSuGOfk_8PfTQYk44kj-I2l8Wxznmck7C0xKct2i6gdD37fWgDyTQKhx1q7JVO4v7ME2UYHu1bXChRMpKpnvfzssZJTH2-En9oPEftW2lahzDhuE0Kyiz7LmnDrJFEm6fCRm3aCKmLJx_mqrS436NpAUUiw8GYLpPtaxqsEz-3WHrdDbGE9RYSo3vdCluNzt-kRBzhQvUmRQbdLKyu5kW5MvdGUyWuiu4bq5DnikN0OujhrfBc7t8EylFH1UXgIAEKX8hg6s7WTzQYrb6ji8MyEHdyCQ1YvujObAbZteUmQvR_l-ImEtl6Z-61OaCnOTIOEyuZBNDmiaIdH6eoZSBIEzLrhV4Ps_HB8BfYQcF9LxwpVLltU3oO3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی از آنالیز عملکرد پرسپولیسِ مهدی تارتار در بازی این هفته سرخ‌ها مقابل صنعت نفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31386" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
