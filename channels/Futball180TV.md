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
<img src="https://cdn5.telesco.pe/file/rd1PQJJYcNCsoz5lOXocl4dAccTnGEqHfpNqOsrkGScXw75XQRQ-O5_BhcZue26wfzTRioG5A3Ry8bnMmsatOGJpACUe-35mBVK6w6Z8mlc6O5ImEGdWfa_YvJ7NdgPp63ekynj7uTDdF3zVFZV5rTQn6qInKlVvkUfOpF4lQhwqnBXfmocbqLijaWSU7KaUzXN3iQkNRLwhEOwf_rU5Jipz2NW56O0khWMmVEFE4Tu09Xx605zDTfgf30bUkB6MXMixt304RBnHaZA67jQz2cXLuGiLLUNb9Kj9MoHzSO2Phuy60Dwf-u7tvZiwxjHAbtgjOrLqjAEsYyD6ELiFig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 488K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 13:56:28</div>
<hr>

<div class="tg-post" id="msg-102976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlXT3fcPMNQAQbqRwG8QE-xnWAhu4oVXTW_pFLN_ULQdKn6tekmP7eRJe6HFXeAItci_Z-yZbyn8XnivFf0-bfF2I-lXzhkAe6zwGCh6yddcycxh6gY72Wx2i1CxoqZeRtGHM2G9o_Hq-FfcpqJVPHNq_OlD5Su9Pcv8Qi1PFU0TpmG0Nro3mBVUoPcJPJJfL9e_vL9aC7KL6Mr9tcbONC8GtspsTIFQ-BRjYwaHpMQr7mIRx4FXSCayyWhprsXv6d5NaBJfUIap2SvdGHLSVJSTzMxD_apq-TikHe0rEOctLm9yK0RXHBdpOZ6TsvxZi9MxSF-f6YDVMDRCyTPagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
برخی از ستارگان فصل‌آینده سوپرلیگ ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/Futball180TV/102976" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102975">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw9noE2Oud44fNMJzK6qONXpwAdJj3yd9EeqNs_YZriLM3GX4JqxdSQncZlsCjpSHysfjk-xy2CoOY5h-MDs5ey-1lvztloRNPuHxIFsYYfCoUGOraxXPbY6_pqEKXxFxnkr11t-MdUIej8FxG7P9M-dVChoCTwBaD9vEApxWCikeJrx-2JI8pZ08fdZ3DcfFkHNcw3z5CnVuWtvVc_V-SYTHLvWKF-Nj7s_xgXnONw4s7WRNpSghkCe1lqpzWcGme8iyZ989tcJ9OqBKxJ8fRg-mnuo50JgP2wVqh6TpZHHr3B3qEcVzTq1mZjzgT4yU4HuJh4pW0VCMQ2-_ePKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسطوره موسی جنپو، وینگر فصل گذشته استقلال به پانتولیکوس، تیم یازدهم سوپرلیگ یونان در فصل گذشته پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/102975" target="_blank">📅 13:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102974">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6I3sAdykoC3s50xVCDZyn7QUa3pxR3O3qtg3me129UBBUno40zDMtiVY3xDywi2CjhyLmJgRCdQafR-DDcIgdf91ULxeSkVL4Xa_A2kepOQzjVVU0rxk8MeOJFl3R6dtCsQwbUOZOVVG_qMkT4yS7MlKOx3RlolZ2VlJYN8KdZp7WdzsbyRBo3TXXGIbhm7Y4hnGoOQMSixXikJLs49kuvMRL_uQx7Pp7Wu7jLqe6TZwAfW7bs0husxyv0EyE2PU_a1AwVdqhiHdx56EttVJmSRaFf3YwLuKZnpgjvp6lA0XKw_yzISMapIZdXslanmQTtjn0U4-QWr4oeod3q_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول برای جذب بردلی بارکولا به توافق اولیه دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/102974" target="_blank">📅 13:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102973">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=B9MDUn_TrkCuhy-Y9bB2i5jCrSlCTOyHcxDK0QTRatQdVoYk3fcgoRRIu4XUDkQWEXwc38SI2j24VBit3W0sJscx6O6QiTcq-M0gcI-P9pWgMGzjKeHLohJmoEWQM2BzcW8TL8uys9MDvEWNreejGXnUTzJ-52Gmg2rZotgBUriKt-53y8Wq_ghC2JTFN6CEUyApbiRhUF3r8ffDNLvJ9Lg5brT-ntzL7KS2BcLvg6PAnk7FqqCFHX8UF61oKIFQACAyXHmHqUgH0F05wxVnfqXJiph3ryiumN8NaQrlDT35olURYIxfy9WZuXoKrT_BTX1ZOHcJgGStfLF-O3eEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=B9MDUn_TrkCuhy-Y9bB2i5jCrSlCTOyHcxDK0QTRatQdVoYk3fcgoRRIu4XUDkQWEXwc38SI2j24VBit3W0sJscx6O6QiTcq-M0gcI-P9pWgMGzjKeHLohJmoEWQM2BzcW8TL8uys9MDvEWNreejGXnUTzJ-52Gmg2rZotgBUriKt-53y8Wq_ghC2JTFN6CEUyApbiRhUF3r8ffDNLvJ9Lg5brT-ntzL7KS2BcLvg6PAnk7FqqCFHX8UF61oKIFQACAyXHmHqUgH0F05wxVnfqXJiph3ryiumN8NaQrlDT35olURYIxfy9WZuXoKrT_BTX1ZOHcJgGStfLF-O3eEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
این شما و این گرونترین خرید تاریخ باشگاه رئال مادرید: یان دیومانده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/102973" target="_blank">📅 13:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102972">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4YQ_GKZkijnrCoNTaTTcZBQa47JYOU-F714i_y7-xY6l5EB4LfCB5GFonpj8q6pRrbOgS0wGjWfuM194OTtl_VA14G47UTMad-N9MAua43KTRZw5NnIdIa1ehXPNQG0plEDZlXrSBhC2qobZeMl8N-U766Lgwav5BG98j2OLrrzeSqzG4xaGAJsWht4O0FrXqUR_uOwpGJaajKMdGA-F4aH-bSq4_95OoZVRGNRogL7xIAej3xEKYVn_U9KkbHqPF45KR3V6C3Cy3XxMifdmXIZA0-kKNqvv6bIPou_3UN3snf6nmKem_WPQyf6wCiVzF0xENk9SGayMycN4zxo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
تتوی گابریل ماگالایش از جام پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/102972" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102971">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWNRZow_fsA-IW4H6pjFzLHHXwQnuKMJS81MEDAh8WQNNL64_RmGkeFhSnIR3yjCk9jgl5d077NYR4bE4uQg0vVYaOntoNzWYvnUQq76zY-SFwBcnsyQ3tXv3bmA6i5N2mx16xqSGjDMgFBXF6UniDAGvSSRYrD1x7H95zkx2Vq1AnXkRxHmQy2oLIWhQbU4TBBKt3tEFfVzEGn734znUmrxrUYaew-xboWQ2Ktw_ivq6OkXKjiegjg8baJcYQ6w_Zd4BhkdIH1F918ZaukSbBBr30UTrZ5HUrRetvN3kG4oqCfK46AK-tgaK67cMgZdM5ZfnLt-WrRiUa5q9kCGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔵
دی‌مارتزیو:
اولین انتخاب مارسکا برای پر کردن جای رودری، انزو فرناندزه. سرمربی سیتی میخواد دوباره با هافبک آرژانتینی چلسی کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/102971" target="_blank">📅 13:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102970">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvjxk8gMvOyRH_q8ikdASt1k9C9HeQunytA9Efn40Gl3q1I5-utzsa8mlI3d8yrfM9eVlkeDK4unQfL1rdy20SMHbxrsRPDqvP9GYISsMPpwZG_0L2meRrLrgox5wvMZcIm_j91ISLPL-WgvvPUZ19v_AL5CzIiXKo_rmavC9Xtc6LPdMeqtrdwSbx2KBmOKZhxM1j2FewJ1humtjF07UCG2uLeSXDPYTx7LAMd64qDfrYoJyPuOYhOhtjRn07IzrQi6nP8x_t9vwtRRhdlyncKXug_-HD0o5eMTMjKvanCpURwhFYTmd_EiED9YWnZHAhAKKRg9Wqv0DadtPJBt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
بایندر سنگربان منچستریونایتد با عقد قراردادی قرضی راهی سلتاویگو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/102970" target="_blank">📅 13:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102969">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXcM-eXQI9GEDAeN2TJBr0HwG_IRxBHbFm61u_3zVkIgvZirpixMO_STE8t0dcvx2AXuZloU0xFTRaKrzklmQzcRjvSGmE824XFGjzHVPbjU46HtrDhbV6b9jpuPqnfz_ZR5L4LsAKtCR_dHEZvhX_rjsiDbeyf9dGvQ4tK9yJlpyMpT518XKZ5AhNmbmUBnIw8JXQlJJJzwm4xq298tyiMO0bH7pLefzWy2SRnlWpHuxjf7CU8aEPZgWF8s44pZ-PQNjcrBMJrypSbhJE8JYr6a47Vb194GAF3zceEyXsxRGKjC1HamPIXUYmhPgH2ScRPdvuTaJYxiw6xy4f5sbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇹🇷
🇪🇸
#فوووووری
از آلفردو مارتینز: مسابقات سوپرکاپ اسپانیا در هفته اول فوریه ۲۰۲۷ به میزبانی استانبول برگزار میشه و برخلاف دوره‌های قبل، این‌بار خبری از برگزاری مسابقات در عربستان نخواهد بود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/Futball180TV/102969" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102968">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/Futball180TV/102968" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102967">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIOwFq6jLMqx8xZkobvRG_GdEaCdcHkDkJiDj9rL2dr95yw_a_DIAkcXcIZpe-DXlxpyIZpB7ciWq31RLvcBg25gWVY2GqtQ3X5_FvmCq_Pf4RApP0e1l7JaZbpj1KlG2sbQ7oeyUQZ4J8fnyfATXKJMuuiPHkn42oKVIu4Bh4R5g-8SQkMOYratvkDccfjlPmitdwZ9ZTth7a0nSKowIsnluoEFzbQQMtEsrvvAe4pQLq2y0f6YqOalDPkLSz3rEMNqKrarWWJ7yOL1_yX99gJJuVYLOweaPK2LzrYbEVidbT3WgjmqCTDgqIviO1MbQjmx32n3xb9F-aFU1KLn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/Futball180TV/102967" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWNd9mSCIvtEZplcStHf0pyQPKaGjnZvVv8NAPBUuKt7plWtOptSa1-ZBqXYk5CeH9qPadQjmtlUWTmaYrFSB2hyTj0q4oj3motjUceL0jr1fOzezmAd80vFWS_3EfZL6rvqZgstR0o5JYubvZo_EPGQZixnrnBpuRkM_VyJv5741KAkwTLB4y84gHG9yOXDqeCjrVYkd1yp5e95Ju_dfSz5rCxqXQ-0oXQBYQO1vPMjnJWyqjwKuQL0AlWr9wDcS2851S9vVOfn5qA9YMdkeUzApC5k4jVxC0rj-64xh1Omz6kIZAvos5SDtNayvuu4vkpjqxIUmPiejmkp17ausg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXazBTkSSx9PxSCur3H5Vq9snEucFC2Rmnb3c8CbjKgWy4u9ZgZroAPfiG1R2C7mizWduclLxMlLZHpIgyKwFkpgbRRoAkGjfseQLEBP7tP4kSiPN-m4oABWfuc_WBkgx235Pkk-9W8fF-eKwuJ3IA8C-JREFSRYhaOhgdC7PrOWSys9JNHD5dEHrBnPvTtxuNFCmtZHEnOBnGwlseCI_4OGy2ghwv_l_nsWndNSwsQgBzgurEJbazb-8LN5L5elLFSqB6ZwUaq9kkFsK9Ydl_NOwyHPx_0wQTdJz2HkkK4fhIKN1Gzn_mEEENlbkDAY54W2nyOTLJ4zge-jFDxXYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الکلاسیکو فصل بعد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/102965" target="_blank">📅 12:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcmlqKSgo6u0yYwYEFoNMpTuShMv2WLK_6VL8GWG4QBDUvvaCP8jHTHA-7WZJ5TklrgIgKxKuE-UfXWp9mRJWNe7HPFydxHnnBGBlwoGj9vMOzNR6hTPCI6YEzks4oR4Fja2csMGcs0o768JvDDyrhsn99RROsaf2l3Sn3vDwnodBDv3A0vutLrRcvyn6UllGmjHMlZH4jBfC8ZVVDZQEabegTyhTo0YdivFKYNTynCMcNJuREXEkgwr1JwPGSLJDl2ELemA_9239m0NHmK-731j75oWo-woxtCEDVwpalBsJwXfMp_2_-Ki_ips_rgjJc5_iAQ2t0Mi5G61WDjMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxOqWSCGajvsXHgYuEnOTtnCyvskb0MuGGnO7lSw1NhJtWUqFo7RR7RbD9WFlaA_kppScJqNBQDRWNbhBZfx32zA2hKQN5lR-PTQOifx8CJ6Eeey04zz34dnBm3kTTwG-5ytSbw29Q6MljyO51ds70rQSxrf5pjFojykDQD28vzECDv5KJ_nvD0wVXKLQcE7QUjnnhZThI_g5t1ENNTIiMm7Su9cTUYUAkSNZjUjl5pjPh5iE0KZuMBvHlQUe7f3DHJcsUYsnqbOW6o3QusxtAm4VxZnAZ7RITmpQOrsk6wJds_PaHzPIAUYAfS3MR1NosXtvEUdmC801FlLaHGeqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
⚪️
تونی کروس:
اگه کریستیانو رونالدو هیچ‌وقت از رئال مادرید نمی‌رفت، پنج بار پشت سر هم قهرمان لیگ قهرمانان اروپا می‌شدیم. واقعا هیچ تیمی حریفمون نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/102963" target="_blank">📅 12:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74542a373d.mp4?token=NYNU9D4gsMjSaIOoJEzBVOuceAbdmXXTBCB0eLM4WsLjxqj1VvF05crO8OyTBIGYVsFsHS4PbBwdteJwrXGvCLzFYSVkRj41qeGyRY7Oo3Vtqe57FIhnpYCFazIZP9BJxborElQNfNU3KUmGW8dKCYjjApvHWHxy5vwE3Tl_lvP8V01WnI2gbP4cpCsuzcnycJ6Ghscoa9Dt5FPrOdkM8ASR952oGX4ASB3beqjDdz7UoNAxr6SXK7VF7KDxINtZPJ62OlXh69ca9v6AbPtQDBZmMUFIFX0jc2x3mxGr1BmhQOjeHGACORn4C6WG-oKUMEUtf-oTyJgUXQz4KfZELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74542a373d.mp4?token=NYNU9D4gsMjSaIOoJEzBVOuceAbdmXXTBCB0eLM4WsLjxqj1VvF05crO8OyTBIGYVsFsHS4PbBwdteJwrXGvCLzFYSVkRj41qeGyRY7Oo3Vtqe57FIhnpYCFazIZP9BJxborElQNfNU3KUmGW8dKCYjjApvHWHxy5vwE3Tl_lvP8V01WnI2gbP4cpCsuzcnycJ6Ghscoa9Dt5FPrOdkM8ASR952oGX4ASB3beqjDdz7UoNAxr6SXK7VF7KDxINtZPJ62OlXh69ca9v6AbPtQDBZmMUFIFX0jc2x3mxGr1BmhQOjeHGACORn4C6WG-oKUMEUtf-oTyJgUXQz4KfZELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دوتا سرباز روسیه‌ای با چوب تونستن پهپاد انتحاری اوکراین رو منهدم کنن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/102962" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZqaV5u9zu8OzRtdHo7AArEIOuWXsqTVreFbxauuVQZJkcqf-4h50H5Tq4nO7_iBzVwHtis4Ad5ywaiaHcx05t14nqlUm0qPiiL3a3RBAx0f77w6s9azFD-9ww4dLgU-wAw8mKBU2AysTge4pFzqYIv8kQo9fGXyiIFbIebVvzjxmGYZPO54LoWryg_VKP2gPzDW4bpzNuu3zZyS2X3ivAY1RuCZRJGzBoduBCkROvNygm1b_V43qLxDAEaCS_Fy08cYkQwCKYj67tbeMX7fCvt9xzNPuBlWT7JU1M9pwGCPnINng6Xa4SzmvRJx8N1cbGGouDQGyTSRM49y-UEbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت پاداش قهرمانی تو سری آ و پاداش صعود به لیگ برتر انگلیس.
💵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/102961" target="_blank">📅 12:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSoU-8JvDgNsUtJ_ML8VGcLB5so8v9Ln6BURvJfdrXNrxIQUsNyqvUNDAXhv1_mQaQ6MbkQOcG2jgUNyd6tmZCzEJX4AlMf98NgBDWVqBL0IBh5CdZogT1D-FLnCcWRHDvGBZhzQfLLBqw01Af9Ieyiq9YPe2lGD9yfyPzrvt1-3PdG28TMW8p31rnGVdfxTfa7fdzrdmKAlfk3cMn54xme3W8DG_M19dHi9AgzSAdUevBn1j0AP4H7Awz69gRtSEh-bcW0VZv5iDXEIljVEgEP0AgZJajinMpHN8MwT-vduPO5fXQEQxhBEOvbcZkDm7mIvlvmj6NcSogdPpJBTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار اگه تو فوتبال به جایی که حقش بود نرسید ولی زندگیو برده‌...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/102960" target="_blank">📅 12:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e300ebd1f.mp4?token=J8tHPWV2pCh-z7r83HtxOi_Bg4MA2nSGddpkH9oSB64Hkcl5GCa4EFEi9F0au6KNv82ESnXIvlZzrQyinbTJYck-wmVp9CThgfFkG9AUv0rcZUvUwi-0xSYA5YKoVmDeFDZG4NjK2oIps_C0iTaIOCTTpzZznU5aD1WKJ_sagw4CsKINorhPSv_Ffru1Q-VtPeXGtGR21xiUNwiuGnoymi05txC2lcIA8-QkMGkUV-7GYNgK3Av_r_qEa0NhAjKv78IIr55neSsHzJ3okoxNC-g0iEHeeMjorfWOghko5XV21KgAo45uRBJ3IAd7ZSZTWd2vh0pxgn5lXNu57wEroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e300ebd1f.mp4?token=J8tHPWV2pCh-z7r83HtxOi_Bg4MA2nSGddpkH9oSB64Hkcl5GCa4EFEi9F0au6KNv82ESnXIvlZzrQyinbTJYck-wmVp9CThgfFkG9AUv0rcZUvUwi-0xSYA5YKoVmDeFDZG4NjK2oIps_C0iTaIOCTTpzZznU5aD1WKJ_sagw4CsKINorhPSv_Ffru1Q-VtPeXGtGR21xiUNwiuGnoymi05txC2lcIA8-QkMGkUV-7GYNgK3Av_r_qEa0NhAjKv78IIr55neSsHzJ3okoxNC-g0iEHeeMjorfWOghko5XV21KgAo45uRBJ3IAd7ZSZTWd2vh0pxgn5lXNu57wEroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
👀
یک زن ۹۷ ساله بریتانیایی با ایستادن روی بال هواپیما، بار دیگر نام خود را در کتاب رکوردهای جهانی گینس ثبت کرد. بتی برومج که پیش از این نیز عنوان مسن‌ترین بال‌پیمای زن جهان را در اختیار داشت، با این اقدام شجاعانه موفق شد رکورد قبلی خود را ارتقا دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102959" target="_blank">📅 12:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de05a2b317.mp4?token=t9uqhDCX10HCi3JlCjUB80jTePEbsZKPf79ZTIeRUgIjtLQL6G-m_ybjgF-uSoyZ86aWpY3lnojbE19IyWXxU_omcPS6D7S8_cYjDrVcdt3D80jUC2IKTEew6VUe67fYDOKH9s8CJhAMF4zqyQ7gXZ6ekM0YODG-ZYF8f1d6ktopuH7PEjlNRBEnm-4q5WYtbZLPbALaDYZMoD5BQlKHWVxI_fZ4pLeOZCZALOpAZ0keSdoAZHU353KVGwz9m-fW-nuupWU_RlMK0qaHkobe8-u-TFuvEaniFTU6ytrz1EYv36Sf8ZEZSxBoMkjq4itJAVqYRtYW5_4mXn5eqvXMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de05a2b317.mp4?token=t9uqhDCX10HCi3JlCjUB80jTePEbsZKPf79ZTIeRUgIjtLQL6G-m_ybjgF-uSoyZ86aWpY3lnojbE19IyWXxU_omcPS6D7S8_cYjDrVcdt3D80jUC2IKTEew6VUe67fYDOKH9s8CJhAMF4zqyQ7gXZ6ekM0YODG-ZYF8f1d6ktopuH7PEjlNRBEnm-4q5WYtbZLPbALaDYZMoD5BQlKHWVxI_fZ4pLeOZCZALOpAZ0keSdoAZHU353KVGwz9m-fW-nuupWU_RlMK0qaHkobe8-u-TFuvEaniFTU6ytrz1EYv36Sf8ZEZSxBoMkjq4itJAVqYRtYW5_4mXn5eqvXMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇪🇸
بارساییا بهش Welcome بگن یا زوده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102958" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZLkEu0XgxogEOqQtm-Nguk1KzZq3bN3_PRTynqJimGkSBaU6El5ureJE5D_eFa7TKPAW2WIW-aaEMc9gn7gap6ahhHt3MWyV9RwPsoYpP7JzLlsosXIIjVjczXw_5qqPSQDx2SPZDQM7JTo_0LXCxfHSf_tWqn6HWlx7vUTLxU5hWWgOzqS-IhV3TfogwCzXCl1v0LUQKWD3ddln01V6IEyDOsMiJ3O0MkoVyhzx6V4EnxvSIOQ2Ce-t8itGd49_Rb4wNY854mdSf6aDHiUSDceWsukATCZr-eLKtHTW7nSbVyDCGMjHsu5-PFQn48Hn88Y5Y190bp3uILx5syRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUZcYRn7hCiktplYpcWNEqj5hhvFYUXT6G7ccCH9b2AxQYDF3v3RHPEP5KTmc7vr-A00BNMOHpYajCbOP2ZZa8ZO7knA_4O7NT7czVMmETy9rjepX5UUAoLVOPlA7FNoah1KwOP-qpTJ6XWfY-YLCyd25ii7KiPFTH7FS8Ll5UG8aLtIPTymQFVFkLfv5VGdADmD6r3ZrRw9ceCxg2FmpnCs5OU0ISGmyYaarE4O2da_HoFAvqi_DlBUp646eBFDYLt7oavUxdk1RCIFgwC9uy2pUt-m9eGrtYL4jpNvlihkCUPd2sjk0aAHl0vVf7VeTEcf1iCcJ-FEY9wphiSLzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
از کیت سوم و خوشگل میلان رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102956" target="_blank">📅 11:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102952">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHWAxygjn1NmAryKjbNOREmOHkZ798uQTx3vk7cXGaCslUTA5fp6GQisUOlKFXulMeZwYYshcJHBePdfVhmJLpNxVxlCUyO1Lltf1dNONEc4HHh8Aj53N-dRTboPpTNNixvdvkIw7qakPgaaxWGxVM0cSD7oeyLP31DADvTUU_QRvr-aaCkxPHE2q7XaOu-Lg_Y_0TB4Eh0maBv97suU29kt55zh04GcT5rVJTAlY6rpsNHm9R5vFLuAlmePuRGu6RltJF727t-oCQdKGz-FMRladvx7RI_VZU76pDrmaH_2OKEDLf3gAZ5gzYwKQMZUhiTDqvyyomWPdzYogN2f-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oROB_nlJ_vUCWLCunm9Xg3AaZUxtezJFCaJ0c_DKphLnZ6dBTO45Fz9pq5o18_ovD2av8cTtLvi-iELqm8Vd1xc9Yy-u23OF6b7c3fzgfDYS1-5aj5HRYUv3Cu7shvvBie1fJxrdQjmXXydLg12MbpxHcqLdPEIIlkU6gxIsxnSwhclhnFvLjxOTKuL9-OgiBewBebkGjRM9yT5Ls6QAHISyQxzkE22aXF9gitvk9IeEUqaDCzxgPWiBIt3CXOMZ5yrXuDDkjHEZA3F5u7oInEBDvrN-QtFaeD__grD_0gYhSK5ZrlTnkQH0LIYdkfExjwvd8WWJ_AnfD_WukQAiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuYEVpJ3n07y83NXJfe47s8cTQWquWija3As7suItLwAewFAWttmg8z0gjgcSzJhug881UTkbN3f1pgW6bJArCOqQR4i4DON4zvEdoxXeKs9Zd38eP-cadOujOdnbJMS1hIQ0zqdrRy2p9IMJZnrgbh2BGsZ-cXzWHPEoJ21tdsSLf8bRShpIiVKf3rtf7zr3778M-WC8olvG9wG-Sk1zw3wYkr0dEpIOYHBZASSBpMuvXq-TRmhPbbj4aiONPahRK1UA7W3Z4GPd-bzqRjMNaMwlPlesjyc4_m6QHsu72tpV6UIwftJWiDbQWOdH4KzL_6dEK-XnkGgmSP4imZTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USCUHjqwtvlefgwzP0WpK-dpvl6iwesm327r5IR8z8H04JrkIbRwU-KtHK4vhW-gaWMWerijZWsUm5PFXCcREHMnOV3reuheGm7rXifpnmDyZvYyjaKXlgnAHLXIuGZRxlxjW5airnnC21p85QMFMfeEG5K__qlXPyxLknIRsK11kCtKVpGbI4psRQvz-DUlg6406FGy5okfw_pxl_DMudDvtxlrj-XaMfBxCG6erWTW9ILHYgD6nNiqkJF9u6Tky_TY_BANE_h8HoYVH_wvXh-yQR7CUX876Uio_cKcPGBMetvcUcI2SpxB8xDOeoQA64_nUbnnbRk2k3kHbbzGxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
کیت سوم زیبای یوونتوس در فصل ۲۷-۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102952" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102951">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0147f7deb0.mp4?token=doPQVgaDPI9lECmp-V20bSKcm6MbOwsZ1HSTzQugn4y7w6oxWLQfXOcrVvSVYt_PZ3m5bFKhTEbnlo_PkcVlFKL9HntkkZf4aOvFBFdrup7j9HdDnkJiRRYNQbE-DtBO-PtLLD_0ST7-7rh1oyT6iqgPJwM3puRG7JGnTexavPHFwRSIri1FMlae7Ki-MLTvRSh_UHczvTX43N0X2zD3zmNkDC7Yf476MPmwwBDQvcQrnWCoyJ3QIXgr4-in48DRyvljaLLZuWgNezDSlVy1LczPPSqalyim2UHV4jlknELuf-P_sbh1a_YBD-E-rcax-Fs8EoVMqjqZffWbmp4anw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0147f7deb0.mp4?token=doPQVgaDPI9lECmp-V20bSKcm6MbOwsZ1HSTzQugn4y7w6oxWLQfXOcrVvSVYt_PZ3m5bFKhTEbnlo_PkcVlFKL9HntkkZf4aOvFBFdrup7j9HdDnkJiRRYNQbE-DtBO-PtLLD_0ST7-7rh1oyT6iqgPJwM3puRG7JGnTexavPHFwRSIri1FMlae7Ki-MLTvRSh_UHczvTX43N0X2zD3zmNkDC7Yf476MPmwwBDQvcQrnWCoyJ3QIXgr4-in48DRyvljaLLZuWgNezDSlVy1LczPPSqalyim2UHV4jlknELuf-P_sbh1a_YBD-E-rcax-Fs8EoVMqjqZffWbmp4anw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زیباترین گل‌های لیونل‌مسی‌که برنده پوشکاش نشدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102951" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102950">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897207ee53.mp4?token=Bb06jF62FVmRUr3DkcAPa7osHegxWIdanF1RBPWcGObgDvkQg05ElU2Eja-EuXAl9qCAorHCkaaaLTpzNZXB2NP43zF1gki676kic_M4rd6K4jGWxHpiEj5Ibg52r7iKk0TWBLOXOmZLc0WycQni1otL3Rtsh7XEP-cGCJctJcsxDf-RR9Aap7BoK4LpCbd_uIuUQ9bRKSuDbeo55mrvFm1gtjwM9A3T413_km5T0Ali14lgu-pTIWLf3lcjs9Lj74ZHBm70B1gwLhe-7XPU7HCnr_Ryy3bRZD37RVJYJYR91hhqUGYXR_fSLit0VyJtgfiFX9axOrb_P3wxm7peuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897207ee53.mp4?token=Bb06jF62FVmRUr3DkcAPa7osHegxWIdanF1RBPWcGObgDvkQg05ElU2Eja-EuXAl9qCAorHCkaaaLTpzNZXB2NP43zF1gki676kic_M4rd6K4jGWxHpiEj5Ibg52r7iKk0TWBLOXOmZLc0WycQni1otL3Rtsh7XEP-cGCJctJcsxDf-RR9Aap7BoK4LpCbd_uIuUQ9bRKSuDbeo55mrvFm1gtjwM9A3T413_km5T0Ali14lgu-pTIWLf3lcjs9Lj74ZHBm70B1gwLhe-7XPU7HCnr_Ryy3bRZD37RVJYJYR91hhqUGYXR_fSLit0VyJtgfiFX9axOrb_P3wxm7peuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
یک ورزشکار دبیرستانی در آمریکا در آخرین مانع مسابقه دوومیدانی زمین خورد اما سپس با یک حرکت شگفت‌انگیز به خط پایان رسید!
🤯
🏃‍♀️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102950" target="_blank">📅 11:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102949">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c054d35c9e.mp4?token=um5yPzPmpNWy2B-XkKzzeBRUeEhhFLX5TDCwIl6eKP810LxwbYyedO36yDR8n9uyMBgjGcZbiLDiJFHPHdPJvJxR0uV7XTtxqRH8Cf9h0MpDjR37q-nRfiLRsvYgV1nOr2ens5_lGHmKduezykM_y5wJJ16Ce6jE4HOFZPIVnyA2nXziZ3XSvFocNTK6Em5GXFPcbtkSAzFkakuQ2eIZPHw5FA18j2iVHiQ79ZfTzl91F9uhBOXy_fIicawTIYULZnDkBd1TnpopbHQ-9Xbxq6H0u0Yy5N7siW2Bdigin2NYY0Fo2dYpvRO6wrwpA9ABWRP8GbKGU-gfzvP93tx_mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c054d35c9e.mp4?token=um5yPzPmpNWy2B-XkKzzeBRUeEhhFLX5TDCwIl6eKP810LxwbYyedO36yDR8n9uyMBgjGcZbiLDiJFHPHdPJvJxR0uV7XTtxqRH8Cf9h0MpDjR37q-nRfiLRsvYgV1nOr2ens5_lGHmKduezykM_y5wJJ16Ce6jE4HOFZPIVnyA2nXziZ3XSvFocNTK6Em5GXFPcbtkSAzFkakuQ2eIZPHw5FA18j2iVHiQ79ZfTzl91F9uhBOXy_fIicawTIYULZnDkBd1TnpopbHQ-9Xbxq6H0u0Yy5N7siW2Bdigin2NYY0Fo2dYpvRO6wrwpA9ABWRP8GbKGU-gfzvP93tx_mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔝
▶️
عبدالله موحد کسی که واژه‌ی پهلوان بسیار برازنده‌ی او بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102949" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102948">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nj5eYo-r_khJrLuxUDLMpaekCbaq-t1NPR7m86YE_oPOryQ3iBjLj2B-6uGl9oVX5ioXv81eiiHfO1bB7VxkKxwHVtizemm8bmdHeUn7tySe8J_zHFKzKGY60-19WgGvp2b6Dqc3wBIOOBK1O3d33d3vZqw_6A23fuSrm1vqE-AbbJOe5Pqho7sCBvaUCQy77yP_k6S5LW1DrbQc2XFkIN88Ez4ql42zeDbf2QZ4jEA4LVhFx9Cb9_X_waNMReRqqsbn_O4-WZR7EBzt1JOgKZWODJmaxZ1enoQ0OD0ExPo-YPVg0BrBDSBrUEqy6vTdyjV_VwHSieTXTRNZSJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
قرارداد رودری با بارسلونا پس از توافق با شرایط شخصی تا سال 2030 اعتبار دارد.
دستمزد رودری 15 میلیون یورو خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102948" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102947">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f949a9e24.mp4?token=Y_RHBkj-zz-CpjEZ0FMJGd9-I52AEsN2S4-U_TUu_aNEKlPqcxeRiQKJp4BO29gBhbZUeiU4vvJfmtaLkkBoB6AiujKNz4whnD-J9J5l0byxUEzdPbzDqDTU2su2MNVihbsZr3Fw-l2DaM2AufDcbzVzkapMfFxS2dCB6jkrZTC57RSwHXdaUIUagM9PL9iV_odYYlMK2YsbEzTPP6UQ5qGPfSwf9dkmSCE3qpV5zhxE1lNEtbAvIU2-QguJt4HXZl-8EmMu7RTfViFZu-4hJTorangM2LuHP4iNMdywAf24i_CMbxqjLK3M01oD6n01I-46JXTw_6dXDvR1zCuS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f949a9e24.mp4?token=Y_RHBkj-zz-CpjEZ0FMJGd9-I52AEsN2S4-U_TUu_aNEKlPqcxeRiQKJp4BO29gBhbZUeiU4vvJfmtaLkkBoB6AiujKNz4whnD-J9J5l0byxUEzdPbzDqDTU2su2MNVihbsZr3Fw-l2DaM2AufDcbzVzkapMfFxS2dCB6jkrZTC57RSwHXdaUIUagM9PL9iV_odYYlMK2YsbEzTPP6UQ5qGPfSwf9dkmSCE3qpV5zhxE1lNEtbAvIU2-QguJt4HXZl-8EmMu7RTfViFZu-4hJTorangM2LuHP4iNMdywAf24i_CMbxqjLK3M01oD6n01I-46JXTw_6dXDvR1zCuS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات کیه‌لینی از طرز دفاع ایتالیایی
🇮🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102947" target="_blank">📅 10:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102946">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6a2b88eb.mp4?token=GgXq5v9fSxymS5aDJga4UeLh7FBwqONC8k5GQmJFAhZN8MMVEN8gymvR3Rex7DjELGOx0UJcEQwSRz4v4bXa1NjbALqyVbgUl3HG4RLPAjP2RQhUSXdrqnv14HWXwr_3SM535kXKMpb_w9wjDPr04ARyiV62J5ZnKceapw1gT8_hM-rT16OAOu2xrMR3YHzIrkhDJEuMd5B6zEjq_Eh8hlOI3iBul9ZXTJNtW18NWSY_H7Ynv50z5S5TnHLuFtN14LC3BS5tPDR5_QdWlFQjtE3ZrV3o4ODDKpYPEv1LN8kyr2EnEB7X7Xb-3PQrSDUoGk_CZTxr80Sw6YVX5g01Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6a2b88eb.mp4?token=GgXq5v9fSxymS5aDJga4UeLh7FBwqONC8k5GQmJFAhZN8MMVEN8gymvR3Rex7DjELGOx0UJcEQwSRz4v4bXa1NjbALqyVbgUl3HG4RLPAjP2RQhUSXdrqnv14HWXwr_3SM535kXKMpb_w9wjDPr04ARyiV62J5ZnKceapw1gT8_hM-rT16OAOu2xrMR3YHzIrkhDJEuMd5B6zEjq_Eh8hlOI3iBul9ZXTJNtW18NWSY_H7Ynv50z5S5TnHLuFtN14LC3BS5tPDR5_QdWlFQjtE3ZrV3o4ODDKpYPEv1LN8kyr2EnEB7X7Xb-3PQrSDUoGk_CZTxr80Sw6YVX5g01Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
جوری که رودری تیم جدیدشو انتخاب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102946" target="_blank">📅 09:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102945">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdea72d125.mp4?token=s6AwGHlX1ZQnNucich3QFPyc5Hy15qU4-gKO8NjAlVRjeOlgegt6Dmu0ofSWyZcYBLt-2zeEjUxNWhRW5o0dUkGEKCd6pn6zSSLmRqKRnxK29Xo6xnjqH2a9qKm_TnoucYPd8YRKr5xQHphRTXQ1kKz3TzjI7qG25aVHoTyqt7GNfNbsioQ71jpaCUrAkKHQs2Qv2u22uROfzVTXzCYMF-2nasxyhfsaazcLg-9dLvijlQl6kMQosWhxndsx4qyztudAIaMFMSnWAuecZ1lovR40WrSfeaGtLT8tdDJpMI694ddbjrFZ62ogLjODPS_vsHS7tO1MqNm1XoDn-YyeWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdea72d125.mp4?token=s6AwGHlX1ZQnNucich3QFPyc5Hy15qU4-gKO8NjAlVRjeOlgegt6Dmu0ofSWyZcYBLt-2zeEjUxNWhRW5o0dUkGEKCd6pn6zSSLmRqKRnxK29Xo6xnjqH2a9qKm_TnoucYPd8YRKr5xQHphRTXQ1kKz3TzjI7qG25aVHoTyqt7GNfNbsioQ71jpaCUrAkKHQs2Qv2u22uROfzVTXzCYMF-2nasxyhfsaazcLg-9dLvijlQl6kMQosWhxndsx4qyztudAIaMFMSnWAuecZ1lovR40WrSfeaGtLT8tdDJpMI694ddbjrFZ62ogLjODPS_vsHS7tO1MqNm1XoDn-YyeWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بهترين آسيايى تاريخ فوتبال؟
👀
يكى از آندرريتد ترين بازيكنايي كه ديدم. با اين که هميشه تاتنهام رو دوست داشتم ولى سون و حتى كين حيف شدن و اون طوری كه بايد ديده نشدن
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102945" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102944">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCAjK_4DkY39ayJyiq8vgzWIAzbcuQdtfCwPnt4qxsMBOeSGGYGAa-yk4cwFBdl5bw4uvnLdXoL6GloRbHKfpKQJRamlF_6trnl6HCl7oXlfK5UqAoUl6Z3Wz8RcbfZtXY_K2SWEwMYbo2paonwGKLRnWUISM-JrVhlERqg5Tbhaqzczr3cFw2QJP4i_q1Gz7P_49egtyBd8oMSPcn97HibigOnlFRfTf7vXdSiPrF-kW1ymaSzYdFiUOKyMoCVIm_H4zSGHzWjwT-aE9h952KRPtjZNH--RQLbpHI9dEvu7gLW0DZSCSh1OXqlFX5UUzjcAJfdlW4cSADu6tcjVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پله اسطوره برزیل، در 4 بازی بجای دروازه بان بازی کرد. تو اون سالها اگه گلر مصدوم یا اخراج می‌شد اجازه تعویض داده نمیشد و یه بازیکن تو زمین باید جاشو می‌گرفت. این اتفاق چهار بار برای اسطوره فقید برزیلی ها افتاد و تو هیچ بازی گل نخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102944" target="_blank">📅 09:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102943">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab63e40e3.mp4?token=ih2leyCxvu9Mg162mntY_p4uejgKMUNbpN0VQGsoiUH51F8iC7LWPgMIxhOTt__V4Agc6-_cf7V7HoSHrisPXTmxh1uxseuUsmOFUAMNRDnWEwwvjFP6A1nJ-RyAxZGAzB9h_bKw1rPgZfhKyLIFOV5CuHemBw5WR0bDc__oQIbdpFPt8Z2Ap0Un21_kXB3YW3XLqza9cSTePTqBl4xbe3Tq8foaq0ED6d7x7FPQG4ysStY45CiCxK2BMqWMrbOmeGGhEzM3h_t0enkTOuLfWCbZA48tDNrmwmIu2W-JbeTsCRAcD5bCxwz2e5R3KdtCWdWdsKdbpPUuQCCqmH-j9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab63e40e3.mp4?token=ih2leyCxvu9Mg162mntY_p4uejgKMUNbpN0VQGsoiUH51F8iC7LWPgMIxhOTt__V4Agc6-_cf7V7HoSHrisPXTmxh1uxseuUsmOFUAMNRDnWEwwvjFP6A1nJ-RyAxZGAzB9h_bKw1rPgZfhKyLIFOV5CuHemBw5WR0bDc__oQIbdpFPt8Z2Ap0Un21_kXB3YW3XLqza9cSTePTqBl4xbe3Tq8foaq0ED6d7x7FPQG4ysStY45CiCxK2BMqWMrbOmeGGhEzM3h_t0enkTOuLfWCbZA48tDNrmwmIu2W-JbeTsCRAcD5bCxwz2e5R3KdtCWdWdsKdbpPUuQCCqmH-j9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🇹🇷
محمد صلاح در مراسم معارفه امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102943" target="_blank">📅 02:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102942">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPRkTbraFsaRFYXZdbvy__qHHzQbwnelnBwhgaJODvUPNP8nTZ0pQqQSdsIDQ_Qc6S_NeKRhKvSU7wPR7Vd0Ffq1UZbzzjbavbGN3oNjUljWOktireUhOBNdsLc-udmPGNDqlqGNZaiKVtJZ3M3opnGD_YSatcgIFtBmkJRYPSTxb2Svb04HbX-mDK-qgQamroEz5liOLXGGm6DEq4aeCWqxcq86o4jHPeDN1TR0CyUibN7x9rBi34_tKaMl-516XvnF2t5UaCVijXWAgB2UCRcTXJAtyXK9Lrdo_6_Ldw1EicP3x1Mao8T4BSdDppXxsASq8UVISztcsOgle5L_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
فوووووری از فابریزیو رومانو: توافق بین رودری و باشگاه بارسلونا بر سر شرایط شخصی صورت گرفت. مذاکرات بین بارسلونا و منچسترسیتی به زودی آغاز خواهد شد تا این انتقال در سریع‌ترین زمان ممکن نهایی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102942" target="_blank">📅 02:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrhZ-gGmp78K6idw6rg3RhotveJ0_gu6Q79oy5Z1Pm6iX7J4p_FbbpSQB_tGxCC_RugojykIXne3SQRCkHkm6GzzbUni1naZKWBfnPBWiLtoDcEpu8txcpu8eC2P_4dZBD8saIn_utXaje11JWLcw7q-oT3IdJtsfaDCyolY71odKkWDCBe0iB7b_Ul0SYaDjWcC7sdK_9H_x7gGQWlAY5-30hxMHTAAQyIVyCKa1LtiPWVdCwDUh_Nr9KkEd_YMNRr3aVW5h_qtTNzaW7R65Wjll-6okMFEAP2Rp8Waj5CSubynwdGAcEn7p1VWCUTAh02HTp-f4VZmByiY1aB61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
⚽️
رومانو: ناپولی بدنبال عقد قرارداد با گابریل ژسوس هست اما آرسنال این بازیکن رو قرضی نمیده و میخواد با دریافت پول به صورت قطعی بفروشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102941" target="_blank">📅 01:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102940">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d0e59f4a.mp4?token=F7-uQzlf2arSDR7bFarlMh-n01ZR3JNnfX_w4nj-tOWL25-bNbTKHYAdMUmDf9z7wVeZtzG-8OYySODn5HTfrY7g3h2-9LRXdCGwzZPkQ_JbZi8YjKIoIrlFPG7pqb5YSQNShb8Oy3Sa969MRF5pooMo6Cs_GZX1k2zlBfPse7Xt6kC3L747X7jwh-Br1RKQh6KwG6IHVdHHQA5omOlBTW8TscFLlg7Vm8lpEeF3TzdRQw_tRMeSuX0lz40-nHJilNW8p2pbdEhCFITtmrhpuAS9kgfDJw-nJI1N3CH6BGNs0vdzZNR37l1ruD4DnfNRfxsBXZ3a2r7FUw-uAfEqww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d0e59f4a.mp4?token=F7-uQzlf2arSDR7bFarlMh-n01ZR3JNnfX_w4nj-tOWL25-bNbTKHYAdMUmDf9z7wVeZtzG-8OYySODn5HTfrY7g3h2-9LRXdCGwzZPkQ_JbZi8YjKIoIrlFPG7pqb5YSQNShb8Oy3Sa969MRF5pooMo6Cs_GZX1k2zlBfPse7Xt6kC3L747X7jwh-Br1RKQh6KwG6IHVdHHQA5omOlBTW8TscFLlg7Vm8lpEeF3TzdRQw_tRMeSuX0lz40-nHJilNW8p2pbdEhCFITtmrhpuAS9kgfDJw-nJI1N3CH6BGNs0vdzZNR37l1ruD4DnfNRfxsBXZ3a2r7FUw-uAfEqww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کل‌کل پرزیدنت پزشکیان و مجری برنامه :)
پزشکیان:ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟ :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102940" target="_blank">📅 01:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102939">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22707bce2.mp4?token=EJvLz6azUOpOZrvUUJgSvtKM6zYWJwdOMMwZ_06J11cH1sGgF8A-7JrGLujlsMBcRsr5RxIEf0P9Ew66S8N9_qk7ci61Hj241YPpeCMB93yErXJguS97R36LBRY5dV7w8vl7PYz1kJWn5UTO5GHVcK5sNY1nhm5xwlCa5JylAYpEvQOlzOR5EwNNQ2GyFIJtn7DsIa3SRFZSpBxhUg4ut5n-v7cLab3fBsx4OcY7boC7_eLwCbB8qiNFR-77_cN-OOaVb5OjC4qBCG3-fwCUayvBOHG_sYqwsPD2L5bfUfIW1sz2oN9OJbVKYnFd5jj-E6wiH0c0d4QIE-74ihSTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22707bce2.mp4?token=EJvLz6azUOpOZrvUUJgSvtKM6zYWJwdOMMwZ_06J11cH1sGgF8A-7JrGLujlsMBcRsr5RxIEf0P9Ew66S8N9_qk7ci61Hj241YPpeCMB93yErXJguS97R36LBRY5dV7w8vl7PYz1kJWn5UTO5GHVcK5sNY1nhm5xwlCa5JylAYpEvQOlzOR5EwNNQ2GyFIJtn7DsIa3SRFZSpBxhUg4ut5n-v7cLab3fBsx4OcY7boC7_eLwCbB8qiNFR-77_cN-OOaVb5OjC4qBCG3-fwCUayvBOHG_sYqwsPD2L5bfUfIW1sz2oN9OJbVKYnFd5jj-E6wiH0c0d4QIE-74ihSTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
جو پرشور هواداران فیورنتینا در استقبال از ماستانتانو ستاره جدید این‌تیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102939" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra @Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102938" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjZzkkUxqpYu3FfhzWxF6nMWzVOSAnr6zr8VfPIxZa33xYX4gwFlggrRiSO0u0P-9eJzNsgxbW-rQsuCYT4OBIuGj8vXLwtmLqcdMZPp3DsftJzFG2gmLLYZZQfFEz5VDvE3Bqk034kmPomk258nbM8kHeu9SAwx1gbI0tosFakPDKiXqteucA_DcFtZ6C08mc-etiHtuljJzvDqgQK4TN-t2_t26OIZSifHynvTXJFZMoZCoFZIp4nbXdZghTkXdhYNP4fvS7KCOZrhLqZo7SolKaSsHr2oMRqCQpw2VRfUOl4qVjzxtAEG93i1XjIia9Md_L5wO473tGsqokMUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra
@Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102937" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UraRbGbS6d3BRTXghYGys9Cq8xNyyM1cjlVCYwWt_cdA23plwJLirRReIjQFRu4KBRfmnvNWgsoel1AQN0q_hrpciF3RKqSL_Xscr2RYK_fNv-cksWDz5MDeSKgIOmJ1qBLEj6cPe5zpJ6P3fmS30GGzMl_DXsHwskz7oUytjakgwV03XMdT3TenF0BdGbi83wSfXnSp6Y4I53y3ip18UywmfguYSrOv74WPco_bH7Co8uWSRMnMf7HQaXWN8n6QTM0UIkA7F124d5pvBKLhfoVKu7tZOJPbthYVVonOVXhL1axcXsVWipPg0UdelVhN9zd1p0xqpeNUDKoN-WJXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
پپ چاواریا از رایو وایکانو به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102936" target="_blank">📅 00:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TombMm5dysHl3AjF3VxqS8tppv7WU0adaI8WClhZczF3lURybUBF9EzWESbtTW2_ujywdH8nYoH03lGdM1UsWTBcccgLQ0IK_N9iu7kQcc_Vh6mGPT0J_uFw6sM_XVRxbvoxP1r5HtyLkUx-MckdPrRQwCMaUSkIiRHCHz98kZXykR7mcZPiR_AF0Kmlck5q56dkW1lDPGNp7DXhs5GlA0ozpButIDKr3IzVaOeOqk2vtIFnqJ3gcmt1EOFOmglqHIJTe0aW72MCpgSMGXYQ16F2TpPQtMCJyXcYtXuwrvNz9CrWjRC0xBQYXcSHA9qr4xzno-sWJICIuGuzaz7Syg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
📰
فابریزیو رومانو:
🔺
رئال مادرید هفته پیش اوکی داده بود که حاضره ۵۰ میلیون یورو واسه رودری بده، اما سیگنال‌هایی که الان از سمت رئال میاد نشون می‌ده اونا رودری رو دیگه دور از دسترس می‌بینن! چون رودری چراغ سبز رو به بارسلونا داده، برای اولين بار درها رو به روی بارسا باز کرده و حتی با هانسی فلیک و دکو حرف زده. دکو داره سخت تلاش می‌کنه تا این انتقال جفت‌وجور بشه و الان همه‌چی آماده‌ست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102935" target="_blank">📅 00:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZspS7QNSL-bkDmwHvQLg7_64vrKqt2nx59jdRqC9FJ_DYRgY75BPwJc8HgvZlXAR6M4mwzheooa3T13aC013cI6oLj-MZjSE7DBGEYsKx-UliC2hsl2Pm8RCZhkmgq_elr2AT54K7LYH4SIA1PaO5BU7FlcTS2zYkKZ4Ji4KiqNYR007OYTluVuNpIiL3deItjBJUUHxIrvxzlB7DyS1-sYQk34_4iwU-YBiAZo1dVB8aJ0pw_9KOemlgaGXdLGG8CsrXFr1gFN6ugb4zXN_NDlA_Ib6aH8WIav2MJSJM4OhnhvhPFZShD-9IQ6BqrIk_Xhi9B5Ndbq8SVLcWBHePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ورونیکا بروناتی: کریستین رومرو ستاره خط‌دفاع آرژانتین در آستانه توافق و حضور در اتلتیکومادرید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102934" target="_blank">📅 00:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxZpzh7MMsbEkdkfOofuSbRGPlOC8zb0DS3pz11P71bCC767oiDNmZase0_-SRCCQfX9HfUmsYOmHuL_MRgK1OIMa6KtHaaUqoPH2QdPq2admgH5yoKI6i6LLAqeqORl3UEi-9tNkGUJgXi6_nVGdEmrLgRTSzzhatbHhcpEfTkiG8oicj4XA890aOmTOzDXzqrmoBQk73pwCvb47afxLhCdqg2AZbHoNGX326yJP5hqLshuJzca1oePVR7GJ-2vGyF0lL8BLtLtdAh1kVRo3bA3rVYEZIVMKd-CfGdi6W0u0hlvxeD0dtxG-2eCIG-EX15tAbfws_aRYhQg62ofFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
گاستون‌ایدول خبرنگار مطرح آرژانتین: آلوارز هفته‌آینده به تمرینات اتلتیکو برمیگرده و خبری از اعتصاب نیست. اتلتیکو هرگز این بازیکن رو برای فروش نمیذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102933" target="_blank">📅 00:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102932">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/Futball180TV/102932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102932" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102931">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd4yrJjgCkjLUGJqbxOwPC01EvhODHXMPRGPpNmUctyWSDeFoER3edpn1EIb3PKvwL0dhZWO00MjVMal7ojTZntDtPx45Ieiw3kF5SA8TOS0VqrGQ5rRaj8xda-afAc7vUjN99zhPZfPVp4Kr_oP0K6ABzkwH6xPr_OH5tYi_exfho-Wa8jOAmKiBo5cl_k_Cq0NIXpIl4GBCA9BI4dBBja0bFyZ7LTqPd_3K8O-n2Mc2yawhdx6Qcx9BqEHxd8c8OPjwZ7Vby0tCkLRkng55vKAiXFtoKDr-RUIs_NNiQowxUWl9mNZBBT3S-q6I1tZiF_q3Zgjg0MwJShkYhOvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a15
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102931" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuN-r57rS6l56s0m4c1Ew9njiKGy_jutiA635qo4IToz8I_64sBKh-vkNNAvjegF9l3kDdnSBbYnANXJG928UEEPkVqd9luqc-JFzkNhAkTP2Xe7KkC4CY0F197eA5Cj9iuAqYC5_fIQST9tlurhzs8UpQwS6OfNivtQtSf9v1RiXD2lXHrRDb_Xepe8IpVBwxhSEgT6oD9l3BEOsv4gUPZOKWdt01EkVsSrFff6nc-Er1F0NHkSQtJD7JUtIUM3T_GEesKv7IluKtt8Hi_g6e4VM2n8j4bC5-VhMuxX3aWChB42epZ9ro4m_Vd8RCHBTfjeL3jwaoJvJv6M2jwxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
باشگاه هایی که بیشترین هزینه رو تو فصل 2026/27 داشتن؛ طبق معمول چلسی در صدر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102930" target="_blank">📅 23:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTUDAFLkZMY-PNBfJMsE4rY5ygiXLqOPxERn9OgfImKRQBejPH9sJud1fGdP6H1lmZkQJUG8l6ZFe8l5kf9uI7nHtkrz0mKz8JQz3_g0sGaBMgZlGCvuMT22m0MEEEDRzzOMjLNTQm5OzNMIh5PNyT6m3U2OgE0ACVAJI0OprmLatExJ_0VJt_8jEEEg6De9SH2dkRRNbuDjI-z2HW9hnCytXMVP6XdxAGGO7djf_s7M0Yw61KH2rqnTLTUfSI9MaBpGqKnQ9dx1AoVMoHp_Ml8ft1ujYxTULgYhbkeUY3Nr4IFsi3vXwKWcaUPmdcvAPS5Uoo-SEdMfsixhz5C4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ال ناسیونال: تیاگو مسی از همین نوامبر به لاماسیا اضافه میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102929" target="_blank">📅 23:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzKyYcFS-ydQODAJCDHFsXnChlpokBCAjjfJp6tdTvogZj50NOU9L47thPDo0lZfbjKENg5h8wCsFsql0XzeeHoPc27EtdyeDydNmliZm57G0nZbjYTGlR5rWTQQWTS4dANmQvTI2tVX2ulXUEUFopVlEG48bZRhsSzFD_AqFLsiGmvhk1GO164zeb_UZxN1KyJDbxKtfXvJH4SS7G3nWfwmvOh5K-8BdvMak_ksQnOH0Br3tTmY4aoAWTYWI88469l1ABg3CjeNXdb3MSgq8bpc8KZgWQ5iRG3_cvtH-fCSWFOwhn4W6das5oeS1nJFea170hJQtZqlgo2JdfNGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف تو آرایشگاه داره موهاشو کوتاه میکنه بعد جرارد رومرو بنگی زنگ زده ازش در مورد رودری سوال میپرسه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102928" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102927">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqu9wJui-jZlYChx1QnCSA9E8BiLvbNCRgaS-Y3vM51zaD8KPmcQZH2XNjhZJaza4kXpqrt8IOT19UIw533kBpRGHa9e_LNsAD5S5fhujXxoBdl0Gmn6eYgqd__kI6sHbs9xtg-SXgcM3e9K1yfNqHuBVIgy-Aex2uzTaTUQIdFxP_YrajE-pxDVGwpj4wFUv8hI0XXWeL0st-g_qCdhLgQx2sjoFCWUuNAjBGC8OsqCmbhoyzkmUfCsIrzAWoH3Ptw58SY97Ya6kEhbWuUUidbE_I34Ecl44cgbWmWxrg-inZgfwGeEhcH9OTAiIncUP7S1_x6ILEfhN6viuo41lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
فابینیو رسما از الاتحاد عربستان جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102927" target="_blank">📅 22:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgRIZlLRsbCsL5dUMNzuA8tqZvBe7necRREKC2uGbxf2BVdWzGDTWUvDEb1Kp_UivNlpgyuHbrfJdFExNM5MpYTDWHRuatLqE_QuVnV5jZvYA23DBONmbIvQyCeel-2CxItN9gq4Uu4XPOuSpWYjbzQa23HCvcDzlicP5WSbhc3e4Ss5iY_PuTZevTxUI0dxuPavPSHcehJ9k9g9jXhqb-Q0aw6OTjalrt5C6ykxT2M5pX8QmF50IM1A1OV2sd4p8noFEpOY5eDBxnnsWRpNS4EKF0I1o8a_fmbFPl1Kp1kRwqkO7igddicZ2E-r_tZGcQE1vwkXLXpRcZF76C54eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات از تمرینات امروز ترابزون اسپور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102926" target="_blank">📅 22:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn_isL8fIEQm262Nc1W7ZIdKnupJgCvk7rnsBo3Np8-KXk43IPxiv9zWjs5iZqASEbYn4VlLbLAo10bp9JezTe5xhF6wxoCBwZpG4xIxllae3LH0JDmB4tptM29aNrajBoLwQdGFEqurA-4GdBVtw-cn6KjMVvWx79rL4fnxh-AE1yCKNK-Xais0ttwF5dke_1s6aCb-kybgj6ux69jUu51dcIDGrOrmsSFC4GxH5tG_WqrQUvmQggr1T70yyIXOnJqZNJYNG-omCax0ESwWMLz9l6JQ88yFK7FqDSHwJwLPINEiqTWgaDgEQ70Nt25Ey5IbDgIgQa-I2wGMa9fH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
‼️
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102925" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102924">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElGPrDtsJ6CdnUWBEf-ueNFelaUMIwdetDaYgALIe4LljUYjOEP907nlclr0IcW9nP0K2WDQ-5HrVi3cmDXogimiFfFRxBprG7lG-zSMTunjYPL_ruS3GwliRMwf7FpQDd9aHqL8qKJHh_QC3_KPC7ncYwX4UUPya391mjKzc8jHfxvrVnTbfJOCTA9XBV2Gni-tHe9Z3n0wX4cWQzUswk3z7WGCOOKW6rzlCvsE-OiE5c4iriUhVLDZB5F2g5Dl71CfdI7oUO1aCghj4i7zPk8OBzcZtptPT6f_NZ8ZyjqvE0YKsJNvFoFRP3V4ucMZsXddeOzvOiOrchVfqxVgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
شاهکار رئال مادرید تو این تابستون
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102924" target="_blank">📅 21:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102923">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJH7l5VgW_voiNR7sRPx39lpMr1FjNtkuQNHw8DQb56srPOU-Dosx0wH0GyKtQ-S2pOSLWONfn2Dj4lg5kQGyC5X9PRr0blmL2GEjArqAMozN9ltXVt6XaHVk8H2u3OUCRenuZnPGn5cG58DDBJFlRLtapfBcvKRgkGacyoY6ZF1813n5Mu_43Cdrr4oCpUjaewbNKIX3RUzYSdwNCIKiY8fK0kTtMA0Dzfq9hLaFypOfg93CGpGcBz0J464C-LHHPKg4-O2tKW1bf4FFBmI31m9C_8BOs2YAI9Wala53N9_0VT5oJaRiUTMmGwtnJnW2R2AJGLdDAyvKUV4tEL3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
تیم‌فوتبال استقلال در آخرین بازی پیش‌فصل خود با دبل سحرخیزان و تک‌گل آسانی مقابل استقلال خوزستان به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102923" target="_blank">📅 20:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzTWcSjlhsTJfnT55oUjb9WLU6nMF8o2EKz9SpfIiuSw0F0jWEJekFFlY4XayJzVcViGeMIvjKqiSRNbEtQwvOz9VLS2pYnNVeSRm69cgTpmwbgrMPyCGBaWW4De_nVrMdtXSPOxkFUxMa0q6t8Yos2XmZqxTRYZJzOc21c49FPTK2_rfZ7rdoEhlQxxGuvKIWbwySFoSm7V-5uxIi48gN80UKsWBVC7tExmhACeE2en7NXvYODRFeXZO2zYvU0qu35wYIXjkr9a1yoGTzCqLLaDgmiU6MZx3bWpwFB074gTO1Dw02KntAQbhuGOAB7s5uzb328Jk9pDLmM0FDV_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از رومانو: وینیسیوس جونیور رسما تا 2032 با رئال مادرید تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102921" target="_blank">📅 20:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUY9zKiF0NUcL9gZpX0ZALKtaX-3x13S31LqoBCSaIKRI1t6AygYN1x6fIBlpXJfkdrhogtUetmEgHLPJztMD6wKm6DlMTDaJaH_b-M-mOAqJlwzF4bSbMF3F8lslcp8PrXyoS4VdORneAB2j5BgHCvcQIvvnvG5ur8ZHAul12YYhNOknDZMimftSLMdGM5hGeTdiXu2Fq5ijR-fMFJ5DICMNVJNAcRajy4aXL3Yx918hZjWyGgryfub6l110GxaPe4TWyvYxWBX18RMCKBf0fkBZm5CeKLibJuChFb6Qi-PqwrFrjmlI8fz0_YCGo8hgMsZvaZhfh-r3v0LETLFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووری
و
#رسمیییییی
؛ مگنوس آکلیوش با عقد قراردادی از موناکو به پاری‌سن‌ژرمن پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102920" target="_blank">📅 20:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102919">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUGyFXWTnoib3CxV_b0vB5VpcQuTWdR4MzT0rM5osrM-wGeoJ14xzs8lYkjLnBxfo0nprrrB93i5mpwGOSUJjNCgKvWnqWHk72VzwCKBTEGeOw5p-DtlV8M9BNNbitKOZ_2DqsM1TkkESXjUWHiZj9fc9c2I36n8gia_tgZDMQhtS1zwH_xeoiAxu59N4EfweBYvyu8UPZ3xh0Qdk4vP13OQ1_Lq-ZIyfSiLYZRbAR5OegzLbZT3KHeQ7aFGvLimyGYOk7K1Q3URo_hHKKlzcBeuRRTbBDA_mEBgwp3MRMyhjdfN89yEFBPsJcn2SRk60pN0QAGY7WGaE7u4NIzGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👀
🤯
خط‌‌هافبک فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102919" target="_blank">📅 20:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102918">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0j0Oh-DSNJS70QUDOxZllK0dD8Ajn1W2UW_otblRkr8yt2aoF3psW2knQnJ4PDKmRiJ0lOBZfIammfwRqv6qaKQY1GZk7vRgOnE-0FCWa3O0GkEgWG_igSmAlw5jdv7qmF5-1x71MrjKyHhyxheYSSzBRRpiJj8YiUtzVRcMogr6Rgzs9e-koDBHq11MhlC6vFnd0a1VRJGO6WqBs8YJ6cFvVT2H4k9NvfKlI9-Wmi6MHAc07D5Vkx44hrNaXRjRig5G-TGWrzPmnuHhfSctGJEupE9rqfgh1wHH8TSUPWF_VazYSnx9Go43Nxu6kfbrndcRdrsC6eNjI6UgaAJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت یعنی ساپینتو که تو ۱ سال از سرمربیگری عارف غلامی رسیده به سرمربیگری داوید لوئیز
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102918" target="_blank">📅 20:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102917">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnVp4dNcWnS8mI0m_b7WEvb3lSRmOUCWo24exAAizBA6fyISoIS-2jcZldLuEQmEA9dVd3XXUjpRobeEXtNSFuoLtlOuZoGQBGkZoZReQu5Nq3Kuff_XzZBbTMSdTxsa2DAn7kz9QUcuzcGV6aH39mQ6VTNcY_gYPtwdvQYJ_ORPWdmqCOdI2-KkWQQEyq69nuVjm65lzuYkSmdiNxkugWNsQLMpX_DgUnjofutN-DBcrqdmLKU-u0uFhmtbje3AAbdn5B8uhmUvSsxG-GRoHY4p9H_wh2qKWdJg9RuPMTE2KbvJBoEGunRivVvRs0AF5uvd1mPysd4Gv-Nc2qagjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
‼️
هافبک های فعلی اسکواد رئال مادرید؛ عملا چند تاشون فقط لیستو پر کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102917" target="_blank">📅 20:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102916">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iramPcjY-a6t_kN0Sa8DTjmJL_Dju6WqApnigXRPHwS_NzCHAb_DzWi0F3LTvZKSPtsibs48meOv2vuK_9ISxcvrur0CNs8LnrfnrZoeufEeRtW1MxEab27qMoe_UTyGGliBPKI6KaZcUe1Cm6ZFF4UoY5WYMoVcEdDY820WTj7beRE3GuL9QkNb5IpucjNDSVhLVb0WxXnODjNO_CN8pyJ8E8h3FjHdiQfz3taXhllQTpoG1VnGF8CE-UOkO7IY2grx6c6GTy43V-M9TMtOd-NTyTNLucvAsdNmZIZIDJJk4Ln9q-E-7w69bDIQokRonnMqaxCzt6R5vc3gJbosgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
خوزه‌فلیکس‌دیاز:
🔺
🇪🇸
قرارداد رودری با بارسلونا به مدت ۴ فصل و با دستمزد ۳۰ میلیون یورویی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102916" target="_blank">📅 19:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102915">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhV_xAeKw0cpL21fYTQVm_FDvz6KrSXbEyHXhcXKqE5fdbixBrc1ooHjwoLtZOnz5a0Ywc6Z_55kV-J4aAh2zpD1x3h3n0TCj0s57ZGN-tXSioPI8pI9CDQKWP2bTaC2hsBERHYCbwDE2GcSqywJ1-wrNvvxJkwbkG9tfz6VH7VQZSIc4WBc-Feglqh9oobOkYL8TzsQsnWttMz_f-Nx7-es4WKTHHF_XIMiInpqGTGmCWu_1fdmmZFsn1LYdBmDzeP7HMAz0JJTFYHT_YpjlIPnr99bHDfShwY--kH_E1Fl5Z_QAsF3lUX_lpZCSxI51HNGL0Uf4Myqo6zWWR6sDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دافید ایبانز: آلوارز هفته دیگه با سیمئونه جلسه میذاره تا رسماً بهش بگه که میخواد از تیم بره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102915" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102914">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVvTUVIvG87pDhFU_ln9MCJdgUuFH_IfarIdcyZvRL4d8pLKYTZqEK9BswV0VFNlC8T9RWx9fEVHBHsyEuLJ2ORvTIbNZTFwa0qQHa-ZWkAxbPcVmWIyvjwdDtnjNv269Z2y02Reyon6XSrQyzHi3kfwvmOxz__mPzsVCo2YZ5Rhd0yuuTSyVRvnPm7SpsztriCrUb-1bOdgxuUdTf6p8SWSyalu0tVVGv4Op6-35uuEmiZYXQap8KtcB7hgmNWy9I3MXrzbAL3zSu65LiQ3zAsxyV9iky3RB7pFh02Nwh0UkLPgcH6XchDZbMGGolsrM-ZiwqC7z_lMkKViAUWqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
دستمزد محمد صلاح در ترابزون اسپور:
🔺
هر فصل 10 میلیون یورو دستمزد
🔺
هر فصل 7 میلیون یورو پاداش
🔺
20 درصد درآمد حاصل از فروش پیراهن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102914" target="_blank">📅 19:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSPTHW2Oc8V6zSI2j4oZy4d7IHr-89dX0-VjOfpGLF3tVu0inrIwjSmaTykUVAYIhtSq2g8pq0iIEvKi9IcW5LLLJ6KXiaB4gNr9HIRXj7MApwV6hvAlyHtaDO_XQeKPH93D5oVYUJHrzuwHIUn8kLYeTEjwymK3obiBVhaYT_UYwaPMqLs2XFdYMk4PebHuW65tpRWzFH4ZkV-un7ky5p-tiFDCGGS9AbGXFVY-zwVXnWDdVAv3SMAcTehBN2o1TIjYfuji98jkOvNwlPnaXeEK_AgndI7vwf_vxEW3Ip9_TlyBmsel-rO91y_pLIhFiw6jGXbzQRwi2eMNJRgj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😐
دیس‌بک ممد رضا گلزار به رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102913" target="_blank">📅 19:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFg3sdCmqaojYGdUY_0bxKbxHwHWTxJOuHXmhv8_T3MHoOiWZ0eVkEeHN5vVMLDOXDyoc6Qi_bnTuSL5De9DGA3pT0DBZTxEzVbUdOD2WxJwIyarS3cO8asFwn8O-15pRCfkiW4LQxyr1robaLlKYAZudg3D-Z_T7E7G1CFQSyj3WCSOEnCCr9seqi3_My3ZRvOXdulyBneh-1tAujb834nHYSj1LwA9LBSqDj8TXnac588f2cbk_fYnR5DYOhbAkHC-3PzkW6lBxqjy4FyMBrhzjPEClQTnw2G4dFGwntZjCiTWUH4xiZ73szjN3MzhUw6CRGV0Vh1GMqvki7iWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
؛
🔻
خوزه‌فلیکس‌دیاز: رودری رسما به پیشنهاد رئال‌مادرید پاسخ منفی داد و اعلام کرد که خواهان حضور در تیمی‌ست که سبکی مشابه پپ‌گواردیولا داشته باشد و بارسلونا بهترین انتخاب وی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102912" target="_blank">📅 19:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102911">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🔵
پخش زنده بازی دوستانه استقلال و استقلال خوزستان ساعت 18:50 از لینک زیر
👇
https://t.me/+KXeZA-eHx3RjZjhk https://t.me/+KXeZA-eHx3RjZjhk</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102911" target="_blank">📅 19:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afgIP1nM0FK498deWe7bdW8enAGb31a6TxBMncy4GFh-xuxiwmfPxsiVaT_cXusw0YtyI6mLQLSYF4xM9z39vMaDr5x4BF4ne9mRt5EvuF8GrhjcNqhKiIdFlGdVBWvVHiZ4Sc3A3aOXWkomV6ZiPf3Hyl8nmhSVqse3345Pmn07flpytA_T4WuXBsVyMsWGjoGK7i8EUJQPqNrZWQWYbeNY2YbXCgl1os5umnclwfbc2KPLSDqNqcADtYYCIm92TjlION91byPkpS-7YcmJlLDafFGQ7hXSuRxbyTt33j3-fvx4gitNaBMX0ij6byXJDz0ItA27vj4aaTOX6GCefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcwoFSfKnlwGMDVZYpdCAK8RqVDYrVDBurAPityEE3mUooFZeFqfVhhT1R4QSta85fi-cD-wlzncPrdWP5lHBYjtf5pP1aheRQwQ1UrCDWgIEb7fTaScRRBkGxrdgJzQ7dtGIoIAtKhtUibjHKZ7p4_K2oFA3FKjRWXSfLn24Ge-MggdUFbDS9vVaHlTXH50jt9OBzG0gwUTu5dB8m0S-V6SLBruyONpcFMDFdSv9vNLMpqmPAPcNuv-Jan1n-PSufKKhT84bXvXeVWXlu0Zl24bEbRSVXfKniJ4D3XVn9FWXIYFvu0-RWfxlmV9tHT--Nupafx-Qfaf9PJ3t3yZzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
شکار لحظه ها از امباپه و استر اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102909" target="_blank">📅 19:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e56c5aab7.mp4?token=HoNasQXDN-0qEVbwZgZ0R_tszJUu50kAOT-ZcV-yg2E-YTS7VtNyy6yP24rJOvwtjdBb0rJBFqk7JHrFipde2zccfL4K2olWI9nTOFzZtO-0xIZNMBm6JQSaJcO7M1bd_rD2hyFw91T3U-ineSuU-UbatV-1R-KZYV9-aAaPdAhhW5v0lACnmMKsYBIDjsjl4i9K2KIDFIA2uS3HKVd5rRKhS5h_lL5pVZrEvzJYgdRhe4rFMC5Ch8hQNHGbCIuHNysc43Jvke4RHJccWl2Refmmd4TZ0PIkjjyZx994iWeQmPxAdTC-GoECK8Oix3cNnQylzUxUQeTZnnjUmq29Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e56c5aab7.mp4?token=HoNasQXDN-0qEVbwZgZ0R_tszJUu50kAOT-ZcV-yg2E-YTS7VtNyy6yP24rJOvwtjdBb0rJBFqk7JHrFipde2zccfL4K2olWI9nTOFzZtO-0xIZNMBm6JQSaJcO7M1bd_rD2hyFw91T3U-ineSuU-UbatV-1R-KZYV9-aAaPdAhhW5v0lACnmMKsYBIDjsjl4i9K2KIDFIA2uS3HKVd5rRKhS5h_lL5pVZrEvzJYgdRhe4rFMC5Ch8hQNHGbCIuHNysc43Jvke4RHJccWl2Refmmd4TZ0PIkjjyZx994iWeQmPxAdTC-GoECK8Oix3cNnQylzUxUQeTZnnjUmq29Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🤯
کصخل‌بازیای جرارد رومرو خبرنگار بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102908" target="_blank">📅 19:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e118ce024.mp4?token=TgU9g7h2F9pO2Q-fez7yYUqyExSGG0asGS--K7W4eTHXB4_-kr8Ywu_6-4cMaX8Wt-qiZ5P-tvPwHVjdVS2CNRXynRaTujGyWF86jLQWEhS2WRmgw535CaL79qPZ8vki5j_7uzUO72ephLHQhTrkAJsuBxNKrS3GVSbZJGyRqaXZeUuRBQQKmaLabOD5DhQ7tJwxOlZYxCDtuT9AqYXk7OyFMW6uX94rYM4-pQ9TAj-EtxenCdPamN-sFtYX3pw_0ttqnzNws_DJmkdiR7tC0WrbihCgdC7uRXKLLJSRJ050ZyW1ZIKs-HDOw8_ER_fbwtTp3-OGpHWXIZkuFnIYXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e118ce024.mp4?token=TgU9g7h2F9pO2Q-fez7yYUqyExSGG0asGS--K7W4eTHXB4_-kr8Ywu_6-4cMaX8Wt-qiZ5P-tvPwHVjdVS2CNRXynRaTujGyWF86jLQWEhS2WRmgw535CaL79qPZ8vki5j_7uzUO72ephLHQhTrkAJsuBxNKrS3GVSbZJGyRqaXZeUuRBQQKmaLabOD5DhQ7tJwxOlZYxCDtuT9AqYXk7OyFMW6uX94rYM4-pQ9TAj-EtxenCdPamN-sFtYX3pw_0ttqnzNws_DJmkdiR7tC0WrbihCgdC7uRXKLLJSRJ050ZyW1ZIKs-HDOw8_ER_fbwtTp3-OGpHWXIZkuFnIYXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح فوتبال کشور اندونزی رو ببینیم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102907" target="_blank">📅 19:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXu6tkJPjg7_av773oeV5xbU6JQu_vLVIVUXy6Otsm3-Co0H6wUMoYTTMb9CpJrRN1bIgw73BH-_Ot_GWjyPFXhre-tpj5QB_SLbrZUkg0y7SwRMUcCnIx7uiJgOub82ouljBl5psRBkj1_Qc1zpD1YeRozvc82Inrt2BOVh9oUtA-V9tohE29ASfbsvF-lexwzOJhIDYOeU7ZTc1LWyyn1oA_zglIxSIchFItu9R-wxQsQPFc2rgXxo1W-Moehf_JpGY3ZbgumS6qaHHXr5CCiLWi4TAT_msRQDc-U3Ao52lnMjsOww5i3L3AclousrVeF7FCx4zo8JJV06ZX8-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دیومانده گران قیمت ترین خرید رئال در پست وینگر راست از زمان بیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102906" target="_blank">📅 18:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2I5Ebj3GkonRJqRMrn4lhoxYIonBmaJMSfll4ZBULL6irWrBq8VZtDqXwROUTvDzfKDBEq552twtD088ZfZv86vE321ENzwhYUaTkDU-fyL4tTJNx1tLLIFiVq-ELFfuhNHUciL-875cISw2r7OCOZYuR74NtksYcL66F3MDs1sbq8_1EvDwO6qOaUrk_-Zqs8DZT9-IYI4sjbXvYFJKTjUQoAErN-KSvQGXVJs-CwzUxX9QXiFxo9wgXwTmSTb82nsMCSTqeZBl8MxD6DZlIcssZenbBCVJbcJAdIojrdiGDDRfEOHjaZuuD6Q0jkKsLDeNIWhXFndOev9UenRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دیدار دوستانه امروز</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102904" target="_blank">📅 18:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgmOwewxRgsGPLasYzCyiAfheDZtlE8Iati8jI2wIEOijF35xPdD2KZ6o2xDFjTMh_o2Wa7YhpsfrqK75qY3Rre10sXWUHRud1wvtyBmnPGOyllh8_-80MV2lfuscvFJfAOBdGXmc1iqaKZO2i70-KtLzkofmRNHCeiut7_EpPchZnrdFd5BROBH5fWKQVMd5Tpg5Emg_pLH8J1K-dGzfqH8eehp3XeTE8QW9kOn-eaT4oUKgQBn9sG0Io7KB8JDvQcE30nzmXx_TKq1alCNF6EJjxLcih8ta__005cylGUOFYPJy_P9rsRMz8BkVUIme1sPaXa-6zLleLVH5ncabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🇪🇸
فابریزیو رومانو: رئال مادرید داشت روی انتقال رودری کار می‌کرد و فشار می‌آورد، اما بارسلونا با قدرت وارد صحنه شد و حالا کاملاً در آستانه نهایی کردن این انتقاله‌!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102903" target="_blank">📅 18:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🔥
🇪🇸
#فوووووری از رومانو: فلیک شخصا با دکو تماس گرفته و گفته که تا آخر هفته قرارداد رودری رو باید نهایی و تمام‌شده کنی. دکو هم راهی مادرید شده تا با ایجنت رودری مذاکره مستقیم داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102902" target="_blank">📅 18:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhpeFBg_pFVKZfKvotAgvT440P_L2o-2PfkCYNwJPCwAyTMNflPWOgL_aTXBdGn04EWRYtU4H5_Wu7FSGAua1ohKtK-2AoBcSWMp7E97Xygproc4AmzWWSCDW5mgW8v29VsLQ9h1puEivBwVB4Iypa6QfP9tH4ELsrPiLsXOyxQ1N7RfHUF6_8hjcsycV-FwtBsq_yK9opfBvpITAZVNZWfUoQ7X4VJKNqdB1LpS34897-B3cOSgL5endOx63gaUkDdHRrZN2wUo8PmVYYp3-RIVHiO1dIPngQpwh8_p260PwxOHZTtg5n5W_LJWue-Wp_EP4wOiSpLSIHSzQOyOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🔥
🇪🇸
#فوووووری
از رومانو: فلیک شخصا با دکو تماس گرفته و گفته که تا آخر هفته قرارداد رودری رو باید نهایی و تمام‌شده کنی. دکو هم راهی مادرید شده تا با ایجنت رودری مذاکره مستقیم داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102901" target="_blank">📅 18:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280d3fe018.mp4?token=ZboVQIqN0wBS1nIAor3tQS68ZfNc2nWh87zKr6GzF30967_Zf81QfDNwm4uE5CxXceMrXv6M8CxAeFerjkS1gaFUGqndqznNPemUOlfJamvcO-CEp7MfSv24Kf_iYASeAM2pql3jv_S4OSKldQm8ZFzoN1DUKhYpX2cx1f6CC3Z42aw6qd3MO5iMZyHPUpP-pVrQowktu65R-Hu59QH4WVXVIvPMR-R8Q4K85zHHMhZ5Qy6J6BRm8QkgFz6k4yJsz3b2tgdr43eAzrZzlHsDwzrOHsSgOqVKScI8I5LsM2VhRJsyBmhwKd_PBtIljki_xzgHacpl-TLw8oNoA3Q6vbWdauy0zJx8RFFtYPLXZ7LxFABpVUm28lVjaQeomlDfc_M8mjaEazqKVNr2EqXaHPWap5hUVxIhBjQg_jNvRqnOrLka3wLUjtZQdpJOn3GPjcMZO0H3lXCn7cCl9pCHqAzYDXpjcPvIjSlgfMu7bObNtbHn4amKvQag1xtkeH7YP-RPw6QjgumpsuZW7HS3jdKaMaHwOXjF-N8-PURujwzJEeXVTwxpVIdyp5BXnCLmgggpGn8dP_MoFq_5GPNC8SAbcalR2nNPKLG6lulNhDNqhD_MMEzTSuUrhKLY7CTox6HW4rMh_63xOeXNpAZqQiaeqYjdhWdnrRTqUhsASdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280d3fe018.mp4?token=ZboVQIqN0wBS1nIAor3tQS68ZfNc2nWh87zKr6GzF30967_Zf81QfDNwm4uE5CxXceMrXv6M8CxAeFerjkS1gaFUGqndqznNPemUOlfJamvcO-CEp7MfSv24Kf_iYASeAM2pql3jv_S4OSKldQm8ZFzoN1DUKhYpX2cx1f6CC3Z42aw6qd3MO5iMZyHPUpP-pVrQowktu65R-Hu59QH4WVXVIvPMR-R8Q4K85zHHMhZ5Qy6J6BRm8QkgFz6k4yJsz3b2tgdr43eAzrZzlHsDwzrOHsSgOqVKScI8I5LsM2VhRJsyBmhwKd_PBtIljki_xzgHacpl-TLw8oNoA3Q6vbWdauy0zJx8RFFtYPLXZ7LxFABpVUm28lVjaQeomlDfc_M8mjaEazqKVNr2EqXaHPWap5hUVxIhBjQg_jNvRqnOrLka3wLUjtZQdpJOn3GPjcMZO0H3lXCn7cCl9pCHqAzYDXpjcPvIjSlgfMu7bObNtbHn4amKvQag1xtkeH7YP-RPw6QjgumpsuZW7HS3jdKaMaHwOXjF-N8-PURujwzJEeXVTwxpVIdyp5BXnCLmgggpGn8dP_MoFq_5GPNC8SAbcalR2nNPKLG6lulNhDNqhD_MMEzTSuUrhKLY7CTox6HW4rMh_63xOeXNpAZqQiaeqYjdhWdnrRTqUhsASdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
▶️
اگه براتون سواله اثر جاودانه "تو که معنای عشقی" داریوش چجوری ساخته شده بهتره این ویدیو رو با دقت ببینید و لذت ببرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102900" target="_blank">📅 18:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102899">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43fa6af7e.mp4?token=DCR-He45Hn_i4Ags7yMxsdaRobGU2T2MuPoPvIkcMzOdKRM0VnYJkfIxI3uiCUv1eqh-Q8LmpLJlz1yrY4k6cPMJ9qpjZYdD1SRKNUkp2-4WwDfzqfecM8TybY7cvLvgC7rLHQ15JUtGai49yb997eOxcMTjhSMu4DxRcznWqnI-cLyhs0aT1cdqyw3y-NLUPYkZz1z5QORaq_1aHXgRn3CA9bxBiQryrWrX2VmhlshTvOQw70n67vsTi_pT40x0kmux6oxHJ7J3vUFjkiR2_4MvOvcim-PZTKxEVDZsgW2dEn-h8LZ6zSX0Yrr4T-csbDrM1ksyCBGozlF8D57Gjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43fa6af7e.mp4?token=DCR-He45Hn_i4Ags7yMxsdaRobGU2T2MuPoPvIkcMzOdKRM0VnYJkfIxI3uiCUv1eqh-Q8LmpLJlz1yrY4k6cPMJ9qpjZYdD1SRKNUkp2-4WwDfzqfecM8TybY7cvLvgC7rLHQ15JUtGai49yb997eOxcMTjhSMu4DxRcznWqnI-cLyhs0aT1cdqyw3y-NLUPYkZz1z5QORaq_1aHXgRn3CA9bxBiQryrWrX2VmhlshTvOQw70n67vsTi_pT40x0kmux6oxHJ7J3vUFjkiR2_4MvOvcim-PZTKxEVDZsgW2dEn-h8LZ6zSX0Yrr4T-csbDrM1ksyCBGozlF8D57Gjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی ستاره‌جوان باشگاه بارسلونا امروز 22 ساله شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102899" target="_blank">📅 18:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102898">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102898" target="_blank">📅 18:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102897">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCtsSwWSHY4d3UNdruvZqpEWIuf0opMgCySCNtdFJyj5n_7fXq9LOjgqB3GOVUPehY_31cuts0kByikQD-Gk14dgCRBP4_VUn9C5hp7N6GYeE5BeU6b_vY1W7LTyEdkrBsF-PA2qnJF5UWi2Io1r3QnaOv8P_paYQZNPyVFsaE1BDtxrhhRBI1VEGCY2FE0TE4Jm4XM4ByL6eqfgf2FuOlkJ6c-GwMB8cFXoHDHGT-Pb5DaaWpcozsCigMU16elDfzcTUcnhqhqd51g6brcIIMQIkGDT_YXVyjKDASi7CSRsuQh-tCIop95IphZ35qZDq3Qs5FsYewrZdQRyueNpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#بایرن_مونیخ
Vs
#استون_ویلا
زمان: جمعه ساعت 15
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g15
@betinjabet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102897" target="_blank">📅 18:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102896">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL0d_95TrbCb3fXWTupgc3Ig13N_-3bnPQatuqQY0HJ677K0zTcH0oRjwJiLPFHhOOxg6bTKh1EwiyGtUbMGM-2rh90rDhfLni4FHyX8fGgyNK74rZrPyZUcIcE3-OhTBk0kfheCfNeG6o4v5rzUT2djzBb53LITlOkq9maDmI34iD9t4PadW5M3ZGH1rsxdYYK9WS8o0QGEXoJnJgUN39EMB0Mj4exOV8mdhvJI-HHBzEA09WUnDoO4q9OLzDEjxIUaESsjVnwb4ZgAnhTdqp8E5ySfajlwBKbw7EvPqNvk6u-2mqnLJi0VlaWfj3JvCZ6urDWVwYmLx-Ed6cBU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از متئو مورتو: رودری با بارسلونا به توافق نهایی رسیده و ظرف چند ساعت آینده قراره دکو با مدیران سیتیزن‌ها تماس بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102896" target="_blank">📅 18:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsApgMx2JImOH0DKQvgwTDoVPeeMJdAcJ8eWQ6_dD9hTLkDtgZ146QDvPut-C2fqmjW0lICnkQuobu9ZGj4e6jcAlJ6UwmcEkCbh3l80nJu77LifVw7hau1oN9k8HNBlmwXIYRWgrvb6lfRwlgVG3ldTwL8a49ToA0Idx_ExB9IHglT7CaHzMAe3ZkOsxUpU7mKgkWnY0HI-efW6WZubUzficiVc4bvmvdLLbVOZqiAJCEWE1yZ-n_Ai2GWwr-xT0vOuqvQudDW2SUadp801YMJdOzEhEIU9g5risXCruOn_3ekeXoFg08SItLzX7F5cAd-fIrq4BpztqZXcTmCBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
‼️
رقم فسخ قرارداد رضاییان با استقلال فقط 100 میلیون تومان بوده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102894" target="_blank">📅 18:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102893">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbde653e.mp4?token=EiJeSJuqD---z4vGbsxf4afFBqvJrAJNL7Z7CbxKuCxVbE2P8EO7dXjB4xcxlreuEdGpDvaWw95B-aq9aSVsL2ZJ4rYCWmEm2TO0sKmEx8WJZyr6BzQfBr9ga-6Ex_e3uoDs1TVxRP7yeRaFTEpGXD1vyoZL44ESwREiyIWFjOT5yvKHGdTlAPbl5_mYbhUIhxkVA41-s-RyKIptNQ6EsmVwV6UzyJMeAqo3BoHYhUAKElcg-NbIiWHfLLl6EtLd4EgDyXCZUBwtXre9A9dtaibWxVUOYrWbASuQg0p5_hPoAod4otw3wg8ytL26jcKRKQ2KZZTx6Bs2CjWTmJdmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbde653e.mp4?token=EiJeSJuqD---z4vGbsxf4afFBqvJrAJNL7Z7CbxKuCxVbE2P8EO7dXjB4xcxlreuEdGpDvaWw95B-aq9aSVsL2ZJ4rYCWmEm2TO0sKmEx8WJZyr6BzQfBr9ga-6Ex_e3uoDs1TVxRP7yeRaFTEpGXD1vyoZL44ESwREiyIWFjOT5yvKHGdTlAPbl5_mYbhUIhxkVA41-s-RyKIptNQ6EsmVwV6UzyJMeAqo3BoHYhUAKElcg-NbIiWHfLLl6EtLd4EgDyXCZUBwtXre9A9dtaibWxVUOYrWbASuQg0p5_hPoAod4otw3wg8ytL26jcKRKQ2KZZTx6Bs2CjWTmJdmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خشن‌ترین ضربه‌ها در زمین فوتبال رو باهم ببینیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102893" target="_blank">📅 18:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102892">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeYYiWgRHkcPc8tON2JPoP5ql8Lcp6Jok7V05zL-1DvmMmCMiY6sX0LNPZkH-0EwZnUB616KEYCDWaLogeWJbn1FlxMPnAfp4x2HRUVe2gttBX28hKeEeLqSp3RgW7GSWqH7Ovo38Eq99oKffJbby_SLkRINFuaf1TJzPDLjJ4VZpV9KsvReCbFB-C9AEqTSAyGNgh3L8MkpENsjW59wC0JJzYkP3JM-kiDs7TNpRdDQ8gy86xPcWC_8MJhzKSKNam8dO5wxXWXfqsC6ic7PN8WpTVPOZF8SADuVdvNZZ4EjjXflaTlXV9UJyem8CIegDLw8BQ7nQNCrGXkZM1b-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
بعد از ورود دیومانده ، اسکواد رئال مادرید حالا به طور کامل پر شد و برای ورود بازیکن جدید باید حتما بازیکن دیگه ای فروخته بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102892" target="_blank">📅 18:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102891">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZVYgUY5yTyGg4N90Ck-nRDhrHNIuL35zcpl22et0CkGG6AA92tLMHk4Tl-HEha98pmxHsvERga4LNSSbHE3N7RSTeS7_97ePrpgswL3eGbj64jL9t2wL1wjPj9hAH299XSxavzS2UVIfdWXUDtB_FGbc6snydEqpJ3UnKsIvGVwXETr2FHUliowwsO-DlLrMy0uz0MJOE-PMaBBkgp6-Ldhv7Cspwui5dh-LGmuHqBqDhsoVCUUisoFoOn7zZIb2pSJDfdJ8g4l-Mhhlq4-99_tLc_s8sJJ3ibP5eAbvM89YnkJqrSuqfNc3S230avEgjVivRO3yrNSr2vVOwaskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اگه تمام آپشن‌های پاداش قرارداد دیومانده فعال بشه این بازیکن تبدیل به گرون‌ترین خرید تاریخ رئال میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102891" target="_blank">📅 17:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102890">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng4ULxHzkjagBcsTHBfhVzlX2nVwuR-xtjHUw0kKFYRMwFdH7llLlRWlYVMf_Yv-OWhBnoma5c67MG2mGwe24XCmF6cn6AUw8Sx37qBKoCP1VK-freRLsgP_nqwe94YED_W0jTmDtKDzV6fwVw8Ub5OEFiROwMhotSCMBMGdLjdCh3fTqhGE1OeahQJZaLYaOJ4bFN2SHnakeMjaD2gFyjBdllInKld0KWsxzSkUBt8nJivnPHsb3xqBk1yyxs45fRMoKgplT971Q6YmYt8BabLS18l8qTjzg0DtERFeE4mtmcD3pwNr8VW-Me4gJbZdfyEgpjrGHcJuA4wguYi_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
💥
🇪🇸
#فوووووری از جرارد رومرو: حاضرم قسم بخورم که رودری بازیکن بارساست و فقط مراحل اداری عقد قرارداد باقی‌مونده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102890" target="_blank">📅 17:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102889">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT0fj4dgfU5xQTgR1QhWxh1e6Rvm1gTYLofM7kyCUEevC6oU-oe0F07S_jzplTZz1Ui0mpKxJoK6_XGTgHVITqn9UpKc4vo7aKk5NsI6zq7OnhxnjViueFs7EHv0UirFa2VF4-iLJafs1aIfVFrVAZw2WRzEecEDZ7r0ViDP6pNtTYzT4NlB5UDJaOzPjxMOwr3C4fhbycy23fwdHPUPHoJU-c9hrgVUVy12D5nUmCwy87UY50z5Ueqt76HmQDW8l3O1cBh1I2Kqw0W5ZFOw82r1ZI5lsJBDVq6_UXGYwWlV22zUYmZkvS4K1EqkqVRbrMNDn5s98Sm_MtyCMUZCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
💥
🇪🇸
#فوووووری
از جرارد رومرو: حاضرم قسم بخورم که رودری بازیکن بارساست و فقط مراحل اداری عقد قرارداد باقی‌مونده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102889" target="_blank">📅 17:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102888">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSm6xYQkvOCwlruC-CcWroKLU1dy1TXAZU_sy5SfEAqaDU07tD-mZ2-YYhGufuJ5-qFie310fA9AIzzMTkwweY4wpCzNIFFXWJZrESJRK3BzPeDMWPwgcjhSPv7wLMNgEFqvXIkKk49FOIIqBlshk8oX1bJPUhAoXynjcyP7s3BABk-oylSa79Ffob5A4SJILmBGBt7nOExF-zFckYscZpGH114cfzSZhjVXLPPA233Bq7LDRU1sXKOmuPqiXHAA_bFYJA64MthHe6om62YlLQlmIxO1Np1zb-KZQk3svV7GBukhFDcLEMNXTFYdmN_KNGV_1NHcgcaZ2qw4Ecl0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🇪🇸
#فوووووری
و
#رسمیییییی
؛ یان دیومانده با قراردادی تا سال 2033 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102888" target="_blank">📅 17:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102887">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🔥
👀
🇪🇸
فابریس هوکینز (بسیااااار معتبر): رودری به‌جای رئال مادرید، خواهان پیوستن به بارسلوناست! همچنین پیشنهادی در حدود ۶۰ تا ۷۰ میلیون یورو می‌تونه برای راضی کردن منچسترسیتی کافی باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102887" target="_blank">📅 17:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102886">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X69GiDpFtrm8tsBm8Uc3xKGxht8wFCUQIkTt0husZMS9s4cGGJlKmHI1tl60JPeD86lNgewtVEmeYb7nfJvebGv7dXlE2ciCzOYBpeziPX3MKDypKr3J2ZlnuTCLoEBKknPoaqFLQ1R5kpQEY5uy464EYc0O-91M4pd983JBsm3GENWesjRVpObrY67Xm7ctRPXVcG5VL1foKTF08GPNMVCl3oho_6MURrKBsOlHRUi0hj1sFwa4gpCmUP0yxwsEq5p55L1_4gOfK6_MvzgfaBdqms2a258NMfxg0MjQXtt0SvOsNqbeuChY5Bt3EgD4BU6emqj437AwwY81DH2GmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
👀
🇪🇸
فابریس هوکینز (بسیااااار معتبر): رودری به‌جای رئال مادرید، خواهان پیوستن به بارسلوناست! همچنین پیشنهادی در حدود ۶۰ تا ۷۰ میلیون یورو می‌تونه برای راضی کردن منچسترسیتی کافی باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102886" target="_blank">📅 17:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102885">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUQCQvwOMA2MRFzcs-IkuXTx3_SqWamNwCgsGY6qArWvGj70xWDGRhCcBjXCIErpDQsAmLySmtC_qIj18FDDD82ZXD9SYY1cz9mzLkFiUVdiEz8PQFmcBGNXLqBbA4PIUtWgI38YlDawHUn3nBQrSFTSLxxcNxAS4LmdsQth36njmNX5lBEZ__Nt7KRTV0tawVQfALxPAdx_p5gyRoczG88i6_ygiX1WYGeG9Vyfy0_JE7mY7pNEUz6ZZuCTQXtVeYAfE4w_JtK-oZTgzwX8JYA0a6B8JuJyHrGMHcBTA9vsaQLHuD9Ml2ZLX5VireQjBwI6pEN0PU1C5fnYhGtcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
💣
💣
🔵
فوریییییییییی از جرارد رومرو: رودری به پیشنهاد بارسلونا چراغ سبز نشون داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102885" target="_blank">📅 17:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102884">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP22e-TJcHNoKFQ7t8zwg8PNS4S4ZK0tNV_acDToE-C-GPUaamcwAEqq9qJmkYjouYy3utDxnaMr4UJ9v3rpoWU_chyEqVHoH9f_q34u043IujsUPzcdq4sLql2L4Y7DzBglbkgdF045D3YK70vWm6F9jZJmJoRfNRdaoGHuDRoP9s3OQfmt7iJBcZ-SRGceEcAweF3ud35v-oOIPFjQthGL62_oUkiiZ2CqTUc4DdfxqQ7a8mRcGOdmrmBdx9IEpm0T_ewBMRtT3FWSvWwMfocruIcyj1X1n6auRewZZjsn3yD8pcLY-1qcdUVFLXMDSjVUdz2jzT1eawjIlE-52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
پیشنهاداتی که گالاتاسرای برای فروش ویکتور اوسیمن ستاره خودش در روزهای اخیر رد کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102884" target="_blank">📅 16:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102883">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SthyayuP_CRf8TX3OB1KNPHc9P4fKODSrpNLMRyPkdjWZ6fJSsCBFXZTF_UnlcYlSt1QZ5AGxH61h4h6Bsp2HiEX4-0ADc65phgWbnVEkC45FXB3KkPrjMtp4UTiAqkyNQjXjUGwZfoLsna7O_cmTzhuNZKt0Mwq0ql2iOxc4_jNrSj7AvWTQbCItM-i0pAER_Lt5XUY0SAkNPl9fEXEwkVU6qOphZ7ScxaPeszKxe_N750uHDzYPKvlyje7P8JPmBM4Xf2M13m35qYnRZ3pSNbKWZhKVCM7umgwPWBBBfRXMUziiS_VHIibc3KygoOI8v1bC9Cw0RJDGEl9iIHSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102883" target="_blank">📅 16:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102882">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f51bc68e.mp4?token=JYQlXOnXJjtmeIaIb77nJhZ27Ph9WXupjejVbsYtv563hC4Nik3KPDJcJ1VyIHeIIiUOY8Q20KkshsINnIhgPJc7qLgS4J3xcFbIC_3waljCoDmirRzOwqbc0V_nWk5XhF-bVectjgKjjqmLV34BTTHxahfTBpk6K8NudGbNiyT33U5cy_VYOgLB8FYSg2zLdD7haoHFbu9_s6hJGIOCy-L_nZsGkpB5y6E40xkiK9r0YxtMd7-zvUiW8dVlehpSgwne03mXPbZHUjMgGJ1bcQXNLoYxMZTf4HEXxXEZ1dcQP1YmV7wOYCMo3nRAhFpnMdTQTbLzJjX_z3dmpegAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f51bc68e.mp4?token=JYQlXOnXJjtmeIaIb77nJhZ27Ph9WXupjejVbsYtv563hC4Nik3KPDJcJ1VyIHeIIiUOY8Q20KkshsINnIhgPJc7qLgS4J3xcFbIC_3waljCoDmirRzOwqbc0V_nWk5XhF-bVectjgKjjqmLV34BTTHxahfTBpk6K8NudGbNiyT33U5cy_VYOgLB8FYSg2zLdD7haoHFbu9_s6hJGIOCy-L_nZsGkpB5y6E40xkiK9r0YxtMd7-zvUiW8dVlehpSgwne03mXPbZHUjMgGJ1bcQXNLoYxMZTf4HEXxXEZ1dcQP1YmV7wOYCMo3nRAhFpnMdTQTbLzJjX_z3dmpegAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
واکنش تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102882" target="_blank">📅 16:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102881">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In2VmDQKhiz3f9sfSADtWbLi5sHk9tatTmj-klvuXs2up9QDpef_U43eQc9B5tu2Ov8HeYtDfgz7HVl1dSP-dk5REDgiwdgalinL2W-6b7eSj6X-P7AiH1vRJ2it2PevoQ2bz_oMZfoQMs8gqf_y1u7qHi9j9jvWgSK5eveA0RWe2_dFzkmj04m1_3sNFZcjht43qTRUiJ9LHCVVxfV6tf83J9SrAC6tHeOahmddON04iEbD-s0mDgvV8q__VLrJgj3iOoDnyGNx4sVtXKSWGobY0ai_AuYFMbWdR6SAvCYqh_bp8n5TStsMgrv2OzfenjWT4GabEFQ2bbOeY7X7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رونالدو نیازی نداره واسه GTA 6 صبر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102881" target="_blank">📅 16:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102880">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed01098c6d.mp4?token=uYZXYTCpXtNllsbRbXl0BSM9kikKhl9CXXHE6Or5B_-bLV90u1Jt5rF_wgom3ILXddnFmwJPtgrjYmlqHGiWsXO7wpirOpFPgww6kNBBTpKAdMqnR07-2RujZik9P89UDelo51c23rAvbBCkc7xXZJ6xfkQsF1baddxEmdaEHEHgLXPKfbnDwwtJArgf3xofaR8STAnVscW39NapS4xxRp7ZfqltDWnB5gTgRVyNbu1jyfe5fW8jPUUyLx53oDk3HzB5Y301xf5bt3DedLV41kl0VR-TlvQcmuJDdh8YVFJ-FWt-xd-tf1pEsO1zWmNhyA7gFBEbiDlpaxZo3d6tXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed01098c6d.mp4?token=uYZXYTCpXtNllsbRbXl0BSM9kikKhl9CXXHE6Or5B_-bLV90u1Jt5rF_wgom3ILXddnFmwJPtgrjYmlqHGiWsXO7wpirOpFPgww6kNBBTpKAdMqnR07-2RujZik9P89UDelo51c23rAvbBCkc7xXZJ6xfkQsF1baddxEmdaEHEHgLXPKfbnDwwtJArgf3xofaR8STAnVscW39NapS4xxRp7ZfqltDWnB5gTgRVyNbu1jyfe5fW8jPUUyLx53oDk3HzB5Y301xf5bt3DedLV41kl0VR-TlvQcmuJDdh8YVFJ-FWt-xd-tf1pEsO1zWmNhyA7gFBEbiDlpaxZo3d6tXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقصد جدید پادشاه مصر: سوپرلیگ ترکیه.
👑
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102880" target="_blank">📅 16:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2G_IU4Nl-3q0Z5xxHE8jlDKNdb7_-G1dmMxt2cw4XLpfgow-lPYptMlX-B6VY6lNg1wPHm1qqcVPaU5YL0cHztgHfAMiSVI0XBlKYZKoKDoItVO3xMPi98mSXDBGT9ETom9St5iX9-AGGv2M1Z_48jTirZRK1-FL1bptYU6wmXCEgA2Xi68k5wLGK0dZ9qBJ8Cb2800cqnSP8M7jHZvHkSXaEaRb0vgYYdzxQrZO4se6qe-at88SHTAAvtNduQ8hq2DcjZvQfJQYJrKHRXaU22UPgfS9m-8tHxM9881Rq_7YFlxYg6BZPBGtK_pgophgSFS7e3nZ4aPCjWZTIBt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
✍️
✍️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102879" target="_blank">📅 15:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAMgB3e_x6xHxrqtl3RB3Vi0nCov_Xddxnv0O4ouMjIjRpq9TQlPAGo0XGgIm2eKq77dX2h0nsu61EXRSzYCFihjtPErczDqDVDK4i78olKJttkTt8ueceDRwQ5n65mC2uSsT-e6gyARkSZgpsyuyNNblZNHUK7338RrdJ69pfrqy8VONXOy-zlPPI6CJWlK5xdLjiX-omr9Z-Yl8Zo2ap7mYTQWGn3awX1Ezzlc8D2ll8JcOlkq1gm3K7fsn1t85vPVsQTLGMGT2WAq_2Ov40M5o8_bfZl6VcIdQy_UY0noEcHNzNFGW74-dDKVexp_qKY4ImeIBPhnlkqWWpruwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
فوری از کارلوس مونفرت:
هانسی فلیک خودش شخصا زنگ زده به رودری تا مخشو بزنه و به بارسلونا بیارتش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102878" target="_blank">📅 15:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954417f16e.mp4?token=TCONPeaczFfen7XyChE16EH7O1Ys2TcTNqivPLyP0tje48fkYK2VmjvOMwzK23jXJluW6u_3A1gq1Q1zsQ3iHQV2kk14HqdUBAA6avfRt7p0lR7e9QnparKkbHen8zoOzoHmyby4XG7D3e36-28DSPJig0fYdzdm925sgQRcwAn3IRZNnh56C7dZi59frtMjHsgEBwg18bDj-wR0pPBpn5-AMj9Fb5PTQfEDA28M3cxT8lcvSFy1JcwN9AD_2dkz3GLw6qoJC_sJTbt-_cSME-FkvXKCSrRiVujdnLyE8AoMy-qprCqVhApvRm5KavdNWekQF7fywgU8YKrsZW1bdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954417f16e.mp4?token=TCONPeaczFfen7XyChE16EH7O1Ys2TcTNqivPLyP0tje48fkYK2VmjvOMwzK23jXJluW6u_3A1gq1Q1zsQ3iHQV2kk14HqdUBAA6avfRt7p0lR7e9QnparKkbHen8zoOzoHmyby4XG7D3e36-28DSPJig0fYdzdm925sgQRcwAn3IRZNnh56C7dZi59frtMjHsgEBwg18bDj-wR0pPBpn5-AMj9Fb5PTQfEDA28M3cxT8lcvSFy1JcwN9AD_2dkz3GLw6qoJC_sJTbt-_cSME-FkvXKCSrRiVujdnLyE8AoMy-qprCqVhApvRm5KavdNWekQF7fywgU8YKrsZW1bdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شادی کوکسال‌بابا از پیوستن صلاح به ترابوزان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102877" target="_blank">📅 15:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llljttQQ6m8o21KWywuUXeNbryE04OSKBTB1ozyZgUUcFTluT7IQztj_7GRwimYCXQvCe8gRICz7Twpiwz70Zn7igK6eSxbU2iRu-riVTvyExvAYvjCVF2lPZHMJntz71TneO6ohzNiu4GgQsjnlYVbncmvVQeSBJJnj_8ICFBJZICtKujBk7oRdgHLzPNCBcwzXdXniZ8JR8dtVzFC_ij4gB9wa4V8VaRTbe8FbHNiDYWmxs2T5NMH2svCMlsRnlLJB7xi1aG52etqJWk5lx_vA45bN1bGDWtkMVSLP0dWRiCejehSXRJE2p4JBrOPmBW5ugoQs0rKEMKupJ0ZN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
فوووووری: با اعلام راک استار گیم پلی GTAVI در تاریخ 27 آگوست (5 شهریور) از نتفلیکس منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102876" target="_blank">📅 15:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5B82Vb-2V5df6GnRymp4nowHPDCQwpQtw7U9bLzfPgp5zZdkfKIQ9LWF4krISNe50QQJrKZuFAIBHALGEhSLTkqdASm1q94Ua1uWJ7i8DgACVDakc72BR5yUn86jH1d9n3K8SG7apEUF72NqJvtLMArK5iAwGo2dL5Njg3UOZSh6FGVzrETPM1G3RTKvj1MvMPVUxyQ14U2fWgMLk_DH5unRgbZLmofXrm_IhvI4TOLrY8ayQp5iT9ujdMB4vRVHLnGmVShSTkfa5jXNs8yZhxZz1fgf90rWb8H6ZC__KE7KURj10WOCkVGmMZqXvnuYw4TFB0hPyJq610QPUPSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی از یان دیومانده در راه به سمت مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102875" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8a690689.mp4?token=AMuV1ZOfxMtKg9fYRzWfMe9itNo04ovaTLWRyPWkeAFNntHw93kTkc-kKDANAKfmEKL83-f05bDzJcT921QGjUjtNlQNN9c8g0_7w1piXSa2SRlFGSd3DX_b3VBTRRzY6tqI-97-qSWYYFqfC_k8EnSmRKrwFUlLuEzE-7X-9W9V8g_1WzPQor9938l2EO7jO3lpV7fpJCveDJ_Tk5y3pnYVjx3gwwKj4BqeKnx5oyVgzC5kCbyio6Ryt6miNWawLrI3s_eE6CbvHq6CSJ-3cJmd1SV9GxN4KQg74hJZIm53INle1jPXE-izhAvjlczQcmEoRlXVGGwzXRRQzwvqcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8a690689.mp4?token=AMuV1ZOfxMtKg9fYRzWfMe9itNo04ovaTLWRyPWkeAFNntHw93kTkc-kKDANAKfmEKL83-f05bDzJcT921QGjUjtNlQNN9c8g0_7w1piXSa2SRlFGSd3DX_b3VBTRRzY6tqI-97-qSWYYFqfC_k8EnSmRKrwFUlLuEzE-7X-9W9V8g_1WzPQor9938l2EO7jO3lpV7fpJCveDJ_Tk5y3pnYVjx3gwwKj4BqeKnx5oyVgzC5kCbyio6Ryt6miNWawLrI3s_eE6CbvHq6CSJ-3cJmd1SV9GxN4KQg74hJZIm53INle1jPXE-izhAvjlczQcmEoRlXVGGwzXRRQzwvqcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎂
🇳🇱
رابین فن‌پرسی امروز ۴۳ ساله شد.
وین رونی چند وقت پیش اعلام کرد که این گل فن‌پرسی، بهترین گل تاریخ لیگ برتر انگلیسه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102874" target="_blank">📅 15:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6d765b6.mp4?token=Vla5568HljcoXJqIOjhi3uBy1lOLNi07t-Z97MptjZG7gsKi97-foaqGofrNRI0q-fYeyaXIz8bxrjUg9aoYoqWUSJvWqn4360kSxoyWWF1ff2XLCnpx70rQLBxJ_sCe1q__6yODKZFab67cgMD3sX4zmsqGRhQDJsXWbxrW5Jne5_xQNmE2j_cUHn0NB07oeHj2YN9946InnetXIdIYWlrOoG-GqhuI-oErYVLJIcGGkM67fF5GsRqF3lG7qGC3cmqDza5yIy-nM47RCBrHOTnds9tGNWL5BrksjPiVvtXD0gfrYPz9pN4GLWb6CdOwLX3pAtPE4lOghxJHRmBmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6d765b6.mp4?token=Vla5568HljcoXJqIOjhi3uBy1lOLNi07t-Z97MptjZG7gsKi97-foaqGofrNRI0q-fYeyaXIz8bxrjUg9aoYoqWUSJvWqn4360kSxoyWWF1ff2XLCnpx70rQLBxJ_sCe1q__6yODKZFab67cgMD3sX4zmsqGRhQDJsXWbxrW5Jne5_xQNmE2j_cUHn0NB07oeHj2YN9946InnetXIdIYWlrOoG-GqhuI-oErYVLJIcGGkM67fF5GsRqF3lG7qGC3cmqDza5yIy-nM47RCBrHOTnds9tGNWL5BrksjPiVvtXD0gfrYPz9pN4GLWb6CdOwLX3pAtPE4lOghxJHRmBmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین کاری که پسرا تو کرج و اسلامشهر واسه جلب توجه میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102873" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9e41e0be.mp4?token=U0diTkmwWtIdJzb6P6ZzVBtplbVxCPSzhTDQJo9xHCg7vHkOPUO7UBhKPC-YWJRG6IrGDsPrm-BM40vNaHNobdmqFz3bnBu-rtFdbt4q58vnYg9KGxOkOIaQB9tN_MD1puOtoFg3iGHR5yafo8sbv2vQaNwEx9XryzYorBTL8yE2HTHaXLtSbKewtuO88Q-VEP9G7UQJjjq1hfvZ2kRB8OEKJ5ylufqT9bVxVJ0LOJOL7IKL8vNdZAwrWDvK3mhK0e-8EI-_66Icmzl2aYbNAc8yEQQdhyjOfF27QX48OVHdnHB0qklHuubE8GfZG9ayYEXoEsE7kE9wF-Ivnm1yNxpus7fkneVIFw9j12q5bCYxvBRhTwU7SoWI7oV8e6Cbj2WmAD0Z37sTOiw04buoHDAV4AyjHkfXGh2GpVSDm-ayN2_T4mmL0R8yUjX0V7U0eBxd6zk8YiJyE7p5EigO_Zx9mKVSj9u2pRKsDbwrdA2gaw__OgD3qccxk2WhmJZO7zuRgwdp2hS-xDtkkoNLihmDQRzQHP5KQFfbG2k7IBOT46_KMy4v4P9oZWY4k04qeB-OgRMW0b5dRSxoJzpdhhzS3DSqFcQ7QAdp0iVRYVdlqbTVIH1tgAJHrWVOn7vbCtbBCeoSk9ynTnodbVkaqCWphCrl7cfUUHbETOxCxWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9e41e0be.mp4?token=U0diTkmwWtIdJzb6P6ZzVBtplbVxCPSzhTDQJo9xHCg7vHkOPUO7UBhKPC-YWJRG6IrGDsPrm-BM40vNaHNobdmqFz3bnBu-rtFdbt4q58vnYg9KGxOkOIaQB9tN_MD1puOtoFg3iGHR5yafo8sbv2vQaNwEx9XryzYorBTL8yE2HTHaXLtSbKewtuO88Q-VEP9G7UQJjjq1hfvZ2kRB8OEKJ5ylufqT9bVxVJ0LOJOL7IKL8vNdZAwrWDvK3mhK0e-8EI-_66Icmzl2aYbNAc8yEQQdhyjOfF27QX48OVHdnHB0qklHuubE8GfZG9ayYEXoEsE7kE9wF-Ivnm1yNxpus7fkneVIFw9j12q5bCYxvBRhTwU7SoWI7oV8e6Cbj2WmAD0Z37sTOiw04buoHDAV4AyjHkfXGh2GpVSDm-ayN2_T4mmL0R8yUjX0V7U0eBxd6zk8YiJyE7p5EigO_Zx9mKVSj9u2pRKsDbwrdA2gaw__OgD3qccxk2WhmJZO7zuRgwdp2hS-xDtkkoNLihmDQRzQHP5KQFfbG2k7IBOT46_KMy4v4P9oZWY4k04qeB-OgRMW0b5dRSxoJzpdhhzS3DSqFcQ7QAdp0iVRYVdlqbTVIH1tgAJHrWVOn7vbCtbBCeoSk9ynTnodbVkaqCWphCrl7cfUUHbETOxCxWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
ماریو بالوتلی از عجیب‌ترین بازیکنان دهه‌اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102872" target="_blank">📅 15:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXgbMGsTKvP5gRyBcyex1yUpGX_B0fqx_EzGrWFpvgFk44w-RnAfJDfaqj6oETQG-hPhc2Lu53wUKd1NFSA_oiHHI-_upXpgia5nY-p61GfF7TWv3PfmNb9km6t8iIG9N0xP_AvEH6zxJG8C5qqpE9KDrlXUNpjdAMiuFowhxFiIx9fvlHE3nBP2b3ICoG2Rk_H0Up8tzg1jJ4SDClCE5sREnLhUX8Mf6-JiKCguri5vEcGI77uHRjHzhaxaWzF6xRL3fpQp687aYMSqnT7Hr4Vt0RQ_YxbmKUhbFzKTO52rfbHHTcITGI4EdolcuPdwYIKV6Gzxb_i3c91N240tgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش رسانه‌ها، "کیم جونگ اون" رهبرِ کره شمالی به مردم کشورش گفته که تیم ملی‌شون برای هفتاد و پنجمین سال پیاپی قهرمان جام جهانی شده و اینو به ملتش تبریک گفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102871" target="_blank">📅 15:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT2gWC5kFFMF37n-hsbNEIGSIhwb-SN0ui0hRpsgp7ahleWDuq_PTcLguwh0T2fNcw18Cfrf2zWyqlSMYOGA3bydV-cpHQT5HuKoIEG-Qbudv3eX0n2PPETc4bnnTz0zWIrp0VtQN8vEHuSiIg45MgmA9Qc3x0E1OG78unuD9imxlU3ZoabHBAmUljPmdW4rGBA8amG4jAT7JUJV5FNmXS1wygkpJ5abZd3Y1_VnyKXP0qqFwPc8sY_1ktwZ7-NYA-rZk0BM-TZsLm47UdS3KUxceozvc0du6o7jOQjjII4LYB0I08aHoorYlDXdXEGWFx-D06mspEPLTnoPKItACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گاوی صورتی تو تمرینات بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102870" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKZhXsefgb-kTuDd4u3VIgWBucloniqPbJAUD-qZUswn4WyTHsdOiA3KiwhDtYkx2vPA7mGpu7C8LxzXaXpKO6f4B8ju91gDu5RQhiYMtIf-dkuOclTHvr8HJWkrWHnWtgatXhbPB4fHG-OJgYggXxFg_f_akfdUSITf6OzEds3RiUZL_8nlhX0Elb_4SMRiwhPjAaXQvscCIFN27m3V3zkbQqzhho035d3Y2zhgtVIz7iE1--SAD4W14IOAk6j2nJgYlsgqliN_TI5vMu8n9w407bVEsPbejL8mQGPb-T2TEfm9XDqzZ4rN0DIxvd1ZeQ14GqqL9TTPb3jmbGQ0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgpfOvttM-8ygA7X-OON6VopA4muqCubrbfvn8hhcGa_nRLGQ6Wt8YlF47jEQqQ62KCFLNli2kZXmrDD3aa__cMMquTvlN4hpMuDAxmjr3tkEe9D8ea4KXRYyFkNwvTjdYjMtPVaiFt53TRt4RttnvEamYTEEhrTUUMV01mLXPhX_72V5_SekG717ek4UecLzQFN_IG2AZgiJJa7PK5Tsnkhqu6rZmramLPvyuLE8mUl6y4RWAcIcMMkbkKzQ8TIS4QF7xXTjY4k5jDKsjH5hdAQ6EozmoRcRMh9b2lvc0sJ7huWo1rPbO2No32gY_nqUXn8x49Wu2dw7B8EB9CBuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جیمی کرگر معتقده محمد صلاح برای بازی در فوتبال ترکیه زیادی خوبه و میتونست به تیمی معتبرتر از ترابزون‌اسپور بره.
🎙
به نظرم اون میتونست توی سری‌آ بازی کنه. از نظر من، لیگ ترکیه یه سطح پایین‌تر از اون حدیه که صلاح باید توش بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102868" target="_blank">📅 14:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102867">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f430a769.mp4?token=g7FQrHZrx6a4Y0I9CYWJx6DStUoQO2_bnTVSglsZLOsXy57gD42QF24C1NOsCnVlcyrz91-fc2tOkOH3EF_rBWNRnhVzzxaqOMTIV7uqtJiJVZiXyI8PTYfuwkAy1kOq3c9DnvgLsw97qfBdiem5RpcL_IGned5DAyOJcT5xWRboeJhO6Tnvq-Jp-DA66B816LU3aoSAOxPksZAS7-JVp20Gs0Y5KxTBofk45I7Yw4Qcx7qND2cuUwRHgvIN_aU3I8LEGu7cYJJ2esnk18_7OXajzFtBbKsn77DimcU6WR8pa21JLE4_UzP6XQZKSf2Jg6KYhItY6RqZZmlG2sBSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f430a769.mp4?token=g7FQrHZrx6a4Y0I9CYWJx6DStUoQO2_bnTVSglsZLOsXy57gD42QF24C1NOsCnVlcyrz91-fc2tOkOH3EF_rBWNRnhVzzxaqOMTIV7uqtJiJVZiXyI8PTYfuwkAy1kOq3c9DnvgLsw97qfBdiem5RpcL_IGned5DAyOJcT5xWRboeJhO6Tnvq-Jp-DA66B816LU3aoSAOxPksZAS7-JVp20Gs0Y5KxTBofk45I7Yw4Qcx7qND2cuUwRHgvIN_aU3I8LEGu7cYJJ2esnk18_7OXajzFtBbKsn77DimcU6WR8pa21JLE4_UzP6XQZKSf2Jg6KYhItY6RqZZmlG2sBSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه آهسته از مسابقات جهانی سیلی
😐
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102867" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102866">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cd6fd12d.mp4?token=qBe8vgfvDFjgLec5WFJgETLdt6QcmVPvEkm5rf4ectyjM2MtfGUzfUMWogiUbaBrOp7byswryw5vI9HQJ-Dmdfjs0JxddaKoi1JVuvuR2STv_C__9mGhWlK7PMD_e8kLD3Ph1Pgj7-yaFiyuJ4dpqoKXM21bFrPlMsFW_dnEVgh3325d1-ZrSREM76U5OzrtNCP1_FyOJ6-Y6fDgZv5oTPQYsvQtPeXYLmFPHXNoqEEALDDFdSsfr1Y_TXFUTW2KOMpCyjx-LrKbwREog00yUyQdHriDuOmZZ4D9_umvz99VEycM0XWMWTWxLM6wG-sfPfFPc7DhIui6yED3YKgbij9Uv5roERxEyndyUD-tkqlsnkTorvY4zlUgN3OJghoaRU7ggs4tatB-rw-hejwg2LwoyeKrCvWQJfV6dsy1pR1mP8WNGteQHUxg7qgmKoqFT7aY3NDpf9zu8NsWwuKtdo5MmgC6Ztf3DPXjANbhL51xtE910HK47zmr8PSPe8zdccxHJ0IhHpMgIXK7whRwpwDJUIUwNloO6WeSYBmco0QrKghiAy2FtE4Xzh4qu2JHeWhEV7wX8JAxbRrElKzBTEVFGoWkt6ibn-_fIqpH0u1BekC3dD4aUvSflFQWSXu_X2T1j82WhOM93IT3HhWINIjsXUTNLmNT_JN7yuClKyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cd6fd12d.mp4?token=qBe8vgfvDFjgLec5WFJgETLdt6QcmVPvEkm5rf4ectyjM2MtfGUzfUMWogiUbaBrOp7byswryw5vI9HQJ-Dmdfjs0JxddaKoi1JVuvuR2STv_C__9mGhWlK7PMD_e8kLD3Ph1Pgj7-yaFiyuJ4dpqoKXM21bFrPlMsFW_dnEVgh3325d1-ZrSREM76U5OzrtNCP1_FyOJ6-Y6fDgZv5oTPQYsvQtPeXYLmFPHXNoqEEALDDFdSsfr1Y_TXFUTW2KOMpCyjx-LrKbwREog00yUyQdHriDuOmZZ4D9_umvz99VEycM0XWMWTWxLM6wG-sfPfFPc7DhIui6yED3YKgbij9Uv5roERxEyndyUD-tkqlsnkTorvY4zlUgN3OJghoaRU7ggs4tatB-rw-hejwg2LwoyeKrCvWQJfV6dsy1pR1mP8WNGteQHUxg7qgmKoqFT7aY3NDpf9zu8NsWwuKtdo5MmgC6Ztf3DPXjANbhL51xtE910HK47zmr8PSPe8zdccxHJ0IhHpMgIXK7whRwpwDJUIUwNloO6WeSYBmco0QrKghiAy2FtE4Xzh4qu2JHeWhEV7wX8JAxbRrElKzBTEVFGoWkt6ibn-_fIqpH0u1BekC3dD4aUvSflFQWSXu_X2T1j82WhOM93IT3HhWINIjsXUTNLmNT_JN7yuClKyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از درخشش تاریخی لیونل‌مسی مقابل منچستریونایتد در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102866" target="_blank">📅 14:25 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
