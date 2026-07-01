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
<img src="https://cdn4.telesco.pe/file/TKzzx13pQ25N9g9POIjlcvconfMgALIcTWtwV4OBNuhGcZZYkulVB1snPIMpNaqpDdVSl_cjziMJARugr5g2AQFUGhLIU1LR6pumS5yxuqqns5K91-3mW_B8VS1chc0HKpL2Rop9gLcqnJ8zsZxtcNeJF4LMnr2o0hJpYJsnt3gzLcHBpYzncTmLSQL5wb7VVPit-HvBRzEphRNonWtF8PcOy1GIQ6z31SVn2NzFnh2QKzv_gkQZJp7Ry2tzO-g08Ck0l_cUEHv55yoAh0ehS9KW0lGPUGPLpzkdtva02R1XZTCbj0-2wNQ0aa1v9C-0cFQFfu5CLY9Y8h2OfMHCsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-131252">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مرکز تحقیقات صداوسیما: تماشای رادیو و تلویزیون در میان جوانان و نسل زد تقریباً در همه کشورهای جهان کاهش یافته و ایران نیز از این روند مستثنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/131252" target="_blank">📅 15:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131251">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESe5oJ9mOG2lo8rvKI5VJhXR9Ag9SSOd4zxXuxsFdRo7n0EJYtPFelRh7hWVY1Vb7nhUaOVDwMU_ID4VkBgboWLcF_2NHKcFBxIGUAIr9kotxrr-_Nrl1cbP8OJLHdGZMZNN0qT8vcjFBMSyPStuUHkhSnbFhXCfQDW5-TTCVWHhnut-r6MuIVLQrNilKU6d9qEae_Xp1zb-PbCwW-ucuO89pUac-tNU23TZIKUMkhzjMY-6qXNAET8tvtwWiGo-H03ZdeDAv_GtXGCAFbxjuM2WTzeLUrmXWtKm-TV8btNdNCvlOVfmcJMeSptPkhZf9wdU9Djgb_h5a7l8LZWMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منابع العربیه: توافق اولیه برای آزادسازی ۳ میلیارد دلار به ایران حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/131251" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131250">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
جی‌ دی‌ ونس : فکر می‌کنم کاری که رئیس جمهور به ما گفته این است که از این تفاهم‌نامه برای پر کردن مجدد ذخایر نفت جهان استفاده کنیم و بعد ببینیم اوضاع دست کیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/131250" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131249">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCn1f2qrXJgN1dS0F64rUveGJL3egVS9mV2cjyMGYy0-lOREib45asYKGMDr4sqAQgWrzl4WjURBLHLf_DWeKzUme1y8BYYX5CUv6oJ4k3roD4-vcXdnoRbbFi_M3comR9NVTNbrVmvyd02MaLnDVhS99NiQCy14HZaOzSGaT0X9kWo7w55C3sLC9niiShryxNbV7z_UYWMrDm3_WJatAYMgKy2-BgrKx6YLr-hsgHkVlnEYTLaTr2Zb3Mb2nV5_LWd8KQLmYWz_HZTjx0FoQdNdSertkPF6tN91puUBTBq1ynmaChFAkULDXXlMx8pDDdB4yVa1cFTq7Mhepy3kQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه هواپیمای دولتی روسیه بعد از توقف یه ساعته تو تهران به سمت مسکو برگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131249" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131248">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
پزشکیان:ممکن است در برخی مسائل دیدگاه‌ها و سلیقه‌های متفاوتی وجود داشته باشد، اما آنچه باید در این مقطع تاریخی به نمایش گذاشته شود، وحدت، همدلی، هماهنگی و انسجام ملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131248" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131247">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قدردانی پزشکیان  از تلاش‌های قالیباف، عراقچی و سایر مسئولان ذی‌ربط در پیشبرد مذاکرات:
مجموعه این تلاش‌ها در جهت تأمین منافع ملی، کاهش تنش‌ها و تقویت جایگاه جمهوری اسلامی ایران در عرصه منطقه‌ای و بین‌المللی صورت گرفته و شایسته تقدیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131247" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پزشکیان با اشاره به ارزیابی مثبت مراجع عظام تقلید از توافق و تفاهمات اخیر کشور: تمامی بزرگوارانی که در این سفر توفیق دیدار با آنان را داشتیم،
از روند شکل‌گرفته ابراز رضایت کردند
و آن را اقدامی مثبت و در مسیر تأمین منافع ملی دانستند
🔴
خوشبختانه دستاوردهای مهم و ارزشمندی در حوزه‌های اقتصادی و تجاری حاصل شده است
🔴
استمرار صادرات نفت، تسهیل بخشی از محدودیت‌های مالی و ارزی و فراهم شدن زمینه‌های جدید برای توسعه همکاری‌های اقتصادی از جمله نتایج این روند بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/131246" target="_blank">📅 15:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131245">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSx4D5Ro3tvaBpn9u28xQOQ3W9CDyiwl6CxcPEPyIJE-pzHyXrhauF_dAwxoJT04CEsh3c2dyQg4ZjFSsmMDmrKXhTy1WGulY90v41oJAanbg2dYvgrbUaGcw1vNKL8mGfLN81ff6c7Xj_5FOGx8FGeSgGlzQkBMQ5yX_G0_vwaK7vviWndHDhuwQbzhs3ubLbmgztCQJqAEB_53x-eLn2A20Og4VqjASA6ulX9CNAvLWcCqVcuJzfjcXc3Hpi5eJJRLceQZyHwRKNDE-oN2r1YtNmcjKDnoGX7wKGlayT_ZyKB9SdCU8gYXiiK5AkdynSKpCrBS5fdDGzUetXLPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه
@AloSport</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131245" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131244">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_uaehGpIvVZ6GOZB8JCT5NMmbehuD6sI782WbbwMPsnRypY5LCftTKV3dDXi-t8DvueFwyPG-I4Ys2-t8rWI4QldDJ2IWoW0w2qdlB-v2ETqWi1S80SBL4N1G81YVRPmKbaGRw2aBSp2j6-5g6hkDV-AnJsoVlLGNXXm0-nzXtU3qNHjEETVFGXo2cQFxnYfIRk6aZMCl2-K0aMpvsdeySPZnK9zkt2wg0w6M3MM6nYOd080ARMNL9uEAHtlY9-R8JGLNN9cM3gl7dFoTCY_eigvUh-CQL3QEr7kBtHMp4QJheMu1fUm-HsMKfwDA2I150VfIMAe4Uja2ZUaVJE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی خطاب به آمریکا: اگر حیوان خانگیتان ساکت نشود، ایران به آنها درس می دهد
🔴
توییت جدید وزیر امورخارجه: ترامپ آمریکا را به «ساکت کردن حیوانات خانگی‌اش در تل‌آویو» متعهد کرده است. اگر آنها ارباب خود را نادیده بگیرند، ایران به آنها درس خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131244" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131243">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
غریب آبادی، معاون وزارت خارجه: گفت‌وگوهای امروز در قطر متمرکز بر پیگیری اجرای مفاد یادداشت تفاهم است
🔴
کارگروه‌های پیگیری اجرای تفاهم و مذاکره برای توافق نهایی شکل گرفته است، اما هنوز مذاکره‌ای در این قالب‌ها شروع نشده است.
🔴
رایزنی برای تعیین زمان و مکان مذاکرات در قالب این کارگروه‌ها از طریق میانجیگران ادامه دارد و در صورت فراهم شدن شرایط لازم، مذاکرات در قالب این کارگروه‌ها آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/131243" target="_blank">📅 14:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
زمین لرزه‌ ۳.۳ ریشتر تو عمق ۱۴ کیلومتری زمین، پاکدشت تهران رو لرزوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/131242" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131241">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6DpotSYwUigSvWY5qTKRNAmVRi4NLy3eyg9yPWlHR9HhlAAEsOYj8IAFCCNrBqIBZLJ_PI1AKAEtl4nEkRCLCTsARNoGnMhWNqP4RIYUuHTSJpHhLuWOIFKLIuKaITUWTdoYIa574goBtqv9APnR6ldxb-A_Yyi0JrE_zBiA4Oc4ME-KV30jX-xnQ_mDcJIpj8acBj5K6tCPX0yNiFIyMYbQq53EyZejH_GlcU4yYjttdxt0mpoMAx26MlQwsa9axv51k7NQtQNO0rHz66ufozX4PkK_7-GXLdEVR2GxOrWWfsmsUG3B7W8RnfUpUuydcbiY95r8S-FYPi50VGrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم کارشناس ارشد صداوسیما:
چین باید میانجیگری کنه چون ما به قطر اعتماد نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131241" target="_blank">📅 13:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131240">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا که تحت کنترل جمهوری‌خواهان است، با ۱۸۹ رای موافق در برابر ۲۳۵ رای مخالف این قطعنامه را رد کرد. دو جمهوری‌خواه از این قطعنامه حمایت کردند و ۲۲ دموکرات به آن رای منفی دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131240" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131239">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بخشنامه تعطیلات هفته آینده ابلاغ شد
🔴
بر اساس بخشنامه رئیس سازمان اداری و استخدامی کشور به دستگاه‌های اجرایی: روزهای شنبه، یکشنبه و سه‌شنبه ۱۳، ۱۴ و ۱۶ تیر ماه استان تهران تعطیل است.
🔴
دوشنبه ‍۱۵ تیر سراسر کشور تعطیل است.
🔴
سه‌شنبه ۱۶ تیر استان قم تعطیل است.
🔴
پنج‌شنبه ۱۸ تیر خراسان رضوی تعطیل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131239" target="_blank">📅 13:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
برنامه‌های برگزاری اجلاس ناتو در سال ۲۰۲۷ در آلبانی به دلیل مقاومت دولت ترامپ و انتقاد برخی از متحدان به خاطر هزینه پایین دفاعی تیرانا، در هاله‌ای از ابهام قرار دارد، رویترز گزارش می‌دهد
🔴
پیش‌نویس بیانیه اجلاس ناتو هفته آینده در آنکارا، ترکیه، آلبانی را به عنوان میزبان بعدی ذکر نکرده است، با وجود تعهد قبلی.
🔴
یک منبع گفت برگزاری اجلاس در آنجا ممکن است رئیس‌جمهور ترامپ را عصبانی کند و تیترهای منفی ایجاد کند، در حالی که دولت آلبانی پاسخ داد «پیش‌نویس‌ها پیش‌نویس هستند، نه تصمیمات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131238" target="_blank">📅 13:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f0ade05a.mp4?token=Mh0oo5l_DN9S4lqZvKWLt0mdmjW0ltV9wsYswdlPb8RD54-M_kLcagoUlJ38zdOaDg3kFMx6QHs8s3Q0Xs9McbswMzWu--lFkhMpX_6ywdrJ4eathPsOYXK4IZozpmf7vTdjX0MWi01CgJcJQY3qGLd3gXwiIJYsHiSd75u2p4XnW1n-O1u8IIxk4i4aWdq5lQ6wuyt31FEqhLKNfozxFYJcDIGiy-KYy-pkkB9p2B-_MCtLsDigL5NTJr3Q09ZFXiT3iIafI2XaC3guubHQNtAnL29j4RkWmWwrHTkyigAEetqlU8fsmafm6T7RAl74ZoC_m-GRHTH6DQkadmqIpR5LYbjZtrlvxnKuGf-iF_RzEUgbtbHtZeN_J2XRFXKm_7bi21C2RUt4QzVmaFVyLKM7KvW00bcCchtBtS4mxM8fiQ0xexjC6-34q1QpWHHKZaG5mvsou1echxLyVfP47_brzfKBTjnB9iWoD2lGlUDc-N8K5GBGjnw2nBx9PWwcBFtNrI9w88gEH5qNl2EpzsZMia4EzdtTCo_VgV2FLt2Z_y_2ywnI35-8MAY5buK56opmIg_udoXaTcb_62YFwtastWhaklJ5yQ3j0jF12toa27iJmloC6cDqnLUwq1Fm416X6vSk4925Cu8JfEbLezsAS5DmJwEPT8rXRAo6VnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f0ade05a.mp4?token=Mh0oo5l_DN9S4lqZvKWLt0mdmjW0ltV9wsYswdlPb8RD54-M_kLcagoUlJ38zdOaDg3kFMx6QHs8s3Q0Xs9McbswMzWu--lFkhMpX_6ywdrJ4eathPsOYXK4IZozpmf7vTdjX0MWi01CgJcJQY3qGLd3gXwiIJYsHiSd75u2p4XnW1n-O1u8IIxk4i4aWdq5lQ6wuyt31FEqhLKNfozxFYJcDIGiy-KYy-pkkB9p2B-_MCtLsDigL5NTJr3Q09ZFXiT3iIafI2XaC3guubHQNtAnL29j4RkWmWwrHTkyigAEetqlU8fsmafm6T7RAl74ZoC_m-GRHTH6DQkadmqIpR5LYbjZtrlvxnKuGf-iF_RzEUgbtbHtZeN_J2XRFXKm_7bi21C2RUt4QzVmaFVyLKM7KvW00bcCchtBtS4mxM8fiQ0xexjC6-34q1QpWHHKZaG5mvsou1echxLyVfP47_brzfKBTjnB9iWoD2lGlUDc-N8K5GBGjnw2nBx9PWwcBFtNrI9w88gEH5qNl2EpzsZMia4EzdtTCo_VgV2FLt2Z_y_2ywnI35-8MAY5buK56opmIg_udoXaTcb_62YFwtastWhaklJ5yQ3j0jF12toa27iJmloC6cDqnLUwq1Fm416X6vSk4925Cu8JfEbLezsAS5DmJwEPT8rXRAo6VnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشدار گوگل به میلیون ها شهروند ونزوئلایی قبل از وقوع زلزله
🔴
در حین وقوع دو زلزله سهمگین ۷.۲ و ۷.۵ ریشتری در ونزوئلا، سیستم هوشمند هشدار زلزله گوگل توانسته بود چند ثانیه پیش از آغاز لرزش‌های مخرب، به بیش از ۱۱.۴ میلیون شهروند هشدار بدهد.
🔴
از آنجایی که ونزوئلا فاقد سیستم ملی هشدار زلزله است، این فناوری که از شتاب‌سنج گوشی‌های اندرویدی به عنوان حسگر لرزه‌نگاری استفاده می‌کند، توانست زمانی حیاتی را برای پناه گرفتن در اختیار مردم قرار دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/131237" target="_blank">📅 13:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نتانیاهو: ایران سعی کرد ما را مجبور به عقب‌نشینی از جنوب لبنان کند، اما این اتفاق نخواهد افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131236" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/131235" target="_blank">📅 13:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c28e55c3.mp4?token=szkrMUXtmLfxUQI3UV02TRUPMWxxqOm0mlDEJJsJRgWvMCqZ2Ghc2se2vwq5XyYWlpINEnY_JAxnkGC1gCYMvFjEuF-jSWnLeXgeOZKtx3ZCsVSITJlQEYDAhrQ08u4zy6b8z1W0aSTC2lZ4UJpDKNPZarjQ5l--PVaNePdFeyCAGaMNoRuIqCDOaWSc9LUrwsPdRwFIPoL9BrW40xWfFiG2Mkpz63eB1hAsaSIKkt1KXFyITlPbS8Go5T3Sf213AqTYGMgKiw8a-r32TNk6V1n5FgTNLjS5sqAD-ie-VxA3V2ac-tnEha5ERd1xYlOS73KjXE9ZDQ0L2sh4EvTHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c28e55c3.mp4?token=szkrMUXtmLfxUQI3UV02TRUPMWxxqOm0mlDEJJsJRgWvMCqZ2Ghc2se2vwq5XyYWlpINEnY_JAxnkGC1gCYMvFjEuF-jSWnLeXgeOZKtx3ZCsVSITJlQEYDAhrQ08u4zy6b8z1W0aSTC2lZ4UJpDKNPZarjQ5l--PVaNePdFeyCAGaMNoRuIqCDOaWSc9LUrwsPdRwFIPoL9BrW40xWfFiG2Mkpz63eB1hAsaSIKkt1KXFyITlPbS8Go5T3Sf213AqTYGMgKiw8a-r32TNk6V1n5FgTNLjS5sqAD-ie-VxA3V2ac-tnEha5ERd1xYlOS73KjXE9ZDQ0L2sh4EvTHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرین شبیه سازی حمله به جزایر ایران توسط ناو باکسر که به تازگی به نزدیکی ایران رسیده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131234" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ایرانی:
مذاکرات دوحه بر تنگه هرمز و پول‌های بلوکه‌شده متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131233" target="_blank">📅 13:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وقوع حادثه دریایی در آب‌های یمن
🔴
شرکت خدمات دریایی انگلیس اعلام کرد که یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131232" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr_XE3UeNxeghn_npE5XYZKwcAdk90JqTNl9V2NypPenwEH1osTfzJ9dgNqzn6HGss6M9NuXjnE-yNwK0Ex4tohJrzSwUYRskSSlB6gSF8YR6IbcZ3BEQU8FJHwlnWlAkxg9R9fr8HZkycLF_clBp1W1yGZeXmrEUDvwR3iuc8S2Df6fKgUwyABp8Zbhec2t6dQEHOV3SIui6YOYw9Pr0e0zcxp9X3UueSELapF87nAO8mooDWjyfmKVW0ePhubRkdLHZB1X4JBJXSgnfZN9TcjpPDDU33CjssSl7KiK1ff8c55uxnK2hZpEiuonk0NGKOv4mfZBX2ZMioI1zzkliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۰ هزار واحدی به ۵ میلیون و ۱۸۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131231" target="_blank">📅 12:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
صداوسیما: یک فروند کشتی که از مسیری غیر از مسیر تعیین شده در قالب نظم ایرانی در تنگه هرمز، تردد می‌کرد، به گل نشسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131230" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: در طول ماه‌های اخیر، ۲۸ پهپاد با موفقیت وارد نوار غزه شده‌اند که بیشتر آن‌ها به دست حماس رسیده‌اند
🔴
مشخص نیست چه محموله‌ای با استفاده از آن‌ها جا‌به‌جا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131229" target="_blank">📅 12:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
الجزیره : گفت‌وگوهای فنی ایران و آمریکا در قطر در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/131228" target="_blank">📅 12:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کوشنر و ویتکاف روز سه‌شنبه با نخست‌وزیر قطر دیدار کردند تا زمینه‌سازی برای جلسات فنی چهارشنبه انجام شود، اما خودشان در جلسات شرکت نمی‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/131227" target="_blank">📅 12:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9119f36555.mp4?token=j2kaddvR8Gy2aSL2nxwFHCjoBekXcwHvIco6fpXiS55-EMypb5PAIP-fPVzaV2pMIMcNzAHKe-dU6onat1mo5ZoVsRZLeQBxW8QswBI6W7mArbhhPC6CGL9N4zazzu_wenTzRHoYL3EqoAMl5hLak7X3IoxNh-0JRyrb_O1dvWaNFkN8r13af5N9JD6k2PR7BKT8IIzqnTpRxS1dFlcp7A_VuZL-Nh3FTNTqW4xGzOnrbeetvBgihZIC7EWByM_zlotVGS5iuP7ej_ggvvc4ahYnslZh1JWJ29qivn3ZO5pRnNDKu98VgxAf0Y3jPcbvcXzZXedD4G7hjCrycKWyTAemTYClxxcGbDproXx_AXyXsl45KZkYVeglg44OUbm7NsT1VMO9nyBVSXxhZwASrM7qxQ1asI-9gRZvtAIFi2EP1w0rH5fzsZu9kE_CS22fbg1anwlSlSzS61edZ-Fgr2mWV7u2MuJvvWv-NStSE_IV-V89O4gocF3autazV_wIqfhB8N5qrbdQmlaOp1dgEio49jONptvh6rNjYEgZHMkYxjLjWJwK4_tAIed-pOyEyNfYb5NnrBQaspDexHx1MPqywaeajiAZLTeMrJdAxyWEfex9F8Rwe8L6bz3Wh6BJ9NwefwiCzlbtbspnLiJpDrIVJ4Ie1Vbg42ekHsRoz8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9119f36555.mp4?token=j2kaddvR8Gy2aSL2nxwFHCjoBekXcwHvIco6fpXiS55-EMypb5PAIP-fPVzaV2pMIMcNzAHKe-dU6onat1mo5ZoVsRZLeQBxW8QswBI6W7mArbhhPC6CGL9N4zazzu_wenTzRHoYL3EqoAMl5hLak7X3IoxNh-0JRyrb_O1dvWaNFkN8r13af5N9JD6k2PR7BKT8IIzqnTpRxS1dFlcp7A_VuZL-Nh3FTNTqW4xGzOnrbeetvBgihZIC7EWByM_zlotVGS5iuP7ej_ggvvc4ahYnslZh1JWJ29qivn3ZO5pRnNDKu98VgxAf0Y3jPcbvcXzZXedD4G7hjCrycKWyTAemTYClxxcGbDproXx_AXyXsl45KZkYVeglg44OUbm7NsT1VMO9nyBVSXxhZwASrM7qxQ1asI-9gRZvtAIFi2EP1w0rH5fzsZu9kE_CS22fbg1anwlSlSzS61edZ-Fgr2mWV7u2MuJvvWv-NStSE_IV-V89O4gocF3autazV_wIqfhB8N5qrbdQmlaOp1dgEio49jONptvh6rNjYEgZHMkYxjLjWJwK4_tAIed-pOyEyNfYb5NnrBQaspDexHx1MPqywaeajiAZLTeMrJdAxyWEfex9F8Rwe8L6bz3Wh6BJ9NwefwiCzlbtbspnLiJpDrIVJ4Ie1Vbg42ekHsRoz8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
یکی از چیزهایی که وقتی سفیر شدم یاد گرفتم این است که باید هر روز خوراک شبکه‌های اجتماعی ترامپ را چک کنی.
🔴
نمی‌دانم این را می‌دانید یا نه، اما او معروف است که نیمه‌شب از طریق شبکه‌های اجتماعی افراد را اخراج می‌کند.
🔴
پس اولین کاری که هر روز صبح انجام می‌دهم این است که بیدار می‌شوم، حساب توییترش را چک می‌کنم و می‌بینم که آیا اخراج شده‌ام یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131226" target="_blank">📅 12:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رویترز: مذاکرات فنی غیرمستقیم میان آمریکا و ایران در دوحه، با میانجیگری قطر و پاکستان در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131225" target="_blank">📅 12:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دلار هم اکنون 175,500 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131224" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
فارس: ارزیابی‌های اولیه حاکی از آلودگی نفتی بیش از ۲۵۰ کیلومتر از سواحل هرمزگان در پی حمله آمریکا به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131223" target="_blank">📅 11:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:  خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟ پسر بچه: آره، جونم مهم تره خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد. پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131222" target="_blank">📅 11:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=NNYpfd-Yg30mE7H0vCYBYc6ku10gyoB4b3MMfXTHTTa8lzZ4w--9m70RvYb_SgbnhLZDc33RpEz4zZ6slrFVeVYWvOmSZDOATkKx2T-tWJEvv26P2-PG9xVMjERPG-EfBlWzh6nyU4qcIj8WOlL0SsHDbL3Gxo28skDsb2MZPc9RKNMdh1OwXJosMWApDVagV_tY5pkXITM_OzIEvxqHB0DkGohWj-VFizkKdNYTmnPABDPI0BL8-oogP9KH2i6gzWu0u1WnqjBNeCjnR7W7l0ckpoLB2MvSNR4nx71-1AEpd6c23pVclNZWro0CpR-CjKXz4TmHT87umaUx-uv4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=NNYpfd-Yg30mE7H0vCYBYc6ku10gyoB4b3MMfXTHTTa8lzZ4w--9m70RvYb_SgbnhLZDc33RpEz4zZ6slrFVeVYWvOmSZDOATkKx2T-tWJEvv26P2-PG9xVMjERPG-EfBlWzh6nyU4qcIj8WOlL0SsHDbL3Gxo28skDsb2MZPc9RKNMdh1OwXJosMWApDVagV_tY5pkXITM_OzIEvxqHB0DkGohWj-VFizkKdNYTmnPABDPI0BL8-oogP9KH2i6gzWu0u1WnqjBNeCjnR7W7l0ckpoLB2MvSNR4nx71-1AEpd6c23pVclNZWro0CpR-CjKXz4TmHT87umaUx-uv4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
پسر بچه: آره، جونم مهم تره
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131221" target="_blank">📅 11:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZkzIxhsxZ5FYyRFm30sMzEQARFqOdAJIrinONBHo7OgP2G2mr6K5hLR5ae4YYM6Qi6va7GAMewDF1hQ18LTTscwvvDu6UsRpNY52PCb5t56XMSDfUOcPvi3ybSL0Ias-CGpox8WE77B21-X0F5ZH-RuMU_VZhA1C5Djw66vvmrAeVODRhgZWSB0O5czn5UxcTAJTMUMP2j5y0SohYWvH0ywY_jMFz_L22c5xHz7snPLAi4WVQe6kXTtzHmVecCjrSYKMiVjf-_B9JC5ju3R9Zdo5CltjSHsXAcBLF7IQRHktOylqxo89R9ImGAWzXmjbrjSTTqEq5ReQ591PmY_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: اگر مشاوران به پزشکیان اطلاع می‌دادند که ترامپ ادعای دروغ صفر شدن صادرات نفت ایران را مطرح کرده، رئیس‌جمهور نمی‌گفت «۴۰، ۵۰ روز است نتوانستیم یک بشکه نفت صادر کنیم» و ترامپ این سخن را به نشانه پیروزی خود توئیت نمی‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/131220" target="_blank">📅 11:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رسانه اسرائیلی ای ۲۴ نیوز: سیا و موساد اسرائیل نقشه‌ای محرمانه، مشترک و پیچیده برای سرنگونی دولت ایران در طول جنگ آمریکا و ایران اوایل امسال داشتند.
🔴
بخشی از این نقشه نیازمند نفوذ مسلحانه جدایی‌طلبان کرد به مرز غربی ایران بود.
🔴
معاون ترامپ، جی‌دی ونس، از این نقشه‌های محرمانه مطلع شد و بلافاصله به اردوغان ترکیه اطلاع داد، زیرا می‌دانست اردوغان سیاست‌های توسعه‌طلبانه کردها را رد خواهد کرد.
🔴
این نقشه در نهایت پس از افشای جزئیات آن توسط ونس شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131219" target="_blank">📅 11:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131218">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کوبا: مذاکرات با آمریکا متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131218" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نتانیاهو:من می‌خواهم کمک‌های آمریکا را متوقف کنم. این مثل کمک‌های رفاهی است؛ من آن را نمی‌خواهم
🔴
اقتصاد ما دیگر یک اقتصاد کوچک نیست... ما می‌توانیم همین بخش کوچک از درصد تولید ناخالص داخلی‌مان که از ایالات متحده دریافت می‌کنیم را خودمان تأمین مالی کنیم.
🔴
می‌خواهم این روند امسال شروع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131217" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار الجزیره : تهران خواستار آزادی ۱۲ میلیارد دلار است؛ البته نه برای خرید کالای آمریکایی
🔴
عمر حواش، خبرنگار الجزیره در تهران، گزارش داد که اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، تأیید کرد که دستور کار هیئت ایرانی به ریاست کاظم غریب‌آبادی، معاون وزیر امور خارجه، محدود به مذاکرات «ایرانی-قطری» برای تسویه دارایی‌های مسدود شده است و وجود هرگونه کانال مذاکره مستقیم با هیئت آمریکایی را تکذیب کرد.
🔴
تهران خواستار آزادسازی فوری ۱۲ میلیارد دلار در دو مرحله ظرف مهلت ۶۰ روزه است که با ۶ میلیارد دلار سپرده‌گذاری شده در بانک‌های قطر آغاز می‌شود.
🔴
در پشت صحنه، یک اختلاف نظر شدید آشکار شد، زیرا تهران شرایط واشنگتن برای ایجاد یک خط اعتباری انحصاری برای خرید کالاهای کشاورزی آمریکایی (مانند گندم، سویا و ذرت) را رد می‌کند، در حالی که به حق مطلق بانک مرکزی ایران برای تعیین نیازهای خود به کالاها و داروها بدون دخالت خارجی پایبند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131216" target="_blank">📅 11:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtx8ttmiKF7QqpNcl-qibJKEPdlcg-KNWw4LT2HS_Xixiu0jJvvPADZSEGOogNaHP2fwCwX0n-XsXiNU6-neor_nJU1_KwQw0NI7G63doa4UBBL6UM_nzOatRiYyZIxzWP7PF9MrgqyHCzg-hbZnhnHvDu0uAS0_af6300tqg27DMxN4vPtHFgaT6UzvNj60tqzQ7xVJ2hl7NuaQD5vjJSQiF6_hSkgFG_utJi_xjSe5C1MrnR_vaAZnb2wH2xlQ4M3iAJsmZpeUOpnt9fZNCaNwuK1nJc1TR482YShXSjsqip9_r39z8e7NhB5mUZwxq03A9InB9Vfb79yCTlK95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش جدید وارزون از نقاط استقرار ناو های هواپیمابر آمریکا
🔴
از مجموع 10 ناو هواپیمابر آمریکا ۳ ناو در حال حال تعمیر ، ۲ ناو در حال تمرین ، ۳ ناو مستقر در آمریکا ، ۱ ناو مستقر در دریای چین جنوبی و ۳ ناو نیز در منطقه خاورمیانه قرار دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131215" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLy1WZzNePsEBK_TGgQvL7bgpRe9wzIYk8Q6LCs_hcI0SKLTt4WCMfHaljcKJ0MLE5kjvr282sq-nmv2LMe-PWXM4iO7RF7kzpqtRlg_QIz3cQuokZpx57s-gBSDOGImPySQt0SnzH4JHMCrxJr4SZypsRYFg6f4Z8xjb3C7xeazBgVnQjJg1Pt1tXdggGHiC2pNhcdXwoKHnM41M0s8BoNdxdvfSChNYz9YXv9ozDLwf-HMMHhlaD-1mNC7V0pZfJgNrBqPBX5fVzzp0KitPYohJFSQj57FFwc403x1uuCzXYofcFx7ViaMaB79O0ftpXYQZSNjvbiPIdmEBFimIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی عضو تیم مذاکره کننده: ایران به سرعت درحال بازسازی زیر ساخت‌های غیر نظامی خود است.
🔴
ذخیره سازی اقلام حیاتی را انجام می‌دهد.
🔴
سیستم های تسلیحاتی جدید را پیش می‌برد.
🔴
هزاران فریب دهنده «ماکت» نابود شده را جایگزین می‌کند.
🔴
فناوری های نوظهور را مستقر می‌سازد‌.
🔴
شبکه پایگاه های زیرزمینی و مراکز فرماندهی و کنترل خود را گسترش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131214" target="_blank">📅 11:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سی‌ان‌ان: با تعلیق موقت عملیات سازمان ملل در تنگه هرمز، تا کنون حدود ۲۵۰۰ دریانورد از تنگه تخلیه شدند و بیش از ۸۵۰۰ نفر همچنان در تنگه سرگردان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131213" target="_blank">📅 11:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آمریکا قصد اعزام نیروی زمینی به لبنان دارد
🔴
بر اساس گزارش واشنگتن‌‌پست وزارت جنگ آمریکا (پنتاگون) در حال آماده شدن برای اعزام نیروهای زمینی ایالات متحده به لبنان است.
🔴
این اقدام با هدف اجرای توافق‌نامه اخیر و جنجالی با میانجیگری آمریکا میان لبنان و اسرائیل صورت می‌گیرد که خواهان خلع سلاح حزب‌الله است.
🔴
روزنامه واشنگتن‌پست به نقل از مقامات آمریکایی گزارش داد که نیروهای آمریکایی برای نظارت بر پایبندی لبنان و اسرائیل به این توافق‌نامه، در خاک لبنان مستقر خواهند شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131212" target="_blank">📅 11:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131211">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816b9c6962.mp4?token=q9k8Yi_Z3ZjYtVgJeBlXsovHClE-R8BMx1_Jj-XEMl_oIr-YLBDFITlflUUIzvPpSKn6vSWFWNeSKy8pGPodWgSCzL6Q-9j8cDc7ulEKRN9VYZlNxsi-lZVCdUIceoBLguy3Tf-BHVNKt7Y8N0QLwQ79XGdU5eLcI93tnwqMXXCnYPP6f3Pk-G4BVCNqLcY6Fu-oWIJhsCErsEDZFDBf0cn0V-bzjywmAjGiFHp-HDkwwmOvEmBPHb5eZx4sQSUrA_To_1LK3B1M7sOVGn4pM8igFFN1Fj-17aRggEFjrnjsMcdl_PFdV_SJ21N2-v0p43MzrY_ZD772HUclPohgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816b9c6962.mp4?token=q9k8Yi_Z3ZjYtVgJeBlXsovHClE-R8BMx1_Jj-XEMl_oIr-YLBDFITlflUUIzvPpSKn6vSWFWNeSKy8pGPodWgSCzL6Q-9j8cDc7ulEKRN9VYZlNxsi-lZVCdUIceoBLguy3Tf-BHVNKt7Y8N0QLwQ79XGdU5eLcI93tnwqMXXCnYPP6f3Pk-G4BVCNqLcY6Fu-oWIJhsCErsEDZFDBf0cn0V-bzjywmAjGiFHp-HDkwwmOvEmBPHb5eZx4sQSUrA_To_1LK3B1M7sOVGn4pM8igFFN1Fj-17aRggEFjrnjsMcdl_PFdV_SJ21N2-v0p43MzrY_ZD772HUclPohgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلی هانری :)
@AloSport</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131211" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131210">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🚨
قرعه کشی پرمیوم رایگان  دیگه همتون از پرمیوم تلگرام خبر دارید که باهاش میتونید تیک ابی و استوری و ایموجی پرمیوم رو باز کنید.  فقط کافیه توی چنل های زیر جوین باشید
🔗
@CRYPTOSMART_ORG
🔗
@Proxy1y
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/131210" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131209">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUGucUj3nwZ1EUG0XqSJ6md1oUAdTOA3ELV3xlqpMtX7b5vl9eswdFZR9XrjiD7hHxdOQaLb8aCHLjCUEQ9Q_u1lfcqSPMY9MBBSBOTpSZFllkwLKF2Ai_JtPArU8aSKid1_krikHxNPscVgHqvHLn0vXV9Jj80DNmz71OJQVTxvCV2LWJuivgZCiROkRhILvmVbCrlKpMe5Pot0kT7nQhjsYU87MXFCxGRA-JKWKIM33H-Li8SQ7dckOVH8WN-PN8XMHF_rarLrENS_HCW0Y9nS7KEC8DVK7tarVb2q3BlmaGz5RkOH53J6bJwKxvHRHLDcN8SA_IJ309RuSwQHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش فرانسه: ناو هواپیمابر شارل دوگل در خلیج عدن در نزدیکی تنگه هرمز مستقر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131209" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131208">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سازمان جهانی دریانوردی: دریافت عوارض اجباری از کشتی‌های عبوری از تنگه هرمز مغایر قوانین بین‌المللی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131208" target="_blank">📅 10:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131207">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فرودگاه مهرآباد از ۵ صبح روز جمعه تعطیل می‌شود/ توقف کامل پروازهای تهران در روز دوشنبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131207" target="_blank">📅 10:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131206">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر خارجه چین: شتاب مذاکرات آمریکا و ایران حفظ شود
🔴
باید توافقی جامع حاصل شود که مورد پذیرش کشور‌های منطقه نیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131206" target="_blank">📅 10:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131205">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پاکستان: دیشب طالبان بهمون حمله پهپادی کرد ولی همه رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131205" target="_blank">📅 10:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131200">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMWIXM_flBO7_wEbWEqTuFqB5Tqg7E7HgvDYtGvi9_lJNWG3oTNNdsWG6om0HNPLL7OrfcrHKDI75MQ_Kd9r4WV6Tr_QHKkqUJQkwVm4t1xC2SgAzHBLbJomnokE5m-ygNmLRnbe9iKQHMBifmsqch06IIKHKOh07b1COx7Ysgqj4YaWvReXbkVkbfuHSIB7nuXeGEx1oRz2Ljg2kOA11klEOFN5lDJI_FCuvMSAofCwKMHvgve_6v65GU77KdSsJXcAwJC-nq_7MUg7U9_GGd42QUe0I4VjrJ2bYH_L5h1jI40HRywNS5-4XSZDDEiAcH4d9GJKDd6byVHBuZ81zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3K2Fi5IpjpNdOn_GmP_Ut_h09mgaud9A3bIXCbh7w_Y1a5tEXhKd7R2MIjqcOF0gZLfXHDwtWNL1lchRGAEyvUa1puZkgrR0EUlw08Z0wIwIVOzVNlapKTzAzH-6rQLMzg4I6VC4jfWNHGneFs23bIX9gaunEMXx1rEfLoL4WEOGg4CRMlFE3XIStd4D1bD-A4hzAkAmzLddxumfhln7mmcSGBkPOknp_YXrH6gllwL9083Qoq5Emleffuci3a3HhSS_KF5535nlyOQYMv1p4zvzh0TlkVWhZVPTS5XGoqwdD59qOcCJcxJljLiYdGCX8UQZatQuoM_JYy15ffULQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbp01Kv8P-YQX7JT9QyEmHZ3qnTjEQWPbT_ziOgdao9p1n8ldY5lQgrKSh4cjEs5VVWsRZdFbYp5yQdFgUq8u-gySLb45Y9RB7AbyP5gjwFnH6pxfZsUJoPEdwwPchOvJ15tC9_Hlhehgu1uydttomDhBY64GTr7dHgNaFLxI45mSSm_JBJlYcjup98L4gj1mdRR0BOu7Yzx-NVYizUjYlxN1y_4J4H6bgJ6B090L6x7yHNXRbBYZfGrOjSIrcIVzxeOiFaI9QLT42a2SWblwLpPbzPZn9QHPkYExdPARIwfqJtzf6gG2OZ6Tgk5e11Ywuj1UHxT_091RJu0MH6mMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW6zz7NTLmAJXG7dml_X5ZS-HDU0PmHPpWSfeo7-I0PHGlo6A0gAqD4PnjMynOervJSnxIUHHSKWp6yIX7mnan1W1_d4q9D5Mukh7nSW_XC0pKbBDqSziztcx85kWbf-vlqqjm-7cn6H7toQcxRfqYnFryuMdqeCL3je9a5InsBVYOM7-e4M8tDvjMghSON2inCYOQqse0c4XUTqv00xWQmhNhum5nIEfHgU7OrLHQ2DpsZlDCQh5MhAelDvFDurJwD5nlxcZi0jHCskuUwPtseGxePU0KzVTi6pSM0CBx04pba0_JjWLOYmkmkvWE_Y-sZXDOh4toAzDPPZha3EIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2FDerybTrSqGdZR_ttTB833imwxQFm_nU4hUZJDd5DmrdqSp7gD4FvHzgClFHZ6yhVh5WNtCtZwKfUieo-Ai0aknnBBMZuR9_kqq2eeqyZzDbsdCzUc47W-kw73boQIHZbqOfPxH7Fp2yvpfv5phzoqFja8C0bgs4mVKnCgjr91eW0T_-fcScmCiWMmf9XMmQOb8hxALVb7nN3xTTfm27RDqqg6J-_-gI5qpM8ZEx47g8MzcQyrQrtt_6dNNMqFBvV13yocMEe0PTZIjxLDtwXZycTDtIcSk4wyCHUBMAdwYgbiLWZaRgKPIhUtnGtblRZAy6rDxsO0HCRrVBx2SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131200" target="_blank">📅 10:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131199">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd7mk-G2KV-316EhLCokWWdXAIsCx2b-k0ZFx1W8plXJ8BQtaakKdjT4zdpEe2vYV-GQlOdV0Qg0nC2IRcBz6ehNEYMsYB-Ws0njQTIM2TRKWNA2AgcTuAZuePLotNbADWjc8D6an7AT5iZ_SvalbfaPz4sLFx6qUD_NUu8yq2i32jfdaiD4mgFbFYvCXwriswrEhzee69nsbSTaw2bmBAlREEG12hJ7wF5gzdqvkNggx7iE5iJAfoao3wqtzmh0QHqnIY_pgOrDlceNHTPiBlUst-pY4IpSvpxX0yOyVINmKA4iEIf07OclA2ZyMHLAsZtFzjZNTEdyzGvLrcGEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ناوهای یو‌اس باکسر و یو‌اس پورتلند به خاورمیانه رسیدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131199" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131198">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131198" target="_blank">📅 10:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131197">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی دولت: سه‌شنبه ۱۶ تیر تهران تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131197" target="_blank">📅 10:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131196" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131195">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرگزاری بلومبرگ در تازه‌ترین ادعای خود به نقل از یک مقام آمریکایی گزارش داد که استیو ویتکاف فرستاده ویژه رئیس‌جمهور آمریکا، و جرد کوشنر داماد دونالد ترامپ رئیس جمهور آمریکا و فرستادگان این کشور در روند مذاکرات با ایران، گفت‌وگوهای مثبتی با سران منطقه‌ای در دوحه داشته‌اند.
🔴
این منبع افزود که تماس‌های فنی بین آمریکا و ایران در چارچوب تلاش‌ها برای دستیابی به تفاهماتی درباره توقف درگیری‌ها همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131195" target="_blank">📅 09:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2068fce62f.mp4?token=a9Bljp48g4wg7k80OF-sMCBSm0u8WFdbmAV6d-Z24Dp2yRSV_5YDiFo6wszEPvHSnXHvRvJJI4zExPaV7WmHbIFXofhyfj4SJk__meuMBLJRrPqjuMsF2HrHcUb_Njt16ZhOWR5TK_4KMG69KWy59GEwkgJC1_nHIYznrhmrayFJCgqLSeXaE4bhABgi8lZ-QRr3U4KD-h3hQAzX9OEGtAzu76YisoQBJG1PKPKVvKRuOQnX8HZkx6agTfq0WIZMW6lbwMW5jPr1nx9s5mVfzKn3dNJnBuqOINEp6e7DtUNMI9lryC-KPjFaI1j3OoHrjWmlC2RMMRh0NLSQk-Mwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2068fce62f.mp4?token=a9Bljp48g4wg7k80OF-sMCBSm0u8WFdbmAV6d-Z24Dp2yRSV_5YDiFo6wszEPvHSnXHvRvJJI4zExPaV7WmHbIFXofhyfj4SJk__meuMBLJRrPqjuMsF2HrHcUb_Njt16ZhOWR5TK_4KMG69KWy59GEwkgJC1_nHIYznrhmrayFJCgqLSeXaE4bhABgi8lZ-QRr3U4KD-h3hQAzX9OEGtAzu76YisoQBJG1PKPKVvKRuOQnX8HZkx6agTfq0WIZMW6lbwMW5jPr1nx9s5mVfzKn3dNJnBuqOINEp6e7DtUNMI9lryC-KPjFaI1j3OoHrjWmlC2RMMRh0NLSQk-Mwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرمای بی‌سابقه در آلمان؛ خیابان‌های برلین را با آب خنک می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131194" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e2ffb510.mp4?token=JdQQZuOPiSxbvio19BMHjc96mDEfqggKFvZnHZqYhsy0s7M7Xl_I_fW5E1JuJMjspSUyOgHPlFneCWpmax_DZ8C7px2lxupfY_Yg6NVFOLhSz6upqr6PhBTQIHL7JuaxOLLlolnftLVShvYFf4axwh1jItYens7ulXmqBTjeUKzfF4lGdFSXibVS6GKT2nQKdWKg4gGqHRYEl7v_BuplOutEO2kI1f-6-ZqWnWvukJnafT2u_Ls7_8UvJF4y9A44MWIqYHGo0EQ5_iWh2uIzFSNjtv2nBYjZUHwX5qGPz8FZmRZ9k6Wm31ic1CqivFMU2Ra_esMhx-mVbVhmycjgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e2ffb510.mp4?token=JdQQZuOPiSxbvio19BMHjc96mDEfqggKFvZnHZqYhsy0s7M7Xl_I_fW5E1JuJMjspSUyOgHPlFneCWpmax_DZ8C7px2lxupfY_Yg6NVFOLhSz6upqr6PhBTQIHL7JuaxOLLlolnftLVShvYFf4axwh1jItYens7ulXmqBTjeUKzfF4lGdFSXibVS6GKT2nQKdWKg4gGqHRYEl7v_BuplOutEO2kI1f-6-ZqWnWvukJnafT2u_Ls7_8UvJF4y9A44MWIqYHGo0EQ5_iWh2uIzFSNjtv2nBYjZUHwX5qGPz8FZmRZ9k6Wm31ic1CqivFMU2Ra_esMhx-mVbVhmycjgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد.
🔴
بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131193" target="_blank">📅 09:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
الحدث: به گفته مقامات آگاه آمریکایی، دونالد ترامپ در حال بررسی بازگشت به رویارویی نظامی با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131192" target="_blank">📅 09:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
میزان خسارات وارده به زیرساخت های آموزشی در جنگ اخیر حدود ۳.۷ همت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131191" target="_blank">📅 09:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pII8155ElozOgdERPw8d2jXuSP_--RpDTb5PqwC_JdkZ1Ptn6SQIjl09apxsbMoDaRqCgvy7fFtuL7cc8N6rDFfBKRwSnIHKX7LdlnJyouw64FwLpAuryd1cATaoB7W5Z1Mjwafw4zB7IlhnZYuKwFtpM8m7NN8xtCRqHFUbl0IekK9_zAEmFDFu9Z7LrhKOxMqiwZMGSwLPwRiM_bdpz02CzIFJL4B-uB4JfOK-ozsL2vrfJXXEikjjGkzzgO7c70WX67kmpsuDbd5DhytG-h_H_4LIW6X0Ir3WJQ2T4EToHoYZYUBC2R97Tdos6unWGIn7p-cK4uG5REQvNP5-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P_BAZV3elYkEU-kFdWM52uLg9_jChClK87CbdxT__BPHPRY5XNRR6NPPuVmywh_g-MeaL3m-XwUySKbR2KZKr8fMBYXZaP2XYxcCtWRLC4xGy4RE_BFH-99qjRH4LWeBDyZqvGqxJb3facwsfGGnVPGG5hrS2kQYL91BTyHD0oqPLUfShCceglBC6F6-uLuvGVXEkD1FjvhKgvrIzF9ZaRkXJts5ZObbgNB4PJAuOvE3LqMIwL-DfE90AfJ5UEzFhxpc3vKKVzwIGFjxy40AXxbK9GYBJPAQZwrUdkXbmHvZBGLbASU0K5_7_zJ4rD7JK8Gyd6hMXIi_nmBWuSXDGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوایل دیروز، پدافند هوایی S-300/400 روسیه تلاش کرد تا پرتابه‌های ناشناس اوکراینی را بر فراز مسکو در ارتفاع بالا رهگیری کند.
🔴
با توجه به هشدار موشکی صادر شده برای منطقه و ارتفاع بالایی که رهگیری‌ها در آن انجام شده است، این احتمال وجود دارد که اوکراین برای اولین بار از موشک بالستیک آزمایشی FP-9 خود استفاده کرده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131189" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131188">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz1gvltLY18s3VuR_OMNd4zV3lbcsIjMhj0lu1T6zrx2tfyF_-qbKQCiwqoJ-PNLvX9J12scYM3bqDMxI2TfV0gNmPr06iMKvpssDJaOWvUY1AucBC_LbmjWETb8_bYvARdE90h2Jl9XIVFZXjqV32lXrgdqhsVQWpAmpdHif6CmqnZ-AqvvazequjtJu296U44uyLRPx22evVaC-wEENXYlgh2QOTx4we7reh5iF3_Zte7l0WcoI2qZwD7F85JD8b_Y3U95wHf6SVBePzti3tkbbmB2Pt9nRm1Md0aOCcL0TcfVDCxGw4mk3bJlzI4VxAc3IuOp4-k3ZRhEmorU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته WSJ، رئیس جمهور ترامپ اخیراً در مورد احتمال از سرگیری حملات نظامی در مقیاس بزرگ به ایران با پیت هگزت وزیر دفاع و ژنرال دن کین رئیس ستاد مشترک گفتگو کرده است، اما به گفته WSJ فعلاً ادامه مذاکرات دیپلماتیک را انتخاب کرده است.
🔴
ترامپ معتقد است که بازگشت به حملات تمام عیار می تواند مذاکرات را تضعیف کند و شانس دستیابی به توافق برای برچیدن برنامه هسته ای ایران را کاهش دهد.
🔴
او همچنین مایل است اجازه دهد مذاکرات فراتر از ضرب الاجل 18 اوت ادامه یابد و در حال حاضر از حملات تلافی جویانه محدود در صورتی که ایران یادداشت تفاهم فعلی را نقض کند، حمایت می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131188" target="_blank">📅 08:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131187">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eky42jKYDcb_Cjv5paQHlY-7r9mydVk00eEQtCurwwOCteDGkyyabJVVYPAZGKkpsGWYGn-xtqC38mB5RSG9DtqCzi4DnmU0KniyRsl4EeUYy54Nqvi3ZTIxv8gtOjRvmRICPABfmKrYfNH8FtTmq6AM-gOBqdpiUvmbW3fEsRa3wDObE9vMH4Eu8euL2JYSk7kZjnqaLynmHL6trFSygJLqRLqjoN_t-n-BV9Nw29xP-Id8U8vvpCWnbuQ2rsVuq0OnoCe9-r4IGtesGGNJ3ZiGXjuhcM8GgArRwrdVuL7WltVT-QUyQ9o3tSaIgorVxKNiIFOJ3t8HmPfaV9EqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش وال‌استریت ژورنال، عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
🔴
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131187" target="_blank">📅 08:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131186">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ورود ناوهای آبی‌خاکی آمریکا به منطقه مسئولیت سنتکام؛ استقرار گروه آماده تفنگداران دریایی در خاورمیانه!
🔴
در ادامه تقویت آرایش نظامی آمریکا در منطقه، فرماندهی مرکزی ایالات متحده اعلام کرده است ناوهای یواس‌اس باکسر و یواس‌اس پورتلند اکنون در منطقه مسئولیت این فرماندهی فعالیت می‌کنند
🔴
همزمان، یازدهمین واحد اعزامی تفنگداران دریایی آمریکا که بر عرشه ناو باکسر مستقر است، به‌عنوان بخشی از گروه آماده آبی‌خاکی، همراه با ناو یواس‌اس کامستاک در این منطقه عملیاتی حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131186" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آخرین وضعیت کیفیت هوای تهران
🔴
شاخص فعلی:۱۲۷
🔴
وضعیت: ناسالم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/131185" target="_blank">📅 08:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
افغانستان مدعی حمله پهپادی به پایگاه‌های داعش در خاک پاکستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/131184" target="_blank">📅 08:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131183">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfzbHueXu6V4cRwPq5CDJ3yIkZqvjQkwqMunwCeK9hlowFRpzZHvKuW9mWqO474BjSY_ndJxKOihpVaFrccH2tYnFx9C5ZfpnYXYQMerVYq9HXfC0WEQ-ZkjEL9QHl-MEZQwfvTEJlzCN20UdBIlrf2P5jCtIPknMfS5VYtbucA0NntynHdtM1UAlVkgMg9tmSrH5jGeQRLXD0197FYllL9t-iOWjOZ2Qa5LBaxep3decvRkgzMf46agGWp_VMYdpU-ouk8cUF3dJz-uuNP7btjKaUGK1yh0zvOA1qtXWRihaDfIV3dD4oPzwpqLemmozuPfZiJVTa7zqFXo8SWQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/131183" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131182">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjUm60J2_fxMu28g-gG8qu-qwp3GefvcrrZS0AzcC0oFsSOZ6iTJ7tlkDwRXd9YRxa8Mh2Xsm_ETeu08hcDTDDphRethwO2JezDcXmABMztD_FftVmH81Fu7Rd1leIt_A_WuWCxPIUcYtnNLPHa8f_bv1tl2QmIvddTmJK6D5zT0b6ZdHFAOwfDL2UqAFGvoi1E_y8wO1y18nOvmQVHjb4U34EFDhJF_PCZVmPEerwm4-GiNa6nBIdPzXle06B16DOJSvxBdXYl635yeM0-RBGKT002Kiv1KOMZezLwWO48VwTXVUy79AahktAITDea6bb_te5nFvAZscmRVNfboLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده رهبر در سپاه:
آقا مجتبی رو خدا انتخاب کرده و ایشون یه پاداش الهی به مردم بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/131182" target="_blank">📅 07:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131181">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/131181" target="_blank">📅 01:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131180">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکریپتو اسمارت | Crypto Smart</strong></div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131180" target="_blank">📅 01:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsIDt1UwQLr6jgUWXl_TOc6DetnTSmAgr6QTOfcg4AYeuiI7odAe6avZMPwiiy42sxC6dZR16VPRrcAIvMlTD-rUX3-u2PZ4ICbgEd-8t5EbKqREvO3tIBwiLkD5fBwnwOby4U9rviC5kiTDoA2QAPFUktPugiwWH0JzlWfhJ-JVIJdbTkdEBPhvOwCP2G0Ih1AzYgftChKrlkze47ZCBSsIggcDwTacRPKptuHLO--d84cnhTsqRs5P-405s-nyoUE7nwTBxyUhYkcLYKOcggr83oY8f-fI_49lCUfA9Y4DISPsn6zEHCikhnV2GubfTuEb8HA_FRJ9XaJQEOf99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه سرایی پیج تیم ملی از ریدمان قلعه نویی
تنها سرمربی بدون شکست ایران در ادوار جام جهانی، مرد خودتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/131179" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131178">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU8b9571LgJ4YWwEGzgRMEAQg-ra2PPyoBmZ6HcEEwDMtLizHtZCexfQF6GKzkVfRItHjGC-rfShV6z0MAZQtKFSKjioq2RKsEWixEiC4_UUzUEMYMrmAwjDjQts9TQvr9hM9-ijNUlyWN9neotudBJeveNqWxUBLdLYnxRLAKeScf8nmyfCKX6r3gzjAPHr36a0H8vnQ06wLD1Gl1P1rHtgO2jo0Odinv-ZNF39mDW80-ydR2er0MwdVCLfKLR-yOzuzVNBmHPS2rEHATj2XO02BrBS6HYCcETj7Ey_2xTWzEaNzalKmAG5U_hgIMRortofmoVG8H7ytz2v7TogsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ترامپ:
ترامپ از وقوع جنگ جهانی سوم جلوگیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131178" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbAaa9dChA3NoFrZthvuImZgmVLOXwMvvg7i36LlnaMLEmerRe4DzBINGolbsjr9Dyk35QuFnHm8wyrZGA2jyj2gCRZdJtvpdAEIxWXkMiIz_79HSSS-33CoXlgTTNqJvozuotAHsDPXfTZEJ-jyCHFvbsr1E0MRdvfTrNp9iRcEQeLynFXhXbuRcgmNVeiNVXW8865-Cg8ZcUsARUnHTkx4vOUqlinQ2nvE9eD7x00r-EOyjW0-SdQ9d8sPp8HS23jJx_c8rGX54hpVQUXTGleczD2IY1rqqx_DYQLNboxgqjGzQhp64OYe-OVKxN1H9jWihyXQeb3fzAEce4hpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طوفان توئیتری طرفداران قالیباف علیه جریان خوارج، از دقایقی قبل هشتگ
#اخراج_جبلی
در توئیتر ترند شده تا این شخص منفور از ریاست صدا و سیما برکنار شود
🔴
سالهاست صدا و سیما در انحصار یک جریان طالبانی است و تقریبا مخاطب قشر خاکستری را از دست داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131177" target="_blank">📅 00:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jusF50qHVXxB3OVicdMSRGlxWU3Y-Umt12LimTzQyuGzXqRf56kKC4CNr23YuBPDGwC3jayQfI0t_0OCvK_-7tZlQpQNDVMN81CCBU41kYw92qx346ro0Tr_z6IIlCjwOw7kyDAH3WoM0QEPjpxRPlbltFbA5As9V3ESB7U5sjieiSTldo86OZIN3n__fcMXQwYxROCY89eNkgVZAbLjXBEaQXshrdlCrfHGAmdHVV6tSn0vWcCAwO3I4DVPeWyR8sklmctosp_jViumCvJoAVFlH43c5kJvUrzgM_qftl7c15mluVYESVndDVzotrfeP1seCtLGSImgRV1BeV6c6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری:قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131176" target="_blank">📅 00:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131175">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=VlH-c9nMbrwuZEDZ2cTR0QAuXVhqJriPccQbUEq4pzKQtOKKyKNb_czdcFt_AQ01vlcF2Ng0Ri8s65lDNvbFS1ONHXAwbyFk8ptGXu1Wd5KfFUiK612RwDHnxYk678-fuqXz8hWfONbn5jBYOivi3uUFLC8wy3ovsEfOEw-cKGw-Yul37EXAMiIW2BtPBqzfifuSdrMmKBN2WdqeEh5Dna5mQDh1p7X5tEAfvfkTzLx4h7q87o55r_-9lmsuAleCHgt5WO5WydJEQqDVkjmd9xzs9Nv0BNBvHzjexzIwkflT0sqxe6TGJ4OVPnOIxeeFj2ve2lzKtQ6MOFWm7exYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=VlH-c9nMbrwuZEDZ2cTR0QAuXVhqJriPccQbUEq4pzKQtOKKyKNb_czdcFt_AQ01vlcF2Ng0Ri8s65lDNvbFS1ONHXAwbyFk8ptGXu1Wd5KfFUiK612RwDHnxYk678-fuqXz8hWfONbn5jBYOivi3uUFLC8wy3ovsEfOEw-cKGw-Yul37EXAMiIW2BtPBqzfifuSdrMmKBN2WdqeEh5Dna5mQDh1p7X5tEAfvfkTzLx4h7q87o55r_-9lmsuAleCHgt5WO5WydJEQqDVkjmd9xzs9Nv0BNBvHzjexzIwkflT0sqxe6TGJ4OVPnOIxeeFj2ve2lzKtQ6MOFWm7exYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حال بچه‌های کنکوری خوب نیست...
🔴
یعنی مسئولین این صحنه‌ها رو می‌بینن و سکوت می‌کنن؟
🔴
سهمیه برای ۸ نفر المپیادی ردیف شد...
🔴
ولی برای کنکوری‌های ۴۰۵، با این همه فشار و آسیب روحی
🔴
کسی به تعویق امتحانات  توجهی نکرد.
🔴
کاش یه سهمیه اعصاب و روان هم برای کنکوری‌های ۴۰۵ وجود داشت...
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131175" target="_blank">📅 00:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131174">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WQLplNROKsr5yciPJR9iRQz_YqGQkp2kXIUZHEbxwEemETWGYTGbPJQVWkUKrBYm0z3_FM6Ctt-o1Ln1Pwd6EsGaqzPXl8gkt3Lidar_m4jejo-N4NXoamnyvmOOxy2oIKYY-nWuyCuYdcCysSkt7vxrDu12UgXBXkIcDy9wvXvxGFnuK9BZ3EfB-tugdnvXn548FFcwMOghzkbxYTEhH9i1Ha5qBi0jwgDlgt29tNY_kE0P6f1YIPaGf8FtdFFzfFbwOiNZ3mRLZinEugsWcMemVkSLIG5HWHPNXqdy5YuDdkwtg8pgTfIBYCwl8G4Bb8osXD5BP4d67vEBn-63Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: قالیباف امشب خیلی حرف زد، بقیه حرفاش فردا شب پخش میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/131174" target="_blank">📅 00:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196a09733.mp4?token=Qbnu4jWU8KGgZLDapQP-7lWDCRPmcKYaerl9H0UqlCAnO__d2bFCSeKnUtcVfMkTL4Rlf9OTs6UE6bDQS0o3xR6SXxinPw63LSDqBt9cbb9h63v-ZvaimvNoQEjs0cAYIgN6HOy7LaAGrq69IaBNMknfa0kLR4NMpFw9WESNmzX2UV4f5nocxfAOgzTfTntsj8CvhzPaoCEdnwIgwLGwnIva-mjzws1s41rOuAZtvhXU5FGn4RHOO6vdeHCeAPOMh9eDmZsymOi3wsZ4afgm3d6CGra57sImcNNshf3ihm1p1HqjCYYcEPCIAsY7RfPWg7J0Pj1Eogitzl1gkVHVdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196a09733.mp4?token=Qbnu4jWU8KGgZLDapQP-7lWDCRPmcKYaerl9H0UqlCAnO__d2bFCSeKnUtcVfMkTL4Rlf9OTs6UE6bDQS0o3xR6SXxinPw63LSDqBt9cbb9h63v-ZvaimvNoQEjs0cAYIgN6HOy7LaAGrq69IaBNMknfa0kLR4NMpFw9WESNmzX2UV4f5nocxfAOgzTfTntsj8CvhzPaoCEdnwIgwLGwnIva-mjzws1s41rOuAZtvhXU5FGn4RHOO6vdeHCeAPOMh9eDmZsymOi3wsZ4afgm3d6CGra57sImcNNshf3ihm1p1HqjCYYcEPCIAsY7RfPWg7J0Pj1Eogitzl1gkVHVdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش سانسور شده صحبت‌های قالیباف در صداوسیما: قالیباف: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوپک صادرات نفت انجام می‌شود.
🔴
۲۰دقیقه از این مصاحبه توسط صداوسیما سانسور شده است !
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/131173" target="_blank">📅 00:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دولت ونزوئلا : یه کودک ۳ ساله رو از زیر آوار، بعد شیش روز نجات دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131172" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131171">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روزنامه «العربی الجدید»: تلویزیون ایران به‌طور ناگهانی گفت‌وگوی زنده با محمدباقر قالیباف، رئیس مجلس شورای اسلامی، را بدون ارائه هیچ توضیحی قطع و پایان داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131171" target="_blank">📅 23:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ونس: ما باید از طریق بازرسی‌های مداوم، برچیده شدن برنامه هسته‌ای ایران را تأیید کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/131170" target="_blank">📅 23:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131169">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نتانیاهو درباره غزه: «مهاجرت داوطلبانه» از غزه همچنان روی میز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/131169" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو درباره ترکیه: اردوغان درباره تمایلش به نابودی اسرائیل و کنترل دوباره اورشلیم صحبت می‌کند.
🔴
فکر می‌کنم فراموش کرده که ۴۰۰ سال حکومت عثمانی به پایان رسیده است. امروز یک دولت قدرتمند اسرائیل وجود دارد.
🔴
او باید آرام شود. ما اجازه نمی‌دهیم کسی وجود یا امنیت ما را تهدید کند، و فکر می‌کنم نشان داده‌ایم که چه توانایی‌هایی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/131168" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ونس: نتیجه مذاکرات مستقیم لبنان با اسرائیل، احترام به تمامیت ارضی لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131167" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e7b409e3.mp4?token=rrlkAivIeSWFwUNu-ISoEQnM23XR8l2wvEyPPfL_MwPj8rRiXNE_qzL1x_8n3EjhaG-Nv208m27UoWtHqoLpAjwR3WM9ow1nGsrUwUZYl_0wgnM8EbcDDi1JEBjVN-NOzGCkO_4bCuaXlhPuPMtPe4k82Wquo0ErsYYUvYMUv9OMDnPJmo0aoSBomXp7t2xBO4i-v5czCvdBf1OCZMWFiRCycwql6KpX3M3ZQ4LElS7qd1tfbn9OsC1ZU7lUoUQbvGIHYQHACDGu0cKGO4-t4jrOfo6zzfVROMkOawUpnq0gSaCPEzth-dU06yGzpiWQ9gDVQn1b48-5N6GcMkK7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e7b409e3.mp4?token=rrlkAivIeSWFwUNu-ISoEQnM23XR8l2wvEyPPfL_MwPj8rRiXNE_qzL1x_8n3EjhaG-Nv208m27UoWtHqoLpAjwR3WM9ow1nGsrUwUZYl_0wgnM8EbcDDi1JEBjVN-NOzGCkO_4bCuaXlhPuPMtPe4k82Wquo0ErsYYUvYMUv9OMDnPJmo0aoSBomXp7t2xBO4i-v5czCvdBf1OCZMWFiRCycwql6KpX3M3ZQ4LElS7qd1tfbn9OsC1ZU7lUoUQbvGIHYQHACDGu0cKGO4-t4jrOfo6zzfVROMkOawUpnq0gSaCPEzth-dU06yGzpiWQ9gDVQn1b48-5N6GcMkK7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیر رولکس : ما نرفتیم مرحله بعدی ولی کلی دست آورد بدست آوردیم اینم عزتی بود که خدا به ما داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131166" target="_blank">📅 23:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131158">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qva9SBKjtoNyhMtRJPfIxbnrzuHtj2cRCbhOSkdaiERol8n7aKEju4pltsl8w4y8W8PPWVc88nBHTdNEH0N49LoqvdkmhGhhPTY56e1mcBZwxMYtvOxbk2KjfwXc9Yg81SCngVH8ZY7rKPj8HYJLz94arXdbap_j6j6dPMEvOpbOy585KKZE1CkLYQRm0WGT6ZbbMh0PnrH9Pky34GKw1yKluUNijYKp1OvIDCXAv1uvzKB33COiGKYhd64iUbOU63y5tmp218wAaFa883tPuxbsjDfeUWvvXzwKjYoCQyRjzFgGd8lOyjgIn8on_qkR7SzpFFkjkLFizgGFLbL3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-oTUN4d9TMsL60OYvT6nBNLy7FNzElyr8ONhvucwyWkQjwV2gsVOlT2u5uGgcjry88XLjZpwUGBBFq5n-IfxezuoiK3tNGmJw6MMo5HeJwF1Gt1tpIQ6bowI0yjrzRbb48hjzY177EbFLWd6Ga0RnJlsxZ1cAZ02fUQxnq65HHoA2mBG_QUMoLWLGF8_HfPs_bknH3Fo_II30wHXHpEvhliMUjvYPxk8EiadiHSHRmknIHE-jqt9zu-AS78nWtt4BIa8r7318oHeLY7xV0GKNMbY54nZ1O6t7jKjEJ0d8Noz3dU9MLmfpNMlYNYwpaXa4o-1ZgN9xxLzASzP1TR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9HZkl2QUpTQ4eZXTNoOUg7NqCVPk7n0GGhhpIeAu9Y94d0J5HfQoumdivRMqOrmeT3iVAajMW5JvqJrRi42LNB5Nt3OJWpWKfJakzdVW3BDdl-_neAmy1m_kvUGtJftyiQ2VUbI97-IfMvJsWwpp--nY02BXjJxQ7NNdsff9mZNJeogH6cPU4wuYTA8he7lukNznXut-8yiMQI8oC7qoyCe0g4EF-7_Gaigb22TiAc8OlncS3kwCyWR91sSwaEwsfc6mSAqyOWoOXF5isOGwNlm_015-ujKsBAKCajTjqUuW8av8tfT9wvX9zhE_Rpho0e32Ons9C8oAjikGnyzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igIemfJUNS-xzvZSdTHo_cIvHJiAfcNnEXl4a0_O7DT0H8R1oCg1UcqapGHqxeVX-eIubPvNrazBuEgtjrzG4qWancDyZ7-bPZlZQSre-D9TyoTOM5yR8X0sLnkupOL1QPWLOkZgfCwXNjtYORldOLjpg8t2qqyskAqNiWGVJwC1zPd9YAOCV42hpEtrt55WHxpwOiga9fsgbtlUEcAjp7iehSDWNV2RJ0xE-t77vaLWPdZEnSMNBNr9XNab49De5rfXqZm7VEXl70jPYLF17LIzGsowYIuEAHCBR_tVmapbixgzubp0gQXluqVnfYMfUgk3zAssiZqBiFQvV7Rlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiJ_c9Bk3dNKb1VGQGFV_KNojCaHrjAt3qEPlqku_fGQK9yH0AJtuGzwqOWfVLaYzu49K66ajm7K-foK9JKqOAZdB-iicUx3uW6tjURCEO0NSzWhxApCbcnZm2zvdl9BbWtKmxuTofmiC5oPrjGrH85yOYfCxDXyEm-qhXz9Osa3a5bacZsZaTIriPdgI3U2X7V8kSb3phVG-0EkeMmuS-cbB0Y5NEuaBaaKZCbXQBi0glHvf_6fVj4-kivHYkSQ9SmJU1KgmGDPkldGM6VUmoVrJ6qJaUBj_5rI466iSDXXZHsDyu8izL628Gxlu9nmyeooAV46Jon6ntfMD-v-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/paXU-JmkcZLtA5yDfY9l4z0pO0G3_ZcogZ8d4fY2NZSrBDQBdLb11-8rlaEAC5cwvQ5szy-53nxg_-EtdU5Ao7gZDBkcEKVeVMsZadiK3NmN7IPNGzSoSryvFU_6CSGzub1_1GlGT4Sstoh-cNf0OLQgviuUmDOz0bqm5oafZLQRjD2O_2QrCOVgRrC1KaTTAp36alngC9JlVG3SjHCwQI0ip5hTN0T1aCr3X8RkhfmcEI7q78DYMMK2hmBMYvPWuGS9KiZf0SQyh-BnQzm1hyc2dLTG1iKJ7JdiiVKPS8jOXdzctlyWjRLFWftxm4yQByiOCGzVjIS1SrV95fvL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyLLN6v_pSsO0A47aTA3F2khQ4gpvt0drFW0l1jXNhP75YlOwRsvXjtmNCJGRgrF6wt5gwzNYLzEsVFw1BYQpE3R1tj3gKy0YDRg0BEI_1F-xNhcJBMHOVjma_vpFaJnfEizcvS5jzS67rrfs5N-rR2IfJBCRujdJ9Hn65UGQww8fM4SufBw--Bc_mtdhKxR9PuVaQg7rSoeE_wKzunonmFa6Bnolkk3nr6Bb0asyXUhXA7WuzmY3_K6jGKDD1W5qs-2MLDz2nucac-sCykqLXvrA9PoQ_urOqZxt4_-BLhhhqAUYAkUCb2HBib4iHh7o_KSDc6Lg1U-BySqHuMz-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2621eaae.mp4?token=TWwckjybyj3viSXXBW8tQeFyhsmuRnCkuMq2-p3OmDX8GU1IlFYPKPXDcJ7eNScBTFtKHk71q85cSWh7TcQADtZKr-z2kY1VkAOl6yPcoeXpeaYWw_qjlRyK3npURpnZY_5urqP9YTO-ItTeON3DAElkXNvCtGo61Vu6JDaLp1akh7aZJBG6HDrNe6mt0Vm4ksyNZPm3vU-zKOQzl3fS3U3BhfoaziW7DgXt3YnuS0_fZYUE9gxTQbzypMlNJ8x-WPC78ConCzYeT3tUPnMG35AHRYrNcXyvF8MFuFiQmWIyyPMKIbJa_ooYKcCnepIOHFxu73B57bW_p95J-y6hE5EgAK3Z1tFNDLL2ynxclRAhY_8nGSPxoX1AIKVflQKoFxlagU6oJuGJPsQyceTPWNogk-hNLjHFr3UZ24YNSiqr1YV_rHpNzlw7vekGihtrdOc2_dGYtVd-rw6FCKvCvrs5qypR1N0ffe-whMMktusfN4-hazNNnkECSNepybVTUpErbx_mrvNw6E0x7UdF-Lz6u-m5bSgDDfJSmRK8Gw2KnF4AlbXgxhjdsK-f_jDtw3Oo_oXn_VmklboLjuVco1_qdjJd1e1v2UPJOur7bdHNPxDxlbKQQXVJ7XKIBJZ9K3TCks_IwmNhA08kZWR8HU1Znw1yWGmuS8bUBRV2kcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2621eaae.mp4?token=TWwckjybyj3viSXXBW8tQeFyhsmuRnCkuMq2-p3OmDX8GU1IlFYPKPXDcJ7eNScBTFtKHk71q85cSWh7TcQADtZKr-z2kY1VkAOl6yPcoeXpeaYWw_qjlRyK3npURpnZY_5urqP9YTO-ItTeON3DAElkXNvCtGo61Vu6JDaLp1akh7aZJBG6HDrNe6mt0Vm4ksyNZPm3vU-zKOQzl3fS3U3BhfoaziW7DgXt3YnuS0_fZYUE9gxTQbzypMlNJ8x-WPC78ConCzYeT3tUPnMG35AHRYrNcXyvF8MFuFiQmWIyyPMKIbJa_ooYKcCnepIOHFxu73B57bW_p95J-y6hE5EgAK3Z1tFNDLL2ynxclRAhY_8nGSPxoX1AIKVflQKoFxlagU6oJuGJPsQyceTPWNogk-hNLjHFr3UZ24YNSiqr1YV_rHpNzlw7vekGihtrdOc2_dGYtVd-rw6FCKvCvrs5qypR1N0ffe-whMMktusfN4-hazNNnkECSNepybVTUpErbx_mrvNw6E0x7UdF-Lz6u-m5bSgDDfJSmRK8Gw2KnF4AlbXgxhjdsK-f_jDtw3Oo_oXn_VmklboLjuVco1_qdjJd1e1v2UPJOur7bdHNPxDxlbKQQXVJ7XKIBJZ9K3TCks_IwmNhA08kZWR8HU1Znw1yWGmuS8bUBRV2kcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل اعلام کرد که سامانه دفاع هوایی گنبد آهنین پس از یک سری آزمایش‌های گسترده که با همکاری سامانه‌های دفاعی پیشرفته رافائل انجام شده و شامل درس‌های عملیاتی از جنگ و عملیات اخیر علیه ایران است، ارتقا یافته است
🔴
این سامانه ارتقا یافته در برابر تهدیدات پیشرفته از جمله راکت‌ها، موشک‌های کروز و پهپادها آزمایش شد، این آزمایش‌ها همچنین شامل سناریوهای عملیاتی مشترک با سامانه رهگیری لیزری پرتو آهنین بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131158" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131157">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پولای بلوکه شده مال دولت سیزدهم(رئیسی) بوده است، مصاحبه اش در صداوسیما قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/131157" target="_blank">📅 23:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131156">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گفتگوی قالیباف نصف و نیمه در شبکه خبر قطع شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/131156" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131155">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=LCqkpXuGPQUYK3ctKpbwvFx7zNMCgsiOM6SjqgZMG0Mp8rJlBi6gLzBb2_emF4Bg9I5zWMEmDffH1EqasJnJ2Lcxl0oU6YCyanhjESoUWowwWeMxlOHyVF9dgbBH659Fbq8SGNya-0FlyT3kcl8IGChXzVq47LW5b2wX-KqZ1FIR7W9IbyNBhoOUUzHK6cjjntLsKsOblQenkPhmq5kY1dE4kkfK1hxp_gltP_tMaZA8DAczKHmFAA0a2B1n8yIjh3jKw18-YU3sZRgnUORrk2jpCu7rgkCFN2hlkzL18bTjdqjEwQD9CflaEaS0MnqbLMMZWUEKlbbtKPGVUw2A2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=LCqkpXuGPQUYK3ctKpbwvFx7zNMCgsiOM6SjqgZMG0Mp8rJlBi6gLzBb2_emF4Bg9I5zWMEmDffH1EqasJnJ2Lcxl0oU6YCyanhjESoUWowwWeMxlOHyVF9dgbBH659Fbq8SGNya-0FlyT3kcl8IGChXzVq47LW5b2wX-KqZ1FIR7W9IbyNBhoOUUzHK6cjjntLsKsOblQenkPhmq5kY1dE4kkfK1hxp_gltP_tMaZA8DAczKHmFAA0a2B1n8yIjh3jKw18-YU3sZRgnUORrk2jpCu7rgkCFN2hlkzL18bTjdqjEwQD9CflaEaS0MnqbLMMZWUEKlbbtKPGVUw2A2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: رئیس‌جمهور آمریکا گفته پول‌های بلوکه‌شده صرفاً برای خرید غلات آمریکایی آزاد می‌شود. این چقدر صحت دارد؟
🔴
قالیباف: واقعاً هیچ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131155" target="_blank">📅 23:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131154">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b26e4e44f.mp4?token=CGyrY4h5SgyXOnZJXh3J_qYH4flPLKDwo5m6DZ600P6XfPYt5k31aHyeYuPJZh_JQMIeUklKU-SNJ7jQ47XmTRd50ouqvwqeLRpMW387H3tepx_YDI_eUN47SuDbCmohdYtgtszsQj8s5Lwyfr4BuRRLjpqpwhwz3-_jy6U2ay8ETMTXxHF02Y2ojhaPKxky3ztOMq4-bPAe_btNGvmza9sffYOp1dlKfdE4TcGHquq3YcSKuUj1QXTN0oqPzFxznFi1MRU247mrk_89XBm7legSHXNpfzhoKODV2Ve__6yB-kuJ-z5Y1KIYrrCUu3TI29AgLPRrufPkYFBAPdRZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b26e4e44f.mp4?token=CGyrY4h5SgyXOnZJXh3J_qYH4flPLKDwo5m6DZ600P6XfPYt5k31aHyeYuPJZh_JQMIeUklKU-SNJ7jQ47XmTRd50ouqvwqeLRpMW387H3tepx_YDI_eUN47SuDbCmohdYtgtszsQj8s5Lwyfr4BuRRLjpqpwhwz3-_jy6U2ay8ETMTXxHF02Y2ojhaPKxky3ztOMq4-bPAe_btNGvmza9sffYOp1dlKfdE4TcGHquq3YcSKuUj1QXTN0oqPzFxznFi1MRU247mrk_89XBm7legSHXNpfzhoKODV2Ve__6yB-kuJ-z5Y1KIYrrCUu3TI29AgLPRrufPkYFBAPdRZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/131154" target="_blank">📅 23:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131153">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گفتگوی قالیباف نصف و نیمه در شبکه خبر قطع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/131153" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131152">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f975bb897.mp4?token=sJVsXMNU-EeA-t24oCSEJagF51aGL2Bm-KByqBXRM6xa8b-QVcNq-V3SXUQ654HenyV3rJPPFsLI98i6hpP3Yfg-NmVZZoSH2wzLS1FUSTf4wEjfLLKG1U-NfEVOws4RhY8_ZH0AqkyGRCoryIA0wfTUtm2i2MGeVoCANggralgoAeiRdb7VL-0aKwN_HIkIzGYioxdZXFXo6oFs_PUU1yQk59JpmYENOrsyv5VXUKccboh32-_V5Ohaw1kTIjnyBvrXNS6mCjklKwZVtJ6A1JNgu4lFnuE_ilTFpXMN8TvC-FFqKrBtuVwKHefHp0fHEnTe5eUdKMzKS9OC4jbJeDM2Jx13sFD-uImXcU7I_1Vai0BQs26bHQyN_cvK7tokY6BufafukPWR814WDMeMX1fCeDnIpDB8Lk6hYAVucXBWhUkrXJ3EQ1EMsdbAndFxPazSYWFA_eGQOD2ey_L_RZcko_us_HsMYi3fZg7RuT0tb2mT3YnnxiuVia0XzvuuI9Z_-wgo_KKlHlpZDgta_oZpQ6PPNB1iops9rz6o8CBrfDPbv1XcxV1xi7e6EcPOt0T37l5iJilCi_9LPIXCU6LTjsqod961C0HG_fcbNf6D43dXSKNpval4BlZzmrJEY1A2EchXx1idAXsWINQxR-3A8wYz0oki8zehTUa-PqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f975bb897.mp4?token=sJVsXMNU-EeA-t24oCSEJagF51aGL2Bm-KByqBXRM6xa8b-QVcNq-V3SXUQ654HenyV3rJPPFsLI98i6hpP3Yfg-NmVZZoSH2wzLS1FUSTf4wEjfLLKG1U-NfEVOws4RhY8_ZH0AqkyGRCoryIA0wfTUtm2i2MGeVoCANggralgoAeiRdb7VL-0aKwN_HIkIzGYioxdZXFXo6oFs_PUU1yQk59JpmYENOrsyv5VXUKccboh32-_V5Ohaw1kTIjnyBvrXNS6mCjklKwZVtJ6A1JNgu4lFnuE_ilTFpXMN8TvC-FFqKrBtuVwKHefHp0fHEnTe5eUdKMzKS9OC4jbJeDM2Jx13sFD-uImXcU7I_1Vai0BQs26bHQyN_cvK7tokY6BufafukPWR814WDMeMX1fCeDnIpDB8Lk6hYAVucXBWhUkrXJ3EQ1EMsdbAndFxPazSYWFA_eGQOD2ey_L_RZcko_us_HsMYi3fZg7RuT0tb2mT3YnnxiuVia0XzvuuI9Z_-wgo_KKlHlpZDgta_oZpQ6PPNB1iops9rz6o8CBrfDPbv1XcxV1xi7e6EcPOt0T37l5iJilCi_9LPIXCU6LTjsqod961C0HG_fcbNf6D43dXSKNpval4BlZzmrJEY1A2EchXx1idAXsWINQxR-3A8wYz0oki8zehTUa-PqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس درباره مذاکره کنندگان جمهوری اسلامی ایران: یکی از چیزهایی که درباره ایرانیان هم شگفت‌انگیز و هم کلافه‌کننده می‌یابم این است که می‌گویند «نه، نه، مذاکرات صلح در جریان نیست»، در حالی که مذاکرات فنی بین ایالات متحده و ایران درباره توافق صلح در جریان است. این یک تاکتیک مذاکره‌ای ایرانی و یک ابزار بلاغی ایرانی است که من آن را درک نمی‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/131152" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131151">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd90a566a.mp4?token=n6I81FMhio2KI_8-znYdO80IV4dY_2-kOgOXqJdWeLYoCFkFfbXKQeQVVPXSGE47ux-8PtpNRfP7tUZzgT_8gANZONc3Ap5dHsxIRfU-2Q36ScGY_Ogn-nuWQhKvzGZye9cEj_8tdW9_t5RmDTmL8R4l2ekoXC3LQoEveXIjIMpL9CcgYO44eWDA-lu6pJxHKo5Ub5wZHB44Gu3HctPt8TdwY62eRw_u8PD5G1xB_yCepwJ0X4naeWJRFeMDnDP6f4oGNlLvtvzqFneI7JHaSB6CGWnRmj601lc66JSQ5Cx5EPxr97lFE2sxuRryosoZKWYvOPShmG3yRQjSflzUqjk71NP4RJyCZpXA63-P5Q-sIAb2llTwsitS-FQOmVNK9T9enFVHGrWscbZYnv5hfMkN5nax8OKhky42hksXMc6rJnxoPYQ-7m_hVw-8Q0Zb9f2MnR2qbtFaxeuMppYL4xKyiPaTV2AE4gKXzXkw_7dew8qGGYNY97ntnU56Gtn5rO6GJ3GtUf5-eEqZjMGtGmtEIIYJQQhyceZ1cI2ubSEzJniiQSyv8S0xtOTsu-Xhuy3HISrp-pcRGRw43_YPt-zIt0eaBeuOgv4mMYacA3omjr8K1ah-csumqr1vLmkMSl3o-oSwGJRNytWGExBMcD5Ej_-_rK_PlUIcQ4IHpiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd90a566a.mp4?token=n6I81FMhio2KI_8-znYdO80IV4dY_2-kOgOXqJdWeLYoCFkFfbXKQeQVVPXSGE47ux-8PtpNRfP7tUZzgT_8gANZONc3Ap5dHsxIRfU-2Q36ScGY_Ogn-nuWQhKvzGZye9cEj_8tdW9_t5RmDTmL8R4l2ekoXC3LQoEveXIjIMpL9CcgYO44eWDA-lu6pJxHKo5Ub5wZHB44Gu3HctPt8TdwY62eRw_u8PD5G1xB_yCepwJ0X4naeWJRFeMDnDP6f4oGNlLvtvzqFneI7JHaSB6CGWnRmj601lc66JSQ5Cx5EPxr97lFE2sxuRryosoZKWYvOPShmG3yRQjSflzUqjk71NP4RJyCZpXA63-P5Q-sIAb2llTwsitS-FQOmVNK9T9enFVHGrWscbZYnv5hfMkN5nax8OKhky42hksXMc6rJnxoPYQ-7m_hVw-8Q0Zb9f2MnR2qbtFaxeuMppYL4xKyiPaTV2AE4gKXzXkw_7dew8qGGYNY97ntnU56Gtn5rO6GJ3GtUf5-eEqZjMGtGmtEIIYJQQhyceZ1cI2ubSEzJniiQSyv8S0xtOTsu-Xhuy3HISrp-pcRGRw43_YPt-zIt0eaBeuOgv4mMYacA3omjr8K1ah-csumqr1vLmkMSl3o-oSwGJRNytWGExBMcD5Ej_-_rK_PlUIcQ4IHpiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس در مورد جمهوری اسلامی ایران: ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131151" target="_blank">📅 23:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d179f44d.mp4?token=H26yje_8mz31n0Pm0emV1CaCW9X5SqxDYp1bvYmBNYFTujiYIf9PmBtRZ4Yg1iGboMQCOYr8U8OxAmsDJUCWrlXX_Rk6peRLXw5-sCK9_SFkbxfIhe2Lv986gP6IDFV9rV3lp4rNq9mZBcxrJ6eKZcizRkpxCiFE3slfBv65k1sRdZ8EgUEqroRa7L490UUMLGI94qJQfYyTNctRfs-IzPf6T3vPq9gPIsQs9C9HEVrq8QRVKxXBkkhN8nXyqxDcPOfWyn7CCugvx3bJs9fm4ZQiRfeuj1Ov8Q55ipejbh9z076mOfwJs5aGH5eQ2P7FUq3eI0YGvqbihodlauzqcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d179f44d.mp4?token=H26yje_8mz31n0Pm0emV1CaCW9X5SqxDYp1bvYmBNYFTujiYIf9PmBtRZ4Yg1iGboMQCOYr8U8OxAmsDJUCWrlXX_Rk6peRLXw5-sCK9_SFkbxfIhe2Lv986gP6IDFV9rV3lp4rNq9mZBcxrJ6eKZcizRkpxCiFE3slfBv65k1sRdZ8EgUEqroRa7L490UUMLGI94qJQfYyTNctRfs-IzPf6T3vPq9gPIsQs9C9HEVrq8QRVKxXBkkhN8nXyqxDcPOfWyn7CCugvx3bJs9fm4ZQiRfeuj1Ov8Q55ipejbh9z076mOfwJs5aGH5eQ2P7FUq3eI0YGvqbihodlauzqcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات جنجالی منان رئیسی، نماینده مجلس در صداوسیما درباره بندهای تفاهم‌نامه
🔴
برخی از بند های تفاهم‌نامه آنقدر ضعیف امضا شده که اصلا نیاز به نقض نداره و خودبه‌خود ایده‌آل آمریکا است/ در سند امضا شده که آمریکا باید مشخص کند پول های آزاد شده را کجا باید خرج کنیم/ آمریکا غلط کرده به ایران بگه پولشو کجا خرج کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131149" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قالیباف: تنگه هرمز بزرگترين ابزار قدرت ماست، باید از این نعمت الهی به درستی پاسداری کنیم.
🔴
باید روز به روز رونق تنگه هرمز را بیشتر کنیم
، محدودیت را باید برای آمریکا و اسرائیل بگذاریم اما تردد باید بیشتر شود.
🔴
باید به دنیا نشان دهیم امنیت اینجا روز به روز بیشتر می‌شود و حتی هزینه بیمه کشتی‌ها کاهش یابد.
🔴
برخی می‌گفتند رفع تحریم وعده سرخرمن است، رفع تحریم‌ها انجام شده و نفت ایران ۲۰ درصد گران‌تر فروخته می‌شود و پول آن به حساب واریز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/131148" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/131147" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131146" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قالیباف: به خاطر مشکلات سیاسی با من قالیباف حقوق ملت را از بین نبرید
🔴
کسانی که حرف ترامپ فاسق را قبول می‌کنند یک‌بار حرف برادر دینی خود را هم بشنوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/131145" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قالیباف: حاکمیت تنگه هرمز با ایران و عمان است و تردد در تنگه با ترتیباتی است که ایران مشخص می‌کند البته ما با کشورهای ساحلی خلیج فارس تبادل نظر می‌کنیم.
🔴
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید و این آب‌های سرزمینی ما است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131144" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قالیباف: در متن تفاهم آمده است که عبور از تنگه بدون هزینه فقط برای ۶۰ روز است، این موضوع به دلیل اصرار کشورهای منطقه و کشورهای ساحلی خلیج فارس بود و عمدتا برای کشتی‌هایی است که با آغاز جنگ به دلیل بسته شدن تنگه در آن منطقه بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131143" target="_blank">📅 22:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قالیباف : اگر از اجرای آنچه مورد بحث قرار گرفته است خودداری کنند، ما نیز برای جنگ آماده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131142" target="_blank">📅 22:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131141">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قالیباف: غنی سازی حق ماست، خط قرمز ما در این حوزه مشخصه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/131141" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131140">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قالیباف: بعضا می‌خواهند مدیریت و ترتیبات ایرانی در تنگه هرمز را رعایت نکنند و طبیعتا ایران عکس‌العمل نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131140" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
