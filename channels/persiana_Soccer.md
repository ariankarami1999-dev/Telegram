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
<img src="https://cdn4.telesco.pe/file/XP37CadWaq5oiZz5omsQZVNmPh49tGQ_gUTGJyJHSObyF8dsQCUhLa28nu6ofrmoa-j1Ak03PH6KqGtrNE_uQKcLKkIrRPoZQIDiuBh4PzmmKUw0QwyD0eS7p1mYOll3ON5MQaBEDJUBwceVEs5y1gGYuwPiJ4VDNBVoUJm3drIPskwGUfGn40ApK0jCC_eyp623kkNrhMncmqPYGvRD0jJRiJL05rfw5qDtzSspZinGfO5r5QF9Z_d2oheIehR-Aw5mGbxTPGu2Ksr4Y4pRqLeiqrK0xAlsuIKQqxe5EKu5rQNKhHscJI7TVJJ_sLBQVgAIW6qoOvdimnVqPIP6Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ZlrpQhxMUJB5XFS2eTgWwD1vZSMgsoV-5FtTIEtzCvO6pUn2wQwYMayCI3LQGFN2kkfFqxZF5oBP-41qfSWUgeRjIlkzBsoayWKJHAg6Elavfi5YIShUM6Ndm-Bwyr-prKXORscBzuAYX8zUczEcEHS03d75eMokuGNkyzAlWjgFV4-9MskCyiXuEdDPU0pdXJ6tZfsp3W9UAdW4xMCyWM0RHWMauOcDXorfXJk1xscYqv5WcOIo2oB_k0-vgMFi6XcH7-mis8TaxCZ82cQJ7yv7eVkJVlZpx1QzF6tfEnoLj5jHIpaVb5xhrmRiRItX47-Hv3ckMODC9v9P2jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BvJ9_H4uMflpErSDNegmZsoCui3k5SijdjTEWaXXApkBOltYa2qNyrB05-iYgIs5QM_0gPtqB7IiHZRwQX0Vcm5k2Kgwi-ZSLsAY0WJl2TaRbR8CrcvGTlC2ha0Ry4z-9odaDySB_CXdnnRVCc86XGdXZGLyRvO9POg5LzTqmE7aScsXw_AXqaTePNqmVA7-wqmdu8tAfJrd0TqKPihbzRTWr3qhQNITJRERGM6hYBzw58O3ljLdXcwNS7yoTQlnUdcguO1c6Xf8G0ocUMoAV_-UFrBINcJRcuy6VbCSxBsoyBhy5NqKDy1JnNFbv9Z5x2G32c04LFQ9ZdzDbGK4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BvJ9_H4uMflpErSDNegmZsoCui3k5SijdjTEWaXXApkBOltYa2qNyrB05-iYgIs5QM_0gPtqB7IiHZRwQX0Vcm5k2Kgwi-ZSLsAY0WJl2TaRbR8CrcvGTlC2ha0Ry4z-9odaDySB_CXdnnRVCc86XGdXZGLyRvO9POg5LzTqmE7aScsXw_AXqaTePNqmVA7-wqmdu8tAfJrd0TqKPihbzRTWr3qhQNITJRERGM6hYBzw58O3ljLdXcwNS7yoTQlnUdcguO1c6Xf8G0ocUMoAV_-UFrBINcJRcuy6VbCSxBsoyBhy5NqKDy1JnNFbv9Z5x2G32c04LFQ9ZdzDbGK4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4576fhAYUxv0_-4pRiJxIHEqRTUA5tqv7ad8uAI4XDNX8ch2yOTrOyXnYjNfqP9Lfx1XiM1FFKtRDxQjk3yRhml3N0GhrdXRy_uNovgEEiqU1aPEpg5tMuiDQW2bTnIGgAbcL3ey-ptJn11QbMLFSg765q5zJ6VAdCnQSWHDV6P1MdaNTPIL313fnMJbjThBv-0mEtmBV3FKbut6mE3fMRExm44ngqs71FlpBWuL78ZBEXbAsy8qNAcKtC07QgOLPPfqfgYTK1hv6ou6Cnv4TXzNh5WTySyqRqWc044EdbTtSL_GGxWYrshUG88y27CrNOIq97vB3NNtwuOaoaU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhpB1sWc1xYlWPXwGeFG49gWd6xB4TtXyCxlU5-l1R0EU5BSkE-129LuEB0vypQGO_7FPQGsY9x_wiBKy5PrkuShYpi6M-eAzyjJV-E6wnjAOto2z1uzLu2aPAs3tbKdYbzuNwitiyBb9H8PvZqLEVFgJAbe7UJCwpXnKv0yibN_8vnWNxSPfY-G5c3ftERnwS350jrVaNBqOo8K0uT_9pDHMFnqSC4sgsNjrmEw3ZzPIin4eruXX6BV9o-gchtq06EBP5chFVLWqBes0Lpt6CQQZ6TSRicBI0tKXJH0t1Zgamy5VTQ_t8NEuadUrCK-Xmy-ebrvdo0CQmAcKkOsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=S7wSAAqiOL7e1K9VWP8_XHI_HyjE5T4H5RgbPwf-z3JwmY6swHXZxM4ZX-7h0eKYW0zD7Wgla73fGeV5eM5SkOrpOz4QnqkrJzhsQkQjbkaCj8pZ64lDPnfovkLmZcJyvFaC4GE58-RkeYEmB3lkso8o5z0UWNHbwyF1D55oqFbZ9KwhFsaPd_kd2EBo3N46vJw5SG5SZcpABIQwTC9nHLFed__MrBLQHc2NkMijWO5tHSqbWofzvf5bG9CqwmpDbxGwQ_yuu0a2lcldrsQWlYPoT2f5_HvYfpSWL5jIKxQ8UrQy7vcVKo8nawuDsERLtFJ1YEJeUbje9g89N3bmlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=S7wSAAqiOL7e1K9VWP8_XHI_HyjE5T4H5RgbPwf-z3JwmY6swHXZxM4ZX-7h0eKYW0zD7Wgla73fGeV5eM5SkOrpOz4QnqkrJzhsQkQjbkaCj8pZ64lDPnfovkLmZcJyvFaC4GE58-RkeYEmB3lkso8o5z0UWNHbwyF1D55oqFbZ9KwhFsaPd_kd2EBo3N46vJw5SG5SZcpABIQwTC9nHLFed__MrBLQHc2NkMijWO5tHSqbWofzvf5bG9CqwmpDbxGwQ_yuu0a2lcldrsQWlYPoT2f5_HvYfpSWL5jIKxQ8UrQy7vcVKo8nawuDsERLtFJ1YEJeUbje9g89N3bmlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=c2qg4gXpmynmyUIFgSscGImFoGOdlWp9sOW0yyNCbDtAvSoWmqXIMDBtI4YAPeC8thINCyRj_VSvQs3d6Q5m9IACicgjydG4SvNRWmSfvxNLk2amqDgNz7S7PuZzZ4HD8Glcyttfi7MahxHAqUlDnFjmLB4Oa3KNczFebQ6TRIjTnG3BQI0XyLZ6MDkuR-9Qr_CyPrqgTzyGd97FdILA6GTDC3GFYJFchXzVaOa5pE6vG3RyeQZHsiBwJBxj5Q8b_XWddJVlSEZfHzdJWClcKubUxSECY5wuGocIHLPt7o6QGXdtd09lN_ieifNPD1mY3dCxwRa61kn_h0cpLHkN7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=c2qg4gXpmynmyUIFgSscGImFoGOdlWp9sOW0yyNCbDtAvSoWmqXIMDBtI4YAPeC8thINCyRj_VSvQs3d6Q5m9IACicgjydG4SvNRWmSfvxNLk2amqDgNz7S7PuZzZ4HD8Glcyttfi7MahxHAqUlDnFjmLB4Oa3KNczFebQ6TRIjTnG3BQI0XyLZ6MDkuR-9Qr_CyPrqgTzyGd97FdILA6GTDC3GFYJFchXzVaOa5pE6vG3RyeQZHsiBwJBxj5Q8b_XWddJVlSEZfHzdJWClcKubUxSECY5wuGocIHLPt7o6QGXdtd09lN_ieifNPD1mY3dCxwRa61kn_h0cpLHkN7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔑V2RAY-VPN🗝️ADMIN️</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiJlXQ2Nqtu7We7c3aexc6Ls10_FG6N5xDiiDb36liAS-huOBGuLCrQq1Q5SLlxrhV8_jUqujovEf6nQM_E_7H2y-6rHLK6ruejCwaMhOM9xT6NKBbBSli3XGMb84NCvgPbhA9YD5NGBnXOmSn5SCETNn7HQ8sWHIfkkw0RaRlByjIi9hrii9aM-lBJ87BF1RTCXvXyMMCqjSOvMcTXvzNaSKYA3eZVGTKEqtwrMmYaQ8HAQX-dcKUUgN3yR9nOY3Nb-jSC1PodQvobQ1hYtL_3PaWUpqEa5IAb-iEgq4YOZMb5MaEPYqsUifHf4WUyE4iD6xEx72XfDCd_pn4oRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
سرویس استارلینک واقعی
🎖️
💥
🔝
موقع جنگ بعدی،بلافاصله تموم سرورهای موجود در بازار قطع میشن پس جای معتبر خرید کنید
✅
✅
🥇
آی پی ثابت و واقعی استارلینک
🥈
پایداری تضمینی حتی در زمان جنگ
🥉
لینک ساب جهت
استعلام سرویس
✅
بدون ضریب با ضمانت عودت
➕
سرویس
تانل و استار موجود
✅
✅
معتبر هستن ما ازشون خرید میکنیم.بگین از طرف کانال پرشیانا هستین اولین خرید رو تخفیف میدن
·• ━━━━༺
🔗
༻━━━━ •·
🛫
Channel:
@vpn_artel
🕹️
🛡
admin:
@Make_server
·• ━━━━༺
🔗
༻━━━━ •·</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22627" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_ax3W7fdpQ-zMR0HBfRmSjxd8QJjwhxZ84DPZ06fbtzgNsS4jxIopj4Y-hkZ8ftjw62c_i9kQ5KdWzND6zHCJf6Bv0h_ZOXkkWRPR0xf7CGLTaT5xpjYmIkBAFXplhtnWLFuUJakSTDwqMfhdl7Lrv9P9a0rQ_NNYXM_uLbSDAI9obSu2nw9E5H-qNLCSFHcT4M0ISU8DeKVxo95_clTmPcdonrd1aIUwwyp3CxZHnCmYf0i4JTHAleAXO8NRI1fU6NyciuXYoYEQ7OW0_QnwQ-fibHfCpd9Q_C8YRX-p59yzKuJtbScvSjyVKZSyWPLxaw53Jk_ZiRLD-sDF_Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZJzVAlZoJZzCgMpuAC4X3NfTMivdxdG_e6_9bHc_UTUPsmZzfruZslHNxhrsFSZe7fr1NRERJ7_S4Liw-lKMJ4zNNBz7DzmtNOIYFTGU1GGiko14_UlpYioILFVjfAwBC7YgVGAfEHcSkQccYRTSauZRgdsPTwIiz0AW1FqhUtjT5m61Fhk9fCQywfUtAfClA_IYSHHLIKLhX6bCVKEL2rgB-lHBb4NnXFS4etBSfkTjiFTO_CKYJ59zBAadwnp_5kFLnmBFdSQDVWY2fDOeuc5Bsn8p0MCj5v4y1TKUivzGsEimEu98WrdvfP46r0gW4ClAzS1WgItxDXitBbOgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=qFk6tJIqpyNseTlsLL6kSNbmPSaPdw2zKL3T1KzSwzloZuMMlwIWXO1X4pXnhsN9D3TSyqpYeNH_ORvWDzEZOmiBYtCPayIP0at5jLNFWNUS3lSMiwkiRIpxZFrvlDxB0wRnluVoQbULLkYdElGBVoI4PMQTdfx89G412nRLkL94IiMat6gFzkFl1LjbGT3UsjPMqlqwBxX6k5zc1eUBqEH3MQg9whsQqvaz1m6HL3HMhUSweh1oQgqQOmZqLfAcBRCDM-0bQAn4EWWmS60EdC_hpkSPYGinZFGH9KEc_4mqtQ0qpyHTLWYfwphVq_cU-tM4d7cFjTsLNGKuW7M1IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=qFk6tJIqpyNseTlsLL6kSNbmPSaPdw2zKL3T1KzSwzloZuMMlwIWXO1X4pXnhsN9D3TSyqpYeNH_ORvWDzEZOmiBYtCPayIP0at5jLNFWNUS3lSMiwkiRIpxZFrvlDxB0wRnluVoQbULLkYdElGBVoI4PMQTdfx89G412nRLkL94IiMat6gFzkFl1LjbGT3UsjPMqlqwBxX6k5zc1eUBqEH3MQg9whsQqvaz1m6HL3HMhUSweh1oQgqQOmZqLfAcBRCDM-0bQAn4EWWmS60EdC_hpkSPYGinZFGH9KEc_4mqtQ0qpyHTLWYfwphVq_cU-tM4d7cFjTsLNGKuW7M1IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=GesQF_qcoJPJuEMgMaLsxOKfTUxh85fkw-aHL6J3E_6r26af9zxhfg5BDJ1vftS0yfOxTzKHcP-NjGpjvGSwL9E8O2hTt6iwj7GAk6G8uRvOcNYZuPawAiDcw8tWfF5iPm7yHhbdpl4eC1MZvIPORzfLpIOF2fCRvY0C_i_ejYzW_mC4Qb_SFSXoyMm5xfeTxArsRWqm5zTnX-xxIuYRbpxs987XNBVrqrGfpjdFV4VvBG1vc6ifSAlCHnUoo58s_qre738YyxXaIWwpdKmX7Y_PPqfO3pGlCcpkuVmfRECU2OlH0aCttLhLEDl9UNJzUHtDgrwV9onQmwlSvzQ3hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=GesQF_qcoJPJuEMgMaLsxOKfTUxh85fkw-aHL6J3E_6r26af9zxhfg5BDJ1vftS0yfOxTzKHcP-NjGpjvGSwL9E8O2hTt6iwj7GAk6G8uRvOcNYZuPawAiDcw8tWfF5iPm7yHhbdpl4eC1MZvIPORzfLpIOF2fCRvY0C_i_ejYzW_mC4Qb_SFSXoyMm5xfeTxArsRWqm5zTnX-xxIuYRbpxs987XNBVrqrGfpjdFV4VvBG1vc6ifSAlCHnUoo58s_qre738YyxXaIWwpdKmX7Y_PPqfO3pGlCcpkuVmfRECU2OlH0aCttLhLEDl9UNJzUHtDgrwV9onQmwlSvzQ3hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhyhuPcZx75u1KkHIU5Y8z_Mapy9shyJJFMSTtI-eN9Jvo3qv50YDp0bOgBek6Blj91gXejpz4ceAqnIs9bO8eZ2IGMJwxLlXiJ8s1qCrTGGp_FHZ2iIDiLQNMV9xKH2mlgTdpTwRP4QyviuxyW1Yp_eJHffphI5qArsIKwMEfS5cG_sMF29aOqcahbNlfuuo2PZa1OyV_T_Q5JXOUwjv4qCWK83HlmcQUEfuo_kuFhVO4f36WDwupXaUaTMir0K5XJVTDWhoA1QVzVphcHbDgTW2rnXfgJuGbyw5afEVBs0mFi8evG2FnVlSYJvVY2oYQmhRwaD4yt3hAH-VOYUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVNsB-fNrSCzAXOWlPISA5S4YQXEpWr4f1ME0SS_XvwgEO-SRCMATIJ3--tBwHiYNOiVWqg827Qjvaqm2ys8Rn_itggZ5gAS4xgD7HsiHZeDWzJVndt_arsrqo8g34aa2KRTrDFyv0k9YSNzVZDtMh5XED_i0qBc79GNceIspV1XobQXPkT-ixNpHDj6_xLN7VaAQeKOrPogobIGjJXEzkd6OgPWvh1dCHL-DK-wnUOYrgBdR93k4Tyoi9VGS7FStVlTBNopLNAjNGdUrL5rWWuHaX_tdUm_Y5-6qKiRqf5VQdvzDDNGjrCdBN64Qn51ikOiHh4UAHuF0y_sZTXecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6P4e4sMLT2jqpnHE_7BAlNGAv8HsuqDHVen1zj7QnuUYoq_YvRA5Q-uoaAY9chY4mPHa0nyxS8HqnfwmSBiwQTAxsc-o6jeVZozWSmChoKqMSinLoWGF6Q10JJ5m_97Bil8W1YubdTcf634mhCcSYHtqmO9qFQhIZYPTxmYtHZ4z_vF5KzHnCJsEHe_EPOUtS_4Qs23KSPULgTltgSklSfMToP8yZAJeOLyftFBQQ48lkPIULDdeCXEIZT-GS36iZG_e-M2GrmK-RHoKViFhDbZw0NUXP11glKYaycVcpd0zvbeUAFmB-QH7rAuB8JemtOGNB15O1P_Eg-Fdsw-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVBDLvOMun8BJmxklwXxFKc7G5d4nsJP1kaGC5Y5FS_961hwYPj79x407SXN8jWn5-PqgdqJ72FRgZi5hsRAv2V1qOyH3q6DEbNXEHWDBNr8AriamQE45v8N9CqqYrbB6m9YkJvrDovTpyd1o6YXRd02uip4WEV82-ixjGZ8vrJQ7q0VrnoPrT4yU45S-ENzS0OXBTWTmmM94SXJo5c05RF3Ky5kJ90kzHxpEd7smfY_c-8KnMk-mBJqFqVqao25eIj63ApGLc0_LdUm4ZWC6voBPpJgWgELQDUeD00_k9p_jW5GJuFYSuOM76H_l2N-VqWM6EskIvquzC-5UkZuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzpkT1zhZdySiKQk8anZYSobG0fOlAejBtp_tBuf8sv1bsL2M3dsrIjd63mFPoWK5z0GvMi-XXehTXN6x3Z4rCemWJTk6ncFVMWMOsCkjMsqGid6LpggueOKEvQkHXhe8XwTQmv6c5cfwi70RhWmxk3Avx-Lkef3iL3jgAstmwcKUMScSOXJ1V5e0c-JGpAhaPxg9QOGfxfM8AHtiZrDijmue2NQdUvoUcNS9gP-qasZvhT0KVbOYB5yheBpVTUGY83US0wndlFVqH99MFNUT2CIvkjvRSyMcGbnjPalbzOEsKLcd3cSnVz8QCHrUmOwK1Q-EKI-_eQZIyweNf1Ggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=aj6-5cg_sTJ7iYBrng8W7NvrvygJVm_PJBcOhqWM_K1GqNedizNZpkKytH634onBq8PiY7oY1gh3KFy6ve-nlZ47ylLOsdY58JQ3Yq354MgOQj7PYyYYsEdvFWQfEOd0MQUJhHqA8sASdObNqyQEolt10lkWO2pe6Jk-kjSzAwWI0FLfT_8H1MiSOmnnOuS8ukyQo-SSMfww-PBms581KAKnAsX619tmLiiVBW9hzUB1ILTbp7eaeS-kd3S0UDuAzcxrv1qLc2H4J9Vfowlq607MBRokMITgYqKgkIi_eOKS6wYDzGENBBBFwESkyi_3utQb2hpf2ePMZxFQ1RpbMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=aj6-5cg_sTJ7iYBrng8W7NvrvygJVm_PJBcOhqWM_K1GqNedizNZpkKytH634onBq8PiY7oY1gh3KFy6ve-nlZ47ylLOsdY58JQ3Yq354MgOQj7PYyYYsEdvFWQfEOd0MQUJhHqA8sASdObNqyQEolt10lkWO2pe6Jk-kjSzAwWI0FLfT_8H1MiSOmnnOuS8ukyQo-SSMfww-PBms581KAKnAsX619tmLiiVBW9hzUB1ILTbp7eaeS-kd3S0UDuAzcxrv1qLc2H4J9Vfowlq607MBRokMITgYqKgkIi_eOKS6wYDzGENBBBFwESkyi_3utQb2hpf2ePMZxFQ1RpbMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ih5EoYdzdx6g7NuWHOjRdjIVE1-puGwyaX8WSBvNpRCuqzTq91fAK268aPvCGxLHa8FDwEdxlRIt0BXGgc-Ss5Y8mVdjXjOiPQJ4gL73quxsyB3CLBLy35EIXzcrelNNErxF1RvOtLgPsX4a28jj54BgGxMcV-IY0PANahGjMLePe98Aw5ZXUM8d9NPz3NPnNICrodo98RNRIiC4vWFvIXlDXrpLaDgRPbO2KOcT9o5LK9NaZk4iXezWkeTvKmRiIqYfoaEQlli0eslDQuusasfGEpRGk43Wfa2TZhVb1g3-UCkGQKFDpHZtvlkPWE_icupOJWTSI1vUtkH8AUztOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تاحالابدون‌واریزی روی فوتبالها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
g11
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22616" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb3szWmW03vpmLsEk9QoDWQl_hBpeLSsv5dq6KxTbQEppTJpDGqVE0ty2kyUuEGE2ULHvng9xyu3F0sJCkCyADagOLWxYJvuYBJgyu8ry6lLN41UmnZ60UsHLTqoiouKx_3WBl-rouEwBS2NSeZPmFyLK20pBGi7zNtzcWPmCADFcwjsDpysn520L1_dNAvFW58ABRouEAC9ontYm9b-ZsuhxzcByZ7eoyfLCGfhKV7shGtSF3C2Org-p7ujOjAbXCJO4WnHZTrVLJiuzou3sNy6tr1FRbp_lCnlHKT_C0ZSgnhgFIE572F_vv5LHa82V3_zh0MQRw5wFtInnJ0aIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=iW7ZmP1TxK1EhYgeupdvCRHDAutlemLJzxQTfplvn-QgPtBJuQ7hOABVSgegTivBaEKgJ9usIk6nF9qkyMyTKCCU5R7Nm2-hlsKKlHnAygwqnW5V94l3Xe44nXfKnow1uyLOppQIki6fd3I6TXnE8x_nptZvoA1TV2-Qd04lD_s57Km_dE9QOCAhCrVP3Ab-rEVLsDWJKsPq0UsIjT9VfbD55aMvsZhOlRBB7kdkf0L3PvmGc_2lutHTETqnzuxZFw8IIbfatkd6gFMcm6J4_ZauqaxuySosPIEtN7O6xRo5RDi0Wl-h2KnKWTXhRppedJcL--WL75pWKiHXnXXDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=iW7ZmP1TxK1EhYgeupdvCRHDAutlemLJzxQTfplvn-QgPtBJuQ7hOABVSgegTivBaEKgJ9usIk6nF9qkyMyTKCCU5R7Nm2-hlsKKlHnAygwqnW5V94l3Xe44nXfKnow1uyLOppQIki6fd3I6TXnE8x_nptZvoA1TV2-Qd04lD_s57Km_dE9QOCAhCrVP3Ab-rEVLsDWJKsPq0UsIjT9VfbD55aMvsZhOlRBB7kdkf0L3PvmGc_2lutHTETqnzuxZFw8IIbfatkd6gFMcm6J4_ZauqaxuySosPIEtN7O6xRo5RDi0Wl-h2KnKWTXhRppedJcL--WL75pWKiHXnXXDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnV7e5B5XFyspuQTtklCbixb0WYriKHY4JdYU_WXAT7mmTTRDHuBxkHgcX4DZlaVc7FilECHkGWuVL4s5kbZTAJl5SXey9krNfpWFCiQo1nBLCjP0d71pFwSgNI9VlTYUUMd90VTvi6FEZ1k1pHgV-7K554NarLI-QUzrAPyD2flnLQ-FtoLMvdIu9OC20Aa9WVFxFRhcAbRV844q-lrwUVBgeVBfROhxA2LfelFtavCSmzbl-m_ZMzKYxKN-ZFd-NfoGl6vU_Orxl9fNy76TbFdo9Rw7TvO5a6OweWTE0ldoxZUWvjnVdY7bVNvkOlAz541bcRQhAblEWbcWWApJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=GGWtfgeKy_e9Txo1nkPx6Lf8r_NpdQD5Aqqxf2CXx3yRBAEJJBUff9wmeB6MnitnZvXm8JdxWDQtXcNm0xzy0z99k-qm3B5njLnCI6y-PocywVTWZb9k01TqDTrizw257FCRFUbP-25E5Ndykr554KE0uxsY8OOArOU7wq1YH_tY-jr4uyU5_ESwrFjABii4R-IgYl80UYo8Nw4YPAw9NhfViWKxrNYMJhf87iCBGDbiej1FECiTswwWax2GXNg18pYUwJ2eQDf8xsRXAb4mEGUW0-pLvykY-Co-hh3QYfHhwQpwpGaoqeT2-BrkgthR68rZDbmGGqZdlKYRnTnCXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=GGWtfgeKy_e9Txo1nkPx6Lf8r_NpdQD5Aqqxf2CXx3yRBAEJJBUff9wmeB6MnitnZvXm8JdxWDQtXcNm0xzy0z99k-qm3B5njLnCI6y-PocywVTWZb9k01TqDTrizw257FCRFUbP-25E5Ndykr554KE0uxsY8OOArOU7wq1YH_tY-jr4uyU5_ESwrFjABii4R-IgYl80UYo8Nw4YPAw9NhfViWKxrNYMJhf87iCBGDbiej1FECiTswwWax2GXNg18pYUwJ2eQDf8xsRXAb4mEGUW0-pLvykY-Co-hh3QYfHhwQpwpGaoqeT2-BrkgthR68rZDbmGGqZdlKYRnTnCXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjCgXEGwL0cxVl1UjbBeL45JH00BVtlQfQzDwvYjbxSO-ZxrVEDuPDH22JOElrX2lRSIjVwfJ6ZWAjJ5_eiEuRRyUAXIlxJbM0G18XpDD4uczL0xp56fxbb3e1kozq7txcbTZzATJ6WX8uha7dK0Jvxrj2AAiHkJ2mLKq_76IDlBLlI7ByH4gOtwzsxtHIVCr8bStWMHATiEBRoFL8ayssgSgwr70NaXrVD9w2zYny2xrByhgoNZcRj7pYSwS3R0uxivFP_F1fVicQEAhDZOUVGVKoxcq7zVQtoGyzAek_HOtyDxmNPLbjhJGZINnbH5Jk0DeVmjD0VhVXIxVn9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWHX7F-2L-PMavmcDyo7LIqG0OG_wJsFbX4bKshDoHBhxxQTNPrhmUa8VoX9ALP7Fgp9j3K1fO2a_bqDMIuizrl8vrXEV3zWf3CWslOSiZE0DNbFlFRoHVeNfQpLWhsbtQOwKFTnsycokOfd3Np4_tOQm17niUQ3fkta9nASfyhfvCAVTkhVTQNWj9v3xEdu8C3EBCmVbKYhS4XCCTab8mpTLU7OKhOTwJ9Gu7_kyBUaHEGZ9WpgXd9tfJk-u1h8g5OoFlP2OkEU0_T4CuyE4w8dkQ_JbVU8nGUAHu219_tBaZ8LdET0WreaKSt5dU8PebokQaz7ZVPOmZwh1de8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilL9sAH4jZXNqcPQgPMj5bBljx3EQqzE8rslRThrmEHw1j2C_NKOz-iVqhFzvgC1qcIC72hSoBKFQDqrNWOBNIXkij0lkyyzdbiMfxyU3yIFiAdp9_5aSMYudFZs5V50IwoJSg2AcFU9G_NuN6USITdSH8P1tcFoNpmYmAZaMg5S-i54fdaTrlkOrf3pMAuwL5wxJf8l971tJa4c26nn88-aOgd2mYnbmQ9UTtR3erRWhBpfzVUggsQz2PtwhXIpr8QrrwkjWyRAaMC2uX_vppY5H4RGCD2EU7OFdDLrejh_qe_ah15198GZcHSWPfvUJ6k_5_G-1V_lb5IrQBe_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvU4GYgPP1JaVsmISPk_khWNCBE1PRLUuyCRDxT9JjpkiSw-Wf3rzEqiWGa_8Cm9DG0DngIfth5xTdMIPDi25GFdJ-KjoyJs7HFkrBnOsnNk9pfClTVmQL90Asu0iAZIRJOytxySZdBfd6Eusdp2gL_pJxNQr2F7s6VaRoxraWUbNPjB7flkEkRNi7xt6c7KrOox2z0Us4p13VzZhEgHj_fWTRsgtiYFGxb0RiJUhHpADkStMa832Mp4RRginZFNObSqRPowK8tj0MfOJladMkRZGiOxA_CTXkYOioE4zeli-aY2h9uVQw7Eia-_k63UDyVd5ce99PmM8Rr4pxbxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dip2crMiWFBTlMNz-TVjOkkeeG7v8S8MndOHcr01_Gzp5JEk7JdwqbjUb_LZabwHIYuGzcvdpliF8GbOO0DK3bGEYtIisORHWtPSidiXjeV96J6A_liIYEAOKCuEQ9pjNWDate2l3Dl4caXVPkDq9AsYn3F91GKyJM7kbnJWcBAlS9FdS-MsdfgBQGQRDzfFCY0D4s8ruWVrWHZEDKA3Puup9a0T9tGbZ8ZQfDWhfE_LzkoL_kohJXXW4q07o2sBP2FKPS_xddpYnfBxYQrGlwNMEDRdVg4J9dZwNC0bc0pdJAWXVSm2Bis9a6uey7Jlq2cDIuT1WYRxJ2bi6Ppjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLuAjEhE76IpGXoAKSGjT85gTFr1dktcAVO5SYiEqUk-R70h4Z4px6xB_VMGheDnC6MA7dsYnl7Kw0ZlcFfUIw85x5iY9SIGsFfY1rQZI9FxiFFsOB0z2Ya8npB9kPoNzacoTlkUxsR_9zBsrXmt3F74HASCbr1YxicDmgARWcmWCZmHKtx3E8GprT7ltk8qlORO3duhwMTQ98cR7Ac5a1Jt2lEH3SwovRzG12Wwo0fYtvqe9bUyqhI2acUBbTIN2hSQ8BSu1RsIed_7U-NWgoS0Kp5NH1FxEkH1Ot_aLkOTeuDc8uDzJB-LLo-LSCZ-32M4NgYHbssV9TW2WjYYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDXj_JAbw6OtlwZr0Xf0ntkZ5dL38CgpjCAG-QDCix7Q-o0wo2yk6dZeDH-JXsPfOBbfz8kmcmQGPf3UJdzGAaTWtFxJfXMrrw_JBFlk563lS2HqPn6VIYpqqwxI-iznL8xddlpSfbhMmtF5puCQ-hPsJM67iH6TuDqqh2DdeCIecEvLKH-8lATyeNa4LUacMK1ZlET_NiKZ44r7N3tqGUrjU83PBlg47QDRrMNqE9Ega9ULvxHxbeUnftpxD7ahjtsyNR0arhwcdL_OzsobtQRbDp1jRfFNXU7MA92COQC3snQm2PTMeDrNLdKJWjX8O3P4CfQMICvUOe4qFAf_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs7aXxbGX-9Wv4c_Tfjq3Z7bfKiAfvkfkePVEzJEHyOlcHmdzBDSfPzQ5Wod7uvW__ZoohE9YHv0PKNtIBXBoevklAw6KP0-gqkXUXwx3rm_MKewAaOrnVzAn41-DwAOXWbssnXWLf3xkuXZuT1wpDeAhHb3QGnQ_76hFHBwhWmZ7c6NhtU_w5C_spK_QEqmelWBASFWU2Pz7ffhu5XV3sED02rsobs5OPy32lpSTI2F6AXhrlYuQmpyLnzEPRcpekjsWLD0SnqgBeSOLmB7B2Of43MsoFcLlrXF39_nkMGoXA506rZw6XEM06Wxz_j8q4rXEPPFgDx8m_vT7I8tRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=tsdtlvYf5Q4ztE5fAIMoGNHMB7bi36PvmA1p9tUYt_1-2c6lMuqxpB7nner85g59f3HjZ-9EpXLMaQ0oKtH9IdcGN1XIawfmb-jYyvyAUIu_JnWzoQrIV8ki68mjyHGnixf4Bk3mSZrLN4ED-MwUROqS3UYBtp4vxd--IPI2KL2FDBBABX64mGU7ek1rVgieookPOZe7mvQVKTzL0-ORoOwp7L-q2t5goGbWLRrPD-gt9Litjqu_eHCbezNchm0E7mMeuqeQrLXYz2lfd71mmK6HtaCNVgGBT-2ST0z-MnYEpkKryZXzJaD1Ue3Nn3jNApga24xbbmuCuVYqla1Imw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=tsdtlvYf5Q4ztE5fAIMoGNHMB7bi36PvmA1p9tUYt_1-2c6lMuqxpB7nner85g59f3HjZ-9EpXLMaQ0oKtH9IdcGN1XIawfmb-jYyvyAUIu_JnWzoQrIV8ki68mjyHGnixf4Bk3mSZrLN4ED-MwUROqS3UYBtp4vxd--IPI2KL2FDBBABX64mGU7ek1rVgieookPOZe7mvQVKTzL0-ORoOwp7L-q2t5goGbWLRrPD-gt9Litjqu_eHCbezNchm0E7mMeuqeQrLXYz2lfd71mmK6HtaCNVgGBT-2ST0z-MnYEpkKryZXzJaD1Ue3Nn3jNApga24xbbmuCuVYqla1Imw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=MoP2_YasLZTuHVrcG4ZUaFvrzc4TfZVwRQ9aMphQCAvCheYNyu43tSz3sweX8pQ9DWSBPws6gSbtNvsfE9bhysc6AeTpP6GH_7144ay70-1flQhY4Z6siMSt2q_n1l1EtNo1cQ-_EhkuVq31Ls4nNmK6p1dzkh8wuLQCxotLbK9dY3pFRqEARZpTGvNQL1MmqBYiDjs4DbvAKkFhebGkPpgQM9A1fFfHv_Nq7lj9wvg2X1-YREaX7TUW471sxE-pIybrmOkR-F9Zcr7uIRwCXV77GsANeNWBdFJLqiy0_KTGZds67jkrncliLtkzWcQXavenXD-_lhf4p0D8KQW8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=MoP2_YasLZTuHVrcG4ZUaFvrzc4TfZVwRQ9aMphQCAvCheYNyu43tSz3sweX8pQ9DWSBPws6gSbtNvsfE9bhysc6AeTpP6GH_7144ay70-1flQhY4Z6siMSt2q_n1l1EtNo1cQ-_EhkuVq31Ls4nNmK6p1dzkh8wuLQCxotLbK9dY3pFRqEARZpTGvNQL1MmqBYiDjs4DbvAKkFhebGkPpgQM9A1fFfHv_Nq7lj9wvg2X1-YREaX7TUW471sxE-pIybrmOkR-F9Zcr7uIRwCXV77GsANeNWBdFJLqiy0_KTGZds67jkrncliLtkzWcQXavenXD-_lhf4p0D8KQW8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfq0sfFpSiZ4DBFVjepFjvRlsGRmYinx1vKR7CzSCxcgwDmNg2mgXb4-NhgDGJvhuuYaoco_iO42f6zMcWi8fS377CSOc7HGH05NPs1MF1IdyslI5e8cI0ZmQF12Ll8KeJFkc-PKI5bK3s4Z17imcSzLK5Vnkg3VOl3m42dzsHzSa_6nvI8ilK4yN4dMo63kGbbh5UJG7xfJ9y6dem7ukINpimQsXM97LAb70m2DqlHwM4qbl8nVlbO5Z3BcUeHmdLu_oHNCV2TS1UGl5Z2CDHuGg4jev2GQT0SXISEjjTXVbDZ-cCHwAvCHT_L_gTrU17xAcO8v53oDWlOMAHLd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=iUpM6yqvsmbqolPxynxRKxkhncvUYr6dd-gQTCBJzPLGdIBG9rZGmXp5pUQAqvDdBLXbZuKe5it7QlScYYqk7I0sW4xaw__q1rIGAIKcLNqYsL81efHzS9yN_O__Z7wHDQZcZca9GFjIBajIHOhmCVBShvEa2Ru2XSesYFO2UfKmLp6aleDcPHcAsI1RdLWVhCpE2WzAEa8lLMgaezW7EE_Jmfxj_AKTVC5DgsSEhGBL8-IGNyc7B1ObNxmhHkty9gGgKA0sws1gLBMfKQuGVMO4AFt4py5ETOB_WLRBNrJksZrblgBQsynuKbUlhca_1cwGjFNdCWp4oSgvxeXIqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=iUpM6yqvsmbqolPxynxRKxkhncvUYr6dd-gQTCBJzPLGdIBG9rZGmXp5pUQAqvDdBLXbZuKe5it7QlScYYqk7I0sW4xaw__q1rIGAIKcLNqYsL81efHzS9yN_O__Z7wHDQZcZca9GFjIBajIHOhmCVBShvEa2Ru2XSesYFO2UfKmLp6aleDcPHcAsI1RdLWVhCpE2WzAEa8lLMgaezW7EE_Jmfxj_AKTVC5DgsSEhGBL8-IGNyc7B1ObNxmhHkty9gGgKA0sws1gLBMfKQuGVMO4AFt4py5ETOB_WLRBNrJksZrblgBQsynuKbUlhca_1cwGjFNdCWp4oSgvxeXIqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxvYnzmJ-QtQaN0p2S7e7t7F85J4PA81uh1Uy0wMe3b8jEVWSm2kf-ziT_CX_CQujdfTE5-fO-0Gtuzh_W8TauXw8vL-NvjW8EKBUL2txP8rZZCxO5uCNBcJIks7KusCd2InTW2Rc1JC1_pWWguw6TD68NssRVW3931NabHPoEpsT52x12ciRiHT6eCObyhwhfI175rbkV47iS85OAU26aFb0q-MVU-mVi3d2bDML8OB1TfXckY7p025ld0V4wBtYK8J8v2cuf5cAg9hKBE8acjelBip-bTxqvUAOce7PsW4ETtFdaQCytRyu_zfV-WHLOC3gWULN9WxK2snKJDEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSRFgWDptkbFCzADVO_Y_UO9xO0hHLZuX2F7cHgWU9RCjsErKE8fdx2UcQxoEl5lortecCprLRJBhOZxu5wrDDN2zm1PuQwAC3EiO7fWJ2BJ-mcVe1v0fu3JmHT6pKbfmHGSyPy8xk-kE-ISCMZbvp0YV6YI90UWXDpg2rWQIvb0-3w2ibQ5YC1fmhWwNWGdbN7GrMEdfB1isZb1tc5bJrtzy7LEM7dm6IQrKgd4AK-gvfZ--2dqsex9xDBwoD5BmqNZWrIep98LK2sGPtHJB9jOov3VOWf6mv2ZSwfaKpZUB7SbW4jpYfBFy72aZfmLyEM12Ah-GxPzqYd4ETLIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=jqkS3-QBfHezS4rbDEJOm1k1-MeDinFfQsmGNoirJmpfhUdUgFS6TIN-YhK-ALhje1NNDZHCr4qJgLOdRueZmv2BI1ofFOvlEwvjid438Di8n6wGwvhqh_Ct8oMNatwMqWpYJmS_6U3AhauAsk5K1xGpTPo8PHvkh7FuC-28WLmL0ktmIMacIW_RRyThNdwb2Jvp3Vbyqc5K8USXoaNKTvZbsTFruioAfM8WPFfJ-LC9n-GKuATFqzRYdvHcoxBCUf93zEl7LhVmpiY4KEn0xqA0dU-r6ZOCRpdIemBabvSDGu7H1EqOJ9Y6GASluURPSmhQc8w_E0MpQzWr64LuyEbueg-Z-QDl065vUGae0XfBOyeI5P5xSTwL2PKovxW6OGvYKZ2yinb8DFReMsGucDRRh11kLJ85673f2AWpvB4AyFHDuAhEgkZ3d_St8TSM7bt-BPibsoUWr7pq1zUsN7T1oMlQpPKPLR3zx1Qnu3wqB6Gyg_3c5GB5wgbX9CGsv924y0YaxUPB4xdLNxxE8UQrmqd4wtU1jWvtVNrOTDjpTPhrSf85IuEKcMNk_tyqg3N7Y0o0gJnSz7wug95H--mcaRNLY3xeOwX9WiceB7kGjeTmMNmqxLnZ4xGDrpI8va7ucjLGo7cvn9cj_vhPLn4CB2p_SifIe2_YFjGhbGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=jqkS3-QBfHezS4rbDEJOm1k1-MeDinFfQsmGNoirJmpfhUdUgFS6TIN-YhK-ALhje1NNDZHCr4qJgLOdRueZmv2BI1ofFOvlEwvjid438Di8n6wGwvhqh_Ct8oMNatwMqWpYJmS_6U3AhauAsk5K1xGpTPo8PHvkh7FuC-28WLmL0ktmIMacIW_RRyThNdwb2Jvp3Vbyqc5K8USXoaNKTvZbsTFruioAfM8WPFfJ-LC9n-GKuATFqzRYdvHcoxBCUf93zEl7LhVmpiY4KEn0xqA0dU-r6ZOCRpdIemBabvSDGu7H1EqOJ9Y6GASluURPSmhQc8w_E0MpQzWr64LuyEbueg-Z-QDl065vUGae0XfBOyeI5P5xSTwL2PKovxW6OGvYKZ2yinb8DFReMsGucDRRh11kLJ85673f2AWpvB4AyFHDuAhEgkZ3d_St8TSM7bt-BPibsoUWr7pq1zUsN7T1oMlQpPKPLR3zx1Qnu3wqB6Gyg_3c5GB5wgbX9CGsv924y0YaxUPB4xdLNxxE8UQrmqd4wtU1jWvtVNrOTDjpTPhrSf85IuEKcMNk_tyqg3N7Y0o0gJnSz7wug95H--mcaRNLY3xeOwX9WiceB7kGjeTmMNmqxLnZ4xGDrpI8va7ucjLGo7cvn9cj_vhPLn4CB2p_SifIe2_YFjGhbGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaUxmAqEKG6jU7Beuq_sPhggmvGZRyks6C5GwHtrUEZqfOcJKuOWNf1ivSLERGfefsxTibNbO9iZgqLopYVYK28cO3SM7bEm0GiouOFqH6xRbQBjicFo5Sn-qDEJw4B1LU0YaXzUxtqO9fUbDspp-19KBHNlmcB0AI-_eBbaf1Vh-nICVpjXJAG8lUmb5ebyOSAl7uz-WVn7JGa7Qr1KqQY5sFHNH2jzLIWCvZ36DFzADh33kayyOg9owGF810Dzx4Ze2BMxXUCrxc_CZA2SRkGIDLfQkk6MCBKxhaxBDe_3tKTQwZTFuMtcjMHMIUIaXdkcgc-IIrN97k1-Mt7QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URToScZ0gG1eXqHYZAja9XIGEkKFNFIEW4fSN5Cn3KB76aWx1vO5dQelLRR5mWIdk7hUpM8bitaqQQV95jjLQoOZIambuagygKdNkQAunpwvc893RdLYyx71LOHQrawPOKugLnXttyGN0jenZN_75V13WsiEbUxu4kBM0uW90UqpLvbNITt1WFnyNuEel9bSL8IqJxFT7ZnoTocSPlbx-qOFlNwYNHeWRLq8nSOiGDip-4ziGeTB3yIRxXiiGJeRA7nRPyPriQp0dx2uMVJrTXnKbsnUaJs8T3VRT7KnlEHrIMe3f9zsU9IgNlgBSKo_C3jA9e-Ag6mwHSEn91MpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edxEYLnGU2CMwZV8qQZJn0iuzi_KZ5QbH2C16zlP6fxEdsP1esc4xsrlaZwZx0UhFXQ82GVGS5PD-lB_j9K9S5_DBx38LgNn75T2AfRGlp_6uyL3qyPY0QjJSiTOptU7aaFcA30jUXpqtQOmRtM6PcsEHGx20jLQziwzkL8SELGXwaqKUZcfl-3AoIIbK8kTBE31i1mug_47S2i0jvSWZ-qqW1-FMfk3GxpWUFlvzO4Q7cKzd5MQrSe1aJDRodMilsXmBNh4iNvX_q9h-KilqE0ypMp7EATFOZCJQVCASV6PzfBHTHogF0XVDA4wP1ilqIaVzBMOHDF76DebUrKjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvIrRp7X92eGyxjPZlb-RH8h1wGdbXNOppO7yblgVAzI8fmThJdWfQs4Rc8muFKrV71FF0zO8lDn6hblqZyE4sMAXFnRSXJTzUzP72mFKKOyPWL9vgwCfb_hNqWSjZKmFDLkx4e0-prZMxIVyyoueqql8htO3T4pQZt5STRPxuZLCxH-0xDGeVXvknYqxG-mQ0XHeYsdkWAvmtIqciUuFQScSvb5f3l97GMD49CRdi4ZlLxyyTme3c0sRo-3sQPi_GmFJT_Q1Sz4f5QUxtUfqkiKpyFSANqA8-FiHFEnouWkDg5vkar-KaA6LvFDCFZjOFPYwtlWoUxb3895BbM0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r11
📱
@winro_io</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22590" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p__xcxDA2wNqJNmM1F70uui7Jhe6rjSVydCWUjoqwhriHYXUk-ikI_Ry_8IZRT_3fgT829u6YJN2lr37uiJHJHpOd7E2nkNHM_vCbBlrbWkE7wfBbSvwTRv7R46WBOFoStkwuCAUOZ9aPhK_nHV15YHwGvdhdvoIzXCiXoraGYr_kYU47hEBCWyb8CPjzR-ATCeHZ7fq2wa4gTDPuDh0vnrdHv9AtchR6lidI81PiViKcIKbUyPU6Ye0nsiByyjsFvQLc9cGnHyj7D1A73ULifP7KF_3pLcHX0cKerQ1Jzxti0Ho5DJlkOUXbksFsXxyZyHteJE0KHIayXWgQk8UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc7wbwb5mHG-Iqzho_QSy356-ZPuTet9CD2Vx0K2Iz89GqBHIgAw1Kc3UvFOyzHKXey8Ry5z3kSxM3l9VQwASJfGPaBn8htmUODs7bTlXCfFWAAX2GYOy7y-FUgfLZraHhEtB1RbIybiuimRwaoAFzMtBaQfUzvgFOpf_O_DH4HgKoRNGHiyMKphBpP-RZShBezx4uRSxGQwm_cY_V6mZ6nIDX82JH370PuWvCz_78uGkT0Y3iTwISnoSAGglc3dO3n7ZL_YY7Vp1c7F54lWeHPTlkC_rZftfnKVbudrTzJjPEWw_fh2IYHzu-reusN9xjZUz6ewCjJlZDcAyWQJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=rvM63zeejXLh2P3CL6YTs08qUpEqu9RkW1cWgVvnQoWnY-mIlewjYsPPVFeil4bQHIHwibQU8LpCUkxLr80EwP_JVNqkVRsnkFRGDtuCw-PKytGQ6kK2l-GQgUZG5AU-HTds-PKdr5RdYJeQWEzfmXmon42OUFxaym8xlkg3biI_oI60vBokwVUx2xzna5d7pjDl974ZVPzvL8cUjMrIZR9MjA9CluBMqNbNMKmfYuQrCZYO6TCpAWiTiSIrlRjv9_OGb4d7VGubFHvL7-jhW3eGGtGpUvPI1V-EgTPRbxNUROZVTi5Wh-m-zMC_gWLJGOCbF_uya-nQ5nxs85Mf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=rvM63zeejXLh2P3CL6YTs08qUpEqu9RkW1cWgVvnQoWnY-mIlewjYsPPVFeil4bQHIHwibQU8LpCUkxLr80EwP_JVNqkVRsnkFRGDtuCw-PKytGQ6kK2l-GQgUZG5AU-HTds-PKdr5RdYJeQWEzfmXmon42OUFxaym8xlkg3biI_oI60vBokwVUx2xzna5d7pjDl974ZVPzvL8cUjMrIZR9MjA9CluBMqNbNMKmfYuQrCZYO6TCpAWiTiSIrlRjv9_OGb4d7VGubFHvL7-jhW3eGGtGpUvPI1V-EgTPRbxNUROZVTi5Wh-m-zMC_gWLJGOCbF_uya-nQ5nxs85Mf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgCnRRyLGKJxUeTXLkJR99DUJL1l_w0_m1BLGV3bb7lbf2ENAAHk0TTroiatFYaW5yoZhEDPvrWkJGe-d8pidd2-HmrV635wK7zRXhzTLcAmmpcMbN0Ly7ZGhjZnN1oKeX3rgvp686wLSo2Ue6Xy7pcY71pSRjaEXpqb-kNNfz7RALZy1dhk9pc7aCpoYLXX8QYUCeCJeyrNKrFKzIrqIpf4HgqHctQ34yda1QVBYy7Fv9Ven8nF9gWQiOqF7_4MH3peBdl8-S9etITj7dFGKrJgf2leEMW6AlcN9WMYRWJyuhaj83vvfb9YyiXWE3zeKE969ULAOEtII1V3Ftd_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=rr1v9onKhKyl3GyUmeASouVQwnWu_2fo7TNOed52a4o55a3H3mUCsMVAJzVDKjas_qc07kqec7MdGHg2WZ88KvkFZuHngb52cAiuiEXycrs2bXP1ANJirx2Vp5X-gs6HNMISFMqjL3tiQRbECYKGpeexwy_7dJBzGaDQ1H-_9gmEkZKawny9TepVgsx7a8YFPuT1CIv_GRPd7gsuANeKKM8d78i0VRmTmQJx4C4d6kMDoQkG8FJ2v6JuBlmR3KvWYPOBNj55VUEI1wVpTPv6BMg_nw2uSrYLoBFMTCyyCkxuCW_B6305UD6w5azGvV-9wE6LmmQie8n3Ock0Xlov5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAf4evg3BeTC5n7GMOeq3ZV-9NHUVeallLyMXH0d_-6yqw15PgP-skp1eAcKhW7clWVXnfEWRkqrdPLJG1mrXnkU0fwJ9M8si40JST-AAggbF0oPh-Clu41k9IbAHzfzvGmLMqahxiBXHaZJR4O1B_jtP_PaP726BJzP2qTG_aT1a2w5NpAmUfZPSq2RfwhT3EnmBr0bGwyz-9PZ98d8qSYniwOofFCLr0S1x5PM_M8YvSrDdHvB5lWTdn9CB-MuPKh0oDyzb7Zo9WYe71jcbBpUzcXMKiXq_8TwfbVB0MwsLnP645fmPT8iGgJ0IdjO5s0vp_Gc90rOsg_jeASFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X32CDIjc0sXtoGGrOMKhlADzL8f2ecxIHLUeulwEdQWIu4zPyVyrEw_sQSkzBdBcL9JZpCmUh0wNRGLCrMwh4WskUMr3uSA5fgTIEUEEdXrm_szMTJ8vi1lVueJmIwIrS62DED8hs301ZfrbeUxwL2tO6hsueWaLehEnxQKpE4giDjoEDkrsZd_bd1dC0mPCibEW1isw5A_FL489Q7HNAxEGVbb8v1ZawIboAGQRApynTP0oj2DMAdg4GGhKIjbFPj-_u8WVsB8jtloSYBlVI5w_PBwzE6wnnMlam6DyipG1uEYoePhGkYpXbIchBHlH67SDLa09eRQh2SrGLxcLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zuta6vzO7GoncmxcVfj_Hix6pW7DL5ZcDcpIOBec1kr8kPso3yR4KopLgnrDzsr69Oos-tBr9gOYsXk1CrFjqC_dxQN4uSnDC1fe3G04RI9J9l2rZqw4ab4Q5N0xUu39qAbAQl2oeQWtgPsHS1Em7JOmhHJlk0kQi0_Qc4GpkUoKDaGSZ9sE3cbQ_pRTKIJb8_psbl2FV_rRsSJYt-CH4JiEDbs9vtYDFyZUC4f4mU46eh9eL7QB_BDfR50m_ofNVVa_G-456bbnOOzBoTs0B1vk3CDk0ASH6b3TzD-yImBOkQd5oucIlytWnnnQLlOxaMZ0Pr0TBALAXmWN35GDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk8Vk91-2HDKE4k8hTYzSnF9ObA5t5o5g0DbRJd5X43RPkjgeBTiHso0UDauYEV8lZ071wNmgOKPJzfAcQkhnVQd1EOQLHaGRvHNgXN5Be8y-z0NH3DjBSNiHXojH4XUsoSsYx4aLnmiRcOiPrwojQxVeIR-V9rGnN_qQ_JgDNgSASmqsNbai53eQepwrw51sokBtz4nx8hOAKcKs-z-35InuLJzNayB-jJfC-fQJS29VJVC3eSqBA0jgEIU00oyArTIuo6qbQ_vUghzOeof-K-tz3upMAOm9LYGK2hfy0RuDCPGZwxAf0fIvcZ5wEMSDwFgxRrbQDQ7JN7vGpqBqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk4k2R_zfZp7sm_TdSwudMMTUIb4IM1FjTtPHfPi82Dh3-LZFpSQUTtRX4CGx4tCjuONRV1jtQiLPXnVJTxgCpBjMna2yWnfZ1w5nDNlIm8-Qte3y3WP-3X4ENIo5otgk3Xrtm0aqzZWcWcLBTYX6MTFO0t-Qw45xW1m75LLyrkaLvf2ote-g9ssFX4lYPd5OuPNrQFhQu5pGZam02aeNlh4EtKEbeWv7wlD15Xf5scinbExXIWGD_H9xa7sYun_FVm4-QDsmUlLZ0My1bsvjr1vxme71q7VKxdaaw3fP1ln8WCi8TrzgFxKO9CbJNvCJxlPpNaI1a-p60Sn_YFsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=OCkn_Pkhhl6hAWAo5wJGoYDQyVQd5pYrYq5ssm1vQsEMwzaCDB6nqu6WGEsuoc5K_9RSnJlbaMonTuiYFQha_iS37yBj1wN4MGCxfHntovs9BTsaUmk5zcBmk94xi6CFB7qFFWnBF0eak7pRRyyZsd2uudlpwpNXI-XEnyX4WEooVJS2b-HgIWHil6grlG_Ubbl2o_sETbPAnymK4GSgzR3CDRDBnnqZ6W6bJ5zfHlqknihwBu1ax-Dt19qwscGFN6J_YB9ISXPcDZWdlHuq6ghn7A4rOh90EeQrnYt13-f480V28BUuhsKRMUxCUD0bmg51-45QQgwA9j27j3Xb9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=OCkn_Pkhhl6hAWAo5wJGoYDQyVQd5pYrYq5ssm1vQsEMwzaCDB6nqu6WGEsuoc5K_9RSnJlbaMonTuiYFQha_iS37yBj1wN4MGCxfHntovs9BTsaUmk5zcBmk94xi6CFB7qFFWnBF0eak7pRRyyZsd2uudlpwpNXI-XEnyX4WEooVJS2b-HgIWHil6grlG_Ubbl2o_sETbPAnymK4GSgzR3CDRDBnnqZ6W6bJ5zfHlqknihwBu1ax-Dt19qwscGFN6J_YB9ISXPcDZWdlHuq6ghn7A4rOh90EeQrnYt13-f480V28BUuhsKRMUxCUD0bmg51-45QQgwA9j27j3Xb9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGwYGOwIN5rQEAbFAc0OmS58Yu_R0lMr8P9Je9C_WD4g_V78yCLgfKz4Vz8xG6GTzmXyIYI3a9t0_89C2dLe1MRAHiDnQ-ztBBNTHXZmOTzKajkI-0D0ngicUnqnZgqG1NVab8f0hVm7JiblRrX4Jc1R7Jj5g8y11s9GY7jDH7wC-NoCA67sEYBTyXJqF9ddNMaFcSRQZEscKFWkx-lYcf6_qgOKoaqPu3ebVzvePGD9jotyZdE9UACQ7yzGwCh_D6ERkjNXLJp4B6-TICG6agUf3PiJQJ4c6d6otsyhSLYTj3khFZ4vrvzmrQFpO7fb2foFYpiog3OZP2lbDy7mpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت‌مستقیم وسریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22576" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NB3otKRfpVoVAIrByZlhPo5_Mm-cr4X5naXTsZGADwq0bckx3T_VqfD6ewztOZ2B1KKEM_ag-WPLi0POQwXg0QAuq-HldvWj28UaOf_xsoLzoEorDz25l5-lW6vmAMMNYCSGzMBmrbrKZ29eOvbTfByQVA-xBfs3qIZjUO9HSoyWkGGGXER-683aWzLLQY7hWM0PkdGWhDBXQnm_edDptEcgQX9KO5Zhsg77wPYj6Y-uoMyAxM057BR4uL4HiTL5lCnOvcVh8cfHsYgS4q-uWaNmNiT5cvXB6n4awPn6EJ9R9cjfFvuAxbgIMvkUFVCWgT7L9ou4K-foEu1nDKZKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFSe8_LZOPBnZqRlcJTD5KxWcl6GSiOgTepq-6HewvmaD2bMuOOWKzR-P8kzQz_shT0hJabo7e8hb0E6EY1KiiLlQivNIltgUaIAJ3qt4L3B_eqmLQuYtsuHbmW0MI5S0rVPRuL04H1Z4h1kA10-xwGLH37_PZgpzalH3RUdk-TRfOATFO5M9eyacwxD8m3lq-Ae5shD74t59EBIZPoTXyHH_KY4VciCqCk9MtRYjm4YGASdUiq73bP0Wp_uF5VLcgtSr2fCOxGx-MrKuH96oCCOibNpIO8kCWfkk64pc-NjHLKBTh5U5EYnLqKXBWXbgE8yzt3EpwiWwkCv4tcRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhhCnGl08o_ocl-2nCnz97OBW0SR8VjgSsn2v8zhoqlX51S5M1O3VcGKLRLweE1rpiE_38lEMGdvl8aLELRw3IFjantZj1CkWQj--dM8qEXGzy-Rx5ubmX4F0c0xN_MX1AngfSmj47Tzd8Qn5D14QZrBzG-i2YTlV1YRJY_zWnYpn2oGjMizDHLkD1wcTtw4VcvPYw34kSf0v63LamD_6x584-6ru97-CDsbM7UmEMPS1tJK5XC08EMHCkDn63Kfzt9M9BVuVT8aK68-bUd2TP2E2E1NAULdkeRPfPDiTgAnrL4O3gnwTGFE1_zOOfQhMyE2MLxO3ru9cbgHarDAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=RojQ7lYVHI4zHTxdDYoY3QvUfoJONeMq_5CAWOSiGlJg1e9W4GDIt8txO0UtS3wbXZqPI7YdG4EAyT0wPhPFXA0x8_MCuRLZVHwek15tRGPN-jw5Hd1rWVT2WCukvn4HoJzhDlppAQ9yKYJNyjXD4Q8ZyhtP6aKzFfcUVIK2GzWMrCoLmeCG2qQf8m76hOprw4Hj0BS9QQ4xqGIvM5TT583PrqRECocwglDtywqiVxcPj75qWU9PC417VBSOhROlZYYlb-9AKM-E17TPjylhimDppLNPyxkwM495SOtiNIHF7dt5efgdP1lQ42U89PNdYOhhMg5VxyCLqFg9grLGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=RojQ7lYVHI4zHTxdDYoY3QvUfoJONeMq_5CAWOSiGlJg1e9W4GDIt8txO0UtS3wbXZqPI7YdG4EAyT0wPhPFXA0x8_MCuRLZVHwek15tRGPN-jw5Hd1rWVT2WCukvn4HoJzhDlppAQ9yKYJNyjXD4Q8ZyhtP6aKzFfcUVIK2GzWMrCoLmeCG2qQf8m76hOprw4Hj0BS9QQ4xqGIvM5TT583PrqRECocwglDtywqiVxcPj75qWU9PC417VBSOhROlZYYlb-9AKM-E17TPjylhimDppLNPyxkwM495SOtiNIHF7dt5efgdP1lQ42U89PNdYOhhMg5VxyCLqFg9grLGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPYNM3t6lWayjYTIyJr4EVlcChWfNRXet3GuLcwnaLSAY9WKLOTkQgqbJyU4XyZKELr1I1KftFc7UJJOKqCE5FruXp29NTeDJeOg-H_pUavVab5DKm_HxZK-XSNiSDIDryh1N665JJB43sXScANAWKOYvojcH8I1hoyjVbT7aR5uYsSrsreGunjONhMAAlxDo1qgK0gKKiDrjN2vbC9hN9SPVbiDlZ4Ww3XJhRooViaLlUhZxgbfgEl3-ZU3Wf07oxr_0svJ4A6bzw02vYNLIQ7WXOW7bNFczo7_emy8OJi1oYWTmyeufoWTpRT9nxxluMZmzr8VeLdchAieB2lYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrYEI_7u2_y41DpoBR9qvCHcBV9hcrzAgcWpOd-fBOEysyeQ4sRTPl1HiR4XbLmkGhW8c5eCuacOFKv3BPeFPZk7eXqGb4gzrgWeqc1KgHbLMvb2zlO13b90o2XgC0qF8AWQNX7hf-ajY1arfWBgkmMvOAtSTxCG4cMeBSTYyZGXp6QcP5xGBeKEND-7lj_qMXVEIkvUrWLy6l-CXQ7qWAelK9gsXF_RynCBNEfDXpIjg5JjBdk8O6to1fqSXJIE1Ye_ipAhadkp82PZk1vNjfO_Yg9hzYINwzG59QvYtVy9w4edkOV5t7n-VEXFDtQPt-2PUs-E0pPBemJgDmxV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCX36jcTk2K10x5vaGvSjO4X0gCHSbXthzQm5_BQPXbOJeM-mFuUXKM_rI8ucKJvJAUAXZ7n5n8u5Vth5mIzhwvipSmZv2B3ECRKkHzc43OZn1LXaeT0fCTbXJWf3EVxNevI0o-d5MppR3kcMDYZCY5uy24Why_0QhpRThv3touBZeXJqEd3tZvu4Jk-cSMjUQGAx4NqGJ4wpEXE9NeWz4PUfNJ0cubF5fWnQ4eAOApfuyaBXVnYmjFtu8_bunzwldaz5UdKMVwOfPG-pq4E-olZhNkekBl671kjxCZ2phbbtSFUOOUMkhtZQfaNu4wa8VwV8ebm9bwetUh2IwwD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo39KttBysmgQxrtkgtuhMsMedFuJ9Tj240v47hAps31KSpN7XX1e0kjoOPBc9InXRm67gb9iPBy1uG7DOn60jqDUq-MpwaRyQ-Kl9wbNu8ra7zWP3UZixT6-pap8kmXGemAbYCZTzqFdz0divWT3WjfptvKM1-1wzg-i9_ptptx3qzusDA0s8sJuQkHcrYOTVN-hZXIg7XpUH6XCYwKFaP2kH--4ZDXz-P6mn_pphGDqG4Z-zs4SGW3sV2UAA0_gwH-OKaY7_JEQoXIoljoN-lkFJMiOBQ6e0wByyCEmmRO76ZQq7KQ-xufF2UeE85SL3-BWT1MWWYN2HeIJ43otA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1eVORbZ8-GPuYqgQoADa2wA5I5zJ_8eyxp5vFg4UheSHaiXgGo9yHg_DQCxj8w4uaXVr7isHVtXvfk1wy3XNX5gXXcXYHexAMM3YYABoxF9_ByF0AoE9xLUNK4vPeKDRYbngGuqzRY15M1MdZvzmw40quJcXWwjIPLnKQR3c3NshwHNvNvTqbXi9WtC1TjlHM8mBcaeWJ-bKkiZ63UtOwqXzA0S164-pczrPKsg5wcwbOBfxYsZo7liWE1tEM9n26MiwHPNSg4ru3n17_uCvL1qjffvz0lBxx9eK4KjSo_AncP9W5cNHaXzAg7lWIGiK4DU4GICsZHiSkwQjbpIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8r2Fy7m9apY65nMLl1qAfcvfbAcGl4teNrVyHwQD8iQP2oh7Yqz4JE12ze3aCKBcRl1AdPxpAPtFct7BvIez4goL8V6XD0bKQbPP4nf9jf2NIVOfjFxi-VEPEDLwpDcV4MRZJPysfg2gbdP297hClhs2L76x-KPs25cMqCpxp6nChaDyKywgePuOADpgiNFojPJpouZw7-U5Fa4-vwPWOkUKE3vVozhZMIWXkwxpxxjbjowgtgMcF1dcRXMWSfWIJsz_sM2fJVjvgggvwXeEOqg6Sg8xEEYjL6U77N4l73Rk9piEAFoQN5RQbYeMe6kRWFU1zxYQVlAt31MKuYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzj6njEkfUXDuDhx04ZDkmmGoHqaUe4V9B409e9CIGvcwQ6nrwdsJrNsz3lMuGH1WdCbqjksp4glg1uYEZ8-3aapZ9KTiTbrxUW1c9VBY1oRqt9hH0L0ZNPpLis7QgYciK-X07Oz0Cm8rX9tkIZxxEjkppZrm5R5khb-9evO6MErHjUz7o8kVmHWPzfVaE6g1niehP87qwLe958vUirMi77tyt2DIdJLx4HMGya8O81bn5ayHRRa5EXNAiRsc6B58pUtugR8IecJtCVL8hdRKIm1M2BbUvcTDLzEBmt9D2g32dYaRas62UiKQQxSqEtWe57fZgqkYzkJ4w5V1vIEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTcTnL8p1vkYlGzCBACYll8WUNXitnvWCkj6NzjIcCyan9CyAKyjfSrNnvyIRIHf9T6YCiF92z4EzPSeQsk7G8eUOwH0RtSW3WEzYIYIaxDTcnOmANZ_xKxtCPtRMG5fvcLqKzv12AG9zcnOm9J4ioic7YX5QlclZk_V2Ws-Bt3VbQwmSZ3I_28eiOmpSsSmjpyLO8Dfc6QpB4ENMSP1iLD53x_qMh6Fs8GAuX0B9zUGWzyVbtQGgnt_nDIBCJqQ5ViOb3iwZHbUjIsP0DO6G_NlpNYPoSrTJ2XdekNkf2ZqPZ9H9ohNqm_pgnySZ3WxdOFvJ0ig6nvoqgQyy_KLGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=rEi464Ypdcg5N8q5XQ2skUOM6GnjV_wkwXzBITXXK_GTaGNGSd0SCBpalsXasKQTUeVfqm1gHkzIZXABU7IHgzi9qpBKEfo4qvoWmhI-kPQbiTuNWFsOZSzNNXsgJ5baR6gpnDhKOUTSP4-FAY0ZTdddHbrpAu7q1d4m--wwOnt6VdGBfvh-j4iQGKDI1Zv_MJVp4o1F1XI33xJaGJBY12h5cQFRE2gGHE2TWCwch89_0fp49n2H3qKRw99_llbCyz-Ra4leEXdgXnbiDT3hLy8UkZCstjpnphbos494K0P6_j7kOYh5X5ktMwR8dVUbwYuuUEbOllxFuACvUBxsjwi_tWi-0kh1_7ZyRykfUD7t4QCHcXY2HVMvzLSF_uSoppqYLj68ybcD4tMaCYnV06kXuVDqW82TD3EoPaoduZiK05n4NoNz0Z_SyBVcR8RNl6HkjobagNBAj_6sDc7xCB3qAhF58oQt5P9S4hxSSIMKEV6Tzj8c-0WDrhfY3g1OvIZ97OOy4XtxYDwhq3lic_eUJSYEFXHRgIrVxm5qfe37UF2paayJDktzOFlgqZfDqMbO8Dx46iw7rmgxSqkoYfYVYiuBr8xvThprWcD8tCa5SYX03C88rXXhT5V_24HdAMQz0k5_wVxt69P5Q1voj4OOpNBrTrcl3xYHm-b9bjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=rEi464Ypdcg5N8q5XQ2skUOM6GnjV_wkwXzBITXXK_GTaGNGSd0SCBpalsXasKQTUeVfqm1gHkzIZXABU7IHgzi9qpBKEfo4qvoWmhI-kPQbiTuNWFsOZSzNNXsgJ5baR6gpnDhKOUTSP4-FAY0ZTdddHbrpAu7q1d4m--wwOnt6VdGBfvh-j4iQGKDI1Zv_MJVp4o1F1XI33xJaGJBY12h5cQFRE2gGHE2TWCwch89_0fp49n2H3qKRw99_llbCyz-Ra4leEXdgXnbiDT3hLy8UkZCstjpnphbos494K0P6_j7kOYh5X5ktMwR8dVUbwYuuUEbOllxFuACvUBxsjwi_tWi-0kh1_7ZyRykfUD7t4QCHcXY2HVMvzLSF_uSoppqYLj68ybcD4tMaCYnV06kXuVDqW82TD3EoPaoduZiK05n4NoNz0Z_SyBVcR8RNl6HkjobagNBAj_6sDc7xCB3qAhF58oQt5P9S4hxSSIMKEV6Tzj8c-0WDrhfY3g1OvIZ97OOy4XtxYDwhq3lic_eUJSYEFXHRgIrVxm5qfe37UF2paayJDktzOFlgqZfDqMbO8Dx46iw7rmgxSqkoYfYVYiuBr8xvThprWcD8tCa5SYX03C88rXXhT5V_24HdAMQz0k5_wVxt69P5Q1voj4OOpNBrTrcl3xYHm-b9bjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeAhD7pzqekfQhtRv7VuxhfxiE0Y6r909HVQljGwmd2JE_J9RTXHlOhqJ46aiGdBQQwWPWXoUwkczNGQDfHTwVhLUH8582xmFsfhVs9K6qMbFInSyFhrP4UbR53yF4hfAcKSXQ-11i5CDvkfucfJiH4FIdIQraeiY4qeU2lO_TZW87rbFsgraS0uIzdnOIUt2_gLgZi1QQe-xEE52nYeJZBhpXBqAltfW9_6okl9KMLzahawr0O2TPOabzoVhQ7p9Ps7G8jFPCEUwZbsyvKYNvVXzCmo3YVX3N0pj8YbzcjjDrgqZRWbr_h24ALdkIuMFnTKxNI9SrSsqVbrg2D8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc1TFKWBeYQnseE9LPWDA7sSCEt2TJLVclxORmD8J_-rfyMR6vr777Jo1kQsv7dZxtsKykI0xV6nCSPvyrcZjpSm9qi6SnYK5W3wDO7IOaTvsgc3_8A_fLudUbDkq6j0BqaRmbVIHiTNU8Jw59nLIE7PKG648bKpIEif_plyfgGinnXWrGhp0tneBxnBIsHw1TzZMSDpQzSk_sk9gvwZQQJpwLeA77gCd7xn-BYwiOuPch5pqWhKLl90gBRPfQfHvtBzS-RoanTivYRWCHh238EU5Ir2WuSx9XlqdiduN_wide-tbAl8qLoeKJCuXAk2GVr2ybqRPmAT0BxxryX5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbQ51SeJW96f5zUk2Sj-1d7UwlXSvqRmcLCWxf3MdO7sJhHV2a9Idxe2K6ZSPCPBpcCtQnRO-DbFfyU7_26Eqf6PeDjOtgRMjlUQ3L4HOdMxsS9ieiYeSd8-_38eoVa6P0T2lGyjT4mgI4jQUmPC9tJr0rAs_BcylCqCaU7k-1b7IynMr_kRpWs9aqVuYgN5qr6tg6nM814hvJx1VakBcE6irZD6oFFewVtDl-7ujOTrgc1IXjjwwFZWRGHiBLturjfQqkVJu6bA4Y2kBYi6_uIl2yjN2iaCA4nHvlfySO0fSBKoe-N_zhPo8sDzIjoGDGIRnn0bftP8QgpYBwqM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIIwJ5cS2OduEFJLGVikEUX_Jjdc13Xo2zKIKCTd-J7Onz9sUQrjmpGYIPq7QG5GD-Rdr8VsOy1kZU7epzcq3t0BQrnyGnaDQIMWStPAiun9oyAvrBOr7a8ac4211-UK1NfTeGEc4630QdPjQrtGtc9Hzv65woPVZ6EeFxMDl6imovzMJrGkPlr5LUgabhlzQXKyCwsUmGDQ1hkE2RMpnTl2fNvvatQiA_ydhpwauXNGA73LqB_BzT6U2E5QNFoFbuvFoIJdpotposCZ3PgM-X66Bq94Ahb1X2RZ3u2kQgDQgvUo4sxiUCWpZEIKWaqiNSCghvLwFU4zy4ANPcjSmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=AgNp8xyd5IQKYqzffLnjkqcUPQImn-WxixqABDxY3_5ZezNWufvqOV8_R9ygroC9B2T91BaqTRL5dguzZocT1B6Iq0IHjjjfLL9t3KbLWIh_ggHvS4_NOa1gp_UeZPAutqlN4rve1HOWTUw-Ajt_P-sAdOKYBHYEjSLDCaF0C8W0QWw8MspUJemfeqmVUAIWhzZzSQCqcBngHPJVvQoEV-KQ-kJlZHcNK1vfJObIBp2nv1Wd2washcRNlteOk1yb1knJRpbqgN4UnabVAVVPmKXglRtAmXL3qPc2_S7QqfmrBMt3JBiynaAZZvlTwEFr547d1y0z2HPNt3bdT-YnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=AgNp8xyd5IQKYqzffLnjkqcUPQImn-WxixqABDxY3_5ZezNWufvqOV8_R9ygroC9B2T91BaqTRL5dguzZocT1B6Iq0IHjjjfLL9t3KbLWIh_ggHvS4_NOa1gp_UeZPAutqlN4rve1HOWTUw-Ajt_P-sAdOKYBHYEjSLDCaF0C8W0QWw8MspUJemfeqmVUAIWhzZzSQCqcBngHPJVvQoEV-KQ-kJlZHcNK1vfJObIBp2nv1Wd2washcRNlteOk1yb1knJRpbqgN4UnabVAVVPmKXglRtAmXL3qPc2_S7QqfmrBMt3JBiynaAZZvlTwEFr547d1y0z2HPNt3bdT-YnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt-ekX9tFTt7-5KPxvN-dO5ai2uG3Nn6IZJMrtnfUU__atG3qdL2hYAVdGN7J7391an8qo5dq9F1rSyGBIkBqgraSW016c0CplNIkpXskg-4MHHToff1uzAJwKc3xMdsdWXKmM7F4ot0njNIM-93PUxm57V5y-8cPlgqZUMZPn0Ogo0y4Pcci1mSq1GcJuXgp6QAmjsTHIu-m89HWJI6TGy4zAdlET3Mgpvtqh1yYu6YgeApaPP0u7f6hGwkAUadaOVBIDH15ksWpz4kTGqKzSkLKCt_UTXBLBfaYUVYRstoEjU9MJaduyL-4hnPwuBaaBK-x947b-I_yOsUMRZ85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd9Ya7ev0zG3sA7L6T6C6D6LFBMjayDVIYGAwdUpWoB6f28nAJ856YVegKv5yVNQ3QKCy6ktOZa-aS7HUqrsrSZ_lb3nKo3AFoMtTz1ffSznIAdkBs-Guac7qns1jL9dhWv_9HsJ5hDpPEeKbMZ03ohO5CigIBo4QJ_U7LbVidbblFoeKZ5pJpUtHNNslKyI9wTmrdKYh_HUYoJJN41c5jaLyqg1We6CgB1XjToXq0e-SRo-UHpy34gnb1az_5mcaixhKAox7bOOllthaDGM68bbLIxK-TnCtWxmQEz8se5XPZqfi7kyl76V2hCrYl2Haa15BkSLs2CgSfeJBY7DOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_aMVhCD83VeUIKaGsJjwqeluWkUeGQJETP-jJQrcr6QrPyuSIIUWMHn6aJX9rZH2ks1jfOOFMPfmJgEDhKJUEWlZsYl1qBea-s7D4RZgjrS-tDRpuhloXPVwrz5gQ2gKWr9QyKLJX8OqgbS9fhTtUk8Ou0bNUSqC6wtZ4G-t8Xa4-JzIae9WqbpU6zZ1conwXNd34N7Ac0-OvfRuSVz_x7W2vyeMFvRXmsg3zF3GxtEsTDl2Isu1HBqoUXLoV_UrF96hyeAqzPuv0kw1MT0VUTcPifBCbn8ZSzdEzjIgeDTaHnnNKH4o-1hESi4WgDGPI_bOczIxnnPkPB-4X6WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaHiDvbLtpeRDDrDFao4XluezfM_MdNg5Y7Zs9Bvw_ocPoN_GMOIjsuTvZhnwEa2BkPALvZgiYIs47bkJkDe8UswKutrhMkdjykWuXIxD8IdkAq3qbtCvNHFhyF1sR5ZN1VZ3FUPJ53sx51SHn6ZPwljPkBuEXFIJJ2VbbVo1srKowS3A1kKRgmvYN7HItS7Lwp6RrzuwoSjJC-3_XO21jTiVzaO9kRlRGNOPo8HtAhKqfyOCi_YsSNkg5n0cZIQUnw8yrmmOmca9ntlN5dAQe46LvLYBrOZDvAAy7XMG3NO7dLZLHQqcLyHaY9si-Jgf5K2s9Ld3sH3p4yRX8pD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi3ndrIatNvVWZuLb4A_4gygORrvl3fwCnHsdLK_KhkVOHdnFswIWbAQZUjblZb6KDUt3WKbhpCN7UsQgbwTy5MMFJtW8dKXyzPQiqXWs5vIZFYYeUMm7OIzk39zFBJsIy-SpISdiYtnk5qf4CXrhveOMYUx2hY5KRWHCZUAOn8V89RnWBmnqUMAlXGLtgTC_13i1lpiUQe5FGlJzmrsO4HApZt2TdCDE0k9D0TCNfHHLarMWqER2Y3oe4jcI4V9ZmMaYjWmbAllABCSkTX_uNbinm0sP_s09NTQ9e-87G1RVtUcMnh1ircahmc13rt-8JOXqDtQJDyF0iXRYR4TCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppveFKvgW1aTmvSq3WzF7lOnO899VI1mfHss-t3xXevkoyVvBnR1eoJZ4DkvAYfgNCxutRdpuuNVZlFb4J2v8A3Us_jSnFcL7E7k_ud2n5Og4xFIpg4ht5H4bu2DNGaowcEAAaSBs4s3wDNuuwniAd1S-5cp27W_NcEzTZRms5nXJePxdx0FdvTonr5d1IP3xHkDopekKuQlxDuwfbCOn_Ws8IvlbNe-rp8sYsoE_242x9vdc_l8R2cgH_dbmY7_FYOjL5S3nHbxTRMdIWVs62D2EeIQnkoJwkZF4U4Bx8fn_DZQhwXECFmTfGsyZkpDG7iuq_imtbj08gJUa_tczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jext5pCWMGa-rl49IaXvhXREd88KGOM_euq6w9EG9fU5FplCP-AkG4ghoJxL7c6Y-DHMEp8tVi6qyeLlsK6fkliQzSBXyLrMpUenNx5JTr2lHGenVuLvnjYutrZXiIzj3KunbEwp5ktYSt461TZ8kd2HZ1e08-IxnyHFLM2Z3UnP-DwNz3mM9f7f4pcMKy-kMr1C5ybN9L7jBS6HR6P8Y6QXe1PpPMQOBjZzwLsUaXkXiRa61c1v1OncK87oxylGQtGLtcci82hIQUQUw6stB-vSixOKx5WSVU6j4PkAhmcpo7hTlj9F3CTCWaZ8Mu-BiVTlmiXb6fLYPqYfqDiFKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYNK_LbmxzlasoIWNnlqGeurfXKVQauWc1UI8h_UDMA7-PyXKJ9MvXVTM_nrZJA6R178onqRca1z4XoEXH-XXjKyu8a1LhuJDt8Ui8GKFHf858M4gW-6uKSc3Yj2KrN4j_UWbdYMF-ysBNhL0a0g3YTvrKW_S3R5k8iug9FNa7oXLdpDqKQKK9rTKr1zzTzKRhUX63qBF0mopyPbC60PSTHwbjom7igidOWpL1yyqvVqsBXNxbCGx00aYCEDAvEg696QeRFROE7zk6Sb9cg-9sc2cvTtbRO34psn-y0xQO7ZwrIp9xFfXNJ3BB4jwX15kSrOOae_F2JKRqE-rn-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=WwFg1Jxw9iQs4Wen3-cwhz-Dt0ir_lYEdQqCXjl7_lnUuZsSOoG09rXk2FDsvmrBLCM9HdeW0WZ9Gx1ThSvFP3muY2AVmIrX18_0esjT9WNvtQvrQXFq3-X58yjO3Adh1jrTlNbANXz7oAsNwf9NZsSQ2rr6O_NCK44FxgfJX4UQrbDkCdfs21UXXznj5FexPeDcHTu7T4a20XFvMzT2KQZqVoH7zNGNB3gvPU1c_W7ki38z05Kdm64ZDhl1yi5tkUCQ7h6JPGAJhHeBsxLlgK7L-reuXIcYd0eef6K98MGe95r8HM4U0NMoZ6gIH1mZgdnLm3a_7hQGWcLpZ2iF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=WwFg1Jxw9iQs4Wen3-cwhz-Dt0ir_lYEdQqCXjl7_lnUuZsSOoG09rXk2FDsvmrBLCM9HdeW0WZ9Gx1ThSvFP3muY2AVmIrX18_0esjT9WNvtQvrQXFq3-X58yjO3Adh1jrTlNbANXz7oAsNwf9NZsSQ2rr6O_NCK44FxgfJX4UQrbDkCdfs21UXXznj5FexPeDcHTu7T4a20XFvMzT2KQZqVoH7zNGNB3gvPU1c_W7ki38z05Kdm64ZDhl1yi5tkUCQ7h6JPGAJhHeBsxLlgK7L-reuXIcYd0eef6K98MGe95r8HM4U0NMoZ6gIH1mZgdnLm3a_7hQGWcLpZ2iF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYr4QPV7PCjOV8XxDa0nOjW93L8X2KuZei7qBtVFVfRoD2wyvr0FICJcOhcw6y0y2XGgyXtRSsPg72qVbjWd4E5S4sD0k0m01_oofyaGziKNgoHlIFp7BP6rRxMyirwmjaXuLJr5zlcn7tnfKAIouQKRmfKr1VjKNT5K338tcRxV45F4cQAXJXSbAczmcy_L8KOXqcHy8RCOQNGFGtgt_gmGoLJtPmf2YYjCrlEaIzHLXd0e4qJuRbf62KF1TN82JAVrH4DPaR-fgz3FaIQ_zlnKlq5NsSIa1PdGAtoopp2VSIE1sAg9FJOoEt4RAVM56nzjsULwPR2Pp0tosJKN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt5aiVODcXqYFaCuKs43rTi1FOJ4EZ_tcpwJwS26PTSpgRnu-y7mNRI_c_xbvVozJLWRe8Ot5d4Fz94fIizLYbZ6id4C8S5Z3vru9Reh7ORxx1FmNvHHCSmI90eW5LecaBbTvvvxGumA3woNacQaYhuEs1SpPdrS-3GlTzEFnUTtRGEqoyhtzsQ-3tfAIE9jx6z-tzrwJeKm40tKia3whVJxYgFfKSturI5qF7zf_OgcwKZHEkcUPFGhlSP91U7S1ZS7bdj4W-tOgNSSFBXWLdqzVokoyIRdB_O_gdxCN4m1dSuFiCicHJo1GI3Cz9wVQppTMCdiJJVeNh0oGCsEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLdUkJibb4ZnoFb3lbjO50QdkOTdXdGTD5YAydpY2inaeV5Ba_sl19Pep6EjUerrdK9EVRpOsyabW1sgjtS01GWRNDBSbRf_yx8ZQH_G6fNRN-xHwb1CxAFK3PjuTPoSoRlFGX9n_89uWYlwWUwj8prwW-t-fOO9-cOzjL22F4K8MEHvGebE3GMBXrJEBpAkmPUXulTRct6-BcjIVGauKOFNXJLxJGJQR-OLz7dKKwbhQZWtgiM88SzrdfUDUyO4FUT6iOZrB_CyjWdA2jtGzxcM_Kwib7QEZNVJ26J8y8_1qQTjJloam9o0TkCyfCiLLBMY_gLaE54hrojWUk3f3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskh9dx9LKZLYeMdoAUYPbehGpLeHHOMVYIgrhb_yPwF5kNae7AryKojexK8tibeDA5jjBd15v7PafRvyZX8aAmS1KTPJRimfgLRL-nJ3_jjjq3fkm09bhC-aN76JN_Gj9VQYNuV0Mwq4PGDUh3fEW6bBJKTGKLawqk1WgrcnzC8MTi_kn54szjsCL-dDU8HYTfKJ4Db6uQNHz4f2MRrmEv7oVA_oy3mxt5juLSv7vzC5dHdStwCdcINL8iBgQyS1ws9wClkwtaolHPn8ChmAHWmeiobxK6T_Q_TmXaPWDGygcvPPqaJcQkAGV9QEnyuKyXTi9ptmd59VYTrlfGgE1iCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskh9dx9LKZLYeMdoAUYPbehGpLeHHOMVYIgrhb_yPwF5kNae7AryKojexK8tibeDA5jjBd15v7PafRvyZX8aAmS1KTPJRimfgLRL-nJ3_jjjq3fkm09bhC-aN76JN_Gj9VQYNuV0Mwq4PGDUh3fEW6bBJKTGKLawqk1WgrcnzC8MTi_kn54szjsCL-dDU8HYTfKJ4Db6uQNHz4f2MRrmEv7oVA_oy3mxt5juLSv7vzC5dHdStwCdcINL8iBgQyS1ws9wClkwtaolHPn8ChmAHWmeiobxK6T_Q_TmXaPWDGygcvPPqaJcQkAGV9QEnyuKyXTi9ptmd59VYTrlfGgE1iCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=v02hbvtKcPV-hSRFd8YD7vzyfVXzYGpjJfxFJygJLw57EwCgH_NBdZ6qRtli7nEJHTZTC1a821FSNRrN4__fFniF-kdsar2iOPl1Z7sgyuUz3JH-7bEAppi0gV-_deMLKBUovSDI7t4-bcjMtFiLipCrwblA28YOH5teSuAFyZlhZFglvX4wz2ZCLhIyf5ogENljPA8OBklOWnowVoN0p2i4QuC2QFvdSnpvee1rjqZxUOMwf9Nk0Fh9wO7tY5DyJvgUTFl9EurmBDhZ5-Az55oqz2KqQ6CmDVHm5u-fS88jhKO7F6JFkXXbb6cQ1Qx16dNfOR-2eU7T1BZIbpDiOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=v02hbvtKcPV-hSRFd8YD7vzyfVXzYGpjJfxFJygJLw57EwCgH_NBdZ6qRtli7nEJHTZTC1a821FSNRrN4__fFniF-kdsar2iOPl1Z7sgyuUz3JH-7bEAppi0gV-_deMLKBUovSDI7t4-bcjMtFiLipCrwblA28YOH5teSuAFyZlhZFglvX4wz2ZCLhIyf5ogENljPA8OBklOWnowVoN0p2i4QuC2QFvdSnpvee1rjqZxUOMwf9Nk0Fh9wO7tY5DyJvgUTFl9EurmBDhZ5-Az55oqz2KqQ6CmDVHm5u-fS88jhKO7F6JFkXXbb6cQ1Qx16dNfOR-2eU7T1BZIbpDiOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=HvVLGPSEsSf71xH0264KHbURCCIdZ3jASpNYteuevjELAXKeEGmpKHeRmDn907dLxyiMP8KAj7Lai7rl5OZIWAMgdlFoVxz11oTCYREwtMKxr5X4nMAi4zlRWZ_iQztWSp83WEXmnWHO_xujI8_oK7gQL0sGfwFfiWjO3CRutc-xx2HIPN0mxy3ROwqqK6XGKB8OrgTgcjBm2vsL2S8O98Vy0NI3OZ6HwQSN_qX0a8dwpz5g_NV_DhRCqo7TDIJ3eylrVTDbnwbZvlZu2ihbNIOL6R-CkiI2tuYqMDE9v05-VBLnG57M8_pOITcRsTF-1FNALtwTeWT6ls2Q5v4JfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=HvVLGPSEsSf71xH0264KHbURCCIdZ3jASpNYteuevjELAXKeEGmpKHeRmDn907dLxyiMP8KAj7Lai7rl5OZIWAMgdlFoVxz11oTCYREwtMKxr5X4nMAi4zlRWZ_iQztWSp83WEXmnWHO_xujI8_oK7gQL0sGfwFfiWjO3CRutc-xx2HIPN0mxy3ROwqqK6XGKB8OrgTgcjBm2vsL2S8O98Vy0NI3OZ6HwQSN_qX0a8dwpz5g_NV_DhRCqo7TDIJ3eylrVTDbnwbZvlZu2ihbNIOL6R-CkiI2tuYqMDE9v05-VBLnG57M8_pOITcRsTF-1FNALtwTeWT6ls2Q5v4JfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLPfQSINhny6gOG22722hbhcYK0EGYaPlnT-SsPRBp5uErhhUw6gYQPXHYyz3maV5nbt7utvGOJV_ddi3lA4V0743JIY9jkCcq-fcmAOnJ3yoHqUXYsc_V2Qu31avll4Sx02e1jYKoMC4zycKlZHzEhuEEMqBmpPGTxaUSPZe0_1SFg9GEOEGLePn9VdY7x0M8LuVI5xSSJ3Uk4QFD2eZHYVMO6AWf2oDvhcuwiVK-ELaZuloYvAaSRQC3Ulz9TO0gnsBj9I5QepKHb5XxQtDHiNDsJE6qDy-XdPZ0of0BBlI4X1oMQl9sRnGe1FDGgGnFJjAzzqgAAlXt0aaY2gZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuZNL6dbGqYkmrbyh_biivZLhdgflgRWgZQiShO3SFH2DyZ3bbfiyPytRvdPkWn9YBKyJcbkHDkR_qMzfiVZFcsrRIAKeZN8abGRSvY98VFwbPOiQiD9O_thZn3OMQwinMHiA5Vww91dcE2ElRO-a8A4EEZrO_1zDuS8ee5KCbJ-43QJdb7Kxk1bt59qohmemk1lcZecTREFbvJJ-qOJLQWCxSAhScXIsDNWw3Sy6z7tNjvi1NxC8DkgX6Ayd4fYfO15krKrMULivGvY2AQo-dRGeRfiniM_i95Snum7ezyycNheVpruzAPJrtXvuPwJ5U-WGsEonxct-iFxmmFmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAuFXo0k2XgVQcRLGpLxDkXqZddO2KplfDpkmBFDCEVr7AWBnQYAnGBgLdL9CyGuzvJfvSwsFFgtTLe95H_1E57xfQabLsW6M_6p2SdV4sDLXiik3b81Yfa6MkfmH1TutQ9__jAE3eXErkewoefmCTArkMNr21-3a3zcHOmUl5EgAFF-iaAShcntHVRTLfraoAcWYuMHKCpXHB8Wcv1NRrQ1g4cc4Zk7D2ovAGRvra7EmQ6Z5oI4AvCW-N0BLDXGQtTk5NvdLpdWVKnLfXXnR5MU_5l5jf5fwAhbidQ7q9wiOl46_LJWYFNULHVd-DPZXvN0bqialTlgLG5LJvM86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9hCnteO58RsZcA-NdFHjYv8UKFS15LNFf_ZXB9WG8yqF77QmMQXIqGx1_NcSeB0UaFCb0bFQ-mostzcYsDew4YEPQPnM8K0bvP43-_Repq9OPcUG8sJ04wD3eEifevwBMvyVp4lzYuh50u9LdsnvJ4PWhH5nCKljS8JJAV2B3vRG-dK4PkYnAk7DfEQQmMgmEckiSneoL4VUisFhtpVV1pPeXAD5ubL_KANU5jSvIE7fn6-bgo0svqY7_ByeLjl3LmVslT4IHweh-Y_wi2c3MLqOg8-1Ex0TiUPjAzLxO-hrRRR9vor87A9PI_XyTj8N9Ijn6vWp2Mgxsb1VwB1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtbjynH68hd7UHO6-rGdc7ovr_RbtDthHJGkrl4c4QUTSC1u-Ek9TipHEO-eZR8TqMBEZ4tToiNJxRTBne_1cR5OyutUhT7ElQofTAUhYjpX-VoXCP0Ry_YTbXBLpZOoltlcItW-lzagSJNWoIljTVbJTpJzS3FR0EsKZow5eRGJAit6SRBZvER-tFnjCvMKqLONNBHoOmPv5dxaJoE1neCGonnyZo0wpN5YHbXcXL1GFhHLLyp0LepOrfh8i3ghaoIwdZOocmNxLy6xzdhQzeFxZiduu3-XJiCsUTgRJQckGeapjXio9BZunWRr6aRhS2JMQJOmuiEZWQkYGIBuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVX3AlK5UXYAAaFx9PC4TSPgside21s_kI-RHogrgpg0ZeIEPl6_AbFYgtQYauuxL9imdwNG7NGS4TiLCn3FkfqIwtjLAd3l2wBNQBvaH_eYnNpPFE_MUDaySU-q0B0XmhSuStudBjLWHvlWMN2gEzCBUnS139B0I8WutUoYAoi83mIfPBBke3to9j15YosMgVKoH1q_E92sjV-w4HjRF2jbWM8YOP7g8kegsMU1uLYV2PHU8-RebD3nd_oKZo3Y3fYxF-414dIS3RViaYXX1DLuEHJhriS3PVgGkaN2yDiOic1ijucN3J7sMaa8lOFIZg4g-09tOl23W-ZtZhVPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9hmJTwznNouYQbo5DPeWj6o09XUyXZZ08_pfsGe9K9NNLJTcz0lQozUoHx-tHl4j-0XCR5RA_sM_aqNstwsqSPa3uza-QUsqg5ckhFqaGk0h6xVibB7f1ddWwsfOJPG0jOcTzPaVxUrMnREd4pPOESQ7CgMR2BNh9JaVp1ljhjID2s9c_BZHf2Y32r0DLWNzQ86jIj_d6BM57c7Zj1bOho-Ej8YCoyPxOZqnfA2-PoClVDrJuaPewTkjta8HOQui1qMzO5QpFIkCet7ucFrUFZ4WruCSEKYndyTtpSAo6aNHassrz9CSSzdcKbfpUQcAat-BniEgLEWlsJz9_Mc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVm0SOUiKFVzBoM62QbhgKc56cSvmixbovCAFkGv-f0xcaKF_yTQAiXHRA6LE1ZlUbLmA_M0iIM7KyHjfaNnhRz1ENe5KNy5yl0ALHZCMc-0FLzb2k8JBYD-ethEXp3YsEFKw1V1Knl_Xm557Lo5xmqRQkipS_qpdLjnLOQPqEszQ8Z7FEwWcadviSqtmSNFKV8CuOBbiUJ5p0ORxt9ARR4BIMvIX-PbzK2IY4MgPDIbmeMgGolfdoOFMzN2HTEz4yoWRphk7RjF_KlYaWwWDzdZZ2rHWUCe1ZJTMdrOrV5MpQUb1mLRq8Fz3fmmM0gDPOdaD90_5pTW8b8q2ICwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=ai1gAbd5sjIfLE2v1u3tMspVKSo1YNN_nnYFAldo-uoUSGpkfJ6M3nWklJZx-VyDQXti8KwnUZyk-o8LxmWyllumHz_MxoXHXL96uSGGbxbz9V2o4UJc9x46GdGBrksxfmOYCTlx0Ftumd1-Qq7mpkwh6xhf0zymNu9O1EW7KG6a65sFpaeYSfl0cqCc6k0d8jp6qxeLgmvfXPsuVn_Dl5WHbMu9Kvw7USiIXR3oG-O0L0tFocvGAyc6FCv067A8CU-7Rv7Eabl-TLwsAHHZekQA5kUiSuvP7VGmiyfTUoz2BZYUbftcysNCLADVhE_mNiWFXJi-Mc1BU-AfB4smGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=ai1gAbd5sjIfLE2v1u3tMspVKSo1YNN_nnYFAldo-uoUSGpkfJ6M3nWklJZx-VyDQXti8KwnUZyk-o8LxmWyllumHz_MxoXHXL96uSGGbxbz9V2o4UJc9x46GdGBrksxfmOYCTlx0Ftumd1-Qq7mpkwh6xhf0zymNu9O1EW7KG6a65sFpaeYSfl0cqCc6k0d8jp6qxeLgmvfXPsuVn_Dl5WHbMu9Kvw7USiIXR3oG-O0L0tFocvGAyc6FCv067A8CU-7Rv7Eabl-TLwsAHHZekQA5kUiSuvP7VGmiyfTUoz2BZYUbftcysNCLADVhE_mNiWFXJi-Mc1BU-AfB4smGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d60uVjAZdwLOEYRAhJ_NKTd1kMV0OIn7e0k0Wy-33p7oeHcu1oOJf_qEJlZMljc1LabZ8EZuMUsOL55Hz4C0AW7MtRVWm-z_iGucWYZ1YskdthSJPvA6Gd5TKcgGdIEmhCHf8S_gkmk_VWvyJ3aJx-9n7T6UPm8I0R4ymcCnFT2ZiNRQl10ucr9ckCOacqRDbUiMszccvH6G-sJuHjFGxGSOxhjizFi4ZpZXNk_NthY1yqUk8vQkMEGz2G4lVQcPe_xaZe04s6d-UZQlTxy6Y7B9Q3BkR0Iy6Ds50-ElixR20BT_RAGcuofjy4wxoayAb_0ASu6TOMzz-MaSMBAPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=a5JpU7Agg-bA5uTnn5ICH9c2ORMEtwL3cXCI_mCswWWQMpORN4Tn9HzN-WHMa9VGcCcveBIUrpoB7hGWcyU561rDI23GI9VviWTb-ZuYd4tVelzKviWPP2wyh6hQwCg_Rustm-05bc9CLODjjYv5WgJlFc33MJ1eoBAi0ji7wj0oLYPSWNB6xun64NAFRWfUvy08EOdKgv2uDEB3d0mPS5zjMVh8CBBrS2MgEU28-M1ZPN9n3zLSvKgzHlgRKWQV1pJrlzGTR34rzXHZxZjVSQgzoQbqTy58WYVMoYMgcdDSECC6_F5e4FrT_B_B6PaOh3DK6nsv--iDzXsb5XkCLiFPwc6UyOWVzZIgyMSaveW3o96TO-RKv-TbbMF9Khrrn6p694VMZmZywQav15upThtzRxxgNsax4SWg_260_daMOR-bVX8ELF1y2nFr8cjIbRJR2oX2lUCqgUsviiGAh2aDt7vkpd_CWi3yNmrsKCpA9X0Hzf-2vN_Rhe_6QYbaB8OlXNohTFO_9SLv4ab821tJQcmjsu5A2VjZ4yMvScwAhfXTZDUuaOSmbm97WxFkV6TJmjkUlxONcj43ne-lzNl1kZYoQpYgdoy0hzxZc_eK-X6FbwyJ1gEsL4-uNZLqdqFIch6uFkNUPiY0DJZhVYB73x7J19KWXIwDy5e_iLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=a5JpU7Agg-bA5uTnn5ICH9c2ORMEtwL3cXCI_mCswWWQMpORN4Tn9HzN-WHMa9VGcCcveBIUrpoB7hGWcyU561rDI23GI9VviWTb-ZuYd4tVelzKviWPP2wyh6hQwCg_Rustm-05bc9CLODjjYv5WgJlFc33MJ1eoBAi0ji7wj0oLYPSWNB6xun64NAFRWfUvy08EOdKgv2uDEB3d0mPS5zjMVh8CBBrS2MgEU28-M1ZPN9n3zLSvKgzHlgRKWQV1pJrlzGTR34rzXHZxZjVSQgzoQbqTy58WYVMoYMgcdDSECC6_F5e4FrT_B_B6PaOh3DK6nsv--iDzXsb5XkCLiFPwc6UyOWVzZIgyMSaveW3o96TO-RKv-TbbMF9Khrrn6p694VMZmZywQav15upThtzRxxgNsax4SWg_260_daMOR-bVX8ELF1y2nFr8cjIbRJR2oX2lUCqgUsviiGAh2aDt7vkpd_CWi3yNmrsKCpA9X0Hzf-2vN_Rhe_6QYbaB8OlXNohTFO_9SLv4ab821tJQcmjsu5A2VjZ4yMvScwAhfXTZDUuaOSmbm97WxFkV6TJmjkUlxONcj43ne-lzNl1kZYoQpYgdoy0hzxZc_eK-X6FbwyJ1gEsL4-uNZLqdqFIch6uFkNUPiY0DJZhVYB73x7J19KWXIwDy5e_iLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=mYHqhkYG-0U-POJxpKlf-D3Th6ei6ywr_xueRSTFS1aEA8FrAG2x8P06bTwNadaEihaMtYiY_D1USkrRc3fAI7F8JhvIwMdo54PJxUWEUe1Fb_tU43kHcCZ3zt8d5LoTT2315_lawDDH8CR2mTY8JxFok_BEZFlH7PO4TBxWZUjmzq2cHapPdyZnRfSJKgHQMXOA5ng1SAvQh-n_P-9XXKHt65n52oAepMnzDrrL3-0wK1B3b3w0LnE0Zqu7r4yRK28ybkMX71J9W0LhjTw6Lj5VPVXEPy_u1Uc-e1Z11_Ml_67VLP-Cncz9NGWxW7SuLg3Sn3FcajsYKLYGaFlvIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=mYHqhkYG-0U-POJxpKlf-D3Th6ei6ywr_xueRSTFS1aEA8FrAG2x8P06bTwNadaEihaMtYiY_D1USkrRc3fAI7F8JhvIwMdo54PJxUWEUe1Fb_tU43kHcCZ3zt8d5LoTT2315_lawDDH8CR2mTY8JxFok_BEZFlH7PO4TBxWZUjmzq2cHapPdyZnRfSJKgHQMXOA5ng1SAvQh-n_P-9XXKHt65n52oAepMnzDrrL3-0wK1B3b3w0LnE0Zqu7r4yRK28ybkMX71J9W0LhjTw6Lj5VPVXEPy_u1Uc-e1Z11_Ml_67VLP-Cncz9NGWxW7SuLg3Sn3FcajsYKLYGaFlvIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGHtpp4g2R-WQYfmsXEeOT4ttm6uoq16bxqa6VYihb2J7v0jzzmS5qsffb6tkebnpzNs-a7vEHJoAQl_bspHeOW5XZDFIOdbhp3ah4rUiVjyi4eQk2VHAIRga36nVfWg3gbyng2Q54OeTOelO8ZGGMnzaKx-of0HMuPH1JxTYsnKXK4j8lFRs2ZK6_c-V1ses9UWESGjW_WayUt87TJR6iJPJe9Kz3GNMAt606cR88F_pBk9Ra8DC9_IolQwy63-F51JfJ69JHtbRIx1turtCD4o84iNOnNK0q_y-0xNWrJgrLjUsuAozJek4rTX-TdA8BlB_rmWUqteIV3foO9fEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=vYBTzXcfWs-462Rpse4thJEFD5vI4QWDcCbWKDHNzq5z43F6hs5DAXE7UjoIA6uqOnQUJ8uYEHNoJBJbC8YwyVlQrvqpESeKM8ZT4EbIcdmSwOrYmMagHHls_I0Su0MHSKf1g0OlN2VVZYzfLZy6RP43nhfXwABoWpJsruM3bABz7lMiIjrvnADYIB9LNbdntPiiwU2gXQAXBnMdbWOTDWVCp3Lnp15qi8CwjTS4wW0CI9zWZO504RsVezvfI3LQtS3HLAW5O2ifcAGSg4YalaeL2bLYnDWg-n48cbptoAEtl2JUDngTfAPfVsKcmPRmG44Ty3Il8HAOa0AoXiE4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=vYBTzXcfWs-462Rpse4thJEFD5vI4QWDcCbWKDHNzq5z43F6hs5DAXE7UjoIA6uqOnQUJ8uYEHNoJBJbC8YwyVlQrvqpESeKM8ZT4EbIcdmSwOrYmMagHHls_I0Su0MHSKf1g0OlN2VVZYzfLZy6RP43nhfXwABoWpJsruM3bABz7lMiIjrvnADYIB9LNbdntPiiwU2gXQAXBnMdbWOTDWVCp3Lnp15qi8CwjTS4wW0CI9zWZO504RsVezvfI3LQtS3HLAW5O2ifcAGSg4YalaeL2bLYnDWg-n48cbptoAEtl2JUDngTfAPfVsKcmPRmG44Ty3Il8HAOa0AoXiE4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=LDzVTGOEoN1RKnRr21XGs5keGqEAjf1rK4MDrRpmmwViC9KK291IPWRRZWMUbGPK5GO0o-7XYgG2zGjLJl4RmmofZytJR3xtASk38cAq3n5NvJT2_6oXZwhuo2TKshB1zZPc_qV3vkEI4GYiCPohdX-WsoBnByRwpZMVXlMM8OC92h7SPpFTX6Lmz8yYcsiz-6Cj8FSw8iLji65EHPjrLjhOWkGOH7aCidPIZupUlDC70is8FALgfBlZXq-Bv3UDwjUTj1CJs5_si2jUM_Vceq5TXiQ_pEQ1HQT4eOyM0spJVo1z9eEzFdbw1on61lNmx3dZ82w_ub24SLOKX6MlHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=LDzVTGOEoN1RKnRr21XGs5keGqEAjf1rK4MDrRpmmwViC9KK291IPWRRZWMUbGPK5GO0o-7XYgG2zGjLJl4RmmofZytJR3xtASk38cAq3n5NvJT2_6oXZwhuo2TKshB1zZPc_qV3vkEI4GYiCPohdX-WsoBnByRwpZMVXlMM8OC92h7SPpFTX6Lmz8yYcsiz-6Cj8FSw8iLji65EHPjrLjhOWkGOH7aCidPIZupUlDC70is8FALgfBlZXq-Bv3UDwjUTj1CJs5_si2jUM_Vceq5TXiQ_pEQ1HQT4eOyM0spJVo1z9eEzFdbw1on61lNmx3dZ82w_ub24SLOKX6MlHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=Ym1WAo4vx1jw9hm1qDPowBUIAeqz9QurWgwu9LrfQXZ-4T0A8HF-9CbJrJhLD-Wxj1a-8w716JReGNIbUtRtFYScrMAT2FKOlB1Ot7sLttI2ZSQ-jNo-DJR9T8L2opwBTKTyDPkFtPQg2khi2IwZpOerkex1wMK7UbhPrh3B9ccY4_zI-MuDE8sfP_4wRWHJLiXd0YRnL_kBsHFA4Luh5hEaw9vX_iLQHhEcMLI6toezXupuI9uK5zRdzEKSlYWYVsS8TxG9jimSXWwEqtyfNJ6UhhQrGX5d_OQ3hVfA_h908qMHpVG0dUZr1KSHjE3dodBdWn9vyHbLg6pq5UO1d4pY6oKxExwKH2XGY01XQdS0NDxP10MNNgyx_Gtl_Lmou0kQd5EZi_RO5DwIKaZ4tnyzDeIDL-xNvdMOCsG72ZQk_XsMSuEEn76Ea2s9njEyaDCLrurXOjnb2bSgp-u-G073gDO1_0HaaxCnckCI5VJdSisSaJo8acQLVHqr84_eKzqFP9Zgy78StzT1ELIcq1bpsWX3U_f5BCHI4NMSNFoEt-VG-O4EMIL4UNn1Am4cxgVqGCREZrmgOxw9pxZYE6PhEa0JURpl3kz29P0TlClbaRgx414HCyH0GgjwyVb5udLW04fLsyWXu6QAzcHtA5AqwEU8oCTWVvGU4Z2fkp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=Ym1WAo4vx1jw9hm1qDPowBUIAeqz9QurWgwu9LrfQXZ-4T0A8HF-9CbJrJhLD-Wxj1a-8w716JReGNIbUtRtFYScrMAT2FKOlB1Ot7sLttI2ZSQ-jNo-DJR9T8L2opwBTKTyDPkFtPQg2khi2IwZpOerkex1wMK7UbhPrh3B9ccY4_zI-MuDE8sfP_4wRWHJLiXd0YRnL_kBsHFA4Luh5hEaw9vX_iLQHhEcMLI6toezXupuI9uK5zRdzEKSlYWYVsS8TxG9jimSXWwEqtyfNJ6UhhQrGX5d_OQ3hVfA_h908qMHpVG0dUZr1KSHjE3dodBdWn9vyHbLg6pq5UO1d4pY6oKxExwKH2XGY01XQdS0NDxP10MNNgyx_Gtl_Lmou0kQd5EZi_RO5DwIKaZ4tnyzDeIDL-xNvdMOCsG72ZQk_XsMSuEEn76Ea2s9njEyaDCLrurXOjnb2bSgp-u-G073gDO1_0HaaxCnckCI5VJdSisSaJo8acQLVHqr84_eKzqFP9Zgy78StzT1ELIcq1bpsWX3U_f5BCHI4NMSNFoEt-VG-O4EMIL4UNn1Am4cxgVqGCREZrmgOxw9pxZYE6PhEa0JURpl3kz29P0TlClbaRgx414HCyH0GgjwyVb5udLW04fLsyWXu6QAzcHtA5AqwEU8oCTWVvGU4Z2fkp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=pxa4-Bdl-6Re0ljim1EaSFVsMlP0hw-5E3c2ANmU7vD7BZdUi6l3zC4708kfEBufQNZzsbR3rclw6qgB22j7av99t2yqjijkYynhjjQX9qMCguqVjL51p5GA9nOw0a5Zy1oOvJYHxe6IXmGTXYoOIk-MrTDTPv9DiotYq7qgT5uObTSTCmwasPP_PKdK90A_8roJmsTfLTHuswDGZhpKmCw7mNTe0v3G57R4vyAp8k1ZoXAfoO9AARXCdR9WST2cKdV-XXobpZlHE0wKZeUYAsJMBr8k0M2Ei-LsPOc40-9X3sRZTk2Z4HzmStbPSEKnq7H7iH0XhWEKQtpLF12zNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=pxa4-Bdl-6Re0ljim1EaSFVsMlP0hw-5E3c2ANmU7vD7BZdUi6l3zC4708kfEBufQNZzsbR3rclw6qgB22j7av99t2yqjijkYynhjjQX9qMCguqVjL51p5GA9nOw0a5Zy1oOvJYHxe6IXmGTXYoOIk-MrTDTPv9DiotYq7qgT5uObTSTCmwasPP_PKdK90A_8roJmsTfLTHuswDGZhpKmCw7mNTe0v3G57R4vyAp8k1ZoXAfoO9AARXCdR9WST2cKdV-XXobpZlHE0wKZeUYAsJMBr8k0M2Ei-LsPOc40-9X3sRZTk2Z4HzmStbPSEKnq7H7iH0XhWEKQtpLF12zNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
