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
<img src="https://cdn4.telesco.pe/file/jW6S-yCiFaKFmxA6l3b4xDlSAI0NDTvuToXB99bn-rwSRY0DCw4KkswGTKG-TYHbPE_3nkr69dqX6pKg6D6aGRQSUwghNo9Zi7nbr2dt38UBQr-Qh8bj1Qrt4XDC_F_tBebH10Kcpwyx3NaPml8yLjpUEeLcI1MeNG7nZqoWT9vEK7jSoUZp-lhYlXCI9hXQgA-62GScjRlZlJFUgs58QMfaPsD3zdJ43VlwSgx-CyXVz8pf3FQuUjz_4ECkSIwWr46UbJe7Dxy_tTuSyCIUbDy9q-abTSWO-t3BWmdIJaKHbxCI-PrUKuFWD6vHlIJhh48VpIwqoh1gC2aKCZj9oA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 16:54:32</div>
<hr>

<div class="tg-post" id="msg-126527">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/126527" target="_blank">📅 16:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126526">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/126526" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126525">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6oNjj1nnppyGmWZhybHRw0z6iWIJO0yWKZB2_fhwSPvb5AMgALs8xA1sFekye_5UTDNYkZxm2IoRriae45v_Mw41w12tay8isfP1QgsZ7aBUrbvTfgFKzYEoocFRwNGFjsJd3ZQifywIgHrnEvyV5OJ3eZLtp3hIlB4267_Kve8b7_aHfUSrYB3AF7R4JTae887ImE9aReM7SKMAm6xjBVtPLDxZJa9irGN8VitbuygyxOel-odaPzKvkyuvOtTMX07mr4jYhWDkCY42CWKh3N2piwgdWip4z8VYgOpNDNvBq_cH1sh9TIdpDb-RySnFLH4LQWK3QXTCNTboVCehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/126525" target="_blank">📅 16:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126524">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR55R6RIrmA8wUoyZxg4jue2m1zU2--6DY2Y_LLaf3saYnYVI0a1cC7IlaYb9TGFLlm6dy0oUWYksZIBul8PSai_zWmfeYlrQ4GcjogrsPN47uhUFL-eiJ4MNZUozJSbTGa-hgTogId31Q6jsepBjS_UP3gIo64j2WATFFk9IwbYu4KqR6Pzuo9Rw0aNgOSyS-sVmKHHOqaJxZhsOEhHrVbpskbzQj78sAq7i-K6pCjEIxPf6jzYE4PH4osRLbctMM1JatuWCxMJCkTyENqfs2auLf2Pc42ovhSmEiaeGqqvnZ1MNJRuVaYpKe2UNMPADE_YPKv6cilulZRY-nhFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/126524" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126523">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-HBinKNcpae9RBU4rslVbFzvdxPAXwZR6QDcoa6ovpk0cdLObXpfhfXPCtQvRsWOnWp2elNaIwkpDCKA_OhPwLxSZQAL31oj0ep2VxuFqV9nmrBrK8xJvAcioZ1L18mIkNigfTUaZX2579iBFzwqw5fc6MAEkA9TJ6VenaovjCDCEGUC-IFH-0kncYokT5EMQ8fi-I56G_HplVfbFjmQZldrJWl4UHcxAmor34GyjIRHxyDGNK5x7FdIUMQ-uXH22QK6OUn9nVWXpMwP79JOycP2g1qTEpreXmr9svEgjSVJchqGQzeRZaENI6HLPRsI0v6BOYV3LTsvOTcupEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/126523" target="_blank">📅 16:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126522">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حزب‌الله ادعا می‌کند که با حمله پهپادی به ساختمانی در تلات الصلعة در شهر قنطرة در جنوب لبنان، یک نیروی اسرائیلی را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/126522" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126521">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به شهر عین بعال در منطقه صور در جنوب لبنان هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/126521" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaW-Hws7SD9TKgW1oibbeI2cqaYJg8MYEbc9E2vX2evyBWTEyoCNq4X7yAYEyEfyrsmjf4YFnKXFyYgZupOIaSDwoGQAb2MC-abVp4GlLpAfIdhqCMbEddXiT-7GfcJ2FYZTKSbLnTX2uVrztILBK2Z2r7hNjqWl-CW3oGNGb85x4Z2w_WuM5FQeqVivdnS2je4SOrFmv56ZKcytgSJRxC-h4eE4ZtNL2mvSSvvKioV-M2n_GVZpUStWZwdOvdbZvrw1Ivl-bwPln7D9xRE3p3NtvfxuF5m58pESWS5QY5d3h3y8u-xAnauJ6v3BNWBn9O8mqOlqWDx2KdIUxB_emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه و عربستان برای بازسازی خط آهن مشهور حجاز به توافق رسیده‌اند
🔴
قرار است این مسیر ریلی به عمان و بنادر اقیانوسی نیز متصل شود تا به گونه‌ای برای دور زدن تنگه هرمز هم مورد استفاده قرار گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/126519" target="_blank">📅 16:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت دفاع ایالات متحده ۴ شرکت چینی، علی‌بابا (پلتفرم تجارت الکترونیک)، بایدو (گوگل چین)، بی‌وای‌دی (تولیدکننده خودرو) و نیو (تولیدکننده خودرو) را به فهرستی از شرکت‌هایی که گمان می‌رود با ارتش چین همکاری می‌کنند، اضافه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/126518" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urjz2ho2LbimJNi77Rz0ivogBS-yjiNBCkV1WCsSuriFIH_jL6fyqp6tZaQcxsX-Udvcc-iMofWu6z0rFMWIXhyiaSmjxsuP8VQiGCnwNYDbSMlK0UlvCQm21RO493wUg_ytYrNWZCpal2MMcxQA2Z6p6-IPBuSlfud4WDdivZE8fKbVTNkUatMiJnZqyGMc0JXRzT-OvzLRZmjQh0MR1kdrcr4lYGZutsWS527XQ2G3v3jV4Xasa13noK5rD0LqMQ1lq2y4IbEoZK50ah_TiOSHNPJLtKjfRJ_7vA4DVjQRNfF1dbKTbQcYLnuBolQvjnZOhJdj3PqbSHxum2WcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عدالت اداری شکایت برخی مسولین تندرو بر علیه رئیس جمهور جهت تشکیل ستاد راهبردی فضای مجازی و آزادسازی اینترنت توسط وزارت ارتباطات رو رد کرد و به نفع دولت و ستاد راهبردی فضای مجازی رای داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/126517" target="_blank">📅 16:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QZ_bqrGMAKoa5oEq3RbYTy8zBsZkFNEt3b9c9A7OQn9YPsa56yk0glBJnitHMW4vyxECcN5K5zieYQFc1tqtUVS9DVxhF0ZIjjHi2sLJSZRL5VDrT5-kNEautLWPzNHoAxV9OMISn8onBodARQdiji_u4XQP2JsJKxT581GT9MmXUIBxikbNU8rFKNj-IcxLqGlAoB2JA04jt-I2am4yirM1tOwauMVTtkuLO066A4Ew60iCj7QsSfVkTsnWp1w7GxB9UcSRVwkp6D44lhjuyCqZFNMKlX6DK9TmDW4s-yBI3gEOoJJ4EE75vxnPDm1pCBLD5odvfY9aUcdKDSbxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BfRpcIc99y8Ml0NZLgEHhTLMa9ccI_GmbBobq-5tZPweb6kyjKa56GHrpUq0LZpxxUkdMZ64qj8v66zE0mW-nVXtEEBNmUwrZMVVs-fq3xDGfbI7PFeu9qTorcxF28J_5DhhuCNEBRCgBimnIgym484uvTeOew0gmJ472xXCELVXfnzL_zNy_K474agvS4ERQf-eeVo8vb6O5bKP-mEdUwA-xcnRp_1FMiPHwU335Adwy8zNI8HSPbMaOa3g6gUteywQzzQbeCZYxmrSeCEFXB-ZVg2eD5z7yz-TIsnv0nvEFO2X3CPPYRwOx03Xr_ipi64sTkq-7uvnPeypIb6Myw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا امارات صادرات روزانه ۱.۵ تا ۲ میلیون بشکه نفت خود از طریق انتقال کشتی به کشتی که نیمی از آن در لنگرگاه صحار عمان انجام می‌شود را از سر گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/126515" target="_blank">📅 16:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بر اساس نامه شرکت مخابرات ایران به سازمان بورس، این شرکت مجوز افزایش ۴۵ درصدی حق اشتراک (آبونمان) تلفن ثابت را از ابتدای خرداد ۱۴۰۵ دریافت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/126514" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE-5IsfXj2f9WFSYBYjIorOdDgladtuj6NC24_ERr3Jo909X1RgZtibVnldr6EAWnXMqYNPMN51VgdKz3kwKuC9PEpE4gpgpt5mmglT2t8Kb6_wjdVzvPPdZRKDj1T0ncphoqDDUQIRv4PKnzHfDPNry6E1EvjqOsazAvphkUZAhFfwItOXwbnXaZv9cM42sd9-6PGNxC034iszTg7Rxp-Uc2NrZlD-lbKdwKXbLbyWZu7gHQiuuEwct5R83EZJM8P1IhrPBHCp_XIifdMICeytBDhMSENi8O5HKbiHk5bWZbDqiifsSGEznj3rYeFGXPPxFrNpxXUrOJpAhlTq9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا کاهش بیشتری یافته و به زیر ۹۰ دلار در هر بشکه سقوط کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126513" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2vD-cbY20LbkO-Wb-zO0UHOUi5mK8dTtBrvxvH7jeqMOf6JgcIK0HC1XC6Bqm5Xb2GQSmfPQaFgXT6KwmZTIzn18Uxw0T4C4NFgzeruUGsJqYXeOHh5Ov-I_-43r71Um0A5T6khEFdtwP7poh_-Di0zUYsE2dRkg26ZZpZDrdjeMoFf1E9STAGVoWBcJiGByjqm19sCz8ImlxeJgjgDj4i5OynHkwyHEcqGZmD4vODjA4wyT2OlgJbcXQqITUQKggl80eefrGtzHfbnCZGgX70ah9Mj4MwgV50FAwxBq1yQj0f2ZOdmR-MJSbG5LV9NgdpstZURBjBcTRsZOlUmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز مدعی شد، یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده (USV) که توسط گروه ویژه ۵۹ اداره می‌شود، پس از سقوط یک بالگرد تهاجمی AH-64 آپاچی ارتش ایالات متحده در تنگه هرمز، به نجات دو خدمه کمک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126512" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گفته اسرائیل ارتش، یک فرد مسلح که از لبنان به خاک اسرائیل نفوذ کرده و در منطقه رامیم ریج به سمت نیروهای اسرائیلی آتش گشوده بود، به ضرب گلوله کشته شد.
🔴
ارتش اسرائیل می‌گوید در این حادثه هیچ مجروحی نداشته است و نیروها در حال بررسی منطقه برای یافتن مهاجمان احتمالی دیگر هستند. یک پهپاد نیروی هوایی اسرائیل نیز برای کمک به جستجوها به منطقه اعزام شده است.
🔴
به ساکنان جوامع مرزی میسگاو آم، مارگالیوت و منارا در منطقه جلیله پنهندل دستور داده شده است که تا اطلاع ثانوی در خانه‌های خود بمانند و یک بزرگراه در نزدیکی آن به روی ترافیک بسته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/126511" target="_blank">📅 16:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-wIfqIy9l7hQqttKo25mt_E3eufz7GWKW7MLrbMkgbd_W3p93MMG90cyrtjNtRQ_yOQRP52aI_Iv1iW6nir3SVZzAT6Kr5IVcy1CUE5uJlknxOIAreZXPpQF7dXqGXiOkHNfIYCAxvV4JjiONNRnRyWTgTEH7F-d7Az9sedN8s7ipfvleLfXW4hoyVY2E6hAJOYefjQKetASd7uPpUQtq6xj0XC7xJinkjQKqz6_LVFG6jZOz9U-WuUo-OyR1DpaGYkErVt5Si72hZw2QmEW3WQ9-1F21IBiqFDzxn_aCYAjMRBLl7nxRZNTJ0wPAw5OPIeVPWtpqs_AxCMEenw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEcTAovwx2IPu7yZEQ9T-RWzQCIJGjPxqOECwO-zR_YRcJ0Qz5wDZDip02B10mQMEmVmsO1igppFyYOR3jZstqjOH9HM6phd22xYAU5hHH895p9vnh0Qsha_aIMFDbChTbdS49TG56y_RGimT23ZgFkZ90os50hqL0VZeoKpAl4iz57JdZqyi9W7TSsivUHPHbyJYNkeLsB08yQ3Zbc43dck5TSzT4TAkifUI0i3zh5hTQ_wY_iw2hjhBscy3wdO0M4Uphlcmy5UibAl5KoEH-R9qJfjCNjILM4ouK18nmh4nY7PPwuFdHLtPdEJfy_21vszF_aNYW-wieBmXcoJsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زبان ترکی به سوپر اپلیکیشن بله اضافه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/126509" target="_blank">📅 15:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزیر خارجه بریتانیا: با عراقچی صحبت کردم و به او گفتم که از سرگیری درگیری به نفع هیچ‌کس نیست
🔴
از اعلام توقف حملات متقابل ایران و اسرائیل استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/126508" target="_blank">📅 15:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nmcDRzGep6wbX2QfCjqD4XSIr3WIJRgikDzQWK8sR9cqbK6utRNiG4z4vK0u4wCGPaMJbaMyd2-Jsg2zV87PhEpeyxQ2g8rsb1R_SmljE9rDMUDVwhXtJJ0FZIKE-pVd_xl4UnSB05d33eh1AYh1rs0r3QJRTNtizcX3eryBH1PW4pO0Dv7yyqa0qb3sL4vIvtstCBMkkec2TFKT7Fk5MCruybBrh0rPe3ecBUxE9jfMHeko9D_sVTMOrnXbneNTgJavZc1lVL6zgPDmOixkHAVoSFWPijeZpNNua5DBrGT88GC8V9d8faS_LF0I_TaI8sgDVgoZxq1GYiexAXGVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-SATOAunGhpERV1rR9MUe3_2VZZSYa8E-DbbviPtM2Dyk2IATTAxmoyW8JGdRsugCWh6b-2CCGemy_wO5DJih0FW-OL4G5LCiuxQqEvZYYtoaWMFgXiGo753v9SGjqA8dFk31mSLJg1uz_jwSf8X45kXe3zORWu8REzLYxp4oRPHuqIFJqwGMjgK8A-C1xOSupgTAu1HLRV6qYLS1fwToNjOUzw-Hr4NqMxdwcm0toH3QQetfGBPCC13tFvc7GoE2yEUcHtDCTohx5vjpXdtJO7SOV7tW1-lN18RbT01vFUzKmsYjadwIcdzpELe4g-GXPvBagM0EvXIx0yFIxVOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=KJr_KuZAONYR-FhbqJuoUe2Ob7mf7XGL_3QETLrw-nH-LzYaMd1wsuTdVZUnR8zY85CJRhcd0FcHHk4NDTQcRqxakSx2T2jqGMO8-d-IPOZSHoJT_G9ylkWl7EQFhD4LXaiyNscS2CkymHa4w5HmERLmOyiL7dhXafZ1cDrEe22CB9x-7IjlwembzvCuWp2F9XV2j85vX-8d6f3yuZqa3EKGHheTiywP4yXnA0TVlHoXsBVENg03M1dru7PPpD2rkbMrCNA_Vz84ZgOEmeWzGt8XD7RcfA3VW_YgH4wOnu5BOyzw6h6rn0I6VnlxRNQ0bUITycfqDEXAtzVusTvmnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=KJr_KuZAONYR-FhbqJuoUe2Ob7mf7XGL_3QETLrw-nH-LzYaMd1wsuTdVZUnR8zY85CJRhcd0FcHHk4NDTQcRqxakSx2T2jqGMO8-d-IPOZSHoJT_G9ylkWl7EQFhD4LXaiyNscS2CkymHa4w5HmERLmOyiL7dhXafZ1cDrEe22CB9x-7IjlwembzvCuWp2F9XV2j85vX-8d6f3yuZqa3EKGHheTiywP4yXnA0TVlHoXsBVENg03M1dru7PPpD2rkbMrCNA_Vz84ZgOEmeWzGt8XD7RcfA3VW_YgH4wOnu5BOyzw6h6rn0I6VnlxRNQ0bUITycfqDEXAtzVusTvmnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز چندین حمله هوایی به صیدا در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/126504" target="_blank">📅 15:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز بلافاصله پس از امضا باز خواهد شد، که ممکن است در دو یا سه روز آینده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126503" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سفیر اسرائیل در آمریکا: می‌خواهیم جنگ را طوری پایان دهیم که تضمین شود ایران برنامه تسلیحات هسته‌ای یا موشکی و حمایت از نیروهای نیابتی خود در منطقه، از جمله حماس و حزب‌الله را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/126502" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله هوایی اسرائیل به شهر نبطیه الفوقا در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/126501" target="_blank">📅 15:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
پاریس:  ورود بتسالل اسموتریچ، وزیر دارایی اسرائیل، و ۴ نفر از رهبران سازمان‌های شهرک‌نشینان و ۲۱ شهرک‌نشین به فرانسه ممنوع اعلام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/126500" target="_blank">📅 15:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی شد دو فرمانده ارشد وابسته به جنبش جهاد اسلامی فلسطین را در حمله‌ای هوایی در جنوب غزه هدف قرار داده و عملیات موفقیت آمیز بوده است.
🔴
در این حمله «ایاد محمد عبدالعزیز نفل»، از فرماندهان نیروهای نخبه جهاد اسلامی، و «احمد معروف»، رئیس یک هسته عملیاتی مسئول اجرای حملات راکتی علیه اسرائیل، ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/126499" target="_blank">📅 15:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bj8xLqqdp40YnyZf7NwWZvJd0kXM5MUrkG7GIC7vpOdEYXfhJVnM5ATVhtMac3AO52Xy8-ESUsxUNM9hT9Bolu37L_TR9ZmE2R9KipjBsq9z9YBoBmhZZ5lORjh0mZBGSwf7cZsFrU3YT3ugIniEXi3rPpuCUsfRVoy00jSdk1KBr2RGtoKEN-X02u0GC6__V9vvRiFmJKofkY7X1KriHg-X6S2QTbw5oR7ouE2O8RjxfEbicVpfofiAGAFfzUbCpFgoMSIlx3Jc95yZas3rqoiz5bArmda7lru6zGPaSGjIj63jRh0-xnvfhZfmVfVgCip4sc-lRk_j6O3CIrcUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjgcpfEsrL3IQF80Ne1ZIKxIqrtSkgWMPm2TvyGGmpDysY0ge-5VEYJlqlC84DOPb4eDPDSpiF5sqrCQSNBhkT9ZIEgG3VHlpA2fAJovRCmgKGg7b91GH34eOHqh0jCPRb4W3HXX8-G2YSiLzONhBeFoC9UdzGyboyoQrxQ3bPJGUpOriDf64V3fhcWGKrSn1FHKkb8j0eXNsKXh82X_DxwG_WxHuReGwrDqcChHFzNzo1ML4alj250TQXEF8uASUy-crLiWbHFz--zabhLmdzY79os0X4Lq0GTiRKYqXJFYSNjV5oiJctABu1E2DqwHjGOaEJqCYSiqELHjAsprEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملهِ هوایی به شهر کوثریه الرز جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/126497" target="_blank">📅 15:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : شورای وزارتی کوچیک تصمیم گرفته هر موشکی از لبنان سمت اسرائیل شلیک بشه، جوابش با حمله به بیروت داده بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/126496" target="_blank">📅 14:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اسرائیل هیوم: مارکو روبیو نقش کلیدی در متقاعد کردن ترامپ برای حمایت از حمله اسرائیل به ایران پس از حمله موشکی تهران ایفا کرد.
🔴
بر اساس منابع اسرائیلی و آمریکایی، روبیو از استدلال اسرائیل حمایت کرد که عدم پاسخ دادن به ایران برتری می‌دهد و تشویق به حملات بیشتر می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/126495" target="_blank">📅 14:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نماینده ایران در آژانس بین‌المللی انرژی اتمی: تجاوزات و تهدیدهای مداوم که شرایط استثنایی فعلی را ایجاد کرده‌اند، متوقف نشده‌اند
تلاش‌های آمریکا در شورای حکام آژانس بین‌المللی انرژی اتمی الگویی برای توجیه تجاوز بیشتر علیه کشورمان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/126494" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e8515ff.mp4?token=H4HBaj51jiFEgfHAWAP0svHBf2ubW8-H7JmwTNNPiPtqvcFfN68Ps5yshljCvtt3efFbF9Ll0Rmz7ZNyTNpNUggBv9eI6HQcdlWfguACDJzgkGjbWhYFST5TKl_MmNWqFeuf15wsgg9tiNgrE_cGAcn2N07elf0MYdEXqSEL6sEY6BDXBTK2UM8rSaOjGJ0zy89a3PtJk8FGlpiBfacEFmfhOFKtXFr-C3k1Xk2I3rcGuKUko5nCkDYgclzn6zzNpy50HN92StHS-Yg3_8i8NCY3UIA_q1XNBYh4gG1h1bBsbOy_G9P3AKqXEiB9SjEaHTpw17G71742132kDJXpWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e8515ff.mp4?token=H4HBaj51jiFEgfHAWAP0svHBf2ubW8-H7JmwTNNPiPtqvcFfN68Ps5yshljCvtt3efFbF9Ll0Rmz7ZNyTNpNUggBv9eI6HQcdlWfguACDJzgkGjbWhYFST5TKl_MmNWqFeuf15wsgg9tiNgrE_cGAcn2N07elf0MYdEXqSEL6sEY6BDXBTK2UM8rSaOjGJ0zy89a3PtJk8FGlpiBfacEFmfhOFKtXFr-C3k1Xk2I3rcGuKUko5nCkDYgclzn6zzNpy50HN92StHS-Yg3_8i8NCY3UIA_q1XNBYh4gG1h1bBsbOy_G9P3AKqXEiB9SjEaHTpw17G71742132kDJXpWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس
:
خود آمریکایی‌ها تو مذاکرات غیرمستقیم به ما گفتن حرف‌های ترامپ رو جدی نگیرید
🔴
اون چیزی که از طرف آمریکایی‌ها تو مذاکره‌ها به ما می‌رسه با حرف‌هایی که علنی می‌زنن فرق داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/126493" target="_blank">📅 14:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucSCLoVOX3zpXgNSoBB40T8vxm9VFfwdsWt6SlHrlRF8wR7LPKiQ-Qy1k2UK0qI3hoaitmtpXbh9szaD3TWEEcLgx0KvZbV6OvYhlodh_2Mpj_WaOudWFcBHmUa2JtyW9daUa0kQvS8y7RX5_9UuvO24MWFk06vfrmlgt6dx3-l_NNQOo6Zl535-kPSe3Hx7J3NtYQs8pL2jW_TQn1A3pPo-YacokwrIUxFeQPzKIc6ZyN2ZMAz1OxFDfWEHgxxHIjtN4OwhYTZmPFQ7ogKZB4mwGb6d7n70dj3DEDrV9RDgMThoD8an4kQQ_SstawiTILBDA-YAviPIHQviGt0lgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، سقوط قیمت بیت‌کوین به زیر $۶۰,۰۰۰$ دلار در روز جمعه گذشته، بدترین عملکرد هفتگی این رمزارز را از زمان بحران و فروپاشی صرافی FTX (متعلق به سم بنکمن-فرید) در سال ۲۰۲۲ رقم زده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/126492" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ادعای یک منبع پاکستانی به شبکه العربیه: اسلام‌آباد در حال انجام تماس‌ها و رایزنی‌هایی با همه طرف‌هاست تا در همین هفته به یک تفاهم دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/126491" target="_blank">📅 14:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کانال ۱۲ عبری، به نقل از یک منبع امنیتی:
ما وارد مرحله «دورهای مکرر» با ایران شده‌ایم. ارزیابی‌ها حاکی از آن است که تشدید اخیر، رویارویی نهایی با ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/126490" target="_blank">📅 14:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
حمله به نیروهای امنیتی پاکستان ۱۴ کشته بر جای گذاشت/ ۷ نفر ربوده شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/126489" target="_blank">📅 14:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKW-hevoM5-_cT3ihVTr4g0_lZ41YR56bva9jR6JGoC1wxtnVizx7_wkJLPogQ9flf83tq_f6AaesafgxYVcn0MUZpm-n5QfZ4jyWqzg8owk8GHVZCuI6jEU8nco4Tgxgq2wCRx5ME3Y3RGib1OqzWGaFCzOJMu0aL73j8_u3OBjDQpufTG4UmXuLgK0Vp_s6FMGqpVd6h7uPM00CSkuxv-YkteyPCdHID0Rr3nYE_dqH3_ljPlySgCq7xuGq6rLBHUA-L7icWSLN_IWa0199YjpHHlcLUATJOStbXWnrNadDZt1-O6OQfEFNLJVp5x07Yb6vt8KZCtLYmaLgs5k5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش اکونومیست، ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/126488" target="_blank">📅 14:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126487" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کرملین: میانجیگری آمریکا در مورد اوکراین در حال حاضر متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126486" target="_blank">📅 13:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=j0xlu02Tiv-aaaQZCSNV5-tjbjMywHg3j_cA_au78qwoafnzado32w8q7H7IZ9L2lBYdxttrVVAxq7_zToeNONTRp60QtWCXjYMX0NvZT08HfKo0Gc6GK7ix7GH46DIurT_mi-shKbMnawHtL6r44IgkZZuYWFTLb5SdnhyxlyoavRr0TAyb_N-nnoIRpWCB5RGb3y-BgJnWEguEquPWIeK9kkY4HxXwwSghcLDRjlRr1P_h1amm4MIeqLLjKCPfVcjR2fIQZVKji2TFGhG0E73D-GqTDLXFagKsEP_daqxLwh-n4AeThl2ED91XSisSbQTrh3YRyJduYokNv-1HHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=j0xlu02Tiv-aaaQZCSNV5-tjbjMywHg3j_cA_au78qwoafnzado32w8q7H7IZ9L2lBYdxttrVVAxq7_zToeNONTRp60QtWCXjYMX0NvZT08HfKo0Gc6GK7ix7GH46DIurT_mi-shKbMnawHtL6r44IgkZZuYWFTLb5SdnhyxlyoavRr0TAyb_N-nnoIRpWCB5RGb3y-BgJnWEguEquPWIeK9kkY4HxXwwSghcLDRjlRr1P_h1amm4MIeqLLjKCPfVcjR2fIQZVKji2TFGhG0E73D-GqTDLXFagKsEP_daqxLwh-n4AeThl2ED91XSisSbQTrh3YRyJduYokNv-1HHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودروی بمب‌گذاری شده در مسکو
🔴
یک نظامی عالی‌رتبه ارتش روسیه در انفجار خودروی بمب گذاری شده در مسکو ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126485" target="_blank">📅 13:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AFpwJpR2ql0N4gmZflBl09RJQ-oYFNouypLsDay0e85yOhsEes4LedhDThVeRNU6OAth5NgJAmec2vD3yAemiZRacDHs5cG1o2axRPGL44sV-Q9RfSprJy6pQ3Nq4RMylVnQf0Uu88o-oA8DMMCUAsITwfmjqmJefHBagkU1RCOM89MwQ8aJiW22jpUEFRYWYdPjgDT_fGzhjaBFYP-TBCQs2GBi3dDjtObJI9EMGIEl89Ryo5iXiR057IhRSJ8zBtzCDh43otStt2rKBVLfM0KUAUidtOi1zT7EayQFyFZo1QS7TCXRowb4q7KeZ6EyrAlkKzptb8PPlyQ5pfecE5PpgE2q9OVH5deVha1kLY7tc4FXpeVwcLB5X2SYci0ZJyWMAg6OjAss6z2xFONe4HCg74TrdIh0yCbgcUDr31XmONRG6kB5KVFfIP4ZtEkXQy4a98Ek7FEhMRrfX7tTfapdR1viPuN3uKJc8olgaGgnWdZvG072PcDbh3YATY4Ku1qw7fbGPN5HxH4lK3137BOBG67TIg5zTqqQ62u7CMqrp7V9eOkOmh34OPeV0YzjRf8VNFoJ6MJyhx0CJnIsHnHxfnQDQWyEAQda1uCZV-oKsyBw1aJmbRpEif7dt0cdaSc6UnXSaxi8c17HDcetD5n6Pe7hMjgsWeGDWvF9uEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AFpwJpR2ql0N4gmZflBl09RJQ-oYFNouypLsDay0e85yOhsEes4LedhDThVeRNU6OAth5NgJAmec2vD3yAemiZRacDHs5cG1o2axRPGL44sV-Q9RfSprJy6pQ3Nq4RMylVnQf0Uu88o-oA8DMMCUAsITwfmjqmJefHBagkU1RCOM89MwQ8aJiW22jpUEFRYWYdPjgDT_fGzhjaBFYP-TBCQs2GBi3dDjtObJI9EMGIEl89Ryo5iXiR057IhRSJ8zBtzCDh43otStt2rKBVLfM0KUAUidtOi1zT7EayQFyFZo1QS7TCXRowb4q7KeZ6EyrAlkKzptb8PPlyQ5pfecE5PpgE2q9OVH5deVha1kLY7tc4FXpeVwcLB5X2SYci0ZJyWMAg6OjAss6z2xFONe4HCg74TrdIh0yCbgcUDr31XmONRG6kB5KVFfIP4ZtEkXQy4a98Ek7FEhMRrfX7tTfapdR1viPuN3uKJc8olgaGgnWdZvG072PcDbh3YATY4Ku1qw7fbGPN5HxH4lK3137BOBG67TIg5zTqqQ62u7CMqrp7V9eOkOmh34OPeV0YzjRf8VNFoJ6MJyhx0CJnIsHnHxfnQDQWyEAQda1uCZV-oKsyBw1aJmbRpEif7dt0cdaSc6UnXSaxi8c17HDcetD5n6Pe7hMjgsWeGDWvF9uEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: پزشکیان، عارف و من نظرمان این است که وضعیت حکمرانی در فضای مجازی مناسب نیست
🔴
ستاد ویژه ساماندهی و راهبری فضای مجازی با قوت به کار خود ادامه می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126484" target="_blank">📅 13:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پروازهای فرودگاه هاشمی‌نژاد مشهد به روال عادی بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126483" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126482">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=OAe8q-lxOxeXebMvq-SjxqTdvBA8fSfwV3mDYSZrHTeuMtncGZ6LKvL7U80miFZa4aFw-4v9uP8SDeSH6PrAZ3qgjt3QY2gwBFnlFnYbpsqzAMm9hcfuSTrQVx6jOlBXxzCJ9rqSz9RMWD0iJXyaa8-Ings1cnbQhY2aSszOFTqHEIfTK3R8VbcvHtEvwU5S5vJ4vGzMaLBL3p3sq5tgNmob7qEqVVWMyVLhjd4TtQ0SrrxWjO0PPYwV63GEn3qCokpRJpqxFQQwxQdHx7tP3ObUYAFhlhd8lv8aHATPCVzSdFmjzOH15k1WogSlRtARB8HJYrS6WQ0MNWjkdVg9nymaT_MJD8E9KGZPtZSpJJIJ9liYhsGBrdfypitVCDBNpGF7iV7Mz3jTugHriinesT8Coy2Z5-7_l0gGbckRDMZZun9KtJmx1IwHNVVRXjsLn0UDJtvNu1mvSK0OvNSTxaNaL9jxmHHmB6Dak7jpfMIEgnTnk3ig0jDatXGLlQfXSciQABv-TZ7Ad82vJMRcsw-HTofgsgfScpc74bgG0PaVeKF353PGTIyVeN2jl2NW1Ci-jxAlFETY-guhjf2eChotUKUiZMTyhiwZNEqffgFAg1muke_DHVq5FYfpuENZPNazyrIx6vtk8YXydUKnB1J5G6mljuHFmPlLqEpQrCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=OAe8q-lxOxeXebMvq-SjxqTdvBA8fSfwV3mDYSZrHTeuMtncGZ6LKvL7U80miFZa4aFw-4v9uP8SDeSH6PrAZ3qgjt3QY2gwBFnlFnYbpsqzAMm9hcfuSTrQVx6jOlBXxzCJ9rqSz9RMWD0iJXyaa8-Ings1cnbQhY2aSszOFTqHEIfTK3R8VbcvHtEvwU5S5vJ4vGzMaLBL3p3sq5tgNmob7qEqVVWMyVLhjd4TtQ0SrrxWjO0PPYwV63GEn3qCokpRJpqxFQQwxQdHx7tP3ObUYAFhlhd8lv8aHATPCVzSdFmjzOH15k1WogSlRtARB8HJYrS6WQ0MNWjkdVg9nymaT_MJD8E9KGZPtZSpJJIJ9liYhsGBrdfypitVCDBNpGF7iV7Mz3jTugHriinesT8Coy2Z5-7_l0gGbckRDMZZun9KtJmx1IwHNVVRXjsLn0UDJtvNu1mvSK0OvNSTxaNaL9jxmHHmB6Dak7jpfMIEgnTnk3ig0jDatXGLlQfXSciQABv-TZ7Ad82vJMRcsw-HTofgsgfScpc74bgG0PaVeKF353PGTIyVeN2jl2NW1Ci-jxAlFETY-guhjf2eChotUKUiZMTyhiwZNEqffgFAg1muke_DHVq5FYfpuENZPNazyrIx6vtk8YXydUKnB1J5G6mljuHFmPlLqEpQrCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به شهر ساحلی جنوبی صور حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126482" target="_blank">📅 13:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126481">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f61dlTgV9r-csYjBBn4_-AZ15rq7u543s_yA08yV6BQ5M5Lu2A7aO81d_DLfROGP2UNRYBW7BXV3bNbIFo1CmHlcUTcFBhGDi4i7sJudZjdH7NQ4rkFhZnXXgMs0Ss6D517C3tIfpF6n1fAkS9M2w5MpVp9Tt3cntIDZT8Kh42hKOFO19Zfniw5k2VD2O5e9ZMDUpo4xUfI7O6KleQLiE-x-DBUjm-67jb8ilGwx1W0DbmyeviGXgqHUyDD2_tCwzr9YWywC-2M-pXR-oXMz7xA3KyvbrbuMyfXbALw_4AMiGQ1WvA9vSH0h5cf34iFDoyIoWwtOJtf7_5Fr5pfllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۱۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126481" target="_blank">📅 13:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نیروهای اسرائیلی در یک بازرسی نزدیک اورشلیم، هشت عرب از یهودیه و سامریه را که در دیوار دوجداره یک خودروی تجاری پنهان شده بودند، کشف کردند. راننده تلاش کرد فرار کند، اما پس از تعقیبی کوتاه دستگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126480" target="_blank">📅 13:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126479">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به گزارش تسنیم دو عضو از یگان‌های پدافند هوایی روز گذشته در حمله اسرائیل کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126479" target="_blank">📅 13:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126478">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
زلنسکی، رئیس جمهور اوکراین :
- روسیه جنگ رو نمی‌بازه، ولی هر روز داره کم‌کم ابتکار عمل رو از دست می‌ده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126478" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126477">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126477" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126476">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک شاهد عینی اعتراضات روز سه‌شنبه در هرات به افغانستان اینترنشنال گفت که یک کشته و دست‌کم ۲۲ زخمی را از نزدیک مشاهده کرده است.
🔴
منابع محلی دیگر نیز زخمی شدن شماری از شهروندان و احتمال کشته شدن یک نفر را تأیید کرده‌اند. با این حال، تاکنون آمار دقیقی از شمار قربانیان در دست نیست.
🔴
اعتراضات روز سه‌شنبه در منطقه جبرئیل هرات در واکنش به موج بازداشت زنان از سوی طالبان آغاز شد. به گفته شاهدان و منابع محلی، نیروهای طا/لبان برای متفرق کردن معترضان به سوی مردم شلیک کردند و تجمعات اعتراضی را سرکوب کردند.
🔴
منابع همچنین گفته‌اند که طالبان شماری از معترضان را بازداشت کرده و برای بازداشت زخمی‌ها و معترضان به شفاخانه‌ها مراجعه کرده‌اند. به گفته منابع محلی، طالبان همزمان نیروهای بیشتری را در منطقه جبرئیل مستقر کرده‌اند و فضای شهر به‌شدت امنیتی و نظامی شده است.
🔴
طالبان تاکنون به‌طور رسمی درباره این رویدادها اظهار نظر نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126476" target="_blank">📅 13:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126475">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ به بی‌بی‌سی: اگر به نتانیاهو بگویم کاری انجام دهد، او انجام می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/126475" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تنکرترکرز: نفت‌کشی که در ۱۵ مایل دریایی سواحل عمان دچار آتش‌سوزی شد، با شلیک جنگنده F-18 آمریکا از کار افتاده است؛ موضوعی که سنتکام نیز در بیانیه‌ای به آن اشاره کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/126474" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی دولت: ایران و لبنان نه نیروهای نیابتی یکدیگر هستند، نه برای هم می‌جنگند، بلکه دشمنی مشترک دارند
🔴
تیم دیپلماسی ما متشکل از افرادی است که به شدت به میدان آگاهی دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/126473" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNuJhQ8c3ZSQVXhJtiEPG8Le2U_HMS01QO9qI4i-exiRVdWbsyuL9WV-wxh98956muDb-VpRNQJSSAP8bNc1hL_3G9NodzghmJcHup7U0jTc5FTGhrdq0ix-KKNr8UW2loTQH6qXLkZUoYwVOQ4FZsjZHlUHaGBVjfLBMRpb_rEtIusOZKqTDcQS2_4xKXHOAk0i9u0WjXO6F172ZzhQLprambiAjz7sbk7aeo4hpBss2Z8VXp8MnXXQwuMXct8E17xkAnTia18ryRJXfc_TV68MRAfdi2Af4nWLL-WWFe-fY9TQnAHXBMiIx9YED5WYEkLzaw1cakv-JNkqzjOOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش بیش از 114 هزار واحدی به 4 میلیون و 540 هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/126472" target="_blank">📅 12:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq67o4AFtEKGHIDMYKSBkhk6JSdqRwugbXeH3I85Uov46z5iJwzXRmnsx6rZdP6fpO4itVjHkKR7SQtUCPhiefeJ_1fY9Ki-JfkuAJXBHBO1JoPNvdBbRk9yVTdxkyXu_0cSvrjMmO3kKNHZQlFKutv-UNulfjob5RkhchiOvdKBCJhA-LJRghPhpSyx2PsAkTFG2P4ZM6TiqjJ6fOJnnomUfezkgjSi-4dg1dmMBsR-f3rbNxB18Y8enqG50PSqYOiPVBz__M70adFQc7tzQfqgTocXokMHSPGbIm1PyUihc3RuTdNLSho9siE0rATz4C2SD6KoTQ0bc1VmOcgiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فکر نمیکنم حالا حالاها جنگ بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/126471" target="_blank">📅 12:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر ارتباطات: شبکه داخلی ما با قطعی طولانی‌مدت اینترنت، آسیب‌پذیر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/126470" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یوتیوب رفع فیلتر می‌شود
🔴
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/126469" target="_blank">📅 12:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر ارتباطات: خسارات وارده به وزارت ارتباطات ۶۸ همت برآورد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/126468" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر ارتباطات: دنیا دنیای هوش مصنوعی است و ما مانده‌ایم ارتباطمان برقرار باشد یا نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126467" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/8d88eccc6f.mp4?token=pGOJgaNGrnpbTrdKLv-a2C0859Y4XavJj57qenJPpowjSNerEGDyWXBiLazpCnJLBTFBaJFSaV1S_lge8DLjLQBr_eBnR0b37ZN-gNCToTfLEfvpej9jb2DYQ9jweeWSQ9kTwsAUo4Hk0p97W4_KR8aW9o6SGndXQ1cDwVeFxGP-tuxTrzfoZxzgB-m3FCEei11cscb0LeZdribOIRW5Jh4Jz9VGdgiGNhPk7jHB36daf72_m8Pm7ccicklAiHXxio_sHm7HLvvuxa951b2LuV1qItLBTmm5HLHh1sHOsXSDMDY0WcHbA5tAzrrye9Tf3nTs7rYAJ3Nh13xdgPx29g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/8d88eccc6f.mp4?token=pGOJgaNGrnpbTrdKLv-a2C0859Y4XavJj57qenJPpowjSNerEGDyWXBiLazpCnJLBTFBaJFSaV1S_lge8DLjLQBr_eBnR0b37ZN-gNCToTfLEfvpej9jb2DYQ9jweeWSQ9kTwsAUo4Hk0p97W4_KR8aW9o6SGndXQ1cDwVeFxGP-tuxTrzfoZxzgB-m3FCEei11cscb0LeZdribOIRW5Jh4Jz9VGdgiGNhPk7jHB36daf72_m8Pm7ccicklAiHXxio_sHm7HLvvuxa951b2LuV1qItLBTmm5HLHh1sHOsXSDMDY0WcHbA5tAzrrye9Tf3nTs7rYAJ3Nh13xdgPx29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان/تظاهرات در شهر هرات افغانستان ادامه دارد و طالبان در حال کشتار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126466" target="_blank">📅 12:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=OITifU4gl-BBbYDA5ferpOp8ng5OdknIq5oLNvp63upKdWGtCMgLIPDfZzVooHqkrUypQbVlc_YjrDq19g2vkz8I0zty8NjngZ4iWrgtC2rzNIuAyBG9FVeYeldP5S1a7WIXKFzkRQFHhlRyrfFuKmzT_DLiUyvwvtJFEmRJa5vKo-LMYEp-0WeMX-LGddLVTOmNSMQIa2xZuW6iFLMbTvu7bAridLLkN5L1_dX8va5nAd8rV0ZNhJsEIq-l3atb9bu-0jz4oK0R3ZlnN_5RF8Sv2Eu9ae_ubzG-eeZ0sg9xj-xcyuhZPxY9EGzmakVtmvoIXBdRhlmnm7ERZpkcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c0fbfca63c.mp4?token=OITifU4gl-BBbYDA5ferpOp8ng5OdknIq5oLNvp63upKdWGtCMgLIPDfZzVooHqkrUypQbVlc_YjrDq19g2vkz8I0zty8NjngZ4iWrgtC2rzNIuAyBG9FVeYeldP5S1a7WIXKFzkRQFHhlRyrfFuKmzT_DLiUyvwvtJFEmRJa5vKo-LMYEp-0WeMX-LGddLVTOmNSMQIa2xZuW6iFLMbTvu7bAridLLkN5L1_dX8va5nAd8rV0ZNhJsEIq-l3atb9bu-0jz4oK0R3ZlnN_5RF8Sv2Eu9ae_ubzG-eeZ0sg9xj-xcyuhZPxY9EGzmakVtmvoIXBdRhlmnm7ERZpkcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک مستقیم نیروهای طالبان به معترضان در شهر هرات
🔴
طالبان میگوید که اینها مردم نیستند و نیروهای تروریستی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126465" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
چین: مذاکرات آمریکا و ایران در مرحله‌ای مهم قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126464" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سپاه : اردن به اسرائیل تو حملات به ایران کمک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126463" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413a6c6658.mp4?token=fzSLwDREwLyrcdCH-TWYDajb4B5AxYoIK0_YFpthdrlNq8WYWnhuBOC0PkCsb-RTt6BfOODp_49CvvNInWw1OZxmhraCZwf9Lj_7oOBvqfTtT32WAbjtcUxMAMWmSeiIUSNv1DLr2Bw6hJ7E7owzENXuxCqPBsnSKkj7l3tByGfTVvOsfkMAA5Gnv4AKHxCvnJEw87xFQc_m834HY4_wLk5tciCQgNGrVu9kwcs54dALO_demt4GV6jikKXSe2CH0BqTLdmMVWRT4Iwr1G6xYaEcGSKWXX_sT1TcMwu0ltrZnVZIRSTLLZTeHfG-DU4y_qFAYTOEIm7lwZ_KFflVMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413a6c6658.mp4?token=fzSLwDREwLyrcdCH-TWYDajb4B5AxYoIK0_YFpthdrlNq8WYWnhuBOC0PkCsb-RTt6BfOODp_49CvvNInWw1OZxmhraCZwf9Lj_7oOBvqfTtT32WAbjtcUxMAMWmSeiIUSNv1DLr2Bw6hJ7E7owzENXuxCqPBsnSKkj7l3tByGfTVvOsfkMAA5Gnv4AKHxCvnJEw87xFQc_m834HY4_wLk5tciCQgNGrVu9kwcs54dALO_demt4GV6jikKXSe2CH0BqTLdmMVWRT4Iwr1G6xYaEcGSKWXX_sT1TcMwu0ltrZnVZIRSTLLZTeHfG-DU4y_qFAYTOEIm7lwZ_KFflVMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به یک خودرو در روستای الشارکیه در منطقه نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126462" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی دولت: میزان قطعی احتمالی برق تو روزهای گرم پیش‌رو، قابل پیش‌بینی دقیق نیست و مستقیماً به الگوی مصرف و همراهی مردم عزیز بستگی داره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126461" target="_blank">📅 12:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پنتاگون در ماه مارس فاش کرد که بخش‌هایی از نیروی هوایی ۸۲ در حال اعزام به خاورمیانه هستند، اما این موضوع را که برخی از آن‌ها به سمت اسرائیل می‌روند، فاش نکرد.
🔴
دستور اعزام ارتشی که توسط کن کلیپنشتین به دست آمده است، نشان می‌دهد که سربازان از تیپ دوم، هنگ پیاده‌نظام ۵۰۱ در آوریل ۲۰۲۶ برای مأموریت موقت به اسرائیل فرستاده شدند.
🔴
یک منبع نظامی می‌گوید که این اعزام به برنامه‌های اضطراری جدید ایالات متحده و اسرائیل مربوط به عملیات‌های احتمالی علیه ایران، از جمله تصرف جزیره خارک، مرتبط است.
🔴
نیروی هوایی ۸۲، که نیروی واکنش سریع ارتش است، برای حمله‌های هوایی و مأموریت‌های «ورود اجباری» آموزش دیده است.
🔴
به‌طور عمومی، پنتاگون فقط گفت که سربازان به فرماندهی مرکزی (CENTCOM) اعزام می‌شوند که باعث شد بسیاری تصور کنند آن‌ها به سمت پایگاه‌هایی در کویت یا قطر می‌روند. مقامات هرگز اعزام به اسرائیل را تأیید نکردند.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126460" target="_blank">📅 11:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718745a1a.mp4?token=iX5gThMRTPM_2WqXTaTxoUCC_BTtjmWSxTf9g4e9OFol_bwbie7-dNhSf2-earuQtKrzDi0m7n3iUnPD5PPLwwJWuk8LnXlLwMN5RfzmJn19OGp7lxd2eWDNJQYtf2Dfnnw6gFJavstv4g9nZeZLmyCb2sD9Zk0VFf11WKMvmWc9lCvOJYfHJYCr_QOpbFOA0q27Euuc0uwoKcd76SnHCmqDUxcpSWrhw-zRFJrCzXwp_n9aKjgAlBEQkGkx1fH9pLpfC6OF10giVMrhbUdz4Ch74dpW9jnEPdvMPfFD1qJor7kO_Mu4k2x0nUVpxmbRySKn9pGk1ITmf8LyhdrTPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718745a1a.mp4?token=iX5gThMRTPM_2WqXTaTxoUCC_BTtjmWSxTf9g4e9OFol_bwbie7-dNhSf2-earuQtKrzDi0m7n3iUnPD5PPLwwJWuk8LnXlLwMN5RfzmJn19OGp7lxd2eWDNJQYtf2Dfnnw6gFJavstv4g9nZeZLmyCb2sD9Zk0VFf11WKMvmWc9lCvOJYfHJYCr_QOpbFOA0q27Euuc0uwoKcd76SnHCmqDUxcpSWrhw-zRFJrCzXwp_n9aKjgAlBEQkGkx1fH9pLpfC6OF10giVMrhbUdz4Ch74dpW9jnEPdvMPfFD1qJor7kO_Mu4k2x0nUVpxmbRySKn9pGk1ITmf8LyhdrTPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: اسرائیلی‌ها و ایالات متحده منافع مشترک زیادی دارند، اما همچنین شرایطی وجود دارد که منافع ما در آن‌ها متفاوت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126459" target="_blank">📅 11:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIfZK6FtRVhvdJRnxLa8x0s88qqSvKmPBWniCKx7Mw5qOyuk1Aa-poBcCl_g1ItbqL5HnCVSRa-LxhdW_Jfw0Vm7kI9fmN_zsnJEeiJpoYrZB58l8wMGCOJcbjAZnDkQzRBL9Wyv3fjcXrHaCWY23IrZVE6yp9gVPkjX_wST6gFo11GDBZ13UsqJKmpdZv29QTHbj8gYAIllRo-B_Z1UdPIqJATLWuX2sddrThxtMzm6SIPzT4y7Tekh-utFrw1MPxIyUXjt5WvUJ5oc1qyUWfv7jItwYKweo3BW8RKlGeJEJoDHVMIt3vioqoVtOjKp2KaFQA0C0d91RMcLN_VgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: پنتاگون ایالات متحده فهرست شرکت‌های چینی را که به عقیده آن‌ها به ارتش چین مرتبط هستند یا از آن حمایت می‌کنند، گسترش داده است و شرکت‌های بزرگی مانند علی‌بابا، بدو، بی‌ای‌دی و نیو را به آن اضافه کرده است.
🔴
در حالی که گنجاندن در این فهرست به معنای تحریم نیست، پیامدهای قابل توجهی به همراه دارد.
🔴
طبق قانون ایالات متحده، وزارت دفاع به زودی از خرید محصولات یا خدمات از این شرکت‌ها، چه به صورت مستقیم و چه از طریق واسطه‌ها، منع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126458" target="_blank">📅 11:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ در مورد جمهوری اسلامی ایران:
فکر نمی‌کنم هیچ نقطه‌ای وجود داشته باشد که مانع شود. فکر می‌کنم بسیار نزدیک به داشتن یک توافق بسیار، بسیار خوب، قوی و قدرتمند هستیم
🔴
اگر برویم و بمباران کنیم، که اگر بخواهیم بسیار آسان می‌توانیم این کار را انجام دهیم و دو یا سه هفته دیگر بمباران کنیم، دیگر هیچ چیزی برایشان باقی نخواهد ماند.
🔴
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید که بسیاری از مردم کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نه.
🔴
و ما به یک سند امضا شده دست خواهیم یافت که در واقع قوی‌تر از انجام بمباران است.
🔴
شما به یاد دارید ونزوئلا را، درست کمی پیش از این، یک جنگ یک روزه.
🔴
ما آن را تصرف کردیم و روابط بسیار خوب بوده و ما میلیاردها و میلیاردها دلار نفت گرفته‌ایم.
🔴
ما هزینه آن جنگ را بارها و بارها پرداخت کرده‌ایم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126457" target="_blank">📅 11:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9623807c6f.mp4?token=rIOdXtkfK5IWiEPY7rP4iiK3kTO0tUvKlnkZ-PAS38uXQZJzoIB3JGYPXG3A7rUXO4SKUcYQhObAZWjoXKfMWMBMFR4XphADh9rb3Ev3YBAN6YdSCFED5tU5Kn6PTPfmET2-LU3qDhUD5OoAkn892rDs0TCGhUU60viqHd9sTIDVxaU5190Fr3nLfNYkfnyL-yO8Xo0GfbhRravMuc9zt7HKTuRypPTcK7_JbZzpx73PW3fBNDKi3_P1TfYiv0wYvBIDUvusrSDm9FDmtpf7SQqBG-f7BI9yNGLwjfjG1EMZ2t2nRqQjBiefC-ap-srABifrGMaAG_AhATQm-Yxx2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9623807c6f.mp4?token=rIOdXtkfK5IWiEPY7rP4iiK3kTO0tUvKlnkZ-PAS38uXQZJzoIB3JGYPXG3A7rUXO4SKUcYQhObAZWjoXKfMWMBMFR4XphADh9rb3Ev3YBAN6YdSCFED5tU5Kn6PTPfmET2-LU3qDhUD5OoAkn892rDs0TCGhUU60viqHd9sTIDVxaU5190Fr3nLfNYkfnyL-yO8Xo0GfbhRravMuc9zt7HKTuRypPTcK7_JbZzpx73PW3fBNDKi3_P1TfYiv0wYvBIDUvusrSDm9FDmtpf7SQqBG-f7BI9yNGLwjfjG1EMZ2t2nRqQjBiefC-ap-srABifrGMaAG_AhATQm-Yxx2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر نوجوان سنندجی که قربانی خشونت خانوادگی شده بودامروز یکی از مهمترین مراحل درمان خود را با موفقیت پشت سر گذاشت و جراحی فک او در بیمارستان کوثر سنندج با موفقیت انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126456" target="_blank">📅 11:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126455">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400f3a9182.mp4?token=AhdYrXfK0oafjMdZFb6-XZ3UULMeueqeJPIxE6GNr-ifYyi2Zo6pbJYn7bnfeazKgzX7SELfDbQ1r_xt315TJNMPMPIMl0dVv6lN6fFSroNYfUGxXDAlkXvfn8W0Stpt-3e2rFiQTlxrN_ILOIdAZydUO2dWcqpGId5kXw5LKWlMpCqPeORGklTJWonoNBZrw51w28L0Bp_a7L1ADm7Rj5TIrDxm7zLrT-cyNLjfIikTjGC5SIPhqPRG6qrS5iA_MXv7vbR1G6dJiRT4UnTNPD_HerSNab_SCKe2vorxRH7j_Q63HaLw31fB7-mCocoETm5gHFV5FHK-zdKJBvAtaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400f3a9182.mp4?token=AhdYrXfK0oafjMdZFb6-XZ3UULMeueqeJPIxE6GNr-ifYyi2Zo6pbJYn7bnfeazKgzX7SELfDbQ1r_xt315TJNMPMPIMl0dVv6lN6fFSroNYfUGxXDAlkXvfn8W0Stpt-3e2rFiQTlxrN_ILOIdAZydUO2dWcqpGId5kXw5LKWlMpCqPeORGklTJWonoNBZrw51w28L0Bp_a7L1ADm7Rj5TIrDxm7zLrT-cyNLjfIikTjGC5SIPhqPRG6qrS5iA_MXv7vbR1G6dJiRT4UnTNPD_HerSNab_SCKe2vorxRH7j_Q63HaLw31fB7-mCocoETm5gHFV5FHK-zdKJBvAtaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد جمهوری اسلامی ایران: ما مذاکراتی در جریان در ایران و با ایران داریم و این کار متوقف نشده است.
🔴
ما می‌توانیم حداقل یک ایده را در یک یا دو روز آینده داشته باشیم. اما فکر می‌کنم همه چیز خوب پیش می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126455" target="_blank">📅 11:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126454">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8080f5f9.mp4?token=FHyqUotc8fQeZy6C-fI3zd6vwGZ0cKgZtvMi8WHnZvU-kFuLypBP9BhFP0QB4w5fNyhz3Ne0w1CQCT05d-M5Ktgj-nH8dfkUG-g1O8GVnYdaGbN6vkJ3654D2G6V1NqIk5Lm87jZNOUxT20AtBW1JocXXqJh8-T6W1ZRQciWa2o5OFsEj_jlVuBGXLI4W78ouviBQlmRoXNhAMbzn6k5oY85rXgBy6GhtFaDIBlQHQEOwJKPBDMJAf-1vJPZwRdMec2kMOIzhMnFffBNrFryhzcq9fK1I2svAUPe0aG3JooR71EtLNpugROnkhttn6iLhuVsbgzGy9nLX6TgxjjLrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8080f5f9.mp4?token=FHyqUotc8fQeZy6C-fI3zd6vwGZ0cKgZtvMi8WHnZvU-kFuLypBP9BhFP0QB4w5fNyhz3Ne0w1CQCT05d-M5Ktgj-nH8dfkUG-g1O8GVnYdaGbN6vkJ3654D2G6V1NqIk5Lm87jZNOUxT20AtBW1JocXXqJh8-T6W1ZRQciWa2o5OFsEj_jlVuBGXLI4W78ouviBQlmRoXNhAMbzn6k5oY85rXgBy6GhtFaDIBlQHQEOwJKPBDMJAf-1vJPZwRdMec2kMOIzhMnFffBNrFryhzcq9fK1I2svAUPe0aG3JooR71EtLNpugROnkhttn6iLhuVsbgzGy9nLX6TgxjjLrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در فینال NBA (نیکس در مقابل اسپرز) وقتی که تصویرش در حین پخش سرود ملی در حال ادای احترام نظامی بود، هو شد.
🔴
او بعداً آن را «بیشترین تشویق» نامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126454" target="_blank">📅 11:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl8C8tv2W1kEP7RxWWYnXbbNBhQ09Oc-SzrBXkBkutj_dCWbhZrOaK4P7-WgTAuRAWG1jFeGkjhcbm4D3zALCko4UOnSB56CY_l5Fg2ytxp2qbbKehu5WH7Q5RBwBxIivjQXSC35f3g1mc-VRgZsTPa7aTpmgSmhHaoriDFXRoFwZOALG838lXBC02q_zPLku5BXGTrl2FeYdqazjC7QD1OBofrjs2-eCU4-29Sfu193KCngFmuLygO0sqjBbXswSb5DJeRnWDWkgNAUEVfM9H-M9FQ1t2W4nt62KBsN80T4l7AnzF5FJL5TSWHFigkfLSLgDMC3xPXF50lqv9RKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: ترامپ ۳۷ بار توافق با ایران را «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126453" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ممکن است اسرائیل از توافق هسته‌ای ایران خوشش نیاید، اما ما به دنبال منافع آمریکا هستیم
🔴
مجری: "شما چقدر نگران جاسوسی اسرائیل از ایالات متحده و اقدامات مستقلانه‌اش در لبنان هستید؟"
🔴
ونس: "ببینید، به نظرم واضح است که اسرائیل و ایالات متحده منافع مشترک زیادی داریم، اما در برخی موارد نیز منافع‌مان از هم جدا می‌شود.
🔴
فکر می‌کنم جایی که رئیس‌جمهور خیلی صریح بوده این است که در حالی که اسرائیل مشخصاً اهداف خاص خودش را دنبال می‌کند، هدف اصلی ایالات متحده در قبال ایران، اطمینان از نداشتن سلاح هسته‌ای توسط ایران است و ما در واقع، به لطف تحولات چند ماه اخیر، بلکه واقعاً یک سال و نیم اخیر، فضای لازم را ایجاد کرده‌ایم که رئیس‌جمهور معتقد است می‌توانیم به یک توافق بلندمدت برای حل مسئلهٔ هسته‌ای ایران دست یابیم.
🔴
حالا، ممکن است اسرائیل از این توافق خوشش بیاید یا نیاید، اما در بنیادی‌ترین سطح، ما فکر می‌کنیم این توافق به نفع ایالات متحدهٔ آمریکاست.
🔴
بنابراین به دنبال آن خواهیم بود، چون رئیس‌جمهور ایالات متحده برای همین کار انتخاب شده است. برای خدمت درست به مردم آمریکا، این کاری است که باید انجام دهیم."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126452" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126451" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126450">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر ارتباطات: ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126450" target="_blank">📅 11:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126449">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ef04fa4d.mp4?token=qi4k7pvG1v-kpqcvtBhfKELa2Q7GHFyPQ677_t6khhmJ5hjKBQ-aFiQRC1vBvosEZTh93Yq8EDYP9ACNC8Tb8oMhal-I5QBTtYBJiXkO2AhdXD_n3Wrhg55kP9t9tfJ8CihhMho96eNUPyvTNPdxSOPtR5hAidW7VlkuxaMJkiH7Oe0LK8FweQu5Pr9v7a4KuEaZopq8u60KTEoDODP0RuL_DOlfIhDbwljz-DGjzSlTIX42EH3A_fqbSaPGHiTxFeL7g5VGC8MxKM5mOWpDWwAzyntggrP5z8XKODMsOwaGuPuMqwxqR3dSzBy3At1X6hqBdFfP3BQEQ2R0Z8mcXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ef04fa4d.mp4?token=qi4k7pvG1v-kpqcvtBhfKELa2Q7GHFyPQ677_t6khhmJ5hjKBQ-aFiQRC1vBvosEZTh93Yq8EDYP9ACNC8Tb8oMhal-I5QBTtYBJiXkO2AhdXD_n3Wrhg55kP9t9tfJ8CihhMho96eNUPyvTNPdxSOPtR5hAidW7VlkuxaMJkiH7Oe0LK8FweQu5Pr9v7a4KuEaZopq8u60KTEoDODP0RuL_DOlfIhDbwljz-DGjzSlTIX42EH3A_fqbSaPGHiTxFeL7g5VGC8MxKM5mOWpDWwAzyntggrP5z8XKODMsOwaGuPuMqwxqR3dSzBy3At1X6hqBdFfP3BQEQ2R0Z8mcXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از  رهگیری موفق یک پهپاد پرتاب‌شده حوثی‌های یمن توسط پدافند اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126449" target="_blank">📅 11:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در جنوب اصفهان تا ساعت ۱۳ امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126448" target="_blank">📅 10:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126447">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6mhwiTtTQhaOE28yQDww-DR5LRsbxTbiBfSndRr60Yf0sRE9cQOgGzBEiOtdxaqVezTz6LOrhh5j5dKv-USJ2LopitMJSW_Fyn-T6ppX0phxq8O4AVQNMqCB9Vac8i2dkjJOxpdwAhKhfSunwru4JdGbHte4p5BMKysYU6pdIUDVyl2oAqpqfgW2-PsNnHnGg6Fw0c6Q27Ej8YyB61AkhhDmsKpriz2GGwa3kymJjScAmNIt_Hx_POHLXb8_bU0Z9aOXZC1tT6RYrelK6oDYKsOWkCllNRkyd5bYd-tlNt3DbX8yWB1_uffiMVCC_ads3PSdQIuHmTWsJKK1qcs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بستن بازوبند رنگین کمانی تکذیب شد؛ درخواست ایرانی ها برای بستن بازوبند مشکی
🔴
از اردوی تیم ملی فوتبال خبر رسید که مسئولان فدراسیون فوتبال ایران از فیفا خواستند در بازی با مصر که همزمان با ایام تاسوعا و عاشورای حسینی برگزار می شود با بازوبند مشکی به میدان بروند.
🔴
ضمن اینکه بخش رسانه ای تیم ملی فوتبال الزام فیفا به بستن بازوبند رنگین کمانی که نماد همجنس گرایی است در بازی مقابل مصر را تکذیب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126447" target="_blank">📅 10:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7L1NMiiABeMUeUvMxVEsHEqEnQ6w3KQQ8xhLBtWgeBKupnhgbw2AzYwCxnQJadIApa0_0E0jWLdEPyuk6etu9xKTI-_KLi5cBCAHzwpsC7x-M4JDseVpyfXm0zUgpRVOD-KMoOZE-t81dl5W17ZWNZi7Iv1LqPgrnC0WnY_k6IQj9f7q8ay9SRdpO6Z1LDwKGpyNNJju6-zNRUrYnYhE3vwLXCA511RJ1uAyuxsSGdHy5ojNREuEt-Hrz1ZVZJu8_uxE4d8YjEBWh0kX3S7KUk7yhKODzC6syHexLea55dol2hvFZLtglAUGiZVE1AqUMAtJY7Hvm76uL2b5VMMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDsxeLM_VZJMpNGFjvXw1S5vCVgQYtD4peiyaN7Nk6eAQBJeEElU6e4JL8k7BZEq5_yV1IXG7lIQocf2aOAOtStSrIVIzHddmunoMwtEFWZaySX2Iy7oXqQtOHFN1kEJdjXmqeTOhllE4ybPmCn6rSV-y8MbfDN9ovqrFyDKZdvMDHX0nuOpNlMfqXzw17GIh_93BGzRYEzGv_RPk4OYsY7Kic56YfG3-uIuZYpPpOefjn_R1cHUCpw6LB_ma5olV38R1we_2_V3g3eoktYmXKO--ynrnSZdAR2Uzh1452QigHzb5FQZdu4sb_z3seg68586yrzlUrlMTqift0_6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1SZf8EPwT934dVz3HZURuljqYnZ6ljd4SL511oiThuwTjbeaClUVgKPCGyQI6I9QIIRZbj1Xw9Zz1DNl00GinPBmxdAXvb7EF77CFx1mnko3Qn4iB0PaWLhqpaUIfQzRaYw2ERcBM90N2jGDyAdkiS5IVP6X8zwPWl-4d6qMo2fgguRMdeMZEliSuQpu8f6V0IhFPI06FFnWua_KP_pU1jSQXjxp952dYHKcvBdOWqWwT9m0B3IOKvmZCZDvyhtRfQy4xaiomAE7dY9_as0XSnn8vSGckIznJ7Ga54ROz1sG2D0RGw_wGw1zbZ9MB9kUV8t7IWU2Ds4Z5m-56b77Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126444" target="_blank">📅 10:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فاطمه مهاجرانی، سخنگوی دولت : اینترنت در حال‌ بازگشت است‌ و مشکلات فنی وجود دارد که ان‌شاءالله به تدريج رفع می‌شود.
🔴
موضوع اصلی ما حکمرانی فضای مجازی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126443" target="_blank">📅 10:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d982e90999.mp4?token=Arn765vwKEtJLGzzt8UXQOF9PKzAoIivtmeHVAsBznCcFKAoQtKUtA-w3Pdgdupg67GTcAJcx71AHt2vv4DfFD2dwFBcleaZGgQqHi2w1IpEdvEfRfWH9VhwHZkvKY4LcdGr-6dn6nJI6hS0EQmgZsG58gHMpUYLc2CT-9Qjm1ooCR862SlAlTTQWtTT2nC82MKDJLWACQDPtyl7M-MDs6mCuL5_Kh70bGXyBbuOKsoU8yi2szHewoNgnLNFwzuyPSalwWtwwgqCDrhAio4acOYaywi0owV_tJ3B7yV9yaQQct-9BjfMDtdz9Mk5SJKafwWgVBgW7suHN2jmSTQp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d982e90999.mp4?token=Arn765vwKEtJLGzzt8UXQOF9PKzAoIivtmeHVAsBznCcFKAoQtKUtA-w3Pdgdupg67GTcAJcx71AHt2vv4DfFD2dwFBcleaZGgQqHi2w1IpEdvEfRfWH9VhwHZkvKY4LcdGr-6dn6nJI6hS0EQmgZsG58gHMpUYLc2CT-9Qjm1ooCR862SlAlTTQWtTT2nC82MKDJLWACQDPtyl7M-MDs6mCuL5_Kh70bGXyBbuOKsoU8yi2szHewoNgnLNFwzuyPSalwWtwwgqCDrhAio4acOYaywi0owV_tJ3B7yV9yaQQct-9BjfMDtdz9Mk5SJKafwWgVBgW7suHN2jmSTQp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره ایران: ایرانی ها نمی خواهند این جنگ ادامه پیدا کند. به نفع آنها نیست.
🔴
فکر می‌کنم آنها به میز می‌آیند و چیزهای واقعی را روی میز می‌گذارند. ما، البته، بررسی می کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126442" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / ترامپ: توافق با ایران ظرف دو هفته حاصل خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126441" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره: برای ترامپ ضروری شده است که نتانیاهو را مجبور به تسلیم شدن در برابر سیاست‌هایش کند، وگرنه با او به ورطه جنگ سقوط خواهد کرد. این امر به ویژه در این برهه حساس که تحت تأثیر حل بحران تنگه هرمز و انتخابات میان‌دوره‌ای آمریکا قرار خواهد گرفت، بسیار حیاتی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126440" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh6Oj1QMqDOYf7VWeXYe79cVvrkqdyz4z4onXsO85uw5Wf9x6Me7yoNShDra36HY7RTRUSnhk9wnjWvtEboINAf_8uvir6TdrKmqPdaAYPF-VgJ8jVhvoWY0RpoFUVttJaeZOT_uXdFsB_3i-u9JdAdBQL_1hxZlmN9X-WsMacrPUg86Bj2IGckncapiOsjD_5muqWMoiTnAoYBNC83c32RVjWws1IFkQkrlzEHlPQu1x8UTbwjOeGQIQJT-MYkwakJH8wA7JhMospcxuKJL4UumBotBCyCKTw8If9Mdc8CSUy-plFKPO5mjP4VxKHTCVtQedKALTU73m8hJ07Xf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش ۱۸برابری حجم آب دریاچه ارومیه در کمتر از یک سال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126439" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMqGtnAHxxaXfK9zbb8SsMvzlGMQfz2Crg9PMgse2pm8aptNAMu3HOJIg8j59kv54Xr_f5-T6lE8i1uVCfRsjqPyi7lrfA38FUqhsBGot73oVHG_BKmemqovFKPmWYWFuBas5qnonh_kCB15cYJFp2uFPznODij3yNX5S6-t3bNsY5iS4Ed2Kr1xnZqXt_SBss33EU6s0DFmD8SyRltCkRfsdulZWdHI3d0zuFK_2Dw7Comtx-RkjAr9d6nL_cY_j3LOoiPUHTpyvZRNSf-UnkeI379sh6weM8Z0FhJTjaUfTAMVr0MQLQsEEJUYMgwqTMjl2AVOCZ8IwEWILm3E3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار تخلیه کامل بندر صور و محیط اطراف از سوی ارتش اسرائیل صادر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/126438" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سازمان سنجش آموزش کشور : ثبت‌نام کاردانی به کارشناسی ناپیوسته از ۲۴ خرداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/126437" target="_blank">📅 10:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فارس: تجهیزات هدایت و پشتیبانی جنگنده‌های اسرائیلی در جنگل‌های تنکابن کشف شد
🔴
خبرگزاری فارس گزارش داد مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایه که گفته می‌شود برای پشتیبانی و هدایت جنگنده‌های مهاجم مورد استفاده قرار می‌گرفته، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شده است.
🔴
بر اساس این گزارش، این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌ها به حریم هوایی تهران مستقر بوده‌اند.
🔴
فارس مدعی شده منطقه مورد نظر در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شده است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126436" target="_blank">📅 10:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a89527e91.mp4?token=WYwuVRPH2v6B2z7jY9--W1Vu1aMkw96lYPbruB4ekwsZVojV16CrAKFG-U4TFjIicM_GLyj68071uSk7Hjh_RWxasPBMdIWL6bTV01q443IzM1skAOvVV5SfV1KhY_g0_edIgIOPy1tpExmXSS4E82qBXpQ91xDZ7tPesBuG28qnAnbQ1s6eqBaRkot1eUxZI24oZ5TTI_UbO-FKpkj4_dQFxdFP_B3rJu3fUrn2Fedayv7IgtqEPe7m_el82jVqHaq2z4OIKOrXGuLZsDWjqtdY5-ZxKWY0aUV3jIHAmM5CwUEXStWvwnSBNpfrmfXIboB7PyUSmLEjAFGDwRdefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a89527e91.mp4?token=WYwuVRPH2v6B2z7jY9--W1Vu1aMkw96lYPbruB4ekwsZVojV16CrAKFG-U4TFjIicM_GLyj68071uSk7Hjh_RWxasPBMdIWL6bTV01q443IzM1skAOvVV5SfV1KhY_g0_edIgIOPy1tpExmXSS4E82qBXpQ91xDZ7tPesBuG28qnAnbQ1s6eqBaRkot1eUxZI24oZ5TTI_UbO-FKpkj4_dQFxdFP_B3rJu3fUrn2Fedayv7IgtqEPe7m_el82jVqHaq2z4OIKOrXGuLZsDWjqtdY5-ZxKWY0aUV3jIHAmM5CwUEXStWvwnSBNpfrmfXIboB7PyUSmLEjAFGDwRdefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض مادر خانواده پرجمعیت با ۱۰تا بچه به مبلغ کالابرگش: ۱۲ ميليون فقط پول شوینده‌هامون میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126435" target="_blank">📅 09:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4wZACb44MSFbVUqxFUtLo_wnBOgrebp-FPfyuyjGnS0IBJaNkDtIFckSsrFBa8CcMvNNZxlZqKdEUxmueBX2VSqNV8itmR1Fei98X0YTyAb0WglLmEu3UWtkfNjxEzCjI5h00AIKmK6mYQSv7bDpATMiXgQ2FUtxJ7b0boIBZ1uPDjWhAHTPeZ-zihv5LBrWf1xuoqWeVgxwygil4I44mQb2bAijhbvomGAYlhj8IVe_zlQ1__l7Gxg55Kez_Ds5DuIXuanqu8p08JQXdmFkImSNaLd-bmwrJePIFt2FXiwtO5bXAE8DS2078fTpArYFvQhFbUYxMnL8NmtxQtP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر جلد نشریه آلمانی اشپیگل:
ترامپ، خراب‌کننده‌ی جام‌جهانی
چگونه دونالد ترامپ از جام جهانی فوتبال سوءاستفاده می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126434" target="_blank">📅 09:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diAaORoefhstBhlD_5x2-JPnaRY4oz--dlE7-dB_GZGaKUbyPqw4OF0cGVG780wi_GJxdN5dFzIUWFxTu2qOStCas_TqMsRYwbv4TtY-0OYvq__qu40irhb56lybscGU_70BV_QFAV2aceRAATYarBxQpGu4zsfrqllh3f2peTERsurJc67aeG7oIVLSJ_2pnmK01x3DJkok1AzU0npn9Sc7AZyqxL31u_8t6G-4mWvzBQbLCcBC1b2yF8--NpJCRYc0MIx5QzAczJy8kcmNI_rocU6TukGSSmoJo5Jxd5sZYXwdmkd1wh3-N401OMWX32Eqg_kCQnXi61hHKnzuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخیره هسته‌ای فرانسه از ۲۹۰ کلاهک در سال ۲۰۲۵ به ۳۷۰ کلاهک در سال ۲۰۲۶ افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126433" target="_blank">📅 09:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGyeuXNph9wa6FgtBubv8EgQNk0xyBUc3D-k5Vfr90m0s08QefhpDTvYG7GM0EQOXmkpQ_3LfZ6yebi21xMEqdnmhc8MP8S3opTpagqUysdwk8v3_daiyA7ZHMMPQPXn3HVoHsWs7eZ0_HimgTKvN125zlTkD5TUGKXJvQcXbkHFHCOUr4fS0zMiZhGOtAXkgu1TNIBuZFEA4oMUTER-i3Ym-tCNJ3wH9zTqBhlYd-JXVC3p2Ma_AfipeJVm3dEmieZE1EfulX6UIBAqFk4iVXNwN_SqmacmcrcUtUG0tahdugp7j80gwaBoxBBLHeO2GZSvC66f9Mkx8Co5UtZXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: همه ما در قبال حفاظت از محیط زیست مسئولیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126432" target="_blank">📅 09:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=sJXLYtuPPnhUt3LDR5Y44VuTZ2XWjmio367sYr5EdhrHmaWeXifIpROYGQkN68SAYY-4xz_rXXoRu1a2IW2rts11qLsW3AbdKq2lvW4pMjVTaod2G8sgMBooWIYyfNYpbOKc0Csyw3716zJyjsrPgfaIGM09FUwt84d7KwXqnaXzDlcqcYnn5u17k-F8AC587jamVF7e38Cr8DOD88dYX87ueMniyiRwGXEDNHtl4lsRXQihprzpBWDexwsNQd4YuWfrddlOpwOld32hcuAOMwoeSwvNDCz0BTb61-uYJ4LrtkCSfOBs_k7EBTlk51JvHNxO8l-Y4dWJIoSQQz1xSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=sJXLYtuPPnhUt3LDR5Y44VuTZ2XWjmio367sYr5EdhrHmaWeXifIpROYGQkN68SAYY-4xz_rXXoRu1a2IW2rts11qLsW3AbdKq2lvW4pMjVTaod2G8sgMBooWIYyfNYpbOKc0Csyw3716zJyjsrPgfaIGM09FUwt84d7KwXqnaXzDlcqcYnn5u17k-F8AC587jamVF7e38Cr8DOD88dYX87ueMniyiRwGXEDNHtl4lsRXQihprzpBWDexwsNQd4YuWfrddlOpwOld32hcuAOMwoeSwvNDCz0BTb61-uYJ4LrtkCSfOBs_k7EBTlk51JvHNxO8l-Y4dWJIoSQQz1xSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا ظرف دو هفته آینده «پیروزی کامل» بر ایران را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126431" target="_blank">📅 09:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad6e09e52.mp4?token=bTvjC0GiQViy7pF63MJMD7cyLUzB-8Z1rhWsvJndTdVFR5SECcuwwE3y0CadiOKK4rMbouy7cuBjRzPoIR4TPefN-Qe6q4zKswJ68I8rd0uG08kYywMggaBnZFGeDjTZVc4lJ0JRE-qxarp6uKqx_1VD_buSwIo8twcjGLKLY6XivnLq_AFiwz6RyexijhICDq1M-5rlo1XlT-kfL_xiwrwvigQatokkS4shm-2YjgqBmyKQjRdwUqeZDs2cS5HzPi0tpPeP-RjRql0ATnzf42HS5QDJn4yzmuk3ZwwU53YfZR-CDHfook6Yoyfqlt74a9jHd72mzbiJsUXqUmzuIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad6e09e52.mp4?token=bTvjC0GiQViy7pF63MJMD7cyLUzB-8Z1rhWsvJndTdVFR5SECcuwwE3y0CadiOKK4rMbouy7cuBjRzPoIR4TPefN-Qe6q4zKswJ68I8rd0uG08kYywMggaBnZFGeDjTZVc4lJ0JRE-qxarp6uKqx_1VD_buSwIo8twcjGLKLY6XivnLq_AFiwz6RyexijhICDq1M-5rlo1XlT-kfL_xiwrwvigQatokkS4shm-2YjgqBmyKQjRdwUqeZDs2cS5HzPi0tpPeP-RjRql0ATnzf42HS5QDJn4yzmuk3ZwwU53YfZR-CDHfook6Yoyfqlt74a9jHd72mzbiJsUXqUmzuIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا از نتانیاهو خواستید که علیه ایران تلافی نکند؟
🔴
ترامپ: "نه. من گفتم کاری را که درست است انجام دهید، اما می‌خواهم هر چه سریع‌تر دست از این کار بردارید. چون آنها باید دست از این کار بردارند، این به لبنان مربوط می‌شود و باید دست از این کار بردارند، ما می‌خواهیم این کار تمام شود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126430" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
غریب‌آبادی، معاون عراقچی: شورای اتحادیه اروپا در یک اقدام مزورانه، به اصطلاح تحریم هایی را علیه برخی افراد و نهادهای ایرانی در ارتباط با تنگه هرمز تصویب کرد. هیچ ارزشی برای تحریم‌های اتحادیه اروپا قائل نیستیم.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126429" target="_blank">📅 09:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رئیس پارلمان لبنان: ما خواستار آتش‌بس کامل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126428" target="_blank">📅 09:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل: هنوز به متن نهایی برای توافق دست نیافته‌ایم/ ایران و آمریکا در حال پیگیری و تبادل دیدگاه‌ها و نظرات جهت رسیدن به این متن هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126427" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQJDlwX2oZNr1jTciKhDin5usJ21RCJNEsCmMRgzYOxrRz_Q4Lg6cyG2pgGvGpS7YydHXPodmRz3_usAQVOr_vcEyb02CIzZP4NlNvn6OqZELvBQnXguaZVaTkAqF7Fb8mz93Lr-DREqIQNppas5FYa56od26b5fviIc2beh3qFQOZp1O6_5xZuWusJplo2fHnAPcoR1vUdAbOtu5aLRDjLo_SfXpTdOq9kJpT5yjNlwTUbElj3bGU7ALHXkPHQ0oacc5jZV1wTPi3auWbQD24xg_ICvdwuAsw3Rb-XO38mIFHadEqr735xhQooiO-staNO3fai-v6wuB-L7LvBjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون رئیس جمهور امریکا، با تأکید بر اولویت منافع ملی ایالات متحده، اعلام کرد: واشنگتن به دنبال دستیابی به یک حل و فصل پایدار و طولانی‌مدت در موضوع هسته‌ای ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126426" target="_blank">📅 09:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/017bc45150.mp4?token=fqKlI_LysWflcQP3yR1Cjq_EjEUSZiDxUfcGwg2WyQZD2GWTDtGN1EV4X-kSnADpDv9IQ7w1dXK2flC4VzFvTX6ED9W4s2ELeuGVl2VD_6c2jf5oQ3kKSdbifi_-bNz1ql23SI-L8jyi1snEJRg5_fM-8zHC8aSpAyOYCyaT9dOBQJx2MGqyvWaemEpNMaHgZVoF2vXVC2WpycYYSBpMaTKkWW9s3z_W2zwAXOfi9LQNuAGdPk9geDvBGbDAMaL3Cq1OUbjli95iex1wWQd2xedW9PjHled7Cr8nCnjhsdHh_lFVgxVfUACfcjyw2rjdG8vRk7ghG0k7dOhfDMzlag" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/017bc45150.mp4?token=fqKlI_LysWflcQP3yR1Cjq_EjEUSZiDxUfcGwg2WyQZD2GWTDtGN1EV4X-kSnADpDv9IQ7w1dXK2flC4VzFvTX6ED9W4s2ELeuGVl2VD_6c2jf5oQ3kKSdbifi_-bNz1ql23SI-L8jyi1snEJRg5_fM-8zHC8aSpAyOYCyaT9dOBQJx2MGqyvWaemEpNMaHgZVoF2vXVC2WpycYYSBpMaTKkWW9s3z_W2zwAXOfi9LQNuAGdPk9geDvBGbDAMaL3Cq1OUbjli95iex1wWQd2xedW9PjHled7Cr8nCnjhsdHh_lFVgxVfUACfcjyw2rjdG8vRk7ghG0k7dOhfDMzlag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126425" target="_blank">📅 09:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
منابع لبنانی از دو حمله جنگنده‌های اسرائیلی به شهر النبطیه در جنوب لبنان خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126424" target="_blank">📅 09:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از منابعی:
یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
🔴
هنوز مشخص نیست که آیا این بالگرد توسط آتش (پدافندی)‌ ایران سرنگون شده یا دچار نقص فنی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/126423" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
زمین‌لرزه ۵ ریشتری سرگز هرمزگان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/126422" target="_blank">📅 09:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سقوط یک فروند بالگرد نظامی آمریکا در نزدیکی تنگه هرمز
🔴
نیویورک تایمز:  یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
🔴
هنوز مشخص نیست که آیا این بالگرد توسط آتش (پدافندی)‌ ایران سرنگون شده یا دچار نقص فنی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/126421" target="_blank">📅 08:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ دربارهٔ ایران:
«ما الان داریم مذاکره می‌کنیم، و آنها می‌خواهند یک توافق بسیار خوب انجام دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/126420" target="_blank">📅 02:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=IEkR2o6u_d522TtnesRx1ssofaWGZVP8Q2E1Bp5MZEPAVl7kCS9yUFMNGUtjs3T0CCCaUcUtsqgShlceChPRDjT46xub13Eurkegku7D13ZWDtUWDccJJO94hl37bJNvgwTX6NkEQCcNGP2LWaxXvYueoKuTBFR0busL1MKuc9l5_ySC2F6P-jphx3xqrlADMSIZPKP32hRSZp-AKZv_k5gjA7bvqXQCzOknal6mkPPGsPR2Bd-7MdV_XJUfeM-xhPKwA3f1vzE9rejrxYDnePfTWQbrMOVEWjGAXYpSSHqWVzn8xsO58OlNzWnBM53nllirOHwmp6qxfkTg894W2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23d700fa.mp4?token=IEkR2o6u_d522TtnesRx1ssofaWGZVP8Q2E1Bp5MZEPAVl7kCS9yUFMNGUtjs3T0CCCaUcUtsqgShlceChPRDjT46xub13Eurkegku7D13ZWDtUWDccJJO94hl37bJNvgwTX6NkEQCcNGP2LWaxXvYueoKuTBFR0busL1MKuc9l5_ySC2F6P-jphx3xqrlADMSIZPKP32hRSZp-AKZv_k5gjA7bvqXQCzOknal6mkPPGsPR2Bd-7MdV_XJUfeM-xhPKwA3f1vzE9rejrxYDnePfTWQbrMOVEWjGAXYpSSHqWVzn8xsO58OlNzWnBM53nllirOHwmp6qxfkTg894W2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا ظرف دو هفته آینده «پیروزی کامل» بر ایران را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/126419" target="_blank">📅 01:51 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
