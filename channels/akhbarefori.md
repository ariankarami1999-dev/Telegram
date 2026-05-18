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
<img src="https://cdn4.telesco.pe/file/BH5E-dUd-WW-7ytskn_GF3xtuhInPFbmfSyRK71mnm8TjkcVVxTYhhtxF4aNjGRAqbhaRdOZPmbO6enerQDrqgdWmBePPvQY3HZhgdDBUX8jtwXu3BhVbCXlQf34zQsHnF4haykmaNrPDaW8hST-1lx1SRt1IGEfQHMbEQwXxzDkiA8MkAbRUKLNxdxXuTo8erI5VbsMqWIRz1dIsR62Ny0Ud3HOwpfL30aqA-bfjbABa9xR-_EzzZRWL80ovIU4_vPl033mpG3VLfcgwxjNEDBcIcbTDBRHxexhzVwi2oPSR9aasAuXGUtUNNanS7r_gVATz8tOOZaL58CdwMaYXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-652793">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c126e340ef.mp4?token=UT2lwhdAKumb0JKf5csP6ZtnJ3xs5nptWr0fcNxZVzUTX5lcSY4elsBFo7B0pzpOWkI2mPN9DWKem-5Ep1QiE_k7NCha2NZNGetvaafNrk0c7kAGf0nb68JyIqxDrYbUtq-XnwMAZI8hUHCTCBFanqslyu04VKgq8C4GuRGCRkXdbroklKwZ8hy89zx37ZCC5i7H7IJkt8XuS2eB0wOHiPOnaaUrl26VlQh9u0T5lMym-WlmL-Q2bKGTXwNbXC8EmG0y7cfDRB_wVg5nDu7E75LxGguF1vRf38IA4afiKcrfvgQGLA-U3FUyNSDRkSZ3RYeQEuuEtna4JBx7yHG40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c126e340ef.mp4?token=UT2lwhdAKumb0JKf5csP6ZtnJ3xs5nptWr0fcNxZVzUTX5lcSY4elsBFo7B0pzpOWkI2mPN9DWKem-5Ep1QiE_k7NCha2NZNGetvaafNrk0c7kAGf0nb68JyIqxDrYbUtq-XnwMAZI8hUHCTCBFanqslyu04VKgq8C4GuRGCRkXdbroklKwZ8hy89zx37ZCC5i7H7IJkt8XuS2eB0wOHiPOnaaUrl26VlQh9u0T5lMym-WlmL-Q2bKGTXwNbXC8EmG0y7cfDRB_wVg5nDu7E75LxGguF1vRf38IA4afiKcrfvgQGLA-U3FUyNSDRkSZ3RYeQEuuEtna4JBx7yHG40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل برای سه شهرک در جنوب لبنان، هشدار تخلیه صادر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/akhbarefori/652793" target="_blank">📅 13:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652792">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اجاره‌ها در دوره تمدید اضطراری ۲۵ درصد قابل افزایش است
🔹
مدیرکل دفتر اقتصاد مسکن وزارت راه وشهرسازی: طبق مصوبه شورای عالی امنیت ملی در اواخر اسفندماه ۱۴۰۴، در دوره اضطرار، قرارداد‌ها به‌مدت دو ماه به صورت خودکار تمدید می‌شد و سقف پیشنهادی وزارت راه و شهرسازی برای افزایش اجاره در آن دوره ۲۵ درصد بود.
🔹
اعضای شورای مسکن استان تهران تاکید کردند که ظرف مدت یک هفته، نرخ جدید اجاره‌بها برای شفافیت بازار رهن و اجاره تعیین شود. بر همین اساس، کمیته‌ای متشکل از دستگاه‌های مربوطه حداکثر ظرف دو هفته این موضوع را با بررسی تمام جوانب، هم برای استان تهران و هم برای سایر شهرستان‌ها مشخص خواهند کرد تا مورد قبول و عمل موجران و مستأجران باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/akhbarefori/652792" target="_blank">📅 13:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652791">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a894fb101.mp4?token=KdtEIBtwZLNe077y8BCOsDbNKu7qRrF7ZNpwfr6iN_gubJdjwW2WZ9pSFNnt3sg63iRR4PvvxKiVIMU1ozRQJOqU92pVfATu6_pppvMjB2sr6wkePqRXXJxLdaEiEmwASYdKtGsU78JxXurYSvuEBs1n54zm-lUTTqnJXFl8h_NG46pAtyN7PaHCO9bXxQipRBykD-Wdm2F748G_yZTUZpT-vrScTlaB43zAMuQ4eCcV31r3x7zFm_D4I-i5mirC49YytF4gRlYXcxAgXLoOlbMvZrtetx_majbpd9aTcb7kLAZCp3KzOnBzqbpXpIoD95ZNRztn3Z1Xtvy8yemxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a894fb101.mp4?token=KdtEIBtwZLNe077y8BCOsDbNKu7qRrF7ZNpwfr6iN_gubJdjwW2WZ9pSFNnt3sg63iRR4PvvxKiVIMU1ozRQJOqU92pVfATu6_pppvMjB2sr6wkePqRXXJxLdaEiEmwASYdKtGsU78JxXurYSvuEBs1n54zm-lUTTqnJXFl8h_NG46pAtyN7PaHCO9bXxQipRBykD-Wdm2F748G_yZTUZpT-vrScTlaB43zAMuQ4eCcV31r3x7zFm_D4I-i5mirC49YytF4gRlYXcxAgXLoOlbMvZrtetx_majbpd9aTcb7kLAZCp3KzOnBzqbpXpIoD95ZNRztn3Z1Xtvy8yemxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک شهروند کلمبیایی از ایران و فلسطین: ما به آن ملت بزرگ، به آن تمدن پارسی، به آن مردم بزرگ و به آن فرهنگ عظیم ایرانی که امروز به جهان درس می‌دهد افتخار میکنیم
🔹
گفت‌وگو اختصاصی خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/652791" target="_blank">📅 12:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652790">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
کشف مقادیر زیادی سلاح و مهمات‌ از گروهک‌های تروریستی ضد‌انقلاب
🔹
گروهک‌های تروریستی ضد‌انقلاب مستقر در شمال عراق به نیابت از آمریکا و رژیم صهیونی که قصد انتقال محموله بزرگ از سلاح و مهمات آکبند آمریکایی به داخل کشور را داشتند در بانه استان کردستان مورد ضربه قرار گرفته و مقادیر زیادی سلاح و مهمات کشف و ضبط گردید.
🔹
پیگیری‌های اطلاعاتی برای شناسایی و دستگیری تمامی عناصر داخلی خود فروخته گروهک‌های تروریستی در دستور کار قرار دارد.
🔹
قرار حمزه سیدالشهدا علیه‌السلام به همه عناصر و عوامل خود فروخته و سردمداران آنها هشدار می‌دهد که با هر اقدام امنیتی بشدت برخورد و آماده پاسخ پشیمان کننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/akhbarefori/652790" target="_blank">📅 12:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652789">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-5PvryRBypXN69cF3LFfKCW2bVZNiRI2JlUYrlJfagQLq83IENsyGh-A9RXdm-GbAGVxr8PJ0Sz22MJlBLdRvKErI5DclOiKkQ1FpAG40TB7aS1swXJR2oUPLuu8EO3_OEv3P_BsfC3pipARUH0mH67bQ9nQBS_DXjDKb_YlyT3V7_J_hI0-vTEpAk4rBFFiA-TSMJv2SKiv4Ny42Q2JzStH-s9TFYCWyWbpQDKjTQb8Kmm4cfTGLHBNTPCw84P_GadJxE9dB_r6qdzm6z83hBjKKD3tLkroa2aLMv12gJUfNcBjLfoPs8h-DLG4ALB6XAI-Z7IbPvHm0uLD0Te1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بار سنگین تنگه هرمز روی دوش اروپا؛ کالاس: لطفاً توافق کنید
🔹
با ادامه بسته ماندن تنگه هرمز و تشدید فشار بر اقتصاد جهانی، اتحادیه اروپا از ایران و آمریکا خواسته است تا در مرحله اول بر سر بازگشایی تنگه هرمز با یکدیگر به توافق برسند.
🔹
مسئول سیاست خارجی اتحادیه اروپا کایا کالاس در مصاحبه روز دوشنبه خود با خبرنگاران، هراسان از ادامه بسته ماندن تنگه هرمز، افزوده که: «ما واقعاً تلاش می‌کنیم تا همه بازیگران را قانع کنیم که آزادی دریانوردی باید رعایت شود، زیرا تنگه‌های دیگری در جهان می‌بینیم که ممکن است به روشی مشابه ابزاری شوند و این به نفع هیچ‌کس در جهان نیست.»
🔹
کالاس همچنین در بخش دیگری از سخنان خود، «بن‌بست» در مذاکرات بین تهران و واشنگتن را مشکلی بین این دو طرف دانسته و مدعی شده که اتحادیه اروپا «اهرم فشار چندانی» روی هیچ یک از طرفین مذاکره ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/akhbarefori/652789" target="_blank">📅 12:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652788">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fhu0BE60zLWg7Ty7D3Y2ZQ-8ijPpGHL5Fuqw0kZJfouaZdzE196pppLvpB9nEVPMZCOIUz_awY09ddn-nJOjLrmbIFV9ffzEXXhGMuKq33nq2QZBCU6ZIFxKUDMLTY39ST8akNKLNDC5ycMIpCDFkwTTenfGgEba59uUi-uU-5EX8ayguzhZ42rTOvB_HxFpLy9BMVodQMX7IkeJlKVVWmxCD9FZuWHDm8pKmxMzBSP6SM7ooOOTydBmz3AkUjO-T03K0j0Hrid5oHv28QMC8FZrSn21mLktsjhyI8Zoa-xv7WdpPLRbHvobKneAb9Nsou5TIrzdcP9Ago8ATVL7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چالش ۷ روز بدون پلاستیک
🔹
یک هفته برای تغییر، یک قدم برای زمین   شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/akhbarefori/652788" target="_blank">📅 12:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652787">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
العربیه: ده‌ها اسرائیلی تندرو وارد خاک سوریه شدند
🔹
شبکه خبری العربیه از ورود غیرقانونی ده‌ها صهیونیست تندرو به خاک سوریه خبر داد.
🔹
ارتش رژیم اسرائیل گفته است که این اقدام، نظامیان و غیرنظامیان را در معرض خطر قرار می دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/akhbarefori/652787" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652786">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4279769e28.mp4?token=TM04tUWVbz7AkmEAKXQ_1pPDRFbwDsC5b6ao6SP4MmhEHullPoho3xUTWts0QGurVdyOskm20hJQ2Ehl7quGXKuD2ndlmRmMhIGZJBWPXXiYkgVDOPKbcQJIsgNkJhU701UodAo5PJ2yPvTMhfZWLT7ndDKxCpCthY6qhl0VcYIsWAgqRxhqqKQYX4xu-rDUFN-gaere6niPuCAQInIJu8AITa_XK0nvt5z_Lhccpmf52glCtLnutsnKSduFpjnZgN6w_GnafQXAAnrG9tho-2GGSvd91pjA3QQWUQI4AP42dl0G3SNTnsPKnqCbZDn4XHDU-YoJVytfHV-kCadL3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4279769e28.mp4?token=TM04tUWVbz7AkmEAKXQ_1pPDRFbwDsC5b6ao6SP4MmhEHullPoho3xUTWts0QGurVdyOskm20hJQ2Ehl7quGXKuD2ndlmRmMhIGZJBWPXXiYkgVDOPKbcQJIsgNkJhU701UodAo5PJ2yPvTMhfZWLT7ndDKxCpCthY6qhl0VcYIsWAgqRxhqqKQYX4xu-rDUFN-gaere6niPuCAQInIJu8AITa_XK0nvt5z_Lhccpmf52glCtLnutsnKSduFpjnZgN6w_GnafQXAAnrG9tho-2GGSvd91pjA3QQWUQI4AP42dl0G3SNTnsPKnqCbZDn4XHDU-YoJVytfHV-kCadL3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید دشمن را عقب بزنیم؛ بازخوانی بیانات رهبر شهید انقلاب دربارهٔ جنگ اقتصادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/akhbarefori/652786" target="_blank">📅 12:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652785">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انتخابات هیات رییسه مجلس سه شنبه آینده برگزار می شود
علیرضا سلیمی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
انتخابات هیات رییسه مجلس  به موقع روز سه شنبه هفته آینده برگزار می شود و جزییات برگزاری آن اعلام می شود.
به هیچ وجهی این انتخابات تعویق نخواهدیافت.
@TV_Fori</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/akhbarefori/652785" target="_blank">📅 12:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652784">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju3hxiqn475RcHHPCYL1LyEyAdcHGXoY-AghPJNhuqxw-gnn-0GXew2wRYJY8MqYq3WUSRXG66VXnJblynVW4CqsZUdNyxEHgTGeyRfjFTijOhmY8Nn0kar1ZgFUzGWm7VCFPf4LS0qNiOUMDItzUJqGtiUwZiezW6SgIL3k3JfmY6d1N4iYTpGtkkTNNXAcips5DY0jcyvMLXkTFndVPTzXSAhDj_HhSagKjBOeuu89naAQEbr4ftzbTB-1NA-vHpTWBBStwfA9uY5VhTcqbPth6iIeGYoX6riMlLyJcvi_2YRJ7jp6UDj64mb5YvCrSfbIF99_Ix_VWy9Z87XWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
*جهش بی‌سابقه نسبت کفایت سرمایه بانک اقتصادنوین*
🔹
نسبت کفایت سرمایه بانک اقتصادنوین دو رقمی شد و به 10.55 رسید.
▫️
به گزارش روابط عمومی بانک اقتصادنوین، این بانک پیش از این موفق شد با ثبت افزایش سرمایه 135درصدی از محل مازاد تجدید ارزیابی دارایی‌ها، سرمایه خود را از مبلغ 103.254 میلیارد ریال به مبلغ 243.145 میلیارد ریال افزایش دهد.
🔹
برای کسب اطلاعات بیشتر روی لینک زیر کلیک کنید:
🔗
https://www.enbank.ir/s/mfa2Zu
‏
🔗
www.enbank.ir
▫️
02162740</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/akhbarefori/652784" target="_blank">📅 12:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/214629aa2f.mp4?token=lB7rTucr_MCjSUBDarsJ_GK_94ms18r5Uer5KyfOn8v0JqsZjoBLRa6NtLRkDtjbUNdBcVXtiW1_TqCk6-taPVi7_clJQyUI77lLkn-07imj797vbZQ8mVsVQHjFgy9SdLHdh4Tsq-uSp9V15cVCwcHw1I7UF3ILQ-XjUggJGCEhTh_HDed8ozdXg_-EaOtzMny6KXrqNrpiKuaaiEKmqdjViQu-9xMrQJBkIv-3Hv89xhJACBXrvzfZJVKyVjesfTROzAd_3_-71MiKGFM2ELeIPqy9hQj1EL9XstC0OL5oG7ttzMlWjdswzlsdktC-gdQHD7w91sCqUh-gM54WCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/214629aa2f.mp4?token=lB7rTucr_MCjSUBDarsJ_GK_94ms18r5Uer5KyfOn8v0JqsZjoBLRa6NtLRkDtjbUNdBcVXtiW1_TqCk6-taPVi7_clJQyUI77lLkn-07imj797vbZQ8mVsVQHjFgy9SdLHdh4Tsq-uSp9V15cVCwcHw1I7UF3ILQ-XjUggJGCEhTh_HDed8ozdXg_-EaOtzMny6KXrqNrpiKuaaiEKmqdjViQu-9xMrQJBkIv-3Hv89xhJACBXrvzfZJVKyVjesfTROzAd_3_-71MiKGFM2ELeIPqy9hQj1EL9XstC0OL5oG7ttzMlWjdswzlsdktC-gdQHD7w91sCqUh-gM54WCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رابرت گیتس: نتانیاهو سال‌هاست آمریکا را به حمله به ایران وسوسه می‌کند
🔹
وزیر دفاع سابق آمریکا می‌گوید که نخست‌وزیر رژیم صهیونیستی از سال‌ها پیش ادعای ضعیف‌شدن ایران را زیر گوش واشنگتن می‌خواند تا آن را ترغیب به اقدام نظامی کند.
🔹
گیتس در مصاحبه با برنامه «فِیس دِ نِیشن» در شبکه «سی‌بی‌اس» گفت: «او (نتانیاهو) در ماه جولای سال ۲۰۰۹ به من گفت که رژیم ایران شکننده است و با اولین حمله فرو خواهد پاشید».
🔹
وی در این‌باره توضیح داد: «من به او گفتم که کاملاً اشتباه می‌کند - اینکه او مقاومت ایرانی‌ها را دست کم می‌گیرد. این همان چیزی است که او سال‌هاست سعی در قبولاندن آن دارد».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/akhbarefori/652783" target="_blank">📅 12:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn50XohMjBPecUJe-HRqicUWu2oucC92a6h28Dk1b0ygzaeaVOecX3AV2oHfk_PkSfHyZ2ZkBvjj1CmZFBxjdsWzp9H-n-k4n8gq24q3P8EXPMNqD6asT3BqYksGiTCe5S8UOXrLK6Z-7TIBzzVbdzFkCshNc7jlGmVHIz6pSh0UArkXr34-I1sMtpRzSdGXXeV3Z01qENKPfVpZJdklTS1boTqBa6n6Xfecicq4nijfCkjkCx9PgOd1lwmc2y4Qm3ZWPMlxDeaCCYt9hXyzyRlsgE_ZT-DOAS2KiqqIy_cKyuuuqIB-D79Ftw7PGDG4ISDs7TlzxLypxKiWM_6Ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه صهیونیستی: آمریکا موافق حملات اسرائیل در لبنان است
🔹
آمریکا اخیرا توافق آتش‌بس را در لبنان تمدید کرد؛ اقدامی که به گفته کارشناسان صرفا مجوزی از سوی واشنگتن برای کشتار هر چه بیشتر مردم لبنان است.
🔹
روزنامه «اسرائیل هیوم» امروز فاش کرد که تمدید ۴۵ روزه آتش‌بس در لبنان توسط آمریکا، به منزله موافقت رسمی و خاموش با عملیاتهای اسرائیل است.
🔹
این روزنامه با اشاره به اینکه آمریکا با این اقدام، به اسرائیل آزادی عمل می‌دهد تا دست به عملیاتهای بیشتری در لبنان بزند، نوشت،
🔹
واشنگتن و تل‌آویو به صورت پنهانی موافقت کرده‌اند که عملیاتهای نظامی رژیم در لبنان، تحت پوشش «آتش‌بس فعال» ادامه پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/akhbarefori/652782" target="_blank">📅 12:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652781">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQZYctZnETuCJ8xgnA1iGMldwyfAoBzo8v8jtermvYKRmJ8oNn_5IhNJwb64CXDzaCQR1ojZRIpW5PJoas-trdWrvlRM8uPErXoyYmD6KGb6ub2Lqn9Y2rrt-AnOL2Cl1CyaG9SOs8aw_6PhL9iD00bntTV_NTd98SeimkiVRt_V7UChnDXg1VPEc_uYtLZBuSJZUA8BI54rXtjgtWcDYGd4UB3DmNKXxzjkb_AJRzGcfRGLkegHxvnjyNFZ_WrjXhOXZgve-jp6t3X7-LAKp95YabbSzGZXfZudl1ubJ6wtb6CZeOBSdoaZCI5b2hWcpEyLyVj3PYxGfWinUd55eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: اگر در شرایط جنگی هستیم، باید آرایش جنگی بگیریم
🔹
مسعود پزشکیان رییس جمهور در گردهمایی روابط عمومی‌های دستگاه‌های اجرایی، با اشاره به جنگ تحمیلی سوم: دشمن نا جوانمردانه رهبر، فرماندهان، وزرا و دانش آموزان و مردم ما را ترور کردند.
🔹
اگر در شرایط جنگی هستیم، باید آرایش جنگی بگیریم. مراکز متعددی از جمله نیروگاه‌ها، صنایع پتروشیمی و فولاد مبارکه هدف قرار گرفته‌اند. نباید به دروغ ادعا کنیم که هیچ مشکلی نداریم و دشمن در حال نابودی است. همچنین مسئولان باید صادقانه با جامعه سخن بگویند و از ارائه تصویر کاذب مبنی بر شکوفایی مطلق ما در برابر نابودی طرف مقابل پرهیز کنند. ما نیز با چالش‌های جدی مواجه هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/652781" target="_blank">📅 12:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652780">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
۱۶ شهید جامعه پرستاری در ۲ جنگ اخیر
🔹
رئیس سازمان نظام پرستاری: جامعه پرستاری در ایام جنگ رمضان ۱۱ شهید و در جنگ ۱۲ روزه ۵ شهید تقدیم کشور کرده است.
🔹
کمترین میزان ترک خدمت پرستاری را در ایام جنگ داشتیم و حتی از شرایط عادی نیز ترک خدمت کمتر بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/akhbarefori/652780" target="_blank">📅 11:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای شبکه سی‌ان‌ان: پنتاگون فهرستی از اهداف برای حمله به ایران در صورت صدور دستور ترامپ آماده کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/akhbarefori/652779" target="_blank">📅 11:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaf462542.mp4?token=bgx4OFP7qPWis8n2MyUanYVYJypw-TXcqRJLAw4tWuvbWhIHb8QvRoEwRFI_9TWSJuAz5XunQLGBqeRZkvdm2zzH2WSpoIKYSDc1QPG0CG8WVNugIE6kUOpxHFEKA0-th73e_S5jCnJawOwpE3hyS3Tj8MugnkRjvqVmcxR-rq7hsNEWi2W_qabsWb0dCAD2AIElTWd9_HT0wzRrL5r5rYUVKT2gM5aoUisyyaMdBiqXvmL8EczUgnmjc7-HaPhRhFo2zCkgtMoCxeDEn8i_nLa0iNoTqm8e5HkYr-8BrAzBfA3UYk65rGyFJ4hOahlIWZoiBQyUUA95s3ZBd_CYKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaf462542.mp4?token=bgx4OFP7qPWis8n2MyUanYVYJypw-TXcqRJLAw4tWuvbWhIHb8QvRoEwRFI_9TWSJuAz5XunQLGBqeRZkvdm2zzH2WSpoIKYSDc1QPG0CG8WVNugIE6kUOpxHFEKA0-th73e_S5jCnJawOwpE3hyS3Tj8MugnkRjvqVmcxR-rq7hsNEWi2W_qabsWb0dCAD2AIElTWd9_HT0wzRrL5r5rYUVKT2gM5aoUisyyaMdBiqXvmL8EczUgnmjc7-HaPhRhFo2zCkgtMoCxeDEn8i_nLa0iNoTqm8e5HkYr-8BrAzBfA3UYk65rGyFJ4hOahlIWZoiBQyUUA95s3ZBd_CYKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
در روز ارتباطات یادی کنیم از روزنامه نگاری که صدایش در راه بیان حقیقت، خاموش شد...
🖊
میرزاده‌ عشقی
نسخه کامل را اینجا ببینید
👇
https://youtu.be/7otmLqnDYEk?si=pbC1vgSrU7VeGkQ0
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/akhbarefori/652778" target="_blank">📅 11:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSwKUiMSpELt5UpfzxqnMh9toX0HV8AzLJttcXer4yIdQAQ3GSGTf40xMPVjMIsPdNLH47pINsrxOaxmAMKQWyBt2woN6nWl9WhYOs7KAtqhcIv4KT__TUoqb2OyrDE6kylN0FjiTyBxhDvJYhuWyNuieEyPqa6HMlPEPRrrZyQrSK4z68aA7CMOYr6Z4HEuMDgH_3yTNweh_isdo8iO0Hpe3s8hUzLh8XoxEHha-7yYjcc_4TOoSOdaz8W7vG5YXRFBFV0hiLc2kdrUY7l1AtdwRzZAfuie_mEtyQfUVPhSjN9lwMa7nbP8YG10iAG418IxRCBZSEIs2OIwEisByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضرتی: گشایش اینترنت بین الملل سیاست قطعی دولت است
🔹
رئیس شورای اطلاع رسانی دولت تأکید کرد: سیاست قطعی و بدون عقب نشینی دولت گشایش اینترنت بین‌الملل و رفع فیلترینگ است و تا کنون سه جلسه از سوی شورای راهبردی و سیاست‌گذاری اینترنت کشور توسط معاون اول رئیس‌جمهور برگزار شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/akhbarefori/652777" target="_blank">📅 11:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بازداشت ۱۰۰ نفر از فعالان ناوگان صمود توسط ارتش رژیم صهیونیستی
🔹
منابع عبری اعلام کردند نیروی دریایی اسرائیل ۱۰۰ نفر از شرکت کنندگان در ناوگان صمود که از ترکیه به سمت غزه در حرکت بود را بازداشت کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/akhbarefori/652776" target="_blank">📅 11:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDac-0GN3klGEuCxkxbfUtBtZRvALhs7nxOI3ynBImKXVaIkniweiYh8c0cy3FeDUHUSglxHge5C0yJW44gqJn2wf0VNr4Ebr1Rh3h6gqUggHkavGDGO5UzmyjLUxLmoxW3VoCGXpkTmOz-SrOXazoOdShUmPzpX-0oVa5SVJXS-TCYcoonCtnhypW2fCEM0oHMpQu45YvsQ_IPGlp1BcDQGroAoaz7-FzCx6KZ_ZluZn2pmLjwD_EwfBWYlbMzX2OlYfhbQOu6pbWr5ULOYly5GtB4eU6KjtONxP-akraNlVsihbN3iGsZ6Hz8qllpL9FSNIM4pQM6gSmBp_NbIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارسال پیشنهاد بازبینی‌شده ایران به آمریکا
🔹
آخرین پیشنهاد ایران برای پایان جنگ، یکشنبه شب به طرف آمریکایی ارسال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/akhbarefori/652775" target="_blank">📅 11:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028a958134.mp4?token=U5cWGEEJ8d1cfmaedbRgQOxJxaSPHEP3yauB4qPR7hnqhV_NaewEDAu7CPRJ6sGIQoQSzHtZBBZxe-Qw9M0nnPoGNZWJrJDNTQPjhgP_i1uQH0EE8Sav2UQ9ay_pDQSEpCKfpUyMvXWVCD4DTiIsmMhSB6nOgTdx3jMGrmCShJV_oVg2WTYc9oXFCw2MD7YsfJHQDqTiLIzo04tjtawzFCZo76YiFj_qJNRt5zoPSbGjtdG7COcqEDQOhEq9SjO6WaXNUTI2D1hRP_XlpI-n3y9HttzoXDfYXPqtUwcYkk4a1CBHNoLfQ0-zA_K3PT5YBHUCH1q2kKH4-VlWpuSLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028a958134.mp4?token=U5cWGEEJ8d1cfmaedbRgQOxJxaSPHEP3yauB4qPR7hnqhV_NaewEDAu7CPRJ6sGIQoQSzHtZBBZxe-Qw9M0nnPoGNZWJrJDNTQPjhgP_i1uQH0EE8Sav2UQ9ay_pDQSEpCKfpUyMvXWVCD4DTiIsmMhSB6nOgTdx3jMGrmCShJV_oVg2WTYc9oXFCw2MD7YsfJHQDqTiLIzo04tjtawzFCZo76YiFj_qJNRt5zoPSbGjtdG7COcqEDQOhEq9SjO6WaXNUTI2D1hRP_XlpI-n3y9HttzoXDfYXPqtUwcYkk4a1CBHNoLfQ0-zA_K3PT5YBHUCH1q2kKH4-VlWpuSLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی در پاسخ به سوال خبرنگار خبرفوری: با بدگمانی عمیق و سوءظن شدید، در هر روند دیپلماتیکی برای صیانت از منافع ملی ایران مشارکت کردیم
🔹
سخنگوی وزارت امور خارجه در پاسخ به این پرسش که «در مورد احتمال خیانت چندباره آمریکا به دیپلماسی، اگر این بار هم در حین مذاکرات، ایران مورد تجاوز قرار بگیرد، چشم‌انداز آینده دیپلماسی و گفت‌وگوها در دنیا چه خواهد بود؟» گفت:
🔹
به اندازه کافی به دیپلماسی خیانت کردند و نتیجه‌اش را هم در حال مشاهده هستند. آمریکا طرفی است که الان به هیچ عنوان به‌عنوان یک طرف معتبر تلقی نمی‌شود.
🔹
در سطح بین‌المللی، دیدگاه‌های متناقض و اظهار نظرهای ضدونقیض، همه این‌ها باعث شده که هیچ کشوری در دنیا ادعاها و ژست‌های آمریکا در رابطه با دیپلماسی و مذاکره را جدی نگیرد.
🔹
ما هم به نوبه خودمان با بدگمانی عمیق و با سوءظن شدید، در هر روند دیپلماتیکی مشارکت کردیم برای صیانت از منافع ملی ایران.
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/akhbarefori/652774" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475c2e1a71.mov?token=rnD-lDjGjksgkc-ouutiVKiCaB2e4WFGE4tGUYUSD0CDEplCMw-XXQvvv8-8jpKP49mI4eVdsqURGdYhNWyZHwLSyzSyzaD6kngItW6SHqMsiUnwxVyLcqeB1wJikpsB_quFjqFg50sah-BrRLwoxStP1VDD_sU4ug1fR2Ki4pfjUIWvBUwoixm_2tfhNLxVfHwv3wK89zy3UQmW2YlUN0jZDTQb3qUAXPF43NO-kKGx6qjSOPaZeoQETKC91cOoB4EK65YWb3Xx11PoLFCbjvPdrUsRVLKPw7G2nKTUGqTU2RDmhi0fW4LyuAiHTkVJ6eGgSiaApE2PQKphia7o8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475c2e1a71.mov?token=rnD-lDjGjksgkc-ouutiVKiCaB2e4WFGE4tGUYUSD0CDEplCMw-XXQvvv8-8jpKP49mI4eVdsqURGdYhNWyZHwLSyzSyzaD6kngItW6SHqMsiUnwxVyLcqeB1wJikpsB_quFjqFg50sah-BrRLwoxStP1VDD_sU4ug1fR2Ki4pfjUIWvBUwoixm_2tfhNLxVfHwv3wK89zy3UQmW2YlUN0jZDTQb3qUAXPF43NO-kKGx6qjSOPaZeoQETKC91cOoB4EK65YWb3Xx11PoLFCbjvPdrUsRVLKPw7G2nKTUGqTU2RDmhi0fW4LyuAiHTkVJ6eGgSiaApE2PQKphia7o8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی شهرداری تهران به خبر باشگاه خبرنگاران
🔹
سخنگوی شهرداری تهران: به دلیل اینکه دیروز جلسه شورای شهر برگزار نشد، با تصمیم داخلی شهرداری، اتوبوس و مترو رایگان تا صبح سه‌شنبه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/652773" target="_blank">📅 11:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4650970567.mp4?token=HI9svKPar3l9y7BQuyJR8z8GlDz1OreEbDFDZmYTNPj2gyZr8c3wt8T77fCeFFKMK6qFIJzb_KI3RHLaRgEGC8rL3NlBsbXOvHyRo42gf6URgtSb5QaKbtOiV390jp4AmQ1xxn5GP2msixP-pLKQu8FcT-Tb_AIxZFopnSkr5rA_ERzDw3r_k_bTCvDylmsnqeyqKthAr9X2KYCl5eHRAmJld3gt2RM0lr-AaxW1Vk4pUPkMpveb_q-docq8i0vLa1arHkh9BjPJkAsJFA12AoRiHgdDfI4D4IkW5_HKU6RZ4dlckA79QkWJnKNNIvBpxhpZT3o5LvSfflIf3fpo3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4650970567.mp4?token=HI9svKPar3l9y7BQuyJR8z8GlDz1OreEbDFDZmYTNPj2gyZr8c3wt8T77fCeFFKMK6qFIJzb_KI3RHLaRgEGC8rL3NlBsbXOvHyRo42gf6URgtSb5QaKbtOiV390jp4AmQ1xxn5GP2msixP-pLKQu8FcT-Tb_AIxZFopnSkr5rA_ERzDw3r_k_bTCvDylmsnqeyqKthAr9X2KYCl5eHRAmJld3gt2RM0lr-AaxW1Vk4pUPkMpveb_q-docq8i0vLa1arHkh9BjPJkAsJFA12AoRiHgdDfI4D4IkW5_HKU6RZ4dlckA79QkWJnKNNIvBpxhpZT3o5LvSfflIf3fpo3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: تمرکز ما بر پایان جنگ است
🔹
سخنگوی وزارت امور خارجه: قرار نیست از حقوق خود در هسته ای عدول کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/652772" target="_blank">📅 11:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: در صورت وقوع جنگ، نیروهای مسلح ما حتماً سورپرایز‌های جدیدی برای دشمن خواهند داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/akhbarefori/652771" target="_blank">📅 11:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
بقایی: با فرهنگ و تاریخ ایران سر جنگ داشتند/ ۱۰۰ نقطه در کردستان هدف قرار گرفته
🔹
در حمله به کشور ۱۰۰ نقطه در کردستان مورد هدف قرار گرفت.
🔹
سفر من هم به عنوان یک شهروند به این استان برای تقدیر از مردم کردستان بود و همچنین بازدید از نقاطی که مورد آسیب قرار گرفت. از جمله عمارت عاصف و خانه کرد که در جریان تهاجم رژیم صهیونیستی هر دو مجموعه آسیب دیدند.
🔹
یکی از اهداف حمله دشمن اماکن تاریخ بود و باید این‌ها را مستند‌سازی کرد تا به مردم یادآوری شود این جنگ فراتر از یک جنگ متعارف بود و با فرهنگ و تاریخ و داشته‌های ایران سر جنگ داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/akhbarefori/652770" target="_blank">📅 11:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
توضیحات سخنگوی وزارت خارجه دربارهٔ درخواست پرداخت غرامت به ایران
🔹
در زمینه خسارت ارزیابی‌های دقیقی صورت گرفته و همچنان نیز در دست بررسی است چون خیلی از موارد با گذر زمان مشخص می‌شود.
🔹
این خسارت‌ها بعضا قابل احصا نیست مگر می‌توان آسیب به اشیا فرهنگی و تاریخی را با عدد و رقم مستند کرد؟
🔹
اما در مورد بحث پیگیری خسارت، این یک خواسته منطقی است چون این یک جنگ غیرقانونی است و طرف‌هایی که این جنایت‌ها را علیه ایران مرتکب شدند باید پاسخو باشند و درهر فرصتی پیگیر آن هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/akhbarefori/652769" target="_blank">📅 11:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca620cb48e.mp4?token=e3wiS0CxQzwSrP8Gcglzv8yWbYopm5chrrwaZIDiZNqMu5imnVYmiKSyHuKEmUpuR5wIQWDC9zvt8-eG4VfFXvkoav-ZkkO-Q6QWfoLzkQbtT1RP3XpnZ3F-_EtQj7zBOr41E7kn3933OsRJ9r-bPKx1dHAPgW9FRaypGPBhmqm_gXvQY1UOIC5wtOumfvNRo-Eg4Bff16Rl3rq8pcaGr3XNCP3omib-4_c4gRCQzJqGVWM3PqjVob91aQwuqRrN2wgNudb2TJotUGBr5_Qom07BPvrrbwWqy_9viLvBDwdYTtaICpDWuq2izIF-ewwgdKwwC3nFspw5dtY_i1SYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca620cb48e.mp4?token=e3wiS0CxQzwSrP8Gcglzv8yWbYopm5chrrwaZIDiZNqMu5imnVYmiKSyHuKEmUpuR5wIQWDC9zvt8-eG4VfFXvkoav-ZkkO-Q6QWfoLzkQbtT1RP3XpnZ3F-_EtQj7zBOr41E7kn3933OsRJ9r-bPKx1dHAPgW9FRaypGPBhmqm_gXvQY1UOIC5wtOumfvNRo-Eg4Bff16Rl3rq8pcaGr3XNCP3omib-4_c4gRCQzJqGVWM3PqjVob91aQwuqRrN2wgNudb2TJotUGBr5_Qom07BPvrrbwWqy_9viLvBDwdYTtaICpDWuq2izIF-ewwgdKwwC3nFspw5dtY_i1SYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ سخنگوی وزارت امور خارجه به سوال خبرنگار در مورد تهدیدهای ترامپ: نگران نباشید؛ خوب بلدیم چگونه جواب بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/akhbarefori/652768" target="_blank">📅 11:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: در تماس مستمر با کشورهای منطقه همچون با عربستان و قطر هستیم
🔹
اولین سفر وزیر امور خارجه بعد از جنگ تحمیلی به یک کشور منطقه یعنی عمان بود.
🔹
در تماس مستمر با کشورهای منطقه همچون با عربستان و قطر هستیم.
🔹
مصمم هستیم که روابطمان با کشورهای منطقه را بر اساس احترام به حاکیمت ملی یکدیگر ادامه بدهیم.
🔹
متوجه هستیم که به‌دلیل اقدامات آمریکا و برخی کشورهای منطقه با طرف متجاوز روابط ایران با برخی کشورهای منطقه دچار زخم‌هایی شد. باید این زخم‌ها را ترمیم کرد چون ما همسایگان ابدی هستیم و هرگونه اختلاف منجر به بهره برداری رژیم صهیونیستی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/akhbarefori/652767" target="_blank">📅 11:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی گزارش دادند: عملیات کنترل و تسلط بر ناوگان دریایی که از مبدأ ترکیه به سمت غزه حرکت کرده بود، آغاز شد
🔹
کانال ۱۲ رژیم صهیونیستی گزارش داد: یگان ۱۳ کماندوی دریایی (شایِتِت ۱۳) عملیات تصرف «ناوگان پایداری» را آغاز کرد.
🔹
یگان‌های نخبه و ویژه نیروی دریایی، عملیات تصرف «ناوگان پایداری» را آغاز کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/akhbarefori/652766" target="_blank">📅 11:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سخنگوی‌ وزارت خارجه: ما با چین در رابطه با موضوع هسته‌ای اختلاف نظری نداریم
🔹
ما با چین در رابطه با موضوع هسته‌ای اختلاف نظری نداریم و ایران دنبال سلاح هسته‌ای نبوده است.
🔹
ایران باعث شکل‌گیری این وضعیت در تنگه هرمز نشده است.
🔹
معتقدیم در تنگه هرمز باید به صورت ایمن زمینه کشتیرانی بین‌المللی فراهم شود. ما هم دلیلمان برای ایجاد سازوکارهای ایمن در تنگه هرمز همین است که از اتفاقات ماه‌های اخیر جلوگیری کنیم.
🔹
طرفی که به سبک دزدان دریایی به کشتی‌های حامل کالا حمله می‌کند آمریکا است و چین هم حق دارد در این زمینه از آمریکا مطالبه بکند تا اقداماتش علیه ایمنی دریانوردی را متوقف کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/652765" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه:
🔹
اقدام کویت در بازداشت ایرانیان غیر قابل قبول بود.
🔹
فضا سازی برای ما قابل درک نیست؛ روابط بین دو کشور اقتضا می‌کند که اگر مسئله‌ای وجود دارد هم از مراجع دیپلماتیک پیگیری شود.
🔹
اینکه به شناور مرزبانی حمله کنند و مطالبی را مطرح کنند با عرف دیپلماتیک هم خوانی ندارد.
🔹
از طرف دیپلماتیک انتظار داریم زمینه آزادی شهروندان ایرانی را فراهم کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/akhbarefori/652764" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: همه تحرکات را رصد کرده و برای هر احتمالی آماده هستیم/خوب بلدیم چطور بزنیم
🔹
یکی از ابزارهای آمریکا تهدید و فشار اقتصادی بوده اما دیدند که با این ابزارها نمی‌توانند ما را از پیگیری حقوق و منافع ایران منصرف کنند.
🔹
ما همه تحرکات را رصد کرده و برای هر احتمالی آماده هستیم و در میز مذاکره هم فارغ از این تهدید ها کار خودمان را برای پیگیری حقوق ملت ایران پیش می‌بریم
🔹
در مورد تهدید‌ها هم ما خوب بلدیم چگونه پاسخ بدهیم.
🔹
این شب‌ها مردم هم در میادین تهران هم می‌گویند که تو رستم تهمتنی، خوب بلدیم چطور بزنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/akhbarefori/652763" target="_blank">📅 11:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: آزاد شدن دارایی‌های ایران را برخی شرط مذاکره دانسته‌اند اما این مطالبه ما است
🔹
این مطالبه حقی است‌؛ طی سال‌ها اموال ایران مسدود شده است.
🔹
یا موضوع رفع تحریم‌ها یکی از مطالبات ایران است که در هر مذاکره‌ای با جدیت مورد پیگیری قرار می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/652762" target="_blank">📅 11:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojY4kQnkk65xHt_nWT-3zLhTAptgNWtS8v1gB33MY2IJ0K2pthsi0Y2Piw8diH7BgI4B1RWrN8Fk7nta79pYKVrU7NFH792xKleecMoP9eAc8gF9_VbtS68qX5TROo6J1VyM2m93XBPfZpuv0tI0qR4JqFpLUvcs28ZDroaLFyO4DNlzbjbJQ_hkKAaUrUtoCMvbKjMUeYm1pmGnf72bo2QhKj0MFUIoF0Tx5NFARbh5zvu4RuY-CmsGtIumy9jqf1r7UpHvHU9pKPd8cDJegovTpMzHw3mZ9kkyhLoxnrCeR3ZXm0MenuVceoLlANVJBdbMgYPyhM6ggeek-UKRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ik7EtWfhDOR0lV7RIYQpuGZRLE1IWDS5z55ddy7_FUSEArtodsffZsk_aww7c0-BMnBRy8YqO8Hna3resVXC5ep7N7t5WO5gI9vUJEdOOALmU5t91dEJG-sp-wgM4-DCZ4r50jUvRMjU1OIRPv0hlrsGge7z4eDr4VUgvf28sQ7TaTgizsUjc-Mrf753qvkG4Y-9nAGHz9DWN10dGJCKJZRnL55jcFKwnwOZhT051RnVkUSNiHQ8qxMSM4vYB6dEeb_jQa1RAeJfYADU-hahKcRO1PxAh3faEsPJGUQjZQpg8TmGshU3ildxSZItkWeIqmwUrKDtI2mlsPBYksDBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDGRs8UEAHTrhnMk1m3Xivh4qdX_EtWzJnJ8VfbggtMlMO5Ls9TjDqvViJE1AHGO1SCDeSX1-OIKAs1-k1TPeKF4LgbeqD4IhDHYgRzR4yo-wQwWv0Uipo6noxVh7cPrKx55NGNGDAsr2KoP85luaW98YUnz4neRUj3MEKXPKHB3hVfK5HhhE3tIs2Niv0DtBBNykSv8osknPgcdX7uWsMk61GdYVAoA-8iIFL_O6PKtcE18nbUeET8M9FJCC3Edg5fh948ZixuMCkIGhWUn-OA_mMIZiNinE3lHNsOlLEGYwREdYwbB_7rfPzUk9TX7FFiricTxBklogHnvRgdZsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سلاح در دستان ایرانیان؛ تصویری که سی‌ان‌ان را حیرت‌زده کرد
🔹
در حالی که دونالد ترامپ همچنان با زبان تهدید با ایرانیان سخن می‌گوید، مردم ایران در رسانه ملی و در تجمعات شبانه خود، با در دست گرفتن سلاح، آمادگی خود را به رخ دشمن می‌کشند؛ موضوعی که از چشم رسانه‌های غربی دور نمانده است.
🔹
در گزارش خود از تهرانی می‌گوید که پس از تاریکی هوا میزبان «هزاران ایرانی» است که برای شرکت در تجمعات به خیابان‌ها آمده‌اند. این خبرنگار از اصطلاح «دریایی از پرچم‌ها» برای نشان دادن عظمت این حضور استفاده می‌کند.
🔹
وی در ادامه اذعان می‌کند که مردم حاضر در تجمعات، حتی در تجمعات، فریاد «مرگ بر آمریکا» سر می‌دهند و همگی آماده فدا کردن جان خود برای ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/akhbarefori/652759" target="_blank">📅 11:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ics59HBQO4O0YKm0kO9Omqkgt7PmEwppAoo_yECzEkACpKCbQ5Ee3VdJBN23JgsNlPk18bl8ma3bWvHPo0-iSOtEpeup3spjzDTBpK11gCs5B4uRATccLr8kOTmpSHI28nZjMYgHams9ZcT791LPESSZbzSGffxvUg1xQQQEvImaKhvEX89RQYyp5FeNVmkhthv4m7mG5UlNWLVvYAD1PCVKHxhUKWDNBVLi4Bm2k-paTPYikiNVNRv3Rk3CIBgapPqNPoI4rFGplzOKqTP41FjQD8_s2omOGtueb6spKayTT6mKoliy_k02EDF8aZrjvyLvK2rqeY4r86NMbb8JTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکمیلی /
🔹
سخنگوی دستگاه دیپلماسی درباره پیش نویس قطعنامه علیه ایران در شورای امنیت گفت: این قطعنامه هم براساس الگوی دو قطعنامه پیشین از جمله قطعنامه اول طراحی شده است. نادیده گرفتن واقعیت‌های کاملا واضح اینکه وضعیت ناامنی در تنگه هرمز و خلیج فارس ناشی از تجاوز آمریکا و رژیم صهیونیستی است. شورای امنیت نمی تواند این واقعیت را نادیده بگیرد و ایران را به ناامن سازی متهم کند. در تماس مستمر با کشورهای عضو هستیم هم در نیویورک و هم دوجانبه و با چین و روسیه در ارتباط هستیم.
🔹
چین و روسیه می‌دانند عامل اصلی ناامنی در دریاها و تهدید تجارت آزاد، آمریکاست. جامعه جهانی به شمول شورای امنیت اگر می‌‌خواهد اقدام مسئولانه‌ای انجام دهد باید آمریکا و رژیم صهیونیستی را به خاطر شروع تجاوز نظامی محکوم کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/akhbarefori/652758" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_haiVTMsK6Uc1jLJgsWj2xsZ1LdpLg4kQsDKsvHh56zNgZcJEyy3eu-PMc97bLns0bL09J58Ang7XtM7Ls8xw048E6ZF21zHKO0uktLEuS9snMkCNnySCQAMtA88d9Mw55VMWqTzkIOiR_P0wyZ-XBXJYRwtP8L4z4JWyzKMW9JfQPLnGPYkn5vwmLcMrMvdfItol1txVZfreozSsXZzhPxGD_2R1CcxMdwRcx6xoFFr-nWIWoRDtvNeurkgl92CCqQgtVq4d1ZzgvXXkO11BkWHqYCqwn9j5ti_YaTM5U1CilA9LsFwa2nByadsassnx3ElZKq6V-PcIU73a7RGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نرخ امروز انواع حواله ارزی در مرکز مبادله ارز و طلای ایران
🔹
حواله دلار : ۱۴۸ هزار و ۱۷۹ تومان
🔹
حواله یورو: ۱۷۲ هزار و ۲۴۴ تومان
🔹
حواله یوآن: ۲۱ هزار و ۷۷۸ تومان
🔹
حواله درهم: ۴۰ هزار و ۳۴۸ تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/akhbarefori/652757" target="_blank">📅 10:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قرار نیست در رسانه مذاکره کنیم اما با اطمینان اعلام می‌کنم که در هر گامی مواضع جمهوری اسلامی را بر اساس دستورات مسئولان کشور پیش‌خواهیم گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/akhbarefori/652756" target="_blank">📅 10:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بقایی: در مورد حق خود مذاکره نمی‌کنیم؛ حق ایران در معاهده عدم اشاعه شناسایی شده و نیاز به پذیرش طرف دیگری وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/akhbarefori/652755" target="_blank">📅 10:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: رفت‌وآمدهای فراوان مقامات رژیم صهیونیستی به منطقه از دید ما مخفی نبوده است
🔹
این حضور جز اینکه رژیم صهیونیستی را برای سو استفاده از قلمرو کشورهای منطقه برای تجواز جری‌تر کرده باشد کارایی نداشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/652754" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocQimgbuu1APznRscTIuUO2u_T-h9GyeOqMA0rNO8wymz4bLFiCB-pHSQzRh-NsS3WWiSl_TRGibP26AELMUMjtJgOlFY0t-Do6WA4Yhl8YvZg09hTmvvXadcgsi-01dov4AqNnOJYwWfjNSnyMPGU53lWoU2_j_Q-8zlAi3M5L8ZV-oIBR1sjdtiSSh2vQpJRiBXmZt9kDYvBlDY0hzKjpxpvSTwLgPtUSpLrOv85DoK__bqE2Dxq-9i37RDF8IjwwS91h1v9sdq9-hok9EdGY7dYMrJR54Q83TLchX_ckukG8QcpgBgT_rsQbfRQJKCoh0fd253KnBP-J_FZSc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح حمایتی «کارت امید مادر» برای تمام مادران دارای فرزند متولد ۱۴۰۵
🔹
علی لقمانی، مدیرکل تعاون، کار و رفاه اجتماعی گیلان:
🔹
در نخستین مرحله اجرای طرح حمایتی «کارت امید مادر»، هزار و ۲۷۳ مادر گیلانی دارای فرزند متولد فروردین ۱۴۰۵ مشمول دریافت اعتبار ماهانه شده‌اند
🔹
«کارت امید مادر»، برای تمامی مادرانی که فرزند آنان از ابتدای سال ۱۴۰۵ متولد شده است، در سراسر کشور در حال اجرا است.
🔹
در این طرح، ماهانه مبلغ ۲ میلیون تومان تا پایان دو سالگی فرزند، به کارت بانکی مادر واریز خواهد شد
🔹
تمامی کالاهای مشمول طرح کالابرگ الکترونیکی و بخشی از مایحتاج ضروری مادر و نوزاد از جمله برخی اقلام بهداشتی، در سبد خرید این طرح قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/akhbarefori/652753" target="_blank">📅 10:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از تداوم نقض آتش‌بس و حملات هوایی رژیم صهیونیستی به دیر الزهرانی در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/akhbarefori/652752" target="_blank">📅 10:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
حملات پهپادی اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی در این حملات، شهرکهای «مجدل سلم» و «تبنین» را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/652751" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تجاوز دوباره رژیم صهیونیستی به خاک سوریه
🔹
منابع محلی سوریه خبر دادند که یک گشتی رژیم اشغالگر صهیونیستی وارد روستای «العشه» در حومه قنیطره جنوبی شد.
🔹
اشغاگران اقدام به تفتیش و بازرسی تعدادی از منازل این روستا کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/akhbarefori/652750" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733c44bcbd.mp4?token=Vy4B5FT6nfOfRGC29wRdLnqsV3UdvPunVpLT6c_1WWkVmr0VrHrYvRCsTsTU_oJvxxUsGbmnyT8Vneihm8uWpMHMR5d5EKMCTahhp-UeTvF2YYk90gZs7O6Qr9PlP5_rD0JUiTMTjgoczRbAhERus20KRmzM3Uh5iIqSQ-sBGo87Y3xccrpp7PxoED9X-0-BDK0gdxhci0oYlP7MmUbl8FhjQm_pJMoZgQeILCI-q5kscZcdeVgBPk2wwN7uDXk5_fcX4YH5RL1zpx2qW7HaVHSt8WAJ-8JQw7lEY2PUUibU3mP78qJW9CIzdvR8u2yx-Q3WX7EJB8b33eRnLPhjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733c44bcbd.mp4?token=Vy4B5FT6nfOfRGC29wRdLnqsV3UdvPunVpLT6c_1WWkVmr0VrHrYvRCsTsTU_oJvxxUsGbmnyT8Vneihm8uWpMHMR5d5EKMCTahhp-UeTvF2YYk90gZs7O6Qr9PlP5_rD0JUiTMTjgoczRbAhERus20KRmzM3Uh5iIqSQ-sBGo87Y3xccrpp7PxoED9X-0-BDK0gdxhci0oYlP7MmUbl8FhjQm_pJMoZgQeILCI-q5kscZcdeVgBPk2wwN7uDXk5_fcX4YH5RL1zpx2qW7HaVHSt8WAJ-8JQw7lEY2PUUibU3mP78qJW9CIzdvR8u2yx-Q3WX7EJB8b33eRnLPhjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تازه‌ترین تصاویر از تنگۀ هرمز
🔹
عبور فقط با اجازۀ ایران ممکن است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/akhbarefori/652749" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7f9WUelzPjxzbqV4gy4RWCelLLgIJ1c0kYP2RWK2ot181yN5hNiUpaOlpBTSo7fosvta71Gz5JVneJUWzTDDoQlt21Lo9P2-JcVff5IweYBWH3cq6NZqpiJIUWtwLDfC-uSf7P-HSBCx8UkMKEzQ-K6Ay2SxDgVo8XDYeSUi0ax3_C9TJwrf3S2IPonbpAaqtXYMJcjIFRDk2DZOtm7k_Ks2XuHTfO8ODh0y73_bNQkTjDZuKCiW1GTONQXDno8STaO_yQ-5WwsfIP8o8vdf3NG899tDxuCJ1OMoH1IFFwt5V9AkCfbNHYtBbf9n1tlPj0AUIwBUCL7vkscS7OAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک بطری امروز، صدها سال آلودگی فردا  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/652748" target="_blank">📅 09:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcj5CnXY7gMeZGRwS9yYSZi1T9OxtPy_40Yu9qVHvKVNeHA__QRTqCsvHKvf175Bm1qEEthkmL2WaOh0MGTdhpt5VLOhdw46yyzvoEDwq35o0OrdKQyfr3QyJUyRGfeKRwBNQUpHY4VGVjhY1wwc7T6alIsKpSmmMrhHUhe67msMqFilHVUlH3zQ5EZ2HWJMRZMzCkcZEXjF6PPmQUxGIhgDYMnMJGW0BTt2AEfGZ0pdWm7YxkF5cwAdy7tX3HWXnvX-wB6etmjUfw943RHrn3kuFNdVoRK6NBnF5FN-dXgKRDgjF8kvaYntgkr_AtBNHKk3uQghlvfQxoZOtu7Miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمک‌ نظامی جدید آمریکا به اسرائیل از مسیر آلمان
🔹
در حالی که دونالد ترامپ می‌گوید که «منتظر پیشنهاد به‌روزشده ایران است»، هواپیماهای حامل کمک‌های نظامی آمریکا وارد فلسطین اشغالی شدند.
🔹
طبق گزارش کانال ۱۳ تلویزیون رژیم صهیونیستی، «ده‌ها هواپیما حامل مهمات از پایگاه‌های آمریکا در آلمان در اسرائیل فرود آمده‌اند.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/akhbarefori/652747" target="_blank">📅 09:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b73ea5ee.mp4?token=k6MgrYaFfTGe3x1c6dr05gpu6uFeZ1nItQu6cDj_29JU9mjS4KDM_1fhz5gPTRJKVQ_CKj_Cn7UrezOuP5BU_mO0p-ZFSpEN52f1RijSK9kYMxE42f4bB9oVDgdjIpxw_aavnPUFW-onAjZnAZOhDwX0kxCjIgSSwP13GUsvUhxolHBVGbO1BWPd0Gi6Rq5fPgmz19sqYXduZOHSAQaOY249gc5Gu21q-isU4C1c5Ms_teFf969JK2K24qTvBFRrKRkS6OxLTNDrz46eV6g533ST3APOQlZ34nftFzqrJP5rG0SjRJWDYpu2kIR4dlhPAXZHCwqjbH5GakvfGQAAqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b73ea5ee.mp4?token=k6MgrYaFfTGe3x1c6dr05gpu6uFeZ1nItQu6cDj_29JU9mjS4KDM_1fhz5gPTRJKVQ_CKj_Cn7UrezOuP5BU_mO0p-ZFSpEN52f1RijSK9kYMxE42f4bB9oVDgdjIpxw_aavnPUFW-onAjZnAZOhDwX0kxCjIgSSwP13GUsvUhxolHBVGbO1BWPd0Gi6Rq5fPgmz19sqYXduZOHSAQaOY249gc5Gu21q-isU4C1c5Ms_teFf969JK2K24qTvBFRrKRkS6OxLTNDrz46eV6g533ST3APOQlZ34nftFzqrJP5rG0SjRJWDYpu2kIR4dlhPAXZHCwqjbH5GakvfGQAAqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاجعه مطلق برای پنتاگون
🔹
مارکو روبیو تأیید می‌کند که دولت ترامپ به خاطر واکنش شدید ایران مجبور شد بمباران خود را متوقف کند و ناوشکن‌های آمریکایی را از خلیج فارس خارج کند.
🔹
روبیو ناخواسته افشا کرد که کشتی‌های جنگی آمریکایی در حال عقب‌نشینی به‌طور فعال توسط ایران مورد اصابت گلوله قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/akhbarefori/652746" target="_blank">📅 09:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اموال سرکردگان گروهک‌های ضد انقلاب و تجزیه‌طلب در آذربایجان غربی توقیف شد
🔹
«ناصر عتباتی»رئیس کل دادگستری آذربایجان غربی: اموال ۱۲۹ نفر از عوامل دشمن و خائنین به وطن با لحاظ اقدامات ضدامنیتی و همکاری با کشورهای متخاصم به نفع حقوق عامه و مردم توقیف شد.
🔹
تعدادی از این افراد، عوامل اصلی و نفرات مهم گروهک‌های ضدانقلاب و تجزیه‌طلب هستند که اموال آن‌ها به نفع ملت شده است.
🔹
این تروریست‌ها هم‌دست با آمریکا و اسرائیل علیه مردم شریف ایران و کشور فعالیت می‌کنند.
🔹
توقیف اموال خائنین و وطن‌فروشان توسط قوه قضاییه با قدرت ادامه دارد و در این خصوص برخوردهای قاطع و بازدارنده انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/652745" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaaIE1UsgnljyY6Fu8fXf68m4F5VR8XaoCyQ_43cQPRKK6tgHhy2REItucbvpcSJR5-eNyTLQnud2HUvTpibGJ_kmZYWnTZ0X7FJuPJSoSQYioaVvkhDhSsdUrZV-jyU_qwofYPr8GAWK_lNVtcdKFJUOa5i7uGV7eliDAFzg6bH90DCnRnkKl_8-2E1wXMkInPo8iJOxqiC10zqsvRJ_qxDb4oVSPai1-Mj_5Lkm7Zf6s0cohLu0pAFoXQZ0oppHnyiqpJv2DgczswKXeedm-c2ogRa-w1V_DpkF4Y00zRt995UAlJPrEdtzOsr5WO_MkNoRe03goinkpqyqyBMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۸ اردیبهشت ماه
۱ ذی‌الحجه ‌‌۱۴۴۷
۱۸ می ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/652744" target="_blank">📅 07:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLtJPPdHqN3aKypvIKM8us4apnVb68deFPjH0FRoTBDiyZ2Tgmx7AG4OOfHewuLQe1EkdZXDb9DckxlbnyAqy9rYCO5Nl9t5wtDi0sZdUylJgCq6PqrzL_KIurMztlfTpOv45fHDbTlIWzWAv0qLhfPSX4GDwOEpa6CYeCq3c_XrZCSmJeqRorqk-rrXCsXqBuIhu13IjBHsQOTABjdCzX6s09EHMIiKO36v9ofahssv0wdZiA5m6Z3Awgy3tHs5rUiCAyVUp9xpqHPdaP7KeOgrBDSYLi9yA18GS5Zt2HnGOh2qCgrbXSNnlBblIWthhfUnEAEaeAYUZpsc-b-9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مارجوری تیلور گرین: اگر نیروهای نظامی آمریکا را وارد ایران کنید، یک انقلاب سیاسی در آمریکا رخ خواهد داد
🔹
نماینده مستعفی کنگره و حامی مشهور سابق ترامپ: کار ما تمام است.
🔹
ما گفتیم دیگر هیچ جنگ خارجی‌ای نمی‌خواهیم، و کاملاً هم جدی بودیم.
🔹
این ائتلاف، متحد خواهد شد و شکست‌ناپذیر می‌شود. من شخصاً مطمئن می‌شوم که این اتفاق بیفتد.
🔹
این جنگ را پایان دهید. این جنگ احمقانه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652743" target="_blank">📅 05:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هیچ جایگزینی برای تنگه هرمز وجود ندارد
🔹
کشورهای عربی حاشیه خلیج فارس به دنبال مختل شدن صادرات نفت‌ و گازشان به دنبال مسیرهای جایگزین خط لوله برای تنگه هرمز هستند.
🔹
این راهکارها پرهزینه، ناکافی و در برابر حملات هوایی آسیب‌پذیرند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/652742" target="_blank">📅 01:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پروژه استراتوس؛ معادل انفجار ۲۳ بمب اتمی در بیابان یوتای آمریکا!
🔹
یک ابر مرکز داده به نام «پروژه استراتوس» در آمریکا، آنقدر انرژی می‌بلعد و گرما پس می‌دهد که هر ۲۴ ساعت، معادل ۲۳ بمب اتم گرما وارد محیط می‌شود. این پروژه‌ عظیم تا ۹ گیگاوات برق مصرف می‌کند.
🔹
پروژه با ژنراتورهای گازی مستقل کار می‌کند، بنابراین این گرما در یک نقطه متمرکز می‌ماند. گویی یک آتشفشان تکنولوژیک در دل کویر روشن شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/652741" target="_blank">📅 00:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuXYYAXauC8RBBIqB3YyVCjB7BSU5qUWs8iraYJ8GVQcmYy_uRahn23u4YaSqk4YKg8RX4r5LY7wn-yEzOi0xGvJl814-pX752XzIDpnc-_DhMEePC20aTqD7xfDAA29LhIRAAn4krT5QDgeKh6-IWnypbwnq4NcmbUF-FdFgRc0E0O7j4aaKQZHCIa92SYFLxtlRUjak8MZ1k5h9JYqyvzoRIH45MstBxugF4EtusJVsVClOrWh1CIVv7GH-odR3q2hHuqScWi_XCFo-lUg5PezWFHEx3KLftvf4qQgi2qg_exc9btlPxa9Z1R13PKwY6SYl_yukWuc2q-HQJxnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بغداد: اجازه نمی‌دهیم عراق سکویی برای حمله به کشورهای دیگر شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/652740" target="_blank">📅 00:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSBoRTEpiqBtjLVEJ7kp6wKpCgaUEs-_iorOq6ZQUrT032mmhD83U4znh40JPCdAdOIOffndzICDBxCvjyw9FA0XHo-LzdtIEU6GUF-F09033hCh4MuA75jaiWbmlGC8chMs1bww7cn8VkaIo0HJzUDN_3UoRhDnfBr0zHL0cOPusEVgzRAAYXYOFSQbnnGpTLQngGwrIe3mrtc1wPGwP-bSgfRyKCP7lr6Vc2ISm-FV05UFa1YmLfGI7nhfGTVsfyEsdUnJ4cb1u6Vp_L-VH8EROIWIudTs6dcPQOC08wHv9zVHT0_F8kDc2HIeMg29eknDNc0u2Uz5l6sjYrqbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ft_4ABr6IcehCRy5y5RqiX9RU4KPPMOwg7pKyhxcrRqVLzJsuh-Ue-2zkpV_aywxedgE-UvsuzDNSA1X0dZoAq1xxzVIJIhF9M4UdmFxiWpNDFKLKOCJM394nrfUvzkHI4_AxAOM0BQEjnvCpWvqdCnBOM0ItZUakJq7TnM8YN5RC5GbkVpdSOePesLtnq7gFqWzvtfdKLgtfmHdPKojVFx0AZbZgjDmDQkh8Aps-0nni269VG5D20QWtAEv7QcylPtvl1p4PmgE74AbhgNMEAlu7HnqUW1uSKRqD609b29mu3el119YI7NkJDqrCgXSYUccQ64hc5UEQ4Atpb6NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFG8IO76F-jhMg2C_f35LOl0qXL7-0H0xfd2XKFLxVJE6Yiq-G6PUv_J-yTPyhmAOLDV1bRethiAWZlvppXhMjH4XA74LA0-mla1id7Ne4G5a2exHyZghtBj-4MjI74HAsu0P3_Jv0JWtEmLIlENc8lqAWHyckpl2e2dmKPoZop-0_tYnXVAFT9cQvyRyFaoEHuZeb5bhOKY0sJ0QImLw-ChUewMMD_8x8EHnuE1OppVMkgyQ97KiwbeMb27B5rXTLTnWG_061E44bccRGSPQLPB4x-bI3uGX2KCTgIFBiLqhhqQhkAcqLnZeOKvd3BiZhjx9EAEAnUBV1ixfJASUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OETyh0cr7BZQK3i6JHl9pZCSSmEOkplq871mM9ef_ggRe3QXL8QOsRARvQYGW5rHRtM_MTfxBt8gbQ-IOmIUWkoh306JzGAfMD0MOL1jDfwz8VZuO0xzSDMaHmCwn7HaGAf8zS4MKC974_ohzmnmLErQrr_HsEloc5gQtsjeqmWNGwkVXx_mKYeAKH1ghhDuY2EzkpLAOFZ-8O0WiuDavxg_1KDIhrcRfSzuHlVyvM0KYqljVlfcwMMbHd6kQBWbG7gpwNOILaAcPa07SElj3yYGkS4jE28CIa2bZ6Sc_BW86MQIOFqw4V8kjz5i56XkCDHWmXnVWXnYz1oSkCJXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fu5HhHSJ19QkGTaSuSYI22BsOxFiK2p2eKyT3BgZ6ehiF27QpJqWd7YGHY4HKAXP67dipl-3IvdMGVQqS8NhByyN06OFo7aF64cSRvaFSu3j0NLh8l7Og8Nc1b2RsL29Jw5m5K5_7V2NUpNzZK6X_K4FiMITFquDF6nxFuQUp0hbDQJsrmtA47SgUQYXq0rv81eDb5QV3kVsEsZbzcb9zuvQ5l3vp7z9-SmDzkik3R-5g8s40CXANcWT2inx3VcM7ahjmAXo4h_ozm6xGcJ_CPk4DFR-bEA9X_DcvH3nfFu7HU7kKTV5L_JpPHCKG1r5QuNIv2AOLKJLMWRDLEj0jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تنگه هرمز می‌تواند آمریکا را به توافق بکشاند؟
🔹
ادامه بسته‌ ماندن تنگه هرمز در پی تنش میان ایران و آمریکا، به‌عنوان بزرگ‌ترین تهدید عرضه نفت در دهه اخیر مطرح شده است.
🔹
مؤسسه Continuum Economics با بررسی سه سناریو بر اساس مدت اختلال و واکنش جهانی، احتمال مصالحه میان ایران و آمریکا را ۸۰ درصد برآورد کرده است. نتایج این داده‌ها را در این اسلایدها ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/652735" target="_blank">📅 00:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
از خبرها و تحلیل‌های جنجالی امروز غافل نمانید
🔹
🔹
خبرهای لحظه به لحظه از تحولات منطقه | ترامپ تهدید کرد، جنگ نزدیک است!
👇
khabarfoori.com/fa/tiny/news-3215612
🔹
اموال این بلاگرها و سلبریتی ها توقیف شد + لیست
👇
khabarfoori.com/fa/tiny/news-3215517
🔹
جنگ سوم ایران و آمریکا چگونه خواهد بود | از تداوم ترور تا نبرد بزرگ در خلیج فارس
👇
khabarfoori.com/fa/tiny/news-3215690
🔹
ماجرای حمله پهپادی امروز به امارات چه بود؟
👇
khabarfoori.com/fa/tiny/news-3215668
🔹
تحلیل آخرین قیمت‌ها در بازار | مورد عجیب ریزش طلا و گرانی پوشک
👇
khabarfoori.com/fa/tiny/news-3215805
🔹
در آپارات خبرفوری، ویدئوهای خبرساز را ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652734" target="_blank">📅 00:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdqL9ZQhFmmXHOoz3A8UQzY9ExBbZM4fseYg5xsPigV6sOqwYs409DVbP6OHFr1_ffMWO0XFA_XY4lZ1saEDkoxwZY_YM_5FU0_h-zz5j4b1SmhFLJ_TjgVdLJa7KnXgy5dnMdqgkarEulb6dFCOxbuPthNAhcIvjb17QOHSW5HHSiSaQ67sM1Vtv7bSuPHjIy3UnUHl4HYUjjoTQPbyIQZOXoe8oGwN9i4ShFKXhxWtNegCzCNjA6zbcd_uaS7rlRVUEI78Ejg-_aSREl6bOpRg4cxvbhhTXTFsKJjYtBd0yt4rm7VBZgnCvItVqTX_srvpTWWE6gvyE7nrOgU-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عربستان در حمله پهپادی از عراق
🔹
سرلشکر ترکی المالکی، سخنگوی وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح امروز یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شد.
🔹
المالکی اظهار داشت که عربستان حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند و علیه هرگونه تلاشی برای تعدی به حاکمیت و امنیت این کشور، اقدامات عملیاتی اتخاذ خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/652733" target="_blank">📅 23:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWaXesvT_2iPQrzL_P_14iOmQYc3NNgfR6ChKv0FJAXzUDZCswvKWylc-pNzlWVRcDzCy6iAVX7fyDkgIS8FPBpKSV-V_BWNY5iVUSuBE5bFIzxoJxF7Do8qRNHDOJhkOmMeJJSx6ufJe5f6XMJWaigM1XwexI_TARGwYnnxg-AvHDcFPjDHdMdvZzaty_XV1-pz7m_azEuw_B-rMQUc-DMYImJ0UpLT_ilFo8DlRtW6KZ1UCmwsolpmZ8hz72jxBApFvWE-Gp75BAVyzeW8W59nd_w1k0StzaLIEhpOqyja9kHi6cqP0BAYWuSnyxdE9hr9-W29g2d19B_tPO2QhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالانه تنها نیم درصد به جمعیت کشور اضافه می‌شود/ تعداد ولادت‌ها به کمتر از ۹۰۰ هزار نفر رسید
🔹
سعیدی، رئیس مرکز جوانی جمعیت وزارت بهداشت: شاخص TFR یا باروری کل که مربوط به تعداد موالید در خانم‌های در سن فرزندآوری است، رو به کاهش است. زمانی در دهه ۶۰، به ازای هر خانم در سن فرزندآوری حدوداً ۶.۵ فرزند به دنیا می‌آمد. الان این عدد به حدود ۱.۴ فرزند رسیده است.
🔹
آمار ولادت‌ها به زیر یک میلیون نفر رسیده و در سال ۱۴۰۴ حدود ۸۹۲ هزار ولادت نوزاد ایرانی در کشور ثبت شد.
🔹
سالانه حدود نیم درصد به جمعیت کشور اضافه می‌شود. به عبارت دیگر، سالانه حدود ۹۰۰ هزار ولادت داریم و حدود ۴۵۰ هزار فوت.
🔹
با ادامه یافتن این روند، اگر تعداد مرگ از تعداد ولادت‌ها پیشی بگیرد، رشد جمعیت ما منفی می‌شود.
🔹
در سال‌های گذشته میانگین سن ازدواج به ۱۸ تا ۱۹ سال رسیده بود اما اکنون این عدد به حدود ۲۸ تا ۳۲ سال رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652732" target="_blank">📅 23:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8aTCkU-vjBxKyGK4EriR4eYxNdBA0RQ0nTWYAIuy3Gm_UnZqfb8dFU7UpWOxRoX5xh9kYxxF-2_LcEmHLfTXXw_W7fuFhtqVRZYpvTYwbHRskiMkPvab-VxNkAh_uuH_dxnaQaKF9wY36Z4IMm29hOo9M5sEuVm9UA_YbhUOy7XqxUblgoS6EswZBQvvFVFC7_8cbKq20hWTr0tAerwKFg45g1UFw-amJwWplSxJb2t3Q8FM70xkGr2gavcPV59P-O2qzjikh3_zDj9uvMoxOlBJGjlPWs2UA0TyYmUdwVkEGdgEgLwKzdLT1tuKBrYdlLZTA2WrK10ghhVCIYRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه قطری: اگر جنگ باعث ناامنی کشورهای خلیج فارس می‌شود، چرا آمریکا در منطقه حضور دارد؟
دوحه نیوز:
🔹
آمریکا پس از این جنگ بیشتر به یک بار اضافی تبدیل می‌شود تا یک حامی. کشورهای خلیج فارس می‌توانند برای دیپلماسی بیشتر تلاش کنند، اما ایالات متحده متقاعد نشده است که این جنگ به اتحادهای خودش آسیب می‌رساند.
🔹
اگر آمریکا متوقف شود، اسرائیل فوراً متوقف خواهد شد. این تحولات، کشورهای منطقه را به دنبال‌کردن تضمین‌های امنیتی بلندمدت و تلاش بیشتر برای دیپلماسی سوق داده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652731" target="_blank">📅 23:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Etvc_R6dWoY27378MfwMonzdhLO9dBK1U-sB0KAHAh85_VNhBXeQDuxR1hUCoDQooUXENSUoK5-93IEjNr-_IXVSB7ViRTZlgnc5Rpd0R9NUUy3Z9dqJL79y37GCeAA966fj79VSy9h5iId1YhJAB-psh__4c7nIfxg9pxz5oAg9JWSPPTa69KdEVU3tMo8ghZLv6nAStIrIYUVPyWsOhUclGARpZuIzvbVtws3zKgMLwhJ8AvVJheY5Ho5QQkzPA5glDMP1DWXaoVoGlqwMMm_3yuQoVpHROVfKgd_rWV_51arAuQEIkQ7E3TsaKFSL4xA1k0gjQww0dhCwDKtFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6J0u89QmvnJhRwA0ocOFX0t80Mc77HUDAcnjRWzbIICwAFXmCzCGx6uQw1UExO5zbsYJjlVaqvV3m55DUjUpMutJxu5aliFzpjHLMM4-uQLykoqRN10ErD9I4qTihSAMpHp6-mDwybst_Ivjx-QpQ-oLfsVzzry19CszCe1JhkfpzUlYO4kDQvmWbCgPSCCDOYBNkFAcQRX2NQ_MRzNC607CDzmTe6qX16zBpfNXpesdC9jG6kOM2A031wbGiwHTol5K0PxsqGDfGjVLl_2ZKmyBoApov5O3HXoBZHNOgdxWAMozZtxfLPXL-XS1hAbR4vDRJC4uwn_SEFopVLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irdhWLaptuQ9NdS31MjLWS2kKFgvVX1N374-QgSTJNO9RwNCNNOyFtgbO__Sn0BaTfxo5PtBU91AOZgtSke_S1lyX-p2IiaSiG3qfQeJLU0u3eBdnUVzeZb-Yu2PJemvpJqa8PsqYDBT-KMk2mqZWODtVLojr27OxsixcU1VrxEre7trg4Ij3geviUJRoe8Ykq7XtJS53LA9N64vo178UWa3jCjt48ZY4yq2o6fpxff_hzjSbP6fRnVwOw1zeANAPivR_nLeFND7ZcBOWuGVfvrI593D3g4GHaFY-M3USVtpx2FaknZLzmGry_XOBbndVEY_mouaKjYy0KbqX-7zDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec6544557.mp4?token=cuSceOeYKUwqtaFDXc6Nu10epcLtldHLMrnYlo7O0UBvA-Tf4bdV_M9vvUPzMOqpu_1gXOWVvopUygWg03qCVpVJJd0gTNnZLZ9o46PQrP64bT6ssq8oHCU4HhMSIRWp0_vMOSIsGcKvPixG93QCgdjxamHiZIgHnJWWNhCBEqEAQUmhmpua91PJCgNgCvfPTWKw82L0vFWvZJzvzWadI05wkDaA1lXQ6g2zOefvPiG5NRUJLaqjC54NgX3Ym4mQgN1uTA0LBsbbmbHvShSr838ULRQwijJh3gDKaoIG-Swsa4Eg1awvRSDOYo1d5xls10Y70ywtFiBsyjuHuk0TgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec6544557.mp4?token=cuSceOeYKUwqtaFDXc6Nu10epcLtldHLMrnYlo7O0UBvA-Tf4bdV_M9vvUPzMOqpu_1gXOWVvopUygWg03qCVpVJJd0gTNnZLZ9o46PQrP64bT6ssq8oHCU4HhMSIRWp0_vMOSIsGcKvPixG93QCgdjxamHiZIgHnJWWNhCBEqEAQUmhmpua91PJCgNgCvfPTWKw82L0vFWvZJzvzWadI05wkDaA1lXQ6g2zOefvPiG5NRUJLaqjC54NgX3Ym4mQgN1uTA0LBsbbmbHvShSr838ULRQwijJh3gDKaoIG-Swsa4Eg1awvRSDOYo1d5xls10Y70ywtFiBsyjuHuk0TgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی درباره انهدام یک پهپاد آمریکایی در یمن
🔹
برخی رسانه‌ها با انتشار تصاویری، از انهدام یک فروند پهپاد MQ۹ ارتش آمریکا در آسمان استان مارب به دست نیروهای مسلح یمن خبر می‌دهند‌.
🔹
نیروهای مسلح یمن هنوز بیانیه‌ای در این باره صادر نکرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652727" target="_blank">📅 23:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تکنیک اقتصادی روسیه در جنگ برای نجات بورس مسکو
🔹
خبرهای رسیده حکایت از این دارد که بورس تهران بعد از بزرگترین تعطیلی خود قرار است سه‌شنبه باز شود.
🔹
تجربه بورس مسکو در ایام جنگ روسیه و اوکراین می‌تواند برای ایران درس‌آموز باشد. اما روسیه در جنگ برای بورس چه کرد؟
🔹
در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/652726" target="_blank">📅 23:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y443M5wRR90sjCU2cmKWypBwbGk5tVZ7wQcQfvLqtNRn02oOVerMHgxgrEvLfGdHEl8SX7263YyDzfdk3wdUg-_2RcGNjjpJc2qsIYhrKOnkeZooylRW0x9p7zUpKS66f3zo1p1S6cAE6jlIUVIr5ZZRzAyzG57PDMQZvWxbgTWejjyFEIZRVd-Fc-OywQBishGqmLS5PAdS0ozVE6crlwXfF_jJSWxRQnXuWT4k5S_LxN12C27VK4XrqNWc2MBDy7Usu8bkSpm_dVB1oRi1cj7it79MwEo4NmjmOO9J8_EkqJ_jynCyHqDE7Dbugqdu3qdkQzDt1EfMPKTSjUcurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از چین تعهد گرفت که از ایران حمایت مادی نکند!
جیمیسون گریر، نماینده ارشد تجاری ترامپ به ای‌بی‌سی نیوز:
🔹
وقتی رئیس‌جمهور به آنجا رفت، نرفت که از آنها بخواهد در تنگه هرمز اقدامی انجام دهند. او بسیار متمرکز بر این بود که اطمینان حاصل کند آنها از ایران حمایت مادی نمی‌کنند. این تعهدی است که او به دست آورد و تأیید کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652725" target="_blank">📅 23:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f594291402.mp4?token=s3SRIpvVeKpES_agXRtlCFqEcwsI6Hn3f8FtwDdDec_TmZ5p-ufgnY0j3TV_YpE2S-z35NPMZbh1j6qWLF-1ssAU147x1iZ1CDiLeNVOzX9VJClYn9xISwF44GEnmjaEs6-F7Ebycxc1gTUf99kJcqNAAL89l_PQctDjTmpcBmZ3KW9o9fSdufJMMFI3XjMqU7x5gstbQiMhEkkQrT6Jtld2OVh_3h4VPlWoGa2efPLkDBc-jb8GKqVYqlu3raS4GyRebG0nba_L8iGh5eT_adH20kPnZ39dpaht_CZWIlXmkZI-XkJJW5vRDLqp8J8HDOCI1KFX8Nc7KyDsSz2y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f594291402.mp4?token=s3SRIpvVeKpES_agXRtlCFqEcwsI6Hn3f8FtwDdDec_TmZ5p-ufgnY0j3TV_YpE2S-z35NPMZbh1j6qWLF-1ssAU147x1iZ1CDiLeNVOzX9VJClYn9xISwF44GEnmjaEs6-F7Ebycxc1gTUf99kJcqNAAL89l_PQctDjTmpcBmZ3KW9o9fSdufJMMFI3XjMqU7x5gstbQiMhEkkQrT6Jtld2OVh_3h4VPlWoGa2efPLkDBc-jb8GKqVYqlu3raS4GyRebG0nba_L8iGh5eT_adH20kPnZ39dpaht_CZWIlXmkZI-XkJJW5vRDLqp8J8HDOCI1KFX8Nc7KyDsSz2y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: فتوای حرام بودن بمب هسته‌ای رهبر انقلاب  تغییر نکرده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/akhbarefori/652724" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1FB4Aqc_rQLatN8fjcJ5GIFs1_fP4NbetYANr5E2IGu1GXjJD62BZIV6uYAAA6jn1xDy3JOGlJQTslaF7_-irwmDH3oz5JIlyDUzfyaVV3m-A1MquTvzJSxj4ArG9BtmCazpVOcxL2ucimCSCDDS9wQ8CkCOUY_KxrfRKjM7gKmnm_9uwvTWtnpq1uFdzBJXpBq7EqnS-mN_8qYDnIDOQLI7cChoV_PX4rE9fmxmVhnN4RRAw5sfKnDOKOUt_S--PpVzY0Lug78hXJIGTwqRC1irrCn6EadJ9LJxgT1X0qjIraEADMNAuJUAADBLO6jPSRmKVKvnF2V-juJ9D3ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشان ملی «روابط عمومی برتر ایران» به ایرانسل تعلق گرفت
🔹
همزمان با روز روابط عمومی، سیزدهمین دوره «جشنواره ستارگان روابط‌ عمومی ایران»، ۲۷ اردیبهشت‌ماه، برای ششمین سال متوالی از ایرانسل تقدیر کرد.
🔹
در مراسم پایانی این جشنواره که با حضور جمعی از فعالان ارتباطی ایرانی و بین‌المللی در سالن همایش‌های کتابخانه ملی ایران برگزار شد.
🔹
در این رویداد، نشان ویژه «ستاره ارتباطی مدیر ارشد»، با کسب بالاترین امتیازهای لازم از ارزیابی‌های تخصصی و به دلیل شخصیت و منش ارتباطی، روحیه تعاملی و نقش تعیین‌کننده در بهبود ارتباط با ذی‌نفعان و نگاه تعالی‌جویانه به حوزه ارتباطات، روابط عمومی، رسانه و افکار عمومی، به مهندس محمدحسین سلیمانیان مدیرعامل ایرانسل اعطا شد.
🔹
همچنین روابط عمومی ایرانسل، بر اساس رأی هیئت داوران و به دلیل درخشش در عرصه‌های مختلف ارتباطی، به‌ویژه مدیریت هوشمند خوشنامی سازمان، موفق شد لوح سپاس و نشان ویژه ستاره ملی «روابط عمومی برتر ایران» را دریافت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/akhbarefori/652723" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درویش: خسارت جزایر مرجانی اطراف جزایر هنگام، هرمز، و کیش در اثر بمباران‌های جنگ محسوس است
محمد درویش، فعال محیط زیست در
#گفتگو
با خبرفوری:
🔹
شاهد وجود لاشه‌های ماهی و آبزیان در سطح آب نبودیم اما خسارت جزایر مرجانی اطراف هنگام، هرمز، کیش در اثر این بمباران‌ها محسوس است و روی کیفیت غذای آن منطقه اثر می گذارد.
🔹
معاونت دریایی سازمان حفاظت محیط زیست باید موضع گیری شفاف کند و بگوید چه حدی از آلودگی، خلیج فارس را دربرگرفته، چه میزان خطرناک است، کدام جزایر ما در معرض آسیب است.
🔹
نزدیک به ۲۰۰ شناور و کشتی‌های مختلف در خلیج فارس و دریای عمان غرق شده است که محموله ها و مشتقات شیمیایی، محموله‌ها و مهمات آنها زیر آب رفته است و می تواند سبب آلودگی شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/652722" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سرلشکر رضایی: ایران در دیپلماسی و مذاکره جدی است اما در برخورد با متجاوز، جدی‌تر است
🔹
آمریکاست که الان باید خودش را ثابت کند.
🔹
انگشت نیروهای مسلح ما روی ماشه است و همزمان دیپلماسی هم ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/652721" target="_blank">📅 23:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
برنامه جدید وزارت اقتصاد برای تغییر مسیرهای تجاری کشور/ مسیر جایگزین معرفی شد
🔹
در شرایطی که طی هفته‌های اخیر روند واردات کالا از برخی بنادر جنوبی کشور با کندی مواجه شده، دولت بامحوریت وزارت اقتصاد برنامه جدیدی را برای بازطراحی مسیرهای تجاری و وارداتی کشور در دستور کار قرار داده است.
🔹
برنامه‌ای که بر اساس آن بخشی از واردات از بنادر جنوبی به بنادر شمالی و مرزهای زمینی منتقل می‌شود تا روند تأمین کالا بدون وقفه ادامه یابد و بازار با کمبود مواجه نشود.
🔹
بر اساس اعلام وزارت امور اقتصادی و دارایی، این تصمیم با هدف افزایش تاب‌آوری اقتصادی، جلوگیری از ایجاد گلوگاه در زنجیره تأمین و استفاده حداکثری از ظرفیت‌های جایگزین حمل‌ونقل اتخاذ شده است.
🔹
در هم ین راستا، هماهنگی‌های گسترده‌ای با کشورهای همسایه برای تسهیل ترانزیت، حمل‌ونقل و ورود کالا انجام شده و کارگروه‌های ویژه‌ای نیز در سطح ملی و استانی تشکیل شده‌اند./ خبرآنلاین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/akhbarefori/652720" target="_blank">📅 23:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652719">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای رسانه صهیونی: امریکا به امارات پیشنهاد داده جزیره لاوان را تصرف کند!
جورزالم‌پست:
🔹
گزارش‌ها حاکی از آن است که دولت ترامپ امارات را تشویق می‌کند تا درگیر مستقیم در جنگ علیه ایران شود. برخی مقامات به ابوظبی پیشنهاد می‌کنند جزیره لاوان ایران را تصرف کند.
🔹
یک مقام اسبق ارشد امنیتی دولت ترامپ گفت که استفاده از نیروهای امارات، از قرار گرفتن نیروهای آمریکایی در خط آتش جلوگیری می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/akhbarefori/652719" target="_blank">📅 23:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e3688043.mp4?token=tiuGYwqTr1F5WcJ-RlLqRZGBlInIvInReBW7-JIkajfsARUZzZ17ylyeEmn-eUobpCGVBAvMv0PubBy6DLC2SN9haVp373SA4s_-E96QINMrPbEGu1V82w7fmDK9TLr2QJWJ-F64oE32jfStC5QmX5Dfy-p42h9zqCLO7VfLrpT1anvdWZTwKEMI1H4i2Paz1hIoGtPFTYXsZBoxqZrZPoPaQSQQS08RjtmFGRMxA7NhEnz84tnd1CODFH26V_2AKxqkTxWLvtMF0GQ-bFPLfs0lDs_dR7ybcBVGlR9D2tmBjFZHEll5DQUcBSmh1KNzJVRoFvG5oPPCe2ne77PmcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e3688043.mp4?token=tiuGYwqTr1F5WcJ-RlLqRZGBlInIvInReBW7-JIkajfsARUZzZ17ylyeEmn-eUobpCGVBAvMv0PubBy6DLC2SN9haVp373SA4s_-E96QINMrPbEGu1V82w7fmDK9TLr2QJWJ-F64oE32jfStC5QmX5Dfy-p42h9zqCLO7VfLrpT1anvdWZTwKEMI1H4i2Paz1hIoGtPFTYXsZBoxqZrZPoPaQSQQS08RjtmFGRMxA7NhEnz84tnd1CODFH26V_2AKxqkTxWLvtMF0GQ-bFPLfs0lDs_dR7ybcBVGlR9D2tmBjFZHEll5DQUcBSmh1KNzJVRoFvG5oPPCe2ne77PmcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست بیمه بیکاری به اوج رسید!
🔹
عددهای این ویدئو خبر نیست، واقعیت‌های این روزهاست که از پی آمار می‌آید.
@TV_Fori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/652718" target="_blank">📅 22:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv6E68S-2YZ-7Qhq-U5LMXin8E-3ATefImQv5yYdiE4iarkHAU_OTkPVrde3wk8AE6avPWUrmY6LByLZ1XJly86R7SNRzxMeuPIiJCJiurb92_6FxydB0R2hy3ugMWFEO_4kDaOBM6jEDgRRY56aUNcwKFIxOtHDeFmBtHjTNqQS-xUbEfAjpJjnAA45aCdVZ3IY4ME1osID08ylVky_ySYE4PXZ4XSKy5WwwoN_WvCIoXCoSUryjIzNJM1j3L-IYpFBc-TBgMMdUwHu5g3UAoqfJCtbPrsvToQOdBvCQOypUVWC261kCbUAmh7CTaLyyZaiS1HGcaEEsevpUnpY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف چند دقیقه، آلودگی چند صد ساله…طبیعت، سطل زباله‌ ما نیست…  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/akhbarefori/652717" target="_blank">📅 22:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652713">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ef0u9Bg_nRfZMcj2O3638FV6vxWBPnDhEd3pFZzsycA6ak1mVFaSlyTLvbD0CfjcseInzRKHjYITUgOfwsHIzjRbK0I6lEL3SBaT2AkNhBFtc-Jw5zAU4efCBLiEv9mcmFr56fG9kNIVVTKusiPMEOYJEB00fg0g1WGIGdCTPpRhcjiPHin_wo8fdHKKB4kJaWGuIS4f2S5o1lisPO-oDQjEu8Em0u0MRMEz_8f_KBJm4D-JMTnFFQ1HFEEMNeZz6hRLy8TDWu06IEaDN3Pr3M2OrYZvCu-g_V9ubL4IDnYfZqsX1kmzcB03Z1Mp7jHEsGMxK-I5xJ925l365eDRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QG4Zcx0JiOCoz5nxM4DXmR3WDvlZGu90JTU7EM5fXPKi7zn2fnuIo-yKeJsCTJHVOEl_Q-VndSpN3gmCfrz7CkZTWg4xEk5nZsHMxdBkm60OKkopbwVA38vJp5p3Qf1dE5xmVWHGXQQRk4k-s-rmXG5nP20iX0yVnS03opVzN5zykFPOj0Ts2FOl_mlxUJwrGSpqvfkwG-ElIdm1lLS0u96Ty0dBpMcg9D1gz-eHfABrT48JTMxoK4Z7w4v7fE9nTHLMR-1F3oXr7D-G4DKXzi5em3Q4ZkFzUu-MgV5xw0MeuTWhZsetZSP6G2YMB-obSbeRTp5A85o2_ujcI4xlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCIb4fjAgGts9IkrBHFjj38FwDz135MRZc4LzxylBNy8s3435GzYFaPpU-VRe0GXK10637OzZH_Rt1zQgBS8nd_5aF7PRjjye_HiBH0d2gZ1hONvtLMPSTQoplhn5-I7GhMU95iZAS3S7XvDeekEPPMJyXJqDJOoijz6xqYVl6SbL36ekykWIfcDZmgAtXESL5-odguzHbRKS_NQjkifzqfpFbuY0J9xfGS83LVKb0xfbuDsvUAqVzcXUMNihk6-cMRsF8Z0f_qyNFAkrzK2rfKuPpfd8vWQ-HkgiCd4KMZ9BagDRJsAAFZQCs2L8SdvBJRcZDxpa46ep8PGWjycsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6128f73793.mp4?token=Ssq2dscCkB8GdnW9qbEh1o0beJQg1iIUpsL-y3Br0XXhi0Bwh08WqanLlRP4WV9TO30DdDG5jozCBqGZADlYmqXVK_kmoGnUkytLTHoiwraUQv6ONnLLf5JmFRcU6FdEOvdGBzE0XOrd-jncNf1BiVvgjoU7gkt605EhBePcPZAydjL3ipVsADHtZ6mV4MSVK8tDcPDhdpXkucqeZT35BkHpsQbqsJOY1-H0DOGZ7Vwxo-ggYzJc4fSrVpLAUtNgasVLJ5IZaNLsFYlHL2ir2iptcstcbST8rq0jy2sTyuvfLj4MIxqJ1gRSiidBvWRaj456w0Lwq_U5-aIbH9jerg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6128f73793.mp4?token=Ssq2dscCkB8GdnW9qbEh1o0beJQg1iIUpsL-y3Br0XXhi0Bwh08WqanLlRP4WV9TO30DdDG5jozCBqGZADlYmqXVK_kmoGnUkytLTHoiwraUQv6ONnLLf5JmFRcU6FdEOvdGBzE0XOrd-jncNf1BiVvgjoU7gkt605EhBePcPZAydjL3ipVsADHtZ6mV4MSVK8tDcPDhdpXkucqeZT35BkHpsQbqsJOY1-H0DOGZ7Vwxo-ggYzJc4fSrVpLAUtNgasVLJ5IZaNLsFYlHL2ir2iptcstcbST8rq0jy2sTyuvfLj4MIxqJ1gRSiidBvWRaj456w0Lwq_U5-aIbH9jerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوری| برخورد دو جنگنده نیروی دریایی آمریکا در آسمان
🔹
در جریان نمایش هوایی Gunfighter Skies
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652713" target="_blank">📅 22:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652712">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
قیمت های عجیب و غریب در بازار میوه/ یک کیلوگرم انگور ۵ میلیون تومان!
🔹
این روزها بازار میوه با قیمت های عجیبی روبه رو شده است، به‌طوری که در یک سوپرمیوه در خیابان فرشته، هر کیلوگرم انگور یاقوتی بنفش را تا ۵ میلیون تومان و زردآلو را تا نزدیک به دو میلیون تومان عرضه می کنند.
شرح ماجرا را در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3215722</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/652712" target="_blank">📅 22:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652711">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975f8b4c2d.mp4?token=lunYJEmRxBOXbXq6xxZZT1ZeI9CdPE2tKG0r_rTTZloTWbT1wRBVAnwcgXZwXpAC11c3GQRmbiCZRKkaJzyae1FRoj_QsXVozqkhYRO4FTv56LStkk6-E56SImyylw3xObrRxgYAf9B_v9mTURyp-f5C7KuTaNre4-yKPS64nDF81ZeRMnqktAx3p7dEEsO4v9ffYRdnFWUJZC4wLu7WSafiqa4SOY3WeKeHs-p-eb8PN27uKNkgy6Hgvr5K-yi1D9rJ_x3erJr0SS8iZMB2xbg2DFrARsbZ9oaFFAh3ViLvzoqVhkSBdCT9ypDag1sPRkdvim_UHf2Eb809x5x-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975f8b4c2d.mp4?token=lunYJEmRxBOXbXq6xxZZT1ZeI9CdPE2tKG0r_rTTZloTWbT1wRBVAnwcgXZwXpAC11c3GQRmbiCZRKkaJzyae1FRoj_QsXVozqkhYRO4FTv56LStkk6-E56SImyylw3xObrRxgYAf9B_v9mTURyp-f5C7KuTaNre4-yKPS64nDF81ZeRMnqktAx3p7dEEsO4v9ffYRdnFWUJZC4wLu7WSafiqa4SOY3WeKeHs-p-eb8PN27uKNkgy6Hgvr5K-yi1D9rJ_x3erJr0SS8iZMB2xbg2DFrARsbZ9oaFFAh3ViLvzoqVhkSBdCT9ypDag1sPRkdvim_UHf2Eb809x5x-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نه‌تنها «هنوز زنده‌ایم»، بلکه دست‌های دلاوران نیروهای مسلح ایرانمان هم هنوز روی ماشه است. مردم هم هنوز در میدانِ خیابان‌‌اند، روحیه‌ها و همدلی ملّی‌مان هم همچنان در قلّه است. ما اینجاییم تا اگر پدوفیلیِ جنگ‌معاش و متوهم دوباره غلطی کرد، به او و نیابتی‌های کوتوله‌اش در حاشیهٔ جنوبی خلیج فارسمان و در سراسر منطقه درس تاریخی بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652711" target="_blank">📅 22:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652710">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
برنامه جدید وزارت اقتصاد برای تغییر مسیرهای تجاری کشور/ مسیر جایگزین معرفی شد
🔹
در شرایطی که طی هفته‌های اخیر روند واردات کالا از برخی بنادر جنوبی کشور با کندی مواجه شده، دولت بامحوریت وزارت اقتصاد برنامه جدیدی را برای بازطراحی مسیرهای تجاری و وارداتی کشور در دستور کار قرار داده است.
🔹
برنامه‌ای که بر اساس آن بخشی از واردات از بنادر جنوبی به بنادر شمالی و مرزهای زمینی منتقل می‌شود تا روند تأمین کالا بدون وقفه ادامه یابد و بازار با کمبود مواجه نشود.
🔹
بر اساس اعلام وزارت امور اقتصادی و دارایی، این تصمیم با هدف افزایش تاب‌آوری اقتصادی، جلوگیری از ایجاد گلوگاه در زنجیره تأمین و استفاده حداکثری از ظرفیت‌های جایگزین حمل‌ونقل اتخاذ شده است.
🔹
در هم ین راستا، هماهنگی‌های گسترده‌ای با کشورهای همسایه برای تسهیل ترانزیت، حمل‌ونقل و ورود کالا انجام شده و کارگروه‌های ویژه‌ای نیز در سطح ملی و استانی تشکیل شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/652710" target="_blank">📅 22:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f895fd79a.mp4?token=lcsySV6oAypeCuw9kC16WS-2CNBCKN7UaQrd-6lMfKHL1VdNE7k9gc-WjxLNWHJphB1Z4pCC9_zNSEDcG7Gim-YBt9Cbtee0KA525Kh0G5AEgG6ehyBqQVyyUBmhHtdKh-cnH-1Z08aMQscJZZDZOtYAyw6GI7sFoyuUM0VsMu0UXneQfGoVX3nZ5qSnPn14zoZuFlnrgre96ZzeT1Xauz7mQiXNcKNJjfoqFcnIOqiHaKk7cxePVXdtEst30Ffk0EbGxav2ZcsJ2MrGJYrikG7WRfzBZja2pg6xB0h7TXIvaCisUFA6GdN39MfHNItZ9gUxg8AFA5h9zI5-7e2dT5_2Pr5ihHbNwuEVeSK4EaikcNAa1Zwur5fWaV-sxm6ht0N8jfkN7-LNZDa9ULravctOBe9x3_k0WBLrLgKLSIiti8nhRrate35AKaRCgWEOMl5bY15ZWEq-YARNdoJ_h-FR3HXF_qOVJeAd4T07tc9RZPSIKWgg-X6Nr5U3edD42t63ttxtsZHg-4YcjqWao60IZG3EE92jomesxQDbLCgUXwPOVTYcmwbm-kDNsMpq08MPNwvfnQGb_a6RlKwn8ILormmzwWfSSIpnf8xzLMnndMtBVP5fgMv4bVweFKko8-VQvEs7YKNRmWphCassz23i7vW-Ql8BS7qPkLBGq-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f895fd79a.mp4?token=lcsySV6oAypeCuw9kC16WS-2CNBCKN7UaQrd-6lMfKHL1VdNE7k9gc-WjxLNWHJphB1Z4pCC9_zNSEDcG7Gim-YBt9Cbtee0KA525Kh0G5AEgG6ehyBqQVyyUBmhHtdKh-cnH-1Z08aMQscJZZDZOtYAyw6GI7sFoyuUM0VsMu0UXneQfGoVX3nZ5qSnPn14zoZuFlnrgre96ZzeT1Xauz7mQiXNcKNJjfoqFcnIOqiHaKk7cxePVXdtEst30Ffk0EbGxav2ZcsJ2MrGJYrikG7WRfzBZja2pg6xB0h7TXIvaCisUFA6GdN39MfHNItZ9gUxg8AFA5h9zI5-7e2dT5_2Pr5ihHbNwuEVeSK4EaikcNAa1Zwur5fWaV-sxm6ht0N8jfkN7-LNZDa9ULravctOBe9x3_k0WBLrLgKLSIiti8nhRrate35AKaRCgWEOMl5bY15ZWEq-YARNdoJ_h-FR3HXF_qOVJeAd4T07tc9RZPSIKWgg-X6Nr5U3edD42t63ttxtsZHg-4YcjqWao60IZG3EE92jomesxQDbLCgUXwPOVTYcmwbm-kDNsMpq08MPNwvfnQGb_a6RlKwn8ILormmzwWfSSIpnf8xzLMnndMtBVP5fgMv4bVweFKko8-VQvEs7YKNRmWphCassz23i7vW-Ql8BS7qPkLBGq-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: محاصرهٔ دریایی آمریکا را می‌شکنیم
🔹
صبر ما حدی دارد و نیروهای مسلح درحال آماده‌کردن خودش است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/akhbarefori/652709" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
کاخ سفید: ترامپ و همتای چینی به توافق رسیدند که ایران نباید به سلاح هسته‌ای دست یابد
🔹
ترامپ و همتای چینی توافق کردند هیچ کشوری نباید برای تنگه هرمز عوارض دریافت کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/652708" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
محسن رضایی: در جریان باز کردن تنگه هرمز، ارتش و سپاه جلوی آمریکایی‌ها ایستادند و یکی از ۳ ناو آمریکا با شلیک موشک‌های ما آسیب جدی دید که صدایش را در نمی‌آورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/652707" target="_blank">📅 22:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee0743e80.mp4?token=JeVdekkJgM9JMJRp9M0gv0_hi5YNsDFW3rtsdKp6XTaDwRBZPeTGg3DqXeXI2z_V-IZZ_HHq7ktLxvSTqHhjT4zrFByBgHSqNz9ZiOMbwKzKNAqL3qV2HsKcI8qXioy6aYmMmpuNqK0InBO-izrho_Vz2m9M_77M05UjqdEDP24EeFSp5y4FOWJCHMjF02JRrmPs-WLJYFMQHc3YFvF5Pnazy-DLN91EVcwC6C0QSSQ1ykM9GXDqT5doqXPTQPOQ16vDNoYOUhceBYbo8skSDFdZzgdLu1oXj3TucGLCrmdNe_nCJzL0TkMhwyS7ieqDn1Kji3JFan1uldbrAzpqamXOdtI0xm3qQoQ463DO4Y7Y1Nzi5FQvCXz5vj8VHISFQWphgVGdW7KM74bVNI8tF8XrsrsymnNUQSJN16pLkTvkzFT0QTTRc5Bj7Xa-hrim23QaZAWtKrS9pr5fo2Tcm7cbbuq6yhed23hwhYyh2BG5UcXRRLSsNqh-mqkRYWi6GWMxXVjihV4Z5b3qfdDgsto6A3Mza4ydO9nuc0Khsdvex5ylxYdZsy9saPE7VamXzes9g6pEz2wU06OswCVaUhf1pn6ovnv2oPoXVGCJ5DJEAwvheCUAyMycoCh3ZtBAeZ_0jaWciIG0fL5gM5iXFhyT6esDRjujvbGTham1rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee0743e80.mp4?token=JeVdekkJgM9JMJRp9M0gv0_hi5YNsDFW3rtsdKp6XTaDwRBZPeTGg3DqXeXI2z_V-IZZ_HHq7ktLxvSTqHhjT4zrFByBgHSqNz9ZiOMbwKzKNAqL3qV2HsKcI8qXioy6aYmMmpuNqK0InBO-izrho_Vz2m9M_77M05UjqdEDP24EeFSp5y4FOWJCHMjF02JRrmPs-WLJYFMQHc3YFvF5Pnazy-DLN91EVcwC6C0QSSQ1ykM9GXDqT5doqXPTQPOQ16vDNoYOUhceBYbo8skSDFdZzgdLu1oXj3TucGLCrmdNe_nCJzL0TkMhwyS7ieqDn1Kji3JFan1uldbrAzpqamXOdtI0xm3qQoQ463DO4Y7Y1Nzi5FQvCXz5vj8VHISFQWphgVGdW7KM74bVNI8tF8XrsrsymnNUQSJN16pLkTvkzFT0QTTRc5Bj7Xa-hrim23QaZAWtKrS9pr5fo2Tcm7cbbuq6yhed23hwhYyh2BG5UcXRRLSsNqh-mqkRYWi6GWMxXVjihV4Z5b3qfdDgsto6A3Mza4ydO9nuc0Khsdvex5ylxYdZsy9saPE7VamXzes9g6pEz2wU06OswCVaUhf1pn6ovnv2oPoXVGCJ5DJEAwvheCUAyMycoCh3ZtBAeZ_0jaWciIG0fL5gM5iXFhyT6esDRjujvbGTham1rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز برای تجارت باز است؛ نه برای لشکرکشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/akhbarefori/652706" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da680f7fe.mp4?token=pni4eQS9DOAIt_ulhrwOADA-POyr6ooLXu24jYEnQd7967dhGA-zOCvscRb6O8hOOeOQvfiB7q6XBOG7mpov9TJc7XC6kU9wihicFg_OmC7Y2LX1-n6HCuNAJ16IXOinlwckAVMG4DutTLE_hwscc4YKf_v8oCPixls-dYWG56zSl5HOusf9_AMc8xt9n0dH7-WVpfHrNA1xIpQdpAWSrLMHm8QfiM8gqMTQlGo5gdxiyh2tOa2p2D--rZGkJ2AcqEHNFyF5yqwEpRIWAr6tVr8pArxDGEhocAwymKq9apd60_4xPu6MNIgn6MVNSkDjxDWHx8AYx7UIMGvTLwRX3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da680f7fe.mp4?token=pni4eQS9DOAIt_ulhrwOADA-POyr6ooLXu24jYEnQd7967dhGA-zOCvscRb6O8hOOeOQvfiB7q6XBOG7mpov9TJc7XC6kU9wihicFg_OmC7Y2LX1-n6HCuNAJ16IXOinlwckAVMG4DutTLE_hwscc4YKf_v8oCPixls-dYWG56zSl5HOusf9_AMc8xt9n0dH7-WVpfHrNA1xIpQdpAWSrLMHm8QfiM8gqMTQlGo5gdxiyh2tOa2p2D--rZGkJ2AcqEHNFyF5yqwEpRIWAr6tVr8pArxDGEhocAwymKq9apd60_4xPu6MNIgn6MVNSkDjxDWHx8AYx7UIMGvTLwRX3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری و کشته شدن ۱۶۶ سارق مسلح در ایام جنگ
🔹
رادان: همانطور که قول داده بودیم در ایام جنگ با سارقین مماشات نداشته باشیم، تا امروز ۱۶۶ نفر از سارقین مسلح و حرفه‌ای که در برابر پلیس مقاومت کردند به ضرب گلوله زمینگیر و دستگیر شدند و تعدادی از آن‌ها کشته شدند و ۱۰۰ قبضه سلاح نیز از آن‌ها کشف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/652705" target="_blank">📅 22:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2o1AC3DKohWdjAAkyIYzXtX2DL-FBbQnKVvrIf9_r6zHWg-lKYl20xIGLcupLatwi6W2MMgrgfdCb4PLHcE7BEX7OJDNip_4QPbQu0YWZiEvlWTFe11JegNBRShFugQaT6OzY2SSfzdlQR2RTMxvwCdzzAWYXP68DPXRP5t99f5lGI3CgaRSIZroqDkM1Tk_sJP-S2_ZqMaMFUyzzGlxSaI0Hhoe_8J722nU_qa0yZ55z3RFC3f00iaIQRim5G5d2W3TvR9TbxIvmKAh1BD-13vOKiTpDPAEhxVAP6pQi1ydc0f5PwPck1VywWiE_vz4KrjV38WV3Zsrcz-Nqbs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN: ایران می‌تواند با تهدید کابل‌های اینترنتی زیر دریا در تنگه هرمز شرکت‌های فناوری مانند گوگل و متا را ملزم به رعایت قوانین خود کند
🔹
ایران با الهام از محاصره موفقیت‌آمیز تنگه هرمز در طول جنگ، اکنون شریان‌های پنهان اقتصاد جهانی، یعنی کابل‌های اینترنت زیردریایی، را هدف قرار داده تا از غول‌های فناوری جهان حق عبور دریافت کند.
🔹
تهران در نظر دارد شرکت‌های بزرگ فناوری مانند گوگل، مایکروسافت، متا و آمازون را مجبور به پایبندی به قوانین خود کرده و از شرکت‌های کابل‌های زیردریایی حق لیسانس دریافت کند.
🔹
با اینکه اپراتورهای بین‌المللی به دلیل ریسک‌های امنیتی تلاش کرده‌اند کابل‌ها را در بخش عمانی تنگه هرمز متمرکز کنند، اما به گفته مؤسسه پژوهشی «تلی‌جئوگرافی»، دو کابل کلیدی دقیقاً از آب‌های سرزمینی ایران عبور می‌کنند.
🔹
کارشناسان هشدار می‌دهند که هرگونه آسیب عمدی به این زیرساخت‌ها، می‌تواند یک «فاجعه دیجیتال زنجیره‌ای» ایجاد کند که بیش از همه کشورهای عرب خلیج فارس، را تحت تأثیر قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/akhbarefori/652704" target="_blank">📅 22:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8MQeC_5XkaiYLKdsukoT1e-Uy5PPLK1tiIeFtp0xU82QCHmHGsMIPVkuqfUhFxolp88_AjfdhzHINH8ruhigT1VqV6ZlMTrmDkycFOzKQ6v9F00C9scTNn6xLKvxf_RR0tN6h_hN5JoZ8lyVm6MoFmTTs4AbGjtSWkiNiC7Zvw-WPtM2BVPmPU9a183f70TVIr6yE1hGTeOrdAcJoz3NhJ_nAs0uvfw6uJMmsbtgtpdWd2USLhFqUxHrStRIxa2wAS4iya7EItxS1mnOhy42PFlCdMkc6ophqmvUSv_c8CarEWRkG7i0sOTp6sZlkQC58u1BqZBs-B75u-0uMvG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاف تلگرامیِ «العربیه»؛ پیام اتاق فرمانِ رسانهٔ سعودی به کارمندانش: تا می‌توانید به جنگ روانی علیه ایران مهمات برسانید
🔹
«تا اینجا چند تا آکسیوس و ترامپ کار کردیم. آکسیوس‌ها رو فتونیوز کنید!» ادمینِ «العربیه»، رسانهٔ نزدیک به اسرائیل، این فرمانِ صادرشده از مدیران به کارمندان را به‌اشتباه در کانال عمومی‌اش پست کرده. البته این نکته، چیز پنهانی نبود؛ دو روز پیش هم که کانال العربیه سعی کرد در ادامهٔ فعالیت‌های رسانه‌ایِ ضدمقاومتش نقل‌قولی از نخست‌وزیر لبنان را با تنظیم خاصی پوشش دهد، نظر مردم غزه درباره فعالیت‌‌هایشان و اسمی که روی این رسانه سعودی گذاشته‌اند را مرور کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/652703" target="_blank">📅 21:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2f385bca.mp4?token=ACSYPTLtEm0n6o2PM_p1_M0i-VZ38nnPV86TlEc0pQQ4Bi7OmVcWxgESOJDIj7-Hgaa0r5HEKwLaAbuT9YhASLYo8re3nWj0rKQ2ZmZPS9QFzXk06JvVL0k8qu4Oub2QJaFbg-M5tj-B7kYnmYR44o57GzouyTf5vo7sR8SJlYPy2CmR7b2f8Z6DasnJu2PDt1cjI9lEOKQ-VLyVwgxbfjPN_HOAahRHjTiU3wp_H4yNGKyjk92w0Mi_dz_Y_0hRozpqkyer5p3ZaMCfNLl6wy7AKBkN-7QzqpyRUDXSqM2e7CXfOnbB5rD_9uzMYeql7KdIEDrj_3v36uxTT2fsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2f385bca.mp4?token=ACSYPTLtEm0n6o2PM_p1_M0i-VZ38nnPV86TlEc0pQQ4Bi7OmVcWxgESOJDIj7-Hgaa0r5HEKwLaAbuT9YhASLYo8re3nWj0rKQ2ZmZPS9QFzXk06JvVL0k8qu4Oub2QJaFbg-M5tj-B7kYnmYR44o57GzouyTf5vo7sR8SJlYPy2CmR7b2f8Z6DasnJu2PDt1cjI9lEOKQ-VLyVwgxbfjPN_HOAahRHjTiU3wp_H4yNGKyjk92w0Mi_dz_Y_0hRozpqkyer5p3ZaMCfNLl6wy7AKBkN-7QzqpyRUDXSqM2e7CXfOnbB5rD_9uzMYeql7KdIEDrj_3v36uxTT2fsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هماهنگی با سپاه، لازمه عبور از تنگه هرمز
🔹
نمایی از مسیر اقتدار و نقشه تنگه هرمز که نیروی دریایی سپاه مسیر امن آن‌را هم برای ورود و هم برای خروج به جامعه دریانوردی در سراسر جهان‌ معرفی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/akhbarefori/652702" target="_blank">📅 21:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f344W5MaEUFse79uQENlh8lx6_CCmMXVGBSBOTGvG2j7mtT-BEPT7D55JfvbqClF-TLI3cmZ2nZRc8TPGqZ5QoWuwB6b16X9ggJK7cNT-iHi1O2C6R_KrM9eTYlPfm7y-usgQCCk7g03UfbgNSTA914vo9FL54coFQJ6Vz6__j6c6rRmqDLHOYj8YTfoa_PQKyDmvBywnanEqIRv_wEMnbbPyL_2zZMukPAcGioi9KcMWny_KTXy8Tg67IvWALqA5GD4onkaJRRA24sD9n57rdwiWNrZM8tOgYmtzc1VfLFgOA6GGZIFEavofxJuwS-bLrDuiQMqAvdfO4aC4Qmb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار مشکوک در باب المندب و توقف چندساعته دریانوردی
🔹
طبق اخبار واصله از منابع موثق شب گذشته در دریای سرخ و ورودی باب المندب انفجار مهیب و مشکوکی رخ داد که تا ساعت ها تردد کشتی ها از این تنگه را بدلیل ترس از انفجار های بعدی متوقف نمود.
🔹
تا کنون هیچ گروهی مسئولیت این انفجار را به عهده نگرفته است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/652701" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96c671aef0.mp4?token=GgHGa8ffNlCHHGZq8tBbpDI64TYrHmyLNfVUFOE8HNbnUv0O49jt716182S6pjVaGdhM2-cqXTeDbFQB6sRqymX8YWFqK5JGOgRbNEMiDazZ1f3KaodcVvzvoBif9mOmXUvqFxCcU2s3qFLXhVYAjDbzlDBQd2mH8uOzkAUgFWr8SEiKUxN-bMRof53Sl-ZTfi0QMfhZ0VDMs6jzhBUB-Gk0iL3WEvzRPXAmFchV-Dcr-BcPO-_Y0z3gTpvuf4JsUMwlhsz336-KPstjTdvHZjiPiHmIesGVzb0wXr6nnIYr_EeAX1YueZgp3N_pWHgykwwiqt96pPdgupjWC-mIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96c671aef0.mp4?token=GgHGa8ffNlCHHGZq8tBbpDI64TYrHmyLNfVUFOE8HNbnUv0O49jt716182S6pjVaGdhM2-cqXTeDbFQB6sRqymX8YWFqK5JGOgRbNEMiDazZ1f3KaodcVvzvoBif9mOmXUvqFxCcU2s3qFLXhVYAjDbzlDBQd2mH8uOzkAUgFWr8SEiKUxN-bMRof53Sl-ZTfi0QMfhZ0VDMs6jzhBUB-Gk0iL3WEvzRPXAmFchV-Dcr-BcPO-_Y0z3gTpvuf4JsUMwlhsz336-KPstjTdvHZjiPiHmIesGVzb0wXr6nnIYr_EeAX1YueZgp3N_pWHgykwwiqt96pPdgupjWC-mIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رادان: از آغاز جنگ تا به الان بالغ بر ۶ هزار و ۵۰۰ نفر از وطن‌فروشان و جواسیس دستگیر شدند که ۵۶۷ نفر از آن‌ها موارد ویژه مرتبط با نفاق، اشرار و گروهک‌های ضدانقلاب بودند
🔹
دستگیری سربازان دشمن و وطن‌فروشان در اغتشاشات دی ماه همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/652700" target="_blank">📅 21:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib3FxWBqzVDfBcoHTV5Mk52qLxsfeG4IqyxanME5sKh9V4DA94ck9ESUdgVmZvy9iKldHPN4RL4FiJNsJv0d1rnyJ3k3vpSHd6E7eSBDwtVcZKZuQg619gW5WqWp02XNTBGKo_vTqv2Lj1tgToMqgmtHNhTHegMLu0_SL_2ljLvjDF354O2gEG-N8VAKhgk877BNAqZ13FeqdWCaVzp7MwCSN8lMkvnLe8KeeIXEb-VMdzcxL9omLHgeL6pbd2xfwMhBmrIvYfqXfLGUV-YDIv3jkzb4-4rs5-NrFY66q88TqD3b_reAGFGXg7vxhG8wVxXR5i2Ci0dABT56_Wra8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضایی: هیچ قدرتی نظامی نمی‌تواند تنگه هرمز را باز کند
🔹
سخنگوی کمیسیون امنیت ملی با اشاره به اینکه آمریکا دلیل اصلی اوضاع کنونی در تنگه هرمز است، گفت که هیچ قدرت نظامی در جهان نمی‌تواند بدون موافقت ایران، این تنگه را باز کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/652699" target="_blank">📅 21:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q46Hj9rMpPkiZj1IPyH4foKrq9zCLNiR16OigFpm1FNeGKtyzFu1ao45mV-yaFde6cyQJxV-FyR6B8q6r6npZ9XW09H4cQWBzbLCdfDupaK9Pp3nv3LNlsF1NC9FLWT7-PZXbV9sGhqZn8MTlIlLcDezO40wl4nKPJZKfadXGDdN7bOApfZJIKfIpwfrcLN9DMGG13IOY92XyXFlIGpjTp91nomfRCHGim5DKl_hHGawZkyZchPbraPf8POjpeTaFXFfGFaQiyvjcA3ZTkNRX-PASXAEuPoMjbNaGJ2aOfq5xqVt_pmufJF_DcmU1efIwGx4sRkHsZZKHTdZt8LiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مافیای گروگان‌گیر
🔹
اقتصاد ایران در برخی موارد در گروگان مافیای ذینفع است. گروه‌هایی که نه از سر ناچاری، که به خاطر حفظ منافع کلان خود، تصمیم‌سازی ملی را فلج کرده‌اند. هر طرح ساختاری که به سودای بی‌حدومرزشان لطمه بزند، با وتوی پنهانشان نقش بر آب می‌شود. مهمترین مصداق؛ قانون مالیات بر خانه‌های خالی و سوداگری و سفته‌بازی در بازارهای غیرمولد مسکن، خودرو، طلا و ارز است که زمین‌گیر شده یا به خوبی اجرا نمی‌شود. یا مافیای فیلترشکن که به جای شفافیت، از بی‌قانونی ارتزاق می‌کند. در این شرایط، مهمترین وظیفه قوه قضاییه نه شعار، که برخورد قاطع با این گروگان‌گیران اقتصاد است. ملت در گروِ تصمیم شماست.
🔹
هفتصدوپنجاه‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652698" target="_blank">📅 21:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN4LchX0_UQlzKUnkS5XkUH6tgQ8iqCCPSnYwv5iaLDYUrlQKPcI2alzstjR4Vysk22BFWS1vWyOYctPCWsQ4Yh_-XfEuczO3h_Bcdn5JIUUjHjm4Z1cqivXHTUKGkzrah7vzPjzVFVVPp8HEeVA40VziNstNmYDAHckTpvCe1qEVypafM2p54O00MQnN9tjkyJEEmC91btRmR3bEoim3c810RkdLMnM3G-G9yHt5RoLJbcsvZ48KTscvQULF4_WN7ITEOIooswuQ9k80FswrKlpambjcpi64I8WrqA6ZSrKJzy8bWQgHY-NKlzOVKIpFh9-vZrC1dbdS46wfJ6ViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای نقش وزیر جنگ آمریکا در کشتار کودکان میناب
🔹
وبگاه آمریکایی اینترسپت نوشته است:
🔹
گزارش افشاگرانه بازرس کل وزارت جنگ آمریکا افشا کرد که هگزت عمداً جان غیرنظامیان را به خطر انداخته است.
🔹
این گزارش نشان می‌دهد که پنتاگون هیچ‌یک از اقدامات الزامی برای کاهش آسیب به غیرنظامیان را اجرا نکرده است.
🔹
دیدبان ارشد پنتاگون در گزارشش اعلام کرده که کاهش شدید بودجه و نیروهای «اداره کاهش آسیب به غیرنظامیان» در دوران پیت هگزت (وزیر جنگ آمریکا) توانایی این کشور در حفاظت از غیرنظامیان در مناطق جنگی را عملاً از بین برده است.
🔹
بر اساس آمار سازمان «ایروارز»، ارتش آمریکا در دور دوم ریاست‌جمهوری ترامپ بیش از ۲,۰۰۰ غیرنظامی را در سراسر جهان، از ونزوئلا و یمن تا ایران و سومالی، به قتل رسانده است.
🔹
در جریان جنگ با ایران، تحقیقات نظامی افشا کرد که بر خلاف ادعای ترامپ، حمله به مدرسه ابتدایی «شجره طیبه» در میناب که منجر به کشته شدن بیش از ۱۵۰ غیرنظامی (عمدتاً کودکان) شد، توسط آمریکا انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/652697" target="_blank">📅 21:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652696">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui1uExhZOay5nvB-RmCP90Eql5MP-YXi69nMDgo7IENP1E0nUS08ucgDWt_RCfnLS3pyH_t_jMyY0LuL7r2fTKeZoPkoABvGWzLDYg1OOSdNxdwBxFEVgtQebT0RsRWbcVglxbY3jVbRra-c8V2EYl0VwvSGpmjLrUmn2Mb94U_LAOt-uwiwqP5iRGsC-HEz3GunpJQC5tGDjWViqM14CCacnptXPBt-wyfgqUkcRtmYu69v-siTP1XuipAzCAs0PNZpBL6rgLmr60RFJYJBgfbMKlfokmRb8Qy35Y6aS8zEjR-qlwcVDA23Qz0K9SfTCkwFFZo3iVug-PWPGkAA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار وزیر نیرو به پرمصرف‌های برق
🔹
مشترکانی که بیش از سهمیه خود، برق مصرف کنند، با جریمه قطع برق رو‌به‌رو خواهند شد.
🔹
مجوزهای لازم برای قطع برق مشترکانی که مطابق الگو مصرف نمی‌کنند از نهادهای مربوطه گرفته شده است.
🔹
اگر مشترکان، ۱۰ درصد مصرف برق خود را در مقایسه با سال قبل کاهش دهند، روی قبض برق آن‌ها ۲۰ درصد تخفیف اعمال می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/652696" target="_blank">📅 20:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652695">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ به Axios :
🔹
«وقت در حال تمام شدن است برای ایران»
🔹
و هشدار داد که اگر ایران پیشنهاد بهتری برای توافق ندهد «آنها ضربه بسیار سخت‌تری خواهند خورد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/652695" target="_blank">📅 20:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8468cec1.mp4?token=dP9EPEnbLW6on9Q4iLD96z-Q9Zd6WLUiajV0why9YAnIIMYBWYbBoAq6OMPNsyKFjgfT-mUiTL6S_KXiymhg-omi3hTtYBodrXNhIeu7Imb7o4kP2l5jmKVol_2FqyDwn-En3SfsJJwY9ZV7V8cKVxl47JJeVmPDTA1im8oZy0045O7YM5r0dX3On4hd26vocq-uLP0_d9uOK5RceoVObIlScZQOkppLBYjSbjm897Azdckp0qh3E58I0HUzc9D0z9M6RZVS4dZ3FpC2I8ROgXMUPQP013WfcyfBWo5MQv7rpcfdskKrsa_H3LdbjkheKe5z4jxJQQC1tgkOeJpQZJZVL_jo7fNajAt5dT71TtKJbRMC75GbxvNakpfAICf51klfVgUedo_Y7XiEmFVjvYWXhjoXMqmTzQuHDgKxvJ2VfWnkhV8zvbopv9jE9Bfc27CjSCJsvOw5zTl3A3CLu5ZLcCs4LjiAcS7Q-8MdUvhzFKg8nVzpees6QXcyz4qLcxDu4r9j3uzDWsP2i8ZjeN0H9OyslK0m4Nu7Vy4ATYqDp0NBHhlnEWjt4YQd4LcQUU4U0a2jsdOqmQeMJ9xAPELAga-nIWsc8urXXpr9FSF26IkPu4NcypCVWa68M_ufUfi2Ojv2ip1FrnP_8jzJ_ixFBtrupHPSoPWUVn6Rb08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8468cec1.mp4?token=dP9EPEnbLW6on9Q4iLD96z-Q9Zd6WLUiajV0why9YAnIIMYBWYbBoAq6OMPNsyKFjgfT-mUiTL6S_KXiymhg-omi3hTtYBodrXNhIeu7Imb7o4kP2l5jmKVol_2FqyDwn-En3SfsJJwY9ZV7V8cKVxl47JJeVmPDTA1im8oZy0045O7YM5r0dX3On4hd26vocq-uLP0_d9uOK5RceoVObIlScZQOkppLBYjSbjm897Azdckp0qh3E58I0HUzc9D0z9M6RZVS4dZ3FpC2I8ROgXMUPQP013WfcyfBWo5MQv7rpcfdskKrsa_H3LdbjkheKe5z4jxJQQC1tgkOeJpQZJZVL_jo7fNajAt5dT71TtKJbRMC75GbxvNakpfAICf51klfVgUedo_Y7XiEmFVjvYWXhjoXMqmTzQuHDgKxvJ2VfWnkhV8zvbopv9jE9Bfc27CjSCJsvOw5zTl3A3CLu5ZLcCs4LjiAcS7Q-8MdUvhzFKg8nVzpees6QXcyz4qLcxDu4r9j3uzDWsP2i8ZjeN0H9OyslK0m4Nu7Vy4ATYqDp0NBHhlnEWjt4YQd4LcQUU4U0a2jsdOqmQeMJ9xAPELAga-nIWsc8urXXpr9FSF26IkPu4NcypCVWa68M_ufUfi2Ojv2ip1FrnP_8jzJ_ixFBtrupHPSoPWUVn6Rb08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«باب‌المندب؛ دروازه‌ای که اگر بسته شود، هیچ جایگزینی ندارد»
🔹
از جهش یک‌شبه قیمت نفت تا شبح قحطی در کمین ملت‌ها؛ این همان کابوسی است که جهان در لحظه‌ای که تنگه باب‌المندب به طور کامل بسته شود، با آن روبرو خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/akhbarefori/652694" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یدیعوت آحارونوت، به نقل از یک منبع اسرائیلی: اسرائیل در حال آماده‌سازی برای کنترل ناوگان آزادی است که هفته گذشته از ترکیه حرکت کرده و به سمت نوار غزه می‌رود
🔹
ما کنترل کشتی‌های ناوگان آزادی را به دست خواهیم گرفت و شرکت‌کنندگان را به زندانی شناور منتقل خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/652693" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhqTtRUtOowOOhORgqG26NV-eY-FN_VUxMMZ5OQ1sIs96XkYP_OSWmQWviWcX3DN2rlU1_9VUs5VdeeHbAySBS7oTXF7POp05djk6Ew2wDKJ6DANiyJJqIPtEr4wXjloHshq2ndoFRprNEdf_YuoqDL5o2v8jUOVnf4tgYoMRVW-tgJpzNDOaIg7DR-6Zgk4Y1AVQEGFqhw60UmGhVeKL4wfNDk0obIrrROAvfE3YykJv12mVYkiBxAxEcTFCu1rR6EG_vilT3rm-25MdO8kvlyaR-DSDuCxvuMaLg5Dyto8B5gGWhEtOmSJAxDlFBZK-6_X80U5FjMvlGOcuqJfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در مصاحبه با رسانه صهیونیستی: ایرانی‌ها باید بترسند
🔹
در ادامه یاوه‌گویی‌های ترامپ درباره ایران، رئیس‌جمهور آمریکا مدعی شد: به نظر من ایرانی‌ها باید از آنچه در حال حاضر در جریان است بترسند.
🔹
به نظرم ایرانی‌ها باید از من برحذر باشند.
🔹
این اظهارات در حالی مطرح می‌شود که رئیس‌جمهور آمریکا ساعتی پیش با نخست‌وزیر رژیم صهیونیستی به صورت تلفنی گفت‌وگو کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/akhbarefori/652692" target="_blank">📅 20:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dveduCql-OuG5slZbUvUftepDIa5Z6PkbGW5uiS0gm0vPYaRALZmfoY3xmDa3CUJqkNek7iuFevfGH7mXIBvPvz2--zYw_2ss8O6BrE3lnSOvyMQWASC6VfgHCEDuhKHKVoWA4J5AiacavrCRyv8bQB1XU29rGHgqO6_2HMMQ_Ysikal0qop5huPxUUbZf3EmlARWwGoqWHXxVl1ioRbAhMDhslVyzS3G066cPTOWPSvbzVFn7IOVwdM8xgJZcjlCFz3BbTnMkwc26syQYnNobUv8ShPQgoNOVpnqkuUB9cy1J9uFlaMx4qzUEDMXal0qUiOUxubOBSA4-onjnWtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6n_LN0x2MJKBnEiWOWDF6gyefDrbDfVYrjrpdEYMurlc9qRwz6g6JxTUMm6hemz6KYQ7t9MUn8dsvsNBtQ5k-7ltKWBvXYxpOjl16o1hZjh8bqUY35iB5IYUspC0IyTwfsTGv7NAOb4YT0Splx886YHOdgTfdVu6k4R3kgB-VC8DBK2tVyLnueHdgyUFkZV6ezJ9XOklGbqsacXE4S7PwHGR_1UhxVcayrbGbv0VbVl3d_U-xl_xks7-m7wmqdclA7d2-aW_ZdNxFfLyk6TFuwh_UXp5rj-02gaBhzbrHkC7ObT6ZqxNo0W2CEXulRjmp2397quolzllQ1F6slemA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxuVIlLE0tG_uyMUpdLo92EcvckG2SvkREIJzKmWSirfyD5iKBmeT8a4VmqaefspFs5rvM3-8aLZhJ3hMzejd6y0frdCRRgG2shIk2Xk1OrNm-ENYv29wr0hu1Bze-Y43Ov62lWVSKsgRZnkJlBRY9MeKPk1V9wvaXZZJvnZHrUJU3Pb4oxv8AttKQVi-WVNmBF_upR3bEptgLdFt5ufqT1tCS5HTwEKe8njipNz3CM1aYyxExzyjtFzwEinQFSEP3fps8NZDm_oqgjKuOQDadHRhLrlxAu7UZBS1C8-1v-2POSLpPHIbl_RTNW8ZyeNpQ3mEwFdb504k8slj50cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBL9zV1Dq1GvC9fPeyVzorGEmgqshVXWoTym9-XI6_xYcKyGsE0YSG-rkkzXE1KSWbRz7_TD58L2pwc3FwkScnC7LPwLLNmF_OSe7GbaBP0nrKnYrOLMxy6FgHQyUXEZVDkgELbWSMu60P5uxOswuzGlkr0QFtehgPFJrF7wTyQVnoLcj6oTZwDpM2OhhBBhTzIY8nT6iQNxmMgS4LDQ6vjMjxkjRMvRzfy14UA8pv4sYC0IxIvFhbCoToq1-K2VNVKl9uoyaV1zbGW79jaQzAQwq6zTTcONQzxqN0INGDu-bHqRyxisgI1buCEL88FtQGKxsbKTVxlsQxMMbxhTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCNtPDjOJEB9VrLHcas9daYCOEMKOBeuIrwh2dpk9Mxk7JwCAM9O3D-YVZoTqCoTUxpf0r73hSV18ukDz5F2ErR6SC7-0BOBRdE0qmwW15hqeATGWuI5x2onkqNmcwl8FubuC93WLP0XJd58baXSht9dJOFTexnAnwdU_fApZo2uJpk5IWetqkXH7OGP10MSpWab4n2SWhTfo1BN2FE6bcyqcHbKwLm4rqxRRNWFR7fMY-PNXagoOzqRWhqMUIV0Jgl3ciF45k92K85dPaF3VZAJo3ur_UgcNImSzPmFTfCGTWTqMwh-hvw8m8WKMzb0c7HX-6dj-IcBT5wsts8zGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blT1a2S7_kW7nG94DdQyJRgq5vljDpTMLygpsaWBSF0KiwDbhrQ8l-nnCiSiGwhoxVjXeaiZilwgMbpEVO-FEokD-jAgDGJYcgrXAeP0WCXVoKsOqr9BGz16PfEkOizP_hCv3UvoaguNhu6pdxmBZfjk3EHO6Y1dLkg85jHdxebyFXts__yB5TyGA8cdck8eSUa-WknPUwtsDFo3ZTSQEUEMVSwRMaI7FVhOZ8YSqp3pN2-dykX62O1RxNVX5Q-PiuInpCVlszjPT0sAta4eeR_ef_zb-ZxLKHgTN6MbuTg6GxGPh78ugyVK398yYvuBOfp_J-Cv4P4aZPa-YWjxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzqDA8j9nfoBbLjqZdSiPSwm3mf9gT3AxN7Ququp_xPDY_FoaW47CGs_Kr8Y2QWAgTNkcE58s9wZZgINQQtqhrlHoki-YUmJdIYda5ruWWwwRmfkv5pEe9IME4ocIE7Cvbmj0wnT24SsKEtyqgvrzwpjqpDeXBLjcMa1N4cXCPV00CERjgLfXJO4EsnyFBaUxJyXtfzyait03JLklUFiThhZb0Wcs52A2S5uBv7kNYKwAkjoqdwF5tL5QlnJFNIEI3Yj3Mz1o80VumBQntPz-8_eEtQH60qTBA0hrS6MDznMeNbAYuwvnx81A8CwUBQEcBuNfYEweVg5kzJtNzCbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f20vMxA6TN3ShitdJCOwy1nnvidbDicvpJs2Aa4PqLTBxsMyN19z2vKopQ6qx1bMUY3OyQWMV_mdARfHFU-ka3Wlh4kor8quzyhnM88nsKa7qUBJl4NASDOEWS4349p1MMTQhtJyoa3GVZGqBIZgQf36O-lwnXbcjHCYgpBISdbZ4dP5eTiZHe6J4o7MaS5iF63lDyI65rG7pN4Shh10yxp1LKOc55o_00eyRsokRC4Z7ZbCo164QIEHVGT6Ly8DmlotPhzMAIBxaxraxfG3zm8njST5_6LhiOuMvZJwA3vKbQKQbyPDDIjxBkXwRpNDozOv_031JF4uv-oILW7udQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk8q0XybYjzgGuTs_551MqtLwpRRUdHn1DhEMNfo-4O26P5ytl51uHDVV0-LUvn7FaBBD73S_3nNjYdd97f0gSllknexsvGJYEqoZFPcBSCWaeEl4_xV4dckaHgYY9_x31V3RYTjlWQl8xVquzI-xjlvSevw5tajihvCt5VlygvR2abEYhraNFif1i-1YB2mmTAFiB1d9sg1zR7ZUAgStaVrnqpOW-BPJDwOqVaaGioVX3DdFLZCLliZRoco-lzDJ8N0eoQQ111kRLUFogVAN24hxOBxxq57AxhLo-x3omQkAlDGUI-tK5hVTMixTMiijuTFIVi7LYjAUe_ryB-P5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjsLRF4zQPEx7xp6c9U4A4lEau3TJIHDAK4rJgojJc-UlU_j6Uoysy-FVcKsi0eI1mo-v1P3_4UDxIS9uIWrtFdXWIeDXh4F4mgCZa3muv8kIU_tdIu2MOz24StbG15CDhmpZbbD9rhA5bk5I_P8352IsX9m3_9h6BaiwiCnj22ya_4ebjznfR1FWTgnftN7fyOeKXEctEjZ79i5JgG3WFf7uVhGmtiBGLvefHGzqMfBSre1SJugFs92OrLhtI2BktxakoiEzRAJgPTmqUg_vyUJOitH8XwkPOV75RMLpIZJt2k6A7tMQn9LP8Y2D8KE6er8UWb1lPKNlHlgoQ7RKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/akhbarefori/652682" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDvDKRhCESP-daiu8XWVxVyiUdBoZhFHaqy8i1MASWWl8zRu-Jm36LATpCI_6DfCV_Y30Ui0hCI2ujeLng1-5voxW5xC2rNjHMNxmxJxjStOpW6visCZuQ3DME0l1f3nLEVFkWcBYnKonC9q9Rma_cTpBHToy5OEwjeh6zfzQOG2MKGkwldoHgoC9fcUp7I9RGkpqMwB4sNad22QFrYuxFeMGGKKOKrrxbwjcizjjCxzvNawrKPrJu_bAa4OZso6-JbPaNytmfw7N_1AMNrqNIWMOF_-hSzOM8hSWYAik9y196oHmJVpohepxmUICQB_VNHSlAPYIVwzQT7zh_e-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست با دامن شدن فیلترشکن فروش ها به رسانه های معاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/akhbarefori/652681" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSqjkbmdDlFsvE0rWchlsBNiCU8vRMgDcTdX4z-P9IgbZ09ZwqVRcnplyLikPHeU3RDplqkp7yco8KrfpkI3OwwqYoO8gmqlzi2zfrrYDdxPFzeRmIzArhe7JpnZtUJaxS0aCRnYywbpWc1HyimCkgM09F1EHZjrqa3H1AAEaBOhLvgtaTr1_IqZ_pQ6c2tkpUuZOQg54nHpAwlP1GKSP-weGb8Zv_kBHtqIXNEKMbNqyM7v4pJaky7f6spd4Dwv3pftR-1_xDIqEN_ogpRmRtLCiAXelR38GU1baHOrT9uMWyDAV9E46CDkHqTfKK_NKLkKIa8IOjUZ_7wc4ibiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان بارندگی کشور در ۶ سال اخیر؛ امسال رکورد شکست!
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/akhbarefori/652680" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1650f70a.mp4?token=ahuZn1hp9g1bGUzUCt6mh_680eBVwh7kbBwmETVsWfjGske52ObNyo4hpjfDTpSWw09FvV6t_FIKMi_Rt_HiziO-i2iRCm-LzC8LXk9KOYE_tMqU-Si3KGWtBEIaiJdN2z5pVv5xaAPgmDCKL8UQ0FVkk9p-4lTLBlYzMF21LN5nCq1459VxtIF62XBIPK8nW7aMm_WMH5wWSURoQMYw47vHuLG21gHG7rptCvrTML6kqVsrCCFePrh_PfCFkreyj17Tte26ZxCjVmGbhO50-l0-DA9bpxfnwJ9QB8O5f38sU29GSO66d_UmAHiFYmu_D-kRGWvlCfSONx0LBs8StLpOKeUFLqv0fBz-7Abm55WYYI6o_9Czubn5rEHM7DJiYWDqw6WhN2irjxqsL_ZuVi2GdiHW8v4eNNopd_V57-BwyFTSzfggwSeILwyrga37c0yNDgknK3C5eHD-lCm1Y20bU-bs6i_tMxuuXIkCX5seT7rQsVqSoCK2jzPFSs1idrEEK5anTNeha6i2YxiwC8xEFoCRpI7dvC5r2YE9ulZtAm8bJTmqvTnj3S7oWXWTOk6o3E2ee_gRZC9Q7nmlB1AO2gfqFYxs2UAtCiFb76M-TNoVSc2KR-X45MAZgX0yVUF6c70eIIHrIUT-oeStJLkYhKxrDKBTvUI1K45e5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1650f70a.mp4?token=ahuZn1hp9g1bGUzUCt6mh_680eBVwh7kbBwmETVsWfjGske52ObNyo4hpjfDTpSWw09FvV6t_FIKMi_Rt_HiziO-i2iRCm-LzC8LXk9KOYE_tMqU-Si3KGWtBEIaiJdN2z5pVv5xaAPgmDCKL8UQ0FVkk9p-4lTLBlYzMF21LN5nCq1459VxtIF62XBIPK8nW7aMm_WMH5wWSURoQMYw47vHuLG21gHG7rptCvrTML6kqVsrCCFePrh_PfCFkreyj17Tte26ZxCjVmGbhO50-l0-DA9bpxfnwJ9QB8O5f38sU29GSO66d_UmAHiFYmu_D-kRGWvlCfSONx0LBs8StLpOKeUFLqv0fBz-7Abm55WYYI6o_9Czubn5rEHM7DJiYWDqw6WhN2irjxqsL_ZuVi2GdiHW8v4eNNopd_V57-BwyFTSzfggwSeILwyrga37c0yNDgknK3C5eHD-lCm1Y20bU-bs6i_tMxuuXIkCX5seT7rQsVqSoCK2jzPFSs1idrEEK5anTNeha6i2YxiwC8xEFoCRpI7dvC5r2YE9ulZtAm8bJTmqvTnj3S7oWXWTOk6o3E2ee_gRZC9Q7nmlB1AO2gfqFYxs2UAtCiFb76M-TNoVSc2KR-X45MAZgX0yVUF6c70eIIHrIUT-oeStJLkYhKxrDKBTvUI1K45e5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده پیشین فرانسه در سازمان ملل: با ازسرگیری حملات آمریکا و اسرائیل، ایران وادار به تسلیم نمی‌شود
🔹
ژرار آرو، نماینده پیشین فرانسه در سازمان ملل: آمریکایی‌ها و اسرائیلی‌ها ۴۰ روز دست به حمله زدند، اما نتوانستند ایران را به زانو درآورند. دلیلی ندارد که با ازسرگیری حملات آمریکا و اسرائیل، ایران وادار به تسلیم شود.
🔹
بر خلاف ادعای ترامپ، ایرانی‌ها توانمندی‌های نظامی و ابزار لازم برای پاسخ تلافی‌جویانه را حفظ کرده‌اند. اگر آمریکایی‌ها دست به حمله نظامی بزنند، این اقدام نشان‌دهنده ضعف و بی‌برنامگی آن‌ها برای خروج از بن‌بست است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/652679" target="_blank">📅 20:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5sl9Xje9AMm48cKXPmks-tZyK6QJ8XvoeJXupo9WGa4_Yy14sh4dcqalp3PSiOy0JNQ3wRhT-k4YwkQx7cax6vlWIj9MxeUICBCVJGcHNyEnhRJGRSJEgNWVi1GTrwfSAIXb6kPEx1zbpOgj4z5BP_gF-x9EZeeazGYntUlDcIT2O4AZ-dYmsR_5TT5LAE8Nt2GbJBbNc9AvAUDvQ4R51a16heG1U4ljYwZ8Wu3dVEaNRfyWH70ckBdUSOPvzUAGW7MJ9pVAUtA9umvUdioRGuB2SlcHSqDAsdefOXS9DLJcq8VJA1C5sCmmJ8Uo9HXv8UghZAnB5IQw7FuxUpzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح عربستان برای ایجاد «قانون هلسینکی خلیج فارس»
میدل ایست مانیتور:
🔹
عربستان در حال مطرح کردن ترتیباتی مشابه «قانون هلسینکی خلیج فارس» با ایران است. این توافق فقط یک قرارداد سعودی-ایرانی نخواهد بود، بلکه به خلیج فارس و اتحادیه اروپا گسترش می‌یابد.
🔹
هدف آن تثبیت عدم تجاوز، عادی‌سازی ساختاری اقتصادی و مکانیسم‌های نظارت و اجراست. اما توافق عدم تجاوز خلیج فارس-اتحادیه اروپا-ایران بدون آمریکا، یک خلأ خطرناک ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/652678" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba03a97bef.mp4?token=wB2ZaL00oz2IIpG2VaJD7fzhKqEXCE1n9L4OJ7rWytM-XFqA6QsIyiJ0zk-I2AweNVZaaztpoYr93jxs9PEPQ1D0GBDHo1iTyVfav_D12ZtP_jkwo9z_zD1gJhWIc80m78RAPtS2lxbzVbE0BirHLgCmOUa-0uxC6avGcdmjfeUa9yq1guMO5kn86Fqkdtz-ykeCkBI-DkkXlWQ9h1Cvqr6yPWFZxywU4FowgycsS5IbRwhQy7E85fPFbEG5H-FmWne1IYNqxELo4vSzyFxUmEB8Xzbj9k9qngNbXqxosieH2uzm8Q8HhNRXtUtYu2boHjAvwDdAkExmB7vGHKC8PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba03a97bef.mp4?token=wB2ZaL00oz2IIpG2VaJD7fzhKqEXCE1n9L4OJ7rWytM-XFqA6QsIyiJ0zk-I2AweNVZaaztpoYr93jxs9PEPQ1D0GBDHo1iTyVfav_D12ZtP_jkwo9z_zD1gJhWIc80m78RAPtS2lxbzVbE0BirHLgCmOUa-0uxC6avGcdmjfeUa9yq1guMO5kn86Fqkdtz-ykeCkBI-DkkXlWQ9h1Cvqr6yPWFZxywU4FowgycsS5IbRwhQy7E85fPFbEG5H-FmWne1IYNqxELo4vSzyFxUmEB8Xzbj9k9qngNbXqxosieH2uzm8Q8HhNRXtUtYu2boHjAvwDdAkExmB7vGHKC8PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفوذ دستگاه اطلاعاتی ایران در قلب نیروی هوایی رژیم صهیونیستی؛ اطلاعات فوق حسّاس در اختیار مأموران اطلاعاتی ایران!
🔹
گزارش ویژه شبکه عبری «کان» رژیم صهیونیستی: دستگاه اطلاعاتی ایران توانسته به نهادهای امنیتی اسرائیل نفوذ کند و اسرائیلی‌های بیشتری را برای خیانت جذب کند!
🔹
پس از پایگاه هوایی «تل‌نوف»، این‌بار پایگاه حیفا تحت نفوذ دستگاه اطلاعاتی ایران قرار گرفته است؛ اکنون اطلاعات و موقعیت‌های جنگنده‌های اسرائیل در اختیار مأموران ایرانی است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/akhbarefori/652677" target="_blank">📅 20:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
احتمال تغییر ساعت رسمی کشور
علی بابایی، رئیس کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
موضوع تغییر ساعت رسمی کشور از طرف دولت است و در مجلس بررسی شده است.
🔹
لایحه اصلاح ساعت رسمی در نوبت صحن قرار دارد تا تصویب شود و در روند حفظ انرژی در کشور موثر است.
🔹
تغییر ساعت اداری به جای ساعت رسمی کشور، تاثیری ندارد و ساعات اداری تغییر نمی‌کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/652676" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
خرید ۳۰۰ پهپاد رزمی توسط کوبا
🔹
بر اساس اطلاعات طبقه‌بندی‌شده‌ای که به دست وبگاه اکسیوس رسیده است، کوبا بیش از ۳۰۰ پهپاد رزمی خریداری کرده است.
🔹
گفته می‌شود کوبا از این پهپادها برای حمله محتمل به پایگاه آمریکا در خلیج گوانتانامو و کشتی‌های نظامی آمریکا استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/652675" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای رسانه اماراتی از استراتژی اسرائیل برای جنگ با ایران
صدای امارات:
🔹
استراتژی فعلی اسرائیل نابودی کامل ایران را هدف قرار نمی‌دهد. بلکه بر انجام «حملات دردناک و قاطع» علیه تأسیسات ایران تمرکز دارد.
🔹
این حملات برای شکستن خطوط قرمز تهران و مجبور کردن رهبری ایران به بازگشت به میز مذاکره ظرف چند روز پس از شروع حمله کافی خواهد بود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/652674" target="_blank">📅 19:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi2Y9goDCTKjGe3FcHvoYo4aOlHmBlVP8y6SaBffSskgPahr_-SEulA6iG7ijAIjgOjIAk55p2wF0r6XZIbo8_US4QbyNaNVkj3xWZoR7_XFCHWhdXkrgzjgTqb6INYyLTS3tN6j21ct4NQX-k0ZeFOg-rHPyebbmgotZpMU7ehrTiDh4uC3cGvMc-gZ9UGt1zZon8qLwSAHTt8-s0hDCgTolz4OgF2Qa4d2h1cSEHaf23fzJgje_tEHTZP-BQPs6VLZwEORj3ucC8rSs_0jGALm-6eRGxpFJTJ9hS0CqC3z5wl59Dfj86RdQWV6KIIIO1xFBNVXVQDyHLHTOoFKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون حمایت از خانواده مجلس: میزان اعتبار وام ازدواج و فرزندآوری در بودجه امسال ۷۴ درصد رشد یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/652673" target="_blank">📅 19:28 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
