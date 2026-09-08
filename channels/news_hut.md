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
<img src="https://cdn4.telesco.pe/file/afKLmoGvCp62j475DquBz5TFPkWJ3Ds62RT2JbG7yiCwIjyBGedNI4i2lh1-Ne5nNUvDYXHaUgFrCg-LE11o6X4hSzA32PABk9XG16L_UK0NlXWv7z2WniEpZqGUUv4is-EOfchDBmt46PgpBNXknUmNeyRhv_tNGQiwq3i1jlSVl8f0uAqjogfzje299xUj7Yk7YVOg1EpiENK_fEeQUOjUhnyl3oFscU41Nbe1jQzqlty4tBj_CTKKuaSEyX7YpPBKTljDf4IeCY8CnDTEtxS52sSjNl-bfQfc-2SniAnY2SRzjlnNe9hpy1WwBaSJTm00daFGuqEm7eSO3K-exA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 02:34:10</div>
<hr>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy50Hoa68qEdZP_QneeoJXMdNCyr0Sa-hp01vyxxySdO8eK4c9D020V8sdxeZFyyC2g7im4oybiafMfXaISuxDTKYZMXx0URGnrvV3bYWime4Wf1Jr-d7UFYdPfPO0Dm5h4hs_APcLnG1R-cQPh9b4iK9kdOi31kc-KAPIGncKp2RT9_4hWCWFQM86CNmAWl57yanVYLhstt5hFtDnmGTU-FTx4oUjDnntRS-99nNHpDHQUgtt0TyND14jX6bcfMgsMNAQ0zfBRFn-f3s6mLfk1UxLQvaKwId15iuwYHvuZ2itlJAX5Ue9sjGgV1sXJGYVGcFnFEWdDbohIa0Y4JtQ.jpg" alt="photo" loading="lazy"/></div>
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
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
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
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=WMOcQwCpLpDXddi6Q_8FVBM8VDnyLEgx65rOBWZHdEaK392Uds-QX44ZxSyP6KGKYjoTJVkeyq0p29mE1TJpJeiBlTF6DLBv_CYO71vK6n1OBJt7FbuGmE4TOuUNKjBh235k2KO4VhlZd8OPtE0up4lqkZYQzCLJqeShxen2yTOugxPjdxlBGL1B9mSG-wIqvy5mTKunsYenmrK2pcod0H94kjVRgDV6cloroX6vLNeo1zuvVbljMrEEn5yh0UqC96dDMCKZfNCjhPrnVkbo9RqJjPguRA7xBrPzzEdr3IN4BYqoTOzMQfOZ9E6U0tQsSlnq1X08KrmiLnXfVNZQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=WMOcQwCpLpDXddi6Q_8FVBM8VDnyLEgx65rOBWZHdEaK392Uds-QX44ZxSyP6KGKYjoTJVkeyq0p29mE1TJpJeiBlTF6DLBv_CYO71vK6n1OBJt7FbuGmE4TOuUNKjBh235k2KO4VhlZd8OPtE0up4lqkZYQzCLJqeShxen2yTOugxPjdxlBGL1B9mSG-wIqvy5mTKunsYenmrK2pcod0H94kjVRgDV6cloroX6vLNeo1zuvVbljMrEEn5yh0UqC96dDMCKZfNCjhPrnVkbo9RqJjPguRA7xBrPzzEdr3IN4BYqoTOzMQfOZ9E6U0tQsSlnq1X08KrmiLnXfVNZQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=A76uDy0z1RtkyFJSxYnJUP6VzICR2IKpQAHJx2DgnNKb8JMeLjndHT9gRsRWN2yrbch6B_HMxp02I0oZ1O2GMaIScNpJuKdTuRrU6sCYUIbNTBG8lvLf3Uq0Jlk3IHNi0U9Zphztf22o8w2lyLNoTfTbNK1DET30B5eHGoOIPS54uGg98WOm4E62UQTSmL_8SZD5U1p4utb_i7lhojlCOxiLL66HWV1_ZpqBPSfFRwVuTXV43_RFq48mN3T46ZJnQwlqt8Xb_noCi9OtW7WccYbqbuu8iNZnpxoS7KNFvVrmkPzxMbVW7-hZ3J8MajOxLL_roQxlrbdnEjUmCwCQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=A76uDy0z1RtkyFJSxYnJUP6VzICR2IKpQAHJx2DgnNKb8JMeLjndHT9gRsRWN2yrbch6B_HMxp02I0oZ1O2GMaIScNpJuKdTuRrU6sCYUIbNTBG8lvLf3Uq0Jlk3IHNi0U9Zphztf22o8w2lyLNoTfTbNK1DET30B5eHGoOIPS54uGg98WOm4E62UQTSmL_8SZD5U1p4utb_i7lhojlCOxiLL66HWV1_ZpqBPSfFRwVuTXV43_RFq48mN3T46ZJnQwlqt8Xb_noCi9OtW7WccYbqbuu8iNZnpxoS7KNFvVrmkPzxMbVW7-hZ3J8MajOxLL_roQxlrbdnEjUmCwCQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=bA3cvvVRdqvYpRkqws9g9G261bcE_ONqznXwXR1aERyai5bHQ28udYTwkPHW8qrsN1m9ewkbY1HGSLbbG-4kRs5HpxPCz0v6Eyxn5Z181TPZ2yWt3FJYu5kzM1Po9afp08f60DTUkrjdlau0F1V3phqSFWQONRXbDmHFJiva5O-OyUIttkczXM6ufu_FveIPLJnKTsqcfYBiuD3Q2cZ1z50tc6hKRrRv3t-9Uv6Gh_0jdxQi36PWHj7ExrOTrdyd-4q5SFFnrR8_VOl74j4c1z74mqieNKbIik-jqLnjU6kofyfhtBU1erQsDhPWveqIjEKOy8J4urOnhiROiuKfOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=bA3cvvVRdqvYpRkqws9g9G261bcE_ONqznXwXR1aERyai5bHQ28udYTwkPHW8qrsN1m9ewkbY1HGSLbbG-4kRs5HpxPCz0v6Eyxn5Z181TPZ2yWt3FJYu5kzM1Po9afp08f60DTUkrjdlau0F1V3phqSFWQONRXbDmHFJiva5O-OyUIttkczXM6ufu_FveIPLJnKTsqcfYBiuD3Q2cZ1z50tc6hKRrRv3t-9Uv6Gh_0jdxQi36PWHj7ExrOTrdyd-4q5SFFnrR8_VOl74j4c1z74mqieNKbIik-jqLnjU6kofyfhtBU1erQsDhPWveqIjEKOy8J4urOnhiROiuKfOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=vwnSWdb7yEuEB_6blcbRgkqeat7bEtp3UgrDHQ6t03n77_dBtnTalllz5bxJA0wuLAnuJCT_f5sMz-QW1FJOYr1U3wUwyD0cicbtdWpxhcY9E-TNpKV8WChdLbEBd5DYJWFgGa_VLRahuLQSOKWP_lFco2h15BblGqrPgEVsrImcVPpG7N_gqFvQ98gRXq8EZ2K6HaRAtgcGeEX8EeN3QsKqXzQhSlw_KiT3K9XP299fGEgCdMlnCbZssFJD2OQiYPSWe1Zb67AlVjOk22JW_XPgn4PghAAU-6ucBdMloZPDSXaxWfH9_1pWVkzNX1Ji7XZYPu-VONfl7G7cN5Z73g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=vwnSWdb7yEuEB_6blcbRgkqeat7bEtp3UgrDHQ6t03n77_dBtnTalllz5bxJA0wuLAnuJCT_f5sMz-QW1FJOYr1U3wUwyD0cicbtdWpxhcY9E-TNpKV8WChdLbEBd5DYJWFgGa_VLRahuLQSOKWP_lFco2h15BblGqrPgEVsrImcVPpG7N_gqFvQ98gRXq8EZ2K6HaRAtgcGeEX8EeN3QsKqXzQhSlw_KiT3K9XP299fGEgCdMlnCbZssFJD2OQiYPSWe1Zb67AlVjOk22JW_XPgn4PghAAU-6ucBdMloZPDSXaxWfH9_1pWVkzNX1Ji7XZYPu-VONfl7G7cN5Z73g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ICRuvu2qkKT162ZrPAUcwxMHLyHDkumJRMZ9VkIJ_1kyAySa622O-NTjLAsqPwwUw7TmeBNR5VsNALqIr7MlCSqkVk9JzLF9ff-1y3fZjWRm5gOGhbb7XzlSt-HttVesFZ_AcVP9Uokl2Na6PhkwmcPVShE1FCAII7RrZkf_f-aDhsyJXYrTGpg6b4S_mGBTfcefG_DRYrhzFrWtqX8Bp5q_H77NhDN1fnOji5ZUBAnIdfvigV5WNg7Gu1SZXw6sbnEdZgDqfUqdMM_sxZ0vv_pxMO6cC_vuZCf2s_8-LyeeeAqdh_JG9ua9BGt_4qqPFy9mTMLXEj32dIp2eW4fkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ICRuvu2qkKT162ZrPAUcwxMHLyHDkumJRMZ9VkIJ_1kyAySa622O-NTjLAsqPwwUw7TmeBNR5VsNALqIr7MlCSqkVk9JzLF9ff-1y3fZjWRm5gOGhbb7XzlSt-HttVesFZ_AcVP9Uokl2Na6PhkwmcPVShE1FCAII7RrZkf_f-aDhsyJXYrTGpg6b4S_mGBTfcefG_DRYrhzFrWtqX8Bp5q_H77NhDN1fnOji5ZUBAnIdfvigV5WNg7Gu1SZXw6sbnEdZgDqfUqdMM_sxZ0vv_pxMO6cC_vuZCf2s_8-LyeeeAqdh_JG9ua9BGt_4qqPFy9mTMLXEj32dIp2eW4fkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNhyAOsDvxMGdqNzHfhvyrXpvF6qKvuuCdo8qB0bG4jgiSQs2FMFkNjkjRSfkOU0fT3H0otikGL86zKRG_tKZMIH7KojBk01anriaRszWrD9Vhehsg8gBh0giAaWbh1sacoWdGYlR6TXQviuPUhJhKvwxgbtGvYe8nZNqYWqmrAxXcNDWw5eQjE52zKldCji1NZ00AS-GGp-Nx3lRR1cv2HQhPbhkRMUvmFGxwBQ44ifZ-oOnc39SdUTdzbCz8ql7UNY3VIxyYe0V7tsqwvIpSt45Mfod_bcHjFeGuJCylnEHrfKAsrIEqSWYv0hTR-ql6NB2kjaZL1b6uqMrluhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=fuTQ1rr3XbGv50g2RqCRBCNkEvU1zwGIJwwWkNF--9cbIbwpi0Z_bPi1CVuSTL6NdJskCmdiEx9Q7V5gFPZc9PNEckzvAismU52Qpgv0Gu481cYL7XyXyDkMWBOF-s07x-m0DVz2qBG1YRGXemA7Yoo9iTpP_QLKwRjE4Vk8GS7tMLtV2lsyQcl41RV_yNrcMNAAR1_PpIhIb9ZasJdT6CNGxaaGrl74gfFGv9vMiCMzGg3Ma0G-PlP-UjaVbaOrnOiU5-3Lbl1wDH60GzM8j7RFUArr2VXgH61JMLY764qWgNhAFahYnDCLXlBR3sbazdiajYczDnFLDARwmKAMJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=fuTQ1rr3XbGv50g2RqCRBCNkEvU1zwGIJwwWkNF--9cbIbwpi0Z_bPi1CVuSTL6NdJskCmdiEx9Q7V5gFPZc9PNEckzvAismU52Qpgv0Gu481cYL7XyXyDkMWBOF-s07x-m0DVz2qBG1YRGXemA7Yoo9iTpP_QLKwRjE4Vk8GS7tMLtV2lsyQcl41RV_yNrcMNAAR1_PpIhIb9ZasJdT6CNGxaaGrl74gfFGv9vMiCMzGg3Ma0G-PlP-UjaVbaOrnOiU5-3Lbl1wDH60GzM8j7RFUArr2VXgH61JMLY764qWgNhAFahYnDCLXlBR3sbazdiajYczDnFLDARwmKAMJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=KjzpeEW68bOa9aR_0Q3BddXIybZhYrJ4-y1OI8g1EYOAmqrkxJsZ-7211NjZrG1PIudbNbJ8FPWnRcn2Bgw1SviA1ukJxqrKPYo3bFhs4uFde2DgumT2N7m7ENKNqgAxOJ84O92kHQGCNFx1An_96qoKoS8bC0ftyD6iPLxFw2Ui7Qsay6p39Ieva3_oUCyadGY5dHfmYG4xmEmjAmnqI5Z1HKjdEveu1g2Mrmk0950A5ocbvJSDLsNTdjRGvSNqcKkcxqzQUQOLNA7V7uEOOaKHcp0y3HrTTSbyq2M6dOiaMkDp2hM5U4Ri6o6dZ9eDpFB4kd9pZrr6lkhEDmp7cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=KjzpeEW68bOa9aR_0Q3BddXIybZhYrJ4-y1OI8g1EYOAmqrkxJsZ-7211NjZrG1PIudbNbJ8FPWnRcn2Bgw1SviA1ukJxqrKPYo3bFhs4uFde2DgumT2N7m7ENKNqgAxOJ84O92kHQGCNFx1An_96qoKoS8bC0ftyD6iPLxFw2Ui7Qsay6p39Ieva3_oUCyadGY5dHfmYG4xmEmjAmnqI5Z1HKjdEveu1g2Mrmk0950A5ocbvJSDLsNTdjRGvSNqcKkcxqzQUQOLNA7V7uEOOaKHcp0y3HrTTSbyq2M6dOiaMkDp2hM5U4Ri6o6dZ9eDpFB4kd9pZrr6lkhEDmp7cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jou6V5-yXQMYPBoli3xRlN2yjtb_UY5nXtOLBxYpjp5CCYbFQgpSRoToYLRd9QvFLXUxq-5Bz0aUHRixRGhjLznY8mWme8nSvpcT2HaQ1shepV0Wa6yc6B5BwcRyH-oy7DO84ivVBeuXKqVOh0Nki0LLBoaGDD5yN8GmZsjAIn4d0yDAVgdkPWVYeTLCo14-LSLniipIWC3YIaD3J_aTHmrDj69erxEzI4iLe25HsBdhW9W6Sp1JXIfMYcPY2J16ibNUurZWs932ZVU16uSlQ7isdqK15IHGsbDp0ET1Y3iweHUSbjWxuN32QWJXSP_UDX_twaOKFNLrydihaMU_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns60rbe9LMzHg6VpeexSkf1aoxcNgg1cDT-n-jJn6MccGwsUSzxUoC8OVJXh2o8IFEou9jsSRGKKKENltRyxrIJxvCoMFn5JZxnFCMs46Xum0Xd7PCUc69JyyPju-4RSBVtnX9q-J7DJFVp4daSWQGGY68OB5wFXJTiDwRk1WmtcJ6GeG99GnidGgnewV5gMXjExj5tIW1H_II8VhDy0AJDdcKlGBFuuko2J0heKWmDBKlYzbF3W3psIB-AhsdBh7fo49moQLo4r_W4_vIQrF0UjQyAryKcaUue8yXfGhi5Q7TFsv8bAywLME4h2LKKUenrex_3uM7gXnKfJQAbNbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT9G5EODA4jPGbzme6hIdYpseARtT6_-sn93ciaUliDF7jFIwZ_AJxDXTSVshb-dQ4Xpep-Ujzh8elT-4qQI3qzPi6Gj5ynVhtXXPwU_-H7yOmnN6M7CBFY1LWkyywtQ-0Bys-053YVcrlqv1FJlcmYRhncWo_Snq5HFtmEEQHrsT_O0DDNStgw21mRbUsci5S9iRxq5v1SatgnPi74eOn3p261AdiuAV3vLhaY8FOYVWHrTs3o1CsNVsP3y60kfQKqWUViQQKGpBlQ_qTKaBbRvTpoLUFjAJvVKwgaj2GlWbDEaTdRbyy5V62kc_VtrrLI2kC8Y9MUGz3OCV7G4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geq3I5_4Nyre5KSG9BjJZVoAyN4hAuJkw3O3XQe8aRIoPNQvM4Aufv6F52Xlvm9kCBQAgESnP3LVOYzgO3L6S5z9BoACX7BEqSqZ2lRY4gCEb9Hud1FBvUNNmNI0BwL6guAdK2LS6GEkebzDrjahcv0tYsdUwv5MHGKupiMGrcLyCt_9GVoekrpfgcFfD4MZ0K3QpMYCbxmJ2jDl__FDLnOKU80OPH5WvoPI146i0i0jDcE_bE5IsH0HZixyr4vSenZMoWjg-Ay8DKA6_3ZG8Fhp-VTjSJ30beRLs1RzIxQHsB5i3-ljHYNxS5ACbl4OfSbo5h1hlbO5XuG6Fa81tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=qfyXMR7lFCyVg2x6dsowrQ65khR1AwPpyL6wRb9pPQKKxhokQz4MWCw4diS36rqNjidrgB144C8jXrUKzgs5rd3LwQX6q8rw3NdTr78GrJeD2nbEdtn03AqcQ33Ka__lJd9NSWiiYWmLozpTrs5Hlr3wHvmGlHqNtGGH9iV2eb8moX8U_Fzjswf70Fptr1pOKKDv1yMDvGr36Uq1Y_LtU_jdZvEhtMrQ1cNCYfvq2VbV5SKCYm1wXOmaiwz3Z-89dsGU4GK0KMkN48hERiKlfjaJvyCkc9KHxRod7UkzDxQb37gnlHfsJLsscJMNx5gFl77AVgUHcue1DACpLfcmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=qfyXMR7lFCyVg2x6dsowrQ65khR1AwPpyL6wRb9pPQKKxhokQz4MWCw4diS36rqNjidrgB144C8jXrUKzgs5rd3LwQX6q8rw3NdTr78GrJeD2nbEdtn03AqcQ33Ka__lJd9NSWiiYWmLozpTrs5Hlr3wHvmGlHqNtGGH9iV2eb8moX8U_Fzjswf70Fptr1pOKKDv1yMDvGr36Uq1Y_LtU_jdZvEhtMrQ1cNCYfvq2VbV5SKCYm1wXOmaiwz3Z-89dsGU4GK0KMkN48hERiKlfjaJvyCkc9KHxRod7UkzDxQb37gnlHfsJLsscJMNx5gFl77AVgUHcue1DACpLfcmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=EVk7RTDYYlXBk1KASoV8onMX7-1_ZTVMTkYVzGsMMCaZWtKfjuB8hj6qIzjqdxOggHPS4FW1fjG2zJyUVTcHqlrhyOIR9FG4clOsRohHWOn5zuRHPvAYF_MJC8AOntT6f5jEG8PQbHm0NNT0KwhYxYEnk7Hvown87GG-OSCy_cDXmdhVkEpWeMstqqiSbERcUukBfwGdfCNzmigbh-DtiViN4_ah0afHXnF93r4wV8q4Uwbkm0soaVUmiDycerbwYxy21tSdMTig6KftFiQk2JTQFNI1VnBrax2dqlE-UgpSFH8dsIVBjj6vo-L_8CHWxR71NcahQ8oJSYfNN_x-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=EVk7RTDYYlXBk1KASoV8onMX7-1_ZTVMTkYVzGsMMCaZWtKfjuB8hj6qIzjqdxOggHPS4FW1fjG2zJyUVTcHqlrhyOIR9FG4clOsRohHWOn5zuRHPvAYF_MJC8AOntT6f5jEG8PQbHm0NNT0KwhYxYEnk7Hvown87GG-OSCy_cDXmdhVkEpWeMstqqiSbERcUukBfwGdfCNzmigbh-DtiViN4_ah0afHXnF93r4wV8q4Uwbkm0soaVUmiDycerbwYxy21tSdMTig6KftFiQk2JTQFNI1VnBrax2dqlE-UgpSFH8dsIVBjj6vo-L_8CHWxR71NcahQ8oJSYfNN_x-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=ulbme5hQNAv13C0Wp0wwxEPGNHBYI66SUXcib42eoT5ITgas0WkHvY4cKLItLiLH2-DHwPu4OB8g_oUMYYdYJjRU6ak1IeB3Wm3zfkzCMhpHdFdEfYjR4D0eqfIkZXR0pXS3IFDNZaZbzAXpNFRWI9LOjTY5NWbO8IvOSyKgQSfdixYx1LX6qU8mWc3Ekes_QiEEcwocznhLY7B0lPYGZe1ruGNPur0HJdUOtBsZcDG6UA3zEU6I_TUK3h260SYWHsANhZeUmWO_eITR2hjgJ_txiuhHnaXMdeY2pZVPHtb3PJGC9fu5OkcHUQ4TiwYGWo90Xcqn0gPNMqGqC2eO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=ulbme5hQNAv13C0Wp0wwxEPGNHBYI66SUXcib42eoT5ITgas0WkHvY4cKLItLiLH2-DHwPu4OB8g_oUMYYdYJjRU6ak1IeB3Wm3zfkzCMhpHdFdEfYjR4D0eqfIkZXR0pXS3IFDNZaZbzAXpNFRWI9LOjTY5NWbO8IvOSyKgQSfdixYx1LX6qU8mWc3Ekes_QiEEcwocznhLY7B0lPYGZe1ruGNPur0HJdUOtBsZcDG6UA3zEU6I_TUK3h260SYWHsANhZeUmWO_eITR2hjgJ_txiuhHnaXMdeY2pZVPHtb3PJGC9fu5OkcHUQ4TiwYGWo90Xcqn0gPNMqGqC2eO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=sRSN7H9oLiVWHUewir7iqqkNvcJqwaqz0xW_sndKlqQqPgpGTg_kwTd1pXUR4xeLqXuinBhlCONEKXOeLcOTmost_Ji7GhCLDIILKGKsfn4kAlzI_e_2Nj5SInIJBkyHX4X94q1UzUd-MnYkG9NlsXFxmHixs3R-u4ju7RoWIXdRvcoE8AB_d_kBr9b2R_-p-vQiRF_zD8tBOvsdQ72GNcW3wQlaJcwlG6uihZpOBhuJ5_UoTbubYBweMUlELjeWa1O1LjfbPJGyxeWtD8twELEM1m765X1SfmghKjE2XasBsur1OYKlpsH2plLvOZWxkf1GmH_Lz224VQoz8c2prA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=sRSN7H9oLiVWHUewir7iqqkNvcJqwaqz0xW_sndKlqQqPgpGTg_kwTd1pXUR4xeLqXuinBhlCONEKXOeLcOTmost_Ji7GhCLDIILKGKsfn4kAlzI_e_2Nj5SInIJBkyHX4X94q1UzUd-MnYkG9NlsXFxmHixs3R-u4ju7RoWIXdRvcoE8AB_d_kBr9b2R_-p-vQiRF_zD8tBOvsdQ72GNcW3wQlaJcwlG6uihZpOBhuJ5_UoTbubYBweMUlELjeWa1O1LjfbPJGyxeWtD8twELEM1m765X1SfmghKjE2XasBsur1OYKlpsH2plLvOZWxkf1GmH_Lz224VQoz8c2prA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=ZFzvSvKXPZZtLj0YOnB_1qxOTQNbQfH2gVNQybojGBoNMaprQQrCt39vUbXiP9Y_S2I83Dtsy56h1GBsm1RB1QyFrWUemW_WmNtUbKm_5QKy2zYY5ysMYfd-3J2WVTHmN4NnxV-q8-VCfCjjm8FHjSfEVbrNcRB1Zv2MlhH7akCrLHXlF8249373KLJVcDFUte-eCb-iMGK2LDC5fYBfoPO_lwdWElbrUnHpE_3aPRqCWt4aEN7w2ZLYCYl68GdN-74O5qpw_DH8hY_FwfTwbmZ9hwgd_SKN-AJNaSBZx51aFB8El19yRntrNvYS0Kx3tDSJUkLM_Iogx6gYt_-8bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=ZFzvSvKXPZZtLj0YOnB_1qxOTQNbQfH2gVNQybojGBoNMaprQQrCt39vUbXiP9Y_S2I83Dtsy56h1GBsm1RB1QyFrWUemW_WmNtUbKm_5QKy2zYY5ysMYfd-3J2WVTHmN4NnxV-q8-VCfCjjm8FHjSfEVbrNcRB1Zv2MlhH7akCrLHXlF8249373KLJVcDFUte-eCb-iMGK2LDC5fYBfoPO_lwdWElbrUnHpE_3aPRqCWt4aEN7w2ZLYCYl68GdN-74O5qpw_DH8hY_FwfTwbmZ9hwgd_SKN-AJNaSBZx51aFB8El19yRntrNvYS0Kx3tDSJUkLM_Iogx6gYt_-8bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZGKsbHwK2EFcB1DcBYY2EVmqmNHTWt7iFgJcztv1aXuAe7piSxjyObzg87hDKYjPfchUzOzBvCplfH-d4URvrEIaFIWjbxhr6yknrO6LHOYdf0wePCZ3H-Af_EStxUAS2BkywEAh8woe75aWF0mL5WjIzYqSsUH9FxdVEv1K3ep1DbKFAh8tijet7sTXJw8fOFGN1d4xNrsmgd7LnVJRphtQ-6JPF7FZlImLI6rt5VZagtncnY7OxXHKVghBCigvOhdB8djK_U-LeXjpHo172AUkjz0esFvImi6K0tDwNa6r3jk6Yal1Nhn-jSt1cLvA8hoF3XdnImB6wRN_seW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EzW0yDGTgGxXH_-33CW3UyhcvAoM7ZM0EPd2o4qsaC0mRc1oJA48iBlk2K-Ogc3TXStNWpDRILIIHnC4Spj0IN5qsCbj4D-J0qaJtDh3hb97f4OXpJWrtasqrZlE7bUiHNh1iFYv9P9HfMNugMPnYiSMREjEF2rU35GmMyZNWoN8XhScc1a-CFYSEuuFnwrZYLnK4oqnaimDygrok88WbVL8m95JLU8tcHj2mSQHFwh4ReLsXz_qvbFVD0iVeOMUphJ_G8vf7J0pidwCQwZLu_pXwJ0Vp3mW7QTu7RxlFaGMjbOI0eYgmg70BgRqUPe0EzET_eI9UUIiInJSnEsmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=TPKtkL7_5C3E02ZKwkpojF-H-rJ6F7bLFBBShSgjPvxm0SdoHFZI_CPoK3pAK4dEe6vWuIXNihX4eLujuAbPw3oKG9eP3mKTeGSbh5U7_EIntk-5-V22tx-np4TYNPGuxLT5NA4zSO7jFCz51j54ZwtlPw3qLFoxmgyGVKBzx5kyo8qf0x3lMM3Er4KvkhKmdLEpHNWLl60fjqqmDHeMXPy9O4d5IOmzPde79oVO6_gKAgWf9IUCjJbdpRFwUDcUwiy5PSwHtUyP56qbuny3DxdPtg3X5xuXiGTjq67fsTiiJB772LdyRDZt1wMHFMYCBnbTRHJvJ0WyYLrZ_tizAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=TPKtkL7_5C3E02ZKwkpojF-H-rJ6F7bLFBBShSgjPvxm0SdoHFZI_CPoK3pAK4dEe6vWuIXNihX4eLujuAbPw3oKG9eP3mKTeGSbh5U7_EIntk-5-V22tx-np4TYNPGuxLT5NA4zSO7jFCz51j54ZwtlPw3qLFoxmgyGVKBzx5kyo8qf0x3lMM3Er4KvkhKmdLEpHNWLl60fjqqmDHeMXPy9O4d5IOmzPde79oVO6_gKAgWf9IUCjJbdpRFwUDcUwiy5PSwHtUyP56qbuny3DxdPtg3X5xuXiGTjq67fsTiiJB772LdyRDZt1wMHFMYCBnbTRHJvJ0WyYLrZ_tizAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz95Tu8LmekkMatkAHecKuSkl6OMu6x6mk9hU0vXRdR52nuhytHkz9THK5KSD8GBMfB-jvqEMvz1jWIhXN6-78mhekDIXWjMxiA2-7bTsOOfMrE0szVpu_J63xAdHCOZDCcjrqRUOH86neLEBZXQ5vowiUoM70ACTe5_FRrd8HiHC_XwzJr428FwlFIOXBCHZi117RwfdzuWEzRqBe8avJxKRGBxgfQyDmImXThefn6Fvc5yFKpWuSQaW8S1YQaWPphEiudckfp1fvdQL4BUwO9JccErrFPJ1XU-ZJXRWFZTc-3_C84g_oSMo9Yacf8sty_m70H9s12kmeyy2rUJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=DkWAloO0nSixbwLAC6Vcffp3OZzpotwFtOjvHVDMPVW3uChVkKa-0RfjUfc1RvqKNgghS4Ggh6S09Fuxwzmu6ragYbpN71OIubPI--p6gzlC6Be1e1DXR3lXkAkXPZbGxYPszg7U7SURCohC1tCyiSAzylnue7JjDEUoKIkkzSy6JdrMY1UUPsXuTJvnP57yebj7GFQMwtQcUH-GfujNQrEl8yCnyYf2x18bRfnKPaafK7maehkMtOu0V27opM0qZ449c2e_8hYn2Yv5RnyBfj37Q3Qj0kM37L1zWDwKNQ-2v2TthxuTOG9a2A7ss4u6267BhC-ZxdnAoh-nkEgcmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=DkWAloO0nSixbwLAC6Vcffp3OZzpotwFtOjvHVDMPVW3uChVkKa-0RfjUfc1RvqKNgghS4Ggh6S09Fuxwzmu6ragYbpN71OIubPI--p6gzlC6Be1e1DXR3lXkAkXPZbGxYPszg7U7SURCohC1tCyiSAzylnue7JjDEUoKIkkzSy6JdrMY1UUPsXuTJvnP57yebj7GFQMwtQcUH-GfujNQrEl8yCnyYf2x18bRfnKPaafK7maehkMtOu0V27opM0qZ449c2e_8hYn2Yv5RnyBfj37Q3Qj0kM37L1zWDwKNQ-2v2TthxuTOG9a2A7ss4u6267BhC-ZxdnAoh-nkEgcmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iauzC4X4-4Aj5GBgW4iIj3rxOXqKzMAZvh3omSMwDPy-P7vkS3ag-zU3FQ-MlO6YzX7WalojJBG8PwXyk44Ii_FIEhIGPYFnl_aH0uZFNjdoTOrWwVZehb6P2BeY7VX9eJhUFZ9yLN2FEYen8eeLfpROZiF-RPVAqe8bAr8zMPAybFl07Y7npr5I7Bje4DodcdNZIMZhYGnDsdhdwAAGerp-a8Q1SyFaWQYI3FhTaII22KxKSM81A40R0M9DsT4xQSS-Wl2Qzbm--wTqUa4rTMAp7_tiyFgPM8B19wNh31nBW_7MeW_uZsPOJGcQNMgjG2oGiGiUiBgMd6B6PUAdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=kyUxWn3bu9zBfQymDU3PrSHCLluMSRtSaE6dwbsCq18ZZZRQRstKzGbHpIazYFTaCJBi0hKaSEJVqTJkGdpnXZBg6oJcZ1iBMra_usGTLfYtlRYz9rekZl0pyuNwIozHYk1KhPXvoZkxXCyCImnR-5-FrnOvt6KXIgFtjPMFqZI07O2ASytiZsKlLabcIKyu21wHC0KELC-AZuxRoIvHX4yTKVxZ9iFQ1TlLdnpjzxFnoeFJJmspsJYuOSVqDo0wzLv1Gv5oMXR_PECnXrSpzcvsVO-C4u0a3hfFqAnXDyQvjb3ous0oWaqfkF0wsAbbqDsaY64f9YN_JwMDyT5sxXu7sJaOkZQJUZNBRDUBAL7DHLXq1MBB-pqClmNygPF4zkHqS6f6YAMJzt2AkV3Mel79OpnpdaDL8ejlpMfQ8rLJyHCdaRWUKcbWf4-j-IHw-xcA6T3rC0LCNZPsp3pUYgM1pDRSfpSiknfmfDCZISAYOn3mVCC14A_VBrq9WoLk7eordrRkZ4WRlsSuoHmcdxJlM2G75rr1-g5Koi7TAlkAbbbJuN29vGSFrWa_gSPtVmvz_MQxThVSu9uX4vNSkIV0msYhBHMRv3rnY9Lt1n9FSSQtvQjTyfaZLMWf9_f3qQEyj2sbIOXgC7CFrOVZ5F3cPJ1jKYb7tfUo3o9bNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=kyUxWn3bu9zBfQymDU3PrSHCLluMSRtSaE6dwbsCq18ZZZRQRstKzGbHpIazYFTaCJBi0hKaSEJVqTJkGdpnXZBg6oJcZ1iBMra_usGTLfYtlRYz9rekZl0pyuNwIozHYk1KhPXvoZkxXCyCImnR-5-FrnOvt6KXIgFtjPMFqZI07O2ASytiZsKlLabcIKyu21wHC0KELC-AZuxRoIvHX4yTKVxZ9iFQ1TlLdnpjzxFnoeFJJmspsJYuOSVqDo0wzLv1Gv5oMXR_PECnXrSpzcvsVO-C4u0a3hfFqAnXDyQvjb3ous0oWaqfkF0wsAbbqDsaY64f9YN_JwMDyT5sxXu7sJaOkZQJUZNBRDUBAL7DHLXq1MBB-pqClmNygPF4zkHqS6f6YAMJzt2AkV3Mel79OpnpdaDL8ejlpMfQ8rLJyHCdaRWUKcbWf4-j-IHw-xcA6T3rC0LCNZPsp3pUYgM1pDRSfpSiknfmfDCZISAYOn3mVCC14A_VBrq9WoLk7eordrRkZ4WRlsSuoHmcdxJlM2G75rr1-g5Koi7TAlkAbbbJuN29vGSFrWa_gSPtVmvz_MQxThVSu9uX4vNSkIV0msYhBHMRv3rnY9Lt1n9FSSQtvQjTyfaZLMWf9_f3qQEyj2sbIOXgC7CFrOVZ5F3cPJ1jKYb7tfUo3o9bNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=aziZXFAFk0i3BVOjJwagPK5YEhmsTngTwQyE0bRQ9tSQfQT0iD83psfs8Mt2sMYnZrWKjigYhahEMlJmJb57ptSWc5CuoQ1zcBYdykoCegSiSGaGPbXegHCk6U32_2zMPF_wKc6pJv1YBa464BWZbFKY1k18Xc_K9PRb_aURKpUbxMEaL0DxGdMyX2uVW3qqgqSJmdzsV2vmDZUfWe6lWTzO2DU6WHEYTBJ3Zls9SvOZBvm0xv_-0n1rqwqt0e3OWk5Peb57vxt8szZBg644Wv12HOaJn7pVN53N-B9L6fybalQpi2fZQyItxsQ9JHDyasdbpdejib4WhDRz3YBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=aziZXFAFk0i3BVOjJwagPK5YEhmsTngTwQyE0bRQ9tSQfQT0iD83psfs8Mt2sMYnZrWKjigYhahEMlJmJb57ptSWc5CuoQ1zcBYdykoCegSiSGaGPbXegHCk6U32_2zMPF_wKc6pJv1YBa464BWZbFKY1k18Xc_K9PRb_aURKpUbxMEaL0DxGdMyX2uVW3qqgqSJmdzsV2vmDZUfWe6lWTzO2DU6WHEYTBJ3Zls9SvOZBvm0xv_-0n1rqwqt0e3OWk5Peb57vxt8szZBg644Wv12HOaJn7pVN53N-B9L6fybalQpi2fZQyItxsQ9JHDyasdbpdejib4WhDRz3YBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=FXCpnKYIbrKul9FGj6_IekpP-3dfZUbqCznzWYHIbRMWALVHVjlw9V5A_jBIhYEUanaeVjKXrUtKExUuWRku5f9fXPYocKXziSEMCrxvdFSIHArq1eUeNzBCH1_bHeXGfktLfH85jVjen8MjBbZpUnW6t0-AZWDD8a2S2Zwpd5P2iy8YCg8aJ_7-XNSY-2mws9ugS4yiQJ7NT9r6sqvsh34E5rvNgSblPKNFHS4GS4GVdLqwv3QiELnqyDnkx_9YoYzTrCt7-SFTSLDKsLcPZS5vZEHy5EgZjHk7DcrAD_5HFvhXxEmE82a5BMsH_bVgusB00Qsju-SKcCvsF6gJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=FXCpnKYIbrKul9FGj6_IekpP-3dfZUbqCznzWYHIbRMWALVHVjlw9V5A_jBIhYEUanaeVjKXrUtKExUuWRku5f9fXPYocKXziSEMCrxvdFSIHArq1eUeNzBCH1_bHeXGfktLfH85jVjen8MjBbZpUnW6t0-AZWDD8a2S2Zwpd5P2iy8YCg8aJ_7-XNSY-2mws9ugS4yiQJ7NT9r6sqvsh34E5rvNgSblPKNFHS4GS4GVdLqwv3QiELnqyDnkx_9YoYzTrCt7-SFTSLDKsLcPZS5vZEHy5EgZjHk7DcrAD_5HFvhXxEmE82a5BMsH_bVgusB00Qsju-SKcCvsF6gJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=MoGnbcCf3nUZH0-LF5L2ZVJetYMwTxuMW3ywZFj1ebQ0X3vOLiXfOGDm__C_CYK16y9Wx87nLZyWUJG0Kku84BXMHQ8UAfigUKmJL5I7FHwGUo8KsVo0hZuozxUQHtRQLaTMil1gGAuDgsVtwCHs16SFNDOsDtYsURB8IsKy59EANv5Mz9xsbC-abVTT4tqdXCjWX9gmwMAWvghR8sRX2hUp0T9XIA4RcubCCxmvwGAuqKxm_UAXlgQ5UTHAJMsnJOfQUEErkXNBb5UGa7Rn9G-FaiGs4fGuJxvhKXEgJ6ZQcca371mlDk5qNLCh8AcqghgugJ7sGZpPFUH8O4wt_TaMN8v2tZNj_KBQzBMwb0K58dGnCLFnSb3e6gNMe6yeKLwL8kojJchlUcFz0uiBuoeAVy-rOLvqjRUv1ACHnFMUgxa80UOoGemhhjY373PGVuw8HL39wkRy4LVmmdbk7lFxAh6Aenm4_hQanl7dLoIaFTq1j4i6MFqgq3jQyDHdDkbDbi0Qd-fxoTCLhMur6poO0rghoCg3X4DyMqjafEpLOTcR8ANQStiT_ic0cVbHoVRy7GARs6umedWa7jsj3mb8aMyuvQIORrcEPfo0WLV6inILuoLM1kXF6xdGGD97VQSrFf6kLYH9PuwLKm2ueEyLSM3WHuC3eqDJyxV-Jc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=MoGnbcCf3nUZH0-LF5L2ZVJetYMwTxuMW3ywZFj1ebQ0X3vOLiXfOGDm__C_CYK16y9Wx87nLZyWUJG0Kku84BXMHQ8UAfigUKmJL5I7FHwGUo8KsVo0hZuozxUQHtRQLaTMil1gGAuDgsVtwCHs16SFNDOsDtYsURB8IsKy59EANv5Mz9xsbC-abVTT4tqdXCjWX9gmwMAWvghR8sRX2hUp0T9XIA4RcubCCxmvwGAuqKxm_UAXlgQ5UTHAJMsnJOfQUEErkXNBb5UGa7Rn9G-FaiGs4fGuJxvhKXEgJ6ZQcca371mlDk5qNLCh8AcqghgugJ7sGZpPFUH8O4wt_TaMN8v2tZNj_KBQzBMwb0K58dGnCLFnSb3e6gNMe6yeKLwL8kojJchlUcFz0uiBuoeAVy-rOLvqjRUv1ACHnFMUgxa80UOoGemhhjY373PGVuw8HL39wkRy4LVmmdbk7lFxAh6Aenm4_hQanl7dLoIaFTq1j4i6MFqgq3jQyDHdDkbDbi0Qd-fxoTCLhMur6poO0rghoCg3X4DyMqjafEpLOTcR8ANQStiT_ic0cVbHoVRy7GARs6umedWa7jsj3mb8aMyuvQIORrcEPfo0WLV6inILuoLM1kXF6xdGGD97VQSrFf6kLYH9PuwLKm2ueEyLSM3WHuC3eqDJyxV-Jc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=rpco5qFqlW1O2EjGXOKTdS1ccOksD7nCJ9SyZDu_F3LDRII__6lKzK7z_Y_J0WH_lchqVsEiYHBhKr0F5pWiJsWlFA0OHE0az0eq_9WsnGE11OT2_Gqk9XCq3r6Wby22uV5OyqdArEHyhBDtTUTHZgzo44NufQCect0wrgtm_ThZ0QUQr0FwXOGS19tJNo_T85VJVdLSlzNKAiWIWX2Iu00LNG9u_qeBJdNtKP-m18CsDLI0qDfxLzhx5Kmur2nehCLJL4NUdk6vMsy22W71HtjBtY_iMPGOmC31uEp38MwCzwhW5QjznG97XFAkj0GrW4f6kFKZJE-ZD1_MihcT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=rpco5qFqlW1O2EjGXOKTdS1ccOksD7nCJ9SyZDu_F3LDRII__6lKzK7z_Y_J0WH_lchqVsEiYHBhKr0F5pWiJsWlFA0OHE0az0eq_9WsnGE11OT2_Gqk9XCq3r6Wby22uV5OyqdArEHyhBDtTUTHZgzo44NufQCect0wrgtm_ThZ0QUQr0FwXOGS19tJNo_T85VJVdLSlzNKAiWIWX2Iu00LNG9u_qeBJdNtKP-m18CsDLI0qDfxLzhx5Kmur2nehCLJL4NUdk6vMsy22W71HtjBtY_iMPGOmC31uEp38MwCzwhW5QjznG97XFAkj0GrW4f6kFKZJE-ZD1_MihcT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=k1HFT7p-dWnJDjmKAw_zjhQajKkavj9hXwWgXXjOerh3vs3SszDpX6orOTwYpkU8HMJsI0t3OAyMP01EUqAfKyDag__ymmUF2A9lZ8CDYHDCYLMd_DWrHP3qK1LTbG6q1vWipmsk4cV705LiV9DDdBu1wUZHt-4AT8_btpNvKppZ0yzkWWh4BIRFdSIJdJUePK8D5iBbxcxHNuu1iax8UHQSmF_CI05mr2OA8t0U4Ya1fmpwEFdxvzh4tiGEqZYXE1lgugqU-IO-27fgyg-KmYruTsQofnelfqAIpXU6ztgzoZHH-Jg-eMgrecd7nGFJ8iU_vEavwMuzfXFJs3RYXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=k1HFT7p-dWnJDjmKAw_zjhQajKkavj9hXwWgXXjOerh3vs3SszDpX6orOTwYpkU8HMJsI0t3OAyMP01EUqAfKyDag__ymmUF2A9lZ8CDYHDCYLMd_DWrHP3qK1LTbG6q1vWipmsk4cV705LiV9DDdBu1wUZHt-4AT8_btpNvKppZ0yzkWWh4BIRFdSIJdJUePK8D5iBbxcxHNuu1iax8UHQSmF_CI05mr2OA8t0U4Ya1fmpwEFdxvzh4tiGEqZYXE1lgugqU-IO-27fgyg-KmYruTsQofnelfqAIpXU6ztgzoZHH-Jg-eMgrecd7nGFJ8iU_vEavwMuzfXFJs3RYXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uS0ekXjmzI4YtDRdl-r0kR_kBRCdv6u6IkcEvBBffsARAeQcJfjm769Jc5167VijEF6OQme_Ppb5mDJFe9cwSzGe5wXDtcqqzO0yT_r-BfLaEIUuwqYo-82C6j6ymFrpfN2gdM5meA6-K_cjqTQDcOH9hK7R7QSIXUEqFIWE5YdTyPfDgeRyrCakqGwslrg0unrq7a8qGx1zQh_ZyBvqr4Rudyhd41D7sHJws-Z_MDqD4LUQ9t04Jxl1lHKb3PhP6gctex5IMKrWSTbY6vcreJ6dt05zRNYJnrYp2hxW2ZX1goxpoHHDn34kwya2JJE8foNFMEeLL5no0DIx_Ny-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=BKKkosu6eQtuBHbwdIARIlZyfRRhHO3CFPbUZoVw8FT8U94d-zOblR18x85W7-lkebt73A5JJ99YH3-zP-8WgfYpeSsYIDbV2Ivu8xoMkT3o-hWkrDjAkDuTmAyul9YHo33Awyv5WM8UuGIdaE09sac01T16NswmIMwaTNvtAiftHIQkSJw8VSIUVAllDbz8TQAUCrIzdG1WSZqc73d64oY78VRSx5RldInGTiFf8C0pr3ZMtFgwtXUit7__C0py6qd8I09gwPxqKpYElZEbQYUx2abKwwWeO9ksXOL7Ks1OBiUrlD_adkV3wF__JhFXlADt0lYCTSNF9AtEOaUBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=BKKkosu6eQtuBHbwdIARIlZyfRRhHO3CFPbUZoVw8FT8U94d-zOblR18x85W7-lkebt73A5JJ99YH3-zP-8WgfYpeSsYIDbV2Ivu8xoMkT3o-hWkrDjAkDuTmAyul9YHo33Awyv5WM8UuGIdaE09sac01T16NswmIMwaTNvtAiftHIQkSJw8VSIUVAllDbz8TQAUCrIzdG1WSZqc73d64oY78VRSx5RldInGTiFf8C0pr3ZMtFgwtXUit7__C0py6qd8I09gwPxqKpYElZEbQYUx2abKwwWeO9ksXOL7Ks1OBiUrlD_adkV3wF__JhFXlADt0lYCTSNF9AtEOaUBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
شب گذشته در سمنان، به افزایش قیمت بنزین اعتراض شد.
این اعتراض در پی تصمیم جمهوری اسلامی برای دو برابر کردن قیمت بنزین خارج از سهمیه یارانه‌ای از روز سه‌شنبه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71276" target="_blank">📅 13:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipYkjz3QHTRCmaUw6a_bRYAnHKUTdJ8ftCDbqTFKgkyO0zlZUnvL8wBapzw5GQSBmtYMly6bZPsyP4rzA4WqbR_g5sIBpyarOwcG6ZOkZdSTStYKlAidJsH97ny9RPsYgUJWu0uD9lgwGvK-yO9GriJth1-HBcAkOaRM4jsKEldt9Il_Sa8-Xc-_oYnRNRN_18comvR3FXyYLFdu-ioHqx6gRh4wkApz5TO5FDB65zkmGv7fMyFKDwEmVECnVnFLlAozqvZYqSfHvTomTWIrTO_YnTkvd7kDQgYKJspG3G_h1msJx3NTQ7-BRriuWa5dVxQJExPI2gFVcgKtdUc8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VWEleAcVOP2bdR-sHLUYJe_HX7iRAHyulz3R8tJ-zoLXDmyDrhELD2YfSPsGV0IlJUBONFqFECv8wXbPDd0HZ57gjO_SBvNpME9rBxfkgLQ99UW8iPetKY2aObcOuDgn_uyeDGUbMbXf40D8D_t-ZEblhg-OIXKs0FEW1SVyWOwGv5FriHCey66Akh78CxVYQ_E6MrnO-LBS_wqchebHAl-hAYeZvCLTuGhajbJy-mrJ8a4eVCVIZgokmxUa5WaiRsFRMpNpsA6l9kzrBIYAbW-pm0tLWgK8X7bUxNsl8CuYZLKrc_wjgrwk_POBfOqHfUCLCLg7to62Fqd2_n71zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=NEPggAUe15kw4YGaG8yFeVbG3odfcZp2hFbY_eHpuS9RhkkEgQYjRCDiJTnxoXMSD47mNDB8iRJ-iTdywLNdvul1AzHLGpVtXXGPBxylDNFpjIdEqwFMJzdbNv7BjvstGhxUEya_2-1bZfA2BjS2hgNzYW2wBTDI7fmz1yqFBNGhRMf_pl4MXjTJYbfhRmosVIL8gegnT_mFcSq-14iz35k0yx4pNhuJFNVa1zlLNRhbkvnwOLczwk0h7HSBnUUz4zNjDlofUgAy-NvcdqCJx-yUsIH89dRmjQbckTZHdhoV1B1toCZcY5DgEQCAGcFn3A2crDaXnJ_Eax54fCGPGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=NEPggAUe15kw4YGaG8yFeVbG3odfcZp2hFbY_eHpuS9RhkkEgQYjRCDiJTnxoXMSD47mNDB8iRJ-iTdywLNdvul1AzHLGpVtXXGPBxylDNFpjIdEqwFMJzdbNv7BjvstGhxUEya_2-1bZfA2BjS2hgNzYW2wBTDI7fmz1yqFBNGhRMf_pl4MXjTJYbfhRmosVIL8gegnT_mFcSq-14iz35k0yx4pNhuJFNVa1zlLNRhbkvnwOLczwk0h7HSBnUUz4zNjDlofUgAy-NvcdqCJx-yUsIH89dRmjQbckTZHdhoV1B1toCZcY5DgEQCAGcFn3A2crDaXnJ_Eax54fCGPGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx8DXPSQWHpgP-SRMh9Rj6wc5foCq5yT6x4uYrSVnIuOvYFsqoUAc020kF_26iWckTFK_Wxl1BCrO7Xo3KsloRDZHWPFV1ucEbFtq4cduLZF12Pk7zYWNSbL0spb3KEqhV2dJEDO-fN3y8KgQh8uNPN1WToAYtu0L0Pa3aQ7L650r-P7UsqNa-8Mq5UzLopEMhcBJexyuLVh9JJb6iKVKJWmIjilI16NHCZOyQydpHpHCCbASsUXaWm5jbta81k2VoW7wJXIhullC-cIe1UjJF-zS0z__EChOh8J3pZqFpybKOqdAiHMUo7nXFVfhfdnCUbBbYhSRxxGbt9etx5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=MVhIqNL1ZUk2UZIQJ16CJz0Ke6c8B9tl_6x2agwftIXzLLnRRI7QP2gGIpsekFbRt9imZeUKgr7ctHvBgUzHn7CoZDBnCGzrLWthJmb3wDtHmkBZJQrYlH0Pfce5eaehHgStIb2dItX3iUf9fmmSpSBcqm1uG98dWRTgsW3ncdOfOympmk3hDn0c4ESeSLtR-9zB7BCzJ94fYfnf6Pzd5Ya7kBTwFRFL9J-TuW9-kHOwYMUC3Kd3Hi3llPwNKG1nFQI31suCY_d2YJzirmKwhql8rwfBW5kOHHcCG5dN8hWdX1eJr3um7XxJG0wSq8lJZtWeoC5Mu3g0_CkTaEEwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=MVhIqNL1ZUk2UZIQJ16CJz0Ke6c8B9tl_6x2agwftIXzLLnRRI7QP2gGIpsekFbRt9imZeUKgr7ctHvBgUzHn7CoZDBnCGzrLWthJmb3wDtHmkBZJQrYlH0Pfce5eaehHgStIb2dItX3iUf9fmmSpSBcqm1uG98dWRTgsW3ncdOfOympmk3hDn0c4ESeSLtR-9zB7BCzJ94fYfnf6Pzd5Ya7kBTwFRFL9J-TuW9-kHOwYMUC3Kd3Hi3llPwNKG1nFQI31suCY_d2YJzirmKwhql8rwfBW5kOHHcCG5dN8hWdX1eJr3um7XxJG0wSq8lJZtWeoC5Mu3g0_CkTaEEwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzwhRA9rA8lO50hRbQmjsWpG0kQdHlr42tUi9JbKbM1eRVmu4xnD4dLv0XllumgfK65MwjgIX7tUmjuXJjBM_qtcFWUtfisfaqhb3VUeuLsko02oNyXNDzbqAJTl7-zMYsB-5JQZzgmEppJmcaBmMz3JQeF9imwsPuobnZsYrUETFJfwSfNB8RJ1FV7BrKGKjFWE-kysEtQikFHFm4GYYjiiHE62apvb9re0t-I-TX0Am2nwUug6SK26892q4meby3xsPFAvqd5OfXcNjZG7w0f_j4bAPz2EMq512NuHo7dS1OTyRSZIqodyt5tnFONC1V2rjGonrhC8-gu9O-rFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=n6Bi1H_q1vFNGc2OZowplLTUez751t0xszAQBxPzR5eZY6zPwWhz6SNWqRkvHmq4DxUDD_QR4iCcfGdHzljm9JSEZbKntmSkUVzPkXVs_XvriIB1NdhDEku8LHtY7WCvJ6c0niuqNOX_hl6W_0x78XEqL7JrLuz5Vi4RAasbyWVDYVWDGrz8iytfPBUI4yUTSTp_VOv5pfJ-DKvNTOgj4b45KtJ13iElT6vaDgpa4uUwAiCPG0lY7dk_VOTM2iV0VQWwMWQDWRkGH5X-xj82jHjpaHuVuylyy8kxke1bAVwfWCvMextLWcXLkZIhUT7FqTXBsTHb0jmKxRj4F0b92DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=n6Bi1H_q1vFNGc2OZowplLTUez751t0xszAQBxPzR5eZY6zPwWhz6SNWqRkvHmq4DxUDD_QR4iCcfGdHzljm9JSEZbKntmSkUVzPkXVs_XvriIB1NdhDEku8LHtY7WCvJ6c0niuqNOX_hl6W_0x78XEqL7JrLuz5Vi4RAasbyWVDYVWDGrz8iytfPBUI4yUTSTp_VOv5pfJ-DKvNTOgj4b45KtJ13iElT6vaDgpa4uUwAiCPG0lY7dk_VOTM2iV0VQWwMWQDWRkGH5X-xj82jHjpaHuVuylyy8kxke1bAVwfWCvMextLWcXLkZIhUT7FqTXBsTHb0jmKxRj4F0b92DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=Hc3M7O_XrrhuUKpWVHecLAXC9JsidJG6ga-y4wDESbAq2k3FtcYfRaEEJC-QhyQnQCpwbddY3iL2F7rQdC6mqfGi8VsY9QvZmuqrutG589magV-qY71v1xpbb5HRgYPnY7hibA0V31yFIEvyJj-1kqqarDiQg38UNPdKNiLvPPTEPoTC3AqRzOwQLh_80_QWqm6KJjIOIosKbvLLIsuYV76HPThwyjuQ0gRa73nAejaRS1sr2A9Hm8l3ur9M4cJlsJDBOKrmQ9rkgccV5j2fAVCpcfkUZP2weMK0U6em17llRngXarPfu3EkFWNfHlO8p9M-zeMsF7KLhUiiDt8Pwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=Hc3M7O_XrrhuUKpWVHecLAXC9JsidJG6ga-y4wDESbAq2k3FtcYfRaEEJC-QhyQnQCpwbddY3iL2F7rQdC6mqfGi8VsY9QvZmuqrutG589magV-qY71v1xpbb5HRgYPnY7hibA0V31yFIEvyJj-1kqqarDiQg38UNPdKNiLvPPTEPoTC3AqRzOwQLh_80_QWqm6KJjIOIosKbvLLIsuYV76HPThwyjuQ0gRa73nAejaRS1sr2A9Hm8l3ur9M4cJlsJDBOKrmQ9rkgccV5j2fAVCpcfkUZP2weMK0U6em17llRngXarPfu3EkFWNfHlO8p9M-zeMsF7KLhUiiDt8Pwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=ePRCWk0-6e2s8xWxcrsVN380AmIsYcX8ubrdsUJV-EIMiiwIUvS98qAiej8vwmVgNNb8DvBIH4EhbDoDKj3QjcSxExBx2ic9jotD0Wiyn02P904Nly3uKUloH18em1cYZkUz5jvslVDTabnHfpTgekWp3F650Qe7KeB42C6NvGtAtmjAR-jqrgwjF0Qa98qQHi5S1s68fRkIPtTGLM2uG-lU-iyuerDplXw7qyN4d30tBrsBNDAnJI318oq2-n_2fmRMZ76E6stJSzMG8BE0qfduTe9OsLQv51seIT6AaWCPdDy3ET9Y8nmVlhLUZ5fzjLwMw8LIWbr6dDLUXB2_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=ePRCWk0-6e2s8xWxcrsVN380AmIsYcX8ubrdsUJV-EIMiiwIUvS98qAiej8vwmVgNNb8DvBIH4EhbDoDKj3QjcSxExBx2ic9jotD0Wiyn02P904Nly3uKUloH18em1cYZkUz5jvslVDTabnHfpTgekWp3F650Qe7KeB42C6NvGtAtmjAR-jqrgwjF0Qa98qQHi5S1s68fRkIPtTGLM2uG-lU-iyuerDplXw7qyN4d30tBrsBNDAnJI318oq2-n_2fmRMZ76E6stJSzMG8BE0qfduTe9OsLQv51seIT6AaWCPdDy3ET9Y8nmVlhLUZ5fzjLwMw8LIWbr6dDLUXB2_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=gJfgW1JxcPEBGbyCNsTbtFg12CfuSjoZ8iBwTbJb5sXdr6B3sdAJmPH7hbi1K637TPVp0xfFZQ3uXzX-A_zqzO6uTGGaOlOH4m1iFW5MaWBYv2HP8-vGxA_3JJBCF2hdmSeOgXzQLfDxPSpwFPpTw7lEBlVP1oI94CNJiXvVbl8ydxNcL3LMw33IWO_y982-Id7SLwJMsO2h7nhpmtywJVKkRcQU7ZDAAX87sUM07ohRzqj1foI_D6vejIWmKVTFu7-TgKeaFZi9Wk_5huHzllTbAlVMBqx-8O1dmjM-lUkKiyYaz9dIb73J_exx-oY7jQ6lmn4g-ilCaGNAcg4FdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=gJfgW1JxcPEBGbyCNsTbtFg12CfuSjoZ8iBwTbJb5sXdr6B3sdAJmPH7hbi1K637TPVp0xfFZQ3uXzX-A_zqzO6uTGGaOlOH4m1iFW5MaWBYv2HP8-vGxA_3JJBCF2hdmSeOgXzQLfDxPSpwFPpTw7lEBlVP1oI94CNJiXvVbl8ydxNcL3LMw33IWO_y982-Id7SLwJMsO2h7nhpmtywJVKkRcQU7ZDAAX87sUM07ohRzqj1foI_D6vejIWmKVTFu7-TgKeaFZi9Wk_5huHzllTbAlVMBqx-8O1dmjM-lUkKiyYaz9dIb73J_exx-oY7jQ6lmn4g-ilCaGNAcg4FdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=nZA5SR-sbIEd7XzBiAjTJI_6D1_DqbA51su0Q9GQRJsloTvxneU7ZjnhqG2Zl2Fe51WXc44pRP3k6XX_XC-ZHEQnfK11tM4arBtZcsXRZC5w1tqDgMuzBV6jMEKXzy3yp8sT7cd_mrvm_yNnj1BQAzDaZGi-20Voc1512b3Mf87S6AXWdSnzWxSY5yr5VmCoua4fkmX7-jCz9xplseypxUAESbfYjQdlpqOKA6G6Amlzu-l3wPzLkfMsDpdKFTeQUywrcsLbiB-sSGwedZhtthOSxS0fUNGF-uxXPpBd2HMdAyaSA56_54eMI30UjdSciL1lUkLmUXV2suttFH4jDiEkdSZFSnXvFzsyORx_GaxB2VoF9wcXkZgDx3Wiyq0put-NwX-8dBDjAbq2m5JFd-rRwc025NvQwZP89chNpi0LQA0XPgoXSwHlHcTLERV2EnrzQ8t5j2T29h6WpmY5W3hUdlsl7TNQ1MKkyPU0vqhcYXBnVRLjQQ6cEWXXtp-bKer83GWeQt0S--OgTQB_q4kqPKiexcj2d9fLmaLkntXHdGLzN-MJA1XqvfENoQ_A2dNnPaiATe-HNFKLsKjF4HV5etT-NXVoX89vcEoRkDAFyX7pFT4j5-ltGRzZ63xr0Q-FTozWghAOtrC53Pb55MRR7dka1YmqsJTeBL2BaoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=nZA5SR-sbIEd7XzBiAjTJI_6D1_DqbA51su0Q9GQRJsloTvxneU7ZjnhqG2Zl2Fe51WXc44pRP3k6XX_XC-ZHEQnfK11tM4arBtZcsXRZC5w1tqDgMuzBV6jMEKXzy3yp8sT7cd_mrvm_yNnj1BQAzDaZGi-20Voc1512b3Mf87S6AXWdSnzWxSY5yr5VmCoua4fkmX7-jCz9xplseypxUAESbfYjQdlpqOKA6G6Amlzu-l3wPzLkfMsDpdKFTeQUywrcsLbiB-sSGwedZhtthOSxS0fUNGF-uxXPpBd2HMdAyaSA56_54eMI30UjdSciL1lUkLmUXV2suttFH4jDiEkdSZFSnXvFzsyORx_GaxB2VoF9wcXkZgDx3Wiyq0put-NwX-8dBDjAbq2m5JFd-rRwc025NvQwZP89chNpi0LQA0XPgoXSwHlHcTLERV2EnrzQ8t5j2T29h6WpmY5W3hUdlsl7TNQ1MKkyPU0vqhcYXBnVRLjQQ6cEWXXtp-bKer83GWeQt0S--OgTQB_q4kqPKiexcj2d9fLmaLkntXHdGLzN-MJA1XqvfENoQ_A2dNnPaiATe-HNFKLsKjF4HV5etT-NXVoX89vcEoRkDAFyX7pFT4j5-ltGRzZ63xr0Q-FTozWghAOtrC53Pb55MRR7dka1YmqsJTeBL2BaoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71259" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71258">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHj-7b-MtnAhwDCafComKXz3I4MoM6euTknE7JXjOXds67zIwgGgeQ15kq32YVKqr8XItcgmwmeTwHYGYnElIyn4mxQ1ok_04hlH5k9-gUFc5CFfIi7Iz6vli66rL8zBGaBsRd3a9-RF0XR6es3stXiVACWUqHpoqy0Y8yz1bEtfD-8XGgNGDLdmLgZO2kmLf-ZVzHNYDhA3vH6VhpzCoeCUr58HqW73mke_JFZbPuoXng_EPJaFQ5WC3aVest0xrCB6p9zBms55t0T42NxgAFMoPgYZTX5cg9cqAsjbFakfQWW9mDw-oxPY3lUu-xe-CHD9c058uK99tzqLk6_Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71258" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
⭕️
از دقایقی قبل نرخ سوم بنزین به 10هزار تومان افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71257" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=d7XY6BTizTkvZJvcnjYsT1KLdLgLpUGZMrtFZZWcB_9yRVLbD5i6aUmth15lPA2mjFWIrL3Y_kR2GyVjS3ZrimiPKeuhW4nUc2pBlcJZIf09DcszzrtkzVJkVNRWdjWIQdqE738nXkX3bHGNrWkvYViMmnqbkkYiaEfdceTbJA5IX7jwqc-0w3ihCevVCWxosf8LJVIznZ6GQXdMoxip8A-WQtDPvRup4UxQTTnT24nulHl_9eoIAko6B2UgJPjRR2kA4Bz4zUWtUMgXEF9dtjSuJw5OYNk-l6T1XF2wzANYiwACmzwndPAQ3kCo424tod8XBLf9lXhRaZy_HR3ctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=d7XY6BTizTkvZJvcnjYsT1KLdLgLpUGZMrtFZZWcB_9yRVLbD5i6aUmth15lPA2mjFWIrL3Y_kR2GyVjS3ZrimiPKeuhW4nUc2pBlcJZIf09DcszzrtkzVJkVNRWdjWIQdqE738nXkX3bHGNrWkvYViMmnqbkkYiaEfdceTbJA5IX7jwqc-0w3ihCevVCWxosf8LJVIznZ6GQXdMoxip8A-WQtDPvRup4UxQTTnT24nulHl_9eoIAko6B2UgJPjRR2kA4Bz4zUWtUMgXEF9dtjSuJw5OYNk-l6T1XF2wzANYiwACmzwndPAQ3kCo424tod8XBLf9lXhRaZy_HR3ctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=NVCXloP4UokI0flfLq9FP8CjsmPCAaQvlYjiKdUe8zOtc7T2NxiaZztYEtnyseuHUQsrwiNwdK6OwpaKUjiKuP5qgVj6jD_EPEqLCR8QCnfSz-j2z3m9s0YC6i6Rmb5MPzWoaPTlPwRq1kGoyI2QB0CmYaTvlTO4mqYagduRYZLTiNU7SpqAWqoqUl63oHYHGirsNTvUq_PN1doXRIFAAfg6h9c5qcxH6TJSkTsawHKxa35pwDjl4tY8w-AnHx_MMHhmBE5OTi-H7U96kLBtYeAzLEOxCalOe1Pwnmdesg0vhqICLi_C9nqXR5e0Ehqn6RptrqAUx34ejlCfxiSIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=NVCXloP4UokI0flfLq9FP8CjsmPCAaQvlYjiKdUe8zOtc7T2NxiaZztYEtnyseuHUQsrwiNwdK6OwpaKUjiKuP5qgVj6jD_EPEqLCR8QCnfSz-j2z3m9s0YC6i6Rmb5MPzWoaPTlPwRq1kGoyI2QB0CmYaTvlTO4mqYagduRYZLTiNU7SpqAWqoqUl63oHYHGirsNTvUq_PN1doXRIFAAfg6h9c5qcxH6TJSkTsawHKxa35pwDjl4tY8w-AnHx_MMHhmBE5OTi-H7U96kLBtYeAzLEOxCalOe1Pwnmdesg0vhqICLi_C9nqXR5e0Ehqn6RptrqAUx34ejlCfxiSIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=UK_a3M6Nug4drRBlgn0y2iY5o2uSsH7hvD0nrTx9jWMM2bbxF3T7-Yws_QGRjSPiSTQwAA9uHKZpvPEzbyWj1OtT49IfB5aYVMvGETlEiB1z9oHHq210xqJhUjF66q2cZXk9FTsnttFv-CZst278eErdnOW66z5T_sWFFV-n7v7KdcWZAi4qcocG2KKC7M8B5qIp6Rd7u3dFW2prhYQ5KKwbRe3YMXdP3I0lQYj4dec5PMBYdDlYG-IAXrWvJEzs6POpWh7nFV0s6Ul-P0jU-C6C9YKbE7LSX68JoVMBEQKF84mZrzb_GhfPoJwVi2G5MXbsVOx7YWU7tLtBjXqjGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=UK_a3M6Nug4drRBlgn0y2iY5o2uSsH7hvD0nrTx9jWMM2bbxF3T7-Yws_QGRjSPiSTQwAA9uHKZpvPEzbyWj1OtT49IfB5aYVMvGETlEiB1z9oHHq210xqJhUjF66q2cZXk9FTsnttFv-CZst278eErdnOW66z5T_sWFFV-n7v7KdcWZAi4qcocG2KKC7M8B5qIp6Rd7u3dFW2prhYQ5KKwbRe3YMXdP3I0lQYj4dec5PMBYdDlYG-IAXrWvJEzs6POpWh7nFV0s6Ul-P0jU-C6C9YKbE7LSX68JoVMBEQKF84mZrzb_GhfPoJwVi2G5MXbsVOx7YWU7tLtBjXqjGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=dVpSmT-9uvtXlrL_7mfCre4PqmpGtvfLViNpobBKbDSI2HlSRmXAUrxtWyftEhnTwNbBRl718nA9sJWlqnf-JE6vEZh2LFVrI9m7nO4mz4oaDquJbQ4LyG4csZ12sKAWnU0qIGcmb6UHaoY4SXgvYnGEHSFquO8dtMtaSqCKH7VouiJ0ljzWd_-27pOaqxg5qZkqzcCrez43kyxxB97ydcmlgHGd3FSK8tqstHCkzvD67FWhxODD1aSaz4mYIAtVgzpbDWm07uddybBSzawemqOMe05ZPMO9ME9yh00Kx_GbG511UrZeto2f2e1ePaDosZv4z_Is0o4hrkOXv8tQqgk7fbcF_1RfL3avXiL9ioiHve8ZfOOUdIJ32QjuLjRFFfntcwr9ARUlnaC2pPddA8xkClmf2I_1iUFQ6nMk3dvaut78Oun_88RPpChCIAZHNmfIwLRVXoppIRinuK5xMLBJ-v8wpb5xCntd2bak8hs4iXQCWX3cGuoGwUHqWGUEDbZ8mu3CpDmPgTsoXZnlXOblL82FVm3Ru8DnKZ9xKDEZjDFwe6fm4hl0y_gHBO9ZJfoR1oayeMjc2gDh4xof9RAT8qZa6YVKbj9wRMXTXMWnILHBaLYoRL7TyedJomNHZrtgb28VLUeYMqEHjvYyOaeif07k65LVL-APTy5qKGU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=dVpSmT-9uvtXlrL_7mfCre4PqmpGtvfLViNpobBKbDSI2HlSRmXAUrxtWyftEhnTwNbBRl718nA9sJWlqnf-JE6vEZh2LFVrI9m7nO4mz4oaDquJbQ4LyG4csZ12sKAWnU0qIGcmb6UHaoY4SXgvYnGEHSFquO8dtMtaSqCKH7VouiJ0ljzWd_-27pOaqxg5qZkqzcCrez43kyxxB97ydcmlgHGd3FSK8tqstHCkzvD67FWhxODD1aSaz4mYIAtVgzpbDWm07uddybBSzawemqOMe05ZPMO9ME9yh00Kx_GbG511UrZeto2f2e1ePaDosZv4z_Is0o4hrkOXv8tQqgk7fbcF_1RfL3avXiL9ioiHve8ZfOOUdIJ32QjuLjRFFfntcwr9ARUlnaC2pPddA8xkClmf2I_1iUFQ6nMk3dvaut78Oun_88RPpChCIAZHNmfIwLRVXoppIRinuK5xMLBJ-v8wpb5xCntd2bak8hs4iXQCWX3cGuoGwUHqWGUEDbZ8mu3CpDmPgTsoXZnlXOblL82FVm3Ru8DnKZ9xKDEZjDFwe6fm4hl0y_gHBO9ZJfoR1oayeMjc2gDh4xof9RAT8qZa6YVKbj9wRMXTXMWnILHBaLYoRL7TyedJomNHZrtgb28VLUeYMqEHjvYyOaeif07k65LVL-APTy5qKGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمودی بعد مصرف یک بَست:
موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71251" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jso3_v6EzQA5fmWVZBwImRjY0FeyTW1pWpzfdyH7NRl8XRuzxeXZedeGOH6j8M5gTFeXOOyM-pa4XXDqy5hoForIv_kbNqBrKXTk5PS3hedVgit6vieHXuEXXHhv8KZfLvXyNxj9BxegY8pM-nAcv_F2mdv22jXbnItjmt7xkg9HxjL5n57wz54udx2mWGbcJpi1OCpPW_b-RNpwkcM4jJrYP8OQbdZsDZ0kKQUrfhmNHPwenIdsmP7MCesT2S-42hpbPdskn5hRmSSBEorLwakWQEtBbDgSc_g71iHWEpQbjDHrt8v1288haSXDMhH9GI2nX-Je7DoRWTsZRtbAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=MzSnKTeUGLu1xLf-xITtWLz8hIrzJrTBpkApF7bfhkPdviVyH5tvQ18KoGeH5F0FCv6NptqOaKzRtCJ6ciLX6YyhX-YHbeHpKW3RX19L4sZnnH17jtVd73MkPZfM6vvHOQuEOL8bwIxuxfNlNZkTxePuaiI_dYwM32rAmnKoaU81Fd6zufEJbNsTgbU_bOs16qvuu1XZ8UfxOOA3d9ewFwUlfnkU00UC_kQBlBrm02kDwyVnEDoqrxnsQpcRsSCy-6NrUBNmWZLJe-RHn7l06hTNEiUVheOv9j_EYPNckC_JH2iE3vGrJgrmClQSipu7PGzUptKcbEpIvtSf0Dck9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=MzSnKTeUGLu1xLf-xITtWLz8hIrzJrTBpkApF7bfhkPdviVyH5tvQ18KoGeH5F0FCv6NptqOaKzRtCJ6ciLX6YyhX-YHbeHpKW3RX19L4sZnnH17jtVd73MkPZfM6vvHOQuEOL8bwIxuxfNlNZkTxePuaiI_dYwM32rAmnKoaU81Fd6zufEJbNsTgbU_bOs16qvuu1XZ8UfxOOA3d9ewFwUlfnkU00UC_kQBlBrm02kDwyVnEDoqrxnsQpcRsSCy-6NrUBNmWZLJe-RHn7l06hTNEiUVheOv9j_EYPNckC_JH2iE3vGrJgrmClQSipu7PGzUptKcbEpIvtSf0Dck9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHrp_u4IbVaEcTdxSFU0vj4ePGp-j3y8TFYWSnhp8SiHPU-6uCOYJao_PQxF0Yg_096kSf4RJj5yYjn4Z6XbJ9MWwMklloq6hdKzK2VvBQ-FU3e4L57yXutR4xWDSnQOpkjAvBJzcaU7OnstmdWImEcoydrJlFmANRSbcT6aQZv_Gu_hT9vfb9GF9gkMr2BiaJHb9IN_TSmdMVwgeQ-F-0qQbVeZ8rDXDBWZJdeefpetyNLQpUrbEH2pqp8lv9oVeO3w6ZbQqKjzXbmCod6fgmqdZOckIAA2nkAsCXm6Xdd7hLmE1t3nMXQ36_Qx7VX8mJc6XGNTo8jnnSw6WB83qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Cqj5oUmJS3RIRiEmlHa-0O6OeLxije8aQRtZ3_gqJZZ_UcK1vAKkbB2dKpFqLh1kWvK_ryUTf6u2LqE2R3JmspcXyDE5WQUzrkuzR1nWm-7GDy_wWrstrTsfr0utIdSMS2TZCxRL9XmIrJ5b66oMrUrlnfudVBGNS8Y1r-SrCA4MddjjSZRZ4Ko9bKbraHEdDj29j60TcQoPc9UJ-8Cnds4ckZAcD04cEnXu29RUqCvn1RD6bKdibtxmx_iU7sPxSfgpl_j-aiy3HFYc7mNkVIoh4O2G_Ydo24_W4-exolazlbeU1aZiTDSDZAGPzpNib2mQzl7RKFsXLpN_FYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=P6qvnAmRlLYC7g3Hxb8pNtIWcHiaue2CRMY92Gu-Bx2U4tGRGUQfMj_j_TnTiuPt8inmEIUepIqviB7x0iYJ_AqFhsiLGciZlyyaMHYRRExRHkRxeaZfOj3nBLKjUJ0Kk1UhQash9ZpDOoedC6V2B73Zl1-edWocK2Q9exwmFsI3rcgFF3_PpDMN8WaMq2vEtfU_TrJXfuhGR9Y4L3mjjElRpBKbqle6nUS10stt-Kr1_JlW5xLeXoAoMd9L4ZO0nDOjXUIq8DYWa10HCqBuVTP9WRlbU9BzbXjDzhSj4i93sSPTtZmF1xSsJMVSyJ1K8qyUd_VaByw5J7vFhO2HKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=P6qvnAmRlLYC7g3Hxb8pNtIWcHiaue2CRMY92Gu-Bx2U4tGRGUQfMj_j_TnTiuPt8inmEIUepIqviB7x0iYJ_AqFhsiLGciZlyyaMHYRRExRHkRxeaZfOj3nBLKjUJ0Kk1UhQash9ZpDOoedC6V2B73Zl1-edWocK2Q9exwmFsI3rcgFF3_PpDMN8WaMq2vEtfU_TrJXfuhGR9Y4L3mjjElRpBKbqle6nUS10stt-Kr1_JlW5xLeXoAoMd9L4ZO0nDOjXUIq8DYWa10HCqBuVTP9WRlbU9BzbXjDzhSj4i93sSPTtZmF1xSsJMVSyJ1K8qyUd_VaByw5J7vFhO2HKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=ZOjAZc8JM8Hhh4GnWlKIwbrqkJe-xC7Dsn2slLLUHnVphx2r6SquGhb6uNajooFxvi75EBrENRX4agJArzIX_ZxM7MkVOoo0Y3icgnmZa0_9zxmuvBvGAGWwJtWIxpeTPY4Sj1Vbfg_kb6OzZsS5ShwMdj66K87xS_RAWiCUtk3Wphm5DbYEeJjv8bt8C3JC6-HFLfynABSRtb2kN4nNG-j_7ug3Y_I8F0XBW9CrY7LJpTDOvm15fR6O7SmnddmKbi1lp-PwhV2ow8UnC7X_zQClQlS0EbSVfnhCiNl5E0owEVUlAW0I9xi5gotpc486ljzm5VVWKS1u5sBJKPFBiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=ZOjAZc8JM8Hhh4GnWlKIwbrqkJe-xC7Dsn2slLLUHnVphx2r6SquGhb6uNajooFxvi75EBrENRX4agJArzIX_ZxM7MkVOoo0Y3icgnmZa0_9zxmuvBvGAGWwJtWIxpeTPY4Sj1Vbfg_kb6OzZsS5ShwMdj66K87xS_RAWiCUtk3Wphm5DbYEeJjv8bt8C3JC6-HFLfynABSRtb2kN4nNG-j_7ug3Y_I8F0XBW9CrY7LJpTDOvm15fR6O7SmnddmKbi1lp-PwhV2ow8UnC7X_zQClQlS0EbSVfnhCiNl5E0owEVUlAW0I9xi5gotpc486ljzm5VVWKS1u5sBJKPFBiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=frHJ7CgMlRIzndAnkcGl5a3I7D3awmtKBVyLbt2x_98XZgxEvdfu9ROIg-7ZyGEzYfucmkYUNYvIIpawbkHmJP6dMO3WVfmyBw-bO7mUic2x_wAceWPub9jZMYqHDK1-mqiwcWjtUl_-LxaeCbXfrVt5AvAuL5TEBcJik6644Fj4Bfbru23JFDuJ7XbZR8alYcNT3W0OViDba0-i9Hs-LHK2tCeZrbvEk2ei_bwQh-bcATAM4sgiZbIHWJSYPdnQPTILSDAl4Ymla3EqBW1pM-88fEnFiHivl81z1_ZY7nh5d815hTl-NYFWURHwHndE2HolF4qaOCrnz0AluSyR5ItDbhkDG6w-ea3V2coI-q4ZIP2Q31rf0EOarsOEdAmJaSVjW8bbtYaVKtUCKgwm8iwfSdBZs-y8NoWuUrvDMMh-i8LDPRsn43rBAQiXJCTphqBEnQJuSabgjH8W5fe8mYtY1B6Q1c3sRpjGYg3H_poD6YRVq3zwYkG5o7wdCLuk0t7kgd8yKrvzEaqN77QtWsd8yPf5IBbzdVv1jNHO9vX9t92KL0Rdpv_rqeGgIkjTiiU1bMTkbu7Ke5DWTQe38FIo1ADGkol2RBAsBL5wHMgfUKtbnY87JECFPMvVYF4qkwroS1urXF8xWtE7ZYXDCtT9xpuy9ICLg1xTQs5uHGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=frHJ7CgMlRIzndAnkcGl5a3I7D3awmtKBVyLbt2x_98XZgxEvdfu9ROIg-7ZyGEzYfucmkYUNYvIIpawbkHmJP6dMO3WVfmyBw-bO7mUic2x_wAceWPub9jZMYqHDK1-mqiwcWjtUl_-LxaeCbXfrVt5AvAuL5TEBcJik6644Fj4Bfbru23JFDuJ7XbZR8alYcNT3W0OViDba0-i9Hs-LHK2tCeZrbvEk2ei_bwQh-bcATAM4sgiZbIHWJSYPdnQPTILSDAl4Ymla3EqBW1pM-88fEnFiHivl81z1_ZY7nh5d815hTl-NYFWURHwHndE2HolF4qaOCrnz0AluSyR5ItDbhkDG6w-ea3V2coI-q4ZIP2Q31rf0EOarsOEdAmJaSVjW8bbtYaVKtUCKgwm8iwfSdBZs-y8NoWuUrvDMMh-i8LDPRsn43rBAQiXJCTphqBEnQJuSabgjH8W5fe8mYtY1B6Q1c3sRpjGYg3H_poD6YRVq3zwYkG5o7wdCLuk0t7kgd8yKrvzEaqN77QtWsd8yPf5IBbzdVv1jNHO9vX9t92KL0Rdpv_rqeGgIkjTiiU1bMTkbu7Ke5DWTQe38FIo1ADGkol2RBAsBL5wHMgfUKtbnY87JECFPMvVYF4qkwroS1urXF8xWtE7ZYXDCtT9xpuy9ICLg1xTQs5uHGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=kEqyRKqU55sCpTx4aLYnrH4klx1EA-SQQPpUkWkb_sPW4V3hQtQhZja_DRfTQlpz0CGUtgIqmfcZgM995A1OQmF-OQrS6wk0MuoW9PQ7qgQUHwaDAGIVtGZV5YHPSDq3EdOcHrCPDWQ3vKx4eGjwTkebqOSbqwXmI5cHRB31Cu98kT-hNfJhrAk3SihvH3jbxa6SMCM_DiDZbpIUL0j7z4yyG6WgEDsmnoCMMnxuHAllLBgkl1lbXyau0nYMMpJamNwNEhmV45kpE_hQ3ecYO0w0EtO7In9A9Z6tp0eCbTgnQsJIwphTkU7RNmNbPN9KbwmgLSHqyed2FaIxwzH_vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=kEqyRKqU55sCpTx4aLYnrH4klx1EA-SQQPpUkWkb_sPW4V3hQtQhZja_DRfTQlpz0CGUtgIqmfcZgM995A1OQmF-OQrS6wk0MuoW9PQ7qgQUHwaDAGIVtGZV5YHPSDq3EdOcHrCPDWQ3vKx4eGjwTkebqOSbqwXmI5cHRB31Cu98kT-hNfJhrAk3SihvH3jbxa6SMCM_DiDZbpIUL0j7z4yyG6WgEDsmnoCMMnxuHAllLBgkl1lbXyau0nYMMpJamNwNEhmV45kpE_hQ3ecYO0w0EtO7In9A9Z6tp0eCbTgnQsJIwphTkU7RNmNbPN9KbwmgLSHqyed2FaIxwzH_vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
معاون وزارت ارتباطات :
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی باید ادامه داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71241" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=Da25xBE0bz5xty66C_tR3nZyxXX-cY2AgslOZjtFO_nNgCMgYnC9axzIQk-yuQ2sfHfhpvMwLYAqarCE_C9V6MgDKBtcOMmbqAukLhTWmbr32eRZZ28zSmgbBv9gWcfNGLkCOiXrNc1DLgQbJXokT2L5t_hz9CZbhxX9F4bLAyRAfof1O-7Y8v6rYu1VnVcpgH7nwRGw3QU9L7snZ-577y_nVzSh_b19OGm0mDFYoK_wyqmGOQC1rNy2uZSU5kNDZf4qgM3g2RTbA1ncABeR_nBBh_CgSogfziJEI21qWxebL7Ra1NgjdyyYGTMhOjZJVDjdb7MTaa6nvbzip7mDJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=Da25xBE0bz5xty66C_tR3nZyxXX-cY2AgslOZjtFO_nNgCMgYnC9axzIQk-yuQ2sfHfhpvMwLYAqarCE_C9V6MgDKBtcOMmbqAukLhTWmbr32eRZZ28zSmgbBv9gWcfNGLkCOiXrNc1DLgQbJXokT2L5t_hz9CZbhxX9F4bLAyRAfof1O-7Y8v6rYu1VnVcpgH7nwRGw3QU9L7snZ-577y_nVzSh_b19OGm0mDFYoK_wyqmGOQC1rNy2uZSU5kNDZf4qgM3g2RTbA1ncABeR_nBBh_CgSogfziJEI21qWxebL7Ra1NgjdyyYGTMhOjZJVDjdb7MTaa6nvbzip7mDJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آخوند قاسمیان:
برادران یوسف 11/11 وحدت کردن یوسف رو انداختن تو چاه، این که وحدت نیست، وحدت باید حول محور رهبری باشه..
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71240" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98f065761f.mp4?token=nkHvtQtnqx5Qdc4v8egH7J3UmdJj_lPbYzaoRzLwz6MkLXgM-Fs3SXSs60sbe1S7wKOnaJpP2FlnnalZzvjEUwj89FP3kKzRDgTuGCs5x-xsLe1o1Dg86x18M6pFTQNbkp5L9UvsTop2cZV88FzFsaJBhb4qyfIjKhUiWbCaL7FhnJNgmgJFgaD8FqMz-RVi_Ajk5w6dYk6j6BiS2irE5fXSF3JjA2J485i0wvfGQPp2f1LeDJ1F6riOyReRZyZG6aqMBxLjdwFSXSyWRZtT6aLJNFrhSpg9LWybgQex_4W3yOIt2XsXTpZ4mTCW_A_2ybyHFfk6hnom7xsG_qosnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98f065761f.mp4?token=nkHvtQtnqx5Qdc4v8egH7J3UmdJj_lPbYzaoRzLwz6MkLXgM-Fs3SXSs60sbe1S7wKOnaJpP2FlnnalZzvjEUwj89FP3kKzRDgTuGCs5x-xsLe1o1Dg86x18M6pFTQNbkp5L9UvsTop2cZV88FzFsaJBhb4qyfIjKhUiWbCaL7FhnJNgmgJFgaD8FqMz-RVi_Ajk5w6dYk6j6BiS2irE5fXSF3JjA2J485i0wvfGQPp2f1LeDJ1F6riOyReRZyZG6aqMBxLjdwFSXSyWRZtT6aLJNFrhSpg9LWybgQex_4W3yOIt2XsXTpZ4mTCW_A_2ybyHFfk6hnom7xsG_qosnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رو آورده بودن موقع زایمان پیش زنش باشه و بهش روحیه بده، آخرش دکترا مجبور شدن خودشو درمان کنن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71239" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=bx52NqbHnxpUBxbNoYwq-5pUAxH3PWfRaPoamsVqEkBsHygKHHvUi3yz95-K6JidJHW8-E7WbAYbjJ8kG3QOvXHrMSGNYcvudxsa4A-byMkk9xJBGIapp_jlQxL0cRsMbH0nXzFbeuBB_7gUbe9r-Wize5kKjGJ67b_3ZWG-mW87mSiISTfuAd8F3XMtvL1i2x5_R2-GJ9Xww8zXfBzsv1AN8H6bJ2jL385wJxbltyIjKrCUdCzBoTDz7Sr_UJj6LeTOK_s7pepoJ6skrqmAtroTzn2k_GrXVS-ajH-vTH5DHK119H8tVed7Jf7mg1WY3EBlFXG293mR9yFamYWyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=bx52NqbHnxpUBxbNoYwq-5pUAxH3PWfRaPoamsVqEkBsHygKHHvUi3yz95-K6JidJHW8-E7WbAYbjJ8kG3QOvXHrMSGNYcvudxsa4A-byMkk9xJBGIapp_jlQxL0cRsMbH0nXzFbeuBB_7gUbe9r-Wize5kKjGJ67b_3ZWG-mW87mSiISTfuAd8F3XMtvL1i2x5_R2-GJ9Xww8zXfBzsv1AN8H6bJ2jL385wJxbltyIjKrCUdCzBoTDz7Sr_UJj6LeTOK_s7pepoJ6skrqmAtroTzn2k_GrXVS-ajH-vTH5DHK119H8tVed7Jf7mg1WY3EBlFXG293mR9yFamYWyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویدیو وایرال شده از یکی از معلم‌های مملکت :
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14 تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71238" target="_blank">📅 15:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
این خانم ادعا می‌کنه که در جزیره اپستین بوده؛
صداوسیما هم صحبتاش رو پخش کرده.
ادعا کرده که به کل جزیره تجاوز کردن و شرایط بدی بوده.
بعد میگه خداروشکر فقط خودم مصون موندم و بهم تجاوز نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71237" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=r-pIhXAyAsn50Kwf9-ze1UV_sW_x6t7EyIJNHboa3M7diince92Y6TeFajUVLlKLVj4lw13PRDVFKm5kKtHA7LmeK0JSXOA9Q3OlesqKUS0mGaeq8go1NDOLQDLBe0NDGq4giThebWf3U3pb43BKWHLYkDTCU1FXUy9r5Q2AivZU2UExDQXsTfRWv4K6jGrsgCg4cNcNMV2ItN_mQBZJgGgIQ9vVW_mnyVgLDV490FFpuCLdmf5Nvtk1E5mnuKyj712lflzz_Po8Poq0Z36GqlH7H_VO6v5SFszzbWHCt4bPVNETR68AQ7l5C3lbz9ROdQQkxb2VtRhfFcKwgir5Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=r-pIhXAyAsn50Kwf9-ze1UV_sW_x6t7EyIJNHboa3M7diince92Y6TeFajUVLlKLVj4lw13PRDVFKm5kKtHA7LmeK0JSXOA9Q3OlesqKUS0mGaeq8go1NDOLQDLBe0NDGq4giThebWf3U3pb43BKWHLYkDTCU1FXUy9r5Q2AivZU2UExDQXsTfRWv4K6jGrsgCg4cNcNMV2ItN_mQBZJgGgIQ9vVW_mnyVgLDV490FFpuCLdmf5Nvtk1E5mnuKyj712lflzz_Po8Poq0Z36GqlH7H_VO6v5SFszzbWHCt4bPVNETR68AQ7l5C3lbz9ROdQQkxb2VtRhfFcKwgir5Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2rDZG4kCQ-MknAsXv2RiTfSmuoL79g8yQCIZIMsuFpTXgY53TUJz4abT7EPqlJyP46SoDGVijSnmvGr0zjT4CKf7mwjMYSXLm1YhWChJXleaqkmSIKveboVbspxE9QOXeId97ACMLdOyehTXcVBwPMPgXo3GaACsyIowIF5zcxfUT2scn7dNAL5q_xOp_D4MJNTclnobOpV7BSMnOjDoSEdA_dWA6Z6xEL6nGlyusYyw-SrmbqGnB58xmM29lnV_ktzFYeshuRb9CP-OI-2wTWaoPDDOOukS7pq3Kv6PbtwmpIc3qtnAIzqHYMvyDbXYrKIQbgUamSTcW_lUpIZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSyo82-Mr7SGW3QkcEMWP46WJyuIzsMT2e8MuXtht2kJUzDUqO2FDUS1fNsmAgbAH5UM0S_qh5gMz2AkrGvbOZxXGrdlpfMGgl1rfwe_F4EeScnaLEj7pcSEqyvsTfOwYgmZRczKa8DcSK6awWm7doftLG9YvQWwCuh0qQc53t4FlP1rureaLJRuYYnPml9SOmiRBE6MUt7uAq14rwYr-mUHwNLqhIxngYmksbOIP3shJ7uouj5l8K_Q2Vdn3xgg9sOQL4ueUR5wQq4vIJFhdzrh0fqbwIriKdBDvRdwVI5__cZjezkFI7NUaBabGIqZjMRdRmE4LnjFb0DsCoRd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=W0KYnDTaLpju2gcY96DE-iXEX3Pbsi2lrBworGJav_IlOlqURuAbcSNvbPl6D2aWdDpmB-7MKvscXLv_RMjmogC7S17WO4K48tofGuP3IVqBp4Z8kfmclmrUSIB7uL7J-kTaJ9Bt6AFFUck8JhxvatzJw9Hr6E5ljlPyY7bdL12L3R1-NwBqgLiLmYft54fTyVk5W5ReDwofnUy08Hhy97j9gMfmdHKgjrp47sQzzWVsmfZxyefJe5uo1g3NahgaVJRRPgbR9OGWNoPQozEC0JoMZnWbbRZPvwCoD1u8baJFRTDdkqMY48EIe6ilyOs2_ibBCPmxpPQ0DVtrNhbrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=W0KYnDTaLpju2gcY96DE-iXEX3Pbsi2lrBworGJav_IlOlqURuAbcSNvbPl6D2aWdDpmB-7MKvscXLv_RMjmogC7S17WO4K48tofGuP3IVqBp4Z8kfmclmrUSIB7uL7J-kTaJ9Bt6AFFUck8JhxvatzJw9Hr6E5ljlPyY7bdL12L3R1-NwBqgLiLmYft54fTyVk5W5ReDwofnUy08Hhy97j9gMfmdHKgjrp47sQzzWVsmfZxyefJe5uo1g3NahgaVJRRPgbR9OGWNoPQozEC0JoMZnWbbRZPvwCoD1u8baJFRTDdkqMY48EIe6ilyOs2_ibBCPmxpPQ0DVtrNhbrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mntCqkQaZ1ZijqxT2Mvn3LpLvKZvWi0NXa3x4bgUNOm0hK510W7lehZ7Kql6lFnFb9lWv9hFHDgVRKVpLx4ZBVv0mocFj9-PXTzD8MjO7q9fG0XRdEF81btc7K3BI9q2ermP1x4UR2cJ3xn_AR9mFltzW3jm6b8uKjsW3nX-H-aUnAurMPDd7A8z18RZNmgZ4jSGnWqI-b_z6Yq3kEAxD7Iqk7EIVS1rQCrdYn6KCgfwAgofE76R-x33zNI_Xlu87jnmC6ZKmvClq9339pUUcyKLtUUAdEGipQleaJYlsIR56i4sAoyNlP8_wB2vRoSL1Pr6LDjcRbe35z21xuPiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=bPw-3Sn6TH7UTWldw-KgZiEncqEU6231qfcClyN-mBjsltyeeqXvXIuVwzJkmWyrD1GXOwqlzdoFYYDg2Cq1-iUQTEjiaJ9itJTsuHWLtgAVmaA9LLEijLCCZiJd5hSb6NY0wz3taFbjz4Gczn102GC1h-i_HtUjLSukRPh7Jf36arX8uypA40aH7bgGk0xAk781wS3EOANUfMdtbAJ-oTm4gLpyqfbzIIVCivEvg-gOVBdrF3tMsAk_sAXI7CKbWUfo9CMdKUaxAUmqf0akztNWc4dlllzt0qZnNHeiNBFZTBuwsvYmJErsvVsub0knnaUATCfX02xvvPlL9NHjyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=bPw-3Sn6TH7UTWldw-KgZiEncqEU6231qfcClyN-mBjsltyeeqXvXIuVwzJkmWyrD1GXOwqlzdoFYYDg2Cq1-iUQTEjiaJ9itJTsuHWLtgAVmaA9LLEijLCCZiJd5hSb6NY0wz3taFbjz4Gczn102GC1h-i_HtUjLSukRPh7Jf36arX8uypA40aH7bgGk0xAk781wS3EOANUfMdtbAJ-oTm4gLpyqfbzIIVCivEvg-gOVBdrF3tMsAk_sAXI7CKbWUfo9CMdKUaxAUmqf0akztNWc4dlllzt0qZnNHeiNBFZTBuwsvYmJErsvVsub0knnaUATCfX02xvvPlL9NHjyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=TbEDx1u9Z4J_YX3OnsfMH32kzCFgOdJxXRSnCelMfagbilGBVasHVyiDGGrN5hZl6yBpU3u1mCg4IW6FtXPD7RgJ3gWhQEdURf6YwNLs4Z_qTuWOyfrQlV7mUsHIIoEq68SmhiqdFA7twA6BCRTRoFp8HYevW8nYCx2FQrUywjXLGnFWcdinIHfSMWPOkWLd-ICaRIjiRFXhJ-9OTK16iteRmILwLVBSy51WFjPL7zD1rAi7O9XvtTzcmC327fzUTY1HnLWe1cCKoxjrGm-TYMARuFrLjhIhUOm8aehaSFMA9S8ACtmT3cDGD0drvuEXLS0a7tpfQZnx2_Dn74gU6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=TbEDx1u9Z4J_YX3OnsfMH32kzCFgOdJxXRSnCelMfagbilGBVasHVyiDGGrN5hZl6yBpU3u1mCg4IW6FtXPD7RgJ3gWhQEdURf6YwNLs4Z_qTuWOyfrQlV7mUsHIIoEq68SmhiqdFA7twA6BCRTRoFp8HYevW8nYCx2FQrUywjXLGnFWcdinIHfSMWPOkWLd-ICaRIjiRFXhJ-9OTK16iteRmILwLVBSy51WFjPL7zD1rAi7O9XvtTzcmC327fzUTY1HnLWe1cCKoxjrGm-TYMARuFrLjhIhUOm8aehaSFMA9S8ACtmT3cDGD0drvuEXLS0a7tpfQZnx2_Dn74gU6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk3BcFDcyouBZY6Uy6MKpTWYAnaQOAv3lfwC6RiquEUo7PDQNG2BTq4odNnndGjpcEeDtRvauxNPkcEJqajx0JlBPqOOCKV1a1BJmCt4W_XCwcfwHg_kDmlM0Qii9fYaaFWawBKKoG-nrQwrl-1e0T6rLLJdGJRcx3EfBQE94ZKo5vn_Vx7EoYfAkYktGueLVML7mSXkncWU-WKn-yzmwVlQ_4lfN-UPjFXpQXPQn0dDarCnCRtp7eRK1I0yOReNFtc2kRCt3JGuXxrQPJ_EIwf3kNMik6-z6ISurtx5WKJNuLaQUBvGZtYsrZWDlILK5TT8GC6BF_s7HPLOr2mIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXJK3w_ghCTzw7Y0pPdMobuFpr-DwCvB2JBJAnFqMW614FFzBlUr1ZvNDRwIcwU_Ypg21kAIjUO6y5fBoOw4rcUH8XObk4je8Ba6lEflVER-ue2heuQ8PHLWJj0tR7iBBjHE1TWV6ccu_nrmeJvjNpKbJOhgF_y47a4VJeRjii8Jsggvpi7BBGM3lzQ4OxgI6_BXjWl6uk6fOoaC8pzy-th8KdAEnlZLOIMNLBNFo69PAlFpEdZ7rS3nDlk7YORoVkWSPA05a-nJqjfrzR3tG_fmER7Lq91SYtXFJmS5Dz9SmgTp09eJUjDxehjAVg9YiKPH1kBbFo8KO_J8_jXg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
