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
<img src="https://cdn5.telesco.pe/file/pDL0E12lylfR7sm5ETUI21Ip7F8QQKI51pFHdy_ibHNW578jEdUeyJM-eKHGqnJZUo3yn__hSIR1lXA9BMTVBnZAOGR_Y2Sx-3waRg3SMzm9bysaC0QiBq3u8uO5RqpUmW-NJVc1nOTmFm35fnojqYuueAHE7laFLbuhguPkZxpYKjeDfWAb8XebhC3XyFc2wNOtt8IKqtIIfumhZXnOquL8bxW1Ys687WkKEKbA-G4jaQQrC9rXQPyYddnKIqQEfIhrTpBkik3vRS-cCDplYxPkwmvKscbkzkQrNlwY4rFEvI41h8TN4_EnwxyeFG7kDKI_TdEHLFAtIcA3l4jtfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 385K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
<hr>

<div class="tg-post" id="msg-108384">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoNlAYHQzc9MEBMUjR2v8qS3OArRLtaoUOH8iNTjjjzH357OQRYWpwWjzje_3Sfyjl9Xw-gemyv6G5woYDYnI_W3A2pG0rN3SCeMGs5HHrNLRyLk_kY8w--kqYU7PVGGnrNedsuO4oNWBCTeZxNp2riesaUbe47RQ2NYGLJkaa9Spgl9VcSVAs2SE_zc3nEuNwFDBDwE6XCpMrFbTbtuaWRpfK_jx9jKi6wr4D6w2gg_2IKHcsXJVWwa9uu-a6CIfBRuG6BZl6_uJBzns63rth54mc_fCd7nYI3K71j6rM96M-Yvgqr1QLLNMwyijj2XMdgOApQl837708FHRwIZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇺
لیست بارسلونا برای بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/Futball180TV/108384" target="_blank">📅 11:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108383">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDm0mFeTwSN-Toje_kKW2oHIXJ5vufQkLGvBElF7QzXRpp2XdSXSbnEYmfukeNreuQWAeG4Jg98huM9hT-VSTeUgcRjnK2uAjqDQ9Znn-sFr_PKIAKhSMj2JlJyNM4IuM0TzWLOLC8ZTj0xak6xgIVpoIUALAkLarJciZtnncjGyoMnLXBeu-dUtRH6AljsVrfkBtoWnBZ-IjdxLj0H0x0zmqiVk_gQ36OzdnhCpqDPFATyFdsuEEQe9dAr-mO84verLYlLntbpsJyvD6rqsL6K2ycKLrrA9XIGgYfSqwgar664pJwrGRcve_LYjFZ6NryEoxovRoUyxldQUvhgpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر روز بازی استقلال مقابل الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/Futball180TV/108383" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108382">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/Futball180TV/108382" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108381">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLh9ruKfovcfYCTbIWYOCkiUdcmAk3iUOC6VBCQXJ6mYCjLu6pD8S8HGnsSW-OEbTnnuACneuByg5760MskQqmMqQ3lDVLVGisIFb-T0eQBUjHzCWUhCDAK-uTPz-Pga9VoTLYxWeOzKGz3eym6nziKf0kUIZ-I18iefky4wyseTtzaZIP58MLiHYcunSAuixMtgDPjLmwJiX29vm0d0ismFh7CW6ZfE004ocst1wrLQtPFCPjl3nXxRI9fr2A_cfE0n1XW41bXIBbU656XYO9eMR0Z7RuOU4yBI6Xg8MG75KJ1P4RtYRmsabLD7zbykvWn7Dlv6q6VYUFxp-Xn2Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/Futball180TV/108381" target="_blank">📅 11:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108380">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
‼️
🇮🇷
خداداد عزیزی: اگه دفعه بعدی مجوز پرواز مستقیم به عمان نگیریم، از ادامه حضور در‌ آسیا انصراف میدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/108380" target="_blank">📅 10:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108379">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b833840a70.mp4?token=JvdGjZPa0exVnE_gkIxzXln7bMxXW1idvGjS5tJ0vnB6RN0pYtv7BrVwG_CKpUgwgZ8fisTbop2VBgvvR8DZU79d0q0tBXLOxOGKPsQLKw2a7Dxj3kaoSQ8M4qnDeMQBe2Ty4miJx6FNmpdbk3CK-0rrJjlpoOVv3mTiIEHKDlixEhqY9Ne-Dy5w2zJm8uLZcCIkmpFEALUV0M94OW01yelagqDMXLf7hsliEbqtBMAUS34mjbMmWMTNds-oyNDJ8-Mb74LhFdIsF_5xm5KaMcAA-Xv1r6zX-TsPa3XDpFh7iq4RzACOEIVItqXQfzPblsGrt-oRI2DK8peO6ujGJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b833840a70.mp4?token=JvdGjZPa0exVnE_gkIxzXln7bMxXW1idvGjS5tJ0vnB6RN0pYtv7BrVwG_CKpUgwgZ8fisTbop2VBgvvR8DZU79d0q0tBXLOxOGKPsQLKw2a7Dxj3kaoSQ8M4qnDeMQBe2Ty4miJx6FNmpdbk3CK-0rrJjlpoOVv3mTiIEHKDlixEhqY9Ne-Dy5w2zJm8uLZcCIkmpFEALUV0M94OW01yelagqDMXLf7hsliEbqtBMAUS34mjbMmWMTNds-oyNDJ8-Mb74LhFdIsF_5xm5KaMcAA-Xv1r6zX-TsPa3XDpFh7iq4RzACOEIVItqXQfzPblsGrt-oRI2DK8peO6ujGJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇰🇷
گفتگوی رئیس اتاق بازرگانی کاشان و معاون وزیر:
فرش راوند سال ۱۳۵۲ از کره جنوبی کارگر داشت. ما سال ۵۲-۵۳ تکنولوژی‌مون از کره بالاتر بود. وقتی هیوندای اون سال ۶ هزارتا خودرو تولید می‌کرد، ایران ناسیونال داشت ۶۰ هزارتا تولید می‌کرد. ما اون سال ذوب‌آهن‌مون از شرکت پوسکو کره که الان شده بهترین فولادساز دنیا با اختلاف بهتر بود، الان ذوب‌آهن نابود شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/108379" target="_blank">📅 10:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108378">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8cwgE1cN8pxSjEpnOhJYRqQMt4whQmydwaDkmNoldQrFcdeSxROnc-tLoO5k8zv51i_YCRLZpDYtJOOukTACRI7HE4CBMc4RirxyHOOYMxYfWH_ilQouRbMnhUxAnqh7pQI4UMaU53kTx2oZuMRoJFnl-BAKwVSROYvajnxUfll62FM9lJaCV-s31rR0wACq3l89-WCLRTlEVX7b21y8QC8iCK-Z25CFsCBa6qLPs2p9bARTsTwFBLdzemfwkKSq2m1WHkB3N7DSd9UEl-Zw3zZEyICUiXZYQ3NcLsKeOKpKVziM0jsAVPHKgs78ZMH1MZ7HL-UTZhfJRtaq5cmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه قدرت خرید ۱۰۰هزار واحد پول ایران و امارات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/Futball180TV/108378" target="_blank">📅 09:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108377">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c44921ed.mp4?token=c7WdJLajoYP9_4_lhfTJpgAq4PS5SglPv9ywSnresZV5ikF2DYQyb8OkffNJipf-dATTl3rqXaK86EFDoT8POrNgDpP908vcLh5A8nCpxJVa2z0xRAa4_k94-rLjBXAiFC29hsT7laVcCZGuKkOFbXr-_5rdswZkZvI8ZmBWS5KsboX8LwLPc9P-Up59pwzxNIGzr2DEItNOgxR5swG9cnSPCAgDp4i8wVumP_4HICywiEEYoz7dn_38-bzG2hoo-Bfm9jIqPbMRtFu0xj7IiNy-pKKbvxDxvgfotRbk2NGUSNo9T2pOxY8hDiywd1UFVx5X5IO8g16hsK_RAvwjtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c44921ed.mp4?token=c7WdJLajoYP9_4_lhfTJpgAq4PS5SglPv9ywSnresZV5ikF2DYQyb8OkffNJipf-dATTl3rqXaK86EFDoT8POrNgDpP908vcLh5A8nCpxJVa2z0xRAa4_k94-rLjBXAiFC29hsT7laVcCZGuKkOFbXr-_5rdswZkZvI8ZmBWS5KsboX8LwLPc9P-Up59pwzxNIGzr2DEItNOgxR5swG9cnSPCAgDp4i8wVumP_4HICywiEEYoz7dn_38-bzG2hoo-Bfm9jIqPbMRtFu0xj7IiNy-pKKbvxDxvgfotRbk2NGUSNo9T2pOxY8hDiywd1UFVx5X5IO8g16hsK_RAvwjtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان عصرِ مسی-رونالدو.
💔
😭
شروع عصرِ یامال-اولیسه؟
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/108377" target="_blank">📅 09:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108376">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6ef29c07.mp4?token=ZaL5v6TNa6T-8GpKEt2W0gmNwLpXsyZKh17mLddHGt60oYj7SQ5E08NqLH9d_8dqSEAA2AH4xzxHp0GBtvYv_cuF7bil4OSSNn_5LfdW84rEA9Z9erTmSW5Ik3gT7UM8RuDEyBe59YhveE1rChuIUfRfzTOcY5VckzeyTFggINcQU4zP_eZaIdzTolZVjSnwQJRJiYxPySM7L0kY9dPnTMDd57hUkqNEohT3KyEe05KricMidRr5vQZEbbGBpmSu1VnDETWbLUehcvBZ-tlRlmBI4LyGIi3YOm_S_ljXiCyV4qfBy5cZKehIiyiOATh6wxLaU99d6boYSY52fh1fGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6ef29c07.mp4?token=ZaL5v6TNa6T-8GpKEt2W0gmNwLpXsyZKh17mLddHGt60oYj7SQ5E08NqLH9d_8dqSEAA2AH4xzxHp0GBtvYv_cuF7bil4OSSNn_5LfdW84rEA9Z9erTmSW5Ik3gT7UM8RuDEyBe59YhveE1rChuIUfRfzTOcY5VckzeyTFggINcQU4zP_eZaIdzTolZVjSnwQJRJiYxPySM7L0kY9dPnTMDd57hUkqNEohT3KyEe05KricMidRr5vQZEbbGBpmSu1VnDETWbLUehcvBZ-tlRlmBI4LyGIi3YOm_S_ljXiCyV4qfBy5cZKehIiyiOATh6wxLaU99d6boYSY52fh1fGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
ویدیو جالب از آرزوی سلامتی کودکان جنوب کشور برای آسانی ستاره استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/Futball180TV/108376" target="_blank">📅 09:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108375">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری شدید پس از بازی دیشب سیتی و لیورپول که با دخالت خشن پلیس همراه شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/Futball180TV/108375" target="_blank">📅 08:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108374">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108374" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108373">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjRcbMdyqJfub4MHPGk6V7YO2rmcK8uHEFRZmeJ8IgK2mv_fzjL8sZOPG-IqsGP8XgDhhXGS-me4DjKf9JoOLd1Di7WoCABlaegYY1HxV7M1exWjj2JqE_pUG0yKeNDapgrxPURnOA_-EQt_-i3KOAbGe1tdOdfGRlmRBgrmw61FuKNKwebnpeTyGIIGbLbZjKgq6KKoSCp_yElUNehfq5ohi2GjcLfzpjX8SONTzxuNBx-S2HNV5El5CY-mOlxASHaBoWEHjHyVhKLmdS8qh3jIsy9g4Npetb3PvV20jZ5uB9Z-C6YSgYJ8SnsUU6LzZ5mvotC48jFmZnzfroO_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108373" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108372">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108372" target="_blank">📅 01:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108371">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Anfm-1TNnVIDxp686e6gWqFWHZZB-s2GJNqqIF3--WxDPr79O1EXuwEvzy0wPuRVXZwVKrbEah0Y0XzfVOyTAkt4x8lP2FoEcFEXw-woZwxfqamoBfKs9rzLkK3Xlb851zuO_jAaIl5HUEsrnuFQqw0NPGjmdXMM1iGEWH5O73R3YsheE2Yry8VWC5JrqnHKFnOMOBh1O6wrziXms8ubsk82RTyzTWRI6dhYK8fpbNYOEwmHbdpRsSIpiE1pRbtm-cDH1hEd7FI1fAEul0okQicdOgB-g0oxkqgS6t7KeSh-zydW0fFrB9ZC5j5ApSi59j-iYrZjyAHfz4XWHurvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🇮🇷
📱
استوری یاسر آسانی خطاب به حبیب فرعباسی: داداش رقیبت برات پیدا شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108371" target="_blank">📅 01:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108370">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-ocOfQ66c07G13d9RyE_w4OWlVA5qbW6LIA50Oi1yOpvalE5GxmXSYoG2lYwji5oI0FJHjXoQc-4b4l0a8RS_GNQfBkIbkYWYBxq8DMMv9m1JpNiZYZskuWHtVSOi9wXXVKUfSBIszgqvR-PXpMQydje47WHPrK2J_10zrgtkxdyzGgyXIQURven17emLB7i4QBMzBYSoHHqm_uUWnqnJc_1TUAtvSpXjwmI2VgcI_y1koZRJXxF6XCHVac8OtBEcBu2h8JFCKVnbJuwYOeR53gepfzIsrll_BsI3i4Ih-z1FkLbFjFIgtzlmJKSESV-nOchqxBGtYbDlB3SIAa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
حجت‌کریمی مدیرعامل تراکتور
: زنوزی با وقت و پولی که برای بیرانوند گذاشت میتونست ۱۰ تا کارخونه جدید بزنه ولی یه آدم بیشعور فکر میکنه همه‌چیز پوله و اینجوری تیم رو به حاشیه میبره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108370" target="_blank">📅 00:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108369">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjQpMty_Pqg9M3jg-8Kk4pbYcGME62VE2aIzR9V9J2A-MD9Tk9ijPxQ9K_sl8XOnLXYTqwYI7Yq0shhTURuPi8aBu1RzHDl58rbdyk6t7Soga3_fINZc2TAn7-fpwQqwRnSGYD2f2s4WTDBRSvYlfsJgSdk2miFNDECC2ryeIDWNZcDPZdIrOpXsl9RTzNbDfOgajrIAWiWVDbHh8yuLUB4j1EXcnL-X-EkP1tdlP8r1O3SrVdgKDV0hxxa0X6hiUKfEnt_b6ckaLok5Fnx4R5cAkJuH6RtustKRhGEhFA7RgsiyfnbpbQYw6Dqlbm3YvtWmkUO-paIgoSx6nMOFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تصویری از یاسر‌آسانی در تمرین امشب استقلال پیش از بازی با الغرافه قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108369" target="_blank">📅 00:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108368">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
⚠️
لحظه اصابت موشک حوثی‌های یمن به ترمینال شماره ۳ فرودگاه ملک خالد ریاض که روز گذشته موجب کشته شدن ۱۳ نفر و زخمی شدن بیش از ۳۰۰ نفر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108368" target="_blank">📅 00:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108367">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108367" target="_blank">📅 23:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108366" target="_blank">📅 22:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNpbtvCYktoSY9EZUxP3aIxXObBczPlGT14-IZlftZupYBAW_jPSdqH36txfoimnfq3VTdhlWzUMBMF8JN_R0UtM0p-iVzrsR1wlNR5B2GS49vA2YaMd0efZw6zoagV1hg1K014Q02e2CI-WzlBkkCdvLeXQT2ZW076WxUi9Z3Xd8zF_2FtzlaE9TJEv3FYvCNwApKNIsFFvaUzbyBuGBWUL4xcEZdq12G9T-HkDSSPpLyiV97CMSL-wJzgWXXcv5lnXEDPBr9hbjJuIiLLbnrDbLbe3fmVGsKa7PnRWDFz6-mxhydVMy67lXDt5k1cEky5FGfoJwhhIkA9Eaaqp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
محمدرضا زنوزی مالک تراکتور: از طریق فیفا و CAS پیگیری خواهیم کرد که چرا استقلال با پرواز مستقیم راهی قطر شد ولی تیم ما با ۱۸ ساعت سفر به عمان رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108365" target="_blank">📅 22:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goliqZEgSZqPb3SYZtHaSuoQpeiOj6H2Dz_jLF0-oAE0JO3QNUzkOdacQpkc9Gp4qtQ90vx6gTbYhzHyM69WO_vmZ515QOAn1KbqRgC09QpxgPTYru0lMsqYm2nzyhBKDIZ-abzGb4VPjp4ieDhyI4ILVQa81cCDRrL9_-czc7XTBp1GxQIWv86OyzJIjyisazHKm44T8Rgk2pGJVf4QhPjfTQSRWKs3nX5ZfJEwUBtZpqdu73QxtTtB6G49GtHpmxPF7tZaJc6qd_FrPZ145t_A2en8ronMYhC5ogAQtP1dCJANEmLVg56aTtXN0cYLBADFlNsIgpZxqzKjV60DhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🇪🇸
🇹🇷
ترکیب بارسا اخرین بار جلو گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108364" target="_blank">📅 22:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108363">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqdayfDZRD4eFx6KR-ienHeAej0FnyYblC6dwLiBeNxjmexoBSkwAB0AdoPZHj9fh1zziqYfQrYw-QXXvkeYct0C-Oi71ApiQ7e7Ntp-Y15joIqPO-cyMkQ9ReeTtED8BSYjXHngHbr7Su9mSxNvOum-XZnPnkLzkj8nRfIXhy8wS1kxnLY7gBo7CUCWUax0FmJOOY8udmCM7YBrwdOzeWdHwR32o_qdI9lVjx9v3gvmFFLSQ90Ga6C6nrXt5mWxX5pVL6wZjaUPPJyFay9WeOoN3tIwc5E0gp1A7IxW7WobVU8ftlDScjihXGTn1v-vU4epYog9zAPlUrRjxlgTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
جدول لالیگا بعد برد امشب بتیس و سقوط رئال‌مادرید به جایگاه چهارم جدول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108363" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108362">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9324bea2.mp4?token=J8WNcD9Riqt6Qv5FDdmsjzP53PaSZLd5fo9ZzuRvNGL10yzs3X1eDUsUVu49lFQ1g9o7442SuBbboGuVMpVp8wEnVj-rZ4AZeJFFKKUtdp8pPeQSjdczTtAK3y3lN0LC9D13rgibI9NAyYH6cM0uCxSY_4Yt1Q21Q4mWM5hojNKoeLLC37WUIH0wVTRH5r9qOthKWSkBEx7nwRmZDsrY5twD0lo0maiLY9OiEf61JUjnZLJgJ33G6orbRJPEQRvJj_GCRWZHXlZGxyj-d65LbPaUtqWOlKq3nbl-seTwTj2YbOmXGrSZNDQhIkC9BhidY_v0Pt7n-ycjKgv1of_iPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9324bea2.mp4?token=J8WNcD9Riqt6Qv5FDdmsjzP53PaSZLd5fo9ZzuRvNGL10yzs3X1eDUsUVu49lFQ1g9o7442SuBbboGuVMpVp8wEnVj-rZ4AZeJFFKKUtdp8pPeQSjdczTtAK3y3lN0LC9D13rgibI9NAyYH6cM0uCxSY_4Yt1Q21Q4mWM5hojNKoeLLC37WUIH0wVTRH5r9qOthKWSkBEx7nwRmZDsrY5twD0lo0maiLY9OiEf61JUjnZLJgJ33G6orbRJPEQRvJj_GCRWZHXlZGxyj-d65LbPaUtqWOlKq3nbl-seTwTj2YbOmXGrSZNDQhIkC9BhidY_v0Pt7n-ycjKgv1of_iPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
یک پیجی تو اینستا هست کلا یارو با یک بیلبیلک میزنه به مانیتور و نسبت به دروازه‌خالی خراب کردن بازیکنا عکس العمل نشون میده..یک کلامم حرف نمیزنه..انقدرم بامزه انجام میده که میترکی‌ از خنده..خیلی هنرمنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108362" target="_blank">📅 21:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108361">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJZZkm0wy2aiEKTj44heyXqmh0t9_zy30OZal7wiBHBnHAu-9GKkPcbnD7J3D2wElNdrQ27LgGP8dIXf2Jx-XQkC44s5Q0tD7BjFEFq3VTbg0xzoPHNBn_O1qc8mGtTFQDuEmFlwJlnTnUy9vNIJwSniliHRmed9tgzqeO1Im1bVrRlA6VzW6ok8sEf8-ztz8TkD9d9JJxnkuqIhxBeRUykv2dOKtbrf_1CkUASOZC6M0s-PO6JW6BU-k9mvYzET-p_piIY49WWPnN3Y4qcJ4o47B_eUHQqfaFGTOg-sKNMrhKq2PzgZS4_AmQNJ5B_Ssd7kEdv1JkydkTpYw-8Z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/108361" target="_blank">📅 20:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108360">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=Qj2jAdZaRwSFT0XFWcqnXpmXH216lCCGP8WWirRzP3biaqtlxKEJkyvY3mWAgwKTGyAWq814B58wKvhhJWaSQANrNn90BxT9HZ7zWM-VqKoO9Jj9NldtZ4Mls_yAWuArdD_XhKVokCPiV_bc303wrQEwngcOKqi1NJjumeZdLIgGL0BP2z4xc6NhrwOKs8nEt_wrMuAYBRl1JmfRdaQgFdQ33WWBw_O2wkQh0t4JGYrrMGxOgPofxtG9nzPJJq2DE0bM-Vwg0DiaXDxwTz8QZ9uzn5ffrGzYZIW1_NM4_xk8mVRjISAwHnf7b0mqy1c-N6quA2PnSeG4uoxvCz3ESE111kxrYSfdUjydUkpRtu6caq5OTteupm8m5LowRmYuEXdq8SeuEvl0z1lCc2KegsXDYDul3qif6Fia5tBLXQ0KNiouL-g2rSxTfPeXZVpd2xhdbUpeotL5am-3fjgHFDhs_vWQIWz7qMdfHhMa5tD8H-c4lOBWy3qOMs8joZnuQlL1ZFq7p0GoLD9oH3WL1K7NXq7CBYIp6Px_88WWmBkbK8aaDPTw3a0Wz2LeFxicXFD0JWnvShPC1GlbAks97N2E6b3jVUQbXJQbLW5O9rjcPFKcB_BpgKrTNOopzRvPmhrTtscynIjDfKe0bSqeHDKfyPS23o1MAI38tO7ya1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0ceb28628.mp4?token=Qj2jAdZaRwSFT0XFWcqnXpmXH216lCCGP8WWirRzP3biaqtlxKEJkyvY3mWAgwKTGyAWq814B58wKvhhJWaSQANrNn90BxT9HZ7zWM-VqKoO9Jj9NldtZ4Mls_yAWuArdD_XhKVokCPiV_bc303wrQEwngcOKqi1NJjumeZdLIgGL0BP2z4xc6NhrwOKs8nEt_wrMuAYBRl1JmfRdaQgFdQ33WWBw_O2wkQh0t4JGYrrMGxOgPofxtG9nzPJJq2DE0bM-Vwg0DiaXDxwTz8QZ9uzn5ffrGzYZIW1_NM4_xk8mVRjISAwHnf7b0mqy1c-N6quA2PnSeG4uoxvCz3ESE111kxrYSfdUjydUkpRtu6caq5OTteupm8m5LowRmYuEXdq8SeuEvl0z1lCc2KegsXDYDul3qif6Fia5tBLXQ0KNiouL-g2rSxTfPeXZVpd2xhdbUpeotL5am-3fjgHFDhs_vWQIWz7qMdfHhMa5tD8H-c4lOBWy3qOMs8joZnuQlL1ZFq7p0GoLD9oH3WL1K7NXq7CBYIp6Px_88WWmBkbK8aaDPTw3a0Wz2LeFxicXFD0JWnvShPC1GlbAks97N2E6b3jVUQbXJQbLW5O9rjcPFKcB_BpgKrTNOopzRvPmhrTtscynIjDfKe0bSqeHDKfyPS23o1MAI38tO7ya1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم منچسترسیتی به لیورپول توسط چرکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108360" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=uSEV1QSVM4NNt95ACRl5HE4kqPqhufN5WjhO-ZD5FLukdlzjS2IoL1O7mOJjQPDxjcB6SlSV-XI49zCtVbBv9Bp_THLIcC1l5a5aLRBaaYCdXhpDH8mdpf0CRWwPzg4wrE3L08t0D6aDKj5ADw8xyqhHOTxa2skhT9gzUhZTV8dFRkUprQSvDV4mBlNUb_1aNWjTSxBraOud_WxmQqDbU5Cmfchji-GH-LJLzlzmnxIiU2vnZ2v3A05eTsNHU87pM6UA8itpgLHFa9QUbbqabTm6QTMGNgxFfqteaNN3XQQ3uhuwF_cPzLUFkpmWh3P7YugBFFpKmEID73MKNWi2wW3KLv7xJLQpyfDiZqPYZNcvEGRBRotcYN0YBTkTkx3NVN44vS62mlcGKIhUE01Hw_9KsdGWp9CarwLQu4nDv-NJ76L1Pspe2pwFIYLaJK7KoqRckbjLDp3oIAYLAr2YNhUYnHREHu7X-qA1hYpqlKOfxRWpO3nCBn0SPISTzQUkbAEN-merZLaSG6wbypMpSGAf8RlB5c2b7hzAY2I2HRiHGnHUI5IFq1tNuING61NqmDZG5PM3mn_Aa8pssE5qvnoL2xCDS87B1gprbo1SrMa0nawzFKPnhSjMzh8Bg0b6R6BA50kPyGyFd5LpwdRV0WhL87GfyzlvEcEzoj_-Qsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2ea33571.mp4?token=uSEV1QSVM4NNt95ACRl5HE4kqPqhufN5WjhO-ZD5FLukdlzjS2IoL1O7mOJjQPDxjcB6SlSV-XI49zCtVbBv9Bp_THLIcC1l5a5aLRBaaYCdXhpDH8mdpf0CRWwPzg4wrE3L08t0D6aDKj5ADw8xyqhHOTxa2skhT9gzUhZTV8dFRkUprQSvDV4mBlNUb_1aNWjTSxBraOud_WxmQqDbU5Cmfchji-GH-LJLzlzmnxIiU2vnZ2v3A05eTsNHU87pM6UA8itpgLHFa9QUbbqabTm6QTMGNgxFfqteaNN3XQQ3uhuwF_cPzLUFkpmWh3P7YugBFFpKmEID73MKNWi2wW3KLv7xJLQpyfDiZqPYZNcvEGRBRotcYN0YBTkTkx3NVN44vS62mlcGKIhUE01Hw_9KsdGWp9CarwLQu4nDv-NJ76L1Pspe2pwFIYLaJK7KoqRckbjLDp3oIAYLAr2YNhUYnHREHu7X-qA1hYpqlKOfxRWpO3nCBn0SPISTzQUkbAEN-merZLaSG6wbypMpSGAf8RlB5c2b7hzAY2I2HRiHGnHUI5IFq1tNuING61NqmDZG5PM3mn_Aa8pssE5qvnoL2xCDS87B1gprbo1SrMa0nawzFKPnhSjMzh8Bg0b6R6BA50kPyGyFd5LpwdRV0WhL87GfyzlvEcEzoj_-Qsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دوم منچسترسیتی به لیورپول توسط دوکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/108359" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=AimxAmHQr-DalZwUqro_WG9P18L8mZ82F-GaANQYj5UzncvSrnGM_NefygVVwfB0vuYfGTgk-hu5F9Iudm4jj20zRziTAh8NHpTrNZDF3Y9azJl2lKd5hAkc14_wY9R8GT2Uh1fbnpG85iEZ4YUPvBGisebvxHiG0ZqcDpghOFsEAwPDyaq0nD7vnFozEtu0nU38tuWldTw4I-SPET01t8xy3QM0kdlga3Pog91lmkGyN7VxX619g_wV8dBBxRUxsXw322jrbTgtVJda23E3F9lkk2ZqLbk4qhg8fJhOOHzWGgZ0efB5jVSKxGos993izwJnEWcARN6s7x3t6i0UPY2jUYcA0Hv3U7vwZv3JyLbPACT3TD7sWk9i_jfIDhOymsQl0hFltY6YNHt2IOHM4fGbN0yOCMdGEwRnqcap93fTFVnD5NOFJOZPgl0vDwHtn82td-rh-BMWEodA1CwgALbZBSaA46yZDWuRBf5gcykqb3GrzgOfomtc7buD_seZ4p2FTIh6lNO_VUK8oG2DFscC8dVbvbpIit4VH0ycg-N1B7NHh_Je8xTFRMfOlNXpa2RR5cVrz1MWxastiw6XhYWM3MAjXelZjuk8eFR798QjOf0k3o0TKuHjAg6LqPZz4yLBgE4Lr4_iepSQd00rtB6rT1hWpBaavfmA6gZzpnI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af24dd3625.mp4?token=AimxAmHQr-DalZwUqro_WG9P18L8mZ82F-GaANQYj5UzncvSrnGM_NefygVVwfB0vuYfGTgk-hu5F9Iudm4jj20zRziTAh8NHpTrNZDF3Y9azJl2lKd5hAkc14_wY9R8GT2Uh1fbnpG85iEZ4YUPvBGisebvxHiG0ZqcDpghOFsEAwPDyaq0nD7vnFozEtu0nU38tuWldTw4I-SPET01t8xy3QM0kdlga3Pog91lmkGyN7VxX619g_wV8dBBxRUxsXw322jrbTgtVJda23E3F9lkk2ZqLbk4qhg8fJhOOHzWGgZ0efB5jVSKxGos993izwJnEWcARN6s7x3t6i0UPY2jUYcA0Hv3U7vwZv3JyLbPACT3TD7sWk9i_jfIDhOymsQl0hFltY6YNHt2IOHM4fGbN0yOCMdGEwRnqcap93fTFVnD5NOFJOZPgl0vDwHtn82td-rh-BMWEodA1CwgALbZBSaA46yZDWuRBf5gcykqb3GrzgOfomtc7buD_seZ4p2FTIh6lNO_VUK8oG2DFscC8dVbvbpIit4VH0ycg-N1B7NHh_Je8xTFRMfOlNXpa2RR5cVrz1MWxastiw6XhYWM3MAjXelZjuk8eFR798QjOf0k3o0TKuHjAg6LqPZz4yLBgE4Lr4_iepSQd00rtB6rT1hWpBaavfmA6gZzpnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به لیورپول توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108358" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=aD2-GZzMxw-Lrg1SGpIG7V7rYj94rySEA889pjlhV9GE1LjuVqNBFfrBtvxiSXPXj-qmaTHvyY15T3UufPhJkN5HvPZMp942Wp5xm7T15zTzSVNgjorNwLSMTW1uMEKYFj_z8AksUpyQiDA6upWoJRr9yG5KpdaHQPRD2NYHg0lWQWWvO0FzMn2HbPPMl-bVaCqWzf-4hGAjRVN1X98ME1A-43sli1iSnF5BR63sOsmiT0x8ixAN4pxwucnctMNCCCWQtc2lKEZrws7lW_1uaHnxuTaiKwOUsIKKdJxMLew8JUgFGAW0aVclWbeLBWJ_EHSytl8QEnqsIkKse1JYQVRNFUL18WzCatyFTTrvyT_DwVnktPxGqtxeumkYBxCzO9MSfTbicmoLDfv1lhGtDqqq8_V2l62eFOJduKaWqEcyFiA8wwMs49T9yr7sTxanbpC5VKOvjXzBlUK-lUI95vpXx6hJL67XL4XAGgA5VTKVsHlzDMg-JJauE0OAGlDFDNNhuGj7HSjOSN6jhOxXh5IsEEQER15Av2SMm5caZOfN5n9TYf5p7JG4139ZahtjZ8ND-taM-_EW0F8mPiKksX5t-eggYziv2clXYriYrSKyGY7UgFjMGykeIE13HxuqIRAgYbmwbd0JLfRfsl0sCFnEAQ4UmkOLQBudORZzu6I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f590a86e3.mp4?token=aD2-GZzMxw-Lrg1SGpIG7V7rYj94rySEA889pjlhV9GE1LjuVqNBFfrBtvxiSXPXj-qmaTHvyY15T3UufPhJkN5HvPZMp942Wp5xm7T15zTzSVNgjorNwLSMTW1uMEKYFj_z8AksUpyQiDA6upWoJRr9yG5KpdaHQPRD2NYHg0lWQWWvO0FzMn2HbPPMl-bVaCqWzf-4hGAjRVN1X98ME1A-43sli1iSnF5BR63sOsmiT0x8ixAN4pxwucnctMNCCCWQtc2lKEZrws7lW_1uaHnxuTaiKwOUsIKKdJxMLew8JUgFGAW0aVclWbeLBWJ_EHSytl8QEnqsIkKse1JYQVRNFUL18WzCatyFTTrvyT_DwVnktPxGqtxeumkYBxCzO9MSfTbicmoLDfv1lhGtDqqq8_V2l62eFOJduKaWqEcyFiA8wwMs49T9yr7sTxanbpC5VKOvjXzBlUK-lUI95vpXx6hJL67XL4XAGgA5VTKVsHlzDMg-JJauE0OAGlDFDNNhuGj7HSjOSN6jhOxXh5IsEEQER15Av2SMm5caZOfN5n9TYf5p7JG4139ZahtjZ8ND-taM-_EW0F8mPiKksX5t-eggYziv2clXYriYrSKyGY7UgFjMGykeIE13HxuqIRAgYbmwbd0JLfRfsl0sCFnEAQ4UmkOLQBudORZzu6I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
دیشب بیچاره شزنی سرش محکم به سقف نیمکت بارسا خورد که همه از خنده پاره شدن. فقط واکنش لاپورتا رو ببینید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108357" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TBZEDZkyrJm5FOG9o1fsNrDA4aYgHadzDnOQrJfgs2knXqCOlm_Nh01Jf7etmrdyDs4zD5RVLgmTCNg1at0AD-W6jRMc3doWJadtFIsZ3JEBw59nTQ3DiTU5eL4eewmKOwojlJAGi5uNFrb8dfcEYutGzXKf9A2B4itfoA7rhdNb1cAgX1BPGAxc9osk424KpnysL0jCOLp_la98gSKu28S-YDaA5C8D8dBMx66UXH-zV_GsJXYnLdG9k0jkIOttGAcg1cImGAPFGWfxejG61tyWAPY9nM1etSeTv6lUXkvM-CFU2S00ZbGO0oOv-zyxm7LZklPkJpgfd2BcpEyWZLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f48e140da0.mp4?token=tjuMYIlX3_LKckcwiDigjnbsBqwQIVvL2UhnjhWxvvQwwPupRfgtotMzYkJRiOrdvO5VJCh0dGRpsnjocq6VT7QuGUndXi3KsETlVAmZUe4EnRM-NHwm1GyAO7NRt0ku42sqJ9bD2rhmFfcYk0GKoGSxa-1IgMnG6sgMRXmxHEVAXD4kon3yB3Z8Zj-yZnoUq1Iu5DPc0nBkQJwg_RFYG1GulhY6zuEnsVYWhrn7Wzc34DenxtB4150Wb6xx1dYwhGNfJESx9UQf5r0soQ_bwWRDdISuIzKxPo0p6J5oZoC-e-v_efhXhATmxOZiFIRRIL7l0qdi4_W6xOUCOPW9TBZEDZkyrJm5FOG9o1fsNrDA4aYgHadzDnOQrJfgs2knXqCOlm_Nh01Jf7etmrdyDs4zD5RVLgmTCNg1at0AD-W6jRMc3doWJadtFIsZ3JEBw59nTQ3DiTU5eL4eewmKOwojlJAGi5uNFrb8dfcEYutGzXKf9A2B4itfoA7rhdNb1cAgX1BPGAxc9osk424KpnysL0jCOLp_la98gSKu28S-YDaA5C8D8dBMx66UXH-zV_GsJXYnLdG9k0jkIOttGAcg1cImGAPFGWfxejG61tyWAPY9nM1etSeTv6lUXkvM-CFU2S00ZbGO0oOv-zyxm7LZklPkJpgfd2BcpEyWZLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد ربیعی: سرمربی تیم ملی امید نمیشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108356" target="_blank">📅 19:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=IIz7diVeQDInCGeQkSk7Y5CYW0Cgdj0YJ-mF6Uv5PC8rIXfPFwleEkKckDJqC6JtABUpN1KE604IhAXBnpBz2r4HjasF-RJN1Hmd16FZ6gQJqWvLKXrFxs-tI6a4mOMOSwXR605YsQbzkn5TkdhmAd7aS9ziGN9FI0RyC705bQv1JA0XVXq-Hkyl10pqsWd0ZT3f_3t1q_eF5CSy6HdxG-_TWftUwemcJ-osGiPs-Scg1ACZqGqoG3ZvmCuVlWRRl6vxbSMMwccrAfatAPPVw4DaviJB7bSxNPmtCwfl5KfufFsJI-u5HbfLl2kAikPLcgUtBT05klyi5KVj-boIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad48af115.mp4?token=IIz7diVeQDInCGeQkSk7Y5CYW0Cgdj0YJ-mF6Uv5PC8rIXfPFwleEkKckDJqC6JtABUpN1KE604IhAXBnpBz2r4HjasF-RJN1Hmd16FZ6gQJqWvLKXrFxs-tI6a4mOMOSwXR605YsQbzkn5TkdhmAd7aS9ziGN9FI0RyC705bQv1JA0XVXq-Hkyl10pqsWd0ZT3f_3t1q_eF5CSy6HdxG-_TWftUwemcJ-osGiPs-Scg1ACZqGqoG3ZvmCuVlWRRl6vxbSMMwccrAfatAPPVw4DaviJB7bSxNPmtCwfl5KfufFsJI-u5HbfLl2kAikPLcgUtBT05klyi5KVj-boIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رختکن شیاطین‌سرخ بعد بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108355" target="_blank">📅 19:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=gyZVAQ1vxZKI8ArYG3cn4-pU8R2vDPlprOv3dhjd7Q4UvcV5SjxVC7ovw0RykhleuisGSJJE8NH-8d0HpC0FIFpBDdngwyBcpQ7xeghAmj0Om_Qbk26yQP-slJgB4QFV7TZEfx8xVYWai7nuIkUhpoSoyWlD8-9dZmgzHtmpkKsVUTKTKicQds0v4Ra3eCRKQjkw__Pdp-KIfANED38hBoMv-OQ1ygcK6l0InP9pyr8FHmhWgKDCbtbMmitNHharNpdRwROAhYw_aDbqZd6S-4ZG1fGbeI5EVuFOazQid7rcKZCtz-ajkHF-JikcXjgStQmUoQfcytIp1dUlQ4pz_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1015d7a264.mp4?token=gyZVAQ1vxZKI8ArYG3cn4-pU8R2vDPlprOv3dhjd7Q4UvcV5SjxVC7ovw0RykhleuisGSJJE8NH-8d0HpC0FIFpBDdngwyBcpQ7xeghAmj0Om_Qbk26yQP-slJgB4QFV7TZEfx8xVYWai7nuIkUhpoSoyWlD8-9dZmgzHtmpkKsVUTKTKicQds0v4Ra3eCRKQjkw__Pdp-KIfANED38hBoMv-OQ1ygcK6l0InP9pyr8FHmhWgKDCbtbMmitNHharNpdRwROAhYw_aDbqZd6S-4ZG1fGbeI5EVuFOazQid7rcKZCtz-ajkHF-JikcXjgStQmUoQfcytIp1dUlQ4pz_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
بارسا با 9 برد از 9 بازی به دیدار مقابل گالاتاسرای رسید.
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108354" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
ترویج گل‌زدن در صداوسیما و مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108353" target="_blank">📅 18:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3e_Msi5Bm40-HPxfabZu-mL3_20qvLvMwxEugcMwm1h7lnt3jSQC_cKeQBVOfDAXCNITvKWbrchw__4Ho2pj6gS3YNtrNLmAVO-Yvy9pYCoy2KX02yRDQCvBMa4gcSxd9YB47Lxf2yVb-2niF4NoUNOyxlBg9qDleUTYu9HUd3YdYW-Lloz7YTyzBylNurQEcjz1SpIGrRKa9tJNIevprAxSeLKOoBZDByCyxnk7qubik2y7RNWQPmtovyXmu_oMrSdIRFJrvPi1UY1q3yhrujnLTW58bjuzPcnmdBetgQLFDJ2pQDcAzorBTok1f-QM0vOMyYAtLP7lGIVSkpPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کلارنس‌سیدورف از شاهکارهای مدیریتی تاجرنیا که به مدت چند ماه بدون هیچ کاری چند میلیون یورو از استقلال دریافت کرد و از ایران رفت، سرمربی کورنتیانس برزیل شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108352" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlwnbDRXonE5ZX09_Nqx0f6ON9I4aa6hkpqitkfU6XRJQw9_uW3LkRC3YwUf1G2-UcZ2USeNixFG2tS2lPFoUwDblKEhOBN7CMZuwYs7G1znJ5myhsXD4FIXg7h9S4BkwKWhxQrYEkW8rng9RmYJnQfDkfzs8SsRpZ5MQS_f6pKDSv1Sr4x78BEFAov64M3T7g9p5CYF2A0bhW7bcxnrwMp7Q6ZcN5A9xPDiKVblVSgfxrR2KL__7euhpLVuzyX5R_8X7Oh_2MYDmwcz_P2rt0J_R1heKnsaV4cTkOSu2tXpfl8nXvWgi_Zd18PqaefMksZl2-e5QUw0YTVzqyiczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXXqeraMtM9uUrNWdk2cyKgGLnsYnpYCzez4aQr1u8W3SFfcU9R-ZLawbrlxD8zFM2slMQXRbBtRzJRpsHvyYW-Ve7GWuQTl6ME_U0udwiHIlH8-tSwZOMDOXZ1cWZKv2vZIO0EzTZ8xXVeNLC1mfYcm6FmJbrtN5bpJXYInGkeGuuSsmtEqAaZ5KlIsM2xloDctKBX2Dj8NqmZVZXR-5N3b_kpkjbuVaHVve-6tSCUejwSXstnSSPqpTAVNxofGHeFbxeXaALalP-dRMP624Y4Lqjbmixse4qHY8TvuLuyxsZC1-zAvgF4lkYBoHQmlAQfAGQ9Qn0jnngHiT63j2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچسترسیتی و لیورپول
⌛
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108350" target="_blank">📅 18:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108349">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR05krKe9fnZg14jAeY9ZVr3AjNI1Ni3hoB7uD8Gtld4C-mCAkH6EzXkDb8Uc2etYp3QyDRqRA-GJ_aAAbVfevULmetKwIBMDUiOdY1f1eRT1xtiM1Ne8EB2TanwgPWBRBAd9Qo6krVILcr2l1wOGpGDHxiEhzg-s2gXOiRqbmEwoylqpMRJc6XRYmQb_N0hkqDTQnxTRtzlNHAJfE8zxOMBcIWoD20TPu5UUz1-L6OXq6oPWDJzivgX_1zC8fdftoaLi2j8vCvnT8bdE75RM2bM1jZ4xAtmP9_lSZDnOpmmDlPtPs-nf_sk73ab9JFCrXVL17iLnBIPxLDZ1fR2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیر سفر گل‌گهر از سیرجان تا بحرین را مشاهده می‌کنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108349" target="_blank">📅 17:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108348">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=D7S-QJl701SSQ8tSA33izcj-7yvclodffOXV70FuDqXJCg6VT-37If7lnpCHAlgAQl3bbXLMJJt77H9Rlfd4g1UBRi5So9soyEHG47ZDDMwcp6ofNOarD12Ji-iI1ttwAEc-ymD721teAE4aW4MMOOqb58f7DN1Ekw-A5JPvHZloESdTFQQfMUtFMDWoTztEPqu04QRnNJNGTDNwozm1VgoYZPn3ojA6NtoUAMyeyoF3IH8gc_9s-mvg-LUbmW1BLfmjgUW-v_gFvupvyLgboVYTtGpitu1Tx0HD2Se_WLBE2iJNOWyBJG339A66rS6CjcQGtapvYhIBf2ZKAhtZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080d5c7641.mp4?token=D7S-QJl701SSQ8tSA33izcj-7yvclodffOXV70FuDqXJCg6VT-37If7lnpCHAlgAQl3bbXLMJJt77H9Rlfd4g1UBRi5So9soyEHG47ZDDMwcp6ofNOarD12Ji-iI1ttwAEc-ymD721teAE4aW4MMOOqb58f7DN1Ekw-A5JPvHZloESdTFQQfMUtFMDWoTztEPqu04QRnNJNGTDNwozm1VgoYZPn3ojA6NtoUAMyeyoF3IH8gc_9s-mvg-LUbmW1BLfmjgUW-v_gFvupvyLgboVYTtGpitu1Tx0HD2Se_WLBE2iJNOWyBJG339A66rS6CjcQGtapvYhIBf2ZKAhtZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب خیلی جدی ادای آخوندارو درآورد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108348" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108347">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108347" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108347" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108346">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbruxj_aqXRY21nP26LabQJpDIzPemaKsEd-srEga6s8m2t4Tqe-TXGKSo78lP6hoeroENn2XgTKgk2TeN4ch8VIKNDmB8lg7TNzG-3T0nkBV1y1gTkM1TNR5jYntJNpJT37JEKNMLxFzCM2tF4S6-SHLdXYxBsgRV8yUH6Z8neU_VwC6YTPcUxnv4MkwxrQVQ15HmJu6JMnMliwWbncdInZWT5UAOGRhWwO9ujlxEKrMTNY0gRjj0r3RKOYetQ8OlRdxKSDeTxV_bRwug2cjlCbO-8RxTA3ug-bWdWclQNOngmPvLxfPYnJOGpUOTgEv_AOyP5DSN8MBMp1rwKxaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108346" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108345">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=Tob-C-jp-Dy2An9ISZHfkuTwnMXEd2GxoOyqYx0zXrV46--ZJv83eGdijOXZENrn8grAvmzBscMLInhUjf2xcF02CIKg8OJXzVOf-YxSj3ExkpcCr8ESmeB6Q7njIT2dgfJi3HxOwMnBLDcd3vUC4MvtVLCYZxN4Mq8oTp4DPk0nJsN0yUzG9Csd5AWRhfLpwMbOs4lyxddKfyQeVmQ2zAEXNhCNX1MORRM7QmwbTQIhTX423FFeYfimPhy8eyti_bR4902TuwlpSxfWVu-gu8Zzac07kh5Nq4JzhMIrGzjEgKJEKxcfnR5uSz39wuGlNLFeJp3fCPX9oDazi5IV_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e1c89b4f.mp4?token=Tob-C-jp-Dy2An9ISZHfkuTwnMXEd2GxoOyqYx0zXrV46--ZJv83eGdijOXZENrn8grAvmzBscMLInhUjf2xcF02CIKg8OJXzVOf-YxSj3ExkpcCr8ESmeB6Q7njIT2dgfJi3HxOwMnBLDcd3vUC4MvtVLCYZxN4Mq8oTp4DPk0nJsN0yUzG9Csd5AWRhfLpwMbOs4lyxddKfyQeVmQ2zAEXNhCNX1MORRM7QmwbTQIhTX423FFeYfimPhy8eyti_bR4902TuwlpSxfWVu-gu8Zzac07kh5Nq4JzhMIrGzjEgKJEKxcfnR5uSz39wuGlNLFeJp3fCPX9oDazi5IV_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس سمی عروسی گرفتن مسعود شصتچی در قسمت جدید مرد سه‌هزارچهره
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108345" target="_blank">📅 17:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842c49b387.mp4?token=OPe4zHifpkRCeEIog3meHoyi_QoZDdn3CB_bu7GQa-W1dGgh7_jFLQhWY3uKNdCNWATleIG5L8vk5WghcP3ouz2GPXadFM6nVzbFD8YjtuFUapg6bgQhZIXkv9fhOTsxzMsRQG1zn5MLF4WpT0PxLPZVsGPmxgU0qiJTqgVr8g-_pFJ-brNjmOwg19HSp4IwAUUqNwk8PwOQ9a4IQdMI7BpbpDi0aY6slwpImgLclDQm6_EvwqxSqMhZekO362Ski9MkYFs8eaZjHmXlGJyep4101DY2lnWI_qOXnNAv_W9YbNwKxhcgJSJwLy5cXOmeXFf7kc4o76WZ8_cQzjkEyzkCEi49LvBlO1-wEHgP4lbJxFlZu353QLAP9ZGizRG3b8stNojlLZbF5fzdGYU1-09x7lBoZXRbgQUsLeneDXzsKDTo9uWZU598wCqHoVurPATGkjPnVpUYzYLINL5DRIPrBeUa3LIYu2pQ9lzm6gzfl_taMs_RbxVvqS22ossMLUU_zqtCbX6Vng_z4vNh8qb2keW0IlcZCZZyYKQT3JO7Kk2_Ma11zsBG0olWRW7AZRMn_4GfryRo9u4nLwTT-sf8_CPbirRn4uvcl3NIHdLOhhX-j7TVJ5qcS5xAFDkzT5tFlQckM3g2GNulZbZ-cszThpi2X6UTI4IsLDPcIcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842c49b387.mp4?token=OPe4zHifpkRCeEIog3meHoyi_QoZDdn3CB_bu7GQa-W1dGgh7_jFLQhWY3uKNdCNWATleIG5L8vk5WghcP3ouz2GPXadFM6nVzbFD8YjtuFUapg6bgQhZIXkv9fhOTsxzMsRQG1zn5MLF4WpT0PxLPZVsGPmxgU0qiJTqgVr8g-_pFJ-brNjmOwg19HSp4IwAUUqNwk8PwOQ9a4IQdMI7BpbpDi0aY6slwpImgLclDQm6_EvwqxSqMhZekO362Ski9MkYFs8eaZjHmXlGJyep4101DY2lnWI_qOXnNAv_W9YbNwKxhcgJSJwLy5cXOmeXFf7kc4o76WZ8_cQzjkEyzkCEi49LvBlO1-wEHgP4lbJxFlZu353QLAP9ZGizRG3b8stNojlLZbF5fzdGYU1-09x7lBoZXRbgQUsLeneDXzsKDTo9uWZU598wCqHoVurPATGkjPnVpUYzYLINL5DRIPrBeUa3LIYu2pQ9lzm6gzfl_taMs_RbxVvqS22ossMLUU_zqtCbX6Vng_z4vNh8qb2keW0IlcZCZZyYKQT3JO7Kk2_Ma11zsBG0olWRW7AZRMn_4GfryRo9u4nLwTT-sf8_CPbirRn4uvcl3NIHdLOhhX-j7TVJ5qcS5xAFDkzT5tFlQckM3g2GNulZbZ-cszThpi2X6UTI4IsLDPcIcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
رونالدو این‌روزها کلا اعصاب و حوصله نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108344" target="_blank">📅 16:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108343">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgEgZc9n8X7VkLFgy73x-JlbwYGE6JbKtQLSFrBxR3xH4WO-0Ct87XBDEeTr21fN4dy9-MJfx8mgWvnk8ENgFGK65TbnYBE29jrXaMfC6Usrh7MuhBFcT0WRTlea-4C1Sgvxcoo0E7ZUGbfKyTN_OQGwcCPr_S2ldiyEDSTqQIVJ5Eb2tDWTRLwEDzzf8cJsvOnWMwjDeuDC5G8-NdikL_SMZnjfyQeIRvqUChYGFTVpi5ZBLimA2MdfQ_o_OriCH3RWPY91j7L1zDBErZpwq0eXi6S5-umbvGDluSGShz803taUuwqCNQRMuSzMOsBLhywUQeJdKF5or9DqcvjIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
با اصرار یاسر‌آسانی، پزشکان استقلال تا ساعاتی‌دیگر تست پزشکی از این بازیکن خواهد گرفت و در صورت بهبود نسبی امکان حضور کوتاه مدت مقابل الغرافه وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108343" target="_blank">📅 15:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkhgCnF8dnpnyOc6lDgrvEtNy4Kpcj0q6acG0SdHPQgSmdpV-J0rtafZaMWNXBy2slX7cRzyR50cQcMnH2EWPRs4Vo2gfvEvaSika2DGxBDdGetq2mmr9Q_a5phPOfFiz9QXJi-hmhgKLURonxejKcRCzxqAY6HFEcYYZBMRKUiThQ0TDK5-fkc1rzZ2iNLR70N2VSzU7M_7k3BoaGyz0CHrpua41QFXU-kymENRNTRjY4uKY4oKUpra6zXH9RY4SfZjpYJYVVWseZJi4UO6eWljMZYtqVehOLty78bYsHb6dBnJLxXePNVkMWP6yCnQxbBQKh7EI6zs4VtfAHYyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108342" target="_blank">📅 15:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT2VNlNg-pK1c34UjdRZ44dtifmKKy2hKnccHE2a7EtBwPLkdXJs6OizjEo5UBOcwFAzRfQ1n3zZML9rnnLSZCUQjnMYUpQR7ophxj_yNFCrj_LaTA_UBQ8P02-JAR1-DN_xBYI6jrhtwz-Cb2Ba2s3Bfzu5jYEtQWEnF6ye8PZZwjmVcvTHQivLisMVpTD1TGmF3p6Ift2PsUjZKq7MzkgKHW6duuQHL-v4GR06CerSYF4gOec-c5CObystHmqqF970M57KfgiPahm4fmNLv0Upv8l4xJlGmAvDxbF6RED6bktDqHCbqYQ1V9Udtvm_W6aZjlkaoHyiEFnG9_kbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آمار تقابل‌های رو در رو لیورپول و منچستر سیتی در طول تاریخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
110 برد لیورپول
🤝
58 مساوی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108341" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش مهدی توتونچی به مصاحبه علیرضا بیرانوند پس از بازی با استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108340" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه‌سنگین ابوطالب‌حسینی به ژوله
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108339" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
واکنش گلزار به ساخت کلیپ‌های هوش مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108338" target="_blank">📅 13:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108337">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbt-7Qyswj2KuE_Ht8w7X9pXVecBL4RX4UPM2MzK4H-usJODevYJaUTOuZI03GiAPFp8TNepQI26LBeybe3IYB4HJ2MQNlc1s-UqWYPbkOlHg7Aeys_klwnhcrEOjkQQzmfnR65bd1EzmVZfR_g0C_sWo-zLYSWtgjUXGunZ8NF_8m_TOFGBSTKLC3oItjzRYHqE2LX0TjiELdspGWn4msqFwPnz7FWd8V5JwSRbFo7rZr66FppH6rODyz70HwQ-GxVsjY_ko_icWKzMS92_cJFhJcBkG3jMv-8CYboSsc8eV5aj-t3GDvWSupnB3vX93ye58nRQOm1hso6HmSdrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر باشگاه استقلال ایران برای بازی الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108337" target="_blank">📅 13:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108336">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تذکر تند رضا گلزار به قیاسی درباره ایرج طهماسب؛ گلزار با تاکید بر جایگاه طهماسب به‌عنوان یکی از چهره‌های باسابقه و پیشکسوت سینما، از نحوه صحبت قیاسی درباره او انتقاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108336" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108335">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینی داشت به فوتبال برمیگشت که ناگهان ...
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108335" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108334">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOrOvD1JIWfdr9zNglo-3XWNYmYglQ3qG1kpj8QbtqcirdfN2PwYknguNIWY2HnYv_CmP8_ArKgPqnq3dMFjk1SSozhrfYUnPX9vHvCn4D6vQbvARTTyzPxRXfsk335y6FX4Uz5O3QUmnayWS9CIFTmb6Y0CqTDL2U0c-sReEoVLmKtpl7ZoMfYpYfgkXuOMJMirMV-RmzZhhCSgIARtBnJB8_Kxfg03ZvZtebYhCZ8E4S-NqePvyjljMxkHzvC83Qq8P08kQPW63MkBkb2f_5t2Di_GJsfqmEo5_PnN5P3AZh72p1YIHSi8zA6VI5aDHeTJSk-LXB4ZizM7E6ZRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108334" target="_blank">📅 12:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108333">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پشت پرده دستگیری مهدی طارمی و سروش رفیعی در جاده شمال؛ رویانیان ۱۲ شب به داد فوتبالیست های معروف رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108333" target="_blank">📅 12:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=RBvZNGA4poFeG8DrOgqMbX_8X9xhFIhtNN2maUlq2S4oyP0TyIzRaU2em5qMa6YLh9eMJVtMeLIcWXVJQ_wCR5ez069tg-hAGmmALkLEexYSPzVF3VhXS9F5yh7Bth4GE8p5i7V5xjVe7ZzLdzADpvLgoUQaglx2vcdEvNKsVePloRjUxlasRJgWSYCU0q1HisrnJJIq1UeX_Wu6-u5W4uXlAvSFlXiQernM_VY4ON0F72hohjOVfh2TP2lxuG7oVx_4KJGN75goXdFOn1ir2g24H2YTfd9WbRJcmxPFqoJrAxqrb8WDMlGhfQ_2OGPg8iLIHi7W8XBkZjkD0BCatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=RBvZNGA4poFeG8DrOgqMbX_8X9xhFIhtNN2maUlq2S4oyP0TyIzRaU2em5qMa6YLh9eMJVtMeLIcWXVJQ_wCR5ez069tg-hAGmmALkLEexYSPzVF3VhXS9F5yh7Bth4GE8p5i7V5xjVe7ZzLdzADpvLgoUQaglx2vcdEvNKsVePloRjUxlasRJgWSYCU0q1HisrnJJIq1UeX_Wu6-u5W4uXlAvSFlXiQernM_VY4ON0F72hohjOVfh2TP2lxuG7oVx_4KJGN75goXdFOn1ir2g24H2YTfd9WbRJcmxPFqoJrAxqrb8WDMlGhfQ_2OGPg8iLIHi7W8XBkZjkD0BCatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108332" target="_blank">📅 12:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=V53JcAMwFoE9j8uxE8hNO0HzHFVKTffA-0lhFwlXPqqsIQJqUOjPRRtVx-qX6kSIe89RemnqTZeKst4_9u79SGSsTlnO2ijVI_jb07NP3i2CM6WTpZhl0GPUakjhueJJ492P4y8laVTKefEzUX02ilvGvO9lTuRMsaqlPr1eQTrG8mVp8YfZ9oySJtyt0Fivah00Swi-T6_DiG2StkXcTAReym2YjqJb2_CjYAvyClZn8XEOaYNVq1dgqxVBu_P8pPuP-e0bu3HL3B9NBh8EBV8FcLLIvLBzrk8q69WmHTxrD4wbli2T4AIItKfgoTzVXSvsx4i18RSQzeQb97kCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=V53JcAMwFoE9j8uxE8hNO0HzHFVKTffA-0lhFwlXPqqsIQJqUOjPRRtVx-qX6kSIe89RemnqTZeKst4_9u79SGSsTlnO2ijVI_jb07NP3i2CM6WTpZhl0GPUakjhueJJ492P4y8laVTKefEzUX02ilvGvO9lTuRMsaqlPr1eQTrG8mVp8YfZ9oySJtyt0Fivah00Swi-T6_DiG2StkXcTAReym2YjqJb2_CjYAvyClZn8XEOaYNVq1dgqxVBu_P8pPuP-e0bu3HL3B9NBh8EBV8FcLLIvLBzrk8q69WmHTxrD4wbli2T4AIItKfgoTzVXSvsx4i18RSQzeQb97kCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای کروس کجایی؟ رئال مادرید بعد از رفتنت دیگه پادشاهی نکرد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108331" target="_blank">📅 11:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=SeD8FW3IUVnUQS98SWctDI0rn92W5Zo4zkWHAxBJc7qtulhUMyd50YZpJvMkE1OYiUfS9YEnafXkqXgHub7zc5R4YcQwpHzhHDWDI85dDBm26vj5TjnkKPnsztp03q1PQvCft14DXgarYmF8YjXPiUkx1TRUCOQeY4iv28Gf7E6I0MHW3Thpnx7bCQSv1N5joeymAA-yab7eMJs3QSdd0kJssnKsG3SRIOlV1fKfyPFfv0E89-jeTOL8yWxaWaDkrnJfQ0s0aAUyyaAMuy0Cgkzsv0P2URFAgWHbLHRZNfbk2tHlGvuf-TKIWjJPEcD4mmGyOePuRV4CsHBy78N40A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=SeD8FW3IUVnUQS98SWctDI0rn92W5Zo4zkWHAxBJc7qtulhUMyd50YZpJvMkE1OYiUfS9YEnafXkqXgHub7zc5R4YcQwpHzhHDWDI85dDBm26vj5TjnkKPnsztp03q1PQvCft14DXgarYmF8YjXPiUkx1TRUCOQeY4iv28Gf7E6I0MHW3Thpnx7bCQSv1N5joeymAA-yab7eMJs3QSdd0kJssnKsG3SRIOlV1fKfyPFfv0E89-jeTOL8yWxaWaDkrnJfQ0s0aAUyyaAMuy0Cgkzsv0P2URFAgWHbLHRZNfbk2tHlGvuf-TKIWjJPEcD4mmGyOePuRV4CsHBy78N40A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ختم چالش رو اعلام میکنم
🦦
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108330" target="_blank">📅 11:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=EnpKfb3s6aPYV0V4kpqUo6laH5q7NvO7Vc8D2wQ7WIFQdAtxy8FVe6oUhRpiUZKmLN2mbH8CPi1IrmuGqE77aBTMiAz0WZuJWslF9r_-nzUde1bsrh8sKKbBgfgRiGRto1sa8SDr2O80yF4P4np3kJuPEtMR9F-k_4gGVVvbnVWjGEiYd6hxBxPGmui8eGvs67CE8zepu6bTmx0IS0g5Dh9WryURdbawwqjZkzwf7TRX9XaEt_GUopnajB9xtapdUsqmAIllemoT9CNPoaNT6-xKtUjkgi9qgqYRhzNH91Q11KN-tPpaZmi1dee1brHtT5jDKCoH0wBl81WjM1Ey3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=EnpKfb3s6aPYV0V4kpqUo6laH5q7NvO7Vc8D2wQ7WIFQdAtxy8FVe6oUhRpiUZKmLN2mbH8CPi1IrmuGqE77aBTMiAz0WZuJWslF9r_-nzUde1bsrh8sKKbBgfgRiGRto1sa8SDr2O80yF4P4np3kJuPEtMR9F-k_4gGVVvbnVWjGEiYd6hxBxPGmui8eGvs67CE8zepu6bTmx0IS0g5Dh9WryURdbawwqjZkzwf7TRX9XaEt_GUopnajB9xtapdUsqmAIllemoT9CNPoaNT6-xKtUjkgi9qgqYRhzNH91Q11KN-tPpaZmi1dee1brHtT5jDKCoH0wBl81WjM1Ey3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جادوی دیشب اسطوره لیونل‌مسی در اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108329" target="_blank">📅 11:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=sj2396rF8OiAMwWuZb0pTihNRiY7973YTuOEUShkFGYl6Bi93BipvAz09yHI7uwPDV6Q9-bixvQp302UYULLmkd4v1uplZXGGPIt-mDlwDpxCHAgYAcb_rR8OEcUeEeCcnbqP9aZee1Zy7x7ZlWHOEYrXcXfrJoN9onVScELMEqXD1PVWicfmTl1GOR_7AaUyurhTzsMLeyYd4VUh0nkJwpQLN40hWfajlWAk9bPtLTSejigf29GoZMr57T3jiGz3sHvXMNQrVY6XxYHgc_ldOR5gMRR4zcAjVNWH49iuPTbfAZrfPppDhddIBQpSRS1V7bYceG7imyNUYmepTJBkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=sj2396rF8OiAMwWuZb0pTihNRiY7973YTuOEUShkFGYl6Bi93BipvAz09yHI7uwPDV6Q9-bixvQp302UYULLmkd4v1uplZXGGPIt-mDlwDpxCHAgYAcb_rR8OEcUeEeCcnbqP9aZee1Zy7x7ZlWHOEYrXcXfrJoN9onVScELMEqXD1PVWicfmTl1GOR_7AaUyurhTzsMLeyYd4VUh0nkJwpQLN40hWfajlWAk9bPtLTSejigf29GoZMr57T3jiGz3sHvXMNQrVY6XxYHgc_ldOR5gMRR4zcAjVNWH49iuPTbfAZrfPppDhddIBQpSRS1V7bYceG7imyNUYmepTJBkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل یک فوتبال
❤️
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108328" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108327" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ9k5_eRGYE0M-yGkQJTm2LiExCp7rlu8u7bwxd7a92VncuZc-QxdkfUlGWlLYfeh1qqwv80pGpZVRkF7t1ueyJ01n0UTerd2XVQ-Tru-gcTcdH5JYj8v2qPRT8JFQof1xqWyHFQbU_avzYi_js5qyipncnhaPaVF7gXsi3uMUhYnqaQiRdddbYO2EFKUMh_GnF0Q4s034AyW0Lyb11Hb-Y6RIuj-bo1z-08GQR7ZLNItg14ZKYVVuCeP9Kl3A1GTopPn2EcvThfx4n10X4KKex7KL82J1TCy6_42mApCKy2XAdR_Dcr0E4tGj4Z3LCaNfW9q25Ys8YSw1oMB0gZnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108326" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZeGhxiUVchO40E_G2JM0xcv50z76mB7a9z016yXmHcKKWWhw0HgsxEw-Yc08-Y_ss7df9ChUDnSdsB2bCQRDnZ_9fCEG25oNOc2pU8gRJMMY6R35dBS9OxLWOX85qyuYJJGEecQkPIsNmoCF7b1z3d_MvQffD5IsHseAJ5arakbtHR_Sm_pGudL-cc8-lW4SMEYL4pJUdZhWsqHYvFA7DjvFO4waomUxpB8bE01V_F3HFBM8fVWIv7nHebRhmEIaCUOW0aj9QfmHWFmChD8CWxeZO12isGnjqL7_tTUlQsR2WbJcCJFGLmUW3f1Y0HAmYAR_McJjWNgA8zIBF1VEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108325" target="_blank">📅 10:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=rsclSvMsOBAV5KykkIWm1CdXPVJiqP1ZxnblT8XglLe4qm2OiAYpA878bb_ahgb1B2I4JeidxMrCRjXHAXtEhwE1wK68SCWIzu6srgbLcyeZ1bfEJzsEPxQz8Rx6eGpKP-MwYgFXt7AG-dEQZaTt21GMA_gvfeemVKxEwnUQoysljfSQ077Mryoz21GHGEBuhf1yrJ0BU0ZMseFYsUOCMraVzuwILdFQkCTBWvkay8uLW2ZGgM-yE23ROMvphxEMc9ZmpIrHH7fuPwEjECMxXRanPZN1oBfa_DR5MwLu4ZNCfD1Ewv67iEVGSMLKbKF1m9zCnpvSTYY-onVNJ1Kwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=rsclSvMsOBAV5KykkIWm1CdXPVJiqP1ZxnblT8XglLe4qm2OiAYpA878bb_ahgb1B2I4JeidxMrCRjXHAXtEhwE1wK68SCWIzu6srgbLcyeZ1bfEJzsEPxQz8Rx6eGpKP-MwYgFXt7AG-dEQZaTt21GMA_gvfeemVKxEwnUQoysljfSQ077Mryoz21GHGEBuhf1yrJ0BU0ZMseFYsUOCMraVzuwILdFQkCTBWvkay8uLW2ZGgM-yE23ROMvphxEMc9ZmpIrHH7fuPwEjECMxXRanPZN1oBfa_DR5MwLu4ZNCfD1Ewv67iEVGSMLKbKF1m9zCnpvSTYY-onVNJ1Kwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نادر قاضی پور، نماینده پیشین مجلس: تراکتور پرطرفدارترین تیم جهان هست. از رئال و بارسا هم پرطرفدار هستیم. کل مردم ترکیه و ترکمنستان و آلمان طرفدار تراکتور هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108324" target="_blank">📅 10:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=DgtHdXnSE7dHNZL2W2LJbuX2huNeWW_ekpU4DcpFWUE5aqzAgEYtdX6yCe6qbJmvlyM3iss94bXohYidFtnZZlkavu57TFMpsdtXcGtwevgErO6kc-jTGABQbapY02e0xYsVFTMKnGUvzGlMEyJHEIHCJX35guVDGkJdixvVlaDj5YPlUQPKuQqpnILkdmpwUblKT2Yi2lqGaoReiANBx5j2BpEHb0jpurWX2L-kcKHGKyjtqateNkwuayM5y5ddprCcvIWJq7Tug2qVc50vTMjKdhza4piyPCJY876AcfiaQ86MZJJ9rMG-YCRFLHCusnOlWZQWQNmxqpqNThM5UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=DgtHdXnSE7dHNZL2W2LJbuX2huNeWW_ekpU4DcpFWUE5aqzAgEYtdX6yCe6qbJmvlyM3iss94bXohYidFtnZZlkavu57TFMpsdtXcGtwevgErO6kc-jTGABQbapY02e0xYsVFTMKnGUvzGlMEyJHEIHCJX35guVDGkJdixvVlaDj5YPlUQPKuQqpnILkdmpwUblKT2Yi2lqGaoReiANBx5j2BpEHb0jpurWX2L-kcKHGKyjtqateNkwuayM5y5ddprCcvIWJq7Tug2qVc50vTMjKdhza4piyPCJY876AcfiaQ86MZJJ9rMG-YCRFLHCusnOlWZQWQNmxqpqNThM5UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
بیژن بزغاله 2008 روزی 4تا رونالدو و مسی به عنوان صبحانه می‌خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108323" target="_blank">📅 10:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108322" target="_blank">📅 10:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇮🇷
🎙
رسول باختر، کارشناس حقوقی فوتبال ایران در گفت و گو با فارس درباره یاسر‌آسانی:
🗣️
درباره بحث مندیت از آنجایی که این موضوع به منزله فسخ نیست اصلا نمی‌توان به آن پرداخت. شاید باشگاه پرسپولیس بخواهد از این سند به عنوان قرینه‌ای برای اثبات فسخ قرارداد استفاده کند که در این صورت باز هم فارغ از اینکه فسخ صورت گرفته یا نگرفته باشد، باز هم تفاوتی در ماهیت ماجرا ندارد. چرا که آسانی بازیکن جدید استقلال محسوب نمی‌شود و به همین دلیل از نظر من بازی کردن او غیرقانونی نیست.
🗣️
اگر بخواهیم طبق نظر فدراسیون فوتبال پیش برویم که مشکلی وجود ندارد. در زاویه مقابل ماجرا هم حتی اگر قرارداد را فسخ شده در نظر بگیریم که بدترین حالت ممکن است، باز یاسر آسانی بازیکن جدید استقلال نیست و قاعدتا نباید مشکلی برای بازی کردن او وجود داشته باشد‌.
🗣️
کارت بازی بازیکنان توسط سازمان لیگ و فدراسیون صادر شده و نبود پروانه کار این نفرات در نهایت نمی‌تواند باعث تغییر نتیجه یک مسابقه یا اعلام غیرقانونی بودن حضور آنها در زمین شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108321" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=VbZA9SMp-0s4G9T05RrXoMlCcDfzruKTa2CAkAB2hEXGPIrhaSCHkwtIPCvaNrvkNMKNAan3_hUTpnSO6Y2fK-I9uW8t_CVoINA2NvgAX7qSBlbV5tICql4ZhmxQp5JspdnfHkBnxEMGQhvV82HefHZ3TvIQZnwFgvBIORCVXssw1HbfJHCKBe7nPvgVSv6jUKyd3q3k0fwMGCJTf0UYf6EJNPMKZqoZj8Aoc1pynAklZP_osQI0Cc7PLbpJNnlB-A_hS0_I4JdwRTLcZaVzLLzkiWkxKY8lPOaejV5yKoPgn5pu6ReX60TVEG5u4YY3pUxna6i3f_Bz_ApnkL6ZEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=VbZA9SMp-0s4G9T05RrXoMlCcDfzruKTa2CAkAB2hEXGPIrhaSCHkwtIPCvaNrvkNMKNAan3_hUTpnSO6Y2fK-I9uW8t_CVoINA2NvgAX7qSBlbV5tICql4ZhmxQp5JspdnfHkBnxEMGQhvV82HefHZ3TvIQZnwFgvBIORCVXssw1HbfJHCKBe7nPvgVSv6jUKyd3q3k0fwMGCJTf0UYf6EJNPMKZqoZj8Aoc1pynAklZP_osQI0Cc7PLbpJNnlB-A_hS0_I4JdwRTLcZaVzLLzkiWkxKY8lPOaejV5yKoPgn5pu6ReX60TVEG5u4YY3pUxna6i3f_Bz_ApnkL6ZEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
پاسخ زیبای سیمئونه به سوال درباره مقایسه مسی و مارادونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108320" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=ve2PvNmuBqf13LsCkopI4S-uJqQWrr2F6joxdvz7Uf_fkfwgv5_9CRXUaueWHDo9H-YyGOCxNj3zmKhHMV3OLONRTOoh2Tzbxgnx2x4YVEURBDBchHDkDupXEINF0fm1c1vKp1z9SpJYipA7nDkbdsyBwTApYaZa4NQxYUzpXMFnLL2C222QCIL-fT58jY7lJCZ3P5289c-x72wJ5rjfXGHDP2OPAXtyH2IyrbD9uROqbrgJyNqmhYGfHxE3YdGnCMtmryFsveiSGz9iDzoZ7XRWevWqbXNE6nmwVG7nAmkwJ0lN6mBeS7_nToP5FEjiJlhAH2J2aIhmELPASL9RNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=ve2PvNmuBqf13LsCkopI4S-uJqQWrr2F6joxdvz7Uf_fkfwgv5_9CRXUaueWHDo9H-YyGOCxNj3zmKhHMV3OLONRTOoh2Tzbxgnx2x4YVEURBDBchHDkDupXEINF0fm1c1vKp1z9SpJYipA7nDkbdsyBwTApYaZa4NQxYUzpXMFnLL2C222QCIL-fT58jY7lJCZ3P5289c-x72wJ5rjfXGHDP2OPAXtyH2IyrbD9uROqbrgJyNqmhYGfHxE3YdGnCMtmryFsveiSGz9iDzoZ7XRWevWqbXNE6nmwVG7nAmkwJ0lN6mBeS7_nToP5FEjiJlhAH2J2aIhmELPASL9RNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
گلشیفته فراهانی توی جدیدترین فیلمش از جان سینا اسطوره کشتی کج و قهرمان دوران بچگی خیلی‌هامون لب‌ گرفته و حسابی خبرساز شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108319" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108318">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=IT0BXCiv3BmRqyDYhnHNWEh-XVHN7oS0MlbTZHP5UGuiZfIJzDN104LQNRp9Dd54NXc8EBSOYEznEpXqxXE0YK2ld63oJNdTonJj_5rbzU6Byn-buvuK5AQgxn0t2yrecNZwn-sZdrSpdny0Y-dGPVFHBeSypA6VFs9SeHDcEw1zKKFZwBI-7fY8yNZMVk58dLbmIjlJfREWaa8AJ5hsDpCmVxEM52ITRc6CRDPV_nfFbccPSVFK9TlSYVwADebuFX19RGClZp-fNyghYH7M84J37xrJER4UuUF8Ok8646t_vpDOGyiHwiwM36Phrv3k14JKRGmghk2fEyOHWdN2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=IT0BXCiv3BmRqyDYhnHNWEh-XVHN7oS0MlbTZHP5UGuiZfIJzDN104LQNRp9Dd54NXc8EBSOYEznEpXqxXE0YK2ld63oJNdTonJj_5rbzU6Byn-buvuK5AQgxn0t2yrecNZwn-sZdrSpdny0Y-dGPVFHBeSypA6VFs9SeHDcEw1zKKFZwBI-7fY8yNZMVk58dLbmIjlJfREWaa8AJ5hsDpCmVxEM52ITRc6CRDPV_nfFbccPSVFK9TlSYVwADebuFX19RGClZp-fNyghYH7M84J37xrJER4UuUF8Ok8646t_vpDOGyiHwiwM36Phrv3k14JKRGmghk2fEyOHWdN2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت هوادارای بارسا در این روزها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108318" target="_blank">📅 08:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108315">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reMv5NZUszivG90j9eyQjsYI6hTHrxd0lHc0HhCf4SaXqgIdlGcSOhOr9Ju1bvrLpGRlBVfYN09l6SPdimLBnVrJziifhpuE8HAgs-RdE9-qWq1W51YZpjQRIjrl4-yuW6fSkC9H7UmOmhHH3L4MCxKwi6LOSZmWogAmh0JiETMuyRnrZKFLiMtOtwfCb3xj6XMOfnDUuhaJz4A9W9RusUWE5N0IqcXy8NzCkUkgcixCJiZ4IdpsZ6qrBEAj1oiJKh2X7mflxr9Od3W6wZiORZvn36zkV5N3Rv1xCzN5lhNgn9ZGxNKvs_oQ09kNL7k_aVzBWBn4helcyy-vi16blg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
وینیسیوس با انتشار این استوری نوشت: همیشه تمامی صحنه‌هایی که کارت زرد و قرمز دارد متعلق به وینیسیوس است‌. چه رسوایی بزرگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108315" target="_blank">📅 01:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108314">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwxBvpKGyyceBQsOu7kXE9Q4hXYAYMNjwRU9NqpY3xauoVHFBA1Zz6XBG0v_BiyTRtd7WdimafKhH19FWsvjL-dJoYxyRnOSYWJ7WW5Ea9f2T_aThEVQIKTWt5jsw9LtHYpB1eDq1RoJnQ51CGriaJr_WGiLRJ9hHoVFCkQiO2c-G5ibhpVS6n7mrKiYedZr8sXew1Gju0v26sePG1pH5Bj6i4xCbLBsQ9xMVbDnBB12aU4M1El5UY94qh7uws7pwYUrNocQK3Oz9BG605rZenr0uAOXEYV8_33_WZ2bVsk4N-tk48HWAUgOQqNfVFX_FxEU3zEQwC9gRHsEydg8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🟥
#رسمییییییی؛ طبق گزارش داور بازی امشب رئال، وینیسیوس بدلیل پرخاشگری و رفتار غیرورزشی از زمین اخراج شده و دوبازی بعدی رئال‌مادرید مقابل سویا و بارسلونا محروم خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108314" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108313">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIYt0nmRqPNTMyE49i73DIkATMYrgTIa-tA1-p-4tG2kxKLVRsbrE_X4cj_U-15SZlwMDuiMQrvKjRgVnmI8ebfCJe9vxL6UtlIRPBrxQXNl3LdfywEfR9hErs9rqzROsCg_Jx148axvHBTpXNCKW1-0EIqmKskrUqtGKMOg3YoF5rG008LwL_Kosvh8gAZH6oLNhSIw3aTnBMMvK98w8q4suB78IbytHTLxOxx6lYi39auLfrogxkIt8i1xBvgD6Kny4qkgFPPXhYEORKk2pUdbEJt04Xgl5C5zSkkgHq_G2pYWRkffr-Pb8apj8f0od5QyBT75723725FCrISq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
وینیسیوس بدلیل حرکت غیر ورزشی حداقل ۲ جلسه از میادین محرومه و الکلاسیکو رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108313" target="_blank">📅 01:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6VlM47PpBLb_wDqjDY5LjH0D9ePhzF9qS7QmEL_RlDkGWrcYI2wB_u7eLYyerIl07V9r-80eGGdvEYjFuk0fHQHnjpLrfNhY_AlKahsECL-MG2IkoyyDRWVO9K1sliVznlTYRkYBPkTHrBv3jP0czrjE3fAXEjXvyIuO9sAKSHx6PnwH4MNddukjGzB0x7K--VIjcm3oJ2cydvrHrSbgRF2VvIZuzDzyGGeAya8YHE8r0G6NVnYpw5XhH9sfiUPtjPNLojq2i_wNeOU-ZWZK4daJJ_4rKojcaGdHkP8--_cY8e0EB-c478BQBdfxb7TIZCAtZwCZgJ1tbi-SMQgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
🇪🇸
پست وینیسیوس در اینستاگرام
: من هنوز هم خوشحالم. می‌خواهم از هم‌تیمی‌هایم و هواداران رئال مادرید عذرخواهی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108310" target="_blank">📅 01:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108309">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0k5R5aBw6ry21sGsWFV8_qIUlEtLsF-3A5DDi7VQtE6Ru2w7qMj4_uDRCHVJyskbidrYLzb2CGjSf1aB1-hm-K83kNNn_ZrN1gaEkqjiR46RF9dMprhPqSz9PucIDl3CL2XfT-PftoOwJg9ztR6Fn1cTuXcDA0yfHxY_2cl5srqbc_kmXPI3zZIRJeGm-pKPF5sdDFuE1QDbpchaYNsS47oaAHNW3jV5jLiwYjN4szjI6UMA_lYBjFUcbUvuhgnQIIzNpq1MxHTMomfFc1jtNIWe-qhcj1HHRnnoAmDMuh5oPUsJhaR1PpS1fDy4n5WwJiq5xfeza3lezSDyh5MdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو بدلیل حواشی مربوط به وینیسیوس و احتمال غیبت در ال‌کلاسیکو در نشست خبری بعد از بازی حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108309" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HheTd5D1oOYDVNkPzdedwWkoJyUBK-Q0-KAt9l30Eqfm7JqUgs6Ddx-0xHJkDdgt6wdbibw_izOTmb5LFi53FIGExCiKuU4CtqgBfkFvV0PXJ4-pCssBmc_h3lzK80ZzITPIc-FArneVHhGFabHELnBZL38Z5bWLQ9zd5y3k42sgv4JcM_f_1PC8oS54PT4_BbAVL7sUxRWe_RDCEzyDNjZ4VbbCf5JGThKdYbagP-5ayiaSe_9WYlbuP-a93dzQrEwd9ejA4H7jiEsXqEHEHANBMaiYpGKqc6p0N0q43mgWbtt2tZH0-gDi2myxPrgOTA4GmW24ksIvIB7q0PF4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری رودریگو بازیکن رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108308" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108307">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
پایان بازی با برتری رئال‌مادرید مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108307" target="_blank">📅 00:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108306" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/108305" target="_blank">📅 00:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/108304" target="_blank">📅 00:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRGWOX_WcnKvZvshrFrfFbGY4QwlHIaoZt0UfCzzQ_kUQDv_O95pcewmEvRhdbecDhJNwbHb97nRuscwSieYcG6q0w3rInlHz33s2R5W5Hcz9mvV9pySgKLsg9hT20nn8JIV7WJxDWFt6G_XM1nPZOdAMMRnVrmKS_Sk17qm9OpCor-qGnfg0z61rICzEkuiJhHLVNnV5exgS2yPNiKxrD3bsu55S1yXEWSK7ymLSvga1646rYLO44dIkk2zanMbLyPh719Cg5HudH6tYmEVjjznQTBwz8bQNEiTcV8tdowkQlUS_7oXA29TxtbpvTpUR58PA-uW-iVyK2_kVInemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/108303" target="_blank">📅 00:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=pOV5MLLi4CqTY1FpsOe_9Tsapxttq56CsbhKKZyKEIguSJYzm9IWX-1FuwS9QiLysnqJ_eIIKWuZkH2VOniUArM9zeShYsB5VMXBMHnECx7L_E8DiWMJmbulg3n-2-DsW-lwcu1IT96yCZ3u__qtaFEVD6c1-GBmF9O-qJS6lbXUYT1Zuajr_ICpFnYZyl5VJEN7ktfmmxaXDRHLAkmvmAr4gqMfs49fCKENZD5sw218ugSF4j3KN0GrcWO53may1ltVzRkJ-fV1L-Sh9mGu-YFDXl1puKXYxd3p7aEY0kstNcLBRLaIsBII6zdMGwQTiqVTgVC6Z6aScbQdKiV4FkjbCmfA5I63Y56CrGExm3VkBKzxuEXHqvAAfSXcjkO7GLHR2Lq48gM44Ajva2c-fPVOtiqll0b_3y-H9qFjzr0rYmBjbsuvBX7jPvUb7az5sus7X9xcNlZEqBdJKqcRd8yXRZv4WRM_1sVTybhkB7s4g8wfMrbvQajvpz2yWoWXTumVprsdluXP6cJi-U5t24BhKjkHTfN-1wS9MFhTHX-JVbfj_6bViX6X1-CYmzzy_ofI9q9q5Km6jn8tIAlKocQf_C7CWBJZDDumTOu0ymQcBReHC2j1y29VWfvDxbTOinTvHp2FilQ1R5YxA7TZ2KZcYyeAoveY-SYH41NBcDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=pOV5MLLi4CqTY1FpsOe_9Tsapxttq56CsbhKKZyKEIguSJYzm9IWX-1FuwS9QiLysnqJ_eIIKWuZkH2VOniUArM9zeShYsB5VMXBMHnECx7L_E8DiWMJmbulg3n-2-DsW-lwcu1IT96yCZ3u__qtaFEVD6c1-GBmF9O-qJS6lbXUYT1Zuajr_ICpFnYZyl5VJEN7ktfmmxaXDRHLAkmvmAr4gqMfs49fCKENZD5sw218ugSF4j3KN0GrcWO53may1ltVzRkJ-fV1L-Sh9mGu-YFDXl1puKXYxd3p7aEY0kstNcLBRLaIsBII6zdMGwQTiqVTgVC6Z6aScbQdKiV4FkjbCmfA5I63Y56CrGExm3VkBKzxuEXHqvAAfSXcjkO7GLHR2Lq48gM44Ajva2c-fPVOtiqll0b_3y-H9qFjzr0rYmBjbsuvBX7jPvUb7az5sus7X9xcNlZEqBdJKqcRd8yXRZv4WRM_1sVTybhkB7s4g8wfMrbvQajvpz2yWoWXTumVprsdluXP6cJi-U5t24BhKjkHTfN-1wS9MFhTHX-JVbfj_6bViX6X1-CYmzzy_ofI9q9q5Km6jn8tIAlKocQf_C7CWBJZDDumTOu0ymQcBReHC2j1y29VWfvDxbTOinTvHp2FilQ1R5YxA7TZ2KZcYyeAoveY-SYH41NBcDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108302" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdDr6fadrhIzf-b8ptsNXGkeL5QxDv_F_OSYw4fEPJPxvk3drD5WZoxKc-q9pE80SmOYbNM7bj7RcTBM90nrpIkVMPDRdS23vdGjOq2K4DKKgrg0XZp2WgH4by_wClJrKLsViCBQ_WGJrFsmN0bVxYXC6kIxTHpN3lc1OBWKRZPKZF2AgyUWGt6BxipOhkBhB_ywimvzImKTV4Xopc1KUzXSpUCiqX5fd9FM6M__Fi0sUbAZf9VbBCEVMxQ-xSsui4DeFmeDegGwnoAryu3mOobCvOgYOPjSckc3RbD4HMIaXWCPWYPVjcyc64LKTAFO_LKtQ9_itT7ZHsy8HVsuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممم بخاطر این صحنه اخراج شد
😐
😐
🚨</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108301" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGzDgSdBEpsIGTi7jik6s5BOX6Wv_65GePYENg5ENyZNnNAhl5izMcOeaWXrxYNGlF_CzIJ_ScpFGRvKi_5lziBL-kp_QjLMGEkQWkiUr3foxsu5WBN0ufeZnzMBJ5EAyb06JlwIC0IpcS3Wf6HCTXkYJ0L9seEXKxax6s8-vXVnGg2KEVZf-i63e4YHylIpRBaz4keY1cgeo1-dXOmlZaHhFbS_9D_6dZdmHjiQummR2DAAb1bAFBEi5FiJYZgCXfzaqfVPkZkpQCHh_b2iLad6M6ZA_8xuxLsRxO7XbmYloGuuzA3udxKf_Fn6E3mu_HcJNjoZ8zt_B3UJ5x8ykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس اخراج شد
😐
😐
😐
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/108300" target="_blank">📅 00:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108299" target="_blank">📅 00:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108298" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگللگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108297" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=SdIYLl0Cqr8zobDqeha1iy59uaueZ1dGpT8EAW7z_ngvdAfXpCpHcp-yqHZ3CzvbAkHEG_7MIaF1KFXnXCzfFEQK6826GuzbH2ZxaY3QxNQ7UfsJwi5jGHatElTepLxa0iSZi8pCsCn-GJoVwOVLw3Iot1y_KzNWnqY-AHCbr0dvVJE6aFstTpjVOG8zRjAakg-qxp_zPc56lvaFl3y3roZ_pSTGNggvuKeepu_Y_dtcdI09Zv8e5QOABK0FnIv2OOeeDm51kyzOVia64ta7ZZwPb9ehGPNMSONKl4CyTZSAjIHp0PiSNhx3sgCHzkUY0i1Ku7EnX3wmQPBG4lvH-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=SdIYLl0Cqr8zobDqeha1iy59uaueZ1dGpT8EAW7z_ngvdAfXpCpHcp-yqHZ3CzvbAkHEG_7MIaF1KFXnXCzfFEQK6826GuzbH2ZxaY3QxNQ7UfsJwi5jGHatElTepLxa0iSZi8pCsCn-GJoVwOVLw3Iot1y_KzNWnqY-AHCbr0dvVJE6aFstTpjVOG8zRjAakg-qxp_zPc56lvaFl3y3roZ_pSTGNggvuKeepu_Y_dtcdI09Zv8e5QOABK0FnIv2OOeeDm51kyzOVia64ta7ZZwPb9ehGPNMSONKl4CyTZSAjIHp0PiSNhx3sgCHzkUY0i1Ku7EnX3wmQPBG4lvH-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
گل‌اول رئال‌مادرید به ویارئال توسط دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/108296" target="_blank">📅 23:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیمه‌اول بازی رئال‌مادرید بدون گل تموم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108295" target="_blank">📅 23:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
واکنش علیرضا خمسه به ویدئوی «خلوت کنید آقای خمسه هستن»: من پول بادیگارد ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/108294" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برررریم سراغ بازی رئال‌مادرید و ویارئال</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108293" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYL3j1otkpdn_NQYWWtMF4HfpjKUl3OeXMsDWBg-fcPBNWiEEuhIP8m0n3P7mlGnZFSfywCn8excBAv0ofwg6d7l2LcXae6jJ9i9HTnbFWtIcHZQzaLPasPbJAB3WH2qfgtmMna_8JIoZpozVCVxzs3ucMtg-vbFC31jClUWH4NyrVzapxS6efgk5TccutUQmSPbPYLkqiDK46kaLTQhIq1DSF3IFnO36mlyE3YrGKhVLPGrk2LyP7OYqKOXvt9MdXplf2mT0QbIjQL-Aqm8V2c8pWWIwTMgOmsFbpqbDzr4HzWzu0FdaJVOpJ_bDFIaqB9hBVZtjGqCW2KPahcA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هشتم لالیگا؛ برتری قاطع و آسان در خانه؛ بدون حضور رافینیا هم برنده شدند
🇪🇸
بارسلونا
3️⃣
-
0️⃣
ختافه
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/108292" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyk7x53sD2bjrBnpaN34f9nsx7HtqD2_yue0ePXItZEFWYCxe76vVPncg4dqnWpmOP2AND_bU7-8E6ny5MlbGilZuAehMGqXH9OIFAXh-Lc4PkaLH8IvZ3sgJ77MxJb8fLP0CCJAAoAtnqBfmSI8YlxvxOMyN0iR-4rxcJ0DOGxNGC3w6h6yLSRcg0jZEp9Jd1FL0oY7WKdY1TIb4xOSs_tgZKImLobc8w-JwnhFWhBKSesrMsr98JKnly7EnqYkzfQOa0ulh1J9Q6lsca-L-ZCK1F11ucmLM5a0PHnMQOPjotvfWr5oaC71N40teH5fb-eUU3UrOzjPUoVRjqnZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ برتر انگلیس| منچستریونایتد از پس تاتنهامِ ١٠ نفره هم بر نیامد؛ مساوی که به درد هیچکدام از دو تیم نمی‌خورد
🔸
منچستریونایتد یک - تاتنهام یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108291" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=g0qPPPtg1-zGPfAri5Hw1gK3LNyMPzaazpVX01q79ImYVGQQtMnADwHOStKU8v36-IQYH_dhO49NjXizgm6XOUtfHmulFUzp_uhE-cnoJQT1R-rvT_PvYMdGc9fhPR3wqEO-BRWhYFWl56_31UgkIvbkZ1aDC2aIHrCipJdpkPMN4uflmunMke73ernJIqS84CuATHrWRDCaowOBZrQkl0pSWo_822Lvbv13VCoXrfsrqF7jPOLkrp2wsDFso9Po53cuTA6-dV6TLZJrqzxvMFWh757cseg_Ak6KVYIl84FK7-9jnujPXNBfWtSWrBb1QhUrPxdaz1yALm8zZMnVNpxJnM611uggx2DlOC01Fe8bEneOLjR7wcMoPSEzFlCPj7-TkhNuuRYOUgVskgrnhSfH3POnrYWAOZhhb6e-3FAHqIeFhAmk_JkKgdgudwiWOTbiERafkgKdNCmQn3pNXgA_QF0MiFwxtGM90hzzVCXNbZJTvSxOiO1arAXNHW_-3voQbp4UHb0KAZKh7Llq6J15ZSTmOsuS1MqsNeJjnM54ChaW-PyOF7MxADg4AVOjCsCYOKTBMqykfZG5A0J7iKcBbg2sYbr6TSzM-qvDwyMneW6YUcHo9pTK4Xc5ewcPpoqF4TveZHZei3GCK4lNw7N-LDC6gRDWXAmb4WK-IDY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=g0qPPPtg1-zGPfAri5Hw1gK3LNyMPzaazpVX01q79ImYVGQQtMnADwHOStKU8v36-IQYH_dhO49NjXizgm6XOUtfHmulFUzp_uhE-cnoJQT1R-rvT_PvYMdGc9fhPR3wqEO-BRWhYFWl56_31UgkIvbkZ1aDC2aIHrCipJdpkPMN4uflmunMke73ernJIqS84CuATHrWRDCaowOBZrQkl0pSWo_822Lvbv13VCoXrfsrqF7jPOLkrp2wsDFso9Po53cuTA6-dV6TLZJrqzxvMFWh757cseg_Ak6KVYIl84FK7-9jnujPXNBfWtSWrBb1QhUrPxdaz1yALm8zZMnVNpxJnM611uggx2DlOC01Fe8bEneOLjR7wcMoPSEzFlCPj7-TkhNuuRYOUgVskgrnhSfH3POnrYWAOZhhb6e-3FAHqIeFhAmk_JkKgdgudwiWOTbiERafkgKdNCmQn3pNXgA_QF0MiFwxtGM90hzzVCXNbZJTvSxOiO1arAXNHW_-3voQbp4UHb0KAZKh7Llq6J15ZSTmOsuS1MqsNeJjnM54ChaW-PyOF7MxADg4AVOjCsCYOKTBMqykfZG5A0J7iKcBbg2sYbr6TSzM-qvDwyMneW6YUcHo9pTK4Xc5ewcPpoqF4TveZHZei3GCK4lNw7N-LDC6gRDWXAmb4WK-IDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به ختافه توسط کونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108290" target="_blank">📅 21:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کوندهههههه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108289" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگلگگلگلگلگ سوم بارسلونا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108288" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8kRgrf22z0Njue7zIQRYv5PHc6lXusvDrhhouCnV0CgASzLhPi3icDQ1kO10ZmI_PMStkn2zNJmWRIBvtVWe3PpyMyHtos7SXpplQuB4EbjrCvdZjN59ZhxMn9Qj6iiFWQ-WBgVnMo_QAYp8c8KOlj6Jw5mSsR4rh_xnMBRhTkMIKbDihYpdCaaBq2p12NS8sCLBTiMVwpkNTiKRtVGW9wFbKuLsIKorsM3ZKT6mbPTCf7jzRzMM3C-FxCe-OnEjEiQ2pdrmf2ycPj7VHDmGTRcdR8pisnDxglRUtJmtQzh2a8m-lA8oMIoLI0X2-fbCwmCBC44GO1BNAQvMj2Jeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل ویارئال؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108287" target="_blank">📅 21:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWnJ2vY7uFsIQg0MbGsxb4fWmZMKr2hlcwTHjotOUGmpeJC8k2Yangv4GCAWhavNDhKPdJPFnjVLiGhLMWkEm09xDSldGwrdB2TpGVNzIy6TIoofKWhTxy6LwM2QjKvONvifiwy2m0BlHVFdaHKSJioe6JQZcGUWThLRPrm7fz_hrW9oKfPJkwPrjrLiesiKkPS7VF_882Vv-OW62Xv99DpIcEarLqDHdABXnWJDxcQUl92EaLNpMKaWpJtCGillfd68FuGeCYvdLdRCjZZJVgswfTRoZAlpaJKgvYVPXhYZPGWLYaKTyMjXdwDn3cGQNdOkG3Kj7W_TepXtOkMK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=h4u4baPU5flPjckzWWvV5cTTxwNfCIb5rqVC5Wplp58SDiXbGOqhGT2aRpm8si1W6IIc3rOaoUOdrXeG-Be7Tq2T72H2wqwub84U4EqGe5XqjVedtRaiNkLsbh-0yMAlZbQZ1eBrqZTF22IVj6hiw-IZCLfHtix9DNpM2Y8vO6LzVeF0P44DNb6noQ6YRySXOzNcJmc9PUroxYiOBr0awqtPpR9TUESlXqsf4Eap1fZLSR-ZFqPl52eUeXvNoBOYrxcGoTIdkl-k6eHl-4p5-W7jijMziRf41XFM8q0tiHpP3AvfhXFM7t4sQVXTkvJFYkBrpXIFRSVzVhdKCSjNyTsovJSRmnEmrj9VmmcEjhWvF0N7VWiFq9r11zPscG_edKnVAD-DY7FOzt6wHTLyWncRtJeAQlSJAanwePZpUzaf7ozcXAmBg0BvyL4U9dAyJU-63PTGDaX-4M6I3H2JGdGz6pQ-h_tiNAfaubxaQ_3U6DfhXIHK_NFUITXwtIgyn_UYYN42t2Z3FqyM7NYWIzy4DQlXjceF0IxVDXkVd4AJPaX_EMEMpzAj1FHKMd_vl6P04ZCqm2JZZRG7HUAOUCHiuu-C0jEMCS91NCB0WY-YVQa_g7g7L4-kn7a2J69GAObNLOqfAc7S2eyDIgXq9ymChsyCcvooy8jVLDW7hXU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=h4u4baPU5flPjckzWWvV5cTTxwNfCIb5rqVC5Wplp58SDiXbGOqhGT2aRpm8si1W6IIc3rOaoUOdrXeG-Be7Tq2T72H2wqwub84U4EqGe5XqjVedtRaiNkLsbh-0yMAlZbQZ1eBrqZTF22IVj6hiw-IZCLfHtix9DNpM2Y8vO6LzVeF0P44DNb6noQ6YRySXOzNcJmc9PUroxYiOBr0awqtPpR9TUESlXqsf4Eap1fZLSR-ZFqPl52eUeXvNoBOYrxcGoTIdkl-k6eHl-4p5-W7jijMziRf41XFM8q0tiHpP3AvfhXFM7t4sQVXTkvJFYkBrpXIFRSVzVhdKCSjNyTsovJSRmnEmrj9VmmcEjhWvF0N7VWiFq9r11zPscG_edKnVAD-DY7FOzt6wHTLyWncRtJeAQlSJAanwePZpUzaf7ozcXAmBg0BvyL4U9dAyJU-63PTGDaX-4M6I3H2JGdGz6pQ-h_tiNAfaubxaQ_3U6DfhXIHK_NFUITXwtIgyn_UYYN42t2Z3FqyM7NYWIzy4DQlXjceF0IxVDXkVd4AJPaX_EMEMpzAj1FHKMd_vl6P04ZCqm2JZZRG7HUAOUCHiuu-C0jEMCS91NCB0WY-YVQa_g7g7L4-kn7a2J69GAObNLOqfAc7S2eyDIgXq9ymChsyCcvooy8jVLDW7hXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به ختافه توسط گابریل ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=KOLFvtH7B4YAuHG14Md6KUYepAJCIPD7ke7Ztrb7ynWKRFDRgzfjIB9P4fffscqn0_1H79uK2zU2NyxSld2TQwZ7hUD5AeqfbsW0cr-WNeYOVwSG4HJSUbUW50G17mPtdAgs-6ip2eusxiiSiCFwyfnvX_wC3Vxy1ZZWZST8UrHAh_8tw1aiqQuKakxUZ02GzPEeY_qUzZnWFO1cdeqAVJmcpBpM5nhxtFHiieT1JKaq2qNyfWOjX28g6qpkgd0dXQ4-e_vyWJPkfEaqv7whPp3HG3Ee8ix5o8oIDcYm_Tw47QOSakMkxWwUMQMpvJfFtk7dJBalRoy1Uj5x-6e8Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=KOLFvtH7B4YAuHG14Md6KUYepAJCIPD7ke7Ztrb7ynWKRFDRgzfjIB9P4fffscqn0_1H79uK2zU2NyxSld2TQwZ7hUD5AeqfbsW0cr-WNeYOVwSG4HJSUbUW50G17mPtdAgs-6ip2eusxiiSiCFwyfnvX_wC3Vxy1ZZWZST8UrHAh_8tw1aiqQuKakxUZ02GzPEeY_qUzZnWFO1cdeqAVJmcpBpM5nhxtFHiieT1JKaq2qNyfWOjX28g6qpkgd0dXQ4-e_vyWJPkfEaqv7whPp3HG3Ee8ix5o8oIDcYm_Tw47QOSakMkxWwUMQMpvJfFtk7dJBalRoy1Uj5x-6e8Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=dBjlhgkowI11rlQft26QjVAr8wE090GzsPWFMjeJewN5YqFo4s9iM8Oq4QTUO9N_g0QucBxEV5nUNbWlb5HgkDW-CTT4_2MnDvof8zN0_TOJ4FbD4BAftUT88Xy9k7xVh93iVlbu-zRSodiKgPbRwPmHW-kQIWiPne2ifOnFz7N3aA5csCvWOF3OX4N2gKO6byUJMuv9tbMNLUnD8FR59wyJCSRaq2z6xADHLrgeBTIRDgRKzNucQb5aTcI9mL4UetSUqh3o2ps6HWf8HkaOtTiv4Lu7brC8v7PaX6Mmnx6Or9-n6YbSfYvTB9LX4vjZhTFc9PvMgodxO2LJJoOBuKKWTMbnVcJUM9o7H-WyLzUx4yUgtE3ECt6lJDowA27vpkffPv9BlVrM-QVTaNWF5QOOXKW-brIKM5Q3jj_h_0UJ2247Rt7FY5-cVYa9qdvMcP0iCfMrbUAnitoHG8jat1pjCMpR2jdJzFBYAYfHMNkFYdPJJwB6Er9syY7HrZMSVLw6K4ipCYUsA-xlwWcH72UwKQa8Ri-mfbg8tBeyzmm10awxhoN9vjc9WPTgz124DJsStoF9rt9W8Ozw5qRuwMzOePfp8yJcAt-CteBTEc44LineRwmVA9HEuzne4AYgyQRdQTR9Fx8UNsxFqvwA9WwNmoQS72yYBpS-R6FGqKE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=dBjlhgkowI11rlQft26QjVAr8wE090GzsPWFMjeJewN5YqFo4s9iM8Oq4QTUO9N_g0QucBxEV5nUNbWlb5HgkDW-CTT4_2MnDvof8zN0_TOJ4FbD4BAftUT88Xy9k7xVh93iVlbu-zRSodiKgPbRwPmHW-kQIWiPne2ifOnFz7N3aA5csCvWOF3OX4N2gKO6byUJMuv9tbMNLUnD8FR59wyJCSRaq2z6xADHLrgeBTIRDgRKzNucQb5aTcI9mL4UetSUqh3o2ps6HWf8HkaOtTiv4Lu7brC8v7PaX6Mmnx6Or9-n6YbSfYvTB9LX4vjZhTFc9PvMgodxO2LJJoOBuKKWTMbnVcJUM9o7H-WyLzUx4yUgtE3ECt6lJDowA27vpkffPv9BlVrM-QVTaNWF5QOOXKW-brIKM5Q3jj_h_0UJ2247Rt7FY5-cVYa9qdvMcP0iCfMrbUAnitoHG8jat1pjCMpR2jdJzFBYAYfHMNkFYdPJJwB6Er9syY7HrZMSVLw6K4ipCYUsA-xlwWcH72UwKQa8Ri-mfbg8tBeyzmm10awxhoN9vjc9WPTgz124DJsStoF9rt9W8Ozw5qRuwMzOePfp8yJcAt-CteBTEc44LineRwmVA9HEuzne4AYgyQRdQTR9Fx8UNsxFqvwA9WwNmoQS72yYBpS-R6FGqKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به ختافه توسط آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
