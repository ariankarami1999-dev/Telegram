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
<img src="https://cdn4.telesco.pe/file/jigrrrwDjZa9CCsY8INFgSsd5VoVCqY0KWW-oI_N6bEfPoq1u178EHh1KQzwgjjh6G5qnJ-jfkUGG69mYopfagP6MXMlA_t7mrwS7AwiGFQSEwHzElO6SLvsHnSo9PMhntKUnpOXMlnPVa57uyTkg9InQLrvZalk1zfTT5TKhnpqBWv_XkIxbOUwdnwhYfE_tOkd3i5zWm8IOG0yv27pjbxGcn4djfRa1IRSSp-_VEl1h1dGfq0mXOXFuhymLlwlMuo8BR35XY-akRL9sBVm9w2-156ynKID0HXCyxfY72fMmOb_WNxPkBzqgwXwX-tXuOxz5DbFb1db8S7j8b1C-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 930K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-132000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی ارتش : تو مدت آتش‌بس از فرصت استفاده کردیم و توان و آمادگی رزمی‌مون رو بیشتر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/132000" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK0A4HOMukzD7SHFf0SNrQ3l9zwoYqAXOalkkFoKZ6d5mx-O8c4NlywhSDs6GZZa7vdQbS1rgJBSMoC-c2e7-27VA9KPwde5Xg9LVMckedqjHko5zCjK-FMF8fmCghlwjSXHMugXREFpsm2zQB7qlpc1vVkxh1B-7pX2RPCmS85dESo_WVNK9dUVpNG6Wa-al5-ufCZ9QDX8JvWeh5SyEKkdCXLKF4RWZog3hOefq_xBc5dFjnwCCI-_psPVHGqd_vaEWtRBc5Sabuk0-SvxqKOQvxGeLTnyubPaEov9cteGAXYcInIc4VOEq7VwpL0HUUuRQkhkjQm_IdH6WS6hNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوناتا ۲۰۱۷ قیمت در عمان ۸۵۰میلیون تومان
🔴
در ایران منطقه آزاد ایران ۲.۵ میلیارد تومان
🔴
در داخل ایران ۶.۵ میلیارد تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131999" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74ab95ac3.mp4?token=AuxBiEXHA3hiEs-J9FHkoGQnwKgQSf_y0wRFXC7YGydhFyCgx3qXdyeMlLp9qYrqbt74WbNo0NnDh0oATcpJw353fk6NguHi5QizIXF8Wc5ZtamY61B64108r0eMHNAxjdd4UQstyKAU9z43TpzljrWaT3fFV5fJDVuAraYUwYaBUM3gYAVY5bJWH0nDKEIYJTz2l5DyszNSJhTY8BOmEkt5lNvPG-ixUDBfFC4Uj18Dd_yQLykx78g2DkZGMOGZhScyxnXorVqhV6uwtOz1oMJ4nzUQn1im-NySBlAQMeQgI2IpH5-zytlXcas8AvSzJaxrVcOi0zZdak838djy2jyE53re6iblxwcyPqMhKMvgkEAFZMR4f1RUkCG6wD40GRsmEbz0nghyCR4XEbvLAtRfuX7vESbQOzuCEmpG42HgDjYH35zg0sk2Ss80NmcufF008Jq8M6JufNq2_xC_MeUDbBiBgkJL3p2Ta4t0azm2FSUqV0YJWX4KTLTTNSCz0g6UD5InwwAqtPpC7QaEs4TwAV1Q2ATa68QgkRwe6AHUFM_Gb8U7rTbH0EAInJJ7GWsRP-z6Woc_OGNayqYh2MewCwKrpxiaoXy5zGVNvd47cYU_m2FydqioZm91-pxt4Ytb8yZ-QAWttd-CmGrlZGIsKycn4Ha6dSPEcyJ9FFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74ab95ac3.mp4?token=AuxBiEXHA3hiEs-J9FHkoGQnwKgQSf_y0wRFXC7YGydhFyCgx3qXdyeMlLp9qYrqbt74WbNo0NnDh0oATcpJw353fk6NguHi5QizIXF8Wc5ZtamY61B64108r0eMHNAxjdd4UQstyKAU9z43TpzljrWaT3fFV5fJDVuAraYUwYaBUM3gYAVY5bJWH0nDKEIYJTz2l5DyszNSJhTY8BOmEkt5lNvPG-ixUDBfFC4Uj18Dd_yQLykx78g2DkZGMOGZhScyxnXorVqhV6uwtOz1oMJ4nzUQn1im-NySBlAQMeQgI2IpH5-zytlXcas8AvSzJaxrVcOi0zZdak838djy2jyE53re6iblxwcyPqMhKMvgkEAFZMR4f1RUkCG6wD40GRsmEbz0nghyCR4XEbvLAtRfuX7vESbQOzuCEmpG42HgDjYH35zg0sk2Ss80NmcufF008Jq8M6JufNq2_xC_MeUDbBiBgkJL3p2Ta4t0azm2FSUqV0YJWX4KTLTTNSCz0g6UD5InwwAqtPpC7QaEs4TwAV1Q2ATa68QgkRwe6AHUFM_Gb8U7rTbH0EAInJJ7GWsRP-z6Woc_OGNayqYh2MewCwKrpxiaoXy5zGVNvd47cYU_m2FydqioZm91-pxt4Ytb8yZ-QAWttd-CmGrlZGIsKycn4Ha6dSPEcyJ9FFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنر چندمتری «ترامپ را می‌کشیم» در مراسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/131998" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab849993e.mp4?token=J0ZDfsWpwbZqTR3s-Jqrm23X3W9bD90026_1sftzVKSNxsE5zH3DIaW6A3Q4pvZEYkLgWzmyDGierhjc3GxSig1FBgyBioUBnxdzFYfy3GwBc9Q1QOI8qHHSWpwAYexh5aYK72dBGeTI728KTZWAZKUoecBRx6MEkiSEEBjMGcBKbXNRdQyPyr8IK7w_M8uhSZrHGOLRYckcG3xrdUwoVkAw5ZgOmsG9P1KEeFEjo68nqpSnHp_AlgVst_bxHbkaArTQedM2rl6YmoCCMFDxHekTnPtMbFp4bNHLdU0Ga8ZpH-Hvh0xeQTaJXqhPvkFNw6nmnTrt82ikQdm-tYtEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab849993e.mp4?token=J0ZDfsWpwbZqTR3s-Jqrm23X3W9bD90026_1sftzVKSNxsE5zH3DIaW6A3Q4pvZEYkLgWzmyDGierhjc3GxSig1FBgyBioUBnxdzFYfy3GwBc9Q1QOI8qHHSWpwAYexh5aYK72dBGeTI728KTZWAZKUoecBRx6MEkiSEEBjMGcBKbXNRdQyPyr8IK7w_M8uhSZrHGOLRYckcG3xrdUwoVkAw5ZgOmsG9P1KEeFEjo68nqpSnHp_AlgVst_bxHbkaArTQedM2rl6YmoCCMFDxHekTnPtMbFp4bNHLdU0Ga8ZpH-Hvh0xeQTaJXqhPvkFNw6nmnTrt82ikQdm-tYtEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود سردار وحیدی به مراسم با موتور
✅
@AloNews</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/131997" target="_blank">📅 11:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQuKPIo0yfHdR8aEhL0vIKILR5m7pt3LQ9SvMDy8md45orj-9iVAC1UsifywuzGxs1q57aLhjIJuqUrs1n4_xxq7VCgZ7i5y9YVz_iniQ3os6fVrpM75nhkCixXfaTOSxmBjjPT-8rlIz2sbwLppcszP7K8N5oYdobt4eNzF4yFyThl5hHYnzOD_NCENd6clnKX-t5fMCRcf5uYO2yNQkM9awKB_GNpwKhG27HLxYZRuWlSjF41zoIoL12pUcTsNhkS-bCpz2hlguGyNYjmHyn5s0K5X5LoV2KrwfLQbfO1Eg4LY5AQcz88VdDuKxkJTPiTbDD2xvwkZU4Vzq8OgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی نژاد، رئیس جمهور سابق ایران در مراسم تشییع امروز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/131996" target="_blank">📅 11:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muiEMFU6OPPjHb6UhXC3toK3jZWl-7Vu9-REh0CwVFOMp4kRoNSzkVoQ95NpKawex4iOV6xgPxQgdAEa0od3Via-oK554-AiLUeN7TTg02R6fatUEVf0MO6WEjdoc7F_7d6E_irSdzyfcKRywwRFSsMPSt0093NAKBopPLvEgKd-UgxUBq2CygGbbpUp69gAZudnqOS2yYP8ShNAqoI2_igjGTX9zPlobDBmdtbHCFZezsOB9SvtLZW1uPPMesiyHDtadacicFqg98iFH6cIrprYN2qwxAEu8I62A5E30EcsHl7aPYpGqCrgDaiFocPbAm2Y9svTYqdgP6FbFhs9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور اسحاق جهانگیری در مراسم تشییع
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/131995" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / هشدار یمن: باب‌المندب به روی کشتی‌های سعودی بسته می‌شود
🔴
در حالی که یمن منتظر دومین پرواز غیرنظامی‌شرکت هواپیمایی «ماهان» ایران در ساعات آینده است، روزنامه «الاخبار» به نقل از منابع آگاه خبر داد که «انصارالله در حال بررسی استفاده از اهرم تنگه باب‌المندب برای تحت فشار قرار دادن عربستان سعودی است»
🔴
این منابع خبر دادند یمن همچنین به سازمان ملل و عربستان سعودی مهلت داده همه محدودیت‌های اعمال شده بر تردد دریایی در بنادر یمن را لغو کنند.
🔴
به گفته این منابع، در صورتی که عربستان هشدار یمن را نادیده بگیرد، نیروهای مسلح این کشور مانع از تردد دریایی کشتیهای سعودی در دریای سرخ و تنگه باب‌المندب خواهند شد.
🔴
خالد الشائف، مدیر فرودگاه بین‌المللی صنعا، نیز وجود ترتیبات جدید برای ازسرگیری پروازها به فرودگاه صنعا را تأیید کرد گفت که این ترتیبات شامل مقاصد جدیدی برای فرودگاه است.
🔴
الشایف همچنین گفت که ازسرگیری پروازها بین صنعا و تهران قانونی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/131994" target="_blank">📅 10:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131992">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnS0O7l-0peXkRcskh6UTMliSXJt8GfOo7lJc-w-1lQzzHVU1Ven9T9h0DLUNhQUk-va_LPcqTgEtoJw1wlpDS-h3m0wNzP2uqQvJ7dTK-t8ApCY9h1xk8NqAStCqftwCghEM2WCO9Nog0-nhc0JgFDZ3aU-cp_HYRTKdh1cxs35CxNvWv0wvoanUmsCIVCO0jPQUDmvw5Kd9qhOuoH3vuCoTOsU5VWNMvDzHF_mxowZA-gBLxcspAGMb7yR_3jXXlE2DhkY7XDpQMrCXbVo4UNPEqSCY_V8Il9UAbvYFdDYe3QN_TzO9LahHTnMdaLMtdlgfPG9Lxnmfm3Tzm0Ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/filsq0jr8IXGUCXErLXJPQnZ2tBEb8m74BUTBk2vV5Bu9IlSIjrXoGEwfkEaXgWcfI5kVg6GMRP64n6vmP_welXqDdytkqYkYFbH_fPVmFYHWSxP8h9pnStZoMlMfl-Aqh0GHwVEJLv_i5-VofGdoTUKDVU4qFCpeABob5O-fFz8U83i-LnPgDAnAU5gA2dKE0DoS_oDfzYoQbBg1awp2PAsEdhZZP3DH3aeN4Acq82Hs2JvoseQV4SQ8cB_OwqjRTVJLjuQh9_IF1rHK8GAubYmgOaIgPG0irrOu7a5n9QvrkRRDJMJokjuGQnsqZqodlc1LxIXDpZ0ZF_YcX1pAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در یک نمایش قدرت در برابر ترکیه طی یک تمرین مشترک جنگنده‌های اف ۱۶ نیروی هوایی  یونان از سوخت رسان‌های اسرائیلی بر فراز مدیترانه سوخت‌گیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/131992" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131991">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبرگزاری هندی (ANI): حداقل ۱۵ کشور در اروپای شرقی، آفریقا، خلیج‌فارس و آسیای شرقی تحت فشار آمریکا، یا به طور کامل از شرکت در مراسم انصراف دادند یا سطح نمایندگی خود را برای حضور در مراسم رهبر شهید ایران کاهش دادند.
🔴
گفته شده دستورالعمل‌های محرمانه‌ای در این زمینه برای سفارت‌ها و مأموریت‌های دیپلماتیک آمریکا صادر شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/131991" target="_blank">📅 10:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131990">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بانک مرکزی: نامه‌ همتی به رهبر درباره کمبود ذخایر غذایی به هیچ‌وجه صحت نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/131990" target="_blank">📅 10:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131989">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335c644043.mp4?token=V2eywBd3VuzWTegcSg-cZF1pjpzinJlIPhykYEiOOZhsJbxkIPH4kzj-rv7YZ-k2QsEDHJ7L0Rok_8WLrG9WUY0pAAJt7dh049krb9BYDw9Iw6rM8EMba5V-_tT1bLkHV2iTZrr1qLPuayTgkJlYjgQdDtn-cNMcL44R8zdDv1eqbPKCn5ZRiG5YOKRL6lXtSJgbAAEK9DfPV12R0zaUsYH1URNqWlXQEnU82zn6RXqnOXo-T0vVLGm38z5qGLCviWx4mqTI5YeZB15v5IaOnMv3zYbDySfYGR8p3m-gA5GvS6p0Xnkmflw9SZj039tCQLzBs4NhA2UhG9En3zsU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335c644043.mp4?token=V2eywBd3VuzWTegcSg-cZF1pjpzinJlIPhykYEiOOZhsJbxkIPH4kzj-rv7YZ-k2QsEDHJ7L0Rok_8WLrG9WUY0pAAJt7dh049krb9BYDw9Iw6rM8EMba5V-_tT1bLkHV2iTZrr1qLPuayTgkJlYjgQdDtn-cNMcL44R8zdDv1eqbPKCn5ZRiG5YOKRL6lXtSJgbAAEK9DfPV12R0zaUsYH1URNqWlXQEnU82zn6RXqnOXo-T0vVLGm38z5qGLCviWx4mqTI5YeZB15v5IaOnMv3zYbDySfYGR8p3m-gA5GvS6p0Xnkmflw9SZj039tCQLzBs4NhA2UhG9En3zsU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون وضعیت خیابان های تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/131989" target="_blank">📅 09:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131988">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / ادعای شبکه ۱۴ اسرائیل: سپاه قدس واحد جدیدی به نام « یگان مختار » تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131988" target="_blank">📅 09:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
آتلانتیک: ترامپ با حفظ مشاور مسالمت‌جو (ونس) و وزیر جنگ‌طلب (روبیو) چاقوی سوئیسی خود را برای هر سناریویی آماده کرده
🔴
ظاهر متناقض سیاست‌های واشنگتن نباید کسی را گمراه کند. سند تفاهم پیوند مستقیمی با بازارهای جهانی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131987" target="_blank">📅 09:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37ce8846.mp4?token=HEFRL2PJopmULAzTajx7IAZNjsg1RTPVkqhyTlK9AU6W6nVTIu4sftzlA6d5YjfvF5CJfmCzf0cwl9ME5JJLkUwbB5i8A6e8ehrgHCi20QHDtge0ECTKSRcYbZKAO9FWYsSfSgDMCkkh7KcjFrMi_Bz69K-8ivwQywIlDlvxHG1OB-E6xMSPdUCL88tCEEXlloRAsWGOMgI6EzIoZE2196Vh3ZefSr1JbFDf4PJ5AhJ13-pJ1cYJambTmjMBGv9DmeDxxmClDxHGhqiv1YnkmN8KB2FDOJ6jV_CITswdHjk0mjMosAYiPLUD9TTieq3TPPGEzdpol4R-z9Rhgoi5Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37ce8846.mp4?token=HEFRL2PJopmULAzTajx7IAZNjsg1RTPVkqhyTlK9AU6W6nVTIu4sftzlA6d5YjfvF5CJfmCzf0cwl9ME5JJLkUwbB5i8A6e8ehrgHCi20QHDtge0ECTKSRcYbZKAO9FWYsSfSgDMCkkh7KcjFrMi_Bz69K-8ivwQywIlDlvxHG1OB-E6xMSPdUCL88tCEEXlloRAsWGOMgI6EzIoZE2196Vh3ZefSr1JbFDf4PJ5AhJ13-pJ1cYJambTmjMBGv9DmeDxxmClDxHGhqiv1YnkmN8KB2FDOJ6jV_CITswdHjk0mjMosAYiPLUD9TTieq3TPPGEzdpol4R-z9Rhgoi5Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حشد الشعبی و حزب‌الله وسط تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/131986" target="_blank">📅 09:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فردا بورس تعطیل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131985" target="_blank">📅 09:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2888c102f.mp4?token=k66Dbl9RB7ruUpLaUvFSm0SmhldOB2f5fZpnxl-W0dHj-9l760ptZcbKxrd8EmPhCxc6mpqXjvZZWt0zYIcTLzMXvmmdPcttEwcrevGwAPO4RMvbrbYhgE0BrOYQUfXVrmdr4aO_e7JnBGJEa9ORMvqOFg7QhKDmmaVuijEf_t7VuwsNVCcGRo-PUzOvcRSrLKAGwbmoDaAD9wHb2KNMNpJa0yQ1miltBoOFav9mmMT7jR4JCOEkNBMwq5nZk_ytHY_AP3vMG3bMhxA6lQTw1PJ-cWSM3pUBn0__zYIQfPqm1AoDeXw5_etC8QPcdRf-xGaAvXI80b80h4OjW6lq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2888c102f.mp4?token=k66Dbl9RB7ruUpLaUvFSm0SmhldOB2f5fZpnxl-W0dHj-9l760ptZcbKxrd8EmPhCxc6mpqXjvZZWt0zYIcTLzMXvmmdPcttEwcrevGwAPO4RMvbrbYhgE0BrOYQUfXVrmdr4aO_e7JnBGJEa9ORMvqOFg7QhKDmmaVuijEf_t7VuwsNVCcGRo-PUzOvcRSrLKAGwbmoDaAD9wHb2KNMNpJa0yQ1miltBoOFav9mmMT7jR4JCOEkNBMwq5nZk_ytHY_AP3vMG3bMhxA6lQTw1PJ-cWSM3pUBn0__zYIQfPqm1AoDeXw5_etC8QPcdRf-xGaAvXI80b80h4OjW6lq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی سنگین روسیه به کیف در شب گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131984" target="_blank">📅 08:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131983">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqLzhSVHhTugROx6htRbGg68uvi97o7AP5iOvW9LkRaeaD_FXoHOiM9aTfKUJemVnWHgTv-9MQqJHi4pQwLi0-uGdFUoqDWNAB_KMmNjzVHbEZ1xr6fL6B5PlRQ92G0a-1XvVdQrMv57R9nnuP-8yq_yG1hXHiiZv1C9aKVUycSOrd-xFB8wpbPmSDLMT_K7HX6HR7DdHJjo_MENB7QegGk-sjG46zhIugJG5TnLAPQAta-lqiEHuK33LAV1zO2g7pd4tFgNjQXQrRnHABmUdOBXG4Lsg7u_CVOvKNbDM-pjdTJDyAOx4aK3UL8x7C0aGQtdKyD5Y9wR2GZXMoWEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی:  پیام روشن پرچم‌های سرخ انتقام است و بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/131983" target="_blank">📅 08:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131982">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ccd88a65.mp4?token=KT3nI5TGIPqUI09kEHAuKtCWEZwIBa2AmA-TfunyE80JuUkDh2gjSom8VzLQauW7LQy3BT0eo9v3P3qRGSzGyL8P6psKNHNEfp57LDf41NMh7AwWYjiT_MTGzBM7zuyzfGSUwAfZ2RibFA6rBeOKlLmSuTUOsApi6ObnqtOnTM6_YPNt6VvH-UbSmVfZT5D15R_YOOFiAsqTGVvBkTd7sfyNeGEkiMq2vOjq8YiNqT0OGIS9MQ6fCAFshGpRjgyV19vnu2T0BaD7-Fn4DJNwxVTg0W8UyJu1IZItQz_WxNfgHufj9GhHcClLeVbYSTh4p8PCoNoHHtlnFiyX_t6rCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ccd88a65.mp4?token=KT3nI5TGIPqUI09kEHAuKtCWEZwIBa2AmA-TfunyE80JuUkDh2gjSom8VzLQauW7LQy3BT0eo9v3P3qRGSzGyL8P6psKNHNEfp57LDf41NMh7AwWYjiT_MTGzBM7zuyzfGSUwAfZ2RibFA6rBeOKlLmSuTUOsApi6ObnqtOnTM6_YPNt6VvH-UbSmVfZT5D15R_YOOFiAsqTGVvBkTd7sfyNeGEkiMq2vOjq8YiNqT0OGIS9MQ6fCAFshGpRjgyV19vnu2T0BaD7-Fn4DJNwxVTg0W8UyJu1IZItQz_WxNfgHufj9GhHcClLeVbYSTh4p8PCoNoHHtlnFiyX_t6rCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریستیانو رونالدو تایید کرد: این آخرین جام جهانی من خواهد بود!
@AloSport</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131982" target="_blank">📅 08:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131981">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqidyzzAnJygvDvZfS9svvjrEsX5tWLpZ9Tu8hnbHbNahiejye3k378_DjUPsWeuQ_4EhWIPns9McoV7CSJf8jnAhxRaHiTiCmTrzV5Czxz0KrWo91_lVEyoj0s0xhdkMoOC0xMP_byPfnLiv__324kRKdJ0MSUsnXql8vIgZCnZM_cftMS1K4V7tyngmF-xHPK93SkbDVeG_IO8qZMq3TEOXJ0wW1GVOu-DSDGix8b63KEvnd_YbGdxqrktgBsRdQw3BzNMihwXitlLCFxh07hLnWSfNAUUTs8FO0DCZ5IpwLR6561bquHvdUIQyKaBknWBa9AknRG5Hntl5_rl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی دبیر: آقا زورخونه‌ای بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/131981" target="_blank">📅 02:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131980">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-2V28pl7BUXPatZLj_jimb3LGlrX0MNtx-ShyEOIcXoOy1bfawRn-JvzhV9_B7XfiGzgCfw-sqpmPTY_UK9JPOsuGTaCJy60MiUwpFuLTv76sA8jdJXFaBLAzvk5eUcKjJhD8xFXqw-vlvaFhDlIxnGeE7ZpuYnaUcfNlT-lN1DjC2FuygbGqeFNGjAYWBPyV_tQ34_RK18zrvkHBBAxzQi8rNIodJvQUaaLnPef1FV17o7CpZpJQPNb16VWLWFzWP6yADUYSQ6iBqZevnd-fGru7mmCKBd3MbxqaV_lNfzaIA6YebFOhpMqXxFruSSBfHP_HTFmOXweih50hxKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ در Truth Social، نخست‌وزیر ایتالیا، جورجیا ملونی را تمسخر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/131980" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131979">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEHdZVVpxC0P56mflgZIyykBrjqFgI3cUScG10LvmsNn3haMraGbvZD0gRbkKZxsLfLWNfnZl6NAtZYCu9Uuceqays_d9igeS2MLqMJrnlm23u3vbwsHAPq6D8cYo0OHWs7YSCOm1z_c20GamlS2g4ZW24gl_p7jpKR63o4v_XySsg5kPgj8aALToFhN5yF4qiDV3nCCLoJzxKply2z0tScw_18f28dRdFtWMoJrvRk5QH0uSiAfoE8SMut3Vg3cO6brpCZ7LiR-vXRMtQDQ8wKRWdNQihvGKvDvZf1MVB15MUy4RpItGWoSgDV4HWkoKlKvxiPAWOjIURWxJ4EvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
نروژ2-
1
برزیل
🇧🇷
‼️
ابرویی که بالا نرفت/ بچه‌غول حکم به حذف برزیل داد و نروژ را به یک‌چهارم فرستاد
@AloSport</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/131979" target="_blank">📅 01:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131978">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نتانیاهو: اسرائیل هرقدر لازم باشه تو لبنان می‌مونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/131978" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131977">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de38c0981.mp4?token=TTAMbg1EADo0bSNx9R7n0uYAmPSmNTU_Ouyhk08ma0aNXtyvw2oAADlhsFk37g0W-NlNW9On6m4TsoMOSseQrXO8AcAW7i_gVTPd-W59_4HVn-f7mDbnm7mXuRAfgMlT7u9rRrjYWSNd-D-W6q8LV-sSVYIt9KZq2ppOjnfiZRyvW6_gzKoI2wq1n4vTyIiusq-CFSH_W7aHyzkvgqcO7KEMEpUUT-7FAzleUkQXgG3cxhPdE5HNvRdYELLDxl6bS6Ek0Cghj_6ilviA5RchbJa09aOwIr7QIHJcMw10Xhq5PLk1HHwRYMxKgaij-K2KV7Jc-6d-66wKAc2V2kVETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de38c0981.mp4?token=TTAMbg1EADo0bSNx9R7n0uYAmPSmNTU_Ouyhk08ma0aNXtyvw2oAADlhsFk37g0W-NlNW9On6m4TsoMOSseQrXO8AcAW7i_gVTPd-W59_4HVn-f7mDbnm7mXuRAfgMlT7u9rRrjYWSNd-D-W6q8LV-sSVYIt9KZq2ppOjnfiZRyvW6_gzKoI2wq1n4vTyIiusq-CFSH_W7aHyzkvgqcO7KEMEpUUT-7FAzleUkQXgG3cxhPdE5HNvRdYELLDxl6bS6Ek0Cghj_6ilviA5RchbJa09aOwIr7QIHJcMw10Xhq5PLk1HHwRYMxKgaij-K2KV7Jc-6d-66wKAc2V2kVETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بی اعتنایی عجیب پزشکیان به مسعود و میثم خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/131977" target="_blank">📅 00:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131976">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سه غایب بزرگ مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/131976" target="_blank">📅 00:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4yb2qvYNceNwYTxj1liNh8lTWpkLkUwzHSA1Z3mqNKV8X78nKDDu5B1Otb4iPp_o_LF5sinHft3ozGMrs_jazSwnA9UVzG1FrDJEVHHkWsMnGiNaSR6vnjtmyGHlf7619nplnAMEzgE8jtv1gesAVnMBSN2aIMWkcT_ijP3weQ9meQli1upv3sdKeiIESAULSDW8s1lOj8pcBfi7hL85GD-nLqQ2Ux0736bFEMKGLTqtWrNu07WoaQeDcvWTzk4DEINqmzpT5ktRDqYjpLrgRx_kMCLPVbv6e99t8Stt5lVF6F2gjbkpLV1fwrhwWBnnQKZBP6OtmqPu1o6ryjZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOmk34ReR1lKN2iqwV13niUCkSxuoTksI7sxRoqr7KW81mN6jYoSI-B8u2A1_Ai-IwPyChRQdQ69XXLjJjYDn8j24zt0vUM3Yk96JsWv7T_cgjYPjhsilJWn3Ul9l8OhNr7Tg4K9Yw7-sjryIrA9-bua2gsE-vN5qYhPqynXkx42_uoXg-8uV5Dc34R70Hqn3xpZRdgVBdknujdB1U7d6FNci3_AJ4YmWuZyktlQU7z3syoCMm8zLu3c1U4dSVH2Ee8gh0yf_2WHVAS0xYILUn-G8HXXVxMdQwYHpkjjFFamPZitK88rw8JKOlph-C2fw04zyfNrQBucvwhqZb6IqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwKeBgDdjV7Fh7NCjwzge2F4eM24_BHGWce4gSbR_rMWt8LzOzpaNOCeXZN1aFTaZIsfIhjJrByx5qgVY3yS_5sl4AnqBITyeHUvczoZwF3gyrEPB1hDnLa8u4mnVZ5e0PatzmyngmVJRoKmq8MT3DYV9h6_VVP4sYBb7rOYbCTY7MpVs-hBVYrfPOmJn2johAhwf144mM1XErprBwr4hT9RmUkYKL6FibKbm6Tx73ZL3ANNtmWyr2eYLgXqamq07VyZ2V6BP5w_BvpWXFRok3TlKC5oSu230Zs-H2xyUmPqp75A4g86QwYJ5HjvmWPv8RnPbZi1-oFENDID7jC2MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سه غایب بزرگ مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/131973" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55821e32c.mp4?token=I6wtDB8BCgwj0HUJE7qYja70DA_0E-gHqe25NNCj3UNi3vk3Aoes5O92e_M8eavL9wtR4bWHeS_R4kHq2D-AHnbHVYAS-sAKNHn1y7HzRYaRwZu4Tk1RJ24A32or04nGRJV462uXjCyV6Y0Ioig6oRzk0SDXaqla_tiiJv2YWlddC-x-aEi6LDUw1ZtdLg4Y0AcEzVqG_RkhqcCPnnjyE0ODoSMly0kWyeobRLRHh8BIHHOWLQbJl9yj2RCMzKH_OzGTxo8opZVOPcraDPisxFdyeS51Vey6-fyK9hFref1zQzO053J3aRMePkjuW_MSDz9Jdf7W4XXDZt6K7NNrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55821e32c.mp4?token=I6wtDB8BCgwj0HUJE7qYja70DA_0E-gHqe25NNCj3UNi3vk3Aoes5O92e_M8eavL9wtR4bWHeS_R4kHq2D-AHnbHVYAS-sAKNHn1y7HzRYaRwZu4Tk1RJ24A32or04nGRJV462uXjCyV6Y0Ioig6oRzk0SDXaqla_tiiJv2YWlddC-x-aEi6LDUw1ZtdLg4Y0AcEzVqG_RkhqcCPnnjyE0ODoSMly0kWyeobRLRHh8BIHHOWLQbJl9yj2RCMzKH_OzGTxo8opZVOPcraDPisxFdyeS51Vey6-fyK9hFref1zQzO053J3aRMePkjuW_MSDz9Jdf7W4XXDZt6K7NNrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسئولان برگزاری مراسم حتی به آیت الله حسن خمینی هم تیکه انداختن و هنگامی که با برادران و فرزندانشون اومدن ادای احترام کنن آیه زیر خوانده شد
مؤمنان خونه‌نشین که بدون هیچ دلیل و بیماری‌ای جهاد نمیکنن، با مجاهدانی که با جان و مال خودشون تو راه خدا تلاش می‌کنن مساوی نیستن و گروه دوم نسبت به گروه اول برتری دارن.
🔴
حسن خمینی هم همون اول گذاشت رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/131972" target="_blank">📅 00:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e716df92f8.mp4?token=e-OuIkDWvC16QfW8C49DprdiZyy-KApNXAfIYy2MG_h0QUu86_wmd7mFo6dTbn9dIFhXB-sZQ28-MkZ1ufKdx-Ei2GFcojZrCmeHopZjnxB6KD6zOFh98o_K0SC2yteUvFb0KEG0kQNAKe8g0GgXFpqhE5ur6HCXm9U5K9fIpwFY4IC4fYgjWDDiAswVCMjQrUVieZ9B9pdb4SLV84nhhv8S_hOC06g5ZnQthrEpcM6ALJRXJizkqKGA4MPFjGTcuAwpVRLLbLrxkbEAeDRKV9Ztwr8D_4GJbEHDwp3GSnUlUG1276H7xlIajt8YG3q6AML_as0sq0gJ0CRsgMrw5r_arhWSo8w-XdQrHtxypOFe6loJ2Al5EcAaaC4nu1Z_Y-kFWI_I-7BtOv7tbbi1Lvtp5AOp5STM8H_A_i7h3h_LUT2G1X3zBMat9iucG_nesxY7BPI2iMffyYzg77lFsbfOIwpHbWM04YUoWBSqi0Ht_TECNjbHCzbBxUsgKjv0W_--nh1BmPQp60S90keWk_xthZFf5lEGPDe2m3mtWEhD2eJCtl03DgPTAPgfWOGeUjjlREhWfQi3gSOK8Op6OA4Wj3lfIpS02pRsuX5QY-YKqRznD7HPXvO5tUY2qlIgpvbBTkZ7HklJLPfAzOYhgJhkMOwHOXqzVI_1wHiMIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e716df92f8.mp4?token=e-OuIkDWvC16QfW8C49DprdiZyy-KApNXAfIYy2MG_h0QUu86_wmd7mFo6dTbn9dIFhXB-sZQ28-MkZ1ufKdx-Ei2GFcojZrCmeHopZjnxB6KD6zOFh98o_K0SC2yteUvFb0KEG0kQNAKe8g0GgXFpqhE5ur6HCXm9U5K9fIpwFY4IC4fYgjWDDiAswVCMjQrUVieZ9B9pdb4SLV84nhhv8S_hOC06g5ZnQthrEpcM6ALJRXJizkqKGA4MPFjGTcuAwpVRLLbLrxkbEAeDRKV9Ztwr8D_4GJbEHDwp3GSnUlUG1276H7xlIajt8YG3q6AML_as0sq0gJ0CRsgMrw5r_arhWSo8w-XdQrHtxypOFe6loJ2Al5EcAaaC4nu1Z_Y-kFWI_I-7BtOv7tbbi1Lvtp5AOp5STM8H_A_i7h3h_LUT2G1X3zBMat9iucG_nesxY7BPI2iMffyYzg77lFsbfOIwpHbWM04YUoWBSqi0Ht_TECNjbHCzbBxUsgKjv0W_--nh1BmPQp60S90keWk_xthZFf5lEGPDe2m3mtWEhD2eJCtl03DgPTAPgfWOGeUjjlREhWfQi3gSOK8Op6OA4Wj3lfIpS02pRsuX5QY-YKqRznD7HPXvO5tUY2qlIgpvbBTkZ7HklJLPfAzOYhgJhkMOwHOXqzVI_1wHiMIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عربستان حسن نیت نشان داد اما جمهوری اسلامی بازهم نیش زد!
🔴
هنگام ورود هیئت عربستانی و ادای احترام، آیه مخصوص منافقین خوانده شد و به عربستان متلک انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/131971" target="_blank">📅 00:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dekQpxoJ1RyojUfcPPPBjYrz5I_gXbyywMQ52-u_lNbM6byRO-BycbpZnljemTG-sv08S-7-6njnVTEJn_M_-K8K1IzpZcIHmsBlEEr0oiie8L8YlUHf22x-r0djYvtH-Lsh7Ad4T7hcin-MWz93LIjdczkCc0Nm6PHIdFLbCjItazDtr_yIROzHQWwwqh6K-vx5P2RqxfAWQuuG1LbguV1Hif9aBDxpTnOPHVUSnjUCKhviZm3SANLsx9CbNupLaa-vQ67WJ078nqozjwQJ9-ys15o9msvVT41sKDbc7m2yyYgyKlsx9ZDzOK9_Czh8EWjDdWSWb54gChDxt3pwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی زرنج شهر افغانستان، یه کودک 8 ساله در حوزه علمیه مورد تجاوز گروهی معلمان دینی خودش قرار میگیره و متاسفانه جون خودشو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/131970" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/131969" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41L3Jtvvd_h1U9UgVXnDtx9KmfRnUauzEvpQ8EszycaQVX5echn3BN_e_6YEWSU_uXaBPoKVjdEn_yTrfif0vcUoZZV2lGXszaGooJ1Jdg5iNLdkDpLlvOmv0OIko8an_-lkeeo4AKQOfjMC5pKqQ-ZVqh5zxZe33oZ1vp1vMxlLhuvn3KxyDZjeo1-KhFPsZZSIi_Tzo6EbtMPX6Er9JJDkdPQGLwP747QIPA8mt9DfqNdOWPWkln6GcS-PAe6Ew2vWwyexLC-6G209jP4zCKBS3IdmVVi7XvQRd4lXh5e3m9jYVAO0qLxgHD2uXZ8eb0uy9DSE8bm91KsW_-vwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین پهپادهایی را به کریمه و غرب روسیه پرتاب کرده است.
🔴
منابع نظارتی نشان می‌دهند که تاکنون تا ۳۱۰ پهپاد پرتاب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/131968" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWr-Qxud94m22K_5XFbWbM0T9DfdzVK1SKASDv5UvO4CWX7vn_rOYGNdvPTBIKZ2fk6ax0r2ig6Dequ21RZhnSeWEL94IFB5JTBVjP3wONE9RiF-ByllrZ4ylVximkbx2ESVzSVKbDerRIJ6zRigj6HolqZBTfvalCQM-PbdrYxpZD29p4Ra06zUYRsy1svkes4qRn6i7W0FM9sEQnnp3I0e5eEAHoZvK5cohT8wfGQFRiVz6sUpeQeiZHbp_Oh6NMJJRjNGUsxCsC7TmdOj29USKEZGj0K2QThTm3aqq7fIEdOmGYbz0K2Oos8wm40Fa2eF2oh2rVa6x9irVQgEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال
:
تجمع ساعت ۷:۰۵ عصر شامل ۴۲۲,۰۰۰ نفر بود! همه مجبور به ترک محل شدند زیرا به دلیل آب‌وهوا، رویداد لغو شد و همه به دلیل رعد و برق رفته بودند.
🔴
وقتی شنیدم که لغو شده، بلافاصله آن تصمیم را تغییر دادم و مدتی صبر کردم تا مردم برگردند. باورنکردنی است که حداقل ۱۵۰,۰۰۰ نفر بازگشتند و این شبی حتی باشکوه‌تر از چیزی شد که به صورت عادی می‌توانست باشد! این نشان‌دهنده کار تحت فشار بود.
🔴
تبریک به سرویس مخفی و نیروهای قانون‌گذاری بابت توانایی بازگرداندن این‌همه نفر به داخل استادیوم به این سرعت!
🔴
این شبی شگفت‌انگیز بود که حتی باورنکردنی‌تر شد با این واقعیت که بلافاصله پس از پایان آتش‌بازی بزرگ، باران‌ها با تمام شدت شروع به باریدن کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/131967" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
استان خوزستان سه‌شنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/131966" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51d88b2c6.mp4?token=YIll9yGFlASafE8lX638WBSlqGfN3PZdoBuyz656XLPHF_wHedKYwuipVv0cl1ilrtoMjVDXIhBXxqy5X_6t71VM78dFDrS8WDjD_-IKxnXUZEkwYZlIpZDwnOij6p5zASytDGrcjxXR9joQWiSz7We7tjN6wGvD1V4ZpcHyZ4hKNySJpzRyLPkN4yT6rm2bb8GKvdsewfNyn8pENVTf2E4ZJp1IaG0VuqppG50PV8mcgoTMU4LYI4Qzn_SlvzPrSz52f37KjwHAFyYdZaQy7WHFdkVuH0PICv5e9ZLsdt3zVBquZR_jtnCeOXnhbZVRzcO4VFp6LFm7tDrItif8HbAw_Tac6caWYhNx-OOuMqnaigvCZzS4zHY-g7cxM3Ux0yeBB9uBuUc0niev6QcXRxsbOGz_tJPrukwuSYhpgnRcXJMU4_KBrxsdG0Cyqw0s1smHmtk20_BUXE4X_vUr3N7gRyxGaTWUjC4E2V61Ts7WtQfzOzSCs99cG371pnBaIzEIcfoWlsH8bvAmcvuyatDB8tZhJjSCY9rfOipSmBBAdov_3S7q9E85ysAJ9B3aKeVfau2vHDk6eITXd3ZIi6xsZZahRXdmbayx0spC5N0yJ9giK1pBTVZ0JPOuoltSgLxbeA6XnSiXlHxAqyO5h4v2WxzeiHYbtHmu-jPi18s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51d88b2c6.mp4?token=YIll9yGFlASafE8lX638WBSlqGfN3PZdoBuyz656XLPHF_wHedKYwuipVv0cl1ilrtoMjVDXIhBXxqy5X_6t71VM78dFDrS8WDjD_-IKxnXUZEkwYZlIpZDwnOij6p5zASytDGrcjxXR9joQWiSz7We7tjN6wGvD1V4ZpcHyZ4hKNySJpzRyLPkN4yT6rm2bb8GKvdsewfNyn8pENVTf2E4ZJp1IaG0VuqppG50PV8mcgoTMU4LYI4Qzn_SlvzPrSz52f37KjwHAFyYdZaQy7WHFdkVuH0PICv5e9ZLsdt3zVBquZR_jtnCeOXnhbZVRzcO4VFp6LFm7tDrItif8HbAw_Tac6caWYhNx-OOuMqnaigvCZzS4zHY-g7cxM3Ux0yeBB9uBuUc0niev6QcXRxsbOGz_tJPrukwuSYhpgnRcXJMU4_KBrxsdG0Cyqw0s1smHmtk20_BUXE4X_vUr3N7gRyxGaTWUjC4E2V61Ts7WtQfzOzSCs99cG371pnBaIzEIcfoWlsH8bvAmcvuyatDB8tZhJjSCY9rfOipSmBBAdov_3S7q9E85ysAJ9B3aKeVfau2vHDk6eITXd3ZIi6xsZZahRXdmbayx0spC5N0yJ9giK1pBTVZ0JPOuoltSgLxbeA6XnSiXlHxAqyO5h4v2WxzeiHYbtHmu-jPi18s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما به خبرنگار نشریه تایمز: برو به مردم دنیا واقعیت ایران رو بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131965" target="_blank">📅 23:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWMbLnUjd3QVrBb2cWNRwqjHJokaOowg3yalHsEZCiGFRuZECRSIPcZmJUlwGrBfzKliX_AgxsUbgYgw3TRN3WnGSpA_JxpkxKezBVuWFTfexTb-8RiHG1GK9vZDLC72sQmljE-hc7mQmvMqM-QgIkezgDlKkmRLx8Q3ui-L6lUyvs_oH5_d6ZFBqPwqByx_1tVVzjif3DKrKzcXKyRw1iblI_4bfvVBwqG8PEWyl9Uz4PNN-7u6WaC-dW7fkJF80iG4euMx9kYd5Gbh3jPDb7d0kOe5llrXQK40ns_xiqpTQ1R6LxUuXH7Yo_Odd_rkcFEvaFlXajSlw0IbyB-QKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسوشیتدپرس: یک مجری (محمد رسولی) در مراسم تشییع رهبری ایران در برابر جمعیتی متشکل از صدها هزار نفر، خواستار کشتن ترامپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/131964" target="_blank">📅 23:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر  شرکت نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131963" target="_blank">📅 23:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
زلنسکی: طبق اطلاعات به دست آمده، روسیه در حال آماده‌سازی یک حمله گسترده دیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131962" target="_blank">📅 23:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرگزاری رویترز می‌گوید احتمال زیادی وجود دارد صندوق ۳۰۰ میلیارد دلاری بازسازی ایران هرگز عملی نشود.
🔴
این گزارش می‌افزاید یکی از ارکان اصلی آتش‌بس ماه گذشته میان واشینگتن و تهران، ایجاد یک صندوق ۳۰۰ میلیارد دلاری بازسازی ایران بعد از جنگ بود.
🔴
رویترز به ذخایر ۲ تریلیون دلاری سازمان سرمایه‌گذاری ابوظبی و صندوق سرمایه‌گذاری عمومی عربستان سعودی به عنوان گزینه‌های محتمل تامین مالی صندوق بازسازی ایران اشاره کرده، اما می‌گوید با توجه به حملات گسترده جمهوری اسلامی به این کشورها طی ماه‌های گذشته بعید است آنها صرفاً به درخواست واشینگتن هزینه احیای اقتصاد جمهوری اسلامی را بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/131961" target="_blank">📅 23:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: واشنگتن در حال آماده‌سازی ارائه درخواست‌های رسمی به اسرائیل است که شامل موارد زیر می‌شود:
🔴
کاهش تعداد ایستگاه‌های بازرسی نظامی در کرانه باختری.
🔴
انتقال وجوهی که به دولت فلسطین تعلق دارد.
🔴
اتخاذ تدابیر سخت‌گیرانه‌تر برای محدود کردن اقدامات خشونت‌آمیز و پاسخگو کردن مسئولان آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131960" target="_blank">📅 23:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c5bb8bd4.mp4?token=H-QNJ6hJEMn_eS-1KC1vIJtD9qEYX0EsH0sO6NhSDgQoqWA53R4PGEzXIRDfbmlmWdrcqyQZ4HSsRWJtD3pnspBwxieHE7Di0pQcFpZTebtAPGuyGg0J80Rt5xz-tz85pOr8t0mmE3foXmWu5Qk-L93-ztRO2yGGZooPmEX0nR9wRAf3OxINOMaDEaBuGRe59wsNGnFgSZyCmYg8pB9kASNX2w4IpeIMmdk-AU1H_PV7nkW0nelatV03zk9qclZu9j_ZxTfwgC4WgXNWDi2pMrvlJyQ6kq1zXLXU19R4YwxxcL6fBIRfu4Bp5wMQ-X5RkEbYoGFt5JIr1-i3UGqVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c5bb8bd4.mp4?token=H-QNJ6hJEMn_eS-1KC1vIJtD9qEYX0EsH0sO6NhSDgQoqWA53R4PGEzXIRDfbmlmWdrcqyQZ4HSsRWJtD3pnspBwxieHE7Di0pQcFpZTebtAPGuyGg0J80Rt5xz-tz85pOr8t0mmE3foXmWu5Qk-L93-ztRO2yGGZooPmEX0nR9wRAf3OxINOMaDEaBuGRe59wsNGnFgSZyCmYg8pB9kASNX2w4IpeIMmdk-AU1H_PV7nkW0nelatV03zk9qclZu9j_ZxTfwgC4WgXNWDi2pMrvlJyQ6kq1zXLXU19R4YwxxcL6fBIRfu4Bp5wMQ-X5RkEbYoGFt5JIr1-i3UGqVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف‌های چندین کیلومتری بنزین در روسیه در پی حملات اوکراین به زیرساخت های نفتی این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/131959" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USpIYFrISmPBIGEwD2gWsEy59gt5oU89u87WdkzrWPwDDcAMB7W-K2KoabwvU5BgM2XXz-u0ZfK561xxv-NLqa2h6bD_wzDlZRhgHJKJK3WdKHvaMRJkVIBhCA8uuWUN8jIwN-usKAulsPjeGyn5P7Npb0014UWQtbxwJof4syrUvTkLJtgXd3GwRVLxBOxd1_2rz28bIdzFCK0InF2ZUVZ32hdiBj0_ATpiGtnq7D6RqJfAUYslTOFm4GRan3lRPUL5Ei2xyCWv3ejyTCffEzvmPhevLW0aG837gj6NM91a92z3cvYMX6XQ8GfHGN3kfnPMp_JLaydM1wrs-umIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تابلوهای جدید بزرگراه I-95 در جنوب فلوریدا اکنون مسافران را به سمت فرودگاه بین‌المللی رئیس‌جمهور دونالد جی. ترامپ هدایت می‌کنند، حتی پیش از تغییر نام رسمی فرودگاه بین‌المللی پالم بیچ که برای 9 ژوئیه برنامه‌ریزی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/131958" target="_blank">📅 22:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBE3tXqA4COX_6NlrVxgnT0RIF6cISwUbRTKi-u6Bv1h41LnQaklLqmrjXPGiG2mqMTEAQOGdGeBTNdZBTHqmeL08ufvq4qS4fku344SBdfqiPyJTfZ0s0IdSvMAHx8_MsWmT092wfOlrAa8WkMD0ISMch8-T0Lm7vvMgAECjGS84_xS2KCcWv7Lg4p6HMQ_ZtBwdjca46w86WhzXz8QROOQBxQwq98So_frEInXjabb_NnpW7-kEuEAliuYddLq95qyhffzFSeFCS06rsFP5UXrBFmWPrtSfR5DIcMrKqDc1x48oyDjEDMvOb_9cvd-vzAneFHvM62e5uPzI1k7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
⛔️
تصویری لو رفته از همسر سپهر حیدری و ساسی مانکن در ویلای شخصی ساسی
‼️
⛔️
گفته میشه دلیل طلاق اسطوره پرسپولیس هم همین عکس بوده!
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131957" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
شمار قربانیان دو زلزله مرگبار هفته گذشته در ونزوئلا، بر اساس آمار رسمی منتشرشده در روز شنبه، به حدود 3 هزار کشته رسید. هم‌زمان، با کاهش امیدها برای یافتن بازماندگان، تیم‌های بین‌المللی امداد و نجات عملیات جست‌وجو در زیر آوار را محدود کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/131956" target="_blank">📅 22:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it22J6vOT0psEuI324PpdtrSy8xdR_m0af9dIaN-bw1XoLMNTR5BZNxXL8TYOSuOEsSi6okYtuWd9uYetjXm8FPPS8nuwZNPq-KDEQURQbUEicIGW5vviP1WsCRLWOl0AEuCNynveTEMo0tGGMOBD45iVihCTZxOA-P2iwh10g0lUriN_cDEjBdecvjseS-3sXqsUuFIccUZjYcE0DC0FCvLnW6AHiLfSJ_JdIO4Ow50K_zwPu78a6ylYjTWna_JsrGlk5hmx1cvjfG1V_CK3JBCF_Me_8NpbVgilWYkBJGcl6LLgznnMOz6YqnooAE4quqG6FHj8oMZWoTZDgJYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: هیچ کاری وجود ندارد که آمریکایی‌ها نتوانند انجام دهند به جز شناسنامه رای‌دهنده (شناسایی)، اثبات تابعیت یا، مهم‌تر از همه، لغو مانور پارلمانی (که دموکرات‌ها بلافاصله پس از به دست گرفتن قدرت انجام خواهند داد، و ۲ ایالت دیگر، ۴ سناتور دیگر، ۸ نماینده کنگره دیگر، حداقل ۲۰ رای الکترال اضافه خواهند کرد، و غیرممکن خواهد بود که یک جمهوری‌خواه هرگز دوباره به عنوان رئیس‌جمهور انتخاب شود. من نمی‌خواهم آخرین رئیس‌جمهور جمهوری‌خواه باشم!).
🔴
جمهوری‌خواهان، هوشمند شوید، اگر این کار را نکنید، مدت زیادی در قدرت نخواهید بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131955" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سی‌ان‌ان: ایالات متحده انتظار دارد رهبران ناتو در اجلاس خود درباره امنیت تنگه هرمز گفت‌وگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/131954" target="_blank">📅 22:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بر اساس گزارش ها ،در درگیری های اخیر یمن حدود 50 عضو از حوثی ها کشته شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/131953" target="_blank">📅 22:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=J6_1oLGHt_EE9kebzfWoMr7of9uNCPTxoUR6BRUJNnwG0dNgb32RuaiapA-29ZEwObeV26s9vLuhXNCRkKDxpiLmO-tspIkW-ei-4lWz3hNCvNkLHdumr68TForMOqAZR3j3_fr09zgGqlR53zr0AOi0hNl40G8WltLAz7S2_if2RhIzDJMljs--FUyl35XqN9gTJf0NIujf2vSXUS5WB1ZZCV5UnZM1ny593brmxnawZwlTo_wlsh0ct9s_vLmgJE-bM2mjIihl99kPWinjW0Ht61WfUJK4e5jWOtkdwFZleJJqMgF8H5pYRfALq9f9QHWVtBtW6Nsy39FdeuAbwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=J6_1oLGHt_EE9kebzfWoMr7of9uNCPTxoUR6BRUJNnwG0dNgb32RuaiapA-29ZEwObeV26s9vLuhXNCRkKDxpiLmO-tspIkW-ei-4lWz3hNCvNkLHdumr68TForMOqAZR3j3_fr09zgGqlR53zr0AOi0hNl40G8WltLAz7S2_if2RhIzDJMljs--FUyl35XqN9gTJf0NIujf2vSXUS5WB1ZZCV5UnZM1ny593brmxnawZwlTo_wlsh0ct9s_vLmgJE-bM2mjIihl99kPWinjW0Ht61WfUJK4e5jWOtkdwFZleJJqMgF8H5pYRfALq9f9QHWVtBtW6Nsy39FdeuAbwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/131952" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بانک مرکزی: سامانه‌های سحاب، پل و پایا جهت انتقال وجه روز دوشنبه فعال هستند
🔴
با توجه به تعطیلی رسمی فردا، سامانه‌های ساتنا و چکاوک روز دوشنبه ۱۵ تیر در دسترس نخواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/131951" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دلار در تهران به 177هزار تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/131950" target="_blank">📅 21:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-VSwumG3g3b_SPlwHB6qKwsuk-g7_83BeOuKvdfhQQmlJcPwY25AGq51AIS0eW7znEmr5iHEEkvAn31lhBcMofizKhtmCh0XlXf_wxz0mG6sV2DY83i1IdKSdlEfuiTjiojuBROc7S0xUYnUzj6EVAzJfxRp96h3zqjVE436LZ68x2e5Rur2aFmcBkPQOPbqZILIh5wDHocGvbXueI5EOPAQ_XbkjTiJFVfhS2l1o_LXmDa6yLQbN_AY-OetlpmxG4cD0PwiqRCXHY_oH0YBMimW7ERT-grr26OWMrlZNtSPaQskSFy8eL4jHQJK7dcRGiEC-6Ko7iGuRk5kGjkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه امیدِ صداوسیما:
برید تو بازی ماینکرفت، انتقامِ رهبر شهیدمون رو از آمریکا و اسرائیلِ جنایتکار بگيريد و فیلمش رو واسمون بفرستيد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/131949" target="_blank">📅 21:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نتانیاهو: فکر نمی‌کنم میان من و ترامپ شکافی وجود داشته باشد
🔴
در ۹۹ درصد موارد، من و رئیس‌جمهور آمریکا کاملاً هم‌نظر هستیم، اما مانند هر رابطه‌ای گاهی اختلاف نظر هم وجود دارد
🔴
کسانی که از اسرائیل نفرت دارند، در نهایت به آمریکا هم نفرت پیدا می‌کنند؛ وقتی تظاهرات می‌کنند، پرچم اسرائیل را آتش می‌زنند و خیلی وقت‌ها درست کنار آن، پرچم آمریکا را هم آتش می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/131948" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131947" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ادعای شبکه عبری کان: در روزهای اخیر، گفت‌وگویی میان ارتش اسرائیل و ارتش لبنان با میانجی‌گری آمریکا آغاز شده تا معیار روشنی برای مفهومِ “منطقه عاری از حزب‌الله” تعیین شود.
🔴
تنها پس از آن، ارتش اسرائیل مطابق یک طرح آزمایشی و بر اساس تفاهمات انجام‌شده در آمریکا، از مزرعة‌الغربیه و فرون عقب‌نشینی خواهد کرد.
🔴
همزمان، از سوی اسرائیل نام شماری از افسران لبنانی که با حزب‌الله همکاری می‌کنند، منتقل شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131946" target="_blank">📅 21:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
الحدث: نتانیاهو در دیدار خود با ترامپ، تلاش خواهد کرد تا بر "توافق" بین واشنگتن و تهران تأثیر بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/131945" target="_blank">📅 21:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXthG6amQxdhvWMtqa7q6bLybo1RGaxlwH0IY1ys0nw2Z9tOxJnoTnWNhoBHnt9j-eNVe7Kjr7veFpzS0UzAXdAEf2V4t7eygh39M9el3Zt6eS_j-nCXpsvmrqwTCmvjAAiqnWRkLdQC8R7cP9eeZ8bzhSvomk4TRZ8AT3ECzUm48Ki1AsaAqn9cHmx_g_teh6NpkF9LVn35KQdPkkTC8mLfpxEHotrFOcQVjf6lYyPekMUvlFJ0uudlLGKdheQNkh5DfA5dTs2CqauNRq2YBv6AfxiyXNYBIg7Elxy_cVMOGO16tegjrN8M-jAfojzhE2MzFsnZ6X76Nzlu9E2wgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/131944" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیدار کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/131943" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e189569c76.mp4?token=Kdpbapa8NtoLMoOHp6mbqTTXwkui-tDMqjX5PmOTqQA8A6S7Ol2uXWZ_tJrt59HmLaQv-YUZPUxuQRUx2KS3Y543eg6vKZCtP_zcdMQpd4j_FKCqLm_8Ufqnf1IulCrWXNXcZpdcJuEZPRMRUN54Skr_F5NcAhlHnfKdNdlhWpLcRZJsVEcaOk8m6YE3eZdcPk_SrJGrOu1nVtZ5FobXqAydWWcM7uHUUVoOjx7Q5t4RddYo67TU5NKuxpDtiX1RIIBgBTJr8v3BRaAwNbKEFNPcN_Bbym-dN2vyWiBsmtxP3ghTQLlI720RpFJ-UVOHJljDEPH3FEa-kk2qrAB5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e189569c76.mp4?token=Kdpbapa8NtoLMoOHp6mbqTTXwkui-tDMqjX5PmOTqQA8A6S7Ol2uXWZ_tJrt59HmLaQv-YUZPUxuQRUx2KS3Y543eg6vKZCtP_zcdMQpd4j_FKCqLm_8Ufqnf1IulCrWXNXcZpdcJuEZPRMRUN54Skr_F5NcAhlHnfKdNdlhWpLcRZJsVEcaOk8m6YE3eZdcPk_SrJGrOu1nVtZ5FobXqAydWWcM7uHUUVoOjx7Q5t4RddYo67TU5NKuxpDtiX1RIIBgBTJr8v3BRaAwNbKEFNPcN_Bbym-dN2vyWiBsmtxP3ghTQLlI720RpFJ-UVOHJljDEPH3FEa-kk2qrAB5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزمایش موشک‌های ناوچه "جیانگ جیان" کره شمالی، دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131942" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
به گزارش فارن‌پالیسی، تهاجم اوکراین در کریمه به‌طور جدی توان روسیه برای اجرای عملیات نظامی در جبهه‌های جنوبی را تحت فشار قرار داده و می‌تواند دامنه محدودیت‌های عملیاتی مسکو در این منطقه را افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131941" target="_blank">📅 20:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نتانیاهو:برخی از شهرک های مسیحی در جنوب لبنان، درخواست الحاق دائمی به خاک اسرائیل را دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/131940" target="_blank">📅 20:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4sPpktLszMJN7voKkFjj3xgPBiE2r7jbfXA_xRs-Ov7ZpIfwdwbmUjNFRcDZEOw44by3MBNjY3CtMZtcTin8i9H3dtETPp78-vVPzLDd1efpNVQ6gdUCHNEZgJfVl3oXkaD2Aew8TBOkJr3RqeoBCC8qNo59yTR5QevylLJaAd-H5gfmHqphEvXKKiDYEY9k0NA8_FxxdPjMg4N_um1tj_T07OFDlBcdeDESFNo0Xdc0mw8Ygofy6wKlqlyQ40HIOUFHJ3knNxzo9n7-Yb75iqFkKezH0olTGk6ooNv9DIkGaT9Xl6QE46xgnn76dst2m9s0MWFsiWtDrbzNkCW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری Uscirf عبری
:
امروز برامون ثابت شد که فردی به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده
🔴
چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از ابراهیم ذوالفقاری نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/131939" target="_blank">📅 20:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
قالیباف در دیدار با هیئتی از حزب الله لبنان: صلح در لبنان جز از طریق ایران ممکن‌نیست
🔴
با آمادگی برای شهادت مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131938" target="_blank">📅 20:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نتانیاهو: تا زمانی که من نخست وزیر هستم ایران به سلاح اتمی‌دست نخواهد یافت
🔴
نیروهای ما در لبنان باقی خواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131937" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
به گزارش اکونومیست، ترکیه و اسرائیل ممکن است پس از کنار رفتن بنیامین نتانیاهو و رجب طیب اردوغان از قدرت، زمینه‌ای برای کاهش تنش‌ها پیدا کنند؛ اما نگرانی‌های موجود در روابط دو طرف فراتر از رهبران فعلی ارزیابی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/131936" target="_blank">📅 19:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یک منبع نظامی به فارس گفته خروج حداقل ۱۱ فروند هواپیمای سوخت‌رسان آمریکا از منطقه تأیید شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131935" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98cede34f.mp4?token=r6YaEMdDX8fNKmJ-S2NsK1jjHo81GZljbMwl93aAX2tG7Arl3RKN_yVjnYRK5auPuRmRLIjyKLye-9rZlq3pLTyK5FczGDxtapRq4hHFqhbsSEH9DTpAziEq9pFz1fDdqIycMd31EGe_ZodRR-pMmVttZhxldt-wctEW4eVYmG5hbme7ejyt7-WOB2wz8_rEvureSmkdLfg06b1uYHbjNatxGOrCXKjsigDE1VgV4QKleM5mwyQgxAeuitkmrA8ArqGxEk5LzOz5Iebfg9XlphXRvRCMKNWkj_GuOyzq3bCbIkZKPoiLUCgLpzbUqIswdfyY8FmQUYRN8Vy1Mdh3hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98cede34f.mp4?token=r6YaEMdDX8fNKmJ-S2NsK1jjHo81GZljbMwl93aAX2tG7Arl3RKN_yVjnYRK5auPuRmRLIjyKLye-9rZlq3pLTyK5FczGDxtapRq4hHFqhbsSEH9DTpAziEq9pFz1fDdqIycMd31EGe_ZodRR-pMmVttZhxldt-wctEW4eVYmG5hbme7ejyt7-WOB2wz8_rEvureSmkdLfg06b1uYHbjNatxGOrCXKjsigDE1VgV4QKleM5mwyQgxAeuitkmrA8ArqGxEk5LzOz5Iebfg9XlphXRvRCMKNWkj_GuOyzq3bCbIkZKPoiLUCgLpzbUqIswdfyY8FmQUYRN8Vy1Mdh3hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزیزی، رئیس کمسیون امنیت ملی و سیاست خارجی مجلس: دنیا باید بداند که ما انتقام رهبر شهید و فرماندهان و مردم شهیدمان را می گیریم؛ پیام مراسم مصلی تهران، پیام انتقام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/131934" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fcbb6feb.mp4?token=FWvWZrYN385WFJBVlFlwvQBirsf7El47kVbE4PzV0LEnpzQcSqwFLKJlNnrguWPeGe5qjnzsfi5nDmDfIgGHrpOFNeR5hKFondOlDZ-aRVTH6hgTaTwSQNva1FUKslEFp44ctAXqpozPBHt_vZ2Zj3xXpsnxYcLXZ9NCva4RDPwMGoeb5agMj1WpZ3f0aWlLU5Lah8MK9RLZ331v5fcq2I1gBe9yZsdYEvuI7C_RjibMDS3N4Rdb9SO-ib45B3-TXbsJGmzIzzTjduoy2QfxGCLGARMfEXOslw3C6C3mAH6qqMg_1rmtNqE2c4rsteGnjZgeR9S3rTH6JG2mFU_0Fo4oHEsDrrgFnx2GC3FQDFPqJ-l35gsiVJ8dd94PeOSW1-rRSkpFNMgVlcd4OIKw-Ehpb6fFM1qCpnJ3M14L7U10pk3bDERayzPKU5sr43U9WHH9HZREtP4LBAroM5dvBJNxSeL4NBDIxRe3hp7MW6yU8Dp-j2O76D3C-8yBLErsDBN5Je7-Hf9lOKKtCqtsOvas7BXkyPFHUHhcrmSoTkYs--Q_L0r7AqBdO2S-en0eidqmhOmdmP4g4mM7R0icqwPPWVi-8dtB5ZKJEse0uramPhdWtB_QJs0UEFytCesvNAmkM-nGyHUlGQNjD4Y4f9V2iV5EtLcDdLs8DoFqgQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fcbb6feb.mp4?token=FWvWZrYN385WFJBVlFlwvQBirsf7El47kVbE4PzV0LEnpzQcSqwFLKJlNnrguWPeGe5qjnzsfi5nDmDfIgGHrpOFNeR5hKFondOlDZ-aRVTH6hgTaTwSQNva1FUKslEFp44ctAXqpozPBHt_vZ2Zj3xXpsnxYcLXZ9NCva4RDPwMGoeb5agMj1WpZ3f0aWlLU5Lah8MK9RLZ331v5fcq2I1gBe9yZsdYEvuI7C_RjibMDS3N4Rdb9SO-ib45B3-TXbsJGmzIzzTjduoy2QfxGCLGARMfEXOslw3C6C3mAH6qqMg_1rmtNqE2c4rsteGnjZgeR9S3rTH6JG2mFU_0Fo4oHEsDrrgFnx2GC3FQDFPqJ-l35gsiVJ8dd94PeOSW1-rRSkpFNMgVlcd4OIKw-Ehpb6fFM1qCpnJ3M14L7U10pk3bDERayzPKU5sr43U9WHH9HZREtP4LBAroM5dvBJNxSeL4NBDIxRe3hp7MW6yU8Dp-j2O76D3C-8yBLErsDBN5Je7-Hf9lOKKtCqtsOvas7BXkyPFHUHhcrmSoTkYs--Q_L0r7AqBdO2S-en0eidqmhOmdmP4g4mM7R0icqwPPWVi-8dtB5ZKJEse0uramPhdWtB_QJs0UEFytCesvNAmkM-nGyHUlGQNjD4Y4f9V2iV5EtLcDdLs8DoFqgQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو:
نگران هستم که این عنصر خصومت علیه اسرائیل، به ویژه در حزب دموکرات، وجود دارد.
من نگران این موضوع هستم، و تا جایی که بتوانیم کاری برای رفع این مشکل انجام دهیم، من قطعا آن را خواهم کرد.
افرادی که از اسرائیل متنفرند، در نهایت از آمریکا نیز متنفر می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/131933" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یک بالگرد آمریکایی در دریای عرب سقوط کرد
🔴
نیروی دریایی ایالات متحده اعلام کرد که یکی از نیروهایش کشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131932" target="_blank">📅 18:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgNoSCmdHLt8tPUlIjm599Fee_EcsxvxVruHTo8I-y0Dk3BlThxAFMGAERSyfAWtQcDy0UsVMSNOMI1RuwiljmtkKxf3GcmRr0v3D9-1f4ODGaB1LzAPQQPNNjz-ZUFcPdIAEVVX_RbywQf7V4P-K2vz90j7QqxihOcHneTBlaElA8x2LOLIsIHQQu9EKWSwGniJD4mPv5EA5uWNEME0fKN6BOjnZpGZdqDDg0BWRa2Zp73ubNqX9V9x3RSwsAUAgNRsm3NtKYqjzRyQJDnf0WZSzciWchelyECQwNaemS4Ip8R7nDIOvmrwj_BHGl6jXMLfhyn001xMC6BusjBuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
پیاده‌سازی تفاهم با آمریکا سخت، اما شدنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/131931" target="_blank">📅 18:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=Vgj_EMi7zzTP5tZSefbOYDcq3Mse3Z6SIeqd1E44OLAP_ypd25x2j5zkZ-1EsVMPO-s4ev8OXivMDaKAQ24GnM-2o0OrUGJyUOCiDTut3htdGp1rRFLP4McVw5Bu9_EHApkkNDTaWDij9mJCvc8OCN92LuxFmi0ZE5xrataerPCqKTfDGV0MwDjzZRql4ZCJ6ImwqTlodncM9iNgRWpEuUGLUwmhJcWy3wWVq1RssXm2o0igeQ0TSjPBaijpmJk04IWJou0y6lh1AcnuZKMZj1u7B52wzbyrybV5PhwP41PJxYksG6W3WxIgEjVnM8qNxh20bBRS_T8VVXtY90d5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=Vgj_EMi7zzTP5tZSefbOYDcq3Mse3Z6SIeqd1E44OLAP_ypd25x2j5zkZ-1EsVMPO-s4ev8OXivMDaKAQ24GnM-2o0OrUGJyUOCiDTut3htdGp1rRFLP4McVw5Bu9_EHApkkNDTaWDij9mJCvc8OCN92LuxFmi0ZE5xrataerPCqKTfDGV0MwDjzZRql4ZCJ6ImwqTlodncM9iNgRWpEuUGLUwmhJcWy3wWVq1RssXm2o0igeQ0TSjPBaijpmJk04IWJou0y6lh1AcnuZKMZj1u7B52wzbyrybV5PhwP41PJxYksG6W3WxIgEjVnM8qNxh20bBRS_T8VVXtY90d5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/131930" target="_blank">📅 17:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131929">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGSSCrq0HkBNST6e5P1zttDqyr6t9B70ylQRsmhmAvlmZ_GXpn96EQNJ0j60Ki0APK_PMYVsYBS7Ot4wyD3-x9ijZdU9QGaD63-MDXlaYIwWXytT5im5X7SPkgYBJSPDDXmGYViKGIeLU2QlDrnnKmZxx7MG-k4g3Bo9URkE7mSCdmfLmXccXE4bYzJzqWdrFSQh65Wyh6Wx8qXupBqPE6bPIIlZL2r_cb2-rw57pvWtM7iNEAzv0ujZTHuagrIRWWzS4LundjQvW2g7LntYILnZIDRXQmsiQcg0GDDbxu_Acz-MdHiM09vMS8LvOi4NOfqXzV6hxGtO7bBaDWUscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پربازدید از نیروهای امنیتی مراسم امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/131929" target="_blank">📅 17:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کارشناس صداوسیما: آمریکا رو به افول است و کارش تا ۲۰۳۰ تمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/131928" target="_blank">📅 17:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
اتفاقی عجیب در جام جهانی
‼️
🔴
گروهی از طرفداران زن آرژانتین بعد پیروزی مقابل کیپ ورد در سکوهای استادیوم کاملا عریان شدند
😐
⚠️
مشاهده فوری و بدون سانسور
⚠️</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131927" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/131925" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoNTFo5I5SqX1--zEsn07NMclm2-zAF1MHlkyBbwBkmaCEl1Uqo8BRCAoXerMC8dFv9VuAMx0eWn-Gh6_PjWBxAnlCV4smPjk61eJQenkUFzRMl8ltc_f2mTrGOqYQVBwKz1XlDBBIQn2GMsc-PKqGyqW0NbJ23OIKjdT9YsG0OW5HqVXcruGlGv3g4NMbNHs-HLjNGRE9BB6HMqA6BcU8v4pL4vhk_pVdndheq6cz7cfjzDMdMU_s7AQSvEwC7w-NlxqbkRLKn1a-XaB12qUIPLaX9aAEpS0tPAD_XKpQDyQoVEiQ8y71Tmn0lcCTpZ4f6nYQGiagIA8Rks0aLjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/131924" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f5adc8aa.mp4?token=bsI-OpdD_O0YEREtRUkJQ4l-bLW0NFtlivmiNLYQn0LypN6AaphzZjZIrO6VCDylohbLZFt0Q9pqy282hBh7bId_0_mbEpXX03aCo5QQUoN9q9MYRxp6d4QUIrUUg1S294-Bhke-N89JqWW9lFBvAcqMape8BIwfWS_okzIoqmFCTx0U00PKisF9spyc7rkcKspjVJ5J1PpPF3EnTQthkvVgQLfu8ct6eJ0DoP8ocnDcORCbKRFgL6m7vzpFviMqcN6qfWP9FPNY7X2lOznXxYYf0vIdvf4rYn7l6RfbvFTCAak5Q1GmpZEwRjsfPgqrt8G9w6fqtoItDxa28VUlbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f5adc8aa.mp4?token=bsI-OpdD_O0YEREtRUkJQ4l-bLW0NFtlivmiNLYQn0LypN6AaphzZjZIrO6VCDylohbLZFt0Q9pqy282hBh7bId_0_mbEpXX03aCo5QQUoN9q9MYRxp6d4QUIrUUg1S294-Bhke-N89JqWW9lFBvAcqMape8BIwfWS_okzIoqmFCTx0U00PKisF9spyc7rkcKspjVJ5J1PpPF3EnTQthkvVgQLfu8ct6eJ0DoP8ocnDcORCbKRFgL6m7vzpFviMqcN6qfWP9FPNY7X2lOznXxYYf0vIdvf4rYn7l6RfbvFTCAak5Q1GmpZEwRjsfPgqrt8G9w6fqtoItDxa28VUlbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زینب سلیمانی: شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/131923" target="_blank">📅 17:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/131922" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG8do3khQe8ycPn9jRUd6adyGPvpeJovEaxisZUKuncKyXvm2l87Ui6Gkb6Scj3bWTxglpYBa4ety0LxUxBEA6cgVJjmIYasO0fGj2PfFaRXHu8hg3fGOa5YfUcMKX4-0wP2mF8X76wF33dqg7vApr29F_rtJ2g_FTxurpNKu6n5Uf3gqM8urp3cgwhmjIpHms-CRyf0qb5YuTbFcm-oWkTAEXxZMBYFgy9Pe7SHXalBBMXVyfZ9wS0J1h0AaYbFEDwoNWrwE4PYx-SDaPLqTSMJhLV1VRd0jk_1EexbqfaFP8BZr0GV9lx1SYLihIsYIOW4YbZ84IaTyHAVyxALTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حضور سردار وحیدی در مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/131921" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d57f1ea3b.mp4?token=k8XOdW3YlgXpuvgUrdqmaF1a4eGg0wxSb0NMkMM3eCNLkvi5ANXpEz5P_2gehjD-uzi85M3t3MVo6T7N6ObdOgFD2-gi6cZcKhqHi4w_tjmjB-Dy5INIpW81E3aNsWa5uE0ibrUBKkv0kFLSBs66a5pCBpU9CK5cYNnDY5QhvnknYyzGPHHxLiRnmsbAOxNEE9tTGGotpgC9vSrLPBG-WYaXP1AUeIuo32BGw_-7QefFcIK4vn-NlHYHt_NMbKgLEnQ5faUc7jjxbAKBaAANhC9SLb3h7CxOvLM-PBzR6Rj00Dy33TJXGpQxaItMEaZzoUv02PJJkvjv3rYoA3tOIWzFdFL_wwGSMKiXAebIB-40-jVNBVxbNSY572U6k5okFK6wXkOLOoAOeyW5vEY-DloE7e9WacOYmxGfeuapZInjx0A8Be9iMBT78M3K6y8Mmuq1Pv7pikyg3VfI0RxdnJ-rvLAh0Viimq0afM9Ef25ZslWDV1ShM9Gg79Wshz000O7MDuCOJDmYVTYukA94DGVLb1HfxVCrd5NEtJbLzKSxYrDyYTbcEZ_X_z_H9-bslm9ODrZGtofFPKOHXOx_oUuZsHmTizJ57RMpRqe-X5qs1mJq9yRSBL0JncAByaW4aLiwyEBgw6ZE3qlN8wQGvLzCju4z_s6Wl_qGprlZIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d57f1ea3b.mp4?token=k8XOdW3YlgXpuvgUrdqmaF1a4eGg0wxSb0NMkMM3eCNLkvi5ANXpEz5P_2gehjD-uzi85M3t3MVo6T7N6ObdOgFD2-gi6cZcKhqHi4w_tjmjB-Dy5INIpW81E3aNsWa5uE0ibrUBKkv0kFLSBs66a5pCBpU9CK5cYNnDY5QhvnknYyzGPHHxLiRnmsbAOxNEE9tTGGotpgC9vSrLPBG-WYaXP1AUeIuo32BGw_-7QefFcIK4vn-NlHYHt_NMbKgLEnQ5faUc7jjxbAKBaAANhC9SLb3h7CxOvLM-PBzR6Rj00Dy33TJXGpQxaItMEaZzoUv02PJJkvjv3rYoA3tOIWzFdFL_wwGSMKiXAebIB-40-jVNBVxbNSY572U6k5okFK6wXkOLOoAOeyW5vEY-DloE7e9WacOYmxGfeuapZInjx0A8Be9iMBT78M3K6y8Mmuq1Pv7pikyg3VfI0RxdnJ-rvLAh0Viimq0afM9Ef25ZslWDV1ShM9Gg79Wshz000O7MDuCOJDmYVTYukA94DGVLb1HfxVCrd5NEtJbLzKSxYrDyYTbcEZ_X_z_H9-bslm9ODrZGtofFPKOHXOx_oUuZsHmTizJ57RMpRqe-X5qs1mJq9yRSBL0JncAByaW4aLiwyEBgw6ZE3qlN8wQGvLzCju4z_s6Wl_qGprlZIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وحید خزایی جلوی سردان رادان میگه ترامپ گوه خورد وطن فروشا لاشین بعد مثل الاغ ماده میخنده.
🔴
پ.ن: وحید خزایی سال ۹۳ تا ۹۴ یکی از بیشترین پرونده هایه سو استفاده جنسی مال این فرد بوده و بعد از خروج از ایران دائم سایت شرط بندی استوری میکرده
🔴
ویدیوهای متعددی نیز وجود دارد که وحید خزایی به آیت الله خامنه‌ای فحاشی میکرده اما اکنون ژست دیگری گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/131920" target="_blank">📅 17:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgVaDjZrJy92gyjHSv5YSidaTm245p-2JMjIdH3O-wdNhCI6PKNXNvtJ-G5TxavPvG_G4UUdce5Yqn02izsPxuTcPFp0gRZIysG5eOY4EMhiciMUyv1Xs9nLspj3iIsvp1Oy4XUa3z5uvmtmCHmOAP2ByCLBwz9ALNTstLyshiDYNmnbPh0Fj3KVb3XgFv3bafmSKbgaXd7ySuTwbiKOcdhAJ9fVNk2GVBkS--GiJetz0EXAULyO54lt3bq6CiSkoORhSUQZ-r6fIf1akcLPyTGQmm4WYbeQwSdW3rooVFk17kOajlse5Fn0a2AVcJyRgl6SNSA_nb-bhSwoOyvkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر برگزیده رویترز از زمین لرزه ونزوئلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131919" target="_blank">📅 17:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ : ما بهترین بازار سهام رو داریم، واقعاً عالیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131918" target="_blank">📅 17:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فارس: کارت ورود به جلسه امتحانات نهایی، تا پایان این هفته منتشر می‌شود. امتحانات نهایی قرار بود از ۲۰ تیر آغاز شود که با یک روز تاخیر از ۲۱ تیر آغاز می‌شود و کارت ورود به جلسه این آزمون هم تا پایان این هفته منتشر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/131917" target="_blank">📅 16:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل:  اسرائیل باید زیرساخت‌های ایران را بمباران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/131916" target="_blank">📅 16:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
از سرگیری تجارت دریایی ایران و قطر پس از حدود پنج ماه وقفه
🔴
رایزن بازرگانی جمهوری اسلامی ایران در دوحه از بازگشایی مجدد بندر الرویس قطر به روی کالاهای ایرانی و ازسرگیری تجارت دریایی میان دو کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/131915" target="_blank">📅 16:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/131914" target="_blank">📅 16:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بنیامین نتانیاهو: بازسازی غزه بدون خلع سلاح و غیرنظامی‌سازی در مناطق تعیین‌شده،امکان‌پذیر نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131913" target="_blank">📅 16:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نتانیاهو: ایران می‌خواهد ما را از جنوب لبنان بیرون کند و آنها سعی دارند به ایالات متحده فشار بیاورند.
🔴
ما به خوبی از پس این فشار برمی‌آییم.
🔴
ما حفظ منطقه امنیتی را از دستاورد بزرگ خود علیه لبنان می‌دانیم، اما آنها سعی خواهند کرد از هر طریقی، از جمله اعمال فشار بر دولت لبنان، آن را تضعیف کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/131912" target="_blank">📅 16:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344ee59971.mp4?token=Qyv6M0vZjY_L-xsqiKikwaFoN34fS1qBPrbVMfRjnI2ffvKbkKscS4r4rExUGmyncE_029cyMggscfwXlTf3dHf-v-4MezGozd_qasaiRTCHzeD__5DveactGjX9vDzcSXHIh4A3KSjjEJX_CiFQcqGItNUeQnPppZSJ7hvMRKTz6TcRfLrUWtXzDumhZQMmwjF8gDWEXT0oAGNCPL13uZAE9-5VRmeSyw3SB4obG8U6qzgQ_dfBQ7oHFYW49jO5TTkWwK723eNB_omK75l0Hu721r2o-Sdo1s5GYIBIPYgPFn4SBtIA-QLahBbFKqTvRG7VGjQW4Byq_S4OQr6Cjb9vxIMd4HKfh2p57dNkOH9gl7yy9vr-a4OAZTi6DKol9u8JrwITB4061KlqIcQ1cQGCUYqflwfwlVkRP2Mg26yACjXPFL9VXtiJlg6vNjU9-PUq9pESbSDPmCL6ujm2_0JEOZj9ZDVvXl4NyfNiUAd2AIED0DmzzEk0urrY5rpsLYNkM4BgzLsWTtt4w15wtbIUreI1aeS0Rsi42IZ_05ZaE08WjBaJAvV0AkLgxkCUDq4UDPXpZ7seBTib1Fbey3m7SxaddU-TWLrylEyCLyV-JsV0hLJGSCqDVKra6Tsc5WqWZzTEc2saPgRtR2dSsdJMe-oeN8oEZfI6X18dvu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344ee59971.mp4?token=Qyv6M0vZjY_L-xsqiKikwaFoN34fS1qBPrbVMfRjnI2ffvKbkKscS4r4rExUGmyncE_029cyMggscfwXlTf3dHf-v-4MezGozd_qasaiRTCHzeD__5DveactGjX9vDzcSXHIh4A3KSjjEJX_CiFQcqGItNUeQnPppZSJ7hvMRKTz6TcRfLrUWtXzDumhZQMmwjF8gDWEXT0oAGNCPL13uZAE9-5VRmeSyw3SB4obG8U6qzgQ_dfBQ7oHFYW49jO5TTkWwK723eNB_omK75l0Hu721r2o-Sdo1s5GYIBIPYgPFn4SBtIA-QLahBbFKqTvRG7VGjQW4Byq_S4OQr6Cjb9vxIMd4HKfh2p57dNkOH9gl7yy9vr-a4OAZTi6DKol9u8JrwITB4061KlqIcQ1cQGCUYqflwfwlVkRP2Mg26yACjXPFL9VXtiJlg6vNjU9-PUq9pESbSDPmCL6ujm2_0JEOZj9ZDVvXl4NyfNiUAd2AIED0DmzzEk0urrY5rpsLYNkM4BgzLsWTtt4w15wtbIUreI1aeS0Rsi42IZ_05ZaE08WjBaJAvV0AkLgxkCUDq4UDPXpZ7seBTib1Fbey3m7SxaddU-TWLrylEyCLyV-JsV0hLJGSCqDVKra6Tsc5WqWZzTEc2saPgRtR2dSsdJMe-oeN8oEZfI6X18dvu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ  در حال تماشای خودش در فاکس نیوز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131910" target="_blank">📅 16:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
آلن آیر، عضو تیم مذاکره کننده آمریکا در برجام: برای مذاکرات واقعی میان ایران و آمریکا، باید به گفت‌و‌گو‌ها زمان زیادی داد
🔴
به افرادی نیاز دارید که بلد باشند همه ۸۸ کلید پیانوی دولت را بنوازند؛ کوشنر، ویتکاف و ونس؛ این‌ها سرشان شلوغ است و مشغول کار‌های دیگری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/131909" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9e3c0b51.mp4?token=VApz3PPif8u1NmhuZlSEVH3JCky4DrhTfCNvNfv82oMcqAqLiDPgtgpUSM5jEC_SxsB4KqOES_Y_C4HxMmdOkdxs7PrWdhXEdgPJLbSf6haA-lzMHihHnIu2NbuRqfyeiTbb1Ygq1ctWyilD6NJVqi-zb8vzH05cVhspui-95Orl0xeJK75hlfR5ZmZwWLUoRSRfIajolhmpsP3PR-Lhp2EegsxOJ8H71SJL0vF_PLftYkvWebkR9ZMe7_sirzHS6OBdevN4eMzVsVkuVyVcEhpuz3K1LWAD7_52AflyeDh5TYI7FvFkcD-qj_fABCGIVq8mLCuTehum2kIVhtGipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9e3c0b51.mp4?token=VApz3PPif8u1NmhuZlSEVH3JCky4DrhTfCNvNfv82oMcqAqLiDPgtgpUSM5jEC_SxsB4KqOES_Y_C4HxMmdOkdxs7PrWdhXEdgPJLbSf6haA-lzMHihHnIu2NbuRqfyeiTbb1Ygq1ctWyilD6NJVqi-zb8vzH05cVhspui-95Orl0xeJK75hlfR5ZmZwWLUoRSRfIajolhmpsP3PR-Lhp2EegsxOJ8H71SJL0vF_PLftYkvWebkR9ZMe7_sirzHS6OBdevN4eMzVsVkuVyVcEhpuz3K1LWAD7_52AflyeDh5TYI7FvFkcD-qj_fABCGIVq8mLCuTehum2kIVhtGipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب منازل در شهر بنت جبیل، در جنوب لبنان، ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/131908" target="_blank">📅 15:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIjFN3chXuS4nnxA0jf2BQVw4HvbGU6YgDvWY-pLY3kbcUbhaNQ6qsSkgjx1B6P0whAyXuBearrPJxSLhIebUXwKoYy0UMhCTjWa_Go8NrYf-247AFI_w8pZC_ALleh3rXkcalLSkNhnSs_sjrlMfEy8TvOxalczcVgNtmMO1pr_rbGRIEYd2LdQmUmqwPkuJWCsfy-xX0QuffwKshCsKTjgxr75Z47fn5jpMGoy3XeoOjczq2-p3r6goCZoGwK2DpNrgVqP-Ylo7Kp7al4Xeq1j2Fyi3VZb0xvHAyOC5Iy-ktVNakA1mNuM1s21MsHR4nQCwm-wRxNbNfZXhke3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی در سواحل یمن مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131907" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
قطر، تعلیق موقت فعالیت‌های دریایی را لغو کرده است، که در نتیجه، تمامی فعالیت‌های کشتیرانی و عملیات دریایی فوراً از سر گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/131906" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131905">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ریاست‌جمهوری سوریه: امانوئل مکرون به‌زودی به دمشق سفر خواهد کرد و یک هیئت از سرمایه‌گذاران فرانسوی در این سفر، مکرون را همراهی خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/131905" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnKNnkoZ-xwmjS871pyCEiLXIUN2nyn_ifhzk1R07M5gNolLb9hIU7CzsNXYT6fqly_G76-WIIViv56v84li4uDkR4Ijg-LDC1887dGVrtMi-W3b8Wl6f5815scWD_UktZgWcImcyivwoxnsUU7f8NVdyel3YwojU4BWKO8etryM4KjkByHtQmcKa05-LIcxyPq222DsMm2pCDogZQv_XdnU_2J1aRZQULus5EXRzRWTBNsoQQX7hu4XcxTA2QTRZTZNuglT4LX9e3gg31rVWmR8hS1g9cTbrhoH8zKF1DhrlMffe-J7tmJN4Uyl1gF_YqrNqyRIL-uiFwhLOriogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ در تروث: از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131904" target="_blank">📅 15:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل: تهدید ناشی از غزه برطرف شده و هیچ بازسازی‌ای در این باریکه بدون خلع سلاح انجام نخواهد شد. به ساکنان غزه آزادی انتخاب داده شود تا میان ماندن یا ترک تصمیم بگیرند
🔴
ترامپ از ما نخواسته است که علیه تونل‌های حزب‌الله اقدامی نکنیم و برای باقی ماندن در امتداد «خط زرد» در جنوب لبنان، مشروعیت لازم را به دست آورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/131903" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سفیر ایران در چین اعلام کرد تهران پس از پایان دوره ۶۰ روزه توافق اولیه با آمریکا، برای کشتی‌های عبوری از تنگه هرمز هزینه خدمات دریافت خواهد کرد، اما کشورهای «دوست» از شرایط ویژه برخوردار خواهند شد
🔴
رحمانی فضلی گفت ایران همراه با عمان در حال تدوین سازوکارهای جدید برای تردد در تنگه هرمز است. او تأکید کرد مبالغ دریافتی «عوارض عبور» نخواهد بود، بلکه هزینه خدماتی مانند تأمین امنیت مسیر، نظارت بر عبور کشتی‌ها و رسیدگی به پیامدهای زیست‌محیطی تردد دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/131902" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فارس: قایق‌های سپاه 6 کشتی رو از تنگه هرمز خارج کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131901" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
کدام فرودگاه‌ها فردا تعطیل هستند؟
🔴
در روز ۱۳ و ۱۴ تیرماه پروازها در سراسر کشور بدون محدودیت انجام می شود و برنامه پروازها به روال عادی ادامه دارد.
🔴
۱۵ تیرماه همزمان با برگزاری مراسم تشییع آسمان تهران به طور کامل بسته خواهد شد.
🔴
۱۶ تیرماه نیز فرودگاه مهرآباد فعالیت عادی خود را از سر می گیرد و فرودگاه امام خمینی نیز تعطیل خواهد بود.
🔴
۱۸ تیرماه همزمان با برگزاری مراسم تشییع در مشهد، آسمان این شهر و فرودگاه هاشمی نژاد به طور کامل بسته خواهد شد.
🔴
در روزهای ۱۷ و ۱۸ تیرماه نیز پروازها در سراسر کشور به جز مشهد بدون محدودیت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/131900" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
روزنامه عبری معاریو در گزارشی مدعی شد که دونالد ترامپ، رئیس جمهور آمریکا، برای برگزاری یک دیدار سه جانبه در کاخ سفید با حضور بنیامین نتانیاهو، نخست وزیر اسرائیل و جوزف عون، رئیس جمهور لبنان، تلاش خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/131899" target="_blank">📅 15:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MH2gE42aapoMYifafvM8qR3Vk-d_84TA3eZMXI8j8BU7RPOugEQcE_onjK5ZTLCcLiulUrtkklnJWF6A_-evfpDUbdYiRCta8tcAkw69uUzLBILJpl2pzJ3FHtEnbi7CgS0z8m0HOwZaS2V606erdFEKOifX2KNuAS-qdHKGM9laklW_OU81vzc0qsSABTAfrOwmNqSkX6pmuKc-UcA2Zi_mdq7hxAnhNk_7lmL6EfZAkNjQtFa_Afo2qafB_Oy1nNHSftqFm8RKyC6ewCpbpqypfA7QS3OeD0Y98GgVlPYb5WswYnRjDF5EEWRXFrozQHcqvVNvCCBZXHBjqxkDtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49482f3e9.mp4?token=MH2gE42aapoMYifafvM8qR3Vk-d_84TA3eZMXI8j8BU7RPOugEQcE_onjK5ZTLCcLiulUrtkklnJWF6A_-evfpDUbdYiRCta8tcAkw69uUzLBILJpl2pzJ3FHtEnbi7CgS0z8m0HOwZaS2V606erdFEKOifX2KNuAS-qdHKGM9laklW_OU81vzc0qsSABTAfrOwmNqSkX6pmuKc-UcA2Zi_mdq7hxAnhNk_7lmL6EfZAkNjQtFa_Afo2qafB_Oy1nNHSftqFm8RKyC6ewCpbpqypfA7QS3OeD0Y98GgVlPYb5WswYnRjDF5EEWRXFrozQHcqvVNvCCBZXHBjqxkDtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور ایمان تاجیک، سخنگوی جنگ ۱۲ روزه، تو مصلای تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131898" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل: حزب‌الله از توافق ایران حمایت می‌کند و توافق ما را مورد حمله قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/131897" target="_blank">📅 14:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سفیر ایران در چین: کشتی هایی که از تنگه میگذرن باید هزینه ناوبری بدن ولی برای کشتی های چینی تخفیف و ملاحظات خوبی در نظر گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/131896" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
