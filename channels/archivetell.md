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
<img src="https://cdn4.telesco.pe/file/CUOd7a2k2qFO7tvQcL5aJxQ1QBFCgKVSs4EMWwUrtcoayu-RMxbHUWCpxEa9kuGulmTbj_PikFK2hdRSsOZlGZnBh8acGuld3arotnt37uun2TAkHOw-R98QmBQ49X0PcD-vpwrtp049JpQ3rdl55Ajx4BKx2NecMaQhkLPznXeh4xuu_TIUdiLRRFYvCdkmDKKaDi0VJazeKVHs_E5IWqbUCCavxJBYAp6T-WL-AIoRUkf00wy7QzxTajOqi0hXdPiRpVJmuAeistcyL_BLenRFxWHEC--9c4Sz2OCRNWKe__xWYj4eyoZEyk7S33LOSWWiEPv23k5X5QZmst_CiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌بازآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-8056">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX-f4bv0UzmoZ0tGR8a8Qu-AnD0p3hYjKR1ggG-Myt3Uz2cXXfBwaHV2WXRjexyAgP99fNQaiTm4SLy7mncSxrYTGtRchkPyUixcgQIFUe6NNSVpS5-Gusg0pu142rEgR5N0J7KYyzoadbxg4syhFM_-s5QzuBTE-GPh5V02H09dmKZavb5r8S8yJTRZ_B-9nVwJe5xQ-qgzuawpeh17nQx2ZE34V_3O6mX2kLW7v2KU5CjTw8tLiT9Fjf0ajxF960FGh-xXWvd6zrPr7kZGD57j9zd9Ra-2qFh_9AIa2x9uFga7ax30HS-5SsiI6Q4Kt8z52QQtRw4c2bwEHU-Fvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
استرایپ OpenRouter را ۷.۵ میلیارد دلار خرید!
‏⠀
‏استرایپ بزرگ‌ترین خرید تاریخش را انجام داد و دروازه‌ی محبوب مدل‌های هوش مصنوعی را تصاحب کرد.
🔥
‏⠀
‏به گزارش رسانه‌ها، این توافق در اوت ۲۰۲۶ اعلام شد؛ در حالی که OpenRouter فقط چند ماه قبل حدود ۱.۳ میلیارد دلار ارزش‌گذاری شده بود. طبق همین گزارش‌ها، بنیان‌گذارها حدود ۱.۵ میلیارد دلار می‌برن و بقیه به سرمایه‌گذارها می‌رسه.
‏این پلتفرم صدها مدل هوش مصنوعی و ده‌ها ارائه‌دهنده‌ی محاسبات را پشت یک API واحد جمع کرده و استرایپ گفته محصول و نقشه‌ی راهش بدون تغییر می‌مونه.
واقعاً چرا یه شرکت پرداختی باید بزرگ‌ترین خرید تاریخش رو توی زیرساخت هوش مصنوعی انجام بده؟
🫪
‏⠀
‏
📌
گزارش تک‌کرانچ
‏
🌐
تحلیل معامله
‏⠀
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 568 · <a href="https://t.me/ArchiveTell/8056" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8055">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
💸
دستیار Dot با خواندن ایمیل ۱۴۰۰ دلار برگرداند!!
⠀
‏یک کاربر می‌گوید دستیار dot ایمیل‌هایش را خواند، یک تأخیر پروازی ۸ ساعته را پیدا کرد و درخواست غرامت ثبت کرد.
‏به گفتهٔ این کاربر، بعد از یک بار اجازه‌دادن، دستیار خودش درخواست را فرستاد و ۱۴۰۰ دلار غرامت گرفت. این یک تجربهٔ شخصی است، نه تضمین؛ ولی نشان می‌دهد ایجنت‌های داخل ChatGPT دارند کارهای واقعی انجام می‌دهند.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/ArchiveTell/8055" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کد رفرالا میوزتون رو بندازین کامنت با هم دود کنیم
یک میلیون توکن هردو طرفتون میگیرین
https://muse.ai/join
5UYP1O
50KIY3
EAWL0N
4RUYCJ
5GD9TV
8809GX
9XQLZN</div>
<div class="tg-footer">👁️ 739 · <a href="https://t.me/ArchiveTell/8054" target="_blank">📅 14:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amOIAdnhPjMzW6mfPO3tmNtE13-sPGHmhuyq_gpCwEdslVFQSC0A3zXX0Arg2WDCkzV0Rt7IZUM5Jq3QqTHstd5bfpOTV7gyttWPMtgaZeWhOdWvBs6XHFk3VWHDcGR5aSghNl8k0oTF3JV41YFz4ooSsF2rDunASaqbIYThJiE_RMQrIvx042bg7qJ2vlPcTE0k2bCsJxcEkVTdh0S-kLqvJygKVdaOsabpPMq7QyGU14kU6v1j5PHHVNt1LOa0l1yMCQUpwLeW6xfqmPNYmGT239a3uKzphiLUHRJieqPxUj1pspOakfpNVs0raf8qMZJRCBHbcp-GboX7KA8WPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
ایمیل موقت رایگان با دامنهٔ شبه‌دانشجویی
‏
🔥
بدون ثبت‌نام و بدون کارت دانشجویی، یک ایمیل موقت روی دامنه‌ای شبیه دامنهٔ دانشگاهی می‌سازی.
‏• بدون ثبت‌نام؛ ایمیل‌ها مستقیم روی سایت خوانده می‌شوند
‏• صندوق مهمان ۴۸ ساعت زنده می‌ماند
‏• خود سرویس می‌گوید صندوق‌های عادی‌اش بیش از ۲ ماه فعال می‌مانند
⚠️
این ایمیل دانشگاهی واقعی نیست و وضعیت دانشجویی را تأیید نمی‌کند؛ پس روی تخفیف‌های دانشجویی حساب نکن. خود سایت Boomlify سرویس ایمیل موقت رایگان با آدرس‌های نامحدود است و ثبت‌نام لازم ندارد.
🖱️
وب‌سایت Boomlify
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/8053" target="_blank">📅 11:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iaj5gpyPT5sBBmdPWWfHPk_-aeGuZuAXdm0l4tAKvnvLjmg9suZqS52fmfrbJct_XsiqpBw_PH78EPg6Lkm67lHBQlyWb5umEf3x2yAbBA5Ks4NOhYgGMSdYMEvkQ1F45WlmVd4git8fipJHdLt1BVZARfeFiVNDAIHyG2yHZLIvk0DCmM4TnvfzFiF5zEJRvGsjcw_hr6Z9wT16zYxy5hiUdcZDpIUHDdphGb9eCxi7eT5wK8UJUSFg-0xvcXOC0_cFfndi-M3GgqGgYmLMxbFKHGG0WUVnT7ruNKeGjG2a6HhaqK_0TReFS52nF8hSiwHTK5Eu5d69jyG-IoxXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📰
آماده‌سازی مدیران هوش مصنوعی برای سناریوی فاجعه
‏به گفتهٔ Axios، مدیران ارشد OpenAI و Anthropic در جلسات خصوصی سناریوهای یک حادثهٔ بزرگ هوش مصنوعی را شبیه‌سازی می‌کنند.⠀
‏مدیران ارشد این شرکت‌ها از جمله داریو آمودی و سم آلتمن روی سناریوهایی مثل حملهٔ سایبری به بانک‌ها، اینترنت و زیرساخت‌های حیاتی کار می‌کنند. نگرانی اصلی‌شون موج خشم عمومی و فشار سیاسیه که بعد از اولین حادثهٔ جدی هوش مصنوعی سراغ‌شون میاد.
‏سخنگوی OpenAI گفته این مانورها «ابزار آمادگی برای نتایج محتمل» هستن، نه پیش‌بینی قطعی یک فاجعه.
⠀
‏
📌
گزارش کامل Axios
‏
🌐
خلاصهٔ فلش خبری
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/8052" target="_blank">📅 18:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=nL0Ivi_QlIj2CswqgikI1IbJ-o-EPLrQOfnoTMthoqpd1LRn2Xws3yQejv105wFO_RYvDuadZ54OLJzCByYU5APQvdaR6JrooiRp113_DjNfQUSXV2UfhhYFTmirhk9ieGGu9nscDyjHUKMI9JxCF7VRw-KH0lxLBugAfVBPlvhYHVLnyoTK9gSmZ98r4lkALMuD_uY__AXZwdSOCZZk-33a-vD-PZity94nYdBJOQ4hgT8vKyrOH4g3gxmUdlZn-YU6tIlH3m4Nx3rno0mr4hkWwhO_0nAbtpb-HgXxwTd3WWdyqvJS_xC5nHgTxdLSjixM_7Kn5LAHfX169gPVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46ccc294f1.mp4?token=nL0Ivi_QlIj2CswqgikI1IbJ-o-EPLrQOfnoTMthoqpd1LRn2Xws3yQejv105wFO_RYvDuadZ54OLJzCByYU5APQvdaR6JrooiRp113_DjNfQUSXV2UfhhYFTmirhk9ieGGu9nscDyjHUKMI9JxCF7VRw-KH0lxLBugAfVBPlvhYHVLnyoTK9gSmZ98r4lkALMuD_uY__AXZwdSOCZZk-33a-vD-PZity94nYdBJOQ4hgT8vKyrOH4g3gxmUdlZn-YU6tIlH3m4Nx3rno0mr4hkWwhO_0nAbtpb-HgXxwTd3WWdyqvJS_xC5nHgTxdLSjixM_7Kn5LAHfX169gPVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✨
ویجت‌های وب داخل پیام‌های تلگرام
⠀
‏طبق گزارش‌هایی که از نسخه بتای تلگرام منتشر شده، یه قابلیت به اسم HTMLBubbles پیدا شده؛ پیام معمولی می‌تونه به یه مینی‌سایت تعاملی تبدیل بشه.
‏پخش‌کننده موزیک، محیط اجرای کد و کارت محصول، ‏کارت پرواز تعاملی، نمودار زنده، دکمه و فرم ‏همه‌اش با HTML و CSS و جاوااسکریپت داخل خود پیام رندر می‌شه و دیگه نیازی به باز کردن پنجره جداگانه Mini App نیست.
💡
هنوز رسماً معرفی نشده و معلوم نیست کی به نسخه اصلی برسه.
⏳
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8047" target="_blank">📅 11:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8046">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8JQIeDtwQTpoES-ahNOaoD6OiFMqnuthPTxHsu5Bel6fmEKiNJMW-T6p0LvD02HbxgVmCYtjv-W5znhaXCt5FHFSYvdfw5XKEyW1GmCTIMfIDRL-iJvVy8ZsH8wAHvIQIvfqmdEhUuisz-__lFPHqrFDyYE8NXmfx5x7R-z4TuUyiJO7Uxa0VESNPmVD-sBz1JbFubKytYCf_DhBd9hP6TQl6gv7YRqKqfaHdYQGf2tXZ3Nb4zjyCUtb-0yvdRbBuqMk_vpIv0Uen358D9PRD376ngSUHDyHpTq62t7-0Id5CEICJgNDsG_kIs255l5PntXg7fU-3jZp6yMSlllow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎹
آهنگ‌ساز رایگان و متن‌باز Tonefold برای همه
⠀
‏بهش بگو چه آهنگی می‌خواهی، آکورد و ملودی و درام را به‌صورت میدی قابل ویرایش تحویل می‌دهد.
⠀
‏
🎼
آکورد، ملودی، بیس و درام در پیانو رول؛ نت‌به‌نت قابل ویرایش
‏
💾
خروجی MIDI و WAV و استم‌های جدا؛ افزونه‌ی VST3 و CLAP برای DAW
‏
🤖
موتور آهنگ‌سازی با Claude Agent SDK کار می‌کند؛ می‌توانی از مدل محلی Ollama هم استفاده کنی
‏خود اپ با Rust نوشته شده و برای مک و ویندوز عرضه می‌شود. قبل از هر تغییری ازت تأیید می‌گیرد؛ یعنی چیزی بدون اجازه‌ات نوشته نمی‌شود.
‏نکته‌ی حریم خصوصی: برای آهنگ‌سازی از لاگین Claude خودت استفاده می‌کند، پس متن و ایده‌ات به سرویس مدل می‌رسد.
شاهکار هاتون رو حتما برامون بفرستید ...
❤️
🤝
‏
📌
سایت رسمی Tonefold
‏
🌐
صفحه‌ی Tonefold در Product Hunt
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8046" target="_blank">📅 10:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=oS6L-_dwOIoldISRO_SFgYi7pa54EG7qwn5DDnkDvuoUw6RGsmo28Y3u8hH0QEoY9yNkCs0SlwoOR6-YvHluXG3zkgw0KvfM5GORS3ARWvLrwFgKYa-rr73L998ZAo_rw7nsvO1h6l0MVwG9qp5jWULT1aqpUpljx8ac-QQ-s2j9PHgSWtmvA1RtQAeSz8A2Eo44hNUawC7P_-tcBWpENuZIiXVpXHiFKhzEv9ZxRpmPLeO9LtEOcVt-iy6yIZvsSGGxJ5XOYaB9qlGZ8TF30xfpFzvJjaXFcDsE9N2ldJQIYdr3zXNMtEUSpX7DxNkpMKR1wkiIyr6RBFzEYSI7PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f019d0d3e.mp4?token=oS6L-_dwOIoldISRO_SFgYi7pa54EG7qwn5DDnkDvuoUw6RGsmo28Y3u8hH0QEoY9yNkCs0SlwoOR6-YvHluXG3zkgw0KvfM5GORS3ARWvLrwFgKYa-rr73L998ZAo_rw7nsvO1h6l0MVwG9qp5jWULT1aqpUpljx8ac-QQ-s2j9PHgSWtmvA1RtQAeSz8A2Eo44hNUawC7P_-tcBWpENuZIiXVpXHiFKhzEv9ZxRpmPLeO9LtEOcVt-iy6yIZvsSGGxJ5XOYaB9qlGZ8TF30xfpFzvJjaXFcDsE9N2ldJQIYdr3zXNMtEUSpX7DxNkpMKR1wkiIyr6RBFzEYSI7PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪐
سیارهٔ تازه‌ای که با کمک کلاد پیدا شد
⠀
‏یک برنامه‌نویس با کمک کلاد کد و کدکس، سیگنال یک سیارهٔ احتمالی را در داده‌های تلسکوپ ناسا پیدا کرد.
⠀
‏شعاع حدود ۱.۴ برابر زمین و سالی کمی بیشتر از سه روز،
‏دو هفته کار بی‌وقفه و بیش از هزار اسکریپت تحلیل داده،
‏و هنوز تأیید نشده؛ قرار است تلسکوپ تس دنبالش را بگیرد.
⠀
‏اولش خیلی‌ها فکر کردند توهم هوش مصنوعی است، ولی چند پژوهشگر سیاره‌های فراخورشیدی هم گفته‌اند می‌تواند واقعی باشد و داده‌ها برای بررسی بیشتر رسیده دست ناسا.
⠀
‏
📌
پست اصلی نویسنده در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8045" target="_blank">📅 00:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">از الان هرلحظه ممکنه جمنای 4 ارگون ریلیز شه...
من احتمال میدم امشب بیاد</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/8044" target="_blank">📅 22:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8043">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjIFBr24L2kplmJLijQbKjYeGj6NWvnoEC9QguSL5yMjue_5YAdx5fEFI2eqqhZKOwjiHWOk3HAN1UAFXAnGZ_b5-T0Vn0DIOdxYAEh8yCYrLL2SXoP-a1jUAQeNDXcH1FfAmprTApWdEVLWdBl0763b5FmqYFQjppCym5qiLMqJQetD7WBs_w4jHEY9e1R6IEzUGpgBw_V_VUIiY31G0V_9Qfgrlhn_oo8P3R7GXkc8oqnR3KI5R4Qc5PRJg4pBrpCljEAI03ulzQqtuKRKAuDc3MJf3tXsyBlAFJvVz51MXyjp2QWzBlDoJRm00dvtvlazGWLp20qlU8Leh-XL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مدل Gemini 4.1 flash در بخش spark کاربران پرو فعال شد
+خودم تست کردم
تست کنین نظرتونو بگین
✨
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8043" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8042">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmBPewWrYwX3kWHeLb70QdfIazXE5JhLdk-6cUaAH2hdB0Q-ktpbTdE-W7BFyQKxXXIcRqoQNkz8-x_Po1RqVc2AhRPtyWt4lqZv0-6iz3UGODd7r8aGNXCBVBIvs06TRujW-FOh8zsiAmkQSF7lDnjQ7duu_bsdGPeKQc6zqN1xwLGonr2xiynMDfD_GdI85rwrkUDBfrsnSj4QtAiOrNkGT8uuEK9Ww2WxOTN3xJAGwjZXph2ZpENl0-rOv-pGlN8m5nht6trje83HE4pQmQoQ69mlT2fqJZW9La54RUYveY0aEVI8PdfQ9_RU9BlxXvwHgjOHHIBXfHl0-L22qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا ظاهرا فقط بحث آیپی هستش با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse Surfshark</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/8042" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8041">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUQ6XHFIaU53E1f8iKpxNm7i4jtRajEBRPtceLYZUC32adAN7bIOyduZIAx0ncI9fg-StTI4ruzBXF2oGaAyJXSqTjaNrEHBY_zrI1WYWjB0xaVIT4-lTNWttBnghGD2yi5xdIFaho9B3icLrkgfnsIp9vocwe53GSluyxmFX-Nwz_Jkf342MWmn4yE0xc5Sx3nqHmH971hz898q1iVE88QlanOa08bD98hliu2ifbh1LvC59KLhSRHi20kZODUB5W8p_I5v_duN_ZMIAwlSL318L4DqAhseQ6lm6zd81vHj-v8YRYGeSG-6QNftwCtjhDolbef8vFH9nWTf_XjkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
متد حرفه‌ای تبدیل PDFهای طولانی به Word با Antigravity
اگه تا حالا سعی کردید یه جزوه یا کتاب رو با SI به ورد تبدیل کنید، حتماً دیدید که بعد از چند صفحه کم میارن، فرمول‌ها خراب می‌شه یا پرانتزهای فارسی به هم می‌ریزه.
ما یه ابزار
متن‌باز
و کاملاً خودکار توسعه دادیم که این مشکل رو ریشه‌ای حل کرده:
✅
فایل‌های طولانی رو بدون خطای حافظه پردازش می‌کنه.
✅
فرمول‌های ریاضی (LaTeX)، جداول و متون فارسی رو کاملاً سالم و دقیق درمیاره.
✅
خروجی نهایی، یه فایل Word مرتب با فونت‌های استاندارد دانشگاهی (مثل B Nazanin) بهتون تحویل می‌ده.
🚀
نحوه استفاده:
فقط کافیه فایل PDF رو بهش بدید تا صفر تا صد کار رو خودش انجام بده. (پرامپت‌های آماده برای مدل‌های دیگه هم داخلش هست).
🔗
لینک سورس کد، ابزارها و راهنمای کامل در گیت‌هاب:
🥹
https://github.com/faithsaly5-stack/Antigravity-PDF-to-Docx
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8041" target="_blank">📅 17:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwjius1NvGV4WdNtNwl2LtTEQtJxzjt6WUdm5OWSLlpyYzI5NNEyp-HcIJ63KbAqcQpIPhr4H_Fmhf-zcSup7U2PQCazmDcXtduOcMeRxcGpMx-ptXLNy1vysCu2c9KbWJZ0DvIfkK0t6FBiu3VrdE1v9gf0IrW929ciptHBPTgieDKiSQvHvRT7butBSLsoXbYGqGrTdvS2gu05hQ-DFs-_IqKCOd660vYSW_-vXBVdT1IE3zB_WqVDQvCRx6O-WMwo9fFTx3DOIBOUs1emhPuhgK7tWLTbCR74fwTIBIXFlh-nJ-AjMLrMvDrQLuA1w3gTT7BTKsmxJ9C5_Caf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8039" target="_blank">📅 07:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inHMD0VAJI-qcSRO3DWI8HLbKNoc3KJmemdmnbkUKgjpxB1FV0-J22WfMkJoyOCez26qjnPXjBaoKKfYor5WkDq7GKuOGffo5KCKCQ7pfJa_6jLOG6sZgDfdwBHUyQJy0NDEku_eYCxIEe695HQhnOskUMHRqkICt4MGLFHi9OnySn1g88lQeZWg73BE-ouysMTpb4BUrCYjmSsQUqNap5SCcJUPWTCr6_0cuPdvc59Ies7-6g9hjThnLnxQFizGI8t49JWlXt58ahv0oYB1J5-TGFluAZZ37CzdGNiQyBIm9YZviUiwbLmPxFGMm4GpTR6qcu7IWHztYlaR0BBgtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه  ‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.  ‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد ‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد ‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه  ‏به ادعای Anthropic‏،…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8038" target="_blank">📅 01:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8037">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">#حمایتی
‏
🔐
برنامهٔ غیررسمی FoxyVPN برای ویندوز
‏به گفتهٔ سازنده، فیلترشکن فایرفاکس رو بدون اشتراک روی ویندوز بهت می‌ده.
‏
⚠️
غیررسمیه و ربطی به Mozilla نداره.
‏
📥
نسخهٔ 1.0.0+1 از بخش Releases قابل دانلوده.
‏
🔐
کل ترافیکت از این برنامه رد می‌شه؛ اول کدش رو چک کن.
دولوپر از بچه های خوب چنل
🚀
‏
📌
مخزن پروژه در گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/8037" target="_blank">📅 22:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8035">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RV3R6YkrszUZY4o1_kH3cpmj54vdtYDLthZUMu69sZwkeXUBH7C4pCV1G6zAnbNqa3DqYmD6ElP9Lz-S64CJfals4hi98_S9-tAFiJLKHcmn7nQnHCKiqZBGXyB9xJ6Q-icTnJckhlZnb_scTtBbkdtVfkyJNgOdptKuOVH-1VydJFE9RxJJkYKz3rl08FI5VwVkmiu8saAjKqtLCsemMtBYX-fLjeMgGAZ6Ah7MgCPpOvEuzGZYhkppOx1C11kXcDannBM-HMK73rtxPPqrFBTc4UNXJooQILCUSavDYTAqfMC2S7GSKfILU2DGTNKVg3MO5fzachAtHFXJF8kXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e43dfc03.mp4?token=RV3R6YkrszUZY4o1_kH3cpmj54vdtYDLthZUMu69sZwkeXUBH7C4pCV1G6zAnbNqa3DqYmD6ElP9Lz-S64CJfals4hi98_S9-tAFiJLKHcmn7nQnHCKiqZBGXyB9xJ6Q-icTnJckhlZnb_scTtBbkdtVfkyJNgOdptKuOVH-1VydJFE9RxJJkYKz3rl08FI5VwVkmiu8saAjKqtLCsemMtBYX-fLjeMgGAZ6Ah7MgCPpOvEuzGZYhkppOx1C11kXcDannBM-HMK73rtxPPqrFBTc4UNXJooQILCUSavDYTAqfMC2S7GSKfILU2DGTNKVg3MO5fzachAtHFXJF8kXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای ثبت نام Muse اگه رفتین تو Waitlist این شکلی مثه گیف بالا
ظاهرا فقط بحث آیپی هستش
با افزونه Surfshark و لوکیشن آمریکا تست کنین
👍
✅
Muse
Surfshark</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/8035" target="_blank">📅 21:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-8ZxxgiNjrmW6JeO9gGfhBElqgjgB-Pu6XZ6oRybrplqIRy_gXUs1HIILIP4oh2ixiiaktTBYy6dXBQg2bvnHN1CcVl81dAZmBrOJH8R7eSFypuOtiUo68SJqDtULVqxiMKTfpKZiJ-9BzJU_ENoEIKRjp2sl8zZsDlNioGx6qua2s2PEbS37e4Ll3cNtlPBAAYce0AcPdrrhFlvNsnkTBk35Xofol2pgzEFgbwXz6dg-cfz-y2bdThI6ZyuiHFXvM8wcl4ZHP_Gwr5A1yXC1VS1jc5nzCF6199n2IK-NjuPRDnnMGeqLkeW86ghElDXGWy5Uf61ceHPvgo3mSWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
ای پی ای Tooken Club برای مدل‌های معروف هوش مصنوعی
نحوه ثبت نام توش خیلی راحته فقط کافیه ایمیلتون رو بزنید و از کپچا عبور کنید ( یا باید تصاویر مشابه انتخاب کنید یا یه شی ای که خلاف جهت بقیه حرکت میکنه رو تشخیص بدید )
‏
🤖
کلی مدل داره که میتونین استفاده کنین چند تاشو مینویسم :
claude-fable-5-1
claude-opus-5-5
gpt-6.1-sol
gpt-6-astra
glm-5.3-flash
grok-4.7
🎁
10 میلیون هم توکن میده برای استفاده اولیه که بنظر کافی هست ولی برخی مدل ها ضریب دار هستند که میتونین از بخش  instructions بررسی کنید.
Base URL :
OpenAI:
https://tooken.club/v1
Anthropic:
https://tooken.club
‏
📌
سایت اصلی سرویس
‏
🌐
کاتالوگ مدل‌ها
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/8032" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هر کسی مبلغ بالاتری پیشنهاد بده این روش با اسم پیشنهادی اون منتشر میشه</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8031" target="_blank">📅 21:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8027">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها ⠀ ‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده. ⠀ ‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه ‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه ‏
⏳
اعتبار ۶ ماه…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/8027" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8025">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1AGgCZK3xaUgJ_bAu9jlheZaR85h6Vq0gZMpZ0NDh-_pBYp5h0VTwpPEEYGo0ZTqrTl73FvOY5EERINQzrGs3Lqbdh5ezt2x773G8nFNsBtrsBOU_rEKmUZ3wJ4oqJr2pLGtGm57MMDtAd-UjCG_WBbvlY-uP0C2Usv1cHWcQGd2tIuZ7ZkwfRT0qfBhhqNYX-6Wll02yXNCQWUfu85jCiJbwj-fivAX_74Vn27zyblJqyJWtMWuD4RQYsdu3ogKxaptVtaMZBgJ8o2Z27gchoJCMBpsyRSKSwPxlpqN0aJ3JtAxtUhMiZGPedqqKryCdrBZTpNGc6nPhMmba9QzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6i5O-Jpc8O7exkoUwMWwYu8hDFW-B0bJo9FIzD1mATIcmrMbr4CQYdviYjhU9lqXj9purmk_R60omIwh8PharIS8yaGbAFzE3dvzGZc3wjNY3gtWjNQN0DF8n9enMr5hp9TrnYKa06iyXcL3vZVyAh0O-aBipWc8FEmNvB8j4b5wozvCTxi3CBdG0aorR2_BWzoOstI4adGyTNCH8uHNchfEynVZD2HO5V6APJvSxSyeOJcx_IfF5jV66tO5my25trxmKu9YsGOkaWrPD7JiKzsELrZGr3dLbn3oiheEBhHZdl5QBmSSnLjCdBHc7X-_D18xDnYfTVS-fnj8gbrhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعتبار ۱۰۰ دلاری Claude برای سازنده‌ها
⠀
‏انتروپیک توی برنامهٔ Founder House به سازنده‌ها ۱۰۰ دلار اعتبار رایگان برای ساختن با :claude: Claude می‌ده.
⠀
‏
✅
فرم رو پر می‌کنی و درخواستت بررسی می‌شه
‏
⏰
اعتبار معمولاً ظرف ۱ تا ۲ روز کاری می‌رسه
‏
⏳
اعتبار ۶ ماه بعد از تاریخ اعطا منقضی می‌شه
‏
🏷
روی اشتراک‌ها اعمال نمی‌شه
⠀
‏این اعتبار فقط روی API خود Anthropic کار می‌کنه
⠀
‏
📌
فرم دریافت اعتبار
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8025" target="_blank">📅 20:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه آفر خیلی خیلی بمب اومده داریم بررسیش میکنیم ... ، فکر میکنم درست باشه</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/8023" target="_blank">📅 19:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=DkjQVTd_RpT7QLRpTWhKJuCAsbWHc9Qrg-WQQ0Bm71E78KZcOkA80FrK_-VNKQLkVGT0E7vuKuvkxy02kI5xBbTIpmNxnp8QIZ1kQwYG4ulhYVyonVZnOEmsZPKYOQ1wf11rynfP7Tf2pS2oNYLyk5sRtkHdC00STDXJCh_mEcbhmJJlaaNEI-jgz4Uo9NjFwGpoe2aZpxe3-xgCMgMgkpWppFbqpHyI-_L0uQg5eYwjE9mv9x4jfS3UnZUJO2eK9VbiDWUqEnS2yaOufmfnj_xG6xHHpL1H8wqVw_2zTh_LJeZ_kJnQ9claP5_P3OiZmsVzaP6e8DgT4B547kr_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=DkjQVTd_RpT7QLRpTWhKJuCAsbWHc9Qrg-WQQ0Bm71E78KZcOkA80FrK_-VNKQLkVGT0E7vuKuvkxy02kI5xBbTIpmNxnp8QIZ1kQwYG4ulhYVyonVZnOEmsZPKYOQ1wf11rynfP7Tf2pS2oNYLyk5sRtkHdC00STDXJCh_mEcbhmJJlaaNEI-jgz4Uo9NjFwGpoe2aZpxe3-xgCMgMgkpWppFbqpHyI-_L0uQg5eYwjE9mv9x4jfS3UnZUJO2eK9VbiDWUqEnS2yaOufmfnj_xG6xHHpL1H8wqVw_2zTh_LJeZ_kJnQ9claP5_P3OiZmsVzaP6e8DgT4B547kr_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldZp0O0XBkH3vWyh9N4WEYok91tDZMz3N167jrHmNXienRVRVTU7ppKfoXkGiBB5i3b0o9-I0lsyUUzBKrLkFTyKKN3O7a4bl6IT8Ky4InmM_RITytrfREoHYphfhxorCwZp93EkpKWtsm7BwPyhvF4xbVU5Dz1RLnyh9Y8zz8ZSphFw6RygmbXD71U5TOpmkv7YqjunZXEsIozgi3llvQSHlzA5GqONgj0euxNIXMjwNoO0Ya28WeHCuq07lNftx7aLBrWKTCYqY23nz60VND36XQVHRQiBh1EW4vX-WFnqTwxDRs7EgIixl08NrjmSldRHC2ON7-4VbvgSmquX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نه آقا ببین ai که حس نداره، نمیتونه عین انسان حرف بزنه بخونه
❗️
🤣
همزمان ai
⭐️
مدل جدید تولید صدای Elevenlabs V4
⠀⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS-EJO9jDZHyy393lE_9I1FLw228zP_dFNnbnO10BqQZmU8XnDt-n0qDptvw_y9o-9qJT9m51yPn2DaLWmSYrUa2SfOkK4cSm2KAe9ImAy2cK3QIH0sLmI4LV3_VGMShg2FiQh8G4Y_aibpxbgVwZ-ZAAAKSCEtaOcvtay8-zqzp930lh7XLEI2uc1CcWzuQsuaiTUhVohdhpnZYrp1p4h_7GOu6JUy6HJJR3_RArQNIDB45-plIlds-UHMXTE0w-5s9DGRMg258nj8jCsD6WOIGC-vamIbv0qoo5WIBy_H-FgicSeK1EENUsV35AABk6bec6JimEvCFr__nVGaCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbvEpGcupbgeMfw33Cn2JGcQ8FepbcQrzV1_KoJH8ZcylxEZr5hU7SnYOnm5ncPUUgld1jldGCkvZGi8xvG1whiylQdzCDjgUEccFtOjVY-FKpqffx3YzXEOmOapXLzmhXxehDFdDRYzSi9Ef--NL6kpGHUr7ICw8Tp0pHTxCIcDCyvlZb0vHVdZ-vy9LTUifPFOiJre8UebVN06hQ23Yi2Dmb1jej7r7j-km8GIkXiMVMar8LKYtOh7YAIf4uffa03EHjKeJMqMMO5XgCbm5i6C9neA3CxDUJDMOM9BElpIlAyu1V6Tm7ajfEOJrx88bo7sqxtoOA_zbgh_W-sX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umRa_2Pej3BVjGSvb9ZoipTRcbCilyxzpO716Hv9K5rbjEg6LyGLtybbdaAKQZrNM8ApsK-dRRzPnEQ4PvYNhZPV8X4O6CuiYdj5vK8s4tbIQ_uP_HwdU8ZvtyVDMWAQ4pN_JYEfNQ5ybIVtQPhpKNl6oaR1X_xfjQnLpQt2XKdB2ubO6Re0vOQHz1Tr3z0LXGMUptnCjZcvM3_nsQVMfjXMoqXpKS6eRkjPWNt2T0uX1YCw3E0seHiEfqJKeaNPpNZvWzEqlEIm3h5mpnfIPl8DkVhCZ48qR_hG7-CENBIsLp1ubrfkJkCv0STkbh5ey3Mz9jFOwMNA6WDFlQwEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHMu7fX61CfepfU-t5Vp-n7o8LMAgzfuUhEir6NJlESPyr7tu2FZIgjYzVaZO7v6-BDoDJVifU75829rx7-iVFhGLQVA392ndxj45xNaHkDzMdVD4fiaOSgKHCSkHXQvyhffXckLeZn3zyQYP-cuCv03DSC9ySfAbM9mLXL8wq1dEkp01qXMABtBGGV8ielvrnaAHdTackqxPoyy4fEnTn5RaunLFLTVuMTcgGhTx70IZqCI6lgOvbPJ736k-BHwBDpV1u71vor-ycHDFyKIYLSXkqffERdojDtrPZs2YvaIkOar0GbhT2QAXfFHqadkhkbJoTu8uwVSBNKpebB7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_7wgY-_qETukaATAtgLVrZbjtJH09jcXMnyXlksYuUCXDdg2WEpXiMbTOCQHT3uCDmOX3sJUKVMs5WTIj3hfgImptKu5vZtsoKlU9bEp_SeLqdTGJof_U4ijtlqcBOtLnv8ypX1Lq6DVDb8vU_9d_eKWhTxizneQ2sSI8lp1t2LmPm14WVQ69miGPxl9On6W03VzQNCYY_ZstwP9ZOPpqEsoS1O-lmlsvC5m7atbZ1y8gi29EUlXHi5ehHYeZrrdivEwDJXb7I4xAl926_ZXEM8TnaQPw0Z2qqBM_ruPBcn5nAzkcaUSb6CM4M16lRlEaxEmMXqhLvCf-L-owcZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXfhtmNJt2FuRaOxizQ1AyZMivaQy3JytGh4_x0UwpYtkJuD8bTTcAKhU10CVkI6bMnml_OvWXgoo0zH0fZjEUojiI4a1XRfjnK8ITOLgc_zJejbaU2qFv48yXIse63iGC5heZ67AITNqY_DQir57bdb8JOpAMUipZfh4a276_z5jSwOK9bHe4x6PvMzvdWxsl0-2YSuWctheyvRt5-vgHDQofP4gAlvZvtQ1Wp2eG_Xept2_AZiT29eCGDUuiEfXDaYAXEa3-WDTVXXwUzX6nATO7BbC8upbmuGtQq5tgLGPYC69Ckngox21Ww6bnTS1kbFy6L_dd5SPakpAOBJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJWucyb86FHVXohSThoM-gfcGsKSSeb258PhX4HzV0dqvNTc2YE6pP-rJeDCQsJ-xmjta_f2u2K5v4BPwfPjYfQgafETBTjvgwsB9NmYPtoyyjtKFqYI1Hjq1z7SCXXqgRgXOWM8JpAizv9Vg3i1Su21cs3CUaxIRVJygF9MhDJxMoF37NYAMp7PMeWD7Y2ktn_CcWzUHFpPNzFv1ibhRBbA__YCRLYCfatIBJ5nUFB5Edx5W-x_Fd7jAXNLa2VfMltsYj81sICJHlS-C2aJVUYa57GgIWNmKZysG421SKr-8fzOiUXwlq2Z4RU4urr8rK0q6rQWdvUGVhIUudRfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro_UG42kCLSQrJAISeX95tCK450dERjNSnkEDF7N_pfgiHKUXCWrxBBJhcjW-gPNlDWHlEjkjCGLggEgCkZe5SkEeY2wNM8-jjEjvSEVuRFv2fzMOy94_9P4GVgDt6XihdfTl6EGabgqpLQKykEZKtcYARByWMCFgIePw852RaD-3pPxlc9hVrpnMTii5lg2njH1usR-vRyECMtIxv4ioPPu3GCGrAobCXg43X5I1ygrx_tj31YMnwsLeOUrFKUnX3ktvQvOmgM4xlwGrOUgcESqe_8_sqGr3FV4UrJWSZZ_H-6CcTB39KWunK3k06TKWRIW_3KBYQhyZMpYZMlRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0TEvQ5N0Hfweaq_pJHJZ-DVZfKnMUXr1JauzJ9hFInw5BRrHqMA2l0354V6-ZNnisREtAfDE4NJ6ib31pttZGBAkt1JQznZzrdt_5fykKlCxMIQNnDCWBtziFECMlv6IHE5JNVnLayv-6vcPsraEcXSIAVzPi0T0TRk6vDvbwEkhMaBE6Qkwn3n072gtNIuLlzpNIoRQ9rdMLwisVQIL4GyhQOWOYZbCq45J2_93x_wbE5-gcLpXPKuI2-tdbf1KIdg3Ha28rtxGoEOj2Aqhw7RbtKWN78MpaGxYiFYi1dldP8wiJaf50QuZP2YIXAENIadzB9QQ6tJYfFKpskDVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeRJaHhNEI-aNPro6KojD9mhRG5XsR1Q6kVlQZKpsZRtV73CVg5K3OJj1pQbqHBxj0PgDZYf5R3QS3GwexiwL8ZHgwLwAKc80ke90ldB-m0tMqIDB5J_xXolHBgqyfO9pCqeLYhMT-_NCiIiXYfFEZcKrK_aL1EJ2BrQMbPuJvgh9PUU2z0_4cCnsFSyhCzvq9FtjJAi7rndacnUuUKd5vgjh18JdA5SAf3R65XJEREL7F9ZNM1gcvH3Y1OYP79RQbUsVsJai4YF6BeJoUApE_zWYG2F0pAedHOuZ3J_ZCNjcjee37ACYuACrWZQhX0h--yz62V_9_Khi8n0Z2UN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✨
بنچمارک مدل Nano Banana 2.1 برای ساخت تصویر اومد
‏به گفتهٔ منابع خبری، گوگل نسخهٔ جدید مدل ساخت تصویرش رو بی‌سروصدا منتشر کرده.
💡
به ادعای گوگل، حالت Thinking توی اینفوگرافیک دقیق و حفظ چهرهٔ چند شخصیت از Nano Banana Pro بهتره
‏
⚠️
هنوز ممکنه چپ و راست رو قاطی کنه
‏
🐞
موقع ویرایش گاهی روی ژست تصویر اصلی گیر می‌کنه
‏
🔤
متن ریز یا خیلی طولانی تار درمیاد
‏این مدل روی Gemini 3.6 Flash ساخته شده. به گفتهٔ کاربران، توی اپ Gemini‏، گوگل AI Studio و API در دسترسه و به جستجوی گوگل، Ads‏، Flow و Stitch هم اضافه شده. به گفتهٔ گوگل دانشش تا مارس ۲۰۲۶ـه، ولی منبع می‌گه عملاً از ۲۰۲۶ چیز زیادی نمی‌دونه. گوگل هنوز پست رسمی براش منتشر نکرده، پس این جزئیات رو با احتیاط بخون.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2j0H02IIqIXJ5Mh6nVIa9nIQ99Qt_Cxbdyyrbgj8dmVdypQHGI0RGhE8Jc4XJcNab8iVI7Ptd4hIMljGytK5G_HI6HzaUBWbE_TM5H5FuePkYBpzD334tFRBjTHNavflqtc-p9IaMpXwOaMf8f1FI41AUynXjWTUhXiOsL9krppqrZ69eZSVIke5UYYlFC998B7cSYb9-Edy5vRNSKzXStfJ-Q-D3Rg2N4_E_IeR5Cup9GDCZs1qCIy4giMEypy_IYcf2W-MgvFZbDW_WBM5HwgVUz8hUUMvDiEYFQKaJlu0e59jSCl55Pq3KX_ZH_QSaxC5DlH16vyFELnHuJYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PyDg4HYwrm4A5yKgBONYTJ7TPxqfSlaM14lDJ7LycWCzWcjY-R2fs8VVZzED2DNdNa8qMn18BYdK2rFwilaWW5nW0SsKm2SL6-6TReoJast6vH3lqgFv_ve4eFX7CtZwbIU016nu7VFBco-qV4Qypvdh0jCmA8DxsYxKwn4kcaG_sjSmrQLBrUKvmXHyey8nFybMLB0Iw04f0N3vOS1-2JXQdVwQ4E02d_8pjwmphvTRJmEPBgvr01zRH9OVY4t2XTeWLVwf_iNpydsNR6MVnXrX7BxH4S4Jg0lzIfJbuP5dAKYLLo1E2VxHn9VDDdMhj3-apq3rl2VjLVICvjGy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚖️
وقتی هوش مصنوعی خاطراتت را لو می‌دهد
‏
یه زن تو فلوریدا به Claude می‌گه می‌خواد به دفتر کلانتر حمله کنه؛ فرداش پلیس در خونه‌شه.
⠀
‏کارلی میشل هلر، ۳۰ ساله از فلوریدا، ۲۶ سپتامبر توی چت با Claude نوشته بود می‌خواد به دفتر کلانتر «حمله» کنه؛ فرداش هم نوشته یه اسلحه‌ی جدید خریده. خودش به پلیس گفته از Claude «مثل دفترچه‌ی خاطرات» استفاده می‌کرده.
‏فیلترهای امنیتی Anthropic چت رو پرچم‌دار کردن و بازبین‌های انسانی خودشون به پلیس زنگ زدن؛ زن بدون مقاومت دستگیر و به اتهام «تهدید کتبی خشونت‌آمیز» متهم شد (تو فلوریدا تا ۱۵ سال زندان داره). نکته‌ی مهم: چت‌های پرچم‌دار ممکنه توسط انسان خونده بشن و سیاست Anthropic اجازه‌ی اشتراک اطلاعات با پلیس رو توی شرایط اضطراری می‌ده.
⠀
‏
📌
گزارش Cybernews
‏
🌐
گزارش TechSpot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seVgSXLo2uG_XiHSRdundeeGRXUjhiNDr80Tei1qvQt_UfK5PXVr9ipaPSFXKU8danIvRgWULN-1YA7RDpoyjd_dkneCzoMR6pcP4BZh_ikd7ZWz7N82iP8fuV8uLU0blRrq7K8g2pklKQ5oglZQYhmllvKf2rafNKStT1xZuJ0Sbw0flZsrRkfpyX7YY0OzsxJBkCpUl2EAAH4UzDdMx2OP_f4n4E5UOfNrscisLEPOnzINOHCBn4MTcFcGUOO0giruRRa-jxmug2UFOMK8_Vgr_rZmtGx-DPXsUVHgVpKZMBcPbvnNqItyThGSawwYFiXa7optn5Lh1ncqU2c6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=lRgqT9XGV40fAy2KZiK586fonF_bkPucPCBSNz0y1x5jraLdhYIKn0IDwCnPyogkatdNIjqIHRNkvoC4qw9kWArB5JL3P5apVdA0wIugElhmWO6zUxkzHw_WizxGaLMFslh4wKcCdnf0D2Rxj_4nxmO9ZGVvedBD7t3fUdh1A_1MEg-rEXZdUuntzYQAaKACejU-6p5sgY64wls7w5qxTgO17FAQtNTq63TlqvnO4NaWQ1QPHW_8H6kfJ0gbuDr7wFuZ8WDVtqHiGRoqtbuvbArCfSs27aJfWC38Vjl0va9zQ8uZui5qy-3kBQtZXY96NCbsbLDsoYqSw1nzwLNtTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=lRgqT9XGV40fAy2KZiK586fonF_bkPucPCBSNz0y1x5jraLdhYIKn0IDwCnPyogkatdNIjqIHRNkvoC4qw9kWArB5JL3P5apVdA0wIugElhmWO6zUxkzHw_WizxGaLMFslh4wKcCdnf0D2Rxj_4nxmO9ZGVvedBD7t3fUdh1A_1MEg-rEXZdUuntzYQAaKACejU-6p5sgY64wls7w5qxTgO17FAQtNTq63TlqvnO4NaWQ1QPHW_8H6kfJ0gbuDr7wFuZ8WDVtqHiGRoqtbuvbArCfSs27aJfWC38Vjl0va9zQ8uZui5qy-3kBQtZXY96NCbsbLDsoYqSw1nzwLNtTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnZr6ugK2vWogjWpt5j2yU4-ncmR6TWzwqwnVRtCoueOzSA2g5XuhGMtU8enqMr29JB995KriNoXRnlSmL4h0XnJ2AGsFOgHbJZtn2AbT13pF5hrzu6W-0ElE84rifnBmMGmWU4rkc_mkyfce3YIHxj6BcRQMOj1cTZ2iHgMnYCPW8xwZ_8LCZ8AjstiQyUDKZW-G2NjDMYewzw4Kf3v3un7qO-ZzKwYEK9EdIOhNVryX-43WvC90sVens6Ye646VxCsi9VpewRtmeB_cdaOfzE6_u_eX1wR13JsJV2xRh3vKLUVjkLP1Im6dzlEdXupiepCoB1DRnE3-IQmAyJo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxcCNzwvt909rMfiZeQjTrXi35Yz2GtC3MceH__dNjmb5zSOINavkHNdh7rdWlGUwOkamJ50d_TIabfhEwlPDSmxTBfxdIsc7col6j72D7doe4ojaRMDQVYWfdgJGZf45mbvo4XfyiuwbGMvz29XV9OqavvaL8IePRs-8KZ4PPmDgCNt_uOo8DPbhk-z2t0skMLAQnKyvfcd01xDCaNYLHzeKhxSztvo732tQFe0kdAzR1LRw9wy_D_28ZQkziCny5m2hHo_MFHnPwF6AxFdPJjGYKX5700KVU6E6_BTLG0O9vntCl9LjwQbuixF7L4ivSMZfWXXfuxWSL3MHu_SnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chglxTXKyAyOt5_vXv_Sn5pPzQnE1h2sPC3UQ3d9PFEuMrNvknD_j71d7ntPWHuLXgANmD3RxN3yuZ50GhU1lJoMVpy2-6cJtF8YG5vz8CkBMWqmm6uhXPjq5h9ptNQfqcJ73qr0E9fn26vGI5MfiF_CgXtug9XXFjhh0oX7WoQQ7flGGQ3xMmLuPEMJ-s9hSfSoyKtjkMK1z09BGb7VSxV8crEocW9ZvUQz9zXlW40QVDU42gO4NgaOHsO60o7h-Nr3MXtzD4eg8EFxjDeQTV4B5dbdVScLjRtoTeqfIQZSfYAwgs9URfIBa-J-noaz9IHsivs3lva8tDY3tEcCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arzo15KCUbTqG79sV80DK4r5UhQu8BMDWQff5eYmjqgfrNjxvGh1minrVoVqg3XAGBykw4i-Lc_ARr4T6tPuoji_e82qVqiJLyoYJWnCsWuyqBVTLiAQ59ZqhlhuZCMTQZ_yNYQWYNFAd5woiRzaTq258w2CRHgWSGBQB6mjTUjrO_EyqzSHgSNnuiugbLzTywtd-rBxNQCIzzi45m4I0dHUHoKyFGnIpL_KSPLiSvQ7zFw8a4K7KqF3Ufdxz-gllXa5vnM5vz-IBvUKtLFB1T7RpGo2JC7iV42CcubgZE3VBsUl-RBlhOb4Vx6yIM9lh8AVaad-ntVqMaCWQeMRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEKLqMFK5TqhXqK-Rj9E3k7e8eQB1yYsIfc5hVJjdvOQnxxezUudqjldjR_7oA1D0nRv3TMWgN45C8iVGj5MMam84YBmuQdaSYu12Un87yspNTxggyiAuXxR_pby9KZwIXKcXHz-PJc_obyg0xeLmHMWUMt8ZHVhtlA_CHl6uihnjdbD7DlHtAVT3U1AA29jPoYbrQym2Mq2RzF7Pndb5e-uU7WLsWihc2QCeS6PxBOjOK475aoPmf5bezPD2S3S0lXaHyKa0266tDP1PoauSuvFaq8m640TLM5QHV1HnaZR8xi-mWbQyqdC3ZwdpzTwqIuFo18DwPNRyk8mwFOnWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBLjpTmW8yIYZd8PIhSaiKTdBUTl11_Y405s3uxmRQKgACqQG4-jJCnHGzPiDrOd9N6rkzYzwuhXkjb-HXeYTm6EUBGcNJX_zZ8XmGkE1_z51XgAAW_Lwp_R1pJJQ7nR_PYUKW0t9RySOblx2OqbEVNHxrwKhsIwZqf0SuOE7zM_3OONZoNbdfEZzEwU6fEVvRPUzsYGPxmNmys5mgvz9eFA2sskPToXn_DmvqGzLNdNEqeGCWZkEmzjNuwzF4k8WpnFMYdmhuChH6CpV3ZZeu05Qao1JtgNCccy1tuzbNrLiSyXugcaE8r_yWuYaXkekmi-AN2HtowHmr2uec0fXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urj0opx1vhAat6hAgIdsXOMr78L_MW9exi8yE_kI5jfdJn5pzPupNxSDqckOHfYegiH3bB3sVY5UW4ULKrRhtQG7NnVxfv9FAh7mwk08SgjsySUrz9Dqoq6WFWB_aWa8H8danEBCCR_p_vrr89IGDVTn72uRu4_dTpSCJxJKd0J3KCX0bIhO0cTN3VzviubkRigpPgK5XMYEEVP3RMvW_i5sTFm725jlSGrfaxhiGSv2KHGFv1AHmAF7hDE6ypgBourt6FC2HeKrN4_fFqwzg6plL4fDFfRprx8GGrSuKfnpVJXq7VpKWpXx5jajfB9DBm6zBOyDGL_T3uZ5TY8l_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RMKS8roDuCTFQ_PIJS_oXV9I-y9Lp73q0CycbvM1z920dX3BsyRsZX0SopOD5KmiYbfyMkk0H7nBVJpCfRieVm2xHjBY7HQrvjVJEe3ikBnXsoimPxxnqp5Is20yAqY_m8LbigUMqRIqBZBvknP3xfLQBOoiB_iDh1hGkRNKEB-up6-ad9vuJvDaIx_igKfbXCryKftDEUQOEsxbGHwDIdqchZNWnIjwGG1XGnxXPf2U64qUKwINQr-V_-TPxZ3TaJFnrnR8vaIZ9vifVtS-0lUf6Mk6EVCITahoeId0iBKa40X9XdP1sl7xD7zayK1e1lCYNRsKV2mVDytlGpFZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nz6d21_zuv9EJHt0Imixs2JLnzSUlhfjm4fuLh6MdM2H-2L978f2H2o5Jyj-6TBp4VbzdxY6mDE79PNHDUqqnGVLmqZDmaHObZXX8Fqq0JdTjPb4HV4zHriOhzP7R7rFRIEGhepCpbj9OrfzaZRmHIfgTt7vNo5o26uwcDEDZknlpjIeXk77mSioxqv767pcvxxQd9vvaDgssH2GYUa-n8Swjo5htOxiZh8LSARd94xLeb5ZDLbKgg8Ak06qSlyBoUDTU30kHEvdT7P_inwTaOfYBX9j9yvWjA58GnAZIGKuQuuOOzREX06-xbppIFWq6S8cWTvBj_UvbTMXMg_2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL80CJNY8VMdoJq4LTu70GzGkYvlNp2IZU7be_WZ6-vFdH4MmaRush8i6bZedUqzSD6eDNsC0Wu71NVZjmDZfQpV8PKlskirB_hl_m7j57CRxTcxbYAjl7orLaTP7B1qFwypdATt0Mr5NoB7JYPG78psP55SdiW-aera8BsgMfFNkKMuqZgiFTOYQF_fu9tWytEjwtzy4UgJkkMYAsqLe1bB6xONh6rHKsHyPRN7KdfUNPFPQlW_doMeqUktSKhUdcrbyzcLpdyxnOw5tw7jbCz1MX7z0O3WfCxireYfzcBFRGUjlBDGPWHSwcUUQHfxxlajXq6F4t-6DJUhJT-Cvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ZqDe-8Ftam8ux-e2LxoYOSlHsTdWPMS-Si1Y89DL7EitjaJd6Ig2hhIwhnJm4WLuOhEYqz20Fh229RSwh5-LWVlAJ_2TezSNGIIIbJzIKgoo-IdEvKd74wVmJsRjLeFXZOLCxMu6jwbL240KlskEVKkB0Q8cWvU4h71R2MMwutBXTTgWgVIcfeCqxU9oKHigw3iRLPIfdds8a-WlLHdeXM_jDbLlztpzw7iTXD64mU9sbIqcr2qNtOHCe6UCHD9idnvojApD_vWTnJG_s8zJbtsrEg2XIy-YKaSa1L5mNCu8xY4zAl50uGsS36EppbFp728n9C-ckdgLFSVQ3ILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFAI2kbGeiFWtQO6wDFDgMFHKt7sgCe3JFBz7NYaM0YiKtdyyROzN60u90SWeEJC-472miimDogPw-PIPJnw4tC9CzyWPAIh3-91MmpOpTmuZYiFrem44Ulk1ftW3oaHpYSuawQmP0h8EnE9nLdr4wOk-jRh-dGQEycBZ06K-s_oo40ZI9MlRO9C9z5gqLSjD4bWgN8RrKJRKb543cTXwhaa-0rkdsFQU-tm5nCY1UhDq99igoG2dX6Dmqfez9x0iHXNNnmMtPVz1L6zn3RC8OcOWJSXsapcMjCy8TSdC70TE8d61BSy7lo30aYJLj26W7W727ZfbQ13vaFHiRMnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIfk5QITMKpu1pdpH5rIrvgnAzeH4eLUDshm7wuxCU4OmKgVq0Yb7lhsJLbiorc2sWtgJVUQXe0fMALnom6AsnbQSjeSjqY0J9MWeyfq5kh72Oj2yPMZ6nPnHlCImpX96nlx-XY-g7akL4a98N9Kly6aQP6KvA8fl4RBEkM-D68HUES9d67F50MhDDyjAF_lTR9f1oj9hd3wmhNPi3bTgizwhWUfYR-Wr2siwycFMpTwfGeE-JD_evLiW6D4ETEXa9Z1VCRF7uE3h5CRTAwRC0Zp3iVTGe8sd9X43d7j3NXyQIUAF13rBRhE1sDeF7C4amy1B2oT3nb4nOpSlA6yyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCicVC5qAgpte4CEFA1cR1HVAjKYvkUWb1AdNnZaq53XQxRyWvOp8i2OYxV5KMFL8Dimew1ezgOHexR1-e3bPQDcv0PYsgjLYk26jxpct3FxOXJVAEjvKTcXf2-ThwjWPu7zHVtJab9YD-guVhXtZ-qlBuXJo0lSF7chwVXsKk-wOZibn-y-xshl9iqGyXJScOWf8B1T0AtOoPk5uhCUaGQwondNZxH2MZE6RfQCa_F-8c1L5DlC9plOLTpBBzid-IlHaEkZy3Su5OpDAwGxA8LXpIAlzgOSjfprPEiSm-xgxxoBwzK8yu0RPzOefkdGIMJz33EVj6bU_1wEYXw0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxzYn54im8mU2FVsZ-hiizKxseTeg77dLWmTVPbLAPxFhOKxXaZkqtsIBux59foDJAozUywEeuqf6mO6S363V_XbjRmIlAO6TZNYG14bKCOTC1IR3h82iPG7r4ve-C6KePSvIWRWk06AdUTw3t8zCxF6_H7MNyH0vOxo9v4vgoR_qX5ZeswYPUth28cIrAxUShJjgynmYPoget9AzWH2mh0PfPGxyc7vXcbylhxG7_xd2E0d3JKUpKZAtBBwIo5je0nLoH-pmzBcgjTM_SKUmg7FrilAM4SH5-Nxy-Pwa3EXNTUPChpXs_xiBXav_u1W6U4e6VcIzceb7OGHa1xrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZScCmiVF8Kjo_BqdVa_Dgg2ZzQvgMrxMY_vlYp2olmqyXkSvwtWJfdgWnvt07BcqpFRsA-pBRHwcAwJIAx99BC5YRuJ9_qlmDOL7nXihvXL8lb2pmXTbmX_GU2HZWWIW2ev1GMzjmtaEoDE3Okj_vW8-S81Tx_2bzq_5f6-GhG2j73lUr2qPYtD5yTu8xnRvv_r6aWAVF8EQ8AWxA0Mi8W2evlaRkh-t5_eW0D_hq82k_2cw8lr_JM8jtn-tdTG1JtNi_LhmGDsY5m3BKlUQDi88PipvtnNaTDLDI09zEMjK4TU4AywIpqac3OahA3ttsCYtvjbgwfLTjwlcwyYTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf-pVwuulrL6FXUtpUe9PlZ4qV_RvHafIv2E18-0WLa4OOWewJmdzC0ph3TACkFSB_rHRmk_wEmEr2dSEchvioCnvFs2tLbHipbTlLb6K9nFi7_wZ2ceMDIY6yFjBEJHXMo1M56i4ja4miH--eed71bLBDWuhh7OT9E3a-GVdhLdi0nQDJytQEbyHQ3rxQGl0i-TCZPfVu_ftoFJ0Yju8RdZDukE81XhRQJEhCYM_BJoWTAXSLTySxmKI3RK8QrBTkx-x6KQ1zAqQ48HMJEvEkLPGtxodlT-p8ZX8vFlVU_IzoRf81m_DtYQzi3Jcm3gX-sDNBQjOOZh2067-c2cuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU05lTg5I781uCdnMtWgeSt-J_GkThunqTZNFDz4sHA-HUpO5UzUZUjQ1O1gYYyY-aJS3FlApLkvY47k3dEMDjK8pH3fiX_Mu2T3zPg_q0FW3dNXYEGl4nRfeKeO-YVRslYzF3FmZu3T06Iv0eYPDwcC6lALps2aWv7UtwU5KHkSEk4BLOcqGj1z41Wgwacffp-q4uhYMrItKA5-u3XIYl8dJZohKKOgXd8ee_zG5hKv1zaTBWC7O0Y8PBGE5f9DCQP6q6vwL3wuVD7QLo1qIYYBDVb3myPQyLQDXmpX4oiCNTASBLKYXEuLsXc3gDlrdLOMDDnYRfNxaKHlpR7h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAUdXzeigAWkA1Kmw2HSV6Z30JNTOnsJ2sLbsqT7Aj_iEKuj7r9sAX7L7KYMzXuZFG-7f_W5XxgMnQJz40vPYGnOsOED6WViM3gIAMKU5JDI7rrhz8x15DRH926D8Iwhmj3wOs5e4wLqtCozmWoZYOr4mqHF3GCW79brzpjTYsW-yi9Lz-3i_EeaRQn_NKUThkuL6RBDUNvgwUXOTQP8LOqu2YnKobM0DhKIJDrLbpNs6J1kJd1QJl3jVkIcnlfk03ZRTUnlA8XJ9ev0xZf5EwaumGYkP94U71hfxpcNTD7Yzhc1oVkoafvCDJzzYNnvi04GGw3L0eS1nGdCTtZn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWDY7McBoCxf32Qhr9nR7wIqoIGDXFbIoHffZ-NCDE1et0k2PH_lEvETJzzzxW0QX8LCuw-5AnOXHwKQMSoYj7EfxzRUpDsQ51afiuPvNxMO_gkesavFU9gr6d40lj56ayqefaqsfeUKuiGb85hV33xALA3bIfAhPbBQqANLgiSqJhbyL9spkJ5lI1ynwbCLqrOPc2hlY-ySKL6Srqu3cfnplr6mYl-KUochLuJIwG0LMterg9a81finyBPeIN4l6A-vqnEwZr76MTaDLjb5BJBytYeBfsEsI_OJJFal0VYpeVj4bVl9Nc6KDctRRMU2mAdD6nzSufzsqhBVTtbBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIprCn2WTTt5a6wLKqvedvCUUHSbFKJlw76ptGS9UXTvQhFzRJu5gfK2t67zuM5e4ZcydYBkYoXEWedyc2cMPDcbZHbFWpAfl_oI9KCUh_3skkI7Ec7_AVA6cLZmGoHbV9E-lfJe557uBCaMbtb9GaCsbV_r3_W3FYTKX8MTw6qRasijXCTRw0Hc4uIIA7wKbJX35LrnJHBF-FeCKq30LeuZsbpjOgGcYL6JGmktq4gLhOVliOO_plCQVrjtcWnjTuXsFUSG6Cqk7Vud1UjprsJniR_xhddqUTA5aEVwS8uA5QappbA5LTV1gC-tkTUB1Xjd6rlGxjieNOM-w5sgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe6bVGWEl7IMbWw9zC2Q6C6z3GIBdYmn68RUIIM-wUPLxUGMS1MOKVXVSPMpzbpDmaW4MnAzPcYFUg0Eip80U38BfaqXWu3gvYkO3azJXLPAc38cXTCQ4AsjjimaWiKCv_N3gl5kxTElkbunD5uuECupfXTqN2TVgxRFxYc0dT_6bamn_IZFKkoJUe46qY5qHsYbtQzgOnS5y_HOreolWVfTgmUJOSQXkKaxAaae4BxEYGAV79-Kcn2ZC39-1Softqc2S933oyaYHLGNxJ4EUIKdz2yNgJ19s8zLoSWmXF-lgr8QRn2xP9ui33dCDPxOacj_6N37Y0OdpAA0ZzJNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJLGiULS_5dc89YBl1IsibY2xPiFaa4XsEIN-HLSpRhVGmlKVYFE19GQkbQlBt3CcdJttuTfNLmryK7a-_Y5nWuw6gp5ZIiXabXfuKQh3gXMinPalbYi8xgYIDphlRocHDvLn0HsCGVHLMUdta9vf1U9J0NtUzoUtTc1MAN06wLkyBayYl0L5eK8gS-PKDdJogdRw8fHdZGRX2hz1JERvx51cBluymxTO4_f_wu5EsKDI-5AGSZBFR5xOc-k4mv_Q5AVjQ1ztdAbyiA-yrgPsvHy08kKbobZlt3f89r5OvtYi_-7pTpzKyFQaRMKtOWXr4F1xgNBHETgcxBT8oZYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKJfpWtnx9SAllg7GCoNYRmKidsLpJRhZI26_LE7TdjgpLlkaF5zzEF8F25riFlXZFIIs6WC3iS8-LHrVOEhEZIFZ2KPqY3CoK0Q605w6rYwk_C7Rm-36Bsz-uDLEaQVtFI_Y1fS7G5TzM3s2VxVDqpuLyyDh4QOsLA-3Vldhl2Hx0KpMBAofvxYAH4It5JyXP0fzliJvl8Ke06klFBqUToWPvV3GqMN2XUZ-RVsVrUzcALQIArVlnLyDUmA9x-PRKXmHPcKA-vWe7_GVfgfG6fd0AN58HpNM3MdLl7i3_Un8tIbuAjmU9d5nQ4ejFWiYM40gzZMqfME7NpkLx-bNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ07HlvUSKZfT0SEvPkGtwfQLJhxKN-buAT7EGr8wo4dxtx-OfORkN32itnuvguRbssNn9ZpFqA5gIpxYu9F5U63XdPEN_Z5ATcE2V9bPi0R1jJ8PBXn2uGsQhqUKZxR0OyJ_AJDBT2nN-UK-MnkDFgLBRb_ORr3XY-MYosZhWxhM8ifRy2vA0AWHJkAb8GXOUZH_TBL4IaQpzYGfH2fHki-t3jxSDoQoPkhThrhn6xEkZk6UQWbUF_l5_l_DkwqIWC1a5Q10lEda1bkasjcKDVYefZXbqoeXiEMFLVPKmng3FiMwBrxnmh57WFSAoLq9gezgGv4GaNms8uVLeZUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diAMyGW7UYSUPIJzAckMLqbTrWO3Sh53cToJtz9Ul50VNo-WvleDY5_Lit24kvuWnUVW032t1pub4sB3x8Se5sDHYlY7FjVwa7z14M7ji37z5vuF7abg0HQTrmCKroD0EP_6cXFCmLlyMvgvqnuiMa_Nq4tRdDmrCBV9eFfJKVFKJ8j0CZggFUH3l1CfUYuQJyw9TKaaXpgi_RtDf3Q51JXLJ-p1h9EXDp4Tl7GpV3gY3M5-s5ZN39aIa5iOTrRebkSp39wSjwnJE0wjroYBrjL_wVxRsjZd9lJ1IhOQ8FUio3djM0xc7oxQmAX4oZp7Ahs9oNhz1s5LGap68hRK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXYZJarwj9NBXPTiHCEzMAjuOSsKSE07HI40mHNW5jy1hQPz4E8NzxmBrvSlGlHS8EjCSjgyIKSHnE2cuiLBaZ9TQQiRCYNyJXaZChduIOe1S508Td2eXndeH_LL7B5b3OC_A4qUQbR3a9ETgyC6YqD0gMw4_w7YcC-OvSolqG5kPJK4EwXPI66z-XQXPxO9wBt-GSEjA8gyxnbQfImkIh9yHRUlP4rAulBZ4UOMo-yXEsLhNdDAr9Ny5eN07H721neEtbX4o_OM_9zli6S6aESi46PTgfcFlckWLbUrNjHJ04JkTsAJIiRnT6cDS-psmqnwZ6HS0NC3SM1li2ccJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQRSINGKQy4kCgv1tjVsJXpS37bk7_iftgnYCybK0w_T7qmIMB78wV2UO1e0cbGBbEDFRPF0dOtcdxdZ29G-Ec091xl0r91DyQA7H4M9R4tuDqhdRI4JwXycRmN43R8NwroA9nJprpk6-LHCQBcRPD6R8qTN-wzs6QGpb3tnIGKNg1OvKBrd-tmH2u7d8w9KLm_nWfVTSIkkGDpFZZ4xTgrLs9xyqOaHoZMdy87mUsd3J3bt--8ig9_MRiRWDMOQFcVWe1fT3LgmcfIJqYbbdl8wdoUiXoX3TBc3q814xC1n2Czxspavmy-0SMvULNh4RpePbZbuJbps6170fAhT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKkCH3AjZEHOSGZISqTkToqWnnaOkGLJQS44kgxMfI6dBde-MzlRpRB5qfREXy6aSKqEa7k6-YHvxuwOtMPMDqitnHnJUG8fvHh4VUGUiQccfIJIVdVlzaxTp6S0Rm6PG5m7rEusTRS8nJyfzUrxP8yc_6t4NK1WquClFeL4KiFYoOAfKax_couAfVdZTEIXFHZEEyCl-JLu9gDoyGY41tss7TRRKIcou3-5xkl3Atm87Z-YMLNujW8YgZIMcxmRe47k7iw6nIGNJ8nydOKQVwUX7f_F1RPbLSTS9DknPvxO6WzjwHuvbzV1qbqvMR_6WcZvUo4s7QgveWGXVpJDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk-J8CmpcgWn8jYvI4w-edkJ-xFhq55mTLiMDAVYdTZbQuEP0kSzY8ksNbN59rXG_GQO1eOXyUpVTfmc2A-g8SGSG7sqUEQDEJc-IdQLgEzjhMTLlxS6QnAXkc4pjH-1rj3cJ7AqeIo3faTeR8VblV8SJLPIgfDSbH5gHAfi-O7LkBwDTrDC27TTqLq2VlMpK3ZnGQ9_3Rn7Kfl0FtTUpOWB4xCLMXFx2s1Z89gW6XRwdLN9sKuCGSUflvVIwN4YrF0ZM_UrxTTY521WpS0DlVFzjqo0hiQMz_Ev3KPPjZAM-2s6otZNAf9eG1RihRgg7uBHNj34elisIBK0xphmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr-CaIRgiAqEygmf8d_7CWTUKfiWR3ZzE96nadUzaPJUqTycoR24xKwgKm2GZviOkQ87-UrkQECsUsgbrXvdlFf_hYTxoY_lcHi8hbDMXJyFj_ljDHS7diYr9NYuU5Xoz0dynHpsDJOoITcW_ypTY8OhiihXga2oP6VnEGDPZTu4yaKs-yUscTLwgS9VkP64ya0k24cCur_unWnJIolUN3XwyQCFH96xnUP-Pc77q7u0G3bVCjkBjoMbGwv0y5HLCaURkyt36PqwAg0LFhmTfPiA7hXlLas7SR2uI77kDaJx1cjH7LqZQRTXd2wwpS2A4cWamBspWUXGz8KTIABxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV9pGGCRC8nGQL6crfRUHDVMbkz9lzNmWpkc28AmudK1LAb8Gp9uE77WcIq8AE_7zlLYfzgjRhKKEOAt6wezC_CDH9n3V6UIWrJWtqm59hz7jZEOWjjHtabbKOedAfkRcI8eX8fIT0rwFpZrlnGSAFaBZUWWFTvGNxaROSMyIWDrwRpGQAAC7Ni6EhHGsaOH7ic6m4H6IcRh7G1xnMpAg9QXIUyjQAFKnCXB8Bq6pD2vxVzFiM5_gnJIn8rLp6-U0pkTTo3YH5VCCFt7uAJ1AHmtijzmOKF8wWcvFTuIfF25LmW-Dg8UhO16q3bQUOgnbLSFZKaXcVYH3gtiyo-Z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxvjWVb8ruJXJkxeSK3n2V0bBGgniglu_VssdHQkJi4nAvPECT7USEZJ3RNvyBa4YImYnzxklC_XJ54tAEU6c1_MaNAV5pp_dzZg0jzR1Q78nWdAQuR2pZMdPAcXNx4x_ety7ISaFBe_WNJA3tYdPpNeYIX-HhKXfoRGe7-q8msIhWmXZHjcRatuIOiJc8woH5XDShdF4hbrNFU1ziAcqQSxahnZiAVGS0dYL1Ang4A42EEkNrEsflXFtegce74_Kp614YcFzejJa7IsHc8m2rYlUXQcxOzW7JtIyAmsrP-noSTndNN3mh1BZJB6ELsx6jGyBWQHD9E__UrbARlgtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCGxfZIsUtkXtzLAD6oQhlxSvYJ3dO-Vfnojxk0wpUMKksnsZ7RyGIAYvluSxasIlSy-EV4-goIcn7_BoYgAepOwWznm5Pk7wnLvveozyEgiPGlQLZGUFvMppwxlYxcZ38Q0S9NJ-espDWdaQ26vczwnN4kI_nLgS7SBkIbYHRwJfsM115lPOOhYnhWTFvhzw7sNYDf7bu4IES4ITCRzwcsePPZsiz2UmfhcGVpzddnkxEHF-Du1bTqqvMyCvM7E_SUlIe8cG-feqPPkRnE_gJiolZ6B-eEnjHHfDYTE1drVFJkHW2Qd5_9vDe1ysDnO8Lt7QbQ_SCm4wFg3G8m8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEhDVU6NdEyQbtPRL5nvan7HjcdVL0y3bCgY66Xn4l2g6UxYnoWcmKLslia21oxXyCQsD_L9M15YrXY1zB1eVSUqNjkk7UNx_bQril18BsfhcytADXuP7SmkhcHnInr4HDpW9GE-Xvq0bNsGYSZj4XmHU-FeTrKjrL4JtVleionGjuoHB4lUKa4Sn7AF9uJSj6u1VlU6KD7hQyy-qtDTTHA6kuqsLCyQ9Lrs3110o9ufAaKBPhKyElFpMV9HqswRlzMX5s3PG__wQcpnomaTzSvDaVJ3dulW5U8QreD_iFm-Nc4tDJecfSDRBlC3BY7mYbRaW2BGSDTBFEHJ-hlIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmkCDwgi_-FAL4NOZKx3yPUOSITcpBh1sR0Z8rCtvqc9lqC7UYwChRjez9_w4HF7rqtQCBgLnOKirWMhF3MWxmQwerG5QwRYAYoI83hZIFJjC_LWAu-lSLovnmN2WbKBM8y7ejvoVrntlLo-f8ZDwGo8JgXhsc04JYDoR3qnfj2k1H7UAbjBTzAvi1urOCNXMhMLceFfzQmr0xlYNWoQ4Bwn7xJS8yGAcHx93l6pmy65expdp6U4OXGl66im4v5EfPusWiyOZtlMH1_7skiOH3j_gewckGP1PikNcHIWMxA2oohxvNKkuSHLKZ_cGIuzSMdP_o3Wtu1tfYQpgQl9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF7aCqcGKJ3wHVyuva2jbP_Eob1MsSefdR5GIH35_hc2jzDduK5sgtDmh-sUN38OnzdrCLBLxyQo4uzo2Y7QBM0RAsBJ5E46Gooh55U2_Sfa-8v20EwIAQTrYAMT9xxI97Bxf_-Vtf905zS87YskI1ApWG5vuPQTKgnU5i_6VLvmaIpQhReZRH_ksFnIROakR-E0wbSFMKsFspU4XfdCMumFVZnR-GkHkHlKWZ3m1g0hsB3rKvifNBBrzM9WrOE3wnY3Nd3xOXVzZtUKeW0v-6MMVy3BLS27dM8nX__g3HZydC0XCNwDebuyiv6h4-Zo9pG_KoEAZuFUOGlzn-4cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFI6_ytj9dUQ3ALM23PXotzXMf5Wz0eEJFSEyUcxIw0s7VyPbyE6ZdXCAi6ytIwoxsN5SupktZn2gGH5iPWxq1dOF-hGRv2eB5yNNC8jtkCOMJooYKy3A8N80xs-yBfrIDkXoWjSaYrdrPdcR8O5EwEt3I7wWGTI2tnUpgLKXWE2zjZuW8e8cnIgZk7GWzz--8aE8wa_YnisAMVYNBxWhBn88aVDiZqwOwCftEIMlHR8_KyYjTBX7220p8ZTfvb-9n83pwY1KdDoHPhihRkKqro480ecCqvNr70i4y0gjY8CIS--_34W5tPV_ipIehHI2N3wMrsopcvfaWInJ3QSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZ1c8dPfdrIjg_P8Ywtu4Jwt0pgOF051yAzYcTl0kI4usWgVFtHplrNMe2o4W0taoCkx8OsRQ2OzgWDPkA_6Fja2doIdXqJdyz0THkLIdFQjVhgXJw--Eee_jzuWZRHHWT1uu22F0ZgpcIA3sHuS3dvh3tWkTBJfRNAumMthAsRWH-I5zIpoRbLgE-FTf6Dgq12SujCXeKgY-ERLKOIyaEqYwAxkqL3Dddq4hBZSCtUE8ELo-m8RVGP_uIXtbnsVpD4pIAfJvadQyG1siM5BtC2-gRZh4AvxHubAnUE-VwlYVTbmP0OuCZDX5YuQE-fWRr93sx9g_hFv5FUkstrDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7KDHj3yTZlZPaozHaUgd2FhHtllcgc4gElp_gQp2CMN5S11uMTov046TOoQT3_9BjO9bzSAmE7h7spCeuvRHwVtSvBpCCgZ-CDMN9vtPSINGLoiKxDFv_kZ-Ej3tYX2ezren6b2IdFMTONYM0P5zzPKTueRYoDbihHWOeuxrnwuF1Tkt6DyJNh_lDHcXQs_w0-rddcpEQ2zIiBSF49WGYs-z8RpX6G_67l02J0zfcymja0FJeLBv_l_XhgzcDbiNDPXnmuTR56LofEZlXx8jE8EkpcXmkyc6NGka9yo1rvUQOGXUeHvDy05uoG4nw4rHBHsw4v9Vpu4X4ji8qLO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf1TnTUkuwSjgf_kwO-wEhDrPf7p40L5HmVp7_LX8O0MluNKURTaiLe1RvR1GAdyyE6PgfQ_cv3gz9s0-xXIJxC6kWSDMZq3V024LdyiIiE-yG-hBaDdkuoKK7avS1NqgO46mb3PvYx_Yq0IPrJvhYBp3ppyy0HmicHqaGr2BRAos2aMXBWed4loNTr3NdnGc6vV3rS7wFdVSI40I-XFtLGxE2H0y1pspdJz14XHc0XgsG3idtv-ypllCg0IZyiKzfWUchXuHLPUzYCTTPLU-AQ7CO6GM2vL6CQvfDpQz_nt0vvFbUM0Z3CCxYn5LoEGmfI7Oxke5gUVLISUFr_IAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0lnhrzuILleudywBoeBoTNzDFFnR8ulLd-foHv3kzw7i8-CD0KJ04c8jt-A1O6NfDmkbXHnWcY6G7xYpgJkTf-Ppl52Rt8n0y-yXBQICSaecuKLMmF-SjkdqIeCGlQG84j92e06ohhACVLyjXjq4AJAz5Aitz_b5LUmONSvNa93JtESPHkOSnmwKfzNNWbeJyBruchWu31VG8qqG-1b45DWJBCzOrKkzlALYJIb2U5bGKiR190y2ke4JPN0jip1oV2bb2Geng9cS-3koC1WB84GqmfKugi_9RYznUaxR-kk3lSQ5N0feV5AGqtQtL1nVebRgj6RGtdQUPbLiGj6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RIsnvGsPJxQacgzmCXwVnC8l4RHJJLMAXKEveS9YTaNXQ_RD91hBkt34ljSzImYKRUcfbByEpzJPYc270e3bxOpOLNlJ4Bf0jb-mg4fcvKNqAqCpzMS1CZjbM8sVNVF7ApzisLSDWLWaTArXrmUMvQDhDkgJ-tivnGVjjhIz8A3BPbFzRomdFzAOJkcwx-QWGUoatrdgJMWORWOwenCxPOeM5_Bq6ur3u4hgOqH2dIrvOvVGDad4hwGDUsFoMXSGRlWd4WKpbmz9r4SpcOxDEFjY54xCYw-tMFjANDN4AdGOnujlTCHGQ5BVRDn4ISqDIQHaevfGb1YjajclYWHCLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIf2xBhwP-hFS5jsBTk5-L8YPTwV8aQTk-liR-KpmYH4RK5iYe1xM1bJ3xCzAHJ0JVz0KoM6pdBQPe9cetMD0VoBxEl68kwCCuxynyAV0qzhXrFn-Qexk_mBk7PIg7MFqH9gM6Pu7obkwNnPjIECy09b_mlCtwxp0w5KSqaOZOpCfYJa0PSnYCcM5EPjDJPbsuX8kN3sjrwTD5tdVinkdrRuF0rDFKnxyk1O33HjOy-LfOkPEXUieKfk08J7PGrI6hYUOkzPgbUnZPoGwnLYI26CImr6qKetI_TTdFTtszKMeooQupD6OThX5usY9ap7uu0pJ_Eqr2cMKjpzasRCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFky2rY16O7eZ2kI1N_rP5th-3YW1xmeW8HQwOSFpn3rELn1XFcbCxY_yw03qh5TnViUO4yB_6XeynVUJmmOBXAE0xIeEo6rmew84of7-G21v8M10_9hV2d1Csh1t6Gm9oXUSm-tHuFuJvxSnOJ3go1o90kUxGv2oYMqY8zjpm-e66LgYXwZ_IGuwRvRbtOyR931ywonEVs-l969joQQ4nTe6RpR-JeXXPwr3nDNY-f5J-mFYNJJfPZZp9lk9je1REpHpJ3ucC97HtJkxCBIo88b05WHaCiqjXSVMZZQHT_vHPf1Pa3VKOeJ1wwaf4Vr2fGR9Tedlpq_JpfREEFASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOP_hCNLBAaJty33DnmMV-itpUAgYEql3GV2oPP_R1807-cHq8pSyADFmPlZt0aPVRB4_49LyqxPD6bZowqwGKviTt6f8De7Q-wSsCdrC17lleFs9sGYFAfsZuxr_Dl7iWMZGnh-NWuBfMHKxWP4rzmes03ApyMja1H8EF6Vpb5nZ12LZfUmqqAM1lGkEIHGf39X2UUDiIx2QbSe_Uqay9YG3WczDL-2DKDXfigsTrUVqxM0aGN548HavW01A_fcWM3LJwNWvUny-UOM0UHm93KxINbZoBmYeWTEY4Wu68-i8a8FLHIyeXytXmaZ7Vxo3ZS0HBloeb3PaHuitP7bKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYupZ80NlCA8XqMDFhv_sJYyXmwfJHDsLbA6oLhs7-KpUSpfcHoowzFSzlbjceiK3IunJV5ia0fgwc6cGJqompnXCC7GZtq9zpQ8BAiOiymeyE9EZuZA5WkB6yGIpBGGgv-DVbkK9RJExc-yndV_5lzyx36ZLghXBRlhCJdqJDBiGS2WfahfSn5SmKq1k73plfB_vAjnUsQjDgIzHRPKVGxsJkTXCc0EKvzNe-d2IaZMqIGCFTFUS0R4eixfptpPACFXUnYvfJlESQzD6S865MzsvVPVyQTNmqiB7eyFmax_1zulNRuhSHyQmn-77ht13eK3y_pQizgV-uymkwjaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSIHQsnVBorZ-QdJWz71tW8wxR-sfRIIsvmBhwCGsVoxtcuAMeOcsHzVUOSBKUK_KeKj7wtCNtlJ56EvxeXkg_obauZPH-CE15DyYBd3hXRrhzlOYwl1-lSt91p3rWG8u7SwZM4eVSSuw8E8SmtI-PFnCWOpWuANuItgOhX7EOdPthsmNQueqIS-N3u1QZ9TM3WoRruJR6HggweOQaw3aHAkJdLpKp6v7-Vsl59O1x_qZqXLqjB9Jb96vsWh5vVcjHpL9-6QBsC8jNJgos-4Fut2ybxyEcmrT9_uz0uFrsL9mu_RINSk8hhjawixkb6zGyaio7ACrEXyfRKmwUs0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve8gaDOFLTvGmXEdLAdyzEIgwUKQrMj7cvB8D7rHl6W5MtzY8eDB9A8bvJJToPSawjlBj28uuM6MmbXZ1dhO5RFzPFKT8y6rAg7Q9n0Iw78DU5NW3IHwuzemC3Gwel2iw7jsW2itzUiXzsNJ-tATi1lQJOhS7m1shRMYLraihfeNmuZDCdR2Li-dHNq0GEKo-BOvNwtB3h_YuRbECoi2FwW6RDBB0SDMWm5bpxTSwHi0dlrA8aqcvigRSo5Uqt3gp7GbwnJFihiP8cPJsia4KbuIas_effC3MvedZe3EXEMf_By7-sNnf3tzBcEqfsbpapmXMchCOLk3VQh-erI8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gM06h37KTNTeW90rvkALL-B8MfkCitkGkonlaHeeADCLcs9UFWQ73AvV9_421ICN9I-KweSmwGTeLBbl0-KoNngtfLQz5krCC8I7QjeH7zAuVl5JkHfEMx9EkZzzg6tR6UR3Pyp2IDk3Qf9c0E9_s2LyK_wcSjw8EMbBYkuXqHdq-r5eGHAK66YZMR-Kd4vHNSh7kfpAPqWBSiE-yK8OTpTwd7O5dcpzdiOiZQj1Sb5YRbnEop7PfwZDm3FCDksQqxRK8IwFskEiSfOUuUXJpsG3ZNl1Y59s5lUv6eIpq_aqONUhBbTgUrKJDvXydyRwd7Mqm7bWrzYXJxhueoScTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqMxBotm9LmmI_lqcz5ackUvrE1Nr5CTU2dGoVitWVUuhZRDWX2kyO-THTACQbRRnM2-vKxg6VnEF0kpgsexJSW39wa6TX9tC-BP5NJjb-SrzG5YyboNjgkYLUNe6SKJ8Ad1VyZg0Ga8DrOHmq3_v66TPmoEZ7ImsVxE5jyiPxfE0W3XiVcmhaY8cjtVvjA1jk6Xkjcb7BmbIw2vrBOb5t2nKZWPXAxyN9NE0bT2-jv8Q49D8hqOLVA5aNclway8rKqma7YRravEcx3_DCSLLUyAfEIpktElSgVlvGx9LIfRwIwcUai3fneaNOfZdMwGi0reoBGzPS1O6shBkN8nAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUCGD0YeUcBgbw26_bWzB6VGJW9QbxNl5gW6QPeMTMeNsb3PDVaohkzecA-r_IlSRJI5EquyrKPdCy-jtAnei3bTGjIAzwxvS1fYPf0tn6dBIjGj0a7Gd40b6hoylfT4_Mn7HGTwOZ2-wEjWb3O8Y66I0Qpn3gQA6HuF53aNI81lf-TfQIz1HfXsH6lxbcx55twbUVpvjiwKjrDsVeXqtxivIidmaeMEr4GdXw40H4qu7qKDCOXm9xdnilhrH2GSJjK3UNPvdg9Laljo_l7rnvcny6zsSbWiQbeYTLD53Ea3GLHc8-33QK9CL8ZrARUhcPvICqPOLmN10bN_yFgI6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbGWRm3Mcz7evjMkeughOUkCPt9c47ipvNt70FcwzdeQt0s_NMP1fslRwWHrOqm05sta4zAqXSTU1o9kpRcKPAHHFMUiK2M93Eu_Sojyt449-KE9EYH-ImP1ORVPPn9482Sbncouh1n_OnJZCtPOE2JskY9NK8cXt1CwxKL_e4sYtzU85f4GXpbrhe6AOHmlgIKsc1d2jwlQaHBwK4Aak7zvp0U9SUcoonlfO-eWCp0KyzDcv6JuAUl52LIMGXt56ZDl9WL3Sm0B0ipEaD_FFueMuRUnSoNJ1WiFg7yK3-28f-4N4yf5NlcBFGhVs6hcxlDCUSoTPK-A6x4y-EXZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaBa3f6l3VsXnkWSBcQ7T7dODHIGw0721L5y6qSL2-NUvnooQ5IBSYhVlcP16m5JwC8WQOZOYnzVTStIGbrQgUblEQN48uGJwDTfe_3SJErdoZSJoy1goytj2DUyp22DbXQghcAOoL2Q8H74ewFyBiMqdd0zRco19d-gP2VNbrd5GTJOW5TG-07uI-5CKqMvdLXntdCftbnD_iUUn33mEO4aCP5vrZ6EPIXKBcatXMRMkuOTGPvIDcjZbsqUNGCqx6NK1H_HffvrW1Dc_Fii7ZRG97Zwr206F7kJGNbee6BCasKtKpHPOmuRkfGgOrcrK9PGq0MdLwkyQBb8KMMIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8WGIFG4brqy9xkdiT6ayFPd86iRNqwEjoVB1tYIhAFzEi8HL9rPM49bY5UqIDex36snlgyhB54PXyfPkMAK6iLsFCn-fknxFi9dErS_3ZcCz1QcPtwnndp6i2B7ltBy4V4pyM3U4t_2JLaxc_rNINBirJWCvHSR8m6oMcs72XOYEyLbqNYGLD_v813zWpDWghtEqvL0TSLY_kSCh5GVICKYj3svpDrb3ft-rk01DvhDXyir0z5SfNx8i0btjFu_p12hHUtz7ESHKZXdcPpy868P5vg7F_kGyyGCoqE-9m6IRkOkUwOpnt3tWFpOiM_iNWvFIm-ACdTXBEIl-MTw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJU3ACOL_qdWWp7v82uaDspHILkW93eqY4qJeYXwKYRfBe8fYlVYyn9xuHHB7jnspwwhBiSsnn6-Aweby3c0HVvcW-87ZFaUT9obM0fH3bj0r1TO960AJN9N_nAvj5w38KbqBy9oBvVi-x8OzkLr3lNnaTIAhmqETDqdNP_5eU6hymVbxaP4Xge0B46NWtq50iSTGTJjlN_a0-Q0Z18RhfsY8DSpB4kNFEvNKZlL_wZVq0aeiK7jvMKHDEy7ybX-WMjbj0T52Fxj0KuDdQM3J3ayox9djckW5KC6OoixQfQ0SJfCCohBGhYGANb7LqqETxHaugfpM-IcGY6p4aDt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZg8zyYdoudQ3khYMaoLNJAbr2F3XFv6ZczU8-2uFiT1NUh93ivpdTee-52VcEDALzS7QQby6538lEkZaVjSUQAduhCX-ub0_aumnJ2hAUxTHPLFnbgV_tcfGZ5SysQvB2KMMxoCUWp2R9E6qNb9CjPVVo2x-xlViVbscOHXi-jgZ2uU4_PyAPaKwd81YCURQdBXbYdyP94hmC8-8bfx4KHKBFa4Vc4Fa7lyOwCXY39bb8VJl3WKupVUjWnNU6JwEplYCw8iZZ0-uTU6vkbaHORUUGl8ACUss0ClE1pmpSKDEbbmZsK8TjZK00e_VoYomqKxCh5Px_0zf5t_JqPy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_lqO0iIn71slXB5oURuDaaj1mkZZ3e3W0FlnwlL2gSjSCWsqpRywI__lYBUj4vtFlTVPHrG3J2fWgD09xZXzr2hL-YVNrhYDm_Xh7NDZcrpXcrF2p_vcowEtAcToQgFy0BPO9JuOMsGG26ciA8hRsFSUKM5HVU4bwMwXEEBNObQlBdzzccpZdtaA8wwq5KVwRqL8pDzgcookOPQKQmKQLPLUNfQkHEFJSrrZd8uZMvquskn5HIy2ybWhPayJuZa9kDUgqodKdqy7MZsJ9lu8uDojur9cls47qEPX0k_E3C35hK-dmihF1HcLxUvx9uflH_MQgbVrNyMu7SdxJWdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=WeM3_cMZiBIhfaStUQUHYbcdzaj9Innq7U3HCOynpZQv1vthd-vJTr-e4mmFb_T-wbFkmJzeIdSKslCvF9BQSgKIVLS2BZlGYZyrhn5aMbf409KXRrLnXPFW7eSDhKxKotTTNJpHEcGzlsSX0fq3VRQbyNQg6lpoIEKZuYN8DqieM-1_VH2hRgTWzL5tRkTNZ7yBGFDFIjqxZHhTTZ_bMqizs9pzwcJ8kq9oO89j_AwD-PFRGj7pf8Rd039zcwx_ElEctDpLEAmneWa-5zEuh3TTJ0ACiFT2wifGgdDIDSE-OLg1RhhPOh2hVVqn2Fq4ssOjiTafzrj3xFkydfnqFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=WeM3_cMZiBIhfaStUQUHYbcdzaj9Innq7U3HCOynpZQv1vthd-vJTr-e4mmFb_T-wbFkmJzeIdSKslCvF9BQSgKIVLS2BZlGYZyrhn5aMbf409KXRrLnXPFW7eSDhKxKotTTNJpHEcGzlsSX0fq3VRQbyNQg6lpoIEKZuYN8DqieM-1_VH2hRgTWzL5tRkTNZ7yBGFDFIjqxZHhTTZ_bMqizs9pzwcJ8kq9oO89j_AwD-PFRGj7pf8Rd039zcwx_ElEctDpLEAmneWa-5zEuh3TTJ0ACiFT2wifGgdDIDSE-OLg1RhhPOh2hVVqn2Fq4ssOjiTafzrj3xFkydfnqFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJtJLFBMlExwY8rkLJpo39oRbyjzTn6W7jLWyWeeum9I_nk-wxp84SN-TCVSTMQ2w7lz93fU93e9AfPkmOTYxcwKO-MRfhDgtQ2_0XiWZMq6ytTq3fT-o8OiDgprdSMBFFL6MeYO_UMBhF5xnlKjLxT5zNC1LEcwbJYuQXjF6Sx3CRa5Gps8fnpnRDW_a_bzuuiIJ4KWIjMuktJ8aWXMdpXVvo2puSYh_-qilQvPn7eXx8RnrcDjI-Vy09cZPTfvYAei_T4nUPpxEhBa0Zeffe_D2ZdfN5-Qi8kjvDeZrKs6RIC6SqWw5JPX4sYFpTzNEvlQkG1tMMuXroaDSVZVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drdvXp8TrDy-aWFbu5md-uSZwYG7lreHQGULoyK2v5LFmVGovdGq_JH1h-1cs-MRwndWtjt5_YTEdkSmXWHl_C9GFjcjXe2nLz9zw6O-JIejEL2-soV7hA0RXuv_2aB8t3IkXrSp81Hnu06p4iee6BsslbGSSb7G_d70KNEd4wfOqqHLjR6Nrl-4fa83D5TAPGAJtIXEoag9UYGsVBxt1eaY1O5jP4fcOCyqhV4vPdpxIBSse_dGTI4smiXDZP9HrBFHKmzR3vi_e6tQZXykOeNWLbW44qXinVZ1qAXcg_pltook454FYUpB-oYfAuUQuLkSCARBj_F8v4f_0ekp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx2TYflHd7Nv0puLRyJoCKUn3yo279Qd0V2ly8EyHMQFGNbhMQDb6hzkiDZs0Jr7iTASiFVipgY-geYN98V3EcxPGUvZylKMVtiRcUX8FXriJSwuv6zB1noT-O5gx1zZDdO12OTu-kb-U5-xk5LRY2F21VAkVlX1tZQSOSa74rHyw3QyVb7b_dVJg-riQEfmdinRI7xY6Za4U69voCevfqycIWIAPHxDoMaAPMzDkjc_jiv-sXJ8q0w070sgG0Vzg3kV9yYz-huEU11q6VSWoJc6e_WOu4yDNNNwG9h_J0IYx9VQBjUohNhP4isJH1kAfhnz1lSPX0inkFmWpfSEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
