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
<img src="https://cdn4.telesco.pe/file/ibArnC4A7L1VTOkvFXxWu1Oj-0qth_PHX5DaSVZSeG35dnpi6WcXxs8SFDdLiw8GqK9wP4cKJVn0B2Bs_Q3EqOMz_vUvcsPMrotljWlHkSRL8I0x7Y6KBzqG7AYQ1sicIOI6cJEUbRv_NMCRnjUaZi7kgHtYmibVi0N705nl2XhmqBZJXDJr5hYWh5PiZD3IGR7Doj5C3lsybl2Voi2hDmWtFTbRbSVv09Wf3pvIyGBFDyTSAIq7TBTsY6wxmmQfm5Gv5oe8ktyEtA6R_92siaipxJ7tbptPkiBRvNt7qZn-uqinR5MDkKW5OfJcax0R_FIkLUPkq5So1e3U3G0HXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.99M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 01:45:09</div>
<hr>

<div class="tg-post" id="msg-654574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9145928.mp4?token=GN7basp_dPLh6FVKjlm9YpDwGlqH9z26YdPkkx8Cn2u12XbAGFGXwBL7TzLDqm71htjwpLx3uor_D9KrCLZKHOZj0kIEPKXls9kKZMYEakpNHLB3JnvYBllaQnQAqdFa4Hbw48uTZ54vDmUJMTce33hJICqAf3vrS541CEy_uqTKLQRMYBrxjFKQtuAgTD07oILSCeep7DIjoZQV9D8SuzaxbaLieiquhuNALXFQJEEAX4KZpKOH4-oWLQqIFifk4Plpl8vEjz6vcroWAuggn5bZKlkJJqI3EMIAT7sxuJ1z2PeRYG4MFNY5Tf23FVfKWrXEUo-ALaphCISva1oLZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9145928.mp4?token=GN7basp_dPLh6FVKjlm9YpDwGlqH9z26YdPkkx8Cn2u12XbAGFGXwBL7TzLDqm71htjwpLx3uor_D9KrCLZKHOZj0kIEPKXls9kKZMYEakpNHLB3JnvYBllaQnQAqdFa4Hbw48uTZ54vDmUJMTce33hJICqAf3vrS541CEy_uqTKLQRMYBrxjFKQtuAgTD07oILSCeep7DIjoZQV9D8SuzaxbaLieiquhuNALXFQJEEAX4KZpKOH4-oWLQqIFifk4Plpl8vEjz6vcroWAuggn5bZKlkJJqI3EMIAT7sxuJ1z2PeRYG4MFNY5Tf23FVfKWrXEUo-ALaphCISva1oLZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروش فوری ویلا مدرن در شمال
- اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat
🏕️
ویلا مدرن نوساز
،داخل شهرک
🔥
✅
متراژ زمین ۵۰۰
✅
متراژ بنا ۳۵۰
✅
۳ خوابه (مستر)
✅
روف گاردن با ویوی ابدی جنگل و استخر چهار فصل
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
⭐
اقساط بدون بهره
⭐
قیمت ۱۵میلیارد کلید تحویل
-برای اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/akhbarefori/654574" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آفــرتــورهــای ارزان و لحظـه آخری
جهان گستر پرواز شرق
🚀
🔻
ویـژه بـهـار 1405
🌱
🇮🇷
تــورهای داخلی:
🏝️
🚂
قشم : 5.700.000
🕌
🚆
مشهد ریلی: 3.800.000
🕌
✈️
مشهد هوایی: 13.500.000
🏛️
🚞
شیراز ریلی: 5.500.000
🏛️
🛫
شیراز هوایی: 15.700.000
🌎
تـورهای خـارجی:
⛪️
🇦🇲
ارمنستان:19.500.000
🏔️
🇬🇪
گرجستان: 34.370.000
🏙️
🇦🇿
باکو: 59.400.000
🕌
🇴🇲
عمان: 39.900.000
🇹🇷
تــورهای ترکـیه:
🛍️
وان: 7.900.000
🌉
استانبول: 44.200.000
🏖️
آنتالیا: 67.990.000
🏕️
مارماریس: 290$+ 34.500.000
🏝️
کوشی داسی: 118$ + 40.000.000
🚤
ازمیر: 147$ + 40.000.000
🚢
بدروم: 171$ + 40.000.000
🖼️
فتحیه: 104.890.000
🏞️
ترابزون: 38.000.000
🌌
آنکارا: 49.900.000
💥
آفـــرهای ویـژه:
🌴
🇹🇭
تایلند: 100.000.000
❄️
🇷🇺
روسیه: 265$ +49.000.000
🏙️
🇲🇾
مالزی:114$ + 140.000.000
🌊
🇹🇳
تونس: 890$ + 99.000.000
🗺️
🇻🇳
ویتنام: 1.590$ + 149.000.000
💰
امکان رزرو به صورت نقد و اقساط
📞
جـهـت رزرو و دریـافــت اطـلاعــات بـیـشـتـر:
🌍
جـهـت آشـنـایـی بـا خــدمـات مـا:
05131714
☎️
https://t.me/fullticket
🌐
https://fullticket.ir
☑️
لینک کـانـال بـلـه:
https://ble.ir/fulltikitir</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/akhbarefori/654573" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtuAAVbahY5XSNi8OIgbWwoqrtq-5a6vx5pujKiUMQagJb0zdNkOD6cCTQqrJfCNX0n8lnzZvx0AQy3InBdmzME449TmY8NGhOoF8s7dDU7xLUPplKd7aJT-0UP6zt-w3YwigoJApjgG1xQjyd-G6E1p1N-Cg4owW0gx6_WgQNqpJKH4IlN2aemmDIWjr6BwwMSnrCJX-f9m-0SYHp-UK0TiJXsQfycJ3s27jJEqzwkeOlG2u7XSOLtJa_XfESazxVvB-uk_ajUUPIGUtNmuDAFGucyTuOMPeDt9oMdvP2ClSC3Qt0INEBHInjPzn-cZ4SnJXaHQRHWlVIHkTKbGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/akhbarefori/654572" target="_blank">📅 01:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: یادداشت تفاهم، حاصل جمع بندی مذاکرات در سطح دیپلماتیک است
🔹
برای اجرایی شدن، نیاز به امضای مقامات عالی در تهران و واشنگتن دارد
🔹
نیت توافق وجود دارد و انتظار می‌رود که از مرحله نیت به مرحله عمل منتقل شود./ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/654571" target="_blank">📅 01:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
افشای
فایننشال‌تایمز: کمک ۸۲۵ میلیون دلاری به «اینترنشنال» قبل از شورش‌های دی‌ماه
فایننشال‌تایمز:
🔹
شرکت مالک شبکه تروریستی «ایران اینترنشنال» اندکی قبل از شورش‌های دی‌ماه در ایران مبلغ کلان ۶۵۰ میلیون پوند معادل حدود ۸۲۵ میلیون دلار «بخشش و تسویه بدهی» از سوی سهام‌داران خود دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/654570" target="_blank">📅 01:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60702f5550.mp4?token=DURrOivJFDMBOABUd_vzdbhM40wv3e9Xr7NvNsKEZFQ51z4lkTwh7Z4Ed3lJz6oIdLpasetsh6kqJrUkfLzdGHVsePfBvF8xfVwRFV7Y82_wklbfIgonHhme3kElo4M_wNuq5p0aLt67NYAZppZaLc7jR1ZQG35QiH1eeOILdYpTxNQqZcySvXVBz9IGQXka1k0OBJkAI6zS4IjHDJsTlKm-BWEXWd-OfkHCs7oZalJfMIDsvsqMG1hG-0Cj2QTNr3VITryJY12d3ojyg1-fUQw5jaQvUUF_1fJfUNjoKHuS7m_Y5t6lax4SBSrcy0jq8HK0X0RduK5FY1xshybCJnOywmayKD3SIrmt5Skani7mweK0fIXaTFWO5bF43v1IleBkmkbt5ROCMmi0uuICTfuX7tnNEoNPYPQQDtoMTJdTZAfh91u0ZpZIRT4DH6igTvnR2Kq6W8AcQrfdYiZjuOBwbdJ8Dw5mWhIhbcqVFwXARvjtfJ6eQDA156iySzMHw_8aqEETV35U8eSKjdYswkMUo6hlw-Nl77KCFpyJALs5ELBF6zD3QFMCbYfTm7O_CA752k_QuCuWv58MW_0_5dS9R7RtqhjHT-VPV5WQnAeLDCXDkW0sLThYWNXCfb_tqcP688MzOIBRiGpEWITSJfpNmbgWt_zbam7oyW7_FL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60702f5550.mp4?token=DURrOivJFDMBOABUd_vzdbhM40wv3e9Xr7NvNsKEZFQ51z4lkTwh7Z4Ed3lJz6oIdLpasetsh6kqJrUkfLzdGHVsePfBvF8xfVwRFV7Y82_wklbfIgonHhme3kElo4M_wNuq5p0aLt67NYAZppZaLc7jR1ZQG35QiH1eeOILdYpTxNQqZcySvXVBz9IGQXka1k0OBJkAI6zS4IjHDJsTlKm-BWEXWd-OfkHCs7oZalJfMIDsvsqMG1hG-0Cj2QTNr3VITryJY12d3ojyg1-fUQw5jaQvUUF_1fJfUNjoKHuS7m_Y5t6lax4SBSrcy0jq8HK0X0RduK5FY1xshybCJnOywmayKD3SIrmt5Skani7mweK0fIXaTFWO5bF43v1IleBkmkbt5ROCMmi0uuICTfuX7tnNEoNPYPQQDtoMTJdTZAfh91u0ZpZIRT4DH6igTvnR2Kq6W8AcQrfdYiZjuOBwbdJ8Dw5mWhIhbcqVFwXARvjtfJ6eQDA156iySzMHw_8aqEETV35U8eSKjdYswkMUo6hlw-Nl77KCFpyJALs5ELBF6zD3QFMCbYfTm7O_CA752k_QuCuWv58MW_0_5dS9R7RtqhjHT-VPV5WQnAeLDCXDkW0sLThYWNXCfb_tqcP688MzOIBRiGpEWITSJfpNmbgWt_zbam7oyW7_FL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار
🔹
خاطره حامد شاکرنژاد، داور برنامه محفل از اولین دیدار خصوصی با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/654569" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMc_ShXIbrVy71Ok0YY7ZVW5v2m21Vtl619z1UOXPFYHZ0EciOaechs5w5Q9WwHuks5VAUz84ZjWC7S068FQk0IlF-FU02nYa-DHvfgS7B4GstWZiD-dgL9G9i0g6WhvYBBFM0l32RiCZvQ15MJPx4Yj0Hnabhaq4nZA0iMGSIZe0maMjHz8KLWcv71FEb49iNVPvJw_hTQ-TzW7H1YEtxVh1H64Oy_xEYyuU58qBhMT676Fx_rfd4DYOSy0Ng2YnWiSY_mTns8M7d_k3F4Sj_fuKvjArEdsX6QPPI0aMk9mdTQYKh_eLDp-HwiIn7YEQauT1k9LH-b7s9mkLdjfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b16ea4bd.mp4?token=D5OaOVbk0LHJUHcCXqQbSaj0wQ-sjFa0KwYHZ8jyOfK78DZKPjvSJiZA8SAmllKkvH6-pTCOZbl7LTxf4Y08mtGQ37VFM4yoD3tKy1lPeyR3yEmjSyhOVoJ4l1kr6fUjqtALf9Njn4sQ6VQlXZwpXTFZ8E19j1iHioOOoOvgelrJqlXEyiBOxB7mMDP-O9E-WdcoMtnu4xX45tgt2SxEy44HhpAtH3NZ3QNMfxI9V4S5iu0GNVu62F5QfR-_VWVNxtVK9z-ZbA4JOJtP10PewhQtBXszZaPAhIZUd3kM1Oxi1K98MCZUPdHwnmLKDEUxdc1AVeoDN472mfAycavG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b16ea4bd.mp4?token=D5OaOVbk0LHJUHcCXqQbSaj0wQ-sjFa0KwYHZ8jyOfK78DZKPjvSJiZA8SAmllKkvH6-pTCOZbl7LTxf4Y08mtGQ37VFM4yoD3tKy1lPeyR3yEmjSyhOVoJ4l1kr6fUjqtALf9Njn4sQ6VQlXZwpXTFZ8E19j1iHioOOoOvgelrJqlXEyiBOxB7mMDP-O9E-WdcoMtnu4xX45tgt2SxEy44HhpAtH3NZ3QNMfxI9V4S5iu0GNVu62F5QfR-_VWVNxtVK9z-ZbA4JOJtP10PewhQtBXszZaPAhIZUd3kM1Oxi1K98MCZUPdHwnmLKDEUxdc1AVeoDN472mfAycavG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تریتا پارسی با انتشار ویدیویی از حمله به پل B1 کرج در جریان جنگ تحمیلی سوم:
با بازگشایی اینترنت در ایران، تصاویر بیشتری از آنچه واقعا در طول جنگ رخ داده، منتشر می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/654566" target="_blank">📅 00:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbhpASOPNzFaX_p49U_QRTtUv5QJ4L7UhxR-zTyHwTgk3p94ZlYF4tR2B8t8_kiIGNkTn1NABB4hH9eR_IzDbslNMlP7cg9CzgUXB46gAHQqNiS_Qfmwi_opM7an1ibJGUTQWj-U1tRc7sRdjgjCs5uML4fwdO0mYLPLy6nnudBd6-xu2dj_QTEYhHBlHjGSmbN9qgL_NquMpnrMIj2Ckjhb59uk5qIDh62-MsLfuH8RSedSChtN598GCOChMmCIOA7JLcE1z7UUmJ7hBXOITuqyrUeFOTvuCqZMDrkB2MPMldNQq4eoUK6T3Jvh3dWYwe8xA2x4aTVqmACE309JlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرهیز از اختلافات پوچ
رهبر معظم انقلاب به مناسبت سالروز افتتاح اولین دوره مجلس فرمودند:
🔹
از جمله مصادیق تقوا، رعایت نعمت عظیم وحدت ملّی و انسجام بی‌بدیلی است که حول پرچم ایران اسلامی به ملّت بعثت یافته ارزانی شده و در زمره‌ی مهمترین عوامل ظفر در مقابل شیطان بزرگ می‌باشد. شکر این موهبت، اهتمام آحاد ملّت خصوصاً نخبگان فکری و سیاسی از جمله نمایندگان مجلس به صیانت از این وحدت و پرهیز از اختلافات پوچ سیاسی و برجسته کردن تفاوت‌های اجتماعی است. ایشان بیان کردند: از این پس، بیش از پیش برای پاسداری از وحدت صفوف منسجم و به‌هم‌پیوسته ملّت اهتمام ورزند و اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنند.
🔹
هفتصدوشصت‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/654565" target="_blank">📅 00:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
هاآرتص: ارتش اسرائیل برای احتمال از سرگیری جنگ با ایران بدون هشدار قبلی آماده می‌شود
روزنامه صهیونیستی هاآرتص:
🔹
ارتش اسرائیل برای تشدید ناگهانی تنش امنیتی با ایران آماده می‌شود. ارتش به نهادهای دولتی یا سیستم مراقبت‌های بهداشتی هشدار می‌دهد که این امر بدون اطلاع قبلی انجام خواهد شد.
🔹
مقامات ارتش اسرائیل همچنین اذعان می‌کنند که در طول جنگ، شکاف‌هایی در اعتماد عمومی به تصمیم‌گیری در مورد دستورالعمل‌های دفاع از جبهه داخلی ایجاد شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/654564" target="_blank">📅 00:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
صداوسیما: دلیل صدای انفجار در شهر جم مقابله پدافند با هواگردهای متخاصم بوده است
🔹
ساعتی پیش صدایی در منطقه ۷ چاه شهرستان جم استان بوشهر صدای انفجاری شنیده شد که گفته می‌شود ناشی از مقابله پدافند با هواگردها بوده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/654563" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
یک منبع نظامی رهگیری یک پهپاد متجاوز آمریکایی را در اطراف بوشهر تایید کرد
🔹
به گفته این منبع نظامی، این رهگیری از طریق شلیک موشک پدافندی به سمت این پهپاد انجام شد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/654562" target="_blank">📅 00:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
صداوسیما: دلیل صدای انفجار در شهر جم مقابله پدافند با هواگردهای متخاصم بوده است
🔹
ساعتی پیش صدایی در منطقه ۷ چاه شهرستان جم استان بوشهر صدای انفجاری شنیده شد که گفته می‌شود ناشی از مقابله پدافند با هواگردها بوده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654561" target="_blank">📅 23:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
تبادل آتش دوباره میان ایران و آمریکا در کمتر از یک روز | شلیک ۴ موشک به‌سوی شناورهای آمریکایی | شنیده شدن صدای انفجار در هرمزگان و بوشهر
👇
khabarfoori.com/fa/tiny/news-3218570
🔹
این سند خبر از جنگ سوم ایران و آمریکا می‌دهد | پاشنه آشیل توافق یک صفحه‌ای چیست؟
👇
khabarfoori.com/fa/tiny/news-3218518
🔹
اخبار لحظه‌ای مذاکرات ایران و آمریکا | توافق نوقت سه روز پیش نهایی شد، فقط مانده اعلام نهایی!
👇
khabarfoori.com/fa/tiny/news-3218401
🔹
رئیس تازه ارتش آمریکا؛ یک ژنرال چهار ستاره تندرو که دوست صمیمی هگست است | کریستوفر لانو کیست؟
👇
khabarfoori.com/fa/tiny/news-3218501
🔹
راهی برای معامله نیست | چرا ترامپ نمی‌تواند ایران را وادار به عقب‌نشینی کند؟
👇
khabarfoori.com/fa/tiny/news-3218537
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/654560" target="_blank">📅 23:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ترامپ قمارباز: ایرانی‌ها مذاکره‌کننده‌های خیلی خوبی هستند
ترامپ:
🔹
«آن‌ها مذاکره‌کنندگان بسیار خوبی هستند — خیلی حیله‌گر و زیرک‌اند — اما همه برگ‌های برنده دست ماست، چون ما آن‌ها را از نظر نظامی شکست داده‌ایم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/654559" target="_blank">📅 23:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
منشا صدای انفجارها از سمت دریا و مربوط به تبادل آتش است
مرکز کنترل فرماندهی پدافند هوایی ارتش:
🔹
تا این لحظه انفجاری در منطقه بندرعباس رخ نداده و گزارشی در این زمینه نداشته‌ایم.
🔹
براساس گزارش پدافند ارتش، منشأ انفجارها از سمت دریا و مربوط به تبادل آتش در اخطار به کشتی‌های متخلف در تنگه هرمز بوده است.
اخبار لحظه‌ای حملات امشب را اینجا دنبال کنید
👇
khabarfoori.com/fa/tiny/news-3218570</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654557" target="_blank">📅 23:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
غیررسمی: پدافند هوایی ایران یک پهپاد آمریکایی از نوع MQ9 را سرنگون کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/654556" target="_blank">📅 23:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تسنیم: گزارش منابع محلی حاکیست که منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا برمی‌گردد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/654555" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
گزارشات غیر رسمی از شلیک موشک هشدار به ناو آمریکایی
🔹
نیروی دریایی در نزدیکی تنگه هرمز به ۴ فروند شناور خاطی شلیک اخطار انجام داد. این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/654554" target="_blank">📅 23:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آمریکا شخصیت‌های حقیقی و حقوقی مرتبط با ایران را تحریم کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا، نام یک فرد، ۱۶ شرکت و ۸ کشتی را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
🔹
فرد تحریم‌شده تبعه هند است و شرکت‌ها نیز در کشورهای چین، سنگاپور، قطر، جزایر مارشال و امارات مستقر هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/654553" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وزیر ورزش و جوانان: وام ازدواج حداقل ۱۰۰ میلیون تومان بیشتر می‌شود
🔹
تلاش می‌کنیم صف وام ازدواج به حداقل برسد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/654552" target="_blank">📅 23:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گزارش‌های تایید نشده از صدای انفجار در هرمزگان @AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/654551" target="_blank">📅 23:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
گزارش‌های تایید نشده از صدای انفجار در هرمزگان
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654549" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: توافق با ایران به ترامپ بستگی دارد
اسکات بسنت:
🔹
توافق میان آمریکا و ایران به «آنچه رئیس جمهور ترامپ می‌خواهد انجام دهد» بستگی دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/654547" target="_blank">📅 22:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654546">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9af1d091b.mp4?token=H89Y4CY2fmxz5q0dgr1ICx-48mdlU4gB0d_l5WZHafcr8jlYeO7sY2aXtL3MLO2FYxvL7qF7tALq49o-BTq7tC_e_wvvR1Cb_oZ5XIsO_IDGP8TPXTYxnPzLdWzsi5wtJ3e8Fmnyru6F2ZjPb7LcdFLvI7iSkls9KB2Rz31qtujiICVJFXfokPmRHB013WzBZ5x0o1TYk54OMxBYoCM3oNlQVeUx2B8TrH50L6kWtS_aR_U1qJPXGQ6oMhBHkhvFG5xRorN9OJEZZBq7pLw8E7MMDECJjNO4BBCsR3I8e4lSMzaPw86N8FIeWCNkz7DJ2JXsIZ-GrFLMy1lQcMRpSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9af1d091b.mp4?token=H89Y4CY2fmxz5q0dgr1ICx-48mdlU4gB0d_l5WZHafcr8jlYeO7sY2aXtL3MLO2FYxvL7qF7tALq49o-BTq7tC_e_wvvR1Cb_oZ5XIsO_IDGP8TPXTYxnPzLdWzsi5wtJ3e8Fmnyru6F2ZjPb7LcdFLvI7iSkls9KB2Rz31qtujiICVJFXfokPmRHB013WzBZ5x0o1TYk54OMxBYoCM3oNlQVeUx2B8TrH50L6kWtS_aR_U1qJPXGQ6oMhBHkhvFG5xRorN9OJEZZBq7pLw8E7MMDECJjNO4BBCsR3I8e4lSMzaPw86N8FIeWCNkz7DJ2JXsIZ-GrFLMy1lQcMRpSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ترامپ مدعی شد ایران برای اولین بار حاضر به گفت‌وگو شده است
!
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا، در شرایطی که ارتش کشورش در تحقق اهداف جنگی‌اش در ایران ناکام مانده روز پنجشنبه مدعی شد که ایران در دوره دونالد ترامپ برای نخستین بار حاضر به گفت‌وگو بر سر برنامه هسته‌ای خودش شده است.
🔹
ترامپ کاری انجام داده که هیچ دولت دیگری قادر به انجام آن نبوده است. ما ایرانی‌ها را به گفت‌وگو بر سر برنامه هسته‌ایشان و دادن تعهد برای نداشتن [سلاح اتمی] واداشته‌ایم.»
🔹
بسنت مدعی شد این اتفاق هیچ‌گاه تا کنون رخ نداده است.
🔹
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/654546" target="_blank">📅 22:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654545">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
برخلاف ادعای منابع غربی، متن تفاهم‌نامه احتمالی تا این لحظه نهایی و قطعی نشده است ‌ یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
بر خلاف ادعای برخی منابع غربی مبنی بر اینکه متن اصطلاحاً «یادداشت تفاهم» میان ایران و آمریکا نهایی شده و فقط منتظر اعلام دو طرف است،…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/654545" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654544">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
یک سایت نظامی صهیونیست‌ها هدف حمله پهپادی حزب الله قرار گرفت
🔹
تجمع نظامیان صهیونیستی در مرکز تازه تاسیس در شهرک «العدیسه» در جنوب لبنان هدف حمله پهپاد تهاجمی حزب الله قرار گرفت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654544" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654543">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad37beb71.mp4?token=HMDEC8-2kLBegJRlFqZWGON4muSPcku8qJdjRGqnRrvcBLmbJZeIRT0SFBhEFZgN0yAZC4AGOrokVl5VrEiqDum3eD9FzJEnpbxog48toI-tlgsC3ex1E5E-mutnAkELQejKEV1SXMiTcaW4vKpSVPKzmCzQRY8QyMndnD68d0UppPJf0D-eUuygeyJE8jdRx8FAT9QkJ_0dTaqdMKLwHmNu2x-mg194XUT09lNasnsh2F8vFJMc4MaUHzbqI-jUTCLVQ_13JguHLx2RuCeEL2sAk3b7a6803NzmxBC3rjAe3_w7813eYtBoUaoSAx2JHfoIax3bsdJAN29e4QvlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad37beb71.mp4?token=HMDEC8-2kLBegJRlFqZWGON4muSPcku8qJdjRGqnRrvcBLmbJZeIRT0SFBhEFZgN0yAZC4AGOrokVl5VrEiqDum3eD9FzJEnpbxog48toI-tlgsC3ex1E5E-mutnAkELQejKEV1SXMiTcaW4vKpSVPKzmCzQRY8QyMndnD68d0UppPJf0D-eUuygeyJE8jdRx8FAT9QkJ_0dTaqdMKLwHmNu2x-mg194XUT09lNasnsh2F8vFJMc4MaUHzbqI-jUTCLVQ_13JguHLx2RuCeEL2sAk3b7a6803NzmxBC3rjAe3_w7813eYtBoUaoSAx2JHfoIax3bsdJAN29e4QvlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کودکی که با آرزویش در برنامه محفل همه را بهت زده کرد!
🔹
مردمی که امروز در خیابان و میدان دشمنان قسم خورده ی ایران را شکست دادند سربازان در گهواره امام خمینی بودند، با بچه های در گهواره ی شهید خامنه ای چه میکنید؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/654543" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbtX39jnFer5gxv8IBoIgG_N5M2e8SJR21Sos_y_MrM7WNbc7cR4RQnwsprG6mBNoYRMvMI9jMewEA18Dz0OJ6FOqQp8qVVmuHj_B2d2vo4t7VqWgYr5gUbOG5onNMh7_jgx0zJQISdZFRaDC4JqBh20bNEDec_ocJINJObkf0D0_oEhOeNixgNcleTzgAorN5nn6Ec3Wm4yoA3ScJBKNT-5VgCW1f7uIk_9pkfleomyzTSYhvLE6_auo0ZyMn1ji1N-PSiICo7qnHtzBwURm2d4pVQ3pVHLfB5k1scR1xoZq63tcY0oeYwZj3I2qId_zDIWprEfxW5eB3qBTOaanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان ایرانی آگاه‌تر از همیشه!
🔹
آمار ۱۰۰ هزار کاربر فعال روزانه و هزاران مشاوره ماهانه در یک پلتفرم سلامت زنان یعنی «خودمراقبتی» برای زنان ایرانی به یک دغدغه جدی تبدیل شده است.
🔹
با توجه به سبک زندگی شهری و مدرن پلتفرم‌های سلامت زنان به یکی از بخش‌های اصلی زندگی روزمره زنانی تبدیل شده که می‌خواهند آگاهانه‌تر درباره سلامت جسم و روح خود تصمیم بگیرند.
🔹
همزمان با روز جهانی بهداشت قاعدگی، آمارهای ایمپو نشان می‌دهد نسل جدید زنان ایرانی بیش از گذشته به سلامت زنانه، آموزش و پیگیری مستمر وضعیت بدن خود اهمیت می‌دهند؛ تغییری که می‌تواند آغاز یک فرهنگ تازه در حوزه خودمراقبتی باشد.
مشروح خبر در
👇
khabarfoori.com/fa/tiny/news-3218552
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/654542" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خبرنگار: آیا کاهش تحریم‌ها از ایران روی میز است؟   وزیر خزانه‌داری آمریکا:
🔹
هیچ چیزی روی میز نخواهد بود مگر اینکه تنگه هرمز باز شود و ایرانی‌ها توافق کنند که باید اورانیوم با غنای بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
🔹
سفیر عمان به…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/654541" target="_blank">📅 22:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047748234e.mp4?token=MnHB3eRDKqVsUug1rWCRXD-cpxGDDWSvHo5ubNlfSZCYgqtatGF2FiGC-C_GKuf2xw4bqGIHtm3lTxHNCs2jkGrlZb8NsZYWYyBp9XJiWjysEDm-rNorO2oU0nCQ10tfccsjFjtMNy-8M8GiyJmlLfD9L9TAwWsAIp5mhb53FjCRe9anVdK7YobUlIMKELkqz3X_f6_DTMqNuq2Xb1M0AcC8OHMr8bGiTxAUFagJwVIAAWYH-gIeMOzmWGK77KSk7HtwhLlISmxK3GirvhixvBIRntFzD56IKPCD-99NoasCLaUjkU3p3tY5rftJT-U0HGMPI8IQasgoNYyp0sBAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047748234e.mp4?token=MnHB3eRDKqVsUug1rWCRXD-cpxGDDWSvHo5ubNlfSZCYgqtatGF2FiGC-C_GKuf2xw4bqGIHtm3lTxHNCs2jkGrlZb8NsZYWYyBp9XJiWjysEDm-rNorO2oU0nCQ10tfccsjFjtMNy-8M8GiyJmlLfD9L9TAwWsAIp5mhb53FjCRe9anVdK7YobUlIMKELkqz3X_f6_DTMqNuq2Xb1M0AcC8OHMr8bGiTxAUFagJwVIAAWYH-gIeMOzmWGK77KSk7HtwhLlISmxK3GirvhixvBIRntFzD56IKPCD-99NoasCLaUjkU3p3tY5rftJT-U0HGMPI8IQasgoNYyp0sBAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا کاهش تحریم‌ها از ایران روی میز است؟
وزیر خزانه‌داری آمریکا:
🔹
هیچ چیزی روی میز نخواهد بود مگر اینکه تنگه هرمز باز شود و ایرانی‌ها توافق کنند که باید اورانیوم با غنای بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
🔹
سفیر عمان به من اطمینان داده که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/654540" target="_blank">📅 22:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654539">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4aeb2fe51.mp4?token=bocJP1ABP5WLjkoQNJEqoS-xFJTKVyJ8aFRRIR44XZkpkMbHg2UWg-kj85QaLhLhMlkWAI8mpt1xXkDtttpIwoaiaG-u_jhyz5UVtt7QJX8IhXonKjRoo7cHUsi6M5S4Uwu_Q19tBzrW3-_x5dRappM31-B8YwIrBT2Icd8ECkdUjQxYa05qNzrzqc6W0cq38g-fFnmww0fbLN6O8tNUchkk6EN_Jvt6m4kLRSGHl-fNMMYDODKLEIDwyETxWPM02Ofr-II6dNRzRH6XRJcufC6MtYV3P49-0gXUbIIgawmbfYNjuymFVDMBgzljkZFwlEGx1tretc_4Bopy7Zy70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4aeb2fe51.mp4?token=bocJP1ABP5WLjkoQNJEqoS-xFJTKVyJ8aFRRIR44XZkpkMbHg2UWg-kj85QaLhLhMlkWAI8mpt1xXkDtttpIwoaiaG-u_jhyz5UVtt7QJX8IhXonKjRoo7cHUsi6M5S4Uwu_Q19tBzrW3-_x5dRappM31-B8YwIrBT2Icd8ECkdUjQxYa05qNzrzqc6W0cq38g-fFnmww0fbLN6O8tNUchkk6EN_Jvt6m4kLRSGHl-fNMMYDODKLEIDwyETxWPM02Ofr-II6dNRzRH6XRJcufC6MtYV3P49-0gXUbIIgawmbfYNjuymFVDMBgzljkZFwlEGx1tretc_4Bopy7Zy70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: تبادل پیام با آمریکا در جریان است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/654539" target="_blank">📅 22:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای خبرگزاری CNN: ترامپ قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/654538" target="_blank">📅 21:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654537">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-nlMD2LeSYJ21401eZF7-n6OsGJRCyZ4G8azriTx2XuiqSc6AHenAInEeKofZuBK25ZpG2hLTntH3ybFkdqhgDVjzSbWd2jf2Okfnb7w6s7BlVYBbPrMoByjIabUREonOdguBTNCowenEutUp5OA9ftAtDKtykoAlzUD1fTjmxo5e5T-jCpdMI23ndJaQfQcWLkN5KgXeLBlwZRAFk-coRmGbU0xq9i-q4mvmhvMBsJTTOFLvs3Gj0bdmXujlQqA_np5FWWdSGmBA9MRaYicqiNtLpC0l_B2BS5IKF6JJhX_zzAnD9YtbI0inHSHZqoIKtfXcevrXQUec0MtmLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این سند خبر از جنگ سوم ایران و آمریکا می‌دهد/ پاشنه آشیل توافق یک صفحه‌ای چیست؟
🔹
پس از توافق محدود و موقت، مذاکراتی طولانی، پیچیده و احتمالاً کم‌نتیجه میان دو طرف آغاز خواهد شد و این بدین معنی است که جنگ سرد میان ایران و آمریکا دوباره ادامه پیدا خواهد کرد و هر دو طرف منتظر دور بعدی درگیری در آینده خواهند ماند.
گزارش تحلیلی خبرفوری را بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218518</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/654537" target="_blank">📅 21:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654536">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PscdwQxiNWuK78Z2ZJiYwX_F6Okqe5pN36yt0Tz11FLU5XmrVwX7nOn4EZgTvj_wnAjs4wkUnzY9OlBTD6cfwsn37Tu4tYLXNK2-f2dE4wujrPKd5kIdev1NLiFq4URfSGQQxvl6ippEyLVuarfy0kIRwDdjCRUweyT2eflT96lXAiNdNscO2BdxCYj8sokLGazsjbWHf_jFkFhxCjtwWHOP3cuEtSbp3XTdS-wm9Ru4XS7bFlESc3KK-HjUYRa63wCLHjyqNeyQvl9GwwdvRvhtARmRAT0G6JX2B4jgjMfwPeJ3kfUkhDVmZ1CD6UbZkZxfMcEyNByfxivo2XUExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الحدث: هگست نخست‌وزیر قطر را تهدید به ترور کرد
🔹
الحدث مدعی شده وزیر جنگ آمریکا در تماس مستقیم با نخست‌وزیر قطر، در گفت‌وگویی درباره حماس و ایران، با لحنی تند او را تهدید کرده است. طبق این ادعا، پس از بالا گرفتن تنش در مکالمه، دوحه نارضایتی و شکایت خود را از طریق استیو ویتکاف به ترامپ منتقل کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/654536" target="_blank">📅 21:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654535">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی: ایران و آمریکا سه روز پیش در دوحه به توافق رسیدند، اما در اعلام نهایی آن تأخیر می‌کنند
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654535" target="_blank">📅 21:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stRWTWmQb_t5gZdTk_Yd0Wz3BfJVSxic2ViOLNgnCp6BW7Y9q-sDxfHMWot5pJrPa1qCrFmTHRqasnRW4bEbNOT9988pTwUeZYMkj7Il9oNFoVnIkVl4nWBGwViRPbACRNuHH4fKK6ftCJAZNIayvG3YRNf5NNG024nuvSoxt7N1OTYxcTYBoh8ixybWDSDbackEONXhT9rltCr_ANUFBWxvulkJ4OUDNoFWwFOPi4-o4I0mS2LPl2ELdtnXnylfTVv9UklcOEHDU3GfyDJ67OEP2ZWlIK55B5yVYWbr0au2n-Gj5KFPkS5qgTKWQQzQonjnekoV7jLt73-j0eYhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSd_gV07-5DQ3yG8-JOgiCQvoRGhZSHPHal2dy7ATFfejt49mL8j0yQbweVbjhaZd-b5DlI7OSDcFW6mZAY9Ojn4IwZy1PlHrqP85bwIOdshG6elpUugR4VcZCsHDIfTbNRjbxN6nG6jmTIK5HQ9btnUDiNUVskYa_19hqOue5XWow229X0kCOkmppBbBrs9DhEYl5DLa1q7j8MUiTzH2VIUcCFqNA6nFQUhLK9f6eeJmNx0CE-Ka3dnA7g4Q3nkw030KizlMnkqx3czFElAGeYjDoDyl3inowgmUNWB2EuzVQlTTCDm42M-lV6zr5-Dn3Tfjq1zuHlWGnIzvL7HYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Szbn3sGo0yLvqbJ232XcMhS8vTPa_J1a-mepV2TcTvZdS6VtKpinlymx2pj7Z5fizs5i49PrS2_IdzvDU5Uqv8Yn4BdVfGj5C4ZZFlnI3Smp3tUV5tcN7a5UbJT_MsQ6awQXpVnviHQ9w66S4NNPXdhepNFcyDy2pL8aNGl-JewTm1yUo6fOqiAxBo_S0LQbh4b_KF2epCCyWc3qC67GWLWpr_JAWcCok78nU6okPv_Y75cJxmXyVp5XN3Sq2ZzzPX66Ql2qFunDB2LyVyWSpH1NsWkIml3TFx-8q2ftSODS3_rhP8zJaYXPPQSeMFq0OOUIhFeLv2gquTwxK4USCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHCAwz06T_T7dLbVaAnOTD_boSGJiNHUj9xEHvJq9OISj3I3qtTZvgyVzrdKonol43gPqoPJGb8-stUcsDFFIr19vKi5VLckEaT-BpV9qEEzjyqfIvlvs49hbPUasT4vRfEhoCUyF-LYcx22gJIj-kn0grNIzocQnK9byjCZadH_fvvq0RTPeV-n--BbNGFlxULaqn4gDt0z1bCdhyyfx9-WEFVU18JsQ7MNsDxCxkafhNJ3WoYxPRo9bQwEB8EkaWNtv4k3Gis7740Q83JGrQyyqygQJOW3hD7OU1wYhKqvmAoVX341fuwUk8ARHtUJqPAh0Hqcdbj3GdvPNaU4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlYpFYkI2Uc33ltS_RRSoCVMciQJGSslUAqbVwOBrs_wZqM2C4BLf9LolcukTCSoJ9W3dnMmOMphtMWZzjeb70PpgByiZOw6t40JC5FU-QnjkUnVQWrsxfQtQtfIyERM6svajnYyy6mlAVb1R2qps_W7G6RWmqKVpbuOWw-WPUul78S7UgKIKLGdMXTI5tnQQB6toGTFx9dKOgaM4IofqL8Pza_jRGb4Q2Tak7d4MVg_-i44b9vPcbfxvLe_Qq3vvsL4EDst1ptyJljDTc-juEu4P0FXDkFCWYWeL5MkBU_MBekX4jJAweA9de_Jbv7WFbHdUTFEnzyDf9j9kUVMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPymfWoGUs5pIzwF8ezytRd3EENY0L9mxH5zfblQcoc-6u-vomee3Qfuu2GNpddOGReESDfYbmvC7Jomx--XEMKE6aGpjJw3o7ZfQ5oX_bSyirCAFH1u6l00ur4LMHiMkoZ00XS8mbnN1uiwEMoNOFt0pHsvAufrbnnxzB4OAjABTWO1XysLQxXrLhMWKkxwU0kbXElmS3mPaesAByqWOjBWA2_2Ix84x31oHx2IKGjRnAl3AwH7ReG2VcmoQ9LIVtZ_3z2arpjT56r-9227jmGl3URHQguL1tg_rncn5i7de58faW8zYmmoKEiY1uzrHLR2n3Ov_ODHdVq8SidAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j280-lb9VLiPcVKL5wkwS3HtYCJJDnZhNz4Ve3FgIEkgOIfQWN86R9rAExoELAWI-JxT5SIRVz3oP8gxFLDKOfbrUjnXZdjjqZue4E0eqFX7wwA_mm7wC52XR9EQNguFwmLNsxr9q1BGMWqrUtJkrhgeMCM_hUvjXNFQlmAyofCCjOF_53XE3_lC4qGvfwukIGAbrBYUmtp3B7u6QoXRpBQiq3mcsTsQ2Uzhoh0Y8JzqdaQJnudsMIaAsBQ8zMp1CAOu3J0qP0do3lDK16-Ms_UnQyAtjT2tIKTz_moEFCSOF7QfeSHOMkGgz3LNkyU-9jrVNlpnw4NK6tKNG4P1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGReYhTswG-xRcyyddPZI_JHsV2R-C2jGoWueFoJsbzgu1QCJrlg0-OO3fifT6LN4LUs1k5u83ePvxt2GGs85ZtY1DZa_2ei0hb9np-ZYdmBVv6ORU49x7BpRF7gsa-9cWQ08JPq3NFwMUQgQTK93cC9Juxx_xckd2jB9Vc6rwmYq3ttyMnPBnXecUY1XwX1KO-FvOljq-k40PN9IrXjoh3s2lSGt2dGyChRtNFT7V1LuOBpaXcyuDdkZvK1IINVmq2f682zrfHxOZoAkiFgqojxtZOOXakxNIP_S4xKWlout6RyaKTSdFpqZZswohG9JUvFniwM7IFg_zfhRC8qkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd6fqg13eQMsdD5TBA6N5eSeB0aVI---h7Qmh2473-Gg8SWJ5mlLXmijniDMT9sBV9Xh6oeepYDiM1ugVA_W04-jg5s1rInu3tNMkZN6bHCQBzvv24LFr_3VwQDAkPgqaHZKFWy6mGM13bRy6rwp-OZcH2S4v16Lo30iBHLw8_vumUrtmkQ0cOS-05QS1Yaqo_rpBPC3ZI3cBHxOD4ZTCso5yPXy7F70m8w6bucVb-8Vu279j3b7o7bOULfapiX6dbONEKuMdGjecjkrwai2xVvQYoa4AHz-fiKXggQxufT39JQYApiiAe70iRzXEnQDLEYOVE3soBJ6sHnv9GbtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkf23kKvWd_ElY4RMfd2QqUptT6rTaGow5518DkHf6f9BKJdXMg4tg2lSVzklRWlt6Iaaa0PN44qw-4TBlBgyT5r-T8JW0gQjW3ixEYCoOQwGwNF3ul8YVByl2l14ncf9qKwTMJzAX_xkGc-RrOaziWjFsXU6r_4YBw3HBA8WGf-ylpfxB-1592JaV420sgBxlqgK40LZU9suGAJ3NJDKmOoGDEqITmZAWzWEU7ovMKdLcZ6xY6dAMNaCASMstkClvFoZYjsOZDptEdYf5j3BOWTWlb8xHZ67FiBnnKHhZz_wO6XeGbmWdwNPlazEzPVhl_LOl7hIdhL44lMx3Cxag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت
#همدلی
امروز
💫
امروز هم سهمی از مهربانی در این مسیر جاری شد…
#هیات_قرار
با مشارکت شما مردم نیکوکار، ۳ رأس گوسفند را قربانی و گوشت آن را در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654525" target="_blank">📅 21:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک به العربیه: توافق بین واشنگتن و تهران در دو مرحله انجام خواهد شد/ انتخاب
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/654524" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654522">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgQte6K4YYEJ_Cecca27tabVFU8LIpkTSTwfm9aJE2Ig8b7Yi2I3UZovHTl3A86fkp_ZwN4F2kfngDfMa899qWEEdzQTT0OAaHlHi90ZNbx1v4lio0U74bdT6B3O16IKmszfxaXevWcxQ0aoWPSZQy7SFhEIX7WFGGiboQfDCm3oIIaRq-EUnTLL7jemNQFi94k-H9NleBzFefwmIFyqveYOGXyLzFHNSkIdhHWjVIaafLD3gvOFfckYPSEe1FtMBrDVSdDqZ9xPopcDkKnBTG3ZGCzPtIvvRIZ5w2TRHZXNgSgBsMoCpSiMFznMGfCoDqMWvSkPDVephh-VfhQrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bccfbe369.mp4?token=Zl24OdHV9Tic4oTQTtTvmpq7WmAhmal9dHOlTm4-FI4Tloa9WsIm6ynBL9D8NrxlxtZ176KzQxhy3XftppqFps_5DFzfrenAATCXx2n_LSND8NTSqmaLVTkSPqqFqp2Y2kJ-aBZhR-A_4y1tsjRpW3kYiPEwTvlcp-aK4izN71Jb4Vt_0sxbZEQwhMAwzwqZu5jqtbaQ0mLDUNiRXdOqETTcSbWVgDeTEx8PeLwwWrMturBAXeXlsnralA4PlnOrzi-1Cp6lgGffBpr-3WawiBMSETOGgUZfr-hD-fC6_vziwI4P00nlGF7NsiUiwS34ZcVlCjiqHrLwAZTnOdyMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bccfbe369.mp4?token=Zl24OdHV9Tic4oTQTtTvmpq7WmAhmal9dHOlTm4-FI4Tloa9WsIm6ynBL9D8NrxlxtZ176KzQxhy3XftppqFps_5DFzfrenAATCXx2n_LSND8NTSqmaLVTkSPqqFqp2Y2kJ-aBZhR-A_4y1tsjRpW3kYiPEwTvlcp-aK4izN71Jb4Vt_0sxbZEQwhMAwzwqZu5jqtbaQ0mLDUNiRXdOqETTcSbWVgDeTEx8PeLwwWrMturBAXeXlsnralA4PlnOrzi-1Cp6lgGffBpr-3WawiBMSETOGgUZfr-hD-fC6_vziwI4P00nlGF7NsiUiwS34ZcVlCjiqHrLwAZTnOdyMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سفارت ایران در غنا به عکس روبیو و همسرش در تاج محل هند: بعضی مهمان‌ها آنقدر ناخوشایندند که خانه خودش بلند می‌شود و می‌رود. به‌خصوص وقتی آن خانه از روی عشق ساخته شده باشد؛ برای یک ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/654522" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654521">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnuHQJnFUSa7xciixbB1lpmayLnwCc9k71beVqJuuDx5kTqQYEUhBAmaQPTXrZuWWhW_u36kFSLgiExvGJdZu5lqjBrXS14GTItVWS4ERrEhIImGlJVa5nyz4zC-dMThzvypJqS4BK25odiUXIeZUyUVqM1yuBT-BTXCbAipcooB38zpky8zzQBj-Fytu2RpRKarDtv10bew9CEF2Wf7PB3QxQy9gFkoUOjEBijSlHgqdiA5bYAudeOU8G0G3nh6KzreVFTCTuVm2mq8C32zrcDztTCP8f-BlfilWPElEXs0nNYozeARIUhsS6DtPDZUMBgGTfof3Jtg-ch81rUhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN: ایران به سرعت در حال بیرون کشیدن زرادخانه موشکی عظیم خود از زیرِ زمین است
🔹
روندی که ادعای ترامپ درباره نابودی این توان را زیر سؤال می‌برد. به‌گفته این شبکه، ایران با بلدوزر و کامیون‌های کمپرسی در حال بازگشایی ورودی تأسیسات زیرزمینی و خنثی‌سازی راهبرد پرهزینه آمریکا و اسرائیل است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/654521" target="_blank">📅 21:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654520">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای یک منبع دیپلماتیک به «الحدث»: پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654520" target="_blank">📅 21:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654519">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQkOs4BqXjkrtqxCpldAYh3lRan2idhtXsCw_5rOlZJ2F0_RS0xvLyvwSsxK7K1sVZ9iGP30IajJ4yVxHPA9EyFDsO8Mp4aJcxIo8EWxNcTj_CejZ9OTzzOMKRXiF3-znNfvNByaQ6VxIIjgk_W1bNGWCGrxrpTO-oVIORkkUvK6BcyPKmq5ri-BRZJz6d9EOs7-_eAsOQ7Ygr04JLsSttTEhQ8V2dGwkbUs82xg7uSjhq1EPazahPvbftGWPAsjxE8rpLX63NJ8DzshpZ9NBgD5gHkrWt5kWKY5IHxOieAE3yHZINYsn-JT-unDxDCWgMImrmydE8pObEnn8NRjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا عمان را به اعمال تحریم تهدید کرد  وزیر خزانه‌داری آمریکا:
🔹
دولت ایالات متحده هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد؛ به‌ویژه عمان باید بداند که وزارت خزانه‌داری آمریکا به‌ طور تهاجمی هر بازیگری را که در تسهیل عوارض برای…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/654519" target="_blank">📅 21:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emnLN1_R7hl_lb1rRDCbBSMTSRE4athNFBOm8pVr-q2hVSVLcVD3eibS0nhwTH5kZelGoi3fg9d3WW7N-bGaESah7jDTYLRpFsqvi1tueIn1h1-pOo2DXfnTCcZxnqzJ08_d2wbMxwZMfFj3UdlpjohxXEV6PFmcLlPWp23pM-OYKCUrK20rVBPs-7XBmUYZjMn-dCQyUsLGTijnTMNCqjx4LKRq2_S9W-8eJfqbEyeHvoCJlO9kSFPcMDfE5fwRMhXdgmHuGVM4Uhe8lI3UVEu_Yo6q8lA4cCWqCe_D-Rc8weIYvFXmJbI-PDeUocTU3WsWUs-04HBszJNsS5XDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آتلانتیک: چرا ترامپ باخت؟
🔹
ترامپ که با وعده «تسلیم بی‌قید و شرط» ایران هیاهو به پا کرده بود، حالا اسیر همان جنگی است که نه بر اساس استراتژی، بلکه با انگیزه‌های شخصی آغاز کرد. او که پیشینیان خود را به بی‌کفایتی متهم می‌کرد، امروز در وضعیتی است که ناچار به مذاکره برای توافقی شده؛ توافقی که کفه ترازوی آن بیش از آمریکا، به نفع ایران سنگینی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/654517" target="_blank">📅 20:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445ef439c4.mp4?token=FFcYR9A06yvEVgZOYVeudG0_XW4OI_OOzGmaSKxNWhFxCkUKCD7a0d48AzFSqDqzzX_8vXy_wy4ZpTqUPGRC1KpwxB71LrETHz6QM7oJMwQnMnGi_t3UzzsQAFaCUrEwV59gOWnURTLGrQLsZ9rUktGScFqkbqyzMLpZNOuypkhaCUThULF6XQn6xVe4xF4xEfP4xqQBjfEkscvyvbwy1Q9JcIHds-JzxmdWdbNGqIhB8xOivMpeISBs9ryop95nent5JuLOoeF4O45LsUYK4354FOEvFtSpynRz7-hk37xKs0wO-TuYfJDUrjP_4KJl03bf_xvfptNm51sn0iCKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445ef439c4.mp4?token=FFcYR9A06yvEVgZOYVeudG0_XW4OI_OOzGmaSKxNWhFxCkUKCD7a0d48AzFSqDqzzX_8vXy_wy4ZpTqUPGRC1KpwxB71LrETHz6QM7oJMwQnMnGi_t3UzzsQAFaCUrEwV59gOWnURTLGrQLsZ9rUktGScFqkbqyzMLpZNOuypkhaCUThULF6XQn6xVe4xF4xEfP4xqQBjfEkscvyvbwy1Q9JcIHds-JzxmdWdbNGqIhB8xOivMpeISBs9ryop95nent5JuLOoeF4O45LsUYK4354FOEvFtSpynRz7-hk37xKs0wO-TuYfJDUrjP_4KJl03bf_xvfptNm51sn0iCKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین پاک، خبرنگار ایرانی حاضر در لبنان: دولت لبنان و اسرائیل همین الان در حال مذاکره هستند تا ارتش لبنان به زور حزب‌الله را خلع سلاح کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654516" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
اتحادیه اروپا خواستار مذاکرات با ایران بر سر مسائل منطقه‌ای شد
🔹
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا امروز پنجشنبه گفت هر گونه توافق میان ایران و آمریکا بایستی با «گفت‌وگوهای عمیق‌تر» بر سر امنیت منطقه همراه شود.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654515" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پزشکیان: به دنبال سلاح هسته‌ای نیستیم، ناآرامی منطقه به خاطر اسرائیل است
🔹
با ذلت، دیپلماسی نمی‌کنیم، اینکه مردم بیش از ۸۰ روز همچنان در صحنه هستند دنیا را متعجب کرده، درحالیکه فکر می‌کردند با دو بمب و موشک امکان دارد یک عده وطن فروش مملکت را با آشوب روبرو کنند‌.
🔹
اگر ما درمقابل قوی‌ترین قدرت دنیا ایستادیم باید سختی‌ها را بپذیریم، نمی‌شود بجنگیم و انتظار داشته باشیم روند طبق روال عادی قبل باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/654514" target="_blank">📅 20:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای یک منبع دیپلماتیک به «الحدث»: پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654513" target="_blank">📅 20:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جبهه مقاومت باید با فشار نظامی، اسرائیل را مجبور کند که از لبنان عقب‌نشینی کند/ اسرائیل بدون اقدام نظامی دست از تجاوزگری برنمی‌دارد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/654512" target="_blank">📅 20:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای منابع آمریکایی: یادداشت تفاهم با ایران در انتظار تأیید رئیس جمهور ترامپ است
ادعای منابع آمریکایی در گفت‌وگو با الجزیره:
🔹
ما تأیید می‌کنیم که ایالات متحده و ایران در مورد تنگه هرمز و مذاکرات هسته‌ای به تفاهم‌نامه‌ای دست یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/654511" target="_blank">📅 20:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654509">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
رادیو ارتش رژیم صهیونیستی به نقل از یک منبع نظامی عالی‌رتبه: بعید نمی‌دانیم که لبنان بخشی از توافق آینده آمریکا با ایران باشد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/654509" target="_blank">📅 19:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654508">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل چند روز زمان‌ می‌برد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/654508" target="_blank">📅 19:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654507">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
عزیزی، رئیس کمیسیون امنیت ملی مجلس: تنها مشکل سردرگمی آمریکا است
🔹
ایران پیشنهاد‌های خودش را در قالب متن ۱۴ بندی ارسال کرده
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/654507" target="_blank">📅 19:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654505">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: دشمن در جنوب لبنان بزرگ‌ترین ریسک تاریخ خودش انجام داده است/ ۶ لشکر بزرگ دشمن از ۵ محور به شهر نبطیه حمله کرده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/654505" target="_blank">📅 19:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654504">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=Ev6wi-rfvMmUbo7DxtNrs3G_ZZGdUO9Xkj0XJX_aRwksLRLHu4D0tpX2zFslq92mkH2CoOUM5EM88e2Pw95-lgkIgy7MJ1Eh3PREQLXb8p0QIhhmIOEnxKf2zFfMRDpWgeQ4WOZ1SyQAdFCexn1IJIVOXmPaniGLBFnokPCZVQiVKIG3LiHBxd2UIkFclPurLbYf87jvPT1vuLXE6E7q4f0Uar9gbybGZw4RnM8CPIvhtpdkeGR0RfbznPAg01RBzBgDvdUknVHI3YwI8OmIAu7g5o90kIIwxBkocVs9CnaU7Mv93ZZVrvjYA9XRzMVRyP56kFD-XphAIwDtN3FvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=Ev6wi-rfvMmUbo7DxtNrs3G_ZZGdUO9Xkj0XJX_aRwksLRLHu4D0tpX2zFslq92mkH2CoOUM5EM88e2Pw95-lgkIgy7MJ1Eh3PREQLXb8p0QIhhmIOEnxKf2zFfMRDpWgeQ4WOZ1SyQAdFCexn1IJIVOXmPaniGLBFnokPCZVQiVKIG3LiHBxd2UIkFclPurLbYf87jvPT1vuLXE6E7q4f0Uar9gbybGZw4RnM8CPIvhtpdkeGR0RfbznPAg01RBzBgDvdUknVHI3YwI8OmIAu7g5o90kIIwxBkocVs9CnaU7Mv93ZZVrvjYA9XRzMVRyP56kFD-XphAIwDtN3FvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم
🔹
تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/654504" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل: اقدامات ایران در تنگه هرمز، قانونی و منطبق با حقوق بین‌الملل است
🔹
هیچ کشوری نباید تصور کند که در آینده از سیاست‌های مداخله‌جویانه آمریکا مصون خواهد ماند
🔹
برخی ریشه‌های اصلی وضعیت فعلی را نادیده گرفته‌اند و به دنبال انداختن تقصیر به گردن ایران هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/654502" target="_blank">📅 19:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fdf2b4e.mp4?token=pNbsQ4heAPk4V6CPqnqVisVZl8npQEtSFDs49gPTVv3QT2UBOzpaf2fCjE1RZQzhMTC6jqyFJwohFw0Z2BjUu2h0ObJaXxNSfqiTylGwBRCmYLIHdh1Yb52bTarnvibjqd9vy7aC1sLZw87opJ7QMixIEzI7pegXptWv6H4PBvqWGxQE7KxLTVT4dRN8sGJ9p7XnhoZAKHaBnQhS5AzvD5gMNtmdRrbrK70aa74cZq4a9F_hvn5-wW9vKko5OcUl5G5cU3V3H_dbT5NUVnTWKc3NpaExuPyVrZD04DchhVRPX6LVlTG24DOPynvZvTECiJO4H3D3MQNJ_JHzgqaGyQiQ5dhZNcuAHvZu33woLx4D9A4ggYqUWwFSDGdxGD0CGVOH09aXryf9G2uAe_HPhNmAKNqEtCIDuerR39KF8R6F6zWqIqURgCvYOtX7ghVXEjtd1ZVtIX1R_Dpqa_kaopYsjSeK94jerOv8lEysJKwkiTBc5P9d2VEEn8051jy3fgLJvHxZDq8UqiRuaUxpQKrsbhRQNdzdcOr2xpZTcrU2dT03pLPcybtZurSzY9lq1Q0o_h8s5cZZP5THFGZ6AY8NJYXw-G15c9KqI9qphHqLYj_9q-ZIl_fKGm0wtgQFj_qUoFFiPxNlGBKndFuhpDpAL3D_OMHTFci3oukZZd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fdf2b4e.mp4?token=pNbsQ4heAPk4V6CPqnqVisVZl8npQEtSFDs49gPTVv3QT2UBOzpaf2fCjE1RZQzhMTC6jqyFJwohFw0Z2BjUu2h0ObJaXxNSfqiTylGwBRCmYLIHdh1Yb52bTarnvibjqd9vy7aC1sLZw87opJ7QMixIEzI7pegXptWv6H4PBvqWGxQE7KxLTVT4dRN8sGJ9p7XnhoZAKHaBnQhS5AzvD5gMNtmdRrbrK70aa74cZq4a9F_hvn5-wW9vKko5OcUl5G5cU3V3H_dbT5NUVnTWKc3NpaExuPyVrZD04DchhVRPX6LVlTG24DOPynvZvTECiJO4H3D3MQNJ_JHzgqaGyQiQ5dhZNcuAHvZu33woLx4D9A4ggYqUWwFSDGdxGD0CGVOH09aXryf9G2uAe_HPhNmAKNqEtCIDuerR39KF8R6F6zWqIqURgCvYOtX7ghVXEjtd1ZVtIX1R_Dpqa_kaopYsjSeK94jerOv8lEysJKwkiTBc5P9d2VEEn8051jy3fgLJvHxZDq8UqiRuaUxpQKrsbhRQNdzdcOr2xpZTcrU2dT03pLPcybtZurSzY9lq1Q0o_h8s5cZZP5THFGZ6AY8NJYXw-G15c9KqI9qphHqLYj_9q-ZIl_fKGm0wtgQFj_qUoFFiPxNlGBKndFuhpDpAL3D_OMHTFci3oukZZd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جنگنده‌های اسرائیلی حمله بزرگی به بیروت کردند و خط قرمز را شکستند/ یکی از رسانه‌های اصلی دشمن می‌گوید هدف حمله یک فرمانده ایرانی بوده است ولی ما اعتنایی به بیانات دشمن نداریم و منتظر بیانیه مقاومت هستیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/654501" target="_blank">📅 19:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654500">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
الجزیره: اتفاقات اخیر تاثیری بر مذاکرات ندارد
ادعای الجزیره به نقل از یک مقام آمریکایی:
🔹
رویدادهای اخیر در تنگه هرمز تهدیدی برای مذاکرات با ایران نیست.
🔹
مذاکرات در جهت دستیابی به توافق ادامه دارد؛ اقدامات نیروهای آمریکایی در تنگه هرمز و حومۀ آن «جنبۀ دفاعی دارد».
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654500" target="_blank">📅 19:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0CzWVXF7nixPlxS6aO4VO5OzuzxkIrzDhaWB8H6yeO65ZTdBTXM5XZkO28_U0gvNXsF4D-5TQ2dLAbliaEYMJj9HkCCkl7PY87E_sWOsAXS5Mqd59zHzvxCsMGViu6JnhVIG3Hjvwx9ekTemVlEWSC2eQDHHfWNQssoGNffCYnVAhS1hevNi-om1rQES4R84HQ8EkoJO8TRhKe7MKXDTDjTQxVlCtqifcxYZDRUqBjUKUT7RjjiKIXfAZSuev-1vZHPNFlTN60TiekTimiCfm43hqVYekjcp5CbW9MMX5xAPvYYnfNQqm5oGPep_XED9UYi4mL_mlrX9Oy0LGgkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت‌های تیروئید کم‌کار و پرکار در چیست؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654498" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9gwkPP6zSG-QSTZgP3hO4y7G5pE9zBRl6Ge5rezUHo200KzJVmH9mVABtffCrgQ4PiJKu1X8A-QAiSh1DP4csiw_rkeSX_UPaJ-VvlWbi6_yGFOFx9GvmD-tuGsbjQUf7GODi7Me9Z6SD9D4bRqK6ZOSLdp_h6uf4Db3UBYq_nTWrXRcqCbaGHGv6EYquYUMWIn-K0H7gI5q87wpBJWYpkk9k-AkLiYGVtAGTRwXJmMOi75SVDYZfgx7ziAxuB1p_a1Jq0vAl1rcEQ0fB2v216kmmVUbbYxP_8RdUkfK6lrI1RlhYFfQU-_yWVggu3DgHqP8MB1cBIlpJ_MTDq-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه NBC: از سرگیری جنگ برای ترامپ سخت و پیچیده است؛ زیرا اهداف نظامی باقی‌مانده در ایران یا زیر زمینِ مخفی شده‌اند یا متحرک و دائماً در حال جابه‌جایی هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/654497" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نگران نباشید؛ ابولا در ایران نیست!
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
سازمان جهانی بهداشت شیوع ابولا در جمهوری دموکراتیک کنگو و اوگاندا را به‌عنوان وضعیت اضطراری بهداشت عمومی با نگرانی بین‌المللی اعلام کرده است.
🔹
با وجود محدود بودن کانون اصلی شیوع به چند کشور آفریقایی، همه کشورها باید آمادگی لازم برای شناسایی و کنترل موارد احتمالی را داشته باشند.
🔹
تاکنون مورد قطعی از این بیماری در ایران گزارش نشده است؛ نظام سلامت ایران آمادگی کامل برای شناسایی، نمونه‌گیری و پاسخ سریع به موارد مشکوک را حفظ می کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/654496" target="_blank">📅 18:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
آمریکا عمان را به اعمال تحریم تهدید کرد
وزیر خزانه‌داری آمریکا:
🔹
دولت ایالات متحده هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد؛ به‌ویژه عمان باید بداند که وزارت خزانه‌داری آمریکا به‌ طور تهاجمی هر بازیگری را که در تسهیل عوارض برای این تنگه نقش داشته باشد، هدف قرار خواهد داد و هر شریکی که تمایل به آن داشته باشد، مشمول جریمه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654495" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo-tJvc5SWJk0jxANLK3R_SyXxFFQoZ2QEp5xCZqDKc3n66hMMWj0m9RWSMdK6Ke1ASmy-fzgCDA4Oz5CANZxNKCfoVGNlEVMTYwu9Sd7I6GPaH61WHcuVMje2EIwqxbo3mt8dWKwpPdgPa5p_hJTpD_tTRJt3JPzSsTdj71fjZnEmSI9d27uWbBEG3f6j8GJGROodlNweLrc6GsbZj57BK4I3qUKfbMORs5WsUx1K35Wv50QZlYNvnPsCP1dQF1WjCcWIc2XTQ_ovJ1nUYAa61go8jWN2OegYUtzESv5HYFo5ojQoBHJNQgG7cHZfeOm3zT_MUyk1IQHGPu-1Ma0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملاصدر؛ بزرگ‌ترین فیلسوف اسلامی
🔹
صدرالدین شیرازی، فیلسوف عصر صفوی که فلسفه، عرفان و وحی رو با هم آشتی داد و مکتب «حکمت متعالیه» رو بنا کرد، دیدگاهی که بعد از چهارصد سال همچنان پابرجاست.
شاهکار ملاصدرا نظریه «حرکت جوهری» بود؛ یعنی کل عالم مثل یک رودخونه، لحظه‌به‌لحظه در حال تغییر و تکامل درونیه و هیچ‌چیزی درجا نمی‌زنه. ملاصدرا به ما یاد داد که تک تک اجزای دنیا، زنده و پویاست؛ فیلسوفی که نگاهش به هستی هنوز هم تازگی داره و اندیشمندان زیادی رو حسابی به فکر می‌بره.
#نامداران_تاریخ
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654494" target="_blank">📅 18:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده   اکسیوس مدعی شد:
🔹
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند/انتخاب…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/654493" target="_blank">📅 18:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته مقامات، آمریکا و ایران به توافق رسیده‌اند اما تأیید نهایی ترامپ باقی مانده
اکسیوس مدعی شد:
🔹
مقامات آمریکایی گفتند که مفاد توافق تا روز سه‌شنبه تقریباً توافق شده بود، اما هر دو طرف نیازمند دریافت تأییدیه از مقامات عالیه خود خود بودند/انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/654492" target="_blank">📅 17:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
گزافه‌گویی
مجدد
نتانیاهو: ما باید ماموریت در ایران را تکمیل کنیم و من تقریباً هر روز در این مورد با ترامپ صحبت می‌کنم
#Demon
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/654490" target="_blank">📅 17:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
علی باقری: آمریکا قابل اعتماد نیست
معاون دبیر شورای عالی امنیت ملی:
🔹
نمی‌توان به آمریکایی‌ها اعتماد کرد؛ چرا که ماهیت آن‌ها بر پایه نقض تعهدات بنا شده است.
🔹
ایران در مقابله با تجاوز، بر توانمندی‌های اعلام‌نشده، نیروهای مسلح و ملت خود تکیه دارد.
🔹
دلیل پیروزی ایران و ایستادگی‌اش در برابر تحریم‌های غیرقانونی یا تجاوزات نظامی، در توانمندی‌های داخلی و پشتیبانی ملت ایران نهفته است.
🔹
علت اصلی بی‌ثباتی و ناامنی در منطقه، حضور آمریکا و رژیم صهیونیستی است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/654488" target="_blank">📅 17:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: در صورت عادی شدن شرایط آزمون‌های نهایی از ۲۱ تیر آغاز می شود
کاظمی، وزیر آموزش و پرورش:
🔹
برنامه‌ریزی لازم برای برگزاری امتحانات نهایی در دو سناریو انجام شده و در صورت عادی بودن شرایط کشور، آزمون‌های نهایی از ۲۱ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/654487" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBz6dqSpOFo10uZLiOlofVDzwxYR_bBR8lvlGBB15UQ-7NjQaW9sAkJRLByBKq5OHn5hiXh0lShOtWPa5jRpcnQBg-JKLTuxOwWR6rQw45hTMd4QRn0GP7fXI_eDn6HHoXnnrP4G5xXEv0Wf7s7hl-5Mmhki3evWilPC7E5H5swFnkPuuBZUuVrJlX80PhBa9ol9Y3vlTSsfmRUYcgn5DzmEgoQKJyow-EugIFN8UfBKZZ0xsfEWwcyZXQ_A_knhJMdRVgTAkSj3LnyJEShbtaXbw3h2mRuvm_lgy6eM94O7NTF2RcHv0AWD75vMku_WlKnzzmyLUJmkZAcW8jYwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شربت‌های سالم و مفید برای داغ‌ترین روزهای سال
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654486" target="_blank">📅 17:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c85fa8037.mp4?token=qP4AdMDS1zBCJEU78SEwD2Eu0lXSveK51KS1wLjXLdSayRoqLOxxNFd-qZvV_uVrS3go-C2IpPZ13v3GjtJVDk_ci0ed6R5h9uO6M22gLp-GXO09liBF1CoF-_zeQNlLlaPTBL1PlQGNYDwYHBw174LfJBo09QqwKuLgotojnStkwoWCD2z8eN6w1DjLY2bY8szHGQOR_ff9H81m3JKZhGG7OFSQlMfNByJJWHCR6Q4_el5M4LWBJttiZhBN4zpcHXVRIactRICfav9TI0Li3-LL-zF5gG-MEWp6UhxNJJVYz8GPNuMbFT0j9t4zbf8FpykkuKO8jZZsNxO6v9g4miFcdNLZoHnpza1c-QRcQASKhFmLV95GL5-BY96unUQiZ91Ey19BO3AywL_JiA1I-3-p2OlpRFkuigO062AkCMKM9AsF--h4tFh_S9cs0saZ4FgOl5V33atziR9J22JoUve_DZpWQmMyRFQZhmA8s_YCm_hsrL35XntyocQ6JBV4qb2dxz1jZm9wg3QgjdiJvBAZlvjnRjTUxvoDkGPHWT0dzJD5rCVl9Wbqn4B62W0e9cBIzUlpLEMGtQKOb-hLeXr5mBH81KSnf1vCsVdCQwWvBmkC34dVqFRgmyrMKEkg-5qdEXEHAhaUTMuGqE-C1qqrbiQDrDUzBgJBhWhpYTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c85fa8037.mp4?token=qP4AdMDS1zBCJEU78SEwD2Eu0lXSveK51KS1wLjXLdSayRoqLOxxNFd-qZvV_uVrS3go-C2IpPZ13v3GjtJVDk_ci0ed6R5h9uO6M22gLp-GXO09liBF1CoF-_zeQNlLlaPTBL1PlQGNYDwYHBw174LfJBo09QqwKuLgotojnStkwoWCD2z8eN6w1DjLY2bY8szHGQOR_ff9H81m3JKZhGG7OFSQlMfNByJJWHCR6Q4_el5M4LWBJttiZhBN4zpcHXVRIactRICfav9TI0Li3-LL-zF5gG-MEWp6UhxNJJVYz8GPNuMbFT0j9t4zbf8FpykkuKO8jZZsNxO6v9g4miFcdNLZoHnpza1c-QRcQASKhFmLV95GL5-BY96unUQiZ91Ey19BO3AywL_JiA1I-3-p2OlpRFkuigO062AkCMKM9AsF--h4tFh_S9cs0saZ4FgOl5V33atziR9J22JoUve_DZpWQmMyRFQZhmA8s_YCm_hsrL35XntyocQ6JBV4qb2dxz1jZm9wg3QgjdiJvBAZlvjnRjTUxvoDkGPHWT0dzJD5rCVl9Wbqn4B62W0e9cBIzUlpLEMGtQKOb-hLeXr5mBH81KSnf1vCsVdCQwWvBmkC34dVqFRgmyrMKEkg-5qdEXEHAhaUTMuGqE-C1qqrbiQDrDUzBgJBhWhpYTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت نوزاد گمشده پس از ۳۴ سال جدایی
🔹
کایل آدلر، آمریکایی اهل شیلی، زمانیکه یک نوزاد بود ربوده شد، پس از ۳۶ سال با مادر واقعی‌اش دوباره دیدار کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/654485" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI8EN0_osPpSIKKLSW3GsT3s50Cx4UszomgR60-6Hyb2CVl9KTekAWlYxeK14hc6dCWVgciAQTm3tIGtRMxKhVc22z7khHjkQrZyKR-XwHHK17qa5KUMUg3t0ImGaH61r_Z-jqfTl0K_EKVjO2LXu4Ekw2YrzQGsfGu4txK3xKHsYuEgv-tYx8dO1vrkvgFefx3XbxHbO57hWQiaRFGJ3Oa1zgOL9vCgz0vRM8YDOx02h1R8HHqroGGMwZa6wjeNCaG8Ydyt4KAEPS_zapL5jAor64YAxFZUbv6TIuae4E-aQoceRoBmnYGcEnpTHQ614j4hFpgyBLUuNeN80IIRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ عاملی که سلامت قلب انسان‌ را به خطر می‌اندازد
#سلامتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/654484" target="_blank">📅 16:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCwQ_rSJElzOhjf2qed-UQj1_Zo9RYXbl2qt47_bP7svfSM-uQdi_BULKbp1cVGWxlqZsnpNIqesqt4D61_BK9oDYVvEyh1vHMxiYm6yryE4KjknV-L3HMpF_zwG_7PpBCbIRjhBJmbaCLL2HAvG6jGUpxWzcK4jbFoWUgRqxhkXXjDKgnS3vjpttfqZw_CriJ6tcHLPp-fzrsPEPbK7VzMBGfq7FpsfWyLht0QhgXoI8_BbUGcCmQjX6y5E1tRafwblWoTtLNwtiICTrqjaL_4QoGSznkwo4np78K9PHxEJLZk1t73OWfFJKJS8gyIlSG-dk87pJSrWkFnoyKKvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
فرصت ویژه خرید از چرم مَنطِ
تا %70 تخفیف
➕
%10 بیشتر
و هدیه 1,000,000 تومانی اسنپ‌پی
برای خرید «حضوری و آنلاین»
کد: PAYSS9R
حداقل خرید ۴ میلیون تومان
مشاهده محصولات
👉
manteofficial.com
@manteofficial</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/654483" target="_blank">📅 16:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk4HaLICCCEp49pob2LHRm1QLj1COsTylV5uOJui3ttN0T3Os4BFiV-K8_dT71xUN9S4pOrW8Z-7REhmwAMNfebVpWowwXuZHOg6c8_8J96XfyIapI9FPEMdKNuJ4DwAgV8r6Ll0PTfLcbG-trz5g--F615fagrjBMxDj9JpkRBlWz95q32oX2udLBNJ3HvNS6tnTP94rHdr3xenSU7qwDWdbDm61dSVwZkIGngSBPobfUgVp7DC6lYC-3LJJPkyu0RW6ZCgQFDL3dl7YhFz3LBJoc169goxIHP42TtBcOmYT2dg-Boml0fTMbe6jVpucng6hC9-X84Cu30c9SUvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قصد دارد چهره‌ خود را بر روی دلار حک کند
واشنگتن پست:
🔹
مقامات دولت ترامپ دفتر مسئول چاپ پول کشور را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که به گفته آنها، اولین حضور تصویر یک فرد زنده بر روی پول رایج ایالات متحده در بیش از ۱۵۰ سال گذشته خواهد بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/654482" target="_blank">📅 16:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فرار گوسفند قربانی روی پشت‌بام ساختمان در الجزایر!
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/654480" target="_blank">📅 16:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a04ecddcd.mp4?token=qbmZhSMFNiaAFMuRczY0fEIM-QngctjP2-WniayOnwSRicaeJ-3gEi4erPAz6ZOo48xWDO5wZe5Lt_ZMe3oqdVpnA53vQgxzqNpZ5PgTzFAD8K5bi_oe1eELq2VrM_e8Zh5L8Q4U2P35BlzeAi-c4ZAel5ieHvTCc9zX8mmgehPVNeEVtpbOARpER7OIHV-tQbiUvRTmphRDCo2GERzV1OJkLSw_HnYI8oLHC5zzBVFgWYbrxca91sthDPLLyTZz6NuTFovNi6-KlhAGviMoHgYaRdItnyf6apeOA0x1se_FbFLGKA_DEpAtCcMU-RnRRRO_wcEOvUFUs3bQYE63Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a04ecddcd.mp4?token=qbmZhSMFNiaAFMuRczY0fEIM-QngctjP2-WniayOnwSRicaeJ-3gEi4erPAz6ZOo48xWDO5wZe5Lt_ZMe3oqdVpnA53vQgxzqNpZ5PgTzFAD8K5bi_oe1eELq2VrM_e8Zh5L8Q4U2P35BlzeAi-c4ZAel5ieHvTCc9zX8mmgehPVNeEVtpbOARpER7OIHV-tQbiUvRTmphRDCo2GERzV1OJkLSw_HnYI8oLHC5zzBVFgWYbrxca91sthDPLLyTZz6NuTFovNi6-KlhAGviMoHgYaRdItnyf6apeOA0x1se_FbFLGKA_DEpAtCcMU-RnRRRO_wcEOvUFUs3bQYE63Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از فرماندهان مقاومت عراق ترور شد
🔹
جنبش انصارالله الاوفیاء شهادت فرمانده «عدی الحلفی» را در پی انفجار بمبی که خودروی حامل او را در استان میسان هدف قرار داده بود، اعلام کرد و رژیم صهیونیستی و ایالات متحده را مسئول این حمله دانست.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/654478" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان به آمریکا می‌رود
🔹
طبق اعلام منابع پاکستانی، اسحاق دار، وزیرخارجه پاکستان، در تاریخ ۲۹ مه (۸ خرداد) در واشنگتن با روبیو دیدار خواهد کرد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/654477" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcCUGdqEKumrPWqZcG6Xwz1FIbdvOKr4XeMYVWXC-stMvz3ooyFB1ROhSfa2BpPXtfVRBb6JX2Dytvsr3qJARMY5gvu1wTMQaTe53wvN1u9rSnbd5ArTciDl6cvKY0I7-_GR1qjBirPEIZ3-j2MXP_CcPodX1aGrGpft1y5O4yUpS_BA5r2fBGQQIp8Z4x1gwYqVr_h0u_fGA14-rijqeV2fsfdYowT6GKzp9A8KUTT1BJx3F6wC336gAWlPJioEPUrMNGS-Beod72EmdasyyHZ05tv4IqfCNjynbVVDFf15F5LZrD8qxsm6_cUWcdBQKhSL2Bj9aDO8ZX-6P-EUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه بابک، آذربایجان شرقی
🇮🇷
#ایران_زیبا
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654476" target="_blank">📅 15:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6fDH1QQ7ATvcZrSul11cD7QccuNUWAl_4XZEAWA7EtWWlHd2zoW3P9mOmj35yZtlm8nodCWIfAyth61x6RpFlqEfGhNHNXjGH-fz5rDLMqZYCe6tkUmqhSWPJfIA9h688ZQJRhCP__-P7g7l9rCn3YmmLz7mv8K4fcxcOQiZxM36xvMTLaTocpA-g0j2XZ0GdbbOdbYExwUPScaEqgskNIM7wYpfmcUDp9sTqR1XKKPkJDljbVyCvBNtrYJE6S59b9OzpGqH07FVdMz0ZAraXPetdIWNzHH2wY5HibHw2ELix3ZXXl4fKInDqU56mP71Ki9t_qvjA-tK8yPlMMBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام به سربازان خود در خصوص استفاده از مرورگر کروم هشدار می‌دهد
رویترز:
🔹
فرماندهی مرکزی ایالات متحده در نامه‌ای به تاریخ ۱۴ آوریل تأیید کرد که نیروهای آمریکایی در مناطق جنگی، به ویژه در منطقه خلیج فارس، هدف حملاتی با استفاده از داده‌های تجاری GPS قرار گرفته‌اند.
🔹
قانون‌گذاران هشدار دادند که این داده‌ها می‌تواند برای هدف قرار دادن نیروها با موشک و پهپاد مورد سوءاستفاده قرار گیرد و از پنتاگون خواستند اقدامات حفاظتی مانند غیرفعال کردن شناسه‌های تبلیغاتی و اجتناب از استفاده از مرورگر کروم را انجام دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654475" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR1SfmRXt2l6NdsI_1xRQu7ksyRY-vwAXp9tLOA-Lyxgrzj0aJS5jkPC1AacrhzuUTrPluqq4pPMd95QQz07WpR6VjCtw8IWWP312R6IOygmumdB1NaSBCTDFSzT7tXrPDVxb7tVWVSBRBg7Gh1rjJM033FYXrO95YZGf9g9UyjwCkeYIJAJEiq2jHvHO9cbuElAonx3erpXwWoMItR1OdcTAZwX55EK-_pO73zySdce8MxtAw6yjtiR98jIeZwNTtK4bc9XqYRiWgDhA9XDrgztpBTbaQR1bjGdwE7AbGJOjVrevWKsLX-ZUyQK3g0kXg2KBw9y3BclGWgcLgHLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لوگوهای تیم‌های ملی حاضر در جام‌جهانی
#ورزشی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/654474" target="_blank">📅 15:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMuD0BGMJYCfzD7mIaRxmSobHghlKY4cwTffNZBFMu9Vh-MNrCafjot6UAca3NdSZQgrs-fWeuhKRLhCNfE1dNNz8ibxIP8wxn_2btkO72F7TjPiEfNgrNmy381-Qj0anvTdkwHTPhzAP-nB1YL1FPYSEEoLrdw3mBP4lCVRmCuIDvo8otgpfjPs-ThyvihR1SfH55QIIbbUemrvIcCz3YdmEshabOSuCDmg1wKaipyckDuSmpkZxZsMiQ2yWRisYy58TRbbsWU9rVzQby3_v9tfyi9JLKZcqQ563lIsqnvBxAgfV8w9XO5qPvmwFCgaAMpCNl63ecE5PeU8EZoQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا مدعی نقض آتش‌بس از سوی ایران شد
فرماندهی مرکزی ارتش آمریکا (سنتکام) امروز در بیانیه‌ای درباره درگیری‌های شب گذشته در آب‌های جنوب ایران، مدعی شد:
🔹
در تاریخ ۲۷ مه ساعت ۱۰:۱۷ دقیقه شب به وقت شرقی، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.
🔹
ارتش متجاوز آمریکا ماجراجویی دیشب خود در آب‌های جنوب ایران را «نقض فاحش آتش‌بس» از سوی ایران خواند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/654473" target="_blank">📅 15:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه  روابط عمومی نیروی دریایی سپاه:
🔹
کنترل هوشمند تنگه هرمز با اقتدار کامل در حال انجام است و طی شبانه روز گذشته ۲۶ فروند کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگه هرمز عبور کردند.…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/654472" target="_blank">📅 14:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست
🔹
پیگیری‌ها برای مشخص شدن آن ادامه دارد
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد
🔹
اخبار تکمیلی…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/654469" target="_blank">📅 14:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه
روابط عمومی نیروی دریایی سپاه:
🔹
کنترل هوشمند تنگه هرمز با اقتدار کامل در حال انجام است و طی شبانه روز گذشته ۲۶ فروند کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگه هرمز عبور کردند.
🔹
دریافت مجوز و هماهنگی برای تردد در تنگه هرمز یک امر قطعی بوده و همانطور که قبلا اعلام شد عبور از سایر مسیرها به مثابه اخلال شناخته شده و با آنها برخورد می گردد.
🔹
ارتش تروریست امریکایی در منطقه با نقض آتش بس اقدام به پرتاب چند تیر موشک به نواحی خالی  فرودگاه شهر بندرعباس نمود که هیچ گونه خساراتی در بر نداشته است و در پاسخ این تعرض پایگاه امریکایی مبدا تجاوز مورد حمله متقابل قرار گرفت.
🔹
در صورت تکرار این اقدام ارتش تروریستی امریکا با پاسخ  سخت ما روبرو خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/654468" target="_blank">📅 14:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: نمایندگان ملّت تمام توان و ظرفیت خود را برای حکمرانیِ هم‌افزا با دولت سایر دستگاه‌ها مصروف کنند
🔹
در این میدانِ جهاد، صندلی نمایندگی، به‌مثابه‌ی سنگرِ خط مقدّمِ تحوّل در مسیر پیشرفت کشور، قلمداد می‌شود؛ لذا شایسته است، نمایندگان ملّت، با اتّکال…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/654467" target="_blank">📅 14:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
قولاً و عملاً، مظهر انسجام و یکپارچگی ملّت باشید
🔹
لازم است تک‌تک جان‌فدایانی که، دلشان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد، از این پس، بیش از پیش، برای پاسداری از وحدت صفوف منسجم و به‌هم‌پیوسته ملّت، اهتمام ورزند و اختلافات غیرموجّه و…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/654465" target="_blank">📅 14:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
♦️
رهبر انقلاب: مجلس نقش مهمی در اِعمال اراده‌ی مردم دارد
🔹
مجلس شورای اسلامی عُصاره‌ی ملّت، مُظهر مردمسالاری دینی و رکن قانون و قانون‌گذاری در جمهوری اسلامی است که نقش مهمی در اِعمال اراده‌ی مردم دارد.
🔹
اکنون با سپری شدن سه ماه، از دفاع مقدس سوم، عیار باطنی…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/654464" target="_blank">📅 14:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‎‌
♦️
رهبر انقلاب: از تلاش‌های آقای قالیباف، در راه اعتلای کشور قدردانی می‌کنم
🔹
عید سعید قربان و سالروز افتتاح اولین دوره‌ی مجلس شورای اسلامی را، به همه‌ی ملّت عزیز ایران اسلامی و نمایندگان محترم مجلس شورای اسلامی، تبریک می‌گویم و به این مناسبت، از تلاش‌های…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/654463" target="_blank">📅 14:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: لازم است، مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد
🔹
آیت الله سید مجتبی حسینی خامنه ای در پیامی به مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم : در مقطع…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/654462" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654461" target="_blank">📅 14:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پیام_حضرت_آیت‌الله_سیّدمجتبیٰ_خامنه‌ای_رهبر_معظّم_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">131.9 KB</div>
</div>
<a href="https://t.me/akhbarefori/654460" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷ خرداد ۱۴۰۵
🔗
https://farsi.khamenei.ir/news-content?id=62984
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/654460" target="_blank">📅 14:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654459">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آزمون سراسری ۱۴۰۵ و آزمون دانشجو معلمان به طور همزمان برگزار خواهند شد /زمان دقیق برگزاری این آزمون‌ها ۲۰ تا ۳۰ روز قبل از برگزاری اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/654459" target="_blank">📅 14:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5753456ce.mp4?token=XddiU8WWrzzSyGo2IWbpvay-dmE5cGWGbYvqH6BiN_h2XyjCaAkRwh_YxU5uA6LBnl9YqtFgT1aB_dRyiG5R8Q2hdAzfpI_V9N9hHglU-Aq4_EMmBhqAhl-FdPFVsiv5dWEJT2LCAQ4y5OC1dze3pQ0f2MKSyqfPs7teYP1oZFSRB5bWzrvUyvrO503eVJh4rHnKDK0g2j0QaDDAr_4krCq9JGYGukqPFw-pCGdsMjYc2GVpbPOcPtlVl709hgzcnIJ5cTGBTohKK25CvVC-JX67QYNOAG2o7wH0f1WhSJyTC3c7AYeVsjAc-DoU_ZRguOWsMD0ZfaBeINrEgwRKrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5753456ce.mp4?token=XddiU8WWrzzSyGo2IWbpvay-dmE5cGWGbYvqH6BiN_h2XyjCaAkRwh_YxU5uA6LBnl9YqtFgT1aB_dRyiG5R8Q2hdAzfpI_V9N9hHglU-Aq4_EMmBhqAhl-FdPFVsiv5dWEJT2LCAQ4y5OC1dze3pQ0f2MKSyqfPs7teYP1oZFSRB5bWzrvUyvrO503eVJh4rHnKDK0g2j0QaDDAr_4krCq9JGYGukqPFw-pCGdsMjYc2GVpbPOcPtlVl709hgzcnIJ5cTGBTohKK25CvVC-JX67QYNOAG2o7wH0f1WhSJyTC3c7AYeVsjAc-DoU_ZRguOWsMD0ZfaBeINrEgwRKrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی شهرداری تهران: مترو و BRT همچنان رایگان است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/654457" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pX31cl19t7i6RVmZivlLe9t1VBPQu0q9EY7ZprYhLgLJJ0IYhzOf9QXhFr6AacmfkKVIND_26YDrT5987lkPaZrAIC9Y28KpuGIR0L4LwPisqOEbgkwTcbH9Qoir_UCDjLvcVieC64Zga6aGbBsj7IiAkEdymwHiF3cWNOYFoS_5WXg1X3NqEAzG5d5p4bNN5uH5g_LHVlDXkciRBweSIf45VTtsX6z2q43o3n0b0DeVTj3vVLnaP0aJkPcwsLXrVRRsvt4Vr-GdDvMMz1G9m8O-N8Kn1_mTBmqjfMzvTZ5K-746B72No0OXeiVyaiejQzImjHcPQaYVStT1SsnPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBFn-XtANa5PFDsISsuQtVDBMR5Dc1VFCW2dSB4_Hm57xdsgLi-h02WErx8WlTZEQguCQ6Vf0FoTNf9vInPIA4skd0REpPx9spvjB38yHk3q_tgpauez7KK3o_040_J9pIlR1E3XPARlaAAzMN0WVBojte9DBpburcYd2z0ovEQ_140L1Yq27c-vVHTDXjrz8d8yEC8RIkNd4oFD00eHvuhFuy_qrNP8oEvq_E_P6SUPpOZO6C-YOYAm1uTQI5CIpf0RzzueToR750j7TkahV52r4_7pYJPMHEBok7tiTY_kvnhRliEE9BMOP4VMOp4UuVfNI60o8IEth8-QZ1RMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0WkabYMXt8EkKSrvo6EHH4hOIDtaFjt7gUg0j3dH7eW5gH81ou3-GNltPdLPCC5I_IPAZ0HOrPEkKttQvJNv-qcQi_4AICDzqy6Epm6zI0tC2QYvG5CrKE8G0_N8PFwbBBlU7wleRS5wlatmnlw8PzkUilWEhIws_SQBlrVqzdg7rkeofgLBLs-jIT2GSXhKbNJMHhSkhd5CIogzbpElhXGo26fJrYwUYwPqsQJraqRdknSUG6qaVXpLfb7pceHWWYa6oJv_JTEBHuIZron9jNPeDzNRCYzeMl8IB53Xf-JdEY9mJsXvR7E3TbMqen_gSXftAek2by2ecLEHDIcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oi9h2a4nFRaufRXUOyEmRsOCjpP_-5F3LPhD-0pwULCaIhBn-kDGPHal7_5tO_S-G5wcMX2rPdJJr0BYQkRcWsqUWZ6ieDYsDG2DkmwmShArvR81kt_ioL2bznukpTG2R_0VFxH9Vw8dytLhHsUQoMaWJL0ud9jd6Bse1mY0rObMn8JvLEIKIoDD8xaQpp3WBoh8fh1sGEQ8Q-0H3Aw8N1Vidny2XthVypdAaInQPk8w_EjHSxRYZ-CWwcGl0kkytitogvbA6z8o8YReC5DmUJAHl6pIIlTJvZ23DFLYYQAu4FaQ9WWbsOYgkCESkrtRETjfgutB7psakRRWE-tT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unQed0qL2wsugrGC1PfhWY6d1eV59V5X7U3RwuXceC0xTMz7Xlpo1wtswW6fvZFqt4JXTixo1R6Lvbz2KA891hI_kfqP5HiuJNkDAgelSVkYAqwwlJ4sAZxVt8v5yC_ZbYTciwJq824XbTokz55pS7_v1N8YMUtIOuhUGjb1Az37UoxpPs0TMaW4gD-lv-bEcL0dT8afTp9yq9Oyef9xUxx3BFM5GlfUjLPXk-xt6WkLt-OXRCa1zhyIjVbGmygCCxMb74gm9qLwHuPvFxGlhZAvsZOt1aQ9n29kRHQMAwZIAjd-hLmk6FbzKZWQ-6PiQuIpvamgIy620F-V6ErXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zdt2tfszPexLh6sy3MLG5nacxeyNuTKmFkUfVqWKtNZ8uq8JJxMwSyxADo78bK3Beyl9MVQHPOeZCzwoBN8j_g48rXO0fs1UIVhQckWq8geyECkzYbwpUCHxA1Lv5uc9wO1lKzS3YhBQphmCsySUNi8p9twB--OSB6HhMvv-9nYHnTyhNX7XsithWyxEO8dBjOaumNyei9px-VcNbTqe7DLWJPHMhfiOuTG94makU_S6QEldnTwgicO12DQV878MT3sdWKgEopKfADL3fUvg9PcrhrtfBs8Hb_nIFKX69BxD6UF0dsBtFwxh9CFMryQJIU6L6LkfRxy9QGx2lA4apw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های اسرائیل به توافق احتمال ایران و آمریکا
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/654450" target="_blank">📅 13:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297ec41942.mp4?token=hCyZMxiULX1FMRsUTRxhKdC8Pm4vBjWKtxe0jiyv2JV_hvgyJqAvrp5b03dLDxSvzWhkva4pLyyAYZdQB7oUQD0ySTPYw-yQ5hAlECt35KstGl5T4wJtw5wEk1DgcnKlIwjMKNqikFiDaqwNFKEbDbOa_i44o8heiBvF9953s4Ib3U1smlj1QEgiR1zSZSkDhca4YgrcRmuZ_vvgFFyisykjjohw73XLyzd_WsP8v4qtitLHEHZNSCrtYs9qABmeVnPbFVGZ-5AKMmi9TZmDqpzcRTxzh-xFerlAEjleMGw-i2K_5Y9WjIxC1-0LtLmZ221SKphrTswINnhTxye6Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297ec41942.mp4?token=hCyZMxiULX1FMRsUTRxhKdC8Pm4vBjWKtxe0jiyv2JV_hvgyJqAvrp5b03dLDxSvzWhkva4pLyyAYZdQB7oUQD0ySTPYw-yQ5hAlECt35KstGl5T4wJtw5wEk1DgcnKlIwjMKNqikFiDaqwNFKEbDbOa_i44o8heiBvF9953s4Ib3U1smlj1QEgiR1zSZSkDhca4YgrcRmuZ_vvgFFyisykjjohw73XLyzd_WsP8v4qtitLHEHZNSCrtYs9qABmeVnPbFVGZ-5AKMmi9TZmDqpzcRTxzh-xFerlAEjleMGw-i2K_5Y9WjIxC1-0LtLmZ221SKphrTswINnhTxye6Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز زمینی مجدد رژیم صهیونیستی به خاک سوریه
🔹
منابع خبری از یورش زمینی مجدد ارتش رژیم صهیونیستی به جنوب سوریه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654448" target="_blank">📅 13:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpQCK2cRP7Nb8IWW1sAj0p92OO8P6Ma5vfOIcU3IiO0pwipuXnIQy3w8p2Bwr3j39px3ybRF1BshBjPMLTAWzkdwTQLT31jxpMNKgWJG7ybi36QEG25kSd-PbPjmRdimfFqpAaR81R5b8hjrBAyUoPOi4LillY-YdsKZJJbr63qjUFveX3nubIFCAdwmboYbxgDLh8gyCJMCxjri6N8zY8y4dlACwG2mxC748D6CuMGgcxL7Ntwxa93b9gyR_74y-nSLG975AFzJTiE-17zvpm9iCkjNkrqMvsoe3VvbecJkmln5V7kRUu7vfCSw9cZSj2lMquC_vBT9It-96Mzjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی از دماوند از اتوبان قم
🔹
دریاچه حوض سلطان/۱۰۰ کیلومتری تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654447" target="_blank">📅 12:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آزمون سراسری ۱۴۰۵ و آزمون دانشجو معلمان به طور همزمان برگزار خواهند شد /زمان دقیق برگزاری این آزمون‌ها ۲۰ تا ۳۰ روز قبل از برگزاری اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/654446" target="_blank">📅 12:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار برای هفته آینده؛ مصرف برق از ۶۰ هزار مگاوات عبور می‌کند
مصطفی رجبی، معاون وزیر نیرو در
#گفتگو
با خبرفوری:
🔹
با روند تدریجی افزایش دما انتظار داریم که در هفته آینده مصرف برق بیش از ۶۰ هزار مگاوات را تجربه کنیم. تا این لحظه تولید برق نیروگاه‌های تجدیدپذیر ۴ برابرِ سال گذشته است.
🔹
در تمام ادوار گذشته و دولت های قبل مجموعا ۱۲۵۰ مگاوات نیروگاه تجدیدپذیر داشتیم و در حال حاضر قریب به ۵ هزار مگاوات نیروگاه تجدیدپذیر در کشور است که رکورد بزرگی است.
🔹
ظرف یک تا دوماه آینده، ۲ هزار مگاوات را در مدار تولید قرار می‌دهیم که عدد بسیار بزرگی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/654445" target="_blank">📅 12:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgshvsoHRDQ95TpxyqEbxwoyoZqyPsONSudPiYcJMzARrv-Dj_Bpidc5jFtEwZ0cwv2bDequSGmCnrIybvGh3ag25jOkcBSPLnLS6r8EeGYaPm12-_lhlH-U6gUgpNjw-NynPlI0wV3-Mp1hrpxDQ0cVZa71ItYRdQAb37p9W5Vp1u8hNXrVuU8kIlN1vamxDVHWAnLJnRCjv0qihMmv-h0VLzUim95y_CtNmsVeTeMcqjuB-4bXZp0V3-jg20u8MzNLlXcv2JiwuZop4AmbjCmE-jgg4z3GFwPqtM3uXK-63erJpLli8LmvEGr0pfjm6uFfL1znMdJ2Ky_JsoZLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای نماز خواندن کریستیانو رونالدو
سعد السبیعی، مدیر پیشین حقوقی النصر:
🔹
پیش از بازی آخر مقابل ضمک، رونالدو همراه بازیکنان نماز خواند و سعی کرد حرکات رکوع و سجود را تقلید کند.
🔹
او همواره به اسلام احترام گذاشته و در مراسم هم‌تیمی‌های مسلمانش نیز حضور داشته است.
🔹
همچنین گفته می‌شود گاهی پیش از ضربات، عباراتی شبیه «بسم‌الله» زمزمه می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/654443" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddKF5EwPYf57mIljMKnDoGt7l9mMTmC269UN-MaZHbMaSchaZY2fgMRKWiNdvssG2RXw7Ot9YCXeXZ5sA_TmYCAoEAWaxFGII8xgSHPfUZhEHQSHjaTcQgkguJtOgK8i9kryma1FcU7-2j20pn-pOxBupm2rGrXnniD3EhO5IawyM8JUEXnuauT9uYEgdDxzY5bBALu1JW8NMu_98iGvxhM8MwGDluZrzllJnWYpd3KxzO4XWN-AJaL1Ovn80p2iNmgTlt1qKYAl_fM9N524_8fJX0OXK-Zy9sRq_NqiRDizxim-smnYZ-9aMfQz6m7DHJYX3KGEIJegUMHZh6tYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سواد رسانه‌ای؛ مهارتی که جلوی فریب، شایعه و اخبار جعلی را می‌گیرد
🔹
قبل از انتشار: مکث کن، منبع را چک کن، بعد تصمیم بگیر.
#آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/654442" target="_blank">📅 12:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654441">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cfde2257.mp4?token=Cz6iYbtXMKqJTahUSFOEPf8b14CRnBdvcP_9dQhrssvc8pNqKhkgoKxLY9CKsPh1kNjhEqhyf773MAPDUe4OvbKbKpCHp2KRnhfIVOHctHKOUvQ_H0tgO0kjspxlVxwDk5W324mLp-GG9oelmF8rooffuABUB2DFyJy9Gtggl_zyBCfcPsFbx17lo7c5SuFgW3fWptSCdkyLcNOpXUIRg9TZZD9RyQWDKussgXyH2jsT8BIA1SpnuHKJKgQ6jBgNCbJhJYBa4p2gPjxgjZ7UnVvPuM6d5VLs8FTLAySVMyR9himwDf7NAyCjm9YmqG1-ykkrLhKXeXHBn74cGIr1tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cfde2257.mp4?token=Cz6iYbtXMKqJTahUSFOEPf8b14CRnBdvcP_9dQhrssvc8pNqKhkgoKxLY9CKsPh1kNjhEqhyf773MAPDUe4OvbKbKpCHp2KRnhfIVOHctHKOUvQ_H0tgO0kjspxlVxwDk5W324mLp-GG9oelmF8rooffuABUB2DFyJy9Gtggl_zyBCfcPsFbx17lo7c5SuFgW3fWptSCdkyLcNOpXUIRg9TZZD9RyQWDKussgXyH2jsT8BIA1SpnuHKJKgQ6jBgNCbJhJYBa4p2gPjxgjZ7UnVvPuM6d5VLs8FTLAySVMyR9himwDf7NAyCjm9YmqG1-ykkrLhKXeXHBn74cGIr1tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا فیروزجا، استادبزرگ ایرانی‌ تبار شطرنج فرانسه نابغه‌س. انگار بلیتس بازی می‌کنه!
🔹
پس از تساوی در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی (آرماگدون) و با چند حرکت سریع حریف صاحب‌نام هندی را شکست داد.
🔹
فیروزجا در اسلو با پای شکسته و آتل‌بندی شده به مصاف حریفان رفته!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/654441" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654440">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaKO2zac_FfLSQ6KqczxePm-mhUOFZSAN5S5vQmZcR7bP350WB8HZVKInQVsHkvcw21Hbmi0IRovMzgffoCH3pELVvXbRCpEfrevPZ6A_LCHKV3QePk9Hr1S6CmRLCl8pvj5vfMNE6jnYylr_-g2VAZRkz9ITcSu1KyYM0qscXo_GkY9jSkD5PGgg85ECYZWOrYbx5TDAOT5FoQ1POeNaJrABNsiC1KmNs95wbj5PcD703IOm43u3EMt4v3rktW0LCamMcd9yPhwCxEZg0SpITrjiD3h6-8RgbjgQHa9dJOBGZaZi2oIZjBhvzohn5EKpc5sHOkrQ_01TgpnTiq6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هزار موشک تاماهاوک به ایران شلیک کرده است
🔹
مرکز مطالعات راهبردی و بین‌المللی آمریکا اعلام کرده ارتش آمریکا بیش از هزار موشک تاماهاوک در حملات علیه ایران شلیک کرده و حجم عظیمی از رهگیرهای پاتریوت و سامانه‌های تاد را در این جنگ  مصرف کرده است.  روند فعلی تولید، بازگرداندن ذخایر به سطح پیش از جنگ احتمالاً تا سال ۲۰۳۰ زمان خواهد برد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/654440" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654439">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
طبق ابلاغیه جدید آموزش‌وپرورش، تمام امتحانات غیرحضوری دانش‌آموزان باید فقط در سامانه «شاد» برگزار شود و استفاده از پلتفرم‌های دیگر ممنوع است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/654439" target="_blank">📅 11:48 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
