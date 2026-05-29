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
<img src="https://cdn4.telesco.pe/file/HOtJqoBTM3e0kQU789dsZ9QWLVuZpxOb9OBJYB8n6-JTA02tLO1rnGrpBPUWZ3wjXRGMzP5iWnl7xiAZJS8xmLxNU0fpj37-XKN7vJfsACaTdK2WLna2xhYm_XtoWMgpVQAK3TV48_3g1qQs0dA6sUe2L8DVelNkYm2MF8Wm23c0n8QoL1z5FHdFLryele4SLoc5pWlK75TyVOXSxaJLrDdPyCXvvdqsfKIuUhqmIYngA_AeHJkty3AXPhYHSR3HZ2hGXHKuFHKHMhsYDJFA8j68S417CeS9ao4-sAjgWafw9J1PsZPPP49OVoaplqSaG4IUIIW1NR9ZT0Lt7YRg7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 280K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-12858">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تسنیم : مذاکرات در جریان است و متن توافق تغییر هایی داشته است
@withyashar</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/withyashar/12858" target="_blank">📅 17:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12857">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzQswYxV6hC0YK6L3_rVd8tCaihPxf2pk4PXTTOaPnhYH4851yRPl5H8cG8dtqr8wjhj9HvScdzMeSW6vl2hOMN7abA-vYzzEZv9WWtjeOQ0xaf3WJM14kmIKU53aKwRksgtJd-uKh37ZJBsTdmhG8JffmJgB5Bd20vgPD7-xWr_VZam_DD1ttpZg8XYpyzWlqLQn5bSSg7PNt-UrHE44gpE-ZBWV2-n49Q7ADCKiydS5RB7yfAU9DCvhhEo8K6MpDPGJSVivu_Ud3hhGKIc_c5sN3x0j1JaqRBe_G5gpTkPr-Iyn2qJwdvtxyeDYd9fwZQ87TRUAVa8tno106q1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مم با قر خالیباف‌ در اکس :
۱- ما امتیازات را نه با گفتگو، بلکه با موشک‌ها می‌گیریم، در مذاکره فقط آن‌ها را تثبیت می‌کنیم.
۲- هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳- پیروز هر توافق، کسی است که از فردای آن بهتر برای جنگ آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/withyashar/12857" target="_blank">📅 16:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12856">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">️سی‌ان‌ان: ترامپ به مشاورانش گفته  که برای تصمیم‌گیری در مورد امضای توافق احتمالی با تهران به چند روز زمان نیاز داره
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/12856" target="_blank">📅 15:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12855">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEZD1ZDSl0z5CY5ygiFGwxVFGZ7Vnn5IkqQQ-8zmEyNdKoBG6CmjJICFJbDs-rwB86ZNs6oI4BTtK8fFIY7FaUF6qMx8fmoiW0Tlc5Sm9fnmwSazxIZWGe97k7P8fFVzIEwJXWaJzpchZ-47sH9WGSIb-6SVc13PJdaK536Y2YhN6TsoUc5g9tFl_9s3V1xEDU2wKZNRlqzOtLGeHCP1-IffbMYGnBrnzAulTe-s83ibJd3MeXy-RLphyLqxNv3LVjbHSMZPxzLWeO8QAt1gZ_ABUOLGtdbS4orvp58VhN34VCF3TzvwEJBtZWVDR8CV6rwapgD5uTDJKftKW5Yukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری سوالات بی جواب تجمعات شبانه
😃
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/12855" target="_blank">📅 14:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12854">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froms@ti🍁🍂️</strong></div>
<div class="tg-text">سلام یاشار جان
من نامزدمو یه هفته پیش از دست دادم سرطان داشت
😔
تا لحظه ی اخر میگفت ناامید نباش یاشار گفته میزنه،تو دی ماه هم واقعا به سختی نجات پیدا  کردیم از تو خیابون .واقعا اگه ما پیروز نشیم من حس میکنم خون این همه ادم پایمال میشه،ما فقط به امید شما داریم زندگی میکنیم.هیچ وقت اخرین حرفشو تو ملاقات اخر یادم نمیره.فقط پیام دادم بگم  حتی امید اون ادمی که روی تخت بیمارستان هم نفس های اخرشو میکشه هم  هستی
🥺
خدا حفظت کنه واسه ما
🙏
❤️
🌺</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/12854" target="_blank">📅 14:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=olW2Gb_rGNmsCKuE6a3CoafzPWnHqFGnABoEd8QE__UNCKilYiy6zxfUnvgtL9ulCmeCsDSC8mjkrx_tXbe8Z3SENjSL73s-0lJca-zd3z-F_ZNEnNqMHg6rT4Tk5jcUpJ-Vtda2DWiYa0lkgpJN-4H_9F8a_yi77zryrmOLUCcsob9S_STQBDedV6jwCfC5E7UCmyFHZbLp1NYkwv4rAlIWNN4hG3dp5XslCc0DHFKLdWz0S9a-N87-v5YugQLQYr-IICfstsH8_r3_bpTUw-vrji3HZgoAyeYo-qAs1Ch_x45OW5e1WBUrgVwukVyVhHWyc1OhCh_NkIdARlcmiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=olW2Gb_rGNmsCKuE6a3CoafzPWnHqFGnABoEd8QE__UNCKilYiy6zxfUnvgtL9ulCmeCsDSC8mjkrx_tXbe8Z3SENjSL73s-0lJca-zd3z-F_ZNEnNqMHg6rT4Tk5jcUpJ-Vtda2DWiYa0lkgpJN-4H_9F8a_yi77zryrmOLUCcsob9S_STQBDedV6jwCfC5E7UCmyFHZbLp1NYkwv4rAlIWNN4hG3dp5XslCc0DHFKLdWz0S9a-N87-v5YugQLQYr-IICfstsH8_r3_bpTUw-vrji3HZgoAyeYo-qAs1Ch_x45OW5e1WBUrgVwukVyVhHWyc1OhCh_NkIdARlcmiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست ، وزیر دفاع آمریکا با لاتی‌ پر مانند مربیی که تیمش را به زمین میفرستد،  خطاب به نیروهای آمریکا روی ناو USS Boxer گفت:
«رئیس‌جمهور گفت: ایران یا می‌تواند راه درست را انتخاب کند یعنی پای میز مذاکره توافق کند یا با مردِ سمت چپ من طرف شود.»
«آن مردِ سمت چپ، اتفاقاً من بودم.»
«اما در واقع من نیستم…»
«شمایید.»
یعنی شما نیروهای نظامی آمریکا هستید.
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/12853" target="_blank">📅 14:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12852">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromomid.behroozi</strong></div>
<div class="tg-text">سلام یاشار عزیز من امشب عروسیمه امشب میزنه آماده باشم تو باغ مهمونا رو از قبل آماده کنم میزنه ؟؟
😂
😂</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12852" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بر اساس تحلیل نشریه اکونومیست، طرفین درگیر ممکن است بیش از هر زمان دیگری به یک توافق نزدیک شده باشند.
با این حال، این توافق جامع نخواهد بود و جنگ را برای همیشه پایان نخواهد داد.
این نشریه در ادامه توضیح می‌دهد که چگونه ملاحظات و بازی‌های سیاسی، عامل اصلی ارسال این پیام‌های ضدونقیض از سوی طرفین است
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/12851" target="_blank">📅 13:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیویورک تایمز: یکی از جدیدترین و شگفت‌انگیزترین عناصر پیش‌نویس توافق صلح ایران، یک صندوق سرمایه‌گذاری پیشنهادی برای ایران به مبلغ ۳۰۰ میلیارد دلار است.
ایران در ابتدا این موضوع را به عنوان غرامت برای خسارات جنگ (که آن را بین ۳۰۰ میلیارد تا ۱ تریلیون دلار تخمین می‌زند) مطرح کرد. طرف آمریکایی آن را به عنوان یک «صندوق سرمایه‌گذاری بین‌المللی» که به تسهیل آن کمک می‌کند، بازتعریف کرده است
یک چارچوب نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از استیو ویتکوف و جرد کوشنر نشأت گرفته است که پروژه‌های املاک و مستغلات تهران و یک ابزار سرمایه‌گذاری گسترده‌تر را به عنوان شیرین‌کننده‌های معامله مطرح کردند
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/12850" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12849">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان من گفتم فردا میگم کجا متن ها رو بفرستید دوبار هم در متن تاکیید کردم! پیغام هایی که الان دایرکت دادید بین پیغام های‌دیگه میره و از دست میره حتی نیمتونم بخونم
😟
چرا درک نمیکنید خیلی واضح گفتم</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/12849" target="_blank">📅 13:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12848">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/12848" target="_blank">📅 13:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=ePYGEpFlSmJeAbZ-7oPcF7fGMI18WlSEk3cVyKrmayoUOa85yTv3aKZ8jXvou5mEWDC4tnR6TYlE2j8_1T_vOpCc--Yu7Aw5wlYU__6Srnx9t0Co3iZetMLYMTVwfkoKsZlltukXLZOTxFsS-jMksGihNjCv_R8m0xhm60Ys1Xrq1Himd2kYhJVPsKJjdVbk3qn2z20gT8fBjM65Wc839pDzAemMRcD2M68TVAJBMmLhUVMZWhDXW7I7VzVYdr94jqdhVaJlamwe6FFMp_2IWbODXd5yxXqpSx_ZDw4ZqSfB4s1HNSXFphcjQdXyLCmwMzs7nPSgV1wgKMnAtttWX7XrPRnYnAam3t5O-lnLOp8IdYoQh6dZ_wTrrs0XLo4mNMs5bqYNjnom02O4-VWSJvScSzG7R1XKL3GJuIR0CwHP28tZ06Lz1I3mgEnDvYPt_DhgPPbrXjmcVFU7lGqPCRCo9NLPYGvKOU0VG_gidwaTVwtPadbUQFCFm6Jk87-MPeU9jCD5YT34v9mRyXgOAbQ2dLGe4PevTM1DjUQ0_F2-WrmtghTQSRVvZNbMmeer8dq-s3dK3S7KzNHP9VK9eo6YKeO1lVllD_szTnMWA0sTOe3STSWjFyd7RLV_ou1n_SkgclCPyuuzbqqeh2jNafHDu3wWp8gOUu-xFQxyhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=ePYGEpFlSmJeAbZ-7oPcF7fGMI18WlSEk3cVyKrmayoUOa85yTv3aKZ8jXvou5mEWDC4tnR6TYlE2j8_1T_vOpCc--Yu7Aw5wlYU__6Srnx9t0Co3iZetMLYMTVwfkoKsZlltukXLZOTxFsS-jMksGihNjCv_R8m0xhm60Ys1Xrq1Himd2kYhJVPsKJjdVbk3qn2z20gT8fBjM65Wc839pDzAemMRcD2M68TVAJBMmLhUVMZWhDXW7I7VzVYdr94jqdhVaJlamwe6FFMp_2IWbODXd5yxXqpSx_ZDw4ZqSfB4s1HNSXFphcjQdXyLCmwMzs7nPSgV1wgKMnAtttWX7XrPRnYnAam3t5O-lnLOp8IdYoQh6dZ_wTrrs0XLo4mNMs5bqYNjnom02O4-VWSJvScSzG7R1XKL3GJuIR0CwHP28tZ06Lz1I3mgEnDvYPt_DhgPPbrXjmcVFU7lGqPCRCo9NLPYGvKOU0VG_gidwaTVwtPadbUQFCFm6Jk87-MPeU9jCD5YT34v9mRyXgOAbQ2dLGe4PevTM1DjUQ0_F2-WrmtghTQSRVvZNbMmeer8dq-s3dK3S7KzNHP9VK9eo6YKeO1lVllD_szTnMWA0sTOe3STSWjFyd7RLV_ou1n_SkgclCPyuuzbqqeh2jNafHDu3wWp8gOUu-xFQxyhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر:
ایران امتیاز های خیلی قابل توجه، مادی  به ایالات متحده داده که قبلا میگفت غیر ممکنه
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/12847" target="_blank">📅 13:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فارس نیوز ، خطیب نماز جمعهٔ تهران: دشمن متوقف نیست، ما باید در مرز دانش و فناوری حرکت کنیم
حجت‌الاسلام ابوترابی: تعرض آمریکا در سحرگاه دیروز به نقطه‌ای در حاشیه فرودگاه بندرعباس که نه خسارت جانی داشت و نه خسارت مالی، اما تعرض به آسمان و زمین ایران بود. این تعرض از پایگاه هوایی آمریکا در منطقه انجام شد
@withyashar
🥴</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/12846" target="_blank">📅 13:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12845">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی رسمی و محترمانه صحبتهای خود را بنویسید  و امروز بر روی متن تمرکز کنید و فردا از ساعت ۱۰ صبح تا ۱۰ شب برای من ارسال کنید تا چکیده ای از تمام آنها را ارسال کنم و فقط کلام من نباشد. حتی شده یک کلمه از پیام هر شخص را برمیداریم و متنی باهم میسازیم که در خور باشد. پس از شما دعوت میکنم به این کمپین بپیوندید ،لطفا امروز و فردا از فرستادن دایرکتهای غیرمعمول بپرهیزید سوال بیشتری را نمیتوانم پاسخ بدهم متن کامل است هر صحبتی که دارید  در  همان متن بنویسید تا همه با هم متن پایانی را استوری،  کامنت ، دایرکت و ایمیل کنیم
🙌🏾
. شروع ارسال فردا ۱۰ صبح و آخرین مهلت ارسال برای من  فردا ۱۰ شب است.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/12845" target="_blank">📅 11:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تحلیل عوستاد رائفی پور :
آمریکایی‌ها نیروهای بیگانه فضایی هم کمک گرفتن
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/12844" target="_blank">📅 11:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12843">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/12843" target="_blank">📅 11:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسرائیل هیوم در گزارشی نوشت موساد در سال‌های اخیر شاخه‌ای محرمانه برای نزدیک‌تر کردن سقوط جمهوری اسلامی ایجاد کرده است. به گفته منابع آگاه، رییس موساد متقاعد شده است که اگر ترامپ با تهران توافق نکند و محاصره دریایی را ادامه دهد، جمهوری اسلامی تا پایان سال ۲۰۲۶ سقوط می‌کند.
ماموریت ابتدایی این شاخه که در سال ۲۰۲۱ و پس از آغاز ریاست داوید بارنیا بر موساد ایجاد شد، عملیات‌ هدفمند برای کنار زدن مقام‌های ارشد جمهوری اسلامی بود، اما به‌تدریج به بخشی از راهبرد گسترده‌تر موساد برای «تغییر رژیم» تبدیل شد.
رییس پیشین این شاخه به اسرائیل هیوم گفت موساد در گذشته بیشتر از طریق ترور افراد را حذف می‌کرد، اما اکنون افشای اطلاعات شرم‌آور یا آسیب‌زننده درباره مقام‌ها می‌تواند آن‌ها را از حلقه قدرت خارج کند؛ روشی که به گفته او «ارزان‌تر و ساده‌تر از عملیات ترور» است.، مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/12842" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام : ادعا: تلویزیون دولتی ایران ادعا کرد که نیروهای ایرانی یک هواپیمای آمریکایی را در نزدیکی بوشهر سرنگون کرده‌اند. نادرست.
حقیقت: هیچ هواپیمای آمریکایی سرنگون نشده است. تمام دارایی‌های هوایی ایالات متحده در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/12841" target="_blank">📅 10:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv_tjClMxaARchz8spPiXRCNswaJ823wXN-78iRDqzcfvqQYH7Ewfb0ajB7tTiUyxfEMYGuQvdWuruh2VZ5U5b6booJ9DtDeZNeqTLaAQV2Qbkq_Ot9joY9Zm8-eXwfy6KfJUtM8qTBqHAwRXFwB6pTOLSP9gUjRABDys0_2JaqTX4BY9YUehjVhqm6JXIEggOKEnLXB9C3hH5DUHjEhzaZTK-yPbJRjYKICORd9KydKPHclX9vPq16bTM4Mkf4zaVby8J6jXqc1Wa-MxEeEXxPBU96-EmAzkejn4fyKpAJZUgJ3cT3dF71-vU_DhU5GwuRj8IAmfEOfMy3b51Z6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید علی کریمی و حمایت از شاهزاده رضا پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/12840" target="_blank">📅 10:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12839">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس: آنچه امروز جمهوری ایران دنبال می‌کند، مدیریت هوشمند تنگه هرمز است.
اعمال کنترل و ترتیبات ایران در تنگه هرمز ماهیت دائمی دارد و بی‌تردید مقطعی نیست.
ایران قصد ندارد اورانیوم غنی شده خود را به کشور ثالث منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/12839" target="_blank">📅 09:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12838">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رویترز: ترامپ در شرایطی به دنبال پایان دادن به جنگ با ایران است که همزمان با دو فشار متضاد مواجه شده است. از یک سو افزایش قیمت انرژی و نگرانی از تبعات اقتصادی جنگ، کاخ سفید را به سمت دستیابی به توافق سوق می‌دهد و از سوی دیگر بخشی از جمهوری‌خواهان و متحدان سیاسی ترامپ خواهان ادامه فشار نظامی و جلوگیری از هرگونه امتیازدهی به جمهوری اسلامی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/12838" target="_blank">📅 09:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a0d910cb.mp4?token=BimHHU-2bY61dO5XgvDsykr3X1IDjspSUChz9btFELRshE02XwqVhmIENkntUaYKUU4nvLL_zUZdtuTrkn4LnyIgl7IhPBMuEq-0ToIxMmDrnl5XinHzVghltG3YXo5S13NoByC9mmW0b3y3bS-Oo0deVQHZjmUZjnLPfz5PO8QSdFLGOzNhs4Y9e1aigAT8OJUB9C-N_0SivsaJ-2IM1P-Ae8spQXqbl4a3A0GzKDHMIdU7SuwGATEItZ0nu7z-6y6gdj9Qd3O79j08tBw7KTr6Z4RWLJGSFvsu4IPQl4TkwH2FHN9eIAgv3FUeOdlEPSNZacglvUEmwYg_y2alpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a0d910cb.mp4?token=BimHHU-2bY61dO5XgvDsykr3X1IDjspSUChz9btFELRshE02XwqVhmIENkntUaYKUU4nvLL_zUZdtuTrkn4LnyIgl7IhPBMuEq-0ToIxMmDrnl5XinHzVghltG3YXo5S13NoByC9mmW0b3y3bS-Oo0deVQHZjmUZjnLPfz5PO8QSdFLGOzNhs4Y9e1aigAT8OJUB9C-N_0SivsaJ-2IM1P-Ae8spQXqbl4a3A0GzKDHMIdU7SuwGATEItZ0nu7z-6y6gdj9Qd3O79j08tBw7KTr6Z4RWLJGSFvsu4IPQl4TkwH2FHN9eIAgv3FUeOdlEPSNZacglvUEmwYg_y2alpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس: دستاوردهای ما علیه ایران قابل توجه بوده است
جی‌ دی ونس، معاون رئیس‌جمهور آمریکا: اگر به آنچه تاکنون به دست آورده‌ ایم نگاه کنید ،در صورتی که بتوانیم به یک توافق نهایی برسیم ،در حال بازگشایی تنگه هرمز هستیم.
ما پیش‌تر توان نظامی متعارف آنها( ایران) را به‌ شدت تضعیف کرده‌ ایم و در موقعیتی قرار داریم که میتوانیم برنامه هسته‌ ای‌ شان را به‌ طور قابل توجهی عقب بیندازیم،نه فقط در دوره این رئیس‌ جمهور، بلکه در بلندمدت.
این یک اتفاق بسیار، بسیار خوب برای مردم آمریکا است.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/12837" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مقام ایرانی به وال استریت ژورنال: تهران نگرانه که اسرائیل، آمریکا رو از مذاکرات خارج کنه
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/12836" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9915e2bfef.mp4?token=MG3B4AplDqjpc0mnYJ-AYMSb9A0Wl50Jkh1AKgCPkci_Fve86bGYH4bWBhZXo0SPBl-0JipvPl_10xyOtF0ScDdxqIP33P_83QTXV4Z2oYPcLmby6FYZd90TMn766ribbMFXFwPfij6veNpwHHPqGmEHnOPbSh3F-HEoYDjZ1mJW7wQ-JlzD3AeuJhpZeE67ml_08Hl8tQNHC3lsBSwKMb-xy0mSNrh-pEOUON6pl_fPZPsx7VG6_RdxFFMl8uz_qdrCWOKAjikAjaFqI9zB3bfvJrE8zvZhGXLtJlboXg2NmSCkHVZlw-8fjfsSXNuxdU-D5UldivbFrCgiv1-AZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9915e2bfef.mp4?token=MG3B4AplDqjpc0mnYJ-AYMSb9A0Wl50Jkh1AKgCPkci_Fve86bGYH4bWBhZXo0SPBl-0JipvPl_10xyOtF0ScDdxqIP33P_83QTXV4Z2oYPcLmby6FYZd90TMn766ribbMFXFwPfij6veNpwHHPqGmEHnOPbSh3F-HEoYDjZ1mJW7wQ-JlzD3AeuJhpZeE67ml_08Hl8tQNHC3lsBSwKMb-xy0mSNrh-pEOUON6pl_fPZPsx7VG6_RdxFFMl8uz_qdrCWOKAjikAjaFqI9zB3bfvJrE8zvZhGXLtJlboXg2NmSCkHVZlw-8fjfsSXNuxdU-D5UldivbFrCgiv1-AZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پودر شدن موشلی ۹۰ روزه شد
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/12835" target="_blank">📅 09:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">https://t.me/boost/withyashar  بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/12834" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12833">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/12833" target="_blank">📅 00:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12832">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیکتاتور مهربون ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/12832" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12831">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">دیکتاتور مهربون
ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/12831" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12830">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پدافند اصفهان فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/12830" target="_blank">📅 00:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12829">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم : یک منبع نظامی رهگیری پهپاد آمریکایی را تایید کرد
به گفته این منبع نظامی، این رهگیری در اطراف بوشهر از طریق شلیک موشک پدافندی به سمت این پهپاد انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/12829" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12828">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">درود بر یاشار جان از جم پیام میدم حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد  صدای مهیب و خوبی بود @withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/12828" target="_blank">📅 00:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12827">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407ae75cd1.mp4?token=ccHXDHr9KchtTvk3ixwRm69ouqV6FOXqfxwvsfpnOd53LKSkgxxcArG1ut64RDnyW9WoNDJtJlvIKqmFDxSySaPrie7HVMX4zVF4ZDINXIFwqpYwHgRKelE7nZN3Hk4HTYgOZSQA3i-8TL3oS_sVHDCEIHgxhdGccbT85MYFITcL0ILODYw1PIFo1UVnGoOJRWsIJZ4OCuMoVGqSVpSppd_SeaFdZuNewaC8_5oluVPmKpL00JTnh6w3g2I2D5fXY5hi_El7HLeB2ckqEsQwxnVOXbM-12uL-UxvNfmIe9OVMR5JKxkN2e5U4dxvEtQG84bnktuxLRtTBr2r9hvGSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407ae75cd1.mp4?token=ccHXDHr9KchtTvk3ixwRm69ouqV6FOXqfxwvsfpnOd53LKSkgxxcArG1ut64RDnyW9WoNDJtJlvIKqmFDxSySaPrie7HVMX4zVF4ZDINXIFwqpYwHgRKelE7nZN3Hk4HTYgOZSQA3i-8TL3oS_sVHDCEIHgxhdGccbT85MYFITcL0ILODYw1PIFo1UVnGoOJRWsIJZ4OCuMoVGqSVpSppd_SeaFdZuNewaC8_5oluVPmKpL00JTnh6w3g2I2D5fXY5hi_El7HLeB2ckqEsQwxnVOXbM-12uL-UxvNfmIe9OVMR5JKxkN2e5U4dxvEtQG84bnktuxLRtTBr2r9hvGSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آنها مذاکره‌کنندگان بسیار خوبی هستند آنها زیرک‌اند اما ما همه کارت‌ها را در دست داریم، چون آنها را از نظر نظامی شکست داده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/12827" target="_blank">📅 23:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12826">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivitUi1TDf78BO3X8KRpG_77mtpibffKNhAvscB1Y5EUkO4STb3rVq8vpOQ6A1XIy5P7njR8Qbzst7vAfjntU8e9ZPdAjE8i6JeHq6FgaCnGCjbYxIrVj55qQ2djuO62LYUNOs9palhWc9WiUKlOlosu-0N2H-aA-jqTNoSjFry8d1nG3feWBHBootpZ6Pv4quw8jkpUWXg_g8-UMDPPjgfjHbBH-TH6LkzN5osBfjB2-4CvcScFVPs_rOZ7JD9D8rlPwK6fINo1N-m7LCBq6KYNm_GJzeaClbM_Tw7TWnAnwgDakREsLYvXjvQiVEIIPJvsop5vk--08mDYKn5WKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه CNN:  تصاویر ماهواره ای نشان میدهد ایران به سرعت در حال بیرون کشیدن زرادخانه موشکی عظیم خود از زیرِ زمین است
.
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/12826" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12825">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ویو از کانال میلیونی ‌بیشتره، ری اکشن از کانال پوشاک زیر کمتر
😕
بد میگین ما ایرانیم چه کاری ازمون برم یاد بکنیم برات !!! خوب اسمت که نمی افته کاملا مخفیه همه پستا و ری اکشن بده دست آدم به کار بره…</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12825" target="_blank">📅 23:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12824">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال‌های وابسته به محور شیعه ادعا می‌کنند که ۴ کشتی تجاری آمریکایی پس از تلاش برای عبور از تنگه هرمز بدون اجازه ایران، توسط سپاه پاسداران ایران مورد حمله قرار گرفته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/12824" target="_blank">📅 23:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12823">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فارس:  دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
بامداد امروز هم پس از تعرض دشمن یه مناطق شرقی بندرعباس پایگاه مبدأ این تجاوز مورد هدف نیروهای مسلح جمهوری اسلامی قرار گرفت.
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/12823" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12822">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رسانه های عبری : گزارشهای رسمی از تبادل آتش بین ایران و آمریکا در تنگه هرمز خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/12822" target="_blank">📅 23:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12821">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسی
💥
یااااا موسیییی</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/12821" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12820">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه های عبری : گزارشهای رسمی از تبادل آتش بین ایران و آمریکا در تنگه هرمز خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/12820" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12819">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایلنا: شلیک اخطار نیروی دریایی به چهار شناور
نیروی دریایی در نزدیکی تنگه هرمز به ۴ فروند شناور خاطی شلیک اخطار انجام داد. این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/12819" target="_blank">📅 23:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12818">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رسانه های عبری : گزارش‌های اولیه: موشک‌های کروز «ابومهدی المهندس» از ایران به سمت کشتی‌های آمریکایی در منطقه تنگه هرمز شلیک شدند.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12818" target="_blank">📅 23:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12817">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">درود بر یاشار جان از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/12817" target="_blank">📅 23:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12816">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتاق جنگ با شما : هرمزگان و بوشهر هم صدای انفجار میاد
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12816" target="_blank">📅 23:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12815">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با شما :  انفجار تو علامردشت فارس  بوده
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12815" target="_blank">📅 23:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12814">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اتاق جنگ با شما : یاشار مثل اینکه مرز بین استان فارس و بندر عباس و بوشهر رو زدن
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12814" target="_blank">📅 23:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترور مامور فراجا در ایرانشهر
ساعتی قبل افرادی مسلح به سمت مامور انتظامی شهرستان ایرانشهر که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی کردند که استوار دوم «عیسی عباسی» کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/12813" target="_blank">📅 23:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12812">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارشگر: ترامپ گفت که می‌تواند عمان را منفجر کند. آیا شما برنامه‌ای برای یک جنگ جدید با عمان دارید؟  اسکات بسنت:  فکر می‌کنم ترامپ می‌خواست بر آزادی کشتیرانی در تنگه تأکید کند. سفیر عمان به من اطمینان داد که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.…</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/12812" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12811">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b307799edc.mp4?token=NZjWZMiEJHdT7gA2EFaFctpgNB8HWt5Gpfu4ZMe0TqY45hcDkW1Li7CG2CmCmwRYtTJG3xWy3dZMv6wKYgQklXIWp4u_gB6kXJU1e77Uvoaid0ruya3hUaYZXd_LQggS1VNxduQi-RsW0wrd4_b8DTj-caIgC1Fn0Dsy1vvcZPdgUUk8Ognc-NhsXOxHf0lyB1TuskFHAlLDhaNu_af4yVIqj1bXRX1Tp2gtUfFyLAOa9G5d_-LQDf4rPPrdg1Omt2R1Go7iOCF07pbLprdyRkxdRagRS22w47tRGIK2BzVEiC4PMvbA18hzUPTZJToZ5Gdt6TTs4vYdmS2dAaGu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b307799edc.mp4?token=NZjWZMiEJHdT7gA2EFaFctpgNB8HWt5Gpfu4ZMe0TqY45hcDkW1Li7CG2CmCmwRYtTJG3xWy3dZMv6wKYgQklXIWp4u_gB6kXJU1e77Uvoaid0ruya3hUaYZXd_LQggS1VNxduQi-RsW0wrd4_b8DTj-caIgC1Fn0Dsy1vvcZPdgUUk8Ognc-NhsXOxHf0lyB1TuskFHAlLDhaNu_af4yVIqj1bXRX1Tp2gtUfFyLAOa9G5d_-LQDf4rPPrdg1Omt2R1Go7iOCF07pbLprdyRkxdRagRS22w47tRGIK2BzVEiC4PMvbA18hzUPTZJToZ5Gdt6TTs4vYdmS2dAaGu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: ترامپ گفت که می‌تواند عمان را منفجر کند. آیا شما برنامه‌ای برای یک جنگ جدید با عمان دارید؟
اسکات بسنت:
فکر می‌کنم ترامپ می‌خواست بر آزادی کشتیرانی در تنگه تأکید کند.
سفیر عمان به من اطمینان داد که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/12811" target="_blank">📅 22:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : موج مکزیکی رو میبینید چقدر زیباست ؟
😍
🌊</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/12810" target="_blank">📅 21:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12809">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای سی‌ان‌ان:ترامپ در‌هر حالت  قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/12809" target="_blank">📅 21:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ادعای تسنیم: یک منبع نزدیک به تیم مذاکره‌کننده گفت بر خلاف ادعای برخی منابع غربی مبنی بر اینکه متن اصطلاحاً «یادداشت تفاهم» میان ایران و آمریکا نهایی شده و فقط منتظر اعلام دو طرف است، این موضوع واقعیت ندارد و هنوز متن قطعی نشده است.
وی افزود: ایران تا این لحظه به میانجی پاکستانی اعلام نهایی شدن متن را انجام نداده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/12808" target="_blank">📅 21:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12807">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">: NBC ادعای
آمریکا و ایران سه روز پیش تو دوحه به توافق رسیدن، ولی فعلا اعلامش نمیکنن
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/12807" target="_blank">📅 21:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfpDAj6gQR3g01g-9jsO4Egh49xjsaGJBaZK-gyLXiSYaqWrbj0_-mvLbvVJZVYXKnF04Js4g-a77Sq25kHWGMvMWBz1gD9fTakeNMHp1JtV3vQQ1dDqOmnfizbu6Je2bv4Ezy-6ZYK6OUpokFRjB1irD8nnDBeSIYZbTbcR8DuXjYJkCpN4fx4RYVsOZGfbFygmv-sqkiJCh078bW-eNVvj_nWkq-ReIE6wnUzEN1jC27DP7ylhYhPn36Pchyvzp5cYAWdyHIgYUORoSulaeAA9Hn0IGCNf8p7o8hdmz7jXd9YH_GQs-pBHSAYfFmoovE0UTR3w7RTdET5NwnoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDIkXraHZ8YBPlmZ9hfTvyc0ILEdr3-XWvp9hFQssr5Y0uOrD7iumpeRO4sE_VUQsjG8kI13i19qDXU2sS10C0VzaEtEbtbVYcsRLgvbXdYNx5CzD3-WWf8hSmQUQKLGXMO8201XgbuYK6kROZWhqahQBXjjNwAbrB2I8mv2F2V8aa2qH7gSjrJzlLie99lpEUNtH6_O6EFHO_sT461rhx3SfRJCidYm3NIWX_GdWPJgmAc1CzV1IFOjXdxL0DOOkmLAT1LdeTM5Q5ASjIcy6KqrRZvf6K0akzE4J4TMjcMQ99XIglmv2ID8Te3l2b_k3iIIMUn0LCMYbPwsYcYBAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتاق جنگ با شما : تو ساحل انزلی ساعتی پیش یه کشتی وسط دریا یهو آتیش گرفت هی منفجر میشه ، ممکنه بار جدید مهمات از روسیه بوده باشه
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/12805" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/12804" target="_blank">📅 20:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12803">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://www.ecolo.org/documents/documents_in_english/ramsar-natural-radioactivity/ramsar.html</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12803" target="_blank">📅 20:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12802">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">آقا یاشار سلام خسته نباشی
❤️
رامسر الان صدای جنگنده اومد یدونه بود نسبت به جنگ خیلی صداش زودتر تموم شد ولی جنگنده بود
پریروزم همین صدا اومد همینقدم بود محلیا میگفتن داره میره سمت روسیه</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/12802" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">@withyashar
😃
وضعیت سیکیم خیاری</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/12801" target="_blank">📅 20:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آمریکا ۲ شرکت هواپیمایی ایران را تحریم کرد
وزیر خزانه‌داری آمریکا نوشت: دسترسی ۲ شرکت هواپیمایی ایران به نقاط فرود، سوخت‌گیری و فروش بلیت مسدود خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/12800" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع اسرائیلی: رهبر ایران، مجتبی خامنه‌ای، این توافق را تأیید نکرده است، و بنابراین ترامپ نیز آن را تأیید نکرده است. قالیباف، رئیس مجلس و عراقچی، وزیر امور خارجه، حتی اگر چارچوب را پذیرفته باشند، مجاز نیستند؛ تصمیم توسط رهبر گرفته می‌شود. ما نمی‌دانیم که آیا هیچ یک از طرفین این توافق را تأیید کرده‌اند یا خیر. اختلافات هنوز هم وجود دارد، حداقل طبق آخرین به‌روزرسانی که اسرائیل دریافت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/12799" target="_blank">📅 18:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌های رفت و آمد به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/12798" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:  اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد. ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم. ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در…</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/12797" target="_blank">📅 17:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900d5bba51.mp4?token=nSF6Ik19HNCHZl0mQhnjDr0KyuiATa2t-mxltOkMpSgSbrZu10f9zNdAAKfG-XW7xHva-Q2x3ek-ikjP2YqI4Q_Np9AuqFFjlTyYIxHeQhAUwgPL8FtMNPR-pNEIwSEpj0bOen8iARASq1up3BiuUHaSaNwvkeKqsZIx2EooZL_L2nUZNoiri5j1SALKVO-dngKsHTDjUx6OcmScmrhUcsOvYnMgmScYuFHycFB7jbMrTttd2guwawlHpSIIszQLiPBDsddx1Y0NkhMZ8N3U9fer3i-40iA3aLDpW9-o8COW6m5rxMLWFRHU4abe7TL3UWsgR3gkLFuO4yD1wDclpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900d5bba51.mp4?token=nSF6Ik19HNCHZl0mQhnjDr0KyuiATa2t-mxltOkMpSgSbrZu10f9zNdAAKfG-XW7xHva-Q2x3ek-ikjP2YqI4Q_Np9AuqFFjlTyYIxHeQhAUwgPL8FtMNPR-pNEIwSEpj0bOen8iARASq1up3BiuUHaSaNwvkeKqsZIx2EooZL_L2nUZNoiri5j1SALKVO-dngKsHTDjUx6OcmScmrhUcsOvYnMgmScYuFHycFB7jbMrTttd2guwawlHpSIIszQLiPBDsddx1Y0NkhMZ8N3U9fer3i-40iA3aLDpW9-o8COW6m5rxMLWFRHU4abe7TL3UWsgR3gkLFuO4yD1wDclpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل کنترل ۶۰٪ از نوار غزه را در دست دارد، دستور من حرکت به سمت ۷۰٪ است. با این شروع خواهیم کرد.
ما در فرایندی هستیم که می‌توانیم قدرت خود را در جهات مختلف به کار بگیریم.
ما همچنان باید بر حزب‌الله فشار وارد کنیم؛ در حال حاضر با حماس درگیر هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/12796" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو:
ما باید ماموریت در ایران را تکمیل کنیم و من تقریباً هر روز در این مورد با ترامپ صحبت می‌کنم.
@withyashar
یاشار : من هم تقریباً زیر تمام پستهاش کامنت گذاشتم بیبی جون، فینیش د جاب</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/12795" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روسیه: ترامپ با انتقال اورانیوم غنی‌شده ایران به مسکو موافقت نکرد
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/12794" target="_blank">📅 17:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیغام فیکی از ترامپ که از یک پیج فیک ایکس است داره میچرخه. ترامپ هیچ پیجی در شبکه ایکس یا توییتر ندارد و فقط در تروسوشال پست میگذارد. این مسئله رو دقت کنید.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/12793" target="_blank">📅 17:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12792">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ابوترابی، نماینده مجلس: آمریکا بعد از جام جهانی و انتخابات کنگره دوباره حمله می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/12792" target="_blank">📅 17:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12791">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سیتنا: تا الان تمرکز ۹۱ درصدی ترافیک اینترنت تو تهران بوده و بازگشت توزیع عادی پهنای باند، زمان‌بره.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/12791" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuQS_-ntwUKGQLBqUI00hDfQ2hssGY-HKyqbOjPhgrgLs1QdFLXGR7GFaKhB0Ubyk0n3OGo7IjG4xZY5W5MQKjPRhh1YMVHxp0Cm9ABy7qjvg3qCgkc1pbkEmPV3rPgm0i2LHlGQ4ryrLvoPUf0kr0qfdgAoTk5_8SeC_BLOZ1wkrQWr-6UhPFFgkZp-eS6h_pajObGtPW7YiWQfBfKoXT0_dBkQiu43AchV9vrrFTFz0JcdK5ne5zV-CGT72I3cBF5Zn7RdfmF_mDQZUNro3ze4KU8et3n4PeDsJGt7F4D36w14xLmT-vpznlUZaUaR_QLGlNr-nkNcFyjT5yeI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست
:
مقامات دولت ترامپ، اداره حکاکی و چاپ را تحت فشار قرار داده‌اند تا یک اسکناس ۲۵۰ دلاری با تصویر رئیس‌جمهور طراحی کند، که این اولین بار در بیش از ۱۵۰ سال گذشته است که تصویر یک فرد زنده روی پول رایج آمریکا چاپ می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/12790" target="_blank">📅 16:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل گفت که ارتش این کشور با قدرت به حملات علیه حزب‌الله ادامه خواهد داد.
نتانیاهو اضافه کرد که نیروهای اسرائیل از رودخانه لیتانی در جنوب لبنان عبور کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12789" target="_blank">📅 16:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12788">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری والا به نقل از یک مقام امنیتی اسرائیل: یکی از اهداف در بیروت یک فرمانده ارشد ایرانی بوده است
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/12788" target="_blank">📅 15:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سنتکام طی بیانیه‌ای ایران را به نقض فاحش آتش‌بس متهم کرد
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/12787" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12786">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qckJM9RznYzTQL6lAJrnLD7dvAchzzQAhclMraVoAQTQEMjBMs_aFLt7U4cgWy5tcBfMR4dgloFtRru09LIbu0DdS3bsjjldUfUbZb37zUSfUI04DSnGKZ25XcpGV9treVNzeeYryDYgGK8s6xgVKGfXTe3N0ULrK5aA8rwoqJS6_40y8FwYI4i4Ns1fTWnTrlwFo6XO3F9rNy43tt3bFuAgKf-g5shWXnBmPEYYvcJj8PJCtp5Rh1NSZMNLCCSWhiyBa2M2vjnX_1YY7JkRpzjfDKnrl-hLSzVdTemLKvhBp82iz3cPNodGF3IvaBb_TPVm7xkaGwF1ED0HZjyeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های عبری : «علی الحسینی»، مسئول موشکی حزب‌الله در یگان امام حسین به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/12786" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12785">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گزارش ان. بی. سی نیوز، پس از ارتش اسرائیل، سنتکام فرماندهی مرکزی آمریکا هم بانک اهداف خود در ایران را به روزرسانی کرد و لیستی از جدید از اهداف را تهیه کرد. هدف‌های راحت‌تر مثل رادارهای ثابت، باندها و هواپیماها تا حد زیادی قبلا زده شدن. چیزهایی که مونده بیشتر زیرزمینی، پراکنده یا سیارن و بدون شناسایی دقیق که ادامه درگیری رو سخت‌تر کرده
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/12785" target="_blank">📅 14:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12784">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvYR9TtRoUOjfZ0xQ13VQrVw-ulp9KNMBP5hhiJbdq8qGxAbxEXkzX6DB3dvVLGD43O2HPUh27VRU9Eyxsa3B0sKb5Ygiv_cFXgiNis3yb5LtbwCEIAo0jbEmQ5KryvgJvladpSA2Jpbre7bAe2ZPD6aHpCsKlSUEGGXVDSIQTUuPCCKXAMpEs6kgiP_ge0eUxrJHIYHOcAhL4obEGeXvNyvjpWVqp67n9xtegNuaR-C8gGrKSKbrYOTbpc74NwfKIlhkBkIApH_BmnaX02GzXXl0xUBlP2HUf81ofKihmevQIOeC2XG6jtKDpgvYnsI-cc_1aCnalVMJ5Bnpw1o6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک Ai موشتبی رو تمدید کردن و موفق شد یه متن طولانی برای سالگرد مجلس بده ، از خالیباف تشکر کرده و به امریکام گفته شیطان بزرگ همین یه امضا بچه ۴ ساله هم با پاورپینت انداختن اون زیر
🤣
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/12784" target="_blank">📅 14:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12783">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4n7fp8Xlt-naUOIzdJ7CBfzVR-hwhh_j1yZnDpOPZf--6LvjmuowC4aBZPfg8r7wuGDAMNqDh4WFpc4w6HA3nEjzGMPnWBlhH3tJHz7k3ZAU3Rt551y95ERmI_Hirkm__1J8Cv8QvpRBVg6gz4vwIkhIRNjpofOAlA2EIvdjCvKw2kA5XpAhOYztogVMEHdcUnSyBZFnQayxdawy0pZ770i6peA50JALpH7JpSX0xU2NIn-qEeGvjsDMiBvbC1pSlA46sC2G0-u6xKA-UFXKLd-kDJmrLkfyzQCAKVp5RCpD9kEdXuPJRaeAgBKimFR0O86wgQN8-XI3GVe_aEaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«روزنامه وال‌استریت ژورنال دیروز گزارش داد که ایران برای دور زدن تحریم‌ها و محاصره آمریکا، از سازوکاری موسوم به انتقال کشتی‌به‌کشتی(Ship-to-Ship) استفاده می‌کند؛ به این صورت که کشتی‌های تحریم‌شده حامل نفت ایران، پیش از ارسال محموله به چین، بار خود را در دریا به کشتی دیگری منتقل می‌کنند.»
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/12783" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12782">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMjgzuFtoR8E_3HhYFA07SBc0OYnDpg8F4H-ceWQxCJzblna_mLK6LnFz9dBsBgFC-cxcUeSjQIJbKoNquYRJ4dYt5vMVtsyBWKyO9z1NgwFZq8X7kLUHyh1Qk2HpEcoHRduAP_1w4V5-McXoUa22HQiB410wa7e1dgdrpZCvyT12r7Vchwu6-temLK7JTJyGX2_YvlqI29rR-XetE9pQb4MtweQmp8rz8X_-EGNT0h2f3NMGJd5TE3ZEGvW0hfj-BrC8XTvLD-9r36eHjjCEr2GH83Zr_SFcYem8AoqepkzqSdBQv4h7NtG9AM6QTV_2XpevFoRU3sfIH302yFShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دقایقی پیش مجدداً دستور تخلیه فوری کل جنوب لبنان را صادر کرد!
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/12782" target="_blank">📅 12:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12781">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مقام‌های آمریکایی گفتند جمهوری اسلامی چهار پهپاد انتحاری را به سمت کشتی‌های آمریکایی و تجاری شلیک کرد، اما جنگنده‌های آمریکا آن‌ها را سرنگون کردند. به گفته این مقام‌ها، جنگنده‌های اف-۱۸ آمریکا همچنین پیش از پرواز پنجمین پهپاد، واحد کنترل زمینی جمهوری اسلامی را در بندرعباس منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/12781" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12780">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/12780" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12779">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOWgJA1L7vdRfpYF3SRZj1QjD2GD_d6Lcz-dNiQCU7GdkKhzp5D0_UUKXaHq0rK5fEv6nMrKvwel-k8HXEtIcsIHDUkBUCgYQKr_J_X9LPS7_cuNbipIZB5j0chevBfTyxOZwmpH2KYDk2LmiaoRlWuMLe5iVavvW-JHFwC1F7HyQVBVtnn_1bDStQgKcUoSI-46rqJOAIWDDn3ptq-Wm8qg7wnXHy6s67tq3a4nEkhqeVd8sWwKiceEfFYN-4RR5FuYJ8IiSGK48gx9LFOxvti7C_fM1mhXJb6MxaMzMtMwasYfB9ZF4NuCB4zpEOoxaB46Nc5rg7Fd4Vn_ilu60w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم ترافیک اینترنت بین‌الملل، تا ساعت ۷ و نیم صبح امروز به ۵۳ درصد حجم پیش از دی‌ماه ۱۴۰۴ رسیده است
@withyashar
حرفم که گفتم اینترنت فقط با رفتن اینا به حالت قبل بر‌میگرده هنوز پا برجاست !</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/12779" target="_blank">📅 11:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/12778" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGOzCH2YoKLEyIKz63jo-I8GOOHfWf9RWYm6W_9-SJQSOKqL2cz2UDLQRBiw4yoQWrcBE75qGYObWYNXjGFCwzlhmOzf7Su5_OTn_0e0FabP8QMCj9fXb-0x-6m5C9KZTkiGYAo2qgUKSJlp1_82XBZd-DCPW9rXzkIPsAXJzLu38jMLC4io9Ef3im_0ed6HUtWMaVL3l9vyMrI3JAa4aYHbGdZcq4b7RLCXnJwLHWMHg0AS0dghuwHqOhVRtv5Tzo25wsEOWdg0OPX_J59oyb3PhWXtooxRvnH8HnDCm_SsX_BNo0oOplqSPRNlw24pdial5js1RtAazFSKWrfRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
👏
👏</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/12777" target="_blank">📅 11:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENkN8aqlp3OL1k-eWXW4ckQm0IPzdQ0ko8rT9pV0AqSlVMgbw03Klvpb5jTvNELOFgJ2jt7zcdGeyrHHplabvftcbyfIdHSuoNpGl69bUJ1D2Rsa23EQjOj8uu77WsrYe9OeGdnUq2Gy4ITbjFwLIFkLgQJK4Pdug9hxr-8GPIjg9InPHa74HiB63Kn2T0dyL2IpQdSOkkjJReZWFTF2gMeq3r9eyWdnLvBqLmwksPtnfT-ydBZPBqBR0Vyllq8PX4QUKr5p8L1YxhJ_FvCsL5NnEuYiH40veGHFk8tJEfK2mw6gRrn08LrStD8MqXhAQlrLUEy66vOOWQwol0Ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12776" target="_blank">📅 10:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhKtRc40W-R7lxZShU0xZBx7dUkIGK9p6WOgxs9DfDAGbGf_1DSCiHJV3jsRIxAwWHl7ArMnxx4UtKMIAFGKtt2e-G_hqlaBS5znp44FhJEKXyW2hoqBnkGzjzhn8RU7B9_QZgKfwB4ySxEm1waajvzQYmvqWOGQ8NeskmYKjR3084XR6mV54BzSygyDKdDecFYJMGd31mMGSrEKY6UIXFDh_FWsah_d8b5QDnVLRQHyEGuLO5h2Xay4OYzGDb7LP2VouoNcP1mQe6tJc6KEKrvya14ysUxYXn_c6z8TijWHolSx95PDgOmAUFIe5LFrpRIvUNPd1BJ4lunBimni0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل، عزالدین البیک، فرمانده تیپ شمال غزه را به هااکت رساند
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/12775" target="_blank">📅 10:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUv6CcdeJlgmN5OrMC_TNAHndKN07pwAYRzmarSolTL_6zauA3ztMR9SMfdjz7W2nscAfIPPojE-zlfePpo0x5l_KptCfwc1vYD6Thhf0I0mho3ejFz6ZMtK9j1AtH4dM7_-9Fgl8-izuzhdFeumZfk4EyrIT5MU3fxOyC2S3nHxDgo4fLV-60K_D1h7cpwfnfo3Tf4T6Jo6aZkBcWy5rxMQVcE-tZ6lXUFjKTvTEgrVlw1j3fAdemUQOCAAu9Qb-Th11NC_DmhkuSYVfigqOn8p6ZkXZxq8358aYQxWvd4-ESuByCEFGXAzDc2uMh_XcKX_oJo1mVwXdl5pFbzSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
یک گاومیش آلبینو نادر در بنگلادش که به خاطر دسته موی بلوندش «دونالد ترامپ» لقب گرفته بود، پس از اینکه در فضای مجازی دیده شد، از قربانی شدن در عید قربان نجات یافت.
این گاومیش ۷۰۰ کیلوگرمی قبلاً فروخته شده بود، اما دولت به دلیل نگرانی‌های امنیتی و تجمع جمعیت برای دیدن آن، وارد عمل شد.
مقامات پول خریدار را بازگرداندند و حیوان را به باغ‌وحش داکا منتقل کردند.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/12774" target="_blank">📅 10:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12773">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس»  را به فهرست تحریم‌های خود اضافه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12773" target="_blank">📅 10:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12772">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=iykUNY5lal5B9sQNSRPtWKpwyt0DTSzG_JwTMHKbDzrvQR5iUWMcJWRpfsosCI_1GTiSyzq7IOIl6BLE0FGnJOn1wSm6oiOttMjNUn8Ns_lIQnIo1HOJx5IEJZ64fVyZveL7qjzmQ1MFqtx1g7UmJeGCFW9FHVC5A0VLGQWlNz47rfB7A93HEpUbgxi5wehlFBm8xdQXRqCBegkS6krjRsoifzhZcb6yFyN32_TnG2y2_cDxa6mYiaBXysoUv-lQLxKd_JSPIlzgqekT6DYtb40828mpb1IEplYE_4-yVodYMWFVrvAFGH0cmtJVAm_Xn7RG1jLPg0_dcHyXj3q2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6fdcea6c.mp4?token=iykUNY5lal5B9sQNSRPtWKpwyt0DTSzG_JwTMHKbDzrvQR5iUWMcJWRpfsosCI_1GTiSyzq7IOIl6BLE0FGnJOn1wSm6oiOttMjNUn8Ns_lIQnIo1HOJx5IEJZ64fVyZveL7qjzmQ1MFqtx1g7UmJeGCFW9FHVC5A0VLGQWlNz47rfB7A93HEpUbgxi5wehlFBm8xdQXRqCBegkS6krjRsoifzhZcb6yFyN32_TnG2y2_cDxa6mYiaBXysoUv-lQLxKd_JSPIlzgqekT6DYtb40828mpb1IEplYE_4-yVodYMWFVrvAFGH0cmtJVAm_Xn7RG1jLPg0_dcHyXj3q2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
رد موشک های ۳پا در امیدیه خوزستان که به سمت کویت میرفت
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/12772" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اکسیوس: ایران چهارتا پهپاد انتحاری  به سمت یک ناو نیروی دریایی آمریکا و یک کشتی تجاری پرتاب کرد  نیروهای آمریکایی پهپادها رو رهگیری کردن و همچنین یک واحد پرتاب پهپاد ایرانی دیگه رو روی زمین قبل از اینکه بتوانه شلیک کنه، هدف قرار دادن
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12771" target="_blank">📅 09:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12770">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فاکس نیوز: آمریکا یه ایستگاه کنترل زمینی ایران رو تو بندرعباس زده؛ همون جایی که قرار بوده یه پهپاد تهاجمی ازش بلند شه.
به گفتهٔ مقام‌های آمریکایی، چهار تا پهپاد انتحاری دیگه هم که تو تنگه هرمز تهدید محسوب می‌شدن، زده شدن.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/12770" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12769">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۳پا یک پایگاه هوایی آمریکایی را هدف قرار داد
روابط عمومی ۳پا طی اطلاعیه‌ای اعلام کرد:
به دنبال تعرض سحرگاه امروز آمریکا به نقطه‌ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/12769" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12768">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مقام آمریکایی به شبکه CBS نیوز گفت : آتش‌بس با ایران پس از حملات امشب همچنان در حال اجرا در نظر گرفته می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/12768" target="_blank">📅 03:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:   ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد @withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/12767" target="_blank">📅 03:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/12766" target="_blank">📅 03:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/12765" target="_blank">📅 03:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه. @withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/12764" target="_blank">📅 03:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/12763" target="_blank">📅 03:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ، به شبکه فاکس نیوز: مذاکره با ایران درباره کنار گذاشتن غبار هسته‌ای به دلیل تضاد در تصمیمات ایران، رفت و برگشت دارد تأسیسات هسته‌ای ایران تحت نظارت مداوم ۹ دوربین، ۲۴ ساعته قرار دارند. هرگونه تحرک ایرانی در داخل تأسیسات هسته‌ای با واکنش مستقیم نظامی…</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/12762" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8116492af1.mp4?token=d49atxmGSfDz2Ow20c8ds2beqvGHXSMzOsmpuA-jx1wped3X7-X7xzZtsTjzUUeXuhvpVALzIyWEpzKZfSjp2DLSH7NjJ2nEug4v7eRAO5YtBnqxCFKeszzWomk4riFjfmLYMfD0L0ASkDf5oPAnYjlznjQv4iPdc96p4_Fm_EIof8_BC1ia3h_N9dQHNQJnAK4MOlk2HL-7Vbrqc0BKqfpSgtUFFAHpE2O1ow_ye0MGanbQtZ9PdlzP728DwLdGcYQAOBoQiXEWO-KDo7tXmOJkpTy2i0RuWR5p0mSE06tvw8NijyOYDcZTwLYCcVpyaFIAHys69xrRAV-41uxxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8116492af1.mp4?token=d49atxmGSfDz2Ow20c8ds2beqvGHXSMzOsmpuA-jx1wped3X7-X7xzZtsTjzUUeXuhvpVALzIyWEpzKZfSjp2DLSH7NjJ2nEug4v7eRAO5YtBnqxCFKeszzWomk4riFjfmLYMfD0L0ASkDf5oPAnYjlznjQv4iPdc96p4_Fm_EIof8_BC1ia3h_N9dQHNQJnAK4MOlk2HL-7Vbrqc0BKqfpSgtUFFAHpE2O1ow_ye0MGanbQtZ9PdlzP728DwLdGcYQAOBoQiXEWO-KDo7tXmOJkpTy2i0RuWR5p0mSE06tvw8NijyOYDcZTwLYCcVpyaFIAHys69xrRAV-41uxxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی همکنون در آسمان اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/12761" target="_blank">📅 02:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9-qYjuc6qPDpnZehOBalVZ9dXVqwZWLyqlD8ekZN1FThcr3VTsIRHfEMEzIW3bBm_x-GVhiYba5SPiK138XrPNNQ2S3g9rDbNqyGQluN07hc2gnMuOCwseoqmFHgey13Q_QM4OZGEAlcr3D00TfjqIV0CD4aCe3DNvU-G79BBn2fBwrSQk58yh8afDcY_0PCL8ndLJ-0sZMH9vJZmK-9G_G0sD6x2mOyYatKdq3rUPYgCZr8r4g7b7Idl_z98EvTb-xi-Cuw57Psi8FPWb7eNqJYrgF5pKc6zfq4BWHEE8aTljcAhw0AtfbcGXp6-A5YW13dqZ02VxWUQC2zb9qzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«رویترز» به نقل از یک مقام آمریکایی گزارش داد:
ارتش آمریکا حملات هوایی جدیدی را علیه یک سایت نظامی ایران انجام داد که تهدیدی برای نیروها و ناوبری ما در تنگه هرمز محسوب می‌ شد
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/12760" target="_blank">📅 02:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارشات تأیید نشده از ترور سردار علی عظمایی، جانشین سردار علیرضا تنگسیری، فرمانده نیروی دریایی سپاه.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12759" target="_blank">📅 02:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12758" target="_blank">📅 02:43 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
