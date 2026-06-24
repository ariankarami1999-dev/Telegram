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
<img src="https://cdn4.telesco.pe/file/gGswR75z_nlH8Ri1Y0wd-o0k0yXvb5PTubho-RQISzmWvPLviyTtBBb0m2OrpMZBgt7DShVwajmQRJC8qrQ-6piwouLvVKOQ1GndH4P96b6dUh3xbmpjJxTHwuTofDaSrrDzA-QONZk-QC4DgZ92o-LB2476E4rYocH_zHo0E1U-uVZg9103qiYpC90E4QKjhThR5fFGp2IplOGN6PeVA_g0jI3itPa1CUxW5wdckzLn-3kUxlaYzcodss7edF-X7KlRKlimdWVxRRyPlF9_1XxQ34RR3mbpMNj1uB2mNoU5pJe4kfs2ElhvSrl7KGXp0Z27Kvvlh9TsEVomYRREbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=BB0_aFOvEXcgPpEDamGZv-L_bvw6gxvJT62vvg9oLbEBss9qoMn-Tm3UgrJXNbmK2H_N4lRgfgd7aVZaJlaay6cn5kHo0c-4b4YUfLElBfIRQSgyxWwYh-_lVPOJfBh1yh2os4Qc1vUKVX2KUbDdZ994rlLRA1mANm97s8xlQY5lI-wY6lwOn6b9bqQ0GeDm9HhzwQUSWOVYHEUo9IWbrMQDfLbCQvozf9aljMjqYtl-pQ_Ymsq9-HHVSQciTYKeVxjP3uioKfLcNaqZPKJ9ZHVo5pfAU5t8tItlvbZ96c-X8dwvIKvdS3_2hv_OrtJhWWSMKjN7ab0KhTRyxS2QSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=vagVfZ3GSjo2VhGwbX4vgMkw6MwjNjB6oK-EeSCmMrU3tygpzvid417b5Fyno0ZN0A7QWlgIQRvHcXqT-RTswoM6bMEltCkKc5AMwyF9QnRKwWoTBhMj9eGl50JnlY8APzNLs7oQ0lJpqEy4TkKGhiDnRhSorpgr6B8jgl3vNmjKs4paERJJ-7ZBV3tnsEe93mYaWI5VHmLHuEqxJsLLIc8fduSVUAEyaK_qHJnBAlYXKBjstzVmSkz0DY8fX18XkPuKkiYG19Am6Dy1b0risNbRMTVnL3Z9pcBJVI6HeC4J6PhUvQOXKGsxLoaYhJQM80i2Nh1NFcVY5JPp4-sYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=BHx6sl5oO_9B-kGBzq0g0mlVSRZxdgwKmdM8bR0_ItY3ZBCM7CyOY43BAOZN4Icod_XigW36FgV1sfeh5_XV4FLj3oYpviPV883cTZwy48eFc1cGgVoShjj9Mjzci8Drn9naEjjbe1L6qzgNmTW3NQB3WW4e8D1CVDT0pcWUs7g5FW0Lu4M6T3qt8zRpOk_hutVUMs_5l2wXsCQWNyOiO_g_WnY80w_5nxq114XtZXFA_ZfFXfWRNkrzsf5VPdl4DPM_hac8EWGWWdjtw68pgvkxFPNc1cBDMQNXeXwKKTYt4qYir5nuGKDYJnEMsXwiMI4siwiBlYGls_TimvB9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=FAyhCZgI98A6aq0Rb4gj1eWqS9pmjou_GmbrI8Oq29wd5OKMxkyCUzovnjRlniRE56w1HOXR9icSK2N1SgToT2G24yeNhbVhkzzr0Wccvrg7EjzIQmFI3VmdX3FGmEJh2L3we_MUuMPLpnU0kWPqMZ-00VzwoOkcsRfZILMNG9SH_04wFv7zpT4nAjlCtEc-Lqe5N8ynGkHNH9WiD7Oyi-uLKbJxwOznG7YFp2t5V1Aw8nsWy7ZJnNVNvzXbTYUHdbGzyKsX_XaBany2BDgZk2sb4dK8fRbi2ix2Sj8GemHSHDbGnjg87SphiIzUesHCyWi-jTZUvWi44GbJtcoruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=gebWfRYBtenaQGWCCe3qsaHkR50w-C8hFHdDyKdIJ_Al50vo6PZ57QlCs0d_TPnflZdONQXJ5ML8OgryIoFQyrQZ9KQbf81Zc8jzJPNd78u3KtDk-dBeSjsfpkuyxLnnRUMsRnBBxIzYx9ircmB5i5N5B6qKsEezbdRywNPAy4nEGSN4VBs6D7Y3-Gh6ae89OEl7xKAKm3L6Z3aB63fG8VMdCkspK5tQYPxPuCy4Gnqf9Ugkk2my7cBsmERklcesQ1_RUrULUWI93_G-2ic-5I59cx1g41odToe6L7_sqtOplQ3qSzSkzosOEPGLbzpxpeX-YhZ1TRQjKxLE_EcvmGsh-lz-ryNxsvHNkcV1dm9mllfbRPwtvym8FHdmHDdhsNsAhZpd2CW5PFkWhz3YqFejFZ1gMpD4IL687U-NozG4XYuTLXP6Bp55YDHusMusRpWJl2s2jfzgKpN0TXYIM5b1bojJu1UGko4qGdKNKf3YLNv030bjsROajUr7QNkXVOgYvwaYg1NT4v7xI3Ej6EM0zO1U4YzuJNt9g45NfK2ucjcNbUcsBqObwI6otFnaQUxjbrL9rekOZBxx-oxJwBJU8xEB-zOrTr2sLMMTES8Pc6uL9GcYsod9wG-7l4Lqn73oC8r8WAR-3Ogz4z3IIEsVzgUR12cFGlBz5dXsUGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=Nf5hgSkTbPXQr8CPDUONdLg2ql-FkcyDKJdaSr7EVv203zJ7mnnXDu3vMtUDCr9GAwlMEZAGHAsN0WDgcNXkrmE25fVX1IkVSqWzQ4CTUiDOeOLdI0SUp3oWXjEbOiiWdWySCSb7IS0yxbjOytDVzwG78mBmYURtLdiyTLusIsMTvwTW_UP4N5f1XxDfwYUhac_3uYPOZA3PgN27I2hceIbZ6d5cIxksVWc47a6cgeA7NbP_YtKpZ1mKA7S6E8wwwpG2WH-Ncs4414LtQuChl1ukm_s1mVXDMdc5PXr6yvXlnW4I45YXNPaHwnUvi-oNYEJsaPou6V4h5jJyrtkmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=IE0jq0s24ChhE0NpUuupgXHQMD9Et1XBOq6QLGMSpDA2PLBF41t1UiYLyNbmUmqUWeEAyZfBGrEqIjfiWOP1c-ON0ZSPbfA4CUtqRumsmm3j60dcjwV5QvbL8S0knoAqBN6JiOcF21HOfl0u7Wk0GNabRMcELc1L6jV43fGNjDf2WWKUzb-UHOCftYO0XqnG9briJXtt8SmNhgXVQw3AbcAdXXmp9daVX-hHs-MiK1Et9HYwltioo0LabCbCyRinSXKm3i0ffChNc6nmg5lEdgUS_X9CXQr966XdKDZgkP7nXsGTC7D2Vr3DeeN3H2rhbiXa_bv_CHAkSdAT76-O0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ffyprLgY_gk3FCwrty6_8kT1wMutnDTXyXstwon8tuvrRgi08hxqjzVPqv-KceDj0phWj96Lvs0Qa2-sQVke7ascleyn6VTjIvn0gIx-dt3VmulX4g7bNqAAzcYlVilQwvG9g2z0VYJ17DdhLu5t2ybH6sjWR5aZwJpT9HS5WJTM9xRbqg3iE4ETI6-wm2TWW6znt56-oSJxml5qS2bSQaUaXJ38X2h_dhFCy9VqQDoe5-GCHBIioByq72GNSKnfd6u5VcWnRwu9S2hHNYx5pMF84ul7dbi0GPSzFxgQ_OQjBSe7b26CQbQCd3oYn_FzEByK2x-C6I2sT1m14RSoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyrLAg5Bbfw9Rh1tEQAl8V0TYYGuWDlTxMX9CtSElotiYc-Ui6rCafcyGX3CLiYcTQh71oY24EuWqNJCp7UVpOoHSW3oaZ1Ia1znSc99jY9AgQSLuesiVKjaK256GU7K2-G18FrOw3RAzuG-crxNNWQMnGcpdM6VW1miQE2yVkvArR6mi5lIDrhai1LnhTPjD8W5S35T7F-DxGBhf6EZ9lhR6DHaxH-XOjkRMpDn6Tum3c_3t9XRxapxWIr52HG-8b-DHvwkA3R1Zdi_z0_ZmHwhmDoSDHbptlbMuMLtRezwsCrdNh9hUqR6fD15lowiw2Xy0RpsOBDg9ZRRLME0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=bbdvWT_ef1_ay6zlbJqAn9z3rSY4yUslYqcfR2zv4RTqO7Xj8DtOR6jlKW7YmOtYh9GR3rxSe4wZcO2DzrgITffx_mhFOtJINnR0V0xNOoqKNZ8NC6EBLeHDKjJTtRYETaw-CUzTDtk-8z5Fz-CCdQsp2Neb-mYLTJvhmeSXcfh91ZXAchT9toyPpgPJa4KhNRVlGkelPZpKvNokMAgkeasgAnoSpwThtRwyC13hYyTiLUsPp5S36TyUhABUP1GQHbwLoqxAnhTctigVqmwd3gtqvcYUG_YR1tqltyJhXGUSF65kYB4tT-uFWLjQWMdhL_5eKR06VOuO7ynALGDTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=bbdvWT_ef1_ay6zlbJqAn9z3rSY4yUslYqcfR2zv4RTqO7Xj8DtOR6jlKW7YmOtYh9GR3rxSe4wZcO2DzrgITffx_mhFOtJINnR0V0xNOoqKNZ8NC6EBLeHDKjJTtRYETaw-CUzTDtk-8z5Fz-CCdQsp2Neb-mYLTJvhmeSXcfh91ZXAchT9toyPpgPJa4KhNRVlGkelPZpKvNokMAgkeasgAnoSpwThtRwyC13hYyTiLUsPp5S36TyUhABUP1GQHbwLoqxAnhTctigVqmwd3gtqvcYUG_YR1tqltyJhXGUSF65kYB4tT-uFWLjQWMdhL_5eKR06VOuO7ynALGDTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=tEZoJwDp2SaQRTEDrV0T3w1HI5OvLty90nWZHg8YvJCNTZXF_I1WJ9bm7E9qe7OFbWc_HKdNwaF9XHgYUFCYnEY_vn2k_B055ew_Zh_W0ZtT_5sjeSw9t6Otm0YIZldRbxvd4VyPZJNDh3nYz_3uLMS6Tqz9XzFNx6K_wu_r7wjXUX3sz9_njS9GNXbq4qUQMOycAInpFmEV5ATjLHXsrFrPecpZjMApSyW43MQJtVERuzZ_Zr9yXOV3lOS-t70QLsyePtFQzBqvhnWAnE4mPSF3Hb_yP5G8bal2Hkm-EALG8VFcn6C_LrAV4LSQes685xLJMdRfl1Xf3LotV1QJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=tEZoJwDp2SaQRTEDrV0T3w1HI5OvLty90nWZHg8YvJCNTZXF_I1WJ9bm7E9qe7OFbWc_HKdNwaF9XHgYUFCYnEY_vn2k_B055ew_Zh_W0ZtT_5sjeSw9t6Otm0YIZldRbxvd4VyPZJNDh3nYz_3uLMS6Tqz9XzFNx6K_wu_r7wjXUX3sz9_njS9GNXbq4qUQMOycAInpFmEV5ATjLHXsrFrPecpZjMApSyW43MQJtVERuzZ_Zr9yXOV3lOS-t70QLsyePtFQzBqvhnWAnE4mPSF3Hb_yP5G8bal2Hkm-EALG8VFcn6C_LrAV4LSQes685xLJMdRfl1Xf3LotV1QJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=IeGlJKTgWpVihaegopP9rKzRdXEt7KWHglT4ZqNwlgJ96Gltm1lRiLrtYFBh8XwUtVWbfAiHU-OEX55oDyPr-waGk3P1kMA6dro5EU74rncpnGD6LtliyCjhA2GUd1IfgsKleMu38uSowsKiQC_dAWOmyS9VOi2YfddVf_KsNGl1YAUe2mYHByOzEAYwJPVFCMcQu1O64hEJYHeTG0lm93u1Ab-7j_LB66GwRojmsm3_aqN-EkdFklj13avlgs2OjRxeO-WaHOI5FJhIkRQBeS2TZHATywCwUSJ62vtefhO257zam7gJ5E6EvFnAgboWNmIMfmP-wUuZ-wwQWA7Knw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=IeGlJKTgWpVihaegopP9rKzRdXEt7KWHglT4ZqNwlgJ96Gltm1lRiLrtYFBh8XwUtVWbfAiHU-OEX55oDyPr-waGk3P1kMA6dro5EU74rncpnGD6LtliyCjhA2GUd1IfgsKleMu38uSowsKiQC_dAWOmyS9VOi2YfddVf_KsNGl1YAUe2mYHByOzEAYwJPVFCMcQu1O64hEJYHeTG0lm93u1Ab-7j_LB66GwRojmsm3_aqN-EkdFklj13avlgs2OjRxeO-WaHOI5FJhIkRQBeS2TZHATywCwUSJ62vtefhO257zam7gJ5E6EvFnAgboWNmIMfmP-wUuZ-wwQWA7Knw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=ORDwtdeHSLgJBitX-noRS3wk64avsWQkDyXj3hV4OEWlSLlDmBLqf_tiFgEqJclXQqh43gqBlCWXF02n7Ch4n6LDkN21NwrJRTx5vN3_oRKZFTEwP8dVTkcdjxRrFuJEQfBFUPFRg1PnIt_atZ4KNQhCFTx8oBgn3M9wO8xqIbKc0ThtPhQ9fU9AstcqFSQQmtdeDpeuG885gNpZk3nD7mn37oVvkixHA0ajtx-tUSt_y59oCBsoCx4-xuiFqmGiQDTQ8Zk5LrjILU3qpl3OXZyz89Ir0XOpkM6BAvKez7Y5k7v4-VMwOypf6vbD3-zz83F3nFUqqtanP-6VkuV-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=ORDwtdeHSLgJBitX-noRS3wk64avsWQkDyXj3hV4OEWlSLlDmBLqf_tiFgEqJclXQqh43gqBlCWXF02n7Ch4n6LDkN21NwrJRTx5vN3_oRKZFTEwP8dVTkcdjxRrFuJEQfBFUPFRg1PnIt_atZ4KNQhCFTx8oBgn3M9wO8xqIbKc0ThtPhQ9fU9AstcqFSQQmtdeDpeuG885gNpZk3nD7mn37oVvkixHA0ajtx-tUSt_y59oCBsoCx4-xuiFqmGiQDTQ8Zk5LrjILU3qpl3OXZyz89Ir0XOpkM6BAvKez7Y5k7v4-VMwOypf6vbD3-zz83F3nFUqqtanP-6VkuV-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=ioKdt1gFn-q1ysj0HHzhBxulOO8VFcMStzIIM433e6Ryh-KU5OB-hAlYlmdzzgPwvOhdtGc4mzN77BmF_w8PDqXJ_Q9GNfPGkJ3OEIzCNc8rAnc-JJJDNlIAqW922AQZ4C09OGpZeavmqqbaQANvIh18KcGCRoqdXMfQ5ZL9sgVBdI6Y5wMTDuq71VtvWljYGwFsWfTCbMhZ3f7EVxZaTnC31i3LN1kOy7fuqVqS5iVOSSBDsOXXXLRdg4wrpfgiHlv7MPr9OgCMTFBJfm4-Hl7o3Bh37lTKvxt2udzL8gff0rwz49QlYynFhYlQ-GYpNUq3KD2J1plKEyzoKhc28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=ioKdt1gFn-q1ysj0HHzhBxulOO8VFcMStzIIM433e6Ryh-KU5OB-hAlYlmdzzgPwvOhdtGc4mzN77BmF_w8PDqXJ_Q9GNfPGkJ3OEIzCNc8rAnc-JJJDNlIAqW922AQZ4C09OGpZeavmqqbaQANvIh18KcGCRoqdXMfQ5ZL9sgVBdI6Y5wMTDuq71VtvWljYGwFsWfTCbMhZ3f7EVxZaTnC31i3LN1kOy7fuqVqS5iVOSSBDsOXXXLRdg4wrpfgiHlv7MPr9OgCMTFBJfm4-Hl7o3Bh37lTKvxt2udzL8gff0rwz49QlYynFhYlQ-GYpNUq3KD2J1plKEyzoKhc28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve7P93zhgyCbzKLF-KHp3jc6kto9hMd9H-eEqTku5rmrhVQm9CiBkgmbkvIF_UJJB2yJLXEpo3HfZfi8_7qALz60J27Kv8arP7mjbYCZBBWnAQR9o41TaefH9_AhJ1M6Z6U77p6k9AYJBVs5pdYF-YyuRGb62-5WYdJTQ9zC9Q7KNaFR5NUg772oynKPbgU37kIYY9b60mEPy43_CBZwV7SmPLUvtzsCOkEsZ2fvHPQ1lPxGjNz7ClMTJdSRbWp-q2pgSpULr4CqTtkAee-0XJdygfsDy65oOSM8wepkkBd0vqblHK47ghK0FcMrR7aSlr2lYGwgrLOr5erZRMWkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYYPR0TGhNcDHvHunkwLlaS294kiOgkRyBiAfEuHeuE4Aw39OrIIMa19exNWnrozECeAMv1hLJg4CpnmI3GJ6pFR7EfykWeZXl9lPNYv8GL38gzQWSpZ_ZRtXqe55LitXcnfKbt0SQMg0-jtMKivfGwniwQEP7s9lCA_gCddVZsYT3Wz_7ZQb6Ow8wgyoge0NiDHuHT0Bmw8DwVgS-xrkdI4ijW9UDEFRKtdoZa7F2y33CdY9hMpABcCTwXqTyYa4-3JmsAnv07knGt6VGGtYxAilY3s30FtVPo05a_vGHS6CVql9dYe6xxirUP3739ODpTXVVmYBPKuyCG9PS4c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzliEQINyK0rc6nS_kzPQlNY1f3JZ3HoxNWll-vU__F6j-5Bjh3WSKmbIyccxHriJd3KhOVXs8tGRmxD6_cdtqEbdXDUP6TADNKOPf_jsflt6marIi3Kmaj3gVzbSUPsXqtFp2wjZjFFpLyBG1xnukATwkZo9s6pWjgTwJu41IHvQppt5WZauYX7HRmnM0hpsFAR03_x1dLUdm5zDL7CK5QC_XGvoCvxIunMqekzfMMIAFARUrPFsoynW497643ZbaTtqjk56GkOO6rK1EE-wkeGyiTsxJtU7_gvaRnzz-Ov1EqrHuRbot7mbFp0ijOOSeRKanD6YezeyAQCaoFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCjAD2IkWHJ2rOzGRvoIoeNCwl1Ty9rAee4S7qxGxfSBQQf4B3h9hAiFQLHzWy7FTY8JXkJ-xVwMPatLVfpe5FGKQQsmdEhqkGolpiZS5QBqKnjOqqcKnbCLuXwXGnvYSdA69BoAqNAPMnGl-6mc5IYISk9CmWSB-ciabch28SAULLX-ypIgnA_TtRelmOczVCRl8F8064tN6f2sdceBY_Wth_MhHzE6VkK9Uizr9gKi01SZ7dF0XygoIDbtW5m6zqm2J-n5XZPKD5NhHisRki9Ad7TyWGodJD_IbGtkS8gj15MqQz13kI7hMHPrR3-laOxxzAcUtbuWlALb_oOOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2n6OjDDP_cAqS76SYdXkYjTJ4T7HchDXQX43WTwvBQyW_A5-GCm2F8qQZngpZz-Q9LbbRRH8uJ-Dq3EecZrt4uIDLFOeSSRCCCj7L90Ob_1hJLtJfP8BVNwznIuyxYWfDIkPQHW9sPs7D3FnWpxGazc5-7pvsQRsD8AheYq1-uVlMl9weBKiBPFrRvjDsH23KZpPRDt_7P-G7z8OV84oV6lUlFmDfR0PNcvCWAecdn7AdswN5xsq5NlvV2gAgbDlgO_RDN-Te9zwn167Ki2Fvq-I9ZraKE4KWnVr3WepL_MhN9yY701umwlJMvFyD_ClxmvLRw1-AATdGLFVIkOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=dmhMIv4Y183I5Jurb7prd_KXHW8QGTvvqJ3ryE2w61eed9ce03MkYMTbYPm7hGvy2b4e1iOpFAU1Oqk-h2N4P9Ua8xSTmsNsymM_R9iDsyBpiiu0pdUvC045sNVZ_l2_rCVWs4odm7Mtm7vLfmYrP8sTeg19dNdb3BlpG7fUn9whBPyY825hb2TsG2tqyy-7AquDiOVNJGN1q8DGlzjFip_r1zyMIa1Uf1RHuS5LRtaQueuJxZUih-hPh3a6hqxMt0PD0ndV8JNnE8OLKghriRaRqd5nDfn7g2jg0suIYGq9gFor3oCiQ7Qlc1KgdRRqvb9I5adxrLjce_uoTCbJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=dmhMIv4Y183I5Jurb7prd_KXHW8QGTvvqJ3ryE2w61eed9ce03MkYMTbYPm7hGvy2b4e1iOpFAU1Oqk-h2N4P9Ua8xSTmsNsymM_R9iDsyBpiiu0pdUvC045sNVZ_l2_rCVWs4odm7Mtm7vLfmYrP8sTeg19dNdb3BlpG7fUn9whBPyY825hb2TsG2tqyy-7AquDiOVNJGN1q8DGlzjFip_r1zyMIa1Uf1RHuS5LRtaQueuJxZUih-hPh3a6hqxMt0PD0ndV8JNnE8OLKghriRaRqd5nDfn7g2jg0suIYGq9gFor3oCiQ7Qlc1KgdRRqvb9I5adxrLjce_uoTCbJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cliyiQtJeDtrvxNodcO9ojJCC0huLxON1ikWOmOOlr2SC_rLwAsrl4GI0Heli_oHUQSv5pU7F4hpBseP-R_pudeJYAvOcAUDFE1pRtFOwu08DMcVzY6WV-L_f2C9CFSulul0kb7ULtddmp_QQ-w8vrlYpiX6iIIcj0tFhOBIts_H18LYsB3wvInzBJlmrGMdd0VSH2N7Yon3KYAWRhMVuNm-tad8Y_V9dfPvrXeNYOB3QQ1LGWRMuPI0wa8tYhnWWk7E061NkVeGHF4A1wLDBW_NrWB_v47xiZvQSsPUtvLrBMoCd2v4QqvRtobMLhm1r9tfYLnSLIy66X5W14SDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HjBN8Vjdtfv6OSk5UVlvcZ3wAA1YIRFUgB6EDECbgu27S-aEDIt8oCe9nPtWbHvrFBVl5tRDDSnFSIDVIZ4hic0yE_1M7LwT3-MMj6ANxZx0yErEIpUMyRqrzH2EhB5b6E3NTK1l2Q8DyVAPZsktzuj8ZHJ3yKsa1m2wPBLhGTtHCwswTmREcY8A0EcMQjsNOvDdsI3juA-spMkJ9MBCGRS8Wzriqlk8CGUcQkE-rpFnCFI5HMHaNbyLzGH3mXJt2R2cJnZVkeKs1NY8CB_NxlKRN_jOjVuv33rTV68d5epZ83JUgqBizxNR5TuR-GXdTBROjt_HPUn_aoIfgSRrvR2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HjBN8Vjdtfv6OSk5UVlvcZ3wAA1YIRFUgB6EDECbgu27S-aEDIt8oCe9nPtWbHvrFBVl5tRDDSnFSIDVIZ4hic0yE_1M7LwT3-MMj6ANxZx0yErEIpUMyRqrzH2EhB5b6E3NTK1l2Q8DyVAPZsktzuj8ZHJ3yKsa1m2wPBLhGTtHCwswTmREcY8A0EcMQjsNOvDdsI3juA-spMkJ9MBCGRS8Wzriqlk8CGUcQkE-rpFnCFI5HMHaNbyLzGH3mXJt2R2cJnZVkeKs1NY8CB_NxlKRN_jOjVuv33rTV68d5epZ83JUgqBizxNR5TuR-GXdTBROjt_HPUn_aoIfgSRrvR2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=e-r-sP5vNkoIKhFrq54oADfN2SEfucOQZEmjm0hcp3XEQT-QarsseDOKg69DWnoSj7raakKn90XaLTPURMUSWwabkMZLk-bGep2BJCDmS8qEwV5Nxq_Kz_E3Kwf--3JzeGG3ntJb5l9vt0B4DKoi3SRPWYYOovZjGahp49n0yuY644bdLrbSnuF5_lGqGYgjusxfz-y6m29l1nck9UEWIgiFiTQfRGBjelek1lKMO3iV78ijQ2s47D1iYiW6YnKYpqHe4oczFLrO17EJJEe1K5NroBiyegnHrMFq2BVakauhDddV89EwRaaCsP_pdO_uGOFAH75TXwUrLAGPGhmwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=e-r-sP5vNkoIKhFrq54oADfN2SEfucOQZEmjm0hcp3XEQT-QarsseDOKg69DWnoSj7raakKn90XaLTPURMUSWwabkMZLk-bGep2BJCDmS8qEwV5Nxq_Kz_E3Kwf--3JzeGG3ntJb5l9vt0B4DKoi3SRPWYYOovZjGahp49n0yuY644bdLrbSnuF5_lGqGYgjusxfz-y6m29l1nck9UEWIgiFiTQfRGBjelek1lKMO3iV78ijQ2s47D1iYiW6YnKYpqHe4oczFLrO17EJJEe1K5NroBiyegnHrMFq2BVakauhDddV89EwRaaCsP_pdO_uGOFAH75TXwUrLAGPGhmwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=Dku5zEvnHh-SSikZHc-pH5hjzleO34EFKybUqVSchFi0c_OuerZdqDo6hf-5DhIVSSFBId_zQel8XDQ7JLbxQ8ZjD670NY17fF5LUqkeoHf7NbkgWin-GHyiO5CNK7YMIvHFxjeU-N7EKrKGzhuZ3NYr3CF5BgLZVx_qjlY7SGy6Fm2MLyU9e1nd_o1azS4VG-5di9QErDlhX4NQFgB0IXvVlwjZcccBm3j-xoIr9-KFZ6xrN389bLcxZtYSZnFMqNI4F91rHMWZfn7tAqgnvIoSlVvz-XthdUngUCe5KOnOKj7AsnfqU-wlByPpFZJkr7wK2I2Kk3r9EwWIN-qJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=Dku5zEvnHh-SSikZHc-pH5hjzleO34EFKybUqVSchFi0c_OuerZdqDo6hf-5DhIVSSFBId_zQel8XDQ7JLbxQ8ZjD670NY17fF5LUqkeoHf7NbkgWin-GHyiO5CNK7YMIvHFxjeU-N7EKrKGzhuZ3NYr3CF5BgLZVx_qjlY7SGy6Fm2MLyU9e1nd_o1azS4VG-5di9QErDlhX4NQFgB0IXvVlwjZcccBm3j-xoIr9-KFZ6xrN389bLcxZtYSZnFMqNI4F91rHMWZfn7tAqgnvIoSlVvz-XthdUngUCe5KOnOKj7AsnfqU-wlByPpFZJkr7wK2I2Kk3r9EwWIN-qJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=owK-i10cAEN09HkSvJpkxiRah9d5KorI-o938Vg3ZAyWWIbq-wEJv5o-djzBAkaB8y19D_RP81o0WzxBwqTaiAWiErLH3DmFTnSHmhNypjqmD4GyQxYL55-Al7OuI6jI3mWYTsSQNu-UtxHBkHCCpiahFZ-0p4NkqQLwffUd_EAd3InCUVd1PGUuh_fC06FL5Hb7eFvuJDqWwebtdhVai8oXplV6bhdLgCeQDhjjH7bEDhYyqQrTh4ciEPKiituLhg2x9BIEM_dpZ7BoEdlQ67srOFAzqOZJTZ_MfpDEI7KwbF7yIymwEgaGpryDhxiZ3oVd2b5JcG84_dSDXV9C8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=owK-i10cAEN09HkSvJpkxiRah9d5KorI-o938Vg3ZAyWWIbq-wEJv5o-djzBAkaB8y19D_RP81o0WzxBwqTaiAWiErLH3DmFTnSHmhNypjqmD4GyQxYL55-Al7OuI6jI3mWYTsSQNu-UtxHBkHCCpiahFZ-0p4NkqQLwffUd_EAd3InCUVd1PGUuh_fC06FL5Hb7eFvuJDqWwebtdhVai8oXplV6bhdLgCeQDhjjH7bEDhYyqQrTh4ciEPKiituLhg2x9BIEM_dpZ7BoEdlQ67srOFAzqOZJTZ_MfpDEI7KwbF7yIymwEgaGpryDhxiZ3oVd2b5JcG84_dSDXV9C8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OCdz6OWQkOMf03om0_PqD3zO39G5ff9mMFeuiu0Qg75EoyyHtBjXk-eHOrJkE0C4BeZosNAutViB1xDcW3-LlesXT9gejMPuarQfAxjLuT2zitKN-CgpB6o8A-G7-F94Z4WdoI50FdMPY4DJiVrKIuFylJKXjSMhNma9QVI7cligl7chE3Pizp-a8igBzfkodfg-IpKqc8u-f1KS2ASqVxVcbymT9fHxzhOgXJJXR5C_IUZ-VwlSREjrohakRVMmq0UP9TNshGDGnNbDBMlwQQUSVEUku8qnT2lBcrExAr6ghhnKkQacYFBHnrJHmVjhOarDaXMO9acehDHAw-4OtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OCdz6OWQkOMf03om0_PqD3zO39G5ff9mMFeuiu0Qg75EoyyHtBjXk-eHOrJkE0C4BeZosNAutViB1xDcW3-LlesXT9gejMPuarQfAxjLuT2zitKN-CgpB6o8A-G7-F94Z4WdoI50FdMPY4DJiVrKIuFylJKXjSMhNma9QVI7cligl7chE3Pizp-a8igBzfkodfg-IpKqc8u-f1KS2ASqVxVcbymT9fHxzhOgXJJXR5C_IUZ-VwlSREjrohakRVMmq0UP9TNshGDGnNbDBMlwQQUSVEUku8qnT2lBcrExAr6ghhnKkQacYFBHnrJHmVjhOarDaXMO9acehDHAw-4OtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=L8tUlGBz1BBaJRFncf_b71SCNbiWsb9dYfx4b1hEhsZhk6mi6F0M6pfuExSgkMKnPjYrTH852gWAHRmsD7UnkY_06gG4_Z39jaPsC8ei_raV7ubGmXcc-7VQsW-UhCzannx63dmCjThcEvV3WD4H93lEJqebL6o4VP6t4Vc7aBU1aIwul_bvbD249xEEzM3B4WWVEmHYysORfPwCHDh0VKDocuJgJZYui-Wz_2Fui4pAHNk6bCX49pRL_MZZfMmxEKtmNpGUrWgpnwZM1_H8LS5LvJf6Iff687KrNgDRbvvSN6SO3lS6vkyCCQZlls1-nP0YDxsQ9_beM8My2et6MVs2Oj0hYER0gvlQZbSgKbmt96pXMqY4QqXGWqeQBQwNARWZ7TBHaua6ShwvX33L4JEPY__MCrcGkCjQGsnN16AFx1wMG1X5izk1U5zM7GWAXyilIOPrILxMf_K-fItBBEpX24ZfONJnSrfo6BBTHBwDxx4u2R0jZd0X4z9XHt4cTdNn2x71UkF2yJGxiyeaCwvpY8y2higrEZRgwQ3R60yO2n7u0Sa7HydARAiNn0HJCDRCnyXX30Jnkt-fcThwIwCONIpkak0gKzf5wbbe1q2kLfGb0s7bpmZuPuRekkQ3EmoQHjaZnWbVXtig3e11odxoj0pSF4Z_5A4xBBg_XpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=L8tUlGBz1BBaJRFncf_b71SCNbiWsb9dYfx4b1hEhsZhk6mi6F0M6pfuExSgkMKnPjYrTH852gWAHRmsD7UnkY_06gG4_Z39jaPsC8ei_raV7ubGmXcc-7VQsW-UhCzannx63dmCjThcEvV3WD4H93lEJqebL6o4VP6t4Vc7aBU1aIwul_bvbD249xEEzM3B4WWVEmHYysORfPwCHDh0VKDocuJgJZYui-Wz_2Fui4pAHNk6bCX49pRL_MZZfMmxEKtmNpGUrWgpnwZM1_H8LS5LvJf6Iff687KrNgDRbvvSN6SO3lS6vkyCCQZlls1-nP0YDxsQ9_beM8My2et6MVs2Oj0hYER0gvlQZbSgKbmt96pXMqY4QqXGWqeQBQwNARWZ7TBHaua6ShwvX33L4JEPY__MCrcGkCjQGsnN16AFx1wMG1X5izk1U5zM7GWAXyilIOPrILxMf_K-fItBBEpX24ZfONJnSrfo6BBTHBwDxx4u2R0jZd0X4z9XHt4cTdNn2x71UkF2yJGxiyeaCwvpY8y2higrEZRgwQ3R60yO2n7u0Sa7HydARAiNn0HJCDRCnyXX30Jnkt-fcThwIwCONIpkak0gKzf5wbbe1q2kLfGb0s7bpmZuPuRekkQ3EmoQHjaZnWbVXtig3e11odxoj0pSF4Z_5A4xBBg_XpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=Gv0TzzFoeQ7fdSpN7EpjGY92QZqmcjoVCYQ9ot4cdeh-0jbS-qgKnhSwLs_T8emS8eiKEMUWLwNxqFj0jMElC1MSwZn1BDFSf0kuW9CDusnyTOM3USSJBpTWxNchVwrYEGy66fho93L-6SVH-L34QLzWveu_sWfdqF2uJkVRFDOobv298WFAwspeVBmQqwzGs84K-TOxYi5yaF58stsDxbQtgyrdfm5jc1CNfaRABkwcwD-TktV2LaJg6CuEP66z80nHg98Qwo4_ZEgetOAW42yBxK7odgp7fwFSL8PrnDrGW6mfBh2qCLWn1W7frYaQ_pGcWVAz59LVEJbm6N4BkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=Gv0TzzFoeQ7fdSpN7EpjGY92QZqmcjoVCYQ9ot4cdeh-0jbS-qgKnhSwLs_T8emS8eiKEMUWLwNxqFj0jMElC1MSwZn1BDFSf0kuW9CDusnyTOM3USSJBpTWxNchVwrYEGy66fho93L-6SVH-L34QLzWveu_sWfdqF2uJkVRFDOobv298WFAwspeVBmQqwzGs84K-TOxYi5yaF58stsDxbQtgyrdfm5jc1CNfaRABkwcwD-TktV2LaJg6CuEP66z80nHg98Qwo4_ZEgetOAW42yBxK7odgp7fwFSL8PrnDrGW6mfBh2qCLWn1W7frYaQ_pGcWVAz59LVEJbm6N4BkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=IN6Uh8g_EksURo2KfubdqeE-sGBcLzhJGRLI0GlfRNxRm3rXKoCgmULVgNTnhsziPVFvGrM0jqkk4Yh2yPp2GRzHcFQqd_nxw2FERMUkTxJsCcCuNTT-VKCkEXfbRKhMWB02t7QbRMvLvmkrOyxeDNcb-AJdPu9ZxUWnMO9LGYgFxkqWti3gjmxQX-SeHiLp9rxOAeZl4pMECY8-v7HyhAqLpXyt-5U7GJ9YO0wBqU964q6WE9UVMM0KJj6Jf1lncpSm5QRBzt-kO7_OMXYJRaZR_lFTT0MTo81uj-sAW3N1viCTWKQTVqhFY_pXbeEGvmE7gcxZiF-WnfSHKil8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=IN6Uh8g_EksURo2KfubdqeE-sGBcLzhJGRLI0GlfRNxRm3rXKoCgmULVgNTnhsziPVFvGrM0jqkk4Yh2yPp2GRzHcFQqd_nxw2FERMUkTxJsCcCuNTT-VKCkEXfbRKhMWB02t7QbRMvLvmkrOyxeDNcb-AJdPu9ZxUWnMO9LGYgFxkqWti3gjmxQX-SeHiLp9rxOAeZl4pMECY8-v7HyhAqLpXyt-5U7GJ9YO0wBqU964q6WE9UVMM0KJj6Jf1lncpSm5QRBzt-kO7_OMXYJRaZR_lFTT0MTo81uj-sAW3N1viCTWKQTVqhFY_pXbeEGvmE7gcxZiF-WnfSHKil8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYyn0IWTfKWS46fOlzU3mq--bShri7aUg3_5volWz1C4J1RtbyVFY-VI1w6FGiGQ0_ZXREXOxz9zuKw-toDLUTIKoZ1PMCSL9Qo99jO_QTw5QMyLZsefPT9LtKRq5AAnhiHF1hjgRUc8YHcHzEYGr7F_xXNxMplwoT2KOMr1lGt2DnO0tsk4KtvquY1Mw_s2fPc46s_VK0WT3tHsCGAg51nJoHPKLQoI2kTHTns-xYWBx4uMIGesCbb5nUtNZMsvXzqkxpd0kC484-mBcIVSi2of1dihmQM4MBJCUZcUBWtLCCLAGR_ozM2bxsfeutAIKjCsxtJxdv9upOHvQXBkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=YCfDWREn9FSIbojR2U7zfz6TOea5i7MYODQuPUasGO0RoZr548whUz0vhinemsR8RCLSai-pfDUs56QQdEvDM81YEJyvgMb_q3jgxfUSN7E2HMcp1bv11rfBzsmiCdhUsoN9xdNXsbWi2ZTvx8AthYIfqRB9XDLERjwIRP4sP0hlT4H6Eqp4ETz-DNsbgmSjjTsox-MPk4hctIOHk5q4azqJqBO6StE6zfFkNruWxCUD4WGODZawpawKcvQHg39adTAxm6nvsSXHBm4m9H6jgNX5UxFR2f-AhRjWJgD_VdYggLTcCPPw00qmJx_8qmFFgY1x71AlrwSswoxIP_6enQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=YCfDWREn9FSIbojR2U7zfz6TOea5i7MYODQuPUasGO0RoZr548whUz0vhinemsR8RCLSai-pfDUs56QQdEvDM81YEJyvgMb_q3jgxfUSN7E2HMcp1bv11rfBzsmiCdhUsoN9xdNXsbWi2ZTvx8AthYIfqRB9XDLERjwIRP4sP0hlT4H6Eqp4ETz-DNsbgmSjjTsox-MPk4hctIOHk5q4azqJqBO6StE6zfFkNruWxCUD4WGODZawpawKcvQHg39adTAxm6nvsSXHBm4m9H6jgNX5UxFR2f-AhRjWJgD_VdYggLTcCPPw00qmJx_8qmFFgY1x71AlrwSswoxIP_6enQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-XoIS_pbsgGs6ASTn1IjBpe-KxjXseeODIGeeGb5JZZq2VhVSUGCC1W-ZwxgF2xeteVF3_5UKrynzbivP_GD_LwegVzNybNHhThKVhiIjlmjp5PXZ6NgV05Qf3Ca4c7kE6XXKpCWr4pOVfd2jQe_Ema63QYhK7HIgpnZ6nQbWuFF9jdbcnF_5x3FEHeJ5JGdXnY3w6jDiCkioViKjx6rQWOy87Z3ansifr1r9vSPjqXxNv69YTabikv9NFZ86vDB2-Qd3MJLl7_Kc5S5mMkEjzW9Ta7qm-OzYJx8cGNuhdy2J8K3T7rCJFrivhOmrFyy_lOaMNm_D67rC9mm5GXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=tVqfs_He1vDDAKNcAhsQ8pwkrfq8cwKy0hRlICj7OMvwtkLC7nTANpzeBY8b2mD9qzIbb4DyxNU6mQLGKbs2TX85lwLzymZcGT3-B7tg7lv_iLov60FZj6RTNuGcOfTprMCfnIZucg_tP9rL9jddV_cUDwfMujAgS_Hdlt4XEaZ_rk9pi4wDitxy_0_en5hDh2bxVRk5jI6VeskGMS0RyI6y2LcLLlQlJQtTQKT8l33Cn7XNPTxm-WOfdOCQ-hM9-yFVqaH3vjMKyafDJj7Si82AAQVt6D39lYWdtoF4jAksh4Y2OlhUIar4Ulj64b9bfnuaQG66xbvOF_tUP1Oajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=tVqfs_He1vDDAKNcAhsQ8pwkrfq8cwKy0hRlICj7OMvwtkLC7nTANpzeBY8b2mD9qzIbb4DyxNU6mQLGKbs2TX85lwLzymZcGT3-B7tg7lv_iLov60FZj6RTNuGcOfTprMCfnIZucg_tP9rL9jddV_cUDwfMujAgS_Hdlt4XEaZ_rk9pi4wDitxy_0_en5hDh2bxVRk5jI6VeskGMS0RyI6y2LcLLlQlJQtTQKT8l33Cn7XNPTxm-WOfdOCQ-hM9-yFVqaH3vjMKyafDJj7Si82AAQVt6D39lYWdtoF4jAksh4Y2OlhUIar4Ulj64b9bfnuaQG66xbvOF_tUP1Oajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=onrUHjpIYDEdawzV9u59ZYM9O6AT9YOMafmJSCbio1PHxXFH3k4d9KUNLUYKrgG3tOSqbUqvTZK989B1qPr57C43o8Zwc3-hmHts5SK25pKplOL0t3_KS8mdGk-tJFRE3h-ppLUSSSugWWyHECalo5O6iot-YVjQl0LOureFsGdupgJtBAnRNQoeFYdc3Vvau0b_QaCKu_UHVb0_LizkuKalq-BUDsjkpsqyD3ybbt1eFWPArIJ6NTxxPbOM3OC3YPCAtFHFuf0osjQGnhBWdzP_K3uxDNTK9W1NbfOfSLGcZu4hwJDCKRuBwTfKaL4kKOi_0k1mJr77PMEsgJNteg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=onrUHjpIYDEdawzV9u59ZYM9O6AT9YOMafmJSCbio1PHxXFH3k4d9KUNLUYKrgG3tOSqbUqvTZK989B1qPr57C43o8Zwc3-hmHts5SK25pKplOL0t3_KS8mdGk-tJFRE3h-ppLUSSSugWWyHECalo5O6iot-YVjQl0LOureFsGdupgJtBAnRNQoeFYdc3Vvau0b_QaCKu_UHVb0_LizkuKalq-BUDsjkpsqyD3ybbt1eFWPArIJ6NTxxPbOM3OC3YPCAtFHFuf0osjQGnhBWdzP_K3uxDNTK9W1NbfOfSLGcZu4hwJDCKRuBwTfKaL4kKOi_0k1mJr77PMEsgJNteg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=CuJFSEsJNVOgz1J3t23Nhn-oAF2b9T56_AgNhj8mj87jfPVGkmQ2T1kVUEIWV5EPQeCYe4gQPEufX6K7Ir8EWVYnM9sXwtOsBTYPLLhpQwhFxyn_1Gydg1SyQfw26Caogi8bxgIFHFakPaMhyXnipeTI-rehdFA8ZDv-q6WUE6MpX1tmwxHRMdq3cYfsim4upbnipwY8RCoDSmCZHIHFsq05npNotRn2q4cjQXhPdbXWsYLVIwLm7IhyuxwFjzXMq5f2RIKHyi9SDWOxugfnlpa0E4RYLuGttuXafXzjHHFQEylqdOY7w9wSWuODTiBOmajTvh-Ij2clyr1_8TKtiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=CuJFSEsJNVOgz1J3t23Nhn-oAF2b9T56_AgNhj8mj87jfPVGkmQ2T1kVUEIWV5EPQeCYe4gQPEufX6K7Ir8EWVYnM9sXwtOsBTYPLLhpQwhFxyn_1Gydg1SyQfw26Caogi8bxgIFHFakPaMhyXnipeTI-rehdFA8ZDv-q6WUE6MpX1tmwxHRMdq3cYfsim4upbnipwY8RCoDSmCZHIHFsq05npNotRn2q4cjQXhPdbXWsYLVIwLm7IhyuxwFjzXMq5f2RIKHyi9SDWOxugfnlpa0E4RYLuGttuXafXzjHHFQEylqdOY7w9wSWuODTiBOmajTvh-Ij2clyr1_8TKtiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=CKhmRVngaAGrjney5Z4mQt90R_ueW5DeLyXqlawiIM3QM7-95CXa3U_NkahQZmz67XwHP0M_QCLJQHHe1jlGWylyraOG24DiUBTYYLnv_nuNCcSuS3b0NjGIiBWvL4cbr2oQSbtAzqdY6H77a-H9wOxYQ2M6IfrdfpYBhkSwxWhhwNkw-Q4qI6VNFLCVj55PbY8nz82hKyJfCY9nYPSfAd2n9gsWiYcUwG-EJ_NC0E183uycZPj_msu0DJbkdcYioU5dNTSopFc7yIlREgKYIywu7M8PoBmtuZSemW1ENCNp7RbRWL1y7dvCKCcVZU1o8H3oPnHwBxHFx74GRAGZ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=CKhmRVngaAGrjney5Z4mQt90R_ueW5DeLyXqlawiIM3QM7-95CXa3U_NkahQZmz67XwHP0M_QCLJQHHe1jlGWylyraOG24DiUBTYYLnv_nuNCcSuS3b0NjGIiBWvL4cbr2oQSbtAzqdY6H77a-H9wOxYQ2M6IfrdfpYBhkSwxWhhwNkw-Q4qI6VNFLCVj55PbY8nz82hKyJfCY9nYPSfAd2n9gsWiYcUwG-EJ_NC0E183uycZPj_msu0DJbkdcYioU5dNTSopFc7yIlREgKYIywu7M8PoBmtuZSemW1ENCNp7RbRWL1y7dvCKCcVZU1o8H3oPnHwBxHFx74GRAGZ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=MBubMD4y1o9cKBGfxypH9uCSKC2vm-iglRDCzzCJCiUiW9XF_1q_NPYeeQNvI91JrPUDPtb-_PXn8Ffyd6DpIBTDIPFa8R-1YmiL9ntNchqakm8U_-fLNx2e-2gHPgiZrYvDjEbQ4o5PlPNb75Z1IZqfIZcjAjynKNXq7BHg13iuwtXc5o5CL2u1UafOVKkWM7hkFgV9mlEPxrE7IDRq6aH80SzOHG24ju6yYV0jMGCenyPCdGqrdep5zAx8FvwPN4Nk40Py355vOne0q8MbeQEe8BFRXlX2owHzOuHtFHCbo7Z-hgZknJxIKFw2-jOvKQy4Ge-dTJbrI3TInWO2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=MBubMD4y1o9cKBGfxypH9uCSKC2vm-iglRDCzzCJCiUiW9XF_1q_NPYeeQNvI91JrPUDPtb-_PXn8Ffyd6DpIBTDIPFa8R-1YmiL9ntNchqakm8U_-fLNx2e-2gHPgiZrYvDjEbQ4o5PlPNb75Z1IZqfIZcjAjynKNXq7BHg13iuwtXc5o5CL2u1UafOVKkWM7hkFgV9mlEPxrE7IDRq6aH80SzOHG24ju6yYV0jMGCenyPCdGqrdep5zAx8FvwPN4Nk40Py355vOne0q8MbeQEe8BFRXlX2owHzOuHtFHCbo7Z-hgZknJxIKFw2-jOvKQy4Ge-dTJbrI3TInWO2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_MFhm80QPe74Ra4rdrTy0MHSCy3_F-_OOj8biZYDkKpSlowhf0pV7OvPAR1s69TK08BT52MiG51bzmSHiMLsgXI_2eNljTocxFXTiBmS739ONnQ9_PEdiIFO4Se37MlRcjTJfsMD0TZ7mGMNMK7nyNAYaPsscN0PdgdG63nmdPcwbx-MwUmDWRv3M3-u2mdWE5dFeEkKplEtWLeQetVxMIp2ILvWfC3kj8RXeKBiIM2gQ2csQm0AwpwKHO9eghSxYIItOcum99Tn7LbHaFuHW-xmzdFtXerP7_wwlNuP8bdTq2LyM4RbiqsYdNsAZWgW04brQDE7tgKuC2FiTz2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwx3lHSe7p7f-uJ0hNyLt4GEn4ulSclrgYvb7IzBM05qZkqBNtrghMgC3eyhaay1jeiJZ6RSJxQvNAAj_QXCtSq8B16Ltr5eu3mnp72mB7TXkbvCuLlBWezrbgcbGMxRdelI_c0bmXKrLZpga5woCgtR4eIxhZyZOyDKjsjeBl4p8PJ0jAeIQHssvWdzxpQKUOUUPH52rQXJcdzoSX55eV5SCpFtZTG56cgJjbxWA48N74s4anl1N4hXLXae-fuVpxC9GsAfipJS3pQR0dqLZTgnbdqw8zAmhO11hvB4VzqPqomB0UZd8OYIi15JtjtRPfQ4fVFNsil5Bh_eRi5vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajsKo82VE_IeocRsURqfG7mQqnW7whs5138TEoqFs48VHBkefvJ8Rgz8uWBoZmj3w5KIecI6K5Ddhr1E6N4vEnWrnPNrexj44ce05zSbkUyoPOaMFZmsEu4aKsmDEoqRYpTWcu7Bne6OFB8wAjgvqaC7NaUsXVFKS5BJwhOxyQOelhK6I1qWMl32ZetmTY3pyqPPQR9KmkpgDmIAJaZzKnlQtDB2H1vZPEG2WOiwS_PqLtXVfi9Fd9Fgxa0GHtW6xm2fJA9tnCapaeBDxmTAIpN0ywHfqqcXGk-hUMxTOs8uL_3eUvVezrJVYP_30tMS7H4C-QQkaRfe_9e4EzRTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUrz__wNOkuLtiVylowwzKEUbO_hLJOugZ3FVwakKWVCVSM0I_5qZ08F9Bm-tHP8VgoWZIKl2yXSrOBXy3_n-GyACtldkh-5DG-FaKkZ0feQ1y1rZp9-bfViGFjLeGu4l_tdj-7cHn0H6xkJgd2P2kqBx-X8yM7kYfPH1dPI1bgLJx5-1hFHu0VG6S7BT2NNLFVWci4X8vfOINXMyNRLBXYmUz9fbQJD68-1H0h-oyxv_fPmLOa4_7Xai5vModZOf6GdKnuytWGjFgl-xXcfqFvpJ6JWkM5ThlNiJ9sAqa83I0QkBQ9DLjOJGrtN9MckFq6UhECkRjPmAm_mKJF0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck_kI87hNkfwam3NlxfemeJ_sgQDYZZffmTFokNIoDwFsWKY-i_OUEKMLijs5mtU1BySIZTeFXsi9Q1rW6vkvR0PpH0VGVfceEyn16rJ4mJKullYtSxk2r88I5a0xqwmiimox4eb3bWKe7CNGMizfBjDB8TlIHFJiOP93oWj9_oM4-BzOx5QALnTGcbTcJD-zukaJhhJjBeWaR5sa0e1_4CpSiJA64ubBH3tyDJ9OBpOiG51x-skdqrUgh1uK2_qoqAZUhGtmIWjZnWF6PJh6CPwVUvah5m1-8xVNT-UrGz6lI_Gx2JIeEHpGf9yz5Gevy1dUHNQyi66JuGe4MfoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMhcF0_0c4eIxzgUI_NXh44ixxdgYTlrRf_IQxfXMMm8pfaCHWmHKXzwh3e8rU5jh-K2IezWK1gNgVEs6I794DwxDp3I3i7W6hgKK40QUsb280BznmEuJ-g1_csGFqzYXlxJY74ECl2ZsYmkSUMKp8dPqm4RwDrdysbwMQQ_neHtwtr7THOk9XyJS2g3f-UJbIl10_s4ursiABffZEx1nWmhwHNRWMdxVVw0u87kYS3e01gKijyG8yFlAtX17S3i14BjjcZgrvwK4zVk3PI9f5yeEtn3ZIUPDmlKKEdZMgHikaEfcWoneuKImOrnr8PSdc86wWz8aazBXrASu_gaSDOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMhcF0_0c4eIxzgUI_NXh44ixxdgYTlrRf_IQxfXMMm8pfaCHWmHKXzwh3e8rU5jh-K2IezWK1gNgVEs6I794DwxDp3I3i7W6hgKK40QUsb280BznmEuJ-g1_csGFqzYXlxJY74ECl2ZsYmkSUMKp8dPqm4RwDrdysbwMQQ_neHtwtr7THOk9XyJS2g3f-UJbIl10_s4ursiABffZEx1nWmhwHNRWMdxVVw0u87kYS3e01gKijyG8yFlAtX17S3i14BjjcZgrvwK4zVk3PI9f5yeEtn3ZIUPDmlKKEdZMgHikaEfcWoneuKImOrnr8PSdc86wWz8aazBXrASu_gaSDOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=Yaz6wZskWoMyTM5ER4C4XjJDbkD74bSgotxDebStOasc869ZEUZD7jDHlcOXZh-mbIH0ghj9n0_EtkbrmYygQbkbHz53qirsjDBHuyv30LCzUvfqaT9cZi_Q1UBn8jJR1Q6ktp95y_7I4pe8x5UAmk0rewik1ptQv4_kUc7vBR5bR-vYWx8bs_CqttCcZzb8LGbiPamyPVw6NQVk6vFNa4Svfx1ezyHCikfY-mwn7lV4chWVEUWniU6rSzGlThUkSxoGOxXkzGZhYn1QBJ9R-pQAWGbkyVvzW6Vod043FJN5dlI_Qqj4_-DAoMTalZAbuh4TNK47uf8akH5rJ4qtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=Yaz6wZskWoMyTM5ER4C4XjJDbkD74bSgotxDebStOasc869ZEUZD7jDHlcOXZh-mbIH0ghj9n0_EtkbrmYygQbkbHz53qirsjDBHuyv30LCzUvfqaT9cZi_Q1UBn8jJR1Q6ktp95y_7I4pe8x5UAmk0rewik1ptQv4_kUc7vBR5bR-vYWx8bs_CqttCcZzb8LGbiPamyPVw6NQVk6vFNa4Svfx1ezyHCikfY-mwn7lV4chWVEUWniU6rSzGlThUkSxoGOxXkzGZhYn1QBJ9R-pQAWGbkyVvzW6Vod043FJN5dlI_Qqj4_-DAoMTalZAbuh4TNK47uf8akH5rJ4qtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=DK0ElkcH-AKSNspTaQicqlCd8Zv6FZtrA4WBdq3_BYBnX8WzXXda7jFzMBRIKy1HD8lWG-MyL7oJPI1GgFySSBZ5nCSApqbkEerzckzJgVo7HhkfgyOIVAi0PJBymIqq1xCyaiNwTwipBCYH50L9YoGwu7JLJFQSP9Olu03bius7emId1hSRtxM78cmzYFnMDTraOLv4Cigsc3J2ZLVjBU2U76qpH2JnJxBbSYPWScJESO4EGLLtoyzxAoSLllYbz52gplB49ycl1fM7Zr-YIiGFe9ocx6aFg_VqsAjTM5ClqRqONtAWMv1k-MkaRx5SUDO0xsNYXrffCxIfjrSoujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=DK0ElkcH-AKSNspTaQicqlCd8Zv6FZtrA4WBdq3_BYBnX8WzXXda7jFzMBRIKy1HD8lWG-MyL7oJPI1GgFySSBZ5nCSApqbkEerzckzJgVo7HhkfgyOIVAi0PJBymIqq1xCyaiNwTwipBCYH50L9YoGwu7JLJFQSP9Olu03bius7emId1hSRtxM78cmzYFnMDTraOLv4Cigsc3J2ZLVjBU2U76qpH2JnJxBbSYPWScJESO4EGLLtoyzxAoSLllYbz52gplB49ycl1fM7Zr-YIiGFe9ocx6aFg_VqsAjTM5ClqRqONtAWMv1k-MkaRx5SUDO0xsNYXrffCxIfjrSoujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=aXnim2fdzhh1mowtSoIV9Tx1MBaXNgFD9zhyoBkqpUGNCTLFt5gNJXQnBatBMAMUasLVazm-nHnPqRhQLEfkDOtBadCCExQxTH-1SD0OQb1Z3EGuKAiqCg2ByMsB5JX3L572cgnDIAymLTfMdzHd53V9UWFFiRi1Ygx5-XbRHtVWhwiF1zPu23rJ2dSEKp0eEKdrJGkQpmd2sPqYaTGa3CjUo6S-OXlIYAQhfMDGfFs3Z1q-au7_qgC94BmzJPNqM0rCSjDV9Njemo6JnKRo_tiyf7i76Jv5la0xa5-Uz0Bypc_lGUM3300gqbGzRu7iLxjEPyD1f80Y6XzNdmn9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=aXnim2fdzhh1mowtSoIV9Tx1MBaXNgFD9zhyoBkqpUGNCTLFt5gNJXQnBatBMAMUasLVazm-nHnPqRhQLEfkDOtBadCCExQxTH-1SD0OQb1Z3EGuKAiqCg2ByMsB5JX3L572cgnDIAymLTfMdzHd53V9UWFFiRi1Ygx5-XbRHtVWhwiF1zPu23rJ2dSEKp0eEKdrJGkQpmd2sPqYaTGa3CjUo6S-OXlIYAQhfMDGfFs3Z1q-au7_qgC94BmzJPNqM0rCSjDV9Njemo6JnKRo_tiyf7i76Jv5la0xa5-Uz0Bypc_lGUM3300gqbGzRu7iLxjEPyD1f80Y6XzNdmn9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7mGSutWYe4uNZe5vzWuQgev89Lh2IZhw_QUSNVkPSz8ctpK3KU07yRgzuM0V64cAmmaCoB-NhEUtmc4lNVHXfD23oEafrZKZMEDOFDfBkzFI8Bjv-EgH861r5nWBwM5fHH91Uqa3ItcN6KH_cFIEujuOxDD0taddAlXOUk2qQwUKKytOlRcz2OgQF62Euch4jm1CHnyAkK7UDwEpBrZD7qu_lnfHs0mZ1EZR5CQgg_MswfCTSvaF7lYU2CWp5P6WXbprrK82XV-6GSJhzwZ8P0S_g0CCVEa35Rx2uB4oz5DWUJnP6giA-CRDkmciGoUlwCOVipfwfVu1TM0a-KWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=VXr5NHUK3whtM0ZguWT549nDZDxf6MbxhapM9eE0GTOrhmc7ex-J7PCXJ0TmATGeFUXisEqU7Zk-7WrvqohX0eX6bd3b4UehytGnovPzJ5Ba8w61p8VFc4ByEsqyCSrXpp4EwK-KhuwTWn6WbcOuakn6d-PrAED1WqxJlJL8SlsNuhQ19ZX8fg7cgqsabseqrqbuWpgnynBkAKk8Y7NMhQKeq7ynMIiIOhpwcCLT5qWgEptJAdll0ayfcNbDEp2C71TXtu9iXlv50uvoGzMWDTlqKNfINBgRY3DJvYQWauuPMKYmSk8bt8RGuEC3eNs9S8xC2hvcSFVPfDjsgA7emQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=VXr5NHUK3whtM0ZguWT549nDZDxf6MbxhapM9eE0GTOrhmc7ex-J7PCXJ0TmATGeFUXisEqU7Zk-7WrvqohX0eX6bd3b4UehytGnovPzJ5Ba8w61p8VFc4ByEsqyCSrXpp4EwK-KhuwTWn6WbcOuakn6d-PrAED1WqxJlJL8SlsNuhQ19ZX8fg7cgqsabseqrqbuWpgnynBkAKk8Y7NMhQKeq7ynMIiIOhpwcCLT5qWgEptJAdll0ayfcNbDEp2C71TXtu9iXlv50uvoGzMWDTlqKNfINBgRY3DJvYQWauuPMKYmSk8bt8RGuEC3eNs9S8xC2hvcSFVPfDjsgA7emQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=uudz9iutLgXPSk1u8bVAz5CwQdE9dia1rwHCRRvWOEmIwxaoTtRexTm1MmrzL9matk_iwgmXmFMc3N_n82q9X8l8iekJjLjwlHlmh9uMd6x7aEte5LtD6I_xKUL3Y2bq6936IhYm5-BZnFW6N58m1AlGHKxRVyPSagIavnidiqsrGrQqlfPKjTvXwILMVg3JC_yGVBINDIgUlfGyI6ZjDdSxwneZkyUbP2dv6ehgUKKkGDqHEIH675QK_OllMhN1UuveXsuPu7FnU55AfFwNzE_ePDRnPFTClZ3rFt4Py27QqT8GNLww6vAXWJ_BtEJmQbWtH3zY6hc_GrEMbJGPng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=uudz9iutLgXPSk1u8bVAz5CwQdE9dia1rwHCRRvWOEmIwxaoTtRexTm1MmrzL9matk_iwgmXmFMc3N_n82q9X8l8iekJjLjwlHlmh9uMd6x7aEte5LtD6I_xKUL3Y2bq6936IhYm5-BZnFW6N58m1AlGHKxRVyPSagIavnidiqsrGrQqlfPKjTvXwILMVg3JC_yGVBINDIgUlfGyI6ZjDdSxwneZkyUbP2dv6ehgUKKkGDqHEIH675QK_OllMhN1UuveXsuPu7FnU55AfFwNzE_ePDRnPFTClZ3rFt4Py27QqT8GNLww6vAXWJ_BtEJmQbWtH3zY6hc_GrEMbJGPng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=KZ4sZJcM5WcAlkH13JgXm9SoSm3YyBlZWgEcVgy737XtiZu--1Sf4ekKLQaS5U_M8TAzK8glHMXxAn_GZ4P_7zNQvwiRbrCzDYur5ajQ9J2CTQ08IwYyCsosMsYQp6weiv0v55NvuH5cAeer1LvyHVl-Mq562Os495gfpdNcIUl-yuxg5t0CPem0X4XP3PSwezUO7ycg7I6GZVoSvYssEkvUbU9t5QpmkG-H_xSlgYOL75yMGHJROYlLN4chjkT2XVoKo_1mo8YKoF0Y0golPD_uyqBjHYDiG5GGs3WFuxdUmjErmVH1IzecQFQi-WiL8ffzxx__eyEa0kB7q2CF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=KZ4sZJcM5WcAlkH13JgXm9SoSm3YyBlZWgEcVgy737XtiZu--1Sf4ekKLQaS5U_M8TAzK8glHMXxAn_GZ4P_7zNQvwiRbrCzDYur5ajQ9J2CTQ08IwYyCsosMsYQp6weiv0v55NvuH5cAeer1LvyHVl-Mq562Os495gfpdNcIUl-yuxg5t0CPem0X4XP3PSwezUO7ycg7I6GZVoSvYssEkvUbU9t5QpmkG-H_xSlgYOL75yMGHJROYlLN4chjkT2XVoKo_1mo8YKoF0Y0golPD_uyqBjHYDiG5GGs3WFuxdUmjErmVH1IzecQFQi-WiL8ffzxx__eyEa0kB7q2CF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=IYRAhAQCbBPB9BZrULHn1Y3KWLR1R4AZrst1A0Nq67Ws66Tu45FlhvuQpiJ_axgz_6N4MEKSPBYBVs-9rElV8AopYDYWR7MCM7WvV3FR_KfxZ7jx4MTnvvMIpw0SuZeR9sJumQh4ua5_--a9wiWFrboPCd91yh1cWK45UiUOYTZePg3M4LFP6Giu-9gl024kzAj4vvWn0FCgg448nbO-g6Ytpz1cYbMElXHiTZ2X8WH_U9juerOfSTFIFPNoi3SiLQVjG2Llw-cjqojnl0wyIVvdVv91FTJtQ8BrHOCTiF0Up8hWxR5p3UZb-jEmyOZbxBLfA0kT1enaxIzG0vEc2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=IYRAhAQCbBPB9BZrULHn1Y3KWLR1R4AZrst1A0Nq67Ws66Tu45FlhvuQpiJ_axgz_6N4MEKSPBYBVs-9rElV8AopYDYWR7MCM7WvV3FR_KfxZ7jx4MTnvvMIpw0SuZeR9sJumQh4ua5_--a9wiWFrboPCd91yh1cWK45UiUOYTZePg3M4LFP6Giu-9gl024kzAj4vvWn0FCgg448nbO-g6Ytpz1cYbMElXHiTZ2X8WH_U9juerOfSTFIFPNoi3SiLQVjG2Llw-cjqojnl0wyIVvdVv91FTJtQ8BrHOCTiF0Up8hWxR5p3UZb-jEmyOZbxBLfA0kT1enaxIzG0vEc2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=q9DbEhneyecWfDt9RABAJK-ZMf1LJFvG27UopJux1Ibob57KceXCoAwNCFjeu3RYoT3vGVSRhAXACFh7zKw1wbXJcc9A_ecFs08VxNozkIo_eZjiqn70vRoFpiSA5wXQ6ZdZxWSaUG6yX2fzkt3t7iGO4ajpvcEUfwnodSuteLIftWG4os2kWKfnw9GMMx0x8skbBG4XUZ9l5G3yQM1Z2z5woP7twfGja_mDuVLvBOi_Em6Dq422VObDcn4O_P59pqxl9uVWiAe55KuyOevwpcJwYPZhIbYp4anLg9jF2ZiFUvwpXv1K9VEyoP40bZ-JxRw9zQ4UUCCzvqIPPDgkQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=q9DbEhneyecWfDt9RABAJK-ZMf1LJFvG27UopJux1Ibob57KceXCoAwNCFjeu3RYoT3vGVSRhAXACFh7zKw1wbXJcc9A_ecFs08VxNozkIo_eZjiqn70vRoFpiSA5wXQ6ZdZxWSaUG6yX2fzkt3t7iGO4ajpvcEUfwnodSuteLIftWG4os2kWKfnw9GMMx0x8skbBG4XUZ9l5G3yQM1Z2z5woP7twfGja_mDuVLvBOi_Em6Dq422VObDcn4O_P59pqxl9uVWiAe55KuyOevwpcJwYPZhIbYp4anLg9jF2ZiFUvwpXv1K9VEyoP40bZ-JxRw9zQ4UUCCzvqIPPDgkQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=DrQ1mtcMq8OvFh1RDyRu608qK-w4bdyBhIMo06UWXOgDSejyt0gOC_Wq63xYrKXm2BLJRde3thUnhNrK7W_bRorI6Iucor5sfgMT3FzaqD4gTjVA8HstKf7kdCih_E1Sb4B0aU4yo0pg40_nR61wtr7dmRdAssmmyE0lzjGss56aiqKJFWGYJXc6krjCivum2ea_S9LBuiJWTtjtMV4kb_cU7BOA-sBUBajBDZTWUMpejN0RaiqMqj9wyuVOJMGdgXW3yDWTimnp_vov6SAf7OqT7dYfg-XsUSerVQ8_JpFvWqJIE7mMxzstSqPmBl-zlEkW8SZsE_2RxaOMeisnYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=DrQ1mtcMq8OvFh1RDyRu608qK-w4bdyBhIMo06UWXOgDSejyt0gOC_Wq63xYrKXm2BLJRde3thUnhNrK7W_bRorI6Iucor5sfgMT3FzaqD4gTjVA8HstKf7kdCih_E1Sb4B0aU4yo0pg40_nR61wtr7dmRdAssmmyE0lzjGss56aiqKJFWGYJXc6krjCivum2ea_S9LBuiJWTtjtMV4kb_cU7BOA-sBUBajBDZTWUMpejN0RaiqMqj9wyuVOJMGdgXW3yDWTimnp_vov6SAf7OqT7dYfg-XsUSerVQ8_JpFvWqJIE7mMxzstSqPmBl-zlEkW8SZsE_2RxaOMeisnYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=T8IC8I36ZpqqTD4Dxk-a5bYyuJdsx4bAp5Zs7f7fucnKhQ8bQR-ReZXSs69_-QCTfbnOTtw45lWm3fB0GgRG8cu6PiGsEA-1P11F85ax3XPMvY_1cT4QXF4aqjaHJ0hJrXOAboSlLUGLw6n4VGj25DEJsfdxSCpElFi1-eUjZlnIa9H5tRwRagJB7bTnZaJqaEmAU4Td0wNOQSfjQ2bgF9hh8CNtlRRSNYg-Xs54CdbOcmAK0npO-_NTPE4hJH3H3UOuW7DB0WDkfL1zUhJiaN2Bf36b9Vfg4JDvimup7hF4De0-aCE8Z_iiMYiv9S7BuLR__11Rc5NNsonMSZ9hoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=T8IC8I36ZpqqTD4Dxk-a5bYyuJdsx4bAp5Zs7f7fucnKhQ8bQR-ReZXSs69_-QCTfbnOTtw45lWm3fB0GgRG8cu6PiGsEA-1P11F85ax3XPMvY_1cT4QXF4aqjaHJ0hJrXOAboSlLUGLw6n4VGj25DEJsfdxSCpElFi1-eUjZlnIa9H5tRwRagJB7bTnZaJqaEmAU4Td0wNOQSfjQ2bgF9hh8CNtlRRSNYg-Xs54CdbOcmAK0npO-_NTPE4hJH3H3UOuW7DB0WDkfL1zUhJiaN2Bf36b9Vfg4JDvimup7hF4De0-aCE8Z_iiMYiv9S7BuLR__11Rc5NNsonMSZ9hoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=XrVhwDweBe9CaBdLU112l1kVo4ARqvxbaIsaky3aD37C6f5EO7XnLTKadGYfjM3pRKgW_o02o4Kh-dBrNQtcItOm6pGE85UCrfKokiWgSo688ic7j7xJk_Sk1mb1KoJqEDW4zmotNfMfebPIngYBkR3IJmynGHPyoF1zb66PHp9-8uKwzVOht3MkVYihyI9vGqSrkFITEQuI-0PnBgBkGX1L1XBnu3UMZkoUyELBdoPNYp3jzBkG007G1Ql_WWteE089k_2oRjAyzvpLjRUK81IDO6o4Z6mrQ3BGRVYtJc9xIttTsLQz4gNnBcmGikclwVE8IrBHwwk7Sp2PSTJf1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=XrVhwDweBe9CaBdLU112l1kVo4ARqvxbaIsaky3aD37C6f5EO7XnLTKadGYfjM3pRKgW_o02o4Kh-dBrNQtcItOm6pGE85UCrfKokiWgSo688ic7j7xJk_Sk1mb1KoJqEDW4zmotNfMfebPIngYBkR3IJmynGHPyoF1zb66PHp9-8uKwzVOht3MkVYihyI9vGqSrkFITEQuI-0PnBgBkGX1L1XBnu3UMZkoUyELBdoPNYp3jzBkG007G1Ql_WWteE089k_2oRjAyzvpLjRUK81IDO6o4Z6mrQ3BGRVYtJc9xIttTsLQz4gNnBcmGikclwVE8IrBHwwk7Sp2PSTJf1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=ZWWNLuQHTiQm2bZEpDR6oWXPPixWIbzbzyHPcflaFT5uOZKCroP57g5JSOUeemrLpHS01v3UDqUSnJGcPyFirCzkRYQNhEGJkCJVrzNTWfxNDS7tDRsZ_iWKq33wa27gREiCv1OwheNgsoB1iYyjHDPV4t8ro5SHiKWsYGqYn2b7doeepW0Dv_fBfPvphSpLENoL0E_utQfCn4sKw8TNPkIVmkOYqCsQj1MJWaVNnlAVvmiUOGG8mdVycMU2dR8LLMRrp_U5Gt3gyvq4zIzMPK7gNR89nfSHDdQRK-f8o8w5IXnmW3kGajhOMfo9l85mqOkQEdQQXyLLIVaKPlOlPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=ZWWNLuQHTiQm2bZEpDR6oWXPPixWIbzbzyHPcflaFT5uOZKCroP57g5JSOUeemrLpHS01v3UDqUSnJGcPyFirCzkRYQNhEGJkCJVrzNTWfxNDS7tDRsZ_iWKq33wa27gREiCv1OwheNgsoB1iYyjHDPV4t8ro5SHiKWsYGqYn2b7doeepW0Dv_fBfPvphSpLENoL0E_utQfCn4sKw8TNPkIVmkOYqCsQj1MJWaVNnlAVvmiUOGG8mdVycMU2dR8LLMRrp_U5Gt3gyvq4zIzMPK7gNR89nfSHDdQRK-f8o8w5IXnmW3kGajhOMfo9l85mqOkQEdQQXyLLIVaKPlOlPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=kDCk8i4wRiWZwvaPZ7NP2NiVvd3b7VmeMKlSQ7909MR2jbY1Yn_176AfTGW4xBZLeWa7EInUhaFFi78Shbs99kgKQrf8h6VPZ0Y6dEsKL7-b2f5Kq8AnzwPW4d7nujj0t9zCM3MS3rFr1qewr2MWnzG7P1JhEBAgHVUTVMZLVJRoFu_yTNHtIUyneqPXNVB5pQ6IGv9gXFlHSq_H4-AburhpwePmvNokMVtnEUHXJ4WkQHnkLdHFW8jsCPiQCwZtqAe3ahHdGVLd33nW0ZTFm9xllIN24yBCM0MpzR18jZj4SdYKYj0aRZWPMyU_81NizZHe-RT8WrsGOTAChCfysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=kDCk8i4wRiWZwvaPZ7NP2NiVvd3b7VmeMKlSQ7909MR2jbY1Yn_176AfTGW4xBZLeWa7EInUhaFFi78Shbs99kgKQrf8h6VPZ0Y6dEsKL7-b2f5Kq8AnzwPW4d7nujj0t9zCM3MS3rFr1qewr2MWnzG7P1JhEBAgHVUTVMZLVJRoFu_yTNHtIUyneqPXNVB5pQ6IGv9gXFlHSq_H4-AburhpwePmvNokMVtnEUHXJ4WkQHnkLdHFW8jsCPiQCwZtqAe3ahHdGVLd33nW0ZTFm9xllIN24yBCM0MpzR18jZj4SdYKYj0aRZWPMyU_81NizZHe-RT8WrsGOTAChCfysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=cnrwDsooztRNbEDyG3cSpRh1LrN1NdR7sqYnA1ja1jxkOUZZ1xLVStHvYc_uj4oNj3fvIOGFvTFUnaWi6VuFMayOHTp3OiPDzup48EpMTiXrL6_oIGZInm_Qio0F_xMik2uiEj2-13sn65uOdVHBNb9M4UoMzMTz4u6YZUjoWTzTJ4eVa24ssCc2V2S82GQmKs6QfCfJz-QhlP9O-tPwxJfpid9ugpxRXVk-Ow9sFvTxiGEZqQ_d7Yyff-W5rrGFlWS-bboaqBLwKpwlT-9HY6O34Avr_vnUERS_EiMQ79tZhXdwk_lqLoxxYrRi2Eg7UaYGMKEZ8-rzJTzCYB2Ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=cnrwDsooztRNbEDyG3cSpRh1LrN1NdR7sqYnA1ja1jxkOUZZ1xLVStHvYc_uj4oNj3fvIOGFvTFUnaWi6VuFMayOHTp3OiPDzup48EpMTiXrL6_oIGZInm_Qio0F_xMik2uiEj2-13sn65uOdVHBNb9M4UoMzMTz4u6YZUjoWTzTJ4eVa24ssCc2V2S82GQmKs6QfCfJz-QhlP9O-tPwxJfpid9ugpxRXVk-Ow9sFvTxiGEZqQ_d7Yyff-W5rrGFlWS-bboaqBLwKpwlT-9HY6O34Avr_vnUERS_EiMQ79tZhXdwk_lqLoxxYrRi2Eg7UaYGMKEZ8-rzJTzCYB2Ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALjjIE9HC43GyKvGPuxiZN6XYFPtiPN1zuQ4qzaNBkp5GIlNmq502LB1zIo30qhcrD_DEXpGIV9D_tFfnkn0zflPtclqGnFp5pZaUU5Xt2MoyuL-XH0Cs0vPA19ArSsQhjCSP2Q-vTKGs-ot6sb_40DFsIf9VJMvgMHPBWkn6emjdwGvCtuLtdEHClC1xtSrNcBExfFRErrJFfwXt0gnhbCWIB2Xc5mcMuu9ReWdbWCHeLSsB_cFBFvVvgLXLgWo4MxG-yplR0ijRwrd2GgfOetVAnmfw0-YemahajWIe60YrpCswP7TVqYppHt14g6ddz4iMqGwdcr0-6jUXmUJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=lsICXtxE3jue43QwI4C-Gat3j_QJfXO8UFA8aZ98L7Vyosi9rHE6tS_6WmFXjTxf_wPACMtYlT0Twjc3AefqJDBAUdJImNTI2p5Kf7vmFRKeZKjcoUypaV2ITi1B9dKikF22kn-kmfBmDv6Om2hRBSn9MZq0nX73UvnhY9AsXIilBEScWgo1z3HFpZIA-g19xHIHejaLss0B2lktAu29Nv7q_jBqyYwYpwfBkm1VZg84ypxQVvw_mEI6QMLqfP6_ouRbZ3HCJEUnBXY_KWGqgdsUcIVtebXTgEVfu1Pwm1VO6O4SfPFwTTIoYhL7BMxUc7FEdYJAlF2f_TMB2vzV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=lsICXtxE3jue43QwI4C-Gat3j_QJfXO8UFA8aZ98L7Vyosi9rHE6tS_6WmFXjTxf_wPACMtYlT0Twjc3AefqJDBAUdJImNTI2p5Kf7vmFRKeZKjcoUypaV2ITi1B9dKikF22kn-kmfBmDv6Om2hRBSn9MZq0nX73UvnhY9AsXIilBEScWgo1z3HFpZIA-g19xHIHejaLss0B2lktAu29Nv7q_jBqyYwYpwfBkm1VZg84ypxQVvw_mEI6QMLqfP6_ouRbZ3HCJEUnBXY_KWGqgdsUcIVtebXTgEVfu1Pwm1VO6O4SfPFwTTIoYhL7BMxUc7FEdYJAlF2f_TMB2vzV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=JEe2F4L3zGAo6ZcDJAHExJ62_tR6IalplnUkQOOS9VIb2rJjeiO4jlVDHW8MtWYUbDrfiDv1LHQyiEjj76cU0Vjmff_o9QXJS9yvjsKjk7g4eHyyhzXTDPCG-739aSKY0ZGjIXwSX6H5bckSjnCqiNgRPspd1hT_Iojh4NgCGXIogLLYD9C6SO1hDVUKII3-uvQ9QDeR_hzqx00mqNwwq_cjKK7HYYsDQ92s3sqPnY20uoIYI-07pUFfQR_RSgi9kJkuPWcB61moDMzaM_iKeV7RNT4-N1aUGkj8kQP5gEQ1h8Wqg_bThtuBdzS2dqRCEwqlP0YBqGY3FrXx6OBggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=JEe2F4L3zGAo6ZcDJAHExJ62_tR6IalplnUkQOOS9VIb2rJjeiO4jlVDHW8MtWYUbDrfiDv1LHQyiEjj76cU0Vjmff_o9QXJS9yvjsKjk7g4eHyyhzXTDPCG-739aSKY0ZGjIXwSX6H5bckSjnCqiNgRPspd1hT_Iojh4NgCGXIogLLYD9C6SO1hDVUKII3-uvQ9QDeR_hzqx00mqNwwq_cjKK7HYYsDQ92s3sqPnY20uoIYI-07pUFfQR_RSgi9kJkuPWcB61moDMzaM_iKeV7RNT4-N1aUGkj8kQP5gEQ1h8Wqg_bThtuBdzS2dqRCEwqlP0YBqGY3FrXx6OBggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=LXQIBqTbOOzgEUQxyBmpPGmkcd2Bl2yg52DoAx5Kw2xb0_YFgsy9k1I3IQiNfl709G6_HhHiE-UMEjzRmm0ecW9_lhV28SFhkwpyx7B9_uvSPNJoJICKlNqtmczb3z6qTGIKRhGOrOEWFTq75SaqFf05RxyhGNJahbGG7MaAzIN_bGARP1kEcsT6v9oJTn5AuQTLt_Bb-cMyBDbUDc2rXdq7Xuf0Uj_pKHL-c4bGu2h_sNSoOqK5HwRGuZmr-x-BTSWzTWAVlxRTrLj8akfE7EEpLbmQTjdPBbip5IsZViudUEQiXhupQYzpwWcfzraf3peQKM-ZLibjTSdw6vVi_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=LXQIBqTbOOzgEUQxyBmpPGmkcd2Bl2yg52DoAx5Kw2xb0_YFgsy9k1I3IQiNfl709G6_HhHiE-UMEjzRmm0ecW9_lhV28SFhkwpyx7B9_uvSPNJoJICKlNqtmczb3z6qTGIKRhGOrOEWFTq75SaqFf05RxyhGNJahbGG7MaAzIN_bGARP1kEcsT6v9oJTn5AuQTLt_Bb-cMyBDbUDc2rXdq7Xuf0Uj_pKHL-c4bGu2h_sNSoOqK5HwRGuZmr-x-BTSWzTWAVlxRTrLj8akfE7EEpLbmQTjdPBbip5IsZViudUEQiXhupQYzpwWcfzraf3peQKM-ZLibjTSdw6vVi_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSgBH8M0Ei8XF17qszYma1HN49at8ZEM8T1AfAL_VZrNmHfV2kSGrMcjLnMruYXqKEp2zAI2oa5aAYheG7db_UGZFJmtcltyWbBWiVcgtNFeUz9NrwXIm20Y_XHryN33ChBkLqUc9kbCyg8Knvi4L2noFeNz10yqxwLheqs9NZjYEuOovggyDVVvCE2qKtb4KDJLdjDJIOYagNFR96R-8go2_I1nsmNW9NPa2m1SkcE6JpfPUsLPM5RyoscaAT1BJgaR5lvMNnjgGsTqlbOWc_Kpku-EYNyatI2_NpJo2AlXPaIycN2M7Tavc5uw7yLAFi9jcxmuWDgHg9mPZkvYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=cSa_WJ6dls3R798jUfqAoi68oE4AoBQiqVgiu4_ME6SqHNgbWoyOlLkd1-SL76_PBJNbhFuxcrBjvmvxtjLYR1EiBAR7mmEQVU3NVXpxW6H58XIJl3V6001bhoNskvnmWUy9urUt71rwsVnjTIQ_6oxif-H0m5Fhc4OqhvX8OyenL2m5saeiZpKTOydOaCc9qNOm0zjBicr3QqNgqTmWZpweSblMb2iPNfC-GnynJOXJP37LeX0u_xr6LwEG8UXWT_CIIGVW0HCHos-Vrp1lw2wvWWobsWjlDveacj09rxGww0Jzmaw7X0fY2DjN9mCmIQiU3hm5UjvGwn-Bur1nQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=cSa_WJ6dls3R798jUfqAoi68oE4AoBQiqVgiu4_ME6SqHNgbWoyOlLkd1-SL76_PBJNbhFuxcrBjvmvxtjLYR1EiBAR7mmEQVU3NVXpxW6H58XIJl3V6001bhoNskvnmWUy9urUt71rwsVnjTIQ_6oxif-H0m5Fhc4OqhvX8OyenL2m5saeiZpKTOydOaCc9qNOm0zjBicr3QqNgqTmWZpweSblMb2iPNfC-GnynJOXJP37LeX0u_xr6LwEG8UXWT_CIIGVW0HCHos-Vrp1lw2wvWWobsWjlDveacj09rxGww0Jzmaw7X0fY2DjN9mCmIQiU3hm5UjvGwn-Bur1nQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YunsZs1x1PE1gyy9nyDQY8QvzOP_Qae3RdvDQInvXLpCYQejjTU0J8K2jtmLsIqGMqep0zwBimaUXfHwIuEZ3_kFbPvvKgidVTqzoqKZ4jHp03Mwq4-Z0MEjeFBRKTdAcCEf0SemoiYeqEBu_OBP3op1Yi7vMzGXgfDZPXbTSOZ9ik1fh7Q9KJUzb6Uv5eC2cEyXiMjvOEU4PkdimPgwWlWwFNHHufeuxoLHMh7nmaUuzvmOGxuMQn8fW9p-VOejfEh5zny6QHAvl05F7Cx4BJoMO6RTLa7uXYH4BntWszberCJx7u46wWQVGwTd8TUWJQAXjc2HB1t45LKa0ZSN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtDTutEjekMy-2YntEcJWQ5xsFp0ZiTIEzY9zz-AMOQDtlPxN5Esq7HvJAhhJVSMrUDa6BmEgnN2XssbGCL6g5C7B2zRg5jMrqqLclrNGlxmUlVgIGnjPLsVJDI9lWua5F0DDG91PRh00dwVVl_lpsS6MPeXMRs4l_B2f0kZPvyC8-4DLfd-IVqPW0euxImgg4ImKgIDOvJlF0E_H3JgkMSHFWLwa4sh8mkNVjCi-cB871Mc2xTQwsYGVV_DrAw3j8BCDr7NLMJV5UnL4lvAbDIipl367d5d1CohWAhy483gCcpy84EyStBiviGdTFfgNlpjjpzqHobm13rsw3KH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mi0hG8PgUwtohIf6qhlXeWGCXLlJqEPyWiTnO7suCLTk1KA_CES8vbhd5TNWhOD_lC17ZOwiXVueEyhY4uRB1IfrNB1DZmr7e6yKmgtVEej3QImVkjrjwhbXUlCEJx0jTtFGcaz86zC3IoT4XdtsnDzS4YPlKiGffbHTFRxyeP-l0Dk9u1gLftY5IHmQYU5QzWleljJCf9eNcmCPgivTU6AXhlRnA2fc5p12veIJgW9wZ_IHr7uCgLgiHjyoLNkXBZ9erO4vVUiHLbkDhHjOnWE6DD88X0tjf7s0jpzTO2G37BD09pzOT3wemastSRhVPT0H2F08H76NSyLWN_zVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHMgCot5VCQyzz2eGhyACcQhrhmrr7WwMV_LEJGl9HhIg0-v9IsNPO6C1f-wbDEytxEZfFEpXk0bomY5XHr5ksEwPbqaT3Ne_tW6tg8pNlFeOVKRgNfjAnJ1AXSPUA7l066cw0kAN-cyVr_C3M1GlSJs_IOjFEUlhsMPXqmEEcMD69_zW1P9tWJg9SoHfaWZ_EnDEklJUTFikQyIQ04AnmffkqbP8GdvENtMVKcMd8tK-Vvjw2EoFaNhMSJEl8Zp5YWRjQ4zZNEqDm8ao8DlcoY6DPKVkSsFsK4je7FQWkNfvnXvW-0iaLjptZl3sK_PFQJ-tK12fB53laoPVKkd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Li2fCAJ6IEc6eKiwbzYhOjqwuxeg-DA73aFAigmrUCqGWo6psvuv3fFWNQ7-8TnZwgp9d77WU_ZGcKjxjHJVizQDqi1Qo4qTp7S5n2BFt0tmuDFGXKQfN_k-n7UQd39JOwqnmQhGCATWE1VQYhWfuC84AO0whx8Psi33NbNOYPjDAqKBqhByUsxnvMogLC_nCOGY4JtOkokTNUF9Dpfzr2w2OE2YoTlPNogqx5MwGi8HZAFAeICnoZ1sPrXJBY4zH0meNL7qErFhAqaeea1rMjnXkxazEWzhhmXNptNlJKhQawmLMntCHt9rbd_ucViS3atPhVDahBKO_ixloxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=CY4KamZuY_vu9EjvV_YlJNFJ-PJvMXUFFEAjVjAO8ukuJkQEa_MUz0BJCWXS1I01bhAzgbMcx-S4w_pptuctc63DGa6vb7JxAiUIJczxsKsdqAdtx__sPnMYCGKk7VVxwzHe82FmAc3MrL-pcpsqwPPfd_2D7gclPuo6T3AVoeo5aHkOrHSWDt4kVq3Nko_K2JyxA9923u31AcSaRSFwCu4xUFZhXoJtUIqC_RzhdMaPSD1gHaQexRl5B_n8Ry59daPDoNrWIg7320-XjVD94aVSuGvA40xUKYfYYhKsgteGl-hf841az9H6d2teLTh3GcRRHM3axBf6SIzaWbcsZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=CY4KamZuY_vu9EjvV_YlJNFJ-PJvMXUFFEAjVjAO8ukuJkQEa_MUz0BJCWXS1I01bhAzgbMcx-S4w_pptuctc63DGa6vb7JxAiUIJczxsKsdqAdtx__sPnMYCGKk7VVxwzHe82FmAc3MrL-pcpsqwPPfd_2D7gclPuo6T3AVoeo5aHkOrHSWDt4kVq3Nko_K2JyxA9923u31AcSaRSFwCu4xUFZhXoJtUIqC_RzhdMaPSD1gHaQexRl5B_n8Ry59daPDoNrWIg7320-XjVD94aVSuGvA40xUKYfYYhKsgteGl-hf841az9H6d2teLTh3GcRRHM3axBf6SIzaWbcsZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bchhRQCLOdiDS5VPUSSvj7EwBWkA68x4BgGEGk1KkE9A3w7qsXLN29hiGu5bJjDm-9LHNiYa0vQ8OsWFCjQ4biLsdbb_vB24Hn4h76TbVvJqBieokfb_P5cf2Iil8TLnZUY4ybpQOh5_8ET8Kx_0pOY87Obxps7CNmNy3yD7A0wQ1YDcMMssrZsRRqgsPHSZPAUP1vZzGhvrxiGH7RrsJhQHrdhNCGyX9fPEGXYD_InS5dTVc2Rf4WEKxo1X24W43vfAyBwG9oEPaeOqKrnJs6gVpTLJJsbBSjBnankZ9Qm5UT9WI-EIscQDbeJBjkSlAGTkXdR51VrHS2x_i5rqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
