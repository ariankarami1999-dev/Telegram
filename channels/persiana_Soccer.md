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
<img src="https://cdn4.telesco.pe/file/l2F25VWpSXTZAfmFUCSH5fyE2H9lvUDXTki1qNafgRmMwv7SYpN7V6kpB-eJr4J0enl-j4OPLYJxtPeFAGoiSnVE1ohbNBrfO2_7hqq7KIveY_g_MOmfb_Vl7e0FDdvIzG_ir3emmeAhGQnm3ZrtHA6PlgKDQ6eI_6YVSweJidtiMPePwHFlrtRIfd0XMDIJgZAQN3lzuv2pzRAynsz-kQV-aFwRvj4FOgfmgKlS7zN30jVw2QkKg-iPwalNNStOhJ2mnM9pjpuDo5S_MRuZNdDJs6vjUS_gOzwRs-vLhjdbfqoWOzOTob8IjJqqODac0g07xl_SwH2FmYvWNb4N9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 301K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=FJkCdf9vR1J7EYh5HUxLYbiYcJG7HYV2M5FexmDCr31hv9KoLJ2m5dnmL_C-8qSCJi9UpsHXn6vewzaEdF79rhk1Zbg3s2KGkWaQxuLXVpa7J0y_DxH0mLdGLX384sp67LwQCtHg9LwcgjZuWqXWCWZBcXQ5B11ZGlgn2MRLGUtdq8s5HOotwY4wTlxNSsD5gTHFH3p03LvVUKh0f_THtrqHOWbIGsHrpl95D_HAEeJF5G0L30ZXhHP0ZAHkd1JwA4EJgTzjslGr9J35OfPy0C0qCXfXevZq6LPJk6pmQeCuOg3Tkz7kZzpHw1uDMhbLbaiPCxL5KXWZkai4qGFr22zkyy3y5pqhtmZbxZxjmLCYi9qLDXEWCCQxwgUOe0cfdoyrQeaEk7vPjqK-ZzEdSqLhHvj2ZvJS58YgH4cgpuiKC4umRM4bBs1S3qVyVcxiIwdcVBcqtbxtJ_Yu6IDd9HphfW_NtH1gc5zMT15qZeMkDlaTW4mZnRkjUi3MuLUt3zMejamOeohvzWImhGDsl4VxRYs0JsV4Uh0iCu5GrZdo0JMC-rmNmpy2AqWw2Tnh2uv7X3XatOI4xQTIoP-egoXhvgan6QGsiIMCQ8lf81WRlKqv1wzDrUd7ZO5r5HMsX58nXV1JxwaL_DPzgudQLZYVDYdu3DHGZz1EDo4VrdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=FJkCdf9vR1J7EYh5HUxLYbiYcJG7HYV2M5FexmDCr31hv9KoLJ2m5dnmL_C-8qSCJi9UpsHXn6vewzaEdF79rhk1Zbg3s2KGkWaQxuLXVpa7J0y_DxH0mLdGLX384sp67LwQCtHg9LwcgjZuWqXWCWZBcXQ5B11ZGlgn2MRLGUtdq8s5HOotwY4wTlxNSsD5gTHFH3p03LvVUKh0f_THtrqHOWbIGsHrpl95D_HAEeJF5G0L30ZXhHP0ZAHkd1JwA4EJgTzjslGr9J35OfPy0C0qCXfXevZq6LPJk6pmQeCuOg3Tkz7kZzpHw1uDMhbLbaiPCxL5KXWZkai4qGFr22zkyy3y5pqhtmZbxZxjmLCYi9qLDXEWCCQxwgUOe0cfdoyrQeaEk7vPjqK-ZzEdSqLhHvj2ZvJS58YgH4cgpuiKC4umRM4bBs1S3qVyVcxiIwdcVBcqtbxtJ_Yu6IDd9HphfW_NtH1gc5zMT15qZeMkDlaTW4mZnRkjUi3MuLUt3zMejamOeohvzWImhGDsl4VxRYs0JsV4Uh0iCu5GrZdo0JMC-rmNmpy2AqWw2Tnh2uv7X3XatOI4xQTIoP-egoXhvgan6QGsiIMCQ8lf81WRlKqv1wzDrUd7ZO5r5HMsX58nXV1JxwaL_DPzgudQLZYVDYdu3DHGZz1EDo4VrdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzfgXG7pIeG7CRZr6bJuUlubsnLEEIyqrJ7Ex6tgpCxOTq3qRl7otHHAjhJrHU3MoVB5d0w2aXDLPbhYaXOKpmNWZ9Qvym96hKTQywJa44LBbVCewRPjA-UYrlnyvuaFbJx8CtVKXE-Sr3hOHq6L_MJLSH45j9C74VgV2TqnoFCL8tUo14Ear39vzxnz9FCdyZ4hB4KlRin0xeHKzNr290u77X7IL4J3pm1wSzD7-rvw7pzCKNtXNHco1O4FHg77v6y1lf1hzIIH7oz4a1MRi3lc70lluUD5df7lQO1zidyP7rXRyJF1WIe3zegCmMPBC7VRddoE80MGwwTl1JNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI0Jt5mpFjmax_shUM2-iJiOIXw_Bg14kOp8BritiJT4cmrorig5ZuG2gA5PpycaJuPhK542r_QcHd4AhIOzUvP9MSWayrnALxjttiL5_hRGoUzWpw5lQLT5AvigFL7hPOcWIy6dFbnnC1JGZS0n0hqeUv6NYQlNxijLnyD_5vR6Y9Qb6HaRQCeNWiz90YVmSYnky8kwBCJWs9MAWFXVMMyLhKtnoThieXKYmtq31U61CueaKNd_wnU-zQxsOBEwVzFwXB0_tFJV27SDqntIdXfa_O7O8WA9_x5TsmzOFr3PmC1XN2cSeG1iV-NM3q6m_rdE0_3h_PA290ugbbg-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXZ3sT3FICq0G3Newx-P5MthINY0wVcaRb6SzcI5tBep2U5xYjwSovmQk2ydyWexvpZvjA-X-aVmBfyf22O6tBBi071jz3Weuqr66-WQbthjf6EueooAk7cutn3sEii3F4mdvjdMLdsYn61Q0p1jfqA5yqsD7COBTNrDJ8Y02jszhSKXJDxfu820nXXJQBwxLM9d16j29Ggiu-1Aac130UwPbvm03hezWxsFvcsx2Hb34w2vID_MYy8EexFjYXwxQ6RrvxENzr1E3yTWMe5IJkIscwKno4BAMjlagbZBvkCpi_q5tRK3C8DUBXPpYRwISNMsDwA21c7dOZUsXiYQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHW6PIZNcudZZcUufhRNdheYNly8avOpDYvsV8n9WSpjxy1xfuS82yviCoIomcJAOtt_60nsQLPyk_1ifM95cGFliXwm0xAEylB0QMWlvtH2eoQdE5frWSSEaVcL_DNMJi3I7zhq8zMze7z1hQ0nKTst7VJhZzo9ZguGTu3hCVVdeZZJ9PeBD2kLOx_wTl6YDP10xqCAsgUywWQjJVlWk14tW6WS6jJcOTg4PFIaXv6ks3cNzjHNLPcFBwR_IP6ssg6gYwJMmhAiMvUwHWJ7zowpf9-A-aJTJd4hh28c8-JNiaOPTOAKXajfZadjjPkPavQnpXFBac_TI3iezoi-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cbDQb4NpTY3KHJRYwEfrRFqHlrRQ097hs_q0L8QQ75QFYCyI5O8vFUYIaDac8QcTTbFwPI-b8U9rF4LRlLbvvIfOXi8UTF-PPV882GWan7OQzPQDb8-aPgkL1iZYvcAkbXcE75aaQdg4F_MaGxQ18Y5W7rUOqZ4y65j-UMcO6yiX9UFXS3Xm7kJfI2RRQKr1nfWeyWq_mypCTE9X2nJYC1N2tmyGEsuNjL3eJjqolYnhr4RCpFY710XM-9vK9RnMdkZs0tRGXo4K61b9I06b_EUXrbBm5ynOJUq_DNUJXehoEjmNQy2LzuulAxzEtbPltM4vT5-iW0_sc-7yuynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq_JXP3SjWHLJU1H-kk1OkLZwQEd_iT7uKvMZEER17kxvI_JN0uOt-R_gGddsHO4OqOy4-Q1hWIGlsLFaiBCTwlwHubEbwK25FAKorL8UOCc70fl1WWJwPCUi8qRiVoDqyacEdIv5RA8imp3BE3BYA3-lcvDjToAAgZGLK005U-fSVxDYVbHR2We6Eg3l9gCv6N11ggT8XUiTyf9J98Gtymlmvf4NwRvJcm1DvaJ1t97oapbuTwpUqtetf8STQcFY-7D0b7yO7Igh-25TxU1TYDXpINZUim1OhjnEGnqtZaQP82Mc4tgwfnfopoiPLsWx6oc6kniKSqS8i_P260Bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-k0BMGeCtg5oLu14coGxyuLUbdPDMaC-efmA7iaVzRKo_S9susYk-MNTSrbsuAenOoHbTZxQ_qH8jPNEd27u-AvyxDiqQ1dVgU1SmKi9jUl5CRH9aIShAPxMMHojuOP7vYOkd-JxjLPss1uZMcVlsOiFMZbLh8L2MN-xqteH83mO450gJLl08_vC3m8ZEx9px7XkiW0S5I4-QwGSdFxCs75aVw_ETMT4U5cpWXjzcwJP7-QfB33OZFZfkIF4Mnsuv4o5ojd5iN18XxvWLnqXIl_oX29BhF8j9LFOYvI_HLv4Bgglke7jpl2mJTw-IsEM-6vwoGMoyHOPV3JrQ-vOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeE8ttAfMEk8sS_1XLLBGrQhI6fkyo0WvTuxBm31siDFe4A4d7k_5C0U2VxQV4oJnpYpCtK-_sh-JNsv2ekOTe2Hh_TDt1KJYQo9otL53jHHZOzwx7OEcjDsDRJqg_uC6pBxabMmyKE4dqrT04i1exn222kPJJq64YDu3yXcW3rri8Y_0ERcF7QA6p4teRi1CxKCvNA4Vc-ZTR89jBd3a3u4aB0igpYiTOAf_IQsQGlkD-LlF_0i-OG3Txrxd627dbat_jq4f-uuEv_SqoUrDOfwADpCIyoBy0MJHpjRgjDVzJibMakOsGVmySVaf_56WM31CkDlcgp5WVULbz22Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvMgV0fB_UZph3Nk5-ld3vbGtofY_GV38j9NsKk8Tn3VN3UNt0AvjkSITulVbS9mbv4PFDZ5nFUNhRslFdI4MfNgv9FsZvZH88LogqHrNgVijOV_l4vSPKvKe93ztQ8WRamkWoZvZsBtR3S6pCfVBTYGW9pwekoB4wVr33IbHemydWVU0OH9AI-TJcO8Q2PTLXDc6P5d50HgzoSKUFSy7Zpk2sadlcWWLGS1M_xKzyk0Dbdq6ZaQ8I2AY8UifkricafTCL-6yNJssyhBToQjir5XZMm4q_7o8rypNRvlwGPyG9t3lhoKUXgOXCnDYPUGgl_eJCI3ZaxL6dNVNNb8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3aqlNPvNt4uHyZHeXi2s0Et5BzE54EHUoopHOVbszfmj7ife9uTCFULw3LywiAx1SyF0xkGai5z0i6bRNZBLWU8dInGF0R3Zh42BKwXKPE2oxAv5D_wR1QSFfAls9xB46XBtMeogkwvvvwioQkTqHJ4ZU04vVIGPdRu8tSrhrH0XQCzHIbumzyk7HztqTGRwyzwO5YTX2nziD6o8vIaPyaDIdGdpCKHnraT7_IcfrEuP1I5SofMrnHd2baUR-iYI5YQ-iYBvPGSccfL3OIshZpWXeodmkz-HqucRgyAlyJS3NHQkCWwW0bnR1DtwiAnrOw4xSh0JUwONi21v6P4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmaF5RSOQ5KCXMKAxgm87GKPtj-fpgehULC1XZA6ePr1mriMzQ4-yd2n9dCrcctK_Isw1Y5VBpoomLkdMZhLGj43zRx6QOSg7Zhn8UCG1FrQWdg5inyPVpeNTeFjOPFDGKvvbD7yUHhHfbglGH1tGIOx5l_-ZU0GJsHBOuRH92QFeF6YYhuDU_8FwLg8SlIuIWTLsJxLBlqBEjIe5QBCw1dTJKv-fb1ksSfR194Q9oj5VNFlCd3s-n4KvNNblb3SawWkMNe1Mok6R5XGHds7KdkiBtXPuYYSiJ2RCNzvIn8KwB6kNmHIMa2bhQFXDThRqRCOgrGL3_ZMdRbCUpf7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD3tKIa6sTGHu3QHmyTjNhdvupjfzjWW6wQqc1Q79a3V0npSmzXOFsTYAbmSHfA_T7TXHvq7UupSPZWwi4ZtbUL9PpGvfdrdVJd0C5iwD4JQAZYZRIBaMmISB-2Jzj-AMbhhPPIbhT01TyBSsBbbeGFWiiAVOEBZVkSMweNXDRexkyvRqoMePU8gRY7GCyarqUJTbpNrmTTaGDYUjbzu8UUc_a34-a1ajeON34E4lJT_eXR9SManrO2PzoArivBBZepTxfG_4AXkrtn65e3L1R1Gfu6R9BrJIupFwoLatKbmu8FVeGRObPis0s8vzvszYAxGo4--wlBkqNgftaL3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBu27JtdHfoG9izratTut75-Cs_atB2naNPzP8oys2CCWIvL_oiKwH2e5HvpNhIQW1keJA9bfc-JZU1myRU31Eso71s8RNtHzk9z2-NLPXctaxV2HI2mPKN8-NWj1CIyHgf9ScN2i4ASW7OpP497V7ptK3tC8hOxxX_vIZJkPwBSzpJAhqysn879RxesSVr1_SQrzhRR6oa-sK5t5sD_VTaJkIHQ319TzhKMzqhsVKb3iSS-PN-lu5PivdP3Quj2S5lpn9--SsvhgIvN1Af8lflBlKGwbV4DKMOmHDR7HQlElfHPWgQWNjdWz5GT2P1e5XliGQv_SIztQzbY06IpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODqy9_PzirnLEp1CVDgWzj-b_Tj8jHlfG5ufIFW9osRLpAZAQmGEqHwURQJKPBUWjZXLVbYyqDxOfv2UxACUkELrSxCjI7BGmslRucFEHmtf9Am8QS2bM-pCFSegNm3cqeWOFGnKNI2tct-mStrFEfNBJHgOPU4O064XR-1oWHKo0JCMTGbmU4F70VsMpouBU7O-oCfyxTZLPhFwYKOn45SzfnEEfnSBUNPUmnntokVKt2qcGvDShv25HUJtKdzSqtj6FmaUWtS32mToZSdCGNg4kAfHVdr1Ow-L2FNoUcVUHrQWmKwf9-3pHJMfSJVRAPfgC4uGjWg3n00jhunwpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=pJz-goUoqQ5Kes8UkAXnD5psSA5sCcEnsed5rC-F1Sd3VU4Yf6mW03wAgp--jpWKf2HzukbssbiPxdOBZA2mJ__u1jxM7YUMQESxjb2b4JBq1m-k0rtTXJiTaOGJfjN5tyTxTDHg30ZIP_hKp8h5JNgKVikXCbkNQHobz6wNKut0bAUyL1PWjWPHNmHAUOFGao0Q9uQHf4pIrOcCXWGWh7DEdI9PxLeV4L32q8q-5ZaERJTXFgw5T4YQGFwZZfHHB8E8j58wYpfkuQfkhDUqUBJzOVr-cTo-CTg0QnpBvNfDK8emrNYSFylGqnYLLKGd2Wpw4ETbn20V2SuDkOX_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=pJz-goUoqQ5Kes8UkAXnD5psSA5sCcEnsed5rC-F1Sd3VU4Yf6mW03wAgp--jpWKf2HzukbssbiPxdOBZA2mJ__u1jxM7YUMQESxjb2b4JBq1m-k0rtTXJiTaOGJfjN5tyTxTDHg30ZIP_hKp8h5JNgKVikXCbkNQHobz6wNKut0bAUyL1PWjWPHNmHAUOFGao0Q9uQHf4pIrOcCXWGWh7DEdI9PxLeV4L32q8q-5ZaERJTXFgw5T4YQGFwZZfHHB8E8j58wYpfkuQfkhDUqUBJzOVr-cTo-CTg0QnpBvNfDK8emrNYSFylGqnYLLKGd2Wpw4ETbn20V2SuDkOX_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23659" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li0aVMbE9wsfAdY-LTvJQCCiy4Kph6v64imyCrQEiR67zoytdWh64t-TP7avhRsg-Ls_9jy-8_CDWf-JHnVwU7lp01j0-RjAjrUdaEY13WeiZWiitRfUmyT2HZ7Q03gzZfjTelBp4dMPrI_iq_lUjP-r1VKXR5M0UEKsVVqGKDxTymkJI8NhvH5oPAQ2nk5LM1GoVUb68VrVhvpIIGtBGGq2g7TM4-BLbSu8meYL8SgFrV0Bn1TylHZF3t84ewpSVQMPYTdgAI209hav_yY3bMem5K1EclKXFF5QwTOWiTdkdcpr4WDLFVpi9em-EBmh1c9FwbidkZJt_I6AkXD1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFt2idejpM6Lv2OozYmSZ5QgzDaTVhJb8F7CQ5C7vZqy21XXkKJflPCZp9SL1vNV262VICcn2-ezBLuISZtsOebm_cZlJhnv1PayYT-mi7C0QJoh6vI2hVfWP9e3R_4uy2_hqoBBW4jFYdtj0pSf3VMG1-YiuwysB2f098LK7u62u_NlhcP6JyaFF10D4u2vOKrVvZqCzTN_L0Xobs9uB_GpSip4eZS2W5EYExsYLSQ-dGWh8WzqLfhPKUTdl2177P2CEwrBCuMsu1SD7BjVDDemuactzHJlDOSzMJ2aDobzJgc2WQ3bS4jh36Ozc1CQOg_SpGDo2FqZWiv7atd16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX4eLC4-BcDqx-QQgiPPute-3Esknjqmm1BnryidB3sngc0TMpGcSUm9ZkBxvlWAxRq4PoQEMSalSn07dnHxRidGcPWMZz09Pf211ziChR5L1pzbAdFxIfgwIPBq1ql8gudYxQ34ur0RIAl1a457w_RkXTbPbktYrX8wuGCN8PZySCeuGAgqFiYmBEiGIb5mEjhoo7sRJM_F59nTDU40Beq_fwPgekNZJb76FFKeE3Mssl3l5wwQhxeDTmzYQf48XTHgykHTJnCfVpljViaSdJc0k4jyG2KKaw64_bl4xKMI8ituWTu189bpUGhpkb5kHmvrpTvNB20AzChzgdGJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=hO3Y1HytHeYt-ixrWuN72dAW6QXV9upFFVf4lX-KmaPHnYPQc-6ETKe2y1_rLmDUS_9jXnqVbz9RpbZwDzJ3lbaDhgGNDKkmyGo8gQIQXCJsqDH6cnFxHTkMGQf9PUVEnKVC5SQwjLwV_S5kMIivATU5H6Cu69jmrIyj8Dp5WLNFuL23o2Seoszk2_-MF3Vf8BRA_LMnqepnMzAfkhA1ULN3Pa0tRWkaQQe3u4zWADYr-gOViHV5qHaZyoPiYBvhT523Jc7uLdSm9dEvfNgna0y216BejvYOz98Wfp3JQNn3Pwy6thK4PcCLecJrYnvzafVPYKe-cWatFT42VYC-3iSpMYO4oJiMkVUrPI7eYQwGEvbeBMZBJC9S1C23TjioeSrgcV4LG9zVoK86TlDxR_otSAesDNF1_dEyLNu1GQ2nVTUbqCdDPuD4WWHM6iVQ3UMznpTIH0TDevGBQVSKNgVIcDmzhI7HsUvIHkovGgbRAOAODqXMlcLWL6Ze62Xl247sEeibbtzRe4hdP6AuHqL9Vv3jOh5U_4TrUqHxdszgX5af8A659aioTFgtkM6ylfah93HAT-qN8FcHBAxghY4G77lF0tXF3d1t_udUWPvoBh5VqYFVKVI28qE_LP3oh308-1B5Z8S99uIhaZRsoZw6voQWikQblVk5eAb7o7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=hO3Y1HytHeYt-ixrWuN72dAW6QXV9upFFVf4lX-KmaPHnYPQc-6ETKe2y1_rLmDUS_9jXnqVbz9RpbZwDzJ3lbaDhgGNDKkmyGo8gQIQXCJsqDH6cnFxHTkMGQf9PUVEnKVC5SQwjLwV_S5kMIivATU5H6Cu69jmrIyj8Dp5WLNFuL23o2Seoszk2_-MF3Vf8BRA_LMnqepnMzAfkhA1ULN3Pa0tRWkaQQe3u4zWADYr-gOViHV5qHaZyoPiYBvhT523Jc7uLdSm9dEvfNgna0y216BejvYOz98Wfp3JQNn3Pwy6thK4PcCLecJrYnvzafVPYKe-cWatFT42VYC-3iSpMYO4oJiMkVUrPI7eYQwGEvbeBMZBJC9S1C23TjioeSrgcV4LG9zVoK86TlDxR_otSAesDNF1_dEyLNu1GQ2nVTUbqCdDPuD4WWHM6iVQ3UMznpTIH0TDevGBQVSKNgVIcDmzhI7HsUvIHkovGgbRAOAODqXMlcLWL6Ze62Xl247sEeibbtzRe4hdP6AuHqL9Vv3jOh5U_4TrUqHxdszgX5af8A659aioTFgtkM6ylfah93HAT-qN8FcHBAxghY4G77lF0tXF3d1t_udUWPvoBh5VqYFVKVI28qE_LP3oh308-1B5Z8S99uIhaZRsoZw6voQWikQblVk5eAb7o7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzXU_6Sw-61Fvv6hjsns5_RRvavqGIu6osocT47j5zt-JCQJfsvotT8mEresXobrgLtC3AbQpwoiZoqMOuAaWPWfO8VOEnLFF_yP-0j9feDk5p9t0-Fx6hDAdq7mJQdXm924d4fF6MF4B54kXIWIHKRCOu4aEpipsp9ua6tQAhPOK3M19gOBAz7FppW7gANzfWiHAtrHjq6O1How1SNXxT-PapPxnelyT8MkCxOQBmlj5xPcWUEv4Kgj7EWqg9PPKqcOVvWFBwJecx1Dmi7rcSZyiSzpeHtH-7ua7wjYQ1UQTJKkEWeBvugT4c-8B8P8rN-W0RJCq21V-cClfAYNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUc00691fwkTJSSNPYo-GKc9ffXqt1D_VjvBhz92m3MC6-aXoh1-Ac4BRavLBgLJA1QxizTm_QBlxf5eJwszWwjs4CeYZqhZywre_CRm7YfAmcziNBAuq2b2KwWFtkNpeoeg2H-yO2cof5qjlRlsgojJoed5XzyFjM-MhW9Ie3fkYGZJKCVUP4P8DJ4kaKkc5C4vIfAecEejBEu7ulEB27wevC688i6be85X7c7C3cj-dYquPKSISb8U8AhGNgzUz2fwxbi3Ei6W0ix51Dgf_9G_5jCD6-92hnkOZODVRIdzqPcK-a7k_VugQ1qYr4UetFge86ZS2tCJAGG8MHMNBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8dy2wvOwuu_00LRKGGQmNsDUz7M3HvEEwfHMZ7Gbm-NEtkio0nYkCMvZtxrJxS5qZx01wl4Kd8b8konjI_v5bF7ZqpfmkpXBTEGTcZc1I8Zfv9ni6Obn99g38hWifLigHR3ff6E6aqM0xuxIX5eveDoeSnB1y4gj0WjKvjeZTaKiUgoZ3Lo9M7kmLgdtXZwF9bGHfzaySn4sDfdZ6PCgG891fyuK6i5b18sNjG5tAX9ZaQJZOIcj3-Hd9Px0WXkCKkVlaaogtIiMrdE1uku3jpoLd0nMK-01NcimDNnw7P9eP84-JhNCkbEBl4dLpMJJTfYoZ9BXML-QPJRsakC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnlhJ-eVm3f2CdAuaj_fsi8XMk40DJ2lS-i6YOjdYdq9a8gWyilio6O9i7lgD3pP0LKNMPAfp-gBo5VPM20i0ErmyHzmMyFyaCxdYr2e4QDv5FseuqBddIlASE6BqAsyHmZKpG86wMLnDfEeeaW9pqEGf8k0V1r157A1toPkIWS-1rRjT5RGd204cBEu9X3JNeIl4Q7hUsoBJNec-Tq1zmUMGjKW1rEkj7_xK_PfgshWAYNc6UArt76EvylQ7PdmeD2rLbVDxnfZfzQF1Od-ODDfyVK0jDt_JjtQh5Ww4rr3U3OVszTeONhy1l4BeQKNq_10A2JjCZcCgRL393zllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIlD__FsJTmn34RjvZpHiiqypAF8o70jmBoVBB6g7DLhYVFtzFFXXxzq4qdzCVop9U6QAMnkreJiQwd-_pKBRJ9ZD0uMef4xNtZ4eANcwweZG-1x2qGl1Dgww7Je7IyhXBDwCu46qrOhCEW-ShdL1CiSpUsqTewX1SXYsA25_Msa-Xax2ote25LMhiU4YBxFKMWvSNSYlKE1BcFwX587MSw1cgfzX38rxpWJFM_OfC8smSnTU6wl3A75PeareAcDwYuJlbs1RgCX0F6vsSC3iLrTyceL1YlpBrHb20CUM-QAwNFBGCvf5aZv9gTU3xre3TkDdc2qMM6LSYpXcuhmOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=Hk3OGzv4NT8SJ5I4Ky2aK_UOej6UE6g2ce85zU_gvbufvQuPRmgsxM0kSRfNQaq_ZzVGOxx1nxJHgCrRSkkxzUmElYQADFkILb08gYe66U90agvn9UwavZ2joihUSYvKd1_jM1kyxYirZQadSR1XEdA2OOqNXgR9kiXXjRXfJZasQkdpjOW2afAGHxI7Rn-O8dYF6vtU-AdfVN-_APyI9dFtb9SQV2VHG4f7VoO8ycH45Y0_g4p9j4JGMsmzQ3lVcA6yANjIcIr1dgJM7msmA3RA9LwiiTGeB0NPCAoxDobgkHhdA_WuvcWs8nUFx7mpj-LLocqfzfHBXvTB3YjYwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=Hk3OGzv4NT8SJ5I4Ky2aK_UOej6UE6g2ce85zU_gvbufvQuPRmgsxM0kSRfNQaq_ZzVGOxx1nxJHgCrRSkkxzUmElYQADFkILb08gYe66U90agvn9UwavZ2joihUSYvKd1_jM1kyxYirZQadSR1XEdA2OOqNXgR9kiXXjRXfJZasQkdpjOW2afAGHxI7Rn-O8dYF6vtU-AdfVN-_APyI9dFtb9SQV2VHG4f7VoO8ycH45Y0_g4p9j4JGMsmzQ3lVcA6yANjIcIr1dgJM7msmA3RA9LwiiTGeB0NPCAoxDobgkHhdA_WuvcWs8nUFx7mpj-LLocqfzfHBXvTB3YjYwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXJqcDy7t2jSxGn-Hp6FxaWzUWaPW4TnYxT9O0sA1dCzTnPKKMSbwR88Vc2O9z-npC5S1c3uyPIVWNmtrblkKq6LN8BpfrpM8OHljNk_kpq_Jpc28EI87b2FU2ZIyJZEqzXeeP1YgH1rfavj3ROpgYJm7Sre5Tcm1TQqP7g1v4CUm-_u2gyRzmRbSZozco-sOW68upzjpL6c2nJloKRQXMDOuFFuQRzfmYckq61JZmZAhCDtWXkjIzpmg-VjWCkQoFIPaO9S0RiZwVcwanfNHI8f-CCwgSRiJa48YLwSeTzxZLURd_Xso2xkXsy3kLobY7HHvSxEEz7dNfnVkdSrCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADN3FPHgbZhkZAZmUxwcRumnblbFqelEY0W6TkVIgfI1GmUbCu_lFwuJR_r6Ip7xY_WXdkx-nNyy3-h9eJ9Vjs7ck_NqLEtv55nBHBywPnN-y5sK4Cyl2QjuqEMKUGKsTUi47UKgu-1b0lue3FR_22ck2QbQ-BY6KRWjRGU_mZpe1t4m6W2IL9q7vsvnCvjLOfQzkvmdwXjzhAIDmrEPZHwDqRRNB6vLGJOjBMjWwJQJdokpdsd9TntD37syVONSqL4o6WT_wY3OQrOuRKE4jHrGFRoYWYDI2uIoZOvcOJQQImv1M769ZQJYtb85DOgoLOqmnxacyiQ7OWEhduCkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR5vBqQ3srsU5fmRLA_YmJWcEwVKVohGJOevf4SNRGVaklCqFIEry0DlHgWCcD_HVkIR7hd6B-k7rM5ub4LcqJjUT_ngwZ3SJhUHW8k0br50Xw1HMIP1vH917vSD8dlM31N-1pqZBUa1-kjeCIRbhHyKvn7M25YQ_TmgSyxFpmFja2j47n1zwbmSGlVOCbmCEckSP1bN_AjKTZveSiQmH_YYBQ26i6pdu0HSYNPXk8aLbUrf5WadefKN0htzN9s0lae3a-UNTs6-qGTaCJ1piACeJHI8uD4UZaBD0QBWyssllr1zEQI1CjaMSPFJZIaKsrWEJjOFrQOh12Ph_940HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K01RIh54Z2JjLW1XO8vS1g2wqdGZvElCHDmrqFUAT-7vQjG0uh3C8uYhRvanfBAJAFo0EU3FVipvsUyFUZkjzd_pYUI8VV2MZk7RkdmQqg4NWSNGgjpkmL2rqCHZP4t_qhgJXnk_3yDacOJChaSBB1g9AZl_qnKeirKxQdlVqNC1wINPqzIPyoJLAXmXKvdqvmgF0BqqzdZK5e2iQD06c7M-vhMSDrlly09THp3QilVl_O5Cz0hpyecj1ALQ-bhxpnCotR_2wrn4Zbeit9PzgLckDYlxija0hYd9L68NZ3LlxMZqPwknFC4pPUQZ3jYmnXyw87fjDgLHOqU3hCH2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHzVd9cFZcRsstG8__V6-IY5RJ7PP6_FQHF8N1rfRC_7F7VFiSqZY7Pc3enVx531mS-zne1w1BUU2ujnsX22CR0rx5X2v-o7FliK_zdjzz10Fhl5c3UOQGJfHABldzBwga6ZuChya3AaLRglo-grMZP4ZaE4be8sdJIjDMqdNlTrECWqNOl7E43eLvBt6nfPGPls9Yo-f0XkqxMLCPy8UdRn8yONfZomyMSzbnLgRR58KTjn4LTQqgYk7i1dQ-a_ZKrKEbyLOAIsTXVkCFMvrNSAcAZ6fx9JWikBsdsKqFYGByg6A0oeInRJ9wZ6kdb80I-I1Op3E-1KfJKPjVOtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajFXvKfdI-mQMazzUKIHn0tta4l8sPJlkcst-VNI1KrWbxkj1fVdmkvgUVWPu1AQz2viN-_M5Z8DOHsk5anAr7-olFnqLJel6-Lfm95sLeme-TEzNA5OB0eF6DvHRk1AjNs-O6XF2YU13RncqfvQXpx60R_ofyLSmpBR-uRJ9Gg6uXPUnVTBVEGWkrJHdoOnCPtVmyqiBs9nkoqqpxSwqyYgrZqq-Anr4eRg4YuDbgL4BeHLNojyKRP_cjq7L4hvEgupbx009fLhj2k0Uj49ZZvsGueSGAqT_sZXrYx9vup0zBZY6gAB41MHRL1RDUrqR9U_OqDCCsYBQyUpAdTS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZOfGYEpTHNPgcXYv81F9KuMHZ3Z225GX0eJD4zrAl4hvNT1khyaimvlQSLT7XnloRC4E2PbFzUk43V5o8K1XrDluCQeXh1v4CriO-p2qNA00E4r5M87Rhz-HFNPYQafCBoDWcL9gePwaUSY9n09O-X-7sRnUykS__tBdVDNYTYQ5RqiCnCdvA7rZIWoewxhYl5YWDUQXRwvdfqV7P98jgXGxiuJg1j6yC7jH_IF8CaugB73zBpDmkWQFh7fN7oaGGZqVDfXgFGzfemlt1VUxu4OyX5RHuELQ749cnHyNnVfTz5wpW57r_m4MP5c8PbWja6FfH_FAZTV4bW6ylLSPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0DoW_CJziA1jYAsL4xD_5NOPsn8Ghrkkps3l0RrbvPVg2eQjf_Pu8B6XvrCmlrEI_mEgi82-TxLy8uhxEnJI1TNIAdz9hJlu_9Q2e0euz8E-3AVMAhKKx9Ah3Jv4SzHESmCWYA2eUHVDNBZ9ure5iKm2G4g-L2cYn6nFX08efjYsr-oUFMQf3DpBLIcpanDj40wVxADSLNNZKkQTihKIacF9fMkVJ-mfcLpygZC7NFW3suvblefH24uJFY4kXfGMQawjMGr9WK0D_F_EU_NsiSZT4_MKt_Wv4lIvcimryT-3_PNSqPcdLbujuA7u6eSyoBoZlnPaWXkg02BLKp1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZDQE_Dr74j5cl0oI3kRH0CbhqBTFTWNb0lkJSC1g9IQzgodtEFwu4mNQTPcDnixhPIJidZ4_RuWdNamp64mIskGhELHZ5g5TfU5koQ8P800T4mi2kloSW-7TpTBzTYjt0wipIFVKQWvIPPYQi0vIEJlEm-fNTNJ7sKm9T0E5IKa4jvw4ULYuzNG1fSV8u2KXuU1H7WM9EofuAc8bsT6UMS8iDOYGd_xn4eDVMFpklJuDMM819Zw8U6uyrIPOUeYBTw0lpSn3OM7WYnVoksrGBRT9QqOpemxo2WTETS27vtqaX8o4dakDLPxbtF9l2VUUcWoBrG9gN5bhwzg4Nl9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccgvoWn67_kdocz5ABIkNg0lN_kmo8IK966uUeoe1VdVu8P2Zi1bc4vtnIcer9KZCY16Yu2S-UfE8-WcbN18k-Xzmj28NIOX8_w2NRHhpCfNM5KhS7HmwVtKmvsk411e8_3P9erLewKJUmrl-tZkfp11Q1tC_3w1cG7UNEhiDfCnxA-QykvtPEZIC9MU_8rHW2YuIj4fEDN2Ce6uJUAeTy0jOeFbwfca8NepLEJXUXvRbzk69XD2GHrZw7sCuapcqLEyNo5z2DPj5EvB1P9wdO1tGnQt7TLmjH5MPp9XnetU-ChyyMVpxSmHiV_Uml76JOGdmn7yjzcjwShp6Zn0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-rhbEoCbzIRCYryVozR0F5KBcJUYGS7ngEWvFEvYHIw3YZ7P01Rh4Zd2HpOMqdpgwm_4KPBqLfHiBoqo11ZeSkskWXuTfhPkqVuXDS2jZkX9d7k62U4eVaJ6H-JR0HOnmvjMgPCWC6OmyFHilG7XtQx4jgxd3RE2gfjwBIR2ZOphWwlAkpsEP8GMTXN1LtMBfSbyZ8BlOxhpg_MvcKL5oEvNfWIHaZAgIzB3mNL0v8Q-OgpVrlDzrdN10UXxaau6mny_wXN717TZxA18MAAP1dKLHUDcSP__pVpxbxK2OLbBz_TI4XyGGYc57HJzuDvoD3MjYfwY2WqL-MMXQK7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=TYT5aKlOqw4CAfzwBaeZEu7XjqbqR04yScdtTmZW0a_MQM0PUcVb7BzDfw50psL2MTAVkv_uCmlaWqY0TWxhL8qR3P53TvxEf0t51oa7pxy7W2d2kYiDjsmyCso_JBWr3G_bN-j7aYN9iPx59DKa--VqvDz9Z_yK-G3Lz-ZZFDw5TF8Zx_ziTkaf58ucNBpE9W19Elhs5KN8rGzKzI7-Xto3z7Qp1TsKaVD_WMAmMqoceaS9wY0dfj8BVBE6wKdiec3o9Ze0x8X1_apUOXhW5y8DYn7dWSfihxbx_C9Wcmj-gSMCEGl_9VdodJjw5bnw8rtP-u7N87-SH7Evl2bKmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=TYT5aKlOqw4CAfzwBaeZEu7XjqbqR04yScdtTmZW0a_MQM0PUcVb7BzDfw50psL2MTAVkv_uCmlaWqY0TWxhL8qR3P53TvxEf0t51oa7pxy7W2d2kYiDjsmyCso_JBWr3G_bN-j7aYN9iPx59DKa--VqvDz9Z_yK-G3Lz-ZZFDw5TF8Zx_ziTkaf58ucNBpE9W19Elhs5KN8rGzKzI7-Xto3z7Qp1TsKaVD_WMAmMqoceaS9wY0dfj8BVBE6wKdiec3o9Ze0x8X1_apUOXhW5y8DYn7dWSfihxbx_C9Wcmj-gSMCEGl_9VdodJjw5bnw8rtP-u7N87-SH7Evl2bKmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_Bg_tjudLdZ_gtjXl8inBWZii3BGIQHN300C-puXoNpSjjKdoaR8DE6CK9OZjuW4AA7DqNzAOkoycKHOkeGT-hFmiDs_onwMu1lNrbK7NNlWLgxj4P9zlUqE--fB0nOOcGQCOiwCFF_H9mF0VybvRDZfd_O5E2PJ-9gvXzufrZ5HjdZLTRshMXVstcbN4RjLhrfTm8waI0gnYclvJ4W9WvZOeukoGdmcYIU2FW8ohqP3t7OLMv9W7f1ZVJ-VTmwA3Z5gfxLdrtX_ZxC6eMEKGjkueAKp932G8X86LtkuCLd-ithr_zl_VnYRpL1ZVgxJEFdihNlECZu4o3udiCddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvTVR3X3qaj6ejoqL7-7C8gp7TeJ-q8gyMvfUEbhkP18tsT_Zv2PcIYr2jSI4dPTUQIqgKvP9BSk1aeEjJT9hC1AryutRWjNKBgRX6rl8yZ4B0qKUOEv0K3MeY8q7RzeLhacKw5Gg1dm0xhxEdK9b5ERuIrlti-ZI2Sgrc3q5aGxSrZnE95w7er_kYOflKzZi3kVwuI2vld7i0xK6tVMcjKNvFvZJSo1CAqTDPgzD21PTV40GkMFYPtekPeEUIJZ8jzZV-B5qskpJDnHMGEfjFq0Z4MIp5IhYQ5M6mtTBJVL3y5wXb73jCy0FXQtCmKdDIKuPQokCwHL5H_xH_rzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1UGEkAlS4nNrZd96QdxURM_97OhS8ufl9cltPlJkJk9NmmVZ-Bnh6qayBsMqsqwBZ3oNkBJLEJrjOyyWf4X9zm05vIOqSjGtAu17HQoQWEATYKia7fLLdevgKSY7HOJe2zz5i-zYyrOOPyBQ7jWA5k9OFgBxeJjzs20FUS_fUCRxfl083Pr0DT7FSFwwVlJ47MLQwGTwrNwf4f2Vp5xQJEU_z2BIb8HEPiLUo4kL8JELWTISf9zqrfGAm2qXxdxdtZL-_QnKklTAnVCdcbkYsQvrD2p3KfueAQIOYV-6blB1ihWo3D9_2k6-ptkGsB14oZMpQS7MNK673laA1703Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3PK6pJRm3VbkYU-lFEmN3wIUEHyuOwPWH7_bFVhqJa8BbL-A8DL-ToKy6VVoxCas1x6SqrN-iu-8VVL1nIXguKr9fo6Flb7OE8hEZdYl06rG2VuSXMQkB2lc77cQ5V65Za_-OxdT6_9vkDJe1quxfVYECXpLXFhalbyN84q4--Yz3CB2wt3jX7k6AfAoKqDiW693h-vsxXxg_zvIVo7d7GjNSLVAIXkSuYJAlYrg5sEelyTfoAFWATTM0qPMW2O8QWDMahlqGNoIV2i1a_sEa3pCXcIs1x9TmTmjD8U1VR2A4YWnwhGcTBLI-un8Hg0LwC1r5vgdS6scevo7Y34XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5Qbw3RdUTTmWBnWeAB1uVyTcWJWj9YVH8mLfVpEGBXJYEZ86xm-aPxWNT25uZ_g9mV4UNdqioFdQXmVJOR8fH_vVXGvdoeq0g7JnvRkBH6e1DFl-JnwZCZj_hbNJT0HCFPMUlbi740BeW7R46Hcava7UadrFDL1BSrgUO_Ub5Yy-yfpWFlrEgnVp-5elYJd-BnK7DfQt2_Jrh_JwRO_WwuWaZDi8U2lsbyX0h-JH9Ne0D6GAPdwk45LNK163QQz6rH-7d4neyohoHxHKETS9dAo_rF0qhTn5bBKZDvxsfqa6YsRD9yrHzxzJ93B4dSJFP-xBd0K8L8DDdwGTugwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoaCiJ0XBJJbzd3fDD6zVb0JQO9oluIyjfSViBYNVEJXAvhr7R3C5OE_512crDjP4c6LQp2s_cyMAjpMCXdfyq1Yk7F8qQe6X0P8LrOGoyZAezc2fFu6-xg_VITOQGXlM1yrzsZPBmsvL50mo6a3Zryb8AP12jCeEN0NxOONXiq_waQVrMCegjYz2NPSaByJ859LupwOMyoCYl9yRZQ-_nMKlUsQ4TIgRM8prpzdC0ni4fVKufOZ4DHdNask-bz69DhAfGc_8d93Wgkq0R8uEy2Kvt5K5Tr4EIhHq0H1WULDZUcz3QhObEbPoAvyvJ9_fg01KxMWN7cU0fda6RqvPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwUcDN8jEVFXgueHPaPzvA64GAomCIPrjPJr1zbk8WIfKuxSoDgqWvQjcHqwpkXva_1lXLO5xiwYZgyij7x1I3CnfLyfxmpc17pOiqsPp45wlqjFa6QMq8VaWkIOa3QZhmk5vlR4QDRMvKGunt1_2LZaHd3Wv6j1Ytj_MEQ02I1KE-IaH7je5S8rhNvlyXZKpGVhrmc14MY_cUe22b81ulecnP0EMrW-GsUBUZbrm6hoyDN1tRlLmLfRwCzqOfVvAjFv8ucEcFcK2dmXa44_qGPWvVBIAUiL6U44pHCKoJv909zTFNqZWOW5nLa0bvTjt6czVD8ZsGBBBqMbdyVaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBaeIXTZBmSxIGairpCJk2WiDkWUNiv5E4-3z26F4bD44KkTq9yY5UcrGelJ35RWXhXONew5U0TG9DUTdEGoTy08hIpfcv5q8wM7SJSuU0VwLodunIfs_teei1C623d0vOXZQZMSLJNkC6isRv4n1_C8ARwjgaMnnij99RFpfsCt9AQd-7xwG6B61kepA-JeLq5TN6B5hOxA0mWyvc_bUZWDrLZ5zQOmo0_R60n7b2AH8q7XAei7tumjmR-dnMA86CzUGr1N7qv-CZvzcJAiyOoaIToXvI_PCVs-e5OxyEbw6rtDd9Qb0ilKE4v7WXcS9yAZqRAvMjQs7sndlMTlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=eM90SRx9o89cT_oH5U4FCY50Oq5aQo_mOdUxlfl23K_Vagr9D5xPjcMQROstwE1xJEEOtU8YwwvJizbqXFaZ6jd6oB1t7DF_IFfgKmEt7dEBEdrlIGE5_tdQeKb_Xwq9YswhTA9Z6_RHNyQXCPJDE643ulWddt_i8dpEohZL5Iqtv-rOVnf7lp7b0Y46ve_n423umiUglAgFK-hMgaVXA8A_MWz0-tEuoDJRo3dlaOAZKREfP1vAjhz-LO7-iHO2lmNPanGOfhh42eC8QiJ3XgrPiOL4f0DUqj6xjak7FLwVWgDZGX8zA5xfoxLGQuHg65WHN5CmbR5bTdumjzGg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=eM90SRx9o89cT_oH5U4FCY50Oq5aQo_mOdUxlfl23K_Vagr9D5xPjcMQROstwE1xJEEOtU8YwwvJizbqXFaZ6jd6oB1t7DF_IFfgKmEt7dEBEdrlIGE5_tdQeKb_Xwq9YswhTA9Z6_RHNyQXCPJDE643ulWddt_i8dpEohZL5Iqtv-rOVnf7lp7b0Y46ve_n423umiUglAgFK-hMgaVXA8A_MWz0-tEuoDJRo3dlaOAZKREfP1vAjhz-LO7-iHO2lmNPanGOfhh42eC8QiJ3XgrPiOL4f0DUqj6xjak7FLwVWgDZGX8zA5xfoxLGQuHg65WHN5CmbR5bTdumjzGg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryKsQTIgbC8o-muM8OryL4OcxBXvQZnMN6CuKx8hitRTZC310Vr_VL3L2MHaoKVB1mK3Nqs75HFfNGnq1SbLLrIxIxcPMwKTTlkOEPyZgdrPSW2bf4oTBvibRGKzik6KXSeVW1GoLYyS4mWA85uO1m_dhMGCxkjzt91PFMi74GxAnAcYq-bLb_XO7i28Hk5IXiBqAY80SkwDJTzmRMSrah5QW2GII3iLgQ25z2xuMv5Eylc4eN8D-HoIvwlpPYK4lCgyvwn1XTF2ERaySE2b62bLufGZu9-XnNMtP-uC_wroKgoVvA94IfVlNQ8JomdMVVWhyAoaw5u7kg2_XdOSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1i0E8Ax7-oSJ4cZn0SPof8XI6t2JJzUpEem-YdiIerh7ZZWKTd0mBXGhrdrWMAcT5_y9075M2d6yp74G56uB1Ohbmp94Z_vE7UTbfid0e_in0oqGUw6yuOPPmi1sgk4mhuY43aPvsuv3cNqf4Ch1UenjoOYM_0yOcrZGaY1mlyIPpur5AZFK8uy400wl0Cfg5aw3_xzKdgb-u2hHw4CNVcdJWrDHoCTLmB9-prtbrNTSm54efI83J0Atuoeq3zeuaQ2UxZWo3cTvTIQX6IZehWL5WdLXPRYk_ZBbf4jAu4tAM6p7-ASe9Nu8qB-XjimkRCkQimTu20UiWbGWvjYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DayMew1D6gpdMZCwTunETDSYeuq29wyKeOs_wsQDtaQ0u5HfK6uLpcJIabPS5NGAXMPJR8f6-mJqUwJsXOZHAhEQWt5g9LT9Lhtd5VAbCW6Urwnz5xZTuXVyUeGTYI1uSH6wcCgAgt9gCy4vdMTBj8CQIC2CG_ZqdQcLBX0U_PFA8O8hJCCfKFYcOMDN213ya10TOZh4Lru5NUwz8r_Gz2qE2wlF4KEadQfqstuW8YGpP_Pf-Svae42u9QMBXUtNDNSCdsEp3UB5dLkl-5NjWWDP1o8tgGlDF_ujasx0e-51d7mHvWCrg5O9MGq50ZwLvTIIfoKOIRE6PysFbDTGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTV70xFoJGJaqDgSdBXqpU4hMgz8RZNw9_Z7INjYz0emQdF2mz8v_JxpkAfCaQElx2d5TqUnTk-wU8he8zUE_nSyu0NCQrRiez3Uz958xwgiLo8spWzWMHRmp4rg1vcBQ9CYjVG91IiIhi4V89hbrXQVdDqe2GmW9OuwXvDjRRQWKRhfzLhoYTwIt71Fh2vxEcV9tcIfy_V-CHaLpvjvy-6UylunOkUK4FIplhaDH7cJs1uUng-E2HRT_rGf0we82tUSWkECfiaq2j7LCSZgAYFZBX8F9piZIQn6pm4VktfjFj8oar5v208TCETd971tq3K-7F6GQje1ilUlCXQz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAeMeWjHIQbVOQs-ZygSgtKPLYEt5uIQvU9GbygpIAPj66HCG4ibfPSjmc0WL5f2nrqI8ALODFQOXBEKAzP2q4HVkJMh4z-7VJ0eUf0FeiiVVrMXiWuJKiv1A7MdvkMG_ZWONMHTXbPQzcCYzrHK66Tha54i8PiYdr8yTr5UQ_Imyx2mEgJw_ZEocJQgwVx9tEkB6gYqXy4eznmgvvFwo5VeT3uEPHm-fnEndFUwENJhVx9Z8gk520QoyZ4N7K-7kVK5GpO5LIdv8s2aaGeyVUv_FAgchGmW-wsno9yKE0SPYN5bwwSsp09ZL655SPfItf1NEpHsngGEIeJZ8WLqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=fhlso8x5-yTB-qY44ooZxIVkVku0OPx94B4M4zEaoF250zvhmKcWefeX7mZta41EAwQICDosVKDmHlaoQhdOD3kdAjAn2UIgwp2T6U7nYzSkWft_u0yXMOEAetTOzCl0yOWmrrdlOQzuuctj67FEaJjwsGrARx61jM2Iklw1WpPkAPcpGEssbnb0ZbzJIHnJd25tc1NMaybyCsHSXmXTvJj4OsdKv9g2LP2-IycC7BAfSLv44HdcQcBrNeDOFq_MXPwMX2-HOIqN1nwYQ3st2ELzXVt7PDbEPqrU8K8ZioQIfriD2xHiAqqM_GBqgNqHO9QynBaZSeIg5crC8t7epg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=fhlso8x5-yTB-qY44ooZxIVkVku0OPx94B4M4zEaoF250zvhmKcWefeX7mZta41EAwQICDosVKDmHlaoQhdOD3kdAjAn2UIgwp2T6U7nYzSkWft_u0yXMOEAetTOzCl0yOWmrrdlOQzuuctj67FEaJjwsGrARx61jM2Iklw1WpPkAPcpGEssbnb0ZbzJIHnJd25tc1NMaybyCsHSXmXTvJj4OsdKv9g2LP2-IycC7BAfSLv44HdcQcBrNeDOFq_MXPwMX2-HOIqN1nwYQ3st2ELzXVt7PDbEPqrU8K8ZioQIfriD2xHiAqqM_GBqgNqHO9QynBaZSeIg5crC8t7epg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFPbMT9vraxH6Un1D_1Pfeo1tE3ekRIT8CMCOU3w1_nDpb_cb2zBiE2dVjWFiJ8MqFKPZeexmFHjPeyo849dHwkJ32yv-gMIMH6eilSGWMpGMmu-Y6R4eQue5a6bl0sDiLiZbgFPP1XWN8l38p2i9X3cS6WztMhza2a4x1OBYhmmxnhZs7C_jR4Tzd0mZLTLUAx34DMJqIaQR8k8mCUbSo1n7rvw5PM3nLnsnMNMLk-eDnVOFEueiZ6Gkno6ByI5usneCXx68CdfBc9NFLWbcdpQ3NZqNTmtt10V0duwlfg1RMsneDDBRl7AekCPbNd0E1gyQLXsg1ttKvDTuiArew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOyGI9217Blpa0yur3wLxibOxgLlF4ih6xLx8Bim54N0psvEp14uVFLJQgmxhrpl9CaBedf5FhwnsyUZkWl42ZKaIVy44O4TNZ4NrM8Z3V3uof5Do3pLQCVyfo1UDsQa2PPRjEs57MLqxs0OtIOjEjIBcQkbN4TJLHx5EpATgGq4So0DT46NZDsxWpkO9p5xh26G6pKRDRGw2gYV7P_IDaP24ky_1ROk3vPedyLjXgGFC2BYol-oNZI7_YOil_R8PjZxb-j5mNwmAnvDPrT6wE7-IJG-edqcev5ry0USsvWghmkFQJFFNHyC47gLWJm5Yuztcv1mMMcqtCcof1M5ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk6OQGpslaorY3apnPKF_Lsz684z5E6g2Eib8oOm2ip-qTJ-4HlOZJZwZOJ-1xQ3TAmG_jznqiohkzee9WY795bRnJb7lXJdIjacKrJCKMCBH0aD3esqGnW7_jcWwym2nODTGQDVDlx0jUb5-DVDlOsAql2_8f2KUVqPJ4_l-eMvMr4SZ1maO_Col_gNXfSrhE72vl1I0PvRbh6oikNtRVYn_EFeEf7pkxwHrwzcKH05g1ui4iFDdtrX1Vw-Fj7x4XlBSTxT1gRGlcL5OtNpWbgdRdAPZxw0lBtwWgjyQUJKsCBzTytxB1OKGIuIcXTrtwcLgJlIIeKdUUIwWErzA3co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=GAHyk1jb0_uGBWyWf-2LHRyzPfHdA55ibyo3fFcG8HoUNib39t3IsHnqeJGJQDLStEtXrbQXVshngbNdJxzDgOa60H0vTsEUhW3-iR4SodQF7jwBw4xHpqaoYpqMMeXNM311BAIK1NolGkVpXebtgXmRRhUzEpVtpcAfKtp4Ci3bw63WaP8C0TNVT8i3e4Vu5lhN85YPzjM8J8PXyNy4TW7uOzro_ag8IoP7-zJfO7Q3zc_kMShgfZBjS_Scvbx6NbImrt0dNuZFubvqPqbkjKE2uXyImIRcvyuv35iEY-wtYlQjQI-6mgXCxU-dHzbYMy8V9JQNFNxSb0emJNzYk6OQGpslaorY3apnPKF_Lsz684z5E6g2Eib8oOm2ip-qTJ-4HlOZJZwZOJ-1xQ3TAmG_jznqiohkzee9WY795bRnJb7lXJdIjacKrJCKMCBH0aD3esqGnW7_jcWwym2nODTGQDVDlx0jUb5-DVDlOsAql2_8f2KUVqPJ4_l-eMvMr4SZ1maO_Col_gNXfSrhE72vl1I0PvRbh6oikNtRVYn_EFeEf7pkxwHrwzcKH05g1ui4iFDdtrX1Vw-Fj7x4XlBSTxT1gRGlcL5OtNpWbgdRdAPZxw0lBtwWgjyQUJKsCBzTytxB1OKGIuIcXTrtwcLgJlIIeKdUUIwWErzA3co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Ou774CMSqwWK5PupqssNbTxbX0x_VksjQwLHOGMaBMgFqc6NM5a-luYuNHqel2G9-9f7gUwC8pi7qlA9zVCvi_uhg1MK_sgoSmjsCgeOz9U7gVnEIDzlSXU3R0RZULYlv26TUFtpDptyleaigF1DEdcZekmuUBX_Ix-7jQnxhfa6LYWNp-VKAx6w0j0RPtEA_CJajQFFyn8_bQZtLfeLGkmRtIsu4AbFs6VcRG9y28JozTIicPvfRxm9eU8Y5MCs9dSmNPjYrvq4cLOi5iDWR2naaxxwFHCnkZezQVm7_Awl0-rJeuP4juTTVkxMww6CD8s_bjF5Zm9kanoETuNsng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=Ou774CMSqwWK5PupqssNbTxbX0x_VksjQwLHOGMaBMgFqc6NM5a-luYuNHqel2G9-9f7gUwC8pi7qlA9zVCvi_uhg1MK_sgoSmjsCgeOz9U7gVnEIDzlSXU3R0RZULYlv26TUFtpDptyleaigF1DEdcZekmuUBX_Ix-7jQnxhfa6LYWNp-VKAx6w0j0RPtEA_CJajQFFyn8_bQZtLfeLGkmRtIsu4AbFs6VcRG9y28JozTIicPvfRxm9eU8Y5MCs9dSmNPjYrvq4cLOi5iDWR2naaxxwFHCnkZezQVm7_Awl0-rJeuP4juTTVkxMww6CD8s_bjF5Zm9kanoETuNsng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQaDWOh8bYCh5WjVVfb4oqd_PBeUb_UdtgsSJG4iuf5zn-cobKq_X-NNVTUzdXv7i9aLkVLX4DqZ87aRHchTQXsl4JFhfNr0o-0jF443Ct7VKOIP1PeK6BtnFVfvsP-MeMMTko6jLenKWmq85mOCN47r1UjsNwk9TcqW6y4GWK0orR4VXyYybU3Hora2VILUtCZmrHwCqmVEUscz8Cc6YxB99TdwqbpHbt10jyhIhBhIT3wtFDoZnABG7sq8G4gPtNB9ZvGRvcFCMqR-8Xslat2LeTSU8_GC2xGXhCcb4hHNxLXLQxUCQZcyNQae8982OVzxXvRjpUXCnmZRvSf5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptmCy7ud8AbUhU8hYjBvm2RuCaB9CSY7JdmDRyFVpEFnjdHOARpi2dHy0-FCTCcm5Tau39idAMRepk6ARSHih7wt4D8C2KAq7U_vtBHFU3MpUsTyN1PXKQ38KZnpbPkYhPorBXeAJ7KsTtCENvn-m8qriR4OKi2KggFtSGqcJPQti_N6PUi_HKgYCTerB5On7_4V_xhECkl4Q7-5rC72kRpE1KajNbuNcrLlK5mdc_CQOeDom97EwNnk_-_Y6vw9cvDh0WGS3bVye_gujlyv4T-oqwlr07aZC0j_Wwm0hsRr_b5aQbUu97OXG9tKAMNVir-cBWECxwuSAaBOh_zmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgHo6GxbO9BjW231dBZ-d-nThiufwaMIbwxZbK8LJTHv2EyawxTws7g4_aBAXO9W0qYnmCRVVCAWnic4M7VKdMO-H091TpvAaiHkMIE35ebIS0PoBm11QQr66447QdQeBrr3Lnhe-3MHxilJOjLJrAXtUAvi0cDP0lzrVuQDGH55PTeF4u76qgBwKHptrdl1D5Ae2R0Ze4IVGtgeZJR_GA_GRe5u0HfR-vJKr4QD6QCTWQity-a5o-A-cqJ9qu8dz052Pp1bKgaOnOYW4461ARUGwWyNdvSWKaqWon3i5WDcLjNzjBu3yDFbCPkSeA8uWgHoMhVH9cKudIAHhRzqsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYU9ivVcibq2Bikb16Qp3AatBw40l1BDONV5xKBSu8uwjNZ64J1a_Th5-Wju8jj6zBxsy2k7ssOgLIi3DJndb20mMdTxafKF5dRSN-UV4YPh1SvjLkHlRESSJHgPfNnXf-YSs9CobQien1JDjYfAyXtHlsRHVzii4nT9mGbW3kGZUQimliiDDhwBXfgpP9xTcschHO7fLtD8QS6huoP7W3QiLYuyWyzfaoYtOaz1FB96UcR5pLve_VG2hPtkmyAgDDwCoPdIAH9GGkbKAg9r3mipN36sOX0DeCjd8sBPVgsRYUJZ33NCOhP3mFKbBT0TWNv19cEE9b8DSM0FHBqf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc2DuwLgzNoYbmAdbMjHJWLxq4LH-BhKnTuF4HZ0bIMH4OLHQ7xlaSX_vVEoa26YIAv_wvIdi1e12tYcratjB0yMSpbdp8M2sDthKkBgjSvrTdt7I9ZF3qlVReFdUd-FYNtsrzMoX0Sr9h5KH-c_SLw5MwCFFQcpLzTZH0kXDYgAgJJKP1euDqU-ieXwITQV0ZLr6m275Muq8yiaBFnbI695UViLu6RKfVO6RxKmzrHt2xZBdnppA9wiPemFwz_0WWJ6IT7IEQMtdr5w3he2fBfnuCDyD7t9_tvcW3xpCG7wBdG-ALyKZgCiBYDFLrhICIaCNRBx1Jv7rr6c-XMZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=KwpqVyLwcc6SdG9dqJKcf-8syNw2M3iGIZCUVUYnZ9RMRXh_eBHwUm-G3DEsPYeejFbfUNsz0BEC0TL2qhTzTDxv7nKJ5QztEI0WG5L01bsyfRyYL6v4UnxV_7EmEVFNoJPV0Rj50n7AY_DjLo6wUI9BAXDSRDAG41QMbBdW_RYmpbMrOAb3Qe_FkYz-2RxK8qjl9NC2WmypGkhJOHeksR7G05f1Qyecwlzet5IBVTlZU7HIEYedlZfH5xet8kI9x1oidKsXygJaeI-9czZFhM8EtR5puSVfDzizyJqzM6gL4bRErgeYfBIJ6VqYDY5DLOI-k-xkI28xb49DarzKyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=KwpqVyLwcc6SdG9dqJKcf-8syNw2M3iGIZCUVUYnZ9RMRXh_eBHwUm-G3DEsPYeejFbfUNsz0BEC0TL2qhTzTDxv7nKJ5QztEI0WG5L01bsyfRyYL6v4UnxV_7EmEVFNoJPV0Rj50n7AY_DjLo6wUI9BAXDSRDAG41QMbBdW_RYmpbMrOAb3Qe_FkYz-2RxK8qjl9NC2WmypGkhJOHeksR7G05f1Qyecwlzet5IBVTlZU7HIEYedlZfH5xet8kI9x1oidKsXygJaeI-9czZFhM8EtR5puSVfDzizyJqzM6gL4bRErgeYfBIJ6VqYDY5DLOI-k-xkI28xb49DarzKyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1FrB356wqjB5w2VmYXV7Gwg-zaQqNx7WJfi1TNEPqajvEkPX6D6VqlNGD2lzdW7Y_5S1kBuDHgTzL_to4s4QVyyuCBPWh43tt-cELWULr8SefVUyTzXiBpPgQfaVbufc5-5I1ot41vUH7THp5foFR4gLpFS01Ba-vfRTcZ_3d4f_8G59S6Ag5WCFW_CC-W6ukYtjrOoW1HIKDd865RUYjo3vtuxNBK2geBrwCnAaQtrTBKXdmdFZj4ti0pd-y4tMQVMizPpL-oYypwpilZK7PzEVvsvwbui6lI8FkdU8SJ7XheY8vzE6LJZZ9Q1WrzSZ-DFasCekX7duDWq79fuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUe-7dntL46uzJ10JlOh80gEEaBI1eLxzfDqGrWrCDyLgRXTOvXwNGBiobhs9Lh_OIbdYdL8cHPUKNk49sb-_CxWi24wKuz03CkV_V_p4MliKjcRDsdK7qudPgGoR-PfkBiZ39EW1rDMuMXh4OAk9nBu5WbZpQO1juYDdH6GfF0W1giE2mTsMtsuATC5LWj2Jc_Kpw91lEkmZrSaRzf__M1rMcoy1U5kVt3iUHhsHx_QJ2AADh8UCTIPodLqhE1vH3aBMTrsMSZ1KvOhkeBnNhZRCUy8OQlg-hW9TFvgY-YrvJEPVLfYDbleSmfWlyFfOn99n4yAe-7y7XFGsXiKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=ku0_iPY3uNxiqpOdg50NRqDCOip78kiao0IcWoQrndB_VHFmaGxAMpyTP-eVbxOqcfpqPGcEpj4IgS5lZehhjH-rSxCljQET4TOF-2KQIcDAEhdoSVbNDEbK7f2AJ0n3Z3zLjKbAI4I4O4wnZvNNfnxOk6e456rfpEPwVb1YDWsfpEKdHHUnOZhWHqz2CWDZz3sh-5AdW7IfJdqFdDIuPTzqFgNEdaJCQO2BniLMtKdApK2je2UqrXR4wtN5agxdjM4sSqxoR0NSbRMx3LBDtAyqgJGmkO3-vvw8Vycbg-rmtiY8mNCoQwvH6QPpP3u9rKZ5OHOpRnF9dJto0ZqT6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=ku0_iPY3uNxiqpOdg50NRqDCOip78kiao0IcWoQrndB_VHFmaGxAMpyTP-eVbxOqcfpqPGcEpj4IgS5lZehhjH-rSxCljQET4TOF-2KQIcDAEhdoSVbNDEbK7f2AJ0n3Z3zLjKbAI4I4O4wnZvNNfnxOk6e456rfpEPwVb1YDWsfpEKdHHUnOZhWHqz2CWDZz3sh-5AdW7IfJdqFdDIuPTzqFgNEdaJCQO2BniLMtKdApK2je2UqrXR4wtN5agxdjM4sSqxoR0NSbRMx3LBDtAyqgJGmkO3-vvw8Vycbg-rmtiY8mNCoQwvH6QPpP3u9rKZ5OHOpRnF9dJto0ZqT6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCSz7-TEWZFTDmSLTRhUz5E6W1A9YammWklgZyLtHTOVaxSY-QpbY-H2nZNgh9oGpXEPlB2AAxN2_6aW1x-FwxUwpAzaDrIhIxZ3_ITThxd-huxk1xY_HSKtquPeVuR4czYsf1b9D-LAT13a3_Arp6ueciEgIhCFLMDUJetvx1YUgvuvU6LksieQ7OEC5UDqtsn3WqcG2_m9bD23d_59nz2t6OITVK49YhvGvQ5Tw8NSXZIxrwqj8MERYLlPNV6VgrrULPFQDL6zt87ZKlorap7t1Wb02L3hEsznel2I5cHwDrgxKGLCTwBuBEE7Han2nXTdtQ3o09Gha1ff-Rr_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfrtKmWAI8J8rsdeFVaww2gQmI5FQS4OV6eZ9ptmuSbDAt6PyUfjO2oiP1eWoyhFHHnNQD2wY0pk1m-v5Jxvf9iUq_ow9ZMU1UU5SbIvXGyDRpEQTgTzRA0iXo8dItKzeqKXXO239s_v2KnP58_jQf2EY1GKXxuQMWfZri_kH71B8CpGn1g6hRIZChK4Bx1cJuySpch7XI7uh9m4Ao5_JEOVPuqDCt2ninyHHJgETj-0dA6cRWxa2iD4BXqQnuBZMrBu9b19hwU7WOOO2-XFu68AWS4dhYDktBjBsc-GL4UrnETZQB47I1to1NdpKveY8NWbs-_UVCcj750VePWoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZTwSPyiNszT7ReSsxDfCLWVXEsfRBZByXJN33LxyxN__kRctFoEHvq7PFzLmqufTCYfveiiPqvfxDtFT7V6RLlQyXh6tBZjpmjZZ_6ZDpq5zdONRPjOdNskv30ESCMlg1XHgmgkxf9QwCIvRVQ0Lgd4OUU_OucL5G6LHvIRt4ktZaG--LR30LJNCCO8Iqbb4F6AHGTbodnhq5UoupD_FmHK6N3J4sSD0rBvO0un4wuVXj-mH2yUDwrUavyszcZcIE0g8iFxA-dWWheb0p4EyE5s39hyZTEX0BH-oxCq9Y7i_rYtxB0joQmbWADsI6CTE090-ozDhrJ4e-ryPeCBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNlkM5BKYZZIjQkFAKfYne-Pj38EWAgDpOTgFPoEUJwfX9PYcFUZbEPQfxJdUSo1rXVokWBTTRo5vTDIFP8GMEsrNVTm6iNKRFR3oq3Q7k3wwWSQ11lJiJEX0Rrdg-DCU_aYzaF9OecGZ3WDmV-vV7K5tfgCJlNhd4b3BuVZxpidy5NdO9nmCfYDuhHXC79_UjngTkJ1OrY_l5k8MitQ9qQ9Yer7k9RjveBGbxKTE6IHbdmDEdJxAO1ODK-4sFpb7a1jdqeltSJpN1yvmTtzs1wCPRK3xPlXzDPqgd7k8XIifbZKM6Dx6PdnCJXS63-eKI9czi3Pu6h46PpMDyFI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc7-7US0oXAUGekWL_G1F0YqqSQQDHTNWVyoOwciyqEqemyBzxSLUFBUl5uiW2lVxsvQV-_ROaY2Ak1mMaUWcwKkXMxhBrk57OAbh49JoyUeGFHRTQ-L2FHZ3urQNzgoGK6S3GjBSVcbtWxG1ca4hOxgpWASjtb0CGq8uJc7l1lKLYvrkcFU_l6WGTmZ5VGliQYMbnJgks3-losJCL8vGP5_wyKvoWBg1ayWC4xurYRKZqcKyssOVaXX9aPzjGw4q5YsKoR6Mqj62rENoeKFXBomsFC09VMzD1PF-TBpUW5dkEMbEqLFzCBA1GLXVdlfHvsM-fXhFsorX-YMh_P5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYxPhniZ0DQXhrnWt2qqzV_MA5LqgD8qQItaE5G1lRHgUP3th-NIiRM0ppT_-PuWbaDLgD-7dpAeGMBNhVtOCPe5mex4ge93T3POZKHWyudxPuUKh6hOz9mj3tyWUQCpRU0ERQ7gsT6o8WBp8lU7lFlA4ewGjxdpGZvpqV6psINruvyxZiN5EIEOCdZxnUq7j7K_Ql4p4xz-eolsK3JRTap3DE_XYz6vvgdBGdoKpXOx30-54OGuidnwk0ydPHpc0VX7rrfLHgKlJ4-iHeQhzKeO8orKvBKPPOPfGVp4VHDplDp3sfJt3B1_-tQQYV1eLxuWm_cV47KQ0jWN3vg2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=JfFDDD28_Gw9XPkUqP3ujHjlhNmotNcFi4DfuZurM1KNmAD9LNtI3NsF0Wh3_s7FV0swEahXOW4IcCBrR_xT1s6kYvpi-eWk5UCsgVVQezR2AEW2oYaxJHxQ25sdpf1ZadqyeBfDYUqi5jtLVkw3xQH1kNWmsFHU0J15qITF4fhU1_YpVx-hEEofxqB6E4pPHsktipDAEzLN1GNSjo6OdktQyyCcPoxt1oJPCcL784sitv0YK9oyDL9koEOEbW-hWqwJSJDJjF6WQbDifXL-WBcKk2_p0IeZNX67kE66x4MkpApHBRdOOe0FNzTQDa7WtYGMDMIPNyqdLXNxtvkVNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=JfFDDD28_Gw9XPkUqP3ujHjlhNmotNcFi4DfuZurM1KNmAD9LNtI3NsF0Wh3_s7FV0swEahXOW4IcCBrR_xT1s6kYvpi-eWk5UCsgVVQezR2AEW2oYaxJHxQ25sdpf1ZadqyeBfDYUqi5jtLVkw3xQH1kNWmsFHU0J15qITF4fhU1_YpVx-hEEofxqB6E4pPHsktipDAEzLN1GNSjo6OdktQyyCcPoxt1oJPCcL784sitv0YK9oyDL9koEOEbW-hWqwJSJDJjF6WQbDifXL-WBcKk2_p0IeZNX67kE66x4MkpApHBRdOOe0FNzTQDa7WtYGMDMIPNyqdLXNxtvkVNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcYytkOty2SMe1aRgvvsnn-iLn9qpVYxudngr1i5xNnWiLw6fBsXlN6RhILrrMOfll4ypjBnWiCi_0MNXjreIz8xXrfdIEjlRusxI8JpCAWCNSgJIm1T0M1hnB2SI6pqoDGgl7Sqa-BRAYAtTX48IuoDmHKPWXjBiVU3-t0PGgeVJjHERdzK5vYOSLT2MxBaF6YSz52FddKDdXIaa-oQds2WKAyvD0a5st04LKtkP0Uk_73plK7U48hH_h2EG0U3YhwqYN8b8xqGeS8pHXX17ZU1nBPx8wY2ehvyPAfA65houdq_4Gk7qf57ObL16tqdQvTTEwNosRPSBsf8bghLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23589" target="_blank">📅 13:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMlD1TYYiZ1azHbkBOCItIfXKjmot2AVv0DfYjnidhpJo1Y35pnbkDaoYvEMNNqdNDsDuLbpvJic8B-etaNxUY392d3Xv3Tpt1rC2IqVeiGus8xRJ8tyPJV1SRVnDPdUieUsc_oXzXzyQ8XmDwPbTbhxxW492VDIsNb8lMPcQPP40WUgAuDVjddnAq0ps9_P7woRTRh44MlFf92xSZByIO6WoTI2o3ZQp6v_f4KBrgV3zfwvw8j81rXjugp55MG1umAzSXZ9tI1nOqU0Rj1Ur7G0bUcMpzfGWme5GrcbPaGEIN48RTWy-FNzkxIBI_PsQOBWEaRURK9xwv9nFPBSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دهنت‌ سرویس پسر یه حرکتی زدی شدی سوژه همه؛ حالا تیری هانری اسطوره آرسنال دیگر کارشناس شبکه جام جهانیم درباره خوشحالی بعد گل محمد محبی گفته فکر نمی کنم منظور بدی داشته باشه. خودِ محمد محبیم گفته بخدا فقط یه خوشحالی ساده بود که اون لحظه به ذهنم رسید.…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23588" target="_blank">📅 12:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbNu2odCzqVVZ6lRSxMEhJGDtmMz2gHekIBEUBuQrivdeTdYqofwjpvsqUB8Zxj65GjErHEHu3HniXhMOk3ENdDbKdAfX-STbhLVlTOEBKq1VNi63wEJ2WriYzNx34jEq1hA6L_KGy-FXOY6Vln568EnTs9OiRO_RHMSUPS3WRXyUew2SerzDCvaUAQ8JPTGI8isVKRMCsJa_GFiDdwY51W188M98BJK-mZa4oUuXksk0_aO17tlElFtgqywcGNPOrf3LC1pzw5id-XtqEDNcuMtvc8ZqCYN-GpB4QEyz4XYK0WOnG9IxL45FwoN1Wouph3rEU9ubUJNhqYzeloqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23587" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXocdb7g3PM5iR9vaL_xnxR27H7L1Xzt-7TEUivsN84hVjpc6aySTJXjE0STv1H5fxFEFRYIkSXJKqIQFS7CkmpNTnsqN6nIOvJM-xXFPWXlgNOWuc0BAKRX3yozkEL7C2vvPcgk8Auj-S_dRJC0c9MVtGU9Dt81uBE_nkQHLcHPqOWh-PBJ2YmPnRxLZPd3qdqDDdwg8zNEgjU_rFcBgpHI2ib34q_EFki2LEJAuvxdXWrpGW5WxApxupE2DyM_sb_YHypYx1b3PRmuI2R_FQpwmlttb9frbjtgdEmNEQq9XP3PvhX_RIa1jgDOqGCH7bB3OfcU6cQn033NbsZ2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درباره وضعیت آریا یوسفی، محمد امین حزباوی و مهدی لیموچی که هرسه مدنظر باشگاه پرسپولیس است و مدیریت‌این‌باشگاه مذاکراتی‌نیز با مدیربرنامه آن‌ها داشته بزودی اخبار تکمیلی رو خواهم گفت.
‼️
آریا یوسفی جواب تماس‌های مدیران سپاهان رو نمیده و چند بار گفته یا لژیونر…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23586" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-v7IbTbXdchsP3pLWzKECEUbjhS4LlpfBViASVhfpUyTKmfQz8cm2wwy3rsFTCFGabzCGOOO_eyWAotzHTbXaDYh9dmHzI_S0umYssLtZnnX7gVkTllicy0yvjTX0Fki0LHIs9Qa3HYQ8qFR6WICtZuV7rLjMNQLMeoXeXEd1HYkZqoQHmCihfyMsB0IgrNLgK5v0jKztn2J3XGko9o-QOA1VW8N5gijsYREBf5UyjPtNwq0vVpA7xI2sNCO3Jau4M03JiGcxmEqMaYyGLIjX_-6yyb7Kxlk5pHEZd4NQ3W2xt-3Q3PDlpXZrXSNTyEei0mEjiaXcRDYfTik4IX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeOp4JP0AhdduHJukkzvda0h7n8s0I59fDkhHVnYWyRmU0G5GSdvE2ezppAmNpVb4os1i1bvC9nyV29irnek4zHHNXdvj2-KYUmlHatUaxzpmdVCb4gAlUJmR4PYxi921QtzWDzlbrYMn4FAeVbqoZHNATc5_3k3PV9aowVFE3Q695KKS-v--SQ9T4JL7X_7Vw6A-wdYQ9XXlChbOneUxOxBDmnAMdSm7TkOgcTht19rbwfxrvRSSaIPerxpo-8RM2KxkUw8oQCIbW-iJveH4I2WP5c8SgrHFH0gYZXeSKUQDxzLVZAVpgeqmECSr7BZdCWY3JhFcD_S-UkgB_VP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW4gvmwdTKM4SlEU_5qG1d8trxOerIxEFe88vXKhWUc4fEkSQQQxjM55CdkUgdEquWNMJ0peV2RxzPlcEY6dd342Tg3OKz_5C_ACI4DCxoUtusULjgCFwhA1DhnTC5M8zi93-C6BK0TXsAE6B8jo02ngJxLLURay5znKhlSMbU_ZF54IseVDtfzGJzhiFScf-po14QnvKj1wB9ppYx--psqRnch1E3cdctWBL97wAnPJtcl-J7V6yf99MVuibWpUcKIRUZtuyZz95IhT25EvLrlPAtraRLbdrVMcNVTeq5YnOxPulnm_GoIRkxYZSd0a-DZK6A3xqUJHyz2HT78p-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGSVHKC8I_9ebO0FYfT5VH2iWhtPXrfvTLYoBR947Xwn3AHrT-BkQYt2G7Or21nrX3WbBrToah91hpVocMNuSDxqDjzgDL9sRn0xsTyd9wG1ZmHeNGE24Pm-j9EPlIeXkQfiUXqkiEc6ueqmFlODAj68MUyIH0I6sBHNmVrKGk0jp71jpheTV5cQooiSmJyUk6YkaprLURYkfeCsBFdwqXxEX1m--_g-uBbyYro2DGCHEIg0XuuAGOVhUBZQln1Wcjbg5xKQUR7NRy38nMMp8OdJR9xtIRRgqP0IZw6Um2dS1AQgAzsUKnIQwH1w2QkbwKD07jC-YTIK7mHxbaoi_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=vymnQR0WG521vSxJvlKaKpFOwc3ZSjeHRN_laFGL3JjMTNuW_QK_ONAiQq8GqLw8Mlz04ftqEqKYt8mYITWlF35LFGCfu8bGq6FNb9805rjrAd9wq45XpYnIDJfZ6ALuXCnJuZ8wh28odHGFr56N1w18N1IaY80PgE5QQHI71ovShUtNu6_qrqz0VIaVMO6jfeUlf06iLs_UrQjMISt5TVqR0UgBbiB2bxUbkLCaDc8aID2hXw20fLB51nna3DCy9AD-GLMNALo2UqYZJ1rAEJRE3KRuH4fTX0RoC43lT1ZshDqZpX-DH3blCQFVaj5lWhibOuxrfPobMNO3x1pE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=vymnQR0WG521vSxJvlKaKpFOwc3ZSjeHRN_laFGL3JjMTNuW_QK_ONAiQq8GqLw8Mlz04ftqEqKYt8mYITWlF35LFGCfu8bGq6FNb9805rjrAd9wq45XpYnIDJfZ6ALuXCnJuZ8wh28odHGFr56N1w18N1IaY80PgE5QQHI71ovShUtNu6_qrqz0VIaVMO6jfeUlf06iLs_UrQjMISt5TVqR0UgBbiB2bxUbkLCaDc8aID2hXw20fLB51nna3DCy9AD-GLMNALo2UqYZJ1rAEJRE3KRuH4fTX0RoC43lT1ZshDqZpX-DH3blCQFVaj5lWhibOuxrfPobMNO3x1pE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGmXuXRv9lcf7711RGUiy4cFmRj8I6C0j3bfQ5B1_PAXCiWepJfkk0xlzEnOb-WmqloLd2eDabHoH62A_6fp-OXI-qyObWy_CAejxp6Q4_JWx_rmArYRfgTCpe78-JNDacnjH_Jk9ggvsz4VIB8fj7hoXzXN5nQ8dDZEG2mnxKjmin21L5I7lSkGaBjlThZAhwh0Hkzwzv5reHo8bM-F2FpVk2TMoUcvMbVRXplYSt65a_k7hqHeWxvP30vGy3FyHT3sG7x4HttpHfzhRkurU0quR8MbIgxu6t_33cT1P-4w7wEcRyIHI2y2VVDGAqWs6r5PdPgKpSSvboeB0l_oKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=gjqNflDUEAXz86OQOssqirVtSf_FegBh-GNe6Fo9f-LCVJyAfMS2bQNWDt-bTOLEU3-jC-1VBfJBHgJqU7FXDoH8XJKdI5aNgGeogEP6S8H3cjhXd20m8DxH1XPvuiwMCMqcdlmvOwWH3F6oSfPPfPqW3IdTzIOc61r97IRbth7LCfteM5cPe5pwQuNyMb8G3UGAMEns-dv1rppv7ohV2KUKpfAi0lw5ilvzfCYs9tmOoDxguU9m0Cm80ualiDWzsZKtfLPUR3D88Jg90jF53dhLje1SHVJMBbcSfk5g7aF9AdUa9NvYbOpHGmbG9mzCM5TjqG67FC-5k44vne62zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=gjqNflDUEAXz86OQOssqirVtSf_FegBh-GNe6Fo9f-LCVJyAfMS2bQNWDt-bTOLEU3-jC-1VBfJBHgJqU7FXDoH8XJKdI5aNgGeogEP6S8H3cjhXd20m8DxH1XPvuiwMCMqcdlmvOwWH3F6oSfPPfPqW3IdTzIOc61r97IRbth7LCfteM5cPe5pwQuNyMb8G3UGAMEns-dv1rppv7ohV2KUKpfAi0lw5ilvzfCYs9tmOoDxguU9m0Cm80ualiDWzsZKtfLPUR3D88Jg90jF53dhLje1SHVJMBbcSfk5g7aF9AdUa9NvYbOpHGmbG9mzCM5TjqG67FC-5k44vne62zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF4nXhTzif6X3FD3P3J4W6yxvclMmJvn1DA7F_m9N739Sjvfhk84yfZvhbhQyJsVJx6byoOYQNdwYQasRaARCaUupVw5vC7AhUvHKnyu3Mh89R5Xj70nulHfbVEza9z1EFpWLKNczGJFpm2YldNNtn_XsmvdmLJFflNz_0xR0R3TeyTyTHJVTZPOwWoTbCKqBirN0FWYX3x5hiwTtcJ7d12dJFc0fYBMTAyR3tENQDjjl4D-c6eF6cVhd80teYS3gRS7fxXqkBlxJqnoUmL7uSTPJfTGqau4z35lsYT-e1FVKMPDoOBGrnqxO8aLhokY-hhdZUrn-bT0QUuxje6-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzQY64QM5Xxa5s2jRItCpGx790oxfW_32qmzl6dxh49YEUmzyNZQ8nUlvNVXnTuHwtuGmsfitwTWwZos71hRHCQJkxt8L6f7t2pFYrL_r32w1zNgVyoOtriP0adS388Mk4yanEqynAOvDxf_O6v91bglV0qeFzKPJYZvOjwYSfi69aFCo96oHKXt_BEzTxMn5LjziviZvwkt6X1KMcA0dAmwy6Hol6SYsX0b1SUVBz54ZZs2hIgtbrJE8-WMJVVDT_Y-e8S6_bn2M7LEbJM16EIssa_Z312uMpz9cPdKVXT0A4-CLgJ6FLWJPais8Nl0mJitP-YN4PlCN6tVA-l8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23576" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23575">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a244147c.mp4?token=ddxojmrMXj2hOm5rgSW1siaP-OyT5nrisQTfc8t0jUjtJ9c7ZC04fEpFYcg_oPc7oFhc1KuHN9Ch2lAf-IVC9bGjtGqfUjZccLle2kd9AbdQh5mJ75oZ6CyaaVHvR9_n8iGXkgVwr2PmCtdseJ1BSc08BOijrs3iUTWlWKr5DOJ67xsNgc6QTPN86BHCFf20BweiTw5fulIeLggvcrf1l9Fd86XPBcu4JsDnk5Lx_Yznpy0K09zzP0SC-xVMHK8UKKS14cV9S-zEPKVnGXbfE3B7fsEZJ9nda3yaLT29RavKk9EmADgYIwyjoQgxGPAyC405-xcB_4USyTvBVY44xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a244147c.mp4?token=ddxojmrMXj2hOm5rgSW1siaP-OyT5nrisQTfc8t0jUjtJ9c7ZC04fEpFYcg_oPc7oFhc1KuHN9Ch2lAf-IVC9bGjtGqfUjZccLle2kd9AbdQh5mJ75oZ6CyaaVHvR9_n8iGXkgVwr2PmCtdseJ1BSc08BOijrs3iUTWlWKr5DOJ67xsNgc6QTPN86BHCFf20BweiTw5fulIeLggvcrf1l9Fd86XPBcu4JsDnk5Lx_Yznpy0K09zzP0SC-xVMHK8UKKS14cV9S-zEPKVnGXbfE3B7fsEZJ9nda3yaLT29RavKk9EmADgYIwyjoQgxGPAyC405-xcB_4USyTvBVY44xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سوپرگل‌دیدنی‌امام عاشور ستاره‌تیم‌ملی مصر در بازی روزگذشته مقابل بلژیک درهفته اول جام‌جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23575" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23573">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIB0RzUMU5DFYm0AgcNPrjA_zBkH_xXwL3R7tukM2QBKhkifJCjzAO5raBDfS3VJIbmc-PoLuwgSKYC2OwE8GlCvoRVx2LhMErWxI5OHiUDmppGEpbjpckZ9TtPOZgJKQbe4K1O0bhDH4mPkJwlxGcaatxHhdF-v-VZRDM0lRaJ1nfcZQRrCPtUBrIG5ON0HeYiXSxEigjceKeOgXUGxHa4F2ej-3yCUzT957Y6YCBfV-3OqOdk8UPmrtN4rc1A8SqcAxfpdAmfsTVuyG9-ztMvoeuqqIl_URXlPVoLm2hnS9hblLE8oADduYc7cSyG1CdFdPXx9piJJHNC_f01mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23573" target="_blank">📅 09:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23572">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7jrPF_KWzl91WTHWvuKHiWB9WaacDQhTxhl6d9w2yJgVMQCYQCvzuQqGKFz1l1MxxkJfBzgbt_myW2-j3EZn7AEuePlPOh709maFXe4T2dHhv1PPAmQz5vbRLtR8fQJ0kTmxoVOtq7X2bdnAGEDi2qrSBxU4YuSoQTCugD-l8UR0a3GVReOxsdbUEETbGIoJQAQrZamYGHznn6a_-C6YxK5B0YbBxo-cnmh1Kj5vPjc-VHhMI1eFwhk2BWor5L-gpIUa53XkCvfzRCjmX2TnphMWzhRvRUAWOp-kADRUx1M72Gwxv0Zoa1scrsTCuVW0J7L8U74PmexXifTI7jpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23572" target="_blank">📅 09:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=hA3UcoJKl6kmAQsLYleeB-xYDqh6v95O1XaQuWuovN6RCv6LlkXYMRPpkbgQe7CjCKwtLF0Eb98n49GDt9ZgyMT_vVJaw_5uhw1vqK-GNt7wU9q5AilPUqCY_ROXEMxMZsqr_xweCk15_e5t7jY685TFVyhIiX-Onru0PPnqogIl2T-9zav7V5puVb4MDeejtfwX1fzuek30Nr52187qVac9n7iSoXvH9rAXj4CVFEoTi2VHsoUFf9otFyO1qsQxvmMhUN90EXvy0LGBWCKCiOcF-_Y_Ev5TTBVDrB27vxf-axi7l05DkoTisfgyYKdmJtdHJuHH7_VZSH6rIhf6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607d3917ea.mp4?token=hA3UcoJKl6kmAQsLYleeB-xYDqh6v95O1XaQuWuovN6RCv6LlkXYMRPpkbgQe7CjCKwtLF0Eb98n49GDt9ZgyMT_vVJaw_5uhw1vqK-GNt7wU9q5AilPUqCY_ROXEMxMZsqr_xweCk15_e5t7jY685TFVyhIiX-Onru0PPnqogIl2T-9zav7V5puVb4MDeejtfwX1fzuek30Nr52187qVac9n7iSoXvH9rAXj4CVFEoTi2VHsoUFf9otFyO1qsQxvmMhUN90EXvy0LGBWCKCiOcF-_Y_Ev5TTBVDrB27vxf-axi7l05DkoTisfgyYKdmJtdHJuHH7_VZSH6rIhf6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ولاتی امیر حسین قیاسی خطاب به محمدحسین میثاقی مجری سازمان صداوسیما
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23571" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23570">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUEc-QTid3630WF4lxkVGBJdaHj6JPNo5Sxb_0qHqgX9G35eHwDd-4rgpbKHW2rDRA7zAydTj31A7WCq3Lvl4RaBCErtYwvyqA-M8xw2_tL2ZsNI4lLYXU5N8VmO9k3aooVYr_qGjS96q9XIKjuTrTLnD-ckghso8jfAuUjpSb37bmqk-YH9EZ2JU9mP7ktOnvtuYawrjJ3kJWkq988zL3Hpa6gjgGLSCrJBzUSApEGgc6iGCZVv-B0UHHTAcr7SenwZgftMGgLQ-5tEVz2_7yl1VPJH3a0squXnatc2OG-kiBT0r4V-_PAVDoWURZL1wB3W7L7fXkGbvLuv81pR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇯🇵
موریاسو سرمربی با تجربه تیم ملی ژاپن با شنیدن سرودملی‌کشورش‌اشک ریخت. یکی از تاثیر گذارترین عکس های جام جهانی تا اینجای کار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23570" target="_blank">📅 09:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23569">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=GzwC2hxIX8IwOuwDhd-d-NxSpytK7u9Zoq-DDXr8m7g_RAHAmtWf3SExPYKshRNZT3V-qR74nJSmUl_m72XuELdX6IQH4lpDquN4tZf1zOd4KXqOONONAaoJ5foMdr72rxCaxVy73qkErI3uAuN-wDKBBu-UT_pctORB0-Lk_pwFWrWtQznd469eVVXVEMHz_XAbwJliMy-t1IQAtBitQ6WCBUFT42xrzqNvEBOg1bSCL7-GFIglz834d1-xFuSJn5I6Laj2dZT3MEYj7_ZvQUjjyZQbuAn3vOUtoyBOq-SHhgwseKpFjBS0xy5N1HCD3lF-HWLcGbXbUyUSElDjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e9cf628c.mp4?token=GzwC2hxIX8IwOuwDhd-d-NxSpytK7u9Zoq-DDXr8m7g_RAHAmtWf3SExPYKshRNZT3V-qR74nJSmUl_m72XuELdX6IQH4lpDquN4tZf1zOd4KXqOONONAaoJ5foMdr72rxCaxVy73qkErI3uAuN-wDKBBu-UT_pctORB0-Lk_pwFWrWtQznd469eVVXVEMHz_XAbwJliMy-t1IQAtBitQ6WCBUFT42xrzqNvEBOg1bSCL7-GFIglz834d1-xFuSJn5I6Laj2dZT3MEYj7_ZvQUjjyZQbuAn3vOUtoyBOq-SHhgwseKpFjBS0xy5N1HCD3lF-HWLcGbXbUyUSElDjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی در نشست خبری هم ولکن ساعت رولکسش نشد و به‌این‌شکل‌اون‌رو به نمایش گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23569" target="_blank">📅 08:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23568">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-n-x5dVzk9MM1mfzpITGZuAHPfc4Y3d3SUqq9-lf6wh30zSj6mgvx3albPBmFP2lV3JdmHH9lqAWvoZ8Ff2PO5TbzYs0ip9CPzbmEXMTP3vGeDzApX3qbXxQWLgq9W-C9N605xegI0px0ZKyceuiDVV912BMsP-73mLSrV2dGjLCZSZDDs2JGuqNjfHdBUdPxLiZvUMjQaPl2KQoFmImjPH08XRS5MQw9LKkCPupKliqBPmkltCrK2RyPlmoJw_V3TbY6g_QlmVhPnN0D7AhccjJZ-a01BLVBGm8sFlLP1iDWour8EC-1GJsd4rteIw6BzJBTVnxHjW7FSKyaqneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌ بنده‌خدا دیگه رو برد امشب بلژیک مقابل مصر 8.5 میلیون دلار شرط‌بسته‌بود که خیلی شیک باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23568" target="_blank">📅 08:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nogsIn7td_iGifnprRC_jSKbE8IIS503ftFCLr23nQVoR2OX98Y620hDznGkgAlD_MbSXXwYH-wfzMlD5FSZi7nJwzvq5N7dJlpsUGsEmQEfltPpGY6O2_yX2Sv1-4JnN5HnJzPBBqhlg-e4cHYBTe9576pgbn_q5rJEg4toz0vO9Cmy5hvRe4GlUwAdJ7XoXc2Pi6mazgN8UjrWvU985MAw9YSRyeguonhXGynALtPx9pnQOpqBZXV2oduWv_TbMHN1CHUk0RWbH_qOLIV-WYYqN1eIJB1-bKCywaR3bpquMovsspbRC8jdkh2CO3E65umt3wy6yAVF4b29A5hdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdJwKeDUswV-0iGbn7G7qNDrdU1P3Oo3wvKgUlk2yJnL3fP1SOs2d6WXqYcJMtGskrJtcU0wRgO-KixF8V_aT4-YoQkcvLbJBUknlnFKsHJjnvsLD94JJ-_gsbpRlMHT3poB2E347-x-7zdHIArf0eN8BqMhMC143xU0u30yFuTlnLvUf83PPK2rukpU9iNoZZe1tbWMJ4iZ9uLMMsGpuEtN0cIGPXn01SW0EE_Qk4L_u0ZYU150Da1R-mIso44aiQSQ-cXjrUYfFEv40b0VTghzZfbdmsrbJrTAsIGy3XTTyjdPHhFgNRyRzDNtmNCvvgbU4wsb3cAj0E0-EBxJEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
نیمار جونیور اعلام کرد که پارتنرش بارداره و قراره یه دختر خوشکل دیگه براش بیاره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23566" target="_blank">📅 08:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws_Pzh-OlH8Nw3FcNrALqx0ZgsIoQocIAxEBtZ6cWuH9mRJuV5UdWDabJe4UdxEExs3d7LZsW2EV8JRIyOGRMqmSXql1vXYXPoxiLvpbHGXfNvFWsYxOXiL8GCS-2-oWAZZ_TvQsmtaHa735tOOP61X2nEMxwqyPApnInGD02kLkXkgMGGQSGbAyzlSqo_mvxkSv8J314yUw3HifPL99V_W5FMqcFBgyx9wNZLLjvTVZ6EsJmxkkZbQxZnZLBj9Zm7XRsPAIXocI73W4AEi9ceJa6NMHvq4zCIKXt2BS9Ck1As8zr2x9n-b0KnnHp1YNaCoHChbGOR4kMTs3dMGpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23565" target="_blank">📅 07:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=gYVm9uXKoKlCyE0-fh09PlpK6JlYFFPHUrdNTDYd67A98psT1x8e7xoUXFbXuCdvl-_iBviwpFRPcc5qdm6-09h4WrcGcztzRS9m0rRd34VdYNs695fckV2u14i74Xbbh91STwOnLibhflnjli7XtTsE5Nc05YHbHS_J2rFkyejuYMUj6zbrc2Q51mQm5EltRR5Vgan2SsfQG8hF6JPdRkDx0v5xyxIfumakUf_3lBr9gvRaj-ALlhlX9whQ4Rp0bOTtyY4IGnuHFC2iCFRaM1mVRuk-4c1SbYn4y1l3aZOq3_ljqN-39IvUtcq_nebTy8j1TYgn_-6WbYin0MdKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae8867bbe.mp4?token=gYVm9uXKoKlCyE0-fh09PlpK6JlYFFPHUrdNTDYd67A98psT1x8e7xoUXFbXuCdvl-_iBviwpFRPcc5qdm6-09h4WrcGcztzRS9m0rRd34VdYNs695fckV2u14i74Xbbh91STwOnLibhflnjli7XtTsE5Nc05YHbHS_J2rFkyejuYMUj6zbrc2Q51mQm5EltRR5Vgan2SsfQG8hF6JPdRkDx0v5xyxIfumakUf_3lBr9gvRaj-ALlhlX9whQ4Rp0bOTtyY4IGnuHFC2iCFRaM1mVRuk-4c1SbYn4y1l3aZOq3_ljqN-39IvUtcq_nebTy8j1TYgn_-6WbYin0MdKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل‌های دیدار امروز صبح دو تیم ایران - نیوزیلند در گام نخست رقابت‌های جام جهانی؛ رامین رضاییان بعنوان بهترین بازیکن زمین مسابقه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23564" target="_blank">📅 07:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=rj8NQX3aDjB4HIweFlSqrh71hflyZMPz1Mdp44UtnAkhSf_AQ21HChLzy85-z5mNTIImDv0aLRo7P6Mf009nkq7M0trgfchDKlA0aYE7N5g4CfIrC7-RvJABDRyWoTdkIzQopFisusCuSGTeJUiW7XVLYrQQFwM15vw6XpXpiP8Gtd36hTdSgf2Onv4SdekT_VH8-mF_NOAuPyB8dc8t7mKuaMTsq2gA6FbtWdBFN_6Xdit-lKgwnlpmSQHS5ScJIhcfj_fPLknrUvd0738psv4BDj4HtKoDHvhlym6hG5O3U6JpPPTVQCAEuSJLrb2dYW0bCRbOzPaGQ1tVes45Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16918ae52.mp4?token=rj8NQX3aDjB4HIweFlSqrh71hflyZMPz1Mdp44UtnAkhSf_AQ21HChLzy85-z5mNTIImDv0aLRo7P6Mf009nkq7M0trgfchDKlA0aYE7N5g4CfIrC7-RvJABDRyWoTdkIzQopFisusCuSGTeJUiW7XVLYrQQFwM15vw6XpXpiP8Gtd36hTdSgf2Onv4SdekT_VH8-mF_NOAuPyB8dc8t7mKuaMTsq2gA6FbtWdBFN_6Xdit-lKgwnlpmSQHS5ScJIhcfj_fPLknrUvd0738psv4BDj4HtKoDHvhlym6hG5O3U6JpPPTVQCAEuSJLrb2dYW0bCRbOzPaGQ1tVes45Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23563" target="_blank">📅 07:26 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
