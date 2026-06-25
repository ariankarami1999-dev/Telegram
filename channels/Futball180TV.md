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
<img src="https://cdn5.telesco.pe/file/sP7IuOnoEyfCSWWMsQho6qEvmTbDcEeMrfmZwXgQJSs_rOi7UgDa6MgtI-aqFPlMFcmOIVdyjf7EFfVJMZ3H_-xSkjEwIoNpoqKSL-ccuWUSSNnJgfitez3v1K4RP0XOKB4qMmwn1wTJak6wrMXzcBpNrgC6sNKky-9kY5b4qKVwqKm09TNFCziG9xpaF27MhLZKcwd--1UOqBTeMawzoZ4l9p0d1hT8_wjBb3JExjY0UvIsyR6AD9TG1NDWLBovrR0N1jtcH_mDAI_wpR4WgykxR7Fiqu1RU1DsxC8aguQi-Xw35qMf2dlioaFqt7uNEny0ITcsuDVvvWMe5SWbHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 700K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-95890">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009dc59e9d.mp4?token=bKM8OtEKUm2ranBwhfC8MLhx038I3aZgSPp4mas4j8grmFqJLU-eV-u99V0Yx8iwZvY7hlAFhmFoERbwdDDsyKhskGncKkLvKIIelYiK7HJJ-d7cq9drqK9Hud0D1jd4CbvqbNcY1rXMsSaiI_OUz7Iv0NQgMZdthukzgqu0ig64qlyevywD4A94ezbPynqhfkHimIL5p5IzeS6OVqeeSqY4ygHxin1gDpaTs-udNPsDFGdHFV5tIIrwjUwIv3LV4BSiw726tKG4xSaqQxDyUwALrNfP4Xo1QduD1uAvvF8a8JOfMXptbfW0WhRKpOQmGmHLkOPo0DiTy2W6Y6QNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009dc59e9d.mp4?token=bKM8OtEKUm2ranBwhfC8MLhx038I3aZgSPp4mas4j8grmFqJLU-eV-u99V0Yx8iwZvY7hlAFhmFoERbwdDDsyKhskGncKkLvKIIelYiK7HJJ-d7cq9drqK9Hud0D1jd4CbvqbNcY1rXMsSaiI_OUz7Iv0NQgMZdthukzgqu0ig64qlyevywD4A94ezbPynqhfkHimIL5p5IzeS6OVqeeSqY4ygHxin1gDpaTs-udNPsDFGdHFV5tIIrwjUwIv3LV4BSiw726tKG4xSaqQxDyUwALrNfP4Xo1QduD1uAvvF8a8JOfMXptbfW0WhRKpOQmGmHLkOPo0DiTy2W6Y6QNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای هلند قبل بازی با تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/95890" target="_blank">📅 21:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95889">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqjoU5mNaSLH2MMAjIYEKyRvx-hn9Tcxb41ILGFdH5fJroFDtMy2VUHVaWcSwHpdxNcboetY4PN0rPpUOrRAKt9BPJXeYL6qA7rd91O1k6vF28bAJDbkg5pRJ1xWlsmnNMXJL1vNUeeHJQo3h5QUV9hXlhKa5C5_RG-V4mPWGaJZfU4625nQ58UmjSeu4A4Lo7Ix9cwC-a-pyVshYjrMeDAG3_EvTMPyXz0MjNQE-T3_0sCdMEpCCGPoA7VR_Xafzl9BBTmKQ_uLXnvayLqhbzDyqn9NUCv3bVAJU9aQEnWCoN3DuSCZPVXxfmfO0WOLklosQu2WtCMliIyjxCrgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇿
❌
پاتریک‌شیک مهاجم تیم‌ملی جمهوری‌چک بعد حذف از جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/95889" target="_blank">📅 21:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95888">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCEfEZ305v2Aq_pT1mQK5UcWL13jDT9IooRG8BVXweqg0ClC-WYbhWnFqkh59TU3XOUTdTxLn8wqiSmRgzPI0YHZ3gqni-TO62mCTmYNt1iVUaDWrtlnQtOfNU-0RsqrDm7_7EDpuf4brycu9jOMEc0adGHHyqbFTi6i4VdU-CW6cd6do0AqCnTuP9NbdvPWtri7URWkDDP95ByIehbG5dy13NAp8BZYVwEY-Bi0pot-WDCzgdRoi43A0m-d6cvUBeIhRUitQq6gNyg_BhewzEiz_55fpur2YQPZ6eOAwr8hPjyCsJ8-cbRiTrbKqvPrqcpNh2fAwLjtyMFnj8b8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه هوادار به یامال کمربند قهرمانی WWE هدیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/95888" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95887">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWgKeWviS23LM65DdQRr8BQjy674GM-2RjLAvLnHHre-aau3RCsa02HH2FfaVFZzMcqibTb110qfbVoAfi2YS0ZD4mwHUUaxFRy6D6EAEM4JbA6qF906m0kPB-QX-_vci6or5WCRDo-UytGxG-JXoxONCWycsY1-Jg3rQ5iHbMiJooVDdVxnFcDOmnP0-aNZFjkKzuaO0kCDWEZF4sKzx7ldGqOSIMaOQEeu2hIk3QohueGV0H8ISMQN8oPCt33VsWniqqq87cytQmTvcVYY10DpR0K3lAsspz-xsuaUNDJfD-oO7kUaRvdEWI4ZboerjoF8sCc1FUx6jYpIePMYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇨
🆚
🇩🇪
🗓️
۴ تیر
⏰
۲۳:۳۰
اکوادور
🆚
آلمان
📌
آلمانِ صعود کرده در نبرد مرگ و زندگی اکوادور؟
جایی که یک مدعی قدرتمند برای حفظ روند کامل پیروزی‌ها وارد میدان می‌شود و تیمی دیگر برای آخرین شانس صعود می‌جنگد.
⚽
🔥
آلمان، که با دو برد متوالی صعودش به مرحله بعد را قطعی کرده، حالا با خیالی آسوده اما با هدف قدرت‌نمایی وارد این مسابقه می‌شود تا جایگاه خود را به عنوان یکی از مدعیان اصلی تثبیت کند در مقابل
اکوادور، که با تنها یک امتیاز در وضعیت سختی قرار دارد، می‌داند این بازی حکم مرگ و زندگی دارد و برای زنده نگه داشتن امیدهای صعود، فقط یک گزینه دارد: پیروزی.
🚀
⚡️
آیا آلمان به روند بردهایش ادامه می‌دهد؟
یا اکوادور یکی از غافلگیری‌های بزرگ این گروه را رقم می‌زند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/95887" target="_blank">📅 21:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95886">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgwxl4j2nZwBbbNdqcZWmEguXMWP5sAwmOkB413oC5qNkl3YqAVsyfyF0Z5O6kFuQ-y2kvPFYM2Aq6yi6-JJsjmR1FS0xXtBubNe8oUjQe5k6k6StPyOMUsK3EvC_I1Yt_ydlnaiPK4xAXLxNulgKH6k1CJS6j0fJF0hM11jvS7rZBu12Nzjg0EVruBNRNxQ69BgrAHPzew4XXpVe-gbOjAxHH1TUI1yZG83oBjAG979c0N6IdPh4YYUALzJGZ45j3JOaPVkoOuXM6K4xWZ625T70iNWflWO6Gq8K21WuXLYe7uSq3daUIVYIQS6nY2j3BZJzuew40z49EAdlJ1Vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
؛ با اعلام رومانو، ناتان براون مدافع چپ ۲۳ ساله فرانکفورت با عقد قراردادی به ارزش ۵۵ میلیون یورو به بایرن‌مونیخ پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/Futball180TV/95886" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95885">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
⚪️
🔵
فوری از رومانو: رئال مادرید بند بازخرید ۹ میلیون یورویی نیکو پاز رو فعال کرد و او به باشگاه برمیگرده. کومو تا دوشنبه فرصت داره با ۶۰ میلیون یورو او رو دائمی کنه، در غیر این صورت نیکو دوباره به رئال برمیگرده و وارد بازار نقل‌وانتقالات میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/95885" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95884">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGOjF8lNzhAq07G1VqRlk1lox2SS_J4SN4UWko9IQMscK7wFIjSjEPoWcoRYLyQQOZmfPeKrWz_rEWQtiPl9yPWdwA2dyPW7Ni5uKxUHuIxppAb5lWPv8wXLxojI_4Ks9Kn8-SvE_5ds9lIQDiHWp4CdgA8R-vEHqHBlXdtzDZSAXcKThmdY0pmepgTEZiaAmqbyYcb_C8ctg6aecZ5APoxe7l73JpdmgSfc9qh1QlG49sMgo52T9wPlNLkjV5eKD721LBMfPGxNdG0FzzZ07TWm5SHIUZ7piLtFKSFyobCCUJR-fAk5pJkfxR5XHMajzIG_F_rilkbNFlgs5RlULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
ریو‌فردیناند: پس از درخشش وینیسیوس باید بگویم که بزرگترین خیانت دهه اخیر فرانس فوتبال، ندادن توپ‌طلا به وینی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/95884" target="_blank">📅 21:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95883">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZiXiUHiYLgW3AR9bZQMvWwpVdOJqKdU6mcxjbDuqkY0zE4FTdZfc8SeZRqhZFsBvNvpfebV5SqvyLpJP0cOIJxyQ0GfoJ-tWq6k5NfGB9mY0nV1prW-EF73QJkJDWFXlhJoQGdN3bZd_7_q9EHIhwPzqXMW8oEUJhGqfSrWDrlX7z3QmaglQoXChF0G7XU-yOoNhllGu5Y6mZ1rGsv1eaTx_3grSXtzoQ-gXYepJI69sPFRKyefNF9gvoPbvj45yZNci6r5DOj-S0LQlXSPAjKIU_tmGjPLDzrDtjJdcGphDHRAQRpi11g_H2EmS70mTrxuaCfWm7dzK4Y7hAAH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
#فوووووری
؛ جام باشگاه‌های جهان از فصل ۲۰۲۹ با حضور ۴۸ تیم برگزار خواهد شد. بزودی فیفا درباره نحوه برگزاری مسابقات توضیح خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/95883" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95882">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9cGoJZcmfMM-ilTt5bsfbHYPeLyuNmkx882XCeTck4QWKmm7GhsqbO3czWey_EFpbIsPVOozBdsD-VxKpB7e0UrkPVGKauqIdizT2a4QhXndcMYm6JJU4pq8MOFnHNaC-mi1L7e41om9MBsBZbQUAvE683eekFn3Tcb-tcX2lZP0r_Kt2gHP42iDG1THxuzJMkq-pzIoKZA__t6F40Hugi3zon5cgRS4A_FItPZgjLIgkosnBHauh3A-ltlg-iOPu776AAeY73KbuW_MOqFJ3bBXPCtsDOP6BHYee_XhsKCW-HUU89Zwxj_SA_gJHg2iLUz-XcmBi5W17RKphBDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو تو استادیومای آمریکا میدن 13 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95882" target="_blank">📅 20:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95881">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh0kfApbsBX54tMacqXNKkzDN-qub1rkX6d2JZM16E4Ahuxbt9unhAFYUDWvEBbZ6MeR7GoiQQCY96kZGEDiv8dliMD2sdfxy30nbjx9AdI_5lyMzfBiUsJ-0uGjDqGNvIrLCxYkt4ITRHq1L_D3EByDGLmywdQSuecXiuFBcrN-lXG5UgQtditoTmZPsXd37ncvkwoItjjaZvPHmdu4KMFQIlcGk2fiOS9spmTIagGXguBWOq4DvP7irQGyfA9Q4W2whuFU4JktvNjFDLbCc1ga3H5TS7OCc_M54tk8IcR6z6doh-T5DJOhyO8F2DbE0omgHgcCCYfOtPmH7u_N_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
مارک‌کوکوریا:
دلیل عصبانیت هواداران بارسا برای من مهم نیست. واقعیت اینه بارسا به من پیشنهادی نداد اما دو تیم مادریدی خواهان من بودن و ترجیح دادم به پرافتخارترین تیم تاریخ فوتبال یعنی رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95881" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95880">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh6UjU5wS3Den-6J5RcuszJpkpFjZ3RSPyzqlldHWfXCOGPZRVN6wYl-Ez4E1eoAGjAoY6SoE-oEN4ut-FVlygxqQ7OJN0ScOBU_mYdq6IVr6Ax1hrOs5FPE_ujJpbyTFmibGkKUG7EMfyI1pEHaNbipXSpv0dxTyGvzaKiOpUl28pgFtjMhmOYECN7SNwtp1xixU21giQG5MkiAWtv2EoGoHzKCvh3LTQ6UuCkeZ65WyenuWGdCeWtJlLZZzbdHWgRfJ0OZTNKt0ZTupnsuZH-uH4a9XJLwNxu3Aurgyjx_q1jkLEezVcZt8q0Lxb_zj3xmZl0TAxzl11Cf6bBASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
🏆
بازیکنان برزیلی تاریخ که در مرحله گروهی هر سه بازی جام‌جهانی را گلزنی کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95880" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95879">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPWMgLUYO1czdDF7H-DhYyVIbnDFztDPBUO2fZ4dpUo8pTW2BZN7fS2uWt0t04mxUdg_SqaEHFRCRNmo0z9GMiV-hO9lrOMDb8-3ETcpqfCOSq40ijoyU06Rx5Us-bE4eP9JFUJ_HAh9XvD7NpiTN08EyC3xy7irVfEGyyABZ5DPw39KC6MV-gRGGXRimm0gdtuTViT0ZWouZM2ZCTo0-jmw7V5SUOWGKJqowR90bOzq1QxetM3n6YCYtjprmWKD4XdfrJiXVEGRsRRayeUFBuyai_sgMqv1pkZAYHP79mjoRdG8A1KJd4k1wYheoOh8V9K1xcFiTRa2nMNrC46_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
پیام رئیس فیفا اینفانتینو:
دیدن تو که فوتبال بازی می‌کنی همیشه یکی از بزرگ‌ترین امتیازات این ورزش بوده است، لیونل مسی عزیز.
در زمین بازی، تو غیرممکن را ممکن می‌کنی و باعث می‌شوی کل جهان برای تحسین استعدادت متحد شود.
برای تو یک آغوش گرم می‌فرستم. ممنونم برای همه چیزهایی که انجام دادی تا فوتبال محبوب‌ترین ورزش روی کره زمین شود.
😊
برای تو تولدی شاد و موفقیت‌های بیشتر در یکی از آخرین بازی‌های مرحله گروهی این جام جهانی آرزو می‌کنم، جایی که با تیم ملی‌ات از عنوان قهرمانی که چهار سال پیش در قطر کسب کردی دفاع خواهی کرد.
تو هنوز هم شور فوتبال را به میلیون‌ها نفر در سراسر جهان منتقل می‌کنی، همان‌طور که هیچ‌کس جز تو نمی‌داند چگونه این کار را انجام دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/95879" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95878">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/95878" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95877">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npymefwXRHhEpXtky6It67PhmS_3iMFPlqfCWh-eMf5oa2V_D1MArlz16rHdwfzjrVSPNTBcIrotSy1F9ljteIOOswRnr78HBk9vwES2G7eqUDQqHX4XnaqbdvVBIfbNmLKmmS1psfyFrcVxBZTz-DKN2yQX2T1KFOuC5suKjtJD3du_p4j71pyrGvnKuIc6PeWoFlUc43p7NY5pIfKKdyUbvm0t2LTIzNKbLNzhmIg148sqTi-6cVOYJaZU-wMjYp80ACWF5sUG8LM8uyj9NL0gifLGj8M2b6BRAS3_QomERs8Q0gDhh31AgWsuvlV-ia1lVvOFy5Ey46MP6wrgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/95877" target="_blank">📅 20:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB_Xw2KOaFruWOXrTwVA8h5Rgh_oe8xNkq3aXLI5eD4wWFHPJJ0yv1pMxiRpBdQPDorEwlg3OiydxB-hNAxLuIHOA8zUgXSjt4q-PikibIXcImK6TdSF-PvMu3pi0rw9fEelDfuNgdrPPMYv-e1Z6y635phInSF_dYQ4lMA9yBG-DF7cHyTNaSsVs75kSz2D_k884HdXAJk8mAjsx1YBHqa8bAQJxvoy_6MI-Ez3M7OCC2GgqUKjjrmDQqNW70IR-lvjL_iegaTVdlOHDa7HeRVzRuOQ6s49Y2RHe2mfs8_TmtWvOk-VE2j3SsntYmDq97Tmu2f7SGK98P6seGY8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته دوم لیگ ملت های والیبال روز اول
🇮🇷
ایران
0️⃣
×
3️⃣
آمریکا
🇺🇸
🇮🇷
23 | 20 | 29
🇺🇸
25 | 25 | 31
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95876" target="_blank">📅 20:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2N3iTBmif0u3McmfeSgayKaWlLSGwUqro5Mwp6jpLcmoHWIFaBMyXoy7ZWVGX1MNT220qkTyhPA-sXaz8j99AOicKEPmT4yYum-lsZ18hkfCsWgnQCUtxXI3hH1cgiV2rf2SiG2c2h2InF6zslLWnKog_QOevz9X5ibzBdi3IR2bvW3_-ODusMb2KnJCBJspKwZxuZWDD0-iq6pdHwPc3LzmQfODwZdNer_PbU1PXNAu1iLgZ55rVYYZanZRKVOOPKxlg018E8ttcXn6ORZ4yTbbowJaJyeimATWzTeL9czqUD8Qj23VJq3NKNJHo2h-mcaZ6GrkRgYEaHvM4LYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته دوم لیگ ملت های والیبال روز اول
🇮🇷
ایران
0️⃣
×
3️⃣
آمریکا
🇺🇸
🇮🇷
23 | 20 | 29
🇺🇸
25 | 25 | 31
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/95875" target="_blank">📅 20:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa774ae16d.mp4?token=RIsj3jJAtVTKdJ4vKszq0EBfyGC2mkhVSNAC8SYDZGpIuw8948BkLli6K3vFY0ATgu2k44yrc0Jy1dmTz8Tkm2HIjIpmD_O7vUHPe1HM1R8RNzVVU94eGQOueWjTfzKrigXC5y7wMt9iYrqOQ43OL1R_shJcQ1VLSRJGB3akrcVrhFQTp0yp33NhyOGg7I0vYDqDLLjoN6UHzGnSg-Jt6Rgj9pBetY3DjfzbWvcQSAfkQBsf2ORFsmj292WvOjyiIVj08g1EIyGAqnZ3kmjGW_vxmwau_cgYPyHKVqZ7MORPpuKf3Dbb6bMBObvLS4Ayzn9f0ImM_DvD_b_9Gbcz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa774ae16d.mp4?token=RIsj3jJAtVTKdJ4vKszq0EBfyGC2mkhVSNAC8SYDZGpIuw8948BkLli6K3vFY0ATgu2k44yrc0Jy1dmTz8Tkm2HIjIpmD_O7vUHPe1HM1R8RNzVVU94eGQOueWjTfzKrigXC5y7wMt9iYrqOQ43OL1R_shJcQ1VLSRJGB3akrcVrhFQTp0yp33NhyOGg7I0vYDqDLLjoN6UHzGnSg-Jt6Rgj9pBetY3DjfzbWvcQSAfkQBsf2ORFsmj292WvOjyiIVj08g1EIyGAqnZ3kmjGW_vxmwau_cgYPyHKVqZ7MORPpuKf3Dbb6bMBObvLS4Ayzn9f0ImM_DvD_b_9Gbcz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇻🇪
ویدیویی هولناک از لحظات اولیه زمین لرزه شدید روز گذشته در ونزوئلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/95874" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d7deda96.mp4?token=jJ2shahcTYwNOnRkKacQrA5_7AwvKvTTBkarYNVdaC3C-avNSGfGAr8LYvzaGVu9ec1QM2PbCmYfjOiARh2vE863ttKsE48pWczNULvjNlStfXXRjb1j-lC9BIM1n7rhP_ip8Wqip4VSNcxaho4y0HlJ47rWSjlueLhNB0CEtFQk1a867AAiEPv0ftGaw7_aCuYYK76Hka1CZZnkGCZ3gsAf0PdwCFNGKZfN12UYVK5obt5Vd6SR6xLenabLwpBEBH0018-zmHCwEdxQ3cnu_xaX3HvjO4peDLKSXr7YBWevO251AB2NO4jVqzZKQwjbJFnuX4DkX2qAs82lSHjzLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d7deda96.mp4?token=jJ2shahcTYwNOnRkKacQrA5_7AwvKvTTBkarYNVdaC3C-avNSGfGAr8LYvzaGVu9ec1QM2PbCmYfjOiARh2vE863ttKsE48pWczNULvjNlStfXXRjb1j-lC9BIM1n7rhP_ip8Wqip4VSNcxaho4y0HlJ47rWSjlueLhNB0CEtFQk1a867AAiEPv0ftGaw7_aCuYYK76Hka1CZZnkGCZ3gsAf0PdwCFNGKZfN12UYVK5obt5Vd6SR6xLenabLwpBEBH0018-zmHCwEdxQ3cnu_xaX3HvjO4peDLKSXr7YBWevO251AB2NO4jVqzZKQwjbJFnuX4DkX2qAs82lSHjzLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در نهایت چیزی که پسرا از زندگی میخوان..
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95873" target="_blank">📅 20:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95872">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWjF9Dr40tUCiUw5-6wvGkQqI2_reAje8P5tcu1-ZMq-eW3X5qWCkCmURtsgZbyUzDFl_El27rCYBQTjMsXcCvurp6Z_elaRHFd0Xf-w5LwhfHkOnXe0M3Q-9u1NbxX7WSNZ-uq6h9txWCU-43mFHWbxCkaZkNAtmHddf3f4pr1E9dsPEk6KFgyRoDbx-P65Yq5RYf1mIo-WcsfiZWUoao6tM8gcgJtXooANMra31pTJ-5ZuLGr1RZNaluQmv1tQZU2OQ5P3dZI46hZ5BOBoChiGQVP8_JLpYX178Tzt73pWV2EkweICE3uxJf0U45Xwbc7lMveXRAUfLEMQnQDBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
همجنس‌گرایان دوباره جنجالی شد
‏
📢
🇪🇬
🇮🇷
گزارش‌های «نیویورک تایمز» و «RMC Sport» از تجدید بحران پیش از دیدار حساس مصر و منتخب ایران در جام جهانی ۲۰۲۶ خبر دادند، پس از اینکه این دیدار قبلاً به عنوان «بازی افتخار» برای حمایت از همجنس‌گرایان در سراسر جهان معرفی شده بود.
ایران درخواست رسمی به فیفا داده است تا «هرگونه جشن یا فعالیت تبلیغاتی» مربوط به این گروه در طول بازی ممنوع شود و تأکید کرده که فدراسیون فوتبال ایران این موضوع را بسیار جدی می‌گیرد و از موضع خود کوتاه نخواهد آمد.
‏یک مسئول در فدراسیون فوتبال مصر نیز به شدت با این نمایش‌ها مخالفت کرده و گفته است: «ما کاملاً با ایده برگزاری هرگونه جشن یا نمایش مرتبط با این موضوع در دیدار مصر و ایران مخالفت کردیم و از فیفا خواستیم که هیچ چیزی مرتبط با این موضوع در زمین بازی وجود نداشته باشد.»
‏او افزود: «ما موضع خود را به طور قاطعانه تجدید کردیم و تأکید کردیم که بازی باید فقط در چارچوب ورزشی باقی بماند و هیچ پیام یا نمایش خارج از این چارچوب وارد نشود.»
‏در مقابل، فیفا بر موضع خود پافشاری می‌کند و تأکید دارد که برافراشتن پرچم رنگین‌کمان و شعارهای تبلیغاتی در تمام ورزشگاه‌های جام جهانی بدون استثنا مجاز است.
‏لازم به ذکر است که پیش از قرعه‌کشی جام جهانی، زمان این بازی به طور خاص انتخاب شده بود تا این رویداد باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/95872" target="_blank">📅 20:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95871">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChFB4dfGfjKmYFI9WgVg15m59XZ0bWJhG2-JZcpHrVwXwxwlZABJOeu9C3KDLpb5pJuS23ZAqcsuvPwCHwG0bpCWuYGjhuYzU2QC-EH2yo8E47kFRDyvkvUtBgl6IZIf-INTdinUg0gFr8z2tJrlUPQmPQoQpMUGn199V2AODmPJWS6CN2Y44h1XUMfXkDcLyND7VMQL58qYqd-Coge57-D5lotDobSbvNzevV-j4ZKIXp48jbbhJ2c0KlPQbUlw1tXoNLxURbsvrebML9Mf_3GK4KmquMs7y8pF7qmXb1_IvO0wg79kFbNnhf9t8NmTIsXU6mVzaXyeJFsNJX4lfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
در جام جهانی منتظر چه چیزی هستید؟
🎙
ژوزه مورینیو:
دوست دارم بازیکنان رئال مادرید حذف شوند، چون می‌خواهم هرچه زودتر برگردند و در تمرینات پیش‌فصل تیم برای فصل جدید شرکت کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/95871" target="_blank">📅 20:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBvuBE5xlZA0oFNe2ncLyBKV1cdPPVntISL62nvs39gjz2dO8FXq4RYvE7dkOb_vMts-er0cpCc37E6YYLyys17qWtsHizqgV5sozynm076rFg1LBh0nv7LGbyFp3ZWgfubhh6BPe0y9NdC0uVFeMqSPBPhPMS8SRodYm27E-dNu8ogLqo7RlUgOZgwUf-CuyW2GB06O_AI0pNrXfKvga_ImHPPzKy5t_dnDKkI0A0PbWNj7MO5-LfHKCP-EM8phMezaZn3RvdFa42Y275jQ8gGhM0n_9wg64TN8BL9dSKHfFuJtvDeDQdGK6pCEhC2dSBXNOwnlsyvOIf1ArumuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
با اعلام باشگاه فوکوشیما یونایتد، کازویوشی میورای 59 ساله یک سال دیگه باهاشون تمدید کرده و بعد 42 فصل فوتبال بازی کردن هنوز قرار نیست بیخیال فوتبال بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/95870" target="_blank">📅 19:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95869">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">والیبال دو ست فعلا از آمریکا عقبیم!
🇮🇷
ایران
🔢
-
🔢
آمریکا
🇺🇸
🇮🇷
23 | 20
🇺🇸
25 | 25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/95869" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95868">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95868" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95867">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbpdyd1ZStvEbradlzBjjtkO0nBBUENfF-3uINlbLccVnSfRXbINhKYC5pYY6BGsJ_MJ43BRubzJrAqfBxLh3IHOG1Fk778Ylc61X_CBW0lr9xVvEbUDQKywAkT7jfJ2WzuSme3ljhxqapLQaYxbe6QiIbOtnY_a-D7gBperOu1evun59djq3iOLTRA4bwUk_uiQcHTwq6GeBbkkk7lvWJ5K5XCkZNebL7gphbOzkLMsVd0zVsgP7sW3bE3rcd9wnefiV3z6CPHKgpuyPFssFLyXn0j_waqc4pxLh2raO5TXvutfLZKDm_TWZP6xwMIgLkUqJN5WbmbWgTCuFIkM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95867" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95866">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWQTf9X1nhQ5hqVaPweaYdtNqvs6R_DCc7twag-CQIUL_h17jo6PjhQNqQe3Kve7dpLh1yWnkaTSmu918QYNa4J_dNxK5zrlN321s56QzYQ0xzh-QW2kSS6IHpYhHWZ8-sI64NDZhIFw97_Oi6T5lSCE8XzCDg7y1A-zb4pxQbRBF9w0LfFj4Fp-tXGGMk8c0sPuPgdnEcnTuiG5ULL9eESchT3qTEg3ZdpFs_daQEx_zoljRiDU3duqHlye5eFH9PSRPX7pP8VuuLb3a7M73JZWCRUintWu8IFu3CLLNx2jYRu9JAU-uwgu8WabdRQHTifv_lMzHxPGv9DDd5InEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
آندره اونانا با یک قرارداد قرضی 1 ساله مجددا به ترابزون اسپور ترکیه پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95866" target="_blank">📅 19:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95865">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHEm2fdyKifcuAZt1vNqD0pBh79oUaPCADGjD3F6R3rLwdvscpXlqmW2iYbCPdN1Dz6Q7iWyjFf4sb9lCdBkelQsV1FokdeP7FHJIWIBlT8TuvLaZPsEWbvXnaFRCquuex6f0m4OuuUDFZtbYqWyKbF7eg8QQAubXpBB7XGA8x7BjFWvnEBapc4INzIqSPkq7zJol-f7njjj5HniAbffFedVQ5_QGZGNUuJSv4XTJgPFk2m_QqvN-QnWDjmHiapLMCdQVbTRMFGcMFNAGS6nP_5oaQZHXPTGal9wXbSUugZvTgIKTOV87aqLhl2Ml0QWhtSd8DSpUcaPF9enB9aVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: «میم‌های توییتری خودت با اندریک رو دیدی؟»
🇧🇷
آنچلوتی: «بله، خیلی خنده‌دار است»
🎙
خبرنگار: «خب پس اندریک در ترکیب اصلی خواهد بود؟»
🇧🇷
آنچلوتی: «کی؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/95865" target="_blank">📅 19:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95864">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50eb40e5b1.mp4?token=SjZy_00U1ZsGR_5oqcbNBBn5Fw3fySCSoiiFkSdiDyw8YYeW5lCYgKIFgMPsbzHR1c29DMXVQhpC7NuZd2v7J8WFTLXyxDHo2qU5bhUQtlhWwejwGMFdBgPUwIK6iRI4TXjw38--w1dAxBmdpbUvHRd6saDyyg7AETQZPueap8jIhy0RMj2G9QVG3-8phmsy2wT8SlpZr5PAY6J20FCoIHgvjlZAuXS330bjpPZzE0zvh1nip6Y57OBunkV50qdqejFxt00ivtnwT0niaj-MLJEpfBIsh7WPD0APETyFdkwuTbS9OKyg78s1xGDT40zIJTE3pTi9-eToOPEZISSmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50eb40e5b1.mp4?token=SjZy_00U1ZsGR_5oqcbNBBn5Fw3fySCSoiiFkSdiDyw8YYeW5lCYgKIFgMPsbzHR1c29DMXVQhpC7NuZd2v7J8WFTLXyxDHo2qU5bhUQtlhWwejwGMFdBgPUwIK6iRI4TXjw38--w1dAxBmdpbUvHRd6saDyyg7AETQZPueap8jIhy0RMj2G9QVG3-8phmsy2wT8SlpZr5PAY6J20FCoIHgvjlZAuXS330bjpPZzE0zvh1nip6Y57OBunkV50qdqejFxt00ivtnwT0niaj-MLJEpfBIsh7WPD0APETyFdkwuTbS9OKyg78s1xGDT40zIJTE3pTi9-eToOPEZISSmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95864" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95863">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTGFNfrMyj8Ft821oLW4NJ_3C3EQBsXRiJeXwn8mCMVLgmiIsZK5uS8bR9rw7pCpvaZbsO2yr1_0bx28s8z7Qhr3Abksuf1n1q3JRhGYaYM3GUd0hvlfT1vqIIgqNMX6osBQ6X1dSu3c9vicMl7uUhUnENGmKJPzfaJoriJrsXhWMICKTFrDrIPvsZyOkOFOdRNikY3pTkw4b-70WzlquQngWJFlLgNTlZ4OEiAPTs2M_Xq3mlQza65eoXf5_Taiog09lGiEQ7zow7xlEAFNSFi0MuTYfaHAVjbgiRP2pCsc1Lkw2GQp-hKp1NPhcnYLzHpjNUb6iPGoMcqNg6iD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🔵
فوری از رومانو:
رئال مادرید بند بازخرید ۹ میلیون یورویی نیکو پاز رو فعال کرد و او به باشگاه برمیگرده. کومو تا دوشنبه فرصت داره با ۶۰ میلیون یورو او رو دائمی کنه، در غیر این صورت نیکو دوباره به رئال برمیگرده و وارد بازار نقل‌وانتقالات میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95863" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95861">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbBMvDABdciw9EWnZ7Ol7aVgNbmL0kTnXK3-KzRoGl4RSunu_6Cnq6P-iLgkCoVVt0_fnnqrWe1QpRAgDD_queIrQ78N1eMwJgIH94Z-tL-8yQ1Tndp_39ElZLgZeKh2AACvV3D4wCuOS0M7cntgBmv24mjYUQincSsRlNfFb-8y0KbyeC7nH1CB9iTOmWsxJIyqTNkpTmIM7QQec9FfW_jD-yI5Y6HSH1BaqOo7gAz0wJ0waUcskdU-8QqBNnufP_DxfYLOjH-i2n4ATh6WpxC_8hb10VsjlINLoHyIQg4pv-kQA4Q40IvZbibHSmurKsT1XAl7c6kRfSmY_2bVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmroZanE3ZfDElKtOxJbR5cCKH910EwLy9rWHjd3trdZ2Zcucr0dmabxcOOwHZkgIxLHDEa7we9xOsAX6lhf5iN07pfQiT-j8Rk5B4lvkY11nWF0Un9FAr8h0fTiR06ZBqCtmDNMm5krVdhBHsTmA829hiJ2XA3WxTjBzZX9dUZmrAU0cl4wthxWYNwdBcaOe4yaTfpiGdNikiIuuV3UHuZ5u4YjiKvGyzXYkU-lmNbb60C3bLjcCIRz_SJK4UuDJ0cMcylFJt4NEL-65vO1pD-XN8upyfo4kxPG2gQKHwbaIKurMkzBKhguBvhZOR8Niw3ZNLlSVO4M36r6vmfIPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نانا کواکو بونسام (جادوگر غنایی) : من، کواکو بونسام، قدرتمندترین جادوگر جهان هستم. هری کین را شکست دادم. دیشب بازی او را دیدید؟ او حتی توپ را هم ندید. چه برسد به اینکه بخواهد گل بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95861" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86caa5adc.mp4?token=a3x39tkFm97jcTtXmeyjHFtwaAOzereXK0BH6rqoKtk7LYpIpjLfVynFI7ZjaLGm4dYjR9YWZlq2__dWBwM7_9FU37pQdcl8FX8X2eFKUKO6XkUOSix6MvauHYYEdJRs_A0abVvAN4tZcIYbGtf1Nv3hnWPM9xE0-2SrEQwqF2QONhTMho3XJc5YglRF5r4a4GAcvdHSsercMVgNhBkJw8iPhnBuQI_qxZTbzbXKxqIkCpaQ1VIWcbaDIMRPES19ZVTSjS7dwU_JNLuphoITwyU-FspS06MNURmses687DJJ7s2c9BJdZBMh09JMjkMKfPRvJBlHAfeo-XkfH-DWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86caa5adc.mp4?token=a3x39tkFm97jcTtXmeyjHFtwaAOzereXK0BH6rqoKtk7LYpIpjLfVynFI7ZjaLGm4dYjR9YWZlq2__dWBwM7_9FU37pQdcl8FX8X2eFKUKO6XkUOSix6MvauHYYEdJRs_A0abVvAN4tZcIYbGtf1Nv3hnWPM9xE0-2SrEQwqF2QONhTMho3XJc5YglRF5r4a4GAcvdHSsercMVgNhBkJw8iPhnBuQI_qxZTbzbXKxqIkCpaQ1VIWcbaDIMRPES19ZVTSjS7dwU_JNLuphoITwyU-FspS06MNURmses687DJJ7s2c9BJdZBMh09JMjkMKfPRvJBlHAfeo-XkfH-DWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل‌کل دیشب هوادار هائیتی و مراکش
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95860" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95859">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9810d64f.mp4?token=sa2G9n6-94s6oOv0uihvkRnNUXILR1HAhUP4LjUCPNCdS3R_SZzRaj6iz5_mVObml3XjadDcsK70lktq4UWKvnTHi3t7B4UvJxdbghIjfVE4vxAo8_FeTmAlLXQU3ZbGaFERdp0hA034_eEsqmyoMsCaGFKVi_pPeD7_sc4B_IF8jAqyOsFI3n6zzqbPpuOhpUmwOBQDp-E32wirDQrMmY3F6OTFZqz4JsFNkRExzcHqmJssW675VtYrolnhX4w52BW-UteViqvsKAjraaByJ8narZ6-TEUkPWLjn-8Aslmks9NENwuJLjwaDowY_msxN9tLg71D6HYKxmptzOlLfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9810d64f.mp4?token=sa2G9n6-94s6oOv0uihvkRnNUXILR1HAhUP4LjUCPNCdS3R_SZzRaj6iz5_mVObml3XjadDcsK70lktq4UWKvnTHi3t7B4UvJxdbghIjfVE4vxAo8_FeTmAlLXQU3ZbGaFERdp0hA034_eEsqmyoMsCaGFKVi_pPeD7_sc4B_IF8jAqyOsFI3n6zzqbPpuOhpUmwOBQDp-E32wirDQrMmY3F6OTFZqz4JsFNkRExzcHqmJssW675VtYrolnhX4w52BW-UteViqvsKAjraaByJ8narZ6-TEUkPWLjn-8Aslmks9NENwuJLjwaDowY_msxN9tLg71D6HYKxmptzOlLfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عادی‌ترین هوادار تیم‌ملی غنا در جام‌جهانی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95859" target="_blank">📅 18:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95858">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUUwSc0bFVb9Ix2pB1hEQztC4doHMhKRzgFZQHIYcbrskR0iZPIoqS3hkjvStOk_XtjUzGniJt6oYsQOLLQ6IcnKWp330rIq-mjLv0s5z8fe0dXPJ8P6mO-XaiQQsYhbraMriwaocX7ucGyXnjsLI7d0Zpnarp3ryH7ZCIqpdDbLe1k8pKdI0EQ-XY3zFC4uEoDykZBd6OOW3WzcqpK6Fuv-OsondDNat_29tQTJuVucOdW5auycWDahrRJ1GPsk1pSDZevwDZ6hAX1pnIr4KRUMvg-tA9uqfpyKZ8d3GKGpOamlEF7-GaTQ5eaz2zKvFu_GmXdrZ92zNhM6tFtOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو به همراه بانو جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95858" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95857">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp1E4zN8Isr1eZMSYoaNv_cXzseT_kjsansw1P6K86QqPe8SgbR-ViN8m4M5rfA5JPYqz0oqLjXPA_Pn-lcMrYxDtktjqjXf66LRymZAIpeNDtf6ValAcmb38wE0JyXce3J8SDmjyxwaXH0MR850y64HFlw8jqPvXhcCpVHdHOqD0fdpbemfdZtDw3xn2zGIK6gPjcu7IYKGXGvp13vlPmFRqH6MUDia93BOpa9qdy5VnybpTdPTg0JOK7MZ76yy4MRBdUIeP4uqaAfJTrS0wrFpzFrT2NXMtv2SWxgv1NgkekCd7nRKSnCTxVjzy5legqg1tcXwC2v2QQtwcziRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تبریک تولد مسی توسط اینفانتینو:
تولدت مبارک لیونل، تو با استعدادت مردم دنیا رو عاشق فوتبال کردی، ممنونیم برای همه چیز؛ امیدوارم در جام جهانی هم موفق باشی و همچنان الهام‌بخش میلیون‌ها نفر بمونی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95857" target="_blank">📅 17:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95856">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQrT7PmfWkWDzdXBXbFl_Ze6wNpb7MkBmveKu-S8OVXKzvLWstGLw4Y3hznp31u2YLhvIsHE72hTIjsCDNHbIt6IhRM2uyL-ghKJVl3awEeDA_pumV92W48eYK8RcKBZ6Fg4wjT-twTgOMsPfW00g1s9UPKh1wbXb4-7hlw6rpN86KP5f6LFpMc_1hSx_kWvyse1XAMK9dgBgMwylg5R-oBpu9_-wDMcfFHMdp8w26QxcMEZ-_drqPJpLJyd7HHgDkmLZTkRRBLWDF3F_OOeyJ7YWStwOI5SJc-OfEi0SgCy6i4BtpaU4YhMQ7jP7IBNoMp3iysbG9SKTtCROTF-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد آلمان:
لایپزیگ پیشنهاد 116 میلیون یورویی لیورپول برای جذب یان دیوماند را رد کرد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95856" target="_blank">📅 17:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95855">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904edba416.mp4?token=Ip2ZNZMKRQvJB-bnfjEKfC_6FiBP8MSOF9wJd7a11ivh0n8FrQ-ku45c40MfgIlZSCG5Zd_jWwXE7oEWLJ-QKQ8wAG1UYqN9BdJzqkVPcPceDcS-6Wq7xwCwJNarH4DHkD3Wus3NDlG3cdEulvIPgxr_KI8rZKdV6m5trDD-CLGXy6CMX8BhJMFd1TJ4jUpIz2QmP4QkJgNJuK3S15qdD3OuPVZiSdRJbqgg2UF53ULrn9vDIp4aB7WEDfosZIrPwO5es-wpERltzW-uuCHEO7cbFj8XFehKsFSGWdG7TuFDFvnFSeO9YIcc8z7TFJ1SGPiNISqec9fUJE1xkkR3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904edba416.mp4?token=Ip2ZNZMKRQvJB-bnfjEKfC_6FiBP8MSOF9wJd7a11ivh0n8FrQ-ku45c40MfgIlZSCG5Zd_jWwXE7oEWLJ-QKQ8wAG1UYqN9BdJzqkVPcPceDcS-6Wq7xwCwJNarH4DHkD3Wus3NDlG3cdEulvIPgxr_KI8rZKdV6m5trDD-CLGXy6CMX8BhJMFd1TJ4jUpIz2QmP4QkJgNJuK3S15qdD3OuPVZiSdRJbqgg2UF53ULrn9vDIp4aB7WEDfosZIrPwO5es-wpERltzW-uuCHEO7cbFj8XFehKsFSGWdG7TuFDFvnFSeO9YIcc8z7TFJ1SGPiNISqec9fUJE1xkkR3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
نیمار و دختر خوشگلش‌ تو بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95855" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDb2luhPpunZRaNPn8-KLmp2xAMhnmoSGFKhYOXJcaq-Lv1CnWddZQcl0UUROhZbrmJJs7gzGuxNRHI_UC7Tqo8HEzNxrkms1GLlHTJ3X-vTtWox-ij-VjgsI-erJemZq3lmd5II9FNqPnOpBPaUG9go3EVdhJVPzCMW3V7d9Az6GNmoKoZGkEXEH47rEF5COyhRuNvxaSqfYLseG1EXCpF8CPkv19af8EqLQUvww6c8FQOLIYQmiu2D7Lnw0IxQ1dYOTxXRyVWOg65QcXTvfa_BwoOSFRgz5nG9ikoC-ojlizfLZmnz6Ax56ywj8YGZd5Yerelo4HlNl6YkV3CTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇨🇼
کوراسائو روش متفاوتی رو در پیش گرفت. برخلاف بیشتر تیم‌ها که بازیکنا رو تو طول تورنمنت تنها نگه میدارن، کوراسائو خانواده رو در اولویت گذاشته و اجازه داده بازیکنا کنار همسر و خانواده‌شون تو یه اتاق باشن. حتی فدراسیون هزینه جابه‌جایی خانواده‌ها رو هم داده تا کنار تیم بمونن؛ این تصمیم کاملا نشونه فرهنگ گرم و خانوادگی این کشوره که حس تنهایی تو تیم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95854" target="_blank">📅 17:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCU4j6WW1tfNuJACMwFPVCX8h7UYi6cY4LXPdbOjJMFLSgsDBfwk1cDKTRGwSAldxeeXocWydDI5E6L2IdAw8_ixXKGfT2YUNSE8rRUXCvglVi_oLJuTzr8_DafhKjB4cbK8qjXL4fCGYEeDu3r0rsDpdpaxTFp8qVejWCI6aVqDaDFTuDBErxni0eX4V3mAbdW6hivw269RukdxH6d_TxYPk15YevgsSmEReRcmRjNNxpKSN1hXOkp_nllk-rnyMx-dcCVVRnlGaqpS0VrUrswwzVZa_tji6IqQkUNhGAMjtw30lUBTtqKosZgaZJsLvFQUMuLCP9zyVNIK7XknAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی تو هر 3 بازی مرحله گروهی کاریه که فقط اسطوره‌ها میتونن انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95853" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa271917c.mp4?token=elKoDplTT4d29St-fVy3I4wFjU7ASLXPZTQfh9lRF7A6bcRi1x3jZG--0Rpa5zxtlAXHmpcgzT1-eawRG8Hdtqt9QMqMfsO1XlbrSB6NGbgvs7aY8e-kbe1UKdQ4DZ4QSPZA8UTSIfN8bDxGI0HvQ0obkSgfiC2fhExYm3xXO9O10ViA8rnuRdJdA3mBJykpwVFU9L67kOLligzfDO_55NulYE77w2nyUf_AkINgh4h7eNfa4gEQ6d__Pbg2hUX62Kg9bHH4GC68vcMCBSgl6jh9zMB93-b1v_QT2Xbkv_WqkQpZCeFWy954MVzqfQMyfvHjk5-ODD0rCJqwdz9VZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa271917c.mp4?token=elKoDplTT4d29St-fVy3I4wFjU7ASLXPZTQfh9lRF7A6bcRi1x3jZG--0Rpa5zxtlAXHmpcgzT1-eawRG8Hdtqt9QMqMfsO1XlbrSB6NGbgvs7aY8e-kbe1UKdQ4DZ4QSPZA8UTSIfN8bDxGI0HvQ0obkSgfiC2fhExYm3xXO9O10ViA8rnuRdJdA3mBJykpwVFU9L67kOLligzfDO_55NulYE77w2nyUf_AkINgh4h7eNfa4gEQ6d__Pbg2hUX62Kg9bHH4GC68vcMCBSgl6jh9zMB93-b1v_QT2Xbkv_WqkQpZCeFWy954MVzqfQMyfvHjk5-ODD0rCJqwdz9VZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
روایت ایستگاه آتش‌نشانی تهران سط بازی ایران بلژیک که بهشون ماموریت محول شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95852" target="_blank">📅 17:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bf6ca2bb.mp4?token=BAZD8hdAbueM-i4nwqK3Jam14XO6gRy1B66csVCX0o4a2P4xBZOXjo0IkwL2OCMBtuKnDuCCnlHCD8s2Zs2YFbi3y02nFcXqaVpExLw-TvWoTQOFFqBTLEK3qgO4Xc1wsYTmwofXcdLDxJYw1zXsMr5eNhtJOB6QbQ3D8LzEO1kDHWrmQgaLU4suJpkYarDglyB2BuI2sCZQr49kUQLn9UceiG4p6H61ZmNJfbuv88lCPzbt2gjvGzf59v4HrwOWNj9G8L84-OQFFeZyGMkwnrsr2MyqLeWDZYOZx0Sp-qFXDM0DD_oHQYxXdUjEZrmIkswL7VGF6MCWsQKD4Ih19nD9b_UW7G27BlLkeUkU3xJoLMosg1fmg-w2wur2n7fTi16ookX5u6-Y2FCf77QtMZNa4Hw9uSOmd25TTdu72EyxDb77Ut3rd_uoXF0qOunBSyHCcafVOA0XPoHTctLqHR2WkmaWb8espghLa6geNAP46E6peL38QaRTF22ClgJd2-qcHHTFLA0FlsbPQnQUlBHVXEnLyBsQzvxMNq2xcx1TC-Rbo2mE8BeJbue209VO1oDmsSUab1x-OgA7X6TcZs7o7Vu6kvP7C1si-gbNaLGPCs92tyXJ38jnrRZX7Xh58Tg7ABGkyN-nY-uWvt18qgAQwRqRVCvGWEwj2PQZbPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bf6ca2bb.mp4?token=BAZD8hdAbueM-i4nwqK3Jam14XO6gRy1B66csVCX0o4a2P4xBZOXjo0IkwL2OCMBtuKnDuCCnlHCD8s2Zs2YFbi3y02nFcXqaVpExLw-TvWoTQOFFqBTLEK3qgO4Xc1wsYTmwofXcdLDxJYw1zXsMr5eNhtJOB6QbQ3D8LzEO1kDHWrmQgaLU4suJpkYarDglyB2BuI2sCZQr49kUQLn9UceiG4p6H61ZmNJfbuv88lCPzbt2gjvGzf59v4HrwOWNj9G8L84-OQFFeZyGMkwnrsr2MyqLeWDZYOZx0Sp-qFXDM0DD_oHQYxXdUjEZrmIkswL7VGF6MCWsQKD4Ih19nD9b_UW7G27BlLkeUkU3xJoLMosg1fmg-w2wur2n7fTi16ookX5u6-Y2FCf77QtMZNa4Hw9uSOmd25TTdu72EyxDb77Ut3rd_uoXF0qOunBSyHCcafVOA0XPoHTctLqHR2WkmaWb8espghLa6geNAP46E6peL38QaRTF22ClgJd2-qcHHTFLA0FlsbPQnQUlBHVXEnLyBsQzvxMNq2xcx1TC-Rbo2mE8BeJbue209VO1oDmsSUab1x-OgA7X6TcZs7o7Vu6kvP7C1si-gbNaLGPCs92tyXJ38jnrRZX7Xh58Tg7ABGkyN-nY-uWvt18qgAQwRqRVCvGWEwj2PQZbPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
به‌مناسبت تولد لیونل‌مسی این صحبت‌های زیبای دکتر صدر راجب اسطوره رو بشنویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95851" target="_blank">📅 16:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a8197a2d3.mp4?token=lfWxJQWTz_0c34pnmjZZLvgq6e-sUqbFdCq85BXjQYvdgdisqDCzlu9KtvNFPQ55dYwIjx2v2MjDPxf7TQnuX_JRNsbR9-KdgB4BPK6_XUgxvfIYBm9Hdzi-nSsAYK6vIjeIjvapOcGBYzp1l6NtbkQ6EppXjMhPTApYF48v2LFNrL424Juklvrwsvhfc3xQxsmbAvzMbtYcL_lfGvHqP0CWxZpp63gCSGMsZu_kRLCo6e9l3ztCs-T7JsFGDWx8dENbADU6Or178P_9RnX0seYXp4HJsYKXiriPw-GgwfSb4v72AxOppVlF9HDRHF5kyzBbRmvFQQq1QAq8k51oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a8197a2d3.mp4?token=lfWxJQWTz_0c34pnmjZZLvgq6e-sUqbFdCq85BXjQYvdgdisqDCzlu9KtvNFPQ55dYwIjx2v2MjDPxf7TQnuX_JRNsbR9-KdgB4BPK6_XUgxvfIYBm9Hdzi-nSsAYK6vIjeIjvapOcGBYzp1l6NtbkQ6EppXjMhPTApYF48v2LFNrL424Juklvrwsvhfc3xQxsmbAvzMbtYcL_lfGvHqP0CWxZpp63gCSGMsZu_kRLCo6e9l3ztCs-T7JsFGDWx8dENbADU6Or178P_9RnX0seYXp4HJsYKXiriPw-GgwfSb4v72AxOppVlF9HDRHF5kyzBbRmvFQQq1QAq8k51oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
وقتی قند تو دل هوادارای فوتبال آب شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95850" target="_blank">📅 16:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0437caa8c.mp4?token=QWMQb6H_8c29Rx-KRSruLPazY6l-hdoWCBYlLz_Yn8dTSD2quS1nISZ2TqHo1cIRN30FcxNkXUetY_QN7W5n0KQ2eAv9eCOv89cHNkWC8-oZSLHXkIUHp32_W5SxjZdbGPeVQUOocILMQGH7niEZLNddu55DAVIWu056eHFWQVK6yVHEeSy5C5HllVFT7QmTjiPdny8LzaiVfc5EeCNKdj6vzesEHqBEO5Z7BWnVtXaakqyBvGtMuxZYn83wQFjZgGP5Fl7ZzWI_1nhRinjrcapjU6_7lQy95NVT6xSYFxWjaRRksUsVyCaLonb89r9INzy3vt8o1nT6uN33iNFhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0437caa8c.mp4?token=QWMQb6H_8c29Rx-KRSruLPazY6l-hdoWCBYlLz_Yn8dTSD2quS1nISZ2TqHo1cIRN30FcxNkXUetY_QN7W5n0KQ2eAv9eCOv89cHNkWC8-oZSLHXkIUHp32_W5SxjZdbGPeVQUOocILMQGH7niEZLNddu55DAVIWu056eHFWQVK6yVHEeSy5C5HllVFT7QmTjiPdny8LzaiVfc5EeCNKdj6vzesEHqBEO5Z7BWnVtXaakqyBvGtMuxZYn83wQFjZgGP5Fl7ZzWI_1nhRinjrcapjU6_7lQy95NVT6xSYFxWjaRRksUsVyCaLonb89r9INzy3vt8o1nT6uN33iNFhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇲🇽
هوادار مکزیکی قول داده بود که اگه کلمبیا از گروهش صعود کنه یه حالی به پسراشون بده که به قولش عالی عمل کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95849" target="_blank">📅 15:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=pKYKSJpGUP_gb5CWF0llH11ndpGQX1IytykfuDlSa5kyZw6TaoFfLUg9GqQC6cU69j7w_keGZyu4Hl6qTj-6k4qvvERll-jY1LrW-2Q8qS4_ytG6b4oKH-s66JxHi0DLeGCBtGfe7ZnLnVp_MQc01xY0t3_iQ2DrSycLCs1sVzawCx1T5vVIk9Hp9gTK_vWojLKrYViT5jZ609mJvSMcOUz3JJJemX00OdMba7aD87Z9h43rh0Eq-jVX6zFrxYLQoHjN4GaljnyDTeIRNiRXoAwQhgXEYJOYVYvI988pBGkMwdiXhZriRTtyZMuyIFUns3FESeu1f2OSaeq7oWXk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=pKYKSJpGUP_gb5CWF0llH11ndpGQX1IytykfuDlSa5kyZw6TaoFfLUg9GqQC6cU69j7w_keGZyu4Hl6qTj-6k4qvvERll-jY1LrW-2Q8qS4_ytG6b4oKH-s66JxHi0DLeGCBtGfe7ZnLnVp_MQc01xY0t3_iQ2DrSycLCs1sVzawCx1T5vVIk9Hp9gTK_vWojLKrYViT5jZ609mJvSMcOUz3JJJemX00OdMba7aD87Z9h43rh0Eq-jVX6zFrxYLQoHjN4GaljnyDTeIRNiRXoAwQhgXEYJOYVYvI988pBGkMwdiXhZriRTtyZMuyIFUns3FESeu1f2OSaeq7oWXk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
جواد حسین‌نژاد از سوال خیابانی هنگ کرد؛ چجوری میتونه اینقدر کسشر بگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95848" target="_blank">📅 15:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=eV223XCW5AgtUz4O8P5Yd-CjJ2MPTmsPd2W4I4PUyclYjbojqG6RAdHm2SMEPZaA4uuGnNrxW7JfnfLQuDxs3OmxBTJ7ldGE3N5LoUsJEjFhZug-jZIidRDgi4W7SDkq8hm6Uulf58R5lFjT2hTs6VXk1-iDSbeiH_7uPYOYZ5o8fZKk0NHU48_fikKp24GYWK5cwwib33GPMkmdQo8cGj922P0jpOogYzPH-IRotyGU0Il7bA1kDqfrKRc37gC1iy7wuUAavr7uIREZfn_besclzLzT5bM12Yjiicpn5g9X1tjOiGsJu6wnMpGiTh8r7G0-K77g9Gg9AgOrUoKLmwR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=eV223XCW5AgtUz4O8P5Yd-CjJ2MPTmsPd2W4I4PUyclYjbojqG6RAdHm2SMEPZaA4uuGnNrxW7JfnfLQuDxs3OmxBTJ7ldGE3N5LoUsJEjFhZug-jZIidRDgi4W7SDkq8hm6Uulf58R5lFjT2hTs6VXk1-iDSbeiH_7uPYOYZ5o8fZKk0NHU48_fikKp24GYWK5cwwib33GPMkmdQo8cGj922P0jpOogYzPH-IRotyGU0Il7bA1kDqfrKRc37gC1iy7wuUAavr7uIREZfn_besclzLzT5bM12Yjiicpn5g9X1tjOiGsJu6wnMpGiTh8r7G0-K77g9Gg9AgOrUoKLmwR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌صحبت‌های زنده‌یاد صدر باید با طلا نوشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95847" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5255345.mp4?token=fQkGFLieZtsEzqwq-S1vX3Jd88wmpgcZik95qgyosQuPtTdSfdLbVEeB81JRcf_A-46OnWv8c4F5rO9uxFAh_TqL4mTUfTSuB5mt_4-XOPPnmBhx7fjiONO3kDW_B__JPsen9vqCBbp1uVHDxPfAqj4LWXhuvcLLb4QDZQVM7DyYtAc9m8mD1Exui1D_PkzWrV8hBmIeuSqvPCd8zq6553pbALps8mpFjH5RXSC8SlQagTRiJ9BBE_rCWq9kpRl9dgJj8dSMDqbhHfgeS0vwFmJbXgZi3fJBXAEhXsabPr6Wp0Hh4SYft1rZCuQPi3V0zgDn-LCpxTa1nHS8QzROkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5255345.mp4?token=fQkGFLieZtsEzqwq-S1vX3Jd88wmpgcZik95qgyosQuPtTdSfdLbVEeB81JRcf_A-46OnWv8c4F5rO9uxFAh_TqL4mTUfTSuB5mt_4-XOPPnmBhx7fjiONO3kDW_B__JPsen9vqCBbp1uVHDxPfAqj4LWXhuvcLLb4QDZQVM7DyYtAc9m8mD1Exui1D_PkzWrV8hBmIeuSqvPCd8zq6553pbALps8mpFjH5RXSC8SlQagTRiJ9BBE_rCWq9kpRl9dgJj8dSMDqbhHfgeS0vwFmJbXgZi3fJBXAEhXsabPr6Wp0Hh4SYft1rZCuQPi3V0zgDn-LCpxTa1nHS8QzROkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
داستان ریشه عمیق ارتباط صمیمی بین کره‌ای ها و مکزیکی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95846" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbf385023.mp4?token=Q7-ecDn68Sk0uRQiP6KsaS481Y4fGKTeih1NjFk5k7ZKXdqUy650QZo0aC2SPg_AnIVPoqnmIPcIFAFJ1Pdk-N04OK4NGCfSevxRGAQ-sBxa7rNiY-qNI0kr6gU5Awoiup4JAxpQYE6tzTBZMK0T2ElRX_uxy11U3L_64Jfkphzqh0apXY8TH7qi7jB6zO9KzY14fn18_MDNzpNQpTzyKqOSMWWxx27jH3P8JN3frj1qvJNVsfJhTsebsbA_itgsRxwOCYDHGp7BS6iIcr7ZuzOdyaFiOMjvN70fP8x3-Tgi15YQyi8yIZCO15MxNMT7uXJZ1ThiH61WtnKBnVbxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbf385023.mp4?token=Q7-ecDn68Sk0uRQiP6KsaS481Y4fGKTeih1NjFk5k7ZKXdqUy650QZo0aC2SPg_AnIVPoqnmIPcIFAFJ1Pdk-N04OK4NGCfSevxRGAQ-sBxa7rNiY-qNI0kr6gU5Awoiup4JAxpQYE6tzTBZMK0T2ElRX_uxy11U3L_64Jfkphzqh0apXY8TH7qi7jB6zO9KzY14fn18_MDNzpNQpTzyKqOSMWWxx27jH3P8JN3frj1qvJNVsfJhTsebsbA_itgsRxwOCYDHGp7BS6iIcr7ZuzOdyaFiOMjvN70fP8x3-Tgi15YQyi8yIZCO15MxNMT7uXJZ1ThiH61WtnKBnVbxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
این دخترای مکزیکی چرا اینطورین، ولشون کنی همشون از توریستای جام جهانی حامله میشن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95845" target="_blank">📅 14:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇷
🇪🇬
تلگراف
:
فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم رو رد کرد. طبق اعلام فیفا، هواداران می‌تونن با پرچم‌های رنگین‌کمان وارد ورزشگاه شوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌شه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95844" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=bWtmTWPVLaNYFvdeIb9qXQ4ew7uI9O5QkCgxCuRt-gXm0LRJADo4hdirMVu5MccsbAYNVIOdydSTP6f22SqxVHaRyj8i6f5f_EjSA9K7Jt_W4r8rB10pPcpUqwnJMWQ98sLuGMBlue-U7q_f40eP4hmEiwzjvR7fawRfw4j52P6HW_WeIdLtudkXz2rotx5-4pJIPT6Jvf62-0KNATauXsz4T3pyI1q7swND0LsytJjnjT62xiKz4nRtVwpOddb3pawGdpxltXlcyPV6f5RrRM_P70sx3eaVwFLPs2Im--FVgLlQIX5Nona2eRqxupX-ScK3q-vgJPPagFBpzXbEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=bWtmTWPVLaNYFvdeIb9qXQ4ew7uI9O5QkCgxCuRt-gXm0LRJADo4hdirMVu5MccsbAYNVIOdydSTP6f22SqxVHaRyj8i6f5f_EjSA9K7Jt_W4r8rB10pPcpUqwnJMWQ98sLuGMBlue-U7q_f40eP4hmEiwzjvR7fawRfw4j52P6HW_WeIdLtudkXz2rotx5-4pJIPT6Jvf62-0KNATauXsz4T3pyI1q7swND0LsytJjnjT62xiKz4nRtVwpOddb3pawGdpxltXlcyPV6f5RrRM_P70sx3eaVwFLPs2Im--FVgLlQIX5Nona2eRqxupX-ScK3q-vgJPPagFBpzXbEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
کار‌جدید حمید سحری به مناسبت تولد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95843" target="_blank">📅 14:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcnPGg3WRnWBWQT9bTrrQ6S0nHnHxjNGzjdjDCGiC_zPHzRu3UFIwq4lgvpuIcLsg3Y98AEKBWCW_Ksz9YCaM_p_WB1gXPOzmmXsVRL7mCFYVm2hQDIbSAFD2nwDl7SwFbJ9nQ_s2VHy_jUItVbAq_Jkj65e043BBXDwBCkjhqvO3nqEihaqAIMGCRFVFRMwB15xt09sSzyN90Xo1u6GOKb02MHztpnzpO2Ogle3VOMymx9jrYI-bQZhz_xBqVGrmx-jVKkNLaZCGCVkXd86eZDHUQxPiii8BZbF_hmpMDSLpfo7wJvI19eD4XCG7bwTDEfAnEUh3-8_D_Fy54jL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/le6G32TIdy49JFOV4DqiIOuAAORLXYhju8oJlYCdgv-vmVj_MqAvox-0z1Cu_kD1yU8upuKSODr-LPaS1c-_ubroUtnXNaU1AFvuLo2BhszWNBFHLAhcSi9HlA5kuMICFTWEYtiFCwmX-e4alS9EJApktV74Pj5Y26oOM_XtdJaY9H5cq6jsq1shosQlYKfAu9If8sztktNORI5_13xrNbQIhWSHf0rxiXcYefjSjoBRPEkHk2Nx2sH9dgCB7r43sHGwpzz4c8PHt3b5VqBJNFIOObHmRJ-UcUC4BQ3-i15Eq0W1bOU55yvvyb57btOyEvSOy5hpmjuW1TWWkrUAdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95841" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=W44rYk7lqKYudgdq3MYJiT55D9IZj6pC-Z9Ll2vH6TTnYcOHY96FDsqnGXsW20nXCIAgs2ckWZAluJKFuhxCEHoFhKy1FmYRNvOzmvnKn3auW4HN-0kdSSEP9mo0bMlxROyz3wKS8dMcJu7ZEt9NjZGYBJvjAbEy5gXu6CqVkYohFsAAlB72AGxWZ_nerX32-GfGMxLp0GygFatN8dFtu_ONpRFQdCEqgY4qy9xbOayqxke74uu349NDov42opjdf8elTNUE14-eGIFg207NMudd2ek3DVABd8se6GMIdprDvHvDdfjTo36JvN2p9o2PxlHkzm9Rg07AUiGn_IejDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=W44rYk7lqKYudgdq3MYJiT55D9IZj6pC-Z9Ll2vH6TTnYcOHY96FDsqnGXsW20nXCIAgs2ckWZAluJKFuhxCEHoFhKy1FmYRNvOzmvnKn3auW4HN-0kdSSEP9mo0bMlxROyz3wKS8dMcJu7ZEt9NjZGYBJvjAbEy5gXu6CqVkYohFsAAlB72AGxWZ_nerX32-GfGMxLp0GygFatN8dFtu_ONpRFQdCEqgY4qy9xbOayqxke74uu349NDov42opjdf8elTNUE14-eGIFg207NMudd2ek3DVABd8se6GMIdprDvHvDdfjTo36JvN2p9o2PxlHkzm9Rg07AUiGn_IejDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
😛
سطح اعتماد به نفس بلاگر نچرال وطنی: فوتبالیستا و بازیگرا میان دایرکتم؛ طرف باید ماهی 300 میلیون خرجم کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95840" target="_blank">📅 13:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9758eff507.mp4?token=YCxlgmCDNHRBNZghH5OJggHclbEEYYsC0s3zvpBWuDknvNR8mmKi8JuGxchN_70IDI3Sn6HuvUQ5McFicQKBKH0oARmZYnQtFUtt8jXJaPJtE_Nht1jBhtQ_CkJXfqSiWgu79H5PwynZTSR2i3qLsE7z3Kr2W6soWslSC6uIVvRuCy2fJ041hC7SyXfaqIkpzEfDE50Fz82jAwo-QfAaVN_spX-2bKKdps9SHA67XJdSqU3svdxZ_07ZyilsX69VuqrkourLuC0OuktCaZG9SxqkP_mrXKiA7vGwilMQPXks2rcmB_81gfcBJYTygcnvT0tmG6p4TEbatm4AaD74JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9758eff507.mp4?token=YCxlgmCDNHRBNZghH5OJggHclbEEYYsC0s3zvpBWuDknvNR8mmKi8JuGxchN_70IDI3Sn6HuvUQ5McFicQKBKH0oARmZYnQtFUtt8jXJaPJtE_Nht1jBhtQ_CkJXfqSiWgu79H5PwynZTSR2i3qLsE7z3Kr2W6soWslSC6uIVvRuCy2fJ041hC7SyXfaqIkpzEfDE50Fz82jAwo-QfAaVN_spX-2bKKdps9SHA67XJdSqU3svdxZ_07ZyilsX69VuqrkourLuC0OuktCaZG9SxqkP_mrXKiA7vGwilMQPXks2rcmB_81gfcBJYTygcnvT0tmG6p4TEbatm4AaD74JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کریستیانو از این‌شوخیا نکنین
😁
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95839" target="_blank">📅 13:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSSEay9aLRJBlcNXLxghD4JYyAEVf_-Yph5yhHiFbJpWOBCdv4Z-QQbgnZL_kFmb2kXMdMw4E7IXQBEtmqaElU-abzOytKWYYtnqE-QQ3hxG4XXwbQ7Nkm7r8TWxxy4QG6pBVlPAgJIRBJTY8_h2offruFHEtzAz3TnF-UcvAYROv0VbuR7H038cLhxrzkq-KUbH182S9VZw1Gayc2SKsaJPmejrXSVhe9mYpevsF1cevjZYp3t4ZBycw3z-y2vK4aQzic3072Us_37Lzp7eQds_Ve5XDwTeCJyIQBRoMDwWvt-W4OHfDxuAGc6hBOHg7YSDHK1vyWvDaaYmOpCxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
🇧🇷
🔸
وینیسیوس جونیور
:
🔺
کارلو بهترین مربی جهان است، و می‌تواند بازیکنانی که در اختیار دارد را بسیار خوب درک کند، او کاملاً با بازیکنان سازگار می‌شود و بهترین ترکیب را برای هر تیمی که مربیگری می‌کند، انتخاب می‌کند.
🔺
او به اینجا رسیده و فهمیده که چگونه باید بازی کنیم، و من فکر می‌کنم این موضوع موفق بوده است. او در طول مسابقات بسیار پیشرفت خواهد کرد. من معتقدم کسی که مسابقات را بهتر درک کند و در جریان مسابقات پیشرفت کند، برنده خواهد شد.
🔺
در مورد نیمار، بدون شک این لحظه بسیار مهمی برای همه ماست، زیرا الگوی ما بازمی‌گردد، کسی که همیشه مبارزه کرده و همه کارها را انجام داده تا اینجا باشد.
🔺
او پس از مصدومیت بازگشته است و امیدوارم که به پیشرفت و بهبود خود ادامه دهد و در طول مسابقات به ما کمک کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95838" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9Pktg3QtTL8L-RucVMHwe-xhFnTFV76gmfOwqejUCf3tA-3RxBwtod-dX1ZuiwdoHtxSps-nOS0w-3RsdPEkft3Q2ZH5zOK9nuO_X5K7yGAP-JXe_14iVY0ebNEkAdVKWmFYS-MLeiREh-JAtaL91_ANfCswqs_J2kIs01sNAsTlnIX6zyTgs6fc1nirQbxqpSlkDzi6Fh2WI4fd9FAsR31YDQBbPJJGknz8hvjnn_aCpcmwkmGKQQTQeKcjbvUeEZ3CYU-O0FsIO79ErOZJbf8ahMCGB1STrRj77jnFoYFo9cbgrLIEI9gQpz1a-lyiqzSrY1E5_GP7jPO2qOKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ترکیب منتخب گروه A مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95837" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=mzqrqFhw33MaPbxGDVb6waXIj6N0x6vS-JIYIQTVUGDqgXlJ0lotfl7zBIc0RFKsvaxw7fGphpZO0cCT-izHhVcFDQoycPK8K0IaU0SkaE1PVnjGjPLcNJXOAAQ5WSs9hjlcFHpYP5ESMUifimJeTBnvnWZ3LvH6HM7mzOrCwLQHM0Z2aw9aKwoJGGB9ElDn-uBhUgPdtO0XoDmbMD9SmhoKSZ72YxQdlLfuBirHZqS_SnnmzualePlbsA8BKv6lC22O6VV3J7RScZ89yDLThgMcqJFLyLMaLVh8ZVAL_zkJPGxyCrDhwBKzp6apA1clzNd5JGcs2dSD09Z-4MB3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=mzqrqFhw33MaPbxGDVb6waXIj6N0x6vS-JIYIQTVUGDqgXlJ0lotfl7zBIc0RFKsvaxw7fGphpZO0cCT-izHhVcFDQoycPK8K0IaU0SkaE1PVnjGjPLcNJXOAAQ5WSs9hjlcFHpYP5ESMUifimJeTBnvnWZ3LvH6HM7mzOrCwLQHM0Z2aw9aKwoJGGB9ElDn-uBhUgPdtO0XoDmbMD9SmhoKSZ72YxQdlLfuBirHZqS_SnnmzualePlbsA8BKv6lC22O6VV3J7RScZ89yDLThgMcqJFLyLMaLVh8ZVAL_zkJPGxyCrDhwBKzp6apA1clzNd5JGcs2dSD09Z-4MB3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🇲🇽
هواداران مکزیکی این‌شکلی بعد گل دوم دیشب کشورشون عشق‌حال راه انداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95836" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/95835" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95835" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpTzQAtew7eda9ItDlLtIEd0ZC-VlWJGJaPM5b7tLtCF1_DH2wZzdeLKfCoC52IokkY5G6Cw03T-pI9OgfV3DBhyBrqhhydysM-3yLnFajrs-fTs0s52nOK_uNrAy10zVEhzFyRgQFCsIi7SQdXSlpmfhq56dGqs7sZOjnABzxRT-JD9iLSXdmm6LH_-0ZODHl_yvyBxdpGCx07Qyu3BQQlyN-LqAD2fZJJ_UaGQj1_C-G58xB_U2SktzNzwTHsnHk3qlflLZzNZnS7JdsA9g1QafTkWmEZa1BEGHhO8lmtZB6mzFkEalB1ga8hNgjn_ptnhK7O1xUHsWaMLWmmsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95834" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3soYolMU7XbeBXBrh-yngcOErIPuZdihpDU1gNaHRzEEkrmru5yDV9fE1OA2YD8KDw0dnRk1f08GDVtVhbUSJYnkhgJwSbPIwDv_T2BMEvQ2xF8JxjVInvYS0DBF70fzynY9uHVAL6iZBzAX8lMc8OhBHGwu4ggtTynfwAvAkNoWo3uabGcJey9LGLQ9ZWQVk6KKBTfVItRzxDdA7yijQEqdjTXlRd3NuBpXbOekJIexVtcK4Uc_xc1gQWl1VB7XcYmmAW0oTiBQpvzgK2asrh-ih7d3d_FUZx9itlm-4eLarA7YjN_-mouRCMrYvD-YkFtNvxHNc4KY2gm06nimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع همه خوبا امشب حسابی جمعه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95833" target="_blank">📅 13:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=B8HzFu58RB3O0xRpqIb8n8JhPpBA_wSgbWPNIISxTWNj3H6IcGkBh93cu025p0oh5MQgkvcZem4DcWWBoOTDRssRo2Bw6v8zI8o2P_ZYZZwqEh5YEk0N8Ot7RSd9_AvM2ckfZ2vEDW3KACJYFTBIw1J0o491r4kbwbpWQzeFmBhZtcYRXumw67sgwsbxjTohzp_R8S0Ksf2UcKlUKuG35UK2Bbzt-XP40PMCS1dIGOcbJyBgwNvwZVwk7-gQneuqXtX1YhlSZ3BAxz_ySEFP77wC9MDJLNgxPXefjfT5_EH6d0lnpP2u5xNMIy0YQ1mvlqhUDPep-PkPS4zJncqa6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=B8HzFu58RB3O0xRpqIb8n8JhPpBA_wSgbWPNIISxTWNj3H6IcGkBh93cu025p0oh5MQgkvcZem4DcWWBoOTDRssRo2Bw6v8zI8o2P_ZYZZwqEh5YEk0N8Ot7RSd9_AvM2ckfZ2vEDW3KACJYFTBIw1J0o491r4kbwbpWQzeFmBhZtcYRXumw67sgwsbxjTohzp_R8S0Ksf2UcKlUKuG35UK2Bbzt-XP40PMCS1dIGOcbJyBgwNvwZVwk7-gQneuqXtX1YhlSZ3BAxz_ySEFP77wC9MDJLNgxPXefjfT5_EH6d0lnpP2u5xNMIy0YQ1mvlqhUDPep-PkPS4zJncqa6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🏆
روایتی‌جالب از حضور روانشناس خِبره در اردوی تیم‌ملی برزیل و کادرفنی آنجلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95832" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnUzCoOiZ_Wm0WlS_ubQbMNV2zx9_NlTo7MsA1YBOSTP7X9fqDhJ7lgCglNNPOZJrKcufABGRnJtmHettmkmWmcx6kphsNheVHYJt0HGj0WmT3Oiztw_zo8jDg1W6F9sfoedAOGIrEHljZOI8L3GgU78NI0vp1zkwoq3Uj-RGDtWqgOY7e8NAjlsf5hA7nBGvCT6-Z3z7APdf5_olDyLp3WnTLnWS1QkuR57yCkrlyIjs6O-H1gOgCYiLckeyTonD7WRbQ5NyGueMGZdjNDOIlv26dZRAGIzLE7eAJHpl4j1xMWQIHAzE1-d-7BpJlV5c172c-7yQHOjRPnk_37OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد گل زده رونالدو با مجموع گل‌های ابراهیموویچ و آنری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95831" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcgPq9e26ZKQjMsrt3Mgi3aSmFuf7VkerNQowb1dQnv3CacOZRju0KmUtsIqBE07N1A16B6SiaOwmWi2V78YfnLBv4l3lYwXBKKmTB3jRditNTudAEqUQ9LbAKVCFvExivEPBO9jUP1usaKg2Teijd3DwXLI0ucYFne11ZNr6vGOPYU2NCzbhgDT6tdnP5TniB_Ft4MlEewkzIt-WPuPFI0YFgvrcOHqavx8mdy75ya-R9MvcLCoU-eBlE-hOXBM-tqthl8BWeWU7M2MhAB4379R6vpUDqvYN1Db3LUyq6Bqup7hRd5LV5Rf_mAmZYLc3zGt_-eivh2SmjkaFFi0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
وضعیت سون بعد باخت کره مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95830" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSKnlGGn8UEY3cnEHv2muecKwjrKAGaH6qoCV1_NhgGOjFr-REsJLdiI47lc7085-3nQW85RmdjfBFDmka_LeM4WSRbiMIwTdFQTHb74uNzQaJgJhEd56As7MLWb-CTR4dNJ-dBnKO3MpjXJLaX8j-rSyrD-JsgFu7W06R1TBscMUlBgAPOXkx4nBjrSL0M6nYtTSYTIH-zZ947cSNq5olvWUcrHNh37DsqieUtsNN7xL9ZLyWKvrb2EIWgNt4OwZLkFmnj48IPlasnoBsFagHXjVfbLlQYG59h5uQSX_4EIkjBLAeWYtJ3KcxMudu10rCGakYpdcEJnbRVk16wNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از صحبت‌های اخیر تیری آنری و زلاتان درباره کریستیانو رونالدو، هوادارا تو شبکه‌های اجتماعی میگن این دوتا هنوز از یه سری اتفاقات قدیمی دلخورن و از کریس کینه دارن. بعضیا هم میگن دلیل این حرفا میتونه باخت‌های قدیمشون جلوی رونالدو باشه؛ مثل وقتی رونالدو ۱۹ ساله آرسنالِ آنری رو تو خونه شکست داد و رکورد ۳۲ بازی بدون باختشون رو زد، یا وقتی رونالدو با هت‌تریکش سوئدِ زلاتان رو از جام جهانی ۲۰۱۴ حذف کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95829" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=CkhX_aTVOlHKrPK-0s_0fTsu2CTvgRkWOq-wJtvf994TZxLgZPff6_lVHOLEcAJGlRx9jlTn79_06reTQtB_2rnKKPZLJYx1rGbUYbcQvrlqAWh_Q9cpUx81ZYO_C2dc6oleILtF1bTT_T7t4P91EMgPMIHuOhDOkuWHaF_h7fhKIKrnWnBl7wE4trO_UnNqosGShl_2B7HyZOxYMm_oZ1a8wPm-Dn0K2wEuFhe-EfudeocgYszeD5OU_Gl9pvvlv1Q8Eevd3J0o-dexYjF0Z5vq_nPUhOT59g2n54YYYk8B7Wpy508rs3TVxyoRgkLATXMOuKsr7tQzJlA6XhvCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=CkhX_aTVOlHKrPK-0s_0fTsu2CTvgRkWOq-wJtvf994TZxLgZPff6_lVHOLEcAJGlRx9jlTn79_06reTQtB_2rnKKPZLJYx1rGbUYbcQvrlqAWh_Q9cpUx81ZYO_C2dc6oleILtF1bTT_T7t4P91EMgPMIHuOhDOkuWHaF_h7fhKIKrnWnBl7wE4trO_UnNqosGShl_2B7HyZOxYMm_oZ1a8wPm-Dn0K2wEuFhe-EfudeocgYszeD5OU_Gl9pvvlv1Q8Eevd3J0o-dexYjF0Z5vq_nPUhOT59g2n54YYYk8B7Wpy508rs3TVxyoRgkLATXMOuKsr7tQzJlA6XhvCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
یکی از جذاب‌ترین ویدیو‌های چالش آهنگ شکیرا که میلیون‌ها بازدید خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95828" target="_blank">📅 12:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95827">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=lB6A3tk1tBRby0_XaAgQgnJIl3eVC5b3gaw_pMK4m6DL3fTXsyzVn0rx8UPKU3EzZXU9UuhchW84QEHcSBmQFsSuaiNBEwEfBeP8yFpEscGU9nX_7BSuvB_WZfVKUNagqgX7a86RnsN4WRBcVZZ9Wl8pdPeVVONZ8cnAd2e4hLyKqo2Mq8-A6ts4N-PEdw2vlGTsx1h337zCvkoyOgJtfKkRHaD_OT0SFhtWI_YuQ6Wk8GQeiA9hNaUNBWtFqgkrysQ3azIm7dZMAyet0Q7kvATzxKfAyelXY1X1dbGEyp_vri1mPnAC9drWIzi13rw4pAVB2KgwdF534lf84h-MAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=lB6A3tk1tBRby0_XaAgQgnJIl3eVC5b3gaw_pMK4m6DL3fTXsyzVn0rx8UPKU3EzZXU9UuhchW84QEHcSBmQFsSuaiNBEwEfBeP8yFpEscGU9nX_7BSuvB_WZfVKUNagqgX7a86RnsN4WRBcVZZ9Wl8pdPeVVONZ8cnAd2e4hLyKqo2Mq8-A6ts4N-PEdw2vlGTsx1h337zCvkoyOgJtfKkRHaD_OT0SFhtWI_YuQ6Wk8GQeiA9hNaUNBWtFqgkrysQ3azIm7dZMAyet0Q7kvATzxKfAyelXY1X1dbGEyp_vri1mPnAC9drWIzi13rw4pAVB2KgwdF534lf84h-MAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژروم‌بواتنگ مدافع سابق بایرن‌مونیخ: «مسی باعث شد فکر کنید احمقم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95827" target="_blank">📅 12:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521d31d087.mp4?token=K5szUh9xCWf6IvQS8-issbgGFG_lwNevBtlUbJ0j0_dEY8aRgXycmsOQ02bXYuBIb0rulqg_9J7IVUHcuCd5QVD10aaOx_Y2REv2uI6l63uGjB689HIhBAGq6qlwqub3AkcF4yRwbDTVsXIqezNn8geJ8w1mxbPZnrgymBRKBAjZkrp2ZY3JyJT2Az6HL7oIsVIAl870Q-7hdvopR82aZZ_gUW6roeHIKeB-E1510DfiFXqtjN7BjC2kxUQLXPJ6jDxnZn6KTlf12DJwb7yIV5hkkTM7YDlUxeU_Q7EQX2U6Sud_0ylqNulPnHZj63aIzOHrEFs3JGRWPd6RJ6tjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521d31d087.mp4?token=K5szUh9xCWf6IvQS8-issbgGFG_lwNevBtlUbJ0j0_dEY8aRgXycmsOQ02bXYuBIb0rulqg_9J7IVUHcuCd5QVD10aaOx_Y2REv2uI6l63uGjB689HIhBAGq6qlwqub3AkcF4yRwbDTVsXIqezNn8geJ8w1mxbPZnrgymBRKBAjZkrp2ZY3JyJT2Az6HL7oIsVIAl870Q-7hdvopR82aZZ_gUW6roeHIKeB-E1510DfiFXqtjN7BjC2kxUQLXPJ6jDxnZn6KTlf12DJwb7yIV5hkkTM7YDlUxeU_Q7EQX2U6Sud_0ylqNulPnHZj63aIzOHrEFs3JGRWPd6RJ6tjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
امباپه: «کین، هالند، من؟ بهترین لیونل مسی است، همراه با کریستیانو.»
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95826" target="_blank">📅 12:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00614f2668.mp4?token=H9tVwhsRx6MbzSmym4ke3pPJHFtyJ5Z-v17TQoZmj6ojx3LRo3RUKLLEpj89UvZh7RoqPsFPeQazPCag8QxdM2FQKH4wy-yIwchFkTlk6KYEXjolQGwvbTtpK2ykUJGkloZBIiPrhqxHSS9JMjWx6WFiJvgF6CmU-evt6i_WbXb9QQwXaoT3cFETqNYajnHkUT8vmpzaZLtetE948Lv5oR_FE1Rqu-66ARD3nK2pfrxq5I_hTPkbwb10sHFinhaJih_aLzQq2lyZr8pJFMohlTMZWBJZnH9VA0oxD4SexGNwEQtYiLQUwvY5TSyA-iVfKs0uswqIuGDcmIgInr1D9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00614f2668.mp4?token=H9tVwhsRx6MbzSmym4ke3pPJHFtyJ5Z-v17TQoZmj6ojx3LRo3RUKLLEpj89UvZh7RoqPsFPeQazPCag8QxdM2FQKH4wy-yIwchFkTlk6KYEXjolQGwvbTtpK2ykUJGkloZBIiPrhqxHSS9JMjWx6WFiJvgF6CmU-evt6i_WbXb9QQwXaoT3cFETqNYajnHkUT8vmpzaZLtetE948Lv5oR_FE1Rqu-66ARD3nK2pfrxq5I_hTPkbwb10sHFinhaJih_aLzQq2lyZr8pJFMohlTMZWBJZnH9VA0oxD4SexGNwEQtYiLQUwvY5TSyA-iVfKs0uswqIuGDcmIgInr1D9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پیشنهاد جالب و شنیدنی محرم نویدکیا به فیفا
⚽️
@Futball180TV
‼️</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95825" target="_blank">📅 11:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=J8Ic5Mem5Ofna8I2bkjzAHY11nKTtW-pP5Sl1YEWTgBgejhLBsO75v0MYz0ilKdy0Joshftm-H6nFoZlirRShwm87tSdit2Oj-bhQdlAvD7Lb7RzcjLkjyMZGwqSmveq4fDkb6_xIjKFocEH_NzsFAFlj4hK6SZwbzqk7lVhw2MAa00VopURWIoqGpbYXtoNWCGDlB8dtz2zS3MkCFmWezeuKEs1H4CIfxxMC8lpZjRUqGj0xE31d8wfGexMAZU_ecm1gXs4o-ihjPK5rz6vfyygG5_32sZgk_PiMS4gsmwiSJpdbpaWo6tUDareIjvRTxdHotFmIr7s4R8k8hkxsWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=J8Ic5Mem5Ofna8I2bkjzAHY11nKTtW-pP5Sl1YEWTgBgejhLBsO75v0MYz0ilKdy0Joshftm-H6nFoZlirRShwm87tSdit2Oj-bhQdlAvD7Lb7RzcjLkjyMZGwqSmveq4fDkb6_xIjKFocEH_NzsFAFlj4hK6SZwbzqk7lVhw2MAa00VopURWIoqGpbYXtoNWCGDlB8dtz2zS3MkCFmWezeuKEs1H4CIfxxMC8lpZjRUqGj0xE31d8wfGexMAZU_ecm1gXs4o-ihjPK5rz6vfyygG5_32sZgk_PiMS4gsmwiSJpdbpaWo6tUDareIjvRTxdHotFmIr7s4R8k8hkxsWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
دوتا تشویق تماشایی که در سراسر جهان ترکونده؛ تشویق ایسلندی یورو ۲۰۱۶ و‌ تشویق نروژی(وایکینگ‌ها) جام‌جهانی۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95824" target="_blank">📅 11:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1-CzcSQqev5FYaBcaWH7ibHjqiOvrtbGBn1Gt1TkJGtmL4viX2z6olMVUao21lMw2Pl7v_rPAD4TbseARYwD7CNvwNX4KzezcXhGdq1gaeRdFXPzis2LqMBmNkNYjzaIWP3gCS1Hn2Z2fjvMoZppIalOirvHGYQh92_NLUvr5lTilKWnRddtlYDH_thTULLrd9kvrJ9Jeg3UvTSG9B8L5eI5W4Xd777YpTKWUYLNdHWOdZ0kxQomSRwKO5aZMY_AUVnhXrrNqaSZT5nVdseKo9D6BLVrSHxh-Zh5Zgdmelro3mdpS8qODn2UVAJTAtgPlIpFV6dmZYBm3hyhwEczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
پوستر جنجالی فدراسیون والیبال برای بازی امشب مقابل تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95823" target="_blank">📅 10:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qscJ7ue4QUhbuOCp2zF5R761dhyfQI08XYYzO3Oq0hzaxzQGr1i6wVIBfeXwUnZYA4FKXowy7EwmeVzyH1HQQ9laVHvIRlvL-AIoTcM0fU2QsUFtSEzh6O2av79CGLLOGfXrWw4lPkcFmUWufyYXfO92tHHxK1OU9p89FtFqyFDQmyrSg_UmZIM4ZGlHdOZ2rzy2ESdMcGd7p7kVUb2fITKpjE6HKGN8WkWF6rxv1mlKesGQ1hHLEkAT__hut8IQVY2dnSYMAD_v9afBc1QGWwcsiqiMZ30qqtI7t7Gd3boxh49_0JlaGo49PL-3QH63MreRl83A2egdpzv4Sy3jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
🇮🇹
رومانو: رئال‌مادرید به کومو پیشنهاد خرید نیکوپاز به ارزش ۶۰ میلیون یورو را داده که اگر باشگاه ایتالیایی مخالفت کند، رئال مجبور به قبول پیشنهاد سایر باشگاه‌ها برای ستاره جوان آرژانتینی خودش خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95822" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx6pStcbDze7R5XIXlu3OFPkNW-gbprtn1eHagIcQicujd0OF51--JvJ5J1zaCtptj6oDbSvu3a0rZna-l-zPkGFpMWBYLfhBlggG5F_BPztEPBwsbFad8COUgDmRHiMkJbj-VQM4WxA-SdXIU3i5Oj1xeksQBpp6fTMSR75DqgnlGer7swpaHh4YgRNyKvNdSPIuhyMghm2_2QHKCeURzRnkJgpHhgiruHNy_itmwMVxOJbqw73z6CxuL623z434jhaHSklminrlIKP4DnFPCT7Qjm_TfSkyck7eRpmvD_IG5KU3Ox-pJtbi4gEBs7vS2HemxMotP7AaoX7tkIIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
احتمالات صعود هر تیم در گروه F:
🇳🇱
— هلند برای تضمین صعود نیاز به برد یا تساوی دارد
✅
🇯🇵
— ژاپن برای تضمین صعود نیاز به برد یا تساوی دارد
✅
🇸🇪
— سوئد برای تضمین صعود مستقیم نیاز به برد دارد
✅
— سوئد، هلند و ژاپن برای صدرنشینی رقابت می‌کنند و هلند به دلیل تفاضل گل برتری دارد
🇳🇱
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95821" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bywUL52VuRBXdJyVwrdcUpHtIec7pHoskok-h1sIonZoS545Bf_rfKzouGDlD8ZLDpjkIAls4U7T0CVG3foAmVoZlR33imr0GBC-n2OFNON6BQdpiDVPlPwhooY69D3oQ_ADx3fMz0yYeJcyA1ZkWMxahmnkrh7vvjNHM3ZKDIZEVQ0ufMsNuInSXysluK-X61QcHFHeb1cZYYIAuveUkVBOb6fGuvZ2Ss--AYqXb8z8FadFJJaKVPpa8ePbkXDk00-uUOsxTqetnqADIgQaPV4a2U0inPYslsuOpbt-bgu4Shvtok69ijdX2xzEIO8XhbCUeo7viEbCCTcAiOOoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
احتمالات صعود هر تیم در گروه E:
🇩🇪
— آلمان به طور مستقیم با تضمین جایگاه اول بدون نیاز به بازی سوم صعود کرده است
✅
🇨🇮
— ساحل عاج برای صعود نیاز به برد یا تساوی مقابل کوراسائو دارد
✅
🇪🇨
— اکوادور برای صعود باید آلمان را شکست دهد
✅
و منتظر لغزش ساحل عاج باشد
🇨🇼
— کوراسائو برای صعود باید ساحل عاج را شکست دهد
✅
و منتظر نتیجه اکوادور باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95820" target="_blank">📅 10:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqfKq9Flem5EWDjoZb_T8BcaA1MlZ774vbjNqZhZPV0BkKytzYB6asLPAs4AqoRz4t3KxCYFDwDoByGXmHwqwjnxOfAJljDRE6zZZwWNzl0JvNOntGn-gJSCLLBwvnFFPb78gLRUJA0b2uN_d0raAsGGCB5andyUjADCPUtVWY80t1LMVHA84t_i00ItTFFApbFXBPFQVShMnq2VBvgrXeG3gZ6GQ_ijEdTWeUk0qM2-EBwCAjL6u_wBsUpnh08JK2STfbcuVnunA6vAJkgSxLWQ3XJCk5ovMLqXU2ynPZ4EEVjIgf_L9vaI0r2NZKaGVy6lutDQM820adNCpNOVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های لیونل‌مسی و رونالدو در جام‌جهانی به تیم‌های مختلف که ایران هم جزوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95819" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=CGDihLVAOwJwBvzZc84ZeWSypxEct-zhMGaOj2drPVLzO8CqM8ZBV5ZW2qYqzn1Pony4OcDvgiT6apDfqdVjJoxWsojRdP8ZFpA0vCB0nbnqEVMW4qcn_QeJWoF8EW4vE6Y3C4iaRmuc8n6wngZns54qzWMBx2OgZV5kDgZjyQxEmiE4KnHDYTogj4nWgJluoyhls418GCDNQHjLilpHXDeDLAY1PCCupjvAKxgeULjDsEXQq5WnN0Ly_-0UShJHAbJBuS6uXTEgqXSkIbHhdABakzaq5gPADkRqb54FLrkeVeT3H7-SVNOaun26dnCuydQPAS4ECQP7VHG5Qe8doUTMfxCzRO2rFkLDHCggm_jqqCI1gMOqsH1xjExR2u3veOlejht0JZvXBJijlUA84vdaYIIsl1qJ3VRmseTKctO-fsghyTMEIk1py8pfNtoO125ppLvBVqIu1WrnUQOCss7YPkMX5a6jwcAR3y6-4vMMUReFRDtEu_8DVyQzQgB97OkpBKBBWFyfE2NfoJJhJulmOi2wXcwyPUe5KtA0ivvnXlRLxTtXyNiVEj7KPeoCCpumyZxLJg0QszMOpVMiRGjhc9FzG9_SC_63f72MKbHa7AJAmRH84vqLjocF8uIHQiiVUUwMqPOR1omNDAtpo4k6wsDdfzfArCeqTa-zsA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=CGDihLVAOwJwBvzZc84ZeWSypxEct-zhMGaOj2drPVLzO8CqM8ZBV5ZW2qYqzn1Pony4OcDvgiT6apDfqdVjJoxWsojRdP8ZFpA0vCB0nbnqEVMW4qcn_QeJWoF8EW4vE6Y3C4iaRmuc8n6wngZns54qzWMBx2OgZV5kDgZjyQxEmiE4KnHDYTogj4nWgJluoyhls418GCDNQHjLilpHXDeDLAY1PCCupjvAKxgeULjDsEXQq5WnN0Ly_-0UShJHAbJBuS6uXTEgqXSkIbHhdABakzaq5gPADkRqb54FLrkeVeT3H7-SVNOaun26dnCuydQPAS4ECQP7VHG5Qe8doUTMfxCzRO2rFkLDHCggm_jqqCI1gMOqsH1xjExR2u3veOlejht0JZvXBJijlUA84vdaYIIsl1qJ3VRmseTKctO-fsghyTMEIk1py8pfNtoO125ppLvBVqIu1WrnUQOCss7YPkMX5a6jwcAR3y6-4vMMUReFRDtEu_8DVyQzQgB97OkpBKBBWFyfE2NfoJJhJulmOi2wXcwyPUe5KtA0ivvnXlRLxTtXyNiVEj7KPeoCCpumyZxLJg0QszMOpVMiRGjhc9FzG9_SC_63f72MKbHa7AJAmRH84vqLjocF8uIHQiiVUUwMqPOR1omNDAtpo4k6wsDdfzfArCeqTa-zsA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
🔥
تشویق وایکینگ‌ها به قائم‌شهر رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95818" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=PjLCFHGyEtKa8yqkE5rfD0KnKZTE54YoIWDeojUMBMLhYEywmq7Exw7jaMyzcQtcgUR3DnCQGSE2uPZb3vKWKXfZBnjdYd_AUx8wqbvym-zP0bfVkeDRe6kxfpLRohxY3OVas6vTE9dX7kBVRXcQb74MOEfQfUb0A9rjDTnJdAv_p-BUDXtQClKhOeba5hSOuF58MhudLl3HOc34leyihMMBha9BtLKDqTl-qV8emPz8M4WwDWim9EU-GmIWdKogdAMHETMFVmk6SEcWSz5kTJDzoLswHYu94piZ_h9BfV0rTCn5-ggC60dsjaT4yzajJLvOJxX8BHF3JU_e8fMHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=PjLCFHGyEtKa8yqkE5rfD0KnKZTE54YoIWDeojUMBMLhYEywmq7Exw7jaMyzcQtcgUR3DnCQGSE2uPZb3vKWKXfZBnjdYd_AUx8wqbvym-zP0bfVkeDRe6kxfpLRohxY3OVas6vTE9dX7kBVRXcQb74MOEfQfUb0A9rjDTnJdAv_p-BUDXtQClKhOeba5hSOuF58MhudLl3HOc34leyihMMBha9BtLKDqTl-qV8emPz8M4WwDWim9EU-GmIWdKogdAMHETMFVmk6SEcWSz5kTJDzoLswHYu94piZ_h9BfV0rTCn5-ggC60dsjaT4yzajJLvOJxX8BHF3JU_e8fMHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لذت دیدن لیونل‌مسی در جوار دوس‌دختر که ما ایرانیا ازش بهره‌مند نیستیم
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95817" target="_blank">📅 10:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=gSr9HeI3sPjwydR2kydU6xlw8j73x1A9YPMM6Fb7z6XuilwnkpyCvwKtS-H0nVcHV5oTuYF0x9l9cpJ1LtFBSAos-HjDye9QAOAbXjPi0PVr7SCfB1Qk8g6EYCOrzi8Pe9gundw2cYwsNbJvCEoSpcKwCV3TaXdPklTx6Srr0l6mT56SPFFSYR8BGjUdIbuQMvsRj22Rh0bwBdxjiiF1LXyxqWUZJuRfgm52AcroCYCm0GJ1SdUJo32s9Cm1OSOB-hbfY6jRsITBI-aU0NGispUUzKOtOq28l7_sKEPUaOJAzMIq3j1ZHXTElcZsZxdI3kdCzYhy7rBvw588iIZztgUafj44HAh5Nk7qHczoYmp2iViktGiTV4m7gi2X_6l-xZC-ugY9aQzJOpCt4jBnXGt0Hu3MfOnsCgMgzLXeNoXMN8bO84Pb8PmDGLsHt-dKaZHpE0Bl2kMbJ57H0UUZFNMnJH3cQNJ59CGm1ZIQVAj9SyEz91UWErmow5YkMRi0OdQDuwsVSy-eLMc2hynE-jjMehZxMcQpjSJG_DVjBfR7Kpjvae5SpB7SVLvRaJY73fqZCrqokXf0Jo5ulmu4m8UWpDfzz4-0HsqE-90t6ZjIaW1F3v4EBTp6mdeM1aDeGInkoVamnPcs4h13IyCKQpPCPL7amVOfjt8UbVgxO4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=gSr9HeI3sPjwydR2kydU6xlw8j73x1A9YPMM6Fb7z6XuilwnkpyCvwKtS-H0nVcHV5oTuYF0x9l9cpJ1LtFBSAos-HjDye9QAOAbXjPi0PVr7SCfB1Qk8g6EYCOrzi8Pe9gundw2cYwsNbJvCEoSpcKwCV3TaXdPklTx6Srr0l6mT56SPFFSYR8BGjUdIbuQMvsRj22Rh0bwBdxjiiF1LXyxqWUZJuRfgm52AcroCYCm0GJ1SdUJo32s9Cm1OSOB-hbfY6jRsITBI-aU0NGispUUzKOtOq28l7_sKEPUaOJAzMIq3j1ZHXTElcZsZxdI3kdCzYhy7rBvw588iIZztgUafj44HAh5Nk7qHczoYmp2iViktGiTV4m7gi2X_6l-xZC-ugY9aQzJOpCt4jBnXGt0Hu3MfOnsCgMgzLXeNoXMN8bO84Pb8PmDGLsHt-dKaZHpE0Bl2kMbJ57H0UUZFNMnJH3cQNJ59CGm1ZIQVAj9SyEz91UWErmow5YkMRi0OdQDuwsVSy-eLMc2hynE-jjMehZxMcQpjSJG_DVjBfR7Kpjvae5SpB7SVLvRaJY73fqZCrqokXf0Jo5ulmu4m8UWpDfzz4-0HsqE-90t6ZjIaW1F3v4EBTp6mdeM1aDeGInkoVamnPcs4h13IyCKQpPCPL7amVOfjt8UbVgxO4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
خوش‌وبش گرم اندریک و بوسیدن شکم همسرش که بارداره بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95816" target="_blank">📅 09:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=lRPNF0M06FRxvhPVPDrtwDiXgN7PthzOVTpNhgZsR7rV64b3gXL_gpyVRgz5zZafURCX1JpDQfJTT4h8UROlEwQCQb-OGNImCwcmlqzsWG_QYVUksfWH3MJWZgucwlZjJna1Yjvi6UR10-ADe0a-rTlSXSuwRr82QhDiV3ljLJEkEp7SDvZ7g4iOZ3IX0-wKrSEGM6OEOPb52ENgnIDXASv9B63oQNkKfzc4XjhNH9BsVOWJqJkESUqGcvLRVHL9qe1T-CSVFzo8HUMYWEM7KBKV5CC0ykIZbNJd3l4P4KZ-kZ6HcMqy16tw4mPCy0tnktq4FaYFlWPS7Z6d4n8kqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=lRPNF0M06FRxvhPVPDrtwDiXgN7PthzOVTpNhgZsR7rV64b3gXL_gpyVRgz5zZafURCX1JpDQfJTT4h8UROlEwQCQb-OGNImCwcmlqzsWG_QYVUksfWH3MJWZgucwlZjJna1Yjvi6UR10-ADe0a-rTlSXSuwRr82QhDiV3ljLJEkEp7SDvZ7g4iOZ3IX0-wKrSEGM6OEOPb52ENgnIDXASv9B63oQNkKfzc4XjhNH9BsVOWJqJkESUqGcvLRVHL9qe1T-CSVFzo8HUMYWEM7KBKV5CC0ykIZbNJd3l4P4KZ-kZ6HcMqy16tw4mPCy0tnktq4FaYFlWPS7Z6d4n8kqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سلیقه موسیقی میثاقی آپدیت شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95815" target="_blank">📅 09:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=acS75cBHN8UEykFVf8SHsYqp-rNG9yrapvNdVbC2DhT6bCvMot228h3X3KcYWW2ylgP6VFadUlqh2kWUhGUdrJYoJMBSYvTZWQU5-Ui5ejfCa53dV9-0B8iXJ8Uwv0iHh1ZmjcUULN8_NdMnzqjIq3Gwbg4wi95hWlyj2HzAIZJXUEJTEiU9cz7W5-Wj_4gmKcfnU8rqEQanvPC08jpfsJSaCnb1X_ctLQkl4csg53odqxNa6Uu201yPDN27oxgMGzVvd6cqnyyHNO2t__Rjvh4HVY3SzxntOEGLYMFh3jH_CSioF5FUnnHvKnnw48lW_lMIPrakaD2drr0K0IX1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=acS75cBHN8UEykFVf8SHsYqp-rNG9yrapvNdVbC2DhT6bCvMot228h3X3KcYWW2ylgP6VFadUlqh2kWUhGUdrJYoJMBSYvTZWQU5-Ui5ejfCa53dV9-0B8iXJ8Uwv0iHh1ZmjcUULN8_NdMnzqjIq3Gwbg4wi95hWlyj2HzAIZJXUEJTEiU9cz7W5-Wj_4gmKcfnU8rqEQanvPC08jpfsJSaCnb1X_ctLQkl4csg53odqxNa6Uu201yPDN27oxgMGzVvd6cqnyyHNO2t__Rjvh4HVY3SzxntOEGLYMFh3jH_CSioF5FUnnHvKnnw48lW_lMIPrakaD2drr0K0IX1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
🇵🇹
فداکاری ویژه کریس رونالدو در دادن کاشته به نونو مندش و تعریف این ذهنیت از زبان هوگو آلمیدا؛ تیم > فرد!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95814" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txGzZ5FdS44iRxLrtpt3GsGut1SUcyjUYfq5yTlTsd7qJrL58rkRrsR5FCLDMFwicoy7HLZLvp_8ZWa2jAr7XwNb5DYDlsjEhqPQDIJLNXM7tK1WqstvrZjUVd2DUDg3tzHwmpdzJQOQnWquMIev5AzuNXig4my2U6WeCsZu9y1uVyk-rtQyrag6la4wJQ__DZghx5Vy5mUi5QswXJT9ipKWz1eRAiOLazMrMnbeMuJ2UhpFM5fqBw4JtZhZ3TuBIdOFm6rGgDuSQzBV7xINc7OB-Yg3-TB2woBsr8NeyC7-KG77CxnCv31YFN4KKcMRiSPTUdRavrpB205Cy9-J9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار درختی مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95813" target="_blank">📅 08:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzn8TsMIs55oxKDje75iS4BkPOzXl99UvZFLf0ncWyZlaEatr4EkHY5-Mx-15-7duxc9wu3t6sRjocfZsxKBAu4gGhmNCzO3dLQnei0uM7tu3psQD-g4nTb-9PfamneezGJwuf3gjFVoYyO2Ig-UaZaRnzN6DESG5qTMUU5II29L54uxAm7CzEKIZgU5KvUOOW986r65FpgTpZfFTXFwMJN9QMQEMVlwccxnBFltpS2qfrvbxOlgGWTe0r0x0E29Yv7wtAhItAZoIhL7Pk6iu6kRlIK-VMOXiwawqhNriLTYx0WLPn63XX9lvVk-I5dBE442UgIBKyVEaYDRuc240g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95812" target="_blank">📅 08:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwsKkEjyUD4XonTwzFKgBfeUrBiRw6UHw1gEimBWfhCwiUMXD5BoNZj8Is9XEu6yuCnZ2MxjXKqLcdDCG27oK-46dnLXWgg7hB7_pGfW2tiB15wYE_pdD8YX53ZOx9ym1aEBBwwCm2b0wLGBQsDZf-C73UIDEnmpxr-nOj34w7jNTrsMy41NGTY_HAcbZLzHkNVdbDttz39F1ktogYS4TtDI7B7TbFtfSL51kLXdgLLg4ywFyNduryOKbJR9aOAgLhn618KVmfyU9xJiISZbNfRmP-X5NrnobGo-_62qNtJMF8bTatA4299wP28HP6f_f4zQwexl6wLOvZ037iwzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95811" target="_blank">📅 08:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پایان نیمه اول بازیای جام‌جهانی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95810" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCuy5g2pbZ1LwUP4qFp9ZC8aT7T5yWZY3dDTpPrhzb6oUaXmxhGXI5_n8zxUQQw9y-2REbmHFzNIeK6_IDj_qjit1fPr0j3tgROEDU47bl0JrdtaU9np40b_13n0uJtJGE3UplY5jpb7_3ORHxkvsKQKRxCiE7nRI6_Yiw5Ip_cZ85EYyEp31mt-LCOjFqq7_QzBBK0mVOJB_N9HT5e2rByk-VBobBZDIkw7zSO-hcBYZ6dfOtTWyCnLV3Y6TtvOurn_Dc8KEOfhXlqxVL93C3VVk8dv1FY9aXo06WgTj0BlRoyDkGuoFKQMY_Gvz_W3tFLXMNsFzYwr_i6UMR36og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbyregvtq2C2wreblrQppn7w16y8swZdtVw72VI4sbhNMiqN3Bcm8RPTh_Lpxwpp3vZk6hMBEwksZnoMt7ULui3n9MynR5Lvxw1s6tjJL_0rbtuBbrqivBEf180tSW9gKygR4noAfNby23KMmwgxAl7x25UXp6iRRu10zw36Zccx_8LPnhFRzZhFMioK10_t3JxVZLov52-8I8cmig3nBFspqumukE7kH_stHsZW2Y3r3kb3WoueMFynzdgg2vpwyWRxfZFElr9vSgIl09lst9OVco2_SjlLze1wGPTgjjcOdRZfZ-q9FsiWtrUwRhGds5EpcjpLem3taG1h0oVDSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
👀
تعداد گل‌ها و پاس‌گل ها در جام جهانی:
🔹
وینیسیوس : 5 گل و 3 پاس گل
🔺
رافینیا : 0 تاثیر گذاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95808" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3Jud_2hV_ORmARqSufLIJwTgnMUQ_kzA2fpMDbye6E8dcP50S29vfB3unUrbs8MJPvRI27Co2422BSiQj7VOjyJYI-cS8sS2WShm2r_KcT44rfHstzuRTJ7tBCnuThZx4AsPwCgwleGp0RtZVySP02L4lfunJtWat7t6S1Yk8Gq4tayVBWVNp6CoLrg_EyiZXSHne-5THK9HJHvGeRZ0hny-HQPhD16PeYZEuHo8Twq-9St7DNIRf9iinL3vLOatFshiYz3IeQW7sWFYiNUxf93rXkjx1AuZ1A9UxNrVtWeNcD0EGODdN1Ur7r7Og5LqQJRdilgGNg14L0kLtMY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای بوسنی راضی از برد؛ ما هم قطعا از برد بوسنی راضی هستیم
🇧🇦
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95807" target="_blank">📅 04:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5mZReOFLsF-SDmnkr8MBNff86XGezcqnGVi5o7mHcVyBIOGmEk67kLRdUSv3PmrlLzIobMHmcUp8Hk7d-T_kz6OqQ5qM1XpUCr_gG6t7vVVu35cEvpc8OyPWyAe4kxwAjMVNrFTVOKwxzISfS9-VtnM0udAwa_gLgh4N1FDaYkBaZ6TFphlc2xqObnDmddnbfjWk79uMDXWlvd4IJ5B3_Zn5SXeaTX-gE8dvGXp6anrHRjSuVg045hX0z13qXV-Qot6K9a_PnYX8pcZ2rzJ0a1Dm1VBDD0-poYuaVPELKD7DBKA8OXBEWPUUi0Pdg1WgBcjNme_2DkRM3BqFbOvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbYv5gVu6pU2VpQF_pwhBjrEGnIB_Ci3IEekUfqr8cFzWCmTsgAaWhIULdnWmx695zm5MnUiIg-2KfDGL6QjqCSJtNxi5j0nq7ys1iOokTljvxvOzvKYHQAjfSJfEZ2DhwtDjGrX549Pb8th1HdRl2lyLy9R69ZPKnkIrsqbdi_A3iREXc7kmKYAhXETnAA08krWxPLmuqY4P6PPuSGraywzhRPPxATCx6N-v4NLCfujpzBScQb3kSsMZCcDZkcVaghBt7aSnjTzsPB921vyJBKf0fX6Ero522jMPxjIvPALv4RupLRRthbjCbO6DzrXQwgC6yMELB4_tQVk5-BH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujOqRdfbTWZAFqIcKv8Dq_jPGNqLarHKRkH2Usj2BzSicUPmR3eePqLLU0AchSS3pdtBiOlc9w9TUzWfxB5O22VUT8M0WKeWjEwofJqbbqOQpqOCxAW5qSBT-tb27v9LNlUZC5XMCc9WJr4GBVnWBO9FbOwSq0YBFkA-1Vap7K11si60f8_CNoaAIIYHj-pYIoWvCzv4_zql7HidCC5dbGU5gg-77bByThIuOxBN9yZfy_waK_fiKlgcW38UICo8TL6TqoZYEs3_hnF3OkEWmCATQC9gwqPfpFRWePc2CYCCIVBbQN4ciO5a4gWN6_91XrOk8kzIPSzjtpEF6U-Wqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشک‌های نیمار بعد از پایان بازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95804" target="_blank">📅 04:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شروع بازی های آفریقای جنوبی - کره جنوبی و جمهوری چک - مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95803" target="_blank">📅 04:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axPNnsw5ec_0z_2Tr_xqUgMrclMtUuZ4QWe_JbxGCjYDc6DHYHcU3FKvofSiPUtbP6etjMT9d0fxSbHoqkUUE5AakCtqo_L7MKM45Wxb-rpMbf1laKWg1nPKpTF95hxeBiildh0m3i8h7efS81LriE0WBzp46-1oeMqJC82akiLozVCNVBDItAv0LmCJGDgLLABFExPOtgt4lZnfbEK9rPD3JKYUUR1ooYUlOJ9TlYJbG5ES0kZlovrRWIL469Y64y9UKQ9aJrv6ikJ00BHgaJ7gcaSO8fc7Q6UoR7oL90KCqHZzbaPIKkvUZOIvvPAcAt2aQCIV8LeAy5POfBZjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وینیسیوس:
من به آنچلوتی قول دادم که یک ضربه سر بزنم و او به من گفت این غیرممکن است و اگر این کار را انجام دهم به من هدیه خواهد داد و الان منتظر هدیه هستم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95802" target="_blank">📅 04:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXstIvzQvYJybvgSFg_yiIB2Le8ty2wwLKHid69kut9yMbPZ-CNutvYeUkXzFGzbcsCM8Xjw4Ew1mLMKpY_KwycPYKog6XBsdeUJvWJQ9bIUWdrYR5Cor-6DYSxzMl8_p8t9FbV4JSc2QZEZC7FJB8WZJgXCbnc_eVKS2YdfqLM4Nsn99Y3zZdoIes_qZGCZetf-V827MVoAuzO-_mBRnojh6BiwJal1TedemTg6QmU4adTQ6GQCPvg8HdKdaBpMf6k-Mml3U6lnvDx7anBaYLRvMRmYj2oi0AtdTGL6gkNXuDb_1EIYwmzRuRC3pMrmLFliVcrl_8lvdoh3bEYJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشنگترین عکسی که امروز میتونید ببینید، نیمار و دختر گوگولیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95801" target="_blank">📅 03:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVZKHKjb7QWe9O98vWpno1d3zok2VuYn-SWJql9BkS5W6NXES2002uyDFRAJQ2Zmn2WZvK1hmot7vZ41qGzj59ePqCFycSTjAwQsH7IJPgNAHYZMlWVpCsSflBW_LKt2SE2Fc65_AFEamcMeco-nqxgasKWTBTTljIe9reFFCpUOzj-DFi1sW1BJ89UfmkvPKWX-Mt9MGbHBu5B2ZD6egZ84U0_cb9g0MMYUS5xQVKfTJGBNW9aGQ1LO29yzZZT8nGKodDNbKRa3qyTTXGXHi1fM_Gyp7sVDre58rS5frckUL3qtL_ioKP8MaMO-N14KRoXZb0xzCIhlIXzKp_sSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بوسنی رسما به عنوان بهترین تیم سوم به مرحله یک شانزدهم نهایی جام جهانی راه یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95800" target="_blank">📅 03:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDH51gJZG45NnrBY-wHuLY0SM_W5Sxbg6_vHsrWlEvc777oAnJnbQAuodjCWcVsmSkzpahUBJSRfmlwAz4UubG6-W65nrTiCfFPM3micRBKsfQt2RLTyKXep8mF2H-TrtkoCqvhFNpFAfSmbYsirSdoSLVPG71mNDJRjPewZ0YSyQ0X0O2WQMsjMEcmgiU0DY8YWJVOlAsZBxuwUm0yAHxdqQzjBCNzfKKHLJTYR35xTgNY_YUfQQh8gMjyBvK0B_KjTH2pZ4IJjTdbvykTCtNrCN7QXjc95zpqOmRCPK97WaMK02RYtc8oaX0zN78OIaaj2_6vqOoB7J5bMt1DBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوست عزیزی که روی نبردن مراکش با 2 گل یا بیشتر بت زده بود 3.6 میلیون یارو بگا داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95799" target="_blank">📅 03:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P49xs4DAaIohs1pYYB0uwDVLWdFoDRVJWJchZE2JMLc6QzcAAtCm2Dj6prMYKcutwRsLBU29MSGi59n4cLIAShxyIiE5Gr_fZaEx0gNHciPpeclI4LA7CBYu5TV4ZRAfbP6re38k68wvZMBZmiZUg_5t3-cGKYb69Yczoi04hHMFeysH-BcTBP0QBxCuz5SQS0hpz_fwBj9VGqK3j7X4KgNzCZUjAA6brSQzw3ME5mjyFaR_wYcbeSTOfnY_ebs2Dflc4P_KVTlJJxJiHajWHuchyS_DYi7OGiYBCzUwf06HrFc69Lq8gYnoHZoVWiFf_a1N2nz5EzkFg_By3mNdsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
نیمار مقابل اسکاتلند تو 15 دقیقه 9 بار توپ لو داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95798" target="_blank">📅 03:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyCiJr3DXEPYXu0B7gHTj9v5SZR_wHkKzqkhTPSs3NwD-8Aex02eXxBv3jiICFaj9OEctMBj0aM5YOjw3Dq9TrkJOrSz8nsg2yWGeqd1puo0tCxwGa2MCClM91rYOxu6DoNpcOYw2A_3FmSQj8SD6Amu7Iw0aA1go-cHXFdgPOLCDRf2-DSPBAlsOXm6ivbtT1iMxbYICIDL6sSVlDTFyOaTi2SQpx2FY7x_AJQCIk3B3ZyxKgwzbXpixCBaItWAK21Tf9Z_MQzOlBkxtAb2NdDThYyT6vbEwJPoiWJwcPAWJK-ifGAS-aJg7Tuxe-1A4fOgYipobpVfMVZBTNhomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم ملی مراکش اولین تیم عربی است که دو بار متوالی به دور دوم جام جهانی راه یافته است.
- جام جهانی 2022
- جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95797" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deBd7H3UsFsq01-flCfLGmIkleHNtazwtNfYqGE-gJZ1M6XAdt5pwt_6nkLhEcKFPe3K02gDJcm37pzDZeQnWqZVfJ4qE1jeWJteVdkxfUIuXln1Outjt650fKRrkPt2TCj1VyY9JQekfOJrsBb_4EW8lUX66y7o63hWz-drPAO2boQ5EQNLIezZj3es5jeu8LIoFWABOA3wrwePdvcrL7j79uCOYN4SaDAeDE3aRNJugG-flfml0I6vf4nLZziG-2mmN07LvNJS7GSFrP2KDAzTWJJnc5M43Y0yyY5BLBV6fWCcuCGlm0d6fkDb3dn3jTZ0aszkakOmUz8psknMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس برای سومین بازی متوالی بهترین بازیکن بازی شد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95796" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZs-NjLoP5DKXrwXd8xxQYMHo6g1GGql0qs0z1TagpA992s0wXlOUzQXy5sTx1sJnj7uHuOXEmS3KBGXIll7V-rC1UA54AmWIlE4bHj6fPwERg0B8pDB6_OpF5qzGOOBf82DEs0ih34cKemZiG5OL6VD8gBjvk74_tAuZRLXWt3F5BEX1WloN7iAaKdro7iwJ_U3eNEFJWKA14LUvtN1za1sxMfFEbTCN5O7Vj_kkV31kKaSa25fQi0yH65pz8KK_uY-0PySjUbEDd6c0bHZRq8gkrgLhgI4dh6wD-Roz1EtJUnsb8An413bwdr-qoWuDoB4mN6U3rn4hxuvd93auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه C جام‌جهانی با برزیل و صعود مراکش به عنوان تیم دوم گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95795" target="_blank">📅 03:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiIrTaiT4JJivhaH2rr9DSOW4D0CGisoGCitoNVeU003KVVcEdPOYEm1sSe6RByhRWvBZVaHjvnIZQDpXakZr_uYQP6Xk7RUBFyLKLeBLTt6EXEde_q4jM8I9dWvb6Zi1ZfAyqeWFgRIviYzthXdZVhMglw3Un92LEevAHqppaLp9YJowa3YCCMStBATjMR41gFyBUQCcoW277gIiBGQBL1KdHMrvQrs1J02waZvW97D9PoV04OLWX8150Dm-f_dQiMwLaU1PtOeHL_5Q1p6at7qs-yI98CBxhUZY_v_3tm0xk91h-v4OJn6eQ_fPO2S_BETJxrmbm1qVqfZkvdpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک مراکش مقابل هائیتیِ حذف شده
🇲🇦
مراکش 4-2
🇭🇹
هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95794" target="_blank">📅 03:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grg_XAc8rAanzvKPpBAOlFyD1PHGzaWJwwvBgR7S20kj-D0HT7DfaZpSUbjedE-04boCgNR7-QEWwN-eA-wdb3fV2rV4LtKN8QcPxADBvNRI4Em9ig5oNbJ6RJ-dNiyykQdWBasLd68nOPt-QR5P-i2JPh3I9UjwjpWsnGDAvZuTE91HLxMrl6Zo3ds-I-WE606B6_Wvr_qR9m-BTTwm-8ButIJOlHClirSC6kkzNk7dVfQFk7mfYBogXEBxWmecLz2FUt1kXI-ZTtoJxrfEHWH8DgLkocE9X2-4d0HAFRPmIrCvQXl-hPou0cpAM8ZWm9qkl0c7tujyu48spBnr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع سلسائو مقابل اسکاتلند و صعود به دور بعدی
🇧🇷
برزیل 3 - 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95793" target="_blank">📅 03:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjRAnR48nCMzTBGg8PC7c6MdHwmUSsPdIxbJua6jtLcE4-EDoWo3NUvrE7oL3WSSd1SfSoQUJAaP8upOWXxahO8ynsxeB_622GdWfM2GGFpzZfa2t3zUGT3en45AbS9IwaO3nSwX6TQ7f0li8sGJMZ17lOdncfJfpdbA8AgK2NFAySDfx3I4Yegy6EOeiMciePD_1KrvaztVKRgSXMekHj5Cx5zQGBwaoClj8q2WTMz5Gt3Lgx4QdEj9J_9Tr8ESoNs588j-AuPCUFTdh6r033gOE2iSrchBkFehmWr2XMYJgcZjaUvcl_YNIX5HO854Ai_5uhIH05Eqio--SVoW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برزیل رسما به مرحله یک شانزدهم نهایی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95792" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95791" target="_blank">📅 03:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mx_xU9E4MNVtyifIzIm-CGm6IcgJnu2hYHthwJz7n11pCpqSiZDV9_KD3sFjVN6cOcJVLrA6nkCxDn6REfSneCvuaP__ix-IGdURCRrvxP9_TRicU7R1rehCXYYfOLYCWXexS4rd1XcNVYcEi9SKjQaEFxkYICVOGlm01rcgG6jbinywoUBz855eBRi-mXweTAYgQC0QVjJrUoO9q3ExS73C15w8Kro6-R5y2S3cL2LVkBBQGo8IS6oymrPiaEt-YfNnX8PLNRyp6_t_zlCTgn-cPw7LCrkzXI2PxUUmYt5NAIFrmgawTkbdUNqaTdJA5TpgnrmXRz-B9HGITFlOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPrqTpdT7e4k7MVH48haj5qTVYQ_YH-nTF-q79jxFZ4g-u1boLihws1xkE5sRc8H0LOactZ0BV-VOIVhhNZZxqko6mAjiPVHBrZAjvD5USnI0kv5da5dG2ixpEyRR1SVjfV2UQsSXzL5mOcLlksTPD-fIQ2OFJ-sdpMQ0TwElnLfrkvHsZBc7cbolC_bZ0MosEz6Wn5jregRt3fBY_Iq7_jVqSykHpQ2Gf5a07OYHBZ6yzhWPd7OHt0isCWUAUTDRtrkWdK6Qh78-7D8RfaA5BHgkKxfLoAqkCPJw6gMqcn47e9NdpX9h5NTtyXMUvtuc35bcYwDJX3kOo6MSFlJqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🇨🇿
ترکیب رسمی جمهوری‌چک و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95789" target="_blank">📅 03:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzrVepvCfzt8389u3dKO6sdi7Jnhi7CDxU4kvkl4Ax5j2tHpyxXBuxVwbnhZRzYGsDvHWK62aXUjUCuTZ0YgOGoj9lf-w_1Nt27ax9G2fhKncxJhyGSvRBvqJ5T780w5UJUtxRRsRVzdanz_ICyRelSJtK-aCcrL3UvYYIlQiAT3PdHRVAJYhCcOYGpwTw68qS2kvSir5Q_zr09P1ysHftB6muF2P3t57XeNh4ozEvFhCf-XU0Zb8C2XIay3udlr-FXPmTOuekZNZl2igEWAjEHrFfQR596PotJ6x9p6iEaiC4l3DAEb2MV9fDy3_UtCA7liWQZyW3GjZFO0W7mIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95788" target="_blank">📅 03:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=kwi91wu8zVrHjs17DzeBj6iIR-5WTwkxiQnKrS1fjxks4h2pmbbw9CoVeoYVENnxTFTqfYYIqmIxuAAP9M8FanDNtZUSttdtsG9Lq0rO0lt_FWoYXuyMslcEiXJwe7gCN90aO8pIsm6u8St_EUV8lnkSHVSTfOe9qFY40fxH34cjafcufudeYf7LaEhgnkYutGp9pIJXBRqBv4XdQWSfCadKT_EWjaF538BzPFYnADVgA7gDU_HHy33KiNtMFPpEWTUtR8NbnFk7m8cEy0fe6ieYUisdMnCMksrkx4avCP-wGkBlNoOZYY_1-64diBIYM0cdNe68VcE9-zwsbo5r8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=kwi91wu8zVrHjs17DzeBj6iIR-5WTwkxiQnKrS1fjxks4h2pmbbw9CoVeoYVENnxTFTqfYYIqmIxuAAP9M8FanDNtZUSttdtsG9Lq0rO0lt_FWoYXuyMslcEiXJwe7gCN90aO8pIsm6u8St_EUV8lnkSHVSTfOe9qFY40fxH34cjafcufudeYf7LaEhgnkYutGp9pIJXBRqBv4XdQWSfCadKT_EWjaF538BzPFYnADVgA7gDU_HHy33KiNtMFPpEWTUtR8NbnFk7m8cEy0fe6ieYUisdMnCMksrkx4avCP-wGkBlNoOZYY_1-64diBIYM0cdNe68VcE9-zwsbo5r8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95787" target="_blank">📅 03:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مراکش چهارمی هم زد</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95786" target="_blank">📅 03:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اندریک افسانه ای هم وارد زمین شد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95785" target="_blank">📅 03:17 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
