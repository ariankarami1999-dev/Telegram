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
<img src="https://cdn4.telesco.pe/file/I7prIQhZP5BTnu9NtgpCwpYH1GDZ4g8EfQJIH5pYyc2oW0O6oT748SCbD4kdRIaEjGI4rtZJi0tTIqDS_Kce074OXnNSaNLTC8yVu6jyNlk0nsYT2VZonRmsiPEe99rJXGfNQvfpGXGM5B-oqUh-tbjtDsQe_kZ20Z-FVle6UiueyE6kWcNq1Yb_wVLxcRLhejESMxWjnU4JRkaVytn3wreRtxTr5m1KZCi47WnVjrLVAHp5n5t9Ks86KkcvOD0Ja6b8yOTOmvMI4KyianF59Dn2LNEoqkMc6JriFUz9l9WAJixufDoqiZoVVBTFzod9bWy99zosvzWjbpBhgsUO5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se0Jp_BZ9FmpzRP2-D4YiES-Xm4zizUQtZpIMVfByk8J3pj1Cd6RtE8acfl0UKE0C_9uA3XzARGEWmYBWpqESsdE5j_u-z3o_XcorfNoXSj-DZKFBpOK2pAVguVcy9Ayeye1L6Q1xzq5v9uNudyxsy8dR7dtjATj0ohadSyuJVnLhyQTnPmbJIUmDIHo6BpgFmaU-cBVvy9awmTgBLlx7bQPvbkOaMm3M84577d00MpZgnG4NJexJWaiJiHpxA3C996etVEiSL9RkGZJBZMxKAFYUmWHwKavArRkXdkyFu8HE3KF6zJAJgFR1vdBI59AkFKorA45cy1wzQP9i_c40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=QOB8XMC8osxsly4omY9ekJExlWj-wynlBUbKwTfaE7_PRRP8HuhMlzREWdnZB-YwTAAoH5g6TKpLI_lWNkeR3YpVV1Pgcq1_EiiivsnRpwPVcJ-e4jjJQ4T3d_IkCBuQr73NMVTS6UpDs088PXStpKMeidZxv12hlu0gVUsefjo-86r4iX-fid2t_JeweoDEO_rbVo1H3bx6YMMC-x9HNlznduf_xcQ9SNGCgWH5o-uqdZY4TU4x8NnAyvgRaHC9nGDg1Ne7yvKK05M3WKHUEHiwECJaQr6ddrunLer2eZFdcrn1ZWyTedp8zf4AH5Xq5tfz5Li-BihE0OV-qK51Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=LkHnYoyn5QgZcw_-3ovn6GCnq8Ut8Qp8MD83y92biRF4hAZrO8i4DPLsHQ_nzud2ckwrLUgLMfViW8W5w4ynyVhcYQKHXruw7iKcuLp3NXxWyUpLZiWqPpk5BWEDiwT5uIKk0WoqQNEewLRDdNssstdz1l0FmiePWJAJQNVQMhKSlp3OZ3V5LhbYDBZjW1hjVeeZ8kDB69zCqJa_43BLa-vq4jEjvZLx0UF3HVF-fYvF4OKh5v8C8vE9MgfmtGUqu2iTqihQfXpGLKI4Tco-wVRpQ2SltzIntrJ6O0C6Hj_R0THTeavas4F7RcxOh8-aOze4yA1cmTzf2D_3r-6ZXW3YOuz_NfbIPOkoQiLikWmlurUTl9W-Fv302HatI93Yj4L4kGDh-Q22Btg40KMgHCOUaaxd0qOBBXOT9dkGdOXWvGNO4tY2-JNzVW_EE-SE0cimq_JfWy-GBl60nEAX5MziYyogapnY1G5b1i29BFu7RlUqBA58VcchRZq90CJwqjwy60qC66dRO8RuhNBMvxhm5BY8-CSXisrRsL-3vcy_z1T19YZy2Gk7wuy4N2MXQt-nR7KVDhKVd-1ID7m5jhm8ekuAlTZpz3Nw7Gxlsfml0JXKSQa59776bI1itufyS9n30X-dClpCNV2tsbnGp8FEVDwjcBgbhvGMhC2cwpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=LkHnYoyn5QgZcw_-3ovn6GCnq8Ut8Qp8MD83y92biRF4hAZrO8i4DPLsHQ_nzud2ckwrLUgLMfViW8W5w4ynyVhcYQKHXruw7iKcuLp3NXxWyUpLZiWqPpk5BWEDiwT5uIKk0WoqQNEewLRDdNssstdz1l0FmiePWJAJQNVQMhKSlp3OZ3V5LhbYDBZjW1hjVeeZ8kDB69zCqJa_43BLa-vq4jEjvZLx0UF3HVF-fYvF4OKh5v8C8vE9MgfmtGUqu2iTqihQfXpGLKI4Tco-wVRpQ2SltzIntrJ6O0C6Hj_R0THTeavas4F7RcxOh8-aOze4yA1cmTzf2D_3r-6ZXW3YOuz_NfbIPOkoQiLikWmlurUTl9W-Fv302HatI93Yj4L4kGDh-Q22Btg40KMgHCOUaaxd0qOBBXOT9dkGdOXWvGNO4tY2-JNzVW_EE-SE0cimq_JfWy-GBl60nEAX5MziYyogapnY1G5b1i29BFu7RlUqBA58VcchRZq90CJwqjwy60qC66dRO8RuhNBMvxhm5BY8-CSXisrRsL-3vcy_z1T19YZy2Gk7wuy4N2MXQt-nR7KVDhKVd-1ID7m5jhm8ekuAlTZpz3Nw7Gxlsfml0JXKSQa59776bI1itufyS9n30X-dClpCNV2tsbnGp8FEVDwjcBgbhvGMhC2cwpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFz2Dw8LYdzSaDugUlzrDj4aECjNmH4c-781vh3kkMvlqMeS__75oxAVDPcPYWh0N4rBeHywxnL0ofwzESWq6FfckUOXs5w7v1Fv7HuSghz683dMcVEdkZOAdhJCug4plqNqrks-Mnp5yFAC0rs3Tgemwi85QX_4elDOZ0UMx33fmkS93dBT2K23eUvaEmZnX846bPeGDtwRFgejoSMDupFaPasSXzOwasb2Br_55d3UP8yn6EnIW-kXANqPkP0z50D7-e3keq3qJDIb7nZJjUhXXw8ZXuurhvk0NLnsOtiq1VoZymqGZrK1M0ey0NsXfZ91JVJqYDnKPt_8j8NsrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=niuQJ7MWmscDFYxohfJnLFpWUkcIiMu16rmHsRnCL10_YnmuFTGSVylWH-vk3XHIMWfMl6tNhDw4NVnFiLebDzgsEI-15uRjEZfVhnEJeECJHzmiUYukvvZ7SZ-bsvNcU-5ueKj0oy9_4ttLAuxQF2cjXjqTdZ3bHrNM2qC1dUTLnyaVnePHC5UyM3Z844ILApa221cn4OvezyvaemL7XzGzw2J_2ARjTX9341gHK8Se7lSr6PHGstsBy5JpYKExnukydKzGDPBb_70T93JiQNJnBcgjFh7GBDfAoOhOldtzfbzqgOUAW43mtl2PNdnI-RLZ1ZA-iYJJ50awHj9Eug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=niuQJ7MWmscDFYxohfJnLFpWUkcIiMu16rmHsRnCL10_YnmuFTGSVylWH-vk3XHIMWfMl6tNhDw4NVnFiLebDzgsEI-15uRjEZfVhnEJeECJHzmiUYukvvZ7SZ-bsvNcU-5ueKj0oy9_4ttLAuxQF2cjXjqTdZ3bHrNM2qC1dUTLnyaVnePHC5UyM3Z844ILApa221cn4OvezyvaemL7XzGzw2J_2ARjTX9341gHK8Se7lSr6PHGstsBy5JpYKExnukydKzGDPBb_70T93JiQNJnBcgjFh7GBDfAoOhOldtzfbzqgOUAW43mtl2PNdnI-RLZ1ZA-iYJJ50awHj9Eug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBBVBr7pehkuHfBntN6Cf3uOa9XmiEBH9gCA7McNOEPU0flqxBR88erj0B0WSuSsiH-MjMCuga8KUxjtN-pD8KO3C8vbxHn4y4a4LI2pVpOounlo-2MzoDbjO_4WttK4gCQw3kL7i4nEo1xDGQKdpHYMmHPHK5eY4I9vSIFKL355gTgFvxCTwi-RvisZUCVlB7D__LwJb9NWWHQx8ZBvxlcUwzE5ZKML-PFJrHzMNFCZeqyVrI3bJ5m4W4wPIqbLfehAxI-l2a0cfngCgyCkYKTJtsABv_FMYTBOvD-nwIWLMaT2cjGqsgRLOgVx7lBGrNLKATBJZjLGuy15RnFCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIcqPGj-aCSTfq7pLBgh5dntKN8sm0jHKlAMjoyGKsAjQhQDoze7QnSUO6TQbaq_Ynunz9EGIhyna0sKpvN9eqRG8bg6ozCzYxDnacn2Z3_WOM654o9NcIoKtkXXlwJq3JrG3lENQajQxNAZrS2s4krzvsoqVmhfjT4zXnUkrhxq6ZMFlPqWh5PwOcqWQwfK3-FN870D-tD660iLmEpa_slvkWhbnI6BA_FUaBjHFiJtZiyDbeqiy3KCLezpmoyYUogiptZIdTSd6D9933Ux_9nvVRt-0dTzi-lcrWU4mPhiTbJZnpOnB5PR3NPb8BnB5fi7T9LpYwzXA8WH6lxAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ridyQfrhsInQTZafCeiOHrLG3H2Oadj7Ql01cK84o1s8fv5ANRyFBAlQYsEaXqMk4dWbV_q--W8BSVjDyDjU3AIdutstHREW1y1pCDMK1bFuz3SrwoTVV_h8VT_D6ufDUSyznLPcj341zgVzbT3SeHfYxaSf0kqw2zZ-gH9S-8RRoobcv2u_6xdQ5POPNZOO7g72kM2m-6TKv53V1GE1o-xwO7POENdrOS8tPLZ5c5c57zjJ7v-BKMMhaWHAmnobhU7nM32FEmgNic3KgHK-9T6Lnwgd5tznGqjD42sg5zPRz1G_a50IZl1aSvF8DENU6XKdFpwtyjr7TyMN14LdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=upE0oUHVJ1IJyYCgB1OkgeolAxf-QD1g-S6hBWWRV6OBlBq6oZKqHQgALCrRPvbeck_idA-wJN5UXJM4raRUEVn7oo-plCGJTqlIe3RXd0p376Al8XHwd_QV0hB7ovnPZuBSAXv7zUCfI9eyq5WxE2MxJ1MmDqTvVgU-gN7RBJsLMtKrVIUPk-r31oiIme3UZBIOa_HumGgE2gO0OIyqgyo5pJn-crBZ6aAdTuUnHnQ1AyPaTL1DkZ3kFSacnp97IlXpCWuvI4_I_ugVFStGIVXbmHdlXiRJp7i5CjOO0KFWUchIXnglxD4FSA9Bp79tvYzpPTjeKq0m0WFKg42QQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=NKypW9aFiG_YfRgv_z_rkKSlsNd3OqcZX5I8SUBZMJZMZ7vglrnnkZMiGd1nAU0VOYdZs2AXWTbRpRmf1V3qiLNBmiJXfNvbXh0JK4I3XqA-nCbSEp0CXysrv1QR_XRGPLLe1p1-J_8y8tzSE0dIpwwRJO8vFhKJ1wS2dEQ_XBpYw43klL_eWe8hiozfjPrpuHeegYPjk2ulU1VOHQVfUZzzDWRaAlCrAg6JgzWC0VbfC-kgHf5Vyn8gz0IdRvOrJBwocxIfyajETGjwb6Nwx5n3uDz5mZC-cpcFHHXZ-xCtWvKlkIYNIfW4BelG1mg2IeGCLj6NJxOqzavDEzGC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=KfveprG7_sjfh9BSL1OCvH2Z6yYyqN8jMUjh4SweBmXz4K-D9TXZSZ4hVrxc9OhlqhilvWlgsvdQK8ErdKO68oxUOeT8UPLNVGKENRGECUGVY4U73QP6YDXmsdUYky8MMWGRXd_2_goJX9IfLj1SDeATzifZBOE5goCxiOSLoTLdLUTmU54j1ajf1r828bgW6Eao1LyqYwYYEIz_odlANQLA2PAB43tUlJYxbENQ7Sy1cuqNN-skY546FgNyvdouIjrekEIHB4ACDOcDPMkKpZxZAy3LEKM5cAt73xC-WhxGkzWD8cgbhnnut5WE1IXaCUUAdIRRFUmFwQDCN01AzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=fO5L6gncvLGwaXiMekO3KP_Cv3tqZWXs5VVOou_pUqt6ceUZmRYbXl4gHPNZS5bcfLie0tiNmrpndJNCM7LZwPqPfM7WcRdkHfT5oO-AGBwN-omuODrBiKfjaAj6puXsc3MQm9wuoNyTCSJOPWICm6OYGmfI5YHb5XDcpCbueV5lh_IMwW6cbfzMAnRZJG97MTThwsKzcJS2A5C3C4TS6dzNEayrgyhI-JnhQ9tB7m88Z5OnAKYcnO-NWy1ZtWXydV0bUZnzKwCzheTkISvjlDMtLe_f8QnHJt9_NL5VpncLVlKjeVBBN_TT6c1QCgTvoOEeec5CubrPm9K-nfkyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=SK22HcmJlcSwwEHByOB7AAih6nWPXFs6mEXpvPDgVBdLEP3cviPeKeS2mJVuhTnbDST21kph0w45zPopWJHbD0D9eJYNRQoHnaC8uUxVdxlCf443CtHg3CxCvZTf3H1R3xQhrycVIJp9lUx_4mU3kJ58dWRuQe0o30Ia9-4OsI8eHl4rvcCrDcEmXCmGsdX-7PFMTw8wsMKi0lcPFXSPDbb3oXV-jIVzMTYQEWXiGUZtnbV_Rcuj-kigwsSayOHsiTeYhgZ2BDkCVpcUVX40G5ZXISheMoM6RavpaWG1VYJkcNbrrSmCiRSmN0YX8l94ZeT4Qj7-pd2_0S958jLJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=SK22HcmJlcSwwEHByOB7AAih6nWPXFs6mEXpvPDgVBdLEP3cviPeKeS2mJVuhTnbDST21kph0w45zPopWJHbD0D9eJYNRQoHnaC8uUxVdxlCf443CtHg3CxCvZTf3H1R3xQhrycVIJp9lUx_4mU3kJ58dWRuQe0o30Ia9-4OsI8eHl4rvcCrDcEmXCmGsdX-7PFMTw8wsMKi0lcPFXSPDbb3oXV-jIVzMTYQEWXiGUZtnbV_Rcuj-kigwsSayOHsiTeYhgZ2BDkCVpcUVX40G5ZXISheMoM6RavpaWG1VYJkcNbrrSmCiRSmN0YX8l94ZeT4Qj7-pd2_0S958jLJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyThFtJs6oWSP2GuJvrZi4lI0nTUUzFun8EvFVR7GFvUl5ZcufzOosoMn9MuQDOE0eEaiqHjPC7K0ZxwSVRDCuS9K4EBu0e56q_zPr8nVH3lTlV-7S3PAmO58t4Kga-9Pil4es5aptIejrSSEBHKMDEg0TMc4DHmP5e-Bqr7Yn__s487Drqj0tkHKG_ouJa5AhbyiPqVzPMc5a9gCYHXvH7p6DIw1zHYHh_MtFSXw6HVugqHDhKQ_GnhbiqVbu8QTpJ__s1Qjiir1tlhn5A2M_N7WznLDOMBcA6So4aS6RJs4mdsjZ0NiNugYsiH4Kh8wtUVekSa4liZWC2j2nI_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVgGDOEyIWPTMU6VWJEvdv9kJTpvCgxDZZXmqwzSHbOyXo8iRZNRHCyqxn9AhPYHWoxKYr66Sx1M_LcqY8BWtRAs6NTHfRYjQkZHKnKZLfahs-DpCunnt7GykJGDYeLGqveZhuz31N2LbF6TrzKOzVPBkAj1JMm07xOrXL66xE0fwzMzw485DKNnMcDgcd5xkDkD2N3P91g0KWk_VaiDmQi2376tmaOuFtNUSoBYM-wVkEiYc0gMbqdKuPjNgG5uzeAzAvbpUxKO_MdpJem_dE2BjhBHSk0ffCpPq7nYJuXvm_DC9vLChAMEBjODLyq3QgE1U1v2Jx5lJAWVsFwb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HA26e_00GHZSeB56cqYePcK5z1Z0vGewfDoezZhjyqEM7ibRCxQzUVYZGhCN6RNXP4w_WAoekYw3nQOTX5jBAAlf45X7izRJefZH8kdsNgd1X5sW_rGN-dnSx7MAhbNlZUOpv5jrwV2zAiLkJwyRvqH9RqTv-fBH65VG68kFwDxe2jO4roSlwqr7PfOnYZJ82O7VFY3QKekUR5tux-6cypWXJS1I-E-4uoQUxh-ulGROpK96j-azZ0HeIEPWiZ0BM9WddJQUhOL1yjkRTIgb80g6oc1o8XPwHxO5oo5wIWJ2onb-Xy589uTdPJRRyJeXUDI36-HOr4rES1GGBPdT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMXjK69jv_6QlGzE3gY8WHQYjzLWXSTBY2M7jO68dWR51MfAXZq0wXGI0ubmUWQSO1LyLIopizZ-XXkGf446gXzsDr22Gh03HT1LHTXxuxb-Oq_gqOpK_HHexGy_SHVCIzqi1g5fsWxQQBUfvftnYRsGiHKAmhzm0yCpgSqb9O5jAS8j4_H0zbtXWpOJqHDakqejm9-HUgA5bBoKF6yC6H8OhxLXcBrfRmEOCONCdjrDcs3aszlf-VV66XDwM4wrt3lCCbSQvbBxleef7uSlWkrGXENMQVcLzilGvIcrlAz1X9h8wHlZ6OSsxpYmvb-q3K9yG7EK6uITqVoE2iomyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=Q24n-pTxQ39qWwUvIHiZWgyQjfgkdt5JW0VqJFtFDkBuFpZ2XsIEMkOXCA-ssEm3G4IkDB5ajK1rOVho_-wSQ3i7hgUXXKbSUUdqO5B6W6DAJctG4BlxcaoUgKLxek5Sl3qu0RqKc2d3cGmC8ybeon8V32atGsPcDSUD3-6ECt99U0kVzvPE8524J8q2rIRwVTYpzFbtg1cmvJm1FHcHHoXpxSRKUvLqjqqLUHvef865FiaNz6OTJn9mooDuncWKO0r5ae5czqfthaCZIk_mURpyfx4x4uffrcz47OkVS65k9BjNtGD_7C36zdsbznKcYCNavkIbt5-jewYnsgpCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=Q24n-pTxQ39qWwUvIHiZWgyQjfgkdt5JW0VqJFtFDkBuFpZ2XsIEMkOXCA-ssEm3G4IkDB5ajK1rOVho_-wSQ3i7hgUXXKbSUUdqO5B6W6DAJctG4BlxcaoUgKLxek5Sl3qu0RqKc2d3cGmC8ybeon8V32atGsPcDSUD3-6ECt99U0kVzvPE8524J8q2rIRwVTYpzFbtg1cmvJm1FHcHHoXpxSRKUvLqjqqLUHvef865FiaNz6OTJn9mooDuncWKO0r5ae5czqfthaCZIk_mURpyfx4x4uffrcz47OkVS65k9BjNtGD_7C36zdsbznKcYCNavkIbt5-jewYnsgpCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZr7BW2VKIck1gbmqMFHVzYSxdf6Xqd1rmCn_nGLcuF6YbQxrk_DxCbQ7y6oEh1Y8XAhxzKcnSwqZG-Jimz55XOKep-Hkb01ZyykIIqB6DFoJgMJyosB7N7tm4fC2TvzNI1h_tKNZH9epj9eq2MtdQzqESQ_f98pfRC0MoZyAZie_-oTrU0fUiW1ocOAJhAIasauxq0w1sR7CMEpkn2BZ6gZSbQEoeAR-6oeuXetvevcznyewyWoNcFGLNV7gH26GxhyfbLNgIyrLKS8Nzlh3atxbN_VI5eQmYQB5Hvx5FVm8uu1i88hidfFN9ZhdHjVM4zzjHvib1SsHhmcUC8uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=sOv47CbjaAClL4ytZjlJwcfuRtYJOZ9_BK-KgPWkx2Xu1dD9tHkDltvDqhyYZCnPnsL-ae8qEHA3j5KcnBCfTlgS1rIrGHZG9SsJlMeFCb62PcR-1qQPFk_y4hGLBmhiF9i92zit1ZZCx3q0GkweZEDUwCDvaMNbZ9W8Gmu79aGUzcgAsB_-eFP4eBn4HWNsNaYGx9OsuQhCS1DmUe3yCaQbDWXXhMXtlNd8v4J3VJfxOT8m9EDpGrGs1p7vqA29iMnrVhTGcSPT7URYAx2yllvfRg_dxuIgUh1_jylO5DaEvETiS_uQyKsPrzM4Azvwg55wcfgbL40wv7D6MhijPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=sOv47CbjaAClL4ytZjlJwcfuRtYJOZ9_BK-KgPWkx2Xu1dD9tHkDltvDqhyYZCnPnsL-ae8qEHA3j5KcnBCfTlgS1rIrGHZG9SsJlMeFCb62PcR-1qQPFk_y4hGLBmhiF9i92zit1ZZCx3q0GkweZEDUwCDvaMNbZ9W8Gmu79aGUzcgAsB_-eFP4eBn4HWNsNaYGx9OsuQhCS1DmUe3yCaQbDWXXhMXtlNd8v4J3VJfxOT8m9EDpGrGs1p7vqA29iMnrVhTGcSPT7URYAx2yllvfRg_dxuIgUh1_jylO5DaEvETiS_uQyKsPrzM4Azvwg55wcfgbL40wv7D6MhijPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTQCJ9epCBS4U4jSLg8q2C2SQ2TPDfuDK4ibeS4n4WdSgKJ5j57BhEaBRWujmRbF1Z1c99rssjONY6rAwS6ZX-mv7BvjlWI_FgpsrKqlvd627yFZVlb62Y-NHoNnLLR8OaLVwNAgy9R5FFcNmblEuLRRJf55xQeSZPZQxBDZ1fz6b1VuBBgi8lHVOjKXqZpE_0AYaibuMUP4g4a8xXgk0_I6lvYzWXHO1H1eWWamudSQS4r29t7SHpxHyElAoiEfwDSZxyT-l7vdsXozZ15QmmL1YS8TPj_rmRKRCI2KYJ0P-riHaSEF94aZQpDO7LNMj2YTme4N8USsbCi5BAxfhuRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTQCJ9epCBS4U4jSLg8q2C2SQ2TPDfuDK4ibeS4n4WdSgKJ5j57BhEaBRWujmRbF1Z1c99rssjONY6rAwS6ZX-mv7BvjlWI_FgpsrKqlvd627yFZVlb62Y-NHoNnLLR8OaLVwNAgy9R5FFcNmblEuLRRJf55xQeSZPZQxBDZ1fz6b1VuBBgi8lHVOjKXqZpE_0AYaibuMUP4g4a8xXgk0_I6lvYzWXHO1H1eWWamudSQS4r29t7SHpxHyElAoiEfwDSZxyT-l7vdsXozZ15QmmL1YS8TPj_rmRKRCI2KYJ0P-riHaSEF94aZQpDO7LNMj2YTme4N8USsbCi5BAxfhuRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=dJfihuujoju1E4Plk2LPfpbyDhYz9GBFens1JEs1fEEkujzlHyycHijZ_1gITt6gHU8j5Ew4ZPvXKb7FlhqlB0xxUK4uk8-IuJsAUfh-pH11wpwPqE95qPlwn-VB67MdMiu0asoqJus-aNO2HbibO9_l3O9kV5sLofpBm_OQ8acA5ngQtk1-ivTW_tyaCIuxkqEkRXC0fEtmP_yCWZzhE-EejVAr9TiLlngg6ysre6i7HK8aZJ64lfe9yLrpfXbzw03_jgar1Z8AXe-IAevJhnfa6rZ852waNCbatk5JVVwYknKwMYwd-8KqwEYuH5MIv1YQCAuZU5tGHG7c5HR2OYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=dJfihuujoju1E4Plk2LPfpbyDhYz9GBFens1JEs1fEEkujzlHyycHijZ_1gITt6gHU8j5Ew4ZPvXKb7FlhqlB0xxUK4uk8-IuJsAUfh-pH11wpwPqE95qPlwn-VB67MdMiu0asoqJus-aNO2HbibO9_l3O9kV5sLofpBm_OQ8acA5ngQtk1-ivTW_tyaCIuxkqEkRXC0fEtmP_yCWZzhE-EejVAr9TiLlngg6ysre6i7HK8aZJ64lfe9yLrpfXbzw03_jgar1Z8AXe-IAevJhnfa6rZ852waNCbatk5JVVwYknKwMYwd-8KqwEYuH5MIv1YQCAuZU5tGHG7c5HR2OYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vjBH-v5L7KGzL06FAkUEWe_7wpbyIyeOQfKGAXCRDSZN9GQe7TyLSWraFjmSFj9U_IyDT_03GgjvcNxYQ37DVTZ89Jb9YGBYNu5cDI_8TIEXcnEgmbiNGBWCamkTpChvFVGvrqUM5FQT790R8Res8nkGtXi6bIyDVf0go-r55pfLKdUrAGwa-Pdl8mpI6t8V_vGwqkHApIAXYrz3mCng__QpRdWhdfkOprX0h82ZTo_YrlBytwnun-uLqoNzJAoKRl8ZfSOi-kaC8PKLqoCe9L-xExVZzNBqX8KmkGYajZOa1moQLd4RLIe4AbCPicYEaMPjeJMBz4oCWG1IxU1f8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=vjBH-v5L7KGzL06FAkUEWe_7wpbyIyeOQfKGAXCRDSZN9GQe7TyLSWraFjmSFj9U_IyDT_03GgjvcNxYQ37DVTZ89Jb9YGBYNu5cDI_8TIEXcnEgmbiNGBWCamkTpChvFVGvrqUM5FQT790R8Res8nkGtXi6bIyDVf0go-r55pfLKdUrAGwa-Pdl8mpI6t8V_vGwqkHApIAXYrz3mCng__QpRdWhdfkOprX0h82ZTo_YrlBytwnun-uLqoNzJAoKRl8ZfSOi-kaC8PKLqoCe9L-xExVZzNBqX8KmkGYajZOa1moQLd4RLIe4AbCPicYEaMPjeJMBz4oCWG1IxU1f8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSDeMxQcbFdLP_olH4g9Or9B6N1RQ1F7phUbzEAea8D0CDLcSCdYIEg_rMqO-ayFjECwJSyD11iemkimgP-NT9uJ-Tvl_o_p4_PChr5sDIsf2GEEGszU4kVtxI0TmraCJW8De2dFtmYHeVpeZZKKm7qb5WcPI0s4j9ZI2-6pdo7xolUWUoOXwEzRPXOs9ehoVnv5XPsecGuAo7MN3STC54ZGU9Z4I6oUd-Y-VvVyNmyTAmse8Ua6ACCCNQWhKZsU1NOTYiERZxVyHiriSCB_3diNxbltRiuD7s3JlkN5zcDrCJ_y7HQADYyhep6dbBMVXcVjdzc6w60cbwKpQsOCDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Au3bobJSnBQJ945iUX0r-mGKgNBqtvUsvbTjY5xinn9iJ9cijweer9VGFDskqLOoY3H-Od58HLV-f-cr4z_kFfqNn3xLyJ6C-XKqpNHjdJRQNHO7k_G5LOcb0ok36i7p78DueOzW8OaEWO4S3KjgHA-wkHes0M9Q4Yu_6n3dV9PjZN9x11Gs_eppwJYkF6B6KqUbxwZ1ciwzglNhxvim7BPhy9tx0f4PME39xMokKdMGVcqQKVf1iRu1DwEaSLf0MG5TvhByU6LXYLR-zB_A_u95lEmkPRtu-BXcQjDOd7oJ1ZciRA9H26J_Cr5Ue2GrrasNjqwk1qQ617U9JyKTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=Au3bobJSnBQJ945iUX0r-mGKgNBqtvUsvbTjY5xinn9iJ9cijweer9VGFDskqLOoY3H-Od58HLV-f-cr4z_kFfqNn3xLyJ6C-XKqpNHjdJRQNHO7k_G5LOcb0ok36i7p78DueOzW8OaEWO4S3KjgHA-wkHes0M9Q4Yu_6n3dV9PjZN9x11Gs_eppwJYkF6B6KqUbxwZ1ciwzglNhxvim7BPhy9tx0f4PME39xMokKdMGVcqQKVf1iRu1DwEaSLf0MG5TvhByU6LXYLR-zB_A_u95lEmkPRtu-BXcQjDOd7oJ1ZciRA9H26J_Cr5Ue2GrrasNjqwk1qQ617U9JyKTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=cVpmZ0qJ7A64GfuEZDPtMnZW4Uk3aIXT_btEbILUZ6Ezcdq0qWFxIpv0As0mJuzwVamo-s9NrwjEyu16ldTaIuqn3GyHgQs-ZX7D5NGZh9ceWZZ7IspD1mtIjxTyXETGjrufWFbxt1rl7-mLaIPoZ9U1_jvCsliBsSvhNCNkd5N_-nUBHp96PIUZD5i5hgRGmJSbJYsPZemHAJ5yP4Yp9zAX3MM3o7AuZ9VPPBgYlzn00WqWq15Yzag8WuGf8u3MeiTpjzyCmHZ8S5wYZ53sTX1ndx5bD-OQU4ZPoWv_9gLgRl4JqnAXuEFQRUKDBFG6U80jWBh-E8VSJ8Egf6b8YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=cVpmZ0qJ7A64GfuEZDPtMnZW4Uk3aIXT_btEbILUZ6Ezcdq0qWFxIpv0As0mJuzwVamo-s9NrwjEyu16ldTaIuqn3GyHgQs-ZX7D5NGZh9ceWZZ7IspD1mtIjxTyXETGjrufWFbxt1rl7-mLaIPoZ9U1_jvCsliBsSvhNCNkd5N_-nUBHp96PIUZD5i5hgRGmJSbJYsPZemHAJ5yP4Yp9zAX3MM3o7AuZ9VPPBgYlzn00WqWq15Yzag8WuGf8u3MeiTpjzyCmHZ8S5wYZ53sTX1ndx5bD-OQU4ZPoWv_9gLgRl4JqnAXuEFQRUKDBFG6U80jWBh-E8VSJ8Egf6b8YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=NapjnNwUhgX29c6Nezq8oVQ0_gBnsa90RgbS9GxmpUM8qzA1oKnTCU1fSRlJJYuNz11rGEYvV6TNYWruPcqW8Umd95BfMi--T3aCX7O8ILU5TEllYsAqBF1No9RaZSQctSmsEiRR37QMwIQ0acAZxNhULoKmRgR6yS0YLOXyE341q-SkS0hvs53JfqTMRB4CHYQOvF-z8T3xUOB0M5BT8VAZeCAECAojoWvU8GTVGFNb-S-jvguDf54pYm9gZPI4yu5s2MpydH1tPjfNwd4WfQ71G-jDykuZmdQyOERYy81rViY2Cpacy68eLC_x_f664DjkKpoy0cm3vTTH8SoZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=NapjnNwUhgX29c6Nezq8oVQ0_gBnsa90RgbS9GxmpUM8qzA1oKnTCU1fSRlJJYuNz11rGEYvV6TNYWruPcqW8Umd95BfMi--T3aCX7O8ILU5TEllYsAqBF1No9RaZSQctSmsEiRR37QMwIQ0acAZxNhULoKmRgR6yS0YLOXyE341q-SkS0hvs53JfqTMRB4CHYQOvF-z8T3xUOB0M5BT8VAZeCAECAojoWvU8GTVGFNb-S-jvguDf54pYm9gZPI4yu5s2MpydH1tPjfNwd4WfQ71G-jDykuZmdQyOERYy81rViY2Cpacy68eLC_x_f664DjkKpoy0cm3vTTH8SoZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caYcdU0_WeXdhN9JaFX1mvJpW6mqegD86HH9jC4Ih-ve0FKAO5ll3RfUzHsLG672QS9AcRk0esJUZf7zQqvugOJfznP9D4cgQNri5BjtQWL51L4S2qfZ2J9ltS67OSPhbuav2Z73XNIUXcW9An8fdXErIDfuNNWTMR1p780sviaE02BZESRMrHCFsQSt6vmMr8njxDgbtqKeC99v1uMFXqZWc8prdO4GuZx_wNvSUc9q9WBtJq8GxVi9yGWkd5LfpM2E_tfAPZlaEkIt_8ojK2USSpwk9-LfDfjIzzHTYA1BLRqcs9t6pRz8LXvNdmGbR-01uvknOelkkOTHOBzyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAiNYdmyDj4p0EB1cCFd_B36Ge3IdZB0aG5zWbKvVIx1dTA_Tf6SfuuFYf1pxKA6_qO4ykShaaXQGRF8_r5TJf4AOlb4lVcycSkG1pomECea2wvmn7Eiz9qvqIDi81LNb1fDuA5jMEuQK8zciPBGVE9bIvweaRV7xTHqeFgcnWB2NBI7pQU0T40Fs9zs_BS9mm0S7G5knno8wnQ1IEivNSbPBrO7hucy9ODmhKsEMRcKa0bqTzFaImv_cnx-DOr3syh7chY6BBhGZOoDi4dkHNF6klHf0RarfG6f1bIewO63JP34fB14Bxbo0zFyKnuSKqz2ADM1monrdcmv33mnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szRTZSTrKDLAw0mMerbNyqPRzc571M862qIXkRZyoPsvt1sXxJYV5NELEVZTNvCtXRWZ2blE31hCmIjsVjBg12EMt3t2Ijtt08nRKLQkC-HW5V1VJ8vhW3UIQN_87SSlZ0JrdLpkBvveHdPLrmCKR0a5-MyfGQD1DBI_kq-wjKmqrGehkGhf3x1awLgAoU8FTldzi6ewFtA2R0cYelZrUO_5sxFLyH7dI0TLPuv0juVKYqqouzZjP0RHGOhkETuJkpR7ubdWHoFpt_LT3y0DXsUFaHM43H75HAC9lzjCthxZ2_heC9f2YQ5r_rEvpYbxgjPr8PXULhcBvtU85MZb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5Lk6n7UH3IiY-l5ItRif8WOhz96T5Z9s9oALjRF0osuNo3z-3OkMN6dYjVPxC2lLXyMVNVSsZ7NkxCUlGeXIi3Ajbh4pVkGWxWozVTqjSQuilerpjyWMMsBxzsb0Xhu55Q1iJW56_8nfEYje2JZRs35_LuFMH8zHnYcXrks0A3sI9A8KNBzKTO1b5vR6AZkovUc-zBNN4iom34qlxCVxKIURkzgGR1CXWKZVSf8enO3syFHPaeBms3KHIHMR4SnGxn_q3b74jzFSLDvP-6jL76EiWeQ_kKPiKvbQDkDNVybaovPjq9R2xaAk2QhYaZ1KuDLaUFTFQSWfN3SWcyUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0nNbnxcQV32jH-RRnfQTS7DHvmGWgty4hymNcd-GxLJLC3IJoAu2ybPLuUAwwjiBnpuLtMiAUiiV-_04qNYhEmUmRTYISwiirmWKMPD84hIXBwXCQI04_VWIPr7g70y8FmA91SsbAoTpsPIUBPY0--pFUfLHd5TNaeHYwYAogCNqzdKqJQCBE1IBONGnAJjSc8aLfVF4ebZXLTijZFUQSesE59cUoA5-QHVUcCvz7Edc_KM_56cXqmJ2bLn7LMSdRObXp4DQmZ9xTr-NwkPxCGgE1ROTDtKxrk_JB6vWhWcYrteCcjrPzKUx1tYsTqh3-Xr8S5XJKYQimHRtOUicw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WOPMS1eSYh2Uujz0RzIFJpE4CUFeAinjfp48chd3VtMYGFwpg0yMb1TE5LZf9kgva-VIMIxSwkBrXZEBWvL5Iihb4I2XiLBBsArFbAOcjEGAWTsjumGRd_C-S7AKAcxUsgJA4V8vxUQ4zF7wpSOOdTWeUkSV1SYKKytfWBTNvKyPAHaI1OsmL2i2YzA4c3cwaoZ6M-0ch2VbKwM_L1JHHTdF-LUrC9Y-Clha4wiOQCS7h4RpTxE-TZ9jBjJauZxvSm1WcTBH2aGCnsTFRCUIVWbt4Ejg_r5l6GTesKZkhgFmDjIhY-C6uuKzFrVotkXeObcE-b1FUsclRHd3oR-OGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=WOPMS1eSYh2Uujz0RzIFJpE4CUFeAinjfp48chd3VtMYGFwpg0yMb1TE5LZf9kgva-VIMIxSwkBrXZEBWvL5Iihb4I2XiLBBsArFbAOcjEGAWTsjumGRd_C-S7AKAcxUsgJA4V8vxUQ4zF7wpSOOdTWeUkSV1SYKKytfWBTNvKyPAHaI1OsmL2i2YzA4c3cwaoZ6M-0ch2VbKwM_L1JHHTdF-LUrC9Y-Clha4wiOQCS7h4RpTxE-TZ9jBjJauZxvSm1WcTBH2aGCnsTFRCUIVWbt4Ejg_r5l6GTesKZkhgFmDjIhY-C6uuKzFrVotkXeObcE-b1FUsclRHd3oR-OGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bSt7YRRqRVnDIIfTWdQok6jKmjEwDJ_fBTiWpsWtdvr5M2LIkpjG-mQnL-JlNu-V4sxHMm6ooqg29jL7gxatgr2PpekPGs8SdH0eml8TLQN-kmOEUaa_yCdRozeIic8OIwxZFWKKTVNa6iD138D5aB6AhCVVvwCM_HoOWYie52hEUojapM-cfO1QoxK-HmZuhGHPlbpoK99Uu6UaY-VTSKijczsKlwvx6XBvHz0ZWJ-1B57zml4ZI-SctgKB7NC0kVfe-db4EGEzv2dZ2OHhNzOEt7t1YNaVfuMVGrpCqiej_6fNvp0BRf-05eqg80oQ4egzCBM9fQyTCUF1-r0qCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMr8BRG48KK7e08EPL4wGgUqpQmcrNmWTUqzxOqKYMD6QJ7cPyPPSpdxhomWBjMMjGHiNLewKxw3i0ZSpZ2pQv6sv-xvFU8yKzGG-9u_SLar5Lagt0uqIXPkcyq9dCXmE-xU0Kj3N4pCCDmjg8wLW_ZS3sKcpDnTvgroTz-T1h_VydzlUw-Tdxj0qNFCZMLujgb4cMHhRnpIfSx8xZyfpc0pcja7eekgmQUfFUIfinVUDYeIOVTms8ExV8N4fV37g98ZAHTMktdy-z_LV8kGWN0kYPtc0KJoUal6OM7c4lnJaTJtiPZ71PIWxQRvvLO3FjnrqWtpc_6xR33t6ykMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpYL3SLQYlibPzSePEFiOV2luWClPeA0zGSfoVFdBAr-PBPHvKlD2-VoDAcsASJCYnZqUnH1B4Y59tqzRnGSfz3-SExz89Dn30um3HLzbJxXbM3JH0MOQUL5dU3VfQGqNCFTCnRvSSI-KiPmEe-C9ey16q60ZKb716b8mzcsUhIU65L6SOwQuiSKYlLRWh-jIKeajyMO9qhuWBcY9JrLwkT072BEMAFqAN1ErmJkHNvBO5C78Z3Htdh_Ymz8DrJPOllLTtyxe3BhOBETGJLFvFDzeCas46rERInWQ9hj_ub7uJXn-CXvqjmm2oeAPucQLnvJ3WU5702udj4JuwIVIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=X-W-esNG94uSfBMuVuBlXjEChikraQy7Bg5yFs-ESzGtC58_5BHJ-joexCe99ITNmUtlt2MvIkbpepW0eoSVBRlaTEV4Dhgc-0D4Gk5ZoM9jodbSkTgaLvAWIdaW74xzlli2tBbZR6GJnK7TVhtgl1OKtI5wFV-BZMtgBRi95F5MGzWkcu00RMs3dmP3hGajvrjRgWBApwkMKzemADOA5eajdI92E6AF5P9t7Eng_cxW1EVAQYGL4Jq_OGy5oVXbTd8MRyJ9bE7UEmRfms2qVhUqTv-HOkmajNTbGYcSSvnQB2N9T5k2umVeGjWSaPeXHrrAntYe5yQ9deMHxfOEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=X-W-esNG94uSfBMuVuBlXjEChikraQy7Bg5yFs-ESzGtC58_5BHJ-joexCe99ITNmUtlt2MvIkbpepW0eoSVBRlaTEV4Dhgc-0D4Gk5ZoM9jodbSkTgaLvAWIdaW74xzlli2tBbZR6GJnK7TVhtgl1OKtI5wFV-BZMtgBRi95F5MGzWkcu00RMs3dmP3hGajvrjRgWBApwkMKzemADOA5eajdI92E6AF5P9t7Eng_cxW1EVAQYGL4Jq_OGy5oVXbTd8MRyJ9bE7UEmRfms2qVhUqTv-HOkmajNTbGYcSSvnQB2N9T5k2umVeGjWSaPeXHrrAntYe5yQ9deMHxfOEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=dt-26oMvWn70CPiMteZEnosko3_fqfjTWIpwrGEEPFgnBYRn6jqLy7DVVOsxbxuLW_KdH3BwP3GYKMz4AOWsRHt17Dca4hFQik7MOi-W6LMEhBy3cjNHMpIo8-DugDrjDB98wJSypBnsttbksDjndQs8O2wjxQzrA5LJOT2-7r_TnOudhd86TBUgmNul9Qtl6MsUk7ZRK2tOrg7HurW_h7KaTZQn0y9B7vsDqpcnX7LpmAJJVT726iGiRN1c7gUI4S7XHXBs-qdPbUCcxBv8moteJJtqitXsU8HOtWNd-SsqMHXfjLsCmNGTD5CjX6maucEWR8eXHd-j7po0W9UppDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=dt-26oMvWn70CPiMteZEnosko3_fqfjTWIpwrGEEPFgnBYRn6jqLy7DVVOsxbxuLW_KdH3BwP3GYKMz4AOWsRHt17Dca4hFQik7MOi-W6LMEhBy3cjNHMpIo8-DugDrjDB98wJSypBnsttbksDjndQs8O2wjxQzrA5LJOT2-7r_TnOudhd86TBUgmNul9Qtl6MsUk7ZRK2tOrg7HurW_h7KaTZQn0y9B7vsDqpcnX7LpmAJJVT726iGiRN1c7gUI4S7XHXBs-qdPbUCcxBv8moteJJtqitXsU8HOtWNd-SsqMHXfjLsCmNGTD5CjX6maucEWR8eXHd-j7po0W9UppDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo46yuGji8XaQxcyG4W75GB3cjU_nCiiz_eKSvjXxeBgzyMBxec-jG9HgToHgiA9KvMD552NmVvz9Yz6NJO8b1iqTAwDMQGgtRV8OnliPTUu5mutlcEUPCPAc1Gw252h_RUhzFveaqIs4UHzMic0V5OmBJzNOh8eTZeZccsCCc684o2jZWmRThN_Fwoz4mzxF2lXf_eYzajOxU0j_guJ5ySf_Edf1N0WzJYsiAPdKT7SRgvUEA6WnwVHIRJ_oD-p6E2PdGG4Ah-SeGLladt9jv1f4l1jRTkS7w2e4wrA92jEM3wZOSZi_YXrjuVBvkBdNrEAeO6W4NgzsknvJ9J0_-96o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo46yuGji8XaQxcyG4W75GB3cjU_nCiiz_eKSvjXxeBgzyMBxec-jG9HgToHgiA9KvMD552NmVvz9Yz6NJO8b1iqTAwDMQGgtRV8OnliPTUu5mutlcEUPCPAc1Gw252h_RUhzFveaqIs4UHzMic0V5OmBJzNOh8eTZeZccsCCc684o2jZWmRThN_Fwoz4mzxF2lXf_eYzajOxU0j_guJ5ySf_Edf1N0WzJYsiAPdKT7SRgvUEA6WnwVHIRJ_oD-p6E2PdGG4Ah-SeGLladt9jv1f4l1jRTkS7w2e4wrA92jEM3wZOSZi_YXrjuVBvkBdNrEAeO6W4NgzsknvJ9J0_-96o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtpMNR4ceIuQjknb-lrpaEq1WZzrLC19bou-ZqpGWnuQR6ttV3HCOW1t9eVrSX7_U8G21unAggi5sxdY664msKUzCEeqLRVhR2cfwH5E3Iuc5U4rRuuMpzYT4IbveyJKMNPYbtok3o_pgeirZPvTXNJ1JztbZZMPN10fHtO4POT0a48ldpgIsCRfC0w7iOEfV101RYNOId423z3dolAw-vDrKWyqV5351ygRTNAQBuAEwR2cY07xqywt4c1QLOnhNbU0TtzQ1jiFLYbM2XwB0hVulkqBgyniiWDlzYVmwoynCbsMtGxjxcm715Sx89Xhdjel-fHLkW4lqGdhUvsFdSc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtpMNR4ceIuQjknb-lrpaEq1WZzrLC19bou-ZqpGWnuQR6ttV3HCOW1t9eVrSX7_U8G21unAggi5sxdY664msKUzCEeqLRVhR2cfwH5E3Iuc5U4rRuuMpzYT4IbveyJKMNPYbtok3o_pgeirZPvTXNJ1JztbZZMPN10fHtO4POT0a48ldpgIsCRfC0w7iOEfV101RYNOId423z3dolAw-vDrKWyqV5351ygRTNAQBuAEwR2cY07xqywt4c1QLOnhNbU0TtzQ1jiFLYbM2XwB0hVulkqBgyniiWDlzYVmwoynCbsMtGxjxcm715Sx89Xhdjel-fHLkW4lqGdhUvsFdSc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=OKyARkp7SJdWhCK1QxNwBp2T0mSkyHSlRDrmk36jb2j1n5nZBJZ29q0XR8u6uLgx2HeACZhq6LdzGjybReNQd-MSlddO_BYttGRXzglxr540Tukz0UVBCP00czFn70P2L9YSat71z69viZ4orw8hwJGy36nmfHhrkTwgpYWsIwy5Xk_3jq4V2fIXrncV5Qpg6J1Iaw0s9Mj86X8ArRHC-CZLUXjB5PypUzaGHnMWIKhOcypAiFg03pTpL8qdfotJMufjZoGXut4i_ZjAqTzJgIJQhQRZuk9qlKeAuw7DyaftvbhKIw97ZUCtP72gwJJ0x70Y0GZa-cr5_DQi33b1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=OKyARkp7SJdWhCK1QxNwBp2T0mSkyHSlRDrmk36jb2j1n5nZBJZ29q0XR8u6uLgx2HeACZhq6LdzGjybReNQd-MSlddO_BYttGRXzglxr540Tukz0UVBCP00czFn70P2L9YSat71z69viZ4orw8hwJGy36nmfHhrkTwgpYWsIwy5Xk_3jq4V2fIXrncV5Qpg6J1Iaw0s9Mj86X8ArRHC-CZLUXjB5PypUzaGHnMWIKhOcypAiFg03pTpL8qdfotJMufjZoGXut4i_ZjAqTzJgIJQhQRZuk9qlKeAuw7DyaftvbhKIw97ZUCtP72gwJJ0x70Y0GZa-cr5_DQi33b1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=LAvBH6MmUArqrnV-SKxQB9An74b0kf920MJZV8SHMIYWEBsVLmnJOoZvrALBBrDIPlBqAb3edQlslS3CrUx8jvDAFaby6uPhh224QJf6wQU_L-6KLo9s6NajgLT5HgUdhaP2JlPTS3-IlvfnhhH75K7Y6C0GbRtfOfZcM_tKWSt1_nYo9ikO5YeYcskLVfAB0tuEodic1TN4sLisDSi0VivMm2zmizQrVlOScqeN-44nhi5ujLkwjOn3aQkaItT1J5TWvkkZm2Sup2DRQV7Long1-6tywPpMBg0RlB-B1pKnvNtRkYjj6TJudneeL-ffUXgiGzTsZsy83XVcQghk2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=LAvBH6MmUArqrnV-SKxQB9An74b0kf920MJZV8SHMIYWEBsVLmnJOoZvrALBBrDIPlBqAb3edQlslS3CrUx8jvDAFaby6uPhh224QJf6wQU_L-6KLo9s6NajgLT5HgUdhaP2JlPTS3-IlvfnhhH75K7Y6C0GbRtfOfZcM_tKWSt1_nYo9ikO5YeYcskLVfAB0tuEodic1TN4sLisDSi0VivMm2zmizQrVlOScqeN-44nhi5ujLkwjOn3aQkaItT1J5TWvkkZm2Sup2DRQV7Long1-6tywPpMBg0RlB-B1pKnvNtRkYjj6TJudneeL-ffUXgiGzTsZsy83XVcQghk2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=E_IuO0DY_1v9kr2uSO_yokzOg3Y6tOj5kv_hwQ1MyJSX4ShQ_QGfO39ysBwvNok4xRoW82wNAtFP67GqxCjdRUxMr_Zqt2pdshfQX9mCf4PaOY5DhEWslR0ROD1FswfnmGDhy47_c33Vgo1gy4idFvxLWpp8J2qeQxMNGJ9-wFhb5f-Rktf77E9C32wVAVOMVpJQJxZnkxVAuKINLI6gICD-N68miaBqXeDbGDVGTed0Bmx4mBYjV2kAo4LclEnQEYqdp8X1QXOi8X8nbIYPNkbZJUqPD_ukrH6N2jbmSMTRw5kWOu3cbog9xsMNOQuTc62YsXH1VmXk0ZjsUbFT2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=E_IuO0DY_1v9kr2uSO_yokzOg3Y6tOj5kv_hwQ1MyJSX4ShQ_QGfO39ysBwvNok4xRoW82wNAtFP67GqxCjdRUxMr_Zqt2pdshfQX9mCf4PaOY5DhEWslR0ROD1FswfnmGDhy47_c33Vgo1gy4idFvxLWpp8J2qeQxMNGJ9-wFhb5f-Rktf77E9C32wVAVOMVpJQJxZnkxVAuKINLI6gICD-N68miaBqXeDbGDVGTed0Bmx4mBYjV2kAo4LclEnQEYqdp8X1QXOi8X8nbIYPNkbZJUqPD_ukrH6N2jbmSMTRw5kWOu3cbog9xsMNOQuTc62YsXH1VmXk0ZjsUbFT2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt044yzb7Ize9FsE7_Ctn4yuBx1JQTO0012mXTLvTkkPx46F72UnFXmU3c1bnkS3xAXRyG6k8KW2o7omRUwtOheRqoBa5JvG6pRtX6OhqLDZzxQgcxMo8-ZgaRg8FK9rhsAWA18PmSNi5_sAeWFVJc3hYsFsThATS4Fev3lQCwHMAHcmk9wB_S10bjDAJ3DA8e6qATeZsH1oQPgzGh6PYuF0kHQkx_ZT-DvfcgW6vvRGhMMg9lKj_wZ9ubFQPKSZwtqxSz9QMwU-NcTvYKKb9ws9HBiO2oaXjBEtAZ4Jn_C8UcvRTJ7tvgvOiIRAJE8TTNlBUYW8m_tPy_mCUjV0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=XRkGrwwL7qAwuxos9Yktw8CCcMuQTQ2HhTL4rz2R4_YZmZBMYu5O59oUs8_YbW2lzX2EAHlGbAaRi8-uuPP30KLicSCjsIo75C27HVpTk7BQWy0azA6aTivoo5b-k0wZiD5Ot8h1S4eerhC9gdgLwhotVw86uqMLkTtv-dr8iKl3gtrCh39EeHtkjBXvbJNAbTyWxQAIQGRpmYzNvCL5NoFvSrc8W8wCwgTRZC6sESffraZDNjAHD35WrjF-LLSxP1iCs38QImMTil_nLh-rv8SaJzw0ZInAKSBo9DR2PAwd5GXNblBXDHy4ZKaCdT7cbQRfM35xRxKe9RURL0H7pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=XRkGrwwL7qAwuxos9Yktw8CCcMuQTQ2HhTL4rz2R4_YZmZBMYu5O59oUs8_YbW2lzX2EAHlGbAaRi8-uuPP30KLicSCjsIo75C27HVpTk7BQWy0azA6aTivoo5b-k0wZiD5Ot8h1S4eerhC9gdgLwhotVw86uqMLkTtv-dr8iKl3gtrCh39EeHtkjBXvbJNAbTyWxQAIQGRpmYzNvCL5NoFvSrc8W8wCwgTRZC6sESffraZDNjAHD35WrjF-LLSxP1iCs38QImMTil_nLh-rv8SaJzw0ZInAKSBo9DR2PAwd5GXNblBXDHy4ZKaCdT7cbQRfM35xRxKe9RURL0H7pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fl78HaI739l0wvjA3FqdLgeIPlr1ASwjjSrE1wewt6yNcaEpcO-a5cCVvOrGT5JcbS_YBm_QnUVNMZvYbr-zT4TEmqdtmQ6KcDp5CZT42ldDC_7xg5B3aSyh5_MWpwyQk58mGd8rRJPfjACH_KzScREjxFGVNsyDTV6MWOt-N5jfyVpz7IKs_gJwqTnqZGaTMhC1auLGFSwP4MEI6MjdToeElV1I0U33vASD-yZrLB1IDDmjdl1oBr6nPbcU6WDsW5g_lg2sCG9NVuNrVtkELC9GtphXkkBoqGcdO5SbJO_uD5TW1pSwoQ9RfDF0Zdm8Gnmeu0Vw5DSlfBqzdHlIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=iuyIWCLDWIP_1l95clrD_Q0c1YH2_qMUnTIzljskxiM5cK9A-spX-zdj2vTwV-f-eVtnfSv3XFwP13lhrNVkLol7Y6OfIygkQiAGbnubwgIpnKTqtVC1FxPvk863wyK9x6eBrrXlS3-rTdokiD8QwpWTUDfh-UyHEdD0FopHfxh1y-hHJm9hkgyoLS88F6jwceaQd3NfU_RaCHFkScMABICacUfrEfeD_aKv-fwc93zEQBogIk66zu4muLNesmB4DqEHrYnsu2E5WikFl-2O3NvPe9jAGAbTC1lqqgHPIvVF9j6tk_gyrwyioUWFtkq83bU2sL9-wcIA-kbsGKGNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=SLEjC-BVWUfINrAq8oJ9xFJIrmKWnIOtgYHSNKrvfsZzvGRrt95zPoz9WWIx9TBMocHMBDp140E4ty9H8baI0sTcbstDdtCsYNj-w2cEakaRYUja63hE8lJuPmeXle1c417iVvmOWp0p0UIvYOWctcIYZEQXBlufwAs-s2fr34HoEoD0OvzZpiAnPTdAwxSj8bSbXAyIdEDuc3UNpd6JJPlkHaaf_N38RM2LJ1BR_lFpH12YB0HyOgwe2G0xQplBGa92-eqNYvlztnVhcZvDBDhBTbCMTQNgZcm2Y6iRkTYvXEf1GcRL32LkCS_K-gbzs1UorywggZKrC3vPJJpL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=SLEjC-BVWUfINrAq8oJ9xFJIrmKWnIOtgYHSNKrvfsZzvGRrt95zPoz9WWIx9TBMocHMBDp140E4ty9H8baI0sTcbstDdtCsYNj-w2cEakaRYUja63hE8lJuPmeXle1c417iVvmOWp0p0UIvYOWctcIYZEQXBlufwAs-s2fr34HoEoD0OvzZpiAnPTdAwxSj8bSbXAyIdEDuc3UNpd6JJPlkHaaf_N38RM2LJ1BR_lFpH12YB0HyOgwe2G0xQplBGa92-eqNYvlztnVhcZvDBDhBTbCMTQNgZcm2Y6iRkTYvXEf1GcRL32LkCS_K-gbzs1UorywggZKrC3vPJJpL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=LoUSkw4cUYYQcFlb4WL5IrsGNgOdKV4ArnMEzIPkSFYaIN0g_7tWdvghFkcnwYpCOzKPzNp0gnvPcBXuB5cOtKtxk-m7XruTOg-swpUGFMT_yuksAOymshjPyb1fxZ70fMmL55GsovADYwhI9Sqkf0mZjWDlZuaQCMv6fZCs5g6sl3slwInrB9FhrRCBF2UjGA2cOQ2jNHpV2D8AlyZomCG8pFMMfqVC_niK0RsJBioUaz_XH8Nu9fAloaFTvhifWkAp3E4SsxQfNb1pqD0AL62mESVos9OOvNUcpJy3tB-1ITNnyj08uCyHHmI1gLdN5eBOQ_ETCrYsIySjzbvCFgnrj9oK_4KtdN2uotn1czTMcl13gMumuNb1rlhECeqnrWpcvynDCmTjgzVlSmjYGCTqXkPj50hoFYtKb8WCzFIDAKtswB0zajS5Arl0D22pxR9OAUmKyEYTjjzWs2wuDgnqgk0NqaaqV9suurThSvQ1jvFqEMCS7JlMoiYyrs6aeyZqYdgk-3TiMSdb6oIjuTl1nRb3Oy_9DdXE6TPx3XT9t_BLBJRyGsW5aTw-xOmnO-vYaDHCrO9ceZmzw9oxfUQbrevyMdt9JhJ5Ogom_4UOr8NJ9qCqTOVSHGnpwSHunYoF_jmBYrt5EB8wPWgdSul5Gjqh4YnfoBcfdEP71Ek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=LoUSkw4cUYYQcFlb4WL5IrsGNgOdKV4ArnMEzIPkSFYaIN0g_7tWdvghFkcnwYpCOzKPzNp0gnvPcBXuB5cOtKtxk-m7XruTOg-swpUGFMT_yuksAOymshjPyb1fxZ70fMmL55GsovADYwhI9Sqkf0mZjWDlZuaQCMv6fZCs5g6sl3slwInrB9FhrRCBF2UjGA2cOQ2jNHpV2D8AlyZomCG8pFMMfqVC_niK0RsJBioUaz_XH8Nu9fAloaFTvhifWkAp3E4SsxQfNb1pqD0AL62mESVos9OOvNUcpJy3tB-1ITNnyj08uCyHHmI1gLdN5eBOQ_ETCrYsIySjzbvCFgnrj9oK_4KtdN2uotn1czTMcl13gMumuNb1rlhECeqnrWpcvynDCmTjgzVlSmjYGCTqXkPj50hoFYtKb8WCzFIDAKtswB0zajS5Arl0D22pxR9OAUmKyEYTjjzWs2wuDgnqgk0NqaaqV9suurThSvQ1jvFqEMCS7JlMoiYyrs6aeyZqYdgk-3TiMSdb6oIjuTl1nRb3Oy_9DdXE6TPx3XT9t_BLBJRyGsW5aTw-xOmnO-vYaDHCrO9ceZmzw9oxfUQbrevyMdt9JhJ5Ogom_4UOr8NJ9qCqTOVSHGnpwSHunYoF_jmBYrt5EB8wPWgdSul5Gjqh4YnfoBcfdEP71Ek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=Vn8nO4dXIXmcDwxqOlRxcspjHFR_Biv44NqKbSL3DrPVLl4VCJ1jmO9RgbxjNk_gDzOLFz2R_dsTr3JlrF6GIQmzT-BUcKrVVGwfsbjIEn4Lf-jFBAqyAp8ttKPfdtt4skzv4j1iY8ovaZJKa-xU6oaBHb0TcEnrFpKlR8oXf9tUvQRREFc0mrUym6WRBjEvcAy-fZ-BzXzqZQsgrOxmiWBL0FmKSyqAeB25AvFNuzADDJ26MHwm25QDnUnJQjXDzniUNhsySJtgb8nPyj7nI6DT5UxGIWMXQYLdpM7SXnMzptd3IXBcQF6ZT5Yq1kORKhVUrsdktTZESPpyuuzHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=Vn8nO4dXIXmcDwxqOlRxcspjHFR_Biv44NqKbSL3DrPVLl4VCJ1jmO9RgbxjNk_gDzOLFz2R_dsTr3JlrF6GIQmzT-BUcKrVVGwfsbjIEn4Lf-jFBAqyAp8ttKPfdtt4skzv4j1iY8ovaZJKa-xU6oaBHb0TcEnrFpKlR8oXf9tUvQRREFc0mrUym6WRBjEvcAy-fZ-BzXzqZQsgrOxmiWBL0FmKSyqAeB25AvFNuzADDJ26MHwm25QDnUnJQjXDzniUNhsySJtgb8nPyj7nI6DT5UxGIWMXQYLdpM7SXnMzptd3IXBcQF6ZT5Yq1kORKhVUrsdktTZESPpyuuzHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=ImDwBDMo7s7--YksHnZZTtSd2ogTyCdJqviz-kxzypYLgmJnIP3MCVgh06VM7LQY2SCRruC2jS_zR9UyLVLGqBaN7gzSk_O6WeilHHp5WNZUtOvIuEMcPGThdedyZQZL5QZSHhJbMlgWXAisPFDNI3pttgWgNCpvRk4ln7EoZFZp47J1CcNHrsZXghzB10S4ZrX7zsey3Eeuxq5LIGdJFe1VSf0rY-Y1GFHbd2Cn08P-kgeHzf8etI0XMftibVDfAWTPZKta2tEs7nwmz3JiKKOBBIeY3IHlfmLMajQse09DU_9h8rnB5LweEIUqLgm9x4DZzr1TrBCy2ShBtY9Y6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=ImDwBDMo7s7--YksHnZZTtSd2ogTyCdJqviz-kxzypYLgmJnIP3MCVgh06VM7LQY2SCRruC2jS_zR9UyLVLGqBaN7gzSk_O6WeilHHp5WNZUtOvIuEMcPGThdedyZQZL5QZSHhJbMlgWXAisPFDNI3pttgWgNCpvRk4ln7EoZFZp47J1CcNHrsZXghzB10S4ZrX7zsey3Eeuxq5LIGdJFe1VSf0rY-Y1GFHbd2Cn08P-kgeHzf8etI0XMftibVDfAWTPZKta2tEs7nwmz3JiKKOBBIeY3IHlfmLMajQse09DU_9h8rnB5LweEIUqLgm9x4DZzr1TrBCy2ShBtY9Y6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsXtxR4Oe_33-943L_FsQFLzIWTgtEpS3zoOb5WxCFIlkDUn9_M9yPBpsi5A2HRtxjVIcDyJshrqwV7eVEOhHLtLq_ON0Flc8irJe9UgpZTIC-PGccOGvXE-yfyLSZsTxtXOvq0v3NJYvQ1xdYm_2MDuFfK6PF2CDpahczlvm1OsHeFVuh7Dj09iH9FweDv3fJPiRsrgFS9jId_0MLe5Yay1oxJo9TrUNHfcj0_fWBmCWjFOb0X-gMgsmOnWAULEOg6V6N17M5keCjq0afvUlrg__DlzAiV-Znusb2AN8lXNp1EoOQNneQmklevvYEA_3fQFAbr2Cw2Mx796jPxPDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=FbGTVAjc3DpaXiVJZucdM0u67TiD9OcAkrNSlAQSDCo6wt226gNqpbfRXb34qtHrNxqmfL8oKUwEtO-lTYBhFOlrEP3wPglXNY8hX9ynRKHpFudXR8HS5R5a2-eEaFrfAPsU1UqAPGBngQeUreD5fS_9AELn-RursGBSbNHDY9k3zmNt4aqfY2A1YhdOUyRl6oYc6GOs2QGiDdFrO_NFCd2ZF6cklgyU5lly-b6cHHSUHUx7k6EszydBVX3U8DgBKmB69z-61Yp8YxzbRAPDFUBd5z5yfhrgB80sVIZKPUgbDsW6FwXRKaigc0r_-2V1OX8nYAmqI4xoxoWFVriHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=FbGTVAjc3DpaXiVJZucdM0u67TiD9OcAkrNSlAQSDCo6wt226gNqpbfRXb34qtHrNxqmfL8oKUwEtO-lTYBhFOlrEP3wPglXNY8hX9ynRKHpFudXR8HS5R5a2-eEaFrfAPsU1UqAPGBngQeUreD5fS_9AELn-RursGBSbNHDY9k3zmNt4aqfY2A1YhdOUyRl6oYc6GOs2QGiDdFrO_NFCd2ZF6cklgyU5lly-b6cHHSUHUx7k6EszydBVX3U8DgBKmB69z-61Yp8YxzbRAPDFUBd5z5yfhrgB80sVIZKPUgbDsW6FwXRKaigc0r_-2V1OX8nYAmqI4xoxoWFVriHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzgZDAMtrDQSAd2Fpn34Q20Gq2_yMspCwpwxfd9hwQ2eMVrJqZnjbNI7NnryxkDf31hiVrDx00O-1ShNBJqAs54aMjc5fHY7wyBe_R-aduhVH2_8yVKxa9VLopi5zP2F3MxYx1UIgOVzUrKsFStlLjQQN2R4Rej1bStYlY1LAOEhQCrwy7ITjSs3wi4TBmHxAg90jnX-N0gAMqBEhTj1eUAq_qFPg2M4W42CbJboyNnIoBJky0k7t-hd0lM27WQclyy7uyiOPfLNWetYxs7RiW3YWGnuRZ5atRDn3cyyAlZd_-hPukP2gxnWSFDXIRQEk0CP_3gZg5Iek4sToN58Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
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
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=li866bKhhI3m1IQN8lWzBhEuvfnOnkFibgasBbkHFYvVjM4XDCkKqIBV3RBCOx6Yn_VMG4SxAz8OVeZlHOpV6wKo8aEUfuTJIIXfKxgND7zj1M28xjwIPCru7aalpaNC5TtoBbP_qWWRsmeOq8MoPL2RNSSunsgxpf_L3SC469vNxH6eF--9AEaANwFXSXPsuZS-gncJA8TPvyFZPCR2XD_kPtX0xIULD2nAvOJXz6ugEodvXyfCZmXfdLtoYNOoZbowmSx_lQBAsxUxuXgFkfFq2vpLUwYjmPs9ELEZlmhaMeyPkRCPGIwTD7nd-WQXT1KKPF77f3QIWuzFWCbH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=li866bKhhI3m1IQN8lWzBhEuvfnOnkFibgasBbkHFYvVjM4XDCkKqIBV3RBCOx6Yn_VMG4SxAz8OVeZlHOpV6wKo8aEUfuTJIIXfKxgND7zj1M28xjwIPCru7aalpaNC5TtoBbP_qWWRsmeOq8MoPL2RNSSunsgxpf_L3SC469vNxH6eF--9AEaANwFXSXPsuZS-gncJA8TPvyFZPCR2XD_kPtX0xIULD2nAvOJXz6ugEodvXyfCZmXfdLtoYNOoZbowmSx_lQBAsxUxuXgFkfFq2vpLUwYjmPs9ELEZlmhaMeyPkRCPGIwTD7nd-WQXT1KKPF77f3QIWuzFWCbH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=V054NtPnnvyZT7ILHbZjYv7HT9v5OZDjMyvAFxo_Ey-piHiPl9PUNH9BbuduIZtCUt01k1FfDjmsjMSRX8czUx1M8cBXpFYS_hAgZ_TA6Ps9Z2HHPWl-pe2giztt_mVJlx9xMKfdtgEyMbKC0qOfetqPKjkD1ZIkP9OBv47PVl--RQ8-Okyu2mk9eDudnH4kjtnvHdR91R5_6ZU4bM6R4LZQwkt0dlzupJ4rpDnhsKn2YWVOB6xU8cw61kze9L4Ta6hm62fJo40th2uNwXr05ziCWHlfC7jAEm_mE8JeXGwKZRwG5px1Uaesxm_Ja-wi8ej1okLEf152m2sx4FD2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=V054NtPnnvyZT7ILHbZjYv7HT9v5OZDjMyvAFxo_Ey-piHiPl9PUNH9BbuduIZtCUt01k1FfDjmsjMSRX8czUx1M8cBXpFYS_hAgZ_TA6Ps9Z2HHPWl-pe2giztt_mVJlx9xMKfdtgEyMbKC0qOfetqPKjkD1ZIkP9OBv47PVl--RQ8-Okyu2mk9eDudnH4kjtnvHdR91R5_6ZU4bM6R4LZQwkt0dlzupJ4rpDnhsKn2YWVOB6xU8cw61kze9L4Ta6hm62fJo40th2uNwXr05ziCWHlfC7jAEm_mE8JeXGwKZRwG5px1Uaesxm_Ja-wi8ej1okLEf152m2sx4FD2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rlq45EUpT2abBM4vX9xE1YT4T7b8A2n8NN3E28PwU0faiCY_w0MTdnUk9sNJb2naHdyYREOm39AoBogfAF8mcR_xImYbIgOy3oPNucci2bysOHLOI1aUAqzQEWnxEui940TSp1wpyVK30T57X9hNN6vPaKDYwA5kSaFHNrAln7AJDbqBD1jjxKDwalVUC23dtRm_eMChk0xKx--nBR1tMzUIgNf5FwF8svBaYibqnkKTTySm5JzXqHsuFuhCXMrC0SoHTWoFOkhUrh1YkW0oxPBXWqF3RhWxfJvHdn_1QaNA732HFfHhELYLl-HdLDk5rA24bIvWf2Oh6TFOhgWnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=RP5uI9XZdnoVBAlT2YQ82M_EfvWW9wUowxKmCGjlSz8rIQz4CA2gBvcrsK8Ha1EXJsiEL67KO7kHl7NJdFxqq1k4hNbLj3Gc7pUmizWRmMCj3c9xocYzTHXiyuNplxSgJqal3V19aP_F7W7W7ebTNqHBiIU8PmTYNgF-Hz2ryDn0a1F7ZNq2-4IZKquZ7_54GZGlyoySlKSJCJPX6wm5KYDR8kWoF2CuQyFdjmI-b_O_3mlA23M5bTUOHHlGbQZiUWWMyJVmUK6l4l5PBialprMQL-i7s23WSwQeLtoNbYbInEYr4784LJWp5f3KucDM82r5VeRnNvwL5vggdcENMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=RP5uI9XZdnoVBAlT2YQ82M_EfvWW9wUowxKmCGjlSz8rIQz4CA2gBvcrsK8Ha1EXJsiEL67KO7kHl7NJdFxqq1k4hNbLj3Gc7pUmizWRmMCj3c9xocYzTHXiyuNplxSgJqal3V19aP_F7W7W7ebTNqHBiIU8PmTYNgF-Hz2ryDn0a1F7ZNq2-4IZKquZ7_54GZGlyoySlKSJCJPX6wm5KYDR8kWoF2CuQyFdjmI-b_O_3mlA23M5bTUOHHlGbQZiUWWMyJVmUK6l4l5PBialprMQL-i7s23WSwQeLtoNbYbInEYr4784LJWp5f3KucDM82r5VeRnNvwL5vggdcENMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUetzyrDkaH4q6Vqu1TlF6_Em4CAtO0PD2FvRnZu2l__Q6vxqwhovUWr2mfARA_tbdUIRGzm12KNlq7g9-_WtswM6QYUnetNhpIB1U9vZo9_UCic6pYuApXBDoJmCCQ3lK3EsnfVof3XzOCf3sC-agS9ujPDisdo2hXBwRAEu3uQ4UJJBWXCwGdU3m6dSANLL0f2s0Fp-BPcBq32-MiF75W5VSmQlJSKGRafI3xlotUZuvHTV7oQG3NXrA5KiZbH1qfG2Jardv_uZcMpn0RTUmRl7-kms7YFeO127Uw9Bu6mhmjHf2UjsGivWIu806TK1scpw_shm9MjgLYVDJs6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=pAXyJahA3txb3kBr596f60KxIAh4t74S0VNOHMoIQy7fJPsD1PKpj_jZ0bYGb8LZm-Xbc9SqPZgpE5tA_ygQnMfLgPxh6Ww4S_ifYi5K9agpORJsnSDMvMcl05cuWottrPVI0Cnt8Qgy4knlRcmyGdL-IhB0zr_0OMMM-jujjV1steCFo64NtSWdaWjNQGW4HflqgeSIBLAv2et3nspkW6roDir2IoeBNXNYkI_U9Sh56M2sKtHpxPIc8tJ0zAvojCd1lS01g_TtI1J8LjQNsQheERLyJvLPTBvHtG_fU2nxaCDaRwzrLzovqQrNm-t0YjpHppV22DSIRaTKmVdzmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=pAXyJahA3txb3kBr596f60KxIAh4t74S0VNOHMoIQy7fJPsD1PKpj_jZ0bYGb8LZm-Xbc9SqPZgpE5tA_ygQnMfLgPxh6Ww4S_ifYi5K9agpORJsnSDMvMcl05cuWottrPVI0Cnt8Qgy4knlRcmyGdL-IhB0zr_0OMMM-jujjV1steCFo64NtSWdaWjNQGW4HflqgeSIBLAv2et3nspkW6roDir2IoeBNXNYkI_U9Sh56M2sKtHpxPIc8tJ0zAvojCd1lS01g_TtI1J8LjQNsQheERLyJvLPTBvHtG_fU2nxaCDaRwzrLzovqQrNm-t0YjpHppV22DSIRaTKmVdzmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmSpPzX-R9-aVAaXleBO7uAVeu82WzhD1_l3tQF_8yIGocOJijMc-Kx-_liZYROv_Tlz4gwJcjHi8HqfFu1PX-AQv6bGlhQOb5fAcTwlCfh2R2fRl_pAOQrtH9IJkJ6Tq62GtC7t7qFvNvgVsZCLj98-H2va8qo27d0UN2Ilv672c1IL1tO3EkwLabgHGRzNtLVGM5GOzZM-0zClWkJH0XXviKTcppqNvx9kcLFuOIIvnS7u81jyqxgJ02zLcUCvR2xR2GfKosWgclfvT_CCNKnLzw19oZE_hPqRk5h6ngEz1UQGQO5NbLiM5R6Lr7Uu8SFRwN5Rz0OFG-FB7hW4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg6uSVU411osa176fcxxaSlOnLAq-UrQsHoqL7DQDlR61QA-yYFsrPDZ_ZwFr-ByFZKutChrRTOTQ3JBrl5hUKMZE1j5LbsHrEEk7fNsEYf6xt4NJh1iJm1GLv9Pm1VzaTwcRNfUIICMvqKBQpKak8FjCGO0tKR_eApFIVs9846ssj6YBbimJ1OZOkh_tESkHFzvrGH4KbNj61Mcp3pX-1SgiGcNt6GqdbJps9Xbem8odTK5skzdBw5-V8--uJvssp3lrg3jBtPhfN6Q8v7Yh8MyZalOT9SGXZ5RM4_n7UmWvP3s5TFPhqKMk_3GAxTyxLo1MWrdNw-9HyMw1o0PrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni3LaxIzQAOdGjeM5cX-wf0gVrlBGIHAzImH-DC_WrGtun5xEGxNB9wUYY2uoIOxhJtwgeyZ1cr1AEn4R0hbkd9Vbxb-6qh79_eXXJGvKpWk31ZtAlIt1Y4NMnUjjOaZEaMer3u4GuZwXrOOl8SaKYByPToae3E-SfLbAOUSlW9gYryvKAIUqaTvZVHuPOOt2elKu-MIA87-x2_NwZEdnXsVNSTTASXkQp1RsHQzKMDaJOPArJ3ydC7EysC2g2Rt1uEJnHGOWGnjxDCsDWHO8JPzM2C02hOIwtV-tnYCWxrTnEF_UQzq3-yVYdixMeHU3BYTziK4QTLFPTNukkHaTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=ncLZM92xOERKgCRRBgnPp6vqni-H1DQshhj9Jkvaia4Qf4-TLh6Yk_sc18BAyE9XL0Na4IqDVbtEcKA6Vx7xn770VvzWoNZTStck0egKYZy8NlGdgz9Nqv8cwYVglQ7HzheBLLI2zG_s7PBxZwdEZDCRSEmKOoPVr34U9Huk3-2Yk070zfyhyafoKfEF8RjtoqBE9Bi6lGDHn4wkP9hmCZjDrnpktB66Tmn1EdvcCVeDKWX3ZDTPBBZ24Tbz6STV4ORPTQyp7nR8Tow6n2bf0Gt-pjl87D9rKUiB-qyGnEtl1zYZWETHaK-a5n1EDe0gUnT4FmSdrWOh0V0F6Upecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=ncLZM92xOERKgCRRBgnPp6vqni-H1DQshhj9Jkvaia4Qf4-TLh6Yk_sc18BAyE9XL0Na4IqDVbtEcKA6Vx7xn770VvzWoNZTStck0egKYZy8NlGdgz9Nqv8cwYVglQ7HzheBLLI2zG_s7PBxZwdEZDCRSEmKOoPVr34U9Huk3-2Yk070zfyhyafoKfEF8RjtoqBE9Bi6lGDHn4wkP9hmCZjDrnpktB66Tmn1EdvcCVeDKWX3ZDTPBBZ24Tbz6STV4ORPTQyp7nR8Tow6n2bf0Gt-pjl87D9rKUiB-qyGnEtl1zYZWETHaK-a5n1EDe0gUnT4FmSdrWOh0V0F6Upecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQh9iBNgyz_NsonU1iRzz5rYEi6iYU_JGMUiI2O70_IfBSjSgGoc7qBBVbe0MQw43ajxVOX5OJMpcMA_RkWWmGwLTQFCYF9KvY2854qDLnYHUTsI0JApg4BnzjeIlQ6TDl6KbLDGGYMnvoXI1Y1cU80k8CmF1wygDoIcVvYiqj70GbKWlBj7-kFIUM_-sRcBFK7ZUC4j22RRHUWCj3IiJjLTYUMsKpt_TF7zqorXxD4N0jveX9lGpz6KMpufXZ-dO39ZxZOxMsqxUNk6j-3psv8k0frdLNCxwFqpKAVsd_2WgoH1MuRYQvcx5MsdCJjcZz3Nbtod8_ROTCyX18RHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKuAYx-i2ODrXCemJPbxDJ-iOKLAcY543bzbe8ijAGFWpf8dtg5d-YaDsunIct2xLSLeGPJwCLThV2CFDLmiUnyTIW93m7GF76wRam5-5o0CVZSbjpJvLHJhwsXoQKohZI16SPBQuQiCPMyN_AyhuWQNSFfDTSGLw_1_saUmc1EtekTbalr8uuN-X4mQPpyBfLF64Phgws51lTx8mIl_34glCNUPVwJCQqewyMLssiugQaD5fSAZ4VFHpSs53zsbVA1lO-09pddkvI218s_pTJ4nfkb7uTd2NyZOqPA2eo-ntNRY4YyaWMldZudhjsEQm9ZI_5Du3e397NQdJxCAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
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
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9Qv10MlPc9US2F-5pP13INCo8PKDCuVZL3HWl-7Hbra3FnB85253A3dZgf4BvHYQN8OhcUBydK75_6tJMtjl8qzsR2S9VVQKcv96QMwE73hAgr0nNzPI3mFVig5JoF2ueGnEnkOs59GrwCiXPZxX79qRPNr_W8UZWwcXH-UOmUa9tBizOzSObnVhObTxuLFGjJj43-39OOqjWQXAq-mCopqdNMFsQsV4VcwvIcQQIc2r33aThMUYT3W7ah1aN903Ylv9johBv2bJA8eqnSCfdvAmIzoafL31kZXZfNv2_SRe7LgkolhobwCX5pzNasrwuo4bzx5T3mJmWAr3oeIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGYQweAjXaeTlG1SqnAF2xOHRshuAuo9nba-NoUB-HR2eaERPxsqKiJiyHbiKXtpQzrV5UbFXhAJf1ZvxrYz4x4wkM9jYp6KnlO2VyBJl2V6UpGEDXAfje2eu5m9L7SnY_f7qRl4lN7CuucY2RppASKGdhPBgVb7xE56ngypFTLPYCInPio_wHk5wbpwrUBilUcKqLYGvc07rN9Sg6uJWZKybl-gPRoO82rcJygOhbdP9w7roqC7agmccjY8uocdZWCqhZg1YKSCxneTz2teEcVRFBEFVFTEdBFuDOgrBVwX1iq_bDtk5jeQ7Jt_U-Q_Stti0y4-8qvh_gU70dhNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=JRW05S9wuKpKlzu6xrne8eR-IBqKvM5TilS9ehDfpj3pQDqkObbu_dMIp640crFwRofduhmlZGH7M6zHSwDUYl6kq1LtCVNxx7bYRFQgwsgdpeKcdOwS-gfClCWHZXFetgrynzCQwsPiTDLM_1GvA2gty6YUqDgBLLEzLqXqTt9QOgCR_i6jYNlq7GZ1ximldisRJLn4dH_wflRSXj8ZZIeN7T8SlXptFuBEsq7WIV928c-W0ta-u_u_f9kQEPFIB4iWqKs7S15p-D0E6kafALsdb3j9laznRZrUCkTRpbc50uPhcz6WQxVaonGFCCZ1vQBoW0dYYDGrj1U7TmRq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=JRW05S9wuKpKlzu6xrne8eR-IBqKvM5TilS9ehDfpj3pQDqkObbu_dMIp640crFwRofduhmlZGH7M6zHSwDUYl6kq1LtCVNxx7bYRFQgwsgdpeKcdOwS-gfClCWHZXFetgrynzCQwsPiTDLM_1GvA2gty6YUqDgBLLEzLqXqTt9QOgCR_i6jYNlq7GZ1ximldisRJLn4dH_wflRSXj8ZZIeN7T8SlXptFuBEsq7WIV928c-W0ta-u_u_f9kQEPFIB4iWqKs7S15p-D0E6kafALsdb3j9laznRZrUCkTRpbc50uPhcz6WQxVaonGFCCZ1vQBoW0dYYDGrj1U7TmRq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=MzbXRNDFVzMzzYLcJYMbB5q4z8II_cGcAOzeaQegdANMWTYqq4LyBvQg22HL3nHZFRknYQWA8Rlyr3mJEbqi5dCM2Ns-rU9jf2AGAm0becKiRDe0E-9NR6yceA_ufZ2EVFgPZqXZ0i_ySgchwQgr_VOqN_DRUSSynObk37DRnc1BxZJLvLzek5yLRF25-QksdpesyqMyT9pmqNO7YBCB0Cs9pfnsna1CLVThc3Z1NnHNFM2IkcBaQixu0esWjVJViXhXoRZfYHVXxjGZefHS0rYst-IXeJHufDll-i3Ise9_ZY8Q0vVyWI4pMRGKf747gJEdkmKvedPN9SsaW357Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=MzbXRNDFVzMzzYLcJYMbB5q4z8II_cGcAOzeaQegdANMWTYqq4LyBvQg22HL3nHZFRknYQWA8Rlyr3mJEbqi5dCM2Ns-rU9jf2AGAm0becKiRDe0E-9NR6yceA_ufZ2EVFgPZqXZ0i_ySgchwQgr_VOqN_DRUSSynObk37DRnc1BxZJLvLzek5yLRF25-QksdpesyqMyT9pmqNO7YBCB0Cs9pfnsna1CLVThc3Z1NnHNFM2IkcBaQixu0esWjVJViXhXoRZfYHVXxjGZefHS0rYst-IXeJHufDll-i3Ise9_ZY8Q0vVyWI4pMRGKf747gJEdkmKvedPN9SsaW357Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kftPMmqu5IrKSpJL9_fV1eDhXatKQOUqEAFNW32q1CYR79ja-UXIpsaWN_Yue6TYjyeoJ-qzeXFWXtLO9Jv4OgdR--hb3OdqvW9RMIGzbyAEhITOT9QPjFbANeNoe5ZkY7e3g07DGPgrGbdwNSfAvzl1B_jTWnTHcJTKrH85I5jwWavylAbdMB_-y6TXAmESHMTnSVAHgbbXmHBJAorzw1lpH7NTae5jGWWFeVFup3Aib0E1RDQ06MM2vKthdrf8EN0mWrZyZG8x0C0yiCNvXSQZUuwypCTfHTbQ5xK1HGwoXsuqnWR71N3uuAWX-EdVYTE5-K_91xv5WfK-_C_vpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=sygwURltoBpdAYdhbQRYIYuFS2xC0MUoDAveMMrMoreZ48iC28AEbrrqYReML7yOotaIzUEb8tXWu4C8kh2cY1i1NXxQER0t5ZigpuT1EqblVN9kIgjG2Z1ArUf7uCMe4cxxbwh11XfRZyYV1quazq6kGQKtaxDocu-K4-c2aUrOUxxFA5WfimBWvNj5PFt4-ZhXXX4Hi1iPCmJzE8Yfow0AiLl4Nq0lv18k4HGZ62JG_L8tqvudaQJgCFHd2NhYoWyMvlvZkWEgJINv-BjOMOAuvdwmTwtemgiAht6zBb2fc7ePMImCYLYRWps49tNDQfRMp1ujT6CkXfNpiTJN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=sygwURltoBpdAYdhbQRYIYuFS2xC0MUoDAveMMrMoreZ48iC28AEbrrqYReML7yOotaIzUEb8tXWu4C8kh2cY1i1NXxQER0t5ZigpuT1EqblVN9kIgjG2Z1ArUf7uCMe4cxxbwh11XfRZyYV1quazq6kGQKtaxDocu-K4-c2aUrOUxxFA5WfimBWvNj5PFt4-ZhXXX4Hi1iPCmJzE8Yfow0AiLl4Nq0lv18k4HGZ62JG_L8tqvudaQJgCFHd2NhYoWyMvlvZkWEgJINv-BjOMOAuvdwmTwtemgiAht6zBb2fc7ePMImCYLYRWps49tNDQfRMp1ujT6CkXfNpiTJN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=dq9yL72hf4aq5FMtriK4DoEf6Fg4dQC_Vq06Q1oxxiVPBmp1HuRsdXnTrxqF0djHbOiFV0Qpi8osuAAJ0OVaK7elsu-Je5INRMexdHYp6NJj30rxiWt5noJGyeZBnY3V26rWzBBWkfHvLbLaUv7NkuSPxD4TG0udvVEn_PS_IVSfyOlWI8XUhjrrR0tSaBqx-YIbQNNbWBDwDJtp9vxy18LKCgRb6Uw8a28Gd04uzfdFsFOT0R1gYqbMpvNUi1hCz0coFBhHN_vV0agOeRWfg7eZvF8M6_BipAz0qz3p-eo3zCK6diUmDCaWdk3hBFI3CHqXL-VOq7w1fW88FnYsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=dq9yL72hf4aq5FMtriK4DoEf6Fg4dQC_Vq06Q1oxxiVPBmp1HuRsdXnTrxqF0djHbOiFV0Qpi8osuAAJ0OVaK7elsu-Je5INRMexdHYp6NJj30rxiWt5noJGyeZBnY3V26rWzBBWkfHvLbLaUv7NkuSPxD4TG0udvVEn_PS_IVSfyOlWI8XUhjrrR0tSaBqx-YIbQNNbWBDwDJtp9vxy18LKCgRb6Uw8a28Gd04uzfdFsFOT0R1gYqbMpvNUi1hCz0coFBhHN_vV0agOeRWfg7eZvF8M6_BipAz0qz3p-eo3zCK6diUmDCaWdk3hBFI3CHqXL-VOq7w1fW88FnYsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=txzXFm3r3TJePOkfF6flUb90YuYQJEZG2wC15Iawo9cAo9C_aZjrVmWXiWUHtUPbzV2ii_pZqxeunEBK_4azso6BfX4-gpSuRV8QLMnFn2O4_BA6EpKEsWsWhjN0qLZkiLGrkp-cjuIH7sbyLBqSoLmoStxTOc6FKMatOuBwSZdLY8UVOietFUmSfugNBK0lOqyU72v0adFsvugPc2WJpxQGZfIXm7po2Qg3xa1RNnERJpD7yg8aBoc79DoF-eycQHwJLQ3gwVC_wtRYyiJMqa2LiYpqHuN6GI_WT6qArp_jGrXmOa7fBAOwWG6ACVvCsDMDvHtdz71Nx2ls4yVsbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=txzXFm3r3TJePOkfF6flUb90YuYQJEZG2wC15Iawo9cAo9C_aZjrVmWXiWUHtUPbzV2ii_pZqxeunEBK_4azso6BfX4-gpSuRV8QLMnFn2O4_BA6EpKEsWsWhjN0qLZkiLGrkp-cjuIH7sbyLBqSoLmoStxTOc6FKMatOuBwSZdLY8UVOietFUmSfugNBK0lOqyU72v0adFsvugPc2WJpxQGZfIXm7po2Qg3xa1RNnERJpD7yg8aBoc79DoF-eycQHwJLQ3gwVC_wtRYyiJMqa2LiYpqHuN6GI_WT6qArp_jGrXmOa7fBAOwWG6ACVvCsDMDvHtdz71Nx2ls4yVsbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDaxkIrgbShGun2awg5uukoCivbuSCC4UKxNjjemfyO21jyJc3vMIr6V0rYOkoHzOrFpDIYcWX9LPQOPZ6w8nP285DKunVMHWErSvsC-hWBQnOUtvMLdmPU7tA1lEt66nrtNi3BgBRgfD7ozP0YTy5nYj40ItCSThuM5PHAkwZj-Djk7fSmzHFt-ivkOsN830b-FBUPg0xHukuGoL5LoeeqhBJc82MF7Ttbcv1tAL0QcIlqKcTy00RUmUl7AwTz2gUykIyFiOn9L485uR1JFGiD4Eywsspa6798QVu5zs0gdlrpprCjuQAXastydvgtOUdqGeS0fldrW1Hz771d2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qf9e7fwXE8zYuxZ41Mbs0gnXw4w5uyKG6y4kJ9FWfMLrayHp4HfrMGdBliUBBWrNqh7dntThp9PXtJEQcHFinjI7B9EYEAez61KUD1P70v0HeyVWnuEaRkNzX02uhArkZV5PSyR3Ey7jCRKC3BYYNWAPnVPe8Tp2UcYxo8dk2DadhLfqf2BWnOPEaEMHZCRfA1iffS_qSF3VM3UTZgZCAjsU0ZKVUO6zRtWn2QWi0nYsBFnqTAf1vcvNKsiEmzoNpkR3daFVKFns_YfTi9wjijvVhlkcS-u_kTaY_oFa75baakcaS9Q5IMmP-7eHoGc7710nqwnBUJHBKbDIANl2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfkqR3JHGp2X2SrSD3n1Q7V6N1dGdmo87lbrX-VrdjKbgGTXVdi0GHZ6uW2j6P6le9vpRw_7xQBQ7HxM0zChm2XlLL4FRG1wcWJZfVjzc0dmjuF8389JcINpB-hFuPgenPARWYru9pUOh8ECEIZeM6l5j4G55n4cGf_xyiet3RWgfKOy4K9jmAdlS90NNQIAGbE2LTx394d5Je4cQZl5CYWx8qf_qmZ9d0eqMpIsOMA4CPaM1FHvd99iKKGmfSg9JP6usbo-zMjSXH_vMLixGgoALO3xhBnOAF55Gd2FD1kI_PQqvCTb_UfCwXymCGueB9fhjaa-JorTMEZGmGOuWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZw0qkmeSlx-qZrYCBIowpKXscbs4zP0RGvP8wq8uCEE5R82sAZfhGdjQ49CCKhVd81uOTdumFXIHwx_i_8Yfuo1s0ShXSBniYkqaLukP0Nq-s0ZFV54wloEdu7isH4mEPzOdU0OLW4prormIa3q0Sl_t3y-7Mxs39EGNoywfvLuaFr3tbsFDL_Do_l2YGH4IPayuW2PQUjQJxGdw-8_bJ0FgV44VvkwjuKi14-QlBPMdFT0V-47mFdZi79oVdYVIgz5Ftdd5HAXma6ogBqFWdtaMFUaB6jNJvikEphjPtOdiF710OqHuS0_M9g36SwStm60_K64jNaA6wJsDPYK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZzjGBhYGg7YIvB2sWsbLbZ3xVBPhxcJBZgwhF9h0Ylu9XuNp5zRWHrje-XzmQGeoDzh8ffeeUAPj-X9pYTaj2YNI6LNugZacskxCkhpPrtKfiFsdfBYuhK_zozv2QruT3rqb5g_elSnN5rBn3ryRIeenoQz8jDBqhXaaNyxyjwQDra5TX5BYpIptzcvKz3TlQSjk9djWHy8olb_9mQZYtLeq9nFiNsty9oKnlm3fYlqZgTpJ3TZxYNw2pw30fZWGZBZsCD6bOou33zwQPMWRaJ_fNok290bP42VOTjLu04iYH_66LgqvmkcAltWhTWd5A8UhCCtlskirtfhg8bskA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsJDUNwwUbZ0-4qTs46cbioeWMNa8oa5R5dMquKn89KrzmLzOat73kjBCWClVURlLbnTe_HDlrz6izShv9ZgW5LNLmH6h4qh44mB_pg768KeeisYR-3aOd5InVAlUFvwLATWa79aXVhYNi6uD6zvRUivy_dE9YOBFXKqzS3bM8vRm3PJLyrHKyJ7TgsXSzkOnonhtGAK4Pufp-vC-KfDkmfq1s4y3jjsWFVCG0wynLs0bAzzm17dQ7CRp1HToYCiwkKckUkBv_I2SDuanWC-r-KbgRgrqEQth327v5_TV1iHdgOi14fWJB7PZfejxDTaZqCk6vQohBIeN6LmRKed3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=DSEbHQyszhY6vX_2-x1Phfkx-LeLwUiAy384PU8mfvukWr9muKfuUzPi7DkiFKNUJK2Kx6_aTts3FQJt2t3tj46hmV0zBQxEeRPfnl4Ci0A7phnRRaYBefG4LYzrFoLh21_Y5XfWAMI3qzaqfxC8ry1UAey3k-PkhgE_9pBX5ayy__qCpk2JQdaYV57puyoHm_3KUc4Q8DxQVSU8zF8cszTzW6x6AahPUwu-9obUVXFt6KRb9Qfy_BnrQlPNAwHEMPLqbsXWts3bJJDzDZtrXAapuvOt5PwjWGUsdVHXFdEx6FC6eoVEWjMsDwlhY3TougxWLZrZJORV_hv-55WMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=DSEbHQyszhY6vX_2-x1Phfkx-LeLwUiAy384PU8mfvukWr9muKfuUzPi7DkiFKNUJK2Kx6_aTts3FQJt2t3tj46hmV0zBQxEeRPfnl4Ci0A7phnRRaYBefG4LYzrFoLh21_Y5XfWAMI3qzaqfxC8ry1UAey3k-PkhgE_9pBX5ayy__qCpk2JQdaYV57puyoHm_3KUc4Q8DxQVSU8zF8cszTzW6x6AahPUwu-9obUVXFt6KRb9Qfy_BnrQlPNAwHEMPLqbsXWts3bJJDzDZtrXAapuvOt5PwjWGUsdVHXFdEx6FC6eoVEWjMsDwlhY3TougxWLZrZJORV_hv-55WMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=YGYgVyLN4aTuB1wS73C3Bn1aA8G2JoKVVEjtlI8pHjXv-ShvE3AsIjS9HvdtO04aa6BxQIJ62DUup_2UGBQpq50LOroCvBS1eKmtsGzRhZV8bW-ZMqltMIZuiS688JjLRHcHLIUiVayp0_gX6spsuMvHDG4uje4HrQjGCy5FSwa4Ougzek3axoDNwqaNUp3teKrz8bsavY4GYvnY4DLKCYEQREe20iOoinwg6OypXxGRdrSToAw5-UoLzYokbLWqz-q1scqT0rb1eW14O--GDR4qRMtatYsdXYYr0quT4WsYERjI4aKcUonrCHCjz0tGx6dbTiTQAvVP-Yl_eGJ7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=YGYgVyLN4aTuB1wS73C3Bn1aA8G2JoKVVEjtlI8pHjXv-ShvE3AsIjS9HvdtO04aa6BxQIJ62DUup_2UGBQpq50LOroCvBS1eKmtsGzRhZV8bW-ZMqltMIZuiS688JjLRHcHLIUiVayp0_gX6spsuMvHDG4uje4HrQjGCy5FSwa4Ougzek3axoDNwqaNUp3teKrz8bsavY4GYvnY4DLKCYEQREe20iOoinwg6OypXxGRdrSToAw5-UoLzYokbLWqz-q1scqT0rb1eW14O--GDR4qRMtatYsdXYYr0quT4WsYERjI4aKcUonrCHCjz0tGx6dbTiTQAvVP-Yl_eGJ7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=SEtmuaGqm2jXYVy96GwSH2VoyMohIEPt8rkm74nh5L4Y-099T_exYO4AzFtdlwa1EF7ToNvRGWWWzNh1oI5LrMWH1KTOjAPTsDderRv1DOQgx4bWXxLq82G_2-OCKfx0cJCtspopbJeChbwfpFcD5xDG0-fjS-KBt2pfI8E8yrY0u7oFXrqAMY08ekVn4qpBMhK-AZ01UNaROnLbq1_7gp4l-VChoVxrMGpGa67L-UmUmlsdXKcz5S9wRyTYDHvma4YxSfsbOh7FpArIs_CwXE28vpombXJso9m7-D3qrWQrG7LVbiytFLRdq0i_s_IIl-wmlIOh2LsA9K5rgFm5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=SEtmuaGqm2jXYVy96GwSH2VoyMohIEPt8rkm74nh5L4Y-099T_exYO4AzFtdlwa1EF7ToNvRGWWWzNh1oI5LrMWH1KTOjAPTsDderRv1DOQgx4bWXxLq82G_2-OCKfx0cJCtspopbJeChbwfpFcD5xDG0-fjS-KBt2pfI8E8yrY0u7oFXrqAMY08ekVn4qpBMhK-AZ01UNaROnLbq1_7gp4l-VChoVxrMGpGa67L-UmUmlsdXKcz5S9wRyTYDHvma4YxSfsbOh7FpArIs_CwXE28vpombXJso9m7-D3qrWQrG7LVbiytFLRdq0i_s_IIl-wmlIOh2LsA9K5rgFm5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=ZAVsia117V4OdDvdZOJwAUSTwSOsOZ7awM8aT6MjJNxC4qu9_3C9gbriLrePTY_E2bW-2e5nttLO38Ez4Wsxyh0AfEZgbaYyIxb7G9mjMc4jAODDsxS3xaVfba6f-kl2Bh7v7FA1g-it630JiW2pOAD74qzh_APCWh5J7TEU_Lhs9b1IKfjspAmRRI87dHcgutuETnQOC2v9fQJ6NcJp5pM79lbCGuV10t4huYMgIWtrz3GA0_ZCzXa7kM2g5PaUGpdT75ia3qVRka5yKUQHbDqhLGrs2xaAWkQB_VOpGP-OFsKdg-UBlYoAP-CxCI5XL4yb4Efz9MpWIa4awNzjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=ZAVsia117V4OdDvdZOJwAUSTwSOsOZ7awM8aT6MjJNxC4qu9_3C9gbriLrePTY_E2bW-2e5nttLO38Ez4Wsxyh0AfEZgbaYyIxb7G9mjMc4jAODDsxS3xaVfba6f-kl2Bh7v7FA1g-it630JiW2pOAD74qzh_APCWh5J7TEU_Lhs9b1IKfjspAmRRI87dHcgutuETnQOC2v9fQJ6NcJp5pM79lbCGuV10t4huYMgIWtrz3GA0_ZCzXa7kM2g5PaUGpdT75ia3qVRka5yKUQHbDqhLGrs2xaAWkQB_VOpGP-OFsKdg-UBlYoAP-CxCI5XL4yb4Efz9MpWIa4awNzjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=HBqsDuV0ipXzlH9vQWMD9JkeUuoTZFlPLssbsDZOYYems-MgJSEaYAikz_XgnUQ9CUnbI87QTt7wgxlb0axoq3j_Nn-pBPq2mGwH0I5ivWWXoUAbu2dlKV2jwOtUKpHg2WhsZ4ZhjDoS9rH6o8QlnmTYG7vMUKuExWS3HF_jXZZOMv3ebUgDIxo8eL7A9skJyY04evr1YzXzJYr6z1wPgs0XncLDi9dmpieS109TyKm3HYRJUktvWQrE5moaPlizJqyoVMt_D8C2bnpLCHF86cB8Rgl8HrT5JjpjVzTtE9K3L8HMm61-EemwIomHzfjIi57DBm5dXF8GWZLYigep7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=HBqsDuV0ipXzlH9vQWMD9JkeUuoTZFlPLssbsDZOYYems-MgJSEaYAikz_XgnUQ9CUnbI87QTt7wgxlb0axoq3j_Nn-pBPq2mGwH0I5ivWWXoUAbu2dlKV2jwOtUKpHg2WhsZ4ZhjDoS9rH6o8QlnmTYG7vMUKuExWS3HF_jXZZOMv3ebUgDIxo8eL7A9skJyY04evr1YzXzJYr6z1wPgs0XncLDi9dmpieS109TyKm3HYRJUktvWQrE5moaPlizJqyoVMt_D8C2bnpLCHF86cB8Rgl8HrT5JjpjVzTtE9K3L8HMm61-EemwIomHzfjIi57DBm5dXF8GWZLYigep7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ivmW5ASErq5BFBWG9o0JgxiXWx3L60RixyMa_hMldJojP2Q8dLugsLgRKlPXFd-SboqUMPOgcE6Xxhj54kmJHpOeRIPX1pI2uS6nT33RBEjYXuwSmym7UUpDwYjW5Ewu5a8u5oLa61DtM0ptO_Vu3BKgv9Pn0TW65zFctFIciai0n0QZ9T6nlCIapRCHiW05EXABeMnPI639N_mK384zy_dV9yIyyRfQkiQH4dpU8LG65yPiwZ2Ie7ifW1DIwLm6gWLTepMoeyV6Ft5V2gBQrAc4BgK-T1zxJK9N6kGci6_NGMqqnV-A_BgaG0ciTuC5CAA4OqDHMpz3nkXwQ2IIrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=ivmW5ASErq5BFBWG9o0JgxiXWx3L60RixyMa_hMldJojP2Q8dLugsLgRKlPXFd-SboqUMPOgcE6Xxhj54kmJHpOeRIPX1pI2uS6nT33RBEjYXuwSmym7UUpDwYjW5Ewu5a8u5oLa61DtM0ptO_Vu3BKgv9Pn0TW65zFctFIciai0n0QZ9T6nlCIapRCHiW05EXABeMnPI639N_mK384zy_dV9yIyyRfQkiQH4dpU8LG65yPiwZ2Ie7ifW1DIwLm6gWLTepMoeyV6Ft5V2gBQrAc4BgK-T1zxJK9N6kGci6_NGMqqnV-A_BgaG0ciTuC5CAA4OqDHMpz3nkXwQ2IIrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X64LUNVltPlu7gLpDCMVbqp3w0YK23diF1mjFxjbrCsCIzVipX4f_diu4omLuZEMRWdxkDJTe3BnrZm24plso2FUfAXnALlnQprO6jOs72l0gacrS7DegcX6sCGxc0P2QA9zLFzFlTSMlT2kfeNntYRXuM1hjeMz8f2K2RrGkBQRWXVg_-B1DJl1UnRdl4E-v9RZNHhi_4ponOpZ6U7UHXrFnsl5xC2HYBokQWr8oINfhwVFlOszCkuoOg_giNjUQ9w2hGqZzVV08HwjpzmbGlePO0jI4JrxayjUhnjIhcNwXjpC6KaieRoV16u39iXWy2wqpG99TgvhSw08jRw3Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=BzlAhTizzRENEW-idM6aPCoh7bp4wSQQX3hRd_kTe-r4qYI4qTdnsmFxbnRvqNyL6DVO1JNuY6C-XF2oGxkIVkFb1egBtSQvXKRqJl7_OCWkp8163dISnUNsYFhm4ckbPswuXSfhsWP-F5SJpM7JODpIC1H1n-SD4A5qURbq2kBoAU6NF4OhAv0u_Jm1Zp5tGAQ2NN4ccHEhO_WVEGaXrlyzEZKF1GHs117TOpNydYeC_71hyz25yETb808hN5ARVA617B8oB3mNRhrWr7DTRPuLcQngGEtySLGYqek9Mbe6GJKM_gsZMPJ4_xe7pcusmX_zv4PeXUQDDF1qEHRBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=BzlAhTizzRENEW-idM6aPCoh7bp4wSQQX3hRd_kTe-r4qYI4qTdnsmFxbnRvqNyL6DVO1JNuY6C-XF2oGxkIVkFb1egBtSQvXKRqJl7_OCWkp8163dISnUNsYFhm4ckbPswuXSfhsWP-F5SJpM7JODpIC1H1n-SD4A5qURbq2kBoAU6NF4OhAv0u_Jm1Zp5tGAQ2NN4ccHEhO_WVEGaXrlyzEZKF1GHs117TOpNydYeC_71hyz25yETb808hN5ARVA617B8oB3mNRhrWr7DTRPuLcQngGEtySLGYqek9Mbe6GJKM_gsZMPJ4_xe7pcusmX_zv4PeXUQDDF1qEHRBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=T3qd8kT_U5T9ABpD8TRoGCUtetp7z7Q_QP07A90uM3Bswn4oDdrUJehzxiqiCqGZqkAgw0PxFCBw_N5mAEFW19CFPdEVsctv78chzozQQUCdDlsIYBriFii6FP81hKhgxU3XCbiJbitqyk-e5Pv_q9OWDYhvQvvNTQkfEttNS116w-a98tclv3QQUggENM5drAu7kb3CTba9rr-UqyG1nabIGmMlE8vGR3AsPU3DnUYuRHOO707LkBVBUVdPMpJn2ZNHOlZ56YiwLxF7StQgJdPYRRJ1eZIq8K6XOqlxlhGQcSsEAQue6Evv9WxKe-vNds3X6Grck2c9je0K0XuOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=T3qd8kT_U5T9ABpD8TRoGCUtetp7z7Q_QP07A90uM3Bswn4oDdrUJehzxiqiCqGZqkAgw0PxFCBw_N5mAEFW19CFPdEVsctv78chzozQQUCdDlsIYBriFii6FP81hKhgxU3XCbiJbitqyk-e5Pv_q9OWDYhvQvvNTQkfEttNS116w-a98tclv3QQUggENM5drAu7kb3CTba9rr-UqyG1nabIGmMlE8vGR3AsPU3DnUYuRHOO707LkBVBUVdPMpJn2ZNHOlZ56YiwLxF7StQgJdPYRRJ1eZIq8K6XOqlxlhGQcSsEAQue6Evv9WxKe-vNds3X6Grck2c9je0K0XuOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7BvmiiaKPuX5o3KIJGn5QpFIIr-mk9zne2x5VqD1jjjhTYlRsVhTexZoy_33Q1FLrHDUi3FYLMkBHsSjb9kedg8-NKmMo_RWzM61GeqoIFmHzh9ELr2qjPTsHOBiHUgs783JeSdBC5yiUu1_1tuI3y45cRpjer-BFGzTv8UDjKbqg--9X3sbJCcIUaEVPHWd0J79-m69H19rdNEA0CoLfeUlSAiVlgvCs2M9ee2UTeWEtkchnnHLh8JU0arKqwNPBxdfbPkk2RiGcT_se5WTTmeoYPJaofGiHARfa0mmxDgmcA9TgutpxW-I492T15H2ZGt6Q0LFehvP6JEigUKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
