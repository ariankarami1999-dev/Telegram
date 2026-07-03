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
<p>@news_hut • 👥 211K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 00:05:52</div>
<hr>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ENSkopgj3JXfFSeEOYbqo2eruKq5Edd6uXeXvu_pj1G3br8DcKRbTZ0tHhq0y0l0eW2H6P0LG3qUbxg99ag38C9Ksb7_MCB9om1jESbEyB_fTJNx28yKneO9ckwN5X3MV5T0ad5Jmc8QJqwRNSTC8ZK7X5B1bbx9MqESLbAkDISRA-7Tju_8v_nyQoQF5YVNViGsEKVj0joFJRSwfA_yJBsyGzKIFUSghqZPXSDAIAo7K--WXXVc9Cq2No9X0oySGYziZix4OU4T9Y8rIMdn6PBOIF0PSWxe5oFtEVs99hoKOtZHhSBpjCEm_6XPQ9xkilXiVmnvywHGzq2dmXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrM_b_XCOK2IvpO_UtxfdYuZzUjU1NJ_umw4cgwCNdN4dWfVU-0bjUSVNBw-e67Bp1p-tvcgPD2F9Sa03oobo-UQBRdl2shbP2YzvXVsVZjrxu2y8kL-sNiRD5V77BI5G20bhbjyY-ZoRT2ZgTGtFXJTVG-bHtZi-oe8SBUcl47LJOn4_ZWx_ns0MwF6LUraCLp2wwmNixH3TcEMcBiAOxLnadAuF_wki-7GEvc6qGOX3hryjnc5hyykwMM3nyWlvjO9SR8wsGEPvMUnRceOzwA3ZcuALb7kl_6PCb1glI-8s87VG4Q5pNrcu9OzktZ07SlLwJ1s33Ia1OkIm1y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhVfeSQS0-k8zhwufwtMKdG94WBlV8zZ8n5rCJqOpMvSWNItbr8NhQPrVGjXmOyzJ43wrOGztWkkHey02-u4Ozty4WoxkGiSuiVnVOvLl-SzZsK2sKL74_oG52gfx17PMiV_YY4M27pnLV-vO90iimkCu4Jh18J_Furfs7iMTHp7Cs3cWDyszi6y_s6mSLiegv-ehFjEBRDALCaT-xPKqWGD-X6INgc5Px4uPERfcrTfor5tZdZEUV-Dk83Lw4hUK1Iye9c2rBrrMxQm7EDzqnVO01qtyMKBcASw8amTgXWKem1uXFh2Bq3rYn4XgasIKWoq73nn85eKMcaFkQ99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfb7i3vKjbMXa19xtT2ohmM62JvwU5v_xC57UlCYTptHJgGVGcIECy1v55bNxPILnZWuLIyGwTuQt_TyjvH4e24PfmWeDgYka0uw3RsRg2xhIO0H1PMK6r4dSW10ZbVJsRslyQEqJ94S8BBl3UBnXgP15DOXAb8C-YnxvoxvmL21qNJheOqbq7XmcAm5vXOt0GuCRjw7RzjVHU6xbj6aLQcUWIbSRAZ3LsKK-4jsEnHRN0NtQpMOP-TWs7xO3SLdmiWtTDenYbYRXHJnJL3EU68sD32g6qLZROghnrCL1cX3KFt-mDYk06I1giUqGyXs3ewRKENxCyXHS4WisPtAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHJ72TPPAe7iW-fBNt1czBEUDqk7nH-AIBEPZtyRNh80PKTGV5QA611QNuBKqCMJ_vZmyrKbFm5gW5RwKdBOoUNBIjOqjizL23Fn0s8lR3-cVADN2M-tMLo-iummAMWOhqvd9DeCg-aoDtPKvAl2hEhbtjNhD6cGsAI5m17Ke5FmP_00xzBRULN45IebrOSPEg7n1P0MGkBXY_v0eM5vo8aRF6EbDT0SCnJVDSMXc03MFOKWYsN8nVI0FVLvtP0pYxhvULsYfCKj3TgjsOX_A8mrrZh8_GwerUOBVlicuVAb1DC4UGp7BjvPQ4-63kSMfRq-q6uxzYbX9ECkiYDM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YjzF9HVK8ZbOHP137q9dubClR7M3XkXPCkf4XJ0ZzzxNbxpFux-Y3e7ZATMpcQaePG8lHmUpjAMe65pVHtm8XBQNAIFJB8_x5y-HMEZgbLkttEgPBE41eFMdG_EDUn9fGPCbxknHVz2jHe7efHy0dj3opG4bOGLM4Mwm4K1z4POZXVJIWSPwjEcVa9fue-vAenptxDwmkFPGDah0e7CwKXoTvZOhExhkpGLhxPeqCdubwLM6RhGW6L2T4SgacHu7weZgk-rHgcrx_5555IgHf4t8gjirYF9MZWLtemLh4z6iBumB-LBh5UKMe032-MIDzAnN_MJY0TY_3icxzJqP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=NK8MRJbk_AFJJIgDsawp0C6uAfs9Fr4hlagK6bYTNMGeE_kpbK9q1lxeeC1k7Qvji5gZ4jDWSamSmzmZOFCG43hgkkLy739wgFxOqY1dUe4raR1s8cFXQXt-VEQW7k9O4_zUPg-mQpIGI9OQAo1bEKQCI1x10TY9aTrxrWTOAj46OBp5rozCUPrs63SptDF9otnz5Yg0K_EeBCXpTEVzV4Se6fuqDlPJeasm8UtNciYhRRBmpbdliZTJtEkcMl31fqUrsvO4xxg8v9PQ7F9vydaRsuYFW_8djtA4s6Fe1oK5pv1h5OQpZ3wJqkBnwp0YGgMC1UU9BC81AmYiVtuwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=NK8MRJbk_AFJJIgDsawp0C6uAfs9Fr4hlagK6bYTNMGeE_kpbK9q1lxeeC1k7Qvji5gZ4jDWSamSmzmZOFCG43hgkkLy739wgFxOqY1dUe4raR1s8cFXQXt-VEQW7k9O4_zUPg-mQpIGI9OQAo1bEKQCI1x10TY9aTrxrWTOAj46OBp5rozCUPrs63SptDF9otnz5Yg0K_EeBCXpTEVzV4Se6fuqDlPJeasm8UtNciYhRRBmpbdliZTJtEkcMl31fqUrsvO4xxg8v9PQ7F9vydaRsuYFW_8djtA4s6Fe1oK5pv1h5OQpZ3wJqkBnwp0YGgMC1UU9BC81AmYiVtuwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=v9GTWsBpyIsFNCMeSuJvDA1cAF-uwnq1UM9VWM5VCsEL24LlZSXjyjZmn55XI9Ms_7-D4ZlPHnGtmHR_L5hZnArGDmcvLuVr__vP8ZJRCO8Nu-LSUYyHI95Ybnv0JWuRW5s28uaWY_uG94fem-pTBZl7U2RXoMQ-KaOp874NYH6BDpHoZHuy1uOu3F3_sy_0mVqVbyPGpfLTY4aEZO6_FnOczirQvAUeuOuBnI1XK5UqEOGEiwes5XQhx8ufUtLNG9HHb7zCyBDdhJ6v8tOcbeIhzFR27LOOLDWRZxfqpKR0UHL8KjAdi6-kMfJBhzP7EH83iW5q6sk8q9-PlB1rpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=v9GTWsBpyIsFNCMeSuJvDA1cAF-uwnq1UM9VWM5VCsEL24LlZSXjyjZmn55XI9Ms_7-D4ZlPHnGtmHR_L5hZnArGDmcvLuVr__vP8ZJRCO8Nu-LSUYyHI95Ybnv0JWuRW5s28uaWY_uG94fem-pTBZl7U2RXoMQ-KaOp874NYH6BDpHoZHuy1uOu3F3_sy_0mVqVbyPGpfLTY4aEZO6_FnOczirQvAUeuOuBnI1XK5UqEOGEiwes5XQhx8ufUtLNG9HHb7zCyBDdhJ6v8tOcbeIhzFR27LOOLDWRZxfqpKR0UHL8KjAdi6-kMfJBhzP7EH83iW5q6sk8q9-PlB1rpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOffS2N7OHGboVmRoeG6o1qoasmi3LzMueLjNYQ3suTViAC_Nk33fyx5hG60ZlwoErKhiEueQLj3YQUEi-faUkM7KZ3baGxeXxFQ5gDqdyxzVurU0mkIabhqCwIuOfjGw-UYbCxgSwsQs7MPI3-YSvaIYwpUVzl8sxONEf3vYIuaKBDeoeCCmpbc48xa1PPvo0OUXN8EmX8KuBr_26dkZlAHJ7yO36QwUWB7vuD4rHLObmcdDlgqynL_RvzQ25qdl2-3oWXaK9SpksxHP6Y-GWjsLm2EbE48nbzdkLJXsijR82jn-TP49MhCdzztfgRfsybLexZUxSqmiLya-1f0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxDX9_bQ0Mrq1PcEnVb1gfqFuMM0pk8xRQZ_m8iqEkox0Kfd6W2GFbXSYYw77Zv15kEp3mH0LfNzdiSZzl-aGteYKpSB_YKcJLAu_S9EsZt4RARnlqNAT_VRevAbTqQ8liZuMG1QM69sfh9pYucmK9w9XYxazJZY-GnIhJKnJzGfQsLLvxDa8TormROnyAdc3-XtECLWDXVBc-kySY0yS8gmlVZfqB6_3N3X7zXZBHOi00TzgzL9ldhe2V55f3aexO5zMXPxJ6rqoC3r3ZirDUG7ePAw7jcPPKWmDF_syuDwdR1VUzH73cSb1L2nlb62uKGyD1smeKtLsECwOM3yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FybWf5vXNj5A7k0kO-JN5WxZ2_8Dv69nx01okn1oK4RhSQgx2kvTJsXYsDllXAQlodDVCuw8pF2Ua--phLNO_MgLiON3F7CtpzqDLnpoJCImsHba9WIJzsS2P5C2LpQ1ldiCdUyCD6LLWK7VLpVB5EDNl4blV0Xa0V7Suwv1jGVylSeOMJTyzl6oDft6t1aEyrJtG3B92s5cYm-dqA58YmzFIeTvI-YGmI4qyeRPigDFGI90qjkAILVrMJCkJAYRLYP4WaS6BMaLbsk-qQR7wpENw_7Z_ilMpE-5tPfxyIV7LJ0LkxhABDoM2kVgZVQwt7xFy1k471aDmqb0oMvilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHCBypWj8V1smiqBxI6jysT2rPmZi0ZHfsqPyz6OLnyYWwj6Tl5MLZJNm-uHHTbUX8IwjxVS2_9e7vvw8BXO3s5tGrtjsJKzMAO9yVSsslDKJ0ysKf2THTUV7ak-Gmriq6SayV0wrnLyb0-4fbGZDqXss9P32XUa1kiuccuHi1zu-AhOKLtyI1UWX4mUuWgo-rqheI1h3zc-_I8Z3XlBPvLpxUPepN6cDsrWKqpy7G21MTEgMq-QQs_bav1HDKKBT5v5jv26tGiWu3vj3FM_SQE3qgPhoW_ZGyBMuaSmzdwXCBwAFyqOh8rsXSmu-xWBBUSNBrj7Dgk2FKEWFu-Lag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=hx5wyi48Aei-t4C_nl1o5cl8r8KmzOfBSyYRy_QxepV6ZgHQBPOTqZUr8eTNG7vJQfhx8bg65l58IJGYd4VA8jI4U10xxqJE9gngBFoXLTOCUJmWqh-2faWcp2IxWkAOuoux3L-N5c5-Ywhj_PbtnSDtG7fYVXLY9SbjYm3of7lawzyh5b42zALEqM7LmiLN84aLnJ02NAlKihGBTvuUxVz1pTjMM6qpIWMZiMTo1gv54TZ5129Mm9SlYTOuDDdklQ--bpdyH-z2G3HgL1CXfuTBSHDsk8V_VckK4wU8KHxM6Z-Hk7HNuWM-k5TybJVh65bPtAz9sY5Co0qm17fmSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=hx5wyi48Aei-t4C_nl1o5cl8r8KmzOfBSyYRy_QxepV6ZgHQBPOTqZUr8eTNG7vJQfhx8bg65l58IJGYd4VA8jI4U10xxqJE9gngBFoXLTOCUJmWqh-2faWcp2IxWkAOuoux3L-N5c5-Ywhj_PbtnSDtG7fYVXLY9SbjYm3of7lawzyh5b42zALEqM7LmiLN84aLnJ02NAlKihGBTvuUxVz1pTjMM6qpIWMZiMTo1gv54TZ5129Mm9SlYTOuDDdklQ--bpdyH-z2G3HgL1CXfuTBSHDsk8V_VckK4wU8KHxM6Z-Hk7HNuWM-k5TybJVh65bPtAz9sY5Co0qm17fmSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5a4yl28hBQfANfcodhYttgvbWdIvwbeMqfRg86yT2gAQKMn8F5Ogg6tcqqMjWezQvktYzS4_n-Gd7NwtpNIuv_vo64Ew499Q90HpY1ny26kTFavYiEJg0ciJbWXgYJO57TlW0hNGkBeaFKfgiKJD6jJzgdBeee3ikSGkFowoWkURZysTIRtfej17kIapKZhW2F4jwUnocfJzJCby3kLZPzbjvb5c_q49trdLY3tgNRmIGocR-eimUZKA0jwT8uD8pfJWtp0NSzqQxtpvUPsszVDo2dEV8EzL2Y6uZFt4y5uRUjhjgTddmPCdGj3sIViZqryDUUbTJquMTVMl0b3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1D29GK99dkEsFPOa6NHGoQvzHAk6Y5GOXCFYadPGYimG53TEvKUm0cGnbTzPRMQusNPfkdAWcgpFP7ImSO8dtJzrvY89b11w7MSUFNskUpgzlKlD-4jsYDAys3OzWuzsKRqcLXFJaiwe80V75i9P7Q8PEJmGdgJEH26XqHrDFejIeb_hxLauwgvGN-SyHscvhMf81omehbQvAxCpgWi5KfbmZaQ-PlFrsxaExRIBDPPN0TUXbdi_jP6MvrgJ6UDaNwk5jvx9e3uZ29GQLu_EQWjAqguEYC7Sz1fj_uyJ2xoBdeq0csyoyGkUNoD2FPCSvt1oXW2sxVDU4E0VKhZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE9hlzuE6wHxUBLtmlUUvV6NbH-y91Gh4DyiKbA-bCYPyhaIWid_xqSYSIAPHFq0AkAxSZrfrmybelu_zSl0BHGW19P_QIardt4J6kCmOCtaB4GJ3Pxrv8Z3Al73QvpJ2VSZfAtweHZeKtR7tgagRyPZaRS8lZFBARsWedxEyGBPFgtCol7mbV_rx9zq1g2E-mhAoZRqhY6I21lAGl96Nxy-U66ySmFgbWJJtBiMcEgs7xE1FwoCGg4yeClFX8qjGezGXDcCer5C_00s1XIcYa3hE36DYsXftMn0Gw0i2_6-vVnQ7VQ2Ezvomc0eW8jZQNan6tZ4ib0Kx2uui65c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=pV0s60M-4Y7s34Y1vcsFYuJj166_WejWtOiBixiCKKnztLUKZ3UxCcM5Za6L_sm8gX3fzonUKObTiNHjTKtIlKcgihhDVCLuUyV3lS0aU3Gsm8qbVAr1OdAv2fKcFRK2qFQHKsMDJ9uXHNcXgmZT8aczhZMqQjtmcs94BjiVZJNd6MvlqjwDHgfajq0izFz9bMCwA6j7Tffrf2W9-LFRWsGDz4gRi2btgfLTdj9xRNrPkeWYniDH89FoCthJNVbwQraf-f_Hu_splFVTTVTyaKAHGebg7Q_Pk6nXSIgr14h99S5AIkJdxf5AuWoovj0b2_Vjx32bLj8IK99PCr5joQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=pV0s60M-4Y7s34Y1vcsFYuJj166_WejWtOiBixiCKKnztLUKZ3UxCcM5Za6L_sm8gX3fzonUKObTiNHjTKtIlKcgihhDVCLuUyV3lS0aU3Gsm8qbVAr1OdAv2fKcFRK2qFQHKsMDJ9uXHNcXgmZT8aczhZMqQjtmcs94BjiVZJNd6MvlqjwDHgfajq0izFz9bMCwA6j7Tffrf2W9-LFRWsGDz4gRi2btgfLTdj9xRNrPkeWYniDH89FoCthJNVbwQraf-f_Hu_splFVTTVTyaKAHGebg7Q_Pk6nXSIgr14h99S5AIkJdxf5AuWoovj0b2_Vjx32bLj8IK99PCr5joQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDsLypJqJFyg16cHZZES7mrmhTdORJLoTWfFKoULhu43e-4-W64SqVevhdZxWTEXFAnbh2sH4aoNU5AJH-sm7O-Gt0YvvX3-KTTy3hSBzKzjm0MTC0FkDdMsJMNCHruCx62XtTrSIT8b89WmJZEXOuYJRCJREKfbRtHw3FwSvlTnDFRI0wui7vozuaVvX1yY7Z6jB5EzrC6-X7cyfOStueDqTvgNjiGOUohaiiheKgktz1HKdEvowNJLsxQP2MwQtV2KDaKFQ8O0hpjzNdZTwmGywp460MIOZQFGk8NTVdRTQHz3q8JquUmj3hDIoLdXjMJKCMBCVtg-_LSCeo_QGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY8bU5OW91vZLOLYk68WiiuUaU8O3AEj09sE-HBweEpNJIGzVMh50DsdOOA9cuB4KPaaiZTmp9LTC-Wuxq5xrbMnKe79ot6TzO_qzxt1vPtYdX-sHPFhrNFfw_ESmWFPzJ2ohzh1oAkS-6kf9K3I6zBvZmZ67L06LfB3AtkYlr187_rAugiixFqbL0UdOq83v5oAs4xG4m-DA2NWI8qVKEfA2ShBubFLk3WL1Xaea3Ajqf_exuf_NzKzQ6NPbi7DNgI-r5HWIxGPWeizYL5qXWYuuazHHics6FB0DTFB5ibGQPXg6oZb0d1v43fJqKh8ZeQ_upur2Fu_8A-HvpDDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=fkHBdigvO9uFgoFj7-3Jg2ANjPZfzFmXVKpm1A3S3Z20hkYjvYsjWutLNxi_rcIB1p5dm-4fA6p_fONmuJiVv1JbHchTb8MVIgeM2cRy428FgqjRQbBFOtF9P8x89GHwYTw6zB8IoysST3AK5uqwnh33YcKRQ14wNM815su4GZUEE4zdqD2xwh5dxsgDF5pOGm1wNoIYMRhoMa5AivZQrGzDMKDli1IOPK-DBAYundZrAN9NktNV9J59fhDhgPob7cyMt_oZHa301LDa7hfY1KoWIRbGh-rGmQIRzXNoy9j1jDctY1e086w1AOq6G7-xbZwvYlAQo6u2vrYudANfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=fkHBdigvO9uFgoFj7-3Jg2ANjPZfzFmXVKpm1A3S3Z20hkYjvYsjWutLNxi_rcIB1p5dm-4fA6p_fONmuJiVv1JbHchTb8MVIgeM2cRy428FgqjRQbBFOtF9P8x89GHwYTw6zB8IoysST3AK5uqwnh33YcKRQ14wNM815su4GZUEE4zdqD2xwh5dxsgDF5pOGm1wNoIYMRhoMa5AivZQrGzDMKDli1IOPK-DBAYundZrAN9NktNV9J59fhDhgPob7cyMt_oZHa301LDa7hfY1KoWIRbGh-rGmQIRzXNoy9j1jDctY1e086w1AOq6G7-xbZwvYlAQo6u2vrYudANfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Ld37-FKTMdorcEdhqavDf7Vz-KEiWPYefuoqGym51I1ArDHxoU1JabaSH32SZmpj2rZgWbWBSrXDO7Jgj-xmaofMhkSSO-PhOaOnRMZI5F_jYMXH2dm2jfSM1fxmniuXlvBGcB9mS1YfWqZxDuVLY_pNu6-E22uDJNR9mj0c3f7kjaBDg03AzqF_MrNvjhhGZkDHrtXWlI9LhEUjFaKz9gN8QivgME-z-yaDLsobxmb_sDgMXRcM_bCY8mUdnWs5VoXJDqy9193H8TQtsaQaPkgRmPSQGnX9Jk6ICMnjo8u96dlWI1OJOdbYK5fNFoq-bzA1L3ilLc7HFJLe6DXd7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=Ld37-FKTMdorcEdhqavDf7Vz-KEiWPYefuoqGym51I1ArDHxoU1JabaSH32SZmpj2rZgWbWBSrXDO7Jgj-xmaofMhkSSO-PhOaOnRMZI5F_jYMXH2dm2jfSM1fxmniuXlvBGcB9mS1YfWqZxDuVLY_pNu6-E22uDJNR9mj0c3f7kjaBDg03AzqF_MrNvjhhGZkDHrtXWlI9LhEUjFaKz9gN8QivgME-z-yaDLsobxmb_sDgMXRcM_bCY8mUdnWs5VoXJDqy9193H8TQtsaQaPkgRmPSQGnX9Jk6ICMnjo8u96dlWI1OJOdbYK5fNFoq-bzA1L3ilLc7HFJLe6DXd7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=avfeAr8chYdXFRCKj1b-oa1eIW8fzWT3YyByW1ubQvUlrIvVInFXTP_wFKSeEaZh4Oyo7fvqKcI_N3vQPHdrTxNgDMBnySJCfZ4Bkck2LoExDyYI6xljFhdyl4_msTVaRSnfAsh6YKfCDP9wm8Aa7nGgE6_s1THzhf9e26U51rAHH7UE7dXKdhIGy5TUKKG-duWzcR8wAMGUCI16TjJpoCF5kT9IG_fcstCRimjcM8rx5ssRtBJc-lNCiOHlYcujoUD2wlP5_pLLp1scq-U4-hjG06dVKbtb9_T_vRSPcz-d-RSjOS-klqx_jSplZibuSphH2kiuIpPE0OWW0v9E_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=avfeAr8chYdXFRCKj1b-oa1eIW8fzWT3YyByW1ubQvUlrIvVInFXTP_wFKSeEaZh4Oyo7fvqKcI_N3vQPHdrTxNgDMBnySJCfZ4Bkck2LoExDyYI6xljFhdyl4_msTVaRSnfAsh6YKfCDP9wm8Aa7nGgE6_s1THzhf9e26U51rAHH7UE7dXKdhIGy5TUKKG-duWzcR8wAMGUCI16TjJpoCF5kT9IG_fcstCRimjcM8rx5ssRtBJc-lNCiOHlYcujoUD2wlP5_pLLp1scq-U4-hjG06dVKbtb9_T_vRSPcz-d-RSjOS-klqx_jSplZibuSphH2kiuIpPE0OWW0v9E_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZ77b-hq0f_oeMaqi77At0T1xlxQNQPegApzpl0WEL3I57wy0UIPR6VgzLWWpPYT69kqzPsU2nTL8R1NOV0e8vFV0KWBCX1yX7NrAhwu7pe8OQlPNTiMQLbtwVtmWJs5McrTmbOMe7mziQSYCHQONLBId7yWdXP7MRa8HYXtUhabNIUbMehJlT_efj9zY60qjl6DzuC6y8Ovc_IdSUCQKEHBpaWE1mSC_ndSc686S9KLAeIMP6h9EKykXxIk9-T1Nbj__KHMUIXGqZtCsD32u6sP8jSM81NDlX2J32MK7WhzXsA7Wqx_w-C56Ipse3v94cZyUbZH7HvZz7juGIkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkCqoY-7l00Gh6AH8Pyam3txAxozPd2LPhB2Hc1TbeuJBFLW_PsJ9nuaCZeUMUL6K_EPQb7R1fHy_UWyxv_buOeGKITIES_-0KxKT1TQVA5Yfhawjn7THowuYIC948u9aKhB2DVaoAXEXwgEgv7Z9hdC3UvlEQcZGilBX-iPOfJSKDluXWY9InEaQZJZWDEtTsWuLbxC56h29dCf8U7hqfunINpJogwtQwtBpZuq-YyCBxgmtPciee5NxTyCh2smH8CHm_2CgxX6JajySNt6hEZU7gdyG1qIq8BN_Oej5cZVIo2P7eUKPsripdnZrsP7j1zScSsiWEXHTHBJ17Z1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=LTtHmW9TgUt1tpT3TdOaH1SKPFW5Ozuqcl2jv1SX5EbSor3fakn00rkMiM0nPC13TQuSZfCaQNll6b2ugWzV41IzFBN6ZdzZqMQXz64AoCnzrqfEpFaXUUgnaOkuAMKiLtEthmt0wo9AqaNw_VzK2l_-EGjSaBflMk7_cS4WVPD3iMIrhOn7R895Z4n4y0Uw5WVqXCQD7K6wpYWRE2QNMJgFhVP92Ay5uS_ZkwE2c-rKg47yEnaTwWMR1TrE3pYkWII6G5fnMqdo6nRTiTenPdbyaiD53wfo-tc9q2WO1BrzkMelr61WlSt8zi2eumRinRZ_9WXkGf2DiDY_FNj1Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=LTtHmW9TgUt1tpT3TdOaH1SKPFW5Ozuqcl2jv1SX5EbSor3fakn00rkMiM0nPC13TQuSZfCaQNll6b2ugWzV41IzFBN6ZdzZqMQXz64AoCnzrqfEpFaXUUgnaOkuAMKiLtEthmt0wo9AqaNw_VzK2l_-EGjSaBflMk7_cS4WVPD3iMIrhOn7R895Z4n4y0Uw5WVqXCQD7K6wpYWRE2QNMJgFhVP92Ay5uS_ZkwE2c-rKg47yEnaTwWMR1TrE3pYkWII6G5fnMqdo6nRTiTenPdbyaiD53wfo-tc9q2WO1BrzkMelr61WlSt8zi2eumRinRZ_9WXkGf2DiDY_FNj1Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpC8cdy7KYonzg2_GGqrgQCpOE4vxufYW3T4L_VGopYcvZrLWOTFm2Cq5UMXqEQjyzZgwNO3EvBbPxItOp7tXxI_xQRreOqwWSuEZPZrkmMpyQotv3qFEH7IhVHjVHANsXMyeRBbFrgPXwSFNQzDOqKjk4fExNQF81e3K9ALfBsjMmjVCT_ThpbpsT9LgaqVV0-hoqT-mhDhAiVr6MJ7xoLKk6o7mrjpkFOpxj8sI8XkdFXVh1ON9M5CsqG_g2U5ixKTrpPdoc8MoQoJbNYyLQo0Xn1-k-0v5IUk4Z8MooUqtXBNNc35vPS13Szz3NPndnv4etWCiCJO-Smha76QCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=dS6P6c-417ntdD92htYCcdnb_-_meqml1K6QA5dn9Kc5mpNMxapPnVLEonW8kWZk7na-9CWsU15flwJmjmMra1bKqFqjdxlTNee71xxS0HesMXNlnXhdkbM9jDGjwKbJeWmglY1OJJaw25qIFFUI7xIl8wQfsF69inQG22Ttr7uV_SUMIdcMKFTaObtlN7V-DXYmLoESCaXVYvRYYEHCsOvMEaPaONdLfwVhgjMiGGMzf3nsux8bB-gwGd_ThW0Jprn2OPVBZUJI0--1QkPsapO0pnw2KKxuvnb03WQhmNBlpi9Oby9yXXqHSmennQ0LPjHOnhoVG5cI7vdD_6731w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=dS6P6c-417ntdD92htYCcdnb_-_meqml1K6QA5dn9Kc5mpNMxapPnVLEonW8kWZk7na-9CWsU15flwJmjmMra1bKqFqjdxlTNee71xxS0HesMXNlnXhdkbM9jDGjwKbJeWmglY1OJJaw25qIFFUI7xIl8wQfsF69inQG22Ttr7uV_SUMIdcMKFTaObtlN7V-DXYmLoESCaXVYvRYYEHCsOvMEaPaONdLfwVhgjMiGGMzf3nsux8bB-gwGd_ThW0Jprn2OPVBZUJI0--1QkPsapO0pnw2KKxuvnb03WQhmNBlpi9Oby9yXXqHSmennQ0LPjHOnhoVG5cI7vdD_6731w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olPJ4Qjl3depWTB878ZnDWZVZDGtPvaWEDXBttmKk8OtiQUKAuhwdwjPZ3wySLr7ye6pMcsPc34dYnhhv6Rnv6VOPjNEehbfesNPlYrmZRfRNYsgteeyqrz-9nk6W2DPEMwQ_1JhJN5SO-WKxLTNS8ZACAIRBe9ptGNJvyKslwkC6d749oE9A_t57H2qoBaNo34iobo6vjt0Bw4E3pgq_HPTqjhvbjU2O0qDNr5oT8Gvnm5s-3QM_j7-Hq0Nscd4Dcka1RitwrY7DkPU9JCN0KoeXjg6cYqflBJ4LXgVf_vwnlxBIcivnWzpQhJFm5N4Dn5k0HVQ0zDzM1SpjEkYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=FNGHvnXcT-xfKfLkHu3ME1tocmfdvjTkzUQAOa_lgRKlM3lLvS8kOevBeEiK7LxXhZe_9xdeaUPdx8JBjFfx_EyToTkxuI9_7nouVTBoj3lBK0X5O-LRstdCZbhWcEugHdrcQc2GcWTapXZO0smuozTalORG7EBWeM_NjtIFEpgsBHCOtKrPvbXxBQQwC5xYQJXkyCmuX25IU5dZ1HrfhUUsJLxJPeOyXaWt1EOKL-GbEEXfy57JQMacBUvAeDTbaMuKj0quhGQU2l4gT_04mILB0Ej_Bsib_ygFVi8IGlbfJGnkylSgo3mL82Vnc_oGhpaaBSg0eC8lfb2uQqR4dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=FNGHvnXcT-xfKfLkHu3ME1tocmfdvjTkzUQAOa_lgRKlM3lLvS8kOevBeEiK7LxXhZe_9xdeaUPdx8JBjFfx_EyToTkxuI9_7nouVTBoj3lBK0X5O-LRstdCZbhWcEugHdrcQc2GcWTapXZO0smuozTalORG7EBWeM_NjtIFEpgsBHCOtKrPvbXxBQQwC5xYQJXkyCmuX25IU5dZ1HrfhUUsJLxJPeOyXaWt1EOKL-GbEEXfy57JQMacBUvAeDTbaMuKj0quhGQU2l4gT_04mILB0Ej_Bsib_ygFVi8IGlbfJGnkylSgo3mL82Vnc_oGhpaaBSg0eC8lfb2uQqR4dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-cUdg0VK6N-RT5ycQFCD6a9K-3SrnhfiDbnhACt3V1h_TS0g1a4Q0RCcZz2m_VqzutToSqn8UGMC6dejDFN4lyiuhfNOzGUvl0DTWmL5J_Fuslg96WOmF_IoqjkZyY6JapaPWHISWZUotVNiubZa2TRjtRaTk7FMALqVXdMpoSnJh7aFhpyQoEaogcy17qHSZpMzSsmD21lW3iYpuNy7EE3hHabmHsry9a-tp7pNtXZcTqNqklzXyBpbEXbbiq8rgl6e9GGdStw4A_11MOwUKMkaYCKBKQBza8tnA21OZGWBCPc1Eb7nTVyW0hhV34C0yt8JjHkVn5bHDjMf_wVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq1XyMbRO7j-VEsStcWIo7K9FDdXxArHHGyxwxknvbfISl9VmLkmrKFUo-QuJDg4bkS-Bs7bwbnw8jpMGJFnwhvaeWI19PtIEll5dGmoHMinX_Rmby5z0hZ2ErxeelwWbkiig-E1U0kWqI8cvGwGUgUi6i86VhmY15iwALEgikLE7ewwtX0odureC99G5DytxUb0zzJ9RyUFD46efX2BIqv5llnk77-W8nGjLSN2i5kEvh7TCx1b-6vxiqG7fmU1NKIvq2elPxL1oHFcjrG0lMLX2wQNA28XAR3dfWZ3nAPsQOZuxj4ZRSEs82OUrXISwLcDuCdnOxVDOAhOVF28PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJtfb3oOlkDi_eu8PgXTnQk9Jm7VQtdglSaSGmzUjkjFyM-St9Et7w-kDEmfkGqPZY4WkH-Mg8WUEjyyfzOLzPmE4me52WLsGt3J1sHkgWE3qOQIxWV30qDNSiPr0U8gdyupMSbc8DIoh2-YmnqgaIrXtFxsf-hOF44oVSoTTiAjFT9aMXPLVYGL9L95vpCMVjkB2CHy1upkWUFG4x81-Bbu4LYmOhwBEP_CcEFuKKSa_yrWEgZP4RsF_jeAipWb2_t4BRLmPRzKg4AVm5eJHTnhh196z9eGMvIeGp-bUJv2yS0FRvXO3LP8viKFK0eFLAZhf39mK4BHM3creaqdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwZ3k2QxTOaT1f6Ndn__R6BdbjSkiD3D1tofDQfTlVeBwWTGlUulJORx0Kn7CIVqHDGJeWe0CWBEsh18wD5x-zVk00jXUgbw_nxSVEcVi18cEK8B7Vj4yQ6msA775cQsWYsbSRL4p-b3OmmzpPEn6eXXxB7NjaavppUnQyhmVAnRv-I1-EWgj6k1KqM7UlEthT-UfFcfNgiY0yjxmnG4vcGLQVerMEdF8VJj0Xp5Mn5pQZ4BxD7kFQ8CAygE65faVFsPObl3WfWdzSF04kCOcyB2fsiIL2xtTy_WNOvrS2tDFJl3-KDg4TkmBAYpW_sK8JZP2ACZauD0LeY9ys9-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=NwzdKEkPxzTvnLv0-r-3iwsaaJpfWenOrs0gvrOqej6pKMDklYnHY5EOpCtwiLFWVZUd9GOTtvH-gbaCTiQWt6uZdDsNool-rqpAguAkkhmrCCPREecFtyy5FhtseGJSvO4ABWSPhVp97Tu_5Uyv3DeDlZAA1OeV5NncbbwrFG5Bv02ShHOOXGQ4D08II8fTK2oZ2yzvdVwjfAPIV6I33zoYMZo9KZR0Vv_JEBLGBxWKypyw4e-e_iElHVXwr7CifNSEe5BW1lMhFs335NVAofIdG7rJZhyC8LqqcHaVjfWatdxetc4DNXI3CVyB7aRxpu_n9KyD-0KCScyPc6UKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=NwzdKEkPxzTvnLv0-r-3iwsaaJpfWenOrs0gvrOqej6pKMDklYnHY5EOpCtwiLFWVZUd9GOTtvH-gbaCTiQWt6uZdDsNool-rqpAguAkkhmrCCPREecFtyy5FhtseGJSvO4ABWSPhVp97Tu_5Uyv3DeDlZAA1OeV5NncbbwrFG5Bv02ShHOOXGQ4D08II8fTK2oZ2yzvdVwjfAPIV6I33zoYMZo9KZR0Vv_JEBLGBxWKypyw4e-e_iElHVXwr7CifNSEe5BW1lMhFs335NVAofIdG7rJZhyC8LqqcHaVjfWatdxetc4DNXI3CVyB7aRxpu_n9KyD-0KCScyPc6UKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=vjP3EUgGRNmzWYCbm3fa8t0nMoS_dZpI0fuISAiQ2nMamb6tBVqMMqB1FdUAc8bXbnJkVDNGR6AEvbPRdPdRd_X4U5Kzb20ELERFT2KaqBWUEotF6pTeaEN3ehlu9WJIYclMq3wIqmidtFASNkcLrskjaqpJ3LEEvJGuk6quwoQehkZW7FCub8pNsdjCeWkdJ5u-c51GfIjvztytC7EUyJy2x0yBRBzoCaHkjG33wmMEBgRFFiPOO2XVFChPtocWBzMFT7BtNu6uiI94B4-GSoIMdiIHi8y3DT6UmYRSeSlBUoQeoZ8rBesBzHnHiyphl-xH2UFSuNaYwA9FFu1tUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=vjP3EUgGRNmzWYCbm3fa8t0nMoS_dZpI0fuISAiQ2nMamb6tBVqMMqB1FdUAc8bXbnJkVDNGR6AEvbPRdPdRd_X4U5Kzb20ELERFT2KaqBWUEotF6pTeaEN3ehlu9WJIYclMq3wIqmidtFASNkcLrskjaqpJ3LEEvJGuk6quwoQehkZW7FCub8pNsdjCeWkdJ5u-c51GfIjvztytC7EUyJy2x0yBRBzoCaHkjG33wmMEBgRFFiPOO2XVFChPtocWBzMFT7BtNu6uiI94B4-GSoIMdiIHi8y3DT6UmYRSeSlBUoQeoZ8rBesBzHnHiyphl-xH2UFSuNaYwA9FFu1tUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=SzvdsPtlZJKIuEEzrHVtYud1qeUDufwOmFndqHzIzEgrYi9rnrVYlaOkPBz1TMgk-2XIEd72SzslHXP-OsmsicUS7csa2phFZxyJzPC3_qA2GF7pOVyscGhmS29LQpknNJFiCxXyDePiIByLqcQJ3_O-LGzUnZDo5kRVlqrMSd8C6BnC2qsDh3ApQinaS1xqee2o_xyeVRtjY26bn8mXE3TEyR-YttK2Qmb0FL_LiHe1gN-EBPcNktPI8MKRR7CxdwgLVGZVfFNyG4jRfZ4fMf4gKCmWSXSgehgiuQhEkxyhS3-r2wbRQhtoTOVj38UXbNanggZ5g2BlJ0KYfs82Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=SzvdsPtlZJKIuEEzrHVtYud1qeUDufwOmFndqHzIzEgrYi9rnrVYlaOkPBz1TMgk-2XIEd72SzslHXP-OsmsicUS7csa2phFZxyJzPC3_qA2GF7pOVyscGhmS29LQpknNJFiCxXyDePiIByLqcQJ3_O-LGzUnZDo5kRVlqrMSd8C6BnC2qsDh3ApQinaS1xqee2o_xyeVRtjY26bn8mXE3TEyR-YttK2Qmb0FL_LiHe1gN-EBPcNktPI8MKRR7CxdwgLVGZVfFNyG4jRfZ4fMf4gKCmWSXSgehgiuQhEkxyhS3-r2wbRQhtoTOVj38UXbNanggZ5g2BlJ0KYfs82Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIH9h55b_yceEJzB07ZXLtIjeT2AxIkwYw3y7-wBGCkmp-0gD9aLYSq--q-yR0wruMf-wZZaYcIb5GqhMlOoU81wKku30YwagrGdBomDcDEeOB6tt7EM8qOgKV1yPeQ_hfawMzWqYZj58foRbt_NKJXM0ESLoxVMqVSB9oHLBBHZ4FsmI3X1PRgfOQC0j4OVkVo1Q3PST9FLM74uPvFY6rYnZtPQvigQDbAEH-NGLAe1ZRLYurVrPEuWORCyOumshpwZ4WDNSWJZP4o79HOgUGFiX5S848R2T3lnK_pn-_C8eZQAX0SmX1vXa41cA6nJ0ksBls8KfAnL6DOG6VSs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xg1flY_ME3eiX6h73NqhlxNxicf-KdWw_GuQb_q2y8Ku1YlYw1mxGzkG4zDPqqK3QY68FKP1k44-7m9MybRLHFGpNNQVrbdeTs6J_dd8EXi10Zlao8heb0nCK5VvnMD9FwIeXhxmBrjvsHqVf1NvQTPKsGh5WWiZbg5MaYxztwrgJ8OSICA6zWyS0kk8SpstMRwwTKZxARzTJ29dZ1nfoywhJRreGS45SWQC7A7ZC94tcjoLkxsqi4s5P6ru34m_HoRV2J-34LjUBDBuK9UD6r6ZYQrMeGp2ktv4_6TQJe1wV5ZVoiV5rZc1oTJ_txV_3oK4P0ZSn-qaG_qaB7Vocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axVLWe8mcdcu5WqF_4gKKUyeIuaB4vq30DBeC_QZquxOtcie7fQn1qRz40OHjWfAzHPwmAqGJ2RP_nWSh31MjLdmNF1ZhNt78821d2aS2D7IPDL3j6bmfDoWyoNmYpu1YDx4vn-0mwb6du60xEpfp5kV5HUOjeZTThTJeB3w-SxEb6DfZdYiWjUHxnsseQeZohyEhyzaJH0lXRihSVKK3Vg2iraFjYtllaPeiigThR54tK_vdD8zqmw_KTYM1PrlECoddsvMpAe8HMy7Q1tMLOdCus9zv9AoTSutsojFLr9JyipPZzD3ZsQTen0xaCdknttlIWiNJ1TQB9mx2rPWVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=NtHp2NmS0RIXG7rxpiS2BEJ1lfy_m6AGa3pAq9VcXqqqZunl5fLC-cViyxJgMB4QUcQnGD0mBMjulyQcIHNxfry6FBAeY0i5oxst3wfn8ZrAH1xBt5Sug20XG6JRCeSsAoUS3Gp2Y_NQRRrcP8NwtfaPHJdsPrMykZb14RfnVNJr3CO-i2PaS54s682VQjn4eigwKRNO2yjtB8jzuJYy187dojAxA4TgYuoFsw1JJnNmbVKFFbBD9Uq7KpvlTWrT0cLPvL6B8tKfGxw6MN2ZyLJrg3X2XMv-lTEOsfVomcCxWlO9qCe2k15nUR_WaPNQmGOFbQsb6K4LyWzIcYnR4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=NtHp2NmS0RIXG7rxpiS2BEJ1lfy_m6AGa3pAq9VcXqqqZunl5fLC-cViyxJgMB4QUcQnGD0mBMjulyQcIHNxfry6FBAeY0i5oxst3wfn8ZrAH1xBt5Sug20XG6JRCeSsAoUS3Gp2Y_NQRRrcP8NwtfaPHJdsPrMykZb14RfnVNJr3CO-i2PaS54s682VQjn4eigwKRNO2yjtB8jzuJYy187dojAxA4TgYuoFsw1JJnNmbVKFFbBD9Uq7KpvlTWrT0cLPvL6B8tKfGxw6MN2ZyLJrg3X2XMv-lTEOsfVomcCxWlO9qCe2k15nUR_WaPNQmGOFbQsb6K4LyWzIcYnR4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=Hm6TeQHNFMu7wi3ZvG6_NZdMY7I0nUHOElnHB8pDh-xV5wAP-kEIme7sA7Sq0jaZrvB8l60SvrlQLdxncAEOmv18Sd614fzcnkRBd7pnBoVCxpyJunFP4IrPdyJguDtxCHpUB4RqYtXotYHvH8GD72Ondd3P5c6qcs8CB455Gu5xYjalwE4xTnzURx1Tc5C2vURD16QizQ9Pzcy5o5BWVdeqHz-4pvn0ualzsOHVyPleI_UeX-FleQugCQf8fyRWgCc07nEWaZVn78ciTVUaPOOgFe5s5h6EU9Fbs3H0rs4SqzRVkD8hmZQWmnSI3TGwEmEgr6l6MAKuSXhStZD5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=Hm6TeQHNFMu7wi3ZvG6_NZdMY7I0nUHOElnHB8pDh-xV5wAP-kEIme7sA7Sq0jaZrvB8l60SvrlQLdxncAEOmv18Sd614fzcnkRBd7pnBoVCxpyJunFP4IrPdyJguDtxCHpUB4RqYtXotYHvH8GD72Ondd3P5c6qcs8CB455Gu5xYjalwE4xTnzURx1Tc5C2vURD16QizQ9Pzcy5o5BWVdeqHz-4pvn0ualzsOHVyPleI_UeX-FleQugCQf8fyRWgCc07nEWaZVn78ciTVUaPOOgFe5s5h6EU9Fbs3H0rs4SqzRVkD8hmZQWmnSI3TGwEmEgr6l6MAKuSXhStZD5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=ZqDACUCkmtldBkTlYiBcEK8D2lRBxGvfSOGymAVRVuV5nbBPe9JLzcAl65DuR9LuNtDK47TC65FNuh9YV-j-b4DwjDyaGDXkbw4jWmFjKF3POBD9fz188S2e_L9I5hoFCbqQUsPpCsUTLvn0rzvc2c8aa2SE4LRhN1GB6plo_0AhduTUTESoP1s6ZjW8i_Y0oEmDWnApASjHSlTOWijlgI1x3rQtXWZsZt-HRlZX3Ndt8M4nziVs_MGOlnztuVhpEHIiN-nqwnxgxP4ifGY2nQVDK1LxK3W3jEv6zsUpQb52gdf-20NPt6hYI-G5oiFAmPlUzt_bIuLWfIrHhBwbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=ZqDACUCkmtldBkTlYiBcEK8D2lRBxGvfSOGymAVRVuV5nbBPe9JLzcAl65DuR9LuNtDK47TC65FNuh9YV-j-b4DwjDyaGDXkbw4jWmFjKF3POBD9fz188S2e_L9I5hoFCbqQUsPpCsUTLvn0rzvc2c8aa2SE4LRhN1GB6plo_0AhduTUTESoP1s6ZjW8i_Y0oEmDWnApASjHSlTOWijlgI1x3rQtXWZsZt-HRlZX3Ndt8M4nziVs_MGOlnztuVhpEHIiN-nqwnxgxP4ifGY2nQVDK1LxK3W3jEv6zsUpQb52gdf-20NPt6hYI-G5oiFAmPlUzt_bIuLWfIrHhBwbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=lsBwcON5ZVpjHhMyjm7o13dgxQaw3tYmvxNLS_10QjupSdMesy1KK6QGdHfEU6zSwnkkHm40Es2zI-AqB7PKZ-RvB7JdTCU5mfLTWoW5c54VzBMUsFbxVXxexQLPx_GBQAAPIRKeA4Fb78rdLvLyq-xBSGndLshEdS7FrttiKtTa6tFoKwuxfblGnhMLKkZvln3bqWunhAFT2mxK1vbi8ghxg3IOBWrEPk9CFoTt0mJ3DhTTRXW8tOwiwxZUi08oQ5XTT4WEF9cwLw2-ruOWYK0Qs9sqQy2XI7MXcGUQhB9dcpNS3NNctn846vCLekPEmKHf9O2yanOXt1bzQkZiUEsZ3woEQXyiuXQ3-DjE7NdPvhOrtqrlBUhvbFRnhRhFlMtgsmZVrqewCingsrMRambGpHcNUX9pvWq51UbxD0Jz7FIv09YZsISZzaGrPy6LXyJJE4dL7tsbgWUhCt1d40XIcPjhA4PJmSFN1QcuRsghoE5djxEsZbQokxQp3fapg_2geMAidfqHzeEj-Y13yfUHs0ee3QjXqP5tvR0w85JlWP9-BiXH5ZHPqxA10qv4-_1TInEpw0wg4bC-xwMshwiOvXIave7bD74VcsIyo3Tyf0iAhd0RAZLa9YMQL9PHt84xEj2G8cI6OU0fVsGaZhARp8dKz4x8sRHZwGkc0KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=lsBwcON5ZVpjHhMyjm7o13dgxQaw3tYmvxNLS_10QjupSdMesy1KK6QGdHfEU6zSwnkkHm40Es2zI-AqB7PKZ-RvB7JdTCU5mfLTWoW5c54VzBMUsFbxVXxexQLPx_GBQAAPIRKeA4Fb78rdLvLyq-xBSGndLshEdS7FrttiKtTa6tFoKwuxfblGnhMLKkZvln3bqWunhAFT2mxK1vbi8ghxg3IOBWrEPk9CFoTt0mJ3DhTTRXW8tOwiwxZUi08oQ5XTT4WEF9cwLw2-ruOWYK0Qs9sqQy2XI7MXcGUQhB9dcpNS3NNctn846vCLekPEmKHf9O2yanOXt1bzQkZiUEsZ3woEQXyiuXQ3-DjE7NdPvhOrtqrlBUhvbFRnhRhFlMtgsmZVrqewCingsrMRambGpHcNUX9pvWq51UbxD0Jz7FIv09YZsISZzaGrPy6LXyJJE4dL7tsbgWUhCt1d40XIcPjhA4PJmSFN1QcuRsghoE5djxEsZbQokxQp3fapg_2geMAidfqHzeEj-Y13yfUHs0ee3QjXqP5tvR0w85JlWP9-BiXH5ZHPqxA10qv4-_1TInEpw0wg4bC-xwMshwiOvXIave7bD74VcsIyo3Tyf0iAhd0RAZLa9YMQL9PHt84xEj2G8cI6OU0fVsGaZhARp8dKz4x8sRHZwGkc0KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=XxTO9BrRwLa3app1Ik_NsZlyUwKnGsC11E7j6TiqLy12dVjgi-YOAQhvCB2pcK7NibxziP8dghXRR3bTwO4BN7Dq0ql9LQbP9YERhMu56pWPwCizRj8DXM-NOENYefFP_-KuuDYA6mbDutzalP-v-tdKSBXMXFMAi_n4n2uRuBkWwdJGOBgWvdnbNthf-OnWo95b153WuHGtlzr_q8kS1Yu9LiDteeDf9t9zwCx_th7uV9Y5FJD1ssKjQ9IiXAuAAJh8PfS2ghYglsDvvmfYCSvt2NtX1YLvB2PWiNzrUYCQaa_EZjxOKIHH4Jo9mfDybNayHXteZl7PtA4EgnI9WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=XxTO9BrRwLa3app1Ik_NsZlyUwKnGsC11E7j6TiqLy12dVjgi-YOAQhvCB2pcK7NibxziP8dghXRR3bTwO4BN7Dq0ql9LQbP9YERhMu56pWPwCizRj8DXM-NOENYefFP_-KuuDYA6mbDutzalP-v-tdKSBXMXFMAi_n4n2uRuBkWwdJGOBgWvdnbNthf-OnWo95b153WuHGtlzr_q8kS1Yu9LiDteeDf9t9zwCx_th7uV9Y5FJD1ssKjQ9IiXAuAAJh8PfS2ghYglsDvvmfYCSvt2NtX1YLvB2PWiNzrUYCQaa_EZjxOKIHH4Jo9mfDybNayHXteZl7PtA4EgnI9WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=FNK2iOnM5imgPi1xnrU_lAXF7N7YaWf-Uwu5NXklUIImebBIwGpTemDs_j-r0o8d9uzg1X3w5uEa0xCQlWaaBeBdhbs9KPHqk5d7JH6I8ZpePcnflwdO2m_kcN43BBhf62Ej8rKmp0qO13y8jWK-J9qGoMxOsFw7W9Exh3Th6TMhhLFKDT0WWrFkgyPSHrviafjC4XzfJeOahdsJukeKbda09MsSKKgxUAsALCmszC64_YSqE9IlXWWVvphfOFAwNBBKYheKKQFUnxIZbEgewtNEfZ-2-Bp46fr--OHFbCdXDPvGEJbyHOFhet_YNm34TLNwWW8_7EJNdsESfE-rcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=FNK2iOnM5imgPi1xnrU_lAXF7N7YaWf-Uwu5NXklUIImebBIwGpTemDs_j-r0o8d9uzg1X3w5uEa0xCQlWaaBeBdhbs9KPHqk5d7JH6I8ZpePcnflwdO2m_kcN43BBhf62Ej8rKmp0qO13y8jWK-J9qGoMxOsFw7W9Exh3Th6TMhhLFKDT0WWrFkgyPSHrviafjC4XzfJeOahdsJukeKbda09MsSKKgxUAsALCmszC64_YSqE9IlXWWVvphfOFAwNBBKYheKKQFUnxIZbEgewtNEfZ-2-Bp46fr--OHFbCdXDPvGEJbyHOFhet_YNm34TLNwWW8_7EJNdsESfE-rcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCDx0dw3bItDazb2JvpzZjT7yZHx-bE75MKkj1RA9NuFNMtV2WgUbnOWcbPib5ZMrkYRndeMkWzZrDGKNDU9ro_4dHh_1ZYGE_X6B5PCBTi0ohH0_WhUFm8tmbs6MgWOYxcw0EbIP0BzpWG3DwmtVeo-o-kYyYGZ2QFo1qpveRsbPuWsRx6nrjcnnEr0NXyXyQ6z3UdVddWiS3l6D8v2IjCoor6_2sorh7I3LoH9AyXjh3iVnVQqRiEcFnURqJTmNuKFhAd0obM0uuZajDweUow-DfYn4aNwBGdBTb_bbb1B31Y_LLABwssNgDpwKMoyWWbcVGFSHGUjobE5ygz7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzQYlobDgwx1JKpSc9876ljXuPlUE4pGuuU_B20IQutDy-JXm_y9Hq8z8aMLZ2AQRLXBsuJRZKAuN3OjZTgy87nh4yhhNAh7WAVm66mHMDSssAI3LxsIQsPiGebCjdkFaVaTg150ow-d_HlY0PiV7ECH99yc_PLBZGlsWLmnC0v7Nc7MTNpVCm_oxMH5UuX__UnmKw0qHDyfzByBh_lVGbqvN0-roc_zhf5cTt3JsH12asUL_m4AmvygnX59-R_J0JMLS3vhRK3J_o-vu2X6gO-tnOtrxkr9xFB3lYx2mq4NyeqY7gBA5r48f4yFkhSmsDDCF5Ws3QGsjIIghjWWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=LEl3y7YSYhO58v9v7VmGfwVuaJSwCqwoiacP6IA8K2Q0sSVOa6G-PyHRVI5M4uEZ6aCHDcW4kmHZx_aoedmb8K0Yy-WZx3zil9Yu4yMVGSsUL22tZhiQ2htT1ZWZfFieLUtoofb359AHN5aEXGQNi9W10AAKxyud_gqw2BRd2Hn5Tu1BccM0HY0OW3qwthEC_mBt5P6wxC-_YRExtNI9e_bNKiPrKEYTzhxnVAUPAPT6Y9uQdxc2QJyFLkNDY2xZxxbQDFHYoUAk9fUco67vbfdamNl-AuVCVWsoRyE5euOpdoG8Zw5SvJ2-hMFJp9s0gmB-SD3RRklIpMJb-vgNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=LEl3y7YSYhO58v9v7VmGfwVuaJSwCqwoiacP6IA8K2Q0sSVOa6G-PyHRVI5M4uEZ6aCHDcW4kmHZx_aoedmb8K0Yy-WZx3zil9Yu4yMVGSsUL22tZhiQ2htT1ZWZfFieLUtoofb359AHN5aEXGQNi9W10AAKxyud_gqw2BRd2Hn5Tu1BccM0HY0OW3qwthEC_mBt5P6wxC-_YRExtNI9e_bNKiPrKEYTzhxnVAUPAPT6Y9uQdxc2QJyFLkNDY2xZxxbQDFHYoUAk9fUco67vbfdamNl-AuVCVWsoRyE5euOpdoG8Zw5SvJ2-hMFJp9s0gmB-SD3RRklIpMJb-vgNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=QvcxJUDWlUL0LO3d4DgmYdO-5TCGToID6SgDVcTCohdDjphZL6iIT6pzQmAlxs6WYqjptjnFG5IT-Hz5KVpUiEQVWuRp6XAqE4VHeGgW9vBnDqL_RtCi1jCZwZBs-XgtT6wSvfdJ3T2hwfUWH25vK4_njOKnNISO1j1Tjz_WVm3KDEmYPBE9rzafY66oiHdyZl38N9UHr4uC7qUWqEzSts1UL99xflORkacYhNopJ1EzWHQPpG9Jqf8hePDmWQdaXbTbEX70yMvvGC3003O8NzDo43JFv1a-uabWOF9Rylrt8aE8QCreySDr2m1rcGLlriOyYEgpQVRrDgDIGYibuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=QvcxJUDWlUL0LO3d4DgmYdO-5TCGToID6SgDVcTCohdDjphZL6iIT6pzQmAlxs6WYqjptjnFG5IT-Hz5KVpUiEQVWuRp6XAqE4VHeGgW9vBnDqL_RtCi1jCZwZBs-XgtT6wSvfdJ3T2hwfUWH25vK4_njOKnNISO1j1Tjz_WVm3KDEmYPBE9rzafY66oiHdyZl38N9UHr4uC7qUWqEzSts1UL99xflORkacYhNopJ1EzWHQPpG9Jqf8hePDmWQdaXbTbEX70yMvvGC3003O8NzDo43JFv1a-uabWOF9Rylrt8aE8QCreySDr2m1rcGLlriOyYEgpQVRrDgDIGYibuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=cuzcqvwM7Vjqw7ir-ZhriZ7Ft2Jc6Z5wSSHA8f43myz1Z75b3xNrEV-PV9aJmxmepdpU10UstES-CKh87s-2fX7U_hhOQ2Y7QnoV-2n7QIvqxLmhn65LlBthc49MrJsNkG-jw_t7Tw8H3UrPd7M4AMCrfuUBG5LPBVJ1qtZ7PPR_ON03I3Z6iLt4zr9XYbX78blR6FVfUXDrKqAugCvibGu1zxZPatjyHQtaYCGwuFLnYHit6gQ8NiAq1dOW0oHH71c_1uPtrfIcGJPR8dU5PQCrYbqWMLDeXX8oJ3VTv_IrXeamFtBnc3ljglAC7PpZ16vENeYcXh3nn5usjJIPyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=cuzcqvwM7Vjqw7ir-ZhriZ7Ft2Jc6Z5wSSHA8f43myz1Z75b3xNrEV-PV9aJmxmepdpU10UstES-CKh87s-2fX7U_hhOQ2Y7QnoV-2n7QIvqxLmhn65LlBthc49MrJsNkG-jw_t7Tw8H3UrPd7M4AMCrfuUBG5LPBVJ1qtZ7PPR_ON03I3Z6iLt4zr9XYbX78blR6FVfUXDrKqAugCvibGu1zxZPatjyHQtaYCGwuFLnYHit6gQ8NiAq1dOW0oHH71c_1uPtrfIcGJPR8dU5PQCrYbqWMLDeXX8oJ3VTv_IrXeamFtBnc3ljglAC7PpZ16vENeYcXh3nn5usjJIPyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu0zn3pLEqIlwxtRSSc5vb028SxpkpGrS0xG6iPuvbwiaKp1vM7tZs2yBAl0bS5zSrtT-gBh5cmCJkLppn50U6qEEmyZWS13krCi1YX8-_CZisMW1Q7X4s2E9cPOuEK7XbTaJjg3NFzh6r5SuIqAw1zBaKCNWzOIo-ZKlOAjVQ5KzCIz7yHg485MdrbJWm3tvYLYf5hcBuN78l82hsDxGviZf1dLBDNLLwnZuic7V5P0DbodjGEO11rKfZF3q8Z6nb64bnfDoTITM1qRbaWhPSjfdPJ8qJVapldKwYM9tphYqRH3_71qDSx6pzRPp0lFz8rOsvSgjdtzTQfmhK0NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QmY_sPTQ_fXT4pjnwbCevpLkOUYPAJwDOl559PTNpBl9nJaDQcI5kPT6b5UgPqQhDBSHu09y9_cAA0FoXiV_C-xt9k_2dYLiRSO1W2tR4DT-evxqCmlcmGC37SmzI6EEmKCG0hnMd_mS5-jFQVLnwgR_NWc5Js8sxidODIKO5Z1mI21XAF3EfLAfXLRcWdV235M-g75G_svYOymtLIogWpflVLUJIUe8Okgg6X9X5McA2U1GICLhSQI70rfOQeWm5BOdu6-R2sUHYPBhqwEFhoHTRaqCVPvr3ABVyMKFyAHImQLMNUxZPH9CoN2H5JGKzNJMdKCSbk1K11iqtCrS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QmY_sPTQ_fXT4pjnwbCevpLkOUYPAJwDOl559PTNpBl9nJaDQcI5kPT6b5UgPqQhDBSHu09y9_cAA0FoXiV_C-xt9k_2dYLiRSO1W2tR4DT-evxqCmlcmGC37SmzI6EEmKCG0hnMd_mS5-jFQVLnwgR_NWc5Js8sxidODIKO5Z1mI21XAF3EfLAfXLRcWdV235M-g75G_svYOymtLIogWpflVLUJIUe8Okgg6X9X5McA2U1GICLhSQI70rfOQeWm5BOdu6-R2sUHYPBhqwEFhoHTRaqCVPvr3ABVyMKFyAHImQLMNUxZPH9CoN2H5JGKzNJMdKCSbk1K11iqtCrS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=gaX9kmIyeo_WM6IGe2BdR-9uFHBE4avHHrQKQNxbBOQewNw3pH57NIJ8Z7V05uq-UsZ5mCpAY-MmIdoA3jDrr_3Vt8y5MCt_eeTdhNM-hSyXlTkAr7X1Y6CceFWPwyv-IdXMD-nN8ZmwXHwI56bmhOlHmNQuuL4w0-GfSUM9Em1My1vw7CVK8jN08ClmqVazmjXE30HApLnJx1mbW6EFJksyl04xmB8kkomMZUM5p6lzzm8YHZi3e41YxWnUKpgYQr4BP0O-IgB2k3aWgf08YLTB8Q9nZ_jEasbk6kCRAviBp7EmrPm-GHHb_vjF5UCFfZDwTAD1N8e7xkgPpS0xkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=gaX9kmIyeo_WM6IGe2BdR-9uFHBE4avHHrQKQNxbBOQewNw3pH57NIJ8Z7V05uq-UsZ5mCpAY-MmIdoA3jDrr_3Vt8y5MCt_eeTdhNM-hSyXlTkAr7X1Y6CceFWPwyv-IdXMD-nN8ZmwXHwI56bmhOlHmNQuuL4w0-GfSUM9Em1My1vw7CVK8jN08ClmqVazmjXE30HApLnJx1mbW6EFJksyl04xmB8kkomMZUM5p6lzzm8YHZi3e41YxWnUKpgYQr4BP0O-IgB2k3aWgf08YLTB8Q9nZ_jEasbk6kCRAviBp7EmrPm-GHHb_vjF5UCFfZDwTAD1N8e7xkgPpS0xkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=NYgV6M2pdfmZpQbjDnCeIQJD1YGEzinz_CPW0u3PfH68LGZGM9ghBI1O7_-0Fba24027388qUGR83KcmyY96sBQRSvcjjN8hDDW4_EHzRf-AFXzaFErd8IJGxofVSnxyEYummjD6rOhsfq7dN4OxM2GJ_iU7mNVKvFDfvXE-1jE-NWAqp5nyryFG8uCGdWRs2Dcv9Rvum1bj53awBAAtTGGZ-kC3rPcETTtnk7zWk7xjrstzTSTTqDAH9Z0AmW_0NPqlgOaFXQRhov4Fn2DsqtXFpeB1UMRZbVymHFv2l_dHZvlUyyjpZN1nOreT31KUxLEAuqSviQLsRcHDWpTPIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=NYgV6M2pdfmZpQbjDnCeIQJD1YGEzinz_CPW0u3PfH68LGZGM9ghBI1O7_-0Fba24027388qUGR83KcmyY96sBQRSvcjjN8hDDW4_EHzRf-AFXzaFErd8IJGxofVSnxyEYummjD6rOhsfq7dN4OxM2GJ_iU7mNVKvFDfvXE-1jE-NWAqp5nyryFG8uCGdWRs2Dcv9Rvum1bj53awBAAtTGGZ-kC3rPcETTtnk7zWk7xjrstzTSTTqDAH9Z0AmW_0NPqlgOaFXQRhov4Fn2DsqtXFpeB1UMRZbVymHFv2l_dHZvlUyyjpZN1nOreT31KUxLEAuqSviQLsRcHDWpTPIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=PjAqpNrxSYy4v6YfM-shJyol8p0AHZpbCB4zDvcVK7zjBSiJhoeIufKyJh20OFIrbsxUwZJlmLqCetPPug_-81_SuOzGyuM60M5l_AIYRXMZE3F0UNpba4fkst-6EbacJJPImTlpVcy5I84dxrfsJbhcBx-Wrn9PIOfQgmBw7EYiTJXSemUMwFO2_g9CM0BYBoAEuc1LZgIxnyEAm4ftUXxY7kj0fbmT7qGxxC9k8G9dPUuPZymFwB7TmhCoUuxsEDzYJBeJurHfFh_yP0G-g7fGJQIut98fqCZ2maWiLANkblSWdsdKLzDaai-rxDasHanzTNfMbBiQESRpFotDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=PjAqpNrxSYy4v6YfM-shJyol8p0AHZpbCB4zDvcVK7zjBSiJhoeIufKyJh20OFIrbsxUwZJlmLqCetPPug_-81_SuOzGyuM60M5l_AIYRXMZE3F0UNpba4fkst-6EbacJJPImTlpVcy5I84dxrfsJbhcBx-Wrn9PIOfQgmBw7EYiTJXSemUMwFO2_g9CM0BYBoAEuc1LZgIxnyEAm4ftUXxY7kj0fbmT7qGxxC9k8G9dPUuPZymFwB7TmhCoUuxsEDzYJBeJurHfFh_yP0G-g7fGJQIut98fqCZ2maWiLANkblSWdsdKLzDaai-rxDasHanzTNfMbBiQESRpFotDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=TJTm133lYRmetZCDXXbzQkAgmDBA8GT4J8o3Fk9Da_osHtA0UzNEenRtaGW80oXDNaRv6AZK7t0ntJiRgW5TPzLz4r3tSMImhP1OE4L8FtGKR1RNB9RaSKi1wTIZUI5N8w3TGMTnCWAFZn0Y8JyR2JDXrWieWzKGUjU62PMNJwLC2YntGzrZC--oRAPWWIAyXuGrcIglpvyxhEjtUP1p_1ZkCUtlV_Srb8P3TFQLs2wlRai-wKBoeiV5W-dmqgzfxq_tcjpt172gW0ULk72So9ExJ8_6r4WIJBVjDr3i0Ih3_TR5pyLooIYhiCdeli_c0vpCdLr4BMZB18yp1WJyhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=TJTm133lYRmetZCDXXbzQkAgmDBA8GT4J8o3Fk9Da_osHtA0UzNEenRtaGW80oXDNaRv6AZK7t0ntJiRgW5TPzLz4r3tSMImhP1OE4L8FtGKR1RNB9RaSKi1wTIZUI5N8w3TGMTnCWAFZn0Y8JyR2JDXrWieWzKGUjU62PMNJwLC2YntGzrZC--oRAPWWIAyXuGrcIglpvyxhEjtUP1p_1ZkCUtlV_Srb8P3TFQLs2wlRai-wKBoeiV5W-dmqgzfxq_tcjpt172gW0ULk72So9ExJ8_6r4WIJBVjDr3i0Ih3_TR5pyLooIYhiCdeli_c0vpCdLr4BMZB18yp1WJyhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=YNLQXgCde1WxanoZbwwItXA0FytQG9KRUOxAxLEuoD6A9ghz_rDAXlRhm_yvtsdWppJeGx61FO7xCbAjHmydMOndOK1Yhi3VAx56601rAi-DUkYQVUC98RzrgLPkNQ9j0Enx9_kFk9Rk_BOsyep0lXse56dNtfrL3hKXHIPhgJz2bajPV8sPnRy0zGwArcR1Csg5QopjzGXcgCJOScPrVOiV_XqY9ickkvty5pn2AGOsMegbVCDByF7EjDlHaERYj9867YkPAa9oRQxDX-q2ICDRNkQwkyyDFpx-6YOKK2vTZhjUvmApsor9uZR1f70rb-cNa9_vZQDSBAWckbI9H7lyqe3WIEjcottz4OXvV69xvH8h1kcN3Ld8qOUplEzN5JJQetJs9dWEm0Rv6rYmtN2Vkr9tOLjp_GD2mq5rqXvqqst8TM16ZSDlXQfQcVQlo0NfY1rV_uFYzoH790oXRbgRI_csXJYdPTo2KKLho29TmqVtLLHX9NVwBFr55YktaKyUBUpNeQPXJZFek-GECyiDLJ71swGP0HfeZ_2wqQvtW8P33zhkuc2zGdfD0QvMHxO7Bo1soaFcgRJ7NIrSxckO_Ezw4WAPU5Se0foyuP14DL7tkzUv9CSswerKUEUuS9iU-4pTOG6Tw9hH2k3SmHOXHpo5XgNaV5cDW-qakQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=YNLQXgCde1WxanoZbwwItXA0FytQG9KRUOxAxLEuoD6A9ghz_rDAXlRhm_yvtsdWppJeGx61FO7xCbAjHmydMOndOK1Yhi3VAx56601rAi-DUkYQVUC98RzrgLPkNQ9j0Enx9_kFk9Rk_BOsyep0lXse56dNtfrL3hKXHIPhgJz2bajPV8sPnRy0zGwArcR1Csg5QopjzGXcgCJOScPrVOiV_XqY9ickkvty5pn2AGOsMegbVCDByF7EjDlHaERYj9867YkPAa9oRQxDX-q2ICDRNkQwkyyDFpx-6YOKK2vTZhjUvmApsor9uZR1f70rb-cNa9_vZQDSBAWckbI9H7lyqe3WIEjcottz4OXvV69xvH8h1kcN3Ld8qOUplEzN5JJQetJs9dWEm0Rv6rYmtN2Vkr9tOLjp_GD2mq5rqXvqqst8TM16ZSDlXQfQcVQlo0NfY1rV_uFYzoH790oXRbgRI_csXJYdPTo2KKLho29TmqVtLLHX9NVwBFr55YktaKyUBUpNeQPXJZFek-GECyiDLJ71swGP0HfeZ_2wqQvtW8P33zhkuc2zGdfD0QvMHxO7Bo1soaFcgRJ7NIrSxckO_Ezw4WAPU5Se0foyuP14DL7tkzUv9CSswerKUEUuS9iU-4pTOG6Tw9hH2k3SmHOXHpo5XgNaV5cDW-qakQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAKz5rf98OApvz7Ty6at0de03ESItvDplshIY23FM6qmnGm9WOndRmGqHpD2ZSB4p5wJMoFtTly6p14C3hPAdSZNcJu05ZZebhm4iKlAtQ53FqoYT90FlyaxwTTsMqvx_4TzRTuvofLEhnoPxXkvvtnUcSBzyjfTHi2DHrvB4qte0uKviDOHqSieGJLOFjwt0z32tvrlyNYzdwny92sQbQjiJwvF3xFCvyIM2TqqZZlSxSAe6NhT_jy4x2dX-94QdXSVLTsGdZEYlq7kV_rOF8EPY5OJGeH5eSv7FYT35HGFwINACzF9YH_lYJGAcv4hivG9Gd9fvQXm8p37NKD6Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QkvwAzlqoo5hd_qcZT5qehKlgh36IwZPIkaqS_D875wvMBe87lOVQ9r1-zXeMkVcU_TeYMuL569nCPTTZbZ8E1AABzxXjx1KeE9vAGzjdpNTKEiJOgrTsFFM9XHPCirQYVXK4KANB-enCnKUO3YnGnB-fDV_JKvNfc6pz4x8iBfHB4b98YDVIetcv0NuOE9sPueRzrYqnexfr4OSMV3GhQD5aY5i7bq4BongtGxPZudYGCyQWd7RZgf5mb6uKCLNL9-2cnVmbGDBn6-kq52oMwLnCQbFq9xERKGWLPB0uS0B4JUFJS-3jObjD66AJMhEIhzxJaDhq89pSqAFTu-TzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuPjk4IYi1salevmxZlh1yyXp-ixmr5wfYfcOf-Q6dgjQhwvYRv8uqTwjuNvBOavkykqbwYfqkU73jd03s3K_NhtOkJ49-N01YJBBQYt_DfqXyQPd4W-BKL8qlROV3jhLECbEMx5-qGMhAZ3P1qkANrtqBP4vyYEb4FFCBxfhJK9Xl1pvYJXh2lxqDRFKRMuy4-Of14s-vwVX0zRO4Z6yvees5VzerPpMbMx_1POG0FVn8ixir7uvfU7h-1ZDOZLRgmc9uRuQV2qFf4i4xW_x-I6nqC3J3JNldRDTuTEjC_8OgfdGnayDPqpytMNbO_pF-hkpelw6UbUzXnF8128bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=kGrnkjpNJAjrnK5ZYL7ufpmfpNEbUMq6KMPEbPoud-LvY_q8e0D7Yz-PCpI80m1qRSnvMu3BFEDtucfJdtTNSBgn9WN_924GHQqE8-5U-_wgecqiF-IwrcdD4Um-gl7muGIh3PyptJnXLwgJNnc9yO67ngLxcgPMhOWHGlk2_OMYxDREavLUHwhdLscVX4R8eOuCuRRj6TT2057SMmfuqp0d7PTH6PLw1I3KbsI-medPVtRAeLor5lLXBwhVdAHYVLziVNWnnBlS6Nsx1P7soxw-Gk1hE9WuRoDyJjHa87hC1FfwejJxUmbkxdTOVEnEgE-IPo89mYA-mA-VObE-aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=kGrnkjpNJAjrnK5ZYL7ufpmfpNEbUMq6KMPEbPoud-LvY_q8e0D7Yz-PCpI80m1qRSnvMu3BFEDtucfJdtTNSBgn9WN_924GHQqE8-5U-_wgecqiF-IwrcdD4Um-gl7muGIh3PyptJnXLwgJNnc9yO67ngLxcgPMhOWHGlk2_OMYxDREavLUHwhdLscVX4R8eOuCuRRj6TT2057SMmfuqp0d7PTH6PLw1I3KbsI-medPVtRAeLor5lLXBwhVdAHYVLziVNWnnBlS6Nsx1P7soxw-Gk1hE9WuRoDyJjHa87hC1FfwejJxUmbkxdTOVEnEgE-IPo89mYA-mA-VObE-aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=fRnHKI9wtfVzCOR5wCLbXTN6h8ni-AjjqHqT6pu5UE5poSHoUfJj1w_JkFevS4tpF7qxJwnQ_fID2oeStWyb56uN1O1rWuI2d5mbgCcjnGQqzBsSqXLOxFnFeAjyHbovsmGRLHnnfYiKhvcmpd9wjD4lthMaJCqx_ETGi80J05iHogDx_7PdpJO9l38nvW8MguTs8yuiSKCPto-6ZudkBsBWKoyvojlIMbnqaTVhehXVwz6bJZDdKeUOVJ0RQE-T7fB_heez1-wT58kVAYBQTNKwRih-UGSKGoeG6V0bXHXtHpQm-9dD5kpdO1xGenocUhiiG-iQvx7Y-hO9Ecm0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=fRnHKI9wtfVzCOR5wCLbXTN6h8ni-AjjqHqT6pu5UE5poSHoUfJj1w_JkFevS4tpF7qxJwnQ_fID2oeStWyb56uN1O1rWuI2d5mbgCcjnGQqzBsSqXLOxFnFeAjyHbovsmGRLHnnfYiKhvcmpd9wjD4lthMaJCqx_ETGi80J05iHogDx_7PdpJO9l38nvW8MguTs8yuiSKCPto-6ZudkBsBWKoyvojlIMbnqaTVhehXVwz6bJZDdKeUOVJ0RQE-T7fB_heez1-wT58kVAYBQTNKwRih-UGSKGoeG6V0bXHXtHpQm-9dD5kpdO1xGenocUhiiG-iQvx7Y-hO9Ecm0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=RlYuL4DRX90TOcuQRBfVqyh4cf0Ija2hP9Sebnf2zu-8gp2lbGurE8LuJCyPR08vsZARIX30fpn5dVj97fsSp7Ceu01DXoYXUHJkoBhJfWqLC0PAg6awoAbVExWrfsbuLJl8wa_luJlRLzEPdaWnr9eMzlZMjQyrAD0CPltdFxEosUlXFJglNpJ1zCsrTfG7uIm7ClQrJMQK-TuUsVD8peWQHqJX1IUCGwsCL_81ltI2dB4nK2ya_TWNjqV5BnngbtVjT7PYQFJrCyklbkMzobailcYMdXcnIL60a829BfB2g1uD0LPB8JjXcZgH4EuLPxiFa9TnBP4GL9l1i4a58DgoCXykbqp8tS9XjJ3Yp776NgOzDtpZvLUBW2bP6C2uUIgRbfUw1rPJ5mTs8fa8vXMw18dPXquAV8G7Bms6AyqBBFmnR0PKlZeZPEa4TWnyx5fUyVmBDy2EfRmAsqYDYWt997f6FDONuh9bXTOaKExnjWph4VY_UZnWAKQNlTQm2kg_n1C1TBlIF_863TWQAqoh2ZVTAl-BrfprLEip5YdL4uIiW2zGu5wLAxoE8D2efhWZQTfAiBX1mE36XCY7jbtWcyPBp6toTc6yLGAIW-LMa4E-j6V-WN982XmplD1ACzTBvy_KkrOpoOXMtV5O4fc0rsLrmuVc1yt70JnGmJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=RlYuL4DRX90TOcuQRBfVqyh4cf0Ija2hP9Sebnf2zu-8gp2lbGurE8LuJCyPR08vsZARIX30fpn5dVj97fsSp7Ceu01DXoYXUHJkoBhJfWqLC0PAg6awoAbVExWrfsbuLJl8wa_luJlRLzEPdaWnr9eMzlZMjQyrAD0CPltdFxEosUlXFJglNpJ1zCsrTfG7uIm7ClQrJMQK-TuUsVD8peWQHqJX1IUCGwsCL_81ltI2dB4nK2ya_TWNjqV5BnngbtVjT7PYQFJrCyklbkMzobailcYMdXcnIL60a829BfB2g1uD0LPB8JjXcZgH4EuLPxiFa9TnBP4GL9l1i4a58DgoCXykbqp8tS9XjJ3Yp776NgOzDtpZvLUBW2bP6C2uUIgRbfUw1rPJ5mTs8fa8vXMw18dPXquAV8G7Bms6AyqBBFmnR0PKlZeZPEa4TWnyx5fUyVmBDy2EfRmAsqYDYWt997f6FDONuh9bXTOaKExnjWph4VY_UZnWAKQNlTQm2kg_n1C1TBlIF_863TWQAqoh2ZVTAl-BrfprLEip5YdL4uIiW2zGu5wLAxoE8D2efhWZQTfAiBX1mE36XCY7jbtWcyPBp6toTc6yLGAIW-LMa4E-j6V-WN982XmplD1ACzTBvy_KkrOpoOXMtV5O4fc0rsLrmuVc1yt70JnGmJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZzUR1cZx4v-ZZOICba610CVLUemMk1efnx-4TOVdiNm-oCl01coHubB-F658sXT9VdFurL9uKPDTkJ1Q4ATNT1exOuZ8-ziQTAzNZe_6Nju7a3mBSO3VUK70vUyg_rFsiNHUlXWfONUQimSw7VM8yoCi3fYG-r_q0vSbOotdIludaiaQ2lLgT8MRX1JByMCGsOPBSBbH90luNaU8RwmmxBeYpCTp2AXdW3tx-PKj_TnZigTbjfk8vlBAaF7TAzh1-0rl4iPGIvj0PUb_EP0q-VLWIZk2J94qHKYm-wV5-Cn-LeajO2pojx3Tu5SYa8KEJiCnrry_XvCB23SUyA6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=k3xvFnMVqE-Y0RYuTXFkRNa6RSaRtmysxBwpBVdGgCm2JRIKT3580TLcT2U7TS2eQ6Z-O1U2RpejtQa1n4c9BN8VJ2ZabKnl5pd7bACGR4cfauz-XiZK2EQsDzUMD3aCncEF0zm1U3tV00ltR-XhCORfmJzvD1apCd6bhhq0o_pSkZqwC3Ievy8ARrxbK7N35WmrqKyF1ohUazwP_pmSyCd6xUBfelKHDiBeqG1us-1jwqTeXAIdTBua1AZOl-v2Kox9atGdaCApbjTgmS-L1qYXjBbKSOZrhXgzuj5rhx5CXcxk77GW3vMDnVG9N-fpPUKZzmaz2zJJKz_4DWx1ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=k3xvFnMVqE-Y0RYuTXFkRNa6RSaRtmysxBwpBVdGgCm2JRIKT3580TLcT2U7TS2eQ6Z-O1U2RpejtQa1n4c9BN8VJ2ZabKnl5pd7bACGR4cfauz-XiZK2EQsDzUMD3aCncEF0zm1U3tV00ltR-XhCORfmJzvD1apCd6bhhq0o_pSkZqwC3Ievy8ARrxbK7N35WmrqKyF1ohUazwP_pmSyCd6xUBfelKHDiBeqG1us-1jwqTeXAIdTBua1AZOl-v2Kox9atGdaCApbjTgmS-L1qYXjBbKSOZrhXgzuj5rhx5CXcxk77GW3vMDnVG9N-fpPUKZzmaz2zJJKz_4DWx1ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=kg734_8VMdEp3NrJF_4bXy0mMR1a1I6Os1wQtDa_nxhDDi7mfDKTBJTShLLEohRJAGcNge3MQ1yPiYY-LFOYmQh1xlNU10-d49r1Ti7D0Xg0bN-MXqABLePJPtWbGpxl1TA3ht5IqXa8JqgNx3Lr4WVyB_MxuD_bFZc0GjLhzyNFZIUhF5gtc2Parky4VLmAlS74nsyXpvPAPHpFrpDjlqDDo6SkVnVYAqNyJSW-Sradwo7EhR7e16M9c6BchsGvAcF6dypAX004GulxsUVcxjNb9HZLbMwNlDID8X5yaFEM_8q65HGHZPRB3ckWB5P3xjq_wkjKOrI8FIoIrfgKDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=kg734_8VMdEp3NrJF_4bXy0mMR1a1I6Os1wQtDa_nxhDDi7mfDKTBJTShLLEohRJAGcNge3MQ1yPiYY-LFOYmQh1xlNU10-d49r1Ti7D0Xg0bN-MXqABLePJPtWbGpxl1TA3ht5IqXa8JqgNx3Lr4WVyB_MxuD_bFZc0GjLhzyNFZIUhF5gtc2Parky4VLmAlS74nsyXpvPAPHpFrpDjlqDDo6SkVnVYAqNyJSW-Sradwo7EhR7e16M9c6BchsGvAcF6dypAX004GulxsUVcxjNb9HZLbMwNlDID8X5yaFEM_8q65HGHZPRB3ckWB5P3xjq_wkjKOrI8FIoIrfgKDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=wBJL4GibUmJj0YrIQBd1QQmgarfgNoNo4jv_otnlrrIYuO90Q9sq_rVHoY6OVnafOlYbbGbnfqXL7yrmrmvRiHN7wG5o6oPVXgX0Pr878iGOlYRM4DuHfbOOHs_13Czz4LpzNXKuljGa16iXouc1Vio_OIsrvuR4m_qUZA-YEAAT5Ejm3VImE732mWLTUKjp8Y4zZkm86fQ3tofcLGYuzvLsxy6RqtRrkQjfYkWGNgA3O1gNDC9MlK6dJRyXS2aiNs7DJbrMQb_mE_TyUqA54UjTfRofJuWeb9ndOMAWkt_jp0RlVyGUX8MlSFOsxCHJOrPImCzgoQJmgT_XUUGSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=wBJL4GibUmJj0YrIQBd1QQmgarfgNoNo4jv_otnlrrIYuO90Q9sq_rVHoY6OVnafOlYbbGbnfqXL7yrmrmvRiHN7wG5o6oPVXgX0Pr878iGOlYRM4DuHfbOOHs_13Czz4LpzNXKuljGa16iXouc1Vio_OIsrvuR4m_qUZA-YEAAT5Ejm3VImE732mWLTUKjp8Y4zZkm86fQ3tofcLGYuzvLsxy6RqtRrkQjfYkWGNgA3O1gNDC9MlK6dJRyXS2aiNs7DJbrMQb_mE_TyUqA54UjTfRofJuWeb9ndOMAWkt_jp0RlVyGUX8MlSFOsxCHJOrPImCzgoQJmgT_XUUGSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skfhn7DcumsFpd4Q2E3v-RIsW0AVrh0txRkAnvpHWpTVI8qk4cUhMUYcgbrPgT19mAYVNzdVKtQCfjO2nUQVz8wQnRDM0OpCI7bVYuPAdQ-Q4A3CMAtW0uhtJqXQsqaU6PMOaLIHxNKLTcG8pHAU0XjAon8I5Cs9-uxRU2NiaEQBLFR2wOVBJABC9rGgf7dFZEFKa5Vzn-GsKCcFPXcyL7-LbdIu6Cssd7W7LgsiWIWQLBMERh4ONCC-5Sm5NmrYt3N_rSNZ60WdDxSMD255QEXWUW6QAUmP20cH1JRkEn8AUQTAJdfasperxhA07cvdCVEfTrlDlFMcRdTXHDyTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=eU3tCLNzoLVnVgwc56ZO_wKgLshji5YChrPHwRckdqQ2mbUMKf6gvjsg0rDnoB7upwkuRF1tgzwAFNi9GVS3k-S4Jky1ejkymdN12LkHmlRhAHj78h7YqN9XWMHbhr6KWFpzyZYJRdvL_ZC8xJ_9JV72mHf2aL5LxtExCIpGvT0h_bR3w2bL_k_JMWqinYmxKfeeVGkVO6BMWYX__yr5zPlk-CUF_E36XhQXRMqATd748XAM-46b4Yo59jfcc2eA3pb8hiwJIsFOTbFt-XOAepP3tFVvGlTIiMBbWv4UuqTWSqGErKG7U0HEiNOQn7Rr0hbCY1I7-u6spPBlE38_xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=eU3tCLNzoLVnVgwc56ZO_wKgLshji5YChrPHwRckdqQ2mbUMKf6gvjsg0rDnoB7upwkuRF1tgzwAFNi9GVS3k-S4Jky1ejkymdN12LkHmlRhAHj78h7YqN9XWMHbhr6KWFpzyZYJRdvL_ZC8xJ_9JV72mHf2aL5LxtExCIpGvT0h_bR3w2bL_k_JMWqinYmxKfeeVGkVO6BMWYX__yr5zPlk-CUF_E36XhQXRMqATd748XAM-46b4Yo59jfcc2eA3pb8hiwJIsFOTbFt-XOAepP3tFVvGlTIiMBbWv4UuqTWSqGErKG7U0HEiNOQn7Rr0hbCY1I7-u6spPBlE38_xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=BCXhj-MnXb6OmzPxpl6NmyU_Ncs3rupaGm5AM76Rr7cnJ6WJoDUs2dVdj9PiT6GOMBGXbJGOGT8YZkLha6A8fRAD_0ibXxghO_T3GicI5iYyB3ZYrdTdTLJdCE8Xd4omCXQBclMEybmplBT9IqYsih8hQ24mK8TAFgnEhWBSks1mEWc1mV8LBPoDq_TREyV-KACpod3ZSasClz52aqzr0RCeZVlQvFnr5NMlWmutXmW8Wp17a1vTt7EsBMysbFjR0AWCBNijP_MgxmdLjZOvNfpJ6fnbpc5HvqwdTf-771aStbZAwmd17ncU-oZfLP6t3HxXovOUkeh35P7K9y3Dww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=BCXhj-MnXb6OmzPxpl6NmyU_Ncs3rupaGm5AM76Rr7cnJ6WJoDUs2dVdj9PiT6GOMBGXbJGOGT8YZkLha6A8fRAD_0ibXxghO_T3GicI5iYyB3ZYrdTdTLJdCE8Xd4omCXQBclMEybmplBT9IqYsih8hQ24mK8TAFgnEhWBSks1mEWc1mV8LBPoDq_TREyV-KACpod3ZSasClz52aqzr0RCeZVlQvFnr5NMlWmutXmW8Wp17a1vTt7EsBMysbFjR0AWCBNijP_MgxmdLjZOvNfpJ6fnbpc5HvqwdTf-771aStbZAwmd17ncU-oZfLP6t3HxXovOUkeh35P7K9y3Dww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=X9lp5xRmSaH1UbQd4-l6MuWuwreipoJeEsK36ng04SaOjni4A-a3lcYP7S0TjqIgr2B637pcTWGsEnq29BRoqrg7Ak2avKiL1g0lNAAZTL-Zer8-ys4aeKabOTjFLZHDODmt4x5Kzs7X6HF0K0iRsZrcNSfP8sHFVCLEzMDNcec3Hps6h5aVnhc7S9TPQigImaxzbqWrNe06asbCktRm7rPWICcCDpgI1LMnON5zbaOxrpFiS8O-zT_yu2GKlu8Z_oEkTld4Acib5AY5mC8Y9Vd2bmAXBOocD-CcX006oeLQFZmhKaYoJ7Zqy-5pOFAycRaJFkpAaR-0TBPG8i5tiKBHM41AuYzQaUtUaAXnuJWMNNEWiBxnEDi1bSOmCixoCJGYbWjQKhocWCihbe9GSnkjOrUBQy1gtS56kcQNEhB6piVxADTwCo7oqCMXnLY1lWiyEc9-_4p6VU56uC1gODdqmJNjk62dgJBboIKD0NAi3DtMq31O3ocptep6Mv_rdt-RcPLXqGjuCDEn8s9_Jsq74HMT7kpRop3q3IJAhtAixaiYe-DcHOzf5oQxNjNO-8xkVrKMOhat8_WkOvHpxjnFOsGUi-VyB8hjO2Vip6Bruca_wukrv6nZW7udiuDqRwmzMRH87_xezs5-k5pCYFizWtXYXMpPp0mcTpt9kv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=X9lp5xRmSaH1UbQd4-l6MuWuwreipoJeEsK36ng04SaOjni4A-a3lcYP7S0TjqIgr2B637pcTWGsEnq29BRoqrg7Ak2avKiL1g0lNAAZTL-Zer8-ys4aeKabOTjFLZHDODmt4x5Kzs7X6HF0K0iRsZrcNSfP8sHFVCLEzMDNcec3Hps6h5aVnhc7S9TPQigImaxzbqWrNe06asbCktRm7rPWICcCDpgI1LMnON5zbaOxrpFiS8O-zT_yu2GKlu8Z_oEkTld4Acib5AY5mC8Y9Vd2bmAXBOocD-CcX006oeLQFZmhKaYoJ7Zqy-5pOFAycRaJFkpAaR-0TBPG8i5tiKBHM41AuYzQaUtUaAXnuJWMNNEWiBxnEDi1bSOmCixoCJGYbWjQKhocWCihbe9GSnkjOrUBQy1gtS56kcQNEhB6piVxADTwCo7oqCMXnLY1lWiyEc9-_4p6VU56uC1gODdqmJNjk62dgJBboIKD0NAi3DtMq31O3ocptep6Mv_rdt-RcPLXqGjuCDEn8s9_Jsq74HMT7kpRop3q3IJAhtAixaiYe-DcHOzf5oQxNjNO-8xkVrKMOhat8_WkOvHpxjnFOsGUi-VyB8hjO2Vip6Bruca_wukrv6nZW7udiuDqRwmzMRH87_xezs5-k5pCYFizWtXYXMpPp0mcTpt9kv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=QR0UHfzli_gT-v3BZviQnnBf9iYYCED3nE_QP91DAP-N_Dvyf5vsyeP_2uTwJhuS1gxeC5OtGK8F-v2RSglSAqfdGm266V612JBib7aK5leBN6GjaQA82K095Tzp9aln6OoINLDabNsChCvSQgHm9UY3hifGJs7TVS_-QcFwQnhGYYfV8pyH1_FxkyVRPdAZQUEFZGd_p4SF1DVBibTZe4wYe2RytYQFFBY-H31_e9TdDbBJ3QKsj8Xe7VeR8z3M88FWNwhtWxtdJ01XKKby6wB1IDC6CFOK67j0cJExgjySXdaGY2NG9aQsHrH5MW6PyQWg1wrmkPF___Yby83I9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=QR0UHfzli_gT-v3BZviQnnBf9iYYCED3nE_QP91DAP-N_Dvyf5vsyeP_2uTwJhuS1gxeC5OtGK8F-v2RSglSAqfdGm266V612JBib7aK5leBN6GjaQA82K095Tzp9aln6OoINLDabNsChCvSQgHm9UY3hifGJs7TVS_-QcFwQnhGYYfV8pyH1_FxkyVRPdAZQUEFZGd_p4SF1DVBibTZe4wYe2RytYQFFBY-H31_e9TdDbBJ3QKsj8Xe7VeR8z3M88FWNwhtWxtdJ01XKKby6wB1IDC6CFOK67j0cJExgjySXdaGY2NG9aQsHrH5MW6PyQWg1wrmkPF___Yby83I9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCB5Jy_p5tPig-zy01JZ5Zoe8L_gUeEZFwV6E60fLuyFIMLSZmnxgLQiJQZl-5dKr630-JWna011BVa43HXwYu-3G7WP2ZXZUZYKhVxIfuR7aMhP-x5q9RzwOHME77NIbRQ0A2DxXD3CJR0ZV3ecYVtbQNRTzzP5ur5AMfXHssJ0mzOxtjM12l5dERQSyKTO3vLlHfwfYxYra-Yx7IAThk7dEeFLXajn6aPFNMqwmfiH9gNhq8o4xM9uo-6pBypFTtRhGQAjkZuz2yDZJkRocZX_nBl72hsdC0b3cba1I-SyxonYsK1mNKVh-dWzDy_J1s4Bmb5UNJhFV1u3DccCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=VPh5Ptr2pxO5YqyWY0hI2y_k888hIrb6luBDq-dIWW9Zkq42ZDgzeqERpbxEFGTzuoq7fXqsVutpX-oIVdI4re6YmodHf4DUttMrV22ukYrJ6-2kcAoGnIx2UllfHL4-9HWq620Dlz3UNoQZATeRd59i7K4f8xzniFuR3NMAtQ8caOAiptYgCUS2wJY_hoAei0mBJjn8_I4kyOGmp1D809TlhWUykxrLZq91RegPpEP4ydyRuHvEd-uMwQC988xwyWIGj5UEgRvHxQH_7YOWGkqJODbGQECNRPftML-3CQSduTGDP12XHeFKGF9JOKW-H1EiFeLAByUzziqKdzMxRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=VPh5Ptr2pxO5YqyWY0hI2y_k888hIrb6luBDq-dIWW9Zkq42ZDgzeqERpbxEFGTzuoq7fXqsVutpX-oIVdI4re6YmodHf4DUttMrV22ukYrJ6-2kcAoGnIx2UllfHL4-9HWq620Dlz3UNoQZATeRd59i7K4f8xzniFuR3NMAtQ8caOAiptYgCUS2wJY_hoAei0mBJjn8_I4kyOGmp1D809TlhWUykxrLZq91RegPpEP4ydyRuHvEd-uMwQC988xwyWIGj5UEgRvHxQH_7YOWGkqJODbGQECNRPftML-3CQSduTGDP12XHeFKGF9JOKW-H1EiFeLAByUzziqKdzMxRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=OykR6AxW9VzBQhPgjoLJ9PMS1V87lQSsX61Wp6HS07RjrzeRfli12R1M5llko0_stIvdx0T0OrR2-fUWWLgmvPK8n4dNuIM1WG2YgiK0udOh9KV4k-9yO8AR1J22sMYwtBJvo8gLB0HloOpgOkvZ-GRzrCgOoq1aW_1oDuFATR74paKvcLfvQiD572ELrgGoEXfArc3SutrrQmHWMIjadM10nJdrXs6dLccNGBsMcn92kmi7Ve18A0_0JsIxWeaUnQrgAsWbBLBAav_6plkRdLS-wXguF9w-wA60cn-HALz2UfF1EMIwTlupamlpCD_qMGLvs3a8K_MQx6LQIs7W3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=OykR6AxW9VzBQhPgjoLJ9PMS1V87lQSsX61Wp6HS07RjrzeRfli12R1M5llko0_stIvdx0T0OrR2-fUWWLgmvPK8n4dNuIM1WG2YgiK0udOh9KV4k-9yO8AR1J22sMYwtBJvo8gLB0HloOpgOkvZ-GRzrCgOoq1aW_1oDuFATR74paKvcLfvQiD572ELrgGoEXfArc3SutrrQmHWMIjadM10nJdrXs6dLccNGBsMcn92kmi7Ve18A0_0JsIxWeaUnQrgAsWbBLBAav_6plkRdLS-wXguF9w-wA60cn-HALz2UfF1EMIwTlupamlpCD_qMGLvs3a8K_MQx6LQIs7W3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
