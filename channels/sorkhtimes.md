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
<img src="https://cdn4.telesco.pe/file/suH594awH74CDTcN8S4_hhLc4FXGmy5GQy8ewUVdKGVIPonsPnKrG8NX3zWUgr6C6HNXLRl5WtuNTizdPZswfPtfleFO2GQR2JoQwkm3hvE4fnHm5mRx0xJhV3K_uiGGglK4yRl2H-ehh59xddC6eKSGCVMc1tvtTMuXTVk_IoxtP-XutbMTQk7oWk3ByvuBUU4AtAWrggDE_I7_uk99Totbd3zEBaWVRGx0wljG1Qm-AHk64jSDVKhIQjnvWq64kRCYNFjNeVeKH4h051ol531ffM2nMk3f282BCKNnykUE-bAx4QY4qMyq1XoVEo6-1LFTt1XcDr_mleA7zSypUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
<hr>

<div class="tg-post" id="msg-133161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBaDoFYMoWUutRtJiOvL38foIsrjF3Wtt1WE-k60mgkXj1zPj1PLEqFAdFkOezv_c9dcUBb1duglOrSNWBdCGecByR0jXjf7FmZW4EevQNSiudVMdna6L1Klet1kJv1oHeU6Agg7RGADYn-0csGmzrdmfEamGfprKEC7hQXQFrkMM11AXW2la2Rnw8IWL4QVcKw2ZeK89__DZr-bUYsXaaBLUumnNX460Zt33tPxNOwDkIreuid8JZUm3cvVpOFQ5NIA86ANm-r6yQc0bJIWz_83xAXWTQ45ygZeI_trTV6iKbERvFiUmPzeSRHTGlAWtIDyKPvUoxG8yFEqOHRPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 632 · <a href="https://t.me/SorkhTimes/133161" target="_blank">📅 01:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4opBbzP8KryUjDbiqVkBrgd6QbUnYrfAegURkH9TjxJ-h6_3fm3Y2a--Nw21jVGC6f82rXCFYMRJ9fMMuQ0eg3jrErx5povLyEXvTZgmsmxjaILCe4LoKx52fusFrlCoYXPPaZEC8wzVcABJRTJUbTXurY-sUBgF55QlpjrsKOKowJJ4QODm_XmPv0MZVCy-4RBspyG4pjQQcZlx_pKZQs_x4YB1Bd0SsmWXVJvI3brkmVk1qZQCqUwELvfUqUNPv4v6M8mKZ-1CFqklW6AlKpo0XjK3r0kOfnpOykt49ZyIC7uAID_u1OpS-rfJuJYaXOuopTmiaPPDF-55J8Acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سنتکام: عملیات دفاعی آمریکا در پاسخ به شلیک به بالگرد آمریکایی آغاز شد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/133160" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133159">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| پهپادهای ایرانی در حریم هوایی عراق به سمت اهداف خود در حرکت هستند
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/133159" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133158">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
#فوری
| مقام آمریکایی:
🔻
هدف از حملات آمریکا ارسال پیام هشدار به ایران است
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/133158" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
#فوری
| گزارش‌ها از انفجار در بحرین
‼️
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/133157" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
#فوری | حریم هوایی کویت بسته شد
🚀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/133156" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
#فوری
| آکسیوس به نقل از یک مقام آمریکایی:
❌
نیروهای آمریکایی به چندین سامانه پدافند هوایی و راداری ایران در مجاورت تنگه هرمز حمله کردند
‼️
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/133155" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
#فوری
| حریم هوایی کویت بسته شد
🚀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/133154" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
شایعات،فهرست اولیه اهداف آمریکا:
– پایگاه دریایی راهبر سیریک
– پایگاه دریایی ولایت جاسک
– موقعیت پدافند هوایی بندرعباس
– باتری موشکی ساحلی میناب
– باتری موشکی ساحلی قشم
– بندر قشم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/133153" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=TBwjOAZfF-7oswt4O2YBnzwNixmITHjfQNWcsPKEVF88AKOPeZ_qAcp8MdFu03PPbsiEmsLpkXJOKa1kM50OB-mA2WIHu_FeY5o1TDVKQ559pFjogPIUe5p7kts0Sl-xQfel7aEXvkLJfy1aUCWTVBtk9tfi63Qd6JUuLohtvM1ZQfgZxSKmd2Tj-Anv_iWZK_IjPajkrLOyrEzZE6s_-hPt1YcuwZVOK_XBBEkGaSqF9lsknfTpRkadorOOHTynpDt8qwkFlzWmW3etFZ-PO8m6EOFynlnkxpWiPLI56_0fUgQMxoLFC32uH7MIW0aLFWAA0SFmKpGIqm4-02HR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=TBwjOAZfF-7oswt4O2YBnzwNixmITHjfQNWcsPKEVF88AKOPeZ_qAcp8MdFu03PPbsiEmsLpkXJOKa1kM50OB-mA2WIHu_FeY5o1TDVKQ559pFjogPIUe5p7kts0Sl-xQfel7aEXvkLJfy1aUCWTVBtk9tfi63Qd6JUuLohtvM1ZQfgZxSKmd2Tj-Anv_iWZK_IjPajkrLOyrEzZE6s_-hPt1YcuwZVOK_XBBEkGaSqF9lsknfTpRkadorOOHTynpDt8qwkFlzWmW3etFZ-PO8m6EOFynlnkxpWiPLI56_0fUgQMxoLFC32uH7MIW0aLFWAA0SFmKpGIqm4-02HR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
سوپر گل کریس رونالدو به الخلیج برنده جایزه بهترین گل فصل لیگ عربستان شد
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/133152" target="_blank">📅 00:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/133151" target="_blank">📅 23:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
🚨
#فوری | پیر دوسی، خبرنگار ارشد فاکس نیوز در کاخ سفید: ترامپ در حال برنامه‌ریزی چیزی بزرگ و مهم تو ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/133150" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حضور وحید امیری در تمرین پرسپولیس  وحید امیری بازیکن پیشین پرسپولیس، برای طی کردن دوران درمان خود در تمرین تیم حاضر شد.  به گزارش رسانه رسمی باشگاه پرسپولیس، در نخستین تمرین تیم فوتبال پرسپولیس بعد از تعطیلات، وحید امیری بازیکن پیشین تیم هم حضور داشت تا روند…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/133149" target="_blank">📅 23:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/133148" target="_blank">📅 23:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm_BJuiNZ4uoBdoXui6WjcbXcP17qObOLNlmgy66Avgnn6LN_w3SKNHoE2JQ2f7YOd6W7r1wEZGWOrU7yUQAPINnWKaWDwsZxKRAZoHeXgEeteuCDVL87yOR0Uv4aH68OxhaH-jlsTiHmF4EFLNl-kzuOmEOg6cg4edvIXznNEhiFy17Wb8IzI5kT8nVsoAKPSC39VFr7N-gfbzFPVSKPGvUaDeWJJeFwwRK9drnnPtTvwM55TJP4QOcuRN1TCxt_rFaTBr-NBqxjqOx_IFwaGcbtWFPoa60cYoZiEtfPfcBIQWSiJFLwMcw8oqYnMWmf1mFBNs02Yu0zsje-TNg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
🔴
پرسپولیس به دنبال جذب محمدمهدی محبی بازیکن اتحاد الکلبا
/
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133147" target="_blank">📅 23:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
فاکس نیوز: ترامپ می‌خواهد دستور انفجاری بزرگ در ایران را بدهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/133146" target="_blank">📅 23:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBiaW40VUZuzTwiRV80R4my85Wclf5tppN1No7Z1jE8c6LD6pKqYIiXfk4m4odKO1Hi_tOkqcLLV7Lf7IgEGrZcprPuy8E3R2rLElOl_bhS0Ko40XhmuphpbrhKbPobf5ih62oCrokUqgO47RzDL6A_N9IVnGaCFpCEEzjYeuWhIV6_nNlwg373VqUMPAXYYRTb-E1yZqYn3Uid20WqU6Z6bNqkZyVZIYK2b2XFeHE7dpWLjnUgm73aQViw_iCQykOKW-FOpoZ-ZKbUhEQ90YZP6TQ-0nrbMCk6MJFvO_1kzyC9n0GyuWQyovCAug1lwOxMq-_itAKksLmPllCMRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
|  پیت هگست، وزیرجنگ آمریکا هم پست ترامپ رو داخل صفحه خودش منتشر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/133145" target="_blank">📅 23:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/133144" target="_blank">📅 22:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133143" target="_blank">📅 22:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133142" target="_blank">📅 22:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
رسانه‌ "چمپیونات ازبکستان" در گزارشی اعلام کرد، جلال الدین ماشاریپوف که در بهمن زانوی خودرا جراحی کرد و تلاش زیادی کرد به جام‌ جهانی برسد به‌دلیل عدم‌ آمادگی این رقابت‌ ها را از دست داد و یک بازیکن دیگر جای او را در لیست ازبکستان خواهد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/133141" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiosCZwvmeSFck9forGbRv9giz70NEUGgvd-YNRqPGc0A4rGLr8RNEcHx2XnTV13kBaNvF_w3K-ulplJoQcAhsn-157WSgyCT7LKctaljCho3GrAXMBCBq4YH5Xn0u8vUZORm71ju_GHtw9t-Cp4kQgr0gA7_n8nAb_jryeMby5xFgc-726dLj5u__X4PtFDcyioNl4lRVvIUgUx12HAueE_IPT858TY569Ee4Sx-Rn_tMfDPxV5bYGVEmAJ0WG83YkOpkna6VWJ_6jf6VIxhyqOWygRD6YboLvsG5QlZisAf1tjx6mlSmXgFYcF0GBpKDEgS_Z_WRwlxIJQZGsmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان: بالگرد آپاچی توسط پهپاد شاهد پرپر شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133140" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔵
⚪️
افسری(سرپرست گل‌گهر)
:
◻️
ما نماینده‌ی ایران در آسیاییم و توی هیچ تورنومنتی هم شرکت نمیکنیم و اگر هم غیر این بشه ، شکایت میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133138" target="_blank">📅 20:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRYf4Nl11Kx6-6Y7wGc1y9hheIc3Y28CgyiFrVjTxPUPA_CaTnjVBv7wx-QGr5Jy8NQkHDGZ9jat2_vbVQKfKXKnlr8nI9pv-QlpnbcrhDQFZonLrInNid3KC44BWPRqyImWoUBaRcTkUQMsAYZ0BJzDMKorC5uGtuBpHC5zL-UFaRkGN5G4c9fgbzGnVyyTUYQbSB9lYzsFyFon08wICGb4a76q-HxpTFY0AQiY6saxJAo2PjwIqCHkg5CsRI_LN-UjqeFSwzgbvYWqJD6v4Pw7TOs1k0uaIxukYnhFP5TqYYn29rjKfkSK041inqDg6wxC2SfHch8N5JfU7tr8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
شمارش معکوس تمام شد!
🏆
تنها ۲ روز تا شروع بزرگترین تورنومنت فوتبال باقی مانده، رقابت‌های جام‌جهانی ۲۰۲۶ رو در سایت معتبر
اسپورت نود
با بیشترین آپشن و بالاترین ضرایب، همین حالا پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133137" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3d7HjZmAuX8KHYIyl_8qYr7134EEjhj-poKnEP-GtmaanN7W6KDnxD3wd5S5km7RVGJ7d31qgLrPd_95ZKkH4-K4aN-i2uooPYwX2wXaCno3n2NPSsd_LWo__pMvc5X4b4KcapZj7PKEgvWwtyeAv0vlbFmpSGLV005HT0FztZHEPrIhgNaqiFwmANqpBkjDy-ZkJv9kJCDw_O30pILR166Y8A9MrzoIOzxnSFMVY8yLo8INor2GxcWnW2GMBgxMAmIxPxCIK6U7nRg-_pCo8aRBCm6Z9Ttef9MdrKI35XTXzB6O2mCFU5NAUFyxz223rXs5RrrAFPrlSrVphSXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ: شب گذشته ارتش ایران یک هلی‌کوپتر اپاچی ما را در تنگه هرمز زد و خوشبختانه دو خلبان زنده موندن و به جای امن انتقال یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/133136" target="_blank">📅 20:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spVjGtJREaEd1NG2nszWXh6jQxW6xOh7_cjKL2FU45hi0X5W90Ndz86eqABtXs5yGBn9d3_4Fs5LrDpqdDbXsFv07XN3ifurjg5GdOJSS7PDrbP54hGqm02npdofgF3DyXwVrnMpG3oNVUp1ObRfewP_ksemfjKJzMYeBjz-ri7BcYqadEcUL7OVRWMxEtrYJK1BQFjdtTFfZW2Ci0fGwH8xYyObfP78P9iJ7NVn_kVYnswqQxTCqqgBj-g_Gy15xVGtL4IbHOqvOQUCq7KQakD7w_9fGh1gFIQ3uooKMvFQKcxw3fbcQwDLPbmSNzLtoqLDkPtB9fE8arL5_sdbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال افزایش سهم بانک شهر در مالکیت پرسپولیس
◻️
بانک شهر پس از واگذاری باشگاه پرسپولیس، با دریافت امانی سهام ۳ بانک دیگر (اقتصاد نوین، رفاه و صادرات) سهمش را از ۳۰٪ به ۴۵٪ رساند و سهام‌دار اصلی شد. حالا خبرهایی منتشر شده که این بانک قصد دارد سهام بیشتری از اعضای کنسرسیوم، از جمله ۵٪ سهام بانک صادرات، را خریداری کند تا کنترل و نقش تصمیم‌گیری‌اش در پرسپولیس بیشتر شود. با این حال، هنوز هیچ تأیید رسمی درباره این تغییرات منتشر نشده است
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133135" target="_blank">📅 20:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133133">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
اینستاگرام پلاس ام رسماً رونمایی شد و کاربرا میتونن با پرداخت حق اشتراک ماهیانه ۴ دلار (تقریبا ۷۰۰ هزار تومان)، به این سرویس دسترسی پیدا کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/133133" target="_blank">📅 18:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133132">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNJOa5OgqX2x1bU1Eq6AbBQ0wygb29eRYqdXFFjYd4asV-mznjQjeEniPYE-CPhnMuBMrOO38u8DprYWSbQFLjLLMsRZ-qyr29Ejpoqh5TAPxzRzfHFY_rN02RqXrmRl2tLBTSJyjPkFWVVf6v1M_sfa5Ph9uJjbyFscqy6IQwsXKaJUVf0Yk19a_9L_86eo_GelutyonR5hh5ODEkXrAwqVdHMCO6I-hvuxl72RL4kK8KPW0Ae0_j92NcX6UqexdwQzYrj5lGN5VufGU8uWZiNlj__MqhpvfpibmtUs8aXwI4_BPiJr-gsyBcIT8oKIr5ETD0wvjid-eDzhsqsV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینستاگرام پلاس ام رسماً رونمایی شد و کاربرا میتونن با پرداخت حق اشتراک ماهیانه ۴ دلار (تقریبا ۷۰۰ هزار تومان)، به این سرویس دسترسی پیدا کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133132" target="_blank">📅 18:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133131">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
💢
مدیرای باشگاه هنوز نتونستن با سروش برای اوردنش به تمرینات ارتباط برقرار کنن.
🔴
این درحالیه که سروش بیشتر مبلغ قراردادشو دریافت کرده و کلا 10 درصد طلب داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/133131" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133130">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
مطرح‌ترین غایبین لیست تیم ملی: سردار آزمون، احمد نوراللهی، الهیار صیادمنش، علی قلیزاده و محمدجواد حسین‌نژاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133130" target="_blank">📅 18:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133129">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
🖍
غایبان احتمالی پرسپولیس در صورت برگزاری تورنمنت سه جانبه برای کسب سهمیه سطح دو آسیا
▪️
ارونوف
▪️
سرگیف
▪️
علیپور
▪️
کنعانی
▪️
محمودی
▪️
سروش رفیعی
▪️
میلاد محمدی
▪️
پیام نیازمند
▪️
دنیل گرا
▪️
تیوی بیفوما
▪️
مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133129" target="_blank">📅 18:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133128">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#شفاف_سازی
❌
از بیخ و بن این خبر غلطه تاکید میکنم پیمان حدادی هیچگونه جلسه ای چه در رابطه با سرپرستی و چه در خصوص تبلیغات از این دست موارد با خداداد عزیزی نداشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133128" target="_blank">📅 18:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133127">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
محمودی همراه با تیم ملی به آمریکا میره و اگه کسی مصدوم بشه جایگزینش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133127" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
آقا کریم در تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133126" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133125">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133125" target="_blank">📅 18:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
● آخرین خبر از خارجی های پرسپولیس
🔴
• دنیل گرا تا ترکیه خود را رسانده اما نتوانست روز گذشته به تهران سفر کند و به محض باز شدن حریم هوایی به تهران می آید تا در تمرینات سرخپوشان حاضر شود.
❗️
• اوسمار ویرا سرمربی این تیم هم تا آخر هفته با بلیتی که باشگاه برایش…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133124" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133123">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZXWP4_2-vLRgWqLK-Gm1NEopL4s_b7KhpVFxuYB3Y0LXY30yQoM2sFB4a_1uL8hExscb0AMr80S0flWQBRDuIO9henwcgDYQqEVUpmJx4zHZuWJzgySEgGfhLLVFj6HujqCavZbyiVVTfN8HTyTzONIPN5KH9r8zoZQZJ2MFKUsiIyZf70L4v5cBBUeAfh8Y2Rso7UhsRbaHZYob2WthFc1ZMSBbJGhrnBUpVkrcBz1IUpDxKc-fmTyyNeozDEg2r0KxZjBhVCVnR4WWkFWJ4qLQ-uczmoxvw6JTCt8L1JybsJUUr71lhrm2FJGbb0D1H5Hjis57KP1zTgGzWpmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/133123" target="_blank">📅 16:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با تایید مسئولان باشگاه پرسپولیس کسری طاهری مورد توجه باشگاه پرسپولیس قراره گرفته است مکاتباتی هم با باشگاه روبین کازان انجام شده؛ و قرار است در هفته های آتی جلساتی با ایجنت کسری طاهری برگزار بشود!
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/133122" target="_blank">📅 16:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
یاسین سلمانی با عذرخواهی از هواداران به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/133121" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
پرسپولیس و مسیر جوانی در تیم
♦️
شاید بعد از چندین سال بسیار واژه مسبر جوانی برای سرخپوشان مهم و حیاتی باشد چون تیم از لحاظ میانگین سنی در وضعیت بسیار بالا قرار دارند و شرایط ایجاب میکند که در فصل جدید به جوان گرایی رو بیاوریم تا از لحاظ سبک بازی هم شاداب تر هم بهتر بازی کنیم یک فصل جدید و نوین باید رقم بزنیم و دیگر نمیشود با بازیکنان سن بالا مسیر را ادامه داد...
♦️
اگر بخواهیم قوی تر ظاهر بشویم نیاز به یک رنسانس بسیار مهم داریم که باید مدیریت و سرمربی تیم روی این قضیه حساس باشند و مسیر از فرتوت شدن به جوان شدن تغییر بدهند موضوعی که خیلی ضروری میباشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133119" target="_blank">📅 16:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn48M5fFfd3-uoOaMKNMS5J0Ab7Jr4nqs3ayhXvnT-cdlzVItUy67cojyaNfloYyu-liFiFLbAONoEkdfq6CL8y_EtD9oYrFt6IpuL5pWyhwdA9gTHpfp-nopAj6KPa-Lf84-5lOnsNhfsBXYE7Cfua7KRlC55fII1s2bntMmX5Tezs9JFC0Qjh_HjGyqXatNlv24ymEDBLcb_wxuBTOH4bejQtATFAFzZapDWA9glRxwIyaNPqolv0tse2Ke2dVkbaeXC3jBvf3o4qkfEmB_3BEbxH71zAqWzQeVcctSlrA7tripO8NNZKsm7GoyjzBPBV95I8cZ7hdVCxCB9nj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دستیار اوسمار به تهران رسید
◽️
جولیانو والیم، مربی بدنساز اهل برزیل که قصد داشت راهی تهران شود و روز گذشته از عمان برای پرواز به تهران اقدام کرده بود در نهایت امروز وارد تهران شد.
◽️
این مربی از فردا در تمرینات سرخپوشان شرکت می کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133118" target="_blank">📅 16:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8xG7Vrw4fcqOEV60HSE0CLJ9U2wcWVqRdUyFpmIRSTulh79Hs9CxBRPVNazaRbjiw31fJy1LY7XQbfUYIUl3rwsMyn13sOOodtzDm7uxCss_AZGu_i_s5Z2pnKthXW4HlVDIiqiyyQUO1U48J9tXn6lQw1zdScOOIHxBFotIFGcIyDC14YF_5xsnCW94f-k9S1IbHDKMdCQrCrXp8_gq-DKqlHshYHn3XvSu8OC9lgXANkDCRPr6l9LHlbXph95Fmv4aOs00pZ4A8HBEkDu0QNsRaoSXzJv5rT9blc--SQzQbJhhdIfkweWHJLMNzBw0BFOblzZXbQs1yjXksJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
آقا کریم در تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133117" target="_blank">📅 16:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
فوری : یوتیوب رفع فیلتر می‌شود
🔴
مصطفی پوردهقان، نماینده مجلس: وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ ، رفع فیلتر یوتیوب  هم در دستور کار بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133116" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajXYsAJQui7lxIZHLhJNXh3_7_PxegEZAT8WPwdj7mh7HGHTgCmLDPq3BbmMK8-3AGcm2cnfrGQ6rg5PDRhTDyC3DULkYQDxefDIbbwh5TmgsAF3B9JyKKDGBnX5krUNjc5qGnYKBUk0M72W1PQRbCiV9UjqxHceiwh0Kg-whxm4cxKoDsBBZNhYyUdncml6wpIUyiW63gHxVhb4IqKSBkJKBT1xCOGpfVSTxiLDUhX4SfpN6AxMX3WfeNe_FGnAplAeSaLaUn4oXYVo3wwL3K6z3EtsxB6Zxt67tlgD8UX6vk5bwsRcywrJPXwTKjD7S-GpC1711vDPUXSZFVqwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باشگاه با ایجنت کسری طاهری مذاکره داشته و شرایط جذبش رو جویا شده...با روبین کازان بند فسخ داره و میشه فعالش کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133115" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdnBtwhYVA07GGkTLr7O2f4VA3a1TGbT7VoeE-MU22S3Fmln_neqm0pvyc4JZvw2OpL2N8v5n5i1HTb1Uu2DmDOILrRX26pp1375kZd16W90E-7auGHk4bi9RrJ779Eja8to2lcgzbT8FBc5SddEdT-dVXYgVUlDobRDJ2NZeikB_N7eKOsj9iBxLeJ-RvcRyA2_peyN0KUq5hYjAy3qY6bLFL0CHJ8uU-A1K3pEvclvi7sBqx9NdyGgFlOTcHRVhIH3Rd48SRkYseatNt1wuxyku6GiJ5RJeCR4ssiMfeQdL5sNcU5SGx0LlO7hx039Dej-f7f_VozY9po4VJzl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133114" target="_blank">📅 15:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🔴
پرسپولیس در مشهد کپی می‌شود
🔺
مدیران پرسپولیس در ماه‌های اخیر طرح‌های مختلفی را برای تشکیل تیم دوم مورد بررسی قرار داده‌اند تا از این طریق زمینه رشد بازیکنان جوان و مستعد را فراهم کرده و مسیر حضور آنها در تیم اصلی را هموار کنند.
🔺
گفته می‌شود یکی از گزینه‌های جدی برای استقرار تیم پرسپولیس «ب»،
شهر مشهد
است.
🔺
چندی پیش
پیمان حدادی،
مدیرعامل باشگاه دیداری با
استاندار خراسان رضوی
داشت؛ دیداری که باعث شد گمانه‌زنی‌ها درباره احتمال
راه‌اندازی تیم دوم
سرخ‌پوشان در مشهد بیش از گذشته مطرح شود/
فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/133113" target="_blank">📅 15:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133110">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odphBSCqpjmeol6ne7CbxlUnAYoefbJsYUJTgak2OPaY9OG-xju3pIqDFnR5RXDM0CDRR2h09KiJLfEcl1E4mx0sGJZY5Jj2EbuWVA4t2MZzDRVHp7FC-9R3YgR6hQIpq6ZP39md1oig22JDtyNRUQj7jIt0AX_RZvZwhZnbPfHtQ6XYCtBfubQFASjwPz65VAgMC9V_iSZAA743kFG2132z6GTI_ZloPGbBMwjrIcF4ho9myMr5jiwTsi12jYmSqkRcP_nD4fGL80KiiSuWJmjc6qDTJZbOsG2f6eCH3J0IPlkUzRXXPJ18rfPqYGfmPdZD4obss9NXgoVl_6KjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Egj3aXVCPwZB04QMxdzNbHPf1cQvtFLzN0jdqra1wPSCHUET7QIo7xjxQEQ4iH9X7Y7v3Jwb95j9TAtyPAPJucKb7yDhZFtcSJ8tJ5eTY0bIHeQXMRA4KhAVK56hRnybC-Y8Plc1e5T_8Cchq9AeStr2X1Aolx1tfwUBkr79Nj5LwQOjOWQ0W2L8jHF1_Ku_ihpx6Fm8GQG-KoACA7g1SBkgi5H9_lWu8QuZcFLGe804FY-Dp9DICDJyFFuUdWvj9fzjl_HMWnAk5JNOtNwyvIBDzk-wm22WQ-3mUGK9zjx3vMWIZ8pl6VMH6PdNvLn-cMVMnkrxslt-g5gQPzXgWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
انتصابات جدید در آکادمی پرسپولیس
🔺
طی حکمی از سوی مدیریت باشگاه پرسپولیس، رضا جباری هافبک دهه ۸۰ این تیم به عنوان مسئول استعدادیابی آکادمی باشگاه منصوب شد.
🔺
همچنین حمید علی‌عسگر دیگر پیشکسوت سرخ پوشان نیز به عنوان سرپرست تیم نوجوانان آکادمی معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133110" target="_blank">📅 15:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133109">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5Dpz2Cuwt-Nzxdhy1_yEWDWNeiL4rW__ODoi24GJAyRGsD1b4XEbI0nisCTUwtlmx8alY8pyqxLzo5t91_Y_eKw3sBEsaKwEss9ICILR6swINl-qAiwGPQilba5Dm0KLR--OqjtOsXzzxDyI0ynSARtI3ZK3EY0YU2B7eQBQyzYRjVWySXIzrsY7KKrYJO8LFepr2PEEp-w5PpJjevwRffPCA51ifRr6BLnVDb9uqdT9mzGnpcczBSQV4eE1Cj1VDCOv7zPPC12WmJkGTgKbqDPT54jc22dO7UGUgtJh1s8FN4CigPM3DuFX_LIUnRs3FvQBfE7GQTB5QAluK8I-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
تنها ۲ روز تا شروع بزرگترین تورنومنت فوتبال، رقابت‌های جام‌جهانی ۲۰۲۶ رو در سایت معتبر
اسپورت نود
با بیشترین آپشن و بالاترین ضرایب، همین حالا پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/133109" target="_blank">📅 15:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133108">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
کریم باقری و محمد عمری از امروز به تمرینات پرسپولیس اضافه میشوند   سروش رفیعی همچنان غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133108" target="_blank">📅 14:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
کریم باقری و محمد عمری از امروز به تمرینات پرسپولیس اضافه میشوند   سروش رفیعی همچنان غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/133107" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‼️
مجتبی فخریان، وینگر پرسپولیس که به صورت قرضی در ملوان بازی می‌کند، قصدی برای بازگشت به پرسپولیس ندارد و به صورت دائمی جدا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133106" target="_blank">📅 14:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
پرسپولیس برای تورنمنت سه‌جانبه استارت زد
⏺
باشگاه پرسپولیس: نخستین تمرین تیم فوتبال پرسپولیس بعد از ۷ هفته تعطیلی برای حضور در تورنمنت سه جانبه اعلام شده از سوی مسئولان فدراسیون فوتبال، عصر امروز از ساعت ۱۸ در زمین شماره ۳ ورزشگاه آزادی برگزار شد. در تمرین…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133104" target="_blank">📅 12:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133103">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
🇮🇷
آمریکا بلیت هواداران ایران را مصادره کرد
⚪️
فدراسیون فوتبال خبر داده آمریکا، میزبان بازی‌های ایران در اقدامی غیرمنتظره، سهمیه بلیت اختصاص‌یافته به فدراسیون فوتبال ایران را از آن‌ها سلب کرده و در شرایط فعلی امکان ارائه حتی یک بلیت از طریق فدراسیون به هواداران…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133103" target="_blank">📅 12:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133102">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
هو شدن ترامپ در فینال بسکتبال NBA
🚫
وقتی دوربین‌ها هنگام پخش سرود ملی آمریکا در فینال NBA، ترامپ را نشان دادند، او با صدای بلند توسط مخاطبان هو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133102" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
بیانیه رسمی فیفا: دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.  در این دیدار ارزشهای همجنسگرایی را به جهان نشان خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133099" target="_blank">📅 11:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133098" target="_blank">📅 11:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYeg9R-pMDJTWObwXxmWJVaKTC6KFU_dhKGWkKPqRn2VluutdvJgCMrXZb8Yk9O-7-ITioXl8Is0S0dJFkiNXYdh9KSbM7dxHNMXH8QyKnhXRhEwP3otCEa_jNlnwmpqjH-JAIO31adpBvS3T5gjb6YF9di1dy6XobLr6s8ZFSDMJgWeE4EbaD4H5DT5B0iwwD2eort7fuWwKaEFgX9NovedNrqtbgUsLaCOVi3-2NgLBXA-XNtuuqq7I3BMPsa64EqSM2DpI082Z3Svfx-2oUMs-AuL1WNzUlUB7D3bBbZdWZFhHxLN_UGPY560aDluS75mkUPUMsYfM_QHHp2Ilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133097" target="_blank">📅 11:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0309c6ebab.mp4?token=LUachFEE2M1RWb1ebRENuPrC6E8KOfnD9UGDRjhYJSKcE_mNLOwhD-V_wPzW2QDUOLG7zrA4Sk_Z7ex2sADptv1D600BwS7cSuhAJt6kbwJ1GiEjVtpd-Jg4QOtH4x2WsXgHEcvjWFBzuQU-sgmKRR_IZ2cIiehwoVbmu7UTfqvfKUgOOzNeayc8aX9C-OOw6JjCm-RnRUEqwt_NbQlh29xm73UeDDV6cP4AhC6c2LRGbzuMWEa0n8X1lLRSuy5q1oh0S2XHhGIDoTYGNMUBPjpvaolmqV8VUfDNwSxi1u6ZNzTF29idwdF9Y4e7z5MWeo-0YUii8KhMnTA99qJj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0309c6ebab.mp4?token=LUachFEE2M1RWb1ebRENuPrC6E8KOfnD9UGDRjhYJSKcE_mNLOwhD-V_wPzW2QDUOLG7zrA4Sk_Z7ex2sADptv1D600BwS7cSuhAJt6kbwJ1GiEjVtpd-Jg4QOtH4x2WsXgHEcvjWFBzuQU-sgmKRR_IZ2cIiehwoVbmu7UTfqvfKUgOOzNeayc8aX9C-OOw6JjCm-RnRUEqwt_NbQlh29xm73UeDDV6cP4AhC6c2LRGbzuMWEa0n8X1lLRSuy5q1oh0S2XHhGIDoTYGNMUBPjpvaolmqV8VUfDNwSxi1u6ZNzTF29idwdF9Y4e7z5MWeo-0YUii8KhMnTA99qJj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو شدن ترامپ در فینال بسکتبال NBA
🚫
وقتی دوربین‌ها هنگام پخش سرود ملی آمریکا در فینال NBA، ترامپ را نشان دادند، او با صدای بلند توسط مخاطبان هو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133096" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR_3-zmvcZ6IEmTH5BX3l6BsPRVcElhZzqbhy3GDv-InkXZHUJ0WlldQ88lgJjN44HyeoRqvqIjreVUipqmD3vVl3gwVZm48zkdhhVLwjViK_YmeVbc5c0Qum914dDmXXdd_m__DkJB50XUixfweS2mKtTTVeqmh6tQdgstTD-2ktpqsJBCVmW_LIclU3HtF1_AAmbUcCIdmN7_UptPLErgNS5mmcYNb_8ZSdjmEad_mLmegc9MChavzSqARUJpz4WDiz2QUVaFOtTqkwyxDURTnQ6rz04iL6tMMiWUbJtzL0k7p7b_8BImOg5NdY8rkor69PFkt5krZtPAd0_xe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فیفا در آستانه جام جهانی 2026 از طرحی جدید با عنوان «سوپر شات‌اوت» رونمایی کرده که به تماشاگران این فرصت را می‌دهد در ازای پرداخت 79$ ، نام خود و کشورشان را در جریان مسابقات روی نمایشگر ورزشگاه‌ها ببینند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133095" target="_blank">📅 09:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
🚨
🇺🇸
ترامپ : فکر نمی‌کنم که به این زودی‌ها اسرائیل با ایران وارد جنگ شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133094" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D17wfQBKyfG16MyMrsC-5a132YNSA5NW9usnxly6Iwj6pjYFfaUOCFCGxhcxUdG7j_7PGr0l2Ww2NGNWRL6OtUOUlP9QckPesma4Z_GyG2nxuGxQm9oxoKuQu-O6bUSS_FuoJbPckEVxJCFntxACvefiOYtNFu4-Nh-NcNeObkADeID96a6w3YY9P-53emoERmM9_9NU2sJtIkEOEPXFvkl0iqIe_My1W4oUnqmTxqHMSf9R7zwWk8fcWEsZsWuxe-9cnvxh3IB-av6ffsveSlDXEyhnjRVwdqQPgxp_nrDwsMaKNilrNyjC9MZKz3rMbQ9UcbYsUj-4DwFuCph1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی تارتار: پیشنهاد پرسپولیس؟ اول اینکه هر کسی من را از نزدیک می‌شناسد، می‌داند وقتی با تیمی قرارداد دارم با هیچکس مذاکره نمیکنم
◻️
من به آقای اوسمار که سرمربی با شخصیت و کاربلدی هم هستند، از همین‌جا می‌گویم که به ایران بیاید. ایران امن است و هیچ مشکلی برای کار وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/133093" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHiPfg0CubnGrPhYGT6gQuRokkrWPhMEyMznpA3wDV2rqWUSgOw_eNEn9pUNfEBQpta-wtt2VD6ZzCcJuoNNgSDkSqWHquS2Tqa3C_iJLUGqzjMrT84x0IQFXL-FxilR3ktdgLFLbkScV4sg_pEqFSvaQXyVygyBWeoXb1caJ2tBsXATZAu2Kbpyg4K0lpkN5oFyu2RjqP40vBeZUdTzREmgQuv3PUCcDsb9Os3uR8WBoSvexCDDcL4_5Sz64hUJYaayMIoUIo3dmduQ6kFmY2BXscPGh0IKtFflExH3MbtVNaj9fObGc54XNqYK1-wVlmsxicJxYEqxiQFDIljBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار سوم از فینال ان‌بی‌ای رو بین دوتیم سن‌آنتونیو اسپرز
📀
و نیویورک نیکس
⚔
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133091" target="_blank">📅 01:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
‼️
ترامپ: به نتانیاهو گفتم درست رفتار نکنی در برابر ایران تنهات میزارم!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/133090" target="_blank">📅 01:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
❤️
گل اول ازبکستان به هلند توسط ایگور سرگیف مهاجم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133088" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57eeddf50.mp4?token=VamOAJSPmDgH-y55fM6CetuvwIN0xy1-7E5RMO4uRvyYgtUR9FVO7nPuoX2ku2xOOUOXiGcIau3UrfeoCk7rEyyIvmiQqTASDUROsH-pe1kdNssDE16Iy6OWg8jSdteWOB7oa-Iyt_K5Gz5-RNZmVgfiGqHFQxLoI36TCZQDWzh10AThMGSYWCGq9hWNtG43GrTQ5z8pNsAK-j-phlib74UmR8Z8_Gyb6BKKrnDDnyWXKsbF_kk81E5FbTKLaTsUmliBziX4L89rYNZN3EiAXYjXZN9MIyU44L1dO-OF9b2Tt7uZpH_5N7UG4HS9KE2K30lOOWL77-s99vRMk8DjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57eeddf50.mp4?token=VamOAJSPmDgH-y55fM6CetuvwIN0xy1-7E5RMO4uRvyYgtUR9FVO7nPuoX2ku2xOOUOXiGcIau3UrfeoCk7rEyyIvmiQqTASDUROsH-pe1kdNssDE16Iy6OWg8jSdteWOB7oa-Iyt_K5Gz5-RNZmVgfiGqHFQxLoI36TCZQDWzh10AThMGSYWCGq9hWNtG43GrTQ5z8pNsAK-j-phlib74UmR8Z8_Gyb6BKKrnDDnyWXKsbF_kk81E5FbTKLaTsUmliBziX4L89rYNZN3EiAXYjXZN9MIyU44L1dO-OF9b2Tt7uZpH_5N7UG4HS9KE2K30lOOWL77-s99vRMk8DjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
گل اول ازبکستان به هلند توسط ایگور سرگیف مهاجم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/133087" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
اوستون اورونوف یکی از ضعیف ترین بازیکن تیمش در دیدار دوستانه مقابل هلند بود و دقیقه ۵۴ تعویض شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133086" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
🔴
غایبان پرسپولیس در تورنمنت کسب سهمیه آسیا، پیام نیازمند، حسین کنعانی، میلاد محمدی، امیرحسین محمودی، علی علیپور، سرگیف و اورونوف هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133085" target="_blank">📅 00:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQIuVC_tNU57QbF_CtO5NfGK-30oUJf6Un8sNZjfQ6MS6lHjfitphJjNn5kkGx0xSOL2XZoFYVYS-scTW7jeCVNBe3ZTv2RjZKrgWlmimRcjdIE4eQThh7-1Ird6JoXlHDIFglcCnVwAVy6qO5dv1JmRtzedQpgHFgEqr274ZiHNbf7h9Qn6meGbNYEXP2jY3Rt7c2jKEDkDso7VgXv56FN2rMzT8iplqAbrmI48aLUNj1MwG-aokEiuxxSJyZr1M3qNEahXUUtzCxmvJ8Abyi1IVND-WU_DfGS75e6HN_dNKSCtc5L8E3huM2K-MEayrYDOgRnI-XbWeCLDyQDgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اورونوف در ترکیب اصلی ازبکستان مقابل هلند   دیدار دوستانه
🕙
ساعت ۲۲:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133084" target="_blank">📅 00:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
🇷🇺
شنیده می‌شود که باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده، هر باشگاهی که این بازیکن رو می‌خواهد باید مبلغ یک میلیون دلار به عنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133083" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133081" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133080" target="_blank">📅 23:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
حمید درخشان:
🌟
من خودم خداداد عزیزی را سال ۷۵ به عنوان یار کمکی به پرسپولیس آوردم اما الان نباید او را بیاورند چون بی انصافی است. پرسپولیس این همه پیشکسوت دارد، از آن‌ها انتخاب کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/133077" target="_blank">📅 23:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
🔴
حمید درخشان:
◻️
کار فدراسیون فوتبال و سازمان لیگ درست نیست. اگر قرار بود که این اتفاق بیفتد باید بین ۶ تیم بالای جدول یک تورنمنت می‌گذاشتند و آنها با هم بازی می‌کردند و قهرمان این تورنمنت می‌توانست به آسیا معرفی شود. متاسفانه این تصمیم شخصی فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133076" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
دانیال اسماعیلی فر ۱ ساله با تراکتور تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133075" target="_blank">📅 23:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فرهیختگان: دانیال تمدید میکنه با تراکتور و برگشتش کنسله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133074" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
استاد بزرگ تاکتیک‌های ناشناخته امیر اردشیر قلعه نوعی تو بازی دوستانه دیروز نیمه‌دوم محمودی و حبیب‌نژاد خط خورده رو بازی داد ولی دنیس اکرت که تو لیست نهایی بود هنوز یه بازی به میدان نرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133073" target="_blank">📅 22:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
اوستون اورونوف و ایگور سرگیف در لیست نهایی ازبکستان برای جام‌جهانی قرار گرفتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133071" target="_blank">📅 21:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
🔴
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
🔴
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
🔴
من هم با نتانیاهو صحبت کردم و…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133070" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
ورزش سه: مهدی ترابی مصدوم شده و ممکن است لیست تیم ملی تغییر کند و از بین هادی حبیبی نژاد و امیرحسین محمودی یک نفر مسافر جام جهانی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133068" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133062">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maVOWtLEPCe-7iFLh2LhmVQdrUl-3sILLjYbf_nIheT4Q0DfPJToILSYQmFhp1TFuEiUTGbnW5a4cI-ldiarOlLOzBSfFK3SCaLpQiuky6me1I5bEyen99hyrOZsgPCYIVFO9R4_AGaemvyCFxx8pl9CrLeFfziuSJQllHZ4zTxZRhtECWc_PEIyL_RL2mzwaVmoj00Xm4ccEDn7gSq1enUqrWF7Pe1cXoANBp1CkOCN6gxDDPZYvkrLgTifPdLlGQQzPu2UVctidU8ZBvekrMAZN24R8aY1t3qtherL8J_pnzOROIcMk9b3nQUD91UU_Fahiwc35oqO2ZllegEY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKUOIHLK_Wl4BWdei_rN3eoenvCnaJogJxGWigxwwT9VHs-z3p7ckP5i2GLlyjcrmenObGkTugeXcC4jTTR-pRiXLUTkfZSXJviJGy0BazIXIgqIIU1yXKgzrxi8qF9LvXXqPTEEZSzo9tTT2Dok0VJwiAGKKI6i--4wI4UNFPV5RYazwjcJDJ_drOyyEQ64fhrQOcCrHyn7c6EfxizjdL5q6y--p6eXd4JZ0NPtTV-Chndx5U59KQuD3RS4F0TmLqBWVJID1Z2S2pNBw0rap8PWkjsrR8vhLLvF7MfxBLQqO03TL1I0HO1MT9w2djFxLR09ZjByWvdxf_HGp0Fhng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mgi_7l-tC-RH8eGXHMsCMNVtpSGu6YfjnInnKpnVZsykp33jIuvBXafVevi2PMO7x9qyJYBEyZfBGl5rbGIXqKpgNhfk7qaFWMnjuqRpvRlxl1fJn1s5qAJ5D7Djt0Qp37pLZju2triWgSjKFrJZsImTzhQw1DI8nByELvSIgE5vgPPnuXD_FIdfTeXceJ3Qvk0F0Bt9vjXZDKUfJohljeM45ZpZKVcujTZxVuz-ssizTOVWkHT6pqwnhZV092rSS7PlnFpHZYxpZ0iXV-QgHvXBAhR1IowhLu7Q9MMl8qt_RatYipSUMCrTj15RU-BELuzj7qTpJw2BV8oeJydXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1elUZWFLveG_w9WNHPJR6Lpfl4m_v8zq32okKdssFfXnaZuaPqucYhWuUbDtowUTI-3yodRDQua9KJnmb8i0nD6cZvzcNoYa0RfcWM7LwH7E9113fMxupzqiWiAmbaI7a5qSzhxGuJeME9lwQ71fV6MOwyKyFPd6syHwWZ0jNot2_wr6QiOKKfNY7EuFz113ZEUGo_R4ghjk5XRDKncJvaOEqZ9VDEOimUSxmnbNcsEreQCfMvY4TU7RiZ3hQ2urBHjFiQA5RHSZ-9U5MlmzyS6YQ6fPtpI3zmWQLwzbJsXReodAmxb7FMoHpfyGk4I0DnZvWLBSNgZGrHT781i3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyY8yhistIOtMi6V6ZcwS6HNkAK1kOYTRhlcPDn5gSpWLOc-kkT8-bRLeTfgvbwmhAlzsHPf360ywOQQAWaYnQOm2JuhNmTTcTGCBta_uZo5ajwoRD53wDQElY1eXEkordkbfScf1Ze_RlHR41Kx1NSiZWmuB0S8bSnogoVUD6PLCfGOSdPLfsaqigtr54LnouWoVGcMqS5PuOZRtYB1X0RIU9HqW0Vav9k0C4HWtLw6YjQYJsr-PvWfNsVFmNzXez5PARZ-5cvHGeHzgVHBhgBUawRyjYMVAOk0KF9WMcU9Z6ocbMa3QDFc2MBYPWMRQPy9uMx83BaIu0roXDfMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQT684p1ShEwfRWvJrH4ONnzezoi2hzH5urTn6DewN214YaukU1mlzIdYLkOuKMB6QsuYG0aJNRzN8qKrPN2BYyCsbc18af_XAs4O1-ReGpEDupYoynGBzyi_OgnnBzSEcHS_FrrnO8K9Kowac-K-0n8PoqJZZHGzbWdM8raDpIHrma5lzFw8KYO-6av93lOgvUXWK9t3EVSFHwEDb6jWjuc8P03mEiUjySzL6LJuKgso6U8qb3MG1PA9kQ0SGFHy5pZKwfp6UoVs0tEjUE_QIGPGG9FjvLuqeHygJ_MvJuXkp5PxSlygF6gOPUHOAk03VbE5AuE7W0aZ2cB0rPIUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
آغاز دوباره تمرینات پرسپولیس برای حضور در تورنمنت سه‌جانبه؛ پرسپولیسی‌ها پس از وقفه‌ای چند هفته‌ای، کار خود را از سر گرفتند
.
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133062" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133061">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133061" target="_blank">📅 21:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133060">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
قالیباف: اگر دیپلماسی را صرفا گفت و گو در اتاق های دربسته و لبخندهای دیپلماتیک بدانیم، از همان ابتدا شکست می خوریم و اگر صرفا به عملیات های نظامی و جنگ تکیه کنیم نمی توانیم از حقوق خود به طور کامل دفاع کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133060" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133059">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=KM2gIxmyl9TaUcWItWWdG20zVremvsH_pBe3zTc60mWVHC-KduuGRBYg1DVTfOpBhiCqAPafM1nbLclUoGwi4v_yJtaHGu0n-4etdKpT0r4siD6OF2Nw2FAriyhXN5ppq27vToy9tkYpQO0eW8LIYNnhy2C7IWpDvTV1pwW3AwYZhSeKyZD2etFKDKY8imh2kh5jKfl31R1njBZzqNnkPOtt4OiiU9HRyY67wdPwIHbc43RNbgUw692XsvYWtu3FzOUnUxP8GfUo_diAJqIi06YgESQMb_Evxta3-TW-33j_ZojYoB1OmF5ckNkOX7315ci9PEN7s_VsaiAjwV8PMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=KM2gIxmyl9TaUcWItWWdG20zVremvsH_pBe3zTc60mWVHC-KduuGRBYg1DVTfOpBhiCqAPafM1nbLclUoGwi4v_yJtaHGu0n-4etdKpT0r4siD6OF2Nw2FAriyhXN5ppq27vToy9tkYpQO0eW8LIYNnhy2C7IWpDvTV1pwW3AwYZhSeKyZD2etFKDKY8imh2kh5jKfl31R1njBZzqNnkPOtt4OiiU9HRyY67wdPwIHbc43RNbgUw692XsvYWtu3FzOUnUxP8GfUo_diAJqIi06YgESQMb_Evxta3-TW-33j_ZojYoB1OmF5ckNkOX7315ci9PEN7s_VsaiAjwV8PMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133059" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133057">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
🟪
چلنگر، مترجم برانکو: او نمی‌خواهد به طور کلی سرمربیگری کند
‼️
مذاکره پرسپولیس بسیار محترمانه و خوب بود. حتی برانکو به آقای اینانلو گفت اگر یک سال پیش شخص شما با همین ادبیات و محتویات با من مذاکره می‌کردید شاید الان من سرمربی پرسپولیس بودم!
🟪
اما در مقطع…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133057" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133056">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حضور وحید امیری در تمرین پرسپولیس  وحید امیری بازیکن پیشین پرسپولیس، برای طی کردن دوران درمان خود در تمرین تیم حاضر شد.  به گزارش رسانه رسمی باشگاه پرسپولیس، در نخستین تمرین تیم فوتبال پرسپولیس بعد از تعطیلات، وحید امیری بازیکن پیشین تیم هم حضور داشت تا روند…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133056" target="_blank">📅 20:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133055" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oie7G_s74ocX3xMtEyFJUvGxEIKk979ts5N40vC9Lo8gk-a0byK6SLTcBk_UR-ezAsR28gtfHYzcINLxuuJLsR-mZB35mPpMF8DmMGDfXQq8M03exyRdXX7CEPWqx5oQTMgBaijj6PtNoR9qMyrJsFUzOcUpddTJ2O9ORPdxA6tXV-KiIAi1jt6Cp3rnQrEDQoyhfI7Ju1QeMdw_gHXgdFhTyVtj4MJzqBaGR-FYoYenSKWUftjx6oV-9CziQ5MFecpW3fnLfgMr95oTHq60fGBX1qmTLvgSenIiKvU-S5WDEhIgpHZ-CDPlub9T37SlvFahKWSCH2lmSCv68Jca2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تلنگر | #افشاگری
🚨
‼️
نفر بعدی کسی نیست جز مدیرعامل اسبق باشگاه که در این روز ها تمام تلاش خودشو به کار گرفته تا چوب لای چرخ باشگاه بزاره تا پرسپولیس به آسیا نره و به پرسپولیس برگرده…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133054" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEPuaVrFTYUPmttJTCOtb-nILvskh8W4j3QDjSViI1zTxJM7cPT-7sH7hQEq2g3r_vANdIK8Nkq0WXrGtfCvgSYz9MJaBHpEDcP2Tkzz1aHx5KoplT9Rd5JzgOOkWL9HIjiB8S7oBLRc5BIy9sfFGO1GWGccbnzngR1q5qhCHtCkh8cuOBuHGL34s3_68QJbz7r7ztUv93lT2vhXZUZhPSRzFT1m9k7-XFEG_S_wExBtisKMi-P4-SMFP6ypQodrM_iIeW9G80SxoUblhEwISEgM5YrcZkCb36fddjTXtbYmqZmGsh4r_L3qlTd0Br_0-Ny4rcoTt3wbw6SNxUQI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133053" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133051">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133051" target="_blank">📅 18:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fygLnEAIb1kJMbPvVnTAdMMGylZqjdwnKd6WXogn272rCsLOHflJW-hThdx6LfvATsek2TMJlpGVsrp7qezpGrkQVuqaHLySZrcdEJoNlQDIlUQG7MGVGhts8Nn7wgqFuWWbPIfDEc_DOPS-YkW8aj8MF3M54YK8pMlMIFk6hA6fjqQehaNRe1NzZw0UAxNiLV4Xfun4P8XEEBNJyb-BbiewHosmNCw3RLNsdHygeUs-wsYzde8cjqwjFJbZEAOlkulgfc652qZ6cPPkvpLEYJDvVNusmDb2mIIK1Mv2qV7ctjMmp3V6AyBNPRiq4Z9-Xv7VFu0ElqOmjllxQ3MHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مصطفی قنبرپور، پیشکسوت پرسپولیس و مدیر اسبق این تیم، به‌عنوان سرمربی تیم نونهالان(زیر ۱۵ سال) و مدیر تیم‌های این رده سنی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133049" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
کرمانشاهی، معاون پرسپولیس: بنظرم مسابقات را برگزار کنیم خیلی بهتر است. اینکه سهمیه‌ها براساس جدول فعلی باشد، خوشایند باشگاه پرسپولیس نیست. پرسپولیس روند صعودی داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133048" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس همیشه خواهان جذب علی قلی زاده بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133047" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133046" target="_blank">📅 15:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqgwWOcS56090OBK5tDKT_JVZIE6NI3UXtwUFIf-a8H8GsUTack0czC35t0j5UyUOLM70xW1eNhofDespCDMVx1qJuhZGjOGmJz7pjVhxKid-G1hpJ4zQUtUNDosyDFZvvCmizsjc2EuvSN8Kks5dKKIMj72tI_GE3K0erMNgvk8B5vY25pk50_myinXqpjJWsi5N8JmkKiZojsGjVIdkMquSQQl105k-RcTkn3NQxz0Zu97HWrPRUfRXYZFHwZ9t9-KYPCERAkGBeOEsiEEjs38XleLNutkrm4wUGEqXfLROUcPInNRyJ6vsnfMab95hidj0lmLj-6y6TciwKBf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133045" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
🔴
فرشید حقیری: حدادی 3 تا جلسه با خداداد عزیزی برگزار کرده و خودش کامل در جریان امضای قرارداد هستش برای همین نمیاد تکذیبش کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133042" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👀
صلوات بفرستید…..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133041" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
صدا و سیما: جنگ پس از شکست دشمن به پایان رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133040" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
فووووووری/ با اعلام قرارگاه خانم الانبیا جنگ ۱۲ ساعته و اسراییل تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/133039" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133038">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133038" target="_blank">📅 14:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133037">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/133037" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
