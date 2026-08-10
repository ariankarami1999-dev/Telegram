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
<img src="https://cdn4.telesco.pe/file/T8fTVauWYWc2vY7wODxtSi6FWD2eMVKWjWNo9xHMIyh23g5Eiu08EEhFl9vJMJHlNW6bfD-9rOMu0-I0md56QAgVzmlEx6mUqPFUaUakt4sqlOd-7uHila4RW7nKZEU85dBABMhgFl4zlhPv5mGK8LiDNbcKj_zk5PVOM2R9xG_1Wspz7SwEmmLSG-9uyleQ7GDR4nHNoo7U45n0r6pSz9SL-1J1SpqD0MTEyIEDdpL5UDAa2vncgmaq-xoSzUJHxNzMLEUYqpnC13C4rp5hS892e8OeGmog6FYTdYBxdggrGdXUg_ifllO6pfBJYp32DWMLJ9Ayhut50M1HwA6M1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 11:51:28</div>
<hr>

<div class="tg-post" id="msg-679914">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حقابه ایران از افغانستان؛ اولویت راهبردی  سخنگوی وزارت امور خارجه:
🔹
حقابه ایران موضوعی حیاتی و راهبردی در مذاکرات با افغانستان است و در سال آبی اخیر پیشرفت‌های ملموسی حاصل شده؛ رایزنی‌ها برای تحقق کامل تعهدات ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/679914" target="_blank">📅 11:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بقایی: ایران توانمندی‌های خود را برای مواجهه با هر رویدادی لحظه‌ای ارتقا می‌دهد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/akhbarefori/679913" target="_blank">📅 11:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9507e5a0.mp4?token=Z89MBqVKAAyHgH1Xqk3-3twReYRuTqCUOLWrYK1yXoiApM1kIo5cLYHQQwZqHxKZdJuUlpbV562okLo2M7uYObuvQ26m4A3vpafNgOsJ1s5711xx2Wqo90kDoo9EzotQdn-vCSXTSAB14lwQgbnHKQiG6jYeb2T5lSyxC15Lts73GrtPAAeWFJtYFqWWknux5Z_boT8pd1tDDOkmOL2T6RDijE5ip9o_zTwAGg7uNZD_gBfM9J6U39_dkaV-lVPWoQrNWCcdYaGo_Dyzswa2VHHlenBVRoWRRqsxAZ3A5AZYnFbzyieYaY4RxXNkroXGPps7yCHX9DYpQOGDmfTDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9507e5a0.mp4?token=Z89MBqVKAAyHgH1Xqk3-3twReYRuTqCUOLWrYK1yXoiApM1kIo5cLYHQQwZqHxKZdJuUlpbV562okLo2M7uYObuvQ26m4A3vpafNgOsJ1s5711xx2Wqo90kDoo9EzotQdn-vCSXTSAB14lwQgbnHKQiG6jYeb2T5lSyxC15Lts73GrtPAAeWFJtYFqWWknux5Z_boT8pd1tDDOkmOL2T6RDijE5ip9o_zTwAGg7uNZD_gBfM9J6U39_dkaV-lVPWoQrNWCcdYaGo_Dyzswa2VHHlenBVRoWRRqsxAZ3A5AZYnFbzyieYaY4RxXNkroXGPps7yCHX9DYpQOGDmfTDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هنوز از ادعای اوکراین درباره حمله به کشتی ایران قانع نشدیم؛ اوکراین یا باید جبران کند یا خودمان جبران خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/679912" target="_blank">📅 11:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679911">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بازگشت پیکر دریانورد جان‌باخته و خدمه کشتی تجاری «آنا» به کشور
🔹
پس از گذشت یک هفته از حمله اوکراین به کشتی تجاری «آنا» در آب‌های فدراسیون روسیه، پیکر دریانورد جوان جان‌باخته این حادثه به همراه ۸ نفر از خدمه کشتی و با همراهی مالک کشتی، امروز به کشور بازگشتند.…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/679911" target="_blank">📅 11:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679910">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c90ea6259.mp4?token=W8OKC0mEZbmBCgUJexHvVLTIJI7CR4vH_mLKhbceyXTORt3jR2VzCjOjcQrtdlcU_DpDCMAl3GC19POMuI8Gu7K1KuNLRtGaxh-rVIxNrDETMesG02VBlKAv07HJTwaFcbdLP3SVZ9qUcdCaKF_dI6xY_pc21WAxXx7AxsWpFzvPb4ZO8unDduFa4QzrHecXCkkg7-Gt0zXCMIa5bB2ULfg8jAVHgj7Gm6PaT1oRSkJqJ8BgzZ3_a5QWyyibgJCkjOeg-_DMqPGlYnb865VmbDf6ECdCrYdQHnMrBIT05EzODUyohlXFgan_Y7DYn9FsBT-fL3puNA6u5KnMNw6PlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c90ea6259.mp4?token=W8OKC0mEZbmBCgUJexHvVLTIJI7CR4vH_mLKhbceyXTORt3jR2VzCjOjcQrtdlcU_DpDCMAl3GC19POMuI8Gu7K1KuNLRtGaxh-rVIxNrDETMesG02VBlKAv07HJTwaFcbdLP3SVZ9qUcdCaKF_dI6xY_pc21WAxXx7AxsWpFzvPb4ZO8unDduFa4QzrHecXCkkg7-Gt0zXCMIa5bB2ULfg8jAVHgj7Gm6PaT1oRSkJqJ8BgzZ3_a5QWyyibgJCkjOeg-_DMqPGlYnb865VmbDf6ECdCrYdQHnMrBIT05EzODUyohlXFgan_Y7DYn9FsBT-fL3puNA6u5KnMNw6PlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: محاصره دریایی آمریکا مانع امنیت کشتیرانی در هرمز است
🔹
تجاوز آمریکا و رژیم صهیونیستی و محاصره دریایی بنادر ایران عامل اصلی بحران هرمز است و تا توقف این اقدامات، امنیت و تردد عادی کشتی‌ها برقرار نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/679910" target="_blank">📅 11:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679909">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
بقایی: عراقچی و قالیباف به پاکستان سفر می‌کنند  سخنگوی وزارت امور خارجه:
🔹
دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/679909" target="_blank">📅 11:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679908">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832f631ac8.mp4?token=VJcEmKSeKo4707OCUQf5VDlqIFqfoxuiF_CPeDdCD6cqYCwVB6qMmc5CVGEUqhwn8iggZM5O423SGg2cBwSsoI4YGZvd2gfZNiJNceKMHqtDa2cXg1vmrB3misYyh7U2eWoHp3Rv-RQI9jm3ZPoIpzXWTaSQPbOAPCTs6cBxJRfFO7UkApCPAIsN5Udy3x-eYyhLrKN315rzTanKSJAeAxu2MuZnLCgKDxHtsRNFwTvG-LljsFX7H1TYtB_5wmzS1qrxtk6JwEJVTr0-D_ViutLb-XT0DL666OrnIrDXY0hRwrNfz72iWiSH7nr61iu6OIChU12Et6qO4isjPqJDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832f631ac8.mp4?token=VJcEmKSeKo4707OCUQf5VDlqIFqfoxuiF_CPeDdCD6cqYCwVB6qMmc5CVGEUqhwn8iggZM5O423SGg2cBwSsoI4YGZvd2gfZNiJNceKMHqtDa2cXg1vmrB3misYyh7U2eWoHp3Rv-RQI9jm3ZPoIpzXWTaSQPbOAPCTs6cBxJRfFO7UkApCPAIsN5Udy3x-eYyhLrKN315rzTanKSJAeAxu2MuZnLCgKDxHtsRNFwTvG-LljsFX7H1TYtB_5wmzS1qrxtk6JwEJVTr0-D_ViutLb-XT0DL666OrnIrDXY0hRwrNfz72iWiSH7nr61iu6OIChU12Et6qO4isjPqJDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عراقچی و قالیباف به پاکستان سفر می‌کنند
سخنگوی وزارت امور خارجه:
🔹
دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/679908" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679907">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سوال یک خبرنگار درباره نقل حکایت سخنگوی وزارت خارجه از عبید زاکانی و تهدید ترامپ: نفهیمد چه موشکی شلیک کردید
بقایی:
🔹
وقتی با خوک‌ها کشتی بگیری، لاجرم گل‌آلود هم می‌شوی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/679907" target="_blank">📅 11:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679906">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eefe72ddb.mp4?token=NacdCxK-IVBkfpa4ktlWmn3UhX4yydcCAvWrnZ20--GlIBaixqNX_0gVIc2za4JA4x0ES-rrxBeBeeR7blnUIFwZ9eGa0f89pziOVH_ouRtpPdM5J5ByPkStuZ4ZV2Dno9etXutsyBd5bJUv-dQ4CgA5eSAADb1t-IY1sxRhrWBkn59FntF2g2X9L0w__bx6oxc4uIyC5br03h8L6IwJtAmrZP9zBSy1DrrUsH-FWq2U-1bepU0Vt5ILlRWosTuoADV3q2V0YWwid3-IFGSbbvu6dBhwIaIPWMvqGCXy5tKQBidt9Zdn0tPMbwQPyaN6yqzUfYIE6ytV_e_Gjx13Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eefe72ddb.mp4?token=NacdCxK-IVBkfpa4ktlWmn3UhX4yydcCAvWrnZ20--GlIBaixqNX_0gVIc2za4JA4x0ES-rrxBeBeeR7blnUIFwZ9eGa0f89pziOVH_ouRtpPdM5J5ByPkStuZ4ZV2Dno9etXutsyBd5bJUv-dQ4CgA5eSAADb1t-IY1sxRhrWBkn59FntF2g2X9L0w__bx6oxc4uIyC5br03h8L6IwJtAmrZP9zBSy1DrrUsH-FWq2U-1bepU0Vt5ILlRWosTuoADV3q2V0YWwid3-IFGSbbvu6dBhwIaIPWMvqGCXy5tKQBidt9Zdn0tPMbwQPyaN6yqzUfYIE6ytV_e_Gjx13Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: مدیریت و تأمین امنیت تنگه هرمز بر عهده ایران است؛ نقض عهد آمریکا در تنگه هرمز عامل اصلی بروز درگیری‌ها بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/679906" target="_blank">📅 11:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679905">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه در واکنش به پیمان دفاعی مکه: کشورهای منطقه در ۳ سال گذشته فهمیده‌اند که امنیت، کالای قابل‌خریداری از دلالان دروغین نیست
🔹
هر طرحی که مبتنی بر واقعیت‌ها باشد و دشمن و تهدید را درست بشناسد، به امنیت منطقه کمک می‌کند و جلوی بی‌ثباتی دشمن…</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/679905" target="_blank">📅 11:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679904">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwrvfrwgmTGINv65qO9Lrvh5njzU5bJSImZ1TkG6uaM_Aws1q03o7aduGG4a6RSiIc2A9y0s_1iAYhBvZrqpZRG67lclEk3T_8GH4PV1Of30oS7Nvdb9LAg8z4zj6c1Dw0VbuwV8LO1s377g_Sm9wEvIUmu8hYQqMRDuDXFRHMCCDs-HbpXN6UVrwOzLkzimUF-TBlpGs9AsrUpVefGZZdEV56U4DUm8Azx721j8N6DQAQS1LbPnh_YtpEWNpe9COGBXaRp7Huw54hTPY2Sl3PJ9HyQr8hiAvOezs52WhMtOFCHVl9z23Jlzl-xkaNDplB_sLHAGJOPCXIJsBibYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
سجاده متبرک حرم حضرت معصومه (س)
یادگاری معنادار از حرم کریمه اهل‌بیت(س)؛
انتخابی خاص برای استفاده شخصی یا یک هدیه متفاوت و ماندگار.
💰
قیمت اصلی: ۳٬۸۰۰٬۰۰۰ تومان
✨
قیمت ویژه: ۲٬۹۸۰٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/679904" target="_blank">📅 11:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679903">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d36785b85.mp4?token=Wl2yvwnJD25ElL1FYyQuDL12tzrVj-a_upDDnXsZ2Vx0E_R8wCe0FYvci5twl2KVyzCm2Wk7-zo9d5FD5fM1g-EYAxev38uhag00YV_KUEgcVyy2h3LENUequq-4QYBPfze1vxgCV_SIRyXQ8MrSHJnYO9_Z-5W7DsFMmcwquNvcpJUoGxOo3kxSC1SSo2oc0q_0BhGCI3lZlp_--Fag0OgMTgeA6QQv1dzsdHDZeM_-y0KiAbp6lxYbfaFe9_1VyQxqkppX98HMZ3hlvIDi7w65DMAzQJpsPvavQyYOVaE-6OfZuAQZ9W8Ki01lFAiiZrPl_aVvj6G5MDaqGyofRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d36785b85.mp4?token=Wl2yvwnJD25ElL1FYyQuDL12tzrVj-a_upDDnXsZ2Vx0E_R8wCe0FYvci5twl2KVyzCm2Wk7-zo9d5FD5fM1g-EYAxev38uhag00YV_KUEgcVyy2h3LENUequq-4QYBPfze1vxgCV_SIRyXQ8MrSHJnYO9_Z-5W7DsFMmcwquNvcpJUoGxOo3kxSC1SSo2oc0q_0BhGCI3lZlp_--Fag0OgMTgeA6QQv1dzsdHDZeM_-y0KiAbp6lxYbfaFe9_1VyQxqkppX98HMZ3hlvIDi7w65DMAzQJpsPvavQyYOVaE-6OfZuAQZ9W8Ki01lFAiiZrPl_aVvj6G5MDaqGyofRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: مذاکره مستقیمی با آمریکا نداریم و ارتباطات صرفاً از طریق میانجی‌هاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/679903" target="_blank">📅 11:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679902">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cdd6347c7.mp4?token=o5KxxprgaT4IlodFir5HqbJczesW5irEtpdvJg_AtFMY-wG4cTYm6nsxxqdLN651qK-owpQZnn8Omq9fpyj88m2CK8L2T6jELEf17bAoaVckLbxIoHAH-LhyDOYauX7qdOpYcohyjec8JqsUWLihjkEAPxEEPb38iArjSTLO1EIDxjX7G6Q0oTxT3D0U13ghVynlbomaXyWXtjgVtegOcJt94aSVDqPdui5cZLLtHS_2fFIPA5qx_KH3qIatvTzxocK7FPsdi_C-nl-lJjzA9RlPY5bUFCqnfgtjA36WFB-JjSTeeZLJkrJiauR5nL9Z6XDLk3l9SIN2MLfX3szzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cdd6347c7.mp4?token=o5KxxprgaT4IlodFir5HqbJczesW5irEtpdvJg_AtFMY-wG4cTYm6nsxxqdLN651qK-owpQZnn8Omq9fpyj88m2CK8L2T6jELEf17bAoaVckLbxIoHAH-LhyDOYauX7qdOpYcohyjec8JqsUWLihjkEAPxEEPb38iArjSTLO1EIDxjX7G6Q0oTxT3D0U13ghVynlbomaXyWXtjgVtegOcJt94aSVDqPdui5cZLLtHS_2fFIPA5qx_KH3qIatvTzxocK7FPsdi_C-nl-lJjzA9RlPY5bUFCqnfgtjA36WFB-JjSTeeZLJkrJiauR5nL9Z6XDLk3l9SIN2MLfX3szzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: سازوکارهای جدید نظارت بر امنیت تنگه هرمز تدوین می‌شود؛ مذاکرات درباره عبور و مرور در تنگه هرمز به‌صورت روان و سازنده در حال پیشرفت است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/679902" target="_blank">📅 11:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679901">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907b318f4.mp4?token=KOA_8qYQK4N-v_zPccegHg59-aC6qwUek4ondst63FoOn0qJo78FqoXR8A-hp-7bcCMHX_TM2Ja9zi3M7G9OjCgV_v56u7WxAqKP2iWCs8NoTeHNNY0GDNBEgwbnoAPgnNBNBvPBc5TCFOFogtqWLbvVnZ-JM6OsbaVtoHBAN2zVQghAMUO9gmikBJJUAWmEfaAgHFLRS-3d6gSAw7BNma6ymPAkQfszvRnkcC29G5viN6rGYvtJZ5ytIIraNMjHllYpNkcqP2rpH62BLN0Dsxn1q5LM5kcKRBekda35jy2hZz5UBWuA4QERbq8EuVgX1euU8LZtHoz9oKEqIBEANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907b318f4.mp4?token=KOA_8qYQK4N-v_zPccegHg59-aC6qwUek4ondst63FoOn0qJo78FqoXR8A-hp-7bcCMHX_TM2Ja9zi3M7G9OjCgV_v56u7WxAqKP2iWCs8NoTeHNNY0GDNBEgwbnoAPgnNBNBvPBc5TCFOFogtqWLbvVnZ-JM6OsbaVtoHBAN2zVQghAMUO9gmikBJJUAWmEfaAgHFLRS-3d6gSAw7BNma6ymPAkQfszvRnkcC29G5viN6rGYvtJZ5ytIIraNMjHllYpNkcqP2rpH62BLN0Dsxn1q5LM5kcKRBekda35jy2hZz5UBWuA4QERbq8EuVgX1euU8LZtHoz9oKEqIBEANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا پزشکیان به نیویورک می‌رود؟   بقائی:
🔹
تصمیم قطعی در خصوص حضور رئیس‌جمهور در مجمع عمومی سازمان ملل گرفته نشده است؛ امسال هم در نظر داریم از این فرصت استفاده کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/679901" target="_blank">📅 11:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679899">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJ9AJrGkjnLFBfpFrxNdLa9z-iolP5TqB6d7d-y5rPrwU_Xeh9DWbc6zVS_3VSeFOXBNYjICFIdStX6sCoQ62al5R4Ij6UGj9ltwZ_c0nliNH_ocGx8MaZ8BN7Wm-iNtmlZB6MROIZVoErNOneHwZdTFaA6RPWcTzlZoR1-cVv_3tnTnAOu9EAKNVZ4F6F05JgZHo4hJ13cQwiW0MrKIPHUoBxMfcp_RguWmK1l_0wbPh2v6gLBKZ9j2yBdsBag9tjtfpHfZ0I1dDnNeJAd94Vb2hZgJkZF3wwgWrZGzOpu-6-VXSXrHpeQMnr8AE4isfNhIJpDF_YvpWu47mDRi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ns8esu2Jb7C7trjAgu13sJP_D_LhgbIWWx1W4lIkJ-p9OeWE6WUXSqMTepNNmWsf9paBzjOwYUMAcoSWUJAUFIancepjaWbtGLqW1VKDXja6BewXJwjv6F93fFmTn_c5l1B9xtbUb1BakNIENALeUwfwEfFSEkaoGs1RfITr_9xFqvU8rAn7DST9UKVGSCon3EKCr1Bx-fm5KE0S_z7qlYEmTOxg2-rcZ9Gh_4ErPgsewVLQnIs6ZjRlGcdOy7hODLUy9WfCX4efg51yMUAmRi7Co1XFEk6NEM8pku5VMNu4btwuYsUn2mg27RmAINJ1QO97XalAJgIoMVIcv-jCng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو تصویر متفاوت از محسن رضایی در کنار رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679899" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679898">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fb622a4.mp4?token=jXdGTEPBu4bfYwixgCa45CFT98iHkIYwu1oHt9ARTUgvPTmJ3wFpoVMuqW7EIZhogjMSkuvosxNWUigeEPKbMfWCAELE_7Dh33HtUfwAR-HGH2xM43vpXdsKItxT0a8hlTaVNG-J4gDEvSN4zQMI0yjMvtAUd6frveXSxDY7XynJwm1QdmUyeuJRzTUxyzjS2QsIi_jvXEUhLRyxUnI-1Cg4JiKEZ7eFa4n3vhIoC6usExuqvkFbybUMYkl7Ieo0WK-b-4ePGgCbyiG7vdszn7tAPO_pbeNtde-t9bfMtWI9l7zvz8xDI4DBP9AOcqdTx9q7juKRfLLGveIZazbD5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fb622a4.mp4?token=jXdGTEPBu4bfYwixgCa45CFT98iHkIYwu1oHt9ARTUgvPTmJ3wFpoVMuqW7EIZhogjMSkuvosxNWUigeEPKbMfWCAELE_7Dh33HtUfwAR-HGH2xM43vpXdsKItxT0a8hlTaVNG-J4gDEvSN4zQMI0yjMvtAUd6frveXSxDY7XynJwm1QdmUyeuJRzTUxyzjS2QsIi_jvXEUhLRyxUnI-1Cg4JiKEZ7eFa4n3vhIoC6usExuqvkFbybUMYkl7Ieo0WK-b-4ePGgCbyiG7vdszn7tAPO_pbeNtde-t9bfMtWI9l7zvz8xDI4DBP9AOcqdTx9q7juKRfLLGveIZazbD5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: تصمیم‌گیری نهایی درباره سند دریای خزر به مجلس واگذار شد؛ الحاق به اسناد بین‌المللی صرفاً بر اساس منافع ملی صورت می‌گیرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679898" target="_blank">📅 11:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679897">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig7IN9gX6df-uTfwhCEHl_Tv9GOb9h1nxuwmvkICXxCO8QDesrm-wZKn2Fgu20rEGGu0_bcQUGS3WPQJz9xq64g-yRmWDC-ap06uuq3RQjgt8MHRqPBRE-jyDlZ0CpL93NrddQ1y2okxViYdAjy7g6qcJlYFNC8szLleqJlhQzXe1FSIjMulNfIBRyLJ8L45RlGYaScD5SjFPSQpX74-srrh1DCwgb-ZGC7Xiv6Ukw3sXdgO4MA6U5fH-fSaWZTl-48sgIiDwv6pR4PdVJck2VE9HEFiGfxFzXVaGUY2uMOuMHWogU16s-6zUYQD7xh8grVEyWGsj2Lzbypm_2TKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از احمدی‌نژاد در جلسه مجمع تشخیص مصلحت نظام؛ روز گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679897" target="_blank">📅 11:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679896">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429d705ce5.mp4?token=cu2IucbN6BFYY6ii1Yc545NRqOT0XEVRTu-rjHW8icsCAYLKOWIFY54qIHLL6HZIX_oTZnkhjLIszTjKWXExydx7PHdid83oaTPZ95xRBPFPpisWZBPyJdYGqeuGjJ7FsUNxC3SRkfWyV0z00wImy2DTQD0_Gb3sM2aThNH-VAU9ETt-Eg3LMm4C4xPppL0nVLqz94ib5wajOLDk15lKHfZXIIfcECc5u2hnOaPJWcYLism9A8uXHGIBGQrvFSigko7jURBZheAIFqglVzswLbPcfqLJoC-m3LxpNBONF9LdNeFyKynABuDywJtEjVkGGYNdVJk8lQnlbqVfz9vNUJIVrTojtL5sUOpBe_oWaiZBkPwgcxv4DlnXa9kE-Jb0L4SJIHSN9T9MGf12HOdfuJWnV-_sR0USLk2AbJkHvlm5IfJ5wbdTDhObQe3IPVfhrPnLR3b7cLKi9ZpnIGvEQa6Q8_sfqiAv1_p8ZK1RZJ3vlCHZA9Kgbq5CxGsVHkYI1vKevaBNU-L4vvyRi2fhjI5WQ0z3Vq__Gmw46mMPB6D-Jx_QFUQpft7FXHXEUA73Y1CqNL0E1zHnVgaV6yz7FaIj4KdT_ukc-PFohDMunpeBBDPrKGPzxwmIfCj91nWmvI8okAkLnx0ZB34FAUcMd_CNC2f3ZJ0EnyMZXYJskzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429d705ce5.mp4?token=cu2IucbN6BFYY6ii1Yc545NRqOT0XEVRTu-rjHW8icsCAYLKOWIFY54qIHLL6HZIX_oTZnkhjLIszTjKWXExydx7PHdid83oaTPZ95xRBPFPpisWZBPyJdYGqeuGjJ7FsUNxC3SRkfWyV0z00wImy2DTQD0_Gb3sM2aThNH-VAU9ETt-Eg3LMm4C4xPppL0nVLqz94ib5wajOLDk15lKHfZXIIfcECc5u2hnOaPJWcYLism9A8uXHGIBGQrvFSigko7jURBZheAIFqglVzswLbPcfqLJoC-m3LxpNBONF9LdNeFyKynABuDywJtEjVkGGYNdVJk8lQnlbqVfz9vNUJIVrTojtL5sUOpBe_oWaiZBkPwgcxv4DlnXa9kE-Jb0L4SJIHSN9T9MGf12HOdfuJWnV-_sR0USLk2AbJkHvlm5IfJ5wbdTDhObQe3IPVfhrPnLR3b7cLKi9ZpnIGvEQa6Q8_sfqiAv1_p8ZK1RZJ3vlCHZA9Kgbq5CxGsVHkYI1vKevaBNU-L4vvyRi2fhjI5WQ0z3Vq__Gmw46mMPB6D-Jx_QFUQpft7FXHXEUA73Y1CqNL0E1zHnVgaV6yz7FaIj4KdT_ukc-PFohDMunpeBBDPrKGPzxwmIfCj91nWmvI8okAkLnx0ZB34FAUcMd_CNC2f3ZJ0EnyMZXYJskzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پیگیری ۴ شهروند ایرانی در کویت و بسته شدن مدرسه ایرانیان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679896" target="_blank">📅 11:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679895">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4bafcaab.mp4?token=Uo-sUwl_0djO2z5rvLm3jsUlggUMA6-v9ga6v4YWRAYl1L1aVVBwz2P0kwsEbKkWS5XYcEIpW3CJ3zZbVqA1Sl97MmVgi6livDDsKqICX5NguUCXCem6BPam_fL_hsNJ-mS7uq75nx9h1EdjNL8Tt3538WbU2znBs3bHJ9E9LSv_T6vVNca8hX5ueZ6sdKjl34Ob0J6CbBf-pobo3-8pqsN5socT4exfXzg9INeKyl0btLjz0pJLoPn_g93lk9PTTAnL3D3f6jecYnQR01BCzTzBTAeGqHRTAvGs9iE65XxtG5oMfGmW1Nhuu6rtpqgwrF4C0-S9mkW5ax3177kMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4bafcaab.mp4?token=Uo-sUwl_0djO2z5rvLm3jsUlggUMA6-v9ga6v4YWRAYl1L1aVVBwz2P0kwsEbKkWS5XYcEIpW3CJ3zZbVqA1Sl97MmVgi6livDDsKqICX5NguUCXCem6BPam_fL_hsNJ-mS7uq75nx9h1EdjNL8Tt3538WbU2znBs3bHJ9E9LSv_T6vVNca8hX5ueZ6sdKjl34Ob0J6CbBf-pobo3-8pqsN5socT4exfXzg9INeKyl0btLjz0pJLoPn_g93lk9PTTAnL3D3f6jecYnQR01BCzTzBTAeGqHRTAvGs9iE65XxtG5oMfGmW1Nhuu6rtpqgwrF4C0-S9mkW5ax3177kMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679895" target="_blank">📅 10:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679894">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd277d9b53.mp4?token=mXLQ8NRStjDcokD8-JVKd_4S8PcYgQQOxJ8D0w_TtqQd9F-SN0-wxyCjLo9J1eCCZ4iSkYJC_G8r1CSrTPGXwdj7T7g8jppwhQtzCigOx8Sz-9qLv1J1DD7LwHQmn6kunYHfe6C_OQun8daoyv6d-jv54TY845gNlAjqjIz0cZCvBe8qqdYq8pgNxwbVRhdxP1_lJfXjWqKPxpyWS2b3b1Q994GkF3VlOnEZzjwyTuenNbqB3GfhoHp6ATV2si0L2BVNne7MA8iqTTngUWtzSyLHk5AcktPjS9txx_zmJlTPKBlACM7CEyBVm10ytYx2LesCk2eOEudm-SeqpyeHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd277d9b53.mp4?token=mXLQ8NRStjDcokD8-JVKd_4S8PcYgQQOxJ8D0w_TtqQd9F-SN0-wxyCjLo9J1eCCZ4iSkYJC_G8r1CSrTPGXwdj7T7g8jppwhQtzCigOx8Sz-9qLv1J1DD7LwHQmn6kunYHfe6C_OQun8daoyv6d-jv54TY845gNlAjqjIz0cZCvBe8qqdYq8pgNxwbVRhdxP1_lJfXjWqKPxpyWS2b3b1Q994GkF3VlOnEZzjwyTuenNbqB3GfhoHp6ATV2si0L2BVNne7MA8iqTTngUWtzSyLHk5AcktPjS9txx_zmJlTPKBlACM7CEyBVm10ytYx2LesCk2eOEudm-SeqpyeHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679894" target="_blank">📅 10:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آخرین وضعیت چنگیز وثوقی در بیمارستان
فرح‌بخش کارگردان سینما:
🔹
بیش از یک هفته است که چنگیز وثوقی به دلیل بیماری‌های قلبی و کمی عفونت و همچنین مشکلات ناشی از کهولت سن در بیمارستان است و مشغول مداوا است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679892" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmUjtUOS5bN0JnBfxh_sBnEjncFG_cs7hEzch6mTG2FcvhzjGWIs3VrLY_tb4jD6_Iw3rQQp5gTg2ZBNJEtGgF6uG-_MdybZSEuB3WtuafmpZ_FitKJy_mj8GgSZ1oNLMDAnvqp4HNe_3ROgEMokLLznbqIFstZSLi-lGgv4m-xT8N9MfBmn4UR3U4AluMrqZHdkSxI-HaoQBC3jxZTNueaMEjS3eUmN2CLUJPbHF52sg2FUNSny58oQlR-LruPufA7p_6rJebM1yLnEG4NApha7A01EYLBlHZN6EP0IXO024KYHAAk57scbUXRWNujMs2ysu2DIi6BJzt_J9Y7cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ونوین» در بازار رکوردشکنی کرد / ارزش بازار بانک اقتصادنوین از ۱۰۰ هزار میلیارد تومان عبور کرد
🔹
در مقایسه با بانک‌های بورسی، رشد ارزش بازار «ونوین» همواره جزو بالاترین‌ها بوده است، به طوری که هم ارزش بازار و هم رشد ارزش بازار این نماد، رتبه‌های برتر را به خود اختصاص داده است.
اطلاعات بیشتر:
https://www.enbank.ir/s/mfa8Od</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679891" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a024cee033.mp4?token=S6HP6IwtNgvQhxwtixsx1b2e1ihKW-1Uug9ElVA5YBPPSG0taeGQvYY7pDleq2ZU_t6lWYxWmTHMl4GQEcMdvDdqgS26CDM8Y6anoNW9cIBvbhjSeLZBeebNW5oUrvBCM67X1EYeXMS1ErUobb9Zt2yzGBLheUSxl3lkqKNe9HETpH74TfA6TdFHu1Nh0-6Xr7LpqMIUdt2Ia2-b48iiE7ST0aQr2KLJCSxSoFPXSR1x10Qi0Qq6bgvDxl14PfIrLDT75vY8V5ZbJWJjfFt2lt-L0GlJmt0vQhTARVtjDX0Jzenwp9govFN9WFmnkhKuNzOLM0jP4HBNIYxTPsvedA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a024cee033.mp4?token=S6HP6IwtNgvQhxwtixsx1b2e1ihKW-1Uug9ElVA5YBPPSG0taeGQvYY7pDleq2ZU_t6lWYxWmTHMl4GQEcMdvDdqgS26CDM8Y6anoNW9cIBvbhjSeLZBeebNW5oUrvBCM67X1EYeXMS1ErUobb9Zt2yzGBLheUSxl3lkqKNe9HETpH74TfA6TdFHu1Nh0-6Xr7LpqMIUdt2Ia2-b48iiE7ST0aQr2KLJCSxSoFPXSR1x10Qi0Qq6bgvDxl14PfIrLDT75vY8V5ZbJWJjfFt2lt-L0GlJmt0vQhTARVtjDX0Jzenwp9govFN9WFmnkhKuNzOLM0jP4HBNIYxTPsvedA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سفر شی جیگ پینگ، رئیس‌جمهور چین به ایران، دستشویی هتل خراب بود!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/679890" target="_blank">📅 10:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMh7J5ezHZmeG5kpZlPPG2er1H-XhflV6AYHJ_FeMSsUeM3gKLETBUnt-ujlaCjfGZcx9hYts5_Kosuizbo40DVjqekYwBH1yaJWBUC0ZmFq805jkoysv_presnY2pZucavpOIIjyQW7ztHOiDhlWmwdz_ZYQsZrF2fGVFSwNKcqfkPcvv9vQgcjH01bhhWUXebY8cTLEUuY0sk3rTaNyvoG0-jNjLrOtM4hL2QeB4YEcrFqF8tfrRJ6EsQihFo8TIXIfVvPG9FpNDV1mFNDScNaW2zI_GOnC2KamEdrh1oN1jSWhK9m84OvKzkC2YipsMD3OK3hchm1vFvLgCtvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میدان نیلوفر؛ ۱۶۳ روز بعد از موشک باران
🔹
حدود ساعت ۹ شب دهم اسفند ۱۴۰۴ میدان نیلوفر و خیابان عشق‌یار، موشک‌باران شد؛ بقایای آن حمله بعد از ۱۶۳ روز به وضوح قابل مشاهده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/679886" target="_blank">📅 10:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای توسعه تجارت در بازارهای خلیج فارس
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی، شرکت‌ها را برای ورود و توسعه تجارت در بازارهای کشورهای حوزه همکاری خلیج فارس همراهی کرده و مسیر صادرات را کم‌ریسک‌تر و هدفمندتر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/679885" target="_blank">📅 10:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmXrqop1uanWMAkRw13GqhSFo4mPqrQGksmt-ll05lh1YehjiIGwSOwY9z1q84D5bDZ3--F49ugbsfnqC4ARZngDvCkz-nVa5yciKPrHAO3N8OWVArvm5otj-CtKobNl82o0etCKao86OgagZHZjbaoEihcn-Z0B_Xp8PPMmziHbyiUJ_UfnlP2DaE7Bfj5bjiYXiH_TrTIAlTllbeuom0jYHyj-L7siwmBqKjLOdoN5dltHNk73FsN79ie-dbeMDhbFy3h5kOcg0Bm75gmXyZBLBs300qyxWtuifs2oY6jF3bqwEp261RRSI1ZXYvq5u0pIMSwJgTnaWrTnR6oRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWSeHEY04ZqjLOPJJlM_qvjHCrivOrP0tI7nlUOCPmFne4UoNyQQntaoEyhu50nVPJa5dfMfIKIT-u_BVKZxDcRfsASKy3dEmMYbLAuGWNyDulm-aR_Q30rUp7Qx-kfLiUfGIe7lRWt_l2u6Yp7I_UpWyAwKxUwOC-TgudSQUaCYpLDTzW9hyq8PNijPZ1PZAQBSRbI6cDZRFtaLcOq1PWFt50f36ifz2VPqhqeiYMOuMaJs9Mh2WShkcuc0sZlcHVRsiY6qe6qHchhGhvWU0xi94ELvIW5Lt8gbfkeE0Z__oXFj1K9GrbUpyEKo1hAedIAmfiiR9yasSHzBlM7u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b53MUZ6sfo9nG1bb_-FIhYNvoF-O1x_1kiQTFUTWUO5zlCwIJGyYU4xmhcSEKVFdb9zSr7xhYOdvDFWRzcVl5i_XyHPvfPBiYh4Ut6rQyWHrfn7N6W3lFgUB1VlWKU90CGj6zWh4bK_y84sEvNk3Jozj2eCM5Nukm3wC_T1v-MFX0HRtgu0CQ9uR8kXmfkBLeHpESxxR-1PpnUtanb4qrbSGk6SiTzWvhewYXXgMEaryJPSIm2zdW9-U7XSIpH3RAAHfRO6GTRsQVjZWapDe6RYsiTzERH4gVBwsf2A_PapLB-YW_iDI897WeGJ7NmsjX4HVcnx37g2LJjGHBfOYdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چنگیز وثوقی، بازیگر و برادر بهروز وثوقی در بیمارستان بستری شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/679881" target="_blank">📅 10:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اولین تصویر از کلثوم اکبری بعد از بازداشت/ زنی، اهل ساری که متهم به قتل ۱۳ مرد که همسرهای صیغه‌ای او بودند/ رکنا  #اخبار_مازندران در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/679880" target="_blank">📅 10:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679878">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da51d32c6.mp4?token=pvVS-deP6XkbfPb7pLty-qrtdSwC8VIwCpnqODhvGEUBvFb3y-WQpO4X9F4asA-Av16aMt1NecgYQQOs0rB3zVztjOCiyg5azLsGj9uiKF_jKdAnFI77qD8RGuXdP1ud61aIcMNWas1oGqpyqPHfOwiL2H7IWF21Yd9AY7EqfdA2aXb04KFBLBcQ7EGlyorJkpjNLNPOc8o_cG48cFlaS-tfT9SjCEREZS1JY0yqnn-5j9RcA3EHbSP7PWpNR7DP4VsWl_5QpfDbeBlLsH3fZaDD-hPc5-qgb1EvPOlmqs4Sc6OTOCskRJiIV_HyCD6YT1rx5DPylCIaaXU31k47ybKMQA6LuDT7q3kgjqdPKAka8PXiMqZiEPOlWhAe8RNw0k1B6N257SanrJZeLEwZXKJMOXRnn54m37PtBA8eGNi_bve8jT3ZSDTSab9vaQsDRk7DxAKPHZi_MxqP60xeFNc8vl1MIq66jOKoC8bWOMWVWOiOZdg6CWvk5flC5lbGmUljw_waJCBDt2gkEmjbMnOr5fUnNiES6RiRPb0yG222Qhw5ImZjCV7298fvjoEaH6RlJs-RHJfkRAWrEHG0QVQEm145BcGTAi0YuMjABb6BMg7A0_tFg9RX3ZBkHJHqOXgensns9_6OrKbh0YmaRyyJLQ2RxUFnKbyKi8xTFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da51d32c6.mp4?token=pvVS-deP6XkbfPb7pLty-qrtdSwC8VIwCpnqODhvGEUBvFb3y-WQpO4X9F4asA-Av16aMt1NecgYQQOs0rB3zVztjOCiyg5azLsGj9uiKF_jKdAnFI77qD8RGuXdP1ud61aIcMNWas1oGqpyqPHfOwiL2H7IWF21Yd9AY7EqfdA2aXb04KFBLBcQ7EGlyorJkpjNLNPOc8o_cG48cFlaS-tfT9SjCEREZS1JY0yqnn-5j9RcA3EHbSP7PWpNR7DP4VsWl_5QpfDbeBlLsH3fZaDD-hPc5-qgb1EvPOlmqs4Sc6OTOCskRJiIV_HyCD6YT1rx5DPylCIaaXU31k47ybKMQA6LuDT7q3kgjqdPKAka8PXiMqZiEPOlWhAe8RNw0k1B6N257SanrJZeLEwZXKJMOXRnn54m37PtBA8eGNi_bve8jT3ZSDTSab9vaQsDRk7DxAKPHZi_MxqP60xeFNc8vl1MIq66jOKoC8bWOMWVWOiOZdg6CWvk5flC5lbGmUljw_waJCBDt2gkEmjbMnOr5fUnNiES6RiRPb0yG222Qhw5ImZjCV7298fvjoEaH6RlJs-RHJfkRAWrEHG0QVQEm145BcGTAi0YuMjABb6BMg7A0_tFg9RX3ZBkHJHqOXgensns9_6OrKbh0YmaRyyJLQ2RxUFnKbyKi8xTFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین باهم یک دسر انبه یخچالی درست کنیم
🔹
یک عدد انبه بزرگ
🔹
یک بسته پودر ژلاتین
🔹
یک عدد رانی انبه
🔹
یک بسته بیسکویت پتی‌بور
🔹
نیم‌کیلو خامه قنادی #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/679878" target="_blank">📅 10:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679876">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
شهید علی لاریجانی پس از شنیدن خبر رد صلاحیتش توسط شورای نگهبان: این‌ها اشتباهی هستند و این‌ها باید بروند؛ من هرگز روی صورت انقلاب، پنجه نمی‌کشم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/679876" target="_blank">📅 09:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679875">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea5aa23a3.mp4?token=Ls_dQtS7OLUcx8sKR5kdMnUHN6av3yS4PQW3rPgG6vpb34PEh-6PPnMtmMcHhbduv3IKHIvCIGtsgS3WbbUxmUDn1ezWqlHoB01F5TaMU36msyVjvalRc1tnrFNC--UjeO6DIzPjvHZ7jsZJxa6dX-YrQ0cYLKBcKLrSMU-R6CerDwHKFFH7S3s1LSzrAjguWqy1hxkVio_QjeSZFIvQKiagZT2_kN35NKtCRfpQcD9ekwTf-l6PHV5hbkCK6Ezq9eROv-7aIMaL1KTOID0efU0gnQIWhlLPKYA3bZDKgRa_7T0DYgABwaWqHfaiECRHY6YAKFKBM0Sc_pLLnaISGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea5aa23a3.mp4?token=Ls_dQtS7OLUcx8sKR5kdMnUHN6av3yS4PQW3rPgG6vpb34PEh-6PPnMtmMcHhbduv3IKHIvCIGtsgS3WbbUxmUDn1ezWqlHoB01F5TaMU36msyVjvalRc1tnrFNC--UjeO6DIzPjvHZ7jsZJxa6dX-YrQ0cYLKBcKLrSMU-R6CerDwHKFFH7S3s1LSzrAjguWqy1hxkVio_QjeSZFIvQKiagZT2_kN35NKtCRfpQcD9ekwTf-l6PHV5hbkCK6Ezq9eROv-7aIMaL1KTOID0efU0gnQIWhlLPKYA3bZDKgRa_7T0DYgABwaWqHfaiECRHY6YAKFKBM0Sc_pLLnaISGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا همسرت همیشه صورتش را می‌پوشاند؟
عثمان دمبله:
🔹
همسر من یک زن بسیار مذهبیه، پوشاندن صورت در اسلام اجباری نیست، اما اون واقعا بهش پایبنده؛ گاهی بهش میگم که حداقل صورتت رو در جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679875" target="_blank">📅 09:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJ8oG3YZx51UAt1sCWnvbHB_Qc2ZXsDZnlehi6J7h-ATN1mdjaGIROtrwPxfITMdNyLSWZ9_MgNI7AVbFsFMnZkGPqgimQPR6D9t8rmP8SSXpbTSVyHdtUVa0tU8I6cgnLNrTjWO0LUHEC5RpHV3t4NtVkM_Bm7gyrapMEsCRKz_RGKD9qxfSBQt8hIzn0LyNKro-I-FieWTzyxfUoTjfslYJjUGqVOyKBlWmSl4tKq6o5ShVK3CY6znpHoHBESkr9tVOV-ZBd0V5XaRnxF22V618vCGZBv23HC3EnqAnLxxlwhj6uoMRfxut6NTZgE6IzF9YbTTZ37vMnlivMPfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb8oStzC402R6PqtOPqWasWeXNDK72rcUzRnEmHsTcVd_PDcSW0tZvm_taiyVt3yU8CXIGvTRwRHxGRLgB2CtLXjs-GP52tL7CyBqGRPv3B24NLasiSOV2yPNYvQE7Rh1WPflGRCQ6c9ggGnclLEYotEkHqTAOFIbimHinPEoP_bRlBER8B5aF15SvIE8JzGREl-xm86795TXjsyBeuppOGyRmI58Sh9QxbyLYAx34JtfItQWmhV-0hz-N1ju73yT1-re3th9S09BgMaL-yD6OIs_JA9F6j0ZClvUZ_pp2JsAwSCGWIGDExZy1xCHu9x-wKj2mgF0y2FykE464ceoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSIqP2RRfs6F3aMjfK6BCAxJ89TOp-pmIDstxWqzkyEPez4PZoE6YkSKOGtVoQX2P_gpT7Q7j56x-LTfH1fiI_oj_AdTXrbKiKod_WLXai5CcO-5o8qHtxhWsZUh5kWgVG_Ga7WfZNyMDqUSglMswQ2vBKrcf_WZzkWRr2xCCJEOI7HOV0CrCdIv30bF17AaqUkYRYve88_JrOTYOVIuaUpQzlavEPnFzX0TcQ0VChxTFdKmgLwP6b1PnFyLPyjjXpUGGjef7InnjPwqFUio6vTqKjDOQqW2FxjPf3PDNYkjwpnUpHEdAXMNl0dqIc4pznRRpqGlfVNqi_4McOb0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeqfZ0QGvNdwxWkpMP92X645464dXmsdJEwaZsBlxvxH0P7k5y4xVq7at3GpOnqM20jC1L2CESH0yEo4-9fr_A9gqOxQeftRsu4hgvTaiZIxmDx8LxEgLtgqupCZEdMMIVAqFYOW9xCup9IYBWZu_xPVCRB5jpf6LwGYfjNtRq6fVxIsUOVGPTgP4VGLoGp_4B0GTckBwV2laxAqWu2DZeW6fdX0RDB4TYRZtAx3JzQ_gmBdp7eD9w-65vxQs2dybIkoJ0SVJDiQ-7TB3XDXci_X2hvGQCp8pxKk68EpRoxegWAIp2DGZE2DEqFbPMHaDFuQSP0mKLExynYMMb02rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3tALI-gC-rJIkE_Q-MR84Mmx6OMm6-DgZ2B2l9AeIZ728mWKVsiqOKvg3Pu0hQiiwX9Wk2IcTzFjGXImF3vKIw3OhRbm8W7MJ74GE17zpwcu0nf0EbJT9qRtxEyXzx-2YLj3AySvyLLj5zIxebvmNm8AZixp8AYVVeXbdar7YJkhPjQMQ28eEDXrsLeThKytz98KCLYHRQNow5bJ-qLw16GYg-4Oi40vc-kWCpQPrf47c0TGaFdB_WrtiL5dq-3EEijl9dLDmAqXXssECw0sUhV-SyLkbiA-t-qLqeNRJMlROo2U1BKOgfpG52VLx9cCdYYXfJPZCyI6JH_1ZHLEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵
نوشیدنی ساده و خوشمزه که می‌تونن حال بدنت رو بهتر کنن
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/679869" target="_blank">📅 09:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42b704b33.mp4?token=Op5LnSYb4Ulf3hkj_fWDp32j-QiPdKqanNJrJUQDkKDjql155MC1AkmMMHaRqCzfTQRBAmuhw4hBiaw1u6zoSYlrV4-RMyLA0fsfXsxcCDoOAi1V5VHy6LvEH7oFSbQGL2YRE0tm5XIE0e4vYY2dbtGjMoi422t9p6RIZwz4lVWGrzJVBY4v8RME6xH_5BG0F09IVATWCClUwIs56JW1ZsE-oPw1e993abZSbG5FqBaIAQPNJgbtIHSUa1USf-SyVcuzwblnYNxc8CANDMPrJjZx_u-_UAV_e1aEv8p0N6i-AfpIYp-hNP1gI27zj7CEdbXZBiS3OtRNJo7di5-XvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42b704b33.mp4?token=Op5LnSYb4Ulf3hkj_fWDp32j-QiPdKqanNJrJUQDkKDjql155MC1AkmMMHaRqCzfTQRBAmuhw4hBiaw1u6zoSYlrV4-RMyLA0fsfXsxcCDoOAi1V5VHy6LvEH7oFSbQGL2YRE0tm5XIE0e4vYY2dbtGjMoi422t9p6RIZwz4lVWGrzJVBY4v8RME6xH_5BG0F09IVATWCClUwIs56JW1ZsE-oPw1e993abZSbG5FqBaIAQPNJgbtIHSUa1USf-SyVcuzwblnYNxc8CANDMPrJjZx_u-_UAV_e1aEv8p0N6i-AfpIYp-hNP1gI27zj7CEdbXZBiS3OtRNJo7di5-XvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کادوپیچی تیشرت با یک کاغذ؛ ایده‌ای ساده اما متفاوت و تماشایی
🎁
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/679861" target="_blank">📅 08:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل در راه است/ روز در کدام نقاط زمین شب می‌شود؟
🔹
چهارشنبه این هفته، برای اولین بار در دو سال اخیر، خورشید گرفتگی کامل در بخش‌هایی از گرینلند، ایسلند، شمال اسپانیا و شمال شرقی پرتغال قابل رویت است و برای دقایقی، با ناپدید شدن کامل خورشید، آسمان برای لحظاتی تاریک می‌شود.
🔹
این خورشیدگرفتگی در بخش‌هایی از اروپا، آفریقا و آمریکای شمالی، به صورت جزئی دیده خواهد شد و در آن تنها بخشی از نور خورشید از دید پنهان می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679859" target="_blank">📅 08:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682e4ae741.mp4?token=E0teNFPDEr6rrHiPYrKxXeEYJOvVfUXsIOfsG_vvXeKkFRUwfFOquXbaR91Gq-UmDN0TwwTCkA1XuIjJ6XwAtNvJOq4QPOV5KO2lrKJgvfwcUT7hOHmRYBPa8v19AAxfA9KBE7-RP1YlJg1OcPff0XQmf0thwcfqIA0L0wGp-9t74_YViXAJC2QJszrZx3yqxMfnK1QOcgxxjGITYuDNvE-KktK9hyuKQf-NItLGFZVAdlha7QsDsrUjA8x6MXxfVoqirloX1eOmLY26enSbPavX-OfIacfhXD0msCl26cRi2ISpDooCi9RxGRpb2haLwUbmZBkRKhTAPklxRwGGCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682e4ae741.mp4?token=E0teNFPDEr6rrHiPYrKxXeEYJOvVfUXsIOfsG_vvXeKkFRUwfFOquXbaR91Gq-UmDN0TwwTCkA1XuIjJ6XwAtNvJOq4QPOV5KO2lrKJgvfwcUT7hOHmRYBPa8v19AAxfA9KBE7-RP1YlJg1OcPff0XQmf0thwcfqIA0L0wGp-9t74_YViXAJC2QJszrZx3yqxMfnK1QOcgxxjGITYuDNvE-KktK9hyuKQf-NItLGFZVAdlha7QsDsrUjA8x6MXxfVoqirloX1eOmLY26enSbPavX-OfIacfhXD0msCl26cRi2ISpDooCi9RxGRpb2haLwUbmZBkRKhTAPklxRwGGCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاس گل عجیب بازیکن ایرانی در روسیه چشم‌ها را خیره کرد
🔹
رسانۀ انگلیسی one football با انتشار ویدئوی پاس گل نادر محمدی نوشته: «عجب پشتکی!»؛ محمدی در تیم اسپارتاک کوستروما در دستۀ دوم روسیه بازی می‌کند.
🔹
رسانۀ انگلیسی که در اینستاگرام بیش از ۱۰ میلیون دنبال‌کننده دارد، به تمجید از این حرکت پرداخته و با تعجب نوشته: «او به معنای واقعی کلمه توپ را با یک چرخش از جلو به داخل محوطه جریمه پرتاب می‌کند».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/679857" target="_blank">📅 08:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90d15cee9.mp4?token=SV5Pgh0Zu-39faHZ4v-aAxmDQ3ulE085P1GfOIL1sVjWlDK5bon1jmdFZWFDrajMKBzGyEVJGjD-QdD8s8AQPHVRurXb4kakofZd76eXBMESvC-VKKCHRhb6UFh-R3KVDNE7prE7FnwncilGQWl6Wc5-jRM8xTgF5LGFDO8bhszapVFbLwMqRH-AKaFCQ0diXizS2R2MsLqYvL3DMZVAMDCFCau7yOuBJD7IaEcwRSnc7buPNVByrW0K7yg6FfbkScZJ5yDhn2xca8XvzvK5T1BB7xRMsC7TfF9oGw3jxiDSQrcqlcu7bsiEcisha-ESEwPOr_fXwdfWE8tYQtPvtR4T2DHlkmeW9d1mfDziMJZp0fBFVkZ6GVdKykwVnMg68_2eF_9lKXsWAf0OvS_Pj-ha5LutKZic9VWK4y9hP21FMpNRfJW1FEz4UAAmBOiNgkc7mEdRw2HDz4aFI1JqwFpi-XAvocTSNfONFx7om_CEYYmFjkVgapAM8vM8ChbLN3rG2AI_U7v5SqQhLNdQEosXIm88xNyow548_UN_bJBM8CFhwEatqcdm6kEf-Q2SBT9czTXFvwpydZV4euF_E_RCZVtqev_ZFK6aQJAehfmzv4SzV-m40RgtjVmA58ttlKRZeEKFJXa1hEk_23mVBlKgwc4gzAMWJekzfySj8RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90d15cee9.mp4?token=SV5Pgh0Zu-39faHZ4v-aAxmDQ3ulE085P1GfOIL1sVjWlDK5bon1jmdFZWFDrajMKBzGyEVJGjD-QdD8s8AQPHVRurXb4kakofZd76eXBMESvC-VKKCHRhb6UFh-R3KVDNE7prE7FnwncilGQWl6Wc5-jRM8xTgF5LGFDO8bhszapVFbLwMqRH-AKaFCQ0diXizS2R2MsLqYvL3DMZVAMDCFCau7yOuBJD7IaEcwRSnc7buPNVByrW0K7yg6FfbkScZJ5yDhn2xca8XvzvK5T1BB7xRMsC7TfF9oGw3jxiDSQrcqlcu7bsiEcisha-ESEwPOr_fXwdfWE8tYQtPvtR4T2DHlkmeW9d1mfDziMJZp0fBFVkZ6GVdKykwVnMg68_2eF_9lKXsWAf0OvS_Pj-ha5LutKZic9VWK4y9hP21FMpNRfJW1FEz4UAAmBOiNgkc7mEdRw2HDz4aFI1JqwFpi-XAvocTSNfONFx7om_CEYYmFjkVgapAM8vM8ChbLN3rG2AI_U7v5SqQhLNdQEosXIm88xNyow548_UN_bJBM8CFhwEatqcdm6kEf-Q2SBT9czTXFvwpydZV4euF_E_RCZVtqev_ZFK6aQJAehfmzv4SzV-m40RgtjVmA58ttlKRZeEKFJXa1hEk_23mVBlKgwc4gzAMWJekzfySj8RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ دقیقه تمرینات عضلات پا بدون تجهیزات در خانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679856" target="_blank">📅 08:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i93s7XiZ-PglaExZlzCJDlv8HoNRZ8o10E_QraSesWh5tgFmcPMENKNgFSJPkP67wGfgH-g0ln6MdCIYPPvXWw03EZUrOGmpgO7EuzhZkCktO9E3DPuVx9kzxBA-uMooOJkQPQ-QE_Y-vgTTNk6fDoKWqJ24Q3T6oOeSW58nWRay-ebKPAZeZvhkF7BlxS7aZlCekjNPhsvp_bY2OM6SE1FFOlMz9feY8lVJ_yWBC69clSOULhsXSxHjLcZ7FBv42pXpVYJgbudRLvm4nJKbMCxWbHebNpblGBBBqsk70dWxL1bmz7DrtZLYkedPbS4igdCEckxM7xwzepQGvljcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGkj9agRqoNXf6qWC6ZP1FC-gA-jGiVQP1qaQScEr7cq2zTmfKaRZu9pyw_efl4MzCAalkkcBo_5k9LppuvGesvp6xcoCV1XUWHKY2XfgGGUDHeaF0nzaIOIIV847Z5Msx9ZFJT25vSCJTMjgQ9Gqfkib6gzhqn47kuusi6UzsiRjLQVEdklL_aX7lVZc_De0ZStE1JRrUgv2mIsjbCWLIpxVb4yMAyY8BJoJgUwiBzNay8cosvFdvhtWS6btD3M1jS9by2IyGgHXutYpcZ93E9F2EYtjZvMbolc5_1Xa-Kc0uRDhFfuuhb4bGOrfkUQJiu6QanDDKbADRO-eYjDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcMunhkPZhHQIxlx5j8Aket_Re2VKcv_yIJZLVveU8w94WrYmLwtG7T07fk-BSv0RFxiw8It2pKJLRGDoGOF6H58nATO-mIXU8Iy5ygHQCZtJC--W42ipM-IbccBAfAh2dIm8BGMHVcbNOQ9aTVgofd6TtjcU5Brq693QE4SzW2k2yK-3z9XQ_fECaA99MQBvWXUYsGmYiGJyRn2rW3VsJfGBTAkC-Scmzto-082ibc2CnnKh5uvg4Sub1or5i-hJQJZ8KKqptjo-8lz1TrKM4wDJD42RfGUtiVnXoUy7zf_IBbdob-jiyCcF2EW0RHiUhf6SzYMtfUUl6raslLdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4UIUTGw9Idp6NPXcvRpNcBZkvriXXKa-309yDc4mFvn3kjf084au_d3D10Ey2XpZV3iNNbSrTXw0HUYjtCpGDXqi86yfPkTRqxLog8HdDFWbkbW0uVk2GuLcIUvmijDFkRula_6QWi9CQVrO-fzWU5wrlhHlFf6R4iN4I-BwnNEd3M_HM9IzCI50sG7UGoTYqdLEAgknDIhudUgialuuhcMsyqnkWmrOmFk10KGo_zUW7j1qKkWGfzlJbF8vgySQ_WeaNDlHWTp7Cdp6nWRIBAP9vmFxL4sSpCevgowWNkzbq2GxbscECwsgZc0epMm4D0GEyskE7pSOFjjRHF-EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بلیت پرواز تهران - مشهد از ۱۰ تا ۱۹ میلیون تومان
🔹
قیمت بلیت پروازهای تهران - مشهد در روزهای دوشنبه و سه‌شنبه به صورت یکطرفه در بازه ۱۰ میلیون تومان است و از روز چهارشنبه قیمت‌ها نزولی می‌شود و به پنج میلیون تومان به صورت یکطرفه می‌رسد.
🔹
همچنین قیمت بلیت این مسیر برای پروازهای کلاس پریمیوم اکونومی و  بیزینس نیز از حدود ۱۲ میلیون تومان آغاز شده و تا حدود ۱۹ میلیون تومان نیز ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/679852" target="_blank">📅 07:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679850">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
چین یکی از گسترده‌ترین اقدامات تلافی‌جویانه تجاری علیه آمریکا را آغاز کرد
خبرگزاری CNBC:
🔹
این اقدامات شامل ممنوعیت معامله شرکت‌های چینی با هفت نهاد آمریکایی، تشدید کنترل صادرات پهپادها و فناوری‌های مرتبط به آمریکا، و ممنوعیت همکاری با نهادهای انطباق و گواهی‌دهی آمریکایی است.
🔹
چین همچنین نخستین تحقیق امنیت ملی خود در حوزه تجارت خارجی را علیه تجهیزات چاپ و کپی وارداتی با نرم‌افزار خارجی آغاز کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679850" target="_blank">📅 07:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679849">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8MKHdg0x4pSCqVXX06S2xkNxbqkMVAaoGnoHP-2_voZkWTldh4tPcRnbAJrygBnQCSUWmn_yllzm90WT95dufIxNIEW80BrmMlm0sJo7r8kifn2y1HJWb9HWSkmFZIp1X-eR3AU4WvO_wxaSkOqkGNBF-JefyydAW7vz5Urc9vgCAhn_aJ41wcEXKegfh6szkdUYjwojbw3zYg_wB2qmUwoNkZ9tyzQbzdeG_WfXaTJ0HbeKbnrZ7TgaURnbm8_0A3YpzaKth4QHIm9jZ3OYGIx5uz1bDRn3zji2_qfpHL6DpZBaNQP4SABBovqNyv36H2kbBArNiTTLRzWW_I0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۹ مرداد ماه
۲۶ صفر ‌‌۱۴۴۸
۱۰ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/679849" target="_blank">📅 07:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679848">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b634713d8b.mp4?token=ASh81L-mZV7F1y8vLGS42lDvZrqVxO-p1j5Vth5K8FWcR_HRcyoNq2QJBZY4-6YncBuzc9iaf071zZTXRPvUtmSFuxvXx1HrXVawfAVVUnajCJj3_Hw8ztYSBMt3pHq8qtiUKTYrXLmdDLh2pY9Ci6eCDaQG6t2k1vxXoZzDa8FuzgWCSrNiFXT79mjDYxH4dfzlFKvU-b0Rr7N8lt7YQ26NHTR20AGzSvU4wAyP1fsb5bJwLQ6Y1mxrwUy1C4HY-5CgdAvTWQC5_xVhnKyaBV9VPrSkU8KVI_kLVQuWXORyNxBBaaEexv-BWrhO-n3P4WYrPFz6kgnsLOCOrXOMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b634713d8b.mp4?token=ASh81L-mZV7F1y8vLGS42lDvZrqVxO-p1j5Vth5K8FWcR_HRcyoNq2QJBZY4-6YncBuzc9iaf071zZTXRPvUtmSFuxvXx1HrXVawfAVVUnajCJj3_Hw8ztYSBMt3pHq8qtiUKTYrXLmdDLh2pY9Ci6eCDaQG6t2k1vxXoZzDa8FuzgWCSrNiFXT79mjDYxH4dfzlFKvU-b0Rr7N8lt7YQ26NHTR20AGzSvU4wAyP1fsb5bJwLQ6Y1mxrwUy1C4HY-5CgdAvTWQC5_xVhnKyaBV9VPrSkU8KVI_kLVQuWXORyNxBBaaEexv-BWrhO-n3P4WYrPFz6kgnsLOCOrXOMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهپیمایی بزرگی در مونترال کانادا در اعلام همبستگی با غزه و مردم فلسطین در حال برگزاری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/679848" target="_blank">📅 04:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679846">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71c940c21.mp4?token=LcXKanvBrI_5deC2oQBVa_LBrC8i5ETu-XAesq2gqfy1BbyY8y980RORXbtfdIcfXFHtLWItKkSLqq-jxtX8EXA9s-xPDv2DIIMEB5dTpez0CAhtfKoeDpYLf50Uzde24nmCQiymhvAa5ugIAjuwLmtrbAMf4QY40AsNkT9B3hn4ZKBtAQxn0OtFh0bXz581Qcn17SE97NrhWNAspIiq2GnGkbrGOqvhcZeqo-Z2RY4vmPeZ0Hibz5AmLkFkZM90Q3kl753x72u4UsZE-l44R5gPRTeCTHkDsMeolBEVcTa7TeVGbO2WcATciAiM7W7nlGg_fplBxm7Nzt5VBBm5f2QN2L9pe8yqNktxJ7L8yx1g-8ZgJ5mu2_j-qptZeT4HOgOl2V95UGnF1UiIlQZXcupIatsDXRsZmubU_ZdFxXIdPi6g8VmbWSsbIB7I6yixuDHdkXsGBGerGngmJpUVbdeHtpzSQPdWrOE4udLutLPyKSifw4iyG3sOJa-exbL5dQqK12jrq-CiwpO-1teOtRrgh_Uxf6trNQocLPhR_6BoWIwv0vR5ndhZSN_wZq-vN6iyHuKR1LmjSNTEDK0Mzj-MzebS_aXu3vYDjd9PXjV9_clhcI9y_gRyKX_VDY2QGVtsiCWZehqdMWo8i-LBIvjw7mh0lrcT0gC9u-QBz18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71c940c21.mp4?token=LcXKanvBrI_5deC2oQBVa_LBrC8i5ETu-XAesq2gqfy1BbyY8y980RORXbtfdIcfXFHtLWItKkSLqq-jxtX8EXA9s-xPDv2DIIMEB5dTpez0CAhtfKoeDpYLf50Uzde24nmCQiymhvAa5ugIAjuwLmtrbAMf4QY40AsNkT9B3hn4ZKBtAQxn0OtFh0bXz581Qcn17SE97NrhWNAspIiq2GnGkbrGOqvhcZeqo-Z2RY4vmPeZ0Hibz5AmLkFkZM90Q3kl753x72u4UsZE-l44R5gPRTeCTHkDsMeolBEVcTa7TeVGbO2WcATciAiM7W7nlGg_fplBxm7Nzt5VBBm5f2QN2L9pe8yqNktxJ7L8yx1g-8ZgJ5mu2_j-qptZeT4HOgOl2V95UGnF1UiIlQZXcupIatsDXRsZmubU_ZdFxXIdPi6g8VmbWSsbIB7I6yixuDHdkXsGBGerGngmJpUVbdeHtpzSQPdWrOE4udLutLPyKSifw4iyG3sOJa-exbL5dQqK12jrq-CiwpO-1teOtRrgh_Uxf6trNQocLPhR_6BoWIwv0vR5ndhZSN_wZq-vN6iyHuKR1LmjSNTEDK0Mzj-MzebS_aXu3vYDjd9PXjV9_clhcI9y_gRyKX_VDY2QGVtsiCWZehqdMWo8i-LBIvjw7mh0lrcT0gC9u-QBz18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات گسترده در سئوتا؛ معترضان در اعتراض به مدیریت دولت در بحران مهاجرتی اخیر، خواستار استعفای دولت مادرید شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/679846" target="_blank">📅 03:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679845">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: از آغاز عملیات «خشم حماسی»، ایران بیش از ۲هزار حمله هوایی، موشکی و پهپادی به پایگاه‌های آمریکا انجام داده و به ۲۰ سایت در ۸ کشور آسیب زده
🔹
خسارت وارده به تجهیزات و تأسیسات آمریکا ۱۳ میلیارد دلار و ۴۲ هواپیما منهدم یا آسیب دیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/679845" target="_blank">📅 03:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679843">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqOwy7XGurEy1ZQhHv9QrFaxxSyAgu5M3VsRQq4FVLn8bS-YQEYvebIYAL-M25Mdrc-O4Yn1q1NuaWlxtCESfvWVJ9E-_EBIpDIVI50LwmJ3y06BOdvWx-LhGRHoXqairvC9pYjif6WwTu2yk7RgHqRfwxIDLhKkTY2980Y52ymnvrPracLMjkbKia9jz51ddpx1Bioq5JZT8eGSTN3SgvImcINncXsKqpZKzFkjY3-a9r4BT4jjmiiUoRiGyJ2Bc0xi2tTe-dyRjBiiRMcC3s-pvR-WKO7cjOBxdhxmjxOafMopmbsd00VhQLFMOjJj94GaXO8Mtpe8dYLAKbp2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای یمنی:
امیدوارم توافق دفاعی مشترک، شامل کمک به سعودی برای خاموش کردن آتش‌سوزی‌ها هم باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/679843" target="_blank">📅 02:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
برای آزمایش بمب جان ۱۵۰ هزار نفر [توسط آمریکا] در وهله‌ی اول از بین میره...
🔹
به مناسبت جنایت آمریکا در هیروشیما و ناگازاکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/679841" target="_blank">📅 02:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679839">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
افزایش قیمت نفت: ۸۴.۸۳ دلار/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679839" target="_blank">📅 02:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679837">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8104959d0.mp4?token=KJ3PLe0lI5utC80-BZVsNTtUuEMQBb4SK2ONUME0a8FOJ-b9PEj7iXGEgsUB-86jmGjb5T3Ydckko0M_KmU6yrlP2_rlRu4O-0NKTcgMnNLcZ0rBgew56G3IOohqGaLSV1ywi0SWGri9tgZyrKBuAzJ8cwZGAXNxYFsdi4yudWUUdBhhoHbpDbr4o5YRX3MYbo7kHqgVEV-fEKb7w1w8FhhFiDelSxRnoe--c_AwBe3iXowo7hXp17Vp-8mf6JS1eDMD7n--bEBHPCv-af1w7sTD3BzVaoafKAL9ccEdwIN35wAEr0UFhdQAxNJMkLIJIu949SSOXFUS9rTHhdMGKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8104959d0.mp4?token=KJ3PLe0lI5utC80-BZVsNTtUuEMQBb4SK2ONUME0a8FOJ-b9PEj7iXGEgsUB-86jmGjb5T3Ydckko0M_KmU6yrlP2_rlRu4O-0NKTcgMnNLcZ0rBgew56G3IOohqGaLSV1ywi0SWGri9tgZyrKBuAzJ8cwZGAXNxYFsdi4yudWUUdBhhoHbpDbr4o5YRX3MYbo7kHqgVEV-fEKb7w1w8FhhFiDelSxRnoe--c_AwBe3iXowo7hXp17Vp-8mf6JS1eDMD7n--bEBHPCv-af1w7sTD3BzVaoafKAL9ccEdwIN35wAEr0UFhdQAxNJMkLIJIu949SSOXFUS9rTHhdMGKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفحه فارسی AFC با انتشار ویدیویی نوشت: وقتی علیرضا بیرانوند روی خط دروازه می‌ایسته، گل زدن بهش تبدیل میشه به سخت‌ترین کار دنیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/679837" target="_blank">📅 01:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
هکرها با ترفندی جدید بیش از ۱۰۰ میلیون دلار بیت کوین از کیف‌پول‌های سرد سرقت کردند
🔹
هکرها موفق شدند بیش از ۱۰۰ میلیون دلار بیت‌کوین را از بیش از ۷ هزار کیف‌پول سرد شرکت Coinkite به سرقت ببرند. این نفوذ درحالی رخ داده که کاربران از کلیدهای سخت‌افزاری فیزیکی استفاده می‌کردند و تصور می‌شد این کیف‌پول‌ها امنیتی نفوذناپذیر دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/679834" target="_blank">📅 01:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef5_QAIu8fb2U9U8quVBwuYSSMDCIxH3uG4-SMDjzcfNLW5gTAA4AhYaLLBgUAKGKawoNjLzs2Y_2PFeV1l7NrcQZ3-Wul1WwPGBIJDAfEu2y9kbgzvR8zY8Ju707s2WkEUQjqMPjJwk5ZLgSr7-8WSpWsK0C0YL51ZRGPyYdYqaABQteS6a2W6laiGqh4aqm90QTLeBYfcH79LS0O7dQVOne4tg7ALlrgCygg6BcfDCZcYkrc2UlwxzYLUKN9ury76Uxg_22tN9__D6qvrk_6Qk2_E9QuR9XTrPf2I5SfcIwY8mZKIYn5PxXzfDT_iL85lDGY_SUAkAfJciIIZ4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: همین حالا باید جلوی خسارت‌های ترامپ را بگیریم حتی با توافق بد
کریس مورفی:
🔹
من حتی از یک توافق بد هم برای پایان دادن به این جنگ حمایت می‌کنم، چون باید همین حالا جلوی خونریزیِ فزاینده خسارت‌های ترامپ را بگیریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/679833" target="_blank">📅 01:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54f13a0af.mp4?token=WISAQ054ZsEb0J4Q6g5zXeYTz3N5Rj08GoR1WhXXNfp3Nf0zXtrtA8n2eHYvDXMqiBHvyR1txTDVIzZwlcmS6igXE7VBSbJAdie09SPeKEhEJ8TF4wsI3OFHzxqAbTonO8eNAT-roIWZG75U3LeX8KlcqqPAWUx60K-jAJBq27ugb66N2tY_BXIReyomQv7xPdaiUeYY5qsTXgdOKLnpL9dAEJ1WCoR_HdpPa27o2rTtidtrUxfhOZK4Kd8_K6eNwyjLqhFrsmBNYsLZXGfVjMgD6QpjiIQVq3e4gVQOd_5MrA5t8xjK3J2zvQs6Sas9Iyx1TD8OOJ5go7aGV3TkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54f13a0af.mp4?token=WISAQ054ZsEb0J4Q6g5zXeYTz3N5Rj08GoR1WhXXNfp3Nf0zXtrtA8n2eHYvDXMqiBHvyR1txTDVIzZwlcmS6igXE7VBSbJAdie09SPeKEhEJ8TF4wsI3OFHzxqAbTonO8eNAT-roIWZG75U3LeX8KlcqqPAWUx60K-jAJBq27ugb66N2tY_BXIReyomQv7xPdaiUeYY5qsTXgdOKLnpL9dAEJ1WCoR_HdpPa27o2rTtidtrUxfhOZK4Kd8_K6eNwyjLqhFrsmBNYsLZXGfVjMgD6QpjiIQVq3e4gVQOd_5MrA5t8xjK3J2zvQs6Sas9Iyx1TD8OOJ5go7aGV3TkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرنگونی یک پهپاد متخاصم در جنوب ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/679832" target="_blank">📅 00:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی تنگۀ هرمز خبر می‌دهند
🔹
شبکه راشا تودی گزارش داد، شعله‌های آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/679831" target="_blank">📅 00:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
برخی منابع خبری تصاویری از لحظاتی که یک کشتی در نزدیکی سواحل عمان، در مجاورت تنگه هرمز، مورد اصابت قرار گرفت و آتش گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/679830" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679829">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c140aa3b9.mp4?token=XbxGdmAl30pJWEkZ-4KxZCAQahjTvFbTR9sSazMFCxx3ArwICZ5I3jwoy8sEoZLgvwJewJ545GS2WEuomT820bZu1qg6b-8tSZ7h1CZ7yFZ8HOoNqXhhenaKinFMYxD_a9GjYgdaSRXBL8NdMexdzTy6IVi3PngAUbSQyDxwgY_Fj0cT0XNRJGd9m-91daRQF-jm-iM57ndPmymp0SFZ6vrIam4OCWT5-N8XxLFbWevOS2MaHe_lNuDk7f-HDBLcxd2qr8Ql94sBezGicDzhw7F29xBnD-8bHczB2jHSD6xNRg_uMCvaZokcoKGC9OsRZV2dYrzJ2uHTTw5IGvr3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c140aa3b9.mp4?token=XbxGdmAl30pJWEkZ-4KxZCAQahjTvFbTR9sSazMFCxx3ArwICZ5I3jwoy8sEoZLgvwJewJ545GS2WEuomT820bZu1qg6b-8tSZ7h1CZ7yFZ8HOoNqXhhenaKinFMYxD_a9GjYgdaSRXBL8NdMexdzTy6IVi3PngAUbSQyDxwgY_Fj0cT0XNRJGd9m-91daRQF-jm-iM57ndPmymp0SFZ6vrIam4OCWT5-N8XxLFbWevOS2MaHe_lNuDk7f-HDBLcxd2qr8Ql94sBezGicDzhw7F29xBnD-8bHczB2jHSD6xNRg_uMCvaZokcoKGC9OsRZV2dYrzJ2uHTTw5IGvr3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منایع محلی از شنیده شدن صدای انفجار در آبهای خلیج فارس خبردادند
🔹
منبع این صداها هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/679829" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679828">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_7xFaJRtkFjKVdn-eE3b7U-jpZVFG-9q7yHuK3p1m-LuyAJID6SaaS7ztQpKOiklepRe2l24Fbc4p1bbE1Rvg0r-2lI8C5w68TGVz61UfTEJWImPB2d-Tnlc4sS0mlF2p1tSSGl3gRlkCU5Pzoxb7kb2TJRksewAyJhYplVAVDa0rUiKuyrQv_S2doFYkDFNP_0i39cbn3qLxarjG2g9PK_hqEnIt_RJavvXsXZVjG4yWjUrW3wc4ljVPHqGx8Ono8BeBjgR0XMUB5iQCFCdbcfgxvHHh-ryvtpTjDpG9-jpAvJUS9ExKEApRl6QAO1FQK-bk0tEOTc0_S6GhuqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره به پول ایران حمله کرد
🔹
دونالد ترامپ طبق معمول پست گذاشتن در شبکه اجتماعی خود را امشب هم آغاز کرده و در پستی به پول ملی ایران حمله کرده و مدعی شد:
«نتیجه
۵۱ سال رفتار بد! ایران هیچ پولی ندارد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/679828" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679827">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
برخی منایع محلی از شنیده شدن صدای انفجار در آبهای خلیج فارس خبردادند
🔹
منبع این صداها هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/679827" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679825">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
موشک‌های پاتریوت عربستان هم ته‌ کشید
خبرگزاری رویترز:
🔹
عربستان در ۳۸ روز نخست جنگ، حدود ۲۴۰۰ موشک رهگیر PAC-۳ شلیک کرده است؛ رقمی معادل تقریبا ۸۶ درصد از کل ذخایر این کشور معادل ۲۸۰۰ موشک که باعث شد تا آوریل گذشته، تنها ۴۰۰ موشک برای عربستان باقی بماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/679825" target="_blank">📅 00:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679824">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اندیشکدۀ آمریکایی: قدرت سایبری ایران در مسیر تبدیل شدن به تنگۀ دوم
🔹
کارشناس سایبری مرکز مطالعات راهبردی و بین‌الملل در گزارشی تحلیلی نوشته ظرفیت‌های سایبری ایران به نحو چشمگیری ارتقا یافته و عملیات‌های موفق اطلاعاتی علیه مقامات ارشد امنیتی آمریکا و اسرائیل، گواه آن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679824" target="_blank">📅 00:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679822">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e44b695b75.mp4?token=kacZ2vn1feS89UAklSWLYMhCNeEumv4Q3MRShDDJ8y9GPSGLgrk1ems59P2hy9VmaktwP4CqqjVrCdFEVa96GHgzQBmHLtvKLOxa8xbt4KLavkY9sRAvZO6Fa8PVcshmVaCcq1t-7V6Imt8kgM5WHVi1GF4a-qRKG4mbQB6OYuvPH5eCn65qSIKCSmb7rLrcuLfUPh5T5hemPWCBOc4GJxGO9C0hGU_R2kn6QoEgIhWa0lIUUeXJmTny9LF2FCUS1xLQWS-k-DPDH83UOmxjqoUOnvxDIIN38Z8YlbMKAfrOMeum7zxrvinbkFmJKQstJf-6Azk4dGHl3SvW35pVCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e44b695b75.mp4?token=kacZ2vn1feS89UAklSWLYMhCNeEumv4Q3MRShDDJ8y9GPSGLgrk1ems59P2hy9VmaktwP4CqqjVrCdFEVa96GHgzQBmHLtvKLOxa8xbt4KLavkY9sRAvZO6Fa8PVcshmVaCcq1t-7V6Imt8kgM5WHVi1GF4a-qRKG4mbQB6OYuvPH5eCn65qSIKCSmb7rLrcuLfUPh5T5hemPWCBOc4GJxGO9C0hGU_R2kn6QoEgIhWa0lIUUeXJmTny9LF2FCUS1xLQWS-k-DPDH83UOmxjqoUOnvxDIIN38Z8YlbMKAfrOMeum7zxrvinbkFmJKQstJf-6Azk4dGHl3SvW35pVCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی مهدی رسولی در خونخواهی رهبر شهید انقلاب
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/679822" target="_blank">📅 00:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679821">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpmUk7zx3tkW0oUQPrb4rfay1b3kJ4pwxUzZKjWkkcJDgfJjMYaL2c2LXhnuxZje7MfrdI49h7hh9gRrqS6Kt4JxhodYbRjZZAo2vykeO4oPXK8rNe6ROY_rqXdkpUt5-vJiMMnjf6FG75NtB3_pK7qFroJROkexaAnplso7k2xXbZbNYLUvayk5wA-0PZwZh-IJih3R3v_bwHY66TsTesVeRQFDl2QrVXO6EZnrLLHomvLImGYxZcTTFUDkKSIVL9QSz-gEdsfUEzr0Kc-iVj_81Y-g121C3Faosf5RB17AIKSdOBUgJWvoMKeD8Ii9ciaj6Qj7zcFRi251OFRfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/679821" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679820">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/140c7347c8.mp4?token=TMFVz6yNlD6MKkxGmmPrdI0FzrHv57PXvuBPjLwcDkOA6xyo3vcDiy5MfN-dzYzENKiIRCpeq6GOilfq8O-wb4_Coe2wQLWh-uw1s9Oa466m2oh1X6ry0JFn1ubAJcUMbwAyXDMGDe1Glw5QREuI9lDY9Ixhjphl0R1OGUe_WDH20kggblbXQN_2oeUpaXBRgrsMEIP46jXK3eLfvlQ78xykDCkaveL3rFMs9qtUsc2Qr4GQ71js9He24S3Bu38PlnsrSfeZNrPBH_6xgg9OXGEcxuplQjJzCKQxBFCZcf3Nsde61OGGM7xZLOeTf2HrejgcnFPIA6M6ECSHgRPdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/140c7347c8.mp4?token=TMFVz6yNlD6MKkxGmmPrdI0FzrHv57PXvuBPjLwcDkOA6xyo3vcDiy5MfN-dzYzENKiIRCpeq6GOilfq8O-wb4_Coe2wQLWh-uw1s9Oa466m2oh1X6ry0JFn1ubAJcUMbwAyXDMGDe1Glw5QREuI9lDY9Ixhjphl0R1OGUe_WDH20kggblbXQN_2oeUpaXBRgrsMEIP46jXK3eLfvlQ78xykDCkaveL3rFMs9qtUsc2Qr4GQ71js9He24S3Bu38PlnsrSfeZNrPBH_6xgg9OXGEcxuplQjJzCKQxBFCZcf3Nsde61OGGM7xZLOeTf2HrejgcnFPIA6M6ECSHgRPdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین بار | فرماندهی که در میدان مسئولیت و خانه، بار مسئولیت را عاشقانه بر دوش کشید
🔹
به یاد سپهبد شهید سید عبدالرحیم موسوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/679820" target="_blank">📅 23:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679819">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdm8vjTf51xmFSOeR3sBHD4gWy51rGFzpAQ6M452l-AY7rkh-wFSS919RMaDjWDYq5dpjfYMgPbmu4E-rIqvZpJh6fYLW4uvWtSAHYELIZUO8kSIRRClyrIhzBdeDRhZvNhnr5tzFJ4AjK0VNBnNbk-FG01ilTGc0e8NFgYeT8XCxeojfD6QpxfQnfPQeODvnGLcdJ2jsf8PLwCGiqIuokLMMLuoByayfR9Fdp2DS5FqVEEOT3kxS2iguAOOQ4EWVQffHPBwLeempayK3gf_12fFTVLfT7Fq_yelPoI903CWnOZUYz6YsPnHVirMTvzgFe6lHlJbdIRsmaTUPIuSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروژه‌های ناتمام در ایران
/خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/679819" target="_blank">📅 23:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679818">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytxxFTngwD7D54RvtPa3kj5Ghg7rCcKh0Z-J5TQkkHvISJZ5rtEgBd-wkCYoCLrUOG_gFRjcmFWQ2YASVQAD7u8B_ftvdUYx7TvZS-2SThWjv8kRLTuhgAFlCVDCs4sNIQWRSg4znUCdcOKn--rAA9MlEcOjGWR3dDOPyN2P67X3YQg3Id7s7B9h2K7H-yL4XKKIah8loVwm145NSnKCeg2k7ufS9WXdM4Z3mSWcfIk0TMDMaXS4Rwh1DCG7v-kT_I9sNzcEetnxEsSYCMdT0TB6rWdx6OsUdZVjltDbdRGdEr-4q1tsjdhBADPZrnEBwwrUKNeQt-edhN1qLBCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین برآورد موسسات از قیمت جهانی طلا
@Titretejarat</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/679818" target="_blank">📅 23:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679817">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f416e4e6d6.mp4?token=l2Um50z-TaNw1qb0RWrWZT4lbNXwXV1L1RAZTuWb-phhdj7jG4Hw4YgBqgm_7E3du9FXGfY3gsfTf7ADdAPQWKugep7KDllnnVjVHxA5QQYB_v4hGrBuO0OwLPPZnTj-ByoKTPEy1i9PALSS0Um4npZrr1q8qWbfioCRdsHMhI-WuiK0tFDX-3Rh0DEb83NQO4lzLb_QtD_yqcp0DFRICZmF81XTK2BVZxMUdrYqtl85PawFUYYWP_UIa7hjEVtkyYnXETQGXEtsQBKsxISsu1gRx2cIPHm7rBfGc2CasgHkcT57-rHcBD78jGNc1w0CkAsytTfG3hsnWfms1cc2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f416e4e6d6.mp4?token=l2Um50z-TaNw1qb0RWrWZT4lbNXwXV1L1RAZTuWb-phhdj7jG4Hw4YgBqgm_7E3du9FXGfY3gsfTf7ADdAPQWKugep7KDllnnVjVHxA5QQYB_v4hGrBuO0OwLPPZnTj-ByoKTPEy1i9PALSS0Um4npZrr1q8qWbfioCRdsHMhI-WuiK0tFDX-3Rh0DEb83NQO4lzLb_QtD_yqcp0DFRICZmF81XTK2BVZxMUdrYqtl85PawFUYYWP_UIa7hjEVtkyYnXETQGXEtsQBKsxISsu1gRx2cIPHm7rBfGc2CasgHkcT57-rHcBD78jGNc1w0CkAsytTfG3hsnWfms1cc2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌‌های آخر الزمانی در کانادا؛ آسمان نارنجی بریتیش کلمبیا در پی آتش‌سوزی‌های جنگلی
🔹
با ادامه آتش‌سوزی‌های گسترده در غرب کانادا، ویدئوهای رویترز از نارنجی شدن آسمان یک روستا در استان بریتیش کلمبیا خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/679817" target="_blank">📅 23:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679816">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
سناریوی تازه درباره احتمال حمله آمریکا به کوه کلنگ
👇
khabarfoori.com/fa/tiny/news-3236499
🔹
جزئیات تازه از پرونده قتل یک مداح؛ پای یک زن در میان است!
👇
khabarfoori.com/fa/tiny/news-3236583
🔹
ادعاهای جدید محمدباقر خرازی درباره رهبری آیت الله سیدمجتبی خامنه ای و شهادت سید ابراهیم رئیسی + ویدئو
👇
khabarfoori.com/fa/tiny/news-3236624
🔹
جنجال جراحی زیبایی ۴۰ میلیارد تومانی خواننده زن | چهره او چه تغییری کرد؟
👇
khabarfoori.com/fa/tiny/news-3236501
🔹
سلاح های خطرناک ترکیه | آنکارا با این چند اقدام مرموز می خواهد قدرت اول منطقه شود
👇
khabarfoori.com/fa/tiny/news-3236597
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/679816" target="_blank">📅 23:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679814">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43fe88aaf.mp4?token=pPxtiXmGrsYoU9Z3i2x__PVBf300UShfD2OEisV6qysXPU0w_viG4F23aeo4aRDPb-CQusP0QTMKfaZuvG9yi7jFnQiAMMLqCEUSyQyv49VYjL8OraA8BTnbT-4GJEUOu0zmn_5J9kws3U9oH-o9EgdQXIFVRKgHwwVhJ8PkqkZYyNEZ5bHDmQB6tI2bhaPM76KzNXpkEM2_e6IdP-VPiG0ji-iCu_TunEDT0BM6U1XavnTFUXe3Z_3tAVxkHEZQxa8zRjp2OdBkgZ46_HcNj4ShWlt_mVs6aAXY-u1Ix08NeIGFsp2Bd9xjcLHhzKeIhhvtz7kG8NFnO-vGYxuFIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43fe88aaf.mp4?token=pPxtiXmGrsYoU9Z3i2x__PVBf300UShfD2OEisV6qysXPU0w_viG4F23aeo4aRDPb-CQusP0QTMKfaZuvG9yi7jFnQiAMMLqCEUSyQyv49VYjL8OraA8BTnbT-4GJEUOu0zmn_5J9kws3U9oH-o9EgdQXIFVRKgHwwVhJ8PkqkZYyNEZ5bHDmQB6tI2bhaPM76KzNXpkEM2_e6IdP-VPiG0ji-iCu_TunEDT0BM6U1XavnTFUXe3Z_3tAVxkHEZQxa8zRjp2OdBkgZ46_HcNj4ShWlt_mVs6aAXY-u1Ix08NeIGFsp2Bd9xjcLHhzKeIhhvtz7kG8NFnO-vGYxuFIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره‌ رئیس‌جمهور به فعالیت شبانه‌روزی وزیر‌خارجه با چاشنی شوخی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/679814" target="_blank">📅 23:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679811">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukSVwJac2Pmgs3preeG-vIK4HDHli5oXn4NF9OJtQDsYSn3o7zG9bHjtEf-57Ns4MS4bJfuqZUhPF-rCjGr4hZBgfUtnqghQmHy7FxS6Ss7G4e_sqiVTaPpokbiu6xLKesgN4gFWJjwSFuJZWjp64YZC37P8hdgmmTMW3Rp9R8E0Jsk9LqGYL46lsZfuq6_1zNVxHQARxeG06YrTdm1bUiYY6O94jItsVQAs-v-MAk12Co9PAtUin9k0Bepq9XCsGwNP31g5rH1Q9GUqANq_EYrBRpCGA1TEdJ3AAF3-FRdFJMcsgvILl-L6JzYTKqfW3jr3_sDfG9-x7QEjmVkFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448edf4631.mp4?token=rHpnRfMuyqXwEsA18QCu7esM4EWMWZmRvF2SUNvud4vVQ4ENAtlBe0GEiJVfwn1OzBJpP59K4QCVJCokqY2bZEC6LvX9TedJgXR0614FQrgngLMbTwfo_pB8LvmcVaPlGYjXyi38n1RP56NUwPPT5uKfzyMgmhRS6hFj9vYb3sb6cdkRbiBzYqSTrH3GfXvFCiFYoXkKvlMSgf6GdXOgeCCfc9C6HBpyld16vfmp3CzG2sX1Pqqfdcc6cB6NIHQ_JAz8fhOmEbd2IAvu5XVJPvFoRaBvS8tPFBWVbVQP1lA5gRxZenmCCvglq4wrt14clVtW2IoYDuUhkSpHGHC7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448edf4631.mp4?token=rHpnRfMuyqXwEsA18QCu7esM4EWMWZmRvF2SUNvud4vVQ4ENAtlBe0GEiJVfwn1OzBJpP59K4QCVJCokqY2bZEC6LvX9TedJgXR0614FQrgngLMbTwfo_pB8LvmcVaPlGYjXyi38n1RP56NUwPPT5uKfzyMgmhRS6hFj9vYb3sb6cdkRbiBzYqSTrH3GfXvFCiFYoXkKvlMSgf6GdXOgeCCfc9C6HBpyld16vfmp3CzG2sX1Pqqfdcc6cB6NIHQ_JAz8fhOmEbd2IAvu5XVJPvFoRaBvS8tPFBWVbVQP1lA5gRxZenmCCvglq4wrt14clVtW2IoYDuUhkSpHGHC7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توئیت سفارت ایران که آمار بازدیدکننده زیادی پیدا کرد
🔹
ترامپ رسماً از رئیس‌جمهور به اسب شخصی نتانیاهو ارتقا یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/679811" target="_blank">📅 23:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/679810" target="_blank">📅 23:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679809">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های بالستیک و پهپاد یمن به مواضع ائتلاف سعودی در منطقه المخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/679809" target="_blank">📅 23:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679808">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❇️
کمک فوری برای درمان 2پدری که حالشان خوب نیست
🔹
پدری ست بیمار، مدتی است به دلیل سکته در بیمارستان بستری است و تحت درمان قرار دارد نیاز به عمل دارد که هزینه آن حدود 25 میلیون تومان است ، وضعیت مالی فرزندانش نیز خوب نیست و نیاز به کمک مالی برای درمان دارد.
🔹
مورد دوم:پدری ست جوان، یک فرزند دارد متاسفانه به دلیل سرطان معده  تحت شیمی درمانی قرار دارد نیاز به دارو دارد ، هزینه دارو بالاست هر دو هفته بیش از 40 میلیون نیاز داردبه دلیل ضعف بدنی توانایی کارگری ندارد و با کمک مردم امرار معاش می‌کنند.
🔹
مورد سوم:دختری ست جوان ، پدرش به دلیل فقط مالی توان تامین جهیزیه اش را ندارد و بیش از یکسال است که عقد کرده ، نیاز به کمک مالی برای تامین چند قلم جهیزیه دارد.
✔
پرداخت انلاین خیریه نسیم وصال:
http://www.nasimevesal.ir/payment-new
شماره کارت بانک ملت : ۶۱۰۴۳۳۷۸۱۱۴۱۶۲۳۷
شماره حساب بانک ملت: ۵۸۹۸۷۷۱۴۶۵
شماره کارت بانک ملی: 6037997599156198
شماره حساب بانک ملی: 0219934010000
شماره شبا: IR310120020000005898771465</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/679808" target="_blank">📅 23:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679807">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌های بالستیک و پهپاد یمن به مواضع ائتلاف سعودی در منطقه المخا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/679807" target="_blank">📅 23:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGTx0yvPv2Akc-F0Yo0tvgbIh4JVJRtdFOSZzdQYq7niqQv0wQgNfHtJrRW5bDQaEifJuPi9eQ7mdpiBHXtv5mmVZBR-1JlPWd9SdkvmXYfxlKEo2b7lupYfuS8EzOOyUE0hdz1ZADyd1oiiCSXmfklCQYLQ8NErkF-FjOSUoiyBoLErDtRiKy9Vuv6lBe9Xvcr5-jJ2jVU0O-uv7vrznVKSEanUK5B148oxAL506V2IPavWe7TtcwtOg-wLtexM4sl8TcSXOXrQkSpKT2fGTQsNUd0w1oOY2cdop1mlMMGPV_dzkV2v2VWC185uvVoDfz_TdWyJPU_kKLzn5Od5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/679805" target="_blank">📅 22:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onq8VovS0T-LVP_jhGsemJPQ9fwvbrvEnSdhmz-dheiJWlYrXwvaImELytOeaSwjQIP-tHwXiH1jIxhRXD1X7XuCkqNCXWJjmjxutWxtb6Av1Sw9FxooqIdiazWyCRHkrrRSP6hvamkcIrFchFFSm4xZEpqPHw0GQjpsHywfl_1jyClWSaQdKGyPbeNP6sCRU-5_QRu0NJkGR8IqMH4Y4F462KypY3rYbfDvu49gXiWHNrjOoS3OE4jQlDbDzxtFm3UwStLn9MP8-KkF5I1JEPCm8fvA114VatY8Uj3JFK4FPXz6hKjJUhEPQ2S-o8wM3B3YFJEUMJvA7EZcQuAk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار امنیت
🔹
با حکم دکتر مسعود پزشکیان، رئیس‌جمهور، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد. رضایی با این حکم، مسئولیت دبیرخانه یکی از مهم‌ترین نهادهای تصمیم‌گیر در حوزه امنیت ملی کشور را بر عهده خواهد گرفت.
🔹
هشتصدوسی‌‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/679804" target="_blank">📅 22:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679802">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c8ba41d7.mp4?token=a89emb1mWuh2nUhuJXQaQ37Cq8vjseYxZ13XNNw5mHQl2_gddsThZzreFch4deazGgSEqeqEhMWwY6t9sPEnp2WzUgiUESzGijxATQGRnf8mWLblG1Og6t3T0uNnjCSyjZfTIB0mWh_4qeNerRNqpGMwiehK1rspDrxjz3bfaTvA9Ce7eSp7N_2OoSa7GE8GCcE31lb2ogBMypfw10qcjFYdPuELiyOTTjaRxQLQjMiQpZQ_glATXw0aelvhGn8psNbZ_I56WPMSlYDyxqgS3Mg6h3qmEMJoUiCn5-5YI6bBQO1BtIX2cJtDHVkSbcN0v10tEWZ2tUYpBAsY79Tr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c8ba41d7.mp4?token=a89emb1mWuh2nUhuJXQaQ37Cq8vjseYxZ13XNNw5mHQl2_gddsThZzreFch4deazGgSEqeqEhMWwY6t9sPEnp2WzUgiUESzGijxATQGRnf8mWLblG1Og6t3T0uNnjCSyjZfTIB0mWh_4qeNerRNqpGMwiehK1rspDrxjz3bfaTvA9Ce7eSp7N_2OoSa7GE8GCcE31lb2ogBMypfw10qcjFYdPuELiyOTTjaRxQLQjMiQpZQ_glATXw0aelvhGn8psNbZ_I56WPMSlYDyxqgS3Mg6h3qmEMJoUiCn5-5YI6bBQO1BtIX2cJtDHVkSbcN0v10tEWZ2tUYpBAsY79Tr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره‌ رئیس‌جمهور به فعالیت شبانه‌روزی وزیر‌خارجه با چاشنی شوخی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679802" target="_blank">📅 22:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679801">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
کارشناسان چینی: ادعای ترامپ درباره بازگشایی سریع تنگه هرمز، صرفاً یک خوش‌خیالی و خیالبافی یک‌طرفه از سوی آمریکا است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/679801" target="_blank">📅 22:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVIcBgqZKVC1nVxfSNmBu8sHHpWEd_PA8UZyW3YbyBjoZ3r3aYmQo3mb5FWmM2HIhtdLkuIeGIjQRq8RTzbddeKburFl0YWS57wx6-uHFIiS-WgFAAsPHALHBIE_GdYoM9JlkRyQLnw0rp5wusw3_LZXu2sjDZu4EVfWsURaeKE8JJL97ucMBlbegAOndAh8zU130xIc3KbLzZO-uQlci_KJuyiJSPVNXt9_HjEMIEgNK0kOA-y9lTOsnkpJplZ9USFr5fKmM2F9wZxbzG_P316aKfU4pRiYfvzcIUNOFOseaIBwwbAEvNFNbHOHBMfMOnZDd39PSZYyXEw1kJaCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای اولین بار فروش مستقیم
در اتونوین
🚨
برای اولین بار عرضه مستقیم خودرو 《های وارداتی》 در اتونوین در تاریخ  1405/05/19
🔔
در این روش، مشتری بدون نیاز به بلوکه کردن پول، وکالتی کردن حساب و قرعه‌کشی، می‌تواند خودروی مدنظر را انتخاب کرده و
۱۰ درصد قیمت
را به حساب شرکت واردکننده واریز کند و سپس برای تکمیل وجه و عقد قرارداد در سایت شرکت عرضه کننده اقدام نماید
📌
اطلاعات تکمیلی مدل‌های قابل عرضه در این مرحله از طریق پلتفرم اتونوین در بخش فوروش قابل مشاهده است.
✅
اخبار و اطلاعیه رسمی عرضه های آتی در پلتفرم اتونوین را از شبکه های اجتماعی اتونوین دنبال کنید :
👇
👇
📲
تلگرام
💻
کانال بله
📸
اینستاگرام
🖥
سایت اتو نوین</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/679797" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhpXF569MGsya2V97cPha1tkSNEj3y4UdhW8vtDnUF4lJYkttbNnAGF6sDwEO_SkTFHUGWS62hV1p1FugAeceezesmRtJlRVE7h1VrDYCj8Lxj3TnmMYUe_y2lTrMG_qPiZcBBaS4on3NJA55fUbMiKnxHaBa1Vi_Jpecfrl9RKhlpRVxmSxe1-PuKgyNFG6m92eXWbizDPGD25H85GGvgpVOy1fi0X-lkDM7b9RROdcOR513tlHdM3y5mLtaF-68QBZm3S-5RMZpHXR8UYPk5XUE0EDiKkKsxggUOq_MUJMYbUQ3AJgVZdw55i8qQ4eBwSYwUHMbKbmn_rRkpwXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زندگینامه محسن رضایی دبیر جدید شورای عالی امنیت‌ملی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/679796" target="_blank">📅 22:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18b6ab1f9.mp4?token=MVdvuDTyRtRLG5fBJ3Sw9K87ZUKYT5LjfG_StlJ2jj6A_AccTBxWC_-_TkVCsWaswiSpLL-v8pd7bi7nLZaZs7pB4PEzwmCtOamcZ5_7VFkSIx81qhY6AV6B9wPmO5VL6d_ufIyciuUPzs17XOadiZnQUZnbLj1e0nkhQ7MAtLlr4wRWO5KzfEFfyXtlgI_vlSx5C62t-boUqOVT1Y0xYW7geCZtPKo9KjBy2zTTUZ-xjVJwSmu69YWBcGkQgh15D-yFLqT_XvU2AY-hlsUFEsx53GgpoUmfwrpWzG6VmsU4uyIAg7jUyvrt01_k3_F0vspwvOcx7gdsb95ynPBPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18b6ab1f9.mp4?token=MVdvuDTyRtRLG5fBJ3Sw9K87ZUKYT5LjfG_StlJ2jj6A_AccTBxWC_-_TkVCsWaswiSpLL-v8pd7bi7nLZaZs7pB4PEzwmCtOamcZ5_7VFkSIx81qhY6AV6B9wPmO5VL6d_ufIyciuUPzs17XOadiZnQUZnbLj1e0nkhQ7MAtLlr4wRWO5KzfEFfyXtlgI_vlSx5C62t-boUqOVT1Y0xYW7geCZtPKo9KjBy2zTTUZ-xjVJwSmu69YWBcGkQgh15D-yFLqT_XvU2AY-hlsUFEsx53GgpoUmfwrpWzG6VmsU4uyIAg7jUyvrt01_k3_F0vspwvOcx7gdsb95ynPBPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع «حادثه امنیتی» در نزدیکی باشگاه گلف ترامپ در نیوجرسی
🔹
فرماندهی دفاع هوافضای آمریکای شمالی اعلام کرد جنگنده‌های این واحد، دو فروند هواپیما را که به حریم هوایی ممنوعه در نزدیکی باشگاه گلف دونالد ترامپ در بیدمینستر ایالت نیوجرسی وارد شده بودند، رهگیری کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/679793" target="_blank">📅 22:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MID_7adHGYZO2DhzzM0AGt4NNMOl4i_6JjZaiDa6UlL5wn_MUiGxOawVQfSmXS2qVL6uElz3zUxH6dbvvG6qcud99PU_kRm3TRExLrgdg27YGU9jbcPmraPEIzkMhStCo6rwh63-Pt2K5Fy4CpU1lpZYeewjZVGFjHJzPmtv2v2KU2bqN3MwYxrDqukkmT7NShAV-Idw1OJUS1yakr9F_EtnIcTnjbaC-HjLJTIW_6MfNaUmZvMAmw2OE3TufWaGD_vna_LoxiVBfVhUmlqp0q6EjMbC5ao4H1f7UCwGhdByCHsIh1cuI1PXsDdKIg79RGI1ls6YhTzwVvMgKjK04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسی که نعمت‌های کوچک را نبیند، قدر نعمت‌های بزرگ را هم نخواهد دانست
🔹
این سخن یادآوری می‌کند که شکرگزاری فقط برای داشته‌های بزرگ نیست. توجه به نعمت‌های ساده و روزمره، نگاه انسان را عوض می‌کند و او را برای دریافت و حفظ نعمت‌های بیشتر آماده‌تر می‌سازد. #ن…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/679791" target="_blank">📅 22:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679787">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/679787" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679785">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOOPAvi9RqUVDB85F2W0LDMHOOw37E8WPhh1pGILYhUvS-2QLrqp-OX-ICo-tK1t_i6hvGnMDQJdzb7Jf2zv320a7NZxOHDyAztPajG85iIjSPD7sCMnqAlERyNs2E-j4ZueYtZRtm4Rduye5KoMkLa9_9N-UeRI0268aFb6nQX0ZMx4slOhpYdr7I9bP5zFIXA-qTqm9qM0q6G9App5YbkEjZQ2N2CXU4VcvcPoEfNP-uJhxvkRZuuGzGprnUVKhGpPLEYie1HWhEULNLn374p4T1aI2DKtO30SRaJesW62SUn6VzqSwvOSpGcRafE2Bp8cwSF3dlkrflpcuzY7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس قدیمی از مسی در کنار خانواده و فداکاری مهم پدر
🔹
وقتی لیونل مسی ۱۲ ساله بود، پدرش از او پرسید: می‌خواهی به روساریو برگردی و در کنار خانواده‌ات بمانی، یا در بارسلونا بمانی و به آکادمی لاماسیا بپیوندی؟
🔹
مسی تصمیم گرفت در بارسلونا بماند. پس از این تصمیم،…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/679785" target="_blank">📅 21:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679784">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fbbd9ebf.mp4?token=YhcnOmuoAFBlCPknPOko_yIPAH00qJKgODgMXWPMs-AGNtE2E04muXqj_Yv1tcPgig2xKxM9VI5XKTr0I5zobAjuiiO3dhUyvkl7bCsWTYjWeSc8CRecs7Dntke61M8iq91QkkRymBhgbGQ05S55sIpI6c-ZhqAgIJDZ8jvgsl_W7iTkdHsTcHWBibKd_qmTA9Fu885isT7Atmnia3iib8BFp9IUU4smf8KlPOXI2haCUuAZ_SK7ZLxzwFqQqgHp-DSOMnuzklGePJt_yt8xereG5Y6oifcua7vtLpqEXeSfMwIFYeMtQCpJtdzN_5KK_AwhpImxxRB-EV_0ePE2Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fbbd9ebf.mp4?token=YhcnOmuoAFBlCPknPOko_yIPAH00qJKgODgMXWPMs-AGNtE2E04muXqj_Yv1tcPgig2xKxM9VI5XKTr0I5zobAjuiiO3dhUyvkl7bCsWTYjWeSc8CRecs7Dntke61M8iq91QkkRymBhgbGQ05S55sIpI6c-ZhqAgIJDZ8jvgsl_W7iTkdHsTcHWBibKd_qmTA9Fu885isT7Atmnia3iib8BFp9IUU4smf8KlPOXI2haCUuAZ_SK7ZLxzwFqQqgHp-DSOMnuzklGePJt_yt8xereG5Y6oifcua7vtLpqEXeSfMwIFYeMtQCpJtdzN_5KK_AwhpImxxRB-EV_0ePE2Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان پزشکی قانونی کل کشور: ۳ هزار و ۵۱۹ شهید در جنگ رمضان داشتیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/679784" target="_blank">📅 21:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjJw0hjstgEEFzIWOIX-fac128wHypjlC4HwL_VtI85YsILTSnTgYS5ulv-4lh68dTtPAj1Hcm036PadqMkAmcdy6aahmLIE0xfSW54Bvgk0aefDm7-Y8pIH6JnG0lMtxL0JGmi63hZR5pAMOT2JuXViINo37j2IeAcgnPQr-TZLQJnk1eNcho-06QAWQxlRbgtR-_5NXDUNBNjCYgH3UCq0-fyo0-YGnb4qo0ocP89DEzKf6IuDdmcSiMF-IZM7xwwuhUQ1Xb8aEvthsUuAWcd71mE9A7kaAfbyZkOqzYCaTAk29oax-7iEXiOjuQRoQyAFb7zAjEDwASfg9BJefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امکان مینا
🔹
کارگردان: کمال تبریزی
🔹
ژانر: درام، عاشقانه، سیاسی
🔹
بازیگران: میلاد کی‌مرام، مینا ساداتی، شایسته ایرانی، بهرنگ علوی و…  خلاصه داستان:
🔹
مهران، خبرنگاری جوان، زندگی آرامی در کنار همسرش مینا دارد؛ تا اینکه نشانه‌هایی عجیب، او را به رازی می‌رساند…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/679783" target="_blank">📅 21:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679782">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای کانال ۱۳ اسرائیل: اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/679782" target="_blank">📅 21:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5455897411.mp4?token=MYYpJOj_DzkoteDSSviDjqlQNl0EFhKgOmdL5GWGNPC7fE2VS4DyAlvMJBO-zfVsADsPhSveZ-jQGKoAuUbzUQAtLHhhNMJtuuhhiFL-bb8lJF-Vp34cZtOaEG8vOhwg4cjdRlDp2Mr5jwFQbZaSit-lky3mZy1ZB85o_cNvguerSkF-FFgl6faw5M7DkclHavtz0ZoCTePMamBksVtz6GXpZo0O3dtLdMTP43S7v3nmVghiI7npqvG4ybJi_mS3mfwH9zLoZVnnKp75CBRr-p7jslkB4fRYq92CqMynQu3RmoQJIsl2HFOIbO4HTZv1FiPciWsUTbRiW5KalC38eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5455897411.mp4?token=MYYpJOj_DzkoteDSSviDjqlQNl0EFhKgOmdL5GWGNPC7fE2VS4DyAlvMJBO-zfVsADsPhSveZ-jQGKoAuUbzUQAtLHhhNMJtuuhhiFL-bb8lJF-Vp34cZtOaEG8vOhwg4cjdRlDp2Mr5jwFQbZaSit-lky3mZy1ZB85o_cNvguerSkF-FFgl6faw5M7DkclHavtz0ZoCTePMamBksVtz6GXpZo0O3dtLdMTP43S7v3nmVghiI7npqvG4ybJi_mS3mfwH9zLoZVnnKp75CBRr-p7jslkB4fRYq92CqMynQu3RmoQJIsl2HFOIbO4HTZv1FiPciWsUTbRiW5KalC38eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک نقل‌قول جعلی منتسب به سردار وحیدی چگونه از هند به سخنرانی نتانیاهو رسید؟
🔹
هفتۀ گذشته نتانیاهو، نخست‌وزیر رژیم صهیونیستی گفت شنیدیم احمد وحیدی، فرمانده سپاه پاسداران به صراحت قصد ایران برای ادامه توسعه سلاح هسته‌ای را اعلام کرده است
🔹
درحالی‌که برای این ادعای نتانیاهو هیچ منبع اولیه‌ای پیدا نشده است؛ نه ویدئویی از اظهارات سردار وحیدی، نه متن سخنرانی، نه گزارش رسانه‌های رسمی ایران و نه تأیید مستقل خبرگزاری‌های معتبر بین‌المللی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/679779" target="_blank">📅 21:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa5gi5INOOdcxU2Iee198BNObY0fW8cIlFLc8uTSO1QuKG5qwF-WqugQ0ubEIdeiB9xrTKpTOuMQ_vE_LZMPb5yxuevWoG9NtuMCOFT4gnmHURJDYqq1Qf3i6cEgifUecddte_Yrm9XsApunMdu5qCipOCF8rsOcjNeVE7LE03DePQI_19bo_AFcs_ItfMrSA59tNBuFcBtY8VOd0Ca3k2GuNSKGTPXUVeET7Jo8UVSkcmj6fl-1RGORqZv5DIJthLFHDlRfGoWVWrb20LRa6s9LkUURj0107UTi7I7wGM53hoKhbKY3WC27wikiPWgUBR3nSDTw4v8VmvmHp3ZRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/679778" target="_blank">📅 21:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
انتصاب دکتر ذوالقدر به عنوان مشاور سیاسی رهبر معظم انقلاب
🔹
رهبر انقلاب اسلامی در حکمی آقای دکتر ذوالقدر را به‌عنوان مشاور سیاسی خود منصوب کردند.
🔹
متن حکم حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای بدین شرح است:
بسم الله الرحمن الرحیم
🔹
برادر گرامی جناب آقای دکتر محمدباقر ذوالقدر؛ باتوجّه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را به‌عنوان مشاور سیاسی خود منصوب می‌کنم. امیدوارم در انجام این مسئولیت و در پیشبرد آرمان‌های انقلاب اسلامی، تحت توجّهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله‌تعالی‌فرجه‌الشریف موفّق و مویّد باشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/679777" target="_blank">📅 21:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUnfz6rMb0-QnfXfKEkKbYyIvX6JafF6NkbHJlJYcLYQk8ul6fIeRtTpSdD8ss6qU29KgOWtEiczcgxAuzpze_zRiwNnNczBXW9qvWC7bfWt9BNLPVgsP-z-_3sGFCLGvaivXvaF05aH1DeB98iTQHKSHyzzhFVyMGMaD_qyonWSZEkDLZsT5kKKyaDGpp_khJCzV0-hRYPhjQwgkgj1ZAWOHmT9lYxGf1gA6ooFw4jHfjX306AyoE60fjL649iMD5QWKv_6y-graHh1nrLUzQmzBlm_9alH2_QPDxD8ykFqA5dkV33kfdOyjR3xBqsgDfEQidwo61WdHgvqDcQY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگاری که نامش با «روز خبرنگار» برای همیشه ماندگار شد؛ محمود صارمی
🔹
محمود صارمی، خبرنگار خبرگزاری جمهوری اسلامی ایران، در سال ۱۳۷۷ هنگام انجام مأموریت خبری در مزارشریف افغانستان جان باخت. شهادت او یادآور خبرنگارانی است که برای رساندن حقیقت، حتی در سخت‌ترین…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/679775" target="_blank">📅 21:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HITaXt4GRrvl3SG1fgSVmx3OqpFKKAQowSBubHPO3ddpyjfodHAJ6ZEP01NTPCbI8bzE199d9N4COUq1rllS_CSdj454asQZROWQDFzWahkrzQ9_0uXnkwkmrHWsG4LM-QKuIY6fem6g88GnyIxLolKp4u7d-EvooV4BYb6P2kNRMhyDAy-lX8IyI_YhbCngkr9etVntU9UOMbad89z5i2ltPr5O0Woy2gMkrPE7-5o7s6LrC7zZiKmhIn2SEwPF_wlNkAyoekdw53F_Lt5gsK1FJW1Z3wBTnvEKNQXZPpei2PunWIMWCIlYrOFHwDe9aAoW7bAJDa0TyvF6ZvTGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
📍
فرصت ویژه دندانپزشکی
📍
📍
🦷
در کلینیک
سرو cip سعادت آباد
✅
۵۰٪تخفیف لیست قیمت
✅
۱۰ سال ضمانت نامه و پالیش رایگان
✅
شرایط پرداخت اقساطی بلند مدت ۱ تا ۱۲ ماه بدون سود و بهره
✅
۲ واحد کامپوزیت رایگان
✅
تخفیف‌های ویژه محدود
👇🏻
👇🏻
برای
✨
۱۹ نفر
✨
رزرو امروز
همین حالا به آیدی تلگرام زیر پیام دهید
👇🏻
👇🏻
@Sabericlinicvip
شماره تماس
👇🏻
09384307498
📩
ظرفیت پذیرش شرایط ویژه محدود است
پیج ما رو دنبال کنید
😍
✅
👇🏻
https://www.instagram.com/p/DblisM0iNTa/?igsh=YXZ3MnZ6d214Y2Zr
sarv_royal_dental
✨</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/679774" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-vmwuXECtFfqh4Br_JDGY3XVQp5HBtyUQXoqOBCACB2Qa_sRY3EuRcxqh-g4fzI9PbsY2r8cuD0CZO5zN0taaBTDXG3pXH16INPBqhDGZ3SYREhxS0gZfzDa_O0Q-QmYEF-jrq5XIv_hdftXeTIdAooymfmttlENXswtmGCRvE3P3CfEwBu-q5X4z50F-gnaHlwAKj-6RwQNJbEA_--LinAxdrT_jBzs_otp9i0Tc5zGvcKFsXE09Uu3rC2ekRQuhrMVOkAIgIUnFKoifrOLDFIEVufiHVawEaESjqfpjt399E-FVxRAICqLCdwCWrglF2uSC4lvSVK8A0E5Dp3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی ابریشمی، انتخابی مطمئن برای معاملات ارزی شما
✨
💵
خرید و فروش انواع ارز با نرخ‌های رقابتی
🌍
انجام حواله‌های ارزی به سراسر دنیا
🔒
تضمین امنیت، سرعت و شفافیت در تراکنش‌ها
✅
اعتماد شما، سرمایه ماست
راه های ارتباطی با ما:
☑️
شماره تماس: 09158516875
☑️
لینک کانال  تلگرام :
@abrishamiexchangee
لینک واتساپ :
https://wa.me/message/32HOPV4AHR2HG
اینستاگرام :
‌Instagram.com/sarafi_abrishami</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679773" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvArDR8_4UYLfigJudaO5chgQF8Siv7h1gZtWXT-WaeFbOd2Gq2yuyLgN737hkupBU0fjSMERVI0WeG02_ZofmS-aShJgB7JCbzrS6Fp8G0mpbcjZwzAEHioIr6TnaahiKS3qcGnef4uxQViEkUpKqeQTFFF_WCjoNcGdlNxr-NF51wsTyKOCwahAFyPH0lVLXJBsq38HaDjpPxlHKHx82peMEi21jwlqmv6guqWuIc4YD42eQ9AGc-6v4ZqYXaJ54NSSsY-6l0LvJuC1g1ORMHYXQQDwoYag6iKfYnTcYL0UCfEdd7YW8mvbuWuxdfCIyR6AHAbWhDRbtjxPAUTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز عجیب پنجه‌های کوالا؛ اثر انگشتی که با انسان اشتباه گرفته می‌شود
🐨
🔹
کوالاها اثر انگشتی بسیار مشابه با اثر انگشت انسان دارند، طوری که اگر ناآگاهانه توسط یک محقق پزشکی قانونی بررسی شود، او حتی نمی‌فهمد که این اثر انگشت انسان نبوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/679772" target="_blank">📅 20:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
احتمال پرداخت معوقات افزایش حقوق بازنشستگان تأمین اجتماعی از ۱۰ شهریورماه
🔹
پزشکی قانونی: ۴۰ درصد از شهدای دو جنگ اخیر با استفاده از علم ژنتیک شناسایی شدند
🔹
رئیس لالیگا: دوران اینفانتینو به پایان رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679771" target="_blank">📅 20:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwBjgq7bRXSmyw8LfF3eTPZfhUo3QOACFGfB7RfxB-PQN4Mo26hK2SA2GXrni_HgWZ6VZCp8cGQqoHhqLVwiWC-UCtp6MlIpFV_9il4AL8hU5ce4cUGMode5bkurwjqqmnCp12vTQhLr0Drjkd3MW4algO60zwhensaAEsi9a43b1SqY19vxUPtwsqr8rLxD3tAga_UaljIWCvKPkzPNWw14kVtOS2CLkpkgKATPf_OwR574GBI51hx4FPfpF8vC9bRVLLjIp06viEJFlGvLfv3dyd5eAESEcGOnkIdwJtxRwMko9kkN4WtOgnG_sVVutZT07A5g8rInlaEbduxF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
هیئت غریب مدینه برگزار می‌کند؛
مراسم عزاداری ۴ شب پایانی ماه صفر
🔹
سخنران: حجت الاسلام دکتر رفیعی
🔹
مداحان: کربلایی جواد مقدم و حاج سیدرضا تحویلدار
🔹
با اجرای: رسالت بوذری
⏰
از دوشنبه ۱۹ مرداد - ساعت ۲۲:۳۰
📍
مکان: حرم مطهر رضوی - صحن غدیر</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/679770" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
با آرامش با ایران تعامل می‌کنیم
!
ترامپ جنایتکار در مصاحبه با آکسیوس:
🔹
ما با آرامش و بدون تشدید تنش، با ایران تعامل می‌کنیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/679764" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuNc3zR6eoQRZCmpACo8XnNTFLqc_AQzf1MWMfUPOalYCt-gXGW4wYc3lRl-QgemM9F29ayJOj_yILH89gMkBHx_cWKJlI9uwr_0YGrXa2H2Dow4gzj9rv01Fc0gF0TWC048h-3eNil-HtXj00v7o2lknTPNJvTw57pbsgb7xJvKUQsOH9eUQ4xKJP73h1ztqqyWtepOtj1wSkJhl0br0egBTKRs2qLTUsrtwp7iVhLca1bb5ccGJFHUBHWS4zyqAFC8GAfQlKglm621xLFUCcA3N7hCvVSi7FyPparUsSo_OY2B7wBgfUMszTBeC0PFtpTqELn6t52qTi5pRrjK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حکم حضرت آیت‌الله خامنه‌ای محسن رضایی به عنوان نماینده رهبر انقلاب در شورای عالی امنیت ملی منصوب شد
🔹
حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی در حکمی محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند.
🔹
باتوجه به تجارب ارزشمندتان بدین‌وسیله جناب‌عالی را که از پیشگامان دوره‌ پرافتخار هشت سال دفاع مقدس هستید، به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب می‌کنم. امیدوارم در انجام این مسئولیت مهم، کمال موفقیت را کسب کنید.
🔹
ضمنا از تلاش شبانه‌روزی محمد باقر ذوالقدر تشکر می‌شود. إن‌شاء‌الله تحت توجهات سرورمان حضرت بقیة‌الله‌الاعظم عجل‌الله تعالی فرجه‌الشریف همواره سربازی مجاهد برای ملت سرافراز ایران باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/679763" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
روایت تجربه‌ای متفاوت از دو مادر؛ از جدایی روح تا بازگشت به زندگی برای فرزند
🔹
00:07:00 حضور ناگهانی بدن‌های انشایی در همه جای اتاق
🔹
00:24:40 ارتباط صمیمی با موجود عجیب بلوری
🔹
00:33:00 بزرگی روح و سختی ورود به جسم
🔹
00:45:40 قدرت چند برابری در وسعت بینایی و شنیداری
🔹
00:50:40 تأکید هدایت‌گر به خوردن سیب بهشتی و امتناع کردن من از آن
🔹
01:03:45 ادامه یافتن صحبت با ۲ هدایت‌گر برزخی بعد از بازگشت به جسم
🔹
01:13:00 رعایت حجاب، نماز، اطاعت از همسر بعد از تجربه
🔹
قسمت بیست‌وششم (نخستین نفس)، فصل پنجم
🔹
#تجربه‌گر
: منیره محمدی/ نفیسه متعبد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/679762" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679760">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y60jqdpp7umfQmu5fD232zUDU_V8rrXZUPlOx0seOPf7P-_CTDUukuQ3URpDEtu88As3UQZsnBAKDuev48L9otMmDbpuXPdgAIFjktXvqbgoypfs38ft8yMCJPhGbOGkxgDr-e1G9ETP_7Uw5rC8ku5iNNu2PkPAKDhTjK8QvoE1EyRcVIdCLSPDMP64HtwA5A3RUv2lJB4jTn-sEYF--_5rZo-_FjSIXxMJVdXGuAa8VgjvJNoyS_t0p8Asn5yPDpmUCx2kI8nLkukCyhEWg_qGhDVmK-ngpmUKCnTALsAcqfNLK0CN0yypT7SI6hBNzZ9-drIBkt9GVNbeJNbJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنجال جراحی زیبایی ۴۰ میلیارد تومانی خواننده زن | چهره او چه تغییری کرد؟ + عکس
🔹
ابرو گوندش، خواننده شناخته‌شده موسیقی ترکیه، بار دیگر به یکی از سوژه‌های داغ رسانه‌های این کشور تبدیل شده است؛ اما این‌بار نه به دلیل انتشار ترانه یا برگزاری کنسرت، بلکه به‌خاطر تغییر محسوس چهره‌اش پس از انجام یک عمل زیبایی.
بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3236501</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/679760" target="_blank">📅 20:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boHXMkW7prRPXZISfBqhwvCEqkYQ0rx8DhdkYm4t8tIYwQdRbHhjVl4ymuYfoAq0bephJf0uMuMxks7g2kei-M3Nnaij3XIXfSEBPdyyN8XhPaB6VGshCZxeycq35SA2ruKF-is5O3004pkI6tVpsM2BvZUh3wHxcRHcvI3ZrJdlZE4ObialqtQ9kcj0Kl6b0DUOID7ErKdqsn8yIg7q27E-55Zgr1c1K2n4Y837SLjRoD8gOyFIZwzYb85VoqttqV1W9ansHKerKT2bpVMkiJ7VBXmvZlQrW933-ngDYYT5xFygbGUhYIGJLAd7Re4H6AIOIsDI0ctPh85JDxzvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسواییِ دشمنانِ ملت ایران با انتشار تصاویر حضور امام سیدمجتبی خامنه‌ای در میان مردم و جلسات با فرماندهان نیروهای مسلح در آینده
🔹
جانشین سازمان بسیج مستضعفین در آیین تکریم و معارفه معاونین نمایندگی ولی فقیه در سازمان بسیج مستضعفین:
🔹
تصاویر و مستنداتی که در آینده از حضور رهبر معزز و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای (حفظه‌الله) در میان مردم و کوچه و خیابان و جلسات با فرماندهان نیروهای مسلح منتشر خواهد شد، بار دیگر موجب رسوایی دشمنان و بدخواهان ملت ایران خواهد شد.
مشروح خبر:
👇
basijnews.ir/00f14B
🔻
کانال خبرگزاری بسیج:
👇
@Basijnewsir</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/679756" target="_blank">📅 20:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713efbba80.mp4?token=QTBIgMRdnLXbkGrXKuf8MjiWJj4uE_Sfw2KwnquvXYJqxXCZ7eCHjVfFM1njeRT2Pn6N2-wqj9eVz0aXUN2iYnQ69MDQGqnnp1lNV4xWY2htOK1i7YJ92bj69K6vw7t8nzw8v2zV0hnGg-f5yc3fiESKFBiBF-N5zNF1RBpBEVqvNHufPE-NbTH96e0Ukbe1wiCZ59g3_mCyc2-B1RksI3KOhDgTYFMubcuFDr44BNqDXMI0oTf_tG_FzIAnB9jPrmNRkV2GuE7BbjqOyXaZDl16uWzmwdfkMAFBtX3ABDg7VMl0QuDjSTLyXnjpPQfcwnO0kW11pwIf5oRQIZejLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713efbba80.mp4?token=QTBIgMRdnLXbkGrXKuf8MjiWJj4uE_Sfw2KwnquvXYJqxXCZ7eCHjVfFM1njeRT2Pn6N2-wqj9eVz0aXUN2iYnQ69MDQGqnnp1lNV4xWY2htOK1i7YJ92bj69K6vw7t8nzw8v2zV0hnGg-f5yc3fiESKFBiBF-N5zNF1RBpBEVqvNHufPE-NbTH96e0Ukbe1wiCZ59g3_mCyc2-B1RksI3KOhDgTYFMubcuFDr44BNqDXMI0oTf_tG_FzIAnB9jPrmNRkV2GuE7BbjqOyXaZDl16uWzmwdfkMAFBtX3ABDg7VMl0QuDjSTLyXnjpPQfcwnO0kW11pwIf5oRQIZejLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مسئولان خبرنگار می‌شوند
🔹
دیروز به مناسبت روز خبرنگار این دفعه مسئولان از سلامی، خبرنگار صداوسیما چندتا سوال پرسیدن و باهاش مصاحبه کردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/679754" target="_blank">📅 20:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679751">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVO-gxL-4dFxegdJWkIdrkKjy27J2v11YFK4PFS2Y6ihyK8_qFdHZ1mQYBPCgYbJpW7po2rM21awPJW_8Pgg8MQivOOPaqwFIHk7lf9lY1o3AG0P-v36s7Oetv7NkfNoE6JqyPnBDhKaZta3Ge31tShswduj4u5lkaY4-yZQnZiz2_5QkaYifhqbFiYOjrnyiI8sB6P62IxyUQ5Z32a3RKDtLtUfC00DPQhip_WqOAw0CjP3RQxmS5cOEyGZ3rzEaGfGPD_dLIFC3LhBPeipCrTXU8NPhEZCc8irJkGq7kPuPJMBYbEptplDofKyGURoVB7XeXRzWYz-qyb1rPM-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/679751" target="_blank">📅 20:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679749">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaDGA9AnnVxjbHOHKU3yFUiKBvBopWpZSB3kEJ0yeO7jRAnv2uUVnrfZKkVb_sL6255meqjr6vkyo1Eg51Kj4ATzZ_NXzlW1oXoIkCSWt1Z46-ByZd7hupOqBD1uYTwWJhjwXx3ZwtppeynhAc_IE6yS1_ARzbLljxIuZN11DfJagfwPH_tw82sFgyB_qLHZCppGNkBlXJ_q4TzkediGTk0gRY8R6KD6Br5DnLKFPc_AxLxZkKoZUtKH14whYb45cDlbcPQWfoqMmNGTh2QOuK1rjt89CKCb0kzw4cG6rtS2GFRIRSIFL768pcbhQsYQI-eGlYVSJDj-G1czqcQJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
مام اسپری سورملینا
💥
✅
۱۰۰٪ حذف بوی بد عرق
✅
بدون حساسیت، بدون لک
✅
مناسب برای خانم‌ها و آقایان
✅
ماندگاری بالا با یک‌بار استفاده بعد از حمام
🔵
🟡
بسته ۲ عددی با رایحه اسپرت و دلپذیر
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=foritel
https://yeklinks.ir/mamtele?utm_source=foritel
پرداخت درب منزل +ارسال رایگان</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/679749" target="_blank">📅 20:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679746">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtKLZB5nVWPewoShOxy4FNdhLvDDwugZDWhWj76SscsThvJQ8nL3d4cEpZtm1XgXGzW5ZCkvJWauwtHTasZQ2GJhm6LL5f6RD6RUXJbQa5uN7m0GjkGbP1bA0iKfwx6xOB67IJZMKVwhdy_knMfx5soCFDpvmTTsjkVaBupLgDbBypekyoLYcxEzgYaZyUP97sPwyQuMV0c_jsIydkHsjf6mDLSOpco_Zma60JQqjcRVnuhR6Oan_nYKBohgNiT7yOz7pLhLqXVk4A739SAe5o1mZBhqrWRCgRUGwag2KmBMVh-282R2G416EnLMmQqI2tvuxOh39q-tBrmr0s0sLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل تعاونی لنجداران: ممنوعیت واردات لوازم خانگی، درآمد ملوانان و شناورها را کاهش داده است
مجید کردوانی، مدیرعامل تعاونی لنجداران بوشهر:
🔹
از زمانی که ورود لوازم خانگی باتوجه به بخشنامه‌های اخیر ممنوع شد، شناورها و لنج‌های سنتی دیگر امکان واردات بسیاری از کالاهای مورد نیاز را ندارند.
🔹
با کاهش حجم فعالیت لنج‌ها، درآمد ملوانان و صاحبان شناورها کاهش یافته و مشکلات معیشتی برای آن‌ها ایجاد شده است.
🔹
مسئولان باید فعالیت‌های ته‌لنجی و ملوانی را گسترده‌تر و آزادتر کنند تا امکان ورود کالاهای بیشتری به بازار فراهم شود.
🔹
افزایش تردد شناورها به معنای ایجاد فرصت‌های شغلی و درآمد برای ملوانان، مالکان شناورها، صاحبان کالا و سایر شهروندانی است که به‌صورت مستقیم یا غیرمستقیم در این چرخه فعالیت می‌کنند.
🔹
کاهش هزینه‌ها و تشریفات گمرکی می‌تواند موجب شود کالا راحت‌تر و سریع‌تر به دست مردم برسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679746" target="_blank">📅 19:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679745">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d719b401.mp4?token=N88AZxTY0ZuXRzd3NlWYHw9H0TQ5K0kftGhpPxJEHMIhdOA5-iBqB_-Kn_1KzP_FrWcinXvdM8IkjbzlYC8BW0IyUIsL4DHsuVFyA2qK52gLoyyKCFvtuNuh9iW4HGaaWaHy1B7JYfbgFrUU4D5p4krNfYouLiqU1MOpc05Jv4ROVbX_kGRySbcaoQUcFwHGHgg9Z69mu2Cuh42zABlbpS5JYSS2hgeT2OCxn_uZX2AB1zmDrBX2oXPcWh5XH_Hhtw33dq5UsINl35RZQxgHvtFJDMUcHy9EYWqRTANdjQEXIiGIPqJQifLy1lE0s6_6HQjOBqReZDQ3DCYxd_dN6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d719b401.mp4?token=N88AZxTY0ZuXRzd3NlWYHw9H0TQ5K0kftGhpPxJEHMIhdOA5-iBqB_-Kn_1KzP_FrWcinXvdM8IkjbzlYC8BW0IyUIsL4DHsuVFyA2qK52gLoyyKCFvtuNuh9iW4HGaaWaHy1B7JYfbgFrUU4D5p4krNfYouLiqU1MOpc05Jv4ROVbX_kGRySbcaoQUcFwHGHgg9Z69mu2Cuh42zABlbpS5JYSS2hgeT2OCxn_uZX2AB1zmDrBX2oXPcWh5XH_Hhtw33dq5UsINl35RZQxgHvtFJDMUcHy9EYWqRTANdjQEXIiGIPqJQifLy1lE0s6_6HQjOBqReZDQ3DCYxd_dN6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری آمریکایی به یک اسرائیلی: دیگر نمی‌شود از شما دفاع کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/679745" target="_blank">📅 19:22 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
