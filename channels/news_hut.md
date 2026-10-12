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
<img src="https://cdn4.telesco.pe/file/ZhlkQFHyBR2iTjyGzrG5ckF4J7tIZcQgI9Tr7ZN9jtNe4do8MRda41UhnuMrnSMJKUza8e2WfNt7IRje7y0-HIcsd31ni7HPAFcHDgHRU4qncsNOBfspv-DiedlJ-bTw6zArkLl8QtHb8bRzihmrIWwMgOKmeABsm2RNHqJGwg4mPIdgz_PWhk1Cq3amIwQosozRj6Tl6BrGeV6jNKRXpYTZFadOmfGOVnYfNeIXbiN108rtenfr5AZBidc652wqnEyddGEplDqr-q0kvwvBN0zfXlQW64s5cv07osk2S2kfpxDERXL_LTVNoU-iHGiAlPoxyF50275GrkM0mlPgFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-73174">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtCELL68f85DlgQZErVtsop0pt3UeRsjovl9eqo-QN_OOWsMGWY83qWxa5LNklBQWGidGp4P446Cn55M9Ix_vTAh-AzTeQNMqxhORx5MxmtrkNUT_uxhRk_AQ4cz_jn25EuAgGUv_2TKsJvWIUq4P7OOqvQGnD1v8HJTjWz0h9qGLyQZB7kmle5m9AGR6rj4XuQ8D8yw5cd2r7c_nx4UaLxN0WB1TAYqgG9OG13B-ZI3hmb_02DtQ1-18uqaV-DRidaHjVipRJSpjhCFdPE_Cx-hpdsJd4P1JzGPjx63WtlHI9OdofaacXug_kHypcQp4l0g7wR4SmFz2QB-iyf6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار تصویری، اعلام کرد ۱۵۹ کشتی ایرانی در دوران ریاست‌جمهوری او نابود شده‌اند؛ همچنین مقایسه کرد که در دوران رؤسای جمهور قبلی این کشتی ها روی آب بودن ولی الان کف دریان.
@News_Hut</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/news_hut/73174" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=fyu6ydgb6NxSqvz3g3ddgbTI6VtR6ghBBo3hDcxATFzyn3V9HXaOhe3-2gTdBxRpT3UlbKI5LTFqYB-ZFAAL-lgmxv3L3IbnNZoIv3iD1Q6YpAE2Zr9PKoqhCeIQlvFv4Q4PG7-mtY94T4zTmUQkZSbQozwlzdsQ12wig-FOLHZ-1EmUJC1KarsHYqV4ad0giFuY6k5Zw6y9yw9ewCCOJyFEKMQWyTp7iibAvgxv_BZCRKg2TmLZ-NBOz6h5ugRFzcPTmV5JbO78bcNo3rU-w7IS1NUlmbSOdG7BIKbrGxX0PUh5-S7Nv2JcpSk_9hL-72mhBZw4-eFmWPDkY1M4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=fyu6ydgb6NxSqvz3g3ddgbTI6VtR6ghBBo3hDcxATFzyn3V9HXaOhe3-2gTdBxRpT3UlbKI5LTFqYB-ZFAAL-lgmxv3L3IbnNZoIv3iD1Q6YpAE2Zr9PKoqhCeIQlvFv4Q4PG7-mtY94T4zTmUQkZSbQozwlzdsQ12wig-FOLHZ-1EmUJC1KarsHYqV4ad0giFuY6k5Zw6y9yw9ewCCOJyFEKMQWyTp7iibAvgxv_BZCRKg2TmLZ-NBOz6h5ugRFzcPTmV5JbO78bcNo3rU-w7IS1NUlmbSOdG7BIKbrGxX0PUh5-S7Nv2JcpSk_9hL-72mhBZw4-eFmWPDkY1M4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سرباز روس تو خط مقدم، سربازای اوکراینی رو که از پله‌ها بالا می‌اومدن، با نیروهای خودی اشتباه گرفت!
وقتی اوکراینی‌ها به سمتش تیراندازی کردن، تازه متوجه اشتباهش شد و درگیری از فاصله نزدیک بینشون شروع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/news_hut/73173" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8047543035.mp4?token=v987uI4gViEQwo4oC5hQ7Gw9pPn6wT_w34qyzZGFPFBfhENhf8OaZhonF611MgeCi83ZIcrla0RoxhXdibMXusbfQUKryq-l1oXpr36FMUhLQ2FcvFJ54UUDWtY1m_yr2o1MVA2PmlDQIWPtcmgYhRPqYLIdS4TKdXce61uUh7ocFflV9CuexrR3i69PJGiJqF1FVuwt_9VqNdykeh67CQVmhXLfE4D2qTM4EL4fB-iWlZbQRoMRdVz2_TEQrydQgOnqfRyZccVR_h_myFJzzfy5Lu4clKBeNK-MqX0Au3G4vh8rOZdBi30lSPQ7xBZQpUe3_wpn3azVRIJltEvstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8047543035.mp4?token=v987uI4gViEQwo4oC5hQ7Gw9pPn6wT_w34qyzZGFPFBfhENhf8OaZhonF611MgeCi83ZIcrla0RoxhXdibMXusbfQUKryq-l1oXpr36FMUhLQ2FcvFJ54UUDWtY1m_yr2o1MVA2PmlDQIWPtcmgYhRPqYLIdS4TKdXce61uUh7ocFflV9CuexrR3i69PJGiJqF1FVuwt_9VqNdykeh67CQVmhXLfE4D2qTM4EL4fB-iWlZbQRoMRdVz2_TEQrydQgOnqfRyZccVR_h_myFJzzfy5Lu4clKBeNK-MqX0Au3G4vh8rOZdBi30lSPQ7xBZQpUe3_wpn3azVRIJltEvstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش علیرضا خمسه به کلیپ معروفش توی فضای مجازی(خلوت کنید آقای خمسس...) :
منم مثل همه شما یه آدم معمولیم. صبحا میرم پارک پیاده‌روی، بعدش میرم نون میگیریم و ...
بخدا من بادیگارد ندارم چرا به من فحش میدین؟
چرا به اون جلوییم که اون جمله رو داشت میگفت فحش نمیدین؟
@News_Hut</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/news_hut/73172" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/news_hut/73171" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9ABFIfj74x8n4d3WMIerwIRXIQ6zrgZB3gGBCzE04sG90rYhsgOO7SwKSl0nn8XelQWwLKjCJVXCt6lkGnI3qgmSuah-JVswj9zdnj88cM5BDqQm26p4S1rbskNVypTHCf6yQQ0MSZScTAqth7Z9JHWh6s5djOC3tBYJ2NcJPs54l58MS_0dzuqbcN6og_Pg5dKWpi55AqdljA8CT7to9ayQaz5QWB5-C71mN_qQ-TYJ1Ai4WXe_S5pXnzHfEoqibRsiGYkVrYrUa33A03qNtXg-koFEVT2Av8Y7Sgnk4l_7pdkOjE3GrraYSCfgvnD5pEZceNSsg5FJmlSFr47ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/73170" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#مهم
؛
اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید می‌تواند تأیید کند که حادثه پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
من می‌توانم ارزیابی خود را مبنی بر اینکه این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریباً به‌طور قطع توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است، تأیید کنم.
ما این تهدیدات را در خاک خود تحمل نخواهیم کرد. ما با استفاده از تمام اختیارات قانونی خود برای هدف قرار دادن شبکه‌های جنایتکار مورد استفاده ایران و همچنین منابع مالی آن‌ها، با این اقدامات به‌شدت مقابله خواهیم کرد.
ما تحریم‌های بیشتری را برای محدود کردن توانایی ایران و سپاه پاسداران در آسیب رساندن به خودمان اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/news_hut/73169" target="_blank">📅 18:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50742ac121.mp4?token=RGRYzidJxvV5LMpyQKaJJc6B3Zfe8m8z3s-K6a2gjEGABmAZtKVYEU8WIqNnKfCDwHmAxsVByGeO7Yqm_KHvR-AhsgUENK4vmUy7MPY6PMXO-a22dvuKg1MbsY6I-CvAUzeDLoOu3M_8791cmAYvWGT0C-6ICwsb9qgHPLJHa-X7_kYaKPjuQYnNEefJcPBaDdJrmqBCUbW6jExf4scoUVPiswV-h4mNJFZ4qY3ukrqzEIlNQexmHpHMO3zrXIZCYwM5TImxFnULzB72RNaMJTjrFWZNtywCFX4t8Qz9TfSUFmC5kW1SB_MboP0nQP6Uui9_sJrqa3KgEqIa25AYMr-18YFIpK_swYoGTmiYUE4Qh9k-Egb1RaMCmdnuk9MJ5XwlY85-hiMFIfp2A__8Expu6LUxQt5NAehmjBFx2yMQbFZKKREPJYnLZNJi_ns0fxfUgape8lv4GShF3tirubaiq9uTn5iVJAAV7xKF3Yn3virudJ2apZvFrpmktRtqk2aMjo3IxKsiXrVKAkhQtdMLtvmRbfKCe0hjiwMwvO1JmnD9nXSgHyxIIFLtjh9labvQ1WYGmCx82rDkr_oyexFbDx-W2NRz6EOs-z0dS7MEB_IEGDN3I3tPpewx_PIDA2cMTLQ_hcv9DYKW114YmNcND8u1D86dcE9lHroHyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50742ac121.mp4?token=RGRYzidJxvV5LMpyQKaJJc6B3Zfe8m8z3s-K6a2gjEGABmAZtKVYEU8WIqNnKfCDwHmAxsVByGeO7Yqm_KHvR-AhsgUENK4vmUy7MPY6PMXO-a22dvuKg1MbsY6I-CvAUzeDLoOu3M_8791cmAYvWGT0C-6ICwsb9qgHPLJHa-X7_kYaKPjuQYnNEefJcPBaDdJrmqBCUbW6jExf4scoUVPiswV-h4mNJFZ4qY3ukrqzEIlNQexmHpHMO3zrXIZCYwM5TImxFnULzB72RNaMJTjrFWZNtywCFX4t8Qz9TfSUFmC5kW1SB_MboP0nQP6Uui9_sJrqa3KgEqIa25AYMr-18YFIpK_swYoGTmiYUE4Qh9k-Egb1RaMCmdnuk9MJ5XwlY85-hiMFIfp2A__8Expu6LUxQt5NAehmjBFx2yMQbFZKKREPJYnLZNJi_ns0fxfUgape8lv4GShF3tirubaiq9uTn5iVJAAV7xKF3Yn3virudJ2apZvFrpmktRtqk2aMjo3IxKsiXrVKAkhQtdMLtvmRbfKCe0hjiwMwvO1JmnD9nXSgHyxIIFLtjh9labvQ1WYGmCx82rDkr_oyexFbDx-W2NRz6EOs-z0dS7MEB_IEGDN3I3tPpewx_PIDA2cMTLQ_hcv9DYKW114YmNcND8u1D86dcE9lHroHyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ اندی برنهام نخست‌وزیر بریتانیا می‌گوید می‌تواند تأیید کند که حادثه تروریستی در پایگاه نیروی هوایی سلطنتی «فیرفورد» «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/news_hut/73168" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73167">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=CFNuD3IfpailPPtVx-uXKUHyenjZo7659jzC5Z4jODHB5PyB6Y8BBbw47ygQjNXCKZnhxRRGMZCuofOVS1UN0KJbQdwHrk7GuzIA7QcGSwyAwSRnp2ocrxxDM99qnzeppImnxL1uurX7jF00Krtf2O3K5W9H8GF5VqRHh1jcx61VJlEFvTA2WTZRTDpRq6fD32nWOqXf-bYaeorom9UQr88SvcTmnyu8jUsIpnmGFzlaF4jDuGUmYVml0sv4c0yigADxwZGPyw2W13wDacV0Pk_uY7cHyU0PrMYphzVPh_bUCtmf2G2iBQF7QTmsSHX3pL2Fr6z6jKW-iPP8bv69mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=CFNuD3IfpailPPtVx-uXKUHyenjZo7659jzC5Z4jODHB5PyB6Y8BBbw47ygQjNXCKZnhxRRGMZCuofOVS1UN0KJbQdwHrk7GuzIA7QcGSwyAwSRnp2ocrxxDM99qnzeppImnxL1uurX7jF00Krtf2O3K5W9H8GF5VqRHh1jcx61VJlEFvTA2WTZRTDpRq6fD32nWOqXf-bYaeorom9UQr88SvcTmnyu8jUsIpnmGFzlaF4jDuGUmYVml0sv4c0yigADxwZGPyw2W13wDacV0Pk_uY7cHyU0PrMYphzVPh_bUCtmf2G2iBQF7QTmsSHX3pL2Fr6z6jKW-iPP8bv69mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که طی دو روز گذشته به سومین سوپر نفتکش در تنگه هرمز حمله کرده و موجب آتش‌سوزی آن شده است.
سپاه پاسداران اعلام کرد که این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه، سامانه ناوبری خود را غیرفعال کرده و به هشدارهای مکرر بی‌توجهی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/73167" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73164">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1oBPqj6SaIqbUsqLBUi-xK4Q3Q7F7h8_Ove1LUg9alkioOhCuAGQblHWTCS88bWrj5Z-qfJHZxO54j8W-I7ra2rYvpCp63ZY4VfhD_6OO17yZrlbN-lleEX-dL6xuJ1J8wUaX1jUUBf7k6f_4CwlA4-yaxFK-hSd_kUVaBcSNu-8BeBivh_TyzDoVJTCAD6fCSq75wW0NGp4hQPb0jtElUuE9425RRdhOVqdMiyxoNJpe5WnOFZjhcotnaT-CrlYSk6dY3xe2pYUjbCGJCgc3KCb0bZcezKQY1DVx70nkg9VrArREDKj50hOWRp8DRLZlEQ1zCn1kU81eti9slF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LncsvKZMmfDgStvo650nOBe2JvX9OMn4b8IFa914aJO6YWc4T27Ryc3g-wPFa-BEAIuIP77CVNav21-c5-pl37_Uiiy5xv0UPsEEEull4gISwVbmqkBx3l9rQBHmEj2XSLFnULh1qS_HdEF2usxtT00gVFoh1iu_VWVOFVSTBNb7UHjEgL0L7RP3t8R2VRLOj_PAYe7D-xprvzbfeUMlyH6UBtkCZ4qBQNGBJMEtOAkflsMSJXbICliZ03hQ1CmKvqj8-9lwvLPIPZ1KWTCSEXRw0bB4n52tCFIoJPWXUlqr3l6O6PPdIJaRMFplUs6dFwjQ7F9nk1eY6KLC6IPBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4sNoK29wej7nln_KQZoKqsHfoRsErNqJdxvfJe05_EI6HF3rL_HDbRKv101bknLS6-DuImi7RPT2zmoQck1gs1bey0DtqHvekFjFT7lrXxrUT8Qe2xYyW6N8nqhFCUEGrqTSLPS5lc7ItuvSBLC-yAamo4YIAPJV1fEPRXDqMx1yHaGqOY7K1ETrCEXA1Uygny5yD6Rg42XukBc3SsGqvOUfwMm6_Wej7BL1ljHkrftKf2hRo32acVoK646qWmPnMplTeHGa4SxCUlYquqKX0tDppNoQK1doUS51QbYhAORtRF4plwoeeu6kCiTOFhHnPV60WhIdayydlCeIsh7uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آزمایش موشکی سپاه در یزد:
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73164" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73163">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=k-igTRzNuMrHAwZE4-Vh2dUWCFHuhEPFG-Nce_KAtXBRBy8oL2KEKXweYMuMn5iUm94Epbf-YrAjyY2V6ygJ98HiIUHsEO_P5w33d5ffSa_9rD6XG3byj8W2QrwM3sXY50ohm8FrriTQn0NA5HoDQH-fqEW7oHvvQE_bU0ITi5lB3xZouO6q8ZH4vCpvnYNeZ9yo4CnikKKcplqbeWXoKa4NqkoXLWcDphO5EjiDbfIzWR6lY-Yueo14nCK3K7zo6knH2mYJamdB0GErtTZGYWgOkAAquIbjk0_9S2cx_TBNpNWqYYe2t7fJkmnTpfRzWe4brFwqlXTFVWBmC8PPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=k-igTRzNuMrHAwZE4-Vh2dUWCFHuhEPFG-Nce_KAtXBRBy8oL2KEKXweYMuMn5iUm94Epbf-YrAjyY2V6ygJ98HiIUHsEO_P5w33d5ffSa_9rD6XG3byj8W2QrwM3sXY50ohm8FrriTQn0NA5HoDQH-fqEW7oHvvQE_bU0ITi5lB3xZouO6q8ZH4vCpvnYNeZ9yo4CnikKKcplqbeWXoKa4NqkoXLWcDphO5EjiDbfIzWR6lY-Yueo14nCK3K7zo6knH2mYJamdB0GErtTZGYWgOkAAquIbjk0_9S2cx_TBNpNWqYYe2t7fJkmnTpfRzWe4brFwqlXTFVWBmC8PPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین اصابت و انفجار ها روز ۹ اسفند در پایگاه سوم نیروی دریایی ارتش، کنارک
؛
در این ویدیو ، یکی از پرسنل که به ناچار و طی غافلگیری به اطراف پایگاه همراه با هم رزمان خود پناه برده بود، می‌گوید ،"جایی نداریم ،فعلا همین جا بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/73163" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73162">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/73162" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73161">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiKCPSbNbf2Oxz7_bdJ6hT-0TmqhUrcD61hzt-RsWwXhuJRWINE3mmd_4oXZqiZSkxIBfXF_V7TH3Rl7BVgsnVuDnmt5nKO1Lhj6G8EkMJxMPW2FhPJIbHN6ZBD1XQA1OS43jqvV4qySepk0Vnil3ab4xfCQMzv6eKdoRnf-BO0wS_uWB7q8y1_MImI7JHmqVHdTQFzhH7Z-Esc_800SX4-RFAHTrcZDCUm9oALWgE9xkgC6G3KytYwPgMQVc5wRiSmbCx8pKUTCLD47VriP3ViYp2LPJeqTm2qjbMayAQ_4LZS9rGQw-_cjAyYXA6viQ3qCxmemEAES9D7uuuoR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/73161" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73160">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش اسرائیل در پی وقوع حادثه‌ای در شمال این کشور که منجر به مجروح شدن گروهی از کوه‌پیمایان (که گفته می‌شود معلم و دانش‌آموز هستند) شده، وضعیت «حادثه با شمار بالای تلفات» اعلام کرد.
این حادثه احتمالاً ناشی از برخورد با مهمات عمل‌نکرده بوده است.
گزارش‌ها حاکی از حدود ۲۰ مجروح است که وضعیت برخی از آن‌ها وخیم بوده و یک نفر نیز نیازمند عملیات احیاست.
ارتش در حال انتقال مجروحان با بالگرد است.
نتانیاهو حضور خود در برنامه تلویزیونی «The Patriots» را لغو کرده و در حال عزیمت به محل حادثه است.
فردی که در وضعیت وخیمی به سر می‌برد، اکنون جان باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/73160" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73159">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=uxZ4LKo08VJKuVM6cDhbYwG7MpUj7xgAvKzsdZEJ381Tr4JwV32XAfrfIVJ8rXw9V-UvlmfMbk5fTexKpJsZqzEGnil0tqFkaSbm9IK9KaIUCmgfbDjUlEJ3jcBnWajvzewFC3McIVixto_vrf8l7U8l2ZASUPvY-YGodmlz0Ulme4Xnu8A6qD8ZCQSMLqFjcFBWiJisygZwUdJcSrMzE-BX8Xc1A-XL5N3MHoJRMZippLHHqGgL-hCe9tGd6jUfMNMvYumk_6cQBAmIPg0m-UK-OhxVf3vvRwA-YSMX2lqWMoJhFJrk4-fBYyNA6Qr-C8eX50RPRsDgtOx66cOQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=uxZ4LKo08VJKuVM6cDhbYwG7MpUj7xgAvKzsdZEJ381Tr4JwV32XAfrfIVJ8rXw9V-UvlmfMbk5fTexKpJsZqzEGnil0tqFkaSbm9IK9KaIUCmgfbDjUlEJ3jcBnWajvzewFC3McIVixto_vrf8l7U8l2ZASUPvY-YGodmlz0Ulme4Xnu8A6qD8ZCQSMLqFjcFBWiJisygZwUdJcSrMzE-BX8Xc1A-XL5N3MHoJRMZippLHHqGgL-hCe9tGd6jUfMNMvYumk_6cQBAmIPg0m-UK-OhxVf3vvRwA-YSMX2lqWMoJhFJrk4-fBYyNA6Qr-C8eX50RPRsDgtOx66cOQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو ماه پس از سیل ویرانگر پیشین، نپال بار دیگر گرفتار سیلاب‌های شدید شده است. این حادثه خسارات سنگینی به مناطق سیل‌زده وارد کرده و بار دیگر زندگی ساکنان این کشور را تحت تأثیر قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/73159" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73158">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=h0eGiiIUlUkTctDrBGsToZJF5WUuvWVjaji7uqRII8NK9SnItL0hSX4fwxlGsTFriCyLail-pw_4Ik6QpZogEz88wgRx0xd2lXN32FwJl4X-_iLy0Kau5b5LaA67wyP6mtPOfA0OcU_a5qtuhAeeM0fHRuRxAZflp7DVjjb1E4vuN0ookmM-oKAJA8p7p2Rtv1kAmwJsEtblt5RUz4AiGKDJI4AQiPfs2iN6-m5GFG1-4WG5tYEX5tDl47v10cLMeLClwpNcAdPqxJYM89IQTQoYxr3d490pvuz6MTTjDvFttTEEDAYzHq-2vGRiHBm06LGTcCk0ETjJxGgnyzp3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=h0eGiiIUlUkTctDrBGsToZJF5WUuvWVjaji7uqRII8NK9SnItL0hSX4fwxlGsTFriCyLail-pw_4Ik6QpZogEz88wgRx0xd2lXN32FwJl4X-_iLy0Kau5b5LaA67wyP6mtPOfA0OcU_a5qtuhAeeM0fHRuRxAZflp7DVjjb1E4vuN0ookmM-oKAJA8p7p2Rtv1kAmwJsEtblt5RUz4AiGKDJI4AQiPfs2iN6-m5GFG1-4WG5tYEX5tDl47v10cLMeLClwpNcAdPqxJYM89IQTQoYxr3d490pvuz6MTTjDvFttTEEDAYzHq-2vGRiHBm06LGTcCk0ETjJxGgnyzp3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی عجیب که از اعتراضات فرانسه وایرال شده؛
مردم تو یه میدونِ بزرگ با جمعیتی زیاد جمع شدن و درحال شعار دادن هستن که تاچشم کار میکنه پرچم فلسطین دست گرفتن و حتی یه پرچم فرانسه هم دیده نمیشه :
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/73158" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=aJP_DKVXufidlkD8UoHkXtP_miYngGYh2p7zFP0R4bpNvhXYggfZjFiIWc1aO6WUvUIkBOJA47mQAhntBIm0LTo-vckL5_OyjZ742Kksx4eY7LFjsdSrfGIc6HhjdUoOhptmXw9KDcWts_jbMSNmaw8X0OlwY157p_Nzu3OSRBMeQX-Wbk3FTkp8C5DqTkq_9A5n7X4rSOsYLWHCNyMBr5LkBlCKheGiMszKYRJme3xUM_0Ekqu2cE5ZcDT-S1882ZeQ3L5EtjuhrRmmqTfOAqmipVoCNah7FkTVjIstKC9zon9gC8dZCbBei3tEV65UVx9-75IkI-1XsWCiNmr9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=aJP_DKVXufidlkD8UoHkXtP_miYngGYh2p7zFP0R4bpNvhXYggfZjFiIWc1aO6WUvUIkBOJA47mQAhntBIm0LTo-vckL5_OyjZ742Kksx4eY7LFjsdSrfGIc6HhjdUoOhptmXw9KDcWts_jbMSNmaw8X0OlwY157p_Nzu3OSRBMeQX-Wbk3FTkp8C5DqTkq_9A5n7X4rSOsYLWHCNyMBr5LkBlCKheGiMszKYRJme3xUM_0Ekqu2cE5ZcDT-S1882ZeQ3L5EtjuhrRmmqTfOAqmipVoCNah7FkTVjIstKC9zon9gC8dZCbBei3tEV65UVx9-75IkI-1XsWCiNmr9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "
من میرم بین ببرها، ازم عکس بگیرید!
"
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/73155" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e5000591.mp4?token=L0g9JUVD908qIezQgOmPnQzjhg53a5IK5ImnZ0Da1XMOam5m_LtzCjMC7BLs7uXg5p5dV9ixToPAnUM1IrUSJkJWQDYklkhKlcoug6YtM-rKQvsNPeYa8ZhiLzmCf4vg63DWCKRro5MG69KK4CuLQUe-pjdrlXOJOWDv5nlf5KnRIRcQt4hp3_TKWRNZBBbD_Spdm1U8-9OTqwlt5FD7pZApOTVz6LOYfO2-KnUudu7DAgDYogLit5QOtXDR-wvhBpgxzV3Ut34ahmQALa3Lfb2PHv7Rwre-DDLt9T2hNOLAlOznVEjf_sOPijJrMXCh0R7msdHr8HmXBrkPhrO-ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e5000591.mp4?token=L0g9JUVD908qIezQgOmPnQzjhg53a5IK5ImnZ0Da1XMOam5m_LtzCjMC7BLs7uXg5p5dV9ixToPAnUM1IrUSJkJWQDYklkhKlcoug6YtM-rKQvsNPeYa8ZhiLzmCf4vg63DWCKRro5MG69KK4CuLQUe-pjdrlXOJOWDv5nlf5KnRIRcQt4hp3_TKWRNZBBbD_Spdm1U8-9OTqwlt5FD7pZApOTVz6LOYfO2-KnUudu7DAgDYogLit5QOtXDR-wvhBpgxzV3Ut34ahmQALa3Lfb2PHv7Rwre-DDLt9T2hNOLAlOznVEjf_sOPijJrMXCh0R7msdHr8HmXBrkPhrO-ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با نیسان از اصفهان راه افتاده و رسیده به پلیس‌راه سیستان‌ و بلوچستان؛ اونجا مأمورا بهش می‌گن می‌خوای کجا بری؟ می‌گه ایرانشهر.
مأمورا بهش می‌گن مسیر خطرناکه و توی جاده احتمال کمین گروهک ها وجود داره؛ بهتره صبر کنی چند نفر دیگه بیان تا باهم حرکت کنید، یا بین دو تا کامیون راه بیفتی تا همراهی‌ات کنن و به ایرانشهر برسی!
+
گنده‌گوز منطقه حتی نمی‌تونه امنیت جاده‌های داخل کشور رو تأمین کنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/73154" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tK-9RWk-OLRk_ceXGOfavi3KELOYdEnY6B9GjMl8JIVM5ENF1lKa-AhrkMXGdgMWNc8ydbHKyftSz1uwnZISXmg1cVpHxO706ud6g6y8dBW2NQTpaLt984CIpCtfYZqlgAH7AgrPA3HbxVnLpIqhmZN-cuI7TtBHqaBrdoZZdK6JZzTL0blWbMIG85JF7-mbpZf6CTPcx1pfOP45Q-s5Lo2RewiMW8yQT0B5UOIlsqwWR6TNJyRGegiuaLbvQRT9wjSrWPQpuaY-b39rj51MWLY7kvyfO1UiRQTbU5hCE7BG1Qz5QLMvyx-tEV75oSlt4Lu_ZDaEY35KB74o-9pgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر به هوش مصنوعی گفته هر چی میگم، در جوابش بگو جمهوری اسلامی.
بعد ازش پرسیده بهترین حکومت تاریخ ایران چیه؟ اونم همچین جواب شاهکاری داده:
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/73153" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=Rg-IN96pnVONF4E_pCDoxBCqYsPB44kbeLd3zbxob67wPeRw6eVGBs3Djowko57mtIsSmzF6qk1ljyU8Tn7H57xD3NGedGA5ejlse8kyjBVhtrqrLDXXqgUZ08dqE8oAuACgihSsxuJvhy5AzswKmh-1FE-Lprvh9p2ZpOpEmM7w59MYPYY1RV7W6LZjfkktpfkxNe0vvAYF66KQNdsFsOf8mxZg-qbQJzGUW9lMDWhZpeMjTHtk1ncoeJ4TrB-8lDONyeQGQ4tshJxbnoZ-dOH6ygWZYiELr31kdBkFJ0a1_dSzmqn0C1VZpnTTgYg5iaT4k_ph-F1bvtAA01wh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=Rg-IN96pnVONF4E_pCDoxBCqYsPB44kbeLd3zbxob67wPeRw6eVGBs3Djowko57mtIsSmzF6qk1ljyU8Tn7H57xD3NGedGA5ejlse8kyjBVhtrqrLDXXqgUZ08dqE8oAuACgihSsxuJvhy5AzswKmh-1FE-Lprvh9p2ZpOpEmM7w59MYPYY1RV7W6LZjfkktpfkxNe0vvAYF66KQNdsFsOf8mxZg-qbQJzGUW9lMDWhZpeMjTHtk1ncoeJ4TrB-8lDONyeQGQ4tshJxbnoZ-dOH6ygWZYiELr31kdBkFJ0a1_dSzmqn0C1VZpnTTgYg5iaT4k_ph-F1bvtAA01wh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دوربین مدار بسته از لحظه وقوع سیل‌ ویران‌گر در شهرستان گرمی اردبیل:
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/73152" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=GXjjIA5QTLGAz3WkkAcALGtgN65-PZF_0gjx6J8UUvAEdqbiCfHcoLhLHQUEp7A_lL_cMxoGVfpW6kUg-9i5Ux5BJv7dAnoM3aaPqRVTjM7-K6w_vgO6LkBEOdEVoW13XPyphUH8vEMhBKSuTaAsG8vHqju58rKkFOiBPyWYF0yFjYI6B1Ik9S5Q8BCXiAAMZe5kKs60pkyQSuVHtkUQ8Jx0vzo610-wJ_seZzm4pxzL1UR6dN31j1y3TS0CtWk8JGmX_JJoYncjYtnu-Vk9jFP65Dk2PWjiDIfdBFbNopoRTfzngC4H4-d77Z0SynO1rMr418AF83TMIGoDuOnAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=GXjjIA5QTLGAz3WkkAcALGtgN65-PZF_0gjx6J8UUvAEdqbiCfHcoLhLHQUEp7A_lL_cMxoGVfpW6kUg-9i5Ux5BJv7dAnoM3aaPqRVTjM7-K6w_vgO6LkBEOdEVoW13XPyphUH8vEMhBKSuTaAsG8vHqju58rKkFOiBPyWYF0yFjYI6B1Ik9S5Q8BCXiAAMZe5kKs60pkyQSuVHtkUQ8Jx0vzo610-wJ_seZzm4pxzL1UR6dN31j1y3TS0CtWk8JGmX_JJoYncjYtnu-Vk9jFP65Dk2PWjiDIfdBFbNopoRTfzngC4H4-d77Z0SynO1rMr418AF83TMIGoDuOnAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر:
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73151" target="_blank">📅 13:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=s3TjaK9UZWWYoZgKh1LUL7Ap4acanU4fRbaN9tCBSg46Dm6y0wpL7jCCpJnV2z5vCx0cBnSt_Qg2JmKTGzTyA2TZ4JO9b_mFiMCTZfG3oXGI3pDn9KgmJiy8SdeRCvtrAXdZGU2qeq2O-IyLMApUehHWCCDmA0_FAKSxAGkafLYSjSZVrAL-wZgXoqJH8PZksixjq7Wjrw6rlRl83lt92X6Becy1Z4rX0cVNXVdhEc01vwMl8Vlf-CCUiKhHILu2nrXfN2B_wHorCk6AAOxxLhrpYGuwcLURNsEYRRbsPfeZRIs4lSLteLgUn7e19OYktAwyArZP1fMBvPXFJxueCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=s3TjaK9UZWWYoZgKh1LUL7Ap4acanU4fRbaN9tCBSg46Dm6y0wpL7jCCpJnV2z5vCx0cBnSt_Qg2JmKTGzTyA2TZ4JO9b_mFiMCTZfG3oXGI3pDn9KgmJiy8SdeRCvtrAXdZGU2qeq2O-IyLMApUehHWCCDmA0_FAKSxAGkafLYSjSZVrAL-wZgXoqJH8PZksixjq7Wjrw6rlRl83lt92X6Becy1Z4rX0cVNXVdhEc01vwMl8Vlf-CCUiKhHILu2nrXfN2B_wHorCk6AAOxxLhrpYGuwcLURNsEYRRbsPfeZRIs4lSLteLgUn7e19OYktAwyArZP1fMBvPXFJxueCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی:
«بلافاصله بعد از پست ترامپ در تروث سوشال، روسیه حمله‌ای هدفمند به یک نیروگاه در خارکیف انجام داد.
معلومه که پوتین تروث سوشال نمی‌خونه!»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/73150" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=FCnYKe-cMM1pulqdZWJixCC7gUtnM0BJEJMjzg7xGqHOyOwsnPlMy4204J1ZkV-ICUQXLywvvwurXwJ03OLl3XlCgqmHn_DETED-wCI_FR6-d4yIUIp_dpmeHd1F6b_lJhCAzQVsJNWqK-IIKk8HIVG-BRvPRW3ASRYoSSfRfnNYyR-Bi0QMxUB8D7zJGPl_4mfrsj6jaGq9FD5zFIqrUXn-TJDuMzCJ71BHU-dUPsQHbXrY1TelzPNormXb-PmCM3gImu-Olr74o355hRq1Va9zxENCChOqRDSf0_FEZx9uNLGpmsqZbxTOylVKcqDjPnolXxrFYvoCXdBNulgzYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=FCnYKe-cMM1pulqdZWJixCC7gUtnM0BJEJMjzg7xGqHOyOwsnPlMy4204J1ZkV-ICUQXLywvvwurXwJ03OLl3XlCgqmHn_DETED-wCI_FR6-d4yIUIp_dpmeHd1F6b_lJhCAzQVsJNWqK-IIKk8HIVG-BRvPRW3ASRYoSSfRfnNYyR-Bi0QMxUB8D7zJGPl_4mfrsj6jaGq9FD5zFIqrUXn-TJDuMzCJ71BHU-dUPsQHbXrY1TelzPNormXb-PmCM3gImu-Olr74o355hRq1Va9zxENCChOqRDSf0_FEZx9uNLGpmsqZbxTOylVKcqDjPnolXxrFYvoCXdBNulgzYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بیکارِ کنجکاو رفته بازی Resident Evil 4 رو روی نوکیا N95 دکمه‌ای پیاده کرده و همه رو به تعجب وا‌داشته :
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73149" target="_blank">📅 12:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=FGicMDmqC2G2kFO-CgYL1MORZsiGGwCh39JD-3MyK08Dk-8nf2VomB9xhv6yZpA3m811kNl_55JK8ocrJsphyyHve01hgcTklm_f1CcImOsPfABthcEY7zPZOFQczXMSKxvZr1tIBnb_Jad-_9WpgU_iV4tA12cP2FL08oKYAgv1i5R3E1o7_hHOm8ey-dRgSWh8mrH0MEttJis9yqjwtP-ukbbWAO3SPkWjkGolSnZJ0TXFguXf6A62-zooXsXm_uvTPIVf6eQU9xLUL9TYMzEN1NvsvkiEmT4GD7in7MdrcXuBMZUJaCLiYxXtCjOqbAHtqkZCOeIXstdMEQPFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=FGicMDmqC2G2kFO-CgYL1MORZsiGGwCh39JD-3MyK08Dk-8nf2VomB9xhv6yZpA3m811kNl_55JK8ocrJsphyyHve01hgcTklm_f1CcImOsPfABthcEY7zPZOFQczXMSKxvZr1tIBnb_Jad-_9WpgU_iV4tA12cP2FL08oKYAgv1i5R3E1o7_hHOm8ey-dRgSWh8mrH0MEttJis9yqjwtP-ukbbWAO3SPkWjkGolSnZJ0TXFguXf6A62-zooXsXm_uvTPIVf6eQU9xLUL9TYMzEN1NvsvkiEmT4GD7in7MdrcXuBMZUJaCLiYxXtCjOqbAHtqkZCOeIXstdMEQPFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیسکو مذهبی هم آنلاک شد و توی تجمعات شبانه یه رپر آوردن و حامیان حکومت دورهم میخونن و میرقصن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73148" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73147" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/73147" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4gngzAFo1VolfV06vg5pJ7xsYi1hq2kZKhHJueHxSWT-4Ry-YriFwZ-Q1BHIvWUbKFK0u_aAVJF2RY7Kwc7xDKLfJUBgpmDuKmvKiYWG39Kx2bn4Y64BozGGApL3KD_9m1nGsvrhKesTv_YPrJ-FrF2T4cV5Au2hsmuHTDqSvXdRxEeKeGgUrxNC8E0O5G67es2L4rhG9nz76f1HVOlv835h4OnNhWg4eFYki3vKapsF_UVLmlbn7KTvGd9URfqpzXqJfVlBJmNRp5XZG7-NyuORjFL1VGnA26QZILfo2cR_OKDX774SmenVABTHfEQ-zOxMVxI4KlW-oaVGnixeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
کاونتری
سویا
🆚
لوانته
ونزیا
🆚
آتالانتا
اودینزه
🆚
تورینو
نفتچی فرغانه
🆚
النصر
استقلال
🆚
الغرافه
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/73146" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=Ww34UNk0bMTxNJP2GF6B_whSu3mBmlX-O2vw1BQIHMSFsivNnmTUbFX40phELFz22czWVq7aP-qjTtxbjDGjVEsJRa3z98T_oOKP3HKhSCalBItOeuHBA7wKpQFSz_vKIKRlZ8s0qLLMPQJkfsbfvLOv7nXyjI8QHWWWd3veaju_FNzVhU0tSdLyVtOFGuIy0HnrNmF6rN6IGUPDfShjeBVknepmdBjHz3DGsXNsqgKxtR2owSThafuwuCCICDLdS6_dxijROvS3COU9_B6eC2zsGQxcd8V5D58MI5Ff2lchUH05CucZ8P78_bQSHHSmtbIFDgmbkJeRbk1HTqjVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=Ww34UNk0bMTxNJP2GF6B_whSu3mBmlX-O2vw1BQIHMSFsivNnmTUbFX40phELFz22czWVq7aP-qjTtxbjDGjVEsJRa3z98T_oOKP3HKhSCalBItOeuHBA7wKpQFSz_vKIKRlZ8s0qLLMPQJkfsbfvLOv7nXyjI8QHWWWd3veaju_FNzVhU0tSdLyVtOFGuIy0HnrNmF6rN6IGUPDfShjeBVknepmdBjHz3DGsXNsqgKxtR2owSThafuwuCCICDLdS6_dxijROvS3COU9_B6eC2zsGQxcd8V5D58MI5Ff2lchUH05CucZ8P78_bQSHHSmtbIFDgmbkJeRbk1HTqjVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف رائفی پور به باز بودن تنگه هرمز برای همه بجز جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/73145" target="_blank">📅 11:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=uFafFi4NaaKZOB2R30X3EX5VF4XzLEeYeSyNBxckaduzC49mW4tkFbCyYv2DHrnFgqzx57qRZMb31X71SbEG4ZNjgjSix0swMQVL7d-eZL0NgtT04oMjC4qy7U5m0A07EbJLNZUDPSqo1dMVgVXr-6kM4TVa5HA4xxxw2oBMj-cu9-2p60r6wiBqdyntn8pDiv2v70bNuWF5bQ-84hUutYrLVlbAyuREJs-C--TRU8hRvZMH8PdDb5SgTtQOiQv9ykeV2b5HIv6qHZT_CwqKB278T2FdxPa1NZLRdQtqVFALVnLAJkJsEGXBSkW_ifnNZHb5l7LGPyFnBG4CBHWS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=uFafFi4NaaKZOB2R30X3EX5VF4XzLEeYeSyNBxckaduzC49mW4tkFbCyYv2DHrnFgqzx57qRZMb31X71SbEG4ZNjgjSix0swMQVL7d-eZL0NgtT04oMjC4qy7U5m0A07EbJLNZUDPSqo1dMVgVXr-6kM4TVa5HA4xxxw2oBMj-cu9-2p60r6wiBqdyntn8pDiv2v70bNuWF5bQ-84hUutYrLVlbAyuREJs-C--TRU8hRvZMH8PdDb5SgTtQOiQv9ykeV2b5HIv6qHZT_CwqKB278T2FdxPa1NZLRdQtqVFALVnLAJkJsEGXBSkW_ifnNZHb5l7LGPyFnBG4CBHWS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی، مجری صداوسیما که سال ۹۸ گفته بود «مملکت مال حزب‌اللهی‌هاست، هرکی نمی‌خواد بذاره بره»، طبق گفته محمدرضا باهنر از ایران مهاجرت کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73143" target="_blank">📅 10:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=Ueqn-lv8OIUAccCDlcX5G4zua2BWHdTgoBbxGbip4RsKZZKuuMJduAEgecGuOBjgHjDaL4ycQQp24NMTkgeGTNEecSA-ZEOlnfCg5SiLK0AXnMoi7NU2-QNF875cC8Vns2SlBQTDe2z7H8vwRWTy0u0kseEIcyxwfmCKontR0dbwKSXJ5dTEep4WOyh_YYM-fGglVEXvN_psgaBrTbXkCT3Q3PYNRfrY81syCsn-cWMtJ14mi5Uhaf1sd7qHAwtUQ56gJl7gnBIOjdLXg5zTSSlgF5GO3gYZr_7g5mxfrNZXwwukqt0eD-tDj1dgMSQrxLQ8kVvSvQf2ro76vV3kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=Ueqn-lv8OIUAccCDlcX5G4zua2BWHdTgoBbxGbip4RsKZZKuuMJduAEgecGuOBjgHjDaL4ycQQp24NMTkgeGTNEecSA-ZEOlnfCg5SiLK0AXnMoi7NU2-QNF875cC8Vns2SlBQTDe2z7H8vwRWTy0u0kseEIcyxwfmCKontR0dbwKSXJ5dTEep4WOyh_YYM-fGglVEXvN_psgaBrTbXkCT3Q3PYNRfrY81syCsn-cWMtJ14mi5Uhaf1sd7qHAwtUQ56gJl7gnBIOjdLXg5zTSSlgF5GO3gYZr_7g5mxfrNZXwwukqt0eD-tDj1dgMSQrxLQ8kVvSvQf2ro76vV3kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای این خانم در مورد کادوی روز دختر و گل‌های چند صد میلیونی که این روزا بلاگرا به پارتنرشون کادو میدن، حسابی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73142" target="_blank">📅 10:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479627e865.mp4?token=DRa3VWv0ekRBq716G8NptdbDDQNVpEwHRiwRglLvhbnAghJBd3UdRDkCcb-5nnPumXozfOHSsPrbSoyl-ss3QT34ueH-FkEz5aIDQGQhQXX4OIrL8yst8KaojEPP1CejOdAtxw6DkOGHZvQ16CfmnuhSuyp6TW67TgLfR-zQb0ZYCO9B39VslwXCSXiN_Q1Hh5OnYpas7M0MBTQS80Hrj63ofGpe54kDWzr4z_h7f5s1hSXKsITStsRIKnR932esIUCzwHTFSjKioeIEFZhr_jJGomfXUDxCgpxw7XQaCpKtaPT7NKPF-vkZkrZKDm7a_97DTFyEzQw5WztrNRICZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479627e865.mp4?token=DRa3VWv0ekRBq716G8NptdbDDQNVpEwHRiwRglLvhbnAghJBd3UdRDkCcb-5nnPumXozfOHSsPrbSoyl-ss3QT34ueH-FkEz5aIDQGQhQXX4OIrL8yst8KaojEPP1CejOdAtxw6DkOGHZvQ16CfmnuhSuyp6TW67TgLfR-zQb0ZYCO9B39VslwXCSXiN_Q1Hh5OnYpas7M0MBTQS80Hrj63ofGpe54kDWzr4z_h7f5s1hSXKsITStsRIKnR932esIUCzwHTFSjKioeIEFZhr_jJGomfXUDxCgpxw7XQaCpKtaPT7NKPF-vkZkrZKDm7a_97DTFyEzQw5WztrNRICZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه یک صداوسیما:دانش آموزان معترض فرانسوی، می‌تونن بیان تو مدارس ایران که همگی فول امکانات هستن، تحصیل کنن.
شما هیچ معلمی ندارید، پلیس هم داره دستگیرتون می‌کنه.
ما اینجا کلی معلم اضافه و کلاس خالی داریم.
اینجا ما آرامش داریم و همه چیز عالیه.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73141" target="_blank">📅 09:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=vV3esPAiWzNnbTHW5VXADMLXE95QdI6UeITtcMZDvzoOfvwcDeJvuan_J9FoSxNGNAwXu0JGWj1jKdonVJZ16z6f9u_SWU77WS841ENDCyfrbZ17tYftLZoGgRl-4yzg09AWvUwCtXbaf46W4T8Y2X6CBqm_yeBHrRi28o3OCu7w7rhnNB4tePQipWKKISfST92XmMykEqtnkuqg4WWjSG79BuRqGmaGpOtihHfvxnZbZu7i4F5-sZOWOvgb1siHS04mvwrG8YEZytDskBDxAQgdzdlBqEGq1AmsF434yYYXS3-FijQk6vAKMDSJ8xfXK0tHZMqx_tOJgy58PU9nXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=vV3esPAiWzNnbTHW5VXADMLXE95QdI6UeITtcMZDvzoOfvwcDeJvuan_J9FoSxNGNAwXu0JGWj1jKdonVJZ16z6f9u_SWU77WS841ENDCyfrbZ17tYftLZoGgRl-4yzg09AWvUwCtXbaf46W4T8Y2X6CBqm_yeBHrRi28o3OCu7w7rhnNB4tePQipWKKISfST92XmMykEqtnkuqg4WWjSG79BuRqGmaGpOtihHfvxnZbZu7i4F5-sZOWOvgb1siHS04mvwrG8YEZytDskBDxAQgdzdlBqEGq1AmsF434yYYXS3-FijQk6vAKMDSJ8xfXK0tHZMqx_tOJgy58PU9nXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که روبیو درباره خشایارشا صحبت کرده و باعث شده عده زیادی از طرفدارای حکومت عصبی بشن، یادی کنیم از مصاحبه قدیمی خامنه‌ای درباره خشایار‌شا که دوباره وایرال شده؛ جایی که می‌گه خشایارشا با بیش از یک میلیون سرباز به یونان حمله کرد، شکست خورد و هیچ منفعت ملی‌ای برای ایران نداشت!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73140" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73139">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73139" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73138">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCCEgHzViXj1Sio8idcTUJPQOL9X4LkZp5Z7bsRcOCpY2T-jRAQkhJ1KiyG-iNvU2hchjuqQ0wVPc4jzrY_r-a5xOesaAjzXAteIfUCcNociSM8T8qrl_xfr94E-yfwL0sSuDcTPXIWlkorUBHwHv2VAK6yO5MhJkmsOPB9iDhOgwz2qWL8oHRguOW9cjrqnyKmL8MRfdszfdV8pUtlwNtGJfKF7GFPCeoXYib6Kh0SCKqJ4Ny-9F5iNMTDkSLY6n1GAJpSeKGU6OarCxc0mMwnGDrzl4EMmF9RNaz35G8JC8wLKhv1ywCD-CMsietZwbByVX2Br0tYJSRmBZqapYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73138" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73137">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoPUgbsSqSxeUfGaCWipZQnHEDp2AALA-fEwPGlZZ6VfTOpg-L6ckU6ApHUnRm6eGwhPrNvwgUZoYSwek8URv7jqEjjiTQKJCrAf2VqLu3qz1D-G0OtGA8qzdraeDUUYYhPWHUX79YkOc609IwFCv9rlCb6jDxhgSM6w2EsiSEpF_I2o3x7Zid2Je_tvW2A1dadxBuJ7Pl00pAEc75RMEbYAKzAOHvlU727QUITh5YLm936xM-D3wyjP86X95QloKGZTpktyqvcQTk7Rz9bxGy0Ykgn9mKDcIU7dyhkKEy6LlMsvsdv0FG9g9DZkmZCd36orONHnUpRAdrVJ2nXRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
«آمریکا با بعضی از شروط هفت‌گانه ایران موافقت کرده، اما از نظر ما پاسخ آمریکا کافی نیست.
دیپلماسی ایران تغییر کرده و دیگه اوضاع به شرایط قبل برنمی‌گرده.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73137" target="_blank">📅 01:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73136">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ویدئوی لحظه اصابت موشک حوثی‌ها به فرودگاه ریاض
تصاویر دوربین‌های مداربسته، لحظه اصابت موشک بالستیک حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض، در روز گذشته رو نشون می‌ده.
بر اساس این گزارش، دست‌کم ۱۳ نفر کشته و بیش از ۳۰۰ نفر زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73136" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73135">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=Xu86Ts54s60qtSGvX0eCi_8gjNCL5di74Qovuc_uip3e0u___6X1-rIl6iGJ78wEdl0fyiB_nVbdvhEbrTRKFgSTUTMV73yemJDbXRVWgPbWDiHNn78SdBsG7m6GHCH4RpbxXtgFy5BOgD98_TSKNPB5ABd5Ye_pOFsu4ofCRz_k2u5kDV7vCRp-YxQm_s5ZcvvlJhEEG2nq-zLjPNm3GaPwTalKvsJvgpjUJPs5zHSYb3r1NJV8JFn4mcQBhjylAS7W8bke29M5PXgMzI4dRsUVLKzf0MxBKhZs9f9iImbWHjndBm0CPYiZBvMRLNfjQasDj_NVbjqNOVCTESsmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=Xu86Ts54s60qtSGvX0eCi_8gjNCL5di74Qovuc_uip3e0u___6X1-rIl6iGJ78wEdl0fyiB_nVbdvhEbrTRKFgSTUTMV73yemJDbXRVWgPbWDiHNn78SdBsG7m6GHCH4RpbxXtgFy5BOgD98_TSKNPB5ABd5Ye_pOFsu4ofCRz_k2u5kDV7vCRp-YxQm_s5ZcvvlJhEEG2nq-zLjPNm3GaPwTalKvsJvgpjUJPs5zHSYb3r1NJV8JFn4mcQBhjylAS7W8bke29M5PXgMzI4dRsUVLKzf0MxBKhZs9f9iImbWHjndBm0CPYiZBvMRLNfjQasDj_NVbjqNOVCTESsmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس پسرونه، اسپایدرمن تبدیل به اسپایدرعن شد :
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73135" target="_blank">📅 23:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73134">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=A4UvPRtoT-rScbunaNNFcFhvW_zw4oBzfH4-VARKaKckcKbp8QCttnkDsyyHvHDF8ZjBHT3Kz741fnFzdHVnGnL49ECREANx4_WCDOVc1uWJP7iwpF_ymSFBE8959DOdBLSxoC9F1Rrr-g0fgN_GegDmloJP5RUir9luOiK0mPXn3yN0A-ntcK23LbcqNx4co6r_RIJQEVhS02VlX3jsF_LeVRHRmYtOl1CgSnWlvCYgY4cMZZcVb0Tni8QVvN8mX5uxU28AN0XcBBuzjJPXmEVkxRcnxZwfuRrNyb9obG-fhpnQC7tRXmh0995A61_cAvNyLe5xRy_RgFW82JyKRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=A4UvPRtoT-rScbunaNNFcFhvW_zw4oBzfH4-VARKaKckcKbp8QCttnkDsyyHvHDF8ZjBHT3Kz741fnFzdHVnGnL49ECREANx4_WCDOVc1uWJP7iwpF_ymSFBE8959DOdBLSxoC9F1Rrr-g0fgN_GegDmloJP5RUir9luOiK0mPXn3yN0A-ntcK23LbcqNx4co6r_RIJQEVhS02VlX3jsF_LeVRHRmYtOl1CgSnWlvCYgY4cMZZcVb0Tni8QVvN8mX5uxU28AN0XcBBuzjJPXmEVkxRcnxZwfuRrNyb9obG-fhpnQC7tRXmh0995A61_cAvNyLe5xRy_RgFW82JyKRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود. مردم همکاری کنند فشار دشمنان شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73134" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73133">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=FlZhEcJ_s-GAGDqoPMU4FKRZiZRNPWmPcDHYzTIl12hNeVf_4y7dCs6X6kGl0wzmxxpDT2dSZNa564gPXmNvrSlnfjXL0TDsLG6Ziq1-jD3ys-c_HPVu7kk_hXLoM_EbMcNx02McgOONUyUpZXdNtp8ODFViPZE4TyiyxgUXpysX20lZpj4fTWfJoyg2W04n8gf_stmWMy0a_Dtm5GoYMR4OnwqjF-Pw7gpx50BMRsv7QJdYIWn0pTTHbyv6V1t-chCR-sAqisOzdA_AMlmFXqtQ_OKM0vcrx1hXZdvJinaRi25FCdFQqj34s2E_KQje8bzrMbTdXOqafZNTmSR7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=FlZhEcJ_s-GAGDqoPMU4FKRZiZRNPWmPcDHYzTIl12hNeVf_4y7dCs6X6kGl0wzmxxpDT2dSZNa564gPXmNvrSlnfjXL0TDsLG6Ziq1-jD3ys-c_HPVu7kk_hXLoM_EbMcNx02McgOONUyUpZXdNtp8ODFViPZE4TyiyxgUXpysX20lZpj4fTWfJoyg2W04n8gf_stmWMy0a_Dtm5GoYMR4OnwqjF-Pw7gpx50BMRsv7QJdYIWn0pTTHbyv6V1t-chCR-sAqisOzdA_AMlmFXqtQ_OKM0vcrx1hXZdvJinaRi25FCdFQqj34s2E_KQje8bzrMbTdXOqafZNTmSR7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ مربوط به پشت‌صحنه یه تئاتره؛ جایی که همه با هم دست می‌دن و همدیگه رو بغل می‌کنن.
+ عرزشی‌ها هم از این صحنه به خشم اومدن و می‌گن باید این بساط جمع بشه؛ حالا هم افتادن به جون عوامل تئاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73133" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=qFxQqLTw0spNNpRgRg3aMJQxbf0i6IOYgxJBdPrhK0xFQu75FjOj__9yqXl4SZb4TFBIiKhWNckqq_Oia8TTiyXr86VlnO978hdT0QwsOXP0nNk_UHeucgD6InBSfeAXMZGAsb9rzPdk8M1yq72jvnBgqqOXlKI3Hla9BsMb7_FrfX2IhJ6XN04L9J_dkedGy6Y1B7OyfyuKcKTFz0_ADx1HgOYax7BfaMIcdeVfqW8ehP4_BiSl2WISeuG0iC8yuX3TcPmPk6en21DPhoGyWnxvcC7teRUUqwGnw_hcyfTZzUmH68kr_RzB-BrTumT8R2vKx2VWQT1FWUmbAfUExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=qFxQqLTw0spNNpRgRg3aMJQxbf0i6IOYgxJBdPrhK0xFQu75FjOj__9yqXl4SZb4TFBIiKhWNckqq_Oia8TTiyXr86VlnO978hdT0QwsOXP0nNk_UHeucgD6InBSfeAXMZGAsb9rzPdk8M1yq72jvnBgqqOXlKI3Hla9BsMb7_FrfX2IhJ6XN04L9J_dkedGy6Y1B7OyfyuKcKTFz0_ADx1HgOYax7BfaMIcdeVfqW8ehP4_BiSl2WISeuG0iC8yuX3TcPmPk6en21DPhoGyWnxvcC7teRUUqwGnw_hcyfTZzUmH68kr_RzB-BrTumT8R2vKx2VWQT1FWUmbAfUExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=NrPQlUI10NuGhLJxsLE_8v4P0PTcV1vIJ3KDsZ8zZrWv_0zzboYKcO83VJxs1nAyRttCa60iYRNwOWa5zwIVZP0NvvmhUzHAxXfxzYBxtMB-PsgET8qICvhphclGUsoKqxKoxsZnAIZocLKdbtI4wq5h1VDpjozJ_EA0SVdl-1bdYEU2em9iGVZHrf8wtrlOsSy2EpiDGAZuG8eLkfNoZ6Qthqlj0hBh6kKSblRa-zaUn1d28EdWrtDjEJCNokbZ9hhKNdCd7NF4WXp175QuZcLv8dr3hEmuqDD0aQFqroNEkDcgULD-ZejDfrgnJwucMOiieglywgxqIfNEVR8_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=NrPQlUI10NuGhLJxsLE_8v4P0PTcV1vIJ3KDsZ8zZrWv_0zzboYKcO83VJxs1nAyRttCa60iYRNwOWa5zwIVZP0NvvmhUzHAxXfxzYBxtMB-PsgET8qICvhphclGUsoKqxKoxsZnAIZocLKdbtI4wq5h1VDpjozJ_EA0SVdl-1bdYEU2em9iGVZHrf8wtrlOsSy2EpiDGAZuG8eLkfNoZ6Qthqlj0hBh6kKSblRa-zaUn1d28EdWrtDjEJCNokbZ9hhKNdCd7NF4WXp175QuZcLv8dr3hEmuqDD0aQFqroNEkDcgULD-ZejDfrgnJwucMOiieglywgxqIfNEVR8_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=AoIJ3iV9MeMe-A7bya7T3daQDHWfdKKYPEyQGmM_yQAejuM77pzQVf1yYFs93FT01RCN7xxwP71TjiAsbTfFP-tt20Cr8g-8Go0Dg0FuJ_cPiI4hPgOmrXj6yGunEKjiqOLpKS8xvk5Y2r9y99Wri27ekYvjCXYj994F5tyBuNgMwMdXgHDRPmrFn3Mi4HtUxHNpeQ7JI9naGOpbllxrlzATJuJ7hSJuCHA8sZcgnrsBzw7IcV-p_cp8Rm_JkYYQD3t5KL-lqVpfu-jvJfAyO9LK2CI9FBjOgRPD_grwk0MX03BSd4vswioaIeAlkehB577LEAvxY5YP9X0oUjxrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=AoIJ3iV9MeMe-A7bya7T3daQDHWfdKKYPEyQGmM_yQAejuM77pzQVf1yYFs93FT01RCN7xxwP71TjiAsbTfFP-tt20Cr8g-8Go0Dg0FuJ_cPiI4hPgOmrXj6yGunEKjiqOLpKS8xvk5Y2r9y99Wri27ekYvjCXYj994F5tyBuNgMwMdXgHDRPmrFn3Mi4HtUxHNpeQ7JI9naGOpbllxrlzATJuJ7hSJuCHA8sZcgnrsBzw7IcV-p_cp8Rm_JkYYQD3t5KL-lqVpfu-jvJfAyO9LK2CI9FBjOgRPD_grwk0MX03BSd4vswioaIeAlkehB577LEAvxY5YP9X0oUjxrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=T7jJzmq64H85Eu-8oNl2b-MAcGzoeWIUT3WtJj9oZNEFwWIrbbz6N5ola12JfldogxDfhqh4Vn6jRUD82qyTsiq9McSSOh0a9e0PdNYtAtuEzSgS5uBFqSePU-9EUflYWLBEiMrOkyqQ1oWdvZJgQNXSu-cmiepX9QZ9jxuXEE4py-0Hf_sSW3ofcGk-x46jm3uIy6XQO8_7MmPoIvcbEcrRUPhP3E849XwzkGWM5BLp5Y6cCS6ShLCg3e-hmuTMGqXvmYjcZgTq95fNu9Oa7pGixdX_kKel4MKWmLSOf1ir486zxLx8RTmB1Iz807Qqh1NpgqbHeYDbKY-QWz3xHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=T7jJzmq64H85Eu-8oNl2b-MAcGzoeWIUT3WtJj9oZNEFwWIrbbz6N5ola12JfldogxDfhqh4Vn6jRUD82qyTsiq9McSSOh0a9e0PdNYtAtuEzSgS5uBFqSePU-9EUflYWLBEiMrOkyqQ1oWdvZJgQNXSu-cmiepX9QZ9jxuXEE4py-0Hf_sSW3ofcGk-x46jm3uIy6XQO8_7MmPoIvcbEcrRUPhP3E849XwzkGWM5BLp5Y6cCS6ShLCg3e-hmuTMGqXvmYjcZgTq95fNu9Oa7pGixdX_kKel4MKWmLSOf1ir486zxLx8RTmB1Iz807Qqh1NpgqbHeYDbKY-QWz3xHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naZQv5j6Ti-yZ-HkIddKn5D-l_gfuiUr3BcE4twJu5kJEPjkbbOak2FSbXlSJjuFb8N2yDAO-kgqsWc5aWYHQEiHzYYL1-1ayR6nknuKIWh3nlt3hKF2lVm8_lfmgCU8F0rZ7t08uk8CNX3YVIp1d4Gx1NIHctImt9qLF8iy7XaKd7a3XdbQaf7p4aq-ruerIdBcvBVQbfpzedLEv0MlFCgqlosi8LRTSCcmxxX6N3JvtQ-5DsKg36V5PbAggX9wcg_iJflfVLdEOXZLYstjDYAY5ka9v2MWSxjWke66VnojtgS73jUbXLSPJ3ODPYyIWM13l25TuOsiOKrvGl4voQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=OO5CEL7fLEbx668hKw7CNs51qJT4fR6oInYfMghOHbqo55dXvhs3_IduvrQJsyE-V7yNbu2WrqCpfVWaWSuzvFw9XNy6QOXPSX_3PlkknXxYQeZYgKTtVF6bJAVy5DNp5nGNSjWiyVYsgffmxejL0UkGFg2xVQqMyW_iLTnxlafvYYq8JRkZ8fKxTvG8-qYsWU1zb0LxWxVUu3kz9yPz2wuUtfIxUUd0IkGsotcLuOKgMR6qtBjWUXksBj5NxBBdxJgoBF3v94lVnjBGDC6ABVQpv4lrY-lrgKdqj1jJFse4bOJ15zCPGsSkbgqkGR-nd_uLbFyJ7AcB6aFEIoCr8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=OO5CEL7fLEbx668hKw7CNs51qJT4fR6oInYfMghOHbqo55dXvhs3_IduvrQJsyE-V7yNbu2WrqCpfVWaWSuzvFw9XNy6QOXPSX_3PlkknXxYQeZYgKTtVF6bJAVy5DNp5nGNSjWiyVYsgffmxejL0UkGFg2xVQqMyW_iLTnxlafvYYq8JRkZ8fKxTvG8-qYsWU1zb0LxWxVUu3kz9yPz2wuUtfIxUUd0IkGsotcLuOKgMR6qtBjWUXksBj5NxBBdxJgoBF3v94lVnjBGDC6ABVQpv4lrY-lrgKdqj1jJFse4bOJ15zCPGsSkbgqkGR-nd_uLbFyJ7AcB6aFEIoCr8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">زلنسکی در گفت‌وگو با باراک راوید:
«اعلام آتش‌بس برای من هم خبر جدیدی بود. اما اگر روس‌ها با آتش‌بس در حوزه انرژی موافقت کنن، اوکراین هم موافقت خواهد کرد.
اگر رئیس‌جمهور ترامپ این توافق رو با پوتین مذاکره کرده، لطفاً به ما بگید آتش‌بس از چه زمانی شروع می‌شه. ما آماده‌ایم و این توافق رو می‌پذیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73122" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iK9PvlBD4YNK620rED8q_X59KFl4-xlsb_4Xte4owM-M9gR7v6rfqhMQtnAJW9oP0Qz5QzctNRA370_0q_mm242X0YLOsPWwnqA0t0Nvad1VcygMLQFj-3FiiSXd6lnrH4gfk98dnPyaGNuwkW4-mcmy59oSpO1NaEChxb4ooWAHy1o4ty9GtnPwakRkZZckkjYN2fEutyEZLT7vCGO1L5dVkZVj7Xgp9acnWo_LZygQcYI2OHw5kgaCowa_MDd4SeB5Jf7T29qf3hoqT8jC_ojNY5KtnA9oC2DMctAiGQbapSWJ5RWuIYfFcua7YEJ_XIKrrEjUCDI6Ec5ieUv9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از آتش‌بس انرژی بین روسیه و اوکراین خبر داد
«از همین لحظه، آتش‌بس در حوزه انرژی در جنگ روسیه و اوکراین برقرار می‌شه.
هر دو طرف با این توافق موافقت کردن. این آتش‌بس رو نقض نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73121" target="_blank">📅 18:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73120" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gViBkudT8RJPGYEYcIBpad-wg2i2FZV3VGoUhrvetLO76i5y2kSvF5UJQni8_3KHHkNVjHAtXWMeFDukEo5Rtmzb5ChwENiVHvLcK3CjJYcVjXdTbwDQ4MTDq266331b4MFYkNY5hoC0afV88RobaDN9clDNpOJQ3SrumBMDwKS4T_V7twUCg4s3v_YIZGuCwRAPprtlUtvrnSUyAP7Kd5EgzyvtdXswF1pW6fM2Z0DXtuk6SdNRFqhB26iqApNIY5iDxUosFrUyuY3nDx2qY8XHLBhqnpBRcG82OXPbVVJ44uVLMrHmqkCleSL8Ns-YI7n7nQdhWEEsZ-EvqDUJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73119" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=J8HCg32reT8FwzXPmFP3BmpzBn-GOvPdoMdX3AXzlXBB3-RTWCP8-Jy_ukAS5MNtawxNWx7oe2CujalMwmti7pq1wNqXeeDSSvqBWFngdW6JlnEXYij_2u7r_XKeAAchG8SIcz-KMm4xnSaOk2IRZ8KYPd5dfLhZSdDh-QJ_bCzDm3AMDCFgniWAzaC3LXjXZFMmWKWhKJs6-c_QJ02iwEQajoaogPFD3EzEIMbpQvNKDBZvklB0nhPfLpRy3RxYAIpf9a4HfYe071AVdH7MT7g1ca_yemyKx3jJyVU2a05YqH0nX_n4X3zUw_ZyKuk43a2NLUS4hM0kVio2fIQPyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=J8HCg32reT8FwzXPmFP3BmpzBn-GOvPdoMdX3AXzlXBB3-RTWCP8-Jy_ukAS5MNtawxNWx7oe2CujalMwmti7pq1wNqXeeDSSvqBWFngdW6JlnEXYij_2u7r_XKeAAchG8SIcz-KMm4xnSaOk2IRZ8KYPd5dfLhZSdDh-QJ_bCzDm3AMDCFgniWAzaC3LXjXZFMmWKWhKJs6-c_QJ02iwEQajoaogPFD3EzEIMbpQvNKDBZvklB0nhPfLpRy3RxYAIpf9a4HfYe071AVdH7MT7g1ca_yemyKx3jJyVU2a05YqH0nX_n4X3zUw_ZyKuk43a2NLUS4hM0kVio2fIQPyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«نمی‌دونم این ماجرا چطور تموم می‌شه؛ هیچ‌وقت نمی‌شه از قبل دونست پایانش چطوریه. دیوار برلین هم بالاخره یه روز، یهو فرو ریخت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73118" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=JT1dLxmx_nznwqUqClGkemFtiRHOLoOodofXpQktpvyzftwiFH9kdFvKJ1wesMB3OysL2IdCnTne6mswZAgq2qjcMMDDjX5D1K1PMuwn9e89JnFH-_VyMu1PT3tv_cwAj8YJGRkfGMTcXl5iNjyaNgDqnAdUGvts31Njee4k3oN9bFiTk31ST9Aw0GZJAypwndaZMnVGxD8CujU89Jev9o6w1JH-BeKtsEJ_B1ySKw28sQCZTAk_QkGy7GyVQJT8G9mGnHHdMdxAP614WNq3Fnhiq3WcbL0GzhGiqB-jQ0qMryKXi0sil50mrbhnIKrDy5XZt9-ZL1eG3QKkCu5b6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=JT1dLxmx_nznwqUqClGkemFtiRHOLoOodofXpQktpvyzftwiFH9kdFvKJ1wesMB3OysL2IdCnTne6mswZAgq2qjcMMDDjX5D1K1PMuwn9e89JnFH-_VyMu1PT3tv_cwAj8YJGRkfGMTcXl5iNjyaNgDqnAdUGvts31Njee4k3oN9bFiTk31ST9Aw0GZJAypwndaZMnVGxD8CujU89Jev9o6w1JH-BeKtsEJ_B1ySKw28sQCZTAk_QkGy7GyVQJT8G9mGnHHdMdxAP614WNq3Fnhiq3WcbL0GzhGiqB-jQ0qMryKXi0sil50mrbhnIKrDy5XZt9-ZL1eG3QKkCu5b6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«اگه این ایرانی‌ها کشورشون رو دوست دارن، خب تبریک می‌گم؛ می‌تونن همون‌جا بمونن!
این فشار مستقیماً به نخبگان و مقام‌های حکومتی ضربه می‌زنه؛ دیگه نمی‌تونن برن لندن و اقوامشون رو ببینن، تو پاریس به دیدن دوست‌دخترهاشون برن یا به پول‌هاشون در سوئیس دسترسی داشته باشن.
اونا از دنیا جدا شدن و ما به ادامه این فشارها ادامه می‌دیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73117" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=aqPtqs70e68cO50AguvXS8V2an0wzC5zCmXDVD1ohwJlBw6vT3v1_K3YoHLl8DMm913_N8ZNijDAc_QszsmSpaNzLI8hmJRIlhaTe1l5Onf3-9pKlOo56TLrNzInxcY0naZc-PzvoA8HRdgGThbDm_mCiAiq2aT7OGoXN100AwOGQhEkqhu6d6AutbMynV_V0-3A46idY1JlD5D5LF7lHLIlgDNSbfOXMS3OWva_o6agMUDkkVPl-byEtdxUIGHwk5uFZ56On8KnzyPtzvnxcarqLBXakDFtVllIsBQ453AO8FjWguU-elyvesmbX4hY1MKNye6OOY8fEq04iARolw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=aqPtqs70e68cO50AguvXS8V2an0wzC5zCmXDVD1ohwJlBw6vT3v1_K3YoHLl8DMm913_N8ZNijDAc_QszsmSpaNzLI8hmJRIlhaTe1l5Onf3-9pKlOo56TLrNzInxcY0naZc-PzvoA8HRdgGThbDm_mCiAiq2aT7OGoXN100AwOGQhEkqhu6d6AutbMynV_V0-3A46idY1JlD5D5LF7lHLIlgDNSbfOXMS3OWva_o6agMUDkkVPl-byEtdxUIGHwk5uFZ56On8KnzyPtzvnxcarqLBXakDFtVllIsBQ453AO8FjWguU-elyvesmbX4hY1MKNye6OOY8fEq04iARolw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«بزرگ‌ترین بازنده در این ماجرا، حکومت ایرانه.
اونا سعی کردن با بستن تنگه هرمز، مسیر عبور و مرور رو تحت فشار قرار بدن؛ اما این کارشون جواب نداد.
بعد تلاش کردن با بالا بردن قیمت گازوئیل، فشار ایجاد کنن؛ اما این یکی هم دیگه جواب نمی‌ده.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73116" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=BRtGfA4Mru_cEyr4IL82C0V3oFmpVL5j9comlxMWu-qpa3r39WQAJdd-823C_iaoy_R9MGkt_VhQWpXq1kFtKldQBu2i5xpCX2yOHwlR1lMkqd26YIxE6yhwXRTKYQw7Xp4YjqkT6aJ6Y7kkxly77xBwh_WE90gW5VddlIh3DPu94LXNEn5Vp2tBStfIqDNJleYj4rkA8kPhB7G6dgKa3QHJNRfpfheqreSS7soMzF1HL33rHqgC0jsxaY7b9eaCD8bpcdqHjPtZmLAT270Z_kI123UyqKNGWdOMyVIltUbXouzgiNn6zZXRCv2jnBwJmUbzd5F8ra1wDPgUfBxe7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=BRtGfA4Mru_cEyr4IL82C0V3oFmpVL5j9comlxMWu-qpa3r39WQAJdd-823C_iaoy_R9MGkt_VhQWpXq1kFtKldQBu2i5xpCX2yOHwlR1lMkqd26YIxE6yhwXRTKYQw7Xp4YjqkT6aJ6Y7kkxly77xBwh_WE90gW5VddlIh3DPu94LXNEn5Vp2tBStfIqDNJleYj4rkA8kPhB7G6dgKa3QHJNRfpfheqreSS7soMzF1HL33rHqgC0jsxaY7b9eaCD8bpcdqHjPtZmLAT270Z_kI123UyqKNGWdOMyVIltUbXouzgiNn6zZXRCv2jnBwJmUbzd5F8ra1wDPgUfBxe7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«کارگرها دیگه سر کار حاضر نمی‌شن.
ایران به بازار دلار دسترسی نداره، برای همین کاری که می‌کنه، چاپ کردن پول بیشتره.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73115" target="_blank">📅 17:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=bI9CqfaKi8IXBLoGXbEESNnHx59ropQ2HK25eFmKNIVW1cJcdzcXdzv36nPX7Udf9U51tTiRn9qTjWqfBnTYZ16xXGT9TIi6xYPqOLW9zXlIXIq9wTYYOJnzUM1yHTP4dbuS7aaKU-Cg2i3pbFlUsla8Hfl0cFfLzMrXiYQ10H4Bf1L3XSRHuiMscJAH0v216ki57-i3veh25bEX6d1lFTL4S6lJS2QkgpcyugewXXrfQrx0pnRofOt-J-y4vGqEyGNJJC8OOkn0xl3q2zLDzKSFeWhkDMQVL45ing5Krv7S3i2s5ysZ6Lume_qqjllbGyoh76pWzTd4pRnCetWbvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=bI9CqfaKi8IXBLoGXbEESNnHx59ropQ2HK25eFmKNIVW1cJcdzcXdzv36nPX7Udf9U51tTiRn9qTjWqfBnTYZ16xXGT9TIi6xYPqOLW9zXlIXIq9wTYYOJnzUM1yHTP4dbuS7aaKU-Cg2i3pbFlUsla8Hfl0cFfLzMrXiYQ10H4Bf1L3XSRHuiMscJAH0v216ki57-i3veh25bEX6d1lFTL4S6lJS2QkgpcyugewXXrfQrx0pnRofOt-J-y4vGqEyGNJJC8OOkn0xl3q2zLDzKSFeWhkDMQVL45ing5Krv7S3i2s5ysZ6Lume_qqjllbGyoh76pWzTd4pRnCetWbvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«ایران دیگه هیچ محموله نفتی‌ای در مسیر انتقال نداره. جریان نقدی‌شون منفی شده و ما راهشون رو بستیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73114" target="_blank">📅 17:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=ZVGodp9Dz2hH7-E6yh0y3786o00oVSeQkrmJjp7VlfjSfu-sucPKsQ1E42FlKz3EUeh_v036-wuyRGmx-i7Mbhm4ntEzNXL7F7jyXfo3D-Xk8B0CCGT2y_zm_VsCWaXdJ-f_RXMQzmNuW0gutvEn-LlJS5POvEYK2op9yDvy7jwF_KQeWdJh-lX4giIg8Gda8xP-KBpJ7rgm5YSkiohGB_4XKDN8a02mOLEk9_yA9B5vYCQ0Zxa2GiI0DT5T_LEhgUqZJp8qLHmWJmmPawjSyiBdLobZTvAhoHNoWqMzwKGRAbmRqkBEuo80hu74jC13QX8BjX0mmUx79ZvFMzQ0sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=ZVGodp9Dz2hH7-E6yh0y3786o00oVSeQkrmJjp7VlfjSfu-sucPKsQ1E42FlKz3EUeh_v036-wuyRGmx-i7Mbhm4ntEzNXL7F7jyXfo3D-Xk8B0CCGT2y_zm_VsCWaXdJ-f_RXMQzmNuW0gutvEn-LlJS5POvEYK2op9yDvy7jwF_KQeWdJh-lX4giIg8Gda8xP-KBpJ7rgm5YSkiohGB_4XKDN8a02mOLEk9_yA9B5vYCQ0Zxa2GiI0DT5T_LEhgUqZJp8qLHmWJmmPawjSyiBdLobZTvAhoHNoWqMzwKGRAbmRqkBEuo80hu74jC13QX8BjX0mmUx79ZvFMzQ0sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«همون‌طور که رئیس‌جمهور گفته، انتظار نداره درگیری نظامی تا قبل از انتخابات میان‌دوره‌ای اتفاق بیفته؛ دست‌کم نه تا بعد از اون.
نمی‌دونم معادل عبارت «تسلیم شدن و درخواست توقف» به فارسی چیه، اما ایرانی‌ها بالاخره به جایی می‌رسن که از آمریکا درخواست کنن دست از فشار برداره و تسلیم می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73113" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=KSHeCxXFN0CP_Sd26KcRh5z_uKkF5HfWGTzc07KZDgdUTHa-j-5-RpcPzkgiw-HjTsgJe75_fCY7o5_0KO7PKozjDrF1Yaet9uof3AHqjdKc-3S1BdRxLzRkSi1ROaqHj7t5Wnr1ZAMKamO98K2xUisxD_XD1vP8lm6O4lieNEQYkeVreZuHun_Yc1UUPvO59uKCBxagtRfjd1wGdP7uMuPohqsqBZMyze0SqC2yA9ECCp9QtoMpmkSwWp-LdkYZv62JyPZgtTckA4RtJKsDclYqcYJ7ycrljR-HuOJxOhGwbkcfNo4LN7VcHNM5EgUAOV-GAjUkUPk7vgprHloOgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=KSHeCxXFN0CP_Sd26KcRh5z_uKkF5HfWGTzc07KZDgdUTHa-j-5-RpcPzkgiw-HjTsgJe75_fCY7o5_0KO7PKozjDrF1Yaet9uof3AHqjdKc-3S1BdRxLzRkSi1ROaqHj7t5Wnr1ZAMKamO98K2xUisxD_XD1vP8lm6O4lieNEQYkeVreZuHun_Yc1UUPvO59uKCBxagtRfjd1wGdP7uMuPohqsqBZMyze0SqC2yA9ECCp9QtoMpmkSwWp-LdkYZv62JyPZgtTckA4RtJKsDclYqcYJ7ycrljR-HuOJxOhGwbkcfNo4LN7VcHNM5EgUAOV-GAjUkUPk7vgprHloOgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=VYXmkzLPVScXeei3ugjbQctnfUZYvp6np-qbHAdtc9UmTcsfped6tsvwb9SjwFe-7asHNX9_MHfPlEJDuOjmIGRsAWzqtbtmk4EdW0DnYlqGZ1AZH1GVfHcwn4Sr9c09KN_3yl7aNFRZyIuW7KPPE9dH4JrM74nkK40biHHs5zZ6odjzdTi6XYUhKOgPPKa2UeuO109XfWk3sJCAiH22AfCb18Yy4Jsf3GV4awsHtkztXTqUq8NEUBiOoWCphdqtkHPiYc-aeEgeDYHfxPgcOqUtiR8kVnnYeYH-4-PfOr7SRWFNNlUB_g_pVM6bPhjb9qi0QBSyLDumoN59B1DliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=VYXmkzLPVScXeei3ugjbQctnfUZYvp6np-qbHAdtc9UmTcsfped6tsvwb9SjwFe-7asHNX9_MHfPlEJDuOjmIGRsAWzqtbtmk4EdW0DnYlqGZ1AZH1GVfHcwn4Sr9c09KN_3yl7aNFRZyIuW7KPPE9dH4JrM74nkK40biHHs5zZ6odjzdTi6XYUhKOgPPKa2UeuO109XfWk3sJCAiH22AfCb18Yy4Jsf3GV4awsHtkztXTqUq8NEUBiOoWCphdqtkHPiYc-aeEgeDYHfxPgcOqUtiR8kVnnYeYH-4-PfOr7SRWFNNlUB_g_pVM6bPhjb9qi0QBSyLDumoN59B1DliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=qgd4PEVlxwZnBcGyXMeE8BxoLqQGAZ3sWdeMElGu58i3L6IFOvCcwUpZ1bWQpcJDhwl358eIg0Uh1Ku0OIRQzD5Vvd9ou8pbVHOwALNL4oCOR8t28XPm-0p_bT2_48gHJzA-p-3jiXmG_Huei3yDTDbonI8mUztevhbD75d2ZHZQgT-vkHY6DGLsGRn4tdi32oO8gKH61jJ0NGb3JAX8rmuiK7Cm2oSddNWB0rOBMmZMZva9BgIe1Wp0PfuMzRo8UaH9sUfGDxyTgYubtcQCcWKRbnx_jQ8IhL-sYZUGiXkoDsAdxf0SMHwlNiZadIdwrCXcSuc9WAfaAcacsQMpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=qgd4PEVlxwZnBcGyXMeE8BxoLqQGAZ3sWdeMElGu58i3L6IFOvCcwUpZ1bWQpcJDhwl358eIg0Uh1Ku0OIRQzD5Vvd9ou8pbVHOwALNL4oCOR8t28XPm-0p_bT2_48gHJzA-p-3jiXmG_Huei3yDTDbonI8mUztevhbD75d2ZHZQgT-vkHY6DGLsGRn4tdi32oO8gKH61jJ0NGb3JAX8rmuiK7Cm2oSddNWB0rOBMmZMZva9BgIe1Wp0PfuMzRo8UaH9sUfGDxyTgYubtcQCcWKRbnx_jQ8IhL-sYZUGiXkoDsAdxf0SMHwlNiZadIdwrCXcSuc9WAfaAcacsQMpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=SJQ3nsw40m3cv1X4LC78hEewgHCfaI65qKhWnPKxtRut6bwMHGKe2yhD9ol3Y5r_qYq_zbLY_7OUW-qBLTn0O5FaVccnPw68En_1xeH1vUebXgs7bwCiMoOPTNs5fK2g-TiuiypsLfbWFwYAxkcDYVDsvbjmdwRS9dTMch6p1NEbEW3u7YOgmE4g6A1PZaHFRsb9Qt-W_Y7FR_JIek5QZ53VeU9ORZBxxaWX2bTCTFyxWD1P2342alzWUo3CWfXTgwkxjIjy-nxfdgmb1CldbF0sgRKW52RXZ_4iDbGzcSO7Fh4KCDQhKiFYpgXOH9hATtf_t0Sz-MgElFdqAn58LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=SJQ3nsw40m3cv1X4LC78hEewgHCfaI65qKhWnPKxtRut6bwMHGKe2yhD9ol3Y5r_qYq_zbLY_7OUW-qBLTn0O5FaVccnPw68En_1xeH1vUebXgs7bwCiMoOPTNs5fK2g-TiuiypsLfbWFwYAxkcDYVDsvbjmdwRS9dTMch6p1NEbEW3u7YOgmE4g6A1PZaHFRsb9Qt-W_Y7FR_JIek5QZ53VeU9ORZBxxaWX2bTCTFyxWD1P2342alzWUo3CWfXTgwkxjIjy-nxfdgmb1CldbF0sgRKW52RXZ_4iDbGzcSO7Fh4KCDQhKiFYpgXOH9hATtf_t0Sz-MgElFdqAn58LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=DdMJcDzX9O0nUVkjhwBa7k1-pGl785mnyE2l_UkxFIMXAuXC3ARPy6sBIW6M5Ohq0ZSa-JDQwZcI4bETmPERr4rHZZ9oajfaBNRDI1MRwk51E7XOxI7qtMVeVUdlVBzLObwu9sK9WlP-Azx858KObfxKNk8WHsTPU7KBvuK1bIAcAYQ-gJckEvbwK60WbveLn3S-wpAobD8gDFU7AIVup7ZeI-9DYwv0nQPxaCZVAQn0cNlouJM8bQU4vQi7ABifPEuAS0LWC4_kG3lvyfd4rVhAAECdFAyXVgtOR6T079GjTrhLvrL1pn90vBKWZgLet2wJDM4Vn62Slw8lJaAiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=DdMJcDzX9O0nUVkjhwBa7k1-pGl785mnyE2l_UkxFIMXAuXC3ARPy6sBIW6M5Ohq0ZSa-JDQwZcI4bETmPERr4rHZZ9oajfaBNRDI1MRwk51E7XOxI7qtMVeVUdlVBzLObwu9sK9WlP-Azx858KObfxKNk8WHsTPU7KBvuK1bIAcAYQ-gJckEvbwK60WbveLn3S-wpAobD8gDFU7AIVup7ZeI-9DYwv0nQPxaCZVAQn0cNlouJM8bQU4vQi7ABifPEuAS0LWC4_kG3lvyfd4rVhAAECdFAyXVgtOR6T079GjTrhLvrL1pn90vBKWZgLet2wJDM4Vn62Slw8lJaAiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=dBPvnhwSDAQK8iU46ab0hYTl_AlJ5bASV-zkpXBKmhRMy97CljqHyhWertXji7HkmB7KYyYZttBU5ckqIqQxPd8QGZS3Maf1-benUikVoYjM0LWsVJYRaTF2yZxOIrVzZ2lm8Dg1Y4lBfiws1QE1kK2ZHoLvSH2SMZradDRS1mLc3Guwm4CWsudtm0F1kJ8xTYZAiUZI787JNWqg-ebGNBIb7XfbkBMiuv14ug3jMIYFzVJNqhBpevrgwKu4i5U8Br4nM_vhGhloKh7P2hO3wwEM1Yynu8KiFxaplgD-x2Kaa2gsvjjlbVDTvCfWkQz04kLBNaQYK12ylhLPk-LLzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=dBPvnhwSDAQK8iU46ab0hYTl_AlJ5bASV-zkpXBKmhRMy97CljqHyhWertXji7HkmB7KYyYZttBU5ckqIqQxPd8QGZS3Maf1-benUikVoYjM0LWsVJYRaTF2yZxOIrVzZ2lm8Dg1Y4lBfiws1QE1kK2ZHoLvSH2SMZradDRS1mLc3Guwm4CWsudtm0F1kJ8xTYZAiUZI787JNWqg-ebGNBIb7XfbkBMiuv14ug3jMIYFzVJNqhBpevrgwKu4i5U8Br4nM_vhGhloKh7P2hO3wwEM1Yynu8KiFxaplgD-x2Kaa2gsvjjlbVDTvCfWkQz04kLBNaQYK12ylhLPk-LLzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxrxPYtphGnFaxyzcnDr9EiBdVLr9cW5Jgtwtro-41TW3OryYCZSgI_EjT-20rOnAJQHiGNwC_742-CILhkZKqvskAC2-lwaiVvkwJuO_wVA1C_XmWDeer-tv5XHuOUSsZ2RUI2lUH39ZOwueV_0tFBA5XBOvyprDbdVwT_Rchh9mTA1rbCnPL7VshGB_mlO9iXq4U8TcImHQzsLcbxKGfqMXWeoIVoBzLe6vgaavmMNDHP2LXemVmPCjfK9o-XpPSOxvn7_JrhhKsUvOWgK44gkd9pDXt6p8dDicd0kgbope14dtXcb_0YFHwsj2kEvrf-IQ0iFkIxnPqvoY-7xQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7wtVKP5YP4a14KqJoMB5ebjQ27lf6StZmv6Z0kzh3E1zG6f1ffoojQjOCLhFIBI93Yb63tmXrgXe2WHJyt_DmbBFPPQb3spTWESZjyJidROsVQfSzv7k6Ij8Jte4HeQNAYpqBECv9ksProjcpLJqHkUmva3Rp04x7l_Zu3uLch5divaRXmga5onNK2oWbgcdVIBHI2L8vt1Aop3O1470PIEYmU2S_wZjhGlYTPhpdFb_StglSGhFqN-6b32romWtyCf_OcIxbBfPZNgMtNlEZJOrYne0HADPXD5u_ldqgTybI5EGo1p_FGKY9nE9qnWx5Hj20Bef9kQyDBm6tvVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=OgQx3LYMO-eAyBi46v-5tpjs0R5CmsSZqILo1ZgUt2vZdrJfRY4VeM3p3v1lP9STAHmR67mbjbHS9Vlz8BLHCqgQgTjE4i1AFcAW0ddjUf-4mNH2IUTpIMFAEyiUJKxSo10KlpZzLRu1fjuToXrm5CjICSYm5jdaelpM2f1RezgQRY9bsbyJEXsgIDD8fmIGbSAxq8R6HS7bj-MseT0PUZrHjsW8HTSZQ9fAUtM41bICJNQqECX0cO9KmuSrtneFzShNzsTe5uawtfT308f4h5zRtARIi4oEzzlaOlKootJgI4pVS9O13t95v8n0f0TWg3ZRTZyLtOw-DtTyA54CzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=OgQx3LYMO-eAyBi46v-5tpjs0R5CmsSZqILo1ZgUt2vZdrJfRY4VeM3p3v1lP9STAHmR67mbjbHS9Vlz8BLHCqgQgTjE4i1AFcAW0ddjUf-4mNH2IUTpIMFAEyiUJKxSo10KlpZzLRu1fjuToXrm5CjICSYm5jdaelpM2f1RezgQRY9bsbyJEXsgIDD8fmIGbSAxq8R6HS7bj-MseT0PUZrHjsW8HTSZQ9fAUtM41bICJNQqECX0cO9KmuSrtneFzShNzsTe5uawtfT308f4h5zRtARIi4oEzzlaOlKootJgI4pVS9O13t95v8n0f0TWg3ZRTZyLtOw-DtTyA54CzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=ltqk6a0bh3AhPS8OpJj-zAv_XJ-5nU3J1eoSrOFnk4Z_mjULrfQ5hzLaz3rU50BWwB8cea9f940pRsC1VpZ5R7sVqLWWljrYrXlXue-azdMjxxaxs8LjPb9o1ZcRQ8B1vtuCH_JYoSvQrf7-_1Hqxuj8kvUa558bNHJwa90CBHdaMSjrte84jhtPXv1I6FsQ-7N122DFRuXXMmOoLs4fMPxa3slf53Q6kWLIpAiLRZFTWn4AdwlsN37GbL4jWcAtgsHhgT_13Lv2D6lXK__ecJzxU-L5BRHoTiWorjk0HJYEJs8FtiXj-5QR9L_89XNkxZyyWnVwQmeUVeIPgH1_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=ltqk6a0bh3AhPS8OpJj-zAv_XJ-5nU3J1eoSrOFnk4Z_mjULrfQ5hzLaz3rU50BWwB8cea9f940pRsC1VpZ5R7sVqLWWljrYrXlXue-azdMjxxaxs8LjPb9o1ZcRQ8B1vtuCH_JYoSvQrf7-_1Hqxuj8kvUa558bNHJwa90CBHdaMSjrte84jhtPXv1I6FsQ-7N122DFRuXXMmOoLs4fMPxa3slf53Q6kWLIpAiLRZFTWn4AdwlsN37GbL4jWcAtgsHhgT_13Lv2D6lXK__ecJzxU-L5BRHoTiWorjk0HJYEJs8FtiXj-5QR9L_89XNkxZyyWnVwQmeUVeIPgH1_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=qBbvYdH5QQ6q0eiwhxlqJzivfWc3MmuBMZjMOo0SVVEtEqHjSYJ2y1vsG2CjFOTj2I3LkgGnpo5qkZvN1uk2PX288GVBatPrqFexUW8qyiXL_x8JP5UC8iDVmZpV0bruDHD2xEP00-PWxwi7QgftCSdhvh63uEWJrLwKRlgIz2NyqLtPpS_Qh85mOql_64Tj93m0a1nE15zZLK9hCoUee5-pqQzHwKtNGUNJidAeaH1jayL1M38z7wPHjPz2g9Kh8wRGaOMifSkDJq10HXcXpm5Xq-LNygnxADnNtUjF9v-Jp8xzSTgAhELn_bR6BIZDGHmR7hLnAeeO5SoCIfVyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=qBbvYdH5QQ6q0eiwhxlqJzivfWc3MmuBMZjMOo0SVVEtEqHjSYJ2y1vsG2CjFOTj2I3LkgGnpo5qkZvN1uk2PX288GVBatPrqFexUW8qyiXL_x8JP5UC8iDVmZpV0bruDHD2xEP00-PWxwi7QgftCSdhvh63uEWJrLwKRlgIz2NyqLtPpS_Qh85mOql_64Tj93m0a1nE15zZLK9hCoUee5-pqQzHwKtNGUNJidAeaH1jayL1M38z7wPHjPz2g9Kh8wRGaOMifSkDJq10HXcXpm5Xq-LNygnxADnNtUjF9v-Jp8xzSTgAhELn_bR6BIZDGHmR7hLnAeeO5SoCIfVyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73096">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ درباره یمن:
«ما با حوثی‌ها در ارتباط هستیم و باید ببینیم چه اتفاقی می‌افته.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73096" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73095">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=rt26xAVe_096HbZV7GzaI-6JYevsRP_Xmyx_YaupELz0nHelK93VD2G-UlLimk4AIt7y2fK228nTFvi5qPl69WpWmfWEykahYLkNCzs2uCKoN5OUjRpseSYnZaa83ykug26sjMJI4ZShLu0iBIfw4tbouKIhFZBd45mqgYeSjQr8kFBRjX8nxV-CmMSsib08gZ0D78VnbMQMYQCsxxB5V0mKrPRUzXBvofGkyD2QczyORYzrsPx9dI-NcTobGxfoepqmioRu4BaL5gQetp02HJGC02sdKF25Mu7GYPu-myxAEQwqkgcJXbetBLisqzuU30yr1BcgRqHoop2iK4f0og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=rt26xAVe_096HbZV7GzaI-6JYevsRP_Xmyx_YaupELz0nHelK93VD2G-UlLimk4AIt7y2fK228nTFvi5qPl69WpWmfWEykahYLkNCzs2uCKoN5OUjRpseSYnZaa83ykug26sjMJI4ZShLu0iBIfw4tbouKIhFZBd45mqgYeSjQr8kFBRjX8nxV-CmMSsib08gZ0D78VnbMQMYQCsxxB5V0mKrPRUzXBvofGkyD2QczyORYzrsPx9dI-NcTobGxfoepqmioRu4BaL5gQetp02HJGC02sdKF25Mu7GYPu-myxAEQwqkgcJXbetBLisqzuU30yr1BcgRqHoop2iK4f0og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا سعودی‌ها بدون حضور نیروهای آمریکایی هم می‌تونن از خودشون دفاع کنن؟
ترامپ: «بله، توانایی دفاع از خودشون رو دارن. سعودی‌ها جنگجوهای خوبی هستن، اما به نظرم اون حمله اتفاق وحشتناکی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73095" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73094">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/73094" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73093">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1Yp4oPutgTmt3Gw-mYGwZag1k2kF1T1hsZbBeN4b_N4cqtpwbP9SqgLKaNMOgYVp9dk92poKhHER-38FNLkn9-CvY0-vGcRdHqdAhVpdk-s5qd-QwvQXS8u3JTNdHIg1IQrr_3S_jGhqSniikOu2TiGvZwbYwFca3iyuYyqiJqxrVfNTo7O1PgXjFcbUrNDB36-CGiPhN9f5eklyNaO3OibVDX8XejF9NOidOYp5pi3lHRTCjram_0QjRCaN7LbkC6jOm2ckjx5CdiBXhzjafRKDKUbictgKbwEXluillbUqlXfsVd203yrTL7kRG9HnRdxUy0oNzdJ_WuZ5tkjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73093" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73092">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e6800693.mp4?token=UDnBl7ePby5LePWY5-rrsi2YSv-fxXEZCTzY7wP-QG1Q0OjOFXyQf2-AJbD08GRhT7KpT9-jCo6MXzuOPe3-0hHGN98ylJKhr_erFtrx6_BgUxeTeJ9M-v-F_9DrFuNSBS83dXtm96EVGSH1hwmuOQzTCsOSIEaFQ3Dr9x_2eGHY4dB697w8IhR6O2022opYjvcV4xbeXdAqyaLpG41ejI-jyvCzPk6O_Ryq04xgzX1Gbtm7h5wKC41nrr3dgN-j8xJPXSeCTbbEbHEj3vTm-_zQ_TGCkFlYTCnS2r2Omkw36klZSPjQlx3Rwgld_ua3D8Zvx6EcmYpEhN5B3zDa7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e6800693.mp4?token=UDnBl7ePby5LePWY5-rrsi2YSv-fxXEZCTzY7wP-QG1Q0OjOFXyQf2-AJbD08GRhT7KpT9-jCo6MXzuOPe3-0hHGN98ylJKhr_erFtrx6_BgUxeTeJ9M-v-F_9DrFuNSBS83dXtm96EVGSH1hwmuOQzTCsOSIEaFQ3Dr9x_2eGHY4dB697w8IhR6O2022opYjvcV4xbeXdAqyaLpG41ejI-jyvCzPk6O_Ryq04xgzX1Gbtm7h5wKC41nrr3dgN-j8xJPXSeCTbbEbHEj3vTm-_zQ_TGCkFlYTCnS2r2Omkw36klZSPjQlx3Rwgld_ua3D8Zvx6EcmYpEhN5B3zDa7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام جمعه تهران:
توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد؛
غلط کردین؛ برید گم شید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73092" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73091">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=ttqWKqk_I1wR2HpJ0iYB0nXkTL0i0U-OG_xpyoAD2aNk8tRu-SAezY4LgNpjBvprWMUJBhBz6mobELXgUgMMRFyFdbputy_XkfsKNmX_5kHSqwLbuMznTz4LbB-ZTH4adzkNWecqkKg80bUd-WarQlOzlTHmFF7A6etRwg0oMfWhFT-ij0Ozjy_5RAz50pkWCky9rfbLIZzkuNQnGaKckmZyEvUBjlTo8_GjBtIGtzIvGPOPOdnCvvJVMA1Mm_franBJLO4YXvJ4k7g73VskGoKgmOKbp_diM4DTxWtb8CYZWk3s2HsqO4bA01c5lOos2ZvAC3uWMK89OoyhzycuPyN1lVYhBXa15dtAx1sZYt_R-Q_98RdYWVoCUCryIPFYAu_DODZZDL0KWFUnQaYUo-NbN5kWVyZvpunHurn5iXBmIM2QGwseN2aFVbo5GeBClEI345rWBmUyk24Ubq2VDBIBp0iStjSVrUzr7PgScwTfBdXlrB7VIofsnePdPnPZqhZVwu6SI8O243rqPTV-19PU36xNMcA26f-a4qAIWp2vISiYisHv6HuQjih7tCE2XVgR4DDv7ttsxGVimr-4bL-tstKvQWFjTOvur6KXvk7BxYNO_V5vNdOYMkMFP_PBoXiRTuaJnqWPz1dBpjS-4FgXibJouwqoFjGvTnGN3tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=ttqWKqk_I1wR2HpJ0iYB0nXkTL0i0U-OG_xpyoAD2aNk8tRu-SAezY4LgNpjBvprWMUJBhBz6mobELXgUgMMRFyFdbputy_XkfsKNmX_5kHSqwLbuMznTz4LbB-ZTH4adzkNWecqkKg80bUd-WarQlOzlTHmFF7A6etRwg0oMfWhFT-ij0Ozjy_5RAz50pkWCky9rfbLIZzkuNQnGaKckmZyEvUBjlTo8_GjBtIGtzIvGPOPOdnCvvJVMA1Mm_franBJLO4YXvJ4k7g73VskGoKgmOKbp_diM4DTxWtb8CYZWk3s2HsqO4bA01c5lOos2ZvAC3uWMK89OoyhzycuPyN1lVYhBXa15dtAx1sZYt_R-Q_98RdYWVoCUCryIPFYAu_DODZZDL0KWFUnQaYUo-NbN5kWVyZvpunHurn5iXBmIM2QGwseN2aFVbo5GeBClEI345rWBmUyk24Ubq2VDBIBp0iStjSVrUzr7PgScwTfBdXlrB7VIofsnePdPnPZqhZVwu6SI8O243rqPTV-19PU36xNMcA26f-a4qAIWp2vISiYisHv6HuQjih7tCE2XVgR4DDv7ttsxGVimr-4bL-tstKvQWFjTOvur6KXvk7BxYNO_V5vNdOYMkMFP_PBoXiRTuaJnqWPz1dBpjS-4FgXibJouwqoFjGvTnGN3tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه بریتانیایی ITN حدود ۴ ساعت از تصاویر وقایع سال ۱۹۸۹ میدان تیان‌آن‌من را منتشر کرده است؛ تصاویری که پیش‌تر محرمانه نگه داشته شده بودند و توسط تیمی ضبط شدند که موفق شد این نوارها را مخفیانه از چین خارج کند.
این مجموعه که حدود ۳۵ سال در آرشیو نگهداری می‌شد، شامل یک ویدئوی تدوین‌شده‌ی ۲ ساعته از سرکوب‌ها و همچنین ۹۰ دقیقه تصاویر خام و مخفیانه‌ای است که در روزهای پس از آن واقعه ضبط شده‌اند؛
تصاویری که کامیون‌های نظامی در خیابان‌های پکن، جمعیت مردم و پیامدهای آن رویداد را به نمایش می‌گذارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73091" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73090">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=pDrh84mphaUXlcIEIB3kH1gAR1x2kHyKfj3uQNNQCrZoQFuND6W_GcIBBuqXwc94wuqIPpLeTAsmZ4yH_B5ZGvqLlyVIBERlMc0U48Tkw0ybVJXlJbv5pOcpSFw-Np7VobAKip7PtSKHwnQWlB8kXQI_UgLeTkFAKoTClaIVWxsuifYgtQLzOnJ56jQ3BhZ5dq3ljGmne77tuITaOTzmJW9d0urDxlkWh1Vyk2S0E96-4OTzwBnfx5yND-GFBf_CR8mjItzi6HvLb7eYm33RjlBAjaOAzu1SByGfAd7CLqHpCAVelxK2TlsmGkJGSIFPjCOIsdS_aMqg7HATCUdyNDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=pDrh84mphaUXlcIEIB3kH1gAR1x2kHyKfj3uQNNQCrZoQFuND6W_GcIBBuqXwc94wuqIPpLeTAsmZ4yH_B5ZGvqLlyVIBERlMc0U48Tkw0ybVJXlJbv5pOcpSFw-Np7VobAKip7PtSKHwnQWlB8kXQI_UgLeTkFAKoTClaIVWxsuifYgtQLzOnJ56jQ3BhZ5dq3ljGmne77tuITaOTzmJW9d0urDxlkWh1Vyk2S0E96-4OTzwBnfx5yND-GFBf_CR8mjItzi6HvLb7eYm33RjlBAjaOAzu1SByGfAd7CLqHpCAVelxK2TlsmGkJGSIFPjCOIsdS_aMqg7HATCUdyNDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
فلسفه بازنشستگی در یک کشور اسلامی هیچ مفهومی ندارد و مسلمان واقعی باید تا آنجا که می‌تواند خدمت کند
حیف است که افراد ۸۰ و ۹۰ ساله را از خدمت کنار بگذاریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73090" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73089">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73089" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73088">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/73088" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=Ccro72E1mutdabuCpF-fJ2UsIixY3Q9emPOJauRg9kQvZWJFdqFpabgG-KhksCX_kmun6v0UJCgfUjZbFVKQjyxXjln2NS1840tF8PbNqSbYrm1Rx9fK2Zn0Ea5kR4jhDG19Mq-nNdLoqln8K0ewkYoI1cGHDSUSiRwv7wBZt193HbOPlLAtarp98IOU2XbC7WS3Vsa1AZFyx86kRKa-NbGrAuhdFR_xPZoY-Ojr8N9uM-JCiw7OUKYROvMzmUvyoVlkEYqP-CHkfZ9VmzpUss8cck3RkiatL0UuJN4MG9aLQqj_Lqea5DuzT1H0lUwRtSWSaS0cNhpkjwTKrOERtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=Ccro72E1mutdabuCpF-fJ2UsIixY3Q9emPOJauRg9kQvZWJFdqFpabgG-KhksCX_kmun6v0UJCgfUjZbFVKQjyxXjln2NS1840tF8PbNqSbYrm1Rx9fK2Zn0Ea5kR4jhDG19Mq-nNdLoqln8K0ewkYoI1cGHDSUSiRwv7wBZt193HbOPlLAtarp98IOU2XbC7WS3Vsa1AZFyx86kRKa-NbGrAuhdFR_xPZoY-Ojr8N9uM-JCiw7OUKYROvMzmUvyoVlkEYqP-CHkfZ9VmzpUss8cck3RkiatL0UuJN4MG9aLQqj_Lqea5DuzT1H0lUwRtSWSaS0cNhpkjwTKrOERtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«ایران کشور بسیار شروریه؛ بزرگ‌ترین حامی تروریسم در جهانه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73087" target="_blank">📅 01:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=N_NXuxpeq36mFSF41zcjmhslplFdE4GX-WEOqvnqK2vRafvTt80DnBjIh2w3wEJtI7GVPDSKI4NnF-69r3N4dTwAainDLwwT4ifrA5gUBX1D2ugLjASmfJLMk66cpsSlCW5zRB02l3Zit1V34jVZq24ph7_JUbuu_r3cVMIFmAeb4a-Z7u4ET21l5JHjQ45wOCwuQmvBwNbEqwmzg0TcQM_TY-yreFDXinFWchyz7oUbwVxToZ78RoOYquWAiqHi7VnHO34hGsQ9Y4NC7v8P44KIDCz8Gs8yp-alscsbDcx8Ara-HmYEeICBAjCB5f00vZrw1fv61q4gYedJ3Wpf5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=N_NXuxpeq36mFSF41zcjmhslplFdE4GX-WEOqvnqK2vRafvTt80DnBjIh2w3wEJtI7GVPDSKI4NnF-69r3N4dTwAainDLwwT4ifrA5gUBX1D2ugLjASmfJLMk66cpsSlCW5zRB02l3Zit1V34jVZq24ph7_JUbuu_r3cVMIFmAeb4a-Z7u4ET21l5JHjQ45wOCwuQmvBwNbEqwmzg0TcQM_TY-yreFDXinFWchyz7oUbwVxToZ78RoOYquWAiqHi7VnHO34hGsQ9Y4NC7v8P44KIDCz8Gs8yp-alscsbDcx8Ara-HmYEeICBAjCB5f00vZrw1fv61q4gYedJ3Wpf5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اون جوان‌هایی که در جنگ علیه ایران از دست دادیم، بیهوده جونشون رو از دست ندادن.
نمی‌شه اجازه داد یه آدم کاملاً دیوونه به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73086" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=tPo81OS3d8eYHgI-SAAe6SlChbX-iQWZgpzsoxHgxpvWFAYPpGCdwL6DQ6kpbqbNokGHxpVKjV54BUb62JmqOF3Kf-5-HfDWTwOoUOpGvQGlmbVD9zWUIlqeY0C0z_3_diAOqphSoGH8bvtncgagEfRJxEgRF2mQLyz5GObe4fL3xBPjzYWkWgYlUHLeEVFyyLWEX5EvfwBOx-8fj-JhrbZoJTCqSc6t9AdeVA-4sKx1uUCAhqURKX0uKA_bT7iKnjGeext5l-HyhxQC_USNRYy-1gbdjVAVvmitVNmzyKHFVycmGPt4jlebAYsZrYm5ricPxr6tObiRiMpALDrPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=tPo81OS3d8eYHgI-SAAe6SlChbX-iQWZgpzsoxHgxpvWFAYPpGCdwL6DQ6kpbqbNokGHxpVKjV54BUb62JmqOF3Kf-5-HfDWTwOoUOpGvQGlmbVD9zWUIlqeY0C0z_3_diAOqphSoGH8bvtncgagEfRJxEgRF2mQLyz5GObe4fL3xBPjzYWkWgYlUHLeEVFyyLWEX5EvfwBOx-8fj-JhrbZoJTCqSc6t9AdeVA-4sKx1uUCAhqURKX0uKA_bT7iKnjGeext5l-HyhxQC_USNRYy-1gbdjVAVvmitVNmzyKHFVycmGPt4jlebAYsZrYm5ricPxr6tObiRiMpALDrPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی املاکی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73084" target="_blank">📅 00:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=Q1hweJhHCQNpRFivD4gF497q_ONxgT19qJPqKjM7jW-Vszht9_zdxBRplWMsOY31v3nWx1_-SFOBEAltV4cjGwFFyDknOjiSfrwWsXMACvtczy6qT7dC4aUG5qyBDpy7Kb-Vj6NKo4h3m1aBGRIfh_bWHFH-0TdaGtnbeS2Y8-dyFMfY9F_P7N0SuiJ5nJFmcR93xSWdaWQF1v8Wpb1VWO6xyZqpEnTg4DNKgkqim7YmOmD8MAaXWJsaNxVU9b0fCplFJq2te10JnzPpdn9OUWQc1GFTgmGwBg61hUi9NC7tp854EWp6390fQh17slCwpg2LhqpOQk5piueS-bP_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=Q1hweJhHCQNpRFivD4gF497q_ONxgT19qJPqKjM7jW-Vszht9_zdxBRplWMsOY31v3nWx1_-SFOBEAltV4cjGwFFyDknOjiSfrwWsXMACvtczy6qT7dC4aUG5qyBDpy7Kb-Vj6NKo4h3m1aBGRIfh_bWHFH-0TdaGtnbeS2Y8-dyFMfY9F_P7N0SuiJ5nJFmcR93xSWdaWQF1v8Wpb1VWO6xyZqpEnTg4DNKgkqim7YmOmD8MAaXWJsaNxVU9b0fCplFJq2te10JnzPpdn9OUWQc1GFTgmGwBg61hUi9NC7tp854EWp6390fQh17slCwpg2LhqpOQk5piueS-bP_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی یکی از اعضا از گرگان:
بارندگی شدید امشب در گرگان باعث وقوع سیل و وارد شدن خسارت به اموال مردم شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73083" target="_blank">📅 00:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=d9jNXy228hYiosE5xL7wYAw_w6oyBBmxcNWlVJw9jY6vcDjPY6HTzAl0hB9GcYCYeMEG4QNLPdsFFIyvVuBmNzdF2iR1Z6sNWlY3k50lVBy_AdxBmvzXxx7x0JvcQ0HLygM_iU3GYXM6LF5__7ojKpgxEiYj_9EqN9xF_hAd-phWPKzpXm2OGiklkH6UC2xZ7DZGiJeCJAFEZ07UDchUp1TGMZZxnoTQ_1RyLw0XKwp5AZJsOzRGsMXNyD4yf17VdtrzcHcsfTlFg18dY3MzwMJsElGU3GLIPtKOEI69GdQUSs_4gGp7Kj8fMhAtCOdfGLxCUAhEBus6GSm-nIH53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=d9jNXy228hYiosE5xL7wYAw_w6oyBBmxcNWlVJw9jY6vcDjPY6HTzAl0hB9GcYCYeMEG4QNLPdsFFIyvVuBmNzdF2iR1Z6sNWlY3k50lVBy_AdxBmvzXxx7x0JvcQ0HLygM_iU3GYXM6LF5__7ojKpgxEiYj_9EqN9xF_hAd-phWPKzpXm2OGiklkH6UC2xZ7DZGiJeCJAFEZ07UDchUp1TGMZZxnoTQ_1RyLw0XKwp5AZJsOzRGsMXNyD4yf17VdtrzcHcsfTlFg18dY3MzwMJsElGU3GLIPtKOEI69GdQUSs_4gGp7Kj8fMhAtCOdfGLxCUAhEBus6GSm-nIH53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=K0Ep-h7D2SW28osZQls1u8Pq_T64eghUT2YUoPweK_vKixu-lW6y-xPUjsqrJg2j1U2JvVY2civB6f0YKuIdxo5x8e5Z6A5lrLOh3yK0V6NsqhZBisPTFuQAF8ihuwf7AMJkq0fQ13MPwKxApWgx26YVqCsIvbRt1Vq1XvacYvAZNgLZ6UUYgVLCQKepwrB7XCoFRjlD2zzLbNln4HQIiv2pUrWBrrlnUgV0AepbB0GdE9e_Xclkrb3YZs2hq_nNozCrP2ke2ecUwwepG8YNGE1Y6TnYkgcKT0HMAEMVsoBXtK4gWzfDqG11F3UJITUaEOG-FgaAbAH3ivmm-U6Ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=K0Ep-h7D2SW28osZQls1u8Pq_T64eghUT2YUoPweK_vKixu-lW6y-xPUjsqrJg2j1U2JvVY2civB6f0YKuIdxo5x8e5Z6A5lrLOh3yK0V6NsqhZBisPTFuQAF8ihuwf7AMJkq0fQ13MPwKxApWgx26YVqCsIvbRt1Vq1XvacYvAZNgLZ6UUYgVLCQKepwrB7XCoFRjlD2zzLbNln4HQIiv2pUrWBrrlnUgV0AepbB0GdE9e_Xclkrb3YZs2hq_nNozCrP2ke2ecUwwepG8YNGE1Y6TnYkgcKT0HMAEMVsoBXtK4gWzfDqG11F3UJITUaEOG-FgaAbAH3ivmm-U6Ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_7capl8I0SDEWoIP7jIcAl85xlo7GiRH4bONynw3iOnt59AUob-npTlI84HBG0sT5Dx81W1UQ-NEJ2c4UrBU7ESsY5gjqzH4ePbWhdtQj_yzpZMroNS9PcBUGgj_AZqVPsj13_bUHyOvX-HNjBJx-VeG_28FapliyvLGPpAg0uLddTvS1lJCRVCacq5lfQk3JyfyRYwoJ78xZTRClQkkIGiZRHfyocxixbX4bM2DxZSlnVtYJVhhkyZY2VNlEYD8cELM6_m_ECbDm_KZ3FFdimJFRFVRUQJ8gEgsH0RLXxgbyyayx_26acy5I4tl8JMlJcFK8aTsyjlrbZHFxqEzLy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_7capl8I0SDEWoIP7jIcAl85xlo7GiRH4bONynw3iOnt59AUob-npTlI84HBG0sT5Dx81W1UQ-NEJ2c4UrBU7ESsY5gjqzH4ePbWhdtQj_yzpZMroNS9PcBUGgj_AZqVPsj13_bUHyOvX-HNjBJx-VeG_28FapliyvLGPpAg0uLddTvS1lJCRVCacq5lfQk3JyfyRYwoJ78xZTRClQkkIGiZRHfyocxixbX4bM2DxZSlnVtYJVhhkyZY2VNlEYD8cELM6_m_ECbDm_KZ3FFdimJFRFVRUQJ8gEgsH0RLXxgbyyayx_26acy5I4tl8JMlJcFK8aTsyjlrbZHFxqEzLy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=LjOS58O-f__O1hPHbxYzHnHTH2h_kYY52MtpXI-2XvUohwlxbICY6c5SxkKnqQqlaHB-ofmE4Wu5fUP6g4UkP3__S1UiQQGxqHCtNt3wu8ZGOJwp_hFflRYqfWyYZ1vPTHjHHJYC5RM9cvFwH5dmG4cuzp1gqTXTyLyZbfcmsA_m0P_g2PKQJ0IaqN98ZeqKW8LW4WX4iSZ84c6Z6ZAIiVLWrjo8Ju66y3s1XYsGSHuXK_ZitlM9LRXdTeg5-ft9KCeqeQwaxkZoSKZZer1RX0ncOfS3cTtKV-shS011UB4dUlqYhFd8u5jyN2fwBckQp6VOQAjtEbiMOtbDyHbIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=LjOS58O-f__O1hPHbxYzHnHTH2h_kYY52MtpXI-2XvUohwlxbICY6c5SxkKnqQqlaHB-ofmE4Wu5fUP6g4UkP3__S1UiQQGxqHCtNt3wu8ZGOJwp_hFflRYqfWyYZ1vPTHjHHJYC5RM9cvFwH5dmG4cuzp1gqTXTyLyZbfcmsA_m0P_g2PKQJ0IaqN98ZeqKW8LW4WX4iSZ84c6Z6ZAIiVLWrjo8Ju66y3s1XYsGSHuXK_ZitlM9LRXdTeg5-ft9KCeqeQwaxkZoSKZZer1RX0ncOfS3cTtKV-shS011UB4dUlqYhFd8u5jyN2fwBckQp6VOQAjtEbiMOtbDyHbIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=iM6V_42gLx2ic7d26-2SJ9wWXJRfr-nhDl1v0ZyLSIU2TuCrObcHfcjBmeno33Pjd7X1F0l6ByxxkWdEO8PECuEkWoFYrnw-R9M8ZJVDeuMCb7PXJcyov9QTw701PJcyUArn1dP6Qbfq268mCSYdoPUaQIGh1PxUl6PLRqixc5fgIuq4by6vBQ36KaC7wjq1wV-L9NzN-30E8VvdDlPauUHMseUHzl_Cr8e54vrVfH4PjzOC_NAeAmkNqrhTo_5b8CbN4SDWTKjCNUEhW8ZSjyx8F1_ttJ3t9Y6iS2elyHuUhINyr-eQOBauij8IvxKtDOSNnDIevHmfrCsTkZT5lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=iM6V_42gLx2ic7d26-2SJ9wWXJRfr-nhDl1v0ZyLSIU2TuCrObcHfcjBmeno33Pjd7X1F0l6ByxxkWdEO8PECuEkWoFYrnw-R9M8ZJVDeuMCb7PXJcyov9QTw701PJcyUArn1dP6Qbfq268mCSYdoPUaQIGh1PxUl6PLRqixc5fgIuq4by6vBQ36KaC7wjq1wV-L9NzN-30E8VvdDlPauUHMseUHzl_Cr8e54vrVfH4PjzOC_NAeAmkNqrhTo_5b8CbN4SDWTKjCNUEhW8ZSjyx8F1_ttJ3t9Y6iS2elyHuUhINyr-eQOBauij8IvxKtDOSNnDIevHmfrCsTkZT5lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=TWDFhEq08xVY_eywXrJI-OeZhnGOjxcRcjhdcfsz0NEF_-HD8i4A99aVBEqbsmquTEg0OKsjG5Shoqu6bPT1EYL2H3odBEccYgOVvQOI1Pazg_bScwSkOURNabwk_QTNYBpxv7qKIZkPPxCabUgARuApsLXW-YUNGE0Gdm63KLK5lsReXmKmfexmswdS0UXtbvEAGsMIPNv1Bm1WqjMrbJcyZDZ5GO3pLsCWMaRJh027KSkenULvuir1r-IZe4J0WzwTs0e7Rfn6ZmTIaD7QjRPvqt6ilwJXXBabGWfT-vbDF_xjZGEludm_XOqp1j0eHl1ed_arw3Hy0R1VyGxOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=TWDFhEq08xVY_eywXrJI-OeZhnGOjxcRcjhdcfsz0NEF_-HD8i4A99aVBEqbsmquTEg0OKsjG5Shoqu6bPT1EYL2H3odBEccYgOVvQOI1Pazg_bScwSkOURNabwk_QTNYBpxv7qKIZkPPxCabUgARuApsLXW-YUNGE0Gdm63KLK5lsReXmKmfexmswdS0UXtbvEAGsMIPNv1Bm1WqjMrbJcyZDZ5GO3pLsCWMaRJh027KSkenULvuir1r-IZe4J0WzwTs0e7Rfn6ZmTIaD7QjRPvqt6ilwJXXBabGWfT-vbDF_xjZGEludm_XOqp1j0eHl1ed_arw3Hy0R1VyGxOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل به ساختمانی چندطبقه در غزه
دقایقی پیش، جنگنده‌های اسرائیلی یک ساختمان چندطبقه در شهر غزه رو هدف قرار دادن. پیش از حمله، دستور تخلیه ساختمان صادر شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73074" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=TIrsM5FC9u4cbX3VlzUEh2l0WgTYBYkHIMmk7BilcVPQ6ag1Mzv0j4XDgBT44eUDH8mvCYqTRhj6a9Yu28w6NWfek-30psxPUp4RK5uI0AWUP6afgyZ6EoLB1UAkeW3iLCTS_y5GkiSrNZnIdyrD2tOpmICxeTUyraX-t6rMpHepPieSw4NqMjYZzFUxslKua4llOpeOqLXzX38FFTXJufTDIWhFbky6dQW_Uwe3ePn1VLhKMaUOXUMq-aDgtS-6T_VrHQT3YDUeTX6BBFwZJEOqSWKtyR3exKP-NXRsCxtUB75w0QzPHbtVtHDP4BKbg6ao_tDdcqqGI3zGj9myOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=TIrsM5FC9u4cbX3VlzUEh2l0WgTYBYkHIMmk7BilcVPQ6ag1Mzv0j4XDgBT44eUDH8mvCYqTRhj6a9Yu28w6NWfek-30psxPUp4RK5uI0AWUP6afgyZ6EoLB1UAkeW3iLCTS_y5GkiSrNZnIdyrD2tOpmICxeTUyraX-t6rMpHepPieSw4NqMjYZzFUxslKua4llOpeOqLXzX38FFTXJufTDIWhFbky6dQW_Uwe3ePn1VLhKMaUOXUMq-aDgtS-6T_VrHQT3YDUeTX6BBFwZJEOqSWKtyR3exKP-NXRsCxtUB75w0QzPHbtVtHDP4BKbg6ao_tDdcqqGI3zGj9myOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73073" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be565181a8.mp4?token=KbJUbQZfUhplbhfP46q3BGjqym_v4Fkk0pr1DDVemnfpJXQ7iuqKmq609HRAbN9aBoNWi30v0ictD5D-72yCJ7GjRnRvvON7KuzVKKD2BUuQmkvSY8QZDauDtkrZ4uvEcwaJaB2aJml5cgGWKwHBWAU4Vq5sdzS5tU4c2e8ohF2YiKjp06l1wFAw0fJyL5fQiDqyhBXxSK60UKVFLUlKgkoVukdc0uJ_HDXqPRHP1dzHmlQCuSsVCk-QlYydaYwpKcz0gYC-BS9_rl5jtmju9MD2C5E26Qg4Ivc3DWaCC4NdqUzNUJAoXhjVlgCixvgo8Mfmn3Zq4Y8CKwNf62CVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be565181a8.mp4?token=KbJUbQZfUhplbhfP46q3BGjqym_v4Fkk0pr1DDVemnfpJXQ7iuqKmq609HRAbN9aBoNWi30v0ictD5D-72yCJ7GjRnRvvON7KuzVKKD2BUuQmkvSY8QZDauDtkrZ4uvEcwaJaB2aJml5cgGWKwHBWAU4Vq5sdzS5tU4c2e8ohF2YiKjp06l1wFAw0fJyL5fQiDqyhBXxSK60UKVFLUlKgkoVukdc0uJ_HDXqPRHP1dzHmlQCuSsVCk-QlYydaYwpKcz0gYC-BS9_rl5jtmju9MD2C5E26Qg4Ivc3DWaCC4NdqUzNUJAoXhjVlgCixvgo8Mfmn3Zq4Y8CKwNf62CVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش مصاحبه یه دختر 25 ساله منتشر شد که ماشین 50-60 میلیاردی سوار بود!
بهش گفتن چطوری این ماشین رو خریدی؟ گفت تلاش و استمرار!
رفتن امارش رو درآوردن، دیدن باباش حسابرس شهرداری تهرانه و دختره آقازاده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73072" target="_blank">📅 21:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=lqtTQB1kMb-6Itxo-DzBzYgr9ADKFHl3cz3qg8wVqmf1erm2Dq8NCJnDPawfXlNfifH5Vz4m4fxqrL2jx_c1s6EdKxT8vhSR27kvsCZHpX46NcXMVJd5OwzoiGFPGXHRN1qAX6NkFrkCP2YU9h8lU8JHD9kG-f5doE9ittxguH7c8UOlmRO6Tg3UUBxKCmeu7vLBuGDaEPIUdpLp4t8qbMePkew81iQQbUbWMOtsnXNz0pHHCroPVmKFmiml4cn-x1g3tGWKmJq7-i12BFqO6EK6SwmP74JVKZv_8mnqfMjcn9OGYUMvdIxCzXe8ckc0Fu-5NikPawQ7Zj6jhEzAxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=lqtTQB1kMb-6Itxo-DzBzYgr9ADKFHl3cz3qg8wVqmf1erm2Dq8NCJnDPawfXlNfifH5Vz4m4fxqrL2jx_c1s6EdKxT8vhSR27kvsCZHpX46NcXMVJd5OwzoiGFPGXHRN1qAX6NkFrkCP2YU9h8lU8JHD9kG-f5doE9ittxguH7c8UOlmRO6Tg3UUBxKCmeu7vLBuGDaEPIUdpLp4t8qbMePkew81iQQbUbWMOtsnXNz0pHHCroPVmKFmiml4cn-x1g3tGWKmJq7-i12BFqO6EK6SwmP74JVKZv_8mnqfMjcn9OGYUMvdIxCzXe8ckc0Fu-5NikPawQ7Zj6jhEzAxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.   ترامپ: کی اینو گفته؟  خبرنگار: زلنسکی.  ترامپ: باشه!  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73071" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=lSFhp1p8wmYEMI6qpKDnp7dGt2KVzMg7FzhiVx1pOval7SLYELAOqTm_ZOf7G5uxQmevq1HafGgnr4Uar_knabuydhKEV3m_8o_fA7GXtWFFzZiFpyLVCwwP61tYJ2k7SabE1Q_C0XsFBv-ssee1NuvZNNM5fKbUE3kvgz03ZWXxPH1ag6ojP9Z7oRPPw35ajvFToj9oPSP_lDIg5sgX3mP6yIZp2hB9-yfjFBNLrtLtXy4ZIGPQYxLpkD1CE_MQowG4f0Nb_JyeGTI7r5-04d6byYsQSjCBnb_iRDVrit66p9WuvnAySMacNZ_7zzx0lByNsNitMmWIAJ6orcBrtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=lSFhp1p8wmYEMI6qpKDnp7dGt2KVzMg7FzhiVx1pOval7SLYELAOqTm_ZOf7G5uxQmevq1HafGgnr4Uar_knabuydhKEV3m_8o_fA7GXtWFFzZiFpyLVCwwP61tYJ2k7SabE1Q_C0XsFBv-ssee1NuvZNNM5fKbUE3kvgz03ZWXxPH1ag6ojP9Z7oRPPw35ajvFToj9oPSP_lDIg5sgX3mP6yIZp2hB9-yfjFBNLrtLtXy4ZIGPQYxLpkD1CE_MQowG4f0Nb_JyeGTI7r5-04d6byYsQSjCBnb_iRDVrit66p9WuvnAySMacNZ_7zzx0lByNsNitMmWIAJ6orcBrtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=p6dWQrapqXNv8L6CjRnlF5WGqqlTEcLSPGB2QA8boBbTNpmq5OaJhpbW-FBOrVQxKkwlJYaocQm8co7x3ZQwLD6aDk90-7NsYxl6Qe_PvjFoWl3OjYtMk56hRnncOv98WTo8t95G4QlB5iPNcOcysjcM6VPeol7YyxRLWLiITu7yNyThJya37EsB_sm-GvdYRHnLtPCteLODFq3m4V3cEp71BKgzHIXisGWYmXesGuPjLF6I1W5FcfNOB2tGc0OfXxjhxfbLUMirShvROSMW11NHTCCJnw7Jfzu2Qn2AEaZOCuO00QZLED-vRuk6htd8Z-bwDqXWZWOdfvYySlTCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=p6dWQrapqXNv8L6CjRnlF5WGqqlTEcLSPGB2QA8boBbTNpmq5OaJhpbW-FBOrVQxKkwlJYaocQm8co7x3ZQwLD6aDk90-7NsYxl6Qe_PvjFoWl3OjYtMk56hRnncOv98WTo8t95G4QlB5iPNcOcysjcM6VPeol7YyxRLWLiITu7yNyThJya37EsB_sm-GvdYRHnLtPCteLODFq3m4V3cEp71BKgzHIXisGWYmXesGuPjLF6I1W5FcfNOB2tGc0OfXxjhxfbLUMirShvROSMW11NHTCCJnw7Jfzu2Qn2AEaZOCuO00QZLED-vRuk6htd8Z-bwDqXWZWOdfvYySlTCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=ov0QZyjyKGr8wh1lUfQoOeZsjw-irrLwvVQuERPBYbES5QHrKzv6T9ioGoKrKvcOyiitnBkxZT87VAzSrEw9adFAAJJbHaK7g3FG_RSh8LqVUJkHLKW_Q-AAjHALWhr7g5YsJsTMILUoF8xmHJo8kv3QEJDXe5ShT8QxBl1VFn1jQs1HqjCmttItBlN4JkMDCQX-Ne7JgXpO51McJkzRJfqY42Sj8BTKPueWl8Yfl3Bu0O3_eaSaa86Ygv74tqY_MQdnOWKD3IMxz-OyDMjwhl2cVh3ZKas1Vi6Y7KA8PHB6LKq1bBfy0m85OsmZmigM8EB67fkL0wJ6jClm291P5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=ov0QZyjyKGr8wh1lUfQoOeZsjw-irrLwvVQuERPBYbES5QHrKzv6T9ioGoKrKvcOyiitnBkxZT87VAzSrEw9adFAAJJbHaK7g3FG_RSh8LqVUJkHLKW_Q-AAjHALWhr7g5YsJsTMILUoF8xmHJo8kv3QEJDXe5ShT8QxBl1VFn1jQs1HqjCmttItBlN4JkMDCQX-Ne7JgXpO51McJkzRJfqY42Sj8BTKPueWl8Yfl3Bu0O3_eaSaa86Ygv74tqY_MQdnOWKD3IMxz-OyDMjwhl2cVh3ZKas1Vi6Y7KA8PHB6LKq1bBfy0m85OsmZmigM8EB67fkL0wJ6jClm291P5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=umshPRNqZR1osLbMN6js7NyBuKIvg6fOxX9sCsHwrk65pXhDhcswn5YU9Kue5c3pWPMDfNIe686YelI_mnSNL7BpJQxO02PbSSUfFtKKIhd3S1aFxBq3b2AdBE-tTdLoXjW4oAuj_yS-GxpLCCntRM65aDgPKqWRplTcE11NvkhGmNCKWRzznbHiWCBNUUWD-17icAdvncJlhXJEZMcTO3gwquleC-lHYHRfOXtcCadxWaK83ei208AZ8hyUO0PXxn7Q8l1kG-XHSWX8jCZjZwYJutyr3-7GWd7whos0MBY9F5E_gYOKHtFPk8v_Ium9zGiQ7l6W0G4t52OtYk5Zvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=umshPRNqZR1osLbMN6js7NyBuKIvg6fOxX9sCsHwrk65pXhDhcswn5YU9Kue5c3pWPMDfNIe686YelI_mnSNL7BpJQxO02PbSSUfFtKKIhd3S1aFxBq3b2AdBE-tTdLoXjW4oAuj_yS-GxpLCCntRM65aDgPKqWRplTcE11NvkhGmNCKWRzznbHiWCBNUUWD-17icAdvncJlhXJEZMcTO3gwquleC-lHYHRfOXtcCadxWaK83ei208AZ8hyUO0PXxn7Q8l1kG-XHSWX8jCZjZwYJutyr3-7GWd7whos0MBY9F5E_gYOKHtFPk8v_Ium9zGiQ7l6W0G4t52OtYk5Zvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNW4nGjrPt0Qbc0AjGoqUhp3D-lKJqD2UWql8FvkG7DmF-uu9FQ_bWOvf3xP2TCMKdfXv7Dq_7ju0nZ5juIM2HTGXdg2GeWZNedYRBKa7Tt6deUgLJwW8MwGQExnvya61hfnoFpo8-D58YcfNjOedRbH9nbro9gjpR4miXxba3HTUz6cqrTiw9YnQfWZmrtBFa6YZOKNUAMgWP5CVTI9iGobZPgY1XUGNZuoKyoFGueLiEfISQ_DfujWPLs5EOPgHtlBtFadjDgM2v9YzemnyavE5wq7xkEj9ARm5kwg_JK8rBN3kLP49qR6XxJqHH2KPFbY2rd_tIRpnMzEU_w3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=o75i-cmlyRxxU9K754OQmzKQNoMpEcQ4FlG0qs5elBljEMOk0zBIGP4cStmcFS-6Wwjx6uDjTg4l0ob1SHzUtYIpqnyr_DYdL5Whkjtd2BryTJo9zcm3WWtNYwaXQDZkf-w0VtCOUaGjybblJYqMpKdQ2oINlfRrRteLGc1vUkT8SzI8aNXUXEIVTI1HPaTucaKbG4mv9yoJcnVAJb48S1npyxnzXpmO1L2rOBdsw7IgiWxqu7zDCKc5qTQ5CL0J35p6Cw0T0ibMleC3XwZbttNqWtP5KdCLxX9D7fMA4MDNYiU6QPC927RQ8gB8KFoWkcUGc6AJj9RJVds34aU_6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=o75i-cmlyRxxU9K754OQmzKQNoMpEcQ4FlG0qs5elBljEMOk0zBIGP4cStmcFS-6Wwjx6uDjTg4l0ob1SHzUtYIpqnyr_DYdL5Whkjtd2BryTJo9zcm3WWtNYwaXQDZkf-w0VtCOUaGjybblJYqMpKdQ2oINlfRrRteLGc1vUkT8SzI8aNXUXEIVTI1HPaTucaKbG4mv9yoJcnVAJb48S1npyxnzXpmO1L2rOBdsw7IgiWxqu7zDCKc5qTQ5CL0J35p6Cw0T0ibMleC3XwZbttNqWtP5KdCLxX9D7fMA4MDNYiU6QPC927RQ8gB8KFoWkcUGc6AJj9RJVds34aU_6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=HzMsceR37PB6Mhw4t3gh1gwVY5Wyxig6ABNkBWHkJMVoBv4spqMdkLmrF3varvCN7iB-FRaiDWF1HGk-6WMXCpAY2FgKI9DD2wF2wpdGOpodzVyUZvXAdQVPQFI_w5e5uSsz6UP98buN2c4XjHtTju7u0rG-JDbHITqAo7RR78MqH-iXi117Q6BwqUt8r9OzTV65-AVb0DBPYjUJDe6y5tTleafs_6AZrIliWmh0aVDnnipAWSIFrtj4lzQsaT3G6-Y0_6ZDy4LFKwDdnUlNlGNcEBSrQye9MVWg9jlEp74HAeFYyhkak6S2UDTCVVq4uvZJTvPH6FktyTxYFgvlVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=HzMsceR37PB6Mhw4t3gh1gwVY5Wyxig6ABNkBWHkJMVoBv4spqMdkLmrF3varvCN7iB-FRaiDWF1HGk-6WMXCpAY2FgKI9DD2wF2wpdGOpodzVyUZvXAdQVPQFI_w5e5uSsz6UP98buN2c4XjHtTju7u0rG-JDbHITqAo7RR78MqH-iXi117Q6BwqUt8r9OzTV65-AVb0DBPYjUJDe6y5tTleafs_6AZrIliWmh0aVDnnipAWSIFrtj4lzQsaT3G6-Y0_6ZDy4LFKwDdnUlNlGNcEBSrQye9MVWg9jlEp74HAeFYyhkak6S2UDTCVVq4uvZJTvPH6FktyTxYFgvlVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSguG_AZvcDvzZYKkKXAw2mSTS9MyAH2Ng7juYrwoxF_b_7THQanzx3uqzM-JDkX5jFiN4fZa4PUjIroHD64i94j2tV088YLnu6XGJY8SXz1lSJAfN5xyWz3viGvUkEVFsMXz6_uerst-9UUpqvUMtCh0GPms5IoEXlR3TN8Pr423BfuKLtdF3KEGJeFZ-Zvlw4zZo4UyN5hMn0Chb1qzOyuFqIh00a9dkdwuC0HWexJrzMvi7Xk-QZ9ENoWZHJiO44sVrC6QENxLOU-CkXKOJFL6X-UL0Anj8IGz5njvkmM-f-5dRgWAG2iqY49t9eHGaNHa5RErYADCmTUTIadJZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSguG_AZvcDvzZYKkKXAw2mSTS9MyAH2Ng7juYrwoxF_b_7THQanzx3uqzM-JDkX5jFiN4fZa4PUjIroHD64i94j2tV088YLnu6XGJY8SXz1lSJAfN5xyWz3viGvUkEVFsMXz6_uerst-9UUpqvUMtCh0GPms5IoEXlR3TN8Pr423BfuKLtdF3KEGJeFZ-Zvlw4zZo4UyN5hMn0Chb1qzOyuFqIh00a9dkdwuC0HWexJrzMvi7Xk-QZ9ENoWZHJiO44sVrC6QENxLOU-CkXKOJFL6X-UL0Anj8IGz5njvkmM-f-5dRgWAG2iqY49t9eHGaNHa5RErYADCmTUTIadJZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
