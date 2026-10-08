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
<img src="https://cdn4.telesco.pe/file/gnaEFnK0wFd5Ae4KqCDoK9C0F9i8yJ5SocR_0uYgaalj5NrebynFDXPDNQzQFfaKooXA9mtbFGNpteuLUPusz582HWi0Zjt_jg-KzD7IjkyXu3PmdIJEpaVlKu0p-dwxOz5FGaFIhzLkmmK4R2N1RmzCdGqv2nCzBeidZ-SN6p3Qt0UUZb7mwdhEb842AOOXuczxnBwiaIAhJ8QbTvyXhKTRA69iPaikikDZEcrTxo7XHdD6-Rf2IkWoN3JBoOV84zOW-jGjjC6EISk6XFLMU0dOikXjEfvv-SS8OA2cIX7IGIx7e5dr4xKhg8C1FwqrX1ValZSZ206iHbgSWCQdnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 05:37:29</div>
<hr>

<div class="tg-post" id="msg-141083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOcRCyfS5LNssJmLEUcNknEtroh53Jf50EX-hosVt-SxQqjLTioh3jDeoYDpPUyu1hZswXZg9UsbBGtdKiTatio8y1q0SE0JF8pfzQSjptEpQcliT-DgT8G94U-yLOqjvLDVzWvOFQb2R0JosltLKItY4X-OmSyTQgVHax-BayvFS6A_x3wtyTuwcMZaPaSUwh-LAO2flt-jAOpkNNbypUphLCVP8cu9ls7iruKfKcqG-oBvODeEZTn9MWHZOvcM319_qv_l7L7ezxGvuFy2iWsk3Nwoy5XxdlJBZEyXHAtcjwzw_lp-nAXWTi0qUnnk6zpnSDNccwhW8h1QR7ZNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته‌ی هشتم لیگ خلیج‌فارس ایران
🔥
⚽️
هفته‌‌ی هشتم با چند تقابل نزدیک و کم‌ریسک از نظر گل آغاز می‌شود؛ تیم‌ها بعد از وقفه فیفادی معمولاً با احتیاط بیشتری وارد بازی می‌شوند و جزئیات تاکتیکی می‌تواند تعیین‌کننده باشد. تراکتورِ صدرنشین با خط دفاعی بسیار قدرتمندش مقابل استقلالِ بدون شکست قرار می‌گیرد و این دیدار می‌تواند یکی از فشرده‌ترین بازی‌های فصل باشد. در سمت دیگر، سپاهان برای تثبیت جایگاهش به دنبال پیروزی برابر فجر است و فولاد هم در خانه شانس خوبی برای کنترل بازی مقابل مس شهر بابک دارد.
سناریوی محتمل: بازی‌های فردا بیشتر به سمت نتایج نزدیک، نیمه‌های اول محتاطانه و تعداد گل پایین تمایل دارند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/SorkhTimes/141083" target="_blank">📅 02:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141082">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فارس: مجوز خروج پادیاب خلخال از استانش صادر نشده و همین موضوع باعث منتفی شدن این انتقال شده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/141082" target="_blank">📅 23:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
هیئت ورزش و جوانان اردبیل با فروش پادیاب خلخال به پرسپولیس مخالفت کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/141081" target="_blank">📅 23:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141080">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_2B0ImgVr9jOUR3O2pagRkOlmVuR2ECkZUQHGmgAWPs-vzCQkpKai7el_-g4LbjUoAzdCu8VdL6DdGKm6QYdkED7ZpbdFc6CceiVge2Bkg3bV4CIogHG2hkx-95UEV9zF1FWqql42yIWqNx5n5y6IQwdDwhl599HmTNLL7fjYdMgPZGSpuKVOkW86g1U522D-HD18vnBwB1N8LRWBDTHOO1CZ_iPcxbRroP5sL1Wu27sOSktehMIJdKr5CORQuDmhLuOl4HBbEd9UIaDI9z2PEhxO8SPHPDXLO_lOlRjecvF8CGzigc55p8mEcvLz1J_1oKLB_nbdiSnc0WD9_4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فکت: پرسپولیس در تاریخ خود در خانه به صنعت نفت نباخته است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/141080" target="_blank">📅 23:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141079">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7Q8JYr06wWHzEWkqjTAXdIZQo_ktsaxIcpCxSUChAE750eeRvcOuOATfzvCfS88n8yx_Da2hRhbXX0SQSptHZSik0s6OtV9vZnhVGMZmS3fhRdlzaccubJ1JJgwn36qWG2AEnnfzznYMQEIMW341MriygYC4o1l7heoZx_8gpop2Q9r0-8gcZy-7FVAl2g6D4ATd2wplHWH_5Q6UkmQ8pTbcnLl9OitGSEZMWpRHuu0jqM4ToOrL8DlVSmY1HXp94cZN52Q_S6qpWUJG7oR-XSsaTM1iXu9tvLoJkw22lDNmMKSAn4sAJgINkwxccLQnHyn4iIuQJX48FrbSMfAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
طرفداری
:
✔️
پرسپولیس در صورت ناکامی در جذب محمد قربانی و استقلال در صورت نرسیدن به محمدجواد حسین‌نژاد، ممکن است برای جذب دهقان هافبک الوحده اقدام کنند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/141079" target="_blank">📅 23:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141078">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
امتیاز پادیاب خلخال به پرسپولیس واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/141078" target="_blank">📅 23:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141077">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX5hzPvrdBzViFvX4uxE53jwrJoIEgi682Ull8n4qMlsKFxcj_UM6ysAvz5eZS6duKO-amRdy_09nmNcXxpl9_9GoDLbwFUCwtWz-asIqHjM_K2oqAuMbemxjns-kOrAZ8_ZwcT9s4uZxQm1OEgbBGxklBvWJ9Hl3basGSDUU_4KEPgfpaJDap67eKBgYwqtRnCrJr52JPPOlMppV12chroaDRg6gprPg9PDRUycQ0hclBHTePtlMuKzLXOx5a9H9fRg3rBMbycRYt4mrvpbFQ0YYBQsGL2qA_PSngy86yHtsV8876FWQTAXXSUAWlFJS8-2S9emUXEOH8esSeCAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
❤️
بیرانوند صبح دیروز به کمیسیون پزشکی اعصاب و روان به دلیل داشتن خالکوبی رفت، همچنین دستی که از ناحیه تاندونش مشکل داره MRI گرفت تا ببینه نتیجه‌اش چی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/141077" target="_blank">📅 23:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141076">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrnnWXbjJFSoT2yxrKFpfrp9FG88C62e1WzL2VQjYTxfkNHhiQkHOnCxmFe514PgWwFsjSfypDYqrAixIkjk7IB9X7mLBkrn5lcgw7sFc4La0JBCENAPZpucFi53ZQ5CjIPvoofZe4KEhG5P5ax3Yc-bAqvk9ZT_zdNMJ6MnCD5eeuEUPr92QFLSha1ddpQJuQUzaNDaexVmiGUd0G4HVoLlBN0gSdJzKwLZdtN-ZhKAM5c8NyLvYAAR1vZhhZ8kBvavYZAHYXTYUQnF4Q2jn6ap_odC5LwwXHpRkn9KfAQn-cEc2h5Z_latxYSRXmNwowDonr3CT6p90966FJMYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#یادآوری
✅
✅
استقلالی‌ها بزرگترین خیانتکاران به‌منافع‌ملی هستن حالا اینا به ما پنداخلاقی از منافع‌ملی میدن
✅
✅
سال ۹۹‌ معاون‌استقلال مستقیماً به النصری‌ها خوراک میداد برای حذف پرسپولیس‌، صدای واعظ‌آشتیانی دراومد از این خیانت‌
⬆
⬆
ما مثل شما نه‌خوراک میدیم نه خیانت میکنیم از راه قانون ۳ امتیاز دربی رو ازتون میگیریم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/141076" target="_blank">📅 22:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141075">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
پرسپولیس و دانیل گرا بر سر فسخ قرارداد به توافق نرسیدن/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/141075" target="_blank">📅 22:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💥
#فوووووری  | #غیررسمی
🖍
یحیی گلمحمدی قراردادشو با دهوک عراق فسخ کرد و در استانه سرمربیگری تیم ملی امید قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/141074" target="_blank">📅 22:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎙
🇦🇷
لیونل مسی: غمگین‌ترین روز فوتبالم است
✖️
✖️
امروز احساسات زیادی دارم، اما اولین کسی که به او فکر می‌کنم پدرم است.چیزی جز تشکر از این پیراهن برایم نمانده. ۲۰ سال، حتی در سخت‌ترین لحظات، هرگز دست از جنگیدن، تلاش کردن، تمام توانم را گذاشتن و خواستنِ حضور در…</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/141073" target="_blank">📅 22:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFN-c6usMCtd0CKhq7J1-Qtj74UU2PWtNhUnmNiimMvkUCegGCH-I4I14a-dioH8yd4u3eg2N5N36RsUr70VgClvD7Rf_WCegq1miILt2EHjmitci08uHdO5r4stlYeYbhGbNB8HANKkb8QLo2Dp3zFWX-abGvBwFBi-i8Z-tMTKBxEJKOQA121CmyX5CziS6Ellcte3eJWt_imyeqYZKX51TLTI6EOAht9AV4t7RO7f1vTyKorbsND9nMNxNurvVLWDmNb-vQhLMrXLAMf-x9Sx-aVzn1ErN8fe-sf6quLB1ZIzKnH2hEThB72yKSvibf-CooJ8b-nGKdqqG5wZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:
• ساعت ۱۴:۳۰، محمد نوری سرمربی نفت آبادان
• ساعت ۱۴:۴۵، مهدی تارتار سرمربی پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/141072" target="_blank">📅 21:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUpk8HWWmSJIyWcysFzOPC-mH1YjN29IRj0z0EEsNhee_S7JD-Lq6Bzi_KYQFEm8-dY0NPX3cyvxVLe92MyEX6pfCNra9tbkkFka2wNe7Pfr2noEvS3K1kUvFIuuz5Lu37q4OkhADyMikDfyx9O7DNGeF8mPRjM319TfBvVE12LFT7gLPn_o0HqeMIdK5Fqf97vMzoJCuF6xMU7s6UtKWR2qFrLICBL6JZNbXcKnz9PaMdstVLcBdgxjuhtJXssNG-bHDGkmgbR5iqb2PeYwL6UABMnFdl7Wb1j8IYFBI_5g-53Mhe1GaENIr6bzkW96n7n-HfIaWfsGyMUduu8WXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری از تمرین امروز تیم پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/141071" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
رامین رضاییان دیدار مقابل پرسپولیس را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/141070" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fbb819f6.mp4?token=DBDZt8AbWXnvHtFqIdQbYLNY27D3My-sIwZFzXGhVzzO8qr731O9RvH1MotS3TRLPNRrEGtUkQa9ZOtRcZixdWi1OIAXjrL471MipSAWzIQeyUEFcsNo8Fp3bjDD7eHVTrfhRTcOOt-PbxPTIUclvTtQfLa6WE96W-25fJ4-dQEEUPcflOBW8UbnC9xL5kwgIykxoZb1RW9CYPugBpExDPDm2jy-5iHsgpzksVpC__UiG5xwPium3K63Z2siDJviPBZGqCn-v_zxTHkeQdMLhPUrjNWan12XAMYwbDD8nAOM3GY3TCOqHYuQXbph_WOJNW8VJtcP2HLxarxXxcjDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fbb819f6.mp4?token=DBDZt8AbWXnvHtFqIdQbYLNY27D3My-sIwZFzXGhVzzO8qr731O9RvH1MotS3TRLPNRrEGtUkQa9ZOtRcZixdWi1OIAXjrL471MipSAWzIQeyUEFcsNo8Fp3bjDD7eHVTrfhRTcOOt-PbxPTIUclvTtQfLa6WE96W-25fJ4-dQEEUPcflOBW8UbnC9xL5kwgIykxoZb1RW9CYPugBpExDPDm2jy-5iHsgpzksVpC__UiG5xwPium3K63Z2siDJviPBZGqCn-v_zxTHkeQdMLhPUrjNWan12XAMYwbDD8nAOM3GY3TCOqHYuQXbph_WOJNW8VJtcP2HLxarxXxcjDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل برتری تاجیکستان مقابل چین در بازی دوستانه توسط وحدت هنانوف، بازیکن سابق پرسپولیس و سپاهان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/141069" target="_blank">📅 20:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
با اعلام جواد نکونام، سرمربی تراکتور؛ مهدی هاشمی نژاد وینگر این تیم به بازی فردا مقابل استقلال رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/141068" target="_blank">📅 20:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
✅
احتمالاً در صورت غیبت کنعانی و علیپور، یکی از بین اورونوف و خدابنده‌لو کاپیتان پرسپولیس مقابل نفت آبادان میشه؛ بعد از اون هم پیام نیازمند بازوبند رو میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/141067" target="_blank">📅 20:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPivsyHYypULw_xjA5pZGdMqWbubNMx5KCntCFn7rPKBNRBx_ZbQHeU8DRZplgyxj70QLdG1yaT8suk2WrWAX-hS5lQYEBY1PzcIqfw3SQaUSTAcrgm6TQzl8k9_XdFe94G5pMM2MRmaCZQKZgkRyQOij1akcZIsaf55bidrh7but5igNwApCM-ZEHZ6eWEb1ZPAOmcY2e_wr-kgoudDsiXEbhXsNx08IdEBhVQy1B5iBTEtvAyKdX6CGJKOS9etQq-dYTiIbfPdR9RDfBt1OHzCmZ7MqDZpbcm4F54KHPGEZr2zIzFjBGO5b2kwPkcOPqqiQP1XjdLTfqejoO-aAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت‌ نود
🔵
کازینو آنلاین
اسپورت‌ نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت‌ نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141066" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/141065" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W87_cC8rkVhcON7Ovs3gN6OnFEoezd_-g-tXRq2gQVtz1x1P6PLDwdTGZMy8n2vIqEWv_Mhv-hHmOuFixmppPaWmsE9EjrpuoLKphQPx5iLCbcecUMR1dKDjIN6LZ2lHJrC_un65aPLyp1RrzGwlNkHIbyVbotQI15OpqE_tyzkgKeBP8XNJnZOklDM-sjwt_FNnk1tYHjZTxUxTnIgVw95fGXDgENuCORh9s9ynk7e-D8CH-fH0CUng--dxTybbxzTidylF0rErqLu-vt5JKsp_e19Y5Jt6z2BWGFnWcVr2UNuktvbQ6TkNwPrGXuDQ9lfpEWGcEDFuUlqQRd__nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
حضور پرسپولیس در رقابت‌های فوتبال ساحلی بانوان
❌
❌
باشگاه پرسپولیس با خرید امتیاز یک تیم، فعالیت رسمی خود را در رشته فوتبال ساحلی بانوان در لیگ برتر تهران آغاز خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/141064" target="_blank">📅 19:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plZ634NUZvRqkLMlHpShAsuTIsAd5fDRpd1F8HSB6iYlkrsACaDLqiWPFXqUcrdg3gG8vkkN8eNCsIR2LN4fd1ilXnxeh5tEojQpUh_XyazhoHj4bdx_rUFp0w5v_eNIQ-uVqUiDK0c_UsJ9f6SLaQZgVvAeVXe8b8zUywR5jdsRK4ZeqcT4WLPpSsRA3ZzRSMdJV1tECaankQJ7qK5_8aNkIaHnmoVHY3FzyshnxGmpkhqkQNf0Posaa3GdKgPijTU2UaFqi8t2CHRG4-l3tHvf5Q9eX5I2HQ-VfguXN7TjOdmvf3536tBuZmkjDsZ9GPzz3hSON6L8Rsl0YGIlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
سیدجلال حسینی سرمربی تیم دوم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/141063" target="_blank">📅 19:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
بازگشت سیدجلال به پرسپولیس!
🚨
اگر اتفاق خاصی نیفتد سیدجلال حسینی به عنوان سرمربی تیم دوم پرسپولیس فعالیت خود در فوتبال را ادامه خواهد داد.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/141062" target="_blank">📅 17:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9jkULU7I7dcakycGwftZprIBAwqxtSv3-YZkGJTLxMsngiKISUjqnHFjQEXqMvzv3-GLODd_DxgjHeLfFPU4Q6OU616toTbeg1rDGX_9VdqYsJKcH4muqCekiENczK7PPHRWkPok3UCB78mLv4NhtHdYgq5T-iz8OFlIjvZ7S3E7WOf-0VPoBclBnoF3cfWMnW3DkUw9IMNuDv18Drtr0mi6g-ATS9cjHlIB9PsUoryNNvtp5fDSRCZnJdNcYRL1wfZRQHRe8Ia2Jh8Ds48EjydfsjYyYJnSsi4CuPQnnR3-JPueH6VoPIyPwDAjNVlPhY9rZ06Pl4YNNRFKMS1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
❤️
بیرانوند صبح دیروز به کمیسیون پزشکی اعصاب و روان به دلیل داشتن خالکوبی رفت، همچنین دستی که از ناحیه تاندونش مشکل داره MRI گرفت تا ببینه نتیجه‌اش چی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/141061" target="_blank">📅 16:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
ترکیب پرسپولیس برای بازی با صنعت نفت دستخوش سه تغییر نسبت به آخرین بازی این تیم خواهد شد
🗣
حضور حسین ابرقویی بجای کنعانی‌زادگان
🗣
حضور تیوی بیفوما بجای اوستن اورونوف
🗣
حضور پوریا شهرآبادی بجای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141060" target="_blank">📅 16:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✖️
مهدی هاشم نژاد به دلیل مصدومیت، بازی با استقلال رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141059" target="_blank">📅 16:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYKXi6PgDjgTi2P-SB1GHugPkXuWOAueskVu5T0Lz8quoRCwQxQLzuREjgFO4IvfvAU0XS4sAdzBw9xk1hba34qwKaKafTI8YTtO1SS3l-P6P40E7PHeUWcSvJxug-vTpzePqecCc3Pu6drrOVktm431P16Ti0kSoETrHFV_DymaQSCodexbEvCZDCaMaSAXaZr6HOQhb2Aw9167b-nNw_k4gcHVS6DAhxSR2-QWwTBZm89hB25v_wIF6FL80A3WlxYt9Vnk0qjFMc6FLH8VE0yOWLjElmK_Za1a36KceliS4v1kMU1wwtBf63zObH_PJnYMLkXUEFz_bZ1W-R_7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بازگشت سیدجلال به پرسپولیس!
🚨
اگر اتفاق خاصی نیفتد سیدجلال حسینی به عنوان سرمربی تیم دوم پرسپولیس فعالیت خود در فوتبال را ادامه خواهد داد.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141058" target="_blank">📅 15:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3zqWZC3a3UjjZlaZcTk58q52zlzEwR02JwdPgRCNdU3EXou_gtauOnFqKuQTGfe_flp4nPEDvm39mSKkvHhk_FZa9HZkCAdNIXS3NluhylmoqRtLAkp9EXDuYdsm_wJuPGKYxger8G28JU6eE-yhq2Vn0smQ6Xorv0A3OeyGFDlkxm7if6NoWUw_x01a9LAIPu2xvFmuOaiCs_xvKAZTae05d0gmicQTZDsSrVzDoUkcA4YbRtlmbKnYRONMdvrqJBcIBBpEo3oOomkDraCfMK7muDVC6_bpQVKo2603qEmxrrvr2wDm5WNrGamsLhoJ-wW1GlUvPtTAuFyvMlKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
احتمالاً در صورت غیبت کنعانی و علیپور، یکی از بین اورونوف و خدابنده‌لو کاپیتان پرسپولیس مقابل نفت آبادان میشه؛ بعد از اون هم پیام نیازمند بازوبند رو میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141057" target="_blank">📅 15:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
رامین رضاییان دیدار مقابل پرسپولیس را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/141056" target="_blank">📅 15:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED-p7eP3FOCDGAsVDMUt7N_M7k_ECnlb8JltHfjSERPCcYG9Pp_GuqsIUo1_iZa-RLBjBcrsb3ExAxkDRod5lJEjM2PCy6o-IYSMe5n-4XrPOdiM08oez4UY80xtvw7DOWwJPHJkxfFLiJsoz5Rs0SGb6qBIk-1UhWMgihIQgAJWdGPxQcip0vihMpSjgmMmBcrLChIl4INuQY6v2t6loKttHNAYTYUgfOSlgT7Tge_CxdxKA5ierQD0zgvtD6HEOtN3LG_FhkpNnJzlR_CLiJ3ovp7PUxIvLZ-gQn-clBEl99sAVev7_7o-6nOZZtKeBCd9beOrSwdFP9xOrJEQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
#یادآوری
‼️
همینایی که با حکم ٣ بر صفرِ شکایت‌شون از ملوان صدرنشین شدن و الان باهاش طلب جام میکنن‌، پرسپولیس رو منع میکنن که شکایت‌تون ملی نیست گذشت کنید‌. ما ذات شمارو از خودتون بهتر می‌شناسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/141055" target="_blank">📅 15:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYCIpyqaG8ibBuPmG3--X2rH4idTsY6YvSPsWXs64SPwxdXSygktdksGQnliNxGBWaBjB0YY9NoGvFBbxrAHSwOE9yUOl7Uu9UbcBKjLYtz5nWAhVzR3214cKXrJ-EcX-C3JAkWCBlaosxpinnFd-819ihOaAtJ557hr8TXRce4jDKNck25fhNJlWwdY1WGUYbFDZubr4awwTYr2SlD_y0eZXiMYOyPMxkMZ2UlHfXA90i6aEHKRvamirIqxBPA7sZroQVxdkrKeZiX-f02fu6RQwf_Zu-9Fg68eneJoUEpXWi1Ap9g-od0u1ywiymP_D2Vqlpvcu3RtuN4Jd5Rkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبر ورزشی: ابوالفضل جلالی به احتمال زیاد در اردوی بعدی تیم ملی دعوت میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/141054" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141053">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✖️
✖️
فوووووووری
✅
تیم پرسپولیس مشهد ( ب ) با خرید امتیاز پادیاب خلخال در لیگ دو فعالیت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141053" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141052">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
فوووووووووووری
🚨
🚨
مدیرعامل باشگاه لیگ دویی پادیاب خلخال امروز در باشگاه پرسپولیس حاضر شد و برای فروش امتیاز این تیم به مبلغ 33 میلیارد تومن با باشگاه پرسپولیس به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/141052" target="_blank">📅 14:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff23e6127.mp4?token=j00Sy7r2wjkUl9blDeky_h6zff0EvT1xYzh-26mc4Y14QyKyhoxoatHvq-bfR2DduMFEslZ0Dp-beXsA5ZPoQYugJNmXujuJPZ6F8qGkKDwlOVg7GlUZEn1o2d9jXW-J7g82M5DWFAF-IZjt3qMqA0k_hJWmOIC6e1kFNX8n6AWFMGOFtYj44jxvkQtBuNp8pfTjjF_oTnWvQG9y-p8jImzqY3hyeOQGMkyfFqhnSe2o9TQl0yVfiq-_EZY85CMSqYZ4n9S4RbEObiOFdStXeyr2D-NqXYGwWxlKa70CJvrAwFjPRy2Q_Sp_o0ba2NlYIIsZyV5G9_GF8o7fIvjGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff23e6127.mp4?token=j00Sy7r2wjkUl9blDeky_h6zff0EvT1xYzh-26mc4Y14QyKyhoxoatHvq-bfR2DduMFEslZ0Dp-beXsA5ZPoQYugJNmXujuJPZ6F8qGkKDwlOVg7GlUZEn1o2d9jXW-J7g82M5DWFAF-IZjt3qMqA0k_hJWmOIC6e1kFNX8n6AWFMGOFtYj44jxvkQtBuNp8pfTjjF_oTnWvQG9y-p8jImzqY3hyeOQGMkyfFqhnSe2o9TQl0yVfiq-_EZY85CMSqYZ4n9S4RbEObiOFdStXeyr2D-NqXYGwWxlKa70CJvrAwFjPRy2Q_Sp_o0ba2NlYIIsZyV5G9_GF8o7fIvjGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141051" target="_blank">📅 14:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فووووووری
✔️
💢
💢
💢
تاج دیروز با مدیران باشگاه پرسپولیس تماس داشته و گفته از پرونده آسانی بگذرید
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141050" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ارسال پاسخ دوم فدراسیون به AFC بابت یاسر آسانی
🔺
فدراسیون فوتبال که با سؤال کنفدراسیون فوتبال آسیا در مورد شرایط قراردادی یاسر آسانی مواجه شده، پاسخ دوم خود را به این نهاد ارسال کرد.
🔺
فدراسیون فوتبال ایران در پاسخ دوم خود به دستورالعمل حاکم بر قراردادها…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141049" target="_blank">📅 12:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141048">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/141048" target="_blank">📅 12:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141047">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7jJvRWDBfECMmfhZA_9isSejVFMtWn_HraaCy5Px--BZT4eb9fl1Dfw9VZnNZWLiQu9dM9GTy6wOzE2EMZTWLl6WNdGheq9oxp7IEcAuFTWYEctnp_bKHNm0TOj-hl5j9yLs3oAR1ubogAdiskXqtAgpcw7m4qQCR__X1in7uimYXFaHGPIeO5EgOdsIyhYKHV35FmxGOHvk15i9wN0SOK6bJlmUhYfxrybJBPgRNjGhaplX3z34KlKEXBdqqEePfomGkRLyUGSrPQi-Qwkyxx3vCzMTKKl5-8zlXyom1dYzj6k63l28AekyRFXFUYKpn_gS1WQE-GZ1lrZYsWOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس و دانیل گرا بر سر فسخ قرارداد به توافق نرسیدن/
فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/141047" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141046">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDHaoDzSuSdWz1iu5Od4mZPOCbWwNMzxo55yGMDQ9BBkv3gIz5R8mCBLMHr0xDtEyQL3LbKX8LLI-cmXBrgDWEDsD7h3GafQkGYbn_hfCUlKvk9GhzKnm53EXBFO-sweK_7PS-3WKxQDvS5zd-PiEOYP5XieSeehxYwlncJYhu1n3avlMZRSd4KmRiBULNqEVxphSj9Sa8FsVmOTWjRmplAPcqgBLpES3HRHhzR9HedMOkYWhd6_ZrcyTXcJKNBBQCnbDxefepb9uFK4mwCryeNoPOoy9E9VSeWHTdQfL9R0pk3VRo6hKkrULI9EQSBaZeLmfevAkaTQjsMXAIeBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
🤩
| طرفداری:
🔴
🇮🇷
💣
علی قلی‌زاده تمایل دارد فصل آینده در پرسپولیس باشد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141046" target="_blank">📅 11:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141045">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPPxyMDRS1hwBDYD7-YvtFYUZZVadtfTxs1rvVAD1VT3MjPb281MbaWPCPWK41kr7MlGhmfMy2tckeGQef9YayFzVpn9V_xxefEQVrWK0R0CpEAhw8LAADFOqxCE0YJTejWuzHgNtL1xt4pZk7DGcdSXec_rtHMgKj2_Y2B1jqDa6MUKl-ONiW091fvvHnnwCIU0pyh4wDW5pnXscdBj1oj87shr_eGBxyVp9XGBLdEkbZhJTsMlD7aAw4eJqtAKm9GzV0hwGxT47SC4U7hjvcyUQEjAGquTB1gh3Y3dHeB9slyW3ZxBtv30Vmdg8XW0SFVu05JazjbBCuimiWWwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی کماکان شرایط حضور در میدان رو نداره و به صورت قطعی، غایب بازی پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/141045" target="_blank">📅 10:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141044">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpsBcmQ5bdXr7mJwCs6aifGOZZrGAbktMDMbRDjkDE3uXK5uScEM7AVoenN6SOsvtxm795AQQOEPtw8ERlFmfkqkg2o1qWgs8Td4WPknY9YshnoP3WOZZqWPnnLya1d4yMKWxZtLPjRDdEzigXh5IXNEh3_KTiXhr2oSrHdlYuq74P8fkPgpsw9ciVQeEcMKXGeiKpFvBpiXgt3qK33Z4n6luLIu97mhqHrnNZM3PmGBTLSjmGjtvzguae2gOVKtSJaIkQ6T9zbL1NZvc4eDxFpcVRT23kU1do01IXR1XivyWQcXnt0sTwnclZdS_lOgEYzQUzT34X2fmK5O_nUq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استقلال بیانیه داده راجع‌به آسانی و گفته رقابت را به‌خارج از زمینِ ورزش نکشونیم
❌
کسی این حرفو میزنه که خودش از گل‌گهر شکایت کرد بخاطر باگناما و حکم ٣ بر هیچِ انضباطی گرفتن با همون امتیاز مفتِ شکایتی قهرمان شدند‌. یقه‌تون رو سر آسانی‌ ول نمیکنیم‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141044" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141043">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/U9oIUYx3oBZEGQHxQariTn4-Gbml6y4aVstUxMP-R_iUaWMljpNySQ9VnsbKgVyGlo_rgRa4e9afTlCtgNOR8I316XTKZWmI-hnSNy8ZWBcNQ8MintVOhrmVuHhTdeOc1J7ReeCtoL_4Jycn9rjg7b2vw-8VLXDI7_r-eMuY43XyPYC-6TH719bvfz5cp22CVK63TeVU-l1ju1Rlly2vaWhVKXpxBQ-kWuLwMqcBTdQuco1ZUMV5yh9jSH0FOsjytfQ4UPtcbnZw24kZVhAIZFdIefOXD2ICdXmfundCmUFDrGXDPxCpaX6JYwxB2drkTKapS4svGo96-Q_9HmS_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی تو بازی خداحافظی‌اش، ۹۳۲مین گل دوران حرفه‌ایش رو زد؛ ۱۲۶مین گلش با پیراهن آرژانتین!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/141043" target="_blank">📅 09:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141042">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎙
🇦🇷
لیونل مسی: غمگین‌ترین روز فوتبالم است
✖️
✖️
امروز احساسات زیادی دارم، اما اولین کسی که به او فکر می‌کنم پدرم است.چیزی جز تشکر از این پیراهن برایم نمانده. ۲۰ سال، حتی در سخت‌ترین لحظات، هرگز دست از جنگیدن، تلاش کردن، تمام توانم را گذاشتن و خواستنِ حضور در اینجا نکشیدم.
✅
✅
اینکه دیگر با تیم ملی آرژانتین به اینجا نیایم، درد بسیار بزرگی خواهد بود. دوست داشتم تمام عمر اینجا باشم. بازی برای آرژانتین، زیباترین چیزی است که وجود دارد.فکر می‌کنم وقت خداحافظی من فرا رسیده. با هم رؤیای من و رؤیای تمام یک کشور را محقق کردیم؛ قهرمان جهان شدن در سال ۲۰۲۲.
✅
✅
امروز باید غمگین‌ترین روز دوران حرفه‌ای‌ام را تجربه کنم؛ روزی که با تیم ملی آرژانتین خداحافظی می‌کنم. دلم برای همه شما تنگ خواهد شد. از حالا فقط یک هوادار خواهم بود؛ آن طرف، کنار شما، تا از این بچه‌ها و هر کسی که بعد از آن‌ها می‌آید حمایت کنم. برای رسیدن به موفقیت‌های بزرگ، به گروه‌هایی قوی و متحد نیاز دارید. از خدا ممنونم که مرا آرژانتینی آفرید. به آرژانتینی بودنم افتخار می‌کنم و خوشحالم که توانستم این رؤیا را در کنار همه شما به حقیقت تبدیل کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141042" target="_blank">📅 09:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141041">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7ZXnvMO2f0LW4xrdV1OvCs0q8xUJkcmarOTlShPz0fudR7kgzyqKcypqD6AK0mP8ziU4FXj4VQ8vRl7VINywBv5RCWHCUipkaZDP7UxQvR4mKe34mt3SdFQ9rGc5bEp3T5peWPpRubyLgZ3SXAjEJ5GC5WZRkQ0E9DkD1mUt0esneT3gs0W7ZhJXcpRf5NmBGZ6SE-BNyNEKQ-S4ObGhx-_2qV6PUDmxJjz413b6NwpwWEE_oz6MjH6UKUGR56ZVXU6gYrR_51qthUw2zkKE9exV1m4rhLCs7M9_6wJ9jEg1cV4GrPPs0jxbC8GbGie7-QYYV6FBuZi0mSeeVhiyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/141041" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141040">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/141040" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141039">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
❌
کهریزی از استقلال دور شد؛
❌
❌
محمد محمدی، مدیرعامل آلومینیوم اراک، به‌دلیل اختلاف در انتقال خلیفه و گودرزی به استقلال قصد دارد رضایت‌نامه عباس کهریزی را برای باشگاهی غیر از استقلال صادر کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141039" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141038">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
#تکمیلی؛گویاخبر آزادی امیر تتلو خواننده مطرح ایرانی از زندان تایید شد و بزودی او آزاد خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/141038" target="_blank">📅 23:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141037">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
فووووووووووری
🚨
🚨
احمدرضا براتی کارشناس حقوقی: حتی اگر آسانی فسخ کرده باشه نتایج سه بر صفر نمیشه و فقط پنجره استقلال بسته میشه و آسانی چهار ماه محروم میشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/141037" target="_blank">📅 23:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141036">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/141036" target="_blank">📅 22:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141035">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkateE3uECV-f9ZDAMqUJkvBOpRW6Z4mZyD_PX4i1AuRTj1uPrTtCOTUASnGu3wNb8LrwYd3rCCr4-ja1eLmb0GCqjEpBou8wodD5z1CwDzfC-ZkDhohE4dsLzQwcRq-FXMamW704Pn7P9Scu8KoRObW1si1OK_ghwfUEUjBu898dEHOuj38fYKrpHSpCZWuGtBVhO1vyI1TAjQPiNqOyextNzd7zQtzdkAkWXxPedUxXC14TxqOcWI2ZiML8BjdOXFc8KnQOUJEZP7FLLpCZoBeIWt_SzJ2qoaOMak9oLUZLk3wPvcJgiUcJs-6-yA73avGkldzi5ZOvP83To10Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141035" target="_blank">📅 21:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141034">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f02aed72d.mp4?token=hnoam4YdYrOpeNDMkfIJBsn6TLZJkAgHoSdim6eNwseRNuZw6MW2HFxO6_fL0Aesqmx1NqscP7LbuswUEb5cAt8NhOsZwzXOXP0BIF_cT1sVBVE8z2S-dlnekv7pJavdamLaqOJG71psGKBJRi3qh4xukVXlJHz-EK_Hw2OIPPEnyESmA245hy_EFttCDm566EE3I9n7mvNIcTtOuexAQsLqBCHJnXf9iu0Lb0Nhj_T06mqYejNqdwLh3BZnXUVMMLvjrBL-PvaNngZDBqv98TK_vN0oGsYDERyXjp5ccvwUtAwO7iBF0OHWexuIKAEysPMc9kw7YexGhLJ4IFt6VYXFW6KULoLB0ZjpUKtfsAvjA83ciZAObPJUuf4c4k5VEnNTYfSHMom_uxu5hKkbE2N0OBbyTgTD6lp4DemUz4tD0tcQuB-bHSoJKpqFVjkOHKAkMFSfJ3t5ZqxBybyai0ttrfiUVROqarqOZcJVhfoY7KqoiO4C9cD43bmAmmWgGSkSFN2dlMxfawl-CcAvbNwORTHLPWUzr47CHz4QN_HKLQoSjfzu84yBisPQGAFugjtgZ8OhBl6UrBdoh-zSEOxmjgEDlsE769Aci9s37-BYVzVmHnVhrTMBP4m46qqXNk5Qc0C9IKQ30SzJTsU8gxMHvtTNseHgGziJu8m_8pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f02aed72d.mp4?token=hnoam4YdYrOpeNDMkfIJBsn6TLZJkAgHoSdim6eNwseRNuZw6MW2HFxO6_fL0Aesqmx1NqscP7LbuswUEb5cAt8NhOsZwzXOXP0BIF_cT1sVBVE8z2S-dlnekv7pJavdamLaqOJG71psGKBJRi3qh4xukVXlJHz-EK_Hw2OIPPEnyESmA245hy_EFttCDm566EE3I9n7mvNIcTtOuexAQsLqBCHJnXf9iu0Lb0Nhj_T06mqYejNqdwLh3BZnXUVMMLvjrBL-PvaNngZDBqv98TK_vN0oGsYDERyXjp5ccvwUtAwO7iBF0OHWexuIKAEysPMc9kw7YexGhLJ4IFt6VYXFW6KULoLB0ZjpUKtfsAvjA83ciZAObPJUuf4c4k5VEnNTYfSHMom_uxu5hKkbE2N0OBbyTgTD6lp4DemUz4tD0tcQuB-bHSoJKpqFVjkOHKAkMFSfJ3t5ZqxBybyai0ttrfiUVROqarqOZcJVhfoY7KqoiO4C9cD43bmAmmWgGSkSFN2dlMxfawl-CcAvbNwORTHLPWUzr47CHz4QN_HKLQoSjfzu84yBisPQGAFugjtgZ8OhBl6UrBdoh-zSEOxmjgEDlsE769Aci9s37-BYVzVmHnVhrTMBP4m46qqXNk5Qc0C9IKQ30SzJTsU8gxMHvtTNseHgGziJu8m_8pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
گرشاسبی:
🔻
تاجرنیا نباید دنبال این جام باشد.
🔻
قهرمانی پرسپولیس در سوپرجام با قهرمان سال گذشته استقلال در لیگ خیلی فرق دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141034" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141033">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
#ورزش‌سه : حدادی پرز گفت پرسپولیس دنبال ترابی نمیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141033" target="_blank">📅 21:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141032">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141032" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141031">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRLqjq3ia_S_xhxIUD_q1mVfh3ncT3ZqMFRicFf49KM94HrSp32BAiJz4k4l513_UT319S_UBHECJJtIiDOGIKbVNBbaVZ3oz-SY6kYP6D0kyQbltZFSdpGTlT-YH4MB-j5yREwOhyGlBL-LY0qo0ZmdKcM008aPcqdgHM3rlNbPo08-HSXejsjHukbdtH4rZwebjs_JJkg4bmoI4mVrURr9ov1g-xWxNSJnKqQE4ms2wiFqPqlQYW3Ib_YyzlnkRMHLa8waRLcVDbyVS-7JhFeMi966IObqGt7Ov8YCu_4tQBR87BmLzPyi3g8WbM7q5Bq8PbhkM7i0tntwRyVufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Croatia -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Stadion Poljud
⚽️
اسپانیا با ۴۰ بازی بدون شکست و میانگین گلزنی بالاتر، از نظر فرم و قدرت هجومی برتری واضحی دارد. کرواسی در ۲ بازی اخیر ۱۱ گل دریافت کرده و مقابل اسپانیا هم در بازی رفت ۴ گل خورد؛ ضعف خط دفاعی مهم‌ترین نقطه نگرانی میزبان است. باتوجه به‌فرم دوتیم احتمال می‌رود ماتادورها در این دیدار هم براحتی پیروز میدان باشند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141031" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141030">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjS119NqNASvIB3MOsCes4L0MwwtzQvT1UpnpCEzGmVaoZNtB2X1cIRNdFlz8JeAf-dFdJL5y1UKzNGu_7pGPxJhFohu-rFfOGpVfJMsQ2aIYMDDijOlE1PCC2-m3LOQUp8s_iAqmM8GFAJnMxDukL3aqfsoCa7R42tLNvW4etU_576l_a8ByWzYqq9m_XuKYfNpXRlU7pmyqJf-ulWJ16qP2yzCoN_gg8IE16LnHZEBjKs_FDSPVjURDNPgMNIlIy-6pH85eB_2jb8Kii4AuZDCKyQwqUu0iP9n1pwU3JQXLFQ2vrIKm5xOcl_VjkjWxvzb1DmKxjAjdDBybec_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمودی: تمام تلاشم رو تو تمرینات پرسپولیس می‌کنم تا نظر کادرفنی رو جلب کنم. اول می‌خوام تو پرسپولیس بدرخشم و بعد بتونم برای تیم ملی هم بازی کنم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141030" target="_blank">📅 19:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141029">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✖️
✖️
✖️
مهدی تارتار با بازگشت مهدی ترابی مخالفت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141029" target="_blank">📅 19:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141028">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daQRBLAfRxPDtssYdB24Ftkx5mARWbZnKhK435FxyAsT1ZG-p42EYBT8geVp1yl7QsEY_zxqzuxp-ZfNGxGMUe6brOxic6qtQBMKsgzxpazaB7LOXIUsUADhFCRSIYBxSrkTiaSZNwtVpIiPL4iQ7bixmj6xOTkfGKxwOpgGlpbHPHKXUtHZZo0uXnyI5afo-uca3bnk03g3Idbvo18sOd9-el02j-BdBxK_64btdtsAKSoWU0mliHAd6UaZ48lm70uhSfiozKcNeWV4J4SEORhU216kU9gHIixR28lAwlqEdmm6VlH2uZ-0o9-F6e_xUzQZ7IC2CzIEqLgSF-U43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
آمریکا ویزای تیم‌های کشتی ایران را صادر کرد
🔹
آمریکا به تمامی کشتی گیران و اعضای کادر فنی تیم‌های ایران به غیر از یک مربی روادید حضور در مسابقات زیر ۲۳ سال قهرمانی جهان را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141028" target="_blank">📅 19:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141027">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141027" target="_blank">📅 19:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141026">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/141026" target="_blank">📅 17:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141025">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6EzHOhc8c5-kYSCysqb8y4Fzrf9PkukoNjQZ3A49cPXB4qDqp7tdsNfJFcTm8tnJDw67tKzMLCjDUd1k-EaJsqAOJJ24u7DQ70A6LBegpV6oeRzpc4rKtuR05NZYlWgy8E9fpAqMYPCIaG1L67emBr-lUrTumfm5lb_Jy_0l0hIaKy6NVR4e9VST8d3Xwk6J6ubO8gHTec0KjFniOVmSYnk9nlCHIDor4fkvU-WUlfKOdBfH2S4oZNJyLlLfudbB--QOsCc9Ap3ABO6Ed4Z4QUA1gkZzMubTyR19YWwY882HNRSckOTo-gCQMQpn-l1RB455Q9v_0-BYz6jFeQPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
دنیل‌ گرا در دفاع چپ؛ چراکه نه
🤝
🤝
باشگاه پرسپولیس برای دنیل‌ گرا هزینه کرده اما ماه‌هاست که از این بازیکن بهره‌ای نبرده است.‌ گرا بزودی وارد چرخه تمرینات گروهی و مسابقات خواهد شد و می‌تواند گزینه دیگری در اختیار تارتار باشد. او در دفاع راست رقیب تازه‌ای برای مجید عیدی خواهد بود اما همچنان یک بکاپ مناسب برای دفاع چپ نیز به حساب می‌آید. پرسپولیس در دفاع چپ همچنان دچار نگرانی و کمبود است و با مصدومیت‌های متعدد جلالی اوضاع کمی نگران‌کننده پیش می‌رود پس می‌توان به جابه‌جایی‌ گرا از راست به چپ و حتی روزهایی که عیدی روی فرم نیست حساب باز کرد
✍
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141025" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141024">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubIEEU7QvfNLLVjwzhaJzdjcOoKRi3DJqaEU5_NJuFkxyl7tBmgzlEvgeiMw1CoOwWjURJg_ze_KdxKsssZhHu8JHXqHl7dzk6XqmOraKXfM9cA0OQwDJKrRs5Jx2LE9v0MtPmDFiaqkvA4sPUov4jFnkvmL2Cpzi3pOBSl5UuM8-djIPYYrWVOvqysUB5UxVuc_BZP8oorAooJkQ1P5X3l0_5e-DvnTJbGbqm3NfU8s9cJ3Vt8fVFEGafAxoYw7YHgFdBc8JRw6xM5BHufGMgwaX_fk-6HcZ56JYlcb0w0qm3e9bb7Fnl7qLIqXcvtw7jzWDAGpVdXtsCOUOaDsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
مجموع قرارداد بازیکنان پرسپولیس اعلام شد
⛔
⛔
مدیرعامل پرسپولیس: «جمع قرارداد پنج بازیکن خارجی ما ۴.۰۸ میلیون دلار است.»
🔹
با دلار ۲۷۰ هزار تومانی، این مبلغ حدود ۱۱۰۱ میلیارد و ۶۰۰ میلیون تومان می‌شود؛ یعنی حدود ۱۰۱ میلیارد تومان بیشتر از مجموع قرارداد ۲۷ بازیکن ایرانی.
🔹
مجموع قرارداد این ۳۲ بازیکن هم به حدود ۲۱۰۱ میلیارد و ۶۰۰ میلیون تومان می‌رسد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141024" target="_blank">📅 17:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141023">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
مهدی ترابی به نزدیکانش گفته بعد از اینکه رباط پام رو عمل کردم، هفت ماه دوره نقاهت رو گذروندم و تمرین بازتوانی رو هم تمام کردم دوست دارم به پرسپولیس برگردم!//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141023" target="_blank">📅 17:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141022">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
سرقت موبایل از سرمربی پرسپولیس
🎙
🎙
هفته گذشته موبایل پیمان حدادی در مسیر بازگشت از محل مسابقه به سرقت رفت و حالا این اتفاق برای مهدی تارتار تکرار شد.
🎙
🎙
امروز پس از تمرین تیم پرسپولیس، دو موتورسوار در اتوبان تهران کرج موبایل تارتار را سرقت کردند.  «سرخ…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141022" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141021">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✖️
✖️
✖️
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141021" target="_blank">📅 15:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141020">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141020" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141019">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚪️
فرزین معامله‌گری، بازیکن پرسپولیس برای گذراندن سربازی به ملوان پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141019" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141018">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzkUty2wVgE6RUU0w2eKuQZUNm08s4TKiz2DpANT16_A6w6AOTXmZ8FSF9blJRjySzsVg1xJ7vbptwJRcDT8dA7OIjblfKQ9Qnu4L_AhYLxVvIunTeCw1sWagL29Z7XRFKItjP-kLaPDcIyHTygZvVpa3P32Ep_Ivl1iNeZK1fy01C4tTG4MrMLUnvx2dDeoKVaVWqn21mrW3zaycoNxvYkazdmV6uO1jGV74V8CqfzfQx9fAkdOkVL4_J1-qi4nyW471XycRvLE2l9iMZUAMbv5uistk9c6RXWszdtSvvGoRTV0gm90_FvpBMIRcUMQyjigEicdvLp3gjMZHZRC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد آتشین بالکان؛ کروات‌ها مقابل ماتادورها!
🔥
⚡️
[
کرواسی
🇭🇷
🆚
🇪🇸
اسپانیا
]
⚽️
کرواسی با بازی فیزیکی و انتقال‌های سریع، می‌تواند میانه میدان اسپانیا را به چالش بکشد. اسپانیا با مالکیت بالا و گردش توپ سریع، شانس بیشتری برای کنترل ریتم و ساخت موقعیت دارد.
سناریوی محتمل: بازی نزدیک و تاکتیکی؛ برتری اسپانیا در مالکیت، اما کرواسی خطرناک در ضدحملات.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141018" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141017">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlkY4EIFkcRfbE_Fv1RjASp5FUX-3tRnrPwhSdIkyllTmFOwSHNBzJIBkBl-njC0hAoYqxszWUHWKaPz86vaBQMQrZuyyWGqWLq0iVkwg7lTRyW4pGr-d1KE7nbG16961GuSpozfa7Bf9VjuSmrX189-imsvL2TaFFkDsa-ltJO0Tdk7qEz4XbDwIEhF1Dtky6-mMcvYwkwDAv-9CDPUln4cKswmvm77VplJzn0GIrm-PiyqAA2CIZaBz-0TftBVyz5uxyRne7QkwuIhh9eY9S2Gaj_77w0n7LDukoyJahZy1VPEYevxwFvoQT0d13yN7dxo_oxRikotJKEQbEROPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
ورزش‌سه: برخلاف خبرها پرسپولیس هنوز در مورد اورونوف تصمیم نهایی نگرفته
دستمزد بالا و مصدومیت‌های اورونوف تمدیدش رو سخت کرده. البته احتمال تمدید و فروش او با قیمت بالاتر در آینده هم وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141017" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141016">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
حدادی : در یک بازی رسمی از عالیشاه تقدیر میکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141016" target="_blank">📅 13:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141015">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv4UEodUw9mT91hFv2i9xeICujGzfyTvdO4NGw9ni_ySg9dxRhp3WId6yTiXtEs6xWnZVNSYoAAeV5ZK9A2B88bcjC7hCeMej1Pdi2ea6mO2tJN2jmRN2AO5Q-Tj8t_8Q0l2LnY5D799xtup8qHXVXgSdUt7nwqqvsyyEjCfULuRbLM_0lNYtmNuvQB4qa15XTQ9_Md9GlaJkSNmk5libIlhbmGpCm8sVX3itKVJn9-iLCuFxv_zEgpsOzDNl9HaWKa9t8SPKSRWmUsc2EVlbuMDKYy-WmbutKBY2-JUWEh3jZ7s7je7is1P_GmZN62QVWpa9wqNowlcJYD3AwpmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
به احتمال زیاد امیر تتلو به 20 سال حبس محکوم خواهد شد./آنا   پ.ن اینم نابود شد
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141015" target="_blank">📅 13:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141014">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_D02fqKLTj5G2ZDRfsVM1T7MI_jdlIIZHpDo2UdisUXchYg664LCObbhVf_wze6PH_ye-gzP1WYSTft4aURi4-DYiL26sLZMBefsjcMfil_qJub79xs3a7mUDiGdIzzbbArUhaPv6n5yfvD_CSiQS3cpO5pfp3R1-CyP1L_kjh4nIHdDNC-vxZ6xUNrl4EYqNXgV9EkYhRX00s9aO92L5n5G9zLpYrWSdpEVasTikNhqOf4LoaXrzXzmd9UiAABjFEICYlEvtYf9TXPn34HbCgCG4Lc7aXnglACgL_MM5xtKxI2HtbNPVo3ghLfxjjqQ0VeTZrf_hKr2Pu_M2TAxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141014" target="_blank">📅 13:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141013">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
پزشک پرسپولیس: دانیال ایری در آخرین بازی تیم امید دچار کشیدگی بالای عضله کشاله ران شده و به محض برگشت به تمرینات پرسپولیس برنامه درمانی و فیزیوتراپی‌ش آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141013" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141012">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
ترکیب پرسپولیس برای بازی با صنعت نفت دستخوش سه تغییر نسبت به آخرین بازی این تیم خواهد شد
🗣
حضور حسین ابرقویی بجای کنعانی‌زادگان
🗣
حضور تیوی بیفوما بجای اوستن اورونوف
🗣
حضور پوریا شهرآبادی بجای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141012" target="_blank">📅 10:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141011">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqa-pikMZ92M1hd-FOe_dtcKYFvUYQOMUBf63cmR07K8DgFVcPtaKDK_F40VHbIpazRGsIj_IGUdBEbpdzXvapqLfZPN7PUAdmgDbgx4Y_0F9GJ53LVRK9wSayKamh0eGzLapXL9yIFRRZcrTO8MMD7Ds9zOsbDFOK0ada9m6Z0hoqKxgXeGx4b47FNCQmLQDx0jZTca-IG2eYCW0fkwhKMpwZMg1OucyQ2WjbbM4iWM-aZSy8tqPM3yeA05HEpQCFOkxB_vz-mIe0KwdiMFAK0F3qMJuQwLAN9oFCFSPEoQQjwQ9ocj2MopJiO8d6EOc-zY74RRUS6xKdVD7UMCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😄
بیرانوند به یعنی میگه یهنی
!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141011" target="_blank">📅 10:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
#فوووری از ورزش سه
✖️
✖️
محمد حسین صادقی یکی از بازیکنان اصلی پرسپولیس مقابل صنعت نفت آبادان خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141010" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141009">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
مهدی ترابی نمی‌خواهد در تراکتور بماند و تصمیم دارد که هرطور شده به تهران برگردد و فوتبالش را در  پایتخت ادامه دهد
❌
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141009" target="_blank">📅 10:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💥
#فوووووری  | #غیررسمی
🖍
یحیی گلمحمدی قراردادشو با دهوک عراق فسخ کرد و در استانه سرمربیگری تیم ملی امید قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141008" target="_blank">📅 09:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
فووووووری
✅
باشگاه پرسپولیس نامه فسخ قرارداد یاسر آسانی با استقلال رو امروز به کنفدراسیون فوتبال آسیا فرستاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141007" target="_blank">📅 09:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141005">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQlEfiZsN89zJ4-4SNNof9ULeSvjbmjSEeMhwPx9B2e2nx2_XTFIN6iGJ_pO8wyBC_3gDeF2fM5R2fAWLEaKygAV1qbtuPM25eiGDHStSNxRXHohB40cNR7-TeDk_QNULTmLilAB-e3FYU7rFi7JP-1t-3pyjeSDdwSEK2ASoNaUG0J3vvvrLUU6EgShCDkrp9uIr6hr4qcJqZQcI91zd23LlKlU8yWry1ccNwPTY8TdiG3yc45D258iEuebCLzRVi6KbZmwuIYK1LxxpmnzGTB7YummUMXJ2JNZC-WHtwHzKa-uq_QHGPRi7B4VUmaioQE4VBaJ5eAgtruk3vhN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
سه‌شیرها در کمین؛ چک‌ها آماده‌ی شکستن نظم انگلیس!
🔥
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇨🇿
جمهوری‌چک
]
⚽️
انگلیس با مالکیت و حجم حملات بالاتر، احتمالاً بازی را از همان دقایق ابتدایی در اختیار می‌گیرد. جمهوری‌چک روی دفاع فشرده و ضدحملات سریع حساب می‌کند؛ اما مقابل فشار مداوم انگلیس، حفظ کلین‌شیت دشوار است.
سناریوی محتمل: برتری انگلیس در موقعیت‌سازی و گلزنی، با احتمال بالاتر برد انگلیس و مجموع گل‌های ۲ تا ۳.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141005" target="_blank">📅 01:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141004">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPPVSuu1gn4EfUDD8S4TTs6XKn3v0vxBzvGthiSlyBXIuLA-lmVgoipC65h9dpSa_uTQGxc0Y3bMnb8-olSv_jb7c4XcytTpOl0wuqU9PGnsCt0P6s1PtwifwGRhZKi7MaeTt4mC6k56iaU3m-BmARbuRyq42_MTN8JeoRif4IFFSTbPx09ciUNEQjdGjzRqda5t2NqY1YkOUh7ckdy5L-XAHVN6tdqLf7JWOAFP0B4v-t7bTfMRVTZrac6zVA40LtHVJ6-MIj4Q4Gwp8gEvnEiYI7-claRUZoekFlBJDFE9iQu_N2Flz4LYg6w0jEg4iyrJRDJcxEE8vD7u_HnC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سعید شیرینی، سرپرست سابق پرسپولیس، از مطالبات حدود ۷۳ میلیارد تومانی خود از این باشگاه گذشت.
🚨
بر اساس اعلام پرسپولیس، این موضوع مربوط به دو پرونده حقوقی بوده که یکی از آنها بیش از ۴۱ میلیارد تومان و دیگری ۸ میلیارد تومان مطالبه به‌همراه خسارت تأخیر تأدیه داشته است. با اعلام رضایت شیرینی، مجموعاً حدود ۷۳ میلیارد تومان از خروج منابع مالی باشگاه جلوگیری و پرونده‌ها برای مختومه شدن ارسال شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141004" target="_blank">📅 01:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141003">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
مهدی ترابی در اندیشه‌ی بازگشت به پرسپولیس/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/141003" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141002">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141002" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141001">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
عادل فردوسی پور: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبود بهش گفته خودتو بزن به مصدومیت تا تعویضت کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/141001" target="_blank">📅 22:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141000">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141000" target="_blank">📅 22:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140999">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
✅
فووووووووری از فرهیختگان
❌
❌
پرونده آسانی از دست فدراسیون خارج شد حالا دیگه فقط ای اف سی درباره این پرونده تصمیم میگیره و کسی نمیتونه کاری کنه    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140999" target="_blank">📅 22:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🔴
علوی: هیچ جامی قرار نیست به استقلال داده بشه و بحث قهرمانی این تیم در سال گذشته منتفی شده
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140998" target="_blank">📅 21:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140997">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIpSsGNl1MErwtOEIwRFJs9AsMkER1oBvNQx2Vz1kmdqyMjCbNhQtjSq1yzmp6xPR58OrRwq1lL6hqIyNnAJtlLE7lHsu4HK8fmR6dFz4W2ynIIYLPuk9_pPQepnva4a9Q8WmFKRNn_BFsi0ONEf3tbsFiwSlykssxwpNNUBcphOe17axfQHHp5rCswWb0GaUc4TLu9CRzdXDrzmNC_0u5imcg86vRAOqi33J68LR1bfgBQ1GZP9hT9euKPuK_l1qTzpEG7uKwr5jjkqL6QjnJ_mlKMU8mHdVPHYhoT6jxvn5mHISy9_LAMbf0sCG4tZupII-a7kxF2S899mzWxzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
گزارش تصویری از تمرین امروز پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140997" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💚
عادل فردوسی‌پور: دیگه حوصله شوخی‌کردن با قیمت دلار روهم نداریم، روزگار سخت و تلخی که سپری می‌کنیم، شروع فصل لیگ برتر، با دلار 187 هزار تومانی، بازگشتش از فیفادی، با دلار 270 هزار تومانی!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140996" target="_blank">📅 21:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140995">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140995" target="_blank">📅 21:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✖️
✖️
✖️
فرصت طلایی
✖️
✖️
پرسپولیس در هفته‌های پیش‌رو برنامه بهتری نسبت به رقباش داره؛ استقلال و تراکتور درگیر آسیا هستن و سرخ‌ها هم بازی‌های عقب‌افتاده‌شون رو دارن.
✖️
✖️
با توجه به لغو جام حذفی، هفته‌های ۹ و ۱۰ می‌تونه فرصت خوبی برای تارتار و شاگرداش باشه تا…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140994" target="_blank">📅 21:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
لحظه گل ثانیه پایانی جوانان پرسپولیس مقابل پارسیان توسط محمدامین قرنجیک
👍
👍
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140993" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGWnvqt5uqR1dwIhCpyPVYP5n5S-mnZCXowQHWvoFFi1tVAOi-_HPFmYFyQt3UOQXoWx38hBJJy4KYnTkE5NCJ8_OrSS6iIkCFGfUY4A7bYKqL6pbv71wK4hXVzc1olxgIxg5AezpxJnUa1cxur-nBRvG_fa2GygIkrT-4LyjSrU1dvWvgNoHF6CKmnxfSsYJIOpzouSXVE4lDwHdE4MX5-fNncwhd6Hhanf6Opo55a4sXxE49nTTjXPVrGi8nTKCiLy-ScOxwMjqR8M4-rlA-KOl7-J43GeW32O8TT6PQu7IVfw8S-9U-JvhSceQZJMZHUOpVI7I_1cMoEVxk_Zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140992" target="_blank">📅 19:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
مزایده اموال پرسپولیس با یک خریدار خاص
🚨
در پی شکایت یکی از طلبکاران باشگاه پرسپولیس، دادگاه شعبه ۴۱ عمومی حقوقی تهران حکم به توقیف و سپس مزایده اموال این باشگاه داد که این مزایده در نهایت برگزار شد و بخشی از اموال پرسپولیس به فروش رسید
🚨
🚨
در این مزایده،…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140991" target="_blank">📅 19:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0qG1LKhGGFURgW0nMVBuXZ2JQWvKWutdFpmsja5VXuIu62BEtQZtpbI2E-fvrg_XFgn3BGQF4fOu1oDvy908n2AIscbB40o6sWOBLJ_jI2Hv6l2K-aXw0j906y-SgbALPvfhYrTh_wuliNYWLLLdeDxGCjDdMrVVwN6gf_tgy8xRMiDJGQRvIwfUxeUhGhjPVetLG-as4J9nM9aqJCHYH9tKm9YcKgV3QtmYN4QCJcioabYmzZrfFfveN8lfIyvqBMaDS4ZzPiRfJUCSmmkLXyyTBikJDncX9BeKcMC11BPPwmnxW0L_dDSkod8iom9mbqnbHJOLxiwN0oOAbZL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇧🇪
بلژیک
]
⚽️
فرانسه از نظر کیفیت موقعیت‌سازی و عمق ترکیب دست بالاتر را دارد، درحالی‌که بلژیک بیشتر روی ضدحمله و انتقال سریع حساب می‌کند. با توجه به قدرت هجومی دو تیم، سناریوی گل‌زنی هر دو طرف محتمل است؛ اما فرانسه شانس بیشتری برای کنترل نتیجه در نیمه دوم دارد.
سناریوی محتمل: برد فرانسه با اختلاف یک گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140989" target="_blank">📅 19:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140988" target="_blank">📅 17:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
🚨
فووووووووری
✔️
ای اف سی در نامه ای به فدراسیون گفته پرونده فسخ یاسر آسانی مشکوکه و جزییات دقیق خواسته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140987" target="_blank">📅 17:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGcVZKFxbwpYfiSQQtm6XuafOtFpAcka-dsvY73wIjARQyIrrYbDf7Jy897bI6bBci_geB8oFDV9HfE1u1s_QGAjs-yN21DhVhhN-EM-L87chBAzdyZ0K10dZFIt72ki7nuIFvApqkZNI5iqSv7P_Un4U7ir73V13aHf5a5sv0NpjEUO-TWBHw5O2MrzDEhZqyGQdDuvp85Eih4gcCAPvcgm1kVlYIFPu9_FbltScxtIohtk-b4CdzwlkGE2wz7qWLfM1e43WWRpwya-zUmkoz6RsSdMiRvvcIm-DRLR7KOHlN4hc8KKT8mPVMnjEDF0jcHcCfsxGbReoDPxZG8iSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
ساختمان شهدای میناب باشگاه پرسپولیس مزین به تصاویر شهدای مدرسه میناب شد
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، این اقدام، ادای احترام خانواده بزرگ پرسپولیس به مقام شامخ شهدا و خانواده‌های معزز آنان و گامی در جهت پاسداشت فرهنگ ایثار، فداکاری و شهادت به شمار می‌رود.
🔴
باشگاه پرسپولیس ضمن گرامیداشت یاد و خاطره تمامی شهدای مدرسه میناب، بر ضرورت صیانت از نام و یاد شهدا و ترویج فرهنگ ایثار و فداکاری در جامعه تأکید دارد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140986" target="_blank">📅 17:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z16pbur1TO_xUvZ_2RaN5nqVoW9M1jaj7vbuZYl3XkS68aW_3hpn5r3k5zP_q1PJG22JkPZW1IRMNIACFx0PFEUhZV2wqjfBXH_TAuZ9v3sh4Mb4GKEjxlQn_cL3Dmc9FZRPi4bmHqkj6LsQ1MxAbGr4n7PmjAPAHAgLpjh1ikXkbyZAKw95aoPqY7tpkvSstTpa_rt871A5L8BIB9PfkkjX6A25I27BAopjkOPfJHvtlM-hQFY49W0TWv7TSps8vwvgdU02F-c9zHZ53m5xUHmVuB--GFhdOZQXkaVqjHJxKmPVHL9r5NkHkXR_nPflAYFicWqFsN-3wOncX60fwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140985" target="_blank">📅 16:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140984" target="_blank">📅 15:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140983" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
کنفدراسیون آسیا جواب فدراسیون رو نپذیرفت
✅
کنفدراسیون فوتبال آسیا برای بررسی پرونده یاسر آسانی، این بار در نامه دوم مدارک و مستندات بیشتری از فدراسیون و استقلال خواسته و تأکید کرده فوراً ارسال بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140982" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
