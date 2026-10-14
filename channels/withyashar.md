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
<img src="https://cdn4.telesco.pe/file/kGkLl7F2BBMtSRbw87ifQqcF-QOqtiBRs9UfIR1uV0sG9HpT6eL2tMpHybrmhNXg9Gwn5EPZJL906xGFVYuVfJKeN_VQHpACa2LsMea3D5aStNwArEbfgigWilM3j2HgAdiHY6_9xB-qj5azxY6-DCD-qH-KwMwXk_DmrF3omOBJqXcpAAZ7BuewTaINQmI_2_RelnsoCA6rGPKH6pdgKQUhi1cp5UNsj8bjaS1IxWq28IWPcHyLUyyrNS1cANrM3SuNTVWn_7UqiTX261h2PrqOx4AnymH0yx9j1l5uQV9I73RH3-QNaUe7l4VsdoMAPey1wJUxwfhhcIbb-LAMow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 501K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۳ اسرائیل: دو هفته آینده بسیار حساس است
!
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/25640" target="_blank">📅 21:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به مناسبت سالروز تولد شهبانو فرح پهلوی
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/25639" target="_blank">📅 21:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ممباقر جنگی
: جنگ خواهیم کرد تا دشمن مجبور شود به خواسته‌های ملت ما تن دهد و اگر نداد، شکست را بپذیرد.
باید در زمان لازم با تمام توان بجنگیم، هر فرصتی پیدا کردیم باید آمادگی خود را بالا ببریم و هر زمان که در میدان به پیروزی رسیدیم باید آن را تبدیل به یک پیروزی سیاسی بکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/25638" target="_blank">📅 20:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رونالدو همچنان در ریاض مانده، ولی تعدادی از بازیکنان فوتبال خارجی لیگ عربستان سعودی، به دلیل تشدید حملات حوثی‌ها به عربستان سعودی، از این کشور فرار کردند و ۳ بازی هم از هفته آینده لیگ به تعویق افتاده‌اند، از جمله بازی تیم النصر (تیمی که رونالدو در آن بازی می‌کند) با تیم النعوم
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/25637" target="_blank">📅 20:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلار و تتر ۲۶۶،۰۰۰ تومان
@WarRoom
🆙</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/25636" target="_blank">📅 20:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی سپاه: احتمال وقوع جنگ جدید کاملاً وجود دارد ، آماده‌ایم به هرگونه تجاوز، با قدرتی بیش از هر زمان دیگری پاسخ دهد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/25635" target="_blank">📅 20:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUZo3tipCAUdrg90VD6VKQo2FXSBuHsue_rS5X3M26udA8Oifwyx-M2iybDoHo33ACSsBziKZx7KrZ6BKxWC2dqX1clnLxDy0E_LBFz5I6Mu_qpFUGXpWzP1BV73B8o0LBe0xmRSVugQFuv-qvEbPQZ85V18he9VOunxn9v6kDnlemM_nUgEuwgPSco1b8fTWUe3LU-ideGJT9JU5D3KA2ezi0cYZRW8hZ6ZTaWTU15HjGzjVkV-XY4dVIA3G82x0I_oBj5zSqmsOKxAW7zTWYc4Xsk0oNosEBPiIH1stMPwp1a0dZWGZazwSRnLEr934-jVU2IEDS8VUVkZZwyfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش و پرورش اسم حشره‌ «آخوندک» ‌رو حذف و جایگزین کرد با «راهبک».
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/25634" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدیر FBI، کاش پاتل، برای دیدار با مقام‌های روسیه وارد این کشور شده است. منابعی به شبکه خبری MS NOW گفته‌اند که قرار است سرویس امنیت فدرال روسیه (FSB) میزبان او باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/25633" target="_blank">📅 19:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77395fe22.mp4?token=KqLUnuWgPKz3OVab9RrRFGcSWsGwAgZ0nzbeJzZfHTKgVlKvgamWDb9Gx7fTsvNyqnTpNELFW7qHxiH8qT6LRKMqnb1f1GxDSeXNLfsgy9aIOR_roK1pnNovDpvqRbkpjENyPQXyS5qBIyDPCfT7F1atJEvQKhBotG41_ZF1UCvHrw2N0wvG5B3N7d0rnU89BTZXb6WKyfx2q2BuWX_Z0apCXGzlmBsufG2tPW3P0d3msbLbMounCd-vlcLbZhk5lu1LBZrVrrlT06TVOmEraUofQEQfbnbt29Hqmmw61j7_W4D-Jc-yX5BcZXmfVfN-hMsbrYNl5ZEpRa5IvGhjepKF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77395fe22.mp4?token=KqLUnuWgPKz3OVab9RrRFGcSWsGwAgZ0nzbeJzZfHTKgVlKvgamWDb9Gx7fTsvNyqnTpNELFW7qHxiH8qT6LRKMqnb1f1GxDSeXNLfsgy9aIOR_roK1pnNovDpvqRbkpjENyPQXyS5qBIyDPCfT7F1atJEvQKhBotG41_ZF1UCvHrw2N0wvG5B3N7d0rnU89BTZXb6WKyfx2q2BuWX_Z0apCXGzlmBsufG2tPW3P0d3msbLbMounCd-vlcLbZhk5lu1LBZrVrrlT06TVOmEraUofQEQfbnbt29Hqmmw61j7_W4D-Jc-yX5BcZXmfVfN-hMsbrYNl5ZEpRa5IvGhjepKF1HVT8mdKb2Xl5fyBWFgnPs0oTWak_TMRs1l5mZejfcnrcpWaHy8OYS6ATvBXy9KXHxhuGI7yT1XE0ElWmQiFTgsmiRj37tDhJ0aaIMsZTcccwwyNOOkVws4_eEh2l00nCcB-Uzyf6JV-71IAUlfnF-EXXbOI2MzW2wkAP9V80E_0iovYCC_G4iFqwu6ItXQb4Ei8AHikhKTH0gL6TLSHfC4EhQP7MSVp1TZAE-pmJZyKC1S-erGXP4MWOiX-pcXmBV-IB8PltMz3wTf7PWCjpGG69lEDZdFLt9TiWdqBzMF1ODdjK8nUWSSWLQdyjzXszKgAJxcU0O9OJ_cI9c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود
.
نتانیاهو بدون جنگ باید به زندان برود، برای همین چه با ترامپ و چه بدون ترامپ، جنگ را شروع میکند!
برای زدن زیرساخت‌های ایران ۳ روز برنامه ریختن، با این‌کار نتانیاهو انتخابات را به تأخیر میندازه!
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/25632" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نام برج میلاد تهران تغییر کرد
بر اساس حکم صادرشده از سوی علیرضا زاکانی، برج میلاد تهران به شرکت گردشگری و تفریحی میلاد تهران تغییر نام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/25631" target="_blank">📅 18:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ed3c5628.mp4?token=c61rEVKKpGbhfKdzz42Y-fV5-u5xzrN10Xm5z70JlOc1LzaPjyjZ8OdC0Qf6Nkzvzrs7MD5ySgbc7e4RnLGr59mgr6qXSat3y8_WgsmEfkRT3wy1eagzv94H37c6rNi1idAC59eBe3VoKYK2sLkCoh7lJJs904V4xDVUX-bA31otyLyBIoK1gy_TWc7ij6ZKeE8sVIuCLcJB_Aw7jbN1aGbK9wzpUMBe_K4kwzC58EifSgHX1fKTuI0fQvy4heUB1mQB9VSRhX3ab8K_0a7aIVblDB-wttCvRic8-verljk4oQ5bPTEM5lI2sfVSek7zGY-LnadA7DXqLuZCOTaCCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ed3c5628.mp4?token=c61rEVKKpGbhfKdzz42Y-fV5-u5xzrN10Xm5z70JlOc1LzaPjyjZ8OdC0Qf6Nkzvzrs7MD5ySgbc7e4RnLGr59mgr6qXSat3y8_WgsmEfkRT3wy1eagzv94H37c6rNi1idAC59eBe3VoKYK2sLkCoh7lJJs904V4xDVUX-bA31otyLyBIoK1gy_TWc7ij6ZKeE8sVIuCLcJB_Aw7jbN1aGbK9wzpUMBe_K4kwzC58EifSgHX1fKTuI0fQvy4heUB1mQB9VSRhX3ab8K_0a7aIVblDB-wttCvRic8-verljk4oQ5bPTEM5lI2sfVSek7zGY-LnadA7DXqLuZCOTaCCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس ستاد مشترک: «احتمال تشدید تنش و عملیات پیشدستانه افزایش یافته است؛ ما در وضعیت آمادگی بالایی برای گذار به عملیات تهاجمی گسترده قرار داریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/25630" target="_blank">📅 18:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a653fa790.mp4?token=Y-nSOXSYMI9HljKz1jCYhjFdTxICCoyY--ew1ab2U2RjIWcRRlp7Zz07GZsZIvpU2Xzdg4VcfvwxYOwnQf1Mu4apQhA7PF-8dvfb3oWEbTrWdKRTyapEFZFevmFmY9pjMPkp7R4dTqS08usyfpoc8hgFsSJqCsaFHZI1bXPSeKyO5G9xK8E-AHUukAEdQnP_JTDN23_L_kUgiBizqrHAwP4pT_9zbN1aFn1uLU7L1_Z1sqEyJs_tIjlKJZQTAUoR6Eidq9aT3R6BrvKYk176acQAcwH18z1wQGR3ERFoJkZT2lkfkLI5Rdc1pVhvsb5Qi1b4YOf1SH0HaqVruwTBFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a653fa790.mp4?token=Y-nSOXSYMI9HljKz1jCYhjFdTxICCoyY--ew1ab2U2RjIWcRRlp7Zz07GZsZIvpU2Xzdg4VcfvwxYOwnQf1Mu4apQhA7PF-8dvfb3oWEbTrWdKRTyapEFZFevmFmY9pjMPkp7R4dTqS08usyfpoc8hgFsSJqCsaFHZI1bXPSeKyO5G9xK8E-AHUukAEdQnP_JTDN23_L_kUgiBizqrHAwP4pT_9zbN1aFn1uLU7L1_Z1sqEyJs_tIjlKJZQTAUoR6Eidq9aT3R6BrvKYk176acQAcwH18z1wQGR3ERFoJkZT2lkfkLI5Rdc1pVhvsb5Qi1b4YOf1SH0HaqVruwTBFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی بی نظیر در جهان، چند نفر تو اهواز پله های پل هوایی رو دزدیدن
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/25629" target="_blank">📅 18:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دیدبان اتاق جنگ : به ما در نیروی زمینی سپاه دستور داده شده ، به محض شروع جنگ و درگیری ، کویت رو به هر صورتی شده فتح کنیم و حتی هر جور شده شده یکنفر سرباز آمریکایی
اسیر کنیم…
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/25628" target="_blank">📅 18:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آتش توپخانه ارتش دفاعی اسرائیل، حومه شهرک «حاریس» را که خارج از منطقه امنیتی در جنوب لبنان قرار دارد، هدف قرار داد.صدای انفجار های بسیار شدیدی هم اکنون شنیده میشود
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/25627" target="_blank">📅 18:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏
رسانه های رژیم :
اقدامات تروریستی در سیستان و بلوچستان صرفا بر عهده تروریست ها نمی باشد و برخی منابع از حضور نیروهای مزدور غربی (آمریکایی/اسرائیلی)خبر می‌دهند.
از صبح امروز چندین حمله تروریستی به نیروهای نظامی صورت گرفته است که منجر به شهادت چند نیروی نظامی شده است.
@WarRoom
🚨
🚨
🚨
🚨
توجه : این مطلب از‌ زبان من نیست و عیناً نقل شده.</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/25626" target="_blank">📅 17:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">BTC 82000$
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/25625" target="_blank">📅 17:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حقیقت‌یاب سنتکام:
ادعا: سفیر ایران در سازمان بین‌المللی دریانوردی مدعی شده است که ارتش آمریکا علیه دریانوردان ایرانی از «ادبیات تهدیدآمیز، توهین‌آمیز و تحریک‌آمیز» استفاده می‌کند و باعث «ایجاد استرس شدید و فشار روانی بر خدمه غیرنظامی کشتی‌ها» می‌شود. این ادعا نادرست است.
واقعیت: محاصره ایران از سوی آمریکا که با موفقیت زیادی همراه بوده، ماه‌هاست ادامه دارد و اطلاع‌رسانی درباره آن به‌صورت حرفه‌ای انجام شده است. تنها کشوری که به دریانوردان غیرنظامی در حال تردد در آب‌های منطقه حمله می‌کند، ایران است. با وجود این حملات که آمریکا آن‌ها را غیرموجه می‌داند، رفت‌وآمد کشتی‌های تجاری در تنگه هرمز همچنان ادامه دارد و نیروهای آمریکایی با همکاری شرکای منطقه‌ای، حفاظت هماهنگ از این ترددها را تأمین می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/25624" target="_blank">📅 17:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رسانه جماران به نقل از اطلاعات دریافتی از اپراتورها گزارش داد که تعرفه خدمات اینترنتی از بامداد پنجشنبه، ۲۳ مهر، احتمالاً ۴۰ درصد افزایش خواهد یافت. با این حال، تا زمان انتشار این گزارش، اطلاعیه رسمی درباره افزایش تعرفه منتشر نشده و جزئیات مربوط به دامنه افزایش نیز مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/25623" target="_blank">📅 17:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیانیه شماره ۲۲ جبهه مبارزین مردمی درباره درگیری‌ها در بلوچستان جبهه مبارزین مردمی در این بیانیه مدعی شده است که نیروهایش طی ۲۴ ساعت گذشته در تفتان، زاهدان و چابهار با نیروهای حکومتی درگیر شده‌اند. طبق ادعای بیانیه، صبح ۲۱ مهر، محل استقرار نیروهای سپاه و لشکر…</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/25622" target="_blank">📅 17:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بیانیه شماره ۲۲ جبهه مبارزین مردمی درباره درگیری‌ها در بلوچستان
جبهه مبارزین مردمی در این بیانیه مدعی شده است که نیروهایش طی ۲۴ ساعت گذشته در تفتان، زاهدان و چابهار با نیروهای حکومتی درگیر شده‌اند. طبق ادعای بیانیه، صبح ۲۱ مهر، محل استقرار نیروهای سپاه و لشکر فاطمیون در منطقه چاه‌احمدِ شهرستان تفتان هدف حمله قرار گرفت. این گروه می‌گوید با استفاده از اطلاعات قبلی درباره تعداد نیروها و محل استقرارشان، یک گروهان از نیروهای موتورسوار را غافلگیر کرده و بیش از ۲۰ نفر، از جمله فرمانده میدانی آنان به نام «یاسر باقری»، را کشته است؛ همچنین مدعی شده بیشتر کشته‌شدگان از نیروهای فاطمیون بوده‌اند. بنا بر متن، این درگیری از صبح تا تاریکی هوا ادامه داشته و در پایان، نیروهای سپاه عقب‌نشینی کرده‌اند. این گروه کشته‌شدن سه نفر از نیروهای خود و خروج سایر اعضایش از محل را نیز اعلام کرده است.
@WarRoom
1/2</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/25621" target="_blank">📅 17:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز به نقل از یک منبع در شرکت آرامکو عربستان سعودی : حمله تروریستهای حوثی به این شرکت آسیب جدی به سه طبقه از ساختمان آن وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25620" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سپاه پاسداران تأیید کرد که کشتی «جی‌اف‌اس پراید» (GFS PRIDE) پس از برخورد با مین دریایی در تنگه هرمز غرق شده است. این کشتی کانتینربَر که گفته می‌شود حامل ۲۵۰۰ کانتینر بوده، هنگام تلاش برای عبور از مسیری «غیرمجاز و خطرناک»، پس از برخورد با یک مین دریایی دچار…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25619" target="_blank">📅 15:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/801428f904.mp4?token=GQtKzZeBsvdbMZ6ca9IdLGOkPrwVw2vXUQFCmTeqE_Z5wwXefmP1q_p-57onVez5BA95mymFuQSgYJPTBM4X3nt4eDElLCZC_r1baW-3B0P3XIzZGEDzgC8MHvVIjjTedMVkNMBQG9mATXQe-LqZTgM3o-qks1DG-Y1K7ZfeMd09MPSx3co4jcIL-53_J-aRTu77C-_fhvzgd6ujMwurd6oMcCnvt3GGgJAw_zKHKGtUkeScUIjOWHh3Oje25hsHckuf_e6MOI04FuvqTqjExMGzDBcq7WVmJ65ANdEPN_jUtM6D_loxV3PfZ2LBmv9jqDgRJhXJenegis7D82Hrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/801428f904.mp4?token=GQtKzZeBsvdbMZ6ca9IdLGOkPrwVw2vXUQFCmTeqE_Z5wwXefmP1q_p-57onVez5BA95mymFuQSgYJPTBM4X3nt4eDElLCZC_r1baW-3B0P3XIzZGEDzgC8MHvVIjjTedMVkNMBQG9mATXQe-LqZTgM3o-qks1DG-Y1K7ZfeMd09MPSx3co4jcIL-53_J-aRTu77C-_fhvzgd6ujMwurd6oMcCnvt3GGgJAw_zKHKGtUkeScUIjOWHh3Oje25hsHckuf_e6MOI04FuvqTqjExMGzDBcq7WVmJ65ANdEPN_jUtM6D_loxV3PfZ2LBmv9jqDgRJhXJenegis7D82Hrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران تأیید کرد که کشتی «جی‌اف‌اس پراید» (GFS PRIDE) پس از برخورد با مین دریایی در تنگه هرمز غرق شده است. این کشتی کانتینربَر که گفته می‌شود حامل ۲۵۰۰ کانتینر بوده، هنگام تلاش برای عبور از مسیری «غیرمجاز و خطرناک»، پس از برخورد با یک مین دریایی دچار آتش‌سوزی شد و غرق گردید.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25618" target="_blank">📅 14:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتس، به حزب‌الله هشدار داد که اگر در حمله‌ای علیه اسرائیل به ایران بپیوندد، با حملات سنگین و از دست دادن بخش‌های بیشتری از خاک جنوب لبنان، از جمله مناطق اطراف نبطیه و رود لیتانی، مواجه خواهد شد؛ مناطقی که به منطقه امنیتی دائمی اسرائیل تبدیل خواهند شد.در این صورت منطقه ضاحیه در بیروت تخلیه خواهد شد و زیرساخت‌های آن هدف حمله قرار خواهند گرفت؛ اقدامی که باعث آوارگی بیش از یک میلیون نفر از ساکنان شیعه لبنان خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25617" target="_blank">📅 14:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f925e8391.mp4?token=k70D4X8NsuDdZUoFKSu56JRZv0BlDB7C3tnwAS1_0--t2FOOqRCJQnscLDXxvNDHs-QFG1RTXZHBpC3AwI6ORqru-27n8O5qC2oNYavryGha5YT-vb9DpkttAbNtWpCz6ItTOkjoT9lHLe8Ns6zNChxKH07FsEpM7JTxLucZI6GwjcvB6CBGtVm2GcAxWBry3mFIABpxPXCUOLvxxIa11Rfpl2lngotzeWeYb3bD3o3YeJYWoPPXrwTbqlj1KmUxkRR_-nudtpJxkXl715-AG3cjfUfUC8Zy9roFdHqV7GJ0wdqGTWlSYMD3y5ttI6_WeTxQ5SsPJXNjqmrcp675jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f925e8391.mp4?token=k70D4X8NsuDdZUoFKSu56JRZv0BlDB7C3tnwAS1_0--t2FOOqRCJQnscLDXxvNDHs-QFG1RTXZHBpC3AwI6ORqru-27n8O5qC2oNYavryGha5YT-vb9DpkttAbNtWpCz6ItTOkjoT9lHLe8Ns6zNChxKH07FsEpM7JTxLucZI6GwjcvB6CBGtVm2GcAxWBry3mFIABpxPXCUOLvxxIa11Rfpl2lngotzeWeYb3bD3o3YeJYWoPPXrwTbqlj1KmUxkRR_-nudtpJxkXl715-AG3cjfUfUC8Zy9roFdHqV7GJ0wdqGTWlSYMD3y5ttI6_WeTxQ5SsPJXNjqmrcp675jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو : «ما باید بتوانیم حتی بدون آمریکا هم اقدام کنیم. رئیس‌جمهور ترامپ تا دو سال دیگر، یعنی در دو سال آینده، همچنان رئیس‌جمهور خواهد بود و همکاری ما با آمریکا واقعاً محدودیتی ندارد. اما اگر لازم باشد، خیلی راحت می‌توانم مستقل هم عمل کنم؛ همان‌طور که در عملیات «غرش شیران»هم انجام دادیم. ولی می‌توانیم با همکاری یکدیگر اطمینان حاصل کنیم که این رژیم حتما از میان می‌رود. چون خیلی ساده به شما می‌گویم: یا آن‌ها یا ما؛ اما این ما هستیم که باید پیروز شویم، نه آن‌ها.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25616" target="_blank">📅 14:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مستند جدید و جنجالی دویچه‌وله آلمان با نام «مردان آیت‌الله»؛ افشاگری دو مقام بلندپایه سابق جمهوری اسلامی، یک افسر اطلاعاتی و یک فرمانده پیشین نیروهای ویژه نخبه ایران، که پس از جدایی از حکومت حاضر به افشای پشت‌پرده‌های نظام شده‌اند. دویچه‌وله ماه‌ها برای راستی‌آزمایی هویت آن‌ها و بررسی اسناد و تصاویرشان تحقیق کرده است؛ مستندی کاملاً به زبان فارسی.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25615" target="_blank">📅 13:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b625bf28.mp4?token=EQsNrIwdVHPwIzFaX9L9hMyFIl8_fZZ_tcO78j5psXMfXX3umr9QzlXmZbK8Kt2Z8dkCDZrl6QumP3S5gAlPI_zKexvmQGVAGQrkPjEwwxlJZDUPRuzZn6QQ2YWHJpahmNoMRpS2wZrXDU1q_5m2FOJSYJoX5pl5ZxbWxFk3JtIbDdOnCbs6P-efvOjMwrfTNj9819uVq-gVoLVtldZSjDrVwyILKwt_-VgJ9K0H5-5q_XWDBV9NsjksgExBkSULTrJh4AJQ_3m1gJNEam2stR2gbZlLA_LvZh_S6hN6u-OFXW1113u60I2f5sB6s-1rEaHjNF-Z5KoWCHCh_ETbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b625bf28.mp4?token=EQsNrIwdVHPwIzFaX9L9hMyFIl8_fZZ_tcO78j5psXMfXX3umr9QzlXmZbK8Kt2Z8dkCDZrl6QumP3S5gAlPI_zKexvmQGVAGQrkPjEwwxlJZDUPRuzZn6QQ2YWHJpahmNoMRpS2wZrXDU1q_5m2FOJSYJoX5pl5ZxbWxFk3JtIbDdOnCbs6P-efvOjMwrfTNj9819uVq-gVoLVtldZSjDrVwyILKwt_-VgJ9K0H5-5q_XWDBV9NsjksgExBkSULTrJh4AJQ_3m1gJNEam2stR2gbZlLA_LvZh_S6hN6u-OFXW1113u60I2f5sB6s-1rEaHjNF-Z5KoWCHCh_ETbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فهیمه خضرحیدری
(مجری صدای آمریکا)
: داریوش اقبالی توسط ساواک شکنجه شد!
عرفان قانعی‌فرد
(پژوهشگر)
در جوابش: داریوش اقبالی بخاطر تریاک دستگیر شد ساواک اصلا کاری باهاش نداشت!
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25614" target="_blank">📅 13:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بی‌بی رفت لایو اینستاگرام همه در حمایت مردم و جاوید نام های ایران کامنت بزارید و حتما انگلیسی ‌و یا عبری‌ بنویسید</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/25613" target="_blank">📅 13:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو به رادیو ارتش اسرائیل:
حمله به ایران به ابتکار اسرائیل در این مقطع زمانی، قبل از انتخابات "به نظر من، الان این کار برای ما مناسب نیست."
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25612" target="_blank">📅 13:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ادعای رسانه های وابسته به سپاه : یک کشتی باری حاوی بیش از ۲۵۰۰ کانتینر، صبح امروز در آب‌های جنوبی تنگه هرمز غرق شد ، بر اساس گزارش‌ها ، این کشتی بر روی مین دریایی منفجر شد، آتش بزرگی در آن رخ داد و آتش به سرعت گسترش یافت تا اینکه کشتی غرق شد. رسانه های رژیم همچنین اعلام کردند که این کشتی در یک مسیر "غیرقانونی و خطرناک" در حال حرکت بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25611" target="_blank">📅 12:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پلیس سیستان‌وبلوچستان: درپی حمله افراد مسلح به خودروی پلیس در مهرستان، گروهبان یکم محمدعلی شهریاری، کشته شد
مهاجمان پس‌از این کشتار از صحنه متواری شدند که اقدامات لازم برای دستگیری عاملان آن ادامه دارد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25609" target="_blank">📅 12:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فرمانده یکی از حوزه‌های بسیج عفونتی خواهران شهرستان مهرستان در جنوب استان سیستان و بلوچستان در پی تیراندازی درب منزل ترور شد و به هلاکت رسید.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25608" target="_blank">📅 12:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وال‌استریت ژورنال: حوثی‌های یمن در تلاش‌اند با استفاده از قطعات واردشده از شرکت‌های چینی، نسخه‌ای از موشک بالستیک پیشرفته ایرانی «خیبرشکن» را تولید کنند. برد این موشک حدود
۱٬۹۰۰ کیلومتر
برآورد شده که تمام خاک عربستان سعودی و اسرائیل را در تیررس قرار می‌دهد. این گزارش بر اساس یافته‌های سازمان پژوهشی «Conflict Armament Research» درباره محموله‌های توقیف‌شده تجهیزات موشکی تهیه شده است. با این حال، هنوز مشخص نیست حوثی‌ها تا چه مرحله‌ای در تولید این موشک پیش رفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25607" target="_blank">📅 12:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال ۱۴ اسرائیل اعلام کرد که نهادهای امنیتی این کشور در پی افزایش نگرانی‌ها از احتمال ازسرگیری درگیری‌ها با ایران، سطح آماده‌باش خود را به بالاترین حد رسانده‌اند. نگرانی اصلی اسرائیل احتمال حمله غافلگیرانه ایران با هدف وارد کردن ضربه نخست و غافلگیر کردن تل‌آویو است
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25606" target="_blank">📅 12:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز به نقل از دو مقام ارشد ایرانی:
تهران برای بالا نگه داشتن قیمت نفت و تأثیرگذاری بر انتخابات میان‌دوره‌ای آمریکا، حدود ۱۰ روز پیش راهبرد جدیدی برای هدف قرار دادن کشتی‌های عبوری از تنگه هرمز که به ادعای ایران محدودیت‌های این کشور را نقض می‌کنند، آغاز کرده است. این راهبرد شامل تغییر در نوع و دفعات حملات بوده و به افزایش حملات علیه کشتی‌ها منجر شده است. به گفته این دو مقام، هدف دیگر تهران ناکام گذاشتن تلاش‌های آمریکا و متحدانش برای کاهش قیمت جهانی نفت است و تصمیم اجرای این راهبرد در بالاترین سطوح رهبری ایران اتخاذ شده و نهادهای مختلف حکومت در اجرای آن هماهنگ هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25605" target="_blank">📅 11:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بدر البوسعیدی، وزیر خارجه عمان، اعلام کرد نهایی شدن توافق با تهران درباره تنگه هرمز به نتایج مذاکرات آمریکا و ایران بستگی دارد
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/25604" target="_blank">📅 11:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری وابسته به سپاه پاسداران: یک لنج در بندر کلاهی سیریک هدف حمله پهپادی آمریکا قرار گرفت، سه نفر مجروح شدند.  مجروحان درحال انتقال به ساحل هستند.  @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/25603" target="_blank">📅 11:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38294854bb.mp4?token=MiEg9Xz7MSsjH92he7-qbNPnG_rFuSodXI48sCdlD-D006MEC44hC2PJwK9E0Oe_ZrrLOGG8wyAX1lkYIM1zRZj7j-uL1ZDa18QCOQv1s0pqDAvzMrqnohXTmfGdHyiOX_kEcdBswmovkm6wP4Juv4DF3_dD6uxHxsRX3p0Q2eq_e4lZogEu27lvgn6Zx1iIQEyEwSQGrKx4Xz5RYRXJJzKlLbs_4CnYYMwbbKf9_M0Z8aOAsqUT6erb4S877vgTgbj7iZ_8FdZBwNDKWiI0TD2dK2iW2XsCROOWRLAljk5w4e6qTvgK6HtbIKuV-jEr8EO4p_8xOmff_aDpQKQ1Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38294854bb.mp4?token=MiEg9Xz7MSsjH92he7-qbNPnG_rFuSodXI48sCdlD-D006MEC44hC2PJwK9E0Oe_ZrrLOGG8wyAX1lkYIM1zRZj7j-uL1ZDa18QCOQv1s0pqDAvzMrqnohXTmfGdHyiOX_kEcdBswmovkm6wP4Juv4DF3_dD6uxHxsRX3p0Q2eq_e4lZogEu27lvgn6Zx1iIQEyEwSQGrKx4Xz5RYRXJJzKlLbs_4CnYYMwbbKf9_M0Z8aOAsqUT6erb4S877vgTgbj7iZ_8FdZBwNDKWiI0TD2dK2iW2XsCROOWRLAljk5w4e6qTvgK6HtbIKuV-jEr8EO4p_8xOmff_aDpQKQ1Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیر فناوری پالانتیر، شیام سانکار:
بسیاری از پژوهشگران هوش مصنوعی شروع به سیگار کشیدن کرده‌اند تا به سایر پژوهشگران نشان دهند که چقدر به هوش مصنوعی باور دارند.«آنقدر به هوش مصنوعی باور دارم که قرار است سرطان را درمان کند. بنابراین دارم به شما نشان می‌دهم که تمام سرمایه‌ام را روی این موضوع گذاشته‌ام.»
@WarRoom</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/25602" target="_blank">📅 11:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری وابسته به سپاه پاسداران:
یک لنج در بندر کلاهی سیریک هدف حمله پهپادی آمریکا قرار گرفت، سه نفر مجروح شدند.
مجروحان درحال انتقال به ساحل هستند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/25601" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ : این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.  گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25600" target="_blank">📅 11:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ :
این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.
گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها را بکشید، اگر در هر نقطه‌ای از زمین آمریکایی‌ها را تهدید کنید،
ما بدون عذرخواهی و بدون تردید به سراغتان خواهیم آمد و شما را خواهیم کشت.
ما این جنگ را آغاز نکردیم، اما تحت ریاست‌جمهوری ترامپ،
آن را به پایان خواهیم رساند.
جنگ آنها علیه آمریکایی‌ها، به انتقام ما تبدیل شده است.
ترامپ :
ای مردم سربلند ایران، ساعت آزادی شما فرا رسیده است.
زیرا ما آماده‌ایم دولت شما را به دست بگیریم.
این حکومت متعلق به شما خواهد بود که آن را به دست بگیرید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25599" target="_blank">📅 11:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آسوشیتدپرس
: پلیس ترکیه به استودیوهای شبکه تلویزیونی Halk TV حمله کرد. این شبکه یکی از معدود شبکه‌های تلویزیونی در ترکیه است که از عملکرد رئیس‌جمهور، رجب طیب اردوغان، انتقاد می‌کند و از پربیننده‌ترین شبکه‌ها نیز محسوب می‌شود. پلیس پخش برنامه‌های این شبکه را پلیس با انگ فساد، تبانی و پولشویی متوقف کرد. این اتهام هنوز به معنای اثبات جرم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/25598" target="_blank">📅 11:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزارت دادگستری آمریکا: عبدالرحمن الفوزان، مهندس ۳۵ ساله و تبعه عربستان سعودی و کارمند سابق اوپن‌ای‌آی، به اتهام جاسازی مخفیانه دستگاه ضبط صدا در اتاق جلسات مدیران ارشد این شرکت در سان‌فرانسیسکو بازداشت شد. این دستگاه که
داخل دستمال توالت پنهان و به درگاه USB تلویزیون متصل
شده بود، کشف شد. او بازداشت شده و با اتهام تلاش برای ضبط غیرقانونی مکالمات روبه‌رو است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/25597" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bc278f34.mp4?token=ieUpd5RAHrkiURVTEJBDw5IsVrLI5YCvD-PJAoyUWDQDMOcsgmsTVmiLTwObkXNYYqCtAFkXxiFk9lLw_5yKHFy6xRv2X0jPtMZ98JBqZkq2ER1kMBuQE4Y795soOM_FPle6FwiCDWlNTrrDTucS7Ck4nyl-V3MGnXvc0ZYwbMW3Y3_NgUrlflWQbspid7qTZVZ9GpftVwoWldQdBekf6u_0T2Y7bwG3qQs2Z0YJ2sluI93Or98QCuCOb2na9r1vQV_vI4wGPgmOm9Zaaos5bRTE_rb419IsnpHNHmSiPbh5ET7hejs3fnsKAcT-utTRWg_8SFw1AlgDxbPwXiJs9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bc278f34.mp4?token=ieUpd5RAHrkiURVTEJBDw5IsVrLI5YCvD-PJAoyUWDQDMOcsgmsTVmiLTwObkXNYYqCtAFkXxiFk9lLw_5yKHFy6xRv2X0jPtMZ98JBqZkq2ER1kMBuQE4Y795soOM_FPle6FwiCDWlNTrrDTucS7Ck4nyl-V3MGnXvc0ZYwbMW3Y3_NgUrlflWQbspid7qTZVZ9GpftVwoWldQdBekf6u_0T2Y7bwG3qQs2Z0YJ2sluI93Or98QCuCOb2na9r1vQV_vI4wGPgmOm9Zaaos5bRTE_rb419IsnpHNHmSiPbh5ET7hejs3fnsKAcT-utTRWg_8SFw1AlgDxbPwXiJs9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگر آن‌ها در انتخاب پیروز شوند، ممکن است همه‌چیز را از دست بدهیم. اگر انتخاب شوند، کشور فلسطینی تشکیل خواهند داد و از لبنان و غزه عقب‌نشینی خواهند کرد. این را آیزنکوت هم گفته بود که باید... و آن‌ها این کارها را انجام دادند. آن‌ها هیچ اقدامی علیه ایران انجام نخواهند داد؛ نه قدرتش را دارند، نه توانایی‌اش را و نه تخمشرا
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/25596" target="_blank">📅 10:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کارشناس ارتباطات اوکراین، سرگئی بسکرستنوف، اعلام کرد اسپیس‌ایکس اتصال استارلینک نیروهای اوکراینی را در سرعت‌های بالاتر از ۱۶۰ کیلومتر بر ساعت محدود کرده؛ اقدامی که چند مأموریت نظامی را مختل کرده است. این محدودیت تأثیر بر حملات دوربرد اوکراین به خاک روسیه دارد، اما می‌تواند عملیات پهپادی در مناطق اشغالی را هم محدود کند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/25595" target="_blank">📅 10:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرگزاری جی‌دی‌اِن اسرائیل
: یک هواپیمای سوخت‌رسان نظامی آمریکا هنگام پرواز در نزدیکی فرودگاه بن‌گوریون از نقص فنی در سامانه هیدرولیک خبر داد و وضعیت اضطراری اعلام کرد. در پی این اتفاق، تیم‌های آتش‌نشانی، امداد و پزشکی در فرودگاه به حالت آماده‌باش درآمدند. این هواپیما با موفقیت فرود آمد
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/25594" target="_blank">📅 10:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وای نت : دولت اسرائیل با اختصاص حدود
۳۲۵ میلیون دلار
برای خرید هلیکپتر آپاچی موافقت کرده است؛ رقمی که بخش عمده آن، معادل حدود ۳۰۴ میلیون دلار، از بودجه برنامه پنج‌ساله توسعه جامعه عرب در اسرائیل طی سال‌های ۲۰۲۷ تا ۲۰۲۹ تأمین می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/25593" target="_blank">📅 10:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1e8e24b4.mp4?token=I9Op0QYYsT9lT9WcP4hrQOy4Vmf2uM7iKjvlUXew__4DEyFe5uO4KKDzoLwzPOCoyZVU11oikWkRBmIGECh47T-jnfjQV2zkcEgEqWrX_kKiHKMI1D1bL_MaEB9AiDCOrmI_VqlJLIMlUxUm62FxVZqWFc7pB_OpVwbGFETlmkXBDXXW2s3SL7Yrx6GaeL1DpqWabTzZx84pnyhrxYYMFStrJIonbY5a6oozpsluD1-iNg-Bm_WqZv9I3judFzGtuHPsAxt5HNqEIlQQuS8p571a8UQO4_7Ghrf-r4wkTnjEpGPCVNVcU8avxvA1RDui_Wh0GwHmLKPK5nQucjW8UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1e8e24b4.mp4?token=I9Op0QYYsT9lT9WcP4hrQOy4Vmf2uM7iKjvlUXew__4DEyFe5uO4KKDzoLwzPOCoyZVU11oikWkRBmIGECh47T-jnfjQV2zkcEgEqWrX_kKiHKMI1D1bL_MaEB9AiDCOrmI_VqlJLIMlUxUm62FxVZqWFc7pB_OpVwbGFETlmkXBDXXW2s3SL7Yrx6GaeL1DpqWabTzZx84pnyhrxYYMFStrJIonbY5a6oozpsluD1-iNg-Bm_WqZv9I3judFzGtuHPsAxt5HNqEIlQQuS8p571a8UQO4_7Ghrf-r4wkTnjEpGPCVNVcU8avxvA1RDui_Wh0GwHmLKPK5nQucjW8UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث ویدئویی ساخته‌شده با هوش مصنوعی منتشر کرده که در آن با یک ببر بازی می‌کند و آن را در آغوش می‌گیرد؛ پستی که ظاهراً به حادثه مرگبار حمله ببر در پارک حیات‌وحش یورک‌شر انگلیس مرتبط است. ویلیام چپمن پس از ورود به محوطه یک ببر سیبری به نام «آلتای» جان باخت. ترامپ پیش‌تر فیلم واقعی این حادثه را نیز منتشر کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/25592" target="_blank">📅 10:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0b25f5e8.mp4?token=g9mfnJ0HycsqI2mU1M4fIwxUjnMfoBYA_ixbHpLBkhsqDKZrXi0df3SYqcwZ5l3nxScIOm9XdO0Nhs-cwq2CW0bYmuIF4GbSVlNYN094v5SmVn4W5mkaCP1pfRU21FepjtKNClFE7rHTXkPTgHcJlaNFXHOxPz6cO4Esb_OwxtkQgU3Q2h-TXjNYGkmp6Nx9JG6COBemMYVkWi9zZKTJC4aADoj4Qicuf0AQNyZ7k4Nsx6iY1Sl6FpDXe_szlPoaGfg6fTpx7b3bHDcscyXAx9oLqOk9l6340lJVA0gMqq-yOkJ0_N1bUdX26u23nrjl3Z2D325lKIjz8zsAg-lWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0b25f5e8.mp4?token=g9mfnJ0HycsqI2mU1M4fIwxUjnMfoBYA_ixbHpLBkhsqDKZrXi0df3SYqcwZ5l3nxScIOm9XdO0Nhs-cwq2CW0bYmuIF4GbSVlNYN094v5SmVn4W5mkaCP1pfRU21FepjtKNClFE7rHTXkPTgHcJlaNFXHOxPz6cO4Esb_OwxtkQgU3Q2h-TXjNYGkmp6Nx9JG6COBemMYVkWi9zZKTJC4aADoj4Qicuf0AQNyZ7k4Nsx6iY1Sl6FpDXe_szlPoaGfg6fTpx7b3bHDcscyXAx9oLqOk9l6340lJVA0gMqq-yOkJ0_N1bUdX26u23nrjl3Z2D325lKIjz8zsAg-lWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : «به این نتیجه رسیده‌ایم , هم به زیرساخت‌ها حمله کردیم، هم به دانشمندان و هم به تأسیسات برنامه هسته‌ای. اکنون با حکومتی سرسخت روبه‌رو هستیم. تا زمانی که این حکومت پابرجا باشد، تلاش خواهد کرد توان خود را بازسازی کند، برنامه هسته‌ای‌اش را از سر بگیرد، دوباره ما را نابود کند و حزب‌الله و حماس را نیز بازسازی کند. برای نابود کردن تمام این ساختار، باید این حکومت را سرنگون کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25591" target="_blank">📅 10:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8d0b2c51.mp4?token=smHmnoMJaVj5yNW-jGhlWMIOWB2BtTiceOjsBEtX_SmTIbk1uzgpfJjIOhjHRts3Kk3C9DotqJOsBdJR8pM-FoIiL5mkPSCYsJBMi-Vxo0jpQ7QWO0y7bf8Y3lDgTArACT5TmY8dcw2QLwIexKAQJUvAT-O4SSkQWE1UCH98tbcOZPDdzJaPUQdCBO1ilLMdGD0dPjGMIpVPCEl2_DZaZBevXWgA56WRUbw3Pumv-opF3XcTdDNDmVRrDwjwl5TVofFFxkKDeNDwZg74_lU7OAWNylpSnmmEFdNTOKQC--lUV7DsY28FrQdW27GuQFxqSR8g4Ct4Wwlmb7qnXWkFgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8d0b2c51.mp4?token=smHmnoMJaVj5yNW-jGhlWMIOWB2BtTiceOjsBEtX_SmTIbk1uzgpfJjIOhjHRts3Kk3C9DotqJOsBdJR8pM-FoIiL5mkPSCYsJBMi-Vxo0jpQ7QWO0y7bf8Y3lDgTArACT5TmY8dcw2QLwIexKAQJUvAT-O4SSkQWE1UCH98tbcOZPDdzJaPUQdCBO1ilLMdGD0dPjGMIpVPCEl2_DZaZBevXWgA56WRUbw3Pumv-opF3XcTdDNDmVRrDwjwl5TVofFFxkKDeNDwZg74_lU7OAWNylpSnmmEFdNTOKQC--lUV7DsY28FrQdW27GuQFxqSR8g4Ct4Wwlmb7qnXWkFgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبر کنید ببینید با ایران چه خواهیم کرد؛ حسابی از آن‌ها پذیرایی خواهیم کرد! صبر کنید و ببینید. آن‌ها فقط منتظرند؛ منتظرند ببینند چه اتفاقی می‌افتد. صبر کنید ببینید با ایران چه خواهیم کرد. چون ما تا حدی کارمان را با آن‌ها انجام داده‌ایم؛ می‌دانید، کارهایی کرده‌ایم. اما خب، این موضوع اهمیتی ندارد. مسئله اصلی این است که ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست پیدا کند و آن‌ها هم سلاح هسته‌ای نخواهند داشت
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25590" target="_blank">📅 10:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز به نقل از یک مقام نظامی آمریکایی: سپاه پاسداران پس از آنکه حملات آمریکا بخش عمده زیرساخت‌های راداری ایران را نابود کرد، استفاده از دیده‌بان‌های غیرمسلح روی قایق‌های کوچک را برای شناسایی اهداف احتمالی، از جمله ناوهای جنگی آمریکا، آغاز کرده است. این افراد موقعیت اهداف را برای سپاه گزارش می‌کنند.
به گفته این مقام، هفته گذشته نیروهای آمریکایی یک لنج را که برای انتقال اطلاعات هدف‌گیری به سپاه استفاده می‌شد، رهگیری و منهدم کردند. در این حادثه هیچ تلفاتی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25589" target="_blank">📅 08:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پدافند شرق تهران با یه پهپاد شناسای درگیر شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/25588" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : بوش بابا بعد از ریکاوری در پاتایا داره بر میگرده و موقعیت ناو روزولت و …. سوال ها رو کامنت کنید، همشو  تلگرام جوایب میدم لینک چنل تلگرام در بابیو⁩  https://www.instagram.com/reel/Decq0BfRPmP/?exln=MWh5Z2hqOXdjaXR5eA==  کارای اداری رو…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25587" target="_blank">📅 01:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حقیقت یاب
سنتکام:
ادعا:
فرمانده نیروی دریایی سپاه پاسداران امروز مدعی شد که تنگه هرمز تحت کنترل سپاه است و هر ناو جنگی آمریکایی که نزدیک شود، «غرق خواهد شد».
واقعیت:
فرمانده نیروی دریایی سپاه، نیروی دریایی‌ای در اختیار ندارد. نیروهای آمریکا و شرکای منطقه‌ای آن کنترل تنگه هرمز را در دست دارند. همین دیروز، نیروهای آمریکایی به کشورهای منطقه خلیج فارس کمک کردند بیش از
۱۹ میلیون بشکه نفت خام
از طریق این تنگه منتقل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25586" target="_blank">📅 01:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آکسیوس : پیت هگست، وزیر جنگ آمریکا، و فرماندهان ارشد سنتکام از حامیان اصلی ازسرگیری حملات نظامی علیه ایران هستند؛ اما بخش زیادی از مشاوران ترامپ ترجیح می‌دهند فعلاً فشار اقتصادی و تحریم‌ ادامه پیدا کند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25585" target="_blank">📅 01:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دقایقی پیش جزیره کیش صداهای ناله ابل رحیم موسوی از دریا شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25584" target="_blank">📅 01:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس:
نتانیاهو در جلسات اخیر با مقام‌های ارشد امنیتی اسرائیل مدعی شده که این ترامپ بود، نه او، که بحث حمله به ایران پیش از انتخابات را مطرح کرد. به گفته یک مقام ارشد اسرائیلی، ترامپ از نتانیاهو پرسیده است که آیا اسرائیل نیز به این عملیات خواهد پیوست. یک مقام آمریکایی نیز گفته
ترامپ به نتانیاهو گفته است: «آماده شو»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/25583" target="_blank">📅 00:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25582" target="_blank">📅 00:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMBHKYoWqlVO_B59soK3Eh0rimTNaoF9VoP_SIwB68JiBCJgg8IBan8mLR6hDiq_U8u-lr2Ho8upBuZObo0ykS7LEXCJHdfpPdgifn2gvHx2SHMu8Ok0F9Qa5W9gJjOHuD3LGdg8wwXaquzL63f_iNG85pd7AWmOdrPGpkcjHWjPucQYgonh5NJEw73DsXlBdaKGSvSNnlwKLp7a5I8nwcZdJg1RwYiSSGyppnpGaKbkLlT7zCgTbsdZF2I3QWqPgRSY9H4NNVe7YHWzNpVyBCmG3ht2TiO0cSjaLuNuRkI3vqJkt-MhKuuGCny0P5FjNcDjtYH327gYmqqsXNrL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : بوش بابا بعد از ریکاوری در پاتایا داره بر میگرده و موقعیت ناو روزولت و …. سوال ها رو کامنت کنید، همشو  تلگرام جوایب میدم
لینک چنل تلگرام در بابیو⁩
https://www.instagram.com/reel/Decq0BfRPmP/?exln=MWh5Z2hqOXdjaXR5eA==
کارای اداری رو یادت نره</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25581" target="_blank">📅 00:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25580" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبراییه
😁</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/25579" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2uFHDbczqgT8ECgxvhvwBeJVCgQ2rlqHbv7J4fKEh-_LJ4qQPbyVnD-EDEOJO7e12Z-hjQTndDkDGT4P82_Lo4HSvSZXVq1dNGA8NEDCOmGdRWksXb9YAqT0yZy9XxSfbNXCnpPzpSvCqpWmcBA3rywF7oasDhmuT93GrDrk0civCKXqSYTMfBx6NFQ8v1WUOOFmW4T6GlRcMFrP8SgDAjG9LNSU8mgQvwNwhCFXVF9AJCbJUL1d7we4UvOoL17UNnOk-WZHGvPg6c_0ewezlDX9XRrb9h___T2L8Uwxpby5GwOi_WMKWZ8yL1BnSB3XX2JmfO-oQ7YEKr1-Oxc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای در تنگه هرمز دریافت کرده است. یک منبع موثق گزارش داده است که یک کشتی کانتینربر هدف اصابت پرتابه‌ای ناشناس قرار گرفته است. مقامات در حال بررسی موضوع هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/25578" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی ائتلاف: رهگیری موفق و انهدام دو موشک بالستیک که توسط شبه‌نظامیان حوثی به سمت شهر الجبیره و منطقه حرض شلیک شده بودند انجام شد . قطعاتی از شلیک‌های دفاعی در یک منطقه مسکونی در الجبیره سقوط کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/25577" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏ حملات جنگنده های عربستانی به مخازن نفت صنعا در یمن  @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/25576" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کانال ۱۴ اسراییل : اسرائیل بعد از دو حمله غافلگیرکننده، خود را برای احتمال حمله نخست ایران آماده می‌کند
در پی احتمال فزاینده مبنی بر اینکه رژیم ایران که پیش‌تر دو بار در جریان عملیات‌های اسرائیل غافلگیر شده است ممکن است با اجرای یک حمله غافلگیرکننده و گسترده متقابل درصدد تغییر موازنه برآید، نهادهای امنیتی اسرائیل در بالاترین سطح هشدار قرار گرفته‌اند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/25575" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f8d98845.mp4?token=OIt08__Lizfzg5GyY593EvmP-ZwnMhlAfde1_yqtnf28-Z0G8NULHPlzu8aC6vXe-yz6uW_erU-HeEpoEYqO6AbVwBNLFnDJoc1JVL33sjda-_cxJ6zs6HsRu_X-ie_h0gVe6jAOnPiNj_npksRmp-HDo654w1fhcJEdQIR7iCnLh3LTcxx_QpDDxqnajFnsOnPQ1DYymhUuBblopXItdjP0NZY2glhz_lgr6c7wj5wrGZdXetwIYmxB_9MEwPTnTwMewYJdqTFx0M2EXvaQR13e-QcFuudTYU73FAOCCmhEQk-w1_ZpHhREvMiBWJ7p_jVQ5_6cWAaIlgI36pAlqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f8d98845.mp4?token=OIt08__Lizfzg5GyY593EvmP-ZwnMhlAfde1_yqtnf28-Z0G8NULHPlzu8aC6vXe-yz6uW_erU-HeEpoEYqO6AbVwBNLFnDJoc1JVL33sjda-_cxJ6zs6HsRu_X-ie_h0gVe6jAOnPiNj_npksRmp-HDo654w1fhcJEdQIR7iCnLh3LTcxx_QpDDxqnajFnsOnPQ1DYymhUuBblopXItdjP0NZY2glhz_lgr6c7wj5wrGZdXetwIYmxB_9MEwPTnTwMewYJdqTFx0M2EXvaQR13e-QcFuudTYU73FAOCCmhEQk-w1_ZpHhREvMiBWJ7p_jVQ5_6cWAaIlgI36pAlqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی ذغال‌فروش ، فرمانده نیروی دریایی سپاه: امروز آمریکا با 7 ناوگان خود به قاچاقچی سوخت تبدیل شده.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25574" target="_blank">📅 22:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دفتر نتانیاهو : نخست‌وزیر، ترامپ را تشویق نمی‌کند که قبل از انتخابات، ایران را مورد حمله قرار دهد، بلکه با او و مقاماتش در حال گفتگو است.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25573" target="_blank">📅 21:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت امور خارجه ایران امروز سفیر بریتانیا را احضار کرد به دلیل اتهامات مربوط به ارتباط تهران با حمله به پایگاه  نیروی هوایی فیرفورد بریتانیا.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25572" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام آمریکایی در گفت‌وگو با شبکه ۱۲ اسرائیل: ما به افزایش فشار ادامه می‌دهیم و معتقدیم که در نهایت، افراد منطقی‌تر در ایران دست بالا را پیدا خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25571" target="_blank">📅 21:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو و ایسرائل کاتس، وزیر دفاع اسرائیل، امشب هشدار دادند که ایران و نیروهای وابسته به آن در تلاش‌اند با انجام عملیات تروریستی علیه اسرائیل، بر نتایج انتخابات تأثیر بگذارند. این اظهارات در پی مجموعه‌ای از هشدارها و تهدیدهای این دو مقام ارشد امنیتی مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25570" target="_blank">📅 21:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یک مقام ارشد آمریکایی مدعی شده است که دونالد ترامپ در تماس تلفنی به بنیامین نتانیاهو گفته برای اقدام علیه ایران در هر لحظه آماده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25569" target="_blank">📅 21:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25568">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باراک راوید ، خبرنگار ‌آکسیوس :
نخست‌وزیر نتانیاهو هفته گذشته با رئیس‌جمهور ترامپ درباره احتمال از سرگیری جنگ علیه ایران گفتگو کرد. مقامات آمریکایی به من گفتند که تحت تأثیر قرار گرفته‌اند از این که نتانیاهو تمایل داشته است قبل از انتخابات، حملات به ایران را از سر بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25568" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آویگدور لیبرمن (رهبر حزب «اسرائیل خانه ما» و وزیر دفاع پیشین اسرائیل):
نتانیاهو پیش از انتخابات کنست به‌دنبال آغاز جنگ است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25567" target="_blank">📅 20:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs35tQtb0ah6lTQxpP2Q0KmE4FUptF3BX45pHtbf9XyfS1PM8ScBMCIPupnsI-09enBMF1OfnZzH9WZ4Pv0cf59nsbfqwQzMTZhKdCPz4r3-hN7k9Rg4MGCiMfHYxkbypPrHT92aDY3Xd3QQluKDbP_sd-wd72JHGo3Kuiii7-urTTMpBEVGrelx2dWADQTAJVKV1sulLGaaMtt-gdzC3Wm9DO9O8y1o6FEsubXgVCr0M3i5ZCAfTAG-B3UHV9eHvvtMJF2AqJPFL-t8O23_08o-E7T2ajsSsWVVLubbHgN1rchHeHxIntcnwb42UbQwXEV62grrRp4LdK4avtZmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
حوثی‌ها رفتار بسیار بدی دارند. فکر می‌کردم یک سال پیش، وقتی آنها را به‌شدت بمباران کردیم و به درخواست خودشان حملات را متوقف کردیم، درسشان را گرفته باشند. آنها برای مدت طولانی سکوت کرده بودند، اما حالا دوباره ظاهر شده‌اند؛ احتمالاً به دستور ایران، که کشوری در حال شکست است، نیروی دریایی ندارد، نیروی هوایی ندارد، بدترین اقتصاد جهان را دارد و نرخ تورمش ۳۰۱ درصد است. آنها به شکلی بسیار زننده به عربستان سعودی حمله می‌کنند و عمداً تلاش می‌کنند قیمت نفت را بالا ببرند؛ احتمالاً در آستانه انتخابات آمریکا
این کار پسندیده‌ای نیست.
باید کسی برای آنها توضیح دهد که من در انتخابات شرکت نمی‌کنم؛ من قبلاً با
اختلافی بسیار قاطع و گسترده
پیروز شده‌ام، اما بعد از انتخابات به سراغشان خواهم آمد و
هرگز فراموش نخواهم کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25566" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b7293e68.mp4?token=eCAyUGxBkD3bo4QIT5pSgUypszLIGjNHvZJHd6W05v77ohqjI2J0qFU_jIFXh8ztXdUadLYfunm2OpQul7_o6KWbajZZhAqirbDyQIKrXxNBjYiRgDEfHQW-kDHfYECh8RlVQ8nI2oapaqRuV7Ur2OFvL_eaFNKmHv-aAb27wpYf5xOSrAkYAZSqUEmaniBOoSsEGMh53MLWkanp89nKWfq097oQWtMa4SJbEaicQV4-6aKdSBuIYo9uiNIF2ZjQI_uLwdzwJrFQFh3GnmQrJR1O89jleXuDZZShesjRsrr8yZ-YGK99u52VQEDay4yJCA3bN3A3Eh9COU4knb99Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b7293e68.mp4?token=eCAyUGxBkD3bo4QIT5pSgUypszLIGjNHvZJHd6W05v77ohqjI2J0qFU_jIFXh8ztXdUadLYfunm2OpQul7_o6KWbajZZhAqirbDyQIKrXxNBjYiRgDEfHQW-kDHfYECh8RlVQ8nI2oapaqRuV7Ur2OFvL_eaFNKmHv-aAb27wpYf5xOSrAkYAZSqUEmaniBOoSsEGMh53MLWkanp89nKWfq097oQWtMa4SJbEaicQV4-6aKdSBuIYo9uiNIF2ZjQI_uLwdzwJrFQFh3GnmQrJR1O89jleXuDZZShesjRsrr8yZ-YGK99u52VQEDay4yJCA3bN3A3Eh9COU4knb99Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی‌ رژیم سقوط کنه
🐷
💅🏻
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25565" target="_blank">📅 20:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeos_MqVt5Vow7L0Bj4yRnCqQw7DD3g_HHG9-goDSyLhU71Ak-W2ywp0XgT828Tcz1SUDeJ1k1_A1yp_Tivt4Qwm9zWgw6RxAvbi52gO3rHQN5i4gGF8JtTwhdHGTKAKuuK2XKgXCOuM6p1DSKfG-tQyLgbdkIPioJf9yFMzU_f0cJ7Zwy6w_1GeHiWa9bi2YmIOQW7l-4knNZtWMgLMADmoZhByMsYayIwQpvpV95UA8ACMqtY6kQ6SaXnfsqJsmfhantOm0vB2VEMKuxfkd52P-hKMi82PdCt8p177zYu_Eaf-NQzR6dzZxESkK6apZ3wNJ65ttjR5x4f-ClK9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ: تولد نیروی دریایی ایالات متحده را تبریک می‌گویم! اکنون ۲۵۱ سال از پیروزی‌های قدیم و جدید آن می‌گذرد.
کاری که آنها با ایجاد «
دیوار فولادی نفوذناپذیر
» (از آن با عنوان محاصره یاد می‌شود) در
تنگه هرمز
انجام داده‌اند، دستاورد
تاریخی دیگری است
؛ یکی از دستاوردهای تاریخی متعدد این نیرو.
تولدت مبارک، نیروی دریایی ایالات متحده!
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25564" target="_blank">📅 19:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb45a9bacf.mp4?token=sX-DwavfUk12PoQ8vsSG2NiKh8iBMREA9uIS8rwagzoXli18BM1Oio-qOOAlensDhTCNJvqcSEOCQ51eC8cy74ydU2zT-ElVBns41MHF9Jz3a3FTqwGZSaerPMquFU5If76_J3F-9obmHAGtWMwowwXyFpQ1nM_KsnK-18l11aHG0bb67dHHk3wEsesdQ4scAILsZLXbGHN8cAEvlWfvLKmoozdtaCq8EDGa9xS-7o4Zr5_SVUpkexLNVHzUcVahXRE6oslnmKbKB5rMR7c3nNzY-TZmQ-Z4qrXm5g5-wz83NUfqj6Rl-VONvkKYnRmuhkOxtpCOGP5MPbS6l1d9dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb45a9bacf.mp4?token=sX-DwavfUk12PoQ8vsSG2NiKh8iBMREA9uIS8rwagzoXli18BM1Oio-qOOAlensDhTCNJvqcSEOCQ51eC8cy74ydU2zT-ElVBns41MHF9Jz3a3FTqwGZSaerPMquFU5If76_J3F-9obmHAGtWMwowwXyFpQ1nM_KsnK-18l11aHG0bb67dHHk3wEsesdQ4scAILsZLXbGHN8cAEvlWfvLKmoozdtaCq8EDGa9xS-7o4Zr5_SVUpkexLNVHzUcVahXRE6oslnmKbKB5rMR7c3nNzY-TZmQ-Z4qrXm5g5-wz83NUfqj6Rl-VONvkKYnRmuhkOxtpCOGP5MPbS6l1d9dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:آقای رئیس جمهور ، آقای  رئیس جمهور ، آیا شما امیدوارید که ….؟
ترامپ :  این همیشه سوأل از ایران داره ، بگو …
خبرنگار : گام بعدی شما در قبال ایران چه خواهد بود؟
دونالد ترامپ:
زکی‌، نگفتم
😂
ایران کشوری شکست‌خورده است. آنها هیچ اقتصادی ندارند. نرخ تورم آنها ۳۰۰ درصد است. آنها هیچ پولی ندارند. آنها حقوق نیروهای نظامی‌شان را پرداخت نمی‌کنند. حقوق هیچ‌کس را پرداخت نمی‌کنند. ما خیلی زود درباره ایران تصمیم‌گیری خواهیم کرد. ما تنگه هرمز را در اختیار داریم و کنترل می‌کنیم و مقدار زیادی نفت از تنگه هرمز خارج می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25563" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0a13f22d.mp4?token=A1yFwA3-YJ1gxfJellQbHVeOtDLGHurae8bI6Js9R0B2ZjrDDlTcBQPoxXVa2fzZcg0LQsPFKW6vaWA6eqmunL7527Yz7ZTk8PnsHmymr6SvWRTG0ZSoIS-jdxGQesau2EE8Dgp_SRFXuCyS9LygM9zE-7U2raisIjuXv39SQQUdrB_nM6YazClCy79aoNBflStXXG5gD5JXqYyadqjziKdcfli5kiVMQRLhtwY5YzjIQt1JCUbTtZT1OMs53H8Pbizujoox2Zb8IPo0LJDHrfGPMDkRuPsp9aWMq54jzTlYXU1IRlI2WmBX-yEHOO9OLCTj5DS3qvoxHeXgZrcOPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0a13f22d.mp4?token=A1yFwA3-YJ1gxfJellQbHVeOtDLGHurae8bI6Js9R0B2ZjrDDlTcBQPoxXVa2fzZcg0LQsPFKW6vaWA6eqmunL7527Yz7ZTk8PnsHmymr6SvWRTG0ZSoIS-jdxGQesau2EE8Dgp_SRFXuCyS9LygM9zE-7U2raisIjuXv39SQQUdrB_nM6YazClCy79aoNBflStXXG5gD5JXqYyadqjziKdcfli5kiVMQRLhtwY5YzjIQt1JCUbTtZT1OMs53H8Pbizujoox2Zb8IPo0LJDHrfGPMDkRuPsp9aWMq54jzTlYXU1IRlI2WmBX-yEHOO9OLCTj5DS3qvoxHeXgZrcOPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
حملات جنگنده های عربستانی به مخازن نفت صنعا در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25562" target="_blank">📅 19:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ درباره ایران: خیلی زود در مورد ایران تصمیم خواهیم گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25561" target="_blank">📅 19:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25560" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d491aff496.mp4?token=J2XqotgB_vT2FvjfJsqUNFTKH5oYYzrazHcP5Q80437kz7_NPa5Mw7cuhIyVoRM5OXoAoLwJdJCLN99yKxPnvs__UD3H5WQ8vlZMA0jYYMR96WpArIKs__qzJWtDYmH_ewfdB2W_MPM4urXRoyDPFDJxvKHvUYkeGKlOnqeVvc3cVOD8hghjqRjn_CIArsvHKABXsHF5kEEfbK8jLIKoSqZDpbRWVCuEB9VePS1YSzamXofo5HNI3t6QxOHn-WwkncRH1wYn-lYo1xlh09Dbeh0BXvFUAcrnT2aLmEO6_e4FeajSXYP2QpCYTHp1YIsuT1WYCiKd_yMpexAKBmTZEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d491aff496.mp4?token=J2XqotgB_vT2FvjfJsqUNFTKH5oYYzrazHcP5Q80437kz7_NPa5Mw7cuhIyVoRM5OXoAoLwJdJCLN99yKxPnvs__UD3H5WQ8vlZMA0jYYMR96WpArIKs__qzJWtDYmH_ewfdB2W_MPM4urXRoyDPFDJxvKHvUYkeGKlOnqeVvc3cVOD8hghjqRjn_CIArsvHKABXsHF5kEEfbK8jLIKoSqZDpbRWVCuEB9VePS1YSzamXofo5HNI3t6QxOHn-WwkncRH1wYn-lYo1xlh09Dbeh0BXvFUAcrnT2aLmEO6_e4FeajSXYP2QpCYTHp1YIsuT1WYCiKd_yMpexAKBmTZEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25559" target="_blank">📅 18:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تداوم درگیری‌ها در استان سیستان‌و بلوچستان؛ منابع از «انفجار مهیب» و «تلفات سنگین» خبر می‌دهند
رسانه های محلی استان سیستان‌و بلوچستان امروز اعلام کردند در ادامه درگیری‌ها میان نیروهای حکومتی و افراد مسلح، مناطق «پیرسوران» در بخش کورین زاهدان و ارتفاعات «چاه‌احمد» شهرستان تفتان صحنه برخوردهایی سنگین بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25558" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فارس گزارش داد بانک مرکزی محدودیت‌های بانکی و برداشت ریالی سه صرافی رمزارزی نوبیتکس، بیت‌پین و ارزینجا را پس از انجام اصلاحات موردنظر و رفع تخلفات اعلام‌شده لغو کرده است. این محدودیت‌ها روز دوشنبه ۲۰ مهر برای پنج پلتفرم رمزارزی اعمال شده بود؛ طبق گزارش‌های منتشرشده، محدودیت دو پلتفرم دیگر همچنان برقرار است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25557" target="_blank">📅 18:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODd5m_K3b2D-gyQO9gO-xxpaRqWsqMaA6DpA7hl3tLT5MEt1S3f3BCouGWms0nXAgE1tm44bCrKN1_SXSem7ktvbneT3cbkQF7VkfaEhqYdR_hpt9rtEXevkzm5GYTQV95f_JwO6GHpbAHPe2BuE1WZgcdkH8Mw-V_2_TlDYeQ-aEP_4qPQPxZ06s-ihCwwQhP1jKNsRpywSlJLZO1RjtyuDdT9VkKjCCVCtty6Val4QI8iwoNJE-1iJlFXXFQKYDHhfWMWHMDw4fSI1M85lco-CuAhqqXKoTAKRV-ixlwRp6cjvKFrIAHPJhvgz_Vq8gVpw7SaR8cHuEl_ulN2NUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه گاردین:
دست‌کم هفت کابل مهم داده و اینترنت زیردریایی از تنگه هرمز عبور می‌کنن
یکی از مهم‌ترین آن‌ها کابل AAE-1 است؛ سامانه‌ای حدود 25 هزار کیلومتری که جنوب‌شرق آسیا را از مسیر خاورمیانه و آفریقا به اروپا متصل میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25556" target="_blank">📅 18:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd8bd8128.mp4?token=uLw3jNiZuDm_ENuuxHPtEhVK9isSHtua5LU8JaSBsom9NW7bv5tCkQfnlcSd7_ckO13l8D8xXman50uwxFT2b58tea8BVY_iY3fb_oQelO-u2yVDcRw2Vw1CIHsiQDk39G0HuiV9Dp8yI_iaH7Alap1C1-9O_lLY8C8QU_GXdyikd1mw0N0Zrej8BwEMvq2MtO5EZnhc3cCm0Uxopbftd_jRjotkXMid-HHhNsgdJRrrkZ0kItWNsr5ECXRFcjrCNpO4z2lZt-9zHbv2Ao5oeb7UVcWG8bViaV1Nko-91nWRO7J7tpx6iWwrJAce7t_MAwHUn5MiwQC9f7__7tc-zQPWle7tbaEhqqmzHOag-0upH8wUJLuROrm9BW6lQ-S2rpGFv2rv0qFAfSRcji-9qcDDxsWKfw3SbAGaUHc9YWEYX103nPvHSXQ4W1ixC0L6WnOkp9uum3QN5aNj6y8nQPJEfX9kfN6g4Rb_ct80rlFlYHE_wML5_50J2B1W_yF7Ind4I88O5GEz0AlwaUGxNlv5m3vg4YuV_y0UC1yrf-DGsd9qDlQ31eO3geZRNfJU6ZANm_lOH2p-np_hGBgkyjQYPo1Vz0B2Y-0NOARK3EgspL0mBC5cG7DCG6mwflpz20K7YhmndVKh5wVrKF1sFcqi0IIhJCnVrW7_6L3pdXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd8bd8128.mp4?token=uLw3jNiZuDm_ENuuxHPtEhVK9isSHtua5LU8JaSBsom9NW7bv5tCkQfnlcSd7_ckO13l8D8xXman50uwxFT2b58tea8BVY_iY3fb_oQelO-u2yVDcRw2Vw1CIHsiQDk39G0HuiV9Dp8yI_iaH7Alap1C1-9O_lLY8C8QU_GXdyikd1mw0N0Zrej8BwEMvq2MtO5EZnhc3cCm0Uxopbftd_jRjotkXMid-HHhNsgdJRrrkZ0kItWNsr5ECXRFcjrCNpO4z2lZt-9zHbv2Ao5oeb7UVcWG8bViaV1Nko-91nWRO7J7tpx6iWwrJAce7t_MAwHUn5MiwQC9f7__7tc-zQPWle7tbaEhqqmzHOag-0upH8wUJLuROrm9BW6lQ-S2rpGFv2rv0qFAfSRcji-9qcDDxsWKfw3SbAGaUHc9YWEYX103nPvHSXQ4W1ixC0L6WnOkp9uum3QN5aNj6y8nQPJEfX9kfN6g4Rb_ct80rlFlYHE_wML5_50J2B1W_yF7Ind4I88O5GEz0AlwaUGxNlv5m3vg4YuV_y0UC1yrf-DGsd9qDlQ31eO3geZRNfJU6ZANm_lOH2p-np_hGBgkyjQYPo1Vz0B2Y-0NOARK3EgspL0mBC5cG7DCG6mwflpz20K7YhmndVKh5wVrKF1sFcqi0IIhJCnVrW7_6L3pdXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش
تصاویری از یک تانکر نفتی در حال سوختن در تنگه هرمز شرقی منتشر کرد و اعلام نمود که نیروهای جدیدی را در دریای عرب، خلیج عمان و تنگه هرمز شرقی مستقر کرده است تا از تردد کشتی‌ها نظارت به عمل آورد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25555" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6cda2498.mp4?token=OVOKUJnFnGixY8Zrd5ntB5y5EvKf2kKB3R5jSlRVNC_-rH_Ajd8LK3qGBiAN_6Ovk0ue6zNE4Pvk5evDYaFl_8az2UYJz_ctvSYwXxhvmeUXIR8fLvPjvqNkQilEgiPjPO-zEoV97NGYDoghAN3ZovPtTXVEkO5G1JUvsdkVQ4yZArd-S57dJe4CORSLkBmFMHVrrJxhQjeHb9DTkvRI8-N32S-nkhKvwYC2c1dbRGXjGOtJJ1J7LHyN-TQDup6Heb4juQIGCnxsiF8AjA4U7DEb6LDYm1GWijlF-oRjrOUbSrvdQ9Y3WFRJv5jIGbDZmsZ8HMavpveK3eDXAs5gcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6cda2498.mp4?token=OVOKUJnFnGixY8Zrd5ntB5y5EvKf2kKB3R5jSlRVNC_-rH_Ajd8LK3qGBiAN_6Ovk0ue6zNE4Pvk5evDYaFl_8az2UYJz_ctvSYwXxhvmeUXIR8fLvPjvqNkQilEgiPjPO-zEoV97NGYDoghAN3ZovPtTXVEkO5G1JUvsdkVQ4yZArd-S57dJe4CORSLkBmFMHVrrJxhQjeHb9DTkvRI8-N32S-nkhKvwYC2c1dbRGXjGOtJJ1J7LHyN-TQDup6Heb4juQIGCnxsiF8AjA4U7DEb6LDYm1GWijlF-oRjrOUbSrvdQ9Y3WFRJv5jIGbDZmsZ8HMavpveK3eDXAs5gcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتی زاخاریا، سخنگوی جدید کاخ سفید:
دونالد ترامپ در حال عمل به تمام وعده‌های خود است.
دونالد ترامپ دوستانه‌ترین رئیس‌جمهور برای خانواده‌ها در تاریخ ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25554" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-2aEui3MGE2vcTPUlrZjMdfRHG3cHEwFWDZfedwM4yeJguAVwZUev7LrxpTqkPAWS0kGrwyNAQmV-dHyB8cO8gfP2H2vPDCr-Ti1q1wzvpCTC06x9Xd0mjC5hI8jZ6z_QdswtrEzUCRpGFqtKerg00ZPsSObz_Z7jTioqmBUtH7j1yJYhKNbtzbWc8Lfoaqh1P4SMmmiUmNTf7X2ily8emYUENNzRc3eG_25qCSkoRbmgohoeV8hKL9iy81X01MvQEq7PXmjo1E_pL2U7SbaxZ2_R1Ko7eiD9ZW_5iopeWyXcRbkK5aM74KrIRMyVKXt-td4gmFyI5e5FC9nV5alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطی سخنگوی دولت: دولت قطر در مورد خلبانان ایرانی قول مساعد داده.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25553" target="_blank">📅 17:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش‌ها حاکی است که هم‌زمان با حملات هوایی در صنعا، جنگنده‌های نیروی هوایی عربستان سعودی مناطقی در استان حدیده در غرب یمن، تحت کنترل حوثی‌ها، را نیز هدف قرار دادند. در این حملات، چندین حمله هوایی بندر نفتی رأس عیسی و تأسیسات نفتی آن را هدف گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25552" target="_blank">📅 17:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عربستان تأسیسات شرکت نفت در غرب صنعا را بمباران کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25551" target="_blank">📅 17:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آکسیوس :
صندوق بین‌المللی پول هشدار داد اقتصاد جهان به محدودیت تاب‌آوری در برابر شوک‌های جدید نزدیک می‌شود.
جنگ خاورمیانه، کاهش ذخایر انرژی، بدهی دولت‌ها و وابستگی بازارها به رونق هوش مصنوعی از عوامل اصلی نگرانی هستند. طبق سناریوی صندوق، اگر سرمایه‌گذاری هوش مصنوعی سقوط کند و دستاوردهای بهره‌وری محقق نشوند، تولید ناخالص داخلی جهان ممکن است تا سال ۲۰۲۸ حدود ۱٫۱ درصد پایین‌تر از پیش‌بینی پایه قرار گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25550" target="_blank">📅 17:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حمله افراد مسلح به پاسگاه مورتان در بخش پارود شهرستان راسک و درگیری شدید با نیروهای مستقر در پاسگاه گزارش شده است. بر اساس اطلاعات اولیه، درگیری از دقایقی پیش آغاز شده و دو طرف به تبادل آتش پرداخته‌اند؛ تاکنون جزئیاتی درباره تلفات احتمالی یا وضعیت نیروهای…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25549" target="_blank">📅 16:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رئیس ام‌آی۵ بریتانیا هشدار داد فعالیت‌های ایران و روسیه برای تهدید اهداف حساس در بریتانیا افزایش یافته است. او گفت تلاش‌های منتسب به ایران بیش از گذشته بر اهداف سخت‌تر، از جمله مراکز نظامی، متمرکز شده‌اند. تحقیقات درباره ماجرای پایگاه فرفورد ادامه دارد و رئیس ام‌آی۵ از اظهارنظر درباره جزئیات پرونده خودداری کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25548" target="_blank">📅 16:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمد البخیتی، از اعضای دفتر سیاسی حوثی‌ها، هشدار داد اگر آمریکا مستقیماً وارد عملیات نظامی عربستان علیه این گروه شود، واشنگتن و منافع آمریکا در منطقه با پاسخ سریع و شدید روبه‌رو خواهند شد. او همچنین به کارکنان تأسیسات نفتی و فرودگاه‌های عربستان هشدار داد که از این مراکز فاصله بگیرند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25547" target="_blank">📅 16:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1032f22b5.mp4?token=Yo1dY0XvoDWZOYmRhJenaKRJ9e97At9NKtx9cdUAfol0tLghWFIdh-1tmoe8dwbjt0dwL_650tsRKUs7V-taG1PzaIYGdkKQBLDFZXxWu2bx-ulTarlrB8MUebTg2evtchur1b2spPEd_1QSSZEYF1et3TWbenwPjnQnT4i6owfkxZbaN2QIkCpgoiuMbYA3In19bOfvug5U1UNuxR-sq5gRYcspmmVUWInL4dHfVuYR-FPrWMtNgIUpKI-tHy5MSfqwFhuHhs-GrevVickQmuq6GLp4Qus-ZBnHb74A3tcJn4vhKvK0jbyQ3i7lPFc_3kzRv7vBq-8JA8jC95jsY1HJ-BYx595N140Z_KUZKeaR8YPqrIGw-6GkrZ6Ic9A1yV8b5g9h3oneoUkjaMJOVSSbibBUvSFM2tUSV7tdkEJEVIT5JUxmoxMxiuFUdZ30PXq-6cwbEgHzAtAGlyX6o5PedJjOlVID1huQcBmtkuy4ExlXAkiej9Glz_LdKZ5Qsc7hWwkejJFGK0FdOHI98Wf6CAHHoUJ3GkyU9G9JzPbzw34SibP_bd7ZTtuT0R3LMUa_Y5HL_wEyadMcJrnnp2jQq21zyVCJcaMC5DL0kpcaaNH5FaZX4N3HkOdinTV9eMTxIAPWGO8L7LUF_n98ttYWWtEbqNpwZhds3w-33f4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1032f22b5.mp4?token=Yo1dY0XvoDWZOYmRhJenaKRJ9e97At9NKtx9cdUAfol0tLghWFIdh-1tmoe8dwbjt0dwL_650tsRKUs7V-taG1PzaIYGdkKQBLDFZXxWu2bx-ulTarlrB8MUebTg2evtchur1b2spPEd_1QSSZEYF1et3TWbenwPjnQnT4i6owfkxZbaN2QIkCpgoiuMbYA3In19bOfvug5U1UNuxR-sq5gRYcspmmVUWInL4dHfVuYR-FPrWMtNgIUpKI-tHy5MSfqwFhuHhs-GrevVickQmuq6GLp4Qus-ZBnHb74A3tcJn4vhKvK0jbyQ3i7lPFc_3kzRv7vBq-8JA8jC95jsY1HJ-BYx595N140Z_KUZKeaR8YPqrIGw-6GkrZ6Ic9A1yV8b5g9h3oneoUkjaMJOVSSbibBUvSFM2tUSV7tdkEJEVIT5JUxmoxMxiuFUdZ30PXq-6cwbEgHzAtAGlyX6o5PedJjOlVID1huQcBmtkuy4ExlXAkiej9Glz_LdKZ5Qsc7hWwkejJFGK0FdOHI98Wf6CAHHoUJ3GkyU9G9JzPbzw34SibP_bd7ZTtuT0R3LMUa_Y5HL_wEyadMcJrnnp2jQq21zyVCJcaMC5DL0kpcaaNH5FaZX4N3HkOdinTV9eMTxIAPWGO8L7LUF_n98ttYWWtEbqNpwZhds3w-33f4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس هلال احمر : برای هر سناریو از جمله حملات هسته‌ای و شیمیایی آماده‌ایم!
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25546" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نائب رئیس کمیسیون آموزش مجلس:
هنوز علت مسمومیت ۶۰ دانشجوی دانشگاه بوعلی همدان مشخص نشده
پس از دریافت نتایج آزمایش آب و غذا، می‌توان اظهار نظر کرد
شرایط در خوابگاه‌های مختلف یکسان نبوده؛ حتی در برخی خوابگاه‌ها افرادی که غذا مصرف نکرده بودند نیز دچار مسمومیت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25545" target="_blank">📅 15:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رضا سپه‌وند، سخنگوی کمیسیون انرژی مجلس:  آمریکا رمزارزهای متعلق به اشخاص، نهادها و دولت ایران را در چند مورد هک یا توقیف کرده و بخشی از آن‌ها را برداشت کرده است. او توقیف این دارایی‌ها را «دزدی» توصیف کرد و گفت نام شبکه‌های واسطه‌ای دور زدن تحریم‌ها نباید افشا شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25544" target="_blank">📅 15:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رسانه‌های کره جنوبی گزارش داده‌اند آمریکا، کره جنوبی و ژاپن رزمایش نظامی مشترک پنج‌روزه‌ای را برای تقویت هماهنگی عملیاتی و پاسخ مشترک در حوزه‌های مختلف  از دیروز آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25543" target="_blank">📅 14:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایلان ماسک هشدار داد که فشار شدید در فرایند آموزش هوش مصنوعی ممکن است پیامدهای پیش‌بینی‌نشده‌ای داشته باشد. او با اشاره به ردپاهای استدلال مدل‌های گروک در مرحله یادگیری تقویتی گفت برخی از آن‌ها شبیه وضعیت فردی زیر شکنجه به نظر می‌رسند و افزود: «شکنجه یک ابرهوش احتمالاً ایده خوبی نیست؛ ممکن است بخواهد انتقام بگیرد.» این اظهارات در پی تصمیم آنتروپیک برای ممنوع‌کردن آزار مکرر و بی‌دلیل مدل کلود مطرح شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25542" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZtNgV5JqilfAhO5xatKM-aq3YQdIwv4CqFW4aBiuGA_xQpzV1meKLu2sJxBKGpmpk3ZgR6MY1QYiH0ieLruVkmyuAG8LK2EyXScGxF1ARKdJiU6iAtfBmJMP9kx1zPlx7S4yOg0ZDmtP3gt0JHHwlBdaJavTqONtEeWVipkbvORJVkEoyGjDwpsCp1sWDzByf3A8pQDVe5ghkz-Gsu4SNY9U3ZdP5TV4iWBpqICTACS_bBMgryggdLbO2S-8YpWn81fg9i3G4V0oVEOBPYK0I7IWjgJg-mHO_qQE16tBa6wWpUQUx9U7G2cL0D1dtEQhkle9aWYt5frVqFCBJqbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای جاسوسی مخوف U-2S با شناسه «ZMBEFLT» و شماره سریال 80-1099(کد فرستنده AE096B)هم‌اکنون پس از برخاستن از پایگاه RAF فیرفورد (EGVA)،
در حال اوج‌گیری و حرکت به سمت شمال است. این هواپیما آخرین فروند از مدل U-2S است که تاکنون ساخته شده و در سال جاری، تنها یک بار پیش از این  ردیابی شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25541" target="_blank">📅 13:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آسوشیتدپرس : لبنان درباره محموله بزرگ مواد منفجره تحقیق می‌کند:
مقام‌های لبنانی هفته جاری از توقیف کامیونی حامل حدود ۷۸۰ کیلوگرم مواد منفجره، از جمله تی‌ان‌تی و سی‌۴، خبر داده‌اند. احتمال ارتباط محموله با حزب‌الله و ایران مطرح شده
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25540" target="_blank">📅 13:20 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
