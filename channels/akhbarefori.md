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
<img src="https://cdn4.telesco.pe/file/F64n2Ox_ZfqP2x1r_7p9hd8wQjQYsxt7wwfqWgfEKEW5LQ_9bOc9J_WSfkKEtALS1bVcw-FZiJ1OzDmxPUc_4tW9AkXnfBKvVP7t5a1-r0BGlxDicnhVelQ995_EnBdtJboAc8LvJ5IssDxtUdC7ZKMscsWht0h1XWMUuiUCIaPG2PwliKYJrRURSiA7tjn5vUTo_96iMrzWz02dEmsJIBRLL_J8ddYIYaVpjJ1R3-Arhkr4wiwb9dfJaHsitLucyWhvdDuVWY8NXr3EYhoXr9FIeKG6X0hB78Td-29VUw-Y3v9usvgOBdYwUUP352teABDs1ksUTbyq-WFLYi0myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 14:21:26</div>
<hr>

<div class="tg-post" id="msg-661754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513861ce4.mp4?token=UaagAm5NroixkOHJmgrj7IpUiO5F_tZVw4GM1gtD_sZvfuxEQNsiXh_Ul9DMOlNJ9dH0MqXz3zHIe7IG8DnO30x25E69uVrOtMdRNVELVxUQ1IQ5jvIw5kYiYNfcpoT_u13gJnLkMhNR0wLIczD40UHjTsoMWEkXziymw2Civ_O_pBqITVFj2xdM9yPvSOC5aQqdlTAKzManIIhK4UhXJykaqm1i_20lUEexdjbcJa_W4r3NC94UDJBouLtgSDQLfMq4o03P3vVo6tsF0BnHW1TcyqJ-9mAIhk8Ns-DfgD5DnlEOzqeSJlfwFjDyFMAQ5SnLTP0bBYjIDn54FoGhKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513861ce4.mp4?token=UaagAm5NroixkOHJmgrj7IpUiO5F_tZVw4GM1gtD_sZvfuxEQNsiXh_Ul9DMOlNJ9dH0MqXz3zHIe7IG8DnO30x25E69uVrOtMdRNVELVxUQ1IQ5jvIw5kYiYNfcpoT_u13gJnLkMhNR0wLIczD40UHjTsoMWEkXziymw2Civ_O_pBqITVFj2xdM9yPvSOC5aQqdlTAKzManIIhK4UhXJykaqm1i_20lUEexdjbcJa_W4r3NC94UDJBouLtgSDQLfMq4o03P3vVo6tsF0BnHW1TcyqJ-9mAIhk8Ns-DfgD5DnlEOzqeSJlfwFjDyFMAQ5SnLTP0bBYjIDn54FoGhKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشجوی ۱۹ ساله‌ای که با ۲۰ دلار، ۵۵۰ هزار دلار درآمد کسب کرد
🔹
دانشجوی ۱۹ ساله چینی با کمک Claude، تنها با ۲۰ دلار و در یک ماه، رادار هوشمند ساخت؛ سیستمی که سرعت خودرو را تشخیص می‌دهد، ویدیو ثبت می‌کند، پلاک را می‌خواند و جریمه را خودکار ارسال می‌کند.
او این ایده را به دولت هنگ‌کنگ ارائه داد و با قرارداد ۵۵۰ هزار دلاری بیرون آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/661754" target="_blank">📅 14:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ریزش ۳۴ هزار واحدی شاخص بورس
🔹
تخفیف ۲۰ درصدی قبوض آب برای مشترکان کم‌مصرف
🔹
تشکیل ۴هزار پرونده اغتشاشات دی ماه در اصفهان
🔹
رسانه‌های عبری: نتانیاهو به باری سنگین برای اسرائیل تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/akhbarefori/661753" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661752">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پزشکیان: چرا مردم به خرید طلا و ارز روی می‌آورند؟ به این دلیل که پول خود را در بانک می‌گذارند، اما پولی که ۶ ماه یا یک سال بعد دریافت می‌کنند، دیگر همان ارزش گذشته را ندارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/661752" target="_blank">📅 14:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پزشکیان: ادامه جنگ به نفع هیچ فرد یا گروهی نیست
🔹
بر اساس همه تحقیقاتی که در جهان انجام شده است، هر جنگی موجب اختلال در رشد، توسعه اقتصادی و اجتماعی و افزایش فقر و بیکاری می‌شود.
🔹
این سخن به معنای ترس از جنگ نیست. ارتش، سپاه، نیروهای هوافضا و مردم ما نشان دادند که با قدرت در برابر تجاوز ایستادگی می‌کنند و اگر جنگ ادامه پیدا می‌کرد، با قدرت مقاومت می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/661751" target="_blank">📅 14:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661750">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پزشکیان: صدا و سیما نیز باید ملاحظات لازم را رعایت کند و مراقب باشد اجازه داده نشود تلاش‌هایی که در حال انجام است، با طرح مطالب یا حضور در تریبون‌ها خدشه‌دار شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/661750" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ویکم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای باقر حسین‌زاده که به وجود خداوند بی‌اعتقاد بوده و به خاطر اعتیاد و در حال مصرف مواد به ناگاه روح از جسم به طور سخت و وحشتناکی جدا و در آتش برزخ می‌سوزد و خاکستر شدن تمام سلول‌های بدن را درک می‌کند و با التماس به درگاه خداوند و ارادت قلبی به امام حسین(ع) در طول زندگی توسط اشاره‌ای از جانب اهل بیت به جسم باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: باقر حسین‌زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/661749" target="_blank">📅 14:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661748">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e342b75637.mp4?token=A_syqA5qxRyIVuQ2RqR3TGzZTJkuBStubkSuEKHjMUtiPr7qnL1G7w9LrMgsa8EKhK8clQfD90OWkAGL4ZMxYFA2T2-OGJPHBEd2_XRxwz53y83-kRkOuc7z6A1_xghTOdi2Jyn3P36O2wamzlxevK5KMlLsQNGk2ZkqyGBkwOkA34XkFsWPcGI12jcVu8gLUNQc8-MTs6ytQf2NKNOTV4l8Jc_2A9pj0HL-1ZPdBVR9rvfnTi6PPL_KlwWoBjabPTq_tWpo1JDN622O2IGWGxWEvQ18YzBPE7JHb8mx9PYadQvnP6vDzjSEECnN4HL0-qwWjNi-6KVS8dXCtrMqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e342b75637.mp4?token=A_syqA5qxRyIVuQ2RqR3TGzZTJkuBStubkSuEKHjMUtiPr7qnL1G7w9LrMgsa8EKhK8clQfD90OWkAGL4ZMxYFA2T2-OGJPHBEd2_XRxwz53y83-kRkOuc7z6A1_xghTOdi2Jyn3P36O2wamzlxevK5KMlLsQNGk2ZkqyGBkwOkA34XkFsWPcGI12jcVu8gLUNQc8-MTs6ytQf2NKNOTV4l8Jc_2A9pj0HL-1ZPdBVR9rvfnTi6PPL_KlwWoBjabPTq_tWpo1JDN622O2IGWGxWEvQ18YzBPE7JHb8mx9PYadQvnP6vDzjSEECnN4HL0-qwWjNi-6KVS8dXCtrMqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/661748" target="_blank">📅 14:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSY69YjRktOubaKeA1HD7z2DJGUZhyn_aejW4EQ-35DidiXWP0xi3O8hHzZVrENpWmnW54yvDMYq4gDbdfiKfIOFYQAg0nUFkZFRh1ftyFN24u2wkYpzLBs9FN_H4iHnsoUjhZc4Cgr1TmxQL63hv58uiJs4CmnGVC5SPgA8EC1g3fceIArfeKQcMp67GT-Gk_lIiEPLlHWCNgJ7WQeakxBujCnjml_jER_KNJS3sp0KSiY1D2ZKnP3g4qpEqwaboTr0-I43o38QRcN1tgbxanV1ZFobNWD02KKEsLYAq2rAZ78p02rmNnRQc2z7TYl9str2MbCNKpDay-DrAnQQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ خرداد ۱۴۰۵؛ ساعت ۱۳:۰۵
🔹
قیمت دلار امروز با کاهش ۲ هزار تومانی نسبت به روز گذشته به ۱۵۹ هزار تومان رسید؛ در حالی که این ارز روز قبل در سطح ۱۶۱ هزار تومان بسته شده بود.
🔹
کاهش قیمت دلار همزمان با سفر هیات ایرانی به سوئیس برای مذاکره با مقامات آمریکایی رخ داد و امیدواری‌ها نسبت به پیشرفت گفت‌وگوها را افزایش داد.
🔹
در همین حال آتش‌بس در لبنان نیز تا حدی از تنش‌های منطقه‌ای کاسته و فضای روانی بازار ارز را کاهشی کرده است.
🔹
با این حال، به دلیل تردید معامله‌گران نسبت به نتیجه مذاکرات، افت قیمت‌ها محدود مانده و یورو نیز با کاهش هزار تومانی به ۱۸۵ هزار تومان رسیده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/661747" target="_blank">📅 14:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhsYiY0u1t3QxabZKtH9ULHTsQzaXSV5pD3q_wFjxIHDYH_HkRtRylVvn50oBYBYzWGMXjcJyFfFvSFuA-2GMDW31cfkBiW8o5BMUX9ntx-YuMaNnnHxREaPZ7Xhl2Aps-_4xboeflWLAFei4keiZlGflCXfoxYL7S6GQuJn5orVEvw59NNc6MB3pw6N2dSHVtUh7JsVusB5mkXlMWXm0ZPEIgwHzwS0lTDYPUeNhvCvCRZsvUGCIzQ8CmixK0gSiTpsBdkulKg99i73_yhqfM8bOVy4GRzUAU1f3JR2ZHgrTX7h_9ffktTyhkw9ZdWwagYFUcbSqWVs3p5r5c-mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تورم» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/661746" target="_blank">📅 14:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12443b818.mp4?token=IUwGFonb6SP7pHbcYvlkcwm8hCPvSIAey3zYi0i641RwnilawPNzcozgSGy2on1wH9y7JyK-XJ97XvsgJiqiv6Hrkd1wJI-5JZMX3WhZggkTP77CIkkWWOkDd6yLAgs7iR2th3NJSaIi9I5oZouu6yuIe_AJ53iHrab4AJT4Ces8O1tZBY8ClMcSYpJxnAOAEfd5QucWusgEjo8Dw_18uLVeJ7ANhLZzGPxnLFEi_7OBK0qvLxbgVTTOUoJoNYrSahs36MsM3PPynP7_zRMLiscmGgdhYlI7m636B4FVxxPE2ZLfC31dbuuoDyBj2fncpuiEv2cbrUE-X-fHoD51cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12443b818.mp4?token=IUwGFonb6SP7pHbcYvlkcwm8hCPvSIAey3zYi0i641RwnilawPNzcozgSGy2on1wH9y7JyK-XJ97XvsgJiqiv6Hrkd1wJI-5JZMX3WhZggkTP77CIkkWWOkDd6yLAgs7iR2th3NJSaIi9I5oZouu6yuIe_AJ53iHrab4AJT4Ces8O1tZBY8ClMcSYpJxnAOAEfd5QucWusgEjo8Dw_18uLVeJ7ANhLZzGPxnLFEi_7OBK0qvLxbgVTTOUoJoNYrSahs36MsM3PPynP7_zRMLiscmGgdhYlI7m636B4FVxxPE2ZLfC31dbuuoDyBj2fncpuiEv2cbrUE-X-fHoD51cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماس تلفنی، دعای خیر و آرزوی موفیقت خانواده شهید میکائیل میردورقی از شهدای دانش آموز مدرسه شجره طیبه برای قالیباف رئیس تیم مذاکره کننده ایرانی در ژنو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/661745" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
زمان مصاحبه‌های دکتری ۱۴۰۵ به هفته پایانی تیرماه موکول شد
سازمان سنجش:
🔹
به‌منظور فراهم شدن زمینه حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، زمان مصاحبه داوطلبانی که پیش‌تر برای بازه زمانی ۱۳ تا ۱۷ تیر برنامه‌ریزی شده بود، به هفته بعد و در فاصله ۲۰ تا ۲۴ تیر منتقل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/661744" target="_blank">📅 13:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0-N_M4-dmmXstowERLBT2W4feedNtOoJpOUL_AJYMxNtGUC6seJ7tAHHHjVUKmP6rV83WUAB7yGYd-U-g9im0JArNieingyrYURMoV8w7WZNG12S8I653zdipsz9DmY4ozF8PBHitqcisSBByBJ0xjAvh--aN4cyMJENUiTKGOxFJXbko3zh_unGb2fwlSlpbJ301-cfUruXtAp6y2DVr5prH8dT8-eIP66EpcGjdldvORfxd9yHGdQytcUs04EtYPmSxgATqc1sQScQRcYHwNQvWwIA7C1KP6e0Tcsogud020JCayUtsfcj1VlcrmCe8DpLpzF0sXoVwWT-32jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام ایگنازیو کاسیس وزیر امور خارجه سوئیس پس از دیدار با عراقچی
🔹
جناب عراقچی به سوئیس خوش آمدید.
🔹
در نشست دریاچه لوسرن، ما چارچوبی برای گفت‌وگو و تبادل نظر فراهم می‌کنیم.
🔹
در شرایطی دشوار و پیچیده، رابطه مبتنی بر اعتماد میان سوئیس و ایران، همچنان در خدمت دیپلماسی و در راستای صلح و امنیت در خاورمیانه قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/661743" target="_blank">📅 13:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
پزشکیان: در شورای‌عالی امنیت ملی تقریباً همه اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/661742" target="_blank">📅 13:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
پزشکیان:هر پیامی که بوی تفرقه و اختلاف بدهد، در جهت راهبردهایی است که نتانیاهو و سازمان سیا دنبال می‌کنند
🔹
اگر قرار باشد بر اساس نیت‌ها و سخنان گروهی در کشور شقاق ایجاد کنیم، دیگر نیازی به اسرائیل و آمریکا نخواهد بود و خودمان کشور را نابود خواهیم کرد.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/661741" target="_blank">📅 13:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661740">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پزشکیان: قاعده تغییر کرده است
🔹
پیش از این می‌گفتند باید درباره موشک‌های ایران نیز مذاکره شود؛ اما اکنون می‌گویند همان‌گونه که کشورهای دیگر موشک دارند، ایران نیز باید موشک بالستیک داشته باشد.
🔹
اگر طرح‌ها و راهبردهایی را که نتانیاهو و سازمان سیا تدوین می‌کنند،…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/661740" target="_blank">📅 13:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پزشکیان: در همین مدت کوتاه توانستیم بخشی از اعتبارات و منابع خود را بازگردانیم و اقدامات متعددی انجام دهیم
🔹
برخی موضوعات پیش از این، مورد تفاهم قرار گرفته بود و در همان چارچوب پیگیری خواهد شد؛ اما از حق غنی‌سازی خود صرف‌نظر نخواهیم کرد و طرف مقابل نیز ناچار…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/661739" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پزشکیان: امیدوارم مجموعه افرادی که در مذاکرات فعالیت می‌کنند، از جمله برادرم آقای دکتر قالیباف، آقای دکتر عراقچی و تیمی که از بانک مرکزی در این گفت‌وگوها حضور یافته‌اند، بتوانند مسیر را با موفقیت ادامه دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/661738" target="_blank">📅 13:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پزشکیان: پول داریم، علم داریم، پشتوانه داریم؛ ادعاهایی که می کردیم را باید عمل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/661737" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HY2UhmeSyefG58mMOniu0UIehkjgzMjrdneHGVLDiqSp7K2dru_K3oa6KFHZUK1ZS4wMVVP0Lgn5EEj2oJrkbXl6UB8wfHXjSnn_VVaVbaTw-89UDDZDhZFeH0zA6cx6-AYju1Z6HcPDXmFch1jiHBohhBXKayttIaNAGv6LbyugHBnXOaLQC1QD9WkZUgdSQgUD_WfhKr07g7TwmnDDG4X9zlBU2k3VQisjbw8dt-nEpxmxQGS3S-c5QHgw0QmPqc1d4ZuoPsYkc8r2ebIUJX3tPLvDlEDuSIbrGbcIBLd0UCGNQOZ6ty68lVXNJAPp18a1yJzWXi4pkzQn7UaM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هواداران ژاپن بار دیگر با پاکسازی ورزشگاه تحسین جهان را برانگیختند
🔹
هواداران ژاپنی پس از پیروزی پرگل تیم ملی کشورشان مقابل تونس در جام جهانی، مانند همیشه پس از پایان مسابقه در ورزشگاه ماندند و زباله‌های اطراف خود را جمع‌آوری کردند. این اقدام که بخشی از فرهنگ…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/661736" target="_blank">📅 13:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661735">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5654ba754.mp4?token=O-VQZySRYsGpwPLd_9965wkAdlr9Hp2s3bY7tg_ymJ_iD_xcl5iNbTfdUDdwBrWXYeBW8jiMwmVmh7arkZyXNZgkMAXRXJgj839p6aCDcLBHUVlP1reaz6LgN54ZJfa_MZk8kk108YLCDwGzDQwrE_hRw45Wvn29YIfFVDdjUliREYamiBQEcRPgnsHC2Hw10Hink-WyJe7wG2_HIaIj9JN_aBehlI_gso4rCEH9Zi8oq2TncHHuDJqE_DgbwoqN2rWolM9IFm-k9KdMprWxOJMAuoR8b-tgLl0HsuhIjq9xKC6_7p0Hkr5n1BUz-VkD7ie0nbXKo493dPnr6vKSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5654ba754.mp4?token=O-VQZySRYsGpwPLd_9965wkAdlr9Hp2s3bY7tg_ymJ_iD_xcl5iNbTfdUDdwBrWXYeBW8jiMwmVmh7arkZyXNZgkMAXRXJgj839p6aCDcLBHUVlP1reaz6LgN54ZJfa_MZk8kk108YLCDwGzDQwrE_hRw45Wvn29YIfFVDdjUliREYamiBQEcRPgnsHC2Hw10Hink-WyJe7wG2_HIaIj9JN_aBehlI_gso4rCEH9Zi8oq2TncHHuDJqE_DgbwoqN2rWolM9IFm-k9KdMprWxOJMAuoR8b-tgLl0HsuhIjq9xKC6_7p0Hkr5n1BUz-VkD7ie0nbXKo493dPnr6vKSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی سهمگین در مجتمع بین‌المللی خودرو در چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661735" target="_blank">📅 13:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661734">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCbhnMNBjkdW7LaMufx1ElWAY1pw1eMCr1aXGVeGB3yRxGlTe31KwtDyeMq6QVSULFWpXYt6c1vKxXwS0q6_u3mg6z7fjKUsIaJuWhxh-wIUv-loNWf-SavFaXkkRRzz1ZNmsH38cvq8A9h5W6jDk_HUYkvPkK9OzUklG8_POVpj3UmSSxxZQVYXZH89UNZqqlnvhLNdgJrVMXDi-Ov0ue03hRXNNuDUODx_CtGQTOecTY5HNl3gQNJF-tYtA1dtD8GxbBB6o-pw25ej8OaNFHt85kbIX3GHp753aJqU-ApmL6RJE0FUkdNQbkU-JynOuiIsJ7Z2BFBSQ70qniSCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی لبنانی‌ها از ایران؛ از وفاداری شما متشکریم
🔹
مردم لبنان با نصب پلاکارد در مسیر فرودگاه بیروت، از ایران به‌دلیل حمایت و تأکید بر آتش‌بس در جبهه‌ها قدردانی کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661734" target="_blank">📅 13:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqSyFhtIOo0Ji9LVHUCPQUD3uoxSHigPKWTYOTfrzI41f66MY_sJm7PoSF61C6AnDItBO7gOfjrl_cB_yWcg-0Tq-BSh0DQB79XRMAXDC4XgxHJzfHzMMiSU4MvAObQAkFI3JC-6xunDAsU8UNHj7xiNsiM7NjuzUZfe_112uqor4ZeVk0Kagr1V7iZLt98DnEauxd7IDKkmy1Nf99Wn6JE_pUPeE3-KS_S3n-0O9m4xWWfDxuhVX6PxmYs0x3x1_PqJ-VquL8aqTUY5YRmDp1m6kGOkaKEP-YlCLCEan6QkWkUI_gq-7Xgcl2w6jX-gDvVCBGUI9X0TURlRR-cZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: دستور نخست هیأت مذاکره در سوئیس پایان تجاوز در لبنان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661733" target="_blank">📅 13:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661732">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
جلسه با میانجی قطری و پس از آن با پاکستان در سوئیس
🔹
«بقایی»سخنگوی وزارت امور خارجه: عصر امروز نشست چهارجانبه ایران آمریکا قطر و پاکستان برگزار می شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661732" target="_blank">📅 13:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661731">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmkHhBHvwXkpmPgxQPlPe2RIMYrG564ffyTVd26qy4H9qSIZoR4rGfNWiURl5ds0h8J2k_WhwGrmWhBRBFrGUrm6Trbl8DaZM3dG7b5JRip5k2vfyJ7aN6Uqg74yaFjjDQ91u-FQQXbYG1TVPvcq2lzDSbCmGFwYMFhFyrOqYrVedoXLG02mDvsOt-YlBjyaNEUF2oEwUHt0-Rj5gqh5XARrqXsY-X_rO3DGiHcpazr2njcgZBoe5_y8PZ2zdOzuJmbSSApSFrL2kSSNuVe_cNi1PZspvcQNR0ef6ESduJGLLN9novA6mMHb6l_K8nsOO3sXI7Y3gebE8avFk4Ndsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی هیئت مذاکره‌کننده: ایران مصمم است روند اجرای تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661731" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661730">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940e5d97cb.mp4?token=Lx8Jquhf4EeGcT----Dew_k7rx7eYdfUlkU_UHvUMPrSiS_sBuyIgfQEc-FzRousq6ycaMVXvsx-h-stzSZ_qPLm_efBuVN14cenrORZbcCp_dsx3CFzRoZdXF9QYjkQ8BN2LXijitZUu8YUutVZDAJNb3dbj1yfQrWCEqfYr4EHFcL5If3irOwCkdOPANr2BCMIIbGT9ksFVcQJlbCt7ytvuEkPRu9e9rAtuw3dHVSC_p8bYSLjI36L9cPadkuwuigYcetor4JpcW1W23jITA49Mpf1JXpmtKSVCJ7DgCs-z1s-l8d2Xbjan3VFsp2dexAzuEuewX_50YGI-xQqSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940e5d97cb.mp4?token=Lx8Jquhf4EeGcT----Dew_k7rx7eYdfUlkU_UHvUMPrSiS_sBuyIgfQEc-FzRousq6ycaMVXvsx-h-stzSZ_qPLm_efBuVN14cenrORZbcCp_dsx3CFzRoZdXF9QYjkQ8BN2LXijitZUu8YUutVZDAJNb3dbj1yfQrWCEqfYr4EHFcL5If3irOwCkdOPANr2BCMIIbGT9ksFVcQJlbCt7ytvuEkPRu9e9rAtuw3dHVSC_p8bYSLjI36L9cPadkuwuigYcetor4JpcW1W23jITA49Mpf1JXpmtKSVCJ7DgCs-z1s-l8d2Xbjan3VFsp2dexAzuEuewX_50YGI-xQqSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که مه‌لقا باقری برای تولدش در کنار سگش منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661730" target="_blank">📅 13:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661729">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e1446eb5.mp4?token=o2Ogpht4yoX3e8C5tcLVrgy_1TzEd32JGZsJKLVDcZ0PtPYjOa3o6YojJaR2wKa5H58oxRzywC5ubVkxknX2KU-VMJft-YS4Qd8CuMW1V5HEEWzipZcJXPTPd0FeagsGksVLcvlQeXPC5MapKDdS6-zdCzO4zHrsW0wNWyEmJJKfo-kABjoQz8OAMACHQgDBK1rqwvoMo4_xQujRoaTjS8tF-bcKgJqf11aDuTSPE7VD6WoA9mTafsdmOJMDkZAVoatDddKH5KhtTxg0ZiqZ04CTVStzsn3hURxzpGtSefElBacWRps83EyhoVdMUCgxUeO1ltdfly4Mczo1J9mBBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e1446eb5.mp4?token=o2Ogpht4yoX3e8C5tcLVrgy_1TzEd32JGZsJKLVDcZ0PtPYjOa3o6YojJaR2wKa5H58oxRzywC5ubVkxknX2KU-VMJft-YS4Qd8CuMW1V5HEEWzipZcJXPTPd0FeagsGksVLcvlQeXPC5MapKDdS6-zdCzO4zHrsW0wNWyEmJJKfo-kABjoQz8OAMACHQgDBK1rqwvoMo4_xQujRoaTjS8tF-bcKgJqf11aDuTSPE7VD6WoA9mTafsdmOJMDkZAVoatDddKH5KhtTxg0ZiqZ04CTVStzsn3hURxzpGtSefElBacWRps83EyhoVdMUCgxUeO1ltdfly4Mczo1J9mBBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آرژانتین از مجسمه ۲۶ متری مسی به وزن ۵۰ تن رونمایی کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661729" target="_blank">📅 13:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661728">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ec10ba03.mp4?token=KYoLsizdyqJLII-rwt0v6CgJMOdy6uWR-6HqCqfyUU1xMQz4N0gM2SsffcTWLNR5eOzQmf4Eua1pelqmdV-8KqwiuQrrBRNgZr_0gezSZcp8qu5YnjXF1WMjKrHPlLa_AUMv_2Ri_RwRCe7r2wmqe3RRHVZkn7BPY5BPE6hVARiGU_yCSzuNaWBcRireUJDrSOEMvJ649ER1iP2M2UJgKP0ZsAoJWgS4nuPaFTUPYu-iwHsieFfw8ks5lA6i6wIEowSUEdoa2UPdvCgvBBxY2vBpQNswoqUnizL9Q6PnKVGJvAe1Z2H0ZeLzNW2Lt7zq_JqsfTlwq40DFjbLp-DT5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ec10ba03.mp4?token=KYoLsizdyqJLII-rwt0v6CgJMOdy6uWR-6HqCqfyUU1xMQz4N0gM2SsffcTWLNR5eOzQmf4Eua1pelqmdV-8KqwiuQrrBRNgZr_0gezSZcp8qu5YnjXF1WMjKrHPlLa_AUMv_2Ri_RwRCe7r2wmqe3RRHVZkn7BPY5BPE6hVARiGU_yCSzuNaWBcRireUJDrSOEMvJ649ER1iP2M2UJgKP0ZsAoJWgS4nuPaFTUPYu-iwHsieFfw8ks5lA6i6wIEowSUEdoa2UPdvCgvBBxY2vBpQNswoqUnizL9Q6PnKVGJvAe1Z2H0ZeLzNW2Lt7zq_JqsfTlwq40DFjbLp-DT5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلسه با میانجی قطری و پس از آن با پاکستان در سوئیس
🔹
«بقایی»سخنگوی وزارت امور خارجه: عصر امروز نشست چهارجانبه ایران آمریکا قطر و پاکستان برگزار می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661728" target="_blank">📅 13:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661727">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b2ab19bf.mp4?token=v6Aj6WwsdtBAsm6WdlEodlVvDdKrWdi8N_ZdpL1aWrXY34ryNEPcRuuRXpGLPW2LmsQItHMICq-xvvDIl79LPUwwo7vo5r2JcJsfQdBXup4WS8V90rE-PK3aDBIz5YKBmBzay7-3jz58xhxmlfjYGXXW9GKMtBDSM9FU_6fJBqUf6d1mUCcishoZZ_V-KT0dtqAEPb-vZrHdU_VcgrpM7Pb3Z2l2n8Tk2xbgwdiCyEyc8809pDJV2IX367yOj7qDBU5coQQCmH6cn29Rs3pC8eRk637cfYwnuRo3kCMk1Sg09BeHGS7gx0GwVLj9bDkUxrL0FRKNWPzK4CcENEyGWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b2ab19bf.mp4?token=v6Aj6WwsdtBAsm6WdlEodlVvDdKrWdi8N_ZdpL1aWrXY34ryNEPcRuuRXpGLPW2LmsQItHMICq-xvvDIl79LPUwwo7vo5r2JcJsfQdBXup4WS8V90rE-PK3aDBIz5YKBmBzay7-3jz58xhxmlfjYGXXW9GKMtBDSM9FU_6fJBqUf6d1mUCcishoZZ_V-KT0dtqAEPb-vZrHdU_VcgrpM7Pb3Z2l2n8Tk2xbgwdiCyEyc8809pDJV2IX367yOj7qDBU5coQQCmH6cn29Rs3pC8eRk637cfYwnuRo3kCMk1Sg09BeHGS7gx0GwVLj9bDkUxrL0FRKNWPzK4CcENEyGWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما ۲۰ میلیون بشکه از «نفت خودمان» را دادیم به هوافضای سپاه تا بتواند بجنگد/ در شعام فرماندهان قرارگاه، ارتش و سپاه تفاهم را امضا کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661727" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661726">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تامین اجتماعی: با توجه به اختلالات و محدودیت‌های اخیر پیش‌آمده در تعدادی از بانک‌های عامل، بر اساس پیگیری‌های سازمان و اعلام بانک‌ها، ممکن است بخشی از واریزی‌های بازنشستگان به صبح فردا (دوشنبه ۱ تیر) موکول شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/661726" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661725">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZetD290ymtyT-_WK0c-agVHvm0UDgIJ2TUJ3IMrruigGrcu4bV4risx4XYYBKH__yjsRrw7c3ON_pi6U_GsvAyMKSeVHaPU0pU5In8_PLggK-Y8_gj2TY5g3iPd1MwL3wP94yHxBcqY-bj9ge8GR5480jgGf6J-m0OGDgkoVokECZYf5RK_2Xev_GMpvOK1X2u2Fm-TyXyEag4nEyLj3Ha2psr7_dZadyRR8sgGpYGW51ccCMgZMqlxDI1z9GUw1SwWJG9AO5pDGkgJQ7viMEPY5RCS32L26_GDxknH5-f5iBD5QiCVwRuZP1KO239IvNyJpJCg2cL68_i5bRl15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی مانوئل نویر در جام جهانی؛ بیشترین حضور یک دروازه‌بان در تاریخ
🔹
مانوئل نویر با ثبت ۲۱ بازی در جام جهانی، به طور رسمی رکورددار بیشترین تعداد حضور یک دروازه‌بان در تاریخ این مسابقات شد و از هوگو لیوریس (۲۰ بازی) پیشی گرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661725" target="_blank">📅 13:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661724">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
شهباز شریف نخست وزیر پاکستان با ونس معاون رییس جمهور امریکا، در حضور کوشنر، ویتکوف و فرمانده ارتش پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661724" target="_blank">📅 13:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661723">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796fe75a01.mp4?token=snjBL7acWSwS_FcI7b7l6xnEyQkoLLS46z_dCQepIrIgD7W-UF8J0ZNBJilSXnAAcbNU4o5gg5BzWV_YW1MxGAV18ma2v-3LbpL--QAUVMA4tfj7Kqmry_dOeP4uRI10I5PNRkW8xGE9Mp_Aion7Ipkd1bQJvKcJEflZwS2KPtY5Tu3O4WZBkWFFCSAyXAIjhSAxYEc76OGGPKUkMtuKUDmW-PnzPcqQF93YL0dEr4g8bi2dAcCES9jIsck0b8Atul71MWBxvbar0_YSVk7AowT0kV3VHeBes72egYr4yHfzFRokulsumICvnedbBvNzSkwMKZd9egHDjt5Xq2uumA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796fe75a01.mp4?token=snjBL7acWSwS_FcI7b7l6xnEyQkoLLS46z_dCQepIrIgD7W-UF8J0ZNBJilSXnAAcbNU4o5gg5BzWV_YW1MxGAV18ma2v-3LbpL--QAUVMA4tfj7Kqmry_dOeP4uRI10I5PNRkW8xGE9Mp_Aion7Ipkd1bQJvKcJEflZwS2KPtY5Tu3O4WZBkWFFCSAyXAIjhSAxYEc76OGGPKUkMtuKUDmW-PnzPcqQF93YL0dEr4g8bi2dAcCES9jIsck0b8Atul71MWBxvbar0_YSVk7AowT0kV3VHeBes72egYr4yHfzFRokulsumICvnedbBvNzSkwMKZd9egHDjt5Xq2uumA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: اگر آمریکا بدعهدی کند، ما هم تفاهم را نقض می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661723" target="_blank">📅 13:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661722">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQNNETQyXQR3NzzsqSr4q8qFoZrSmhf4L3j8MwlIluz0kCj7bHhsSZ5DhIOZCy76k9L18gOHlZwEzcMm3OvaZ3W1Q61D6iFSZluMIwPxR1Qy34bnvO0060E31QkTuSK5hkTPR9vRxyyW_brn5DzUHUDZVqQIg52fQn63bRArfF9ACdHo8l1HltwKgTkePfkFpk7WzG1kSeSb09BZJug59z9mb3RvmkkphuMsMda9-t5O6GiInD99NwtTx9cVeKhRqhv7wSdHAQ4dV5DNKqxf54hmnaubmJZRqn_DMck_WbVUQKq3FPH9Odq-CFmjND0aeO_hz8S3xEJgT_FYP0ybDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار گروسی با وزیر خارجه سوئیس در بورگن اشتوک
مدیرکل آژانس بین‌المللی انرژی اتمی:
🔹
در بورگن اشتوک با وزیر امور خارجه سوئیس ملاقات کردم تا تحولات اخیر در مورد ایران، مسیر پیش رو و نقش مهم آژانس را بررسی کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/661722" target="_blank">📅 13:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سربازان برای شرکت درمراسم اربعین ازطریق یگان خدمتی اقدام کنند
سازمان وظیفه عمومی فراجا:
🔹
کارکنان وظیفه حین خدمت که قصد زیارت عتبات عالیات را از اول محرم تا پایان صفر در بازه زمانی( ۱۴۰۵/۰۳/۲۶تا ۱۴۰۵/۰۵/۲۲) بویژه ایام اربعین حسینی را دارند ،می بایست برای دریافت مجوز خروج از کشور از طریق واحدهای نیروی انسانی یگان خدمتی خود اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661721" target="_blank">📅 13:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ea3749ae.mp4?token=iTqal26w3V9f7M09qH29JwRTEkGInSyExsRffYyiRcmNN74stM_aEttRKRvQEIaDJ2ZGXyBYW7mcea1IVR2X2aDhJJx3_noD_olavVBK7p9MnZltFTfTBOAXBGLUr9FTgrj6CVXIuajweGI--41c_Mx2dwKvJI7rmNCkXhKQyYr4A84jfkjGphFmajBmJBV0PGJKIdWCP0bse3HCWIUQIoJhkZpp795uYcF_7L8GbHIG792uYe94ne3lEvjr41YfLRFxs6-8QPIHLN6iS2gbdEVvC7CTbJhfNvXj1Mf6HMM1bz8oYk2sHF-xvbA1-momYIm5m7wMwVZ95S3GA3ehEQZE5qINl5a2tDJw0DLKlSqDA3k-BNE83TbNR3G4coMnvAdza8o8Jl9js0uGd7ldPUKz4p0R0M99AJvs2gw7rm_SjEDm_kUl0jzX3Jj6gqTXmrJgZudjw582qulugM5n32vIAgkk7QTs-bsE--06uZ4AkS0Qq5uVBHmL6-_cWiYecxbbnEDFCAb2UDgPdgH4ZhksLCl1WMfSYFKqDxGiYKur0HBtMbtMjqCiqPmY4heFnt50OxNxoiGQETeWcLM3Q9Eza1ePT8Jl8SpUcsb1QsOcrmZlxB0Q44okSh4VuD_6PKUUxeKXultMxHcAct5y3FuttBcoCrhHLBiwnUF0muI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ea3749ae.mp4?token=iTqal26w3V9f7M09qH29JwRTEkGInSyExsRffYyiRcmNN74stM_aEttRKRvQEIaDJ2ZGXyBYW7mcea1IVR2X2aDhJJx3_noD_olavVBK7p9MnZltFTfTBOAXBGLUr9FTgrj6CVXIuajweGI--41c_Mx2dwKvJI7rmNCkXhKQyYr4A84jfkjGphFmajBmJBV0PGJKIdWCP0bse3HCWIUQIoJhkZpp795uYcF_7L8GbHIG792uYe94ne3lEvjr41YfLRFxs6-8QPIHLN6iS2gbdEVvC7CTbJhfNvXj1Mf6HMM1bz8oYk2sHF-xvbA1-momYIm5m7wMwVZ95S3GA3ehEQZE5qINl5a2tDJw0DLKlSqDA3k-BNE83TbNR3G4coMnvAdza8o8Jl9js0uGd7ldPUKz4p0R0M99AJvs2gw7rm_SjEDm_kUl0jzX3Jj6gqTXmrJgZudjw582qulugM5n32vIAgkk7QTs-bsE--06uZ4AkS0Qq5uVBHmL6-_cWiYecxbbnEDFCAb2UDgPdgH4ZhksLCl1WMfSYFKqDxGiYKur0HBtMbtMjqCiqPmY4heFnt50OxNxoiGQETeWcLM3Q9Eza1ePT8Jl8SpUcsb1QsOcrmZlxB0Q44okSh4VuD_6PKUUxeKXultMxHcAct5y3FuttBcoCrhHLBiwnUF0muI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: وحدت از بین برود دیگر هر حرفی بزنیم به جایی نمی‌رسد
🔹
مهم ترین مولفه ما وحدت ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661720" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دیدار و رایزنی محمد بن عبدالرحمن آل‌ثانی نخست وزیر قطر با قالیباف، رئیس هیئت مذاکره کننده کشور در هتل بورگن اشتوک سوئیس
🔹
پیگیری اجرای بندهای تفاهم از جمله بند ۱ و ۱۱ یعنی توقف جنگ در همه جبهه‌ها به خصوص لبنان و آزادسازی ۱۲ میلیارد دلار از اموال بلوکه شده…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/661719" target="_blank">📅 13:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661718">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzIkwAxryFQ5Z6hHHU3DqFY6ny0yQ9YVRF0I1JyjXhnsDV8nA1UhE_16k8q4J3boblEdsjEtw_KeKDov2X2qXHCbta42pCi5cBC18K2aZfceyXgYmiSViCTVag3frKR-TC57FstcfRya8mWWkMY9VPkPUEeFmPlWNdLh0roFb1NKuuLXjcF2sUxo2Sxt4GOeHsml4p8jV8Y6WpXviZHoUH6hE6ukywVYVwCfjnqXHMJWOEfBF78d7_vyQLWFmPogw_pRvhCsM5zywKDmfozRG1wp6NHuYHrYSbuMH7Opa05QJEkoTKwVXItzrPxh_3pBUiu_Aai2_HWP9ISG-XYq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرادو ۲۰۲۵ در امارات ۵۰ هزار دلار است، در ایران ۴۳میلیارد تومان
🔹
حتی اگر دلار را ۱۸۰ هزار تومان در نظر بگیریم و ضرب در ۴ بکنیم هم به قیمت ۳۸ الی ۴۳ میلیاردی این خودرو در ایران نمیرسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/661718" target="_blank">📅 13:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661717">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مودیان نگران نباشند؛ مهلت ارائه اظهارنامه‌های مالیاتی تمدید می‌شود
سازمان امور مالیاتی کشور:
🔹
درخواست تمدید مهلت ارایه اظهارنامه‌های مالیاتی اشخاص حقیقی و حقوقی به مراجع قانونی ذی‌صلاح ارائه شده و قطعا این مهلت تمدید خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/661717" target="_blank">📅 12:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_0PYKWhln0hn87HeDHnRJxq9xh7awR-38v50BsGYOqYjKrnrAyd_f2wFKJnSUZ36golK254b6hP_0kyquBQatSH2BXMO08AoArcO07WrGPM1eSxOgYkrndism9ao1fryqJabh4-GmiDe-FbCO6HhdyhBs-fBDs7MSHSNLDrEdwFVTJ0LKKzunEOGjbxnxDcKWR7NgEyW2EnSh6_ocXDTW73jwvaIorHf12eechyrNLWaII2_F9YlC0PSVQA0ivLJ7NVaFjARmA6tSkq2W7qN-x9tKmHvgNlyRMflHwKfpdP1IRgkLsB6FBsFW3pW3P83LbCxrkV99kvTjIaEPCcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هواداران ژاپن بار دیگر با پاکسازی ورزشگاه تحسین جهان را برانگیختند
🔹
هواداران ژاپنی پس از پیروزی پرگل تیم ملی کشورشان مقابل تونس در جام جهانی، مانند همیشه پس از پایان مسابقه در ورزشگاه ماندند و زباله‌های اطراف خود را جمع‌آوری کردند. این اقدام که بخشی از فرهنگ «گومی هیروی» در ژاپن است، نمادی از مسئولیت‌پذیری اجتماعی و احترام به فضاهای عمومی به شمار می‌رود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/661716" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3edb590.mp4?token=drXcR7PfjdWMB7WkB2hjk6k68m0Tcec3ju1DWPOwmqd1MG1xe360ARYsu8-woTZXbWkX7HahteTTSRbLCoslylvugbAXqMOAp1dPGtlCrXhTeObhItcuVAwhQ4MWgc4564J-xpXGXXvMwxpkklh6LTTmMf605-3RpLoWENVSPSxsWa0r3dJ8eXDYyJp6ie2N8JpVXSloNOXYsV45pTPkvMPrAcwHFrNWbO_GI9K45K2It0dUf7plh4hg1l1F5f-feX8m_FKdGhJ8dxY_XiWwsXOK3xMdjf4unU18FEMrMm_NBhj4admVQ7xBrEl6oVdBwQVQIFmS74yW8_z4SBdGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3edb590.mp4?token=drXcR7PfjdWMB7WkB2hjk6k68m0Tcec3ju1DWPOwmqd1MG1xe360ARYsu8-woTZXbWkX7HahteTTSRbLCoslylvugbAXqMOAp1dPGtlCrXhTeObhItcuVAwhQ4MWgc4564J-xpXGXXvMwxpkklh6LTTmMf605-3RpLoWENVSPSxsWa0r3dJ8eXDYyJp6ie2N8JpVXSloNOXYsV45pTPkvMPrAcwHFrNWbO_GI9K45K2It0dUf7plh4hg1l1F5f-feX8m_FKdGhJ8dxY_XiWwsXOK3xMdjf4unU18FEMrMm_NBhj4admVQ7xBrEl6oVdBwQVQIFmS74yW8_z4SBdGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در چین، ربات‌های انسان‌نما همراه با انسان‌ها در مسابقات قایق‌رانی اژدها شرکت کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/661714" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وزیر اقتصاد: مبلغ کالابرگ همه دهک‌ها افزایش نمی‌یابد و اولویت حمایت از دهک‌های پایین درآمدی‌است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661713" target="_blank">📅 12:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دیدار و رایزنی محمد بن عبدالرحمن آل‌ثانی نخست وزیر قطر با قالیباف، رئیس هیئت مذاکره کننده کشور در هتل بورگن اشتوک سوئیس
🔹
پیگیری اجرای بندهای تفاهم از جمله بند ۱ و ۱۱ یعنی توقف جنگ در همه جبهه‌ها به خصوص لبنان و آزادسازی ۱۲ میلیارد دلار از اموال بلوکه شده ایران و نیز ماده ۶ تفاهم مربوط به ۳۰۰ میلیارد دلار سرمایه گذاری موضوع بازسازی، دستور کار این نشست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661712" target="_blank">📅 12:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بقایی: امروز دو نشست در صبح و بعدازظهر داریم  سخنگوی وزارت امور خارجه:
🔹
قرار است یک جلسه یک روزه داشته باشیم. صبح دیدارهای دوجانبه با هیات‌های پاکستانی قطری به عنوان میانجی‌های این روند خواهیم داشت.
🔹
بعدازظهر هم نشست‌های چهار جانبه میان هیات‌های جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661711" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تصاویر دیگر از ورود هیأت جمهوری اسلامی ایران به سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/661710" target="_blank">📅 12:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCG3Q5w5GkInTGlykTTwhyRaYva8MztR7vdNdK6zLrkH69U9rQ1XVQTOsfBZkxFjcHYefdI_lPPpDrxvluE2HC-QkpzctF0fHSCSLwe2V7iw8ucGOBP2bAAHP-kLBcW3d5SHqCNi1JSp9piR7WEufAzZBMEHjUrwvxBKv78l7Zx2Yetjr7e-v8DR-8voi4fhrN8rbKUcsTKyosCaVM3Kz6f2XnwuO2uwKBIRoa4jo0kEJqxfWNh4e3wGdwRJDqcSty-JVjAeonwhMUon6qHmsg-PobeJRXmaI_8uZ8XkqYrG_knSuKhe1O-fx3WaJtjKPyalQfHIXHewDKJ_k1QeoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همسر نخست وزیر اسپانیا ممنوع‌الخروج شد
🔹
«بگونیا گومز» همسر پدرو سانچز، نخست وزیر اسپانیا پیش از این پس از دو سال تحقیق، به اختلاس، اعمال نفوذ، فساد در معاملات تجاری و سوء استفاده از بودجه متهم شده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661709" target="_blank">📅 12:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عارف: اهل جنگ نیستیم اما اگر جنگی به ما تحمیل شود خوب دفاع می‌کنیم و دشمن را گوشمالی می‌دهیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/661708" target="_blank">📅 12:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36bc56e00.mp4?token=jBhNE576q3QTKMCgLJVsLq3rvG60Oh7uj8OZ10MJ1nSC_YGStwVROUg9_MjDocmk6BTkys8yzfVGcE0UTc43JhR54i6YywYHDtD2ysdG0pOZPfNs1RmIs0syQIoSk6RzUHklNMgo5_X_EWKcKMHsZjo4oMzw2Pz7Tz61-lIpGEnRNqn5BlBBF4lA1uWoax-QG0yhFMNmE3-V5-dha2CmYSnitzIUIh-Sq1cRDqNK0e5vtx959Km-fC7XqOXDzEXxvXnOPpk1LheUzObiX3EeF0pI2TCuKGTcAbHiHYU8ageNh1lEzwqhzeifspSQ3dAnvfpKjNLthY0LxNmqOBx_uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36bc56e00.mp4?token=jBhNE576q3QTKMCgLJVsLq3rvG60Oh7uj8OZ10MJ1nSC_YGStwVROUg9_MjDocmk6BTkys8yzfVGcE0UTc43JhR54i6YywYHDtD2ysdG0pOZPfNs1RmIs0syQIoSk6RzUHklNMgo5_X_EWKcKMHsZjo4oMzw2Pz7Tz61-lIpGEnRNqn5BlBBF4lA1uWoax-QG0yhFMNmE3-V5-dha2CmYSnitzIUIh-Sq1cRDqNK0e5vtx959Km-fC7XqOXDzEXxvXnOPpk1LheUzObiX3EeF0pI2TCuKGTcAbHiHYU8ageNh1lEzwqhzeifspSQ3dAnvfpKjNLthY0LxNmqOBx_uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: اهل جنگ نیستیم اما اگر جنگی به ما تحمیل شود خوب دفاع می‌کنیم و دشمن را گوشمالی می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661707" target="_blank">📅 12:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
بقائی: آمریکا بند اول تفاهم را اجرا نکرد؛ توقف جنگ شرط ادامه مذاکرات است  سخنگوی وزارت خارجه:
🔹
در نشست چهارجانبه ایران، آمریکا، قطر و پاکستان، اجرای تعهدات آمریکا و توقف جنگ در همه جبهه‌ها، به‌ویژه لبنان، محور اصلی گفت‌وگوها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661706" target="_blank">📅 12:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emcG6__oaQLnLtoRcjNAuOm6HMbfFGSbl9NG8dKrv-3LtOmLJiZyr7yEjFNvQShWfKTAiBG_SHYOzLVy55nOvFjG0mqJVTOM1cMuFnMRmX1ZmfWtmputC077owm8tMuijzklw-nRpUlEs7kBlpIWIhDs1lXDTBNJqfpLOgPSChQWuSxzPOVnL9ihC2L8gNV9QwGLQnXEZVelQxIVcFHg5qx8x6FPPFVIrJCD_oQlODjCYs64ET-_pVs8aOniTU8rByztyZQOaNqgp2inFBV3hyBgA7Ts2G0AuE85GSVwTa2AqyYbFqVzJV6sAdaafd7CMZ7v2WluoyzdqoUCOBoIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای بازی امشب مقابل بلژیک با تصویری از بیرانوند و کورتوا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661705" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7tDxZuYB6ar7g7ig0QpEzS1JUMdlrOWcHEyLMMtvdPlckwVwVOoopVnJpVWPBgh6HICPWxfGbsct_nwHFP4oSgfdHHAledi4PANieMcg1Y9o5iakfSgr5BBqhnKTwUnBfYWmTo2QRJK4_CNiChHR1gcAV1_TRUIMhzvp346-6nzOKgYN4oLcitglw7fJLaFEv4pIBI-7VUdMk2uiHCNuzTBLb3UVSg1i3G3CL6RS-h7XqbavnfNFVBW_nPSIl7djR9xQntKPuw0CEAoY1lLqI6uQO-1sujiM2WjvjcRCYeA0q2_k62bT5zmtm7ZxjH9bEk6nq0Oe0zW1iyb6fLMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین دستمزد در بین سرمربیان جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661704" target="_blank">📅 12:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5857eb70e1.mp4?token=Qjmx2jduoEp8xqALz-_gLpsTxL0i2O6M5jjU4CeyhzYd9jQv805wFxZMtyMVZb0U6UT6FTR-gDwrlXO7x1ymUiGKpQiaVgFRYJ_NZ3EpUQS9VvA7yIotmoOq3z0U1z1NJ7HxJ5SUYVwQpv56_f7hiEu9qNI3VNPKIgZbHtuOL-oWHCPeUXZj4Ft2F1jNrzvKwJ43aQdq0OKkYN7FtYnbRAEhSoGn_GaASu0wtYKxCB_Ec8yZZMQnEitCiHCzgeGWsXG8-tS1WU9KC3_7lwE3vphUtWA9vO6towdcghzFSyxIXnynuIfGrwfGphCg5zTZgExpul2QGe6wmEHaPkHk4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5857eb70e1.mp4?token=Qjmx2jduoEp8xqALz-_gLpsTxL0i2O6M5jjU4CeyhzYd9jQv805wFxZMtyMVZb0U6UT6FTR-gDwrlXO7x1ymUiGKpQiaVgFRYJ_NZ3EpUQS9VvA7yIotmoOq3z0U1z1NJ7HxJ5SUYVwQpv56_f7hiEu9qNI3VNPKIgZbHtuOL-oWHCPeUXZj4Ft2F1jNrzvKwJ43aQdq0OKkYN7FtYnbRAEhSoGn_GaASu0wtYKxCB_Ec8yZZMQnEitCiHCzgeGWsXG8-tS1WU9KC3_7lwE3vphUtWA9vO6towdcghzFSyxIXnynuIfGrwfGphCg5zTZgExpul2QGe6wmEHaPkHk4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنها کشتی‌های ایرانی از تنگهٔ هرمز عبور می‌کنند
🔹
اچ‌اف‌ای، شرکت تحقیقاتی و تحلیلی در زمینهٔ سرمایه‌گذاری در بخش نفت و گاز می‌گوید، از روز گذشته تاکنون تنها کشتی‌هایی که به ایران می‌روند از تنگهٔ هرمز عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/661703" target="_blank">📅 12:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سی‌ان‌ان: اولویت هیأت ایرانی در مذاکرات امروز، پایان حملات به لبنان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661702" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xras6jlLJQ040UnboujApBACy6nitBGJjhxCEDJ-AcZcu9amW0hOzgt-oe9RDKmy-MWZPnUwEo4BCj0TvfUf3TjvJLAhf3mwb1CQGdzdELvCef3ikqisBSIaBnIJuOh8Erh2mIjTwrzGLazN3bnfwF-JSnyT8Yu0AAh4JWpTwoWn3uyfCYCZhIyLWJqaEs9KteJwPenBkCojUS73tvhnG5kQbLUVGstTWOo1DbwYHCTfjxFrON_5Pc1vVAASD1G9QiyTrVjd8hcqIbQx1u3qRsJSSbD_Xm-M96v53fAdjPvqDD19KeJYHM5VE1OvNihGZuk2ABwf4oyKLl1UUpOJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیات ایرانی عازم ساختمان محل مذاکرات شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/661701" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661700">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رئیس سازمان بازرسی کل کشور: اجرای طرح «اینترنت پرو» متوقف شد/ تخلفات به مراجع قضایی ارجاع داده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/661700" target="_blank">📅 12:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661699">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a86d7bde5.mp4?token=LDjDCtaEO4ueLWz4CiglC2LTzmBRNkkurh07oU9R7nFFlgGzM2VejscDjVE_vQrVRBGrhRwY3vtVuGXkqDK4P9ajn85Jo6HnD86vKnmZchYino-nYSw9QjLB9XVRIpqfdfjN1EEfe9bisSo6NrRBbip3XWKaU7iiUSuIT3-aV7XPh3PtEjzYp7ITLjptm7HKWzPORKkJ5eMF8GD4ZVQo45d8oqU5jlIunhSxihJ73LJr7CVvAt1Wfs8d7A3UUrb604lBwdpMjqmTfORmBfXjG7lE54xwx_YsWx8Xn5mtcMXaoczq5-FhaVxxCiSGV46H2iuNuApL97zclJB7wB1FsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a86d7bde5.mp4?token=LDjDCtaEO4ueLWz4CiglC2LTzmBRNkkurh07oU9R7nFFlgGzM2VejscDjVE_vQrVRBGrhRwY3vtVuGXkqDK4P9ajn85Jo6HnD86vKnmZchYino-nYSw9QjLB9XVRIpqfdfjN1EEfe9bisSo6NrRBbip3XWKaU7iiUSuIT3-aV7XPh3PtEjzYp7ITLjptm7HKWzPORKkJ5eMF8GD4ZVQo45d8oqU5jlIunhSxihJ73LJr7CVvAt1Wfs8d7A3UUrb604lBwdpMjqmTfORmBfXjG7lE54xwx_YsWx8Xn5mtcMXaoczq5-FhaVxxCiSGV46H2iuNuApL97zclJB7wB1FsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: آمریکا بند اول تفاهم را اجرا نکرد؛ توقف جنگ شرط ادامه مذاکرات است  سخنگوی وزارت خارجه:
🔹
در نشست چهارجانبه ایران، آمریکا، قطر و پاکستان، اجرای تعهدات آمریکا و توقف جنگ در همه جبهه‌ها، به‌ویژه لبنان، محور اصلی گفت‌وگوها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/661699" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حقوق خردادماه کارمندان و بازنشستگان دولت با وجود مشکلات بودجه‌ای بدون تاخیر پرداخت شد
./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/661698" target="_blank">📅 12:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM--RhCjqF3l0NED04Pon5nbBuXvW9FojmXQNNzNEM0WVfC88ej4xslKoax6BTIOf_HGBo3xV5y147QMawYulA2uOT4gzhqmGMEFMUo2jJp3ySC069jK242NXjOBtObs4g8G5iWz7oUmpBWcC_P4gP9N5Y2l2HQVb_Up7jnhsqOGmTKDWvaKbuGq-X6c26bJZ4H1AY1oJq2lHPcIIh_e0XF501yAHIzqcFg9rAeXvtbTcqsacD9mWnbLxNwYlSIq8HTuyrKskTZWkhxoEICDMxLPKaGcFLvHkJ9XCQmhdFPHTNi8UgH2HjVpErK8SC_eDWGoIboB-vECJshvdIeX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ راهکار طلایی برای محافظت از حساب‌های آنلاین و اطلاعات شخصی #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/661696" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقایی: امروز دو نشست در صبح و بعدازظهر داریم  سخنگوی وزارت امور خارجه:
🔹
قرار است یک جلسه یک روزه داشته باشیم. صبح دیدارهای دوجانبه با هیات‌های پاکستانی قطری به عنوان میانجی‌های این روند خواهیم داشت.
🔹
بعدازظهر هم نشست‌های چهار جانبه میان هیات‌های جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/661695" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
پزشکیان: توافق با آمریکا به نفع ایران است  رئیس‌جمهور:
🔹
تمام مفاد تفاهم‌نامه ایران و آمریکا به نفع کشور است، ۶ میلیارد دلار از منابع ایران در قطر آزاد می‌شود و تنها خواسته آمریکا، نداشتن سلاح هسته‌ای از سوی ایران بوده که جمهوری اسلامی پیش‌تر نیز بر آن تأکید…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/661694" target="_blank">📅 11:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMICqAFrj2XCPQh8NI84bXr35zG4qet-VfpyBxArg5DYsjTn6kqScnHPOMmvZtjAmxWBGMNIxqXdou9lQs8pH-j9TDZhw7ihfgIAKJyreUSg-WGJJo07PYMPwNcg4p2I4qKVe4sBCDP3BOL_Qyiink9F3OKvyCH_yXR5TLmuq9Iz-nn4DzXUWadK1N_p3q6YLi9FoxF4XChH7QqIPEulHRdyozHnnC9vCOW4CnT97hGcB07sB12MqrnmbkQPKuTF0SnlnNEqKoD5ILctbSlqt0_g18rITV7LksoxxoVA73c79YmwJrTplRqVj-OEhlTTh3LJ2IZKZj7pJw4NXn00MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یکی از قدیمی‌ترین تصاویر رنگی موجود از تهران ولیعصر در دهه ۴۰ در کنار تصویر امروزش
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/661693" target="_blank">📅 11:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رئیس سازمان بازرسی کل کشور: اجرای طرح «اینترنت پرو» متوقف شد/ تخلفات به مراجع قضایی ارجاع داده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/661692" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
بقایی: امروز دو نشست در صبح و بعدازظهر داریم
سخنگوی وزارت امور خارجه:
🔹
قرار است یک جلسه یک روزه داشته باشیم. صبح دیدارهای دوجانبه با هیات‌های پاکستانی قطری به عنوان میانجی‌های این روند خواهیم داشت.
🔹
بعدازظهر هم نشست‌های چهار جانبه میان هیات‌های جمهوری اسلامی ایران و آمریکا و با حضور نمایندگان قطر و پاکستان برگزار خواهد شد./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661691" target="_blank">📅 11:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دیدار عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک
🔹
سید عباس عراقچی وزیر خارجه در نخستین برنامه رسمی هیأت ایرانی در سوئیس با ایگناسیو کاسیس وزیر خارجه این کشور دیدار کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661690" target="_blank">📅 11:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cetSnKdafQ5jJgk_obqe-4ocZ57TRfdJZosaMe1BFo_HT4btb7QEU1e05T_D2N_ne7dZTAiCJ2n1ddVrVJHwz7brFZMGJwyDbvA9fOQp9AtVw0T9rgWVlXVgjvtacKZs8YDMx3sax2KMmjIZ7GjwL4BbEj4gnBq__8cZg0UqkzY4NuVwg9rP0K39WX4E2h9vExEstTFiCh4yVexqzMCXm8kWbIVf5_ZLB_9wqAXOhwcaVFFgoTHCWyBudJR4j2xmCZB9otSiEBqZ4WeSOOh9_1t4dkB4TsirzY2alUrSgdEMRdPRpS2-ssE2MSnfXqkI_N7PZBPbnputjR4xLEK7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PABMWglW7iwkq4aLkaCt6-IKjIf3KnMvmtJP9VPHIyQAJAwEEEs3Sy_u0zwsZKYKQ5_HCekURf3Gz2d2hgSGSglXLvM1UGv59K3eY4mwxbvmECE_eO_Lr91CjDvwfCdRZxO4LFgo5EGIGkBrKPhPn1JFwr--Bz50sM5Lirebjr61hBlQVZ3xqfbXrZqy7PVW_jRvOkX0GPO2scz5kPqxmTeELE4XSu5q1Bu-CWSxMsqTMDKjLokMBeBwwPFn6pAZFnV3KPIR08U3FzWcPqKv5Nui6lQfe9Xts0-bYkcN58gEimr08gIbCgUZHTLhGA-VKVyXKKQVoOfYJu0HkPnx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNnkcT2cCLTweVJVj8WXuAI7MNbLHBZuRx-7GHz97W6qD74LLHhHSB8K2yVUtQFBbRaUksUhMW_V5zlMNaMJVwAN1mUDrvFaQoKEaXIrfisftBNe2nK_PDZfKbaSF_ed8-5KriXUQX_LyLHmF-li5qgFzxFrHN83oPIp0mOpaXBycU5lU0YQIbIKzwG121sm-4eZWp_rbUWclh-h3h1aazUfnhrOzYmfpP1GiBO0nGUrQVttXc9_EdgTTuiLn2hks4rDhDArm3bbw44Bjn3R7gKW6ufNecqgerxeczyHblrpyfY1yUGAOXsnSLVlhFJLEr3PRk4rIhTQOwxwFVSBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVoJ7JUMX3DvvvUbbX4nFm5uZxn51szIMAAX6zCRdHLG32jCfYwcF5GnbFgVruM_2FjJuOSNZ8Bzn8L6j2zHOzUWFN_ws-6FGfpeCD2Sizmfvd8_T-wC_GfGgz9wJeuk6paU2m-UqJI3lcfv1SaQqy1el3zSWdOmcQgQTM58tMC7fw3GmcF0bPzQLeax_XLfq_tYq4D9ctNnTVonOo6VT4YtOclgBiG8JSOkAtlLV6AIQSv5J_EqB19VUlOUP1Ux-zgyvoCURd0mZuAEsrRb-EISma6JepQJNDW1ZUP6yI-v6Xz23f5VJ4WAf1vlXuGbbcxFw2wWQO3wS1hqiwe7HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این چند دستور ساده و مجلسی، استاد حلواپزی میشی
🔹
حلوا فقط یک شیرینی نیست؛ یک ماشین زمان است که با اولین قاشق، ما را به دل خاطرات، خونه‌ مادربزرگ‌ها و سفره‌های پربرکت نذری می‌بره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/661685" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/661684" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رئیس جمهور: مبلغ کالابرگ را افزایش می‌دهیم  پزشکیان:
🔹
ما وعده افزایش رقم کالابرگ را داده بودیم، مبلغ کالابرگ براساس تورم باید اصلاح شود.
🔹
بگوییم رشد ما ۱۰ درصد است اما مردم کماکان فقیر باشند به کار من نمی‌آید. من رشد ۵ درصدی توامان با رفاه مردم را ترجیح…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/661682" target="_blank">📅 11:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBzqpe-_rnMNQezcf4qcJPTwvBqL79scfFbj-9KeoczQw4A06sM3zxYH4MmhT-q0QdmJFSiqwqO63k-yr326wr_kCGbsaRH8f1kDc4mkDlbsYpnmexXnEzlWK7WymXAL817WHBbRXUxAdofdBEnYjR-BTxCNV7qMRa4OcZpyUk_r6h-qu9mFd7QoVTcbveYgL4npaAdBcBTSr2vTnQi3W3taFOB4r-cz2AmbIBWPHzCtUugWZoI4aqI4ptvhQu1K0Z_N8OFCBZCPZJkVrbuSlRJdnrrWW0En5lGXIeKKjofwG_nFH-EtWdCB3ZdSnn18EjqGhKrQ-A5i2jPMh9fLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از سریع‌ترین بازیکن جام جهانی | جوردن بوس کیست؟
🔹
وقتی فیفا آمار سریع‌ترین بازیکنان دور نخست جام جهانی ۲۰۲۶ را منتشر کرد، نامی در صدر فهرست دیده شد که برای بسیاری از هواداران فوتبال غافلگیرکننده بود؛ جوردن بوس، مدافع چپ تیم ملی استرالیا.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3224482</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/661681" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تصاویر دیگر از ورود هیأت جمهوری اسلامی ایران به سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/661680" target="_blank">📅 11:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=VIkcvWKXRJgUDd86Td6YktmGIYFEsGHSjUMC4gDPwsdZ40VsmgOAJ8IVcS3IZrH_E8mpEqqqCjECVl6C5pwxGfqK6AoPjMzwLOmM1-vzvr3f5FDr1Ge4lOJDpBKtypWTarwoP6QK2P-_-fnZGhDWAJcZqdYfk38nK5d5qvgLzOZWVAQ2SuL2NnUoex3Fmsp8S_G7WdojCC0ZX6WiOLK2iS2OyKzg7S_i6sCJUqwU2gsFkAvSTULdWs1idgB3fHBFKPkgtIFzmWJRTlsnWDLEawHRC_2d6ptc1e-UhOzj7HYlZoGbS0DrfnvZ3o9Dkf2N7_s218eXzBmDI18_pUrYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e72e4364a.mp4?token=VIkcvWKXRJgUDd86Td6YktmGIYFEsGHSjUMC4gDPwsdZ40VsmgOAJ8IVcS3IZrH_E8mpEqqqCjECVl6C5pwxGfqK6AoPjMzwLOmM1-vzvr3f5FDr1Ge4lOJDpBKtypWTarwoP6QK2P-_-fnZGhDWAJcZqdYfk38nK5d5qvgLzOZWVAQ2SuL2NnUoex3Fmsp8S_G7WdojCC0ZX6WiOLK2iS2OyKzg7S_i6sCJUqwU2gsFkAvSTULdWs1idgB3fHBFKPkgtIFzmWJRTlsnWDLEawHRC_2d6ptc1e-UhOzj7HYlZoGbS0DrfnvZ3o9Dkf2N7_s218eXzBmDI18_pUrYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه دومین دیدار تیم ملی فوتبال ایران در جام‌جهانی، مخاطبان با ارسال پیام‌های صوتی پیش‌بینی خود از نتیجه بازی ایران و بلژیک را با ما به اشتراک گذاشتند.
🔸
شما هم پیش‌بینی خود را ارسال کنید و در حمایت از ملی‌پوشان کشورمان همراه شوید
👇
#برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/661678" target="_blank">📅 11:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOlOZqI921hKYET9p9J0_yCQXXZez6B5e7Acjaaqb1gspbfFaietWy1o8jXZqq0YqrjzmqxdVXXfeOV03xai-Ku1jfpMFYFmbu2770wLaBBgifQHhxLzG2JlMBQLBzv9eu3yXO357qJrQeqhd7hhtjrs0LECFAkVrmZSMzdaovbOPjNmeKtI9P3pZ8Qo42T083pKnUf8KrIjQQt8frRQCQyWsltfwbnL3S8IOxl2VspfHqp7KXAKrAHhPiAl8j-f8zUgk1CDwQ7wc1ivGQwCilvV1FLCln0GSZjrdaY9IpDk7PQzAkJ-5-WleHF1n8os8943O56Yz9J6a0gOdLY5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
لباس خاص داوران مسابقه ۱٠٠٠ تاریخ
🔹
دیدار بامداد امروز تونس و ژاپن در جام جهانی ۲٠۲۶ هزارمین مسابقه ادوار جام‌های جهانی خواهد بود و فیفا به این مناسبت کیت خاص و متفاوتی طراحی کرده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/661676" target="_blank">📅 11:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5c0f6a0.mp4?token=UszmxzbF8o-TZOUrZmq22Rq35tZlHSe7nkkSeuCbKC4vD2TUYM1P9F6E977Kggc2DYiYPDsiin-qjySBFI9m4khCUZrdO1GmnHYSnbB8CVf2HeEK1XUUxCCka8T229Bi0lEFuR-mZX_cmuv--16NzUu1Z7Ko82RkkXoO1Eluc4h6OkyjbzdnvYX4WciCU3CaGPL-Y297xUPt0Tb5paNdzFk38dXBgERiEQhgyudi0xQDcbMEJ_iWv2rrtRWpVwstqoShN7oGGGRRuJCDEwQNpwZaKqQf4cG0LzKdqfo_yk3mck2lECUHkscwLC3UWmWir-_kI7XUlOH9OCTD88w4RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5c0f6a0.mp4?token=UszmxzbF8o-TZOUrZmq22Rq35tZlHSe7nkkSeuCbKC4vD2TUYM1P9F6E977Kggc2DYiYPDsiin-qjySBFI9m4khCUZrdO1GmnHYSnbB8CVf2HeEK1XUUxCCka8T229Bi0lEFuR-mZX_cmuv--16NzUu1Z7Ko82RkkXoO1Eluc4h6OkyjbzdnvYX4WciCU3CaGPL-Y297xUPt0Tb5paNdzFk38dXBgERiEQhgyudi0xQDcbMEJ_iWv2rrtRWpVwstqoShN7oGGGRRuJCDEwQNpwZaKqQf4cG0LzKdqfo_yk3mck2lECUHkscwLC3UWmWir-_kI7XUlOH9OCTD88w4RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز آزمایشی پادشاه اسپانیا فیلیپ و دخترش شاهزاده لیونور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/661675" target="_blank">📅 11:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60654023c.mp4?token=E_1Ft7SuafdLMTsERBxeqNsbKuEQ7-hDUEBMbErJKg_Lv2n_pCmj0nHcItfU9jCFsR6KtGpWsgbm6Tv1-8yDw6sYlHroCWyIGx917et2tFJbGxeLijVSicoCgHvNNMqVKjAIjsrwrUNb10IlZj3N1QsnrjrXCLa0ZV8Ml01fnZq2jgwrs6aBpCFS5Fgr2ty0gNvpVmfei2V43V3Dxxvb66hdho2RGF1Wq6uKSVoPK4dfqHEav5gtDm5bPbrRwILCOZr9mw33lZZ2seiifz32yoLzBxOS5r9vrF_rCA51BD-TRifduzGMJabeNoW2DonqVpEtDAvH9jSyGOb71AARhS61uJmp_IbI-Hsw5jYjx-lFpdmIYFuCwHjZcDzwJC6aH2cFH_Nya-6G4IIA5X0gtu5-hhWOgZibzbNwPrH1zWhggcXR58a8eL3piPiHiN_W87jPVzPk2sRDQDhqflpYfkE28fl5nHP1-XVtVVrAQEBpDOlnFrsF9F3u_l3-414n0uV3gvIseEvNu8i9uSBEQW_fsAD8RKRz7qLRqJ4zTSrxkxpxhncSoBcCSmWbgoKnBQiXDj5f7FFizI59bebuyvVmtqAR-rtQH3AdWq4xflhM0pbXbrNChHYfK4fHyBeOYjnyYvMhJfUXQfQEWLaf3Q9ogukjmKlgS9NS_PYJKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60654023c.mp4?token=E_1Ft7SuafdLMTsERBxeqNsbKuEQ7-hDUEBMbErJKg_Lv2n_pCmj0nHcItfU9jCFsR6KtGpWsgbm6Tv1-8yDw6sYlHroCWyIGx917et2tFJbGxeLijVSicoCgHvNNMqVKjAIjsrwrUNb10IlZj3N1QsnrjrXCLa0ZV8Ml01fnZq2jgwrs6aBpCFS5Fgr2ty0gNvpVmfei2V43V3Dxxvb66hdho2RGF1Wq6uKSVoPK4dfqHEav5gtDm5bPbrRwILCOZr9mw33lZZ2seiifz32yoLzBxOS5r9vrF_rCA51BD-TRifduzGMJabeNoW2DonqVpEtDAvH9jSyGOb71AARhS61uJmp_IbI-Hsw5jYjx-lFpdmIYFuCwHjZcDzwJC6aH2cFH_Nya-6G4IIA5X0gtu5-hhWOgZibzbNwPrH1zWhggcXR58a8eL3piPiHiN_W87jPVzPk2sRDQDhqflpYfkE28fl5nHP1-XVtVVrAQEBpDOlnFrsF9F3u_l3-414n0uV3gvIseEvNu8i9uSBEQW_fsAD8RKRz7qLRqJ4zTSrxkxpxhncSoBcCSmWbgoKnBQiXDj5f7FFizI59bebuyvVmtqAR-rtQH3AdWq4xflhM0pbXbrNChHYfK4fHyBeOYjnyYvMhJfUXQfQEWLaf3Q9ogukjmKlgS9NS_PYJKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صعود مانشافت هم قطعی شد/کامبک شیرین و لحظه آخری ژرمن‌ها برابر ساحل عاج به‌لطف تعویض‌های طلایی ناگلزمان
🇩🇪
آلمان
2️⃣
-
1️⃣
ساحل عاج
🇨🇮
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/661674" target="_blank">📅 11:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661672">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رئیس جمهور: مبلغ کالابرگ را افزایش می‌دهیم
پزشکیان:
🔹
ما وعده افزایش رقم کالابرگ را داده بودیم، مبلغ کالابرگ براساس تورم باید اصلاح شود.
🔹
بگوییم رشد ما ۱۰ درصد است اما مردم کماکان فقیر باشند به کار من نمی‌آید. من رشد ۵ درصدی توامان با رفاه مردم را ترجیح می‌دهم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/661672" target="_blank">📅 11:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661669">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccapNgsXsaDdwkShJa3U1gmpQPq08fr-D9iUgmkjtjuO35vuPOo92S215gOiisc8BrCtutQH0Jb96d2i3ahRbKlwxsfaf2R5bfduV3zyvFDC4HBWy3GqnJFzxFdHNcb0AyPYpeZxGrMNSnylZ3JAj-_ED2kVA3oEr9rD5YWiSD3s1CjfPAyTNHQUM3lCz-98C-uXBTrz2__CyqlKE90Lf71kPZI3tF9SXeeceQe75iW6ACFcEV5IYIGeILYnsTqco78f8WvJvUosgOV6kFN1RRaUbcXrDV9ymhdpZ95a0abN_40X9Vkq_W5Xpy6p034lC-WBjHbwbpO4a1Id665A0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پشت صحنه خونه مادربزرگه، سال ۶۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/661669" target="_blank">📅 10:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c780d691.mp4?token=SDywpAJtHP2PJrBTc6J0d32DPRwcze7XSZ5SW7dDWbmLninRTo7AQUGFj5YoyKzXJHYxOG8AEt0InQiA-xlusEM0iG6UFl1sk_7IrgvMkoSvHIaQIFzyPGl1mLvcC5vzEfocR5ktjTy8Lzf0ti_mbZcpwSHMavDiOzulGtRZLW50w4L5rLBuimInr8wAXnjqAMOGznoMtc9wf4aGZGmvR1tVxQZxy6busvyfDvroe5d-Bop7grR18Km6Jo_prTNguxcyx4HXrg-7F6UImPqWj934oGKCxjidB1hnpvdgpcwCIhW2o-z7BtMq2sjkjnq-4oaAGlloVbxBfFqQSyZ8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c780d691.mp4?token=SDywpAJtHP2PJrBTc6J0d32DPRwcze7XSZ5SW7dDWbmLninRTo7AQUGFj5YoyKzXJHYxOG8AEt0InQiA-xlusEM0iG6UFl1sk_7IrgvMkoSvHIaQIFzyPGl1mLvcC5vzEfocR5ktjTy8Lzf0ti_mbZcpwSHMavDiOzulGtRZLW50w4L5rLBuimInr8wAXnjqAMOGznoMtc9wf4aGZGmvR1tVxQZxy6busvyfDvroe5d-Bop7grR18Km6Jo_prTNguxcyx4HXrg-7F6UImPqWj934oGKCxjidB1hnpvdgpcwCIhW2o-z7BtMq2sjkjnq-4oaAGlloVbxBfFqQSyZ8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مومنی: وزیر کشور پاکستان حامل پیام‌ بود
وزیر کشور در پایان سفر وزیر کشور پاکستان به تهران:
🔹
از روز یکشنبه، مذاکرات برای اجرایی شدن بندهای تفاهم‌نامه و تحقق شروط آن از سرگرفته خواهد شد.
وزیر کشور پاکستان:
🔹
موضوعات در مسیر خوب و درستی قرار گرفته‌اند.
🔹
ایران یک رهبر خیلی خوب و واقع‌بین دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/661666" target="_blank">📅 10:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تصاویر دیگر از ورود هیأت جمهوری اسلامی ایران به سوئیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/661665" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0163e2ea9.mp4?token=GiKZvfESzxX6pwFmezVcJDfdUcFz12ihSQy-HOp4xbVjZivtrGvruOwzJihwEhmb1X0Ig1PcMLS-x_w483UpAmizuOcTo6sTOqgKeR9gamVjlgZYONER8x9UtOKdPM3cjr8NUfUc1XwiaKaUPOkOp4GczKPCZFI7zw5WIPX5QYUaqTAevBHgAu4Ah8slcx5Vb4ywTZBqnjULMGNwVX6n-XenuVWSRAGfEo-P86VGmsGo1DtEaZzXZkmN4vVYwrXAIQknrtr_Zh-ePTLR-py6-ZBKdaVJyqOPcUShNaNX9x96WPPdiR0lnHfo_nTg9w8usdU50rwAt-16tlykTSNUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0163e2ea9.mp4?token=GiKZvfESzxX6pwFmezVcJDfdUcFz12ihSQy-HOp4xbVjZivtrGvruOwzJihwEhmb1X0Ig1PcMLS-x_w483UpAmizuOcTo6sTOqgKeR9gamVjlgZYONER8x9UtOKdPM3cjr8NUfUc1XwiaKaUPOkOp4GczKPCZFI7zw5WIPX5QYUaqTAevBHgAu4Ah8slcx5Vb4ywTZBqnjULMGNwVX6n-XenuVWSRAGfEo-P86VGmsGo1DtEaZzXZkmN4vVYwrXAIQknrtr_Zh-ePTLR-py6-ZBKdaVJyqOPcUShNaNX9x96WPPdiR0lnHfo_nTg9w8usdU50rwAt-16tlykTSNUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نام‌ اثر: تاثیر اطرافیان بر شما #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/661664" target="_blank">📅 10:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae8430d65.mp4?token=cOLOzX_09bXl4ADDUmFB9V_85NDDgeLn7DrdHoLM4Yw3YuwP0jj0lZynyZuZ8hDyvZu4fKvMDUgCqxLglSsunp6j7qPVbXH50hZWBETCLf9INSr0ZNy8kFw0KolpImpAz3SisDu41q361274B7Sm8Bzr6iKfwuydo0hVhE_M-jsD4o47fOvYIqumuI7ONe55qjmp9gjIiTy51E-viBPYeJ6eme-yDRN0_gbosWHfh1Jt_Gm7xRucMbwi165OuQOw5rxjFTHQkeAULdoVILbxdbV7mAdqmYpsHydzV7lZhrPhq3HFCGJn6CJhRBmTCRIVZW_vqipT_LA8Nh1baFnabA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae8430d65.mp4?token=cOLOzX_09bXl4ADDUmFB9V_85NDDgeLn7DrdHoLM4Yw3YuwP0jj0lZynyZuZ8hDyvZu4fKvMDUgCqxLglSsunp6j7qPVbXH50hZWBETCLf9INSr0ZNy8kFw0KolpImpAz3SisDu41q361274B7Sm8Bzr6iKfwuydo0hVhE_M-jsD4o47fOvYIqumuI7ONe55qjmp9gjIiTy51E-viBPYeJ6eme-yDRN0_gbosWHfh1Jt_Gm7xRucMbwi165OuQOw5rxjFTHQkeAULdoVILbxdbV7mAdqmYpsHydzV7lZhrPhq3HFCGJn6CJhRBmTCRIVZW_vqipT_LA8Nh1baFnabA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدردانی لبنانی‌ها از ایران؛ از وفاداری شما متشکریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/661662" target="_blank">📅 10:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661660">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سی‌ان‌ان: اولویت هیأت ایرانی در مذاکرات امروز، پایان حملات به لبنان است.
🔹
وزیر اقتصاد: نرخ سود باید اصلاح شود.
🔹
انفجارهای کنترل‌شده در دزفول از ساعت ۱۰ الی ۱۴ امروز/ مردم نگران نباشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/661660" target="_blank">📅 10:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661657">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqeNLVqO-OKv4BM2nDyNxIey2rxH3rTgn4B6w5VwiauS_VzD5h3zkfYlsA_kjYGPerhFJCc9mg_Fw-p7C0NcQIsOPK7Czfs4t_FUCyR_ykvZyJHkqJixffw1J_GlM6dJ8sSUpxOQUOvD2pVn4q5sImN0x1TIVs1qXTdiHZ3RVcv9Ka5s5BvDVfq7B_un2S3WiTk6XfOjd1WO_BjuNPMmzJDSnBPa0_WKUNttGIgZ_jDZFf34-qsfH55QtsdhWzUzD7GDRKRwPLIM_GcFjdPVCd_uObwvGKdHsYbn2i1dXxTS_8n3q1fA80TsJH0b5RFWLqoVaWDWLf1J7s-PZP6leA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHAQ2FSc63sURFL5a-2lbJCtXkC8JPWdCYa-F1x2n3pCHJCuZIvA0zTk9RI41wlAfvNjYLsdlvLjpjUXiNyk-DZXNCP_gym4d3ohdYgV_yuXcuYTZeHFG8qD7Z4sYwf30g_X26oYq6t_FFZO7os7pGNoZ604Dqf0M5Bj1JskdGm3yuxxKI66JylYNk-HdgZkj2i9_rDZCLNwpbHRVKn7CKb3QC8x9bHYHYHdnK1Z2g9qCZD2IFhr_eAEaRB7mFAl7YYgXH91yrHI6-bqoywrqnb4kVeEhw5m1AaNH0n86SkR84TVqdLQ04ShvNRg8q9Oh7wozA6xjnLf_nYCMOcSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خبرنگار الجزیره در نزدیکی اقامتگاه بورگن‌‌اشتوک سوئیس: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/661657" target="_blank">📅 10:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661656">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/661656" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661655">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnXLQUIK7lC65PDeLLFAYH2_4DFXnwzLB1NojHEuH5rhtjFWpkCGj7no6pOa8xm_B9mgBVR5YrefnfDo5AGjfGsMIFEpkWO8vPR2BTuU_39Esznc8KOV2TvNZ8DKDnCerej8hN13zoHrF-QBz5-eXuU1QnuCaMz0y0udB8sxUsmc9Hu0a2S4CytkFuYX9FOfzWq-aG2VqHw37zVDk5hH3ubtpVGAR3vDmCmz7Jt0AcHnuA8rcrMgK4qlBVoVP_gwCq7syVFhnTRwN4n6VczF1C21wxh0OTut1_ZzUaqnc__4IenN5iyKhtgLf9w_HuLzemzvBzG6rA8gPXQ1rJ7CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلیس رومشکان یک دستگاه پراید را که با حرکات مخاطره‌آمیز در حال تردد بود، متوقف کرد و مشخص شد راننده آن پسربچه‌ای ۹ ساله است که بدون اطلاع خانواده خودرو را برداشته بود
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/661655" target="_blank">📅 09:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661653">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مدیرکل بنادر و دریانوردی هرمزگان: نخستین شناور حامل کالای اساسی در اسکله شماره ۱۰ بندر شهید رجایی پهلو گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/661653" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwtZEFUlQlWo4jP46pteDB5i27CXTsdyZVeHZikRQpcMrrD-28GesGDSh3dN5VWZlJryBR4EcELdCkMMubucKd-grBaNdNZdKacgedT5RCy9t6nj_PbGF_9nCfzV6ScG5YPgPZBejLBd6NfGAStrCLFBeapsSh5pvkh3pLLN7XOiSWIEpMNsKRu_oOhwvUJQDs9uF3lGwUhLDftBJsxL4rlLbgFOc89fkY8Uze9K1aUwBiShr3I-oG3E-l2kCL9zg-xGIcZiaSzcY4RFepqfD2HZbgDYjAB7qHS0AoGKN13LRA13NLIwXZWgZ-NXSW8LZwlhQw7iW5DIM4x3Rfv_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/661652" target="_blank">📅 09:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM0tWenNebm9ejYdpPHUfARV6P5CzpVZgt_eJ5ExLPBF8Y863-VuR5qjQajfe60b2szhICD9P96ys_Fj-Knoxl9DkfT3PprgfS6_ZLGqGASUU0n_YfekP4v7wNU6i0FnebRiP-vEXZTKS6sU8HD9gVeN_kkWDpm2tPYwxeaBQoba1wGAv4xFG2jR8W6DCwM6s9qRUQQFImfkrabnvZAydE1ycUZzBCUaS57mhqAIpD9XETHK181K4Lfr3hcn77XFDfFmVm1KdUnUTpaiHGvTwxcE2whzcJA3hb9p5D_ih835wpcj_NP2Yr82jOvvL8tKiV7MisgtMxAZzF25PZEZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: هرگونه خوش‌بینی مورد سوء‌استفادهٔ دشمن قرار می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/661651" target="_blank">📅 09:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd2c9cdf88.mp4?token=ROhlpTwHfr-RE32ONwg4Fd5ZNpAOowBFzDxLCynBN1fepmImyKFk2k7G-aua_ME3BuiAP9ceF3WLa4aym5VbAWF7V5936bVCjplJPNwo4eyDRGOGiK-X5n6dvKBqdIq2OEsSua2c4uzG3f9gxZd_39vq08PAPLoiQpDlgSeJUSOv3jmNL1Dh9Oj4pJRhHg_UhMVTuqNza5ufFTU4I82rcTwLHTxl1Gffr1x62oAwlgwAM_0ZE9ry6vx92mj6z41jX1HIRqimdTK4DzNz_XdciZkGF02dkcVCX5u01hoWl3ceoEo8dTa9E6AyJGnOQVNOKd5DUKkpCyX3uBkOS0Iyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd2c9cdf88.mp4?token=ROhlpTwHfr-RE32ONwg4Fd5ZNpAOowBFzDxLCynBN1fepmImyKFk2k7G-aua_ME3BuiAP9ceF3WLa4aym5VbAWF7V5936bVCjplJPNwo4eyDRGOGiK-X5n6dvKBqdIq2OEsSua2c4uzG3f9gxZd_39vq08PAPLoiQpDlgSeJUSOv3jmNL1Dh9Oj4pJRhHg_UhMVTuqNza5ufFTU4I82rcTwLHTxl1Gffr1x62oAwlgwAM_0ZE9ry6vx92mj6z41jX1HIRqimdTK4DzNz_XdciZkGF02dkcVCX5u01hoWl3ceoEo8dTa9E6AyJGnOQVNOKd5DUKkpCyX3uBkOS0Iyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به مداحی که می‌خواست با تیغ، حلقومش رو ببُره: خب فحش بدن؛ هر چی بیشتر بدن، خدا از گناه‌های من بیشتر کم می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/661650" target="_blank">📅 09:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc_nnV-mPYn4gP84iHgzGkUqf66t20Pz2hardzwOQQQPW24aPktEcYfOs3s8ivmVhx6UPA6N0KkDHMYLFfShxS0wCMMMuEN374xOqKrAM320SUbW508ENIjO7gNiTBOK5J1_yrg1kwHvsaT7CiIxIlibJ8FjMHLRNhSn6JaV17ByklIGCt52Jsd1Od7KQmqVQ7mi9Uiol0HgYre_h8KJX2UimonmQ5A6xwLXwKXKwXYAT45TKpmMRydqE2Tq4N-ZSEGocFpBPlRuHqvd8P2KEuHHCG4ev-0jcd0_HhjdsBFkcOIFeJCQShii3f1KyCqCx23hBOlWf7IT3i1yiSia-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس اطلاعات آمریکا اسناد محرمانه منشأ کرونا را منتشر کرد | چه کسی ۱۵ میلیون نفر را کُشت؟
🔹
تولسی گابارد، رئیس اطلاعات ملی آمریکا، مجموعه‌ای از اسناد محرمانه‌ درباره منشأ همه‌گیری کووید-۱۹ را منتشر کرده و مدعی شده است که این اسناد ارتباط‌هایی میان تحقیقات تأمین مالی‌شده توسط آمریکا، مؤسسه ویروس‌شناسی ووهان در چین و برخی مقام‌های بهداشتی سابق ایالات متحده را نشان می‌دهند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3224472</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/661649" target="_blank">📅 09:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661645">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPwEXeRxl8s-3oFh8vNFX5onuqPh4l607x_lfPqhA37eP4Wk3jXMHw9wq0uwIDFYe9Ygtvz1pWmqL2Wg0Rx5ofj4UNNkZk3QJpFrpUgS6A3blpHkyk_aJYXAJ3YNXZFmBEsKEt57Vo_ldN3XEQHG5N8RwClA3DRGH3JXY7UeyQGvxbYZDUbOivtFh2ifkPM_nSDGQegCUHdalD8n7ph_dZKiC7EM_pxDanqg2cnRkKLlvIh3aoSS3704IMuLnbkWX7R6N3ECTqM9YAt0eg7NfyVWT5ttnsIJet8poAhLJZ_O9ipVmjN7lq_IByz_kNT4wOMhNef69lGtgYeL8aE5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slBe289NCU3HB44FqKpOH6Mhu-AmT6yVBYf4hAmTOhBfOVYsqipky8tRbCfqldBMfIaQkxB9MqrWjzXzZCMCOWAgyqNz1zNN7GbMXaLTRqmqCJGeSxSujH5dMyBGIa1IJAKV1vW9Vh5_chmsUhIYVOojqhcQIevLqoieRaLoud6UqXBQKDZ7D3WsNn9K5lESdB1TvcARqDVs9VlKLp6EVIdomVQNhXe_9PT9hbuXtvxXSlLkJ878I3IVkPxoOvtzhPCo5-UV1RIj0zZcfUArMaZSJIfcCl2LcFHQrbCDIqU4bIjAuTvahRMR0ZC4x9kkLj2GpQklffgVfPiCjj3_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRDPm1RHSKaLZcxHdQKFnHxJ_KN1Yq9-J7wWn4mf3-WDajO0eHd-hrg-XoNCkzsF_Y8MPYJSM43Hio6Utwshn67o9B3vLVnl3PlPUgZIz77zv8KGrbfYQkkzl1MpoDKGtTFBAbH4ol3pYSRl09MHn93h06NIRFrjqbzUJtQFydTKrHvGgPooTX7OlMLgddkBvBb7ujpvFJVfgXWVOK7rfY5jmq66-COBrd-SPoCLEbzsZrUU2wAjzgRU0RuwvrDGhGuxA4XRqQZq5mnAlLZOxDLDdOB0ZZPIwsOoc0uGasV2KswShaLzIi1pHEOjOP7vYNbmfW76G9T6bY9OJY4LUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3466d6772d.mp4?token=W4izeSVp5Lgh-juhZE-npNSVaP6Q-UfNCueQDjdmN9CYDfCBx53s0Pvu9frmyIi73bWFOm60LX8VTgh59PfRV8zkb2a2eEkStq46BDyrqNHFvMKlUNId1Cclu_9Zv_u-IvhQuuG50MoV7wfZgFkS4HVgmo_G0J-l-C9SBohNbbixyUytgC2pzXmYFi2vJDrbtmX8AwIyMHMzJBK2_X5OJlKDIMsvyDcow5IvVcpdHwMK6LCCISXSc_HRUBvaDqIOdU9U6xwUPIj4t7xGu4gao-5Yp1OXkyd95_k4zcYk2R8dTn3qUpb7FTisAUWsZs3WJxb_iphIYr5efwNV_HtyeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3466d6772d.mp4?token=W4izeSVp5Lgh-juhZE-npNSVaP6Q-UfNCueQDjdmN9CYDfCBx53s0Pvu9frmyIi73bWFOm60LX8VTgh59PfRV8zkb2a2eEkStq46BDyrqNHFvMKlUNId1Cclu_9Zv_u-IvhQuuG50MoV7wfZgFkS4HVgmo_G0J-l-C9SBohNbbixyUytgC2pzXmYFi2vJDrbtmX8AwIyMHMzJBK2_X5OJlKDIMsvyDcow5IvVcpdHwMK6LCCISXSc_HRUBvaDqIOdU9U6xwUPIj4t7xGu4gao-5Yp1OXkyd95_k4zcYk2R8dTn3qUpb7FTisAUWsZs3WJxb_iphIYr5efwNV_HtyeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توپ رسمی جام جهانی به ایستگاه فضایی بین‌المللی رفت
‌
🔹
مهندسان ورزشی مرکز جرم و تعادل توپ‌ها را با دقت اندازه‌گیری و بهینه‌سازی می‌کنند تا حرکت آنها قابل پیش‌بینی باشد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/661645" target="_blank">📅 09:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661644">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تحلیل سیاستمدار فرانسوی از جایگاه جهانی آمریکا و روابط منطقه‌ای ایران
سیاستمدار فرانسوی:
🔹
به زودی ما شاهد غروب «امپراتوری آمریکا» خواهیم بود؛ کدام تغییر رژیم؟! در ایران ما صرفاً از «اسلام‌گرایی نظامی» به «نظامی‌گری اسلامی» گذشتیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/661644" target="_blank">📅 09:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661643">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ونس وارد سوئیس شد
🔹
جی دی ونس، معاون رئیس‌جمهور آمریکا، برای شرکت در مذاکرات با ایران وارد سوئیس شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/661643" target="_blank">📅 09:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661642">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تنگه هرمز هنوز به صلح نرسیده است؛ با وجود اعلام صلح، بیش از ۵۰۰ کشتی همچنان در دو سوی تنگه هرمز در انتظارند و بازگشت به شرایط عادی زمان‌بر خواهد بود/
اقتصادنیوز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/661642" target="_blank">📅 09:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661639">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXpvBwwX0KUyKEoSqHpSflsV1Izpx6QpCJxbZRPW7vgdLBoRxS5YH0zKdUtcD7f3T_wh0KUJ2brzbZgWzICLDJq8kSB3Tzq9s5wzq4uv5NDpofK-sLNDcbNZilXAL0Iow-32_Sy8est8uRYWk9LxQNB3vlp0GQOX1owI5n2h_MoE4yiL7x9n84Z7oNW7QrSlPuioW0Z87Ctzhc45H-6LDNZ9PPDx4NfohNDohifEVxWBvRIQcsSqGY2k6Fwx4nuiqYSOF3YUs9iSQ6gVowJ5fVYZ6rbYl3mYikRtZ8M3THT9JXa9IwUICjlHhWRCXlwqfRQk2sZ30MUqyx_NfENqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای بازی امشب مقابل بلژیک با تصویری از بیرانوند و کورتوا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/661639" target="_blank">📅 09:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9bc3ebe5.mp4?token=YO4O-mQoHPXS76LNJ2QUXviqGXO7h-BDwRY3SJYQiQabfb8O9phhGOT3F02eSdVSPLAWnTpcvHPAqkwha2Zr9iHp426zmAlXBOFP7p4Uf2Uq0Q6u2950yEjrDBvW7nynJbDfVUK28F1ZJhlrLdyGCAZLlAt2RQvnUeiaE05xLwmfzyU-ZLxhR-0oaXtdXw5M5uVTwsBIgXOBrWhhVV_t__rWchFREzAKvQSA24TFzB106VTIa4wZ0sXqezIgPxLxbPGTHpaGbEurx7VdldvuCFJzyZm9EnMGV7zKO90ncZybJWENXVHHLTP3byMTdbZoECuqhJMszPSWNLrey2iPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9bc3ebe5.mp4?token=YO4O-mQoHPXS76LNJ2QUXviqGXO7h-BDwRY3SJYQiQabfb8O9phhGOT3F02eSdVSPLAWnTpcvHPAqkwha2Zr9iHp426zmAlXBOFP7p4Uf2Uq0Q6u2950yEjrDBvW7nynJbDfVUK28F1ZJhlrLdyGCAZLlAt2RQvnUeiaE05xLwmfzyU-ZLxhR-0oaXtdXw5M5uVTwsBIgXOBrWhhVV_t__rWchFREzAKvQSA24TFzB106VTIa4wZ0sXqezIgPxLxbPGTHpaGbEurx7VdldvuCFJzyZm9EnMGV7zKO90ncZybJWENXVHHLTP3byMTdbZoECuqhJMszPSWNLrey2iPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرتاض هندی ۱۲ سال است که ننشسته!
🔹
«دولت گیری جی مهاراج» مرد هندی نذر کرده تا پایان عمرش هرگز ننشیند و معتقد است این کار او را به دیدار الهه هندو «ماه‌دیفی» می‌رساند. او حدود ۱۲ سال است حتی برای خواب نیز به‌صورت ایستاده و با تکیه‌گاه استراحت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/661638" target="_blank">📅 09:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661636">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiyIPMv5g1EivlpeJLNHcLz2gLJGOXb3oWShqPyfHEs7gJkf7cKozkOum55NkdYyXpP5eh-zw2qEYPzxgccekWFk-kYYLM39l9W3VC3PTZRxISUuZEe-8gueZDynaQfmMVw3K2KwXik9deDnWbD8-3Wx0Z3TBu8fR9y57kNKAjAcRa4J42YJYl4kIG7WwlXOx81Rtyfo3B0rqt2BQY6H8VjTlbtaDzazlvItLVxfFZScnZubFRgmV2AHh-USly59DVR0pp_hQ7jGyBeXdXiQo4PguU-vWmeK8nulMTw8x84sVbtvLEu9F5e8hp8wz_fx-waAard4uMaP0RbAH8RAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c9d4dbee.mp4?token=m2DaJhO_jwMy2X-bGZCvOU9rLHI7xbgNcUuUsKxRzfvvWpQJaJdjAml-mOUyzuQKPzyLkYu2XClYHC9HgA87LqdUL4A-yetFWR_Al9E7yhyEupIQNkd37ASe7IXQBlhYZACAJGqVNOmFWnDExAZhyJTulyuKd8T47brn3uwuQQSAjM09dHiDaEr-xSJvSDE47S4D8NGBdc8pG8-mwD77rMQDtf3457O0nmJumsbY9U2hq_wnJphX92q0TUpUN2Oivft0DssZr2PDdaQxzHb7RMWJL7bWuYKuSYRLTHgqLmhAwOa6t5AFAfAksca39nAnsf2Vf8tRHyiaIv81AS104Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c9d4dbee.mp4?token=m2DaJhO_jwMy2X-bGZCvOU9rLHI7xbgNcUuUsKxRzfvvWpQJaJdjAml-mOUyzuQKPzyLkYu2XClYHC9HgA87LqdUL4A-yetFWR_Al9E7yhyEupIQNkd37ASe7IXQBlhYZACAJGqVNOmFWnDExAZhyJTulyuKd8T47brn3uwuQQSAjM09dHiDaEr-xSJvSDE47S4D8NGBdc8pG8-mwD77rMQDtf3457O0nmJumsbY9U2hq_wnJphX92q0TUpUN2Oivft0DssZr2PDdaQxzHb7RMWJL7bWuYKuSYRLTHgqLmhAwOa6t5AFAfAksca39nAnsf2Vf8tRHyiaIv81AS104Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارمای اسپانیا به ژاپن رسید؛ توپی که میلی‌متری گل نشد!
🔹
شوت ژاپنی‌ها مقابل تونس با واکنش تماشایی دروازه‌بان از روی خط برگشت؛ صحنه‌ای که بسیاری را به یاد گل جنجالی ژاپن برابر اسپانیا در جام ۲۰۲۲ انداخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/661636" target="_blank">📅 08:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661635">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8owHnYxKYi34J2NvrRqVe73i2XWuJdQG3i3L2l0hOJmD91CXfP3vmVtrgkpZDV8eQaJVsdUmk2CgV4cgXvOr-lmyxyi8HW8Icbp2aMF9TefBUGvUs8PhUbTJyw6C3NoiyKVaARdRDcVE1rIU9u_GDEWvrsLG2r4Z1i7u0wL0-iXHbZO5BEk9s8-5kBUob_Kz26GiDMx-uUFaLfpnye12QV9cX3PopdAeiyB-DeRNl5QVgSYFLYEYx2orXz-_t04ByO8w6E2MmJBD5jfsXWRWwDlJXRuTdRTW3jeGBrPEd9FcAaMg3CRo0Bs0tVywzcZzsz5RtEKdqIFm2S3uSFmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت رونالدینیو به فوتبال در ۴۶ سالگی!
🔹
رونالدینیو، اسطوره ۴۶ ساله برزیل و برنده توپ طلای ۲۰۰۵، با باشگاه راونا در سری C ایتالیا قرارداد بست و احتمال دارد بیش از یک دهه پس از آخرین بازی حرفه‌ای‌اش، دوباره به میادین فوتبال بازگردد
#ورزشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/661635" target="_blank">📅 08:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661634">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اجبار دختران به برداشتن چادر در آزمون سمپاد
🔹
اخبار رسیده حاکی است در برخی حوزه‌های آزمون سمپاد و نمونه‌دولتی تهران، از دانش‌آموزان دختر خواسته شده برای جلوگیری از تقلب، چادر خود را بردارند؛ اقدامی که به‌دلیل نداشتن پوشش مناسب زیر چادر برای برخی دانش‌آموزان، موجب استرس و اضطراب شده و در برخی حوزه‌ها نیز با حضور یا تردد بازرس مرد همراه بوده است./ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/661634" target="_blank">📅 08:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661633">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قلعه‌نویی: برای بازی با بلژیک کمتر از ۱۶ ساعت به ما وقت دادند و مجبور شدیم تمرین نصف و نیمه‌ای انجام دهیم؛ این کار را سخت کرد
🔹
نسبت به بازی گذشته تغییراتی خواهیم داشت
🔹
اجازه دادند که برای بازی بعد، دو روز زودتر به سیاتل برویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/661633" target="_blank">📅 08:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661632">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001b5e2780.mp4?token=ZPNq56Tyl6IRvih48faj_Gcwzro3FX__oEqObrj_Kahnjb3LYwbC6bEsXYqOSgEktjJAP-ad-dnPBQ0FAY2-k4459GxIEbh7VL0-MvhEKLoNsnVmzKFyq_89GoLm_iTgA7_36gTeLKzF1pTa4BM7xNjNPSbkSWtfMCV78YQQjnZJymrVZ0WDKK1UTTtV8OBWNM8OzvH_V2gG6sdJdhNMSO-t4W0TOFPIW1mx2fQ0TCDyFxQPMvo38s4IVfAVCokm5mhAuYsvninzkx40P2dfQjGE6gaJSbN69_d7cAfU7VCJDmzUrlbHjYTbYC4enpZPktgANz0L2ay32jfAZE3Zfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001b5e2780.mp4?token=ZPNq56Tyl6IRvih48faj_Gcwzro3FX__oEqObrj_Kahnjb3LYwbC6bEsXYqOSgEktjJAP-ad-dnPBQ0FAY2-k4459GxIEbh7VL0-MvhEKLoNsnVmzKFyq_89GoLm_iTgA7_36gTeLKzF1pTa4BM7xNjNPSbkSWtfMCV78YQQjnZJymrVZ0WDKK1UTTtV8OBWNM8OzvH_V2gG6sdJdhNMSO-t4W0TOFPIW1mx2fQ0TCDyFxQPMvo38s4IVfAVCokm5mhAuYsvninzkx40P2dfQjGE6gaJSbN69_d7cAfU7VCJDmzUrlbHjYTbYC4enpZPktgANz0L2ay32jfAZE3Zfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ایستگاه فضایی بین‌المللی در حال پرواز بر فراز استرالیا و اقیانوس آرام در شب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/661632" target="_blank">📅 08:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661631">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تیم ملی کاراته بانوان ایران قهرمان آسیا شد
🔹
تیم ایران در کومیته تیمی بانوان قهرمانی آسیا با برتری مقابل تیم های چین تایپه، ازبکستان و ویتنام در دیدار پایانی هم مقابل ژاپن صاحب برتری شد و به نشان طلا رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/661631" target="_blank">📅 08:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWgTmXpCQ6olMOn3tu5gbYiEizmd2eB6NzGQeGVP7-lcWdnBzOOV4R10xQw3mxZaA2PNDc3xAYngymSW0m5PEgKmYMRlwgOP7lA4uBz7GON2e2W4m0MRp8A70hYx0C9G9hRTHmqpWE8KcEoZwftHm64bRFAXXQBabR7hkbkmmpbgnSzSUauPnU9hqPzXywZF03vxfD0wyf9g0RJbVgqLkM_uCxIfl-l_8wGJS8aRsuhM6SDzD0DaCf_egA1LBC418XoIu43eA_LPmOt8o9rhuzcOzP2yTmLNThp3z9_ZiizflIOr7w2Yd-jwYAh4nwzKBrgYgKiPL90_PJCLJrKK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8SO-IMUFDffHB9h9yT9jDP0IGcM_mXGRmexfx83ZvXF-T4szMp69BTWurjaMoaXlfY7-37CD6DhOPL13RGPsekIfyptTfwebT3c5PqXy0PG4LUDhoNuQvQu8_byvplF65SbTbKf3v2Ln6w1xlKRO8EEdQMofnMQ3n-tf_q4apMpTjBhCGCtuTlsEZkT5Z47HsS00LeVTfUOwIPBqMLbMP_VNjj6zwlBBBUYLNBqT7TuJqyKRGFwA1WQbmKF5n4WWfY2gTvIaox4P4drij3Ui57dtZtboZe80XMQBZuRx3ZeScqE8WsmThAiWmdrSVQw0Vf-WvbRlvnS7a4Hd2ufHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1uaW7RdtTlAOJ6aWkWbUlC2pYZREnQG4PS9o_ITh_8RdlbG_s9E7vgUsK98cqqA670BZCkxbZDncHOtgMX7eK9Q0_cHJiSRIleZZDB0DwTQY6j2gitkAdGm8M2I9U2RW7gcD3M1R9GMIS5AYxQ8vD85UONkown61TaqbmHNTH-3rMLc9ceMAlXV_9oj5ibYbpf99umJ2D7K6uZkpHM_XyI1s3ffp4FNFc3-mADzeoVtiEGV1zQD-t9sa2RJrdCoDMGGyoYoFwF9UbaYD2-q__z9wTtb8ci_bkeuXH-WB2m0Xtv5v0CcRNTnslpmzlb5TgQcwyCIjt9EmzEN9VjDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm_G_Bo7UWkO7Mj2YVAfku4x4tgdTzMsdt04305Df8m7jKo3_jArCARjkMzwitgtsRgz0vpocWgDdX6M50yiauKri7ZJrtpzN65O7NajQ9TDjjXgxa3OpKWZ5msnhF7ZgecwcQmhKvQ-pIP-0TNdsDR_Vqk7o-NrBKz9QxNzp-ZQ2ZGusFVf7FxR9mdrab9GfsQ50A4bifk6Bg6rJDDcpiqrXu0r5rBmel2WlrNMNGJbblDvgi1SE26cJKSYzCaiygz-z6VDIwxScvQUdaMyN16KJ0Qu6ijIIs9-iv9qxKhKZDZ9pso10Bfmu4LXgrjPPs-iEju-I2oAifwD0ZAyrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب جادویی قلاب‌بافی و گلسازی در تاپستری‌های خلاقانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/661627" target="_blank">📅 08:35 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
