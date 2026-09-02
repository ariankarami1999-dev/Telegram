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
<img src="https://cdn4.telesco.pe/file/ArCWpLc91Hl_Y6tNgFlCiQcSMDgcHcQ37ryjI9063OdtYjwY22pyGssT6Z16orP7taEkXclLUX78dPVWBwBpDHsKc7z7-OXYneyFNN85MbnG-IA4xK7aj7tQ5uIEgxXxm0EZ1C7OzXOH7rWbKchewtEsOK2UincHD4aXE7oz2jCVkpMnY5QIrR7m1oHcZyxktmctQxmZ-7ffPphNWTp0dfvyJhMIf4geAVUbCytsrlVlS8It11vAwLFyxdCH2Gzea7RteTj-nmU8kOLF-Gcaaihcji5NdI9TdJu0jhpNEXcC0EdhOkJssH48aHmrkz6F7awpRhJ-YIzn-Wd6cwBJFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 113K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EodhnD-DGysUWNu2JKgxJWhQxt7Sf62drKC01s0yYQa-enQexTcKwDWR6siEd7g7qVaoFnyHa6UrdpQaIWM2fFqb8aJG08Nz1V4FjMF9qS875vDPe3Y-woHiIphLzFaO3wkpyX0qQDoRTj5W7LpoflNdprl8zJIsmfzE0Jv6jpNhKEQU08DhFR-gBUN8MCwSC7X8LEON9Ejih8qCVPBcBk6lx25GJnE-AD-e3UTDkMICTN8IZ-R5NwCEmMmmjELtFdQmAXHHlJkmumYHGiMD8Goc0w4FxzEEFAMQkWOPXS6JsdoVBXXuQSJCjMfQN593YZEhdomy_LWwSzkCy98jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR-oWidxX8FJ5h-3VYMT_PKscKHmVK_iduQx_1Zr5IlnGTv-p_EDtA67E9lRRi13JXJOx12fUxiWSQYdrE0HJMJyu2Z2H6IhkqK_RH2ZR7MroCTssCSHIAN67C66Je_ImXzpP80k5UJgBC7fcNcNMcJcbPP6lxJbo6NgWmxNwTOIPNR_WZ8XwjCAMc5E91387nWx-6iS7RLHTtuVkrOqJ-yfwNqmpiYK6b3AgbenznyFy_U1x8Lifd_ctaGPR5ZFy30ZS9NZANB645B1vfohryNFadHwzjOCfO2s71OURp74wS0PDkhRQAJh-zw_XieijrxGDf5SBfS8mpUKNyMZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUVVpqrVrUV1Rv9Ys0ZsO-Y8MBxTveRdLIRkeyh9Gf9md0l1yv2K_JJ5fte4SGMrNP0yGyitG_SH56rZ5nSFWvZH_Biwdtc7XgxfjRJ2WzOeSfgxVzq8p74Vn_wtj0ZGYcZ80ixxPNwpvu0jAZvi7LJv_CsPzlYY8pVSjO_rBEdUJT8s9XL3e201L0MWkZQOCg6sMKCcgVFP87nXlFtE3eR7Dk9JurfGTqhgMkzqbMBi5NeGUTeVgJjTedCpLaZTuBbfYqWPq6FUR-x4p5YGwFIaRHdcmR_Ao78cAGTR_C1mq-iWbqtpWFfdXzAGfocFHmALVNSM58CO3geEm4vYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFkoqOvXLYEP8dqy9Fye9j866PrTZPwmI7sDPJA8dih0zesHLSa3wrWd9ON0VdzNnTIahltJLDv19u8f-LAOxA3ovooMxg1cXjWPI1YBKD7QuB3b1Honk1BROuIskc8uORBJKhh3eXgf6aAT8LPmbKrZ95x7tI0bj8YyoKRAxPCeN2MNys5SwOqLh9Mlb21NfE9Wy6CkNCiJXqGohZ8Bi7zYKCQJey4IjfggeolKJWwOn-OkhQ6YWYuMDFtC03U3eUfgnHuWjcJnF259lTsL-8rsCksYV7r3QHHTGGQC6IfWHAx4CkUGUfSB2CH4TxytHyKj8-9k-3NkfoMq6mKpvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=o6cJbPWqDKCfl-3DqaEvIvnpIUQ4WZMZ6N9CJrESOnhaLwEtZwjh5u30VxkP-ut22rPRWgc68x-RUbswFJVN0DCGqS3v70KlwUzG3pN-n939j4Y2SVzyZdoBgZ46CSkEkk0hwDlnk_5RWbHRwecX6LzWwmvSSlL1op9S2tkO8y188lrkY57qONX6DwNv9uicN7vkMGJWYdiXhHl0Vd78mlsB06lMD8HHsUPKUrHpmNktA7ABlqEy9Iit0Y7JjcCKHfGyREpzpUlW_EZr6YNc9k8qn-HUySmOIqn_26c8pjrpHW4CkJdrpHlP8C417KLeskrHHYOY5aVI_7A4pezZug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=o6cJbPWqDKCfl-3DqaEvIvnpIUQ4WZMZ6N9CJrESOnhaLwEtZwjh5u30VxkP-ut22rPRWgc68x-RUbswFJVN0DCGqS3v70KlwUzG3pN-n939j4Y2SVzyZdoBgZ46CSkEkk0hwDlnk_5RWbHRwecX6LzWwmvSSlL1op9S2tkO8y188lrkY57qONX6DwNv9uicN7vkMGJWYdiXhHl0Vd78mlsB06lMD8HHsUPKUrHpmNktA7ABlqEy9Iit0Y7JjcCKHfGyREpzpUlW_EZr6YNc9k8qn-HUySmOIqn_26c8pjrpHW4CkJdrpHlP8C417KLeskrHHYOY5aVI_7A4pezZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peKQo_eXlBD-0ZkN9CCpn1GvJvDttMhlqG72g3Bs6MftG1uWS7f07lucRw22548CAIWEnanGuhit4bQIO8EFA5yEa9mo0au9piVFWuaspCf33tJvjgmaW-uF2cyU76lR4Vmky72HFD14yhzKorpKNjpILdHK4ziNL9R5pq9Pdkh_ZxrUSwSBoK5ihHEKYuiDPYE4tA5snW7A2CgGv2iA-7ceqslVmuYQxB3pI2MLssOZ-9EbkIe-jkfzHeFi_znJQfAaWfRBfNX4KbIFqQs7G7s3D5g1IPwG3q_n7wKhKX_GjIT2xnVTd_Qy2PFtvl2GMd8NiyRtk8nUBdpor-eMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm58_K_sazFXZ69blCwSCHRwo46rW9ju8s4mQCRsmgta0mbsP8cbf73aBL8ueaKYUppjgjI9u7dtYV5beNZCa5AXLDaQslBsJv5sBw5RDbU-a22sHzz7rH7LY78kDQ9-DtlevLBTAJ0f06ZH5zhb50jZ9H6p9y3pGUwYs11RpCLxV1s3H-vijpbvw9hU5uoui9Huqn5uh-k0MqV6SC-p2rJCF9ulb1VPkjpz-tqpabACDW-sjo66dvqoWITdKUOeAd6fddFbAX-2c3zvlJ_I_Sm_uEJnYuzbYS2NJjagdM0OeVO4m7vVrWO10jttJzlFaGlRYS10pvRSqdipkytckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=ax373LZxZFejLfXaSZmNMF0eTwGBr51hgrkUS1xF2CZ-gnI6tQWS-ts3vZyt1FyoAyfUWtvVGYLyHQixXbGnHfL-hZpg3YtkuAx2eO8rQgl9N5ObWo8X82Ly_zSIa7j5WDKml48ZiCOtsK_UFS5nqmJK8M2RxgPby-mLkKXbSkdi6TRklOzwBOcIOn2IF068ddlJpQOojLXfgJJRhxuk2eKJX6CWbZhIHF3sSvQY6zrj_AJ9I49R2sYM3gFRNEI0PZynIELj40gsPcfdDr2g8U65mgsmjrsncID1Swms2sQuyxpVmXvoO2U08h5mmZlvutNU-kKcuyf_biOuOUVjjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=ax373LZxZFejLfXaSZmNMF0eTwGBr51hgrkUS1xF2CZ-gnI6tQWS-ts3vZyt1FyoAyfUWtvVGYLyHQixXbGnHfL-hZpg3YtkuAx2eO8rQgl9N5ObWo8X82Ly_zSIa7j5WDKml48ZiCOtsK_UFS5nqmJK8M2RxgPby-mLkKXbSkdi6TRklOzwBOcIOn2IF068ddlJpQOojLXfgJJRhxuk2eKJX6CWbZhIHF3sSvQY6zrj_AJ9I49R2sYM3gFRNEI0PZynIELj40gsPcfdDr2g8U65mgsmjrsncID1Swms2sQuyxpVmXvoO2U08h5mmZlvutNU-kKcuyf_biOuOUVjjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS8RFD-3ClbVNX4tUeQpYT3z0tQDF-XEFhpT3bR33GNMb724bZ4oGUeM4ttBLV1NnOXIzv8n-tdtoD4h_AfP6d2U9JP6gf1tMo0TcstNPU3R1H6V_MN-MMD-rEoZRY_8iTV5FCtntqaPUEizYLKf15bAsegi1TaI5cjHdccJ46r5D3XC17ZKl6k11htc1FN0oiLqXIwUPdlnyavQmf3p0_5591sv3ImRZb38nFUYFST5qcPwTIzuFuw6xCptshcVqUBkM86z20UNeZEiXES-oHhjVu7dtd3WgAQa05LkprcBJGdepY2D1mfqltCohC3q-XucEEfWpllbUmtlAT8MbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=puI8aJ8kW9zPyzs3htxMuVCaGXuJqSNQ5myYzb643WuXZldbqdH4DFKwGLVQk5kR2gpP8EKJlabk_Q9Tqg7wsumgkDJxuS13nHXDBeRa_U_bbWaG0cnP7KEU4MBjvxFXwjGqAZby7aRc6X1lBxzXGnA37cxzP45ATi3ckcS8SkP2VMGLVGBS55d0P0he2RQAEsk59a-Y87qFJryOvtbfMjfZkDSXe36YDGX0pR7c-tkYebYydNooeCrCHt1zJ7EBSrvBSzSWsS8Y_fGkWZzz8ISoE-yJBqeMAeef-KWEGh_9gFZBikw4aWYSLTrE5nGqfMqA--JK9zCmCyHD6RvXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=puI8aJ8kW9zPyzs3htxMuVCaGXuJqSNQ5myYzb643WuXZldbqdH4DFKwGLVQk5kR2gpP8EKJlabk_Q9Tqg7wsumgkDJxuS13nHXDBeRa_U_bbWaG0cnP7KEU4MBjvxFXwjGqAZby7aRc6X1lBxzXGnA37cxzP45ATi3ckcS8SkP2VMGLVGBS55d0P0he2RQAEsk59a-Y87qFJryOvtbfMjfZkDSXe36YDGX0pR7c-tkYebYydNooeCrCHt1zJ7EBSrvBSzSWsS8Y_fGkWZzz8ISoE-yJBqeMAeef-KWEGh_9gFZBikw4aWYSLTrE5nGqfMqA--JK9zCmCyHD6RvXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=rJiw4pyfjwV9bgeNoAk0_5Ie3RcMzTilJz-gA-H13_4bVFzfcfx91YyILVmbOrV8lrSlNDiftlMHmZNokzDFGlxJ6I4eJLnBKWDRGKe-Yk4eLBk6Km8TMeJOs2nStsV0JtJbPnUpPRiGbe2aqRIrr6h0efticbTE65D0V9k2cLkJCwRytRkyrGAumYTbDeO3ESIYCG17YuFwdAsAj53y6n48_Gz62K6VfsM8mbqA3bZwd-vH8g_nkbcIFnIY6PNX7CH7uheLTahAdEf-YiMhtZl2RS4tE5IoapiTBNduPFJSsxbQKkY0EblqSwHbImNYifBjACX_fvlAcyOxu7E-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=rJiw4pyfjwV9bgeNoAk0_5Ie3RcMzTilJz-gA-H13_4bVFzfcfx91YyILVmbOrV8lrSlNDiftlMHmZNokzDFGlxJ6I4eJLnBKWDRGKe-Yk4eLBk6Km8TMeJOs2nStsV0JtJbPnUpPRiGbe2aqRIrr6h0efticbTE65D0V9k2cLkJCwRytRkyrGAumYTbDeO3ESIYCG17YuFwdAsAj53y6n48_Gz62K6VfsM8mbqA3bZwd-vH8g_nkbcIFnIY6PNX7CH7uheLTahAdEf-YiMhtZl2RS4tE5IoapiTBNduPFJSsxbQKkY0EblqSwHbImNYifBjACX_fvlAcyOxu7E-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=Xe0qNH7FD75QaM4e1fjnBLnNeoH5zDxvM15mzyLuoknwO0nKAZjLR6V9R7MERZS6G76ncpKfERkUtoBQQb8AShPD-LobIMi8cyv1vSuJmQmX6k6IlRI1ODLCH3vg0HcSO3X2MRdr1VRK0HBy-vOL-KWIugkHFpjD0MoaCq1U-qQhqbkDa8pDe0Tbzno5WRsjYVy-vzphdO1J4YEgf_2bAM4tX-jtnagF7IRXNZYays2WtRo7I5XV-vjk7-6pSyO1ZGMlVljUoVXVcsv2ykBwBVu-2mhJlCa2AEw6TTIebPU9j6ltOuh0xKxowNrF1AOgaBS2MKP-lprzKOLJa7PGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=Xe0qNH7FD75QaM4e1fjnBLnNeoH5zDxvM15mzyLuoknwO0nKAZjLR6V9R7MERZS6G76ncpKfERkUtoBQQb8AShPD-LobIMi8cyv1vSuJmQmX6k6IlRI1ODLCH3vg0HcSO3X2MRdr1VRK0HBy-vOL-KWIugkHFpjD0MoaCq1U-qQhqbkDa8pDe0Tbzno5WRsjYVy-vzphdO1J4YEgf_2bAM4tX-jtnagF7IRXNZYays2WtRo7I5XV-vjk7-6pSyO1ZGMlVljUoVXVcsv2ykBwBVu-2mhJlCa2AEw6TTIebPU9j6ltOuh0xKxowNrF1AOgaBS2MKP-lprzKOLJa7PGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=Kba92_2vGNGlgF9ur4oXh1bwkkRJlwy37o5y1IA8350hEcgHMVN1FTlv2iwtByafJF4QHSM28r3_xwFTmmNNbaCzwXdZAS-mSQhF9Z_TpQoxUvk0oVX_4CIyAyWH5qlpqmmqivGgG4_nPCoYrLshR3X1djohopUN-E22Td8NuVAkPcQJx6GzTg9VwNQmOsP1ur1GBjg8BLimivKJgnA5THMIZVrVXyZYf7Po0qsoCFhrJUxC6GHBY8ERc_tj0Vw2bUpTqTGQ3oemwiVCYlLq2s3E-GYE3KC1O8YYfEdXGz7-HFZLMJhkl3_dqjpwkmvPIkAXKM58ExcN-f0msP5HAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=Kba92_2vGNGlgF9ur4oXh1bwkkRJlwy37o5y1IA8350hEcgHMVN1FTlv2iwtByafJF4QHSM28r3_xwFTmmNNbaCzwXdZAS-mSQhF9Z_TpQoxUvk0oVX_4CIyAyWH5qlpqmmqivGgG4_nPCoYrLshR3X1djohopUN-E22Td8NuVAkPcQJx6GzTg9VwNQmOsP1ur1GBjg8BLimivKJgnA5THMIZVrVXyZYf7Po0qsoCFhrJUxC6GHBY8ERc_tj0Vw2bUpTqTGQ3oemwiVCYlLq2s3E-GYE3KC1O8YYfEdXGz7-HFZLMJhkl3_dqjpwkmvPIkAXKM58ExcN-f0msP5HAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=itKdFCW3lixgDaTVkOeDE5GQ-nh5hzNvRiv9Pf2E2k3ln_RZ4R7cTQYI84_iGY4qy8v6Qm8wL0980Iz7YMkAEbufx665K9i2r-Qdgo3siTYqLBc4iohs_0bJj3KjbGR0BSJMwODrxXN8S7kNPsPVHNfOA1puAx7SzIhbnIV9b-Px8s1nimbfaMXiTvBfj3BdjJOnFijvCn8Fd2qvSg0wzh4vIR6gx-VOaEEeWM2lqZ7DDDwqlK8NaqhdTGKQra_DefLiWVtESgMm_1IIcnpZ6WXzIMungQDZLQZ9TxeHTTS_00YkMPhKkbrxPKoMvppgx8H1yazH0122M7FzDfUSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=itKdFCW3lixgDaTVkOeDE5GQ-nh5hzNvRiv9Pf2E2k3ln_RZ4R7cTQYI84_iGY4qy8v6Qm8wL0980Iz7YMkAEbufx665K9i2r-Qdgo3siTYqLBc4iohs_0bJj3KjbGR0BSJMwODrxXN8S7kNPsPVHNfOA1puAx7SzIhbnIV9b-Px8s1nimbfaMXiTvBfj3BdjJOnFijvCn8Fd2qvSg0wzh4vIR6gx-VOaEEeWM2lqZ7DDDwqlK8NaqhdTGKQra_DefLiWVtESgMm_1IIcnpZ6WXzIMungQDZLQZ9TxeHTTS_00YkMPhKkbrxPKoMvppgx8H1yazH0122M7FzDfUSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=P-3R2Y6fl_YVFfEvH-6C4FAVWqRI1HjQ2dgVBHcyl6HwGnIUgVA8xKV6l4p6V81Gr_oCMz7uoYjMN5opGXGPvaEJ1dDI1wASz-9ICfkJnwuJ8kkFR97Xfhuc3O4NUaQRi_ejd7G8j4DMLfbXgk2n3Uua3cCizqT14w_BINPuPDf39lZwbXCFK5Zvd2q6p65G3F9Wce1irci3amQE57rp3t4lbKLT64ti8qs4zmW4mmxjy7nTB-QtHIn2IAM1hoofRaROniIGOPfJDlKam0mTekDNLLA5scwwvLBcaQ08CpXIg1JEgZyiS98AmWB4Vikdd7CQtyrfTFIO7oyVH2AXamSwWd62PTop2bjfni54AsbqcILal6TUw5UlumAFMiHo90KlIMQz2WoTc2PWG59FM1SJLduKKIfueKk334NJfcI0VIeRgTngv4xOSqw2BvDXHeMUS6JvN56LVBgMfuSfPsrfnjZNJ541_T16JM0Hqq3GVeXbrv8S8pKbzv6b8s0GbD_m6uN1Lxc8DPVxJLttznoNq3XgjSQ9EEgcKDjLD8bWLTmONuAyYjp21kmbEv1jpuUq4dzCoaYuIJV3vZcsrWxb1nifVt13gen5b5SP_C9YYTiw-pr4NOfXd_cfJ6w4lluGAn3aDSSNnh4beR3uZgAY3Rquv7i7IM_OYZ_spTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=P-3R2Y6fl_YVFfEvH-6C4FAVWqRI1HjQ2dgVBHcyl6HwGnIUgVA8xKV6l4p6V81Gr_oCMz7uoYjMN5opGXGPvaEJ1dDI1wASz-9ICfkJnwuJ8kkFR97Xfhuc3O4NUaQRi_ejd7G8j4DMLfbXgk2n3Uua3cCizqT14w_BINPuPDf39lZwbXCFK5Zvd2q6p65G3F9Wce1irci3amQE57rp3t4lbKLT64ti8qs4zmW4mmxjy7nTB-QtHIn2IAM1hoofRaROniIGOPfJDlKam0mTekDNLLA5scwwvLBcaQ08CpXIg1JEgZyiS98AmWB4Vikdd7CQtyrfTFIO7oyVH2AXamSwWd62PTop2bjfni54AsbqcILal6TUw5UlumAFMiHo90KlIMQz2WoTc2PWG59FM1SJLduKKIfueKk334NJfcI0VIeRgTngv4xOSqw2BvDXHeMUS6JvN56LVBgMfuSfPsrfnjZNJ541_T16JM0Hqq3GVeXbrv8S8pKbzv6b8s0GbD_m6uN1Lxc8DPVxJLttznoNq3XgjSQ9EEgcKDjLD8bWLTmONuAyYjp21kmbEv1jpuUq4dzCoaYuIJV3vZcsrWxb1nifVt13gen5b5SP_C9YYTiw-pr4NOfXd_cfJ6w4lluGAn3aDSSNnh4beR3uZgAY3Rquv7i7IM_OYZ_spTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=LCY8n3sT8SCOv2SVBC2Mf8sgA_sziZWgQiJNBz_hiOHtu5Eptpp3Da38TpB6CwtCamgh19AyNCciZaURUVtDY8WoeZXM8U9QeplmIqShljV6g2tQuwJFojvsHm1o8YhEzppcOeG6J1IZA8pLVhdXhrMaGpxgMZNNvcKiHwkzEsgBV5xK9bG-umaOA52juzjCda3o20pBiNSHyzo9VFw5Vg3Gstt81sJ9aWERztFB_zGqG-HmIUuzW5IS_vL8ent--rNIjwGId1bQHfjDtu1wBCxwfw8es_fp9GJTedfigna3yqd4GNT7Y9_F6s5jhDfvrBF_KTiB6GieTxfg2o0PAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=LCY8n3sT8SCOv2SVBC2Mf8sgA_sziZWgQiJNBz_hiOHtu5Eptpp3Da38TpB6CwtCamgh19AyNCciZaURUVtDY8WoeZXM8U9QeplmIqShljV6g2tQuwJFojvsHm1o8YhEzppcOeG6J1IZA8pLVhdXhrMaGpxgMZNNvcKiHwkzEsgBV5xK9bG-umaOA52juzjCda3o20pBiNSHyzo9VFw5Vg3Gstt81sJ9aWERztFB_zGqG-HmIUuzW5IS_vL8ent--rNIjwGId1bQHfjDtu1wBCxwfw8es_fp9GJTedfigna3yqd4GNT7Y9_F6s5jhDfvrBF_KTiB6GieTxfg2o0PAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Xf7elgWQ21Ij2O5ZCLbT9IPUjg-fjaVi7p87Fuk72qbebfKk3XMjUXtDaXdgMk5xwHvUyZW6UBljjZ8AeAo_6ecVbJmhHdz2bXcKqo9a3U9esOwzeW8EO-rfwqqj6oXqCkIdmpx42xTWBPTTH1jJa2HK6c8Fza4sWspQocXYuB3oM63j0rJs0tbqqN_2ei99eMK2dy8izMPiwWl5Q_RvfraSJ6L4CZy2CZwfQxgpusi_vieZudXdioSNrpoXhmrPuW07tZDRyINVV732tC98r5Rn-RB5X4F4LNyYk51Kg8UZmU8YGqhz-YyR-7qmmO8pyng_1Su6FN4_rlRFHPiTbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Xf7elgWQ21Ij2O5ZCLbT9IPUjg-fjaVi7p87Fuk72qbebfKk3XMjUXtDaXdgMk5xwHvUyZW6UBljjZ8AeAo_6ecVbJmhHdz2bXcKqo9a3U9esOwzeW8EO-rfwqqj6oXqCkIdmpx42xTWBPTTH1jJa2HK6c8Fza4sWspQocXYuB3oM63j0rJs0tbqqN_2ei99eMK2dy8izMPiwWl5Q_RvfraSJ6L4CZy2CZwfQxgpusi_vieZudXdioSNrpoXhmrPuW07tZDRyINVV732tC98r5Rn-RB5X4F4LNyYk51Kg8UZmU8YGqhz-YyR-7qmmO8pyng_1Su6FN4_rlRFHPiTbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRi0guUhbppDIk4DwP_q9g5sjGOKVklBQf8tBlvh2azbkvb8RgnY3wziqOCiumDNva1GYtwmIzyvENBx_WiXD99nOOZVSrIp23fwCHCCG98xlRuvsNfvMhwqyivEj-U1DSbwRVf_ozfAoK8RCdDXHhMaAqiX1gZSpe7KnBlkyVT0qNwz0xCeEiBPecR0eFb19z3AIEY7k2wKFHJs2DYMVkY03L11SHutwZHhxTv8MShi2JGcG6lLQylacTEHw2ATGqPlU9gSDvq0FvbtfG2l-wDB9uhat8PpKunNhBZ9PPZYEZTpGHZOGKNfulvfFK4tqZiTL3wh--P1AKvmgNpDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX3QdW0PXJvDX-awJ_-9qeZHvkF2RGAg3CyEdrXtG9Y5pCrbCGOtmsD2p-o6WwhT7737_VKs8kP7UR-H2AmDQkW0MbAJ92lOoOiBOpterH3WOBQUgv5HmmvUvMAziIw9XATtPZG5DmRQhaLAY1gfpMtEd438j4cqRBgEgl3rvZ0EqpnJSunzV3ywkAoT44SvKvsTvx6UzYHtJFI6q1U_fkpdCwtBTWQXWUZeafK7h35M9Z8sZ3plvyedhiUmqOLg_pncykIhotw4K_lFeIjeTmLLd04GIgHe4ho2MJmkxMh-WPHL7C_s6_B7oT7NDlSQ6N7T03PvoevkEnWXRatPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbDQyKUaj3G6Tbdy7MYOg-n0ZNRH3fg2Mb-tjIX090ZIq4Co_m5YnojBwRwiX8hI8ZX_gRy-LRfFDHizyQ5Ta-7AMkFLVaqDcRVpTRgZCGs8gDqc0cpIsE0lJigVvujt_rLZeIWomBqKT440oZptKbuxALm1WrBrYzmye-hhv_eVk9jmQuQmtP0b6jopKe3JvA_TbwWjvtRZR7xP_Z-srmMy5Hp_fCJZmVrVXO32mskSSIKXNpHTApa-wOm9070qHjL9u3ilte5uf3rZMRxG2rv9HfWlCNmMHc0uFcXWNpyWkR9gqUuVTYO2sUg08sjeKhLnba6RaZ2qyPKEs9MwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzkTzPg1yAOHnGjsWC9m1kU9S84xE4siay1ZBrxw0XMmaMsPzhG_MwCrMssMbSWbC_vudwjXEgmTfwcjH48YbWZ_-Ejw8M08-Skkp3CiKj7xkDXRp4xvl3i8yMzKxXVxN7LAgdzrM7HDA2GWvojhM5uWaYcdlXADW-rMYIAkoHwPJU5G50HDyMiABmbwJvlIpfuXdmhqNoDqIdw7NfRF6oCbv9mJCVoeqaNsomNCkBa7rGYr5j9FCEHsVUH1fx81FVM-NlZPMoR19kwtiSgglP269OSwjPlM_43xMlKIuoUSPYiyw25bBq7q3rT6leX1YGZrvNjuX9S8K9HbEAaTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ePz_sVQR9mK0ieNNL6Zt4dUIaACTZPUDFEC_Q4lIG6C3TRN1e3fS8swNYzj_Y8GBz4WcVyFO8d3bm5eCjxxjmyZ1AGnWSf-5JiIJKlmgEg85n4GfODLo3oDT4AYrAjLVZkPvauwjRqncl--gd1BeKhVq9LfCf-1aC7aMihygAWi4458D6vJ1d9_P3EsBqzelIsmo1bWd2VUpiKF6dD3WeNaQPYzoKpKJpwGFjJwQ23HAQJinoyCG9XVvzm-Zub9_r_nstlPVVabm4ZK_V98T-9AmhWPfd4YygNRrTPCpDd9_Eel-QWjGIoN4V3_-4crwXwibnCkwJWkFmM_v75Tnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=rOw8cxvxALulfDQlfmfmyOEFVloRXpCWKvpc-JtIWxwVjy4Q_vzT7SFnPHFtS-3nvzu5zrX01jbv77pkqEZqih3cFDs0D9BsPD-1HLJXzSIHP33FHbtPceF1hIWWC3piAZ50qCBfITnMGjXgUqM8dckIundY0kAjFNhPhJpnPc3f0J4bg3IeQvE8O3pWld4dWQwkP0SYtHuwkuQtwZIkbOCA3MKCPrlmZyhHV5DYKtcoyl2RcVrP0Oe0DoewH8i6-N34QY0aMX5gsDwvwNCrfRru1BdPfdaVKo_pCFgu1iBYSD3l_ml7-h0VH3SGlUuVguWPasoebE0po9iMQSkGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=rOw8cxvxALulfDQlfmfmyOEFVloRXpCWKvpc-JtIWxwVjy4Q_vzT7SFnPHFtS-3nvzu5zrX01jbv77pkqEZqih3cFDs0D9BsPD-1HLJXzSIHP33FHbtPceF1hIWWC3piAZ50qCBfITnMGjXgUqM8dckIundY0kAjFNhPhJpnPc3f0J4bg3IeQvE8O3pWld4dWQwkP0SYtHuwkuQtwZIkbOCA3MKCPrlmZyhHV5DYKtcoyl2RcVrP0Oe0DoewH8i6-N34QY0aMX5gsDwvwNCrfRru1BdPfdaVKo_pCFgu1iBYSD3l_ml7-h0VH3SGlUuVguWPasoebE0po9iMQSkGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T2FARj2YOp8_A78H1ZL1AWlW-5-48lHXBb6GM5L2wnLQysYzF4abKT2E90fI65zC2kEUydqLR5oENrK9r1dokQ9Cs6jLmOhkT3-83-JzRKqyU4Jv-hnVNaYYY8zY6esFSj1hPT1w083MXgY5QeQyTS765ddDxzWMAam3QWvt_N5BUMLHXwfrQEkp8eMErGVS0XQyvdQmD8q17WA3tRC-3zANrHXmmIqvIrXGNS_0RQkBZxiyLMycQZ0WyVj8vBSf2iANtPNu9f0OQkj3nydSb8KUQ66ojfsHNTRv4fma9M4d1Y8x1lo8MNgxv8WZEHnDZoBgrST_0VDyaDqQtEYRSQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T2FARj2YOp8_A78H1ZL1AWlW-5-48lHXBb6GM5L2wnLQysYzF4abKT2E90fI65zC2kEUydqLR5oENrK9r1dokQ9Cs6jLmOhkT3-83-JzRKqyU4Jv-hnVNaYYY8zY6esFSj1hPT1w083MXgY5QeQyTS765ddDxzWMAam3QWvt_N5BUMLHXwfrQEkp8eMErGVS0XQyvdQmD8q17WA3tRC-3zANrHXmmIqvIrXGNS_0RQkBZxiyLMycQZ0WyVj8vBSf2iANtPNu9f0OQkj3nydSb8KUQ66ojfsHNTRv4fma9M4d1Y8x1lo8MNgxv8WZEHnDZoBgrST_0VDyaDqQtEYRSQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgUQZ91QfOtwGGNXWVo4LmEsM8vMXd8t1QIotYbh1q5KN253PwQxMree4gM2pQ0hN4jH_ZUFvH0hZAoXPLmNMLBdL0nLntPZfeLFqNFcgv-0vIVVqAKRr0VRqhG1MuixvqxXpEH4Nb8JM7EWhYygO5AYGiffP-BhhG9-Xa0Be9LAoz7q74qRlJXx-CG6n3oRqK5Cz1D6HTCt-J6x6FhlL4HAyUOZTYc4GPdXxy1Bu7WYlUUeliKGrPhAJXmz1AC9IyGDD6mCGPL_zhfdxu2xbI0CZp0I_U0Ifp3AD4IryY4Ar_OMoDWXAIx9zQrouIIORctu61pykuFCp-krt3PdnZxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgUQZ91QfOtwGGNXWVo4LmEsM8vMXd8t1QIotYbh1q5KN253PwQxMree4gM2pQ0hN4jH_ZUFvH0hZAoXPLmNMLBdL0nLntPZfeLFqNFcgv-0vIVVqAKRr0VRqhG1MuixvqxXpEH4Nb8JM7EWhYygO5AYGiffP-BhhG9-Xa0Be9LAoz7q74qRlJXx-CG6n3oRqK5Cz1D6HTCt-J6x6FhlL4HAyUOZTYc4GPdXxy1Bu7WYlUUeliKGrPhAJXmz1AC9IyGDD6mCGPL_zhfdxu2xbI0CZp0I_U0Ifp3AD4IryY4Ar_OMoDWXAIx9zQrouIIORctu61pykuFCp-krt3PdnZxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-q7ZYmTqp-6B-nrOz0cwDCS2V3W6S2mv9vRCrIdoRe55k2BJEnS7W3Z2cGq5IizYH1GxtRC3rP9IHzetv4OBnzCXkI94eUpY9AYqh8ZNs5w_JJa4e2skWcEvH88eAeSpPg_8o0FtwNfFfyY7gmrgchW3pLrCk83hQ8WAj6Sq3gvIkBkGk53GtPGDVs-gaOLkNLJjMSzk0XzIfP9hz_pp09QJVs6c6abcZ2oeCValTLCofzqlJb0kdntSsflFZhj3n2Z3iLfYCa1jg3CBfCnqZpjBXQJIQfqyYrJ2sxEM8pM6srbq_zx2AqThSvGs_ve7gCbLMDEk655uNhTbXYoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6oN9hO8U575DLBmi6CfCWHIfVaVw91Q3OjQ5Ccvh45YuRamlt7npT-UKaXt7WRef5gV9gY9Q04N0mqc3UNJfkZuY5pgqxYFdAPk0NcENCn7D19RGpASlpBo_wyybh6o0S9X4cALZ2uYSqU5r86pkHkIZM3fqtoQXohNxalsz3nm_v81tC7TBZCSuHqvOXlMyroqM9lFcPiB0GGaskDmQF3Kof9kfUoRfSL5YJTctDmSBWef-CaNKGa6J6PfOh2_KqWb07Lsf3JlxRIOJkYiDO-NUZSKFN7oi71YMkyuHTzBs5bmgVyLHETUGr4l4LlNctDce5FUN2qvCqoNyIdogA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=Yj3K-odtHZitYQWIoScPRFpWVaTzgdj7rL0LUX8GRh28WYCfGFxae9V6sc1GkM8V90c5XxCG4WKSNJ5JrraLOC-vzCuMDitjDCPb_WlgaRebMil-aSMVnBNgC-HOeB91BKx3LlG4XBVHZFJHQBiCSe0UAexgOCHEU_TXBBPrzpRZMnX3acSDIgFRGfVcABMYb-HVcr_NQs97u8tM50TRc8naZ0UEYAD8yqm7x5s-jDW1D39xgOoXvshMgzUOO2HlYWNV72k1bjNx2FHcytkPyYuAjfd2XKnXA8C7AgO7L6p_dqtFc2og2B8wVJrgGZatlkAvtZ2y7q-Sl9Lxri15ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=Yj3K-odtHZitYQWIoScPRFpWVaTzgdj7rL0LUX8GRh28WYCfGFxae9V6sc1GkM8V90c5XxCG4WKSNJ5JrraLOC-vzCuMDitjDCPb_WlgaRebMil-aSMVnBNgC-HOeB91BKx3LlG4XBVHZFJHQBiCSe0UAexgOCHEU_TXBBPrzpRZMnX3acSDIgFRGfVcABMYb-HVcr_NQs97u8tM50TRc8naZ0UEYAD8yqm7x5s-jDW1D39xgOoXvshMgzUOO2HlYWNV72k1bjNx2FHcytkPyYuAjfd2XKnXA8C7AgO7L6p_dqtFc2og2B8wVJrgGZatlkAvtZ2y7q-Sl9Lxri15ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=XMNtW4zxKqYNZtk7tmqWuZiUW212YG_CxLUF59r3mDal7QGY09pyjrFmZki2M5U6dON8lGmgGvpDlQdwICa106d0aFsjW1wRxcmE3edkJF258F_2Kd105f3IzKo0LKOAiy0STGd-v1Beq_3pkQc8aCveaY4REZgABMepzuf9TlAQK4ZduLiuFeOnkeUKOUB07ACgoH6JNq3bMVaH7GXpd5yEhfr4ytrJdg2bvlYw05POcpEOcCJbjFY12gznWeaByH2wnGjvCZ9-2LiwFKhOn_vdGhxlJY9qutaa9fGwasU60D_S3RwWNV-eGexd_XQrsigS20IiG6YmLvDLGN0hdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=XMNtW4zxKqYNZtk7tmqWuZiUW212YG_CxLUF59r3mDal7QGY09pyjrFmZki2M5U6dON8lGmgGvpDlQdwICa106d0aFsjW1wRxcmE3edkJF258F_2Kd105f3IzKo0LKOAiy0STGd-v1Beq_3pkQc8aCveaY4REZgABMepzuf9TlAQK4ZduLiuFeOnkeUKOUB07ACgoH6JNq3bMVaH7GXpd5yEhfr4ytrJdg2bvlYw05POcpEOcCJbjFY12gznWeaByH2wnGjvCZ9-2LiwFKhOn_vdGhxlJY9qutaa9fGwasU60D_S3RwWNV-eGexd_XQrsigS20IiG6YmLvDLGN0hdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
متأسفانه شعبه‌ای از یک بانک مصری در دبی وجود داشت که بیش از ۱.۸ میلیارد دلار را به سوی رژیم سرازیر کرده بود.
ما از اختیارات قانونیِ «قانون میهن‌پرستی» (Patriot Act) — که پیش‌تر از آن استفاده نکرده بودیم — بهره بردیم و در حال تعطیل کردن فعالیت‌های آن شعبه هستیم.
ما آن‌ها را مستقیماً تحریم نکردیم، زیرا نمی‌خواستیم کار به بانک مادر در مصر کشیده شود؛ اما همه باید بدانند که ما هویت آن‌ها را می‌شناسیم و خودشان هم می‌دانند که چه کسانی هستند.
احتمالاً همین هفته تحریم‌هایی را علیه یک بانک اعلام خواهیم کرد و هفته بعد نیز تحریم دیگری را اعلام می‌کنیم.
ما با متحدانمان در اینجا در حال گفتگو هستیم؛ آن‌ها همگی پای کار آمده‌اند و شاهد حمایت‌های گسترده‌ای بوده‌ایم — چه از سوی اتحادیه اروپا، بانک مرکزی اروپا، بریتانیا، امارات متحده عربی و چه از جانب بحرین.
ما قصد داریم این رژیم را از نظر اقتصادی خفه کنیم.
و همان‌طور که رئیس‌جمهور ترامپ گفت، دلیل بی‌نتیجه ماندن آن تفاهم‌نامه (MoU) این بود که آن‌ها آمادگی دستیابی به توافق را نداشتند.
وظیفه من این است که اطمینان حاصل کنم آن‌ها خواهان توافق باشند؛ و قطعاً هم خواهان آن خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=mqaCmvsHZ8Ryvlz1Y3RHWoPxJhGH1snwUKMJkqEaiTcSz-COsw_dkuV_xsuPtQHCGm47VK3DMERZ67PSLnvuq8j_GdLEgci1eETw9xYS3EnD97nbDs_RegS10SSWNwYoU2_AUluG29rRB2NiaYiiVUMGG-wZoadIrqe5XexQGjwomoUQWKPi5uKTPAtTAOmvXBl3W6YDCZzk6KWQ2tFtJheAPp2b7RAnatUuhUMap7vYTRFtEUQeVwGv19v-ieDNyEY-jHnnuz5Gzre11B-1SqT-sx4Ptj-IkMovEpiUUSmSxIXan4P-CRvT-zkxlYURDRaIK5TUhENmX95OC8_j5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=mqaCmvsHZ8Ryvlz1Y3RHWoPxJhGH1snwUKMJkqEaiTcSz-COsw_dkuV_xsuPtQHCGm47VK3DMERZ67PSLnvuq8j_GdLEgci1eETw9xYS3EnD97nbDs_RegS10SSWNwYoU2_AUluG29rRB2NiaYiiVUMGG-wZoadIrqe5XexQGjwomoUQWKPi5uKTPAtTAOmvXBl3W6YDCZzk6KWQ2tFtJheAPp2b7RAnatUuhUMap7vYTRFtEUQeVwGv19v-ieDNyEY-jHnnuz5Gzre11B-1SqT-sx4Ptj-IkMovEpiUUSmSxIXan4P-CRvT-zkxlYURDRaIK5TUhENmX95OC8_j5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
ما در ۱۵ ماه گذشته، در حوزه نظامی به اندازه یک دهه پیشرفت داشته‌ایم.
در هر دوره از درگیری، عملکرد و نحوه نبرد ما نسبت به دوره‌های پیشین بهتر بوده است.
نیروهای مسلح در هر دو حوزه توانمندی‌های تهاجمی و تدافعی، به مؤثرترین شکل ممکن در حال بازسازی و تقویت هستند.
این اقدامات مرهون آن است که فناوری ما بومی است و جوانانمان این کار را انجام می‌دهند؛ از این رو، نیازی به روی آوردن به دشمن نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70920" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70919">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Z7xa2qFzoNRhnujo14JvPL07iNyyTI-OTlA8omQOYvap2i_koyF9IzOPMbfkgJpEE5cT5YPzrpD3mEYthY88neRCw8hR5IrDsKIROpRT3_Wyq9kyoVeeWd7qztr51jOfQZqa8qSYUQ_tbiPgY0LFO_Fu4tNC9Ter3Bxn9-WItwSTSf1zuiLkAHk2DRe_KDRsceO4B55MGT12occw56iYHxlZbQYnNGyxSG0Brkd3vzG1gE3E-3a3jhXEMkTvxYb61UxNxO7dwLkJyS-P7Bhv-xxhrGXvM_9hYW13zktwQqiMUXzGtJKOkUd1lMclSX-i4W56Kvwi6hDeGTih5Btk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Z7xa2qFzoNRhnujo14JvPL07iNyyTI-OTlA8omQOYvap2i_koyF9IzOPMbfkgJpEE5cT5YPzrpD3mEYthY88neRCw8hR5IrDsKIROpRT3_Wyq9kyoVeeWd7qztr51jOfQZqa8qSYUQ_tbiPgY0LFO_Fu4tNC9Ter3Bxn9-WItwSTSf1zuiLkAHk2DRe_KDRsceO4B55MGT12occw56iYHxlZbQYnNGyxSG0Brkd3vzG1gE3E-3a3jhXEMkTvxYb61UxNxO7dwLkJyS-P7Bhv-xxhrGXvM_9hYW13zktwQqiMUXzGtJKOkUd1lMclSX-i4W56Kvwi6hDeGTih5Btk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=RRISVDw-Fqjdd8SV1k_m6qcnqjDa7K5-rHN6JeUvnmN0oaaM-7ZmFm3rnjsKuVciMgCzTHlN46q9nklIi_BeXwzp1gxq6dwiBsU7PTU0vJUyDNQN2IWxxqYREuUhRFFTo_lI7XYHcraNu_Mj9l6faBpLaIy2sk8hutUa0-ngX-RAAG8cudZHDpPqssY-9tQXX4sYk-iJZIxoK1VZGEAN09MlW0bwLwTNBIAqULwMl6pOKg_IBCTAFDAXKBHQbFU70nmJdEVSM4LuxUyW2yljCQkSHrVpQEvwbTm3PkgZl6k7IU0BFhNyaeh0D0lKvScrpcxhN5xIqdieJvKJcaNbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=RRISVDw-Fqjdd8SV1k_m6qcnqjDa7K5-rHN6JeUvnmN0oaaM-7ZmFm3rnjsKuVciMgCzTHlN46q9nklIi_BeXwzp1gxq6dwiBsU7PTU0vJUyDNQN2IWxxqYREuUhRFFTo_lI7XYHcraNu_Mj9l6faBpLaIy2sk8hutUa0-ngX-RAAG8cudZHDpPqssY-9tQXX4sYk-iJZIxoK1VZGEAN09MlW0bwLwTNBIAqULwMl6pOKg_IBCTAFDAXKBHQbFU70nmJdEVSM4LuxUyW2yljCQkSHrVpQEvwbTm3PkgZl6k7IU0BFhNyaeh0D0lKvScrpcxhN5xIqdieJvKJcaNbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره اندام های تناسلی  حضرت آدم و حوا:
حضرت آدم وقتی اومد به زمین دید لای پاش یه گوشت اضافه هست و میخواست اونو بِبُره
چون حس میکرد بدرد نخوره و فقط تکون میخوره
که یهو حضرت حوا از آسمون ظاهر میشه به آدم میگه نکنه میخوای مارو بدبخت بیچاره کنی؟
حضرت حوا بهش میگه جریانو و اون منصرف میشه
آخرشم میگه حضرت آدم وقتی حوا رو دید اون گوشت دراز مانند لای پاش دید یهو تکون میخوره که فهمید نه مثل اینکه بدرد بخوره و منصرف شد از بریدنش
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70918" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70917">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=QVtFf15SOYjx48fQ5xtX8SXHgdqF-XF5ZRpDDQvp7Ll2GMDGDEgwCILLjkTA2bedgVxdi7ydP0ExvtnE_twqQCf9ialHbNFUGuKq0BPfP6p72Rqzi5xHMAtGmJiwZLrT2NshN1TKU-x7ad0l8jq7GNrBuxyZhhhSU9rojwKIJtEcRM_S_kzMA_VLfyGoKQT9xWZ6zLcrExPm2gFGJok2gdysaPDl-tzHuTJ7QggR6USgPhGknp135J_TigAGoy6pkGvRBb5s1BuL5aHU1Xu9z0yWIOWAUgve2-ukCH9-28tsWEjq6xRpZ9GutkHrDmn_LQubHqWOz5i0bdMYsBK7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=QVtFf15SOYjx48fQ5xtX8SXHgdqF-XF5ZRpDDQvp7Ll2GMDGDEgwCILLjkTA2bedgVxdi7ydP0ExvtnE_twqQCf9ialHbNFUGuKq0BPfP6p72Rqzi5xHMAtGmJiwZLrT2NshN1TKU-x7ad0l8jq7GNrBuxyZhhhSU9rojwKIJtEcRM_S_kzMA_VLfyGoKQT9xWZ6zLcrExPm2gFGJok2gdysaPDl-tzHuTJ7QggR6USgPhGknp135J_TigAGoy6pkGvRBb5s1BuL5aHU1Xu9z0yWIOWAUgve2-ukCH9-28tsWEjq6xRpZ9GutkHrDmn_LQubHqWOz5i0bdMYsBK7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70916">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=gCg8peF9gT-NUpsXfKokWqyLWniFfg6Uq6hLofKw16Eh16egCgjS9OUmvNFJEeATO65qQy9R1Zq1Wjo32DgR_AizyLsaDGJoONieolSi47nnGu1nxMqo9vxyoonfz0m4xQYEryCbwwCHJ7ZJR0oNjCK1Ud234dLrMMLyB1YTK49eLL8gkDbsOFCXHT1vqI208jPjgMOKMyl8T0vY0qutPyHkFmPh4bWnumD_pan4BJZW4oqebeYw1Yy7T_V0XUo5T5ZPtVhdNHpgy8-SqsFOFPQLuCnqujwLXWzJQ4lJHe2Dwjx8YR3LzV9FuKwZVWigR-3Jibo-xUx5qEkmr1M6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=gCg8peF9gT-NUpsXfKokWqyLWniFfg6Uq6hLofKw16Eh16egCgjS9OUmvNFJEeATO65qQy9R1Zq1Wjo32DgR_AizyLsaDGJoONieolSi47nnGu1nxMqo9vxyoonfz0m4xQYEryCbwwCHJ7ZJR0oNjCK1Ud234dLrMMLyB1YTK49eLL8gkDbsOFCXHT1vqI208jPjgMOKMyl8T0vY0qutPyHkFmPh4bWnumD_pan4BJZW4oqebeYw1Yy7T_V0XUo5T5ZPtVhdNHpgy8-SqsFOFPQLuCnqujwLXWzJQ4lJHe2Dwjx8YR3LzV9FuKwZVWigR-3Jibo-xUx5qEkmr1M6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏺
فرماندار ماکو:
آیا دولت مقصر گرونی هست؟؟؟ خیر ما مردم مقصریم باید به خودمون رحم بکنیم
قیمت ها خیابون به خیابون فرق میکنه تقصیر ملت هست که تو ذهن هاشون فکر بدی دارن
یه عده گوشی و قلم گرفتن بر علیه دولت مینویسن نه آقا ملت به خودش رحم نمیکنه و خودمون باعث گرونی هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr-DqO097WPWjtqg5AYfTxqyOhcG1aLr41zwFdChibxPe8Lv5iLjCaMkqSetETZdNAy9uzADuN7pPphy_Bl8YUIIeQfEGfWlZtGch-cb6cW6QjT5o2k-4Riy1tU3p-vE-rcNzgZBteT2SwdQ0Y7LhE-y_1vwBnbSt2sC8OvqLr-ON53ACy-l4XXqJm-B6HIdRJYLtNs4yx6wqZ0QueFN1vAjJ3RAimTQwGwa-r1lw5jOevHUaMfLhQoi9ByMhk67hBnRo1YeHkdfYgZ61NfhSkfGlcHsMDX7yj__5o0L_0e-s4C_nemafxs1ToY6Kc4mJiy20Ed7dtEg12ZcxzsbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jr2_Lr3TbjgBp83OcTpDI4Heau02gOB3Ht7yGxK2z6xBfHHtcpOdbpVw-0JrDsLdFo1VfBEpBaMPkezVQ5FZUDa5wDewj_roUqGm0xpPNG0gM7sCQxFCZlSbTlz1XfEGsCmGd42vhumXhf39y8K6ApgjdjObefkfdfpcwF3ELKjcPW0snGOPpnf-xFVfRUpd7gTqqhdgl6dTt3SuG7qGv5zcmk0U4gf8L_bCC1w4UrOzBC5xxF9IuEokOEDNkeX7rkOnmZ-4XHQBvFgn2BMswvb2pEyKxS14yQU3fPbk4dSXZFm-kBTyxXxDterNHYNMbtm1uIrK_FOCjCVdCkBOkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=mcBKve73xfrkKPuBOPnRBEY8LOfP1-oTxfy8gO-PMjJI3CsqD6eVCyvydWDzweJSkLXmX6mYVeFOuM1Cqyi8Z_CJ3_A7rsncxFi9zceypRncStuKcIB9zJz9c0RvLC7HUeAYA1ug0Vh2WpLi7rE22NSr67Cg2rtvHtgdWmuFtoSpMa1lQ2nsewfdr_ynBozV54zUGjQwwKxN2SNLH06fYG-e1cuWaLFpQUlapm7GZslseZcv17LeJYMaufaO5j2iKgyK_Zl3YtCPLom-v0zo6BExUpG4zaNjV-bubqUxkFjmJoIncre21zgbgzES9ybGOdywGSac3-xXuKS4aPiXPmx_ztzf2gmon0W4362mAJTXqT3z9Z3i_qGW6TZ8TroXeiOSUb9pH4Z0iDgJB_jIXNT20EJG_FRQh3J8C6amm9fqUJUM2ws8W4zAmz7ETjvek7ObpXPbilufJmEVcEvfkCdYEZybFc0L5Bn2pTp4PsODMu9yTsU1XJdYBcXBRx_2hzPzUISP7qKRiT0S2qw6JW-iOIadLPKmQE3FAHUjWjr6SSqoh_jqRnHHhxT-uPFjGwTXmyBCHOwDDuYrGsbQaP5bJjA4JSHfHPYNVOZzz2hxiCUoP5ugmPfO2rxXbMRDuKXJUB4UmMyEIyNDOdp8-tN3HqKtFwj8SfjC1RX3ZXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=mcBKve73xfrkKPuBOPnRBEY8LOfP1-oTxfy8gO-PMjJI3CsqD6eVCyvydWDzweJSkLXmX6mYVeFOuM1Cqyi8Z_CJ3_A7rsncxFi9zceypRncStuKcIB9zJz9c0RvLC7HUeAYA1ug0Vh2WpLi7rE22NSr67Cg2rtvHtgdWmuFtoSpMa1lQ2nsewfdr_ynBozV54zUGjQwwKxN2SNLH06fYG-e1cuWaLFpQUlapm7GZslseZcv17LeJYMaufaO5j2iKgyK_Zl3YtCPLom-v0zo6BExUpG4zaNjV-bubqUxkFjmJoIncre21zgbgzES9ybGOdywGSac3-xXuKS4aPiXPmx_ztzf2gmon0W4362mAJTXqT3z9Z3i_qGW6TZ8TroXeiOSUb9pH4Z0iDgJB_jIXNT20EJG_FRQh3J8C6amm9fqUJUM2ws8W4zAmz7ETjvek7ObpXPbilufJmEVcEvfkCdYEZybFc0L5Bn2pTp4PsODMu9yTsU1XJdYBcXBRx_2hzPzUISP7qKRiT0S2qw6JW-iOIadLPKmQE3FAHUjWjr6SSqoh_jqRnHHhxT-uPFjGwTXmyBCHOwDDuYrGsbQaP5bJjA4JSHfHPYNVOZzz2hxiCUoP5ugmPfO2rxXbMRDuKXJUB4UmMyEIyNDOdp8-tN3HqKtFwj8SfjC1RX3ZXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRp7nq27avzG3yysk72jAji4J-RDJfCh3acS7sGMoITtlQI_DCPMzPxPkapGTytBjhOTrsLHxdncDBfWcnztiHhG46eCu7nVn88OxigOOwE7wI1C1hPhQNNqORpfZLecq4ey9jVcP_UYQFg26SJG9GA68wZh8gK7HVzMV7DdfLtt-6T6oW9F2T1n3IdG_wDcvIsncAcFI6J_4i3lG_v9x2mwrqbfSesIv7aY3871Si0Dl2zuHP-z_fU_8JDVDxDBfBgAsK6HDV6eqzj53DvwIqR5PdIsOnS40Se0iKUA5lXbiNyXtQSuIxeaXR7q8Vs-DGxj0HF28dCEZRSGvhMs-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=UWYSfbROPtae1k40srWxSrn-aRw_DFqJJ9cqJTwkGzz0cClOg57mgF_fd121A0YSUQ2CfppXlgjj7qhGMY170V8xvmN81FJtY58cj4S5CCk77zlTtQJNG2DMmfi2QJ8OlJrNZCqrB-bvnjDz4NJ_8Q-7qHz9VU9_90su-MmuFRu5eGqIREc1-W0uhWAkMKOze7AnThEPQZr0yJsRCJat2nou8QGHj3U_3c__G2ozl_QVTDhA1Kkuzsk0_ig9GpupVSiOsjOu20Di4XXwgtCoGZu-yvClCatH6gL7zAkO9r6oVULCJqJTrd1XM-mKs9eIJgHWmCgc41fW5HCT_kH04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=UWYSfbROPtae1k40srWxSrn-aRw_DFqJJ9cqJTwkGzz0cClOg57mgF_fd121A0YSUQ2CfppXlgjj7qhGMY170V8xvmN81FJtY58cj4S5CCk77zlTtQJNG2DMmfi2QJ8OlJrNZCqrB-bvnjDz4NJ_8Q-7qHz9VU9_90su-MmuFRu5eGqIREc1-W0uhWAkMKOze7AnThEPQZr0yJsRCJat2nou8QGHj3U_3c__G2ozl_QVTDhA1Kkuzsk0_ig9GpupVSiOsjOu20Di4XXwgtCoGZu-yvClCatH6gL7zAkO9r6oVULCJqJTrd1XM-mKs9eIJgHWmCgc41fW5HCT_kH04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کسبه پاساژ پایتخت بورس کامپیوتر تهران می‌گویند مشتری نیست و سابقه نداشته که پاساژ تا این حد خلوت باشد. یکی از آنها صراحتا اشاره کرد، گرخیدیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70910" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دندونپزشک‌ها میرن میپرسن کدوم کار زیبایی تو دندونپزشکی رو نمیذاری بچه خودت انجام بده؟
به طرز عجیبی تقریبا همشون میگن کامپوزیت و لمینیت!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70909" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70908">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=NdAHK02Ykpt76t-HFujsFVu78XadV-4xygWHBtYrALVoZjmxiMECK4PCafcxjunLl-anU6X4LjVWSIZpFuMKBaD_KDTkYUzcmWoH6WJTt8pUQPxBZqTQyE-0a4u5KBzLeVYCoKE9gcQhl7LTmi3aRVLVF3HGmH5GWNVA26WhOGExf0iepxFiI5qKNPRHSJBCWmouVdmfo-Mr14yGi79nV-czlZ_lK74-7aBjiaip8QUNVrfpuVe-3btlsQNXWyMW2jT8mlAo5GiAU32WUV_NU3eqcHWXecz6-ak3rZWXDEQ5QNJS5_4aZ1tIrxwdQVnZAA28_sZ39mv5SuHOYjfesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=NdAHK02Ykpt76t-HFujsFVu78XadV-4xygWHBtYrALVoZjmxiMECK4PCafcxjunLl-anU6X4LjVWSIZpFuMKBaD_KDTkYUzcmWoH6WJTt8pUQPxBZqTQyE-0a4u5KBzLeVYCoKE9gcQhl7LTmi3aRVLVF3HGmH5GWNVA26WhOGExf0iepxFiI5qKNPRHSJBCWmouVdmfo-Mr14yGi79nV-czlZ_lK74-7aBjiaip8QUNVrfpuVe-3btlsQNXWyMW2jT8mlAo5GiAU32WUV_NU3eqcHWXecz6-ak3rZWXDEQ5QNJS5_4aZ1tIrxwdQVnZAA28_sZ39mv5SuHOYjfesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70908" target="_blank">📅 12:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70907">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70907" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmYckz_KZKjJtLIRQhZazH05iOu2OLBkfp-IJbuG8ebHzj3dxWEwvrwz1DDJrhMtvGSIkrUOskJOvnzIKiq62fn8TRxrkTdFHS4nkm0cbu_tY8517z38D-wGkRtqpY-LdSwk7Damy1imjEt-suCi2DYL8zpv7f7tXZIbXBqntbLlHWOqkdWjLivotyWS7H5mjGuPHAq1B5qQR91RyLKzp0UiUba8PvBFs3I1OhQMQMAwev9isiqyXbrXMTm-9D2UQM62TRir1fpoXrcez5WO-PLz4DMa54y3LKYKOY7mjup1h34uLkdNDxRuxUAvjozZUBI4OEps94HucHAWV8-UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
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
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70906" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70905">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ترفند یه آقا برای فروش بیشتر:
برا اینکه فروشتون بیشتر بشه پای مشتری رو بخورید
😟
اگه پاشو نداد که بخوری بپرس ازش ببین کجا رو دوس داره بخور براش.
بازار خرابه مجبورش کنید اعتماد کنه بهتون.
بعد خوردن جنستو براش معرفی کن و اگه نخرید بازم براش بخورید.
بعد مشتری میگه هروقت بیام همیشه اینجوری سرویس میدی و اینجوریه که فروشتون میره بالا
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70905" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70904">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=IdckLurBcY830oPoFWG96Q9qJ6Zi-ZYroJ1_x9Ppgb2ayOXtLX4dR9aoXT-6o4n2aE8SDl1PpRo3PPLw41tD-488lz75hHhIW_9GXgZAduFICRYi2N5dUkZV-7ZR1XG5heWAzhimZExun9iEaXevlmZvbknSIIJV3jriN95HtCsKT9iygUgjGQRtxIYsIvegVq7_TCjhbUfyX3jZoG34YXIOV88RyFmatJTO67mSnITol_Yool5QoibR9X42hWT5FJvm0bOjnDae3yAQ1iMxKorCa3pJOtokf7g6AOGNytYnoly75bOLier0LHJKpfpvoSqPngKqoVeEihJUCGcCSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=IdckLurBcY830oPoFWG96Q9qJ6Zi-ZYroJ1_x9Ppgb2ayOXtLX4dR9aoXT-6o4n2aE8SDl1PpRo3PPLw41tD-488lz75hHhIW_9GXgZAduFICRYi2N5dUkZV-7ZR1XG5heWAzhimZExun9iEaXevlmZvbknSIIJV3jriN95HtCsKT9iygUgjGQRtxIYsIvegVq7_TCjhbUfyX3jZoG34YXIOV88RyFmatJTO67mSnITol_Yool5QoibR9X42hWT5FJvm0bOjnDae3yAQ1iMxKorCa3pJOtokf7g6AOGNytYnoly75bOLier0LHJKpfpvoSqPngKqoVeEihJUCGcCSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70904" target="_blank">📅 11:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70903">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=OAaWqTi5vuD4G57KBBS8HjwsBAzHiNPGp1zqP-b_4usjIpA9zvFZsj1yapbTpTr8QLfb2PXvptKiK1m-NOOvfcCkN_dmmA085ucbTqOoKK_ShoI_FkIkcNG0dgAZN-lYD7q3LLzZ5iwL-2rs3d8yRZpqz_0jdir1F9rLK3RXwmUhuei8vZy1uNIigz50vN1Lmt0EHTJWDuDNUCpFA_B5B3U9J8yaexxbpzXcJG8ISBvMsHTCTOGFLfpW0Xdhz98eQ3YrOnVbVMxQdNJr72ybWrK5HTOxBzThWsdJ19m7P764gWfvGmNnKOdw4cacOcLOQ3_6qnaLv9gVwaYaR2Thmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=OAaWqTi5vuD4G57KBBS8HjwsBAzHiNPGp1zqP-b_4usjIpA9zvFZsj1yapbTpTr8QLfb2PXvptKiK1m-NOOvfcCkN_dmmA085ucbTqOoKK_ShoI_FkIkcNG0dgAZN-lYD7q3LLzZ5iwL-2rs3d8yRZpqz_0jdir1F9rLK3RXwmUhuei8vZy1uNIigz50vN1Lmt0EHTJWDuDNUCpFA_B5B3U9J8yaexxbpzXcJG8ISBvMsHTCTOGFLfpW0Xdhz98eQ3YrOnVbVMxQdNJr72ybWrK5HTOxBzThWsdJ19m7P764gWfvGmNnKOdw4cacOcLOQ3_6qnaLv9gVwaYaR2Thmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حمید رسایی:
هم‌راستایی من با اسرائیل در مسائل مهم کشور(جنگ و مذاکره) مثل داستان دویدن یوسف و زلیخا به سمت در است.
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70903" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70902">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=oBIQ-INmU-NYue0KhlGDnjNtWUstyDrsWGu-AzLhL10IOw7u0lzG7JKNYa6I5of-RbN3zrVLGbp5Ip3N13v4CVTq_ohiw3ecC3cSHE0Wxy0BJi9pxp4ttdoaabwVqf5dMA77-5ICUyXszAimuQseil6sSevk9UWV-dTIc53oneYFefDVHlYZ25dJTg4J8lDaMcWrtFqm87yDluXL3PcfpUun_SvKftZZEJpYFDo5Pqan7_V6ir9ln-SGqd_DRgT1PooRYN0l1Io9hFBqc1wfe8uKiZ-TWU2LNJZ2dhFDmDyGjGXCsrNa3qdKnXQoaQu1DsyT0PQHVZIaCU7fjhmiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=oBIQ-INmU-NYue0KhlGDnjNtWUstyDrsWGu-AzLhL10IOw7u0lzG7JKNYa6I5of-RbN3zrVLGbp5Ip3N13v4CVTq_ohiw3ecC3cSHE0Wxy0BJi9pxp4ttdoaabwVqf5dMA77-5ICUyXszAimuQseil6sSevk9UWV-dTIc53oneYFefDVHlYZ25dJTg4J8lDaMcWrtFqm87yDluXL3PcfpUun_SvKftZZEJpYFDo5Pqan7_V6ir9ln-SGqd_DRgT1PooRYN0l1Io9hFBqc1wfe8uKiZ-TWU2LNJZ2dhFDmDyGjGXCsrNa3qdKnXQoaQu1DsyT0PQHVZIaCU7fjhmiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجددا در سراسر کشور، حجاب‌بان و گشت ارشاد راه اندازی شده، توی بازار تهران حجاب‌بان گذاشتن و هر کس بی‌حجاب باشه، بهش گیر میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70902" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70901">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=umDG_VXGXi7qNf2jsZN1k9DtplXl2H5bcF1uFG0-5lDoHHTTC0r-e3br0tfxQEsYdhCrL33A9c6huOY_wRMAhim_pPeD6TpH10TlmrQBYhsMZ9A_17KzpHxHZAhA0-EKEGwFNmmuBVmcjMTyGmPO0501voGtYhsNsN6nNf_qYrEtlhuu_cDnP46mszz-ks1exNli-ihL7xDAMkBqpAyoHshxyqnVgKgT6Et4k7ewUpU6GulstFKVljC2V5OwZE4PbImwNMPbAJ8ThPezd1Io5hZN00aRE5yYz0n55--NTKSgscqSAZSaGK3lc0CEru5Mr5NDrYAU0SNLnpPqaHn-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=umDG_VXGXi7qNf2jsZN1k9DtplXl2H5bcF1uFG0-5lDoHHTTC0r-e3br0tfxQEsYdhCrL33A9c6huOY_wRMAhim_pPeD6TpH10TlmrQBYhsMZ9A_17KzpHxHZAhA0-EKEGwFNmmuBVmcjMTyGmPO0501voGtYhsNsN6nNf_qYrEtlhuu_cDnP46mszz-ks1exNli-ihL7xDAMkBqpAyoHshxyqnVgKgT6Et4k7ewUpU6GulstFKVljC2V5OwZE4PbImwNMPbAJ8ThPezd1Io5hZN00aRE5yYz0n55--NTKSgscqSAZSaGK3lc0CEru5Mr5NDrYAU0SNLnpPqaHn-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر ماشینش رو داده بود دست دوس دخترش و داشت بهش آموزش میداد که این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70901" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70900">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=cDZloSDZg1nwvklv0ttkQSD6TO6et17t_PMQvMY0NfQrv5TTmprygzGGkrwNmgMoanEPnKGAn3VhWtO8Pmd4zqtLvG4IevWaMVGcqk-2WWqRwEZVHjAY9SPtSHDA5pYQSdwi0XJg87qmLHtwcQPLkm-4OPbFhS_9vytelpDtBemZtpbaGbeoyqEL0Hn0f-zAeKIIb5t5tNxifiebjESJRaYVya--BEKXNd2L3gUkOn0kLgGRCnCEaarPPk5vilbx8t9bC5x09Y5cI44tBune26sOdiAa6orgfPzIXZqcZ-PHweHyvEB4aK0aEU0Ywkh6_8x0bolZ8o0xsQd7tMmlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=cDZloSDZg1nwvklv0ttkQSD6TO6et17t_PMQvMY0NfQrv5TTmprygzGGkrwNmgMoanEPnKGAn3VhWtO8Pmd4zqtLvG4IevWaMVGcqk-2WWqRwEZVHjAY9SPtSHDA5pYQSdwi0XJg87qmLHtwcQPLkm-4OPbFhS_9vytelpDtBemZtpbaGbeoyqEL0Hn0f-zAeKIIb5t5tNxifiebjESJRaYVya--BEKXNd2L3gUkOn0kLgGRCnCEaarPPk5vilbx8t9bC5x09Y5cI44tBune26sOdiAa6orgfPzIXZqcZ-PHweHyvEB4aK0aEU0Ywkh6_8x0bolZ8o0xsQd7tMmlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇳
خب، این آقا سانت رامپال، رهبر یه گروه تو هنده که پیروهاش اونو خدا می‌دونن
.
این آقا برای خودش یه اتاق شیشه‌ای مجهز به کولر درست کرده تا وقتی اعضای فرقه میان پیشش و پاش رو می‌بوسن، آقا گرمش نشه و عرق نکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70900" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70899">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=vdAHLQZ9WIW-ZTrSudNauSoAkAbsxlKOSdmG1EdpdmUtz_jkYpIGYvgppTEWrVP9gAc57abEmrYQ-gEWvt4_J5UBuCzgB7Si6MWO4E6Ozzv6EiOeaH95GyyJfgE84xcpsS6a1eKDyLyOsVfSejgFDdfcKVbyQDBa8WCwAAm_NAXscwJ_Nn2FMhBabM6_SQ8llo7RBoyYIq32xUHBf01fKnlV0yxICSIe0BGN6c0z9KEsNehBe8LQIbctjbfXqIgRXzKxb4ZhAEiNsL73CML8nqIPO8cIctKKEWJ69itTjXlkNPzoVMoBj_j4dqwUQplGzpVf3t33LG85ZDQgIZg8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=vdAHLQZ9WIW-ZTrSudNauSoAkAbsxlKOSdmG1EdpdmUtz_jkYpIGYvgppTEWrVP9gAc57abEmrYQ-gEWvt4_J5UBuCzgB7Si6MWO4E6Ozzv6EiOeaH95GyyJfgE84xcpsS6a1eKDyLyOsVfSejgFDdfcKVbyQDBa8WCwAAm_NAXscwJ_Nn2FMhBabM6_SQ8llo7RBoyYIq32xUHBf01fKnlV0yxICSIe0BGN6c0z9KEsNehBe8LQIbctjbfXqIgRXzKxb4ZhAEiNsL73CML8nqIPO8cIctKKEWJ69itTjXlkNPzoVMoBj_j4dqwUQplGzpVf3t33LG85ZDQgIZg8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی تبدیل به حکومتی شده که نه فقط مشکلات مردم رو که وظیفه یه حکومته حل نمی‌کنه، بلکه خودش تبدیل به یک کارخونه تولید مشکل برای مردم شده.
تقریباً اون ده پونزده وظیفه اصلی که حکومت‌ها انجام میدن در ایران انجام نمی‌شه.
و بر خلاف اونا حکومت جمهوری اسلامی تبدیل شده به یه جایی که روزانه برای مردم تولید مشکل می‌کنه. شده کارخونه مشکل‌سازی. شده حکومتی که مشکل‌ساز است نه مشکل‌گشا.
مهم‌ترین دلیلی هم که مردم ایران از این حکومت متنفرند و می‌خوان سریع‌تر سرنگونش کنن همینه
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70899" target="_blank">📅 09:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70898">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEfmb8JJnI26RmHdKYHarJFIavhGrOvaEbwqIOiajxKGSLDv3JjVUuig4qHkKBHtu4OY8faSRLfMKGOBpwHJ7Ht7kKJGdaOTn1WvK6_L1OdsnbFglLxTZXyD6u-gCSAyPEFlKuFRlENtQUUR-dN9zz-cyX2lSAVkBhlyeWQ_oGtgbH0CE1Sf1XJI6BPE6lFCtU58Y_MGJZi9WPSd6h8vQem_GZwXXEfY48qEAHvMthRFEznu3a1dMR90N9_6T8-xOXnUmdFdVtFsL48bXrzMCE1_7jU92sDwwZNyOd6RAqFj1yd0fs3124ouYE5-awGpVF8TyTSMczoZBGYAre_gVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70898" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70896" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-ck5V7BsMFv3ZzKDEElbC4NvNrT9p8vnJn8n3O7W5mZR2sZVl1FJ11coX5QVmU1f44mOPOhfUBBQNA9DbVazdI637cJ1kMc0Qs4E6sjFR0jgNX06v2IPGHDXXzagaXdy52LBJ47g9rEsXKB71NIvyaOryUs1YRs1mAvB9gMk_Uu9X5y7nFuzolIZPEC3THTwG63XXA4z4TYNaTPeWgJ_YR-Z1-ledhcIbvnabsiAZn2E6W1SIiCRpaqbRfyUvi27RDFM3bqCmCmSKdEhNwyROptMPmhcrDu_BcB-VEUr-kM9syKE_OFAcj7BuG2xh3Ieo4RduqH2OxkHzlR67nuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70895" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkVfDcYxixDljRxg74B4QzuqdA1tYXmDK6s-rC0Mkot-VIi3ZVg3OgTvDLBh3Vw1NRFfTopX5aQ9dOrhBgpsR-Q2VY6Z1mLfXMoF5KgfqObhwlTU6F5BDx7kihK1RIOQBZksIvtxEwfmMKTEqCEEluzbS2HdyKiRzZ58aFO6yWq-r0ZNFIIh680y-TY4MFmw-lw0ZgUwHtqLgaxcthzdxdktyGszyHQFREmFWcPGMFNFjImX6du0JRkb78-CY_nCvwoaW8ZWfEScFhzW0dsfo-hRLCBrbzkeB3prH_iXK39mhPEEgzbPmj-0aa4VYfYWZ1ycoMyTqlkyahCXCjrKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=qZyFCUIlX-kvM35uOUirtc5nhttdTYY6N8fCzJl8AYEN2U9KfrmI9Gfutxfee0MrpJxRkWy-UxlpLfi63XKFkmAyt1LxnjWYbWpjmJyylEm7nhEG_SoH0bzbpzLSM_K8V00fWYhHF8mHxYpiSDYJUPV7nHSonn--G5IXCgZVMAWctAmGb75wWuzbkTYlKDTe5fpPASVc4C0RGnxJ7mbUpsrxAS3kgL_nMdC-wwbVTWX8YaN8VQFYcQMyUsPV9ZerGBNY8gDWRe0wDpyYMZy8E0ZHfqGdv0bEPeJLS2MXMxNfzo_vBUW4Qs1p4xZ6eH-_z-AT10ebgPDUq1bFN3IllhRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=qZyFCUIlX-kvM35uOUirtc5nhttdTYY6N8fCzJl8AYEN2U9KfrmI9Gfutxfee0MrpJxRkWy-UxlpLfi63XKFkmAyt1LxnjWYbWpjmJyylEm7nhEG_SoH0bzbpzLSM_K8V00fWYhHF8mHxYpiSDYJUPV7nHSonn--G5IXCgZVMAWctAmGb75wWuzbkTYlKDTe5fpPASVc4C0RGnxJ7mbUpsrxAS3kgL_nMdC-wwbVTWX8YaN8VQFYcQMyUsPV9ZerGBNY8gDWRe0wDpyYMZy8E0ZHfqGdv0bEPeJLS2MXMxNfzo_vBUW4Qs1p4xZ6eH-_z-AT10ebgPDUq1bFN3IllhRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcByQTANEPBwUz_-uEA2yxlDmunkEqLpGB7YdWTKkwKDF6C2xJY25vrvnrqtXT4lQ826JUX7pVnWQbJkaEoSagErkvzluKCUl20CLN5Z6KjgS_TbGZ-wimC2IEBubqBMMJ94U9dYTUi5ub3CmWj7TaVgJvXrQ5zBzjJPF0QP77n2BaDth6ehR_DspZvZfmYfo08XRQ_ErpEMd4EyU9gYFoDY-kItZ2zZvpY6LFH27mhh1beRaxiPaAlx-O72YVRyeDfbg_YdIfjL7CSIcXOSHClO0C2Xp9m04SeB68Gb3wIJgtp-gtxAAUx-Iid4mP5JL3JOROdMTkZ3J5AkzNXLXhz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcByQTANEPBwUz_-uEA2yxlDmunkEqLpGB7YdWTKkwKDF6C2xJY25vrvnrqtXT4lQ826JUX7pVnWQbJkaEoSagErkvzluKCUl20CLN5Z6KjgS_TbGZ-wimC2IEBubqBMMJ94U9dYTUi5ub3CmWj7TaVgJvXrQ5zBzjJPF0QP77n2BaDth6ehR_DspZvZfmYfo08XRQ_ErpEMd4EyU9gYFoDY-kItZ2zZvpY6LFH27mhh1beRaxiPaAlx-O72YVRyeDfbg_YdIfjL7CSIcXOSHClO0C2Xp9m04SeB68Gb3wIJgtp-gtxAAUx-Iid4mP5JL3JOROdMTkZ3J5AkzNXLXhz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADBYNAEcnaSX6H1ZpVt-5EpTOrpiMD4ooIj6YE1QdVu8sVSfx1afjtbpjxrC7xzrK-7sdfvHmx7B7HKIbXpIFRWZft2ulI_CI12f4YvCeSktTWKBY2oV-ZcG1Ku1qYNtwtwyQKR_QgplZWv8to5cgdn3vmOT5ugiYe8MuHik3z64zirsq6zEvzEH1hahBFjzmLo27G_yLpCLACUOeq1VzLS9Vr3sc8KU0BqDOtQm6hlXR2YVdDleUviiQSeiF3lPlx6ZIccDdTZXuefNWy1W0qDTGgzWYM5AK3z2jyDFoE1J8BdWDZ8dDfM9RnlcTV_yifVCbuN0kanSOJfpXFNMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeT7ZjhnLKOlVh0lWtaq9GqUPzlOLiZrvDXaDTTJ3szGdxMRe1qIGXB1T0pZkHonhOGVSLFbP7nRQ4jeWdz5358XCgg79X6z0rD2GA6rP14WVxMWqNQsqNXtb0jSKfFX5MTkWILIE2UQ0yh1Rfeaq9bPRZ9CqtuLIlae0RPZdNQ86zNBsiqIH5XfhbKxOvOyxw2puOp-CvQoKAp2NHJQ6lQcuF9dkxDPdduTy-NBnEMT5YElKEjHK6GJ78VB1_XYFNo0YN9tW4gCwmkZowQAwBCzwk0FOwxZRxYMn8Ayh_zqFJEL5fqZNDttp10t3fFPjUZl9Ucokij1SPjyNKveWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=Q0wcQxVmF3y4dwdJxfQUCtgMu--fWTWMzdyFFk9OEYT6c128UAYG5SDJEymSt1TDL-1Lyc_6rDN7KqACEWtc3gjnqtxiNaSm1KhayFh4lUW3AHhCAAkRCEhIhPo3rObcOByAA7LXKvYFX40HGmlp0FjKtJsUIj_bjNbb_L-JnYVajIEPOA6tMWycL072BY6Za0A627P3a_BibYcMmldl_edLHA33FphjHdT-tVj0BvVmj2B2e0-XrPQIIZ-blkrPAik1SWpFr8souUFQX4ZqSEIjgKRzxpf58LVbEwKfriQSXD10xkheVoor-yZkc0n32leVR1Fd2yNZeWOdWpYr0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=Q0wcQxVmF3y4dwdJxfQUCtgMu--fWTWMzdyFFk9OEYT6c128UAYG5SDJEymSt1TDL-1Lyc_6rDN7KqACEWtc3gjnqtxiNaSm1KhayFh4lUW3AHhCAAkRCEhIhPo3rObcOByAA7LXKvYFX40HGmlp0FjKtJsUIj_bjNbb_L-JnYVajIEPOA6tMWycL072BY6Za0A627P3a_BibYcMmldl_edLHA33FphjHdT-tVj0BvVmj2B2e0-XrPQIIZ-blkrPAik1SWpFr8souUFQX4ZqSEIjgKRzxpf58LVbEwKfriQSXD10xkheVoor-yZkc0n32leVR1Fd2yNZeWOdWpYr0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=CQA_1HuXcAlWhKLLsirvrm9D0CC99Bv4lfbYcfZOJDUGlb36zx4gHz-6IkRO9nOhNWPkjVepry_1dN_ItqD4mxWabA_Bh98mVaaElIjMMhEEC68hmaaOyc6GoeikUQFAcJJhLMu6AyFF59KAl_9zmc4ZucPW2Hl_KabXfRqbD8H_xdpYrlW-PyYq_e-8J3vrTHTJXubLO2oiHjkxeq5k0TECoFbbd31otBwT6vcrDQVpzxduyb1sr49ywSTtOEcO6f0hZDWmi6hZ_aTTZKFWKxmtw2qxysCQqS3gu3eue-DwUPef0eAujmaxHc2RG3I6Kiz2TyGNAMNOFMGrJfy0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=CQA_1HuXcAlWhKLLsirvrm9D0CC99Bv4lfbYcfZOJDUGlb36zx4gHz-6IkRO9nOhNWPkjVepry_1dN_ItqD4mxWabA_Bh98mVaaElIjMMhEEC68hmaaOyc6GoeikUQFAcJJhLMu6AyFF59KAl_9zmc4ZucPW2Hl_KabXfRqbD8H_xdpYrlW-PyYq_e-8J3vrTHTJXubLO2oiHjkxeq5k0TECoFbbd31otBwT6vcrDQVpzxduyb1sr49ywSTtOEcO6f0hZDWmi6hZ_aTTZKFWKxmtw2qxysCQqS3gu3eue-DwUPef0eAujmaxHc2RG3I6Kiz2TyGNAMNOFMGrJfy0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=pf2mXDtOS-tj1kZHevqHwMxBZjsKCJqEcrvX2MsRbRrhfp7XFHCjRHqW3aYM9H5RzPUVdHpfoc1MWg4SeHK4at38RkhysOZPAgRzCwuQ0ec9zo4T3VQZqHhO0XzoXdqiaXvQuZ09SuYs2dQvhOLohQAON9b8_ytKTWsNhLDTK2wCYOjO_qre1Gk_iRjmdS30XbSAuVpQr9DA4Ln57tBcNeyfbxym-iW2X2fxDbY1oeGslqelXyJOCIo1LxRc9aTNoU3_jbehk6J7Ht73TFKfjQO9iku6z1dP_6cmmpsW6p6v2edg7G037S9UJu6tXgjWBIL8Kc7muaXr9G71n6FpzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=pf2mXDtOS-tj1kZHevqHwMxBZjsKCJqEcrvX2MsRbRrhfp7XFHCjRHqW3aYM9H5RzPUVdHpfoc1MWg4SeHK4at38RkhysOZPAgRzCwuQ0ec9zo4T3VQZqHhO0XzoXdqiaXvQuZ09SuYs2dQvhOLohQAON9b8_ytKTWsNhLDTK2wCYOjO_qre1Gk_iRjmdS30XbSAuVpQr9DA4Ln57tBcNeyfbxym-iW2X2fxDbY1oeGslqelXyJOCIo1LxRc9aTNoU3_jbehk6J7Ht73TFKfjQO9iku6z1dP_6cmmpsW6p6v2edg7G037S9UJu6tXgjWBIL8Kc7muaXr9G71n6FpzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqOJJNbiY7KSH0WX5BJC23HNNxmeBvE9V8gfgz1EIp4rQFzxexKMnLHkoJgopriHmVN75xDIKMNCJz1ZU_SSFMruNnPqbuB7THuXlo7TkJKwbApkKBYDX4IZCIcy_WVBH9U0UaIYFz5lr1rpSaZiAbdrN44tfN9DWTVKa509KhGF3cAAl2v4xSkU3sspBxDNrLP6fk-mt_OImuJzPJQX_2B7FPI_0EqnpokRgkpvNYD8w8EJNNvtisDMVc7p3K4vmX9HsEJXEwQCntbNj3gKsKQsKfbFAm31__0m2W2JfYQzXY8KgySEarw4mDYvUIcaFpf00b2Hk6XQaiuOI2WNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-M3gCSS-TBh6c8dCH_xd1vfUctfvuZXoNl945qdXwlMjNLY4UIS8NFl3Hf1D_0Rz3iC6YfXhIzXDC8qzUarhB7hSPjcq_xWnJJ46Ga0dyz1PNa69gI14R5FoZVpxgx8_t4MHq7Ly9LkGbLRy-kPPPxjTbN3_qnO73hCGTv33j_-IYJpvhd1qjN2BIWgHBrkSlQocSR2ANJaaqR7H7vsxG3vYimfbC2aQApiwgrSZwMczOLBzQ8lhVDAnME1VC5zgZCydlx6zAwPgoNWv3CMMrRr3sgu-PgudFj-0j0sbAHFLen55UpXC487X7Oz1hiwgoIpbld_VxMWRaw45jnlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=Vm_3jEotV4UBnc6EsLI8ibmkNXzGFjPfM8Yu2Jq16mOv22O8M5JK1WtX_m2EpfU5gX-faQoWRP2F1u9X7tG7UhceQmN3tZ3-NMa5lePtyNvY7THzV9cm8vvboqYZjKV3NEz7FuYP4xFdM06Q_ju7ivExAFmLZSsNqsi7B-ce7S6PJIEPeeAPOWMVHn6qT49lUgrQ6Di09q9WMd4VcF6Xmmc2oKPZK_pAgl_OUwE_UIVj7GfSyop3L_M379_iOKEqKBNEmGnt-YyOa_FloHBXNg4U-xiGZxckuGiZyAZQ-TvMFuo4nGlom-i_99N8TWt6ob-OmH7MUjILHlTssPXm-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=Vm_3jEotV4UBnc6EsLI8ibmkNXzGFjPfM8Yu2Jq16mOv22O8M5JK1WtX_m2EpfU5gX-faQoWRP2F1u9X7tG7UhceQmN3tZ3-NMa5lePtyNvY7THzV9cm8vvboqYZjKV3NEz7FuYP4xFdM06Q_ju7ivExAFmLZSsNqsi7B-ce7S6PJIEPeeAPOWMVHn6qT49lUgrQ6Di09q9WMd4VcF6Xmmc2oKPZK_pAgl_OUwE_UIVj7GfSyop3L_M379_iOKEqKBNEmGnt-YyOa_FloHBXNg4U-xiGZxckuGiZyAZQ-TvMFuo4nGlom-i_99N8TWt6ob-OmH7MUjILHlTssPXm-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMgJXEss4jl3ktkVc9td7jMIxI8ORsYnQBz9on0yNfeXBF7DamnaN9AQoMkgDw793z5F9-XvhaydzoeXsmpMW_ZOy6pGrE_SIijfiVT3BKxdTZIblUtKk4Ef5FKGh0XfXx1abVTqeB_jf-G8JIrAPY7IrKi2vDS9Q69L-f5d-wus2NgMS4ND5qazqk6_ThBha8jRAt52QtvusTGsXr_KOP74Ee1mdwJgc6yqsDGoKX3_I__udfCmwTKr3qSn1gwfvXwjsyQsoBl-VL_ZT9xFxwgycfCd0pd-9oqoBePus6t-tzlWcMcsRu7iSL8oysXH5HplzOPzmhgpMDVU3DVXnVqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=iLvM0IlrdilUfxcOoMHe5NJUVSQvfMi0DgU-kDL_hVmgJ1nMxUtQwgnbSSpHUtM7CgVKJ2xnIJTgo6izy8asFpQ8qk9QTp8yhebf__Mm7vgrO8aHKyYSnpzHDhr5ztZnXcPGIlXriNFsRpZsrfztKYMEPWuKo8UElh3bTWgq-ZpUJkgkUWBd2NgdTw4736oxiik634toLfDtwRXmTizE_P2HhVW8dxSHA3O66fIH0zrbgXbNuE_Z9UkwEo__wS9Jk9rrN6W3wWF71UXsvy6965RG4PNXmR6Woe7wxCLB9_ZWgCZ7lrHsRPuLpaG0bHPYoftFprudDQUcSQgCDUKHMgJXEss4jl3ktkVc9td7jMIxI8ORsYnQBz9on0yNfeXBF7DamnaN9AQoMkgDw793z5F9-XvhaydzoeXsmpMW_ZOy6pGrE_SIijfiVT3BKxdTZIblUtKk4Ef5FKGh0XfXx1abVTqeB_jf-G8JIrAPY7IrKi2vDS9Q69L-f5d-wus2NgMS4ND5qazqk6_ThBha8jRAt52QtvusTGsXr_KOP74Ee1mdwJgc6yqsDGoKX3_I__udfCmwTKr3qSn1gwfvXwjsyQsoBl-VL_ZT9xFxwgycfCd0pd-9oqoBePus6t-tzlWcMcsRu7iSL8oysXH5HplzOPzmhgpMDVU3DVXnVqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=LmXCK7EHqqwiUcnllfXiE3qD36D4ZXVyBU_8GCLBh-qhS-2KjcnKfKPIuPaN-UStR-wQF76ghmK3JqQLscRulgS42QayudbjLJWmvr4bbruWR4j4IUg6O0BaEq50SYlb8ccQJi0I3CtqUgVrzS3Oog2IR94a0A2Iqdni5xkWAc0FqnZHvnm1M2IsNMuz8Tgb02gHmxtxz362WusJw24fUHxKO83fEoGTIGje_XhqAnDCFoLlWNXpvjdoFXaBtQf0DXHDmsp0S1084eOms6a2fzec1sZ5k99sDj8tzqsoLlyYTbOE6TbcpoUfuKWLwo5gjSlM80BVrreSfY8CJrznOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=LmXCK7EHqqwiUcnllfXiE3qD36D4ZXVyBU_8GCLBh-qhS-2KjcnKfKPIuPaN-UStR-wQF76ghmK3JqQLscRulgS42QayudbjLJWmvr4bbruWR4j4IUg6O0BaEq50SYlb8ccQJi0I3CtqUgVrzS3Oog2IR94a0A2Iqdni5xkWAc0FqnZHvnm1M2IsNMuz8Tgb02gHmxtxz362WusJw24fUHxKO83fEoGTIGje_XhqAnDCFoLlWNXpvjdoFXaBtQf0DXHDmsp0S1084eOms6a2fzec1sZ5k99sDj8tzqsoLlyYTbOE6TbcpoUfuKWLwo5gjSlM80BVrreSfY8CJrznOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0omzO31UW5CnNvlfyn_7jHBt2iLyJTbqT0sEPD1mtHWiwfv2tYVhtU2h52eTMcwRGSlHeW8wNnrg230M_WDGUxhpFKpjXwz6SMa-PDWImtCg875hOSbeSGu5m3AIQFgQVIWS83d0OwEht9DJh8vh2fFdveMKyegnKb5K1HIwMXPU6RA1tjJwhTZmXAdKueG4bJfwtelf45zUc_2EFFqP78hHmCAPl9oPGKaY35G9Q-b58ZT6mf9MCrgU8QphMPmH1UOFtD0Y06Wk4AT4tVSxwFBi1CmdFGcWXFMSl7QEwUmXsCqw6ruTA1ifJCbcj3HgDPrrQzuOFvjxl3nMVLYdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=PS2A9RUy9AJ8HG93uTfnj1MI4pxcyZSb6Egy7PS9LmZgZgEECyTFLGjIRHGwRx-NZ3LSSnVyS0CAEhMqI2tF-tt_5H8qhVDQfEsxDGv_d8QaNH_iyxh0On1IRnowFLfr3ZJ1mSLlKBdRyY8G_RO1l4n-pclqfM8Pwh8U3b1ZmNtBsm6csOnM-CnXh4E8aF4OPMJ3WFm-na1QgtGSjXIqfDF33sB9BS0VCWQtRyod9Qyv9jcj0jxIhCw6TDyT0tPKD_itGivDHhAlvqA-CEbw9eyHPNlz4IbgBAWmjU6IWXNZDVPQrhEhMhSM5NUBShfIT4iErNiRu-hfsN6qC5SAlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=PS2A9RUy9AJ8HG93uTfnj1MI4pxcyZSb6Egy7PS9LmZgZgEECyTFLGjIRHGwRx-NZ3LSSnVyS0CAEhMqI2tF-tt_5H8qhVDQfEsxDGv_d8QaNH_iyxh0On1IRnowFLfr3ZJ1mSLlKBdRyY8G_RO1l4n-pclqfM8Pwh8U3b1ZmNtBsm6csOnM-CnXh4E8aF4OPMJ3WFm-na1QgtGSjXIqfDF33sB9BS0VCWQtRyod9Qyv9jcj0jxIhCw6TDyT0tPKD_itGivDHhAlvqA-CEbw9eyHPNlz4IbgBAWmjU6IWXNZDVPQrhEhMhSM5NUBShfIT4iErNiRu-hfsN6qC5SAlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=syceJknWJ1Vkq81Qv9aeudHZlZoBXFGEKUKZMgpHrjkTsG92ohDm_9JpSXJ_L0zJofQ5W1etVygoYvf6H0xaXfavvDPDyzOC6NjcDidYDiq02EaJEXhtPZFgct6AjF0pxHJRZf-RDgn-NP94jR7IfMtQASRLfpkdVvuIQc2kkufdzwP9bwH3aZGaQACo2F5L0Rvua4Hayau83GyzK_xl7HFZ9DEl-g0ub2UcmhySHs3bpqAXJ00vX0rk0i421VJO607cBEFpQp6bQLbZW9hNyMtPHsg6CWfwtPAE3GsSbXEBS6EWmObGJuTJvTc2X5O54qL1KIHSiT-VPkyBLyeZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=syceJknWJ1Vkq81Qv9aeudHZlZoBXFGEKUKZMgpHrjkTsG92ohDm_9JpSXJ_L0zJofQ5W1etVygoYvf6H0xaXfavvDPDyzOC6NjcDidYDiq02EaJEXhtPZFgct6AjF0pxHJRZf-RDgn-NP94jR7IfMtQASRLfpkdVvuIQc2kkufdzwP9bwH3aZGaQACo2F5L0Rvua4Hayau83GyzK_xl7HFZ9DEl-g0ub2UcmhySHs3bpqAXJ00vX0rk0i421VJO607cBEFpQp6bQLbZW9hNyMtPHsg6CWfwtPAE3GsSbXEBS6EWmObGJuTJvTc2X5O54qL1KIHSiT-VPkyBLyeZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=AM8QbCqD4BLSdppIdkeAEGO8k0cqstR9AOaHDNDW2qfiMb-VkHhEUNRFvygyGQBV6BVxj3FIS-qvQ-QRGQxOYQD9iATUlDKPKDRv9jekRFEtsQHBZTLtfO7zUvP2antpxVFKKsHpLpUaMxE-TKV8o5BRiQC4O6hVAJaRltOnY3T3Jd7XCJq0P3CuhZaZ593aR3RZmzU5xCGQwkAdJtDW1Ll3OY3uYja2Ss6meArTr3J3R_uFkuwUSnhKtrDy1obfbjeNKnpRpmDGLk-wXMOjBgAEGbEJIoVyc1o0uXlXpKJJTTmy7NUMf0Xd-iUVQJ3tflZ18bTRBXa5H_nKnRHYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=AM8QbCqD4BLSdppIdkeAEGO8k0cqstR9AOaHDNDW2qfiMb-VkHhEUNRFvygyGQBV6BVxj3FIS-qvQ-QRGQxOYQD9iATUlDKPKDRv9jekRFEtsQHBZTLtfO7zUvP2antpxVFKKsHpLpUaMxE-TKV8o5BRiQC4O6hVAJaRltOnY3T3Jd7XCJq0P3CuhZaZ593aR3RZmzU5xCGQwkAdJtDW1Ll3OY3uYja2Ss6meArTr3J3R_uFkuwUSnhKtrDy1obfbjeNKnpRpmDGLk-wXMOjBgAEGbEJIoVyc1o0uXlXpKJJTTmy7NUMf0Xd-iUVQJ3tflZ18bTRBXa5H_nKnRHYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBZWec7239pE_wxAGLDoXrV0ydPxImTu2497PGHHziBYiJ0uVRTk1tyx-ZQWixOBqLnDa3TsKKQSnNuMDFfcPVlCXI8ECdu1BrNLq8mk2dS9FBash4RwpBmBJZaAON6mtSzfsdtn38fYgik6GjxlKELCQzh-vAP4fCgYxq6eXY5_lvYZX96AP-W9MuVJXPxv9jRQMD64BViLtZon5Fj4MnJO727IfRB1bodkRiwBgUyRyGtOHJskgjPIo0wOKTVeopUQqjul-0BTrpGnBaZmA2It9R0XceTdnrbAPNbUK0h2mcXiHkeuGSRxraZAmN2Dh9vayWWN_4XTOyhLw5olEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
