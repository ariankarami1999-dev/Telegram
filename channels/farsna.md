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
<img src="https://cdn4.telesco.pe/file/JfuyMv93vPmWeg1UJk6BDN-jkRcMQYWKhEbql625EKlJm7GhHJzMoVZD1G15vAN_9NC7Rne_-90oE9sJLnTW_3xgkd4CG058IXIiS_sabH2SC6eRxvA7Te9JwkoxqSNbWK7Eph1Ciw202CAb6yn3hQktZk9f5ExbiFIZjrMwuG4ghwzS4bPhwdm4NMmzlCVQU1m_Jp_NcnneUvQClYEm6bKYxd8aI8rlv8jx5qtkfP7BoUr3RFzKrOFU0NNDTt7WNy1fZyMBP63Rd9fNZlr4EORZ5ofW8cdpaaHaUAaGB5z5xS4GjP7mxPSBM9C2f_d9yTqr73mfp9p8ho5o-vvv5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 20:18:15</div>
<hr>

<div class="tg-post" id="msg-457806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4016a54675.mp4?token=vOd8zj0lHrH69dtOp5UqNz3HtqF9K0kZ4okWseug4zXwjAF1H5PVkg14XnedJ-CIieu6O-0mbmobM5hwi1FZAe81ukIUbp4p9p5SHbNQVOg0gZO-wPHFLjhrLE718DTKOzPySZr30xPsEjNmXAkNgfLHmozJJ9O9bLh0dG9QgihHYT7KbP6lxY3GNUh-h4zO0-ClBg5xSY6CH2MTPpuOhXrO1lofpnKYF9jHVqXMOZBkxoYee6Ke0Z5gbqu0fvsSpOHOvsUpz2B6wn5ciDc2HjDbxZdmg2dMcPoS8LwNh-0c8HC8UxcIUexGFwehWg6tXlyf8zD8VPqB69CfOR2Jfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4016a54675.mp4?token=vOd8zj0lHrH69dtOp5UqNz3HtqF9K0kZ4okWseug4zXwjAF1H5PVkg14XnedJ-CIieu6O-0mbmobM5hwi1FZAe81ukIUbp4p9p5SHbNQVOg0gZO-wPHFLjhrLE718DTKOzPySZr30xPsEjNmXAkNgfLHmozJJ9O9bLh0dG9QgihHYT7KbP6lxY3GNUh-h4zO0-ClBg5xSY6CH2MTPpuOhXrO1lofpnKYF9jHVqXMOZBkxoYee6Ke0Z5gbqu0fvsSpOHOvsUpz2B6wn5ciDc2HjDbxZdmg2dMcPoS8LwNh-0c8HC8UxcIUexGFwehWg6tXlyf8zD8VPqB69CfOR2Jfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلیلی طلا را صید کرد
🥇
سینا خلیلی در وزن ۷۰ کیلوگرم رقابت‌های کشتی آزاد جوانان قهرمانی جهان، در دیدار پایانی مقابل کرمیوف از آذربایجان با نتیجه ۷ بر ۳ به پیروزی رسید و صاحب مدال طلای جهان شد.
🗣
این کشتی‌گیر پس از کسب مدال طلا نام امام رضا(ع) را فریاد زد.
@Sportfars</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/farsna/457806" target="_blank">📅 20:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457805">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1689685762.mp4?token=C1pdUp5dEKG3s0j6whJ1m9A9DXS9th8T1WE4rTCu9fl41O5k1t1G2UYOd8hawnZHCYbR6G3mtwQbcony-Iu2fWbZwT_ANUQmmKqWhyRWhcGjH3P7PWXuHOxJMaEjJv_Su1uhYWpWvwpMftRIZ20KLUznq-Fy4ouTrrRsBUceuwDApYEihdAg2h63YHlIigbsyWzycbLucqY07tTx8hk_GM3cbGNu5jDnm9Ggv_DNxbMSxyMwLcXJKw_czUGqssZBTUaShfqSk9yb_uDqpkKOtem_gYcas-b3nxfaQSsCOq6Wzvj5-p4rJskL81WUSesrjzBffgtwxiohobiBFgSPdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1689685762.mp4?token=C1pdUp5dEKG3s0j6whJ1m9A9DXS9th8T1WE4rTCu9fl41O5k1t1G2UYOd8hawnZHCYbR6G3mtwQbcony-Iu2fWbZwT_ANUQmmKqWhyRWhcGjH3P7PWXuHOxJMaEjJv_Su1uhYWpWvwpMftRIZ20KLUznq-Fy4ouTrrRsBUceuwDApYEihdAg2h63YHlIigbsyWzycbLucqY07tTx8hk_GM3cbGNu5jDnm9Ggv_DNxbMSxyMwLcXJKw_czUGqssZBTUaShfqSk9yb_uDqpkKOtem_gYcas-b3nxfaQSsCOq6Wzvj5-p4rJskL81WUSesrjzBffgtwxiohobiBFgSPdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودروهاست
🔹
با اینکه کیفیت برخی تجهیزات پایین است اما تغییر رفتار، زودتر از اصلاح تجهیزات و اقدامات دیگر قابل انجام است. @Farsna</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/farsna/457805" target="_blank">📅 20:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZX1ZMAyR_AjVSDhXNotYslWPc51qlHdYHsrXHlNdD3nME9BM4MV6d3jWmKeEpBXOTgwqMYOwFuPBiaSYKL3yxtfbX8lTPmq3QWSXKmSFx44tcKQacTjfr_2c9DFq707iQf6amr_lNHdYza3FlORCCh2sl5bAAVI-MfgxIRJHGUwEi2OTgcQjQn9yW9GjNR10e08KsfY1u_qbaiYDrlk3XtPlfxyjbKmPU_XiPjkw6svOg7cmScVuAeIepvAOB0qnAlT-S1Ew2S54iyEHB2PAK-uj8kkHgxm_Vpi7gf-P-aPyWpy7Z0nJYkzYudxtsn8LEuR6ep1gG4S_vM6eUQ2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیو سفید ایران یک قدم به ثبت جهانی نزدیک‌تر شد
🔹
مدیرکل ثبت آثار وزارت میراث‌فرهنگی به فارس گفت که سازمان منابع طبیعی به‌تازگی نامه‌ای تنظیم کرده و براساس آن، از این پس فعالیت معادن در ارتفاعات دماوند ممنوع خواهد بود.
چرا فعالیت معادن برای دماوند مشکل‌ساز است؟
🔸
ایجاد مانع برای ثبت جهانی دماوند
🔸
آسیب به چهره و ساختار طبیعی کوه
🔸
ایجاد آلودگی‌های ناشی از فعالیت معدن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/457804" target="_blank">📅 20:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebf1a65c9.mp4?token=LD9_5KcRX3klMscxxS7PiQevEgnB1w7bm0E4vIABOjhTmUsayZCBvpso_6QkxP1kMGUS8XWtJrV3TkZYZyzHszGfkTdRkyt6TYy27KTrc5nYjKRHuIJm0zoIhb_9nbbSrBGcmCdcmW5rmjfWxwAT8GQ2GhP7RTQggFEMKk4-npNrdbPFdOYZnqZxp6HjVPAIT_p7Dw5Zfw8Py-kD6OlSiRzaWEMz4IHlbjx0hX_stP4gh4-pEl4n04URWALt-UciJ8u2v3-5_OkiOfBIiFi21ELybl_k7EzdYr2Z6rb_JH-zBugX0b-5isfeVZXEmrrQMGYtovEJeKXb7GIOb-o4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebf1a65c9.mp4?token=LD9_5KcRX3klMscxxS7PiQevEgnB1w7bm0E4vIABOjhTmUsayZCBvpso_6QkxP1kMGUS8XWtJrV3TkZYZyzHszGfkTdRkyt6TYy27KTrc5nYjKRHuIJm0zoIhb_9nbbSrBGcmCdcmW5rmjfWxwAT8GQ2GhP7RTQggFEMKk4-npNrdbPFdOYZnqZxp6HjVPAIT_p7Dw5Zfw8Py-kD6OlSiRzaWEMz4IHlbjx0hX_stP4gh4-pEl4n04URWALt-UciJ8u2v3-5_OkiOfBIiFi21ELybl_k7EzdYr2Z6rb_JH-zBugX0b-5isfeVZXEmrrQMGYtovEJeKXb7GIOb-o4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: ۴ روز بعد از آغاز جنگ، جلسۀ دولت تشکیل شد. آقای عراقچی در جلسه گفت ممکن است دشمن اینجا را بزند. رئیس‌جهور گفت به درک که می‌زند. من جلسات را تعطیل کنم از ترس اینکه او می‌زند؟ خُب بزند.  @Farsna</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/457803" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92cabaea4.mp4?token=GUbGzOfFWba7IZKMGxEafo_TS0vTnZvt_njL_t_E7GR8Aa6lEaxBpte-wz7RA27rdR3S6hAiCb_jQ8tHnNxDDS-VA7pjWVp6IuWCN7EaZ58kZVsRDFWqfJZjWMm53e-JlYtWVJU_WExzfjbr8hjPkPHw-av0Jkfrl5jtuTTYhv31ZX-2V1IX5TWKkT7AHs2IgFyJLtMca_v3Z8vwQ8H6tsO76aM61tEi1b_Gklwzb_CTn4GXQwBAUaEf2Wc73UTSwBF04bp5-VJzkSGBbjb1TxeF7rdFDxmf0V_L2Z71svRGqqjIClfgo8P5Lv78i9qK8k-Lfsve_w2exzTlLGQ1RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92cabaea4.mp4?token=GUbGzOfFWba7IZKMGxEafo_TS0vTnZvt_njL_t_E7GR8Aa6lEaxBpte-wz7RA27rdR3S6hAiCb_jQ8tHnNxDDS-VA7pjWVp6IuWCN7EaZ58kZVsRDFWqfJZjWMm53e-JlYtWVJU_WExzfjbr8hjPkPHw-av0Jkfrl5jtuTTYhv31ZX-2V1IX5TWKkT7AHs2IgFyJLtMca_v3Z8vwQ8H6tsO76aM61tEi1b_Gklwzb_CTn4GXQwBAUaEf2Wc73UTSwBF04bp5-VJzkSGBbjb1TxeF7rdFDxmf0V_L2Z71svRGqqjIClfgo8P5Lv78i9qK8k-Lfsve_w2exzTlLGQ1RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: در ایام جنگ به رئیس‌جمهور گفتم حاضرید باهم برویم پای لانچر؟ او گفت برویم.  @Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/457802" target="_blank">📅 19:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ngp5GwSnAThAn67GoAlSWeSUfjzj-fj07ucxnu9zvIvjR6Q-Cl67XPtUvD6NEFwKhQQPb_MaF28NWCIqsmSrVEjggD7HIx7EieZFRcc8j-zbLyEwuA8WdWmw1pDA-ICb_PZTCJ_2QnxlYSM08ivbYqrCur6ozC-d8z0gCzNErojsXsqq6YEYtKeVTgVVimQ1tpAErCDJ3ofmUP7gDv3FFDsvc13fcW9TQfeTPRoEzbKaXQ13WYrEf_w2b2nIOKkVR30gklZhhJod6dAmANob3K_5p7CJ9l5Y3KDKNsy9fjm_sI-crGLuJInyN-D_zBs5FDfsqVhEshOUZ24uo3sV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
در پایان مردادماه ۱۴۰۵ رقم خورد
💵
رشد ۵۰ درصدی اعطای وام ازدواج و فرزندآوری در بانک صادرات ایران
🔹
بانک صادرات ایران تا پایان مردادماه سال جاری به بیش از ۵۲ هزار نفر وام قرض‌الحسنه ازدواج و فرزندآوری پرداخت کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/457801" target="_blank">📅 19:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOW4lzEZlO-noVwVyQlWr0w8DtmEvdRnAlDYlT78j-lv_9DwGVP1WYhyC9GU5U-sRvxh76Nnm4yV-zCa9fH6HTRQZR8buKhiAgQsI1pffyUuDwccATEUzQiTfGj4HmLp9xFfK1_w9T0Qwhx8peUlMzrzIgsoaJ0bDiSKKneXTkfxOnNYqQ0uxkAaCAI_sKlawIW50mlDOS4MibReJGIp5-L9N-wF1-s4I5-qipUylmocbHvV2XObu2a8TNrDLxSnzS6xZ2f7Rthwab394yWltQzbrkDXVk91M7MwsPMo3lIqRZFGZxzbPXEZlqR3IxmCJ1dTzZX-qwmOEeKYcgUKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هوش مصنوعی را به مزیت رقابتی سازمان خود تبدیل کنید
🔹
تحول در روابط عمومی و رسانه، از همین امروز آغاز شده است. سازمان‌هایی که بتوانند ظرفیت‌های هوش مصنوعی را به‌درستی در فرایندهای ارتباطی خود به کار بگیرند، سریع‌تر، دقیق‌تر و اثربخش‌تر عمل خواهند کرد.
🔹
دوره تخصصی
«هوش مصنوعی در روابط عمومی و رسانه»
با تمرکز بر نیازهای حرفه‌ای تیم‌های روابط عمومی، رسانه و ارتباطات طراحی شده است؛ از
پایش و تحلیل رسانه‌ها و افکار عمومی
تا
تولید محتوای هدفمند و مدیریت ارتباطات در شرایط بحران
.
ثبت‌نام انفرادی:
📝
ثبت نام دوره آنلاین
📝
ثبت نام دوره حضوری
برای دریافت اطلاعات و تهیه اشتراک سازمانی:
📞
۰۲۱-۴۲۰۸۲۳۲۴</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/457800" target="_blank">📅 19:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/457799" target="_blank">📅 19:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/debac0175d.mp4?token=BUwU88JJhjMiInWrkDi2nXmqZnIFyaJX2gu85NHEsG6TMyI-ym8wXuvoDoX4cdbTVX5yWunNbS5zmi0Vq0Gs0dcfZMFcepVhQT5bMMT9SAx5Jb-wKlZooJm67V1aKpcUrp-1aYgNE5mw5FAhR-ne6vI1qDzMMv_0cocUtKXK2CBvm_8-sXZdHfH6iYGHJP9vyiocXZVMlAxjJLYxLAs3zoE5CYoKRiPXYfvb-1LXbuxbWZJMnftuS5tV-UXdNFocBDXlo2B64j4M2bjCwPePphXLKNPOgN_fTMSJu3i-b7f-DuzeqDxzmgRaDQZu3oSPVNmyFuWGDzY25g_6fYCZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/debac0175d.mp4?token=BUwU88JJhjMiInWrkDi2nXmqZnIFyaJX2gu85NHEsG6TMyI-ym8wXuvoDoX4cdbTVX5yWunNbS5zmi0Vq0Gs0dcfZMFcepVhQT5bMMT9SAx5Jb-wKlZooJm67V1aKpcUrp-1aYgNE5mw5FAhR-ne6vI1qDzMMv_0cocUtKXK2CBvm_8-sXZdHfH6iYGHJP9vyiocXZVMlAxjJLYxLAs3zoE5CYoKRiPXYfvb-1LXbuxbWZJMnftuS5tV-UXdNFocBDXlo2B64j4M2bjCwPePphXLKNPOgN_fTMSJu3i-b7f-DuzeqDxzmgRaDQZu3oSPVNmyFuWGDzY25g_6fYCZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/457798" target="_blank">📅 19:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457797">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=IU6WStDe-LJHExCVhDPQEpIxPCXh8rpvFm7O5r6z4UD-5KlPyhufuWiyo_dsU3sa27SMUzrZVORPkQsbj2wN9EMOzHSCJBZ6aKbXenERoIB5a60OyUQokV8MZFFfGH--IDmxuoUWQu47rQeMv2p2O0kco7RoySVjsC6E83yU8CMtP7jbyiEtKkv8Tk_9EnL1sgicYBM5C2PD9DWLNh8eEcOUQE2J1cI87Xk4mxBtJfBLa7T7BFuDZj5n3GAnIfI0pbtWgvFxxfxB6DeWiQyl2Y8yIlX0lDq8aXXSZSI75vrO5B6l5sFLtAMuR_qjJulHAjv4yc1vqIaSaPoJKpU9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=IU6WStDe-LJHExCVhDPQEpIxPCXh8rpvFm7O5r6z4UD-5KlPyhufuWiyo_dsU3sa27SMUzrZVORPkQsbj2wN9EMOzHSCJBZ6aKbXenERoIB5a60OyUQokV8MZFFfGH--IDmxuoUWQu47rQeMv2p2O0kco7RoySVjsC6E83yU8CMtP7jbyiEtKkv8Tk_9EnL1sgicYBM5C2PD9DWLNh8eEcOUQE2J1cI87Xk4mxBtJfBLa7T7BFuDZj5n3GAnIfI0pbtWgvFxxfxB6DeWiQyl2Y8yIlX0lDq8aXXSZSI75vrO5B6l5sFLtAMuR_qjJulHAjv4yc1vqIaSaPoJKpU9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/457797" target="_blank">📅 19:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پزشکیان: صرفه‌جویی مصرف بنزین باید از دولتی‌ها شروع شود
🔹
رئیس‌جمهور در جلسه هیئت دولت: برنامه‌ریزی کنید که چگونه می‌شود ماشین‌های دولتی و مصرف دستگاه‌های دولتی را کاهش داد و میزان ترددهای ماشین‌ها را پایین آورد.
@Farsna</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/457796" target="_blank">📅 19:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6892fb9e5e.mp4?token=cxL3hstEfa3wRTWAZ_DTflO398XBuNtS3ACFKkEBHUvMuP894M6V1GFrUStfn_r877Tu3DT7kZA1-AFAFcoZBYLiMLQT6OIHX9XRjtvcYr3HKDY8CJX0irHFXbcUSfIDfZlMeDtbwras1TT4OTcZPWkpPWHI8rYNNbJ-nj1MpjxAb5CKidlinx081-oaBcmJaQ87XAyWlgwzjVDQA7LPpqia1rWy30ieFm5TP8Q08ltCHF9aNBn2bKKjdRExEnOwzwhECgrCvE3aCeRmm3pVH-KJUjAfJd3BHLn513P6PkP6qWZi1PBR4jN0gYy1T1uqeh_0pG7e825iSHpBt4GOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6892fb9e5e.mp4?token=cxL3hstEfa3wRTWAZ_DTflO398XBuNtS3ACFKkEBHUvMuP894M6V1GFrUStfn_r877Tu3DT7kZA1-AFAFcoZBYLiMLQT6OIHX9XRjtvcYr3HKDY8CJX0irHFXbcUSfIDfZlMeDtbwras1TT4OTcZPWkpPWHI8rYNNbJ-nj1MpjxAb5CKidlinx081-oaBcmJaQ87XAyWlgwzjVDQA7LPpqia1rWy30ieFm5TP8Q08ltCHF9aNBn2bKKjdRExEnOwzwhECgrCvE3aCeRmm3pVH-KJUjAfJd3BHLn513P6PkP6qWZi1PBR4jN0gYy1T1uqeh_0pG7e825iSHpBt4GOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به سپاهان توسط آسانی در دقیقۀ ۴
⚽️
استقلال ۱ - ۰ سپاهان @Farsna</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/457795" target="_blank">📅 19:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2507495102.mp4?token=U18bC6wXsDlFE6t8Ax4TnguWj7KPVkBO7PP4-Tf218aoDCUJ7Z7rxV5nQhydddDK_2WppACSN-PXRimWmsBjXRWnllriY-05tjJwQJFU76N4GeDnhnYr1W_HIlv5Fo7idxYh1503QqvJ5OohN5u5qlBpHQBn_J9jttprPx_2GJRsAPL_nUKLflCiGteUHkEv0whDTZgbAR55mojlMSuoug5QME7BpmRlfqBnjANZG7rG5V4skpQzz5FqHJJ94sc-H1dexFfixouYrn9H1rQYdmFIZWCSR_MOr36bpvbZUJrkiJRvKqbrs3IW_PUfhoOou83CaiW1vIrzBjAv1baJAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2507495102.mp4?token=U18bC6wXsDlFE6t8Ax4TnguWj7KPVkBO7PP4-Tf218aoDCUJ7Z7rxV5nQhydddDK_2WppACSN-PXRimWmsBjXRWnllriY-05tjJwQJFU76N4GeDnhnYr1W_HIlv5Fo7idxYh1503QqvJ5OohN5u5qlBpHQBn_J9jttprPx_2GJRsAPL_nUKLflCiGteUHkEv0whDTZgbAR55mojlMSuoug5QME7BpmRlfqBnjANZG7rG5V4skpQzz5FqHJJ94sc-H1dexFfixouYrn9H1rQYdmFIZWCSR_MOr36bpvbZUJrkiJRvKqbrs3IW_PUfhoOou83CaiW1vIrzBjAv1baJAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول استقلال به سپاهان توسط آسانی در دقیقۀ ۴
⚽️
استقلال ۱ - ۰ سپاهان
@Farsna</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/457794" target="_blank">📅 19:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
انفجار در حلب سوریه
🔹
منابع خبری از انفجار در حلب خبر دادند، ولی هنوز جزئیاتی درباره علت انفجار منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/457793" target="_blank">📅 19:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDhO8n2U_oKqPrW8iW3SSR7gB3r8o0gd1pA_CX5lpfdYqDUnz1nBbYB_CkCluaXVwBsCNckebSvNU0v4PtpUg_I8Ai0NimTxs7ipVK3wxdpVvCqlzZhqAe6JGVMAXDFx94ruBAddViSGusUpqEyjvgqzHkucd3LFS_BGBQGBj5wQD0xdEh5nYNUBFEznw8SQPV-qv3jtFKOUDqYdaTuYbgjed0kk_qsIza2adyQMRI9Ea9CBBvN24bDul8kQnXNqKWo9a-nR0tmUTi5Nuluo4Wd8R03RLT4RAxS1xR5wVrpeO3v9uf9Y05mIczUJLREkqDA3KjM37rT8zKka-6i_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس حشد شعبی: رهبر شهید وجدان‌ها را زنده کرد
🔹
مراسم عظیم تشییع پیکر رهبر شهید در عراق، رویدادی پرطنین بود که جایگاه والای این شهید والامقام را در سطح بشریت به اثبات رساند.
🔹
رهبر شهید یک امت ساخته و وجدان‌ها را زنده کرد؛ مایۀ افتخار و عزت است که امروز بایستیم و یاد و خاطرۀ آیت‌الله‌العظمی خامنه‌ای را گرامی بداریم.
🔹
کسانی صدها میلیارد دلار هزینه کردند تا عراقی‌ها را مسخ کرده و هویت آن‌ها را تغییر دهند اما تشییع شهیدخامنه‌ای در عراق ثابت کرد که ملت عراق به هویت اصیل خود پایبند هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/457792" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDX97VHhqetZj58yELCmXdwH51W8F7l4PAa9VtF_VQdPqGS8rv1QXDDdJUgsvsJfjy0cT1kW4T_egAL9P4pGbrn9ld3JZ4W5o-wJYeiJWqV5nDqfMWdjJQVLQvrL2G7BGrDzivJGcxNhKCQIcvmjsW4S8TpFY1W_sQHQoD36p8AGyxTTZKrB6igRrQQ7zwwNs_DL4NlyZ96CJuNF6evSVCG-gOfUiH8aGqE4cOjXurtMyA66b7oegtvTaHTfggNNg00DztPv7dpUOEcdbmAtpsXbtWaJQfcssPV9yLvhK_2FDKJznFZLj826Ev3CcbVLxIg2-qVYaKhNEmF-00J89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جشن «امت احمد» در تهران برگزار می‌شود
🔹
معاون فرهنگی سپاه تهران بزرگ جشن امت احمد با شعار جهان در آغوش رحمت از میدان هفت تیر تا میدان ولیعصر(عج) تهران در روز یکشنبه آینده برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/457791" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d29962d8d.mp4?token=fog4VqTDOoQ8wdHp3s4vaA7R_iithNAZrYsoqwT_ghLKeQyE0jJP5fXZyLQTWc5RXHnorRC6vHjN0vao80-aJ6DBeyiPLk4pa0O_8Mtl09MlMxrrFsG2_GKTSD6xmkdhdf8CTijh6DbQquPys411TqKjY8BSjCplR15qBmeFgLiZUuWg39QMqZWcomPr3pex4JfkndjDkQ1I1lunNw07YB7Cj63eA2525hWu7Ez580RZgCSOknwUC1Qt9W6G17eMVipvmol2iLFKWIn6CnClE8Jv-co8R2NcYS5R51XQGJmyd1aGdcq6JV7iL2uRChdeF_edanP6ys3UMoBjFzBsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d29962d8d.mp4?token=fog4VqTDOoQ8wdHp3s4vaA7R_iithNAZrYsoqwT_ghLKeQyE0jJP5fXZyLQTWc5RXHnorRC6vHjN0vao80-aJ6DBeyiPLk4pa0O_8Mtl09MlMxrrFsG2_GKTSD6xmkdhdf8CTijh6DbQquPys411TqKjY8BSjCplR15qBmeFgLiZUuWg39QMqZWcomPr3pex4JfkndjDkQ1I1lunNw07YB7Cj63eA2525hWu7Ez580RZgCSOknwUC1Qt9W6G17eMVipvmol2iLFKWIn6CnClE8Jv-co8R2NcYS5R51XQGJmyd1aGdcq6JV7iL2uRChdeF_edanP6ys3UMoBjFzBsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز دور نمی‌خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/457790" target="_blank">📅 19:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERgHupG43Qq_lxMxmvuvFBoe7p5K6NZeltAN1AGSFF5gtlDwJHwG_fhTeKdiw7qwg6bln9G_LeJd_vfSe46qDu0YiKWZ2u-iqzL4RFvMcpm8P8oNWouOwu08d27Nx3nzBvd5Vc7qU7ERzn1l9RSkClLUq-R_EdnOJatApaHLDa9PbS4SanZRPnO27Elr5xHBSHXc_kMEHOqSbniiG1c6TvRgMItBnpFrOHQxMQ1QfNFfYnEXypavwF1Yfh6DK7USxBZ8ZIbDbDooG6RPAp0HQpAOBnHzicW4ZB4MGXnwwHWT8GL4YqT3GA9-d4o8kHxZ-Yu7D9Qorce6NpqDHtihWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: ما خود را برای تهدیدهای ۵۰ سال آینده آماده می‌کنیم
🔹
سردار ابن‌الرضا: وزارت دفاع با اتکا به مدیران توانمند، کارکنان باانگیزه و نخبگان متخصص، مطالعه آینده را در دستور کار قرار داده و مسیر پیش‌رو را بر اساس این مطالعات طراحی کرده است.
🔹
این همواره مورد تأکید رهبر شهید انقلاب اسلامی بود که باید از ظرفیت‌های مردمی به بهترین شکل استفاده شود.
🔹
آثار این سرمایه انسانی را در جنگ اخیر به‌خوبی مشاهده کردیم و بخش مهمی از توانمندی‌هایی که در میدان به کار گرفته شد، حاصل دانش، تجربه و تخصص همین نیروها بود.
🔹
ما در این جنگ به صورت نامتقارن و بهره‌ور جنگیدیم، در حالی که دشمن با هزینه‌های بسیار بالاتری وارد میدان شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/457789" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مخابرات: ریزمصرف اینترنت مشترکان قابل‌بررسی است
🔹
در پی گلایه مشترکان، شرکت مخابرات ادعای کم‌فروشی اینترنت را رد کرد و گفت که مردم می‌توانند با درخواست ریزمصرف، جزئیات مصرف خود شامل زمان، میزان و مقصد ترافیک را بررسی کنند.
🔗
توضیحات مخابرات دربارۀ نحوه محاسبه مصرف اینترنت بین‌الملل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/457788" target="_blank">📅 19:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طرح امنیت پایدار تنگه هرمز، اختیارات ویژه به نیروهای مسلح می‌دهد
🔹
عبدالجلال ایری نماینده مجلس: طرح امنیت تنگه هرمز اختیارات ویژه‌ای را به نیروهای مسلح اعطا می‌کند تا بتوانند در مواجهه با کشورهای متخاصم و عملیات‌های احتمالی در تنگه هرمز، اقدامات لازم را انجام دهند.
🔹
پس از تصویب نهایی این قانون، شاهد ایجاد سامانه‌های متعدد نظارتی خواهیم بود که عمدتاً با نظارت نیروهای مسلح اداره می‌شوند و حوزه‌هایی همچون عبور و مرور دریایی، تعرفه‌ها و دیگر موارد پیش‌بینی شده در قانون را پوشش خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/457786" target="_blank">📅 18:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGEGe7M1c68dN3yGcxv6Xy0lmLhN8_Y16q0wC9d_ERMRA9_2jx8f1v88IMpZbjJDx83KRLfrFt4yMrHbP_bHhoypDTcOFCDOn8cD_ltWbyr7JELEUyCWFqxgXBvr6S8UUO_OkxXjudWMw7f3wmYvZ_soqWlTuaJY3kX5eaZkUh3wXKY2Blw6hav5PbyuJ37MlBL9j5lB1Q2FcQ3g9m2hoNEiQxTqQFMYKfVI470KC5fMHTYb5qzEpcewM2A6jN9l_qnKIcYJxcCgC7tSAbMtEhfR4xVkGz2Xn4daRQ3vMJxIrlViIvyk4l1qkpN4tfAfYtcBYtmhHekV-bj4hzapcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار گذرنامه‌ها ۱۰ ساله می‌شود
🔹
کمیسیون امور داخلی مجلس با اصلاح قانون گذرنامه، اعتبار گذرنامه افراد ۱۵ سال به بالا را ۱۰ سال و افراد زیر ۱۵ سال را ۷ سال تعیین کرد.
🔹
این مصوبه برای تصمیم‌گیری نهایی به هیئت‌رئیسه و صحن مجلس ارسال می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/457785" target="_blank">📅 18:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnB6Ya_W50y-i49pOa9_yOep7sPwGzBs9w1B8wX-rKCGBlgTuaV9Md8rhCNYKCNq8kvkgNChNmWp2rLe6IriRKlWzxlmEkPZtmVrWvDDT2IwTVv1XahhSr6-HFGZ9XvCtsZKDGWwJ3ZqP0BMmnL5wuKk-dZ74Y43HfaQtTY9nb1wx8T0fYyPRjk8IF9A1jmCtJ3m3uZOkejuEiL9I9J5XM117QIeEooXpMAMtXnULkyoreQBPBYVgvl4Qt2xJEw_qfPCT7sttodU2zS4NENHD5iT-jSYlxPjHDNLJEKX9qF8l7R7zAhxV3qq1-4nKtnjwHLTPZd2LEf2DosLRG3cgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیتۀ انضباطی به استقلال و تراکتور هشدار داد
🔹
استقلال، تراکتور و گل‌گهر به‌دلیل هم‌زمانی بازی‌های آسیایی با نخستین دیدار تیم امید در بازی‌های آسیایی ناگویا اعلام کرده‌اند بازیکنان خود را در اختیار تیم امید نمی‌گذارند.
🔸
کمیتۀ انضباطی فدراسیون فوتبال این اقدام را تخلف دانسته و اعلام کرده باشگاه‌های متخلف جریمه و بازیکنان دعوت‌شده نیز ممکن است از مسابقات داخلی محروم شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/457784" target="_blank">📅 18:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تصویب دریافت هزینه خدمات از کشتی‌های عبوری تنگۀ هرمز در کمیسیون امنیت ملی
🔹
سخنگوی کمیسیون امنیت ملی: بر اساس ماده ۳ طرح اقدام راهبردی تأمین امنیت و پیشرفت تنگه هرمز، در قبال خدماتی از جمله خدمات دریانوردی، محیط‌زیستی، سوخت‌رسانی در شرایط خاص، بیمه‌ای، ایمنی و سایر خدماتی که ارائه می‌دهیم، هزینه دریافت خواهد شد.
🔹
این هزینه‌ها از کشتی‌های کشورهای مجاز به عبور از تنگه هرمز، به ریال یا هر ارز دیگری که مورد نظر جمهوری اسلامی ایران باشد، دریافت خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/457783" target="_blank">📅 18:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آمریکا: خروج از عراق تا ۳۰ سپتامبر تکمیل می‌شود
🔹
خبرگزاری آسوشیتدپرس به نقل از یک مقام آمریکایی گزارش داد که آمریکا در مسیر خروج تمام نیروها از عراق تا ۳۰ سپتامبر است، که به حضور نظامی در آنجا از زمان حمله سال ۲۰۰۳ پایان می‌دهد.
🔹
این منبع که نامش فاش نشد،…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/457782" target="_blank">📅 18:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGGCaq0vcLgDF39tK8pxFmdkON6IgGPZC3byR6y8ZEsxyuq3sy1oF0D_83NSNuzFwBgg2FK0k0F1OAWSkMI4iOBxMAvLyrm-bj0IBvypt12c5poa1QsLu_AeN7PSPMcRfsJWy69nPTETNAdxEoZ6LsXAgNhr1OXrYJ-zWC0t3NzElq5uTxDyAb3MuPmgHUZHMI-T3Fk4PbMDL2D7ZCqNao6l4csRmNB-a0M9OdXoNSqEMLOjs0MNOZmayQfqKTEMukQ-ODiiYjCrWaAyd0oQCbZAOrBmv-YkQb-fNFagW9_iKuVL8ABbeZEQdUz9cPeWMyt8mJaU9Ht4uXPM5rOfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس نهاد رهبری در دانشگاه‌ها: تخلفات دانشجویی نباید بی‌پاسخ بماند
🔹
حجت‌الاسلام رستمی:  اگر تخلفی در داخل دانشگاه اتفاق می‌افتد، باید در همان محیط دانشگاه و براساس قانون رسیدگی شود؛ این به نفع دانشجو و محیط دانشگاه است.
🔹
مسئولان وزارت علوم و وزارت بهداشت باید به‌صورت جدی پیگیر اجرای قانون در محیط دانشگاهی باشند و اجازه ندهند تخلفات بدون رسیدگی باقی بماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/457781" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54c909067.mp4?token=ItP5YQGpguoJx8gsadd2stCc9a6BV4-ohycfMoS0wVcOFJ9CFXHhN9Oc-adIoSQ-9RIhPL1Uq2Kip0lAucrlmtN4KAEPvdNqV0Y2ud9IruW2hHFhDITihSoVtvIZTnwSyRdGfiskLkWzc73EqRH4Vua_p1_AycHKhTH9Skrs7ob9HlxMLRzUQARttMSWfedXphPu-Fbn6cMqPbEeCNeOenJVFKBPeDfydbPemlOTvQmw1P4iU74_kbTrG1wK_3ZZ3HhvbC8t1KjCT8-7_ToTPT4EYE8Dv_x8bgcXcOvyxeYL4IJuGi2JELT5-djj7crcj1H1NgTitkqT55vDXGmefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54c909067.mp4?token=ItP5YQGpguoJx8gsadd2stCc9a6BV4-ohycfMoS0wVcOFJ9CFXHhN9Oc-adIoSQ-9RIhPL1Uq2Kip0lAucrlmtN4KAEPvdNqV0Y2ud9IruW2hHFhDITihSoVtvIZTnwSyRdGfiskLkWzc73EqRH4Vua_p1_AycHKhTH9Skrs7ob9HlxMLRzUQARttMSWfedXphPu-Fbn6cMqPbEeCNeOenJVFKBPeDfydbPemlOTvQmw1P4iU74_kbTrG1wK_3ZZ3HhvbC8t1KjCT8-7_ToTPT4EYE8Dv_x8bgcXcOvyxeYL4IJuGi2JELT5-djj7crcj1H1NgTitkqT55vDXGmefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تحلیلگر بی‌بی‌سی: نه تحریم و نه جنگ حریف ایران نشدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/457780" target="_blank">📅 18:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">۷۰۰ پرونده تعهدات ارزی در دادسرای جرایم اقتصادی
🔹
قوه‌قضائیه: تاکنون ۵۸۳ گزارش مربوط به رفع تعهدات ارزی از سوی سازمان بازرسی به شعب بازپرسی دادسرای جرایم اقتصادی تهران ارجاع شده و با احتساب پرونده‌های سایر شهرستان‌ها، در مجموع ۷۰۰ پرونده در حال رسیدگی است.
🔹
در بخشی از این پرونده‌ها برای متهمان پس از تفهیم اتهام، قرار بازداشت موقت یا وثیقه صادر شده است.
🔹
همچنین در ۹ پرونده مرتبط با استفاده از کارت‌های بازرگانی، ۷ نفر بازداشت و روانه زندان شده‌اند و میزان تعهدات ارزی تعیین‌شده در این پرونده‌ها بیش از ۱.۷ میلیارد یورو اعلام شده است.
🔹
در سطح کلان نیز پیش‌تر ۹۴ میلیارد یورو تعهد ارزی ایفا نشده شناسایی شده بود که نزدیک به ۲۰ میلیارد یورو از آن با پیگیری‌های انجام‌شده تعیین تکلیف و به چرخه اقتصادی کشور بازگشته است.
📝
قوه‌قضائیه اسامی برخی از این شرکت‌ها و افراد را با حروف اختصاری اعلام کرده و گفته اسامی کامل آن‌ها را بعد از قطعیت رای اعلام می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/457779" target="_blank">📅 18:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97563b435.mp4?token=tTS-eEw-LAddGqEpvyXXZd7FnBdfKUnV5Hgd3mEZNGQedw6c3ykCkYGI5EnegLCNjqLp3tnSd74qpJcXJMM_KqFH9r8yCo5ony_RvB6RPGlbFgfWJTzxRH0Dszaag0XlU9D3d28DAgN_f-Ec98w6ItnedrXTYuJy_2akegXwCn8ntn1WbsY0HwnxufW2ZvPB-ff7uNtkAkk00JcKeFJAftJ6chUuE4CxuLJxjm3ulo5b8hGtoxu1QnZ3D375S8saGmUGyhfyAaGsN45_oxvkjjdcvvmZ6GdYxNVQyvJO7hVR8ztoiCgVdyqe2JPLvD0Ko-KyVmQe5L8w_dSogTzE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97563b435.mp4?token=tTS-eEw-LAddGqEpvyXXZd7FnBdfKUnV5Hgd3mEZNGQedw6c3ykCkYGI5EnegLCNjqLp3tnSd74qpJcXJMM_KqFH9r8yCo5ony_RvB6RPGlbFgfWJTzxRH0Dszaag0XlU9D3d28DAgN_f-Ec98w6ItnedrXTYuJy_2akegXwCn8ntn1WbsY0HwnxufW2ZvPB-ff7uNtkAkk00JcKeFJAftJ6chUuE4CxuLJxjm3ulo5b8hGtoxu1QnZ3D375S8saGmUGyhfyAaGsN45_oxvkjjdcvvmZ6GdYxNVQyvJO7hVR8ztoiCgVdyqe2JPLvD0Ko-KyVmQe5L8w_dSogTzE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه: مراکز کنترل پهپادی در شرق اوکراین را شناسایی و منهدم کردیم
@Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/457778" target="_blank">📅 18:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyQzXXZ16x3-JBW4L052dGHPAaThB7-pH1RIw7tthzOT4jcx27V8bccc4L5Fnp3ZtGpflXqaX8jOtiynncI-tJBrS72zbtPp_k3Uj9mu6pEApyKxTzbwh5lBn6t3Btfd_tcgYlvcZSNwUsFGKiZ07o9LLVvDsKAAR3QSMpAp_JI0ilu5yPpDz3vfzyjqOuieU5yMyes6R8k2sZH0fn_Dj_H1yZGs_QyGKhYfbbhRG19TKlaHCfutDX_Ghyl8LehrDlc4fT9uFmO25dtmGsoBOqsc579hsDi7EOAJ-U8rXZ9DVJIVp06Gyhld8cJKk_ueiJDr5riysQlUEIVgDYJx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برداشت رسانه‌های آمریکایی از سخنان پزشکیان: ضعف و اختلاف داخلی
🔹
پالسی که منابع خارجی از سخنان پزشکیان مبنی بر پایان جنگ از موضع قدرت دریافت کردند، بر دو نکته تاکید دارد: اختلاف داخلی در حکومت ایران و اتخاذ موضع پایان جنگ، همزمان با افزایش فشارها و تهدیدات ترامپ.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/457777" target="_blank">📅 18:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye28oKKV85KDD9dnoSiyjB6oebkReuwhT0YVlPKH-MVnZ2riAxoRBKB1Rfakc1jFOPMyVz0wduWTp4FxahZg6RSGsVsS3jEVkva2t70somDRtU9zLAIkdIIsrEZUWY5Y-ph1NqovNYoaRn4Nqwvdy1aVtbolQGcqr63XnHx1-QL-XzstKaHIk_sOBEbb1ICgrUKfEgaWcVUANqhyLV0Ii29GKbvwYzs9tUlrMtRov9hZb8QzSEvDOP25zstMkfY8h-DzBVqVPB7U8lqovslyc2GP12yQFsIsdIvC6FEc9PrtUUpOkXpDCK9PeJ24-SY9qIJkxLnvNvzlJO5OkX16TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: فشار اقتصادی علیه ایران مثل بومرنگ به صورت آمریکا می‌خورد
🔹
واردات گوشت یخ‌زده برای کنترل قیمت گوشت؟ باشه، شاید جواب بدهد.
🔹
اما برای اوراق قرضه چه نقشه‌ای دارید؟ می‌خواهید بازدهی یخ‌زده وارد کنید؟
🔹
برای مسکن، خریداران یخ‌زده وارد می‌کنید؟ برای چاره‌اندیشی دستمزدها، فیش‌های حقوقی یخ‌زده صادر کنید؟
🔹
یک سیاست خارجی یخ‌زده و بدون ابتکار، اقتصادی یخ‌زده و راکد به بار می‌آورد.
🔹
تنها چیزی که هنوز در حرکت است؟ بومرنگ ایران که به صورت خودتان برمی‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/457776" target="_blank">📅 18:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUH4fatoxF845QWqH4cDqmSbafJWpu2WrLTGLgIvFo_uKvwR2QB9d92Blp21EKDDD7D8iSXBzCAdIaTwLsJf74bIM3cxel9AMmIKXUn1uFHFic7a5aFxGuE_nl0AOj-NsPRU1UOIkhgwy4SgalwjVsbps76a-1KhJgjagPsPDvQ_-vcHZI65JL2P_KPKyB9SLDZGf51DzCtK5ZTd0NEG8KR6Mu8ry5vKyD1VkQits7_gaJ-tdCH8NoWJvIqVeKHM6XEseecQQ29veSBHA7I_dtBrqhS0AB1R5ONpbm60tjY6hr8EWQBqiMP-toYmW6o3ncFwrzwkvy3cxuC1UD5A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نظام دامپزشکی: فعالیت پت‌شاپ‌ها غیرقانونی است
🔹
پت‌شاپ‌ها در کشور به‌صورت غیرقانونی فعالیت می‌کنند. آن‌ها اجازۀ فروش دارو و مکمل‌ها را ندارند.
🔹
درحال حاضر اتحادیۀ گل‌فروشان, آرایشگران و بعضاً اتاق اصناف برای راه اندازی پت شاپ‌ها مجوز می‌دهد، درحالی‌که طبق قانون سازمان نظام دامپزشکی مسئول صدور مجوز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/457775" target="_blank">📅 17:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uky4plHUEuDaBMWz9qzDivxiqoM9zAgdKWtQYwNLJFOud8-AQhQRl1VnPpetfLGd8s961DHHD9XvtXNRxKjp11V3yCareIx-8mEU6ccO6i0Lb-_26GlRamCoLg_kY7FvYmZyIwDA-e_xLCfaZeG-GA-5nxamOFOpeg3zoStuKDpSgbnYcVbRK-WCM7o7CY0lnkwv0YL-tvWvNh8ij752EQDarhAuJbPwLTil4HqKJm3sGmYgHMGWbjACkFjS9SrLs5A2wt9NP7_9hj86cxzazgjhv3Gs23wY5UoqiPrMcUGorI1AGfJIz6DjHCa2RaES_Qzqp0wScFMulVtw6UK4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
پیشنهاد ویژه ایرانسل به مناسبت هفته وحدت
🔸
ایرانسل به مناسبت فرارسیدن هفته وحدت و گرامیداشت ولادت پیامبر اسلام (ص) و امام جعفر صادق (ع)، بسته ترکیبی تخفیفی ویژه‌ای به مشترکان خود ارائه است.
🔸
این بسته ترکیبی، شامل ۷ گیگابایت اینترنت به‌همراه ۷ ساعت مکالمه ایرانسلی است که با اعتبار ۷ روزه از زمان فعال‌سازی ارائه می‌شود و مشترکان می‌توانند آن را با قیمت تخفیفی ۴۵ هزار و ۵۰۰ تومان خریداری کنند.
🔸
بسته ویژه ایرانسل به مناسبت هفته وحدت، از ۳ تا ۸ شهریورماه ۱۴۰۵ قابل استفاده است.
🔸
خرید و فعال‌سازی این بسته از طریق شماره‌گیری کد دستوری #۵* یا مراجعه به سوپراپلیکیشن «ایرانسل‌من» امکان‌پذیر است. بسته ویژه هفته وحدت، در طول این هفته، به تعداد دلخواه قابل خرید و فعال‌سازی است.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/457774" target="_blank">📅 17:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457773">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxqpQegpgZEix7yogdh3UkjVpEGqer3t5XWziHFjRmS4qgg-_D1F0A0xG-hEbibtcNqXCFfjil5BPOu5t-Sn3rJjgMbAymghFV3fTN5Nxo6p89cct8_-5Avt--Gfpi0sCwd3dVtFEIc_nAqjvU4nyPZWfNW7RrFscDUZ-6uX_nGKpEBONC8aftlKDu7HZZd-aiUNPyEaG6r8cP684SGDy4yvEvJpFqKku6M1T-EBIoBYEHdOVrBEU8mQyaQKoGaK1kg4g_qIrwdCnDTSgtHeFkAh1yyzgMdT1DI6cYuxHBz0zSVZ7UEeNyVtFCemIw0De0Lq2GsHJmel-Irx48y38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش‌آفرینی بی‌بدیل
#بيمه_البرز
در
جهش
#توليد
و پویایی اقتصاد پسا
جنگ
شرکت بیمه البرز با محوریت
#مدیر_عامل
این مجموعه و ارائه محصول نوآورانه *بیمه زندگی و سرمایه‌گذاری پروژه‌محور*، موفق شد ظرف دو ماه بیش از
۱۵ هزار میلیارد
ریال نقدینگی را جذب و به شریان‌های تولیدی کشور تزریق کند؛ اقدامی کلیدی که در شرایط حساس پساجنگ، نقش بسزایی در احیای چرخه تولید، ایجاد اشتغال و بهبود شاخص‌های اقتصادی ایفا کرده است.
مشروح خبر</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/457773" target="_blank">📅 17:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/457772" target="_blank">📅 17:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28d42a7cb.mp4?token=NVdC7eEssV4udGVlMOuVLRB5zgCL60RkkBzt6DUC3KgAmgPwfBpisAV0b0QiF9j6nt9hL4_rPkD2RnRoFzMqEmZwZiiGs3OsPNQVrALKOphzodmNzuhpjJ5lToyF9lCr6p5zf7RgTS6Oqb-YlAXJjuVZnj5NPy6w4kxkPwSpobmmXwVvxm_cBp1biAnM5coR3Je1Qi4ewACg8CjbtOmSFcxxmTKbi73Fs6E8IFlxZJkGKn4I4LtFgPYof2XD1c_0afGuP6czJB7VUv_IjHIU1shHLrBQXSK1IIkvphWquEDOCLpE9k5hSo37nyFEjgTYoVZc2g79Y0ZUMhbWKTEmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28d42a7cb.mp4?token=NVdC7eEssV4udGVlMOuVLRB5zgCL60RkkBzt6DUC3KgAmgPwfBpisAV0b0QiF9j6nt9hL4_rPkD2RnRoFzMqEmZwZiiGs3OsPNQVrALKOphzodmNzuhpjJ5lToyF9lCr6p5zf7RgTS6Oqb-YlAXJjuVZnj5NPy6w4kxkPwSpobmmXwVvxm_cBp1biAnM5coR3Je1Qi4ewACg8CjbtOmSFcxxmTKbi73Fs6E8IFlxZJkGKn4I4LtFgPYof2XD1c_0afGuP6czJB7VUv_IjHIU1shHLrBQXSK1IIkvphWquEDOCLpE9k5hSo37nyFEjgTYoVZc2g79Y0ZUMhbWKTEmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتند قبل از رفتن به اینجا اشهدتان را بخوانید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/457771" target="_blank">📅 17:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0ZlJ4tQMk8UOaeFuTcyDCJs6ajBbnu0GFtIuDl-dhP6AOGUGi6jfOIkmg6Muf96x5nclwFVfVKXMR2q96BsnoxsrPb_hqKBt--Cx-YwQ58fApLODpDt8T4q0qpSplBnkTtHGY-VbJuOjlKi4vb4xQ0RpUPf5j6ZZtQK-08zSF4cXhg_pC-0JyxtFvbfZe5h0KOLHcF0u-RpXo3I46aiPOj_1TCmz6eUnOUkiBLvY_zlBKP5m_UMYuMQaS4BCBYWoyOCJ6hrBTw6v-H433aME-Zfo4uj2usNtjcwuCLzc4pFRIXc1AKtJh01lI8C_8s0O09Wob-TcEqjGOeMfts9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_M5Lc4yzGKlfjvdz14nJnjxqmDFiWk_vivtAKU_Fiv36L-fZSIEBvOJdWv4y2TAIY9vJLd4P7HCMMPePYsED3ZnS5Jr0FcV852qRqCr03R0WRFHPDySbNyXPGdv03BarSVkvr9qcGdBLFSAbOyAfIcJF7LuSKGw1jptggHNqgBn6AnLROehNiwC3fiN0hcuXm15Neqy2StQ2khRyA9A_ytveuIGZewTA9XNwnukIi2IjQtpjQARKRY3rTRMRx3ljVr3l2dvq6GV0FmdUQkL6kj8XJththfyajxG3We1qegUSOxwEjjRRNSK4gUiOdZVXhtVczvRnIajCEP-RP77rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZqFP4uuyFJ8uboUmBP9cVWXhU3LUEshKhEx-IV2X7JCRJiFsZykfKiK7kN48V_Z-VOSb2OPWO1TsIPy6ul4j-1Cw7M-d_A9MSOiVvYSFtyij9z2oelp1m0ivMUNQMiwOqhCF20VN4bhYyyYg_daGbArSHzPNmkbwomnemuOslnblJDTfN0Fk70g7VtS2MZF0riYenkakKe3PV4qRAa5nKcTIVGORQ4YGnkxwhMRxjwm6CDcD51aixNAprabgjh6icXf0j7trihossKRb5iZUjvwI8p7onV69BASOTuc1bugwTLGgL6vlwhyF7yJzdwuAa9E0OJj9HG42HzSH5FSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T43BXsyooZfHPtk_NyJzifSQh6lysz4_OhJ-tj6z0uEbpGJT9wLD36UT4vQO64H3ZDgBb0dRlZ-3kQcGwNCvgJBDDBEmo8yjmUjfn-gtuUeaCiCnOjWs459TTbjQ4Z9v5Kb2GKsLid-DZDbvEfMpD3Z6xbJufAEHcJjNtMprFsz273a01VaPkySX_MAuGjdiwPNae56EETkPOVpDW8ma4-K81KeNWtzb_vlKapPDg5Xi_anQo1cmlgUSAYhvx4nkG-pqQ6J6Vbuj9mGWohEHmJDJNBb39WUV2SgDxZj0sYRGpfDHubU2eQXiN1gqv1nGAwVtGlb3FR1WEOntH5TS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7-FzBfTVpTEK_rnIRvJ19A25Z6H4cbB5e_xkIhNHWbdRELzTt4FHnIrwbm47PU6r7lcFhjdR6bZ3x6_j-DomrrUe_rQC1gVNTlq_eA40u7Ua67Yt-sfPhdYaFA85nSxjoqdtiYrPNiuKxKSJTzIeaez3Klg5FOqPEbFdjZYOEqKZGfBjUImpT2gLwsfMCyroZXgiI5tZbvjAosf1KLYm8kNBR4kvuiRLxFi3FPunJWGkAV5H70AOkvpqhqXr_WXBsHexVpzMn62FuW9Dj-l8w3W7n2LxWHZg8EQUHlmF_I-40zIaveK5A6NyENF_bNizTuG_1K_V2rarOIFJdvHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjDzVG9oXm2Unz_TNflwVb0h4TG4J1tuBNBVZF4V_Itto1aR3mTMxNbSMkq5lq-gmYxn4M8ckCU-emnkOcXMDkoaI2zjSsECptGoo-Zm8FFm5rtq76MI6CIhxbKbsrslAjz7Tjwg3cQJELofmgXNpiM9DDyJ1LRVM4jrBElh4b_lawrltr3MO82GCjLAOsnb8wUGKDk_Ao_jOFfvuOmGy6mOgcMjyM7g8lTRsVgza5yTJCaJryyYQmbb8UNXnz8l137zAiy8IsEKkRi4vAga35lCnvBmWwtN_CXT7z2fOTpy2I6TYYl7HRGMfWUOkZRSafRMvqB2HHY3axZlQH2CVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار هیأت اعزامی رهبر انقلاب با رئیس الحشد الشعبی در عراق
🔹
الحشد الشعبی خبر داد رئیس این سازمان «فالح الفیاض»  امروز میزبان یک هیأت از جمهوری اسلامی ایران بود.
🔹
به گفته الحشد، این هیأت از سوی حضرت آیت الله سید مجتبی خامنه‌ای رهبر معظم انقلاب، به عراق اعزام شد تا از حضور مسئولان و مردم این کشور در مراسم تشییع پیکر مطهر رهبر شهید انقلاب قدردانی شود.
🔹
هیأت ایرانی از مواضع دولت و ملت عراق و ابراز همبستگی آنها با رهبر معظم انقلاب و ملت ایران قدردانی کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/457765" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKNqcKDayvU8QdcA44NNoxTUH58iRgCtGviRystc45_LmL-FeHRuwIgU3tMDZHde8Iap_1lDbVlAMPP_7d2gD1iVE493QWODTpscX_1QyeGNUqqhdvAdHQoLJlgr9lacsYe6uKnHyNuzQe4haz0JTuUFWljeUQBHesYoZQIfDCYZpFVY7lvMHfglWQKbKWCBd0HDOpBkHMcKgu0IdapSqwvm41vxfPq-YyQYiF5W5V9HGDlCpx0i2Oyncjudmj_WssKnOni88XvjEF5gZuGrw94QjcPyJekaKIrSqi1KLm9VzwN27H1VrvTGbpUBwnlJOgW_F6jWV-6DXqSjeOi76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DI5Od9stmrgU0xfF9_iCwtmYi8virIpYZ2SL5_iTt50l37M30amPfRUX02mQbEbSPcj3iuanMThJPaGsbAmFF6dt9B61mPh3uMj-A_IOWsMvw5zFI62ErOerms3CM592vZwU1SifRPNF4X3dFXzVCvSYVFkqG3I4gGuizsqXHF5qxfHhgeBop4azRCJ814UvCnFu3Q121ytXpwcEHbiqL4FOOuraqIEPhxlGRVXlKRaHY_RxssetC5uCjmxpW2DdDEL8d_GKL3KMYXlmJLZXMoMxyl9S3PTDE_0lt9fQhIe_-oaFEIvxVjAweP1UiMm3CH5sUsXyt0x8jQ733ZjwVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G71EDMaAT8hY-yM4sTWFrnOdK7PxUxXOrICEJHufJ1eZ6T_IIbn9cA3r1HDpCYTyFFTPXg14PMpn1P1Cwb8wiZiSUONPHDbnwIivqDzHEPRQNCLOQdcAPWGuh9bWqNw4ta1piaH5MoY43JQgefqra-uzCtS3z0CRnfdGt4V4LVjmffU-i15vB8mmrq2X4luMPibrKXUYcmWURs0zQUWFJLvCJmEtPyeVkZh_E7mXoT9q281XmyDs-lV0FkG0RUN1C4AM7MkPPmwjbtwu83bE0PG5Wvz_mMdrV18gtFOny5lEsy_xpIvwQ0ZGQiWJdJ6aCAyFDnkmTVCnIwb5D_JWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxkKz2aeoNC717iY7rJJaXMqng_zbhh6cXyqErmHpHih93NeLrJGt5Q66v1bJQvqaPDiDGY4BxvqeTeXsEgi-FDLn-T9j9vKcOGlA05ViYo5SYB7g9WS5brtQPHoPDT9IT8nzLu8PUWeZZnV8Kdg6c2OAqqKcAS0zgIG2kET8Pj9TQRh6RUb4a6Xj1czzdF6eZL3mXb3W8pU7E7wF6eXF6ha2upFL_fVpfHvM0ZotjjacEmhyychIndUpp5aG6MYNHgKIHauMVh1N6DKD_HrZjsnCzF0rH5_52f8ppsu3EYA8SbKD4zEVd_JC81aEfbc_8FTtCcfv_PPDiiHmygX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLE_fe__PpBDdB-1WTAuwv9ma5b4B8xG184mv_0K7Yaz0w3nIT-y6WyWjtvjmK0e1BvLzwI-YBTkmO3KQzaMqQJvGatGyY-T4petIui7N0PeuGN6T-E9SHy_5oKTA3JmX4HYYtaILql4sggIMVI7jhHiONoMOR9cWtD_TcDLYSrw8A52YTxuXcZ6gJHz-u1mHSmDXe9imsdd_XLxScuA3cnlsUlBOCDlUWAiu32TfAikmG3gTGF2EAZXkBbgujU5goaeFF90ElIAZhjjq6Z92WAqIL7s_pu8dWM8I3TekTq_TGFv_ZjJb4dZewr3BvLikLyd6haSRCXeLsFHI6lDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bml-AbA84JdVxRA69Nltkuv6BrY-aN5p2DlO9jZkH5y1ZCcgRyGOVLYIQnhJIRKlfpEv62spSQ3NDm1q7P5kXDnBxsqWowcG5rwWFjIbZ4rMdsMcSFl9IpGotd4AbHxhw4bxKKH8aao9NC8bFAceikJTD2SBcDDH5g1NRb-pVCKqkx579Uv-uvV_CFXMX1FJnzQsp83EXcMgb_gAJRj4aEoNzWSJyPQL6FII-mNasfJOGBpGosAx4qh3j2yU2IRA3wXLkYjnN3a0y1wvpoOgre9BCxyTower0PaV1g4dsNh7VaoaTcH-3dfQTpGsnouhIu1EBTdQs6uFkahlNnUelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ_YgEjPkpxIYMjmJ-D6G0xC--b8jGlsbd74fNGRufWJWx0-5X_r4O8BCfgfLQmlXdX40eKeWtOvZoXn5eTrlg_A2wYFQe4mPp2vElKc3-7Fk2bgrdvcWUqZ7d0tlv_fwc6o2oWm237nIOP_SUtuCsQS41dtmsYpcDC_xzPPSE9yCWkxZQ_mZ2flWiaDn29SH8IrI6RWzrXT8hDr5d01Tt0a8tIDCuCMjjME2HBtHdEA7kjFiLFqu8l2HtlSLWh0XEsQ8SF9RNqfG4T05bBlB7dHEzLye6Y_SH3HysRrPXYbxht84juLieEdxN7zx4toMH3ZWRUkCzlfJ0D_JRC5KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آغاز عملیات اجرایی قطعهٔ ۳ آزادراه تهران-شمال
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/457758" target="_blank">📅 17:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f439d26cac.mp4?token=EnpUEUhOi7V9Ie0L2K1f09Hc4RFHSB8Aa1ip7QoH3cuVwIsStQi5hNiKYUawUA8cbekxPHdeslW3GzOH0wCBj_Z-tiebda-0njad2c_n3NLdxzhEICI_8DWeqdpu-B5V6cqbWuVp9JNlrovP3E8is8UhJoLTpAeF8n0216DnqVXHwxO-XfuX4_IfHxaD2D_xtLRCd59dagoDsAiD1pN7fQutozq_Id26ZRq1seK9HsQHuRnAw8AtnYIzoDshjBBHapzRb1ZZvUyEF9gezcABr-hYI50VYithjFPl2G4dmf-9b4aK218RMJrtWlQ7lZrm-_LpDOnx37fmamDe10gCcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f439d26cac.mp4?token=EnpUEUhOi7V9Ie0L2K1f09Hc4RFHSB8Aa1ip7QoH3cuVwIsStQi5hNiKYUawUA8cbekxPHdeslW3GzOH0wCBj_Z-tiebda-0njad2c_n3NLdxzhEICI_8DWeqdpu-B5V6cqbWuVp9JNlrovP3E8is8UhJoLTpAeF8n0216DnqVXHwxO-XfuX4_IfHxaD2D_xtLRCd59dagoDsAiD1pN7fQutozq_Id26ZRq1seK9HsQHuRnAw8AtnYIzoDshjBBHapzRb1ZZvUyEF9gezcABr-hYI50VYithjFPl2G4dmf-9b4aK218RMJrtWlQ7lZrm-_LpDOnx37fmamDe10gCcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی حماسی احمد بابایی، شاعر آیینی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🔸
دیگر چاره‌ای جز شکست صهیون نیست/ خوک صهیون بعد از این روز خوش نخواهی دید
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/457757" target="_blank">📅 17:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e5295f0.mp4?token=K_on6szw7U2Gpr2IXV7r5ypFDUrTTsKZ00Ud_ISs-Q9oCaS2aBmujhK-o7T2dw4f50y6H5yQCwW-QmFIPx6fFm__R5nExQN2vQSZBtDspUZouWav9L5_Gv8pXd2Z3xRzFAzmSXM3A4UOa09ggRv1NxCx2O6mqMrn1tQckm9vui8C_q_-mXkkAogHSPV5_hS2ZoKTBxDkI0A-mjnVSCKUrgJ0gk73KIv-Q8BLnMNTeq_6eEfge_vkKcmc8lWC6IqxlHugXWGMOvT2ehtsqWaoQhSEQGBesTBNmtGFKjOnAd55BR2Jh8Rc1lUqTKKVfCv2d3TOSfj24gySccRoZEm9_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e5295f0.mp4?token=K_on6szw7U2Gpr2IXV7r5ypFDUrTTsKZ00Ud_ISs-Q9oCaS2aBmujhK-o7T2dw4f50y6H5yQCwW-QmFIPx6fFm__R5nExQN2vQSZBtDspUZouWav9L5_Gv8pXd2Z3xRzFAzmSXM3A4UOa09ggRv1NxCx2O6mqMrn1tQckm9vui8C_q_-mXkkAogHSPV5_hS2ZoKTBxDkI0A-mjnVSCKUrgJ0gk73KIv-Q8BLnMNTeq_6eEfge_vkKcmc8lWC6IqxlHugXWGMOvT2ehtsqWaoQhSEQGBesTBNmtGFKjOnAd55BR2Jh8Rc1lUqTKKVfCv2d3TOSfj24gySccRoZEm9_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
موقعیت‌سوزی عجیب هالند مقابل دروازه
@Sportfars</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/457756" target="_blank">📅 17:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457755">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBQoeEgNfvHVv_dTvQkQcxRWtRc5cPhAmxiY4GVfXSf11YN0hJerOQ5Urdr1nS8wt5scxsoaX8S3VaPG6JlZ6WTMlwZ4j36PZ3mpHW_eaqmZlxsaLfm1Fl45gRYeKAM4s_rSX4lo_t0Zn6qyhyeUyme-XZmFPgqi2oPcCqqEYXPcVg7xvttGYTTmsNFF5sLjsXTWByEABs1ms9ZhdgrUr7mKfjcwP2c-nAsiQw7P2jHc8EiXKM84nAc5ORiqobISloWCkvjbr3OGVodKRLo9Kche9BuYMVnPoUjcvoXpKRZsGaOrD-gIhxMg2zwsPKTGqpbmWgH0xWEut1hs0FDkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اساتید جمعیت‌شناسی خواستار حفظ دبیرخانۀ ستاد ملی جمعیت شدند
🔹
جمعی از اساتید و پژوهشگران حوزۀ جمعیت و خانواده در نامه‌ای به رئیس‌جمهور، نسبت به احتمال ادغام دبیرخانه ستاد ملی جمعیت با معاونت امور زنان و خانواده یا وزارت بهداشت هشدار دادند و تأکید کردند که موضوع جمعیت ماهیتی فرابخشی دارد و نباید در ساختار یک دستگاه خاص محدود شود.
🔹
به‌گفتۀ این اساتید، ادغام دبیرخانه می‌تواند جایگاه فرادستگاهی آن، توان هماهنگی و پیگیری عملکرد دستگاه‌ها و همچنین ثبات سیاست‌های جمعیتی را تضعیف کند.
🔹
آنان با اشاره به چالش‌هایی مانند کاهش نرخ باروری، سالمندی و کاهش رشد جمعیت، از رئیس‌جمهور خواستند به‌جای ادغام، دبیرخانۀ ستاد ملی جمعیت را از نظر ساختار، نیروی انسانی، منابع و اختیارات تقویت کند.
🔗
متن کامل نامه و اسامی اساتید را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/457755" target="_blank">📅 17:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457753">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msB1QXRw6HrxhIy7WAKO9pPuZQhWIT7-qWz1KETyRWtJrVX35WyJ-wQaE1Boz3MYQI1efkWk4zwg6MfkbaccVxxRqR7rfSRAdbH2t3Lic1DCdwoUBq_8Ywwr9u91j64ZtnUesmLOABdS6eX8ASmEz4Cs-dJmuIo4lH7PYGQXq0Ytls5PeTdgrpQgdzc8wUkr2_SVuBUvY3Eqga3iZVRlpXgKkP2odIarWDCDAed8iYwHq05a_kRX5ZFbP3OeIbgveGBHyP5EfLkUqqLYMD01B2mMi_D1ihE6V1I4a0_Amd-m3nYgfBgHUbx4QDwjshFoS09sVzsjujm6Y4DEySR2lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Utjo6aDYAnYE7GccklLu1ZWY7xlRdAVRNlAG8eM7_fqh66HMpRBAQtATJpdDEhkeYbixXDVrNZlkMZQY2II7oopMWJ4NNo0og9L_YwpnN5xmKa21Wk0BQrcs6Vz8U-DlgdC74_9R6AotFr8nKHpuUOkKTYVsWTNoF4uW4Ct5gV9e_0Ki6N59Tg4vkPunb-RULEd8beLPqWjZa38GhPdEYwpa4APSPwMFqkfDYL-QeWHCvLXAVNMxR2xLhPHBD6kMExNz-oBJm7Or6tWwd9mbVBXla-YO9OzQXqOJjwNthctwehCO05o62meE5kSdkxgsFZaYLun92lkluuF8Y61_hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور پزشکیان بر مزار شهیدان نصیرزاده و خرازی
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/457753" target="_blank">📅 17:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457752">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7NbiN0T0M4ipPfkcEL2T8Ua5PaHoweqWn_ap9DGtm8deUG7WAP-C5IOeQIU7Nl-Een1GqJbBKDmnfnF2eekSdV1Df7iOXpcE-KmF3KDzYrtiTIFS-5xZKUUV0mL90lJrqDmMGBT1aXLmrQ2f2GokFm-WycpcZeYEHhx4A5B8ux5Nylc-MHiC-PixY6BeDNw3GTMjtVd_125LkqKi0CF2ntDYP0z_j1u_CrPqwVXGj4wlPKcPyYauHBFf_qmj8xFBCfNoSYyLK0iTt7FNFRO9T4i48K5FFWnmXQyaFQ7Q4D_Xamt7OLCOfwVESPnd6N3zol9jbUJI45O7nd69vv4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی‌های چینی از مسیر ایرانی هرمز تردد می‌کنند
🔹
اکانت رهیابی دریایی منچ‌اوسینت می‌گوید کشتی «نیو وییج» و نفتکش «موسیک» با پرچم چین درحال عبور از مسیر ایرانی تنگهٔ هرمز هستند.
🔸
دوشنبهٔ گذشته رویترز نوشته بود که ۲ شرکت دولتی چینی نفتکش‌های خود را  از تردد در تنگهٔ هرمز و باب‌المندب منع کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/457752" target="_blank">📅 16:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBUpUWgvzFtkT8nTo8gkdjIH8xGJKAUePuQLqdTU5AceiSP4muS7ncbzfUmmLv9tG3Zq02AyhzspxusyLToLXXp-7NQ2coM60HEQqHhk0paYN-DE-uuY78u66cOabjqN7-R2oQCWq6utcVNs54iFpTfyq3yUCy5cAkMz8pd6TaDyqCsfwChNFrL2fJhdDPWErGhnOjA13nkxbBN4BhWYa1eNkoGtLBpC_qQq4n0viQfth9i-XuBiccf07wdYU9sGvaL4sUxmMQTrdfC8ISSvMygfnFYVZF_Gkk-RwvckQbDvIXtxQP7ZTW7P1ZW3Z6UunRcMFzjjaXyfF80vBYa_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه‌: بیخ گوش آمریکا تعاملات اقتصادی داریم، آمریکا را دور می‌زنیم و نتیجه‌اش را در آیندۀ نزدیک خواهید دید
🔹
سردار محبی: رئیس‌جمهور آمریکا می‌گوید دستور جنگ اقتصادی را صادر و شدیدترین جنگ اقتصادی علیه ایران را شروع کردیم. این اعتراف ضمنی به شکست مفتضحانه دشمن در عرصه نظامی است.
🔹
اگر در عرصه نظامی پیروز می‌شدید، لازم نبود جنگ اقتصادی را آغاز کنید. مگر جنگ اقتصادی تازگی دارد؟ ۴۷ سال است جنگ اقتصادی می‌کنید و همه ارکان اقتصادی ما را تحریم کرده‌اید. کار فعلی دشمن فقط ادراک‌سازی و ایجاد باور برای مردم است.
🔹
بارها اعلام کرده‌ایم که برای هر اقدام خصمانه دشمن سناریو داریم. یکی از اقدامات خصمانه دشمن، اقدامات و جنگ اقتصادی است. ما برای دفع آثار سوء جنگ دشمن سناریو داشته و به‌راحتی ارتباط اقتصادی با کشورها برقرار می‌کنیم؛ هیچ نگرانی در زمینه اقتصادی نیست.
🔹
دشمن در حال جنگ است تا ما باور کنیم او پیروز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/457750" target="_blank">📅 16:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650f899407.mp4?token=XmfUU5uHmZrYnzvM1WeU9X8kCO_EUHbuGun5GTlvm_j1U1vrp2g4f6hqXMuBUHdQmDxmYcuUuCE4F8vhgp-59P3MUD97N0NJdibFpc8gNt54Cnjd0W02oyP3-Oef6Y6yEnlsAFQ8pKHLhtjHwwrxNijJqX53Srex-1wLRw2jiPJPI-zCgz_hMqneQS9-wz1YB0i359y0l0ygR_U3vTpLn90Gm--M4TWdR9McQ_tClcVtWz1OmmikhpngmmIfZEh1RIddUBZdkIBxxalRJkaDrTIlEZMP23NABtU8Blzdt3XCP2EIaqMAaqSDppNz-klzVA0sNJcSdzVmbiCJUVVApw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650f899407.mp4?token=XmfUU5uHmZrYnzvM1WeU9X8kCO_EUHbuGun5GTlvm_j1U1vrp2g4f6hqXMuBUHdQmDxmYcuUuCE4F8vhgp-59P3MUD97N0NJdibFpc8gNt54Cnjd0W02oyP3-Oef6Y6yEnlsAFQ8pKHLhtjHwwrxNijJqX53Srex-1wLRw2jiPJPI-zCgz_hMqneQS9-wz1YB0i359y0l0ygR_U3vTpLn90Gm--M4TWdR9McQ_tClcVtWz1OmmikhpngmmIfZEh1RIddUBZdkIBxxalRJkaDrTIlEZMP23NABtU8Blzdt3XCP2EIaqMAaqSDppNz-klzVA0sNJcSdzVmbiCJUVVApw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامۀ سمت خدا: در حوادثی که مردم به میدان می‌آیند، نصرت الهی از مسیر حضور و اقدام آنها محقق می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/457749" target="_blank">📅 16:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2dd57082.mp4?token=HoiSKbtJd7Ds1mFP77g0QLc5CVwP2XojXD7uhE_4GRv34pYmSUA6lpMozcWzkLZ69zCFNuP8py7wVVGQo8xXPZ8KttZiK8bD0ePI7jA1eS4MhDyGAQMUDmMZ3vxy6XKGhqBKDUDhNjlH2vJrUl-ZbEuuxwwekr0RuNBe0S10uYv_nvjvf_fAjhEKVJVgpUDZtI8JTYj5disu2zTMOhAa9wGzsu5cS1sEHKgrB56aW_V4NUMfMQuNK0-xbL0hDfjMYuC9rT_Nopp7MoZKkES84yVO7O84_J_TATAHhSy_j4L-ut3vh2OvgOY352U_tTrcJzkWt6gcbFo6O3w6iEF4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2dd57082.mp4?token=HoiSKbtJd7Ds1mFP77g0QLc5CVwP2XojXD7uhE_4GRv34pYmSUA6lpMozcWzkLZ69zCFNuP8py7wVVGQo8xXPZ8KttZiK8bD0ePI7jA1eS4MhDyGAQMUDmMZ3vxy6XKGhqBKDUDhNjlH2vJrUl-ZbEuuxwwekr0RuNBe0S10uYv_nvjvf_fAjhEKVJVgpUDZtI8JTYj5disu2zTMOhAa9wGzsu5cS1sEHKgrB56aW_V4NUMfMQuNK0-xbL0hDfjMYuC9rT_Nopp7MoZKkES84yVO7O84_J_TATAHhSy_j4L-ut3vh2OvgOY352U_tTrcJzkWt6gcbFo6O3w6iEF4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقام کانادایی دربارهٔ ترامپ: با آدم بد نمی‌توان توافق خوب کرد
🔹
رئیس دولت استان منیتوبای کانادا: «همه دیگر رئیس‌جمهور آمریکا را می‌شناسند؛ او بی‌ثبات، غیرمسئول و غیرقابل اعتماد است. به‌خاطر ترامپ است که ما در حال حاضر هزینهٔ زیادی برای بنزین در جایگاه‌های…</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/457748" target="_blank">📅 16:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHnZhOwTux929fMT4v-B8XlZcFRFBM9VNnjdOZTiZYF85ZDczUNM2EzHfFxvIV0XNiXC6kGEcESfu2RbH8h_CsQLL_s2r2rk1KGbM0OfyIoq42yk6vT8GboaxYDxP2V0W2KKsBSz5RGsAhx4kPA29iokoXT_ky-NIJljWf7DeYimEBZ5SZBNYK1jKKsWHv2qNcyB5BchLZ-FZEbNeLiJzTiVptyGZLdpDKC4j0xB5_4QJ-bCiwF387uUa3vh5lvm85P_rpLJoW5BkwnMxAIzCmfekW0uXMH_48py76Mx8sGMD1QvjQ7ge9qHXrXhGe-6lxof2zZE9WeKv2nf0bKyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در تدارک ضربه به ترکیه بدون درگیری با ناتو
🔹
پایگاه خبری اسرائیل هیوم گزارش داده که سران اسرائیل درحال برنامه ریزی برای ضربه‌زدن به ترکیه هستند؛ به گونه‌ای که ناتو بهانۀ کافی برای حمایت‌نکردن از آنکارا را داشته باشد.
🔹
محاسبات راهبردی اسرائیل بر این…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/457747" target="_blank">📅 16:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f217d6f888.mp4?token=kuFr1wrhQwA1utSljSeprl8CCXhicb8sO5Q8LP7oIepkmpcFTXkxPMuOZl0e90NyzUKl0cdlIg6pQiWbltLV2hDdlispXsNz58TIgOzQw9mWfEamksk7E7E-mqG1rm3mUmIevS55gz7Bi2-TAFgWtr0gbRY5S8GapyKlRafS4o0GjwBnFjHsDUZAxgKVsWJqFnVl2wDWvb48KmZNa9r403twlHKmGL1d8BdjOme3q2_CE5BfhjSF8lfhR83fFu687u_IZtkGL_8qoFS_fDkfWOrnvxihGIOenww9pBUQD5NcwIBf3RZL0RxTknHqaQCcr-ohYnFdg3ZnAOdpnxKQSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f217d6f888.mp4?token=kuFr1wrhQwA1utSljSeprl8CCXhicb8sO5Q8LP7oIepkmpcFTXkxPMuOZl0e90NyzUKl0cdlIg6pQiWbltLV2hDdlispXsNz58TIgOzQw9mWfEamksk7E7E-mqG1rm3mUmIevS55gz7Bi2-TAFgWtr0gbRY5S8GapyKlRafS4o0GjwBnFjHsDUZAxgKVsWJqFnVl2wDWvb48KmZNa9r403twlHKmGL1d8BdjOme3q2_CE5BfhjSF8lfhR83fFu687u_IZtkGL_8qoFS_fDkfWOrnvxihGIOenww9pBUQD5NcwIBf3RZL0RxTknHqaQCcr-ohYnFdg3ZnAOdpnxKQSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناریوی تکراری اینترنشنال برای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/457746" target="_blank">📅 16:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JiyUDyEREWacxdVeyAMfQubyOYYqvaQ7XqzropqMvxQCSjJq5Tvu1Wg5Yj8EvmOPXRncBMC3x34XVwhAUGfBSZmASaFGb1kbFHU0jV2fRaYM32ZHFg3MWTCBp7LUhS4NmgenH_qfDhwyoSJIINeNnuszEYRJMN99CgrVNVuWkPq71CvEwjLQ-ukFFnCupflV1TET70zjqd0jOHNNxM3qQQ7H6metkWw3qR5D2BAuMn8NJROtnM9OMm3EQ6lTvCo242cKz1NE8QdGzPIeKjenKrJMRdmZUzH9N3qU67Tl2x3BtUrr4M4plT4Wcaxj9HPey4BPM1qE3e2Jb6MqvgfmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtiqtdmnP814AZgKXY59Nx05G1qDpPsioJJFu9nxRrdkwb1aeU8JGZwn3EQQq7basKd0k993YcoeLTUUKXa8UeK0p7i5DTqoixLvgvbD5zIRo4Mto_HpeZYsYwHGJyv4h7dv9DtBgEwWZF22LvphaILYtyCmdjgUC30flZ9x_G0HaVg0KkPIAxseJXl24aLNlU9aP_nEqt_XsjNE7W5y29lgU_CMHsthrYWXdvgLGJurX1wQvGc5WXJeLOsA03BGSnfGsdKbWsJl7H2VWpLL8Js_1ok7McTSbjSTpqDZ22agRTd0DKT_vlhqCB9CQIm0lBAJiTW8RDz9h-Xqm-X5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2KQ7JgZJw8CSdMrnKwQXiSYxkcBd0V8yqFHFKXFvyQsgI_MBjxehhVhactvVzCRIIddKU6UddEx-fqsiHJDjFrgJTeDEbCP4QDJpZAD24rlCGGCqg8rUHfnCuwkWCq3IH-drjQi8yWpc8gZRyiMCaR9-M3Eog9oIn_AWZk3cs5UnYPey_LQLjjMQZ0raTJta7n2bNSwUFV4H8v_yDQe7YDhidplHWNLbzvzholLj-A5DkTZSYzyNpHXeA3iJaJiJC3IVfVBMCkmQWR7piCoz8iIrZYnt3srwm7ef3VbIpXh4B1xyFjWkOHIj0qTUGN0lhAXjg0hscV1XObQ1hiOZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آیین غبارروبی ضریح مطهر امام رضا(ع)
🔹
هم‌زمان با ایام آغاز امامت حضرت ولی‌عصر(عج) با حضور آیت‌الله سبحانی، وزیر ورزش، تولیت آستان قدس رضوی و آیت‌الله علم‌الهدی، ضریح مطهر امام رضا(ع) غبارروبی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/457743" target="_blank">📅 16:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef27bcbf19.mp4?token=eGJ2En7cmk8YCRWZld06CNcN2jwcnztXTd9VAJAAtKeoziW5We4g3m-ZkCvV13GlfiM8owdKd1jJhONjnGm3aQXWNPO_V71r0DvoEKA87a6YSfHUSubZk2mX3Tf6hjnvs68vEZCB2h_hDro3D43p3FfOZU7tWTJyJXWArc-2pXMmlAy9gFIobp980JFqMqg9zYM1MuIdpcMyqfp2qu3L6odm41DFd1nPWupFgsJobl6-7QrC_TTysSKI4A7qPDM17kirJLM8mCcn5jlBVXRkmLZLzpAwwD1iVGhQEG2ZzHW68vhp-jq58JMCabkTrzQb0_MFYVDsxq2bmHT55QiOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef27bcbf19.mp4?token=eGJ2En7cmk8YCRWZld06CNcN2jwcnztXTd9VAJAAtKeoziW5We4g3m-ZkCvV13GlfiM8owdKd1jJhONjnGm3aQXWNPO_V71r0DvoEKA87a6YSfHUSubZk2mX3Tf6hjnvs68vEZCB2h_hDro3D43p3FfOZU7tWTJyJXWArc-2pXMmlAy9gFIobp980JFqMqg9zYM1MuIdpcMyqfp2qu3L6odm41DFd1nPWupFgsJobl6-7QrC_TTysSKI4A7qPDM17kirJLM8mCcn5jlBVXRkmLZLzpAwwD1iVGhQEG2ZzHW68vhp-jq58JMCabkTrzQb0_MFYVDsxq2bmHT55QiOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معجزه‌ای که در روز حمله به بیت رهبری رخ داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/457742" target="_blank">📅 16:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbJyTb8Zap7st7xGlBR9VkREveOH8VA4B9K8n9Woyhy1VtoouY_u87sVhOirS_xjoCWGYHYm5X5Yw2bwqrbPZ7WJypjNS6VFlfrswV9tVpthPcJMygs9y7Uwnd1bLN96wWyvVSm4Zxhgm53rXRDR96I2rkCMJzzKRYGsDlP5aLy1Yak6RJr-rxAARL8YBgRbpEYwbBp0vSRqo8lUz6h_jdx8izoREFMfsDKiZg64kGSesXFMDtbyuAGgJymdV4PnlZZnaPjXQITH_LJHqytDKEyzZJ34mEdmdvfcUKeBnL3Syt5vOCjLfPkSXTcrswKh9HysTNhuAyNOhmm9Xagd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنگونی یک پهپاد جاسوسی عربستان در یمن
🔹
خبرگزاری رسمی یمن به‌نقل از یک منبع نظامی اعلام کرد: نیروهای مسلح یمن موفق شدند یک پهپاد جاسوسی اسکن ایگل متعلق به عربستان را هنگام نقض حریم هوایی یمن در استان حجه سرنگون کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/457741" target="_blank">📅 15:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db946df252.mp4?token=oerJR-DRDnoG-7aUpfRT403x9uxy_cac9nFzGYBi0DndkaGmGZiLp7CKljad4eQ02F1Q88SS6n37S8nxZWzeGFLZtck8UWzRa98jiyIlTPu-5WstIPwOndKmS3irGqbOhzfbw4CjNXTCZoebERktKEpX9TtI9_ofoGe9hdGgOJYAvaqTUgqe5zYVc9z-3Y-R-Z5RC6YMTU0JAKRQbpfvJhxM3ADDaxZm33p5bWDwG-OnnIuMPJFfu23YaDg-BiYOst0yMPNc_iEXJTh7cElr5IB9L_y_Le-1PQCAT-gWK3Q21uQRiTDHSmFp_aRGzC03i8WxMxIgh9rTuIHCSGLJQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db946df252.mp4?token=oerJR-DRDnoG-7aUpfRT403x9uxy_cac9nFzGYBi0DndkaGmGZiLp7CKljad4eQ02F1Q88SS6n37S8nxZWzeGFLZtck8UWzRa98jiyIlTPu-5WstIPwOndKmS3irGqbOhzfbw4CjNXTCZoebERktKEpX9TtI9_ofoGe9hdGgOJYAvaqTUgqe5zYVc9z-3Y-R-Z5RC6YMTU0JAKRQbpfvJhxM3ADDaxZm33p5bWDwG-OnnIuMPJFfu23YaDg-BiYOst0yMPNc_iEXJTh7cElr5IB9L_y_Le-1PQCAT-gWK3Q21uQRiTDHSmFp_aRGzC03i8WxMxIgh9rTuIHCSGLJQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات توپخانه‌ای اشغالگران به جنوب لبنان
🔹
منابع لبنانی از حملات رژیم اشغالگر صهیونیستی به ارتفاعات علی الطاهر، دوحه کفررمان و شهرک المنصوری خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/457740" target="_blank">📅 15:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMgechk5x1-VOBz7mkBUBq3MbApTkI0rIVhBSwVV8ZAn1L9QdY_5MOAluq9LKqU2jmVbXLfF-sc-vT8Oivcm0gs6DJqlAdMkAgcX5fbs2EsdHV8KOnXerLOCAD5861XSurJ9DFOb0TIStbXW4l7_cp90Dw6HwZqsW_44sK5k0MWxPGYweIquZW7oKVupOuFsVF-pRb_ZaX_QmPDq66GaArEJcy-HBFTzVlgy945NTLVc7E6i0CGFnAvlmhiCkErsvp6F16z3KRd4sGjoBKa4IYqnekt1h5m-rYXoxN_oElL-qwuVJihPAUnjrmeocmvrPBgVbf5BgPUWi8-fhpkbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجارت ریلی ایران و همسایهٔ شرقی ۹ برابر شد
🔹
شرکت راه‌آهن: جابه‌جایی ریلی کالا با افغانستان از کمتر از ۱۵ هزار تُن در سال به حدود ۱۳۰ هزار تُن در ماه افزایش یافته است؛ پیش‌بینی ما این است که این میزان در یک سال به حدود یک میلیون و ۵۰۰ هزار تُن برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/457739" target="_blank">📅 15:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3edfc522.mp4?token=ZJnCBxCG6w4HEquSKwxee8A_g-LxIaHLIQC8kypAmMVX5vrHXSDRKnhfRgVV7bRYWrY_CCV5ShbIoUpwuLeskoRbUhrCcoyegrEHVh2aUkQ6EuUKv2o4KdkAOxxEESvIqVIliY8_MmDr5f6vcJO0Z8fAE-fo9nKHE1RsyzIPCVY7Xaas-YWAOulysxcn3Pb13M5rTwOJ9-jUIqCMuxXPehchsuccSCLVHdM_i0KWOKUx-2LqP3Yvv-XHPDFDt2LW_hGWt94OQKFLQVyJUJh7QuAgS3TfngdYmW8ME7SuxE26ptz7c-_GU_NHMrDygNlUkMVjwxpPItQ6fLCz_71TKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3edfc522.mp4?token=ZJnCBxCG6w4HEquSKwxee8A_g-LxIaHLIQC8kypAmMVX5vrHXSDRKnhfRgVV7bRYWrY_CCV5ShbIoUpwuLeskoRbUhrCcoyegrEHVh2aUkQ6EuUKv2o4KdkAOxxEESvIqVIliY8_MmDr5f6vcJO0Z8fAE-fo9nKHE1RsyzIPCVY7Xaas-YWAOulysxcn3Pb13M5rTwOJ9-jUIqCMuxXPehchsuccSCLVHdM_i0KWOKUx-2LqP3Yvv-XHPDFDt2LW_hGWt94OQKFLQVyJUJh7QuAgS3TfngdYmW8ME7SuxE26ptz7c-_GU_NHMrDygNlUkMVjwxpPItQ6fLCz_71TKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ بانک مرکزی و وزارت نفت به پزشکیان: پول داریم
🔹
درحالی‌‌که «پول نداریم» یکی کلیدواژه‌های پرتکرار رئیس‌جمهور شده است، رئیس بانک مرکزی اخیرا گفته است که تاکنون ۱.۴ میلیارد دلار به ذخایر بانکی بانک مرکزی اضافه شده است.
🔹
همتی آخر خرداد امسال هم گفته بود که…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/457738" target="_blank">📅 15:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e75f520aa.mp4?token=eOcm7BpYUg46c5ZDSzePktOVNYV-r-fuKltJdCjgc5zpMT71qaaE-ynAFPF2c3raCrvNBmp3S63x-9kyPDJF_wIU1aM0RpDjmxTZ7soBkTAqTEPW1T-YnX4duz-mSsNt43enPRdB1WAAmXPIfaMYtc-0sAUM8N4SCkgl_GBS-7VpKIXqSRZCcAjUR_uvmmyDM1VInrfGhy0H_aGT9Al3hw48mfKtyvh18wqIwau5udIb_Thrr2uOKnDtUFlnkmQECoVQcEG0gC9uGwhovt99FjWJXDDBbOsDp8vdycFqvW5XRR0F5tUe7wU-nuLn6DA1iCmbFJ3ZtXLiKi8fC-5RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e75f520aa.mp4?token=eOcm7BpYUg46c5ZDSzePktOVNYV-r-fuKltJdCjgc5zpMT71qaaE-ynAFPF2c3raCrvNBmp3S63x-9kyPDJF_wIU1aM0RpDjmxTZ7soBkTAqTEPW1T-YnX4duz-mSsNt43enPRdB1WAAmXPIfaMYtc-0sAUM8N4SCkgl_GBS-7VpKIXqSRZCcAjUR_uvmmyDM1VInrfGhy0H_aGT9Al3hw48mfKtyvh18wqIwau5udIb_Thrr2uOKnDtUFlnkmQECoVQcEG0gC9uGwhovt99FjWJXDDBbOsDp8vdycFqvW5XRR0F5tUe7wU-nuLn6DA1iCmbFJ3ZtXLiKi8fC-5RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر کانادا تسلیم‌نشدن مقابل آمریکا را از ایران یاد گرفت!
🔹
در روزهای گذشته مذاکرات فشردهٔ آمریکا و کانادا که قرار بود مانع اعمال تعرفه‌های جدید شود و افزایش تعرفه‌های قبلی را لغو کند، شکست خورد. مذاکراتی که ترامپ دربارهٔ آن گفته بود: «توافق بسیار نزدیک…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/457737" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d92f2b851.mp4?token=dMsNChnwDbFPfin8qOlnHpA73Dm-cqTKIy8h4QeJ3Lkz70VBIPCB42whnqxRvpwRxth0035PuS8cw4QJj7Hc0aM-qFoDYfIGlYWSUnnd2qdieJU0pkgcsaZOfaRDgM91nnujMHx5Cs39wDTMULbxK9zlzxL2QhMPL6YBKIPFyGlPQDG47YETYV3m_1RGKXTwO03295JwkSEp4A0hQElSEBSGdyJBDmgOk5HVb3X3P-XEVDhfs1OjeG-RdbrX4gB_8vIUwmz2nLRItTsUrdtNkSIfR969MzJlRqKlTuESlcVm4nI2KGgApMq8tMv7tYOTWhQq0jMFc8dXn3H6yTto-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d92f2b851.mp4?token=dMsNChnwDbFPfin8qOlnHpA73Dm-cqTKIy8h4QeJ3Lkz70VBIPCB42whnqxRvpwRxth0035PuS8cw4QJj7Hc0aM-qFoDYfIGlYWSUnnd2qdieJU0pkgcsaZOfaRDgM91nnujMHx5Cs39wDTMULbxK9zlzxL2QhMPL6YBKIPFyGlPQDG47YETYV3m_1RGKXTwO03295JwkSEp4A0hQElSEBSGdyJBDmgOk5HVb3X3P-XEVDhfs1OjeG-RdbrX4gB_8vIUwmz2nLRItTsUrdtNkSIfR969MzJlRqKlTuESlcVm4nI2KGgApMq8tMv7tYOTWhQq0jMFc8dXn3H6yTto-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکانی که به‌جای رفتن به خارج، از حس وطن‌دوستی و خدمت به مردم می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/457736" target="_blank">📅 15:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457735">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b8c1383b.mp4?token=HSWOe1KsS47lsHFY9ryRixzouUzhP4IFywbxzoHvMRkQ7fA1SqJ58la7bU0nVn1xCr5RqX6X-90ZOSRUbycsHTAczVaOSFOtIvCzAx8vnE3P1_7_fOXrJ2o7VxOnC-i9j9R2vIlWpIwxgmVQ8EPglW5uC0Zya_I9rf1rz7kr8eH2dzdPHL_RePh52hoPFEUxhoQ9qVKwv0-QcDp-W-yZndgu1z2HFk7743jm9LRxT_zcF7tdmtgMG7VL22XHedttUgPF97YXhdofgAC9HyZpPIaSLWGsiuMOif62OKn7Ylhv_6LD2FgXncu0SY-oXgD5zGJxRfxwRqGsnsqaBO0JbAnBNvorb1Qqnp9cJcLyrlbnViWZHMSUGSDAEGrZqjKSWj3y_EO1b3wgDPxqFXKDEKUFe3verUt8VCgdpgsf0PfFdy0oJ89YpFhFnH9Y2j14VBvAiWBAfb0TkQP1_Okl2cM0u5VrG7gkj8Hq4hqWhwYG5LaUttktrHKclguFvmk6QV_Sitg280RDZhpMMbXRsruFVDjBCkmcfb7TZP0NFO63MM_2jqls9WCuM9eZ4IUwG42CLRWg7PJEwuhdEhST_-HF5KE_wsR8EHTq9wVVTekztGNrdPSLw4r6A4CEqaf8I9CDZ8mKFV3dFrVjfg8XgZY844cwNb0bxlchBMleeKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b8c1383b.mp4?token=HSWOe1KsS47lsHFY9ryRixzouUzhP4IFywbxzoHvMRkQ7fA1SqJ58la7bU0nVn1xCr5RqX6X-90ZOSRUbycsHTAczVaOSFOtIvCzAx8vnE3P1_7_fOXrJ2o7VxOnC-i9j9R2vIlWpIwxgmVQ8EPglW5uC0Zya_I9rf1rz7kr8eH2dzdPHL_RePh52hoPFEUxhoQ9qVKwv0-QcDp-W-yZndgu1z2HFk7743jm9LRxT_zcF7tdmtgMG7VL22XHedttUgPF97YXhdofgAC9HyZpPIaSLWGsiuMOif62OKn7Ylhv_6LD2FgXncu0SY-oXgD5zGJxRfxwRqGsnsqaBO0JbAnBNvorb1Qqnp9cJcLyrlbnViWZHMSUGSDAEGrZqjKSWj3y_EO1b3wgDPxqFXKDEKUFe3verUt8VCgdpgsf0PfFdy0oJ89YpFhFnH9Y2j14VBvAiWBAfb0TkQP1_Okl2cM0u5VrG7gkj8Hq4hqWhwYG5LaUttktrHKclguFvmk6QV_Sitg280RDZhpMMbXRsruFVDjBCkmcfb7TZP0NFO63MM_2jqls9WCuM9eZ4IUwG42CLRWg7PJEwuhdEhST_-HF5KE_wsR8EHTq9wVVTekztGNrdPSLw4r6A4CEqaf8I9CDZ8mKFV3dFrVjfg8XgZY844cwNb0bxlchBMleeKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس صنعت: مصرف بنزین خودروهای داخلی حدود ۲۰ درصد بیشتر از نمونهٔ خارجی است
.
🔹
بیگی: در ۱۵ سال گذشته موتور جدیدی در خودروسازی کشور توسعه نیافته است؛ یکی از اختلاف های جدی در حوزهٔ مصرف سوخت به مسئلهٔ موتور برمی‌گردد و در این بخش اختلاف ۲۰ درصدی اصلا رقم کمی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/457735" target="_blank">📅 15:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7dbc8d28.mp4?token=vu9406xroS6EsYp6DW0pO-TNTN6x6XPVkeHuJc_59JJcHtJWSQiyQ01IB8QApRifjEROcD6Z-CK_-rRyu-_XFd28JAKYrrvafahsu2gsw31hoDNj1zxebk4tXi4wktTqjKP5-psneC6hnA_N094hpJT_M4wr3YAYaBU91b3T8VFOi6zfkaOnamnbuIHUUd--We_nFfOtkqel3997zsKqpErJ3qWZt7XoGOBRgjqqhh3pA5N7VV1uNdYeddqOi3iHBRXZ_vTSpQHuSJ8kYMMp_EoPftTJXsL8Rt0hktHKSkzy8okV40UtNGqtimH87pe7D_1Is3JQoocGdRSEoDCehA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7dbc8d28.mp4?token=vu9406xroS6EsYp6DW0pO-TNTN6x6XPVkeHuJc_59JJcHtJWSQiyQ01IB8QApRifjEROcD6Z-CK_-rRyu-_XFd28JAKYrrvafahsu2gsw31hoDNj1zxebk4tXi4wktTqjKP5-psneC6hnA_N094hpJT_M4wr3YAYaBU91b3T8VFOi6zfkaOnamnbuIHUUd--We_nFfOtkqel3997zsKqpErJ3qWZt7XoGOBRgjqqhh3pA5N7VV1uNdYeddqOi3iHBRXZ_vTSpQHuSJ8kYMMp_EoPftTJXsL8Rt0hktHKSkzy8okV40UtNGqtimH87pe7D_1Is3JQoocGdRSEoDCehA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجهیزات کشف‌شده از مجید آدینه؛ تروریست آمریکایی اسرائیلی که صبح امروز‌ اعدام شد  @Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/457734" target="_blank">📅 14:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMEg5eRULrf0NMdgmdylH_Q2VXQFZ3qbayOdG7bUmxkcvGCG5LSc7zree-hO1mfeY3mpO87Nos4qD-9i-ozLlTuYnI_zJ0omv7Tkb0_CA-o5UXAdVFRCXSHIgFR2dVtZCwutRXyqE8ih5xwulRxSSCmcSJFNV00EohhbHkHMfkbFxbPxQAEUk75ClRFXLLfF6vDc6xcQ5hgFrg3ssUCADhR0CNTx7vxcRjfq_Kgsbo9okj5Ne9zBa3qNBhCf7mroYtiG8e-M1PQZebkL1KFct9naES86q6Vmq958mppQOfow4pZ_9IgP9qqVM9rJB4K502tIj-KZtLnDLuk5B4J5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت مذاکره با آمریکا از زبان نخست‌وزیر کانادا
🔹
نخست‌وزیر کانادا مارک کارنی امروز با اشاره به شکست مذاکرات با آمریکا گفت که واشنگتن خواسته‌های «خیلی زیادی» داشت و در مقابل، امتیازات «خیلی کمی» می‌داد.
🔹
مارک کارنی اعلام کرد که کانادا از ۸ سپتامبر تعرفه‌هایی…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/457733" target="_blank">📅 14:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97fa8afb5a.mp4?token=RPw1D6q7jTXCEOB_Yvx6z7j16eg64EfDgxoe0hGVNm2HvQr-32CAmQofOZnkPhbs-0RQ2snBghh-A2L22ndhmVICoee5RPLni5wW62PMn4LSC_TdrH0cChu8hbSFMdmfrSj5ED-LK0hhFZVsZbrN_yDGX7WeDjGvSWN7EfZCBKcr131ITLqb9g8e4lJR7wFcpNpSxeu-Vx_SY7rYxrNhEd08JVwHTTCL7mU-9Opl82hznh3O243EhzmvbZPAcA6oUh-Q4UYPgDV7uiud2lfHq7JLzs3-6MH4_AWdjmOdziehMsDELqA4dqc6o1U_Psf_3HG4Ljh2dWBPQdSFCry22g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97fa8afb5a.mp4?token=RPw1D6q7jTXCEOB_Yvx6z7j16eg64EfDgxoe0hGVNm2HvQr-32CAmQofOZnkPhbs-0RQ2snBghh-A2L22ndhmVICoee5RPLni5wW62PMn4LSC_TdrH0cChu8hbSFMdmfrSj5ED-LK0hhFZVsZbrN_yDGX7WeDjGvSWN7EfZCBKcr131ITLqb9g8e4lJR7wFcpNpSxeu-Vx_SY7rYxrNhEd08JVwHTTCL7mU-9Opl82hznh3O243EhzmvbZPAcA6oUh-Q4UYPgDV7uiud2lfHq7JLzs3-6MH4_AWdjmOdziehMsDELqA4dqc6o1U_Psf_3HG4Ljh2dWBPQdSFCry22g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ حذف حبس برای مهریه‌های بالای ۱۴ سکه
🔹
ابوترابی، نماینده نجف‌آباد در مجلس: طرح اصلاح نحوۀ اجرای محکومیت‌های مالی در صحن علنی بررسی شد. با تصویب این طرح، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف شد.
🔹
در خصوص مهریه‌های زیر ۱۴ سکه، امکان اجرای احکام از طریق…</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/457732" target="_blank">📅 14:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d41e31642.mp4?token=WBK4zqyX52uOZDa2f3yFiTxhcrSOIezy4w4E5LGDx36rp6tf2WZwBfLFAm4U7MGue7W51mfJGSrn1jAxOV7DiHGIp7cOY9h0IX-1Z3OVGGB4oUr0kPNXFlJVfV6eDstiQezLwasQclvNReNTOisGcUeMPzaqz0Nj_n4x5Cn2n6ZcG7VG5motvbwFM_Qf5GekLaaaMCwqiHv22AbWhSmDwe-sZMbg0Xrq6vDdvs0A4APYlZE8lWORSV7XonyLkarzZXssScfpbheBFnNhnrz9ljIJAlwqVYBPKfs8XlXd1cbazOmZ1oTf3k9r7kV0w4RPWr3U7YFiIV3XRim-SNaEHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d41e31642.mp4?token=WBK4zqyX52uOZDa2f3yFiTxhcrSOIezy4w4E5LGDx36rp6tf2WZwBfLFAm4U7MGue7W51mfJGSrn1jAxOV7DiHGIp7cOY9h0IX-1Z3OVGGB4oUr0kPNXFlJVfV6eDstiQezLwasQclvNReNTOisGcUeMPzaqz0Nj_n4x5Cn2n6ZcG7VG5motvbwFM_Qf5GekLaaaMCwqiHv22AbWhSmDwe-sZMbg0Xrq6vDdvs0A4APYlZE8lWORSV7XonyLkarzZXssScfpbheBFnNhnrz9ljIJAlwqVYBPKfs8XlXd1cbazOmZ1oTf3k9r7kV0w4RPWr3U7YFiIV3XRim-SNaEHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیویورک آمریکا پس‌از بارش باران غرق شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/457730" target="_blank">📅 14:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=j683ejysHu6faYlQC07nmZzjSmCWBRK3dzLJ0EVTv2pdyaDFW0-a2zl3d_OEMFDJFR4a0jb0UVh_1KYpl9lwb-T07Q1LZqVAPwp6UZ3rjD3VBHcqzifUcGi-eqdZMm_0E65UzkyVaslbESpM9dpC6OCMEcoFKZ4PNYwN0zHQC4ROps-cdN3_-K_7e-PUNp6OoELAa3rNL2fnnKFklkpFVX3UDUq-B-z3egBcM73xXME8HkJMevT0xKCB5WaGAAxt3TacLX-sycYQ5xdHT1nXfTUvhDrOuGsj2j10rhRG6UvFGR5YR408DZ5rTdE9QSDZ1DlRUi0eKuCJb6Z6oGuT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=j683ejysHu6faYlQC07nmZzjSmCWBRK3dzLJ0EVTv2pdyaDFW0-a2zl3d_OEMFDJFR4a0jb0UVh_1KYpl9lwb-T07Q1LZqVAPwp6UZ3rjD3VBHcqzifUcGi-eqdZMm_0E65UzkyVaslbESpM9dpC6OCMEcoFKZ4PNYwN0zHQC4ROps-cdN3_-K_7e-PUNp6OoELAa3rNL2fnnKFklkpFVX3UDUq-B-z3egBcM73xXME8HkJMevT0xKCB5WaGAAxt3TacLX-sycYQ5xdHT1nXfTUvhDrOuGsj2j10rhRG6UvFGR5YR408DZ5rTdE9QSDZ1DlRUi0eKuCJb6Z6oGuT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرخوش وزیر نفت در اولین روز هفتۀ دولت
🔹
ثروت عظیمی در حوزۀ ذخایر هیدروکربنی کشف شده. این پشتوانۀ خوبی برای آیندۀ انرژی کشور است.  @Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/457729" target="_blank">📅 14:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daa67aabe.mp4?token=Z5q0E5srNgfLJp30HK5drX3Re1SFwMnoktXZL0xxlllYgBfasgYIa6Z0-7IB8bGzldI9s16Qd9PKGpzTlrEJah-BhN0NIzWLs1ZtSuChFUdzV1te085zcL0qOAzF_m0C0lumadoMmZIhq_-Omzglz6Lfr5Tw6pQowhoXPItiXj5szNW_ogQoXikTNWLU8xRg0b1SDW4yg40fhJVFCp3SyJEP1UCLxiYyMn44olZ8vCIkJtmYs09a5jOHp5HfkSwlDvynsX5f3pLpnKjT8K065EkukGFRe8Bev_BE2eaQKbGcaQoeoE9Dvrv3njdmlvIwAFdipKQZtU5XT4DFfXEfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daa67aabe.mp4?token=Z5q0E5srNgfLJp30HK5drX3Re1SFwMnoktXZL0xxlllYgBfasgYIa6Z0-7IB8bGzldI9s16Qd9PKGpzTlrEJah-BhN0NIzWLs1ZtSuChFUdzV1te085zcL0qOAzF_m0C0lumadoMmZIhq_-Omzglz6Lfr5Tw6pQowhoXPItiXj5szNW_ogQoXikTNWLU8xRg0b1SDW4yg40fhJVFCp3SyJEP1UCLxiYyMn44olZ8vCIkJtmYs09a5jOHp5HfkSwlDvynsX5f3pLpnKjT8K065EkukGFRe8Bev_BE2eaQKbGcaQoeoE9Dvrv3njdmlvIwAFdipKQZtU5XT4DFfXEfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سوال از وزرا: آیا شما از تهدیدها و محاصرۀ اقتصادی می‌ترسید؟
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/457726" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae5e0523.mp4?token=uz0pRsrc3TdLtou6vvPMSu4Jakb1uN8tWSnN58OUT3VWZABfj_b4gIHmrL7OzQyCEmz5PHXUnThk_OibOcbfpEvhgwulGKxfPqzWLAtiv0Fj5IsVp5iAXStGejDYh3oJ123mGun-gFmLVpC8MYM5nX5Tt25wALOGoCBImAGrCBmZyZO3d3eSsBOywIb2MhF4UjmHA8G0WCjhzeQDLSO8Tqj1HBqlQBock-hkmSIfl89uR5KteTl_8TP-Brl1c2BckcyKNR1uzy4ms1JW5dmRDsCveeHTLe22b7HfMsk2nYi2O-WgRjwZ8WHzK9qNCNciir7k6KXc6fW5OXRd-38T1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae5e0523.mp4?token=uz0pRsrc3TdLtou6vvPMSu4Jakb1uN8tWSnN58OUT3VWZABfj_b4gIHmrL7OzQyCEmz5PHXUnThk_OibOcbfpEvhgwulGKxfPqzWLAtiv0Fj5IsVp5iAXStGejDYh3oJ123mGun-gFmLVpC8MYM5nX5Tt25wALOGoCBImAGrCBmZyZO3d3eSsBOywIb2MhF4UjmHA8G0WCjhzeQDLSO8Tqj1HBqlQBock-hkmSIfl89uR5KteTl_8TP-Brl1c2BckcyKNR1uzy4ms1JW5dmRDsCveeHTLe22b7HfMsk2nYi2O-WgRjwZ8WHzK9qNCNciir7k6KXc6fW5OXRd-38T1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعاهای تکراری رئیس‌جمهور متوهم آمریکا؛ ترامپ مدعی آغاز جنگ اقتصادی علیه ایران شد
🔹
رئیس‌جمهور آمریکا ادعا کرد واشنگتن «خردکننده‌ترین عملیات اقتصادی تاریخ» را علیه ایران آغاز کرده است.
🔹
ترامپ با تکرار ادعاهای همیشگی خود، مدعی شد نیروی دریایی و هوایی ایران…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/457725" target="_blank">📅 14:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roIvS2i2n6QL6fVfXQGMNoX7cpUsAN1L4207uWcPcsWPgKQ8WZrnZzpN7874Lx1exEWR8oYhMnrnxhZhY6nklGCDiY7rWorXDYL6wV1Ipwb_WdrNAdPHTI_NEDghKRgbcPAkSK6IxfMUI-iiqQ5IBrS8-yp9Au5fj1OndJwokM2MPjA7jcFzduA0DMWczOZleh0ORLwsSLMdKD4-4_VfwN5u87KLWOQu5FRBJ4bc8rDzArk242UPR0iyM2N9QqHWc7Jk3le2MW4c6KtEXjZFkL9z_EejesonNcXIlKhFNP_XaU0To7ZDE1qZv2Qiefcn2fQj2IVyrMyzvD-XisEeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آبفای تهران: ذخایر سدهای تهران ۲۶ درصد است
🔹
ذخایر سدهای پنجگانه تهران حدود ۲۲۰ میلیون مترمکعب کمتر از شرایط ایده‌آل است و میزان ذخیره سدها که در ابتدای تابستان حدود ۳۰ درصد بود، اکنون به حدود ۲۶ درصد رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/457724" target="_blank">📅 14:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457719">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAzOxgeyUQSstqNsd_L9O7o7q-FnMmFa3QuCe6MmKXFdV3y5NCPygECKarlJ-NXG81ld6H1-c79UaZVZP8sZf5TtcHsd3GyyzG5yjnWc8Wu5eFs9hxMQ-Sozli8-3qaThlhWPonvuymvPog6keFECKEcdFyS920JCKoZO_CMs1GBZB2vQcR-dBpOE5rGL05HCMPNQOEy_lLJhy0-PQgukRtGzu9_hEy5cxXBmA38fI3Q5oKg9kSuVT4K75JRRf-Vs03iLfj2gtvI33VeHWAulzIFAKvQDRy9jYhC3KJRPmHYdM8KySMgH-CmRjDE2rrJop-4ePpQ3A-ynSBePzrd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCZoNDHlxIm7a8_rz-S7fpOhvjAh8S5Ei_wggdxjrOhI-0-7EOOa-JhXtllxPKGJ-t7fEyCphEzG7EThX2_JnoQS-y9fEU4Qe0wOqcLtSQM6oDciMxk9iz2cOZPiCQO4UgjZaOXwrEf8x7kE7cZTdun4ymKjlBF1cd5cOlaK43seZ5wLKoLsrMbfPRgAyaTYmUV7GyFvuHtGKiMVfINZd5oRFHFt5h3GdWYRqjy2-Czd9v5ruMOJPeOyVyeR_k0YicTy9pNQQ02K8hP3QaAl7QD9SF2NlllNYU5BPqx1IXl0ECRJjxySAevObt3J4CRI_2g8xvM5UVGqYb4rqEu9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mhVGtTwFso3tPVoj46kE1x-Jnprk1bivqpwVMlIFqDX1zS2ppq4d6F-LtC3JkzbTu756eVS9noQkAS9pq7Xxg3eF5SmIFy2GnU5QTPAFmoKj_is8BwVWIoFYpUr3-ETo8w-pG3oMfN61jkI3yA1pata0MXlvMv1Yb5c7a8wPL4wHQ5wqLr4K6yr7NA9VFyp2NnxsE3Gcq1Z1XzjE0HPWUKcOF7AyCpu-aHMW9jPP66CEllYnxKnp4x8L-54XmfVpKhX1lWJA0AlcHceKlzwr_wV66aMOTb10-GEurlecBQ60SSMLIdg-oii4MpVyQmAQfRmIBbPkn7rYWSVR_zQosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAPRhWY5y3Nq6AlmSN-9LqSVdchWntoDLNAK0cmvCVQTXfYexkVDMVenV18va_ve_--3Yhhun--Ul_eojlvBkM6VjZX_vLBtnhedFNxmR7KX_s8zXKTrWqvduuD55h09efmvGSH25lAO-IFqQQIaIwMwAeHeQeD8rzuFROE1jMNNYhV-AUqtaGIyhg_e3mWNGQwucLKf9HhP3MuwgE8VWrDyWXI02VCFBNAh8K69-XRN6RUZxGeviyWjKM6qJzC2AzR6oAi8QwAyVa1c_IrFS7ArDgr9oz6-t6zpWi-jGh9LyMvg8eZhCJsbB5Ngp9YGI-OhTl9XEyMrHAdK4lPm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiwY17Ne3-D6FUU2Mf4kdhc1DG5cc49s4Sw5nLl3jzdcfJ_zMVRGlG8XRU4s4e2wu9kjBjv_yBkZt8zhEuNOem1a-pjy5dEbR1bU4eUMjrcI4K7MB1fWOk6f4dBVThN3UPWc7wqXm1KAgX_y--SYPLy6HwGCR1MOyblgAghBa5hzeQ-FRMH8tvJkDkjDXGYtAWshDxx-7a0yNL70_k_gpSLCpcHRj8lT0QfgnGanRWVvnpRVmeoWWNgzxeQJ-dYHO2y-EFZUFMb2DpNbnIBrsHskggu1KTcdZidd-8PTmhcWP5bvGVy8PqcMkcYDVDJp1C_7TZkHXES53O1S6l0-Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزارع کردستان زیر تیغ برداشت گندم
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/457719" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457718">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5c3ec98b.mp4?token=oFJy0uzDpvLiMR8cEQNPxgeUAOBs-vqDXggbrbuJDKWGUA80bHFCemw5M7k1f_A9yIw8-NEsxvpRuVCVwsNcpg-Q-S61YcZ3lQBJuE1tMbqH04U60UDxSGu6lXhuqhtyGBUgxg4RyLhFA33EZqnXHhnoKA6ctBz0eb_-NUuGZBX-UsiXPe2w6UfAe3GLHXajBZebfw8LFT2ZB5KK3c4C4p2OVK7HEXklxzeBIPJHKfazOAnP3vSLwe2HySmqb1kdUPO_tRJGGD6vzRWkcP0T9umraBQVOMfuVBKNsclo-CyNc8JkLOuZ04FmIyhFvl0X37HZf0-MDfqM7KFOb2M-Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5c3ec98b.mp4?token=oFJy0uzDpvLiMR8cEQNPxgeUAOBs-vqDXggbrbuJDKWGUA80bHFCemw5M7k1f_A9yIw8-NEsxvpRuVCVwsNcpg-Q-S61YcZ3lQBJuE1tMbqH04U60UDxSGu6lXhuqhtyGBUgxg4RyLhFA33EZqnXHhnoKA6ctBz0eb_-NUuGZBX-UsiXPe2w6UfAe3GLHXajBZebfw8LFT2ZB5KK3c4C4p2OVK7HEXklxzeBIPJHKfazOAnP3vSLwe2HySmqb1kdUPO_tRJGGD6vzRWkcP0T9umraBQVOMfuVBKNsclo-CyNc8JkLOuZ04FmIyhFvl0X37HZf0-MDfqM7KFOb2M-Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ معوقات بازنشستگان تأمین اجتماعی این هفته واریز می‌شود
🔹
پرداخت معوقات فروردین و اردیبهشت بازنشستگان تأمین اجتماعی در ماه‌های جاری به یکی از دغدغه‌های اصلی جامعهٔ بازنشستگان تبدیل شده و زمان دقیق واریز این مطالبات، بارها مورد بحث و پیگیری قرار گرفته است.…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/457718" target="_blank">📅 13:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457717">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5ab0ce19.mp4?token=OKmfH2MTWcYiicV4fWMeaGZqniT1VK35D73CzQ18hO4c94XNFtmxitwTqZH42ffezdSKbT99YgON4nd4zkJwzam3p3Ri3xHclU-CHCon9n1lQX38Bf1a-G-C9pGKFODtVfc7nVgBY7Efw2x96H_fH3HGzdDKX9Lh6d4XGu4MQ0EkXi1GN9zNqKM-hxAuauhQnuVzj7xsddvFWttMzYDtFkcxfgMxjXMDd4H31BW9q03VwYpUly1o0PU11fD-Di8F0ItQZPY8EmdJA9-I5nJFE2BPPZLpJ79IFF2-iHu4IIWFxxOFQDGEWCK8E2s123FrQJBeKSTsIqvos4PnK-p_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5ab0ce19.mp4?token=OKmfH2MTWcYiicV4fWMeaGZqniT1VK35D73CzQ18hO4c94XNFtmxitwTqZH42ffezdSKbT99YgON4nd4zkJwzam3p3Ri3xHclU-CHCon9n1lQX38Bf1a-G-C9pGKFODtVfc7nVgBY7Efw2x96H_fH3HGzdDKX9Lh6d4XGu4MQ0EkXi1GN9zNqKM-hxAuauhQnuVzj7xsddvFWttMzYDtFkcxfgMxjXMDd4H31BW9q03VwYpUly1o0PU11fD-Di8F0ItQZPY8EmdJA9-I5nJFE2BPPZLpJ79IFF2-iHu4IIWFxxOFQDGEWCK8E2s123FrQJBeKSTsIqvos4PnK-p_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرخوش وزیر نفت در اولین روز هفتۀ دولت
🔹
ثروت عظیمی در حوزۀ ذخایر هیدروکربنی کشف شده. این پشتوانۀ خوبی برای آیندۀ انرژی کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/457717" target="_blank">📅 13:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457716">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b72d321d1.mp4?token=N6jNzRY7xjKOLXTGj_arbO6_TqLluEbgAeus-M3lCE0P4E9PAfWTUQMpdfIM-KUxhUXxqH3n5f1o6WKS3n0MoGF33lRStud0v1ERyGTBZNlwEytbHAkomvEIx8EgKONIGH0sX5ht_Ltd6mQk_B6B7gF5OYaA0FMY-BMU8o5wR6ndqlU5L6WxvKDT4STWqAOSHKCWFsTNrK5QTwegzlf25hR6l979F3qEyqojym9lwlOAlVJMRCahKB3SVMMYuiQKVswkdVGiBEqulq2s_oAG5eOZSSX_Jr1S1irRbFx4wHJniu3RHT1XeV_4E2HW8nDx0f0LBoNtuVA_Bt8asBT78g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b72d321d1.mp4?token=N6jNzRY7xjKOLXTGj_arbO6_TqLluEbgAeus-M3lCE0P4E9PAfWTUQMpdfIM-KUxhUXxqH3n5f1o6WKS3n0MoGF33lRStud0v1ERyGTBZNlwEytbHAkomvEIx8EgKONIGH0sX5ht_Ltd6mQk_B6B7gF5OYaA0FMY-BMU8o5wR6ndqlU5L6WxvKDT4STWqAOSHKCWFsTNrK5QTwegzlf25hR6l979F3qEyqojym9lwlOAlVJMRCahKB3SVMMYuiQKVswkdVGiBEqulq2s_oAG5eOZSSX_Jr1S1irRbFx4wHJniu3RHT1XeV_4E2HW8nDx0f0LBoNtuVA_Bt8asBT78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی تنهٔ درختان زاگرس به گونی زغال می‌رسد
🔹
تصاویر رسیده از منطقهٔ زز و ماهرو الیگودرز، قطع درختان و تبدیل چوب آنها به زغال را نشان می‌دهد.
🔹
به‌گفتهٔ شهروندان محلی این عمل در سال‌های اخیر افزایش پیدا کرده و رسیدگی کافی به آن نمی‌شود.
🔹
کارشناسان تأکید دارند که این پوشش گیاهی در تولید اکسیژن، جذب دی‌اکسیدکربن، حفظ خاک و آب، کاهش آلودگی و تأمین زیستگاه نقش مهمی دارد و روش‌های دیگر و امکان استفاده از سوخت‌ها و مواد اولیهٔ دیگر، باید جایگزین این روش شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/457716" target="_blank">📅 13:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457715">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی: با اجرای طرح مقابله با قاچاق سوخت بیش از ۱۴ میلیون لیتر سوخت قاچاق کشف شد.
🔹
۶۱۷ نفر از متهمان و قاچاقچیان سوخت دستگیر شدند و ۴۸۹ دستگاه خودروی حامل سوخت هم توقیف شد.
🔹
در ۴ ماه ابتدای امسال ۱۲۰ میلیون لیتر سوخت قاچاق کشف کردیم و ۱۲۱۲۷…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/457715" target="_blank">📅 13:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457714">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
رضا برکتی در برنامه سرآشپز: هوای فروشنده‌های غذا خیابانی رو داشته باشید و چرخ زندگی اونهارو بچرخونید/من در جوانی بلال میفروختم و به اون زمانم افتخار میکنم
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/457714" target="_blank">📅 13:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457713">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8UTEuesT1IwAJFkhjG-fQg_GQZkUo-irKlLeSherZakZRXxNPyAre-__ZXDS0pTfu5H-YnEZO7HYx_yO38f8ITr37d3IW84e02EoPgz5F0N1GnBDLnYbcvtiM-rrl3Ai4TsDk5NpQKGp4dPFsGRuWTrgzJAPAaZvKox-MyZCgx5y_vgGv_5yrhW9z6DvZJD0_nuLoplz27KGf8szPftHdb-HmtBPAcqsLBYqo8I-bSB07cD1KMNQIRnhRFZGHFKxZ1uiIFcDB_GaE6zwO8HGDR4wP03C4RmzJXIEezaadXstNKsUJj5pf46TZKcnmJhqGfNVjzXOXE4kiF9dueK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک ملی ایران در جهت پایش مستمر سامانه‌ها اعلام کرد؛
خطاها و مغایرت‌های احتمالی را گزارش کنید
✅
خدمات بانک ملی ایران پس از تکمیل بخش مهمی از اقدامات فنی و تثبیت زیرساخت‌های بانکی، به شرایط پایدار و عادی بازگشته‌ است. هم‌زمان، پایش مستمر سامانه‌ها ادامه دارد و مشتریان می‌توانند در صورت مشاهده هرگونه خطا، مغایرت یا اختلال احتمالی، موضوع را از طریق لینک زیر گزارش کنند:
🔗
https://app.epoll.ir/97455750
🔗
مشروح
خبر
…
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/457713" target="_blank">📅 13:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457712">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/457712" target="_blank">📅 13:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457711">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d07tunkLksK-xWlardTBGzXHhbLRSNviQ-nfHsjqCRfXALX3Ho3ixjNrIiLbnI_eB7jI5PNyXq9hNZnGow0noYFyIzhyRKnugUcui0bAvrDvUoAas0P5WfYUQsJUevvXF51ceVoOW5BlnoNKzATzZXos4gQmaEmB3muk5QREPtyoTIXGER619_qkttYU9eeRvaFgVLRB-tUEk2x6JpoVq26H7aAkKZWFw50y99IO8H_v-PyScOptNLMhmh-Jrq_aHSh0LBtCZrAzWYtz4p3sRmBpPkNLRuGPydwPtbLf9Yf-8c9NimRTomg4E2Pcf7rs64FkVbpwWLBXfAdZVhin8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی: با اجرای طرح مقابله با قاچاق سوخت بیش از ۱۴ میلیون لیتر سوخت قاچاق کشف شد.
🔹
۶۱۷ نفر از متهمان و قاچاقچیان سوخت دستگیر شدند و ۴۸۹ دستگاه خودروی حامل سوخت هم توقیف شد.
🔹
در ۴ ماه ابتدای امسال ۱۲۰ میلیون لیتر سوخت قاچاق کشف کردیم و ۱۲۱۲۷ پرونده برای قاچاقچیان تشکیل و ۱۰ هزار خودروی حامل سوخت توقیف شد که ارزش سوخت قاچاق کشف‌شده ۱۸ همت بود؛ البته باید گفت که سوخت به ۱۰۰ شیوه قاچاق می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/457711" target="_blank">📅 13:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457710">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بهروزآذر: طرح مصوب مجلس در خصوص مهریه، مخالف اصول قانون اساسی است
🔹
معاون رئیس‌جمهور در امور زنان: تغییرات در مهریه باید حق دو طرف یعنی زن و مرد در نظر گرفته شوند.
🔹
ما همه تلاش خود را برای بهبود این مصوبه خواهیم کرد ولی در نهایت بازیگر اصلی ما نیستیم و بار…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/457710" target="_blank">📅 13:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457709">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52364ba26.mp4?token=nyvu_TolegLAP3PwU0bDuugoPJB8oKMKrM4oHBGiTFvOxQNKEu_5IYrLLKVBROQwQayfFU1NAvNBkAkd1qA_Cgk995m2zl4d1Jz6d-IqqTTAx5lvMc_gPAIw0G8RbF_EutFjcxlWI01l6exhQfpoh6hF0YncF4QhA0TV6Ko5_QmbiPFpEuoL8w7hNxEQeDNF9Igw8SipbVVdJEEiUfefM04gN7RupNpI7k4Z-89YowpQSzGYm1zNXSgwz1lWviDgQB9Lk4oqwToSkfvZXabSApY0O4994Mn5B3NogVx3AMbehr93H0hxfxseUBMhlISripi1h_v4b0RpGokRlyVcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52364ba26.mp4?token=nyvu_TolegLAP3PwU0bDuugoPJB8oKMKrM4oHBGiTFvOxQNKEu_5IYrLLKVBROQwQayfFU1NAvNBkAkd1qA_Cgk995m2zl4d1Jz6d-IqqTTAx5lvMc_gPAIw0G8RbF_EutFjcxlWI01l6exhQfpoh6hF0YncF4QhA0TV6Ko5_QmbiPFpEuoL8w7hNxEQeDNF9Igw8SipbVVdJEEiUfefM04gN7RupNpI7k4Z-89YowpQSzGYm1zNXSgwz1lWviDgQB9Lk4oqwToSkfvZXabSApY0O4994Mn5B3NogVx3AMbehr93H0hxfxseUBMhlISripi1h_v4b0RpGokRlyVcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسرو معتضد: این خانم مسئول پوشک ترامپ است!  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457709" target="_blank">📅 12:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457708">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBlvPbfTIhujiy6RZ_cxPT4lXAO7bOUL3tBZ4EOeIYvDU7UlJvwq1HETjY4nJxXkdgnlyMm3hv_sSstoPBtvZG4fc_jaZM5Ax_u0zVnbrRLVnNEZWFL7E08EvbHhNwjGOYhqcAbYO1WB0kPLUoN2unOLc3MiezyfUbXCt8PjmBDkSC1Ydlt-TSOOpsBfkaGT4cLIgJF3MruimafsHePMVykQzcEGx4ai4l8ahYCs3yuxyxPI52ZAjPP8h54lHF7IBq6zfqnmo4_IkYBFGKyluU7ZvKzJlkuMwtLU-2RnV2XCfv4DGQRkOd1tHy03zEAYSMUV2DsXl3WoeLWgWYQwTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۸ هزار واحدی به ۶ میلیون و ۷۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/457708" target="_blank">📅 12:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457706">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c02276ea6.mp4?token=oW_avWHJboHV2dpH2rkGuzLY9rnXQHSRmFJqOW_D8LWIGlIssAaMP66O5VjhHqS3Tp3Dx5DE-ilcP3JqsS6bDIhxnik7ZAJBkgmGBOAI5LOtMztkOw1KTe4_vvGhtzO0dLvaoQ3yaxDwJU8yIwdkRBBGAa_3H6-JfhdVHBOCLbccYAFe8Ny0hHAtA30H4lF4QeCwK7uGzXep9-aWbsPv-i1iQVGYHuvie69MbvYrqSX_dZchX7WOtFBgkRLqSqjy-2npFhiE7wfVHRxDoqOK075Tv8BjAoS7y0wRL8Bs7QoIfHVwsZ0GQkEAm3aBR1e3S3w1ZcFqENWBwjUrcVcALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c02276ea6.mp4?token=oW_avWHJboHV2dpH2rkGuzLY9rnXQHSRmFJqOW_D8LWIGlIssAaMP66O5VjhHqS3Tp3Dx5DE-ilcP3JqsS6bDIhxnik7ZAJBkgmGBOAI5LOtMztkOw1KTe4_vvGhtzO0dLvaoQ3yaxDwJU8yIwdkRBBGAa_3H6-JfhdVHBOCLbccYAFe8Ny0hHAtA30H4lF4QeCwK7uGzXep9-aWbsPv-i1iQVGYHuvie69MbvYrqSX_dZchX7WOtFBgkRLqSqjy-2npFhiE7wfVHRxDoqOK075Tv8BjAoS7y0wRL8Bs7QoIfHVwsZ0GQkEAm3aBR1e3S3w1ZcFqENWBwjUrcVcALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در نوادا از کنترل خارج شد
🔹
آتش‌سوزی گسترده‌ای موسوم به «هاوک» که در ایالت نوادای آمریکا شعله‌ور شده، تا ساعاتی پیش بیش از‌ریال هزار هکتار را سوزانده و همچنان در حال گسترش است.
🔹
در پی گسترش این آتش‌سوزی که وسعت آن در کمتر از ۲۴ ساعت حدودا ۴ برابر شده، به هزاران نفر دستور داده شد فوراً خانه‌های خود را ترک کنند.
🔹
فرماندار جمهوری‌خواه ایالت نوادا با اعلام وضعیت اضطراری در شهرستان «واشو» تصریح کرد که این آتش‌سوزی «به سرعت در حال گسترش است و خانه‌ها و سازه‌های مسکونی را تهدید می‌کند».
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/457706" target="_blank">📅 12:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457705">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTxlRyCzn8-l-7Nma_JirqpnIG8S2hd46fi5AOdx7mGIfa3cEQJE4cwVTmMl_8yxqC04X1kYObXRcTdXhOIGQs3OaYXJDTvzjRuDvp582aqLu4w14wR91dahq547TjwxJjbRo6V6g8JbcEYyD_xkgppe9ztsWYJcOC9jxsh7sa0AgibMa7uS-ZlByqn99S0CE7jfK7LSqrV7UewGD3qy2ZIAdgG1QJuvK1FAdXhKiM7PJ5EWA5vLVO9IxA5-M8FZf7yLsNiyldCDerWJkSxYXpIi7-YJNFV3vq6o5UShzdrAA8ahO_1AWHjdLRJacfdFb7yckc1XCqhg-lW43KQU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت عربستان از رونق افتاد
🔹
براساس رصدها، امروز تنها یک نفت‌کش فوق‌بزرگ درحال بارگیری محموله‌های نفتی در بندر ینبع است و چندین کشتی کوچک‌تر در اسکله‌های متعلق به شرکت آرامکو مستقر شده‌اند.
🔹
این کاهش درحالی ثبت شده که  تاسیسات و نفتکش‌های عربستان در ماه‌ اخیر بارها هدف حملات یمن قرار گرفته و ریاض ممکن است نفت را به‌جای صادرات، به‌مصرف داخلی و پالایشگاه‌ها اختصاص داده باشد.
🔹
بلومبرگ دراین‌باره گفت حملات به تأسیسات نفتی عربستان و تغییر مسیر نفت به مصرف داخلی، چالش‌های پیش روی ریاض را در منطقه نمایان کرده است.
🔹
به‌گزارش بلومبرگ، مجموع صادرات نفت خام و فرآورده‌ای نفتی از دریای سرخ درپی تنش‌های منطقه با کاهش ۲ میلیونی به ۴ میلیون بشکه در روز رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/457705" target="_blank">📅 12:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457704">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIdswMqa0ipKi-wHVTVh7S-_-s27eDqmQ3Ku5Z7n84G0pRQSyy_lKaXI8QmkXHtdj22dVuUMLfzJ1gOZ0C25bK-K6Q3YMWBek_HQdIBd6YvpxIZWlCzw3DC7T6B5ctkTuj6jUSTcCT91DP-yjSKaBdK_CrrWlZA8yYay3IjFPPelXlNzqdErMVx3kh8w6ZEnamATVnmuAi6CsvDYB67WyZyRQXnEDWCMVtOJgxqJGvM3dvAFE9wIiGSO8vuuGUpZQUGfbLRgGVDi_xv3wKfULLfmGLZzHb0N7DC6lbXR_BiTtzD0jDJDuKgt9vdxfBLX04g9Mqa8fikPJOFbhjZhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: فلسطین آرمانی زنده و تغییرناپذیر است
🔹
فرمانده نیروی قدس سپاه: آرمان فلسطین، از بحر تا نهر، بیش‌از هر زمان دیگری زنده و دست‌یافتنی است.
🔹
توسعهٔ شهرک‌سازی و جنایات صهیونیست‌ها، تلاشی برای فرار از بحران و بن‌بست عمیق نظامی، امنیتی، سیاسی و اجتماعی در سرزمین‌های اشغالی است و نمی‌تواند شکست‌های راهبردی آنان از ۷ اکتبر تاکنون را پنهان کند.
🔹
فلسطین آرمانی زنده و تغییرناپذیر است؛ آرمانی که به‌یاری خدا تا تحقق پیروزی حق پابرجا خواهد ماند.
عکس: اکبر توکلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/457704" target="_blank">📅 12:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457703">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adca269943.mp4?token=rFOPl_kK3cYR6DBmGrgRgVPmVwZYBeBpVqrrQx5fNhCyiXlKWQNmRJJ0wTTmuqUgmc3fzXQUTss66zxU7smIcBU0NkFPlZg0sW52vfMG2WObmYn14tEntPfn9sWOT2fA_ZrAAby7cbCyb0tvqyn7_qsp8agXtsZsLbIa0YpR6pKWu1J91Ew4wh9XCLTdisHqIPKWL0JRiML9hFdwWTVCvR22nMvqD2Io3Cq4MJS91k9tRxjswrt010Eo0yhM8V6s9ZHNUZv_DOR9SeGYQbzrfSrr4cWpqGTQRE3bgqLDjqyXUyTK17H_Y3b1D-wW0DcyE2oZo3FZ92lKzWwzNb50eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adca269943.mp4?token=rFOPl_kK3cYR6DBmGrgRgVPmVwZYBeBpVqrrQx5fNhCyiXlKWQNmRJJ0wTTmuqUgmc3fzXQUTss66zxU7smIcBU0NkFPlZg0sW52vfMG2WObmYn14tEntPfn9sWOT2fA_ZrAAby7cbCyb0tvqyn7_qsp8agXtsZsLbIa0YpR6pKWu1J91Ew4wh9XCLTdisHqIPKWL0JRiML9hFdwWTVCvR22nMvqD2Io3Cq4MJS91k9tRxjswrt010Eo0yhM8V6s9ZHNUZv_DOR9SeGYQbzrfSrr4cWpqGTQRE3bgqLDjqyXUyTK17H_Y3b1D-wW0DcyE2oZo3FZ92lKzWwzNb50eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران چگونه در جنگ شبکۀ فرماندهی آمریکا را مختل کرد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/457703" target="_blank">📅 11:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457702">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762f3b7b45.mp4?token=KWdSZruTb0u9XKM3x_oBeVrUx2eidytc_07h_LhYDxY1hJHTVb5AkXgEJLsNgv32Ghtj_DGkLztkWrvwAzAzuO9lfAT6iVJz1o4T2jW1MmyGkgSPg8UZ8WX7tZKn-rAmiXVbjIcqYJoVPIiIPZMoyRPmEvy3mJMscL31qiM-CaUIdFwnAaedCEP7hT6t8O1SG5S8oYGN6eL1OGsMPirYyjlED1AU7HlIYERgMPy4hlD0V91co6OhkK6FYXY0CB3ZHq49L8Fqv4ixbyYzAMKcJzclhWzZtVGETOpRAWiGpHZqZcldgwYARDXsryvvcMYKzYySChCosPm5nTjPDC1r4iV6wKKkHgDYid5tqthQBGz9Urkyqpn8kLVTjbnrD37wsRbP60XatidgHmNHwDVmi7ZgjD5THmiSyJ8z_YCgJ7hEzaoV4ZfZs77s_F5bg1VIqxmExXPS855sAjZI-upM096x3AsWKqLpOnqeLIyuIULYsmNnHrFHm8q14qA_9yZVSyYPb31HOUybSdqzZ65lTnYvICrae0zZAO3-y27Tgp3KSxkGufRlKSa_aawHJ0Q3k9Y25zShk7P6f1RSAvxzSmTNV0PsrQkZjKRgFuFUFOvJi8I1g5skUlyTxDhfH-OTf6V17SpFl8GYX3mTLOm-i6Z5-Kz2leCX-0_WtMrxpAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762f3b7b45.mp4?token=KWdSZruTb0u9XKM3x_oBeVrUx2eidytc_07h_LhYDxY1hJHTVb5AkXgEJLsNgv32Ghtj_DGkLztkWrvwAzAzuO9lfAT6iVJz1o4T2jW1MmyGkgSPg8UZ8WX7tZKn-rAmiXVbjIcqYJoVPIiIPZMoyRPmEvy3mJMscL31qiM-CaUIdFwnAaedCEP7hT6t8O1SG5S8oYGN6eL1OGsMPirYyjlED1AU7HlIYERgMPy4hlD0V91co6OhkK6FYXY0CB3ZHq49L8Fqv4ixbyYzAMKcJzclhWzZtVGETOpRAWiGpHZqZcldgwYARDXsryvvcMYKzYySChCosPm5nTjPDC1r4iV6wKKkHgDYid5tqthQBGz9Urkyqpn8kLVTjbnrD37wsRbP60XatidgHmNHwDVmi7ZgjD5THmiSyJ8z_YCgJ7hEzaoV4ZfZs77s_F5bg1VIqxmExXPS855sAjZI-upM096x3AsWKqLpOnqeLIyuIULYsmNnHrFHm8q14qA_9yZVSyYPb31HOUybSdqzZ65lTnYvICrae0zZAO3-y27Tgp3KSxkGufRlKSa_aawHJ0Q3k9Y25zShk7P6f1RSAvxzSmTNV0PsrQkZjKRgFuFUFOvJi8I1g5skUlyTxDhfH-OTf6V17SpFl8GYX3mTLOm-i6Z5-Kz2leCX-0_WtMrxpAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلخ‌ترین صحنه‌هایی که امدادگران در جنگ رمضان دیدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/457702" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457701">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka0u9RiQ553SkDQ2NrxXbDS6SyfK8abmwgL_5qc6ntMkPqpDB5icYwOzpYWguIG1YwhGn-r8qrOWN18y7ADySCLJEumuSLh7M6-vTf79gj_0WXMsd3UpyK-QbcA9ZT22sBY_RXhEcGdqvRT7OTOmUuErEECTjXbSDFMiXjPTl3GyXRlF2wYvO9XTngvWCJNCVMvNlkw0VxQqYX-JZZHTT0L8zhqvaVhs7GXSaI2MkzCUc_mSOKTnEx8Ee5reLzTr3KeVTcg_BJ1pGoZvhsVLf9_fZR2irYhe1sHUegcrriZtUKDaBLuh_Yh06cnbfmvH9Lh1OOGqQQb7SOgFjn-pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: رشادت‌های کادردرمان در حافظۀ تاریخی ملت ایران جاودانه شده
🔹
پیام رئیس ستادکل نیروهای مسلح به‌مناسبت روز پزشک: تاریخ پرشکوه این سرزمین، همواره آکنده از رشادت‌ها و فداکاری‌های بی‌نظیر این قشر است.
🔹
از حضور مشتاقانه و آگاهانه در قالب گروه‌های اضطراری و بیمارستان‌های صحرایی در دوران هشت سال دفاع مقدس، تا نقش‌آفرینی جهادی و شبانه‌روزی در طوفان سهمگین همه‌گیری کرونا و نیز حضور عالمانه و داوطلبانه در مراکز درمانی برای مداوای مجروحان و مصدومان نبردهای اخیر که همگی در حافظه تاریخی ملت ایران جاودانه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457701" target="_blank">📅 11:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457700">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwuckm9CXij0bZIESFAeISLinuHA2ua2D-jvahj1hDA24TV8lLgFH632Bw1x7uIuRtEOjIe9Fw5jmEdarNAA4unZmENt0jTUTxc4TSTIJK-7sCInmu__-Zujy8vALfAE61CBRWDupVgYNgpHGfqDmdgBMO_Kc8e-lXaYQns05qR5gQifeZs0kBL4OKaph-hm08-_quNZPccCTJwUFz99m6CTfiLboaXSY3whg689U_yQddSXjLQqAGZ4k-DH2wjSxVqRDeUto1yiUzCERMqN_LJd7JiVKM3in_wWu9daLiJ3DuUa3gg31-XA3gb1_m5kzNEZRQ4UpD1HRjkvK_QyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز ثبت سفارش واردات گوشت از امروز
🔹
با اعلام وزارت کشاورزی ثبت سفارش وارد گوشت گرم و منجمد از امروز آغاز شده و متقاضیان از طریق
سامانهٔ جامع تجارت
می‌توانند درخواست خود را ثبت کنند.
🔸
درحال‌حاضر قیمت گوشت در بازار از کیلویی یک میلیون و ۷۰۰ تومان تا ۲ میلیون تومان است؛ درپی بالارفتن قیمت‌ها سرانهٔ مصرف نیز از ۱۲ کیلو به ۶ کیلو کاهش پیدا کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/457700" target="_blank">📅 11:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457699">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سخنگوی وزارت خارجه: عاصم منیر فردا به تهران سفر می‌کند
🔹
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/457699" target="_blank">📅 10:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7vrl4jhJERF540QVk3oxY0nd2Ey1WR2q7qioWNA401oOjo7jkiZsdlJljtrQcLQ7sP9oMIkxRaJhdVu3hr_GK0IIRni0-v-KA24MQaaqDnTXyJceoC_ueZGnXJU4-mvjCjYWw1DeETqrOc67nUGxF5InxPordL7eg4K5voV-MWDz4sgMhQjL07InwCGWUp_Pn7UdJ0wPjaWL0e_uNi6PuDosdTGYmsJwtIhsFEVxoO9CpBH_AKciKNq2aT02ODL4YJxvIBqyIxBqfR_exarit1z6qWyAMQBpJa8sP8aqSDT06CFX99TGe8rTNvddgzPf00BHsnIcgA8vl6niMgTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ایران به ستون فقرات حضور نظامی آمریکا
🔹
روزنامه انگلیسی «فایننشال‌تایمز» گزارش کرد که برای نزدیک به چهار دهه، زنجیره‌ای از پایگاه‌های عظیم نظامی، ستون فقرات حضور آمریکا در خاورمیانه بود؛ اما شش ماه جنگ با ایران کافی بود تا نشان دهد که این معماری به ظاهر مستحکم، تا چه اندازه آسیب‌پذیر است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/457698" target="_blank">📅 10:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRpcdIRXvTwzM3krcB1FWOmN4UQInLBu_uAtndVB7sjy92iiYDuxRknw9beE2JnBs03ZTu8CP8wFWuohaFBMmQXTlRgVWGAuQtEdNOU2OndeutjpjyZ1lKkBnAv4TAZMaM2uNzJTWYZHA7HDYWLW2InuFksEwO5_gXCeV2qAgMn2o5k9big7fBqEcTbGtVYi9x0xnGG9zQiEJKRRYgWbti7xMjXDmSprRbBPE1eDIm7R_M80sOG2J8A6h5YJTMs_Uir-ih_RM2YtYTfkCTnyMvw0_HsY2lE8ACojVU_SJehd7x-mc8soM_w99j0ExowEWYmk1HZnymg26W9PCTFReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرغ‌های تاریخ‌منقضی به بازار تهران نرسیدند
🔹
دامپزشکی استان تهران: حدود ۳ هزار تُن مرغ تاریخ مصرف گذشته شناسایی شد که پس‌از بررسی و آزمایش، مشخص شد حدود ۶۰۰ تُن سالم و حدود ۲ هزار و ۴۰۰ تُن تاریخ‌منقضی بوده است.
🔹
بخشی‌از فرآورده‌هایی که قابلیت مصرف خوراکی نداشته باشند، مطابق ضوابط به پودر گوشت تبدیل می‌شوند و بخشی دیگر نیز در صورت برخورداری از شرایط بهداشتی و سلامت، برای مصارف عمده و صنعتی مورد استفاده قرار می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/457697" target="_blank">📅 10:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دستگیری ۸ نفر درپی فساد مالی در آموزش‌وپرورش رباط‌کریم
🔹
دادستان عمومی رباط‌کریم: ۸ نفر از متهمان مرتبط با پرونده‌های تخلفات مالی در آموزش‌وپرورش و برخی مدارس شهرستان بازداشت شده‌اند.
🔹
اتهامات مطرح‌شده در این پرونده عمدتاً مربوط به تخلفات مالی، از جمله اختلاس در وجوه مرتبط با مدارس، فاکتورهای غیرقانونی و تخلفات احتمالی در قراردادهای خدماتی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/457696" target="_blank">📅 10:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de0d4f81c.mp4?token=py6ekz7DuqqTshSJHF2mXiJWsi2J4tJa0OcI8JZEWY0u6w1kwqIwjEiaGmJrDR8RGSkLw9H37nwppvFJkctUfSb051zy-wVC4XTJR5ZF64myfT7QKfrTcrsxSRk1b4o5trDUub20iW5-bdViNL1ZbhUe9huQ4v5S0sbIXXNMIUfUtBtydE3KslBDM273W8BGy5rAhxjjdzXCVy37Hx-r_5hM-FMdKR_zG1N8LpdeXNPXiKpwehg1mKZq1MNCLDGcrOosWQwt_yGRQDUfKiZk4rLFUqPffq1sDeEEUeUNxxBLL2EJGy0imUyycPLKFYD4xeMjBhD3snOkeVMt7p0YWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de0d4f81c.mp4?token=py6ekz7DuqqTshSJHF2mXiJWsi2J4tJa0OcI8JZEWY0u6w1kwqIwjEiaGmJrDR8RGSkLw9H37nwppvFJkctUfSb051zy-wVC4XTJR5ZF64myfT7QKfrTcrsxSRk1b4o5trDUub20iW5-bdViNL1ZbhUe9huQ4v5S0sbIXXNMIUfUtBtydE3KslBDM273W8BGy5rAhxjjdzXCVy37Hx-r_5hM-FMdKR_zG1N8LpdeXNPXiKpwehg1mKZq1MNCLDGcrOosWQwt_yGRQDUfKiZk4rLFUqPffq1sDeEEUeUNxxBLL2EJGy0imUyycPLKFYD4xeMjBhD3snOkeVMt7p0YWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من آمریکا را به باتلاق کشاندم و حالا زمان مرگم رسیده...
🔸
پویانمایی به‌سبک ماین‌کرفت از باتلاق خودساختهٔ ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/457695" target="_blank">📅 10:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd6b195c6.mp4?token=ddBEgeAQmdoyxY57fc5OQHuQBTjchRbs75HUPaYgImnQivRsMLr4P62Tghlnrtq2vp_Ae0QM3bgkeLP1O32FEPy_hflTAsXNmNEe8zqJvRQ7z88hV3CCYBAlXTaG8eT_G6xwj3w7auM5pC37yQaWfhRVmR7BkzKuasXomHTedG61NqfLuGX2ebFyk1EXwtXeuE411kMS63eslXKr_VS8oAtbWJwDwFW32Znl2SGHGw6Dh7UiwO6wsfIHgYl6dE966FcwqiHsq7opy3poVh5yvT8Ns9c2Up0cvGgfkev1W_clYqmWs6_Mgk5SX1oYEGtKsa4V0UN02jpYU0lYt0h0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd6b195c6.mp4?token=ddBEgeAQmdoyxY57fc5OQHuQBTjchRbs75HUPaYgImnQivRsMLr4P62Tghlnrtq2vp_Ae0QM3bgkeLP1O32FEPy_hflTAsXNmNEe8zqJvRQ7z88hV3CCYBAlXTaG8eT_G6xwj3w7auM5pC37yQaWfhRVmR7BkzKuasXomHTedG61NqfLuGX2ebFyk1EXwtXeuE411kMS63eslXKr_VS8oAtbWJwDwFW32Znl2SGHGw6Dh7UiwO6wsfIHgYl6dE966FcwqiHsq7opy3poVh5yvT8Ns9c2Up0cvGgfkev1W_clYqmWs6_Mgk5SX1oYEGtKsa4V0UN02jpYU0lYt0h0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرطان‌شناس برجستۀ ایرانی: بعداز اتمام جنگ تحمیلی ۸ ساله، مرحوم هاشمی‌رفسنجانی گفت آدم‌های جنگی و جبهه‌ای دیگر کنار بروند؛ وقت سازندگی است
🔹
پروفسور اکبری: بنده در زمان جنگ تحمیلی ۸ ساله، مسئول دانشگاه و بهداری بودم، ۱۰۰۰ روز در جبهه حضور داشتم. همیشه ساختارهای سیاسی زورشان به ساختارهای خدماتیِ صادق می‌چربد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/457694" target="_blank">📅 10:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457686">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4P2pYjmnpjQSZqw8rD5fBJbM2f2o9obvzYkX4YUyQtTk6DFVwyODTGsnuRrGqDe6E-GsPxPorh3y8IbKy65JKITUmi_TMcymTlr2vYsgJ42qrLzBbc0N6Ao3PVaUn_iuALEEJPo68f5ndwzqrddutMydWApyMrmudA1vit8jaRueFzTif0goIB_b0ZKknNX3nU4wHtUh8txO3g-vBLc3ITj7ovQxi54wubz8uP4I7It-kN0uelf56P9JtqksHpsiSGu0o62rFepxsnPS6Vkp7M03x37sqbtcrA8Mar-OVEmrjAOFLnvuCPe70HO7JIr4ALK-M5c-olnXjA57mHJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bO3MzwOAtQMFIAIaEkC8gLcMSfh7z4h2ql_-KH8S9wUKbSoZIbyGUUu7QHSq8bEnGPgvUitZ4yDzW2u0QqkDtY729CLEozlWmNDxVEvLA2zAdjgloJUbU4kt6VdH0c1-Y_Kcq4FOjbdmpCUDzaV7ZutO237l3aeSyAxXd1q-fdiMaNC-T6YG-xtUYkaLAOqEsB73o2uXi-cOA7HzuxJhM1VXmor17f5XnyiTGkLu9ABp5URIBtdsNoGGDwN7MKkK7H5KaeiyGSS3qLU_77BDG9lt4acYeg_mSVA8N-70bTKK8AAE9iKpxoNsAJL9253Ueiy3UxUFML3a1lhSvAySlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHktnhSDIPJs-0fxY5Ofb2SmndO3mEk1csCFVtzQngV97oz68y3NSvjlnvn3YvpnhyFM2lnhRE_gcrki35j-br3qEGJbO7xW_K959rJM21p-43I6LIgBPhsrBkKzi5L-UcmkXKZtyDI2S_e31tAJ-7QyOJLTTWnfCBEIPlYVbJI7VvYoKc2x2KptosYENAziS_2VSg0pFe5QxJUKau_EQr-opLi-eIfkEcv3XnRADibyWOG9tPTOxZPdJMLSgAZeCYyFvWOKl3jCLL-HIgu7PZOMadlpLRGepGRRKVEIDtgN7lNrxFPqEfqGbYsYB9O_dYj4JEQdrOigWVF1eQua9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNapineyVPnQjEmntEf3EtJlGwG57joflqwRMB0PPSMxahwCOnsxeFRqyfJf6X9cXDNhcnEC8SbFIl9W6X0wuWUmdmYamwbxDRsE2uSvqn7Vr79wVN94QpfL9sM9QJOnj-a6vtTwrDttERmBs_YFa4f72JnAxL4ZppqtwxfKnjuCaCbJ0HZu8Bd_Y9Q2O1JhcrKFBQgwEScstraISUX4VUtyQBb00kxFOxG-vWm7I9UBxA171B35PCEOV2mqycYemzqwZKZL8dwHt7vEwqd0spXYhNTtHdvCHiBQY5rfxXr0vK4GkFmTOiSrfjyLqOpp6H95K5BK7hubYkpFG9_C_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5tX5AmbEGI2o20tPALU3qLTmpF_SOxEt-Ro8LSUFJIVvj9FiS5zuNbzAAILMzToQgGmli4tpvoUU0MY0dtFkKsGTuUpBkOjUGRQziCGugzUHlnKibRwxxov42OqSV5eYZnRLWoQ6HrhjDpr3U5xuExxzbURdwf-RQHx_oiZZM7seIy-6ofO4jKW3fENUQ2r63iw6gAkmPciSN9cNwV451gHLVkhX95n6JzeDS8YLgwOaq77Obz8UusiCz9Ix2OvZ2CiBRaNowWhng-ZXjI5q2M-k2itslNE0gGz3YVM5QuiOCeDhvtNm9-Hvx8MkFCDSxkp91TjqNkgMOvcUeM-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUAXakjszbfwd0Gbjh9lPjHFlZCoTzFMC7QOZqVJdqLEAeflF2wix_mUKDWr3FDZd3LOPsWLUtV6eFS2c_shpuH6MPFR8HwqukDjSls5oQlmEKox9Po9DwjBEkiiMnyreE3NGVp38aMYW-KqalH4bJYFVEGxb-HBIxCYyapneiKCZmF7aGOaPR4e3sn_I_4YzduxoHaEKlYVKYnVs0nZMzQuG1QTNaqtWPXlndF-7-Vf0vwPzPZy1gCJGOvds4rmRbwdbTgUZxar1YAw2duiCuvaFii7WhFpdrU2KFYne4nc-BBgJVpnRiLppnM5HhhlorXYAEc1ubx9PpQ9JQ5c2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSEuDFfXVAEjIHWallX--_ne4nr_g1QsSyzdJmsoVyaFz-IlYWKbHfL8e9L8oVWhawkDQoXYMQBnR9a9uSL_OxgjaIeOycAl5FodQt98tvHuFto_RuGQLFM86jsJHpKULQ100W9-bn04dJO2PyGI_rRN3n0Lb0ta8F-6SuCI2gY2jh3OcAQ8TOX4prK37EeTqcBTqzZBhDjcQ2z--QR3Cy15cqiuw7SRw9Zx4bCdoerIp9iXt_7bZm6Ilx3fl-Of88VbPaJm-KBeqYrYRpXDKJPGaxnOZ8u9fSBMOcWjMYY4xOpVQ4LZa9eHK7UaySaTEQszeXBR5Q_4m61ta8lg8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت بوعلی سینا در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/457686" target="_blank">📅 09:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457685">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4880804d1.mp4?token=flZa0Ud4RaxOs701F8CVWVOnBqAJzVmAio9h8mx_yK7sI33X5yAUc0z4hZGxX3Ba36ISadgxanMeKMWuiNyjJs705ClnE0V3gmTwvHjf0aHp4o4OnxBV-i2Da8Y16Jf3mTxnbnMOkDWG6KToxSHZM8XdsIr9vgvELIqtrrtW90ES7BGzNPcanFv-1X1Zulu0W1qfYhM9ZqEmobhhGKkQr-ZxoPncHfVqFFebR-tCXRLSsf3Apoq2dRdvusUU3SOTCVW5hsR-ZDIJ8tDD4Arpy0MoLeC5kWKwyV4QH6QU_1rJspKNwglhM80yRfeQ8Oi3iQ4jjLImE2uSXr9EtB-BTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4880804d1.mp4?token=flZa0Ud4RaxOs701F8CVWVOnBqAJzVmAio9h8mx_yK7sI33X5yAUc0z4hZGxX3Ba36ISadgxanMeKMWuiNyjJs705ClnE0V3gmTwvHjf0aHp4o4OnxBV-i2Da8Y16Jf3mTxnbnMOkDWG6KToxSHZM8XdsIr9vgvELIqtrrtW90ES7BGzNPcanFv-1X1Zulu0W1qfYhM9ZqEmobhhGKkQr-ZxoPncHfVqFFebR-tCXRLSsf3Apoq2dRdvusUU3SOTCVW5hsR-ZDIJ8tDD4Arpy0MoLeC5kWKwyV4QH6QU_1rJspKNwglhM80yRfeQ8Oi3iQ4jjLImE2uSXr9EtB-BTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشک ایرانی نسخۀ جدید درمان سرطان در جهان را نوشت
🔹
پروفسور محمد اسماعیل اکبری، سرطان شناس برجستۀ ایرانی: ما در سال ۲۰۲۴ میلادی، برای اولین‌بار در دنیا، یک روش جدید تشخیصی و درمانی برای سرطان‌های پیشرفته و متاستاتیک (جامد) معرفی کردیم که سابقه‌ای در جهان…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/457685" target="_blank">📅 09:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457684">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948f9ff060.mp4?token=owVFg8KbWk7Kk8XK9GJbpAHDS1DzEbD0SO-JThTyzzCqq2RhdKscDN0c8RE3BudlnYxsqEoskzryJt16InmVjyT2FF1h3UYwWRLqgtaC8V58Luxc3-73-eHH_8Gzyuk_PcckCOZzWkItieyu7wxk4ernzXmtgAtI_JrcYNwHzEG0RdWK8yqoataVEe5KoCbAVf7TUqZWyZW60HdWvueg3FKhzWOVEA5U9UGJouKBzYRs2a08ZHGDDi2TpqOSuBKc_sBuF38QER7zx0J4R8KfUIYU_Rx5FHWmF2MXpSI1nHTQhE2vkNpuhN-rYZxtN4j6EVruQz07ZBdOYoLR57Kjdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948f9ff060.mp4?token=owVFg8KbWk7Kk8XK9GJbpAHDS1DzEbD0SO-JThTyzzCqq2RhdKscDN0c8RE3BudlnYxsqEoskzryJt16InmVjyT2FF1h3UYwWRLqgtaC8V58Luxc3-73-eHH_8Gzyuk_PcckCOZzWkItieyu7wxk4ernzXmtgAtI_JrcYNwHzEG0RdWK8yqoataVEe5KoCbAVf7TUqZWyZW60HdWvueg3FKhzWOVEA5U9UGJouKBzYRs2a08ZHGDDi2TpqOSuBKc_sBuF38QER7zx0J4R8KfUIYU_Rx5FHWmF2MXpSI1nHTQhE2vkNpuhN-rYZxtN4j6EVruQz07ZBdOYoLR57Kjdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشک ایرانی نسخۀ جدید درمان سرطان در جهان را نوشت
🔹
پروفسور محمد اسماعیل اکبری، سرطان شناس برجستۀ ایرانی: ما در سال ۲۰۲۴ میلادی، برای اولین‌بار در دنیا، یک روش جدید تشخیصی و درمانی برای سرطان‌های پیشرفته و متاستاتیک (جامد) معرفی کردیم که سابقه‌ای در جهان ندارد؛ یعنی اولین‌بار ایران یک تکنیک درمانی سرطان را مطرح کرده است.
🔹
ما پروتئینی به‌نام FAP را که توسط سلول‌های اطراف تومور ترشح می‌شد، هدف قرار دادیم. آنتی‌بادی مهارکننده‌ آن (FAPI) را ساختیم و با استفاده از یک رادیوایزوتوپ اختصاصی (روتیشیوم-۲۲۶۸) که توسط سازمان انرژی اتمی ساخته شد، دارویی تولید کردیم که دقیقاً به بافت اطراف تومور می‌رود و از درون، سلول‌های سرطانی را منهدم می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/457684" target="_blank">📅 09:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457683">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/457683" target="_blank">📅 09:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457682">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYsFbDUAuwI_Fs3zXY7rg_kpwU9lwdnJGTUnMLy8-4R0gG94PbLzgqQ73VRfXIJrBsLyXMHBG_vL1OhJGF30TUmHHT4gte8O-9Yi9SEU14OarDhoER63s29XlZq1HkqVpPq-SyDy3g3cC2Lzktpc4DXiw0boBIqnv7tes9Ia0RCNrawPFjr0ojU3nyGXnvDL_okZcEPsmaGP1xQE5PHBxr9ikftesuRmy78uwLKhvr2FI_O2tyc27ZrxTRCGn5lFM_Pvd-jjnhKqwkhUtvxo78w4iECtL0MVoEvJomMA39-AVe8LptD6qpcP1soIFS2_AUjZ-QBSmclzNyUd1_Iclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵ سلاح و ۹ کبک شکارشده در فارس
🔹
حفاظت محیط‌زیست سرچهان: ۲ سلاح غیرمجاز، ۳ سلاح مجاز و ۹ کبک وحشی شکارشده در جریان پایش شهرستان کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/457682" target="_blank">📅 09:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457681">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dff09b5188.mp4?token=VLMMWcoTMsEw0_rgkSk-1-5OPJ05oy9wK0HFw1AYm9GEHy6zeZ31JU69n02dFFQp5-m_vtqI8IM6ZveS7DC3KXPPcIJzJg43PnABN1vAS10fixRjbn8cIFt-mLx_8w-0oar1V8vk73Kz8sg_WP3OOI_K6Nh_6UZne85ChNQh0u5fu-zsu1e6T9YkpVc01HIddQ82jbx_YMALxHCg6AGS89GtW7D_FKiwXTY3A2NJW7s4hkm_s4-5HFnYoPHKL6k8dNqba5GJ0nq81BoweKCt59hFL6_GWAXngUK8_7NGvhDWtSTADm4-3cla4sBDUO2iMu0RMg7ox7OjtwpCbgHrfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dff09b5188.mp4?token=VLMMWcoTMsEw0_rgkSk-1-5OPJ05oy9wK0HFw1AYm9GEHy6zeZ31JU69n02dFFQp5-m_vtqI8IM6ZveS7DC3KXPPcIJzJg43PnABN1vAS10fixRjbn8cIFt-mLx_8w-0oar1V8vk73Kz8sg_WP3OOI_K6Nh_6UZne85ChNQh0u5fu-zsu1e6T9YkpVc01HIddQ82jbx_YMALxHCg6AGS89GtW7D_FKiwXTY3A2NJW7s4hkm_s4-5HFnYoPHKL6k8dNqba5GJ0nq81BoweKCt59hFL6_GWAXngUK8_7NGvhDWtSTADm4-3cla4sBDUO2iMu0RMg7ox7OjtwpCbgHrfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من می‌فهمم الان در جامعه مشکلات زیادی داریم
🔹
با تمام وجود به‌دنبال این هستیم که تورم، مسائل و مشکلات معیشت، شغل و آینده مردم را به‌سوی عزت و سربلندی ببریم.
🔹
من می‌فهمم اکنون در جامعه مشکلات زیادی داریم. ما تلاش می‌کنیم تا جایی که می‌توانیم از…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/457681" target="_blank">📅 08:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457680">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94f576d82.mp4?token=RMDX4p9akX4ARFV56IN1s0PRQail79y7UR9VBQWNbdgzcprHrjSyJRmXCCcakSNhdi3xregULS_xtIDa9izGF_7JhV7GOVvyTjkHoSI62hTf3bXEpRWqjl-4O041dgVzA8EnTU-jJins0F1yoBxT0NnjMz4xgJAtw6rfrMy806gH-8zSq0bVELeFQtdg_rJWicbdbMYZ0mMRtkkUZK4wrBYILT4peuV0H5J3m8YRGd_YaDtKpy2d6VrKd9LrfzWD98sWSJxeRGhgOshGufLJTNgaWoGNWm1mSfOIHAU96yQl-x_hX64CRIWITOF6V4gwAsyNc8UGP2MR0cpnnhpfVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94f576d82.mp4?token=RMDX4p9akX4ARFV56IN1s0PRQail79y7UR9VBQWNbdgzcprHrjSyJRmXCCcakSNhdi3xregULS_xtIDa9izGF_7JhV7GOVvyTjkHoSI62hTf3bXEpRWqjl-4O041dgVzA8EnTU-jJins0F1yoBxT0NnjMz4xgJAtw6rfrMy806gH-8zSq0bVELeFQtdg_rJWicbdbMYZ0mMRtkkUZK4wrBYILT4peuV0H5J3m8YRGd_YaDtKpy2d6VrKd9LrfzWD98sWSJxeRGhgOshGufLJTNgaWoGNWm1mSfOIHAU96yQl-x_hX64CRIWITOF6V4gwAsyNc8UGP2MR0cpnnhpfVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آنچه در روند تفاهم‌نامه به آن رسیدیم، بدون استثنا اجماع کارشناسی همۀ کسانی بود که دستی بر آتش داشتند
🔹
تکذیب می‌کنند چون بیان قضیه را نمی‌دانند و یا دستی بر آتش ندارند.  @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/457680" target="_blank">📅 08:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457679">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bcc0df7e.mp4?token=RiKUW0_JrziD5yk4U1RWHf1CNKAWCZD2TpEJBx54Z3MBWmICRwHlCskswxKNxHjCTsT-XOOVeuFZPYU-knV-FryCUHads0BqRCJUewA_LXyw38cNwkRf-ufNcCeUnogkhR-xnusmEUi8qvW14_hCYG53AdLyY38o43RamF_LHsnhsp4r7BrWzt3IK8AaVp0hnykCvcR_-OT5JkB9uib3iP9e5V_0_ag6oF90hA8GCOHKJ1kJyhEToAIDhA3oeKEJ9UVtfbk_g-BXrzDiVbrSyfnqzVkGmhKTyYNLzKA2UhvpCmTk0v1QCfvX9j6XWlP2bigqxKMsZzhPYgKwFpml4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bcc0df7e.mp4?token=RiKUW0_JrziD5yk4U1RWHf1CNKAWCZD2TpEJBx54Z3MBWmICRwHlCskswxKNxHjCTsT-XOOVeuFZPYU-knV-FryCUHads0BqRCJUewA_LXyw38cNwkRf-ufNcCeUnogkhR-xnusmEUi8qvW14_hCYG53AdLyY38o43RamF_LHsnhsp4r7BrWzt3IK8AaVp0hnykCvcR_-OT5JkB9uib3iP9e5V_0_ag6oF90hA8GCOHKJ1kJyhEToAIDhA3oeKEJ9UVtfbk_g-BXrzDiVbrSyfnqzVkGmhKTyYNLzKA2UhvpCmTk0v1QCfvX9j6XWlP2bigqxKMsZzhPYgKwFpml4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نه تنها ایران ونزوئلا نشد بلکه دنیا در برابر قدرت ایران حیرت کرد
🔹
شرمنده‌ایم که مشکلاتی وجود دارد. ما در جنگ تمام‌عیار اقتصادی، نظامی و امنیتی قرار گرفتیم.
🔹
ترامپ خیلی راحت می‌گوید ما کوبنده‌ترین و یا وحشتناک‌ترین تحریم را بر ایران اعمال می‌کنیم.…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/457679" target="_blank">📅 08:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457678">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef4cb6ed.mp4?token=qwvYOYXloGHNDn3nxf0sbHgu47YC3JgKCUPHBhjcamTEjsVbU_KFmcb0m360VeX_Y_EYC39wUHtb2AV2MUIv_zkQlkNdTjZXWJBLWotUSfeM9FSRA2d233cF-iS-8p1phFEmNmgFExeViQH2rMWXHasVGUa2UJrF_dvDH_B3uVWsKnojPa6b69ZfQPa89DPHGBNir8daJPs2Ej9sLpX_XKMnSdK04K_t8HtOnZTH7wJLo1paRNBnrwrJ6YYXr2jEJ4XuEUzvLDkoEsR0JEDRRxAejpAIX5d7_VrDrkZYbLbTcqc0NyIEN6hy-kNRhVvPEKp5acr5GS2Zt2uv0U_pXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef4cb6ed.mp4?token=qwvYOYXloGHNDn3nxf0sbHgu47YC3JgKCUPHBhjcamTEjsVbU_KFmcb0m360VeX_Y_EYC39wUHtb2AV2MUIv_zkQlkNdTjZXWJBLWotUSfeM9FSRA2d233cF-iS-8p1phFEmNmgFExeViQH2rMWXHasVGUa2UJrF_dvDH_B3uVWsKnojPa6b69ZfQPa89DPHGBNir8daJPs2Ej9sLpX_XKMnSdK04K_t8HtOnZTH7wJLo1paRNBnrwrJ6YYXr2jEJ4XuEUzvLDkoEsR0JEDRRxAejpAIX5d7_VrDrkZYbLbTcqc0NyIEN6hy-kNRhVvPEKp5acr5GS2Zt2uv0U_pXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید میثاق رئیس‌جمهور و اعضای دولت با آرمان‌های حضرت امام خمینی (ره)  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457678" target="_blank">📅 08:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457677">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f52dfed6.mp4?token=Eh0F_w0K8rXY5bNf_6SSMwu0qs6DHWU8MjYxspeTViJiDLsWEaozA8v6eX8oGZReAKaJ4TbMCON4WS1xp51xIP6KgbF6RYKE9_Ws-zvj8bUAchSsndQUdPr1_UJZHHV8I6lqz6UiqJHABHlDrW19CophbtOOzRbIyIaYGsrFI7ktZdCIHbiVDPcxsJlHxxL1kHZ4SXWXnXjGN4VVmH9yNg9piPaVmCYAH7qt40n5lM1_gs-ryyYlofOo2B2A3l4d4-EkE6Ho-OSFrnF5VeQODSivjzFSOnJBfXwrY2Xs_P4Ny3vtO19AzjqPF3hSPOYvTuY30ZFatMwpW544rS8U2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f52dfed6.mp4?token=Eh0F_w0K8rXY5bNf_6SSMwu0qs6DHWU8MjYxspeTViJiDLsWEaozA8v6eX8oGZReAKaJ4TbMCON4WS1xp51xIP6KgbF6RYKE9_Ws-zvj8bUAchSsndQUdPr1_UJZHHV8I6lqz6UiqJHABHlDrW19CophbtOOzRbIyIaYGsrFI7ktZdCIHbiVDPcxsJlHxxL1kHZ4SXWXnXjGN4VVmH9yNg9piPaVmCYAH7qt40n5lM1_gs-ryyYlofOo2B2A3l4d4-EkE6Ho-OSFrnF5VeQODSivjzFSOnJBfXwrY2Xs_P4Ny3vtO19AzjqPF3hSPOYvTuY30ZFatMwpW544rS8U2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید میثاق رئیس‌جمهور و اعضای دولت با آرمان‌های حضرت امام خمینی (ره)  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/457677" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457676">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diMdB0-7I-8_vwFUsAdesn6j6P4EfaCWumrspIFVILsFLxrC9laM9ExK4e6rtnXwSa57xilI2a1v5H3neTMbfVX0F3BaJtmEvlIIKa7YHXijXzyOL2no3-sJUgkPFcwUerhvJV2aJrI_B6d4hSrfl78SWNc4YL3e8FvPi1iDsUxZWRJIvC5XCQiFPhx_L6CuTwJYWMoIO2_sezeTXYRPAFXUwE8CPYn-oNnbZBgRxs4FCuaMNv5Y7duky2eASzHkNQ8t3CF1iCsJLVQ4sEYkeDOivTHIzw213r_g1n2ZPaMtih41cagvd22BzKlrlthfuRy836AlfS6mSsoTt-NljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام تروریستی که در کودتای دی با اره‌برقی آدم‌کشی می‌کرد
🔹
یکی از پرونده‌هایی که بلافاصله پس از کودتای آمریکایی صهیونیستی در دی سال گذشته در دادگستری استان البرز تشکیل شد، مربوط به شخصی به‌نام «مجید آدینه»، در محدودۀ محمدشهر کرج بود که نوزدهم دی با سلاح گرم…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457676" target="_blank">📅 08:02 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
