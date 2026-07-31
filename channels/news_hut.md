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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNEoa3z83DhAmzHX79exkK9qm8caMwF6_7-43V3W11mOpO16TUjW6oYvzNnOtBDb6sFSBgN5grLxLYFwLspNngtuW_HLTrfFibu3cy5gjzKo4A1C3iu2XY-VJ6Rn5kXgWofx3NdaiaZ2je0neZlXIJ61Mi5eFItEexiZDzp3wX_syg9v2EpSgvSZtzmOYO7-7qDNa4dwyIGhQ9lAiXIVL558iP4TdrLO0DW3pcI3ZvaCiR7XEpLpeBlpyIZl86JzVPeR8h_i-lo7OzfT7_TdAidV1Um67Ni2jm1mm9dK5mSqt1quvtRQ2AwcBDkYTnEuxnCyjfbisRhx4UnTQ-QMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT0CMqL5pPY3arsHSxgGKfOSv2B5DwmznjC3YRpW0B_11eqtUwcgQqVSwuvY6_mV49Sd_9ZA2SogOD2z95i6b8lHSjoYGMJffj53FxnT4yfyeyIJwqFmYLWJkao3xDolM7fNNmBP-f5P9ZXq5dE9z3F8FY7blInvMXqlLVRw3KkJIbppJnRf5qofylH29tF9BbQNWq8av_FVr8dXk39XmG8sL6nX0M2y6AprRWs6fhJJFxd8Dz0bHg2jn3H52GnHr5aDMFCOItYnIN5u56wuAmx0jZ9bf9F2eS-Ps93GMewhegq6XZjskDUV8xBxcJI5soJxjHBp_TtP5w9ZheuSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1tDxlaxzjR2YB9JxyQWxuEnwLhHabUAIQq8wr0VnJc4sZ7f9oaXx_v9rf2svFmKudl5VVBzBIkXlMttV1rZojBaKnbzGnnyXTIcgEu0gvjgKec83vxZkUcWSfJy60u8c4IDMGnCa_H8NpecIDQuHGXgHsWquRatVx-0UaWDELHqTAcOm3DyM6AF3uMPG7GIw2kAMWzuM9gskdP3FxZTCBwQlvJMPLVismSd6uupipiV9EobYGeqSn8vN9OOq28jQ2-rYFpOPlbNldowfMmW3jCwtITuQynlhmK_Q0QSA0ehmwvFTv30hR1EwCceKd5-qKgQaazAAR28nicUIAthvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dHmabU2NopAQjTroZ22lBRTZYwcCKbxVRa19oJvFM0Z-3xdmteqbv4vndGO8_4Xx4ZSE1ki4DqdKqNliZ66dpUsJXYE2moxPGuNwSATShqYsLZ1o1LU8Yh-TOvbEXNCwxF2b_xbu2x5TjISOsNbjpLLIb65BCV50ub76jSo9NvRqdTcqdkM5AEINzNHkUq-sOENwuISAF0B7A7HsOvcvFIpxqRlXjW_VYMtIRiNIEsa8RcV8mLH4Kz-bWzIeSxxbWaNkfM_6PTuRS8h6PNMdsUE4gl45Y9AhgQnN0OJQFQCIoe3pRuxUjSMOYBL3cp1BQenMVju_SfyWX9AODhWS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=dHmabU2NopAQjTroZ22lBRTZYwcCKbxVRa19oJvFM0Z-3xdmteqbv4vndGO8_4Xx4ZSE1ki4DqdKqNliZ66dpUsJXYE2moxPGuNwSATShqYsLZ1o1LU8Yh-TOvbEXNCwxF2b_xbu2x5TjISOsNbjpLLIb65BCV50ub76jSo9NvRqdTcqdkM5AEINzNHkUq-sOENwuISAF0B7A7HsOvcvFIpxqRlXjW_VYMtIRiNIEsa8RcV8mLH4Kz-bWzIeSxxbWaNkfM_6PTuRS8h6PNMdsUE4gl45Y9AhgQnN0OJQFQCIoe3pRuxUjSMOYBL3cp1BQenMVju_SfyWX9AODhWS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=bqTfJfmsGnevR-m0TZYYwm93yGaAjS0yirk1hkmHkJNiJ9z8uMikPoKvQyZNNyCf5In5rpUws4fI_MzDiORskTegCuYaY1ApWNm7TfP0DdFL1oeFhTOUKc5McQUKAMR0FkgGyT5CRQSXYlm35OSq3ILXnh3P-ZRcTP8yxP1IskyzQnK9H8G4oQLWx9Pf4lkgVF4uZDlj4bk9KWRpuK2xhv5bvAnaUw924kLi8MkeQ6v3sBo6agubVOUgl0Zg22NyN5ky3bcxB3Rx47ohgpiJl5_IY_r9618DH9UCymDNmwHBpf-2WB-UHjUdziSH3Jma60pY3p80rCKFQbu19jq_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=bqTfJfmsGnevR-m0TZYYwm93yGaAjS0yirk1hkmHkJNiJ9z8uMikPoKvQyZNNyCf5In5rpUws4fI_MzDiORskTegCuYaY1ApWNm7TfP0DdFL1oeFhTOUKc5McQUKAMR0FkgGyT5CRQSXYlm35OSq3ILXnh3P-ZRcTP8yxP1IskyzQnK9H8G4oQLWx9Pf4lkgVF4uZDlj4bk9KWRpuK2xhv5bvAnaUw924kLi8MkeQ6v3sBo6agubVOUgl0Zg22NyN5ky3bcxB3Rx47ohgpiJl5_IY_r9618DH9UCymDNmwHBpf-2WB-UHjUdziSH3Jma60pY3p80rCKFQbu19jq_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WN0bGlbrSHUJyW6kt4JZqOio16tYtgn-N_986P2CLZ6WD8sVzWkvK2cyRKnhU4Hj6GM-VBotYuYhr15GFiC1lTNZIi9YvH-9YMoJpGDiuW-16XhGi0mv9WgCvaPuPHYJvnAcVGBZ7s1K1NYTR1q_BiPNKojfGCc6Af2Eot4sjW-4hZxclMK5p9Q8CUsEuopM_gSNzZm5G_nNxP43APECVIfa85hFycQOGdNUphM1-bZ8gG2gkqjTcErWdFaKJuvQfXlJ0-VYySnjNgw7N6OvmijbESp9MVydmSxKifioA_If50yNbHDIMoutogHnKUtA0N-j_lBE_unl4FrGq6FWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=cLT4ZhsYrrh_9AUixZ98SIG6HqdDBdHzSIZe-iC2xm4uqBUgzL8HM6286Hr9c7D8583YDl8dWsklLeVsgjTCWQZ3D4kx3fk5oe1BTy0MtwD8-Iasx-oYSyY46oYM_gceI7h0dgPDsVpDXTHFzQgkFnxKQ3W34NFiA8dEoZGXEXJmj0qLLbLOiFsQcFP3neAsOpJyR6LAGOJqOTN4-Vm2Qr7A0jMGZGAu8VL-Pk5HnFfYD0ejO5mCbd2ZQWJcklG5ExQ3cOsu40UIPOJbTWVLwWlj4aD7k7M_Sk1FBZi72QjgTx5sWiELgqVWScyz4FxfEWBOjI3TS49rzWAnrv13DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=cLT4ZhsYrrh_9AUixZ98SIG6HqdDBdHzSIZe-iC2xm4uqBUgzL8HM6286Hr9c7D8583YDl8dWsklLeVsgjTCWQZ3D4kx3fk5oe1BTy0MtwD8-Iasx-oYSyY46oYM_gceI7h0dgPDsVpDXTHFzQgkFnxKQ3W34NFiA8dEoZGXEXJmj0qLLbLOiFsQcFP3neAsOpJyR6LAGOJqOTN4-Vm2Qr7A0jMGZGAu8VL-Pk5HnFfYD0ejO5mCbd2ZQWJcklG5ExQ3cOsu40UIPOJbTWVLwWlj4aD7k7M_Sk1FBZi72QjgTx5sWiELgqVWScyz4FxfEWBOjI3TS49rzWAnrv13DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vttN1s0h7TKAf_frPo9ce-a21jC_c17SLTwQhVBG0taJvi4X1AXXDdU3-7jv2V0Pa2vvFJ33B8c51eaxSYE3o1e2bGt08o8TsDbf0iuxubk4wdArABpN7jtouZjVCCuEitB2ifnWAmefH_yqNtzL6mo8kXcwdEvBipLpE-b1swXtbxINLOUdn0VLXnJDg1gZOesVEf-VGp6Ylabxha90o9bJQnELGu-rHqM205RP1IF6RTMRP98Xg86D-dTQuOaoAqtEs8GK--fRUvMKzAYGBKEUxz3ksxyZU7VPU0p0nUZlDhJLsFrFcT1zIEgdzdnswXIW8BszWixdc28NZ-GZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1l9Dk0teRffYIOrRzaJyBf6438qW_BiOznbkjB7lzPaWG3YHEVcTXVW3tTvzgO5VS0c470NKQoHW9mOCXVVbe5vlxI2JUydgl1Dx8TAA0wLtTkvSr8c_1y7F3OVIlIV03HZIyVOtHV46AMV2izfitqEGQaN3p1iLyaTZyNXAd_zGsVzFF50HTy53Hxl8sP-023u2TuRZ1HvAXE0eOv0dQ0K757FntZdiiu6bDhiYEX2kBpgYW8uuPQ3oAwUm9abjSpLYDBzhRFWtaQpRWWEaA30YdAn1r-0vBPEAm5Ovxi9dlHlov6pGYrIDJTANR_pgJvcdgxcWHgkSlB1A4DUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBNu6-r1vNZT0xopJwSvuwU3GNhfoJslOgjozCwj-hMH06B3b0sAmdX4h4LRs4y0ppL0OXQ37cjN6FKea9Gv5lp-sBxr-qrCOYjsO8Mz80PeRoL4gRfSB1jMT2C3HmORTz0u0VlbYfkNPykIqqiUAQZPzCMHmSRrIXG5-pbj3lDViuSQsRWunoAe45_77GNwWxrBjsSqKuS32ZgvyPMbEz0B0TLJ1nty_4FmoDgS4h32DYM1irfAmdzwiAhFCUGJ-GKfFei4Axgbh7FkhT6F5ECOMgXJMz_evk2bsIxjMcwqHZlsj0r_MAaLfE1Mppc5BkL9crcizFLONKewo0XVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=UWcKrxjq0Fxa9ix5esJWejPd41HDDsXAM92TnJ36hyv_0F830ALPdOfRuw073KmzNPss8NoNkuwX71m3dDJbPZRCAEVA9FcX74kaSsOA0ZLLWSbt0vDGw934QTmVxWvUFdf2QqEEncPaGUQCoxAf72i0pxYY5A1JeURgpOAIRrXH8JtyHtstm6GclSB17lDtfv1kGGyet3lwojQtggFhlHxjSfD593BoQYyyeYyty2uKFGCXVTudbLnBmlMugsKKody4nulo14pjRKN3SBheEJzdfImJJLpKy5NS2mBdKXVC_MiFhF_oqRFF-QBY6HBEPL1X2yxF2dmi76Sk-PT1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=UWcKrxjq0Fxa9ix5esJWejPd41HDDsXAM92TnJ36hyv_0F830ALPdOfRuw073KmzNPss8NoNkuwX71m3dDJbPZRCAEVA9FcX74kaSsOA0ZLLWSbt0vDGw934QTmVxWvUFdf2QqEEncPaGUQCoxAf72i0pxYY5A1JeURgpOAIRrXH8JtyHtstm6GclSB17lDtfv1kGGyet3lwojQtggFhlHxjSfD593BoQYyyeYyty2uKFGCXVTudbLnBmlMugsKKody4nulo14pjRKN3SBheEJzdfImJJLpKy5NS2mBdKXVC_MiFhF_oqRFF-QBY6HBEPL1X2yxF2dmi76Sk-PT1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-HhNPEsLi2snIEG15-fsTWV9QnRPc1jmJcSOgLMbko-hAgZdcxdAtVyjVJvPz9UABvFyWx9kZPd8zVU__GYg1f0kTqg114EHr6U6uJTife9T5m7VLrLV3OdB1IVuImxrbtDnHePsotsLJv30pexnSp2wXDk6udNOkjRmiNSSDE0jAnksJ4GjxdLjRIY8MMK19HzpsFpqOrgEs5Q6FWIX9w51CGQuctrHohEGkDe1qkLVGH9Tz_dqVQf_gBw9FRfPyGAmWDIW0gxexiesJiFJOFuzXyq2Y7q5H0TUCHjHey_ZaeNUxxbkdiOHbXvgnYq8DES6PL7-hzq4ZdEwewzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYTlMFlEgL9Ie3lcl17RAvWPVX-EfepAljuvybhvIoAP1HFIaePKAbpWtexUMbiuespyKlJ3ME1a9vPAvueNhbCGoAx0kUzgfcllgGsO4KNHeRB3hsZQrGGWm5J-Cc8ZZ3T4YcsDx45Xo4zwQlMPsOmQOWlUhiGkNdHQz3rMB93H4qCoEVMLj2qZXWYjyyFqF7D-k_oU8nOUenbJi-eEk1rNZMbTroQnN5aliPf6RJFZlYB6jDFGaDcpoRTOklRwd1k_cizqZQ7fxJtfzeFS7wnR0x_9aujvuALwBo1xgduI2b4kWExvX6FG-Sl68HlxVNF-DE__M81kEIlMcpj15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=NvWC5YefSTi20EDfrIADZ7ZCl7Pa0EobV_kGwInNB7_8zG3rOYM2FBgGuMA1Wre7Zy6UtwmC6Uc1SHaXpvGY67jiSpqJxvY_8lzQE84LQn2-L2SZmg_ZCwDy5PE9UA4yhqeIZ5WZJ0A3R3O_K9YgE2sk0doNIZR376yS2oPO4M_tnYhhb6srQE_U5aCdl_NG_FrX3d8AdpEOi-9jLUDRddnFCLEthoAfguhBvnRnuxSclYIqyDK53eWhzU6renGYoOS3J2DrvPV_1FkPheH1t1JnEyH5igZSVod33aq0uCxco3ef89wbGg3TS1k_o5PmqAZPiTKwpm9GfYuQOmCdog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=NvWC5YefSTi20EDfrIADZ7ZCl7Pa0EobV_kGwInNB7_8zG3rOYM2FBgGuMA1Wre7Zy6UtwmC6Uc1SHaXpvGY67jiSpqJxvY_8lzQE84LQn2-L2SZmg_ZCwDy5PE9UA4yhqeIZ5WZJ0A3R3O_K9YgE2sk0doNIZR376yS2oPO4M_tnYhhb6srQE_U5aCdl_NG_FrX3d8AdpEOi-9jLUDRddnFCLEthoAfguhBvnRnuxSclYIqyDK53eWhzU6renGYoOS3J2DrvPV_1FkPheH1t1JnEyH5igZSVod33aq0uCxco3ef89wbGg3TS1k_o5PmqAZPiTKwpm9GfYuQOmCdog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jgn4McnGbfkKBqgKnfRKvH0aLELVdkQLtZ-FX3x0IWzLhlqwFq6v_ue7JEEgEvyLaN8Hs3SnUkUqhcd58I1U89XebJtKgEThqXHdY41QyXh7x7dV_OkPvDEosuqA4T7uyHRVBtdpllzWn975-bTZx7DR29-iw_MSbYA_kbIT3qvX1q5ytWNoqAeW-bMXIppm7u_vn4zi4WPGEs1_D51T1h-cZ1toaGDXalYBk9S7HHPl4KX7lNSNIhIg0iW6c-M-6lkh7K96zJIre0pWyDySHC5nvTPdjku0TAOlY3vFGACLe_h8yDYBV8dFJb9-6pqZ9pVSSO7TVHXZ51U01kRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=FBBFqHM4EYWWRoJFl8ixZVNFlLkNi-gNnPIzKsyYd7674fxSzOgq6wq4ZZOEXnuAPCDDO1k4Qwfr9TRH7J20R5zXVMDZKf4iBp0KgRxuVtbP3ON6RXBgSMDBEQWVmtro3zPWeEiOtGPg-F1CYFdAwYCmxiFyNoy9KplsTQqPiroaD8o5xhpZ7ak50MnGkmeN79f1IwjTIQZ_yqEnlcLjUG-m1u0U5SILfbhSbpWdfVFkgd7GJ1TRCdf9IaIbux9CF4herpOav_YT7HlqQHNcygiSCCZ60jMbD_ryTCyBscmnpzmfP4725H90OQe4b-6n2OBCa00DGfswQcdnjnIA2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=FBBFqHM4EYWWRoJFl8ixZVNFlLkNi-gNnPIzKsyYd7674fxSzOgq6wq4ZZOEXnuAPCDDO1k4Qwfr9TRH7J20R5zXVMDZKf4iBp0KgRxuVtbP3ON6RXBgSMDBEQWVmtro3zPWeEiOtGPg-F1CYFdAwYCmxiFyNoy9KplsTQqPiroaD8o5xhpZ7ak50MnGkmeN79f1IwjTIQZ_yqEnlcLjUG-m1u0U5SILfbhSbpWdfVFkgd7GJ1TRCdf9IaIbux9CF4herpOav_YT7HlqQHNcygiSCCZ60jMbD_ryTCyBscmnpzmfP4725H90OQe4b-6n2OBCa00DGfswQcdnjnIA2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jceSMrZXSQymF3acz0xm52LljPcbPrdZGKI2hUWsLZYHJ25hWei7l68SUh9EHd3FgHMBFhql_oULY3_sZkFezNOBHrqCI19zU89tHwXICLt9NXaGkdZ541FrcDdmuO7tqQv74DIj4DiCQN1jKAipuDVARdjyZJN3i4KoJi9e6q7qI-vQd2goyvN4DLS3-UsHYAibYMYBKZFdpegq5LY3Dgs1Bz983BHlW-8CVqAj8xB2OpG-ru1yRCwsjnpoeUh3k7V4WFqLR1O-RMLHJDxD6IDbTVGl3eiD8QTMJ-MGOgCha-hwWhEfJZeIdmvsIDOiS_ie6-znOXxMqIToEqB7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=iI3HJzJeZqc2AsXkeYQaDaKKQEnuBg7gCA_0itmRu9xtUPcxmnqAts3ZuciZEgUQ3eYoJ0PIQwIpTKllKEy-CXMdmZOPCc7uQ3LRBH-E8tMugpGLy9i0CK3Bycg6uJHgGtfMBFHLQxlzOxNCPTVRL2_J3KhErk49a1NlrdtFkG6YinLsCaMDjffMW5LsLQWnGW4uLFZaUiyemtdqon1hL0--Slg94VICz4MHaZ3TiD6ssEx5wsEMqMeltGOynczE2DdQKXHW3eCxxMlulG1iu4J0PdS0MXzhcs9mNSboI5jL2AYfEMO88YOfZUkD9m9kytfb6NEnEdVJzBqrBukMaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=iI3HJzJeZqc2AsXkeYQaDaKKQEnuBg7gCA_0itmRu9xtUPcxmnqAts3ZuciZEgUQ3eYoJ0PIQwIpTKllKEy-CXMdmZOPCc7uQ3LRBH-E8tMugpGLy9i0CK3Bycg6uJHgGtfMBFHLQxlzOxNCPTVRL2_J3KhErk49a1NlrdtFkG6YinLsCaMDjffMW5LsLQWnGW4uLFZaUiyemtdqon1hL0--Slg94VICz4MHaZ3TiD6ssEx5wsEMqMeltGOynczE2DdQKXHW3eCxxMlulG1iu4J0PdS0MXzhcs9mNSboI5jL2AYfEMO88YOfZUkD9m9kytfb6NEnEdVJzBqrBukMaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=rGW0lGUnrn_4EsPhbdpNBiK7ZgM4N5dE0T9NYX9t1EdAE54uLf8eH4YdAHjccxW5fkoy8KscIeDzvJq3PccK209KCqJAMOel2w332ssoBl2dhu9eZ8FRt8W05S3C-TSllcZXS0dt87DHyF6rg5KMCmxhOncP6VJR7CTFMjFZn4_HSbIlNfVcV5lnWazha_ji0GiwuhtYLEHtGQtix6jgcXX3KBoMz_oxVNgVwAYdJxnqb4jxC43ujUrG9SI_7RgkE2PCsk4t33_Z1lDkFJkBdgWALJRp1ndIrYo1_zNS0YFWqppgdKbhikiRbqvELmxcAA0_uu_XyWSeQyLYl4dLrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=rGW0lGUnrn_4EsPhbdpNBiK7ZgM4N5dE0T9NYX9t1EdAE54uLf8eH4YdAHjccxW5fkoy8KscIeDzvJq3PccK209KCqJAMOel2w332ssoBl2dhu9eZ8FRt8W05S3C-TSllcZXS0dt87DHyF6rg5KMCmxhOncP6VJR7CTFMjFZn4_HSbIlNfVcV5lnWazha_ji0GiwuhtYLEHtGQtix6jgcXX3KBoMz_oxVNgVwAYdJxnqb4jxC43ujUrG9SI_7RgkE2PCsk4t33_Z1lDkFJkBdgWALJRp1ndIrYo1_zNS0YFWqppgdKbhikiRbqvELmxcAA0_uu_XyWSeQyLYl4dLrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAJL4dgIzobO-x2dU676HlIxQwaLot2RpTr28icU-u8b1m-_zKk8WJVUh5UCZ3qWgq0UtAswSDzhNi1pRwyXW3-t3uYkm7xabIp0y4plIWqp68pU9WErfY12uQwtvmA9mJdTuih0zuuYlhcPfx9-5MgsGY0ofSwp-tuwGBgzRw5f13xrT9qlKpYHdJDiBl_-WFZ0UwtNes37BmH5hDjyaK5xi1spIkVvbnedwtTZ4LISxU6MTem-fTFc-s33FS1ccZf6ieZzBcYcfEnGQc0WoA1zxjxHAyF-ivMHfWFKEfhEhSy8GMpkSNSdi3V0w56hvTHuJGVNJPEKlMQPVWPMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhhSo9OaztbWCemto4blQ5msZPLq6m9TgrMLyQmpdGGbIuww-dtstfZcK2HJRcOCqjfP5LELMUwp9Ld7peQNwTWRRIwYCGr1hnOGka01yjyJJdlCZBVzRgeLxcKgPmm7bg2sMy2IRkXXz7ivQC3bLT46tBN4p_skJA08KeZnxrFgqmtipIssCjHtuM7NRBEmjN44L0gJt_Zi_UOn_Rpmrwdf07JzZYKYjUt1RmkMi7ftmhu9wRI9Rc67k_R6zAloIwNgRDIUwGDW6ztcNxX7mB3yv0CJRoI3wNlpfN0eBdwFnm8tUv-zmLbbuJoeC8LBztOL6kwLzrSDQ8e6Eao_2bRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhhSo9OaztbWCemto4blQ5msZPLq6m9TgrMLyQmpdGGbIuww-dtstfZcK2HJRcOCqjfP5LELMUwp9Ld7peQNwTWRRIwYCGr1hnOGka01yjyJJdlCZBVzRgeLxcKgPmm7bg2sMy2IRkXXz7ivQC3bLT46tBN4p_skJA08KeZnxrFgqmtipIssCjHtuM7NRBEmjN44L0gJt_Zi_UOn_Rpmrwdf07JzZYKYjUt1RmkMi7ftmhu9wRI9Rc67k_R6zAloIwNgRDIUwGDW6ztcNxX7mB3yv0CJRoI3wNlpfN0eBdwFnm8tUv-zmLbbuJoeC8LBztOL6kwLzrSDQ8e6Eao_2bRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZK8r6gvXoGTVV9Tl-1MTBN1QMdeujY2hWKX33ar_71COSAoGUC3MZyKw1FWEQUNldlgUv5tlTjhSeUwgOx27ZOhOxtFhnRiixQmn8e4pS3wWmm93hRXIllW_q9q6QumEWX1tWZTJEjFivRVKjInltodX4OuyJRVUl4hQDZBfd1cR7PO469j3ykfs8usDwcSEiHXERftEwzFL8pejODpRdVHx6reUiSweGVVgR95QlkWcld0zKJGRerJ1nZjdcC1q-w8OWoOMLbI1MDuy-BH3oYBgnpcHGfGVsMIH2IWHVGPVqNeVXTjH8OxwGzeFl0VSG3K7HLM8htq2x0TSVdb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfcIlgTiWh44TzRu2T_maZVMCXUtPi4NsfLuwQA5XHaab6cRplvEDeS3uevGunO-KFJ4y7ejJ1xbS9ZSEIfhfiwL1MUd4tb9IhI7c50Jy3zsPSycgEnOCCvQzjAw04XvNEQN7Hi2WWvKYxQgBXUfnOKY9hI2BofgqpBX6ZecjUVlq5tj-N1GjyCi8_1RZjsLZA_sg5lQfYijWV2L9QAr0h3tMP973vvyFdLaJ5xIS54vNS3qMgkIvZLyG8fWuLQTMCK8-gI4tZckDoiUEG6D3CiMgEicMbBG_8DwyWAXwOs-Vc2_vW8Q08U1PttizEZS6fOZjU7cIsUzyB2EDKDAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=usJFhOygxWBf7RyCsU6HNGG4r0v43i8vxWK4f9T60g2LHRfFeBQ0UMU_1ZJjqtNm-8IsusXCR9my8Yi-yR-ZcXSYCys8k8Wf1BcL25UftJl05HVhloVAW_AzZ-ZTqm68F2Lm4_lYGGTZnjBhsvIxvX6ljFrxeFbM6rxuXhh44gxRNFcBjN6Oyh2oFDUGfkZvCMDQQ9ZYiWBFiD9orHWiAgVdocevv3bzMTAHp5AyjUjL2gDYqFIDBM1K-0KCJPEAHWyfIaDHCdAj_oiGxioDMeV7PpQCx_GYHsz6Wrm07WSeNpEE4qlQitibceC6bo0D5bHk9xG1bZKRWMRa-BYBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=usJFhOygxWBf7RyCsU6HNGG4r0v43i8vxWK4f9T60g2LHRfFeBQ0UMU_1ZJjqtNm-8IsusXCR9my8Yi-yR-ZcXSYCys8k8Wf1BcL25UftJl05HVhloVAW_AzZ-ZTqm68F2Lm4_lYGGTZnjBhsvIxvX6ljFrxeFbM6rxuXhh44gxRNFcBjN6Oyh2oFDUGfkZvCMDQQ9ZYiWBFiD9orHWiAgVdocevv3bzMTAHp5AyjUjL2gDYqFIDBM1K-0KCJPEAHWyfIaDHCdAj_oiGxioDMeV7PpQCx_GYHsz6Wrm07WSeNpEE4qlQitibceC6bo0D5bHk9xG1bZKRWMRa-BYBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=BffC9FSsMc_R1mzfjL4_59dwACo2pVr5_SkOCT-6hFKjZW9z616bNxLJQy_ZHRzMWghpSSTKHI4sbcHY-4KAkojlh7vTiEvpfQBoEn4qGI5iB6pk4l7LpyBD3bvqHyeMJu0MVdT0NWdMDevMBZuf48BCASdGkyhELhyhVkaUlzJPHiR9CAEkIVGMhplG8U0HxYGm9ITOddNYN_Mvj3d55wmqkKvHllkRGM-e6owCk3Mwz35dITuQtrr4ym4sd3bh1lEim5RG1vA94fD5NfwimeimVnv3zV01iDzHLyc4VvApHzcm7ZhZG2SfelvMbE3ZTNoxzEHCaLtrg5dnaSbxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=BffC9FSsMc_R1mzfjL4_59dwACo2pVr5_SkOCT-6hFKjZW9z616bNxLJQy_ZHRzMWghpSSTKHI4sbcHY-4KAkojlh7vTiEvpfQBoEn4qGI5iB6pk4l7LpyBD3bvqHyeMJu0MVdT0NWdMDevMBZuf48BCASdGkyhELhyhVkaUlzJPHiR9CAEkIVGMhplG8U0HxYGm9ITOddNYN_Mvj3d55wmqkKvHllkRGM-e6owCk3Mwz35dITuQtrr4ym4sd3bh1lEim5RG1vA94fD5NfwimeimVnv3zV01iDzHLyc4VvApHzcm7ZhZG2SfelvMbE3ZTNoxzEHCaLtrg5dnaSbxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=bDt4PUn_eR-PdfvWwMzrKXKETHBLHI_0HC1C_3p3etuedoK0gGbIbr0N9pMUrVjs8P2pROvZeADzLI15j-Q2iKdnrna0Ew6nUAzsclK436ivsMXeXe09VvzhFPurZ9DWxXxlyLWPu_tpShxeESxIusoIRgqay5mT0-_h4VYh7t5qo8Q0nqIKF5Djrt4ZaRoZdhkbvVdpLc3n_r_Iu_TwHXlER7mm6jAvtp2bCPYgz1VWmenvzLVhe6QiSxZdKqgD3BiAP2wVZfqehTbo2WsgR4m15pJNQtwEF9EntYD245hjN6pchEcb8MVkVEkksjCpqOHmHoKoo_2xMAFLVYhJ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=bDt4PUn_eR-PdfvWwMzrKXKETHBLHI_0HC1C_3p3etuedoK0gGbIbr0N9pMUrVjs8P2pROvZeADzLI15j-Q2iKdnrna0Ew6nUAzsclK436ivsMXeXe09VvzhFPurZ9DWxXxlyLWPu_tpShxeESxIusoIRgqay5mT0-_h4VYh7t5qo8Q0nqIKF5Djrt4ZaRoZdhkbvVdpLc3n_r_Iu_TwHXlER7mm6jAvtp2bCPYgz1VWmenvzLVhe6QiSxZdKqgD3BiAP2wVZfqehTbo2WsgR4m15pJNQtwEF9EntYD245hjN6pchEcb8MVkVEkksjCpqOHmHoKoo_2xMAFLVYhJ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8E1mq9wIrn-vNZ590K2Tv6haGtrOZv5RqNfedtuBD3S8IPfZkkxKsx-w1F7V085AN4ThLBMF-CUhV1rvcL5LieOUsrn2aswO0GjRQVTbUD_r0w-Z2gMQNs_eG7oz0jJ5pqVT4s0tVmwG5iBqkat6MKrcrRmjNOh5u5Yhjwo99tUMxBk-EHewb5388HGy16El5G7gn_lOvb4LbL91BB9yD_ZihXYC2G12G8B_d5o08UoZJaNc5Sp4D4KfuNl0LeWYtNEOkv13JcOBih3yZYcF_Fd4HYqzc3Bdm_6gFwpwnRzqseU9Xq00bfHCfE5yz99-weeQmlSGplcfeu9r8TXc2fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8E1mq9wIrn-vNZ590K2Tv6haGtrOZv5RqNfedtuBD3S8IPfZkkxKsx-w1F7V085AN4ThLBMF-CUhV1rvcL5LieOUsrn2aswO0GjRQVTbUD_r0w-Z2gMQNs_eG7oz0jJ5pqVT4s0tVmwG5iBqkat6MKrcrRmjNOh5u5Yhjwo99tUMxBk-EHewb5388HGy16El5G7gn_lOvb4LbL91BB9yD_ZihXYC2G12G8B_d5o08UoZJaNc5Sp4D4KfuNl0LeWYtNEOkv13JcOBih3yZYcF_Fd4HYqzc3Bdm_6gFwpwnRzqseU9Xq00bfHCfE5yz99-weeQmlSGplcfeu9r8TXc2fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=bq_EjvXAXXRi1W38zle15AEVqsUmSD5kSefYb8d9bwgTylmRtxma5scbKO0Ce4aI5QWxmk_GDiIuS3DKmG-VbR7VHlq-osIzK2DFg3p_GdK3M0l4gP9mJpjnE2drqb1XY8Si0Rcoi_tBnL5dYrXDirV3jrRwhpc1X1psavExxEWKRvHXWIaQAsIel5QdN9fu807QtrxQEho6hH2r97VfRUyOKhrm3owyuopjdBRSF-NyvTe-AM56UR-gWr304TQPj96SmjgYrC_eWp7brFIUSaj1ZTXICUN5MLx7ex-IJI_WQkC8tIAKIKXE-Sbdoa-ESpc7E3Q-fFWh0iDCXDWuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=bq_EjvXAXXRi1W38zle15AEVqsUmSD5kSefYb8d9bwgTylmRtxma5scbKO0Ce4aI5QWxmk_GDiIuS3DKmG-VbR7VHlq-osIzK2DFg3p_GdK3M0l4gP9mJpjnE2drqb1XY8Si0Rcoi_tBnL5dYrXDirV3jrRwhpc1X1psavExxEWKRvHXWIaQAsIel5QdN9fu807QtrxQEho6hH2r97VfRUyOKhrm3owyuopjdBRSF-NyvTe-AM56UR-gWr304TQPj96SmjgYrC_eWp7brFIUSaj1ZTXICUN5MLx7ex-IJI_WQkC8tIAKIKXE-Sbdoa-ESpc7E3Q-fFWh0iDCXDWuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=A7lj3vbfToY2OQS5SbIjMDcGZbYVHpil-v4DW2LZcSMVnh8OuF4WvXLtl9kwLqXplaQ2e_SW25iatsMDvF4k9qfKV8N3_Sy1rBcKKDz-UbU9fVqVb-WnFfrzOWXx4DKz40nLakPjCN4y5BdAUXS5loDNDUVu0DDFTXl84t0OsHf-D40jMBOhtDv_nMZ-hPNiNzoa4Qh3fAz4ZGh2enXJsuSbdK_mut-1BPJjE0Y_y-9ZIzyFzn-C2n1wIaJgTMeoCyk35xTsD2x3qdep6SXXxVJ5z7UJuECuQ7ObK2UE0mz4tHaZsT7EJooV_AEx7wTUMVAT83XYD7ijKy3v_1tvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=A7lj3vbfToY2OQS5SbIjMDcGZbYVHpil-v4DW2LZcSMVnh8OuF4WvXLtl9kwLqXplaQ2e_SW25iatsMDvF4k9qfKV8N3_Sy1rBcKKDz-UbU9fVqVb-WnFfrzOWXx4DKz40nLakPjCN4y5BdAUXS5loDNDUVu0DDFTXl84t0OsHf-D40jMBOhtDv_nMZ-hPNiNzoa4Qh3fAz4ZGh2enXJsuSbdK_mut-1BPJjE0Y_y-9ZIzyFzn-C2n1wIaJgTMeoCyk35xTsD2x3qdep6SXXxVJ5z7UJuECuQ7ObK2UE0mz4tHaZsT7EJooV_AEx7wTUMVAT83XYD7ijKy3v_1tvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNS1CCWmnjeCnEJLF4ZvSbjWM3E1bAr67IDyBjctFgSMH6JPHdLs5awqNka7t0VrH2QORPin3U0wPa7F2KSy54iCwlsgGmS7SJNOAjD-A3rjdYAD013RxfqydZy-QfLF9dZU9YmmwOMykQ5bL-gmFNsDXmQKFGaNl2R_1wttNDkoaA0kxcDVVN9RqvrtjpKX0LlZKWsKqT6oLMNffkkK3YlOHlnXS_aDBM7TtjDfDrs8FA_f0tJxsb6D1IyKcladFM2AjG7JDDbnUoy4exq8O1TWP1TPTMSwevNEc3--1Z7sIDTB9OGnoobDWhlO1dGQIaxYcfKHCpP8CQwLCD2oBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCLGsKpYku1dwDRcWkYEZqQ53QtGX9lDkiXs8GBcpXqJyYaFj1_hdYverw7xX65VIN_bfgdCRQsq16v8dWfgcW3OwMLAYe-g_NnrhLRBXwlvKnma4imhnS2rUMekqrqaq2xiX4O54Elj4C0Swby_r8JTRkRfwdX6b7-RbG3VuKCdJNSvjyMQ0kmUQTzjCya3lori-v_0iOCKlQk7kasP6_3chP_HFqMfux-B6yGLySTMWer3IpMF8r5Y8nkenTy1x0rp_0eC04fFpR9Xq__0wkeJ_Lu5eMhyH4knSgKz5oItSAE1XtJnmG50dBMdAyuRl2aRe5VSN2PCjLKwwC4Cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=NvO8mAyLMG-eYvBLGpQeYUOZRVX0U4jIUW0IWo0elN-q8gWWzMOEIXJWCySMLxbHNGHrj0WRNbIf7xKe4BZ0Gd9sVNvfSlQzO8p8jo8vPq8RLXXmcNjfNL6bc_4uihCjZToElfuGi7LnzlwPK5T88nWrJ6j7Pl9Sd99E6v0s3jiYzW9VlXyAlXslTXVp5VsrkbWRiSZ8IF1wWePkOooIsG26i7tPdXxE5po_UZ1xlXnk2QlK-hIHbpED2KBED5DqpMAeLCTTCq2_34dr8Tj9iJL-cVFKCTq9o5IVDZBhcPsvkwFWuafkDe-9jvQT7i3PY0zbkZdJYnVmwVA4wNMAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=NvO8mAyLMG-eYvBLGpQeYUOZRVX0U4jIUW0IWo0elN-q8gWWzMOEIXJWCySMLxbHNGHrj0WRNbIf7xKe4BZ0Gd9sVNvfSlQzO8p8jo8vPq8RLXXmcNjfNL6bc_4uihCjZToElfuGi7LnzlwPK5T88nWrJ6j7Pl9Sd99E6v0s3jiYzW9VlXyAlXslTXVp5VsrkbWRiSZ8IF1wWePkOooIsG26i7tPdXxE5po_UZ1xlXnk2QlK-hIHbpED2KBED5DqpMAeLCTTCq2_34dr8Tj9iJL-cVFKCTq9o5IVDZBhcPsvkwFWuafkDe-9jvQT7i3PY0zbkZdJYnVmwVA4wNMAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=CK_-65FEFhs_xQGIxuNFXAzQQj5dYE3A6Mn9zl58DaN4N16toi_yoHHddaEy1OSbsWF66rNwa19Ry9A7GvgVW1VHNCANNMFhJKUFScY10RHjgQVUNdacRzAOX_ig4a62BTgIcJq-oJv01odNxj9VjavRirZjeKhulOfXSeiADLH6p_OjQS0b-T97Jkkqmhpp0qIQZ9OS_Dt1z8v9ujTJyRzTScsfFyvvs8qZFfqaiDgU91vXuiDBjZ8v9ajP1PL9HYQbEg3nLRZrMJMhmb9h-hYi7jKR14Tj3KW_cPTmhj3t9cPJNO8aPLETN8pM2ED1ZgS7hw1Im9N5DEPz2F7moA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=CK_-65FEFhs_xQGIxuNFXAzQQj5dYE3A6Mn9zl58DaN4N16toi_yoHHddaEy1OSbsWF66rNwa19Ry9A7GvgVW1VHNCANNMFhJKUFScY10RHjgQVUNdacRzAOX_ig4a62BTgIcJq-oJv01odNxj9VjavRirZjeKhulOfXSeiADLH6p_OjQS0b-T97Jkkqmhpp0qIQZ9OS_Dt1z8v9ujTJyRzTScsfFyvvs8qZFfqaiDgU91vXuiDBjZ8v9ajP1PL9HYQbEg3nLRZrMJMhmb9h-hYi7jKR14Tj3KW_cPTmhj3t9cPJNO8aPLETN8pM2ED1ZgS7hw1Im9N5DEPz2F7moA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=HQn_IKqyakNw6n-9s3p54ToCR7k74wK_F8TKSqD2yogzM3zfMbxQem4cTIkYdU81J6--xOrauv72bzmKaJ5qAvNNbutlXDrDaIM_tT_WOmMy6b7XRAjZvqJkbervykd0J3vZv5ZJw_7Lw-o_CeJ73E8zhWijWyF7L-zO3XdFpmtMWr4mqySZWcVvUvcUZAIq1pTstxRvkvNQyRJ7XyR7IyahMruqrakp-B6P7sdRnKlXPyv4Ln4si7tdmmb7YOqVlLDPxNAggoPYP9qkybfVjkzfY3lHh0FW5Mzr05YegTc6zbHrG6X7Ji5kLbHO4cGzegEFIcyHdkYc1iDTUILL2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=HQn_IKqyakNw6n-9s3p54ToCR7k74wK_F8TKSqD2yogzM3zfMbxQem4cTIkYdU81J6--xOrauv72bzmKaJ5qAvNNbutlXDrDaIM_tT_WOmMy6b7XRAjZvqJkbervykd0J3vZv5ZJw_7Lw-o_CeJ73E8zhWijWyF7L-zO3XdFpmtMWr4mqySZWcVvUvcUZAIq1pTstxRvkvNQyRJ7XyR7IyahMruqrakp-B6P7sdRnKlXPyv4Ln4si7tdmmb7YOqVlLDPxNAggoPYP9qkybfVjkzfY3lHh0FW5Mzr05YegTc6zbHrG6X7Ji5kLbHO4cGzegEFIcyHdkYc1iDTUILL2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=ptEgPq0o6JYWZWcDXgtaG1hofpqeLCsSS5D6u9Ku3JoTd5SA5Gd7qoneyzfg37UrzIHhbOul0HBf-sUvGIdTPSysTbC_gKUhx6S_yvxJZgGbyQ3dOrS0GuQysaBw0UtbRHfxxtZaH5hXBWssyauEG2fvnj4lReQB_c2LWaxQrJHyCDkz-r_68m2kau8M9ImoAgp86zWJw9idP9oLir4t7HYWZMuFa2EhZf_durCMrkydEk3WF25MFXC2KygkSBfIGT_U7TaELBWom6uRMKCYIa-lpRiJ2pgQs_WBxhIVF00zOFI9s_ppDmBplps3tiyHzD5lRUYq63BJNf746Tzlxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=ptEgPq0o6JYWZWcDXgtaG1hofpqeLCsSS5D6u9Ku3JoTd5SA5Gd7qoneyzfg37UrzIHhbOul0HBf-sUvGIdTPSysTbC_gKUhx6S_yvxJZgGbyQ3dOrS0GuQysaBw0UtbRHfxxtZaH5hXBWssyauEG2fvnj4lReQB_c2LWaxQrJHyCDkz-r_68m2kau8M9ImoAgp86zWJw9idP9oLir4t7HYWZMuFa2EhZf_durCMrkydEk3WF25MFXC2KygkSBfIGT_U7TaELBWom6uRMKCYIa-lpRiJ2pgQs_WBxhIVF00zOFI9s_ppDmBplps3tiyHzD5lRUYq63BJNf746Tzlxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=tXcOevoi732vPm665KlO6FZ1kWgNcKG4FrmHJmF61UBFe3p4T6VeZyzDQxAHLXkHeNz05Tunz4zlpo_3WNBxQq75-j-IhohklV2yggaCsyo-lXDJHfQuzDblSyGJ_EdScoQbMAPqmiY9m2ucwAYZ1JGnipTjzo2mpJ1KUIhZE2hc7htkFzi_MEQ1j_kCfYgSuBfXwA91dRi5MNWfrXrqBTxM1wT0IDiw9eR0JKS9_cuUR4sW4GOdQUwkP6ea5IakAzYJ4mFBWVxIcUI_aIzQGrOVKWsKQfAf52ZqJJ-N76rsCZYOPX_G9hV3q3pcOVwRlariubqtquphqHAYkazrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=tXcOevoi732vPm665KlO6FZ1kWgNcKG4FrmHJmF61UBFe3p4T6VeZyzDQxAHLXkHeNz05Tunz4zlpo_3WNBxQq75-j-IhohklV2yggaCsyo-lXDJHfQuzDblSyGJ_EdScoQbMAPqmiY9m2ucwAYZ1JGnipTjzo2mpJ1KUIhZE2hc7htkFzi_MEQ1j_kCfYgSuBfXwA91dRi5MNWfrXrqBTxM1wT0IDiw9eR0JKS9_cuUR4sW4GOdQUwkP6ea5IakAzYJ4mFBWVxIcUI_aIzQGrOVKWsKQfAf52ZqJJ-N76rsCZYOPX_G9hV3q3pcOVwRlariubqtquphqHAYkazrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TwfSNUvHcZY6ZI5gCnt3hoCuYDQ23JkKAygYcGThBp3hha2DMerO6oqv--GoJK_avsokUIlEim_Ij6lYXj2Fk663mN3OMRkCWjMFFnxcK5NDPeWRMNGTYw8luAh5GHk1fLxWS7AvGIxmbQ8-eZyyQqojvdIMjuzY7AqHacajjbcTWM2c4oTlkSfV94_Vvowdi1HC9Yl_7g85T9GvPS8telsBE6wF3-esaxqFKOxebrV-tixI-lRZMCd_HcKuDKNmr-r50P2Uyh_s28EmZEzZoGui1o3Sa1Z2EiqJpKUze0-0gyQ5dOIEE6wR7JTexxFiE_J1V8zmhoDUN_YZzLT0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=XfwRUlFJV9gn1Iituy8g36e6ffsm3ZsaggMOadpaTWUPpedtylqBK4LxUR6_gfj4ZRurdVe2_Fo6sYbF9SBx6o16sZNNgcVtkPnBOtU0hRbF87YIce_whx5_1HiUSRttl2FVEHCRMmjQvTFC9HyLkaxA-BaY-5wf3rxMvidgeqXNMxUzXs30tAtupiZ8X1Z68yHo2w-4DLpHUSVqtG4RkZfRvbzNgIJoT_hMtwomh-PE0w3gYuEUazMqN8UDtnEJA9vqI_vQpKTA1R8V4PWbkIbIvNRUsD2lq43AP319pTIBcTq_tHcHAPjdKrYXngLPi8O9M1S0psz8bn5Cxbck-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=XfwRUlFJV9gn1Iituy8g36e6ffsm3ZsaggMOadpaTWUPpedtylqBK4LxUR6_gfj4ZRurdVe2_Fo6sYbF9SBx6o16sZNNgcVtkPnBOtU0hRbF87YIce_whx5_1HiUSRttl2FVEHCRMmjQvTFC9HyLkaxA-BaY-5wf3rxMvidgeqXNMxUzXs30tAtupiZ8X1Z68yHo2w-4DLpHUSVqtG4RkZfRvbzNgIJoT_hMtwomh-PE0w3gYuEUazMqN8UDtnEJA9vqI_vQpKTA1R8V4PWbkIbIvNRUsD2lq43AP319pTIBcTq_tHcHAPjdKrYXngLPi8O9M1S0psz8bn5Cxbck-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=c9D3HqQo8ahuebzSFZf4rg2QvlAkQK8nhdBY60OkGlzBf51FuLwE14npn5qrqsVSouO8bH7-nllKzijzj1peSejD0kD90EdY1JeaObesX573XP22FgVEPhW-Ihwh_UbwHr6LJqDfcfOO8NGRuQTxOiU6jjBEDIEUh9SrHQUqTAeREhedCx_yQo6aJLNqwsnsmFpY_klrconos95xr325kc8HNL9e9UXXXfJr967S1SjvgtZUNvT0RnZ4PaI-2SHF3vyXJtn8stml0iPh9cUY6tL-T_K3sgEpYK5ZpLvy43JSPZ_m5MuUUUZSVFADVsWo_iKxEWJUOS9uNllS1rhsiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=c9D3HqQo8ahuebzSFZf4rg2QvlAkQK8nhdBY60OkGlzBf51FuLwE14npn5qrqsVSouO8bH7-nllKzijzj1peSejD0kD90EdY1JeaObesX573XP22FgVEPhW-Ihwh_UbwHr6LJqDfcfOO8NGRuQTxOiU6jjBEDIEUh9SrHQUqTAeREhedCx_yQo6aJLNqwsnsmFpY_klrconos95xr325kc8HNL9e9UXXXfJr967S1SjvgtZUNvT0RnZ4PaI-2SHF3vyXJtn8stml0iPh9cUY6tL-T_K3sgEpYK5ZpLvy43JSPZ_m5MuUUUZSVFADVsWo_iKxEWJUOS9uNllS1rhsiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgEWPNEUGV8GaiduRSLxETAsBdU5YAJJxNHjwu7V1ChS6KsotiALiOXf__h346qQD1S2Ob1iBRx8UuCa0Nvl04DnwlPSmPqN3YRCDzV-ryGhxzI3HHkdSZM7rSJ1DOq8jKVMR6xC_CKtgZvFSGrxOxit8iIrtPQJvtGTsJjLFnCvmKU4Zdwzd9MtaJAVelCoAMcLvjSRGzH2g1b-Sbq_9OBKtSZN7n_ba8mP5ZumZsKykTyuEt1CkMKayE7N7LpG0lx6sFhkUICA0ZlJLz4LmfZTxxK0fGG3RoZ9vxtpvQZ1Hwwa9JH1HygzalAs5siqDcu3GcPLhZhu9FXVkXtEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=ulua4qDZhqwSiLhF_N0FXyiWydDR5ElZDOnQeoCjfOv8SWdfCeDeENlBSlbr_CsJmY55ann5e3TMSfQLhmmBX6du1wQSxJWCGmU8ZCvk4KmuBwT3F0d0B1Guc0QJJGESRtJbMCW9ppEyPkRZyLQ0qnFb_ED3MWd4PdicMku_W07E2wAiQF6JekNcbnzEW1Oqt3yOB76CqkARkn0DhLD0Oz0MZVPczM3HxsprljnHGemqDZzMW0H1Kyz-jSQ_sV4wjBgQWqIwMi1RzMuqF7NwtKYgoMhDI4yfvy_vduLwLXrI7CPbNInwHK22n4N7KeGTxKvjIpyOEsFQLWZGChdTEV6GO2bF8MWz5a_nMDSnxRBGOac4cN0r9SZbpMBIyGcyv5eCvLoHCKR7wDkoFsiVZuayjYOv-9HzwvyM-OtiW0ctQFhkIYZeiPWjLtCKH1F8N8dkmiL8ND5atYoRDu1-MWvESM8PsgYHFUgzzZ6eWp6yF3jIwFs7q6k9dvSermJOfH8abKzm2zIbgcUJvEnSuuojsjgI_sqjFKeG5wSLBGVfgNeFNZyEusJgrsh6Q7H0ukMqMJzoeOh8l_qb6jyaGnHfS3SmuO-tWo2ere-vg-i1ri2sWmrC-XxkTxO2J44-U1uyhT8etl-5OPrCZzP4g_YhbFDXc8Binym6iDAtGp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=ulua4qDZhqwSiLhF_N0FXyiWydDR5ElZDOnQeoCjfOv8SWdfCeDeENlBSlbr_CsJmY55ann5e3TMSfQLhmmBX6du1wQSxJWCGmU8ZCvk4KmuBwT3F0d0B1Guc0QJJGESRtJbMCW9ppEyPkRZyLQ0qnFb_ED3MWd4PdicMku_W07E2wAiQF6JekNcbnzEW1Oqt3yOB76CqkARkn0DhLD0Oz0MZVPczM3HxsprljnHGemqDZzMW0H1Kyz-jSQ_sV4wjBgQWqIwMi1RzMuqF7NwtKYgoMhDI4yfvy_vduLwLXrI7CPbNInwHK22n4N7KeGTxKvjIpyOEsFQLWZGChdTEV6GO2bF8MWz5a_nMDSnxRBGOac4cN0r9SZbpMBIyGcyv5eCvLoHCKR7wDkoFsiVZuayjYOv-9HzwvyM-OtiW0ctQFhkIYZeiPWjLtCKH1F8N8dkmiL8ND5atYoRDu1-MWvESM8PsgYHFUgzzZ6eWp6yF3jIwFs7q6k9dvSermJOfH8abKzm2zIbgcUJvEnSuuojsjgI_sqjFKeG5wSLBGVfgNeFNZyEusJgrsh6Q7H0ukMqMJzoeOh8l_qb6jyaGnHfS3SmuO-tWo2ere-vg-i1ri2sWmrC-XxkTxO2J44-U1uyhT8etl-5OPrCZzP4g_YhbFDXc8Binym6iDAtGp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=BDpA-AqGGAEq6UYXDxgmx0oF7EHEJAXcESB6zkN4bApe9HltyS1ZM6QoWKazfKa3-UROeQi2Rva6q14ujC9GTT2We5SKsE2lhHDQIwe1ZnrtqVqUnNvol7dK2zn97lbJXw7czMY2HDVfa6XGlOcv7w2boHhH67Pl6Uibr4-JVnTdvcyA_uoYFC08wQSyErLDAbZK2TVc4LN3aQRTaQ-lxRkqvIzkwvrBQkIR0r01PDE1FPjMhlutWfOxqblAcWiO4_8oLMqDjQcNT5l52R7rGm_4fLrXDORYe_9tPVfj0alj1UvRJ0wuCT4ppDCjBiF4E9iR0yBqISqFP2mP-6afAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=BDpA-AqGGAEq6UYXDxgmx0oF7EHEJAXcESB6zkN4bApe9HltyS1ZM6QoWKazfKa3-UROeQi2Rva6q14ujC9GTT2We5SKsE2lhHDQIwe1ZnrtqVqUnNvol7dK2zn97lbJXw7czMY2HDVfa6XGlOcv7w2boHhH67Pl6Uibr4-JVnTdvcyA_uoYFC08wQSyErLDAbZK2TVc4LN3aQRTaQ-lxRkqvIzkwvrBQkIR0r01PDE1FPjMhlutWfOxqblAcWiO4_8oLMqDjQcNT5l52R7rGm_4fLrXDORYe_9tPVfj0alj1UvRJ0wuCT4ppDCjBiF4E9iR0yBqISqFP2mP-6afAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK1biUjfnD_XVjXLfA1OOsylSv1LASKQJiGIYUHqhY-KYlB12gw1DLE1gcjHj-9CG6z9RCsTFwtTil0NlSzAatrGZAJLadcIn0dkS3cf1WisNm3xFLH2epf7LyY_axSTDJbJkh9QAxYxAZsrDkcmTf874dZPRkcc2lDXVp6ggwj6DFyI_pOwZtuBfRvWtt6dZLaeMvLqdSfravoe22x_3qnpSl4KxfzaZu-yNiCWp49U3lagnWugCxCtQ2dn9Zu3KXXQg8ycz820SCK2ielfIPoByUWpzu9P1dv5Hss-Eq-TLDPvQldDZFJzs6zRQPhwEvqND-SHzhyxOeoakvZ-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpRZ1hEOU7-dEmBpSa66heG_L-fLEeRZyb2eGDSdjItaWGvMNRnQhTXJSpbkNOi_eFn7IibMGiT80N79MxbUsMkEoNH_T1CqWfxqfsb9qDRKwUC8BaTVHGFsVdSRkVTiuQkgxiCfBvuWro2Rgqij5l31-ZYDTgvTz6rl0sIVpxE9M1MkJtRNwruxOxug31YAc3i163ASaBa-plex4Qnkh3nM6CySrcjv30XuEkP1eHASgLq-Xg1-TQvvnfaCuqFlk7oom1kq-vv9hl3F-TtBlum526kwYs4J4k1UZ6x3ckxU143Ly-TSpl25GyBnEgBTbiC9MGlcp_aNo0mMH6eLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=Z1v-4XVLc_gjMIPSgXHL1Sr2J2g4RVtd7ejSdNcQGoG-QtA4maqVuav7e_yEaKPl_eJ3gmEmi52gVkLLgAZ43NsKtpViih33cYzbOpAXACxNPGlyZjhDcKYjpn6iBOzVF_bctTqiTQx1-pWT8FpUfs3Br3VtIdmWeDzmuHqjOVlFSO0KrlculdNA7dU4Gn5zrvSyZx_aN2oBrboQ9axhAjtJHKxiFBeW22pdkqhMkVqTfcmDpuhMXMnybiN5iRvke80CVypIJa79pzddT_QgFsgEMKksp7-6fEgUhtH-uoUEuVyNXFKonfbb-gxS6g8u6I2a9M4XaQlXgVP0tPHdEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=Z1v-4XVLc_gjMIPSgXHL1Sr2J2g4RVtd7ejSdNcQGoG-QtA4maqVuav7e_yEaKPl_eJ3gmEmi52gVkLLgAZ43NsKtpViih33cYzbOpAXACxNPGlyZjhDcKYjpn6iBOzVF_bctTqiTQx1-pWT8FpUfs3Br3VtIdmWeDzmuHqjOVlFSO0KrlculdNA7dU4Gn5zrvSyZx_aN2oBrboQ9axhAjtJHKxiFBeW22pdkqhMkVqTfcmDpuhMXMnybiN5iRvke80CVypIJa79pzddT_QgFsgEMKksp7-6fEgUhtH-uoUEuVyNXFKonfbb-gxS6g8u6I2a9M4XaQlXgVP0tPHdEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=IVWjBDylFvPH1Z70saB3MbFB7h4oyVtiPNshfbNnMQQm7yetnpzR0BIyOYgL9unvsxHXC1IUIh8QVbjeYEAatgiCsAseEskZAR2S5cN6_kVZdKz84b0wNq4lD001ndWSuts7XvoNRK-TJDguJ2X4RCf88LECpGoaTz8ljN1eGRk6zk8EE0qNQgKKTw2XntwDR0WxIKs6VrXa256cdmnIpPFHT_4y3IEMRPFpMFnPLEYFKe3__PHZ4n8iS8zdeogAt9ZCVJEmJmEJMRevoit7ekUOd9XQEVVYqfoblZ4cZqPegNP_ORbube73LEiQt5iww5A30xws9glx4QcuZ8sAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=IVWjBDylFvPH1Z70saB3MbFB7h4oyVtiPNshfbNnMQQm7yetnpzR0BIyOYgL9unvsxHXC1IUIh8QVbjeYEAatgiCsAseEskZAR2S5cN6_kVZdKz84b0wNq4lD001ndWSuts7XvoNRK-TJDguJ2X4RCf88LECpGoaTz8ljN1eGRk6zk8EE0qNQgKKTw2XntwDR0WxIKs6VrXa256cdmnIpPFHT_4y3IEMRPFpMFnPLEYFKe3__PHZ4n8iS8zdeogAt9ZCVJEmJmEJMRevoit7ekUOd9XQEVVYqfoblZ4cZqPegNP_ORbube73LEiQt5iww5A30xws9glx4QcuZ8sAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=RBTsNGlQm4OP4d1L7kBFCNyzD20j5_34-FWbby2RxJaslnt4b0OtLSOq5l6ZD0A_-kc1NeOyr49tMHKYWkTMrk6jxX19Th_eMz35bwI3BeVw--1Od7am5sn6gOXAJCgWRnuu146mm8CK0wYodx_5nouKnjTPEk22IyENBePpYwydaqiTvWRvYuYi9pIb-wPEoSNVN81VSJ4XLZLoReHyLQs5goNwj-sQe9Sby0UwJn6eqAvyi9WcpUwVPuambc-TSne2Pyjot7ewUcxVef7iUekVojuw_jmmE0c1bp5Gfvg0s4AaR3_YzDm4nbahXv3Y9YJsrawC8En8kxni2iNDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=RBTsNGlQm4OP4d1L7kBFCNyzD20j5_34-FWbby2RxJaslnt4b0OtLSOq5l6ZD0A_-kc1NeOyr49tMHKYWkTMrk6jxX19Th_eMz35bwI3BeVw--1Od7am5sn6gOXAJCgWRnuu146mm8CK0wYodx_5nouKnjTPEk22IyENBePpYwydaqiTvWRvYuYi9pIb-wPEoSNVN81VSJ4XLZLoReHyLQs5goNwj-sQe9Sby0UwJn6eqAvyi9WcpUwVPuambc-TSne2Pyjot7ewUcxVef7iUekVojuw_jmmE0c1bp5Gfvg0s4AaR3_YzDm4nbahXv3Y9YJsrawC8En8kxni2iNDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQtEHcBE0PI_zVGoIpKeXnQI1gNQ-xT0Q-8l3a3i14cgAxK4AGik-TuFjdZrgOtqEqFGP_ZhDYfAHs8hDkj5pozfiB7YI1yza51gPFMfA2MhNOYdlGTzS2-FCoQ_G4Ga--JwpO37skqSeBZGkcTs1-UZGjkGnLB9mi_1rZZmKHH0yzKH6PjoqBKl100tegoIpA5jlmQo1-Yl-YwnOQxTKoRk2rPjQOj9kZlfwH7aFFeXi_qNrqWHOc0ZhQQ7kxe9bE-gXWCBOcDj-gJn71GtX3rIfkUr0-BwZSx1FpeH7qSCNDRX3wrkc32ek2RLs9RAUUhAj1H-UAkVQVX8D63SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=el4bTycDzBoLxSyW4Q03eCpTVkUQIV4wz5AuBd-CjB0tAIRkAkNr7ntLX_GPP-zXiI3Pj5xZy-7U2N_uBvPjOgck_yIAbPjSj6DgXUI2Dw5hUI-65j8wrdUNLpxADBPXtWjaQnx7yc7QKwCsp1OkPkRxRgg1hXuPzA5OVoS3120gheXriYLRM2v-zNks1uEX_DTUdeZS-2RNroTCRzUAvMD1nUwPhRIbPGw01c1c0giynLPgfGAz8wcekm_fdfJLDEfwiEPxR52jRTKtVkVgfWWM3RAxvFhp0Ac1OQI_WpMDWbWy-CslufN_oJXOabfdUsuklsSMN-W9em5-0wpgKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=el4bTycDzBoLxSyW4Q03eCpTVkUQIV4wz5AuBd-CjB0tAIRkAkNr7ntLX_GPP-zXiI3Pj5xZy-7U2N_uBvPjOgck_yIAbPjSj6DgXUI2Dw5hUI-65j8wrdUNLpxADBPXtWjaQnx7yc7QKwCsp1OkPkRxRgg1hXuPzA5OVoS3120gheXriYLRM2v-zNks1uEX_DTUdeZS-2RNroTCRzUAvMD1nUwPhRIbPGw01c1c0giynLPgfGAz8wcekm_fdfJLDEfwiEPxR52jRTKtVkVgfWWM3RAxvFhp0Ac1OQI_WpMDWbWy-CslufN_oJXOabfdUsuklsSMN-W9em5-0wpgKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Z1XWSTfgcO3DR1pvNmzxlGFbmuJFNRlEyu4uIqotUjRDiYYUC2UUg0afctz-RngyDMUZIxNssA0wasCd2GCeJSVw9OIpS4WcfvTqXx9Q3RHwz7GkaVVXp0e_ZupxsdR8pdaHpx6xSmyEBF7yPMNY1uONbJUs2CBuz9N9hWD4ddrB-KwR9nEF0Y-G4bZL0iseF-yD7OCVYxTh1BXBWdKVcwaN0oAIiLNGLhQwmBGJJDxSRP0feqDwoTM0bzVGX95IHLUhNJCC1690eiW9sjyJnl4GPmrjfOpRu5h6EmpYJMEr3WP0zx2LCiUbDbcN4vyeGH5YKphQc30f_zP5oerXhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Z1XWSTfgcO3DR1pvNmzxlGFbmuJFNRlEyu4uIqotUjRDiYYUC2UUg0afctz-RngyDMUZIxNssA0wasCd2GCeJSVw9OIpS4WcfvTqXx9Q3RHwz7GkaVVXp0e_ZupxsdR8pdaHpx6xSmyEBF7yPMNY1uONbJUs2CBuz9N9hWD4ddrB-KwR9nEF0Y-G4bZL0iseF-yD7OCVYxTh1BXBWdKVcwaN0oAIiLNGLhQwmBGJJDxSRP0feqDwoTM0bzVGX95IHLUhNJCC1690eiW9sjyJnl4GPmrjfOpRu5h6EmpYJMEr3WP0zx2LCiUbDbcN4vyeGH5YKphQc30f_zP5oerXhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=WwjMaWhFyk-sinhcsWcP_n0YI4e7VUVKgCc6hBg1J7J-FaOpfmqGIHVuq9qPWRr_N7EENxzrZX0-cBtjkWCv5Zhr6EHPSjZERra7LYS09JhIdkZrYQRTDvBPFe1zYoDPCCWZ5JpLQjma7BNtmW8P4madcZFO6LiXd8b6-C2yKX4rx8KZWLBXxscv0gxZpzaVSg_0h8-GfMlGavMgGe0ODLaj5po0oRqD4LauGV6iuYxPtWFLj-A4sYgCXu5wl8kjcK3HnsktOvUlE_5wRyKzHhtMVkQJskYHLFnXea2zGTWqojl6v78Jrc_4ndXAQ-xmTrZu_dI2HWt77c-QnHkKQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=WwjMaWhFyk-sinhcsWcP_n0YI4e7VUVKgCc6hBg1J7J-FaOpfmqGIHVuq9qPWRr_N7EENxzrZX0-cBtjkWCv5Zhr6EHPSjZERra7LYS09JhIdkZrYQRTDvBPFe1zYoDPCCWZ5JpLQjma7BNtmW8P4madcZFO6LiXd8b6-C2yKX4rx8KZWLBXxscv0gxZpzaVSg_0h8-GfMlGavMgGe0ODLaj5po0oRqD4LauGV6iuYxPtWFLj-A4sYgCXu5wl8kjcK3HnsktOvUlE_5wRyKzHhtMVkQJskYHLFnXea2zGTWqojl6v78Jrc_4ndXAQ-xmTrZu_dI2HWt77c-QnHkKQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOqHXfUsQrY_UeGyZm3Whx5xb8H47jn7v4xb6i0L9lcNer8rP1ftBcNoST033apIHex_4atL4DVJOWUt_zjixhR6WZgszGaGMkM_XyfD-Z1bauyUzhbblB8mhBcUE2-ar58KSphplRGJkOblfZv4FgUQC10hOPttBHs6EBFpZ-CBOt3yI8za5Vexr2nVezD9M2dIOFEz3M-lCi3ks3mdFIwokF_VKlPGIXqnmLv0uTXdaBPsRRnFNSr3qVlU6w2OHvP3FanR2oIvLCswh3fd0-otPITkcrwS2TBv9ZYuubO8HI6-JE962P16wUqAOMGcBkyuYlQP40cWS6xjL3Shog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkxW42T-2zxfV_rMTwqb96C3Ff07ostGTmnhX8T2pl0zlA8l2IG7BPZ2-uSDixdpe348ItMESDlwIoa2K8rjv981f5Kdmas-Aq5BF34a8YX1ZB16pxZ_5BZtjjb8ucwMDDsIdjmXA2Gc418ywOeINIEwEM5yx0mJ0ltPsdtwxdgZfKZ2c6lPmzoLDrK0CTKxX3hTNOQAo7rVzLxkh468d8nDSJVYkJFKU25sZ1lmg4feazzt2bbeJvd38Q1NNqFyqoonAiBW-8GfuT87R9IydcNS9bPOH9Pdc1gQuLlNwfu_HqZu4XaE1qCtHJeeJO8pqF1PV0F9GXFlqlhLiYhDDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6SMrOJ2badM8HwgYvfrTK52itvd8CAnO0Nto875oJVpJtRfen5aUaHGJNIikcN9zYQKRQD8binK9soFo-7vNnq3k2kBUZOtcESPay8_GRS6bpw8dGNr5HrUeJx0iFgsdSPXqgK9cY2nCJjZmc4XADNt5Ff0wvEvLZTC9gj2O0aT8aAddrJXpvy6pfBlO9WrXNRbcYjtdey4NDRQvy7F4plUBoSBHLG-9jDrEYL4UqboTGAu7BT5BVhh5iJdJiY_86ew96Lldu1MW28VLyiQstnHiT-7dgiRgIThDzLX1gC4xNXWDZAZwUjbLVIW9HOb1y4XhmstnPHyecqcmEifvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYDHvlCUvgi3RRXHpyiuq_x5aZODKWV0jXOptVm6BCIJwaIekaAEJ1NkCq5auX0fUjZZeO5LxAu7ToIgVQISAhPz0G2ibIVppgldnFZjSqVCgRvWOU3s2NuCuF12v66Co65VxH-BsPWhPFzBHT9ohEPJtqtFHQGgZqJGhrhuwt6m0_ui6qRWycJX_yZptIHIC4sDBylqIkJgaw-TQ5UIZ2tlAcV5DrQxWp0v-oT3mc7jTHVcoGUm1xDgMJgG71otajwbJyaHQhLPgd4Dj54KvI-37CMaWqSmMcbkJ5TXpRGmf51NhHf7ycOe7IUhjDuJm7lKWElF6TB1tiPE64v4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut_ipmGKTmQ6372o7HUORnggYUaOuP7jjUa3zYE6FszVaAOtxjOnViT3vszsjneYJ6u8qlT5otVdzCIbH3HP_Yei40JTtEMkQ3byTrHYHgY3BB4hwAbVVmdX1S3TTVLsLItvK1Y5wKXCbm1Aolx4y0VMHSIbEiLHBQ2ujKTRdZXJGjYMiNYLAUNgULr1fr0kisOwW9QdrqpWhlkVMOZM1d9K8R2ncaK2JyyqyglOeHZik9veK_t_Ed3UpWmPeydc5yMiolrKcYNftWB0jvspoPuL2PvBbztY3velvpzFfRTDRFpDwB-j4cNYABz-L_jAswsKxYmj3fZcYn8ACBqyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEcZelL3ijWMmUK9QRmgYLqPmJyW9wlo0lwob3pS7R6hyLt9z7R2LPGvoHA5ohaI0sBkDc2oRA0kN5WoML56Wke7SunEpEYhhGQxcQYV6DzgNBnpkS1ko5w2FdndatCGbp65K9bDcKn3nbVI8YsJ9RTmAkHyhi76KwPBkhQuDo96JSBogcoyukMvjRFtumkn5Ntu7kUm92eNeD_4jzWxsb5GpqQK5z4L_HMDTHgoI_u-0tnB5SZ4cHwqSv_CMcR6lVT5cPrAd1mHf4aCXSI7eRd_Jdhtvi6NJYJ3GfjGPmqJKQaco3ErRAUrBgNZJLiom3EkYJe6O2LCV6HJPu_hcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWEK8YztgOld_-u77LjM2-LVsBnPTM8yK2TZiilJamxMaLFRj_c3Y8pd-7SzqoSYScE3C-ugEpY4H8-mBNbdvDJL9tiEUU4JONy7NUjNgWnBvK81KI2oJKKT_2qtFOzhe-5jYTrs8UU00L8YW_23FlSFDx1dvcLBDld9WsrQ_n-NZfyNn2e4tGuFC2PIuu9em0ym7rKCCAj85PIcg018ikoYn15oqkdyn0pirjpj_Hn9O2WA2X7PIvqABo-umuF51OEfBD_Jgg-WK94wno6rMbmBsW5mAeSWGkXdzK5JZihRS705cFPx7Ti-ut-Jssv_qld-XQU2SPzh5b4wgDR12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQUCKnZUMxua6NoV2qrAnxz2lDkcw66myt0wYsaOAM1gbyNF_JZyYrtAL8bFbeo4uTXEOxLgoBJ5KWZ0trxldLiFIWV4ny80toOwhmrIeUls6dCQgIco9V7KsdZ7GVmnQLfW4bC1jcV2yXtpSBTpJX4SjxgiDPsAY7Q0cnBaKEtsdWME5eP-6OKVswOytND3Qa4tUevrgbvqhMsya5SV_aAwRZRHaZP6AHdGzTZfkgpJvk_nbjoUM6RNlhUknuRq5ggIpT5nl3pHj-CloHor62i-z7UQl8Ud5to95O1EEKQCr8iOSWMl2Atwza2GlgYakSMAJipP32ggNYAI-HeZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=uat0gqQBUsT-7S_TVw-yj0xFrd6HGzJPV9511C5nnrGMF_kLljhU1KjTuStVinj6AE3PF8kNv6sD-4w4I3dNKcbhzjscDsgwGmVfD5UMkZXjpi04kf-wqP35QtJ0l2pBkCPBLgL-4xBgP21hz6_oM_fjGb3tWfVHau5etAWq1T8OAymW2LiAnr-MafG6W763E1_g9-dEGKeTuYMXBZ4Q_57ZWAzZ5e80TQraH7iLKNmGUzFsNtUf4fZ02VkvNLcPAKVv3OG1p4YWJt6Wl55L8gbOPH3Uxq5ZOSM1WEW3MlNAy0txXuGVSHpJMfn2ObC4DIaEWcyXZZwWJI9DZct5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=uat0gqQBUsT-7S_TVw-yj0xFrd6HGzJPV9511C5nnrGMF_kLljhU1KjTuStVinj6AE3PF8kNv6sD-4w4I3dNKcbhzjscDsgwGmVfD5UMkZXjpi04kf-wqP35QtJ0l2pBkCPBLgL-4xBgP21hz6_oM_fjGb3tWfVHau5etAWq1T8OAymW2LiAnr-MafG6W763E1_g9-dEGKeTuYMXBZ4Q_57ZWAzZ5e80TQraH7iLKNmGUzFsNtUf4fZ02VkvNLcPAKVv3OG1p4YWJt6Wl55L8gbOPH3Uxq5ZOSM1WEW3MlNAy0txXuGVSHpJMfn2ObC4DIaEWcyXZZwWJI9DZct5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=qg6KzJxkVtjFKy-hmfhNeDvSXahjuVD1oH9Sx6uOExvqT-OdxGqibPDi7MSKB1UruL-foTXtZ-ll_TG5RCqCvxCSeqLje9lMNeKbRX0S6ikLLaSaQcdhjpONorRo8dZuZ3NL9_cKrAS2-uMipabVXWyCQGmFuMA31tjri7OPBKQqobcn4fEtTWA3HjstAcpDsIOGS5nPmUIOeIFhnD7Nj6_Nkj6nt7fIbeuO0QM5AGqPgWuO82UBQulQbzNiFbFHpEwdaD7W9NOcHtyqUVfE6eyq5eOU5grI_NlM3dsit9xET6WrwJhNqA1THGd5ELz-zvq1M8c9XHrXay8ccAAOOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=qg6KzJxkVtjFKy-hmfhNeDvSXahjuVD1oH9Sx6uOExvqT-OdxGqibPDi7MSKB1UruL-foTXtZ-ll_TG5RCqCvxCSeqLje9lMNeKbRX0S6ikLLaSaQcdhjpONorRo8dZuZ3NL9_cKrAS2-uMipabVXWyCQGmFuMA31tjri7OPBKQqobcn4fEtTWA3HjstAcpDsIOGS5nPmUIOeIFhnD7Nj6_Nkj6nt7fIbeuO0QM5AGqPgWuO82UBQulQbzNiFbFHpEwdaD7W9NOcHtyqUVfE6eyq5eOU5grI_NlM3dsit9xET6WrwJhNqA1THGd5ELz-zvq1M8c9XHrXay8ccAAOOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=EKvGiH1ubn6q6LvJO_mdkAnaDo5gtgQAGW95BdRnMpNoFZzdQYkpKdoeEBNzFRbVajhp4MyKA3aKUQSpZTsGqcFwfvx4ODE7VJztVe1P3BZ89S8zEYJXoLmfgOJ0tI1iQJsOq7cpU8wjbE_sp72-QNkLY2M9voOcyIOA1wzKBLqFOvl7UuRj1pjc_uNbpjlflP-SAZ98z4y1Wg4XPNin96HF5GVpybx8m3nXNel4AQFfDw0FODXXPQ4vZX9WdzkgEjgd6WNu1LaOnoLpVahW3AU0GlBCr__awSJvWbOQeAoKMqa_cgfE-MKciANdfhFnmcxLYGbFjVGwhcPpF6kp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=EKvGiH1ubn6q6LvJO_mdkAnaDo5gtgQAGW95BdRnMpNoFZzdQYkpKdoeEBNzFRbVajhp4MyKA3aKUQSpZTsGqcFwfvx4ODE7VJztVe1P3BZ89S8zEYJXoLmfgOJ0tI1iQJsOq7cpU8wjbE_sp72-QNkLY2M9voOcyIOA1wzKBLqFOvl7UuRj1pjc_uNbpjlflP-SAZ98z4y1Wg4XPNin96HF5GVpybx8m3nXNel4AQFfDw0FODXXPQ4vZX9WdzkgEjgd6WNu1LaOnoLpVahW3AU0GlBCr__awSJvWbOQeAoKMqa_cgfE-MKciANdfhFnmcxLYGbFjVGwhcPpF6kp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=lrL097ype_PmC-CE5QkwH_S1AZPThGhP7So5DO6o_7xkMMiyfpuuJB74VHJN0tXkoYP103XesM-_k5B2nAf8eOuXL_k4SkDLmlmXh8zcE3i26z5cW79K7dL1JCNVl8jXvox8K_QpW5aHnhSMc_Rb5S-u_odZPEcJJeIRq9pu0y-u1HHlhmgSTutJw7uaX0CAx4qKkjBmdVz2gbRgwnpDcQha-bzDyFX0O3e2FWFZiiMbyV4Mp6HUTzwA54W5_pTWfvfgdxZBFC1q5b-Rkv54dUaWh5y8TVw4XbXoFv62oFsFhxYEcb4d2sPzqRZ9jIfl5r1-2XwIunzXM_vfqh9TEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=lrL097ype_PmC-CE5QkwH_S1AZPThGhP7So5DO6o_7xkMMiyfpuuJB74VHJN0tXkoYP103XesM-_k5B2nAf8eOuXL_k4SkDLmlmXh8zcE3i26z5cW79K7dL1JCNVl8jXvox8K_QpW5aHnhSMc_Rb5S-u_odZPEcJJeIRq9pu0y-u1HHlhmgSTutJw7uaX0CAx4qKkjBmdVz2gbRgwnpDcQha-bzDyFX0O3e2FWFZiiMbyV4Mp6HUTzwA54W5_pTWfvfgdxZBFC1q5b-Rkv54dUaWh5y8TVw4XbXoFv62oFsFhxYEcb4d2sPzqRZ9jIfl5r1-2XwIunzXM_vfqh9TEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB9-tJB13gh3dLuFLqILVA0DfZhsH6ZIpO0Zpbz25vPN3qNvkbHkPENJUVDjfoXjDZAah-v4W_lZhUwVMELbyCfKh-HV1SVoiDPMcwq0jGZoXWlrpvYUzYo1B6uLx5oa3Zj4fufBB2op8GhTMmmrLG4Pc6vPivkB2kgUhZpGkmHjstW3hzRMk6BxglmzEG3jHTBSgJQ02pwVYEwbWUazPULnFlIob7RYnIYPRgS9H7D4mRIUnx7_I252gdwnxd0qSFqMT8TfvqUiszZSD9dGJnnoBkpX6gBPI7C44GMv-92yaLaPU_ZZe5GlG-bx5TwIvi5-qjltPLAe5SDEmad-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1ihVYJJyIzkb1w8p0aDg-UwlEHSJYFAF5EKnHT3RzoNNDsc4bNBRt2-ENCnQt8YyzYTQzRXzb26K-quJARsBSrFtdXWYX3J2ysvHm878OSaSKZAfcUEnlKRw8GmxnD-omJX8N8MBp1FVrchj4Ua7BzLpIFJbtL_hxQz8pkW3fGonRb183_nNIY0QPOYH0vNj7a1YUhQzJEyiFwJNVUxosD6p4eZS-Z6wcsq1vPqksKK6piSS-_PT-jR9YzbYn1QXDc2yq8HMcAVK6qwyzQhQYFq-K8N49BNrScE-_YtOfw-bU_ySQE3RZMwUZvzWW7iyABR5VXYMLrZZ_nAbZ9BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oKkozbw37gux_U6rmRkdqv0J6xITC1lLeaE5PslgFfX2921weFIjV7toHkURwBHcUGHXc9D7y3PJxBqbhkI60MZ6qPJAPxwOpKVzatF4ueYav9UfihEh5qj1w2FBfF5BJneYhr9EV842AhP2Qom88gGxipHtRzisqqGz1tuFjxMwi1rRq55Aubr7iPxbdkspgsxO9JTcP0pZmGs1_cKbIPwo-CVqqr8YKjhiKMMr6xKzLwvmDDPIHyyzUN6-p1hj2igEb8IzYmKioaeAECL7VCgVxfHOh2Fhrj6Ob24vSEA0pxezfWJnN5d3I3cg_GsAItSg0sv2pBcVng8sbA2WzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=E5_lffhX9K_qUHpBavg9MA7VjW9RsNodHQUg66okqOgzTS9VH_LDefg_K3nB--0ijrT_tOOVd6-XnY7qEkzOstatRr8WV-AGW1D4TXW2muazHAIher2nfhxBd2f8n21mKsDBXoUu7g_91nR4EQhL1yEKmufH7yBcerLBCX-KybNPNcF2ofA2WwkLS3qok14FzdnlFZuFAAR0SWbhq8Mts-OiNDDSzqcgJ_51VZ-4lXPxotf5fjCe1s1RyOoRcE-VzzQB38mddMfWe6gN9aNe7xW7Oc3w8_qZamaU9vepLLbdhTEUTDngYoDBZ1zczMOJ5ErsLtLUAC3wq0q1V0tVewyxxa34gcXHmklr1QI2PSBj0yC5agIJxpSkKsnhSzeLCKnI6fbpIeW8tAKHybs3NbOHRM9YMRAi1tD2rG3tZCTpXdOJ3hYGFgbyyd4DdV-dEmI90IwrhcxKnx0aeGMK2U8RNZuVuEbGmXU2Ln8S_LZrLnWTkMhUOJHxsv3yx7lhwLjuR4oEoFSWLeSRVnZF44IWy6Wa775L0kERlWMU5ovR_m98IPtX6AR1XabnDNcl5zZDXy9TSf-qJ2Ql-xIc8ZjLLT19teU6Mv_Eitg6d7j8R3RSaCC78w54cWT8AAWLS2RlOz1Xb1M_S2ItYxXgfjfUU78zAAmkl9rudcRJ6hM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=E5_lffhX9K_qUHpBavg9MA7VjW9RsNodHQUg66okqOgzTS9VH_LDefg_K3nB--0ijrT_tOOVd6-XnY7qEkzOstatRr8WV-AGW1D4TXW2muazHAIher2nfhxBd2f8n21mKsDBXoUu7g_91nR4EQhL1yEKmufH7yBcerLBCX-KybNPNcF2ofA2WwkLS3qok14FzdnlFZuFAAR0SWbhq8Mts-OiNDDSzqcgJ_51VZ-4lXPxotf5fjCe1s1RyOoRcE-VzzQB38mddMfWe6gN9aNe7xW7Oc3w8_qZamaU9vepLLbdhTEUTDngYoDBZ1zczMOJ5ErsLtLUAC3wq0q1V0tVewyxxa34gcXHmklr1QI2PSBj0yC5agIJxpSkKsnhSzeLCKnI6fbpIeW8tAKHybs3NbOHRM9YMRAi1tD2rG3tZCTpXdOJ3hYGFgbyyd4DdV-dEmI90IwrhcxKnx0aeGMK2U8RNZuVuEbGmXU2Ln8S_LZrLnWTkMhUOJHxsv3yx7lhwLjuR4oEoFSWLeSRVnZF44IWy6Wa775L0kERlWMU5ovR_m98IPtX6AR1XabnDNcl5zZDXy9TSf-qJ2Ql-xIc8ZjLLT19teU6Mv_Eitg6d7j8R3RSaCC78w54cWT8AAWLS2RlOz1Xb1M_S2ItYxXgfjfUU78zAAmkl9rudcRJ6hM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=fZtAtHDvj6M73gSGp8rwHMTOKWmUM_u6G6wsS-G2bSMDloMuMg7NCgjDdSipcGoHXzuMvn6hNyZrLvxjB8GAkVcScHZxld_pi-xP4hUiYva9z-BK-54nUU9xApT2TKwR5MUIx_28-I8-5IOr4xXEcJAf-meBS2-7fi-Th2kD6xj-jNR4W4IInksgF34ZzNaEzF0c4F0b7g1XfjUzHffgR_1RtGrALvVvlw30yDz8ae1Bhh2UJmnt0EUZ_jfddWs2m9lS_xe8XNMyJ9JDSrBZQitLfzGnGHpl0IZnZ2VlIJ6JOsC2TkL-zjCZfhfgJd-_1oVSS0p34DKSKtP5oieXhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=fZtAtHDvj6M73gSGp8rwHMTOKWmUM_u6G6wsS-G2bSMDloMuMg7NCgjDdSipcGoHXzuMvn6hNyZrLvxjB8GAkVcScHZxld_pi-xP4hUiYva9z-BK-54nUU9xApT2TKwR5MUIx_28-I8-5IOr4xXEcJAf-meBS2-7fi-Th2kD6xj-jNR4W4IInksgF34ZzNaEzF0c4F0b7g1XfjUzHffgR_1RtGrALvVvlw30yDz8ae1Bhh2UJmnt0EUZ_jfddWs2m9lS_xe8XNMyJ9JDSrBZQitLfzGnGHpl0IZnZ2VlIJ6JOsC2TkL-zjCZfhfgJd-_1oVSS0p34DKSKtP5oieXhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poEwpruKpjnBCaCz4V1N14XHrcSL2_uIjEiV6oWQBn1_r5j1hZfzJDupHsE0PUzXqPyc-gYcwz57N-9i1GvGAu9XN7mBfD2uLQYnojzvIA6ZKM5oQ74clzGlxp4iNxkOVuDUTz-qifC3uO1pNsugq2GmCWHRC-sMML87chdi-Np7eZE0EZDGgfawtksKswySUixcCYvTTNKr_N6O-pkyS--GvhmXIVVShc-hvInptvBlFWpzKSibz3Q6ZMRZU7BPyJ8JAJZAhwzleCiz8xSUs6ykJlW20oFi5nukzJMLGgiK0coRrxKpPIEgj2UaTYFdeRhDZ6D4HYw-tAfHdC3N8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=F1MU-wPFn1ZVPG7c4rca3d7Fct69RQ5CJvMKi1IJ3E7uh2Cg3UPvx3D7lFCgL_m2J34w9_xTNxT1P9Pn1sVABi2RcZzxvW1r-HnimN-XBfR1_O-piQOVcEeBpSS1502Gid5qGp_6doseAUG0948h_Jllb40cFNdKgCODFzWeeO4TCPzj9wvTRfYo4D2Leanw9EZLcTESS8Aj-uHItIX7lm2Eoicgr0lBOhtOtO_xJnHePSEljdjwidXgxLgU3Gn2UkCbH-B67DidnpkeczYyHVh3e2NOc6MTDBBbriBIF5aoe1mnMO7AGRCULh21hVF9JBE5Guru-1pRW2c5FtWwCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=F1MU-wPFn1ZVPG7c4rca3d7Fct69RQ5CJvMKi1IJ3E7uh2Cg3UPvx3D7lFCgL_m2J34w9_xTNxT1P9Pn1sVABi2RcZzxvW1r-HnimN-XBfR1_O-piQOVcEeBpSS1502Gid5qGp_6doseAUG0948h_Jllb40cFNdKgCODFzWeeO4TCPzj9wvTRfYo4D2Leanw9EZLcTESS8Aj-uHItIX7lm2Eoicgr0lBOhtOtO_xJnHePSEljdjwidXgxLgU3Gn2UkCbH-B67DidnpkeczYyHVh3e2NOc6MTDBBbriBIF5aoe1mnMO7AGRCULh21hVF9JBE5Guru-1pRW2c5FtWwCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=LfCY5Vcdh-R_RsHIpkg2HRU8vrFpr-_XyENfVVHaQm9g_6OngladbyyiVEDDxyvUljVmezLAGvnIC0MFjkDzPY3r3Gy29MBges1KNWflHIRFwpBllFMT7ELsqitrR9y_H_rPUfdPL5XrVXjkykkUAOa56Eg5zdDUhBnbAnaf1_n_Cw1uxH5UXLewg4HJBdMeH5xJPTj8Mo8dId8jEzJocGl8VyGclAR_Af6vS3BngGruvUowUexnhmw0WHJ4sT8EMnNqaA8c5ASGrj4Al0nLuzw58xUTmGOcUmA7uVRzH6EzSYf90kNwUmq56J7hOJwOWVtqabtZCvZafAu9ip9kSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=LfCY5Vcdh-R_RsHIpkg2HRU8vrFpr-_XyENfVVHaQm9g_6OngladbyyiVEDDxyvUljVmezLAGvnIC0MFjkDzPY3r3Gy29MBges1KNWflHIRFwpBllFMT7ELsqitrR9y_H_rPUfdPL5XrVXjkykkUAOa56Eg5zdDUhBnbAnaf1_n_Cw1uxH5UXLewg4HJBdMeH5xJPTj8Mo8dId8jEzJocGl8VyGclAR_Af6vS3BngGruvUowUexnhmw0WHJ4sT8EMnNqaA8c5ASGrj4Al0nLuzw58xUTmGOcUmA7uVRzH6EzSYf90kNwUmq56J7hOJwOWVtqabtZCvZafAu9ip9kSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQhq8KddfPijItcPXfZf8lxh_u4AYj3d95S4JgOAbxWmgaX1rrIWt6odLA-im11RhG1wHCPd7nAxCq7lGsyW3n8sK4YihUU5M4zSrB6QUS2jtOI6xJTDErhmkm7Wc5gktH3-8Wxiwaqrmjo5I1U6RctjL4Q_vj1hGruAvN0Nj90t8G5CuiB5o1TqGcY1Kk6DBRtqOIc7x7FXXlkIaV5uRa9xBL-N0cRpSdVkpHBk3KArZwjBQMuFQ6MjfCEXtn4vXrt0xSOFLwtNp9NKXWIBLWaOzKSavfyNkHSKb0A9vuGi7yFQ84J3KLKxMect90LCDxpaqUBk6dWmflcrrKGqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim8Tm86Ia3uQlcln9CAAofSgQsYA7KxFzMizvuncBR2w8sl3ms0LJzKsQPsqJA4kFsNmNq_O6r_25SxMpzrLNOxNEUYkxM4N_5Pya93BnsV8DoaLd43Krq7owMlYSHOcgVM5cXG4L_hlUucPWy7N6Hk8KkYMibu9K7-bATgvNCa9ceQA0QBIJfrBCDCJS4wTRL1JD7cukEXxoe0neNYe3wjWuiX-xeOx9_MIjZARkm9Dm9jg-JJaJcf7YKx16hK8wvxtVaA5cuRm9mWMe7ORLGgm7iBkN8e2fMgutxn3efO1Cqia9xQG4vrMGOfMVkEZ1WXh94_byZa3ERNzs-M7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS92frNBjvNcW_DnUqINecIOkDrowB6GwDyHiJXm8X4Cm8uAWGsvPFDZVVLlfkAWUpgv6kA7x32rl1z6PEeIwPE6H6qpX3PgeP15-XYmLXyJtO9-xwnBDXuWBdMFEXXnO-elMDW01PRZQh4r0PN850aKl5GEjA4QWKfu38UtTaOuA2k_dYup84jfpvDodH0qZhQYMPardyxQWnkX6tP-cf3MPpHRAHJjJLDvSj0SEumQT8SLulHgxWhaY_dlqvrv4dH8a4GuTzIssc5oyeI5SDHExnIyyEF3gwOU3nUA1bhZvGyuHYY0wNHN2HCBJ3xZEt8HMWJhCmicDjxXDWQWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbi9-rw6Wu6kgtiWha9M0k5cIBJ-RP7L1rl68fUSgd-8uXm9J1LkGsojwge9WBJqC_UyvwpOKreZCT9BMhQ0KGqI_J0Wf3CaR9fzLbDHRUarBYoFCKg1PVOipBP65a-jl9WRm8cN6Je3P6NB4G0uVCCcoD8nObaTu8pO9SWPPor4tsG2dcP_ivLhV3HOAXjWNlNTwnvipTHcngzcxy29FVKIE-wlhHdzrVeyxIBz2nnk1paS_NRSLXHXzs-L5rFfNwViXR-ukVZHbIeRfAz-QtWP_25HpTrtJFZrUY6udr6NxGtWaXawRZbm8dXHWymyeQbAJxBUoQHFOtMfi3aCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=rhW7hQrpgX7UTq8cE3EI45xBCpdQRqWHERZJoTWFr8mrCexgcFI8igmkgtD1k18_XHvvC6flCAnyFl_lyWpNG0cJ57t10ikmq7tE0Fjk7BOWjtMAnLwn6D_INY5qNef4aqfWh5V7wATq-7NUmGRYwMROzxRIzlXyB7gDdlkZ5IGZOhEW2Dq1KDQb-se9UvIFN_YGyD8JRpq1xg2HXHgk9oHlooS4z9cj0E6r_gFxaqhr2p6-qyjv96LsUB2dTj1lIjT5SjLEi92nhsid9nZX5gnZ4YzXLuHO8sHpT7q9jNfeddmDXpsIA75NTUbg4Fb3hyrGpSX27-jub9x1fLjtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=rhW7hQrpgX7UTq8cE3EI45xBCpdQRqWHERZJoTWFr8mrCexgcFI8igmkgtD1k18_XHvvC6flCAnyFl_lyWpNG0cJ57t10ikmq7tE0Fjk7BOWjtMAnLwn6D_INY5qNef4aqfWh5V7wATq-7NUmGRYwMROzxRIzlXyB7gDdlkZ5IGZOhEW2Dq1KDQb-se9UvIFN_YGyD8JRpq1xg2HXHgk9oHlooS4z9cj0E6r_gFxaqhr2p6-qyjv96LsUB2dTj1lIjT5SjLEi92nhsid9nZX5gnZ4YzXLuHO8sHpT7q9jNfeddmDXpsIA75NTUbg4Fb3hyrGpSX27-jub9x1fLjtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIzX3g-usEMPSIFq7LyRnN6bzZIV2nczJhCjkg5sPmwm4-c7NrWgXfnRpjaMDYntLWwc2STBFvnVMxe5dVK1pb_xmxRWomtMMuHdF3iqsOKeIStdeX65ewGd8qC0fm3Dfg05g-bD5jD4-zMMwidScGj2prSoRL8TH7Rrtdabi9uxciUda3lGFAA6pq5uGbytdZTvRPEQ_7L2rIo5FhRCnpswM07dM4D2MI3dZq1z3v43k-HVO_cGdRvKbG9NN6bgUeiJLORYjLDqeMVU_O0z61zGUFMHU3IjU4AY3RoMxljjYp9lyul3MvPnGvaGX9Y3r7OTXktonXaS9bTbsR0Dyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=Su7NfaYunAHupyWHtJ0e7Kdq3o4jGgEoQehmPyflSJ0YM5E00EPV_V1cGjvV5hTxWzajpaaK5y_ZpntCnB8PAg_cN7duJiaG-bojVQ8Mzz7QCyLuZrhXcihQNSFn-SNBpCQxCUfyABN6PwSzRNi46RgYyGujWNP6W8jHdMslJAl2Ow0lMAJgcf5UyC8dsD5eavKrSaph-erAUOU0fV_A5nz93Y0S4goIk34CaEs1_iCAal_IStwczkWBMVDlpphJkKHd5f4rHGzVKgkUmi5dlb5wrDCBgv2xdcdxOGB22B8Yx4c3ETyBZJPk31iUguvD3f3vLgtYGKD48DpoGCCAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=Su7NfaYunAHupyWHtJ0e7Kdq3o4jGgEoQehmPyflSJ0YM5E00EPV_V1cGjvV5hTxWzajpaaK5y_ZpntCnB8PAg_cN7duJiaG-bojVQ8Mzz7QCyLuZrhXcihQNSFn-SNBpCQxCUfyABN6PwSzRNi46RgYyGujWNP6W8jHdMslJAl2Ow0lMAJgcf5UyC8dsD5eavKrSaph-erAUOU0fV_A5nz93Y0S4goIk34CaEs1_iCAal_IStwczkWBMVDlpphJkKHd5f4rHGzVKgkUmi5dlb5wrDCBgv2xdcdxOGB22B8Yx4c3ETyBZJPk31iUguvD3f3vLgtYGKD48DpoGCCAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=oM3CsIEHYpqFOmwQqL1seGa8hYtSfK7HiaeRhVyULwu2ypAydFta_kq5hYlkpAemAxZOUzsyipfnm_4TVapoNJb1IHwku6zRXEWqG8jx6ZSp-NtbSlW9MDQDvBk-Af1bNc3qphWY-TQhQP9XteZIrySoRh5ytJbw_2WMl8qXM1yqWAzni60mK4y8IR-8mEUOUn3kEXSfC729MkfMBNDN_RFxx7kBW_uYB78eNLbKcW3Y5zIZiO0gZsQl2S1gis7dzU4P_EDfJ51xvXe0nwA7DMd22r6SyssF_L7R6ensBT_ByPpRdCLbfXiC1gl42ZAHZQC75MMC0oDmBCZzKPYy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=oM3CsIEHYpqFOmwQqL1seGa8hYtSfK7HiaeRhVyULwu2ypAydFta_kq5hYlkpAemAxZOUzsyipfnm_4TVapoNJb1IHwku6zRXEWqG8jx6ZSp-NtbSlW9MDQDvBk-Af1bNc3qphWY-TQhQP9XteZIrySoRh5ytJbw_2WMl8qXM1yqWAzni60mK4y8IR-8mEUOUn3kEXSfC729MkfMBNDN_RFxx7kBW_uYB78eNLbKcW3Y5zIZiO0gZsQl2S1gis7dzU4P_EDfJ51xvXe0nwA7DMd22r6SyssF_L7R6ensBT_ByPpRdCLbfXiC1gl42ZAHZQC75MMC0oDmBCZzKPYy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH3GCq90_em8MnihXFivoJ7mYe4aM_K_6LDdRSO64FPdM9srFQ-SiOE3uQ92_YkztsEfg4KyayH2p52eU-rhH_uB4N8xYJPlOjLfQ_UiEPA1BNnEJprT-Ca2GpkoUwcGhxsslEYbdYbq8BJZz32gC8EnQ3UnDTBNEFhWexT3ckRE1uNGtN4FhzDo6nhbQhbtU7IS2Ek0VPILLXlXRCFfdJSz87eNMXtfKyHu7se3gWBcHNsswHoeKpI08Y0T-7MEFcbLGGByvTnSgKCBP01Fie2ydvfrmKbX6ZQcufKBhl2XiI67GhymcliQp62hHK6B2OzJdPZJQXrU1vGEaFEnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=Z8xfuqrRUnFLMuaBCehji5k9fzKU2_rNfgx4v2A7XJ_H7MThtViFTDPx5QyI7fulUaQm9NRi2gGTE5J3mOmm4Qd9UpljMkQp-MqDSqcNL5VVsRdnF5CZTRZhnQ7M75OvwNosdWDa4eikjs0UO0BndHC6GVGfdiQcxM_GicrrxHXJ7WGEC0bYrU-3YATHC9g6B5PZrISuKAoNzYajuUSjCovvgZL52--6v5sPv7B05Pw-SUKS8qRSHJC4_pqb3_3mOonMhiRguTygn_PbDa8t-Bt48In-2NmylDLN6cRC0Q6_5R7uk7Z-bR7aUb5wUE2wTpCPJRa-bgYuvAAyNOSNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=Z8xfuqrRUnFLMuaBCehji5k9fzKU2_rNfgx4v2A7XJ_H7MThtViFTDPx5QyI7fulUaQm9NRi2gGTE5J3mOmm4Qd9UpljMkQp-MqDSqcNL5VVsRdnF5CZTRZhnQ7M75OvwNosdWDa4eikjs0UO0BndHC6GVGfdiQcxM_GicrrxHXJ7WGEC0bYrU-3YATHC9g6B5PZrISuKAoNzYajuUSjCovvgZL52--6v5sPv7B05Pw-SUKS8qRSHJC4_pqb3_3mOonMhiRguTygn_PbDa8t-Bt48In-2NmylDLN6cRC0Q6_5R7uk7Z-bR7aUb5wUE2wTpCPJRa-bgYuvAAyNOSNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_OSVeCLBrH17B3opX-B3nmmGt80rlraduNZFIZ5G-mAoPrJHHaJ0J1Sce6r2-Y2Yer0f7Uj-bAcAY05-8TlAToui4f54-quSH0fLfMWexJ6TZYNPGmDvM0GEODSgSCxCQcUdaLs9uUMPGj7KEUI3A1_Ai52zsWbBB4vMdVxoe0G4S_G0p06bJaWGwD6VVwUy3v5LOcCPtsNf9R3cB_K0Uoqu69Ajf6twgoDOm_o7dk5CUdmkXlC2sPIj743NkKNM17QRNXYLLV0JgvHhvaNXUJ4BpJ6GJ2wj1tQAI764B8KIDZq-uBvnk8GtYuKy_1x5Bc6BF4dorzzlmwezlFHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
