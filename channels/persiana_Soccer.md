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
<img src="https://cdn4.telesco.pe/file/IDlIcgVzMC4pt-LUkL68bFxexMQ55XE5dU7OKE9PK8O5hOlBj3zUxsmfyp7hUjR_IvosrcnS3bgIo0bJgHepZqZON23PGvpHckxqKM2XqndUBST1OZuvrSNplbttYq_A2a9h4wge3yb5GS5YQr9608ZqGT34Petkh2D9MooMv5kvqg52t-wCvP1M7-RKVoFJ_LZ9LGYEQEV6Shse8m1_CeQsVuCyjbbgyHx6Yu-hgTBdXtx0Ah_FSf9cW_7Ca9QwljBjUNJpbZK4t49-PfF_PaVn6jirZs8W5Ik9xQ7oIMp2bhk8NGsaI2CqwjH0O-tHlFszLgocRnZDdpMuR7pIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 628K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 21:39:20</div>
<hr>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWGgN0qtBBCTMP_re3UDCOz8IgBCMni7cgENy8NjJmaZRx2YzWfvdGL2ElgugbNdXJ7TBFE9RwtxWk4VLKaXK42-SejSVIYcPs0Y2NRH1rm799-KACoJfQoAqe9TG_6bcWBeB_Xm-MExwJh0WNv2VowYgZNdwxEyAsRm2H-OBwZkdaUkoZ5MZMHK8bWcxDTa7OBxsZ1uMhgXJv4WpeW_1CgGNLM3C4ze4P2iShQlNEHpJVfKTr8CpKD3yNwkTJ_bx7Q749Yf4Uhj4Y0mq-pyyacQ5_Jy4mlpolISTnQmhwWwQtHkDY1FUF7iHw-UWn5-dZzNPwbv9N7fj4eF0EXXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q42LjlUXyZKsYxEcyOkQ4OAsqVN1BZXGncGQNwkfjawuPGyr8C3hE_2zQQ3O5V0gI3MaND3-dPr2ir2Ag_X9v_GA9g9kabdr3qktNI44Q_O19vYezQIq9wi57U_aZSRlcD8V2gYsxpjJystLiUt575-ASyMbHnbAg43-QZSPT1nHJ4B7ywMPzdqQyzj41MWN1s3psmuwOMHoF1Bk3GQtBoEXKorHYUnJyG81cEYu3SPREVDYYiEcKTG2q6tSZPaUv9FQQHbdKKxnP1TDao92Yi_2fSVBKjmctvmWziAJ3-zNzXdBnfpng-wg8bczxYHLp7kk9CRUI6EpqBT8xIguQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfAbLigdGpwzS_SYmd_1vgERTjy0PmcML2IPdP_qvpouPooVLwk16OtQ29vLshI7Ci-ubf5gRc0g-kxeDvG4JVIGBsCz_F3mBd630hgHDNT3u_ymPD7iGfIrLFnFiikU6Nh67mm2AqVOEuPH8UHdI-fyIluAcGBOym0KmvZ26_U-JFXe0IojGMIsnaGpk8_M4g-SOHxXPzog78uhSA8KzrenlMS-wvf0NwAaknVo6pbiiN5nzKD3VDGtuYhV05LNVyz24K9ar9PagXygk7FyNAZCMz65gMgv0s6yNwEZess_unswvs6VSqmsv23aKnji96rHmlCmGss-X2slisS73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMQyx7PA-jBPQvZFi3GpzPsRZUeE2yT817Y65ilecfajIxOcqqEhZJxS7iiZfm5xshl-3HXG9boPpHW9Nl1ytXCgrZZ-_qW1pEozmfZff8nbLa9kvVuKdqmSFVqaS_J2f5MYLakmrM7l1Rar-w_JWX_xTCTg7j-u7P0jcaCmjJ2thf_Yn2R7HbA6Rk6Pmfi5BUHPHrvGXcKj-JrzVu4S1qGZs5b6GgtSZvI20O6niV0-Qj5WOawq8e3iKkJnArAB11rxuzHWvuEF4u72HSoY6m5LOztnhi49zKfZ_SB2vIMhmyi0sKTzNB09TQn1ig9nkLC5cDI97aZbbWRLmbpOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3TS7ZhautjT2ckPJwIiaQU2fsKPAfhod6KrA4CKqgNwVkwuiCi39UBREVRgKMxJ5fHPOsGypjqvtjLOdhYODbppXu2KQUR9T-oNVSl-OlcalTKoh7lMOueDVa0nVV45IPYlTI6hkUNr2Wg4ww7IhLhXyiGR386JDtjG83CbyzTiavImulp4gPno2vn_6YTk7YvyKqa7UkerG4jEsjNinX0r9XiEF0HC5p9Eh1BmXqRLXnoZZ_oVlgY5N8NHuPs_gZasAVY6vwnSRckL_2G8697oIIlrk1Nr58VOVcN9IqZwqnu-KI355ObxgwvzzuP3Cs2kJL-pdigVjktOYgc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWWYupexukNNBV-_I7mZoohWSz0Vl7sUyAQ190tOTdnuaLgNAF-uNpGkKsT6n_24lWbWdVTKBnVEePd7YkQHtszi6ysyPQTa_ce7KkILcxzeHAKgJczeSJX8B0P4oLys4oc772Tk7n-2KN5DNZBZcj5ax25f-37_5ExI0Qct8mYLDoEC3nBukSeHw0YrxEiUUa871cyvYjgrUTQ0fjRDjW1J_VmC9s59saWFJr_y60VAfp4isUBjh5LTacKcJkJLwW0DWd0WfBsghjD7rlx8DRAl2lqCyYLtzLlA-Igo37L8iRRbfVjsJhG6DEj-gO3wT_jwmg6w5kmWNItL6kopcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtnEIbR83MrbJpjsDoxH6kHY5mweSj7Hv3dPEi0V85QKnYS-6ZQExnRZD3kQAYaUEfsoLihvka9UFpSLUNNQrIquhVtI7isS4kU8xK4SpZIx5db0iur16bgSB5UOKNO340dmyjZwChgkVieTeF1vDJGnqygGWL1T3Hol1N-MMkjbWK0gkEMJTrX1YocReize_-62EcAvfDfWmp5i5D4d31eFyIQXQy8fgtO8C3mIxpHa6nBeXtyoratOxNjhSRA5hJWzF1yO0n1iP6RgiDbyJla552XjG3UVk8hq5u-nyl3wOETM4tkes7lJjgs2Jqd0rN1Un6RwCZDdxOueq2Mclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qViPoyhAKcyGDIGj8HrUC-WKhfRq6ZFY4OJ5voLu29LRw_kv8_k6bG4ucQoLC4q6pKFReMvqwek0KWXeNPF9STGF-1rtOpQ7ET7IgEm8MTnJwj2aPqvp-0DA-PRJwkS_2cFt90Utq7BvE1aEm_5vN-e6FgwRPmI-1UXZqmvc0o7MZiVM2EnNNLA44iVR1qo2VceoHbe2XRy8NXE-P0y0lsusAR_hmqpu5Rn5u0zndELr6ScbLF6OfhQ5SHA7aLRVtzI7Bhv8AZ93n8_yzCPbp0HQkmpWoszV6msQRr9RJy9bo8YMN7APvngZ1A7YZRJAkGhSLoaIs_VgujQWqaW43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub71iKPswRgLY_pqQAnpWF1mflkhQfAMMTwaxcRGo2Ng5c5OUfApefUoJ8Kj5ymojBSskX9ufMRSGhTNRs4zM2XGCCoaIxiuS26aC1BgDYt7d4SSMLHcNMT72J_sye3JPROBZ9_8gU_5MpPoiL-5gHu5foc_WDiE56gaBw_6xNDpHZobpluluHvCLHtMFuYIKG_Kg1zdMXMNTfWarTxP-h9dH8bjl-ePOVU3zv6Hzrml_nunFTbTLcjNBs1ZQwnT_aXUVzyAhGSpDh0gn9TcVkDw_SKlPZoiRada1EkVwLKkDdXaiSTpOeKNktQgr7XA3VJplk79uvllVWnKCI2AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntd67xHqISAR5W5dG0dF_bUYZBjbSpxtrsw6x2qduNwK2hgzj0Tqv4M7euBEHTRXQaV-rG6a99RjIHAQylbiani7fIGSqHgXI8ppN_EoaX4xmIrq_fluY9Sz-MH7B7_IewnkUP2FHIkB7URKePcMkkTiY54yvSOu8ZaKNlAID5kR0Vcsf_YPfWL-_-p85N46yjDW5NpdqMqCu-HFZyVc7t7w8XflhItvEe_XKUgobp6P5HewTvtZ7PyHZBR_OGk25ZmX7UjcUO7xXWa8qTY9Go4HoMMofecTWpGuzoPcReVwNiGCXzaFAL875fHALPY4KNCvoFiRMR2sgZ00Qgkmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTDN_x3QE3uP_JvF5TFkLLB_EDGieavdvxyAiiUNzkwZRYWXRHGjRpPOXXt_qLs8_IQ3zgky-brhVtANdzf-b8L7pPcB1oZGHxto3-QpDTlmIw5pSHrP69e7mVasqT1zi_ohujOJKubVXNvvNxvEgLgsYnb_MIzA8HEwxMZ-_prg4Ma2xxJR2Yhhn8-MEvXaISn1ljunE8Plg7RHv1rsLkzg6fK7ylENKqcLIyXx_HPAVzEq9pQcamPPv0suS1Qiwy53mjCkZbO_eNxPdxBOL6TMXcEH5v_W9rSYtfAt6trkCcNwI0Vtn8J4Ulyum160n7RhzKHS2JkpauHF5iwMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3q5es5ZJXPzY9caEIVD3wd1NdShJci-46wmrakSzImGF2hLeVYNM7CuohQdGg8ZRr013ukL6yDFJvkFgrQOVoLRz6wp-ba5lGo5xpbIjJ6FeukO7GOCLw5sQcCYwiyxby2SY-y8biayJMUypirmSbzWUdFGoFhPvxbCvz80fsKa2icAh9wgQSDz5yARiefEXL_p2OEq2o6dHP6x3Ebrx5CxMCLO4nev4HIxI4q_ypw5OpGPpkPJJdqT9S3TAO0mnzC79yWxn7N--17Y_rZYc12V2wQSjhXMat_Fzn5iPYxQM7OlJw_OkJXfEVYFk5ecEuoeeHXwzl2U9-nwetPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/retUssdp_gfhy1ihfY55xqHPDRHRLzKuragYTz6un0tFHl38XQYOQq30ZqpDPzrqw19b79sv67Q9VgUn92AopM_3qfoRAzJDgMgGzeRUxtfk7bqhUPwVLHWmPMOqyZxmQFnGBNVHV27DdjbOCZwVyJ9F4FJUTyvL9rth2xNl2tk_cZ_mXxyP85fCPHPPlcvds4zX796obyFqZPaeosf8U5DPJGw-62eKV5thTGHRLb-XRmdD8RSGluQE3inAbi4BJ_oNHqIM-l2rEslYLyQfU5xHJ3a76GfaoAGLjKApcX4CuB8mOzqjujyJoU05wovyWRaFqkz_3MJ5h1ZKkbzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d39tCvmdr27z7WLjfXiQOkJGi8rrSlvAu-JmpU_in267MKkDSvnH9stfeOJN3g0ekJJrA5FSBzoOnZuP88U8Z5VG70IkUIvA-MCVxa0R7PTW630ta57ldh1g1mJRS7NkCyamAQP5VddPerTDPq375TVhZA94-cbYso1DqGQMRm2NVV8V8XPoLM5K-oJWWE8YpM4uT4eu_DGSgzNQdt72QIDVDIXr32nmTSGx-YudUDAWvhTakMko9tRnCx5enbmwcsBOXwpxJc8kIMME_AGckdsgKq5OVJJcs3scUiMjQyuZte4Nkecr69vWV68WrYvzMTlTwjYjB0hH3shCqzEnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTRdXCs3BXfRJb1LPdWxP0KEliF41D-w_dOG95CjOIIymS-NgEpoOesPNa7PgN5PZaZgQ92pPv_VVRb5X_BXI7BK-KjPVQQsoFkkBFCHh-MJmS1GxUcdcQ6vPmr0-i5BvwAbCg1Aivn9sFVOJ83sf_nj2nLrQ6vrFI0v1IxD_oRqzKeSOC9Qr9c84PB4V5HF99wiPlJxYcG7QI3ewYJcUM7rRpHztU1CJN4HjAVyk46-xflrmxDVDFUxuHiFHEGY7bKYjsBiWZC5tnQ-LnIZ39jcEg4-0azeBZw3rMreWWA0uk1iVu3qpiMsfXXOJddrZwsBdgm_fK6yaXuLRVvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJvdcyCSPugtiPgFv6dr4N-G3hcs7QcHiyeoYlY5edVAcfvCI41c-G5jDLnaemM7fMJVHZ5iBBYl3iZV643wZ0i2O-4Epa3Vmb1d6HB69S5_l99O0810ZuyvSU2MXuI3DSC97dDFLL8oKxZp8mGgu9BED8iO-y3ZznuDau8sSypIdTdq-fRAclbzf1WNV55uueEwiJZmLnllJwPAXtGdO2enwwo0CYfm1ER6p3iF-pnrI26UGN_8JfeaTM0E94KrSPSjVQLR92eLPiVr2tnNKQ0YW2jYv1TnCbTEN-m8b9FgjXcHKV0wcDA-nwsH7SLrAPNc-oi6XAL3VAAwZYvA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgc-Z9q_aOBXjeeBHJzmOKKhsLkP0WEB1VeDH7C_pWmOXZQwfjm-r9BPAcq6so5MrW7Aycbu_9pGvcNs82CfNFacUEIm2f9pQkopzTYydY_h7vFev9gyRdhyPtk070JCgdhX1z57vwvuMVluTE3tRno_mpKlkQX8ctn6PUYH2tja1zxgDj3ahbQy3EUsQ2ZYkoIR5nxCY3V85DyggXzJXAGIPofxTEzIgskfSUAsJwYjvyAMIolR4-GwmSV8LuYsM2WQwNePsPgxu_4LZPaDTtpwXOyvswB1GUthSKVmjbCMtchUDh7lkSh8Y05VaWmPBwoEdm5sOHZM98DuVFRBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKA5Nx577lVIQpa1BqEE68BCWiSYC6cbIs6lUA0Y4jM05x2hDAr3VIHpvFFY5W-AXc2CBi3l-bsCYrPKA04F8uc_8zkxwRtwfjszX4p3fYnQl67aslEmyUet1_R0zl0C_GMbB6CfugYkEcK0-UXP3WDLaTn64QVA74OtusYwp5ez0OrJ0mDIY325GCzQXl6aYnsRUt9NNCaawVo0_3h59Kb9i7iZ2s7-c68TGPwFjNym7eRHmhonMk5dUPx6gPHKwhVYUT5WyWo2fsaEfxAARY4OEUq5dfPkx2zqhrLRxyziuIXM2qZeqqAIg7wbu8gOcTpkoAJZZJnnTHCwgGisUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27088" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFGPBChoz1tQC4CJ5fGzY0Ax0FnCLMU9zr2OAZA1rM6vjNzc3H1YZvhlrw_ncEFANfnoEYL5R_yuvFak66ekPrU30GkAZqh5XtL8z58-8s63k50-R6JSNZzZeZF5WJp1CDWve55BV6pln5daMO3-C5VtvdJX32jo5fhCaQkB2NAKXBUwYIenhHCfydsNOXJjAFcztZnL1mGzEB-nknqLrrGf-VIOW8ViSySSQJ2SESmfrDGfrT2A8PSaAAWhDNrDZXDhinRp65dFbD7ZJ3gOscIMp8FfMsJeymOa0300cyXUOQvZsCpmuqOdO8Oe-ab1xPYSlY1Hc9rXk8K6xdR70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7kInltQnZitUpPE3rBlOE0CHQQ2mL-DguptyD7ePWVRXIj2TN6fUc8wZZpIDHJaHcuTggICeAcCq5WswGHXghokJpfr4yEBm-mb43osMRTeGpMDicj1G55W_zJpr_vm4xS2Jemx---8ENobTJhh2saxCOd8yPGYUey0f3qd_ByYKD0AVypujkjmUhVdXcPbUteqTLtEoEla3rQy3iZWd403XzB6zFWDw1hWkPDo5G_EcodHyEfhlVvHfc-IcrDid8TnAR1zKLPKhybno0X3M5H21vzjBaaTO6k5Gx6m7hz8iAOLANtfRW7cb4SwApyh7H7l6WvkPTD_YtDtAZqQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz_h5oWkQoJei4d8EFySMhfiRRYiNhFfbtwVoKCLOFu1cETFLQlWynW1MX5SFL1RuoPqNHx4nN5UTrV3tsR2Yd-Lt0VHNjRhu-59LFdQmty8FizZPsVT3ruGDCyAFFxLTmk_dRMGUP1sSLr90fpHxgWB5jRZy5yL8v1AvA2lHd0YSlEuxJbYGi_JbMSvjj_UdU1YuJHLp3cbWVZW7xS9t3J2MH0yH8i3fYu6s-Ga3TKMCcHM9FQp9zOWmhnqHv_TDdaOGo4VXQ09ot_NeUWBBQi8BBi9zgvcwBxDIVWtKaW_Jb0VWGVneip5r5mxlB9RSabgT2L4fhBncnLEhCtxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjerXJSK2j6_mZJaTJICVMs4NWIWT2WeuHl2aP5Uy4oJ22Kq-0Xr555cjbKhZ7S1ejl01WvpOCAWefFxNwTS4JuP3cv0u-I39i8g8mhZwGrw4REC5cu-SkWzmBZHu3rRE6Bi7FFwHzCyBPCJ9GxndZyr6jG5Wuk-ZQU6uhezjpcuxz9TRKhxNuNT6y5ZlOy0FV1HMSUai7eWss6vNPtKpEJaOZJzUQNXBvUKP5zj0AQ4l5aaY-YBHtSkLjw5rluN6cjQH43ToWTZp5kSJ_gUGUOvtevQBXy1mg5v4uz0fFqUMvUTBZVWIAuzxYfiWVoGgmMeQf0wDjb_ryJ5KdURNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCRmZe_LKHdUMGPvHHGqUzauQukFYdY49Nkv043SzQg4LWtQnAHi7pHG_2wN-0ubHLAX5hAImZTOO1-yd0_yUxJNU-FdHQMzbHpEkG6Ha4YvtFmLDl7s2W5UMy4_ATB97nFZznpymnshPUljEymbFDXOgkFXoppaxJkUScqGysItSFSyDWPW8USI-Su6Td9IT-KfovvpMVKTPu4KvHYo3h9iUNXQcQLVYhzLuYgWDW-FnVRixrpaEfFIQVBOJTveMKIuZ11xJqB1brAMhsHEnowrPfT-QkScdJqnBJigMiBI2Bedp3Uej8z_Rc3TpUUilTbGUhaJZbu4k0dY9ekIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0hub9yQ0YJ1yJvtR6-Z9KiAza10A6iNcbxDW0XcADwNbgwe3YAb5eZncnI1ZPiSDWP8w-hUtjY6AZ_I4uyNAYqcGg5QwHjVxeBVCdYNbqkqO9npGnl_O3OlVW3ZpoL8iuYkEwWFk2VzGO7XmaqQ9cyZYnALSsR9cxo-GM5HCXwY2MCyJtdzH30ilNhnA9yWtHGATT-rUddcdrvf5P6FkxDTmhgFYNArePav7PUaRSRpWY1S9i4KhI5TAL3V5E1rxYX2NGw4-GqSENnAk-U0G2TZWZW250sP9t8C0wJlTJsZgv1WvbmHmbsSCEiTy1uiKpx2Wa3tCBT-iH3EQJmXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXpgzN3Y3cG06A4c0q8AR0REf301MDFh1YJeymoMv9dqTgin7wtA4g542-Vqlzx5v2r2JkxVlzYC5KnbH8VVT6wnrFQxgsC6u63fj4DD6XBppj30OFdNcofdAJbCCJEu6TLxiZI81M-S2AmVasbw-jJW5gIk_vmZzYqJfkyki76OlhyiDxj79zptKqGqbW7tuAjUuQxucQQtnjcHlqWHQ4KdgAhwAfhFvHvlfz7KLroxpaOq7tjU2_UHvXEfkTnzV0MHqa07KGUzrUWmUv27B1EVGcwqpt5s9SuXyVTPuer63_kbWxPqJX5_sLeVIH3hH1R-JC3mxZPOHDUYG_rd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjgwdgTc6hqhBdTjGFqaNREo0k5uwLcw430sO2yoob3z-dz6A_qh8175IiorAqCS0ZLFJSGZvP7NQefYsi4BQpWYZ4-LT5Xi2j4UhR_-oBj-SSsocnQhbZPDMcN14lQSYutjx6wlKr_A0P0_8PrxACLk5RmT88MBiBI2ZtRBDYyPWCjLKThL5Yy6UACoDQ20LnSrjgLgs3U0iz7UdVZd6CCaIoYLmgdlyYhdlhvOYMDllKDKeDdX88nX6N9GjYmwJnJfe05sMcpLyuG9NAw6Lnse08BL9DUjo93l52dP-MV11Kuiu7es-tkx_hxvkrBKYrRR5TIzuLwyapBoHPUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI6Na56tW-jOn7jl1Z_heFEhwrRJU4-bC_GcLje5pYVEgv4cEqNXFxLw5QAFhba2h0ur7cC9MtbPFp5_z35hWn1R1ZujglHqowUfwHW9CMeW5hJzCs0n-iG8DrhT8hrZw8UrG94Hd007JZUnnrgR8zy84SEYTItTm7G-xZRaghzPKqkddcG1f8N8G9t7B7Nzy3cdokQaCxwz0DO4fUjvj1y3ZQr1D9yNNu1OMeTrZd5vLPKSED25mtiDuV2ruHwBHENbtt7IvloavUD53_OxkduoHUiANueIPPCVlh_j5FNmJZZh1M3pdqnbKiwWOCdYxiBoltLzyy_xgRUw6koY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mREO0kSN2ovoaxJqC4YZvoj_nJvLgGfKs6V_TrrVLXjOlaUMKh0rDhqfEwGU2C6gh6wQy00n7HpX7p05WYlDb6zpHEC5OXpksa6etXpYkATd68uVwhdMtMdPWxHBchWleIWB8CZ-OLhLNfeXAo1sC1QKU4YroB7lOmPbczZ6Jk9YvpruH3cNQsKBLeR6aHX5jlWctPIhwUsaa93BYjN2XsBvqEit94d3LlrjmUVMpYQrUvd1sBIqLV9_iXod8n5-6yAC5JfxDs2Zk6ktK4m77-Is432oPh_qQA4kR1R2xyk8yNWLQsvaAPzhwtSPQTDS_vtqYLtpzt1NYJ3pc-jQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPqpoTI_5z63JolSUxtZwW_BCuvOIGKRo-p8jSJu0TfQyjoNc6BXV-DS24qWqf-DvZeXrmVh8jJUJseVp9_Il0VqSoov2M71kp7DzxMPZyoVha7s3_bXPz6-tz-nPWhqZUH2OqKvfH_Fk3q9SJHwS73m8vsxnOSIWUjBbmhXcwxt7tYv7JynAtM95wnjisFp4CY15SCENkBWklnylJZkv18bkGeNb1XR7v8U481dWWCBf_3WXVcEl3rvK6WPeXba3pKxHWeLo19jRvmDld7-JLQJgeGOuA0EMDZGHL2rphWjSG8DFA0F6r6uLxPHaWpcWh-mHcyC3eBmbH4Y5SGBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5o5PC13_h52EWgeMfxlJ3Hks_fs6_pmOmtLYEgf6KIrTdTAgy13wcV5rMlFfVWu9F-utGrG29aL4-ORnwpDA-iymUkvMiQRqGjrD1y7qBa36sPUThlLJkI72l7Q8zEJJhRlln2CqeOT7lXpxdrw6zW1jbEzU4DRFD3CQ8dcj39C34jQkJmsoiWPKN6CjroBgSDdbU37s25s29P6KthTiT1iintr1Y8YyboKEcjKjxIJHI00_g0sq_wwqdyVZzCAOhh82ZfQHAy9c1WT7Q399cQADiWoQy-CtmyYTGgUixqAuyWjbUp8GEkJYMvi3QAotwpWcmDgKrhF4eIw0FhCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szZoBX0M02-UboudNUPwXCoeWcQPiAwZGXPnActfrd026Z2G54lS2qGDL7-BRqr0IOv0Mx9q4jJasApIbY54cLBvRqFwtGCI0P_H67XJkkWiG026qJGJaDvR2IWZjA7euDNx5_xrHpbOxuXC7uDPwu5gXPFPzH0dCmvQuPAyaQqydLbHG2E1M6iwc8WwLmbamoNG56Whe6HrI1nqhxiQbev-pmyl2CeCAXgZXtz5ZORdd0Orr40E8z6PJp553kfzL_dsrCQCODC1gycxbThrjncmSJgOZpFrKzsa9Mceq6iZc0keqmG5XJ7zili7xSZ4K9cr18nIQXjj_FVu9CY0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDj6r0CCzr0rPJSYaKg9OmN7kY1ej5WdOUpVVRAgT37DJRKVSgiXtRN0xqFmQgrTKrNa7pKMrgt3erLSiTpO_KHaq5t80_KAkvXYT1axU1rQieqMqFROBKjWGBR9T1Hg2QzWVkj-5izPFveUUQBxILU1I9Gfy5OdXkYUNfTn8lTEXOrde3Uczice9ODHPappsUHIcGG5CMMv-RnjD9ZKf2pV-6t2WsDFq_xGRvG_kcZzDfkEgtFLUbQzyrVndOhCNkqhwhGMKgEE9YWXC2hQnuvMixA_agUDOn5Gy0JUq9jrLOcRnCHpfjGJ5p_0d9IRcYe_SbFd910KTKjW2FsouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US5UXCbdPa7G-fiYPThNytNUB4DfGAM1Y9Gz5EwBNT9leeuIK3iJNeLWf4aP15IqYPexrjaeobyffA87h3-VdckY3dh-A_MrlaJ6T0n4vcZiBmVojnSPWN6v5-2QGPdRTtlh62SU4OPh8QV7XKC8nc59xcnMyR6FzdJGwfhtrKwL_GO95Kt_wLFe3WdJ3X4UPwa7SsOXYjWBkqdYJReLOSD0YiG8mT8YEfdd5tjZrn1f8wtAYFK3TfAMMD1kPiR33K0xDJMuXEw3DhLUQq-Ep2xx16SFge2fOLKax7DGE4XHAPGLVxIcO4YD0p5vI13Z2Q-3e0ZkEYAAp-a5UAgQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVgLSvLdTKASGa1vSLRPCtsrMAvpKLid98Q_PysbnOaUQIXsy6G7R7Tc8-0kqIN_LwIXwSSxSMEU146KzZBDhlkkQ6SrP9Yl2HqrZ_sUkT6XJqqjdG7Dhb0VWRrldWTJMK3IlfguS1L68Q1AOAjK6YiNnawgEeioaw10mvrVhecJDKzpNXo7n0FBjbTaMYGktKX7a5fXBAcnZoQiOICXzWdwDQzLchwF62JAiySRDtnocSJLqW2nBufrxbk_65lZMr7B5hdbFk5ouSCDIgZ_m9k3p4j4GocYT5wZ5CiJIuZMCB2URtBuX8T55i3YB5cQBf_e1BftPR0h_piyvwao5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=jQpVibWluB5qTUBZnqN2NQi64c2KTKmGrxKQ8BGIzB5TQoxVp5nSzWOA9F0yWJzIMMIajyPJaZf8pRQuAFHXt16qnTyKeeJysADFL3KfIBlelP9vPcfQqq2wYsAxiMa-qp8V8fFlqxTTZqmVIAwldyU9mVVr1xl1BPn9Ak-nHA1_LYe8yhzhvPDG17lHhHlHM6gC1YW70-bNfkVKJ3I6pflUmZqmG6Yk5RuHA2iqdK-0orTlV0Arl4YG_WRlZkqOc8NKX_e1qHHgnGs4X6d1ggWxAriZ7k7cFLxqq85MADaIuDHaFwxJ1xBb21dI6hWY8Xmph90aZPbpljEoL5pulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=jQpVibWluB5qTUBZnqN2NQi64c2KTKmGrxKQ8BGIzB5TQoxVp5nSzWOA9F0yWJzIMMIajyPJaZf8pRQuAFHXt16qnTyKeeJysADFL3KfIBlelP9vPcfQqq2wYsAxiMa-qp8V8fFlqxTTZqmVIAwldyU9mVVr1xl1BPn9Ak-nHA1_LYe8yhzhvPDG17lHhHlHM6gC1YW70-bNfkVKJ3I6pflUmZqmG6Yk5RuHA2iqdK-0orTlV0Arl4YG_WRlZkqOc8NKX_e1qHHgnGs4X6d1ggWxAriZ7k7cFLxqq85MADaIuDHaFwxJ1xBb21dI6hWY8Xmph90aZPbpljEoL5pulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cObgWUvlnbK-WWkoUBk8SSOSJ_T7cKetvdyuu68x-IvCMEppIae69TJma_dC3fzrQNwRr7a2HVR9dC2kujw9AGZubQSV4hafvnwgIOqS_cvfNDGugAc2-DyX4SL16uvA_3Rl1PTOTkjZ32HcQoRzsP_GSAP2tD-chc6gbWVcguEh7KIbksDc4_Sl2qzQzpy6iUWakSh9mVKmntw53Vwj-FtUdoIHrlYgvh7W8DlyZjQuS-osK3RFnQV7X8h0mJpACy6l_bTCtNgPCdCK44sNHV_eCMeC6Y2WkdiplJlOsGRHG8TFBVhUUdO-RKHR7wAzBmxJ9ezAcaH6oMxxPL_AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe-rrW1N6MgiZ-pck2a_zr_c5uidxc6BAUczC5302JQ07xA_T6Cl0PJ1Ymc0kW6bGMGUWgpX64Mn59wUJLdcbHin1MmBBH-YETflvlF2YoGu5boJiUA2hj9JJxOfFFnhxYNCu0MknuqwWqc93y0wH5BsTd3Bed-DgHRlyetJ-LnlHscPIuhFewPzdP3xcTrbaTs8Tq8YGhnCTgUbsnqeZF0VuIJn6N-xDEPhFdzuAwIyIbqzOrRuO8s7MsSc9Il-c7ZtjWimnOjPlbZHaQ-1snnAzO23sLeuqp-LHxOSiXih7nJsYEVsv2E5R5kbogbHTcOZ40pZeDbF6krXAUKWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX06oocH_gvN9QhWE3BKpQ6VmGJE7Q5U2M-DqcGojRjoT3grHxnkmNNuecuWDNQRWgeOznaFaO0fuGS_lbIjMTEY3YpeNyh80ZhwSMrQtRMmOTWxHVbM0buQTLQf_63AY8T_7ip94YBmujiHmBnPmc18dqyTPR8MBxjeIIhq-gz6OfDibtmS-QRAUzpTvigZJ7BsWo_yJeelzZDYah7o7XJl1YkD8JtFZ1hwnt6N4_pdmtXbfhOjeqZe8mVuvENaMintUS901vM99OTW4wc3HpYB9Zeqipf__Qpv89n1BgLxP68o7cObXlIthp9RmNfJ_8JAyMB515jn569ByNZWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocvpPDV8jg2sK5_WoYVhfM-3vyGPZJRBbXHf_E6k7UvmOdWK6mixdOwG_fz_VHFnca-02RMJx6X-WqYvdzWL77bpFI3PvfpT883vRtQkKXf7upXV7l70g_oxOVA7HSzKpvLH7nkkVnUUq90jmFY9p_kSx7Iqax2kaGExVQM8HRYdlJNqUDctUwBJhZcrKWBmqbhawq6KNEzXrBj1evd-LVIbQcEXKtrJQYhHy4nxJMwIRmcUosRvhtKrZFj7vRhT_IR2VhJ-qHgJ6n8w4ltyYwT1Cd4YoGfv2Wg9W3_oBh_rEnA1V1unHRbFECJi-ZVDycog42Jobqn81MKRvOP4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=l2k84PC5xcOrmfezRwg-ZH-rrqRp3M8TKamRjPNi0OV5-j2EDudnZ66rLNLxycfGbGS3d8UgfhidQjFLSsjwXRoJGHFH0fvtA9aKCr9NpvNh1knXOaeVsvEBqpBDDASLfBxWvJ3Za_NSlhcX-rTygUrPKEbsq3Q94XnZdQe3-MW6qWhdWM5g-MM1mIVS7p_m-0rqodoR5UqqyaN_DBZDZsxZIFVMtv2R7v5H-r2D6qDZSsnTklBBnPhBMFoK9khmYI61PBsINrE9VJ6RGeGTthMh3GthNzL8G3MsJifINSv7w0zh8r0fq1zDWoCHPUfiuFhVUogp4MYy70TgG1PbEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=l2k84PC5xcOrmfezRwg-ZH-rrqRp3M8TKamRjPNi0OV5-j2EDudnZ66rLNLxycfGbGS3d8UgfhidQjFLSsjwXRoJGHFH0fvtA9aKCr9NpvNh1knXOaeVsvEBqpBDDASLfBxWvJ3Za_NSlhcX-rTygUrPKEbsq3Q94XnZdQe3-MW6qWhdWM5g-MM1mIVS7p_m-0rqodoR5UqqyaN_DBZDZsxZIFVMtv2R7v5H-r2D6qDZSsnTklBBnPhBMFoK9khmYI61PBsINrE9VJ6RGeGTthMh3GthNzL8G3MsJifINSv7w0zh8r0fq1zDWoCHPUfiuFhVUogp4MYy70TgG1PbEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvvS8P9kuQaMBxMiRRuIStoWXTcwpvXIMpXzzcQZCoT_yHtnfP0FEGB1zeWPLosLdCI4qEyTvvw_drUQZ5h-QRaIdCcjiSN1JepuAYsTTjdaMykg1HAjVhqxFo6UwF-nmiPJ-bVVjAMH6N6SlfULO8S--Lj-Jkg18Wvyl8kDA_LGAvQWMTdTIr_HCnNujvuLDuVbZeS6u4DLc7eR9j5CBTw-dMXqkPBGNOzTVpR9XqeVG6h_Z2SyyzeeWcJAvEPzZW_rqyaQydKuq-OErrQmybCVzpDTgbJQPNuLjkELKl1yb0h2YPp753H0ZJTHs9_9x7LtMbNwGxVWvQYQYyT7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm7zWTtG70DwcFgfd0xVYip2GGItfFL43B2oHmCtUPP7MbK2a0vXmtBH1yV2HQh_HqeCcGRk8tpV-kl0HfOPwxmzIoBQMu67JW_M1rG-DqLpUhdkpTykA0l6xlbIigD5nUJOMFcYH9uVYOtqI2uq-D7qfbgdJ661PGbIfbUeTepHJAdRQLo30COd2vYM--zR_mm6KMYCwvOyCONze41VETUZcEFcnh5VkMwTld6SyS-D1oBDEdT9jzhRnVle_SyuWe9K4emozaiMi5v2qf3v7VYjqYFQReRwBHhJc1bgneJlyfmImc79nLShOVfN8OT-eCBfyQOvx_mcX48xp4E31g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB4ul2XndvkVIDGC2QUz9J4dt2Eoo2BYutzw2hOkQ-SpaNW3nenuoHN6LUg25LhGsQ3q67JybpknXMgJCEAxYYqtXJSZIdFOaxJWqbGTqL-GdUK6QDufXdIkiUVWWbC223GfZQu7_RrTYnEhSTmSvU2LTpZT4zDzA_ZEJ4MGxI1jccsodehXffxbksi27DcA_5bB0N6GNU09R_4576Q5wgs752yLUyrzghSBfxfLzx5pgY6UkM84YyyjJ-mMwYO6ERR6WwTvw1B80BR1GQbVkvHuCUjOwpuocYfE7EuUR_SadFKY0J5huWVvTPPHv1ndhq7hf2q4CaWO-I4tlWvpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um3-XxdO0ycFFoRY0mpSSCjv2mH5F7D2egqh0eClNat1S2ttEUJpM-ZJfGMARjff_7P0seozXlhqNhYBUjf5T3oCsXfJ-4OFTqfHAjjAvQ7Wtz2xN4NJRetpZ61YfvRVvfOzKifZcJTmKQBn7gRif3SfGR-hPFrI-Ppgb0BQ92vDuplOm-7PbjsSJvBE3sVGuPTx0YHmeG1s62InhuP_bGCSVVcXO5A1anSMdhrSvQx7matyCa9zSUsydKbo5sUa2JlRbaE2S4XleoI5PZAV3VshSetTTLbSae1sseXdurbIk_nCDYwsXky6OIeQFoy9EbyQQVfenBBm2g6uid8nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar-iKsAFI8Z9Qw54ozdZ-VL5irfFruQN60wzNrKqzueA7ahSkF7Or4vjpYaB3VmADUgdAWlYZ2-QULIpos-enI4c5XYfMZmcRQHrwh13zHHQEk2UAiwm_UnWEuTKWec5D9sG1jtdv9URchp4W5LoejJBC8KLQn-RL1_067EnTrX25mp0_26nEUjNEmbMThcYs7HoWB4hyRpXjruaOEi1LtlAZ735c3usAd9lmb8XbB-SUxCKtPUN8VBpXBIt3jST2j7qb6BWug8zFviifYswsbh6RkpzExkMBW-HhI1bOQODl4Mp5TdDrn-DDszSBuIVCTwlLQuAWvbDpxrttBAQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHy2w4AAq3kvTL9gh47YjteckPkMIKqt1_ImPBO2AExdnY8GBoLiAGfynv8HfQ0jYPpLKhO4XgqrbtFM8LqDavBj2MS64fpiSLuU60M1W7CHmXUXISYbqgZbmyamnle6J4brZ5CBY-XKk1zv8h3DPNMf1KI3n_WnSPXUYpP1FoNVi18jcgH2YGuu2RQSLNgQPhyMLQtvexT616LIiX6uXrK6M5EE24JzmBxeuKHEn-u5VRNj87XV-z3usP8vQodC3Dwj5IJ98Y6LtkBnNZgGASfHZU3w9CBehZRlOqm2aW0i6qcFu-cFfG_SeT5hyvflmYhocHJpZJwy7SlfRHjXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9vuamlDtDJp-i40XWX3MvaLDJ9I4YFtm4aIQnGZXXX4A79BwwdnFBBTQJbOQCRYe9R5K9mLHXcbPskLaOjLLuHOQbgTcV-UVSq0qcxo5lg2G6P1-X0Qbk3P_4SWG2_kZ4L8C-YCGBqRk8zJS2TThAnx7ihv6lFAMQTRVVErgyTTGleiR--jxbOXDACCDfrqo6j7l3WkeGM3lTZ1hRCa9ErOm9nU6ktlTfAnx0o1jEmLVBh3T79aq6yyf-o6kIix0tnrWXt0Sj_DsVD8zvskhcIkJ2s-_Gf-a5zdW_t8Dq9eqoHAjMDcIxd-nS5BVGeQKsgPPHzOqyZ6FEhL59FMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=HnWduxHmFJxzPgdlFgH7_0YcBAlzZRDwBKl84KM4mG-KtA4vvJ1_4eVzaNnNdv22kjPUFH9GVrJtM67k-5zUDaLRgCYyqQpDExdppyE8V92-vjsnC4QLz19OlK6y_tivKci9thZo--IhwFHw-f9o6wa0c8Yfw9TCCg4c3944Xw5zVV0jYJBraroDlmD0ewlFPGlWnZFw09npEPkcQS-Cex0tiBr6c1C-Q3lY7R84WqI0vjE-6x011GMrEfVvJPobc5_GVYChKz_qn1dPfi0qjLwEWnnLJhZj9PMjeozSZ4Ys_QrwPHsIA_gdBfO3Ck4AgZVj-iMTxRn0bYaxHX7QBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=HnWduxHmFJxzPgdlFgH7_0YcBAlzZRDwBKl84KM4mG-KtA4vvJ1_4eVzaNnNdv22kjPUFH9GVrJtM67k-5zUDaLRgCYyqQpDExdppyE8V92-vjsnC4QLz19OlK6y_tivKci9thZo--IhwFHw-f9o6wa0c8Yfw9TCCg4c3944Xw5zVV0jYJBraroDlmD0ewlFPGlWnZFw09npEPkcQS-Cex0tiBr6c1C-Q3lY7R84WqI0vjE-6x011GMrEfVvJPobc5_GVYChKz_qn1dPfi0qjLwEWnnLJhZj9PMjeozSZ4Ys_QrwPHsIA_gdBfO3Ck4AgZVj-iMTxRn0bYaxHX7QBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjpoD6Hi8CTXNSlop2wCUBF5PG0uyrKXSuOzvlGa5liuzXNJBW_f8XOH1_1LESR5mo08EyzZiGX2nnNTjQy3IlD4cw50glOgnxZGXhOfqi1mTaFNuk_JSgFbVyXv_gmM4hC5fY_cU4yfR5t_lT5CaAy5SB6MafZfD0ioYWmAYQ0dkUpY8GFaZfLhbKEXip0Wa8z-fy0POoas4-adNXza2bPHKlA_Qc8WDYDIwpoI5uj5SiyC739mhkvkrSFcbRdXg6uE2l8WaAabIlLFD4_qrEuLaaWVmVAi_AnHa8hVFsHtyV_plCW1eXSCu5SnhWuFG05au-vpmbmXiNYI5MrbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXX1OgMdVd1KmwX4lpZ7FdNtw9hYvSC8GgnKSqz-Qti3EnDrAMSWBjaICuK7v5YCGyOQONY9-Xpu86JEQp4GJy1pXMZS_aL_9Nmx_PURfr7hf9WHzaYrFgFM2j6BcIPSOSMJLQ1bD1KCqa3hq2QnaOLx1_Wh_cQ8P4vbY53uIy2ekE8yaNd_xDU9Na34vimjVorojN5Zk4ZD-4V9E6LEz4oaobYH5hS7t-8Rl3PnWv1tqBYmWZSVj8eY-TmGDH5zk1mdhTS6nnRAtF1b9f2vV0LzaIEIUl99dlIuvHQPIgtukpjz6T1KNBsW2CRPdUzglbSz9qpIAtXScROaxt0nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbwy22y2JVE_6G_Ped7sKQh7EznCBdX7C0BVunf06HYCYohrvwfrApAA-2zneSJozWBUHABn0ik5fzH9tLGLMcynkPxv0QkEtBLqDQ4GABP9Q5LCDuZ3tyRlZ4ZqlRR97phKK02L04Mp0KHKcnbb0_CTgRc7dkXo8wL7R8-3I6pLcarggumMxtY-H2FvlWFq2jsCW9mUX30aZY7_uCzjtNpMbpAnMyOVRzZXhASI7sFTFtIUX-MegoEvSjBuKIujCN1TuDRU86ba0NoRJWLdlYeKMm5a131m0tjNKcgt_vb4wZifMAzFQOeHSx_IF2vD2gGNRx7VQyIzTx6YfAWB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqivA5rrDazikIFth2SKDyH3njxC9MMHQwvm-q-paam1K5o08Nyp6xR3q3_R3Q1fUuw17xepD6Y0shkllSL_QbuZZC_1Ia5HMUmlYMFjP4w63BvMApg5Eqyva4eBl_cQ6vJjL5TkI_9IGnQesFx8Z_NPpOAe_tnQ-jg4_xKwf3r3Ck1tY33eJfIdenJayebswLgg-cyvjVH_-u4Hga3xMdcPCeVMURS5W9teZAhTlsPq8K7Y98_3ZKgRCKGgOiCT_X4ilSX83hmFUFVS8LxTrOwvbrsmceuxAoO-cur1_-c8GLyhesYDbxee6o_tjzeGjFQP8nXRq4lg2f8c1ZD9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3G6rdjXFlWO8wbcsqt89Ihb1jtCw8CWMPOPAzqw8bxi0N1bu10SBFVzojJN6hfVp-XfmzW5VL-tZOswd5OTZFzBPfVEouRyFaYmhWB1_DGqulQO6dTO1bLLr2GI_b1oBrJVkiT5Q5vhRstTMmrW6SuUncLTjMRuecA5lS46Z1-M5kgTcfzV2peqzCl3lr8UJqOftueZ14K8Uhubj_RTw35c8Z_4VKUrbYk_r-gLGOwvKNudNbS2eLp_06xY65sVIuSuz6cn9Cj7TnyfbfrxlfJDyWh0WEwRV3QV_KgUx4MB3Hls5HbTTvhh5HRviS_74TkLI_xC0IFlgn4GBUQBL1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3G6rdjXFlWO8wbcsqt89Ihb1jtCw8CWMPOPAzqw8bxi0N1bu10SBFVzojJN6hfVp-XfmzW5VL-tZOswd5OTZFzBPfVEouRyFaYmhWB1_DGqulQO6dTO1bLLr2GI_b1oBrJVkiT5Q5vhRstTMmrW6SuUncLTjMRuecA5lS46Z1-M5kgTcfzV2peqzCl3lr8UJqOftueZ14K8Uhubj_RTw35c8Z_4VKUrbYk_r-gLGOwvKNudNbS2eLp_06xY65sVIuSuz6cn9Cj7TnyfbfrxlfJDyWh0WEwRV3QV_KgUx4MB3Hls5HbTTvhh5HRviS_74TkLI_xC0IFlgn4GBUQBL1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMd0zeGJOhO_hW7e2G63hw51qVe8D5BvL5od0XMEBomnLYLQL9GFwGcQHXv_qydZDpHC4n8ZEO1Br-zTOFkRUh6jRhXsxNvVN5jaRpKQZxIOtXepi0et_TfDcbPiCFLeoLyqkkYNCTBNv7xQWZWEHpB6XkgE2_WTgCGWhyWYWgPSHScqTHfZeAJIKDPvXrMsxMJhHvHzCA013Bho1UBBw7a8MkxZO8HNc2fZCm8JFU7LSoWfEPMok4EhdA2PXomQShi1MqzdDVtzyfg0aBM1f51TsTpZTXk2_Vwvd65jVMV7ih73mfUS0zi4Huag2D1OsXkQueFCyqH6BSqttTKu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaMfQAwFrJ2v_h_oQkwCguyte-64GASM4Y2L2VQtHyX3IRIoCpATZ_4bxm24SZseiLapDJTE_m84hHui1iB57t3xB5Rj2Mr7WbCRdrNhfxxalmcHLiVWRD7z4Q4MDeO8XECBiy-LPjrcNp1ioWRtTXxWF4vsoD3MMeacxTjEZGwo0EslUnlkVI35_i3hzYsdChkOEGXgfkaxAWhYla2n2uJ09AZcQSWyWmMXkX9TyKZnz0W21bblBpNlbGKn8tgKu18LHKMH0S00MvbKtUoz6j35oN0-PUJBRZfbtDRyqFQp8u4Bo21zvkx9u_HWcz7v1nvYMOlaeAOpomODQ9rj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_YD1hnCZsZY-uOKtqBki1SWvcusc2pBrnRRb2seBI9fp43oW7BFyfaXqjMuFMMIddnJP3H9BabwWDYAny-CbyVS36rkD0__6FNCxIhoTPDN1byPhLklc4SkZJrWs1ajuxU0ShfMKicCsWADvC9im5sGfu7X2kJwwD9_QpKE3STSZF9hcmZjyoAqWjUjdq3-M6gD4MFqnarthc9c36WWmf_21GAwkuRmn6HIquK7t3bVMMAp-2zdc1vTI9XDQMkfsJpw5hvK7QzIhJa8QD06wHfqArjkzXwlqePLSdHRAwBcW-_2O36vkerw2ODim0a_AQ-P_clOofU39RFVBF9R6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=bmWDcQxQ8KN16ogRaUlx_zkkfxbAt8vBa4C3batyymYRbifA6TGo6beAa_S2xIwWOl4-WM6jDxaiqS7fKHlunQ44jKfINk6-sQGtqAbZp7Z_VsE2zJBKwU4KhIbdfmcasd2rnDNS4MLVRVZ_OwkOfW1BeMt6F3LuBfN2aQmNJAt6GxgUUJSJZmVMbgDswqPHy3UFfRurxlNN5uhXz3_w-yqaoyGS10EAB4zWeqe3xR7zjTencd_BI9D1xrinD6dSbwcae1WabI1s5sTRi_hHVjlhX4qlQUZe8FCyqc9NOEtQXnWIYu9v83Mhbv44VeAg7I815RA6PgmNHaLktdUlfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=bmWDcQxQ8KN16ogRaUlx_zkkfxbAt8vBa4C3batyymYRbifA6TGo6beAa_S2xIwWOl4-WM6jDxaiqS7fKHlunQ44jKfINk6-sQGtqAbZp7Z_VsE2zJBKwU4KhIbdfmcasd2rnDNS4MLVRVZ_OwkOfW1BeMt6F3LuBfN2aQmNJAt6GxgUUJSJZmVMbgDswqPHy3UFfRurxlNN5uhXz3_w-yqaoyGS10EAB4zWeqe3xR7zjTencd_BI9D1xrinD6dSbwcae1WabI1s5sTRi_hHVjlhX4qlQUZe8FCyqc9NOEtQXnWIYu9v83Mhbv44VeAg7I815RA6PgmNHaLktdUlfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foyf2fT6mxyfOEYASpKVvihI5uB8gn5e7uAAcg61YtqcG1Q5_P5OKtLD_kIFS7Q8xSXa8muPN5X8LfQwB0WtgKKMXqOWR7Se1Ch4t0M7uDCIoEfasUtnUeM6oIZBZNO1T9YZKou6IiCbzijiGovzhkhFvJwR4mFy6zR-i4cltHAwl9tMGBOPppPdSXvHHTWZIm4EoDQrkqON7tMpoMsl1JleMQk3Xko6iXdHEKVUKNvEtpD_qb4Uexrc5Dl_qSlHsFI-yFUGNdBFiBnMveg6pRegnULvz9asi_oJN8yFsJ7hgfI2E8b0XkgGHXx-DChnhXP-QjaDOJiRuOWaHAFbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ62Mu215Je0cxsdDESfmKtpNyvONMxVs5sGfdfGT3nRlaK43qdKaJJebQbylDrx417l4EeCw6CnZ8cR9LHfq930KsZLoYopRLCbhBESwGlXK62e44CEt05Ih-FB5-TaDzgZnTOfq0Ukx74D4BttLz-ohoflrT0wFmsKVm7gv_vvjWIP5cUQem76iuLNxBR2DEsARI5EerGO5VqF_7oJwv3AgJPiYDSvPCnyaVgkIbECY-neZH5UfbFkUiGDqx5oPRCSAf1G6pCa6w3aXjmMhjUhYZDCniWjheqcrRCFrxQcrNA0FjuaOEb87tOLf7dXH68-WdLwjDDqc87sK9-Ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvCSnfHh4rv3Deh8b0ooEFIzHdJp_pJsi0BIPHeRAh6lgVoHM3y1uuZ-SbrDsELxHxx5jc95futwkx4ec5cyGiSFeCOVXw4tki_Q1O6_5pFtE4YuLi985xsGv0fOetb0KUtFvimUx21L-g2htXguTCctySyy0rtPmMYZLzkoFXSETrkPz34uBbTVb4Vh3LRqQZiewjxDIJjqMc64oQ9Bl_UazSrzVNmXQ-Nq2LUsEbWiyCHT82h4MUvj9Azbj5gF9vJVixuNTq3DoqC-SxCioaq8jfIsAhBXRZtnZ-eTy1N8ZyaYUTPDhxiUhepn8MghHmhHS05CYpUPTwPm9Z3vzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNeREQYMDmE3LnfLvY9sFgXiUSpOTPbxhLFHSbM9b6G1P3JlVwg-WLiVSgliL_pJSa93ebZG1sF7DHuitpQiI079SwX3EQ4h2sKkWC7i8doGFRgfTfVYB7etuepvs07nweTkU-41rEyd43dGkl3kDbyJKZWS7EBinr0kMEAYF5Qg3v0oDpjSCmB9rcnGqoRVL37Ko0MDeuKA__5IIDvn-WEvD_cbP6ysCKWm4wCTA5n1doXaWl61M7usZRWCUSagLFt7GZTy-VYJ46cSl_MVAHysXCbXC48f_zBb0y9Juk9GW0f39_R66tj7y9pG_XdtK5VNetG5Pjn1lr8phtVSSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vguKGQKfSzVGyKPIBFo1tXHw0eA3hidr7cyZ13U0PCqthl44-Kfikf5mziV3E5f1ZUDEDCtIewk6tvvzeRFMWwtd4M6Sue-Nv55eaYnuozTpgy0-_nM7EWOsjg7modio7gICcH7WvwuSlwJuVenKsAX4mf03bcO9nI-MmVsI-vlHnYzmQhTkYfJTvd9TOhtPYlGpm408TNC9aOlRyHIsTnF7wXVn9j_3vb5IsbXM4_lww4dcvxphY7FshTLbocpWNJoOTwapZSVHV9Ra64YIQ-LHoKDt4Ql3T_nHYzbPtFdbLS4aVeGGppicvedQ8TW1bftbNyKnc1ghsbsC4Z9zCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMGelX5I6OI5xQKQ4kL6UqabDUYSV8XDSqALT14m8rlOQGRQXTXAK8aeT2PfUYwSczaijJa3YEr2sitrrM9b9cMRtJXaQgHkOGneH302agNQ-lRc7nbD7vk3rCuNMLiCoo44_keRoZpkveoZN2Ojdj5b0XduvbLcQHJW1rjgx-GkLLhPH_XZRBq7qnBRoO3fvdUHygVgTjFmUkPVTbuaa5YQ4skp7QmeHxGXATp7dtBVR0GnzADmkbmdqlhqdC_4txGhmAuoLjtIfU4AW1HsqlUbHpqri5LW4PJfDW1_Tm_yRS_A-djFr3OMFbrnmL28ZpygtQFz0ePGUNm3mkQPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uisVvhwitOusVKfG8kVDPvFk8Us9t7ZwoIO3Ry0zyVFa1Oubr2s01aAl6st33pYQAD0gD3kUloBvnFJmkvr8_aeS0D7cTRrTwr2SreVDM5X7gXyC1l5dUVar6hrQiir6G_hJinHxBNMmk7nvnpLHkBOxH5bfho27whXoqptjuoGopqomSUwJ7gQJ1sStKFEy8g3vJQeRV6U0mTwF7tLtZf0caMIpQkvPm1mQ_tSqWUtNAQvmfrrjKd6JANHMN6ndi7uJkVaYsaxC-_36K9ExS91XoLzWaDyu8KBSzRNgYt2mDBYE5bEQ0_1DHPzO8MEQCYNentlNLwWPdSQ8kuVGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crzQ855I5J5TJXMSG5GrvBaGEE8HLRfjEA2s3AJ8RXsI61ef47m8brRPTIM_9B1zBXTCqK87mW3RnWp5HCJwhXuSoSRUktlLoCfxso8feRE8UpTmY22P-PMzaU08-KQ7HllgSZ85fu96NMEBRgti-uRKjltTB6tc3vaZJ717wLVdY_RuYPgbSrvqCI3iREJCCbQtC-mWP0A0h_e_Pf3QoxZnO-f0y-asSNSdPsUUd-YDoxQuoKfkMiTSBPwe3khsLVoiDyO5SMDJjY4HPH8Y16erTcJ2VdQ46nIo5386YJXBfE_mxQehG0fQCmllEM2fGiofSTmfewJMTaecWd0KJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=QEgh3VrRZ0XOjogVcgDO7ZR6sEomjHxVuJkAcTShUiK7K9vlCRnUQWvjVzTIG8h1YrhQ8deH9pm7FNrHsX4-r0HXIU_TtBtwQaqe-TJm6i1BhFtFh1Z_rHXa4VUNuR6FpH8Y1XxtX_MT53Q6-6G3m8JOzGNfjFI9skbEiVVqXW5Zc3y_znYDdGIjW9zqWAMSSp2v2meZ76F5K5TcoAX58oBbqLvzR7lhQL0igD_enSdPu68NmY2HuO-7zGygcNA2-cN_Zjo7K0gQNuNwUjWz1DHbQ0S5bAhUKVESVw6i1oWM9lMo-fmn3_V50MvgoUrQb1SVN2NXhVoJsNf4j9ELzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=QEgh3VrRZ0XOjogVcgDO7ZR6sEomjHxVuJkAcTShUiK7K9vlCRnUQWvjVzTIG8h1YrhQ8deH9pm7FNrHsX4-r0HXIU_TtBtwQaqe-TJm6i1BhFtFh1Z_rHXa4VUNuR6FpH8Y1XxtX_MT53Q6-6G3m8JOzGNfjFI9skbEiVVqXW5Zc3y_znYDdGIjW9zqWAMSSp2v2meZ76F5K5TcoAX58oBbqLvzR7lhQL0igD_enSdPu68NmY2HuO-7zGygcNA2-cN_Zjo7K0gQNuNwUjWz1DHbQ0S5bAhUKVESVw6i1oWM9lMo-fmn3_V50MvgoUrQb1SVN2NXhVoJsNf4j9ELzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=h71flR6E8ovQHlT8iWHpL1w98qRdA9A7g46SChJHNJ1YVYPl89DJc-reG5RHfCz4zOYtUMo9VpUbq9ZU3XcVxcpuxsxTAqacQMIcPrlUc8XjnlGDwieScWTX_aL5tZ_fod30fNoKNPv_ifGU3GlWExP1ot51z_SeDgi0McA3ogKGSi0m_qoqioRvUQ04d3nA1aPmyG5i7d7hN9OHYJeh_ehc4A7LVbFyLECv2a43sjIVb8nxFbykr4xVeqIgxgUxP_M0-9v-P_dOKNGMSfdUlL0_AYW_QiA0p4EE5qNc8UqML4aWUZPG4ou8YC4kZwoWh52Z7ce6ih2eo6gE2uXAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=h71flR6E8ovQHlT8iWHpL1w98qRdA9A7g46SChJHNJ1YVYPl89DJc-reG5RHfCz4zOYtUMo9VpUbq9ZU3XcVxcpuxsxTAqacQMIcPrlUc8XjnlGDwieScWTX_aL5tZ_fod30fNoKNPv_ifGU3GlWExP1ot51z_SeDgi0McA3ogKGSi0m_qoqioRvUQ04d3nA1aPmyG5i7d7hN9OHYJeh_ehc4A7LVbFyLECv2a43sjIVb8nxFbykr4xVeqIgxgUxP_M0-9v-P_dOKNGMSfdUlL0_AYW_QiA0p4EE5qNc8UqML4aWUZPG4ou8YC4kZwoWh52Z7ce6ih2eo6gE2uXAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEi-uuzQp68P0KT_vhCsrgFtXaOq97vc-iBr23ytDnhnxI5vSMxOfjP2x2oMzq6bxuAear4ZPVkZIVHwVWNhh2I45_eBZDDXCQCr8xxTmekURIY2KnGw6Ja7OGgtHwQjb0A-M4aIehxM3S-M8rAvhFUenqzBMjo4k2lUKjyZO8I0QdRX5h7vtUl6IF17CQ4PFzkYzv7B2Jffgs1IXIax4dabxgGWIhqBZlpXLtqxpVUtk4SNT1xZqd_3iFS9n_AQDg9JeUrlUc6B4pIY1zx6WncJk8OZCsfp-Bv8ZoYYri6IAjxC2c05-wgsynF2h_F5TYCmD47OEwDLZwe1wr7cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=TMKPVK4ZAC_4SVQj15vKpAOyhZHVsWHYxx4yeoKV8G3GwX3lELbn5NAhRvNaEEKfuMmKrB_gdsDVW6QzlVU3yKFZ2TaDhgxVDR7Ewb3ZOLbv-D0jMUCIKCyzK2V82ldWW2qO3LPI38VxkE__kVvnhOLJu9Uvur_BEXzZLuSBFmji4JG8yUw6k92kY9I4OJhZ0BDo6A_gOrKm9S2rdrl-7N4xUabDLWYW8LrpAevSJgvZNxMZFHLly-HTZ1txKXScT12dZ3tCoQ-O1zzOQjAPGsgOhPAOIKDc0pnGbaABC55z6eRpvaVoVYpdApet-NQ0Iv6vszb3uTzA1QQ8CiIf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=TMKPVK4ZAC_4SVQj15vKpAOyhZHVsWHYxx4yeoKV8G3GwX3lELbn5NAhRvNaEEKfuMmKrB_gdsDVW6QzlVU3yKFZ2TaDhgxVDR7Ewb3ZOLbv-D0jMUCIKCyzK2V82ldWW2qO3LPI38VxkE__kVvnhOLJu9Uvur_BEXzZLuSBFmji4JG8yUw6k92kY9I4OJhZ0BDo6A_gOrKm9S2rdrl-7N4xUabDLWYW8LrpAevSJgvZNxMZFHLly-HTZ1txKXScT12dZ3tCoQ-O1zzOQjAPGsgOhPAOIKDc0pnGbaABC55z6eRpvaVoVYpdApet-NQ0Iv6vszb3uTzA1QQ8CiIf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcHqsQXYdEAkipOHeohFHeyab-dSKxG5A_vyRaShfbeR2LjVyEv7FmLokm5ROES896WaO5oO3eaEZNxbjzmIIWMMnPsnHrevYfTp7pT-2oZZqiuFT1kP1h25KGeremJLU_gv7brDG-U0tOHGFCW3roaVjidR27Fil90iONMVt8atkIs_AB2IqzcI82EzxqWXzc1sKOjm9xUcLRZwtz00Bd5PKgG74tXRZPJUchAYyQLdS6ft20TryCQeFOeZ0y5gobyBsOyxg9KLmASmMpwrfJC8oRElTk1Pq7tsqga0DEl-Dv6PO60UK5ara75l_JMri26koASPGBddFUIWevLrZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGvr8qXvmMZe-ByZDQ7sGMXrRLFWWQknYUNHCkGXX5y4ix6SwGmQiAMsHae7tGOdO0sG_7h_1NmuivIYaxi3gaZaeY1UmioxzbQog-5KPyVG1FFCNSZV45a5BeDoQfq41-YNjxCb_KYMEd0cxIV9uLb_bj0H3YgMb1eVpFW0Y-Nqwcj7lyr2nEJI6pd8iSk4HM0lyCnOUcmgF101YDg0CAGlUt8B8lx3dJjJ-HbSkzwM0sALbK2lQl2VAnBOgCJrgONMLdpztvsPGn0sn-5SbzjHN5s2pO8072_0ndeZmhEyTsyeKKtnCPKJfARgD3dXvTm0VoX6ArsjYBA3HshjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHvPu8YLPr6uod_ss_JZLokwEv0iBBmwj5NiKwmcFCLol17dg9FiQjgDMSttC6QHTlDkDdsJ7LiM223dwlLZeCzctd1XA6dwuJHKWE3h4kqch_W2KNtldMLU-_GfJ0bTsDkEJ16ZkwoUs82CNScKhDYESY6YjtPqWJBwNKTLVwstmmpweiu9zH2jWg9tGuqqDvHfWs_RRZP5XHBFq1NYv8S9YaRW3pEbvUYDqotDas6__6k3MkLpgvU4bLcUaM-JA2nhR9LR3E6OR9zFJITNxM6fWLbbm-ByWS1R_Fo2Mz1ftFsRP3lQ6e-2v9dpkTZF9VUNtpqdltivkZ8-ixt4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2PtdxfEcHGPTq3Ag2CjsdGQULI48-hZda71GGSHUMXcVlg6iXkGVZxceFLctt7tnpSEIH8oY8e__gXhfAY7EqYLP2Zu2LK5dWO_bfNt2slg3GA1_YSMlNi3FjDnnUyxXDoiPUKd6STB19f70ASkvpJmGa-K6oA1dRFFpxid1y0pR6_iqKRKri7uDgz-QXokLxgnPb7ckLm4Ixya5HQLovjROHpllJkEOxCrUkQVbgn0HOXgnfgwg7TdeqvtxYM4tNraACiEBM37UowBdTT2yM4iPhUpR5K_P15JYEeRtNsT77Zh5uutTe56yR4i4M4xxq-yAyxUq_6B-xmttCYTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXQ4WGgi4XIDCtHvnrw1SesNyz4Po3rV6gc9hzu62wkMQBmeFKlpP5smg20CAkdS8yUE0EyCEh2yhhugcHXFB9oF7LLMomD_PYbW14-REzMklYJjWV8ZZeFinNUsda_o2hv33cga4_MI1_6xP61ikHoUFlTytbTOVgC3EFgJi447MSpWoZ0gEjsqq_JbLQ6qYnYLS01xDwtMD1ajFGfvCc_p_kUg4gaXALf1tx82XceLjaX7lxf5fIYEmEMTLNky0Hi95cbWgwfRbEDfitvx5j1QXZqRUJa1OpKmgEXxt8Clwgh4z0Y3Y5_ev4sn58-dkaqvbgF7wtAryxR4o7plTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLvOG4D9W0JVMIItkNBgBBc6JWO3dCUOPe8QueDHyS_KuQZkionzzD22Ui1qcQ_BF6E_3-F5VmAMF-p34co5FhAZonpCriM_2aDOnTJXgggbD6LfG_a6bBvHrzJHr9YM4VwPSG3ApGTNAIzKITiZqnowW1aCanBcNZXGHHLfY4836laxEPpsbT3Bx69k2Aa5Hp7n1LV0RaKTaFZIBY5jj56jn9-btmFv31-qnpkyXhrmbl_UB9wS9rjPvcB6NmjOSU0AA0mQlTL4iHAwlbCm6yZwCPDGLk6-soK1HPS1svAolJvKfuocv82BsvQCSlW4H0yjRgmvFQPrzzuRLR6_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSeqstPIReQJMastylE974agkdZOJYLsiekOUh6B9CCv9n8EKlyOsxibzHLNHCElqE_KpfFQRf3ticj5KqMTsaMGKWzjgzYzRh96MbjTt0QlTPZBAzCf5rZABI94gTQijTgM0soZ8bZaX1WjUXtgx2wBVaGMQV2jZuJcnMzXX1XlWzDbfpBdgcbXq9VVXVq0CgV2W1SLkc8gH9cneS1LjigB-SzZdpDn9OYzbs_wPhg22tf74ezGeSXVqaB32kFcr8iq34V1UYV-ANO70paEgZbFIpSTDayzMAsmKROql55JssgSst9Wjm_w_18tQBnATHWGPLYoM1G2lQZn8eyT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngEd8yAi6SFsRxz_YXvEVrDUso9hhyuzKNr4G5bIHixik4obEbVt9t5wiHAN0OxwHXrRMex2YN3vU7KR31qcg0y3YKMKIoKXD4fPrkZN-kpM8AXbWF1WGgSk94RYagdT3wc98DxzPQ4h4OkGRpAarAJaq3a1fD65_p3oEY2j-yhzVHtem2FYifOadtDX5B6c6Q5e7sxKeXBiIBohRhyxrtS93GKKBj6joZqmoTWjO9k5y_mLsNNCyKQJuFoux7z18m3y424TRxRzSKuV2NhOgF3TxxIFArbVxkxsrpNHophpOrhzCgQOMs3RLrxG5h7qfs6SclFvqhix2Y_sRKmgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReuWg4zlPs-j9sDM1mon1ZHgUcf7o5uECzLJhxgQcjnUbckJf9TafAawPlVC_ahAOiy7mXf9Vai6IL3M5jV0gPisg6wIxQkyaPDaEZaUcv7umAVJplqhZjjz7Gfa_Pb2rlDxky2xvQgVfHZxG1-pfv3LW_u3qaj5LIcUPK3bDwzdDG2LhrWWMm9pT-QQrdOvkkRWnT5XyBKDCyDCk7o6etibPaNJer6d_hsTT6osRtg07iLvoTW2FMR_JJ8UV8wX_mwOo-KtN5nQZO-7sNp5G7ASVy984zO9ynvCIh_MVQjyc-CPksV2zNRMiSp9hmeHJtZ7LFv8nUtKEVZvNAsddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIpZySoGZiOR4AJWUaLfl-Ezo8DjfovzE3RZdXWqWM9_GcmS4cgV_vvtZtPmaVySNKala51_OjMKkTk8r4l4yZm5vbYz_cFjf_IvbtSCKP93ATeB_TZhcGiJgQ6uidXzdCpVRgmA0tDu-M9N0yUx66GNp8-3nBTVezemWdtDPd4bmm98leqB59ColsPnFnZpH_B0_62q6ulgiG-pN1a-GmvLM5V6w1P9cjyuATn7o2uyjmC2plx8Vwn6dJ6MtmvwWsGExllgY8iMS37WcaeR63O8IrhaaGNjt2Pggjj4gavXk0Z0dOZVSMsQ-gV4vSJmkSWW7QTtc_0WVLRUeY0IdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=aXBZbhhiz6piSy26ukHucnl4nEr00lQzvzb_TFbwd1C_dmfzWdvAXY5sCLjfbKbXtEfrexMpbuw-aAnrDfofhS41xThfbL32VhdG6r66lILf_ZbxANXiFAQogbKeJC03RMaNr-9bV8_925ecJGy8-bqWz6VovAXN9HSwaLPhLSEEji96SAofJ6mOmbIBltHYSylUsH7LjZI68lsE6jMEvip1A19MoQEAugPfjXkrBidz1XRXYUN-5CiERKSBtHVpqhf9A1EAjOhWQPNlgCqfddfyngtscMwFiUsbgVZwVjOE0z3VwtsyPNLMITIH9kUvQ6SnJJ5efiOT4bY70FzRCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=aXBZbhhiz6piSy26ukHucnl4nEr00lQzvzb_TFbwd1C_dmfzWdvAXY5sCLjfbKbXtEfrexMpbuw-aAnrDfofhS41xThfbL32VhdG6r66lILf_ZbxANXiFAQogbKeJC03RMaNr-9bV8_925ecJGy8-bqWz6VovAXN9HSwaLPhLSEEji96SAofJ6mOmbIBltHYSylUsH7LjZI68lsE6jMEvip1A19MoQEAugPfjXkrBidz1XRXYUN-5CiERKSBtHVpqhf9A1EAjOhWQPNlgCqfddfyngtscMwFiUsbgVZwVjOE0z3VwtsyPNLMITIH9kUvQ6SnJJ5efiOT4bY70FzRCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwWN6K908m6Ybxd8FcKRd0ZwRbxFgtrKz7GvM8fVDyJ9Z649qYkUBjKk8jUyhFLe4fGid8hclYlEg-536BgXghzMsqBhRXIiScbY9tVkVzuPDWWaFjvGTVIlLWzyI6BA0Zd8sCymsjvUfifTjLAhCY8JF1VqJA_52064ZNjfrHqgQ2wcVBEVzLY-NtGjrc0Ii1StagElgF6cLA6XFAZbmKO6C1TvjEs6Igy9WLiPN6V8VyB-pm2KfrXa2qgP2uu5Bgq_xDgVCx1KUrU8rzXMLxsnjtj75xc1JPQTt0TG0VIfPTxN3LqthgyLz5L--4l51R3ro0_Qdf0A-njMiMBALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYrjvNk73_FdLXKZRnn36VLarXvvtf7nxz02Mr7tPmexVy-teBZOwJyWWmNmOmUO7ljXreYQMWU1_iSLk4pXzm6sHhYYe9R0gxkqmSt2A3YAZbWAbDqUU19S79dHHtibpafoIMb0mffLlW1zLwd9FPPHLupZbsiI2FLXQ_VnkfO6fiz8O97wheJCrR17vTuA7F-7UtTCo-4Fjr0WdSW9yWq9XVYha7VQee9p9A-diQ05w1OvjFKXBqcN2wy7F48nmNeM5ry7KEamP1PwmsGQqaggXEhI18KM3gmwUus1UByfAwrB_3qtqCTrAzBTeLp_4YjvkAQWpgiZTxzV18YdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMKYBuOih5u3wyCt-5NqVW5dGh99kWMiyHpV5Wr4ZwbHE1vfk-VxMhsqFPsD8R4MPrYfKzeispBQp8VkYduPkwa2h-gwj-clgBPvsyFo4yGYK3MwxFuB2vsVSREh_rlfAblCzeJU8I-Po7Otce2c2b8GGgvP9w9HBkMeWTj8wZmOje3TFF-FRkmgNpU8v-y_BDsaioPpRB8-rqzTb8RlWRiDCc03efe83RLjD21zlQntnYn9A4jh3rHoIanN2akDrGJ17pNFCvKEgDz0iaJKf0O4bSSsXkLe7LNV5iS8mYlhJt_q-45AlJ6_bekX8nVJU2oeC1t81pdD7b6fxH9Zog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf8H-mlniQTWxv7zBermHJknu6dCULrMuW84oNNxjoN5P8gUTfg4E_VZ4H-5KTHOQz51naopX1y_9xigjNOh5x0nlkuIjioo3GmO3mK1htMBmmx3V-etbWK-CEbEmc-3tujAC5Lw0Y3noI7K8Cg_h7nr11RgScp5WE87fjFw0fn9xslb3S9yksjZxRvt3nBulLMMysFxr8sNjTZwfF9IKGQLGpmh0xmplVAw6exZ1RijUzWvEJp-e1rA6q8xIvzSZtnfDXd7WOgl5Y16LeR9bXj5rf9zyCtpVD9ekfndOJWpLGJWEEHkTBtgIZN9CJfoPZYNYsLjzt3YiSL6LtSwYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=NB0PmIrhcZnplp4ICJ2towSvss8gzVn749e8wAP9BgIW6GF0wz-wJCtQL0XLh3qTiCU5as382WovTnF-azLzsMnIsNtFMQONdfAVWvZ1lAMc60B7oDiBTVZUmCYXuu-DzCk5kfOE44x2y838ik1n37XVGyqWdr7pJGfGKYkGZUdXDorMvMgAe3ICUbh1QB6PmwhTvYN76w_U2YMAkhW_S5QrC2YwB-WKCuHwk1V-IGxpdjUh5h7szja9HNnVYRyaaRtFrRJa9fnVvJl8GyFVwVzRj_FkafxF5qyC_D4UDboGAQkPvPqebowSpUPW3dBDv_JJeCKYL1GHU-bJLhfBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=NB0PmIrhcZnplp4ICJ2towSvss8gzVn749e8wAP9BgIW6GF0wz-wJCtQL0XLh3qTiCU5as382WovTnF-azLzsMnIsNtFMQONdfAVWvZ1lAMc60B7oDiBTVZUmCYXuu-DzCk5kfOE44x2y838ik1n37XVGyqWdr7pJGfGKYkGZUdXDorMvMgAe3ICUbh1QB6PmwhTvYN76w_U2YMAkhW_S5QrC2YwB-WKCuHwk1V-IGxpdjUh5h7szja9HNnVYRyaaRtFrRJa9fnVvJl8GyFVwVzRj_FkafxF5qyC_D4UDboGAQkPvPqebowSpUPW3dBDv_JJeCKYL1GHU-bJLhfBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj88smNWfLWwN5SSsCd9MhKgGZ0hs3VJ883aGJH_qXJvMp4tvflHP2RA7ypr1tkdHBuYSk_k2dyFBbcjoRnDqdZ18iBMd-VD8gtEaosbDUz3saLttHxTkF0v9ukX8-EBM1zt7FQ3zdfg8o8j4tOEozvAucC4pPtvuCD7BqIiDPxjMG8r5zmw4wjYK134vOT82nL2De2DQfxMnpwbuDMq1DShq2OPscQIik5G-GZ9J1UhVWaN7B6OHZzmaNfEKNfciZ1movDzRXAqr28603VT7I_i7yOgWP9e2xq5gpvP8RXVW0jUWPjJpAEGRN_xa4dRIfPUC5fT6xtxz1PvpEQXxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSCGfRZbA30U3ocfuGUgL0nH75HezNzcp5Xmgvx8BDeLV2eKH7_2vJ22_urcsugxs8MYqeSd07MnGl_R6K8hTp4B-Sq3zCEJ-0jjbeBM5IZttRwW31c5d3hpHAyRarIg7bIDe-DzqgmRHVC_Vbu8zG5ZhMRYkBznmUD-G3tvu4qH8lA-Tc9d0Isw0IEhERtfVSh6Is5fQRzrEggeChX2K7YFoHQpn2T500aqNoErUZwZK6gM9OyrSGz_Y29DgFlnbXC4cSavOHG-7yZvz8kN_ey5-uejt6cjXwRjxfsMwC_wAlqCtVSRybTCesZkMf8lvrx50ku5r1o5lfNlzAJyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMPvyNCSAKneEcgoobgCqMC11W6Ltx5tkfgUAWZHqOb-zhv84U_K89oorMDun6mEGEZ-kp-eX5Q1Bcwlw7ExHU85ALIhICnZ4BesL6sSyUY6AQRoLVQNVG-zZQW75j-aic8cS_hlDbl1RouwMmW0kQxhvJAl9nW3slZ5mhLojfPF_JECyGMeuqU2VW6pOViQIu7UQ3zWaH1CbtK6d4d3atHOyg3QGKhzfTOwXDb0vD98UUtUEzpW_Iphf5rvIYIWDlAoAjoWCiFG2TS0mE4VP0XyDnn0DOVWDzXFwKaIjWuviQqtxv2VdVg5bz7fRRyUjxRIsS2dddQxDZrc2DpIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMhYjNLH5eHbn7GeS8h85wITf6rNvbJy0kmn4XKDdDBfZllo2g3XXOxzskmmjuRm0nFY26Ge1mZx6Fle0p5BAdjjJcdHA2995OhLuf2B3Fexzn6_6Ovp4aH2qgBwiW5eRUehl0Wojffzn36ZYJp4zwammT4qWsYXNHtvKQhVPMbgKahhDtTrvPdWFc4eD58r5TDQWeT7SXHc5-5CETeYw9hY5tntYg58y7ZqFLNvBCW7IwpA21m167GLvanju-Prxrf6ECk5Dosig-85aTeDyXzr-Yby5rqvqJhYlwBGRYaHvwrOVNWJt_grqoq7rQWDv5vzAMfFIY7Z7hHRPfOVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
