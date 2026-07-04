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
<img src="https://cdn4.telesco.pe/file/RL43ruEtqcGwsh9m3dN0nKxVwM1sKBucpSi8Q22f3XoVqENTABM93ujHpiFWU3Y6vr62Z81K1W7xbp4HFFsvbdtucW85XOSjCcKx4B6ujTd8EVszlg0Oub2ZuUVyUbnR-csxKH6izTDLeSkNLbUUca1YQo9kkwcJ-vfz2qqrQsNIgUybYkfxDiZ8ZPCp5kohv-C2Bs_QTFsst3LjjJRYKWy70GCjwaugATcb60toIV8SPHacc8K-9LoeTDWJ7P7xQT1XLPeRZ5_xHCKa3zwNpTGPdAa_yMxNGlIjxXKEQGTWXB3wm-TPhny6RFixkc6TpA22x9hFzIfo7UrfECH-pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 210K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W6fZjvEJcMp9D7TXH-tqS5phNCktm5a13S5gpF4f0i2gb9Hm6kd1SGeBU5zxHq5R5HVjK_n9Bp-H1KLmrN6hg5S1GmVDcSH48p-sZO38s0I64tzE7gvbhR321pR7_tYYWVj2m2IulNTJpxZAexVl-PpiMQwZh1KiPHVwhvozy57_Fc416SPstg9KCzecxh67TiVIHVcuhuTDCvev0Zb6r2xryYZCpXXudSiPmosXfT1hEderm8RsFCzcZlVxg4lrHSi2hfZ9KgNs4L0sTh3Ei9RDaN-AfQ3YZ3pUe5zwvC4aQSfuGT3XjcVUx5-yn85WdUidK8Mb6PpcseDtPydyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/koWgyGceZ52C6NM7MhhG5QXd1u1I0fORsv2ArZPGMpsU_uS_7mHDF_qmpG6G36NQ3N_E7wKAiPlExhIsbJL6W4NJXrOVCouy4PpuR0_4bgmFtGLIzMUMhFQQtqRtEcvU27Fzp9cbdZIAhqovJCg91XsRdTLhhTo88U_S9GtdtpneKwK7LK1ACxK8F9cIoFFU6FuKoqqZ2L2_4Ww3tlNffeotey4hIh43mZOFvS5eKXZmVtjI9X6x6yG7fkJOqsBiMvnwAyz0AD_NeUPW0CdV9dU6B1zVa2G4pA5DnYw98f6IM_XA9HBchH476u04WiM639W_7zL9nvdUW3StNufWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=XK5DaQ0aDwJIHO7WOy6ntksN-kSNknvXCD3Tzw1sYdStSFMsynaOx2o_xhUJGNt5Tu-Kf0p_eAmlTgVY2e3JquNvsfFzk3r_kgT5QJtLxKvnw4QLxrfmxnsef9aOzTyWU06V5L-mXdrqRg00R5v3C-9PmIYM8iiW4iLjfpJCZkmRju1SEYStBkf5GxSkPJciMzZjcC17t6eyLVK7GrUhFOQ_2HtFG4kwYtjBoqB2uy9dwuTRr-NJGTMtS4FxKpF4wnajC90iyXmcwHKl3iFtFSFO9CyHXDIF_SswdtOPpM4JwohoHVjWkTowfT1u1jTl1YAsqzlW4kSh312XHFIMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=XK5DaQ0aDwJIHO7WOy6ntksN-kSNknvXCD3Tzw1sYdStSFMsynaOx2o_xhUJGNt5Tu-Kf0p_eAmlTgVY2e3JquNvsfFzk3r_kgT5QJtLxKvnw4QLxrfmxnsef9aOzTyWU06V5L-mXdrqRg00R5v3C-9PmIYM8iiW4iLjfpJCZkmRju1SEYStBkf5GxSkPJciMzZjcC17t6eyLVK7GrUhFOQ_2HtFG4kwYtjBoqB2uy9dwuTRr-NJGTMtS4FxKpF4wnajC90iyXmcwHKl3iFtFSFO9CyHXDIF_SswdtOPpM4JwohoHVjWkTowfT1u1jTl1YAsqzlW4kSh312XHFIMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ENSkopgj3JXfFSeEOYbqo2eruKq5Edd6uXeXvu_pj1G3br8DcKRbTZ0tHhq0y0l0eW2H6P0LG3qUbxg99ag38C9Ksb7_MCB9om1jESbEyB_fTJNx28yKneO9ckwN5X3MV5T0ad5Jmc8QJqwRNSTC8ZK7X5B1bbx9MqESLbAkDISRA-7Tju_8v_nyQoQF5YVNViGsEKVj0joFJRSwfA_yJBsyGzKIFUSghqZPXSDAIAo7K--WXXVc9Cq2No9X0oySGYziZix4OU4T9Y8rIMdn6PBOIF0PSWxe5oFtEVs99hoKOtZHhSBpjCEm_6XPQ9xkilXiVmnvywHGzq2dmXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrM_b_XCOK2IvpO_UtxfdYuZzUjU1NJ_umw4cgwCNdN4dWfVU-0bjUSVNBw-e67Bp1p-tvcgPD2F9Sa03oobo-UQBRdl2shbP2YzvXVsVZjrxu2y8kL-sNiRD5V77BI5G20bhbjyY-ZoRT2ZgTGtFXJTVG-bHtZi-oe8SBUcl47LJOn4_ZWx_ns0MwF6LUraCLp2wwmNixH3TcEMcBiAOxLnadAuF_wki-7GEvc6qGOX3hryjnc5hyykwMM3nyWlvjO9SR8wsGEPvMUnRceOzwA3ZcuALb7kl_6PCb1glI-8s87VG4Q5pNrcu9OzktZ07SlLwJ1s33Ia1OkIm1y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhVfeSQS0-k8zhwufwtMKdG94WBlV8zZ8n5rCJqOpMvSWNItbr8NhQPrVGjXmOyzJ43wrOGztWkkHey02-u4Ozty4WoxkGiSuiVnVOvLl-SzZsK2sKL74_oG52gfx17PMiV_YY4M27pnLV-vO90iimkCu4Jh18J_Furfs7iMTHp7Cs3cWDyszi6y_s6mSLiegv-ehFjEBRDALCaT-xPKqWGD-X6INgc5Px4uPERfcrTfor5tZdZEUV-Dk83Lw4hUK1Iye9c2rBrrMxQm7EDzqnVO01qtyMKBcASw8amTgXWKem1uXFh2Bq3rYn4XgasIKWoq73nn85eKMcaFkQ99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfb7i3vKjbMXa19xtT2ohmM62JvwU5v_xC57UlCYTptHJgGVGcIECy1v55bNxPILnZWuLIyGwTuQt_TyjvH4e24PfmWeDgYka0uw3RsRg2xhIO0H1PMK6r4dSW10ZbVJsRslyQEqJ94S8BBl3UBnXgP15DOXAb8C-YnxvoxvmL21qNJheOqbq7XmcAm5vXOt0GuCRjw7RzjVHU6xbj6aLQcUWIbSRAZ3LsKK-4jsEnHRN0NtQpMOP-TWs7xO3SLdmiWtTDenYbYRXHJnJL3EU68sD32g6qLZROghnrCL1cX3KFt-mDYk06I1giUqGyXs3ewRKENxCyXHS4WisPtAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHJ72TPPAe7iW-fBNt1czBEUDqk7nH-AIBEPZtyRNh80PKTGV5QA611QNuBKqCMJ_vZmyrKbFm5gW5RwKdBOoUNBIjOqjizL23Fn0s8lR3-cVADN2M-tMLo-iummAMWOhqvd9DeCg-aoDtPKvAl2hEhbtjNhD6cGsAI5m17Ke5FmP_00xzBRULN45IebrOSPEg7n1P0MGkBXY_v0eM5vo8aRF6EbDT0SCnJVDSMXc03MFOKWYsN8nVI0FVLvtP0pYxhvULsYfCKj3TgjsOX_A8mrrZh8_GwerUOBVlicuVAb1DC4UGp7BjvPQ4-63kSMfRq-q6uxzYbX9ECkiYDM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YjzF9HVK8ZbOHP137q9dubClR7M3XkXPCkf4XJ0ZzzxNbxpFux-Y3e7ZATMpcQaePG8lHmUpjAMe65pVHtm8XBQNAIFJB8_x5y-HMEZgbLkttEgPBE41eFMdG_EDUn9fGPCbxknHVz2jHe7efHy0dj3opG4bOGLM4Mwm4K1z4POZXVJIWSPwjEcVa9fue-vAenptxDwmkFPGDah0e7CwKXoTvZOhExhkpGLhxPeqCdubwLM6RhGW6L2T4SgacHu7weZgk-rHgcrx_5555IgHf4t8gjirYF9MZWLtemLh4z6iBumB-LBh5UKMe032-MIDzAnN_MJY0TY_3icxzJqP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=n9W0VdK0aKH5tpBQoOod4vcXXTpAgbJ4VhFjDI4MaGipCSqoexQ5CgVemzXnZYPogOOV8jYF9xP7bAsOg3euAZ64IdXfZTXqm7a-MRBYeqTLjFHudXqn7jfbhOTDwwKhE7KsvLCHPHfiIXE9hbLIvZmMWfiSxOPCevhlUBL7GiJZlPtsMBHSUKAikgNwXh1bYpFW0KvohnvI3N1cH8aEYhFrrMAtJFa-kNYfTir5D13168A0oyTpdUv0mD8XAYTGlO2IZZQxZnfzycdLAtd0DBmt22uPwTzX1G7gbhGw_Zv-0cpR0LhA63CBYtmL6P68g2zVwD2iS37r5Gi5SuZe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=n9W0VdK0aKH5tpBQoOod4vcXXTpAgbJ4VhFjDI4MaGipCSqoexQ5CgVemzXnZYPogOOV8jYF9xP7bAsOg3euAZ64IdXfZTXqm7a-MRBYeqTLjFHudXqn7jfbhOTDwwKhE7KsvLCHPHfiIXE9hbLIvZmMWfiSxOPCevhlUBL7GiJZlPtsMBHSUKAikgNwXh1bYpFW0KvohnvI3N1cH8aEYhFrrMAtJFa-kNYfTir5D13168A0oyTpdUv0mD8XAYTGlO2IZZQxZnfzycdLAtd0DBmt22uPwTzX1G7gbhGw_Zv-0cpR0LhA63CBYtmL6P68g2zVwD2iS37r5Gi5SuZe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=APqrW6Wx3zZycKzhnKXacG5QeKwrsGLl1fuXp3JTlIkbfm3WnzgIU8AOsruId6qlzUGtbZaz4ZmHhRv96XB5AVJunBBrEfnjnhWRh7nej-JNbb3UQGE_nLjTHSkWBtXVsA3MBj1muH_3OP5so__k9vQ9NiUEvHm_sMB0guwtew7_RkdwrMtvASieOvMYJOQFzWYHEONanVfQGDnCOjdETQDg_2QpejEt3_ySibjC3-47_swuz5-WkdPXbtC43VObRiSlhVIBjMjqJlOE_09RRiqD646URwXNN0bzv9crghOmoA4XZxHhGwfl6ixBjWpoGK1JGpfs6RRaS7MfGMh4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=APqrW6Wx3zZycKzhnKXacG5QeKwrsGLl1fuXp3JTlIkbfm3WnzgIU8AOsruId6qlzUGtbZaz4ZmHhRv96XB5AVJunBBrEfnjnhWRh7nej-JNbb3UQGE_nLjTHSkWBtXVsA3MBj1muH_3OP5so__k9vQ9NiUEvHm_sMB0guwtew7_RkdwrMtvASieOvMYJOQFzWYHEONanVfQGDnCOjdETQDg_2QpejEt3_ySibjC3-47_swuz5-WkdPXbtC43VObRiSlhVIBjMjqJlOE_09RRiqD646URwXNN0bzv9crghOmoA4XZxHhGwfl6ixBjWpoGK1JGpfs6RRaS7MfGMh4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=BfKas9h1k5rBlL8aqQshXrUAtyhQuneypXeJr-qpIyE89kGWAEwDSVNPE28jIDwqMFENaIVCWAJbM7ln1fxcvn1-qd2ec1tSfLl8a4oXnYvGaR0-E04a3dv57lXvr7xT14h193-z9YPGUUy-39j8aNXr_Zjep8kHtZoIsQ9q6om7kXNQN5XbPKShQMTn_H-RHuWwqv4sWiGhu0zknTuftSo8DjcG223GPTZ5EFkR5MNAZzDmyq1eKz9uPFJ_pah5cppJbnoUL-0p-fvFP_YfLZ_ICzfYyY1PHEg3srIvtAWYNzyOAqT38WQtP_TabhXOqwh3e0u4kgXLKaLSW95loA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=BfKas9h1k5rBlL8aqQshXrUAtyhQuneypXeJr-qpIyE89kGWAEwDSVNPE28jIDwqMFENaIVCWAJbM7ln1fxcvn1-qd2ec1tSfLl8a4oXnYvGaR0-E04a3dv57lXvr7xT14h193-z9YPGUUy-39j8aNXr_Zjep8kHtZoIsQ9q6om7kXNQN5XbPKShQMTn_H-RHuWwqv4sWiGhu0zknTuftSo8DjcG223GPTZ5EFkR5MNAZzDmyq1eKz9uPFJ_pah5cppJbnoUL-0p-fvFP_YfLZ_ICzfYyY1PHEg3srIvtAWYNzyOAqT38WQtP_TabhXOqwh3e0u4kgXLKaLSW95loA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPgQyClc35lgT35oGQRkmHJhBlYHIV_7SnIbB8v-Rks3t60lIhfkBtydqBDFnsDEKzm-4T6DYzomnO3SBGQdED-hBZ06HGknKsey_eS7t9EbQ8_MlXUheKtQI1sgt-U8IsyRQjf2BoZ_-jO7ymmbBk_I586Torck3dkgd5aVX3Hff_ucn_uFgAHxMcqRTSqnUNCAUWR4YgbjA9CEcBFGKduU5y6pKAuXjvpbsqhJoo9IPJuYJmiK0UUQKMLE5d6aE91AUGEA6GxBnle0gacd3QL4cz_BQAcdXyFaUdcO36Ynzifajf3fLZ77FYKgrRiuKi5aPeXM-CgSVLI3lsKwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU2lpuVCCrIzvpBm-brJz6GsMpx68XSAn_9epqLdcDzVNffEMsY5nG4uhbHDKhLEgSz8IVyj_LtsO_ZxUnjx5E1tAebwhqrTxh_ZxowC2dzVgokt_vSLRWRmK_kV5-roF84LBCnTQ6lKuLZT5oFaZh8qyTu9hKErlx1v-pTA_1ws5hyVChot8C-0oE3vFCrmgWit0iExkv69Ts8s6dOlIevuGuIwaWTqdOmA-0BN0eLQJvOfKLa-d7h5Tx1DgbncPMNfyR0-5NcIbyv-nQdPH7ND50qofDBLh8RltuYa9Lcl-HR5Yqx83fO-pwhL4dUhCOglTMH4gZWvch8HggtR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=QL1F05kN5uS0EJvUQz_ncu4j2QbcrLoXw2QAnHq0qmTq7sbYlv49YJebDQjCnX_gleaXkAvdU6wAf0Ysm-m6y6IBJ5qBZD8JyZbsxHAlquNUSocQmcDByFgGQ6WHfj3wQoGdCQV-Edvf0ERcZzHDmWzRMh9foT-qO7LsXuAuwCR0q-uFLOEfgZPIElFnLcNCtOf5etjCYAyrq0traWZGqal_Fo3es8Nud4yAZ3uKU_Qefhk2r0Wtxd7xACi3y8bEfZtLtxUyZnW21fgQGeH-RkrGstrZyRJ-T4KTrzN2oAgxFGtguELEO743MkOWjGgv4mc7FOqt8-Fmkbxy6MqYyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=QL1F05kN5uS0EJvUQz_ncu4j2QbcrLoXw2QAnHq0qmTq7sbYlv49YJebDQjCnX_gleaXkAvdU6wAf0Ysm-m6y6IBJ5qBZD8JyZbsxHAlquNUSocQmcDByFgGQ6WHfj3wQoGdCQV-Edvf0ERcZzHDmWzRMh9foT-qO7LsXuAuwCR0q-uFLOEfgZPIElFnLcNCtOf5etjCYAyrq0traWZGqal_Fo3es8Nud4yAZ3uKU_Qefhk2r0Wtxd7xACi3y8bEfZtLtxUyZnW21fgQGeH-RkrGstrZyRJ-T4KTrzN2oAgxFGtguELEO743MkOWjGgv4mc7FOqt8-Fmkbxy6MqYyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQMR4Jibc9MyQ6jWmrbcm9AGfzNPXUGOaCyUKSAeoY6N88Be2LhjCitmsA_eF__wZYdwlQj2TdcQyswNp3qjgzbHdXwOoa1y0ZmGbFJdAEdbd1g7mH1WPb0FNVTUi-USc7E6JzV_pZCX25iLGf8qrDMOs-WV_TGSXzBspk-2EJwhO6xx4ylCNB5TekAONJifhJM_Mze1irwWFipDAK0srbhKTemBAlpoxHXHCeWKU6QfuZ84jyL_OoEOVzqoKqnHFco1MyEQCAU6hZpavFuHOWqHSN6d4wD_JrmOInaDlqDH1kGIHOIXyx5lCsRAFXZfIZnGr-1_hWaM7tX5MBWBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=PGQTLnf1Tcxg59Wbwf1XIamI6m0uKQCoUxQZcS-tNk6VDI-vNpXbLevK9OC3xprOh5Xofrgf7rEDA6wSdWiCBHrpYzluJPrAoTRBKVQAWKjL7rB7Q1lfB1fC_qtu2J8koXLnhxWkPWC0vijt9U36pDN63hIVa97AEaQsgelCZwUTWrXzuyNQDl0AEfodPVH_kHWa4F9OwSqkG81mu_Q5IKANzR5oJp0w7jRJYp4YtRVcAgtImW4D9s9nvIfN7jvaXa8RTOCvE6firnPCoO4cKnencjVquZ5D15sxhk4RuYpm-kGRLpNDJpTg165ZCtmQCbr5roIhWnlDPopavgZMPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=PGQTLnf1Tcxg59Wbwf1XIamI6m0uKQCoUxQZcS-tNk6VDI-vNpXbLevK9OC3xprOh5Xofrgf7rEDA6wSdWiCBHrpYzluJPrAoTRBKVQAWKjL7rB7Q1lfB1fC_qtu2J8koXLnhxWkPWC0vijt9U36pDN63hIVa97AEaQsgelCZwUTWrXzuyNQDl0AEfodPVH_kHWa4F9OwSqkG81mu_Q5IKANzR5oJp0w7jRJYp4YtRVcAgtImW4D9s9nvIfN7jvaXa8RTOCvE6firnPCoO4cKnencjVquZ5D15sxhk4RuYpm-kGRLpNDJpTg165ZCtmQCbr5roIhWnlDPopavgZMPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSUm-CIwVqRJ254vs2KSs-4_OOzRPP2w699jP2i5zVPDeBvsGnYZN6ujELPlDRpQHpFY3MNVirFJjFnmARVMqv_t3drV9eI9KodPIcJoU7r2UFS-su9jIgwXkRSvKl7-fY0UkVdV6O0-4tIwq4IwrmcdxzX0Khnpe0pBKUq5GN_eX_IdoBtTsYUZFIP6xGNhN3ydbjp_6YpsnRtmlxIPwQTqDUCGHUd8r10sEvzn88C2IkUZCXHn777gXVkxyg2rZYj_QgcylLaHxFkOfIgqM8ca3CNU8pNdkLapqJ2VRCBBRAqCyJVeh67r6TjAGMRtCWR3BDWFqKtXQjO09d2m-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=bQ4lIJarIYRpbnnCkPiRElpRn0A81UKmn5PqYp3MZhMkDwp0OCps_9aJTGAM5P_QnvwIYMqdPPcR8SqU4FPkFMUUFG28sLiXGtYP8H0bVaJQ-g0R0aFW9yJXkD_gJnTQo7OCgvOqPPnC8tldlrLp7_y0upFVZK94l0Hcny-3TG_88aNgV-8ogdYJ6I-Zzu3ZAWrdT2Wi4VQBr0Aq68Libcao6_U-Hf9mahCF12szx_43OXy2Dxcw0oqf4jGgnwc62AEyXe-_zCqqDLQzQ3o826sbZ76Ewlo6ZRtUQchLDltiLEQRfb7CTll8bVGRfNIyvSHyrd8QjHRrTs5XIMNGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=bQ4lIJarIYRpbnnCkPiRElpRn0A81UKmn5PqYp3MZhMkDwp0OCps_9aJTGAM5P_QnvwIYMqdPPcR8SqU4FPkFMUUFG28sLiXGtYP8H0bVaJQ-g0R0aFW9yJXkD_gJnTQo7OCgvOqPPnC8tldlrLp7_y0upFVZK94l0Hcny-3TG_88aNgV-8ogdYJ6I-Zzu3ZAWrdT2Wi4VQBr0Aq68Libcao6_U-Hf9mahCF12szx_43OXy2Dxcw0oqf4jGgnwc62AEyXe-_zCqqDLQzQ3o826sbZ76Ewlo6ZRtUQchLDltiLEQRfb7CTll8bVGRfNIyvSHyrd8QjHRrTs5XIMNGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTggOMdbcegObxcSBz8oVgWm5yVqm_x2BOOKVqTeT2dZU1BDmxHeYWmXA_kvJHlEL-WjZdVQJmBVL3tXPUaVgT4PlVGpI9hMJPH_2c-V3Yxjs6XafDI1o4VSzX6m1tpKvPT1bZ5gk4yLZays-A98fW-91x22aiCbeO-8-jIZo-7T1NZ5yhwlsLN1eoSiKTq5dzu40C2fuSoK7bYgXd4IIgWuPu4MQla97CToST5DIDNchMEtMJ7e35au5nLrH4_N0Bcn7sh_58aE8O0LvnyLSKqqVZCAMdnnvc_54KMKgr0oTOBfPSmI1DDZ17nHWW7w9yuXmEg7ou62JgqsIfNqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWiG4pH8wLbnyyDtVzdxXecyjNkLrwNOnnNUVAyZwmXfCjk1jOvlwZwvIKJ3455WseN5g_VUIAEKfzBCJbjbTWUKR0MhtPqRCuKZNOdk3X9YUAo4wULA2LJhpw4L_5UD8aKs-OybMXvd6NNlz5DLPb9CUcKX6KBBNyNRQZ5mLDWteSPrAtnMwoy8K-OyFoIkKXYyynJUlHP4xJlt0DBYKzaxJflsOlY4j10Ya4VnnOySPAKbK38yNZK-QCbMF4ox97lbj2R061NJCOLVqmmLksedUcOqrnss-SplQ_D-oRCswuWjlNT-Z1VyYQP_F7A-1CXy71c0Qj4HUllSyFFkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUmsZgiDUhfV-Rl3HNfgexOYYBkerZIO-Mk5cOcA8EgUSxJpieUEqpwViDjl2P7O7pjXXpNJ_qtvrwk7r2mGvtu_lwDtJ01sTaFn-xRLZA8gfEIceiV5Hdpd3brf8r9UpLL4fsaPQJr0iOFLy7nzBEWOHdoHSyTicNlmdE6vdbrJxAR7Lcsv0XqZtzRvM-z5KoNZqL7k68NhFdNno97MNoZ26LJ96dWx43BflcBU8kSv2B64hDP9pafgywZTHvdOBzPr7fJ-ipNiPiFocEHPmgxZ45u-V621VuR8ZmdfLxTpElwyk6m2MFmFkPX4afHhFpvdoADsmUl0BulMao-7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=o8dAp1Ff2-pvG6hnz8tOr-XjT2RyVlrJn5p3snVx7ounh03jw4TLRwsnNJE8s-FLbJnZmZjZWpqHPyDfM2AZcUV_fjsikntcTT3MT6K_Kwj2nzL6t43kd02SVFNYCv5uLj2rVIMZnYrSpLwJ6lry9sG1poIOKe4iNU9eWx12eUlGMu4U0Fp4W7ly4HZDzeQZWEBbR4ytlQugEHD51i3c6FE9hZNHc774WkseTc7oQsFhiC032s7mg07Z9op3rOiixCDIbBQTSIV6riI-2hcR1owb0S9ugbKLzUQys03R_aLsBchj3DBV0-ZWV3oShG9pwtjyqdre3pWrAWABbVh5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=o8dAp1Ff2-pvG6hnz8tOr-XjT2RyVlrJn5p3snVx7ounh03jw4TLRwsnNJE8s-FLbJnZmZjZWpqHPyDfM2AZcUV_fjsikntcTT3MT6K_Kwj2nzL6t43kd02SVFNYCv5uLj2rVIMZnYrSpLwJ6lry9sG1poIOKe4iNU9eWx12eUlGMu4U0Fp4W7ly4HZDzeQZWEBbR4ytlQugEHD51i3c6FE9hZNHc774WkseTc7oQsFhiC032s7mg07Z9op3rOiixCDIbBQTSIV6riI-2hcR1owb0S9ugbKLzUQys03R_aLsBchj3DBV0-ZWV3oShG9pwtjyqdre3pWrAWABbVh5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=iPda86WH-qn9MUgPkkUtIZZCn-xZbFl4S3WVjEvSO1a8ak59gH0RN4uVfPY4ioqEaxioRP2cR3kZJpwFdfJ5h4iB5ZT5tJ-FWa8sFWs7Hd3-ARQ576X5MAnE0-jdCto8tqX0dtftxOWb4qmPQ_zrGw97JTQ05HxZtiO5phJgIktRCkyJBplQBO8zJbN3mWog4Axiv1HHkzlFKHOxXKCTYML8Wxp7gOmbnytrnXTTYwhCx0L2-QdEvjab86KHWWchdMi97z0SFAGm4T8qqEp8OPn87mexSJM69ud8qjJ1-c5FKrn2PzcEwx8u_nAeDNPFQ7tvvXoKx3in7Ardd7RZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=iPda86WH-qn9MUgPkkUtIZZCn-xZbFl4S3WVjEvSO1a8ak59gH0RN4uVfPY4ioqEaxioRP2cR3kZJpwFdfJ5h4iB5ZT5tJ-FWa8sFWs7Hd3-ARQ576X5MAnE0-jdCto8tqX0dtftxOWb4qmPQ_zrGw97JTQ05HxZtiO5phJgIktRCkyJBplQBO8zJbN3mWog4Axiv1HHkzlFKHOxXKCTYML8Wxp7gOmbnytrnXTTYwhCx0L2-QdEvjab86KHWWchdMi97z0SFAGm4T8qqEp8OPn87mexSJM69ud8qjJ1-c5FKrn2PzcEwx8u_nAeDNPFQ7tvvXoKx3in7Ardd7RZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNB6i9HKg2mEC2hmb4pX9XomahHMFXNpkPMR34H9KCLSERiaiIioe1xTBnpPjSXDGb_UINhA6xqCR4spUUX3AbK9Sun2V_tx0yiuTTbrXalVisxbcWCCHzQ5PY0Q4uuniHpDvm5NejSvGJU1PKmlYA-eb06GalUnFkjwr12jkkEzFzrQCy9yBZFTkeFgLcWs3EY4bwEzaXFGwmkPj_mn2uToivmJQGSAUPGfMYP0eZyEPywEc1e04RaKl_w5D4JR9Cj4mIqkCbgTMlEImdn7I3pUAJ4S-PYK9b6o6ISEtKxfQgdaqrn-kR0KM9sJlhuhucmwlxrzzsnGzgNO5eK32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=hIR75M6tDf_ZmuiYlQjVQdG_EFCS2I--5DOdvuupK3MLUDbSmtanAjIi-AoHPDXoXlK_WPpBFrDI1yk46b-xkEVrDMxR5dYO6NJO498rINWeLnFs28cGhRH2yD4BK0_7yqvhJbXyDRUOLR5uoy6sxt0NU9ZN_9x5ySva7Tocndl7lfByrZ-uuIhV1mqgAungHXrvEhGYM2EM8XhgFHkYUu6Lh57lXraaJiJfykesspV13qBmgMOLTiV5WDTdn-szGtdeFhxqt67hU3eA7uPOlA4UY2NeyD5hvi3F3jpLbBqPOZMHm6znj380iRBSdSGVQZdKCmCGxaXTKbuOgNFmRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=hIR75M6tDf_ZmuiYlQjVQdG_EFCS2I--5DOdvuupK3MLUDbSmtanAjIi-AoHPDXoXlK_WPpBFrDI1yk46b-xkEVrDMxR5dYO6NJO498rINWeLnFs28cGhRH2yD4BK0_7yqvhJbXyDRUOLR5uoy6sxt0NU9ZN_9x5ySva7Tocndl7lfByrZ-uuIhV1mqgAungHXrvEhGYM2EM8XhgFHkYUu6Lh57lXraaJiJfykesspV13qBmgMOLTiV5WDTdn-szGtdeFhxqt67hU3eA7uPOlA4UY2NeyD5hvi3F3jpLbBqPOZMHm6znj380iRBSdSGVQZdKCmCGxaXTKbuOgNFmRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rtv9368jl5e6mj-9o9Hu0f1FMeHLIony-A9AaCd-oqb1kGfN5gekgQklNliR1aXPMnqlrOdokUR5XIG6mgjs7yjEbwAVW4G3YHnac6BmEQPnku6RE4y91IJuBQjDabrLegafH5ZjBeuBRWYcI_fNC1xSW4x62ZdfVMHX4NRvArPOA8MODkmRVdmQt8QuqUzVzj2btmV8kE8aJNx-lp20b07xfh1d8BjYHoO_Z99_xrBo8b8oi47s_rEIFskLTGxXygoa_IsZucm6nwszcBpK64h-BScBKuQIxAhSJTO9474wkYwR9TEPULHX3kRg2H5IXImdZIjMkegABW2LUxbwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=H4C89VZuWuesJ9KdccXADWp17g6hsIlmAAh7wMs-Q5p43cnTFfGBWq6R6NxpSii29UyuaAUjSBgvAbgucFdz6YPzPdtQCCWhg8Fk4rWjkWfZAkGP2a0VDSgatwTbHXvvTSDZf33tmy0ME-nClm81lLw-ewd-8esEBYBm06Lco46cI6G0PF7IFrwR8SU-e8GL_MSv7JczBOudDa6veCRWSjfoX1RXb9D17mBIAny15uRUaw2wLsTOhBwWvYrVSDONPwIsK93sM9HN0F_TLvXH5kwmV0d9HRg189h645o68OIbLaE5ivHv9QCW6d8P4pJalQiKsXHWGtSVSUNM4YLWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=H4C89VZuWuesJ9KdccXADWp17g6hsIlmAAh7wMs-Q5p43cnTFfGBWq6R6NxpSii29UyuaAUjSBgvAbgucFdz6YPzPdtQCCWhg8Fk4rWjkWfZAkGP2a0VDSgatwTbHXvvTSDZf33tmy0ME-nClm81lLw-ewd-8esEBYBm06Lco46cI6G0PF7IFrwR8SU-e8GL_MSv7JczBOudDa6veCRWSjfoX1RXb9D17mBIAny15uRUaw2wLsTOhBwWvYrVSDONPwIsK93sM9HN0F_TLvXH5kwmV0d9HRg189h645o68OIbLaE5ivHv9QCW6d8P4pJalQiKsXHWGtSVSUNM4YLWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=s_pFoLzoQcK69vZ6YFg7_i3yq5Jfve4RVOMJp4G61kmtXMoYOIHqYSVZORtWwQkDUiV_6iDGXTVhmB52nB1a2xIWe-BxSa4wET4vay8w0lgOGB9KaFRRQ6IN3_V1ZRCSQQO48sZtkI4sJSO6flgwrj-mDDukATuHJhrUUGxUI0MoTNo5ZXdFpmr8uagONFf1CXzAGRL-fuzCoK23PoNAobo0TFiuKyqsO6SxmfObl0t3B1kwl-4MDCkXkV4QjcdOAlLb0owsOFKwLQwqEnPePfiJ8kmRdf7bgJeaeQvJqwF6fCXJtJ2h37F3sg_CkB_aqrAfSgXxgmN4q0KmbNs_aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=s_pFoLzoQcK69vZ6YFg7_i3yq5Jfve4RVOMJp4G61kmtXMoYOIHqYSVZORtWwQkDUiV_6iDGXTVhmB52nB1a2xIWe-BxSa4wET4vay8w0lgOGB9KaFRRQ6IN3_V1ZRCSQQO48sZtkI4sJSO6flgwrj-mDDukATuHJhrUUGxUI0MoTNo5ZXdFpmr8uagONFf1CXzAGRL-fuzCoK23PoNAobo0TFiuKyqsO6SxmfObl0t3B1kwl-4MDCkXkV4QjcdOAlLb0owsOFKwLQwqEnPePfiJ8kmRdf7bgJeaeQvJqwF6fCXJtJ2h37F3sg_CkB_aqrAfSgXxgmN4q0KmbNs_aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=rOAL7tS_yqA9TVkw-MTgdGXoPjtGYOWN3O6mDTWhNYEMlet7hQno0bigve38rV6REgY1boxZO5LM2rCyQ_af2DIZUaNM1cP-Yzqa9HjYSP17mklltgfs1DysPOIkGfJWbgVEnrsND4H-Ikqxl1Cdq9ItPa25n-G9Q-NqAbwskV3CbKIRx7BzRqdRfvPmQ4f6lhtYve2a6xfFYZOaYvMOjYYMAOegQjkxtpTElu57b_9q1v5c8gpw2APApUBI8VpZgftCIUd1Dvo__nHkkVa4aXuNrytIFVR6MyZiqHpzncBsoqzqCBxnYfG0q5J_ezfLvsL_4W5O9gmEuwXIvRCC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=rOAL7tS_yqA9TVkw-MTgdGXoPjtGYOWN3O6mDTWhNYEMlet7hQno0bigve38rV6REgY1boxZO5LM2rCyQ_af2DIZUaNM1cP-Yzqa9HjYSP17mklltgfs1DysPOIkGfJWbgVEnrsND4H-Ikqxl1Cdq9ItPa25n-G9Q-NqAbwskV3CbKIRx7BzRqdRfvPmQ4f6lhtYve2a6xfFYZOaYvMOjYYMAOegQjkxtpTElu57b_9q1v5c8gpw2APApUBI8VpZgftCIUd1Dvo__nHkkVa4aXuNrytIFVR6MyZiqHpzncBsoqzqCBxnYfG0q5J_ezfLvsL_4W5O9gmEuwXIvRCC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnwMvsq1uFdk58fSWhRifEfRMl_RwnEfo9vc9TkHwZLcbB3Wod6v6Ge8DojZJsYTL_pkNzCl5jU6M4ivr8aGgjxzqkNRDGE41aeyv8NNIsIqHw7sokIzWeKkWrUcueM1tnWwvPDpWjinQhNHvrVgrvQTXEX5rNUJ4FU_ZrHKBCowegBemVXwl6ZzyoHZcQnaoBvj6QbXSIXHfjX2nFQpAn6gzwJOoLBTHpfqDbSHvg-ZMeQOCfaRNOQZW1h6gXaj-M6Y47TJSsbJLOl3TUhv-IfkobXFPunettrbj0vL87Fzimto2ALTjDv6PZGRjZktt9mM3cppLVePGKXKUgAMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3t6wO_yV202IxaS8wYoc8qfEjNs49m8dwDQAVFWXj6fDx39dv53KnUCg7zR3DhIIre1AnpXiWdFBra0fGl0ORc-TldVLqZPEiWTT06g7pbHpGU-t3WJajjqaOD73BRJuG651dk3gmqLoz--9Hth8u2vx9nTFtNcinRk4zYGlouVXoNR_EHzkpAfh9XZ4j9P5Hx7DwJYtEvpsOwx3MUy6X87BNwhlLHJc8lkXAHmp-Ts1ZMF0NWRaM4rP-uksZl5--g1G4pSwBIEyMCrGrcz5v9Yym_a-aHN-wmb9xXvrz7wHKE-FZVaTvwW1DnlF4Q3z6AA6JnfrT364PB23vEkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA-abM1vqjTKJH0Atudn7o6dUW10EWDhoh81-BlruKBAsQawOdJIeFeJ6NHyJJrl08eYZb2XsE0SOiaxa5X2HVrUbbWA5qkCnazif_kuTIO0xA5H2P81zeKHYfvl0JNy59yzB7H7uw_3o_SXr-nwYF-q9tj7k6Nzyd_7gtHiUJ_fCMIcix4nDc1CrlMmRtRZ3ZhaXRr32wweby4JTEhw1-DnUqkwBThjB-M1RDL7jppf9BLn7TgAQHOe26DqlZ_BJxPfgD0dW7GO-itBDDuBDJjT-iVhlNi2nX5TUHN7BLOTUnKmHTyPt7x2n8bjaKekyptN2aCtI7Bc3B8iVKiYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=F1UAKDID8cJ6emLj_7GxMQeN_MfR-EI1j6hEpj324E5oz7GnnS_KtvAiax5QOCSvpOfnszrS_p2wUwlVoyOBswn0kRwp9hkoGXbyLTgekRkvWN63gyoKJFye761qu3PKOlKW14ryJEKMGOlDwXc6FAHoE3G55lMGnnLb9VL8O1SKuKyqWsP_nU2QFpaY5nfA06lL11wXXSlVe4nITbwkkBIUGbmn4sNRqGLLVOrnDzKLottekjI5YVVeGNNCilnHypef9idrDZi3seOnLkt2uTt80zLZmqAu2nwKAcUefGB3hvdUC6vuKSYCEGwxAW3gIQRCcV7ybgeNufveZcUNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=F1UAKDID8cJ6emLj_7GxMQeN_MfR-EI1j6hEpj324E5oz7GnnS_KtvAiax5QOCSvpOfnszrS_p2wUwlVoyOBswn0kRwp9hkoGXbyLTgekRkvWN63gyoKJFye761qu3PKOlKW14ryJEKMGOlDwXc6FAHoE3G55lMGnnLb9VL8O1SKuKyqWsP_nU2QFpaY5nfA06lL11wXXSlVe4nITbwkkBIUGbmn4sNRqGLLVOrnDzKLottekjI5YVVeGNNCilnHypef9idrDZi3seOnLkt2uTt80zLZmqAu2nwKAcUefGB3hvdUC6vuKSYCEGwxAW3gIQRCcV7ybgeNufveZcUNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpC8cdy7KYonzg2_GGqrgQCpOE4vxufYW3T4L_VGopYcvZrLWOTFm2Cq5UMXqEQjyzZgwNO3EvBbPxItOp7tXxI_xQRreOqwWSuEZPZrkmMpyQotv3qFEH7IhVHjVHANsXMyeRBbFrgPXwSFNQzDOqKjk4fExNQF81e3K9ALfBsjMmjVCT_ThpbpsT9LgaqVV0-hoqT-mhDhAiVr6MJ7xoLKk6o7mrjpkFOpxj8sI8XkdFXVh1ON9M5CsqG_g2U5ixKTrpPdoc8MoQoJbNYyLQo0Xn1-k-0v5IUk4Z8MooUqtXBNNc35vPS13Szz3NPndnv4etWCiCJO-Smha76QCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=ZQ-LXuFyvh_ORjkHm5vawQ345EBThgl1b1CktOWcGX_mqmpJFTDxK_AY-4mu_E47ptUHAbpZ82KrPe2yL5Y9gYqE22zJW8qwmDCu9XUzMFB9HcfijtaFW-wba5_IZ3Fdctht6Bv14GRZfptbSt9xvaWkl_EV18kl9DTvh0KtLa2cofkvo2MKXknxi5SHGZUrlpHLl3sfnP1lvYme2Re5nxA2X6G4sxfSnlCGWMswcJbtzrsQOwCbg8vJFS-gLcD1NP_CryZGU_z1evcY2O1rNlNWqCgRsqt-uTevo2ST53B8KHZESlPYOf-4WgKOwKH7YaLsTdi99cDPYyMB7H0LYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=ZQ-LXuFyvh_ORjkHm5vawQ345EBThgl1b1CktOWcGX_mqmpJFTDxK_AY-4mu_E47ptUHAbpZ82KrPe2yL5Y9gYqE22zJW8qwmDCu9XUzMFB9HcfijtaFW-wba5_IZ3Fdctht6Bv14GRZfptbSt9xvaWkl_EV18kl9DTvh0KtLa2cofkvo2MKXknxi5SHGZUrlpHLl3sfnP1lvYme2Re5nxA2X6G4sxfSnlCGWMswcJbtzrsQOwCbg8vJFS-gLcD1NP_CryZGU_z1evcY2O1rNlNWqCgRsqt-uTevo2ST53B8KHZESlPYOf-4WgKOwKH7YaLsTdi99cDPYyMB7H0LYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY_tEKlsh7usicgqSzaX8eOzleH_SrCwmbIxuSAODQZsgTyKkMO5JfOCSUj_wV_MD90Yd8ZkVcoRAolNYM2NipQo0Gr_jao1IGnz_uOGxlIncw59jipX4SSEfiVxvJllhYsqHv5JCLeiuknlSJmSSSJKh-VNJp9uxRjKOW2cgk0jflgD_ZKN_NQrApqg6ZP5lpNXunqsacpreMsw6lkH8LtSkB_Ed8I8imQV3Sr_dTi0f1ORuTl6wZrJsKRUbaAr6qyi2ClitrWYM676vGd1wS_g_JA2Mv6WbFAY0zCGazPYDOGzFq38XnAwRah7cxSD9KiMF3Zg73P2I7oS4ZJVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=b8JSVvJneBDNaMV0xVQ8tgJLf91FTXSS674xoX_dDWMmtcpOC_w0iqHawH7YeJNXPD1rNd3X42VpmnUlULqgcSO3RZrVT7EIF4WkZNhPudOkpkKNYz47KFISo_bGxzfeyFKzoLvgZYto5wz6CHoOwVOUAc_2pOKNc1WNxaDNGaqxZ9SEvCi3I8lH3YILZnZUUy1mDciyBjzRjPU0d_wYxc-8FSz9H0byLJtBZUrL-c5Gpr98HRXrBo1CkAMuyAU7ngi-Q0n0kyRzRatz2Es7cUkUz2M4Ejd1KGM9Bg_5_f5qgCcfPdkrhOci2WJeGHH4L4Y0BM8sbR0JBc3_5S5KeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=b8JSVvJneBDNaMV0xVQ8tgJLf91FTXSS674xoX_dDWMmtcpOC_w0iqHawH7YeJNXPD1rNd3X42VpmnUlULqgcSO3RZrVT7EIF4WkZNhPudOkpkKNYz47KFISo_bGxzfeyFKzoLvgZYto5wz6CHoOwVOUAc_2pOKNc1WNxaDNGaqxZ9SEvCi3I8lH3YILZnZUUy1mDciyBjzRjPU0d_wYxc-8FSz9H0byLJtBZUrL-c5Gpr98HRXrBo1CkAMuyAU7ngi-Q0n0kyRzRatz2Es7cUkUz2M4Ejd1KGM9Bg_5_f5qgCcfPdkrhOci2WJeGHH4L4Y0BM8sbR0JBc3_5S5KeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-cUdg0VK6N-RT5ycQFCD6a9K-3SrnhfiDbnhACt3V1h_TS0g1a4Q0RCcZz2m_VqzutToSqn8UGMC6dejDFN4lyiuhfNOzGUvl0DTWmL5J_Fuslg96WOmF_IoqjkZyY6JapaPWHISWZUotVNiubZa2TRjtRaTk7FMALqVXdMpoSnJh7aFhpyQoEaogcy17qHSZpMzSsmD21lW3iYpuNy7EE3hHabmHsry9a-tp7pNtXZcTqNqklzXyBpbEXbbiq8rgl6e9GGdStw4A_11MOwUKMkaYCKBKQBza8tnA21OZGWBCPc1Eb7nTVyW0hhV34C0yt8JjHkVn5bHDjMf_wVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0pWI7-87mrr96lQrZOlBQDsOBHeXdvRgbCeA8wf1lMOo8xG77-gHJswW6f8ub2cTFEXpRmRUvDwpGWhDczK5ooZ01uN4_XvXjBfzUcmedjm964ghJd1RSeep4KaKddYeBit485FMnjHbyBxwOU_lTJmCpz7Qh5lz0px-KRC4cQmyye4lIN0sGemz58qPcklM0ViN-shjcfjfEIyZzWPYZJfbdx32Jez86ey3m83ASeWwLRIz3_ygwAw_prFa5qEeWeFlFdjcDRSR7UoohR0LAUri9MVCXXrbNP0DlhcoqvilNWkI7WsNBBQkAkaPBvMy0jZVQFQKPZe6LljPwMnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJtfb3oOlkDi_eu8PgXTnQk9Jm7VQtdglSaSGmzUjkjFyM-St9Et7w-kDEmfkGqPZY4WkH-Mg8WUEjyyfzOLzPmE4me52WLsGt3J1sHkgWE3qOQIxWV30qDNSiPr0U8gdyupMSbc8DIoh2-YmnqgaIrXtFxsf-hOF44oVSoTTiAjFT9aMXPLVYGL9L95vpCMVjkB2CHy1upkWUFG4x81-Bbu4LYmOhwBEP_CcEFuKKSa_yrWEgZP4RsF_jeAipWb2_t4BRLmPRzKg4AVm5eJHTnhh196z9eGMvIeGp-bUJv2yS0FRvXO3LP8viKFK0eFLAZhf39mK4BHM3creaqdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRxCsnFTJR_vQxLpL1ttzz6AU2WFTofnoYpuxo1UmvWvfX47b_RwAodOeu3V0QHZfKzgdvNghlBjKM9JJzGdjG3NC6EUWjp0-7EvBh60YRPNGRhQ_f6BKpdMiv-AZdPIY2OudFA951lhuvNi3wtU46MsUsMq6ND9qKJMVEud04178K-tJWQjnmwfveoiS99ieVJ9GPaCZ2xEbuLwi1iWVYXJZ9clOULqUcvP6qAOOtKwX3KVA2O6WQsMLMhPx3EKkMO5WzuU-JBkBT72QzuEmKJxgC0YBTxgpnfYLbvR9hvwFbsMtGZZ-t4EGML0M_Lo39z3rqi9297Qs8DEGp4bUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=aHh-t2E51xsTO0kqao4og70jomxvivLJFTNn3fg4p8N5UvXJQQQQFFLeswapK9i5rUQkLg5p9P2bDYvyCPX5VrfA6aS09z5vyKMUowKjUaSfXT7K9jAwNdD6bIBCHiQxC52m0WTzX8c4jWGDKxAVqIfyqXnJtHcoYuaJaV6xI1_wc9znAV15PVyA-8naqBijOE_8u-3Oqke-GU18ZxOttpybhWEyV4KRC00m6GEfcLm0pVGCmakB-b3FaYwJM9IGeotfr9p_8nYj5Uk41CH2AEXUAlMNpdZO5LOtPw_rASj26zxWaXmGiN8UXiP4TMPHvYrU_tvM-ob8DFhyAMhlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=aHh-t2E51xsTO0kqao4og70jomxvivLJFTNn3fg4p8N5UvXJQQQQFFLeswapK9i5rUQkLg5p9P2bDYvyCPX5VrfA6aS09z5vyKMUowKjUaSfXT7K9jAwNdD6bIBCHiQxC52m0WTzX8c4jWGDKxAVqIfyqXnJtHcoYuaJaV6xI1_wc9znAV15PVyA-8naqBijOE_8u-3Oqke-GU18ZxOttpybhWEyV4KRC00m6GEfcLm0pVGCmakB-b3FaYwJM9IGeotfr9p_8nYj5Uk41CH2AEXUAlMNpdZO5LOtPw_rASj26zxWaXmGiN8UXiP4TMPHvYrU_tvM-ob8DFhyAMhlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=USGkO1mnE5sRFHFcaaUFQBkhDXRDc6inQxKiOon8-XptQOH9rHLDtRAdtsaW9WPHtMaAfcgA5ShheURRPX8WfisupDGuqIzDTkrZW3Fi2XQvVZlQn30Xwi8AClNnP5JlGeyS2T3PWzusvTzhtuWnrUbIMR7JCDl4PSTCKDwh9tMPK_MzK9A6LL1N4_3BWytuO4rgAVELtdOO1my5E40EEOudC0cGzx5x4XMCn8mAR4pBLQFD2jWWYT6fmXZpz_JSX3FymFL-53Wg5jkKPpBvWx2towcDPkfV6KYYMHfBVKFXqaBvQVNqVrjApRmY6Pzxm6xmrS3-p6Dnnk340ES_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=USGkO1mnE5sRFHFcaaUFQBkhDXRDc6inQxKiOon8-XptQOH9rHLDtRAdtsaW9WPHtMaAfcgA5ShheURRPX8WfisupDGuqIzDTkrZW3Fi2XQvVZlQn30Xwi8AClNnP5JlGeyS2T3PWzusvTzhtuWnrUbIMR7JCDl4PSTCKDwh9tMPK_MzK9A6LL1N4_3BWytuO4rgAVELtdOO1my5E40EEOudC0cGzx5x4XMCn8mAR4pBLQFD2jWWYT6fmXZpz_JSX3FymFL-53Wg5jkKPpBvWx2towcDPkfV6KYYMHfBVKFXqaBvQVNqVrjApRmY6Pzxm6xmrS3-p6Dnnk340ES_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=dNZOnrG3HpWEzMH-JxLArSssUviwOkNRo9h7y6AGmc1rhpy4tlV5FQ7Yig8Qxii4jMjkiza-qA6EcVCcW3OPSmArR9z1RzIpsClTqHnM1lxn1QD4Xski4RyEJQoY8Q1UumWcoWP-7xS-bPNfLJFRRrgVbProJfWbplpV8olxXHX5JZjgeZbgY_sWhz8xkaFZ9dp0sPDKN087l_mPXrwqoIDQIDQIdmwgr2osgB2qr5yyU89pR5C_3U0F5vKPtTkQGIiOMBDr26V8XnxMAINsgFLeWUYK2vJmQcnjYy8S1THa6Mtyk2ywzpbWdDArMRZH_ybEYpK_Jy1hXkm9cGcEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=dNZOnrG3HpWEzMH-JxLArSssUviwOkNRo9h7y6AGmc1rhpy4tlV5FQ7Yig8Qxii4jMjkiza-qA6EcVCcW3OPSmArR9z1RzIpsClTqHnM1lxn1QD4Xski4RyEJQoY8Q1UumWcoWP-7xS-bPNfLJFRRrgVbProJfWbplpV8olxXHX5JZjgeZbgY_sWhz8xkaFZ9dp0sPDKN087l_mPXrwqoIDQIDQIdmwgr2osgB2qr5yyU89pR5C_3U0F5vKPtTkQGIiOMBDr26V8XnxMAINsgFLeWUYK2vJmQcnjYy8S1THa6Mtyk2ywzpbWdDArMRZH_ybEYpK_Jy1hXkm9cGcEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tp68x8bCv14zYr20MDoWhCJdJ-oFBQiebi4vaIe3lt43U-4UDI8j-iQS6voQH8xgdaGj2CnZHQW3Vp8dArbzxLn9fbKlsUZCinz9y8kokQvMp94Sr4BTz2Z61GDl0uxiqJA-rN_O4rVY4_qTLpwJvUUsgkUl63619vLRu2XAjYknXl6lpOBjUDHMWdWWCJCqnZVYsLWy42NKLDnmE1nrLOvZWlOfPHByNPf4uCoSPjImRHll5abNk4XcVzLN7mY3R0ONYQJpgO5e6p4HlSqkiRZpls9rkh6AmCqJ8nRAe2VIBKIGtE-PSckZWi5Tzxl34P-o-g4OkEgpdw_u2vuCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6YJ_CP3oEgywtpA19nzExIKqfb0StSCkqYnBoZxYg_P-SXciR48od4SmwlLcHcQR2PYWSrmruOHwq3qTKKlT-Y9aDjByanuhUP4UdlGeAevGZSgcnaybnAC-D2UR8UF2u0TfWs4Ee0QFi954Ph7YBvIDkoHb6MaQxQlv4MYwBpLzx3vjKU6t_tnFJGbsc4u09OZWyjqSHHoBXuQRMB_X2dVImYSLGnwbG_7OUQGyQM4bg9PNvOf9ei9xd_DwLy1uVvUwg2LCmj6__4i5CPWBlQkC25YJZtuCoYRY7Y5P4fyjV_Btyi6kBQiXdBjE1cOaKEaIyedubsWYkPIH0YGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIdX1wEDJDxCt4JT87oE2BKt2_aagEaNG--00_g93scFVqRykhN4oxNrOfDTPCrhyRIvO0FUsJn4bZw6Bun1H-XneH7YxUshpxtb89J0TMxQwU-Vv-sI_OkOOYY1L1Fzg7NlE1BujEqZg5AaMYYJ2aYPLiKvDFg9M9ARMSkyP6Dj4x6gK2FtZUZB69jP48GP1zAy9Viz_55-GudWXuIjQfMUZs4BrVlLiG16yZmWngMGGvBBfXCeWyFZ_g_NqZRqSSLfWO8zD8py5Y4ytEBm8uaBABegg0wow_eCAAeFT6RrjkGF88TeOhs23UGDH_6KeS18b-YVrK5tYx0bCJ5ubg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=cjIhdb68Twoq4Gq3eHCOcuNk6-KKHMd2OlJsmmOIucg3uGEhhigh1JA9WJEqSGzzvKQeaxs9fYs87esJKVHCS15DXwvq_1sjr5oPIyGu5LLJCl2TKfba8q2jowU84KbsC0CbfHrZoiQfP8hzbkrySC_tH61aydmdp5mBxNe7OWaIuTY2-3Zmsjh7Vi2_yWrBKdZfEv-HgddijuuyYf4YwFThkzvZKQ-_kEOXTLER8hS_5iL3NfaEvJhEChE8yMrfmKWFVrYRBjkAcIuf5-YjwBRkjUfMy5-EHP_kYfxsFPw2HhpKoZRqT-twLTy_AQ_MgtUJZgTOQVbnyBHaVBrV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=cjIhdb68Twoq4Gq3eHCOcuNk6-KKHMd2OlJsmmOIucg3uGEhhigh1JA9WJEqSGzzvKQeaxs9fYs87esJKVHCS15DXwvq_1sjr5oPIyGu5LLJCl2TKfba8q2jowU84KbsC0CbfHrZoiQfP8hzbkrySC_tH61aydmdp5mBxNe7OWaIuTY2-3Zmsjh7Vi2_yWrBKdZfEv-HgddijuuyYf4YwFThkzvZKQ-_kEOXTLER8hS_5iL3NfaEvJhEChE8yMrfmKWFVrYRBjkAcIuf5-YjwBRkjUfMy5-EHP_kYfxsFPw2HhpKoZRqT-twLTy_AQ_MgtUJZgTOQVbnyBHaVBrV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=p0LR7zmLXw9lyD3NfnbGcrF7mItQ3XqYL7wir3qXhDU9n7l3VhnLIfr5DbIYA3iqtpwHJgesbQj70V1wQ_IJkDdRX4BapxizsZbVlNAUDa7FUSikpOxPmXt73ZUmchXcGXwkXpLs5sDVmNwyg4qqIv75j3WGeV8Vs05QDEm6IHh_mD-6LUsjoxtUk7ZQgIPAE4_RfZJTeabhXRml2WkNinfQVgD-7Qxo31LzveCltSvNY0GoJmJgNd_QpCinnkHIP-DFJO2AId_9exJexvfx8BMh9JphNuLvwRCjDe7SxdQv2o8kKQAdi_77eoMdrXOQ7hOhGU1gvoShohNfBl6dOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=p0LR7zmLXw9lyD3NfnbGcrF7mItQ3XqYL7wir3qXhDU9n7l3VhnLIfr5DbIYA3iqtpwHJgesbQj70V1wQ_IJkDdRX4BapxizsZbVlNAUDa7FUSikpOxPmXt73ZUmchXcGXwkXpLs5sDVmNwyg4qqIv75j3WGeV8Vs05QDEm6IHh_mD-6LUsjoxtUk7ZQgIPAE4_RfZJTeabhXRml2WkNinfQVgD-7Qxo31LzveCltSvNY0GoJmJgNd_QpCinnkHIP-DFJO2AId_9exJexvfx8BMh9JphNuLvwRCjDe7SxdQv2o8kKQAdi_77eoMdrXOQ7hOhGU1gvoShohNfBl6dOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=mPsfOX2VZH38Pw7rD-QyX2McRJFboYWYo5ZhS5GqNtIPPf2D9Ol4QWua07GWPTWAW7BWcgs_jH9Ybkva1c3hAnl-S0nhkCs2TncYTijsXCW0C2Z69n4Br5MRVPvmrMW3MhjGQV-rEK5TXrlGHbao6e2HOoYZFxUYAwUYr1Df5cFkaPvdGmPnuPa_9p_zqsuiW2dTUtiCFOrjZcQwLsGvS5S3F5KEDnV09Fz_GNzEdVleJ75UQ-q1l1aFeOWIF4DgnVU8rQ-gd3RDMsHtV5k48jMVDjI4Os-MKzxvhdrhlB7Ryf0mG_PZtYGOJeBOy7Qkq1KFnpx6hqxysq3o1JWZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=mPsfOX2VZH38Pw7rD-QyX2McRJFboYWYo5ZhS5GqNtIPPf2D9Ol4QWua07GWPTWAW7BWcgs_jH9Ybkva1c3hAnl-S0nhkCs2TncYTijsXCW0C2Z69n4Br5MRVPvmrMW3MhjGQV-rEK5TXrlGHbao6e2HOoYZFxUYAwUYr1Df5cFkaPvdGmPnuPa_9p_zqsuiW2dTUtiCFOrjZcQwLsGvS5S3F5KEDnV09Fz_GNzEdVleJ75UQ-q1l1aFeOWIF4DgnVU8rQ-gd3RDMsHtV5k48jMVDjI4Os-MKzxvhdrhlB7Ryf0mG_PZtYGOJeBOy7Qkq1KFnpx6hqxysq3o1JWZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=mNivQVusQAKWRS7vqOxI2NDp7opuFLojSngSxgoftvGVDjDyi5QUHkIldcdisRmtbYNdvdBxFLYWoGMmRo2PoXKPvpVhfKDxmr-xKosa_JC6C0k7J81T5oap5dvMxeQ1vTH5KxPHBcPuPeJP7MznY5AnQr8sbUlKiGTdMqWsGl-2L7CqC-Y4PHuj4EiCK4BdGH5AyUyRLuyGJ1c_e75gYdTwYnKyw4YPDMP-1qRYGL8u_PVc4NRH3cQDlXqsPjB6VbfYfsjcbQPsYq7FSMvgW-YK7mZfwT9_4bG_5UTPnnn8N8WAtWunHQzntUloFTi3WQQhmj-PPBZ2JyZzpeVQbWA_OHX6IPAbgW79ymr2WFvmme0Wg6HzRnq1SZNMOJ0BD0HqmXBKpL2JpdDl1YiJJMy38RWVRYWkaywwm1XS2gn1s5ytrQ2WTHD5AjXFrONAZ6ii4ZIU-hA9gpzQQkMBLoSyBfUOdk1KzgS3PucANIVXw-CbCHomHoAwPE3Yy73knGbSpW7NaGX5gtAv2PWVWxmJ1Yk4v9hfmbwp-nTSoYd3PcFeNzixADGQww04V1MxZiAod6oqQ6X_AopOAi3j7Prid3wLRmYR7ZWyjU-bW9pJfrKyhe4pN2xYN7DlVzGAn4Kr4KaCh8gIgZhF88OI1WEDX6-M8-8LfGzfrifUlys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=mNivQVusQAKWRS7vqOxI2NDp7opuFLojSngSxgoftvGVDjDyi5QUHkIldcdisRmtbYNdvdBxFLYWoGMmRo2PoXKPvpVhfKDxmr-xKosa_JC6C0k7J81T5oap5dvMxeQ1vTH5KxPHBcPuPeJP7MznY5AnQr8sbUlKiGTdMqWsGl-2L7CqC-Y4PHuj4EiCK4BdGH5AyUyRLuyGJ1c_e75gYdTwYnKyw4YPDMP-1qRYGL8u_PVc4NRH3cQDlXqsPjB6VbfYfsjcbQPsYq7FSMvgW-YK7mZfwT9_4bG_5UTPnnn8N8WAtWunHQzntUloFTi3WQQhmj-PPBZ2JyZzpeVQbWA_OHX6IPAbgW79ymr2WFvmme0Wg6HzRnq1SZNMOJ0BD0HqmXBKpL2JpdDl1YiJJMy38RWVRYWkaywwm1XS2gn1s5ytrQ2WTHD5AjXFrONAZ6ii4ZIU-hA9gpzQQkMBLoSyBfUOdk1KzgS3PucANIVXw-CbCHomHoAwPE3Yy73knGbSpW7NaGX5gtAv2PWVWxmJ1Yk4v9hfmbwp-nTSoYd3PcFeNzixADGQww04V1MxZiAod6oqQ6X_AopOAi3j7Prid3wLRmYR7ZWyjU-bW9pJfrKyhe4pN2xYN7DlVzGAn4Kr4KaCh8gIgZhF88OI1WEDX6-M8-8LfGzfrifUlys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=WDF4vxLDfk51PQng7EP5i8xHnX71hvOHk8nrBpqChfH81sRbj7viV5xve9Bhu4nKCi32AVvhUzcXqrgo5oDVeTOJflETcPCCTSnjRWE38pSxpOZMT7TRaXa-YrLuylrx8MIFgOHqiTNjw7pSTnak7jKjfxJWGHs7jz0jhoesx-5RRHv4mFMfXCXvjzQ5H3YeasVJuEXUjNb9BCukNiaSKdiB_-uDK6Zi3wXggjYizcP-LOhlDYEVW13sDNSrhKWDyjwgplsKwaXKdoU3_KthsovVLXVFLG3mCqFDOK1aW71YNA8htLlI5EVRenN2iiYTQZXWC4vHiBhvNQGpHjISEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=WDF4vxLDfk51PQng7EP5i8xHnX71hvOHk8nrBpqChfH81sRbj7viV5xve9Bhu4nKCi32AVvhUzcXqrgo5oDVeTOJflETcPCCTSnjRWE38pSxpOZMT7TRaXa-YrLuylrx8MIFgOHqiTNjw7pSTnak7jKjfxJWGHs7jz0jhoesx-5RRHv4mFMfXCXvjzQ5H3YeasVJuEXUjNb9BCukNiaSKdiB_-uDK6Zi3wXggjYizcP-LOhlDYEVW13sDNSrhKWDyjwgplsKwaXKdoU3_KthsovVLXVFLG3mCqFDOK1aW71YNA8htLlI5EVRenN2iiYTQZXWC4vHiBhvNQGpHjISEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=Vm3m61G0N5ZSQu77fsW9LDMsjxdTqGi1TeET-rXhzn25_GbzSOLHPmYNWzN_YqxdKAaY7s35pBeR1oWST_4H10Q0fjqMSV1UXKET3P1MapI0VEu9riKqO_nbSm4sCr3NIIct9iyyEn6oJysiifNdii2-i5Og_YBx6_FE_cDkhIHnunBon9duD973yuhcqlTs_o8-yK5TJwWgpidlA9zW3lGdtUdF2TOFpyS7H80jS4DYQpb6Y7rRWj_vpOCrpIY7ma_JRmvqsyFqYu3mll2THckPOmqIwTTlWuz6zloQe2cTHexOg04gArK8imjgB1m1h8DUK4RI9eKfMcRIcpz6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=Vm3m61G0N5ZSQu77fsW9LDMsjxdTqGi1TeET-rXhzn25_GbzSOLHPmYNWzN_YqxdKAaY7s35pBeR1oWST_4H10Q0fjqMSV1UXKET3P1MapI0VEu9riKqO_nbSm4sCr3NIIct9iyyEn6oJysiifNdii2-i5Og_YBx6_FE_cDkhIHnunBon9duD973yuhcqlTs_o8-yK5TJwWgpidlA9zW3lGdtUdF2TOFpyS7H80jS4DYQpb6Y7rRWj_vpOCrpIY7ma_JRmvqsyFqYu3mll2THckPOmqIwTTlWuz6zloQe2cTHexOg04gArK8imjgB1m1h8DUK4RI9eKfMcRIcpz6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHjUBqu-yQuyqeKagFBvar66XwwkGVrICrXxF0o22089oR2AG_FmeSHGl0djBKHfcR9doRLg6mfV70oH6Tl8H-V9_ZHfn3_TpCU_aEOmYlwdWCrEXjd0bZ-d3L5XPYEiRtFMJsTdUAf0P11nnooOkQQFP1-IIjtQK1HndIc-njkdGnOZ7BDxr2KKx44A8qU_xtK-eSBfYWI1ssE4BSPf09dmmGla9BzbrBK4An7QZqczoTwNLNsYS8dK4KsV9ojauMByyiuchNfO0c8I-87M0DkgZ0wcgYkHwEmQZb0t57WX7q3WO2dVdyTVvCVQxE_kHpavyjSKxfLXXmpRHNWsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkuE7kVndiYM6TbVRCnrnqjoGOR0Y3HQsGpLknVInSqQtzBRMF9cS9iaFgsrqpAX9yZ6oKhj2rNoLHsnwTnQHnwcpeTdxI9UYKzvTymTuxyKrWdZHg_35HWJQmG_9WaU9ToQVhGdxSSP-FVI-zWv7oQrr6lDl7Hf8zeqJL5PficLDDO8NiO7_I-SPLBfoqIMN5KMuoyvt8TE8COMPylbUXEinAr2zpUxYr9m0gWc5AEYZh48aK_mLglwJR9ILIEVdmzW8iJHSjysQQa5VY75Ug-PJCi4xx7f1qahI4b7glsjLdDtYMotW-khRhR83oB05UvyJ7rq-HBHChd9xQ8aEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=iVIjK5R7wy6Hqd4VEzbwJrzoqq_wRm2S9lQ67P6QEIoEzkA-7GEtV2MvY89Wd2b_yhn5etfpdOptGq0mX2Tbtt24DZpjbVGb6Rs7JdIzd3dR2-I74gZNiyO3QK0Y1EjmRu5hUu1JZHgydMkrZoGXmRF5CX4Yd6NbqS3ATcVME4ntVF5WbkDvIdsg31l_hAJ-boeNZqLXv_9FSovTX7C8Zf0cAcPjy1X_G8dYt-EyADwO-O-1KRqYaXVb_SPwe1zmSwLpaX_KAwWze4LNlp7YKXqjbjMYQ2R5XiD1gjBNqN6cGxrPDPn-_joe2Wktb9Lb0r1i0RttiVjGNG45kUXggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=iVIjK5R7wy6Hqd4VEzbwJrzoqq_wRm2S9lQ67P6QEIoEzkA-7GEtV2MvY89Wd2b_yhn5etfpdOptGq0mX2Tbtt24DZpjbVGb6Rs7JdIzd3dR2-I74gZNiyO3QK0Y1EjmRu5hUu1JZHgydMkrZoGXmRF5CX4Yd6NbqS3ATcVME4ntVF5WbkDvIdsg31l_hAJ-boeNZqLXv_9FSovTX7C8Zf0cAcPjy1X_G8dYt-EyADwO-O-1KRqYaXVb_SPwe1zmSwLpaX_KAwWze4LNlp7YKXqjbjMYQ2R5XiD1gjBNqN6cGxrPDPn-_joe2Wktb9Lb0r1i0RttiVjGNG45kUXggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=gfuL4sVjVE5HBay2WMpsTXHC6rvqE8w4ZU2JPh2TkALpwUqqpJZ5afZZBiVpYtJyqDyVBJ0Fx-4KvGPqpY8ckJgsgPhDzbTgHDSSBn7IxMiKZL_FxhsXpSFLElIP4AUdPKciNkNCxs-vCZaVy85ar25K_SUQxTSf3jNQt2MvSqCwGv9Ass3r300YK3pm0n0rY2mqgEhRT26ydflwzjLVwWnXOhbIPb2QMfT_Sna3yTOley8vbX4o5K3Qa81xdL3b1S7247-cBiDje24umvqWLKjLY8_zbUvo4kU4ElGzILa0HzfntJMk8X_mWoJMYKCYUCIlRfV1a0uzLWbW7iyzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=gfuL4sVjVE5HBay2WMpsTXHC6rvqE8w4ZU2JPh2TkALpwUqqpJZ5afZZBiVpYtJyqDyVBJ0Fx-4KvGPqpY8ckJgsgPhDzbTgHDSSBn7IxMiKZL_FxhsXpSFLElIP4AUdPKciNkNCxs-vCZaVy85ar25K_SUQxTSf3jNQt2MvSqCwGv9Ass3r300YK3pm0n0rY2mqgEhRT26ydflwzjLVwWnXOhbIPb2QMfT_Sna3yTOley8vbX4o5K3Qa81xdL3b1S7247-cBiDje24umvqWLKjLY8_zbUvo4kU4ElGzILa0HzfntJMk8X_mWoJMYKCYUCIlRfV1a0uzLWbW7iyzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=U14SaRV1txkCmq_Ff3DBub4lt1O4NhbROVfyXix220LZuPhIRrC9T1C8kLz-BMKt0E-0LzLTEL6vJRgw4OfxAoRR5IuttGDBecIHf_Anyg2ZlU0QfnEo-Q-MHACr2PTSkP-bn_q1AgVYvhW_cspqgbCuWsdvY97qho_AsN4zEBtlr1LkvTgQrsqMwmz5yKVeEKPuruE0h88RhMOlruFYG3htytF2SmQPe7JtbM0T0Pns_14eJjQRz_FDxCyFF-61W59Mij9CrYNmMubnH0c3Sz0RZX5ksHoM7LptmMEX2cS4sCWQMkRQOwReJCpBbA4ZQggi2ua5WKcRpMWoXUwEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=U14SaRV1txkCmq_Ff3DBub4lt1O4NhbROVfyXix220LZuPhIRrC9T1C8kLz-BMKt0E-0LzLTEL6vJRgw4OfxAoRR5IuttGDBecIHf_Anyg2ZlU0QfnEo-Q-MHACr2PTSkP-bn_q1AgVYvhW_cspqgbCuWsdvY97qho_AsN4zEBtlr1LkvTgQrsqMwmz5yKVeEKPuruE0h88RhMOlruFYG3htytF2SmQPe7JtbM0T0Pns_14eJjQRz_FDxCyFF-61W59Mij9CrYNmMubnH0c3Sz0RZX5ksHoM7LptmMEX2cS4sCWQMkRQOwReJCpBbA4ZQggi2ua5WKcRpMWoXUwEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9rG6TdxUtMhJwISa05VSW3t1puzuJacdkl3KFkGGsnulemM1LrNX2zdohEx9e2_IIReuZmcBW5aChLqvo8F8zoc-oQQ-JirX2I-gZBoSdCOiG-bYI5NoD8HM5JD_Jucg0XimdeOVZrKqYR7jU3iT3Xsuu2eumI5hxjY6SDljBDZ6CFXYeEkV3oB9IDn5BiSzwqSYvVQJQL1p7br6jhUsKs9HXtoKnqTz9y3rGeAEqB3jV3_OucABbvA4OKCZXnMXvDfRvaWMUaivEnNDKdRbuvXraFnw0fqPqix1zHDwfJpp8CLYnCW4dk145Ib9wk2JIEcV_BYFb5OxLFrZCQCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=Gl16joYa7l86ZEpIFXwxyrjB3HVVNAp4pADFmxJZ360auLPds1c8iMFe8E2JbmevaZSy1vLP5j5OtmVlUJMr7n1-gXL6hYlodse60piYxQc78g6S6dgUW-fQ6jlxPpl0f24tIK990ML9HRjlzbkLA3ClQtP5tV8IXaVKuJk7xo37OeuNSWtzzcnE2HKfIX35YgOqcZ7Cb_qcJWE_VvH1HEcYDq6fik3By-ZLz6q9eXn4pW5pYrkvvELgNAhqJRJYeiFtIcb_YPk1cUfUX9dWFhoEttwDD1cttfr8pUVt_o8gtwb3U19GG8q9pupfZzSgRWSBflmCZ0tnb2CQATEBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=Gl16joYa7l86ZEpIFXwxyrjB3HVVNAp4pADFmxJZ360auLPds1c8iMFe8E2JbmevaZSy1vLP5j5OtmVlUJMr7n1-gXL6hYlodse60piYxQc78g6S6dgUW-fQ6jlxPpl0f24tIK990ML9HRjlzbkLA3ClQtP5tV8IXaVKuJk7xo37OeuNSWtzzcnE2HKfIX35YgOqcZ7Cb_qcJWE_VvH1HEcYDq6fik3By-ZLz6q9eXn4pW5pYrkvvELgNAhqJRJYeiFtIcb_YPk1cUfUX9dWFhoEttwDD1cttfr8pUVt_o8gtwb3U19GG8q9pupfZzSgRWSBflmCZ0tnb2CQATEBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=fGhryYCNgzotEusVFNP5P1_CVtmIWYxMJlEvBCU2AvnIWIAR1KajD1YL_HQvqAgbVz4W9isgzbzOJgT61gkZsQmTCyO3uzAeGtP0jOSvVSykTejfcPqH9wq7w70UcqDLek-jLnNh54_YYtVD28wdKkcGGQCKhRP8Qwc_jX3TeYnNJmxyBk16HHnIQ4KFC_q3ycaqp6Y96ZasXfCo05hUfu97LN_zMDOv1n5rI8Yp9pUUS7bO9WMwvsrbZEHwED8gTS_1D0adB8LUIlv4h_98SphyzYGRFj94_mtPS2q04jpcWxvFRY-jNvnaZ0oh0vVyNLz3E1c1bBcQ0FiYRlY0RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=fGhryYCNgzotEusVFNP5P1_CVtmIWYxMJlEvBCU2AvnIWIAR1KajD1YL_HQvqAgbVz4W9isgzbzOJgT61gkZsQmTCyO3uzAeGtP0jOSvVSykTejfcPqH9wq7w70UcqDLek-jLnNh54_YYtVD28wdKkcGGQCKhRP8Qwc_jX3TeYnNJmxyBk16HHnIQ4KFC_q3ycaqp6Y96ZasXfCo05hUfu97LN_zMDOv1n5rI8Yp9pUUS7bO9WMwvsrbZEHwED8gTS_1D0adB8LUIlv4h_98SphyzYGRFj94_mtPS2q04jpcWxvFRY-jNvnaZ0oh0vVyNLz3E1c1bBcQ0FiYRlY0RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=C6ifQCeeKR-6RrXOuAHK_hSJFqv3zOzkWDhMlSBb1MnEA4xc8BshzlrEbuvyzTORDV-xbabRj0iTaniFo_mCygt4hGvjzAQcVCynat5QDFv9JFDKhF_oLw3DtgB4Gk1tu7J6_lOwlYDUGJ2B5GTZeFQxx-PJWHt-rv5TzEQ9PHpT6q5-OneDfvqUbANqDis38lvE0nHvQjGtSBnzYe7Cj1yQre4ywx9HU3feEenqAhfFejICRNA_iZ5QkBGh_ojn9NEUM6hcXugLfxkmPxumT2a9TLO-jVdYt1OotZvPjLvEaiHJnMT4d_ZUXxhvGkKGN9J6h5Ki0y8DTGJSFNWeSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=C6ifQCeeKR-6RrXOuAHK_hSJFqv3zOzkWDhMlSBb1MnEA4xc8BshzlrEbuvyzTORDV-xbabRj0iTaniFo_mCygt4hGvjzAQcVCynat5QDFv9JFDKhF_oLw3DtgB4Gk1tu7J6_lOwlYDUGJ2B5GTZeFQxx-PJWHt-rv5TzEQ9PHpT6q5-OneDfvqUbANqDis38lvE0nHvQjGtSBnzYe7Cj1yQre4ywx9HU3feEenqAhfFejICRNA_iZ5QkBGh_ojn9NEUM6hcXugLfxkmPxumT2a9TLO-jVdYt1OotZvPjLvEaiHJnMT4d_ZUXxhvGkKGN9J6h5Ki0y8DTGJSFNWeSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=SDnNYRQFLMzG13HQHQtfv35ArGlyvjH-VxquYkhLgJJTtKYzsBl6SgCR08znMk_HkFQF9aCbkAYlj_7aR-AbCUoGDlOCP1uPAObNjJWArb7-Sn4H2M4Mxwuxy7hj5tvu8oViqE-t3NnwLQsNs_L-lbYBC0CiZEBPOZQwFiZ9FtLBUjdjLjJ8yvivQQ5X5DCcHv0qM7EiVMpHD1yJ1-0-p87p-2_t6jrm-dNrhhAJHHXUw3f90hXAklplGSnrsEseoLMfFmryzlIcCfrWNqMK48kyU_ZFjbHd7pEWfjBr9azKBy_j_bsH7NnNT2rlnN58_9T8kTKEBJmBdSaeRr-XHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=SDnNYRQFLMzG13HQHQtfv35ArGlyvjH-VxquYkhLgJJTtKYzsBl6SgCR08znMk_HkFQF9aCbkAYlj_7aR-AbCUoGDlOCP1uPAObNjJWArb7-Sn4H2M4Mxwuxy7hj5tvu8oViqE-t3NnwLQsNs_L-lbYBC0CiZEBPOZQwFiZ9FtLBUjdjLjJ8yvivQQ5X5DCcHv0qM7EiVMpHD1yJ1-0-p87p-2_t6jrm-dNrhhAJHHXUw3f90hXAklplGSnrsEseoLMfFmryzlIcCfrWNqMK48kyU_ZFjbHd7pEWfjBr9azKBy_j_bsH7NnNT2rlnN58_9T8kTKEBJmBdSaeRr-XHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=RsqTMHkST3rDz5Rk3r6deqBR5UjUIz1wT2KRHYalsIIuDMSM6GZAO_pe9xSWx6miOFKdMhDWIaRWJH1Q07amvNci1AUWZbPbZeUNDQfg8dsK7FTotVuJBvVBGA21HMfyr6yQuiZRya8Rn0shsZPZNqbcH3lExw6TyVxfFC-m8pl0lZ-7HrbAQvP35taZn5ghLy9yAd74xqM6jCXLPqWOHp0obk3nFuLdLRwL7MptWUXTrnf4OQlo1d5logkbfz3p4h7tKrtSra-k5pdo4lKy9NBmpnUJ_856fjLpLpD_z2tuVbBxrrm3nBsNHfqDj16nW74Q-hCacSve9BHy_8iRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=RsqTMHkST3rDz5Rk3r6deqBR5UjUIz1wT2KRHYalsIIuDMSM6GZAO_pe9xSWx6miOFKdMhDWIaRWJH1Q07amvNci1AUWZbPbZeUNDQfg8dsK7FTotVuJBvVBGA21HMfyr6yQuiZRya8Rn0shsZPZNqbcH3lExw6TyVxfFC-m8pl0lZ-7HrbAQvP35taZn5ghLy9yAd74xqM6jCXLPqWOHp0obk3nFuLdLRwL7MptWUXTrnf4OQlo1d5logkbfz3p4h7tKrtSra-k5pdo4lKy9NBmpnUJ_856fjLpLpD_z2tuVbBxrrm3nBsNHfqDj16nW74Q-hCacSve9BHy_8iRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=oCxv6j7LwIrXLQMt92ZPGugnkRPyo6VvmTCtBs6zUCHsXAcAp0jnimeqBtBKLH1r38-qNN09OXq88iZ24OmmTc_enTIzQ_7V2NC7EQrtZTKG7Xwo93NHC7t9KhXk-K_sdAOixbEylXZ5LoQxaKCcgCpAKE0JgFV7daYfN663OTu5RJIDYNtVraJuK44dImxTGxg9msVfIKmGZg0aemSPCJ-_F0FdzDqIbg3Xrq9KwlUWMne8EHOqBwSxka9FHxQmuDXxLMcevj2tIhbwr6vKsapSgkyHeuU4YkxEtqm6kMNeUbjkF63js99OMFZpnWK2qfzXoy6VSFYGPKh-wML_cbSdVeXzqwG9OKYAELH6FNLz9a4tUTtzQyvKjx5Bx_YNt8up8HkyBkBsaYiOfQqkFStAreI9xF-7WlcJQZSmT6wN3RTjppzfRzgjzB8K_H2ER7NeGJ4yK2khawLtw3NhkVO4zuyCcgxyHvqNidymvoFkF-cGfycbYBCbVNysQ3ojQntlhfz4i_O5VbTBMvVOe0I4E3MVin4aJzHodMaqUNiQN4aEOfTX2W2qGvpVbbDSTsTSUB2vQq3GRHRYya-P7asti7mmGbXJyR8nF28_1JP9_fYaOEhDrzBWxWUwFLDnnINk8lvM2w3AVpdml8H8hNObElBDVW1BvGs3k9_rLUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=oCxv6j7LwIrXLQMt92ZPGugnkRPyo6VvmTCtBs6zUCHsXAcAp0jnimeqBtBKLH1r38-qNN09OXq88iZ24OmmTc_enTIzQ_7V2NC7EQrtZTKG7Xwo93NHC7t9KhXk-K_sdAOixbEylXZ5LoQxaKCcgCpAKE0JgFV7daYfN663OTu5RJIDYNtVraJuK44dImxTGxg9msVfIKmGZg0aemSPCJ-_F0FdzDqIbg3Xrq9KwlUWMne8EHOqBwSxka9FHxQmuDXxLMcevj2tIhbwr6vKsapSgkyHeuU4YkxEtqm6kMNeUbjkF63js99OMFZpnWK2qfzXoy6VSFYGPKh-wML_cbSdVeXzqwG9OKYAELH6FNLz9a4tUTtzQyvKjx5Bx_YNt8up8HkyBkBsaYiOfQqkFStAreI9xF-7WlcJQZSmT6wN3RTjppzfRzgjzB8K_H2ER7NeGJ4yK2khawLtw3NhkVO4zuyCcgxyHvqNidymvoFkF-cGfycbYBCbVNysQ3ojQntlhfz4i_O5VbTBMvVOe0I4E3MVin4aJzHodMaqUNiQN4aEOfTX2W2qGvpVbbDSTsTSUB2vQq3GRHRYya-P7asti7mmGbXJyR8nF28_1JP9_fYaOEhDrzBWxWUwFLDnnINk8lvM2w3AVpdml8H8hNObElBDVW1BvGs3k9_rLUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM6NocYzNqpEph2pNRfmvxFUveLtrhlv3xvd2B84ta93yaNPBkXe8e4ELs4QE5lCU_ZlXMPIMZ7w6O9n-MrU4qwOMUJNMTuO77LynLdsyCQfzOi3mFdemK6r8Z4ZRN9qAu-dHS7672UWQSUtj_Wvl2DzQwW0TJ9Ga2EZiG5HdoupMMzRbXE8Wtr5onBmGdDJpMwtrEjVpsoa6RG2hXqdI4xx-MPO8PBr0QksbhrctJsNoNAin_3by0LBRtZ6m4TjZGpXB9gW749Cl1LktQSCwyJ_VqnygyhMKYGiD2RrXr9YB-AdTSvY6iYfC39ZJPxf3KMh--uxoxLl8M7kQhfMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a2sSZRSFqBEFu4hC2KAN7wvsfAZKVLWvnyjUM7K4JN3uuOb2E4uEjXiUhVwkFm3F3MQgAs7LrgOf1wwXcYu1Ayizdxz9SltwGLu2X_cMA7VouS9HakCKuTNyQRZC7PSct3EUckzJ9iNLZ1_oTk2hp8AP30tu_Mu1NgCuh3ECNcpMXSeHJRpIyJsq9QlTIpVl0y0BBqukHiI5922ynvmeSZUBMsPbei5Q3Kn0mpFEnlJhofYeHy46BWSAvKdHyYBmlFnNpI0bbwW9Z8izyA_Vx3PBznMglqN4FnTdeDAvMDA4GTNMcbvcFddXfo2qNs4gDlvCWVumFOkzX4BOlH4qsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYLC86DOLTG8l2cmr-aGfBd9BY3IL_Paxmu-GhALH2QVf9gobXXdT6leYZXw49dMWjq5l7d9VaVNLL2lVUsygbggHeSQN-WtoYk7JrQlYo4Lh1mgXsdLA-8IN8vm2lzz5KqvYF85Trt2YrHnodLbIlD6MBPTULe1esEWOH4yZFUXO31FA6Hz7LApgWF9_Hqm5Ig0otmq7hWEBqmgY17Xdi1EkEopIs0iQTyvoD8kVbCj9g5IAFdlpEvvNYQEH8kRQ62xoEPaKeffxN8jg7HjrtK2w2ZXVVvEEqmC08woPjl7wkZBJ_h4saKI4OSPJqyClziBYYjK1PozDyCnhO4Esg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=gtqe6GTTdxIlHU-OSy0sNyyKVwlskuaWdZIS6pVHvuGnt1Yhw_cfzif9EPUFN7LrzQ19tVLAs6VudZ6YXNLlpNib8ZYWWDeHN7iGEji30qvSOQBrwBNdtNjqIV-4cAElbdbbQTwmel2M04Knn5uqiJ2v-df98vS_hsuHL04NR_CQHby-A57YgtoCC1LgUzNHCOI0eKHoYqFPYzIEplzW7eEQCyrcxFbATCOnG-sOyf549snaDtJs2KYR1sP0LCfRr46JmBUwo7-aI2_3gBOF0zWoWI0MCvPm-JpeA2UYtPDf_BNz41bSrd2GA4GciUMhZWTPqjHTFkpjxbnyOnLJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=gtqe6GTTdxIlHU-OSy0sNyyKVwlskuaWdZIS6pVHvuGnt1Yhw_cfzif9EPUFN7LrzQ19tVLAs6VudZ6YXNLlpNib8ZYWWDeHN7iGEji30qvSOQBrwBNdtNjqIV-4cAElbdbbQTwmel2M04Knn5uqiJ2v-df98vS_hsuHL04NR_CQHby-A57YgtoCC1LgUzNHCOI0eKHoYqFPYzIEplzW7eEQCyrcxFbATCOnG-sOyf549snaDtJs2KYR1sP0LCfRr46JmBUwo7-aI2_3gBOF0zWoWI0MCvPm-JpeA2UYtPDf_BNz41bSrd2GA4GciUMhZWTPqjHTFkpjxbnyOnLJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=L8nfjvuCK-t4KO0aKsPJ8Isc_1-AvNYb3v0N0vxsDgSROvq5Nh1DX4YHCq_9GYCZYVXebc9ULjoBcmc-FQCrGKhxJ1_hMkSR29K_tLLKUnoL-H7g_hg0rApExYlRqVwBWvWtTt7wUe9CrqAsymm4xhRnHzctTS2NHUbgL5YpYslZm97BRZotOZY0nTepczRS-_6QKvQqgw2wYvSuF0aeyCoagG46xDmlkNHiThHmjqGt7WH4dUpVVpJR8aciNo6FA8i_FbkX9M3nIzzd_Lx7lQ66lV52pQTW_QjST6DnDb7ZE7GB7JBLmZkfycMTvBEA1RCXp3OgGrK-DGK22wtQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=L8nfjvuCK-t4KO0aKsPJ8Isc_1-AvNYb3v0N0vxsDgSROvq5Nh1DX4YHCq_9GYCZYVXebc9ULjoBcmc-FQCrGKhxJ1_hMkSR29K_tLLKUnoL-H7g_hg0rApExYlRqVwBWvWtTt7wUe9CrqAsymm4xhRnHzctTS2NHUbgL5YpYslZm97BRZotOZY0nTepczRS-_6QKvQqgw2wYvSuF0aeyCoagG46xDmlkNHiThHmjqGt7WH4dUpVVpJR8aciNo6FA8i_FbkX9M3nIzzd_Lx7lQ66lV52pQTW_QjST6DnDb7ZE7GB7JBLmZkfycMTvBEA1RCXp3OgGrK-DGK22wtQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=BRD6Y6r-aMdoMwVJflO8wObMeZAlxj6ZfLxo32jLvivt8J7bgNrNOe0cRyhOfh7ecY2Vr5ZYSLxM4dvPvS99OsQMDuCFN_yTnzRM0-YuMCztdfvC0F4yPDd2XpwDVheBN6XvAwwIWRH0s5oPyqZug7jscD06rHKLC_IBJ3IYZfdRZVENeShUlkWESZKX-tU0cfvRdTR0l0WD3UmgB37LGy2B42Pw_nMtHnMpcpuDq7VQBRZrq-R9lTfSq5txSF81KoF3UbEHcg26WmN_vHpjQmvv-7UQrqDyrR47C5Csf4rXtUZvqKBoEnwcwknbwOQwsBJeiZiPchLeuvNcbe5fZzW0oe2KpDt8EVrPPc_lnsUwU20Ntb1u1JXuT87Un6oZ0Sy-cRRQ5dWsmW7MUA7_5HuzoJHGDcDO4_MqEor1ObjmiLqv-yArMieNeGTWyKw-4rRDUlErL9RnO72xqcqaWZ6TE3IZcz2nTXCubeWCfIFgDfg7v6HqCxKepqtqXB472h_h3GeYkz49q6PTl-DQD5kysjUt0STM3MDEF7CY5Wr_TFkrYARWbBH3JzNTQX-bS5Go4zlm9PTMTrTNo_JI6Id_GaUHBIFaHmqMb1vZbR0U3XumSf3FFBIcK9d4Cd_79ySL-ZtwgWIB4Zi-JAUcDqhVThePMwrtMGTgRQe-5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=BRD6Y6r-aMdoMwVJflO8wObMeZAlxj6ZfLxo32jLvivt8J7bgNrNOe0cRyhOfh7ecY2Vr5ZYSLxM4dvPvS99OsQMDuCFN_yTnzRM0-YuMCztdfvC0F4yPDd2XpwDVheBN6XvAwwIWRH0s5oPyqZug7jscD06rHKLC_IBJ3IYZfdRZVENeShUlkWESZKX-tU0cfvRdTR0l0WD3UmgB37LGy2B42Pw_nMtHnMpcpuDq7VQBRZrq-R9lTfSq5txSF81KoF3UbEHcg26WmN_vHpjQmvv-7UQrqDyrR47C5Csf4rXtUZvqKBoEnwcwknbwOQwsBJeiZiPchLeuvNcbe5fZzW0oe2KpDt8EVrPPc_lnsUwU20Ntb1u1JXuT87Un6oZ0Sy-cRRQ5dWsmW7MUA7_5HuzoJHGDcDO4_MqEor1ObjmiLqv-yArMieNeGTWyKw-4rRDUlErL9RnO72xqcqaWZ6TE3IZcz2nTXCubeWCfIFgDfg7v6HqCxKepqtqXB472h_h3GeYkz49q6PTl-DQD5kysjUt0STM3MDEF7CY5Wr_TFkrYARWbBH3JzNTQX-bS5Go4zlm9PTMTrTNo_JI6Id_GaUHBIFaHmqMb1vZbR0U3XumSf3FFBIcK9d4Cd_79ySL-ZtwgWIB4Zi-JAUcDqhVThePMwrtMGTgRQe-5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXk_WCVUq1GU0SkO2sO4hs_mcv3UmGn9KVCWuqd3iGKExaAmq8ON67u6Nz4ZA27N2VhCg3a79qr_GrbovsosMTCoEmeF9Mpm6N0f8dYwW-uEEnYasdj6J6cNqbfoUXtPZr6ZQqNUfrlkhhzJwR6dYINLNbPW3gby05MlBmTu6MR8erd2zyNRkMFduHAaTbP3zAWzonRWjc3H1I179L0AToS_-jXsbPhK2uoGvQeAvY-y2bAtTZhbmaHpXBJ1zcoQ9MDDxgC7wEjP9zqA6tE9Hd3M2A-60v7TZu07cub24CBSCm1iZ-4vZ1iasVWS0C-VF0tJKPcFxG9c9ByJvJ20hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=I6EX8FmyXBR4rLMnLsYYyPfN-B12ctK6NlktwHqNkSorvgnjrmi4zS8zQn_aeVCnQNnPFU7hOpsot1uV-_j8okLubciT7CbcCICJj4lmfIsL4b-E0R0fULIK2nSRitOqrIxcXsnW6VfRYWKwhVdZ9N5jMHku8wYZ9yeMYLf-ypsYXn_1O4FQs4E4eyXYFalEJJN8cAF4V06bIS2MNtt2YHIkAbDtQ6zstkJNIdsS3nXbDPueuAdfoZSW-UzNV3JtxQt-_hbc03mIJ8B8BxQxZerHp9Lb20H0l9v-junWUBGNKI5OohQq4LEZGUlJohrDgMnpc0u1RBgIe5KCO3c1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=I6EX8FmyXBR4rLMnLsYYyPfN-B12ctK6NlktwHqNkSorvgnjrmi4zS8zQn_aeVCnQNnPFU7hOpsot1uV-_j8okLubciT7CbcCICJj4lmfIsL4b-E0R0fULIK2nSRitOqrIxcXsnW6VfRYWKwhVdZ9N5jMHku8wYZ9yeMYLf-ypsYXn_1O4FQs4E4eyXYFalEJJN8cAF4V06bIS2MNtt2YHIkAbDtQ6zstkJNIdsS3nXbDPueuAdfoZSW-UzNV3JtxQt-_hbc03mIJ8B8BxQxZerHp9Lb20H0l9v-junWUBGNKI5OohQq4LEZGUlJohrDgMnpc0u1RBgIe5KCO3c1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=BFzv14FzbeBZdSCu2AwB3n2YEdog3Q6R31PHlzNV5VHK4qjrn1QyD6LMIrqmNu_ZPIma9PB0zhGpJam2kkf3GAFigQnLDH-FurTEaNLY7KS4gSdIEn6wWEA8r--aHXPceqgtG_-L9Sy0HLH1cmZbauxwrmDnhwmX81I5y5F9FIT5R1FMOkxIsLppDZA5Yu-wXbqE1kpyZ8-iMiVjvldRrSg66MCf2USm9x6rgzV999GQl9TBO_95apvlHyRF4-sY0dj2VGRljg6I-wrpEn-0BHUm7sRnGOhPbmwKSWJTyxRfFFnyB64Z8pdmhA26FKyIXTJVuUZn-Ji8h4ggmcj1mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=BFzv14FzbeBZdSCu2AwB3n2YEdog3Q6R31PHlzNV5VHK4qjrn1QyD6LMIrqmNu_ZPIma9PB0zhGpJam2kkf3GAFigQnLDH-FurTEaNLY7KS4gSdIEn6wWEA8r--aHXPceqgtG_-L9Sy0HLH1cmZbauxwrmDnhwmX81I5y5F9FIT5R1FMOkxIsLppDZA5Yu-wXbqE1kpyZ8-iMiVjvldRrSg66MCf2USm9x6rgzV999GQl9TBO_95apvlHyRF4-sY0dj2VGRljg6I-wrpEn-0BHUm7sRnGOhPbmwKSWJTyxRfFFnyB64Z8pdmhA26FKyIXTJVuUZn-Ji8h4ggmcj1mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=bEMh59LgmHV0fdqtMSshIn-8X2WC6a0-9PKPPsu5mLoLrDMUAtySo5aLBfhEuXGJazbM0doJ28sUXC-CnOsBMIYgd0C23MQglML6JOdJLh5RqyEFLmW1SZ2sKiiGNbVwDdkXpthuUnmOc2ZKb8XSuTaE-sOmeiekkSU5oFE8FuAPbinmjnD3v7fd-hL-ZCjfeX68KE4k9-dEAusqriQH3zuqy7DyiLGWotQR5BH5flC-FeFYpuuwwl1nwXuw6VC87ryrxVVZOR-OhZY8eXQybW6EjIRzKWWtwxJxtVY1yorf6uM_afiWZfF8FLC4ruejEYEVYBLx9OsOxg6RyE1MdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=bEMh59LgmHV0fdqtMSshIn-8X2WC6a0-9PKPPsu5mLoLrDMUAtySo5aLBfhEuXGJazbM0doJ28sUXC-CnOsBMIYgd0C23MQglML6JOdJLh5RqyEFLmW1SZ2sKiiGNbVwDdkXpthuUnmOc2ZKb8XSuTaE-sOmeiekkSU5oFE8FuAPbinmjnD3v7fd-hL-ZCjfeX68KE4k9-dEAusqriQH3zuqy7DyiLGWotQR5BH5flC-FeFYpuuwwl1nwXuw6VC87ryrxVVZOR-OhZY8eXQybW6EjIRzKWWtwxJxtVY1yorf6uM_afiWZfF8FLC4ruejEYEVYBLx9OsOxg6RyE1MdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPa01813iq4vsF1Lpd1ptUHb06VO-bhADVu8gTLuM5dOQbW7PnlHONjKFGtwIkbJR-lkK-O6EfgagTtdwuCIEjeLsEnSgNEKcU7Kc9JrHuF3-E4ejDBxs7OwIi4eEye5eD0pUVpv4xDG-qU5aOsf3IL5SrnPvpV6x7E6WQrRWJRENeRsuoibDXRfhml6vnYICej-hR7xllCtgB5YnB3qZslaI-HHSmndY7lfUFABMiVBAtH6-wisa2Ml3MK1Bb8y8IRmLc4wCEsBvO5tOQsZvxbVGdYDh6o7cp0nscIDkZh1tFDfWP5Q0tpQ1YDRzb8QYLm1NBRRoxHG4_vAomPAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=BZIGORjPP_EvfoMDr9PtibNB94xe3Zm7wUOqX3D7yKiWKYSz0wmQNRV01JrCoJHNB4AlsU0CNirN2P8_PTtRzRw3RJjrhyr67fQnrgZKqS6LlE4eLvmtnCJnIeKtYpiYH8PWKoNuJbrYrsQaDuS3hZ4kOEvfrDJnvWEsTDCeNqEgYlgcQBwsckHcq0k2JI7O2HmBT7vmBcp3JklbRMKNWYjbDoQwB5-cnkC6HqcQAIRrz84T20TzteGoeisp7PO8oHA2OJBWE0cntNcH_pH_82xLV2fVTfHqe_i_na-e3BmtLuHnrMbozPS2k4FjbZQwgWm8RmdpXilLn056ryrZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=BZIGORjPP_EvfoMDr9PtibNB94xe3Zm7wUOqX3D7yKiWKYSz0wmQNRV01JrCoJHNB4AlsU0CNirN2P8_PTtRzRw3RJjrhyr67fQnrgZKqS6LlE4eLvmtnCJnIeKtYpiYH8PWKoNuJbrYrsQaDuS3hZ4kOEvfrDJnvWEsTDCeNqEgYlgcQBwsckHcq0k2JI7O2HmBT7vmBcp3JklbRMKNWYjbDoQwB5-cnkC6HqcQAIRrz84T20TzteGoeisp7PO8oHA2OJBWE0cntNcH_pH_82xLV2fVTfHqe_i_na-e3BmtLuHnrMbozPS2k4FjbZQwgWm8RmdpXilLn056ryrZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=bQqJSqX6ItQLIVXdBR8RCtELfg5XsXg6f6N53o-kzVqE9Yzykr2L12Smeefnv46N9hfoBysUHTrQSEp3RFoompD9N3AS39uxRpc2XASOvpyCJTHlGKNCUYRVB8Z3AUYPj_7DA14Q4pYuR-LiTdjdV-c7y-xywL58uXFCP8Q90W7p5s2nPjehm7hLrLZTm2zlE44Xht8q4AxtXKxwtE96kePcE-fTBm1zmEAMBcBqz1vv2lrqXRi4Zhwz_2auhbSpHAlZSr0veaZHc5bomIGHm-GzUm1ug-KlkMUeL62MFIAMD9FXCyoY_Xkc04NGl9J7UnTkT9mXr4a-HGo5sTnu3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=bQqJSqX6ItQLIVXdBR8RCtELfg5XsXg6f6N53o-kzVqE9Yzykr2L12Smeefnv46N9hfoBysUHTrQSEp3RFoompD9N3AS39uxRpc2XASOvpyCJTHlGKNCUYRVB8Z3AUYPj_7DA14Q4pYuR-LiTdjdV-c7y-xywL58uXFCP8Q90W7p5s2nPjehm7hLrLZTm2zlE44Xht8q4AxtXKxwtE96kePcE-fTBm1zmEAMBcBqz1vv2lrqXRi4Zhwz_2auhbSpHAlZSr0veaZHc5bomIGHm-GzUm1ug-KlkMUeL62MFIAMD9FXCyoY_Xkc04NGl9J7UnTkT9mXr4a-HGo5sTnu3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=aQFxQ7merDM6vt81yxBifRzHKjPMyCvYWfk341HNAdP4gDikJY-Tkgnp1JyJ1DBqR_O_cFeDlC0XHYNoMrBE8KbbdFBEBAu8CMoe8rPYR8M39E450laGEgUH79cy8hVc-dJyTnRfLD2nh5Ol-gknvO-qiX3CpEBp0qvZVKi-VNSSsjJ45JeL5AsInFyZ1QXc_DEcERWkf2ZKIjbjOFdKDybsTcIAfBenBcS6sN_cgSB2V4KKxTTixwut6dYZtOgr9_l9OoY5EhgfZGvHXL0TQU9RJqkOPd-zxOoFiIKKTtpn0O6lIazm_cJ2m49o77Z6KFiY8YItScMEWWzimXzbkReV7RY1FJ7hgHc0plUaowo_yiFSglqdBPgdHdf8AcVLrm7f_SlHyIG9385srEPe6ns33T35MxrHTy-YgISKYvExkT5qe6U84gUooul3jyLP6L0EXvapLz2wobY4JtHvFzjvhGmluvdQHpENpmQtNw03ZeDCh3ZLSFF312QE_qVVdh9PYuMyvPGfMJ8MwAQXkKKxxHj8fIMpAOdB3ZUQQQKa7uuBbIJ_e6cpumJBHoGG7JFiQlr_HPD1DW5594Uj-NT2HoPu54HjrjmY5UzeIkQQh977ot7dWuxxCjyXgm_bPOUeiqjbpWPtFRyP3kZoAIzNOQ0B2IVG3r1uBy9V-Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=aQFxQ7merDM6vt81yxBifRzHKjPMyCvYWfk341HNAdP4gDikJY-Tkgnp1JyJ1DBqR_O_cFeDlC0XHYNoMrBE8KbbdFBEBAu8CMoe8rPYR8M39E450laGEgUH79cy8hVc-dJyTnRfLD2nh5Ol-gknvO-qiX3CpEBp0qvZVKi-VNSSsjJ45JeL5AsInFyZ1QXc_DEcERWkf2ZKIjbjOFdKDybsTcIAfBenBcS6sN_cgSB2V4KKxTTixwut6dYZtOgr9_l9OoY5EhgfZGvHXL0TQU9RJqkOPd-zxOoFiIKKTtpn0O6lIazm_cJ2m49o77Z6KFiY8YItScMEWWzimXzbkReV7RY1FJ7hgHc0plUaowo_yiFSglqdBPgdHdf8AcVLrm7f_SlHyIG9385srEPe6ns33T35MxrHTy-YgISKYvExkT5qe6U84gUooul3jyLP6L0EXvapLz2wobY4JtHvFzjvhGmluvdQHpENpmQtNw03ZeDCh3ZLSFF312QE_qVVdh9PYuMyvPGfMJ8MwAQXkKKxxHj8fIMpAOdB3ZUQQQKa7uuBbIJ_e6cpumJBHoGG7JFiQlr_HPD1DW5594Uj-NT2HoPu54HjrjmY5UzeIkQQh977ot7dWuxxCjyXgm_bPOUeiqjbpWPtFRyP3kZoAIzNOQ0B2IVG3r1uBy9V-Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=SDhdakv3QHzfau4pD_LDgp345n7isOc1BcwILXZ7z-PdUE6WEV8RzuJnT_zNk-KYMiEDncZm6N5McWkuwfGecLkEmTA80xGNrS232U9xHq6G5wGCmVq0vC35Hadizi8j4P4c0RYj1g_xyUittJJ_CWWstuVJx1-Nv1ZibzfxPtXsSfRAyyXCOi5Drd-YLKKamqqf3A1Q787mIFQDiHUb77ZWhlsH_ju6bqOcvMGm11PhfFgwKnM5IWlB0Juk4oRZqvPGbA3RrOq6aQmgiFvK70B4S5a7ofzmgtHx8ACCSStG7pLDb830WwZi8jd90n0Mn1Hyqsw1wQa0o_QuCwMRcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=SDhdakv3QHzfau4pD_LDgp345n7isOc1BcwILXZ7z-PdUE6WEV8RzuJnT_zNk-KYMiEDncZm6N5McWkuwfGecLkEmTA80xGNrS232U9xHq6G5wGCmVq0vC35Hadizi8j4P4c0RYj1g_xyUittJJ_CWWstuVJx1-Nv1ZibzfxPtXsSfRAyyXCOi5Drd-YLKKamqqf3A1Q787mIFQDiHUb77ZWhlsH_ju6bqOcvMGm11PhfFgwKnM5IWlB0Juk4oRZqvPGbA3RrOq6aQmgiFvK70B4S5a7ofzmgtHx8ACCSStG7pLDb830WwZi8jd90n0Mn1Hyqsw1wQa0o_QuCwMRcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZKRU7jnwmbK5dgMbQdyBXEgFmFv2zg5kJrR84C6nZHet0fNwBx1bYrw0YrhpJyXRc8WshL1xcyVsGaUd2Xgl8miKpPqpQleuLpX1zTZFnxRw_z9VyaRp6ctGz1Y1O5s7KFoTU89wLHLIk_QgRD4t0KgRB49mpWZg4cQyJZm6WyrhVYGvkZ34mrzFwDysLVE_oAS1Jh1Pev9nGhKq5xrx-BJ7rUntuv_gE3V4NjdtoKe5wu0iNMDB8F2TkiFqSFBFInLuDC4Kp_yjV9nAqtp53tJAXcQKel1gJA0gAhkvOU9ac0RMGTu-nOp4cXZ3xwTwOTf4YLS2QolMO-AAFT2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
