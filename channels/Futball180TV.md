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
<img src="https://cdn5.telesco.pe/file/KKjYoAEBi2oaAPOpqi-v47KKX2bhj9DZPxeIXfg9JmDtDZMXa27zhNkXTydUp6pD5BU8w-ZpgjnTp-qP5XeG45HujCHjYzFj-gruzH1ZQdA5wXb253iT9gaNRYav4JYK60XBs77x_TsdGRJLu1i3U1ogenpFmK82BZKGa5u2vBy0vznnyFVHtNlaLOs4Plr_ast1HO9lI2svR5JAIAdihfTxc-6LqYts9BCaJEtk3OmcUOKD3xtMdqA0xNST1WcjpWUO4uR0FTx2Oe-dW7g5qPoRc2WwhVGWFowyhD57I26L0pynOAoC1F2Ls-kldoompYvyJYmhbIdFgXmqGmpg4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 419K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 09:45:45</div>
<hr>

<div class="tg-post" id="msg-106198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=Z5G3mhDYczYurnokpTZsZ1LMRRJ8_HjeeQ0Jlpk_M3JddH3NKCDclz5l-wCR5j2swiyZJVs_Qnfn9txPjix_zPovhaBsfmmyZirM_WF4ZOic-Rk2UDF-QkOcrGin7GGiXCSp2BJ3O82rfiwFDCROAZt4NIHuyVcihnCYdqgLdCtMkLxqa9D8CjDZIVaOXKjQs4bUEbRJOXaiRWzZs1YzHNH_rcSN6HCohtZU2uswJ2d2vhIv3Lk-pKJddqG9sHjr0HRSF-NsOVq8Ed5Q2Yp3Em9mGimQEe2JinlKtOMfJ5mo7_81nbuMEeZGFzE1W-Hh0gXHrLigZPkwkqzbpXqFQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=Z5G3mhDYczYurnokpTZsZ1LMRRJ8_HjeeQ0Jlpk_M3JddH3NKCDclz5l-wCR5j2swiyZJVs_Qnfn9txPjix_zPovhaBsfmmyZirM_WF4ZOic-Rk2UDF-QkOcrGin7GGiXCSp2BJ3O82rfiwFDCROAZt4NIHuyVcihnCYdqgLdCtMkLxqa9D8CjDZIVaOXKjQs4bUEbRJOXaiRWzZs1YzHNH_rcSN6HCohtZU2uswJ2d2vhIv3Lk-pKJddqG9sHjr0HRSF-NsOVq8Ed5Q2Yp3Em9mGimQEe2JinlKtOMfJ5mo7_81nbuMEeZGFzE1W-Hh0gXHrLigZPkwkqzbpXqFQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
🇪🇸
تعریف و‌ تمجید جالب تیری‌آنری از رودری خرید جدید بارسلونا و تشبیه‌ش به سرخیو بوسکتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/Futball180TV/106198" target="_blank">📅 09:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=tEsu2SWHEhjsHb8Iu-InNfHZ_AZStwKNmFlnrO3jknRawYLTRfJckqLLrR048BfFoAilz6ADbUaV0V8jKAXuFQordCLKiPS-5YS6sS4b7TIXWPJXz9Ep1i6LYkUfc4XkQX14LlYpvGz0lpL5QF2XyDgqAViAByCDAoJh8XxTcEMgzwYLmzqJP-gF8TTwIhhtdfyAowF5wOVxJ2-VnzLvnAdyd3hEjtyL1Vn9jiMOewxS69HyfkDGeTnMVXo2TihA71ASzPx2EH2T5yCdFQ_wv1Jzx66qtxbFjF8KOX4nLfiT19NQ4hjUcqg0keDWHQjBhkRycxXe0HNX8M4dxG766A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=tEsu2SWHEhjsHb8Iu-InNfHZ_AZStwKNmFlnrO3jknRawYLTRfJckqLLrR048BfFoAilz6ADbUaV0V8jKAXuFQordCLKiPS-5YS6sS4b7TIXWPJXz9Ep1i6LYkUfc4XkQX14LlYpvGz0lpL5QF2XyDgqAViAByCDAoJh8XxTcEMgzwYLmzqJP-gF8TTwIhhtdfyAowF5wOVxJ2-VnzLvnAdyd3hEjtyL1Vn9jiMOewxS69HyfkDGeTnMVXo2TihA71ASzPx2EH2T5yCdFQ_wv1Jzx66qtxbFjF8KOX4nLfiT19NQ4hjUcqg0keDWHQjBhkRycxXe0HNX8M4dxG766A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
اینبار کنایه تاجرنیا به پیمان حدادی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/Futball180TV/106197" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQrBUxuiqV11cmyg45F_ya0yA2XpX86tQMu9-FeGWlny0ELEVE-hTvwiTFVb7ZZzNt-wnIbY32v2MwoZ5somJdKQzgVYLZZ9sCJuWxDpmGnERGfjzrQhuxqgwg5h3g-F4uq--hBMHQZ5vXL2fiy59VAKL4B-BA5NRCJZUtC2xV0mAv0nN0vQIdPlUgepI4x9truzazLS8FhthImbr-2eFPQ9LJA6hM3ws8MO2UocjTWF8BF_eo_TtGaCVcTtYPDpa90FaCWwNEzs2G11_oiZHbV9VmTEjesOJWCIrnK0l6jkPUwY10sVZP09Pz1OXmkoqWwW_7t9z9XLY4os7ElVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
🇪🇺
کمترین تعداد بازی برای به ثمر رساندن 55 گل در لیگ قهرمانان اروپا:
◎
🥇
🥶
ارلینگ هالند — 49 بازی
⚽️
◎
🥈
رود فن نیستلروی — 70 بازی
⚽️
◉
🥉
هری کین — 71 بازی
⚽️
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/106196" target="_blank">📅 08:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/106195" target="_blank">📅 01:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPes7VUvW_BVOsrW9u_6JBtr2OXNPw9k-vwv8GqJgK3M4GJSrcrvF0IZr95AcyPvUgNrKBN9ABsDvedxLie3OobMeJ7Eerz3OlVvNDCUvjPPe6JEldr3B8ZYEp_7UyWf30pjpWMvx39BPU6Yv35MSpFH8RQTvg-t626h4I5Fa-pPnmMvJ3DZPTvocTuaC9AQCZOB41-IQFXIJd_Hn7BAF3E3a7VdhKmxpoBoFXMwu5yugpYAlvN3bLqrj4-NAoGjfAEQWcv_ZaBTCwnnmVTfMvQNUP6wdXzaLecjF645lxfj7xyjJsf60MCXCSD-hMpxSumnAj47caMUMbuQFc8A0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/106194" target="_blank">📅 01:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/106193" target="_blank">📅 01:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvLIep68_ZYKp01TMy_rKNdDhdvcCSjRc5MbAa2byJJXaYrxIw9053JfOyhGIX3MMKPRgvehy7GtsJ-ljIBQH6QONDl2NGfB2JZJILd_Zm_lz8Vla6p7ToEKVdhnNaHN0gn-mzklVh1JclywsfeXGAVIZyc7RuaNlvcgQ22iUGvi8HnYTdYW5iI9mj7ZLxG57D_pcRCTyxtQsZ8uqkYE2r7OojeiXjEGaeTb-JRQtMhijwLueMhsFhTG9gnz9JfKkGGojFwIGjBbnJ4iPIjpH4QTbHB-aGuSCqyxxK8Uip81n8Jf4sRGc1UWYOVf4G0mYWxBvDRGBG2lA0tP1BrT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
مقایسه آمار السد قطر و بارسلونا در لیگ:
🇪🇸
بارسلونا ۴ برد و ۱۷ گل‌زده و ۱۲ امتیاز
🇶🇦
السد ۴ برد و ۱۹ گل‌زده و ۱۲ امتیاز
❌
پ‌ن: دوشنبه هفته‌آینده ساعت ۲۱:۴۵ قراره استقلال ایران از السد قطر میزبانی کنه. ایشالا خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/106192" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu1fZVI-ylBbnFriEhr7Sc2ubQEzqohsKKfUkkT-fQ5qNgk0XmaBYwyJINgXQgPqK6pWwJ5EgqA3g9l4K5eZLtfji78pFA5wdrLKzdIhNZwImBAIQ4fC_lERpJhMDJi_R53eRFL1nB2s_xKNsslc1qvcghWObGwnuwyhDE9tBjFcv0OzTovG9rKmMbZ6Awl3eHEqWxUYl_bVFw92CLlY3Rp-6AZlDSwL1IvtzwMOxK_3EF1GuB8U7OGkmeEqWmcR22wukGBUZIf60_Q1W09epGeT_SvkS-cYHZ0mON2DIQpK7TTNOVzeG-et0AdEMsxKtNkLkTDQUs9wybpzaO2iRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/106191" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mws_J-BzYoBwY4qvfmGEISBO1NSDNA_iqavVe6BrMZHJ49w7ECdVooA9OH6RFzjVusgnKeECoDBeS0zztL23E4Y7lAnId6jKWH3KfMZLKqpr5hDjOHcjZAQapXvfcRoIZesma5sXJFSkQV-Zug_c45HYuYlL7iF9zEUPj0_GItsB2IcaCcyD20GVnMmsUyy5F9gkvPGNIMcuyyvVPJXue_SnvcqWMhcxaB28t6FWIn_hXvrBoRjwPbAiItVlaXymsnRP6XkNAHmlf75CtH-6nnk6_7V5Aiu_1sK8xFnngSZQkbC3t28K-budTXkw031NLFp2bsZmpiCps_jYKv19hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106190" target="_blank">📅 00:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇿
هایلایت بازی منچستر یونایتد 4-0 صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106189" target="_blank">📅 00:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc0UZH3spIKZO1ZjbZO385pFuUUDdk94g_PIebtytNzqpqNqNLODO1mM4UR-DlZQm4AKO0qdiW3pHgOs5B_GwrxuKTv4bLoWKaxs2H28W8RQuSzxojgLJ3O0LX_kan78SY3z2Gz5VtokkOnTQ7iOhRklbNe06xMPFKAL-BYUb_cO7XfB8X1F2k-00761Ww6w--_kVYPk-brdU6dqTiDYOfGo3uBwZLC83Wx_yjxLcw5em3_VTjAc2u1G1XZdSKaYElZBESUJ0iQTIy1Vm3BwIqdK3h7IwMGe16IPO_yZfSafwIFKgeW11UkNXw1SVEDK_Lp1Fn0BhWmcY6UglORCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106188" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3993269f13.mp4?token=ZruDLX2Mz8cm4ox0xujme9AqxVVVij6abPmXSkjRR-CAZiP0JAxCHz_UEIige42IU64jVKhWW8PW7VVH485ecBMAI7nOq1oo3aq3OgSVWQs2EUpi170yQ-cwOtXW6EFBEQrhhmShMltDkr1qXHVKWjNHb1t7NES97Ybh7HGBSuM3j7X6S6XSiBsFm908dakTu8Up396eTxdAhaGZv8lBh8D6CUDOaTfLK2899egqLL6cySScYL_Q4wuhNI33IsyTR1vOmY7pjzj2ESgSuczq617bK86re5kJXCsOSUycGkVH2g5g3bCOsk8rcOxF6UZUFAYknqC7HVtwESUZHAFywyoOB0SU7yN9_DvU_hQmqRSJOOmQI0uS8piBl06gMD1oVfS4Ok-H01YUg3iOD6TdLxkn9DaXEiu8Rx3SiN3sPFwI9mruxHGTIns4e718u5QBUVCfjV99JBTj0B8co36O0_A7E7LUElKJgnH7S22lRCee3u4Gct25nMRJ-2rx_9_sDruD991emD9n8ynDLUWFcvcjiv41ZNBdQXmdCfEnLGATb_NnAQYKV0Yl-vc94NFPlKxhPzcaPAALKmvolyOktUH7bITf4BDTFo_fGTwCrlqYiXk2Cbt5O29dH7JmhPscN6tNSL_tvHg_07zLsuzHCVymoIuor99bFAmUlnV29RA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3993269f13.mp4?token=ZruDLX2Mz8cm4ox0xujme9AqxVVVij6abPmXSkjRR-CAZiP0JAxCHz_UEIige42IU64jVKhWW8PW7VVH485ecBMAI7nOq1oo3aq3OgSVWQs2EUpi170yQ-cwOtXW6EFBEQrhhmShMltDkr1qXHVKWjNHb1t7NES97Ybh7HGBSuM3j7X6S6XSiBsFm908dakTu8Up396eTxdAhaGZv8lBh8D6CUDOaTfLK2899egqLL6cySScYL_Q4wuhNI33IsyTR1vOmY7pjzj2ESgSuczq617bK86re5kJXCsOSUycGkVH2g5g3bCOsk8rcOxF6UZUFAYknqC7HVtwESUZHAFywyoOB0SU7yN9_DvU_hQmqRSJOOmQI0uS8piBl06gMD1oVfS4Ok-H01YUg3iOD6TdLxkn9DaXEiu8Rx3SiN3sPFwI9mruxHGTIns4e718u5QBUVCfjV99JBTj0B8co36O0_A7E7LUElKJgnH7S22lRCee3u4Gct25nMRJ-2rx_9_sDruD991emD9n8ynDLUWFcvcjiv41ZNBdQXmdCfEnLGATb_NnAQYKV0Yl-vc94NFPlKxhPzcaPAALKmvolyOktUH7bITf4BDTFo_fGTwCrlqYiXk2Cbt5O29dH7JmhPscN6tNSL_tvHg_07zLsuzHCVymoIuor99bFAmUlnV29RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106187" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=RhNK2how4B2a32IxGq6NLMCvbZ23BI8yEUGNm3fhYep4dlkcnQ-a0a8A5nZmBKnWPhPPoHeroR9ipEpQ42RieKeFjkt4wOInpC_1wvdmmxl7e8oTXSXY12j69UMQ_bQPKcSEFosd844T44Cl6gNsKPi8-HZIJwLADx2G1vGwH5h3L5bBuw4fnCeaZfuxor07qbUw9Em9OgeRoMxDUkcXIWPWUF6wTZKY8pgL4cpyDw-Mpqyu8jqSa3kvy1GqkoSTk6Xfs4ZmRGiiPVVriLH6ojKJhrfZ07yn8goaNGAfRPLWTF2N0GzR9hyWvI1Rz8raKP8mE-8V4cvyQQuae_cIRyTWoK_VK4yAKgj3JwRkE8rQ2GC62X08HHAwLnS73_wdrxSb2mUqZ17daWEmxS4TOIy5N3YJMZx5ZncXxyqi_yYgkXaDofqryZUGC6soGInUdou_OZA6i6zDRUos7eJGSSXGcaISI4hqlxvrmBZPCXcgnmDHCw09jB0wFKOBpHEOt_kfCQNxR3ov0QdOcU_1GOFkFZq7q21zptFStH5_wU8lo2kiLrrJYVaoyo__L_eZI0fRC3YxNrIRfu7gZXWSBouJzUQpDQBYRe8opITI1z7JQRCRgZyXjPnrdnVYTaH4pbJTr6O4ddWYkVdt8eT14eOLTOYSv5kANOJwn6bGN30" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=RhNK2how4B2a32IxGq6NLMCvbZ23BI8yEUGNm3fhYep4dlkcnQ-a0a8A5nZmBKnWPhPPoHeroR9ipEpQ42RieKeFjkt4wOInpC_1wvdmmxl7e8oTXSXY12j69UMQ_bQPKcSEFosd844T44Cl6gNsKPi8-HZIJwLADx2G1vGwH5h3L5bBuw4fnCeaZfuxor07qbUw9Em9OgeRoMxDUkcXIWPWUF6wTZKY8pgL4cpyDw-Mpqyu8jqSa3kvy1GqkoSTk6Xfs4ZmRGiiPVVriLH6ojKJhrfZ07yn8goaNGAfRPLWTF2N0GzR9hyWvI1Rz8raKP8mE-8V4cvyQQuae_cIRyTWoK_VK4yAKgj3JwRkE8rQ2GC62X08HHAwLnS73_wdrxSb2mUqZ17daWEmxS4TOIy5N3YJMZx5ZncXxyqi_yYgkXaDofqryZUGC6soGInUdou_OZA6i6zDRUos7eJGSSXGcaISI4hqlxvrmBZPCXcgnmDHCw09jB0wFKOBpHEOt_kfCQNxR3ov0QdOcU_1GOFkFZq7q21zptFStH5_wU8lo2kiLrrJYVaoyo__L_eZI0fRC3YxNrIRfu7gZXWSBouJzUQpDQBYRe8opITI1z7JQRCRgZyXjPnrdnVYTaH4pbJTr6O4ddWYkVdt8eT14eOLTOYSv5kANOJwn6bGN30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌سوم بایرن‌مونیخ توسط آلفونسو دیویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106186" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29ed472619.mp4?token=vg_G4cwXduijRwqdElIl_es9zN1ozp8iSiLOZlStQ9WB-BWzjGNJ_28j9BevJP7GMRbPS_uEb85ad9q9Oza73GAK09gB-FGy4SoeXJ5zqDC-j_IvDKG1DLKOP2O5PuPsZeL0Z_muW305jpT6epuGrq0aLy-0RhY7H0A-qscwr4drwXwR51rxKge3QU8jSuxJd-nxIpHV4FsCqamSp9oScgx6lu0SWV7wcEUkDOj4zNt8vLCVkrd5_5gR7WlfVLWytKggtfN-ncaNrs64PB9zkITWeuYgD9ZJzl5dIIJfKVWSyINMFOWz5lnCE_5yZTpf2LYqdJCKoW5oZEdkF-twEEBBWTm4V4RM_pHfs-v309CeeajKfwy9q6OW44q2tzXPZ4aBZc_MMqfJMXr0dA6XZSwb9Q_H9eBonbeszqL89ysHwAKc5jcp3axV5Wirtfei-rouviVI2JaAmkMmnATAmm9URobkPJI1g0hSeyAMw5u8hjWQGMVXD6UfTsEZdgOOYaqpzIF0e9bHMHfH-qZL9yghCW5Hgkz76YJ9wlNb7dtswxjejTZIiMkt-iD4fVYTn3zfENdpoZ-hQexZNDLqFH3PZu3_zASk5Ss6rF-S750l8l91kH9I1Epva0qTTK-TpH_MHVb6lhwTCIh7gwbazyrJxX7fDZOVMTNSza4gz-U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29ed472619.mp4?token=vg_G4cwXduijRwqdElIl_es9zN1ozp8iSiLOZlStQ9WB-BWzjGNJ_28j9BevJP7GMRbPS_uEb85ad9q9Oza73GAK09gB-FGy4SoeXJ5zqDC-j_IvDKG1DLKOP2O5PuPsZeL0Z_muW305jpT6epuGrq0aLy-0RhY7H0A-qscwr4drwXwR51rxKge3QU8jSuxJd-nxIpHV4FsCqamSp9oScgx6lu0SWV7wcEUkDOj4zNt8vLCVkrd5_5gR7WlfVLWytKggtfN-ncaNrs64PB9zkITWeuYgD9ZJzl5dIIJfKVWSyINMFOWz5lnCE_5yZTpf2LYqdJCKoW5oZEdkF-twEEBBWTm4V4RM_pHfs-v309CeeajKfwy9q6OW44q2tzXPZ4aBZc_MMqfJMXr0dA6XZSwb9Q_H9eBonbeszqL89ysHwAKc5jcp3axV5Wirtfei-rouviVI2JaAmkMmnATAmm9URobkPJI1g0hSeyAMw5u8hjWQGMVXD6UfTsEZdgOOYaqpzIF0e9bHMHfH-qZL9yghCW5Hgkz76YJ9wlNb7dtswxjejTZIiMkt-iD4fVYTn3zfENdpoZ-hQexZNDLqFH3PZu3_zASk5Ss6rF-S750l8l91kH9I1Epva0qTTK-TpH_MHVb6lhwTCIh7gwbazyrJxX7fDZOVMTNSza4gz-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل دوم بایرن‌مونیخ توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106185" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=oXdqGRMYSvyRixjBA0KKDAUKlFqWeULQx5k8SuSevFUIUczbivQJ_aRJubemrANyPfGHbQE4eBpKsVrG7kTs-h1nEWS6J4O7cLtxewLYH6eCWpSLc0el9Sapqf3EZd5rnhrbPF6JpEmF6uVWwIdHFmHr4xw3XCADH12WgmtI5Oim6ZsOviIS0lhosatf4-3sMKSZatAlwHJMtP02Z7WMn81yQqr-VSICQtotFAACDFPahqT0KL_r_v-ZGuYWixc6R_bsvB-qgRfJXkX5__v3MdM_qh4PJT9UKwL_Y9h1qJyQ6WBa-eoCAb9Veq9sGt01LYCdt0GBofllg_cCIr2hfQPYgmnOCwydYCGaJz7w-dElNs60MpSZ7BI1ix6k32yYINGJZCYgKSrg24RmBjjBhtB0IBEaea6n9UJAR9BYdRAoJykPBKS8XOOOOKvjWNWyobUVu9CtbaV3Z9LymrsjyhiWTkJaVowDv_O-SNEM0hVEgSOYoWgiARiKB6W8XAfeg-EU8KnxGnhti2cpitdViPPZD5qz_TgrbOXbe_T7ZvTlQy6NoJpX58ANSBMnyIvyFIEcfcYNsLUnr4KM7UwVfeqKuBrTdCqjVJq5srXo5fmJRc7R4q-cXHKw_isdbKYLMWUg4sU00FDLVSww1IVEEDPweyAzR8ORnwPhBG1AmPc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=oXdqGRMYSvyRixjBA0KKDAUKlFqWeULQx5k8SuSevFUIUczbivQJ_aRJubemrANyPfGHbQE4eBpKsVrG7kTs-h1nEWS6J4O7cLtxewLYH6eCWpSLc0el9Sapqf3EZd5rnhrbPF6JpEmF6uVWwIdHFmHr4xw3XCADH12WgmtI5Oim6ZsOviIS0lhosatf4-3sMKSZatAlwHJMtP02Z7WMn81yQqr-VSICQtotFAACDFPahqT0KL_r_v-ZGuYWixc6R_bsvB-qgRfJXkX5__v3MdM_qh4PJT9UKwL_Y9h1qJyQ6WBa-eoCAb9Veq9sGt01LYCdt0GBofllg_cCIr2hfQPYgmnOCwydYCGaJz7w-dElNs60MpSZ7BI1ix6k32yYINGJZCYgKSrg24RmBjjBhtB0IBEaea6n9UJAR9BYdRAoJykPBKS8XOOOOKvjWNWyobUVu9CtbaV3Z9LymrsjyhiWTkJaVowDv_O-SNEM0hVEgSOYoWgiARiKB6W8XAfeg-EU8KnxGnhti2cpitdViPPZD5qz_TgrbOXbe_T7ZvTlQy6NoJpX58ANSBMnyIvyFIEcfcYNsLUnr4KM7UwVfeqKuBrTdCqjVJq5srXo5fmJRc7R4q-cXHKw_isdbKYLMWUg4sU00FDLVSww1IVEEDPweyAzR8ORnwPhBG1AmPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌چهارم منچستریونایتد توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106184" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=W6toq-5MFdnMHI7b8exuNVYgtVPgFWwfL9zw_wd3l3r9YR1g-lijibV2K1J3UE3coXIwxmlhbZrukKIACUDFNfppH2fkOXxXJifzzLVOXnBvhqCuv4Ha385DTKQYf97ldiOt2nCLlmhWPGmMABM6fwQRKuMlJAkzIxD5cB1D31okZH2DY4tXhYcmb_uaTsju4BmWYIAv3KhXFPkegPMcuQxgQHQA-6JzKhvgxSdSn3O9meXOtpnFvDuXyuvMRr5pDH-_3fm5_IUOF8Mr4OjWT2ULQMPktk0mQX7Nz3XCx4wz3Skr7C9txqpo4-KeFHn3v8DfhhpMVcRnSN5kU-6DeVFwFHrOMW_vP-0WQPHCovaReE13lfgaHtonmT33khzrb9NGqTkOUPrR083WaC7xkZ6GuEFVbptWcrVc9rlCev5_Yo36VZXesYQ-RVV1HSZBWF-3DSoTAay6BBydFR8SrtMeaujWkLpng504K1Y2t2vQ5z-Kfit4uSirOnQl-GTx7SqLaasZ1_caAQlUVPvPueFSLoV3c-QOpm5PNHrNfJ6Tx9v5luS6pcxsv2G7Q6tfi2WoFIozC5O50l0Ubq35Rx8GJ0ZtRGfQpfU5D_JP-GHROlxCzXCdD82gPYav5ocCI2aaUO6Y--XuM8bm6RTyMPY4l-ELkqP21sgxg8GN04A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=W6toq-5MFdnMHI7b8exuNVYgtVPgFWwfL9zw_wd3l3r9YR1g-lijibV2K1J3UE3coXIwxmlhbZrukKIACUDFNfppH2fkOXxXJifzzLVOXnBvhqCuv4Ha385DTKQYf97ldiOt2nCLlmhWPGmMABM6fwQRKuMlJAkzIxD5cB1D31okZH2DY4tXhYcmb_uaTsju4BmWYIAv3KhXFPkegPMcuQxgQHQA-6JzKhvgxSdSn3O9meXOtpnFvDuXyuvMRr5pDH-_3fm5_IUOF8Mr4OjWT2ULQMPktk0mQX7Nz3XCx4wz3Skr7C9txqpo4-KeFHn3v8DfhhpMVcRnSN5kU-6DeVFwFHrOMW_vP-0WQPHCovaReE13lfgaHtonmT33khzrb9NGqTkOUPrR083WaC7xkZ6GuEFVbptWcrVc9rlCev5_Yo36VZXesYQ-RVV1HSZBWF-3DSoTAay6BBydFR8SrtMeaujWkLpng504K1Y2t2vQ5z-Kfit4uSirOnQl-GTx7SqLaasZ1_caAQlUVPvPueFSLoV3c-QOpm5PNHrNfJ6Tx9v5luS6pcxsv2G7Q6tfi2WoFIozC5O50l0Ubq35Rx8GJ0ZtRGfQpfU5D_JP-GHROlxCzXCdD82gPYav5ocCI2aaUO6Y--XuM8bm6RTyMPY4l-ELkqP21sgxg8GN04A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌اول بایرن‌مونیخ به بودوگلیمت توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106183" target="_blank">📅 23:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipv0iWaFRpN7lTzy5avSpEpeWlhkhdl94IgB9WPtN7aylVdDcGYiFZglRXhEWfq9G9OX6rKPwHYjxK6A9qOkuch_ubWWQK3u0xjscYWPUN9zJuvRnlgX3BOqn7_2gVuhKzXWwL8_BhwX6u-Jn3WAREqsH65JogtqPPeDOCtH2xmdsBnEG3hS7zh65myZDGCGX-taOoYxM8ffFZqT8kleVgiTV2wgZpdS8u_-95LZF4sBZsf_xxcePIS3dQ2_xVrdZX41dPkNb2zpuGr04C4Rw78UvI21Y0RtMjEvHPrMFouAAQTj6rG3ks0nYJyGtu3Sj0KjtAYFmMCvvFSP0Ms8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔥
🗞
رومانو: فیلیپه کوتینیو با قراردادی آزاد به سانتوس پیوست و هم‌بازی نیمار شد، هیر وی گو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106182" target="_blank">📅 23:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106181" target="_blank">📅 23:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t48G_m-1OYjWlqW2os7rvHlYRUuQC3axdKZWfMRIKbjCo5xjnOuMR_nfzl8cJ9A4cMJ49tyTzbvUVBgPJ-kJNvPE-JKqNfD_0y1HPJoWu-2sdjFtEVQQV_j5GvodRPPj4iuRY_xiyJGqJ-g3rtMas1-6pgfRcJHn2duoasq2Z71-4KSI5bfoUw9TcMTYji3g5GOKMG9SayoXxJZTACJjIJWr8KlHV9CoMoiZVuZFsLouiMc2zhkRzqS6UaIQdtcLMMUuKfJnyAL1YwZorLh1J1-34mRToN49JB8HMZT90jQJOhKUn1Dq60c6YIsnQzApX8tM8Pr1u32SKZxmkO3LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106180" target="_blank">📅 23:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=Zx3DX4d-GsI1jCA8gmvpCxPTPCL7f7IsTzk3U2bN-kgXnAjie4os6xiVudzQXAWvwMRomDb-_CJZIuWGChZ6-Tp6uLkL4iCph4ZPy10MJfHR8sIZB6p_oDpwNo7HrNjALkDrQGg3OmYWwINg9hYR0SC1ozteacsNwq1HK5P94X08wwez1Y72oI8xzlK-mb9JxFsBnVn8o8COzYsOc1WUL1F_Jh2izvgua0JbBDCOHb7oKYzLFyfAAVM_sD-1xxGicc4_W_1Gcbxr7JDvolCv6L0LbgcdKNbmyzvNakk-vyUb1afED_FaeWicPRpCJPbJTq-yRVTGVMVSZezMwSRsIDEUvH3gTJ67lPk_GlM9TWeiqKPVBpAZL8r3vz7L-MDzFCmXDFBVShSPd8_y-smkMq8Xx1W6XV8dBqDbLwGnRqf6qaY4Lc9uGUquf-3DFyAI4Yqyyrk4_fgqCnzbjZuW_70_XTazTlTpJOadQeAArVp9TkBJaq0kDGoNkh1q-Z6nnEaNlnPWfh7ZgPNBk1VK_iZZxsgPf5TLqJjyh584YW36mH3audEtzBVXJRN1dmU1tIGPsF9w49LSpIDKn8Oa8hU7ExnvMcpaZE8g-dS_Z1ZFB43NAfkdzaP5y8PDLgmGzQzPHaNYtA_xd_0QiK2jucRDwgh3c2vSdCNnT0eJPug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=Zx3DX4d-GsI1jCA8gmvpCxPTPCL7f7IsTzk3U2bN-kgXnAjie4os6xiVudzQXAWvwMRomDb-_CJZIuWGChZ6-Tp6uLkL4iCph4ZPy10MJfHR8sIZB6p_oDpwNo7HrNjALkDrQGg3OmYWwINg9hYR0SC1ozteacsNwq1HK5P94X08wwez1Y72oI8xzlK-mb9JxFsBnVn8o8COzYsOc1WUL1F_Jh2izvgua0JbBDCOHb7oKYzLFyfAAVM_sD-1xxGicc4_W_1Gcbxr7JDvolCv6L0LbgcdKNbmyzvNakk-vyUb1afED_FaeWicPRpCJPbJTq-yRVTGVMVSZezMwSRsIDEUvH3gTJ67lPk_GlM9TWeiqKPVBpAZL8r3vz7L-MDzFCmXDFBVShSPd8_y-smkMq8Xx1W6XV8dBqDbLwGnRqf6qaY4Lc9uGUquf-3DFyAI4Yqyyrk4_fgqCnzbjZuW_70_XTazTlTpJOadQeAArVp9TkBJaq0kDGoNkh1q-Z6nnEaNlnPWfh7ZgPNBk1VK_iZZxsgPf5TLqJjyh584YW36mH3audEtzBVXJRN1dmU1tIGPsF9w49LSpIDKn8Oa8hU7ExnvMcpaZE8g-dS_Z1ZFB43NAfkdzaP5y8PDLgmGzQzPHaNYtA_xd_0QiK2jucRDwgh3c2vSdCNnT0eJPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
گل‌سوم منچستریونایتد توسط ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106179" target="_blank">📅 23:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=g8ichIZHLvtDaVyJYQAd-GRgDj-Ljw1rL1LCqCekOHwi__NvYJB0_WH2IQW1rbCQrDX_PsL8YeeAypIycsG8m2SpUOnIyoGRglA5cXQNajitQ1wrCNnlsXApixIqlzwGoUyTJDnG4jLKKnVNY-jK7M-gFzb00OpJMcPVc-NQ4m2L_16EvXlCb6lLx-DSlV88fJKJSWNGUY8NDNfU60Mjdah1Of7V3GNoYX6qboHrCcirPNRkNWUzu5a9pK49YO_WNDgPGD818JUkqxenwXrBvwIBqW6fsKhHNP2f2k73ZkT8vxD0gjMkgWRI5x-M80teQCG3R-I4QGOBJFqleNA-HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=g8ichIZHLvtDaVyJYQAd-GRgDj-Ljw1rL1LCqCekOHwi__NvYJB0_WH2IQW1rbCQrDX_PsL8YeeAypIycsG8m2SpUOnIyoGRglA5cXQNajitQ1wrCNnlsXApixIqlzwGoUyTJDnG4jLKKnVNY-jK7M-gFzb00OpJMcPVc-NQ4m2L_16EvXlCb6lLx-DSlV88fJKJSWNGUY8NDNfU60Mjdah1Of7V3GNoYX6qboHrCcirPNRkNWUzu5a9pK49YO_WNDgPGD818JUkqxenwXrBvwIBqW6fsKhHNP2f2k73ZkT8vxD0gjMkgWRI5x-M80teQCG3R-I4QGOBJFqleNA-HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچستریونایتد توسط برونو فرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106178" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=tnKQ05XzXb6nSkf4i5uaFLqBLBCqAcZx8YXdoxx0bdfjP6Y0k6EOG58NBghQsdwQNTmUhQ5pj4qx8VG2M55qO8JtMAoW0J4lWfJiW9ZuQW4JQM8fW5tAGn7UdRBEyYGrtv1gATTUo7QkchG-9BMSMcEyttxIFzvQ0rjbyBCIVwmN_t65hKy_QsfkgVUxfLZUoD6F2zw3XvHfeIixKs0cd0oTIYZb4A3h7CzqPb1vJ_Cfrmlo7q8Cz0vA6GZ-U-Q-5UROThme152WKbI7guUm59PAMZpvXBzFNPHdFQhrI8A8xyhR7dtv_5hK72oOPkZwIaHM3YRBxuPiMqvpXLMmMKPhS5nsMs7MAQqMQPGIeJ-5eUMs0hsvwwgdv9VhpYHcay_ezXwGNG5yXeBQy0UQ1djMXteweuvoFvCSH2lRnOzWg422QN74OamBITFdOCZ6JXPj6ROKkwwRuyhrsrK2z8-WdR8kBPvEULBiKRyvsSrPlH82qLAYCBDJ_36m231Iu5B6qTAqzEanPT8xQgwFzYml8Cq6cyURh5fjnsYFnyyUBPPcl3QVEZIp-ETWAoz--wLId2IhqtV1V1hnv7tYfQsE0DQGY_iVbBGbczS8xXipOWk_aRLX14WxzEsG5Z44Iq7y87NT7Egt5Hula2FBGdjkcH-W_U0Uw8HPB9a75jU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=tnKQ05XzXb6nSkf4i5uaFLqBLBCqAcZx8YXdoxx0bdfjP6Y0k6EOG58NBghQsdwQNTmUhQ5pj4qx8VG2M55qO8JtMAoW0J4lWfJiW9ZuQW4JQM8fW5tAGn7UdRBEyYGrtv1gATTUo7QkchG-9BMSMcEyttxIFzvQ0rjbyBCIVwmN_t65hKy_QsfkgVUxfLZUoD6F2zw3XvHfeIixKs0cd0oTIYZb4A3h7CzqPb1vJ_Cfrmlo7q8Cz0vA6GZ-U-Q-5UROThme152WKbI7guUm59PAMZpvXBzFNPHdFQhrI8A8xyhR7dtv_5hK72oOPkZwIaHM3YRBxuPiMqvpXLMmMKPhS5nsMs7MAQqMQPGIeJ-5eUMs0hsvwwgdv9VhpYHcay_ezXwGNG5yXeBQy0UQ1djMXteweuvoFvCSH2lRnOzWg422QN74OamBITFdOCZ6JXPj6ROKkwwRuyhrsrK2z8-WdR8kBPvEULBiKRyvsSrPlH82qLAYCBDJ_36m231Iu5B6qTAqzEanPT8xQgwFzYml8Cq6cyURh5fjnsYFnyyUBPPcl3QVEZIp-ETWAoz--wLId2IhqtV1V1hnv7tYfQsE0DQGY_iVbBGbczS8xXipOWk_aRLX14WxzEsG5Z44Iq7y87NT7Egt5Hula2FBGdjkcH-W_U0Uw8HPB9a75jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچستریونایتد به صباح توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106177" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=ELySs8uVOSsTkgd7s7gceFtYWrEkJoYEiyewgILhCblYFa9c24IF-Nqqjs_58LQVq-YzM4OiFWaD-G_nnj-BjJ11e8ANj4wbuuI1i9P5Ka0xWCt0sf6LixU7hrE03CxOc7kgPUZ_cPAd2WHhdeYMRc-hwg9ZpFPAJM-sLmNuCJG8gkw4f10lglTnVmwflK8Cg4hS2ukeAROh41ug7tOETsiz2omolK8wOlyi87Xwc7HaycnLsHE_oig0wZ0mYN6zA4ttSyZoGB7v4-Wpw4EPxM-T1HWCv2XV6n_m3MyRBxWBkmDGSreAuNepiAy9jd8mYCnlQJ3Uc7PzQmxre7yjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=ELySs8uVOSsTkgd7s7gceFtYWrEkJoYEiyewgILhCblYFa9c24IF-Nqqjs_58LQVq-YzM4OiFWaD-G_nnj-BjJ11e8ANj4wbuuI1i9P5Ka0xWCt0sf6LixU7hrE03CxOc7kgPUZ_cPAd2WHhdeYMRc-hwg9ZpFPAJM-sLmNuCJG8gkw4f10lglTnVmwflK8Cg4hS2ukeAROh41ug7tOETsiz2omolK8wOlyi87Xwc7HaycnLsHE_oig0wZ0mYN6zA4ttSyZoGB7v4-Wpw4EPxM-T1HWCv2XV6n_m3MyRBxWBkmDGSreAuNepiAy9jd8mYCnlQJ3Uc7PzQmxre7yjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
بازی استقلال ـ پیکان، داغ ذوبی‌ها در دیدار با پرسپولیس را تازه کرد؛ باشگاه ذوب‌آهن نوشت: دلیل مصونیت تیم پرسپولیس چیست؟
❌
⚠️
باشگاه ذوب آهن: دو صحنه در یک نقطه از محوطه جریمه و در یک ورزشگاه
🟢
یکی امشب، چک شدن صحنه توسط وار و اعلام پنالتی به دلیل بی احتیاطی مدافع. دیگری سه شب پیش، خاموش کردن VAR و چک نشدن صحنه به بهانه پایان بازی و اعلام نشدن پنالتی و دقیقا همان بی احتیاطی مدافع پرسپولیس و ضایع شدن حق ذوب‌آهن برای بار چندم تا هفته ششم لیگ برتر
🟢
⁉️
قضاوت با شما؛ چه کسی پاسخگوی حقوق از دست رفته ذوب‌آهن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106176" target="_blank">📅 23:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106175">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهارات خداداد عزیزی علیه فدراسیون فوتبال: پول ندادند، VAR آفساید را تشخیص نمی‌دهد
🔴
فدراسیون پول شرکتی که VAR را آورده نداده و VAR اصلا آفساید لاینشون کار نمی‌کند و نمی‌توانند سر صحنه های آفساید تشخیص بدهند.
🔴
آقای فدراسیون چرا خط کشی نکردی صحنه رو؟ شما وجود ندارید اگه راست میگید بیایید خط کشی کنید و نشون بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106175" target="_blank">📅 22:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106174">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApotgdY5d6i--zDQWuN92fNSxCVSUdsb9VZB99gR2jiVbTHP3U3f4sQDdrVbX2kaywrqfSXX0i9WAy_kig_fGCKcXTIB2MRUVNx2qSbAFDRe8M1wpLkdeyghkU3Ef5BRmGhHXWWZFf7aeWlWbmphHE34ol8KRvjGcmmd3rqts-F57SH6uXAiGkabdYUAMDYOVYkmJGeDeNqtAPLy3prooegfSjVidzRW7EnacKgG6FHxBKoJmjMN6rYBarTC5uLW3Hq8g-0vGxz5M9j0QYhqclsGhaH_cgv-Vudo5qVSsxBSsHN7-kPXprN44aX7YnN8RuupqPc10KvLVVW2v1g6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
‼️
واکنش خداداد به داوری بازی تراکتور و اس.خوزستان: تبریک به فدراسیون و کمیته داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106174" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106173">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
❌
🇮🇷
🇮🇷
بیزاتی مربی استقلال:  دلیل لغو بازی رقبا را نمی‌دانم؛ شاید چون بازیکنان پرسپولیس قرار است بروند تیم ملی، بازی آن‌ها لغو شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106173" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106172">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588203f560.mp4?token=tp8DOxj-YVVBs7wBJffOzsMBR2Us2-SQyuu6BnntMfwTjz2zGPgLm1vEaentLsDgKD0JDZCclck72H6Hqd1ue-exiZdbkKLrW0dIEuH2lrwpsDlJbadRd2QOCJfg5LIZAyJHznY1iiMGaikDeYWeDXsiB1fbhkhwjGkNc2kudEAI2xxyVZmhvHfol4DWZSMNAcsVE9Gajy9n1268YvffkbdVnI0O3L6jHjiMPShevuL1QCqJvSJFAcSucMqjOuZHGc9pL2F6FZWfqnYWK5kKC2yo4dKy6dvkFgEByxJz4hMf4dxedGNBOPel5dR9lU4LWgXYsf30DQQ-rUKcOE-o5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588203f560.mp4?token=tp8DOxj-YVVBs7wBJffOzsMBR2Us2-SQyuu6BnntMfwTjz2zGPgLm1vEaentLsDgKD0JDZCclck72H6Hqd1ue-exiZdbkKLrW0dIEuH2lrwpsDlJbadRd2QOCJfg5LIZAyJHznY1iiMGaikDeYWeDXsiB1fbhkhwjGkNc2kudEAI2xxyVZmhvHfol4DWZSMNAcsVE9Gajy9n1268YvffkbdVnI0O3L6jHjiMPShevuL1QCqJvSJFAcSucMqjOuZHGc9pL2F6FZWfqnYWK5kKC2yo4dKy6dvkFgEByxJz4hMf4dxedGNBOPel5dR9lU4LWgXYsf30DQQ-rUKcOE-o5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
وضعیت یاسر‌آسانی حین خروج از ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106172" target="_blank">📅 21:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AARk2csjTbS0W5Yfs2XweHb3rvJN0E5YhEU_JGQp8ELmgBZAOZcFPv9mndR_QM1nTX1Bd_4yAeAqCsFDyYkYd8lNMG4vNnwy3wlHmq9SKjFwcMaFzrMe6ygWPuSrkXuijNmiuLZOVoKzSwnhI8SR03sZVYqtis4WxJ4uo3XXBWfONWw4BEWNH3Ifd3C6urmn9AZ65ogjLMYRJvNVjEVeqSySpRAaoTh4MSPIeOy1Z43Ot0LzwBEWMYNccSowH_zaHMBjvaT6_SCVHqah4BviZqmTn0VR-g-5LnniwBQ_Kf5V5tv9-rqfR9QszfESj9WQjjRjYVPdFE0HbHdeBdAa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
❌
🇮🇷
پزشک استقلال در حین خروج از ورزشگاه: یاسر‌آسانی شرایط مطلوبی نداره و حضورش مقابل السد تقریبا منتفی هست هرچند باید تا روز شنبه منتظر بمونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106171" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛ آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106170" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=HPorxKiZ7wlI5SCWVJJCnBCgkKK4k0z3SoWtLW0WuHJ2OYaROXOnTiMlIvfBXcSepirlACuruhh2T_mLNoITZ8oGXVPCH8WVJap64fwpwhyAKqjXandcn0mW97vIka7cQ6E2Yp5vMwmNj3CcXhkfhzMJJNhF0PtdjHIYQKaJ6RfqM4W6OyybUzLRznf4SPeXt0ikqhNnRpKWQBXedCM1YFkUznqg0C2eF1Y-1lf8Ju-LS0ZgYZefYGrTDhhKtB2y_b_2frvDgOeNRZ2627yRX7640RMQ3rJDCR328-1oYf2cCvnirRJzL4_YVgb56XsjGVjPCJqfkNcV0FGOm0Qyjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=HPorxKiZ7wlI5SCWVJJCnBCgkKK4k0z3SoWtLW0WuHJ2OYaROXOnTiMlIvfBXcSepirlACuruhh2T_mLNoITZ8oGXVPCH8WVJap64fwpwhyAKqjXandcn0mW97vIka7cQ6E2Yp5vMwmNj3CcXhkfhzMJJNhF0PtdjHIYQKaJ6RfqM4W6OyybUzLRznf4SPeXt0ikqhNnRpKWQBXedCM1YFkUznqg0C2eF1Y-1lf8Ju-LS0ZgYZefYGrTDhhKtB2y_b_2frvDgOeNRZ2627yRX7640RMQ3rJDCR328-1oYf2cCvnirRJzL4_YVgb56XsjGVjPCJqfkNcV0FGOm0Qyjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
⭕️
🇮🇷
سعید سحرخیزان نیز لنگ لنگان استادیوم شهدای شهر قدس را ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106169" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=czw3abvGvGUzATOqrwQeQHAj1AUHViIeilqna3R3pSUx3xreE81PG2kwT2P3QezBcm73qjmQSxr2uF3tSeZpv-7mMTW0KBBoOGrw6B-xPNkaw-OnDUTyywZe98DHP3QVVPdgF4lTqq-UfJIM7uKdj3CZSMknyggvzEFaP1lN8zU90UT-QSMgGw5InRy83TA5pR5Hh0zk-MfY3QZa04YxiZfPHnUlZsKa9S7RODkaFGE2EAFqzYVq9xm6aqUjTrD5OmFBV7Bkm1eeOMaQTPUkxBWgT1Z7rzdYHzjWrCUbQCplfUi5sOAxy-dUC9pJDoz69087kPRZy1b2-PtpyOVksnytdlV8VuHBOSZ-XYVS-6i40DgZlnXWe3NMkIM0rZx4NMXGwsqqJO62kCCzMmfXyrIZWNAbJI-6fVqA8WVFPDTI3QM4n0JvkkQJIoMm8-YfUlrIzTe4gTpz06YV8TMzMUq0Npb12KgrtXtTN1ZvN-qPXB8uYhGibePgJBfED3KEpsTqT72gd0UyYr4ER5k-8JZWQqYy3Xd0uV1252mVjtYYvUgJpye5932IVlCf3WyDF2cwrlhKt5c0JnpeAgRYriuQGdOOVcu-EQPtSMOm4KhCWf1KK-dDnH_o2npBotSQ0Vg3eRnf5hfPlk1suaZP1V9anW1xuBMbKRHtGBzk3YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=czw3abvGvGUzATOqrwQeQHAj1AUHViIeilqna3R3pSUx3xreE81PG2kwT2P3QezBcm73qjmQSxr2uF3tSeZpv-7mMTW0KBBoOGrw6B-xPNkaw-OnDUTyywZe98DHP3QVVPdgF4lTqq-UfJIM7uKdj3CZSMknyggvzEFaP1lN8zU90UT-QSMgGw5InRy83TA5pR5Hh0zk-MfY3QZa04YxiZfPHnUlZsKa9S7RODkaFGE2EAFqzYVq9xm6aqUjTrD5OmFBV7Bkm1eeOMaQTPUkxBWgT1Z7rzdYHzjWrCUbQCplfUi5sOAxy-dUC9pJDoz69087kPRZy1b2-PtpyOVksnytdlV8VuHBOSZ-XYVS-6i40DgZlnXWe3NMkIM0rZx4NMXGwsqqJO62kCCzMmfXyrIZWNAbJI-6fVqA8WVFPDTI3QM4n0JvkkQJIoMm8-YfUlrIzTe4gTpz06YV8TMzMUq0Npb12KgrtXtTN1ZvN-qPXB8uYhGibePgJBfED3KEpsTqT72gd0UyYr4ER5k-8JZWQqYy3Xd0uV1252mVjtYYvUgJpye5932IVlCf3WyDF2cwrlhKt5c0JnpeAgRYriuQGdOOVcu-EQPtSMOm4KhCWf1KK-dDnH_o2npBotSQ0Vg3eRnf5hfPlk1suaZP1V9anW1xuBMbKRHtGBzk3YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ساکت الهامی، سرمربی پیکان: این برد را به استقلال تبریک می‌گویم؛ ان‌شاءالله در آسیا موفق باشند/ در نیمه اول تیم برتر میدان ما بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106168" target="_blank">📅 21:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=bQAGHLegD1uZaIzSItkhFI6ohukBQmFGgol7FO3J23eh_IfkFVOI6nrOoYMMKS8ORuvzPVovLe8MTsoXbQ7nRkFPHYNggFsVnWkisGL7idIS9N3k39nUg8yVSsKNShxAFQd8vglKH-8uVp19SjftpBUiwWPt1WmW3Y_Q5xvJ8LG4U_8wFdPRfYxdx1rLHJDY5Ct5P_pI_rhkVegS_UQbBMwuZ-aaeo8BbQEV20R7zKHZop6jZSctTge_t3DUvnazF1xaS298BjUc4TcqITc7F2g0hVfQz1OVrUys91mdF8oPdoLhdMxJDDv1pd25O9s4HIIQCVuqmfk7ZEKJGtYgyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=bQAGHLegD1uZaIzSItkhFI6ohukBQmFGgol7FO3J23eh_IfkFVOI6nrOoYMMKS8ORuvzPVovLe8MTsoXbQ7nRkFPHYNggFsVnWkisGL7idIS9N3k39nUg8yVSsKNShxAFQd8vglKH-8uVp19SjftpBUiwWPt1WmW3Y_Q5xvJ8LG4U_8wFdPRfYxdx1rLHJDY5Ct5P_pI_rhkVegS_UQbBMwuZ-aaeo8BbQEV20R7zKHZop6jZSctTge_t3DUvnazF1xaS298BjUc4TcqITc7F2g0hVfQz1OVrUys91mdF8oPdoLhdMxJDDv1pd25O9s4HIIQCVuqmfk7ZEKJGtYgyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هوادار تیم‌ فوتبال استقلال: تا قبل از ورود ماشاریپوف چیزی از تیم ندیدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106167" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106166">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c788208205.mp4?token=mB21BuYmuqgz7gCggwNzEFSV6NwSIF1pn5QCsaQ7Bdot5Nh_x6kzYiDeOhmzwa9Yu7o-Xxfj0zemaZ0TLUVTCknsC15PI-bWQsKE9REyFpwogsc3VPhCddAMBxV_oZlbUN8rVtDceW1cJep3es9YmZ2edyGdOErwpIdcQwTxijZ6x_HE9ZkFjG-ZzyUG-q86gigfVq4gyEqaCQB4M2krMKe3D-ESjeMPb7OSl4b8yZOSzwDXDkA_ySFSq3NlQfcoiMXv-_bIh9trMZv8-21IWtR8pNNPiwrJ7DIemwS3iTzZQQcfQdnK51_ACxuWuLg944cZwTubR9su3WUF4mB-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c788208205.mp4?token=mB21BuYmuqgz7gCggwNzEFSV6NwSIF1pn5QCsaQ7Bdot5Nh_x6kzYiDeOhmzwa9Yu7o-Xxfj0zemaZ0TLUVTCknsC15PI-bWQsKE9REyFpwogsc3VPhCddAMBxV_oZlbUN8rVtDceW1cJep3es9YmZ2edyGdOErwpIdcQwTxijZ6x_HE9ZkFjG-ZzyUG-q86gigfVq4gyEqaCQB4M2krMKe3D-ESjeMPb7OSl4b8yZOSzwDXDkA_ySFSq3NlQfcoiMXv-_bIh9trMZv8-21IWtR8pNNPiwrJ7DIemwS3iTzZQQcfQdnK51_ACxuWuLg944cZwTubR9su3WUF4mB-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
هوادار استقلال: به زور بردیم؛ آقا سهراب دست از لجبازی بردار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106166" target="_blank">📅 21:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106165">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
صالح‌حردانی مدافع استقلال: از آقای سهراب بختیاری‌زاده عزیز عذرخواهی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106165" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106164">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=OIHIUIU8ZxCQWzH9kAqKf15wgajpgAYG9WQ1dAfAXjd7Peb8ECYdVAOx1YD8Sy2sEZeWEx4WGSf3OgEQ8L-6S9VMCYZ0UjpdAQw-tRUtRsZyFvpzbEzPB8H04N4p29axulBchh-6ffEBfYP1TjB-CVfgSF1r7AvbsG24_eOXoSBmh3EJx3NqMmMPUjJWOBN32fXzaRGz0nKaJHacWlhlOaqAZCJYFzb3O0lIUpH41c5GMpJxthHD_2RoDEDlWaZgvOGrAsOpk60u5iYyTO7FQ-FLBq-HueUXsZ9z8dVD8IfTeGpP1-JgOzQZoLx9FfV17cIHOXLwWtIE5W-pvbTgbgy653m329KfMJbt2LZQcmL-Baanfmcjmm82TUDKSw9MNOVrDiFNDHLnHmk5o-FVmXvJXp-xobVQZwr64Bv2UYUHqOWlH9ylQfzIBf1wFCOzw-DE3rQjFCEO8VFjrzvRxPyXZA2xlicmcTKEpNhlRHNNRGgCLoauVIZg8ruWr5EokmWv5WZE_wfZhBivGW0SM-rUYG1oexWaUmEJ60xpblp4ErOsJ-J6jc7-M6V3wkt081mPp0cjyB0-2DmVSHxM09yVAzFsZYx-umJoP3XbXa-6dfYKbgIqmrUCzr0f3ll5zktWSGKL1ZaI5j6ggT-8kwrTrERkTA1KJo2LrWpDCpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=OIHIUIU8ZxCQWzH9kAqKf15wgajpgAYG9WQ1dAfAXjd7Peb8ECYdVAOx1YD8Sy2sEZeWEx4WGSf3OgEQ8L-6S9VMCYZ0UjpdAQw-tRUtRsZyFvpzbEzPB8H04N4p29axulBchh-6ffEBfYP1TjB-CVfgSF1r7AvbsG24_eOXoSBmh3EJx3NqMmMPUjJWOBN32fXzaRGz0nKaJHacWlhlOaqAZCJYFzb3O0lIUpH41c5GMpJxthHD_2RoDEDlWaZgvOGrAsOpk60u5iYyTO7FQ-FLBq-HueUXsZ9z8dVD8IfTeGpP1-JgOzQZoLx9FfV17cIHOXLwWtIE5W-pvbTgbgy653m329KfMJbt2LZQcmL-Baanfmcjmm82TUDKSw9MNOVrDiFNDHLnHmk5o-FVmXvJXp-xobVQZwr64Bv2UYUHqOWlH9ylQfzIBf1wFCOzw-DE3rQjFCEO8VFjrzvRxPyXZA2xlicmcTKEpNhlRHNNRGgCLoauVIZg8ruWr5EokmWv5WZE_wfZhBivGW0SM-rUYG1oexWaUmEJ60xpblp4ErOsJ-J6jc7-M6V3wkt081mPp0cjyB0-2DmVSHxM09yVAzFsZYx-umJoP3XbXa-6dfYKbgIqmrUCzr0f3ll5zktWSGKL1ZaI5j6ggT-8kwrTrERkTA1KJo2LrWpDCpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تاجرنیا: امیدوار به حل مشکل صالح هستیم. جام قهرمانی استقلال؟ خبر موثقی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106164" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106163">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBYIkNndX7szd6jqe6i7iUkAe_deXCxeTD8LzaBj1qPIZ52jDCuvc17RKSjkF5VrhC-H9lNe670qSaXX66afrCi0WySF7jpwRTU8Q2RGH1bxSoPt3RSoBRpszXquVEWpqr6I2x6RgeAXs-UxjYRv-XPK_F92VJxK8WbB0WWLSouxO4fdvsvO11fvSJdJANJKlKN2Zu_SB_7LDrHcnwEyUav_m4DLbRp-vgC6W0eeWc1xcUpRE5qlz3stoRLXAW8hPS0_aNznawFc-MSnPN2vUElkgyabzuqQS6INJ9_cp6bQ2RUKTUxrqCqXmjQVXTtheTQwFNSHexTdrsZEvXySWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106163" target="_blank">📅 21:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106162">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=ZIKp1VdRtaBZ8UQLxl3Fw4oVYp1kCXu5EX7D4r5Aq14BLJDXYSV9uT_KinuxJhjRcToA7GHZ_plZ-jeKMYCAJlPGSi0R5VdptAAnEVdkGF82h4jwOHJ23UU4kGbcJcNx2QkBe6DI-yYNFNpawg5sIyV1RcrUWVrGqskevxoktkC2w0k2N-coXmGOYXpy8xFpELnwCnhCoLp3ePPeWa2iqQ4rTF6NQtg7wp00iJFeyydszqavvatK-Rx9jPi7m1Sc4jk_289rYO8qzgErOfWhlm37fdEKPvyW1nbmdcNFomExbiJYt90homY1Gib2e_A_6c3kVh_nUFJYi1H5jtVvkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=ZIKp1VdRtaBZ8UQLxl3Fw4oVYp1kCXu5EX7D4r5Aq14BLJDXYSV9uT_KinuxJhjRcToA7GHZ_plZ-jeKMYCAJlPGSi0R5VdptAAnEVdkGF82h4jwOHJ23UU4kGbcJcNx2QkBe6DI-yYNFNpawg5sIyV1RcrUWVrGqskevxoktkC2w0k2N-coXmGOYXpy8xFpELnwCnhCoLp3ePPeWa2iqQ4rTF6NQtg7wp00iJFeyydszqavvatK-Rx9jPi7m1Sc4jk_289rYO8qzgErOfWhlm37fdEKPvyW1nbmdcNFomExbiJYt90homY1Gib2e_A_6c3kVh_nUFJYi1H5jtVvkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛
آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106162" target="_blank">📅 20:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106161">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
🇮🇷
خلاصه بازی استقلال یک پیکان صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106161" target="_blank">📅 20:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106160">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btO0XsFlcjsCihj8gG4U9tuvVLPs-j0qYe26eoIKWQKjRzPeWvC7bxDhROp5QOMqUQhbbe8d8GG_hXxxGt6L4PdCq1OC9VkFX5pCfDjsAJvsLsdCx5x-ki9aRVKCVtUQ2SvVhfSNKsdQoOyLv5ABmupy12RV3lXeW0zY80hwJ8KZpG4-X2bph3DuX0TzVRJpmQKeMyZhfDdXV1pvw8AX2nEP_GgCi9MEgeIJeqSBG4mBEdr-vyfKhuJePQ_W8Pkk37leBl1uSiY99XT_gxbAphSGrqUi_cSBTmnYo_LsfoNzQJRg1CUasbr2j-oYszQgoqO7aNqG8wsyR_9L7Sj6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106160" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=GrnVkUS3T0QZyioOFSqKjIdBCeASZRn7WOSoZ_K3admpRQAaLnnzoYk4Do818LP4RcYFsczaA19usf9nbO9K2RxmG2wuwbAItaDbjkN9s5GUZBB827Z5Mx-o_H_Wk4foQeF3D7o2SALJHkwfdNa91fKQ9nx1RMBGXmJanffs4BNfwnQ8urDtB1M9jlh067VP0tej7Cu3AgcITBFV1oLJmvgrs0quY3nsPDjc6b3A2qShG1jkPl2rwGu_QXFV-N6jSWz2R5GcFAd4DmBTkPzvZpTsnoxtAmuTUYkhxhpHT78y6GIB9PaBnzRWLw8ztKF7ux44MP9MpZ0QFjABLGrAtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=GrnVkUS3T0QZyioOFSqKjIdBCeASZRn7WOSoZ_K3admpRQAaLnnzoYk4Do818LP4RcYFsczaA19usf9nbO9K2RxmG2wuwbAItaDbjkN9s5GUZBB827Z5Mx-o_H_Wk4foQeF3D7o2SALJHkwfdNa91fKQ9nx1RMBGXmJanffs4BNfwnQ8urDtB1M9jlh067VP0tej7Cu3AgcITBFV1oLJmvgrs0quY3nsPDjc6b3A2qShG1jkPl2rwGu_QXFV-N6jSWz2R5GcFAd4DmBTkPzvZpTsnoxtAmuTUYkhxhpHT78y6GIB9PaBnzRWLw8ztKF7ux44MP9MpZ0QFjABLGrAtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزادی چه توپایی گل نمیزنه و ۱۰۰ میلیارد پول میگیره از استقلال
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106159" target="_blank">📅 20:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=g7IHZYJIfl3jLkOpOhld2zc3PIcOyt6e8lDTQ53YmdQL2RvwlsXagEc1SqXWqTzqghvoFWhyTzcezyF15Pbs5k006ft-ALWlg4RwL5irVw04aTOWrhSr6shfDANY6umqkhat7unHy_3EvVdeJXpbab7t8C6mAcaIW-T75bmPec5Ea5pnKeJHRGXK0xB2uhsr7Vpq-nS5-Q3hMy_dQjZAHV7WfjintbxLuHhrxgfBhej2AmD4ld00HPBm-fFAfGK6mB6tbg7VL43nRM6nkx3J3RxRjWcuDb-IiiCugSW5-adB_FUB5x2ktnzbySDRrSGK2eTQIKvvajDSoWZNr0cjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=g7IHZYJIfl3jLkOpOhld2zc3PIcOyt6e8lDTQ53YmdQL2RvwlsXagEc1SqXWqTzqghvoFWhyTzcezyF15Pbs5k006ft-ALWlg4RwL5irVw04aTOWrhSr6shfDANY6umqkhat7unHy_3EvVdeJXpbab7t8C6mAcaIW-T75bmPec5Ea5pnKeJHRGXK0xB2uhsr7Vpq-nS5-Q3hMy_dQjZAHV7WfjintbxLuHhrxgfBhej2AmD4ld00HPBm-fFAfGK6mB6tbg7VL43nRM6nkx3J3RxRjWcuDb-IiiCugSW5-adB_FUB5x2ktnzbySDRrSGK2eTQIKvvajDSoWZNr0cjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل اول استقلال به پیکان توسط آسانی(76)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106158" target="_blank">📅 20:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
✅
گل اول استقلال توسط یاسر‌آسانی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106157" target="_blank">📅 20:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=tZE14MQS7Pu4bOJt61FCI1ZzJePOHo5qENUtNY6vYrQm0reWz_Dp95LgIR3XG7NPA7OHk9ua2imTZH7TThE_r2ZpgoRx_FJB_ZWl_cu6TVljKrC3id2wg5SuCormY8ML4HYTOQGfEysjiH8Kzi9E00d6JaGveDuiVeZoAU4zc-e21AfXA74DxqiMDg5b8osNRGLiB8N8H6aJXb6SfD4PU7d8pKaqvs8AaDjpqHhIf4n1uyzB7Strc8KxRIFsa9_kspMJqhdmex8cIggXMTpOMksqUq_KqT2sGm8CTpzgq7v0V2PjGJdLCTZg5qChVY9l7dTeXbzhoyKd1aLOnt1yjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=tZE14MQS7Pu4bOJt61FCI1ZzJePOHo5qENUtNY6vYrQm0reWz_Dp95LgIR3XG7NPA7OHk9ua2imTZH7TThE_r2ZpgoRx_FJB_ZWl_cu6TVljKrC3id2wg5SuCormY8ML4HYTOQGfEysjiH8Kzi9E00d6JaGveDuiVeZoAU4zc-e21AfXA74DxqiMDg5b8osNRGLiB8N8H6aJXb6SfD4PU7d8pKaqvs8AaDjpqHhIf4n1uyzB7Strc8KxRIFsa9_kspMJqhdmex8cIggXMTpOMksqUq_KqT2sGm8CTpzgq7v0V2PjGJdLCTZg5qChVY9l7dTeXbzhoyKd1aLOnt1yjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇷
لحظه اعلام پنالتی به سود تیم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106156" target="_blank">📅 20:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106155" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106154" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106153" target="_blank">📅 20:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNnUdTHoySQphvd3lLey8jqlsSaMCsFYiu0Mp95XNb9s5IlCwBGchgmVkaa3NSRZk2WQ2k6DdlgAy2XAZwbZyWS1-nD7H-1Y95zNvKorS2y1l1Z2AJODaioiJCiOwaw-9CedLaaKePH9e-ZWg21GNBodjm7L1cEtjQlcSQNea5KsZi_r7y-KrSPu8EK-hLoLKGFpz34sF4nNzY3OHATxYXvypzdzJRxDQJzaPWpjOnMsEoiamamaIo6kD-jL7McCBFK3iXL2eamcT2kkmCjhQ5LPh6uzefOnTB2Cb9SLsgsEU3RMSTzeFpaEHTInBkaMVzKhVfKl4S6k5bDbKOu-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
تیفو فوق‌العاده هواداران فنرباغچه مقابل رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106152" target="_blank">📅 20:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac6a80c90.mp4?token=NcJAgT2qqJBU7GNEpv8qhpctruadf1FAcCVLiGPWyebwIkkP_vlLMWHB3vbJ8ji0QRA0iEhOErnfzcEqtEUDNFya2SiLNHJvyS9AsTQIkh0K90rrUREOAeTmrBsKKtW4Sjvysxmr0is6UZglrhTUES01QSrPmqokW465Wiwh-WH5wER-hyN6Aa6lh-LoV6g-fYoJSKIFfqSyOCXHWNPkz6flqLtVLufmzUWl7vA6bQSZgbILmKkgXiBiWpdk7hr1iYbwgAv8NU6ZoWykwb0qJG9Z568Rr8cbCrZ3YoYB4InqBHDPbF74eE9HTcKjr7taokzNciqZslqNcSRTb53P-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac6a80c90.mp4?token=NcJAgT2qqJBU7GNEpv8qhpctruadf1FAcCVLiGPWyebwIkkP_vlLMWHB3vbJ8ji0QRA0iEhOErnfzcEqtEUDNFya2SiLNHJvyS9AsTQIkh0K90rrUREOAeTmrBsKKtW4Sjvysxmr0is6UZglrhTUES01QSrPmqokW465Wiwh-WH5wER-hyN6Aa6lh-LoV6g-fYoJSKIFfqSyOCXHWNPkz6flqLtVLufmzUWl7vA6bQSZgbILmKkgXiBiWpdk7hr1iYbwgAv8NU6ZoWykwb0qJG9Z568Rr8cbCrZ3YoYB4InqBHDPbF74eE9HTcKjr7taokzNciqZslqNcSRTb53P-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
🔥
سوپرگل دیدنی العین به الوصل توسط عبدالکریم ترائوره با گزارش قائم خلیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106151" target="_blank">📅 20:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226e1ece2c.mp4?token=GemCkvYidKVVGEEPbEW6G1iemB-YeLIeu93jjLBJwhMfAom92cFOVjCove_xS-UFZnd-fFyjapUZ9w0VBdW8SjEK4KK5dI_VWJscA-xXqb6P8_JNv8o7EtcKFyJmYVCiay8hBXYmOjD1QW80Yx666R__pNrgKTaDMNbkd3uOf5vB-6dr73_N9kiXap3_ESx9YqjazD6JMhlLQ9_oifYoT5VQd8AmUWnqAikbEbPkxlv3nWMtCBA6bRr7sSObiKWZnVEFQqSys0R-RsuxjmAxHOymwezQBS3GN9rAAftZo_bZkRk-tv_olCTCiZIBZPuNhO2tWViZb69I_A8b6fjPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226e1ece2c.mp4?token=GemCkvYidKVVGEEPbEW6G1iemB-YeLIeu93jjLBJwhMfAom92cFOVjCove_xS-UFZnd-fFyjapUZ9w0VBdW8SjEK4KK5dI_VWJscA-xXqb6P8_JNv8o7EtcKFyJmYVCiay8hBXYmOjD1QW80Yx666R__pNrgKTaDMNbkd3uOf5vB-6dr73_N9kiXap3_ESx9YqjazD6JMhlLQ9_oifYoT5VQd8AmUWnqAikbEbPkxlv3nWMtCBA6bRr7sSObiKWZnVEFQqSys0R-RsuxjmAxHOymwezQBS3GN9rAAftZo_bZkRk-tv_olCTCiZIBZPuNhO2tWViZb69I_A8b6fjPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول استقلال خوزستان به تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106150" target="_blank">📅 20:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcQkqzFAm7_QebYs9U6gFAHBNvCJjL8pjtrGMtwZvCxb1mGpZ5Ey_lp3PcGNTA-SZ40p5J8qXzEufd2z4PGCCWp-_M6ClWOVhskAfspa-qJ9inlg1lwjlR-VF6Z5_38dXQkB4V-gnXnmsb5gY5Odo-KQMAmCtscBAozwPORgatBI_qH0nj3p1Yy39Lc3RXE74woeOv9MO5mY1nF7K4Z6xnLTqU-3PGk-3lTAII5FiEhmdxGqrPXxzhAZ0dEDXJtmFHtPt8qs_k1km9WTP4Gb8YG9jwepFkzDALt36_3VVBxpSSo5-q3SM8DMMhxUBkZIQkwBqcZA8Il1hqnVMMpfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
‼️
سقف دستمزد پرداختی تیم‌های لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106149" target="_blank">📅 20:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce42c1eb19.mp4?token=Z7FAT5dSIUNwIWHdHjzLnkmYgLjQWSb291LiMG3APm556Mq41Kt0HPS3kn8IHPIc66P3d6UbBhH4Po1t_luY-oyu0VOcYlOkNOmSiBnVmlPx8P-IdjRDSHeNdQBrbUet746uGeZFhEdY9Rg4xOUc2jIJDxyxzzwO20rsK2omwPPJ8gQp_Nbyh4gZXUMbWyGA7KfShOzHfTNJi_9QijGncdw4nKbm2-pHF43gsarNSxqGuilqfw0PQh2sFjUxclb7KUv1me0JaZObBNtC4_yPO4SI29sJgK3flYP6LGdmECbLggKHKH2l9WfuvtsO87ZRBDjjLZOOYyP4D1x8eqBF0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce42c1eb19.mp4?token=Z7FAT5dSIUNwIWHdHjzLnkmYgLjQWSb291LiMG3APm556Mq41Kt0HPS3kn8IHPIc66P3d6UbBhH4Po1t_luY-oyu0VOcYlOkNOmSiBnVmlPx8P-IdjRDSHeNdQBrbUet746uGeZFhEdY9Rg4xOUc2jIJDxyxzzwO20rsK2omwPPJ8gQp_Nbyh4gZXUMbWyGA7KfShOzHfTNJi_9QijGncdw4nKbm2-pHF43gsarNSxqGuilqfw0PQh2sFjUxclb7KUv1me0JaZObBNtC4_yPO4SI29sJgK3flYP6LGdmECbLggKHKH2l9WfuvtsO87ZRBDjjLZOOYyP4D1x8eqBF0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تشویق شدید صالح‌حردانی پس از عملکرد فوق ضعیف استقلال در نیمه‌اول مقابل پیکان
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106148" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494b673a17.mp4?token=NczinAd5Kz90cele1fXv_THpkGHToR2iKl18o8iYRW8x0W6nKtZGupwc5-VF1D_nFyXyk1As0FMHv8LAk-8uMv0bDNf4HH4XQbPX15qEyWPua0810sMNxnlraGgiPAw-TWuo58XWctVbLGMoYxsmE2Qi26rp6dQVwTTKG9CmllZ85qq9pROYonWiy2HmblBEgOdXZP-zfWlfgc7YHGHSjnNwF8an-Af1OsjZSEbSYlhRVPfJrlbhtjmU7BqZbB8pt-p6HNEqB0-9QYTDS3Qj4pTTanwhMOOras0NanU7EmgT7ymPAX43mJFTqhTfx6RpGuubySXmRKggmKZsjRy1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494b673a17.mp4?token=NczinAd5Kz90cele1fXv_THpkGHToR2iKl18o8iYRW8x0W6nKtZGupwc5-VF1D_nFyXyk1As0FMHv8LAk-8uMv0bDNf4HH4XQbPX15qEyWPua0810sMNxnlraGgiPAw-TWuo58XWctVbLGMoYxsmE2Qi26rp6dQVwTTKG9CmllZ85qq9pROYonWiy2HmblBEgOdXZP-zfWlfgc7YHGHSjnNwF8an-Af1OsjZSEbSYlhRVPfJrlbhtjmU7BqZbB8pt-p6HNEqB0-9QYTDS3Qj4pTTanwhMOOras0NanU7EmgT7ymPAX43mJFTqhTfx6RpGuubySXmRKggmKZsjRy1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
آغاز حواشی در استقلال؛ درگیری حامیان صالح حردانی با حامیان سهراب بختیاری‌زاده پس از پایان نیمه‌اول روی سکوهای شهرقدس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106147" target="_blank">📅 19:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae32d5f075.mp4?token=cVCangFgwFO9XDzOW5OULwyDHoLfT3ytGuEKmCBN3Pene2HaNWitYHjPJ3grpceOazQBCLlHRrp4hGPjKwJsgyHvv2YmYbP0-JMOf8CL6tCrgRGq0Fltn5I9Kac8R35f-PACsfN3rV0TjPI-GUp4joQG2x85rUTLEXShhI3q_IstrZMF9Aj1LQtYs9HOL8GNgmtDiWOI8wSUdEjYY1dkzbF4IxxDelwuyqMqgPHsZZrVQhXjqcfdVJfqzb-sbmjKSI_Z-3sU5F9RGevpAwP6WmOwf6J3DMGlNB0SQ0mKu5bcKVfcUuNAfQnk73exNwHrgSnJn5ZKnwnh_uzpzXa2ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae32d5f075.mp4?token=cVCangFgwFO9XDzOW5OULwyDHoLfT3ytGuEKmCBN3Pene2HaNWitYHjPJ3grpceOazQBCLlHRrp4hGPjKwJsgyHvv2YmYbP0-JMOf8CL6tCrgRGq0Fltn5I9Kac8R35f-PACsfN3rV0TjPI-GUp4joQG2x85rUTLEXShhI3q_IstrZMF9Aj1LQtYs9HOL8GNgmtDiWOI8wSUdEjYY1dkzbF4IxxDelwuyqMqgPHsZZrVQhXjqcfdVJfqzb-sbmjKSI_Z-3sU5F9RGevpAwP6WmOwf6J3DMGlNB0SQ0mKu5bcKVfcUuNAfQnk73exNwHrgSnJn5ZKnwnh_uzpzXa2ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
درگیری لفظی عوامل دو تیم روی سکوها؛ تنش و حاشیه در جریان دیدار تراکتور و اس.خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106146" target="_blank">📅 19:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnPUBIAkT7ug-0OhAwetcrOUBFFSp6PKapgaNRrqhWDGtmUPepPew0E4jQGRi5i3RkinKaESFHdcd0WjkYRCkRSuk762Rb7V9fqp6TLoIb95GXuDmXtUYwLro8eFirDcPYwyiHNnAngLGPlDPc9Or3U4XkZ8xph-Iu8qMipaTS34wPuCPxX9Y6Bdt3m9WySHp5SmhPZRB86VNFd_X-IT3Kq57B2K8Nb3Z6vGDYtamVpgxqgX2Ka7Ftogi7D87tGBF4WRnW77csNJJIKVyOG5YHUHvdBTHt3Lf8lYnW0Va25PeGkLL6M0BLcwTWMQRagyuGowyzKKGWOg3KCKjT-HhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
فینال جام‌جهانی ۲۰۳۰ در استادیوم الحسن دوم کشور مراکش برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106145" target="_blank">📅 19:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استقلال با این سبک بازی جلو السد باید به آیات الهی متوسل بشه</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106144" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663dc60b7.mp4?token=ncOiDgGai_dsWQEZXQ8xjtI2k7pL89K9XRTex42_flQ28hJbCtl3Msd190CK0Ezeuy5kKly-UBZ6EtEkhGpfji_JGxZQ2n6cthtd21L92DWbvv59J5vGe33KkywW_YZjoKFy7FgoFRFj8ocvmQTYNz8AbGzPY73loodROwHsSaHsskwVpK6zGFpbBSSETnvQTvV7BvKjy02RqxV5X-lTomSgeHMI16aP-v2bbXHGiVK36Osm6uSh6LYj7FmkAMsCQReIM4uRo8mtfgWZhlHvvqEfqBYVbg-oDCMJfHTykR0luiR3UI4YqWB0Nz3IMk5F-D1il96ASjQcVThnhgmMZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663dc60b7.mp4?token=ncOiDgGai_dsWQEZXQ8xjtI2k7pL89K9XRTex42_flQ28hJbCtl3Msd190CK0Ezeuy5kKly-UBZ6EtEkhGpfji_JGxZQ2n6cthtd21L92DWbvv59J5vGe33KkywW_YZjoKFy7FgoFRFj8ocvmQTYNz8AbGzPY73loodROwHsSaHsskwVpK6zGFpbBSSETnvQTvV7BvKjy02RqxV5X-lTomSgeHMI16aP-v2bbXHGiVK36Osm6uSh6LYj7FmkAMsCQReIM4uRo8mtfgWZhlHvvqEfqBYVbg-oDCMJfHTykR0luiR3UI4YqWB0Nz3IMk5F-D1il96ASjQcVThnhgmMZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار جدید استقلالی‌ها: جامو بدید، حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106143" target="_blank">📅 19:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa632d35c.mp4?token=o-wBZgFsm1wW24wSlLphoA2blpaJx9Unhs03y-1Z93v03NZVfBLAEybpWAxVMa6hcUVX5qHta49MYbAeQM3uTkMpisn06XcIDpU5xsjz0LM29-Vuog2auAYYmWnNDwycxH3FWb9RkzDIEbPszxAjQr4IWXtbxONb8TOl5RcpgYTekqjZWP6mHbwzTIJGzeJCtisKn12jpl0r3kjEwXJzJCuE2f_GnHYjdXg7q7rKobRKEqG-FV7PYg7ScsgB9vwrWiKnNG0pGwm0m7u0_AiOrGU98T47gLzsNOFDy4hI4ohVqrp1ZAk8kuiflp5OSHAnvm7OL-NGy1l7JNEQjbQtNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa632d35c.mp4?token=o-wBZgFsm1wW24wSlLphoA2blpaJx9Unhs03y-1Z93v03NZVfBLAEybpWAxVMa6hcUVX5qHta49MYbAeQM3uTkMpisn06XcIDpU5xsjz0LM29-Vuog2auAYYmWnNDwycxH3FWb9RkzDIEbPszxAjQr4IWXtbxONb8TOl5RcpgYTekqjZWP6mHbwzTIJGzeJCtisKn12jpl0r3kjEwXJzJCuE2f_GnHYjdXg7q7rKobRKEqG-FV7PYg7ScsgB9vwrWiKnNG0pGwm0m7u0_AiOrGU98T47gLzsNOFDy4hI4ohVqrp1ZAk8kuiflp5OSHAnvm7OL-NGy1l7JNEQjbQtNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
صالح حردانی با حضور در ورزشگاه، دیدار استقلال و پیکان را از نزدیک تماشا می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106142" target="_blank">📅 19:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=HPLKX8--fsdffAsHday-XHNZKmsTlZZQrEiWjyyW5N0yF0TfKuhqyiGzL5eawvuWyp-ajerCVs6qvOaQxwo3LAM1hyfrr9r0WHKbSiJ1-ONQxgtEpuVxXgtP0nMHnrSS3oAHYyvP2ryqZGKjcY0YfdYVBttMv8TYtj44aelyu8ERoPQ7aHg-pTjMkJJlMErJr1PyWw5-fss2FA25cMAL8SjRU3oFwRsrWoRoE9CXdI9Pk2CoX7c2j37Y7HXsVqRhbmod_ea8zUXxVis40MKPxoiWF5nVROZno5mxnLs9kfuEKNQh-c_6eTMc9fzTMHfQPro0V-8DWkCUsUBEdr4nTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=HPLKX8--fsdffAsHday-XHNZKmsTlZZQrEiWjyyW5N0yF0TfKuhqyiGzL5eawvuWyp-ajerCVs6qvOaQxwo3LAM1hyfrr9r0WHKbSiJ1-ONQxgtEpuVxXgtP0nMHnrSS3oAHYyvP2ryqZGKjcY0YfdYVBttMv8TYtj44aelyu8ERoPQ7aHg-pTjMkJJlMErJr1PyWw5-fss2FA25cMAL8SjRU3oFwRsrWoRoE9CXdI9Pk2CoX7c2j37Y7HXsVqRhbmod_ea8zUXxVis40MKPxoiWF5nVROZno5mxnLs9kfuEKNQh-c_6eTMc9fzTMHfQPro0V-8DWkCUsUBEdr4nTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شعار خاص هواداران استقلال: بختیاری، حردانی، می‌ریم برای قهرمانی
؛ این شعار به نوعی درخواست هواداران از سهراب بختیاری‌زاده برای بخشش کاپیتان آبی‌پوشان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106141" target="_blank">📅 19:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=tmMbFgKmf9fXs598QeMXnKAYlV-VBlKc8EtIcAQFv56r5EY7burx8pCNdpTEEFc7SrePNpgwNpPCnd5EwiDMTovg_cuSCsHnzNfkM9Oz9_46LE54JUur86cv6yNGM01Hr2KkoihOt-JmHCOq-AjtpX280ooBdcGqaWS7zK_FilV4jrpy5QM-x9-fSRAucj62l1ZAx_2VdtJKtK-4LPipYO4F1-wozsh2dmPNXYgGfCEFVMDU-HY_HfqHG5Jp3ybadSVvA-SSOQLFD1M94Fjb2YLRAGxpKTaYAMbEH7yeONY-2mH3L1IVVSzmishTbfFct7N4ZW5w_29v4jHUq6YiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=tmMbFgKmf9fXs598QeMXnKAYlV-VBlKc8EtIcAQFv56r5EY7burx8pCNdpTEEFc7SrePNpgwNpPCnd5EwiDMTovg_cuSCsHnzNfkM9Oz9_46LE54JUur86cv6yNGM01Hr2KkoihOt-JmHCOq-AjtpX280ooBdcGqaWS7zK_FilV4jrpy5QM-x9-fSRAucj62l1ZAx_2VdtJKtK-4LPipYO4F1-wozsh2dmPNXYgGfCEFVMDU-HY_HfqHG5Jp3ybadSVvA-SSOQLFD1M94Fjb2YLRAGxpKTaYAMbEH7yeONY-2mH3L1IVVSzmishTbfFct7N4ZW5w_29v4jHUq6YiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
هوادار پرسپولیس: به عشق رضا شکاری آمدم پیکان را تشویق کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106140" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=feB900E-H3l6_dTu--wjaeZvcqV6Hi_iCVVXtTLKVhME5Ow3p6_z7oulQ7WJqaD9nEFwMcdw1R8zjz3YPJIBM4GZv2cgBAJq8jmVAlqMDax_krBsa6ysWXOAd45b5PqFuZBFS4I5hD4zGeNHuv0WW4vOKuVrtqptAilQv27Vmnhnx6sHbHzfMNRh9IpmV3i49iL6a7zmnEX8nRQ-X-5QQZWjHo2i3H8Un3cRBptL5Y-zWqZUsAdWM1DOuboVMDak3v-fFAFP1VdOb-kKwN_16NLRA01fBSXNYGeSxvUWXbHN-ovmPsqmEHrt-bY34tQ7ihTsuS0kVZ3qxehTmy7VEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=feB900E-H3l6_dTu--wjaeZvcqV6Hi_iCVVXtTLKVhME5Ow3p6_z7oulQ7WJqaD9nEFwMcdw1R8zjz3YPJIBM4GZv2cgBAJq8jmVAlqMDax_krBsa6ysWXOAd45b5PqFuZBFS4I5hD4zGeNHuv0WW4vOKuVrtqptAilQv27Vmnhnx6sHbHzfMNRh9IpmV3i49iL6a7zmnEX8nRQ-X-5QQZWjHo2i3H8Un3cRBptL5Y-zWqZUsAdWM1DOuboVMDak3v-fFAFP1VdOb-kKwN_16NLRA01fBSXNYGeSxvUWXbHN-ovmPsqmEHrt-bY34tQ7ihTsuS0kVZ3qxehTmy7VEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: سهراب هم مثل فرهاد بدون باخت قهرمان می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106139" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8269376a.mp4?token=M-qU7p0vFOFBqfTUKZWodM5irKORJjvwVmxBLqso69t4Tc6qY7oT75EeoGuiJLX2t-fMB35EHOVmLX2dW0R-sYKdoMVZfXmpFiFprKHk3yp23SOm8K8B9fBtrMO-du5Sa6Xl7HO2Lv7mMJEZCUOmlWaLDb3PL3Ugv6P7ciUFN9CQmzNaVlw_huxGSfWT8NJJL6cIK1G6EembisASwDfcgXVMEZgQ9_qyGoyBHAp7DwJnA96doQ6LDDMsuHHF3hr4jlxdE-6d2jOS1EsOqvyu4FXozpL03QoQxghcL8tlc3gt22XMpthY73IpXZ3GOV1IUw_HWxP1_8rJTYWT88zy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8269376a.mp4?token=M-qU7p0vFOFBqfTUKZWodM5irKORJjvwVmxBLqso69t4Tc6qY7oT75EeoGuiJLX2t-fMB35EHOVmLX2dW0R-sYKdoMVZfXmpFiFprKHk3yp23SOm8K8B9fBtrMO-du5Sa6Xl7HO2Lv7mMJEZCUOmlWaLDb3PL3Ugv6P7ciUFN9CQmzNaVlw_huxGSfWT8NJJL6cIK1G6EembisASwDfcgXVMEZgQ9_qyGoyBHAp7DwJnA96doQ6LDDMsuHHF3hr4jlxdE-6d2jOS1EsOqvyu4FXozpL03QoQxghcL8tlc3gt22XMpthY73IpXZ3GOV1IUw_HWxP1_8rJTYWT88zy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: مشکل فدراسیون با ماست؛ وگرنه جام را می‌دادند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106138" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106137" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZBiIhikbmA5iS2Sq0EtFicwNZxDtGXYtYDDUPMo__uekquBsW3d8STYjAcr8kcTqmP4l6FCbLcPmoP-LrNJ7spNvlpTt9lTaKZjODB_kzQfZGb-tG_lnghKWGiTw3wKRUmyNUb5rTf6jS7iWgn7rJBKYl8or-hWf5yEQQaVCGXDyHnzw0Blp9yQnnL_9WCVld_J-ChrAAypmYdeKhtJjeIcFtcS623_HpBO-xrZKkISbQq6ORsuQmhhDGQMMsbp3LOpZS6oZq-snk13qJ__roOBFl35XKzVt4x-VdrJfB5UUoR5Wc1mQf5ikBMc1x7bO9FR2l09CGf1CHkRcLWhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106136" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjxaLreDIG2GySHPVBkU5PSSK2JLaK7AZ5xi9z7JrnzKlJwW3thDAzWy6myfv--zWrkrFw-aT3LRpEVhEe3AovQnI8AZzsg3TGCGKntQKhDwEpULVgI-sRBNBjXQINmCmh1Ux9bbZf1JWxlWPPWGFpBU_w6y6BFvjbiFxrRvqC9bHWePxwqP0-ivyicUfSFm8bpzACRI3HOBpH-NP3uXwPPaUNlA01fk_NhfNbCboSFS4uvwFyHlUta5LESOb4X3Om38yKR3tpQmEX5yalcUOxutBiVGnT6U0_9dfHHRor2f7NTZh0hW5AlYRb7565mRrRV4DdfZr7uEmkeR535dVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106135" target="_blank">📅 18:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZe9qQhpidL0tJDdlxBfQhNmVYM3H8CjWbTg_jIcbwZAgPSF0SQ6xDajtgDEpo7BqTHtPdyQ-8j8-0n2rwvAXoAHnJeTFZANKfYUYdjkSppvUZOsm6lUMRWkEbcZSInsx7258G73rf-dF1RsaA9S4V8emx-nM9xoy119HZZj3ERRUXtY5vbvEOwsAPmfxwitKzkwE7Avj_4twgiknLo6-7eToc5wDhcmvMYqtl78iHv9irPkJYJIELxql394HrkrWMDo_fIcUsQMJ8FcbKK4N-OLTipoQIEmuRwFnPWQfvgFCifdpSTKYwzsviCOEXcUdCm5PcsPKl_XmqgCRb3vGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106134" target="_blank">📅 18:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106133">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
ترکیب تراکتور برابر
استقلال
خوزستان
علیرضا بیرانوند، شجاع خلیل‌زاده، محمد دانشگر، صادق محرمی، دانیال اسماعیلی‌فر، محمد نادری، مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و شهریار مغانلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106133" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73a4eaf66.mp4?token=pxQTSd8fkKgyXLgMu6CsL2NyYsNQz8H_ipv1dSsauQxzzDGVLEV15heBP7o3RDP5NeWiqTPr0AkUB5r7j5c882Rwfs6Q8Wvf2c_PGe-mvzZPZ-p8numxW2hTViin76CyQKtZccVJoaRV4A94kDt5oZEstqnjZWzdZxtKXkcBSbz8g5OouH-w1aJYqBgQuojAOOxDFaWN6HJbQF7oL-XXppvQRh90g5vaGBleBBMHYWmQhSlUT-TVjYh2yWOg6S6bw2XUpsV9VE6_cEb479ITsqU8RKH46J9wVvJ4HhyTMRtKSozuRaXFVf9BiJZFIH47QK-o0XzK0NepmF8UTUa6xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73a4eaf66.mp4?token=pxQTSd8fkKgyXLgMu6CsL2NyYsNQz8H_ipv1dSsauQxzzDGVLEV15heBP7o3RDP5NeWiqTPr0AkUB5r7j5c882Rwfs6Q8Wvf2c_PGe-mvzZPZ-p8numxW2hTViin76CyQKtZccVJoaRV4A94kDt5oZEstqnjZWzdZxtKXkcBSbz8g5OouH-w1aJYqBgQuojAOOxDFaWN6HJbQF7oL-XXppvQRh90g5vaGBleBBMHYWmQhSlUT-TVjYh2yWOg6S6bw2XUpsV9VE6_cEb479ITsqU8RKH46J9wVvJ4HhyTMRtKSozuRaXFVf9BiJZFIH47QK-o0XzK0NepmF8UTUa6xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
حمله تند هوادار استقلال به بختیاری‌زاده: برای دلخوشی پرسپولیسی‌ها صالح را اخراج نکن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106132" target="_blank">📅 17:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7cjigX5rqAo7Ea1cdwzlCVU_BSzLWA5GJ_yWE8GVEuKY_JwI9NooLdwb1Xpq4c_FlryabL1vgZpjKxO0tGPJQpGOmzW0H3vYScUYa30vxWIIOrGFl36CdKlTnaXOvq2fqOFzpMYUCZGEb_g9azgOaFuBgI3wbbAwTQrCl7apUPdLnlI65CdmxCYfKxEjXFujjjetADThs-OW40E_lXZeYwXJO2jWLZaMR1e2UgQzdqq6hsZJV5rRUCCYOLhegKpY92Wkm1JYj_8SCD0iIlKIqaieEXuwgT0go6wGdlHrJGhpRZ31aq-YTTimDh-SnbjpOvIhtrbUQ4_HyJbbnwPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aidq1biBAip7YYFu__T2E3mzQvqgXYhqyjKxlcx0aPoesCG2iJVEPobGbzSRz-kyZa8ZvsdgYtNGriGvWhmcs7P3dIAAjpObCOpdDQkpTwz8AZe9-x9zEtQGO9_sWHFgwsL2N-ZtL1UsIGKL4bvZx3B7QEeR8vX58zjaoPjDUUGk31yyu18ijNZ8p5UpZLgumHYPt12boswLv8YX1wiW5Z--hQu9mGug9C3DkDJ-5lLn6gnywBHES88O-uXdaJe3tlsczOL01cdVjfGfNYDY1oGK_3RmJf2DlnRm9nZbLANm-aR1sSH_RjC7Bj89O_H-N-sI4yTBWiKQYpRMCG2I3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rn5YSKic75DiTjXoEgKkX82C5XGASfbn-ATfcpkyVSblWehhqYzOe9yh6lIaWKYWt5w_8h-RmH1gK-paVslNdxLcOsiy4371948uYrUZ2mVSnqX3FfU7omlURvVeX5FIVku4ocsBW_mzimirPwkqemusi3rIIwZcPtk-6JbuYHHMAyPtw065T7mXzZN3ykWt-nCP7LsYyYMtX0uAvS6ZzpS_Tz-PGsWdzGopoCNT6_fMC1hxd3_wlIj7PxTwCO0e3A9KvCCX-Em5e0j5w4Tnz5J9Ts5cDMKVoe7K2VQfTZa_owPTsjkEALFmwb6SKuzyiuK-eAwkbKoQ3EvLjc5uPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNii3K7PwKefW7Qi5qhn5Q2u1DWlXsncEaMQjf53cyDIQIO_jQZtYvFhpRsmJqOpvndMLCu2MUKKHHrtIl_enE52Z-IrGgVfdYVDFdXFIMI4gl_qQQxy_K76VHItBDwuxAg_4np-1lZ8KogUtNPLrLWXWjbZx3qDxT0hadJrGCVfqPH7NyIe7RnTqPwqFeqZIaQRJpx8dxrNw_LgmzIY94OcXwKt6xD8CuOAfezJnDFY7xmX9BsXevB5RU_v0PMPBUCkCUz8CubQbC2BRE5qWGmDgqVCw3HV1apPHP6TgYMnE2ncNGn8S_2O52vJHkjVzK6BOJ2I2tRh6YnN_OheIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😍
زیدی خوشکل و سکسی امباپه تو فیلم جدیدش یعنی "Drawn Together"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106128" target="_blank">📅 17:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81979f53d.mp4?token=ph3ExifzRF9jm_gK7UvvnFv7xWCo2ciFCxEbgjjIqC3ID05ngVlvsnPVogJp-PjfoU3DMOiU_ozM-vwnwMkO2qRPLkNC2l7z3cDjAXXXEc7qBXDZjla7tCvUXVS_Ilu2f6vQfbYRtBihjvIGCXnViBvHPnCIu_FOy520FcWwXXavjKuTK8nvgkWgggwjBBwM79shFDztxKcvhDST6yrC6-49eV0zMvXdoDO1o4xKQivywi9FjGgPNUpQsYPnB8RtBZ-NiMBy_BexuIUJt8gubWTj9zGLVDCyDVgS0Y2_d1XYrHnt4o9I0KEGVT7sA8sq4T7t6WAv-p4m2ZSXB6wPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81979f53d.mp4?token=ph3ExifzRF9jm_gK7UvvnFv7xWCo2ciFCxEbgjjIqC3ID05ngVlvsnPVogJp-PjfoU3DMOiU_ozM-vwnwMkO2qRPLkNC2l7z3cDjAXXXEc7qBXDZjla7tCvUXVS_Ilu2f6vQfbYRtBihjvIGCXnViBvHPnCIu_FOy520FcWwXXavjKuTK8nvgkWgggwjBBwM79shFDztxKcvhDST6yrC6-49eV0zMvXdoDO1o4xKQivywi9FjGgPNUpQsYPnB8RtBZ-NiMBy_BexuIUJt8gubWTj9zGLVDCyDVgS0Y2_d1XYrHnt4o9I0KEGVT7sA8sq4T7t6WAv-p4m2ZSXB6wPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار استقلال: سهراب باید صالح را ببخشد؛ ستاره سوم را می‌گیریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106127" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59106dd8ec.mp4?token=gk8t4I9xmF0O_5wWr6cr5IGh2VwzmzUSkIAoGao2LoQOwEKFzRahvSh6O8m93hWxftpvhGfLTbaJeg294kRAKs7bopXeSBc-EZuUfw4kzTvM2dFzU_Spxk12v94JO35WeuZUd9ql-Ek7aT5cGXuASPyqOyAasZH93vvEz_Ttz5q8oHlS4Nuxpf4rpaVVpxzujjSYPS5I9su6wlCNbPK2P75JlSmL0TmT5zz-cOUGeWRpNLIbANwkDmw4IpNBwsMXLNXAIg0pSxDMcdvzuiuvr7MCOymfjnPTrPZiCM1ejEbiH56i6SIz_EIIhHry6AozYIyWNk6j8DnMXE8oDHCXIhbV_UzdoH267gmXBFHNRJPtUW8H8GDWI3tdpSX5fDjJPIhbweaMhhT2U6OnbF4qsbrP2UaXTqEHc087iWTjZ4T3oECBwzv7etUHhOdPO5QzjrUvOPJn_-5eoVA5ypUv2m72NAhr9eqYYTyt_8IZo0nFbUXBicKanLDW4Nti_TfNRtXvSZA_dmNSrVvUPYpk23D3QB25kxUlI8IfEl_qdwo3jMB-8aqdDtEoNyMsbeAI-SA8ouehVLER7RU-UfyEN5Z44X-CTLK6vrAL6RycR4nwVdFk8QvhvUx-TdVP29CROQRkaN9MYlsPmE-crkynDTlck8Ey4T4leG3I4vYz250" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59106dd8ec.mp4?token=gk8t4I9xmF0O_5wWr6cr5IGh2VwzmzUSkIAoGao2LoQOwEKFzRahvSh6O8m93hWxftpvhGfLTbaJeg294kRAKs7bopXeSBc-EZuUfw4kzTvM2dFzU_Spxk12v94JO35WeuZUd9ql-Ek7aT5cGXuASPyqOyAasZH93vvEz_Ttz5q8oHlS4Nuxpf4rpaVVpxzujjSYPS5I9su6wlCNbPK2P75JlSmL0TmT5zz-cOUGeWRpNLIbANwkDmw4IpNBwsMXLNXAIg0pSxDMcdvzuiuvr7MCOymfjnPTrPZiCM1ejEbiH56i6SIz_EIIhHry6AozYIyWNk6j8DnMXE8oDHCXIhbV_UzdoH267gmXBFHNRJPtUW8H8GDWI3tdpSX5fDjJPIhbweaMhhT2U6OnbF4qsbrP2UaXTqEHc087iWTjZ4T3oECBwzv7etUHhOdPO5QzjrUvOPJn_-5eoVA5ypUv2m72NAhr9eqYYTyt_8IZo0nFbUXBicKanLDW4Nti_TfNRtXvSZA_dmNSrVvUPYpk23D3QB25kxUlI8IfEl_qdwo3jMB-8aqdDtEoNyMsbeAI-SA8ouehVLER7RU-UfyEN5Z44X-CTLK6vrAL6RycR4nwVdFk8QvhvUx-TdVP29CROQRkaN9MYlsPmE-crkynDTlck8Ey4T4leG3I4vYz250" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صحبت‌های عجیب و وایرال شده امیرمحمد زند درباره تفاوت زنان ایرانی و خارجی که در فضای مجازی موافقان و مخالفان خاص خودشو داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106126" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dcdf837b.mp4?token=bDqZHhN_VGkaSfZuLVyccQ7Kg6S7XAhnUKhtGJmMBduWYyGfLYHkk9uhgxq2lp3ZMcOf0JwzaB0veCZmxMbN8HiTWk7XkYpW11FxaU-molRc09QttF9hrFfT0Ue7-F5YB0WH8PpBCvYfxigtW_4jH2GOVIgWmZTknZDWwuKrcNJOU30FWR9Gym0T3yTyJYJGtrTlBTtrRqFnn2k-P-WcKDXiIzWc7ZgCaEqZPTalsEKcj8AK17THEVp8I-v50F_6iuV5emfqQAXzeaM6OIZdm7zc4nuPzKYlFlWWM5Kuj0qGsCqmSfpdVDAVo6miX_GHOUVQ7zpq-MWGsV3fJZzRoicyqR3X_G3m-y4TcCmKgrs5Q1YnkgrVTp8GEHs3I3T2_nhijNDfZh6IIEnNZFh6nX0f03xj7ol1GGhlXNyPWH390s_WA3jkiRAk0f-rlL0QByOaXMbgrSWpIi-Zzvqsv3_vHfk2r82QGf8w0o4YZs4FCN_SV1vbMe5GDe6sO6_I0I3J1DXu6Ch8VKuOZ6e2GkJoB4xsKHneRK3v_IrjjxDTW4zSFZ75HlEel33Pt15LoG-DlmmIM-Hq9cDR4hCRZqDXIM462t1yxC1e8z0ucWNf6IT_T0QoaspiYOK2BySvnhOvz1pS7qcopvUUBeyxWUpoAtJ4qlz9Qrva7vGRqIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dcdf837b.mp4?token=bDqZHhN_VGkaSfZuLVyccQ7Kg6S7XAhnUKhtGJmMBduWYyGfLYHkk9uhgxq2lp3ZMcOf0JwzaB0veCZmxMbN8HiTWk7XkYpW11FxaU-molRc09QttF9hrFfT0Ue7-F5YB0WH8PpBCvYfxigtW_4jH2GOVIgWmZTknZDWwuKrcNJOU30FWR9Gym0T3yTyJYJGtrTlBTtrRqFnn2k-P-WcKDXiIzWc7ZgCaEqZPTalsEKcj8AK17THEVp8I-v50F_6iuV5emfqQAXzeaM6OIZdm7zc4nuPzKYlFlWWM5Kuj0qGsCqmSfpdVDAVo6miX_GHOUVQ7zpq-MWGsV3fJZzRoicyqR3X_G3m-y4TcCmKgrs5Q1YnkgrVTp8GEHs3I3T2_nhijNDfZh6IIEnNZFh6nX0f03xj7ol1GGhlXNyPWH390s_WA3jkiRAk0f-rlL0QByOaXMbgrSWpIi-Zzvqsv3_vHfk2r82QGf8w0o4YZs4FCN_SV1vbMe5GDe6sO6_I0I3J1DXu6Ch8VKuOZ6e2GkJoB4xsKHneRK3v_IrjjxDTW4zSFZ75HlEel33Pt15LoG-DlmmIM-Hq9cDR4hCRZqDXIM462t1yxC1e8z0ucWNf6IT_T0QoaspiYOK2BySvnhOvz1pS7qcopvUUBeyxWUpoAtJ4qlz9Qrva7vGRqIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا مرزبان مربی سابق سپاهان: اگر بجای خداداد عزیزی شخص دیگری بود، قطعا محرومیت سنگینی برایش لحاظ میشد. عزیزی دارای مصونیت از سوی حکومت است و در رای کمیته انضباطی نیز همین موضوع مشهود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106125" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106124">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlZzb8WVmlQIQvtE2GbT-_CVJhR_IRiVmb6qvSxBThfBA6pTt4k1s5md_o0cvUFfRW21ZV_lR7gwFsVOoFvCqa8VBten0B__sFeo4royj9HKc3v00N2EilRftsVQGvEksQhOygJOzd2ZH-f_zeNM9IbKTwGXnbiiWTNK3Jg40Uc8CMlhNoHfcR8jtQ2G2dMINb4EQIVIFgU0WdMGuz0zeGAA83-DGen8K_FifcrqYFnq6a049c6GI2RPpVnB7ZCrxczbm1WrDbNqAWw0VwenbLCfXp4MKEIU9xeNEn1s65AXdbOPSdyeDck0TGRZBVuJlK4kYPTJaZ3rX6fC5BagpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید بزودی قرارداد آردا گولر رو تا سال 2031 تمدید خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106124" target="_blank">📅 16:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106123">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5becd61f50.mp4?token=pCD2WIomqApoKpKa5n-qmz_yCuIDYJfogaNfpeBncdf3qwRDsKL38md_rMfETWdcaN2zJbimK_qLXDAZ-3rJPz8-QvIIU0kQPwqS0gDIO8yovJJp1RTPkNW6FDGmswZq9ZUcpat5wV7l3i4qR2DNxdtsMl2WGAJMhRT_SHKnRCqfYSIPRRC3Mq8jn_BJRqM1pi0IZqvDoS4FqQORoKY-_xSftTE0iP87BArue2GgTzhK8CxK2_zbTROMACNeZPAEDzrhkKzS2OWahCBvC4vZkyc8YJVs_KLS8tRxGAtUsaqKULf5l773dLPvYHuRwe8bnEAFrXQQtttibtTx0xAbkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5becd61f50.mp4?token=pCD2WIomqApoKpKa5n-qmz_yCuIDYJfogaNfpeBncdf3qwRDsKL38md_rMfETWdcaN2zJbimK_qLXDAZ-3rJPz8-QvIIU0kQPwqS0gDIO8yovJJp1RTPkNW6FDGmswZq9ZUcpat5wV7l3i4qR2DNxdtsMl2WGAJMhRT_SHKnRCqfYSIPRRC3Mq8jn_BJRqM1pi0IZqvDoS4FqQORoKY-_xSftTE0iP87BArue2GgTzhK8CxK2_zbTROMACNeZPAEDzrhkKzS2OWahCBvC4vZkyc8YJVs_KLS8tRxGAtUsaqKULf5l773dLPvYHuRwe8bnEAFrXQQtttibtTx0xAbkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
جیمی کرگر درباره هالند
: "من اصلاً نمی‌تونم تصور کنم که هالند هزار تا گل نزنه یا بهترین گلزن تاریخ نشه. تا حالا هیچ‌کس رو مثل اون از نظر تعداد گل و آمار و ارقام ندیدم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106123" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106122">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a155534f18.mp4?token=b3TNPoHy9akBAoIjBGT3N-7YSqDzEEhcxNe1Fq9Nfu8_Ndv5QR2PsQPr9sQKGkuw9gsmnyoQNidbWV0-gwTNj22Kk-RjSfzrR00r0rzorJwS2wCnGMrkk-eiczkXFnSEIaBZASa0RqpQ6uPHm5YoL_jSsCzNaejlaAJDmlSnuOyzY3eyP2gBF7gr9K9aELjfufQt--R1cHb-VUzy2zJf3Oousu4tvA0y5FAMlE1pA3yyJyU0fGZOZFoO9wDN5dnHbw3EUJ-vSQegZu4JzJMtYk3e-DPQUbXhyf44z0oqEIuU1q8D47XJMWUAuC9BmcLLwDJhcByNUgNZEwZsL-dilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a155534f18.mp4?token=b3TNPoHy9akBAoIjBGT3N-7YSqDzEEhcxNe1Fq9Nfu8_Ndv5QR2PsQPr9sQKGkuw9gsmnyoQNidbWV0-gwTNj22Kk-RjSfzrR00r0rzorJwS2wCnGMrkk-eiczkXFnSEIaBZASa0RqpQ6uPHm5YoL_jSsCzNaejlaAJDmlSnuOyzY3eyP2gBF7gr9K9aELjfufQt--R1cHb-VUzy2zJf3Oousu4tvA0y5FAMlE1pA3yyJyU0fGZOZFoO9wDN5dnHbw3EUJ-vSQegZu4JzJMtYk3e-DPQUbXhyf44z0oqEIuU1q8D47XJMWUAuC9BmcLLwDJhcByNUgNZEwZsL-dilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی نامزد نهایی توپ طلای ۲۰۲۶ معرفی شدن.
🥇
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106122" target="_blank">📅 16:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106121">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eeeaa17c6.mp4?token=SOgb-RBR3JQC53CvZAJCyDdqVkhaFulyZgeNGM5L9i9DusngJujU7J3J3FWuTfT_C7E7LMd6Ia3jquvCTBE2hrxJ45e5CkyQB40S9_poX4lNFCJJnDj41x_4tKFISnriF1pC16jGcHOEDWQZGTZiAd8bhY20xJF0WTK4mOKzlMaka0AJix6F1WdsN5_MnVgAQZb8OlGpcy8K081Sy9x0TDCHLzt-UEQ8g0-oUqLQJF9fSD6aNmnsCw1pZgDBpJ65XgNyQo5ihUIjua-dicvI7G0F8aMFc3AraOmoyqkV-gnFOLAk_pVOMMhWDf0mT-_IGmI-XobCCi7A7gFosuKzGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eeeaa17c6.mp4?token=SOgb-RBR3JQC53CvZAJCyDdqVkhaFulyZgeNGM5L9i9DusngJujU7J3J3FWuTfT_C7E7LMd6Ia3jquvCTBE2hrxJ45e5CkyQB40S9_poX4lNFCJJnDj41x_4tKFISnriF1pC16jGcHOEDWQZGTZiAd8bhY20xJF0WTK4mOKzlMaka0AJix6F1WdsN5_MnVgAQZb8OlGpcy8K081Sy9x0TDCHLzt-UEQ8g0-oUqLQJF9fSD6aNmnsCw1pZgDBpJ65XgNyQo5ihUIjua-dicvI7G0F8aMFc3AraOmoyqkV-gnFOLAk_pVOMMhWDf0mT-_IGmI-XobCCi7A7gFosuKzGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇮🇷
تیکی‌تاکا جالب ملوانی‌ها در هفته‌گذشته مقابل تیم مس‌شهربابک که منجر به گلزنی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106121" target="_blank">📅 15:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106120">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdxlDKRu8SOgH-4faNSC69GnDF2AbStasj6HUYOVdlpE88ujOd7UnNwAR_jHfPFfhAfnMcQImK9KX3wfqhxryTCux_3Utb_QN9uZZ8t2hACV1rNkFplIN03MpLUJyAiyPPJpGyh5As2iwLerIunwbyOc1pIE_EkOLbdh_d40Trk-VQYyi1L4DN75aeNgWB-8Zj99Lhp6TY3vxFMbymUaa6L2G9s7pvnIbk13hap3llK-GV0jMpghyeYGR5TFcdOYeLundEQz25mGHZh_vW17c7_nixdEvlzie6CStaTxJcE6trjJ-hRQclKwdH6Wx6Ty71D0bCXIc60qPfrFu6x3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
🥶
🐐
🐐
فقط یک لحظه به این موضوع فکر کنید. بیش از 20 سال است که آن‌ها در بالاترین سطح، هم‌زمان حضور داشتند. ثبات آن‌ها واقعاً ﺷﮕﻔﺖ‌آﻧﮕﯿﺰ است
💪
⚽️
رونالدو: 18 بار نامزد، 5 توپ طلایی
⚽️
مسی: 17 بار نامزد، 8 توپ طلایی
👀
✔️
امسال مسی برای اولین بار از سال 2023، نامزد دریافت توپ طلایی شد و با این نامزدی، تعداد کل نامزدی‌های خود را به 17 رساند و تنها یک بار از رکورد تاریخی رونالدو با 18 نامزدی، عقب است
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106120" target="_blank">📅 15:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106119">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ab051ddf.mp4?token=CCeGIBLbkZ0NAOvoufiwEV6HPaUXynGn1cm8JcvpM5WTxFb63jjz4XOZJx0xY8F-VbsVAxjWLWPN0T_OvwWX514xRT43HQf_GJ4ZygW7cgUTBYX4XvXC0nobzbWwyj8_Y7ImFUol1vjkJSrDZ4Hi2DNvKD5SVYRFiSXETRZ87T0PiSEbvf76sioConQMH-Qk0DAPblthIDB69V9JEEVra3Bx8DRBWuqR8gcsuJCEaCHW87gzqYMlgMZzilZ9DbTuF-BTP5Xgm0NAC9YAaOECCCL7D3kQXEPlqiluNhoXC98cjSOp22hxKBOU1RFsU78MZWmnHHI5nWXS6lHu80gfkR83sp21m2heTZKfUwJc2fih63lwAg8NCQ6HoJgHzvJnOFLE0zcBTzt_xmbu9ibJDjI2DvqrGoTHJrW4ECLkGzZZp1k8Y19S11keFxURl-Z-j-lo_5fYPbHLY_wNxxC5SFmD8BBBoYRkc15a-VOEuHqUeJGFkyJbICL5ymguMFumsW0tPL4QM2pxfniiExaWppOTBFJxKzKEYmpamRQmt92D_pB7uOKpXuk8uOi_BxSYE4lYNmsf-1W0c9YtXk6R6WC97WQsGcgdzDj6hfOM39VIyf5qZngfuGUWbCjIOS8xXXF2s0_wGbPJycY3Ph8v5a8gqMZGBX49BQmtzSAeER8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ab051ddf.mp4?token=CCeGIBLbkZ0NAOvoufiwEV6HPaUXynGn1cm8JcvpM5WTxFb63jjz4XOZJx0xY8F-VbsVAxjWLWPN0T_OvwWX514xRT43HQf_GJ4ZygW7cgUTBYX4XvXC0nobzbWwyj8_Y7ImFUol1vjkJSrDZ4Hi2DNvKD5SVYRFiSXETRZ87T0PiSEbvf76sioConQMH-Qk0DAPblthIDB69V9JEEVra3Bx8DRBWuqR8gcsuJCEaCHW87gzqYMlgMZzilZ9DbTuF-BTP5Xgm0NAC9YAaOECCCL7D3kQXEPlqiluNhoXC98cjSOp22hxKBOU1RFsU78MZWmnHHI5nWXS6lHu80gfkR83sp21m2heTZKfUwJc2fih63lwAg8NCQ6HoJgHzvJnOFLE0zcBTzt_xmbu9ibJDjI2DvqrGoTHJrW4ECLkGzZZp1k8Y19S11keFxURl-Z-j-lo_5fYPbHLY_wNxxC5SFmD8BBBoYRkc15a-VOEuHqUeJGFkyJbICL5ymguMFumsW0tPL4QM2pxfniiExaWppOTBFJxKzKEYmpamRQmt92D_pB7uOKpXuk8uOi_BxSYE4lYNmsf-1W0c9YtXk6R6WC97WQsGcgdzDj6hfOM39VIyf5qZngfuGUWbCjIOS8xXXF2s0_wGbPJycY3Ph8v5a8gqMZGBX49BQmtzSAeER8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پشت‌پرده جنجال‌های اخیر امید عالیشاه در تبریز؛ خصومتی که سال‌هاست ادامه دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106119" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106118">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc99cf37e.mp4?token=T_kRMoW5lxJ5dGDei0hH0jbwr3hSYgXTYZPZgIR8tLJV52LVyJFv8Bpe5pMLdOzFBFWoxB_cyq4rtglElTxOEi-r7SwgQGg0-SvJI0wr-zR2t_GIV30SZwUskIcT_MWk4alimkNfmEEllcrciSPPAMPrkihF4tDQOGtuhKphA0fwSzKqQiWXn558IfLWRh54-ShIW9fMMVeyDr02PxRF5hzidHPQ3y2sFannTVQfre9ESOsWeypi0GUX0UbEHs2adJeR55GvjU2JOnOe3ppTHqAOol42qu0r0Kkl1fN2E2YNdtxafQOpd5AcR5Ff_OVIdTR9VUfwBfUCThLF1MRjYq-HYxcedaqRxBaPYucLYzOxruDrCIq5bMwJDJAI_m46bQ8bOW9Ls5mrgRLtwtvmYSZJzyDLfGlinPb1j2PPFMu6XPlX5Jg7mT9NcHYViTcl4GA0ckMsaOhraynYLdnTkor_DtUEbBOxF-EkZAE_15dRuCx52-JPSx_Ez3V67PocyBEq_JUXk7NOFsePsdnmZU5t6B_R33QafguROIkBokE3x_wnxLw1_uemmcR2qd3NOlThOq3UKqPZZNKfmCUb2oPnpJJU268BK2gV3lqfu3tTSoZ_4fWiYRkTitP7SFkXFzXhNgVZWyn88QdzqnSOiR94KlI6KSghefTVBolZ8Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc99cf37e.mp4?token=T_kRMoW5lxJ5dGDei0hH0jbwr3hSYgXTYZPZgIR8tLJV52LVyJFv8Bpe5pMLdOzFBFWoxB_cyq4rtglElTxOEi-r7SwgQGg0-SvJI0wr-zR2t_GIV30SZwUskIcT_MWk4alimkNfmEEllcrciSPPAMPrkihF4tDQOGtuhKphA0fwSzKqQiWXn558IfLWRh54-ShIW9fMMVeyDr02PxRF5hzidHPQ3y2sFannTVQfre9ESOsWeypi0GUX0UbEHs2adJeR55GvjU2JOnOe3ppTHqAOol42qu0r0Kkl1fN2E2YNdtxafQOpd5AcR5Ff_OVIdTR9VUfwBfUCThLF1MRjYq-HYxcedaqRxBaPYucLYzOxruDrCIq5bMwJDJAI_m46bQ8bOW9Ls5mrgRLtwtvmYSZJzyDLfGlinPb1j2PPFMu6XPlX5Jg7mT9NcHYViTcl4GA0ckMsaOhraynYLdnTkor_DtUEbBOxF-EkZAE_15dRuCx52-JPSx_Ez3V67PocyBEq_JUXk7NOFsePsdnmZU5t6B_R33QafguROIkBokE3x_wnxLw1_uemmcR2qd3NOlThOq3UKqPZZNKfmCUb2oPnpJJU268BK2gV3lqfu3tTSoZ_4fWiYRkTitP7SFkXFzXhNgVZWyn88QdzqnSOiR94KlI6KSghefTVBolZ8Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🍏
توضیحات بسیار کاربردی برای آشنایی با آپشن‌های سه‌مدل جدید آیفون 18
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106118" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106117">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f226d46bbd.mp4?token=gp56subNeCnTlMdD1IuEIpudpmqylmpRXpzkSyBwiN3tghx-yW5JR7xY4TzBJI6gFp2q6OWoXmYBM7U21h0Ky66HGLU36KywZxYM-hsThTRVAe_EjuqU7RoaO2VDUGh3pdarhidhHEzukBYopXZhV52rvSLX53EyLwYktze17i-z55GYhOBTgVAMAfh1eOwfmW9MYo_7O8X1isKQQnh7OcumGUuGLjlbnwi0ADIbPvTeoThvF3Nnomg3t0giIhb_VF5WJvn3nEC4INcNoh7FDUvVqwVqv1uMZHJJdo2Kokh1CrfmYGJeOEAOcasZJunnxsesiGW2ORfysPQ6KGgfSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f226d46bbd.mp4?token=gp56subNeCnTlMdD1IuEIpudpmqylmpRXpzkSyBwiN3tghx-yW5JR7xY4TzBJI6gFp2q6OWoXmYBM7U21h0Ky66HGLU36KywZxYM-hsThTRVAe_EjuqU7RoaO2VDUGh3pdarhidhHEzukBYopXZhV52rvSLX53EyLwYktze17i-z55GYhOBTgVAMAfh1eOwfmW9MYo_7O8X1isKQQnh7OcumGUuGLjlbnwi0ADIbPvTeoThvF3Nnomg3t0giIhb_VF5WJvn3nEC4INcNoh7FDUvVqwVqv1uMZHJJdo2Kokh1CrfmYGJeOEAOcasZJunnxsesiGW2ORfysPQ6KGgfSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
تشویق وایکینگ‌ها در قلب قزوین :))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106117" target="_blank">📅 14:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106116">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf79d5ef7.mp4?token=SUMWtA1jZ2EbSbkTxEeICrA7OIGUvayIue6TlObRksZwBJiWDlqso2PXc8HVj-UkGljHO-KsBAFm8o04WU63hbcxiSvKxSVSyfyxLQ9w0m8JBXR3VIsyXPyKvanrpSQpk2RxXv8HXtrPdTY7XNLcGONQIVp0nbrUzx-J9TPMauojKiIaEVSim5KBNX6xWT7KYE3xl7A2PX3FlS5MXAPbOJpuDx7I2GJcZrQy7OrVFJ8WJYN_dq-OCprsGhXmP3SiCTAnBgmFapFr8ES-ANmmc_vHT88F_2d-KLDUl6y8Nb7g35hLnN3OOD7uj1y--Wes-rX3SNJYMrLJuVvz1SHMOHcPXAvHHH9tV_Mdq3gOzx6eGi0hQD83Rhc6Nw03Dx9_HzpX00n-acOlWH8VJxUf1gluEWCK4K1e9_o4NHnjFk55Jh4QnozUDFLuvRZSdiWGDAhZNSpTJdxmq18TaFn9JHuzky_9sNrx--EJoQ2z9dsk9QvJD1thL-ASD6lk2TkuTbB7VQC86oR6po5huYrcfjJh9VyRz6BDa7yyOkM-hGPduudNChQP98qh2-0hwGoxm2AmS10sHtssFuoN816MuLsciksPcf5-nMJIbQRhCocgEpdPKlwZOLkQO0nnLapIDorZ9QA-2zeeZ0AJlgt7hG8ydU0vli3ij4nwDNFGdgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf79d5ef7.mp4?token=SUMWtA1jZ2EbSbkTxEeICrA7OIGUvayIue6TlObRksZwBJiWDlqso2PXc8HVj-UkGljHO-KsBAFm8o04WU63hbcxiSvKxSVSyfyxLQ9w0m8JBXR3VIsyXPyKvanrpSQpk2RxXv8HXtrPdTY7XNLcGONQIVp0nbrUzx-J9TPMauojKiIaEVSim5KBNX6xWT7KYE3xl7A2PX3FlS5MXAPbOJpuDx7I2GJcZrQy7OrVFJ8WJYN_dq-OCprsGhXmP3SiCTAnBgmFapFr8ES-ANmmc_vHT88F_2d-KLDUl6y8Nb7g35hLnN3OOD7uj1y--Wes-rX3SNJYMrLJuVvz1SHMOHcPXAvHHH9tV_Mdq3gOzx6eGi0hQD83Rhc6Nw03Dx9_HzpX00n-acOlWH8VJxUf1gluEWCK4K1e9_o4NHnjFk55Jh4QnozUDFLuvRZSdiWGDAhZNSpTJdxmq18TaFn9JHuzky_9sNrx--EJoQ2z9dsk9QvJD1thL-ASD6lk2TkuTbB7VQC86oR6po5huYrcfjJh9VyRz6BDa7yyOkM-hGPduudNChQP98qh2-0hwGoxm2AmS10sHtssFuoN816MuLsciksPcf5-nMJIbQRhCocgEpdPKlwZOLkQO0nnLapIDorZ9QA-2zeeZ0AJlgt7hG8ydU0vli3ij4nwDNFGdgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
قدرت نمایی رئیس جمهوری مغولستان با وزنه!
رئیس جمهوری ۵۸ ساله مغولستان، هنگام بازدید از یک واحد نظامی، ۱۰۰ کیلوگرم وزنه را به مدت ۲۰ تکرار پرس سینه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106116" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106115">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea95c3de.mp4?token=c3BZQI39-3dl3gkXv9odradvXTNYln3VRf28H83bA9pqh1Lw2r5gSYb5xw_RwqdyO6n3ei22IV0IpkGS5A1AubPD3yfguEYes7u9ULtPMJIxv4ReVrXHCVYiS0XW3z5NZyMxoQIigiPG-q36HjTkpZnX3WcF_b3_nZN4O58nl49KNMm_tKJvHlNA0jaTCvuCfIvK_Fde_OcgP0BYE-IOD9lUqXUEn5tzoSqt3b2u-24Smg3GIjHquWz2yJ3aUwSKmk_S9WICAp7GRYGH7duZ2o-LTUV2Gpt3Hpf8hfTXAiqGH6iGDMuhEEvCHYGajhb0fLDyE4mAoDB3jhwm9KRzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea95c3de.mp4?token=c3BZQI39-3dl3gkXv9odradvXTNYln3VRf28H83bA9pqh1Lw2r5gSYb5xw_RwqdyO6n3ei22IV0IpkGS5A1AubPD3yfguEYes7u9ULtPMJIxv4ReVrXHCVYiS0XW3z5NZyMxoQIigiPG-q36HjTkpZnX3WcF_b3_nZN4O58nl49KNMm_tKJvHlNA0jaTCvuCfIvK_Fde_OcgP0BYE-IOD9lUqXUEn5tzoSqt3b2u-24Smg3GIjHquWz2yJ3aUwSKmk_S9WICAp7GRYGH7duZ2o-LTUV2Gpt3Hpf8hfTXAiqGH6iGDMuhEEvCHYGajhb0fLDyE4mAoDB3jhwm9KRzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ایوب‌بوعدی در نخستین بازی سیتیزن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106115" target="_blank">📅 13:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106114">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
✅
🇮🇷
بیانیه باشگاه پرسپولیس: از سوی باشگاه ما هیچ درخواستی برای لغو بازی با خیبر خرم‌آباد وجود نداشته و آمادگی لازم برای تقابل با این تیم در روز یکشنبه را داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106114" target="_blank">📅 13:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106113">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da7a59d4f1.mp4?token=IKDCRfokeAJdY_qSwEA1S46jLCEzKx6GcIMrgt64RrJ0_xP5-TIwVEXbr_bqNp2wh2DMRpjSbP1H9TgkHHLsKDC9CElsybLuWDOE7NaYfUZY5fObLx3HaKDxy8XdFsRiTET2v25kNITS86EEX6DuytmXriZfn_GxYZHXi8EZb4KqF4NhhAi9oI3vybxbU1XK6GsYOSBE7rbyQ-2XUHpSM0EbxiEYsXw595U_YO7HRB63eZLtmFAlDZKxPSii7IY_z0ROZbWxH45qb0oJU4stzJLm3hQuOcyFlUYkBw85Cou0c0wpfch7MheYwj3j8eP-pXQcejeqiXhLpFOUX6a2a4yKnUeHuXlZykQjlfBTJ66bFKAchZDrhRMIFgJBUblW4jUguXx0iSegUyoawjD3mSFKMWs6khq7sduhJ0rN7Zs8qj2-8KiKNcZ4KTGT9TsFytWIkn1nO-cX2AZ49CjwSC9sjBrlRKzZE7UJ9FP8rh2oCXJzOeNfBGiNO3BR0WqqohTXq9OFDQ5xB8HgHX6Onn4Tan376VljRR6oPGmPGGksfjet04Vo4w3BfOf6aUtVHcrdh-kDvzdlxqN5EBC-dyUU1cuCTBsorIBpr7dQHDdQ7-JIg0GYyq8_gxYeZ64K0iwetFkDOiGurLjSTF9mZRIBgjgnX3autUNvZfvWiZ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da7a59d4f1.mp4?token=IKDCRfokeAJdY_qSwEA1S46jLCEzKx6GcIMrgt64RrJ0_xP5-TIwVEXbr_bqNp2wh2DMRpjSbP1H9TgkHHLsKDC9CElsybLuWDOE7NaYfUZY5fObLx3HaKDxy8XdFsRiTET2v25kNITS86EEX6DuytmXriZfn_GxYZHXi8EZb4KqF4NhhAi9oI3vybxbU1XK6GsYOSBE7rbyQ-2XUHpSM0EbxiEYsXw595U_YO7HRB63eZLtmFAlDZKxPSii7IY_z0ROZbWxH45qb0oJU4stzJLm3hQuOcyFlUYkBw85Cou0c0wpfch7MheYwj3j8eP-pXQcejeqiXhLpFOUX6a2a4yKnUeHuXlZykQjlfBTJ66bFKAchZDrhRMIFgJBUblW4jUguXx0iSegUyoawjD3mSFKMWs6khq7sduhJ0rN7Zs8qj2-8KiKNcZ4KTGT9TsFytWIkn1nO-cX2AZ49CjwSC9sjBrlRKzZE7UJ9FP8rh2oCXJzOeNfBGiNO3BR0WqqohTXq9OFDQ5xB8HgHX6Onn4Tan376VljRR6oPGmPGGksfjet04Vo4w3BfOf6aUtVHcrdh-kDvzdlxqN5EBC-dyUU1cuCTBsorIBpr7dQHDdQ7-JIg0GYyq8_gxYeZ64K0iwetFkDOiGurLjSTF9mZRIBgjgnX3autUNvZfvWiZ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
سرگیجه جذاب و سخت این‌فصل کارشناسان برای انتخاب مناسب‌ترین گزینه برای بردن توپ طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106113" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
⭕️
🇮🇷
با توجه به حضور سه بازیکن پرسپولیس در اردوی تیم‌ملی امید، احتمالا دیدار سرخ‌پوشان مقابل خیبر خرم‌آباد لغو خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106112" target="_blank">📅 12:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoJm19YRmHkNP-bFfhwus9GOnAR6uIp7vHpYAWQEtI_rmsxxOjrnPjFmmvvLU7p5hPlQKVSGUUY1cj7mOyOZNaI9R0SEXjxpuDk-7iyqPZXk6xOKuOcjphzMSnOIe_LlrYJHilisj_B4pd666gaV-si5oGOZOpDtZTzrGXEgo-Zqe9jCjTk6MpfYIn2e5H3RQW6gveT0EahqEu8qdU_3OFzrbRMMYg-1Z68-TuL29sWIgCCix1pgrWC12_9UZvQYo1htBVEyt0bL6R40QBau2nBO3rXq_AFlU_TgaPZSFegyil4NzWW-s7e06b3y1Irsu0JLDGSWXbZGeVpGKij1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⁉️
با پول پژو ۲۰۷ در ایران در کشورهای مختلف چه ماشینی میشه خرید؟
🇦🇪
امارات: لکسوس ۲۰۱۶ تا ۲۰۱۸
🇩🇪
آلمان: بی ام و سری ۳- ۲۰۱۵ تا ۲۰۱۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106111" target="_blank">📅 12:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
‼️
⚔️
کل‌کل و دعوای دیشب رودریگو دی پائول با روبرت لواندوفسکی در لیگ‌آمریکا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106110" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b9052ac6.mp4?token=p3E1CVlwgYKqPY5dCf7tLgAhs96yTlIRb9Usmu2grg9_RW8D3fWBkv00v9p97vnCRy0D7L56iRmU2bDmiMtq4S1MSLS4Go-B4Dwe16RiVpNDZtjfTyE8AugEoRcT3fTRWC3M9iFE1t1kLPIBBF86TDme8ehv-FD29R8GUcy5wTYBL_RavonrppeppV_RfMWssROBB6LEDx8Q3ACZx2MsZ6Kj_uYFcbFMUQ5crV0PRRD25WYftzgDEUS-WecoeSXTxtnsPz7ygtnmAEN4rjQk2Ae5FHI1_coynK5O_S7r3wb2pxcVUN-UAAWuXZhsdkMP7weRMHHJ_q4NFFFhfj8KPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b9052ac6.mp4?token=p3E1CVlwgYKqPY5dCf7tLgAhs96yTlIRb9Usmu2grg9_RW8D3fWBkv00v9p97vnCRy0D7L56iRmU2bDmiMtq4S1MSLS4Go-B4Dwe16RiVpNDZtjfTyE8AugEoRcT3fTRWC3M9iFE1t1kLPIBBF86TDme8ehv-FD29R8GUcy5wTYBL_RavonrppeppV_RfMWssROBB6LEDx8Q3ACZx2MsZ6Kj_uYFcbFMUQ5crV0PRRD25WYftzgDEUS-WecoeSXTxtnsPz7ygtnmAEN4rjQk2Ae5FHI1_coynK5O_S7r3wb2pxcVUN-UAAWuXZhsdkMP7weRMHHJ_q4NFFFhfj8KPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه‌سنگین مهدی مهدوی‌کیا ستاره سابق ایران در مصاحبه جدیدش به عادل فردوسی‌پور
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106109" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff5f3cdb2.mp4?token=bmZy8H-jfI2jiRnplCgtJcc4zPN1AgtxvquYwRc9H-G3KceNYRh0zi0bqAxRWug1DWSYersk79eCT98FLrr6Y1ywpu8toolGDQWIcM-ByTcFtlvxM6FjmuSOtVYZh_kP3ndEv7-L0GXjTMoYvt3skuAPpsyLdRu6jV7ILKZYvsicIhXqEo-Wh1ya4awrqLTEC2nwrSPf_GSkpWLaMwxETrq8mP0Wkfmh7GMI_uE_32-UXtAcot3h_Y-tN034BGkfS2dkX93IWMbMzGUD088wIKxku9rLLm3EgwitRT3zewInKcZSqlaP8ebYmtR1cz_dXqbAgLtj18vt-lH7R-pqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff5f3cdb2.mp4?token=bmZy8H-jfI2jiRnplCgtJcc4zPN1AgtxvquYwRc9H-G3KceNYRh0zi0bqAxRWug1DWSYersk79eCT98FLrr6Y1ywpu8toolGDQWIcM-ByTcFtlvxM6FjmuSOtVYZh_kP3ndEv7-L0GXjTMoYvt3skuAPpsyLdRu6jV7ILKZYvsicIhXqEo-Wh1ya4awrqLTEC2nwrSPf_GSkpWLaMwxETrq8mP0Wkfmh7GMI_uE_32-UXtAcot3h_Y-tN034BGkfS2dkX93IWMbMzGUD088wIKxku9rLLm3EgwitRT3zewInKcZSqlaP8ebYmtR1cz_dXqbAgLtj18vt-lH7R-pqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
لواندوفسکی بعد جدا شدن از بارسلونا تو لیگ آمریکا هم هربازی داره گل‌میزنه و چه گلایی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106108" target="_blank">📅 11:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9d287e7a.mp4?token=IFduUZZCl2CqneGi1JdHqpGpD7mzZQnhqekH6k0rfJ_-VaQPXalAH-3HAE3H70Gp2HBgvt4IVX7pvYmSWBldAedSuNZeVH1fiUZ3htnOwrR_A1rtb-PomiG4Fuais-YsFxH7aUTQ8MsE3hbFmMfTTbmJwozR1hb7XCnzE2bm2y6naIho1NqnD59sMAwoVbkZIy2VIvaIPRcK612sDp4cerRHztq-iDfKCcT7XIXbLsAaJXtoWWycM6ior2Vw1Wi5sZpuLNadJiPjzEbsDFi79T5oQw2OtUEybYymMQGGk_w2E0hocCSar6pWNV4T_qeukUW_JX1zb4glTbkdPXXdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9d287e7a.mp4?token=IFduUZZCl2CqneGi1JdHqpGpD7mzZQnhqekH6k0rfJ_-VaQPXalAH-3HAE3H70Gp2HBgvt4IVX7pvYmSWBldAedSuNZeVH1fiUZ3htnOwrR_A1rtb-PomiG4Fuais-YsFxH7aUTQ8MsE3hbFmMfTTbmJwozR1hb7XCnzE2bm2y6naIho1NqnD59sMAwoVbkZIy2VIvaIPRcK612sDp4cerRHztq-iDfKCcT7XIXbLsAaJXtoWWycM6ior2Vw1Wi5sZpuLNadJiPjzEbsDFi79T5oQw2OtUEybYymMQGGk_w2E0hocCSar6pWNV4T_qeukUW_JX1zb4glTbkdPXXdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شفاف‌سازی عادل فردوسی‌پور از ویدیو جنجالی که به بوسیدن دست وزیر مرتبط بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106107" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106106">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106106" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106106" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106105">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kH-FTisxAvRFFog1sj5LXmkgsYBdluoZFZXhrf_mdIEpGn-nQF70_lsn4GgBGNzLrvwusfRoLC5bZ3WLmd2Mab4Nu638ShoEyqRsULXzkUUujv3HrJt6o_iSezbzh5erpct0oF6C6yACUr9tqERqC8gQ691Yc53Dm69jgJkKixyvinjt6uOuNI5k1UGXF67DCZttqTRtttDcZUdfRlL9gqtAWOwjnQDSO-JKO8y6aNPQ41K9GTHBvJGkjUQnwAhmsrzaLq31fFeR89HksOeE86UBfusOZYYYwYiQ2CVV2V07i4_Ct3lUzMvx9yuw3sGKRSlfO8qafReJb93WuPPoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106105" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLxwI_yXy3m99rYEGf8aVkb_F6YTNW_OBGn_aZ4w17yRYt3Lv6qyo3zc3Jb0ZzKoJdtjNI_FKghP7gJTjoGQmBXotG8IgVU6qrBmLmOMUeSDF95-nuozEkfEP-its517Vsa95r1FIp23Qh3smrwYPFVDnVMDpN6Im5LMeMcZNsZ5uD5-iRzYP4qsrKXNN8Slo-u-cHR6K0fMbNMHY1jzCnPDk-eSw7Lh00v1rVN9ZLCf5As61AypSjobhozfwNKnQxgM7f5zxRopAXNTa5G5LrlVZp55Wzy2Zvh1nriM8v4Po7VE8PuV88pmG0BcsDrsZuwwXcdJHe6K1_3NQbxz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم‌منتخب غایبان لیست توپ‌طلا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106104" target="_blank">📅 11:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106103">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1619d9ae.mp4?token=i2SxrrSaqcFTOOTCNIRMZLE-bEI9P4VAyn_lk-B8zaVvATZIYKo1uDRjGWCzYLwprn28-vpP_KjUkIk97rPMuUrGTUGqYau2g0lWzKkad50fJ-2eyylzfEHFqpWH5wZCAF9VMEV2ocW5OHKu2ldFuF72BI2tSG3Wa0BJbas-ojUe9hs_iZGACV0XR8cjOPijmFCVpKXoCKDfTrYuPFxi1hVNkgOusbBvlMa25Fs2Wh8wY4tNW6f0_vVvSp1Wr61jD9hEBTKbBJTYlfqlCx3Ajhb1f1eEir41WKRua1RzFJyfL35H4E-Fsg-NdBxUq1z28M9w7y2uJckST2TCHsh7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1619d9ae.mp4?token=i2SxrrSaqcFTOOTCNIRMZLE-bEI9P4VAyn_lk-B8zaVvATZIYKo1uDRjGWCzYLwprn28-vpP_KjUkIk97rPMuUrGTUGqYau2g0lWzKkad50fJ-2eyylzfEHFqpWH5wZCAF9VMEV2ocW5OHKu2ldFuF72BI2tSG3Wa0BJbas-ojUe9hs_iZGACV0XR8cjOPijmFCVpKXoCKDfTrYuPFxi1hVNkgOusbBvlMa25Fs2Wh8wY4tNW6f0_vVvSp1Wr61jD9hEBTKbBJTYlfqlCx3Ajhb1f1eEir41WKRua1RzFJyfL35H4E-Fsg-NdBxUq1z28M9w7y2uJckST2TCHsh7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
رکورد لیفت دنیا شکسته شد...
۵۱۱ کیلو رکورد از یک جوان ۲۰ ساله مکزیکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106103" target="_blank">📅 10:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106102">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef0e259b6.mp4?token=jg326kHN3hWl6i7m_4SRucNBnbqPA_oGx0LgS0ayK-m0xpNx8OEkvw5yvIDiJlgNxEYD-tc_asJbe33pvkVOItj5fHUtOUHg_mSM0FjaM6PCL2QNGQwQkwRi1lhkgGSzCfMjKpYwsQEo5tmoUi9hWY5IrSTVtT7IgH-g_u_2z5qNQl43WUsJZgGk7uV7cohlImxvMYW9iamVtS9fn1knmNKfdH6WahWi18pExs7KcuTc85qYnydXCg8d8k_n7ZQQIQYMrkwTh7P3_s8bxyOTvTeSnjNVwygQoRqWqYwT0weSdEYgd-tWqZrFS0Ht0yY_0SQhOD3CaF8EZo5UWsYpSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef0e259b6.mp4?token=jg326kHN3hWl6i7m_4SRucNBnbqPA_oGx0LgS0ayK-m0xpNx8OEkvw5yvIDiJlgNxEYD-tc_asJbe33pvkVOItj5fHUtOUHg_mSM0FjaM6PCL2QNGQwQkwRi1lhkgGSzCfMjKpYwsQEo5tmoUi9hWY5IrSTVtT7IgH-g_u_2z5qNQl43WUsJZgGk7uV7cohlImxvMYW9iamVtS9fn1knmNKfdH6WahWi18pExs7KcuTc85qYnydXCg8d8k_n7ZQQIQYMrkwTh7P3_s8bxyOTvTeSnjNVwygQoRqWqYwT0weSdEYgd-tWqZrFS0Ht0yY_0SQhOD3CaF8EZo5UWsYpSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔻
🎙
ماجرای ازدواج محمد پروین با آناهیتا درگاهی عمه دنیس‌درگاهی مهاجم تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106102" target="_blank">📅 10:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106101">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9e4c6ba5.mp4?token=ghgSu6MMdC31RoZvLmzN0lOXUjiS7ilFKK276RurSL2pxrOKyr-LnnhMi380wZzrTjFymsfSgG_msb_EDuQhilfLhTej2G6Bt6uoeaUkelwxKZjbvgC-phgkpiuOpZh6l9FYtqnkntTH5niUNM5h1LKnnTzcZnPAFRQ3W0TyHIXp8uLRdpRe0d6v_65SxYSk0RGHGjpzJMqZvWificlvUTx8ibTbbo_q-Ex6Jiz44wl0tDcp4WYxP0K0cQAh7lmV9r0ZPE7Y3fRmU9F3NJ1lcr5KIXeQaTUQKF3Jtvx1jTBVzw9Lslp2c-S7Da4_0XuVv1-3WWGg4UkquB9zmlTOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9e4c6ba5.mp4?token=ghgSu6MMdC31RoZvLmzN0lOXUjiS7ilFKK276RurSL2pxrOKyr-LnnhMi380wZzrTjFymsfSgG_msb_EDuQhilfLhTej2G6Bt6uoeaUkelwxKZjbvgC-phgkpiuOpZh6l9FYtqnkntTH5niUNM5h1LKnnTzcZnPAFRQ3W0TyHIXp8uLRdpRe0d6v_65SxYSk0RGHGjpzJMqZvWificlvUTx8ibTbbo_q-Ex6Jiz44wl0tDcp4WYxP0K0cQAh7lmV9r0ZPE7Y3fRmU9F3NJ1lcr5KIXeQaTUQKF3Jtvx1jTBVzw9Lslp2c-S7Da4_0XuVv1-3WWGg4UkquB9zmlTOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
ریما رامین‌‌فر بازیگر معروف سریال پایتخت و پسرش روی فرش‌قرمز جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106101" target="_blank">📅 10:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106100">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710d093c91.mp4?token=ucYdQAIUAGvOKNF-keOPpOH3sPPPF5eY89JhE2JWxMBAKtOqX7xWfyIGaEjJh5TGH1NBsO7bWKa4aMp1kwvqkbCsDY-cnDnIZwJ0yznE6tfMMsltbx-L0ZvMx-uyT2PtnQ43puF1_p4Etk7ZwpL0fnbgxRlfK7IMAQCkyuMR0_KbelN78Vz16Em4aMQ27q31sOL7svWwvEs8Bw_i3vECidpg__b9KH5TyXio4_sflnmr8e1XbyXXdq7QlalmyxHRDZq4EBehf-tx9Z7en1Z5i247ySQ7G3W4_0YXAW1ZBtaaJ99zNzz2yuUg6UW2obp0S2SHHmDRBCbUrCuZWlNtFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710d093c91.mp4?token=ucYdQAIUAGvOKNF-keOPpOH3sPPPF5eY89JhE2JWxMBAKtOqX7xWfyIGaEjJh5TGH1NBsO7bWKa4aMp1kwvqkbCsDY-cnDnIZwJ0yznE6tfMMsltbx-L0ZvMx-uyT2PtnQ43puF1_p4Etk7ZwpL0fnbgxRlfK7IMAQCkyuMR0_KbelN78Vz16Em4aMQ27q31sOL7svWwvEs8Bw_i3vECidpg__b9KH5TyXio4_sflnmr8e1XbyXXdq7QlalmyxHRDZq4EBehf-tx9Z7en1Z5i247ySQ7G3W4_0YXAW1ZBtaaJ99zNzz2yuUg6UW2obp0S2SHHmDRBCbUrCuZWlNtFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
هوادار جذاب و خوشکل تیم فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106100" target="_blank">📅 09:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106099">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=gXFuuqoHoaQ8b9qFBgZkO_cT21DP2AYfaJ3Jgu6fld4xwlP4S9U4yrheelCPOIi1mvVQkL_6om0bvZaqZd_V2c2Rsb1eDUOMgIHAgM5D2-NZqnQgzv4Nf-MaKfI_AA1_qswvOlJzNI7pyQjZbqax7flRgDM18_hOK7mELm9cBuU3EUcVdqQeI9HkIrYw30GjNHRboN5B7DWkcluicljrSLqhVczia6kgc3uMWMLoHgMHM-R6lHMtVhCnhALIyEpGN6dMF438VMF1UZ762z9IrwLbVbaFYJ0io5ZjRQJr42MvRJ_PXzLrAOUyf6VA0DUaFA1fVY4i7gn9smc-26FsIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=gXFuuqoHoaQ8b9qFBgZkO_cT21DP2AYfaJ3Jgu6fld4xwlP4S9U4yrheelCPOIi1mvVQkL_6om0bvZaqZd_V2c2Rsb1eDUOMgIHAgM5D2-NZqnQgzv4Nf-MaKfI_AA1_qswvOlJzNI7pyQjZbqax7flRgDM18_hOK7mELm9cBuU3EUcVdqQeI9HkIrYw30GjNHRboN5B7DWkcluicljrSLqhVczia6kgc3uMWMLoHgMHM-R6lHMtVhCnhALIyEpGN6dMF438VMF1UZ762z9IrwLbVbaFYJ0io5ZjRQJr42MvRJ_PXzLrAOUyf6VA0DUaFA1fVY4i7gn9smc-26FsIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
داماد سابق علی پروین: بعد ۶ سال جدایی هنوز لادن پروین رو دوست دارم!
🔻
لادن پروین رو خیلی دوست داشتم الانم خیلی دوسش دارم. لادن سوگلی خانواده‌ بود، دليل طلاقمون قماربازی من بود. چندین فرش ابریشم زیرپامون رو تو این راه به فنا دادم و ماشین بی‌ام‌و که داشتم رفت.. لادن هیج تقصری نداشت خودم مقصر اصلی این جدایی بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106099" target="_blank">📅 09:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106098">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=bNx7n9oMRoVn8oHFukZ5xhsEwi8AH5Ed6LaKhbjxmMLnNMB6xyvZ5e3txQ8STGAz4RlutYlp53OkYNeuq2yfZZwPlTck_swHelhF2UF9LI_20_673A3oImXFYzDzennt2XFXmDAkucAvjE-EZ8W1If0TUhhVYQAOWjt6uftNTqUyV09uAdEC9UWHvyO9m2zQ8LNNqWOhJfwOLJS63_LYZH_hAclesixGbDThAcDyLLFlUZN1fgLjR2GwNFJxUolqtFF9CQVkiW-czvkdx3u60TzG7F2NjOVUjxqe0EE7mG-3DbE35LRpF6tGfaup5ODyz8JwlHlTLsjVyK2Nsbz05A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=bNx7n9oMRoVn8oHFukZ5xhsEwi8AH5Ed6LaKhbjxmMLnNMB6xyvZ5e3txQ8STGAz4RlutYlp53OkYNeuq2yfZZwPlTck_swHelhF2UF9LI_20_673A3oImXFYzDzennt2XFXmDAkucAvjE-EZ8W1If0TUhhVYQAOWjt6uftNTqUyV09uAdEC9UWHvyO9m2zQ8LNNqWOhJfwOLJS63_LYZH_hAclesixGbDThAcDyLLFlUZN1fgLjR2GwNFJxUolqtFF9CQVkiW-czvkdx3u60TzG7F2NjOVUjxqe0EE7mG-3DbE35LRpF6tGfaup5ODyz8JwlHlTLsjVyK2Nsbz05A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇷
🇮🇷
بدشانسی دختر کوچولوی یزدی در حاشیه بازی چادرملو مقابل شمس‌آذر قزوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106098" target="_blank">📅 09:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJcoo5XZNUH5lM38GQ75ykRXXN6InkcK1poGY3bmMbWpw6i7SH9YEOjDEDL4NbVBNxApLACQtCIwJGeGwbH9GDKvu5YIj-TykQTi0F9pcXd_NBw0hYrPKvg3tM2V_vm004W66icKnp35JI1O9inYiA4ZDv6SnHD_Mbp7GbpBISHVgh0nm87BSPSylzHSOgLmm3i1h9ZY4ras--7p_ttNOjH6p2BcInOPo1SKS5auROV0RNYe__Hxp6PQ6tats5t0Ao4t_sBnCp30A2gXYDy0ZKjyZnlrAHc4DoOUTC4_ZpgMx5vy83TUYNhMBddKhzAmUi4v6iXl1KyCoDUYF56TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cI5sPeEAZlf98ZQLWcwS_OTczQp2TUC-tCVEGowCcxz7Y8hfrzALERUVkirrCH7piVTYSKu26C_3YhO8ihcKmkHQg3e5HAjZ8IcQDRX4tvHFiIk0rFu5491HP0sQkNJOC-D9sKyo96u2W32bhqh_2YZVJmpAjmH_l-ECMpIM1FA1BhGE14-is7R52ly0QP1vmv1w3_nwuL3pjiUVpYOdDnNj6PFyVLM9JSVP0wre8XU8ysG8fXbhmylAhhQWKywrGdxarEn9B43yHARBGhuQWd92e8LZTHCnPYCTJc2PXpczvyCvwP3HUWCVn_rNWE4gvHLOZLn7VT4Ak0LWrXvpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVRtdcBmR5aUi5adui78a2E_V3PpgxZHSzzfWvdeJmEXwBb5lKjtIYSEppqMPwaSMU0HixJZxNbSMMkNiPt76p5ulryb9nX9Eob7Xo8iDPYYzAgR-r5xP_8qsxVzOt9kbrgj5NUj5Gllicxfcf1rDRnA4g5APnC4lEXHj7ZFitseF6qI5uCqfmLpZMfvR9JP1Fr_NiQh3lnUpLD0MkLOWJHJWzRB9bA5-zoW9MtNQTaHr3UV5J4BqVUPRmnG_GCPF4Vbk5hPj4pl4rRe9c9OVJ7WCRNdRY9Rf7c6e-wLlykihowIncqFIpG_AtcJAgigyXG_E_ti0Csl3o-1IkpZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhjawElXlBxjq5GTRixBen5NfRYY78SJ-Ch-IEHHW_BfHDYvOPajF9xrTw87wM4Ooj9Pd1a6DwPhzMhSXsyRsvtkrDd87jv9be1421DGcRVvWWt6X8uzupvKiHfNksgUkbhJsEyHtCZTjPjXTv04wfGG3DOeABfYrgc_9UTDdQIoTwKJEhZQVdpB-Pz8ph2j5JRSIJHmmAm5I8v0hmCx6_6ONptYKOA6Mz0j8c01AIFm6ShPca2FcAe9NOw5OMnbdH9jZ26Bkn5QB7chUTohKDGg3-6wR1MoJ26l1pb8CofKUxgW5DUQpdB0TWAKFelYhfqCvTvMdtczQEAO94QWtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
دختر پرسپولیسی حاضر در بازی ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106094" target="_blank">📅 08:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/970c991132.mp4?token=gG7zYF5p0-cKyetjo2mI1vkI9kDi5Hv_RGVuUhlEJofaplRvMayWRBYTI4peQUqK7fDMD-P1xPMmTpe3t7RHcJOy1GOtX-FKtZDzxXCEiCGTAX9XVW91BeXZilpJx0W0zVMKfvZ2HDkaxE1Um5Uj8UnGCZyPFS3uhR7UssTC2urN2AR-1dZ-EScZ35GP0GO2-fJCQa-S89ZYO2UGCRrabOQNZH5951gb_hLBTEwKxvJusywFVUBZtB_HJrSB2TwggD3iqhmwW6r-sNKNERqyhgkJ8WjRdnDWZ2kQxhL9BXO64-sVMzs0sYruMV-InUFw2lKcfaMJPOZL6BwvgCf4RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/970c991132.mp4?token=gG7zYF5p0-cKyetjo2mI1vkI9kDi5Hv_RGVuUhlEJofaplRvMayWRBYTI4peQUqK7fDMD-P1xPMmTpe3t7RHcJOy1GOtX-FKtZDzxXCEiCGTAX9XVW91BeXZilpJx0W0zVMKfvZ2HDkaxE1Um5Uj8UnGCZyPFS3uhR7UssTC2urN2AR-1dZ-EScZ35GP0GO2-fJCQa-S89ZYO2UGCRrabOQNZH5951gb_hLBTEwKxvJusywFVUBZtB_HJrSB2TwggD3iqhmwW6r-sNKNERqyhgkJ8WjRdnDWZ2kQxhL9BXO64-sVMzs0sYruMV-InUFw2lKcfaMJPOZL6BwvgCf4RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤔
🖤
ایرانی بیا که یه حسرت جدید به حسرت‌های بیشمار زندگیمون اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106090" target="_blank">📅 01:21 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
