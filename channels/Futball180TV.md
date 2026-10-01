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
<img src="https://cdn5.telesco.pe/file/RAaJayT3WAfGucXPGu6W27Rmzumka1DVmQSoP9lgUJYjALrZS4GfSNlPUHLHXpITbMjY9m18xzJckvYHsI7va3qxO7uWNnlVmYUgh_tnlJtC5ZuzgpeeR4VvqczBdX0jpme5yxbJrtVvY5yfsAwG4UBuBjShXd6JfcTbSF7dSKfU0Pi6IIsYx-AZxgB0V4ZWVKBRKN4SdK_5cGJJZj4Txrp_JWpCGmwJ1QaH_ml6pYJGrESnIkwotdpvWdH48eHG3g_uAF_NaYi4PWK3dJYfEpmOmWKriMukHkf60qtBkbKBnMDgR5UFsmfkQARiJgRSOd2sgpEhSpTR_V_Tmx-2uQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 395K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-107610">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خلاصه مقاله جاناتان لیو‌ در گاردین در مورد ابعاد ژئوپولیتیک پرونده منچسترسیتی
🔻
برشی از متن: شما به جای ابوظبی(مالک‌ سیتی) و عربستان سعودی(مالک نیوکاسل)، به راحتی می‌توانید جف بزوس، عضوی از کنسرسیومی که اکنون تقریباً ۴۰٪ از سهام باشگاه فوتبال لیورپول را در اختیار دارد یا متا یا ایلان ماسک یا بنیامین نتانیاهو یا دونالد ترامپ را بگذارید:
یک طبقه کامل از مردانی که هیچ مرجعی فراتر از خودشان را نمی‌شناسند، کسانی که به سیاست و تجارت و ورزش و فرهنگ همیشه به یک شکل نگاه می کنند: بازی‌ است که رقیب باید به هر وسیله ممکن به زانو درآید.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/Futball180TV/107610" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107609">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=fATn8rqdh1-s4GkByFtIwjrXKytrHY6y1uC_KcFead5jaZuat9H_GgX14Nx-8ZFXZuQVRv0TOghic9IAJzKUlLQTbSoZuwxakbomY7cH2-vGFtRR3rZ6Uj7hUgLVmvbZOWTlwr1bsMwjYMeFGhSwX0muo1UneJUT07-QP8LDbhUfPa19tXFQiQPjlQm36L__JvlHXdT8yME0b44UpOl3injkiVd9sVR8YTKuuupqwrssx-QucwQC6zceGLzNYdbsEpPkxyy7-v9BQmmeIiPI3sJFGNHflYXociJNn6aVv3OEln3dR8390rv8hkONYu46ztSwmJ18ypHHEwDCwKQIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20411da1e7.mp4?token=fATn8rqdh1-s4GkByFtIwjrXKytrHY6y1uC_KcFead5jaZuat9H_GgX14Nx-8ZFXZuQVRv0TOghic9IAJzKUlLQTbSoZuwxakbomY7cH2-vGFtRR3rZ6Uj7hUgLVmvbZOWTlwr1bsMwjYMeFGhSwX0muo1UneJUT07-QP8LDbhUfPa19tXFQiQPjlQm36L__JvlHXdT8yME0b44UpOl3injkiVd9sVR8YTKuuupqwrssx-QucwQC6zceGLzNYdbsEpPkxyy7-v9BQmmeIiPI3sJFGNHflYXociJNn6aVv3OEln3dR8390rv8hkONYu46ztSwmJ18ypHHEwDCwKQIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
دور دور بیژن‌مرتضوی و زنش در تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/107609" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107608">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=ONzQLy-uQoNbgGzpmgFSR2qS0UX8t0Z3c_IV_AiBzYEFNCkZVDsRtNEQoXLHRsk-cEbEGqi3F_cL6NaXbEvf-eAunQNZFGLCRokgkknZxJKhmtdNbaHL8FDDE-QI5Aqk_MlwIBdJyhyIuBdXDqGYAdhGqewxYzwfcU-mFCT-kpn5zIWgX-oa6CmMbpA7LEvCpptf9IqRKugBpnlr9mrb4JJzKdn6T7mmlm2ys1tCGynF4IuKjJODGViHEAcguAYJf3eiWOYIZZwiWQ714P_udWe-SBhd87FJNmnCTV_LFumBOOGxQJG_WnTO0iYovqOQmFJ1Kou0XQDmmBxN5oSvbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a1969c57.mp4?token=ONzQLy-uQoNbgGzpmgFSR2qS0UX8t0Z3c_IV_AiBzYEFNCkZVDsRtNEQoXLHRsk-cEbEGqi3F_cL6NaXbEvf-eAunQNZFGLCRokgkknZxJKhmtdNbaHL8FDDE-QI5Aqk_MlwIBdJyhyIuBdXDqGYAdhGqewxYzwfcU-mFCT-kpn5zIWgX-oa6CmMbpA7LEvCpptf9IqRKugBpnlr9mrb4JJzKdn6T7mmlm2ys1tCGynF4IuKjJODGViHEAcguAYJf3eiWOYIZZwiWQ714P_udWe-SBhd87FJNmnCTV_LFumBOOGxQJG_WnTO0iYovqOQmFJ1Kou0XQDmmBxN5oSvbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
حنیف عمران‌زاده مدافع سابق استقلال:
من توی دربی که چهارتا خوردیم هم بودم.
آرش رو گذاشتن وینگر که فکر نمی‌کنم اصلا اون‌جا بازی کرده بود. حالا دلیلشون چی بود؟ این‌که رامین رضاییان هی نفوذ می‌کنه از آرش بترسه و جلوی نفوذ رامین رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/Futball180TV/107608" target="_blank">📅 16:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107607">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e980239cb3.mp4?token=LY0DM09-JxmscmmHKyg_l9_esk4EUBCsUwu6nLvDh6IQnrfmzSzLxIV4hOyvCIQ0ySq9STH1kVjmnq0W2Y7eh2ycpIX07abVJr6EMYadamHAYtE-5lnKjxRpzwvAeXiGoQFzqQvN097F3HrnUAEACuXGZPS33CJmqDRtLYmJuUGcqGdZdlFFSdl5Xe9rYCQyP4ewKJx6lzYqWb13OhCViFLN4z2ZpmNw-EVQ-AZRidoqz5QePelh9v5UxqUuzw8ZwiS5nCQCG6C9EkzrTqaJtJDGe1ZTvtV5iA2DTzlu44YteRzTT2u_MR4Iy7cey5K4j4DmF99Db8Ev4JSFzCET5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e980239cb3.mp4?token=LY0DM09-JxmscmmHKyg_l9_esk4EUBCsUwu6nLvDh6IQnrfmzSzLxIV4hOyvCIQ0ySq9STH1kVjmnq0W2Y7eh2ycpIX07abVJr6EMYadamHAYtE-5lnKjxRpzwvAeXiGoQFzqQvN097F3HrnUAEACuXGZPS33CJmqDRtLYmJuUGcqGdZdlFFSdl5Xe9rYCQyP4ewKJx6lzYqWb13OhCViFLN4z2ZpmNw-EVQ-AZRidoqz5QePelh9v5UxqUuzw8ZwiS5nCQCG6C9EkzrTqaJtJDGe1ZTvtV5iA2DTzlu44YteRzTT2u_MR4Iy7cey5K4j4DmF99Db8Ev4JSFzCET5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
صحبت‌های شنیدنی و جالب احمدزاده درباره اسطوره ملوان مرحوم سیروس قایقران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/107607" target="_blank">📅 15:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107606">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgVzbkqrld-4jtezHizBLqTsml2uUINC995P79Dv-rhy4jFJqpJ4JrDxEXGZWuGtIUNy-VoYsCgHJ7x7PbV6cxT0GtrYbzMM4chyqkncfYRUlSEzlbdDH0pxZyQ5tIXi-0J5s46AKcN7UEsZNBUea3SLmyTyumj_GB4y-36R5HJHgMsL6wqqwuaec7l9hhTiPeFDkcCJd8-uBps7nIzUD6o8kmQt08hvmpCF6BOTnhtpJzgOiYjovMaHLoIUEga9k5o8sosF0dslimEqsn7XhcElPr1ylspwNiONuAZBmGLOxeBR6QfPAP2Rdqa9aM8jqNUaRjuf3r9S35jMop8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس دیاز: کادرفنی رئال‌مادرید تصمیم گرفته که کیلیان امباپه مقابل ویارئال به میدان نره تا با آمادگی کامل به استقبال الکلاسیکو بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/107606" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107605">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5204393f.mp4?token=HZSAaozttveWV5qx1OLU-cZklZyVO4jV9Rpzw9VF_GMRWu4U58XgFlcictjvh2IJQlWUXn68-rXuj2G-40fmoFtclF3dFGk1w1zFrnwC8-eWrdxO273U0FriNUgJwW88pQZ-uBa994Jf8UI1dnb1JrvBmg5CICLC5XDCvAJhVfyKM9pjcv2JHYPHkChcaYixjjsUoGxK_5eH4NMLDqv1oWkSVJZQDkkDYqJI9DPE6Qvl2vVSq17-Uxtfp9mN0cDwljzOHORzqm2ORBlvXBs1hxhbD0CQllUZrInpYXaoTCIwUsAUuKCCfFW72M-vZlTovQZg2WQyUjv5U5uqQxG6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5204393f.mp4?token=HZSAaozttveWV5qx1OLU-cZklZyVO4jV9Rpzw9VF_GMRWu4U58XgFlcictjvh2IJQlWUXn68-rXuj2G-40fmoFtclF3dFGk1w1zFrnwC8-eWrdxO273U0FriNUgJwW88pQZ-uBa994Jf8UI1dnb1JrvBmg5CICLC5XDCvAJhVfyKM9pjcv2JHYPHkChcaYixjjsUoGxK_5eH4NMLDqv1oWkSVJZQDkkDYqJI9DPE6Qvl2vVSq17-Uxtfp9mN0cDwljzOHORzqm2ORBlvXBs1hxhbD0CQllUZrInpYXaoTCIwUsAUuKCCfFW72M-vZlTovQZg2WQyUjv5U5uqQxG6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
استقبال خانواده بیژن مرتضوی از بازگشت این نوازنده در ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/107605" target="_blank">📅 15:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107604">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297bb4ba61.mp4?token=VDcPwXzMRw7Sts8eSg8_SHLSpr-26yDL5rEIbObADTwr6hN1sj2IzWaX3-m4m5NhUCSFt61FZzXQT5mKCti5FfPXsRETHoo5WsjvVIH529qL8d9_Bl4EiDoNZ2anecb0DFEXDo7foGgf22dprURx8evFBpjNUamF-bU2tMzluY1QY9IoIDXTh-CTwco7qdb3GsdnMtD1_dSRvPPl4S0Wr-gBUVLFxzze3EXhQMHAgT1_WsMkE7TsZ0I3LuzYdQVPAsnV5sbVYC5P8EtuiJWu3hoTyYxxiceZqqrQTXfNDnVMW8r62AOE0QK5K5VXXbShxlzLEBkPfLVF_dQ3OW5wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297bb4ba61.mp4?token=VDcPwXzMRw7Sts8eSg8_SHLSpr-26yDL5rEIbObADTwr6hN1sj2IzWaX3-m4m5NhUCSFt61FZzXQT5mKCti5FfPXsRETHoo5WsjvVIH529qL8d9_Bl4EiDoNZ2anecb0DFEXDo7foGgf22dprURx8evFBpjNUamF-bU2tMzluY1QY9IoIDXTh-CTwco7qdb3GsdnMtD1_dSRvPPl4S0Wr-gBUVLFxzze3EXhQMHAgT1_WsMkE7TsZ0I3LuzYdQVPAsnV5sbVYC5P8EtuiJWu3hoTyYxxiceZqqrQTXfNDnVMW8r62AOE0QK5K5VXXbShxlzLEBkPfLVF_dQ3OW5wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
✔️
🎙
مهم‌نیست در چه‌تیمی فوتبال بازی میکنی؛ مهم اون انسانیت هست که یاسر‌آسانی به خوبی در ایران به نمایش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/107604" target="_blank">📅 14:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107603">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc7d01e79.mp4?token=EGVvlolCYMCXkgHTFxX055Tvsm6jgXAQetGH5K34ITLGDPM6_83kopFuoVQL9SzaDuxZBH4xYZxCNf22OqhVqdDRL3_k21X89SNwmoNPjXrJ7TrSebDavxn0RN5rFHwobr4VdxIMBWuQx4CdTvHFi-L0iCyV1bFphH7BZYAE0Rf1FjScTwydb0W1ppNFtOklDeOfgL0OzhBfrTbaVo22AFANx06MjQoJ3NRbtzVk_Qsl938ZJSQfy719mMXlkSr1G_gof6QsyJ9-aTR03OyWs0jSPzZuZXvIk-rYi-MaNgMSQZtJbEhM7s_H0hxB3JFopENSYv67nZFYa7gujzsdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc7d01e79.mp4?token=EGVvlolCYMCXkgHTFxX055Tvsm6jgXAQetGH5K34ITLGDPM6_83kopFuoVQL9SzaDuxZBH4xYZxCNf22OqhVqdDRL3_k21X89SNwmoNPjXrJ7TrSebDavxn0RN5rFHwobr4VdxIMBWuQx4CdTvHFi-L0iCyV1bFphH7BZYAE0Rf1FjScTwydb0W1ppNFtOklDeOfgL0OzhBfrTbaVo22AFANx06MjQoJ3NRbtzVk_Qsl938ZJSQfy719mMXlkSr1G_gof6QsyJ9-aTR03OyWs0jSPzZuZXvIk-rYi-MaNgMSQZtJbEhM7s_H0hxB3JFopENSYv67nZFYa7gujzsdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🇵🇹
‼️
ژسوس درباره ماجرای رونالدو گفت: هیچ بازیکنی، حتی کریستیانو رونالدو، نمی‌تواند ایده‌ها و تصمیمات من به‌عنوان سرمربی را تعیین کند. نه او و نه هیچ فرد دیگری.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/107603" target="_blank">📅 14:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107602">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABTUEXkqlLEw75mIqJiMnBicLNCLxe9eV2HEHXMCsM138vOCJwSV6fmVIH2gTs6CMZOS3PjBnbbKKD7mSKngffKKAry_ldTX8OuOage-BBXoJU6wW5JaD2tNYqTl27rN68j84rT1L-bXTdxRM4LbF7GU7qX_z4RveGCaAIxisp41tiCO3p2Un0VHMEodHwHe95u5TGVNjyWM4sf8Yq8zHJiAIFjF2AkGN6yb7id66SApZA2-ahuGyzwzOMMaU0438ahNVobFrjzCblcoUBpUZJyCnoMFXC9Vm-s8pK_hd0lKeA0Zw6Wk_5fSXPKQ3oAMSy_A0Mq-G3a1q9RctQTfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👇
‼️
فکت
:
هر ریال ایران حدود ۰.۰۰۰۰۰۰۳۹ دلار ارزش داره، در حالی که قیمت هر واحد همستر کامبت حدود ۰.۰۰۰۱۷۱۹ دلاره
یعنی ارزش یک همستر کامبت تقریباً ۴۴۰ برابر یک ریاله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107602" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107601">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df216dbd92.mp4?token=cyPWi6L_emuI7ltyEr2Oik1CCeGi97KTS6fOsK5rziiNLHsnYjAw-i1JhBHBHPeHin4ay5QVlclhCr-XfZcR6Y-KnnB691g_KNELvyAkZYJ9tYHorAw83zYyD_4camP89Z8FkERYmosrkTN1Vt_wTXEN4Dh7qTbvRxm7Xb3o5h27m9MWqpM8J1AKr1HYN0MShjbSKjBiP017zzomvkle6e2On1us8_f3ibpayf5NMzIao66rXYR5t4J31DhX3mH40doknrW-I97PWiUnUxyYrpLOL2nxwcPfVdEcH4CJtFNQCAFaqs9saJ53pyUlx-f0eamiqoX1D9kwZN-XMaQ57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df216dbd92.mp4?token=cyPWi6L_emuI7ltyEr2Oik1CCeGi97KTS6fOsK5rziiNLHsnYjAw-i1JhBHBHPeHin4ay5QVlclhCr-XfZcR6Y-KnnB691g_KNELvyAkZYJ9tYHorAw83zYyD_4camP89Z8FkERYmosrkTN1Vt_wTXEN4Dh7qTbvRxm7Xb3o5h27m9MWqpM8J1AKr1HYN0MShjbSKjBiP017zzomvkle6e2On1us8_f3ibpayf5NMzIao66rXYR5t4J31DhX3mH40doknrW-I97PWiUnUxyYrpLOL2nxwcPfVdEcH4CJtFNQCAFaqs9saJ53pyUlx-f0eamiqoX1D9kwZN-XMaQ57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بعد نتایج درخشان قلعه‌نویی بد نیست از این مصاحبه طنز ساکت‌الهامی یه یادی کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107601" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107600">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc_dMgUBt_YEWvAAXwc_X05NeKDIg3AWTOIRvLBAx2hgMa8apt8clPSHUd77ucQ1BZ1JfIFkB-Hw9GnCHrWqtEShulh4EMcMIkCtGFrVaE8ljdssW3WdwDnCaV7iBta9x3pfrTgjK9IojE2qdIVbKTcxlwhil9EvANA_epf4j_CBOyThxzsq_EFiH_y5sUHPSzW3438rpDkKJz1qwfeQcVp5inMHvXJIq-YNn_nDplIKjbh-xT2Gc9RPY6y5sJ2gyQ2ueWqalWg018CywY2thmrNUANvQu1VDkQ1hf9a6N08lYCUQJ21TKF63JyBlYQQs8gkxhfwVboBWj1GxpqYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇵🇹
⚽️
ادو آگیری، نزدیک کریستیانو:
🔻
«ژسوس در جلسه خصوصی بابت توهین (گرم کردن ۳۰ دقیقه‌ای و عدم استفاده) از کریستیانو عذرخواهی و وعده عذرخواهی علنی داد. اما ژسوس در کنفرانس مطبوعاتی دروغ گفت و وعده‌اش را نقض کرد؛ این خیانت باعث خشم شدید کریستیانو شد.»
⚽️
…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107600" target="_blank">📅 13:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107599">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972dc1e1fc.mp4?token=crjFhU-KZljewF9z8irZyB-LCwsHGweBwj4re7utGzjnXHuMAYRsrvziLmFDW3t0ujia1uI3vHpC45t9ypLVjmARTxFGcyM2JAdDSeF25BoJhg0hmnuniVRL6n4eBFQmP6B6TyBezbq-3VnrT4Y6y69Jj4xP9lsvwiHa8y_tRznGiiC-imusLhL0VTLHl14MC6DSaUq-sorJ0J5yEgVy3TYul2aFyFzdT7PLleLPC1QbA6r38Pdl8iKqenm3onWoOH6Ir2n7nOjG8jPQASJWE-wl4l3Do0gj8AQ_88ozcIYrxDI-ya4t3ask_yJJEM16RZksdcmIguZqxY7P1duXMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972dc1e1fc.mp4?token=crjFhU-KZljewF9z8irZyB-LCwsHGweBwj4re7utGzjnXHuMAYRsrvziLmFDW3t0ujia1uI3vHpC45t9ypLVjmARTxFGcyM2JAdDSeF25BoJhg0hmnuniVRL6n4eBFQmP6B6TyBezbq-3VnrT4Y6y69Jj4xP9lsvwiHa8y_tRznGiiC-imusLhL0VTLHl14MC6DSaUq-sorJ0J5yEgVy3TYul2aFyFzdT7PLleLPC1QbA6r38Pdl8iKqenm3onWoOH6Ir2n7nOjG8jPQASJWE-wl4l3Do0gj8AQ_88ozcIYrxDI-ya4t3ask_yJJEM16RZksdcmIguZqxY7P1duXMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عدم پاسخگویی مدیر اجرایی منچسترسیتی به اتهامات وارد شده در پرونده فساد مالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107599" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107598">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1tTE-U0aBnHftSls8MBwMOLh00GySGhWC8tumzdC5GC1W6r0Poij1a2qrSNnd1FHjms6-4gky1ErV8lonTe8mOcchQlMOdY5nXgPGtDcbWvkFbxAml2sSES8wbJRvLQMIIO8DG0BVJww6DOQYpSZxZlRBH437hQdLMMvjy0BB-STKLn1oCPGVmdjIJKhczJzVeDcvZ6yHWBfie8VkUhGu3HdOjmcZ_1mk6eer7P8ikhzxy6IUvR2-l2PkdfrwVM1Qz62AoohS_NgNGfdaD-zcaciY45cDQTb01K8GototYGXUhsXkSHcfHyk38431Xu3TPK_WEinMTzTr8kJH9aLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتایج اخیر قلعه‌نویی با حقوق ۱۵ میلیارد تومانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107598" target="_blank">📅 13:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107597">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb2nGF92raTHFuvqW-GkJfQPf0KFDFjeXNvdoZIpuuV-vloKZ41X4UWpymdfbFY3LSvdzUrlU3dDhBOXBJT6vqC7kEK4gbCE-qzDABSd0vng2VlVdLqIQJcwj5Xo-1UBBWDLi1k4a6eNBrL2n60QrWIL1nInTJzyKU80dbFta9sATCEogIaLT5c8D9cEFkDE_Zz1_zJ2IdfKTp01yprbrvBRcVNbEiO7A8vrr-hJvuVLI2npRTPCXwUiZV9hQtcEDvkncP-53PTKNScQTMUCVw2tzL7CYxNZaBtpYfTKI48zMhOP6GI46bUPfS_h_Niru9_Y4DIn0EHzpcUt_fJKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
#فوری
؛ رافائل لیائو وارث شماره 7 تیم‌ملی پرتغال پس از کریس‌رونالدو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107597" target="_blank">📅 12:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107596">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f7d3031e.mp4?token=ONzfnSM_JeTqjoTNAPhG3VyBhi7egng0Qd1ExlmglRtnTya36-7VKlFU8xujFtxN5oChw0YfGeOO2jCEnO9_XhU_lqyL-9eaW0SJDx2KnL_YBLwzhv3-xn6QaEJwLCYg8mP-aq2fM1-AA-0JS1ixnE8K2KmZTaIlTj5VgVZSnyW9EXYFlmD5N_HB8sqEODUlGxJk3xAl2upmtCcKyVfg0YYbc-eK17f0snbXAj3BxahHMcwnx-_KG4fa36e6rXQVKpfPI-tpf3qNCMDUyCHpODZoPJKiAB-jIiTxAWCP2nfvyZtZvd-Z2iI5afmv68duuMbc5qzVEEz65gZZOse10Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f7d3031e.mp4?token=ONzfnSM_JeTqjoTNAPhG3VyBhi7egng0Qd1ExlmglRtnTya36-7VKlFU8xujFtxN5oChw0YfGeOO2jCEnO9_XhU_lqyL-9eaW0SJDx2KnL_YBLwzhv3-xn6QaEJwLCYg8mP-aq2fM1-AA-0JS1ixnE8K2KmZTaIlTj5VgVZSnyW9EXYFlmD5N_HB8sqEODUlGxJk3xAl2upmtCcKyVfg0YYbc-eK17f0snbXAj3BxahHMcwnx-_KG4fa36e6rXQVKpfPI-tpf3qNCMDUyCHpODZoPJKiAB-jIiTxAWCP2nfvyZtZvd-Z2iI5afmv68duuMbc5qzVEEz65gZZOse10Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند حسن روشن پیشکسوت استقلال به امیر قلعه‌نویی: رئیس مافیا سرمربی تیم ملی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107596" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107595">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107595" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107594">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afj4uNrnt27vH3h4O4kpP0kB5o66glWlvPlExOIj3MeZqHFQAFNFktWmRpf75hHNg6XLg2-6aiI4VFTuBywnlGqqQgJArUHf--sl8RaRNOJ_NC0nXAVbzShoxEE4Q2lZeyKphzutdqPZSYAEhc9k8sN17V_TP09wF7KUTkh0jHQUBId9yqm_a8tZyL0RpNU8BpJIHVpKb97PiBuowguFyxFLIfjQIpigv8jArHHkyF5ncUtBc2ztTQylKNqMWdiMFjAH1s54phfVZe_CrPnV0aglKCy2wg4dXmF7lb5vI_0ygSV1fqUrtT5UdJ7lIlgXvkOcoYB65DOtFxQFlOUIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107594" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luSzNAZzpw5yRrEjOqyR-cWMsfV_srgRzIxh8CCTU_4u087o0x7G4PiOWjyqaW4Hn8x1VAiG7FSJ60Yq4TksZzSiT-04mwoDZVCIHqiOPQzyr7fUhnj0okcY7xPXWxawuJV5_W6UTObxRRhzBbqOuzlO6mbRLIQFUpEogmtnfd1bbSOL2PyiJAw0nEU_saCjef_lOuw8BVpvFA6x3y7_SePx6EY_va4v8PZC0UjJeVgvHAW6RhTgFnuYdFM6T5yCf0XViMK72YFNcdRdKyOiBfMkqXjtzXfGW8DTgL0ZSkSrycckggxo5khFMK8ukvwkxsncFf6RHLUPmLpiRsrIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
چندین واسطه به علی‌تاجرنیا پیشنهاد داده‌اند که استقلال در نیم‌فصل با دنیس‌درگاهی قرارداد امضا کند که تا این لحظه مورد موافقت سهراب بختیاری‌زاده قرار نگرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107592" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d48b3887.mp4?token=DTR-Cp8YWQhznB0lWLm1OC5HwdVxLDhcVTgtyYgg9A0vAZHekGF-jVvKCpstEPteaw_2gYmpjvb3QA6jYibrL3RvVKt8Mth89L5piatHIBeigYsl9eIeiZzW0NmzmWTYpIP2F8WtiWJwoX4AUQqPO8gmZMfTuMc2RVs1N8BRLs7JCxiEBQYaax3zVe3JCh6f7vYHzd-KNeTVa89vJBlprdDIURJ-1dMnjbLO1hJPPOaqC_qiZptIRo_yY9v0pEAVcdnFYNLGdFbBFqow9-ajjvMyppfNMXRgbkwIPKOSLT7363bOz_rJoFFaODpBkxsLkGWiweOG-KJAvSpGJNO-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d48b3887.mp4?token=DTR-Cp8YWQhznB0lWLm1OC5HwdVxLDhcVTgtyYgg9A0vAZHekGF-jVvKCpstEPteaw_2gYmpjvb3QA6jYibrL3RvVKt8Mth89L5piatHIBeigYsl9eIeiZzW0NmzmWTYpIP2F8WtiWJwoX4AUQqPO8gmZMfTuMc2RVs1N8BRLs7JCxiEBQYaax3zVe3JCh6f7vYHzd-KNeTVa89vJBlprdDIURJ-1dMnjbLO1hJPPOaqC_qiZptIRo_yY9v0pEAVcdnFYNLGdFbBFqow9-ajjvMyppfNMXRgbkwIPKOSLT7363bOz_rJoFFaODpBkxsLkGWiweOG-KJAvSpGJNO-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
همچنان رقابت نفس‌گیر برای توپ‌طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107591" target="_blank">📅 12:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
❌
⚪️
#فوری
؛ بدلیل تحریم‌های خطوط هوایی ایران، سومین بازی تدارکاتی تیم‌ملی قلعه‌نویی مقابل گینه‌بیسائو در هفته‌آینده لغو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107590" target="_blank">📅 11:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0FOz7CQ9Nr_2NN-2TZN6dJpnlDQxtWw641zMbkKJbxAkobN-LQev62Z6m2pvhSKdpnJlKqKvynS5mWocW737j_c58VXg8zvTlZds1PccLRh0AnO4HBsphp4BK5I4s_w7dYaS8IOoc6drN7lKt2dI1CKS5NKRpdRMRgHm237HSvVZn4FXfF_QY3iWFWEnVp6MGbu5335cjJU9mQzWSa0Alu2jXS9QtaMWA_Ycp8SfT7euMfO6IPJF1jkOn8DKGeJqiIfaz2cGzRXY4nSMBqzzB3Nbb-6a2brZqHfAA8nr9J4FUX3SBpzpmEd8T22U4aERSYjJe_PdB3Zx-zUz2ycBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
میگل‌سانز خبرنگار اسپورت: خورخه مندز ایجنت ژائو فلیکس به بارسلونا اطلاع داده که این بازیکن در پایان‌فصل قراردادش با النصر به پایان می‌رسد و قصد دارد به صورت رایگان به بارسلونا بازگردد. تصمیم نهایی درباره این بازیکن با هانسی‌فلیک است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107589" target="_blank">📅 11:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0340a7da43.mp4?token=XaQJdpMnFtW1QzrQAYGpuXSGME_Bz0PjbuH7aGo5WsTqVJX5jiy7otWlu5YtmaLocNeSQ3gjAj6gWpmZBYp8UpYGxbx3S3umr_ktaVV-dzw-YgBbyqx-NvA45C34DRbQwUpzW6Rr0d-VKduLfB3saGD4LHAVK4fdjkvuLnoMWMDoKNyFM1ny0uer-lDw5Mms8z9L3AYGeq2zHg41WUNEI8GcB3H0hMl4kHgD-NU0qyUtoaJE3nusTbKSWFOBYsHNmnAF4glL5xzujGgug5OTtm8Nqk7Pnoy9wdfvI71H7EYIvKk_pJgLGM7JWsXU3z7Seas3jZ0Dtsc99wg0Xbi0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0340a7da43.mp4?token=XaQJdpMnFtW1QzrQAYGpuXSGME_Bz0PjbuH7aGo5WsTqVJX5jiy7otWlu5YtmaLocNeSQ3gjAj6gWpmZBYp8UpYGxbx3S3umr_ktaVV-dzw-YgBbyqx-NvA45C34DRbQwUpzW6Rr0d-VKduLfB3saGD4LHAVK4fdjkvuLnoMWMDoKNyFM1ny0uer-lDw5Mms8z9L3AYGeq2zHg41WUNEI8GcB3H0hMl4kHgD-NU0qyUtoaJE3nusTbKSWFOBYsHNmnAF4glL5xzujGgug5OTtm8Nqk7Pnoy9wdfvI71H7EYIvKk_pJgLGM7JWsXU3z7Seas3jZ0Dtsc99wg0Xbi0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇵🇹
⚽️
ادو آگیری، نزدیک کریستیانو:
🔻
«ژسوس در جلسه خصوصی بابت توهین (گرم کردن ۳۰ دقیقه‌ای و عدم استفاده) از کریستیانو عذرخواهی و وعده عذرخواهی علنی داد. اما ژسوس در کنفرانس مطبوعاتی دروغ گفت و وعده‌اش را نقض کرد؛ این خیانت باعث خشم شدید کریستیانو شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107588" target="_blank">📅 11:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107587">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7be9b354c.mp4?token=fsktxxa4fpvLO8D4-hWFwyBiX-Kw9LC_qz78Cu_8bQv3V7QlIhNfi990xeysLbzUQulLs4XjJq5WawXV402A1-iEF9RC6GgY_gQozgwWvwgyBMvyyxBIh9Wp4zRBpKDDqCl5n1zuMK-zQNnWds-iOYQAwrr5aZeA3JcXdwWBtpcpGLufxl47k4_FF58xYeihMx656DuON8PvHwmvagXM96PwP39B7pXNhvAIntCh-tFAFI2YdxaNh1qQtgQ8w5UAco_UCe3Xtaa3ZgU1MAaUXZn7pI3CS6bmY-1Rv8A1NrVTRfW-AeMX0ovV28ce-YpZNC5oBqlPmoBBM6XdpakUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7be9b354c.mp4?token=fsktxxa4fpvLO8D4-hWFwyBiX-Kw9LC_qz78Cu_8bQv3V7QlIhNfi990xeysLbzUQulLs4XjJq5WawXV402A1-iEF9RC6GgY_gQozgwWvwgyBMvyyxBIh9Wp4zRBpKDDqCl5n1zuMK-zQNnWds-iOYQAwrr5aZeA3JcXdwWBtpcpGLufxl47k4_FF58xYeihMx656DuON8PvHwmvagXM96PwP39B7pXNhvAIntCh-tFAFI2YdxaNh1qQtgQ8w5UAco_UCe3Xtaa3ZgU1MAaUXZn7pI3CS6bmY-1Rv8A1NrVTRfW-AeMX0ovV28ce-YpZNC5oBqlPmoBBM6XdpakUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سقوط امیر قلعه‌نویی با انتخابات و انتصابات شائبه‌دار و پر حرف و حدیث!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107587" target="_blank">📅 11:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107586">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▶️
🇮🇷
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت هادی‌نوروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107586" target="_blank">📅 11:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjo2BPkFg7WaU_gclDnRwRVAivd-N_cgTRHYe7nDttCGITDYuvW4hAbdK7yd_3ZHDDUcPupy6mw7rNS3FGZkKQ4p1IGq-pnKCAdYj4wmUH7rNHMXbW2ibVlzBFA5edXSSMIt7ZaCLTQkCr6FNMX9rUMErOxecxZI5-nd0x4KAJVMO8grjfR7shtWZy-5d1uJteaFNLu7EKS9FvD2Z0Rw1SFce_axduD7G8-WtowLYMJyYHj_VfwwxhKn9C0hVvTiLKf0rgIWVJgQXJ1UF-O31tgvRImqJwTtxOcJTMimBRmkgRJ3UC-GKSOjuuKtBZ2SSYTbtP5B6Ze88AtG8x5vIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مهاجمان بارسلونا در این فصل تا به امروز:
لامین یامال: 11 گل، 7 پاس گل
رافینیا: 15 گل، 4 پاس گل
آنتونی گوردون: 2 گل، 4 پاس گل
کریم آدیمی: 3 گل، 3 پاس گل
گابریل ژسوس: 2 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107585" target="_blank">📅 11:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d3c9c064.mp4?token=EcMsEEBOC-qSy8ZcfSD-oRX7qI19DkNoVxrMCESEglC6iplNn6fnuwVhMG4QGfXmtQmUa6rZDO16wYt9yPQyWhPucIT0Am-X9whZGOwYcNnMOjk5vaTRVcb4CJJBvzVqG1PaN0EK3TSVU-wyl5JuaBiZAIZ6DBk94PJzHnv6hq1Uybcw1ho8RUqPXha3KIgfb7zs0sQfu9WzN27ved92ljF3btjDR74EMbWALOfQpQLGr4MyJ7uIFoqYarTSmx59DF4osGt-mVK-sdYu28K0LOWXpw2hkCtHw6LWlFsSHT7qgu345BiFgkn5wGdnYUUjo6rE3T2ygtE8TH2HI65bXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d3c9c064.mp4?token=EcMsEEBOC-qSy8ZcfSD-oRX7qI19DkNoVxrMCESEglC6iplNn6fnuwVhMG4QGfXmtQmUa6rZDO16wYt9yPQyWhPucIT0Am-X9whZGOwYcNnMOjk5vaTRVcb4CJJBvzVqG1PaN0EK3TSVU-wyl5JuaBiZAIZ6DBk94PJzHnv6hq1Uybcw1ho8RUqPXha3KIgfb7zs0sQfu9WzN27ved92ljF3btjDR74EMbWALOfQpQLGr4MyJ7uIFoqYarTSmx59DF4osGt-mVK-sdYu28K0LOWXpw2hkCtHw6LWlFsSHT7qgu345BiFgkn5wGdnYUUjo6rE3T2ygtE8TH2HI65bXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حسن‌روشن: یه روزی چند ماه پیش بیرانوند بهم زنگ زد گفت اجازه میدی برم استقلال و بهش گفتم اگه اینکارو بکنی میام جرت میدم. واقعا سر در باشگاه رو باید گِل گرفت اگه دنبال جذب چنین بازیکنی باشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107584" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800d85114f.mp4?token=VyU7IHXRme2hZen3QCJpH4BtY9AcyX8EbQCjheUtqj4YeEJZQiKVC69Uk47mb2qpB_dL8-eVUYlON5-ZGJ2ke4wHrL5wm8BlIHdpN5ADJ9isYeEkn6uOx4_iv9qcTQ3BfKgB2rEg8k3ozQm4_bFGgCMGIh9FEPY1kY7UfcSG6BcCYfX-lV7YKtB2Zvq7VgF1oH7246hvZkw4NQNoSNFUkIc8JbedHrwMy4vKI-fBs6KyRl0S68rmNuuoA4z8HQufvYyRR5N7XmouzhTy-Azk1MO-YHb4pizq2PR4ZTtkRxLd-d21lsW2XtzHnXwzTM5-15fojPCtrxNEai9XO_6osA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800d85114f.mp4?token=VyU7IHXRme2hZen3QCJpH4BtY9AcyX8EbQCjheUtqj4YeEJZQiKVC69Uk47mb2qpB_dL8-eVUYlON5-ZGJ2ke4wHrL5wm8BlIHdpN5ADJ9isYeEkn6uOx4_iv9qcTQ3BfKgB2rEg8k3ozQm4_bFGgCMGIh9FEPY1kY7UfcSG6BcCYfX-lV7YKtB2Zvq7VgF1oH7246hvZkw4NQNoSNFUkIc8JbedHrwMy4vKI-fBs6KyRl0S68rmNuuoA4z8HQufvYyRR5N7XmouzhTy-Azk1MO-YHb4pizq2PR4ZTtkRxLd-d21lsW2XtzHnXwzTM5-15fojPCtrxNEai9XO_6osA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های رسول‌مجیدی پیرامون وضعیت تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107583" target="_blank">📅 10:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107582">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09df2fee06.mp4?token=ZN79Z_ct4wqNtuUyCOB2TqTFNTzGcb1rigpLxeEHsGvbVgDdzDDz8yfBT_pcsa1OAQeJH_UV-Xx7J2cmqSwQmz-TDsQp_IqMb1eFczJtNy1-C5kkcTBGAMAXAcpPrgoNUCdtpo0FohLJtqa-6FY-QQlrHFTMX-L5A5I4PZy4SlOUZuepWnICJxfmuOCLV0LGX7ZSWJeuWml86oAJfP8et8nRp71rXyvMEMRqMdQwFI6dBHEQd2ZdIhCZ2a50_ePQEVxeveXA27Ubob4PD6CNYL4Dy8KqSNAamKUp3lLZmiW3fz5clzCoUIknSOxW648QhuKtcRWopAgUxgJZTwxJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09df2fee06.mp4?token=ZN79Z_ct4wqNtuUyCOB2TqTFNTzGcb1rigpLxeEHsGvbVgDdzDDz8yfBT_pcsa1OAQeJH_UV-Xx7J2cmqSwQmz-TDsQp_IqMb1eFczJtNy1-C5kkcTBGAMAXAcpPrgoNUCdtpo0FohLJtqa-6FY-QQlrHFTMX-L5A5I4PZy4SlOUZuepWnICJxfmuOCLV0LGX7ZSWJeuWml86oAJfP8et8nRp71rXyvMEMRqMdQwFI6dBHEQd2ZdIhCZ2a50_ePQEVxeveXA27Ubob4PD6CNYL4Dy8KqSNAamKUp3lLZmiW3fz5clzCoUIknSOxW648QhuKtcRWopAgUxgJZTwxJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
⚪️
از مفت بری تا رو مخی ترین فیفا دی
وقتی منتقدان تیم ملی در جام جهانی انتقاد کردند، جوابشان شد «مفت‌بر» و «جا خالی»؛ اما امروز یک شکست در بازی تدارکاتی، می‌شود «رومخی‌ترین فیفادی» و دلیل برای زیر سؤال بردن بازی‌های ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107582" target="_blank">📅 09:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107581">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ebca248f.mp4?token=fT2181Fb8sWG9xcK8QJ0THpLmADvEZxFQ1B8ztLz9WLsg9BW4Ez0G8UA_4VLQsY8Z0_4i1dEXnIt9z5y5Es-iLn02XcX0Veb6zVxKWzLozT29xSdKeDpXBg6sBXm-K4zilyXHkK6KmV8OC8543F6fCWQJgq_mOVeQcbzWSMmYqAYKc79cJle4g9fH4p_l_DYdstwvdiWMjPn-HJWQfhGgVdICZvUP1pWdaYJwq3YX5rWmFTVqWU_KWJjrddflb8r_uDZ1Vm9_sCunCgDeQH5Q-eVXPTM7sxJpdBQybbzKy6kmUE0oWCqq8s7uASW5GTxVWwlNGvqX8nhaBtT_VFZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ebca248f.mp4?token=fT2181Fb8sWG9xcK8QJ0THpLmADvEZxFQ1B8ztLz9WLsg9BW4Ez0G8UA_4VLQsY8Z0_4i1dEXnIt9z5y5Es-iLn02XcX0Veb6zVxKWzLozT29xSdKeDpXBg6sBXm-K4zilyXHkK6KmV8OC8543F6fCWQJgq_mOVeQcbzWSMmYqAYKc79cJle4g9fH4p_l_DYdstwvdiWMjPn-HJWQfhGgVdICZvUP1pWdaYJwq3YX5rWmFTVqWU_KWJjrddflb8r_uDZ1Vm9_sCunCgDeQH5Q-eVXPTM7sxJpdBQybbzKy6kmUE0oWCqq8s7uASW5GTxVWwlNGvqX8nhaBtT_VFZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
صحبت‌های کنایه‌های مجری صداوسیما به سعید الهویی دستیار پرادعا و بی‌خاصیت قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107581" target="_blank">📅 09:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/serpwMoi-2sormLmSeaGQvhLLzRVVDvKd_EveryJMOG_pVv-yXfVGdjspEnCquSWTfwib9XVjLG2HxXtolEilBK-aF1pmJbnJSpUp9nOpFZKwlt3hkK6NAFHOLgEpdpk7ncp4dKCheZRPpjMdMag3sh_54Y9I08OrTCbnkuhU5oLpcUe4ZW6sYzjy7DdFuLDt5J145XV5NYmKGnaSyWQocZwfQ9hrvl21KxbjqcVS-ai74mAFn3JmGyFFgQu-JvL59Ab1OCd3FVXhAtJWCFWuF-QPmyvOOD1clw4dBrVJBGDYTWodtzHYbH3JbN0psUuLfNxsOYlAgEmkc-UCjJBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
⚽️
فدراسیون فوتبال پرتغال بدلیل بی‌انضباطی در ترک اردو از سمت رونالدو میخواد این بازیکن رو جریمه مالی کنه و اگر رونالدو از میادین خداحافظی نکنه، ۶ ماه حق حضور در تیم‌ملی رو نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107580" target="_blank">📅 09:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMDaQq5X2cbW5tnPKDAZF0mxKYIHJPp1Dvzet60lLU2J7T2TPkG65pZFZweJfsoUrbnM4crfCJDcl65mzfZnovWwiv3F-pLuR1YoRvODtKXXslw2ra2Evb3J1A93xcWef_rg2UFog3lfrUjHgm7PzGZ0iU0V4x0wuuPXxT10ZB61Ny9cOBqs_JbWgS2g8L0hbOHwffBhCKYoSv0_3ARvXTqX_t3ZS5sqn2txKZsKPSRtSEmvN2VepnQ2T5tKbuQiKbcy_5--y3-PFNpLkoKNmniUns_DFCt0QKCViBgsndkV0ch3jh3le2KnUI-ImZek1UXzmlnOPWig9R_njMGq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🎙
تیبو کورتوا گلر رئال‌مادرید: بنظرم جایزه توپ طلا باید به بهترین بازیکن فعلی جهان یعنی کیلیان امباپه واگذار بشه نه کسی که صرفا جام‌های بیشتر برده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107579" target="_blank">📅 08:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107578" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/107577" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107576" target="_blank">📅 01:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8n-sEx5oYHQWLjVnfV7HlMbqGZeYRu5varFC8N4GsvpRfac6-KjTYzKL15Krd3SnbnlhodF8mmZ37FkXFx7bEu5b0H79pXCqcZcjv4KKVYAIUrIHgjRSIWB3z7nRmJCxZO7rywzYkD331QtCiUTZLK4XcneE-KjXWFB3EMYQShKCn9AS3X7oufB0bmqUQJZk4xmcBEGD6FUMwHyoxF6-xJu43BUTPOre-FrDs6Hs5G5_ON8YHL0cN1FWmZqZH-rF9JZcrViRV047lrh0vUAf0-yXUBdm9j5id41W_xCWCevonNZYn78ccfyc9rj0OXsBFS8ZJDpiihSv1gXKWiLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بولیوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107575" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107574">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7236f39a.mp4?token=QqrpJwYzq9zS6j-mHTZUHaGanzyHur8blqDwoVrhEJrMiSPg7oRHdhmfE8pm9OMUrGw2WO1obZeXszdGiejx4eAvOiQhsDqjeC6ySuyKtQvuKXe7nZA9QUcABE4OtmFAosqE4zxZtziBY6sVh7oc_uOapWtML60yYMaTFIgGo3GxTmwnijH69CgFZfCuIZtyCMGQkfubTlW31NCEfR0W30bvKvEc6fKOcJWLuNYPhXvJrb9Rw5xx8gprlJgu2iOrxbeQd0T4MUj12M4mI30E3SnEcqGwsnINkqUJzcJwEdw_iBQmMjpE7wLx29PJkxAIOJB4W1EkcATXu5mFyZib5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7236f39a.mp4?token=QqrpJwYzq9zS6j-mHTZUHaGanzyHur8blqDwoVrhEJrMiSPg7oRHdhmfE8pm9OMUrGw2WO1obZeXszdGiejx4eAvOiQhsDqjeC6ySuyKtQvuKXe7nZA9QUcABE4OtmFAosqE4zxZtziBY6sVh7oc_uOapWtML60yYMaTFIgGo3GxTmwnijH69CgFZfCuIZtyCMGQkfubTlW31NCEfR0W30bvKvEc6fKOcJWLuNYPhXvJrb9Rw5xx8gprlJgu2iOrxbeQd0T4MUj12M4mI30E3SnEcqGwsnINkqUJzcJwEdw_iBQmMjpE7wLx29PJkxAIOJB4W1EkcATXu5mFyZib5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇮🇷
محمد خلیفه گلر فعلی آلومینیوم: قراردادم با استقلال امضا شده و نیم فصل به این تیم می‌روم. خودم هم دوست دارم در استقلال بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107574" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107573">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45c62d9ed.mp4?token=CS1T3gVjSEIm3g4s0rnlRcgi3NThmEAs25gHHDtFTRfBUguCw5UIVxCUNIQ4Vcjc5iEPfld73KTp4xh0uHLSqYzx1byp0kFfKxR_bxXW_mFSuD98310W9jpEery5bYI1WGHZdIFGpee4pqlEB274Z_5n8qs98DsAhrzRly45fmoffAg4tLxI0EARfi_LTNMi0Us1Lpw7X8skZfoMGa_ijT_WzF50xswtg0n9HL4lJWM4xRc8RflITbpRxzivsZZkzpizw-23eREnVR9vWHR3LSCZ29EwuWVoJcQeyP2ySTLVc7TWrB1gZGHTiT8L4FIyn6-fde457Y3vncZuOGLJwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45c62d9ed.mp4?token=CS1T3gVjSEIm3g4s0rnlRcgi3NThmEAs25gHHDtFTRfBUguCw5UIVxCUNIQ4Vcjc5iEPfld73KTp4xh0uHLSqYzx1byp0kFfKxR_bxXW_mFSuD98310W9jpEery5bYI1WGHZdIFGpee4pqlEB274Z_5n8qs98DsAhrzRly45fmoffAg4tLxI0EARfi_LTNMi0Us1Lpw7X8skZfoMGa_ijT_WzF50xswtg0n9HL4lJWM4xRc8RflITbpRxzivsZZkzpizw-23eREnVR9vWHR3LSCZ29EwuWVoJcQeyP2ySTLVc7TWrB1gZGHTiT8L4FIyn6-fde457Y3vncZuOGLJwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکت‌جالب بیژن‌مرتضوی در بدو‌ ورود به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107573" target="_blank">📅 00:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107572">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCiKYC66vYSE_rq_ucRqUZAyE4XWC73gRD4h8Z_n-CCXO7JFU-09GyvJc29-oypQsJVpKrcUq02LBwIPl-fiVuE6y8FlcQpOVSyimyfY9eaMZ8kJe8LB0I-6eOSkBTYrgno5w1j0DM4-E8aluRShcBtpRZ6nOi9QaEdz8IZLFBcX5PGwPdiRyz6FCY_-sX7VmsSdvYQHgaHTGW7kVqIay4no7PAVUQGxsr2dYAXoAmOsi3zHST2gGIcJ0BTQ3Pg7tlloqmjTHVTVnG6CcxxrXS0Rr1otrNjXnHygQwFKbaxwxqmkqOyCgKCbDARKI7A-pRZwdQaa61H4N6gUr11PYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
👤
رامین‌رضاییان از ناحیه عضله زیر شکم دچار مصدومیت شده و احتمالا برای مدتی از میادین دور خواهد بود.‌ وضعیت نهایی این بازیکن تا فردا مشخص می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107572" target="_blank">📅 00:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=vdnb7zDUOaykO9CNqWHaEBO0182TfhmCZFV9lT9LmvhI3Kt8Wa4XpXEQhR_wOhgD47mIhaopIoCfs2fW8ZNoF95CuCSddpDxxRb8w4m5poiEtuFpQVs17BqFYExxhfgKi0w5-STMXuHt8TwmuoI2BIq5gk4knJquF2i7aSUkjQUcBw6cYOGOzwUblL7gL_zZba5MF7nv6ahFUSAbuDSqz13KqZcYnUw88d7PcNuLerAuwBobU-gDypSqTBsxB15R_ZCG9HVVPpOkl-WjrgUGtoBdSZ8Z4d8LtdkwzwWVANXWiDrpgrguWAFOJmWmBe5tIqBInpx3byPRQT2QNK5zxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db10a352e4.mp4?token=vdnb7zDUOaykO9CNqWHaEBO0182TfhmCZFV9lT9LmvhI3Kt8Wa4XpXEQhR_wOhgD47mIhaopIoCfs2fW8ZNoF95CuCSddpDxxRb8w4m5poiEtuFpQVs17BqFYExxhfgKi0w5-STMXuHt8TwmuoI2BIq5gk4knJquF2i7aSUkjQUcBw6cYOGOzwUblL7gL_zZba5MF7nv6ahFUSAbuDSqz13KqZcYnUw88d7PcNuLerAuwBobU-gDypSqTBsxB15R_ZCG9HVVPpOkl-WjrgUGtoBdSZ8Z4d8LtdkwzwWVANXWiDrpgrguWAFOJmWmBe5tIqBInpx3byPRQT2QNK5zxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آهنگ جدید محمدرضا گلزار منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107571" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHeulcjPtDvXfEkAISwF9-TOrDJQ5-ItbdGGcQQN0eazTl-MDInesADvMsT8HVPlP_dLYFQ9RKwavJL7o6bZMRacCzyuYye8knc8Z4Jtq5NcRbET0dTzglkZlyxaHAJnvuOeqyArRcFiP81PKV9crvmMNebvWoWcciIGK8HJ33D12Dnf5mTHz02ioxFBeuP-RnwTeh8QYBo-A6__dHBRf0hBL75OJTCfB-7_DE46p6tFa89XvKw3Zu56mDi8AelhWcEEcAC3nFSu3JlEbFlkcOB5Xaxu251DjNBgtwMKPg0ea0FPvr-OYclN3raNLLaV7HBT7i7JKw7fl-DjeY9bzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107570" target="_blank">📅 23:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9vLS1tOnAhmrTGifNUHJ4CIKsq_TFi7FToqPGBLTOZuzE9NcOV9DMpvdoxzS7SFHq5fmb7QKD-KmVR6LjHJrJ9z6lEcRt_5QJclhSK1ADksnFhHkCYqgvgWQOu0aXC5Vb8KhvaAQlD3EeUZ85fFhYixIv0O9SHhDLeVIrUORWK7v-4JMDpjjgTkV41tN2hpaexpwexIxrYQGPBZlLOwvg6VIKm4vwXbv2KWmxEr2DP5DiUD_jh7z4ehBVEb6I038Vcgef4i9Pxe6JMscl6SzOJD8qFz50MGqwEpKI0ole7WOwmo0c9LniCY6eaSS_kj9tK2jtB0XmldhuFCMGa22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: اشتباهات اخیر خود را میپذیرم اما از مردم میخواهم فرصت بدهند و مطمئن باشید که تیم‌ملی را دوباره پرقدرت خواهم ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107569" target="_blank">📅 23:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBOQMgSrI1F1XN3CB0imc2ZLju_tt2gJFLvYbXgwkrTnhR7y5H3EDUOOTpYn5GzJm_3dh2JNB4ZlphqIU3VuHr-d0HYfTZOrUsFq6xeZ_v8ac91hPjygDyTkJ-1DMZngSXvjO1dIms2OLsyOn4BcgA8GSBB9-eMcJSv969hFoSzMtyKY-jOKRzbsWtAGfgblu2eUDXKPIPcYa_7SYNAff5H2vZAIta375kMFlqcvsRV1XKOMTvcdCLGO74vKOrgiDxTiByvX634Yi5RQYkht6Uu24cSm72OOOMRnUG1yxhYaIi7FqCBf5WCnFGGveNjOKv98TISECbgYKL8AvA4-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
#فوری از آبولا پرتغال: تا زمان حضور ژسوس روی نیمکت، بازگشت رونالدو به تیم‌ملی غیرممکنه و باید بزودی شاهد مراسم خداحافظی برای این اسطوره باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107568" target="_blank">📅 22:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107567">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4O2xbNmT_crXw7kj2t4D788v-a9vT68ItOpBs7goQQAx957OqlyOI9uTGwh_Ubbtn1keSuG6T3ATo6YQjbTYEhwRP7NyR2Ny3BlhTZlQpOOgfMFBmVl_36EI0YJFpxqZsvbWA4A0LdPmNJvBOrYpJbmKsgz77kklT0IxzNRt7rBcgJGPehJ3FTtX9Le10LdM872HZeFRaiGjwwEGeMuWNmwEIIkmyE5uxhSJtgpRSZz-02ghDtWDP3PozzNd_Kqwch7eRIT037h2dfVj_chx62PgT60C8CMaOt9GilTBJU2UoJ29conzpojqJ19K9psORssFECaaXFZmDaNJnXC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:  بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.  در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107567" target="_blank">📅 22:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuadZvIyLhanzlTjLsDQITvasQZbpdNHssRyYwzhocXlIveW9qOqajLMRtMK2qzJ2JOn9sWDk_SJBqAnA_iHl9yxDN1N36DJnTHEjFDYfbOhpf4FRU4V3MWX0ZZ5FRNOfcwYhBSWzeXHEQy5IjtFgAST4iJoQUzKP3kFOPuGJLuPxfC47ZoNRUGvZeR7wPNSHvcxiapgzJ4mLVNe9VsPudEj5173_0rwMQ8GCSeEITSRc6iIpw5x91Yzah0T96FHyusxpTqK2udbRqBWx1xahjX0RZpqCQKNJT1lBAhbxU11nAmTCEYFl6AmfIZ1uqy0BzQ5JJnaGdytGnfyWsMPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💣
رونالدو اعلام کرد که کمپ تیم ملی پرتغال رو ترک کرده:
بعد از کنفرانس مطبوعاتی سرمربی تیم ملی و متعاقب گفتگو با رئیس فدراسیون فوتبال پرتغال، تصمیم گرفتم کمپ تمرینی تیم ملی رو ترک کنم.
در زمان مقتضی، حقیقت رو درباره دلایلی که منجر به جدایی من از تیم ملی شد، تیمی که همیشه خودم رو وقف اون کرده بودم به همه مردم پرتغال خواهم گفت.
اکنون زمان اینه که برای پرتغال و تمام هم‌تیمی‌هام آرزوی موفقیت کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107566" target="_blank">📅 22:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpu7PZZA-vxxB0Z63gf8AkTtEqtE3BbvlYJltWg0Ei6vWpxnF9M9QISzM5MBt_aV9xh4IcJuNVhTb8AtlndhGrJd7FPcpAExvFdD0mCBcn0mxW3w4shSgGDNUlNOX_rB2t9TQeZ2rdyiX8H_xjeTnNmfB7mef3ueQlzklXdz6T2IM6rQeFQ7Cfom80-uHi9xZ7eOnRH0hZdl1QLRbBOqyDRHFPq166b02-Z2PukJNjDhfJ3gpd0em2kKRiWENzh5W86Q_kIuWaJ6KTfWOUhxcD8wwey4aXE-O2QAUO1ITewPnrUoSUZvBGqgzqHka_Kmbo1ONdLkdpy01i998uP4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
فرانس فوتبال اعلام کرد که عملکرد ابتدای این فصل در ارزیابی توپ طلا  محاسبه نخواهد شد:
🔸
دوره ارزیابی رسمی از 3 آگوست 2025 تا 19 جولای 2026 است.
🔻
هرگونه عملکردی پس از 19 جولای 2026 خارج از دوره رای‌گیری خواهد بود و برای ۲۰۲۷ اثر گذار است
👀
به عبارتی درخشش‌های ابتدای فصل یامال و هری‌کین و ... تاثیری در نتایج امسال نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107565" target="_blank">📅 21:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrTzrz_oqrgz97gIFsjOyiyBQQ6b9rg9dHbcYC-UMkqxhEPBKfsiU03jv3rPfFyAgo2vNZL7vzbd0zAn46wX1XU_m76hnGVyMwvVIUlrd3v84HE505cSOKwroAzLhIwG0PqnFJH62gP35YH9tDiygmUO9PzSp57MEdrHThpWSGKLAdhjfb_1B0cI6i5xQNNqHipQjRPg81BBisN3Awrwt_cMTlMyUzCD9ulrTI675VA9u1EhxGcQCp0mscQ6XpjmD9mRH9vJkOHOe3b8kZUX9Nw32TnfQ8-bHRLLpCpf_8s949xyRHR860zEL2e4-Yex-xEoWxoq3z28bG7VttJWyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107564" target="_blank">📅 21:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=ui0Ex1ILM4A4AmlcB1pgNbEwMzXRx98PfjiEaZUQV0cHAqVrvlGhfO_Yevf8Mu4T6kUEyymJasQGuo8EE4Wo3G2Adk969QzkuN82Q1IR9rOWnCPR7kCuhuKB914F6iLUpnuqknKebSqtivQ6lgK4cwUw-ecAnWrdeBuGgf8DBcY-sqSDDX1E_SF2xnnnPYUP_eH-Vo0m_WfuxucJWWCkGPsITfl77EkJ33gWK9dPYlgnalLu6WGa5r3Zz45wOLyJvbMYt8trFmBCbIUAlVEgRR-Bn5jW0CObjpl13ut6Q6hY4RgzJY_EW0NYDU6XVa9rtG7r218-sr6nE8J7xs4Ksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81558f0c75.mp4?token=ui0Ex1ILM4A4AmlcB1pgNbEwMzXRx98PfjiEaZUQV0cHAqVrvlGhfO_Yevf8Mu4T6kUEyymJasQGuo8EE4Wo3G2Adk969QzkuN82Q1IR9rOWnCPR7kCuhuKB914F6iLUpnuqknKebSqtivQ6lgK4cwUw-ecAnWrdeBuGgf8DBcY-sqSDDX1E_SF2xnnnPYUP_eH-Vo0m_WfuxucJWWCkGPsITfl77EkJ33gWK9dPYlgnalLu6WGa5r3Zz45wOLyJvbMYt8trFmBCbIUAlVEgRR-Bn5jW0CObjpl13ut6Q6hY4RgzJY_EW0NYDU6XVa9rtG7r218-sr6nE8J7xs4Ksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رنگ عوض کردن سردار آزمون؛ حین جام‌جهانی خایه‌مالی عادل رو می‌کرد و الان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107563" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=tSsMxuSrH6_M-JbYjviRlnDtg2R6xEiffog0aevzOVCoO7E5HUqnIjvAisykQDOZ13yQvdlyVf-4qz845UxdyE6926CL2jng06PBILcglTtsKDTqe2EI_QJgvs4tGm34iCb-pIU5JbpWQA3NgJouKS3zTHvDRPuwzdbXqD-Ld6W7_qXYpHaS46KeMdX6uLptxJt-Bzni66sTdr6k0DofS5p5-ZA5IKQ-zRTt8GqMNzWP8VWjlv5IbKbgP59KwEZij5Cji7_-3gVh19OJpsSAtcascWjW_qKTxLm4ukz7LdlHFMnhDrgOtlFxy0H2iYMv2xwKJK1nX1KkvX8KCvgGUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=tSsMxuSrH6_M-JbYjviRlnDtg2R6xEiffog0aevzOVCoO7E5HUqnIjvAisykQDOZ13yQvdlyVf-4qz845UxdyE6926CL2jng06PBILcglTtsKDTqe2EI_QJgvs4tGm34iCb-pIU5JbpWQA3NgJouKS3zTHvDRPuwzdbXqD-Ld6W7_qXYpHaS46KeMdX6uLptxJt-Bzni66sTdr6k0DofS5p5-ZA5IKQ-zRTt8GqMNzWP8VWjlv5IbKbgP59KwEZij5Cji7_-3gVh19OJpsSAtcascWjW_qKTxLm4ukz7LdlHFMnhDrgOtlFxy0H2iYMv2xwKJK1nX1KkvX8KCvgGUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس ژوله به قائدی و قیاسی؛ ژوله وسط برنامه زنگ زد به قیاسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107562" target="_blank">📅 19:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8WsH9BukMb_d7oHu7cZiw2zd1GOUzpCMNbH1LAgM1-a46hAyX_taYZR9xreHzEfQSieLEpYGqV64EW9PaCZdF6jb3cMp8Xe5e4IjzYIc_6a9X4eWSGH7A2n7m1t9rDLbS0r9zELwJAzeB_jBh23PtnLFEXUGVE6yi0Xbd_Z4rIqOLq-GFbuRgtyuA_N_TewFDJABljUz76CrRjMRSmUcutEoDkFwcmcgyvY_yIkGTr5SpBv7cuf1XfftNTFTQGkd5-AiNa7o6CFj5R2MRc8OopXpYRs2RW3CNO8Gex_f_Ql9-s0TGmrayLcsNz4FkX_i1EOoyzcMJr3OnroglYPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107561" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=B85zjq9G5bJ6BZSe2jgCaqmr5IlKPuBXHnIgbURASSr_BzIstUznqFhF64S9NPIEX-nhTq5pzUFxi4rkDK4EFPB2COM_C-DAMgLuFn8rJIOZtPy1hgcrkavwFfHY1_tPyjciT1BuiU2sPw6tRF7FQtWaxrWBSCw5uh47L4Rlj8tl8U2jlnX5SSruKNS2mHgy264rDqeUyoQGp26QZMU4yXWKKvmK8ceDSkCoV_BXAczCq1R4rfnZBQAJXEj3VGO-DO7Kh0hn4kX4t9-iAye35IumbJD4h8XeBpJtEYj_hmorO6W0Yy2WqN7v2sq3J-5lv86MiQOxMx3Q5mVp1oaDPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=B85zjq9G5bJ6BZSe2jgCaqmr5IlKPuBXHnIgbURASSr_BzIstUznqFhF64S9NPIEX-nhTq5pzUFxi4rkDK4EFPB2COM_C-DAMgLuFn8rJIOZtPy1hgcrkavwFfHY1_tPyjciT1BuiU2sPw6tRF7FQtWaxrWBSCw5uh47L4Rlj8tl8U2jlnX5SSruKNS2mHgy264rDqeUyoQGp26QZMU4yXWKKvmK8ceDSkCoV_BXAczCq1R4rfnZBQAJXEj3VGO-DO7Kh0hn4kX4t9-iAye35IumbJD4h8XeBpJtEYj_hmorO6W0Yy2WqN7v2sq3J-5lv86MiQOxMx3Q5mVp1oaDPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های ژوله‌درباره جنجالی هوش‌مصنوعی در ارتباط با سربازی علیرضا بیرانوند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107560" target="_blank">📅 19:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=QUTEN4XTu81UknZTeLA21LH4Hpo8BLaSzqNzxdNIqpL5MvFz113dvzVeoTusHhZY5ct8Cz_fY23Rdku_0Bcw_bceI8N84GVjkcYWAd2WArw8F7XC-9RBgW_V1vsPYjF5P2tv17NIo0dgRxqZan6O9ue1-LPau4v8iSCcfT58k2kF5QHw4hjOfl7yIFKHMBaUaP5HR-977bzFufQIU_bR6VV_7KsgUcAGnPhonkgPwofkZHQjxrqz5Gn_R4FG-5MiP0NH4mARCK_7lnqjurpEOc7HGsp9wsDsFt2I06awXvqKsjbBF7QugdLJzxIYsLSx2bax-1zpIX50ngVweOrOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=QUTEN4XTu81UknZTeLA21LH4Hpo8BLaSzqNzxdNIqpL5MvFz113dvzVeoTusHhZY5ct8Cz_fY23Rdku_0Bcw_bceI8N84GVjkcYWAd2WArw8F7XC-9RBgW_V1vsPYjF5P2tv17NIo0dgRxqZan6O9ue1-LPau4v8iSCcfT58k2kF5QHw4hjOfl7yIFKHMBaUaP5HR-977bzFufQIU_bR6VV_7KsgUcAGnPhonkgPwofkZHQjxrqz5Gn_R4FG-5MiP0NH4mARCK_7lnqjurpEOc7HGsp9wsDsFt2I06awXvqKsjbBF7QugdLJzxIYsLSx2bax-1zpIX50ngVweOrOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
شهریار مغانلو بازیکن تراکتور: زندگی کردن خیلی سخته؛ مردم نمی‌تونن خرید کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107559" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107558" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugEbri3wXs9opFf_32OLeF7cLtciq-7ZBuVFWYYz6tBSWt7lCTq36rJ9wwfa5PXSBmlxt5tKiWIu8wkTQQVb1bbpu75QYBKCn5nByBaosQCswCgW5m1CBhMhI_MsC10J66MVb6RRSYG-A8CgnE9HSFwyxNBGLcpe_bSZlO-ondP6w_Z53TpViSCDKgSOOtFr8_Zlp5aMTdwqz0T2PmRPJoenW9AjsTEoVYhJKAu89iq2cNgUR3lz4uBaeDk2CMzlwSE90CXc90rZsxYf0YUTLLWqZ46ImFdgZonk8sG-WSS8-8fa3oP4qifNGsR4GfAemm1eTDDY-KfKgluiJ9bqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107557" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
آخرین وضعیت ورزشگاه مخروبه آزادی تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107556" target="_blank">📅 17:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=sma4zaDmo21NUsTyR3ULJ_AFtGePDfnG0ku611JV_HjBxqIEm1LKdQReR9xSDJyPcSg_1LTUBWLaO8gYL9JYo6i24aic4W4yYVK7PR7X0kF2apVRcXpOT0pmqq1AHC-vMpG4Y27zvurwH-qwgtAAq9VMEmV2zTOtfv_xttQWAWh6UkSaSGUWWyp2g2ydGHDiPwgflNCmQcl3rxbYMRHvOw_f-5-_BJ10ZHvmsFxYfZG-TAY8HwFp3_bZX4oTy8iznUitSIS1zgWY36Cu_tUJU0Gc-WSwrcLOjyZJtu5ob0Ll6a9WFxwzNY5KYuIExm9YFLXkNSG1BljkaD-wjdrFuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=sma4zaDmo21NUsTyR3ULJ_AFtGePDfnG0ku611JV_HjBxqIEm1LKdQReR9xSDJyPcSg_1LTUBWLaO8gYL9JYo6i24aic4W4yYVK7PR7X0kF2apVRcXpOT0pmqq1AHC-vMpG4Y27zvurwH-qwgtAAq9VMEmV2zTOtfv_xttQWAWh6UkSaSGUWWyp2g2ydGHDiPwgflNCmQcl3rxbYMRHvOw_f-5-_BJ10ZHvmsFxYfZG-TAY8HwFp3_bZX4oTy8iznUitSIS1zgWY36Cu_tUJU0Gc-WSwrcLOjyZJtu5ob0Ll6a9WFxwzNY5KYuIExm9YFLXkNSG1BljkaD-wjdrFuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دیس‌سنگین ژوله به حرکت کنعانی‌زادگان روی گردن عارف‌آقاسی در بازی دربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107555" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=atBXt0Twht0gWNfk6MzZwvIBr7sAEVci97BZtLyMaMyW2nl-Wj-gni60ePQsV_k7m0ZCxP3pZy_EpEDzsANsLWRuKSXkBwFSqq6S4DbE2bWugu2T8elPJ3Zko96ywDVsINYmu_TYW6pzDgb8R7INoCpyfPoioh36u-4ay8Ptr6kI5ulQhR3pdfZr7FeDwe3RVi1V7pcHoVgn25oGLoC9me2FP9v_Uk7MnQ3O2gok7HpSuqllKuJYbaIm10xI_NXYU09lADK231SA3op6o1dzK5uS4OjHxECefI-k0HMqgRwE2qEuJ9lU8hKtFokYRvwCPZmPGCjoV-dys1oY13eQOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=atBXt0Twht0gWNfk6MzZwvIBr7sAEVci97BZtLyMaMyW2nl-Wj-gni60ePQsV_k7m0ZCxP3pZy_EpEDzsANsLWRuKSXkBwFSqq6S4DbE2bWugu2T8elPJ3Zko96ywDVsINYmu_TYW6pzDgb8R7INoCpyfPoioh36u-4ay8Ptr6kI5ulQhR3pdfZr7FeDwe3RVi1V7pcHoVgn25oGLoC9me2FP9v_Uk7MnQ3O2gok7HpSuqllKuJYbaIm10xI_NXYU09lADK231SA3op6o1dzK5uS4OjHxECefI-k0HMqgRwE2qEuJ9lU8hKtFokYRvwCPZmPGCjoV-dys1oY13eQOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش‌ ابوطالب به صحبت‌های مسخره حسین عبدی پس از شکست ایران مقابل کره‌شمالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107554" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=J2agCl-9ys6Ms7sk6B8KFKrXsMnGjnjTs4NavM8nYATh9l5pkyidzgSVX_p2PGvS4a4rqfV2LrKmbBb7JC2b5mf78CppPjy2PvKBEc8vlJHbRD6tSgsxhrDW3VH3rwqBovkhzNGtNtTvGdVPTIeoYfJvgqNZGiMQblhhRnX9_h3vnRWC8V1J5bIKJfb9g9eJY9Aptsd9b1WTE2ed65xAKJSRtCxmW1egyL1HHC08aJDPk62RZB6EiliRZqljn72lR4Yn86A_DnqYGQ8zdGG61xwIb_MuFu56rsGYV3YFhEmpFJRG6dAbp2EHf_TUwG0ISUxmnQ9gDgNMKOKfvRX_6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=J2agCl-9ys6Ms7sk6B8KFKrXsMnGjnjTs4NavM8nYATh9l5pkyidzgSVX_p2PGvS4a4rqfV2LrKmbBb7JC2b5mf78CppPjy2PvKBEc8vlJHbRD6tSgsxhrDW3VH3rwqBovkhzNGtNtTvGdVPTIeoYfJvgqNZGiMQblhhRnX9_h3vnRWC8V1J5bIKJfb9g9eJY9Aptsd9b1WTE2ed65xAKJSRtCxmW1egyL1HHC08aJDPk62RZB6EiliRZqljn72lR4Yn86A_DnqYGQ8zdGG61xwIb_MuFu56rsGYV3YFhEmpFJRG6dAbp2EHf_TUwG0ISUxmnQ9gDgNMKOKfvRX_6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
همسر بیژن مرتضوی خبر از بازگشت این شخص به ایران را دقایقی‌پیش اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107553" target="_blank">📅 16:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=pkVw1GsRPquvjWCVbDKOJ9GQW5LHCSV12Cx1O1XCiHE7bew4nYsApbFR3giYMJqBpbDYtVHTIknycJkXMEtBu4KMR4ygrqkfHN74lLdJbryPoo9gm--Db_zZtUKiqxOPxFLdYTgDfQT1TbdzQN8bYijxKMWDHefoIKJ_azMx2CKCISUDtxM_8QHXn98Mx4EIscPiAHKlhk8RuPC_EoBuPSzWLdl-wpzFiZQzh2JFBmYYNHabRM7q3vnHJWz9z8MRilWuxCt4kQGhCHkIMujAUK7lHmKHTvwBTMmjUSjjLiQ4_RMCglPMm48wK507PvZanTOhQVc5OT-NgdfINsGiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=pkVw1GsRPquvjWCVbDKOJ9GQW5LHCSV12Cx1O1XCiHE7bew4nYsApbFR3giYMJqBpbDYtVHTIknycJkXMEtBu4KMR4ygrqkfHN74lLdJbryPoo9gm--Db_zZtUKiqxOPxFLdYTgDfQT1TbdzQN8bYijxKMWDHefoIKJ_azMx2CKCISUDtxM_8QHXn98Mx4EIscPiAHKlhk8RuPC_EoBuPSzWLdl-wpzFiZQzh2JFBmYYNHabRM7q3vnHJWz9z8MRilWuxCt4kQGhCHkIMujAUK7lHmKHTvwBTMmjUSjjLiQ4_RMCglPMm48wK507PvZanTOhQVc5OT-NgdfINsGiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
قلعه‌نویی میدونه ترند چیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107552" target="_blank">📅 16:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGcz2n6oL2ZGg-vG1_eSP5wUpW7eHcPXUfYeHx0bUbug4dHxN91s91UirWvWb_DBHHzZuJww-DC1HYeNInpfp1eK0bwJFWwr4vxtuvL2iD7ZWzlkpYysebElk2Y62GTWbj2W-rY1xaM5rC_f6ifWaKpis_Px6rYu_aqmmrzaxrgPH6EpypfVofu1tCDxyq3C0E1ESo-ExiHPmEar9Wd2n84Iq8TgzhJSBVlU3DtNdKWTHlDVp5Tg_03DPgOtmEZYyvql-IqUpHmH4Cf6I-E8n-HkS4nQ5YPhl6jPzCvLX0tyJ0cDvNvVJVfddCTPZdaishnLSysb_C-KslsNH_GXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
⚽️
برای اولین بار از زمان رقابت‌های یورو 2008، کریستیانو رونالدو در تمام طول یک مسابقه، نیمکت نشین بود و حتی یک دقیقه هم برای پرتغال بازی نکرد.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107551" target="_blank">📅 15:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=EmK8Qk5jeMzG5V3-a1k-qy1jkZdF-if6nCQo8HAYP8RTEnXRjLHoMZsDtpTEiAA7Z0m1T-P-OWc91kceVetsI83cb5mJrH7jfSf7wvpJmDXxh06zKGeFEbxuk9daqhpZtwAeJc_hLI3VaObm3Qr7DOaeqo3F7elUvFY7jOIzE1Ge8PGVDKhW46sHxN-LfToNaV_EygxCVFyrv4q8g82KgS_5M_LovVdbU4cCsrKPqbfkyK7ilA-B_FQWhFFvuwrdv1wZpNQqdJ38H_qjRgUb6H18pO7ou_y7v6aq0a2vC6-3xNeY9ymywWWoGJ4guOQJkO2Y7AKRbaj-aN9eYBgO54WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=EmK8Qk5jeMzG5V3-a1k-qy1jkZdF-if6nCQo8HAYP8RTEnXRjLHoMZsDtpTEiAA7Z0m1T-P-OWc91kceVetsI83cb5mJrH7jfSf7wvpJmDXxh06zKGeFEbxuk9daqhpZtwAeJc_hLI3VaObm3Qr7DOaeqo3F7elUvFY7jOIzE1Ge8PGVDKhW46sHxN-LfToNaV_EygxCVFyrv4q8g82KgS_5M_LovVdbU4cCsrKPqbfkyK7ilA-B_FQWhFFvuwrdv1wZpNQqdJ38H_qjRgUb6H18pO7ou_y7v6aq0a2vC6-3xNeY9ymywWWoGJ4guOQJkO2Y7AKRbaj-aN9eYBgO54WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
دیس امیرمهدی ژوله به جنجال خداداد عزیزی نسبت به پاهای پرانتزی امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107550" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=vRg4Vq5jKNQn-yq4DDyiKSB3rhoC4Y_vPYeOcM7BzNaU-_UIK_w6-OakmR9nhqkDJuAuh2sfrqh2499Gd8i2_KYwywZ54F0BzJSc9jbUDzAyK_nIpXAp5OzWTi-2lGJYkxHLI3h73kucoBX9tmMuNScP1Czaktf5mHJCHMtHqGtQtll2fQPa1sfz2IFOlZP9GOgdnXMSkfmCkJM7Zs8VAJhqN48wjr0T6IOzbOaHl6H0IuqWGbMz2j8nTKlsgV6ipBwxpwwkcBc69FvOLotfP6xcodI3Dk5rx7Bta6-t6ueIKjX8MrNz1sYDB0zn22xhJj04037yYq7OW4NTFVShnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=vRg4Vq5jKNQn-yq4DDyiKSB3rhoC4Y_vPYeOcM7BzNaU-_UIK_w6-OakmR9nhqkDJuAuh2sfrqh2499Gd8i2_KYwywZ54F0BzJSc9jbUDzAyK_nIpXAp5OzWTi-2lGJYkxHLI3h73kucoBX9tmMuNScP1Czaktf5mHJCHMtHqGtQtll2fQPa1sfz2IFOlZP9GOgdnXMSkfmCkJM7Zs8VAJhqN48wjr0T6IOzbOaHl6H0IuqWGbMz2j8nTKlsgV6ipBwxpwwkcBc69FvOLotfP6xcodI3Dk5rx7Bta6-t6ueIKjX8MrNz1sYDB0zn22xhJj04037yYq7OW4NTFVShnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
جام جهانیه یا مسابقه‌ی انتخاب کراش جهانی؟ کنایه ابوطالب به لیست نفرات قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107549" target="_blank">📅 14:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=RYsPwKKjL9I2gZM2adBm0dItU7YTXY3S1ynHdV6HdOBm2WEIFwBEoHL8dst69tmkow08ujwq4OnIYy_Lug8pnnuXhM8U2Du8v5hSKpWHgc1OP5WoYrpfHdHOkKFAnvJtc147a7fQLL9AudmlrWthPTRFUySGWvkFKpoYCE2sHhBjJuEosbYVgXgafumd7jFZa9FOPjVOeM6CXVxYdkVXE_H8peDxiZlaW78m9Uyjchbsu_5ZNwXpZcJ1BV2KPPuNsU6ABHRBSMOtt3QzypYfhzoLZBn0f4iu7YlLM7HB9d2XHZVEiFz-AJ_ntxCT35Y_gKTQF4iPrE1-fO6WHiOPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=RYsPwKKjL9I2gZM2adBm0dItU7YTXY3S1ynHdV6HdOBm2WEIFwBEoHL8dst69tmkow08ujwq4OnIYy_Lug8pnnuXhM8U2Du8v5hSKpWHgc1OP5WoYrpfHdHOkKFAnvJtc147a7fQLL9AudmlrWthPTRFUySGWvkFKpoYCE2sHhBjJuEosbYVgXgafumd7jFZa9FOPjVOeM6CXVxYdkVXE_H8peDxiZlaW78m9Uyjchbsu_5ZNwXpZcJ1BV2KPPuNsU6ABHRBSMOtt3QzypYfhzoLZBn0f4iu7YlLM7HB9d2XHZVEiFz-AJ_ntxCT35Y_gKTQF4iPrE1-fO6WHiOPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پاسخ ابوطالب به انتقادها از برنامه‌فان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107548" target="_blank">📅 14:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=abOfxnklF0sYAyC9Fyvb86F4xZyZHm6R_IC__kBowvFgk7ecAtOaaKdbwxObHA0dv4M9broyjTtP7DOdvsgPP4hNHmdyqAhW-1TzMLXLuaxoE0g9kx0uHBKKZRpetBg05pEL9iXry2iTOLy2TUQDNjEpmv6qlyoQPG8vRwsCHTRA_EC8rtrahCEVhW2Uo90dIU4rIqAnAas79g1JlAQcQWvmuFYf1CPoWSdbfQfO1cC0VzWWQbMd1130X254kqUbQiVEqi_uJVKWxkmk009hBaU3tHnLkE7EUFQF3egAXcPBJbiHEiWGyNRNzsNvYK87FFsnuIXp9Lct2myEZJouUJRcLzy0C3tyWnpclYR8Jl10REXwqDBgVau-q9A91NwayVlEcdBJogQ9Uht3bySE1ykEZRebg4Rcf2Wk9DadbXac85ZvtCtb2sJQ8ERC0cjAyZ7Km75GknSycLnF_SwpRcKgNg-uxJjI54MRhqYwK4F_qhjrD4xfHGNwGHFFw-1TAKNO8oxSF98lvqOOJ59Z_I8JsujeFy35sJqbETsPGcrNOONcj_JEwKUFv8V9lH0YFd174p1DyX6M7rwiSC1VC3LWpHtmyqG4ix94HkNoNnspDUXCG6qqbsraExNQ04hABDAVGGztTaXrbX6KeUyeI7J6z6CzcBU-m4MQPwDfsYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=abOfxnklF0sYAyC9Fyvb86F4xZyZHm6R_IC__kBowvFgk7ecAtOaaKdbwxObHA0dv4M9broyjTtP7DOdvsgPP4hNHmdyqAhW-1TzMLXLuaxoE0g9kx0uHBKKZRpetBg05pEL9iXry2iTOLy2TUQDNjEpmv6qlyoQPG8vRwsCHTRA_EC8rtrahCEVhW2Uo90dIU4rIqAnAas79g1JlAQcQWvmuFYf1CPoWSdbfQfO1cC0VzWWQbMd1130X254kqUbQiVEqi_uJVKWxkmk009hBaU3tHnLkE7EUFQF3egAXcPBJbiHEiWGyNRNzsNvYK87FFsnuIXp9Lct2myEZJouUJRcLzy0C3tyWnpclYR8Jl10REXwqDBgVau-q9A91NwayVlEcdBJogQ9Uht3bySE1ykEZRebg4Rcf2Wk9DadbXac85ZvtCtb2sJQ8ERC0cjAyZ7Km75GknSycLnF_SwpRcKgNg-uxJjI54MRhqYwK4F_qhjrD4xfHGNwGHFFw-1TAKNO8oxSF98lvqOOJ59Z_I8JsujeFy35sJqbETsPGcrNOONcj_JEwKUFv8V9lH0YFd174p1DyX6M7rwiSC1VC3LWpHtmyqG4ix94HkNoNnspDUXCG6qqbsraExNQ04hABDAVGGztTaXrbX6KeUyeI7J6z6CzcBU-m4MQPwDfsYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز بازی انگلیس مقابل اسپانیا که حاوی نکات بسیار دیدنی برای علاقه‌مندان به فوتباله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107547" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
رونمایی فدراسیون از معیارهای تعیین رده‌بندی و قهرمان در صورت لغو فصل:
🔻
۱-در صورت برگزاری حداقل 75 درصد مسابقات رده بندی بر اساس جدول موجود.
🔻
۲- در صورت برگزاری کمتر از 75 درصد رده بندی بر اساس میانگین امتیاز در هر مسابقه.
🔻
۳- در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
🔹
تبصره: سازمان لیگ می‌تواند با تصویب هیئت رئیسه روش عادلانه‌تری را جایگزین کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107546" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=iynrnYFw37WqflaZrnw5tcLhTdXnTq7soHGF1dz_HRA0YdAsyltQIzuSNlRKTfCwXmcwOIozvCMdEgxvL6V3U8_zelaRYRi5XRxAIZ5bPMOl-Tj3Cq442jUjA6BhQtAStJoe-LPrJaAjr8zMnR3Ghffp89Vt_StnyrQyxlD9GAWqQFrNMI_ESa1XD1hT4fnOSzcGG--vNVKxxaDTvc9TvH8pdcR320otn_El1JvU-RmHAQglGvtjhM9aautyiJnTakAuXJBxiTbMQDWRCJDIWC3ZAvCf28c8zHU_lTt4zBTaAFmBCxm-qMTE9iVz0XVLw21BJKJ3GwVi9BcrqCfmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=iynrnYFw37WqflaZrnw5tcLhTdXnTq7soHGF1dz_HRA0YdAsyltQIzuSNlRKTfCwXmcwOIozvCMdEgxvL6V3U8_zelaRYRi5XRxAIZ5bPMOl-Tj3Cq442jUjA6BhQtAStJoe-LPrJaAjr8zMnR3Ghffp89Vt_StnyrQyxlD9GAWqQFrNMI_ESa1XD1hT4fnOSzcGG--vNVKxxaDTvc9TvH8pdcR320otn_El1JvU-RmHAQglGvtjhM9aautyiJnTakAuXJBxiTbMQDWRCJDIWC3ZAvCf28c8zHU_lTt4zBTaAFmBCxm-qMTE9iVz0XVLw21BJKJ3GwVi9BcrqCfmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تصاویری از علیرضا بیرانوند با لباس سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107545" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=gMDGrQFc7aD-mCu5PrTS_SRNG-paOCzjL2Zim2mO8JcpPvYlOy-vwVgzhAml9ciM5bYJsMVOFJYM9xopzihFKr-HOnSEdkMsuFXCPjtVYeSFIK820-m92KJ7YlW1KxmCpwM0P5Q-UXLSmYaaSPQtcWp3NkZ40RU1-safdbBWi14Xf218kzFuPmeWABkaVSkuxumY4N8TvhcRY7HR-9QiC5buQP9XzIibwGDXmYyzKnX-65u0T81Te2gSajBFPkm2dAgs0xxEpQdEyFTm8WpvK8ifD9u-FnhyRlcXhu986Y7NB5nNlQ_kui8u5QWf1L8D52Je3ggHo5VSwVOC16NG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=gMDGrQFc7aD-mCu5PrTS_SRNG-paOCzjL2Zim2mO8JcpPvYlOy-vwVgzhAml9ciM5bYJsMVOFJYM9xopzihFKr-HOnSEdkMsuFXCPjtVYeSFIK820-m92KJ7YlW1KxmCpwM0P5Q-UXLSmYaaSPQtcWp3NkZ40RU1-safdbBWi14Xf218kzFuPmeWABkaVSkuxumY4N8TvhcRY7HR-9QiC5buQP9XzIibwGDXmYyzKnX-65u0T81Te2gSajBFPkm2dAgs0xxEpQdEyFTm8WpvK8ifD9u-FnhyRlcXhu986Y7NB5nNlQ_kui8u5QWf1L8D52Je3ggHo5VSwVOC16NG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚽️
توصیف امیرحسین قیاسی از امیر قلعه‌نویی: جوان‌گرایی و تاکتیک مناسب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107544" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=oUY3l56pHwTbN4zRcpRw__w5y9OKagnmNQYoja5JEuA3UwBwM7IAUtIjSy_FhQWSb4yVa2aO8ALhs4Q9pEh6HunOuClx6TNiB0vrQgD797quDBAXK0x1F4Mk188NQo5j3Abm2gc1VzAZd5jh8LGRBQCqsOJQ0Cw07urZKKvGgtZSXB8CJWf3ba5NI6-S7H_PLAHRjC8X3dU4s_BcALvCe95kCbjWhTsoT5_lRwGqaxR1rHrD6a5ghje0ofCiL05zL9qcx52282DyVnLO-dalPyKA8ryepp4F4sSy6ROed6MjLoHyqBJYhICz0aXC6kI6s5awpflA_Mla2Pfc9h214w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=oUY3l56pHwTbN4zRcpRw__w5y9OKagnmNQYoja5JEuA3UwBwM7IAUtIjSy_FhQWSb4yVa2aO8ALhs4Q9pEh6HunOuClx6TNiB0vrQgD797quDBAXK0x1F4Mk188NQo5j3Abm2gc1VzAZd5jh8LGRBQCqsOJQ0Cw07urZKKvGgtZSXB8CJWf3ba5NI6-S7H_PLAHRjC8X3dU4s_BcALvCe95kCbjWhTsoT5_lRwGqaxR1rHrD6a5ghje0ofCiL05zL9qcx52282DyVnLO-dalPyKA8ryepp4F4sSy6ROed6MjLoHyqBJYhICz0aXC6kI6s5awpflA_Mla2Pfc9h214w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین‌قیاسی درباره سفارش غذا ۶۰ میلیون تومانی برای مهران‌مدیری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107543" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=WzP6SbUW9cRViP6ilsN9xhd5IhS13O82ZH27z-YWqXP8_U7NxkuwZV22sk3aLrqdGD-9HSOzF0_BsWwD_5ZNS06_WWXdS6Rc5QBhMcDfr2rGTrasuCbm7r9YTpD5xJmVI-S84O98SatdV9C8Vyz1z8yAE6vFbMm_AgJjHTppmIYL8wW65vTRgiTozvE9Y-wDZLT-Vht5D4nLd0E829nlGAjfGaiFlEoYzZBbfMkhzci5aEOpJKhTiUrh8w8ahK94DcUcNjqC0rgn-YZ_iARpxdxaRKtelbRspHfJOLpCBiBCxO40Uuf6v8ltpu_JyX9wHkihww6XdTTGilZ08OIFnmfIrR8vH_SoK0acROD8JYRuJzTh5oZY-_mgXHowSuND2gaXDqnVQY0K6Oc7k7w6RgDf4jvlomy4nfrmI_nDDQkGlVP3iGiHWLszFM140noA1c4fT2SjtQpe0g2BkitBQpM9ZOojTkspFAYmeG7TtWuvqI5gW5vbjCLjMweLaZCkZuH8jPrG_WiJJhZ4c1OQuuDdSXtR-a59d0Ev9X4fse7wgHt-9NUy4a4cmUYjhZUaHdbMTZyfNkJiW0XNvDHz42As1iNTyD8dJy6ocVUQjSwFwtEMaXWdRx-8qYs0XxO9XCjdFawmPuE5gKdvt18uXep4Vqu3aZ3EKFRqgUwKfuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=WzP6SbUW9cRViP6ilsN9xhd5IhS13O82ZH27z-YWqXP8_U7NxkuwZV22sk3aLrqdGD-9HSOzF0_BsWwD_5ZNS06_WWXdS6Rc5QBhMcDfr2rGTrasuCbm7r9YTpD5xJmVI-S84O98SatdV9C8Vyz1z8yAE6vFbMm_AgJjHTppmIYL8wW65vTRgiTozvE9Y-wDZLT-Vht5D4nLd0E829nlGAjfGaiFlEoYzZBbfMkhzci5aEOpJKhTiUrh8w8ahK94DcUcNjqC0rgn-YZ_iARpxdxaRKtelbRspHfJOLpCBiBCxO40Uuf6v8ltpu_JyX9wHkihww6XdTTGilZ08OIFnmfIrR8vH_SoK0acROD8JYRuJzTh5oZY-_mgXHowSuND2gaXDqnVQY0K6Oc7k7w6RgDf4jvlomy4nfrmI_nDDQkGlVP3iGiHWLszFM140noA1c4fT2SjtQpe0g2BkitBQpM9ZOojTkspFAYmeG7TtWuvqI5gW5vbjCLjMweLaZCkZuH8jPrG_WiJJhZ4c1OQuuDdSXtR-a59d0Ev9X4fse7wgHt-9NUy4a4cmUYjhZUaHdbMTZyfNkJiW0XNvDHz42As1iNTyD8dJy6ocVUQjSwFwtEMaXWdRx-8qYs0XxO9XCjdFawmPuE5gKdvt18uXep4Vqu3aZ3EKFRqgUwKfuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مارادونا: ۴۰ تا بازیکن از تیمای مختلف ایتالیا روی هم،  به اندازه یه توتی نمیشن!⁣
اسطوره رم ۵۰ ساله شد.
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107542" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4869197932.mp4?token=Z_8jUHpsXigb7sAj_GEkpoMJ0OqmwUWT3LKTkhcAs5HwvMLpEBQCsfxy_qyXDKug4NZhinumfHrdPzB40lWkZ3bI-2FiZGaw9oONfxyWy18nLK_umrqK5yhXIhr6_Bx4Tx7NxsDJPUuylHlZyB0j6yZtVAP9RlaAdT1Rck4psUYjnzN0z_EgTMu2hvftgT8N7XuZxDMLNHKtxkhTjnopZKet46pNOgJuCOkOYWGNJiMAv2iGjcx6fGNEqOMfBpcnHhH2XQJL77dvBMarxynAgDYwyFsxghPP_nygYzBbFHZSG2GThhnEi9rzmzHVsWo_BnvONc26XGjz81XcD8Ntog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4869197932.mp4?token=Z_8jUHpsXigb7sAj_GEkpoMJ0OqmwUWT3LKTkhcAs5HwvMLpEBQCsfxy_qyXDKug4NZhinumfHrdPzB40lWkZ3bI-2FiZGaw9oONfxyWy18nLK_umrqK5yhXIhr6_Bx4Tx7NxsDJPUuylHlZyB0j6yZtVAP9RlaAdT1Rck4psUYjnzN0z_EgTMu2hvftgT8N7XuZxDMLNHKtxkhTjnopZKet46pNOgJuCOkOYWGNJiMAv2iGjcx6fGNEqOMfBpcnHhH2XQJL77dvBMarxynAgDYwyFsxghPP_nygYzBbFHZSG2GThhnEi9rzmzHVsWo_BnvONc26XGjz81XcD8Ntog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🇳🇱
یک‌ماجرای جالب از فوتبال هلندی - بلژیکی!
خانواده آقای فن‌بومل، خودش، پسراش، زنش و البته پدرزنش⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107541" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=u7M4Wx9F1WoU9SJLmowxZHSIAPR1afwoABnS78-TNFXoB7NcayzNnaJDoXVSQ8ci_J4PQwWPEWYoyY6NXnUdpSTKNdMvoopcZT9zgRSJ5z8Zu1viEbfDXywSLSkm-xHnDk4n0YO3Z-LRsMpe40nPYsERIL3cLeHM_V_AzFSeWvBablLr34gjCaII0rXzmQy9eEFBwkTglcDBnavE1zrCMwF2GXfv1G6D775VgrAvLMJ-03tetcSbmPowGBr07RBxuMiF4mcYULUcIEKpDtA3cG9ZxdtWJD9U0VhUUeNDKuU5RIU9Q85VM1n2pIDh6CEsK5m1-2IMJtOs-YWDvjvnUxz2_XB7-29RfrbSTUzYanHLkftr3WhryzoIDi3S0Isx6265RqmIe3i1D8zx-o4p0fBCxZZYDvgVR3QKbHIVJpNcRuefE1KW36pONSuxxI-zau_UZW1d-m9Iuq-ZGhe3VsP6GXe_G5fcFo6jQz7UQFpV8-Mf5NBBk3ReH-FCsqK3I-057kmCnO1j4nN_mcIBktvtD_mSO_02HmhSFKbg4Zk8T40XuK_3xqNNvaOvxMpbVZGkSWwrHvWyOXqS9dc1gR3nDeC8SkAHXKzF8fGWb5gtMSeUy9CxFv-uh2WXORjddKsNUItdevwH_D1waegXK-HItMtVt19utADpoDLt0aY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=u7M4Wx9F1WoU9SJLmowxZHSIAPR1afwoABnS78-TNFXoB7NcayzNnaJDoXVSQ8ci_J4PQwWPEWYoyY6NXnUdpSTKNdMvoopcZT9zgRSJ5z8Zu1viEbfDXywSLSkm-xHnDk4n0YO3Z-LRsMpe40nPYsERIL3cLeHM_V_AzFSeWvBablLr34gjCaII0rXzmQy9eEFBwkTglcDBnavE1zrCMwF2GXfv1G6D775VgrAvLMJ-03tetcSbmPowGBr07RBxuMiF4mcYULUcIEKpDtA3cG9ZxdtWJD9U0VhUUeNDKuU5RIU9Q85VM1n2pIDh6CEsK5m1-2IMJtOs-YWDvjvnUxz2_XB7-29RfrbSTUzYanHLkftr3WhryzoIDi3S0Isx6265RqmIe3i1D8zx-o4p0fBCxZZYDvgVR3QKbHIVJpNcRuefE1KW36pONSuxxI-zau_UZW1d-m9Iuq-ZGhe3VsP6GXe_G5fcFo6jQz7UQFpV8-Mf5NBBk3ReH-FCsqK3I-057kmCnO1j4nN_mcIBktvtD_mSO_02HmhSFKbg4Zk8T40XuK_3xqNNvaOvxMpbVZGkSWwrHvWyOXqS9dc1gR3nDeC8SkAHXKzF8fGWb5gtMSeUy9CxFv-uh2WXORjddKsNUItdevwH_D1waegXK-HItMtVt19utADpoDLt0aY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
روایت عجیب و غریب میثاقی از معافیت پزشکی برخی از فوتبالیست‌های مشهور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107540" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=jZYwqHtbwcmi9perL3CTTlEiFUhW1KPGhlVd_hGBPuA7vwjiOpneEBTzmJgUAlqFHYksmxRMc1IyFEbolz8G2Da6HuXcWrSSo1R_4Uze7FyiWBJxK_0rV3wULD-IxDqt_oa2oVXf6q4EU9H60Df41JH_Ues_2RPAI7hF-hc2_obEVQ-DLRredheB-G2lio6uLvT2uPt122o5N7xfkj17LV00gf-ctyZjmd5u2jD3y0tpAxvdq1aHj2SnhLoocAMJFU0_FPzIhvbajX6waJ3CahSntmaAdk5rkPlOXf_sf9VmexKHg6N3p5UvmjD0wH881Yarq_BRd8roJihDWFCTaC2wK4pUjAqVZauJgP4EBtQEfXQX8wunR1oJsE71HWwEP_WnZjjGe3pGQfkmwAKBFfjjLF9sFzorMbk-GCBYwyaDasyr0RVyFrTkDofybyWC9PWsBNP6q2ECMaMX50whXRHniV3vXxFB3ClmAVpA6r3yf-mxerqU4UxGDq-SidwqGo3LqUu1rK01lyffn-fWRnUP54zoyoKUvyGEwNuEtBJSweSf7IMd3ViYbzrnjvysd1juCAaOSQjEkSeca3Hd96Zn0tz36M8vKXaUkfjS0tcSReJFezdMqX3eYWTKp6fmWjbe7yZlJNrJ_Ec519sBOjFLgWE_vxZ-4pJKRAIE-X8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=jZYwqHtbwcmi9perL3CTTlEiFUhW1KPGhlVd_hGBPuA7vwjiOpneEBTzmJgUAlqFHYksmxRMc1IyFEbolz8G2Da6HuXcWrSSo1R_4Uze7FyiWBJxK_0rV3wULD-IxDqt_oa2oVXf6q4EU9H60Df41JH_Ues_2RPAI7hF-hc2_obEVQ-DLRredheB-G2lio6uLvT2uPt122o5N7xfkj17LV00gf-ctyZjmd5u2jD3y0tpAxvdq1aHj2SnhLoocAMJFU0_FPzIhvbajX6waJ3CahSntmaAdk5rkPlOXf_sf9VmexKHg6N3p5UvmjD0wH881Yarq_BRd8roJihDWFCTaC2wK4pUjAqVZauJgP4EBtQEfXQX8wunR1oJsE71HWwEP_WnZjjGe3pGQfkmwAKBFfjjLF9sFzorMbk-GCBYwyaDasyr0RVyFrTkDofybyWC9PWsBNP6q2ECMaMX50whXRHniV3vXxFB3ClmAVpA6r3yf-mxerqU4UxGDq-SidwqGo3LqUu1rK01lyffn-fWRnUP54zoyoKUvyGEwNuEtBJSweSf7IMd3ViYbzrnjvysd1juCAaOSQjEkSeca3Hd96Zn0tz36M8vKXaUkfjS0tcSReJFezdMqX3eYWTKp6fmWjbe7yZlJNrJ_Ec519sBOjFLgWE_vxZ-4pJKRAIE-X8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
‼️
سه‌ سال و نیم بدون رشد و تغییر در ترکیب نفرات دعوت شده توسط قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107539" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4GYb4Z_7dvkCnv5Nq76aQsX2uVhIxcChdM6MNe6NxdSHtQIxhIF0hBjxnD9wL9P5fqTz0UuGhax1hktu6vhk06N7BkhX8L2Jc4ll4HiXf--yZlOAk3Y-ABLMHyssw-JnK8sXDuc0aSrk_3gondQvQUnn_Nk7ytkDfDe4V3_ElN6-nOv8aep2xa0Ib1qyehQ4VCG3X_JX_yJsrdOUNv1PtGywVbovFquO_VnFp-qXnxUtvZG2G7OKQJAsnC82sP8RTqDQ8Rodqrp7FHTr7kzDq5ckfw1bNfAj7wxlRZMuUTyU5yobH7POkhxW-Af7GyFMcP9ikwOTVMJM64-058ZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
📊
ترکیب منتخب دور‌دوم لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107538" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
🎙
صحبت‌های شنیدنی رسول‌مجیدی درباره کیفیت آکادمی‌های فوتبال اسپانیا که زمینه‌ساز نسل‌سازی‌و قهرمانی در جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107537" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107536" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107536" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZMrBNy4miXlMKByS-estidiN3fXbA23xrKDTbhBX_nSY1F5MBZWE5t6aupyJWKZ6BWuD3W9g7kFRnf_eTR78l14BO28T-Litt1qtcMrZEvSCCTwDhol40eBPVSq_wryubzgHVqcJrKTWkAt_hkNNcXUYoIjtngn9K1q7_iCv1jzySZC0XwIaf5GyutDhF0yTbYXPZjzy39t4B0BBzAAX8MUJeSXAf4e2fyNLMcdmkyo-RbyJJrUtoAtNT5bIhdVQW6TwpH4RhpspB936QFOcupRawwosxy56xJwIUruJFoimQlLbUA_nAPvyJwrlx4W8UkXqe1fxU50iGMEMxOEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107535" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0dJFJYcTlbHnaYvf-VSC5BMOncBuYzObWZh8KkDqBoxW93RvHENi49GjGZUPuf01J1E-yHLuXQy5rqSiXRp8UG1B2ATSSxI0F1Ts6HCr_Lr9sbHNW1S3Kx7mUf4tWARx56Uk_XHdQcgZ1S0glDwexFysFrhR-lP-qo2N4rbdLg1hBiuFEH0CWZjts_YEf4E-6UYlgaMjwFZ4R3GuWChJW6mmrwhcRNJMmQqHQQMyRtb-yjvsNMy7kUrPPViJxuDESlHlGEPr3wqyGI-Ay9xDTTVipJMYUzMeLI41q6OCMQVPNcOhPY_HB4s7ChkIlYzP8Vvx6PjqaLpve7hrkeSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
رومانو: رافینیا اردوی برزیل رو ترک میکنه و برای مراقبت بیشتر به بارسلونا برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107534" target="_blank">📅 10:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9vTn3JnIuyrGTDLiJ_yRKXuCInAgQwjCAcCPE9fNaiZJYTXG4BlHgZN73N6P_WgpZXPjD5CP7Fla_acG5eh6_FMhExs4jYOBbwOEatZHVjPZVJXicYxa8nVk0vybTQAuKoMpgiysVCwSuuDRIrXfaEFfqEuVJHW8-LIs3dOx-bqzjdlVXcWbgG9akjOiOvG2FucPN6GN6qnyetEdvxozSnCIvwZkXGdSQ_i9VeuRSuROlpD3XZKMQatRamDRJ3vCDR5wuPJY1S0S-oDAgRMMl79OuGw3C88dw9xX4LYX1Qktd1ov3_gjec8t_SXhIZKKAjFl3pm7we6iqm0gqaeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🇪🇸
اسکاتلند تنها تیمی که توانسته اسپانیا تحت هدایت دلافوئنته را در یک بازی رسمی طول ۹۰ دقیقه شکست دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107533" target="_blank">📅 10:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78614739b9.mp4?token=sv7huPkUtS2fm9SzsbLB0oCdwJRLkPsbRgQMZBsgtVw-ocMIOM_vtnbQMM8qYCUcbEI9OMDYB8dK9w2H47H7gZQ1y1ma2hce7uEZDKBe1ko1o-y-IXrhVmqDR7lxNAhsTGkhlPULywX1yRNqgnnyZRyIfLIwIhr6obO4xBOujCcW6RTNX_yE0ZmPxxvTgWn9msDjwr-nMZ6RnILwa_Gpb17eRyTJvbXQwguoOyV7Fjps2P0HBWi2NhyvTiQh-hLSwPS5Q29y4h5wzM3Kq6RMMWT0T-uWTxzAcq5wMy94zXuQ5u5uLTmNDWdajgowCYYMkJkATKGV9mB3gdw_gAog9BGLCUJ_rxpev8uqliUoVH1dZszPl2b4EVJkEkDOYJlBt0GPM277ZXwFa4icYaHfWGM7y-ifKg-0gWi9Cr36lu5kR1oDyIgT4E8JdGbClDInr9_4VShBxgozoVr9tOUtokmgy3K31HSyyiq9e4HxLrHXkkhjLI8SWKoUHuIDyfd2W15prbf9pxZcPaWomJJ_g86Hne40Gwe2L2nCJ-oUfQ1P73LTkkvVjk79sPDUcwYnJsRa7CWkqzQxt0S28tzE67Pfy9lNZeda3mxdWbwYI0QMPoKUmxZa6am3OcMs3v4hFD91hiUp7FkKyISGK-dXBODxvlLl9K6LQXJbT7jhLY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78614739b9.mp4?token=sv7huPkUtS2fm9SzsbLB0oCdwJRLkPsbRgQMZBsgtVw-ocMIOM_vtnbQMM8qYCUcbEI9OMDYB8dK9w2H47H7gZQ1y1ma2hce7uEZDKBe1ko1o-y-IXrhVmqDR7lxNAhsTGkhlPULywX1yRNqgnnyZRyIfLIwIhr6obO4xBOujCcW6RTNX_yE0ZmPxxvTgWn9msDjwr-nMZ6RnILwa_Gpb17eRyTJvbXQwguoOyV7Fjps2P0HBWi2NhyvTiQh-hLSwPS5Q29y4h5wzM3Kq6RMMWT0T-uWTxzAcq5wMy94zXuQ5u5uLTmNDWdajgowCYYMkJkATKGV9mB3gdw_gAog9BGLCUJ_rxpev8uqliUoVH1dZszPl2b4EVJkEkDOYJlBt0GPM277ZXwFa4icYaHfWGM7y-ifKg-0gWi9Cr36lu5kR1oDyIgT4E8JdGbClDInr9_4VShBxgozoVr9tOUtokmgy3K31HSyyiq9e4HxLrHXkkhjLI8SWKoUHuIDyfd2W15prbf9pxZcPaWomJJ_g86Hne40Gwe2L2nCJ-oUfQ1P73LTkkvVjk79sPDUcwYnJsRa7CWkqzQxt0S28tzE67Pfy9lNZeda3mxdWbwYI0QMPoKUmxZa6am3OcMs3v4hFD91hiUp7FkKyISGK-dXBODxvlLl9K6LQXJbT7jhLY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
واکنش فردوسی‌پور به مصاحبه‌های فرمایشی و سفارشی ملی‌پوشان: سردار آزمون، با سابقه بازی برای مورینیو، وادار به گفتن چه حرف‌هایی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107532" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481359e02.mp4?token=hSLZ0QX2d5g045zcbk5LX2-p_Qgq1o_TaBD_mmsJijr8JHGUw32dwmzDIo8oHnGT2af97BvM6xpz868TPYrB-c3wPwr5v3-tMK54i3PBcTlnJHe3LBXUphNWkeBemjo0r64aYgcXJ9LUxnI0pUoSxZBmN9n2K4tKmc3tn96SB7mbkhVSPFwXBTC-dIOooacGPiBo0ghOVrIPMx9CKWnRiZ58PUiBrqTuObRM_LmAYlmmAQuqlqIutaPp2jiRxHmhN_8DZ-lr6mVLSLV-18IilpniK9cOPZC2GzuV2MykgiMCFys9_jDM3qpKGnle8NL2uRSsj87hjWw6XtBMK8eXjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481359e02.mp4?token=hSLZ0QX2d5g045zcbk5LX2-p_Qgq1o_TaBD_mmsJijr8JHGUw32dwmzDIo8oHnGT2af97BvM6xpz868TPYrB-c3wPwr5v3-tMK54i3PBcTlnJHe3LBXUphNWkeBemjo0r64aYgcXJ9LUxnI0pUoSxZBmN9n2K4tKmc3tn96SB7mbkhVSPFwXBTC-dIOooacGPiBo0ghOVrIPMx9CKWnRiZ58PUiBrqTuObRM_LmAYlmmAQuqlqIutaPp2jiRxHmhN_8DZ-lr6mVLSLV-18IilpniK9cOPZC2GzuV2MykgiMCFys9_jDM3qpKGnle8NL2uRSsj87hjWw6XtBMK8eXjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
شهریار مغانلو و دانیال‌ اسماعیلی‌فر:
🔹
چند روز پیش بیرون بودیم رفتیم یچیزی بخریم، یه نفر دیگه هم اونجا بود و خواست خرید انجام بده و پولش نرسید و رفت؛ بنده‌خدا اینقدر عزت‌نفس داشت نموند که ما واسش حساب کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107531" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=JtxG3bOPneJFIUKFNYWYLJIhUI4rPFSK7CWT6xlUK9zAonMGxr1jyV8uB20R1tzzBmTzcUTvO4vdfp5YRK2Y-i0At_J0jEb7ibR5a6lNjevjYtYDVUIZXJ7bsQVkGCnCOtQVPhe36QnUznF6hwaoqAeGwpdz0qsMd8U0d8uu5_tl4agNdacc6aZhRs1EsiVThw5bz615NfKqDrps3RQhVyH6G6iaX0aBvHAY4L_4tRpAnkLcmY0F1FZoZmcljzAa59J-l0ms073vCTGG4Cqn9ghBXP90fwiLdlxpNBAoGXsc6IJNL8PFxpL7330aozQlJkO4SQIxza6lO7KGrvkwww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=JtxG3bOPneJFIUKFNYWYLJIhUI4rPFSK7CWT6xlUK9zAonMGxr1jyV8uB20R1tzzBmTzcUTvO4vdfp5YRK2Y-i0At_J0jEb7ibR5a6lNjevjYtYDVUIZXJ7bsQVkGCnCOtQVPhe36QnUznF6hwaoqAeGwpdz0qsMd8U0d8uu5_tl4agNdacc6aZhRs1EsiVThw5bz615NfKqDrps3RQhVyH6G6iaX0aBvHAY4L_4tRpAnkLcmY0F1FZoZmcljzAa59J-l0ms073vCTGG4Cqn9ghBXP90fwiLdlxpNBAoGXsc6IJNL8PFxpL7330aozQlJkO4SQIxza6lO7KGrvkwww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
میثاقی: سردار تو وضعیت سربازیت چطوره؟ معافیت تحصیلی داری؟
‼️
سردار آزمون: نمیدونم ولی میدونم دکترای فیزیولوژی ندارم، اصلا چرا باید بتو جواب بدم به نظام وظیفه جواب میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107530" target="_blank">📅 09:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=d7WAqO4ufrljVdOO5JW1jznvNUK_0_xaLQlZlgWhh4FL6Juq2I_GA6lMfd3aAuM5V8P79K1S2DY_8zwV6cIinHI1qOLUTHLmR_2VUPXJvqksho3Ym-JrXL8RW4CaDx_xbgcIiQXTm8gABW3pZOE_RWOtT4pP9fwZfItVKGN5qLhAR9TXlDd1Ja_7QNA9Yco-oejHGUieusAESvWorJn4PE06LV4BmMTmMktSrfdD7g5pf3IcNCYLlkczopCFkiLoykG1EeT5u3NSRvhfb0Opt6hrGi9v1turBJgpNxeuoqGN-cFYbNAq_ZCPEQmdcVYI-KiJlleANn22IfK8JhqvlTozVJudLRPd_GvUA5ZrYcgj8o1rmSDSzyJ4PxUhBjpy6HBT2TolmRIkNcmQiyppJQ-ajWAqnCY0TgF7Cn1cma6VmdtbuNkcW5Z7tSRxv3SZkBUqyTsj0jtDR0N04R-3uCONae-yYblpceHqH6FVxNoREl_F9JcuQbG_gz-9Ssx-lxNCuYzY6HRhdVHV_-ajZLkuVNSm1kWIevor2lkjFBi2NWfmL42CXmD6k9vu0d4ymU08tDclKNWJesMSkqzwNHLhDvIG4Gm82jdeqUXiT_YUo9OC3UtGBfLgaKmIfJDHC5WGW6Aba_RHFxIzyzipzzAKQluwjOQ6NXSGtcu9_Y4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=d7WAqO4ufrljVdOO5JW1jznvNUK_0_xaLQlZlgWhh4FL6Juq2I_GA6lMfd3aAuM5V8P79K1S2DY_8zwV6cIinHI1qOLUTHLmR_2VUPXJvqksho3Ym-JrXL8RW4CaDx_xbgcIiQXTm8gABW3pZOE_RWOtT4pP9fwZfItVKGN5qLhAR9TXlDd1Ja_7QNA9Yco-oejHGUieusAESvWorJn4PE06LV4BmMTmMktSrfdD7g5pf3IcNCYLlkczopCFkiLoykG1EeT5u3NSRvhfb0Opt6hrGi9v1turBJgpNxeuoqGN-cFYbNAq_ZCPEQmdcVYI-KiJlleANn22IfK8JhqvlTozVJudLRPd_GvUA5ZrYcgj8o1rmSDSzyJ4PxUhBjpy6HBT2TolmRIkNcmQiyppJQ-ajWAqnCY0TgF7Cn1cma6VmdtbuNkcW5Z7tSRxv3SZkBUqyTsj0jtDR0N04R-3uCONae-yYblpceHqH6FVxNoREl_F9JcuQbG_gz-9Ssx-lxNCuYzY6HRhdVHV_-ajZLkuVNSm1kWIevor2lkjFBi2NWfmL42CXmD6k9vu0d4ymU08tDclKNWJesMSkqzwNHLhDvIG4Gm82jdeqUXiT_YUo9OC3UtGBfLgaKmIfJDHC5WGW6Aba_RHFxIzyzipzzAKQluwjOQ6NXSGtcu9_Y4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇫🇷
آنالیز تیم‌ملی فرانسه تحت‌هدایت زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107529" target="_blank">📅 09:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107528" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107527" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=rE-6M3pOyMuVk3mpYSjkrvKCCWwRvCBHSIWPwB4mO8ZKDK2VFsvr84IJJVsYU1xvByGPwJh6hrBdxludEm_H_XEwDEZMXhSXe6gF4RsRIhV74ZZrh75NH3EXmkL7vb399pWDjOMXlNytMVehD2IvC_rW9GKIP93axPama-2qr7myLdC3o5ZQO0JTg1bcWRXH_Kzmf_nu6-cyGmsRNvjS1f3IbTd2Cj65wnHMKuDZyRIAS0DG61NDWvV0hHHOXJEjbE46lDdu62GBs_DvCDNdI4oMPv80WE_5uZmH3AP6vqRpGp0M4-0pTGxzSxRRkCrFpZVRMVMJ6yN72E7NNXxVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=rE-6M3pOyMuVk3mpYSjkrvKCCWwRvCBHSIWPwB4mO8ZKDK2VFsvr84IJJVsYU1xvByGPwJh6hrBdxludEm_H_XEwDEZMXhSXe6gF4RsRIhV74ZZrh75NH3EXmkL7vb399pWDjOMXlNytMVehD2IvC_rW9GKIP93axPama-2qr7myLdC3o5ZQO0JTg1bcWRXH_Kzmf_nu6-cyGmsRNvjS1f3IbTd2Cj65wnHMKuDZyRIAS0DG61NDWvV0hHHOXJEjbE46lDdu62GBs_DvCDNdI4oMPv80WE_5uZmH3AP6vqRpGp0M4-0pTGxzSxRRkCrFpZVRMVMJ6yN72E7NNXxVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
کنایه‌های سنگین ژوله به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107526" target="_blank">📅 00:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107525">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkZvkmDahTTymogdUb52ltxFr6BZin_eBca5md5d3k1ZK8936r64o-a5jYE-KqHw173SgRItO72OskrNam6bE_ROmGgHId_mXDPt5b3dxWJqeERNTuvg4FZgQw7vVrlWoBh6H8tLzHFr0t6hi8PfwSg8tAIXYCUcm4c-Sf-WEaZWLp8N_sPxS09XsD17PKm0sF3VUUfJxKEBZkFyxZkRdsJCQ2OjMEss2ix7Y1xgtjgyV0CqSj2c2I4fgSE4XI6dl2cOlAoOxM4EVok8sAe3zuPt0vkRFcKqr6adOE27Xy0x9DIqM_GVQc_01MyjppqCxM81LgvId20GGrIXrjiasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعتراض میثاقی به باخت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107525" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107524">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ5lfafpaahNnu9tOcvHoH4W1gXunQPhRboU9DJ7cDqBSszqsKwpEnHMF5Uj-p1eTsMY8o0dr1YQHgdlJ-jGFmlYrVfK9l52QfJ946W1qEAri6UvNCWVST1dKuvHmLlaFDsExdvtI9TnfTuAFeviNMqZTj168o1GC3CwO7yExvaUJ7aiEPMeErgKQkK_Nfa5DF-GGMcRdNORHLU2vsOcoebSCy0ELQWR8WRofrqw17IB33oPVmFBZNotFjJNYzLjQl0TLKpv6DDzGPSyiizeeggmX7eHiMfuwwkNh3KG41cGR6X3S4TNtm8KXgHQycR9Pmao9p4xEsSZZW9rMh9m8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
پایان بازی؛
🇪🇸
اسپانیا ۴ - ۱ کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107524" target="_blank">📅 00:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107523">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=mvRUWNbINiIWz0xoUu6EuwNthb0BbDj2AxrauHKViQhi3FEMR8eMOxUEHogWQU2fBDS7CqK09YN80DzNRD7uif_m1OKw4Gb7AYToZ-3D44GQG2K8fvmqFxMT2HdOPgbGUG6VCfZuEZ-5Wc_dB4sV7ROwagRswBZLOODDtWOzkYW7oggm9pN0RwkEj7ONzR6uiKFr2rN8cx6pk9usCN_TFii9-IfX3_5WEfQBfR2TIyLnxPVIQw66mGgMbAysPEnIpg2pQ90HD0s5I6BB4sVP1Rw6iaaXHNkHrRFiIY_oT9oVTHnrglWL2rQ6nCfwvngVh0aLzUoj3LWE2ikCXziXXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=mvRUWNbINiIWz0xoUu6EuwNthb0BbDj2AxrauHKViQhi3FEMR8eMOxUEHogWQU2fBDS7CqK09YN80DzNRD7uif_m1OKw4Gb7AYToZ-3D44GQG2K8fvmqFxMT2HdOPgbGUG6VCfZuEZ-5Wc_dB4sV7ROwagRswBZLOODDtWOzkYW7oggm9pN0RwkEj7ONzR6uiKFr2rN8cx6pk9usCN_TFii9-IfX3_5WEfQBfR2TIyLnxPVIQw66mGgMbAysPEnIpg2pQ90HD0s5I6BB4sVP1Rw6iaaXHNkHrRFiIY_oT9oVTHnrglWL2rQ6nCfwvngVh0aLzUoj3LWE2ikCXziXXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107523" target="_blank">📅 23:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107522">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگگل سوم اسپانیا به کرواسی بازم یامال
😐
🔥</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107522" target="_blank">📅 23:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107521">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=jjtRr9oV0QlQVF3M69w2Tli5oXv-PMOf-5uzRk3WjVc0S8xv0Slnh7ZT8rw_f7CLASvK8etihCm6g8cFRxbyo2TAykJ4yYzhckaxFeE-Qym5qD64RCpInLVHvUWA9E5M0634Mkkr8R6kNbecNIoglqB4taZHyj00D-L7CHrhW825U8_5DLzKS7FYnpg0GX_A7IRrW6PuksYN0TSgilqZd_C_AXn_dIKdtm2sy4TuSgwNxKGxdIJ7cfT6v2Yi6SeraoZ-aVDlHwiS1RZSmTnQuDkxdijdF-H2BiCkRAzZqqPQgmKUJou85bq3xcRYtOfcljgnrlWevJ4ATUVtLilNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=jjtRr9oV0QlQVF3M69w2Tli5oXv-PMOf-5uzRk3WjVc0S8xv0Slnh7ZT8rw_f7CLASvK8etihCm6g8cFRxbyo2TAykJ4yYzhckaxFeE-Qym5qD64RCpInLVHvUWA9E5M0634Mkkr8R6kNbecNIoglqB4taZHyj00D-L7CHrhW825U8_5DLzKS7FYnpg0GX_A7IRrW6PuksYN0TSgilqZd_C_AXn_dIKdtm2sy4TuSgwNxKGxdIJ7cfT6v2Yi6SeraoZ-aVDlHwiS1RZSmTnQuDkxdijdF-H2BiCkRAzZqqPQgmKUJou85bq3xcRYtOfcljgnrlWevJ4ATUVtLilNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
قلعه‌نویی بعد از باخت به روسیه: از برخی بازیکنان در اردوهای بعدی استفاده نمی‌کنیم
ای کاش از خودت هم در اردوهای بعدی استفاده نمی‌شد، آقای قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107521" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107520">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: دو بازی اخیر ایران بسیار مفید بود و توانستیم پلن‌های تاکتیکی خود را به نحو احسن اجرا کنیم. انشالله در جام ملت‌ها دل مردم عزیز ایران را شاد خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107520" target="_blank">📅 23:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=gOyq1NUc9Cj3uV1p6y1dhXI8Ir9Bo3kwBBnor8o1GWyDuwxZ6xMdEYN3pe7XJd-Ed_wN5Z3ZNnW32XzE-VgPrfRYVjwXZhkOo2myb85JalmhiGIwczm6_6r1585X5eOsDlFxulbs9Jfj2f_oKFkNIOIQXXJmScvVStrJ5jc3wGnjZh7JVxRcDNWkeYdpmvoSZrZbpcEx4vjo9t6_c9mI-l1vdyvbVhOYTeNetmIfqpXd7feGxOIh86H_GhWn5bIXXbO5BAma0DBkcHkm9WnXgoP57ez1TlTw5L60E4V41Oqi4-cvkx3gWxv_8jWDaIXZ63DnLWS5d8NyAqixNeyCMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=gOyq1NUc9Cj3uV1p6y1dhXI8Ir9Bo3kwBBnor8o1GWyDuwxZ6xMdEYN3pe7XJd-Ed_wN5Z3ZNnW32XzE-VgPrfRYVjwXZhkOo2myb85JalmhiGIwczm6_6r1585X5eOsDlFxulbs9Jfj2f_oKFkNIOIQXXJmScvVStrJ5jc3wGnjZh7JVxRcDNWkeYdpmvoSZrZbpcEx4vjo9t6_c9mI-l1vdyvbVhOYTeNetmIfqpXd7feGxOIh86H_GhWn5bIXXbO5BAma0DBkcHkm9WnXgoP57ez1TlTw5L60E4V41Oqi4-cvkx3gWxv_8jWDaIXZ63DnLWS5d8NyAqixNeyCMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پاس‌گل لامین‌یامال روی گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107519" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=PRYzid-i71nUBZLi2DEDTiyxrf38YsLxy_J3Aaual-ijGp7FhAoAm7PpjhpHyBMj1mmLyQQCZPFfmrWO8Q5hiZx-cU3WwBMGsBGFQe1_4qM8Py7w8bKWtuOONmhlg2OsawISBD6en01mc4XNFC1HXkhWu4VDGH1BqXvoSCW6g0GXfVz1eSXAZIkULS2bnIuR_cnUYN6c9pmr8APsC1Ctb8WG3vVk1cw9_0yl1rU1lqx893Q--hAEhyMc0Wy_x312bfVFKmLUHc8RB9nCDhzK5DI8xY6x0ShEx1ahNTgIhyp45QMh8qlpfpfjO4olgWiyclS96LFVO8seg5XIPu4jPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=PRYzid-i71nUBZLi2DEDTiyxrf38YsLxy_J3Aaual-ijGp7FhAoAm7PpjhpHyBMj1mmLyQQCZPFfmrWO8Q5hiZx-cU3WwBMGsBGFQe1_4qM8Py7w8bKWtuOONmhlg2OsawISBD6en01mc4XNFC1HXkhWu4VDGH1BqXvoSCW6g0GXfVz1eSXAZIkULS2bnIuR_cnUYN6c9pmr8APsC1Ctb8WG3vVk1cw9_0yl1rU1lqx893Q--hAEhyMc0Wy_x312bfVFKmLUHc8RB9nCDhzK5DI8xY6x0ShEx1ahNTgIhyp45QMh8qlpfpfjO4olgWiyclS96LFVO8seg5XIPu4jPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107518" target="_blank">📅 22:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگگلگلگلگ یامال بازم گل زد برا اسپانیا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107517" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107516">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f859d863.mp4?token=Im1zD63Yp0wGgzlL8oM4rooRoBQTYrZcCCqQ1YCY4PxrVSDpvKgIyzFUAsUHM3K383iu1y-joMgFWyxTRpw9O3DnhdLcGPO7UpKGevIOENvCsvuKZr7nS38796dv2qGQXsWVZPCvPGmle9YsqjSAE3NaSZ82edi7ovnVCl4lkmklPl5t8j8-N13NC617jMlgh_jUgwdyC4owSXw1tz3Vm0dFYmAyv2WxVr9XaQekPXzbJOIUVufNsZQNr5dnTMA9GVT7Cs0HYp-RS1rM_g52wm7pVw0jK877891ns1VJmBplZmcZZnmYIwLQr4DrtaqwVdgFFhDDLldOLRWjkMFrtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f859d863.mp4?token=Im1zD63Yp0wGgzlL8oM4rooRoBQTYrZcCCqQ1YCY4PxrVSDpvKgIyzFUAsUHM3K383iu1y-joMgFWyxTRpw9O3DnhdLcGPO7UpKGevIOENvCsvuKZr7nS38796dv2qGQXsWVZPCvPGmle9YsqjSAE3NaSZ82edi7ovnVCl4lkmklPl5t8j8-N13NC617jMlgh_jUgwdyC4owSXw1tz3Vm0dFYmAyv2WxVr9XaQekPXzbJOIUVufNsZQNr5dnTMA9GVT7Cs0HYp-RS1rM_g52wm7pVw0jK877891ns1VJmBplZmcZZnmYIwLQr4DrtaqwVdgFFhDDLldOLRWjkMFrtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دیس ابوطالب به فان 360 فردوسی‌پور: فان واقعی اینجاست و هیچ شعبه‌دیگری نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/107516" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107515">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdOz4T2nmmBclPOu2Exln169kYZR3CoZjxVT1q6wbJxXxzL-_kzTDNYJXRP9xA0Z5xtLBFwJJrTlXncjrvKE8hzNIj8zSzLTlvSovbXt98OhF7SqjisIpIGCzHObaEa1os_cWPpsE0AVyjyMXivUNJ9J9z8bSFRi7UxXCBgEpG0I3j29LQn5pVZxcerABSizgunCS8U1fUcH8P-h7s8zFaqM_vNxU49oflhR7OMfdLihOl8i26eR_a2dnHETK8J7_dJ5z5bOZgdttl_2gCp3qwJJbr9N3SIQSM5NPEttCELXFXMcyCItmMdOIIFxK9UlJIMCKhtplRShRcM-y2vEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان بازی؛ روسیه 2 - 0 تیم امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/107515" target="_blank">📅 21:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
پنالتی برای روسیه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/107514" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn12bK1-59k-pxR7A5rjiyIkeuT-hsfm-9NT7YimFDeYx3E54DdWq6q8BrBFeSST8Mq9rAItIA3bu1nAKSs1Nq8uo0ICLdCLs0l-tSFyhzhcSWugidf9G6hBZ5Dr9P4I9Zj8R4O9n7Ae1jZacV4uyIjkyxi4vlGzyV2Fj5TbSo0mV5-J-u3OJs30GHemMxdDhoj61EXYmMosDtgQQSDZSqrOJqxbGjozJISiiDNfWu7Z0cMGteP9khDc-Idin26uLM_Z2UuGLeopzpRv17RGq_ajoJ_AxTZ51xKWTR4FFOPVLa8I6C-rlFFWziQyGGLyWv_bGP0sL7rGLf4L1AnMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
وضعیت پات چطوره؟ ران پای راستت خوبه؟ همه‌چیز مرتبه؟
🚨
🚨
رافینیا: «خوبه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/107513" target="_blank">📅 21:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=iaMt5PaMO7dAraz9EdTdh7Mnd1zzbxNSjrhZJFzJmX80nFlDd8I8XgEuDLU8Xg4389l7iUFQqbHTIeN4hB9XW0avsIUg1Zp33OND3uIqHGNPDSHfzPQYZWVd5cZDXVNWNhhXcVODEqHjHI3Ynl5WiqOmsjCGUtblXa48PGRvFZtHcD5xpDAfiD_l0NvK4f81QznOSD_Xo8KugnLuyRxUhqcI0D9Vk4rWDINKHyH0mnvZdOetKAmI_wr4XUycjkHKk30Mb4pRRg1eg4QvrfdvJo5CJLzxnjFShlpW6GwUJr87KJUpVyWlvqyaaDI-6D3R1P0BV05gqXm3dNozNCgwdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=iaMt5PaMO7dAraz9EdTdh7Mnd1zzbxNSjrhZJFzJmX80nFlDd8I8XgEuDLU8Xg4389l7iUFQqbHTIeN4hB9XW0avsIUg1Zp33OND3uIqHGNPDSHfzPQYZWVd5cZDXVNWNhhXcVODEqHjHI3Ynl5WiqOmsjCGUtblXa48PGRvFZtHcD5xpDAfiD_l0NvK4f81QznOSD_Xo8KugnLuyRxUhqcI0D9Vk4rWDINKHyH0mnvZdOetKAmI_wr4XUycjkHKk30Mb4pRRg1eg4QvrfdvJo5CJLzxnjFShlpW6GwUJr87KJUpVyWlvqyaaDI-6D3R1P0BV05gqXm3dNozNCgwdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
‼️
چهره درهم قلعه نویی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107512" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULF8pOl1KMz66Ju8XAIDUBezGdgu4SBb4xpzE_Iux5R0zF0bOuYQpp0fRLVWUzvxYWDt8ZCZaeOFRiMa55sH8u4vvxqzImmH3repT4V-kZNqJSqtzORW9qVNbfkOWmmzxxos2Jam0zd6EH84xGFxPYCX6KLwLttYTSMPSaH7EqgHG9ZD9XAavDYIuLRxR93D-Qaam3EYDfpbfeg77jtkv1eBobyJ6fGUPkW-PRSvwVV5nW7qVl70kYPw33m2Jp0Eax36V5ZI4fKt1Icx0g1bGqsTX4sUU97cfiIhf8tX-RQcbCw3maQo7rln2uXHnL3jXkvY6U264ym8tTCKHKh7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
اعلام ترکیب تیم‌ملی اسپانیا مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107511" target="_blank">📅 20:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clE5ARlxrvgsbyk5ICHxJ9sTeDtXlhzTJ6CjQItnGay-8A_v4ow4tdz49PwQ9SvigEczJ9SLOV8ia64SFuyK2pBIe6TGnhl8G76njCEpV2FA8OjTL6_-SW8IE6Bglxr3zUTZwMMGdSJhgaWxM3fVcRuvaIBV28s3malr_bOaprIuuXz1ud-KK5QztyqR5EsvX2UV1n8p-_9DBUZCoUp-GaCMHm7QYVIdczThtEEfZS_BL7bsbSqSaxXAHDhOU0DpAAHYd9oKOj8gqIIQ4t3gMNdjDT9gkTO25nvvV4Iz8alvfKfyUT2eNPvfJPlTvw7oTwxFOMTXTL0y4_lf2iSnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران حالا بهتر درک‌ میکنه که این‌ مرد چه نعمتی برای بازیکنان داخلی و لژیونر بود و فوتبال ایران رو از حالت کیری الان نجات داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107510" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
