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
<img src="https://cdn4.telesco.pe/file/Mm1QRsHlM6A-W2CyiV4U0RNaha1SWCnq-H4Ys1A5fIadHeRKqNDpDVjeAIwo5nk4ydeo4cxbgjlD8KtKq3tvZcR7Eye-9-aDMfTEqsmZRQazNEiE8uACIcFDjFeSn24OOS818GhOzOWdKPnMb418RKkenDd6pkQBvNKp6bd2E3iTzGAPn8B4sD-LkKGbpHEoTvqmTSkubi8V13x3_tP-BaE6n41U_gV3JAdDsbSY4cgUSqdPmV3QzElN1jTrxPkhkjHXqYPt-rFbcpuJ9CJm-SXu5MWS777BW8pxgMBxlbUfzB6RdC-WxelAjeCN1cyI19-kABnD8GxG8RowLPs7SQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 531K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 04:50:25</div>
<hr>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOou2xPAxJAdgwiCditfb4IuTuKyqX7qED4lSZSFvo_b6esmNdiFaRRmMufSd0aF-EOAijjgV74gzT4eEzXyUA6UWnznxfkgyS9Qo4d99q89nF28XuQ01Hh0htEbzXKL_g9BnlWScXY33kn8UqbVjJmqVwyu15K6HyxLLslWNCjjUK1y2z3o1uN6pyaKaUOGeWG41DYymSRUh2YmisYSl0as2kx1_4PYkdToTYgjrix-PHhraJOyXsAQ4cBp6ZafhAl8GAeYEE3sZToNJZUijEmwpii3GI3_QqJCJ_cvFpMq3UD0bSOW7GtgTa0McDGQxFiR5AMslkXYb2nqrYWmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV-Zf6wghRrYkqEA5oLJIuHPHyc8J-opyhc2Mg6wfHeSe2TCTn2PptPAC-aeKXmi63zU6aHQr3NmDipw114Z8-jCOkgNFmZVULR7d1ImfQUkj1UKOfcwSaVfhN_00VoZldE5JGlcKtJMke48F_B3P4Og1FIIAWFR_L75yVmN0axZkRshulqlvp3sdFE2Yb8c8Hs7IApXYccgefnlXBFIq4PrZN_VbMGoGamZ3StZTo_dzOR0xltXwzxc0ELTUmLAN1lWx5DycJje9ujIE94PcHNsf76OwEvJrRBPmFFuVcuAZcp9oxkzEU6vmGI7hrKaDlyejOxXVppAMlH4P18t3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJlLXXDdgsYXq3WLDOBDqJmmRMjblQjcLF8tgIsm-W3bw7cshcNLI8xHc_aA323VLWN7j1dzAnE49GBmBTV-4cCJk53RxWiiOCXSkclv2TKxaVjp0c1ZijRZ5Xhg1Ks93-bBncRKwZ6v95afAIiwzbQ5dnzdmszGIZqHbwW3h3X7pdyIRAVncFCL0648vBQmgij0PABwyWDV8hZeSCCAMT0YVUqimmJentIUYExu639TPNOXKSoCkupE1sBUB8uIIhkgd3dj1vWn1sEUPrNgvZcOCgVhOTC1JwfLS9R25lgSgAPHW_EPptqGzCPYnk8PifeM1Q088gyIU80kyJDW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29569">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe63125b2.mp4?token=s3SKEcFNiCIul2POMpSP8YA-7LHltqTsYv6RPtav89JrE4rfHGUA7MBwgb4O4PO-kLjePfKXYxF5M-IOvop45xNENKyXr3Nn74WbMitZIIr12bnoRWwKm_a1XlgimvE3X7qjAHis4gw2WHcsG9Njx2vrNpXURcJla6NzBJ5rcpM4wpFCU76Cq5A7lJZfgGZtcFxhm2WARB-q4wdv1WpaUt8v0hBj_7MDW6d8taWrQT6LJ3xZfTv0umsw8r9fVovJxYBF650RzsAGj7nosOa2UvXQNUJKKp0Gl03RLMedBUA0qcqHVyYyYtd7hwyguFBH0YylnectyWt6Dw9tL-0-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe63125b2.mp4?token=s3SKEcFNiCIul2POMpSP8YA-7LHltqTsYv6RPtav89JrE4rfHGUA7MBwgb4O4PO-kLjePfKXYxF5M-IOvop45xNENKyXr3Nn74WbMitZIIr12bnoRWwKm_a1XlgimvE3X7qjAHis4gw2WHcsG9Njx2vrNpXURcJla6NzBJ5rcpM4wpFCU76Cq5A7lJZfgGZtcFxhm2WARB-q4wdv1WpaUt8v0hBj_7MDW6d8taWrQT6LJ3xZfTv0umsw8r9fVovJxYBF650RzsAGj7nosOa2UvXQNUJKKp0Gl03RLMedBUA0qcqHVyYyYtd7hwyguFBH0YylnectyWt6Dw9tL-0-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ‌توم‌دوس‌داری‌خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
p20
https://t.me/+6hhOCJLgSM5lMDhk
https://t.me/+6hhOCJLgSM5lMDhk</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/29569" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5UdUGFHq1NlZ5I8iiFZufH3CngdNoy4usS1pRs8Vj9WCb3xOqGUe5h-OgLyM_KAsu9e6Gci9qJMHXXCqyFgei3ygpWk6R8xDkDnmkn1cyvNAJSUaCBOAgC_Y3F7zJbMnaX3rU4FE6CW0-Avdw-EX2Jkp7aiei-0QawfEusGLxsQYJNztyKH0FiWnQqGxWMAL-EmGcj2f0pgfD2izXOhddA35sP28_fEhRgFCKcfm-yMg3hNoL2JYUbRhanAYCt7JFI0HjA53S23J7jYc9bPeByyIx4sh4lN9tK8wr1SGMAyqCSGINuEyxcWbmdFjHCQByAZo3V_pD9QuvS8SRbv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFauMRYdqDDLKZ5ahs6zfxg11sni3OjyNRd5nrGOPHhl9YiVsFOTQXMafANUTLEYf-X2kkYbNDISKskGkXZLixMScsytN3FX6zjPquQfsKvYLND_rs0Ggap0MeNchbqGz_EBynaGrCTjzxmK2qRLMT6kjbSgZPcfgG8cyacNfKP1bSgOBJE7WMqZ3iN_Xm25U1dI8bX60sho1R4AtxGvhwojCbMdF_3qZb3hh6mnTYyTXOgP67-caI2D5ZP2kngmlRb2Ti2PKbyAEPOsw1vqq9k6TBGbEQu559KpJf32ccp-e1yEiiW-8kSR1hAFkw6YtkykL3iYwiJH3W7XtGP4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiNT8Cr1K9GVlWsfOhOLrs2vXSGcgb8FNjYPZEjbQD8AQveFuQiFNMDyxDLNP653p0780iB7hFuxOLAjZtmL1SNdxmppEnX1UhDyW5dWFRDNVpUGmymjfBgezyiN93N8Z7xQsn1e3ozscYMILeNHcCOQdPjJ-XfJ5B8kQ0Obpwzh_dt5sRGsQOizplG7CwpCWWIo4MFvPLMs-3rIKDHsMPeSnigiO7xePFVLnmT2Z4KgCM8qWYSsytdyu--tRvSDJXtNHZ4y1K12VRkXv5mKkABOCYpJDvnBIsI853zCYqupURVbmNmofeWvpEUvdaASmQHeXjjL4ZB9TuKnecU8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2KcstaYvgNQHLDjTuHLjqsBfQTr74tAWNDL6qZwg7Y1tPwFh4HiMuFj7pld3OuoJ9ee3_0mfzZY_tGnSgXWDk4RzwR1quvdsxvJIFQ7hE81KSAWHlpSZblSzjJNteiELY-uu50lXn-7tBveUSGyZ3cyp0Y8kEXrSgDapEbW8PAgxyQVONAbeL1Vds0MxtyyVKeJQyj2bUEgg6BHNaTI9nl8qCOQVRR44VQmxbj4bRoRSsMhVzEUZSLxsZw7QuvRhLRXzL4H0fOlzpHeiuEm3TwP6UjFRwe19Z_Fme7CMUrgX7tgoSvD51cC5EQFPpztMmodcACMCmVB41j9zC_cDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_QWutbpepxJyLbnOUchn24IbFeQlAIZlcjOYTS2eXTziS1b0km0CM68xOcr4eBzqPUUP3-Om7od_O07JmkQUQe_QZlEtNtmEZZVgyh1Ocj_vNDe-iVd38zTR8Xu2ZXH-i3VL7TvH0gS_72ZrxAeQDvUqrHjFSYmIJ9SKbCEj1EJ4g7ygFqn5RwIFUtp4EdEFutpJe0XnmMtgQ0nsbWw5ebeZjOrLaM5hixqGmtZmxe330w30DuHAekKrRVJUPFttriD0qqlyCRckbOZdnWidUZ88MB8n_TsrNS7rP01mLoQW8-_q5uI-cMNRJJ82FYZDP3zYE3ABTLqG8NVChIQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRTsBLqgiZXq9H_1BuAHtP0NUGJhlCQMffVjQg5CnffeDZBQvmyoZh29JWeziBjGpQ1aoY5EkT8svbyQtXP8dZaBL2ElyycZ4v_0swvrvSnwXVEPmL_2UvfaLPGnE-PtTD9s8B23BgcWb-K65tLdU5VNKVCuz2d7Xm3oX-5gyHFVYIs7OvxmquW9fQx4ZeiDIvF1Yt60xoA01GMjv39m38XcwnZO3BNN9BQcMDBTPJU-Ts3duK4XWaymcCKTP8H66_C6nGnGSW4LlkHaROQ4_UW4rRM9f2LYFGzyalAxvbT0BkQPJxwb2ZpQhc9cHbNMA9pOfn0glatSDkdy0u2uPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3j0T1z7SrsER1IuFjOhDaN5_6HKp91CJPW59lAkl7MMlnuIy1O9X-TNRo_ib6lDc50lZ6g7QpQv5pWcJe0KhMztTycZ6N4f3HCBCPMxq1Dp_COBJBhVox0d8FF-ynvalSXcxxzC8uN0ulJpsDsucf08v0kn5B8xhMjfesdt2QqTsfFRDqYPY1XbdI3iZQorD3ntx1608qf7MJimq0uRBmxrZWyFuqwkTVkb_pIVmaqwwdG11KUXoRLuG-wEqXypbdRL-CZA7NfG5RFKxoKWRXy3wIFv9GvO_t8C4Li-BK4aGhOuBRHqXbkknFHFebtcD89Sk1CPgQdbq0eTcRDPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNslKD5psAmSz1BV-5X-zx3x3G8QtIg3wQ1BEZWYL-QguMFAVjLw0j4JTYmG8Mpd_5j4AZym70cbFhucpgFvUuzLYGzDy-dFVBe-0MbKC87LrmYkcy2pybehVXwIjCoPrBZ71_DBu7HBDWODLVhhu06vswJ5XPuwE--NzCLmykU-x5auMT3slqruLOnkiSINW4tnAQDPKgqsZrvCz_F5fMxP7cnYsm1WE1N6GJhdRBCD8I-CFYjGD9FcESrJtTCwflmu0BdHdPxsLkmkVa3GGohm1cNaLVnGm2FGPVjE1GZksYCow6XnJPglgxSN0kZM_oeJN6F4GJ91mAWEWm5oIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZtLxwkyA8L1Q7eWpzaFRCV1fqsOyakyZZg6F3eqHBgiGFn7P2FRJstjevhuHJ55m8UzjIkJ2SVq_sgWk4yeDbGUou5B0nOqWmlqC_a7DE3E3o698coEz7lS5-iHJMBpXjj92aaj9VhJ_nQTj9o2se5xjQgxUhycS8JW4PUJL9JyTHoVMCtnAT-U7FEFnAB442P0Ila1NO28KnL4AMAWyNejYpNFPZogGNei3LSOh2aqP_Cu7HInhl_jmLkg-n3At3Ac3St1rX0c6RZRrYaEKtZSQ5TJbJInZx_zoYJL3sbKfSQvhIg88lZEoJ4ako3NuW90ruyyR2Ze20J6nGLWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=ZfotQ9svWF425OlK2n4tK2oDO5YTgLHrYeCTjcIhKx1-iKWquN_eGB4qEfaDSSn59R0c0Dv4S4M-0x9kp6sBOGpAXKuoPcQtNrtzv-MWs99yTJDiOXrAAKNTztmnJAHShAt4JIz7fpm5ZeDFCo9COnhPl0e0pJZ4VBu1wKVSGSz0kUX-AyyiWFRMzR9AMnXIA9wlOyVpF61pQDcfQOa2-vM1mbBID-5kTH4Xa26Wum5G0_L6lri99LoqcIqPCfdIIQxpzHvANNhFbAhuYoTNZfdm8gz9HA9VN1-E7_T6S_tLWLksRR9DP3ValxYdqM16LY8q-Fl6BI_4uKG8Ull59A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=ZfotQ9svWF425OlK2n4tK2oDO5YTgLHrYeCTjcIhKx1-iKWquN_eGB4qEfaDSSn59R0c0Dv4S4M-0x9kp6sBOGpAXKuoPcQtNrtzv-MWs99yTJDiOXrAAKNTztmnJAHShAt4JIz7fpm5ZeDFCo9COnhPl0e0pJZ4VBu1wKVSGSz0kUX-AyyiWFRMzR9AMnXIA9wlOyVpF61pQDcfQOa2-vM1mbBID-5kTH4Xa26Wum5G0_L6lri99LoqcIqPCfdIIQxpzHvANNhFbAhuYoTNZfdm8gz9HA9VN1-E7_T6S_tLWLksRR9DP3ValxYdqM16LY8q-Fl6BI_4uKG8Ull59A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMBP5IS5B-53duFQFYTCZfVhwvU1l4-nbaQd8VhrkwxxxBCR-zFcgzAnmVTceF-I2iOpv641LCHR17c4OmIT_1ZkVn-xMQtnfbvhm9ydrXtHRoW90JC-AdTrodrMBcCj-Qtxa3fTESnUZa9O7XDx7kWKde-y4qdRmCWi6gWIjquRCOl8oUXjswUfbfoWiQ-B-BLOosw8slwG-Fh2m-du6hsguv-6b2VvNk7BfzPNyLyZdz-g9Ykiepg6WuZQR5A2zUbgCDVdwK79kv6vnWHnDWETIGVmVAydQKq1QYexB2YJcB7_YVQQtf_D7U3po3mQj2uqB5TqfDN3cGyhAaHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOibS_dwLo0JPUYaNsaJcq8_dBhVsUr8rbE9bTdZ3PlE0kPkrHMSpSa9rM7w9CflBGgjYVfsMDM9W4aXDpu-Kxp6yYgAncBi2cBc62PWA2PdkBjnsbkLfdklCQzxIpkQuWTeBUEEZ8w0NOYM2L9LNdNCVi0AHGMt058DlZss3jUaQ_wbDtnpnsq7B2yjGYT7PhdJ8FsUBaZJSPCPPpfis7jCw9dBOxSHN5zdT_EvE7ZbaUSR-GkbCjoX5Lt8nu8RPRV_y-fF5s1KYNib8oVO_BPMF59IRMp0e-nRZdPp5d2D1IcJn19Bq1wOCGgBQkqzfV5hXhuIPLoZV5anywUErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpW9omjGKI-mFKZZM4EBkf8SbiFIseP6h1Bg5pcpu_CHQ352FaSy4CaxMuE0SYTzkwqo8AkObmteTIUcF5_RfMrl9-Yqe_ss8iNPIEQtU4qokVotLwrYc7iNH7PqkxwPMnU4JyNi7ZgQg0J-McOO-C0AvY1w4mQbus8uc7MikIUxVVa8l-Lc6bpZ_5orGBGnlIJTup1y4_Tsxn04VJZEF7HiEAUmC80u_91zm30XgLb7NZGihFT1jdkeJGrzEQk9Ca391FEtLfBx-weeqnQgzmeIHVJ_C6IVHs-0ua8beLq4VkilyLpfgmD45hwVnSvOLUft4A8vRAI_McrV-D3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=nfrkPKhOYs9a0qVfPOA4W1zLfpuwTXPSTB5J5LKpx2wVs4mQU6XVt8k_3S7-k3oz1C9bjy3GdRDEkSRBdRRzg19l5mxtN9UV3hPwqwInfRVubrH-D1Ejt4Dz-dQ7UVCcmGww8bB6Pj8K4XhmvYu28o96pQrGq-4VlUJeYJ_6IKpsJdlcj9oQ1NkEw0YV4o2yAGGrqfYLZwik-LVY1Wge3gFm9MPjWLNq_gYPmVyXPTjYcI8tX5q0wPMFld3B_jQreI8-Ndiplt_6w68HdVV14Q0bowS8wYQmpxfYxtwOFXGkhYWbUqdkZaKNaGwUo2NmI_kYINPdyhAkr98hgyufzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=nfrkPKhOYs9a0qVfPOA4W1zLfpuwTXPSTB5J5LKpx2wVs4mQU6XVt8k_3S7-k3oz1C9bjy3GdRDEkSRBdRRzg19l5mxtN9UV3hPwqwInfRVubrH-D1Ejt4Dz-dQ7UVCcmGww8bB6Pj8K4XhmvYu28o96pQrGq-4VlUJeYJ_6IKpsJdlcj9oQ1NkEw0YV4o2yAGGrqfYLZwik-LVY1Wge3gFm9MPjWLNq_gYPmVyXPTjYcI8tX5q0wPMFld3B_jQreI8-Ndiplt_6w68HdVV14Q0bowS8wYQmpxfYxtwOFXGkhYWbUqdkZaKNaGwUo2NmI_kYINPdyhAkr98hgyufzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSY4el_nTO_vcoZG3J3_XhULPmg-_EebZfABHt70bHJQRAdbISs6wKmAvt3WLG0GCqdfySu09TqiHu_tz7IxOXYpSlztyqNODDt-_FE_UD4aK-a_ePm6NzxTYK-jXGR_vwAhzduJ_708HwwVDOZRkW9EX3fo2t362Ly3o1y0tEivDgsr1SsG2rs0RKnu65XyYetIOyGqV2pv1ctWJoFV_6kQm02385P_X6L8o0K2krAfliMfCmPKP-b7lKKUiUdJh0dNuCnU6pJgUS-vZMa1b7iXJBIrqTOM1wrTEVP4u_ZtCYv_vEfOUW4v8alWY7ig-jxRF1A88qENiW0COSwREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته پنجم لالیگا اسپانیا
🇪🇸
سویا
🆚
والنسیا
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29552" target="_blank">📅 21:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6TJuf-Cx4kNW-_aVimvbMA9BqRii8a0HfnllPlqzA_achQpDPNTNyanW8Wf13dSKwGzSXUROL7T2uY0-OT8fwOqQvhwkB_Y8_0nZDty5Rmz8iY3FPQxYG6GkXuBXxBvLQ7GsVZYg19xcct1GBQZM7yXm9N78vNr2f0rWAulilDa2lQ-t9XKecE6Vm1YUgDTDD8izaipLJgJxzvDtX2EdzrrvDFH5nk5-gSP-eVaDBeCUWyJMMBqHPNMRd2wGE7oY_wuuEpAOLXpvgjq4Gup-qWVx9ggNDJVU2owibF4oXB6kef3mPJ3BjUTM833B0G4CXen-wWuXaaddg4R8Vu_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4FXCy8Gfmqog2QaW3IKRzHRaGtWpkwMShyxDwLxUH6S1733BSjCSez4dohYW_ftAHPyHnHF-F0XAfq55Ufs94mLb4ZBNFOpCH_HXdy7UDjyuHpMYA8ha_R0L3stO-FOw5DV028_pR4XPpkmwV_ObW96sktefceh9M0dQA6c7GKIyzXzqW5VJpdmQSeedxb4Eo3RyuTCnlnzHiG2cQ6oARLP0Sb_kmjFtrpt5TXa1FdTMTyG4M8ECGngk-awZcLZopzwWLd7lnXv2E-rRIlpPdKWwyGiC9QUGuwRgYu2_a_BnFuTeTF48ZsJWMtoU2516Hg_pjC_sENb46zT-pRalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tseDpxZ8VKoYKtg-kPeEzBIagYoXPoyrBQVq4AqL0-vOsxMcl4_LZ_yJYBi93RumLb2BsXI7H0c8mb3Re1hMpD38VwA3xK3Wl0Y-a1P97BaRqVp3GKDYrosb_a4cVP1b8icq1I0r5GvIJruumxpPMM7b4R4Ap480Gn3FXWoJ56bSdtuyROSgGnoFKGwacnQLL0_ScpnaQP_ZjUCGJjyAVxR3QonURwsperGJn4O3xZ7y8pCbptzUlzRwgpyjyBhl4YCFLIUCqUTPz3mI18GF7GiOP8NV774hXOC2teplYYY9NKJ6oCAlG8TTsmWYuGX5hR_FQaQXEo3VtSnyTpXfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg73U5CGEmk11wwxukTvsqaL0_RQ58tIp9xcH2CbFeWwChHOU8TtZuaYwuS0545pje34XKxkBELUjH7JYLOX0igCQI-K2Af9_Aw-gHzNCUuDMGNiLMQiSho-IJzCpza12OZjLm53VQi_UDALYz2GrLIcmXYTMH2NCq9Y0yUS5Ul4MZ6Sc4bxZb2MboZAnEA6cj9mh_dn1Ng5zIwp1SbdN5ktLMdDkXzEaySNMiddlgH6jYS8_wBknvNOQFx6Y5x0OwvAIt2ivi6711rkRMREhE9Ja3-VbzYOTASPHCPFU2P-j3wGtOt01m5ywOsVhj5wU2fOQ82Yhjw5f1_zfibDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXW1Tu70QeFR1iSTfAaiACzHJ_g7Zryi36xaM_Xqbc8uD_JlYUA2Cl6n6hkgLT1b15HrtnvhTRKisbY8qkB_2aT1vYhj_LJDG5jUL4xaLgEg0jjlh2I_symNqfARmWF3eQ_aiIEpBW4ASbqDGX3r6b2k-yxp7meCD69lUihYchg707saHTRayWEjzKYCgh1n06QE9XUkQE03WqkHOULF2Qrz0vFvG0rb7eWu9ny-OJtkDzo3CCpk5gWab-E2KIVS9ufaZZudGDxF8X1aJkKgGnirGTBqQ38U0nhGNoIlHfUTvjhPuneufBUUKZR7CIxNBcfmedyuNQZbGNmo8cG3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgC3n5Zpd5g-4zbhx4KXC3TNOzLAyyjFe6p1Wn4BTStfFkgAGIIH3MIsruoPI6-6lZmgbt3iIk0yWktYWMv8Irmk5n1Iwp_w2WNJ9ebj2Sps9kr8hUU5gAk7ayNdfKSKZXwZTLEVo0hb5m6lTvJV22epEKi5qchQMQToqZWU7OVdOAFYoVMCYS094Vn4k8naugC1EZ_LLfQeNzn9e6w1ObZfD5GWPSjC3kR-jH8wzgzvklTL1dpJSH4OOaGzZx_PiWCmB51lvNSuEv0ZLiJCC8ONkWfw911B5Lj8iK_HOMmrAQ1ufrJ1aKl9rQwJRkfV27NhdtkG8BsmGjWdUN17ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzYnJ77m9SwJ-ZJGeOR2Tg2azaoEmCgsRZr1wGH6p2E0p_gHNqpDKj1IEer-NLPAxBU6jxULY12JGirV2_k-3K52mZdGEwmzUG5L3yz4Hqquzi1TJLGo_b-2I1D_JPfHA_2fWWA4dtJI8gqIQB0bQ91GmIE6JC2m0yyWz-obKWBBdZNi0VIdTpF2Hk413rZZ7lmExKEzkBDlj2UftUwAbjymqGHOSW8i7Znix_tL9f9RRN1wCn3yZ_QJnz6wlUWNMc89meHol0P9-VQ2G7CZzSaZoj6iTmLnWAO52TmqtSka5Q34V82Lx95fC04tN2WZ5mFRJoApWzuUdi9iaYrM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH49KXbswI0p0nTyx1mY6zkzarAAJo904hSx4u-zJSmnkJfs4eywrXTP0ptr8LNGzshndIfJWkiwxCpra9_mgv_DPBapA4foQvVomyCUddLpaS1gojgJpEM54HfpmtZoOTQmBhjM_RJ4QQ4oALxRWGDkhOZsvxhgeh87T-xA1sx6hpUTYVqFYlPxv3jd4oiJnMEdVQSPB8K1sxD5Dw-ldRsqE7EZrkc2JUVkMJhhnhZE2hTHDF2TJVjXVVdX3pOfZPYtV-2J42Wq9gTmIvQeK0FnbEgyiJDgsl7C1YUGtRn4xAh19yrMs5xNuXmkfQTVJziKgplbEbw1KgzTDkrbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریزاول
💖
100%بونوس‌هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100%بونوس‌هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:g20
✉️
https://t.me/+7MwKcg4-gXBkNTk0</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29543" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxcjMdHCybd0JMMB_CocShk0M20zcfGqNdOnvCrAPADNjQxO2aGEUZMtXHmXVP_LwA9Nqhl1b-aGSNXP8EpwjegfGVp5UuiVKbh_lPu7cL31V3BFAdKQxAeFeMBUkET3D4gnrYiCqr5xndiLi-zcsHInN8wEOAKUjoJ7pVEttEKXCkUeDVyqhqJC26CsxNWMZJdL4S31l131ssztlWdSD5q5ByJ_L-CUnRR8bj0_okYFlu4ipSasjd3EaMivuuOJgCIqcIq1BzMZI-bNKEZviOaydesJSvarRSo5PafJoFRsK-sNNAI_k-dY6UnZSQ6ra0rkZMJ-SZvL-3jzy1qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2Q4YfIQynAdJB0B-XtJFbHGb5bW-sj3rXAKEG57K-jN0qCjHpS-7qfD8kGoh63W32d2yEv25_zFge6_hAAS2QO-IGsPelpx2lomqrdSndQAqGC9MXOF4JaXdZ1H2ns3xPoXu-aE046CuqpeidqEPf2ZeZ_lO_ip_noio_uUnUyFqy6HDwmjQE1BzwAmvN86moc62O1y08d1SpHJKIecp_VtolZscvglbdgAn5Plh4q5LtwGfP4u-GIOaVyxjorqpEtmNl8q_rRMplrhzHc8cqhzkPxjS8Zye89a8wr8X8JfkJDS2Y2H7c5cc0ytehMuqvh5RXHb3WBgvRX3o7Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBNKSc6Hd6ZylpIbk4LDvAoiEC7psCAPk5Wl5jGRLDry1yLNcO0ImNTh9iHsQfOBkd1JHHRawC8uGhSgO3MXLaNnTjjzf1LZVbCZy_ZL8MMd5194lq41y7ROOlJ9f9H5xAL2MI9ckHQoFg1zgVbgkG9wlXNsxjizdHzffBVLUFWXcU0w4Xmgcyv596GbDzlqCfSl3vQaRGhLQJBGt4t6QK05Hq4zJrI2jVvYeeNdkpt8KquZxtoujWnSVeii3BLzEuKOjK-I7QArbYHONGK8rxyLFBKNF3gXcQVemLMOwCXizk6Aw2XDF5RSJKO2QkXHaPwopcE7-qHM48dzFY2qZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=AUFEpWiT1nXasc1gCFEY5O7FM3xli7hoenfEhP5OyCagh9OBd0tW20-ISKtUOmlLDJAtJL1oEupcTgegO4LCJkwuwGHCujbRBMmT5Pga23GdPqzpGPrFGK6oAdsIp9uf7_Ra0vYiVeR4ZFiQk976u3WEv13FTCijFbr-OfwZIPpqH4ddVQLxzeWpgOkaGoEdYT4Vndeu9n10OMXs-1nOq7BxloBML7J07lxI_t5tyyhShxi-X-hytFJ-G1P2icd4Y4FlDK2gb9-45W7gLIclh0vaveb3QVvdE1mSCuzmCe0YUxDHtv84pfcBPbBhnd_GQsrIYmOEgxMxlnM0l-_SNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwBjM2XuuyqRtympqjaJgR-0NPKJ6XRhN6mkI8OmE72ezKIC2VlEnRekMkqjSv4PYjMDneboyVt1FDJ7I0T4kr6l0may_8vlCOkf7VRpq5let1VkkzKD5odEi-NDwWHegCpuEdRymlcsURkYbG1xFB6aw6Y8KqhvsViFP07cCMZUUJ8B1AMCRxxDWy8lp8y1FDPAADY_b4VSTjaFkLw63QzsA5K0U5nY-BhoiMYeoAFx67ac8FLtTv2m9pxbqIaJxfqhQr4BsIxI-pybXv5_SAep1X3OdpUGuSnMl_3FLM-lZq8QLf37IClF2sUcXvoIKvTo4gZzAnSfvsGSN6EWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=CdyBquaifLGzmm6XnjVwrddyPqc21Y1vzbE8pHxqSe3yb1iArdDPyScTaGOaZ2LlNfvaJ42sIBVNwETvd4GsU7pRDBFJtXYMfXu3niqSj8Lh1-T2OI0bjuQ8N7X7roN8fA1VQ69a77E8ypvliWvjrFqv9hewshM2PUPwxex9G9MNPTwB9Jm8ZlEQHR8fdtJFzGlMCXGEiLJh6zAaLEqMjXd13Y_B4a-v71i5-A-mkpCGhTos5pQEE7A3m9Tk5Wqice0W1R0z1NvWvIF6751tSsjlKJANG84Z_JWzZW1DrRYgchiCiTa4GxH_WbKWJtcBWeh77I-qeizgxwV26zNF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSS5c09ZBwuO2ve_xawZPmlyCMWHE66DLrCqL0JgAL4rsrbXoiuz5gM7toXWdzkitpt8QEQIHSBuuIvWmY7MrsVhYE0gzNXtSMi33_iHHQ8MmXC_mioYgpQR4ap_w-5fIANmpMKQXxrMPCkSvveyo1h3JRQ4FmCZ73FQTNAbyrtMY-0VdbpCPyjWw3-5f5xacTjJyptJQMt0GHSMAvJWedUVQD5kqfVrkqO7FqZXKu1Zt9dOlr9K9K7HKYWK8hBpVjDq6AG6ZG3Dp7u3HZGuwsavusF0MXpboLC2KlK1UikCO4yeVwGovxOFQPSppNqky4IzWO26XPkax6Q-l1IGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFreexE0WqW5djYX7ex-gH6PDilVaHiIdO_EXhLOpzV1foJCFq3SnZtQ_TFdc-76WhIoDye3dFNz1U94w6bg4VwlSgkAuVTrw1OJM1gSVN-xeePF8d6cRHdJhLN2CaaGlw3FgkkTd_ZBqzyCHERxFIbUD1B1386Bao0_KhxY0jxW8yppMFUZrXCAasuhykIkMzhlDB_w0mrPDPfYimvZPqC6yAshdDE60f7TBRgJtKFjxhrKmj9G6q4RmgtfM82m99AiBy1SWyH4e_w2ui4XeoPeIw39_sqcbHVyy_m98Ay5yQSI8V81GK6E6_kcEGg6t4dKzDDLI7jZUpxcRtR24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJTg_4JWhJMutSF9juR6v-Rx5cLiBDQtajl6fzgShEY-VxBE1hG32VPMKd66p_3TGE2Uw5f2rG_uZkoZNtwebfd1iUdpwVFBzIPY9lp4oCaf5T8gM8COxceDj5IB3YPdJVJqGDiiHcSriw3YD2AZnA1tJ0q-25IrYPkjFtYEpyuvdufZS7nK-ujz6CYUzaTCn5Z6s4kSshwJTt4zCY0YLJfBNsjc6Cr4Nu1T4tMASS557iRJ5oScfs4BSYVhuyazv3ppJsletOkmRS6t1nEDpriyns3-I0qoGximX53FmL7xy63_T0hMq73PjsVyQwBl6gjculXUYZyhDXbn0d8lDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQEHSIGQh0yonWPhUzrLjLdL8qCbrSSwfKIx_6VHp6l4WdA-VzHad3Wbp6dptdzFiKPHZKtOeqWCZZABIoAHJx7sdNw4X42e7MxtrzihI7YtmfiG-TOjpgWSnmdaZ_XhadxRojcCMXBJLgCB_-0tIJYiTr24tPhglFHF7Vk4nf5GElMK-R-MX1YiRNnnB9ch5KgGDfl6_Q8zOJPukjEO6hgJ3rEufnD9Pew3KV5zOeoGbAVq6gVxByFkG6D2WeH1FLQ7PlGyNFR_ng1jJrBQpj1qB7gzJdNfMX49irbgZYnk6wulH_mxgovptPfFZUbrPrTMyO8Nfk1l_eLrF1Xx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcOnzwTubvczbZKDNId8hvVMbURi74q4ontiv4FzGyQmURXi4PFsR7mhvuPv_lzDR2GLaIZ3bHHGdBbMCJoDBGgef6eV16wWjeU1i4Scv-iHjZzpkmpSU8JXVj7V6K40aqm_Ayw93xmvMm2Equyu7uzdYKV9Pg2sR_4NhuEWrsRekK-gCxAjgXUmJhQcVkcH_OsYKUjeKkQ_Yf3I3OMEa6aAbHxKXLLyy-hdWbCUy6AdkadyXptpc1biVsMWwB4vLo2i-gpSfl28-5Pa_qSURzpiNthP8_b5wzf0raP3CEvm8VpJbWj9z_tMQ4XIO3rjRQHCjWG_v_7hkotwZW9eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnJw2w4DJtno8WyGWS2NHq2uvpo05Qh6Xic535DCJWWqYXKzm8Drd1jAYm0Y7guJ09Jrmzh178tTukf4OSwviEA0py6_wsPe4ucWmcG-xRM1FGJh4_O1y3chc9Jh0P3XCeCOJoYyA7wbiZGOxwGMkcyviADrBaz2jd8DkLPjvAkFDtJPL1TRGupvCm1pON2Tm9ELC_DOwMkSDPkqEh8JKHgVSjH9QGhTaF1gt2IPUnuUFFcvGjXufTJdKAtXx0QDirLfO96v6Cuh7e_rqt5Z4nzhuUcGJcI_5kMq1L0IdxyfjrFCF-4JFhK0eEmjQR1kBbTkNaiiZ9Isf08DsF3byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ونتزیا
🆚
فیورنتینا
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29531" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlZ3m7HcstAgGq6u2zIswX5Ocnw4_VaRKoQl0I-Hx5liFrRXGmQT9pROxMVGJ-NcQ6aYCdjQFcR9Ddo9af3ZC1N1QftKhcbu_68YGL5tgNz1WK4uFXHsar9HpH6pnmE0h8riHe4ZEB_l5o9Sz-ouzpNJydSJxsSnJwBsRh5bdCL5Kay5uQTjdHgaAlzNu7pnr8-h8fNV9FLaL_S6i1zaoLy510nTfASg0Nae8w37YS6M0e387qQYNT2RdTUOy0wyVfd202bmruCrDLaEChKwOE8wgwn_nxmL-eFhtUldpMdkKXCCE8y8EO11sYsVmxCSigbNdssxSKYR6qKMNk9Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ0RoWd-uja-3y3E3UU3aXBOfuBRlqlD5I6dHEYD30MX6ll5bpIkTtZUhx_9KrySE89BxcWMKYP_PTDTc7TFHyoJNvlUbWgiE-jPyC9mo-q5VBTujmWhci2e276rWCTcvLIW9salSUz7HhxVuMU9Ere_c77XcJLVRF4G8SFOM8K321tjkz2-pZy5JF3fKeWx_OZRtSOaJKmabcTb2UhazjXO0LZniN5ib5fKp16IZwNFZak6AMsqeIx1AJd8-sUbNMY8KM1r39I5LG4-FTHurWTgTnlu58cUuCqTHyJPnct42ECKzCWhnt7j2tOJ2tklGf5QtzK9KBPzDI67vARo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzboc6U4X11RlH3G5ZhtQjv5EgX1joUiAsrTcFja88QW5-4DD2u1q_xotxVUk4JqR1LfNbQw-cZjf9whNZAQLhit92Iq5bbM1N67h90PLnlQntaqtsL65TdzPjR9d01pezB1H6I1iYIQ8pv_il-dFZtEFztGHmRISFd-ERcycGdz-AqfYMK7uD4BS_STvBp5dODAl1ITmcz0pavHDM1eLGpOEDfP6xxVUlk-Pik_FpUw9Z90GqrmxkpJ4aiGwiUUPjzDkLweIs9ouMkBk1_vaPc0_i8vX-d61vsnDlrJhPXjBdSeOVoPv88ruXaC1FmfmsfHuW_bw43AdT5IUYH2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-16LJajKqUzJ2QQgHb9jVqa33w2Pvcvpxs0HE1DBnyrUTSQrRZE-9r2cWqCps-6wLZRYyf6HoWt49sBudEHl64PPvzvGtG0Q1NEwvdX4HsNd-S1te2BqM6afjLu655lobu-EghEvuoHJ_JFLcmtb__Yo79Bjfga592sm1sU6_WtaDNTwsSbi2z9vZK5Bg61ZqQu-ErUy2d5a4naJ0EJOM5b0yUbf2p587wz9dxdqrl00UnkCEsrgIwRGPrjzewmz9YXOycYTmgP6sSyGdUY49PGzZfexHu4NUbgzEOeZfgnDyNvIgiWNtKFYVBX5SkVBwTNn4SDwMCN_NM6oZHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPy33Fsj0bR8V0MqfsAAMGhhCxkDQIAIKe2Y3KMKBpGRH3SkdVVBbEh6myOxxx65ODO6Mw_eiqbFrGg6ERx6bF1QmkydVa7XOEHV_Ct8tJk-OTG1WV1fxG4ZMHShR8vkNSZc35Ym6c64oAmsEU6ynazlipw2jwRImCwop5QKfeDenlvTN8S2zdfEFhwwCBMDSBpuq4sUSJLj6mJX4ZgodfdEnoWjbrll_lt_yjzo9mrKoZP5vIxcDzFH9-9aoyOSzEQCMi0Q5j2ruxcqguRkbvpChchhcP8636cweFU5RX3ASehYdBy6e__IBLh9PTkGub4n_ZamLxTC0C4KQccVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcOqjuaw0ozs_tmLUvj9Gcqkkn5c5X8xU1j1h5n4QKb3NABHVljFA26VfX6R3_skcmtMJjyCRiR8B9wTKr1LZQflvd7Gq3KxfmHjtt9ihxOw9VPcpa-hBmrWGaUy0Shn9dIzx3VALJjSCi0iXynI6_i0xI4F3nZN5fEut1GELItw9jTU3hdDfjcvmsIxUQF4S3eDcmIrh8UUrDyRwDSp2KkP5qEmoEeJ1YFB722TfUSgmTWvltKq_gXUZXujzSZpYYuG6Grc4pvN9mUi3-Ifr-TTLXJG4W-avTmoaA7WA_teZRC1ikDN_cg_q6zP8lIMivC9nHWRCyaIxkhKuklzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHhgE38MKs2fQJabHfAuDehKJ_IVrKqmYGtXi1MtoWepo4SeNeAEPXUckoGLXgI-6SpqLxkiHWo-0ERm8uk_D3hfajFwtJ3eorhdwxHUcQVpLiMir1nMXPwLIXNPOFZHOsroB3dCMAh2B1mMo9KdP_p1YJ5oSY1ejHLqX53RxUjHuzY42XbQJj91Jny0xhF6Wdd72sytvQPPNBohqzIbXrSWD6a2fZHq8FS5Nod2HAxNjTX3PYPgWqMZK4yLwGJ-8LiuwRdNbHi94GLVwvIZ7lRi1Brz4lBJiaunKKYSCR54iPp-dq-TfyAlj2_OWzt3XFC_urAfXfk0P7GCyp-WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7MqCbQH99GDyI6ANWbprwVRqiR1B5Wxk1eaA3gB4okKHs4fkOWQg-WwtCiqahmAk6Qlg-NHsY0RWzN5Jm_1nGRCp8YPYwJjyEHGpMxfyB831uVUFAjUMOlbnJm1WneKxPU3wUl715eIhZdawdw7AurwAtmRcmWwX7ydlia8ljBBmyc53ah3WFf_YySHfcnaum_HyroNxYpWQykOkQ2dKdHCFBceUEm_eOkldH8OXCo3xvKjIgouMox9wQbTgVrCG2EkzcOVr-8bdngJiCAbtZFbLrU5qxdPHRxbpBXljKN83bFQL8XlC7c8XW_C4fKFZZkZWHRcs5VF0aX9yy3P3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IK8VPpTFJQ9KqRHxe2fbhimXV-MrHL4vP7oIupkTKxVOZDwkuCPm1G-vK5hnAFPNkHmSgyqC7my1emMSdHyLs5TewIQjawXS5NUpLiVK7nvPXrEI_Vjx3Mvflf4k_OErmcTmV9Wm3PlTkVLwhX-jrAiYSKG-oqxQX9y7cgnp3PXzstIdGuu4oGjjUQI8nMKff5g80p0jGfprgORSjyEoy_5oFCl6m2N9Hx_xTiCkVIqQzDTBkERTE5BZI2RwNCGHP6_RlPfPR1A-RDVZvzKmk3zYDm_Dkuco0NtUiA-fp2IhkWj_Ya3m4L5PdLbSfXjgkA30sg84qbKAEczRXYfabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lz7DwxhoM-qkYgHkOSTW-cys8sXr-eJ5r-JCKQP4aogYbhRScThOeTw_-7XHso2jp_0pme7NFp3WTc3iGg3rdhVpqCi66gw3Ow-HMUU6GU26o8bsD_MRNQcwRNehr4ejsOAnSZvHSrUXazRJviAwRdezzbmfPq01mQG_gfi66Uf_rMPIgCKpidJWyA4HUOXLkD0A_bd0qHaUQB2uFEga-ITewLd5csgEBGcVY1rM_56aLSNKfkkZFfdgVH2e7zshc6_vx5rr6m5VH5WtBKGch-MOTYdiS37atKYFnrpFQ2SZfNvStnYWVVpfnGosomD5WHN49EjRyVE24iTsZ7NR5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqNpgEK6gQronjYVxcu6AmRpjghwFHeQ-Xfb7U3gHzJc6pv-9XwLo08adql_D6-eefY-lZDH4fwkANyqN0kJqDq-OdGVQDYNVZDZsgLAzv5LYxHZ2hzzgwiDnBBRiIdrCad42iQqplA1LvZMVpS1Oi1i1KeimQtgSb68UicX5VfVubQm6p3JmDuG49UhGnzXWDGSjsN58DTP6CXBmkcWQtgNAiRHromE9CsdRYOo4i74EB5lGxtYMZu_ui1ufvIMsEn_FEKzLJ2VHC99mx454PyIKnzHDJVj6dTufB57LUK8YiHf4vhEL94TV4vyBKN_UCzi3hOD2Q_KYFRiucENDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2FfLcRbCmgcTgJBSpfM2lVDua7oXx0MvjDJ1ESLSVbejHkLiK6pJPZ7jcpVvRwMDSBN7Sj5SqUPbchCzR_3175ZkN3V_ytt5LaVTaFG8TYWKZu4nloToZfjoTDQ8npP6f9eY_yIn2BeTd3t1AIQlGnzV_xAf3QQAsjXb1VVJ6Zry6q6EJa7D3taEy-G9akA6qG43jzSM3EOvzLQpw2cbktW_cfETiXV22oAZ0z_LbNZfhXiwLytcPjTP32vgj37kxbw0kgMeXKUDY4I9E5BfGs4Ti8DXsway3yB6hHcbaU4-TT9h5_xLhdFHmPBqXOaw0zJnVtzdttVnEDytVfUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJmGW_SolXxuv5kTIv_Wx2TMeRxKosnIAM6CvyQjGBaSLuiqWjeOeTJavau3iyexVtYWgKOl-COgh0NjkocruJiRbsPQ26RMluyqiQmVTUkkyX-EpzAbdfWAGlzGnZbsutWbL71cQTveXdEckPkVUJ7X3aIJGaeys9gxwX0VEDJTdysEsToGsx9EoIhTynDeKLhpA1kSFN77hlhh7P8bOlBHXQauC-Urnir4beWrq7jl9ALYrlfapsU9JGsaZjIL9zpznsu2pDYOzoMKVmLUrfz6cCK05Jl-9DWyHYKbhepswjrdS1PZvyxg_Va1r9XK_Pg-1m4J-BSl1YW59kwtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9CuWr_6VVkV_sYfAKQ4x0THsWx0JPi0uPfg07RYfAUk6vbMj1GXq3OKF0sDeUj_oJoKxjA0rJ9l2HjCoD3r3nc3wV30-JUZ1P-ki9oEJ1x6fJfPHtMOgcigA16RLJuh4s34AIb6RKBd-9xn7AqkTSb4Tjzr1vUdAyUN1ocIk-z14ll8OlDdoIF8LVAQWZ2JtduAY9ck0j-NzLEssTsSAU8Wh4UcOqczfdravuQrmCwLzfclPJbbpK0YTJXI8sVfQFNY3NTfQxrKrWaB2Pt-wJG-a8ndhd29ZGwWOGpMZWX1pP5kI2WXiGQF3ChcdUV38uC9Jt8MQ0lQZB4FLGsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3wkhJVRbLFLzI33JQ64cIeL2MYywWq2k7dYudYPz2eKHnvdj4jtVE6l7E1-FDQCCqolFb-S3syiQ0j5BdSbYYydajYyHjkWeIYRzfhnTmEoFFsp8RSqKlcfuATRpLqcbXGU8IBcULUEzi_TgJ1EfGPNI6YzbCEpt6CpKJRSJpdUoWq40lFBmOrpLflMlexj4crshR5YWjcqJ_RySCL1-uMIHwWBXXhbJ5xQFnEkjp2zy8f2sf1lacqTaNG8uu_ENnb20H2dfX3b9JTDC-BdrLF1ZBfqvT1rCeV_BVLqp1lh1gpMJ_pxu-cORyY9_Wi9m33XtdchSHBdhw2lyPEdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2CRFjQ7KnUDcDgP9cOsGv3m2Rt3jsPTXKVkJ6F7yrjKuMHZt4hrY_ijH2tio67fT2u30eWsRycuZYpGKEPyJ3h8Ji4a0_cv3GS7mtV_AduyOi_WSfYbNYe5wheW1mzUf3fEvfnJgOz5lz0d5hEMsfqSFHeewUZQ_6luya_2z3JNhdRqwv4yJolp3RidhpiFA-QRzVEYa-sVHwRvIf7lXgcBb1xBFJl27mr7HgJBKnWi6C_UVMef-i0o-wTntiqum-h86_rZvXsstxLAvfGxEPgIHPT696sx8ZDHb6JzxGkv2Krq4qdK-5soizhD8WokATIJvvVisdjYSnA6SU0yeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ30_tlNYP_9wefwghcNfOyrpu98VCCjjqjjBK6zVWJfbm5WXDjjle8ukDEXmV166mTAT3MBURM3bQ1WI1CXsaUuPeEGe9GXM5PFOayId2cYd9JBhl-QI2uZ-uTsItcmxH8p7qWQIc-9EpNP5Ty4SfkFUATOkfxdaEh-rkL29Q0NE1oU3xSQTkOHUS1rFk1q7Fkd6miVuTCXEJSSUzdTxln2eBk-KzYSAmupYWyfraOHqpJ_p518vF00WsB5tcjKND59yLpixBTheubdb088Q9nAYxkR58M8SAYVRcZQwAxWcH5RsNRN65-BgGY3qsGADHTDhQTwESWBDHloMlsjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=AC2Um6i_eGqmPCneEc_Pg6gNLtoYn0zpHHZxAqZxCM9lIsNxgZ-yGd_b-YITfuclXb_tCTpai_vyyh4l6leOupImVoa3vqDBW2XQV8qAoV1loaVireJKJQz-HrwhfNI2BAnUrxL4qSrJe_f4KfvJGCc2Q4nurPlD_SyDTHvhFZ7Y6RBE7ExKrTRyfJgZbu8F4g7HY7tCdnysg_bRTPTxnWfRAO8On2vtLSMDWT0fVeQabFzUfvexSLfJlw2vkS2dLxvX3v-IuN30EIrJfLHrn8A556o8XW788p4Pr6EkkuTqnuAVguF4XeignQNQBwjSW0-8Qgt7cFQUD7mA8-3Uww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=AC2Um6i_eGqmPCneEc_Pg6gNLtoYn0zpHHZxAqZxCM9lIsNxgZ-yGd_b-YITfuclXb_tCTpai_vyyh4l6leOupImVoa3vqDBW2XQV8qAoV1loaVireJKJQz-HrwhfNI2BAnUrxL4qSrJe_f4KfvJGCc2Q4nurPlD_SyDTHvhFZ7Y6RBE7ExKrTRyfJgZbu8F4g7HY7tCdnysg_bRTPTxnWfRAO8On2vtLSMDWT0fVeQabFzUfvexSLfJlw2vkS2dLxvX3v-IuN30EIrJfLHrn8A556o8XW788p4Pr6EkkuTqnuAVguF4XeignQNQBwjSW0-8Qgt7cFQUD7mA8-3Uww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=IMXeKfe0Brip8kEGV0b4gjun1R4rbHJs4PMLVp99cMB_oHJ0izGEAT50gXZ0QjTRqO3wlp3CJI3lsYDrrbNwFFLJkKniI4jllWrAVTU9jUuLpGvoTCDDpr-ARdG6DAhnN2NmLjEc6EEJR8c57NJ8uWAv9yKY16pKEVaamq98vVft58j7j601NcTklvGC6oGkLLmlM-nHYwUoqc-FOC8KPvcF3vPWGXrWYu_w4JvEoUAPcWfabe4QI80BREtDosyYtgNaPEQVK1dQUwOSAjAz1YJPEkU01H-AOS4lhC1MgdyNe5YPzdPIxVPki9DjwcStBVKl4VVk6az4Uq8DWcyfegLMEuZRiI4lCS0WpmX7HKFV6OmCSkDitcYJc9jv95ZixmFycl4oTiT1xKBXUwmBNX-CHijM5ErRHc39Wysy8_kxqEjQwHfrIzkfhIOlgiNfU1F8_mPkdVQFQgoaTQneXeijuZpNXgOgNex8VStBsgrP0Badx9Z9s5v8Iwkf1lxZjPh7AEkA1oFbcl1g2WbYYGbF75oUoLurRDk7VNiGH-wZeS6bt-o4fRAClR-1KTF2y9OKzmYVQnQJp48FtdUd6aTuIVPQv5Ihqz2wjQe8304iqCl2QTtGIKv4NYt2h38Ren84hA-nIXC1HmK2Wwrt_37_IPoqODCQtr9pV8nTZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=IMXeKfe0Brip8kEGV0b4gjun1R4rbHJs4PMLVp99cMB_oHJ0izGEAT50gXZ0QjTRqO3wlp3CJI3lsYDrrbNwFFLJkKniI4jllWrAVTU9jUuLpGvoTCDDpr-ARdG6DAhnN2NmLjEc6EEJR8c57NJ8uWAv9yKY16pKEVaamq98vVft58j7j601NcTklvGC6oGkLLmlM-nHYwUoqc-FOC8KPvcF3vPWGXrWYu_w4JvEoUAPcWfabe4QI80BREtDosyYtgNaPEQVK1dQUwOSAjAz1YJPEkU01H-AOS4lhC1MgdyNe5YPzdPIxVPki9DjwcStBVKl4VVk6az4Uq8DWcyfegLMEuZRiI4lCS0WpmX7HKFV6OmCSkDitcYJc9jv95ZixmFycl4oTiT1xKBXUwmBNX-CHijM5ErRHc39Wysy8_kxqEjQwHfrIzkfhIOlgiNfU1F8_mPkdVQFQgoaTQneXeijuZpNXgOgNex8VStBsgrP0Badx9Z9s5v8Iwkf1lxZjPh7AEkA1oFbcl1g2WbYYGbF75oUoLurRDk7VNiGH-wZeS6bt-o4fRAClR-1KTF2y9OKzmYVQnQJp48FtdUd6aTuIVPQv5Ihqz2wjQe8304iqCl2QTtGIKv4NYt2h38Ren84hA-nIXC1HmK2Wwrt_37_IPoqODCQtr9pV8nTZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=B83m8RYXlsmTOYabPclhS7qOPBFmGusl3SnaTXMpbNUQlJ2Cq-INP2nkShVDPQrN_KUHbuLSAZPILONjwLayBU-ctgzaZ3wIbd0nZJUWVMDg9X3l8LJRf1mi2VHa9_gC5gQcyGdm5-lEEyuzOHt70t8iMs1_Ke3Fj0rO3pmyI74dLzvzcHQe0_1dcs9el4UHYqLuUpQsPtRwUArMrDsiAH6mHGResJzPSW3hmWyBXlkD_-fmhasHjbgq8XeZbtHTKufMvqLuoA6lADHQZ81QSMOhKWPaRX8Y2_frp5716aD_qcxw0dGVGBSbNKPKa18X52v0taKD_4r9cdRC-cGj8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=B83m8RYXlsmTOYabPclhS7qOPBFmGusl3SnaTXMpbNUQlJ2Cq-INP2nkShVDPQrN_KUHbuLSAZPILONjwLayBU-ctgzaZ3wIbd0nZJUWVMDg9X3l8LJRf1mi2VHa9_gC5gQcyGdm5-lEEyuzOHt70t8iMs1_Ke3Fj0rO3pmyI74dLzvzcHQe0_1dcs9el4UHYqLuUpQsPtRwUArMrDsiAH6mHGResJzPSW3hmWyBXlkD_-fmhasHjbgq8XeZbtHTKufMvqLuoA6lADHQZ81QSMOhKWPaRX8Y2_frp5716aD_qcxw0dGVGBSbNKPKa18X52v0taKD_4r9cdRC-cGj8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29503">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇫🇷
درپایان‌بازی‌بایرن؛ خبرنگار از اولیسه میپرسه میگه حالت‌خوبه اولیسه میگه‌نمیدونم، خبرنگار میگه حست‌چیه دوگل خوشکل زدی؟ بازمیگه نمیدونم من همینجوری فقط شوت زدم توپه خودش رفت تو گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29503" target="_blank">📅 09:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRVeyts476YEmSxheJxUAKWtZZ0a-wjqAvu86UA9JDN2z-vXPF2pi-0XOWsnW1TXY3Qes5Pe8gdVeAaiV9_HsUN5O89rR-6Yt7K32MzEBBmVe3E49-pRH3dreMVA15j3d5Azcp10_Ij-3ULGaLhR-OAUH1j9bRIvy63VhSVjRym2XW-59iz2VFaWQiZ6P6T_54EII1QZlPMDeGbAPKZpmAjYdaXKBjId6-Rfp__p3Iyx9iURtWuhXPn-OC75_bqfIHp9XAd8gx8Z4NgQjatzyP0o_-udy0Y7SEQzMiejnJ2nVe_Joo9qGqtDnTVmCEPY6BL5DeQq3P1v_QIfzdg3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=nrVKDNgVjWNT1SLJiE9z44S7X00iRIbPeQcxv5hGZU8Jqrc_S5M1i_EmD-EwD4TtRiIJNlqvYwQwEW1HWzdAksqxYdio5fc-lPwRthTd8I1XcosqQaFxtgt-YxrBgpAINrYKr3X7Zo2WuTJdnU2rIqGDC68OkJwAyOf1vbZjXdOBQ5RepfEmAO7pin1OGLLtLwO3IT4m7EXF9TZSQGYCTFx4d1w8YKJZkssFKI_Q0NRRh4m61OajO9KD8kvLnXC1IgG5rfF160dbeyd-dtau04YE3EBDzoMS-K64ZLqGqgomyLoEQXP5qtCIBkrmOa0Oq5A_JUsEX7RlnEiFGGXedw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=nrVKDNgVjWNT1SLJiE9z44S7X00iRIbPeQcxv5hGZU8Jqrc_S5M1i_EmD-EwD4TtRiIJNlqvYwQwEW1HWzdAksqxYdio5fc-lPwRthTd8I1XcosqQaFxtgt-YxrBgpAINrYKr3X7Zo2WuTJdnU2rIqGDC68OkJwAyOf1vbZjXdOBQ5RepfEmAO7pin1OGLLtLwO3IT4m7EXF9TZSQGYCTFx4d1w8YKJZkssFKI_Q0NRRh4m61OajO9KD8kvLnXC1IgG5rfF160dbeyd-dtau04YE3EBDzoMS-K64ZLqGqgomyLoEQXP5qtCIBkrmOa0Oq5A_JUsEX7RlnEiFGGXedw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRrcVlhWiTRn3YmMyztnUo9gi2I-8wP-xNT20mgXnwBKdvjgEnbsy-K6VCxMbTtzTL1HKPZ2TIGJto9G9W1AxAVKM_2v2vSrGVP-Z1rM0gkHhZx-qCMvloCgdH-waZ3jjPgC5WB5bEVmFzdlj1jmbI-R5G4r4jUMZke2VIOk8B4yhB1KIbh8Adef9dwkaDyhRo-PNjYX9PDnHXSfdOw4M53Vttm4MmrMrqADndANNuTDaJlKp8OxKqglSLybAwLya5zWzpDpGd8snMwxkQ_2mo14Pc6Z5cy1uod4Lmfnhe-_UDtzZHHXI2-znGYfMwh2OW8LUwivej9MCRUbc7xBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWlagbdxiNjMpk8frtNpNS759utNUN1jvBqMCMlbpv26YtG1Ts_2U9ubNopk5gSKAQ0ILEGfauZKkqVdhvbrfvtt4_-vVJQUwMJfJRdxNDdbeKdC0rECu4OfUOUEGKPY1oyMinea9xz3ivHXSoQu69eTKnksvQHTGN9p17TN_BbriOp9YlYygX5TVuekOpJsXLTgto8QgYmo9fzgCB87MCgztknXwHjaGX6Nym2b8nGcBvJjbhnXsG4j8vpekxomB2WpYqLp0v4tJeFgJHCtsTET6gmiOi1jsOG3nzHINN8P0EG3SMEazJgD96fvv74h6YZWhM46Nxg_WsgzoPgDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDeNjkFvYlgwh-1PQXWqILZUMR0w7nXdHdhtendtM659-XqLffIU-eHR47aLgmbJLvC5Mb8utbm0pAep4Cf3ueU4g3dmf5E9Nla9szBC5f8vj6xOUHvK3UAHa68ODu_G066MbDNMQGo2iebWDuW9wK8iqSprLqgQZ1MX1SWeJT8EdChiwNeWGE5Ghih-EuA8TR2kZbO0uz8am3_HIbfyl5GU60N7Ei-mf3LaJLVaFglh2Edi5BJ99_63fhtpj8AXZQiqCIqdF5G45DCYwaULyViv1sEb0OyV1zvYM2bbIKKDKLzQVKMCHRhPHThrC3RTIVmlnz-KSP920OCD1Pp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0Vvkq10Y4lELoMPBx4jeExQXbbGBrPF7umdQurqqds3Yc-WsxMayzILm4EcmyKARsL-Zt0J1AGQYZYWMqtrHXn_nyKiLaCLhiMxR2Wjzat-7S8kkrBgbyZfprwv8A8rIDJKwQdupipOK8o0SixWVA3yZQRpOths5NQzl72kAAT8J_Q4Wh2dRgbgSGdNEIzrFtfH1LUm2LIkZ00CTb-W0sOSMWYRTWq5q8CWqjrhkfNpGRkAS1ScNoTfYkYA-URzXT0ZsD7bwxzt6P5Knp82_Vh2VNBdcarYf9UvOzTStu5-tQdt7fF0oiAeReWDWtT1sFntv9pxiAokgYF7VPhZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp26AWuiXdixOKAtmjlkPMJSO-1uXup3TV5bfp8A3lofeVxtQPXouULPizasozmcD_ooG2FvzPnU3z1w_-WDdS6s1HdPnUY9RTixdPgZg8ajOlYZHoN47NY_lo7LqshM0ll6mgT5QM5gQ7-psoDbDagR6Hk3bFPQNpa3YG1JWDWr3df7-Vsj3SLB9LcQnrEnp_IHnGxfCC9DWyAC5vUbQ96BSZ-fV--7hY9uCx2XLR00fH9zreohr8MwXQtwBT-lDXbmFQsw1yg3p2MEi6eX-cqUyMs1tFShC7FFmrRXy7Ral21Bm0RT0KTSgRjzF-EFXRRQzXrx6_5gy_w5zzUUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1mS0Y7czltWUcQXePxeaiYaZJy9BZoLUJMh2kGDHHmH8_PBp0TyB1ySi0GOcvmx-nOtDYFk5xLz0K81r5gczegXw1uA5jiOCag8YjU3O4asPrpNH5V7TU14FssExrtpxrB4AAqEOJLxXU_cU-dM-iuUbgqtKlBdIo8Msa0KVICuP77wsMIqYKFJKK04T99LEsA7Nq7gInrKwhjMzM5uROCfoouFqM9bunRaM-R7dGte4lRzPcLV93d84WMXbiWFYzVBVMzs_ZXMe_L5UXdfxChQJP3M-ajuOOKjLECj9vXZ8BI0S0hELGD_qOoXRjVq_1SdAsFmPV1P17qUJSRGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QardO9IMegNtzXOx89HqN9rGV7EtbV7qalBlYhRe8SKWxAKt4A04T3v4-9eX_hQdTp-IFMlaeg5kEfkwRCAkZ7aHIJFd2KGL1Y40pUu93Qpze2mHjZuMlWAei_I7mywv7w9pOuj7hZWhbhGW5Jg6DHr4u1KffUczUbXmgQGtvxVyXpP5tKV3lkQit_j5pf-G4ooD_8zYED7L_Ob_0aHc2SvRC0LP7SbKdk30u-oLmOy0bBiZPuvhud9LbW1iWVmw3qSo-6AOTh9ulDc8NuEIMhZJakl2tPlXwn-Sse-FYmaMfvvBALkryeKC2Gn0laWh2M9dk55UjfysC_-mPEFMQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29490" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/29489" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjcBTF-nDfmLny1_v6k3TSAnhRrn-CqG5eezsvN5BJwEViZxydBNsnMzO0bhCnJGmUzZsX4cOp29UUGX5E54rYGLZPl1qqgSd9fLe-B1dU_kYbBSGSmdKVj8D3tpHCu85sSjObZ_PbHFu-mGN6txAZl8dyeJUGoP54pAjaQ-Bqygc6Lr1yLCnDW5moaz-Xleg4SYFvd8imoWPsWRonFYIzG9_L6FtKe5T7jnJobOsfYgXBXZ6L85a-hQCU4IrRyIePLHy8wO-Gzo3Tu1M5UQ2qefv8NMOvg_xyAXezEIyqvUxKm8t-Iysrt37SWGQRu5QkWryENNi7g8Ut2kZR6iZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/29488" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljaMwCet3MKUk5VFbuK2wRLRbFxXns7Z8beM3-EG005I8DWTUK9rLGay1pfdYDYnEm8WnIknOW5Xp4d6xIbMfJLvHEk9CiY0XiIzV_zpuuucX56ydam4K3Q-GKCPTY-GWzyrL0-jODrwsNf_wNLHc4bT7zSAMPliDKtlE6K1W8tdQvDqPLSyBhyJL0wzXPOOWoKbNpYzQSPk0_WnJKHwlXZ06bAJ4h9-CwvS2YGYKkDxpM5fM85lOWVDVeJ0ixwqVaI1jWQbIE4fq_dK0PwiC6e7b3I9wUvIbYqu8YYwNXZMpMjwbu_LDa8W7cPxHEPCjy7e_q3-PYVC53F1R_lCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تقابل جذاب دو فوق ستاره سابق تیم ملی برزیل رو؛ فلیپ کوتینیو از نیمار جونیور برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29487" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4VR5BWy8ydWbHr0csmfiJobItpIdlyrHJP3f2SMGSUBrgT40Tm9Oqqpn7No3HSuCKjNHoomd1LtH2m_H_74UipG5A1TnJexDik9twgwVlo0aR9bOBQSvasrS6BPtZc6HRLsMtGEQnx_w2S6C21PjTU0NBowFt1IfFA5RN3pZffORnrM-sXJmE3d-YfFe-OwxmZ7e1aowYEf-0a4ZlJNbEBjwfWH_NYtwagYUQBAmxxcEvjCVS0kJbN-le-84ws2A_udXwEWaDhL2MyI4pO7x39jo-tw97Uq6IwkvCFlyu_VH0DzN5KQF4aIcCEG3JOxmXHpzpcAyH-UV8zOmz2I-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکالمه و پیامک هم گران شد! از فردا ۲۰ شهریور تعرفه بخش قابل‌توجهی از خدمات ارتباطی افزایش پیدا میکند؛ آنهم تا ۴۵ درصد! برای مثال سقف تعرفه هر دقیقه‌تماس تلفن ثابت با موبایل از ۶۲.۵ تومان به ۹۰.۶ تومان رسیده است. عالیه. همینو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/29486" target="_blank">📅 23:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2GsLPy8mcfWLl-UsA2JV67lqDHAtrjeDYsefBnwJgTF58nzofBbX12jFY069jnDQqw2sjme-8zZ5H7KqaFp3upFam3mbbaSbo9XQgmzEea9vx1O2d3neL_ResTP_gEaWJ-MsC4_KfndnvMumQyZYTddWIONU4lCx6RL-7C_9LCC3jbd1j6IoZLwagiMVjKfMo7vavEqUZXhw1bZsSVKVYt0G6l8yeINElSmNqhDlubAuNccgJXd7dkH8hUkni-BS6_WPEY4G1fqLR4FfPG7aG5p9SGBkyvS9-z_amCgswnCLW3L9ptA_ub5kHiejsD0fxbLuBIekxbjoaffCxsoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/29485" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMEUxTMutXwp0WRDnRcV7-cR0g614WxMXn7DHY6YrfWTRhDcapJS1vSsaIPNFvOmyIwWr7Lxqb8wa3Jk_FiSzzDcWD2GQWvoUshv7clfw_25zzevYY9dn7q87jVi_iHGFFPwjvz2Jt9co6yi8sEEySI2_lXU4AKeKra29sF8DeHHoZH-qUL1_H4AthSkoLFhV5ixy1d0Qet2CBLy8aWrxLOrJhWa-1XMVwn56kSFdVN124cHok1w6BtLtzJmLJugVO9YUuIj1HjypxoodfXpj_yLijUYd0yjs0Cbl9ktIVyP6Q5EVkmoWJICzKYiKydCOqmGMndVnPTx-udxhCTmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/29484" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqA_WcxHmMbNA07WhIHSBNqCM4uFAV5-KhTBE-SMyWe5B7wlwJHXwpuVEGpVCu0Ox5PmkrvV6x3XXWQPKzo0CKG6sabrkWyWN6-hHpMwkU8_Q6Xov95KDV_Y316O8Hxi3b4xEuNW85oqpzIzIhGIURTD_XDagqvW3-f_KAxHY745zRnPwIlkopzZ-h_Lc48fjfsuAmqkZouVCocmcfORheUz0NML9RPsUAUyOoO9dA4BwlyEt3NSHLUbTtXGRpuwg8SM_zDtG9MMJ9Wjlv0lnfPXDtPuE4Hk8p-b8VrCN6HOGTfv7P9agoKwAB8RIdTTf-GC5ArQIrKDC45pZOWffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ شنیده‌های‌ رسانه‌ پرشیانا؛ فرشید سمیعی مدیرعامل‌سابق آبی‌ها درتماس با علی تاجرنیا رئیس هیات‌مدیره‌تیم استقلال‌آمادگی خود رابرای بازگشت به استقلال و پذیرفتن سمت‌مدیرعاملی آبی‌ها اعلام‌ کرده و به تاجرنیا اعلام‌کرده درصورت‌بازگشت تموم مشکلات حقوقی آبی…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/29483" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpNB6TUu9YZuKR4kQr96RigUaQsGkQkYJtzH8ZcfkFrb6AphNgkXdoA5hfFOzumpw6XbuJG8j9NB8GlieQHEAuevl0g5XhNVqztMihXAkAZ_RQZzCYr5ONwZazbfserLayLsn6UDW4YATnUjjm1_leeSgzwU8b7IVuJLO1KQeRaRfl_Owwq6slkM8_31H_fXh_TpLLIBoFxGcs7ON45Mee6JhHYU6G_Onr3xYpRZbOnURwgqcxypIM3QM6zSjCL-UVMCZDxNtp4uO959npL9Kk12K6_xf-O-ZBy2fQs95No0sK2-iEIZoCbYcmHm5QDcWbrMpBwD9TkCzj0MZOArtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ابوالفضل رزاق پور از مدیریت باشگاه فولاد خواسته با انتقال‌اوبه‌باشگاه پرسپولیس در نقل و انتقالات نیم فصل موافقت کنند که گرشاسبی بابت رفتار حرفه‌ای رزاق پور در این پنجره به او قول داده در نیم فصل همکاری میکنه تا این انتقال انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/29482" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVdTqmXEKtOIDXYbwUdVynZmIBPkGzw54I4aclYi9eex1eaIKnWAm5dXFTZG6_EN-bLWHJ4A-pvZ2Mvp7CNoNHYtFr1LKPQVh7wH5a2PfBOdKUHu5mwansJU6zqyZWUF8dLxChdFUXXhSfLpGSt84tiYMU8F_yVEfzkRHANA0vd7g-ZwgGqNqioHrX9NcNUJw7dSA-JPc1EKAGrstE52Rp6XnRDNbTbFsJhjUxktYpWyiFgU4Uf3o2mIwr59As-n6cjJaQXY9VMmxnEXIbop08WuXH5CRyniA8nW9UPaEfpNYNStgxGOJUuF7T15P-n3_IoupAW3PktywwlrHeNjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛ خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/29481" target="_blank">📅 21:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri2LLGzP_J3IUFGl4jRVlS8h2A9oARx9FAw_FLhDr2L_PjcJ-G0WrcdUt-ZVxuZ_GgIYHxvb9fMWHjtsA7cTJCYqmzR9NI_hRu__86NwkttdGOQHZQ_o3YX_ntXI94XKT0TV-36UnuxmMUhUCyS92_buuAn_4Ts21a_735j0dJSxm0R8BK3M6ImZfnJrK0mvsl1IsUzYi9BlgrXNC3i_6GS4Onc9Gy914wCIevAH6wC_KNRs1af-BzqIhhFBHB_N62Y0SiToe9aRVR6aZ5LC5PY9srgtmbkSvILNJmPNghOQOrx29fx6z_ZJtNJGFzSEiY7NgEw6mveBr3DCfxOd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/29480" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw8VpFz8zmJr-2oZixIWyTKsYAiIY5UOtdGFmYVMq9kwMfrH1mZfsM4W__n4hHAZHRCy8tsRRuh0hfZEPZXCAH7Yf1J4diqy6cFbas9eGjbllNAr6zZ5qup3BCN8yHWdIvoZTY8JXwW42RwixY8YE_pDmR3gYiws1fv0kQ8Ola-tDAEFobjz1_bjoiOTmcQ92GpFOWa8qYrPp6LVj1XqDAVVvO50ZCm5kvy3ceXMGW8r2MYnc3AGR2AdajqL4aurGNht8dFy0L69XYa2sDD0t9IACKjnlqyk33CzPEgg5glYH6aTxXSieovBm9m3ktVet-a5g0QwvqnNnND6EFhZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ درحالیکه باشگاه پرسپولیس و کادر فنی اش به شدت به لغو بازی با خیبر معترضه و اصرار به برگزاری‌دیدار برابرخیبر در روزیکشنبه داره تیم خرم‌ آبادی تمرینات خود را پنج روز تعطیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29479" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHcXQr0iQrG4YwrlVP6CL6xATEaSkTWCKEM9GtULPyYTJqf5twICFZo58hVFilGZewdfTLJNA105odnjQDhZgMtWQmW6WUUZypmUjjxJlBMDK9fefMhsAi8B_W5HXhlELKItq556Hp5xywaACOXo7guZ_I4hsky7AFXBou3G3_CrnDl4AwCEU9AcVVOkQxL5ouAjuhe72QPQq68kD3nvcPkBD2uRGJ0L16l0EQXy-V_EWMAi_DHa9hJE8zS6zbyT_SkPCJDVi1IzMn_Hb_5dVXEGWYPdvoh26IR8B-f3nQycQLm2btt4SvTz9Mqw9nFxSvfepygjdhS1Ggp9vZSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29478" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29476">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJF4wfkDcSzNjgVDjO14rV9FnJWxuer413lyc6q3qehMCZav7Urs1HBG2nWY8nNW8iQ90stttfkAtWMgyC_LwLaq0GwAcD23BnGve-TPDrEe_0GpliQwYoSmgtoPL477UguIxrivUcLe96-IpI8oIVn5UWcKowDKRYQWDWEXU36cl7zNJbWRQ8VEUCCnliuD68qbkMg1A54VbeqcsuqtqaWaqdENKNTToXId_RbfvoSAUlL4E3I6VR4huPx0lx8pIAM6XgBffeSvOoBu_m8Zf9SVRs8hpmBFl7UPIoj1UaJOgPu8hKWUjqOD1BJudmt-qlSBMp44_P3aSBMEsWUltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29476" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29475">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeCpYkALsoMMfD2bKNLxrVAwWw-rp5lK6fw1wYYKzd_pfGgN48AQiOR5qURtdSH1gUJ-a4COd7lHnt_CEYC2Elz-EVd0rbaLcUOJJiEMoRZdAMAU6nb-gvKuoQS6481qs5fdR-xgHUjVvvbP8p-7rUv0ysY_UtYu6oKgBRBTV07pfcOMnLZBJ3QqrisHAx7wZBunygfEtOjO6q08aHS03moSyGkU6aCUnovceKK-5KCITqsXSl5oQGwG4LYVUgudNSfbuQAZ63-RQ1lqI2iZBTQQbE9ObSINc_9uC4RQH1qeZD8YCskT_VEbYTX14wYCjPa3ONMDQlDTn9xvj_gU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس هیات‌مدیره استقلال: بعد از بازی امشب دوستانه اختلافات رو حل خواهیم کرد. صالح حردانی بازیکن استقلاله اما باید قوانین داخل تیم رو رعایت کنه. او به تمرینات بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29475" target="_blank">📅 21:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29474">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=ifJCRKvOIbx29jbxx--bR84b-lan57-ih-pYD9VqgTgmH6rB9KdUgWDAxlIAcmXzCKYf-07o-ZfJix4ER8-NIVj07CmCwxN2VkH489ad5LCCxVzNO33Gxh48DvAP3K1foQB8XZbe-G9mv3c6McKdwin4f0wpciKjLP0R4rKl9iheEVaDj8NbY6SspBMybHvTiQZ6Tf_iYV9nlXaSVokAlvf98g3Eecrb8x7OhOr4Qm0zzdqKp6op_YEgB79P6ktVtvaJDxZi-nPKsoF9gAn-eOoc_86QQWUtjXR14epmQPsudCzCroYpEW6gFEGtRxMIhCEyrw9rm4KOdzExdGVWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=ifJCRKvOIbx29jbxx--bR84b-lan57-ih-pYD9VqgTgmH6rB9KdUgWDAxlIAcmXzCKYf-07o-ZfJix4ER8-NIVj07CmCwxN2VkH489ad5LCCxVzNO33Gxh48DvAP3K1foQB8XZbe-G9mv3c6McKdwin4f0wpciKjLP0R4rKl9iheEVaDj8NbY6SspBMybHvTiQZ6Tf_iYV9nlXaSVokAlvf98g3Eecrb8x7OhOr4Qm0zzdqKp6op_YEgB79P6ktVtvaJDxZi-nPKsoF9gAn-eOoc_86QQWUtjXR14epmQPsudCzCroYpEW6gFEGtRxMIhCEyrw9rm4KOdzExdGVWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی در دومین‌بازی‌خود برای الوصل 70 دقیقه فیکس بود و درحالی که تیمش 5 بر 2 تیم خورفکان روشکست داد نه گلی زد نه پاس گلی داد و نمره متوسط 6.7 از فوتموب گرفت. هفته پیش هم دربازی برابر شباب الاهلی نمره 5.9 گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29474" target="_blank">📅 21:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29473">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PveLc3I6aJGP4HV1UclZIKZoGmS2NA0QF0Y6Efs70qyF2DuYRYeD3ra044iXdbChws2DJODj_HnYwxb1_UcCM6-tLQ1ugB7n92tcKCcj_jNqK1iVonGs5oCzgJP1LOYJertAQmQF2bp6HPuSXYw4WoLllaA74-_0GPWpGDChBjfdXEMQ6-t2pJxDdMkgWmYS8E-peit60xY77Lb7qMxcGvPSYyPjLNUBIKs_eF9difACvih9RR2_MhJugCClEHnx6rSA6-Ky0rfjRMiJIt7K6f2KMdLAPc9XzRbC7hTEW3kpDfNM3npvcTGoEyG26-6TGhcE7KV3GwZxN1ACMNITbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29473" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29472">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCFozZr3WSlcz1BkDGbPRWfGeBOjQHkNJi6eI7T41e-pE78DqDXkfmMjq3REfbfYwSzDyUSXgX93avRUuXLyn1EGyhx8FAQdaaRgJxxxs4U7T0k1w8Qx67n-Ui3E8mM847P_VXd59luWgFb7FnzkV0Xi_ApUA7jFDKV9_JpUMSCAoF9CglS_Rmy4KYhLSqVZ5OA8WNlUpkeoV9_YrdoUJlDKckYG7i0lvLt2jAJkx19-1O2syo9nmJUqrU2fi9OU0cWjrMJ2RMmYBk_SepsFAYiusJcaAq3app5SU52ALQsxmr20DQjjBqposboey7vp9fgApk2bf_7wqGB9-tv5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم لیگ برتر؛ پیروزی سخت و نفس گیر آبی‌ها در قلعه حسن با گلزنی ستاره آلبانیایی؛ آسانی سه‌امتیاز بازی‌خانگی‌روبرای سهراب به ارمغان آورد.
🔵
استقلال
1️⃣
-
0️⃣
پیکان تهران
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29472" target="_blank">📅 20:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0fShE1Wc0kcemlBmnsJKrRZFRzdxuJvDqqoroyVdWhxIj8HzC79K4xf0YSsenhCi9OOKjasCNEezG_mJHcUwmC5UAQWrOfFdQ_z14oOr0-YrmohXC33NjrVFxOECtTW_SQhOw1F1friW6dr4cSAhhi3jav7JHQ0sclOPb9Ae3Es-mMroMDII5JZIpB9rNJ8VAhmddc8EL_x-Hu6naOyBiwegXIKRnYdfnEku4dGrYvtNDkOs83_Hi4R9TPiwK8HjczWJ9sAYE79rHoLouy2cLnTCJwyT2onhHLsh9uf4SRY7gPuywB6MDbWWgH2T3PAdkCLYSWKzJzNc5LQHS33UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سومین گل وینگر خارجی آبی‌ها؛ گل اول استقلال به پیکان توسط آسانی از روی نقطه پنالتی دقیقه 76
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29471" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29470">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=AnAyq1WPjz3YutRvBDqVUYxIYPSywYU9imEUY1vRNJHZHqfCU2x9v1j4Z8Tf_qO9nGh2ZOr1g4o-fo4H9QdD5wp9qN1CrBRaQfgkrB-0EWLY6lpXRD4KlLNvO7aSeuuUQBavSGntC80vuObBS6oGvmsVbPSGVTbU4sUr57yRVHPIP6LQ9HUPWIjtmjw38-QaibXGT5-sdsRIGi6oSDZM20NiQyZ11HD-4JHxvmBRjZZEKjxDuqLdajPtNGxY9ceCzXx5lqIcnm3_P-rYXPWTyyrDvr8MW3hulRp1hfoSCAI-XtLupTnzrMivHW5nHJ-HvafVR4eN3AKoFscQE74mBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=AnAyq1WPjz3YutRvBDqVUYxIYPSywYU9imEUY1vRNJHZHqfCU2x9v1j4Z8Tf_qO9nGh2ZOr1g4o-fo4H9QdD5wp9qN1CrBRaQfgkrB-0EWLY6lpXRD4KlLNvO7aSeuuUQBavSGntC80vuObBS6oGvmsVbPSGVTbU4sUr57yRVHPIP6LQ9HUPWIjtmjw38-QaibXGT5-sdsRIGi6oSDZM20NiQyZ11HD-4JHxvmBRjZZEKjxDuqLdajPtNGxY9ceCzXx5lqIcnm3_P-rYXPWTyyrDvr8MW3hulRp1hfoSCAI-XtLupTnzrMivHW5nHJ-HvafVR4eN3AKoFscQE74mBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29470" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29469">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=e3jGApjeJD-HmOJ0MGltkSDDQcmd654cX35RNkXJsoNac0zgzJ3mQoHqVe7lKg4KPT5j1RhIsnjeoDnWvn9gYPK_TQ59wDEIoqAOyok_FphlHuY46yJvxe5zWRQfAJ-4ryOrVck22yzQ9hR_2FkGxvHQooGIZT7LVaDVkuCZs_VKgBFQjAhwmTjrzadx3AG3jyqoxHcIeLonPCG3NA_Xae4f0fZdjtM8Zt2f1Rnar7t5wZvTa92XN0rpJ8soKRRJro6GyilvUVcwIc8LRVRroVTwd5wSAErubf7m9EtqefsdbSNTZg0Y8riTPDzg3smeCV9aQKRJRRrdWmU7ulEYCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=e3jGApjeJD-HmOJ0MGltkSDDQcmd654cX35RNkXJsoNac0zgzJ3mQoHqVe7lKg4KPT5j1RhIsnjeoDnWvn9gYPK_TQ59wDEIoqAOyok_FphlHuY46yJvxe5zWRQfAJ-4ryOrVck22yzQ9hR_2FkGxvHQooGIZT7LVaDVkuCZs_VKgBFQjAhwmTjrzadx3AG3jyqoxHcIeLonPCG3NA_Xae4f0fZdjtM8Zt2f1Rnar7t5wZvTa92XN0rpJ8soKRRJro6GyilvUVcwIc8LRVRroVTwd5wSAErubf7m9EtqefsdbSNTZg0Y8riTPDzg3smeCV9aQKRJRRrdWmU7ulEYCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب استقلال برای دیدار مقابل پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29469" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29468">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=jYt4Vh2oRGpCnQWrrz1HS9rMIedejdWlnjQ07OPVN6IKLRhJFGdo184bBchKZ2V5DnDIlC2VXzIdH60dp71Kf5zQWzktGGe_sH_lr9m0TtBjIolMWBTbuOPLLK490WMRxvSUxDys6lJE7_jxyDQTH7u0zA8jbFqNcdREuL40cXwtkdtfUHe3ZdBhQyLoJG5S2kKV5_LcKi5bUGWFEUUh2QUfH8IP4kbzQIy6J-OzngmYFG1uzN-2-WFkR5tot3MrP1Nglepe3TrpH-q1H0jZE9h8c634QmLIEjXmhMcpRddfaQY51oeXmrE1Dw9-fKzG2Xq0Y3gglSd794NrnaIGdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=jYt4Vh2oRGpCnQWrrz1HS9rMIedejdWlnjQ07OPVN6IKLRhJFGdo184bBchKZ2V5DnDIlC2VXzIdH60dp71Kf5zQWzktGGe_sH_lr9m0TtBjIolMWBTbuOPLLK490WMRxvSUxDys6lJE7_jxyDQTH7u0zA8jbFqNcdREuL40cXwtkdtfUHe3ZdBhQyLoJG5S2kKV5_LcKi5bUGWFEUUh2QUfH8IP4kbzQIy6J-OzngmYFG1uzN-2-WFkR5tot3MrP1Nglepe3TrpH-q1H0jZE9h8c634QmLIEjXmhMcpRddfaQY51oeXmrE1Dw9-fKzG2Xq0Y3gglSd794NrnaIGdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛ شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29468" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MP-HjJjp635-y4nXh8XACHW6rUsaXZxX4X3xImIJdLfQX4DdZfH-eSoZjzWK0zWw8Vi4BJJfjKyi6p_fe38VA3Bcut4axG9grklP4NVZd820drIG7Fzc6-BqyqXSrtEznEu08OmGkZeLTjmHnhH_qZx9QF8QDNWJyBax6eNu9Gvd8gFPlbetr93TdCwQeUcBhppuZWMCunGdbgnjJsTCXhRtA0hXtD_BwWA6kPb4z_mTHwb90QhUQetsOaJD9LlJXcPupikL5uaTwzWe5YS2jDpuoExd_Pg9m24ntZSsy9f0BDKs_w6lHyVjerABWB-xbdv_U7_p0P0ukMQ0JfVXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRRZnzimBOxC6J-YLVPmAHF0CW2xlgOXb8WBGlpAx2UgWxRWMM6yOT3B_n1ubIsiFFQEwy9OQ7c-TrsMVeiYMU3OfSzi5aN18zfSg3ga3n3ZlUkAq6loc1fNzaiZAQBwN4r9g4Bt6xFK2AWcGH-EoderhPF6jxOz1OBkQr9Pg8cXwa0hBgSHrbU6ZtzEUuDWRDn9AR1Y_oT7Ewo7TKGWqli2Jv9X4CdUkm7yQTlZJb3ZP-cJtI2b0NSX-Go_0wHHLA7_J3PXgCK-QjULvioZRuGLhC3-_3KViwn8YSTvIg1bvA_M4onJt999xG6lCYezMGibEMAhiYUeKDC0cIFaHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29466" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyztu8rxUqxYpXDq234wzqK52uENZwei4bp1CXiQhuDNEqxgvRAVWAlkysZ2SEXEAo7rEG0g3vAN2ojR7oB75uJKSEa3N9ZM1qsWG2rv2C6Gr4W7DpFMwZDQg0XNf4hSoWuNRkIctmN_wO-RPJeFXp0i2e-dqyq9TlvZiOo-RUmata1poh-ZbKDDrI_y7TiSkfZttmZlqU5YJrA4ryiXHsiYlYqdM-UR43EOdrGHHAJa8NeOoXjczvU2Gua2tXZ0IcwMirjz-7GEwp8ZAXL_bHUZaKzTCVFK1500w6tek67kKYGNSEJtz0vTuQpXbBQ1slf6LSC4LyPCBtYPG3jpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29465" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
