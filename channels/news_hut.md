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
<img src="https://cdn4.telesco.pe/file/A2kF9hvfSXZqGgwrgH2TS0L56pP-y0zKMLjrP3hhl4goqUmxHot539CVnglkH-ym1oTteANtC6OyLXvQ8O3DGW8i6o1rU_LohdKMdEmc4FIgWxEb3KiHQFtVcuUtD5mZ0IcDW-3BHopAUaGqTrCURybNAozAJLwQBVYqEkz4Sy4Fl1wmA8mQ_ermW2C-QNFz66gJZnN5ufHUq6qaWtNzvn_NY8GL_KdtRFT2mnW5G_3mDXMrYJQf2TQ9ZOaWjdgFPKrsAGT-MwRnH81aWP1RzoPXBo1OXdjGlJUy0vVRa7RCUto_M6Z1ZkRHn3XWSZWrN8Hj0jOQzn6WIbZLVMje0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 151K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 08:43:31</div>
<hr>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7CjlSYwTdkwTxOJR4OYQO3tYfU6Zz-eHjrKVbokmsgrvmWcoVNbsUDN-LLWV08NCiAEXDOncszhB6bhcs2FpOBMUNud87f2wW3NHk6AjPNeAsPj5XhMxAI-3zXJ_MDjE8bupXO7tYh5_JB8tH0rwLdCgVqWkSar_SR2jGPCtBX-Bg-hR8EJ_lHbcK8V07Wpz9a3a1K83ENjIzt-9b1fxzTb1bnUFjf6D9jWjKyepPnsW5dJtXVmlOtueJFuPfGpQP02IYJwKca48FT-1zVOemOm3IjCEgxltyJByAHnF0lvYx-jcfKS8yP24V0pRthPm10_D9LRk6jxxfkywUPjTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=W8TK39E-zbdApsg9JznX8AdJTkg8xwdAi_p4G3At1O7oqyvoy4mKd-Hr-Wi8tGsloGnExwHHd_b91lI-CBNsg3VSfOgcuck2DYWdp0N-buq2GFTBawb9l99HaUnl411Yye-wtCjBQ3J7xI5N0S0GFE8SNqroW52W7lJ5Yt7mYy7JHn1utK-shTKQHn6TItsf9R5Vl1a8GbkwISzQFxV2u_FUOGB8e4iYFWCUTWEzY1HLj-2KwP6m5wcHyTT_xt8OcZvRN4ufmm5dyb45sxvYK5-a2FjeqkVLEa8FF0BLpF367oNRSUPHFg0m_RuRH6HAHZ6V_vA-68uFNyYa43C1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=W8TK39E-zbdApsg9JznX8AdJTkg8xwdAi_p4G3At1O7oqyvoy4mKd-Hr-Wi8tGsloGnExwHHd_b91lI-CBNsg3VSfOgcuck2DYWdp0N-buq2GFTBawb9l99HaUnl411Yye-wtCjBQ3J7xI5N0S0GFE8SNqroW52W7lJ5Yt7mYy7JHn1utK-shTKQHn6TItsf9R5Vl1a8GbkwISzQFxV2u_FUOGB8e4iYFWCUTWEzY1HLj-2KwP6m5wcHyTT_xt8OcZvRN4ufmm5dyb45sxvYK5-a2FjeqkVLEa8FF0BLpF367oNRSUPHFg0m_RuRH6HAHZ6V_vA-68uFNyYa43C1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=A1-z9982EshWRxdeUSjduzRThd4KWa-FK7jyNpA547HCkLQsZLOk_ykmQXr1Ak4vjt0BOnlbs0HM5P4NLglV9iaogPA47HOQiALsetTFoY_3Tdu_WLD6TUuPLCuB5R5W6WBeF0xCciuUTpSaTDHu1is-6EBOgHm9rplPOvuZGdFNVilHyWHQslL7EiJUJ1PtEdHreJmZbffYkzK2ZL4XB68dNtjm2MkLDOZqhCdJ-fUu-Vl3RCXAHw_PgSCkZmK8IGx5zoq-ainOA7NRCLUC-xjKF1ie79XHXQ9d372uakKp4S9Qs6zzTlQaS5iDJ2VvEJpx-1K1abSyCT0KTKYK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=A1-z9982EshWRxdeUSjduzRThd4KWa-FK7jyNpA547HCkLQsZLOk_ykmQXr1Ak4vjt0BOnlbs0HM5P4NLglV9iaogPA47HOQiALsetTFoY_3Tdu_WLD6TUuPLCuB5R5W6WBeF0xCciuUTpSaTDHu1is-6EBOgHm9rplPOvuZGdFNVilHyWHQslL7EiJUJ1PtEdHreJmZbffYkzK2ZL4XB68dNtjm2MkLDOZqhCdJ-fUu-Vl3RCXAHw_PgSCkZmK8IGx5zoq-ainOA7NRCLUC-xjKF1ie79XHXQ9d372uakKp4S9Qs6zzTlQaS5iDJ2VvEJpx-1K1abSyCT0KTKYK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFKj8yn8H362oVB1V9haClQU8BpbLbRpoEon8R-XjTop2mRFc8bwKBFNSBEnI_2noGJ3EPfLwoKalJo_3FCXRbHcTLzuaqfNNsnfxVyw_3DAPS-nPhCQhm96R7A2PKdez5710xRO3-UHTLsPasjYsAFldb4TSxrYX9iilRMNJ2qUGPkHHBYgG-Vn6FWN2SyApUpGf4tt4XQQtBhmNZkl_LTRmPpjM8-4O8ye_aqx71i13-IFYVlVzZtMYAcMWgUJXyiJlpUreoB5UAhaHV0E-OigIrtgwTMgkQLb1iY4KyUuFOXRUoLYO0RlQ8QIexpjO2DdMEPB5QTtK6m_jPSrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=CASOcfFdMRawN57ydItsFCmC93SbNSGD8J113MRLZ1jK2EZh7bgdl3YGr6JAGGEx19eXMzuYcUbxNf651IHY5yQVZhwsLrZUfefMESvNScx9_tChLOkFcpwSjdOAvHQjQVobKbV0jPo05V63GcX2c099Hmgm-GUgDB6oiwK-lNLBEYWZjXXLY9VZJrfFx-ytqhVWnPF16eCkuBGBr2oyYnimivD4N5oZgeYra2jjGBP-WmyyUEqrx9dkRqDkJ96N1qAkjz6WQ34NMVMVh-OLmZ0hoUNuzSi2sLhUY2ObG-vpd8L-s4Q9BMiemCzB_AaydaXQGDYQSmft8uwnV2gUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=CASOcfFdMRawN57ydItsFCmC93SbNSGD8J113MRLZ1jK2EZh7bgdl3YGr6JAGGEx19eXMzuYcUbxNf651IHY5yQVZhwsLrZUfefMESvNScx9_tChLOkFcpwSjdOAvHQjQVobKbV0jPo05V63GcX2c099Hmgm-GUgDB6oiwK-lNLBEYWZjXXLY9VZJrfFx-ytqhVWnPF16eCkuBGBr2oyYnimivD4N5oZgeYra2jjGBP-WmyyUEqrx9dkRqDkJ96N1qAkjz6WQ34NMVMVh-OLmZ0hoUNuzSi2sLhUY2ObG-vpd8L-s4Q9BMiemCzB_AaydaXQGDYQSmft8uwnV2gUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh2GXRKdHKzk2kMzkUSTXxVqrlcIwWpOTubrVyOOIPCs_YY7NUtlYY2uY2TYn2pIomRhCVJFIGahjedNF4S1yohamn3uqd6YJBDzTdwUmeV8SSjT5jJBsr2SrsESYutfClthXMC8W0uoloVdOQzwKD9Ezf11pYNhY-df3U3xrtho6VY4xxU9BqfWA6Mi_xAac_kYh5Y60wZwrNtpIwi6YA4l0kDDqBXvCjP_ipYP79C_BNC29_AXNjMhUe_L51GTQz925BNPivpISCfrRJcUs_ZoReEu3S-K4RramWurydpkxj_o96Rmpltjf2PkB-vY9xnLvxlwH4XIFqNFgcyxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=F1MhD0yuU-dMGR4yEPNiRhnwpa_AZgyFy6v5_lDWtNprZaz1fp4JtS6a1dVPjax31OuKT-Za66oHjeGTa6Xl3ZfWEQqmCTwYWKi935WibWfI6kLcoy-uePotoSjTRJ-1evBVOzmZLlH85-jSpvBNVHk4J2s59EcPFzswq9gGN1j4TXFhKYjXxku8-EWbGHDgR0gqlJ9s79PYAIdkP906-TGoYZmE_4g-HYqgk0Ln8hqAwFbDfXSA7kD4TFiJS5weIOY-71MfDXqnkFTKw5RFs1jqL-8d9aBMkwDV0B9PXsQn19fgfTPQdxbHLihuPPGNbYOP_AadJoVel31Incczow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=F1MhD0yuU-dMGR4yEPNiRhnwpa_AZgyFy6v5_lDWtNprZaz1fp4JtS6a1dVPjax31OuKT-Za66oHjeGTa6Xl3ZfWEQqmCTwYWKi935WibWfI6kLcoy-uePotoSjTRJ-1evBVOzmZLlH85-jSpvBNVHk4J2s59EcPFzswq9gGN1j4TXFhKYjXxku8-EWbGHDgR0gqlJ9s79PYAIdkP906-TGoYZmE_4g-HYqgk0Ln8hqAwFbDfXSA7kD4TFiJS5weIOY-71MfDXqnkFTKw5RFs1jqL-8d9aBMkwDV0B9PXsQn19fgfTPQdxbHLihuPPGNbYOP_AadJoVel31Incczow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=IZRbD0Cs_FmqTD_ZNQrAwAjymkrYuvgKhWBACAlULVhSQaSodcXEzXymxs1dranmR6VGch9DS65Pyxrl5DGMN9Y9Mde1rdVC0PwlCxlx1h2jWPuAq4vOaxHkWiAdmgonP741LoD1WhGPnHIJis7joF9KDgQjsjWO_kfI_P45yAC8zawz8gLY1fMMKMk1d0RTjpdIHd1tggVRbTuuL4DsYkzpFqojZRasYPqolhrsB0LI1KiBI2w2NE6u4J3F6iyRh3_KC2QOCUO37U2nvosczaU5s3nHuBSTMsLpRgJBMRkSRKixp8rVc-GE1nGnUeXVoGVgP3D7Vkd3IN6urz269A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=IZRbD0Cs_FmqTD_ZNQrAwAjymkrYuvgKhWBACAlULVhSQaSodcXEzXymxs1dranmR6VGch9DS65Pyxrl5DGMN9Y9Mde1rdVC0PwlCxlx1h2jWPuAq4vOaxHkWiAdmgonP741LoD1WhGPnHIJis7joF9KDgQjsjWO_kfI_P45yAC8zawz8gLY1fMMKMk1d0RTjpdIHd1tggVRbTuuL4DsYkzpFqojZRasYPqolhrsB0LI1KiBI2w2NE6u4J3F6iyRh3_KC2QOCUO37U2nvosczaU5s3nHuBSTMsLpRgJBMRkSRKixp8rVc-GE1nGnUeXVoGVgP3D7Vkd3IN6urz269A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0BNn0CFMF0j0wP3E1gRJOLM6Q-oQRN4nVPGg7JNiurRGaiLb73S4wXLjqOQwBKhNYPwqfHCz75XLqjnQtlknoumy7YZDwVjmoHTSLn6cgrUnOAkRkdV31TYseyTmoqKVOX8EMvOjtOGSa3N71_R_G4kUm_vmgsKylzXlrmc_ouCkuIKm9qLXseNzI0CuiO9kuIgtBiCuPvIkYMbm4L5FJx6D5EA42MTmjaXfoYg0cnkNK8_O8uBaZHQ23mkI4mjp8xkd2rgN4MXXrlHVPNsr3WVlpmNSHjzSn4E6KAfpl3hfku9SgifzKe7-tbpBrge9iDy6unE6gC86xiMg6tSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgX5GBzfsmALsKT1OvtBRGQ9SeP4-JnD6_biFYFZpKV-OP8vhZIlcVsxC8WQAcQutghCoMDX6C0tcDHOxeyOj-eOmzgS7eFCD5IXGd2714cJfAvqRNyX49iTm5fvMF1nM5fs8_La4nu0-6_wawhzI4o-D6uLZmkkG6i-aWy8pDV7czhPm-Z9o0dQsLjTxRTg_PjxRxscbW2Od_RNft1mREm0hX9FxS7W_ghpt0kbURaleViH7HMrhNil3ldCmlulruxDDqexd1YFHcc_49ZBOpKUDCY2p5FRYkPqQ_T9OMSBJrpmVcArc0y_8WbEJMgN230qaHJ4ZgF-EpQdiigS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9qbkJ41vI9Lxca8GUDi6Ot3MdZ9e7z4yw-sU5rR9tmMDpSNt2MPQGU276-mL5Jws0YXngle3HKr8HCgTlCln5QUy1pbbZYbP_9Oh6Myknor_o5rTu4EEqPyHxhA35MTzoHQXvD0fCGOGSWdZUmM9rV7vsdOT_mHZ4bqIXm8XnZtYYbP-esngrTFJWLTaCcGjQ0lEbkpbiwaZHBcGRQQZA2dN-3IyUa4jikzT12Ctyy-KAl7CAKl6WUCPxw07g6ed8ub3q4Nu450BFS9Q2_q80AsPsS5hIS057gT1YoUiGTUdddHwPpfy4z3s4-VnWU_RVLkd9AYqJ0GbYkgMim61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=jRM7KtjYlpxkqAt_Ur3ydlQPS9iPHG36jOlHbc11caG-Ex3woFwNYyi88vxK88oqthDuzLOGMshruz1uLy8kSRcS7VSLvHGaQH5ObSDx9zsoF4o2pKjilzgN2qikRrVTgExwEwfIUK0_9wuAJP7qDUqVdzhVc0zqZzuzOQ4_7WYmU2XwW22BgcbwIvQwerI0_CYW5SiueWJO6Zftpu7CBg1YkxD1A0avT30uVKTXqLuuFDrrzkj96IkOKhrwqKJw4bpz1vJa_Uf-rG5i6aisSxKyYI_LqGIlCRgsWcPC5pke84bbaijscuKxJ1g61gkX0QMGJBrcjnGdjquhwqT48A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=jRM7KtjYlpxkqAt_Ur3ydlQPS9iPHG36jOlHbc11caG-Ex3woFwNYyi88vxK88oqthDuzLOGMshruz1uLy8kSRcS7VSLvHGaQH5ObSDx9zsoF4o2pKjilzgN2qikRrVTgExwEwfIUK0_9wuAJP7qDUqVdzhVc0zqZzuzOQ4_7WYmU2XwW22BgcbwIvQwerI0_CYW5SiueWJO6Zftpu7CBg1YkxD1A0avT30uVKTXqLuuFDrrzkj96IkOKhrwqKJw4bpz1vJa_Uf-rG5i6aisSxKyYI_LqGIlCRgsWcPC5pke84bbaijscuKxJ1g61gkX0QMGJBrcjnGdjquhwqT48A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZLzcJbyylgGGwmMSztt3AUs_l_gjMCORB9BgSwr7ut-jhGXGL35u0Lsk20GW_gutDBPkxTh5VRROTTXrA-kcFCDeBjT01GwXBzBQpfmi_dAlx9aX5hHbuBx5z2scPcQH-1HQafcdiKBi3tpzBkVfr_ZJDuuxmbH46VHGuEjKbZaxRl9WzAaZCBgLThNWmF5WFtlop-aI1rnCkDFYBs1AWOfdT4gbItp9sFnkp2waNKnpBZSRIZxa9RLlgmRgxK4Eky054dx0R3u9cmbqs1XSGws8MJpHXBDUzOlTza6POxbSlcnYehMaiRA760BSE_M5TqQaYg6l0Cg8Rfz_lJ0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVk9v3nWDUCHwCZhnmHJRjok-wo0pI7KfRQlVDrNZF8vG_IMh4GT8PtB5Hd136oTFkzq_K5MUgVVYjfQ9yXgMvVhcl21wCIH5hRAnYAyVoTUqUbYGXkmKaeJAc6u4KZN3BnBJWNfb6UHkl2J7OBtVprztMsKfac_VlZXxotZJrOnNe-qppwb2269hu1WcyonMcwW9gEb5GG3PmNRaXsTPDCe7DqHpEwFsSrYAA_KYmTGQ7INsOlcDsoTYXb4Dl0DK--QpLgveXVJjyRrTNJ7Rmeeohi02lU17sp1LYNsZlPnplxtsGrUUMLqthOfU613Zmbj33zAbSk5GZ_ul8Cosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpJwAQW-ST4HgUaXdHOj71kQZJiAwjK4OeFXtJpUwQLKO_wFdZD8-JeKsRy_1Oat-QHa8VejDym-K5lRl_yzYMAn8ZYKHWbENdM7zUpU7c26BkJ9BFErt_QFq1oTWceYIUgPA-ocEljK0ZdojDPFSujVVbLQ7IqRFBKVWjTtqtzZM8xSY2rwWEzrQXqrIuZ3S63g5XKtewVsQ09T0_pKbIPa2PCcbcNHc4kgl4PNn70GazkcjdYsesOqaTG83LZxQ7nHJeNOVIMa5h_gnZgTgdQUxDANEqpkn0JkBDIOV_8BTWXDm-SeWR2x5LzT0KbJxQ11B_-jMP87AoCHuCe0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCU1Ypy9gfBDKNr9WwRr0-zmwMzou74ReYwelKDfQwZsjlSPtmPjfKq5M45hAkhyE0I9qj04t9YqnDh5uTKBVlsC3KxvOEoUQdFDoqFIF9wwZXZWbEwPGi4a-3mghhOmF4aqWXSrYXBY9yv9_KR46Cdfkclfso98icy9dVveS0ageTe3qw9jsajkW__oinfBFtPp02dsTbkcdlWl1BgF1cfw4rYk45kIzdBlvwknHEk5iK7d6Hh0GnyibmHmhqOTv-yi3uQdIQhQ_vAAD4yutJEtrMXLi_UKIQpqftyBvrulpLdhFdjEGXepbjMmw579X81H9NNzrmna7DimikQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm1mkbXlezvb3qanrzrRjuunFTRNqaQEKZdPYgBKi5RmghzuZmTdjOoM2dlybFhQT3mGzUS_LrGTXQsVl9dDO2e7_KUf3mRnkXEfwIrt9EayNtT1vi0l6lem6OvaXTUCiNMgjppYHMOmnxMCeXMcgB47xu2YiiMxeqFniNP1pUENuGT9QsoWz6heVTETFWIMngs6I3YVRxIk37u4lczq9k2S3S4d5-idHtWTRKICb0o0P1b2HY1x5EwaTSU9KfemQCldq4AWm3QIh2obOYZCVY0r-PUIUs81GqZyJb0YYl4MO5U0EY3PibikAf3HyuLKL2eeNDGSdZlIuxP8cep5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daq1dSGz3ANH-opN0OvS9CbOrjEBCeEmzZwzy6HxH7NiKolcZq9O67EgQzN1xUFw1oNGcVYAAzJR4wFlCdOfmvLfavwKhmx__engJcfZ3eAS0Ch2F7UHyrsyHhOx5dP_ZeGQT9eVkMUlTUvCEvy98hQXDSUOJHY36HuF7-bE4crZSBGoPyTC4z9zXDoiMBGMtgbMFosZq3uesfkbHnnImS32G4EXx60Bo-byR37ANBNALDxBD6WKS25sJunIQYsvZtju3Haa0HkTqjI1htG2lHBZOaGds-fCic4w5OpV_GjevueoznLHQWwpdzEuLMPxh2BUFlu9sMiDlaJxwD4diA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-wod_yn2TUWefU0SW6XCZpZi0pJJ1mXsGrkhuOceKyy5eSdKk19olUJo4nT_DySafrkzsOE4JSz5XKoWuCBhz2YqsUsNoPmj6v-u4fyBO_ADuxSyKMXdaHPIX1NC0uRQTBLB56yEWHXx89iSZ8bibOsktbv3Bz_yaYu86tZ04Izh13nbFUQD6SlFaUgyY2V21ZNck_V8J-Ev6Y6KI-xgHZWCVe0vGaJPwTpyDKQzPuSAEX3PlaI4hzeEMQVO4_6H8GXzfkqClxvSccWKsXpf5TbON0F4jA5323EDY_m3WVW98ZkcO3_cLKf3tmSEQYWfF2Wh6Efav8n2ml-4dPwBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo9tUDli3xlKFsCcgmp1-wg808Iv_U31BD2ejMOsMzFVuAydqFwiYT-bjPCPuS1DNkE6SvA7YbzN6w7l3dbwpOovzP7nY8H07ADFGTGmHkjtR8cmY_KFp7kCYWZ2vdIWt8kpqKbmKYl-v1j4ysPQLT8WWnuyGJIUtJrTEL48e4N9ud7YeqvXhCfbfCV9VMwsaHsyGncPt96thpGhCJTXcqNVSx5Fq42decRPZbe818J5oTS--epJO95zpWpE7YhftKz_7IMbCXVpnqqJqwYU6UFTjZx9-UIfHZKB6R6q1vxVudu70EgDP30AkstoFW-6kyLD4fzj9WZsEglW7xaJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU7gRQDZanNJWhjAIHi-3t-PwWGYsWlly_gSiJC9Kn4OpPUnXHDJnLZApXVRZ9_U7SlynaGfIzB_yqfLBOJpL9A7XEzQp9l_hA6FNrGxCjVF-UaiaKHJ6L7LituBqWeugICfXdKGkvUPXdahbFwnwYSa4KLJEoZGwNmUjHevfMJ1NcZYznFttmK4BYsNkeIEVO7QwZfr02ghCOBjAgGCtrz-7YGtn5hGObIMfcHPzDSlfEWY7YGbNNXjgS7W43eWsu9D5I1MdlHtPPBc-tDk1KOiuVNuwxTGG13NA2srUmcc8F-MyEqMRG_9zKNEg4TDb5IJB-ef5vDCUTwqMfGL2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFX1HiRPqIqyEcC5nMgVyFsazEflLUFMIrv0I3t1lRRo0rZNosTSB9VpX7VzPPEbxBgPoqEh4JfMxAQbWxyi3fYbpHCBa4Rc7tAtVB-hdrjsrLZzbSyfP765V23kXBFSHCV9FuRTqKhMVPEbIwEY004eUfyWyoRT3iyjVv1fOQaEirH6b1L5QBZf1KRh5-KCYzUxalYrvMb5R_oymWrCUfQaFkEeVoAxPnh4uTauyZAJu_Qv8_7rR6V2JbhBmFmRYSTQ0bKbXbrCqEXaR78SdfXgFK8RTVh9U2ZCuaC2OpqkdkAZVz7RkKYI3Gtycq2_V6OYiOlXFDYzyTmjyIK9uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CTFV0nbe-7gZT_aax5t6DhIgWb9GX--Gdsx_XqcifuGltUGbPL7UFM9pb9Fc9Df8My65dQQPUvl-BszYFmvYstiniRuOWpN0gZw89EZoRcnn8CGBhiSIC9vnZvv1VvK0-1RBR2zMUqATJ_280s_sFlXRaHKK3EFSsh1TpY8dgt_PQGFyxH_9ETk0BTxO9RuOVWiIRoKKrOP50TlVOHV489g_pzzUIX0SzVt2eqas31CcJo6sHYX4cex5q9kUOaREK5b5pJQnC72kbkbxZOGsog9dmz4rA3ETONeEltaU057b8tz2Gh0QU00H5CqSTey0vlYcY-D0_88EYDUTaWnZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQ0mVdacPstSJl5xyjsAdRDEOGKZLiMkPy8uotTKSOLo3NWWNfINfXITAQnGLAAIUYMK1RqJEA4UtVp6yJ9YT6Fte9NxmiyvKiKh7jbWErmTxcM-UVntmHluqGuPXotRhhi9_Z9jseckevs22Hq7jGwh20Tu4BaGOTD8k-xkW2k_cxX-8KlA3b3IoX72iNGRsLOrF0ZeXVhs-5bFmTwTtg_vfpxev1Oq87hSMJlb-GtNT45iyq9ME1yl0_1y2xpcohUMGZBXrF3ritGnyI4poICouVv3AyqhdEvX1G1WNP5cjs0qb8qpuTvHSizLAVTapTKsYel_KPmwi-NRNaOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVtjBMXWzaFwdcEWY5KBefGCOqG8WP0wyoIp0IrXfmTlWlOfAjFDTA2I4J7xpQvgDf5zAMgy98czKU3-mELtkzfSDlvUHFQ7wzAZh2LWwWDEdTZP_dS-zpxnfVgMRrdH0jHkRwX6bfsZzF3c60_08r37B9pTZ_1dSb2_rIvZ6a6SQxGBaX7GoH320mxDL1vjwMNoiX7DUQKoBcikfyxqVpLV9mIWbT2U1qK4omnVjnbvRg71V8gdCTJmbjRC44LDwxLxVLC-7o59KGKgCUwSZlpkONXATxJbIkD9WdBBDbss0Hzx9FlKDKxwws97wZCPksP1NFYb4eDTPlPPmW3xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE6XXiYOJfOUtEcSAnOmAFpkqpH8vWljK7wKoedFK_z7nfspMPFwk7d3hbP1oM5CCZALU-_It733vbxeTnUBNOGkBbofEYCDFjcIO8ZcRSOaVM0qY0LLLdd53Srg8CoYagqOo9b7c9jvXSx7xTZ7Nlr-Po3ZRekxiiurgwEIYhDVhf3AK_Ss5FSC7DrsBBQYRiFFhKqaRqItobCHFOM3F7WSo5QgHUMvM8fvJDnVC2iebZa3mHwwr05pRWxwGMOtrrVzBTW3KR3gUV_Augxay9ahDZsK3htEtifliR5pbdFPb5r1ogESG6rHZA-z8ypO9pgTXV8u4vkHaPbHgbp05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0y8WHBInihz3rnEV8GgfwAB6x63gLKtHEr7Ma_d-kj7k6Qc7JGbsvdK2xg05TznN6EgYRZhngTNWsOybuEird5hOzB4dr67DeO3FxEvJKY8InbS2qz-qxvI4kXe3mM5A1ObUlk3r6T2EqDbeafP8mfyH1jhIiRVMh624b0Oc2QB9CdyAXOtw2VD7KOCZI_KYUphl9H9PMQVdgN9eO9j_VvzjiKOGIQA3q8IXe2d9fBoJJlvRznfs2MrJ-BqcHkeBQ1a5rVNUDrgDsC8KOmICHdNz3MgbrA_SKQyKL75d9KWZrFWNUr2YJP9Ilhwg92-EUZg56FUSlDbDsBaeBXi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sggAWV0rolxcArOKGUDjepJP1VTioQYorVApPLMKIm4XNSkAAgBZcHPyab1nrxU-BuGS6xxWT4-A0sN9VFuQuCJNoKWFmtVDNFqC4lOhlOSXMeviaed-ZnAOltmY_49-snZlPnOjbwvuC94fvzaB2gAdzwPjqtzaE6QwP0xizSIlxt9cDti3NZmseKAqB792_uswZZ4C2UqkcpuzI6PFwhHFyv4LTN7YL33WNYwlTHdePBOLHSQxf13R9AVviT39yTZejTizUfQWfCt_ZYAti2D8-2cfc3YFl_QEHI1YPAxXrH3IKIAK7MwpUlAZa4IUxurpOWLm60uwt9XBmj8cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=aoFJkIEJuQoeL4tgA85fhVNc1J-ROqDxe0dYeRAqFQ5fYUOkAdG5cx3iXuNT3pr9r8-OJBjf9x8pFzBhqxX0ISFwZwIxTJOno9ybHkT9MCJTMx6BEV4-ncT9aR8p5G46Jj1YJ-NK3FEQ-LZ1QBUTbaeJurmjX_ejXtVBZq3IoI_eVl8NyegKx6YzueASqctjz7_Oy5gZdT7TvV_6-RB01LLvY_HVztakGudQSTDUBMu5kRiAOqKr9bHzv376gmCq7wqbmTQQS4uOiZkPvmet6GRf-Tt2p9aYKmgAWeoBbOkfTuJSTDlA0Npc0I-Rgaqs9Dm390dptSkZjDC-wJSfdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=aoFJkIEJuQoeL4tgA85fhVNc1J-ROqDxe0dYeRAqFQ5fYUOkAdG5cx3iXuNT3pr9r8-OJBjf9x8pFzBhqxX0ISFwZwIxTJOno9ybHkT9MCJTMx6BEV4-ncT9aR8p5G46Jj1YJ-NK3FEQ-LZ1QBUTbaeJurmjX_ejXtVBZq3IoI_eVl8NyegKx6YzueASqctjz7_Oy5gZdT7TvV_6-RB01LLvY_HVztakGudQSTDUBMu5kRiAOqKr9bHzv376gmCq7wqbmTQQS4uOiZkPvmet6GRf-Tt2p9aYKmgAWeoBbOkfTuJSTDlA0Npc0I-Rgaqs9Dm390dptSkZjDC-wJSfdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBQQ7CAhMk5ctWMJrlJ2oKXJVNGVxEtlLHmWHvxJ_Q0OBRn2i0aZn0ISQgkfTfz8P-aamuwlTPTMA5XTPOp1UkH7J0oDuF5Swt1msbqaTdZ_CmbqqIVg9ZUyYS4XPg3zYQ0po3MAD80SPnCT1lyx1IHirFZql7kUSxQxxD8Av0noYYAZfUhuCvCu7iwRSdl4TpAb-Ki_wALzBg-21HQmOSusKdvsg2_du6zk03MVUhscK-3k_JTzRr9nnb2Et1CiLJ-AdQmh9cbiyMfIWsq0OXuJ-FlfahhIEpnBGz3TP4mO1Hydrrs_wFr68uoa1yWaig9-ZOj1-ZHkBk94tgNm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=UG0jFL6IvXu7UT-BmCNLMMl-0eRSTWUWkemPhDkwe1WZyiQjwTP3ZfL9tb-O4ZInpqQst-npyWVhOwBVK1CQaEzaKfJQ8bASSDZAekqpzR2M-7ZJIHfRYY5YMs_spzkXBddDeeTzUoR-kJbsanNfMbf5xYwT9CWimfmQQx_wWvhKwBjgTKU7pRtnaUAp_OXEesqNywHlxMQIQ6LJT5XCbQb8r9ADnDm1gOTpDztOty5uPnFGRKCfJ-_XTYOVy-fT8S_MpXAYRxIuGfMly6a2yV_OZ5EANjtqhBv-VR66dZezFyQWo200JqLY5Gh9pJQXkV9VVq_Oh-8nc2Q-qVhvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=UG0jFL6IvXu7UT-BmCNLMMl-0eRSTWUWkemPhDkwe1WZyiQjwTP3ZfL9tb-O4ZInpqQst-npyWVhOwBVK1CQaEzaKfJQ8bASSDZAekqpzR2M-7ZJIHfRYY5YMs_spzkXBddDeeTzUoR-kJbsanNfMbf5xYwT9CWimfmQQx_wWvhKwBjgTKU7pRtnaUAp_OXEesqNywHlxMQIQ6LJT5XCbQb8r9ADnDm1gOTpDztOty5uPnFGRKCfJ-_XTYOVy-fT8S_MpXAYRxIuGfMly6a2yV_OZ5EANjtqhBv-VR66dZezFyQWo200JqLY5Gh9pJQXkV9VVq_Oh-8nc2Q-qVhvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDhzA5dmv__muNcI325kA7zIZF68Vq3tgvjAhCH0Bgkg4NHo2aVCKaL599liaHCcbThT_L5YyX03Gj0N9Ge5wkA5uEhyOCBH0xKlYiHIuijj5CnmTZxX7xobWQiKw0xy_eP7REGgOHfn7GCtqS9NDq4Aycefu1VwAMXbQZs7oRapQ_kKvTv33UTA8ipNJci7uvfI3kRJ_wkOXUQz2zIXufLgwrznTufrmJdS7gi0kY0E7G8mjytjFVc32YOmNeTHvIYU954fFcpEsOa1XCtdi8yOCB6TcywTMLnZFYdgg6zQ7QlpXZapqU4jx4HiAnsba4WY1ZNkkca-iuPdtI1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQWnOe03zRFkSYw_aSDkjtBnPICJXNLyvtbA2uDuRr-ttULgUV9cXnaBN2VMEGhAD_D0pWMBbB52DIirtArrawjp1d5Yeif7Mq7bn8OW6H4qajIfKHCKccJ4esEJd724zrlA3amGBF-oxdX96shZ6ZcZowCwSogoYCSzRFRwkNknyxhaLGM_KzZWCDdL6jDVtGFZTa-zx8LAOiRUpVpAS7NDjuUrxc62Uv_2Ej-qA1KMmMIexs6C1dVsefSwB4XNNE7pXXuTn7gOqs4dUCnWwxymnqX8SGAy9_vTvvAydLiBQ9C1N6wD3foHpnbZ-Q2tTs6XsrenGohmvuCDUpPxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ4B6Qj6TM092_3l93vnanC8WTyQrCtB4QSoOSHeE3derggncMh_Gxjjmi9w14qPW9SAsIcVzoYg9INobb3hW8Wrnm2iAM2xvn-uLkqGasIbkTlBW_diTA1EDSQtfVeFQbL-d3yG1LpLjAD4-mNiSHj46ddHh7Y21mPnw0AlN-U5E06FzBZnL33p2xcT-LICLVtQ-vIBx87qVU1Zbs2OY7wZsASG3xNR5ZByEBA2LOynHIcp_Jo08aiUqqEJt4Atk_E34XdeD2oyiobqZuMJg3-W0qHUEoLkeo8eHhmWIbF2G3w9cmndgp03d_Fl2m6ApOZ3VhsLMYo2KmtDQ7T8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
