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
<img src="https://cdn4.telesco.pe/file/AE87toM8i7I9Ik1m3PaE6sNXKVe3IRgfBmbi12Bb4NiikBVO8P3-lUz3eKg4XT15Ou3140QyTohdD_np1ZuiaGpf5-ljR30M9-N-nPwN2Pjlmb42z3JogbkAM8cvdQLziDvBZmim1rYzk5umJp4UQZJtmwWQ2M0pdxQLEdOD7mgojhHtKTyde_zUXWeeGRkIYjBCcsTfwODpJkk0Z3a4T5-sUVRegbcSKF9Z2RG0G7IcBp3YH4voAytJO8Vjjmc6_6ynvy6VXyEuusMso3AjmKOKWZBywJXFLUojiU0ngNNUI3sCHghz5U4Xu0tFmk9tbyxHCMoXRPyZDGim97q_2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFm06uSYg6159Puts4R1f_fpEhfqXtoJ7eyjgLVjtnMxjCLgrh9Lb-btuuY3_h-vV6xwg7H75UQSxhg_2dAuKDJbgb_seP1ty53gdBFDuY0mGyWxIxZs8fM0K1XGHSfJmaS5Sja1UimKL-chjGK1RkRXWkx197oI9cAl8xQ5WzG-a27Y-BBcwW7s01gOKlZpRHiJp08NJ1zljPzQ9E21hAag39Y2bjgb65f6VU6XfivzUmA5YyIQEpm781NvGvs3CbBOHOGV_nQcxLd_5dRXqDV0yrFuA6RPWy1Zm-LItURLndxvGmD88GxL09x55nvbD7pXZxljl72xUGtO84A8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm2dEeQh4y_skKjM6wcngDG1C3Sx3amBxupjkJggt70mQz3C87wPfFs2uBumnrMEGbRuvXSoN7l_wKJ1PU41F58xvHafyb0PYsPGQPcD1RFcWZBfCOXRw6vRMd8vElH5wVAwVu6ZXHQx32_ALO7IDQEnqDSC2oaX5l7YwgFbBLKhDkOis7vq34m75r-OirT2OXXG_KqQdXTPzRPNiMAkpOKl-U9PR5nWMaXwoCGH2yCsRXslap9HAqDxlFw7Tuv5UEML0MIm1GV18hpgkVRLDmP3Hl1sNCKPe-gYXLMU3y9VBcxKw9skFnOMhX6pf75rbqwn0Lg7ZasgrBYON-WtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0J4m7ZtyuWxj8PMAdFOSR21Y1e--yjrgtV_VEOMLZ6qxTxYN5MlqAzXoOnbZrtySATY2ekmgbquDGE31pz64zZQ1xH2G-jqptmLaQiQN3PPygLUQok7LD3YcywAtGpw7KYsosoE4CPpu_CCnwtFpWB8AW0Q5WrON4eUlXwCjz-rHdOPI3j5S8F9c3vKESup1wQLxZycCgszD0ACYlB3fmTtAxspMTmYHNZg6Ak52evG6xW9K6XJzN3yl5b_h1uoTqJh4yaukfFNswRKvKcV50dATNvUraOAZ-HCIky6p_MojGgF3EOP2NYtzT300yIqW7se2FYyspVnkjTNFONvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJmv_LX_PH9Wt5x7I4FtLznHpbeW0mQpU8A-Thzfpwvl4keth9dMp2KGYVg7bffiry4hc_2jKo87G1vCOKts-TOKaa9GoO0VKgpZUUkPDvNB48DTmlcmDuyvtUpGBFhW4shZvkgR0rfaxjQ3V6c9R8P0elnphSLiCKXc3I0xI40JwnUxuOqfmiWRft5g7V0hxEIFdjHEHuwVzrSRyJmaJur8dlKRQxTFoooPWf1dK_PlCpt095GH2N0zHZC_EwvQo8FlFyQsRkbEr8z8cvgsaSJqGz4xshfMIfm2y1wHVG0O0Xro-D8OocGd7pChNWDuwfJLwAQvMwi4V9ZsvCYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44UMwe8q28-Q-74uWtaP9m5w__GCj3Ww9kHgjiIC3AkfJ7CyxAl4HIRuAnEcRiRUBug1HDGlLLeCzlUlk6AV-PS595ZR-GZWDKzN-NjXwBVl_d4OUO4nDg-2VB2b4324kI0Z9MJpUH_6anTjhEoJMsqJEYIAsPpIZ1Za2jeYih8tJ1DkK5xjpLEV0ZMC1VTfXz_YYU7fDK_YD8f718NDWN3-muN4ZZ3xdXto2fcdiC8LFVkqz_nboxKeX24dp5MowKHIm7mgyzRL9PgFrXFm7Wg4igr7zhjwRNfReqQBUyOS7hFlvO5owzjlkoNxr_BCxfuMDumMlU8imPW6F9F7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9aANO2Rp94H8_pHpOZD1OWzEquun0J1w1KPfUkLywkaOM2ad9Z5BfC-rHcLCwc8kgvNMSGESoraTu6vIyTNZ3uteyA-POYR5EbghfQtD_k1VpgK-AeIngy9U12aRAJzdodlpMSLr7pYdVsLQ9aru9E7CwcIPYtEDawqoFbTNjEMBZJTUU_l_2XjReMGnI6RAmJMHqxpACdwbVdoZObedPN2ypUzV4A0Rq3PLv97ULb3ixi8S4qkE2Z0Yyz2ZfuUiue7Q-bXX1p2Ohb-62gw6JZHF4Rv-C3uqnLiBksZxJiq1kYcuO_g82RHW_Cp7R1v_eRNNXdCbYFqnlGgPZWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6praqAha_MBkP65yUkrEm0NDEHf-w-hwTOqXynpVQWId-ECFXV0LLaYegWfNVSHUDWkxJRYEHj7N8gFukJ4u2MBFOYhko2b0UZMQaqZi2YlWkjP4vG0ctFbIubsWBHZwX70UglUX-kibrLuh_QK42Q729HP4vKsrrbkRrUpxEa3AcpcJFH4SMxVIKs8LmtgzIcqnrydAlFxL4l5UjqakNWUVdniOYUxdrPlvnruESood_klGSO3Lfw6QnocfOiKQiGsNdLLvfGGfbrMcCp8vW2UAYS-tBp9dh9bYq56pukMeYmeG1HmtRZgDsC3zAdENd1sHjT6nzbWXmQ0N_Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyQWQv9t956qB7_sADt_7LGEO7autf7AcXedklp61k_mNfuTEtXBnVx6ZGwUg84bs6BYuWxYcg9liLj_IAReEOWCOv8buGt4hQtIjr1t9r1U-_d11SzlEtPBrIxN7BJolPSlvkpziY5sqKbO_EV6DgBshg517G2_ooAn0ZL5Yp4O1h9M5oDxyjQu2J2OKi4eu8pyA4gn5Ks56fQTbt2qNopi5jb2tm-sfLWVerq9T0NyYRp8xlNVhtgTN0LijzT7enzhfEbkx2f1mpLjPzhdADDCe2A6I1xwmHtT5hlfo5gFfWCT17PWecsNwMdrAVmLldM3d0_rvmYmkXZJ0NevCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL4zRlLMw-NoW7Z_chXkQiHRKXwrDeKkS_95GPUwA3mGEl1IzqFstZUvqMc7AOkI1HMMzqMNJ7AKPUcp616OPeOz5pbqK5IUV_8j0gY66ppBTE3ZxWeJsMxM01aJm5Puhen3sTarpxkxmZsGMFutUoFlc1WmtVDh22i4utoWUOsSUxHGmTtEW7lz5VDygagRhGyiuJZDEsPjWUfc77Vh797ivsTOuTBILfTHFs2c9CweLCIgJg9teKKUvQi5-CxiCc8HJOl__jAl5NS8gy1BDvLPpZi1wlMtUNgdkHTeDkDkvhjFC-UvM2dhbiwFrOSGelf4vcOuzyu5QTsfqWQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-WXpQ4AqSuRL296hKpHenFzlX3OvpzYUg3D9sU8A1pRAXN2pQnjyXsUctHMLRd8P2KJFMHWX1b-ZbP-bk4waFk-eMHbh27OW3NF7Ff4WuUTrSswGHfdYPX-x4xU2ENou6mytskF7XX9P-hBR31pXG5Q1T0umnR8FcvOPVrcDE8758MBgPU_grAgEwyCaGo_KOx5z-MrgqFve4df80fm3fP-aubDQeZf0WbkB6ueZhUuEeVS6iLm5djZuErWvGfsRJcjXMWzyG7i5mL60HyNHQtFhWvD-4eNgYhC-UkC4FF8sfchW75uL07w5NP_oR_jr14w1u3BCPZux18sLxSIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=otfFcKeWFNJhrGNQcMHDQAuHgPPp0S2gIZjPvbDqYeO5Vu6VyrnmVtlmX2DYlSbvNs_UgCfvncMo4xVNb-ftqgvYhInXJrGr0VtvLF5JX2eyfWpQiBY8WL1dKLyLt2thawT6FnkCfRu_GYdnRBkaPOp1bpdZGHXjNl50XVZHUGEVclrfGptYAeSKOGkX5tjSNgCgDX8UCdJ21dd9pATqXpaTvE7MSQqWWllC2OpQOSrEEAvxJNoFDRgFBFib_sezHtDUxhVy2cQ89meGTqGpB41a72nGQNCQA9uZqG2Q7HlqJR0mpkUY0LazcAK-6csbJweL4PuNhOYEob-x9d9xnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=otfFcKeWFNJhrGNQcMHDQAuHgPPp0S2gIZjPvbDqYeO5Vu6VyrnmVtlmX2DYlSbvNs_UgCfvncMo4xVNb-ftqgvYhInXJrGr0VtvLF5JX2eyfWpQiBY8WL1dKLyLt2thawT6FnkCfRu_GYdnRBkaPOp1bpdZGHXjNl50XVZHUGEVclrfGptYAeSKOGkX5tjSNgCgDX8UCdJ21dd9pATqXpaTvE7MSQqWWllC2OpQOSrEEAvxJNoFDRgFBFib_sezHtDUxhVy2cQ89meGTqGpB41a72nGQNCQA9uZqG2Q7HlqJR0mpkUY0LazcAK-6csbJweL4PuNhOYEob-x9d9xnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_gho_jXcixdvCGbmxzK1fjfP4aRMJKVTK5v9kh7PLjIcJNHBnvl5_AUp12_xndNaI3sice9hRMgnLHS-NyWlEziPZsfbi02_5muDiSDywzw_TMOO6Ecrf7TZ_1ytG1QS75ScVpvWTDdLe2Ihd-BGaxj1uY4bgiHADiSBvU5rrMKLJc-ZsJ2UCR3aRDoIzI5KzLH8mOZTQ5-SbnweBkXC4deTcr5GJTOTluIeCSmCI7NbYe7Mc4MtPhIQB21Tni2rA8Un4FrAtvTZeN915WFB4XF9Fm2IpX--QP01s4YNBEr2HMJD2wmIW-vQ6bHWfVKn7WiZotQJMi9xmrbMjrchoRsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_gho_jXcixdvCGbmxzK1fjfP4aRMJKVTK5v9kh7PLjIcJNHBnvl5_AUp12_xndNaI3sice9hRMgnLHS-NyWlEziPZsfbi02_5muDiSDywzw_TMOO6Ecrf7TZ_1ytG1QS75ScVpvWTDdLe2Ihd-BGaxj1uY4bgiHADiSBvU5rrMKLJc-ZsJ2UCR3aRDoIzI5KzLH8mOZTQ5-SbnweBkXC4deTcr5GJTOTluIeCSmCI7NbYe7Mc4MtPhIQB21Tni2rA8Un4FrAtvTZeN915WFB4XF9Fm2IpX--QP01s4YNBEr2HMJD2wmIW-vQ6bHWfVKn7WiZotQJMi9xmrbMjrchoRsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=fgr3rz_CcuNCAU01LKTMvYDyEi6g4J83iNaktC_ej0-mqtznES0U6q5cm0-WiqD3yAYzlzsxamjx4dnVaI0ZxALYE9p8iG6edLDsArplOQPbcYUgCv85IpNt4aJjfTRF-qYTAfNWBc7gVIW84mSs1N5Bq8-rcEVbzeML64fh-7NfngFapK94FxzuXcYOVl7NC3WGkC7_t1Q11gwpF1i_2Fu3BuaKR5mRvv48R9qeCvbNYlYRE91r31c0kn-zo7QyWTEGevHtGyLfbkzbgAi0dXO76U-0rd-Jo5xbje4C8ujxt7wuQ_EigFk0V6gt17TJ0AE8JqUSyzA1I2cInvonNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=fgr3rz_CcuNCAU01LKTMvYDyEi6g4J83iNaktC_ej0-mqtznES0U6q5cm0-WiqD3yAYzlzsxamjx4dnVaI0ZxALYE9p8iG6edLDsArplOQPbcYUgCv85IpNt4aJjfTRF-qYTAfNWBc7gVIW84mSs1N5Bq8-rcEVbzeML64fh-7NfngFapK94FxzuXcYOVl7NC3WGkC7_t1Q11gwpF1i_2Fu3BuaKR5mRvv48R9qeCvbNYlYRE91r31c0kn-zo7QyWTEGevHtGyLfbkzbgAi0dXO76U-0rd-Jo5xbje4C8ujxt7wuQ_EigFk0V6gt17TJ0AE8JqUSyzA1I2cInvonNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVaJLvGAl3DMspMR8Dw8wMCjDR2FZnhwZuJOE6rmyQpvOZOCWsOATv9th9ceKOYlCHWhBRNiYwcxQvDKxwfmeS8VfpYFhCiKAOk7xU7qHxGzxmVV20YXV8nqeSmr_2aEgtb86B4IRP5epFtTm3iYbZrbCkhiGVPQozRX2WtoLUhO62sJstTeoI1hbQ8ggMxcbbDTaK0yWbCSmNuyaJmCZOmcZfZF5UcaeFhNWapqlbHL_92MUWzPBI2JaI2HThn3n0ecjJRq93YP-2MR4jumqrcUIBB7bvllTxbk2Xw3SPyitd1KtUaf5qeuXeCICahUcyJOr_qTo4xaXEIwkQ68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ru3J__s7yjkG3DGVTkxcBtWqEkzlQbffbBYtSMAO32N_NNgjxCvD5jGdRtR4yeka4NwNKFC74VfBkvQdXm1RxQU8GPqAeojtCP3C59wlYfx9xTMjPL4FKF9EAmT5eDPBjx_0en1Yvxi0L3gNkfM6HvEB5KPczt_ifdp6zVwymDx2eeaRkBEQoWFPg5cxSVHc1bZZAHnar6Gfh17WQaMe7VNbdnJVbwayoMPjIAEWTVYp2jpvh1t02-QrAZ5G8LhilB_WIvaSoyezYhOCUkvT5BRp1-i2bdIRVbweNLDOm5WllEQEn3AaJM4-2gdWVwoqp6Om8WTDPe9AbSK6NAzNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=k7tmFnQ1-nq52Y-ZN-TyKypoKHqyJIYXLqUwhJTc7HDrbFltAvADw0dbdlVhP3ulbVhMYbkhvuLecIvk9LG_wGLZH0LKAK1kMrZt0tixWdxq1lTB0QU881q1B3WBcA8Lutn0xp9Hxi7MhEW1b0elqIpYT0oxkAgpzQFMtVrWzgfkmVvXmf8qBVBoTC-vaaFqnxEEfq704sqGeMS4MWi5VE_yreIWnFSRTrXagCsDdrn4u9n-gEssCcKQsYMZG66LwjFDL0RUEUEfJFJ4EAelhEAnfgrpOJRcZe6EoBeDsCmbd8W3mj0uCtPTt4NDu4EEPsBgRVwc5KEbaDbUO4K9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=k7tmFnQ1-nq52Y-ZN-TyKypoKHqyJIYXLqUwhJTc7HDrbFltAvADw0dbdlVhP3ulbVhMYbkhvuLecIvk9LG_wGLZH0LKAK1kMrZt0tixWdxq1lTB0QU881q1B3WBcA8Lutn0xp9Hxi7MhEW1b0elqIpYT0oxkAgpzQFMtVrWzgfkmVvXmf8qBVBoTC-vaaFqnxEEfq704sqGeMS4MWi5VE_yreIWnFSRTrXagCsDdrn4u9n-gEssCcKQsYMZG66LwjFDL0RUEUEfJFJ4EAelhEAnfgrpOJRcZe6EoBeDsCmbd8W3mj0uCtPTt4NDu4EEPsBgRVwc5KEbaDbUO4K9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=q06dvUA2zd4pn9P6-BgQN0fvOWj5o54KsaZJLlCYTR_AfFOFwqzzXdD1ey475VdrQu7ri01-MvogINZLGawNGOgXLIez5eZQeqV1uV7mIinGbTtUunLk6dRA6p1NpuZNEbSqzP0NWH2Rt1rbt1cFL7zWqaBw7eqUYGrIp31Tb2AogttQ4EF0-NUnimZSZky0SMcGOvd_lD4FAS6XMR9T_KU2PAEwXnmeLFlGQy996EFnIuwQBwO-m3KIxcy9tkHOeMRiL0mX5yLPVjvxhCXxRyUXg5FCUTUd9ZnsK3dJtC4eUyZm0-dcZjmH8te0wb39jHP304G3wlIjM1GRaqx_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=q06dvUA2zd4pn9P6-BgQN0fvOWj5o54KsaZJLlCYTR_AfFOFwqzzXdD1ey475VdrQu7ri01-MvogINZLGawNGOgXLIez5eZQeqV1uV7mIinGbTtUunLk6dRA6p1NpuZNEbSqzP0NWH2Rt1rbt1cFL7zWqaBw7eqUYGrIp31Tb2AogttQ4EF0-NUnimZSZky0SMcGOvd_lD4FAS6XMR9T_KU2PAEwXnmeLFlGQy996EFnIuwQBwO-m3KIxcy9tkHOeMRiL0mX5yLPVjvxhCXxRyUXg5FCUTUd9ZnsK3dJtC4eUyZm0-dcZjmH8te0wb39jHP304G3wlIjM1GRaqx_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=TGrmkBE_Lqfe0cHVVYHFuj5fLXxHRqw2XTw_eo6I8yTYHIyFQter2Nm1oKzCGXoSAL9olflEVarnUIMxKz0OMQF9k1jxU9TeqhbxCEVsrG8wtKBF0y-CBUpmrQf61nQOYTTJS2T5pH0_pZLcGsCG9v0r8PxGsQg_jAbghw94S9p5FjnYd3GrMBAMzq1eOkF_Olv7GeUSoDLjLQ60CZG3uitR3v_ensrB55WrZgWUcaEbTCiVtKfATK2ZNFv1eEqmT1FTEJiuVon0qjOqtZctD2IQ-YLfTyObtWVpeQ0Yi7LHEqmCgBuYrqQ_5kyOWMBQUyCs6oSwgioLUOKlFT_xtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=TGrmkBE_Lqfe0cHVVYHFuj5fLXxHRqw2XTw_eo6I8yTYHIyFQter2Nm1oKzCGXoSAL9olflEVarnUIMxKz0OMQF9k1jxU9TeqhbxCEVsrG8wtKBF0y-CBUpmrQf61nQOYTTJS2T5pH0_pZLcGsCG9v0r8PxGsQg_jAbghw94S9p5FjnYd3GrMBAMzq1eOkF_Olv7GeUSoDLjLQ60CZG3uitR3v_ensrB55WrZgWUcaEbTCiVtKfATK2ZNFv1eEqmT1FTEJiuVon0qjOqtZctD2IQ-YLfTyObtWVpeQ0Yi7LHEqmCgBuYrqQ_5kyOWMBQUyCs6oSwgioLUOKlFT_xtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=Jrj9T2_svbl0TgmvmVhXTIGMvohlicMNLIlUWgVCDK19_TEIqVmMWi0sT3LsRPFwKZ20kyw5avFicH9idA4107NZJUmNZQWg_jz2s1gcAl8RzPhf52e_Jb5t-2SuOly3YKo5RQmgrum2ZtmyVG4QyVopWIsrLUvxAYxs7noagf_dZD4cfd0VcgXyjB6PkFksAnUtleul629fOMUx8JDAPg--UhVhvpsiLAg5NyvqBKrNdfKGjXfRqnrS9I9xGeKOLkND0pRvA4JyiWAGpe3PmRy2WvVIuZrflmev1N1TvumCk2-q6X7pOaiL4gt-EQq0_WJnp15qRMk2_Wqm09ssvHIlG-kBpR-7PRdtqe8I-TJJmnUcMPw2jgHYfI6d4EjXGXoFYziCv6GpxZKviJSjzEUa_EODnDBez_Rd2qEHcogcRyft34DRoN6yOZ51CGIWlJ7DduqFyEbWfUgXWJTNlF8l1gj1rg58TkkfMJwsjWknJDnkl2g_Xf8WBLtMAYM-YKTalNrNcrEFnefblh4o25sIofh67fJYDrOYsYEDaJr8V9Br9S0_c2aev0r8fSF0OtY1Mz7sj7Q4smJHble3LiZS0D8zCVUSSCysAdLY2vdZcXmarfGIPySoR-8XgkACN4OL3apszlQwi4wGf1j8_Vb6YB9IKvbRd0X9bzXWfiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=Jrj9T2_svbl0TgmvmVhXTIGMvohlicMNLIlUWgVCDK19_TEIqVmMWi0sT3LsRPFwKZ20kyw5avFicH9idA4107NZJUmNZQWg_jz2s1gcAl8RzPhf52e_Jb5t-2SuOly3YKo5RQmgrum2ZtmyVG4QyVopWIsrLUvxAYxs7noagf_dZD4cfd0VcgXyjB6PkFksAnUtleul629fOMUx8JDAPg--UhVhvpsiLAg5NyvqBKrNdfKGjXfRqnrS9I9xGeKOLkND0pRvA4JyiWAGpe3PmRy2WvVIuZrflmev1N1TvumCk2-q6X7pOaiL4gt-EQq0_WJnp15qRMk2_Wqm09ssvHIlG-kBpR-7PRdtqe8I-TJJmnUcMPw2jgHYfI6d4EjXGXoFYziCv6GpxZKviJSjzEUa_EODnDBez_Rd2qEHcogcRyft34DRoN6yOZ51CGIWlJ7DduqFyEbWfUgXWJTNlF8l1gj1rg58TkkfMJwsjWknJDnkl2g_Xf8WBLtMAYM-YKTalNrNcrEFnefblh4o25sIofh67fJYDrOYsYEDaJr8V9Br9S0_c2aev0r8fSF0OtY1Mz7sj7Q4smJHble3LiZS0D8zCVUSSCysAdLY2vdZcXmarfGIPySoR-8XgkACN4OL3apszlQwi4wGf1j8_Vb6YB9IKvbRd0X9bzXWfiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlRtBCHtUqeSEXT6Ntl5svNtVmd-6cUVoxDGt7bnAUGYANYDzYfac3hO4BLmNEdceEB9_ZHOmPq_K1NQVP8rDzf6eN0l3K6IqjxU10m0prfrBVXHlrBP8pzvsOSBAQG_yvaN15aT4QADQzrSPU1-81KRt_SwbPl5Nr0U453LXnezy8jM-CIcKy5_iHWG8ue1RmXVS2ZgnnJ56a9zuj75JBz4wtAnMVq3l4ZxRs93pfUh9HcZTPKzx3rDo7bmnhVPlMT4tQZU7VXVwHbgUa6RwroVG1TCQxLrkfYZT6l0ehRlOVsguhgL2DCJnmLsozk-dIDJ7-D4EjDoEKP_IIK8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYHMob6285KmAALkmOgPY7bx2V6TUV34JbOX7M9RmgX-r9uQ1TbUiG-KXBGkC_NPgolS3TYVLTw_Oz1pc8vge6WSR-I1Lvmvs6gUqelIDGNaaeUn8mnK7-jJWaaXQgOvpF_c_GfrP1W1TIR_5wHZF8RuLbTCUgHC-egVce940EIJj66pCDwrSgZPjkKgji5S35EsQFFHyF1mSxylpYGGuh2xd2vMEyxUP28wvD5OS0ITQBkRE2hluUCVqjbcOuxyhiYA4NI9FTn45RUZb6aDZGaCISJJErEEKp0Zus_u9LJcB2_nxad32AqdU03aPAxn5zshVT7EP6HT0k9aQbInAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=f5Uza2EVUJF2n8anwd-FS4HSB_JctgwR1jULda1n2abXAqG1rANfYqj-E9E3z-HJcKLgQSFFxHCyV1jt6QzFqOMCMC-qlzBznF8O3lOR2LePHEJi6bzkrsRLk7RjTNQ6YlfATxUa2NV-PZYUP7tOd-4Rs9_gDa4pscZ3x0Gw9TeOyA68hlZ3Dh-STn6vWelzWzdrvbUkTdQ4cDLU91hBP3uSkHOI7EFXhjRJEKyK9lgP_MRt5Ek1_aOEQqXQXNdQoQBhN2csB-062mO8YR7cNTho8p1pZ9eYJ5mjwO3S5eIZ9HU261rPsxBqiRY8_-zO55uBREmT33iwW0jiib70_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=f5Uza2EVUJF2n8anwd-FS4HSB_JctgwR1jULda1n2abXAqG1rANfYqj-E9E3z-HJcKLgQSFFxHCyV1jt6QzFqOMCMC-qlzBznF8O3lOR2LePHEJi6bzkrsRLk7RjTNQ6YlfATxUa2NV-PZYUP7tOd-4Rs9_gDa4pscZ3x0Gw9TeOyA68hlZ3Dh-STn6vWelzWzdrvbUkTdQ4cDLU91hBP3uSkHOI7EFXhjRJEKyK9lgP_MRt5Ek1_aOEQqXQXNdQoQBhN2csB-062mO8YR7cNTho8p1pZ9eYJ5mjwO3S5eIZ9HU261rPsxBqiRY8_-zO55uBREmT33iwW0jiib70_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=kHBCWJwMH2WLW_dPv88VG-0JXLUwyTz_o2BpcUV5p0UxbTRmo_nSXFZR_IANSJnzsMKBc7-J0MzF52KNM2cUauyl1ykoGl4R0VdRbonDSfKRPu_XHts5kLoA5BuVTlMf_WVh28ztgbjac6ffE7fdwBo-X4ndDwaALzpe7q6PlQkT9FNaBWO1rZwy6QZXuEVFEWbJ_OtMxK_wEsF1UklZXwMsme1isShug1L7fqVxycdCGckgdx1nvItCvL4j_OxgbHruT_UyJ-HdqN65GtMY1Jy8UTAf07vc9wP2_HTR-AxBmSz48rtHSHTcN4MxcW8daMz8NwYW1jHMi-LIpwTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=kHBCWJwMH2WLW_dPv88VG-0JXLUwyTz_o2BpcUV5p0UxbTRmo_nSXFZR_IANSJnzsMKBc7-J0MzF52KNM2cUauyl1ykoGl4R0VdRbonDSfKRPu_XHts5kLoA5BuVTlMf_WVh28ztgbjac6ffE7fdwBo-X4ndDwaALzpe7q6PlQkT9FNaBWO1rZwy6QZXuEVFEWbJ_OtMxK_wEsF1UklZXwMsme1isShug1L7fqVxycdCGckgdx1nvItCvL4j_OxgbHruT_UyJ-HdqN65GtMY1Jy8UTAf07vc9wP2_HTR-AxBmSz48rtHSHTcN4MxcW8daMz8NwYW1jHMi-LIpwTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN7uGYsz7IOQwrIVXwYKFUecHm5DEIYuKVBoexPqm6IZNeYHGRqGNodx25MgAw4xIJEBhLzbQTVB_IS-BE_ZTXnK94ATFIzVDzI2YUilaveRZy33ifUDNcyLgsLS23c591pgZNAAsypSEzS4J3FGDLsh-GSdng9NzGUIxFcJPajNmShk4mFO1FLs-68H9fFFNeIxmoWhiskl1oqdLQvWWB-cN3F1aAg87Vdjl46OtW4Iq97at6HiSwLhsSxYmWLHhzLaIuKpSnmFdHaR7EcHflI9pJCsQFG4XwSDqaxxufIZlguDnM8tm9OT-6grZf5nIjoJ7R7B95f1q1rgAQs1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=i_yX938_u3qL4QEbtA3oEy7zeqyEScV6xm4nm3xmJypiInp4D99x2mTnWfwgbzf2ESU4qlZoGE7lNav2lkKUamD7e38t1OinfRMGAu8FJ_fn_ON2RwOewN-5Z9JCZdHmx9sn4M2FO42E5trUyiR1lbEbJOQEGmaUd5Oy2KseNt4cjLWoF8IuHyaV0VzBczkHK2oTUj1RiroROs6cOsfw8FdGsIHefi7guoPbr0_UswXc5zOTTlsduCaOfadRN5twbdXURFSwA2j16Bvi3mAV-rtwJh98qeHaYaj9FGK7eSyR6ZQaQOU4fLVcTuYj3fWytl1CBCrB-iGwEdtS9PDIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=i_yX938_u3qL4QEbtA3oEy7zeqyEScV6xm4nm3xmJypiInp4D99x2mTnWfwgbzf2ESU4qlZoGE7lNav2lkKUamD7e38t1OinfRMGAu8FJ_fn_ON2RwOewN-5Z9JCZdHmx9sn4M2FO42E5trUyiR1lbEbJOQEGmaUd5Oy2KseNt4cjLWoF8IuHyaV0VzBczkHK2oTUj1RiroROs6cOsfw8FdGsIHefi7guoPbr0_UswXc5zOTTlsduCaOfadRN5twbdXURFSwA2j16Bvi3mAV-rtwJh98qeHaYaj9FGK7eSyR6ZQaQOU4fLVcTuYj3fWytl1CBCrB-iGwEdtS9PDIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=nzk2xbzg_FKTTBenxYvb-WhSYWqwCf8ph48WamZE15kv4LVz0X1PyWmvbSZPkEjICHkVPBvSz71FIN6jPT1gJWSkqslSX3tmkX_Y54GztG7uOZ2kV1-p_faAEhX-MP21QpQDNdcLQFBegeO5XyF5my927COtVnikd7rHygVyww99kCqbEUF6g0PlPZkoVqkGvz3yVXo14hnV4tddJwAlcKVg50fqBxDbtVSNPonsp3KRv7xtHEoNR73-n8z-attrnDqtYdVoB1dGIjvkN_fic97yQuu9Z96aq3HLziBnGI7MbbbM21PZPPEyHn2nFnIvn0dh_Fhc5ej-mPX7UM2nOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=nzk2xbzg_FKTTBenxYvb-WhSYWqwCf8ph48WamZE15kv4LVz0X1PyWmvbSZPkEjICHkVPBvSz71FIN6jPT1gJWSkqslSX3tmkX_Y54GztG7uOZ2kV1-p_faAEhX-MP21QpQDNdcLQFBegeO5XyF5my927COtVnikd7rHygVyww99kCqbEUF6g0PlPZkoVqkGvz3yVXo14hnV4tddJwAlcKVg50fqBxDbtVSNPonsp3KRv7xtHEoNR73-n8z-attrnDqtYdVoB1dGIjvkN_fic97yQuu9Z96aq3HLziBnGI7MbbbM21PZPPEyHn2nFnIvn0dh_Fhc5ej-mPX7UM2nOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=sKzUxbCSc6NHzbisOEi6CwlWA7ZUA3eZY3xXQ3hwRF9PYdVwLBT7K1QbUy_vlhFX0p1ZCjvFao2kLPax52G3tl_x1M6iPKvtiNCp9IipAaEU_WEQF5UB8gQywNAUKtHQth6Udm-B4FEmYT3PZ2-7m9rL3vGikWR60KLAKaJaAaNoqCgX5MLQcmHzbEEnGpVBk8xgPh040N2drhlBDMPmkvUYxuKR2XAskQrTcmFhIOUnCsnEi4_wQpVgdcPhzitHdO6i4s0yCPU9oFzkNYZFWbxLcBo9LRZAQccwAXq_em-4sFGyjDuHOOHCmwdX6w0iJ6ARZt78nOn8Wdgm_uoqSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=sKzUxbCSc6NHzbisOEi6CwlWA7ZUA3eZY3xXQ3hwRF9PYdVwLBT7K1QbUy_vlhFX0p1ZCjvFao2kLPax52G3tl_x1M6iPKvtiNCp9IipAaEU_WEQF5UB8gQywNAUKtHQth6Udm-B4FEmYT3PZ2-7m9rL3vGikWR60KLAKaJaAaNoqCgX5MLQcmHzbEEnGpVBk8xgPh040N2drhlBDMPmkvUYxuKR2XAskQrTcmFhIOUnCsnEi4_wQpVgdcPhzitHdO6i4s0yCPU9oFzkNYZFWbxLcBo9LRZAQccwAXq_em-4sFGyjDuHOOHCmwdX6w0iJ6ARZt78nOn8Wdgm_uoqSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=bsXQsgDqUk4ALXGOGdvW-3gthCHIe8M3QYimmYoAaNggBjFe2FvgaxU9rzWVBx_4qeHqjKpOcwHG4io_DPlPzzmVw-rbIRnSQ5fZyusJFd7Hd8g6pt31LJfnK7EoL4igBY6FgWRAvZk5eksYvR52ox_cnv1MpeTNmVDJq_e2MdFereOsaqYbsyyCH60zX1_zk4YLUMlbmflxuUZU8revg8IKmpT6tLF7uBporn0zHE5kXhlorhgX4EBxCu2nzUt3RgyT6ToeqmpOPljJStbeNZ_TwFTNHhVLkXWYl3xrR9RD8WMdZ_xTHLNFds53_UI0jw9rlthByM1Svsv-yD48-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=bsXQsgDqUk4ALXGOGdvW-3gthCHIe8M3QYimmYoAaNggBjFe2FvgaxU9rzWVBx_4qeHqjKpOcwHG4io_DPlPzzmVw-rbIRnSQ5fZyusJFd7Hd8g6pt31LJfnK7EoL4igBY6FgWRAvZk5eksYvR52ox_cnv1MpeTNmVDJq_e2MdFereOsaqYbsyyCH60zX1_zk4YLUMlbmflxuUZU8revg8IKmpT6tLF7uBporn0zHE5kXhlorhgX4EBxCu2nzUt3RgyT6ToeqmpOPljJStbeNZ_TwFTNHhVLkXWYl3xrR9RD8WMdZ_xTHLNFds53_UI0jw9rlthByM1Svsv-yD48-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=TSTKMUaW7Lrprdn-r7Go5MgYM1j7bs3gr-zC6e6xNjNppQp31EPHeMqu_bvhz6k2bDRIkba6UFmezJtwrDX7nYwLL6_NX3iDuZ8KIkHLqylkIgxeHpPfZxAjvvkSuCP4-lpyRrBWd7KRroQnkgdllSl1ZOKTp480Ql-zvog7ksP53e54QYNg5imX1ivPnLqt_41anRJb0dFA0AlUv5ClZIA46YKavZ6rQ7o5S4WP7l2zl3CAvPwlTWmaOd7yTnrpfV240Ql41BGLZ1RESzHyPfxRWqS_7WUSEB67MmLfAKknpfJ4IC_iEQrOxLxz7XI9-Rhr_06HSEUBPWwDKL6ZVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=TSTKMUaW7Lrprdn-r7Go5MgYM1j7bs3gr-zC6e6xNjNppQp31EPHeMqu_bvhz6k2bDRIkba6UFmezJtwrDX7nYwLL6_NX3iDuZ8KIkHLqylkIgxeHpPfZxAjvvkSuCP4-lpyRrBWd7KRroQnkgdllSl1ZOKTp480Ql-zvog7ksP53e54QYNg5imX1ivPnLqt_41anRJb0dFA0AlUv5ClZIA46YKavZ6rQ7o5S4WP7l2zl3CAvPwlTWmaOd7yTnrpfV240Ql41BGLZ1RESzHyPfxRWqS_7WUSEB67MmLfAKknpfJ4IC_iEQrOxLxz7XI9-Rhr_06HSEUBPWwDKL6ZVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=LFRaaopHlclpYbUL1OVpOkLY-aJ3LnBjT7P9RijI4liAF5XKiDjGZM0YaS6tiEJXuwgbHfmgjoltAupSUXfetKlWcM72r2G_BYR3zv9oZLYDAuUZUSqzNztJIf1XVkczHQswkiuP6D1r-ZaevkNJtwPiR9KI3DTIIW-87doK7lQIW9uddW3dAgsUQGlTg3ZyH2e_apSf4JuRDL3_LA_7mVwlwrWy6iov-rP9h-DgjCEy9NGPGdtMX0LX9FE6TaDXWBj47RcxVqcnIcoaDhXuCP4AIRTE-yT8SqbVAVgeOPV61C3zXsvimIMmUE_tE_Onhn9jyB8D2ksX39DrvikeCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=LFRaaopHlclpYbUL1OVpOkLY-aJ3LnBjT7P9RijI4liAF5XKiDjGZM0YaS6tiEJXuwgbHfmgjoltAupSUXfetKlWcM72r2G_BYR3zv9oZLYDAuUZUSqzNztJIf1XVkczHQswkiuP6D1r-ZaevkNJtwPiR9KI3DTIIW-87doK7lQIW9uddW3dAgsUQGlTg3ZyH2e_apSf4JuRDL3_LA_7mVwlwrWy6iov-rP9h-DgjCEy9NGPGdtMX0LX9FE6TaDXWBj47RcxVqcnIcoaDhXuCP4AIRTE-yT8SqbVAVgeOPV61C3zXsvimIMmUE_tE_Onhn9jyB8D2ksX39DrvikeCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=OOArbPR3YpZLlM4fRHIkL461ocHyOgiV_gHzAaeHWs7ub1HpEw61LaefJIQDBOrxAG4mRSvF8VNBAeVQDyB8LHIouu5p4aB9XgAADpvfaj7ejvsua6BfQyrThdveji6YN91LL-gpkaX391CB-VPGluORAnsecYZFLwhR5-HZimrnvjF6JcvtzbEhVlAEmRDWRRKzspAKyjDr7qT9bddpxJwowUeLV31WlHoUBLMP4vdYHgEO-CGlSyR0MJtzq1e5VG7XU1MrHer_-lCrqq-vn0iJTMnN7YwXP5v0lgIZibVNOe2iQoiIzztQWU4BO2ChIkzpaMivcnI_ZMynjrM2d4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=OOArbPR3YpZLlM4fRHIkL461ocHyOgiV_gHzAaeHWs7ub1HpEw61LaefJIQDBOrxAG4mRSvF8VNBAeVQDyB8LHIouu5p4aB9XgAADpvfaj7ejvsua6BfQyrThdveji6YN91LL-gpkaX391CB-VPGluORAnsecYZFLwhR5-HZimrnvjF6JcvtzbEhVlAEmRDWRRKzspAKyjDr7qT9bddpxJwowUeLV31WlHoUBLMP4vdYHgEO-CGlSyR0MJtzq1e5VG7XU1MrHer_-lCrqq-vn0iJTMnN7YwXP5v0lgIZibVNOe2iQoiIzztQWU4BO2ChIkzpaMivcnI_ZMynjrM2d4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb4SPMh75Gg9Y04Y6ias4Q1nEkPcVSE0dLeFhhpQIi9xbNJfCSvJJCejIYjma9b054TizTzoTYfgL_T9b_LuS0JKsxC0r1io82guxFlyFZsEgUOWd-hLLdJ_mJOpM_heWjkTb27iNld9NKulHILflpVP3-yRlPT24o-o-HX7PIud9MgN5eYk6_Xug19OBGPJnn1xs1dwVPiU23zKoNdR4-Jv7Hs19zq977vWYa1vKSsMB0XU8WjjdENJETDu11Wmk-A5Q07MBQIh4jOQbD1Zd1jPfnScPVYWutXmwPsufb_WGjH3QBvCegB-dy2cwv7wazZXhcSTOW13dLIt9TIBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=dJW6fgbY60tVr9O3l6LOhu8flsELMjn1CzpxJce2YhLaZV23lYllUaoO3kTyAP9S3ytR7JjIN71SWWbu22hQQtVGIqCq6VVpDqIx69NMy-rCJejVX8lzHNTMk8-KxL3qstF8VEufQ2LFaymy8W-Te6hZ7q5vhuu1cXHK7C4AAPhLagHYH8ZH55uFeWKqpIdNhhCcVHsTa_hyt2XSQiqQ_xyafp6w9lMuCes8JemThRqjfLXo9gi_NkxfHTIw_l8ZdKvz-NJxcl9317Qm39uX4EO3mfN8rpr2x0gjv69dplKnB29_Z38MEg9oXYuSdS5fQd2QDbR3AYOjGRLqEFAVYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=dJW6fgbY60tVr9O3l6LOhu8flsELMjn1CzpxJce2YhLaZV23lYllUaoO3kTyAP9S3ytR7JjIN71SWWbu22hQQtVGIqCq6VVpDqIx69NMy-rCJejVX8lzHNTMk8-KxL3qstF8VEufQ2LFaymy8W-Te6hZ7q5vhuu1cXHK7C4AAPhLagHYH8ZH55uFeWKqpIdNhhCcVHsTa_hyt2XSQiqQ_xyafp6w9lMuCes8JemThRqjfLXo9gi_NkxfHTIw_l8ZdKvz-NJxcl9317Qm39uX4EO3mfN8rpr2x0gjv69dplKnB29_Z38MEg9oXYuSdS5fQd2QDbR3AYOjGRLqEFAVYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=FO33d6uvV15FmzOT9zxjYzcbIIP_StodOm-9BLRm0L-yRqy4NlqF9LTK3t7pvk17bfbwIJ7X4KF9VI7pON0esufF_QHxIgtmXMh8MDmOKozYsvH92THzP7NDVosHaDlxO4KFeLYHYugIsXnnv7cSW43ceJozfh4VpVYnSyeOJ9ubhmEt_tvLt72FibbgPFzmqAyUUuODhUZmefxQiUyRdSVGFio9qQHS2BkYY6WGsuqgg4ZniA_-CW3IziIv3aw3wc2AFbvZ2W63QhP3Ribt7U1MNiAcQglkqQEweBpyx_qClk_fLy4ZIywp3izpMxB_f-zUEgZAIdPxEYLZypFiw5z4xa2bwRRiZmvZ_lfgupKgbrENkHmc4eWdO5IENrhkObCv7o31WPmpr4wzxR9u4I-J15MMycxjdy0PPknvfVtEMpS4khqv_PEe-H-2YSmE78czDobVOjGaPC9mPxV8pqnxG3gU6bRMWEZKWM4m1PHBzwBRafG2xLYZyW7WeK2w_FEwpr6bs5rBL7W9e1J6GpAwOv1X_bNZb2i1TMG0IulMid5u7tqSyotxbZdA5biv3bvu4woLt-mEbKzH--DChK-becCzFz1GLrn5zXDHDWxwYHhjIr8Yajm_YdD9hf6SY_KRhXXnMMb_hHyVs6zejzGxuO87DKHPO9GVXriiEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=FO33d6uvV15FmzOT9zxjYzcbIIP_StodOm-9BLRm0L-yRqy4NlqF9LTK3t7pvk17bfbwIJ7X4KF9VI7pON0esufF_QHxIgtmXMh8MDmOKozYsvH92THzP7NDVosHaDlxO4KFeLYHYugIsXnnv7cSW43ceJozfh4VpVYnSyeOJ9ubhmEt_tvLt72FibbgPFzmqAyUUuODhUZmefxQiUyRdSVGFio9qQHS2BkYY6WGsuqgg4ZniA_-CW3IziIv3aw3wc2AFbvZ2W63QhP3Ribt7U1MNiAcQglkqQEweBpyx_qClk_fLy4ZIywp3izpMxB_f-zUEgZAIdPxEYLZypFiw5z4xa2bwRRiZmvZ_lfgupKgbrENkHmc4eWdO5IENrhkObCv7o31WPmpr4wzxR9u4I-J15MMycxjdy0PPknvfVtEMpS4khqv_PEe-H-2YSmE78czDobVOjGaPC9mPxV8pqnxG3gU6bRMWEZKWM4m1PHBzwBRafG2xLYZyW7WeK2w_FEwpr6bs5rBL7W9e1J6GpAwOv1X_bNZb2i1TMG0IulMid5u7tqSyotxbZdA5biv3bvu4woLt-mEbKzH--DChK-becCzFz1GLrn5zXDHDWxwYHhjIr8Yajm_YdD9hf6SY_KRhXXnMMb_hHyVs6zejzGxuO87DKHPO9GVXriiEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=sB5aBeSXc83Nels41Kn8mGcDU2xC41voMZqqOqjer1rDj7DztfLS5vlY3srTD09nMR38fdTt2Uv4I-YheK7CVje4HSEFU09LQqUM710bYzwr0VLJwMupMgBlMThx_gTusohoOmNrYYzRdMnv_j90GI0QyyLXg7g9O2tt4AN0Ah3ZtPzivheTqnGWDYXKmX-k-RyrJtDtGGFHurr8jkA9GosUKpNrY42ayulQljb2prDX6qSPmp2zumFB3pDxCxPJp-EKaGSjeKrevsnxYIYKrVLal7uh4wndg3a3KoR3oofwMR48AD1qivi7ByVJfNon2JNdhY_wRde33PDKCy4j1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=sB5aBeSXc83Nels41Kn8mGcDU2xC41voMZqqOqjer1rDj7DztfLS5vlY3srTD09nMR38fdTt2Uv4I-YheK7CVje4HSEFU09LQqUM710bYzwr0VLJwMupMgBlMThx_gTusohoOmNrYYzRdMnv_j90GI0QyyLXg7g9O2tt4AN0Ah3ZtPzivheTqnGWDYXKmX-k-RyrJtDtGGFHurr8jkA9GosUKpNrY42ayulQljb2prDX6qSPmp2zumFB3pDxCxPJp-EKaGSjeKrevsnxYIYKrVLal7uh4wndg3a3KoR3oofwMR48AD1qivi7ByVJfNon2JNdhY_wRde33PDKCy4j1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=d2f0hWy_2YZcjflhWw51nJWaBZkwYyLjP3sfU5R10Aag0cZVrKfT5AboxGUYCU_1noR-H9zSo89hIZqPs1bv7EpcBK-tYHRNgg_TyVUwXhkiv1nJh2MGIaZBgPj3xQfeXe9U6delU32kk6JC-lQLCnrcHFSB8mVHIBkY4Ph7qvOAasDRenzhBSlRw7ZbY7unRS_J3vBsiUGHX0EtZvGRSSv2KnjtQ1sc6ctDdNRq2dzYmfBt_igOQZycSPX-Kyx2UIvWKct80y78eEYnCq_8_fjsevoa6gB6Voo9mrwRvRjx8UzOz9J2KGJQl_XLzcbc9lIZtvm8hV5RL4Dx-ZoU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=d2f0hWy_2YZcjflhWw51nJWaBZkwYyLjP3sfU5R10Aag0cZVrKfT5AboxGUYCU_1noR-H9zSo89hIZqPs1bv7EpcBK-tYHRNgg_TyVUwXhkiv1nJh2MGIaZBgPj3xQfeXe9U6delU32kk6JC-lQLCnrcHFSB8mVHIBkY4Ph7qvOAasDRenzhBSlRw7ZbY7unRS_J3vBsiUGHX0EtZvGRSSv2KnjtQ1sc6ctDdNRq2dzYmfBt_igOQZycSPX-Kyx2UIvWKct80y78eEYnCq_8_fjsevoa6gB6Voo9mrwRvRjx8UzOz9J2KGJQl_XLzcbc9lIZtvm8hV5RL4Dx-ZoU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=l-xgEy_YXZ9Ywm6z4Epj4fBEoMBLTbxguZk49BBoDAHgEjIu2iu3-aK6tUorWU00FyANR_G5U-cqOGlde4RkQ1WeU2kg-I9sTSicn-n0OWaQBbN2jn_PMj0Q0zNv55K0oA3QRSizAR8DQiK5rimIesAIRa9QrEolQliS1Gh7g9QT2fPgGsSA-t-KNRBu3zY1mxmEg4O45vrvz74U5yvlO8q9tbXkVFF01LlDhs6yBc3HFnzlPgBVxOjMyo2QaOKRLMoXUIhN2ywf8mYQyLN7egXLpfH5oHBMqqtvCSbp2Dt7g4j2PFvFpZ3-_Y8xwm2sOgg6wxZ1C_bDDjQT_urv4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=l-xgEy_YXZ9Ywm6z4Epj4fBEoMBLTbxguZk49BBoDAHgEjIu2iu3-aK6tUorWU00FyANR_G5U-cqOGlde4RkQ1WeU2kg-I9sTSicn-n0OWaQBbN2jn_PMj0Q0zNv55K0oA3QRSizAR8DQiK5rimIesAIRa9QrEolQliS1Gh7g9QT2fPgGsSA-t-KNRBu3zY1mxmEg4O45vrvz74U5yvlO8q9tbXkVFF01LlDhs6yBc3HFnzlPgBVxOjMyo2QaOKRLMoXUIhN2ywf8mYQyLN7egXLpfH5oHBMqqtvCSbp2Dt7g4j2PFvFpZ3-_Y8xwm2sOgg6wxZ1C_bDDjQT_urv4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=DGtfUTjcSAbmodbz63c3nbaLEs_Aq0yalLNExILG6uuw8geY8DmylZM-j51E6aErvEkC7U0h_nXz3cYGqWDviaP4fjR9XrE8ZdGK60eJsIYOqZiyH197BCn2sdVjh5EwZC6W5Fl68OqfipDT3jeUEIdcILypuILZkT8bbj3YCq8mnjWat38C1YWMjqtpa4PTL8b1146B49StnggAe8jUrCFtGGtQdvMbvJ3ioOlE19uU367XsK_mi_gbMiCvPybWTLy3Klm4axkerYiNTVleT62Jpj6LBcnEHhVt5Nxb8wZCQyQnDpQ6xKTsCfjURiGmdAkYRvs4JB3dxjqe05r7pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=DGtfUTjcSAbmodbz63c3nbaLEs_Aq0yalLNExILG6uuw8geY8DmylZM-j51E6aErvEkC7U0h_nXz3cYGqWDviaP4fjR9XrE8ZdGK60eJsIYOqZiyH197BCn2sdVjh5EwZC6W5Fl68OqfipDT3jeUEIdcILypuILZkT8bbj3YCq8mnjWat38C1YWMjqtpa4PTL8b1146B49StnggAe8jUrCFtGGtQdvMbvJ3ioOlE19uU367XsK_mi_gbMiCvPybWTLy3Klm4axkerYiNTVleT62Jpj6LBcnEHhVt5Nxb8wZCQyQnDpQ6xKTsCfjURiGmdAkYRvs4JB3dxjqe05r7pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXT4OOSmiLIbQSIf3yfl-ImLwafTqwXABmzUFSwPeSLJM81lUzyZdjvFFYDyGWAIoFqF8_Ftj0S4QdvXcSm6YFOOgi9ztXkcqYpX9WmyIHMd2bcET3yTAJ3RxlEXMaaE0KlLt4nH8mUqUCU5uOqosfp2esJlQIrv3-3DaiiXOtbCfUAsZ4rE5KvAkdSwccJ5PQ_oFJr6FvdQK-XOsp_v0BQb5pRS_V1GAhS6uTYERQL-NF0dID191SUUG_N9ACujcdP9rmuCZwHeelfZ7esk9o9P3sP8tkFTKGsrY64aIryZPSQg-4frtOrCOkfSUHXaY7oOr6X9Vj4rNsK7pfvqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKaXQ6Mw2eEDZ-iQlVGG3BJ2xkmo8FCrmKn2xyFkjxoE1PgacrfUtVeo5war37dOKyQ5aUxT_m16KcqmExFyO7PtOl7KN1vV7Kz9KBcbBUwry-LF9JXFoUpAEBiN3dgpgeOqT6IdAt854sfpTkh2j5wV4fR9VEnNha3N61UHQz8DhHctdRn8Tcs_JKjKI9miJdWqMApywCJzAxIU5jLF0vKq_xUAXgsXMi7CqjL8hE7sFaXCqa8NMp4fo1nv_9JY6frt52iifZGpPnnlbHMzaYh61FpzUbTDwCjYXWI1j8Qjb6zGxoy03pd_BKpmNqY4Kc_9l2l5IiVx2Kju8-_bqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=W2fQkn4X2IxWzo73fJLbDLxiuErliLQyt_UNKO1j1iViPqnhQxbpbf5uxaE3TGxWr9N2Zr1X5cTu0wREWEERwZFe0pbADmB6YlQnuNVDiK2pjwSLLns17pjNI3WoPev9BSDIvZLXUpY4SM82iJx7oPmjP29mEq3f-xFS2ZnKQocs9OJI-Oh-i-tOYQ08MK3MQAW4tJ3m_YYJ3cnOTBKdhlVjTjoiL_D5xz4nww6QwZvSf3xOpUVGWjnAXdjLnU5qVy3_xVm96_r67Bd0-6FvLNJcPYLpCi2VwJ8fCWs_F5oapgQLneuvbt0oUFX_IpmTgAAEW7T6exPnsr6sDwfsPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=W2fQkn4X2IxWzo73fJLbDLxiuErliLQyt_UNKO1j1iViPqnhQxbpbf5uxaE3TGxWr9N2Zr1X5cTu0wREWEERwZFe0pbADmB6YlQnuNVDiK2pjwSLLns17pjNI3WoPev9BSDIvZLXUpY4SM82iJx7oPmjP29mEq3f-xFS2ZnKQocs9OJI-Oh-i-tOYQ08MK3MQAW4tJ3m_YYJ3cnOTBKdhlVjTjoiL_D5xz4nww6QwZvSf3xOpUVGWjnAXdjLnU5qVy3_xVm96_r67Bd0-6FvLNJcPYLpCi2VwJ8fCWs_F5oapgQLneuvbt0oUFX_IpmTgAAEW7T6exPnsr6sDwfsPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIHbcYTei9JbHX1z9ULKcOPf-FFFRG-VR8V88kxKMi1nP9lktvDvIyo0kdnXFpsGBoTwe15n-8GMKaeSk8sHM4mhIK_M8793pN6S24rcXCM4BI7GLZ4PyGjP5dLCWwq-fAxrKhysF9PH4BQmkCYW_gbhD_XVP7FhleYIvtF_KZlhWwuKdn3CKoLzfdVq7pXCtlNPp7y7-0_ELmTTGA_wafkYk5H8fz5hSFW0Z_alD79qi7yaiDfTOeSusSkAadClrBJARXO9s9xS54JEPdfLS5LHJy_oL3Wj2ZTQ9iU9jOEyOPK2LwGc4BcHAu5TSHfVQuTfBCB3Hurrne7LuQg0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=fQemV30vNnRIf7W0bR8amfKsHaBiTAZilFXzHjgHg-R0YGcfr4W64qJmOiHGOC3he4-dvUyEmeZ6HnMLJq1OShdWfXRBr5aL8EkbM47Jyhp-wZM_tQZv2WO_5SGRdWoJN2EbJntJknHeWD9-wpDdbAe6VuresxoBTyhfDDvRv3AxJHoPyBrgMAdscxV-XbxgJcopMOX_1Y_BLI7NlAugwgS-T_u71owoP406CRn-U7h4XNm1-SSx-5YVWXINGI6VL7RCFu7wI4ce0AFjgE9Q48SRLctZhGJFpOlpi59XzZ6o-HwYJpQQvKAKIxHDIw6rTDSwJs9YqF0a3xk3ZE7RyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=fQemV30vNnRIf7W0bR8amfKsHaBiTAZilFXzHjgHg-R0YGcfr4W64qJmOiHGOC3he4-dvUyEmeZ6HnMLJq1OShdWfXRBr5aL8EkbM47Jyhp-wZM_tQZv2WO_5SGRdWoJN2EbJntJknHeWD9-wpDdbAe6VuresxoBTyhfDDvRv3AxJHoPyBrgMAdscxV-XbxgJcopMOX_1Y_BLI7NlAugwgS-T_u71owoP406CRn-U7h4XNm1-SSx-5YVWXINGI6VL7RCFu7wI4ce0AFjgE9Q48SRLctZhGJFpOlpi59XzZ6o-HwYJpQQvKAKIxHDIw6rTDSwJs9YqF0a3xk3ZE7RyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=bxrrX67QhhcphW1ecDrsMcvszVY4AoMCq1FEadB4mb2Jz92UVtJE58BZBFznLb2LuLIAMT6H-Fi4Y0yUqCm-aqIxQMS3xRjkGYdMaAfHcyO8BPhFN5B03xs1oV0M4w7s9emS6DROsv-dpEo09YoZwpZkxVW3f0AWc35zfZvW2x-Zug6L5MYZ4e_YEKCQ7K321p4LGUbyW0mi9T5NvhrxwINkZz3WF5zGqp8pk9FflvpxD4fizwlxh3zVkqfZu5fJniq788Ey_ZvRuUqQ1wV2_RznAYqNngQavD_iF69n4SqOuv3UqvypKIqkrtjfCupVWnoQGKR7SSg493WcWA2XJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=bxrrX67QhhcphW1ecDrsMcvszVY4AoMCq1FEadB4mb2Jz92UVtJE58BZBFznLb2LuLIAMT6H-Fi4Y0yUqCm-aqIxQMS3xRjkGYdMaAfHcyO8BPhFN5B03xs1oV0M4w7s9emS6DROsv-dpEo09YoZwpZkxVW3f0AWc35zfZvW2x-Zug6L5MYZ4e_YEKCQ7K321p4LGUbyW0mi9T5NvhrxwINkZz3WF5zGqp8pk9FflvpxD4fizwlxh3zVkqfZu5fJniq788Ey_ZvRuUqQ1wV2_RznAYqNngQavD_iF69n4SqOuv3UqvypKIqkrtjfCupVWnoQGKR7SSg493WcWA2XJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=jdXNidOnQPUQAgPaicw1ywrGP4eT7pQ5KQzkktsWLd5nZ2yL1Wl46B5vVKeqEPXXV0zjLSYQG07LyCPXwuV1_Nxd647SCLFZRtpUnCHI8T0gqFG1AL3865O-X0_wUgTi2K-ZdpnHbFuX_YE4l7Oj9DVfMBxfQP4J7FHj34RVi2at_udf3rDvCe5aP5O6JowFqadlPnDIEQQIfXSMGXgPcoRSRP08CYgZ4xyZHOVBfoaK4EgXcL22HjMDRKnt2sfVY9PWsXdVo9NRQFY0qFp6qMi6DnNCvSo1AVNnm5QILVjO3MDWZtvdS1aDGyowgC9tklFNK3Th7qUvNhnHc5cygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=jdXNidOnQPUQAgPaicw1ywrGP4eT7pQ5KQzkktsWLd5nZ2yL1Wl46B5vVKeqEPXXV0zjLSYQG07LyCPXwuV1_Nxd647SCLFZRtpUnCHI8T0gqFG1AL3865O-X0_wUgTi2K-ZdpnHbFuX_YE4l7Oj9DVfMBxfQP4J7FHj34RVi2at_udf3rDvCe5aP5O6JowFqadlPnDIEQQIfXSMGXgPcoRSRP08CYgZ4xyZHOVBfoaK4EgXcL22HjMDRKnt2sfVY9PWsXdVo9NRQFY0qFp6qMi6DnNCvSo1AVNnm5QILVjO3MDWZtvdS1aDGyowgC9tklFNK3Th7qUvNhnHc5cygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=YrBHC-P6vBGmJCsWvfR5KLXvB988cd6pV_f3AaCvtvLelMc1xCsfYs-ld_AHQP8bhm33LZZPSDF_KOTGFuSRpfJD26XqAqnrF2brH144O3IFPEwYgAbPk3cfX4qI2Per-R2qQ9z5qNbqKB7obQmqbiLEnZSq855Qb_h__MeEKCHq8uFKFtPa80fkOqD4-tiAIhI8HixmrB5ypSp3X2_IbU9acD9j1hmUtOn339wsp8pOn3InXelMfgTD4tGuVOwsANAS8KPobYX9z7XG8lTAcvxPBlFY0badFIlcBCDLtEv5SiIXA8p1rjW4niRPBKolPf-6U2HO9WFacQPqocawdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=YrBHC-P6vBGmJCsWvfR5KLXvB988cd6pV_f3AaCvtvLelMc1xCsfYs-ld_AHQP8bhm33LZZPSDF_KOTGFuSRpfJD26XqAqnrF2brH144O3IFPEwYgAbPk3cfX4qI2Per-R2qQ9z5qNbqKB7obQmqbiLEnZSq855Qb_h__MeEKCHq8uFKFtPa80fkOqD4-tiAIhI8HixmrB5ypSp3X2_IbU9acD9j1hmUtOn339wsp8pOn3InXelMfgTD4tGuVOwsANAS8KPobYX9z7XG8lTAcvxPBlFY0badFIlcBCDLtEv5SiIXA8p1rjW4niRPBKolPf-6U2HO9WFacQPqocawdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=d1yZe5blTiRbUz-tisrAJU9A7o8byeoZ7fF8olwoBbWjNeryJABO7T4FnADEvXkFlPsZYe48keWHKoGCaiKcpslBnBhgLAZ_Jxrh0btIOgMYu6ARrehU3O_DtvtSkBJ_9DsEaQ4uMVepvAHpfnAcjyMsKcE8vsaTglolZIdqcEi6bOf8JWYmmng5yTfp_PEir4ojMeDL_jeaj6jhPkEaOyB7s2C55U3iWUWo5Ekd0nA8SL_Ach00vMbhFNgCQvl67PGWTXdn-e48D1McGE5dEcneleyU_yeBkswWnFvNYFzZtuliwyjZY1ubxAJh6CvemgZ3vMTA-OmDLfdThJCN1aJMJwd9NPmr6Yn6zN_qNe6ivk9HR82Q2-n50GWxNU1J5GxK56orIVhjbvZ7k7Bt5S0FB41PRB-gx8y_7u-O6K1iM6W44RNrgRgvlPWQR-FR7IgOF-y0Rp60yW2Fnj6FAVvM_yk0ScuJ_ucwam-AU3dHdj5N2s0M7zcOHFcvUmB_cH6O_TOfU4a6p3c75NJgDt2d-U8QdQWalH9ygVLvBnGeCEsDfkkXBwExcEMYyhDL8iUXsct6gcsCo5VeBURaakk0xBTXqt405bGHdNFHrckpzS93T6mS_Z8xXRiGTg_Ciqp2b5s_d3rdhVY1EBDqrVDPcvknGZ61DFYlaF-lHgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=d1yZe5blTiRbUz-tisrAJU9A7o8byeoZ7fF8olwoBbWjNeryJABO7T4FnADEvXkFlPsZYe48keWHKoGCaiKcpslBnBhgLAZ_Jxrh0btIOgMYu6ARrehU3O_DtvtSkBJ_9DsEaQ4uMVepvAHpfnAcjyMsKcE8vsaTglolZIdqcEi6bOf8JWYmmng5yTfp_PEir4ojMeDL_jeaj6jhPkEaOyB7s2C55U3iWUWo5Ekd0nA8SL_Ach00vMbhFNgCQvl67PGWTXdn-e48D1McGE5dEcneleyU_yeBkswWnFvNYFzZtuliwyjZY1ubxAJh6CvemgZ3vMTA-OmDLfdThJCN1aJMJwd9NPmr6Yn6zN_qNe6ivk9HR82Q2-n50GWxNU1J5GxK56orIVhjbvZ7k7Bt5S0FB41PRB-gx8y_7u-O6K1iM6W44RNrgRgvlPWQR-FR7IgOF-y0Rp60yW2Fnj6FAVvM_yk0ScuJ_ucwam-AU3dHdj5N2s0M7zcOHFcvUmB_cH6O_TOfU4a6p3c75NJgDt2d-U8QdQWalH9ygVLvBnGeCEsDfkkXBwExcEMYyhDL8iUXsct6gcsCo5VeBURaakk0xBTXqt405bGHdNFHrckpzS93T6mS_Z8xXRiGTg_Ciqp2b5s_d3rdhVY1EBDqrVDPcvknGZ61DFYlaF-lHgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=RQVdyiB0Nv1Sk8iVOSEgTJXyBBhfNXpwV0uslQn5Pr2gY0_mCq3WsNbegT9iYlk9lCZJyrUwyawo67UYsKWARGKv95Xtj_B6RLqO3uAXMxU9gT1BCYAmhFByUVQyH1QYwQduMRdLA15FZW2Ox_seXTjGG8JLqSW8ivNUW6uy942TPoEEpYf8KEpqbtOMrGylJb0IxkRRvpvqF5gLmzJQtevB2Vdwwt9QX_MGdlUGPbOgH9Hk8P0fAlxDKW5oskesTW0fURuIniBsB-IurhtBtaXWoSlI32UWMjsJS4GkkfKIErUAMemIiflYrWqRdfAOBikR92KBrMI_X97Gk-An0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=RQVdyiB0Nv1Sk8iVOSEgTJXyBBhfNXpwV0uslQn5Pr2gY0_mCq3WsNbegT9iYlk9lCZJyrUwyawo67UYsKWARGKv95Xtj_B6RLqO3uAXMxU9gT1BCYAmhFByUVQyH1QYwQduMRdLA15FZW2Ox_seXTjGG8JLqSW8ivNUW6uy942TPoEEpYf8KEpqbtOMrGylJb0IxkRRvpvqF5gLmzJQtevB2Vdwwt9QX_MGdlUGPbOgH9Hk8P0fAlxDKW5oskesTW0fURuIniBsB-IurhtBtaXWoSlI32UWMjsJS4GkkfKIErUAMemIiflYrWqRdfAOBikR92KBrMI_X97Gk-An0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=dF8TXcjazwYIx8kohjcYe9_Mkci7RG3xaJXvIGP3SCo-b4OUCS_OsQURMDImLOle0UB0HReNy30a81gVPH7viPtg-vV7DIr3ZbZiOecrmqajA66SZ7QmAsJ0BZgfsFMMdFZlLk6SfaL3NStNezjYrlHdfNZ-KowHi7534j0DbzPSkGcpKjZ-X4-1Rns4bhMC3mwVVs_m_W2QFk6HFoG0p4MY4xWZxSkcHOtADjRcDTIECcItNUCCD52Jn12RWsLytzkDEbiLmJC0g89f3gi57DckHvLaisvhluY-JVlY6O1OnILoB9DQsHUsJW2wT5c3tl2X8TTMfLJ5m9lgcFAvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=dF8TXcjazwYIx8kohjcYe9_Mkci7RG3xaJXvIGP3SCo-b4OUCS_OsQURMDImLOle0UB0HReNy30a81gVPH7viPtg-vV7DIr3ZbZiOecrmqajA66SZ7QmAsJ0BZgfsFMMdFZlLk6SfaL3NStNezjYrlHdfNZ-KowHi7534j0DbzPSkGcpKjZ-X4-1Rns4bhMC3mwVVs_m_W2QFk6HFoG0p4MY4xWZxSkcHOtADjRcDTIECcItNUCCD52Jn12RWsLytzkDEbiLmJC0g89f3gi57DckHvLaisvhluY-JVlY6O1OnILoB9DQsHUsJW2wT5c3tl2X8TTMfLJ5m9lgcFAvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=OT69l1tPVTvkVtzfJCUWrE8JqEu3r-1pOW_RTsRM3bbfWybRmrm98bZohV9kBxppxXR-DvCXkDxnX2al_i3uyGF0udD-2u5E2JsS9Vp9q-Ugcb2np-lv9m8ympTyJRmEYr9TDKdnP60PS01CjEEuX-XuwqhgD12BSI-YBOF_WwW6z1V9O4vZWBoFDFhHR4LJjbECaVsTNAWVMr4aQJkmnvp57JXMg5wy4-DqhyPylllVx4CbiC_YwVuFt0XiDxERfL9VX2ezK9H8kQHXtauAWj7Mh0KLMWM36Sf3oYD7gNM54Al6lhc2BxY4vV0ZnEYh-DIsW5uuLvBDM7JziQy_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=OT69l1tPVTvkVtzfJCUWrE8JqEu3r-1pOW_RTsRM3bbfWybRmrm98bZohV9kBxppxXR-DvCXkDxnX2al_i3uyGF0udD-2u5E2JsS9Vp9q-Ugcb2np-lv9m8ympTyJRmEYr9TDKdnP60PS01CjEEuX-XuwqhgD12BSI-YBOF_WwW6z1V9O4vZWBoFDFhHR4LJjbECaVsTNAWVMr4aQJkmnvp57JXMg5wy4-DqhyPylllVx4CbiC_YwVuFt0XiDxERfL9VX2ezK9H8kQHXtauAWj7Mh0KLMWM36Sf3oYD7gNM54Al6lhc2BxY4vV0ZnEYh-DIsW5uuLvBDM7JziQy_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SO-0hIAMnEfXB774-NRJKC-E9CvzHi9__P5aoXohYlFsvWG3IDY0VtWjuLozncYyvJGg5I6o-YyXUojxW5YMuEriMh8BN5oTzToHfgsvrviFhMbTYkgxx_Za90vqEMmCp5W_dqezMfHqLza3EeDjzTWmfirKXluq7_uuiAaIqB1QPUwf8D6HoNzx8WS-E437usaG-j52uAbexuN5wB_w4quhn_xO7BCKwR4sx7fkqLhh1PWQa-DwsvWmEOlp4SgMYOFUqF0CraJWNlxy-CCrOpXc9ZwCZ-FgDYfuljYISWeYpB1ZVuDgh0zzDEwSsil7zcTnEft5jKLN6zbxFNr9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=B0YlAeQtxAZV4v9jnGzincc-JIWcq92byiKPvXIBc5JmS4DQormZ3Q4L4YQOoc-2TI8czDJ8PMCPfuMQGFpZDXxyu4dvkRg0vbbLMQC3RMjzne0eha2v78rGdWsJqK-1pHDjNoPa0ynhztYsb7C4HGxFz9r9UaDUtSALGaO2eq_dtxMcIoIjcjxqOg8JvdaCYkw-kE0FKyTBhPBHin1beMovj_acsSdGhREvuY42Q13KGCyj2mWt6-djT-ynQ26Q8VFYYr9eJxypBjvpZlEka8jQoYBckulVNIKytUzlCa2N7N2aKY0Fa6GHb2U0l9ScEw-EIXG0oFJ1ZVZcLDURiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=B0YlAeQtxAZV4v9jnGzincc-JIWcq92byiKPvXIBc5JmS4DQormZ3Q4L4YQOoc-2TI8czDJ8PMCPfuMQGFpZDXxyu4dvkRg0vbbLMQC3RMjzne0eha2v78rGdWsJqK-1pHDjNoPa0ynhztYsb7C4HGxFz9r9UaDUtSALGaO2eq_dtxMcIoIjcjxqOg8JvdaCYkw-kE0FKyTBhPBHin1beMovj_acsSdGhREvuY42Q13KGCyj2mWt6-djT-ynQ26Q8VFYYr9eJxypBjvpZlEka8jQoYBckulVNIKytUzlCa2N7N2aKY0Fa6GHb2U0l9ScEw-EIXG0oFJ1ZVZcLDURiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Qzy32yPa0uVaSwXnIthRtEv9-Q_xHAvf0KZ7X3u50YMx53ujcfvf_gOJ5Zw2xHu7m0U01G0VpkgVD3VUyJlNqlhO6NK4A7lAC40DxT70NowSm3Da83FDt8AxzNH54yz0TeLTJwxx89_YdGIN3O_o-jiSsvxFo7PrI2i7md66aZJrDYm4NJrUqGEqSFbUZoc637bqHtbpV0UUSKHe7pe5cI8LKZbYCS9rtDyhwOT7RId_Ahp0n3LDyatssfKOTQmsLFFKGJIv1RtrRuWSAVqloUMZBy5PPtywxlxwwDpnViLZuGSOqCg7hWF_0oNKRql6B6dVBKzG87ioPPW-t-1DrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Qzy32yPa0uVaSwXnIthRtEv9-Q_xHAvf0KZ7X3u50YMx53ujcfvf_gOJ5Zw2xHu7m0U01G0VpkgVD3VUyJlNqlhO6NK4A7lAC40DxT70NowSm3Da83FDt8AxzNH54yz0TeLTJwxx89_YdGIN3O_o-jiSsvxFo7PrI2i7md66aZJrDYm4NJrUqGEqSFbUZoc637bqHtbpV0UUSKHe7pe5cI8LKZbYCS9rtDyhwOT7RId_Ahp0n3LDyatssfKOTQmsLFFKGJIv1RtrRuWSAVqloUMZBy5PPtywxlxwwDpnViLZuGSOqCg7hWF_0oNKRql6B6dVBKzG87ioPPW-t-1DrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=dfRNGSZHLwk0wKvEKQy0hGGIMgHIN0fP7-eqr1oHnRXUattnR8nQc_GjGGHccPfV6JljuQY09RVUBFWTSvKy_nhbiqHTVxPJMlR9FANZ8B0ZjkrrzPrE-sO7gHoqtRXMVokDoCuN-pwcupcQQW6yBkvuxUvIxqTWgtiTyHQvGKq2vsTVFUGReWwO0nAi9kqXigZMWEFwwasbAFQV7KwNbjbXtHiPyXOZknta9wKZ4n4-ZZipmM0gz7rKauV-Kiv3MVZVcMg4q4n86ax2E5K5tpND3m74JSrnmReHE4uw2VgQBS3y76IZ882QQ5pTfO5w4FkIISJBFKeChSRUV33R6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=dfRNGSZHLwk0wKvEKQy0hGGIMgHIN0fP7-eqr1oHnRXUattnR8nQc_GjGGHccPfV6JljuQY09RVUBFWTSvKy_nhbiqHTVxPJMlR9FANZ8B0ZjkrrzPrE-sO7gHoqtRXMVokDoCuN-pwcupcQQW6yBkvuxUvIxqTWgtiTyHQvGKq2vsTVFUGReWwO0nAi9kqXigZMWEFwwasbAFQV7KwNbjbXtHiPyXOZknta9wKZ4n4-ZZipmM0gz7rKauV-Kiv3MVZVcMg4q4n86ax2E5K5tpND3m74JSrnmReHE4uw2VgQBS3y76IZ882QQ5pTfO5w4FkIISJBFKeChSRUV33R6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=cOvMMdWNHVGZTQJAcygOciR-sN8EHCJrsZ5yinnNowPqUiTmjCFufL1bxt-hZhE9jd62AZOwuWWNLnEAnUEtOTgN5hFWt-1EK6c-lgw7_4VaidVv86VVXmwP_tWNdOt5qd1tzTffaUAMxElvB3C3BtWhZij9cg1Sp8DDErXKsFWRDLDt0gTrF2AKbSwB4TqSDWnivdavMVSc5aG5eX57Ga9GC-ot8XK-07pNB4RozLeq6xp1uQKv29o7y0V4Gsq3fp999NObdmlemNs8bPZ4SV_0YnjkeOXTDmlaqWvdT5h-VQsXKDwnYqCINFSEHb-GJwmqf_gURjrUbIwc_3mvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=cOvMMdWNHVGZTQJAcygOciR-sN8EHCJrsZ5yinnNowPqUiTmjCFufL1bxt-hZhE9jd62AZOwuWWNLnEAnUEtOTgN5hFWt-1EK6c-lgw7_4VaidVv86VVXmwP_tWNdOt5qd1tzTffaUAMxElvB3C3BtWhZij9cg1Sp8DDErXKsFWRDLDt0gTrF2AKbSwB4TqSDWnivdavMVSc5aG5eX57Ga9GC-ot8XK-07pNB4RozLeq6xp1uQKv29o7y0V4Gsq3fp999NObdmlemNs8bPZ4SV_0YnjkeOXTDmlaqWvdT5h-VQsXKDwnYqCINFSEHb-GJwmqf_gURjrUbIwc_3mvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=dEzaxM-IrMTgbzaIVd-pPzpoxvxYjrtDd2B26P1JvXbOYuyU1NPydv40c0DDKrIdmyzTQU_6PiRIYaUzuy3NSNoH4Tc36BgnkELDzmU3d9lp4odW8V_eg5cWZqDglfGq3dnN7mXxHu_UPh6xAZTkDMtCCJ7-GCYI6q2zMTT_gCl9r70MsnHa4bSqqO-Dq67sNkQjyuPhEz-VvaOi43DHGNuwDy16l4liRFzf8qMnqOavSnXQWcQuP3G8dbmKH_sxhEytMMjyCVO6ySdu9jz6V6RNDA6eIkhftgLm_d9tZ_kkot_B75NK6pzW8bc9KexBljnC8Ox5_8ZwpZqvcAAr8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=dEzaxM-IrMTgbzaIVd-pPzpoxvxYjrtDd2B26P1JvXbOYuyU1NPydv40c0DDKrIdmyzTQU_6PiRIYaUzuy3NSNoH4Tc36BgnkELDzmU3d9lp4odW8V_eg5cWZqDglfGq3dnN7mXxHu_UPh6xAZTkDMtCCJ7-GCYI6q2zMTT_gCl9r70MsnHa4bSqqO-Dq67sNkQjyuPhEz-VvaOi43DHGNuwDy16l4liRFzf8qMnqOavSnXQWcQuP3G8dbmKH_sxhEytMMjyCVO6ySdu9jz6V6RNDA6eIkhftgLm_d9tZ_kkot_B75NK6pzW8bc9KexBljnC8Ox5_8ZwpZqvcAAr8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=q5Bl-zRD6K3HMhiTfleFRkWcNOej-iexr6B_D95dzHWrp9xyqO7ISCvYqks1d-dboXcN6AGQHY3rCmO03wJm7u0uyj3FIxiQMO1hUpQqynO7325xybWuIoLU2m-tudHaCZW5i82NDXbKcXeZKL0ARcr0QC4bIpUygCmEMZdkeRzaRof4Mn2l0hWlnUNAFg0LdJ5bmg_Ty83SxiYrkVz3tpp_oyd8RA7blCgjFSyeKN026NK26O7tIs_iTOnG0MB67IFsLrQXN5vt_wwcYXCf76hSzWwHEill73IRVAqpRzMkHEcnBaqVVfWCDKx5UtzAEoDvkY9RGA9ch-WdreNq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=q5Bl-zRD6K3HMhiTfleFRkWcNOej-iexr6B_D95dzHWrp9xyqO7ISCvYqks1d-dboXcN6AGQHY3rCmO03wJm7u0uyj3FIxiQMO1hUpQqynO7325xybWuIoLU2m-tudHaCZW5i82NDXbKcXeZKL0ARcr0QC4bIpUygCmEMZdkeRzaRof4Mn2l0hWlnUNAFg0LdJ5bmg_Ty83SxiYrkVz3tpp_oyd8RA7blCgjFSyeKN026NK26O7tIs_iTOnG0MB67IFsLrQXN5vt_wwcYXCf76hSzWwHEill73IRVAqpRzMkHEcnBaqVVfWCDKx5UtzAEoDvkY9RGA9ch-WdreNq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=v6U4iTA04YMyM4lNhHsi2Gmx1a74qm8xcypGWhsSmfcMnBNajdJq55oa_Xem8YGFQDii3Ebr0fEfI_-vsKONlIxyvREJqzMPiqPijury0NmaqAuWU_xHn5GYeEPU1DUJCJlTI3YOciky2loflOtcJo5h4Kopyra4H-vbkQTZuudUIhJ-nOZ7EJuw_YaA-EUH9GmHGhubV2K8UsUkcZAiQ2AhlUCcNoHFwnjwEk9AMcCxGWWY7WhNh4BeeE-r8-UJ5OULUD0wEGI27YRflvFzuFtuh2XpjNbRXKbwMH3hU-UxRwRtrl-lCIUZ9OPfcQTl5pXn0ILmca77BH3LewerfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=v6U4iTA04YMyM4lNhHsi2Gmx1a74qm8xcypGWhsSmfcMnBNajdJq55oa_Xem8YGFQDii3Ebr0fEfI_-vsKONlIxyvREJqzMPiqPijury0NmaqAuWU_xHn5GYeEPU1DUJCJlTI3YOciky2loflOtcJo5h4Kopyra4H-vbkQTZuudUIhJ-nOZ7EJuw_YaA-EUH9GmHGhubV2K8UsUkcZAiQ2AhlUCcNoHFwnjwEk9AMcCxGWWY7WhNh4BeeE-r8-UJ5OULUD0wEGI27YRflvFzuFtuh2XpjNbRXKbwMH3hU-UxRwRtrl-lCIUZ9OPfcQTl5pXn0ILmca77BH3LewerfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=tDL59UtfXl9cs8IVEYcTRXpfV5XId6_vsSPRwm_fTBv3bXIqjXS4JFM9ITmv15pP8gaoegHOn6S61KItEb0B3fFQroph8EcLIPuz2YhvryZON-NnH6uxyOf4PPlaFQM5RLPvGPARyUHUWvf2ankuP4CaCwBoClby2e28vPhonbRsS85EBm95jgor0qzD9t5isd-w59R9XUpVNSBcrrObAG0ZOOexJs8IEKMQgOZaXcIbmLupJLxKhTAtarZwIlXRCO76v-IceI7ui1Dw9K5qV_KePfZIsDH-rroo2gyXIFXdRtJJ6hTyNL3BPkYUKuaTe1GM_Jj-pMwYcht0YBvc0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=tDL59UtfXl9cs8IVEYcTRXpfV5XId6_vsSPRwm_fTBv3bXIqjXS4JFM9ITmv15pP8gaoegHOn6S61KItEb0B3fFQroph8EcLIPuz2YhvryZON-NnH6uxyOf4PPlaFQM5RLPvGPARyUHUWvf2ankuP4CaCwBoClby2e28vPhonbRsS85EBm95jgor0qzD9t5isd-w59R9XUpVNSBcrrObAG0ZOOexJs8IEKMQgOZaXcIbmLupJLxKhTAtarZwIlXRCO76v-IceI7ui1Dw9K5qV_KePfZIsDH-rroo2gyXIFXdRtJJ6hTyNL3BPkYUKuaTe1GM_Jj-pMwYcht0YBvc0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=WjFgkYT58uD9luQ8Wznah1fve1VMmWQcu0byPMx-Znvbw19x6NXHKtacY6JawYZRZ1hrfuL2YLgq7GumqHMzQZT29AQeMOArp0J7-6WQYc9sQ4UEopcSNAobrLIvUEWmL9yMToMSEWPeX-rT5eIYMAvmCDysU9YIKOpIzNDa6hl3D4W8jMKCu61rcx_6sET_AegqGuWOUCfaisI5u9BhCXgmq_zDHc8eLepYZrmRKrNeC7i2LvwGibi2oi7v6eGaLLth_YfKkF2o37VKsrUJ5uj5Q_dbaqGYrvdRCM7wQaEaxUBzt2aWdq322NikOwuw7Bspa1PN35ECD73CzmZ83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=WjFgkYT58uD9luQ8Wznah1fve1VMmWQcu0byPMx-Znvbw19x6NXHKtacY6JawYZRZ1hrfuL2YLgq7GumqHMzQZT29AQeMOArp0J7-6WQYc9sQ4UEopcSNAobrLIvUEWmL9yMToMSEWPeX-rT5eIYMAvmCDysU9YIKOpIzNDa6hl3D4W8jMKCu61rcx_6sET_AegqGuWOUCfaisI5u9BhCXgmq_zDHc8eLepYZrmRKrNeC7i2LvwGibi2oi7v6eGaLLth_YfKkF2o37VKsrUJ5uj5Q_dbaqGYrvdRCM7wQaEaxUBzt2aWdq322NikOwuw7Bspa1PN35ECD73CzmZ83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=Frt5wr-eDCdIyFVia2Zplji6y6tKrIMTKuqxHpmX-aKbw7YkwNFOv4cXZQjgwI7fBi0v5ROYvYLf_2NphmDN-wqhYMLktg2Zv7DsJzFh62_LofN_HZn9KXnDWu2TrE_YEP_0RFs2K0hqBI22TqV14W-CFsi8EPT31R5zaLu1uuh9MMO3sXHXpnG9yOxyPn8I8uM9T-JQQ4M_evOrp8S82m-xXU0TZD2gmNJZ9UmqPkca9YVRczRkpHe70HthfiFjbDfEd6jl6jwrUwn9KNAzKJADZpUWn2Jrlgx7H3yJMOYlvZGLavGAl0iGp5ruNzDyDj05hfL0b9aDyGCq36SJrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=Frt5wr-eDCdIyFVia2Zplji6y6tKrIMTKuqxHpmX-aKbw7YkwNFOv4cXZQjgwI7fBi0v5ROYvYLf_2NphmDN-wqhYMLktg2Zv7DsJzFh62_LofN_HZn9KXnDWu2TrE_YEP_0RFs2K0hqBI22TqV14W-CFsi8EPT31R5zaLu1uuh9MMO3sXHXpnG9yOxyPn8I8uM9T-JQQ4M_evOrp8S82m-xXU0TZD2gmNJZ9UmqPkca9YVRczRkpHe70HthfiFjbDfEd6jl6jwrUwn9KNAzKJADZpUWn2Jrlgx7H3yJMOYlvZGLavGAl0iGp5ruNzDyDj05hfL0b9aDyGCq36SJrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=E2y-KNXou6UPeQCaPBHVygWuCCSLm3b2xCch00bq_fVd4JVtaDx2jBKXc0V96rBlAHJROmCkylmlo_9taDJsblLPx-1PmkhlsQY5MYDdwSDFvyf9xr2ohU1AvbKO9M5qOjkB7bR5m6-CJaNlVUiyRQ6iapxqhikr_WWtWN90FTJAFTBwfmN_bDvhFsytxQjoh7vH1wsysHTc_2juESTvss9eZl4tglYZjdPJ3w5GM7lhr0QxH5iH-ndoJut6umNfEUU0um7fM1KNkiodExfyRrhxQdEe2inwLuN3UJJL2xgJfxTLw86jdzgcVvBad8ZAupTH4qCOHncipLVO4kl8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=E2y-KNXou6UPeQCaPBHVygWuCCSLm3b2xCch00bq_fVd4JVtaDx2jBKXc0V96rBlAHJROmCkylmlo_9taDJsblLPx-1PmkhlsQY5MYDdwSDFvyf9xr2ohU1AvbKO9M5qOjkB7bR5m6-CJaNlVUiyRQ6iapxqhikr_WWtWN90FTJAFTBwfmN_bDvhFsytxQjoh7vH1wsysHTc_2juESTvss9eZl4tglYZjdPJ3w5GM7lhr0QxH5iH-ndoJut6umNfEUU0um7fM1KNkiodExfyRrhxQdEe2inwLuN3UJJL2xgJfxTLw86jdzgcVvBad8ZAupTH4qCOHncipLVO4kl8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcjFbA85UMiPZTNspVsUdFIetsWoGuu1ro6_ATPrIw0YiuidUNwEn5n_5pGMJcAjLloTE3enSNvSrZZ-IjkNNWcn1bsl0N9usPDSPVDt-0bsUchjMkfU-8w9LwDiWlpWqEgKLgselyHARAIez0MtLcmiTbIYXfV1-muitTkKpJ2P9oiS9X5GfFIDGfW16lZE1TwoT7dcw0mp1oXVUtE7DBnJCTU165U6-trz6XLRPLWts7INLSqFueVtTcX2KlS8DxBGlSAF6ytUzd_eScZRXbm6QpGyNimf68RJdSKuU75ViNbi2uxMfMyW6MAqFVRf_Ktth7tG3DaB1xtHEd8J2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKP5FW5cq1vmqF4CIrWdNFvsLYV2m9pTPbmeowUeXKeHToKgiL-Gi5suMjteBZrZX2e6mKGnsgx7wpHeinWqr1rYlC9RywrYrI5Me71d4V6dFnvslrDu5vBk2EnC4nPeK3oIRPPowcyclUDUwyifObkb8iL75BeH8zl8g-P-IwUD9YLESIqvixo_mbDPYiW_ZeiA8fxWsIpShpjDPxluA5uiW-URxAiCP33S0inG5AN6G0VI30Iz7iAb80fzMTiVt18jSDdCo2DfvAuH9P_CIx8_204KmJW3hRK3oRqzgZPGLzPN-uzlB8v2tcuS0DOeeeLDWG7gLvQUWFyWnAMiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=duk5lVWKjuqA3Ltfq97tOA-Hs-3Lsksp6Mt-qmMj7FAH81edPEosI1Mey39VjiZwPbsCfMo2bd5YZs6qmTuYamTUs3gqvLrqLwOeahoWdXVEcKkGbB8H3I6KVSg9-nWK2bw6XZ-i82YfzGOZSw3igLfrFSFwBug3j_cHNCxbUct7WWrVZ064j7WOuHV2BHS9wRI33RTwUmWaS_9ykmrBxpxll2383sdSRTOGKjnHccEpEAz9YP0C7teMsi6jhKk63iIqrjrj7tVpcYmvs_BJrxXcsw9jG_4Pdo9wexkz4A2d3CFVebm7_1KBMqhjMv3iDsQ0NsDCNbQlZ0oTGWjg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=duk5lVWKjuqA3Ltfq97tOA-Hs-3Lsksp6Mt-qmMj7FAH81edPEosI1Mey39VjiZwPbsCfMo2bd5YZs6qmTuYamTUs3gqvLrqLwOeahoWdXVEcKkGbB8H3I6KVSg9-nWK2bw6XZ-i82YfzGOZSw3igLfrFSFwBug3j_cHNCxbUct7WWrVZ064j7WOuHV2BHS9wRI33RTwUmWaS_9ykmrBxpxll2383sdSRTOGKjnHccEpEAz9YP0C7teMsi6jhKk63iIqrjrj7tVpcYmvs_BJrxXcsw9jG_4Pdo9wexkz4A2d3CFVebm7_1KBMqhjMv3iDsQ0NsDCNbQlZ0oTGWjg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
