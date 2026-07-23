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
<img src="https://cdn4.telesco.pe/file/AKt9Hvo8xGK6wy-8PY0z4DYAr7AuOietYKPee0Aq3adwUfx2SvnK_Ga9pn94wE2I-iNvAXWnKNIcWXrTiwHUafeRSbt8e11Xtf7AMOdULoKGLXMmu7IPTHyBwCkNvYDHB8T0ttuUGxOrGvCxHR9B_Uptim6a_DUSvZjz9sL0VDm5QbznyvdXpFc2MLslpamI2t1X6BzZiVS1t9FJuuJBZ3DrGGggDQziwf4uyLosCLZefObMC7x1NA2dtFUM6r8BJ6ishbBX1mFw0mHDA0wwU-5Ziy3Stvh-y1D0_DrwsCjRm_yvfq633S_dF91Utyd4gBUck2fqxZn4I-v8LiWB3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 151K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 02:24:45</div>
<hr>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0BNn0CFMF0j0wP3E1gRJOLM6Q-oQRN4nVPGg7JNiurRGaiLb73S4wXLjqOQwBKhNYPwqfHCz75XLqjnQtlknoumy7YZDwVjmoHTSLn6cgrUnOAkRkdV31TYseyTmoqKVOX8EMvOjtOGSa3N71_R_G4kUm_vmgsKylzXlrmc_ouCkuIKm9qLXseNzI0CuiO9kuIgtBiCuPvIkYMbm4L5FJx6D5EA42MTmjaXfoYg0cnkNK8_O8uBaZHQ23mkI4mjp8xkd2rgN4MXXrlHVPNsr3WVlpmNSHjzSn4E6KAfpl3hfku9SgifzKe7-tbpBrge9iDy6unE6gC86xiMg6tSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=IW_sa9uQyBUjkRgrLvulOtP4cVTdWBhvTB1LOXGRIimNRRHBnWUoBCDVlPkVc_kuk9uHT2gvQhD9IoH4334zqLR9QJQkrDQA1p6ZEy2ySLwJMFguIPyib2h1QyXoZ_dXPTfQdc5KPgt3CgDSUeWOK3FFm_9P-mW9W2Cb130tRwUvqagHYrwEtEPPtFGuTgKeu0Xeu9vio28ow6htt-5XnudDla1Khgl9Gq_UpD57RVfY2zT5CGLlGvhen4MJemWhYkGBBs2uv8OxpsHpmasuX82UdhQfyvyZXVqOlHGgzgLy-kWElgFo3-PmARsgU3YS3fQ_2yrINxZ5BNNNUxaCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=IW_sa9uQyBUjkRgrLvulOtP4cVTdWBhvTB1LOXGRIimNRRHBnWUoBCDVlPkVc_kuk9uHT2gvQhD9IoH4334zqLR9QJQkrDQA1p6ZEy2ySLwJMFguIPyib2h1QyXoZ_dXPTfQdc5KPgt3CgDSUeWOK3FFm_9P-mW9W2Cb130tRwUvqagHYrwEtEPPtFGuTgKeu0Xeu9vio28ow6htt-5XnudDla1Khgl9Gq_UpD57RVfY2zT5CGLlGvhen4MJemWhYkGBBs2uv8OxpsHpmasuX82UdhQfyvyZXVqOlHGgzgLy-kWElgFo3-PmARsgU3YS3fQ_2yrINxZ5BNNNUxaCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MbivvLuGOQ1cKHx0paqeipqS3ec8m1basDHE9jDJE_QSwk9xChkr0d4sTH4yq-1l8HVk62ZOQQ8B9dAgug-HWuPGTVsxuMRACBfV0hD_Yyme99UpSoglpceV9w8N1-sZ6W1a2GJULEtZVnLKanQv_FKy9b_V7ATAZLQGnULnD8XASztPTRoSU-qAgOGSSizpt4TuyWrEXDmlvDiD7sJ9m3hYtr20Wp3GaH35xRZznLelOMi7A6WeqADCAMvoikf8M9GFvbd8LM1mBFnAuTgDBtqQT8MjM53pl2yEYqclbH6U8PUeHLYpwAsP64pNi2jNhTngzOwMCfPqWF1NpCTU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MbivvLuGOQ1cKHx0paqeipqS3ec8m1basDHE9jDJE_QSwk9xChkr0d4sTH4yq-1l8HVk62ZOQQ8B9dAgug-HWuPGTVsxuMRACBfV0hD_Yyme99UpSoglpceV9w8N1-sZ6W1a2GJULEtZVnLKanQv_FKy9b_V7ATAZLQGnULnD8XASztPTRoSU-qAgOGSSizpt4TuyWrEXDmlvDiD7sJ9m3hYtr20Wp3GaH35xRZznLelOMi7A6WeqADCAMvoikf8M9GFvbd8LM1mBFnAuTgDBtqQT8MjM53pl2yEYqclbH6U8PUeHLYpwAsP64pNi2jNhTngzOwMCfPqWF1NpCTU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgX5GBzfsmALsKT1OvtBRGQ9SeP4-JnD6_biFYFZpKV-OP8vhZIlcVsxC8WQAcQutghCoMDX6C0tcDHOxeyOj-eOmzgS7eFCD5IXGd2714cJfAvqRNyX49iTm5fvMF1nM5fs8_La4nu0-6_wawhzI4o-D6uLZmkkG6i-aWy8pDV7czhPm-Z9o0dQsLjTxRTg_PjxRxscbW2Od_RNft1mREm0hX9FxS7W_ghpt0kbURaleViH7HMrhNil3ldCmlulruxDDqexd1YFHcc_49ZBOpKUDCY2p5FRYkPqQ_T9OMSBJrpmVcArc0y_8WbEJMgN230qaHJ4ZgF-EpQdiigS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BERS-1BIM-jBhKsA6rGZF5Ij2l9J6vNaHkHNcWI50ZqN2FL4eEDQ2JmoHUNA0-OCxgf3dUyw91MOl27IL_i_pjsZH3gXr3VgtnMdtzLYdc2PcIc2mVux_Rq9_T-Abv9UiWLPu8RIQFlqIKCHDyTqI9xdMUY-XrFKG1HlMH-mya_oJ9NkTCrTOhCLrq1g8aDHZIuEXV5tNvuA7hjXUmQHn6mHKoS6pPAWfAzm_9DIz7F8Q_PCyGnTToLs1wlxe26lTrmpOLaCSCBsdE5LFFuUz_FZ22FZyKK9FjrGuOUSvvAEIxXrtBJKL5X_t_-QBKmJXj6sdb9QxfrEQ3x-nx96JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zjo4MieI-SsquTK59NEebRy8MSGtSzP-WVO8Eoflv9660sxvFQRCUlWSMqV6sesrT8cpFWDzbtbh8ldJjAvn4rcwct_WzhKwQCY-L5X2WGOMvF0tynZHvfZydaDxJw5qDAhcSvc-cFG_q5qI2zPyWhQ8-ApyxO8S86pz4E8cjzHrzXzcfBtgfjvF33gG5VjXJf5GIz__n5Er0WuwqMioQWUFQW88BsbbWtiCIrYl-eWtAVCca3Wu5olun1lUt1YCpr_Rp1-fI1HWrwLJSscpwt7UlgG0aYabuZiDTZw0ZVL3Wj3zIEBrKdG8dhZB7s864RTylYiFWz6r6hUi2truCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=dvgB9Y6-MFuoViZpYwDVIRts9dXq029MdHbjXR7SgKXswdOC5NkGutFmsjkOCAD5HpTcNGGKgWLVdWRUS_c5MHnC0hbUApSUHNGGEpCe1KTm5lGmqFEz-fPMqk8lVzPtvIpvn4S8hn9crtpMwCS99pFQcPzf27EKT3WXZg3o5Q7cIMVz_NFiHzXDLQYFNQC5YoYxZA5n84f6lt2PjMGCp9s5sRrYpdN2r1xpfJK9H244G2c2QN0lZmqOwToT5iFEkRYBlXR7M5jFBe0eo4NAifuCtcVZo3JpzuBr8560vmPNGf29t9ZBkqD8LifNENMdkerwSD_O0aB6eAvTP4Bn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=dvgB9Y6-MFuoViZpYwDVIRts9dXq029MdHbjXR7SgKXswdOC5NkGutFmsjkOCAD5HpTcNGGKgWLVdWRUS_c5MHnC0hbUApSUHNGGEpCe1KTm5lGmqFEz-fPMqk8lVzPtvIpvn4S8hn9crtpMwCS99pFQcPzf27EKT3WXZg3o5Q7cIMVz_NFiHzXDLQYFNQC5YoYxZA5n84f6lt2PjMGCp9s5sRrYpdN2r1xpfJK9H244G2c2QN0lZmqOwToT5iFEkRYBlXR7M5jFBe0eo4NAifuCtcVZo3JpzuBr8560vmPNGf29t9ZBkqD8LifNENMdkerwSD_O0aB6eAvTP4Bn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=bVeuFHRtTLZmm51j1J3vOcRisMne5y6zXrT4XVH4fBqFUdDmWSqgBK1rLYXsya2Q_MYp87PszTwB4W3qogCgu3EIfAK0kzt100yzKOVMgx_oblVS5cXZ-ZKADgDXxt-40rvXtIneSTi4TbQYjFZUuAUH_Mqb5RuWZev7Zsrr8qmndTnmkRQBAflPCPxbCiIKibUX_fttmQB6d1zcbYyMFj6SZtUBijtCY_gb4RPySUUtDzR-Na8J-l9Aj-gej1uUJCAztwQo6EaZZh5v8T0cQb8235YMRZTZh4Ju051GmPJ6Ow0-9clO6YZeU6NAt3cCLnNwDzqslZAQbES9SO4TXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=bVeuFHRtTLZmm51j1J3vOcRisMne5y6zXrT4XVH4fBqFUdDmWSqgBK1rLYXsya2Q_MYp87PszTwB4W3qogCgu3EIfAK0kzt100yzKOVMgx_oblVS5cXZ-ZKADgDXxt-40rvXtIneSTi4TbQYjFZUuAUH_Mqb5RuWZev7Zsrr8qmndTnmkRQBAflPCPxbCiIKibUX_fttmQB6d1zcbYyMFj6SZtUBijtCY_gb4RPySUUtDzR-Na8J-l9Aj-gej1uUJCAztwQo6EaZZh5v8T0cQb8235YMRZTZh4Ju051GmPJ6Ow0-9clO6YZeU6NAt3cCLnNwDzqslZAQbES9SO4TXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga9B-y3Ysl2uStvGaxj69vK20jAgVz_z_m8OEj2atBbjUU-FHbwFFwUl5Ip1BRV5P326n8OzBjsQ_BSv8QdNUL4iYnG54pHU6twcwl6sMAvPLD65f2WCrNpRfQKRsBW-73HrnMhzfDbgx3j1xJLv6sA88f4QDj9dywM5JQdMR6wsEDA4UlFDH0dMj1s15qlIfNViPgkxasHC9feztmvRNKJhGschAPmuE4fncEo3T7dOCIFicnpUeD2DgQN-ZlbzJovUFytboM2n5XAsP0SacG_cSh6LTyVAq6a7OaZgbFi3X38cctfkgu398EnEmmbmgIf09UvnTNQHg0-Szx3t9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=AKxxcx0VuHqjrfh8L_n995W_WiGViIcawK9ICUyIjY4etsu-EHngmTbgBhicqq1HK-l9xor3vlqsczkSf-9K81xZZTISNgzvj6v3KnLPhM2xZhPf9kfEkGFQ7EsGyHoSGDzeY43DcaEJ-ZIVIMt90Fifr72SBqKrlU321z2HrcPK7OPNoGLDk5uTsBUjLE_7T3Po8Wwtzj1cUaRfn0wkgjazXBV0mgBMFr44WyJmqJf7--WA_GdAnyqMozrP6RrtGmc9PEoqTL34jnwRUkHdmwgKrnuvR2L9Tzybk2x8JGwGxgimOOzuRyeKQwpWV1JUF51wMll53hF43E0oY4wVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=AKxxcx0VuHqjrfh8L_n995W_WiGViIcawK9ICUyIjY4etsu-EHngmTbgBhicqq1HK-l9xor3vlqsczkSf-9K81xZZTISNgzvj6v3KnLPhM2xZhPf9kfEkGFQ7EsGyHoSGDzeY43DcaEJ-ZIVIMt90Fifr72SBqKrlU321z2HrcPK7OPNoGLDk5uTsBUjLE_7T3Po8Wwtzj1cUaRfn0wkgjazXBV0mgBMFr44WyJmqJf7--WA_GdAnyqMozrP6RrtGmc9PEoqTL34jnwRUkHdmwgKrnuvR2L9Tzybk2x8JGwGxgimOOzuRyeKQwpWV1JUF51wMll53hF43E0oY4wVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=HT4MN5d3JUviflvvyy5Qsyh_54bO_zQn-arFelitsUhpyXxpI80L0bvIqs0s8RPbXhQ_FB5YCuMULc2HjnNXBzpiqDgCEkfArzBwlFmM6bLeM8LJx9SCJpV6SRbFTyd3dlJyajxSbTxLsEQ_g8NL70KJzFOGmlcLR_TTQ__qSl_ah-N2llTyG4AVqKejRki_I63AkZDfdJjO7PAfcnn05h127ijmCAaLBaNGOcSFKmG2VxheSNP26mJptPCRWfMNkgacj1PDNyS3Ho6P9-vtB_l-yecLPWL5n-kyUMZ7Qh-rtsYvhK4uM6WHTPEUZj4WH86XL1o340IrnMG7TPrGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=HT4MN5d3JUviflvvyy5Qsyh_54bO_zQn-arFelitsUhpyXxpI80L0bvIqs0s8RPbXhQ_FB5YCuMULc2HjnNXBzpiqDgCEkfArzBwlFmM6bLeM8LJx9SCJpV6SRbFTyd3dlJyajxSbTxLsEQ_g8NL70KJzFOGmlcLR_TTQ__qSl_ah-N2llTyG4AVqKejRki_I63AkZDfdJjO7PAfcnn05h127ijmCAaLBaNGOcSFKmG2VxheSNP26mJptPCRWfMNkgacj1PDNyS3Ho6P9-vtB_l-yecLPWL5n-kyUMZ7Qh-rtsYvhK4uM6WHTPEUZj4WH86XL1o340IrnMG7TPrGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=dqurP8zUe8W2PlykkBVJo-5YbTKNpB4S4Y3lUKlqYscjC_r71jrpBO4zbtj5G5-50sBkBkx-gtVg9isFd9WZjYl4R_tgr2RX9k2qoqSZ0yIw0o3T8UXkCBDwaVypNh4DWl8V65uXIV0j12MoKZ3ah9pYeB8HhM2EUKeM_kh-8F_VVA2AGpm3Tg3IBpk4LAiGHnbhcrcMIz9A-F7vjaepiyiA6E8xcjVg_Q4XF1duP9lIy55MuhUjKLV7e0AsaViDQLJoreY4TSHctB6BdYCKN13eJGk6fWVwUq5O2GwprJI4QTZGsOUWQ-as-5YR86cxRnolin1WIozQu2lUVhl0nI93fVNQTPnd1kse0d-Aq_cW9vsvEQ3-_NrgNXMCrH7cKyOUe2XhZBGGmcHpM9pkRP1zCSzXzuxxqC2WOourAUWKbNXwYfQA7y0vC4W1tiLZNUhCzwb2Zrv1Ziu8iQojWSnX3J6wGwcYz7vUJ-lvWaJ6WxxLTsCA1G4XXlA7uGwwsBlGeG9WO6YCZ8a3j1GHz7P5QdLAHvQwXgiHt4Wkxam4paBkoozp5cfZYcMDZQHIqZuDbQyINKIyQcLRS8HVYnS9mYsH-pcGFjHdH6hmE0zdeeGPRlQXANGoMgA34H7WBVfINz0N64ON_iIfXsGt7Um0KAzaYycdq5SQQ0Pq4-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=dqurP8zUe8W2PlykkBVJo-5YbTKNpB4S4Y3lUKlqYscjC_r71jrpBO4zbtj5G5-50sBkBkx-gtVg9isFd9WZjYl4R_tgr2RX9k2qoqSZ0yIw0o3T8UXkCBDwaVypNh4DWl8V65uXIV0j12MoKZ3ah9pYeB8HhM2EUKeM_kh-8F_VVA2AGpm3Tg3IBpk4LAiGHnbhcrcMIz9A-F7vjaepiyiA6E8xcjVg_Q4XF1duP9lIy55MuhUjKLV7e0AsaViDQLJoreY4TSHctB6BdYCKN13eJGk6fWVwUq5O2GwprJI4QTZGsOUWQ-as-5YR86cxRnolin1WIozQu2lUVhl0nI93fVNQTPnd1kse0d-Aq_cW9vsvEQ3-_NrgNXMCrH7cKyOUe2XhZBGGmcHpM9pkRP1zCSzXzuxxqC2WOourAUWKbNXwYfQA7y0vC4W1tiLZNUhCzwb2Zrv1Ziu8iQojWSnX3J6wGwcYz7vUJ-lvWaJ6WxxLTsCA1G4XXlA7uGwwsBlGeG9WO6YCZ8a3j1GHz7P5QdLAHvQwXgiHt4Wkxam4paBkoozp5cfZYcMDZQHIqZuDbQyINKIyQcLRS8HVYnS9mYsH-pcGFjHdH6hmE0zdeeGPRlQXANGoMgA34H7WBVfINz0N64ON_iIfXsGt7Um0KAzaYycdq5SQQ0Pq4-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu5kROcIziO2wlKuJs3uw8R3gNNToPC03cvtCe2wrOyoQUZvmm0zGYaXhLCJhf0QsnXNePV_TntYRDwnQ6wIo7zS4zk_xXXwAZySgC_qh7mqw1-sap-NZ0GPajzEJpF4QajOE-p9iXz_pOcRQsWbvUXBBQstY5cERMcZPfbIAk_0YI0Kjp4bXr3GZwlLFzJfyRN4xNx8gtbkggSWASDMOAdpHpDuf3QuT5__Uv106NE31XUYwSXlZb8G04neGAbFkvdEBn-CmJ4llD2uh54YuCi3FQGEQctiK6MyE0zUaC8gnGmJHvYrDEOWblyyQqxXGQdbUwF6yv0V0TbWf85c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9qbkJ41vI9Lxca8GUDi6Ot3MdZ9e7z4yw-sU5rR9tmMDpSNt2MPQGU276-mL5Jws0YXngle3HKr8HCgTlCln5QUy1pbbZYbP_9Oh6Myknor_o5rTu4EEqPyHxhA35MTzoHQXvD0fCGOGSWdZUmM9rV7vsdOT_mHZ4bqIXm8XnZtYYbP-esngrTFJWLTaCcGjQ0lEbkpbiwaZHBcGRQQZA2dN-3IyUa4jikzT12Ctyy-KAl7CAKl6WUCPxw07g6ed8ub3q4Nu450BFS9Q2_q80AsPsS5hIS057gT1YoUiGTUdddHwPpfy4z3s4-VnWU_RVLkd9AYqJ0GbYkgMim61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=jRM7KtjYlpxkqAt_Ur3ydlQPS9iPHG36jOlHbc11caG-Ex3woFwNYyi88vxK88oqthDuzLOGMshruz1uLy8kSRcS7VSLvHGaQH5ObSDx9zsoF4o2pKjilzgN2qikRrVTgExwEwfIUK0_9wuAJP7qDUqVdzhVc0zqZzuzOQ4_7WYmU2XwW22BgcbwIvQwerI0_CYW5SiueWJO6Zftpu7CBg1YkxD1A0avT30uVKTXqLuuFDrrzkj96IkOKhrwqKJw4bpz1vJa_Uf-rG5i6aisSxKyYI_LqGIlCRgsWcPC5pke84bbaijscuKxJ1g61gkX0QMGJBrcjnGdjquhwqT48A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=jRM7KtjYlpxkqAt_Ur3ydlQPS9iPHG36jOlHbc11caG-Ex3woFwNYyi88vxK88oqthDuzLOGMshruz1uLy8kSRcS7VSLvHGaQH5ObSDx9zsoF4o2pKjilzgN2qikRrVTgExwEwfIUK0_9wuAJP7qDUqVdzhVc0zqZzuzOQ4_7WYmU2XwW22BgcbwIvQwerI0_CYW5SiueWJO6Zftpu7CBg1YkxD1A0avT30uVKTXqLuuFDrrzkj96IkOKhrwqKJw4bpz1vJa_Uf-rG5i6aisSxKyYI_LqGIlCRgsWcPC5pke84bbaijscuKxJ1g61gkX0QMGJBrcjnGdjquhwqT48A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZLzcJbyylgGGwmMSztt3AUs_l_gjMCORB9BgSwr7ut-jhGXGL35u0Lsk20GW_gutDBPkxTh5VRROTTXrA-kcFCDeBjT01GwXBzBQpfmi_dAlx9aX5hHbuBx5z2scPcQH-1HQafcdiKBi3tpzBkVfr_ZJDuuxmbH46VHGuEjKbZaxRl9WzAaZCBgLThNWmF5WFtlop-aI1rnCkDFYBs1AWOfdT4gbItp9sFnkp2waNKnpBZSRIZxa9RLlgmRgxK4Eky054dx0R3u9cmbqs1XSGws8MJpHXBDUzOlTza6POxbSlcnYehMaiRA760BSE_M5TqQaYg6l0Cg8Rfz_lJ0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVk9v3nWDUCHwCZhnmHJRjok-wo0pI7KfRQlVDrNZF8vG_IMh4GT8PtB5Hd136oTFkzq_K5MUgVVYjfQ9yXgMvVhcl21wCIH5hRAnYAyVoTUqUbYGXkmKaeJAc6u4KZN3BnBJWNfb6UHkl2J7OBtVprztMsKfac_VlZXxotZJrOnNe-qppwb2269hu1WcyonMcwW9gEb5GG3PmNRaXsTPDCe7DqHpEwFsSrYAA_KYmTGQ7INsOlcDsoTYXb4Dl0DK--QpLgveXVJjyRrTNJ7Rmeeohi02lU17sp1LYNsZlPnplxtsGrUUMLqthOfU613Zmbj33zAbSk5GZ_ul8Cosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=sEwCarSjTtJj3OZgBJbiNFqCXz2_wdhqn6yd9_U4FSZ2qzdQAG3keDfEAVdn2lk7nN6WpOU8xJ2yRGKVHMRbAlRCpe153Jubj-dUowVDlOj7zL5UFTaCZNgRjqHxgoRWgxyC4636zknt9R7o7vSRJvOAYKG-QtXNaMgTJSVS-BqW-L9bwhiWigpZrO4_V9_H2X9Zw7D1FmE2L8xay7EGfb02tiy2k2ZlRgTfksNSlJ57AFiZiZvx-OpKfwU398kMeRXabCq0Mfc5ov8XH6GNsdUBBy8ZVl7t8E7kswiW5DmsaRJFQf2m_0SOiYMEd677AHlXP7llTtaL77w-jZ9xnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=sEwCarSjTtJj3OZgBJbiNFqCXz2_wdhqn6yd9_U4FSZ2qzdQAG3keDfEAVdn2lk7nN6WpOU8xJ2yRGKVHMRbAlRCpe153Jubj-dUowVDlOj7zL5UFTaCZNgRjqHxgoRWgxyC4636zknt9R7o7vSRJvOAYKG-QtXNaMgTJSVS-BqW-L9bwhiWigpZrO4_V9_H2X9Zw7D1FmE2L8xay7EGfb02tiy2k2ZlRgTfksNSlJ57AFiZiZvx-OpKfwU398kMeRXabCq0Mfc5ov8XH6GNsdUBBy8ZVl7t8E7kswiW5DmsaRJFQf2m_0SOiYMEd677AHlXP7llTtaL77w-jZ9xnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=AL0J-FZodkbMRi8I7ffRidj39CNsxB8RMGcHeIdWLa-cVasc2JVRMEYOwdz6VTwIV5SrzP2KNiZ6BJx0EEgBHZsWHo5L1u4JKricvy8Pv8j-0rmD73BJFhbpp_90D5gpUZiaAntLFL506kIzNLA6xCP-d-4AL8Fql7LFgNCo35fpJcWrWab_NYjWDIAwg72sIIbJ6zd8KHng4133Ka8PoIiDxOZGKHMxVdEQoBowNGNSQ3cIKW6JK_bWQJP4XkdRoHsIulKxj4vzOG6OOBWRxP1bsl-PY9xXiEYKnGsZkSQbKuUxxvCq9RxFk_3V7rxV1Zw_Q8_gKhG2p7QdjEkPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=AL0J-FZodkbMRi8I7ffRidj39CNsxB8RMGcHeIdWLa-cVasc2JVRMEYOwdz6VTwIV5SrzP2KNiZ6BJx0EEgBHZsWHo5L1u4JKricvy8Pv8j-0rmD73BJFhbpp_90D5gpUZiaAntLFL506kIzNLA6xCP-d-4AL8Fql7LFgNCo35fpJcWrWab_NYjWDIAwg72sIIbJ6zd8KHng4133Ka8PoIiDxOZGKHMxVdEQoBowNGNSQ3cIKW6JK_bWQJP4XkdRoHsIulKxj4vzOG6OOBWRxP1bsl-PY9xXiEYKnGsZkSQbKuUxxvCq9RxFk_3V7rxV1Zw_Q8_gKhG2p7QdjEkPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpJwAQW-ST4HgUaXdHOj71kQZJiAwjK4OeFXtJpUwQLKO_wFdZD8-JeKsRy_1Oat-QHa8VejDym-K5lRl_yzYMAn8ZYKHWbENdM7zUpU7c26BkJ9BFErt_QFq1oTWceYIUgPA-ocEljK0ZdojDPFSujVVbLQ7IqRFBKVWjTtqtzZM8xSY2rwWEzrQXqrIuZ3S63g5XKtewVsQ09T0_pKbIPa2PCcbcNHc4kgl4PNn70GazkcjdYsesOqaTG83LZxQ7nHJeNOVIMa5h_gnZgTgdQUxDANEqpkn0JkBDIOV_8BTWXDm-SeWR2x5LzT0KbJxQ11B_-jMP87AoCHuCe0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCU1Ypy9gfBDKNr9WwRr0-zmwMzou74ReYwelKDfQwZsjlSPtmPjfKq5M45hAkhyE0I9qj04t9YqnDh5uTKBVlsC3KxvOEoUQdFDoqFIF9wwZXZWbEwPGi4a-3mghhOmF4aqWXSrYXBY9yv9_KR46Cdfkclfso98icy9dVveS0ageTe3qw9jsajkW__oinfBFtPp02dsTbkcdlWl1BgF1cfw4rYk45kIzdBlvwknHEk5iK7d6Hh0GnyibmHmhqOTv-yi3uQdIQhQ_vAAD4yutJEtrMXLi_UKIQpqftyBvrulpLdhFdjEGXepbjMmw579X81H9NNzrmna7DimikQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPi6Z2z3U4VBYknUyqUbZBWN1h8ImQC9sUmZ0hsitxl7z7FWjQTjS03nyqltItjfVkE0uuAIMpBYHuxFGXBrz7Dmg3ivsFKipPEEaGgM9l9TN6Dzs3sSKNkbLVPCOI9fThWjrztk9NFZ1dFtAr_V1IzyMEa3cZlPOBsx5NH1pOZrgBJY_PZ7dEiWI--Ayttb4ijp_NdPI6WHG74TLJokk9v-sLBkOJFliQPrzJHUVasVaMLBp-1HHSqqiWe_K5cEV42nJPqNeX_wtV4rbyVMd7WiqSovzMwR87hP6ufmci7kY5y6f9SuEG8yc_uB19asEJ_1esKk4185UyhM0ZI79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97-xMYL7b5M9xmXHkv28t8eAZfEXCLOGHL8yu4Vxg4RXElx-mGnHcHt0ZfsgP3vrx0ds9oCh1glkfDDGPY-i1Pl6Vbomt4VLqOwzJ3AXCsqwDXYmg4IMgRPqbrFrL5h1CO3_d369nOoszxIh9y-TrewScJQ_aXVdaGOMgBn6G65IDUVvME4hmcLwi1gqko_SgPwa0z_YmrNsUZU7etdwj2tge5IQw3HrI55G48dsQnYeagUXNmt3GulCmqmTHPYRZpjgE5JWeuKGEy0cFWVgW-TNxAM22nTm9cOjcZsHqDICXK4Z3XZQKcFZzIzCRZdrHbrFe1m05UkhMOcQWHXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPFWgbBWYq8FM47e40fn15atGR6oiA5GWKGgf3wBiu7DHdwbCqrOgtSisbSWKPNYk0rvfFWo7BWqcWddvqyqd941IPTTH2fx8Vx29Fud0m-eYzrR5m1C6DQJRH0IewZSpfXmMbWWi-RRd3ph5W0lVjZt_Db8A7z_cEZE0RAbBb7zQejgiU7nT-oGFpnJFhtW73RgprzUj8PnV3E2dCnoS37439_hk226LHY_Hibzfm2ZQMD6UeSUF_Ls3PVrDyBTYgMZyKPUr-taBnAOJRV1_AIfhARpZAvumYNd2x8wEAR9C3GqmqM6BJniqhqz-16pgZ-PylrjM92jXBiiCvtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0MPTcOA1uRVt_3l_ZEdgeqfi85KJwTQcz0dp4I0DBrCUNZVHiPv5fa-zK5sCvgYcc3GK--J7gR8Blk0iYEteqoC5f-vpGQ4LSuZd-kllvIGPnEDwDHmM4O5kCjSoDwenUC7XcvpVBJHrdp1G6v7d67W2pZ-tgg2nJwf7GhtLMQ_vyVtyE8sIqzApOk1PQmHPh5rRpflHP-Xw6Fjtsc2f0_u_2D3p2Ww8K2SfOdmE42kafbacl1-VKTu-ynP9LKUnG-f4-22nVgc6D7SlF6ALGYboZmC62T1TqjHPfUklBl14e1zArzzDigBTMTPYMxmmqsMLcEljhN40nt_NV2vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=i3Yrp9fgrFh6IPFaSSk3xqVNvzjeMgDz_9aJGADZtydUHKubt08NDYSJDJlvr7IHawM26Tq8MiD7fClcBGq3a5KtMRpYLXxil1KyvZEv5u1BPqQSVnslP1jG5IPC4jlR6mDD78WX3P-uaTqGNyMChuUAvrgww9LcdDwfAuHAzoUGlb_91XP-OJ2XIyTXigvHuXWj6U4Q_Z6sED6Nhciceg-ZTeyzjDZHJm5TM4vr9iO1WM90Nj3QNsrUJwXwNdlxXxHlRX0Bdxly7B4S8j4fofgL1PT_UbU2-8Tf4k9Q-GKgxWur2CD7I0vxhx3IuoYW_WQyKK7_oGW2v9uQXeP6_QMvfCoQ0EDGh_zRRkpt0YOaejpdLoEcGaG1P99m25gDmU51h0G6j-EqV67wy-ljSBrdUGYuVBwXBoG-ZJu0HkVUpFj7CUmZ6yAK88iYVSEYOK78RZs825B6IdqoCxzJ9xSD3bvEhnX2D2P2SUXdk99CzAppN9yb8AborXgLUiRG1tbHvgxZ4SU-RgKhDlLoQl1rlpLmEIIv3tAPAZZxoqrIsv7_qeqrFUBIF-OgAacXNnE4oGvuo3LXS1osPaDfYcPeck81liBs_WMalfjA--5fQojX2KMq9zLokrkaYh4xOg1omqgp2lVOuaLdSG633mnxhzRyvOwVObZD5C_ihOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=i3Yrp9fgrFh6IPFaSSk3xqVNvzjeMgDz_9aJGADZtydUHKubt08NDYSJDJlvr7IHawM26Tq8MiD7fClcBGq3a5KtMRpYLXxil1KyvZEv5u1BPqQSVnslP1jG5IPC4jlR6mDD78WX3P-uaTqGNyMChuUAvrgww9LcdDwfAuHAzoUGlb_91XP-OJ2XIyTXigvHuXWj6U4Q_Z6sED6Nhciceg-ZTeyzjDZHJm5TM4vr9iO1WM90Nj3QNsrUJwXwNdlxXxHlRX0Bdxly7B4S8j4fofgL1PT_UbU2-8Tf4k9Q-GKgxWur2CD7I0vxhx3IuoYW_WQyKK7_oGW2v9uQXeP6_QMvfCoQ0EDGh_zRRkpt0YOaejpdLoEcGaG1P99m25gDmU51h0G6j-EqV67wy-ljSBrdUGYuVBwXBoG-ZJu0HkVUpFj7CUmZ6yAK88iYVSEYOK78RZs825B6IdqoCxzJ9xSD3bvEhnX2D2P2SUXdk99CzAppN9yb8AborXgLUiRG1tbHvgxZ4SU-RgKhDlLoQl1rlpLmEIIv3tAPAZZxoqrIsv7_qeqrFUBIF-OgAacXNnE4oGvuo3LXS1osPaDfYcPeck81liBs_WMalfjA--5fQojX2KMq9zLokrkaYh4xOg1omqgp2lVOuaLdSG633mnxhzRyvOwVObZD5C_ihOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo9tUDli3xlKFsCcgmp1-wg808Iv_U31BD2ejMOsMzFVuAydqFwiYT-bjPCPuS1DNkE6SvA7YbzN6w7l3dbwpOovzP7nY8H07ADFGTGmHkjtR8cmY_KFp7kCYWZ2vdIWt8kpqKbmKYl-v1j4ysPQLT8WWnuyGJIUtJrTEL48e4N9ud7YeqvXhCfbfCV9VMwsaHsyGncPt96thpGhCJTXcqNVSx5Fq42decRPZbe818J5oTS--epJO95zpWpE7YhftKz_7IMbCXVpnqqJqwYU6UFTjZx9-UIfHZKB6R6q1vxVudu70EgDP30AkstoFW-6kyLD4fzj9WZsEglW7xaJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDkgQqa1ON9OYzKkWzfwl4-3nEy0r7tMZhaEcLr_BlwDwNEwj3B78ReJuP6baHmAZED3hqwdMoaBzEee3TF0AdfobgonzC4uPZ4UN7AqYm9Cn-gPt_-qsCv-dZq9_Gu45rjhF4sM6xXAURiNg8DxtGr4m2nvBzZSiUXylLeAOSCe6pfs9OPrQ-moAlO4a-kOpl4OAn7YHol86FZsd3WjJch4xP8KSdD98qHg2LtBYs6Rd6RylpTAcn5aHWO0pZE1fgseNT4l91T94ovCGime2SEQFuLMay1_fqX6eHAhYl8MzfdgWNJGQrjsKwfudfG6wClk_MJEGVqdV6bX1y-G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFX1HiRPqIqyEcC5nMgVyFsazEflLUFMIrv0I3t1lRRo0rZNosTSB9VpX7VzPPEbxBgPoqEh4JfMxAQbWxyi3fYbpHCBa4Rc7tAtVB-hdrjsrLZzbSyfP765V23kXBFSHCV9FuRTqKhMVPEbIwEY004eUfyWyoRT3iyjVv1fOQaEirH6b1L5QBZf1KRh5-KCYzUxalYrvMb5R_oymWrCUfQaFkEeVoAxPnh4uTauyZAJu_Qv8_7rR6V2JbhBmFmRYSTQ0bKbXbrCqEXaR78SdfXgFK8RTVh9U2ZCuaC2OpqkdkAZVz7RkKYI3Gtycq2_V6OYiOlXFDYzyTmjyIK9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=OM9NKaAbWsTZyaU9WJwH5DYJvDEHYj5H2cy8GFqLCeg-maQAXqHUTUYkufiWKR7WWctaW1pS-1y3YcEmlSD2-ov4wQ7loxxY6_vxU0zHgWmvqO-o9dQV6cgVqMrRZzyy-PVe7-IcHm4vfDZng7JlcBVGFVd6AiqNfsXk7LA5k-51w7Mr9BmIY8J49H7R4Ew3GBgp2dyaiEpMS__0glYRYU8jNqw4KjWodQt8Plj860abN-z3HpR5nt93TaxK2xOfOZ-qPxHk8Rbb6ZxV_a0GCHJdX5HOSnHEDqmrTpXryplpWeBTYfNIWt-3BaFzB3Zx1_GJ31oPzG0BpJYkMKHRM4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=OM9NKaAbWsTZyaU9WJwH5DYJvDEHYj5H2cy8GFqLCeg-maQAXqHUTUYkufiWKR7WWctaW1pS-1y3YcEmlSD2-ov4wQ7loxxY6_vxU0zHgWmvqO-o9dQV6cgVqMrRZzyy-PVe7-IcHm4vfDZng7JlcBVGFVd6AiqNfsXk7LA5k-51w7Mr9BmIY8J49H7R4Ew3GBgp2dyaiEpMS__0glYRYU8jNqw4KjWodQt8Plj860abN-z3HpR5nt93TaxK2xOfOZ-qPxHk8Rbb6ZxV_a0GCHJdX5HOSnHEDqmrTpXryplpWeBTYfNIWt-3BaFzB3Zx1_GJ31oPzG0BpJYkMKHRM4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aYMKW8_M15pXmGKOf-OqeztPn178cr-r0uPxZHciLe_a5wVDtLhSNSFpFfIcTUl6tqLsEvLeM51hSlGRppfUbLS5s-6auxREWqXQR-N5Gb05e2Rjk21swMYeJlD4TRwXArIyZZa3-RCS4wVyfKiRx2VxkBhBrZqdvBxNuOSR18AYE4FpWOwUWMy_A_q85_yazMFqKiWKMrOLeJ5WTSPTsDjAFEV9JJO8A5jQsnO7eosqF2a78mgSLvSV-_2roU53oSrUF7fpsjYIgkxqQ5TMLiSzclFQ8aXXqBiG-n2Up7vIRdMlekA-5DszK6FI_5brMMnpsvTgakzYEbRTRh-B4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQ0mVdacPstSJl5xyjsAdRDEOGKZLiMkPy8uotTKSOLo3NWWNfINfXITAQnGLAAIUYMK1RqJEA4UtVp6yJ9YT6Fte9NxmiyvKiKh7jbWErmTxcM-UVntmHluqGuPXotRhhi9_Z9jseckevs22Hq7jGwh20Tu4BaGOTD8k-xkW2k_cxX-8KlA3b3IoX72iNGRsLOrF0ZeXVhs-5bFmTwTtg_vfpxev1Oq87hSMJlb-GtNT45iyq9ME1yl0_1y2xpcohUMGZBXrF3ritGnyI4poICouVv3AyqhdEvX1G1WNP5cjs0qb8qpuTvHSizLAVTapTKsYel_KPmwi-NRNaOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=jjG2s7k8-EKiGOSQP_rTyw4W1mwOK3RJSacvNtz50b5T-gLqyMalyL71aUEFjDWy13pTRkwz3HGOTLTqxJWEXc_0vjHfbzdJ5vEJxIAdcrXvbRf1TIvRiiRJe3FvzjTt31gHXWBOiEGW_ta9w1MYoxOrx_Hik7v9A8kUSchfVj5indhcdgP8vfnhhvvUmTbkljVgTTF1SpG1BBPAFq0Q14rVqGPpXkIkRox493qrAfbpiWQRyxZ0sj1_sTMnc70-v0DpmB7uvZLBhyXBPKfK7n8wJWGzuh4X1v6EVE0XDH1BjEeSuVPMRGy9Rs0p6ZCj3V_E9UsRsi_mtJeziKmaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=jjG2s7k8-EKiGOSQP_rTyw4W1mwOK3RJSacvNtz50b5T-gLqyMalyL71aUEFjDWy13pTRkwz3HGOTLTqxJWEXc_0vjHfbzdJ5vEJxIAdcrXvbRf1TIvRiiRJe3FvzjTt31gHXWBOiEGW_ta9w1MYoxOrx_Hik7v9A8kUSchfVj5indhcdgP8vfnhhvvUmTbkljVgTTF1SpG1BBPAFq0Q14rVqGPpXkIkRox493qrAfbpiWQRyxZ0sj1_sTMnc70-v0DpmB7uvZLBhyXBPKfK7n8wJWGzuh4X1v6EVE0XDH1BjEeSuVPMRGy9Rs0p6ZCj3V_E9UsRsi_mtJeziKmaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVtjBMXWzaFwdcEWY5KBefGCOqG8WP0wyoIp0IrXfmTlWlOfAjFDTA2I4J7xpQvgDf5zAMgy98czKU3-mELtkzfSDlvUHFQ7wzAZh2LWwWDEdTZP_dS-zpxnfVgMRrdH0jHkRwX6bfsZzF3c60_08r37B9pTZ_1dSb2_rIvZ6a6SQxGBaX7GoH320mxDL1vjwMNoiX7DUQKoBcikfyxqVpLV9mIWbT2U1qK4omnVjnbvRg71V8gdCTJmbjRC44LDwxLxVLC-7o59KGKgCUwSZlpkONXATxJbIkD9WdBBDbss0Hzx9FlKDKxwws97wZCPksP1NFYb4eDTPlPPmW3xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE6XXiYOJfOUtEcSAnOmAFpkqpH8vWljK7wKoedFK_z7nfspMPFwk7d3hbP1oM5CCZALU-_It733vbxeTnUBNOGkBbofEYCDFjcIO8ZcRSOaVM0qY0LLLdd53Srg8CoYagqOo9b7c9jvXSx7xTZ7Nlr-Po3ZRekxiiurgwEIYhDVhf3AK_Ss5FSC7DrsBBQYRiFFhKqaRqItobCHFOM3F7WSo5QgHUMvM8fvJDnVC2iebZa3mHwwr05pRWxwGMOtrrVzBTW3KR3gUV_Augxay9ahDZsK3htEtifliR5pbdFPb5r1ogESG6rHZA-z8ypO9pgTXV8u4vkHaPbHgbp05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0y8WHBInihz3rnEV8GgfwAB6x63gLKtHEr7Ma_d-kj7k6Qc7JGbsvdK2xg05TznN6EgYRZhngTNWsOybuEird5hOzB4dr67DeO3FxEvJKY8InbS2qz-qxvI4kXe3mM5A1ObUlk3r6T2EqDbeafP8mfyH1jhIiRVMh624b0Oc2QB9CdyAXOtw2VD7KOCZI_KYUphl9H9PMQVdgN9eO9j_VvzjiKOGIQA3q8IXe2d9fBoJJlvRznfs2MrJ-BqcHkeBQ1a5rVNUDrgDsC8KOmICHdNz3MgbrA_SKQyKL75d9KWZrFWNUr2YJP9Ilhwg92-EUZg56FUSlDbDsBaeBXi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=bDqMy3nW74J_h1UPx7GYkEcIj13REViHq0q5IRSidVjuTHtqVM3_oc2VudLnBOq_MaYtjfHnv6X2j1ruaSKTTZlYNAFCS427R8PDdk7oy8Rwz-YNWquU5LVNfQhEavGcQ1vq734RGD_kEGxLbrau8UR_Xj9UoGfPPn2Bw83jn8mVKMs-azWNfWmdkh1NGxCAOFs9bM3GsC6o2CqB-tUlMp1cHxgzLOEvp5RGNwtcOha-btqKdg8UmYqNt1f_R6kC3tq4EBhib38vE_g_8alsKbv1-37amNFBpph-hIGe9wRcwu_feDpQuI94IDPEZCAyi9jsHHH_smTsR5f_pk0kWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=bDqMy3nW74J_h1UPx7GYkEcIj13REViHq0q5IRSidVjuTHtqVM3_oc2VudLnBOq_MaYtjfHnv6X2j1ruaSKTTZlYNAFCS427R8PDdk7oy8Rwz-YNWquU5LVNfQhEavGcQ1vq734RGD_kEGxLbrau8UR_Xj9UoGfPPn2Bw83jn8mVKMs-azWNfWmdkh1NGxCAOFs9bM3GsC6o2CqB-tUlMp1cHxgzLOEvp5RGNwtcOha-btqKdg8UmYqNt1f_R6kC3tq4EBhib38vE_g_8alsKbv1-37amNFBpph-hIGe9wRcwu_feDpQuI94IDPEZCAyi9jsHHH_smTsR5f_pk0kWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sggAWV0rolxcArOKGUDjepJP1VTioQYorVApPLMKIm4XNSkAAgBZcHPyab1nrxU-BuGS6xxWT4-A0sN9VFuQuCJNoKWFmtVDNFqC4lOhlOSXMeviaed-ZnAOltmY_49-snZlPnOjbwvuC94fvzaB2gAdzwPjqtzaE6QwP0xizSIlxt9cDti3NZmseKAqB792_uswZZ4C2UqkcpuzI6PFwhHFyv4LTN7YL33WNYwlTHdePBOLHSQxf13R9AVviT39yTZejTizUfQWfCt_ZYAti2D8-2cfc3YFl_QEHI1YPAxXrH3IKIAK7MwpUlAZa4IUxurpOWLm60uwt9XBmj8cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=dOWxv9ipkaJY1mk-dkfKwkJIHMx6KMWnGA0Rn1Wc90R1Z73rTkF_z4JxsGS-mq0FiQ1lEEX0nvvt6eqyDPgXSWLko_XuQQ4_lvoKBmg8l8O_yEwQ88W0OP5urp4CgSYoPhr6Rpkui4SX1f4Fe-1ySwvMh6iZIN4O1qiopB1b2tSvjYZGQaX56vltZPfHJOwSV-UOtD03KO9PnftZeCNfcJ8mLJhSsBQR9XYpU36QDVb-H_z6YBMu1IQwpBu4ZuffAhgCIBF6xbe15bza8N5I2t-i_aCBupku6m_6I5bbEYqSLLi2jv_KL2piBgO-AwEDmzT1InsmW9XlFbC7sGRUag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=dOWxv9ipkaJY1mk-dkfKwkJIHMx6KMWnGA0Rn1Wc90R1Z73rTkF_z4JxsGS-mq0FiQ1lEEX0nvvt6eqyDPgXSWLko_XuQQ4_lvoKBmg8l8O_yEwQ88W0OP5urp4CgSYoPhr6Rpkui4SX1f4Fe-1ySwvMh6iZIN4O1qiopB1b2tSvjYZGQaX56vltZPfHJOwSV-UOtD03KO9PnftZeCNfcJ8mLJhSsBQR9XYpU36QDVb-H_z6YBMu1IQwpBu4ZuffAhgCIBF6xbe15bza8N5I2t-i_aCBupku6m_6I5bbEYqSLLi2jv_KL2piBgO-AwEDmzT1InsmW9XlFbC7sGRUag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=Q_wX5spnEGcOdetkFYHe9Vdkimw40DFa9MKvPWskwN_5_D_xg233QBw9tD8cD1vQ3MenlPE0jZ-L-ZNYBXz7__ivCJqw9F4ucUBneKcsKSwUZnmDOudnZvtQMvd1f8pb3R62xJD6t7egu-pefwf-VIWEdOFmQ2AUBua8LtKUmc0EpjGGUvYon8vbBZKSDsCnuMxywrjjL8L16426k__8XfmGNWPflLhuo5NfKmzrrj3s9GkgFSQjXlhhEjNzPiuWUxzqfOI3mTTZGSl1E840MwR0YKGn9nZg8-FISnSbaHrIdJlin-KPPIhNzWAkgrh0_h0t9_xgBy9Km3exsqAvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=Q_wX5spnEGcOdetkFYHe9Vdkimw40DFa9MKvPWskwN_5_D_xg233QBw9tD8cD1vQ3MenlPE0jZ-L-ZNYBXz7__ivCJqw9F4ucUBneKcsKSwUZnmDOudnZvtQMvd1f8pb3R62xJD6t7egu-pefwf-VIWEdOFmQ2AUBua8LtKUmc0EpjGGUvYon8vbBZKSDsCnuMxywrjjL8L16426k__8XfmGNWPflLhuo5NfKmzrrj3s9GkgFSQjXlhhEjNzPiuWUxzqfOI3mTTZGSl1E840MwR0YKGn9nZg8-FISnSbaHrIdJlin-KPPIhNzWAkgrh0_h0t9_xgBy9Km3exsqAvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=kSuK5-kpFTtYjX1mrVfaVYxQ1K7BPCaUVh2UAJ3lPSM0-fIBk1ifSOBXJlria1kbwCJLu50KzqrPBFEOPmeND1vf_-jS5UdvqDFmxE8IrPsoypVxeR796En9V8ZvmFbxdgXx7PC9gr07bPdnVnJ6NZRPrXv8ltYZHWdkMOsZyg7t3AS9zfPgpwLNn28ZloczCIX0Hod2ul-RuBXXn75rkbh6cDYlr0G0YOidTqLpAI5Ug4cuJU0uHK04ClGi4iEGZqt3pdmgb6w5HhQmDAg4RR5elwYSLc9vt0X2pypPB0jN2ukl7VP4RmXx09QraAs2ysUUu3IEnhAxHszoB8nJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=kSuK5-kpFTtYjX1mrVfaVYxQ1K7BPCaUVh2UAJ3lPSM0-fIBk1ifSOBXJlria1kbwCJLu50KzqrPBFEOPmeND1vf_-jS5UdvqDFmxE8IrPsoypVxeR796En9V8ZvmFbxdgXx7PC9gr07bPdnVnJ6NZRPrXv8ltYZHWdkMOsZyg7t3AS9zfPgpwLNn28ZloczCIX0Hod2ul-RuBXXn75rkbh6cDYlr0G0YOidTqLpAI5Ug4cuJU0uHK04ClGi4iEGZqt3pdmgb6w5HhQmDAg4RR5elwYSLc9vt0X2pypPB0jN2ukl7VP4RmXx09QraAs2ysUUu3IEnhAxHszoB8nJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBQQ7CAhMk5ctWMJrlJ2oKXJVNGVxEtlLHmWHvxJ_Q0OBRn2i0aZn0ISQgkfTfz8P-aamuwlTPTMA5XTPOp1UkH7J0oDuF5Swt1msbqaTdZ_CmbqqIVg9ZUyYS4XPg3zYQ0po3MAD80SPnCT1lyx1IHirFZql7kUSxQxxD8Av0noYYAZfUhuCvCu7iwRSdl4TpAb-Ki_wALzBg-21HQmOSusKdvsg2_du6zk03MVUhscK-3k_JTzRr9nnb2Et1CiLJ-AdQmh9cbiyMfIWsq0OXuJ-FlfahhIEpnBGz3TP4mO1Hydrrs_wFr68uoa1yWaig9-ZOj1-ZHkBk94tgNm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=gei2v6dAhSG9P3H1Txuvv8RENkidjHYaOMsrJu87rFe9k8cUAj-wK3VKR81NpPLhl8jGGPgYlXUYu0ON11kJQijOsYcYRfRVeG56Xz8Y9IBVmyOoj3TmSnvqXt6fTu6BYxlegzTZaiyyTy4L8JqAJ6sets51C3ItKzJnZ-rzAtyJOfjNNs4jB-ZyXwzWOZNRVkBK60_sO2-8E_Lm5zIwyh5oVv3KXiZ0A9Cr8jyDL0Ewa3p73bcIAlmQuG0KVOeiJ4-9XbfX8jvpWLsIbKwyK2Br7nyd48oiI10TVFxvP53Mi-DWGafbSK3LKnVO7NuW1pzCKHK0AKiDFVQNXLGQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=gei2v6dAhSG9P3H1Txuvv8RENkidjHYaOMsrJu87rFe9k8cUAj-wK3VKR81NpPLhl8jGGPgYlXUYu0ON11kJQijOsYcYRfRVeG56Xz8Y9IBVmyOoj3TmSnvqXt6fTu6BYxlegzTZaiyyTy4L8JqAJ6sets51C3ItKzJnZ-rzAtyJOfjNNs4jB-ZyXwzWOZNRVkBK60_sO2-8E_Lm5zIwyh5oVv3KXiZ0A9Cr8jyDL0Ewa3p73bcIAlmQuG0KVOeiJ4-9XbfX8jvpWLsIbKwyK2Br7nyd48oiI10TVFxvP53Mi-DWGafbSK3LKnVO7NuW1pzCKHK0AKiDFVQNXLGQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDhzA5dmv__muNcI325kA7zIZF68Vq3tgvjAhCH0Bgkg4NHo2aVCKaL599liaHCcbThT_L5YyX03Gj0N9Ge5wkA5uEhyOCBH0xKlYiHIuijj5CnmTZxX7xobWQiKw0xy_eP7REGgOHfn7GCtqS9NDq4Aycefu1VwAMXbQZs7oRapQ_kKvTv33UTA8ipNJci7uvfI3kRJ_wkOXUQz2zIXufLgwrznTufrmJdS7gi0kY0E7G8mjytjFVc32YOmNeTHvIYU954fFcpEsOa1XCtdi8yOCB6TcywTMLnZFYdgg6zQ7QlpXZapqU4jx4HiAnsba4WY1ZNkkca-iuPdtI1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQWnOe03zRFkSYw_aSDkjtBnPICJXNLyvtbA2uDuRr-ttULgUV9cXnaBN2VMEGhAD_D0pWMBbB52DIirtArrawjp1d5Yeif7Mq7bn8OW6H4qajIfKHCKccJ4esEJd724zrlA3amGBF-oxdX96shZ6ZcZowCwSogoYCSzRFRwkNknyxhaLGM_KzZWCDdL6jDVtGFZTa-zx8LAOiRUpVpAS7NDjuUrxc62Uv_2Ej-qA1KMmMIexs6C1dVsefSwB4XNNE7pXXuTn7gOqs4dUCnWwxymnqX8SGAy9_vTvvAydLiBQ9C1N6wD3foHpnbZ-Q2tTs6XsrenGohmvuCDUpPxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ4B6Qj6TM092_3l93vnanC8WTyQrCtB4QSoOSHeE3derggncMh_Gxjjmi9w14qPW9SAsIcVzoYg9INobb3hW8Wrnm2iAM2xvn-uLkqGasIbkTlBW_diTA1EDSQtfVeFQbL-d3yG1LpLjAD4-mNiSHj46ddHh7Y21mPnw0AlN-U5E06FzBZnL33p2xcT-LICLVtQ-vIBx87qVU1Zbs2OY7wZsASG3xNR5ZByEBA2LOynHIcp_Jo08aiUqqEJt4Atk_E34XdeD2oyiobqZuMJg3-W0qHUEoLkeo8eHhmWIbF2G3w9cmndgp03d_Fl2m6ApOZ3VhsLMYo2KmtDQ7T8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM2LUBDKddO8gjXdnP9gwNxdGcieL3PSOHSaHyAKAFmO8ByPxBdO7o2vSnjQhIvrU9ytEGa844hvpCQqzta290OE62u-AK_RsxsVb_ub9D0-s1wDee5qi74DW1bw42wUhiqTMoYxE2zo-3ZoFS3zqc9A2TMSQTVyKZA4xLaJbOKJR9oj86Z_TWhT0-efmOEjt9pZ_FwUjAOpuBNz0p7t1pc0mlm72w12z5jux4z4-oGmNo6kRCL52NMWIEJZg2TA9ASGDZXgnzaIhhjlUixUmohRc3jcYwvF-tDRS7Z6Vq-vz9RGLYXU1dkCtFngxP4U8luDGDG7cuHo-nmnVf0g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ubUYXJVG4-RwBMY8bZR855IOKduvgiSvx_kjsvVlQKXcNBv2_lxLhelkt4clSuJV4pT6BHzyCEek7yOiZFeEdr_0flKQ3uxNildqVE470APQIQsDqQEkxhLPLZ3532zhvBoGzv_uFQCwYG0teHUMfZjckuauV_VwtmVOhRMZ4--jQYVQXXbwI6_V-LpnpMkGf1vCMLK38-Cm__6zjPH9gIAqFpfo7AUWh4_S-GUr19B-kGATV5bA3l87OdMYsGylgIhNxCB5Xi4MT99C_qrkgqwEdEUa9GMG8fgKDb-zN2Fe_yW2rrA6F3aNQlrFTl_ps9QqH6klMzhnib-PvJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-zUTAbiELQ5jJUqVE8fODghzYc1ltmV3AJZ6eGO6c_igZikw3Xa5s8_1k-rXSPRYYYahtXd5K7ynvU1zy4oQpoR6uNmMC0gOar-qrGUsTpj1GuPX7LrfP9KSlRQ7QUSJmXDx28mNZ_C1D_mwGGsJJU0zLiqzapsOdgvY1Zfros-D_N2itzoaQdm5HRbEVaAW6T-qgP4XghXdTq2Do23P7jtKMzW-d0z6KSzk7nKpmPXS3sHWMlnAmsFyWNfbbhXX8k6jst56ff-cN_M6H8SlstbDsF1H_f0GVBmFbZQjBlNjwVJfHf0LyjT9hlslx4G8Q4mZOrd16KSsdcxzCiB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=OXHaXu3XAE0fSlKkH3B84XhE6P6KPj9n3p8GgpJDVxUwd_mQqjOfJJ94bNVC9MC83t2zE22yx3JxSncJAdKKS7SmDIJ-J4QH1sjymT91keDqGvi8e7Xa-rF3LD-I44EiY_S3wRuv-w7xdwevvzG37u7hK5Tjj3Dsjxn6USmJUzsiF5iJqspga2y1DVvtgwQ4-ZQRb0LsnBSS7v568ho3TXuF1muL6oh0646yy5kcWgceFungbQL4an76cdjidRI3U0eYs2r90K8O0ONG2pWUqlKTzlWFJbEUGNc0A36OmGHX53U_C-FK3cQiXis32MCCfSBlnQf2sLXZIZYyhIxsSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=OXHaXu3XAE0fSlKkH3B84XhE6P6KPj9n3p8GgpJDVxUwd_mQqjOfJJ94bNVC9MC83t2zE22yx3JxSncJAdKKS7SmDIJ-J4QH1sjymT91keDqGvi8e7Xa-rF3LD-I44EiY_S3wRuv-w7xdwevvzG37u7hK5Tjj3Dsjxn6USmJUzsiF5iJqspga2y1DVvtgwQ4-ZQRb0LsnBSS7v568ho3TXuF1muL6oh0646yy5kcWgceFungbQL4an76cdjidRI3U0eYs2r90K8O0ONG2pWUqlKTzlWFJbEUGNc0A36OmGHX53U_C-FK3cQiXis32MCCfSBlnQf2sLXZIZYyhIxsSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=B709g2DJKe_BgSzf5dj7vAThSOYCYp7E_g2XfygRbfZdfZrOeO93-M5aE22L3PzExoxdtMa0VXsRaRF7qvigN5weVHnkE5KclMg7deru5RZyPVLHUnHyyZlNqDL-jFcBdAFe9Ux1SrjGO1_PRrk1TApgEsWURskB76IiOPe7NtYHDUdh1pcPJ1w9g_bLOz822pSeJLUbvEZ0x7uR7kPF0QqhCa_bQvUf149HYZfUAgTqpDJBj10L9qiRaiEgaSm2AT0NT7oXDE3KY3yP2itnpf0Ij0PdG9norkBHRMv92k4Ee8kLBcylCNZhfuVbmtB5KpZVwrJudrcco62LNZEhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=B709g2DJKe_BgSzf5dj7vAThSOYCYp7E_g2XfygRbfZdfZrOeO93-M5aE22L3PzExoxdtMa0VXsRaRF7qvigN5weVHnkE5KclMg7deru5RZyPVLHUnHyyZlNqDL-jFcBdAFe9Ux1SrjGO1_PRrk1TApgEsWURskB76IiOPe7NtYHDUdh1pcPJ1w9g_bLOz822pSeJLUbvEZ0x7uR7kPF0QqhCa_bQvUf149HYZfUAgTqpDJBj10L9qiRaiEgaSm2AT0NT7oXDE3KY3yP2itnpf0Ij0PdG9norkBHRMv92k4Ee8kLBcylCNZhfuVbmtB5KpZVwrJudrcco62LNZEhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=D3cXWJGQUNVQxsKFJkQ9txWJYtW1erAvcnSOnG-aoffMPgOFYxm02scduQQfaSsE6U1la7vV6wCl1uNyc90gaQG5oMtNCufm8tB7uWyyXpjM_h_VmXYZU1cX2MwGxWjCVGfBcn_muMohuqMbH9T2ilprvKp20ip0NtE4GABMlL5IACJRwgsojQIU6m3qEKIQ5hHwBNaKg584i0cXY7PXTAhOaI7aFSKYSv9ge3vqdP9BpanAVXXnsSxlGd-_uWrb9_V0L96IqlSpwPs5AF8VXyTaoliHBziFpHGSHKDSE3SfTiAZsiyOX-dhT6_ac_c0vxGRW7WBNSjpbMXnaj1mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=D3cXWJGQUNVQxsKFJkQ9txWJYtW1erAvcnSOnG-aoffMPgOFYxm02scduQQfaSsE6U1la7vV6wCl1uNyc90gaQG5oMtNCufm8tB7uWyyXpjM_h_VmXYZU1cX2MwGxWjCVGfBcn_muMohuqMbH9T2ilprvKp20ip0NtE4GABMlL5IACJRwgsojQIU6m3qEKIQ5hHwBNaKg584i0cXY7PXTAhOaI7aFSKYSv9ge3vqdP9BpanAVXXnsSxlGd-_uWrb9_V0L96IqlSpwPs5AF8VXyTaoliHBziFpHGSHKDSE3SfTiAZsiyOX-dhT6_ac_c0vxGRW7WBNSjpbMXnaj1mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnoIqTxbRdcyLaJdMol_rEsCkIMvKJ7p6KrtZAl8IrCm4g4VMQ8BMBuIZs28WgGGNt7vDkYOICpIMSSE35MNAOGPwdItejxul54K300d9olX_fmMQHQX3zxg29w2KpCUFMmnnZTpPIQyXHrL6VLryRpzUZDd3iPHJ1IBUxOspVwPJeJ_Hlyzyjpgn450KmENwm_i9P8ZHoSbi-w2V_1gAh3-ZccAzRGCVfyDFYuvNiV0qb8uYMCOil7a5gi24G148Nwo9bfKeiyn85myJCoTKy-pnlZYhUqjO_gja4u-xuySVcZEpLqMohYwiCI64j2VA9qL00kU2bS0tDzqXGAFpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8TkDXS9Sd-77RK7wFLOCh8rRo1BH4LkTEBhgXQb48Jqh9Uv17wxKN_iCC3amvDm4Xh26WZIs0v2ywMofG20l1Xhailbk5uMYdT1REXf2EV6g7KgnzKdXXK9actHvDW37tyJNHZsl7NAFs9nt2ktYd6GMSvJziRHcM6Zcea7_xQ438kMDkC_OpR31vDQrR4dMwj1kClA4YBqMvzXxgSB2hRPtt46f4TIQtiOQDWAYHeEl2TkaysDc5KqgLt-bD7UUXE3ZHTCMMkJ4waedNTrVWNI5tOUXsI5WP2N0SbL25f-aIGNuqgraPuOg5Y5p8kBQhoASJMZJpZC63Km_eIp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=nTD-wGGxIprDCsPeLte3CJjhPyCY5JbZ0C3-GT0KILg2br9Jyh5th_BW7DY9iRT6Op7N5ItA57KUNgAH7Xq_nP5TUuSJOccGm8pxMFtpPtj8L1MyX7jhoEImeE82Hyau5v-yTJwgyfkFfRdEfoS0vZMNqfabW2jlZQCQ9yLWDRxFFmTT8Gve1QfgYQyNzElwJLgSt96-ne4GN5KC-SaswYmTNoz0BdgxqCdQn3MJtqnFbngf6AN2oGanuVNh366GyEzLXhDyhnX7jWXbaAgyifFV0GScKx_Ig819dZoteu1RRwLfDxD9bQ3sXUmoIxN0PAb8ng6v63VJWRSq1b5rIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=nTD-wGGxIprDCsPeLte3CJjhPyCY5JbZ0C3-GT0KILg2br9Jyh5th_BW7DY9iRT6Op7N5ItA57KUNgAH7Xq_nP5TUuSJOccGm8pxMFtpPtj8L1MyX7jhoEImeE82Hyau5v-yTJwgyfkFfRdEfoS0vZMNqfabW2jlZQCQ9yLWDRxFFmTT8Gve1QfgYQyNzElwJLgSt96-ne4GN5KC-SaswYmTNoz0BdgxqCdQn3MJtqnFbngf6AN2oGanuVNh366GyEzLXhDyhnX7jWXbaAgyifFV0GScKx_Ig819dZoteu1RRwLfDxD9bQ3sXUmoIxN0PAb8ng6v63VJWRSq1b5rIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZI7bvThx96srmbwdeAC771E0Ds0Bk9fbUwQwq2lEU6KvIdKtfenJ-UhpdJNwulMH4b51ymJdm6jL-nUmVSVrps9Z7XPLIipLQIP9STToTHvpfHYB1Wm3WYCB_1AMXPBxzsQYQ6rIZNrBT4zFf_Ka7Dti67HPVznxxnB8Dff6uYcY053Qo1vUjF2goDvXKug9oCA5AyyI3dG66IWubICyIBjEnEO_jaMekHZNQMn0plKMNU1mlPfjqtt5jUOv6x2KVeyeHdVQDQENWNWEtKEuZ9duGqe4Ms7LnKyrBzKsAAGdHjwurl_grzM9ce5Cl_7Tk1d7FUxVeRwRGhjZgvGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=f9LOZlQ_gjhRyk25p6KeedZ0LmtStqcP3tB1ziHmVvKAHWaPdEzA9VjoJp2dGO3uRbMIFgWPf09DxjjftnAQWhjfW38cGsLwgQaxnzEZAGcZYajF-o622vcdQBrgM5HNLBMaIfU90qBsAwSB4ULuOak0uIAHGxjFYPPQcRhYGZXGEGTqHyPQocqVrEo2yuofDBcCiWzpizAFa8epFGEYC6H8J_MJK5FIiku-f1sZyNjNAHNuAfpcirXYDarfLJ4TSKh9OlhtoJ7uhcHISe55a4-aVrdohgoOSFIbxVl6l5h5Y7eklVizTZG0JPaxDyfRRDHk5x9WsH9FotUNqtLTpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=f9LOZlQ_gjhRyk25p6KeedZ0LmtStqcP3tB1ziHmVvKAHWaPdEzA9VjoJp2dGO3uRbMIFgWPf09DxjjftnAQWhjfW38cGsLwgQaxnzEZAGcZYajF-o622vcdQBrgM5HNLBMaIfU90qBsAwSB4ULuOak0uIAHGxjFYPPQcRhYGZXGEGTqHyPQocqVrEo2yuofDBcCiWzpizAFa8epFGEYC6H8J_MJK5FIiku-f1sZyNjNAHNuAfpcirXYDarfLJ4TSKh9OlhtoJ7uhcHISe55a4-aVrdohgoOSFIbxVl6l5h5Y7eklVizTZG0JPaxDyfRRDHk5x9WsH9FotUNqtLTpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=PC3WCK4N6aRWeYeyY0vCFDDFJzdP2-nz82c-MQvpglKTrfQVROOvbBunhi85nmcZZubqyW5XsHjkOTKfWyIPAI3JRiUpb9KN81WdxhT-10L5HIwUujMGZNfSh7zk5ynzI9djeBInjVYWuOeDEMf4Ky3KKI5d9W0cYyLa1JO9A28e_-JX-AI9ke5mE2QpacLR9l7ZaBpcDT2478xqwtAEs3dMp9nCL-gN2Mwce6DsPuaAS_btWx6UJzZ9jcm093TQHEwWNvEtYGqpx92sgjwhC4DhGxBW5A3DYIN-uxMP6aAX6EzmUKD3Oq5vujo-6Ul8lhdC6trAiD8CEeqnYT9Qcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=PC3WCK4N6aRWeYeyY0vCFDDFJzdP2-nz82c-MQvpglKTrfQVROOvbBunhi85nmcZZubqyW5XsHjkOTKfWyIPAI3JRiUpb9KN81WdxhT-10L5HIwUujMGZNfSh7zk5ynzI9djeBInjVYWuOeDEMf4Ky3KKI5d9W0cYyLa1JO9A28e_-JX-AI9ke5mE2QpacLR9l7ZaBpcDT2478xqwtAEs3dMp9nCL-gN2Mwce6DsPuaAS_btWx6UJzZ9jcm093TQHEwWNvEtYGqpx92sgjwhC4DhGxBW5A3DYIN-uxMP6aAX6EzmUKD3Oq5vujo-6Ul8lhdC6trAiD8CEeqnYT9Qcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=ColWzDV13SpZhvdKRnVYgDjD9zGm4SEC9263feun6Xjb_buzZ5Ieb3KHReyPpUOwFy2CXbRX0b3zEzRikLuv_zbMbYDhZftAgtxwtXKVRdMQ-qqGIzaN3lE1VlFlC-_ldxoRD-V-FtTjw5he2zqm190n4MGgwbGySfMRe5oIVoqoKW6xLpf7A88nobgFvIfKWSY8YZWYYWauqAhOhh2n4iAFazkF0gBHG42GK2n1whG7KjyOb7-MxyTkKr6ySn9mVti1aCEUwfigxoOQ_-xRVR7NVLGEnCALuif_FzSqgIpBnksJdqsqBI3lFlc8Kx17uE0PI0b7ZY_KJrcvk5OBpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=ColWzDV13SpZhvdKRnVYgDjD9zGm4SEC9263feun6Xjb_buzZ5Ieb3KHReyPpUOwFy2CXbRX0b3zEzRikLuv_zbMbYDhZftAgtxwtXKVRdMQ-qqGIzaN3lE1VlFlC-_ldxoRD-V-FtTjw5he2zqm190n4MGgwbGySfMRe5oIVoqoKW6xLpf7A88nobgFvIfKWSY8YZWYYWauqAhOhh2n4iAFazkF0gBHG42GK2n1whG7KjyOb7-MxyTkKr6ySn9mVti1aCEUwfigxoOQ_-xRVR7NVLGEnCALuif_FzSqgIpBnksJdqsqBI3lFlc8Kx17uE0PI0b7ZY_KJrcvk5OBpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=qV3IxGrCzP-ni1Ony7iVBSDqF7eKf1JTv-8sINmpPwJnzUCsolxnd6CyKwBii_u0F4OkOerLD3Au-Gp_NUAaG8FggK9b4EJKMknGt3F90uHhQZrn3e5uaK2ppsoU7Mx393pR3fEWUThxFUs7OZJ7iBCKbRangaHcnqCaPPFroCvP6u3afZ0D_1ZLCPbFmk3ITHwbgIbHuD7FiJhoycmYgEZS60AYRlFwrvqW52zI4RiqopFtmrVcJg9QIUMG5WJZw2B_Yxa8fJyEVlcEsH1jc5VJzK8R2spKtH3NbLljKEwFDNpzG8Qy8Fbjd5w1ps7fp6PDgfICsg4V60ac-PZ5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=qV3IxGrCzP-ni1Ony7iVBSDqF7eKf1JTv-8sINmpPwJnzUCsolxnd6CyKwBii_u0F4OkOerLD3Au-Gp_NUAaG8FggK9b4EJKMknGt3F90uHhQZrn3e5uaK2ppsoU7Mx393pR3fEWUThxFUs7OZJ7iBCKbRangaHcnqCaPPFroCvP6u3afZ0D_1ZLCPbFmk3ITHwbgIbHuD7FiJhoycmYgEZS60AYRlFwrvqW52zI4RiqopFtmrVcJg9QIUMG5WJZw2B_Yxa8fJyEVlcEsH1jc5VJzK8R2spKtH3NbLljKEwFDNpzG8Qy8Fbjd5w1ps7fp6PDgfICsg4V60ac-PZ5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=GvI5kx3Wsil1XRpfNh0XgqxB6T5Knt7B1mUk-W9naJByjKwkjpBD8CAmjdBpGA2qtopwJh64V_LxQIGAiBvQSj0Rh4F0Lbb3I7OYfIt3evfU_z_M5CqyqRF_E9dGGBZzbHA49mHiqK3Mm2-_M8jkI8-G07xqYR52slEvUyswVZEzLPJO4bhTBdXbkNRYmd2F2AORKlJeGgLv2YKZInUmDJXX5UPBi25P7I41-oZmPUOtk9qdz3db6EQ4kX3RdHbj-_cOuJkjC5Y-2yoTS7hsRIcmRHivGO9NBi_ziIueQveeobLrAKfgWHNtDvRwdB5dqTRIrey2CHvniN-9gPEPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=GvI5kx3Wsil1XRpfNh0XgqxB6T5Knt7B1mUk-W9naJByjKwkjpBD8CAmjdBpGA2qtopwJh64V_LxQIGAiBvQSj0Rh4F0Lbb3I7OYfIt3evfU_z_M5CqyqRF_E9dGGBZzbHA49mHiqK3Mm2-_M8jkI8-G07xqYR52slEvUyswVZEzLPJO4bhTBdXbkNRYmd2F2AORKlJeGgLv2YKZInUmDJXX5UPBi25P7I41-oZmPUOtk9qdz3db6EQ4kX3RdHbj-_cOuJkjC5Y-2yoTS7hsRIcmRHivGO9NBi_ziIueQveeobLrAKfgWHNtDvRwdB5dqTRIrey2CHvniN-9gPEPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdSiTNn1mIoF7YTAWG59CUuR_UuYEj8nM-EDyXy10VjSckS4nclbyeM8moTu1dQQ4wUq-2uOOrgP5t8u3JMO6TsCXM-tAC1mbPtJa4SKKbXT-GNZGIjxDzrdgs5RJBwiANbsmGXAbSP4vb96nfKWdSfvTxsvLaEP-Jz6gIhsNzdOFePaZPrijRfOYUYEH1s0yWauLuuZ0vJPEij0lnnX4uKc5RRpkn5YJLBIy7vR0ZeyKzYXXF6EazP6phZMjKkAHnPr28-Xd3O_qDq0dsYPxvvC6d3PGIiG5vi1wQHbj0Qa-MSEO5KDTniZpYDCqVXra6ruPjApq3fQv8D9L76O7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=QZ-JSadfCZYYOSGaysEsYR4KIov7X0y3Arno1VOZU9Z9HGnlZzY--Mvmwy1U79HAU57jIEJgkl-vixCt9ptmyM34x7XbwZexbzmPtRvpwyMVGEKKAd1YoJQ6Jfcb5DUng2LvqhVN2Su96ROEhVWI7Ge_YpQ6Roy4GNwMm_0nmsqQvzGxv2kNmS7W89DqcheV51BPtvmSBtuuzYGQYB5IfbUstAOBkS88yKwmRUM4jnJaBu-oh9TpnHkVbK62LjDm_eQVM2dgwTBg29dp-PGqXUCr3OFbruAcxBeHTR-H0jC7upIBiTjMayWkj81KJx-zLFP6ikVrEwUyAKyn3oWHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=QZ-JSadfCZYYOSGaysEsYR4KIov7X0y3Arno1VOZU9Z9HGnlZzY--Mvmwy1U79HAU57jIEJgkl-vixCt9ptmyM34x7XbwZexbzmPtRvpwyMVGEKKAd1YoJQ6Jfcb5DUng2LvqhVN2Su96ROEhVWI7Ge_YpQ6Roy4GNwMm_0nmsqQvzGxv2kNmS7W89DqcheV51BPtvmSBtuuzYGQYB5IfbUstAOBkS88yKwmRUM4jnJaBu-oh9TpnHkVbK62LjDm_eQVM2dgwTBg29dp-PGqXUCr3OFbruAcxBeHTR-H0jC7upIBiTjMayWkj81KJx-zLFP6ikVrEwUyAKyn3oWHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
