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
<img src="https://cdn4.telesco.pe/file/tGzl99DTxpMYOc03avwktwhPr1Ug2QqI8isfIt_NvNRFPWdSn-5pI4b80idjKbnsm7U2HOBnF-ipKQ-UNWctSL5lbCN2qB3KTcge1uw-SGV3uvXT5uIeYRI0lDVO8Q37AnUwPSJDuccTqXS1mr6SdYkjeQungtc2LOL5V1PK9eGbRGX-g8gyId3SU_gggTzhu_M8Zzc1rk1GH0UYhORFRxJk-juR-G8omp2B8i4c_zgAkMH5Wr1RZlSFhijyUBohqCXk4Uqq2aSErseUpXh7aQoPpF2q9IVsUNaGb8JWJot_keM2MMyzXogK26DabfbRnQAaI_-bsOVik3AaxZ-P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 04:14:22</div>
<hr>

<div class="tg-post" id="msg-143466">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر نیرو: خواستم یه خبر خوب بدم به مردم عزیزمون اونم اینه که از هفته بعد قطعی برق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/143466" target="_blank">📅 02:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
برخی گزارشات حاکی از آن است ایالات متحده امتیازاتی به چین داده و از این کشور خواسته هیچ محموله‌ای را بصورت زمینی به ایران ارسال نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/143464" target="_blank">📅 02:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حالا این وسط یه سری عکسا هم پخش شده از جورجینا و اون پسره
💢
مشاهده تصاویر  فقط قیافه پسره
😐</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/143463" target="_blank">📅 02:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سه حمله هوایی نیروی هوایی اسرائیل علیه جنوب لبنان. دو حمله به مناطق شرقی شهر کفر رمان و یک حمله به منطقه القنطره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/143462" target="_blank">📅 01:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: رژیم ظالم را نابود خواهیم کرد آنها درحال فروپاشی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/143461" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: امروز در سحرگاه ما حمله مالی به ایران را آغاز خواهیم کرد که بزرگترین حمله در نوع خود است.‌‌
🔴
هدف ما این است که تمام خطوط اقتصادی را که رژیم ظالم ایران را سرپا نگه می دارد، قطع کنیم.‌‌
🔴
هر کشوری که به عنوان شریان مالی برای رژیمی در آستانه فروپاشی عمل می کند، باید انتظار داشته باشد که انزوای خود را با آن تقسیم کند
🔴
هر گونه اقدام نظامی علیه نیروهای ما یا علیه کشورهای خلیج فارس توسط رئیس جمهور ترامپ به سرعت و قاطعانه پاسخ خواهد داد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/alonews/143460" target="_blank">📅 01:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: روز حسابرسی اقتصادی ایران در راه است‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/143459" target="_blank">📅 01:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143457">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=aKA_vMk4oKw_3b3eSCg81nur0E5ERLANZrvzmoqMGUnSejAuiIenhhjb57mZgwSoLaA-eHdRCMD6H0p_c9JeqNGnRiTXGEDWh-RLZwBdQ21uQw8l76-lUB_8xGKWW0V6FLaleOqlJLAEY_pdhIVnHzMPT-1FUMrn5SIaAMTWO0AJs-WpG9mLfrnU4yng6SB8648XWwC1ic6PVBIUYKyVacHKmTwYUF-EPsxEwNlMMZ9HY1rsrlYprMsvFVZLQJi_csT20TozaYR2zyATZZ6_g2PiyY65b5o8jiFkhxej4pzwLgqRTQs1jeiUuUlxbAZG56SZUy_-htHGEJPDLEdZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=aKA_vMk4oKw_3b3eSCg81nur0E5ERLANZrvzmoqMGUnSejAuiIenhhjb57mZgwSoLaA-eHdRCMD6H0p_c9JeqNGnRiTXGEDWh-RLZwBdQ21uQw8l76-lUB_8xGKWW0V6FLaleOqlJLAEY_pdhIVnHzMPT-1FUMrn5SIaAMTWO0AJs-WpG9mLfrnU4yng6SB8648XWwC1ic6PVBIUYKyVacHKmTwYUF-EPsxEwNlMMZ9HY1rsrlYprMsvFVZLQJi_csT20TozaYR2zyATZZ6_g2PiyY65b5o8jiFkhxej4pzwLgqRTQs1jeiUuUlxbAZG56SZUy_-htHGEJPDLEdZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/جنگ رسما تمام شد
🔴
عوستاد خوش‌چشم : جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/143457" target="_blank">📅 00:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143456">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236ae62ff.mp4?token=NDpXqwKGfVH0cdZ7ph5mv6M2d4o8558boYYva5afh65ER7yFShLjNxgnQGU2S1gWnEuT6Oe_IqCKISBXDQ-wJvpz_wBtdZQxzkUfxIkn-JFyAi_XpLdihq5Rk7KscaNTk_nSAtSxXBgmlNw8MM51q0c85mrboTNwx8Bv4iemEt-D8GqJnI0mUeFFJuYFfYGBv47sJ6HuXDXSRr_bb-e13ZBkxxKxUZUBSRtneVOAAztaBxmOasIXvvo2q6MyA4Z8O3htw8z9h9JtbPqQdyWuY_Is4MIay8ovD4Q5INqDTLnN56mH3SU7GGwuBbemiO5zO7YMq9_HQu0zCXFwpF54CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236ae62ff.mp4?token=NDpXqwKGfVH0cdZ7ph5mv6M2d4o8558boYYva5afh65ER7yFShLjNxgnQGU2S1gWnEuT6Oe_IqCKISBXDQ-wJvpz_wBtdZQxzkUfxIkn-JFyAi_XpLdihq5Rk7KscaNTk_nSAtSxXBgmlNw8MM51q0c85mrboTNwx8Bv4iemEt-D8GqJnI0mUeFFJuYFfYGBv47sJ6HuXDXSRr_bb-e13ZBkxxKxUZUBSRtneVOAAztaBxmOasIXvvo2q6MyA4Z8O3htw8z9h9JtbPqQdyWuY_Is4MIay8ovD4Q5INqDTLnN56mH3SU7GGwuBbemiO5zO7YMq9_HQu0zCXFwpF54CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط مکرون دوباره سیلی خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/143456" target="_blank">📅 00:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143455">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=f-rKu4Fcv5b_z6b0DP3y0vMbSPbop83X6ESvNFeJuPYRMNR2PoD4M2bSNI8eVpae9dWsnNsvhCiXqXtfyi1ulHqjEVBansEifA4qCVsimEuY2bgILRjhqQxGFpoF79sMGhD-RJTawKS7kGgKSmfr1I50XwgM3Dt3rfFO6QHlEF_zdagxOmXUSwYbWAlVg5k7ik9vCi4f2WTGxG3D50uu6MS5AO0XxokzH13rHj-0paNaNL7kS5PD02e0v1GMFtf-TStShfRRpNJ6zl2qzXrREICvcHnwIgZwvvRIQk0Jwo_n6jqadFAtCDEHkYYGXVfn0zhvPLYd-op5QxyPJjVCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=f-rKu4Fcv5b_z6b0DP3y0vMbSPbop83X6ESvNFeJuPYRMNR2PoD4M2bSNI8eVpae9dWsnNsvhCiXqXtfyi1ulHqjEVBansEifA4qCVsimEuY2bgILRjhqQxGFpoF79sMGhD-RJTawKS7kGgKSmfr1I50XwgM3Dt3rfFO6QHlEF_zdagxOmXUSwYbWAlVg5k7ik9vCi4f2WTGxG3D50uu6MS5AO0XxokzH13rHj-0paNaNL7kS5PD02e0v1GMFtf-TStShfRRpNJ6zl2qzXrREICvcHnwIgZwvvRIQk0Jwo_n6jqadFAtCDEHkYYGXVfn0zhvPLYd-op5QxyPJjVCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی غیرقابل وصف یک پیرمرد نسل ۵۷ از دلار ۲۰۰هزار تومانی و نابودی جوانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/143455" target="_blank">📅 00:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143454">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/143454" target="_blank">📅 00:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143453">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143453" target="_blank">📅 00:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ایران امشب رسما اعلام کرد از امشب هر نفتکشی از مسیر جنوبی تنگه ی هرمز(متعلق به عمان و آمریکا) عبور کنه جریمه میشه و یا خود کشتی توقیف میشه و یا اموال کشتی مصادره میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/143452" target="_blank">📅 00:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143451">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مایک پنس: ترامپ و اسرائیل دوباره برای «تمام کردن کار» وارد عمل می‌شوند
🔴
مایک پنس، معاون سابق رئیس‌جمهور آمریکا :  «زمانش زودتر از دیرتر فرا خواهد رسید که رئیس‌جمهور و متحد ما اسرائیل مجبور شوند وارد شوند و کار را تمام کنند.»
🔴
آمریکا باید نیروها و تجهیزات نظامی خود را در منطقه حفظ کند تا برای اقدام احتمالی آینده آماده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/143451" target="_blank">📅 23:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143450">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrhEN3nJ7SJhWdiImsRVfhn0IrxfH-iDPnmRQ4_2qPc87dhx3uZ1PBWMMWgEQFdEXLQ_74f1zz-eQw7_YMzccpWbn-hdsQaJ3ai6mgNW3HkQIRKgwrPlwHs28L3P67V2Un7_nJ2b-UMQ39Lt2cM7rusSIbDYSrk5QQrKSRnX03lphuPr_bvkpNjCbxM2uW1qj_B1V5vCOtHzi0bFE-tN9ncW50vMWTmWSsd_hJpfGU6bTfXJQsY61y70M0ccaNmMzzdWuFAKheVg0EMYXWY9d7c3mDqWj3l4d_oUVPtVYQcENvvU1j_OWDg0-TrnWiJNL1W7O6l23oRXvncw-I0bJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«ولودیمیر زلنسکی» رئیس جمهور اوکراین  درخواست‌های برگزاری انتخابات در زمان جنگ را رد کرد و هشدار داد که این کار می‌تواند اوکراین را «نابود» کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/143450" target="_blank">📅 23:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143449">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f7bbad3.mp4?token=piX_Za6NMjug6bqkk3QLYvMym9BObeFjTIKyqq85510Ath3DOKrtzdciQjycOyxKYHTez1iA6PmKnPRIvNJQzvWy8qAm9ZQyuMUYTHJPOgkbuqqHiBWytPqJ9DM0F7Ldn_OQ5Rs__S-jJDoDcnSXX4DMgsyokCAOPzH7XwBPXRLbYr83U6Jf95KX-08cfVVA4cJkAzQpZmzPES9WYHJkROgepl7y_e6vXa7Kew72nQwM-ThbQg3TGaBb7OdDLNDh0ISttOyOTQyZzYMmPudkjxi8Pga24r45YUripOTsYRaD5J-8NkdF_0sPpOtLybbDtojZfrZUVJQasZAlJGEwogMDnAw1VeO7FuxJPsNrgxuIYpbrDJA3mMlKfiBmfw0g-LoxcdQbsSj2k2NlXSxs1aS5O_6IgrgSHsMcaVibZwv37W-euTkIHwT4JzZTUrUvktThmk4DlBGj40O74Syot9FjVTmBAyMnXmXGRis_48f9344HzU6lyhq7Nzk9YrMBdGOaYM8GhQdICbIrIm-jFUxYNFWgvKV_KlTG7nclKNqEGmV4v9HXqGBtznbh4LiP9jgKZ7ARS6gF6_Z4UJG8O6Lb_mdd7QgX241s1enDho5uyxaXThgvMhViseRONtG6sRblVZWDu2qygtkvMG8qtw41FNnfZL_C7MWoT9bg1vc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f7bbad3.mp4?token=piX_Za6NMjug6bqkk3QLYvMym9BObeFjTIKyqq85510Ath3DOKrtzdciQjycOyxKYHTez1iA6PmKnPRIvNJQzvWy8qAm9ZQyuMUYTHJPOgkbuqqHiBWytPqJ9DM0F7Ldn_OQ5Rs__S-jJDoDcnSXX4DMgsyokCAOPzH7XwBPXRLbYr83U6Jf95KX-08cfVVA4cJkAzQpZmzPES9WYHJkROgepl7y_e6vXa7Kew72nQwM-ThbQg3TGaBb7OdDLNDh0ISttOyOTQyZzYMmPudkjxi8Pga24r45YUripOTsYRaD5J-8NkdF_0sPpOtLybbDtojZfrZUVJQasZAlJGEwogMDnAw1VeO7FuxJPsNrgxuIYpbrDJA3mMlKfiBmfw0g-LoxcdQbsSj2k2NlXSxs1aS5O_6IgrgSHsMcaVibZwv37W-euTkIHwT4JzZTUrUvktThmk4DlBGj40O74Syot9FjVTmBAyMnXmXGRis_48f9344HzU6lyhq7Nzk9YrMBdGOaYM8GhQdICbIrIm-jFUxYNFWgvKV_KlTG7nclKNqEGmV4v9HXqGBtznbh4LiP9jgKZ7ARS6gF6_Z4UJG8O6Lb_mdd7QgX241s1enDho5uyxaXThgvMhViseRONtG6sRblVZWDu2qygtkvMG8qtw41FNnfZL_C7MWoT9bg1vc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجسمه "مادر سرزمین" در کی‌یف، پایتخت اوکراین، به مناسبت روز پرچم (۲۳ آگوست) و روز استقلال (۲۴ آگوست)، نمایش‌های نورانی شبانه برگزار می‌کند و در این نمایش‌ها، تصویری بزرگ و درخشان از نماد "تریزوب" (سه دندان) بر روی مجسمه به نمایش در می‌آید.
🔴
این اقدام، تداوم‌بخش نصب نماد فیزیکی "تریزوب" بر روی سپر این مجسمه در سال ۲۰۲۳ است، که جایگزین نشان قدیمی شوروی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/143449" target="_blank">📅 23:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143448">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcaa486ed.mp4?token=MJbV3bBsF6pjZYRd_9fzrkXjBsvHe7YBgtHWYh5LO8kNNTT3iV_VczJRS1yIYRlUGye57kXRrOosNsyYsn8dr6KX77UHQ-rZRvnRV7g0W7X6jp05PkttxV-CnNL1VTb0IEYKvLDT0Ka-87b3iO7dAY1CkYFb_94Asn8Xi9Bc_-0VP_5JfabN22QNdN7DUaeXf_fFnNlYav-CP0u4t1u2U8Nonk_E-yNof-r_qZD3_CvRi3pAbJMlrXFoWjhQdaFFrVZhU-UfFXQZFX4oRHfdJoSHAo-0gxttOb3XDyKJjkYfCB0lk90pqGvVUkiCTsPSJ851tlostBF_-1-MbxIywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcaa486ed.mp4?token=MJbV3bBsF6pjZYRd_9fzrkXjBsvHe7YBgtHWYh5LO8kNNTT3iV_VczJRS1yIYRlUGye57kXRrOosNsyYsn8dr6KX77UHQ-rZRvnRV7g0W7X6jp05PkttxV-CnNL1VTb0IEYKvLDT0Ka-87b3iO7dAY1CkYFb_94Asn8Xi9Bc_-0VP_5JfabN22QNdN7DUaeXf_fFnNlYav-CP0u4t1u2U8Nonk_E-yNof-r_qZD3_CvRi3pAbJMlrXFoWjhQdaFFrVZhU-UfFXQZFX4oRHfdJoSHAo-0gxttOb3XDyKJjkYfCB0lk90pqGvVUkiCTsPSJ851tlostBF_-1-MbxIywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات انسان‌نمای چینی رکورد پرش انسان را شکست
🔴
یک ربات انسان‌نما در مسابقات ربات‌های انسان‌نمای پکن توانست ۲.۸۸ متر به‌صورت ایستاده بپرد.
🔴
این رکورد از رکورد ۲.۴۵ متری پرش ایستاده انسان که خاویر سوتومایور در سال ۱۹۹۳ ثبت کرده بود، بیشتر است.
🔴
این ربات همچنین رکورد ۰.۹۵ متری سال گذشته در مسابقات ربات‌های انسان‌نما را بیش از سه برابر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/143448" target="_blank">📅 23:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143447">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
دلار هم اکنون 200,500 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/143447" target="_blank">📅 23:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143446">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
دویچه‌وله: هرمز، اقتصاد عراق را به لبه بحران برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143446" target="_blank">📅 23:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
حاجی‌میرزایی: دولت از وجود گرانی‌ها آگاه است و تلاش می‌کند قدرت خرید مردم را حفظ کند‌‌‌. حمایت‌های کالابرگی را برای دهک‌های پایین را افزایش خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/143445" target="_blank">📅 23:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbac205b5.mp4?token=RjYFiguVnXnCo9RT14e0vpcEPi5Mn5j3qsp5kp4ct7ZJER61kVIbl_e9JYvfLnv4ngvNdns7HsoU-oa13V9e3-uZXrEt8Vf-WAYRsIsTZOU2Tz9u2YD3fioieDVjNa5cXx6LtqWVhNd83BsHe665gDXR9swg4H6t3wAoLWmEX_Rzj52MmqzDJeaDAE8WKzhBx_46fdurW9ugjS-KM0zD4wvgThbmDt-PVHciYdszRXGyewspzEIfF5zVbA13HCSLzU2XWXncd03tvnoH8oQGDXdRt6yMsqoPT6DT3frYvTIHj5k3bW2OXFhnjaDMDtyeME-rOXm-ZPljBtWXEEWy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbac205b5.mp4?token=RjYFiguVnXnCo9RT14e0vpcEPi5Mn5j3qsp5kp4ct7ZJER61kVIbl_e9JYvfLnv4ngvNdns7HsoU-oa13V9e3-uZXrEt8Vf-WAYRsIsTZOU2Tz9u2YD3fioieDVjNa5cXx6LtqWVhNd83BsHe665gDXR9swg4H6t3wAoLWmEX_Rzj52MmqzDJeaDAE8WKzhBx_46fdurW9ugjS-KM0zD4wvgThbmDt-PVHciYdszRXGyewspzEIfF5zVbA13HCSLzU2XWXncd03tvnoH8oQGDXdRt6yMsqoPT6DT3frYvTIHj5k3bW2OXFhnjaDMDtyeME-rOXm-ZPljBtWXEEWy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر موسوی؛ پزشک:
روزانه کلی دختر میان اینجا که همشون ویروس HVP (زگیل تناسـلی) دارن و بعضیاشون رو مجبور میشیم رحمشون رو تخلیه کنیم. یه خواننده معروف هست که تا حالا ۵ تا دوست دخترش اومدن پیش من و همه رو آلوده کرده.
مراقب باشید که با هرکسی نخوابید.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/143444" target="_blank">📅 23:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d1960c5f.mp4?token=gDfbQK-dyXvH4_Q9462bH7Fix803uL2rgOwqI1mHqfKP-W-aJBnpvpsa-A4i9Rp-QkcnVZKGa7kuXGIJBOuSgBvZ4Hrtq4OQONi6K_W0KFWU5JbwfEHlVhavUnsxN8sd7uxeZqOkunFYds51dTci6f3vZwOLz5eTfZEJ9Hy_lztrPQrm9XHxBPQHdoHwZNJmOC6TjH6pHy9NAw3DetPi77zR-L3Oj7f8kRkmTRxg9qEtqfLAgk9RxUmKf6bRVD7mt4ilJFMKXLOzJcc7P0PmT3Nn87jbPGJcXMPAkymRzh9D3hbe1aWdLz61Gv4Z43aQyAcaZZMbNUd68d0UuM6s6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d1960c5f.mp4?token=gDfbQK-dyXvH4_Q9462bH7Fix803uL2rgOwqI1mHqfKP-W-aJBnpvpsa-A4i9Rp-QkcnVZKGa7kuXGIJBOuSgBvZ4Hrtq4OQONi6K_W0KFWU5JbwfEHlVhavUnsxN8sd7uxeZqOkunFYds51dTci6f3vZwOLz5eTfZEJ9Hy_lztrPQrm9XHxBPQHdoHwZNJmOC6TjH6pHy9NAw3DetPi77zR-L3Oj7f8kRkmTRxg9qEtqfLAgk9RxUmKf6bRVD7mt4ilJFMKXLOzJcc7P0PmT3Nn87jbPGJcXMPAkymRzh9D3hbe1aWdLz61Gv4Z43aQyAcaZZMbNUd68d0UuM6s6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یادی کنیم از
#رضا_نوروزی
، پهلوانی که از شاهنامه آمده بود.
🔴
من برای این سرزمین، میجنگم. برای بازگشت شاهزاده رضا پهلوی، میجنگم.
🔴
من با جمهوری اسلامی و رهبران روس و چین میجنگم.
🔴
می میرم! برای آزادی تو، این فرزندانم،
کوروش بزرگ و داریوش بزرگ را به تو میسپارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/143443" target="_blank">📅 23:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36986be7e4.mp4?token=stpOd5K0hnHtJkDFYLvQBKIwVtFq1RFR9iWzdA3pWmjXmZrIQFgUSEq9WACKo_tNY1gdTEppL9zqHaDvddvkp3Qtcg5744IAZVCteqYqaEsBjftGDthapHusyTsrjwrvuXLWzyuPC0on-GfsXiouC-mQj7yRKOmpe83qC2BmmVLIVluUDQ3aYC6CENHMPSdOFLtxGkfj_K-JiWZ0j7Vltl6nsS_QhdxqbI9zkiVrHtrA_nDfeqqK9fw_QE26rNqiOtckKxgqXPRnTNYY7vOEDvkrAwAgEUeQ17YruJz2KrAR98TSX-6CR7uhgENDQfaOs0qylqgSadDZySqOlrsEGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36986be7e4.mp4?token=stpOd5K0hnHtJkDFYLvQBKIwVtFq1RFR9iWzdA3pWmjXmZrIQFgUSEq9WACKo_tNY1gdTEppL9zqHaDvddvkp3Qtcg5744IAZVCteqYqaEsBjftGDthapHusyTsrjwrvuXLWzyuPC0on-GfsXiouC-mQj7yRKOmpe83qC2BmmVLIVluUDQ3aYC6CENHMPSdOFLtxGkfj_K-JiWZ0j7Vltl6nsS_QhdxqbI9zkiVrHtrA_nDfeqqK9fw_QE26rNqiOtckKxgqXPRnTNYY7vOEDvkrAwAgEUeQ17YruJz2KrAR98TSX-6CR7uhgENDQfaOs0qylqgSadDZySqOlrsEGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین در حال آزمایش «ربات‌های پلیس» برای گشت‌زنی و کنترل خیابان‌هاست.
🔴
در شنژن و هانگژو، این ربات‌ها با دوربین، رادار و هوش مصنوعی می‌توانند با لباس عملیات ویژه برای شناسایی موارد مشکوک در خیابان ها تردد کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/143442" target="_blank">📅 23:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
محمد مرندی: حملات آمریکا به ایران در روزهای آینده مجدداً آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/143441" target="_blank">📅 23:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رئیس دفتر رئیس‌جمهور: قرار نیست کالابرگ همه مردم افزایش یابد
🔴
برخی از مردم نیازی به کالابرگ ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/143440" target="_blank">📅 23:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362a915d77.mp4?token=DoVq5nB97XYf36aUYuyrMBsKiit59hQih6VfS-ymMF_hYeE4qhuXigGWcUQddvKBg1ULj89uD5CmkblTMUWesVCU6EiqQditqbZ215fFh1kzMqKWSJMY3BNaz8dZN_WlhQYeEosgovsEsUIP5gbAlRXCuEcNlx5fIJYebX4Ek-pSR9w7n04mIH2-AFULa0gWN5545yStM9ca1LXVRuJXHtVNmYNeyyh3-Y75mpL6HVbsLmdg2Eb_B2pwEpg7oI__5iSr_eX24H_3LMtz8CMVJ9sZfCu-cBXOrMt6C_Ae7lymWMSVkL0kqRS1Eh4M1J2gjwto79lYUzqYcNL3T_H0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362a915d77.mp4?token=DoVq5nB97XYf36aUYuyrMBsKiit59hQih6VfS-ymMF_hYeE4qhuXigGWcUQddvKBg1ULj89uD5CmkblTMUWesVCU6EiqQditqbZ215fFh1kzMqKWSJMY3BNaz8dZN_WlhQYeEosgovsEsUIP5gbAlRXCuEcNlx5fIJYebX4Ek-pSR9w7n04mIH2-AFULa0gWN5545yStM9ca1LXVRuJXHtVNmYNeyyh3-Y75mpL6HVbsLmdg2Eb_B2pwEpg7oI__5iSr_eX24H_3LMtz8CMVJ9sZfCu-cBXOrMt6C_Ae7lymWMSVkL0kqRS1Eh4M1J2gjwto79lYUzqYcNL3T_H0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس دفتر رئیس‌جمهور: قرار نیست کالابرگ همه مردم افزایش یابد
🔴
برخی از مردم نیازی به کالابرگ ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143439" target="_blank">📅 23:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
به گزارش کاربران اختلال در اینترنت شدیدتر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/143438" target="_blank">📅 23:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
هواپیماهای جنگنده اسرائیل همچنان به نقض حریم هوایی جنوب لبنان ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/143437" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143436">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
متکی وزیر اسبق امور خارجه: ۹۰ روز اینده بسیار مهم است، ترامپ می‌خواهد ایران را مشغول تفاهم اسلام‌آباد نگه دارد تا انتخابات را ببرد و بعد به سراغ ما بیاید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/143436" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143435">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNgeIb9Q9wob0hyvUOcpegH4CGs6WqSq2iZeK9aPQXmL6WNW4iytXIXIAsCkx1C9KhejphvEeDF8HmhBhpXz6YmpzfRfEbT046p1elGwOmk5GqrW9xld92JcMWmvIPKJa4rVxQNX5LiKXVtpa8Mr7ReilXiaaKDh657FjgUX5x26NpS6GQx_qYdZ2tRtGOiOkVqLo5BpizMGHuGrSO2bNmpODbgUcKN7AUJApINoW2Bfkyyg_dBmtB6AQFVQ50EHMyZ99vatX_8VTS2HJQ38X0L8qaeHhRxTKzrTsOdFt-1Gu4zycPngqphjjqvNhphbH62gGE6tRad8ouwttayDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
رضا پهلوی: قیمت دلار امروز از مرز ۲۰۰،۰۰۰ تومان گذشت. امروز قیمت دلار ۲۸،۵۷۱ برابر زمانی است که جمهوری اسلامی به قدرت رسید.
🔴
حاصل نزدیک به پنج دهه حاکمیت فساد و ناکارآمدی در جمهوری اسلامی فقر، فساد و ‌انزوا برای ملت ایران بوده است.
🔴
تجربه این پنج دهه یک مسئله را برای همه روشن کرده است: در جمهوری اسلامی اصلاح ممکن نیست.
🔴
قطار ایران در بهمن ۵٧ از ریل تمدن و پیشرفت خارج شد و امروز جمهوری اسلامی آن را با سرعت هرچه بیشتر به ته دره هدایت می‌کند.
🔴
امروز وظیفه تک‌تک ایرانیان از جمله کارمندان دولت و بدنه اداری کشور این است که به هر شکل ممکن با اخلال در فعالیت‌های مخرب جمهوری اسلامی و‌ تضعیف آن زمینه برکنار کردن رژیم و‌ نجات ایران را فراهم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143435" target="_blank">📅 23:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143434">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق: ما پیشنهادی را به ایران و عربستان ارائه کرده‌ایم تا یک شورای هماهنگی امنیتی واحد ایجاد شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/143434" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143433">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0_nGXj9rKzDqbyvwriIT3WbyEmXlAH1id-XdaOE4a5jR-aHnijSS13QdWa3S7jiJBiNLYdP8R7VFm-Ln65Xjm6IBakiRm2FteWaEO5RdFEry0SyO9AAyRAW8JCS4GgJOxaf6OA0LANdWAjB7Rj4KecijjpdQI08_2nKtWRiqwZLnoXd64nCcOPCVeD0l2X61HOmpM9w154EInfXYIAaf6H7ycj5eUqIrGVBaiVXe1-84Sa_wFgG432xCpTw1DBpmvLo2g6QNLPpfcplwENCsh4fzn1fb7C_ihwpqQb53rIQAfpthyd_FEJD0m65fP7DwJ3TVoKYgFPIq0P_uH7TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری که حمله هوایی اسرائیل به تپه علی الطاهر در جنوب لبنان را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/143433" target="_blank">📅 23:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143432">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=R2h5_4ptXD9NZqwnO9xbysBWy3cQm4BQvrgFvBI-ZfGTMP-bN9iCVa8Hy8YDUKmlP0-I6husW-BBqN9ZIsgpM0AuZf6W-OUO1jlNa4_u5qC_pBYTNN0ARNWne4WRyPKLXnfKoIjVk0idjTfxbcBNlXOaCB9BGXl_cTomuX17xYorBAdf1EnOkSNc-T66BTe-_N_VSvB9i1QImMTGufuIdETFS8TvzkPe57mLg9fMRBl7k8GfpU5ukfiKiFFNYc91J54f9UI3-FObekWnHi4K4-hvFghLHdtG5-i4N97ex3dtXfADV0FC_DtcE8mJoa4vjp6Q36bV3qVizPXObyUDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=R2h5_4ptXD9NZqwnO9xbysBWy3cQm4BQvrgFvBI-ZfGTMP-bN9iCVa8Hy8YDUKmlP0-I6husW-BBqN9ZIsgpM0AuZf6W-OUO1jlNa4_u5qC_pBYTNN0ARNWne4WRyPKLXnfKoIjVk0idjTfxbcBNlXOaCB9BGXl_cTomuX17xYorBAdf1EnOkSNc-T66BTe-_N_VSvB9i1QImMTGufuIdETFS8TvzkPe57mLg9fMRBl7k8GfpU5ukfiKiFFNYc91J54f9UI3-FObekWnHi4K4-hvFghLHdtG5-i4N97ex3dtXfADV0FC_DtcE8mJoa4vjp6Q36bV3qVizPXObyUDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس دفتر پزشکیان: قرار است جانفداها به سراغ ۵ میلیون مشترک پرمصرف برق بروند و بگویند صرفه‌جویی کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/143432" target="_blank">📅 23:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFHjrZslQ40n-EAMBcpywgxFU5PHc0Fx6DcK4d9Cx3TKDYQRLAPBQWWDbr4Y5K8zdLkR96ge5z6uqNRMBdOJeNkJzgopjJzc3xFZEUtsRSxVCzZABjG_mZ-IXEFVOxg29yVHP8hPsZaUxDUc9ckSxIJvgY_pSslSm1aJ0OlIhLPGs_DeburZsl7gUAYSnm6isl5kkiSY7jdNacWjYDu0hcZa8RVGPyUyOp5b3-FjUKG_RTQHCIuo2AdAOpY03t1eoc1EZlLg3Gw1Sgiu6eDtuwdLpQfaloUHws9XV48tcUdpzbH9VmSUROKHcIrldWcjNabmD1Lto2SXYTKDXtRNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به ارتفاعات دبشا، در جنوب لبنان، انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/143431" target="_blank">📅 23:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
گلوله‌باران توپخانه‌ای اسرائیل شهرک «براشیت» در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/143430" target="_blank">📅 22:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
طبق گزارش کاربران وضعیت اینترنت خیلی خرابه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/143429" target="_blank">📅 22:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143428">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4GULPdelHIMlPUdQkk9XC0mXYHs6wZiGAP8sW5B0v1X_GewRKBo8b1cfuFKYWLvx9t_hmKXhRSy7xrbTk9dXuEIBd-GnBFJJ3h93ahrQJ4H5Y0M5Tec7FSpXghy2zCmnSIo4iObqg7GceWt7izIAdCUPw1AEPQUCAn875PkcVXR-5-iUyd_sNgzqR-F7alG0wgPLy7e-VZX5zs8YV3XU2NzznSq3racaoK-_lrNfjvXqB8Log_2VB7QAHWm1xQd7kkuoO-MkqHRpTydDPz_RmjJOPA54kSwsiVss6UkSKKZoZJpGyOEcAdjShvZlf8fz9Ww1oJHSoXQvlEwA7N9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی: اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت نه از طریق تنگه هرمز و نه از هیچ کجای خلیج فارس صادر نخواهد شد.
🔴
ایران مشارکت یا حمایت هر کشوری در جنگ اقتصادی آمریکا علیه مردم ایران را به عنوان یک اقدام جنگی تلقی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/143428" target="_blank">📅 22:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143427">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=nV0lbRo-vnf-dBf57Bm3VHzO9EV0rWl217rFeFN_blit5ixe3GfPqFmGGKv-JoK8Ut7iyk6-dVJqXmyBgaOJ-QK32y2UdM3Ontkcdpl6p9prtI-Bdv9W5zicqSJqfJ_WrM8zmnnOFJoCxJXs75vC5Xk0y1yUMOWsEDnkYS6lp6jL_WqN0ge914Dh1HydsgeAKATFhXzGgjX9OceoKx-4hVcPImkTJK9hPk52LiIPyEmMCA8KevpvX-YqkLeJGwy1nEsNB3z-0XKJ_9AoiQF2iRvAXDGyazyMPaz0tLtsAUgNZChRJxp0G-EE816r3lWGzrkthmE0upTzA3xo_LSntw0k1sfWNIccO6f4prU8X0onOPhMqj2nRF9CiJX0l5C_DE1jYrFP40mztAplJkwWzzJOFiPGUsipQVABfP0YwKnDha7MhOP0mmNIYnSfl0Vq5rEu-cCb7u54Kfd3mUROKR5IYTHUbXpKntp7u1lVTj0EZWd0D29ZJDDJc5oq-dqIy0y-vZZAULMrGCi7PwgOYVckp8Qp_9ypnPelicKvqEUuogFtb6VEfBQaqfwx0v3QJx1rqcOdHzd4XOVx1xAvSUVdbSy22At6HjNWIRhftZjU9eh7LtR6rAywFQNmzmoUF_Uhx0E9oiAN2optbjV518ALI_TJSeqRI6LFuSoKT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=nV0lbRo-vnf-dBf57Bm3VHzO9EV0rWl217rFeFN_blit5ixe3GfPqFmGGKv-JoK8Ut7iyk6-dVJqXmyBgaOJ-QK32y2UdM3Ontkcdpl6p9prtI-Bdv9W5zicqSJqfJ_WrM8zmnnOFJoCxJXs75vC5Xk0y1yUMOWsEDnkYS6lp6jL_WqN0ge914Dh1HydsgeAKATFhXzGgjX9OceoKx-4hVcPImkTJK9hPk52LiIPyEmMCA8KevpvX-YqkLeJGwy1nEsNB3z-0XKJ_9AoiQF2iRvAXDGyazyMPaz0tLtsAUgNZChRJxp0G-EE816r3lWGzrkthmE0upTzA3xo_LSntw0k1sfWNIccO6f4prU8X0onOPhMqj2nRF9CiJX0l5C_DE1jYrFP40mztAplJkwWzzJOFiPGUsipQVABfP0YwKnDha7MhOP0mmNIYnSfl0Vq5rEu-cCb7u54Kfd3mUROKR5IYTHUbXpKntp7u1lVTj0EZWd0D29ZJDDJc5oq-dqIy0y-vZZAULMrGCi7PwgOYVckp8Qp_9ypnPelicKvqEUuogFtb6VEfBQaqfwx0v3QJx1rqcOdHzd4XOVx1xAvSUVdbSy22At6HjNWIRhftZjU9eh7LtR6rAywFQNmzmoUF_Uhx0E9oiAN2optbjV518ALI_TJSeqRI6LFuSoKT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری عجیب در استان گیلان، که یک مرد در دفاع از زنش دو خانوم دیگر را میزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/143427" target="_blank">📅 22:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143426">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a7ead4df.mp4?token=bYsiJcrMmpM-yYtr7r8_oq2mTrF0OUC8PtO3eYLdw3fvJnH-tzgx7-MTT8HB5J4sQT5k3O0qnGoj0olHOd0Dd1nxb2C0Tatxx7N1o8zzt4qIyzTQYFURuBFncUNH6lBru5YSaFlLM6EDu7sGKdaS0o-1rz3rK1hoIwak5CgzksVQltK9ldlMFzTUHQPTis-R7XdyeTGceplzhdFBdea6RPLPaCb_x6NBA81_10WN8vNhRcryV9enXdlFSd3fbg-KBrzqSTI9e3QpY2FIBKjAEtcdY38T6guoEANREhIfflytP9sUMQi39zuuwR5LdHJjcV6LSRbg_FSCm04ftziURpEF8spT3mNGvl0Z_xsC4QnfpSOrmWACfAQBKq89Z7hvcx5Jzs0O5M18WQ8aviJlaCfHU5VagCyd-3AoRe3HlCShloHtNUso8-ucxrDmyjOJN19gkezpXjfcZkaNYwcOPd2m3R-ZhqB1146C9OxuYVA9c7l69e2jfqVpFfkRJMzq7Dwhmv4F9LEY0hwbeRR8dIl1SPQe1MFo32ho_88iAGrVnpFQpR4SHBFvC1xByc_-hPy3Dcu0Jlqswva4ulyvL4qVYC3GVXAFBrcly92uuwDTDUnrcBNN6k7nEmcAA5jGts0S5fFa0AP8634a5_0ZswcInWZEwaerewBTuhbjlmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a7ead4df.mp4?token=bYsiJcrMmpM-yYtr7r8_oq2mTrF0OUC8PtO3eYLdw3fvJnH-tzgx7-MTT8HB5J4sQT5k3O0qnGoj0olHOd0Dd1nxb2C0Tatxx7N1o8zzt4qIyzTQYFURuBFncUNH6lBru5YSaFlLM6EDu7sGKdaS0o-1rz3rK1hoIwak5CgzksVQltK9ldlMFzTUHQPTis-R7XdyeTGceplzhdFBdea6RPLPaCb_x6NBA81_10WN8vNhRcryV9enXdlFSd3fbg-KBrzqSTI9e3QpY2FIBKjAEtcdY38T6guoEANREhIfflytP9sUMQi39zuuwR5LdHJjcV6LSRbg_FSCm04ftziURpEF8spT3mNGvl0Z_xsC4QnfpSOrmWACfAQBKq89Z7hvcx5Jzs0O5M18WQ8aviJlaCfHU5VagCyd-3AoRe3HlCShloHtNUso8-ucxrDmyjOJN19gkezpXjfcZkaNYwcOPd2m3R-ZhqB1146C9OxuYVA9c7l69e2jfqVpFfkRJMzq7Dwhmv4F9LEY0hwbeRR8dIl1SPQe1MFo32ho_88iAGrVnpFQpR4SHBFvC1xByc_-hPy3Dcu0Jlqswva4ulyvL4qVYC3GVXAFBrcly92uuwDTDUnrcBNN6k7nEmcAA5jGts0S5fFa0AP8634a5_0ZswcInWZEwaerewBTuhbjlmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آجورلو: تنگه هرمز بسته است؛ عبور نفت به ۲ تا ۳ میلیون بشکه رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/143426" target="_blank">📅 22:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTNMj4_TzkC-BWlYdoFItDzTHRDHjdlX3PZipA2Qx2CWpU5XG5EC_MGUDEZ5Uds4C4387chr4pkkAG-ZIURzwL5leQ9v2AiKluHVUIlrvkO57jy9F5xC1AMzIPhK9yE0H-kPUuvUtxNH-xLQwyw57uG1zw-mYpO24hPuHQnB_JEwv3L8gcOxTYAHe2a0uhi5U4zEo61Pe__UZzn_NLXYf6dr11RXS71Pi7YAyoI6pDiupVTjWKqxdVZUI4hcaFu7PntZ-K-Lcwu34ajYaNn1dnZ33jwGyvdyLtHOaOG2wwMTnRrH0F2k1xtmsbhvsnfMzh2GDRuK9Z2VIsaT-2DrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد زیادی هواپیمای سوخت‌رسان نیروی هوایی آمریکا امشب در اطراف تنگه هرمز فعال هستند و یک فروند هواپیمای گشت دریایی P-8A Poseidon نیروی دریایی آمریکا نیز بر فراز دریای عمان در حال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143423" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvvUKRDRmanFLOXbP7YUG3nbUk5JEj6vxV2oteSLlCuVkTeXI4o3wCwpRSKRCCIwvLSo5jWB5s0iHxbSwOnm3Mw6zEmS7Id_d696c7HM6I8IKAXRJiGG6fT-83RlSaMIuq5T7rJ7T_HbHFmYB1PZSKGYfxmCHcXphEh72hW0pirow-SvUsszDU4q-78n2lCXEhpf8bfYm5-9gIjA56b6E9dHIJnObAwOPY-OfE-soZwET5EnOS9v4fGgk35a9uEwL12yJPxXR-Z-dgmEHZ9m7uMAOyg_oa-0O4yQ3-ue3Mu6JVY4CbnF8_S2uNbA6Q65k8BFE6qAXCZI30UvBw-wWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید محمد مرندی
:
«احتمال اینکه تو روزهای آینده دوباره درگیری نظامی شروع بشه، خیلی زیاده. هر کشوری که با ترامپ برای تحت فشار گذاشتن و گرسنه نگه داشتن مردم ایران همکاری کنه، شدیداً تنبیه می‌شه. اقتصاد دنیا هم در آستانه فروپاشیه.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/143422" target="_blank">📅 22:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اداره تنگه هرمز: ‌ کشتی‌هایی که از مقررات ترانزیت ایران از طریق تنگه هرمز تخطی کنند، با محدودیت‌هایی در سفرهای آینده خود مواجه خواهند شد. صاحبان محموله‌هایی که به خلیج فارس و از آن سفر می‌کنند باید فهرست به‌روز شده کشتی‌ها را بررسی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143421" target="_blank">📅 22:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
از زمان سقوط بشار اسد تو سوریه تا به امروز ارزش پول سوریه در مقابل ریال ایران ۵۳۰ درصد افزایش پیدا کرده، یعنی بیش از ۵ برابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/143420" target="_blank">📅 22:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb908fde6a.mp4?token=iXOcXp7dFtIQ4N1MUhgfmC7-q3TM8ZGccgZ90vxmUeRZHkllC_1nmqMy47he-Vg7c8YuMHxn6y399IGiI4O15lv0bDlnfvzB-1QHlvod1ABHRQi1lfauwKFHe1JZy36NqRMjbafRYCdy6paFHh3rcsTLT9GmQ5Ip_WgKZBhSm0Lb0kRkmBWGfNVQ0nyJ4czDyzm7S30d6BsINuimDCbhI1gXgwjJ_xmYiQ4bSfTMYByQi0ooRiwY0rhqxW9n_-FYOCN4UxGKfGp6Am5MNZk3GUWzhvnwKZ8QOv_hKsxmVujsnH7_fG-IVMUPhJQMnMvTlycySyjtMEpxaAeH6Zsqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb908fde6a.mp4?token=iXOcXp7dFtIQ4N1MUhgfmC7-q3TM8ZGccgZ90vxmUeRZHkllC_1nmqMy47he-Vg7c8YuMHxn6y399IGiI4O15lv0bDlnfvzB-1QHlvod1ABHRQi1lfauwKFHe1JZy36NqRMjbafRYCdy6paFHh3rcsTLT9GmQ5Ip_WgKZBhSm0Lb0kRkmBWGfNVQ0nyJ4czDyzm7S30d6BsINuimDCbhI1gXgwjJ_xmYiQ4bSfTMYByQi0ooRiwY0rhqxW9n_-FYOCN4UxGKfGp6Am5MNZk3GUWzhvnwKZ8QOv_hKsxmVujsnH7_fG-IVMUPhJQMnMvTlycySyjtMEpxaAeH6Zsqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات های انسان نمای چینی توانستند امروز در مسابقه دو، رکورد یوسین بولت، سریع ترین انسان دنیا رو بشکنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/143419" target="_blank">📅 22:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/143418" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال ۱۵ عبری: دیدار وزیر امور خارجه سوریه و رئیس موساد مثبت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/143417" target="_blank">📅 21:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd6uy6JgXvowmlDa8tJTRbm3V5uvcBCYXIZh7zsxR5Se0PX9291inodBbQKY68x_pz2f0NLAixlfuIORJbToRrn_taeb2iH0Yj4m8CoqlbVU4Mb-BJA8_cNr2-2C0ZQy38WwL4UVNOmwR-AopWqKlGNOLqaUDm3oaPysrwOcMYjINm9qKHQTjRS73vQqwzvcHajX42PL-Xy_WKjDQNkkZ1JQo1lV773bFRy3zbBkRh6Jx9VnftJj4Q1VpUAE4V8ev5OqRDf_FZQ7t_u-lTg5UPWdmwdAzLfMs0Q0ZIqbFSKl2NNS1bBYsyazXOCRwr5NnR-mhOyp9CDPDRCi-SX3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس ابوعلی سینا روی اسکناس ۲۰۰ سامانی زده می‌شود!
🔴
با دستور امامعلی رحمان، رئیس جمهور تاجیکستان برای پاسداشت ابوعلی سینا دانشمند بزرگ ایرانی،علاوه بر اسکناس ۲۰ سامانی از این به بعد عکس ابوعلی سینا روی اسکناس ۲۰۰ سامانی هم زده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/143416" target="_blank">📅 21:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e471f88ae8.mp4?token=OqQDQNa66xs3lKd4KXFOE9dExPC_15aEMUsi0CYbzW9SrWu6WDGvH5hVHDio1wsqWeo4z5wFBA4LjGJFbTt0E5Gdk300Wj7wYFFYQjTBqpjTK4OAwMMPjgu-_eZS2zeRAYKA4f4fVp9HWjz9y9t3zhsoJmQ3UqG2g_vd0TvtBiamAOJPm0mYFca0o9pbN35FxTnn_rgqRkXvZAgwjah7teIwfMmPkp89oeQNpLHCIHVtHxuOAaEY25UaCco8rvDre3pI_k98NpnaV0x_XxCCrz0EMRPfCXm4XAvWpEqabT4_Z8jm2MEtKqKDRw-NtMhYTVx7VXfHOqsGhtk8LHXLIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e471f88ae8.mp4?token=OqQDQNa66xs3lKd4KXFOE9dExPC_15aEMUsi0CYbzW9SrWu6WDGvH5hVHDio1wsqWeo4z5wFBA4LjGJFbTt0E5Gdk300Wj7wYFFYQjTBqpjTK4OAwMMPjgu-_eZS2zeRAYKA4f4fVp9HWjz9y9t3zhsoJmQ3UqG2g_vd0TvtBiamAOJPm0mYFca0o9pbN35FxTnn_rgqRkXvZAgwjah7teIwfMmPkp89oeQNpLHCIHVtHxuOAaEY25UaCco8rvDre3pI_k98NpnaV0x_XxCCrz0EMRPfCXm4XAvWpEqabT4_Z8jm2MEtKqKDRw-NtMhYTVx7VXfHOqsGhtk8LHXLIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: صبح تا شب درحال تامین ارز هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/143415" target="_blank">📅 21:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
روزنامۀ انگلیسی تلگراف به‌نقل از منابع اطلاعاتی غربی مدعی شد روسیه کارزار جدیدی برای خرابکاری علیه شرکت‌های دفاعی اروپا آغاز کرده تا زنجیرۀ تأمین تسلیحات اوکراین را مختل کند.
🔴
تلگراف به آتش‌سوزی‌ها و انفجارهای مشکوک در تأسیسات دفاعی چند کشور اروپایی اشاره کرده، اما تأکید دارد که دخالت مستقیم روسیه در همه این حوادث به‌طور قطعی اثبات نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/143414" target="_blank">📅 21:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143413" target="_blank">📅 21:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیرنفت: ۱ میدان‌گاز جدید ۷ تریلیون متر مکعبی تو فارس کشف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143412" target="_blank">📅 21:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4ejR6Y0-KimjTJV5TUxjWlFWH_qotojtUv5gC7Ezfxuezc127osd7qTUzCHuHgMUCAE6PNzLOUTZE-qXREdF75TbNLg0TjGRZCM397EHHC3SLypvT_GNcxdqvQVZjCr8rth40HeIttwOeACRmEUrxeryREoR9HChLRHxy5xnVaazWrJp2HoOo-a7OR0Wp3jwVvRo-fS6nlzycBO8YYMrSMagLBoM1ZsCKWbu0bM8oxbE7TFNlJ8cF2LvMvPqguzsXtMeT4S1KzcTrjihwty_VqM1uI1_HTACNFXLWym26eeY601_Rk2rX0OL6304JESRSx50PDcZUlSHpd1LnOWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست : رهبران ارشد غیرنظامی ایران برای دستیابی به توافق با ترامپ و پایان دادن به جنگ فشار می‌آورند:
🔴
«ما تحمل نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/143411" target="_blank">📅 21:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86287c9d09.mp4?token=lPp6k7eK-RVSmNz4RJWDAfC4ocmWKCod2JhiarALOcQ0s68-TtP6GsqNA9E88KUbvQUheuCBm0ga-QTlkPMiPb404FqJTo_H7573nEgpY5oYoBQtngD-cS6wyjb_eGnMX8gSa2Prs66YwjkbXpq4kYNtazHYJjVyMfcvAsc3v_mlWEuwuZdYcDVkg3ObmN9UbSq-E9G-owjOT2Zf3QUjVpHwwdcFDFny8rR4R0V_xZa2-r3qlHEtnCihM_1CL5sWH1-bXFH9napTyNolCDEgYxJKnIFcuf3PqTrZzMWC4K6hE2iqkthd2j1Du8FXou5gOSatP3OqfztpeLbRb346lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86287c9d09.mp4?token=lPp6k7eK-RVSmNz4RJWDAfC4ocmWKCod2JhiarALOcQ0s68-TtP6GsqNA9E88KUbvQUheuCBm0ga-QTlkPMiPb404FqJTo_H7573nEgpY5oYoBQtngD-cS6wyjb_eGnMX8gSa2Prs66YwjkbXpq4kYNtazHYJjVyMfcvAsc3v_mlWEuwuZdYcDVkg3ObmN9UbSq-E9G-owjOT2Zf3QUjVpHwwdcFDFny8rR4R0V_xZa2-r3qlHEtnCihM_1CL5sWH1-bXFH9napTyNolCDEgYxJKnIFcuf3PqTrZzMWC4K6hE2iqkthd2j1Du8FXou5gOSatP3OqfztpeLbRb346lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وعده وزیر نیرو به مردم: اگر روندها مثل همیشه باشد، همین هفته سختی‌های حوزۀ برق تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/143410" target="_blank">📅 21:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1bcbd7689.mp4?token=JZi3-SXQOBBTS5mdSis8btzCekDAMjokjF0xdjUMGoV7iIfSUheJU6UcFEtaO2uDYZnsRryTJ5KWVtS_J7gMxUPItKnDZDmkJl2tAv5qstRqKsOBs9VzJgHodqmT71phOzylpfv0i18zRU-rX1ldaPuRV6KNWvcG3l4DkmVYo5cNny3I5kyNuk5wdZZ7xARI_faRYhFL0wZ29KWv6qFXC-AUvfHaMuu7gIskFnQ6EG0gq7vLNyGAGhgDmbJu324GKdGfSza3_da0CDcM5YTAjIPGCR5XVbsjhGc4eLNh4Yk29obCe93cL4r-vplwVQC4cIjQoJDc0WZeyt9_LyqfhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1bcbd7689.mp4?token=JZi3-SXQOBBTS5mdSis8btzCekDAMjokjF0xdjUMGoV7iIfSUheJU6UcFEtaO2uDYZnsRryTJ5KWVtS_J7gMxUPItKnDZDmkJl2tAv5qstRqKsOBs9VzJgHodqmT71phOzylpfv0i18zRU-rX1ldaPuRV6KNWvcG3l4DkmVYo5cNny3I5kyNuk5wdZZ7xARI_faRYhFL0wZ29KWv6qFXC-AUvfHaMuu7gIskFnQ6EG0gq7vLNyGAGhgDmbJu324GKdGfSza3_da0CDcM5YTAjIPGCR5XVbsjhGc4eLNh4Yk29obCe93cL4r-vplwVQC4cIjQoJDc0WZeyt9_LyqfhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در منطقه صنعتی در بیت داگان در اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143409" target="_blank">📅 21:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
واشنگتن پست: بر اساس داده‌های وزارت جنگ آمریکا، شمار تلفات جنگ با ایران به ۷۷۴ نفر رسیده که شامل ۱۸ کشته و ۷۵۶ زخمی است.
🔴
‏حدود ۶۰ مجروح جدید نیز در روزهای اخیر ثبت شده که برخی با جراحات شدید مغزی ناشی از انفجار در پایگاه‌های آمریکا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/143408" target="_blank">📅 20:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40e314633.mp4?token=jV-kg6oecr6ulK20WlsNFVKjNHcLAGwbzN7ilHuRKnx9q_oGckj5XrHVTfNrbKEZQqB5ouuQo6IdJ2hScxWunQoRBNFyFcZX5z9bhEnFrKFPuv9FVXQW0yQ4b7Mjkl5XTvbESiR1cpOgyaO9_ln-QqUNHPSQy2HHybcjtJ-LXq5GIDuYiDEnrEIPKCbbHWw9pkHMa3BRgnqRGVUNGAmBFZs1foTnsDHHwJjX8Hf8_bhcCVo-hfhaE_DMhJ68udrq1mq699X-Jkm5BHWWT8UXoH-FNKrFEkLVW5Wtm9SGoW4h28HPmsfj2aPammqU3c4B5Z2VkgHyd-qRZH8AC61dQaX_THyfjOXuOMOoiDau0Gekl0O_aE7-qguiNaWRofSv9FVp8umrJkxiC7H5jAi_VbUuE8n1ZnMzbamohi2DDro7Ls67LZhNxGGzQvvt6LkMN6aeBE0QEdxFza5g5kXRQOYEEF6aiKZQ8lmrjMIxOMZUji4udKc_7TpcdXTJDxC-6W3vCB753kMDcF-Payfjs3Yq2sRa5HQsEjG5AuCW_E93SgBZvnShZb8As8tZ99HlGKTQOo5hHLwJaRzSd52RKPQhp_k1tl1sMMYrlMDhX0fvBdxw95TlGRbq8uQSy8ju2iR9auo2vj2Ns_M7KDsQ10mIDd0hX3xL2u7a6BiindI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40e314633.mp4?token=jV-kg6oecr6ulK20WlsNFVKjNHcLAGwbzN7ilHuRKnx9q_oGckj5XrHVTfNrbKEZQqB5ouuQo6IdJ2hScxWunQoRBNFyFcZX5z9bhEnFrKFPuv9FVXQW0yQ4b7Mjkl5XTvbESiR1cpOgyaO9_ln-QqUNHPSQy2HHybcjtJ-LXq5GIDuYiDEnrEIPKCbbHWw9pkHMa3BRgnqRGVUNGAmBFZs1foTnsDHHwJjX8Hf8_bhcCVo-hfhaE_DMhJ68udrq1mq699X-Jkm5BHWWT8UXoH-FNKrFEkLVW5Wtm9SGoW4h28HPmsfj2aPammqU3c4B5Z2VkgHyd-qRZH8AC61dQaX_THyfjOXuOMOoiDau0Gekl0O_aE7-qguiNaWRofSv9FVp8umrJkxiC7H5jAi_VbUuE8n1ZnMzbamohi2DDro7Ls67LZhNxGGzQvvt6LkMN6aeBE0QEdxFza5g5kXRQOYEEF6aiKZQ8lmrjMIxOMZUji4udKc_7TpcdXTJDxC-6W3vCB753kMDcF-Payfjs3Yq2sRa5HQsEjG5AuCW_E93SgBZvnShZb8As8tZ99HlGKTQOo5hHLwJaRzSd52RKPQhp_k1tl1sMMYrlMDhX0fvBdxw95TlGRbq8uQSy8ju2iR9auo2vj2Ns_M7KDsQ10mIDd0hX3xL2u7a6BiindI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاندیدای ریاست جمهوری فرانسه، ژان لوس ملانشون: مکرون با هم‌سو شدن مداوم و بی‌قید و شرط با ترامپ‌گرایی، ما را از فهرست کشورهایی که به صدای آن‌ها گوش داده می‌شود، حذف کرده است.
🔴
در اروپا، امتناع از تحریم نسل‌کشی در غزه، کشور ما را در همدستی با جنایات اسرائیل قفل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/143407" target="_blank">📅 20:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FahZ3t84bLv33NrVrCnVWCUlPZjKTbrOUFE7Je4pKIDKFNK1yYwN3-kcjjf_1mFHMIz9EcMMcWnoFHXodbSOQ0NEm8xtLDVDD37VFoPh3kqwKOaso1XrFF-e0tSQPSgx93wYTJI-Ia5K8RRzCYRMTmzRHCq6x9uJ0sToi3tpOJmscNRJq1qZG2pYm2RAJg4jpI0ViO9RmZW2OXxzCNDbB_RQyCMBZTy25XED1W51Uh5vO0l_9bc2r9zxU0Ne5tnq-OMqU9ZHv3L7PLalrHKnzUotKeRvOBpJqDyxv096_vc0FfdXGMiNAoHoOZ-vDQj0Wo0TDXbBb3Jg7Ex33b1Eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فهرست ۱۰ ثروتمندترین میلیاردر جهان که همگی آمریکایی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143406" target="_blank">📅 20:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فاکس نیوز: بحران هرمز با پایان جنگ تمام نمی‌شود؛ تهدید پنهان زیرزمینه / هشدار! بخشی از تولید نفت خلیج فارس ممکن است هرگز بازنگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143404" target="_blank">📅 20:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: در ایام جنگ به رئیس‌جمهور گفتم حاضرید باهم برویم پای لانچر؟ او گفت برویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/143403" target="_blank">📅 20:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روزنامه اسرائیلی هاآرتص: نتانیاهو «اسرائیل» را به جنگی دیگر و بی‌نتیجه کشانده است؛ این بار با ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143402" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نتانیاهو: به واقعیت پیش از ۷ اکتبر بازنخواهیم گشت و به هیچ جبهه‌ای در غزة اجازه نخواهیم داد که جوامع اسرائیلی را تهدید کند و امنیت را تضعیف نماید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/143401" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143400">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8ed5a1f2.mp4?token=sbNsLmJzLZlO1nECnoVX3Mg3eSlXHAzhtTEtdgOiD8LliDIfUAcLf1q6bykkuPbRVmOlXe3odAy9t6Wof5-oWqyY1rVqDHLllv969vXZXnymH9SeLU8lY3Cy-1m8dpFO06WwZwMnB7NnI8DGNC1qQYXthfB26xtoYVTJNHKKXYl_RmPRgg9sU7T1FrjPq4o9DTSAKWSIVvV1lqYRT5rNUsRLMmr0fSsu5nF7ZCT6IR2xRfH2XApR5rqO8Sx6o2PG1oyzIPDiKGfkhl20x_5DM-jiUBU6pus00IfI7-6PLyJX1VHcO2aAk1U5yeEai-p7-wtYYI8QFPUtmmprnKIdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8ed5a1f2.mp4?token=sbNsLmJzLZlO1nECnoVX3Mg3eSlXHAzhtTEtdgOiD8LliDIfUAcLf1q6bykkuPbRVmOlXe3odAy9t6Wof5-oWqyY1rVqDHLllv969vXZXnymH9SeLU8lY3Cy-1m8dpFO06WwZwMnB7NnI8DGNC1qQYXthfB26xtoYVTJNHKKXYl_RmPRgg9sU7T1FrjPq4o9DTSAKWSIVvV1lqYRT5rNUsRLMmr0fSsu5nF7ZCT6IR2xRfH2XApR5rqO8Sx6o2PG1oyzIPDiKGfkhl20x_5DM-jiUBU6pus00IfI7-6PLyJX1VHcO2aAk1U5yeEai-p7-wtYYI8QFPUtmmprnKIdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای اف‌اِی/۱۸ سوپرهورنت و ش‌اچ-۶۰ سی‌هاوک نیروی دریایی ایالات متحده نیز پیش از گرندپری فریدوم ۲۵۰ در واشینگتن دی‌سی، پرواز نمایشی انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/143400" target="_blank">📅 20:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=r5SJYUqWHeP2r_WAEAIcAH00pI5F6R4lqcnEBmH2WsLzZeVHHcUl5hWExumwEQHHQNnzkiVqbOAR1chHysm_MoGZ5so43qV22DJmzm-hyi14OTqRPrVOudyXvQqlL83ee6yyQkooj5MU9zDRDQluYMt-ykgrtA4ZzxGTucsmAqsoDa1bqLT5YOKO8VnQFevycVlQj5Iop0aISe8mHwooZ-pYEaRUgF7PQV4I98NVtwjpp1G9k0FpTL9k572jPlvZqquMKvtlAxqpkNonKbeuOlAb-JEqwjeYkH3wAY-eoQ_DMU-0dNLRVNuivfVrgDmRrOy7XX8w8kTkrvmQBwGQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=r5SJYUqWHeP2r_WAEAIcAH00pI5F6R4lqcnEBmH2WsLzZeVHHcUl5hWExumwEQHHQNnzkiVqbOAR1chHysm_MoGZ5so43qV22DJmzm-hyi14OTqRPrVOudyXvQqlL83ee6yyQkooj5MU9zDRDQluYMt-ykgrtA4ZzxGTucsmAqsoDa1bqLT5YOKO8VnQFevycVlQj5Iop0aISe8mHwooZ-pYEaRUgF7PQV4I98NVtwjpp1G9k0FpTL9k572jPlvZqquMKvtlAxqpkNonKbeuOlAb-JEqwjeYkH3wAY-eoQ_DMU-0dNLRVNuivfVrgDmRrOy7XX8w8kTkrvmQBwGQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هلی‌کوپترهای چینوک، بلک‌هاک و آپاچی ارتش ایالات متحده و هلی‌کوپترهای تهاجمی وایپر نیروی دریایی ایالات متحده، پروازهای نمایشی را پیش از گرند پری آزادی ۲۵۰ در واشینگتن دی‌سی انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/143399" target="_blank">📅 20:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92cabaea4.mp4?token=qz0OQHqo3yRnShmaxAzamtMbSyv8yveHSYoA25IG86ptzIYWo9svzhWoVQYqnyryMffrx8MFyAoI9DB6rgdHrM4uv12tB2_d8DQN7R46OBRmHvsfsQ9MfykHSYN4wWtpnHtW7HAjf8K_BH7XEbd8kRdMWFdk_O6ROwxV_fRRGzeqttjh71ar2W1Z9TVRKkvV4kbfVf1GXhkmKX_JU2DNylJ2xPBX9OgPxOohowTgrvHbbC_wNzX0JRXfhFKNAygIA9zygLb0wL5impndk7OmhSg4IXrlJtfhijCix_skeAAk5RSfU-r-nDOLec6ERlKl84gObcOcNgvlCXYAcUAP9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92cabaea4.mp4?token=qz0OQHqo3yRnShmaxAzamtMbSyv8yveHSYoA25IG86ptzIYWo9svzhWoVQYqnyryMffrx8MFyAoI9DB6rgdHrM4uv12tB2_d8DQN7R46OBRmHvsfsQ9MfykHSYN4wWtpnHtW7HAjf8K_BH7XEbd8kRdMWFdk_O6ROwxV_fRRGzeqttjh71ar2W1Z9TVRKkvV4kbfVf1GXhkmKX_JU2DNylJ2xPBX9OgPxOohowTgrvHbbC_wNzX0JRXfhFKNAygIA9zygLb0wL5impndk7OmhSg4IXrlJtfhijCix_skeAAk5RSfU-r-nDOLec6ERlKl84gObcOcNgvlCXYAcUAP9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: ۴ روز بعد از آغاز جنگ، جلسۀ دولت تشکیل شد. آقای عراقچی در جلسه گفت ممکن است دشمن اینجا را بزند. رئیس‌جهور گفت به درک که می‌زند. من جلسات را تعطیل کنم از ترس اینکه او می‌زند؟ خُب بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/143398" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی دولت: خبر خوش برای مردم، سود سهام عدالت از 2 تا 8 شهریور واریز میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/143397" target="_blank">📅 19:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=maos5zH9rEtML-91cnAPiAjiFrKK4ZO4OoyWIvbXxJGf1I7FQQiJv0UJZr7G1hbGVY2qWHhcSBhvJuMSscl9bo-CNASvz7jRC_MM0Kw5ppdVH7rTvQWvO6G_haq8XhKE1skSab1DzIRdN7sIKmG9KaMACg61TR0j6Nne2tvEq_8IeSuPrO4jv24WqM0N1bdCnXuqEwB81Y0OkRfj2knAb4AhSS-I6q33RLUt7cp97FPeXZO5DwFRBkBfOLGZLjcbDne6ZGjz65Cv76zwwabN6yqYIyctYxAuH7oEWdKhD56f2bhtzGNP2rUW9qu3kIwRTBYBdjs3XtuzD5xgTeDIHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=maos5zH9rEtML-91cnAPiAjiFrKK4ZO4OoyWIvbXxJGf1I7FQQiJv0UJZr7G1hbGVY2qWHhcSBhvJuMSscl9bo-CNASvz7jRC_MM0Kw5ppdVH7rTvQWvO6G_haq8XhKE1skSab1DzIRdN7sIKmG9KaMACg61TR0j6Nne2tvEq_8IeSuPrO4jv24WqM0N1bdCnXuqEwB81Y0OkRfj2knAb4AhSS-I6q33RLUt7cp97FPeXZO5DwFRBkBfOLGZLjcbDne6ZGjz65Cv76zwwabN6yqYIyctYxAuH7oEWdKhD56f2bhtzGNP2rUW9qu3kIwRTBYBdjs3XtuzD5xgTeDIHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔴
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/143396" target="_blank">📅 19:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c129332c6.mp4?token=CcvMNVmDK0ISe32aYixO5uvsFc6p8lL5AFfa2D6_Jm92D_ha3rhMYDEPJIQKYsP8xH5R1hQu2RybwuwmP0wI9g2_sSvJzrvunVJR3fS6egq0VFUOe1PYfU2oKJcnVLV0c3kw8-_Sb1PutRVbuEZbrnNLqutdxbrmwT6GVs1aig-ij4NUHVEeNaX4IHdEhY3ONSZSqq1WmxXibF2HQbbjV10MX_JIeJawEewohSqCnDI4M6Ig8vlPqkxuzQR7pfGfVxIl4kHXOgKD1AaHMxaKNt2zu_8fSnIA2-xncHJv6_uMqt-7dyODaKn9CAR4QkwkDbDn5kGdzXR2-Z9WVZvvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c129332c6.mp4?token=CcvMNVmDK0ISe32aYixO5uvsFc6p8lL5AFfa2D6_Jm92D_ha3rhMYDEPJIQKYsP8xH5R1hQu2RybwuwmP0wI9g2_sSvJzrvunVJR3fS6egq0VFUOe1PYfU2oKJcnVLV0c3kw8-_Sb1PutRVbuEZbrnNLqutdxbrmwT6GVs1aig-ij4NUHVEeNaX4IHdEhY3ONSZSqq1WmxXibF2HQbbjV10MX_JIeJawEewohSqCnDI4M6Ig8vlPqkxuzQR7pfGfVxIl4kHXOgKD1AaHMxaKNt2zu_8fSnIA2-xncHJv6_uMqt-7dyODaKn9CAR4QkwkDbDn5kGdzXR2-Z9WVZvvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودرو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/143395" target="_blank">📅 19:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان: صرفه‌جویی مصرف بنزین باید از دولتی‌ها شروع شود
‏
🔴
رئیس‌جمهور در جلسه هیئت دولت: برنامه‌ریزی کنید که چگونه می‌شود ماشین‌های دولتی و مصرف دستگاه‌های دولتی را کاهش داد و میزان ترددهای ماشین‌ها را پایین آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/143394" target="_blank">📅 19:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=r72qQuXN4_PO4zNefHgD0aRJ68j6PiSuwmWKRHfU-i4DnQsAqZvwo94lF4j2Nqd2zVX6fDEn7Js2vRIJSYAi0yKzw2o2utxqUj6rfDh5mzFwaSOgblALh2GQIEpaCQyL4Z_yJUCmL5fvUov7dEGKMEXFUib6HlWq1-WdlO32rDM_G3c4hhZ9AaINSweYwpg96hbWhlOgrWr-TzhTZMSkGEYKiZd5LhLUY4QoW6XUFmh_qUX2oyWDuU4wATo0UQ2LXFtt6rXkRd31qeClfWtTigdLC-RIG4eRjwDlRIu6FjuIQrd6n0vhzrBRdPMzereh-eIUFGTdbRRzLTwTdjc_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=r72qQuXN4_PO4zNefHgD0aRJ68j6PiSuwmWKRHfU-i4DnQsAqZvwo94lF4j2Nqd2zVX6fDEn7Js2vRIJSYAi0yKzw2o2utxqUj6rfDh5mzFwaSOgblALh2GQIEpaCQyL4Z_yJUCmL5fvUov7dEGKMEXFUib6HlWq1-WdlO32rDM_G3c4hhZ9AaINSweYwpg96hbWhlOgrWr-TzhTZMSkGEYKiZd5LhLUY4QoW6XUFmh_qUX2oyWDuU4wATo0UQ2LXFtt6rXkRd31qeClfWtTigdLC-RIG4eRjwDlRIu6FjuIQrd6n0vhzrBRdPMzereh-eIUFGTdbRRzLTwTdjc_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استانداری گلستان: زمستان سخت در پیشه و قطعا ۲.۳ ماه قطعی گاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/143393" target="_blank">📅 19:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۶.۲ ریشتر در عمق ۸۳ کیلومتری جزیره هوکایدو ژاپن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/143392" target="_blank">📅 19:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143391">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
چاس فریمن، سفیر سابق ایالات متحده در عربستان سعودی: اسرائیل هیچ استراتژی برای بقای بلندمدت ندارد. این کشور فرض می‌کند که همیشه می‌تواند با نشانه گرفتن همه با اسلحه زنده بماند، و این به هیچ معیاری یک استراتژی بقا نیست.
🔴
بنابراین، تردیدهای جدی در اسرائیل درباره دوام آن به عنوان یک کشور وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/143391" target="_blank">📅 19:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZxMDh47rvJgm48qVWOgMAl2doTt2bn2P93zCaffOG7Hzi5zqytfR7QG_-odnYvIEbR1G9lN7spNyOCMlSZ0SetcVGNFtnPqnUMNNaMhg-3uKI6RYdsLD1go6V9c99yO02LHngooyvHFcTvajVvgPF-JjaLZLM06NEt6SNK_M5o9lNH2kT7nQCe2fvzNQUGt2IVX2z8XHpe6nADs7bKlEzx2XnfeMsOaZn6Rl_cze0qwyECbeH9oGle1TyPFFN1v-GsxQpuyenbF85QpSZpD-gmnsM0CbNYYXuR93c6dQXE9jrh_FGWCDljCs32EWQtfJpyDu2YYbPyc1xyvDhpiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار مشاور امنیت ملی پاکستان با ولیعهد بحرین
🔴
ارتشبد «محمد عاصم ملک»، مشاور امنیت ملی و مدیرکل سازمان اطلاعات نظامی پاکستان با «سلمان بن حمد آل خلیفه» ولیعهد بحرین دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/143390" target="_blank">📅 19:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
آکسیوس: وزیر خارجه سوریه، اسعد الشیبانی، امروز در اردن با رئیس موساد، رومان گوفمان، دیدار کرد تا تنش‌ها را پس از حمله اخیر اسرائیل به یک پایگاه هوایی سوریه کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143389" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد
🔴
این هزینه‌ها از کشتی‌ها به ریال یا هر ارز دیگری که مورد نظر ایران باشد، دریافت خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/143388" target="_blank">📅 19:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کمیسیون امور داخلی مجلس با اصلاح قانون گذرنامه، اعتبار گذرنامه افراد ۱۵ سال به بالا را ۱۰ سال و افراد زیر ۱۵ سال را ۷ سال تعیین کرد.
‏
🔴
این مصوبه برای تصمیم‌گیری نهایی به هیئت‌رئیسه و صحن مجلس ارسال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143387" target="_blank">📅 19:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL9hxGqtDl7imf02CzesC8IDFGXbbNAAU_LUQQS6yR5Rh2rQ6IH48h1dhfsCAwcb-m8nKs4zzlmzTVhILe3XQ5GBDeeTfPOJ-GHU8fXIR151lwU02DpmRWH3wxOyF3bDuhRjKeu4Nwo_b8Y6oY7cW5GlgLrgtoMG5wgM6gQ5psEMlsNz2xZzk1Y983-1jPGFExGDSVCoI7H1Hxly57slU0uL2Fs3BNMTaYHW9J352jTlf7FFpa3m2dH0n-uyUnFhZaPEoAOTCzl6SK69Y64hi7a8PpsoN2DonZq9HpfATUO86aNqHs9RMNMbdwsFEH6Pn5br7W7MLytkniIknd2hNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/143386" target="_blank">📅 19:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
مجری صداسیما: گوشت بوفالو از گاو بهتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/143385" target="_blank">📅 18:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvpHKAIH6QgyjziryK9PGEM5YcINOE_IZM8XNaMkasHjQCUxO3t1e7A1m_LSc5Bd7tqiv_i1WssKKtD11ceRQaQLNX3UDC8eqNoMoxGvrm2q1YTVS5tF0THjWJfdi7udNHUD0PXSPOqGYn8iFaGfVnFzmj5r2spkdg61IHosnTuovpm0Mh1Q5a2kwl6bkpM7UnueRvbualgUXt_s2hKO_x75eob84vJ3L7h7P_yEzHSCzH9Lq-tuo5AmYPMo0SZo0BXerBER-1uqCFoRx4BJAf_tIOB6GkGxm0wbCW5_ecGe1ROajeGVcyvItaJykWPEf7xnZGuI5HVTpi8v_c3_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد سامتینگ، رئیس مجلس شورای اسلامی:
واردات گوشت منجمد برای اصلاح قیمت‌های گوشت. خب، شاید این کار جواب بدهد.
برای اوراق قرضه چه برنامه‌ای دارید؟ آیا اوراق قرضه منجمد وارد می‌کنید؟ خریداران مسکن منجمد برای مسکن؟ حقوق‌های منجمد برای دستمزد؟
یک سیاست خارجی منجمد، اقتصاد منجمدی را به همراه دارد.
تنها چیزی که هنوز در حرکت است؟ بومران ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/143384" target="_blank">📅 18:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-7eW3fAa5LJ9VTF5_pcPkGQYyX8_sGOr2Ugf7_Baj-2SitgWx6nsFWF7Gxh8yy4J_lCaXSx2zGw7-z72HVWZdC05ngZ3ru6_lWiM2Fo7WaU5bmIHha-f6uOnVvg12og-pnUhtVCsr3jvztTchGIpgOwU-bzY2LQ_E55vkIHeLRmLPuPlbGQOJ24VwwG4vFNb2OhAo30xAL3I-FncvkJ4Af5Q9UGecAiAxy53GPrAowR5OAt2qJccNudh1moEXQRmOldWZkh2CoR7UI6D8zvcrnfCrE2bZbYfm-1a388X8SWa-WlaEm2-LAy6udSLPG2U9wq56S3yCa0SmmuI4fcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان:
آقایون حواستون هست وضع حجاب خرابه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/143383" target="_blank">📅 18:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نیویورک پست: تسلط ایران بر تنگه هرمز درحال از بین رفتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143382" target="_blank">📅 18:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
کمی پیش، گزارشی مبنی بر تلاش یک تروریست برای سرقت سلاح از یک سرباز ارتش اسرائیل در محدوده میدان ریمونیم دریافت شد.
🔴
سرباز به سمت تروریست شلی کرد و وی خنثی شد. سربازان ارتش اسرائیل به محل حادثه اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/143381" target="_blank">📅 17:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
آسوشیتدپرس: سفر عاصم منیر به تهران با هدف کاهش تنش میان آمریکا و ایران و ترغیب دو کشور به بازگشت به میز مذاکرات انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/143380" target="_blank">📅 17:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
قیمت یک اسپرسو تک در کافه بابک زنجانی 800 هزار تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/143379" target="_blank">📅 17:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZepV2ozYyrao106qScXrmD1QE78fVApaO17GCuP6UYtJVPVthKkrdONfaMekfXdhdKI1ekL1dbrKMS8YahTVWsBvncgoW2M4saeBxb4ic2tENdyRGI8khroWGjRE1ru9imB_abzNeO-e_jvRVtCqOERstNtxT8T3gaKM2aKvUi1KXI5qocDJ3usmSi7Qto1NVxJiJUCBeN5VR3CiTto4URcIHQ46BsnRvzVrdkwHbgeq-I3P1HZftXhHtpxaNyazFLvfcbu7Zq83dLq-y1T_vy_fslfN_K0fV03-znLfmHdK4h4dCzyfDjOo1aXNNIcSShyeecVUbhZkDYUUfnMDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی؛ تحلیلگر نزدیک به حکومت:
تغییر قیمت بنزین منتفی شده و قرار تا آخر سال قیمت بنزین همین باشه ولی قرار سهمیه ها کم بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/143378" target="_blank">📅 17:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe7bef062.mp4?token=BhTjowCCaIR_ajmMBcH1eYsIu5dAn04h45GxMm9rhuF7bbUzvV1PE3F90FxLeekKYakSfXRjt1ffQ7rQfpKrSWL_FGqQrNZoOtzL7vJeuT1V3L06z1wAIHQEFOW5KY3-y4h2jQXM60waKq4NkpvIdwUjwHdcjQBf05tBucFHrHKnauXWEqlp91gxEI5UCnoKQIFLATE8K4VEYsrcKgguTymXTe3AimZm4nE1WuxXDaI2wy9eGrUd4K8HTAaB36i5c7oeG4kCGL1pLP91SfQ_CKtBohvi5qSlCgnWyLI6xoXobFmMfHLc3jz-Ujrf6t9pa6jGe56Ti0llSaJZ3UojVT_Kb4mDktIrr9cwvbgekJWexH-aPr7cvy7jwZ0pb_42QHAifkT70yMfnDVZsv2kFVkL_FnB99fKv1LFy1JJaN7D8lO4PDpPYd_s8R95UHWcUkI0pueQNzA_Mdubn4-06gSK3F5v5it2p3IDiCGbjiTdmz0YNucRT6r29PZInguY6FKa5jLDdcQA_8SHiyB0hjucHQi6QHSD6v_s9KCSvZ5dLXXprXAGjXtmNdB_8axOLc6Wn1HACknLqJLbypVzntrApEBmpJvZGHbf6pqmSHoryfriBlpnwzb7SULdD0Svve97ddf9iqPIQMGitaazRF88JMj1TiUj3UGk83cCtQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe7bef062.mp4?token=BhTjowCCaIR_ajmMBcH1eYsIu5dAn04h45GxMm9rhuF7bbUzvV1PE3F90FxLeekKYakSfXRjt1ffQ7rQfpKrSWL_FGqQrNZoOtzL7vJeuT1V3L06z1wAIHQEFOW5KY3-y4h2jQXM60waKq4NkpvIdwUjwHdcjQBf05tBucFHrHKnauXWEqlp91gxEI5UCnoKQIFLATE8K4VEYsrcKgguTymXTe3AimZm4nE1WuxXDaI2wy9eGrUd4K8HTAaB36i5c7oeG4kCGL1pLP91SfQ_CKtBohvi5qSlCgnWyLI6xoXobFmMfHLc3jz-Ujrf6t9pa6jGe56Ti0llSaJZ3UojVT_Kb4mDktIrr9cwvbgekJWexH-aPr7cvy7jwZ0pb_42QHAifkT70yMfnDVZsv2kFVkL_FnB99fKv1LFy1JJaN7D8lO4PDpPYd_s8R95UHWcUkI0pueQNzA_Mdubn4-06gSK3F5v5it2p3IDiCGbjiTdmz0YNucRT6r29PZInguY6FKa5jLDdcQA_8SHiyB0hjucHQi6QHSD6v_s9KCSvZ5dLXXprXAGjXtmNdB_8axOLc6Wn1HACknLqJLbypVzntrApEBmpJvZGHbf6pqmSHoryfriBlpnwzb7SULdD0Svve97ddf9iqPIQMGitaazRF88JMj1TiUj3UGk83cCtQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو حاوی غم بسیار زیاد
🖤
🔴
پدری که خرج عمل بچه‌‌اش رو نداره به بیمارستان پرداخت کنه و دنبال اینه که گوشیِ تو دستش رو بفروشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/143377" target="_blank">📅 17:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سنتکام:تا۲۰ اوت نیروهای آمریکایی ۶۷ کشتی تجاری را تغییر مسیر داده، ۳ شناور را از کار انداخته و ۲ شناور را بازرسی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143376" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
برخی رسانه ها از کشف ۷.۵ تریلیون متر مکعب گاز طبیعی در جنوب استان فارس خبر دادند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/143375" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVRezwmQkHpk7Km3s8Hy-ejgCJ0PoqJB57-GiTV3lSbTyWriEhLtze2uWv3WxC65xlK9pR461IjgIzBLAMFlfRgLNBQtQGj8K9tIX9XYwUER3jeiiqh65zQtuGP1BnER4xWRXr7bXYsYwgrI4-AOaxK5JlGR2jsV-0HMGvLP1eAzP-uU0fSiZoWJ93HZ-XBSrTPhCOCUFa15TeBMfjAFtpSypVWmtkIAl3m5H90prz2i6Fx6_7M8qwtgC2S2XmnroggHelQByJKNo1pA42TV1OcSW3NSFx0skIkCpVKEdBJRWktEurDDb_dcvD7XeGQP0tbHYsQ_hoeb_Zh8HucoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی: آمریکا از ما میترسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/143374" target="_blank">📅 16:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
میدل ایست آی: ده‌ها پایگاه اروپایی از عملیات آمریکا علیه ایران در جنگ ۴۰ روزه، پشتیبانی کردند
🔴
انگلیس احتمالاً مهم‌ترین حمایت را در میان کشور‌های اروپایی ارائه کرده
🔴
فرانسه نیز اجازه داد هواپیما‌های نظامی پشتیبانی ایالات متحده در پایگاه‌های این کشور فرود بیایند
🔴
بلغارستان هم که از نظر جغرافیایی تنها به واسطه ترکیه از ایران جدا است، به واشنگتن اجازه استفاده از پایگاه‌های نظامی خود را داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/143371" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143370">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره گزارش داده نخستین کشتی کانتینری کره جنوبی در یک سفر آزمایشی از مسیر قطب شمال به سمت اروپا حرکت کرده است.
🔴
این اقدام در شرایطی انجام شده که برخی کشورهای آسیایی به‌دنبال مسیرهای جایگزین برای کاهش وابستگی به مسیرهای پرریسک خاورمیانه از جمله هرمز و باب‌المندب هستند.
🔴
تحولات امنیتی در آبراه‌های راهبردی، کشورها را به سمت بازطراحی مسیرهای تجارت دریایی سوق داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/143370" target="_blank">📅 16:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143369">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a41e39b9.mp4?token=nTmS__vI1LqqgFUnK54sQXM7ulV5equClQWxPC_RtRJOz4uOIt2HUJAXupdFNOcPQNoj3iB7vAFAXY4nmoEKIxG1SmsTyyFk5WHg9r9ZNkleKhtnOnXPwAPWQRKJ5lQsTLulFhf503kzzqQVewz5nRTGS5YNszaJiD3sdTYOQ03_sX0xYKzf9ymN3sQmDcCrrLdP_U-uttP4HRAqqqt0E1YC4UaO-wpu89Y7iAz9cdk8DnwCDDxz7f3sKF9C0QtEhjkNFR7712IkfbebMS4SlI90yP1bFO-O9FuKiZDUyLxkhIQ0sLvzedkcTEmL2X4U13W0QBclI6jaTFVKIxCIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a41e39b9.mp4?token=nTmS__vI1LqqgFUnK54sQXM7ulV5equClQWxPC_RtRJOz4uOIt2HUJAXupdFNOcPQNoj3iB7vAFAXY4nmoEKIxG1SmsTyyFk5WHg9r9ZNkleKhtnOnXPwAPWQRKJ5lQsTLulFhf503kzzqQVewz5nRTGS5YNszaJiD3sdTYOQ03_sX0xYKzf9ymN3sQmDcCrrLdP_U-uttP4HRAqqqt0E1YC4UaO-wpu89Y7iAz9cdk8DnwCDDxz7f3sKF9C0QtEhjkNFR7712IkfbebMS4SlI90yP1bFO-O9FuKiZDUyLxkhIQ0sLvzedkcTEmL2X4U13W0QBclI6jaTFVKIxCIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الزیدی، نخست‌وزیر عراق: دولت ما به یاری خدا عاری از فساد خواهد بود... چرا که به‌هرحال پولی در کار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/143369" target="_blank">📅 16:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THvlE8UuLmCofchHDYDw7yOK3Mk6tLklhHv6G_5s7t7LNT-X6ieszlCFybshlFrep6O6XlQLGsgUUz6vSLDahtuyIGbT_IEJB9hj14CsBeYZ6J0CSE4mz1CfKpnDj9861GB4_0MQ6CrUmBRZ6SSDrayjMVW1KsHPDUHSC1K_Nt18cdMcTdQQ46IDWMU6rkdUnTznUm843v7MuVGDSLB6ViVB2N5gdNgRBe5KgGXiAaLusoJ47sFatXhvGca2pNw_6wzKiWAwcl7cOGIxxNhczyKpjCIFxlfuZwoMW-Bs_WC594NMWWz4RaHJBTmbTWImNZUfcL-rLxREUhKwPyhvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گوشی موبایل هم برای ایرانی آرزو شد!
🔴
لیست قیمت انواع موبایل ریجستری در بازار
🔴
یکشنبه 1 شهریور 1405
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/143368" target="_blank">📅 16:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=dIrA__c5e6OrJZmCSkOHXwllwVQpmWdhtZFzLeiABfHhDvVT2EDS17fzU5dj2WhfH56oAjBCE4EML7WO95LEIHGoueWS2Slkg2IKY9pBb5ABcLe-VJ7nmJ9tLHlCrx2eKiYUzGFCMZfr_GMfDS-UoZIgROuRhGR1Xxt92MchRuL1z1KyQsb_3jCLe2gj2hsj_wzbdWI09sRSQ23ZO1c0S_cKHZyVOMqHBkHKo0Jvbma0_v9ON11FCmNejn5KyUUjDcwVOUubNowhGUPDk7t300YP7ZUUuCg0Pu0EZQnnK7TjtEMQr6tToUSGVCy_yaGCLe8roFFLLi9mes1CVpvi2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=dIrA__c5e6OrJZmCSkOHXwllwVQpmWdhtZFzLeiABfHhDvVT2EDS17fzU5dj2WhfH56oAjBCE4EML7WO95LEIHGoueWS2Slkg2IKY9pBb5ABcLe-VJ7nmJ9tLHlCrx2eKiYUzGFCMZfr_GMfDS-UoZIgROuRhGR1Xxt92MchRuL1z1KyQsb_3jCLe2gj2hsj_wzbdWI09sRSQ23ZO1c0S_cKHZyVOMqHBkHKo0Jvbma0_v9ON11FCmNejn5KyUUjDcwVOUubNowhGUPDk7t300YP7ZUUuCg0Pu0EZQnnK7TjtEMQr6tToUSGVCy_yaGCLe8roFFLLi9mes1CVpvi2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متکی: ۹۰ روز اینده بسیار مهم است، ترامپ می‌خواهد ایران را مشغول تفاهم اسلام‌آباد نگه دارد تا انتخابات را ببرد و بعد به سراغ ما بیاید!
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/143367" target="_blank">📅 16:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyUPreHR76eDXbSKm6mFhngo4rmLVO6SjG7952hv0I6gYJQibj545ACVDporpbPfIdHUDYFUErhTzamDibkLHbyTtFtKuYETOlUd6VlVKJIlPrSI3oserT0U4MvdQBf4rKjCCVw2tuMQltVwmCqTqvTjEMwgyFEDd__dXfFm-Kqoekwv4u_YfxcU4JvHMHHvrBAsEa6YRQIMLosDmh7emKw-doUMXnDfQbhdG5-Vu51MhYUMMhCGSDsrDoO1n86i436tYoP31hkgc0J9By3xoF3gn8ys3xiRztRw5-VVYPVPLjxpbp2gmK09mjBHOqgWq1PD1Z0QdLqCCdFJ89NNAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مقصر گرونیا دولت هست نه نظام مقدس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/143366" target="_blank">📅 16:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kciextJbLto_FEYatiafoyNxsFNvXkIckIHUaDrQ2_M8oEUrY21SAy20_LJnLXg42HHoH8fGTSlDuiTqmw_3XcFDxvK_aQ2r8miekmO1xtvRymiQERQ5HtLTsU4JFcY8USRZKN0SMzqeMHbT5WsEBM6VKxiWCSXJhYhszrbGdEHH6mgpFe56Wj9FLnBjYNwTR7ptVZQ-WYWAh3S-4xexCCbGz0G61tV8IYRh7Ru5cUKY4k37KQcsHwu9P_dWtJKvP4XML1L6C6wroHEV1TfuN6FIv-5k88-QG64gVb14KpD1I-nuDEifAyx-j_1GJFYJ3awPw74cls-sMNzBvSQUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی در پاسخ به یک مخاطب: حتی گل(وید) هم‌میتونید تو خونه پرورش بدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/143365" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85fea5882.webm?token=W3VL3RrRaM0IVdZU78xzdntKqO1fUtsIBtesZCT2ojIB-JC-KfYREcblsR59ATpr8mQb-oTIOp6n-7qZc_5D-6jZV-LOzx7TPSgAf3zMgUF5acCCq5uceKNEzC-qb-4BOY9aGzLPlk1t0Hs09zIPUfykCfaCz_ivdAKMd536i0lKGfat5I0TxPROewktpzqNX67BwzVAjiIAJpyP8DAA3aGmUb96KaAshikAGh29TW2dVlmATeBuyppMDJpSzDK23JVYMJvr88ICoM4480Gwt5Q3e_814z4cmGs2CxYUXLjh5OH0tNgaPntuAikXqTeT_4ZU-HghhAW0gVC-F-sXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85fea5882.webm?token=W3VL3RrRaM0IVdZU78xzdntKqO1fUtsIBtesZCT2ojIB-JC-KfYREcblsR59ATpr8mQb-oTIOp6n-7qZc_5D-6jZV-LOzx7TPSgAf3zMgUF5acCCq5uceKNEzC-qb-4BOY9aGzLPlk1t0Hs09zIPUfykCfaCz_ivdAKMd536i0lKGfat5I0TxPROewktpzqNX67BwzVAjiIAJpyP8DAA3aGmUb96KaAshikAGh29TW2dVlmATeBuyppMDJpSzDK23JVYMJvr88ICoM4480Gwt5Q3e_814z4cmGs2CxYUXLjh5OH0tNgaPntuAikXqTeT_4ZU-HghhAW0gVC-F-sXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طلای ۱۸ عیار، ده دقیقه قبل:  ۲۲ میلیون تومان
🔴
هم‌اکنون ۲۲,۲۰۰,۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/143364" target="_blank">📅 16:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
طلای ۱۸ عیار، ده دقیقه قبل:  ۲۲ میلیون تومان
🔴
هم‌اکنون ۲۲,۲۰۰,۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/143363" target="_blank">📅 16:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0pApW5iDQCJmpYHdnHaHj3KVKdl7Ng2c_P-ahPI3fciM7k_-bx1qn2exRMX5IZgiKGR6SyskyxHuE9NTB-beKB-2XbemQwwqCH6zfpFDovONXMuCVnmBMung8es-LA1tuJafbtm1RL6S6JikMBxfy20PkvM2SA6R4T1IkcuJyQJ9zuhjJT32mOQoRLx4mkzN4zg0DGa8yZBRcn29MGCSYe3dehRZ93uBAI5UZKvL2AhPxoHZ8ioWRa7cpUZ5kd4yT-CmUDQ44GcUlSqiYK4Keoypv01jPJsLNYK6GP_8axXq9fzN7hCFfmzcYNxtK93gsRfMjSwYjUgOzYtGIQfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز: یک شرکت آمریکایی در حال تولید روزانه ۳۰ رهگیر ۵ هزار دلاری در امارات برای مقابله با پهپاد‌های ایرانی است
🔴
نیویورک‌تایمز مدعی شد: یک انبار کوچک در امارات متحده عربی، کارگران روزانه تا ۱۲ ساعت مشغول سرهم‌کردن قطعات چاپ سه‌بعدی هستند تا رهگیرهایی بسازند که قادرند پهپادهای ایرانی را با سرعتی تا ۲۰۰ مایل در ساعت (حدود ۳۲۲ کیلومتر در ساعت) از آسمان ساقط کنند.
🔴
کارگران این کارخانه که عمدتاً فیلیپینی و چینی هستند، روزانه حدود ۳۰ رهگیر تولید می‌کنند و هدف این است که این رقم به‌زودی به ۱۰۰ فروند در روز برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/143362" target="_blank">📅 16:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الحدث: پیشنهاد توقف فعالیت گروه‌های مسلح در عراق
🔴
الحدث به نقل از منابع عراقی مدعی شده کمیته چارچوب هماهنگی مذاکرات با گروه‌های مسلح مخالف تحویل سلاح در عراق را ادامه می‌دهد.
🔴
بر اساس این گزارش، پیشنهاد شده فعالیت این گروه‌ها به مدت دو سال متوقف شود.
🔴
این طرح در شرایطی مطرح شده که موضوع کنترل سلاح‌های خارج از چارچوب دولت، همچنان یکی از چالش‌های اصلی عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/143361" target="_blank">📅 16:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b3500bdf7c.mp4?token=iboi_qZeXP0MGnVuKiJ1EgoxgS1B8CPb0fhCRzdxvIGuC10-LcAdgBW2dKWXwAfB34cj4yKds2mS7qszK1z7J1sHHO9jwtX4_-4wsPkEXLtHCkF-xiDffEjqcCGDJP_apdsBjI-cxi3kkSQ6IU1epYt_m-nXXFBPcsXHgzFi_6Pbj_8w_lfGsb3XjjiKhRffK8IKkUgrGvv81zO7zTkS-n4oeVFwbZbyVxbATKy1kAUicWKddH6zf-4UtN5I93Qnd2disrJMA6S9C3mk5mmhCBWcSvAQiyZWyh5_AanpDmcQrlpfpNZcV_q--p_gP_G-RHSwDRr9UAzUKUVGnKMN3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b3500bdf7c.mp4?token=iboi_qZeXP0MGnVuKiJ1EgoxgS1B8CPb0fhCRzdxvIGuC10-LcAdgBW2dKWXwAfB34cj4yKds2mS7qszK1z7J1sHHO9jwtX4_-4wsPkEXLtHCkF-xiDffEjqcCGDJP_apdsBjI-cxi3kkSQ6IU1epYt_m-nXXFBPcsXHgzFi_6Pbj_8w_lfGsb3XjjiKhRffK8IKkUgrGvv81zO7zTkS-n4oeVFwbZbyVxbATKy1kAUicWKddH6zf-4UtN5I93Qnd2disrJMA6S9C3mk5mmhCBWcSvAQiyZWyh5_AanpDmcQrlpfpNZcV_q--p_gP_G-RHSwDRr9UAzUKUVGnKMN3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خرس معروف تبریز که با کوهنوردای کوه سبلان هم سفره میشد و باهاشون غذا میخورد و کوهنوردا خیلی دوسش داشتن،صبح امروز جنازش پیدا شد در حالی که توسط چند شکارچی کشته شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/143360" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
