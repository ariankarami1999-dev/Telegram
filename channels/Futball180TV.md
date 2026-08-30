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
<img src="https://cdn5.telesco.pe/file/XKVbbA7f8rSpsPgQjGcwdPb8W-qgAreGmeTv04qAKJyl1W3N1WLiI5R45GlbfdS5HoP7G9qODS_w12ShjYIzmWAq2IwU10A4sGLS1qOrI2ipjD6osmGifaVtNcM8KBuLEnV7GOOpWG_df8uKiOjeDEMP-rkQMW87KcziMDFUstJGo5dUyhCB-qW-8C9HRcQNlu37pWgK3wVlEDvmorfWJLe9VC1BgZ7hVQaYvenpdfItTNMZwmCTdhyKsiwsJZDqhX-QbB1g0j4yH6RF6PTnheO-TSCWis3NslRJn3eSW9x3YSNq7qVbiNxcUp65Um9MMntnJEs37G9BfGipic909g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 436K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-105127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d54666045.mp4?token=EwLCFie1OLDDrn_MnYuR6sUwXqkrqIN00T90xpN4G2G-m1ba6ovGR8z97-B8XWvSCchrg0FHC25Nv_g_2n7pQT0CDX09yR1gqDwvund6xvTrGGIrQBEnwg1eKahGNezGS0-QqKUD45oItT9fejbQtlhErXTkT3QvGSk0gOjGTWFZCwsF7ZZcAMXjwAFMPfmA4xbuKCn9wDlu8GxJElyLCGLKjVC7-7ArCc5YPq0tqt26FGQiuxHHgY8j_0QPf4vl7npBJdNMjCPTlBeuLvMzQPEEBFInEvi7ma4ET7LW40_XMDMnVcHG_zx4qFqDG6FYpRWdszlWn4mPfUkCvKoMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d54666045.mp4?token=EwLCFie1OLDDrn_MnYuR6sUwXqkrqIN00T90xpN4G2G-m1ba6ovGR8z97-B8XWvSCchrg0FHC25Nv_g_2n7pQT0CDX09yR1gqDwvund6xvTrGGIrQBEnwg1eKahGNezGS0-QqKUD45oItT9fejbQtlhErXTkT3QvGSk0gOjGTWFZCwsF7ZZcAMXjwAFMPfmA4xbuKCn9wDlu8GxJElyLCGLKjVC7-7ArCc5YPq0tqt26FGQiuxHHgY8j_0QPf4vl7npBJdNMjCPTlBeuLvMzQPEEBFInEvi7ma4ET7LW40_XMDMnVcHG_zx4qFqDG6FYpRWdszlWn4mPfUkCvKoMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
😳
کسخل‌کردن مهدی‌طارمی توسط بازیکن شباب‌الاهلی در بازی اخیر الوصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/105127" target="_blank">📅 21:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grY5Az3fSi5HUww4bT9HILr_xdkaMLnb_NRyzRohdJqs62tl8u7x3b4FX5OtUD0MxfihQZEmnetB8qu6NdbgjuEdvHkegiFhZKdd0aBqIj-ndjypEFLfaMbsWo2yLBsxgglfh38b6mt7yIURIsp2e_eyjL7pxZDAxh7i5127cBKJ3t0FyrKLN_UgoJBhm1JNUfWLJhruVuQf4x9TwTfJOrLuGzWPLcIW0Vm9UtGxiW2T_suKHq9SPUQ5xPXx2UjOuUA-s8Baz1V8Z5PtontC_iruCEpJ-w00lzUjMRBMhOW6uHQPH01I9ckzhwq9Zy7MZ0oPIFq2l1EsXRJXNpqI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/105126" target="_blank">📅 20:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">منچستر سه تا به ایپسویچ زده برونو فرناندز دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/105125" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/105124" target="_blank">📅 20:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌برونو فرناندز مقابل ایپسویچ‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/Futball180TV/105123" target="_blank">📅 20:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🔵
❌
کریم‌بنزما فرانسوی بزودی باشگاه الهلال عربستان را ترک خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/Futball180TV/105122" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=hxMunbKZ1FhHuWg95M_m0ipTNNG-QB4uizfzGLo5LcuKciTwloD51GwrN5MtRnBuLsmxU3CevwM0a0D0zrrmxtYNDoJlvBM2KVaP7iOqH2GEmzn6ciy3B_wNxpLXbbSyeDMu3pKFz6vF0fe08cWC_SqLlWH9X9d8khJij-rVHvH-V4MoS37tCN4ZL8x3YEKXFz-SfnKmAVVuLcy9XT1NB5tUiW-x5GG8l9j1JLruh1MnZOkBmbRULiBbjuOF0FKDqx7V0wRcOsxNLlJeQpdLitVxuVVAlDm9V-vsrZ2UqCfw37K0fNKd0XoSu1m08A7w5eHT_C3xuFrf0P-ONymE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=hxMunbKZ1FhHuWg95M_m0ipTNNG-QB4uizfzGLo5LcuKciTwloD51GwrN5MtRnBuLsmxU3CevwM0a0D0zrrmxtYNDoJlvBM2KVaP7iOqH2GEmzn6ciy3B_wNxpLXbbSyeDMu3pKFz6vF0fe08cWC_SqLlWH9X9d8khJij-rVHvH-V4MoS37tCN4ZL8x3YEKXFz-SfnKmAVVuLcy9XT1NB5tUiW-x5GG8l9j1JLruh1MnZOkBmbRULiBbjuOF0FKDqx7V0wRcOsxNLlJeQpdLitVxuVVAlDm9V-vsrZ2UqCfw37K0fNKd0XoSu1m08A7w5eHT_C3xuFrf0P-ONymE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇦🇪
فرشید باقری: بعد از باخت ۶-١ استقلال به العین منصوریان در آسانسور بلند بلند می‌خندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105121" target="_blank">📅 19:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04532a5e26.mp4?token=Vd5a3j1pVlH1h2zBeqJXIbqIjo587k8v2_TVIgM6sijcOBjklWEKjvSDzr8PG4QHIrNLyV0O0rtHKDxc09vogFRO8TXIn2uf5VyhdCUl-FBuUDFWW8VTN3nX36K8dNTR5K2SZ2GqiogZounD9xstcco5sGuiiE96Bu7U66loABzmFEe1Ji3l4Cjqib8YsPE_4ra-oyIUXZHYjyPdMM2jKXQq7-CEXvRCcxtT4RGgN1bZvvN_9cfoXksqJgK_ySyMNj5OD0EIDZEmNs-Zs4HCw22DoXZo30W6x6htDrwa016hEgbTqv912l6xW-zPwYbe72WRbuGkYmLthjVCERJERXTYG9lPnMqd6AluFYsAiullXyq-UF_JsULLG27qWjQehfEwHUhHXABLSONAZsOt1R6H8-8Ler7HJTNaioC_EjdxiM4V8kOKBEix-Y2miq39AKNGoxa5FxHcbTFQwEmlRyBK-3ixNYZV76w4G_jWwb3XVcJZBiJGzptjpPKxas4YUT3GwvUtQ2ZQro8t768e00R-N18u0ImYIaH1VjGskYiY8K_c6M5FNWxQ6km8n23z2tJwppI0CnsyJlfPX1wxgJk5knFurKyREFHPjR3VxrgTQEUrqe6_WeKamJQuVmCPzFXpi8L-q75piWNt7w7o5-S4v_kxIk3ZGFP-87uoXl4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04532a5e26.mp4?token=Vd5a3j1pVlH1h2zBeqJXIbqIjo587k8v2_TVIgM6sijcOBjklWEKjvSDzr8PG4QHIrNLyV0O0rtHKDxc09vogFRO8TXIn2uf5VyhdCUl-FBuUDFWW8VTN3nX36K8dNTR5K2SZ2GqiogZounD9xstcco5sGuiiE96Bu7U66loABzmFEe1Ji3l4Cjqib8YsPE_4ra-oyIUXZHYjyPdMM2jKXQq7-CEXvRCcxtT4RGgN1bZvvN_9cfoXksqJgK_ySyMNj5OD0EIDZEmNs-Zs4HCw22DoXZo30W6x6htDrwa016hEgbTqv912l6xW-zPwYbe72WRbuGkYmLthjVCERJERXTYG9lPnMqd6AluFYsAiullXyq-UF_JsULLG27qWjQehfEwHUhHXABLSONAZsOt1R6H8-8Ler7HJTNaioC_EjdxiM4V8kOKBEix-Y2miq39AKNGoxa5FxHcbTFQwEmlRyBK-3ixNYZV76w4G_jWwb3XVcJZBiJGzptjpPKxas4YUT3GwvUtQ2ZQro8t768e00R-N18u0ImYIaH1VjGskYiY8K_c6M5FNWxQ6km8n23z2tJwppI0CnsyJlfPX1wxgJk5knFurKyREFHPjR3VxrgTQEUrqe6_WeKamJQuVmCPzFXpi8L-q75piWNt7w7o5-S4v_kxIk3ZGFP-87uoXl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌برونو فرناندز مقابل ایپسویچ‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105120" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/105119" target="_blank">📅 19:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=tQzOpaAUyDuXTebi_3DhYDaYOVwLsAWPbe1YzLbmF7uTwTtDv-ady0Wid8Ez9is9OmnLV7-I64nN1K-bfFTVJlovxTeO_E2OUAHb75xUe0Na8vlhYL38e1swAN-yU0YNhZkGmFt2M5KWPj5FO2KRtOYBVDkUUOUGAmckyVvSU21N3POCDV7s0VX2mkaLxjJl0dbR4qdWuU-M1_yXkwfEVBjJ5IibQTT8l4hwRfOPqgBYAaCo946mv4XcqMFy3YoIfLxmnFtk6HL9-JrzWo-562PgD03d8N5XIPZk3Nkn4A3b_KTTNBFoLRCPsK_JibTia4TcRzYbvS-SE-0v0xXsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=tQzOpaAUyDuXTebi_3DhYDaYOVwLsAWPbe1YzLbmF7uTwTtDv-ady0Wid8Ez9is9OmnLV7-I64nN1K-bfFTVJlovxTeO_E2OUAHb75xUe0Na8vlhYL38e1swAN-yU0YNhZkGmFt2M5KWPj5FO2KRtOYBVDkUUOUGAmckyVvSU21N3POCDV7s0VX2mkaLxjJl0dbR4qdWuU-M1_yXkwfEVBjJ5IibQTT8l4hwRfOPqgBYAaCo946mv4XcqMFy3YoIfLxmnFtk6HL9-JrzWo-562PgD03d8N5XIPZk3Nkn4A3b_KTTNBFoLRCPsK_JibTia4TcRzYbvS-SE-0v0xXsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیچاره اسطوره فرگوسن با این وضعیت میاد اولدترافورد بازی تیم‌فلک‌زده کریک رو ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105118" target="_blank">📅 19:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/105117" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
حمیدرضا گرشاسبی مدیرعامل فولاد علیه استقلال: شروع‌کننده اتفاقات بازی، هواداران استقلال تهران بودند که پرچم فولاد را آتش زدند هواداران ما بعد از ورود هواداران استقلال وارد ورزشگاه شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105116" target="_blank">📅 19:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4630f9e156.mp4?token=GvFFSZtLPoVqa-EZuNFk6rQf_xPu5rfx_4GTr6SxIBSgMEV9PB4PJKfbP05SVUU7nYkJDAvD2eX4P-002GUR8AbGrZiGekb5d5OWk45ubD1w5Kg6No4VrFwEUIusyRJ6I3p1GULvXGtjQqhdDW0D1-BhZQxV0Cdhc2jWDuF7Jxm0IadIBrfqjDNI3nakPXFj26C5XkGIlfw0qgCHfhJigqCCVY1R-pALpi1KufY5pAEG0r_USg-RmeUfFRlkFifzQtmTamJwsEs_C-GY117AvwCNHKNCk6tVklMFVGcnyaKQQHriBa6Vk9PB111NTtoZhinx9pVzmStEugZNdAElNXgceVqF4Ee3HeTNtYKjRVlmcQxbfQu4Nc4J8MNbzys8Ct3xEhTCZfP8yyVJMH4qx-VWPbnE9XUueO9LhwVAg2fvXOd-75KKH4I5cUrWa6gbPCBP0csPIwVp7b-44EADsb6vNmy6ItNCxJI9JvxSAmVcq94Nqr-S6Rsway3bkYWqjHlUl8B5BRxAFAX5Wr6vVU-ZVMCFpfHAhtJiGzTMAK4DbzFNESgRTAWpyrRCjh2-kDDcQ0-pm25FCqTbOrSbJmvfau1v-dUHoHOOfITxf0hQhnE0303H8k539IobkHLI0a2NyYU9RN1mZUngCJM1gVVCPYWEHS1a-HTLZsH7pgI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4630f9e156.mp4?token=GvFFSZtLPoVqa-EZuNFk6rQf_xPu5rfx_4GTr6SxIBSgMEV9PB4PJKfbP05SVUU7nYkJDAvD2eX4P-002GUR8AbGrZiGekb5d5OWk45ubD1w5Kg6No4VrFwEUIusyRJ6I3p1GULvXGtjQqhdDW0D1-BhZQxV0Cdhc2jWDuF7Jxm0IadIBrfqjDNI3nakPXFj26C5XkGIlfw0qgCHfhJigqCCVY1R-pALpi1KufY5pAEG0r_USg-RmeUfFRlkFifzQtmTamJwsEs_C-GY117AvwCNHKNCk6tVklMFVGcnyaKQQHriBa6Vk9PB111NTtoZhinx9pVzmStEugZNdAElNXgceVqF4Ee3HeTNtYKjRVlmcQxbfQu4Nc4J8MNbzys8Ct3xEhTCZfP8yyVJMH4qx-VWPbnE9XUueO9LhwVAg2fvXOd-75KKH4I5cUrWa6gbPCBP0csPIwVp7b-44EADsb6vNmy6ItNCxJI9JvxSAmVcq94Nqr-S6Rsway3bkYWqjHlUl8B5BRxAFAX5Wr6vVU-ZVMCFpfHAhtJiGzTMAK4DbzFNESgRTAWpyrRCjh2-kDDcQ0-pm25FCqTbOrSbJmvfau1v-dUHoHOOfITxf0hQhnE0303H8k539IobkHLI0a2NyYU9RN1mZUngCJM1gVVCPYWEHS1a-HTLZsH7pgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه گل‌سوم رئال‌مادرید توسط امباپه
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/105115" target="_blank">📅 19:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlSeqWoy_ekQoZPo9sFTAWP3IHN6ZsWa7rha7fGQo5RvcY_SJgJAWhQD1xXwn2IrwB98Jf3QFUISvu_XHZGBggzht_Ru3z-FxLMol8nX6l31MvjpeQRAEnt3AM_xeY1p9tt3oB9boKmCeZYgv8s-6EIbdiM1kGoSqH1xteatkUPnYupuVJd_PPsuQ6hs7rbFOkDcA8-V-4UcKTlkKeDDAbbw0DOPersX59JRc_IWCq6f1McM0n2-tOI7TjqrRFqWpM7RIeQUZzscWcEFSpX2y5Y6-JD6WTm1nh6qpy8mfkviaNV1zkcKqOJvvSpeHRmHsKPMMywk5ptPJzp2C5VklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استر اکسپوزیتو دوست دختر امباپه تو ورزشگاهه و داره بازی رئال مادرید رو می‌بینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105114" target="_blank">📅 19:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6217fdf7.mp4?token=cqaQcVDLnyt5VtmWoblghOVTA1puIpG9KTWP8E84WLqQZHrFFqX9lCA9H6GhLxALUBvV9JFN5ZWbubwTTThRJW3UrTgFK91HZ6nFcfNMW94hIDlkfTJtAVZ7PP_1MaxlYi7un1nMQJhDVVfWQVGtyYfPHNfBU748sKvoLEvyQ8ps5cYTig2b763T2EggS8QmokFOlges5mnYFBnK5RylfywZdhiZudtpWbwk66660eAj9Uc6rC2WwDHXrHQbA1kglBIGJqshHNq3bBKFdaf7SeQMSdd0gd95OQJhRu6l9G5VJFLYeCvGw4tj5KDTfPBTVo1kFaBjPCfDuxHv6o_1n36cyLpduYTfg1CJd-v4E6joYwZ3oMH_Y_FtYGQ7X_Zcd6l_RLwKiKdES26w9CiOJH7746hGzlurotKEjyeMhoAMNwxm5ILNP0QCjda11EzH3f1TJpd6Jd07Nvk8fghLbUxhOMggyGdL0lxcDAnZtCjQSm65qe22loI4kHZTZP4pZMBT7OPmUKl-aCjIkOSlFfdd7J0U2p7hPObtVaIJFpggmpdaSjrZhK8IxtFKj-PZNV4gwWntcWt_4dtTdnyYmtD2QIMkpunLHUUD4WgDtijtLG5WZyv8SsB27V1bA4kGF640PQoqpgOgd5vRXT3pfI5Em3sYbXqjNUyAydqbvKI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6217fdf7.mp4?token=cqaQcVDLnyt5VtmWoblghOVTA1puIpG9KTWP8E84WLqQZHrFFqX9lCA9H6GhLxALUBvV9JFN5ZWbubwTTThRJW3UrTgFK91HZ6nFcfNMW94hIDlkfTJtAVZ7PP_1MaxlYi7un1nMQJhDVVfWQVGtyYfPHNfBU748sKvoLEvyQ8ps5cYTig2b763T2EggS8QmokFOlges5mnYFBnK5RylfywZdhiZudtpWbwk66660eAj9Uc6rC2WwDHXrHQbA1kglBIGJqshHNq3bBKFdaf7SeQMSdd0gd95OQJhRu6l9G5VJFLYeCvGw4tj5KDTfPBTVo1kFaBjPCfDuxHv6o_1n36cyLpduYTfg1CJd-v4E6joYwZ3oMH_Y_FtYGQ7X_Zcd6l_RLwKiKdES26w9CiOJH7746hGzlurotKEjyeMhoAMNwxm5ILNP0QCjda11EzH3f1TJpd6Jd07Nvk8fghLbUxhOMggyGdL0lxcDAnZtCjQSm65qe22loI4kHZTZP4pZMBT7OPmUKl-aCjIkOSlFfdd7J0U2p7hPObtVaIJFpggmpdaSjrZhK8IxtFKj-PZNV4gwWntcWt_4dtTdnyYmtD2QIMkpunLHUUD4WgDtijtLG5WZyv8SsB27V1bA4kGF640PQoqpgOgd5vRXT3pfI5Em3sYbXqjNUyAydqbvKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل جود بِلینگهام مقابل مالاگا
🔥
🔥
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105113" target="_blank">📅 19:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😆
-
😏
مالاگا  دقیقه ۳۰</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105112" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امباپه سومیییییییی زدددددددد
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105111" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105110" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/28e9c89379.mp4?token=mZRqzLduZONBkSP80yVVKOll64Cszr25McYC6iEGnDEE8g4xEyIgSfTXo_FaU7mXVpabX28dTNM7iF1rs0aVQNuONLgC6MWq-OU1BalDC_xN5_MdRj1pLwo5ux4ejB8p99MoJSKJWL5e71RzFcjZZ_KHOlz6gI3obFPVqmepqT88eJGQ3ZNy_nl4OvaAVH9V6DpgkKQeaUJZG0XUOHViPd96EWv8wva5kIxsgaWJMcXQuQ3KdlKj6tKbYUwr8OA9qUeN9ecm-Y4lMUDjfeaPmZY5ikvHkHpMw4guat1vaTwqiPr1CX-TusZxpT6b5RWdBmDrCfy_79bZWpzCWoqurDLXev0F9o1MYczK0mPMCClbxhN_FxNTgX9zheFOWUgHhOq0rjN1gC0bTxRcoB7mQl9wlpHbPBBmdSeezcBFVI72sqvLOqzXEhDdDHRQlYqpy-5JK5LKY6g2hoLy92E24xVqhWHprnS2j76_wsxSK4O3pFD2J8qlo621_Yn1qeuGL0AezOg_xAMlKvVyVifZZF69aWuVeTN_IlIay2IAjzeyE80q97QV35SnoMI9I1jM_E5prSXYii7awhCiCHaSQ0h0rS4S8U50OhQ61HpPbYyamNoUSjJSqw9lnjWzGaT4DfaeX0u9G0kClIZ8qw-MsLK3htKIu1pC3JU-QjrzJik" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/28e9c89379.mp4?token=mZRqzLduZONBkSP80yVVKOll64Cszr25McYC6iEGnDEE8g4xEyIgSfTXo_FaU7mXVpabX28dTNM7iF1rs0aVQNuONLgC6MWq-OU1BalDC_xN5_MdRj1pLwo5ux4ejB8p99MoJSKJWL5e71RzFcjZZ_KHOlz6gI3obFPVqmepqT88eJGQ3ZNy_nl4OvaAVH9V6DpgkKQeaUJZG0XUOHViPd96EWv8wva5kIxsgaWJMcXQuQ3KdlKj6tKbYUwr8OA9qUeN9ecm-Y4lMUDjfeaPmZY5ikvHkHpMw4guat1vaTwqiPr1CX-TusZxpT6b5RWdBmDrCfy_79bZWpzCWoqurDLXev0F9o1MYczK0mPMCClbxhN_FxNTgX9zheFOWUgHhOq0rjN1gC0bTxRcoB7mQl9wlpHbPBBmdSeezcBFVI72sqvLOqzXEhDdDHRQlYqpy-5JK5LKY6g2hoLy92E24xVqhWHprnS2j76_wsxSK4O3pFD2J8qlo621_Yn1qeuGL0AezOg_xAMlKvVyVifZZF69aWuVeTN_IlIay2IAjzeyE80q97QV35SnoMI9I1jM_E5prSXYii7awhCiCHaSQ0h0rS4S8U50OhQ61HpPbYyamNoUSjJSqw9lnjWzGaT4DfaeX0u9G0kClIZ8qw-MsLK3htKIu1pC3JU-QjrzJik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌اول رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105109" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😀
-
😏
مالاگا  دقیقه ۲۵</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/105108" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دبلللللللل بلینگهاممممممم
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/105107" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/105106" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYkMVVAXDAZCI06Bwl4hKVIgCb2zTc8lwh8h5G3fWbsK5Wc0GAjOOicnmL1rZQREwz2I71q04BJLy12N5nfNz-n1RqIEqZJMg7lJYj-ITzLkGopdrULRQKjS3nE3IUKHKJ5jtPuyyTlxwZ8ur2hyqvvyK36z9L_9GPVJ6g2Mp42oC0jFk2gAt22osdCiiTC3lPmBMsNaqeZ51GV0qlSgpBKeVQSW4fx2g5OS-6J3rW3AufCNXgS1oIfN3tQNnsJMT8HvM7nl5DD3wtcidvWkOIA6g9R7-jnraajtFTqsL72QQHteAEqk5y0x0NiCQFXNt2r0jogyA9-Z9-BNvXu5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105105" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😃
-
😏
مالاگا  دقیقه ۱۹</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/Futball180TV/105104" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بلینگهاااامممممممممم
🔥
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/105103" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگگلگلگگلگگلگلگاگاگگاگاگاگاگ</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/105102" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebsvStXTWyxIRFGq0hAWP5AaZ5yZDlFVt3hBj3sDh1mq4zkz3ZovFQaHV0DxbYPgS1LJITLmdP95z6vCxSVEOKlrVyQB9jCL8gzlxRePdWdqkxFzzP4C-eQEvRSRC3ACZdL2-iM3ejmGfg5VSZHEUE6H7xpr1CeOlKvjeOpjHRL1pe9z9VVkQr7HOwg-ukjUcF4vuYS5Dr8oR1dl0bWEsqvPYmRLzeZyLeIPl0fWMMUVVyi8yQkXgTXWgCojbrqb1Mghwjqyu32Ybukyx8V-s9ItnP_hniIoW7b6HvWgNWCj06NARoX2BdprXE8PCbtN2xth3KpMxEJVuc2fCZ5-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
مقایسه خط حمله الهلال و‌ النصر عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/105101" target="_blank">📅 18:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmeYiZaEcePnynD5WxmYNvwuSEyeifP_YhMN3wiYP-EIVfjCVo5DBSS293OgAInkm9C_3NpT3H7RfuA3NzLKeIMl7qcjeYrVio2kCLRDsW_U3elgQ9jbl7PQ4hSoy4jHO_db5SlWVlsHOGp3FVDziPBS2BVaDHXsm4iXWq1KkrNJCwxAYf7-bnZDYsd-w3CyWK1YTbxmbamcwFkOMbTqJ8bajtF4cDbCs2_fuYVTsJLB0ceVzrO9m4dLUKbSmzIm3pu74qD1jwEa5rklfPVZxz9b10e6Zbh1GmyVF5FHaoYFq3vnJ6HLwZ0l6K__yZY-oMd1mTkQqS0obAizg8o7tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/105100" target="_blank">📅 18:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی پرگل و دیدنی چلسی 4-3 برایتون با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/105099" target="_blank">📅 18:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvm51klZZ6F6eL3bh3RiridMZ1eC6Hp5GVW_fecySk8-sFoIjT0_CTXCAhpviqNfCW99pmpMdma-xNhkDyfmu8P1rKPJibXLnG2gHAg-WHbvPOIWOnqB14gTcrp1rQrZWzc6FpbuVbHD-9Ymdzv0IFihE4F5TscfVcVdFGP-Lc-d62Md_HpqxLpAEISlkuHJvIQIPAN8YOjbFyFiOo-Qhqmh2NVg9exmflPxZfKF7JVvtcdQ2gwA3TvXSV6ZFBI969Ujonct5rsHncIReuPJWev5wlOvo_Phj8e71QGFnGggtTZM_c-RtCMxEMyifRbAIyES58byB1YwoMzg2-mwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی سخت شیرین در روز رونمایی از مارتینز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😀
-
😆
برایتون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/105098" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qby75rxE93-txDD11t9_Mo_EVEi_mBMmwBscIY0_8skAo28nCkz07iG7Ic_-2CaR91L4ENtOfGeAQqZ_CTa1XhM0QkEMqj5QXHqBxKCQM4v53GRO7rGBVNzobi34csyk4LgOW99RJn8n8Kkez_LtEqCFOT6KoaEj44V6oA5ghhYOOLyakH70eHbjuqdWgWm5bIsz86zVlfWHAjl49psVSxjH7OMtpTjjHoSzkueVgM0pDbT9XehWF4saEmjz-teNMPKeBCkmZ_Ls-OgQsvMqNM2xFi-oRxIqhb7otaL4ZJO9zvK9ZAkhPVYYkMthY1v8dUg8j0IV13orSidqRo6JCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105097" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8QS_YAEyVUetTDqZ-RHnKfiOtVTS9noy2c_27xQCA8buTG_z3wt8Z4Iw1QIRrOudo5_GeDN8mLEvOfB5CFYeHMljCm7UUykN0YTXTC1NDnZ2TInTrfFE9q_GHTu_VCYRbmAz2zvktdXE1WfjPmtYhSb3xWP_fSCdtNSAD7TvUdotXFLMkcxRZ4Vc-orLWjp3jSqcbQz0wtWXjc9SoBGdiCwJBOSonX9IL6a0iZHvb_P9ATlwXqs5PmRfkB6gSqaM-MpZXNAV3QnZKR3omeWTjllysvGzjblZtfH9ToX-8J6Nruz99s68GXMs2V-97g0mf8DKXtEdI-PKKboFGzYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم‌پریمیرلیگ؛ ترکیب منچستریونایتد مقابل ایپسویچ؛ ساعت 19
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105096" target="_blank">📅 18:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9709b25451.mp4?token=qqL0CwqhYhwNUHD7BZFy6xwBuxI1saM-j2Bzwx23Ewtt31MDpKPmG6kpsfgWGDjqly3_bwP4iXplL0zWoSB8xjGdwEUeqDaN6OMeCEqaaNOcDKVamR-LJ-RUZCztcI1cQFXVwpYdX6e_hbm9CYNGdF5-iZAGQM3dapF5D0w6-xDAcPBH85GId7Ur73afFNzP8qPg-6jvTm_-9x_WhScAmVkw70au5nEqGT6qW6P9fh9WxZCJt2GS3YConI5B2fgcB7G8uiWdR_amCj1naSrpTiulT0rfzlQx5PjXr57tW-aZjnuzh5ZDkY4ux27I9zbIXudoz-YeRkaeDSzv1QjOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9709b25451.mp4?token=qqL0CwqhYhwNUHD7BZFy6xwBuxI1saM-j2Bzwx23Ewtt31MDpKPmG6kpsfgWGDjqly3_bwP4iXplL0zWoSB8xjGdwEUeqDaN6OMeCEqaaNOcDKVamR-LJ-RUZCztcI1cQFXVwpYdX6e_hbm9CYNGdF5-iZAGQM3dapF5D0w6-xDAcPBH85GId7Ur73afFNzP8qPg-6jvTm_-9x_WhScAmVkw70au5nEqGT6qW6P9fh9WxZCJt2GS3YConI5B2fgcB7G8uiWdR_amCj1naSrpTiulT0rfzlQx5PjXr57tW-aZjnuzh5ZDkY4ux27I9zbIXudoz-YeRkaeDSzv1QjOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
فوتبال خیابانی روی زمین چمن؛ هنر این روزهای تیوی‌بیفوما در ترکیب پرسپولیس
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105095" target="_blank">📅 17:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIqLSWpY2178OUkO92MrBZpk3Kz2HKALo8qf4smAHJXFJ6TumZFgheXuXAktsh0em6vQ85R_4b1_RTiOjcjEY-PfmeefV7mZzWdrRd1Bg8WcJmywKgUfek47kBaTErFpLRIe2LirotA_0W1nmkZB1BWWXewN-8nU1O9NGkrgkWkobcoMmEXpp59B47dd-J8qDSqPGARpMv6jf-a5kUY8WFC0D3P7XfKp0r_TFqTQCNaCLdSATgDLCfKCKac8YfUIFZljwe9-6J9FbdNUT9D5kYPOdfe7xsnVmsK8vGKXakyVJUeFwUCyJEI4BfBEwzMf89H4hq8YESnXUQDw0YLN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب رئال‌مادرید مقابل مالاگا؛ ساعت ۱۸:۳۰ شبکه‌سه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105094" target="_blank">📅 17:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOe4hoHMZV-f7cdfblXAI5TDwNlDwY2CvNntbZ1-bPdYa7F4j1Lw2W5Za0-x9pt4a1rrzYcVQ-VgJNc3iFtbBR8iRqHfcac8cXlpKiOXO352gMRtCAdOrVJSSeDs83DPVrXjpX3pfJUPN6w8cg4sW6j3qZzAPFPmSMPowAFpV5BFbpGQsnkpMMIKtAkD0u1VFI9Fl58T2bLC-ESQxZ460lLvzUdWE-5S9hnYXpsTebFUa0vL1ut7byBbEhnmsqvRQpDHUyyNc3A6Nr35I_BR_cR47aofGi_lBqlsfQB7KqdXakKo08qkqmSXkpDeSZxdmFwTR4tc3HSJW380Zh3K9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105093" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8czCL4qQxROqAdLlQXPAfew22vB9VhoVhYH2JpSGBmiqeblWlIH8Jv-KT9_Qfl-v9FALlVw_srMLv1mKgsJqqIElgt5IqI6eImQFQQFtcAkyYpeeM_rTlFikAo1_xzuupFh_LcgPJ0h5G5rT7wxSw-ckyDckvuoQ53IMVNFM1403tWmHrzycy158U4APpaOmJdAe_zkq9xC3uReMcuPgFuY64ZBNk1QzKbfG2AsLBtiUTXH0Vqp2l9K0pMd14ID_I3fXIu5I8UfX8H1GFCYFhnrF-b-Fpi-J56-CBUcmM_XUbs43rqJsQKPPdaIT_bsTi9B0GZott5VjjxTdNnxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
جرارد رومرو: گابریل‌ژسوس با نظر مستقیم هانسی‌فلیک در ساعات پایانی نقل‌وانتقالات جذب شده و نظر کاملا مثبتی روی این بازیکن در رختکن بارسلونا وجود داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/105092" target="_blank">📅 16:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7uuBB6Qz89WwEVTMVO_YdEts_ZxOIJBBfBBoYlNJbYIhwGQz77iXW4J0Va_By4z-x1bh-xstW-XOvSahIX0eWDHrlCMRJxJS6k-Q4bZoVBNE-bWrHN77p8Ph613pal9Aq8CyZhrHZno8VpYmegbWmUe_oXl7sDw8ctR3DQOEA-JONqOE3FJACOldxLbMnaGo1WFPA0z6Gv0bhao4-nrOHYxzzc2b3BoJpH9nU9cbC2H0G9bNoa30IWehzT9Hfs55ivYgKdPXATwjPqUASQ7itfWbZQcn0sO-drCcd2vU6ZXGKZR30VEV6x_5y3EvY-d_ICdDkYqT-s_4uIJbC3ILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
بازی‌های فوق‌العاده سخت بارساییا بعد فیفا‌دی اکتبر؛ جهنم واقعی قراره تجربه کنن
📅
۱۹ مهر - ختافه
🏟
📅
۲۲ مهر - گالاتاسرای
✈️
📅
۲۵ مهر - بتیس
✈️
📅
۲۸ مهر - پاری‌سن‌ژرمن
✈️
📅
۳ آبان - ال‌کلاسیکو
🏟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105091" target="_blank">📅 16:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CDOh7SzKXN2u32ZpsT7XYI_XW9m_KoJiw_WM3_sJj5VsAWjBH9jacZ_Q7qePFpYPz9fNdGU4hpxiR5SlKbGD-A_5p_kuLK1gtsH2Mexnqw3C4Vgx85gd7Rex1VHh1hTiOC7a02hzyOnhKC9VxKk2bUdtPlJrWNCqhOT-BIhCHX5L5NoOtizS6KrDf2UC9qL4HJBaJzI95k7JuZIeJ_H_kf8sqPIBHl8QZ4Cvy9GcxywA4-wAMKs9LLcUQep5gpMDGjN69a8L8-qnfdLYk8VzzL3HPmgg6ZrzkZq3-e-9yb5fr1SyE8CleXygn4Hg25jKy-_VE95ib9L_O_eHf2xLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CDOh7SzKXN2u32ZpsT7XYI_XW9m_KoJiw_WM3_sJj5VsAWjBH9jacZ_Q7qePFpYPz9fNdGU4hpxiR5SlKbGD-A_5p_kuLK1gtsH2Mexnqw3C4Vgx85gd7Rex1VHh1hTiOC7a02hzyOnhKC9VxKk2bUdtPlJrWNCqhOT-BIhCHX5L5NoOtizS6KrDf2UC9qL4HJBaJzI95k7JuZIeJ_H_kf8sqPIBHl8QZ4Cvy9GcxywA4-wAMKs9LLcUQep5gpMDGjN69a8L8-qnfdLYk8VzzL3HPmgg6ZrzkZq3-e-9yb5fr1SyE8CleXygn4Hg25jKy-_VE95ib9L_O_eHf2xLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌سوپرگل فوق‌العاده از مسابقات هندبال بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/105090" target="_blank">📅 16:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCfPJIErbsAOmoFcrZFU0bX3T1LRDMjOIFdFHbbfq1lh6RxiYZ3W9uXGZX2ck0n79mXcvxP9d4-Y9FDJge-5MjpsaZHpIDjEqigKQDp4s5BJ1zinrbGvlW5wb0V07S894vqESsuyclgO0AM1aB9bkQoxOvuVS-x-GBePZJBdfk847aTna-_JPVAnh_NXc2UITHz7AL4IWCpDiR1Uxx0BUo80o56hppNjZ280ThTsV9Wj5FnH_HfEFuFi9nK471S4YeEpThnHsvQ6FwndjXpxGPc89djuOTGwRTvhCXALpn7PS-xvoPjwGDkjbjmhWtsQiYSTAtk3R8ztTHknCDEm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🥶
مقایسه عملکرد وینیسیوس و رافینیا از آغاز فصل 2024/25 تاکنون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105089" target="_blank">📅 16:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=Z-wp71T22Aa1UWYJjfIUl0aqrK_88lXzgUKGBbOeLYqdwmNNlgk5BqAKuFqgVmsmoa7YlUVWCW6xAl7qpsuhmnD2S4_DswRuyGWgYgU5-_2O5SRQZ_sXFDLtMQNrKXjkiuCeeaZVjBZkuJ0kKM0z5DshdCT1BgWlLXo4tuArK9drq0hsS71zfvAZgG7cOoEleyB11NYSx9Sw2gucIhXxXodSdx0Ylx35Ik6xCdm792czq7u8yup-p_lBurgUZTSj1pdg-5Oexr6AdY8XvmNT3_x2aZJ7zJ7BSByr70IWs-yS2U4TDFhlm5CSw1tlWCE0mLFnpwVT8PPogqIhthxOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=Z-wp71T22Aa1UWYJjfIUl0aqrK_88lXzgUKGBbOeLYqdwmNNlgk5BqAKuFqgVmsmoa7YlUVWCW6xAl7qpsuhmnD2S4_DswRuyGWgYgU5-_2O5SRQZ_sXFDLtMQNrKXjkiuCeeaZVjBZkuJ0kKM0z5DshdCT1BgWlLXo4tuArK9drq0hsS71zfvAZgG7cOoEleyB11NYSx9Sw2gucIhXxXodSdx0Ylx35Ik6xCdm792czq7u8yup-p_lBurgUZTSj1pdg-5Oexr6AdY8XvmNT3_x2aZJ7zJ7BSByr70IWs-yS2U4TDFhlm5CSw1tlWCE0mLFnpwVT8PPogqIhthxOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تیکه‌های فوق‌سمی مهران مدیری در سریال مرد سه‌هزار چهره به عباس‌عراقچی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105088" target="_blank">📅 15:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=KcVjt9EaSLACYtfhyFE60LN20_qnfs8OUjNIrOQtJWaOP27FkG4wTDnBVj03DFj8r9U1JfjmLMo9IPhft-fwavhvr0grZpVMU2-KdnU4Nnk4y3Ww69CmlWAK_16WAd1SYcIbno-AqtCmp9YgwFUStngFOJ4p9diR0Kr1N2thQaH89jeu-9f3HmVCFEeVSVQLjRsa_SVCwi32C0AcFk61CjSb0ehgkWRInkvMWovjQNwHXRPMOO3Dn7JlBl8y8PE8AksvRB4kW-zmByhSqCnJjTi1jIq5zpJgpFMc4KGFk1x54vkzg6Q3sq_HmD0HvH_gI7W9kpKYm4ZVxRWd784W1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=KcVjt9EaSLACYtfhyFE60LN20_qnfs8OUjNIrOQtJWaOP27FkG4wTDnBVj03DFj8r9U1JfjmLMo9IPhft-fwavhvr0grZpVMU2-KdnU4Nnk4y3Ww69CmlWAK_16WAd1SYcIbno-AqtCmp9YgwFUStngFOJ4p9diR0Kr1N2thQaH89jeu-9f3HmVCFEeVSVQLjRsa_SVCwi32C0AcFk61CjSb0ehgkWRInkvMWovjQNwHXRPMOO3Dn7JlBl8y8PE8AksvRB4kW-zmByhSqCnJjTi1jIq5zpJgpFMc4KGFk1x54vkzg6Q3sq_HmD0HvH_gI7W9kpKYm4ZVxRWd784W1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها ۲۲ گل تا رسیدن کریستیانو رونالدوی افسانه‌ای به هزارمین گل دوران حرفه‌ایش باقی مونده.
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105087" target="_blank">📅 15:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY_6cfVGG-sHCv7d2CP8v6NQc3b7nTqG4qew_tkaTbe9FuOwu1CLQGHI1ELQDgWFx_uUvhnIt4KaZ3DjvDsmf2rVM8Uzki1xxcAfuiYx-zcvjcrIRUjACkeM6WZl4LrWNqNeYLh2KEQy9Sp0cfnvb_eFFDfnQCC8FQI1Qs3L53tozs5jEh-Lv1VIIcuCK-X7lUC8Ot6E1-eHufoM7gY4zD9fnlYnFyFVcvrP5UMkjokP-gGn3NHkKkbHsAxBBrbYOpg_ks6UPVOCoE3c_hxIbWP3MnQKH5fEUfAZBArMR4zFcEAXf9zgmXr_OL6J8XLaFMTHHy6VX9KkxI4gNmyjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بلایی که دیروز آلیسون بکر سر تابلو تعویض داور چهارم بازی لیورپول آورد بخاطر اینکه داور کسمشنگ تعویض تیمشو دیر انجام داده بود و در نهایت همین اتفاق باعث گل‌‌خوردن لیورپول شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105086" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=djcRywZBoV2zTv3DKlev3Ex9ULE_fRnKIlORVG5cIbCOY2GO9741ruyIUyv9X4CBg-C3xeFew-sTdAINWly5Y_vTjNT-7gRv7hprXCXvKC68aMUbWwIN3vLzh36YgEhUxfr9dhvz8pZkd1IchNJK4TOp6Hix93J-ofjlEj6m7QgCEvdcxF60S6ffIolXKOGNLV1ZV-V1pkOz40vxkGKT5IkGeydt_g4Y7sll_kU3cec0oBslECKe-kkS7UZRf0E4oCvrj9AVxkGWBEzj8oIp3Mxo29EAFhVWUCI5QY3TGDoWvd-lLdzvoy6sxC4lFEfZew9YT3yeCQ3PK2vftq-Wxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=djcRywZBoV2zTv3DKlev3Ex9ULE_fRnKIlORVG5cIbCOY2GO9741ruyIUyv9X4CBg-C3xeFew-sTdAINWly5Y_vTjNT-7gRv7hprXCXvKC68aMUbWwIN3vLzh36YgEhUxfr9dhvz8pZkd1IchNJK4TOp6Hix93J-ofjlEj6m7QgCEvdcxF60S6ffIolXKOGNLV1ZV-V1pkOz40vxkGKT5IkGeydt_g4Y7sll_kU3cec0oBslECKe-kkS7UZRf0E4oCvrj9AVxkGWBEzj8oIp3Mxo29EAFhVWUCI5QY3TGDoWvd-lLdzvoy6sxC4lFEfZew9YT3yeCQ3PK2vftq-Wxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان دعوای عجیب‌و غریب خداداد عزیزی با رسول مجیدی روی آنتن زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105085" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=E-GyjMxuRmvAHlZOLUnHBIXFpSMc_-NbQuqxUzaW8DQKyO-Ae8mVVXmGfUnT0KwBU59N3Bx91s4DSPLTRA_EGo_24TwJY8xIoZw-6xCap7yX-iK2enfdQ7FmV04tNssIpajUnoekIlwSrlWH7R8kC_ZE7K0FvX-9NrSllHnEnCoX3zsya97HUxuKumB_uNbkVmAl5b2kM3HeZ4B3X0GC9wayKoJEFtfu-1m2TfTR-M4LWoeQogbMzIJ8gHMkIbyKi2tFkj449S5YIajvFTej8xywqIIKfknwOp9ANz1TSARtEX_ZNptKnSZfwxo1HJLW2kP1yXwZT8wOiufl4O2oug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=E-GyjMxuRmvAHlZOLUnHBIXFpSMc_-NbQuqxUzaW8DQKyO-Ae8mVVXmGfUnT0KwBU59N3Bx91s4DSPLTRA_EGo_24TwJY8xIoZw-6xCap7yX-iK2enfdQ7FmV04tNssIpajUnoekIlwSrlWH7R8kC_ZE7K0FvX-9NrSllHnEnCoX3zsya97HUxuKumB_uNbkVmAl5b2kM3HeZ4B3X0GC9wayKoJEFtfu-1m2TfTR-M4LWoeQogbMzIJ8gHMkIbyKi2tFkj449S5YIajvFTej8xywqIIKfknwOp9ANz1TSARtEX_ZNptKnSZfwxo1HJLW2kP1yXwZT8wOiufl4O2oug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
🇪🇺
وضعیت روانی رئالیا بعد از قرعه‌کشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105084" target="_blank">📅 14:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLMb8BtxMoeC2apumZO6fA-b-8jRXlkY4mMF6B-lW8EJ0DofvVAucTikrNeVuycJmreCBwWOY7xNOX-fhz97GOeePs_GbBoiUcGFzTyicq-UUeRrWuQUkAAHajc1RbhG7_mqgBw9XvgyktTij9dGKzNRTtLbhAqHJ_vuhwxPVJsRsuOMQ8HIAEsQJlF_410mQUAiqS859ozJYldgn0xS9_E_BMjTs77Q54GL3iEyDEy7jqtqZSedFkUkSZCXlP1x7aLawBiRT9VNIIWWbpmuE2OMFaGsTucPuzYqiIpDVrFN44vCDzMd1LBDlh0XGv1cN6aeUua_wSg1jmRM4_nDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
✅
🇮🇷
هوادار بانوی فولاد در بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105083" target="_blank">📅 13:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzPKYWfozbqWJHe0Xe-eZGy2EBJc1QTuEmrl8aCpHCUNI0QqYwSoJQCLXh4lN0x3sqTtl0IipcfNhCGRmZ2Af0WjPeNlTlPF9dPZAp6F08P5me6L3IeWXBGr84FhbsVVnqYxhmfO0adAYpnf9Sy7uZawfQo5_09w-mJGfwYaQtsuoyb-Hl1--4wiZ75WNrbulh6j0GpWbKiN5JicjTh8jNO82_m3Yy4liWCfVQBXu6ic2d7NtIm07dGelq2NRRDA2eMqzoyZbkcENh_pzT8HpcYiB9ewYDyrn3oxGmscjLUlrx_mZJkyKW3hU1wETFPHcZQICKkvDFZzvkEen5ZgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
🇪🇸
مبارک اتلتیکویی‌ها؛ آلوارز به تمرینات گروهی تیمش برگشت و بارسا و این حرفا سرش گِرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105082" target="_blank">📅 13:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYtq4njhJiXMnwtINMLlWUYeVpoRYNG9jeTqTJLAyy6tCGlB3NSopCrVZdm4SRBtRdQG19fwX1JxWp13IoFyCYUDFubNImKVnNrSXlVYGWr4p1McSageB77RpnZgxZ3W8voQHWBIJ3FWgCmzni81F51fuftNTCuaXZ7X_FYTz28vTfYbr74R2jPOBwmLty0ZdeoNcqMBvNaObL0gaJhMt6e_OwsgpNfTGSkoGW74vwDz2gLGOokUw9_mxFhTm9WXfoXMAzjjNM1Eo9hcnOUq-jBr0gnwHj3tmhr3JEDtH1lYxHN6w10Jzs0x_MNyNLuqrPxqD8oJ-gPN4Sdn2_IFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgp535ubgnz_CDkCKr53KRdioFRvhBIkfsDOjG_-FozNSI7kYCgMvXtxdAi2BoN3Ltdqn8W0vZL1E5mxR2RzYgPwNkt3ECdtBhFWOg1aCNPo1drQRvi6tBkbG0dlqFPKilTB7NdfoA4wIND-DXvKl_2jQHG-95l0aEAOzbAMW7RZJ-utY0waXIiA1yzIleqEOG9PZyzeu4bJ2DfbKeMXUzWuXP452SoRhARKT5mkTgFTGsfQgXiKFjUUpDy1_zLun_VGa35Z5ThCSGARe9Do1uSCiMhXcZq0m1x9LT9E0MS3j3_Os-Mcea5iF7oV4lkfUTyQlAbyeayrsCM72bNH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFWXfSJx26fVF2PyscmYkb85SrsSF_iyspkda7RjE3TOtbRy_-C8AITWR8qK71qy5nE2Gq4dwNBbYA97aZIejwCd2d2-XSGXQc_P1YrI1hv60WQ-E6yl8gc1InLnC8R23v9YQAll0c5JutwYCN8bhrh-puDQ5vIUbXdenlo-MC6bmdrlXh6COuUYKd-ywhyT7v6rA8HyyB3qZTy9zCkS1ZtLSxLNOK9jc9y74S3vco27Y8lxestwCNLQ5SU8vnleoVAdKDz4loOJgq_yRG_1l_C5k0K6egJoWVOdq_ygtNxnN0TfFtaD5qhz4W_rFe05WX9sAnRu7fvzOWOFkerA2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
بساط ممد مورایس برای تولد ۲۹ سالگی شیدا مقصودلو همسر ایرانی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105079" target="_blank">📅 13:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=vPSQDODAmLXWY8nJvkvreVksInJPok74gdN8tWqGKuNdJ3rjINCk8kqO6Tjv67vqJILKfyii8o0u8p_J0-lbAIy6lCtPsxP4csvFsUyneM6pnE2LGksHzcxCwIQdSREqOX-gWs5TqVDlY65V9L6JyN_uzlcl3mex-7PSbdDw2J8A0hKf7OrbdC_aTzJGRmccgxAYUklu20BDoA4MkF4GM-GiVFsTs-REViQroOKUR3GWxAAdK5HlPBMMdRJ39ZMBW8OQQCGRbKQydJ5JGwffOJmhxCZ0xcCZBLajuVklqGlsiYBFIJr0olEC7A6piq1Znh5U-AOvIorX36sv60yhXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=vPSQDODAmLXWY8nJvkvreVksInJPok74gdN8tWqGKuNdJ3rjINCk8kqO6Tjv67vqJILKfyii8o0u8p_J0-lbAIy6lCtPsxP4csvFsUyneM6pnE2LGksHzcxCwIQdSREqOX-gWs5TqVDlY65V9L6JyN_uzlcl3mex-7PSbdDw2J8A0hKf7OrbdC_aTzJGRmccgxAYUklu20BDoA4MkF4GM-GiVFsTs-REViQroOKUR3GWxAAdK5HlPBMMdRJ39ZMBW8OQQCGRbKQydJ5JGwffOJmhxCZ0xcCZBLajuVklqGlsiYBFIJr0olEC7A6piq1Znh5U-AOvIorX36sv60yhXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
امین کریمیان معاون فرهنگی و ارتباطات باشگاه سپاهان: اگر در دربی به امکانات نقش‌جهان آسیب برسد، از استقلال و پرسپولیس غرامت میگیریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105078" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105077" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=WZ0eL2R3glKl8a2mkF6iGUOz38-9whI5sclqQLHoPJevDEhKpDWTVqgiC0YNO8_Pnw0zeD0BqgHWHAbIFF_ebpdDxNr6TudH6pDW22rJD8u0TwuUbSyl36ImfHN6Gq7azcxLE7KWSAwc_0q47cREopumA0x4b1wCYI-yjLtO9XJsVxy4azp1kJb9hXOR-i1TeBZxu4EAmbKtokdLAJ-inSCb5o0Efu8sjar8wmjtqE7a_Wdu8xIxUXzBfpOIk1alUhxPH14k-L_qpQ5jF0VdKJ8goxsyT2CznkzJLKElrtSOjwd2jnvzNDAlYR99iyYXqH1TtYgtCTQp4LNJlSlVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=WZ0eL2R3glKl8a2mkF6iGUOz38-9whI5sclqQLHoPJevDEhKpDWTVqgiC0YNO8_Pnw0zeD0BqgHWHAbIFF_ebpdDxNr6TudH6pDW22rJD8u0TwuUbSyl36ImfHN6Gq7azcxLE7KWSAwc_0q47cREopumA0x4b1wCYI-yjLtO9XJsVxy4azp1kJb9hXOR-i1TeBZxu4EAmbKtokdLAJ-inSCb5o0Efu8sjar8wmjtqE7a_Wdu8xIxUXzBfpOIk1alUhxPH14k-L_qpQ5jF0VdKJ8goxsyT2CznkzJLKElrtSOjwd2jnvzNDAlYR99iyYXqH1TtYgtCTQp4LNJlSlVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پروژه تبلیغاتی فوق‌کسشر و خطرناک روز گذشته در آفریقای جنوبی که نزدیک بود دوتا هواپیما به سقف ورزشگاهی برخورد کنن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105076" target="_blank">📅 12:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=qx5PKs4paR3Q9oGAnI1C_Bw0RiWwqWPvAdeym7vP00NWAgclOdzLjEerg8GB5_Cm2vFRJxbkUoMatHzbsFClTzvWayjxgfXDt7wuewfNkUW2Ko0UDFhC05mFdMo3ZKfB6C1dooSvj6i-CoXrYSifBRNVG-IDUKbtLdMbTujN60887CwUV0w7pPzQfYqPLa8HKJuHeOF-P8GRNjYTzNKSxuzR6YSN0Y--UXsN4Fx_-XyQEKXucHanpv3HCRvWo-L1OgVg8fobIV5ilCWM2AGYuCED-YnO_Sl3iGw1bqKIAhxu97WRVa_5Z9qBXGul5zNRskpiY3RWIw-sxWDM-dCSjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=qx5PKs4paR3Q9oGAnI1C_Bw0RiWwqWPvAdeym7vP00NWAgclOdzLjEerg8GB5_Cm2vFRJxbkUoMatHzbsFClTzvWayjxgfXDt7wuewfNkUW2Ko0UDFhC05mFdMo3ZKfB6C1dooSvj6i-CoXrYSifBRNVG-IDUKbtLdMbTujN60887CwUV0w7pPzQfYqPLa8HKJuHeOF-P8GRNjYTzNKSxuzR6YSN0Y--UXsN4Fx_-XyQEKXucHanpv3HCRvWo-L1OgVg8fobIV5ilCWM2AGYuCED-YnO_Sl3iGw1bqKIAhxu97WRVa_5Z9qBXGul5zNRskpiY3RWIw-sxWDM-dCSjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔴
یه خانم مُسِن پرسپولیسی : من پرسپولیسی ام الان 55 سالمه و از شش سالگی فوتبال نگاه کردم یعنی کم کمش 49 ساله که پرسپولیسی‌ام
‼️
🇮🇷
دختر کناریش که استقلالیه: خاله تا حالا قهرمانی آسیا هم دیدی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105075" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrWlOcT4xm52_eZfFsWIwz99h3eh3Kmkcatb1r1Z15qKP8qQsiR1FbOBLOkmAgoFdN-jT7bY-SH_IPv4-ZfHQyY2z-KbWr5yoLsdKrXzXf6a_-TV5KlPl4226XsWEkDRyfgxnTyMXaCATfwPr2E81LjjbtCur4S4Iyse6L3cfMC_OPPKsw27KP3jsA8TwAlBPTwXsGwRZKjquqkVUGWkAXV2wxIj2QNpzyaUavIdXN-krFEW4S-19R2Ghd4oG3U5uLo_31u-WzNUvjcX3rv1YI0vKafbg0z69k0ZfR6Sgm3Tn4_mbkN9Ic9dnY77GXMqzpNsaDqh8uYPp-gtldXYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105074" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105073">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105073" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105072">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qir6XKQ0gAYGibzwhvBKyqA4-a4sX36Sd-mAbOMzCRWvXG9tHzZIXjK7O46033Ja1t01-InTAkYvY2GbKzKpJOlDljCJb1qHga6qNoy5zCbyn3wEAnIAZgZwDcov4mNj5Ag5GO17i6tZO3Da8io8hgQaDevmh1Z-Xcp9fYMVpQ3NFHAg_xMguTvG-pvV-v0OZbmBYIH3w6Q0MCQPNADNjB5-gbjC8i2UwinSWHJURcvWNF_VAzazs7v2-FozZZUMoRRLyuNvlBKLf-nm60dFoimTPEhbtpqTC2Zcxpzj7BuTk7bpFhtGFtBweivgOBeKKsHHFGaUdNHeueRK2YgYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105072" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105071">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv_cVkbaF4igK3JFlTUqw26Dw_p5ruJJ6IKel8Qe37eFflFelPrnPTj1W72SOqISLSbvqc3FAWeyepItxZGnGEDgQqkT86juyMya2NN3coijnTjNj7hCkYp93hs8Cv4s0ANsEiqSQckRBeyRLu93JT3zL8dXrSe9FmCJJbGsdQOWN6RjzBpGShZrmlNspKby1AQrXF-jLIxHMkvBWNaRHNB8VngtNSIur5fP0IJdmoVAEDH8oDX4_fYLP1iX7_PuRgf4e5O5OvgfafFqA9Vjtyy4v2MXfwH9s9uQIf30bik_7jlB5nIsjaT4T4VUJty7G7qgzYLYlii2kBf4lKJtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
#رسمییییی
؛ املیانو مارتینز سنگربان تیم‌ملی آرژانتین با قراردادی دوساله به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105071" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105070">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHl0twv_CnpwQJFhNBMLvulvoZYIcatcqZHDQvGeYx3n8hnxwppbCrc4ZV85ypOwvaze6utAODVGt1QF9gUQesm43KK-E86rPJLeIMPAYv6V9ONBpU9WbuDrOhWqrmFvofdU_G3YQddmquqovyHRm4kayPtika8c-hjuu0ZLVTNVg4KtRWriZFPSyhKajMM_QdTZl5LjxqGl6Yq7BwAVCem9DlED4iyqaP8J9SWUwSAEdNJUFvd1YwGr_RezZbQSoFQZUtwMFWAhGGNAWR43qv6vP06LBvu81V9OapVA87RjyyBfqkkFs9VsJPKJHK3JOEW7JTXPwaBKjTH63EvAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
🇪🇸
🇦🇿
بارسلونا در آخرین بازی لیگ‌قهرمانان خودش باید مسافت بیش از ۴ هزار کیلومتری برای سفر به آذربایجان طی کنه. چیزی حدود ۵ ساعت پرواز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105070" target="_blank">📅 11:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105069">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=lzLHv9XhHOm8p6QIENDB2BEoEpcuH9ALateEo6KLb9_WxVEeEHMR5BHzRci795WL_MklHEQQkfnMzHZlbcs873NSViQpiziRRMeBhAj34Lsy_qUNWwqjfWL0cwqhou2KNRYYgMMdzVvFpkUgIuGM_YycoB1Evbkzx2_FKM6c53aR2HMTlqBmEi97DreTy_31MvBY4PUmm1LHVWqG6iRYGpg2lIT8MI_qnyIz22M9As0hfs4IFLk5Ie21jjpyr2pUNx0N_Q9tg29e8kg-NxpLCFxhwBl4uBKi-3zkJQwgwKDGqoxlM3XEozwQJ3QgJM0NFJlFEkTE9GWkRvmf41rIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=lzLHv9XhHOm8p6QIENDB2BEoEpcuH9ALateEo6KLb9_WxVEeEHMR5BHzRci795WL_MklHEQQkfnMzHZlbcs873NSViQpiziRRMeBhAj34Lsy_qUNWwqjfWL0cwqhou2KNRYYgMMdzVvFpkUgIuGM_YycoB1Evbkzx2_FKM6c53aR2HMTlqBmEi97DreTy_31MvBY4PUmm1LHVWqG6iRYGpg2lIT8MI_qnyIz22M9As0hfs4IFLk5Ie21jjpyr2pUNx0N_Q9tg29e8kg-NxpLCFxhwBl4uBKi-3zkJQwgwKDGqoxlM3XEozwQJ3QgJM0NFJlFEkTE9GWkRvmf41rIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
دیشب خدا دوستان‌فانتزی‌باز لیگ‌برتر رو خیلی دوست داشت که کیری بازی این جیمی‌جامپ عزیز باعث گل‌خوردن پیام‌نیازمند نشد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105069" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105068">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=ickY0OVzNp3UbMA41k4H60pk9nht3ZLvUYPUIxPlA7Y9TJO-HYuCmxYtBuVpzVTHJE0kVsUDBVzXbmD0L7BRo-BXfAuGT2z5KJKRSkw6H_t27yeQSrMHtSHV5vO2mSgTtQCPesPEt74hTc2zMnNu8lfVpWK-97Y3KzDFi3DoXrBj5FP-idCvFOBBAXoM4WCTJCFji8KcDGWiu_6ZZOxpN2ZwYWSvMo4c-5RmnySCql20Jx608bc27YVam2JYZZAKtBCBATcYavJSFkbvf0yDFnsl31gVPMIIBbdJflF6FUylBgzuKZUCUYd0Y-bSrhCayR3YQfec8jkW1C-SfUGX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=ickY0OVzNp3UbMA41k4H60pk9nht3ZLvUYPUIxPlA7Y9TJO-HYuCmxYtBuVpzVTHJE0kVsUDBVzXbmD0L7BRo-BXfAuGT2z5KJKRSkw6H_t27yeQSrMHtSHV5vO2mSgTtQCPesPEt74hTc2zMnNu8lfVpWK-97Y3KzDFi3DoXrBj5FP-idCvFOBBAXoM4WCTJCFji8KcDGWiu_6ZZOxpN2ZwYWSvMo4c-5RmnySCql20Jx608bc27YVam2JYZZAKtBCBATcYavJSFkbvf0yDFnsl31gVPMIIBbdJflF6FUylBgzuKZUCUYd0Y-bSrhCayR3YQfec8jkW1C-SfUGX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
این یوتیوبر استرالیایی میره سراغ مردم عادی و بهشون پیشنهاد میده در ازای ۲۰۰ دلار براش غذا بپزن. دیروز اتفاقی میره سراغ یک خانم ایرانی که قبول می‌کنه و ادامه ماجرا ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105068" target="_blank">📅 11:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105067">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=H_REJe5bFb1o3c53WcGlF_zhPM8qZiw3b9pT8d2l4VMQ7ZQJparxlaOEsNIyHXnaS44fJioaTqZELn0qiPY3oGv3M3WHzZDA0z8EmfZ3RNCHs09frPrVt5VeV2pL2Mmoezl5FdknWijWyY_AjMm3IrxmkbZ7TsWJ-LTNZALqTQzuVpIMbtOHvps_d1weTxfe6s8OKnK25eIjuOLRvidw-rY_J34xwMlDFrPFptEb8lWX_BiVdOiQsFpSuV2S9OTxzPrHTgaz4kjasZgRepmmCQXo66EUKIm65ImY43peotrSQJ2gNmOBCcaDjmbMFRnrVflLO1UcFERIRZ7YOru5Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=H_REJe5bFb1o3c53WcGlF_zhPM8qZiw3b9pT8d2l4VMQ7ZQJparxlaOEsNIyHXnaS44fJioaTqZELn0qiPY3oGv3M3WHzZDA0z8EmfZ3RNCHs09frPrVt5VeV2pL2Mmoezl5FdknWijWyY_AjMm3IrxmkbZ7TsWJ-LTNZALqTQzuVpIMbtOHvps_d1weTxfe6s8OKnK25eIjuOLRvidw-rY_J34xwMlDFrPFptEb8lWX_BiVdOiQsFpSuV2S9OTxzPrHTgaz4kjasZgRepmmCQXo66EUKIm65ImY43peotrSQJ2gNmOBCcaDjmbMFRnrVflLO1UcFERIRZ7YOru5Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
پست سمی تیم‌ذلیل آلاوس که بعد سه هفته و با یه بازی بیشتر صدرنشین لالیگا شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105067" target="_blank">📅 10:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105066">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr3ofq9U3lQdq01hq0g7i_qk9Sr78uwZV2xIS80YqVbzf4-_mcDJs2aFhekfWY5EYMD1WnEVzIRl2MBaddfCsh6K41npU_jpAFzKQa7Yf7tbmztmZAXxlmeqXdnswLEy6DCgKXnmzKIL0RVwTihRVtPBcEpwrqK_qvkqK_ZFTsS0uGhX81A37jhK5lroBS8zblxiWonxVWmXRUKNBy-9X1XAqvWngFPKY0AtcvbzEXte6SgG5mKXFKT4g05-M9UuuGKuDH0tve1V9yFpBRZDJ3Pfxw2jh24w3irfW5KNKXGI7s35sppe1OlCfN0-VK5HY0EQ6jTodrFJ_D01Guqp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105066" target="_blank">📅 10:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105065">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=tIOlwX5ZQ19XoGPTkcNpZ2U7tXzjSKrYq_CW8d7Rbo8tGgzSZ_hvMafQqoQyN41fi11-ySKnEb2IeaDGCfY2Igq0Yx2rJvDzRncdoeNOv6UzXVulth8BagGAUe4uvvmNUCaOrhMeR9Wiab-Shcq7giqfk7nkePAaImvedoC4wI-D7VWIXB1w5Kw-NFo-AMTYQ61uTroz0kKHIhwNb4nXyesSwP73Se-EkE5i1l4SRm8ElSPJjeYCsTMAsRuqiBQktvLcThmNMTLuNQpKqSHl0LsSQ6ZKgwnMY8-BszrO9Q3yltB9z3VvbZNX7xkjcFxGmTw2ocXqkDXLyP3GJAfxPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=tIOlwX5ZQ19XoGPTkcNpZ2U7tXzjSKrYq_CW8d7Rbo8tGgzSZ_hvMafQqoQyN41fi11-ySKnEb2IeaDGCfY2Igq0Yx2rJvDzRncdoeNOv6UzXVulth8BagGAUe4uvvmNUCaOrhMeR9Wiab-Shcq7giqfk7nkePAaImvedoC4wI-D7VWIXB1w5Kw-NFo-AMTYQ61uTroz0kKHIhwNb4nXyesSwP73Se-EkE5i1l4SRm8ElSPJjeYCsTMAsRuqiBQktvLcThmNMTLuNQpKqSHl0LsSQ6ZKgwnMY8-BszrO9Q3yltB9z3VvbZNX7xkjcFxGmTw2ocXqkDXLyP3GJAfxPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105065" target="_blank">📅 10:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=MrmELqFc0RxVKgA5h3ZaqM-z7u_5c8YnEzbp6RL3RA1om_H76Mx5KQmvYVmKnhcTGhhZUyw5nCAQAMPbPwQSKbX_LZf8u7NXaz5RY-Te4oJR0EWruLXHpwcgRo13ZldGjxPlWadiXNo2Fu5rkKhuBk49CGbKqYvU3i6AN0gfyGm0B0SA14ATdS4psiXAHSm7CaN_LmMxxl1Yifmcn8u54khB5inLYY2i6aRoaWl633Ld6OL2BowVfBTSB-np6THrmyB8NM6lHJh89qwTXzRImMoKh_mUhg7Zdq05ZxfCUkSXz_G7k3TXDhgWeyPAvw9blMJslfqHnbxcKHpHgYip_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=MrmELqFc0RxVKgA5h3ZaqM-z7u_5c8YnEzbp6RL3RA1om_H76Mx5KQmvYVmKnhcTGhhZUyw5nCAQAMPbPwQSKbX_LZf8u7NXaz5RY-Te4oJR0EWruLXHpwcgRo13ZldGjxPlWadiXNo2Fu5rkKhuBk49CGbKqYvU3i6AN0gfyGm0B0SA14ATdS4psiXAHSm7CaN_LmMxxl1Yifmcn8u54khB5inLYY2i6aRoaWl633Ld6OL2BowVfBTSB-np6THrmyB8NM6lHJh89qwTXzRImMoKh_mUhg7Zdq05ZxfCUkSXz_G7k3TXDhgWeyPAvw9blMJslfqHnbxcKHpHgYip_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
فرونشست فوق‌کیری دیروز در اصفهان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105064" target="_blank">📅 09:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105063">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=R9bH1a0YnrifdI0gV71v2FfycpKhpsgw5uGz5Fqn6Q348AT_IYABTP4S5UfP0Q8c4_H4XBKz7qb43S5X3aaoY47uwUB3NHVbtIS6CmvOQ8jmNMpBCi3i31C1IZBVKyIOYH5tGcGMDDntg7ThrFcrPxMZudSFL8ZcLYZEDg3OofhW_jELnKKL65Thic7Nv31z0RC4y_J5u9ZaOw8FVZVCqhV3CwCv3NY5BLDYDX0c3mK1Tmw1fYOUrq0km5taBk_EbyFYVmgT1-JxlNIb3H8qtVD2wg-IECYPfc_-fjNK38qpOP2_6fWMfvAMwhab0DbjIbcnW7rMOliDFIByIgG3Soi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=R9bH1a0YnrifdI0gV71v2FfycpKhpsgw5uGz5Fqn6Q348AT_IYABTP4S5UfP0Q8c4_H4XBKz7qb43S5X3aaoY47uwUB3NHVbtIS6CmvOQ8jmNMpBCi3i31C1IZBVKyIOYH5tGcGMDDntg7ThrFcrPxMZudSFL8ZcLYZEDg3OofhW_jELnKKL65Thic7Nv31z0RC4y_J5u9ZaOw8FVZVCqhV3CwCv3NY5BLDYDX0c3mK1Tmw1fYOUrq0km5taBk_EbyFYVmgT1-JxlNIb3H8qtVD2wg-IECYPfc_-fjNK38qpOP2_6fWMfvAMwhab0DbjIbcnW7rMOliDFIByIgG3Soi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
ویدیو جدید از استقبال پشم‌ریزون رافائل لیائو در قلب ترکیه و توسط گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105063" target="_blank">📅 09:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105059">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srYqGxqGz9O-9Y2pAYG6h69xEJPWCwLTg3vUxgoi27T0f6c_GIzQ4eOjmSLBbu5tDVANKJxeejNxBJgNLY6QWID-vebhVqdXB8WFUDvEI5vwLGI6RbGMjKl7TdRqJnoYCSEPJQbuOck9p68gl70W30muc_i81dG-KM7L98PxXDKI4s9m2NcYMZoA1a9RW7lf6-GRVo_fxWyjovPlDd3EZwpMphMrbBRRagEMel6kGhBpSnM9vbqVMMS-LzSP0oR6sYCFE2BWy4zscutDaepFoZQtfL3WaIuNVHBthJj3B8ADjJ209N3zUa3m1cs0Enss-U5uUYhwc3QiOyBnG2iTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRUgbl3t6Nn7GzBGAPR_-l8QZtTVER2F2azO2D-x60G2hwmtNrvF_-_-d4yClVytbIWSgNP8iBAu5TA7_qxpe0ATpvMfq03xuPaoHbU0zjTS8ZpHUzCc02P6VIeitZiGhdL1HXsR5xeIE1xPSAFGLJT48GmdhbalIOfAom2VENyyY39Cyj0cB1it0138MR4f6PaxaG-3H_3F_01kRlCd0hsupxOwG_WislZ-ER3gtDIL8sa6ogvjOW9PTnj9aR3iGctZ6IOyfS23UZrFsBzjQbjdLrF928U4QOJlSZqtTWxPqKSsqBGY_s3wLRFVUEk_mdDDm0FfRdr-eW2B_TRstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARmkU_ImXXU5syv_zSIZ6Q_yWBKz1a5LcCNpgLMkm9ziZM4xTtSYtPhAj-wVAPpLfPr2WI9JTirq9SkpLodxZaEhne3nbnHgEjNC9rekdR0K0SJ0LRei1TlvNfufvTEjlZov3diOCvfNEsJmo3KHNcTbUiJnLJjkdio4rEHSNecMWk4QQHPv9Z3ApmeO658RBMQU6TD-eIJ2vm6fKnwWpFK9KtBIkh8NQRFSLSkuEheczu8hrvvWSnyFxRtK0CRNZKKStnSty7LOZSs4D0sdBwvB9rj17FBAJQS7l8M7-JvhBfY49EtQV3axQlxM1f7A8832T1xD71h65A9VixWNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCDfNEYKVFykm0UunNU1Hi2ka0-hd77YNUfck0c38Cj1M-mkOXjy5J6lVRQce5PYd95CskzupQYcbGZOYzRufQKfu_tVfYEKfoYvvuo8iGmKhFh0yF7ZcMn4ZbOHpw34Xfg_117LwgIbzKg9jxfeng-o36MoE9vxf86skGC3ViNR4HtBivdkP0S7sj1MqE-BzDWU-e1MgZ7O68YGCJnjdX0qAIefTA3FpiA3KSk2JwONXivi0qqihRrmVKp5Ub1ek0jIQIPWHbDc1G-h7ByXEvSs-ZQOBb_c6ZhOJO3xhIXWeGEXEWT7dv7XXZ4URUQrGRglAmJY1IiG9RbIimM-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
بانوان جذاب پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105059" target="_blank">📅 09:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105058">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=OeEp2ZjQP-ySVOn88kEbmElMFboHRGgsV6wjvnSy08Z1nTWzra10TGKIGMxwWo5JcxYhRBD15fZUCav7tEPH-SXZInFS_mYO-mQ_oaAstrwvUrGS1FogNU-RzQQTPRIqyyW_GfyjB3Zb5cD1C4onN0zUvIIat_Kq3CJFFaZ1rrnjLslE1x6kKrjDiTstWla0CU8IxTUWoNhVVmZpbRCzu40DAVCgS8Z8Cc2-q3EIaD-yvBZTFWSAhpr98wq0QuhT2YCXsQZVV2bld_VeDBLLk1yyVdmiXdXwRy0ZZv6cI80agIleO2P1L0Mz6A68MnzUJLcXDcchVJYA91tIheNjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=OeEp2ZjQP-ySVOn88kEbmElMFboHRGgsV6wjvnSy08Z1nTWzra10TGKIGMxwWo5JcxYhRBD15fZUCav7tEPH-SXZInFS_mYO-mQ_oaAstrwvUrGS1FogNU-RzQQTPRIqyyW_GfyjB3Zb5cD1C4onN0zUvIIat_Kq3CJFFaZ1rrnjLslE1x6kKrjDiTstWla0CU8IxTUWoNhVVmZpbRCzu40DAVCgS8Z8Cc2-q3EIaD-yvBZTFWSAhpr98wq0QuhT2YCXsQZVV2bld_VeDBLLk1yyVdmiXdXwRy0ZZv6cI80agIleO2P1L0Mz6A68MnzUJLcXDcchVJYA91tIheNjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
در جریان پیروزی 1_7 اینتر میامی مقابل مونترال، لیونل مسی موفق شد چهار بار گلزنی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105058" target="_blank">📅 08:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105057">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-9JlfUAb8ZcJwBJebMVQvhOf5qu_i5Nd_Rk4U6f5Zo2beSutXfsdtoZ9i61Y6ncLp9N8JDTrg9PjJz19NpGjrdvkNTQs3-PxzGZrdB6kA-Q6EDwQkmDE0c2kVSLNi8J6O5M2-1Hw8VDPNCuRzwf7CNuJPaPJ5Lcgl4hwPmOpcvklTN2LqIqwnAzClHf24PTGAAZ-EBYegc1fzOwfIHn01b_qG5go5WhRfFZRvkIxYXH4yzO-L9i_DkcEERq8CBB5vMoOGT95ABh4-cCFTcCRzuLMw_mzDGr_nlvhoIqYh5f0s54c_NK8Cd_rgxTwqEeZN2A0zTMDD6xkBjFPwCw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105057" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105056">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105056" target="_blank">📅 01:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105055">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uObChr4iQvlDfUzQavOEKK_KWD4EYmitwn05AdmRsUhlykNER_IzI1u1BZcMv923j2tHjTbbzlPk1yWIyUHW_7WZtFC3VIHFJrd9V8BpfdvPKJD9Wwc1RUm0rx2s_Nd-_YImLeslyc19Q_sGHmOGdq4p1ge6jhNqgQAjQ4mVB05UJUJIikJ_GwwTw3eNB1SY7_liueTu5TMzsyMRtqmAjCz7HPNFKfhSr8WXan35k2ChngdULJ7kMUa_4yjuR5VwVHSco0Ducm33imwNskTOYBkmi_KLhpJ9tSxtz3Qeek4vQd7YO2u9Wm-LUrX6Q7JjjSORNdLwAasAYWWZ8jMcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
متئو مورتو: اینتر تا این لحظه با جدایی دی‌مارکو به مقصد بارسلونا موافقت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105055" target="_blank">📅 01:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105054">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_sKV2G7GEuF40C4a6eUvQ0PIDq4LUxJZPDBg4-9xA6TDIXyGehrNUyJ4BNEJL7IpXG8Eu1uIY9MMcciqWZO1ljuGUUUwc5LZXYQTgPpJOocdrOuo8bA7DWDkBO8MF97TxwxZSns-bOoq-cTgTSBGY0vlsknI3UGLAFWa_EEuXIfCuNypGWrIv7tFjbueJqOvhKERhZGX6Xgy9qQq_Np28fOpaHnymaLLlfAaHq11CtM6dv5zzjPICpaHxN51axW_-NNMX7Yta5pWMrMBFer7AuaoRlZuIO7XbZQQgd071jU96QnVhY_J62kN9vRt2YGqgRsAufQExp1igpN2KFkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
سردار آزمون با انتشار یک استوری به صورت غیرمستقیم از دعوت شدن به تیم‌ملی برای فیفادی خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105054" target="_blank">📅 01:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105053">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2azAUBQPbdKpEgt1X7Uq_GDsu_6l6s1muixFRCMX8sixxh8DyhJas-IhF2XSWmrJBkt-VDKgmld0nfq-bI-qTNoz2yu3e9T22byJf41VvyrQxhy70BDP-7wIblO1Me_b79UgUILvjn3Tekk7n4bULyMGm8yaF13UJML2rL1I-wCfhGqdqnPfrTtIc5In0SOs7_Jk4MSw_QJPQM8huGIVstrHU0GzQLb4ehw4Mj_94DXZ3Lul-O9_AD0Zeye1A4tqEADGZGXlG1kYMpP1stzyXdVVo9kV4cDOh8NoIbAv1M6lYpa27kVpre2P82P--o4HptImM-RLd3iOTNJOjjREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105053" target="_blank">📅 00:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105052">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiRq3Bki8V4hnzAII2KO4z1sGavzKCalKNNeBTOwPlCYPU15zdL_Bm1p4yO6sb-zfibHDPY9s9VDWP_IFBoZeTS44dKMuUX8C1kzRIIAAQ16ShbT8EwQ09NY_bTmJ1u3PQa-h1HDwa11r7z0bNvkOV4yZxLtfLJSiaMS8x2jxZzJ3f8VIfj6GC_FpNFKJp7_8P4yCg3b3Ts530j7QnR2QZxG2HC9gSdRBRtxv_bk8C1OXjZU-dYILMOEWoEjnnZsk69tWqgZc7zJoUwDyH3TsFv6k_KFbmcxd96UNEYNUy8sfMOKFM5tKL9cOebhDhY-JpfdBa57NhFfo6djZIAklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105052" target="_blank">📅 00:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105051">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH2fCJmtRxl_a_TIn6DNc2oONSc-mqixsSNU_XPngCw9B4yofh2oAhsjRjt6Nw4nFYXwoSygotMLckV18K9p52-1j0mTIoIoG3dHwxwXu8mGNQJ0PzHvCcUX2CImEBwX7vTVrtipUWz06BiwQzQ66ZBTc_gI_g4gI6rm7E98DBKCDDbs3cSooRUCYnrgTwZzcMKlAjh-S5keTklTtb9QtzTmqQv1bFnUvlXasuiCPu6qKRgE_nxoJpLLx11yBLsspt5xVHXDx4gE-bKz5DuQ26-akWHtEG-qeaMf8euwPUQL5eJDlKgjEnNIXuEPKCkngYfqJWM1GwbcKc72hE2GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه تایمز: منچسترسیتی تقریبا با لیورپول برای جذب کودی گاکپو به توافق نهایی رسیده و احتمالا امشب یا فردا خبر رسمی منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105051" target="_blank">📅 00:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105050">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsLJIVBeP9eGFHQGxDISwwt4frz_jAiKR57_KU-7oOpg8kzJyF8rlOp9CSYWp37EnlYZoKZdygdF6r6ev8dlqPHBLZ39inHGdjCPUqqYreQucOhKzTBYU5SqYJCbtZ4ya3neQ315ME9BSPVUl6ieN4YvOOfyJifUYwnQpL-JxP3RoeK-R2jQaedNN7V_7jQPix8xtKB0J61IXakIPOs_eSJyraFRk_RatOA6lR5u_ikfHwnYX9Kim5Czp1YvM5tTqOQXa9Y9g3xqOM940NFlhlSitFoQV-0l87LVHYLhl-EODiM_6JMVz5ReH6N0BLf4Q9_Dihegy14hkphbv5F-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال راهی برای جدایی اوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105050" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105049">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22168159c1.mp4?token=hGTjtW_aIjNGEKjiZUi4AIcwrUkCGX3tNNATmV2WDdBhvrt0wnRCZjZSKVABgIGaM99tHydrbw7U3POS5FCNXdr96zyzZZSumnnhDqAaPtMH2jU8j1cXf5mWJs8Av9bVW9aOabDi63sWdrIHen6_5TYe11RCU8zzDPYzSNpi7n3idao2eFc1C3bgERdSZQHUPUswRvoAmnBw0SsfB7c8sfs74vFxLID4848XdWuSN9jKOFIfFV76O9fonbrGpS52LgnZz8Xjsqd3xa-2m5V2_aceg5wKD1YtPzGZWz1Wr0QAkbXHrsgtFeIrCZo53AZuHj5Ena08mnPuNO5_WW9Htw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22168159c1.mp4?token=hGTjtW_aIjNGEKjiZUi4AIcwrUkCGX3tNNATmV2WDdBhvrt0wnRCZjZSKVABgIGaM99tHydrbw7U3POS5FCNXdr96zyzZZSumnnhDqAaPtMH2jU8j1cXf5mWJs8Av9bVW9aOabDi63sWdrIHen6_5TYe11RCU8zzDPYzSNpi7n3idao2eFc1C3bgERdSZQHUPUswRvoAmnBw0SsfB7c8sfs74vFxLID4848XdWuSN9jKOFIfFV76O9fonbrGpS52LgnZz8Xjsqd3xa-2m5V2_aceg5wKD1YtPzGZWz1Wr0QAkbXHrsgtFeIrCZo53AZuHj5Ena08mnPuNO5_WW9Htw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇹🇷
استقبال پشم‌ریزون از رافائل لیائو خرید جدید تیم گالاتاسرای در استانبول!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105049" target="_blank">📅 23:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105048">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128d699010.mp4?token=fh4CdayyQWetd6X3WOaxLtuk2HulW-oJANuNk8CcM3gK7I6gnru7XMj0D81kLczxdALVBoc7fx0BnCFT6kDHE-U1s3QkgsXXC17NplHnBwID1V_wotj0-neOhQJVIw4EatAXHr9uj_PwD1aMWOP7tM0MZUFWNP3lIPj6Jipx6HdJf_JIm9EbOEsK7Iqiq-5olVMSANNg7R1Ekpi1LknWetPlXq2zxycZJYi-u3uWqJrGQfagdeRVzZHzJwIthY1IiroVJ5pqdtrcX4ndCgfOJImfOJhAapKKl9h5VOrzlzuW10FqiXxw4kmldITn4xuwAugpxwFRe1GY7BGn9uW0Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128d699010.mp4?token=fh4CdayyQWetd6X3WOaxLtuk2HulW-oJANuNk8CcM3gK7I6gnru7XMj0D81kLczxdALVBoc7fx0BnCFT6kDHE-U1s3QkgsXXC17NplHnBwID1V_wotj0-neOhQJVIw4EatAXHr9uj_PwD1aMWOP7tM0MZUFWNP3lIPj6Jipx6HdJf_JIm9EbOEsK7Iqiq-5olVMSANNg7R1Ekpi1LknWetPlXq2zxycZJYi-u3uWqJrGQfagdeRVzZHzJwIthY1IiroVJ5pqdtrcX4ndCgfOJImfOJhAapKKl9h5VOrzlzuW10FqiXxw4kmldITn4xuwAugpxwFRe1GY7BGn9uW0Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
❤️
کریم باقری خطاب به هواداران پرسپولیس: موضوع ارونوف را به کادرفنی واگذار کنید. پرسپولیس بزرگتر از هر بازیکنی است؛ فقط تیم را تشویق کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105048" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105047">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=j6Dci78I3a7kEIfnoyvULIX2HYVuFcripiit6aMrPmH2dThWXFHIFt-QJNoqybHUR1FK5H4vi69EgLjDXQIvwKH7dRJmVYIF_zQCSs7tOIcVM1oyS1O2sj-i8qOyZbJXp5dM6AeB1Nftn-jOzR0Ezk9zGCFEpb36mRhetwwrzq1rXnH2ear1G5gNfhNSNamJuv74B7lmdErtqy4KTZHLa0agqO7b6Dv6dUmjFM4nt9CpnOMYG-NRNGk6vFAjtwldOFYa1o9CLTqk-HsgS3jXFoQR26FB1bYgsmbD9utLpWy6U38bUM4eRNCBErTwCqiamDC1mQIK4L0mBMF_1I-ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=j6Dci78I3a7kEIfnoyvULIX2HYVuFcripiit6aMrPmH2dThWXFHIFt-QJNoqybHUR1FK5H4vi69EgLjDXQIvwKH7dRJmVYIF_zQCSs7tOIcVM1oyS1O2sj-i8qOyZbJXp5dM6AeB1Nftn-jOzR0Ezk9zGCFEpb36mRhetwwrzq1rXnH2ear1G5gNfhNSNamJuv74B7lmdErtqy4KTZHLa0agqO7b6Dv6dUmjFM4nt9CpnOMYG-NRNGk6vFAjtwldOFYa1o9CLTqk-HsgS3jXFoQR26FB1bYgsmbD9utLpWy6U38bUM4eRNCBErTwCqiamDC1mQIK4L0mBMF_1I-ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❤️
کریم باقری: دعوای بین باشگاه‌ها و تیم امید؟ زور هرکی بیشتر باشد همان می‌شود. اگر قرار است قانون اجرا شود باید لیگ را تعطیل کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105047" target="_blank">📅 22:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105046">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrvlWLDSHWujZ_UAUWjI-xAcmnYvnUm0x5sIxXOltggvMvyasXDL5ky6lb4NwY7j8OaOYO7nGW3amGhti5IlTaHcl1nw7n53q2j65p0wjpO9W6wXaLo764U1PoNgXUkiveWsRx7-r0e47iwok-Erx9jQmEtMkwDc2hfdffTBph14Kq-Rq3C9O8bGH5WIU6POzBlQ8xcbacqaWEqMfwH_a2uiY139d68WsTz0x1nd58-7UgyUJc4RGwh61T4Pa90Wmq6YQ8M5P2Zwd-oJMI6bGUCXkK-6FoIM74eFpuIZOvP0CP3F4uPOy_JIwT662cpWWMHmE_eYUfqKkNZo_sf_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس بدلیل شادی زیاد و افت فشار نتوانست در کنفرانس خبری بعد از بازی با ملوان شرکت کند و کریم‌باقری حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/105046" target="_blank">📅 22:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105045">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=P4V_68PLN1sfENjk9NMMwUsgGD6CC94oCU1dwRl2gj5FClq0oCQoIjfbcMxdxNIW9ufGN0Y_KKTwqJvKR3qzPCXVIDx-EXQHtPNuhNl_jCGy69s7oP9ee8t6Jik2hGAO3vcaSGQCATJeBlh42_HA-hAhHJd7EQcZtRvggQ-LwM-UZ6E9l2aRPfiGHHSKD8VDNy3D5TliYdvDkDRr6IX-5RoCuX8iSf01o_qgZ3HGGyK6s5Ssy4tPXfa4mElDJQFYp1qDQIbIpJNcYrFMyCl48oD8c649a6fP42gSo6mcu1DlNWHapoyWbsRhx2O4TBbY_T_KTSfMSR4rv7EPjB_Xk3XNWgQ7dLBhVqiWXO4L-XyG4X7nFPIHtjAPfClsmJJeEXVUMFPqUbyD1P8JH57uDkUxo92vSnj1djnJoIGMNDHnMfsqotgk02tbf1dKVNp_hlNoQzuBF6pVOPsQuL3N3VqoA0LiH-0uVEgmJ9UVyvr30j-80-waSVG3W3-31QI83vIZ4F74fhjtx7ZE4E96JgASU8X_xIyjPTXRK88rwvGCTsyXv0qInIX7l7xq7nOBk3a7ZjtX4FVROkGN6DQ7AbvTi-RRry0bOFwxWeCjJ80TBSpZJLuWL4XAqNdTpH2M65VYGaEeTDMaCRdPE-AAgfuCwzrfzFv9dQanxSfXoCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=P4V_68PLN1sfENjk9NMMwUsgGD6CC94oCU1dwRl2gj5FClq0oCQoIjfbcMxdxNIW9ufGN0Y_KKTwqJvKR3qzPCXVIDx-EXQHtPNuhNl_jCGy69s7oP9ee8t6Jik2hGAO3vcaSGQCATJeBlh42_HA-hAhHJd7EQcZtRvggQ-LwM-UZ6E9l2aRPfiGHHSKD8VDNy3D5TliYdvDkDRr6IX-5RoCuX8iSf01o_qgZ3HGGyK6s5Ssy4tPXfa4mElDJQFYp1qDQIbIpJNcYrFMyCl48oD8c649a6fP42gSo6mcu1DlNWHapoyWbsRhx2O4TBbY_T_KTSfMSR4rv7EPjB_Xk3XNWgQ7dLBhVqiWXO4L-XyG4X7nFPIHtjAPfClsmJJeEXVUMFPqUbyD1P8JH57uDkUxo92vSnj1djnJoIGMNDHnMfsqotgk02tbf1dKVNp_hlNoQzuBF6pVOPsQuL3N3VqoA0LiH-0uVEgmJ9UVyvr30j-80-waSVG3W3-31QI83vIZ4F74fhjtx7ZE4E96JgASU8X_xIyjPTXRK88rwvGCTsyXv0qInIX7l7xq7nOBk3a7ZjtX4FVROkGN6DQ7AbvTi-RRry0bOFwxWeCjJ80TBSpZJLuWL4XAqNdTpH2M65VYGaEeTDMaCRdPE-AAgfuCwzrfzFv9dQanxSfXoCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
تیکدری: دربی 3 امتیاز دارد. فقط به برد در آن بازی فکر می کنیم. تیم ما آنقدر بازیکن دارد که با بازی های کم فاصله فشار زیادی وارد نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105045" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105044">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=dx4G2Fr7mo8XXQKfd_t1jtnktkIbh6iEBUe-ewNZy1ny3E1-H6TiZcYRrCHrxvkDgzwY3JOn0qryY5G3p2CyXxni31ZM_5HsNDGHcZIXq-ZFAevbv6V9x16-MqlzAPIqQnKZSDykZ7UMNXO-lzSDNCPEZl6XBm7bzTbwsy7Kcp88kvZTrT_xogh11AlID79GFScy7_VlfeaILQo0Tfopzl_Mq9PM-SN6Lv9b2psn2rO9ZIfRgjakfuOj6gn0MaGHntn63qENvrML6alOKPdP6B2zFvXWnZ1eqMOAxo-haxGm2bKfPz9H7WD9drSZ34kskHT1YkAfbl_fiv-iEDWLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=dx4G2Fr7mo8XXQKfd_t1jtnktkIbh6iEBUe-ewNZy1ny3E1-H6TiZcYRrCHrxvkDgzwY3JOn0qryY5G3p2CyXxni31ZM_5HsNDGHcZIXq-ZFAevbv6V9x16-MqlzAPIqQnKZSDykZ7UMNXO-lzSDNCPEZl6XBm7bzTbwsy7Kcp88kvZTrT_xogh11AlID79GFScy7_VlfeaILQo0Tfopzl_Mq9PM-SN6Lv9b2psn2rO9ZIfRgjakfuOj6gn0MaGHntn63qENvrML6alOKPdP6B2zFvXWnZ1eqMOAxo-haxGm2bKfPz9H7WD9drSZ34kskHT1YkAfbl_fiv-iEDWLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه فوق‌العاده شدید مازیار زارع به خبرنگار برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105044" target="_blank">📅 21:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105043">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7GS27pTSs4pg9tpNDaRVjpp4fEJqPwdlBiRw3Y59Yi0F7jEDQeWIeold0jlJ2TcVuRC752NIJclret_7O4mEcPzxs9AZZZUj1_ybURKHAc1Ua_X_jwGI4qwOySbRf9yo6_5RCmjdQaG6XMNAS8AR-IVEO9bUzpWyY6ywl5hBAF2Td905jE4auGmc5DinvbIv6OB1B9UfB9CIEDZetZ7AN1nv_YlVaWvXviv3k7apC51SON_uUCsFXfYDIPP_OWnNGchEBblYusvwasEuFbw1iMkYiOP1TDFffhnzZv59k9i5z4MmtV7pRWC21wIMwM07sT_AbhuZmihp8tSM2TVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105043" target="_blank">📅 21:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105042">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=GHYtQ2bEQDKWKJjMLGuo9ooD3qovmPj6xYqCh1n_aoONlerrcFalP1abfj_7P6NaooXSaBiscuWT_7-GJp6fg4gaVAdKtcOqoxCgzUlM4XzVjDgCewWi8ZaCrKwDrrnEBn2l6b71z53JTunUW54DTOEjXNYPuFJBOqHfVREmxw2DBZEPOQsssSIpFNm5ksPzGvKtF67D6lRM6dv2NQWSOWZDGxUMw80YZTauZeJ36M5Sw8WQwhUHNhB9plvtX9ln9Uni4B9CDFRYMSEDCOm1xmjidPyTkyNBD21aq5iIYohlqlUYp8S5Acm0sOnSR4VvaHvd9Q_JXdf5WhzfuLz1CBgUv-wQ_1WPXZjt82VYa6y8gwS7UE-Zzx9V7RvLYU4pO7V5emmo6x9VdIrrHCdnN5fVnSLIIZSWd9HmLgWZaKbL3IBC5QW6uwHWYQGi2dar4G1pZ4L1yprSA_6TAmh076KXixeDsuDzzfJW310fgWKnb13XgJG-4t1-sVnthXAuvcwJ7wUp7N0ZRvVAqPUxo_PLH823DVYZcfR4gZoYD6M-iHU185tpiUKGgecpAlzrZnUhOLda7j1FO3Nw72SIBhEopXWx5qKLmFd0NTEbsrIVpAFb7mkgMaalVf6uCUbkInOsolZw2fSdWRJRrXH3nt0xE7fD18gmDWegbA20bZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=GHYtQ2bEQDKWKJjMLGuo9ooD3qovmPj6xYqCh1n_aoONlerrcFalP1abfj_7P6NaooXSaBiscuWT_7-GJp6fg4gaVAdKtcOqoxCgzUlM4XzVjDgCewWi8ZaCrKwDrrnEBn2l6b71z53JTunUW54DTOEjXNYPuFJBOqHfVREmxw2DBZEPOQsssSIpFNm5ksPzGvKtF67D6lRM6dv2NQWSOWZDGxUMw80YZTauZeJ36M5Sw8WQwhUHNhB9plvtX9ln9Uni4B9CDFRYMSEDCOm1xmjidPyTkyNBD21aq5iIYohlqlUYp8S5Acm0sOnSR4VvaHvd9Q_JXdf5WhzfuLz1CBgUv-wQ_1WPXZjt82VYa6y8gwS7UE-Zzx9V7RvLYU4pO7V5emmo6x9VdIrrHCdnN5fVnSLIIZSWd9HmLgWZaKbL3IBC5QW6uwHWYQGi2dar4G1pZ4L1yprSA_6TAmh076KXixeDsuDzzfJW310fgWKnb13XgJG-4t1-sVnthXAuvcwJ7wUp7N0ZRvVAqPUxo_PLH823DVYZcfR4gZoYD6M-iHU185tpiUKGgecpAlzrZnUhOLda7j1FO3Nw72SIBhEopXWx5qKLmFd0NTEbsrIVpAFb7mkgMaalVf6uCUbkInOsolZw2fSdWRJRrXH3nt0xE7fD18gmDWegbA20bZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نبود توالت در استادیوم مس‌شهربابک که معضل هواداران این‌تیم شده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105042" target="_blank">📅 21:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105041">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=o8TVQp8PEI52koHw4lU24TldhsuP3-TEHl-bCbUniOwBYMmYu44euNh8CnRi_mYhqMLj2E0p2mwm6hraZMMZRZpAuDP2K3p6bksXYRv0jEWcUYub95h3FZ5gEIO_KeSwr68iV0MvqTyFTqJ6ZOS1RNDemUmVnUqAWqk25CUK1Qicy8QQYGJ2fKwc-e-mtst8EZ-94XTNJ5QkTUAhs6kCJwx119cPBWwYJhlvxcDrQZ45Fn0DpUYODfknaDIA1-2rhF9hGusAnacNJe671Q0yj8bNAf8hsS1dy1kzqI5zNCIhKSrn4uMKNxKcyZI3XPdO3ZDQPCt5sOS_JgalqrZuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=o8TVQp8PEI52koHw4lU24TldhsuP3-TEHl-bCbUniOwBYMmYu44euNh8CnRi_mYhqMLj2E0p2mwm6hraZMMZRZpAuDP2K3p6bksXYRv0jEWcUYub95h3FZ5gEIO_KeSwr68iV0MvqTyFTqJ6ZOS1RNDemUmVnUqAWqk25CUK1Qicy8QQYGJ2fKwc-e-mtst8EZ-94XTNJ5QkTUAhs6kCJwx119cPBWwYJhlvxcDrQZ45Fn0DpUYODfknaDIA1-2rhF9hGusAnacNJe671Q0yj8bNAf8hsS1dy1kzqI5zNCIhKSrn4uMKNxKcyZI3XPdO3ZDQPCt5sOS_JgalqrZuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
ابوالفضل جلالی:‌ حضورم در دربی؟ هنوز هیچ چیز مشخص نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105041" target="_blank">📅 21:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105040">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=eLRlJIQOaYq3sKt8P3b9mqdpDajywdONR91_lH1x3I8Lis58ieMtD5gNPElPnIBG75-Gg0a6Og8fRU7eMPb_B-k4BntAnu-Dzd2-wFT_qscyNRUiqupU3QLJ54iNhnbSbBymS5pQHa-w1GeHEWfmOmHW3brRSnqF7jiNc2xzHDiI5V0Ms3loolGLh9P89zpf6RFoQN9DlxGtuzXhiMgk3OJph0tjyTHNaRuetQ3UEKSNApyZdXHKkc2EeFhcW9fKo9UVn7fKxp5t-3STyPhr_OxC4itjxicrfemLxSbVGysALQZLjP3iuJGAw4MU0yXbw_rpSfcnncq6ecEWwIGiyGmXE9bTlbQrCCFYYAHSJoyK9M0M_aRsOj2zavg0zCDj8JrbU5yb8GMGtN0XSmqSGm60BZtO4c70DGC6Iup6v4IA8r1-P3QFFWgkIXbw-xdjrCSE4BZKEjhSRLOAv3OaNxwMjckLt0vdSzxmd5RyspCvFgPGrAoyPQT9as7oiK3kywOB2SniOQw2yODKIqbj6GHUFflwwB3WKx8gtIyvXp692SgMnKeD3u0_Syl8v_u9Z8g4BL3Oa7Lp4gAxY3BDNTDAf6dZQbunYeftkiRLAhfp7dI2D65cwB74rX_4vAxYHxa4Kgk5Tq2f0zpBMwNIA0JKjGsHSx6zOIH9cDgcYA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=eLRlJIQOaYq3sKt8P3b9mqdpDajywdONR91_lH1x3I8Lis58ieMtD5gNPElPnIBG75-Gg0a6Og8fRU7eMPb_B-k4BntAnu-Dzd2-wFT_qscyNRUiqupU3QLJ54iNhnbSbBymS5pQHa-w1GeHEWfmOmHW3brRSnqF7jiNc2xzHDiI5V0Ms3loolGLh9P89zpf6RFoQN9DlxGtuzXhiMgk3OJph0tjyTHNaRuetQ3UEKSNApyZdXHKkc2EeFhcW9fKo9UVn7fKxp5t-3STyPhr_OxC4itjxicrfemLxSbVGysALQZLjP3iuJGAw4MU0yXbw_rpSfcnncq6ecEWwIGiyGmXE9bTlbQrCCFYYAHSJoyK9M0M_aRsOj2zavg0zCDj8JrbU5yb8GMGtN0XSmqSGm60BZtO4c70DGC6Iup6v4IA8r1-P3QFFWgkIXbw-xdjrCSE4BZKEjhSRLOAv3OaNxwMjckLt0vdSzxmd5RyspCvFgPGrAoyPQT9as7oiK3kywOB2SniOQw2yODKIqbj6GHUFflwwB3WKx8gtIyvXp692SgMnKeD3u0_Syl8v_u9Z8g4BL3Oa7Lp4gAxY3BDNTDAf6dZQbunYeftkiRLAhfp7dI2D65cwB74rX_4vAxYHxa4Kgk5Tq2f0zpBMwNIA0JKjGsHSx6zOIH9cDgcYA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
مصاحبه سمی با هوادار پرسپولیس قبل از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105040" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105039">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkeDClr5Cg4fLlOjvdlyR-BOzeoX-CMedmrMi8MzHMciScUD6uPMwRtAyru3qvItp12Osepg-MNPwfOLh_bASEgqzc8UgniDw1lCNTedtBs4TluklOPBPuDtjL3jYJWfCF9-kc0cg1fzIIxiAJa5gf3VypxJf_Xxl-99TY_k4aV3uSO4rjFzOTbaIfwZUWHq3RkvNBpqiBNg_P_Nq-VsIcll1NI09kA4CRcnPOIlPYU0Y6hzAycVbeB0-OJTTmm8Dcosvn3XugN7UT9-szVXex4TqJm8eeVoxOFTZg3-RN0RVCDPpilBSpsDt0aCb8CcrxlUHhHLBpDkaYFfDyhvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
هفته‌چهارم لیگ‌برتر فوتبال؛ یک نمایش روان و دیدنی در شهرقدس؛ بیفوما همچنان درخشان است؛ تارتار با پاسخ به منتقدان به استقبال دربی رفت
🇮🇷
پرسپولیس
😆
-
😏
ملوان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105039" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105038">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vug2zL0Y5OyqqDolxAIhOhOtj3nOzwT7qEs1XFzbXt-SCAzk8QpFJ6-HGK_iUgd_fYfE-aEwn1pRJGO82Ay0sNPjtS8YIR39dayZN65FiCqOSrD29LqzpTVH_BtRHBBSNlQyzuOkP1jEcdJaspq5_RVlBKSksAWbbI6c0lRuzRwpJenUEntmaXGtpMA_oHt4Ho5Rzg_WG8jtXe8q5rrOItCn3Wuu8Of-WNjqaWCDWNTCmSToRAdF0VyzmLGqyWurp7mQ_asshpQKIQoui312JAwZmYoVFLMoitadS6YHHjUhHNh27lKs9cbSs2fjUYrAmWi97lzE64HXt4aF1vKtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
هفته‌چهارم لیگ‌برتر فوتبال؛ یک نمایش روان و دیدنی در شهرقدس؛ بیفوما همچنان درخشان است؛ تارتار با پاسخ به منتقدان به استقبال دربی رفت
🇮🇷
پرسپولیس
😆
-
😏
ملوان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105038" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105037">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
پایان‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105037" target="_blank">📅 21:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFpIXkor1fIi8vA45tI5OJpZFrzolc8M3_VZEzGo9ZhlNPf-5IeVb-Gzun65myu3GqFDz5LWV5qBpNi1nd7jsaQ-WCsdmycVqBSf0RjJsQiTMPL3pJbRLD8kK0NQ4--Q6vJL6O08jnJHDQdBUVF-67c8eJWIUZxOwH9lAO_qdHZy_mQKq0exbCjQ5ayNG61XiviaA73DpCum8mkQyZPx5mOTjAXVbuM0Ei_vGC_lLK1E5uDjZ6ZZZwYzbmwA3B-TQF84UryiPwU4joWCziNPYJ-MxQdsS3d7cO1MxyyW_W73Sd6T4pWluzlKvMUvWTiW1RWMLrB--PO6dMWIkqWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پایان
‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105036" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🟥
بازیکن ملوان از زمین اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105035" target="_blank">📅 20:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105034">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=gLM8NbjwVKpkQF7OzywXCRD-oqVwWtJTXx1mGE-xj-hIv4VmcXRp0OPxH-Kne2pgh1bVv9DTq5TTkXDk3ILVmFcV9dHG7bLwVX406TnZ99T8lD_ZGQHqvDqOSksqgX6XX5dGHXTjXhw61l3oqXTGzoSWaRMy1FqtUULJdymyOHxWLN25CaEbxv3zB4f3l95k_yZAN1mQlPmN_uE8-V4VATRGXb-FSv37VCpbZzGukRlwfFIgggiR2hF11W6oUlQ-u3u8E19RMA4gV6oU2uhmABxwZF1WkYjHGo-UbtBqnvWs6gcW44C4LnTqDx8bfwUPgiNHYlZxpmUi_QdR8o5FPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=gLM8NbjwVKpkQF7OzywXCRD-oqVwWtJTXx1mGE-xj-hIv4VmcXRp0OPxH-Kne2pgh1bVv9DTq5TTkXDk3ILVmFcV9dHG7bLwVX406TnZ99T8lD_ZGQHqvDqOSksqgX6XX5dGHXTjXhw61l3oqXTGzoSWaRMy1FqtUULJdymyOHxWLN25CaEbxv3zB4f3l95k_yZAN1mQlPmN_uE8-V4VATRGXb-FSv37VCpbZzGukRlwfFIgggiR2hF11W6oUlQ-u3u8E19RMA4gV6oU2uhmABxwZF1WkYjHGo-UbtBqnvWs6gcW44C4LnTqDx8bfwUPgiNHYlZxpmUi_QdR8o5FPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مازیار زارع کارد بهش بزنی خونش در نمیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105034" target="_blank">📅 20:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105033">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=bpfEIKHsJu2-gKtrHaVYhGGkc0feRcehf7_HKDaPWHjlK8VUMW409B5yjadKAlV7rO3zK0_1hoWgaq6HmY-WvbtqRPq5AQPgXbXDer4wHoDSxqfSh_zfuy8agHxxKiZgvTUr_9gK5BvaATUf3Ly9ySbTdO2zOTcuHOnp8YdBQo9UVZe6LKLNipKFUxCMOkfhuJDg46BPMWMtaY6-MtzwszXTd7PIqNbvEMv_HxFW-zW2OMOiG1y9f2Qm1NNpbbEQHAIY6nL9TEcapGe-82DYP-ugaeA-kncA0-oRofczkkZNIl8bA3tHBELwdt4ozMXzAObjZgaZkb4jykHaIJFeq1V2URw9EbKhjdBtFP1dZZyF1pn7x_7OPwLsAQQ6uyYouMos2jfNgBqteuJX0a13a-euESv_dWEipxD--5nIH2yni6m8HRE4AV6GizWFab62Q58KIA9EDZnZbUVcJIpvd739HlIYGo8ndcyL65NRQBCb3k-c1i85LOAamRbVHu7hRERWWhRMO8kf-Scx0etlfJ32qfcXChnvwNbSapkC6OPmYpFWLOkbhJcSKeWrkNX_QFuF4PHehiWdMTYzzpR9t8TDa8rsZYPZokK4QPDnv3RhiHvN5ENXuJv5veFdsM2Ry_WJ8G0WcU0WL3wEBWGQtcItaUWyzo6vZgowD24MriQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=bpfEIKHsJu2-gKtrHaVYhGGkc0feRcehf7_HKDaPWHjlK8VUMW409B5yjadKAlV7rO3zK0_1hoWgaq6HmY-WvbtqRPq5AQPgXbXDer4wHoDSxqfSh_zfuy8agHxxKiZgvTUr_9gK5BvaATUf3Ly9ySbTdO2zOTcuHOnp8YdBQo9UVZe6LKLNipKFUxCMOkfhuJDg46BPMWMtaY6-MtzwszXTd7PIqNbvEMv_HxFW-zW2OMOiG1y9f2Qm1NNpbbEQHAIY6nL9TEcapGe-82DYP-ugaeA-kncA0-oRofczkkZNIl8bA3tHBELwdt4ozMXzAObjZgaZkb4jykHaIJFeq1V2URw9EbKhjdBtFP1dZZyF1pn7x_7OPwLsAQQ6uyYouMos2jfNgBqteuJX0a13a-euESv_dWEipxD--5nIH2yni6m8HRE4AV6GizWFab62Q58KIA9EDZnZbUVcJIpvd739HlIYGo8ndcyL65NRQBCb3k-c1i85LOAamRbVHu7hRERWWhRMO8kf-Scx0etlfJ32qfcXChnvwNbSapkC6OPmYpFWLOkbhJcSKeWrkNX_QFuF4PHehiWdMTYzzpR9t8TDa8rsZYPZokK4QPDnv3RhiHvN5ENXuJv5veFdsM2Ry_WJ8G0WcU0WL3wEBWGQtcItaUWyzo6vZgowD24MriQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل سوم پرسپولیس به ملوان توسط علیپور(56)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105033" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105032">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=hmwszXVUxWkez7JQ9mJnf7biSgEoiMmGQQ6gJ9ryMGlpaUxD8TO2Eqxw0LYZj5aqGK8OYAEqqLB9L9Jivqg5oH7Flg-oROiFAMXJTfenbxdeRIQOetwRpf-Uy72j9czRZWshZxjGIHE9r_XXGWDylKXosmRMqFcqNjrus8FonOsd0OZ1LcBWZbO3O6nw1oso-4ySmD1gvJZ2QH0F4bXF3ytWM5VfFsqgo43VRZQsxdDgKbpMT4haD-mzJ3UdyXaPSdm6Fpt-R9SGnJgt051AVbTHagY2SqJMwMrcmDr2KTQgQOiKA-A4LutU70nG7bjYQW7UeiKY5rN56vRGC8cIOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=hmwszXVUxWkez7JQ9mJnf7biSgEoiMmGQQ6gJ9ryMGlpaUxD8TO2Eqxw0LYZj5aqGK8OYAEqqLB9L9Jivqg5oH7Flg-oROiFAMXJTfenbxdeRIQOetwRpf-Uy72j9czRZWshZxjGIHE9r_XXGWDylKXosmRMqFcqNjrus8FonOsd0OZ1LcBWZbO3O6nw1oso-4ySmD1gvJZ2QH0F4bXF3ytWM5VfFsqgo43VRZQsxdDgKbpMT4haD-mzJ3UdyXaPSdm6Fpt-R9SGnJgt051AVbTHagY2SqJMwMrcmDr2KTQgQOiKA-A4LutU70nG7bjYQW7UeiKY5rN56vRGC8cIOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرایزی که دانیال اسماعیلی‌فر ستاره تراکتور برای تولد همسرش تدارک دیده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105032" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105031">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxRzxI1TQMFSCJ-34z1iWrm76funrd1Odgt3D0qVqT6KQzkABQ13btFydQ-aQ3DGF3BJzxj22hfKA6XG9I_Yi4MRhVv74yUEuf0yGjgXO1lznfpLCjupY8hZC3cQErWo3iljyy2XFoezFdci_mDdH-_ZFpWKSdbngAmqSqMMdsT6u7u2cgx6WnwNCSjJr9PN-WrGVaRm6Y2WvQpxwJOqAGP6RXnAgkx72zRhbY1JzVk5wmarqVAmyZb3fCW2cieDrRY3cZ9SKXXXFzVSP2pm1thRILA0e-udDA75D2siIj8rJ5GgiKWeXRCOi4ZP7bzrVLGbOwUY7jnDLYSm9vCUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
تونی فرشا کاندید سابق ریاست بارسا:
جولیان آلوارز می‌تواند آزاد شود، به شرطی که به‌عنوان غرامت، مبلغی معادل سرمایه‌گذاری باشگاهش روی او و دستمزد باقی‌مانده‌اش را به لالیگا پرداخت کند؛ یعنی چیزی حدود ۱۲۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105031" target="_blank">📅 20:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105030">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=ob3OrROsypI15xBaNJF9U7lDN-fNO3F255uPvgYqvaeJk9URyMBOrzkhsTmizEolpIWRu2xPYjvoBORtaXRzjD66JTTFeJK-S_-Esjz1iY6udA29MDNNVf7Qwxjrw-XCBrAm-YO4jbAPbC821jJNJcv-NH6nJobWLcvW5yE_M7IMQb3eW6_7Cu7cB-vB1lzeAKExjGfP0VIIigqj_4xufrt7M6YtgFIX25dj6Q2CFDKzh-FsfTYwcPGXFr3xgo4LDzenXnT3Xbf1-ZHU-mGta11MAbDUP60Re5CrZB-S2cfoqMZcykqzFB-7i9y6QWZ7rwwqid2XZJ0gFYE4JQIGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=ob3OrROsypI15xBaNJF9U7lDN-fNO3F255uPvgYqvaeJk9URyMBOrzkhsTmizEolpIWRu2xPYjvoBORtaXRzjD66JTTFeJK-S_-Esjz1iY6udA29MDNNVf7Qwxjrw-XCBrAm-YO4jbAPbC821jJNJcv-NH6nJobWLcvW5yE_M7IMQb3eW6_7Cu7cB-vB1lzeAKExjGfP0VIIigqj_4xufrt7M6YtgFIX25dj6Q2CFDKzh-FsfTYwcPGXFr3xgo4LDzenXnT3Xbf1-ZHU-mGta11MAbDUP60Re5CrZB-S2cfoqMZcykqzFB-7i9y6QWZ7rwwqid2XZJ0gFYE4JQIGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ریدمان باورنکردنی علیپور در موقعیت سه به تک
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105030" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105029">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
گل دوم پرسپولیس به ملوان توسط بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105029" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105028">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9bdeaa27.mp4?token=ADp9RSfMONvqPDLcFFmhe_cUymfGEa3Phzn-ZqcLoCy4v4EeTpM1Wkr93ecsVez2rAmRHYhOP5NDPAhYqcNCB9IgaYtBmWKGZ5YjVwTKTy7nJQVNGMbEspowSzB09jj9i2eggd1_-MRP3_v4Ku3PJ6BFsiGh_8GTro8nPw6Njvf2wnFyDLKV_YXPh6PHr-EcKBkxAC5p_wSFywkUVCyzqLpompoVGHtl2yZbzKxqyDnl38MK-Rvv0eQlNUcUbAGOyMHUIbRHry3JyU8NWqsYSTo1nCEaPZf174F3rCd1xRrBaSQ8JfAqm_k9s-Ox8vUy4eQBcToi4lXSYGAlG-_FVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9bdeaa27.mp4?token=ADp9RSfMONvqPDLcFFmhe_cUymfGEa3Phzn-ZqcLoCy4v4EeTpM1Wkr93ecsVez2rAmRHYhOP5NDPAhYqcNCB9IgaYtBmWKGZ5YjVwTKTy7nJQVNGMbEspowSzB09jj9i2eggd1_-MRP3_v4Ku3PJ6BFsiGh_8GTro8nPw6Njvf2wnFyDLKV_YXPh6PHr-EcKBkxAC5p_wSFywkUVCyzqLpompoVGHtl2yZbzKxqyDnl38MK-Rvv0eQlNUcUbAGOyMHUIbRHry3JyU8NWqsYSTo1nCEaPZf174F3rCd1xRrBaSQ8JfAqm_k9s-Ox8vUy4eQBcToi4lXSYGAlG-_FVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عصبانیت مازیار زارع از گل‌بخودی عجیب تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105028" target="_blank">📅 19:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105027">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93421b5bc7.mp4?token=GoWOkgdkuVTApmP_c0MyWu-ysYGpzi-Ap9gax6dzLmI9OAvKKJOESvcnfSsBYG9n3vH76-kEl25IBh54Nmo0KcA0-frpJ7znYYwehuPNKpiXNL-FIJoOGcirA96bSijSMcOBgxvA3H5qVX-2OciqpOSixIRYxcJbbU5Y4AfJrzfWO1QL1kVEzkZIjPprzU5Aoh6nfZNnp-ad3r5mWbbD65Cvy9Ch9n2zNOFlHrLpjrK5chFr34KSlRf7eozyzRPZyHJH7qVR5DWvEIHe7G4C4m1X_cgnphmjeHg4ibM09SXBormf3rwo0eFm07em6YlhVeC8ER4uSA8qeXKRDKQ2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93421b5bc7.mp4?token=GoWOkgdkuVTApmP_c0MyWu-ysYGpzi-Ap9gax6dzLmI9OAvKKJOESvcnfSsBYG9n3vH76-kEl25IBh54Nmo0KcA0-frpJ7znYYwehuPNKpiXNL-FIJoOGcirA96bSijSMcOBgxvA3H5qVX-2OciqpOSixIRYxcJbbU5Y4AfJrzfWO1QL1kVEzkZIjPprzU5Aoh6nfZNnp-ad3r5mWbbD65Cvy9Ch9n2zNOFlHrLpjrK5chFr34KSlRf7eozyzRPZyHJH7qVR5DWvEIHe7G4C4m1X_cgnphmjeHg4ibM09SXBormf3rwo0eFm07em6YlhVeC8ER4uSA8qeXKRDKQ2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گل‌بخودی سمی ملوان مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105027" target="_blank">📅 19:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f5729443.mp4?token=F3AyLX6gDu6wizUpwvCZiefmTnCcJrZe_KiYgrCaT6JEI-5VWkuqpgCgT4Lgc8ed8Y-ETrYjMbDjt5lLrSY2KiE-S8odODsmazFqQ7FxAkNvCVgAw7KzCC0r2qYsWmPgPJCLnkIYFLEd3VEPOR9nDOBnu-fHIg8xoxPHw30uaM8AJUvHCqHS9oLmKNOaA6HeEzwplqZ0x-b-dqDJt22Ej6KKwQp4k_x8-FelUflxV9uwnKGoRGdhkivhSkxGiuz9l6h-oQtFd5i_axC1mNIY6jciU2dj62xI19ZAeMCb1zNnd-6II8AX5rvjWt4ejTQVpdvtbF5XSu8RcvzOluFF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f5729443.mp4?token=F3AyLX6gDu6wizUpwvCZiefmTnCcJrZe_KiYgrCaT6JEI-5VWkuqpgCgT4Lgc8ed8Y-ETrYjMbDjt5lLrSY2KiE-S8odODsmazFqQ7FxAkNvCVgAw7KzCC0r2qYsWmPgPJCLnkIYFLEd3VEPOR9nDOBnu-fHIg8xoxPHw30uaM8AJUvHCqHS9oLmKNOaA6HeEzwplqZ0x-b-dqDJt22Ej6KKwQp4k_x8-FelUflxV9uwnKGoRGdhkivhSkxGiuz9l6h-oQtFd5i_axC1mNIY6jciU2dj62xI19ZAeMCb1zNnd-6II8AX5rvjWt4ejTQVpdvtbF5XSu8RcvzOluFF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
🤍
تشویق تارتار و مازیار زارع از سوی هواداران پرسپولیس پیش از شروع بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105025" target="_blank">📅 19:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105024">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHNuQsRxcteFhA6zKrZYdyQfr4CMD6IFVIj0WNT7DbTkEdwPgpNbpZk_niqq1DBZj4YHAEx0vrv75UfchxEqpZeJafVdZfvzMy2Nd3FEv42nUJgZEU993nRFLjrXFhH9fw-erXMxsB-27vvxQJL_ljuwKTJcCYFhHuynQmYpPM9tB5zwsT8WWj0sFmOs3rNJQRPKFmW7vx1x-m-WjuRwMU640vf62ZMl95OrqIz32SrDCUpwFVWqYpwy68ClcJtgjmB3awliWELU3YyALcTqvc-zpIPoZs2zCc_gEEL5JQBNkDEGsAtfhTSA9qk99iD9P6sELJg8bm6Z_H1OaoHbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: فرانک‌کسیه از الاهلی عربستان به آتلانتا ایتالیا؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105024" target="_blank">📅 19:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EB1FwWWunSqFzua2qj16jCAzYpsvs08aId_o_i2fFDXoEfjGXxB9OPtsTSKf5ECHWP4_kVJ-9iTWsYT4sIBDtCnFFMRU3i63xPZFk95zO-ghx-3rLQQDjV8zDPE7omIRRl16MI-IWn-jgd8ffnvgukNgDYsNNLZ73KS_yk1pf8Yc_qXk5lA0jHt6Ld2C4XA-7G3GwYZoPpfaQoZGuxOSCzANuaq234jbwbi15vfiF5aQCkgZ87SF93YOGghBycOHa_8d0aIsxyecKMXw39qQRAyeJycRp969UUDYh5YH0u6iHYxeLebT9iaaP6f4rIl6JQ_3B7RM3RM4U9TY3A3gCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhpK0aViJBX67-RrQwHBoW0A3VTEzw8gVimC6zkoyXRu403KwCS8MuaVOZSsqmQ2eR1pI-WCxLiTAQyLxhkdRWpn2BhvXxow9O2zA4B4ZaORqRfdChrNZ5_wEqrxwUeDgARxAMH4Arq8hUJmEZGn3f5BM19NoKJU7vTKCFEiEm7QSjyloZgoGO7VF7ujn8svGCX0USZZJ22BH-GvVIMtilRIV9xxn0e7wcJg8pvjqt0t39CG8HgVr7pyKaMzSDSJ1uBeCTi7I7zSz2vCGzcCXYIbpEIcfeJbDzngnVEZH7FwZCNM9UnHLI-rckfr39IyfF-l9xX1QwobXuoytloRCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏟️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و نیوکاسل
ساعت 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105022" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=k-Q1ZTP8FEVhbZmw6vHUyZ39_qs32AWFiC9U3Qz8VbjCVmMd7blxfI-a4urcKgnTQTyqF6ushvvBF5yrFO82enarX-IftvgmUtJ9QWQeiVPQSsKB5juzOUOY5I5TrfR07Ce2bf_9G_bHAMeXVQkBPl2-5wnOwSulkz_hNAmq8DMxBwYji9TE3YhL2N10mvtIlN4wSALphQA9e4izdp088obbx_p_NnIFEXZaCi6QcmELi9wtBUz6lgZrB1BTVHX423hQFoufvsKki3LbF6ojet46ffbqf9myu77kXZqs00VgbcvdH6w5M18Ouh4mOB1XWwBjU5SGGfBotKIc6rPkEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=k-Q1ZTP8FEVhbZmw6vHUyZ39_qs32AWFiC9U3Qz8VbjCVmMd7blxfI-a4urcKgnTQTyqF6ushvvBF5yrFO82enarX-IftvgmUtJ9QWQeiVPQSsKB5juzOUOY5I5TrfR07Ce2bf_9G_bHAMeXVQkBPl2-5wnOwSulkz_hNAmq8DMxBwYji9TE3YhL2N10mvtIlN4wSALphQA9e4izdp088obbx_p_NnIFEXZaCi6QcmELi9wtBUz6lgZrB1BTVHX423hQFoufvsKki3LbF6ojet46ffbqf9myu77kXZqs00VgbcvdH6w5M18Ouh4mOB1XWwBjU5SGGfBotKIc6rPkEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان فوتبال رو با لیگ ایرانسل چند برابر کن و با پیش‌بینی نتایج، امتیازت رو ببر بالا!
✨
🎁
هرچی پیش‌بینیت دقیق‌تر باشه، شانست برای بردن جوایز جذاب مثل موتور، اسکوتر، پلی‌استیشن ۵ و... بیشتر میشه.
همین الان به سوپراپلیکیشن ایرانسل‌من سر بزن و اولین پیش‌بینیت رو ثبت کن:
ثبت پیش‌بینی</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105021" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
