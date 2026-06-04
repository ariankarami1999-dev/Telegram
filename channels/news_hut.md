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
<img src="https://cdn4.telesco.pe/file/X8NG3rU_VPDH4CQ8f8kwC71K2QnnyQN67trcyFtZwgo_RqpdHEOn9hjksb_PHK0m89suYa3t0TN9O585AMzNXfMAHoAiApcTlkWlRd8zUn8Osi6VJO0Ak8W8HwsGcxLsJP6_NjTe9mQzFmqdrPFw9QiRniDYEEtlPSN-hW08tSpB8HwNT0t95WbskzwyYs70iyuEBhzs8OuMb-692oq1eyAwjcsTVRwx8aT5s92qxA_1d4eRQUFSHP0uPy95vhrNYIU9LWYQFYKQ0qRn1m44RWmuatPrv8eDD3PiHHkOVY6DeFYy5WhXoNrtg1jpgDzNHktzfixmVJU9yx1kwM2Q_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 229K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 05:13:01</div>
<hr>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce5X2rIXdp0Ty3x6kiXL9QQelw70iE6pjNynlEBWJ6hZFyWPHpf8KRkqyGfMV1FRwBCtCufvgiRP63PbII_fHPjcznroR_OSrTBRKCbtkBaBf-EAirTPLwkYzyLU7tDDm4LYVHLryMUAl8a5aUoZBxITXp8vhoBmmab0qRHlFVz9v4sVijBk0Ds3RDQHsLyx0JrW-jLW8-HID4RNgeS6VaYOEtHxfozi5gP6CrN5J6dLSwk0SeTgco9INXWgeVDhccHb3V5r5_oORbYmwQ4HulJam3Ri_21XETDZNb503vg_T3j6Teb6UvlSLlyEFfr5m_P6EgslktJd3rMsNWT6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBI0WcjaE_syMQSrkLGGORbIwldp7Kj58J4qMh3VZRSfoU6RQ8Vqr1q4XEqAig_xfeT_riXzXmEjMcnSm-WR8FlHN6yfeVO8Xq3-uhb7HYP8g6igo4hBHhSWShj5wb-tOU9sW_mEd1g12_7DDKUIQfoYWfRyZ5sPnP2xYN-seTl-pvonpNObcuV1gMEV2CNMST2EaX32gtky3FKfygCtHYJTZZJ814bvFAw3GrWXgYF8THBzVhXFD79wUm-lFeEn9ILm2FPVt5IkQ_jOFJLDKuA29sCwJoJncZOcHQkYgeoXAuAa7PDpjhup7xZwJyLA4af-DCYYDGVyw4JJxwDmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCB05YnHxNSzcIynJW2Od0o5FOhqEQ_n14IQ78JV3cWcvBakTopEpY64MKBb_qMEOWRFaMmCNTc3QgIvo-fJlSOXsgindcU05pJkx9yOaxT4Bfv93B_c9CneehY23UjLVVrOpfapyZJ_rUPiXEj3er31RgVnNLvzCU1nMa7Hg3BvkUW7iIsgvQp2N55PeczO7_rYynSqdKWvY65BkcBEmcWQ-ZL1SPO-ZKosqx5BF_HDBLpoSLKazYEo4CTYGS-jrMW4ZulHbramJV0tS7v2nDcuJpkhTtiTxApU-BsUXCv19aG_DvtUa7IirfPv14vhQYyORyoVglTFEUdcEYR_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در ۲۸ بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در ۷ بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپانیا  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر عراق  ۱.۸ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۲.۵ - ضریب : ۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fapL9i97oPPcxuF7b_ULQTDmnEz1ZTYDj1u6USZri8Kj6a5MkgpCKzNqP6klmYm_HtZOzEzSx9XlTC4S1m3Q7IHVAistgRXiJJkdI1Z4JsKueg8-O3G9gnFbkyA18WzvGIM16tOkDWUOGDE4JGafR-BRw35-GOxFsc895-VIaji00jB1-z9i8zL5wp6uiAgkWXyD5NDr0KkeTo60_DMeaWGot3sW3KtALBBTLWBZM1O_874nkEyuV7xY84K323lHCfpleSQS4Wfj40dW-crV6ItyrrY2VfAVNT2bP9mrYovhVervww5HVpD9sMvLB7RkUIX5S_DdFj2vmEDDd6iJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=moWV7jYC-8fjQdQvBOzH_dHg0RtrVs46AdjvBKS7HcqIy_IIJKYXSP9Ev3SqFXZTP0EjQgsan5zqtKJd7B866FnUVWhS6e9cSQHlDdtxMAudZ1BVF_QBouU9hJQq58TnJUWKs36iXOR4V1DIqHyjSoLRD-OWsG-mbgnJBT0Qfazl_WhLk38NBqfBfolvnmSTBWMhEUXApeTqxPmAqkHDL2lZe7ucQ0_N4rlYytcXm6w_ky7UJYbKcIIscHCzxS8x2MVAdfn7RWOupX5_52wKdKQj-9bDQhkBb3JPtzZMmiKFpJ-ttv2UaveQfSUvPp8zzUuPMoeg9R5FvNlthGI9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB76IeXPa1lGkgHpHQxLsJB2QTSRHyEqj5_3XW33SeHClwtHQetTF9Y8rLEw30udtq_7DL1AxjqIKSLoTjTZYnbX80FaWbqA9xO6uIAEKvhqD-KFTdufnOv_OVwN88c1UrvH02ajbIbyIVJkfrSRpSoQw612xKOqdCUtd6tdfkaAubYhJUy7AsARQA29FLUJ0ObTN37ZGVBWTBjG_a6gz7AdZ7Gc9YwTymZBXc3yzx-LvyzqZty4Yj_xbWc-baijckmT-xJ5ZuGcno6CHJC6ThCHG2d50KWD4h79KCBBAUpsef56-A0cf-fZrRnZPe-im6Zn_kJngMU_Eph2xds_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=I0YNFHPK2uvjaZQaGWQd-fgEPw_X5o9kLLbLk1qOfzIxLorAeNc9sQvXqqPfQUBFezXGZ_muwUEIcknLpHQNF5qhDGOwvJBufp7mBrjocNmRdo185Z78lHpIJF0ebm3CebBW5rwUFulbv5gvQR6zw9z7zzbPWQyJZjpqe6yUqYCBiwJ3OtRLJQQ2ITrujTHq1qOUYkYrjS3PcGLTF8zz6h9TZvZIlJ6lh5Ox-BcJNEi7Pk7L9G6saiDjr10BwkpIZaTTwhgMM9h0TK1L_VQXd1KKcaqetu5eu4-ugCzgIkxSlvR9qxHsYjKiJcNq5JFv277ozgdhxeOpNRIDpUMNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=ZH-ZBrSwcAwVHUPQYnR7japz3EIhL4EIp2qAevJFG3nRm1WArnYSCqlKanpwKFUFg_OmWG3U6OoMguSvtbMcJjIZEepdrNeyTFYAN29kcvJHJR_o0JzpC7PdDQatZzbqnK7tMvczVbrptsv3vx4YeqrLmyR835SOqUF83RLBm4kYiucI7muSAs9-XZXIBjEcIdkPyxMDRB-yOko_At-8o0DZBGDgrpyiocjjH0K5eqZPocGbt8UUG1mC4ixI-jzmDNPf72bP3d1tNF0EvK1yVN9B3a1YLidxAvkx2f7YmdmYzUNI9h6m53VrLfsULm8bo5R6iXA4TrAGkNHpb-74xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Q6AK0kulPOVm02YDbclbXVg7jrgyiaD0WvURwnVhJk4Apj4P7aOFsQm4f6dE1bBVKksyXeQkb0ZWVo6Nhjd6iQvR_NJ7MJUq8StweYEbDvdiuvKZKa9pulrZFBMXVHx3vlrLYYktj0ajgisvGNld960qlrRFDVg0llqsOfYWFDI7jFcELy0UEUxN_LkWBhama6Z3VVSRlMrEMYdY51Y6_s_kPYTocG-2NflZCPwZC3RqefLWHtVaCvZjz96oAU6kO4mp_uGRoqkuCedRT7xZJeXp1sYWuTvit6_evFJH-7vaE1Mt-VUbTh-mflXc5epY7Tg81UsOnMWtzyVdaB_9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=Q6AK0kulPOVm02YDbclbXVg7jrgyiaD0WvURwnVhJk4Apj4P7aOFsQm4f6dE1bBVKksyXeQkb0ZWVo6Nhjd6iQvR_NJ7MJUq8StweYEbDvdiuvKZKa9pulrZFBMXVHx3vlrLYYktj0ajgisvGNld960qlrRFDVg0llqsOfYWFDI7jFcELy0UEUxN_LkWBhama6Z3VVSRlMrEMYdY51Y6_s_kPYTocG-2NflZCPwZC3RqefLWHtVaCvZjz96oAU6kO4mp_uGRoqkuCedRT7xZJeXp1sYWuTvit6_evFJH-7vaE1Mt-VUbTh-mflXc5epY7Tg81UsOnMWtzyVdaB_9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU5vf017DH5K0K2rJ4sAfabkSz00gHeSs81upJzf0LAoqkefl0J6Ve2bMrFo1PmTST7Kzfk73sNLK7gmwc_OiEVv4CpsBwDnqkjsQ-viy4dio6_nZmOriU4CjxdE_PAegMaNygurlwZNrmR6ccxmGtFRKDHF_2cz8x7iB65gPGpbBxp5m9pG1QYfXKcap104alvbqICVECC9m1T6AOfBnvdCgnruCyL7FffACUk3eklJUI5EbZ7zyJXFlrRAVgLhJbddv5QSyT_q8L7LpbEcN5DmWdASKNxzyB8jj841qJ21YT-WVFt3FzDidTHuHukucIvXpXQpkKGzNBeDXi1XnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcVyN21k_wYF1g4C5KypUkxjqkC6ZfeF-_kKOTWqsueoiCjvfW0vJOZxaGu4iV0KHV40dGwS6Kjp2fQXnSUfRTUBYf-gU78KpypI7BH04Uo_9tlWoOb6yubEC1eVukkLD_BCG0Wa7Vbvh38sP8eBZNslkSrnoODhOK2FNn1PNpHvwqjO-AzjN6EZEZ6TVtHuIQMwrru8zJD5B3n7X7KuoPdXESQMV5sPPLKIJ69UJSapvqYf9tJw4L7hJwW2MQ0qQAYBHE3XNLq_Kp7g3cSwtUstj-MargDQ8Hh5RQZHNMNVfi-RbliF1Zi6g7UKf0OS-KeGzkxVA6JznU_77vNM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf8EEJgL-c6J3PSUgX5B6Bex75Sy2z9Moy3KWfKKf4rfxObf0ujs_kygjaiM-6-iCrpQrbR0v4vmdontBJkPmASYkBiWdK7vT7tPVbr4YLtoAuZOJxJYOFK9IeUUh4_d2IeEGoM-nUzbANnrmDl902ddoHiAGbMUuhJc05mXygpGoTXXgXBwvnLLGaWKLe8VsI_x8CwM26c71cVpu_mlU622-p4AfLhovIUAnH_LCHWLH9_XDh77p8vR9QHKjn3COwfT6QYL3OAEFM6I7Bc9E-hvlUY7QsGlRHm20iKm6iR4PALO-JL_Dnc0bWwTQY_LJQJgb7VrVqHW6tKUHPsnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLKYwPa5aNodM6sNNIXta2yqrB4YXJuLpJusGQGcG52Hl-CnYOQUXKjhaL_hL-5nH1_ABIdOa-egm9Vh8AK9WfWJuZMs3DgAko3w2pFbYFC0gNvQcb998ig2niHIv_kFLcqBVgMLRRLlQlOE5Qc8isb9L84lx1tmqRTnKGAoXO1__J1JCkRpX0PzQR9kr1CPOEeYv4HvoMHpsK0Udah5hLH8F7UoLNUnUBfuNw4vEI-0yZZQHIud_JjV_8uiGnn8sMrC_kKoDhW-_fxkDnev-x1RsKcPVZvpPgbmHM2bHnPmmBjke_joHFvEvi8xr4U-u85fC-PDFNX8zucDTy8XgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYmtunbqNlC3nor_cdTSGPV5BINoZTHo8GnRO6Z3_4QRAg4Yy0rGt0HqLjiN-BSKfVb7EKhvfcSff-M7Tzb17V9Wrpgsg6B9Qzg4M7X82Pz9RO2wvLPTuHvvGLwStxbd3Nu4xZsB-Ze-xFKIBWIjeNRAlxS55QVQeqLAVlEPrtR5M0UZT9lWllHlwHQboMPsZfntxrsbqfXfqNlFkI6YUjBLVKBjhlf8J-4M9Ov38KtdxNDll5XOgAhdAsk1BkaaV8t_Fl-OZmup2tQbgRB03JKVjgNVdSSYT-SZiLkvqJZyVr8G2q5RrXV0PCunJ7_ljPya1yBc4JlyhgHHst_h3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=AmID9XKlnl_cL5lHOPweTkGFEO3z413fNUc8g5A_VZuRBohGNSpts02e6JmIvGvIT9cwMYpp9DeDSmV3Dsr8I74RA_VQ0REz_t0wLHfXSW9VtV3NdM4XdFeIOIJXFDYSEeQ4T4qKJa4AUIYp9LZvGnbiaY9aCnz2LC-CgB10iLhMQnu6DavGvOgM3Lx521AenQ2fYivQyV7g3WkXmP9yiMvhdJGtL5NkvJNo--9fdVA6C3f6zlCi2euRzWKaFTVQaAGzo1HtJHKefnhGKQTM2t-2g21bbvZKCW8M0ldjwpN_3sv1SxSYoN9dSIofMIdmlQXIpOC0Rm0B8Ee59deOvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8fNzYt1TSwr5o6QgyLV-5jB1m7jEVmqsSTfHADlh7LMOcPGarkYq6jWTrbIeKK7x8G7KcjTzR-wWx1hSboVTDSC-Ki4TzK79n1JKzy1z4n8rVVNkgQAawj3Ajx-zPqZIJHuioN8vyhmc7lDI-YFxSnz-Gchy2k669nlKXvzI86NSzhD7fmtHjGLciHpPyQ7_u0aXXDu41cpl21j6IoiItpgDqE6TWJhTASUaD467dgoicuH1CN1YhbhgVZkfY-0JEIOK14c-M1Z4QKqGEvA9b-DOqAbICXU9L3S1YVsUMkRI2dNljvDBuVCibsFmm0m4aK1xForvnOW2Xj8phY-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLYY7DiTHhRR2VuVXo1P9aLjmIb5G0gLO-K1Z_2bTvDBM7DVxJEAbF-u8MnU7ifsu7Hdc2a5Cb597BMYoqrXwxI_fTcSd9bHQxXyv00Tv1icW-09W2ugWb6PzMIy3AJKQ49G9tywXyMxYCctR1xvp4Xn767ZCxssguNeMoFMeqQn5zc01b3LKx43LrhhwYtcmlOyvwxNVw5afQPBcPfasvEPSn9UjRAOPfE9bvSILngcwUwaPqCW9HVzCJh2mR_TKs0sodtnDOp60rzVZP5UuoehDcuCOfu-3bFVeux_azDJoKWIMvDemHyyMCKBp-vXmqPeEJdV_56gxTPEa4uB1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVzFa_lTmTw1h3Qg1e1MO6822jHmxdNo2qhrci8TKUioHWYhO_wdO3npkqBu1ha9wvNbIzerkifEljkFV3LLQNQni0nt3VpAfKfovxtODWxAFSJTz3iBR9R7HS-Wuhex4HcAYywONwyoWlaqFmzvP9wr6thUwSIR0KeAn1xm2SssnDgS95iMoYIEiMKoICVSqphRQ8dYWQnDJLwcAsPwxo6dsNGLklVvwJDjxF-yp08rJNgwBOseWyhHlCcfNZJeTHwI6n3zfuzUBVKeYVUPNKlfqMULwJqd-QbYNIhDRGv8gU-3DCQ4UD1QNPLX5srvqQunFLtffbUjWd7nWDSbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmo6T1EovbtJ4A0ooXOqj7brZ8xQgTGxXSWNi73zU0sFie8q2nJQqZVUyweuEoO9RT3ehwHfS1AJt4N0Dx7gEWbNUJ7WFIsF0C1qQADU8KspuICk2_R7mJzETqjU6MlbzsR5NQPvHw249P_5Nw2ei4KL2DFAjIPR_r8ZghF54T8FzwTK1ILNhoaV1AiL3ivdYesJCfNJydDbcEyFD5pDmlkLCl-Ykq6WUZeFHck4Q9RHK0QtX3cCR1CwT-j8PDFfsIEiQpPWVfWMAdbP7M3GawQ0CuXeAqiigojNXi5FsVPKd--SWI13hgTzXEOs_E-9MgrnD07MoEfv2vm-GFY2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cneegZuTcZTJCfGqG-t6tH-9_BO2OBVDiC0jvYhumQHnz6br95Rp4K5ADNUKsiVEPQGtoWeveTaFg_kxU8DFCXz-3ikRAItbIysOCFlY5_X0VB4cWNwzvVZOmqWXp-02kNUJgaa8Wz-N5KrYyoGxOMOC_AcUrM9GvVrIMyxQyunY1A2yfGZ1YQtUT0JUF7SWCasefGbZfOw9F5RK43vyNlTm3ftQUSLgAO_yS1O4G4a5OMqfauwY50R3EAS4161kTt3VQjkRyp9_hm89aYg9GCJHBUqBN4SptL0VqnRUynr3mkI6OOcZSijBimbcGYstARNp7yOXjcAIC2JdClIGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZL6UD5bDcADch78gBW1vbBAY5ETtOXxuPHHPOG219hQiVQ7S2CInh-rJxn0N6P6XguSQJIAIMQyI4JnzRI-UBx0mCObCe0xcmoRLwFo7-c4JgrsoOZ-IQhGEIkJAZedN4H0DM7F4YCfDfCxnsOWN8MsMH7O0DZfehHx61MuUptdLXPz7ybe2MTDyo8wvRBckSr7XhaXDsDaOMLo_BbQd33TVufwbBYcLESJru97FXT65E2aOeIpMGtaVtky8EbHRLI5tSEM7lrD-GlAJjumfsBAVOkT-XaRFiz1Va9JoJP1esFFDEzvSjnIut6NzTzFakWGPZwpvN1hzoyV1tEUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=OclkFxBB6M-JuYTHc3ebP5OnQFVb4iZK0l7wWyu7P4yge1fyGtKheYojBknE4qr3gndnTarO1ThNjMEWbHVcyhik9Id0esN8ZSQ22FiJyhtR7bXbZrRbuoW6N9GD_uMAisns9Jwrn38ieJc9S-tt4zuqnphPawdcripiGCEA0U99_fl_tb5seyS3YBaoZU3kDBwJVLtTzNwFN0pCmLiNA8ONIenpy3uRDbEzhfUhZ9BLSj8m_XsEyMC-3SEfABwQoWZ432drnwFIN97CmPZGFXCN3xh0oJZPg1iEt9QPaHIJ0DqfxfikSbtwMDcpQIU5ibJh1KAWKHmjPsytUlCNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=OclkFxBB6M-JuYTHc3ebP5OnQFVb4iZK0l7wWyu7P4yge1fyGtKheYojBknE4qr3gndnTarO1ThNjMEWbHVcyhik9Id0esN8ZSQ22FiJyhtR7bXbZrRbuoW6N9GD_uMAisns9Jwrn38ieJc9S-tt4zuqnphPawdcripiGCEA0U99_fl_tb5seyS3YBaoZU3kDBwJVLtTzNwFN0pCmLiNA8ONIenpy3uRDbEzhfUhZ9BLSj8m_XsEyMC-3SEfABwQoWZ432drnwFIN97CmPZGFXCN3xh0oJZPg1iEt9QPaHIJ0DqfxfikSbtwMDcpQIU5ibJh1KAWKHmjPsytUlCNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=W1TlL1axMLw9iSeA2uKqtnmmr572bgJ8ZhigPhfWdghQ9nJbNBKq6IOTWirn_KvBr0Gw-tdhzOdqILAFGX3npJZRb1z50CNJMo6lG0P6vn6qoGLTxhN1gPJBLGdI9DHRUl4JMTqeqUJ2GbPf2mPtJPki-eQ_6SUMZA4CzfJMSh0kLE6vNAKY9Or4VKm_jI1sbzLA94pia9hVhdlWPSW-nyHC7NhE6po5D1vkwX45HSydAArZJkZJT6P0LQPD8p7SBiyYPE2PI-xsPKAOOt52xyHbMbJJXBNpd7cIesf2N9AK3U_k5kvWyzqGxA2bYmwlowly-RwBIFaj_kZWFBwn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=W1TlL1axMLw9iSeA2uKqtnmmr572bgJ8ZhigPhfWdghQ9nJbNBKq6IOTWirn_KvBr0Gw-tdhzOdqILAFGX3npJZRb1z50CNJMo6lG0P6vn6qoGLTxhN1gPJBLGdI9DHRUl4JMTqeqUJ2GbPf2mPtJPki-eQ_6SUMZA4CzfJMSh0kLE6vNAKY9Or4VKm_jI1sbzLA94pia9hVhdlWPSW-nyHC7NhE6po5D1vkwX45HSydAArZJkZJT6P0LQPD8p7SBiyYPE2PI-xsPKAOOt52xyHbMbJJXBNpd7cIesf2N9AK3U_k5kvWyzqGxA2bYmwlowly-RwBIFaj_kZWFBwn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=SAZQEL48sz0ySzp6GPj7gqaogmqaheeMkV9ar_oNEOzKT1prwDYsEmuZIRp0HXLfdIvQNIHmgUAsdZ69Rd06UE7uaNA0qF7Dl4pWoryYRVTwif2JD9MXDkRpSGbvc5qlNrnWyOqr8wwNOlaSpwSHIzBTmMUi98TeHm91gBmVwitktQZqzhnKNRaKajdIcQN6eR4sPXZWXGzYmIfSRP451LrFLt5MW_RbyAAlMTsjleoJsTisNMmSQuevtZgfh_QcdM91saSptJ8WXFWrrd0DEsVIuU0CxdJUSzN12YqzaM2duA1OMDNoBRz7MIbqhdk_b6myH4jLGf691dezQZTjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=SAZQEL48sz0ySzp6GPj7gqaogmqaheeMkV9ar_oNEOzKT1prwDYsEmuZIRp0HXLfdIvQNIHmgUAsdZ69Rd06UE7uaNA0qF7Dl4pWoryYRVTwif2JD9MXDkRpSGbvc5qlNrnWyOqr8wwNOlaSpwSHIzBTmMUi98TeHm91gBmVwitktQZqzhnKNRaKajdIcQN6eR4sPXZWXGzYmIfSRP451LrFLt5MW_RbyAAlMTsjleoJsTisNMmSQuevtZgfh_QcdM91saSptJ8WXFWrrd0DEsVIuU0CxdJUSzN12YqzaM2duA1OMDNoBRz7MIbqhdk_b6myH4jLGf691dezQZTjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxbkNFwbjTy9L7IhpfpBlq3oEVBZculM5fhKmNnCVd9BtJw7m5mcc_LU2TXZmneWYtOEHIU7bRGsmuzkh-uyekmWjbSKgolxD1zdpq2POLtpOpFuILwHT4cI5V3PUnDGftRJ1qPVmA-I8Rc1aw31F3kzP-2_0wQl9q09OOk0NZr2UJX300OIFtIkUjPfdSKVYfCQtt_Vt-11UWHjk3yIRTC8NDyBfZ4jlIbQqLy4rDHLIUe9F4wIKcC0lEaQXAr20keAB673ye4HfMUn4DQEhKxP6V6SSIEk85X5WNW1avIwY7Hql4-pISUJ6_HIUABXXQisRsKHznPWNs-7xVUjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=P1CX-t5LRySdBhfvsJIXnxoHXxVhEhgZfNBEWmTSizvbvg6RkuinJZ8s2tNFw2tz3y9vpDtsild8tC6AjPg0CTCNHTHGpGkqx3DtHekNSWriy9PQ4HPc_8JpZTohQH9g7CH0ra7msBqvsQZEUmSMZbVjAoeotNO6K7t7Va1yaCnZsjyIzagHCDC2a_TcEqHUyTPKZl_J45ntEqAlRj3waMIF2mpDPE2ts_ZToy-Sv4aA27bLdJI7lCSZXxT-fRhzDiP41T8ZVeVWlUHbwzwW_UIuB44EkuC8RnYqemkK3mTKEhCs1IjxX2TEKuiJKJKumN4LMQyRl2Vf1LfJE2JUpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=P1CX-t5LRySdBhfvsJIXnxoHXxVhEhgZfNBEWmTSizvbvg6RkuinJZ8s2tNFw2tz3y9vpDtsild8tC6AjPg0CTCNHTHGpGkqx3DtHekNSWriy9PQ4HPc_8JpZTohQH9g7CH0ra7msBqvsQZEUmSMZbVjAoeotNO6K7t7Va1yaCnZsjyIzagHCDC2a_TcEqHUyTPKZl_J45ntEqAlRj3waMIF2mpDPE2ts_ZToy-Sv4aA27bLdJI7lCSZXxT-fRhzDiP41T8ZVeVWlUHbwzwW_UIuB44EkuC8RnYqemkK3mTKEhCs1IjxX2TEKuiJKJKumN4LMQyRl2Vf1LfJE2JUpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=LBJfGLy2-vOwka9K8ziUeRVMjySeXZeLrnaRAyUfyF4nYbq8YY4LZu050xHrCmeD1IQwlZaf0DaFmKFSkrEscQKHduAFHRKIcsewz0yGPMsnKMiQRBi-eJopwB90dssaSgRueTQLe9ofPbG42NQBP4Q5q1w9wgrMqd0UDDCPWT4JEEgmsnI2Bw_Yn669AGbRmwgR8FkZ-mQa9zZIab2-KNAhRMWO7_DVUCBfJeh8h9NSe5RszpG3E-3i-4fO1Sjbt2Tf2C50HfoE4LbBvZ2zTBrJcoj-qYXZjti-brLoeRpnarNd9SlGgziUXYdQoNX2sMmKDmou0cRiw2ZjJfMjXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=LBJfGLy2-vOwka9K8ziUeRVMjySeXZeLrnaRAyUfyF4nYbq8YY4LZu050xHrCmeD1IQwlZaf0DaFmKFSkrEscQKHduAFHRKIcsewz0yGPMsnKMiQRBi-eJopwB90dssaSgRueTQLe9ofPbG42NQBP4Q5q1w9wgrMqd0UDDCPWT4JEEgmsnI2Bw_Yn669AGbRmwgR8FkZ-mQa9zZIab2-KNAhRMWO7_DVUCBfJeh8h9NSe5RszpG3E-3i-4fO1Sjbt2Tf2C50HfoE4LbBvZ2zTBrJcoj-qYXZjti-brLoeRpnarNd9SlGgziUXYdQoNX2sMmKDmou0cRiw2ZjJfMjXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=kNeexuf4yV70dPw0y2rmj90LKVb0ovUjDllTU_mSdPjbcYP84X-Y_HHJODl-QpLzhVZlr870aR8qXFyVNY9sLa80n3d7vshuybXEgXCKE92o52qISKHDHQ6XfxNtS_l6tIklZ3yOTAoFUIm4CCRIZaYLqacaIWlmMA4FfNf-pZq2uI4lp-EVo-5w-Lrf_cpTT5mmTN3Pk0Ty6NJJCHy6jtinbJdi_m_5bAstpz4ROSk7V1GlQI8LAUQOYp8cqZH5Rd0CkcfvdDqr0AsS9IWOScaCdEgBq4xIhrAmMXxZqjRDw3IFsqZkHHO5HwcbbrxInGX5MJZ21ClZzTGvvJi5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=kNeexuf4yV70dPw0y2rmj90LKVb0ovUjDllTU_mSdPjbcYP84X-Y_HHJODl-QpLzhVZlr870aR8qXFyVNY9sLa80n3d7vshuybXEgXCKE92o52qISKHDHQ6XfxNtS_l6tIklZ3yOTAoFUIm4CCRIZaYLqacaIWlmMA4FfNf-pZq2uI4lp-EVo-5w-Lrf_cpTT5mmTN3Pk0Ty6NJJCHy6jtinbJdi_m_5bAstpz4ROSk7V1GlQI8LAUQOYp8cqZH5Rd0CkcfvdDqr0AsS9IWOScaCdEgBq4xIhrAmMXxZqjRDw3IFsqZkHHO5HwcbbrxInGX5MJZ21ClZzTGvvJi5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=loEK6YkxcrOO08LqFCjb77EnbPdQGmNPWFIkljWxE3jZX4dU3OaD6VCVN3yyL9gYKXzA1dRoAHju1hw3SqCOj_CjOJVshpJRLwh8MD4NUmZXMb2fF6JGihMyZeqepc0Z0YCfBbPpll3M373sg_donxs04FmCfCTIK0W6GYpO1SYPTZMpfJJkxKOYJXm1IZPYmdldTRcjLG2BR7O7tUTtZAKc_0kbtBZpxjJhTqEOLie5BqLWF0ME4MjOF6Wzg0Fm7WLL0lkogEHFkYBzZdPY8_kTGXRG1QVwN9j29qpT29znHWITXhhNZ3pIl0zqH6UAjof7dbrF034d2_22wv5xRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=loEK6YkxcrOO08LqFCjb77EnbPdQGmNPWFIkljWxE3jZX4dU3OaD6VCVN3yyL9gYKXzA1dRoAHju1hw3SqCOj_CjOJVshpJRLwh8MD4NUmZXMb2fF6JGihMyZeqepc0Z0YCfBbPpll3M373sg_donxs04FmCfCTIK0W6GYpO1SYPTZMpfJJkxKOYJXm1IZPYmdldTRcjLG2BR7O7tUTtZAKc_0kbtBZpxjJhTqEOLie5BqLWF0ME4MjOF6Wzg0Fm7WLL0lkogEHFkYBzZdPY8_kTGXRG1QVwN9j29qpT29znHWITXhhNZ3pIl0zqH6UAjof7dbrF034d2_22wv5xRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkZY8IJnVEcQ50o5nVYB9OkhunELIIgKq2vYN6Oo-mBolZEotWhvzYwzIUo0ap7EXJDyofQhUP5f1_J3FU1wQ4coQEQcjhP9W6s48SxFWXad_2xPNaSy1Zpf9SxxYATWiKEOC2tcSg4DscHHTIWXAQs5RdpAAtuLaq7a4w0gnD5R6fZVETDxVlMSbCXaIWL9UUxiL2E-kUaoE59NO9v6W8oEHHXFpfaFpn1MRfWGgc09ySDxpypLrPAaU4XWs9UyO_MH2bpwvDwDSoQwZ2k9lhmwuW9l4w9xTt_6E1zTLoskistphe5RwHUrr7OaFD4RSi7YIxhHCf5yjXRhxKTFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6DIkB45xDAgY7d22bAuwG3efymaaaoBHByfk62_fSbmyTO7ZanArE1xjZlKGhiMKhrluv5LYXX592gHlU0qF_BtvQckgvm0oMDq_xv-cDpofZZXWji6X_tbiMA8NvdE0sjMdxCnHYXOsh8IUAtTGHHfik-7q81yVFjRXBaaGLI9Xt1bq2wCgEc-SWy2nRnK8V9b_DNRnANKIMllE1at2sjk6rbFAX6Ny9oVt9G6biSyxfrBFHFmkCJPI7q7VJD33vsIGimdp3I6RZf7xgKgDaaX2vYOqNuJ7Y5QcPuJy_qCw1OU5J2Hpiom6MYJY8zuFswc6oInmm4v6dtCzLEFqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLeV0vy3F1R1Us_twdH2DQxZNYO138FR-3uWiUtS2XoCZOT-DAlDuzTKoXawYnQqZo21AzaOE6IfNtZPUBQ8XV-XX9AAuHoAPEFf99ZagTOgy6bZcRhTTh_bEl__HEYjn8nPvYDmBNY2s_dCdstW2lE_FbCgZRsMAQ9Rv9iiBqMzjZiI4e0YWKU39jiExRQWW_pVgrJaL4akEiDb_Y_sRXBMp3y1zQZf5vvKSb3BMmZhb-2uBdLnL9a5XgEIuMgo1eWwkMK0eWQocXurCNG2zjdNqeXW4O2Nbz9bzdzMcmJFX8MNzEij7nMbHwn4hWLoinbuSJKT9O72OL5jAwteNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAkZ2t_c0BPyQGCZsfm1Vx6RHnxyUlwIld-SpWwv6XIVyszzVUq3CURKMdwx4uL_rjdVb_WnYB0K8udU9fv2qGgOj-A4MG_WYyVwbwrVCLjQEcaf4XY7nN4vzMjY-gI1EN18Yuk9A5a3GWLNmT3WZIcyIqdUOVyVHchqyO61J5rgcbnXukL6hlmBjbWTRrXNXgaeJ9BuGTH5ru7GL-NRjR8QDvcZNywMPfbeQhk1SrA5hBM19kkmM0Yetn5z6PV8rN37_gM50RCrmrz59yjDO5XUtrK52e04aviB8sifMh5VJagoLumJ6-dGa3ukGEuInoCS7ouGIjKNlv9qjjlRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvcMnjokky5KYO1iSOwRnARwBTz1So3gKEzVfqF-R8Qg7uxilUk1dGait5Su5wcvbTSiEIm068F6pXRg8Cb0wX_1WYkbi6xn7WF7Zkzar220yP6Uj5bF3YJPdIfA_ZdyJUYcutZvNOgmnQAhYEms60xor0Cojv_6NNsoY233S79HiUP8jhy8zN_eCrFXTEL9tZfXc2RP5wedkM2Zu8-O63OxgZyZjy8PdVPpHznXzWRHkx1w3IwzBgBOYfUs81MFUMnRtUmI6ng17r5Uba9F_8tSGQcJyjGBX6RgFVKMV1FNSit72Ac8U4vpEAO2oGhbyl2VZbTZtUZqX3kFaGvVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN_rMsX_zGDsMztWySpvMclaR7ejyiDDbO6vEyyAs5wz3oEyKwO4_kYfGUBUEZ9YYP4X-Pepwi7svKF1aE8WywxjXYkzLcxDGiwMvNNvOII9C8J98kxlDiNya5JE16ocyTp2Bc_s-so1LxHTOZbZRBvv_zNuXhNPX8LgstG1X2CiT0YcdRLClwlIhLOM12Bl2xHmdcpcokt9B4prag24iGQwnFRtPjzHei0GbFgtKtjvoWx87t73amjISJmXQI2dyCCRJuKr9MCiIS9obev7dQKrfk3I-vea3ke364a03Isdbj9mGFdxs5gdMjKCsRvh9sfGJ5qmxOg58IqI9jRP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQhiZ_mmywWNyq98GaanTEKNcB9EP_KZ8ZDSK89scOUqK2SfjDpxR9k0bKjjOCFiQLPc4hYfGafWiDZ4V2DiEP7b9lA00t_Oxm6R0EaZY6awtj2UYOOIYPLzXmP172sPHHd3ALwUnH9euAQpNshr14YGTrVk7Lc6QYAggbGK6hAy80GIm0-rf1rH_QDDk_bwcOTFBRZXqtlJiUhlnTTcV2p2WFDdXMJ8-TCP_7OgcYbOEjEZZttoYIJhq58NP23F-zZNxxKOtZ94-YMiuO9sF2xtZ8RYGzV5vc8zlmWuCh6b1JNmgKZnduSMA9tJKzRYKgmi_SWCOhmsHjY0ij5tvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1Ej9-b5oMLZ1ZdszoV05ExmVTKu7BOviXXHuaXF2WXw775037cMZq-nDGNZbsFK1VxS75HrO67l8Bs6_wGFChitIRgaDsrSoiC7eX0MXdmOu5HI-0Q3uX1z8rNvNOPbjtZchqG13oGE00UJjGumzNm4J1VRGh59t5yu6qofZ5ti0DERPmdW9dnB3iNUShRpzvtNcHoBYqwJ38-ZaNFHxgJd5Och2k349dF8l5Hd94tPqTbui_4BGR2qxqmioLl7pLXIkk9CXHZxLXJnJt65Iyos6WYnoeVaB5msz7oL3WBSYFo159P8kuHcdhpJGLfxqnIzISvDNrLJ4CMmqT_CsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTU2fjNtCUR0uYOBLher1fuSqjbzTpQDboJK3qdHTgZnsPsW-YWYxmsYmTU94uDcmszxPgqNuXbBgy-Iwuybw8XqW6npWbl8Q8wuK_o4N0m6JgO7PHerZRuDYk0_vdKZd8V6hueSZVbuObKSoF77RwvDVTYVGDEjtvDc93SfkXWu-zaSEMKN0Oe4uNrtITzmdCE-0AiQO0j-tV2540oW7GGQ6tMQ71bmYdYKZTju-jWVqptPNkCDFjYKYQqK-ItJelKvLpWZYx1Mfr3hAGRKrtjmqbuSAGc-KKJxxBZrkUzC4_4H6KJZ3HKve_rZPdWbDaVIyAGg6UFCC5CQjDyAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=EiOHHUKnSUkVKKQGR84C7FcpbkJRP0f-0IXxQLIS0MFOAvP13FRPzWqFAFK2KvM94Z1nZaI7KiNVtPtPCmx3mTsfLQRjghHrnbj863uXlzoOEPOWzR9ZqTbzZKtx7ymD9hqCy02oMbA0JnxglnMreSv3R2usWEx8Pq2g0JOc9iL-wCZ6vkXdOQLphFC1g7DBkvVsQcMfmmd4DfednXF3x68CBSFZct7y4lpEPX-dSSW1jgvs792tm2ycOCPeMLYk0oyz15C2kO50mSAN6ln5CmL4Fb0WPFGTDfbV30ax7IZlI9kkWcgyt3peqZS1uIFLEMg-vCrmzlFRm_z3FXFOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=EiOHHUKnSUkVKKQGR84C7FcpbkJRP0f-0IXxQLIS0MFOAvP13FRPzWqFAFK2KvM94Z1nZaI7KiNVtPtPCmx3mTsfLQRjghHrnbj863uXlzoOEPOWzR9ZqTbzZKtx7ymD9hqCy02oMbA0JnxglnMreSv3R2usWEx8Pq2g0JOc9iL-wCZ6vkXdOQLphFC1g7DBkvVsQcMfmmd4DfednXF3x68CBSFZct7y4lpEPX-dSSW1jgvs792tm2ycOCPeMLYk0oyz15C2kO50mSAN6ln5CmL4Fb0WPFGTDfbV30ax7IZlI9kkWcgyt3peqZS1uIFLEMg-vCrmzlFRm_z3FXFOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtI_RzUAMRwDOMuePKL9BlISXev9UzmMsRtT0Tm54ABsEfUg9X7eZrKXRXk4kzUdJQ_9Ck0JBl5dblAuGjcGEjzDTjQiBKc2rSR2TN1s5-RPj1pxPyU6txs9Fz3k8FVJ6ed4Sx-sBzUQ4-e4SKIt-9wnFmG0FjhzXVo6In171eC4MYx4FjfCne_GxUCej4fFM9_7jXp6nLV5_uYuADGevJS0OHIj71Fel0hjicG1T__WHNLgWB7ZyCooL3wF99gJTJnYQxxojDlXuqVPiDG-sNazBwjFEvCFmWblpZ2gfQISYcTCGBTFobU7p-yT9XnMFq-MmoXnIJKWjg8Ho_07Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfwRT8Tv5P9VQqfq4HeKkpBE-I7C1QzOK1FP9bMLdoGeioiboVT-EG3DG2sg4SugcyseNpACX2rjLsnpC0vl7cFk0Zy5ZpmRrGv07ozdXPIdvf2fr7h01YagdkLQIV8QfLt-0n5lv1ScpDTEH8HAIoV_SZVzrvAxVQJyZMYW9wcuXT43FQEtT5fQXN1JYFSeNFm_wBwjhv4ehEARO0ybNXPNVB6BuKPb6oxtrwEel159hnQRMyi_zJo9ZMUmN3lGD26FjhvV6VsKRYU40O7nYKty7wMPcczf2pPflo6l6dhxpwSj2rLshLbWaAztmiDgNgOSf6kuGx3pgcbABXaRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnDly9ZxS7kQErNfjlRlGLri4_2I3__GCYxH3CJiDT4jPtPeDJ7MFchbv6vrreUcmBJvJKV_vrWdKZ5LvmeA1k0W8RgOoeLTnz55lPPEYHwMhVjIxOx5AmeSmSYUopWTa9fDfL9iMeGRyBwu0-yVJlMbfP5KLeopM3nAGfaO_jA1NSCpPs5r14oChZ5t7EIzTU7wyYBs_5-qNk5qgWTbHIl3Vg0iagLVDJcaF8SbKryMUMgRSsLngeHm7s6eCdMfdFKnvqjxyQQdNe7ic5ERojox2LNpIhXgzCqEhIsAlLrq7qABEswF5w3tZOkP3LOcFd_3x-GCcoIeTD4ZZtX7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1kAGqzQei7zThvr2XXEl4wpVjLpeTi9MtLBam4ZRwqJ9WBRIR-yN-mVNKPoz2Dlkr2RhIEzGebi32tNyYH1u_TAoDLsX69QyYkSSIhGcqd8Yr-XpEXvIhN5UiZzbvZiXY7e0Q68MMf-_SasY6Zk-81eqZo_rT6zDTy3cqYesKQt8-VgSGTsllR-MzviYsbGU20VALZDG61NoFl6vsOR1AHx4b9FdXjz8ZKnmt5Is-rIEVJAmZMaf_Z-0IDqJVqW_52Ov12mnTi02Oel16x8Lms4F18VNfBH8hPB_fb2Qy30fn032zwNWKRNhFsI__k7PiwR9K_NjFq7gn76jPcHsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=aOHd5y7zQoitE8EtrIdVIGA9chLeuD3gpbEUH0bOUshLsndG8Lq2lpiSzGPztWfzJpTz-9nfsFbFCRoJxjs0UvFGeZk0HH-CwUDxzyUFkVh6TI1HsxNOujHpB4_g4b1xmwoQENig0ius6UlMflyf6-f26GoBud8J6Lq8jLNgnPYFvS2mKfpMzLbQW1gv5ddrenUnMVE9d-tvGFDXC_tS3QWA8dl6lPZ8hlhWQrWiMsHUlukDVw9deuaijmtl1ulRqhorxR2ZL5Lr_AeTif-nHndH2Agpu77yshWdI17BoyPo4_SyKz__OLf98dGeZumvEmeXN9cNNtK-Ehh8Nue8xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=aOHd5y7zQoitE8EtrIdVIGA9chLeuD3gpbEUH0bOUshLsndG8Lq2lpiSzGPztWfzJpTz-9nfsFbFCRoJxjs0UvFGeZk0HH-CwUDxzyUFkVh6TI1HsxNOujHpB4_g4b1xmwoQENig0ius6UlMflyf6-f26GoBud8J6Lq8jLNgnPYFvS2mKfpMzLbQW1gv5ddrenUnMVE9d-tvGFDXC_tS3QWA8dl6lPZ8hlhWQrWiMsHUlukDVw9deuaijmtl1ulRqhorxR2ZL5Lr_AeTif-nHndH2Agpu77yshWdI17BoyPo4_SyKz__OLf98dGeZumvEmeXN9cNNtK-Ehh8Nue8xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsfdSpNp_zUZYIYOYL-SAelKd6j83_8A8Ix0oXOqMVqnqnbXlVwUE__YizUG8QsKIALyswRgfUd1XaVstAtUY9hY-eKLHzqDM8ePO3kzFxhbVfzgzY4X_JvbCus9ITlkKmWphRVpZSp-1VRuZO-zN2L-IBGpWRS05kXO_L-X0ym62kRfgkR2kWN5m62IgMp1B85I5IhOpLlM13FOiZemgB9FwS5mJmG38a1udc78Pkan0UrIVgu0gwdnLfzEBHnH7rRpwpcN_j_0B0eC9aSNBiaXvjymBsctGhMsmOrWCi_8Us1eOkmKlY4X9TNY-OOhoan3uY6WWZvNFa0CF9BUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=n84hakx3z5yVLN1McBzIXlV3tY41zLsdCCVgmuNjUQa6vYkGOtCQItIwSROH99Iyf_waYKsFuIRGOUTEWJOjff5I0-1OMN9wTMFrJEFfH1zWmPWABJGxiSleRtXYZJqZ3V3N3ajCYcwj7qX1L59uJZKiWaow0MtEePMfpWfyVzSP9ToaV79CwiOR4dfvcq5Ow2zXyDyRL72Ln9HVfYM2wcME0GNvCFoT9WiXDTRCAm5Bv5Hg0vBmIb0I1dYz-IWdaSfLtpj64a2lkmtvdq1TQwzfv85O91HfLmjseOJVjbk8rM1uplH_D-zZ5tHi2NdZGj_oSuYU7j_GF3yuE0ecIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=n84hakx3z5yVLN1McBzIXlV3tY41zLsdCCVgmuNjUQa6vYkGOtCQItIwSROH99Iyf_waYKsFuIRGOUTEWJOjff5I0-1OMN9wTMFrJEFfH1zWmPWABJGxiSleRtXYZJqZ3V3N3ajCYcwj7qX1L59uJZKiWaow0MtEePMfpWfyVzSP9ToaV79CwiOR4dfvcq5Ow2zXyDyRL72Ln9HVfYM2wcME0GNvCFoT9WiXDTRCAm5Bv5Hg0vBmIb0I1dYz-IWdaSfLtpj64a2lkmtvdq1TQwzfv85O91HfLmjseOJVjbk8rM1uplH_D-zZ5tHi2NdZGj_oSuYU7j_GF3yuE0ecIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6cpf9IqaHIORW795-7dfXs2X0BB2k4Iw3NGYLQuijVB3IIkegcP6j8hizCpnicROHQ-LroyJ2MTDxsxKY42EpjSVIsFR76g6Fnl94U2ti8C6REeiXEBvRUy2m7Iqyki2s7ERMRbOK_Fquu8N1_l0kCc1VFvT8CX1sI5067zYa8PNIZBj-ZMsBTF-8vr3WDzDpnq1VyHwDBlMYf3G02LHk1pI2akIJn-At5oYTpuA3RQSN2krk60uCdcXAq24Ch13gJ9Q1SgoOE0tFq_Ng-nXsEdO_zl3WxCEq1W0VqvJy0Er1qm8RCEtq4TUO-mOppYOotwPiI86Ub7gZnuPMfi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=PzBh-yWx_PBB0uSH8-p-_u_A0znXcnZcU23xps1UGeQnxckQ6MRweGRVsrbByEibdpebF30XbygcYCeZ_wgDJ_OLiWViB69w8rB9Bhk26Zbnn5KfGcbA0RgzjPtej6OtQlrYVHAbitqafUysOzFRBmqZzisIZNxelkMZBw5Pv1hgz2qXwoGP-xCYRLMkzCSk7ee7G1OIoTUewWoPppmaj8R9gni6FmmJ-IK99-653GmwM8nd7zRVoYMm-dLQx5NFVeBVVjXUyDc81DpRYNvKbSvr6GcxMttRzZNbJOVJGTk91NkuP7igC3uwfAlLm5jhlNnDoR73Jibhz7RZAnm9YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=PzBh-yWx_PBB0uSH8-p-_u_A0znXcnZcU23xps1UGeQnxckQ6MRweGRVsrbByEibdpebF30XbygcYCeZ_wgDJ_OLiWViB69w8rB9Bhk26Zbnn5KfGcbA0RgzjPtej6OtQlrYVHAbitqafUysOzFRBmqZzisIZNxelkMZBw5Pv1hgz2qXwoGP-xCYRLMkzCSk7ee7G1OIoTUewWoPppmaj8R9gni6FmmJ-IK99-653GmwM8nd7zRVoYMm-dLQx5NFVeBVVjXUyDc81DpRYNvKbSvr6GcxMttRzZNbJOVJGTk91NkuP7igC3uwfAlLm5jhlNnDoR73Jibhz7RZAnm9YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=joKdVCbz8vvX1VOIxNzVT7CH0RQALFqoPvajZXjAke6h5aq88VI_neH8eiADbYSybHaEaX4SuQBFvAIFM_5rv6LZpYzQZce11COVCtfivk-lmLgOzLavsfq3QTZbAPpltKuRodfOSYo82RN4tnHDWwz9lVlt3ML-Ny0FT2Db9GR844IT7b8t-GR0GC5lYF-6x_2QG6MnCThc1XCT6xj6cwMTqbW1BBMc2RkQQpwYn8kK4YI-4MUZrMDQmoLtnnHogbCqlVdRSiP4IdB49vIX8v7gBfxzv8VwD6-HK-YKoCVVaggWrZab7jgcpfgJca20uSFqVw9UdgZWbZGr51PG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=joKdVCbz8vvX1VOIxNzVT7CH0RQALFqoPvajZXjAke6h5aq88VI_neH8eiADbYSybHaEaX4SuQBFvAIFM_5rv6LZpYzQZce11COVCtfivk-lmLgOzLavsfq3QTZbAPpltKuRodfOSYo82RN4tnHDWwz9lVlt3ML-Ny0FT2Db9GR844IT7b8t-GR0GC5lYF-6x_2QG6MnCThc1XCT6xj6cwMTqbW1BBMc2RkQQpwYn8kK4YI-4MUZrMDQmoLtnnHogbCqlVdRSiP4IdB49vIX8v7gBfxzv8VwD6-HK-YKoCVVaggWrZab7jgcpfgJca20uSFqVw9UdgZWbZGr51PG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=lCmd3P8oHi4WiDT1tGjBp5P8QgbgZbXg84-bdVeCruOGUtVnui90OpnRCrGM8sAtOQSGkJ7GmVmf7kvjnu9pQELCPtTwO3xWvL_r1wNLf50zY-C1sSVi7r0DSgOMuEU29NnuiCML5mtlxhcpwP24jlH5GfsMhC9dlizpmlfOn3b31C4k5DG3w8kov8ZIJQiaDeytVj6LkrrnLNWZtK77fEpd4oKk6ctAYHC4cgvs8P9fSrqv5zTYnwRYnB_GwK6XlkQKMiWSYQ-qvp7OHA89KMWSrImczQL697wudbkMER6g4L9A3LCWNFQrgGE46IkwdhQYRN1PdaK73a0EwRz0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=lCmd3P8oHi4WiDT1tGjBp5P8QgbgZbXg84-bdVeCruOGUtVnui90OpnRCrGM8sAtOQSGkJ7GmVmf7kvjnu9pQELCPtTwO3xWvL_r1wNLf50zY-C1sSVi7r0DSgOMuEU29NnuiCML5mtlxhcpwP24jlH5GfsMhC9dlizpmlfOn3b31C4k5DG3w8kov8ZIJQiaDeytVj6LkrrnLNWZtK77fEpd4oKk6ctAYHC4cgvs8P9fSrqv5zTYnwRYnB_GwK6XlkQKMiWSYQ-qvp7OHA89KMWSrImczQL697wudbkMER6g4L9A3LCWNFQrgGE46IkwdhQYRN1PdaK73a0EwRz0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lyP8AVSp6YAulXwel9mgZR57fiVFL0p9MaHMEEOYDgUnqvMkdQor6d1QR3_QBDTirxIY72aKrs67l38Oc0SITkaNBqfgIRNhcj8iLjYQFo6KLC6tiZK_d9w-L2sinVWyCkxeNBv6t3qAunOy-FBflRFCFA0KQkFHANc4bAO6qijI2BxtsNYhxFEXaRZLRe2BPXrDR0_rngw0dIwVlNOkdv0kvGKKwvge6rU6aaod29ws1lQzLpFyEXTg5JU6qCX9Fp4HDiW0h8hZIWhH9NZwKAHnaFvjIZr7EKkfwTkd6GUzFyJ-8ktJZXCuRR97sfzXwaUuLUSm3xu05rvrFDkpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KpTdyazUaQUlQpf7SQ87dDfhz1mqyEgNhfDfw82EunIzxWLwOPZLjFlzP_KN7KMwbnDHqZobs8CYbXne65b6t1L5ww28ae9RaeYa0kC0rlGWO77moqrrfALwZLzRUSR5g-ySWEzQ366v73QWkmTtM05Y6UVmLSasaoDKT5NKZ3tpU3vScDGZrZppxcTnAxTrtJ0RMnNAMwQFb-7TvHJRv8j1erY9vfFZ5AXPrXHTxvBcBnBaAojciSv3nSaNRLUXIcgFvgufFRmyuQl6KDSJS8X8BJ6BO5amu-QeSK5J-G_70Lg907KVL0MFA4Pbc9VVpjOL4UFShG-0VWcAwjAbwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=Fpt6wYU-0wdBjYhX0UHc_LSF59B2wFteucnR7ORzmarN7DTUdDdiiZNkHA_PiHn7W3jhcn1i6XVMh6bAeMAJU5Qi_3TKU9nzV9E2UU26Is9y59cn_J1dDShcsuaaqnCDzHbZEeIWEWMxv1vECY3PNF1wuRzVa9tJ1JVIu22sbbhHqnbUS5GgnPPe8mGFDUljqEoacAbuvafc6S2mfbA94Jh9YnxHpI_tZWoWxCXPeHjK4ciKCSxD9iGPdQhOKIurG35hnoiLcKgHPp4eJm4M637bYyXSHENWvNH0OmWgoIXSHAuq5d5FFQvx8MZAfIRKsjtwA2nFGAn3mci1v4gSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=Fpt6wYU-0wdBjYhX0UHc_LSF59B2wFteucnR7ORzmarN7DTUdDdiiZNkHA_PiHn7W3jhcn1i6XVMh6bAeMAJU5Qi_3TKU9nzV9E2UU26Is9y59cn_J1dDShcsuaaqnCDzHbZEeIWEWMxv1vECY3PNF1wuRzVa9tJ1JVIu22sbbhHqnbUS5GgnPPe8mGFDUljqEoacAbuvafc6S2mfbA94Jh9YnxHpI_tZWoWxCXPeHjK4ciKCSxD9iGPdQhOKIurG35hnoiLcKgHPp4eJm4M637bYyXSHENWvNH0OmWgoIXSHAuq5d5FFQvx8MZAfIRKsjtwA2nFGAn3mci1v4gSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=m0SiLK3I5ZYWRZ5a2rcyHP5Mboepsj16cIztdSjJgHIzaZF4o3e3KUMv8Nl1o05ukhlhfhXL7kvt3vE6NkmNr_r77Ag39mt8nj89EYdKvMlOGJeQOKzmY5ujEpznO0YdQ7Zmjd3YkGx6HWNQwg3sV9lAtMcI0t34AgL9Xya_H4z14nICFNTX7E95zT4egjht7YNIM-7fy0JHMBxO_tDKu9UR27ERWZkcvHB6Bm72JfR8EO7Br2yU3NKXBnrgMktIqEBROAacb8fToq0a3-X6Du5U2qFzNMMC45CQF0HL_zTmBRorqbVQUTiXCQAixQ4fc4IwAn-vWpJW9UXu-qcttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=m0SiLK3I5ZYWRZ5a2rcyHP5Mboepsj16cIztdSjJgHIzaZF4o3e3KUMv8Nl1o05ukhlhfhXL7kvt3vE6NkmNr_r77Ag39mt8nj89EYdKvMlOGJeQOKzmY5ujEpznO0YdQ7Zmjd3YkGx6HWNQwg3sV9lAtMcI0t34AgL9Xya_H4z14nICFNTX7E95zT4egjht7YNIM-7fy0JHMBxO_tDKu9UR27ERWZkcvHB6Bm72JfR8EO7Br2yU3NKXBnrgMktIqEBROAacb8fToq0a3-X6Du5U2qFzNMMC45CQF0HL_zTmBRorqbVQUTiXCQAixQ4fc4IwAn-vWpJW9UXu-qcttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_cmj-XV8-LV0B-mVrh4XiJLG_5eK4YHASeQ17bV1yJP95D3bcQ_8B59B0xKeiyEJAa4p888suvqVXnozb0gANG7eWp6VQTKoyYIe_vpF00yTidfY6XRnEMXhudyk-oFgZi7ezLt7m0gaCmx3Ed-48yj541lkNygRCQvFZziH1_NiBdraMK7mp_4flCofTB013qOUA6bsr3j0CGECj3cPcALjBXSuLqeM8RsAITVXIUdfzkIYbkwyQYek-WRB7C9tYm2-eU9aFe4ZX4m2tLNgkYrSoG6JuTWcdZyL9FLGElkpJnPYH60iwNSVMOMbYAK8-VVVIq5H4nGdYhXuWOnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3n0JnxrmgUKxLR7YIk97fyFzg6nJO_HMoYY3KJ58RiksKssbGtizNewMZkFPOKa5-LWTUa8B8Gp-RcrQ2B1sLlKfutu2NKg05Tw2Pe4BVYYFlMXSxyzpr9MyBXVo-VDmwYtJzj3nPjkyx8DeelGGFveOSL9fmcxeN7ZAeL0AifsF60LV-0lGUPCgYrCYq1X_2bU6ioICYwT9sd6G1YHyCO_oUsFqaielidzmPWIth1G9TliaXiRajz8VnvO1hiFd3RUtIYMES7df58nJ4ULMS5QUgRdYS_Paw-mS_kFez4Vybf3IzCE0MhHuinyExxcazp5WajpPk6bmAKO2K0E5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcG-0Iny6gBTNpdu1KrPqTk0n0D1O4ePZ7YOaDUzYz2x5WGZnNBhBm3A0KkNWSJE7XjujQZ201rElAkrCrH8PHav_Cl1O8x9qSpe51WCv2Ovrwcdh5YKlTAhF3ATEXUXt0lxJVEdPOHmcTiORYzU8FKkhzKqjqzHb7eTJzI4MbcwDE4sTCT7ECSAymeQWJZsm4M6w7JCYJcLs3ufqw_s4QRaLym92wbkzKDLFv47R6Cc-N7JnOP9A7LzWXxnmtXrXouEMB6W582ibcy9oy68MLTtabwJkTrJ5Qhj7_0zfKL7JGweHw3FXZ13iWIYLsBv5-M3GpFJamZg-1HC1t9SGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/As7nJDKDgLa_ukij0c9ivsMQu4Jty9jLaINlZk6Guw-ucXjusb6ZlTHFFthh2i0e_Rmk3Lyq1RVGM4CUlIS8iO5yhBf6zd6_pIkJGB3tAbLp57zQGwYvu-1x8hgN5HN5ju6WU1ABe_TDwd_DwjCJGYP5cgs165uEaBxWLoj6kj355ivfeaVijW3ZrQCxYSwhvYqh5-Z1_Pt7RWnyfK5zdOEvwWGUX92I8GUHU79P9kfPBvpqtoFkM0FIB8OyVssABh-ukW-TONnyvYg63OHaiUUK671JL9zShiXFp9e46idob9LqrNs7XxvUVYgG0aKYsy1dkF-_wBJokK_bV_5pkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhNy0q96sfUZH71RLuzDMjVZf__okcsHn8JKB6Iw-PURNgW9JhMm6YkD3utMY2yG5KHWinopEsRdoksMI2uF6nOaNFdZ8Lv0ws475I7dNteDD0L40N9hehYV8s_Y8ZTDHdk8LaqxYnLsUBzeroCh5p0y-bjjB7PI_1eyIhReFAX3sHUXXdQkmHAq8cxHDRrwf507e8Rmmpm-N-txkJNicTfi-o14PyEhP1Bd3qNMxJnERNOXpIBI3GyP-GN77NalT4JeYv4cOizCHQF6UjHWpcJVyH42c7RGVswufs4HN3GjF2kbc4Frjg7ujCyIs1aihJqWoqTS8vxmEX-tzM1EfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxcom8UZhvUaGJXAY2a40nZsg6uExzcS41yM1EDDwCusdc8dUGG41gGK8xftCoIkn8vkcPVZqovjtkN4BKZ87uOibREoorLe4jJRGfFCKBCsjPD8wZbEervqjNJ0MNYVUvUvhfZRxsdQGp845S6YAvWOoNJZKXzv0HNkwtnUATsZiOJ5gOg56Kw7W2JZfTAgQ3OTk7fr65iaYMMnicjCRkl_Hf5Y_6NvJ_ZPTQ-ld5l8qKamsBYVkgZjqdAgOllbQ5zTc5E5atG9fGE6MaHuVdni5tYK1aDclXTOw4Lp9xIBrAzsS_qWZdcElticLqbE0pFdVGGk5c79UAvfvSjW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vPAKCADYoUZhNiUa0_Q2lluo8IbwygRXNlZ-HLqzfzN3zzamZ0YgcK6Rqtmlt-FfbLrLcRaVZGG0qlLW6ubKqM0zzv2TuTXcrpbxMQJhEFWy-UzrV94o9ViRn28BYcHrswkWTSgqmwqq3rdIxKMyIDtwStc039wE6xpKkHyC7J58jbfJbOFSYFYwp1B9P64Nzd6a7XR2-8s_fD1QhCPOu2VFGhWTaDypYSQRm61PGMFG2lk1N5suxVK3KbLx0SXmXJUlKR_3HUWkoCbv1C7jRXYxQrpd2V7aTJbD3Ta7JOZSvFbRGYjWcgHpU2xvaQh82oQ2TVIvdUGyVTAUl7Vn3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=vPAKCADYoUZhNiUa0_Q2lluo8IbwygRXNlZ-HLqzfzN3zzamZ0YgcK6Rqtmlt-FfbLrLcRaVZGG0qlLW6ubKqM0zzv2TuTXcrpbxMQJhEFWy-UzrV94o9ViRn28BYcHrswkWTSgqmwqq3rdIxKMyIDtwStc039wE6xpKkHyC7J58jbfJbOFSYFYwp1B9P64Nzd6a7XR2-8s_fD1QhCPOu2VFGhWTaDypYSQRm61PGMFG2lk1N5suxVK3KbLx0SXmXJUlKR_3HUWkoCbv1C7jRXYxQrpd2V7aTJbD3Ta7JOZSvFbRGYjWcgHpU2xvaQh82oQ2TVIvdUGyVTAUl7Vn3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEweKjruIp_vXKdRczfsdXQUz2ZRE2ZJZ4ZTClc3b0AxKsSCqvARQPO1rUPktrTVEh3Cy1QsLrIBMEN31t0kwygMS-PvkjtHutu3awxTwp9Khgo0r2JXJbT8Wo2qSBoHntZBXl4wm2FwITwW3NjqgM7psMshzThDmNO4XzP_g-Yn4puVdRJ9XIxTAd0V_VrlBwuTaI1Xjtc4Pjk41P7cCsNG52bQfSGBKSwmQFHMEffGN72v5OJx3_6D52yaZzp5iag8O9GRWuIg1mLT2dqgvDqd2CTIJtCho1KqryghUtFpCVYIEfDIdXt3PQ6fgd9pg0h08coV4jY2TTisQik2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHV3JwDlkCFzVNW35X0tb9mtHwuThgzhzX9fKi7nygKFz2ARMYowsN4dtj2wUKkORSH8gICJCKDQa7S9POvWuV54uIdkPEEq5boSS7nS3DxoQrThwlHhk7EeZ1AYKTh0MAaeiHmpkP8Beawdyvz3yoax5PIkVqg-AtG5xDr32DZphZ4pyiQWnIcqEjwW9rcPr7HJaDbXfcIgP3UXByabPToRiGSN3n77Qe5JaO_bAcdlHklrJUpKXYq1mSDY_O7Do7tYaGuyg7m7AFMdiR3d_K_DyRiiOpCs7jkUwf-A5Gh4U9uPuHVYOUWS9Hah4QR6Rwg3NlyLZHd6HmDJsCVsig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqzC2FKE8grC126tswtJ59kEn53DeqoZVe5OviE2kyAi4ydvZ6c2MO9-WxhJfkc5vK7zt_sPWrBuXIOcBRZIZemDWh8aPRuEUrZ0Lfr_BhGQJx1LjG9xk6vNe2CLbfFOLnOspIoJvcEoqE2MRts3IWht64KxGIcg2NNfh91PJ00z7tAdOPRRs12rbUV52o3qhIM_tOUY57AET8qrYKJ1CZuV3BC9IMW0YYau2vhbk7dOHVLR9fEC8kNvaDr-xkwiWrvLslUTg6cZYo168zCW2KtQCHR0kbOKE8AyjFt9VVhUH4ljbcM3cTp19AbiYoJPSCYODde5bk8rp_gptnww0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7p5WO24LetgilTcnzXeVFPxPCMEYOcKP-e3tor1PZQ_cXk8zdQTaD_VxR6RED3P459bSYnQ68w3_hBn5RwF32iYVTSQttc1BmEKLdOsTVlG8UuELz0CIc4VSBYtoSpsoF6l6dt36GqulnxyHdYjePKE7iUUhXhfSalQ0n60T1RaYuJeXnE7b44CxMYJr24lQmwWFeY2putwnx5-ArbluOnHRwpQq9gJRSb4SYKtViW7Dsh1Agly90OcUiarHL_fY787DD8qsOSXbTDo1sDYtOpkbZQx53K5fLTzNndkSt6C33QWyY4IpPclFb-PW8kv1psUWCRnMMl3IHQXrZgbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lMHYetcHN7jkyoMf3JYC_NSH4zgyMHArZ_RcjMOAU1ipcT3_3_4k-HbhSZxObrxDBga3KTXUzLcfGQTnSgLQm8syvyYWnO4J-Bf4eetIbFjkxyq-ryvnoU573Niu_McbBy4Njd45ttu-CDiUrm3Ea-IsBck8a-Q8NsZ3HhhmqUI_PIYPU_rmkGBNGyv2RE8tKNH0HH5NgNn6jL7RB4J9R5xhhhmZf6vAAgxPeaVXTDuByQDYELaR8gSnP37CoMO2a-bkJe_RkY3EZ1ChY5fukCOWSOxzQtIJsQINTBJR9XGQc5V-y8diKwfS9nekqeA8k-iZgsNyRjRGrNdd16AzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
