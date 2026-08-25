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
<img src="https://cdn4.telesco.pe/file/CNoGlY32KlQEyH1R07cQGT2ieZH3v4eL2WPNNiE6emna2bPfHvWmFDCqdj7TS7vQmdQdkrqpD516ONQOAePBl4yr3HbYVQRapflXXpMJzM85O1ZfujGbQk2wYrW4Ll-oNpcVJukhSOYYaDT7wa_MhJcwbNRcAJQmiMaVqU0MEvQTGG260z01EnKAiW9FwiZUHiEyPMI7SWHsdErtKZlVOrS7D3grZimzG6I4aXmhOjXVizTmLeesVddA_T1NBRyl5PTNp7NVAb4AGXaockfQipl8qj9mvVBu7e5iKp3DG_WLoQWNzDMl0R9c3dndIShrEpzPthlVK5myFpZji6YV4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 02:47:20</div>
<hr>

<div class="tg-post" id="msg-684383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای خبرگزاری ریانووستی:‌ واشنگتن و تهران بر سر آتش‌بس توافق کرده‌اند؛ منابعی در ایران و پاکستان این موضوع را اعلام کردند
🔹
این آتش‌بس شامل آزادی کشتیرانی در تنگه هرمز خواهد بود، انتظار می‌رود اعلام رسمی آتش‌بس طی روزهای آینده انجام شود.
🔹
پس از آن نیز مذاکرات و یک دور نشست‌های فنی برگزار خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/akhbarefori/684383" target="_blank">📅 02:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684382">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1roYXvlfG0JlAhbt0pgS3sPxUjPamzfSlmHg32OdofoQeMgU7nlrm6pUNhq-fByBzW9lW8_qtS4KIRhfxwtEJgBffU--Xc1ZbHOmHKLsvaoZg3NpmxdLH1-uTN3iueibJaulaP9hGRHj6_GTnSHCyPsLVyL45x344VNjXtEeq_XM4h0y_ZChIVQEe5Q7DfHjz98YLFELs-tuZOl6Ak4-iMSm0ys4_0kXlfoNeJdvW744rHRqTxf_enyI2a-LNkdJ0l_69WsClzUVF1QwZ-1ygEzeZ6_Y0R9PiHhsEtwFhcGHvEpKgaMgWuMsTP5OGgy3ZeHIUCn2m0Z1-coy30lKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
گوشی نوکیا 105 | دکمه‌ای، ساده و بادوام
اگر دنبال یه گوشی دوم، سبک و جمع‌وجور هستی، نوکیا 105 انتخاب خوبیه
👌
🔹
دو سیم‌کارت
🔹
منوی فارسی
🔹
باتری ۸۰۰ میلی‌آمپری قابل تعویض
🔹
چراغ‌قوه و رادیو FM
🔹
صفحه‌نمایش رنگی ۱.۷۷ اینچی
🔹
ریجستر شده و آماده استفاده
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔴
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
🚚
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63518/180124/</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/684382" target="_blank">📅 01:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684381">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b8388dc3.mp4?token=RcWyBFsEEechDNFBpn5cEDwz4bDL6b3En92WLf8B_stOrSPqkCvKO8Ep3isvC8zuvQwZHPbLCxaxtN_7R8w58sUgUHaAe3tn0iCJ_bgqaxECARTWVIkOdGRdFaLlFG6KPC6XT97AM79JkdkUOYJozeE_jzfr4MHfQ6we9EpNNiqcFYaUEowk-SpuvXmt7fQNsTRdbwRA40cmS6kNV2Ijeb7b3ntlouSCr8vJNTQPlI4acJ92326zLwiedS9HjAbYJ4zpPhkzZ8Ri00Asi4Zg6PLRHidAEpMNf6r3O4IdIaNGAI2u1LAKdZFbP1jw3T0KcqO5-CZmcLUXGBk2y2SVsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b8388dc3.mp4?token=RcWyBFsEEechDNFBpn5cEDwz4bDL6b3En92WLf8B_stOrSPqkCvKO8Ep3isvC8zuvQwZHPbLCxaxtN_7R8w58sUgUHaAe3tn0iCJ_bgqaxECARTWVIkOdGRdFaLlFG6KPC6XT97AM79JkdkUOYJozeE_jzfr4MHfQ6we9EpNNiqcFYaUEowk-SpuvXmt7fQNsTRdbwRA40cmS6kNV2Ijeb7b3ntlouSCr8vJNTQPlI4acJ92326zLwiedS9HjAbYJ4zpPhkzZ8Ri00Asi4Zg6PLRHidAEpMNf6r3O4IdIaNGAI2u1LAKdZFbP1jw3T0KcqO5-CZmcLUXGBk2y2SVsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقاتی که بعد از خوردن تخم مرغ در بدن شما می‌افتد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/akhbarefori/684381" target="_blank">📅 01:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684380">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_Il33ICllM99-qJg7K0i-BiK_qEkV_XVkYZL0FGMoAMf457z7oN1reoTtakdUkfPta3Jb_xTKASegUXWkhJZ1gFVtJsFsK8HSidHWY6g62a6IwiorQiDKvLmVlSOaME3A4luyDSCDIPvTYNyJP98nBuSFKf8At8nUYtT2_IDYmxzuCU6Fenh9xihWokH_m_YgUYb8g3tOF07i5-SkJ7LXnBVpEu9qZIPUFBfwcWv4asUrnnDpQm6F4Vu0jxv7otLGt9hjOiGicSpQkrCX_7Jt1IlRVFphSFX1pNK5rJKHFOeg5G_xzMVqJq00u9iB4WF23BDHmjf9ZzFxBxmoJoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه هم حمله به نفتکش‌ها را کلید زد
🔹
روسیه اعلام کرد که سه کشتی باری حامل تدارکات برای ارتش اوکراین و یک نفتکش را در بندر پیودنی در دریای سیاه هدف را قرار داده‌ است.
🔹
همچنین روسیه به یک کشتی باری دیگر در بندر مجاور اودسا، و همچنین زیرساخت‌های بندری در پیودنی و اودسا و تأسیسات ذخیره‌سازی سوخت در بندر چورنومورسک نیز حمله کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/684380" target="_blank">📅 01:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684379">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5458e415.mp4?token=qgv1JAS5bm7e-QDxvJSNzsyvgOBnot80A4q3rZxWySwwmwmDzcq4LCSktz16cNdZDt1X6vC3Fl68POSwq8jeRk_njVuPZWMW4viBTZWbO4HzKy5k6jQjf3t9YXLW5Ffr6b4HhUzlhXJWDyhzky5kJz8Hn4TwvGRkT8iRteOdsL2aHBGnk8dRoq8yjnw2U3CZbkFVn-15nhusWSGnwmMsspMS0I7bfebN1SRLrgKtnp8dJpsI72-FBeY0c7TNrWYyqO88rdxJnbyCBtOtWn-hcV66QEqcBHbaIdlDrGv8rnXRL782-GeTzhtYMJoBXX-xfLCC_2mU78Tr7b8KS1iS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5458e415.mp4?token=qgv1JAS5bm7e-QDxvJSNzsyvgOBnot80A4q3rZxWySwwmwmDzcq4LCSktz16cNdZDt1X6vC3Fl68POSwq8jeRk_njVuPZWMW4viBTZWbO4HzKy5k6jQjf3t9YXLW5Ffr6b4HhUzlhXJWDyhzky5kJz8Hn4TwvGRkT8iRteOdsL2aHBGnk8dRoq8yjnw2U3CZbkFVn-15nhusWSGnwmMsspMS0I7bfebN1SRLrgKtnp8dJpsI72-FBeY0c7TNrWYyqO88rdxJnbyCBtOtWn-hcV66QEqcBHbaIdlDrGv8rnXRL782-GeTzhtYMJoBXX-xfLCC_2mU78Tr7b8KS1iS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار درباره گوش‌پاک‌کن‌های پنبه‌ای؛ عادتی روزمره که ممکن است به گوش آسیب برساند
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/684379" target="_blank">📅 01:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684378">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای
آکسیوس به نقل از یک مقام آمریکایی: روبیو به تعدادی از همتایان خود اعلام کرد که واشنگتن در حال حاضر هیچ اقدامی برای انجام حملات جدید علیه ایران آغاز نخواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/684378" target="_blank">📅 01:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684377">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEUA_T6NtXcBzWnMDhawqkHTACi19vmCTqk_JG3fUcGbtOGPgRTXFSDVKj5Y9T7DJhNWquPhF--Fe2lTCYpQOGx4Cajd2vrLy78IoDhwu1X9u595S4xUacOpYwsPBfSqBLMj1vjpB_sfH1llYI4KnvIHW2-Bg9vpr0MRT0BkK3ImbJJ9WRmri933CZKpI6FLrLqZlLFkK9GTT-H7m-m5bskY-wU4CJwNpITEJ7kW55oHxbzwX7Msqidt7vp_-TzFBUzCOL61S9XN1SX8E2Elkd1dvaY8XYilZAjfEGRT4yVPHnr3mc0fedGwTLfYlbrxb3XO9tQwJBddxGv8uWxaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تد لیو، نماینده مجلس نمایندگان آمریکا: قیمت بنزین بالا رفته، قیمت مواد غذایی بالا رفته، هزینه خدمات آب و برق بالا رفته؛ ترامپ روی چه چیزی تمرکز کرده؟ تغییر نام دریاچه انتاریو به دریاچه آمریکا
🔹
ماه نوامبر (انتخابات میان‌دوره‌ای) در راه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/684377" target="_blank">📅 01:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684376">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
مشاور پوتین: ژاپن تنها به یک سال زمان نیاز دارد تا به سلاح هسته‌ای دست پیدا کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/684376" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684375">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ee59bcce1.mp4?token=goePqtcaZVpdoYwM9hBT59m0_CEqHAjJgjhTFTgW79GNbMrcY7OK-fLd1LmcqbtJGh3o0Pz3CrHI4z6hgu8jnF1I3JWArRq4efiNn5haDLB3U5gSQs0gtT29MuXp1970dEV8dZY5ADWC20LRp9Hw770_ACxvmPWU8uxK8Sz4tGYlvUCy0OtS985J6XQiFw2b0C31XBc3ZAHQsRt9ryr0Yuhc2brpgBnyECnvtv_BR6I6qiXzPrCgE7mds3GYzIAjDNcgAucFNYq3YaMtC15vcfjUYnRCLX0Bo3MAuiwkYtBmCPSaBqgP6I1_jsDgPX5PMrs5TUNbg_ap2DsMu5r5ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ee59bcce1.mp4?token=goePqtcaZVpdoYwM9hBT59m0_CEqHAjJgjhTFTgW79GNbMrcY7OK-fLd1LmcqbtJGh3o0Pz3CrHI4z6hgu8jnF1I3JWArRq4efiNn5haDLB3U5gSQs0gtT29MuXp1970dEV8dZY5ADWC20LRp9Hw770_ACxvmPWU8uxK8Sz4tGYlvUCy0OtS985J6XQiFw2b0C31XBc3ZAHQsRt9ryr0Yuhc2brpgBnyECnvtv_BR6I6qiXzPrCgE7mds3GYzIAjDNcgAucFNYq3YaMtC15vcfjUYnRCLX0Bo3MAuiwkYtBmCPSaBqgP6I1_jsDgPX5PMrs5TUNbg_ap2DsMu5r5ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: حمله هوایی نیروهای اشغالگر به منطقه کفررمان در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/684375" target="_blank">📅 00:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684374">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69982cd01.mp4?token=pjGBG5cEB_94v7S0bvERgTkSt_nQpH1KykSSe3opahPDih2qKfsQ4Mu7hSKIw7_tT93GnNIkt-2R3N1C4M1JYPnKqayjejZf2yYHFTZljzn_sVWwDVfYECRen__qIoP4BzLBk-1RogDLv5GxVz0ej_rfzcCLbRQmAQCdKFyPSprBCW66v7qaMudAsYAb_MVp0Zd6CfGM-iXSUEXfrLdeZJvHJd3lUv7pUNEBVmGsJXtIyLUR6pTu6eM2SxARlMVP1Dk2v_S66vJ-08JEjyoGOAs2AxM5F-J-4Y0uGzsgxKC20M2pFojQcWqVeOyt7WOPVzRqh0wtaQDy6zl2TJoU7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69982cd01.mp4?token=pjGBG5cEB_94v7S0bvERgTkSt_nQpH1KykSSe3opahPDih2qKfsQ4Mu7hSKIw7_tT93GnNIkt-2R3N1C4M1JYPnKqayjejZf2yYHFTZljzn_sVWwDVfYECRen__qIoP4BzLBk-1RogDLv5GxVz0ej_rfzcCLbRQmAQCdKFyPSprBCW66v7qaMudAsYAb_MVp0Zd6CfGM-iXSUEXfrLdeZJvHJd3lUv7pUNEBVmGsJXtIyLUR6pTu6eM2SxARlMVP1Dk2v_S66vJ-08JEjyoGOAs2AxM5F-J-4Y0uGzsgxKC20M2pFojQcWqVeOyt7WOPVzRqh0wtaQDy6zl2TJoU7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساختن این جک خلاقانه خیلی پرکاربرد و راحته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/684374" target="_blank">📅 00:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684373">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
قائم‌پناه: تفاهم‌نامه اسلام‌آباد پابرجاست؛ توافق آرا بین اعضای شعام به قوت قبل باقیست‌
معاون اجرایی رئیس‌جمهور درباره حل شدن مسئله جنگ، تفاهم‌نامه اسلام آباد و اتفاق رای بین اعضای شعام:
🔹
در تلاش هستیم از طریق دیپلماسی و از طرق مختلف بتوانیم آمریکا را وادار کنیم که به تفاهمنامه برگردد و عهدی که بسته را اجرا کند.
🔹
امیدواریم بتوانیم آرامش را به عرصه اقتصادی کشور برگردانیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/684373" target="_blank">📅 00:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684372">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBQGr4lAqEtaBcdobXwKdsrNVjpIGBccq-ZFi64FGqr1fpNCkAqztibFH8tdfmuHtOym1ep4PW8d6439AGspva01wk7dhNozz93SaeQDiEfLXig2sv0KD3MSFWNjRp_ZjkBCydA9O-0efi8k6HfMD9Hj30TzX6QQAETu_iQ0Yc2MzIZDQTRCsei8HqMt_rHvjxr2GoRKptWDHcwuAwe6hLofg3P8zL_K-8A536Cu_j4ZjhvYSTnBlQR3G3VPTA5uG25lQ19zT36M_Vib-GTHqPhoOMlt9TF7iU0hf5BMa2s9KFQqyPW6XGpGEixhPPQGCiRX0z9jKJ6fF_iXzVEUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نویسنده سابق گاردین: مصاحبه درباره حکم سنگسار سکینه آشتیانی ساختگی بود
🔹
سعید کمالی دهقان، نویسنده گزارش جنجالی گاردین در سال ۲۰۱۰ درباره سکینه محمدی آشتیانی و ادعای حکم سنگسار او، اعتراف کرد مصاحبه با آشتیانی هرگز انجام نشده و متن آن را خودش ساخته است.…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/684372" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684371">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a1909c4.mp4?token=Gu3E_qs-5-FmnSIC74c9d1FpY8ZCq--5XfQsjjES2c_zEUo3zIcoFK6eDqAKs5lfxREoe5B-_xBbgMmmjAM0j125VfdTuoVw9mlS6vPssBpJw8zHL-z-wmp5X-xfOcgaou3nUuPaSq994kBbTtMaVbTK3MS-4vXAze_g38Efz7L9UPC131OEMgQHJrAeByyDo0tiH_lBrZYzhji5fPvFLYPFEHy5w_bo9ts5kU56IchzLg5GaYDMzqUUz3BQhhIpYDXs0c1QuyAlIXuc-Hbu43v7NBK6huD2MR4IzFx5YKtFcapmK-gNP9r-kwwym26ds3lbH5prVac9YjDBDz0Esg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a1909c4.mp4?token=Gu3E_qs-5-FmnSIC74c9d1FpY8ZCq--5XfQsjjES2c_zEUo3zIcoFK6eDqAKs5lfxREoe5B-_xBbgMmmjAM0j125VfdTuoVw9mlS6vPssBpJw8zHL-z-wmp5X-xfOcgaou3nUuPaSq994kBbTtMaVbTK3MS-4vXAze_g38Efz7L9UPC131OEMgQHJrAeByyDo0tiH_lBrZYzhji5fPvFLYPFEHy5w_bo9ts5kU56IchzLg5GaYDMzqUUz3BQhhIpYDXs0c1QuyAlIXuc-Hbu43v7NBK6huD2MR4IzFx5YKtFcapmK-gNP9r-kwwym26ds3lbH5prVac9YjDBDz0Esg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد جالب درون کپسول آتش نشانی وقتی آن را فشار می دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/684371" target="_blank">📅 00:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684370">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27c97455f.mp4?token=gwzCTHPOaznfM67-_lwUXvVD4rrg7EW-B6rrr-3apA4LGk4-yZCLi66qnuwUKDHc7L3S2TLaray_KrLT6knLS2l20-zN_5XyhszH99HVsHgLWOoe1qxfy6H7hYDnnwNTU8OSDpkm9H5dB90iQvr33dXs_M5z7RRAzJuNxVaJ2tcy8pKveGoLrtdiAmNIZrs-67Anozf_onGLQ3x_TjjpkOEY6kV2IcXwvcAjlQT0PuyE5yrE2xgk8MImQwtP-VQ5lB-M8aFps2fIcQ-CQyngmImkYxF2pg61-46fnF-tPqcN_KRLmW_BETVWnIvD1YeJnpUeXNd40xqJygQZzEtsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27c97455f.mp4?token=gwzCTHPOaznfM67-_lwUXvVD4rrg7EW-B6rrr-3apA4LGk4-yZCLi66qnuwUKDHc7L3S2TLaray_KrLT6knLS2l20-zN_5XyhszH99HVsHgLWOoe1qxfy6H7hYDnnwNTU8OSDpkm9H5dB90iQvr33dXs_M5z7RRAzJuNxVaJ2tcy8pKveGoLrtdiAmNIZrs-67Anozf_onGLQ3x_TjjpkOEY6kV2IcXwvcAjlQT0PuyE5yrE2xgk8MImQwtP-VQ5lB-M8aFps2fIcQ-CQyngmImkYxF2pg61-46fnF-tPqcN_KRLmW_BETVWnIvD1YeJnpUeXNd40xqJygQZzEtsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: حمله هوایی نیروهای اشغالگر به منطقه کفررمان در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/684370" target="_blank">📅 00:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684369">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
‌غریب‌‌آبادی: بازگشایی تنگه هرمز تنها در ازای پایان جنگ در همۀ جبهه‌ها، رفع محاصره و تعیین‌تکلیف وضعیت یمن رخ می‌دهد
🔹
هیچ کس جز ایران از مکان مین‌ها در تنگه هرمز اطلاع ندارد و موضوع مین‌زدایی که مطرح می‌شود، ادعایی بیش نیست و اگر این ادعا صحت دارد چرا شناوری…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/684369" target="_blank">📅 00:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684368">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
غریب‌آبادی: همچنان در وضعیت جنگی قرار داریم
🔹
وزیر خزانه‌داری انگلیس خواستار اعمال فشار اقتصادی بر ایران شد
🔹
«قسد» رسماً منحل و مظلوم عبدی مشاور الجولانی می‌شود
🔹
روسیه: پیامدهای تجاوز آمریکا و اسرائیل علیه ایران فراتر از خاورمیانه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/684368" target="_blank">📅 00:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684367">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73796fbb7f.mp4?token=O6aXa_oHFDyq90J61aeelZaYsQrKHF4kIAvJWiFD3dUuXHKYrFf2tNyDdA5Fx74J5Nz7P8Pk42assWfzivM4d6W5qRi-lDUdGHT8nqzATbSL-MSGPnRphsCS7ntXwH7omVmHZDf8AtcpzncHhfBpywmLyW-TqeojOnICPk6hsI58EUYyK-yOyIOqNn49wes4qIT-5ZgF7zUOzVw13guhJmSCFgbhGJwgj_v9kfSypAlphCgzC26CWZXZhJrV4D3Ynycs0dvMVURu8VXNds40Zovk3yBhJYZIuRoPCtyPCn7CQM61gE5DlI7HIE6YdD2MyqMRphhB2UGUv3GY4vD5hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73796fbb7f.mp4?token=O6aXa_oHFDyq90J61aeelZaYsQrKHF4kIAvJWiFD3dUuXHKYrFf2tNyDdA5Fx74J5Nz7P8Pk42assWfzivM4d6W5qRi-lDUdGHT8nqzATbSL-MSGPnRphsCS7ntXwH7omVmHZDf8AtcpzncHhfBpywmLyW-TqeojOnICPk6hsI58EUYyK-yOyIOqNn49wes4qIT-5ZgF7zUOzVw13guhJmSCFgbhGJwgj_v9kfSypAlphCgzC26CWZXZhJrV4D3Ynycs0dvMVURu8VXNds40Zovk3yBhJYZIuRoPCtyPCn7CQM61gE5DlI7HIE6YdD2MyqMRphhB2UGUv3GY4vD5hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه عجیب عملکرد مکانیزم دسته صندلی اتوبوس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/684367" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684366">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUSZ06hoBpQBJ89ce9g0AtmzfR-Mo-v7TK-R3mkCJRzPo6ChrswlbMdwIDnZZlnscwao9XsKIpfZNPlCtkgL7Ogr_aaidv3Yjxbe0SDMgySy0796FXgkMJA-kSwNsoC-KHF4GpHayewaTKjnqFj_XOsVaT_mcng3qafJ9YhL2iyBZjtd2zeoSs5jKdin2iwYmgKqpJogcfYacg23T_mmGSdELt5GaGtMCLNrpC_Xcmn4Xn_2H07ieuAWty9DsxMRzD-2MM-q_sP0RJaxZgq8h3rIfcp3fIzv-UV7JhECzAopLzSV91oC5yPaRbnFK1R_EE7fiK-1nsofqCNh0zTcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بیش از ۱۱۰۰ اارز دیجیتال
📈
۴۰۰ ارز اهرم‌دار تا اهرم ۱۵۰
🎁
هر هفته تا ۳۰۰ تتر جایزه برای انجام معاملهٔ اهرم‌دار
فقط در صرافی رمزارز کبرین
👇🏻
👇🏻
👇🏻
ورود و ثبت‌نام</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/684366" target="_blank">📅 00:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684365">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI-raUfzqG8xjSkuQD80ZVLGtE0MQDUMn8xa4ppSYS4Sfpw4Hl0_IV-_LYLd14hZad4HdglpG3ZYbl52JR3OUU3nYWu91bnkrtC2ipMMaQE1C33FLdsUNMFSCfZVhzysOwgA28mVEvcCXpuJPY8CDhUsI_BPW2hsL7rc-huwNHT7fULQ7NBgmBJows-_9G-4ak5f8lv98_d7OGqpbQWtDbUsJX4iF7dUOPho4oBZ6XfQWpaFm4Vys9AmXT0pDSkcvfM--pX26raRXKJyM2QP1G16pJ-lXe_wmmskN-kF79cylUPID44QjYbWtYOSIvFyPDHJJsJVzozuWfEhm_x9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/684365" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684364">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3edf60a1e.mp4?token=NvVHQHLXFJyx5-9Egrw5nsmnTEBStisNlKsbZqigllvvdj-50uC3vdzL_DuVBFFZpJUdSe0xT4IZpL9FFZKU05736yhjwlIKhomC5AM_pXiP7d5H54ncO6_Ghm0XNBLSy4wIBHpMFkBAkHnvXJzOs_8jA2E2Ea5fU-xgF3q1sLluOTn2QlSRoJ8kQmWIqkcYrekD_3nlrGsTKvk0T4mrUW_puIXN5uZU79H05tGnY9yjK5y73Wamnwc6tBtTDZHgm6gGpcErFhGWXy2eR6VlmYwCZ8Xx3d3kmgWMeV5RdyT5pUVhAn3a8PMV13Qo_Yyqytp5sOVs1FIQmFhiQZ0x2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3edf60a1e.mp4?token=NvVHQHLXFJyx5-9Egrw5nsmnTEBStisNlKsbZqigllvvdj-50uC3vdzL_DuVBFFZpJUdSe0xT4IZpL9FFZKU05736yhjwlIKhomC5AM_pXiP7d5H54ncO6_Ghm0XNBLSy4wIBHpMFkBAkHnvXJzOs_8jA2E2Ea5fU-xgF3q1sLluOTn2QlSRoJ8kQmWIqkcYrekD_3nlrGsTKvk0T4mrUW_puIXN5uZU79H05tGnY9yjK5y73Wamnwc6tBtTDZHgm6gGpcErFhGWXy2eR6VlmYwCZ8Xx3d3kmgWMeV5RdyT5pUVhAn3a8PMV13Qo_Yyqytp5sOVs1FIQmFhiQZ0x2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: شناورهای مین‌روب آمریکا اگر وارد منطقه شوند اهداف بسیار خوبی برای ما هستند
🔹
دلیل عدم انتشار متن توافقات امروز ایران و عمان و انتشار یک بیانیه مطبوعاتی این است که ما هنوز تعهدی نداریم و این موضوع زود است
🔹
به عاصم منیر گفتیم به آمریکا بی‌اعتمادیم…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/684364" target="_blank">📅 23:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684363">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTu45Q5mvH74qHoFue2dn2purOJtIarvXhZf41o4Ov6wvf-I0w8kEBDDprZDziDaAEFAasXz3UcijIZ9IibHQc4BBgkVd2Pk1hbt_67fnDo3oA2ou-xaPFbtGL_3QUt9EQcbFXMa1emxEvloCb-FWduCWK4sZo_kV3cRiTMMcHo-1tEvg2iL83-V8Rz6C2AkXTLjha3pU6bHn6bsK6cBM1QN5_DyEIZ_PylxiAv2_cHXO6q4NmVOGRsBEyhJeMV7gmjAUX7BbSwaIWWJMxi9Z8cCVRXNHhpQnG97A3GX6W2_JQTP79vSjeCIb_EkrxVVg0lCuHKTpX4RdWjNJXC-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس یادگاریِ زنده‌‏‌یاد اکبر عبدی، زنده‌یاد خسرو شکیبایی، مجید مظفری و علیرضا مجلل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/684363" target="_blank">📅 23:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684362">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26679b39e4.mp4?token=A7wv_zE4t95-U66Xm75llumn7eYWjSL3wQ6jXUITUrOcnzVCURTFcJN2lRW2bg5N0LbbUonyUvu385Qpzmwj13Gzz-jg4gb2AY-QtNZhnDi2ctBmeL2HRzm5JgnIZcFlqoGXKebiq4yIMAAVc2JLDOdGcbvWNNONlhh68KuzziuWVoPqeCEtN2TNKZeQZ8IvDWx8EUYOoteBXBbDijbmk2ALj_wIF_mDMq-BBt6o9nmPloG94jh_Rcl-BvFWvS3evX11Wia3t5bmx4GBH6wAxfvpFyzRw9viA5WA0TvsRTWapomYeZXLrlEr_aaieI3f6WKvAX_oEAKOrLueRHUZOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26679b39e4.mp4?token=A7wv_zE4t95-U66Xm75llumn7eYWjSL3wQ6jXUITUrOcnzVCURTFcJN2lRW2bg5N0LbbUonyUvu385Qpzmwj13Gzz-jg4gb2AY-QtNZhnDi2ctBmeL2HRzm5JgnIZcFlqoGXKebiq4yIMAAVc2JLDOdGcbvWNNONlhh68KuzziuWVoPqeCEtN2TNKZeQZ8IvDWx8EUYOoteBXBbDijbmk2ALj_wIF_mDMq-BBt6o9nmPloG94jh_Rcl-BvFWvS3evX11Wia3t5bmx4GBH6wAxfvpFyzRw9viA5WA0TvsRTWapomYeZXLrlEr_aaieI3f6WKvAX_oEAKOrLueRHUZOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانادا تعرفه‌های آمریکا را با تعرفه جواب می‌دهد
فیلیپ شامپاین، وزیر دارایی کانادا:
🔹
کانادا تعرفه‌های آمریکا را دلاربه‌دلار و نرخ‌به‌نرخ اعمال خواهد کرد.
🔹
از ۸ سپتامبر، کانادا بر واردات ۲۷.۶ میلیارد دلاری از آمریکا، تعرفه‌های تلافی‌جویانه‌ای به میزان ۱۵، ۲۵ یا ۵۰ درصد اعمال خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/684362" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684361">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e1877ded.mp4?token=k3WbXvmMQ_2-pPE8PNGG4hPjjS8Jet4XVvi6OVApQcMvFRaVGZnb1UovCrxYQhz69xkOKP6EkDDS-VeZhmsKit1pCCUD2sktZYi1IDmwYY60Rcy2iAojkvLjkFpriQWXI2QlfX7lyqAhQQzAsELe9WtpX88xSa1ooh_FiQIe9dFy6V8ZC3bg3b6b0YvFitKrZZUvg9ylwCbW1HOaEwYcYkI2AI2Z2uE53HJvU862dlo_gF2jtyRgKb8UiHEWHgw2eIKQGOa0Auh2_irNoN9W7PMRMuXGKM6-AgwdpuXlcMfD7QHnvJ19bxeBdbDcniVnZx42oOtrkbgKKQVJnEdqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e1877ded.mp4?token=k3WbXvmMQ_2-pPE8PNGG4hPjjS8Jet4XVvi6OVApQcMvFRaVGZnb1UovCrxYQhz69xkOKP6EkDDS-VeZhmsKit1pCCUD2sktZYi1IDmwYY60Rcy2iAojkvLjkFpriQWXI2QlfX7lyqAhQQzAsELe9WtpX88xSa1ooh_FiQIe9dFy6V8ZC3bg3b6b0YvFitKrZZUvg9ylwCbW1HOaEwYcYkI2AI2Z2uE53HJvU862dlo_gF2jtyRgKb8UiHEWHgw2eIKQGOa0Auh2_irNoN9W7PMRMuXGKM6-AgwdpuXlcMfD7QHnvJ19bxeBdbDcniVnZx42oOtrkbgKKQVJnEdqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: شناورهای مین‌روب آمریکا اگر وارد منطقه شوند اهداف بسیار خوبی برای ما هستند
🔹
دلیل عدم انتشار متن توافقات امروز ایران و عمان و انتشار یک بیانیه مطبوعاتی این است که ما هنوز تعهدی نداریم و این موضوع زود است
🔹
به عاصم منیر گفتیم به آمریکا بی‌اعتمادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/684361" target="_blank">📅 23:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684359">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b79635eec.mp4?token=d80FE-ftQRMKV2G_ldD-LECNadRMPyP4f9ZHsmBxJHE-L6WWPYaJB4AuJJYI2kYDAtT3dRmu9mOIEaRy5RjGlXBIb_WBvsKZLkgJjZRw575zTBEnJdXU9dgEeUUfdM-do6206vbDy72Lrh1XzIjp0-VParPrKnIYohnStfJDuqme3p-YIKeKPYl6hzSMmazZU-d6WLs0JwKCqxmbp03_7XtksglV1jpR-xaIUhOjhZ-cq-IcA4vqpHEyQJSYQjeSd0khbEYonvphA4PV3ihLQ97ilKiM_wLnhEoUJ6-eoDrVzbf6hZ3B-Q4XpLQB_6ZVRhUB5Kg8KWCB2jsRqpN9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b79635eec.mp4?token=d80FE-ftQRMKV2G_ldD-LECNadRMPyP4f9ZHsmBxJHE-L6WWPYaJB4AuJJYI2kYDAtT3dRmu9mOIEaRy5RjGlXBIb_WBvsKZLkgJjZRw575zTBEnJdXU9dgEeUUfdM-do6206vbDy72Lrh1XzIjp0-VParPrKnIYohnStfJDuqme3p-YIKeKPYl6hzSMmazZU-d6WLs0JwKCqxmbp03_7XtksglV1jpR-xaIUhOjhZ-cq-IcA4vqpHEyQJSYQjeSd0khbEYonvphA4PV3ihLQ97ilKiM_wLnhEoUJ6-eoDrVzbf6hZ3B-Q4XpLQB_6ZVRhUB5Kg8KWCB2jsRqpN9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: پاسخ جدید ما به تحریم‌های دشمن هدف‌ گرفتن منافع اقتصادی آن‌هاست
🔹
نباید مثل سابق با تحریم‌های دشمن برخورد کنیم.
🔹
بر خلاف ادعای مقامات آمریکایی تنگه هرمز بدون ترتیبات ایرانی باز نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/684359" target="_blank">📅 23:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684357">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVua2Os863m8DAiO3uNXmz0IHz5yzdl_yWDVJ7wxKFTln2qe4ZylhY1kaSeWdgJYUQWK9sOrj7aikJkKa_fLo5fVbtmp9txppcYQbOiRhCUXIp0hX7fybNld0-o_4e4fzY_N4m6mwLwIPDXrkGQXEVKfoxnl_ViZ7SxEBlUVuYWFHz8St5WdCuvvS1-AZFD82t-aTeWtr-zJDGGbOY5qtlZ16EI9fqIpHkEZrCTn1ygV-hqaFHrFq-6-9SmPIK-eh6azGvmgwage4n5pxSE1RU3TtWVGAVqi-ikZukh96Ynle49WLTpxV9P6BqAxFWJO4WBAM1kArDDJM-cYWYqGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وکیل و فعال رسانه‌ای سیاسی آمریکایی: وزیر خزانه‌داری آمریکا گفته است که وقت آن رسیده جهان بین آمریکا و ایران یکی را انتخاب کند
🔹
این اعترافی قابل‌ توجه به آسیبی است که ترامپ به جایگاه آمریکا در جهان وارد کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/684357" target="_blank">📅 23:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684355">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
غریب‌آبادی: چرا باید همیشه ما منتظر بمانیم آمریکا حمله کند؟ ما می‌توانیم دست به اقدام پیش‌دستانه بزنیم
🔹
مذاکرات ایران و عمان برای اداره آینده تنگه هرمز ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/684355" target="_blank">📅 23:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684354">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHP4KgZrD22KsemwvqbAcbU7hRA1NTmwGpTfdYbG2ZwUpKgA_dEJ2XLuVO9L0Z4narfrYcxWTULRNCwumhPamwYralLz97zXO4ImQe7F7drAfVbNzNQklUuLdJgcHRZCjJVDSmFO2SH-_5cnB1YSOkJktvvPADR3Vt7sNOGuQB_Jnc6G3k39_AfoSPe3QdMMfQgdZ95UoCmdFj3NUEhZkw_96bkHOaZ9D6gvOEtw5Fuf_Jy_SZL0tLm4N4sa7EiPSa_nY18Dh7SK6mLC4EPR5HkzhKxwMCo3ose0zP0crm-mXs1aCBDG-pA4eNraOfS782ZRMlNsFvTDrspuq0zQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارآفرین و فعال سلامت آمریکایی: لطفاً به مدت ۹۰ روز آینده هیچ گوشت چرخ‌کرده‌ای نخرید
🔹
در آمریکا ادعاهایی مبنی بر واردات گوشت فاسد از آرژانتین توسط ترامپ مطرح شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/684354" target="_blank">📅 23:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684352">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQNW1cjX3PWKLJ-L1v2-jQ6iL0hN49b_IrwbWkS1RCGJ9HIrdNH60j-PRjGWCVdbLC9XMuBv4hB9P7n52UYvgggRvh-SX-xLesGKKRy1NoRhyfvvCvmrux5dxWA_fFez-SHTht6dfpDzydmVswvCbamYFihDeviLyo7LA1wnXlfjMdj1JqlgRHD8P9JmB28MHhuOkOAOydcSEoc150ZaADNQCs3VaeEiM0SBp_VIecZ43OjDC0bLsIhUpM3oeXfbKx-IFGIfnn7BIsTM41vsy_u7hEQsZ6mJf0xoPInLVOJy1zrCpXktwwcocsVT2Do6TA9A3VVYK48ocS9Pa4UK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن افریز: فشار حداکثری بر ایران شکست خواهد خورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/684352" target="_blank">📅 23:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684351">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRswyb76WdXokDlDO8lYgsMJvC4oB2K-9a3WDTiVQGk3jCR7uGqFGPq77ZOOqNwTtf7NUM1Z50puIuh97OJppqujKxEy4zVR-1VksFVvIReuXjYaNI9Aatt2DbirFBOlqNhXsjQMDkROyxHlrm7Jn1iEGfnV3Smw_uN0Lq3cVAEkd3IFBpbjWicZyFxlsa4sEe6pnL7rIJhQpOhbXg0dgUGd5CRaSkDHfaGNuIEHmDEluJUmGpQMNeV2GZ6I8sP5FeKTdtAq3CT_13Mq61rfaiOQR2svjldLzvniO_SzRnskoV76hgMPbhbRzTGd86zPochi9Ar2ZeucHOIASsr1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صمت: فولاد خوزستان یکی از قطب های اقتصادی کشور است/ سرعت بازسازی در این شرکت قابل تحسین بود
🔹
سیدمحمد اتابک روز دوشنبه در حاشیه بازدید از خطوط تولید و روند بازسازی خط تولید فولاد خوزستان پس از حمله دشمن آمریکایی-صهیونی، با گرامیداشت یاد و خاطره شهدای دولت اظهار کرد: فولاد خوزستان از قطب‌های مهم اقتصادی کشور به شمار می‌رود و فعالیت این مجموعه تأثیر مستقیمی بر اقتصاد ملی دارد.
🔹
وی با اشاره به بازگشت سریع کوره‌های آسیب‌دیده فولاد خوزستان به چرخه تولید، از تلاش کارکنان این مجموعه تقدیر کرد و افزود: راه‌اندازی کوره‌هایی که در جریان حملات آسیب دیده بودند، اقدامی درخور توجه و قابل تحسین است و نشان می‌دهد نیروی انسانی صنعت فولاد در شرایط سخت نیز برای حفظ تولید پای کار است.
👇
👇
akharinkhabar.ir/local/10984144/</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/684351" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684350">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb1146038.mp4?token=m1WI6xcGkqn8LE52X4MQAKVjSnPNDnbvX5tmAZyMzATqNGUFzeXNeBLjml3Tvj9TONbPHCSFQP4HYrZTIypbvHzHtwFrUg9jROzUU8m42H98CcQxD9F108Z6pLcsDphDLVvoYLJZ4-FL4XgvfTNEb1RWPwZ0f0ISA2tagfH37x1sIbVW7qlfg50AIEnfGPrrCex1CEBBatqIAhT82xXUHRvE22z8AxqWhtzLchrsVZoQpMrDvxfhszmztR9180hSsEEzfi66niaTns0c-AsON_EGrYwv9rPLRHgaao2NspEKozmYPb2e6h5FlQ4tUx2RyxSwXKIS1c0vzFNk8EyJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb1146038.mp4?token=m1WI6xcGkqn8LE52X4MQAKVjSnPNDnbvX5tmAZyMzATqNGUFzeXNeBLjml3Tvj9TONbPHCSFQP4HYrZTIypbvHzHtwFrUg9jROzUU8m42H98CcQxD9F108Z6pLcsDphDLVvoYLJZ4-FL4XgvfTNEb1RWPwZ0f0ISA2tagfH37x1sIbVW7qlfg50AIEnfGPrrCex1CEBBatqIAhT82xXUHRvE22z8AxqWhtzLchrsVZoQpMrDvxfhszmztR9180hSsEEzfi66niaTns0c-AsON_EGrYwv9rPLRHgaao2NspEKozmYPb2e6h5FlQ4tUx2RyxSwXKIS1c0vzFNk8EyJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب آبادی: طبق تفاهم‌نامه هیچ شناور نظامی اجازه عبور نخواهد داشت و تنها شناورهای تجاری امکان عبور از تنگه هرمز را خواهند داشت
🔹
در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد.
🔹
محاصره ما به ازای تنگه هرمز نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/684350" target="_blank">📅 23:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684349">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
غریب آبادی: طبق تفاهم‌نامه هیچ شناور نظامی اجازه عبور نخواهد داشت و تنها شناورهای تجاری امکان عبور از تنگه هرمز را خواهند داشت
🔹
در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد.
🔹
محاصره ما به ازای تنگه هرمز نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/684349" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6JT2NrZt1vqGgEnHmbMhubyO2hXDVkPGJcfquGgQonclDtAvjZ7yzbRT0VrA5PPadsPF59XmYcHEc3umU0WGzomuzGc3JLMnfUlznbQfG3prE_K-m9Qr0-leyenhXWF3hJMtskkekUYM9MitUxKWPmA3CSAfNdpwrEOrnxa_tuFb1wHiEzNQx6CFO9skB4dsMKcKiQ88Co43lmlHOXMsgDZutfkAu-xHLN1wotSNr18xg78Xjxk_qo_wC0KwhGTRNxYc7F779grVUQO9dtj6QSBnpmn_DfPjRwrXa8PiyGuSzcx9GtQgJRq9nAV_MQ1LLxyCY6R06Ic52cI5EnCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQzH8cyd43AyIO3NCcDAH2KExjdZv-uDx5xe8P59OUoQDKWcVj73mG26fj9iaeBY4SP-wO5eKx_76XJUHFBEPRQ47yWKkx8ZJL89Da0dmmuXjObstu0LyxniswWWTUSt-PvMD0hEul-n2uhD-bZ6fNXDWf3ysPWJdWd7W5aL8lAn7eT65oOqvOuvipnJN8LXG8_unBKI4H8QGhsc9J257QXgefnQVrs-iao4VcR-c0vaNmDo79zwxssMT7pP11cv4hwMfQXAXcYstRpTHnevw17lWRQ-RLiUOspr5G7Lv0IqnAWnk86AEYSeiA2wn6Uc_jpcFvz7JiAUJbebEEMQsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa374e535.mp4?token=gFe6sY7wCkhA01KLUs6BOPgjpglZZXnVQ9AMQQTpb1ELRsBxbiuPuq0zrw05LEAbUuVmdU8DeneGk6Jv3lQ_AEbtkTzhtZ20a09WSfTCOsc5sbJRejOJxq77rwIctLil43TkgIETX2D7RBOSyxlU6drjxpt75VaeMCcfRjkpSEoMDcoWOB0uj3Lqj0OJQAN_2pTv89EBqqIGxC4HmogomGN4KXzeST8XXG30ib-B3KN5bLcRWvQWQQT8Ld8uon4PtFotoBMI8Yh20P4iTpvDtcFEDhQG2BsIR019n0-0DyqWgZzv-ArsmBai_GLBps4SsSs33SQKCoGbddOZDrQGGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa374e535.mp4?token=gFe6sY7wCkhA01KLUs6BOPgjpglZZXnVQ9AMQQTpb1ELRsBxbiuPuq0zrw05LEAbUuVmdU8DeneGk6Jv3lQ_AEbtkTzhtZ20a09WSfTCOsc5sbJRejOJxq77rwIctLil43TkgIETX2D7RBOSyxlU6drjxpt75VaeMCcfRjkpSEoMDcoWOB0uj3Lqj0OJQAN_2pTv89EBqqIGxC4HmogomGN4KXzeST8XXG30ib-B3KN5bLcRWvQWQQT8Ld8uon4PtFotoBMI8Yh20P4iTpvDtcFEDhQG2BsIR019n0-0DyqWgZzv-ArsmBai_GLBps4SsSs33SQKCoGbddOZDrQGGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنکیک شکلاتی؛ یک ایده خوشمزه برای کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی سراغ یک ایده جذاب و پرطرفدار رفتیم؛ درست کردن پنکیک‌های شکلاتی و تبدیل آن به یک منبع درآمد خانگی.
🔹
با مواد اولیه ساده، بسته‌بندی مناسب و کمی خلاقیت می‌توان یک محصول خانگی خوشمزه و قابل‌فروش…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/684345" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB0ewwq5YI0PAKpGicZJpGWrCVDRbu73mho0R0Gt5eu7nke1Iezz7JASvPgdg_HU2pQAZ13gHFB0XGim2JQTq2QnwFTBvfM7dYOpsCqjxT7SrKL7mlyyeCjbp3ejHpk0buUyyEcMy81J9qWPf8i0umY3Z1h5mlYyJ-rhB29p_ecCMmrNXgo7RAK1Dgm-WRNh9vgbdEKCYSmuVWBb-nCzp1JcNEDvQItgT_d9XrpHPeQQYHM_CKdf72dvz-I_zWSu_qOed7RgPBk4MAJXK6nuSDfjPt1iG3SETFU5JL0oMjvfjK4CBZeHJmwjXW7DNQWnUP9P-dFSEgfgUlMKB1sEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا تا کجا بالا می رود؟
🔹
مساله تورم هرگز از بین نرفته اما بعد از کاهش فشارها، ورود ایران و آمریکا به مذاکرات، انعقاد تفاهم ۶۰ روزه (تفاهم اسلام آباد) و ... به تثبیت رسیده و بعد از مدتی، دوباره افزایشی شده است. به همین دلیل، هرگز با کاهش شدید قیمت ها مواجه نبوده ایم اما هرازچندگاهی جهش قیمت را تجربه می‌کنیم.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3240404</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/684344" target="_blank">📅 23:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684343">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
غریب آبادی: تفاهم ایران و عمان به منزله بازگشایی تنگه هرمز نیست
🔹
انتظار داشتیم تا با کمک دوستان عمانی مسیر جنوب در تنگه هرمز را ببندیم اما فشارهای آمریکا این موضوع را محقق نکرد که در نهایت ایران تنگه هرمز را بست و سبب بروز درگیری های نظامی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/684343" target="_blank">📅 23:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684342">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d5b024e0.mp4?token=hK4s3pn3Kn5Fg29XB2kxe5wu4zKKGXG-ejBwaruxkOFSy0vs0GMQnd_yJOvgeRauNldFKKqo64co42_ed6p3F4-sI-gvd5HdJSSSsfNRkzM9UTEyF2H9a-cF4IgmGsHAAwZt4PAIvI5m9-Dyz2sViIkmL1krLbm6tE4XFIAvOAh5B8KhXp_CordNjGhMqJ68qUgf1W505bSCj9IZ8_VEA9bLPQYOsftaMow9UpxeZ7MQanw9JfaP8Tx3a2kv1JTGw33mYXYFQYkxLFnUD1VTdeF4FPh4QvuTdc9SWUjat-P4bzdrwNXvTP1bx7Ck7Gd6DcsjlCffROTkUnOsalVi3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d5b024e0.mp4?token=hK4s3pn3Kn5Fg29XB2kxe5wu4zKKGXG-ejBwaruxkOFSy0vs0GMQnd_yJOvgeRauNldFKKqo64co42_ed6p3F4-sI-gvd5HdJSSSsfNRkzM9UTEyF2H9a-cF4IgmGsHAAwZt4PAIvI5m9-Dyz2sViIkmL1krLbm6tE4XFIAvOAh5B8KhXp_CordNjGhMqJ68qUgf1W505bSCj9IZ8_VEA9bLPQYOsftaMow9UpxeZ7MQanw9JfaP8Tx3a2kv1JTGw33mYXYFQYkxLFnUD1VTdeF4FPh4QvuTdc9SWUjat-P4bzdrwNXvTP1bx7Ck7Gd6DcsjlCffROTkUnOsalVi3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزه مقاومت: حملات رژیم صهیونیستی به جنوب لبنان و منطقه علی‌الطاهر با شدت ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/684342" target="_blank">📅 23:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684335">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epDvw_lAECPCLxyvdFb8VyPHdKHKejVJP_Xh_nqy3inKEjrIodlZLJvaaACQZuy9grsD-k8kshIrGkWFjHCHywBlSoRh55Pa_sYVBq5p0YM5SlKXzK14F-ozCkhYwYBL5CJebtfjxnzXYahkNO168OIm0X75nubrvyutiSt0C0WKnLZCoZ8do-hzSHw3nAqhfpr8ghtZKguBMYYVBf917V6ZRd8v0hU_Uk4hqdbuEjmrVZxai8ggif56nm960CWB3DKF6AyyuuJn1Gn4kAyvckJyQb2PIgsV4g-qAh3Hdws4MKvh4WRSBfqdtEmSl0P68uWYt9kBu2qqvtDlGz2JgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYN6pVlxi_lSjpTbON4-KOi_PQNXL9sMzNoyFeu7MuECcEri8eTLr5M8fmMBM50djGfoUrehbFRZar1kSZlfxVbDWdmqSthtxqOtXZnPS9x2mgLBKF3FQl1HYwq_qiM1FhVd8yc5Tu3FCfEzUPHtwSWXIPrIZaJK1c_3E7zKySkmkLrqh-0Ifewx4gu4dVAIQ3Kdywya2qmhxB9727a4GokACV_0ZDslXPxh2VEZ2XW1pzQT-Fpj7ALPeuwlfZnysLAsJX9Sa21BcePOKpSb_yd5mjFXlfe00IldSVR1EJKM9zBn03lV4YyYyGNO9x6a85rZ3GG5ifDv7-Uo0R8pPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsAKg0uxPeDWMDAmrXjWpnjmrAGePt45xBJzZ2qexA_onjSG3vQ2oMUkO-PCvVRXRr2Im5e41Y1SD_WzJ7_ZRzpxwcUl7CM90bxUbrWWl0zPEoai41yLQIoo9L6ZdGqi9Ef8xP-YSKVGQWNFnjKs6vXB7OtAOfvZWxrq_w0OsLOyM_56xU_rmkqEl4VitshKQcNMVCac_ehFhydAmcRVnJnSvh2UoWZizUfOD9uS2k1A2OSpnp6h8GZvSdCpX9FeIeAfoKGVoVl7RJ7po-m-lHS3H_pDBRxRVW1sWGNIVXK8K6lS5Zku1HzYiXaQNq4VNeWHNsppt9H50D5V4ekQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEryYFe789vKJciQf8grzOk8WHbdrGOm2EsRoiMM7bhVXaWaQzoAC15661EwpXszQI3GvF9cYbMIP4s-HCsc1kbnnaKpNFJfD-UTFcx4zU7HzX4w_DcXxmnHDkNk0xTLa6llcsgNxoQNJVhG0jNkWO9FaSbQrV6U_yLhJnk76wJayk8tiIYJ5c_ytAH9EpHE6KPnCuml_Z58ibtgQdAWoSfmllhNB3N_cPM6LlUjr13KkYzpORWc_48PM5JZxd4yWjTcNBiyFlFb7NU0vx5eGcPczt2x5ufLAMvt-347h8THZAczcfj1QenNaSNhJ-JuBBpC5GqerSXU6RLUAgbhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KttFsiKWrTY3iPQ03zErsZd3fjABrz_XVtDa6R0ifuxvtvSmudwGdWcm7C0XK4OD4c0yj4dZTcIiclZ_L6HbONa7ZFnMaHtKjXpcARZUZfDYEmQfmN4UwiBVxuDvHcGpLTLUrthCiOzW11W00laJpt-xwbWFuvcAYp97vv6N0RMhvlZ621jOzZSbfmeiGiZIkv180zo_8eudlwEz6D4RvMTVv4ZAIfEPN91OMeBnsrLhe6yQLwPka6J1jHfuE-JpIkAF7TcXxrznicJxv5ohT2ZzDpz8--mDrYowaEKqN8BocWgwNTLK4yzoHn1VzV0cCukJIVFJs-pEBkK8SFj5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4CoTkjOr5xFcyX-PqIDOOCxRYUOHXxQgOCeB2MJiKMa1evvlrY5W9nECiU3SWZqYYzBIFJR1IonXt6rN0DwiqNoYTOBfM_rharAhQNeKrT1N8dIpFvnaa5iGmVBqqKzkkdYp1eBtm50RJngmR4tECyyuyfMyDE4S6RXQcoKTbB0COnsZJ4n2d_z2-J3vLHkw57wLJblRVmumgsTtnyWtQtpjxtL5nmBc7bYKlI7cv05b7avRTcHpq9-l1ghSU0QzN64U9EWMji1eZDK5VESo9geVQvkQniLMyeEtcTpaqCnPjE-XIsRU0lgc-6wyHzuyZr7UDTJIFkE-kTYrU38Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند خط قرمز مهم برای سلامت مغز
🔹
اگر می‌خواهد مغزتان سالم باشد و دچار آلزایمر نشود آخرین توصیه‌های بین‌المللی را در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/684335" target="_blank">📅 23:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684334">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4lTl9jW-I1AjBAv64p08-_SZ0n_I2F24nEr6hEKLcowkHdsGuhIY7DJE9wrcTvNBuc-j7P0L7yX8Ufl6xCxdBp4FZKlTy_LSDzChZQt-Mz14eZAN-3HG6RFn2j_Wqf3gl9yrBVxnkslFGlnFFtQAT7GO7s_qC23RX7ilk1COTQdbXVoCjKaNuYvaGYBKunIsrqpjgkVFjnE2XAMtBigJNQ2cHIQRrGezMc7hlfBgRuzOPQ607pDClHuRQb9497gzcF8csv6ouiqqLN-SnYTEmxPzl79zm4cW0sHxcA1romOo6UHVWiWpbmeM7t8H7dBtWhzKIke1_G2V6nwk0mxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور کریس مورفی: بلوف های ترامپ درباره فشار اقتصادی جدید علیه ایران، نشان می‌دهد که او بالاخره دریافته است که در میدان نظامی جنگ را باخته است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/684334" target="_blank">📅 23:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684333">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
تهدید عجیب ترامپ علیه ایران؛ به زودی ضربه نهایی را خواهیم زد
👇
khabarfoori.com/fa/tiny/news-3240460
🔹
میزان کاهش سهمیه بنزین اعلام شد
👇
khabarfoori.com/fa/tiny/news-3240428
🔹
قیمت طلا تا کجا بالا می رود؟
👇
khabarfoori.com/fa/tiny/news-3240404
🔹
ماجرای تلخ پسری که اخته شد و به عقد امپراتور سفاک درآمد
👇
khabarfoori.com/fa/tiny/news-3240346
🔹
«مسعود پزشکیان» در جوانی و به همراه همسرش در کنار یک آبشار
khabarfoori.com/fa/tiny/news-3240287
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/684333" target="_blank">📅 23:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684332">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a52bd8f78.mp4?token=Radn-k89KR4J5l0kQ8I31yyZurfWtLVlIxzcJPYzQmR1mDjQUuCSFS_hf0ATHeaXH0Zc2CIwPcUKaZnPCUZUdfQUeIQjP0T5Hp-hl85l61YqfBx2WqdrrdBW1TVCv3bAjojw7GBktaosrT-RlLAjekeY1u3fh0TyIgcGOFCFeczuyhnFyVokTFI0HqLosrYcovmlwILoSzMvbAYK1YyC8WXGUU0UTVxn6w9ec22ULEh5xY6c8wIMpWLryc_zxobld4sdKWIE6TB2-XBeitCMW3Ck38QPRGSC6pY9o5oGamyZqSPpm1VKKDSv6IPM3fNzZxmwqw4YT_lLNnriXgVFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a52bd8f78.mp4?token=Radn-k89KR4J5l0kQ8I31yyZurfWtLVlIxzcJPYzQmR1mDjQUuCSFS_hf0ATHeaXH0Zc2CIwPcUKaZnPCUZUdfQUeIQjP0T5Hp-hl85l61YqfBx2WqdrrdBW1TVCv3bAjojw7GBktaosrT-RlLAjekeY1u3fh0TyIgcGOFCFeczuyhnFyVokTFI0HqLosrYcovmlwILoSzMvbAYK1YyC8WXGUU0UTVxn6w9ec22ULEh5xY6c8wIMpWLryc_zxobld4sdKWIE6TB2-XBeitCMW3Ck38QPRGSC6pY9o5oGamyZqSPpm1VKKDSv6IPM3fNzZxmwqw4YT_lLNnriXgVFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: اگر اتفاق غیرمنتظره‌ای رخ ندهد تا ۹ ماه آینده مشکل برق نخواهیم داشت
🔹
تابستان سال آینده هم شرایط بهتری از امسال خواهیم داشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/684332" target="_blank">📅 23:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684331">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
غریب آبادی: تفاهم ایران و عمان به منزله بازگشایی تنگه هرمز نیست
🔹
انتظار داشتیم تا با کمک دوستان عمانی مسیر جنوب در تنگه هرمز را ببندیم اما فشارهای آمریکا این موضوع را محقق نکرد که در نهایت ایران تنگه هرمز را بست و سبب بروز درگیری های نظامی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/684331" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684330">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b504dad60a.mp4?token=rs-dN7JrM90DEtxg7eur_W_B7hVCeEaxu0iK_u0an3BOAZIsDzUDyojfVpW3LWW4WK8a8iAyxIib8Fhevidc5RXMCXFTKMWkqV2N8HrdxsfuXPhS3FWwBnajshT9qCA9z5RvY6hVP8RCUtde6cMm5bBhl3cB7CIvihe97jyB4GLeF9c7OZo0odntJQB8GjePASbI5TzU23IefEF6wqYLf7ugIno2zYKxrnIR9TRTWrTRXQlPmH2R4tErMBdgQsWgoXU04oe1efkCA3wor6TTnBsG6luXmHmMjXBkHJ_6rvwgAyfAXAnhDqYcpfYeqoAGd-U5JBBCYF1-PnlCEXTlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b504dad60a.mp4?token=rs-dN7JrM90DEtxg7eur_W_B7hVCeEaxu0iK_u0an3BOAZIsDzUDyojfVpW3LWW4WK8a8iAyxIib8Fhevidc5RXMCXFTKMWkqV2N8HrdxsfuXPhS3FWwBnajshT9qCA9z5RvY6hVP8RCUtde6cMm5bBhl3cB7CIvihe97jyB4GLeF9c7OZo0odntJQB8GjePASbI5TzU23IefEF6wqYLf7ugIno2zYKxrnIR9TRTWrTRXQlPmH2R4tErMBdgQsWgoXU04oe1efkCA3wor6TTnBsG6luXmHmMjXBkHJ_6rvwgAyfAXAnhDqYcpfYeqoAGd-U5JBBCYF1-PnlCEXTlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی‌آبادی: مبلغ قبض برق ۷۵ درصد مردم اندازۀ قیمت یک پیتزا هم نیست
🔹
ما از ۸۷۶۰ ساعت سال فقط حدود ۱۰۰ ساعت کسری داریم.
🔹
هر کسی بخواهد برق او قطع نشود می‌تواند از بورس انرژی برق خریداری کند.
🔹
از نظر گرما و تامین برق در پایان دوران سخت هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/684330" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای پدر نیازمند حمایت
🔸
این پدر معلول دارای سه فرزند خردسال کارگر ومستاجر   دراثر حادثه دچار شکستگی کمر شده وتوان پرداخت هزینه های جراحی ندارد
🔸
اینک برای درمان وبازگشت به زندگی نیازمند۱۰۰ میلیون تومان است منتظر مهربانی شما عزیزان می باشد
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت های خیریه مهر مبین:
6063737004808968
6104337806663215
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/684327" target="_blank">📅 23:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684326">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d538abd.mp4?token=ioVWJ3988A2vmP3DpQvnhpnSRNwuMLGo6yFFbxJhamY8EfIsYIcztYKiPJqfrhHktxRp2FCP5s8Q4R7crcizLuuuMbMrfnKlpPnnOu0-ukOlNkcHbzyLfxUv7bHsw5yEtmE4pnc-tn1kDhcUO5pU3D7xrzY8KFocIde-oknYYDsRtrZ1hRtqrhUxAJLKdqHx3xkGsYAISu9M3glP9ViE_UW2UvVqrIAXeYkTfJxh81-tmV3oV3im1nrRYMXZaKVVqFxu-eD81Cs7NRFhaeGMilRQIp983Og8HUCSI6ezyj0I-w0gMXRE57jjvfncqanUL2mnbj1buIs8HgAvvJP3Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d538abd.mp4?token=ioVWJ3988A2vmP3DpQvnhpnSRNwuMLGo6yFFbxJhamY8EfIsYIcztYKiPJqfrhHktxRp2FCP5s8Q4R7crcizLuuuMbMrfnKlpPnnOu0-ukOlNkcHbzyLfxUv7bHsw5yEtmE4pnc-tn1kDhcUO5pU3D7xrzY8KFocIde-oknYYDsRtrZ1hRtqrhUxAJLKdqHx3xkGsYAISu9M3glP9ViE_UW2UvVqrIAXeYkTfJxh81-tmV3oV3im1nrRYMXZaKVVqFxu-eD81Cs7NRFhaeGMilRQIp983Og8HUCSI6ezyj0I-w0gMXRE57jjvfncqanUL2mnbj1buIs8HgAvvJP3Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی‌آبادی: مبلغ قبض برق ۷۵ درصد مردم اندازۀ قیمت یک پیتزا هم نیست
🔹
ما از ۸۷۶۰ ساعت سال فقط حدود ۱۰۰ ساعت کسری داریم.
🔹
هر کسی بخواهد برق او قطع نشود می‌تواند از بورس انرژی برق خریداری کند.
🔹
از نظر گرما و تامین برق در پایان دوران سخت هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/684326" target="_blank">📅 22:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFKZlSKWBz5E1i3r73mqW1GvsmK42rl5PtfzpduDRL-4Baw0IqwYlhJ0zMDqWY66THNTB0iGfUXXcCsYUd5u-slive9mwDovrM3luwEZ8OlLrkZOhWrpi2TmmpLpV6MIEIsJS-eS0N5dqSTlYgMFUzk70rGs4uxOkR1LkWowZSjQq7oR6Tv_lPUy_kZqn2QjAykQb3U-NR7JO4kk2678Gw8CVHPJr-GH0OC0MCp9827EOwe2bJ-_fihTMa98Tajhut_i4s30MTcUY5AiAOFKCRS95P66Xm4NjJaFKeOky7SciIyMIeaD3WecYyJBg86qDbM8mlCF9NpMkeTsKt9Krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: با دیپلماسی با همسایگانمان تعهد به صلح را دنبال می‌کنیم
وزیر خارجه پس‌از دیدار با مقامات پاکستان و عمان:
🔹
تعهد ایران به صلح و ثبات، همراه با دیپلماسی استوار و مستمر با همسایگانمان دنبال می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/684324" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqx_5BezutXWbujP-QL9hK5kOO8GO2JqnN6-MVT_UzKUavhMmDF1Ts3mNTqM_fDQqNFN_D-N8FvCGe3GrCOA2vQJaucR2shXb27KlcIo4gd1EZekWI57O3M7Gm04B8BfADCebe9r2kE22utYvSNpH7EDuNiP0gfI0rZ3OTG68isuzWNFXHaRPYeYKEiz6gUK5x5gQmClPe17Tuadyywsr8-DQ8RYmy_qygiEfwqwA-p6zrqo1txqaPml_-t3vufG1TWx_K6QpmW6HLW2vfGjqDzgtR99RL-55MSFaIMpoDJ7A9Wt7olxS0t27MIeNlJwxD8meyh4aPwSV-7BVuoEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف به بسنت: نمایش مضحکت «روز پیروزی» نبود؛ «روز دلقک» بود
قالیباف در واکنش به سخنان اسکات بسنت که پیش‌تر ادعا کرده بود تحریم‌های جدید علیه ایران مانند «عملیات نورماندی (D-Day)» کوبنده و سرنوشت‌ساز خواهد بود، در نشست خبری دیروز وقتی با سؤال خبرنگاری درباره توخالی‌بودن این ادعا مواجه شد، دستپاچه پاسخ داد: مگر من می‌خواهم اقتصاد جهان را منفجر کنم؟! نوشت:
🔹
این برنامه اصلاً شبیه عملیات نورماندی نبود؛ یک استندآپ مضحک در کلاب شبانه بود که در آن حتی دیالوگ‌های طنز خودت را هم فراموش کردی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/684323" target="_blank">📅 22:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2296312480.mp4?token=GO72xpVw72yA4X9tusRo_nVUOib7MerRLaUcX9AjlGCRMW4_5-aDozFbtKBVVzgQ3Q8nt9gJezJaTnKbSY9mZj1h7XorT3abLb-goHtjmlHJ_SeRSKUaEZTEKlUpYtvPIslfxHGcqnhTEThd-K6BYWwmDoUkAOE8DRb-pAg8jRQpGeW95FCsQt0LTtQ2_AWW4xRb04fmCa75yN2CobSr_XzbL7u81EO6RsOoDLqKc_E-i2PoaNafO15o7A3Hzd51yzS17qjgIoPXtlhKBtduhkmBDZbpb8RAH379C6yvwMjVJYISc5De773jSKeNZ7X6TCXKAbkUaCMb0-ze0bD-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2296312480.mp4?token=GO72xpVw72yA4X9tusRo_nVUOib7MerRLaUcX9AjlGCRMW4_5-aDozFbtKBVVzgQ3Q8nt9gJezJaTnKbSY9mZj1h7XorT3abLb-goHtjmlHJ_SeRSKUaEZTEKlUpYtvPIslfxHGcqnhTEThd-K6BYWwmDoUkAOE8DRb-pAg8jRQpGeW95FCsQt0LTtQ2_AWW4xRb04fmCa75yN2CobSr_XzbL7u81EO6RsOoDLqKc_E-i2PoaNafO15o7A3Hzd51yzS17qjgIoPXtlhKBtduhkmBDZbpb8RAH379C6yvwMjVJYISc5De773jSKeNZ7X6TCXKAbkUaCMb0-ze0bD-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: در خصوص قیمت برق اتفاقی رخ نداده است
🔹
ما برق مردم را بیمه کرده‌ایم و در قبوض برق هم وجود دارد و ما طبق شرایطی موظف هستیم که خسارات را پرداخت کنیم.
🔹
ما خودمان را برای این روزهای سخت آماده کرده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/684322" target="_blank">📅 22:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCFSuCMZegjsdlHZUAdZ-pPAqprRn3i_1FjXQMhfc_9-ObPtcwWzdahrG3wFNGYcEyDQK-WAgUKZ7_I78NL1bgHhWeqSV7tuefpQckrGqSDWyhyYvjv57tcnuhgz0l1jk98Zhcvnk0oxs5GyNJpDlPYq_EDuvgSjrcSKSTuOBp4H7c3JfR2xWijHESHwzIIrC9Zts9IDC3cK1Gtt6fzR369RBE7-WjzjROnths8nv9go47vMNZcb0MWzkHTNzlishaSKEPWBxGgd77erv95VNvKH_tpOXipMrjbWM_YrEchmYgYJ2g2-7o4EHY9DjMM5_WByIDvUiiXuW8qADqOSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار مجموع بدهی رئیس جمهورهای امریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/684321" target="_blank">📅 22:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سالی ۳.۳ میلیون ایرانی به ترکیه سفر می‌کنند!
🔹
بر اساس داده‌های مرکز آمار ترکیه، طی سال‌های اخیر به‌طور میانگین سالانه حدود ۳.۳ میلیون ایرانی وارد ترکیه شده‌اند. رقمی که نزدیک به ۵ درصد کل گردشگران ورودی ترکیه را تشکیل می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/684320" target="_blank">📅 22:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la8tjqm4DWxKZOnD4VRbw3QnMrNsXHnpG8rC4I_rUP3oEd42Qtn_UNe8X5JG8twHWe4GeEpS6ifGVT75jCvxEa2KmNog4RtKQFvewW1PYEfWMzZ_-4xz3ajndaG2uqhZbRU7J00WoeUa7Y7HMpJL012jDlTiYa3gQ_W1BwG79gcpuaxm3hazYJRFZWzAucK94G6kyFz_NankbkkBjj35Q57BjrETQKzOGH8D-qbNq7Kdr8vUDh4mPpNJyfU5sa8Wg58xUl-st-tmcR_KLgga5dyeeGyfTfhf_5wRSuQqk2T-oY2tpY-7d17o_dtdgYh9JfNAk4L733BgMxe0pjPf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه جهان که ابوریحانی بیرونی سال ۱۰۲۹ میلادی در کتاب التفهیم ترسیم کرده است
توضیح نقشه:
🔹
بالا(جنوب، سواحل آفریقا)
🔹
محیط الشرقی(خلیج بنگال، اقیانوس آرام)
🔹
بحر جرجان(کاسپین)
🔹
محیط الغربی(اطلس)
🔹
بحر شام(مدیترانه)
🔹
بنطس(سیاه)
🔹
بحر فارس(خلیج فارس)
🔹
الصقالبه(اسلاوها)
🔹
یاجوج وماجوج(شرق دور)
🔹
الخزر(شمال کاسپین)
🔹
اندلس(اسپانیا)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/684318" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزیر نیرو: ما آنقدر نیروگاه داریم که اگر دشمن تمام زرادخانه‌های خود را خالی کند، نمی‌تواند همه نیروگاه‌های ما را بزنند
🔹
اغلب کشورهای همسایه ما از مواهب صنعت ایران برخوردارند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/684317" target="_blank">📅 22:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۹ کار ضروری که قبل از فروش گوشی شخصی خود باید انجام دهید
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/684316" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b747b77af8.mp4?token=CixDH2tE3vMphx7ato148W7bSxBBOWb1TMkDqiCH_kZzdnoIxOSUMyIXbakUtQABQWrciCxHg3ekoFVdCIRzG_zesbUIshpfGB_4XEzDxBq91-Mldzj1rqTLPEYy0PVSJK8EDAiXn5HUNguqxwlODL1lqFz8LfXDJ84-xtJCx9LdXVKYZHvgUjjOwL707ie84G0H2vhHhWMTMlsq463pfrPhmiranDu7kriHWMEolaO7oe1RCvCYz7axUi7rX33zGzrC8IMsOGJDmosdtMXa1bqJYJu3y_yg4w7kxjDBIY0osB_X3XvA_dxxe6Ed_d1h7rpFxAaZgWynQb-J_5SngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b747b77af8.mp4?token=CixDH2tE3vMphx7ato148W7bSxBBOWb1TMkDqiCH_kZzdnoIxOSUMyIXbakUtQABQWrciCxHg3ekoFVdCIRzG_zesbUIshpfGB_4XEzDxBq91-Mldzj1rqTLPEYy0PVSJK8EDAiXn5HUNguqxwlODL1lqFz8LfXDJ84-xtJCx9LdXVKYZHvgUjjOwL707ie84G0H2vhHhWMTMlsq463pfrPhmiranDu7kriHWMEolaO7oe1RCvCYz7axUi7rX33zGzrC8IMsOGJDmosdtMXa1bqJYJu3y_yg4w7kxjDBIY0osB_X3XvA_dxxe6Ed_d1h7rpFxAaZgWynQb-J_5SngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: ما آنقدر نیروگاه داریم که اگر دشمن تمام زرادخانه‌های خود را خالی کند، نمی‌تواند همه نیروگاه‌های ما را بزنند
🔹
اغلب کشورهای همسایه ما از مواهب صنعت ایران برخوردارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/684315" target="_blank">📅 22:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684314">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7spZvRI9-DeyJvWaGoj3S9QfLaNr_rMgoy_twFY5nuHQ9pj64lnr_Y3e1A8eTUbVEud2GYPsau1GMH-RcallNFhhURwL8jFmRIJvuvaqmvEamVwDyUhcKQZ2r2jsqgryJbRmvmKKfy6gG4a-QPckbmBi01PQM-2UhA6zN1N3d_he-70VkBs5ymJgQ7IKYgCuDYaec8f-zeg9NdsdXbm_7u0SXrZUhJqBFPrxGGhk17dmEb1tTEUqRLkSiuqT63TKjaGrMH6Up9NWqAbpgiPDmxIbQgvOL5736ZhNN7Dps2UQaQyVcrCYKJN3ydJff3dothDDFBRHgrily9QYdqaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹۰ درصد سایت‌های همراه اول در آمل 5G شدند
🔹
همراه اول با اجرای کمپین «سرتاسر آمل در مدار 5G» درصد سایت‌های خود در این شهر را به نسل پنجم مجهز کرده است. سهم 5G از ترافیک دیتای همراه اول در آمل به ۱۳ درصد رسیده که بیش از چهار برابر میانگین کشوری است.
🔹
رکورد ترافیک روزانه 5G در آمل نیز ۲۰ ترابایت ثبت شده است.
🔹
مشترکان مشمول طرح می‌توانند با شماره‌گیری کد دستوری ستاره ۱۰۰ ستاره ۵۱۱ مربع، یک بسته ۱۰ گیگابایتی اینترنت یک‌روزه دریافت کنند. این بسته برای هر مشترک تنها یک‌بار قابل فعال‌سازی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684314" target="_blank">📅 22:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684313">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وعده وزیر نیرو در خصوص خاموشی‌ها؛ دو هفته آینده شرایط نرمال می‌شود
‌
علی‌آبادی:
🔹
خاموشی تابع تولید و مصرف است و همه عواملی که ما بررسی می‌کنیم، به ما نشان می‌دهند که با توجه به نیروگاه‌های جدید ساخته‌شده و خنکی هوا، شرایط در حال بهبود است.
🔹
در مجموع ارزیابی ما این است که اوضاع هفته آینده به‌مراتب بهتر می‌شود و هفته بعد از آن نیز دیگر انتظار داریم که کاملاً در شرایط نرمال قرار بگیریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/684313" target="_blank">📅 22:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684308">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTco-_Zr7kzydN_xlWEEJEAdpqzdmvTRPWYUL9ceQ6vPs9UnHzxpxjXO68CsgPuw-gb3-QTOPxfcCqtFHxd37RQNd9ita6UQGoOMNFHI9zSDX-cpxc94QL10rSUyjsCbTz-rtmZjyo7OZpJauBu3y1FKvSUF9R1KYQFU08Mjv1oNqzfhU15c95oyPxa5S9fFmiWX_FzH_IVO2MOe4hubzn_KVWa1MuyaPAfKyrT22ICkKekleBKzgwVLnD5zfFpX6VEx9fNTPgiaI4xaMNI1if8Oppe-Vj2WcKN_9A7Gt-gagof4IsB86kg1aUGvRupnDdVj6j7u6wd43DsUUFXfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش انسان به اندازه همت اوست؛ بزرگی هر کس، به اندازه هدف و تلاش اوست
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که ارزش واقعی انسان به همت، شجاعت و بزرگواری اوست. هرچه هدف انسان بلندتر و همتش بیشتر باشد، جایگاه و ارزش او نیز والاتر خواهد بود. #نهج_البلاغه_بخوانیم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684308" target="_blank">📅 22:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684307">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouSnwIqs-RfECb6bxxWEMKmdjVeDvFOleoMHaqDoO0Pjrkba1ND_77ArGMt7ENMs1J0rojvZfdBCi3T16sf_pGzcSRNd91W6FS8WjzK_KiZnCc-AkiB3s-n5eiEDp3b6RGRMlOmNZhTEHG1LxoZ-JVXiaSaYrgYACLBsb0kgjJJec9cPdE9IrpvK1Zw75vnFXUt0JIDDf3nyS5v7CaiPTy2OAWloVHHhpv-RRgJKejYaro4ikixfCwUk2hWwqjTePZ5Qiaad7eI36t6rXGQsLCM34zTq4ag8wEl52LSRHvOTCBERu7OAY6zzO_iPZQzXyWj2LVoPJxY0xCqBDfdbNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش فوق‌العاده کیا پیکانتو ۲۰۲۷
خودرو محبوب بازار با قیمت قطعی
🔹
کیا پیکانتو عرضه‌شده در این طرح به موتور ۱.۲ لیتری چهار سیلندر مجهز است و نیروی تولیدی موتور از طریق گیربکس اتوماتیک به چرخ‌ها منتقل می‌شود
🔹
مصرف سوخت ترکیبی پیکانتو برابر با ۵.۹ لیتر در ۱۰۰ کیلومتر با باک بنزین ۳۵ لیتری ثبت شده است
🔗
ثبت‌نام و اطلاعات بیشتر:
https://sale.kooshakhodro.com/
⏳
ظرفیت محدود : 02149970000
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/684307" target="_blank">📅 22:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88cb1429ff.mp4?token=Nr2u4JiYij3OfcxvMLoTUANnyxhpQ61MZv36Gm95maYS82nXW24I3HgGHvN3mq7tHYnoFGjOC5I3pi0SwzvIcANcpb3m9f_0T0Z-r8kfPb1rz6lKyrz7CvfAzG43El55QfzyPUYuO1zYGNlK11bOGMs7FDlJcNVFe44fhdvNONHoXdSapnFSrH7-zQphSdL0zo3OPyjq9IKBdwNxVZGr8RvoLIGegQFRshRrVqMPReZsyG3eBSxjDskUxBaWl4ddAu54WrjS1QEsRnuGmqRFwTfBMD8LbMOafsLp5WL3_AAC2Qw0kgwWC2IefM5jiz9HctIIsn3hD8u2nojsmR814HIb7o17qiskD4b7-eIkdqxCHh9B5rpcILFna5SXm-WIDKgD5Ngotclq5u3jLve_xgmcywBHRta5RZak_zuf4W0pFlXqbG0W70Obs2qu9JNS315INEyVWKkngCO6DH8HVxLcIABBIw0AEo1hksiHn1wFQBsd8Ot3ySOxK5Eho3D33T7ermZYBLduuewgYBUiI0Xem_bW7FzxDqoQpZ7QooMFQQ1_qBZXxD42AwfHYl97BJTqUFXLlLIDcRmALMChMeRF2pUe4Z_VNOiHWOkUmOpmDFvK_EOZaCvpCIOHMDBEs072VRoi6f4-z91buoIrhYk1IkoYae8fYAryL10OBKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88cb1429ff.mp4?token=Nr2u4JiYij3OfcxvMLoTUANnyxhpQ61MZv36Gm95maYS82nXW24I3HgGHvN3mq7tHYnoFGjOC5I3pi0SwzvIcANcpb3m9f_0T0Z-r8kfPb1rz6lKyrz7CvfAzG43El55QfzyPUYuO1zYGNlK11bOGMs7FDlJcNVFe44fhdvNONHoXdSapnFSrH7-zQphSdL0zo3OPyjq9IKBdwNxVZGr8RvoLIGegQFRshRrVqMPReZsyG3eBSxjDskUxBaWl4ddAu54WrjS1QEsRnuGmqRFwTfBMD8LbMOafsLp5WL3_AAC2Qw0kgwWC2IefM5jiz9HctIIsn3hD8u2nojsmR814HIb7o17qiskD4b7-eIkdqxCHh9B5rpcILFna5SXm-WIDKgD5Ngotclq5u3jLve_xgmcywBHRta5RZak_zuf4W0pFlXqbG0W70Obs2qu9JNS315INEyVWKkngCO6DH8HVxLcIABBIw0AEo1hksiHn1wFQBsd8Ot3ySOxK5Eho3D33T7ermZYBLduuewgYBUiI0Xem_bW7FzxDqoQpZ7QooMFQQ1_qBZXxD42AwfHYl97BJTqUFXLlLIDcRmALMChMeRF2pUe4Z_VNOiHWOkUmOpmDFvK_EOZaCvpCIOHMDBEs072VRoi6f4-z91buoIrhYk1IkoYae8fYAryL10OBKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکات بسنت کیست؟ / او حالا بزرگترین دشمن ایران شده است
🔹
وزیر خزانه‌داری آمریکا پیشینه‌ای دارد که شنیدن آن حیرت‌زده‌تان می‌کند. او حالا نقشه‌های بدی برای ما کشده
🔹
در این ویدئو با این وزیر مرموز ترامپ بیشتر اشنا شوید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/684304" target="_blank">📅 21:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">🌀
آپشن‌های نقرابی از راه رسید
قراردادهای اختیار معامله صندوق‌های نقره در بورس، با صندوق نقرابی آغاز شد. به همین بهانه‌ با دکتر امیر تقی‌خان تجریشی، رئیس هیئت‌مدیره گروه فیروزه گفت‌وگو کردیم.
این گفت‌وگو به تاثیر‌ این اقدام بورس کالا بر تغییر در سازوکار قیمت‌گذاری و داینامیک بازار، بهره‌مندی سرمایه‌گذاران از مزیت آپشن‌های نقرابی و تاثیرات این اتفاق بر بازار نقره
در ایران می‌پردازد.
🌀
افتتاح حساب بورس کالا برای آپشن
#نقرابی
😦
سامانه ایبیگو
https://firozeasia.ebgo.ir
😦
سامانه کوین‌آنلاین
https://coinonline.firouzehasia.ir
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/684303" target="_blank">📅 21:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686dca955b.mp4?token=JAQAw9Az-BMesAvALi7kGCK-sRi-xwyBj8bleMAV6WtkcAgl-joERjTYi7So8mY5qBhT1QnLs7cFcHLfVNsvP19A3hXooDX5ekK4HWohIxrzj6hkk3Bzi6c5xREZXcQpbGohbbfqPPbNw_yL0iZwLWCxQg_PTA64FkIZnFE0iDZG8BPtwj5a0SgqYcm_9GMrX-ypf8fvCyqxx8c0e_ILnu2Q-AcuJZKtX9-fbsdsGZ4AE7aa8HbJct7nPOIr-uaQL3karKkZVfYoGZ0Ivx2GWoFHksLeXJ5183ilf93fKsbEUNcyA5F-tKg2vdlvUq5I1LEoJnIJyXEgWYuxHdJjyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686dca955b.mp4?token=JAQAw9Az-BMesAvALi7kGCK-sRi-xwyBj8bleMAV6WtkcAgl-joERjTYi7So8mY5qBhT1QnLs7cFcHLfVNsvP19A3hXooDX5ekK4HWohIxrzj6hkk3Bzi6c5xREZXcQpbGohbbfqPPbNw_yL0iZwLWCxQg_PTA64FkIZnFE0iDZG8BPtwj5a0SgqYcm_9GMrX-ypf8fvCyqxx8c0e_ILnu2Q-AcuJZKtX9-fbsdsGZ4AE7aa8HbJct7nPOIr-uaQL3karKkZVfYoGZ0Ivx2GWoFHksLeXJ5183ilf93fKsbEUNcyA5F-tKg2vdlvUq5I1LEoJnIJyXEgWYuxHdJjyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج یک هواپیما از باند فرودگاه مشهد  روابط عمومی فرودگاه مشهد:
🔹
یک هواپیما در پرواز تهران به مشهد هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684302" target="_blank">📅 21:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
جمعیت ایران ۴ برابر شد اما جمعیت سالمند ۶ برابر! / تا دو دهه بعد ۳۰ درصد جمعیت ایران سالمند می‌شود
🔹
بر اساس داده‌های جمعیتی، تعداد سالمندان ایران از کمتر از ۱.۲ میلیون نفر در سال ۱۳۳۵ به بیش از ۷.۴ میلیون نفر در سال ۱۳۹۵ رسیده است. این در حالی است که جمعیت کل کشور در همین بازه زمانی کمی بیش از چهار برابر شده است.
🔹
پیش‌بینی‌ها نشان می‌دهد جمعیت ایران تا سال ۲۰۵۰ به حدود ۹۲ میلیون نفر خواهد رسید؛ اما ترکیب سنی کشور به‌طور چشمگیری تغییر می‌کند. در سناریوی باروری متوسط، حدود ۳۱ درصد جمعیت بالای ۶۰ سال و نزدیک به ۲۲ درصد بالای ۶۵ سال خواهند بود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/684301" target="_blank">📅 21:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
نجات یافتن خلبان هواپیمای برزیلی از خطر مرگ
🔹
خلبان ۲۹ ساله هواپیمای سایروس SR22 با چتر نجات باز شده نزدیک منطقه  سرا آزول در برزیل به بیرون پرید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/684300" target="_blank">📅 21:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ee27d7f3.mp4?token=JdH81zQpnlUzyoPc9R6kL2BUWoYKFq3DqPjB0Nt8hQrbXr6SrBGGmAPIfQQAuHAyMvA0AmIPOTT0g7CHq0tr79CUG2psza5n-GhmV7npvWFLhJUeTnqbq_EiQVITyg6D8GCvszAJEINWJ5_9okDeKXkoGKAeLDuhoktwT-8dwoza7T5jyE221yIrXSPPKnzJATsLt895FSiilmlvzXOgc4wOfJTNIuGW2EzAe8jCKe1kuoJ1O0y182ZAulctLzKOYHda8Mo-DJcmG-Sq-qIDpl3SNFNlG7TEDO7YXmrQ6W_rnt_O9cfx0KI83h6Ubv_zoIPkyw9qsO2WIs5nw7bzxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ee27d7f3.mp4?token=JdH81zQpnlUzyoPc9R6kL2BUWoYKFq3DqPjB0Nt8hQrbXr6SrBGGmAPIfQQAuHAyMvA0AmIPOTT0g7CHq0tr79CUG2psza5n-GhmV7npvWFLhJUeTnqbq_EiQVITyg6D8GCvszAJEINWJ5_9okDeKXkoGKAeLDuhoktwT-8dwoza7T5jyE221yIrXSPPKnzJATsLt895FSiilmlvzXOgc4wOfJTNIuGW2EzAe8jCKe1kuoJ1O0y182ZAulctLzKOYHda8Mo-DJcmG-Sq-qIDpl3SNFNlG7TEDO7YXmrQ6W_rnt_O9cfx0KI83h6Ubv_zoIPkyw9qsO2WIs5nw7bzxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرآیند جالب تبدیل کاکائو به شکلات
🍫
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/684299" target="_blank">📅 21:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3b65b95f.mp4?token=jlL8iPCquLoLumO_nAqdOOPYCH8h3tdZzCNQkJcZoj59VHhegCbfzJ4AYkAfnw7_srfm-aVEH0Sj-cE0YBWjFCMdWj5PjP5c0rgSfV0mFbcRfLBBDFOw2p36s3ldoI9b_KU-qJiYOl0vRjFbaABNytm7cqDnQu1-ENa5bKqXv5AManXPUkG1jWdCnpmFBBRjv3a1uPGPDDV1FFgq7iDCwJUG2KreKBXlCzmtdzuabXZGsWcmWZekB7EKnEUFUxSKxHIBCbtLPzKspTUPm3X57ee7dwRUujOzFXMbJiuqlEs_1u0W9dFxen5LZDqdWKL4qC70OcEVorIAenJ99X64AbUAQ1YpXGt-O8pUkvcpmKf-qk2Isj8MOjDzhOfUfmp2hyPL3Y55gX8yLHnLKCnvk9DvaBbp-SJTJ8yfO-W9pm_jEGn6bCYSkfXQ0Bz3wN5fhPkN9C3KuxLCgkAv7ruxxNcnRKggYPNTh7EAi54hVOlqPxV3o0qhzdK_mI-i3FYAZSnV9kozeEoP6CZlN6hp3ll786q3V4XPzdC-D4I6iteAovhQMvZi3AyCdZ2c6cd71TdFBx98OJdzENovNu413h4NIUmGvGjYO6b989vUOHtv5pJhpTBV5nF130vVTn8Y2Qu8iMXxew0S4bm-z-6RNgJxT5iAVtMC87AN0G2c97o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3b65b95f.mp4?token=jlL8iPCquLoLumO_nAqdOOPYCH8h3tdZzCNQkJcZoj59VHhegCbfzJ4AYkAfnw7_srfm-aVEH0Sj-cE0YBWjFCMdWj5PjP5c0rgSfV0mFbcRfLBBDFOw2p36s3ldoI9b_KU-qJiYOl0vRjFbaABNytm7cqDnQu1-ENa5bKqXv5AManXPUkG1jWdCnpmFBBRjv3a1uPGPDDV1FFgq7iDCwJUG2KreKBXlCzmtdzuabXZGsWcmWZekB7EKnEUFUxSKxHIBCbtLPzKspTUPm3X57ee7dwRUujOzFXMbJiuqlEs_1u0W9dFxen5LZDqdWKL4qC70OcEVorIAenJ99X64AbUAQ1YpXGt-O8pUkvcpmKf-qk2Isj8MOjDzhOfUfmp2hyPL3Y55gX8yLHnLKCnvk9DvaBbp-SJTJ8yfO-W9pm_jEGn6bCYSkfXQ0Bz3wN5fhPkN9C3KuxLCgkAv7ruxxNcnRKggYPNTh7EAi54hVOlqPxV3o0qhzdK_mI-i3FYAZSnV9kozeEoP6CZlN6hp3ll786q3V4XPzdC-D4I6iteAovhQMvZi3AyCdZ2c6cd71TdFBx98OJdzENovNu413h4NIUmGvGjYO6b989vUOHtv5pJhpTBV5nF130vVTn8Y2Qu8iMXxew0S4bm-z-6RNgJxT5iAVtMC87AN0G2c97o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوت حجت‌الاسلام پناهیان برای مشارکت در قربانی برای رهبر معظم انقلاب
🔹
حجت‌الاسلام پناهیان از مؤمنان خواست در طرح قربانی ۱۰ هزار دام، با نیت دفع شر دشمن صهیونی-آمریکایی، سلامتی رهبر انقلاب و تعجیل در فرج امام زمان(عج) مشارکت کنند.
🔹
با توجه به شرایط فعلی، از مؤمنان دعوت شده است هرچه سریع‌تر در این پویش مشارکت کنند و در این اقدام سهیم باشند.
🔹
تعداد گوسفند که قربانی کردید را به سامانه 30001185 ارسال کنید. اگر هم امکان جمع آوری گروهی ندارید یا به صورت مستقل قصد شرکت دارید، همین الان مبلغ مدنظر خود را به شماره شبا و کارت زیر ارسال کنید
IR400600520801137000000001
6037997950309105
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/684298" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
یغمای بزرگ در اقتصاد ایران / بازیگردانان پنهان قاچاق سوخت پشت چه کسانی سنگر گرفته‌اند؟
🔹
سوخت‌بران مرزی، مافیای قاچاق نیستند؛ آن‌ها فقط ویترین یک تجارت سازمان‌یافته‌اند. تجارتی که در آن با استفاده از خلأهای سیستمیک، کارت‌های سوخت مهاجر و بارنامه‌های صوری، بنزین و گازوئیل از قلب پالایشگاه‌ها خارج می‌شود.
🔹
در این ویدئوژورنال به لایه‌های پنهان این شبکه سر زده‌ایم تا ببینیم دزدان اصلی چطور پشت قاچاق خرد پنهان شده‌اند تا ضربه مهلکشان به اقتصاد ایران دیده نشود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/684296" target="_blank">📅 21:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای اکسیوس: زیردریایی‌های بدون سرنشین ایالات متحده تنگه هرمز را اسکن کرده و بیش از ۱۰۰ شیء مشکوک به مین را شناسایی کردند
🔹
ارتش آمریکا با شرکت‌های خصوصی برای پاکسازی یا انفجار مین‌ها قرارداد امضا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/684295" target="_blank">📅 21:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee9553dd0.mp4?token=TkzAC3jruVQaiZlrKUM7IV59xAXBJlyBY-5miVRYhePulno3J3a-9Zs-SdeIZgSzxgOPV2VKneeFtH3XWeJJTbEHGkNnBVKymVJW6vYJBRpBdmyTLwCDCF195XQUgNwPfLhmVNYCM1DDkRCk3ETmCh4S35j6mixEKktuNhLTFv2yLnvm4EY25dUo6Vlmpd0U47ynbdAgBR7EZP-mEHSc2V75iKkwsn9UqWyBhg-mBThJWvd3kN4C1fzqrBCfJrzPDwiwAhktKi1QGhiLJrSIN9vgnASmOT2Sx7gh5jHKGHRgrz9kQqX7WxeqilMMCx2pQS9NB726KKZtiYTFOeeD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee9553dd0.mp4?token=TkzAC3jruVQaiZlrKUM7IV59xAXBJlyBY-5miVRYhePulno3J3a-9Zs-SdeIZgSzxgOPV2VKneeFtH3XWeJJTbEHGkNnBVKymVJW6vYJBRpBdmyTLwCDCF195XQUgNwPfLhmVNYCM1DDkRCk3ETmCh4S35j6mixEKktuNhLTFv2yLnvm4EY25dUo6Vlmpd0U47ynbdAgBR7EZP-mEHSc2V75iKkwsn9UqWyBhg-mBThJWvd3kN4C1fzqrBCfJrzPDwiwAhktKi1QGhiLJrSIN9vgnASmOT2Sx7gh5jHKGHRgrz9kQqX7WxeqilMMCx2pQS9NB726KKZtiYTFOeeD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت از کامیون در حال حرکت در مصر
🔹
ویدئویی در شبکه‌های اجتماعی منتشر شده که نشان می‌دهد افرادی با نزدیک شدن به یک کامیون در حال حرکت با یک وانت، اقدام به سرقت کالاهای موجود در قسمت بار آن می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/684294" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎞
کلیپ ویژه| حفظ وحدت و انسجام، پشتوانه قدرت موشکی
🔰
نگاهی به مهمترین سخنان حجت‌الاسلام والمسلمین طائب در چهارمین آیین تکریم فعالان مساجد سراسر کشور
🔻
رئیس سازمان بسیج مستضعفین:
🔹
با پیوند زدن توانمندی‌های مسجد و محله، مسائل محله را احصاء و آنها را حل کنیم
🔹
چنانچه محله مسجدمحور شکل بگیرد، وحدت و انسجام ملی دوچندان شکل می‌‌شود
@basijnewsir</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/684293" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963ce9c3d.mp4?token=maPsNf9rwsAfmUtU1QTkgRufJvqrZhUVxWrd1qlGWstpIpIxNOCVKKF7ymlnUFGUs67ME7em3_zkhN5gFkMDkfN_OgwblRsOGcGe0XCEe6IJxZd1F2S73Bqrcn3A1Jc8HoYgMathy5y38Hb-xdF0cqR01qPHfd4QCOyZWF00gTJzwD6pjDDk-WaJG1oBFns7pmylkHB44nCwM66LZOjv1-RC5vxk2yycnbtU83n5aG40Hll8PsPVJWz83qm50jO96aRgPdgf-ye75u_vkMVOhMydiJmdLYgEGdHf0O-kZvAHJJvH7Fvk7SUfJt1XtBldEZo2LnkrPDy04RmCf_NFehTpepdjVIJak7EhPwxbix95DQfVmsPWjjqBqmFC-IVs9lET8PWuRZrrYcxep6PpL4ZuKf8zlZvWxgE1S1Ud3muKhXIf7bP2XgRHg_A7hsAVj_3jaSwKfdD2k92scHD0NBziuk_onR1jxJqkTDQV7DAvv0ASD7y1xxh_fx3o-Fc4ALPEoPdBBUH7k1-8cv9S5_uAK_G6ipsjym1qbeUIPNGcjQL1RjxvXNK17ZS1i4yYuZyfmwiP1hC7LZBGkVUPP_WPJ0oFws1wBjNOVhoCDxKXrZVefl68uaqR3OSR58EgcVJ4zDDosC4mxvbtI8oqkwb-IWUXJARvvv-eNMdOy_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963ce9c3d.mp4?token=maPsNf9rwsAfmUtU1QTkgRufJvqrZhUVxWrd1qlGWstpIpIxNOCVKKF7ymlnUFGUs67ME7em3_zkhN5gFkMDkfN_OgwblRsOGcGe0XCEe6IJxZd1F2S73Bqrcn3A1Jc8HoYgMathy5y38Hb-xdF0cqR01qPHfd4QCOyZWF00gTJzwD6pjDDk-WaJG1oBFns7pmylkHB44nCwM66LZOjv1-RC5vxk2yycnbtU83n5aG40Hll8PsPVJWz83qm50jO96aRgPdgf-ye75u_vkMVOhMydiJmdLYgEGdHf0O-kZvAHJJvH7Fvk7SUfJt1XtBldEZo2LnkrPDy04RmCf_NFehTpepdjVIJak7EhPwxbix95DQfVmsPWjjqBqmFC-IVs9lET8PWuRZrrYcxep6PpL4ZuKf8zlZvWxgE1S1Ud3muKhXIf7bP2XgRHg_A7hsAVj_3jaSwKfdD2k92scHD0NBziuk_onR1jxJqkTDQV7DAvv0ASD7y1xxh_fx3o-Fc4ALPEoPdBBUH7k1-8cv9S5_uAK_G6ipsjym1qbeUIPNGcjQL1RjxvXNK17ZS1i4yYuZyfmwiP1hC7LZBGkVUPP_WPJ0oFws1wBjNOVhoCDxKXrZVefl68uaqR3OSR58EgcVJ4zDDosC4mxvbtI8oqkwb-IWUXJARvvv-eNMdOy_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفوذ سایبری جبهه پشتیبانی سایبری به قلب صنایع نظامی اسرائیل؛ Novamill از کار افتاد
🔹
جبهه پشتیبانی سایبری با انتشار بیانیه‌ای از نفوذ موفقیت‌آمیز به شبکه داخلی شرکت «Novamill Systems Ltd» خبر داد و اعلام کرد که با خارج کردن تمام تجهیزات کلیدی این کارخانه از مدار، عملاً آن را از کار انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/684292" target="_blank">📅 21:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHiJbLO3IvKtEumbjIGAxz6Xvwu877t1YBA7kzmxonM2MIEWOa7xa8yUmMmtr3lJCsrJ8f_DjpH1ciH2pUoumixlbynUI8sGOBk3f3ZhpHlect5B7VceYFAaRZeKOEAASrpRPrUEr76O2KmCBX4vQe5cMJn9F62aUPQeKost-7aPfMH3gAYMLoPxvkRW4gIU9TZKC2MYKr7ZY74Mz4HrtBUl6jpWnUuVj1n_Duxy_hjhjVkpsdQWp8TUYiLuK-RvmApUUu-Cw7hkLogSyBclEEajlJIcz561ALPfHy9WT6i33qy6Ogb-wcQzWrUtOnV3MMTex-eGorVuMHYYkiPINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد:
🔹
یک هواپیما در پرواز تهران به مشهد هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684290" target="_blank">📅 21:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای قرقاش: حمله ایران به کشورهای عربی حاشیهٔ خلیج فارس به هدف خود نخورد
نشنال امارات:
🔹
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات مدعی شد که حملات به کشورهای عربی حاشیهٔ خلیج فارس «تنها بر معضل» ایران افزود. او گفت که بار دیگر تأکید می‌کنیم که تجاوز ایران به کشورهای عربی حاشیهٔ خلیج فارس به هدف خود نخورد.
🔹
قرقاش مدعی شده که این تجاوز، معضل تهران را عمیق‌تر کرد، یک محاسبهٔ استراتژیک اشتباه بزرگ بود، و موقعیت آن را بیش از پیش منزوی و تضعیف نمود!/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/684289" target="_blank">📅 21:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684288">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cf219f41.mp4?token=pD2L8eWeanY2O3rq3vJ_qCYM23CkR44P9-Mqp7KUKa_L4exlqL_qYSakSpG6GHyM1VKzki6vo9BbCEfEXwcirjrM4EdUUqi9zXWX6tXXynVJOAETgAzH1mcxSScghLvPbUh5-RqZbr-jwej3n3QNE0BmP1dLS_Wm8uu92Kdh5tFN3J9AJJBJGeg12XG1hcGS_Yx-G-PYVilyQPOSTWZxGLweViOjJy59cwbMykONHkg0IoDzfGJ6mM-2_aX7DtQ_pryF6YHsQmTj3gq6OUPoGWe_Lz3mbE9xTD5rxBTVDW_dAQsXESK-4aYPMXV8La7SBBKf87e4A7qPl6eZWkKJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cf219f41.mp4?token=pD2L8eWeanY2O3rq3vJ_qCYM23CkR44P9-Mqp7KUKa_L4exlqL_qYSakSpG6GHyM1VKzki6vo9BbCEfEXwcirjrM4EdUUqi9zXWX6tXXynVJOAETgAzH1mcxSScghLvPbUh5-RqZbr-jwej3n3QNE0BmP1dLS_Wm8uu92Kdh5tFN3J9AJJBJGeg12XG1hcGS_Yx-G-PYVilyQPOSTWZxGLweViOjJy59cwbMykONHkg0IoDzfGJ6mM-2_aX7DtQ_pryF6YHsQmTj3gq6OUPoGWe_Lz3mbE9xTD5rxBTVDW_dAQsXESK-4aYPMXV8La7SBBKf87e4A7qPl6eZWkKJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایده‌ای دارید، اما توضیح دادنش به هوش‌مصنوعی با متن سخته با ابزارِ Squig می‌تونید خیلی سریع یک طرح اولیه از ایده‌تون بکشید و همون رو به هوش مصنوعی بدید تا بهتر متوجه منظور شما بشه
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/684288" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684287">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcba318382.mp4?token=pGcF-0q_VauP5VZlDINCoBPhWQvM3URsV8pGoZIXZmAU_DZptfdm-ydjLEaIR4lwMeiTaQnEXoYK7IgV5sgLwD_Q7ECs5Y-5qr3yY37oE--Mk-K3Lkbh3t4e8lpvU-gMuF28x8TJ4lVKgTJ6da5Cz4---4n6REDv0CsllSGhiQtEx32Ey3c7ga4g5IhHMgQJS4Qn3hUXMpqTFNA3beW4Pj9YnSsWAcrXlDXVsUg-GG-SHC8hwq7jiOdVDhTLxoputXvL09IlgP1t78tBU-NsjLaB8O58DHG8IVwGn02kV8h-xUEUvkFTZJYv3gZfF47xWDaFeReEHzX4TU7CpHZNrmhW4czF4XxQqvoEsRs6OM2jRf_NOmraS2EAOf3FAUj9rLrKldzWkhsvqtqJ0wxV4mkYnqUTB07KbD6BOiokesrrtr1GnUFgUa1F26l6BG_ZWYFNg0jxHWVHFHNTBzgnjYmrZN4EibzEqruz8L0OnGkmNBTfNonE5KENj2dQnyOvDmsbBE7u2YQJfSEoYLC39aR0rfe9hJauUngLGsjkDxI-pJMI8zFQ8QjjWxaZUFAppgx3dtnaJC0m6kHFl6wVBe-uiNmPW2SZuWoZn-43cQi0yE3ORkmmldP6hwFLelJyeftb_2i76C38ZB1WmsZ4JbsBVM_P9fwg_6lna8bzOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcba318382.mp4?token=pGcF-0q_VauP5VZlDINCoBPhWQvM3URsV8pGoZIXZmAU_DZptfdm-ydjLEaIR4lwMeiTaQnEXoYK7IgV5sgLwD_Q7ECs5Y-5qr3yY37oE--Mk-K3Lkbh3t4e8lpvU-gMuF28x8TJ4lVKgTJ6da5Cz4---4n6REDv0CsllSGhiQtEx32Ey3c7ga4g5IhHMgQJS4Qn3hUXMpqTFNA3beW4Pj9YnSsWAcrXlDXVsUg-GG-SHC8hwq7jiOdVDhTLxoputXvL09IlgP1t78tBU-NsjLaB8O58DHG8IVwGn02kV8h-xUEUvkFTZJYv3gZfF47xWDaFeReEHzX4TU7CpHZNrmhW4czF4XxQqvoEsRs6OM2jRf_NOmraS2EAOf3FAUj9rLrKldzWkhsvqtqJ0wxV4mkYnqUTB07KbD6BOiokesrrtr1GnUFgUa1F26l6BG_ZWYFNg0jxHWVHFHNTBzgnjYmrZN4EibzEqruz8L0OnGkmNBTfNonE5KENj2dQnyOvDmsbBE7u2YQJfSEoYLC39aR0rfe9hJauUngLGsjkDxI-pJMI8zFQ8QjjWxaZUFAppgx3dtnaJC0m6kHFl6wVBe-uiNmPW2SZuWoZn-43cQi0yE3ORkmmldP6hwFLelJyeftb_2i76C38ZB1WmsZ4JbsBVM_P9fwg_6lna8bzOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماموریت جدید بابک زنجانی و دات‌وان در جنوب؛ تحول آبادان و خرمشهر یا...؟
🔹
این‌بار صحبت از هوشمندسازی حمل‌ونقل و ماندگار کردن گردشگران در منطقه آزاد اروند است. در این ویدئو خواهید دید دات‌وان دقیقاً چه نقشی در آینده اقتصادی خوزستان خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684287" target="_blank">📅 21:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684286">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5raGA17JMh_b3gXB25J0ADnV3UFRjtoobYRxdTZUkHQmadV0d2hqDUmB5iVHcLhXdj73ZKlFZrnwpFFMbHqG57sq1uJjDWu7OCkYDZzd0ralkGdaq7WywfPfBhTHuXpC8WmjcMyQoi1-bQBBcesaGe_EaOU3qIq_aP1r0qCIkOcSxIf_bu1KX8dM9bkc4C5R5vjpQ3UxB9M8XoMKhq-LVkHAJKhT8ioVfnCMAYxxKjOxRUJfhVhuyVeug9YpH7VVHz-ng_VzNeKAdklMazLdnfsn4kwuobO1Rb9uuMJQb-2o_ggwrf8ojKCdsAo7jGMYxlwGh9zASWE1-i-Jda-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/684286" target="_blank">📅 21:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684283">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdtPZo_wDQQMXa1M7KVLL3ql6AiwBk7J1xhRSuqjsNUJyHR2JnhzSdu3PX-_J1DvO1hqqvUgk2LX-HeHJhaJkLBww4wYxFZOXHPPh39fEPagtZW13-VXEJ3kg0ICCOlHo-nxhMxnxV4uxzOypCUBtXYijovquc-mvMAcQYqfo8iT5kD6AcAgZrXy6HvCmGyWF6kaht5vo8BO23NBk6ZxtvkuBo-K0HUQeL29se4BRsVPrg2cfoQmggJ6-6GIZ7CM09X0hwDbBpRhTGDUL8pBvS7WYzfuDrEbtZbWxkr3BgZE7JAZMWQ1hTyXDiLhPxD2pIOLtK1HLFrI7gMYnZoBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلغارستان: ایران یک عملیات بسیار موفق جنگ ترکیبی علیه ما انجام داد
ادعای خبرگزاری BTA بلغارستان:
🔹
وزیر دفاع بلغارستان، از سیاستمداران این کشور خواست هنگام اظهارنظر درباره اظهارات و مواضع مطرح‌شده از سوی ایران، مسئولیت‌پذیری بسیار بیشتری از خود نشان دهند.
🔹
ایران یک عملیات بسیار موفق جنگ ترکیبی انجام داد که متأسفانه با کمک سیاستمداران بلغارستانی همراه بود. متأسفانه، این عملیات جنگ ترکیبی ادامه خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/684283" target="_blank">📅 20:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684280">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXFtJ6Tf2VD1rS4XsLhmlsIU-7dEfTh-kzV6Yeq5EoIctyz2ylR3-WNerJ6CKl1RUIl5Voy7bIgbJBlCK6YLSx02j9WJmjs7sa62rz3kClmr1eDlyuouM8cMldbnLTSa-xt-TUF6O32Ios0Mu16GiJbOMY-FL-UqvIPf-vfSwRwKPKXoaLSJRo6-KkFt_btyxR_9JTOFmSW_yMt-WEFE_VR_hGJ_hO4wGNCSoCn4E8QiSu5g8uJb8Y86bKyaR3Rjdq_Two_2nNDXep4jb3cYQjbJAao6kjDRwrEM_AvrTZBcKl1-FvaUhvs0lIKjOT2gXrmGFrCCt-Tm6ByVaToi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد ۴۰ برابری پزشکان زن ایران طی چهار دهه
🔸
طی ۴ دهه اخیر، شمار پزشکان زن در ایران رشد چشمگیر و ۴۰ برابری داشته است. تعداد پزشکان متخصص زن از ۷۷۴ نفر در اواخر دهه ۵۰، به ۳۰ هزار نفر رسیده است.
🔸
همچنین آمارهای فوق‌تخصص نشان می‌دهد این آمار از ۳ نفر به ۱,۵۰۰ نفر جهش یافته است.
🔸
این رشد در حالی رخ داده که جمعیت کشور در این مدت از ۳۶ به ۸۷ میلیون نفر رسیده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684280" target="_blank">📅 20:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684279">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سخنگوی دولت: سهمیه بنزین با نرخ‌های ۱۵۰۰ و ۳۰۰۰ تومان بدون تغییر حفظ خواهد شد
🔹
تاکنون هیچ تصمیمی برای افزایش قیمت بنزین گرفته نشده است؛ هرگونه اصلاح ساختاری نیز با رویکردی تدریجی، شیب ملایم و بدون واردکردن تکانه به زندگی و معیشت مردم انجام می‌شود.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/684279" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e43cd1c9.mp4?token=RMCm8VvMfC-OiPOTyoW-ExfJ9vcvg7JWH1KyD9doGh7ghrNGIPfXS4RobDwKgo3aNC2KGdT_HrMVfI6mItvYsdlSYXX_NpkbOgPt1J1-gt136NEor8jF-5m-EPd6olyn5lP5Qn-bPnXVoQxrz-2rUwtYbR_mOnDhnt97NRTCQw3O5Gw9Nbjno3QXFq0uuH1PanQXvSUVorKLvgywjUsNQObdT_4Ktzhe0D10VwcsyYHHY6kJ2ixDRJkZZ5Ij4ubPejdNlp-u2dY2Pzrg-s5W5EyCewqQxJ0vEuYijF92K5DyurHfkQrk5Nv4Fhuo_BvMj7P60HiQk0K94ociOp4kDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e43cd1c9.mp4?token=RMCm8VvMfC-OiPOTyoW-ExfJ9vcvg7JWH1KyD9doGh7ghrNGIPfXS4RobDwKgo3aNC2KGdT_HrMVfI6mItvYsdlSYXX_NpkbOgPt1J1-gt136NEor8jF-5m-EPd6olyn5lP5Qn-bPnXVoQxrz-2rUwtYbR_mOnDhnt97NRTCQw3O5Gw9Nbjno3QXFq0uuH1PanQXvSUVorKLvgywjUsNQObdT_4Ktzhe0D10VwcsyYHHY6kJ2ixDRJkZZ5Ij4ubPejdNlp-u2dY2Pzrg-s5W5EyCewqQxJ0vEuYijF92K5DyurHfkQrk5Nv4Fhuo_BvMj7P60HiQk0K94ociOp4kDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: صداقت پزشکیان و اعتماد مردم به او باعث شد این ۲ سال سخت را پشت سر بگذاریم
🔹
از ماه اول دولت، افزایش ذخایر کالاهای اساسی را دنبال کردیم که باعث تاب‌آوری در جنگ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/684275" target="_blank">📅 20:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbCo_AfqGjInnpihShw2vTslQ8BQrjeZAQagALb-TBlMrx8joajk-iBcK2wDL5Ya3ny_XuZhLigT35PP5Nrvk0G5vZ9hqEhpkvrUNtYPGOAx0Ilk0D5NcL7K5kOrhsY5dNcWXnx37GLAQOv2O1sHRXqKyz5VcVHJx30InIW2PG8yl0uQZ5tB3F-DUtq6G1Xj7Vz3FXDi7XyPxOBN8I6QGQQ70VSLVU3S_tSKSFZwG5WB3yJ3hrcWN-YBGppAFCHV0iSHCZhnEyBKnIvN1lc9cg5pBxKb7Ft06Pv4Az0ZTSqIpVAys11R6p6FgHpQiHzpn0ZKJ6fhszar5olJRgdiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای تلخ پسری که اخته شد و به عقد امپراتور سفاک درآمد
🔹
اسپوروس یکی از آن افرادی است که تلخ ترین سرنوشت را در تاریخ بشر داشته است؛ سرنوشت تلخی که قلب هر شنونده ای را به درد می آورد و سبب تالم همگان می شود.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3240346</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684274" target="_blank">📅 20:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نتایج اولیه آزمون کارشناسی ارشد ۱۴۰۵ منتشر شد
🔹
داوطلبان با مراجعه به وبگاه سازمان سنجش و وارد کردن اطلاعات خود، از نتایج مطلع شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684272" target="_blank">📅 20:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684271">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqRJturpT_T2FwNsY-W8X_smWuSGKOI8AbWGIPSFX35PnHqenCpSZkRWbVCE1oJ-i5xwQNWgI9b-rL10gKY_hlY0bsYgNz5kUkBmhRmL5UbZsv_RBnKwxPqJbzx_MYpjr5w_wxbNCaJwWLnc5ccDG2jJ41L80B9Fp92M555xLcYdX5q7Yn4Pf1THKQX6cD2GVRp_0RhmTptk2eh11CHuWZ3TcN_334kGf-MBMEpBQG2FYeELOonbx86g-NWdl1l_gPjv8EFSGWzd22-5qMyePvQy19Ace0aNol1zvkHuF9hvEysvozyxGJ12icNUOtIp6CdfHLMiEld2-azBFPSL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکزاد: قیمت بنزین افزایش نمی‌یابد  نایب رئیس مجلس:
🔹
مقرر شد سهمیه ۶۰ لیتر با نرخ ۱۵۰۰ تومان محفوظ بماند، سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا کند و سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان نیز به ۱۵ لیتر برسد.
🔹
نباید برخی افراد بدون هماهنگی،…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/684271" target="_blank">📅 20:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684270">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_GUZo-NfEKI-59veiuvVl6bjbIA1-ppl7fXMsy77fcxaW-EBysgRE6KsZMyfSCgWEPfYOxw_MmT-MMNuJiesuNXtwXaobHYRMuPPEsiBBulIBfc5wUz1tyGjHFKjxYNv8HxfqLdlHv5URbEo_jgrpiqAIrmvZdKE3gj_c1ibQ0xRkEc4oQWMNNudHJA_WMU0tZctJWuvLgcCMhu4mgFATjAF3gHjuOVSPRHpNRvCJTbDKZZrFWtZFFkO3pJJHdcQO92c1arDocYLupKU5AyRJN-zio1Jvh91ea40SL9x7LE1Pb6pER__-40h2-bIoIIVZhvTjK4jiHS78BS8yZ-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت به پاکستان
🔹
آمریکا در بحبوحه جوسازی برای تشدید فشار اقتصادی دوباره به پاکستان و عاصم منیر رو آورد تا منیر بعد از پیغام و پسغام برای درخواست بازگشت ایران به میز مذاکره در سفر تهران، به پاکستان برگردد. رسانه‌ها در گمانه‌زنی‌های خود از احتمال بازگشت آمریکا و ایران به توافق اسلام آباد خبر می‌دهند.
🔹
هشتصدوچهل‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/684270" target="_blank">📅 20:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684269">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">04 Ane Manaee (1403-08-03) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه چهارم
حجت‌الاسلام امینی‌خواه:
🔹
دوازده تقابل بی‌نظیر در سوره مبارکه محمد؛ مرزبندی ایمان و کفر! [2:01]
🔹
طلوع نابودی در قله پیروزی: سنت الهی در انتقام از زورگویان [9:15]
🔹
جان‌سوز اما جان‌نواز؛ وقتی زنان و کودکان هم طعم شیرین شهادت و جهاد را می‌چشند [11:58]
🔹
وعده شهیدسیدحسن نصراالله: اسرائیل به ۸۰ سالگی نخواهد رسید! [18:38]
🔹
از شهید آرمان و حججی تا یحیی‌السنوار؛ خداوند قهرمانانش را به دست دشمن معرفی می‌کند [24:31]
🔹
دشمن احمق ما را تهدید می‌کند؛ ما در انتظار لحظه رویارویی هستیم [27:58]
🔹
حق، مانا و باطل، میرا است؛ زندگی بر مدار قرآن موجب ماندگاری است [36:06]
🔹
نقطه تمرکز دشمن، قلب آرامش یاران؛ رهبر معظم انقلاب، ایستاده در خط مقدم [47:08]
🔹
پوچ‌های فریبنده، گل‌های ساده؛ آزمون واقعیت و جذابیت [50:35]
🔹
از قیام حسینی تا سکوت صهیونیستی؛ شیعه واقعی کیست؟ [1:21:51]
🔹
نازدانه‌ای در ویرانه شام؛ نامی که جاودانه شد و ظلمی که نابود شد [1:30:18]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684269" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684268">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b8679b56.mp4?token=WYNncPdCmwfL23yUgL54FIoODYFDpvYiFRqLgY--8cNyWGrRMgn-W4hgvEV8fLEifBtCMMhYJdYUZnQlTCJTH5U1bQHvmpEprUsS_xN9tXOmwLna-9lNJCz_kuAysYZnnvYzg3vm7vFXhqwLywk5ZDfQ9no_7o92Q0Fhlvffi8Qlr5wKomJaxvq_nDOdpOZ3lFqbx6g7Cl2xATb8FPHzGwtRdZToUJsZK2a63iGViBa3F8AGnhmAeYOVF2gK_Qk4aj_s9WgNQWWcBadhhWvap8FljJ-KsKzbUsx0PpAcbDgubc2mesY71I-wti97LdfrpErB1ugqi37I_QzOEAiKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b8679b56.mp4?token=WYNncPdCmwfL23yUgL54FIoODYFDpvYiFRqLgY--8cNyWGrRMgn-W4hgvEV8fLEifBtCMMhYJdYUZnQlTCJTH5U1bQHvmpEprUsS_xN9tXOmwLna-9lNJCz_kuAysYZnnvYzg3vm7vFXhqwLywk5ZDfQ9no_7o92Q0Fhlvffi8Qlr5wKomJaxvq_nDOdpOZ3lFqbx6g7Cl2xATb8FPHzGwtRdZToUJsZK2a63iGViBa3F8AGnhmAeYOVF2gK_Qk4aj_s9WgNQWWcBadhhWvap8FljJ-KsKzbUsx0PpAcbDgubc2mesY71I-wti97LdfrpErB1ugqi37I_QzOEAiKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند، پوست سیب‌زمینی آبپز رو یک‌ دقیقه‌ای جدا کنید!
🥔
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684268" target="_blank">📅 20:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684267">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
جلوی واگذاری اموال بازنشستگان را بگیرید!
🔹
محمدعلی شهابی روزنامه نگار و کارشناس حوزه تأمین اجتماعی اژ از تصمیمی عجیب توسط مدیران وزارت رفاه و تامین اجتماعی خبر داد که گفته می‌شود صرفا به دلیل انجام قولی است که احمد میدری در مصاحبه تلویزیونی خود داده بود.
🔹
شهابی در کانال شخصی خود نوشته است:
سازمان تامین‌اجتماعی برای ضمانت خط اعتباری ۴۱ همتی بانک‌رفاه بابت پرداخت یک‌ماه از معوقه‌های حقوق مستمری بگیران، سرانجام این املاک را برای تضمین، صورتجلسه کرد:
🔹
۱۵هکتار زمین در شهر پردیس به ارزش تقریبی ۵همت، زمینی به ارزش ۶همت در مجاورت سازمان حج‌وزیارت، دهکده گردشگری انزلی و‌هتلهای هما؛ تمامی این املاک با قیمتهای پایین‌تر محاسبه شده است؛ ناتوانی در دریافت مطالبات این سازمان از دولت و یا خط اعتباری از بانک‌مرکزی، کاملا مشهود است. این بدعت خطرناکی است و از این به بعد و با این اتفاق، دولت دیگر هیچ بدهی را پرداخت نخواهد کرد و بانک هم پس از مدتی آنها را تهاتر خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684267" target="_blank">📅 20:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684265">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBewE93Spbbp64NpDMudUcBMKFLiL5RgV1FEnntvjp-zTHB0dWgW_j0mukN3j772eUe8ejxO7qrMGJ9B7l7R_w86tzi0HLXCmOcIMFPBREebcJIVkr-_oQL3EzPU658XK7kdA_qN9Y3KlP12y44bm1KogM1wo9DUBRPI42-nKsXml46NPUVz2O6KBzMdBtGKdnZdf60nZQ_ENT8qoS9DJSIKSUmuIEXVH4zdjMk-LRPus3WvEekOidu2qvsJs7-Ll1QYCV6MnnoTBX62pBFppgHBAdgi2VyoQbHRpCfx64clk_I_FGgKhtM37aJ1MHjbH_1PQ6vTklMgbrg0VK4CEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرزپاتاید؛ بخشی از مسیر مدیریت وزن در اروپا
🇪🇺
مونجارو (Mounjaro) با ماده مؤثره
تیرزپاتاید
، در اتحادیه اروپا برای مدیریت وزن در بزرگسالان واجد شرایط مجوز دارد؛ البته در کنار رژیم غذایی کم‌کالری و افزایش فعالیت بدنی.
براساس اعلام آژانس دارویی اروپا، این مجوز برای افراد مبتلا به چاقی(BMI بالای ۳۰) یا افراد دارای اضافه‌وزن(BMI بالای ۲۷) همراه با حداقل یک عارضه مرتبط با وزن صادر شده است.
این موضوع نشان می‌دهد درمان چاقی با آمپول لاغری، بخشی از یک مسیر پزشکی و مبتنی بر ارزیابی شرایط فرد است.
در ایران هم تیرزپاتاید با نام
زیکورپا (ZCorpa)
، محصول
داروسازی دکتر عبیدی
، در دسترس است.
⚠️
مصرف این دارو باید با تجویز پزشک و همراه با اصلاح سبک زندگی باشد.
🔗
منبع:
آژانس دارویی اروپا؛ Mounjaro</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/684265" target="_blank">📅 20:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد:
🔹
آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/684264" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نتایج اولیه آزمون کارشناسی ارشد ۱۴۰۵ منتشر شد
🔹
داوطلبان با مراجعه به وبگاه سازمان سنجش و وارد کردن اطلاعات خود، از نتایج مطلع شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/684261" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsJXuHHZbYknsV5aC0UROsQybFWuTX-7cnpHpiE2nIIuf91OTsQtL401mIWX1D_uAV3Hh9H_-QKzhzXJv1uvbLVxVQ6vDQ_OEahKQzVld06B59IwwyofPMCxfzyVcVe7osmpLL1fZpqX1qSHjR4eubuzunyznecRnQxz5p3NOwgSHO9WeDb28QYNenrJgZzMA1NzEfCiTWxcedDGZHtVw5ax89tLeKMUOMMZmVAiOX4Z0CQa6aqOWFN4AIdeoVSIeqxtHhD67-I3s7ib1s5dmvifNxRIwmWi2MZA5l8JO3J8Fp09tW3UP2Jb9eozqxKf9SxYu36szgMTuOIUiCPOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و عمان بر تداوم همکاری برای امنیت تنگه هرمز تأکید کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/684257" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZz8tDD6Qizdp397pV1JrAq7530v8wfQOgQUCllfs39TUFIWleR5nFWOtwPcZasCKE98LW4qCvCbM7OEgrgkmTf4UjykLFPmfc-EZwbrcqDb7iR-K2XVg4hxK4-OxcAfyxGh5XBbJF9_NNRq3ZQ6NUI7rnjAWII4jNh1dlN6WrXs1j-0XYNnBCSj7yqRJyesFXxnPjqrYeNiDSQlddw_FFp5MuObOUMX-TpXD2QopLp9ZJXOPxbufHkJaZIlC9CJ8SZLNPbSVnY4bmnSrMAX3WQ7IiFP_SWVXUhziuTt5-aPpcMa1Xl0bMBRSnZxQippaGvLNXm1uwVSIXbz_KvwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ما از طریق نیروی فضایی، تنگهٔ هرمز، کوه‌کلنگ و ۳ سایت هسته‌ای ایران را زیر نظر داریم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/684256" target="_blank">📅 18:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzKMZOPZ3TgqL99yR_TjnkNJLH2m8-CXwfASXr3T5cLOrQ4e5SyUczMaR95xjpmIKvZlTNc_rlvdjhohKVHrbin-qQlHS3izSm5IWczGKHeK2ssfZb7W8NafutR8rcnytjdeHTfiHMUCoPcgS7xxEnruW0xi3VwNT_thp-SEcGyVnI_wBeWuBdMleIMSAENb2qre7nsdhY-82hSInoBEv4cCCejZm5ceMCmDmxXLeomvcTug-uNLD1mwJRwpgNlO-tJQVDB2045mLV1WD2HtP1J4cfeLtuSx8Af_P1twxd6--J2KVQlojzV0WJektUIdexINAPImWfcS4eAcUnL9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جلسه ۷ ساعته رئیس‌جمهور با رهبر انقلاب
چه گذشت؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684255" target="_blank">📅 18:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684254">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تاریخ نشان داده است که تلاش علیه ایران دقیقاً نتیجه‌ عکس خواهد داشت
الجزیره انگلیسی:
🔹
لورنزو کامل، استاد تاریخ در دانشگاه تورین ایتالیا گفت: تاریخ به ما می‌گوید که تلاش برای منزوی کردن ایران دقیقاً نتیجه‌ای عکس خواهد داشت.
🔹
آنچه این جنگ نشان داده این است که آمریکا به شدت تحت تأثیر اسرائیل قرار دارد و بنیامین نتانیاهو، نخست‌وزیر رژیم اسرائیل هرگز به آمریکا اجازه نخواهد داد که به توافقی دست یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/684254" target="_blank">📅 18:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hs2E4wGSNA_wk8CbpEXg3G99x8W9Ubjp94Fi7yjIVBdDJjFw3x4rFUh3UuERToUGSP1CMK08N-tL18uAQorVpkW96lV13v9Z7CJMsT1R74x5LuLYyG5DLaButIPvtmpaZnbLyMhbdGAAPPbyl-LYUkJxM60siYwjlRH8paHecGAhkhdzddQag3jtMn1DzzLebeyOor7Sa7N-gHGC5rWQckZatI4ucOuLInVVL2REIbIngHGJHClR48kb4ICYs162mrC0UU3VL3k-1S5FBI9JIvjwrvdq1JZlJH0G18blBR-O2D25SHrNnCYJMuiIfnR1E-L8nwLYmf5Fm8kFCGwk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USrL69gO4I3e-e0ICBwrZsEmu-A5BGTEUKnbklaQPBkmaRHRUh9FnQMJb_9gpH15yDP6AUiynpFO5X6cmeRTsoi7nR-JBjRCaAS8mjv4Kk3w7sbL7gpQidARBoHQSqSWrr-zR6Kg4wEUvY4GQnI2Fl2yBKgoFhxVXWtQPZy2qJF5Ovnx2QkgWRllXVBhCXhFPuHNvVU5E59Y0yzDzrOTO15tHdN0mh8OaCjAE89GrhGkjrKBw7DHWJfUzh5xQhDe1VL54aVKFe6YsDurvLaHCcoJim-K_Fk2_c3l_Q_cvNBue_RxwjGvf6ZZ2r7rEOSWXJkUuGHS5eEcPR_ESG_y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLVG6J4mRFp5tvCw54aJ-70lnZ_4GS8xThSxlLbpMojH-RCcb2NbKnhad3PqdmHC7cGgpMmBAGSDn0FrXBZkfKpep3f_H3W3XzWvo0LGCH861M4kmA5nChISGVsBYfuzr3yrQmR7zZk_tUwB7p-M9fBSv0hDYc6aZh5Dx8glqDYG18dkmpmnSe9IuYvit5HbqJ1jniZqC7ng4GAct-Mq2WDU1SFcld2dV7cYUcMkit-zkFxfzIefDxAR0-v33F-mB7xi4N88uFV6ut8OOoF3Xeymh2jjrlqmPrdOwQj4FrkFo7p9yEWX90Ntm9aoQIklmFqfaMV1puyCNI2luoW4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHRv4m4V9ygbWyW_x5sCDQf6uEPgnBxPe6rIEMfQ_37f1SVoIpfrOnrMFWdCGIkgi9xvauyOZC4P6pdQeuv6-tKWM0l2lR_CkyalMMMk6zmRHHU1iarIsjfbEKt8jEAFnFQzKJx_b_VsByCwzoeYbN0EGlD9OqgbZvERAyUpVd3QjNfwSik1kJGq8jGutIuTKpVh9W-gpP-1gQop3vGHT7BqKL9wAkxtwTZpRa1DMGMAHkvD1R8YBHXZL0W2s7xRYZBdmLGZwEK-EW_rvvD6JNALzW0dU9aFoCopqLew-bD3hpTgXUNxlw8Q-nudPztU7XPAnT9Zxh6415pa02yfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6PkBPha4_UBz4G8G8p-9pDbS7DZ-fide7iWnzRggjJofToh0napo-NVuiIVaIvL-n-s4VStwOiFtrsLQiNXaVxhaLwUic17tK8g5Kf6Q3mRQF2VJllMWQk5LcJkxkWgvhaoILryhy_bjfbpCLJNWrpRf5xefZA1sEfUGqxDyiKdaGXj6k3kqzvAXUdo5IRWyCpEQTCm12EIcY-MCaG-NvNO_br3P2-XSr663AGV2dfNJpg2UjkwC9xlT6EvmuJkY0fqiYdy5dOnWdZaUpMr369GNAykrLti4syEIvmwHuOEn3PnqkXzVyWQm1w-gktYcUSUtxEovwyqEDlXyk1iTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgTIXw2s8A2CWqBPlJrQzJx10qMYjLzH4v6AIU5aS3uYwsREumBtt6Al9CyYkJFsrd0rIf_h8714cW1sYwGpH_zr-ZFXrGAO-UFashgoB-r_kuS5hlfAY38L3Ed13j4Rng_cZ7Dtpox85iIMsrUePHoIu3yUlfABKfempemTWrIQXLYu0k-erF58pLCIyxZeQy2hAxp4e8YggoLMlbnbqFFnjcUb2oU592K1Z1Kx8Cki3_cnuDJTk34dd3TTC9PvXFKcIlknzU334lU9a2kcnbnCyECKmGVQ1xdrG0W7pvg6FoPuPOcNwHU7wGgGFnkDgHWZCrf0K-p4cuKvgnhsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۶ مدل خمیر در کاربرد که خیلی به کار میاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684248" target="_blank">📅 18:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZzFyLw7-Am2yzxd8ebj04aZ5yRK4Z_hyxaT3CLU_n1zD0e2amaUyH8CXX8rhuXo5ZX92-IyOcG3Qk7yhvpVPgubKQIv8kGdc-MVXR2u6fF3bAIur50nEVlYjf6vUo_DRvmQfuK3dsz963lw6-FE-qEBiBUgjm3-0vkPO4_60I2eOp-HVCzax1UWO2WzDIukmh3T10csdEvaNERwlnvGFWf0nlOiqxPtqsFvVIi8O69E6lJbl6ZyK7H9gmvIX3ytBGopl1ahySFtM8aDDLknU5Snd70tG_AE9j30Lqg7jtWqkxYiSjiBgoUST_YgoUgx9J6_1una1OrDBNbpZEcZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
♦️
عارف: تنگۀ هرمز ملک ایران و متعلق به ایران است
معاون اول رئیس‌جمهور:
🔹
نباید اجازه داد افرادی که حقوق دیگران را نمی‌شناسند یا همه چیز را با تفسیر خودشان معنا می‌کنند، درباره حقوق ملت ایران تصمیم بگیرند؛ این همان چیزی است که در فرهنگ غرب شاهد آن هستیم.
🔹
مردم از ما دفاع می‌خواهند؛ دفاع از ایران، دفاع از نظام، دفاع از ناموس، حیثیت و منزلت خود و همچنین نشان دادن اقتدار کشور. این یک راهبرد جدی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/684247" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
پزشکیان: امضای توافقنامه از روی منطق و آگاهی بود نه از روی وادادگی
🔹
تصمیمی که در شورای امنیت اتخاذ شد، مبتنی بر خرد جمعی و تعامل میان سران قوا، نیروهای نظامی و سایر بخش‌ها بود. اکثریت با در نظر گرفتن اصل حکمت، عزت و مصلحت، توافقنامه را پذیرفتند.
🔹
هیچ یک از افراد وا ندادند، چرا که همه آنها توانستند جنگ را اداره کنند و در برابر قدرت قاهر اتمی جهان ایستادند. بنابراین امضای توافقنامه از روی ترس و وادادگی نبود، بلکه بر اساس منطق و آگاهی شکل گرفت، اما عده‌ای کنار گود نشسته‌اند و مطالب نادرستی را مطرح می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/684246" target="_blank">📅 18:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ترامپ: کره‌جنوبی حاضر نشد در خلع سلاح هسته‌ای ایران به ما بپیوندد.
🔹
کاخ سفید: در حال حاضر هیچ مذاکره یا گفت‌وگویی با ایران در حال انجام یا برنامه‌ریزی نیست.
🔹
پروازهای ایران و افغانستان افزایش می‌یابد.
🔹
مسیر شمال به جنوب کندوان مسدود شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/684245" target="_blank">📅 18:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران طی دهه‌ها تحریم، شبکه‌ها و روش‌های پیچیده‌ای برای دور زدن محدودیت‌های مالی و تجاری ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/684244" target="_blank">📅 18:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot5w8-P5TPw8XOvyKH7yKVpYGeFOEJ2ECj3L-0ytmZnV3V9XrY-wcSjFaSOQW60zeAxpJp1XrynH4P5Fo0ueq5uztQjtrvGG0QKhmICu90oFGV_FhBrBkIoAI2dgJ_ujaXc8ZKT5F7cj1ylQBoO4aZMUXWF6pUr8DSn8sNOBQqRqKFcNhIub6S8K6GClsLWnE-dHMb1Jlupw7HS5vdSu2iJCW_VdZY5GY1HdhIA3jKLD9Q2uxrVZSI1XS6Dh0ack6Gne5hZQvi5edLsfV73Y9EG4f4llZbmVNlr6zASivb_TXMyijvMvBFSayNx3eTw9d4Xj_zUEjBx5Pb3uh-VHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانگین ناوگان مسافربری هوایی جهان
🔸
بر اساس جدیدترین آمارهای جهانی، میانگین سنی ناوگان مسافربری هوایی ایران به ۲۹.۳ سال رسیده است که فاصله‌ای دوبرابری با میانگین جهانی ۱۴.۸ سال دارد.
🔸
کشورهایی مانند کویت با ۸.۸ سال، هند و عربستان با ۱۰ سال و قطر با ۱۰.۲ سال جوان‌ترین ناوگان مسافربری هوایی جهان را دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/684243" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ترامپ مدعی مین زدایی کامل تنگه هرمز شد
ترامپ:
🔹
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از آب‌های بین‌المللی تنگه هرمز برداشته و/یا منفجر شده‌اند.
🔹
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی کار بگذارد، بلافاصله و به صورت سیستماتیک منهدم خواهد شد.
🔹
از طریق نیروی فضایی، ما هر وجب از تنگه را زیر نظر داریم، همانطور که کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلا منهدم شده‌اند را نیز زیر نظر داریم.
🔹
سیاست عدم تحمل در مورد کار گذاشتن مین با قدرت کامل در حال اجراست.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684242" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBW0YVREZHxOVtn-dMN1bSsC53cIvMyOTEzX_FcJGWN5kS7NScJuSmtCEnJv1kRB5g481KwXOoCWojZPAS8OBn4fJdR8Yl6DEh7U7w9GYNVyW7UvgAwBNnScLUKWYBbfbpO7e-Xfu3M4aKn3bUqtyj3rmkD1X4BVT_A-ocKLfMBSBSEk2SDSuqV3hj8KXDYkJEFlN3DOA0PHB2SP4Jk7R_3Cps9Vd1RpmyptcNx8EFNfJR-27EBoSNX0RyWjoydgPrjt2OGZoWYVNU0infwgWfybQYJo-ZEfgoRTMnIrBroXFDGB4U2drIs6USIWNpBcKuiaZbIo_zrevCfKRhdY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشتر افراد اعداد کسر و ممیز در انگلیسی رو اشتباه می‌خونن، بیاین خیلی راحت یاد بگیریم #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/684241" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52ecbb56d.mp4?token=lNgP00oVY9x1QFGpHwDUjGQaWUFdiogRg_UguYiJNUW16BlpcmTWnSSbQp5CIEqLRFg1_brgy3YRW_Ihzy8ChBzxxFU3kXnGWxTFdME5PeR_7tlYRGJLXUgq-qA_S9Fox3XdK_p4LvvFFRxGjyRKgGqRhR8R2Nq4mslFu9OLi7N_wDNHvLVBq5IjFyJFIGj0F-VcpBwipSBCfuzMvnxP7sW4OZ04N1ipZ96I6SU7k3mgGlvRtThqRNdG7SnltHZjfp1ZOGCpKfLYFnloF5yzfGldZQ6XeK_X8wmsGuwM8_YrU6mH_b2ieK6iMOX47QlWtLOiutDtePAHO5N7W_2iug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52ecbb56d.mp4?token=lNgP00oVY9x1QFGpHwDUjGQaWUFdiogRg_UguYiJNUW16BlpcmTWnSSbQp5CIEqLRFg1_brgy3YRW_Ihzy8ChBzxxFU3kXnGWxTFdME5PeR_7tlYRGJLXUgq-qA_S9Fox3XdK_p4LvvFFRxGjyRKgGqRhR8R2Nq4mslFu9OLi7N_wDNHvLVBq5IjFyJFIGj0F-VcpBwipSBCfuzMvnxP7sW4OZ04N1ipZ96I6SU7k3mgGlvRtThqRNdG7SnltHZjfp1ZOGCpKfLYFnloF5yzfGldZQ6XeK_X8wmsGuwM8_YrU6mH_b2ieK6iMOX47QlWtLOiutDtePAHO5N7W_2iug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام تحریک‌آمیز وزیر افراطی صهیونیستی در مقر آنروا: «حالا من جای مدیر نشسته‌ام!»
🔹
ایتمار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی، با یورش به آموزشگاه وابسته به سازمان امدادرسانی آنروا در اردوگاه قلندیا واقع در شمال قدس اشغالی، علیه این نهاد بین‌المللی دست به لفاظی و تحریک زد.
🔹
بن‌گویر حین ورود به دفتر مدیریت این مجموعه با لحنی تحریک‌آمیز گفت اینجا پیش‌تر مدیر آژانس آنروا می‌نشست و حالا من جای او نشسته‌ام.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/684240" target="_blank">📅 17:49 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
