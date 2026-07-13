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
<img src="https://cdn4.telesco.pe/file/IiwktjHCndONpWMQmVILs3yArRzo5kcY5jRWi9tZXtuIiWKdvPtwsbbjHhpz1yNQ9TfdvH_zGZlT1-kECSoX2mHVQJkFbfVsA-QgiNQCKbJovCWiqCzhnU682-710FkBaLeItKLj6Q-eKd0-cDART6ryllTXGBkauIJQqsxytB5G8ak2XVfT_MsQ4_o_07SBmyYsIVO4HwwOf0tFHg9jIq9FVZ7vPuGrV4gZwwrv1P7DkRSQGim36w55DBiW1aS0hvBJI8mj0bmPSppEhRUneW7ao1uyQHWaRyHkDRnXSu7GK8_4zDtsqullixtph6BMbSJKCDiS0WaoATp4Shxbow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 177K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 11:40:09</div>
<hr>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=kG3kMyx8DoyTWCW7jB6_Fr11UM-WkcL1Y-s3I47lrmDQCowMfmjuBOVdv_IijvQYNYJahU-cmbHmNB8zMGwP3wCavZft5-Pzau_86BnxerGKcpnmm0uSHRPFjXTKbDZyqrIGhQcygbuU0IpKgd1NSi_2uOozkgHkfPAro4iWmLatY0gB-SpqMo9j6xFXkDtZXwx4xwtSBAZ_z540dAhkCCFS7nERO_52UMciNZQ2UpIuYCwLsqXEGK7msw7QuYgB9o_bfSJzsIVwD5U8jeOGclnc-YqowoHz1nwsQ-UlHOjVQxP_AssbBv8xeZYt91qLYffP3N09m1gL_Os6N7V5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=kG3kMyx8DoyTWCW7jB6_Fr11UM-WkcL1Y-s3I47lrmDQCowMfmjuBOVdv_IijvQYNYJahU-cmbHmNB8zMGwP3wCavZft5-Pzau_86BnxerGKcpnmm0uSHRPFjXTKbDZyqrIGhQcygbuU0IpKgd1NSi_2uOozkgHkfPAro4iWmLatY0gB-SpqMo9j6xFXkDtZXwx4xwtSBAZ_z540dAhkCCFS7nERO_52UMciNZQ2UpIuYCwLsqXEGK7msw7QuYgB9o_bfSJzsIVwD5U8jeOGclnc-YqowoHz1nwsQ-UlHOjVQxP_AssbBv8xeZYt91qLYffP3N09m1gL_Os6N7V5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای آمریکایی با استفاده از مهمات سنگرشکن، یک تأسیسات موشکی زیرزمینی در پایگاه چهارم شکاری تاکتیکی ایران در نزدیکی دزفول را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgUtZu77c33mr6hYVjs45HDMe3Joeh_ftkGpEbgUDMZHWmKnZ9Q1Z_9ywUfk5kRtLHOzXNmi9MrzCnAhGW5WweXgVlWWwGRC9XIx5wXP4ujtciC40JGWKDRxx7LvIjwv4d6F59MukGFsUR5klWFPLHHDqpOHyAsSEuZguk8umhogGfgCmI8QYjgPMb9oa1N4BYhz4vjLBt01-vB98bDI1F26ikoZPPS8D7mmUfWC6Mec6mtaQdFI9rYJtV7pTdRnX8c3zeXU02y32g71hX4VbXFTE0g1kmZ-Zd2PnO8otZ7Y8N42ocw-95Z9XcDag2UkaibTdJ-WcuNhC5ZRhKc1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ در تروث سوشال تصویری از لیندسی گراهام منتشر کرده با کلاه معروف:
Make Iran Great Again
ایران را دوباره با عظمت کن.
@News_Hut</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/news_hut/67982" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAQFv2J4l3BsbjxgbIxiVuGc23GlgoL_6t45ifoFVJ2KFbDB2ppUZlgTYCHZN44pr80JEdZuUQcwE1kTmFLXpAIzYT_bjekJ_ElFKmbO254JzrG076uP3qmRN9-r-nmOmCQTpx36tdv8u4SyPu0HHXUlPt1e2Blq_hrE4ZvEB8bcLN_Wy8LJUtXFmpr9W6cI9ioSzWTm33AQhlZ8BK2ChyTDlaAXijKZWyseCeTDAcfgfIhmCxLWe99Ig315O-Y6_vrAGw6_9cJkXCvOvE4k7-jOfcEZ0h5oS0CSO6r4Ce0aPRv17g3c9bRB9sXUhRT646LCJQt4ygAC8_QN5gGpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5R2HjAuMZbHy2_OqjcvmrX0hSpZUIlCVeE5IDanSdMYPqHnbsunK-ipGyeHo1tvDXjwgBk-VjeUOyOoXAwW4dfNZMSKiKo9IORstma8n6pZtOsVm6l2Gl_wfmtd4F9qXa2HwR6jjd5Fq-Sg7-hauhRv2RJMuM08KKnZQuJKlKBS8eZzc7Lb9SWKU5QZ2Hp7msfaLZafRStI_RckwpQuAWp0GvknCHnOTzs6H-uyykWLmVBqSnyB-tA3YAJB8kkaJG2I7I6pb5D8DGHFatsAmneGQEWPSgQMgd-erbzSdt8Sba3I2HSRmHYC0-3us1SDIlvOtQ7cNLNh8D5jWOESQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
انهدام پهپاد انتحاری لوکاس آمریکایی توسط پدافند رژیم در بندرعباس.
آمریکا در بامداد امروز برخی مواضع نظامی جمهوری اسلامی را با پهپاد لوکاس هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67980" target="_blank">📅 10:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddd337574.mp4?token=IwC_qqZALDbXZK-piKZA7-ihDV4rovCtaSHN_fE-MSgRyjT6ihsNNuqYKJXEngqQA_6IZsyDU0_4JpbDYLExu3iwkEWiPaFFrGugH7GvPPVC1kafiQ4XWTtfj0wlmbnmoYJ8Fnz0UIVRR_DguF7exILyRlfNi5u2kca656WlFQEi6MBkvIV4MTXMNa0jtGkwsw_MR2XkpU375oY0fYP3HMpkvhEW9j6F-J7dW3LLAbeBk7q31yJKmMthsBO_uLhPwvZgK8_wM9dQoDwSXet_Q-Gn3x-VidMDokMysoyt7TPmNUPpYuRdhed4htLqNw7xP4sFSU2vqwsPVfBKO6rDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddd337574.mp4?token=IwC_qqZALDbXZK-piKZA7-ihDV4rovCtaSHN_fE-MSgRyjT6ihsNNuqYKJXEngqQA_6IZsyDU0_4JpbDYLExu3iwkEWiPaFFrGugH7GvPPVC1kafiQ4XWTtfj0wlmbnmoYJ8Fnz0UIVRR_DguF7exILyRlfNi5u2kca656WlFQEi6MBkvIV4MTXMNa0jtGkwsw_MR2XkpU375oY0fYP3HMpkvhEW9j6F-J7dW3LLAbeBk7q31yJKmMthsBO_uLhPwvZgK8_wM9dQoDwSXet_Q-Gn3x-VidMDokMysoyt7TPmNUPpYuRdhed4htLqNw7xP4sFSU2vqwsPVfBKO6rDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید شاه
👑
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67979" target="_blank">📅 10:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ZfRqTxktr8AKFpOVZzg1q7oKtY-GwQeD6wmH803Qb1Gx4V1_CGT217L73EWnvRHSmQ3nvcdVO-IlJfKcOcK8QNvvcDC7xkbT3aASavT1KFIdXjz2GQqPY0noSlCt0FAPWdF_5zfVtWiKe7wPnIqVjqUGDYVYvV-AVCjPClosjETyOzCBy2nS2q-zdzfdnRilkizVn5c2zhCMoKBPABMGysemnKJ-HbU1VDWxunJS4GXD5F1qY3_pMk7oyxGinYD3WamNohLncrnRgLFn62i4bnT5X-NjaDMAzzIvUxfbZcSstq5GrAP5piF1JvaQ4VWtIjeshnclvyu882PrWYP_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ZfRqTxktr8AKFpOVZzg1q7oKtY-GwQeD6wmH803Qb1Gx4V1_CGT217L73EWnvRHSmQ3nvcdVO-IlJfKcOcK8QNvvcDC7xkbT3aASavT1KFIdXjz2GQqPY0noSlCt0FAPWdF_5zfVtWiKe7wPnIqVjqUGDYVYvV-AVCjPClosjETyOzCBy2nS2q-zdzfdnRilkizVn5c2zhCMoKBPABMGysemnKJ-HbU1VDWxunJS4GXD5F1qY3_pMk7oyxGinYD3WamNohLncrnRgLFn62i4bnT5X-NjaDMAzzIvUxfbZcSstq5GrAP5piF1JvaQ4VWtIjeshnclvyu882PrWYP_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستتو اینجوری کن
🫴🏻
لباتو لوله
😢
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67978" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=E6r9iERejzQZSmx1DOHqnFcDLe7j2tyWBYsbv54amW2x6io5Dn_AQNrxASn5t-5qPVA1TDb7AyS31SIPO6ai5zecFC3hwo1wWe7NqW5YlJZ1tqJ-lDVPUHkiHzUIvpdaScv5FhvOX-vgi-fPHMJTdM3eRmxRjRz9wiS0gUJZmB5qIti2tOabGTmaNmKGL3S6Y5BWeCNlm7GIP8eAh6j7g-lod8VRDMkw35ALIjqLSWHPX9zLxk2uGTurl2qKH0YOAaDo7hoA7OIdxNCQv37omesNcHBCf9H6iUxSJxcI8OY21BcHZnt8PlJqhruZ88qGiNnAulBxstzpLoRdPCTGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=E6r9iERejzQZSmx1DOHqnFcDLe7j2tyWBYsbv54amW2x6io5Dn_AQNrxASn5t-5qPVA1TDb7AyS31SIPO6ai5zecFC3hwo1wWe7NqW5YlJZ1tqJ-lDVPUHkiHzUIvpdaScv5FhvOX-vgi-fPHMJTdM3eRmxRjRz9wiS0gUJZmB5qIti2tOabGTmaNmKGL3S6Y5BWeCNlm7GIP8eAh6j7g-lod8VRDMkw35ALIjqLSWHPX9zLxk2uGTurl2qKH0YOAaDo7hoA7OIdxNCQv37omesNcHBCf9H6iUxSJxcI8OY21BcHZnt8PlJqhruZ88qGiNnAulBxstzpLoRdPCTGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پهپادهای شاهد سپاه درحال حرکت به سوی پایگاه‌های آمریکایی در حوزه خلیج‌فارس
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67977" target="_blank">📅 08:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی  @News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67976" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67975" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67974" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIGRzh-ulHO6eaC8M-O25hSdO7eJh7zR2Rhu1R-iZjrBRxbgfm-pWvpQQAZ1cqDz3P3mOE4mGUtKSHgbm15d6ei7CyD7SO-WNSCKD3U8VkV9D2fGTFYpZTBZ0COFKnj8t4BGosSETzNa48jZnFCSKDoWn6_tATNjTE3aHuoiIXaNpfncDe2CMqUI9Mx1gJ1NdvPBzBITqtd8gzFOtLk6CSTHcRIc7EU2OncRbmgfQ3NzK1fn_rj4S9yldAHxMlnBrv1_j3zKpI7FMFMvA5CgaMEzmyAfeoL_h7NCnipclSEMbphyHiFFjuSYA6ffrZvxMhXDjIDG6KH8GhuPojvDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67973" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به اهواز بعد از حملات ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67972" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
نیویورک تایمز:
مقام آمریکایی گفت که انتظار دارد موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در یکشنبه شب (به‌وقت آمریکا) نسبت به حملات اوایل همان روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67971" target="_blank">📅 02:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67970">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فارس:
دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67970" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
دزفول رو چندین بار سنگین زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67969" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67968" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=dSOgpiTrErMNVX4TAfxpHPep2UWuy5s2zgPV_PIP9oF33JUMxxMVW9zbhQPIZ1ZUyJrqiHAaxJwOJO-zk5eyIgFpLFwJAjQgK7aQc73jYnFlwsOq0xTAs5dMg1XogDNGHDe3ylIsM_xyiL9O-YI0Dzqmx9xTepXf1y3dkQfbc5uy8LqDIU-nldTeinFMkKiSu2HaThsXBDPnSknMirDgFy561wIe3vFUQE1RW-6aqhVmcp4GlimxueBPf6e0ZAU1qAhmxL8NKTFsAltO7bHT7LsHSn1mg1XvNlG_97xIIFegoZN1NF_mUxEGzZAJQ52mAHqrTPRhEXjfVCMdpaLyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=dSOgpiTrErMNVX4TAfxpHPep2UWuy5s2zgPV_PIP9oF33JUMxxMVW9zbhQPIZ1ZUyJrqiHAaxJwOJO-zk5eyIgFpLFwJAjQgK7aQc73jYnFlwsOq0xTAs5dMg1XogDNGHDe3ylIsM_xyiL9O-YI0Dzqmx9xTepXf1y3dkQfbc5uy8LqDIU-nldTeinFMkKiSu2HaThsXBDPnSknMirDgFy561wIe3vFUQE1RW-6aqhVmcp4GlimxueBPf6e0ZAU1qAhmxL8NKTFsAltO7bHT7LsHSn1mg1XvNlG_97xIIFegoZN1NF_mUxEGzZAJQ52mAHqrTPRhEXjfVCMdpaLyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال شدن پدافند در کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67967" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=jQNdc05gv8wVSZiHdH3Xh2cZ9CYotcVX58AQ_piM7HyTOC0I4pIxm4nmDkIIkrRwgHxFoPtKoKuRAUCUCxcNxaEtHnbvG-AbwQ_KRicYFDOgZarzcPMPPoAniO4Cm-XQYCwq9jrQMDRG7-xWzyeyrOW3zBGgTR5sxQ0W6V1QPkM0KqGk744qU1txTGh1zw984W13Sd55XMY6iLn3T_roIX212EE_hFmREhw18HxhRIfdfQQRKAhplXXFCw386ShybEKj3whvfz6cOeKAnz1-Y8YrVXSET_Dkj2OhshrM5ZC3C-GVMvAAjUttF8hiHLJKqrsZWuxvs4pn_qGEO0Osag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=jQNdc05gv8wVSZiHdH3Xh2cZ9CYotcVX58AQ_piM7HyTOC0I4pIxm4nmDkIIkrRwgHxFoPtKoKuRAUCUCxcNxaEtHnbvG-AbwQ_KRicYFDOgZarzcPMPPoAniO4Cm-XQYCwq9jrQMDRG7-xWzyeyrOW3zBGgTR5sxQ0W6V1QPkM0KqGk744qU1txTGh1zw984W13Sd55XMY6iLn3T_roIX212EE_hFmREhw18HxhRIfdfQQRKAhplXXFCw386ShybEKj3whvfz6cOeKAnz1-Y8YrVXSET_Dkj2OhshrM5ZC3C-GVMvAAjUttF8hiHLJKqrsZWuxvs4pn_qGEO0Osag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویری که ظاهراً پرتاب ATACMS با استفاده از HIMARS در کویت به سمت ایران را نشان می دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67966" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
حیاتی معاون استاندار خوزستان:
در ساعت یک و ۴۰ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه نقاطی در شهرستان های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67965" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
مسئولی در استان خوزستان ایران:
دو نقطه در اطراف شهر اهواز مورد حمله با موشک‌هایی قرار گرفت که توسط دشمن آمریکایی شلیک شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67964" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
مهر:
معاون استاندار مرکزی در گفتگو با مهر حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67963" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=urY3BTa5Dp83e3Hbevk2OqJH2OUk5yZjg2mDAN1q3nAdnllrNsGoJ3M-g3FTX6vZP6I3Af009rRP65liaThNvaEAMLP69_4bZYL8IBUVtEG6uZz7YZ3rw5O157XXH2i26ZFF5XIu3JA4ma-6GJ7_ph3MtWPHDGi8Vy-liq_VrQv1upBan2mqTfihV9aOG2zrDLzkS8IgDlWylIbYnOPrjM6vDXHoF_dweCw5aYhxJvTjaj9yN6vw-STN8W-RVNXcFFkbwxW-mqMSXlo1W3_68z0f95TWahnoehbOTAoZR4l3YQvn6WsD6dfNf_OWyRh3Z9INdxonu7CJrmCgXAlyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=urY3BTa5Dp83e3Hbevk2OqJH2OUk5yZjg2mDAN1q3nAdnllrNsGoJ3M-g3FTX6vZP6I3Af009rRP65liaThNvaEAMLP69_4bZYL8IBUVtEG6uZz7YZ3rw5O157XXH2i26ZFF5XIu3JA4ma-6GJ7_ph3MtWPHDGi8Vy-liq_VrQv1upBan2mqTfihV9aOG2zrDLzkS8IgDlWylIbYnOPrjM6vDXHoF_dweCw5aYhxJvTjaj9yN6vw-STN8W-RVNXcFFkbwxW-mqMSXlo1W3_68z0f95TWahnoehbOTAoZR4l3YQvn6WsD6dfNf_OWyRh3Z9INdxonu7CJrmCgXAlyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67962" target="_blank">📅 01:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=TPonUo2pOt-zeP4veRyLYA-s8q3sahoQUY2n93M8C7ey6UhwPGktcdYMnRCpZxGHHhWbOEoiu1Tm0jPFfQmGSaEI1QfTtzumpCJ1VvZxqOBKG-ZjXyMXoQIqAnJPHRnfEn8240JLvAkGeSpDoy7Y0Jzqv3s0dKSBr8saYZmu4cPelpdNljgM-w2EUOgzItYQlE2fZT33y5jQqP_sXeENxbpQgwn2F87SlqqSXGtd8RtMARvMiVRbePiyMVxImPLkNqNGu_2tqYCZb9-BqsfBk6sapZgMfuVF5mjdVLSNuN4YuAwdIA1EfNiAir-mclLHk3Ew05itsoXF01ZpW1Ka3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=TPonUo2pOt-zeP4veRyLYA-s8q3sahoQUY2n93M8C7ey6UhwPGktcdYMnRCpZxGHHhWbOEoiu1Tm0jPFfQmGSaEI1QfTtzumpCJ1VvZxqOBKG-ZjXyMXoQIqAnJPHRnfEn8240JLvAkGeSpDoy7Y0Jzqv3s0dKSBr8saYZmu4cPelpdNljgM-w2EUOgzItYQlE2fZT33y5jQqP_sXeENxbpQgwn2F87SlqqSXGtd8RtMARvMiVRbePiyMVxImPLkNqNGu_2tqYCZb9-BqsfBk6sapZgMfuVF5mjdVLSNuN4YuAwdIA1EfNiAir-mclLHk3Ew05itsoXF01ZpW1Ka3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منبع عراقی:
موشک‌های آمریکایی از کویت پرتاب شده و وارد فضای عراق می‌شوند، به سمت ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67961" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67960">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1E06meslcbtXPuEIQCOY5DBc4Vc2yqJ8WWyV6ZGHmcmIfp0dmmiAwQjciH-WS9KHKp6TxgKsJ3Z0NDY6fhAXfIRoKjHKGnlm4m-2fOnRxSAXg0iDMCOGuA1ROesWCS3Ub3uNz8j7rNU5K5eZcLdjaNxOtPAg7X5MR4WX_x32nwwXManLw02tzlslooiToO_vS-KCvrCSM_CTjU281-xVX3wTIzOaAuU6dZeidvbrLX5Y5wQKNmfmbYpKjcmXxXQ7RCS7k9ZDdm5OG1VudxhGgTl7bKKukKCqTHHaq0IKfU2a_D-r3LZB6JRB_9uv7gNtUvhqYE5Q_TvnTdI2isZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
ناخدا دوم تیم هاوکینز، سخنگوی سنت‌کام، به من می‌گوید: «در یک ساعت گذشته، نیروهای سپاه پاسداران به سوی شناورهای تجاری در حال عبور از تنگه هرمز شلیک کردند. هواپیماهای آمریکایی تاکنون موفق شده‌اند یک موشک کروز و یک پهپاد تهاجمی انتحاری ایرانی را رهگیری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67960" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
اهواز رو دارن شدید میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67959" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش های از وقوع چندین انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67958" target="_blank">📅 01:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67956">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBQyMX5RaB_fae77_Ghmv8eWF1lqj4uDqIgCNVwxyXBZ_sBxPMRTyEMkH3fzEBu48W-341vSSx9uWzf4_sDVLUgYxnCgG0HvCH2S1Plr4K0vt2rAGqCSATpIUGsj7QGpIAVEqdbfQiQOPmrkwNVjrbyTuBq8yuSM82N8hJ7PeLorTHoCrvTX_t4tYwSfZUN7AGn1-R9u4ciDkVaLMkT2PeDhDffxjXPalJYHUXTKUd3Zo2SERZ-LcmrAKZzjG3T4fN1KbCtx0jk3SF7HCYYIinaHUzvu--UzY4960Z42Cn5sLrD6C_EtVmQGwAHl2H1umY2R7bEVhECyKlTJWRC3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=jgJetr_DEHkTn-Y1QWJbl-hCeiidXRktuZjqbuMWf600GSP6aHp44ThEcU5gy043wdADci_APGy60cF6XiznN3hZZV3brhpDzocbPTRdYvt0_SamJG5dFohZK1IFqm29ogaFKPJ2NohKhK4Z1hVmtNqEjOQCUXb2VSxOSMAk6kJuUgFghda-OR62qfurUlhF1042fQSa0Ba5mkDdsJrvd7QxY-rmNheUvXJLw4HaM5xu9UDiVWk_9_z36eA29mdXxRdyHX6GxFzzNbNhJdBYIJg_3lvvi-TWvZkDEfS4LuR_fvHBzeiPrUoiSzOIWcp0SY6XiLx6iHx5C2xEizAGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=jgJetr_DEHkTn-Y1QWJbl-hCeiidXRktuZjqbuMWf600GSP6aHp44ThEcU5gy043wdADci_APGy60cF6XiznN3hZZV3brhpDzocbPTRdYvt0_SamJG5dFohZK1IFqm29ogaFKPJ2NohKhK4Z1hVmtNqEjOQCUXb2VSxOSMAk6kJuUgFghda-OR62qfurUlhF1042fQSa0Ba5mkDdsJrvd7QxY-rmNheUvXJLw4HaM5xu9UDiVWk_9_z36eA29mdXxRdyHX6GxFzzNbNhJdBYIJg_3lvvi-TWvZkDEfS4LuR_fvHBzeiPrUoiSzOIWcp0SY6XiLx6iHx5C2xEizAGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر مربوط به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67956" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67955">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBeHrAd🇦🇷</strong></div>
<div class="tg-text">توالت + دکل = برنامه طوفانی پیتِ پرس زن</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67955" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67954">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67954" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67953">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارش ها از انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67953" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67952">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo14FFNZK21Q08etXddmmRbnamQyHCPDOOw6lMqnm9ODO-TmKR-GoCZneEZgjF3WXBi2l11oBAgINw_ZrdmInIB7fHQpcd1UGeAfF-KtvKFUyPR9jv_49FKmuHgkg2AYxPB5kkXnz12Wk8CJrK29r3yI2bvPPhYb1HRY8FPs0LwrDUUJ4NhVRol_uTd7GtJAHxHxAprv8xtMqknorqbrEbQNrCb9CyeHePiui9WzF08RxfW_a7E8m8FLRE-ms8SuKcCccMLO7ztUH04MN0H8WYPdEfJzHfRi0LoHA_aHXlUvbRf2a4ny9lWlZsUGby2TRq_8dRZpJeJnFt9Mr900Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
9 سوخت‌رسان آمریکا در حال حاضر در حال پرواز در آسمان خلیج فارس هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67952" target="_blank">📅 01:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67951">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzSqz5Zavpulqvhjx0loUWnEzLzbgJhMRPt64qSyLscg3Pqsm2wJJAemcUxOMpIJ5Q9f0rgE8fo1II6mrOSNVXPIDELalVuasDXydX0Jj9FHnvPemGSBht4OI8TcGHUC3icBtdB-YcXCjyL1MT7CLps1JdtFOPssZO08y1EIsqyvr-d4qPgYp5_jFWwgjGibLFfhzhR56gSz4GG2woDhej26oyeauIburclsa4LPX4Jco1v3PnTdoTRUVahlhdEuD4VC35sMv2tPfEszejhFSKpDKpbrZNkBwJ8yWlwuwdZPTVpiVaqv7c1NffDwNKkBPBS26E3AHeDl17ZsvfC7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویر منتسب به انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67951" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67950">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivEhjiiM1al8QbMYZ8Z9ONMTdhtwXHebYifLOOwJL4-G1ZMPv-MegSBQ_P6NWRIZPe0LekpoxmYhwZ4CkhDDEAZOxKTAEg_1iBm1FCVOLtRKjjGyFE0uUfvagMKq-VH44EMQfiR90paWgqvWuPLqWQtJ4eKZNBEtJoJsYBYgT05RPv2GAM6JZ51itc04LkdiMQfyPkFOAlpiekZCt7jPywnb19uYFis6-Z_aH_YnT3g6nbAhDCBEqlgDzYw6WpWPmW4dlHc851YJZEeatb45iRZYBVzuFEpJi0-OadBEniVEUfONw3MaB7T7wrVsHvhRgAOZ7PMbIgq0cMq3T-dZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر من زود تموم می‌شه، چون:  صرفا حملات جنوب کشور هستند دلیل حمله هم حملات سپاه به کشتی هاست و این یه حمله ی انتقامیه، مثل چیزایی که دیده بودیم قبلا   یعنی در واقع حملات، کنشی نیستند و واکنشی‌اند  #hjAly‌ @News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67950" target="_blank">📅 00:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67949">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
❌
دو انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67949" target="_blank">📅 00:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67948">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67948" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67947">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raHZ7mH8lnRSbSM9TfPLmmOslGc42Eeccej2qLlt1lMVOSq-mlgmSeFks35Ja9jtsrtTrlnUDHaHl2BGzbH6CytAPOe6MOfef1tfMstO9WrTKA0rUh8P8PRErQI5LKc8QswoXjrv2jdbVs8jEx2wa3Vuy0dtDgRJQxh1jDaLizHjtOfxvRH7oMuwQAy8yh4KR_eUaMlGqMQRBj8OttKSfcvADmOUNRUBsOkijhRx8NGjPuvR8yD6IGumTGGEwWthSLx273Nm4M5Un3kd6ggbiyzQtNRVtN4iSQ0Q22KggOHNW9spCl5jKUntmE-jibgwd6SCCAhYEGtLM7kY25gxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
ساعت 5 بعد از ظهر امروز، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به توانایی خود در حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور داده است تا به نیروهای ایرانی پاسخگو باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67947" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67946">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIJLneOgg6UA56tpibJ_282NWRf5P8bZWUDfd6sFeCDGVn3q1gzlsVns1s3mSlcs7R8X3ynM_KKuJF596WH2wrs5liTZ7UqOopwIIFQFC5YcXY83_e3VqyRepBKfVTCaoC1twpnK4vSIokTRoqsaYspRJpwQMsFX1Wuoxvl0vBJkCgWeB-F719dvV5AToHSB12OxKrGMQ8xJSoDeYGtrURtjlELDGSYfYszl9j6M_QeVZ29tqPWoG5pAQ4Ldn8Pc_m-db1XwuAbPte22ykhcLRYidXf0R7cRjcQ3DAWPQ50ud00q3mHUPJ-j0GohP-BD6YytmdFem5lJAWp2APMYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67946" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67945">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇮🇷
ممد سامتینگ:
اگه نمیتونی جنوب لبنان رو امن کنی،
پس جنوب ایران رو ناامن کن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67945" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67944">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67944" target="_blank">📅 00:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67943">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
❌
گزارش های اولیه از انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67943" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67942">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67942" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=CU_MLfpIyOQPoNtF-juvZhg-maDyJyKT9OSwSPtq_AmEcCWSPTS2OyaIUNP6PYm6waxh66xScsWRwDLResUCxfOu_TS00cVnT9QTNSaatwhkvyV2GNNbXDV-2zJtjcdzOGpDEIdJMgpunisDnLIYJ1JCvhxai2XTKYAtWJwonxk03R2jqaJy7cGtYMbwcP_eoftt1AKlkDyN-U1jyMpY1iX0na5JJ82ianFbH6ZA0M6n1_GLFU3Sqhqc73LaxFVoNpSZqK3LNpOSbJgtVPSN3ZOnnKoG35jikGRL_vzgzLzvnk15DLPzSUJ96GzIvlEwf5fur98Ssok2PdE_pzbfJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=CU_MLfpIyOQPoNtF-juvZhg-maDyJyKT9OSwSPtq_AmEcCWSPTS2OyaIUNP6PYm6waxh66xScsWRwDLResUCxfOu_TS00cVnT9QTNSaatwhkvyV2GNNbXDV-2zJtjcdzOGpDEIdJMgpunisDnLIYJ1JCvhxai2XTKYAtWJwonxk03R2jqaJy7cGtYMbwcP_eoftt1AKlkDyN-U1jyMpY1iX0na5JJ82ianFbH6ZA0M6n1_GLFU3Sqhqc73LaxFVoNpSZqK3LNpOSbJgtVPSN3ZOnnKoG35jikGRL_vzgzLzvnk15DLPzSUJ96GzIvlEwf5fur98Ssok2PdE_pzbfJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTbp7J_X24O3OJtuKsSw2ZHv7Fo7Co8VJZtmrV4JhdQGn-pPrRji9KeeP69VjSuXo7xfei0pP5eE66zjKqBdFBupQofgYgoc-Iv528jCGqhnBnhMlJbO056iGdspZK6nduHG8M_LgX-dZfddze0AvrGEzLMBpJq2rqxPrFhAvaFUaoCcYA5d0HTFpOK-bMqkzXn2JVIZwnoWHkylRsX_bwfX7uaRXmLyJWZzMhLihcOSxEZMsb77JIf7RZMLcZ7AAWVAR8TO6ZZOueN9txkEeB8f8DsZs-IOcyanc27jxr8JSe7ZmjhRC5MlX3JtrT7F5AkS-3Tf1eKqRCcmySpohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=vq3v7klb2DduuXEg96rByMCQxtb2a-Pmlu-pCZWPDWyrbGfUVy5CKvCbdURQCxPYVXqIIp7cZzmPzhqdV__wJwSj0hUN59tmjM6jjjdJSYIT84RpgqV5WZ6X1w7uOolGmXw0eDeKUHqJqyGm9abN5ksLEL_393KOZlRfwFOm0RPNE6dIyG9-GeGsLy37U9w71N8Bd-6EU5SlTb29NTSs2EIktJXywNlZrIyL70JGKhqkuG7Cce7dURuWkaH-2p_MQxZxJLvpOBuJNa9g92gMXeDPYkQayUYFFavZsQUySzzz_1L_snOn_1B54RbEHMZAo-LPUuXysN9S35AIepRP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=vq3v7klb2DduuXEg96rByMCQxtb2a-Pmlu-pCZWPDWyrbGfUVy5CKvCbdURQCxPYVXqIIp7cZzmPzhqdV__wJwSj0hUN59tmjM6jjjdJSYIT84RpgqV5WZ6X1w7uOolGmXw0eDeKUHqJqyGm9abN5ksLEL_393KOZlRfwFOm0RPNE6dIyG9-GeGsLy37U9w71N8Bd-6EU5SlTb29NTSs2EIktJXywNlZrIyL70JGKhqkuG7Cce7dURuWkaH-2p_MQxZxJLvpOBuJNa9g92gMXeDPYkQayUYFFavZsQUySzzz_1L_snOn_1B54RbEHMZAo-LPUuXysN9S35AIepRP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq73LWChSxWGKgwrIkifHDyymBykY8bgV7y1mm-g46f88DtXq7733eUmQIwxuthKnTDowlfmevIkJUtwgCdzFNidkr_6I4cHfr9ZFJyVkXdlkffCN8MlhBWzCjlAzvGBCRmBjS5aR9-jf8xUrwpQi1OkYHoHbuyPi1-_l6rMLbuq0N-2diBmkNW61Si232ZX2l9sNg3Mv1rePBxsfgXkzPY_zphEVLmBALtbMpTLh0Jihw8bntNNUoCi8ravcYmfxA7wZKETWDfUPda0u5yEkKscZVljJJmUVIeEiRr-A6APnO-M3Z_lVKpDaFTKvzC1sumZTrjG7rCi-wsGaUZUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwmjClYwJnmyDjDwXtEV2MDZo8xUzuT4-S0XIcs8Ml5WQH6I14T75mumU4E6-w7Z5nWESWkTDmUX5wYGaSb5tqPIdY--lTlUh96Me0Vgk8874SBoIrutoowj0KRrQUlSZ5ivuCG_wmqzTZJR7oGdKMDoSTgC99kDZWfASkfG7m55i8ayUdPcOukUKzhpKsu56O9vs4cMslCV1IAv4SuJgV3tJInmZ8Kp6RtplVkEs4x_twrqrY5yT0EV5-MfiqtWsqbE3N4KlJc-35djPOyTSWd_1yzecNB0iZvJbsxGa9ci3BEcastHAE2AAkk1MO_30oJhBRHrHxoL-zBZfPkpww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7x0yuKt_TGVMz-OzHHp8EoEsuyvcUwABBYvHNeWHNF-ziwYehphr0gxsKPICzrmMhYgm63XUVAa57ZU89lxRC-kDmCl3v7QepELOuZQhSs5MC8OrGenG0Ug2Ue0YjmVPEp_ZIqtTN5g4Jo5-MvEoK2xH3BiNkw3xxGU5w0PtJ_vcVK_lRd7eYT6ymDwemP61uzNBgtdp49Ywiob5yY9rjjeGdVVKXP0y-elmDli4lFB47JInAkUXePG0Uo9j5cLaQBcNXFXhcFvwnd0scujjDkjb5_oTw0adWpraXD-5whALlDQgS_h1VVcMD9mBdW0SqxvtjrbS_ufKNUVr-74WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psfrlqvanRVlnddlkfoVS_4CpkJTq8qV8ujuc6fw722XSvEXoP60BvGWmKo_A5M8HFoBi4XqfRcIjDTuPq6SN7tUTT2kwWmw-QmkCyFeIyl0SjGvyMLGErGthqXiRtB5NSeYN8NJpgbJcZF5Wlpav1iwAoqBLisizxTIbBxR1zDhyqVTJwPu0WzE4pf4eb1pEe3eCd5paL5rDs1VLBAgGEa_QoQoLgfgvci8rYnXip9-uZz1udZWptzT8LbBXfcrWLtcaGHEfrTjEl4jAVqRT2oKbbQbqqIjRbruPm3z86__t9DQr-OLKP8Y8uMWsOD8NFz0nQZqNh_IImfOTxd1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOc8nl4W4MK9pxRH0DGD8MFOUnFjPNP4NyTOS1_afRWpMhsWc9g5ky37duPcw-8d6K7mmmKycflt0lLkymh-8YneXfC4nX6Tj68yy04v7m9wwu4_nMJYKW8hHBn1NDrXHB9IO4wa9dTiaqLLq0vfLrZZxtBGIOAFRohW00Do0_O2v_2TZi4P9z3n5ciVTJrZmGo8xk2jh9uss3wG_W1-qVvt54ZEFk1M9P8Kc4dl2IV6y8IUJ-HEIoHfpjNKOJQFKTvI7Wlb5-mzVvFLrOcIIbv1Pxf0Pi4daAOATP6SF3n-n7wSCAv3eP2ZZrhKj-6qCb1dS7r0jU06MHXLcErRxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=EvRhLQKc-WstLEiTk7AbAif8-da0HWnq9rcuWZb-j3rmlFHnL2lzPkVNw4HWsDUx_fbJYbxQbUszjX1e8YNY1sWZ26cetolERvFTsCAKUGmGIy7_uwuxxzEiWKNf5ci9FTjGsN5CxrqimpUY-apN5v0KBfUjjUAgdwkQP3GAevfGVnRwsRlq0YD_jy9KOMnpwjzqME8FOusMSRnD3cWT7a8cdFPncA-L3eiG5-9wn8W2Lvf_vQEEkGDVrbHJdtkG-FjI6K7PDTZ-2ttChgo3rld7jEnsWrMm0lEV5Il4iH-ZA2vhH54ROz8-ba7bm9cvSRGjXyndPA0zIk2w_gpc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=EvRhLQKc-WstLEiTk7AbAif8-da0HWnq9rcuWZb-j3rmlFHnL2lzPkVNw4HWsDUx_fbJYbxQbUszjX1e8YNY1sWZ26cetolERvFTsCAKUGmGIy7_uwuxxzEiWKNf5ci9FTjGsN5CxrqimpUY-apN5v0KBfUjjUAgdwkQP3GAevfGVnRwsRlq0YD_jy9KOMnpwjzqME8FOusMSRnD3cWT7a8cdFPncA-L3eiG5-9wn8W2Lvf_vQEEkGDVrbHJdtkG-FjI6K7PDTZ-2ttChgo3rld7jEnsWrMm0lEV5Il4iH-ZA2vhH54ROz8-ba7bm9cvSRGjXyndPA0zIk2w_gpc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsLV6LJ_63WPojavSGuX-Ylc5sLPYEz6kq4tGVp3Q34h0xFtELurNCl0F4BsNmALoisSH89lzXH3wJjYYJVkMfmhJmHEa8OHP_iv5gzvJUN0Umg_OXMANBnvVpzi30pTvVRQBCnTEEIhWT5e1hFsixjdc-NZxwGWDOkmUlUCvnGQE_UkYq1Eg50wjLwB8RiJGwDWndG_ULR3yR6N6fTnwKgBD6FJ5M6HdqSCatWAwmxOYfqh2u8XuL0bti8121EcWc-id_vWzfBnDKRWq27HeRzc5jGoa1Oxa-DgfkkhtFoAHqRWHgE7QPMdwGNZBiJRGeaQ5j5MSKdBakFIcNpTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIwJAMwUUKbgCmbb1v8Dcec9my_2LvJ2PAPGJ1M6uhv-c79-pL0s-Jsuk2rqhIzhO0QqaPbevvLWwvDH5UVZvMMT7CpIbIIWlL_D0KUM1ALcSgW5tWPs8iLZqzU4wXK38IdOzY33yUOub4GmDmQuacyUUJRllg2cgGF-PXOSkdj9gmXhzeEzn_rGb2bEKrh4zkDnzNTqXy7-nHOPX1yTYYyJocKe22dnUzKqs1MdjRgHX7Vu8KCDfEx_RUL5fostr7DAUEK0U9WfIKAaV2CZeu7KCWrUKUL8kbtb3ksH5pxfwjDNBIQ_GAw8Ky-ziinxNgoliuhiViMRsSF98jA5iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXhKT7-kD0MB4Xu_3Y7p88ZJTiVzOvI04BW6BOv-aBIn1QT9JWwgFPL2dTutHXFU9HBQiisGz7zHoZeFwR6VO0jOCRxkdiCm5LozHrL2r5XNsHmv0uVlGekJKYABZvJ_wx6BFgoksdLA23nir_UzUaCfRDBh2Pz_t58wB85bJFHut_5reFcwnU19BdnZ2fsZyouQPW08NbtHODm3HFk0roXgYwx1fPc2B1D2BNpkFk5NjPcQ1JjsYgh0xihOTn68T-QXNo7DXPiS3M5ApOZA4zSnM0XjZ7-djtt82d6BGfi6V58hDSwUgJLviD7f3k1M_meEFccQ323eQlnaY_1J9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiGvMRD8SkzTD0KmgzUOEv2a2hYBM0Fg7P_OP2X4En2tMfbMxlJQMQQytBIQmybYkC8tCu5xrhRg3ExjgVPKZ_OnFIy_fMKJHrck5JAdEeKr7zRANT3VBDtExqfg5_oU5M1jICuNaStflxdqVyrQb8UrqtTPuJrSfhI4qTIjpD1vKpnMmdD7pBulVlF39KT1-vJZQPf4hB_HK9O8UGi3IEEHpw6zXFC5u494WKjCZARV299DGs1jaY4jWmT_QCFccaWads2hNS-nWJzS3zsqndLfas7vcPjgC6Sff4hu5MXXVtBJ9MxJckIL3EbtObq_q4GaVGh5uyYQc15f8rua2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=HjEUkM3H0bm6F8POUC9WYTiFAcSbecLRHqvdLlCD2gRoZBttDG-tuHPVJnPjfHd_zwPgO6VTa8dPqNoL3P1AtbRj2Tp9O-r8ingJefRvXv35Tn0BQUo9ulQ4Ry_cbEOjEYkIg7RBvNuG4naa4v13i3tW_l-PkpTfz7lbJdP0oktKRJDLvhb9sLF-7WtrPudWGP8wpZ_NbPVzqZFwBl2cUjSMM3iv6fAYJml_YzEr2q2q5Psy3HEIlyUK4rGZ9ZLFYBMifWasSZb2ctoVja5oAvkSo5LMwa83E9j5VaZu2axDghU2U9oJhnGB_FsekmwS_BL8LXepwL13TvoNyND4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=HjEUkM3H0bm6F8POUC9WYTiFAcSbecLRHqvdLlCD2gRoZBttDG-tuHPVJnPjfHd_zwPgO6VTa8dPqNoL3P1AtbRj2Tp9O-r8ingJefRvXv35Tn0BQUo9ulQ4Ry_cbEOjEYkIg7RBvNuG4naa4v13i3tW_l-PkpTfz7lbJdP0oktKRJDLvhb9sLF-7WtrPudWGP8wpZ_NbPVzqZFwBl2cUjSMM3iv6fAYJml_YzEr2q2q5Psy3HEIlyUK4rGZ9ZLFYBMifWasSZb2ctoVja5oAvkSo5LMwa83E9j5VaZu2axDghU2U9oJhnGB_FsekmwS_BL8LXepwL13TvoNyND4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_HaothHzCOZO5JpR4HqhswDffyT4v_1LsXycbUI06YPaO3EKxPRmX1tG8W3VEC0a2ut2VYSIREDpkNpvNYuwMrPTLK9ftLEAIsUO8szaweXTsH0R3qrCZiJoZjVcd-TFWVq34rjZ7hyxSZoUDzLRjDvZESti0e_rGDImy9E1biKTnOABetYtgmmyPZkzZUir2nVRQUvIOAHwryrxZ2lauyZYLtJf-VGBg18lzPJ0qW3fwfJcdg3jDk6CnfqvhVrmYPLxKm3Q9XPL-9wHF0fsIihxS0hyzWnSxC2rkv_72DzMDL20yvXzE3errMSVzJpk5vywloR2jbDyAGHrSoNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=gBUIPSzP46FSw6E318Qj7x5qTfmpEKjRZ4VsnAkPW55NTOZ0GT5ZP2_cxIaD-1ePR-o7hQThcfmu9NCllIuPb-TvPyFTLLmlQ9KwSAnp0VOJasKtfF7s91DADsmVultwsxzmpSLCQpLqiAt8xw0atN_BwYTLeN_kgEze3VPMuS2ZXoVxvRkkHrSJrickKO3ApQeOONyXdgl9NoSKHBgEB8xefTpWxPLDosyHxgGHfRKN-AnDeGNPqhxsd2iNvZGEMNtAxvwqWZv6_yei1aKy-_zrOxyrDJhRgkEp7yv7Ol1OIiIY6cxmWgUNQbOxkcMS3EEZd10Bm3rtiEKQJ8ujDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=gBUIPSzP46FSw6E318Qj7x5qTfmpEKjRZ4VsnAkPW55NTOZ0GT5ZP2_cxIaD-1ePR-o7hQThcfmu9NCllIuPb-TvPyFTLLmlQ9KwSAnp0VOJasKtfF7s91DADsmVultwsxzmpSLCQpLqiAt8xw0atN_BwYTLeN_kgEze3VPMuS2ZXoVxvRkkHrSJrickKO3ApQeOONyXdgl9NoSKHBgEB8xefTpWxPLDosyHxgGHfRKN-AnDeGNPqhxsd2iNvZGEMNtAxvwqWZv6_yei1aKy-_zrOxyrDJhRgkEp7yv7Ol1OIiIY6cxmWgUNQbOxkcMS3EEZd10Bm3rtiEKQJ8ujDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=RbxCHC52K0Ggp4OE51S4uChRUw-63XftzUJOUZ_hWNZ7IYZTfiPsWRAdmf5eRxb-1GTjGn_vTWNOmE-hUqwU9NBloFO4jfXQ7-8t9A1olyX4RcpqMvFLhfGjJkwrEi8ERQm2H63eI5vlPAD3cCseVs4nTXC0gnUZeR-rYUmYJ0dxCkqbIHjy7guBEw8nyGzFfPCTrIwmLY8ZfVfgCZ37XIZ5pu2yVtW7ZEfcv5lHY3XPamh7iZIP5zje2HvbEzPMWIfP6ztk5C2zTIjcEITuRDL_31ZUDUjQXTHiMbK9uzZu6OUPUL1VyFJF8h_LqnFHq3uY6XkNB0qMLgQePQj8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=RbxCHC52K0Ggp4OE51S4uChRUw-63XftzUJOUZ_hWNZ7IYZTfiPsWRAdmf5eRxb-1GTjGn_vTWNOmE-hUqwU9NBloFO4jfXQ7-8t9A1olyX4RcpqMvFLhfGjJkwrEi8ERQm2H63eI5vlPAD3cCseVs4nTXC0gnUZeR-rYUmYJ0dxCkqbIHjy7guBEw8nyGzFfPCTrIwmLY8ZfVfgCZ37XIZ5pu2yVtW7ZEfcv5lHY3XPamh7iZIP5zje2HvbEzPMWIfP6ztk5C2zTIjcEITuRDL_31ZUDUjQXTHiMbK9uzZu6OUPUL1VyFJF8h_LqnFHq3uY6XkNB0qMLgQePQj8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQiqfp5aWNLPn_Q8SmBZ0pnLpfAS7_xqtTLHtc29AZKyIPiXEyt4ZBLPchCcHcZL8cUpRNu3cAZQJ02pdhbG184YR1788dnIHkmm70XnUmp3D9i_zpbae22sZHeJGELa3E_3cwGe98Q7Vj1p7pMBW5HoQoXBgUGAKYeKcMXl4jLNT23trY8tJ9SwXP4p6OcTb6rsLdDxmwACU-1edBRZS3UWK0pMkVcBnf3yjdvUNmrbqCsjL9ZW4ukcRVKit9PmE26MuYkNp5Qomj0RlDxL0cw87WoJTaf3XTeuliYeF7Wfu89AvD9JYZweUkn_rhvj2N1COLM2u9QOi8nRVjX_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=WXhR9BZ3PfykOg3I43L6Jum7I6hnZf8tEbX8Ncr9ctMd9M4kn5aNk_qq-ka2cdVTH1YzrjN0jeKoFgPtTs09x7Hz-oDcFK3yegmncqV0NaOcsSOaq08kqoYwsY5WU_x7HLDxojRtyqDmLvikYsvKVPb5MfZ0G3gRwtm6WFn__LcRsoPeUZPi4xZleQRY7Z2H9ZxYrOJygpZwp3oqyM_jv1mND5kGAefXlaZDZ4zbm8Xz5da89GWgZV5xPnpfDQO9bVskgizJ9aaYuCLtJq03W89h_X8VZ5hYVKJSQj8uudJM_WISfHEzYPEjbkGzyYlF9k-eB-JdLKs4wFU7xRPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=WXhR9BZ3PfykOg3I43L6Jum7I6hnZf8tEbX8Ncr9ctMd9M4kn5aNk_qq-ka2cdVTH1YzrjN0jeKoFgPtTs09x7Hz-oDcFK3yegmncqV0NaOcsSOaq08kqoYwsY5WU_x7HLDxojRtyqDmLvikYsvKVPb5MfZ0G3gRwtm6WFn__LcRsoPeUZPi4xZleQRY7Z2H9ZxYrOJygpZwp3oqyM_jv1mND5kGAefXlaZDZ4zbm8Xz5da89GWgZV5xPnpfDQO9bVskgizJ9aaYuCLtJq03W89h_X8VZ5hYVKJSQj8uudJM_WISfHEzYPEjbkGzyYlF9k-eB-JdLKs4wFU7xRPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILFzdO5PfD6AGBAUszgzMVD41rpR6wEFiNTni8y0J_aFPOmyUAYdb5OJWFHoMSFqLc_3dlnAW6z-gky70pX9xVruQyY3l7hiFIHGt0g_9arFj328jk8Iz1EnIUazUqlanCpCdIeGWNaj8vmI4Nx5bCd9mVaT8ZnKTb05z2ocmHFkPCZRcHl5Anpvlr2paPYIuKwt0cQJVuJVi3-hvhmZZAS3DCbKahiz8mx-vI-BikMwV0LZGmSP-CTypcWufTLDxk73B-Gsu-PpufBZdYJw4tW46mMuASNqCDqBQQZUKWXOeWQlTP26QR8zWlmy8FzNRPN-6OkoyR3CmPvp93lKB6gU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILFzdO5PfD6AGBAUszgzMVD41rpR6wEFiNTni8y0J_aFPOmyUAYdb5OJWFHoMSFqLc_3dlnAW6z-gky70pX9xVruQyY3l7hiFIHGt0g_9arFj328jk8Iz1EnIUazUqlanCpCdIeGWNaj8vmI4Nx5bCd9mVaT8ZnKTb05z2ocmHFkPCZRcHl5Anpvlr2paPYIuKwt0cQJVuJVi3-hvhmZZAS3DCbKahiz8mx-vI-BikMwV0LZGmSP-CTypcWufTLDxk73B-Gsu-PpufBZdYJw4tW46mMuASNqCDqBQQZUKWXOeWQlTP26QR8zWlmy8FzNRPN-6OkoyR3CmPvp93lKB6gU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=DnQmxTiOZ5-bDcurngX2h-I2Yucz3JoMLE3Mcn-l1WoFPYlT-YecGGYBpk8iOA_Yzcj4h6FH61RMqvxNIgTrC-BwI1GEgRTRkK8LUtb1ysFOhbeUZeScgre8pLchGZxgLWUJrojKoirAQ6aSraAhGjvW6TxkT3m4XCV9lYYNLzt8x3gIyDF1OcPM_KLflwAxpYAVk-3BWK2P5ljA28qJklcN8NvydTcJ2FjrzysSPy_17sdoMQ-wHl0qbeQgjD73GyOijPYZvExAJIKqRvzijT4Fvwyb4sDWzGgI_GjFyrDvRVX8ZNQE0z1v-h1sOuYLy1FVdoN1kzbrFMtfJdUcUj2QV7BjHtWhwcQ7ur9EtpSusU0I3QVXXqwmdh2xTspHPh-SD2n3bjZO4kaO2dmi664Eb7MgvTdKg3_pVdvbGm_vR3u8WWw6t9dWqWYxU8TmWRB9vKpURRGMxfyiDtCqq1NjMnSbm4fA2r7MhZYXdSTDc5vFwyQiUPrqO7-5eX0P6V7FY2PqUF6OQJqkAg3rnzyaXV1kfxg1Qsj9LIm3e3jJODpLPbAxCxdRvTDbEtyWZ4UGpGez-f5rwi-5t8Lbu0IpwlgCI1N0C321x2HXvir5_lYtxPeAjlWJiKZUg7XY1Rf_xitPlspHdGNdElqeS9GAlRknFhr90hBDYsMkLhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=DnQmxTiOZ5-bDcurngX2h-I2Yucz3JoMLE3Mcn-l1WoFPYlT-YecGGYBpk8iOA_Yzcj4h6FH61RMqvxNIgTrC-BwI1GEgRTRkK8LUtb1ysFOhbeUZeScgre8pLchGZxgLWUJrojKoirAQ6aSraAhGjvW6TxkT3m4XCV9lYYNLzt8x3gIyDF1OcPM_KLflwAxpYAVk-3BWK2P5ljA28qJklcN8NvydTcJ2FjrzysSPy_17sdoMQ-wHl0qbeQgjD73GyOijPYZvExAJIKqRvzijT4Fvwyb4sDWzGgI_GjFyrDvRVX8ZNQE0z1v-h1sOuYLy1FVdoN1kzbrFMtfJdUcUj2QV7BjHtWhwcQ7ur9EtpSusU0I3QVXXqwmdh2xTspHPh-SD2n3bjZO4kaO2dmi664Eb7MgvTdKg3_pVdvbGm_vR3u8WWw6t9dWqWYxU8TmWRB9vKpURRGMxfyiDtCqq1NjMnSbm4fA2r7MhZYXdSTDc5vFwyQiUPrqO7-5eX0P6V7FY2PqUF6OQJqkAg3rnzyaXV1kfxg1Qsj9LIm3e3jJODpLPbAxCxdRvTDbEtyWZ4UGpGez-f5rwi-5t8Lbu0IpwlgCI1N0C321x2HXvir5_lYtxPeAjlWJiKZUg7XY1Rf_xitPlspHdGNdElqeS9GAlRknFhr90hBDYsMkLhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=msem2MSPk5XQ1wn-CB7gBXLQwtQgwFYiDl3ZhEF4tK9vHL3d0-vnlaKnkjUOX7cQptxyvDToSwTWXVZh4Hb1UiiaCuG7mmr-EKTRRJBUKYa8OX1w_tXP0kVJbouCu69I10_VhyV5uZ5xxi7q6Cf147x4kBD4_MqoW9x4n5lawh88nUA26RF7UXXpmhZWVVn0JAxEq03Qhxw3odk2tHdIb2Nmea2GARSqvjDond71oqBOoTF0ySb0g_I3Ga0F_bFS2Lg8hXV-BWU3RrgXmFTcWhde58RiBk1pmEHKf8rugJTJTCSHL-m3kOZuUAyRS1xd10L1yFQ5OoVj1bQgMpWEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=msem2MSPk5XQ1wn-CB7gBXLQwtQgwFYiDl3ZhEF4tK9vHL3d0-vnlaKnkjUOX7cQptxyvDToSwTWXVZh4Hb1UiiaCuG7mmr-EKTRRJBUKYa8OX1w_tXP0kVJbouCu69I10_VhyV5uZ5xxi7q6Cf147x4kBD4_MqoW9x4n5lawh88nUA26RF7UXXpmhZWVVn0JAxEq03Qhxw3odk2tHdIb2Nmea2GARSqvjDond71oqBOoTF0ySb0g_I3Ga0F_bFS2Lg8hXV-BWU3RrgXmFTcWhde58RiBk1pmEHKf8rugJTJTCSHL-m3kOZuUAyRS1xd10L1yFQ5OoVj1bQgMpWEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_G7IzKk2efhNH9GVEuKWlYdYsBRGEWsvG5BuXcLbNtfMHHw7eDFRCXzB_gLbmHcNhh1vyxeEaf2MaecyaircdyfqGBrgde8F95PxPdRQOlxRozmxA8kXPoerXEpBe73t7MS_HJLiJZCc40BX35vwzQJksK0AWvYyJ1I4JWCVVz1DC_U2yzBw-cIZkprXtutmLi1SuY0ltcQmSafwWsegWwCZItn2-CI1mZYwB1xa4cmOLKGXp1A2lPkv1WjW7IFlnqlb4vi47Qq0NNBMgwy7f4onB9S3jNoOr_AdVNtRIzjfIPFGM9hXd-DeuBGl5vbcrTbZwcAwG-0gBPPy2vMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCc8_AV2dqaNI1VxsI9eSiZOZIVpD0OuC4PycVPey1x0Pl4vfSMFlaCkJRP0GSahJXOCWKMWaCEcTPs65ZMkrF9a4mMefPjsjoIwisslr9AOkJMwuwm8vcvV_2Nl5kByXUmSD8sy8MiD7xh1tNBr7UynWQMRTK6NgrrDe5ec5OkuGzGT6uJvL0v-OfWxe2ame2pdwFfUKLbpH4MiJHj1R1nntBfPC-Wh4fBFae1xF1pC6zM_sg6YnUtW7kTKqDPKmhU1RHtEcXAGA9NAMWqQY0bTL2EEzG2EC26k7k147P3dRMHWGV7-qZMErOlORzx0MleeZ_coH-BljV4Eg-LWWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=i6BvxUTSSV1rGc56Qy3fOqODiWIcIWkvZ62vatTqWbM5H1Nv4mBQJECUCQjiJmlWJ5bClt8j9x6iAQmYuQFtyaP6Cqm5HmbID_eIS1C0MTrqNtGagGIz4Nk9UWL3nPUBeybgj3T2ylUu1AIC7_QnJYC2I47A5eYAPcViWdRpJa2cUz6iTSw-iKXZovj2U4LrKkTm5SpLbV_KJx8ohB91E2_JDNJHiKy6Fx04iRX2wFO2HSamkuxoAeWGaE8tltmeI03d9D2K5lN7X-jIxDhLwfumGravLYmFdmWIgyfltfUY6mrmW2nEB_artyjIRRHwp1EOBdISMz2VChOaCzFtPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=i6BvxUTSSV1rGc56Qy3fOqODiWIcIWkvZ62vatTqWbM5H1Nv4mBQJECUCQjiJmlWJ5bClt8j9x6iAQmYuQFtyaP6Cqm5HmbID_eIS1C0MTrqNtGagGIz4Nk9UWL3nPUBeybgj3T2ylUu1AIC7_QnJYC2I47A5eYAPcViWdRpJa2cUz6iTSw-iKXZovj2U4LrKkTm5SpLbV_KJx8ohB91E2_JDNJHiKy6Fx04iRX2wFO2HSamkuxoAeWGaE8tltmeI03d9D2K5lN7X-jIxDhLwfumGravLYmFdmWIgyfltfUY6mrmW2nEB_artyjIRRHwp1EOBdISMz2VChOaCzFtPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o27rxG72ft2O2sjiHxT7aMCZsbeyK2VmvJMufhW36-WPvkxiS_GDd2_PtJ8-RICl7_tGfS3XadEN1ZcpPVkJv8mW-H5Gxu9WNwmIOMzQBZ1KPI7Pt4JkagCdaa-No9wvqi4LKsTQJYsieplUt2aNjYbsCcewTdHAnUY4ipreQZygpQbAYwGH8AsJh4ecE6Gsz0hq_GUqtW-3PuOA_iwArLPq6kQ2z3Fch31ZVWv8ppcfLF5y62_D1xs5BKSj2lcinhafokOr-eNrd82jsehKTbZjxQhcA9gGX3IVCEOdpVF6hDOgwgWoWs32k9WyFz90Vif2934Yq1hddwebcG7uVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=gTXYNopQ_bsc8QW4Hu93LHcujNJLj0PsWV9P-ogU2GDWw2utahTSKV2bZf0kA8LtQFBBq6GEVCj5m5Pl6zUNM9DHzRX26XtRkRTrt3vEJ_-nXqvLb9ovE-9jYlDv8KHGBSpxpgPn11dDURUGPym5lPI0FdauWck1YZSq1yJS3QvuGyOMtRPq99IM5ReTeg7afESHHVQm8QCcbfirjAFRU00TQzIPCce1atUH3qJjxU_cufD1vwaNLWHZwg-Nkbe1OHlNkUYNkAi6ZUDn3YeM_BnvfPL0TojRJAC75HBkaYwFUqBoSWyNDeVX6sE6xjyyMCyk2xwLZeyMfTJiWHdO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=gTXYNopQ_bsc8QW4Hu93LHcujNJLj0PsWV9P-ogU2GDWw2utahTSKV2bZf0kA8LtQFBBq6GEVCj5m5Pl6zUNM9DHzRX26XtRkRTrt3vEJ_-nXqvLb9ovE-9jYlDv8KHGBSpxpgPn11dDURUGPym5lPI0FdauWck1YZSq1yJS3QvuGyOMtRPq99IM5ReTeg7afESHHVQm8QCcbfirjAFRU00TQzIPCce1atUH3qJjxU_cufD1vwaNLWHZwg-Nkbe1OHlNkUYNkAi6ZUDn3YeM_BnvfPL0TojRJAC75HBkaYwFUqBoSWyNDeVX6sE6xjyyMCyk2xwLZeyMfTJiWHdO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrZKP-RmCX7-MWEvcwSX258btp58VV4rDCFvpmzwUtBjg1cBSfEOu7bebXYSCL6NS56EQPq8YCazJIU9QVIirf04hVSPGq-8KhnRhC2dAkMBDlkl1onijYULaNI7Bl_L9712QmN_sg8a-dGdC-T7pnI34sRmQUVBaNwl9Rvgx53BlBUvVLY9e_D3lhI-za3fCWadv0qgbKdwsIQaKgG_3QgEBoGe6RM_z8SEEJV7DFkySXQnflRplRCb_htN94O-1x3jW2AixnaV_Orx7tD0Mm1j8nPPnFXrp9tiy100KDDZtw4wy_zNUUh0uZHJpWkLGcb70BNbIg2IWs4t_5mCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHZ2bxVRg9IWqou77KYjwt0QgZxVMpRfSzYYRHsSY34eWl-tx6gzdD79IKaqcnRbNeOSXiaaxAtyhSef5IQZiZ-yQo77lZPtBA86o8NhfdidT0Ne8rJjU97uXFQ8u8RzZ4efbuE9sUhwuKpU83Yw5JaJ5VdP4UgksJrMFWbHj0naHnPHAey-B0opZEj2uO-E4CwTIksB8APkkDdskvGynMI0GKndiFdqWvcQBl8TQe6aQl-TOHSyTVPKtwinHIgxc0P9v_v0BkQFau3YkDD1L9oI8EGD7jW4OM0C-bRf5P9ODvOWynofiYsbbH-0bbDkRyaOU9z2ZFQSRHsfOkB2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChkHC9mhNnqrPfPaMS9qiNAvyLln3pIBw-tzDugptbKXYyNzBtL-HWO9wp7_0-jNLI4LiH76BlCFrVrDczdm3MFKtgFvf5FaOdT8ksBz8GaU1cKDdj38SL76MJv5V5yEpQmL1SmwVyxto7mUrwg5Av3MCw6RiT8lHaG3JuYwMKWE3L4XB94Z5NoAVphyFei-u947_pFcCm_rnaESgVgxNyT378NykVNdQdIM8q1ZcjFyvyOH1VRYGiXu_DgeFfz9vdcmgPY1sGX5HIR20kOdnTn5eLG0opiczQ1SntH-PI9tb-JKDH3cLVJMRjSXwTondLB0A7lajyP0QY8YcIkX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv3KlLcz4lFo6tUns_v0v_EyQkJ4ocMZHS0JfiugOXaKHQ0Z3m-Psl6IEqpepApBs4eLETtDPzAJRb5zXvQcBwM--oa1Yjz1nBdP4YdLQXqw3TlAR2KT8RI2NMgevXX52VYV7mJyAEybLT_FDtAvt1FziXF0EX1Th3XhAqJybx_U0BtSx5q0-lNlRkIxopyWq5QCrKlhjE4WfyJfGu7LfY3kUp08E56nPQlDEmeCBY6LNIegpGq-vOgTucE3IJWP9zZJa-xWoSL1A8KiB8hR9Fp5kgRnchxg5E3B6uLPK9G-2fYMy3VV8kC6VnoPL9Ah43kjYGwff3ctQriEInGnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxEce6LqNNo1OB-Zst5z0818kiK2sJ8Sapp2LUxT1jZVGp7je2kQ2CWcDONbNyOh97pUGw0CUl-hzKUVKp71fLgHdC7iZw7mBP_lr0Cr7WHlAGCIhpvlcEb0dLoaOwmjrw-zza5884QrpbSVqWopR04gF_tNxOVctN0DbcWska-axErzWeMRsAXk_gHPrkjOiPlpe_Uca7mG6tRqLVN0SNobHLX3FhYsW8fNXUrG5QtP707DMQDUAXZbhJmoIVq_-A2R8u32hKFpO_jkF_psr_NYaigMgZua2h6xrPZcpPAbErIwt5_Mb0_2syylycJrj5lr0W0A-CRX-BT4nNG-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao4KD_4ApbYIJkBsxMi2g0BMw-rf_uVAL0CneIjrSmS8MZGNHNKmyjd9MCpnMi_Rf0rNmQvcAigRJd090L5TdgoG0yFP-VVE5iK1lCYKGB1qeaCfdwNbOFpzTifNGJJlSDOFFFpEAvZCFXakDYC1sHfae7JvrtptRprbwmYt_clAtqBlFautgWior9u9kiz1dIspgBqSUv3JjMoAXwfAbqgKQ5OMyziCarF5saHCer2gWvC5yv7vscU55QCqYd5XV9oFE7vrJmzNZ60Z0362mVjkuUuiqfxN7VlQHjHHf_TFv3YwVno21_ZCYHBWUiwh7FJ1qXGqTTI8R1ZKiTb41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXKsz_YYtLsGsMSwaDuH66yskno8gTC2mm19oVFntUOUPMf13NvInTNRPxJxBGnyEaeVn1LAYEvdjt-5zHdYsmZdUvErbDVjSO5YQk_y6hIwWzBFEd_9S7iBfcF_Q5jotFQeNsChMVMbQbnutx9TNyPLqtdFS5Pt0j9l1AL1ph1q42_CV3_vKrm2HWdREL9gVDm7RyY-dR63gXWc6WgKK_jyWWelk5Nxiez0zDOMsbhumjRV9brrJg8-3bnSawlE1H89kS8ECacl-72w_TtP5ffAQrFy37ZnnQi2wclxwOSE_qc7d5f-mmmvX7moRfRkFO0fN_NEOqXTrWXANnzeCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udCsz5vyBeXAsPjf9tBfXQPNuQsNPkgQjdEVelTXPvuXljHT1L4dymE2ouNH8M3xAj9YLbALxTGi2S5ClV881XtyncnfEY_75TVCVSEzL76W9BQ7gGcyYkCBguLNejsjiveQgijsynFVgfUfJyBiObnSWBKp9E174S4NYySn95FTE8N6FEUznu90aF5AxwsznO_I1q0lYLbztZIBJBdSLLsGOBnP7sznSYV2xb5Xt5LGZpYEuS8MM7sKjk74SajzJwIG4BUVCyI6C9MrU6eFDa34RfBq3rqXv_m1ghqKhXowVXZ3Ap1dsGhYwW4Q-Oy1_4_VofN_jrt97gOz8SC1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxAQzpO-xHIbrcHGvtpBDZn_E3yrdw6clDcbxwqeqbUfytoKS2Wp0J2CEUGZecjcslNX2VjKIhcsJ4aHTm2MmLeo8YcCy14EPwXKrzTb6oXDSxaId6RMgwCytrUxptp442XY7rKxR7hlxLgFMPsBfP0_-viC7cYjuntThTRZBLuZQlJcKjy5zRF6_K67HDsxHFLr8Z7HOVwno0AznJ0Ahd3dDyi4Yo1aWtQNghsDZVOMlTeDWsG4jIR9je_IezlTli8KfwAEL96LZLTLvEevQH05QZ_TYjw3hFav1RWHkkODIxkHL43zT2PEHkn5eiJZHbDbMLd-gEJAKyRoOgVoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOvYqqL6WzUj-PBvk0uC2AzmSPfb6wgRyUJLqKigc_T7sbbV_HSUGn7m-3cGyDspBZ5TzpA684Zy2k0kcycbbiV4pAZWRC5x7Eo-hVua4VPGTa4sW53yGvDw9p8ieEZbjWPeuxDbQP4FGJ_Ocjs9yV-S3cJNi29UI7Ry_afaqN3551R9B2QUuDXa7P0FRK14p4-87f8Gu2covMNB-kyIQroLltFGSrDeNYbUOBE_msqZcWS2KrfQVqKZf7kmi9q2LKrYhVFZK7RKGQQSdWw-F9wIsSqGq2MipGTEMAqfYXetMM1C49Bt8JVrUhk3GeKrm7y2oRYW4088oHOcgUcj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=OW_6qR9FPvxm7a8zzrM3QFAALR8Po9pJeIcdR488uVzNdEXIbvl12C2rN9xWKr_c9uMaWECMC8WywL2BKbga1txnOUPxtvGCt_wm5LVsahpXeIaZOenR6kTG90afZk8NqoNYS1Ccw1f2hZwA9AMBj2aqEan0AeXYrvjKHa5IAXR8qgUCTkqHEtz_Vcm8xe8wDuJpMymtBwf5gOqBh10_KsPpylv2p8sQip6Kpagc4XGosWIdpOUSMaM11GRDoHb-aHMHbtCLB7TCw49dc2C2iEbtBRmJuk8tMckejX9hPnTiAcGraPJxjgnV7Pg4Kw6yotAi3NbEIk7d4GKErX7PAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=OW_6qR9FPvxm7a8zzrM3QFAALR8Po9pJeIcdR488uVzNdEXIbvl12C2rN9xWKr_c9uMaWECMC8WywL2BKbga1txnOUPxtvGCt_wm5LVsahpXeIaZOenR6kTG90afZk8NqoNYS1Ccw1f2hZwA9AMBj2aqEan0AeXYrvjKHa5IAXR8qgUCTkqHEtz_Vcm8xe8wDuJpMymtBwf5gOqBh10_KsPpylv2p8sQip6Kpagc4XGosWIdpOUSMaM11GRDoHb-aHMHbtCLB7TCw49dc2C2iEbtBRmJuk8tMckejX9hPnTiAcGraPJxjgnV7Pg4Kw6yotAi3NbEIk7d4GKErX7PAzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFP0fSnspCWSm342J7bj6ZTSjiIoD-gEojj1Mivoth7gdCJ4Q6m3CpXLjIXi6irCN5awkA_mkEr-rVlSTx-MSJoGSK7zMdsQu4TIWQUen4GCjTHMZ8t3bF2uMrKpJYrl1sIRsmXjME-hrcjCWRfp77YhmautKvDwJxG2s6nU1LW_Yq9_EFw2oK3hGpKTH_NRuh4m6uLLpu073JKUBwGvnPx09CvwGzvVfPWg4Easinxv1U-FscJ7o-8NiTiy99nuFPh3QAkYiRsCZeRjOC8Ke0o8gL_NkPuy_nykp19YBP4A2QyKf4wtEILwHjBbGNynFQ62gAj27-zSXiayPT8Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=F_3oBM8Phg0WaGgV4ib-7U4_9YbQvhghyBUVOqpioxn_50TRYKEYsjCZ7aSjyTnbOXQRxDtZsSC86F880kjwlRT2Uzq7X92sfNcYy7rXOv8zWOJPOepypDMZ2oAVSSJtrEciEPWHSoItiaUBjRyiU-e7nY-ppxyBtBtqCdWLikFXQDFQ46x8mccM671jLaIoEPD5L-TRSGl5P7Mea7bY-heK8bjBKxlUqGotQ14Kpvi2N0rV3uIhYNsfoOFBxWrv6sqRvn20WZEYc9IvIDeY5zMyKfXjKO9DTAco24W9t2Kw6Yaf1eMBSADH-qcnfkG8UV2_qw2TTebXVTB0tBnhtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=F_3oBM8Phg0WaGgV4ib-7U4_9YbQvhghyBUVOqpioxn_50TRYKEYsjCZ7aSjyTnbOXQRxDtZsSC86F880kjwlRT2Uzq7X92sfNcYy7rXOv8zWOJPOepypDMZ2oAVSSJtrEciEPWHSoItiaUBjRyiU-e7nY-ppxyBtBtqCdWLikFXQDFQ46x8mccM671jLaIoEPD5L-TRSGl5P7Mea7bY-heK8bjBKxlUqGotQ14Kpvi2N0rV3uIhYNsfoOFBxWrv6sqRvn20WZEYc9IvIDeY5zMyKfXjKO9DTAco24W9t2Kw6Yaf1eMBSADH-qcnfkG8UV2_qw2TTebXVTB0tBnhtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=EdTkQoGhnch3EkoRZftxWQ-7iWAzAF_m7g5MxhhMXUEUg897iwJE9ChMrmVE6ardJvvJCTF7aUXhTN7cTYwEctCTwcdOukk_8F5idyjV2qluN-fJBkIqE_199n4dafo1JbwelprIlf_1GWjbzevKwd4yjY9DfU7NBaNqGFbE7oCTRaxB6xzpPTUu6ud6S6jXId7Ok6xKEjxkZEAhHksebNDSho0yJmRq98uHMwONoAnnt7iOw6DSbdf-T_IWDYcFzSRdJkqbldFIQQ6jEyMCcZifLd_IPRV6jrbarHT3ZMllTL6sji1v0zxhXxYSJ2NUAUf3ra_OXu2AtLC0wGC_gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=EdTkQoGhnch3EkoRZftxWQ-7iWAzAF_m7g5MxhhMXUEUg897iwJE9ChMrmVE6ardJvvJCTF7aUXhTN7cTYwEctCTwcdOukk_8F5idyjV2qluN-fJBkIqE_199n4dafo1JbwelprIlf_1GWjbzevKwd4yjY9DfU7NBaNqGFbE7oCTRaxB6xzpPTUu6ud6S6jXId7Ok6xKEjxkZEAhHksebNDSho0yJmRq98uHMwONoAnnt7iOw6DSbdf-T_IWDYcFzSRdJkqbldFIQQ6jEyMCcZifLd_IPRV6jrbarHT3ZMllTL6sji1v0zxhXxYSJ2NUAUf3ra_OXu2AtLC0wGC_gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=rq_XdVAcc1P9jg_L68my8dHSBThsf5OLpncYTxPfUI8mJg8DZPHvZ9-21ATtWSezo7WyPPxpb0pFSVGA6D8lkMp9m52OqjOn-aVQ6obp2919OSi_d-mF7Le2GkUS36YBdQOFIDpFxdEgFKSbranKOMkaAR9Iarbe_xqKVF04NjeDKPS476IzEWGSK6AKuGrmKN6l-WCzBJ7zZ5m-geR9G_QMqfX_FqVXtC0RPu82t2PjDM3oTs9ZyPVBShY2Dkgo3wv79B1bYTzn4ZmicJcG8vc47RpGbLN-pU3UnoywKtJ0DsjkQIF_092it8tIdmh4FHawNhMq6i7SWBDjsTJN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=rq_XdVAcc1P9jg_L68my8dHSBThsf5OLpncYTxPfUI8mJg8DZPHvZ9-21ATtWSezo7WyPPxpb0pFSVGA6D8lkMp9m52OqjOn-aVQ6obp2919OSi_d-mF7Le2GkUS36YBdQOFIDpFxdEgFKSbranKOMkaAR9Iarbe_xqKVF04NjeDKPS476IzEWGSK6AKuGrmKN6l-WCzBJ7zZ5m-geR9G_QMqfX_FqVXtC0RPu82t2PjDM3oTs9ZyPVBShY2Dkgo3wv79B1bYTzn4ZmicJcG8vc47RpGbLN-pU3UnoywKtJ0DsjkQIF_092it8tIdmh4FHawNhMq6i7SWBDjsTJN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
