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
<img src="https://cdn4.telesco.pe/file/VbFKqv_IfLOja11Z5_AjvY2IGg7hQHMPWiEkSyC-nGPWj9oJwIEiF5sYQGYQK5cgp7VrhHS7jCcVs_JpBWq96bn9RJaOKnBlaEh_2PH7Iyne-SR9TsCDW3cj6DeEMEnbYoA9UnkojlrkkerZ5OhjzIVgR2Gdwe3ZEK3eEGdOsK3zDkOlBAhIPbXeUjcndGoEPA9vucHv36W5miwkrJXiiJ3V5K6El1YXtxgH975gDoAwXVeX8BxcOe3q-G_ad_kkGsTZIynAi0_6ys22jYwuQpkjl2er6j7yoeLJB-CyK0H_IDzBO8J1lstJv5U49FTo13WqXXaYGqkimL-pAJbqIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 11:39:10</div>
<hr>

<div class="tg-post" id="msg-137864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/137864" target="_blank">📅 10:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
شهاب زاهدی: بجز سردار آزمون و مهدی طارمی اونم با اختلاف خیلی کم هیچ مهاجمی رو بالاتر از خودم تو ایران نمیبینم
😀
😀
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/137863" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
خرید بعدی پرسپولیس محمد قربانی خواهد بود / ورزش 3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/137861" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
قربانی آخرین خرید پرسپولیسه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/137860" target="_blank">📅 10:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/137859" target="_blank">📅 09:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
❌
گویاآمادگی پوریا شهرآبادی بیشتر از علیپور و سرگیف بوده است اما برای اینکه فشاری بهش وارد نشود قرار است کم کم وارد ترکیب اصلی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/137858" target="_blank">📅 09:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس موفق شود محمد قربانی را جذب کند پرونده نقل‌وانتقالاتی خود را خواهد بست و اگر موفق نشود دیگر بازیکنی جذب نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/137857" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس موفق شود محمد قربانی را جذب کند پرونده نقل‌وانتقالاتی خود را خواهد بست و اگر موفق نشود دیگر بازیکنی جذب نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/137856" target="_blank">📅 09:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
محمد قربانی پرسپوليس
‼️
✅
🔴
همچنان چونه زنی بر سر رضایت نامه قربانی ادامه دارد
✅
‼️
🇦🇪
الوحده اول رضایت محمد قربانی را ۶۰۰ هزار دلار اعلام کرد و بعد از اومدن تراکتور به عنوان دیگر مشتری قربانی الوحده رقم رضایت نامه را از ۶۰۰ هزار دلار به یک میلیون دلار افزایش…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/137855" target="_blank">📅 09:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/137854" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ4e3rnUXqivIXJlX8nYlH7Vt_L82tJnnURZ0QWbYkmxn3mNyCj8rZOpkNp15QNcJNupRvKPkgIs0ZgzZJFfrekEHT_hqluSnhWC8vI2xh1A1eXsd0KuujIScN10HY3P7SDPwY9qfWqBepWha7pmXWbmD66I7a2KTM2ERW3NSYzsYKsY2-4Yg510JfLktYKFN3VkvupdvSnXut5AwGPAquvXIW2xKk0FpWFjZQ36s-q1ndINtnfJauzt8brg2qZ52Hv_JnFdaeMvoJ6rrb7BGjIRy2kcdSkdMH4e4-B6iwkbu2iLlpjT8GlolNOTG71XdM81-0GQxB6nvi0Inn26Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/137853" target="_blank">📅 07:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK7-8r7pKICfPzUl4avWkudFw-3J3MPedLy4cqqqudv3wyOYgQqh63et7uAH4WiXWilnNTdfVMgSoPTtkFZceRZOlf3-nt3ChYZa86FCYevehXOHES2FdaVPRp_5X2jZJPBxRSPctNqDYzmsE-mR7oEkqrEMWL-LcvNizy17B7MNqED3EITjs0IbkwjdpQ7-B5m8wNFTdAutTG81h314Nc7HQ1MgmFvomYyHZTvKz1RDigfpaGWkbOeVHPT8KGiTbXrOxMigXU7gzzkd8E7xfB-qU-eDjC2dc76zGwUjn4vtNkr0Sbb0nndX1x0NCGPG6Lcc71bQLYt4NaAS5a55hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
هر چرخش یک شانس تازه برای برد!
🎰
اسلات با هر اسپین، ترکیبی تازه از نمادها و شانس یک برد هیجان‌انگیز را رقم می‌زند.
از بردهای کوچک تا جک‌پات‌های بزرگ، همه‌چیز در چند ثانیه مشخص می‌شود.
قابلیت‌های ویژه، فری‌اسپین و نمادهای Wild می‌توانند هیجان بازی را بیشتر کنند.
اسپین کن و ببین شانس امروزت چه چیزی برات رو می‌کنه!
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و با اولین واریز خود ۱۰٪ واریز بیشتر دریافت کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/137852" target="_blank">📅 02:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvXa_FUMb588y0DhupZbifL18fktstUrS3Z5zP555V1kkWlo2vyfWqaz_MG7k837CC6swxuqVX2XsbyWWTHeBkjrjEmVaQ35EXIUr_Epc8b5292GB3C3fWocxUs6rSQq_FJoqooq2jx2mPQMTE_jKuig-eYZYScKkInjGazpNbsglyH0LrthBJfG60LUP5WU2DfY8NYSlQ5a_WOHBnmS6sai_5NOvqrqYyF3OiIec8MnCli-kQBMPRhl-1L0eaWLPbf-UBfHf2Zxq-SpxHVO--dneCZ7hwnc42cv2DL-kaaGGBszCmajcSHvk7BeMbBbdWV_UOpw4G2KieOGEqOvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شبتون بخیر سرخدلان
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137851" target="_blank">📅 01:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
یک مقام مسوول باشگاه نیم ساعت قبل به قرمزآنلاین گفت قرار بوده ایری امشب برای امضای قرارداد و برخی امور جانبی به باشگاه بیاید.
❌
اکنون برخی رسانه ها خبر داده اند ایری در باشگاه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/137850" target="_blank">📅 01:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
سازمان لیگ به استقلال گفته کارت بازی آسانی رو صادر می‌کنیم ولی اگه بعدا بازی‌هاتون سه هیچ شد پای خودتونه
🔹
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137849" target="_blank">📅 01:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
استعلام فیفا درمورد آسانی هنوز به باشگاه استقلال اعلام نشده. و در صورت هرگونه بروز مشکل حقوقی در این پرونده، سازمان لیگ مسئولیتی در قبال صدور کارت بازی آسانی و مستندات آبی‌ها ندارد و همه تبعات و هزینه‌های آن را استقلال برعهده گرفته‌ است / فرهیختگان
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137848" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
عجیب اما واقعی!
✔️
تخلف عجیب و بزرگ سازمان لیگ؛ قرارداد جدید آسانی ثبت شد
‼️
بزرگترین تخلف تاریخ سازمان لیگ فوتبال از بدو تاسیس تا به امروز رخ داد و کارت بازی بازیکنی که قرارداد شو فسخ کرده و از تیمی که پنجره نقل و انتقالاتش بسته ست و امکان ثبت قرارداد…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137847" target="_blank">📅 01:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137846" target="_blank">📅 01:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137845">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚫
یه عده میگن یکی از اعضای هیئت مدیره داره سنگ اندازی میکنه، من اطلاعی ندارم اگر صحت داشته باشه و اثبات بشه کونشو پاره میکنیم کاری نداره که…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137845" target="_blank">📅 00:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a39HOMvHlGd5sJx8Ew4tjfSKbsc7VpdoeCE_sUDnqCrYOHikuByDNdzMRrTKNOEe4xFdZhDu5WSAxmywSXZ86uPn0IBJFIp4Ig8_u28oH1GXPUs4v6kdWqjiW5yD2MpaMoKAxgaiplo8TYKxxSNFoCluJtE7sis4cm4qYk0iZt_wCm1gMydfKakZYekb2TEpt8YVtRhUbn7I8v9iGCwagJ9P9z1pM-BuaN7uLBTKZLoG2uJhfsKOik8z1QFvn3nxPIPqsAJJNGDzjwtaTfsJqmFFAvyBtUPU6Vp4ClTO5eHq-R1ZR7SRZZWKuzP0tp-Jjlk5e0xTaoFYC1yyV1dHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووووووری
❌
طرفداری:
❌
❌
محمد قربانی سورپرایز مدیران باشگاه پرسپولیس بعنوان آخرین خرید در بازار نقل و انتقالات خواهد
بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/137844" target="_blank">📅 00:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/137843" target="_blank">📅 00:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137842" target="_blank">📅 00:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان جواب نامه باشگاه پرسپولیس رو نداده و مبلغ رضایت نامه رو اعلام نکردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137841" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137840" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4tgpuzXX85WsaLHkHw5qoIW79Y26RipjNdFCSdp83VLASUdxHT-_os_Ph906zpIrAQZnEoF8rMWsc3XB4A3947S6_X5ugWeT5eoZfNUOoGefXLOjS30FeyVv6IvgpFpMrpmnSIh7B8WBAvI_LzbpJuRTQjcG2-LL66JtsAWbY_15FOauKBGECcQ5pVV5vr7hBmzU1GcvD5ZwSSP9SwCovo-k2wke7TfiAqMpMH3XE4jPGzki6b2BpUBxy8LaI2W66Njku2IEWKOfz-D6Bn6iRaMoIEfcZNHh1mxcU2k6zRnnC4E7U-jYZIPVjNbCRaYJk-IqCMyNOJNbVGWi1Xk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137839" target="_blank">📅 23:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
سازمان لیگ 11 و 12 شهریور را برای برگزاری دربی در نظر گرفته و پنجشنبه 12 شهریور گزینه احتمالی است.
❌
با این حال، تاریخ نهایی مربوطه هماهنگی با برنامه تیم امید و مسابقات آسیایی تیم‌های ایرانی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137837" target="_blank">📅 23:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⛔️
میره تراکتور بیخود به دلتون صابون نزنید، ایجنتشم منصور عظیمیه بازیکنشو نمیاره پرسپولیس و در اخر اینکه ما اصلا هافبک دفاعی لازم نداریممممم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137836" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💢
💢
💢
فووووووووری
💢
آخرین پیشنهاد باشگاه به نساجی
❌
130 میلیارد نقد + اژدهاکش و پویا اسمی ( قرضی)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137835" target="_blank">📅 23:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137834">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137834" target="_blank">📅 23:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137833" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
✔️
طبق استعلام دو باشگاه استقلال و پرسپولیس خرید کسری طاهری طبق قانون فیفا پل حساب میشه و هرکدوم از تیما بخرنش باید تا نیم فصل صبر کنن تا کارت بازیش و itc این بازیکن فعال شه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137832" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137831">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
رضا درویش: سرژ اوریه بازیکنی است که بعد انقلاب بازیکنی به این کیفیت به فوتبال ما نیامده است و او سابقه بازی در منچسترسیتی و پاری سن ژرمن را دارد. به زودی مشکل او حل خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137831" target="_blank">📅 22:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137830">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
باشگاه سپاهان از باشگاه استقلال به دلیل استفاده از بازیکن غیر مجاز ( ماشاریپوف ) در بازی برابر این تیم شکایت کرد و خواستار سه بر صفر شدن آن‌ بازی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137830" target="_blank">📅 22:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137829" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137828">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbRh8kwnHTBMdxdqf1D4YXunCv7bEePrNCXPfGv7Q4S8aVAtLfrXzPfBS3H9Ga2UJy_332Lystg8fz8eRiaWlpoxXOG_UEZy18li0EQ8g99TzxosIk10nJ92Ofsqn-W6w6QSdZDn8nPhpK79aHGX6bguXRiRRhhEPhlkRtR6F7F6UvECdxRHGHM276ABnb7OgaLRVCBnx-FDJ9asVrFqDC052HC6QCBMo7smcbmx4WjFlL2Sg5l2ZI44ajSPXzp78GmzFckO3aStBgn_DBbDBI9hKcWDb0-a6TyQdv1MLDtu2m8GCQcRkqxB6YKZB25ehoqRmRrqb8iemoI5cAcIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هرچی حساب میکنم استقلال از طول و عرض سرویسه
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137828" target="_blank">📅 22:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137827" target="_blank">📅 22:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
پرسپولیس قصد نداره حتی با وجود جذب ایری، ابرقویی رو بفروشه و او آلترناتیو دفاع چپ هم هست/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137826" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tEi9OUGhN4x4G2C0MprnQXLwX8Hk8x6WD57zDQCmf6Yu52XEdynCwyvVWz8XwRymO6TbP_uz0yTiYHJZqaSY8SntcGsZYIMVpHQFxM33WSu6ukBxXWHkCsagqwSsTmkL_Pnt3QGQuUzichaFb44791aszHgw0odzF9rPw8DWz-l3LLfpP3_I4JMP8Lf8xhlSeFQKC6PPjCnGSrKxij_vsqJ1uPRS6SXNHvXJ-DXtF7R7B2WrYTpqhdRCureFSdbHVYAu2mBKESJN2QPhEdAfWgLe7IEiD0TC-Se0W1afj5eMGrtz--43VdF-kXI6EJmqaY30szQEDpFZhSAQHy8pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137825" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137824" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWLOwAQJTwd0OPr0_0mdaZtyh6LVAT0OWgjPJOgyk_5CNeciYsqzg7ad-X7WofS9Mn84QFBSRoR6kpurNg_8YTbG52K8fl8faE_BF0u-cVpwqhLAhN3vVVPF28rTpT564KX5fb9QtjzPYXtVNhpRVvPNv5oV1sUpb9QqT0TJstEiN2FU9ogmO7WZnssV87kyX7xHp02HmlId0KM-b3_9N5_0rmDjNFIsgkm7hEIrGwqwhNFK3awh6LDs5Pde8-9BqeyvcGimja3hict0dQwekcSMGyhYncpl69S2GCsUPvvYiSnwS-xane3xx06NI7NYA6VHGod3DxujqZ8ty-GNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
🤡
نرینی یه وقت سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137823" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چراغی جان با تمام احترامی برات به خواطر رزومه این چند سالته قائلم ولی هوادار تصمیم میگیره تیم چه نیازی داره و تصمیش رو عملی می‌کنه  زمان ثابت می‌کنه  جلوی فشار هوادارو نمیتونی بگیری عزیز</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/137822" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmahdi</strong></div>
<div class="tg-text">چراغی جان با تمام احترامی برات به خواطر رزومه این چند سالته قائلم
ولی هوادار تصمیم میگیره تیم چه نیازی داره و تصمیش رو عملی می‌کنه
زمان ثابت می‌کنه
جلوی فشار هوادارو نمیتونی بگیری عزیز</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137821" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🙂
🤩
ایری امروز داشت میرفت اون تیمه ولی یهو پرزیدنت حدادی و احمدی سر کیسه رو شل کردن…بسوزززززید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137820" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
حدادی یه قربانی فقط همین ...تمومش کن دکتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137819" target="_blank">📅 22:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137818" target="_blank">📅 21:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137816">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
تراکتور و سپاهان با زدن نامه ای به فدراسیون فوتبال تهدید کردن که حق ندارید جام قهرمانی رو به استقلال بدید چون شرایط جدول لیگ پارسال خیلی نزدیک به هم بوده؛ در این صورت ازتون شکایت میکنیم./ آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137816" target="_blank">📅 21:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137815">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚡️
⚡️
دقایقی پیش جلسه مهم پیمان حدادی و شهاب زندی برگزار شد و طرفین به توافق نهایی رسیدند/ایسنا و فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137815" target="_blank">📅 21:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137814">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔄
🔄
فوووووووری
✔️
مهدی تاج: ورزشگاه آزادی نیم فصل دوم در اختیار پرسپولیس و استقلال است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137814" target="_blank">📅 21:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137813">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137813" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137812">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UizzsszcpUnMqUKjmJYi2PUGIn9HpUVYvgHIJTCZ4bm_tzqxG6TXgNxP2hyTyQeTOjoaglfboRITVy5bnfpkkHABOoqcrMSuZwG3WpbL9OHksQfVZv4dZhY0uUHS0ILDuEjyKGRMcuR_2RYsyn4jrp4TXo0CNXaAjtX-c57DLRHB6k8g-lRxzo8gP4UZjR_OqB3q71CeeBfm6YvhP561DgaZsoQ8cdPreW5lYlj7UYfQiu-b0EYLkDPZ--MzBLjzOlJC9bfsb0Ix8H9KKEGIu4h4TDK4XAjIQRsr0K61OWj769OH44byWxXgH3ohbZMtRRUrRJjkyw4IZxBctuapYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137812" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137811">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
🚨
قدوسی : قرارداد دانیال ایری فردا امضا میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس   @SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137811" target="_blank">📅 21:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137810">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3j8lkEuZHudGIteN_puWosE3C1oLGLfhqtI45ARIDs5OwwyKhVd3y-g-NiSxcyyv0uLr9o3xQH-ZZsk6xI4TBV28tK6398nzbzIyCF3BKvzTPSbW-i2rXbEa16QZlzpMtUwwUqRja27UFBwo74ANcdkehbL06MRz9qg1RnKR0V-oEGTeyICw9B-paCMBXoz7SJCFjESs7U-8pDi94fvV_imkm4gbG9QvWAMJ9I5JmKlSIyx8K7DfMOIrgrHRaQlXsVpjsENb_qvVtAXC1-H2cDhah1xp0NsjCcaUlIMSwmOhnL2hAvyOy8iZu27l78DnSRYYC9jDhp5zeEVsZp7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت سرخپوشان به تمرینات بعد از یک روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137810" target="_blank">📅 20:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137809">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc676823cb.mp4?token=o2fIbXQ0pSsnIClP259f1w1tobwf3ozJve7QBwTiV0geIA_aBZ-AoKWvNw0-dsFuYWYjRvBrUA8EcWFr50Ok7_bPa7Qt2i09wgRXNIhhrEG9qrmmUtkRVlse8XXybSTZWFP2chJ8s5aIG8H1uqKH8C2OiDa5y8oGdOh4eV04BqN12VIwVJcvrj4FwKSjPbwru4C38s-YCSLl8fTAbbWZ2pwbfC89A7s2snvSB_jQ8mfNxwsw0N-5OCUVMjV-5DK9O1d1IUbHI4-JgBunOwJogck3EZ4ylX8vSMr5hEUPshQBoGMPAMeKxSg6lbCvQ-y5SDpe83j19MIiiXt1QeDMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc676823cb.mp4?token=o2fIbXQ0pSsnIClP259f1w1tobwf3ozJve7QBwTiV0geIA_aBZ-AoKWvNw0-dsFuYWYjRvBrUA8EcWFr50Ok7_bPa7Qt2i09wgRXNIhhrEG9qrmmUtkRVlse8XXybSTZWFP2chJ8s5aIG8H1uqKH8C2OiDa5y8oGdOh4eV04BqN12VIwVJcvrj4FwKSjPbwru4C38s-YCSLl8fTAbbWZ2pwbfC89A7s2snvSB_jQ8mfNxwsw0N-5OCUVMjV-5DK9O1d1IUbHI4-JgBunOwJogck3EZ4ylX8vSMr5hEUPshQBoGMPAMeKxSg6lbCvQ-y5SDpe83j19MIiiXt1QeDMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137809" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn-HMyhH82GXlaS9YVfRckZCFcckhGHPi36kBOivXaXJQPRvh6xRx8qNfvTihWNFoy-TVq8jjkX_qurflF8QLkaBcwZm5CnGUUMMh4jvxjDZKJTIEh4Ak-19loYnyaFFLbuTMIRBg1wVE03dlhD-qwZWPNTm0LDFu6fySC9GA4b658b1M5a7pAo7iqryuvx6YFAQ17R49ZCMvLf_RJdszzg57t2vHKLpsZiAXlsPFpXP6gJCMa5mfPLuiWeyCcCeU41Cdg_CZtLtS9nQuLfyr96CWsTwa9xFjsrqCXMHSjhoWAF6r5NElYwvuqqZQ24K_iuSqUNcZKvRINdtiHNLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون برای جبران؛ اسپارتا برای حفظ برتری!
🔴
LYON -
⚫️
Sparta Perague
⚽️
لیون در خانه به دنبال جبران شکست ۲-۱ بازی رفت است و از همان ابتدا باید فشار بالایی روی دروازه اسپارتا وارد کند.
اسپارتا با برتری بازی رفت دست بالا را دارد، اما حفظ نتیجه مقابل فشار هواداران لیون کار ساده‌ای نخواهد بود.
انتظار می‌رود بازی از دقایق ابتدایی تهاجمی شود و هرچه زمان می‌گذرد، ریسک‌پذیری لیون بیشتر شود.
یک شب سرنوشت‌ساز در لیون؛ جایی که یک گل می‌تواند تمام معادلات صعود را عوض کند.
📌
در وینکوبت ثبت‌نام کن و با ۱۰٪ بونوس اولین واریز دیدار امشب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137808" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔜
🤩
سکوت حدادی معنای خاصی دارد! منتظر خبر خاص یکشنبه باشید
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137807" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
بیفوما هم موندنی شد و خارجی جدیدی جذب نمیشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137806" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
✔️
پیوستن رامین رضاییان به پرسپولیس شرعا و رسما کنسل شد
✔️
آنا
🥈
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137805" target="_blank">📅 20:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⏺
تفاهم نامه سه جانبه پرسپولیس و نساجی برای جذب دانیال ایری فردا امضا خواهد شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137804" target="_blank">📅 19:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137803">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137803" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
✔️
ورزش سه :توافقات انجام شد و دانیال ایری به زودی پیراهن پرسپولیس را برتن خواهد کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137802" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137801">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
قدوسی : باشگاه نساجی به پرسپولیس‌ تخفیف داده و مذاکرات پایانی در حال برگزاری هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137801" target="_blank">📅 18:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
گرا باز هم زیر بار فسخ کردن نرفت و چون ۸۰ درصد مبلغ قراردادشو خواسته باشگاه نگهش میداره/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137800" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
❌
مرتضی پورعلی گنجی با عقد قراردادی به پاختاکور ازبکستان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137799" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
گرا باز هم زیر بار فسخ کردن نرفت و چون ۸۰ درصد مبلغ قراردادشو خواسته باشگاه نگهش میداره/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/137798" target="_blank">📅 18:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">💢
💢
💢
غیررسمی: دنیل گرا در پرسپولیس ماندنی شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137797" target="_blank">📅 18:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
جدایی دنیل گرا از پرسپولیس جدی شده.
🗣
🗣
باشگاه دنبال فسخ قراردادشه، ولی چون قراردادش بالاست، نمی‌خواد ضرر مالی زیادی بده. احتمالاً یکی‌دو روز آینده تکلیفش مشخص می‌شه و اگه مشکل قرارداد حل بشه، قبل از شروع فصل جدا می‌شه.
✔️
فارس  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137796" target="_blank">📅 18:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
مدیران نساجی بعد از درخواست خود دانیال ایری به پرسپولیس تخفیف 20 میلیاردی دادن و مذاکرات فعلا در جریان هستش!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137795" target="_blank">📅 17:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137794">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efb264822.mp4?token=KsX2zlNbVb0R7CcEzH_qE-MADxP60Kf_IKbEEJ-MRxxGAQ1u2gpI9CuAi9kWzVMxj395sz5uo3Mv9H_QXfuzKKJdWi-eHrF1tg72YqQcQB5MzGmh26nw-Xz_zuUJxReyrf1Z9V2KNJ73qZ2QelXbb8-ZxiFXMPDZdOyOplkUF7_ORjbKh_8kZ4Z4Pvurem9Yt619iGZ8v4PLL7peQ1JiHR60nKaezUfzWJ4ubVdJzYE1wHPZ_nmV6Tqc1Uc5opZ5yZAGQYh7ZoAIyaPb6KJMKlVNATySQD4wisMi8FxLcDcD0vCTJsgXGWC_SDBEwST1_jrST2B-YyF4zaxo3GJSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efb264822.mp4?token=KsX2zlNbVb0R7CcEzH_qE-MADxP60Kf_IKbEEJ-MRxxGAQ1u2gpI9CuAi9kWzVMxj395sz5uo3Mv9H_QXfuzKKJdWi-eHrF1tg72YqQcQB5MzGmh26nw-Xz_zuUJxReyrf1Z9V2KNJ73qZ2QelXbb8-ZxiFXMPDZdOyOplkUF7_ORjbKh_8kZ4Z4Pvurem9Yt619iGZ8v4PLL7peQ1JiHR60nKaezUfzWJ4ubVdJzYE1wHPZ_nmV6Tqc1Uc5opZ5yZAGQYh7ZoAIyaPb6KJMKlVNATySQD4wisMi8FxLcDcD0vCTJsgXGWC_SDBEwST1_jrST2B-YyF4zaxo3GJSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
tik tak...
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137794" target="_blank">📅 16:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137793">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
این چهره احد میرزایی کارشناس شورای شهر تبریز بوده و یکی از نفوذی‌های زنوزیه
🔴
امثال این افراد هیچوقت به درد پرسپولیس نمیخورن و هواداران برای رفتن اینا ثانیه‌شماری می‌کنن
🔴
همین آدم روی انتقال قربانی هم به شدت داره سنگ اندازی می‌کنه.  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137793" target="_blank">📅 16:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137792">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚡️
⚡️
دقایقی پیش جلسه مهم پیمان حدادی و شهاب زندی برگزار شد و طرفین به توافق نهایی رسیدند/ایسنا و فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137792" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137791">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
این چهره احد میرزایی کارشناس شورای شهر تبریز بوده و یکی از نفوذی‌های زنوزیه
🔴
امثال این افراد هیچوقت به درد پرسپولیس نمیخورن و هواداران برای رفتن اینا ثانیه‌شماری می‌کنن
🔴
همین آدم روی انتقال قربانی هم به شدت داره سنگ اندازی می‌کنه.  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137791" target="_blank">📅 16:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phlgMuGnlclSgPyMtE2N0rHaD-EzBJdAaaSZElJYjuvD8PxkXJLHQPmgRuIaYXlO9RgwgowCDBWAFvRvmIs5pMKxq4EUQeABtO6_uB2qfe0h8hIEaSXPXHYuOOeag-Rf_ygv19yHTNOoeOtaxki-rPdflBTsVHYdGnRkDUlanAFHfy5ZwzhWPxWGd4WPaDHiLdy5bh19YPkmtDzT_U9P4KBbddNxsJzr4Brji4bd4gAGgdOq0zfRIlGnEWpz2RvrS1jOWC_vkv2TxSHcmXLdOZBHQZFc0Csklc7U8GzZhpQX0-KdoJ-v1SAcWMxRFK13Y9hYnbrPv-zYwq2su-g16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این چهره احد میرزایی کارشناس شورای شهر تبریز بوده و یکی از نفوذی‌های زنوزیه
🔴
امثال این افراد هیچوقت به درد
پرسپولیس
نمیخورن و هواداران برای رفتن اینا ثانیه‌شماری می‌کنن
🔴
همین آدم روی انتقال
قربانی
هم به شدت داره سنگ اندازی می‌کنه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137790" target="_blank">📅 16:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
#فوری
🔄
باشگاه پرسپولیس برای صدور رضایتنامه دانیال ایری با نساجی به توافق رسید.
✍️
ایسنا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137789" target="_blank">📅 16:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
ایری به پرسپولیس پیوست / فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137788" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
کسری طاهری، مهاجم نساجی که با حواشی زیادی به این تیم آمد، در بازی‌های دوستانه عملکرد خوبی نداشته و مجتبی حسینی از عملکرد او راضی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137787" target="_blank">📅 16:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
❌
تارتار همچنان روی موضع خودشه و میگه نیازی به رامین نداریم/فوتبالی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137786" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
توافق نهایی پرسپولیس و نساجی برای انتقال دانیال ایری
❌
❌
دو باشگاه پرسپولیس و نساجی بر سر انتقال دانیال ایری به توافق رسیده‌اند و نساجی پس از دریافت مبلغ مورد توافق، رضایت‌نامه این مدافع جوان را صادر خواهد کرد.
❌
ایری به دیدار نخست پرسپولیس مقابل شمس‌آذر…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137785" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
🚨
🚨
فوووووووووووووری آنا
✔️
پرسپولیس و نساجی امروز به توافقات برای انتقال دانیال ایری رسیدند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137784" target="_blank">📅 16:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤝
🤝
🤝
🤝
🤝
🤝
🤝
🤝</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137783" target="_blank">📅 15:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤝
🤝
🤝
🤝
🤝
🤝
🤝
🤝</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137782" target="_blank">📅 15:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
محرومیت مدیر بیشرف ترتر بخشیده شد
⚪️
محرومیت یک جلسه‌ای افغانی ترترزاده با رأی کمیته استیناف بخشیده شده است و مدیر تیم تراکتور منعی برای همراهی تیمش در هفته نخست لیگ برتر ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137781" target="_blank">📅 14:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137780">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
چه ترکیبی بشه.با حضور نکونام و خداداد بیرانوند و شجاع
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137780" target="_blank">📅 14:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137779">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137779" target="_blank">📅 13:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137778">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137778" target="_blank">📅 13:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137777">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
فووووووری | خبرآنلاین
✔️
✔️
تراکتور مذاکرات با رامین رضاییان رو آغاز کرد!
✔️
✔️
در صورت پیوستن رامین به تراکتور، صادق محرمی از این تیم جدا میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137777" target="_blank">📅 13:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137776">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137776" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137775" target="_blank">📅 11:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
فووووووری | خبرآنلاین
✔️
✔️
تراکتور مذاکرات با رامین رضاییان رو آغاز کرد!
✔️
✔️
در صورت پیوستن رامین به تراکتور، صادق محرمی از این تیم جدا میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137774" target="_blank">📅 11:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
مدیران نساجی بعد از درخواست خود دانیال ایری به پرسپولیس تخفیف 20 میلیاردی دادن و مذاکرات فعلا در جریان هستش!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137773" target="_blank">📅 11:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
مرتضی پورعلی گنجی با عقد قراردادی به پاختاکور ازبکستان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137772" target="_blank">📅 11:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137771" target="_blank">📅 11:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137770" target="_blank">📅 11:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🟥
‼️
😄
دیشب رامین رضاییان وسط برنامه بلند شد دکمه لباسش رو باز کرد که بگه ببینید همه لباس و شلوار من برند ایرانی هست. ساعت هم ندارم. میثاقی هم گفت خوبه دیگه دکمه جای دیگه رو باز نکن.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137769" target="_blank">📅 11:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
✔️
‏  رسوایی اخلاقی رئیس فیفا فاش شد  ‏
✅
طبق گزارش یک نشریه انگلیسی، رئیس فیفا در زمان حضور در یوفا برای مدت ۵ سال با این زن رابطه غیراخلاقی داشته و از سمتش سوء استفاده کرده است.  ‏
✅
پیش از این اینفانتینو ابتدا به خاطر زد و بند با ترامپ پروندهٔ سنگین…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137768" target="_blank">📅 11:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5721545f.mp4?token=eXh5A2ypuz9VE0R-4mX5zSq5He2dOqDmgsHZfP6fz1KMLTL4n6Ee_GfDV-dJqLa5_6p6b0dvZ-UCwk9auhRZQqecp70tGKPOeO3KO8C4YXJl5TLIKZjiFI3cf04cfPvHloAerP9ziGOr7BDVrsOqo6Mf2LUXSX4Diszy7CY1WcCAxeMAGvTG8Xt0PKO4-6KsWZQoP5SRgKGKsy6ds1kvToKLGEcxc7RpVnzmIpnOii7Sg6ByBUJh8v1BFRAqW3MJelomm1HJrBJ3T4EFNKdgE6KbhqUJE5VGp76Q3KiiLRO4g70nbsaAopvY9l92In1UW5ZNTZz0Opm31isA2AVKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5721545f.mp4?token=eXh5A2ypuz9VE0R-4mX5zSq5He2dOqDmgsHZfP6fz1KMLTL4n6Ee_GfDV-dJqLa5_6p6b0dvZ-UCwk9auhRZQqecp70tGKPOeO3KO8C4YXJl5TLIKZjiFI3cf04cfPvHloAerP9ziGOr7BDVrsOqo6Mf2LUXSX4Diszy7CY1WcCAxeMAGvTG8Xt0PKO4-6KsWZQoP5SRgKGKsy6ds1kvToKLGEcxc7RpVnzmIpnOii7Sg6ByBUJh8v1BFRAqW3MJelomm1HJrBJ3T4EFNKdgE6KbhqUJE5VGp76Q3KiiLRO4g70nbsaAopvY9l92In1UW5ZNTZz0Opm31isA2AVKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
😄
دیشب رامین رضاییان وسط برنامه بلند شد دکمه لباسش رو باز کرد که بگه ببینید همه لباس و شلوار من برند ایرانی هست. ساعت هم ندارم. میثاقی هم گفت خوبه دیگه دکمه جای دیگه رو باز نکن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137767" target="_blank">📅 09:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137766">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
✅
بازی های پرسپولیس در 3 هفته ابتدایی
🗓
شنبه ۲۴ مرداد
⚽️
شمس آذر قزوین - پرسپولیس
⏳
ساعت : ۱۹:۳۰
🏟
ورزشگاه : سردار آزادگان قزوین
🗓
چهارشنبه ۲۸ مرداد
⚽️
پرسپولیس - استقلال خوزستان
⏳
ساعت : ۱۹:۳۰
🏟
ورزشگاه : متعاقباً اعلام می شود
🗓
دوشنبه ۲ شهریور
⚽️
تراکتور تبریز…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137766" target="_blank">📅 09:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137765" target="_blank">📅 09:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137764">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری
🚨
ورزش سه: با انتقال دانیال ایری به پرسپولیس، انتقال حسین ابرقویی به سپاهان درحال نهایی شدن است
😐
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137764" target="_blank">📅 09:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137763">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137763" target="_blank">📅 08:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBAI34kaGnQOV62WvXwLk_lk9KOqDWWF5V9TLGx08WSJfreWp-EDwh6pe8WDkLQzQIfgoC4lr9JqdLtunor2uBmwykLe6X8WhqTtGOFxjV-k02ApvnC31j1MQGP7mt4QL4b1X3Y-VnH62sE2hw5mCYxEVXdRnAuLA8Pk7oEH29uVLiIpn9A0sJWH7hTt6ozB0lymeBGSOROmKORmmf4drIOHmCyvtPg-htle1ooR0I_G0jk2bIdofYD3XOaM_IHbBmxi8jPS-p4aVWWVSTbP37yGII-rke-jTLj-LyGTHJXH4pG6hZ-dWU4rZb2jxgFJrIu0-_uKNu9TAoUUHa2X-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137762" target="_blank">📅 08:23 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
